"""E10b — cajas de las mascaras de TS antes y despues de la limpieza por fraccion (#49; decision 2026-09-14 (3)).

POR QUE
-------
La decision del 2026-09-14 (3) fija F = 0.001 y afirma, por inferencia desde `ts_componentes.csv`, que
esa limpieza elimina los 10 desplazamientos de caja entre recortes de `ts_analisis.md` (seccion 3).
Este script lo comprueba sobre las mascaras: recalcula la caja de cada estructura con los dos recortes,
sin limpiar y limpiando con cada F, y la diferencia de caja entre recortes con la misma formula que
`ts_qc.py` (`dif_caja_3v6_max_mm`: maximo |indice 3 mm - indice 6 mm| x zoom, en RAS+).

CONTROL QUE PUEDE FALLAR
------------------------
Con F = 0 debe reproducir `dif_caja_3v6_max_mm` de `ts_qc.csv` (`--ts-qc`). Si no lo reproduce, el
resultado con F > 0 no vale. La comparacion se imprime al final y va a `ts_cajas_limpias_control.csv`.

SALIDA
------
- `ts_cajas_limpias.csv`: caso x estructura x F, voxeles quitados por recorte, caja en mm por recorte y
  `dif_caja_3v6_max_mm`.
- `ts_cajas_limpias_errores.csv`: casos que fallaron (cabecera escrita y volcada al abrir).
Limpieza identica a `e9ts_corredor.limpia`: por estructura, conectividad 26, se quitan componentes con
menos de F x voxeles de la estructura. Reanudable: salta los casos ya escritos.

USO
---
    python ts_cajas_limpias.py --ts-dir ~/metalsynth/data/ts_total --out-dir ~/metalsynth/data/ts_cajas_limpias \
        --ts-qc ~/metalsynth/data/ts_total_qc/ts_qc.csv
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
FRACCIONES = [0.0, 0.001, 0.01, 0.05]
CONECTIVIDAD = np.ones((3, 3, 3), dtype=bool)
UMBRAL_DESPLAZAMIENTO_MM = 10.0

Caja = tuple[np.ndarray, np.ndarray]

CAMPOS = (['Caso', 'estructura', 'F_limpieza']
          + [f'vox_quitados_{m}' for m in MODOS]
          + [f'{e}_{lim}_mm_{m}' for m in MODOS for e in 'xyz' for lim in ('min', 'max')]
          + ['dif_caja_3v6_max_mm'])


def mascara_ras(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Mascara booleana reorientada a RAS+ (como `ts_piloto_qc.mascara`) y su zoom en ese orden."""
    img = nib.load(path)
    ornt = nib.orientations.io_orientation(img.affine)
    m = nib.orientations.apply_orientation(np.asanyarray(img.dataobj) > 0, ornt)
    z = np.array(img.header.get_zooms()[:3], dtype=float)
    zoom = np.empty(3)
    zoom[ornt[:, 0].astype(int)] = z
    return m, zoom


def caja(m: np.ndarray) -> Caja | None:
    """Indices minimo y maximo por eje de los voxeles activos; None si esta vacia (igual que `ts_piloto_qc.caja`)."""
    idx = [np.flatnonzero(m.any(axis=tuple(a for a in range(3) if a != ax))) for ax in range(3)]
    if any(i.size == 0 for i in idx):
        return None
    return np.array([i[0] for i in idx]), np.array([i[-1] for i in idx])


def cajas_por_fraccion(m: np.ndarray) -> dict[float, tuple[Caja | None, int]]:
    """Caja de la mascara tras quitar componentes < F de la estructura, para cada F; y voxeles quitados."""
    cj0 = caja(m)
    if cj0 is None:
        return {f: (None, 0) for f in FRACCIONES}
    sl = tuple(slice(cj0[0][a], cj0[1][a] + 1) for a in range(3))
    lab, _ = ndi.label(m[sl], structure=CONECTIVIDAD)
    tam = np.bincount(lab.ravel())
    n = int(tam[1:].sum())
    out = {}
    for f in FRACCIONES:
        keep = tam >= f * n
        keep[0] = False
        quitados = int(tam[1:][~keep[1:]].sum())
        cj = caja(keep[lab])
        out[f] = (None if cj is None else (cj[0] + cj0[0], cj[1] + cj0[0]), quitados)
    del lab
    return out


def caso(ts_dir: Path, nombre: str) -> list[dict]:
    """Filas estructura x F de un caso."""
    res: dict[tuple[str, str], dict[float, tuple[Caja | None, int]]] = {}
    zoom = None
    for modo in MODOS:
        for est in ESTRUCTURAS:
            m, z = mascara_ras(ts_dir / nombre / modo / f'{est}.nii.gz')
            if zoom is None:
                zoom = z
            elif not np.allclose(z, zoom):
                raise ValueError(f'{modo}/{est}: zoom distinto de las otras mascaras')
            res[modo, est] = cajas_por_fraccion(m)
            del m
        gc.collect()
    filas = []
    for est in ESTRUCTURAS:
        for f in FRACCIONES:
            fila: dict = {'Caso': nombre, 'estructura': est, 'F_limpieza': f}
            for modo in MODOS:
                cj, quitados = res[modo, est][f]
                fila[f'vox_quitados_{modo}'] = quitados
                for a, e in enumerate('xyz'):
                    fila[f'{e}_min_mm_{modo}'] = round(float(cj[0][a] * zoom[a]), 1) if cj is not None else ''
                    fila[f'{e}_max_mm_{modo}'] = round(float(cj[1][a] * zoom[a]), 1) if cj is not None else ''
            ca, cb = res[MODOS[0], est][f][0], res[MODOS[1], est][f][0]
            fila['dif_caja_3v6_max_mm'] = (
                round(float(np.max(np.abs(np.concatenate([(ca[0] - cb[0]) * zoom, (ca[1] - cb[1]) * zoom])))), 1)
                if ca is not None and cb is not None else '')
            filas.append(fila)
    return filas


