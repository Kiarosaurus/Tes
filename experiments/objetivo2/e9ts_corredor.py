"""E9-TS — corredor oseo sacro sobre las mascaras de TotalSegmentator (decisiones del 2026-09-14).

POR QUE
-------
E9 con umbral HU quedo NO VALIDO (#48): el esponjoso del ala cae bajo 150 HU. Decisiones del
2026-09-14: TS 2.18.0 `total` como mascara anatomica; recorte de 6 mm principal y 3 mm como
sensibilidad; limpieza por fraccion de componente (fraccion a fijar con E10); densidad dentro de las
mascaras. #52: el corredor del Objetivo 2 se mide en pelvis **sin osteosintesis** (a), y en las que
tienen implante se mide **con y sin el implante como espacio ocupado** para reportar la diferencia (c).

DISENO PARA CORRER SIN SUPERVISION
---------------------------------
**Ninguna decision pendiente se toma en el codigo.** Se calculan todas las variantes entre las que esas
decisiones pueden elegir, y la eleccion se hace despues filtrando filas, sin volver a correr:

- recorte: `default6mm` y `robust3mm`;
- fraccion de limpieza `F`: 0 (sin limpieza), 0.001, 0.01 y 0.05. **Rejilla de sensibilidad
  declarada, no propuesta de valor**;
- `politica_metal` (#52 c), solo en casos con voxeles > 2500 HU dentro del recorte:
  - `hueso`: el implante cuenta como hueso, que es lo que hace TS. En casos sin metal es la unica fila;
  - `ocupado_2500`: los voxeles > 2500 HU no son hueso. 2500 HU adelgaza y parte los tornillos (#46),
    asi que el implante queda **por defecto** y el `Dmax` resultante es una **cota superior** del
    corredor con implante ocupado;
  - `ocupado_semimax`: por objeto de metal (componente > 2500 HU del recorte), umbral de semimaximo
    local con el mismo casquete que E8 (fondo = mediana HU a 3-6 mm; umbral = fondo + (p95 - fondo) / 2),
    aplicado a <= 3 mm del objeto. Es la propuesta **abierta** de la decision #22 para mascaras de
    implantes reales. Difiere de E8 en que no fusiona fragmentos colineales.
  Cual de las dos es la principal no esta decidido; se calculan ambas;
- cohorte: todos los casos en uso con S1 en R1. Cada fila lleva `Grupo`, `cohorte`, juicio del clinico,
  `estado_TS`, `fov7` y `S1_toca_fov`, para aplicar despues la QC, #52 (a) y el "con y sin los 7".

Si una variante deja la mascara identica a otra de la misma politica, se reutiliza el resultado
(`igual_a_F`).

METODO
------
Igual que `e9_corredor.py`, cuyas funciones importa (`evaluar_linea`, `picos`, `angulos_kaiser`): centros
en el sagital del S1 de R1, 81 direcciones, tramo que sale por el ilion al menos tan lateral como la EIPS,
`D = 2 x min EDT` sin 8 mm por extremo, restriccion #31. Cambia la mascara osea:

1. Por estructura (`sacrum`, `vertebrae_S1`, `hip_left`, `hip_right`), conectividad 26, se quitan los
   componentes con menos de `F` del volumen de esa estructura.
2. Hueso = union de las cuatro, con cierre morfologico de 2 mm (el de E9) para que la articulacion
   sacroiliaca no corte el corredor, y **despues** se restan los voxeles ocupados de la politica (asi el
   cierre no rellena el hueco del implante).
3. Paso por metal: `dist_eje_metal_min_mm` (eje completo al voxel > 2500 HU mas cercano),
   `frac_eje_metal_r2mm` y `cilindro_toca_metal` (el cilindro de diametro `D_TS` alcanza metal).
   `frac_metal_eje` (metal justo en el voxel del eje) se conserva pero **no sirve** (piloto).
4. Densidad sobre el eje del mejor corredor (sin 8 mm por extremo): mediana HU y fraccion <= 150 HU de
   los puntos del eje dentro de la union sin cierre y sin voxeles ocupados.

La lamina (recorte de `--modo-laminas`, por defecto `default6mm`; F = 0, `hueso`) muestra un corte coronal: **proyecta el eje e ignora su inclinacion en
y**. Para saber si el corredor pasa por el implante hay que mirar las columnas, no la lamina.

Lee `r1_landmarks.csv`, `r1_estados.csv`, `ts_nivel_s1.csv`, las mascaras `<ts-dir>/<caso>/<modo>/` y
los CT. Escribe `e9ts_corredor.csv` (caso x recorte x F x politica), `e9ts_perfiles.csv` y, con
`--laminas`, una lamina por caso. Reanudable: salta los casos que ya tienen filas.

USO
---
Khipu (ver `KHIPU.md`, "Noche automatica"):
    python e9ts_corredor.py --ts-dir ~/metalsynth/data/ts_total --ct-dir ~/metalsynth/data/ts_input \
        --refs-dir . --out-dir ~/metalsynth/data/e9ts --workers 16 --laminas
Khipu, laminas con el recorte de 3 mm (preferencia de la autora, 2026-09-14; ver `KHIPU.md`, E9-TS 3 mm):
    python e9ts_corredor.py ... --out-dir ~/metalsynth/data/e9ts_3mm --laminas --modo-laminas robust3mm
Local, prueba sobre el piloto:
    python e9ts_corredor.py --ts-dir ../../data/derivados/ts_piloto --ct-dir ../../data \
        --out-dir outputs/e9ts_prueba --casos metal_0008 --laminas
"""
from __future__ import annotations

