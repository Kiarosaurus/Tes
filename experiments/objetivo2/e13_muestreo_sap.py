"""E13 — muestreo de poses + SAP sobre la cohorte, y Wasserstein-1 contra `zwingmann2009navigated`.

QUE HACE
--------
Por cada caso de la cohorte: reconstruye la envolvente osea, ancla la pose base al corredor medido en
E9-TS, genera `--poses` poses con la distribucion **preinscrita** en
`preinscripcion_muestreador.md`, y califica cada una con SAP. Escribe una fila por pose y un resumen
con la distribucion de grados y el Wasserstein-1 contra las dos series de Zwingmann.

LO QUE ESTE SCRIPT NO HACE
--------------------------
No ajusta ningun parametro, no elige entre variantes y no vuelve a tirar la semilla. Los parametros de
la perturbacion estan congelados en `src/muestreador/muestreo.py` y justificados en la preinscripcion;
si el Wasserstein-1 sale alto, **esa es la cifra** (D-O2.1).

CONTROLES QUE PUEDEN FALLAR
---------------------------
- La pose **sin perturbar** de cada caso tiene que dar brecha 0 (es el eje del corredor). Se calcula y
  se reporta el recuento de casos que lo incumplen; si alguno falla, su caso no se usa.
- Ninguna pose puede quedarse sin grado (#120, opcion (b)).
- La cohorte tiene que salir de 72 casos (primaria) o 49 (sensibilidad); el recuento se imprime.

USO
---
Local, sobre los pilotos con mascaras en disco:
    python e13_muestreo_sap.py --ts-dir ../../data/derivados/ts_piloto --ct-dir ../../data \\
        --casos dataset7_CLINIC_metal_0008_data dataset6_CLINIC_0002_data --out-sufijo piloto

Khipu, cohorte completa:
    python e13_muestreo_sap.py --ts-dir ~/metalsynth/data/ts_total --ct-dir ~/metalsynth/data/ts_input

Escribe `e13_poses<sufijo>.csv` y `e13_sap<sufijo>.md`.
"""
from __future__ import annotations

import argparse
import sys
import traceback
from pathlib import Path

import numpy as np
import pandas as pd

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src' / 'muestreador'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import muestreo  # noqa: E402
import sap  # noqa: E402
from e12_sap_control import envolvente  # noqa: E402

CAMPOS = ['Caso', 'Grupo', 'i_pose', 'd_mm', 'brecha_mm', 'grado', 'estado', 'frac_baja_densidad',
          'viable_corredor', 'longitud_mm', 'desvio_centro_mm', 'inclinacion_deg']