def abrir(ruta: Path, campos: list[str]):
    """Abre un CSV en modo anexar; si es nuevo o esta vacio, escribe la cabecera y la vuelca ya."""
    nuevo = not ruta.exists() or ruta.stat().st_size == 0
    h = ruta.open('a', encoding='utf-8', newline='')
    w = csv.DictWriter(h, fieldnames=campos)
    if nuevo:
        w.writeheader()
        h.flush()
    return h, w


def control(out: Path, ts_qc: Path) -> None:
    """Compara F = 0 con `dif_caja_3v6_max_mm` de `ts_qc.csv` y resume los desplazamientos por F."""
    import pandas as pd

    d = pd.read_csv(out / 'ts_cajas_limpias.csv')
    q = (pd.read_csv(ts_qc)[['Caso', 'estructura', 'dif_caja_3v6_max_mm']]
         .drop_duplicates(['Caso', 'estructura']).rename(columns={'dif_caja_3v6_max_mm': 'dif_ts_qc'}))
    c = d[d['F_limpieza'] == 0.0].merge(q, on=['Caso', 'estructura'], how='inner')
    if c.empty:
        print('CONTROL NO EJECUTADO: ninguna estructura en comun con ts_qc.csv. El resultado no esta validado.',
              flush=True)
        return
    c['coincide'] = (c['dif_caja_3v6_max_mm'] - c['dif_ts_qc']).abs() <= 0.051
    c.to_csv(out / 'ts_cajas_limpias_control.csv', index=False)
    print(f'CONTROL F = 0 frente a ts_qc.csv: {int(c["coincide"].sum())} de {len(c)} estructuras coinciden '
          f'(tolerancia 0.05 mm)', flush=True)
    if not c['coincide'].all():
        print(c.loc[~c['coincide'], ['Caso', 'estructura', 'dif_caja_3v6_max_mm', 'dif_ts_qc']].to_string(index=False))
    for f, g in d.groupby('F_limpieza'):
        s = g[g['dif_caja_3v6_max_mm'] > UMBRAL_DESPLAZAMIENTO_MM]
        print(f'F = {f}: {s["Caso"].nunique()} casos, {len(s)} estructuras con caja desplazada > '
              f'{UMBRAL_DESPLAZAMIENTO_MM:.0f} mm', flush=True)
        if len(s):
            print(s[['Caso', 'estructura', 'dif_caja_3v6_max_mm']].to_string(index=False), flush=True)


def main() -> None:
    """Recorre los casos de `--ts-dir`; reanudable (`--max`)."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--ts-dir', type=Path, required=True, help='<caso>/<modo>/<estructura>.nii.gz')
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--ts-qc', type=Path, default=None, help='ts_qc.csv para el control con F = 0')
    parser.add_argument('--casos', nargs='*', default=None)
    parser.add_argument('--max', type=int, default=None)
    args = parser.parse_args()

    ts_dir, out = args.ts_dir.expanduser(), args.out_dir.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    casos = args.casos or sorted(d.name for d in ts_dir.iterdir() if d.is_dir() and not d.name.startswith('_'))
    hechos: set[str] = set()
    for nombre in ('ts_cajas_limpias.csv', 'ts_cajas_limpias_errores.csv'):
        ruta = out / nombre
        if ruta.exists() and ruta.stat().st_size > 0:
            with ruta.open(encoding='utf-8') as h:
                hechos |= {r['Caso'] for r in csv.DictReader(h)}
    print(f'{len(casos)} casos en {ts_dir}; {len(hechos)} ya procesados', flush=True)

    s_res = abrir(out / 'ts_cajas_limpias.csv', CAMPOS)
    s_err = abrir(out / 'ts_cajas_limpias_errores.csv', ['Caso', 'Error'])
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
                filas = caso(ts_dir, nombre)
            except Exception as exc:  # un caso roto no detiene la cohorte
                s_err[1].writerow({'Caso': nombre, 'Error': f'{type(exc).__name__}: {exc}'})
                s_err[0].flush()
                print(f'{nombre}: ERROR {exc}', flush=True)
                traceback.print_exc()
                continue
            s_res[1].writerows(filas)
            s_res[0].flush()
            print(f'{nombre}: ok', flush=True)
    finally:
        for h, _ in (s_res, s_err):
            h.close()
    if args.ts_qc is not None:
        control(out, args.ts_qc.expanduser())


if __name__ == '__main__':
    main()