import argparse
import csv
import gc
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import ndimage as ndi

from e9_corredor import (ANGULOS, CALIBRES, CIERRE_MM, HOLGURAS, METAL_HU, PASO_MM, RECORTE_EXTREMO_MM,
                         angulos_kaiser, evaluar_linea, lamina, muestrear, picos)
from r1_landmarks import cargar
from ts_piloto_qc import mascara

BONE_HU = 150.0
MODOS = ['default6mm', 'robust3mm']
ESTRUCTURAS = ['sacrum', 'vertebrae_S1', 'hip_left', 'hip_right']
FRACCIONES = [0.0, 0.001, 0.01, 0.05]
POLITICAS_METAL = ['ocupado_2500', 'ocupado_semimax']
CASQUETE_MM = (3.0, 6.0)  # el mismo casquete de fondo que `e8_censo_implantes.semimaximo`
CONECTIVIDAD = np.ones((3, 3, 3), dtype=bool)

RESULTADOS = (['D_TS_max_mm', 'L_TS_mejor_mm', 'D_IS_izq_max_mm', 'D_IS_der_max_mm', 'pico_sup_z_rel_mm',
               'pico_sup_D_mm', 'pico_inf_z_rel_mm', 'pico_inf_D_mm', 'z_mejor_rel_mm', 'y_mejor_rel_mm',
               'ang_coronal_crestas_deg', 'ang_axial_eips_deg', 'c_x_mm', 'c_y_mm', 'c_z_mm', 'u_x', 'u_y', 'u_z',
               'frac_metal_eje', 'frac_eje_metal_r2mm', 'dist_eje_metal_min_mm', 'cilindro_toca_metal',
               'n_eje_en_mascara', 'hu_p50_eje', 'frac_bajo150_eje', 'viable_TS_10mm']
              + [f'viable_TS_d{d}_c{c:.0f}' for d in CALIBRES for c in HOLGURAS])
CAMPOS = (['Caso', 'Grupo', 'cohorte', 'clinico', 'estado_TS', 'fov7', 'S1_toca_fov', 'modo', 'F_limpieza',
           'politica_metal', 'igual_a_F', 'vox_quitados', 'vox_quitados_recorte', 'vox_ocupados_recorte']
          + RESULTADOS + ['segundos', 'Error'])
CAMPOS_PERFIL = ['Caso', 'modo', 'F_limpieza', 'politica_metal', 'z_rel_S1_mm', 'D_TS_mejor_mm',
                 'c_x_mm', 'c_y_mm', 'c_z_mm', 'u_x', 'u_y', 'u_z']