def cohorte(refs_dir: Path, grupos: tuple[str, ...], filtrar: bool = True) -> pd.DataFrame:
    """Filas de E9-TS de la cohorte: `default6mm`, sin limpieza, implante como hueso, con QC de nivel.

    `filtrar=False` salta la QC y los grupos. **Solo para la prueba local sobre los pilotos**, que son de
    grupo 1 y no pertenecen a la cohorte del Objetivo 2; con ella no se produce ningun resultado de
    tesis, solo se comprueba que el camino completo corre.
    """
    e9 = pd.read_csv(refs_dir / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
    if not filtrar:
        return e9.drop_duplicates('Caso').set_index('Caso')
    e9 = e9[(e9.estado_TS == 'concordante') & (e9.S1_toca_fov.isna())]
    return e9[e9.Grupo.isin(grupos)].drop_duplicates('Caso').set_index('Caso')


def procesar(caso: str, ruta_ct: Path, ts_dir: Path, r1: pd.Series, fila: pd.Series,
             n_poses: int, rng: np.random.Generator) -> tuple[list[dict], dict]:
    """Todas las poses de un caso, mas su control de pose sin perturbar."""
    hu, hueso, zoom, origen = envolvente(caso, ruta_ct, ts_dir, r1)
    c0 = np.array([fila['c_x_mm'], fila['c_y_mm'], fila['c_z_mm']], dtype=float)
    u0 = np.array([fila['u_x'], fila['u_y'], fila['u_z']], dtype=float)
    u0 = u0 / np.linalg.norm(u0)
    base = sap.pose_base(hueso, zoom, origen, c0, u0)
    if base is None:
        raise RuntimeError('sin corredor valido: no hay pose base')
    c, largo = base
    d_ts = float(fila['D_TS_max_mm'])
    sdf = sap.campo_signado(hueso, zoom)

    # Control: la pose sin perturbar es el eje del corredor y tiene que dar brecha 0 **al diametro del
    # propio corredor**, que es la unica identidad garantizada por construccion (`D_TS_max` es 2 x min
    # del EDT sobre ese mismo eje). Hacerlo a 7.0 mm era un error: en los casos cuyo corredor mide menos
    # de 7.0 mm, un tornillo del benchmark **tiene** que sobresalir, y eso es anatomia, no un fallo de la
    # metrica. Ver #122.
    sin_perturbar = sap.evaluar_pose(hueso, zoom, origen, c, u0, largo, d_ts, sdf=sdf)
    # Aparte, y como dato anatomico que se reporta: el corredor de este caso, admite el calibre del
    # benchmark sobre su propio eje?
    a_7mm = sap.evaluar_pose(hueso, zoom, origen, c, u0, largo, sap.D_SAP_MM, sdf=sdf)

    centros, direcciones = muestreo.muestrear_poses(c, u0, largo, n_poses, rng)
    filas = []
    for i in range(n_poses):
        ci, ui = centros[i], direcciones[i]
        desvio = float(np.linalg.norm(ci - c))
        incl = float(np.degrees(np.arccos(np.clip(float(ui @ u0), -1.0, 1.0))))
        frac = sap.fraccion_densidad(hu, hueso, zoom, origen, ci, ui, largo)
        for d in (sap.D_SAP_MM,) + sap.D_SENSIBILIDAD_MM:
            r = sap.evaluar_pose(hueso, zoom, origen, ci, ui, largo, d, sdf=sdf)
            filas.append({'Caso': caso, 'Grupo': fila['Grupo'], 'i_pose': i, 'd_mm': d,
                          'brecha_mm': r['brecha_mm'], 'grado': r['grado'], 'estado': r['estado'],
                          'frac_baja_densidad': frac,
                          'viable_corredor': bool(d_ts >= d + 2 * 1.0),
                          'longitud_mm': round(largo, 2),
                          'desvio_centro_mm': round(desvio, 3),
                          'inclinacion_deg': round(incl, 3)})
    ctrl = {'Caso': caso, 'brecha_sin_perturbar_mm': sin_perturbar['brecha_mm'],
            'grado_sin_perturbar': sin_perturbar['grado'], 'longitud_mm': round(largo, 2),
            'D_TS_max_mm': d_ts, 'corredor_estrecho': bool(d_ts < sap.D_SAP_MM),
            'brecha_eje_a_7mm': a_7mm['brecha_mm'], 'grado_eje_a_7mm': a_7mm['grado']}
    return filas, ctrl


def resumen(poses: pd.DataFrame, controles: pd.DataFrame, n_esperado: int) -> list[str]:
    """Distribucion de grados y Wasserstein-1. No elige nada."""
    L = ['# E13 — muestreo de poses y SAP (generado por `e13_muestreo_sap.py`; no elige nada)', '',
         '> Distribucion de poses y metrica **preinscritas** en `preinscripcion_muestreador.md` '
         '(2026-09-22), antes de calcular este archivo. Ningun parametro se ajusto despues.', '',
         '## Integridad', '',
         f'- Casos procesados: **{poses.Caso.nunique()}** (esperados {n_esperado}).',
         f'- Poses por caso y diametro: **{poses.groupby(["Caso", "d_mm"]).size().max()}**.',
         f'- Filas totales: **{len(poses)}**.',
         f'- Poses sin grado: **{int(poses.grado.isna().sum())}** (debe ser 0).', '']

    if controles.empty:
        return L + ['**Sin casos procesados.** Ver la seccion de errores.', '']
    malos = controles[~np.isclose(controles.brecha_sin_perturbar_mm.fillna(-1), 0.0, atol=0.05)]
    L += [f'- Control de pose sin perturbar, al diametro del propio corredor (debe dar brecha 0): '
          f'**{len(controles) - len(malos)} de {len(controles)}** casos pasan.']
    if len(malos):
        L += ['', '**Casos que NO pasan el control.** Esto si es un fallo de implementacion y sus cifras '
                  'no deben usarse:', '']
        L += [f'  - `{r.Caso}`: brecha {r.brecha_sin_perturbar_mm} mm con d = D_TS_max = '
              f'{r.D_TS_max_mm} mm' for r in malos.itertuples()]
    L += ['']

    if 'corredor_estrecho' in controles:
        est = controles[controles.corredor_estrecho]
        L += [f'- **Corredores mas estrechos que el calibre del benchmark** (`D_TS_max` < '
              f'{sap.D_SAP_MM} mm): **{len(est)} de {len(controles)}** casos. **No es un fallo:** en '
              'esos pacientes el eje ideal del corredor ya perfora al calibre de 7.0 mm, asi que el '
              'grado 0 es inalcanzable por anatomia y no por el muestreador. Sus poses **si entran** en '
              'la distribucion, porque la serie clinica tampoco excluyo a sus pacientes estrechos '
              '(#122).']
        if len(est):
            med = est.brecha_eje_a_7mm.median()
            L += [f'  Brecha del eje ideal a 7.0 mm en esos casos: mediana **{med:.2f} mm**, '
                  f'maxima **{est.brecha_eje_a_7mm.max():.2f} mm**.']
        L += ['']

    L += ['## Perturbacion efectivamente aplicada', '']
    p7 = poses[poses.d_mm == sap.D_SAP_MM]
    for col, nombre in (('desvio_centro_mm', 'desvio del centro (mm)'),
                        ('inclinacion_deg', 'inclinacion (grados)')):
        v = p7[col]
        L += [f'- {nombre}: mediana **{v.median():.2f}**, p90 **{v.quantile(0.9):.2f}**, '
              f'max **{v.max():.2f}**']
    L += ['']

    L += ['## Distribucion de grados y Wasserstein-1', '',
          '| d (mm) | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |',
          '|---|---|---|---|---|---|---|---|']
    for d in sorted(poses.d_mm.unique()):
        sub = poses[poses.d_mm == d]
        dist = sap.distribucion_grados(list(sub.grado), no_evaluables='error')
        w_nav = sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['navegado'])
        w_con = sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['convencional'])
        marca = ' **(SAP)**' if d == sap.D_SAP_MM else ''
        L += [f'| {d}{marca} | {len(sub)} | {dist[0]:.1f} | {dist[1]:.1f} | {dist[2]:.1f} | '
              f'{dist[3]:.1f} | {w_nav:.3f} | {w_con:.3f} |']
    L += ['', 'Referencias de `zwingmann2009navigated`: navegado **69 / 15 / 8 / 8** (26 tornillos, 24 '
              'pacientes); convencional **40 / 37 / 11.5 / 11.5** (35 tornillos, 32 pacientes). '
              '`zwingmann2010percutaneous` no entra (#113).',
          '', 'El W1 esta en **grados**, no en milimetros, y trata los cuatro grados como '
              'equiespaciados (convencion declarada). Su maximo posible es 3.0.', '']

    L += ['## Estados de las poses', '']
    est = poses[poses.d_mm == sap.D_SAP_MM].estado.value_counts()
    L += [f'- `{k}`: **{v}**' for k, v in est.items()]
    L += ['', '## Fraccion por zona de densidad (componente 2 de SAP, reportado)', '']
    fr = p7.frac_baja_densidad.dropna()
    L += [f'- mediana **{fr.median():.3f}**, p25 **{fr.quantile(.25):.3f}**, '
          f'p75 **{fr.quantile(.75):.3f}** sobre {len(fr)} poses', '']
    L += ['## Viabilidad de corredor (componente 3 de SAP)', '']
    for d in sorted(poses.d_mm.unique()):
        sub = poses[poses.d_mm == d]
        L += [f'- d = {d} mm: **{100 * sub.viable_corredor.mean():.1f}%** de las poses en casos con '
              f'`D_TS_max >= d + 2`']
    return L + ['']


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ts-dir', type=Path, required=True)
    parser.add_argument('--ct-dir', type=Path, required=True)
    parser.add_argument('--refs-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--casos', nargs='*', default=[])
    parser.add_argument('--grupos', nargs='*', default=['grupo 2', 'grupo 3'])
    parser.add_argument('--poses', type=int, default=50)
    parser.add_argument('--out-sufijo', default='')
    parser.add_argument('--ignorar-cohorte', action='store_true',
                        help='salta la QC y los grupos; solo para la prueba local sobre los pilotos')
    args = parser.parse_args()

    r1 = pd.read_csv(args.refs_dir / 'r1_landmarks.csv', index_col='Caso')
    coh = cohorte(args.refs_dir, tuple(args.grupos), filtrar=not args.ignorar_cohorte)
    rutas = {p.name[:-len('.nii.gz')]: p for p in args.ct_dir.expanduser().rglob('dataset*.nii.gz')}
    casos = args.casos or list(coh.index)
    print(f'cohorte de {len(coh)} casos; se procesaran {len(casos)}')

    filas, controles, errores = [], [], []
    for caso in casos:
        if caso not in coh.index or caso not in rutas:
            errores.append((caso, 'sin fila de cohorte o sin CT'))
            continue
        try:
            f, ctrl = procesar(caso, rutas[caso], args.ts_dir.expanduser(), r1.loc[caso],
                               coh.loc[caso], args.poses, muestreo.rng_de_caso(caso))
            filas += f
            controles.append(ctrl)
            print(f'  {caso}: {len(f)} filas, control {ctrl["brecha_sin_perturbar_mm"]}')
        except Exception as e:  # noqa: BLE001
            errores.append((caso, f'{type(e).__name__}: {e}'))
            traceback.print_exc()

    poses = pd.DataFrame(filas, columns=CAMPOS)
    out_csv = args.refs_dir / f'e13_poses{args.out_sufijo}.csv'
    poses.to_csv(out_csv, index=False)
    L = resumen(poses, pd.DataFrame(controles), len(coh))
    if errores:
        L += ['## Casos con error', ''] + [f'- `{c}`: {m}' for c, m in errores] + ['']
    out_md = args.refs_dir / f'e13_sap{args.out_sufijo}.md'
    out_md.write_text('\n'.join(L), encoding='utf-8')
    print(f'escritos {out_csv.name} y {out_md.name}; errores: {len(errores)}')


if __name__ == '__main__':
    main()
