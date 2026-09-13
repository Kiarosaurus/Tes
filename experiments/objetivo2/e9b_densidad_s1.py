"""E9b / Objetivo 2 — densidad del hueso esponjoso de S1: ¿sirve un umbral HU para el corredor?

POR QUE
-------
El piloto de E9 (`e9_corredor.py`, 2026-09-11) midio corredores de 1.6-7.8 mm en volumenes
donde hay tornillos transsacros reales de ~7 mm en S1 (`metal_0008`). La causa, vista a lo
largo del tornillo: el ala sacra tiene HU entre 0 y 100, **por debajo del umbral de hueso de
150 HU**, en tramos de 13 a 33 mm. Si eso es comun, ninguna mascara por umbral representa el
corredor oseo y E9 necesita una segmentacion que rellene la envolvente cortical.

QUE MIDE
--------
Mediana de HU en esferas de 6 mm de radio:
- **cuerpo de S1**: 12 mm por debajo del punto de platillo de R1, en el plano medio;
- **ala sacra izquierda y derecha**: misma altura, a 25 mm del plano medio.

Y la fraccion de voxeles de cada esfera por encima de 150 HU. Una esfera con mediana < 150
HU queda **fuera** de la mascara osea usada por E9 y por `bone integrity` de Peters.

**Limitacion:** las esferas se colocan con distancias fijas respecto al S1 de R1, sin
segmentar el ala; sirven como sonda de densidad, no como medicion anatomica.

Lee `data/`, `r1_landmarks.csv` y `r1_estados.csv`. Escribe `e9b_densidad_s1.csv`.
"""
from __future__ import annotations

import argparse
import csv
import gc
from pathlib import Path

import numpy as np
import pandas as pd

from r1_landmarks import cargar

RADIO_MM = 6.0
BAJO_PLATILLO_MM = 12.0
ALA_LATERAL_MM = 25.0
BONE_HU = 150.0


def esfera(arr: np.ndarray, zoom: np.ndarray, centro: np.ndarray) -> tuple[float, float]:
    """Mediana de HU y fraccion > 150 HU en la esfera."""
    c = centro / zoom
    r = np.ceil(RADIO_MM / zoom).astype(int)
    lo = np.maximum(np.floor(c - r).astype(int), 0)
    hi = np.minimum(np.ceil(c + r).astype(int) + 1, arr.shape)
    sub = np.asarray(arr[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]]).astype(np.float32)
    ii, jj, kk = np.ogrid[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]]
    d2 = ((ii - c[0]) * zoom[0]) ** 2 + ((jj - c[1]) * zoom[1]) ** 2 + ((kk - c[2]) * zoom[2]) ** 2
    v = sub[d2 <= RADIO_MM ** 2]
    if v.size == 0:
        return float('nan'), float('nan')
    return float(np.median(v)), float((v > BONE_HU).mean())


def main() -> None:
    """Recorre calibracion y evaluacion con S1 hallado; reanudable."""
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--max', type=int, default=None)
    args = parser.parse_args()
    r1 = pd.read_csv(here / 'r1_landmarks.csv').set_index('Caso')
    est = pd.read_csv(here / 'r1_estados.csv').set_index('Caso')
    casos = [c for c in est.index[est['cohorte'].isin(['calibracion', 'evaluacion'])]
             if r1.loc[c, 'S1_hallado'] == 'si']
    rutas = {p.name.split('.nii')[0]: p for p in (root / 'data').rglob('*.nii.gz')}
    destino = here / 'e9b_densidad_s1.csv'
    hechos = set(pd.read_csv(destino)['Caso']) if destino.exists() else set()
    campos = ['Caso', 'cohorte', 'hu_cuerpo', 'frac150_cuerpo', 'hu_ala_izq', 'frac150_ala_izq',
              'hu_ala_der', 'frac150_ala_der']
    nuevos = 0
    with destino.open('a' if hechos else 'w', encoding='utf-8', newline='') as h:
        w = csv.DictWriter(h, fieldnames=campos)
        if not hechos:
            w.writeheader()
        for caso in casos:
            if caso in hechos:
                continue
            if args.max is not None and nuevos >= args.max:
                break
            nuevos += 1
            arr, zoom = cargar(rutas[caso])
            f = r1.loc[caso]
            base = np.array([f['S1_x_mm'], f['S1_y_mm'], f['S1_z_mm'] - BAJO_PLATILLO_MM])
            fila = {'Caso': caso, 'cohorte': est.loc[caso, 'cohorte']}
            for nombre, dx in (('cuerpo', 0.0), ('ala_izq', -ALA_LATERAL_MM), ('ala_der', ALA_LATERAL_MM)):
                med, frac = esfera(arr, zoom, base + np.array([dx, 0.0, 0.0]))
                fila[f'hu_{nombre}'] = round(med, 0)
                fila[f'frac150_{nombre}'] = round(frac, 3)
            w.writerow(fila)
            h.flush()
            del arr
            gc.collect()
            print(caso, fila['hu_cuerpo'], fila['hu_ala_izq'], fila['hu_ala_der'], flush=True)


if __name__ == '__main__':
    main()