def caja_recorte(s1: np.ndarray, zoom: np.ndarray, forma: np.ndarray) -> tuple[slice, ...]:
    """El mismo recorte alrededor de S1 que `e9_corredor.recortar`."""
    lo = np.maximum(np.floor((s1 + np.array([-130.0, -110.0, -110.0])) / zoom).astype(int), 0)
    hi = np.minimum(np.ceil((s1 + np.array([130.0, 60.0, 40.0])) / zoom).astype(int), forma)
    return tuple(slice(lo[a], hi[a]) for a in range(3))


def etiquetar(m: np.ndarray) -> tuple[np.ndarray | None, tuple[slice, ...] | None, np.ndarray]:
    """Componentes de una mascara, sobre su caja. Devuelve (etiquetas, caja, tamanos por etiqueta)."""
    if not m.any():
        return None, None, np.zeros(0, dtype=np.int64)
    idx = [np.flatnonzero(m.any(axis=tuple(a for a in range(3) if a != ax))) for ax in range(3)]
    sl = tuple(slice(i[0], i[-1] + 1) for i in idx)
    lab, _ = ndi.label(m[sl], structure=CONECTIVIDAD)
    return lab, sl, np.bincount(lab.ravel())


def limpia(forma: np.ndarray, etiquetas: list, frac: float) -> tuple[np.ndarray, int]:
    """Union de las estructuras sin los componentes < frac de su estructura; voxeles quitados."""
    union = np.zeros(forma, dtype=bool)
    quitados = 0
    for lab, sl, tam in etiquetas:
        if lab is None:
            continue
        n = int(tam[1:].sum())
        keep = tam >= frac * n
        keep[0] = False
        quitados += int(tam[1:][~keep[1:]].sum())
        union[sl] |= keep[lab]
    return union, quitados


def ocupacion(hu: np.ndarray, zoom: np.ndarray) -> dict[str, np.ndarray] | None:
    """Voxeles ocupados por metal segun cada politica de #52 (c); None si no hay metal en el recorte."""
    metal = hu > METAL_HU
    if not metal.any():
        return None
    lab, _ = ndi.label(metal, structure=CONECTIVIDAD)
    semimax = metal.copy()
    pad = np.ceil(CASQUETE_MM[1] / zoom).astype(int) + 1
    for k, o in enumerate(ndi.find_objects(lab), start=1):
        if o is None:
            continue
        a0 = np.maximum(np.array([s.start for s in o]) - pad, 0)
        a1 = np.minimum(np.array([s.stop for s in o]) + pad, np.array(hu.shape))
        sl = tuple(slice(a0[a], a1[a]) for a in range(3))
        sub = hu[sl].astype(np.float32)
        m = lab[sl] == k
        dist = ndi.distance_transform_edt(~m, sampling=zoom)
        casquete = (dist >= CASQUETE_MM[0]) & (dist <= CASQUETE_MM[1]) & (sub < METAL_HU)
        if not casquete.any():
            continue
        fondo = float(np.median(sub[casquete]))
        umbral = fondo + (float(np.percentile(sub[m], 95)) - fondo) / 2.0
        semimax[sl] |= (sub >= umbral) & (dist <= CASQUETE_MM[0])
    return {'ocupado_2500': metal, 'ocupado_semimax': semimax}


