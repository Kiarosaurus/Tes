"""Comprobacion descriptiva: la envolvente osea `B` de SAP deja fuera el canal sacro (y que rellena su cierre).

GAP QUE ATIENDE
---------------
`\\GAPDATO{comprobacion de que la envolvente osea deja fuera el canal sacro y los foramenes sacros}`
(`overleaf/secciones/introduccion.tex` l. 96; `capitulo3` §Amenazas; `redaccion/MAPA.md` fila 106).

QUE HACE
--------
Reconstruye `B` exactamente como E12 (`e12_sap_control.envolvente`: union de TotalSegmentator `sacrum`,
`vertebrae_S1`, `hip_left`, `hip_right`, limpieza de E9-TS, cierre de 2 mm sin relleno de cavidades) en los
casos con mascaras en disco, y mide:

1. **Canal en la linea media.** En cada corte axial donde existe la mascara `vertebrae_S1` de
   TotalSegmentator, sobre la linea antero-posterior que pasa por la mediana lateral de esa mascara, los tramos fuera de `B` encerrados entre dos tramos dentro
   de `B` (hueco interior): longitud en mm y mediana de HU. Un canal fuera de `B` aparece como un hueco de
   varios mm con HU de partes blandas; un canal ocupado por `B` no aparece.
2. **Lo que rellena el cierre.** En los mismos cortes, los huecos 2D (componentes del fondo que no tocan el
   borde del corte) de la union sin cierre que el cierre ocupa: area mayor y espesor maximo (2 x distancia
   maxima al borde, en mm). Por construccion, el cierre de radio r solo ocupa huecos donde no cabe su
   elemento estructurante; aqui se mide.

No localiza los foramenes: no hay etiqueta para ellos. Lo que dice sobre ellos es solo el espesor maximo de
lo que el cierre rellena (punto 2).

LIMITE DE ALCANCE
-----------------
Solo hay mascaras de TotalSegmentator en disco para los **dos pilotos** (`data/derivados/ts_piloto`), que son
de grupo 1 y **no pertenecen a la cohorte del Objetivo 2**. El resultado es descriptivo, posterior, y no se
extiende a los 72 casos (sus mascaras estan en Khipu). No usa la particion de prueba del Objetivo 3.

CONTROL DE REGRESION
--------------------
La longitud del implante anclada (`sap.pose_base`) sobre la misma `B` debe reproducir `L_TS_mejor_mm` de
`e9ts_corredor.csv`, como en E12 (`experiments/objetivo2/e12_sap_control.md`: 113.0 mm en `metal_0008` y
154.0 mm en `CLINIC_0002`). Si no reproduce, el script lo dice y no reporta las cifras nuevas de ese caso.

USO
---
Local, pilotos (por defecto):
    python experiments/registro/r_envolvente_canal.py
Cohorte (Khipu, mascaras de TotalSegmentator de los 72 casos; #196 opcion b): ver
`experiments/registro/r_envolvente_canal.sbatch`. Desde ~/metalsynth/qc/, con todas las dependencias al lado:
    python r_envolvente_canal.py --cohorte --ts-dir ~/metalsynth/data/ts_total --ct-dir ~/metalsynth/data/ts_input
        --refs-dir . --out r_envolvente_canal.md --csv r_envolvente_canal.csv
"""
from __future__ import annotations

import sys
import traceback
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import ndimage as ndi

RAIZ = Path(__file__).resolve().parents[2]
OBJ2 = RAIZ / 'experiments' / 'objetivo2'
sys.path.insert(0, str(RAIZ / 'src' / 'muestreador'))
sys.path.insert(0, str(OBJ2))
sys.path.insert(0, str(Path(__file__).resolve().parent))  # Khipu: todo junto en ~/metalsynth/qc/

import sap  # noqa: E402
from e9_corredor import CIERRE_MM  # noqa: E402
from e9ts_corredor import ESTRUCTURAS, caja_recorte, etiquetar, limpia  # noqa: E402
from r1_landmarks import cargar  # noqa: E402
from ts_piloto_qc import mascara  # noqa: E402

import argparse  # noqa: E402

PILOTOS = ['dataset7_CLINIC_metal_0008_data', 'dataset6_CLINIC_0002_data']
TS_DIR = RAIZ / 'data' / 'derivados' / 'ts_piloto'
CT_DIR = RAIZ / 'data'


def envolvente_y_union(caso: str, ruta_ct: Path, r1: pd.Series):
    """Igual que `e12_sap_control.envolvente`, devolviendo tambien la union sin cierre."""
    ct, zoom = cargar(ruta_ct)
    zoom = zoom.astype(float)
    forma = np.array(ct.shape)
    s1 = np.array([r1['S1_x_mm'], r1['S1_y_mm'], r1['S1_z_mm']], dtype=float)
    sl = caja_recorte(s1, zoom, forma)
    hu = np.array(ct[sl], dtype=np.float32)
    del ct
    etiquetas = [etiquetar(mascara(TS_DIR / caso / 'default6mm' / f'{e}.nii.gz')) for e in ESTRUCTURAS]
    union, _ = limpia(forma, etiquetas, 0.0)
    sin_cierre = union[sl].copy()
    del union
    it = max(1, int(round(CIERRE_MM / float(zoom.min()))))
    hueso = ndi.binary_closing(np.pad(sin_cierre, it), iterations=it)[it:-it, it:-it, it:-it]
    origen = np.array([s.start for s in sl], dtype=np.float64) * zoom
    s1m = mascara(TS_DIR / caso / 'default6mm' / 'vertebrae_S1.nii.gz')[sl]
    return hu, sin_cierre, hueso, zoom, origen, s1m, it


