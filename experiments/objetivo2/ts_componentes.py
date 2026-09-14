"""E10 — componentes conexas de las mascaras de TotalSegmentator (#49, opcion e; decision 2026-09-14).

POR QUE
-------
La decision del 2026-09-14 fija la limpieza de fragmentos como "eliminar componentes menores que una
fraccion (a fijar) del volumen de su estructura", no "componente mayor", porque un sacro fracturado
puede ser dos componentes grandes y legitimos. Este script **no fija la fraccion**: mide la
distribucion de tamanos y distancias de los componentes para que la autora la fije con datos, y para
comprobar que la regla elimina los 10 desplazamientos de caja de `ts_analisis.md` (seccion 3).

QUE MIDE (por caso x recorte x estructura)
-----------------------------------------
Estructuras: `sacrum`, `vertebrae_S1`, `hip_left`, `hip_right` y la union `sacrum+vertebrae_S1`
(la que usara E9: un fragmento en el borde entre las dos etiquetas no es fragmento en la union).
Conectividad 26.

1. `ts_componentes_resumen.csv`, una fila por estructura: voxeles, numero de componentes (total y
   con >= 10 voxeles), voxeles y fraccion del mayor y del segundo, voxeles fuera del mayor.
2. `ts_componentes.csv`, una fila por componente con >= 10 voxeles (y siempre el mayor): rango,
   voxeles, mL, fraccion de la estructura, extension de su caja en mm, distancia minima entre su
   caja y la del mayor en mm (0 si se solapan) y caras del volumen que toca.
3. `ts_componentes_errores.csv`: casos que fallaron.

Distancias en mm = indices x `zooms` del encabezado, sin reorientar: sirven para tamanos y
separaciones, no para cruzar coordenadas con R1 o E9b. Reanudable: salta los casos ya escritos.

USO
---
Khipu (ver `KHIPU.md`, seccion E10):
    python ts_componentes.py --ts-dir ~/metalsynth/data/ts_total --out-dir ~/metalsynth/data/ts_componentes
"""
from __future__ import annotations

import argparse
import csv
import gc
import traceback
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi

MODOS = ['robust3mm', 'default6mm']
ESTRUCTURAS = ['sacrum', 'vertebrae_S1', 'hip_left', 'hip_right']
UNIONES = {'sacrum+vertebrae_S1': ('sacrum', 'vertebrae_S1')}
MIN_VOX = 10
CONECTIVIDAD = np.ones((3, 3, 3), dtype=bool)

CAMPOS_RES = ['Caso', 'modo', 'estructura', 'n_vox', 'n_comp', 'n_comp_min10', 'vox_mayor', 'frac_mayor',
              'vox_segundo', 'frac_segundo', 'vox_fuera_mayor']
CAMPOS_COMP = ['Caso', 'modo', 'estructura', 'rango', 'n_vox', 'vol_ml', 'frac_estructura',
               'ext_x_mm', 'ext_y_mm', 'ext_z_mm', 'dist_caja_mayor_mm', 'toca_borde']


def caja_mm_distancia(a: tuple[slice, ...], b: tuple[slice, ...], zoom: np.ndarray) -> float:
    """Distancia minima entre dos cajas de indices, en mm (0 si se solapan)."""
    gap = [max(0, a[k].start - b[k].stop + 1, b[k].start - a[k].stop + 1) for k in range(3)]
    return round(float(np.sqrt(np.sum((np.array(gap) * zoom) ** 2))), 1)


def medir(m: np.ndarray, zoom: np.ndarray, forma: np.ndarray) -> tuple[dict, list[dict]]:
    """Resumen y componentes de una mascara booleana del volumen completo."""
    n = int(m.sum())
    if n == 0:
        return {'n_vox': 0, 'n_comp': 0, 'n_comp_min10': 0, 'vox_mayor': 0, 'frac_mayor': float('nan'),
                'vox_segundo': 0, 'frac_segundo': float('nan'), 'vox_fuera_mayor': 0}, []
    # Recorte a la caja de la mascara: etiquetar el volumen entero es lento y no cambia nada.
    idx = [np.flatnonzero(m.any(axis=tuple(a for a in range(3) if a != ax))) for ax in range(3)]
    off = np.array([i[0] for i in idx])
    sl = tuple(slice(i[0], i[-1] + 1) for i in idx)
    lab, nc = ndi.label(m[sl], structure=CONECTIVIDAD)
    tam = np.bincount(lab.ravel())[1:]
    objs = ndi.find_objects(lab)
    orden = np.argsort(tam)[::-1]
    mayor = int(orden[0])
    vox_ml = float(np.prod(zoom)) / 1000.0
    res = {'n_vox': n, 'n_comp': int(nc), 'n_comp_min10': int((tam >= MIN_VOX).sum()),
           'vox_mayor': int(tam[mayor]), 'frac_mayor': round(float(tam[mayor]) / n, 5),
           'vox_segundo': int(tam[orden[1]]) if nc > 1 else 0,
           'frac_segundo': round(float(tam[orden[1]]) / n, 5) if nc > 1 else 0.0,
           'vox_fuera_mayor': int(n - tam[mayor])}
    comps = []
    for rango, k in enumerate(orden, start=1):
        if rango > 1 and tam[k] < MIN_VOX:
            break
        o = objs[k]
        glob = tuple(slice(o[a].start + off[a], o[a].stop + off[a]) for a in range(3))
        borde = [f'{e}-' for a, e in enumerate('xyz') if glob[a].start == 0]
        borde += [f'{e}+' for a, e in enumerate('xyz') if glob[a].stop == forma[a]]
        comps.append({'rango': rango, 'n_vox': int(tam[k]), 'vol_ml': round(float(tam[k]) * vox_ml, 3),
                      'frac_estructura': round(float(tam[k]) / n, 5),
                      'ext_x_mm': round((o[0].stop - o[0].start) * float(zoom[0]), 1),
                      'ext_y_mm': round((o[1].stop - o[1].start) * float(zoom[1]), 1),
                      'ext_z_mm': round((o[2].stop - o[2].start) * float(zoom[2]), 1),
                      'dist_caja_mayor_mm': 0.0 if rango == 1 else caja_mm_distancia(o, objs[mayor], zoom),
                      'toca_borde': ','.join(borde)})
    del lab
    return res, comps


