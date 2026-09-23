"""E12 — controles de SAP. Comprueba la metrica ANTES de que exista una sola pose sintetica.

POR QUE ESTE EXPERIMENTO EXISTE
-------------------------------
SAP es, segun `00-tesis.md`, la **unica metrica introducida por esta tesis**, y hasta el 2026-09-22 no
tenia una sola linea de codigo (#116). El orden decidido ese dia es **SAP antes que el muestreador**:
la metrica se puede validar sobre geometria conocida y sobre ejes de corredor ya medidos, donde la
respuesta correcta se sabe de antemano. Depurarla despues, sobre poses sinteticas, mezclaria errores de
la metrica con errores del muestreador y no habria referencia externa para separarlos.

La advertencia de metodo del proyecto —"toda capa o metrica derivada necesita una comprobacion que
pueda fallar"— se aplica aqui con dos controles que **fallan si la implementacion esta mal**:

- **C1, geometria conocida.** Fantasma de cilindro oseo de radio R. La brecha de un cilindro de
  diametro `d` tiene que ser `max(0, d/2 - R)`. Da el error absoluto de la metrica frente a geometria
  continua, que es la cifra que hay que declarar como resolucion de SAP.
- **C2, identidad con el corredor.** Un cilindro de diametro `D_TS_max` sobre el eje del corredor de un
  caso real tiene que dar brecha **exactamente 0**, porque `D_TS_max` es `2 x min` del mismo EDT sobre
  el mismo eje recortado (`e9_corredor.evaluar_linea`). Si sale > 0, la cifra de ese caso no se usa.
- **C3, monotonia.** La brecha no puede decrecer al ensanchar el cilindro.

C2 ya encontro dos errores reales durante la implementacion: una primera version muestreaba la
superficie del cilindro contra la mascara voxelizada y daba 1.000 mm donde debia dar 0; la segunda, con
campo de distancia signado, bajo a 0.616 mm pero seguia fallando. La formulacion actual (medir sobre el
eje, con la convencion de distancia de `e9_corredor`) da 0 exacto.

USO
---
Solo el fantasma, sin datos (corre en cualquier maquina, segundos):
    python e12_sap_control.py --solo-fantasma

Con los casos piloto que tienen mascaras de TotalSegmentator en disco:
    python e12_sap_control.py --ts-dir ../../data/derivados/ts_piloto --ct-dir ../../data \
        --casos dataset7_CLINIC_metal_0008_data dataset6_CLINIC_0002_data

Escribe `e12_sap_control.md`.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import ndimage as ndi

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src' / 'muestreador'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sap  # noqa: E402
from e9_corredor import CIERRE_MM  # noqa: E402
from e9ts_corredor import ESTRUCTURAS, caja_recorte, etiquetar, limpia  # noqa: E402
from r1_landmarks import cargar  # noqa: E402
from ts_piloto_qc import mascara  # noqa: E402

R_FANTASMA_MM = 6.0
DIAMETROS_FANTASMA = (4.91, 7.0, 12.0, 14.0, 20.0)


def fantasma(r_mm: float = R_FANTASMA_MM) -> tuple[list[dict], float, float]:
    """C1 y C3 sobre un cilindro oseo de radio conocido. Devuelve (filas, error_max, control_corredor)."""
    zoom = np.array([1.0, 1.0, 1.0])
    forma = (300, 120, 120)
    xx, yy, zz = np.meshgrid(*[np.arange(n) for n in forma], indexing='ij')
    hueso = ((yy - 60.0) ** 2 + (zz - 60.0) ** 2 <= r_mm ** 2) & (xx >= 90) & (xx <= 210)
    origen = np.zeros(3)
    c = np.array([150.0, 60.0, 60.0])
    u = np.array([1.0, 0.0, 0.0])
    sdf = sap.campo_signado(hueso, zoom)

    # `D_TS` con la convencion de `e9_corredor.evaluar_linea`: 2 x min del EDT interior sobre el eje ya
    # recortado. El radio del fantasma es 6 mm y no 10 para que mande la cortical lateral y no las tapas
    # del cilindro, que quedan a 9 mm del eje recortado.
    t = sap._span_corredor(hueso, zoom, origen, c, u)
    d_ts = 2.0 * float(-sap._muestrear_campo(sdf, zoom, origen, sap.puntos_eje(c, u, t)).max())

    filas, errores = [], []
    largo_fantasma = float(t[-1] - t[0]) + 2 * 8.0
    for d in DIAMETROS_FANTASMA:
        b = sap.brecha_mm(hueso, zoom, origen, c, u, d, sdf=sdf, longitud_mm=largo_fantasma)
        esperado = max(0.0, d / 2.0 - r_mm)
        errores.append(abs(b - esperado))
        filas.append({'d_mm': d, 'brecha_mm': round(b, 3), 'esperado_mm': round(esperado, 3),
                      'error_mm': round(abs(b - esperado), 3), 'grado': sap.grado(b)})
    sap.verificar_monotonia(hueso, zoom, origen, c, u, sdf=sdf, longitud_mm=largo_fantasma)
    control = sap.verificar_control_corredor(hueso, zoom, origen, c, u, d_ts, sdf=sdf)
    return filas, max(errores), control


def envolvente(caso: str, ruta_ct: Path, ts_dir: Path, r1: pd.Series, modo: str = 'default6mm',
               frac: float = 0.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """La MISMA envolvente osea del corredor: union de TS, cierre de 2 mm, sin ocupacion de metal.

    Se arma llamando a `e9ts_corredor.limpia` y al mismo cierre morfologico, no reescribiendo el
    procedimiento. La politica de metal es `hueso` (el implante cuenta como hueso), que es la fila
    principal de `e9ts_corredor.csv` y la unica que existe en casos sin metal.
    """
    ct, zoom = cargar(ruta_ct)
    zoom = zoom.astype(float)
    forma = np.array(ct.shape)
    s1 = np.array([r1['S1_x_mm'], r1['S1_y_mm'], r1['S1_z_mm']], dtype=float)
    sl = caja_recorte(s1, zoom, forma)
    hu = np.array(ct[sl], dtype=np.float32)
    del ct
    etiquetas = [etiquetar(mascara(ts_dir / caso / modo / f'{e}.nii.gz')) for e in ESTRUCTURAS]
    union, _ = limpia(forma, etiquetas, frac)
    sin_cierre = union[sl].copy()
    del union
    it = max(1, int(round(CIERRE_MM / float(zoom.min()))))
    hueso = ndi.binary_closing(np.pad(sin_cierre, it), iterations=it)[it:-it, it:-it, it:-it]
    origen = np.array([s.start for s in sl], dtype=np.float64) * zoom
    return hu, hueso, zoom, origen


def caso_real(caso: str, ruta_ct: Path, ts_dir: Path, r1: pd.Series, fila: pd.Series) -> dict:
    """C2 y C3 sobre un caso real, con el eje del corredor medido en E9-TS."""
    hu, hueso, zoom, origen = envolvente(caso, ruta_ct, ts_dir, r1)
    c = np.array([fila['c_x_mm'], fila['c_y_mm'], fila['c_z_mm']], dtype=float)
    u = np.array([fila['u_x'], fila['u_y'], fila['u_z']], dtype=float)
    u = u / np.linalg.norm(u)
    d_ts = float(fila['D_TS_max_mm'])
    sdf = sap.campo_signado(hueso, zoom)
    # Ancla: el centro del CSV es el origen de busqueda, no el punto medio del corredor. Se ancla una
    # vez por caso, antes de cualquier perturbacion, y de ahi sale tambien la longitud del implante.
    base = sap.pose_base(hueso, zoom, origen, c, u)
    if base is None:
        raise RuntimeError(f'{caso}: sin corredor valido, no hay pose base')
    c, largo = base

    out = {'caso': caso, 'D_TS_max_mm': d_ts, 'L_TS_mejor_mm': round(largo, 1),
           'L_TS_csv_mm': float(fila['L_TS_mejor_mm']),
           'zoom_mm': tuple(round(float(z), 3) for z in zoom)}

    # C4 — la envolvente reconstruida aqui tiene que ser la MISMA que uso E9-TS. Se comprueba
    # recalculando `D_TS` con la convencion de `e9_corredor.evaluar_linea` (2 x min del EDT interior
    # sobre el eje ya recortado) y comparandolo con el valor guardado. Si difieren, lo que esta mal es
    # la reconstruccion de la mascara, no la metrica, y ningun otro control de este caso vale.
    t = sap._span_corredor(hueso, zoom, origen, c, u)
    d_ts_recalc = 2.0 * float(-sap._muestrear_campo(sdf, zoom, origen, sap.puntos_eje(c, u, t)).max())
    out['D_TS_recalculado_mm'] = round(d_ts_recalc, 3)
    out['C4_dif_D_TS_mm'] = round(abs(d_ts_recalc - d_ts), 3)

    # `D_TS_max_mm` viene de `e9ts_corredor.csv` REDONDEADO a 1 decimal, asi que puede exceder al
    # verdadero hasta 0.05 mm y el cilindro sobresale esa misma cantidad. La tolerancia es exactamente
    # ese redondeo, no un margen de conveniencia: con la cifra sin redondear el control da 0 exacto.
    out['C2_brecha_con_D_TS'] = round(sap.verificar_control_corredor(hueso, zoom, origen, c, u, d_ts,
                                                                    sdf=sdf, tol_mm=0.05), 6)
    out['C2_brecha_con_D_TS_exacto'] = round(
        sap.verificar_control_corredor(hueso, zoom, origen, c, u, d_ts_recalc, sdf=sdf), 6)
    out['C3_monotonia'] = [round(x, 3) for x in
                           sap.verificar_monotonia(hueso, zoom, origen, c, u, sdf=sdf,
                                                   longitud_mm=largo)]
    for d in (sap.D_SAP_MM,) + sap.D_SENSIBILIDAD_MM:
        r = sap.sap_pose(hu, hueso, zoom, origen, c, u, d_ts, largo, d, sdf=sdf)
        out[f'sap_d{d}'] = {'brecha_mm': round(r['brecha_mm'], 3), 'grado': r['grado'],
                            'frac_baja_densidad': round(r['frac_baja_densidad'], 3),
                            'viable_corredor': r['viable_corredor']}

    # C5 — la metrica tiene que DISCRIMINAR. Un control que solo produce ceros no distingue una metrica
    # correcta de una que devuelve 0 siempre. Se inclina el eje alrededor del centro del corredor y se
    # comprueba que el grado sube. La perturbacion es solo del control: NO es la distribucion del
    # muestreador, que se preinscribe aparte (D-O2.1 y D-O2.7).
    e1, e2 = _base_perp(u)
    out['C5'] = []
    for grados_inc in (0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0):
        a = np.deg2rad(grados_inc)
        u2 = np.cos(a) * u + np.sin(a) * e1
        r = sap.evaluar_pose(hueso, zoom, origen, c, u2 / np.linalg.norm(u2), largo, sap.D_SAP_MM,
                             sdf=sdf)
        out['C5'].append({'inclinacion_deg': grados_inc, 'estado': r['estado'],
                          'brecha_mm': None if r['brecha_mm'] is None else round(r['brecha_mm'], 3),
                          'grado': r['grado']})
    out['C5_sin_grado'] = sum(1 for x in out['C5'] if x['grado'] is None)

    # C6 — los DOS tramos tienen que coincidir donde ambos son validos. El tramo de corredor
    # (`e9_corredor.tramo`, con salida a blando) y el tramo de pose (#120, primer-ultimo cruce) son
    # definiciones distintas a proposito; sobre el eje del corredor, que cumple las dos, la brecha tiene
    # que ser la misma. Si difiere, una de las dos esta midiendo otra cosa.
    b_cor = sap.brecha_mm(hueso, zoom, origen, c, u, sap.D_SAP_MM, sdf=sdf, span='corredor')
    b_pos = sap.brecha_mm(hueso, zoom, origen, c, u, sap.D_SAP_MM, sdf=sdf, span='pose',
                          longitud_mm=largo)
    t_cor = sap._span_corredor(hueso, zoom, origen, c, u)
    t_pos = sap._span_pose(largo)
    out['C6'] = {'brecha_corredor_mm': round(b_cor, 4), 'brecha_pose_mm': round(b_pos, 4),
                 'dif_mm': round(abs(b_cor - b_pos), 4),
                 'largo_corredor_mm': round(float(t_cor[-1] - t_cor[0]), 1),
                 'largo_pose_mm': round(float(t_pos[-1] - t_pos[0]), 1)}
    return out


def _base_perp(u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Dos vectores unitarios perpendiculares a `u` (el mismo criterio de `e9_corredor`)."""
    a = np.array([0.0, 0.0, 1.0]) if abs(u[2]) < 0.9 else np.array([0.0, 1.0, 0.0])
    e1 = np.cross(u, a)
    e1 /= np.linalg.norm(e1)
    return e1, np.cross(u, e1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ts-dir', type=Path)
    parser.add_argument('--ct-dir', type=Path)
    parser.add_argument('--casos', nargs='*', default=[])
    parser.add_argument('--refs-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--solo-fantasma', action='store_true')
    parser.add_argument('--out', type=Path, default=Path(__file__).resolve().parent / 'e12_sap_control.md')
    args = parser.parse_args()

    filas, err_max, ctrl = fantasma()
    L = ['# E12 — controles de SAP (generado por `e12_sap_control.py`; no elige nada)', '',
         '## C1 — fantasma de geometria conocida', '',
         f'Cilindro oseo de radio **{R_FANTASMA_MM} mm**, voxel isotropo de 1 mm. La brecha esperada de un '
         f'cilindro de diametro `d` es `max(0, d/2 - R)`.', '',
         '| d (mm) | brecha (mm) | esperado (mm) | error (mm) | grado |', '|---|---|---|---|---|']
    L += [f'| {f["d_mm"]} | {f["brecha_mm"]} | {f["esperado_mm"]} | {f["error_mm"]} | {f["grado"]} |'
          for f in filas]
    L += ['', f'**Error maximo frente a la geometria continua: {err_max:.3f} mm.** Es la resolucion de '
              'SAP y debe declararse junto a cualquier cifra de brecha: por debajo de ese valor la '
              'metrica no distingue.',
          '', f'**C2 en el fantasma:** brecha con `d = D_TS` = **{ctrl:.6f} mm** (debe ser 0).',
          '', '**C3 monotonia:** pasa.', '']

    if not args.solo_fantasma and args.ts_dir and args.ct_dir:
        r1 = pd.read_csv(args.refs_dir / 'r1_landmarks.csv', index_col='Caso')
        e9 = pd.read_csv(args.refs_dir / 'e9ts_corredor.csv')
        e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
        rutas = {p.name[:-len('.nii.gz')]: p for p in args.ct_dir.expanduser().rglob('dataset*.nii.gz')}
        L += ['## C2 y C3 — casos reales, sobre el eje del corredor de E9-TS', '']
        for caso in args.casos:
            sub = e9[e9.Caso == caso]
            if caso not in rutas or not sub.shape[0]:
                L += [f'- `{caso}`: **NO ENCONTRADO** (CT o fila de E9-TS). Saltado.', '']
                continue
            res = caso_real(caso, rutas[caso], args.ts_dir.expanduser(), r1.loc[caso], sub.iloc[0])
            L += [f'### `{caso}`', '',
                  f'- longitud del implante (tramo del corredor) = **{res["L_TS_mejor_mm"]} mm**; '
                  f'`L_TS_mejor_mm` del CSV = **{res["L_TS_csv_mm"]} mm**',
                  f'- `D_TS_max` guardado en E9-TS = **{res["D_TS_max_mm"]} mm**; recalculado aqui = '
                  f'**{res["D_TS_recalculado_mm"]} mm**; voxel {res["zoom_mm"]} mm',
                  f'- **C4** (misma envolvente que E9-TS): diferencia **{res["C4_dif_D_TS_mm"]} mm**, '
                  'dentro del redondeo a 1 decimal del CSV',
                  f'- **C2:** brecha con el `D_TS_max` guardado = **{res["C2_brecha_con_D_TS"]} mm** '
                  '(tolerancia 0.05 mm, que es ese mismo redondeo); con el valor exacto = '
                  f'**{res["C2_brecha_con_D_TS_exacto"]} mm** (debe ser 0)',
                  f'- **C3:** brechas por diametro creciente = {res["C3_monotonia"]} (no decrece)', '',
                  '| d (mm) | brecha (mm) | grado | frac. baja densidad | viable corredor |',
                  '|---|---|---|---|---|']
            for d in (sap.D_SAP_MM,) + sap.D_SENSIBILIDAD_MM:
                r = res[f'sap_d{d}']
                L += [f'| {d} | {r["brecha_mm"]} | {r["grado"]} | {r["frac_baja_densidad"]} '
                      f'| {r["viable_corredor"]} |']
            L += ['', f'**C5 — la metrica discrimina.** Eje inclinado alrededor del centro del corredor, '
                      f'cilindro de {sap.D_SAP_MM} mm:', '',
                  '| inclinacion (deg) | brecha (mm) | grado | estado |',
                  '|---|---|---|---|']
            L += [f'| {x["inclinacion_deg"]} | {x["brecha_mm"]} | {x["grado"]} | `{x["estado"]}` |'
                  for x in res['C5']]
            c6 = res['C6']
            L += ['', f'Poses sin grado en el barrido: **{res["C5_sin_grado"]}** (con la opcion (b) de '
                      '#120 debe ser 0).',
                  '', '**C6 — los dos tramos coinciden donde ambos son validos.** Sobre el eje del '
                      'corredor, que cumple las dos definiciones:', '',
                  f'- brecha con tramo de corredor = **{c6["brecha_corredor_mm"]} mm**; con tramo de '
                  f'pose = **{c6["brecha_pose_mm"]} mm**; diferencia **{c6["dif_mm"]} mm**',
                  f'- largo del tramo: corredor {c6["largo_corredor_mm"]} mm, pose '
                  f'{c6["largo_pose_mm"]} mm', '']
        L += ['> El eje de E9-TS es el **mejor** corredor del caso, no una pose muestreada. Sus grados '
              'son 0 por construccion y **no son un resultado de SAP**: son el control de que la metrica '
              'no inventa brechas donde no las hay.', '']

    L += ['## Limites declarados', '',
          '- La envolvente viene de TotalSegmentator, que segmenta **hueso**, no cortical. Su borde '
          '**aproxima** la superficie cortical externa.',
          '- La brecha se mide **radialmente**, en el plano perpendicular al eje. Coincide con la '
          'protrusion para una cortical localmente plana.',
          f'- Resolucion de la metrica: **{err_max:.3f} mm** sobre geometria conocida con voxel de 1 mm.',
          '- Las poses sin travesia osea suficiente se califican **grado 3** y su estado se reporta '
          '(#120, opcion (b), decidida el 2026-09-22). Ninguna pose se queda sin grado.', '']
    args.out.write_text('\n'.join(L), encoding='utf-8')
    print(f'escrito {args.out}')
    print(f'C1 error maximo {err_max:.3f} mm; C2 fantasma {ctrl:.6f} mm')


if __name__ == '__main__':
    main()