def huecos_interiores(linea: np.ndarray) -> list[tuple[int, int]]:
    """Tramos False encerrados entre dos tramos True de una linea booleana: (inicio, fin exclusivo)."""
    idx = np.flatnonzero(linea)
    if idx.size < 2:
        return []
    out, i0 = [], None
    for k in range(idx[0], idx[-1] + 1):
        if not linea[k] and i0 is None:
            i0 = k
        elif linea[k] and i0 is not None:
            out.append((i0, k))
            i0 = None
    return out


def huecos_2d(m2: np.ndarray) -> np.ndarray:
    """Huecos de un corte: fondo que no toca el borde."""
    lab, n = ndi.label(~m2)
    borde = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    return np.isin(lab, borde, invert=True) & (lab > 0)


def analizar(caso: str, ruta_ct: Path, r1: pd.Series, e9: pd.Series, largo_ref: float) -> tuple[list[str], dict]:
    """Lineas markdown del caso y su fila de resumen (una por caso, para la tabla de la cohorte)."""
    hu, union, B, zoom, origen, s1m, it = envolvente_y_union(caso, ruta_ct, r1)
    c = np.array([e9['c_x_mm'], e9['c_y_mm'], e9['c_z_mm']], dtype=float)
    u = np.array([e9['u_x'], e9['u_y'], e9['u_z']], dtype=float)
    base = sap.pose_base(B, zoom, origen, c, u)
    largo = None if base is None else round(base[1], 1)
    L = [f'### `{caso}`', '',
         f'- voxel {tuple(round(float(z), 3) for z in zoom)} mm; cierre: {it} iteraciones (~{it * zoom.min():.2f} mm)',
         f'- **Control de regresion** (longitud anclada frente a `L_TS_mejor_mm` de E9-TS = {largo_ref} mm, que E12 reproduce): **{largo} mm** -> '
         + ('REPRODUCE' if largo == largo_ref else 'NO REPRODUCE')]
    if largo != largo_ref:
        return (L + ['- Cifras nuevas de este caso **no reportadas** por fallo del control.', ''],
                {'Caso': caso, 'control': 'NO REPRODUCE', 'L_ref_mm': largo_ref, 'L_mm': largo})
    zs = np.flatnonzero(s1m.any(axis=(0, 1)))
    filas = []
    for z in zs:
        x = int(np.median(np.nonzero(s1m[:, :, z])[0]))
        f = {'z': (z - zs[0]) * zoom[2]}
        for nombre, m in (('B', B), ('U', union)):
            gaps = [(a, b) for a, b in huecos_interiores(m[x, :, z]) if b - a >= 2]
            a, b = max(gaps, key=lambda g: g[1] - g[0]) if gaps else (0, 0)
            f[f'gap{nombre}'] = (b - a) * zoom[1]
            f[f'hu{nombre}'] = float(np.median(hu[x, a:b, z])) if b > a else float('nan')
        # voxeles de la linea media que estaban en un hueco interior de la union y el cierre ocupo
        lin_u = np.zeros(B.shape[1], bool)
        for a, b in huecos_interiores(union[x, :, z]):
            lin_u[a:b] = True
        f['cierre_linea'] = float((lin_u & B[x, :, z]).sum() * zoom[1])
        lleno = huecos_2d(union[:, :, z]) & B[:, :, z]
        if lleno.any():
            lab, n = ndi.label(lleno)
            areas = np.bincount(lab.ravel())[1:]
            k = int(areas.argmax()) + 1
            f['area'] = float(areas.max() * zoom[0] * zoom[1])
            f['esp'] = float(2 * ndi.distance_transform_edt(lleno, sampling=zoom[:2]).max())
            f['dx'] = float(abs(np.nonzero(lab == k)[0].mean() - x) * zoom[0])
        else:
            f['area'], f['esp'], f['dx'] = 0.0, 0.0, float('nan')
        filas.append(f)
    d = pd.DataFrame(filas)
    cB, cU = d.gapB > 0, d.gapU > 0
    L += [f'- Cortes axiales analizados: **{len(d)}** (todo el tramo con mascara `vertebrae_S1`)',
          f'- **Canal en la linea media, union sin cierre:** hueco interior en **{int(cU.sum())} de {len(d)}** cortes'
          + (f'; longitud AP mediana {d.gapU[cU].median():.1f} mm; HU mediana {d.huU[cU].median():.0f}' if cU.any() else ''),
          f'- **Canal en la linea media, envolvente `B`:** hueco interior en **{int(cB.sum())} de {len(d)}** cortes'
          + (f'; longitud AP mediana {d.gapB[cB].median():.1f} mm (min {d.gapB[cB].min():.1f}, max '
             f'{d.gapB[cB].max():.1f}); HU mediana {d.huB[cB].median():.0f}' if cB.any() else ''),
          f'- **Cortes con hueco en la union y sin hueco en `B`** (canal cerrado por el cierre en la linea media): '
          f'**{int((cU & ~cB).sum())}**; mm de linea media ocupados por el cierre dentro de huecos de la union: '
          f'max **{d.cierre_linea.max():.1f} mm**',
          f'- **Relleno del cierre** (huecos 2D de la union ocupados por `B`, cualquier posicion): area maxima '
          f'**{d.area.max():.1f} mm2**, espesor 2D maximo **{d.esp.max():.1f} mm**', '',
          '| z desde el primer corte de S1 (mm) | hueco AP union (mm) | hueco AP `B` (mm) | HU hueco `B` '
          '| cierre en linea media (mm) | relleno: area max (mm2) | espesor (mm) | distancia a linea media (mm) |',
          '|---|---|---|---|---|---|---|---|']
    L += [f'| {r.z:.1f} | {r.gapU:.1f} | {r.gapB:.1f} | {r.huB:.0f} | {r.cierre_linea:.1f} | {r.area:.1f} '
          f'| {r.esp:.1f} | {r.dx:.1f} |' for r in d.itertuples()]
    cerr = d[cU & ~cB]
    resumen = {'Caso': caso, 'control': 'REPRODUCE', 'L_ref_mm': largo_ref, 'L_mm': largo,
               'cortes_S1': len(d), 'cortes_hueco_union': int(cU.sum()), 'cortes_hueco_B': int(cB.sum()),
               'cortes_cerrados': int((cU & ~cB).sum()), 'mm_cerrados': float(len(cerr) * zoom[2]),
               'hueco_union_cerrado_max_mm': float(cerr.gapU.max()) if len(cerr) else 0.0,
               'hueco_B_mediana_mm': float(d.gapB[cB].median()) if cB.any() else float('nan'),
               'hu_hueco_B_mediana': float(d.huB[cB].median()) if cB.any() else float('nan'),
               'cierre_linea_max_mm': float(d.cierre_linea.max()),
               'relleno_area_max_mm2': float(d.area.max()), 'relleno_espesor_max_mm': float(d.esp.max())}
    return L + [''], resumen