def caso(ts_dir: Path, nombre: str) -> tuple[list[dict], list[dict]]:
    """Mide las 5 estructuras con los dos recortes de un caso."""
    filas_res, filas_comp = [], []
    for modo in MODOS:
        masks = {}
        zoom = forma = None
        for est in ESTRUCTURAS:
            img = nib.load(ts_dir / nombre / modo / f'{est}.nii.gz')
            z, f = np.array(img.header.get_zooms()[:3], dtype=float), np.array(img.shape[:3])
            if zoom is None:
                zoom, forma = z, f
            elif not (np.allclose(z, zoom) and np.array_equal(f, forma)):
                raise ValueError(f'{modo}/{est}: rejilla distinta de las otras mascaras')
            masks[est] = np.asanyarray(img.dataobj) > 0
        for nueva, partes in UNIONES.items():
            masks[nueva] = np.logical_or.reduce([masks[p] for p in partes])
        for est, m in masks.items():
            res, comps = medir(m, zoom, forma)
            base = {'Caso': nombre, 'modo': modo, 'estructura': est}
            filas_res.append({**base, **res})
            filas_comp += [{**base, **c} for c in comps]
        del masks
        gc.collect()
    return filas_res, filas_comp


def abrir(ruta: Path, campos: list[str]):
    """Abre un CSV en modo anexar; escribe la cabecera si es nuevo."""
    nuevo = not ruta.exists()
    h = ruta.open('a', encoding='utf-8', newline='')
    w = csv.DictWriter(h, fieldnames=campos)
    if nuevo:
        w.writeheader()
    return h, w


def main() -> None:
    """Recorre los casos de `--ts-dir`; reanudable (`--max`)."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--ts-dir', type=Path, required=True, help='<caso>/<modo>/<estructura>.nii.gz')
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--casos', nargs='*', default=None)
    parser.add_argument('--max', type=int, default=None)
    args = parser.parse_args()

    ts_dir, out = args.ts_dir.expanduser(), args.out_dir.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    casos = args.casos or sorted(d.name for d in ts_dir.iterdir() if d.is_dir() and not d.name.startswith('_'))
    hechos: set[str] = set()
    for nombre in ('ts_componentes_resumen.csv', 'ts_componentes_errores.csv'):
        if (out / nombre).exists():
            with (out / nombre).open(encoding='utf-8') as h:
                hechos |= {r['Caso'] for r in csv.DictReader(h)}
    print(f'{len(casos)} casos en {ts_dir}; {len(hechos)} ya procesados', flush=True)

    s_res = abrir(out / 'ts_componentes_resumen.csv', CAMPOS_RES)
    s_comp = abrir(out / 'ts_componentes.csv', CAMPOS_COMP)
    s_err = abrir(out / 'ts_componentes_errores.csv', ['Caso', 'Error'])
    nuevos = 0
    try:
        for nombre in casos:
            if nombre in hechos:
                continue
            if not all((ts_dir / nombre / m / '.ok').exists() for m in MODOS):
                print(f'{nombre}: sin .ok en algun recorte, se salta', flush=True)
                continue
            if args.max is not None and nuevos >= args.max:
                break
            nuevos += 1
            try:
                res, comps = caso(ts_dir, nombre)
            except Exception as exc:  # un caso roto no detiene la cohorte
                s_err[1].writerow({'Caso': nombre, 'Error': f'{type(exc).__name__}: {exc}'})
                s_err[0].flush()
                print(f'{nombre}: ERROR {exc}', flush=True)
                traceback.print_exc()
                continue
            s_res[1].writerows(res)
            s_comp[1].writerows(comps)
            s_res[0].flush()
            s_comp[0].flush()
            print(f'{nombre}: ok ({len(comps)} componentes >= {MIN_VOX} vox)', flush=True)
    finally:
        for h, _ in (s_res, s_comp, s_err):
            h.close()


if __name__ == '__main__':
    main()