def buscar(hu: np.ndarray, hueso: np.ndarray, densidad: np.ndarray, origen: np.ndarray, zoom: np.ndarray,
           r1: pd.Series, dmetal: np.ndarray | None
           ) -> tuple[dict, np.ndarray, np.ndarray, dict, list[dict | None]]:
    """Busqueda de corredor de `e9_corredor.analizar` sobre una mascara dada, mas metal y densidad en el eje."""
    s1 = np.array([r1['S1_x_mm'], r1['S1_y_mm'], r1['S1_z_mm']], dtype=np.float32)
    x_mid = float(r1['S1_x_mm'])
    edt = ndi.distance_transform_edt(hueso, sampling=zoom).astype(np.float32)
    lat_min = (abs(float(r1['eips_izq_x_mm']) - x_mid), abs(float(r1['eips_der_x_mm']) - x_mid))
    zs = s1[2] - np.arange(3.0, 75.01, 3.0)
    ys = s1[1] + np.arange(-45.0, 10.01, 3.0)
    direcciones = []
    for a in ANGULOS:
        for b in ANGULOS:
            u = np.array([1.0, np.tan(a), np.tan(b)])
            direcciones.append(u / np.linalg.norm(u))
    mejor_global: dict = {}
    mejor_por_z = np.zeros(len(zs))
    # Eje del mejor corredor A CADA ALTURA. Antes solo se guardaba el diametro (`mejor_por_z`) y el
    # `c`/`u` de cada z se descartaba al pasar a la siguiente; solo sobrevivia el del mejor global, que
    # es el de S1. Sin el eje por altura no se puede muestrear ni marcar el corredor de S2 (#121).
    ejes_por_z: list[dict | None] = [None] * len(zs)
    mejores_is = {'D_IS_izq': 0.0, 'D_IS_der': 0.0}
    for iz, z in enumerate(zs):
        mejor_z: dict = {}
        for y in ys:
            c = np.array([x_mid, y, z], dtype=np.float32)
            if not muestrear(hueso, zoom, origen, c[None, :])[0]:
                continue
            for u in direcciones:
                r = evaluar_linea(hueso, edt, zoom, origen, c, u, x_mid, lat_min)
                if r is None:
                    continue
                for k in mejores_is:
                    if np.isfinite(r[k]):
                        mejores_is[k] = max(mejores_is[k], r[k])
                if r['D_TS'] > mejor_z.get('D_TS', -1):
                    mejor_z = {**r, 'c': c, 'u': u}
        mejor_por_z[iz] = mejor_z.get('D_TS', 0.0)
        if mejor_z:
            ejes_por_z[iz] = {'c': mejor_z['c'], 'u': mejor_z['u']}
        if mejor_por_z[iz] > mejor_global.get('D_TS', -1):
            mejor_global = mejor_z
    del edt

    sup, inf = picos(zs, mejor_por_z)
    fila: dict = {'D_TS_max_mm': round(mejor_global.get('D_TS', 0.0), 1),
                  'L_TS_mejor_mm': round(mejor_global.get('L_TS', np.nan), 1),
                  'D_IS_izq_max_mm': round(mejores_is['D_IS_izq'], 1),
                  'D_IS_der_max_mm': round(mejores_is['D_IS_der'], 1)}
    if sup:
        fila.update({'pico_sup_z_rel_mm': round(sup[0] - s1[2], 1), 'pico_sup_D_mm': round(sup[1], 1)})
    if inf:
        fila.update({'pico_inf_z_rel_mm': round(inf[0] - s1[2], 1), 'pico_inf_D_mm': round(inf[1], 1)})
    if mejor_global:
        u, c = mejor_global['u'], mejor_global['c']
        fila['z_mejor_rel_mm'] = round(float(c[2] - s1[2]), 1)
        fila['y_mejor_rel_mm'] = round(float(c[1] - s1[1]), 1)
        cor, axi = angulos_kaiser(u, r1)
        fila['ang_coronal_crestas_deg'] = round(cor, 1) if np.isfinite(cor) else np.nan
        fila['ang_axial_eips_deg'] = round(axi, 1) if np.isfinite(axi) else np.nan
        fila.update({'c_x_mm': round(float(c[0]), 1), 'c_y_mm': round(float(c[1]), 1), 'c_z_mm': round(float(c[2]), 1),
                     'u_x': round(float(u[0]), 4), 'u_y': round(float(u[1]), 4), 'u_z': round(float(u[2]), 4)})
        forma = np.array(hu.shape)
        tt = np.arange(-mejor_global['L_TS'] / 2, mejor_global['L_TS'] / 2 + 0.1, PASO_MM)
        ie = np.rint(((c[None, :] + tt[:, None] * u[None, :]) - origen) / zoom).astype(int)
        ie = ie[np.all((ie >= 0) & (ie < forma), axis=1)]
        if len(ie):
            fila['frac_metal_eje'] = round(float((hu[ie[:, 0], ie[:, 1], ie[:, 2]] > METAL_HU).mean()), 3)
        if dmetal is None:
            fila.update({'frac_eje_metal_r2mm': 0.0, 'dist_eje_metal_min_mm': np.nan, 'cilindro_toca_metal': False})
        elif len(ie):
            de = dmetal[ie[:, 0], ie[:, 1], ie[:, 2]]
            fila.update({'frac_eje_metal_r2mm': round(float((de <= 2.0).mean()), 3),
                         'dist_eje_metal_min_mm': round(float(de.min()), 1),
                         'cilindro_toca_metal': bool(de.min() < mejor_global['D_TS'] / 2)})
        media = mejor_global['L_TS'] / 2 - RECORTE_EXTREMO_MM
        t = np.arange(-media, media + 0.1, PASO_MM) if media > 0 else np.array([0.0])
        idx = np.rint(((c[None, :] + t[:, None] * u[None, :]) - origen) / zoom).astype(int)
        idx = idx[np.all((idx >= 0) & (idx < forma), axis=1)]
        v = hu[idx[:, 0], idx[:, 1], idx[:, 2]]
        dentro = densidad[idx[:, 0], idx[:, 1], idx[:, 2]]
        fila['n_eje_en_mascara'] = int(dentro.sum())
        if dentro.any():
            fila['hu_p50_eje'] = float(np.median(v[dentro]))
            fila['frac_bajo150_eje'] = round(float((v[dentro] <= BONE_HU).mean()), 3)
    for d_imp in CALIBRES:
        for c_h in HOLGURAS:
            fila[f'viable_TS_d{d_imp}_c{c_h:.0f}'] = 'si' if fila['D_TS_max_mm'] >= d_imp + 2 * c_h else 'no'
    fila['viable_TS_10mm'] = 'si' if fila['D_TS_max_mm'] >= 10.0 else 'no'
    return fila, zs, mejor_por_z, mejor_global, ejes_por_z