def main() -> None:
    """Pilotos por defecto; `--cohorte` para los 72 casos (necesita sus mascaras, en Khipu)."""
    global TS_DIR
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ts-dir', type=Path, default=TS_DIR)
    ap.add_argument('--ct-dir', type=Path, default=CT_DIR)
    ap.add_argument('--refs-dir', type=Path, default=OBJ2, help='donde estan r1_landmarks.csv y e9ts_corredor.csv')
    ap.add_argument('--cohorte', action='store_true', help='72 casos de la cohorte primaria del Objetivo 2')
    ap.add_argument('--out', type=Path, default=None, help='reporte markdown (por defecto, a la salida estandar)')
    ap.add_argument('--csv', type=Path, default=None, help='una fila de resumen por caso')
    args = ap.parse_args()
    TS_DIR = args.ts_dir.expanduser()
    refs = args.refs_dir.expanduser()
    r1 = pd.read_csv(refs / 'r1_landmarks.csv', index_col='Caso')
    e9 = pd.read_csv(refs / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
    if args.cohorte:
        from e13_muestreo_sap import cohorte
        casos = list(cohorte(refs, ('grupo 2', 'grupo 3')).index)
    else:
        casos = PILOTOS
    rutas = {p.name[:-len('.nii.gz')]: p for p in args.ct_dir.expanduser().rglob('dataset*_data.nii.gz')}
    L = [f'# r_envolvente_canal (descriptivo, posterior; {len(casos)} casos)', '']
    filas = []
    for i, caso in enumerate(casos, 1):
        try:
            fila = e9[e9.Caso == caso].iloc[0]
            lineas, resumen = analizar(caso, rutas[caso], r1.loc[caso], fila, float(fila['L_TS_mejor_mm']))
        except Exception:  # un caso que falla no detiene la cohorte; queda dicho en el reporte
            lineas = [f'### `{caso}`', '', '- **ERROR**:', '```', traceback.format_exc(), '```', '']
            resumen = {'Caso': caso, 'control': 'ERROR'}
        L += lineas
        filas.append(resumen)
        print(f'[{i}/{len(casos)}] {caso} {resumen["control"]}', file=sys.stderr, flush=True)
        if args.csv:  # se reescribe tras cada caso: si el job se corta, lo hecho queda
            pd.DataFrame(filas).to_csv(args.csv, index=False)
    texto = '\n'.join(L)
    if args.out:
        args.out.write_text(texto, encoding='utf-8')
    else:
        print(texto)


if __name__ == '__main__':
    main()