def procesar(caso: str, ruta_ct: Path, ts_dir: Path, r1: pd.Series, meta: dict,
             dir_laminas: Path | None, modo_laminas: str = 'default6mm') -> tuple[list[dict], list[dict]]:
    """Todas las variantes (recorte x F x politica de metal) de un caso."""
    filas, perfiles = [], []
    ct, zoom = cargar(ruta_ct)
    zoom = zoom.astype(float)
    forma = np.array(ct.shape)
    s1 = np.array([r1['S1_x_mm'], r1['S1_y_mm'], r1['S1_z_mm']], dtype=float)
    sl = caja_recorte(s1, zoom, forma)
    hu = np.array(ct[sl])
    del ct
    gc.collect()
    origen = np.array([s.start for s in sl], dtype=np.float32) * zoom
    ocup = ocupacion(hu, zoom)
    dmetal = (ndi.distance_transform_edt(~ocup['ocupado_2500'], sampling=zoom).astype(np.float32)
              if ocup is not None else None)
    politicas = ['hueso'] + (POLITICAS_METAL if ocup is not None else [])
    it = max(1, int(round(CIERRE_MM / float(zoom.min()))))
    for modo in MODOS:
        etiquetas = []
        for est in ESTRUCTURAS:
            m = mascara(ts_dir / caso / modo / f'{est}.nii.gz')
            if not np.array_equal(np.array(m.shape), forma):
                raise ValueError(f'{modo}/{est}: forma {m.shape} distinta del CT {tuple(forma)}')
            etiquetas.append(etiquetar(m))
            del m
        previas: list[tuple[float, str, np.ndarray, dict]] = []
        ceros_f0 = None
        for frac in FRACCIONES:
            union, quitados = limpia(forma, etiquetas, frac)
            sin_cierre = union[sl].copy()
            del union
            ceros = int(sin_cierre.size - sin_cierre.sum())
            ceros_f0 = ceros if ceros_f0 is None else ceros_f0
            cerrado = None
            for politica in politicas:
                t0 = time.time()
                occ = ocup[politica] if politica != 'hueso' else None
                fila = {**meta, 'modo': modo, 'F_limpieza': frac, 'politica_metal': politica,
                        'vox_quitados': quitados, 'vox_quitados_recorte': ceros - ceros_f0,
                        'vox_ocupados_recorte': int((sin_cierre & occ).sum()) if occ is not None else 0}
                igual = next((f for f, p, prev, _ in previas if p == politica and np.array_equal(prev, sin_cierre)), None)
                if igual is not None:
                    res = next(r for f, p, _, r in previas if f == igual and p == politica)
                    fila.update({**res, 'igual_a_F': igual})
                else:
                    if cerrado is None:
                        cerrado = ndi.binary_closing(np.pad(sin_cierre, it), iterations=it)[it:-it, it:-it, it:-it]
                    hueso = cerrado & ~occ if occ is not None else cerrado
                    densidad = sin_cierre & ~occ if occ is not None else sin_cierre
                    res, zs, perfil, mejor, ejes = buscar(hu, hueso, densidad, origen, zoom, r1, dmetal)
                    fila.update(res)
                    for z, d, eje in zip(zs, perfil, ejes):
                        p = {'Caso': caso, 'modo': modo, 'F_limpieza': frac, 'politica_metal': politica,
                             'z_rel_S1_mm': round(float(z - s1[2]), 1), 'D_TS_mejor_mm': round(float(d), 1)}
                        if eje is not None:
                            ce, ue = eje['c'], eje['u']
                            p.update({'c_x_mm': round(float(ce[0]), 1), 'c_y_mm': round(float(ce[1]), 1),
                                      'c_z_mm': round(float(ce[2]), 1), 'u_x': round(float(ue[0]), 4),
                                      'u_y': round(float(ue[1]), 4), 'u_z': round(float(ue[2]), 4)})
                        perfiles.append(p)
                    if dir_laminas is not None and modo == modo_laminas and frac == 0.0 and politica == 'hueso':
                        lamina(hu, zoom, origen, mejor, zs, perfil, float(s1[2]), dir_laminas / f'{caso}.png',
                               f'{caso} (TS {modo}, F=0, metal como hueso): D_TS max {res["D_TS_max_mm"]} mm; '
                               f'IS izq {res["D_IS_izq_max_mm"]} / der {res["D_IS_der_max_mm"]} mm '
                               '(coronal: proyecta el eje)')
                    del hueso, densidad
                fila['segundos'] = round(time.time() - t0, 1)
                previas.append((frac, politica, sin_cierre, {k: v for k, v in fila.items() if k in RESULTADOS}))
                filas.append(fila)
            del cerrado
            gc.collect()
        del etiquetas, previas
        gc.collect()
    return filas, perfiles


def trabajo(args: tuple) -> tuple[str, list[dict], list[dict]]:
    """Envoltura para el pool: un caso roto devuelve una fila de error."""
    caso, ruta, ts_dir, r1, meta, dir_laminas, modo_laminas = args
    try:
        filas, perfiles = procesar(caso, ruta, ts_dir, r1, meta, dir_laminas, modo_laminas)
        return caso, filas, perfiles
    except Exception as exc:  # noqa: BLE001
        traceback.print_exc()
        return caso, [{**meta, 'Error': f'{type(exc).__name__}: {exc}'}], []


def main() -> None:
    """Recorre la cohorte; paraleliza por caso."""
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--ts-dir', type=Path, required=True)
    parser.add_argument('--ct-dir', type=Path, required=True, help='busca dataset*.nii.gz recursivamente')
    parser.add_argument('--refs-dir', type=Path, default=here,
                        help='r1_landmarks.csv, r1_estados.csv, ts_nivel_s1.csv')
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--casos', nargs='*', default=None, help='subcadenas de caso')
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--max', type=int, default=None)
    parser.add_argument('--laminas', action='store_true')
    parser.add_argument('--modo-laminas', choices=MODOS, default='default6mm',
                        help='recorte de la lamina por caso (F = 0, hueso); no cambia el CSV')
    args = parser.parse_args()

    refs, out = args.refs_dir.expanduser(), args.out_dir.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    dir_laminas = out / 'laminas' if args.laminas else None
    if dir_laminas is not None:
        dir_laminas.mkdir(exist_ok=True)
    r1 = pd.read_csv(refs / 'r1_landmarks.csv').set_index('Caso')
    est = pd.read_csv(refs / 'r1_estados.csv').set_index('Caso')
    niv = pd.read_csv(refs / 'ts_nivel_s1.csv').set_index('Caso')
    ts_dir = args.ts_dir.expanduser()
    rutas = {p.name[:-len('.nii.gz')]: p for p in args.ct_dir.expanduser().rglob('dataset*.nii.gz')}
    casos = [c for c in niv.index if niv.loc[c, 'S1_hallado_R1'] == 'si']
    if args.casos:
        casos = [c for c in casos if any(s in c for s in args.casos)]
    destino, destino_p = out / 'e9ts_corredor.csv', out / 'e9ts_perfiles.csv'
    hechos = set(pd.read_csv(destino)['Caso']) if destino.exists() else set()
    pendientes = []
    for c in casos:
        if c in hechos:
            continue
        faltan = [f'{m}/{e}' for m in MODOS for e in ESTRUCTURAS if not (ts_dir / c / m / f'{e}.nii.gz').exists()]
        if faltan or c not in rutas:
            print(f'{c}: sin CT o sin mascaras ({len(faltan)} faltan), se salta', flush=True)
            continue
        cresta = est.loc[c, ['cresta_der_estado', 'cresta_izq_estado']]
        meta = {'Caso': c, 'Grupo': niv.loc[c, 'Grupo'], 'cohorte': niv.loc[c, 'cohorte'],
                'clinico': niv.loc[c, 'auditoria_S1_clinico'], 'estado_TS': niv.loc[c, 'estado_TS'],
                'fov7': bool((cresta == 'fuera de FOV').any()) and niv.loc[c, 'cohorte'] == 'evaluacion',
                'S1_toca_fov': niv.loc[c, 'S1_toca_fov']}
        pendientes.append((c, rutas[c], ts_dir, r1.loc[c], meta, dir_laminas, args.modo_laminas))
    if args.max is not None:
        pendientes = pendientes[:args.max]
    print(f'{len(casos)} casos con S1; {len(hechos)} ya hechos; {len(pendientes)} en esta corrida; '
          f'{args.workers} procesos', flush=True)

    nuevo = not destino.exists()
    with destino.open('a', encoding='utf-8', newline='') as h, destino_p.open('a', encoding='utf-8', newline='') as hp:
        w = csv.DictWriter(h, fieldnames=CAMPOS, extrasaction='ignore')
        wp = csv.DictWriter(hp, fieldnames=CAMPOS_PERFIL)
        if nuevo:
            w.writeheader()
            wp.writeheader()

        def escribir(caso: str, filas: list[dict], perfiles: list[dict]) -> None:
            w.writerows(filas)
            wp.writerows(perfiles)
            h.flush()
            hp.flush()
            if 'Error' in filas[0]:
                print(f'{caso}: ERROR {filas[0]["Error"]}', flush=True)
            else:
                d = {(f['modo'][:2], f['politica_metal']): f.get('D_TS_max_mm') for f in filas if f['F_limpieza'] == 0.0}
                print(f'{caso}: {len(filas)} filas; F=0 {d}', flush=True)

        if args.workers <= 1:
            for p in pendientes:
                escribir(*trabajo(p))
        else:
            with ProcessPoolExecutor(max_workers=args.workers) as pool:
                for fut in as_completed([pool.submit(trabajo, p) for p in pendientes]):
                    escribir(*fut.result())


if __name__ == '__main__':
    main()
