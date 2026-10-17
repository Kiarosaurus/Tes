"""Diferencia en mm entre el techo de `vertebrae_S1` (TotalSegmentator) y el platillo de S1 de la localizacion
de referencias (R1), en la cohorte primaria del Objetivo 2.

GAP que atiende
---------------
`overleaf/secciones/capitulo3.tex` l. 513 (ronda capitulo3-r27): "diferencia en milimetros entre el techo de la
etiqueta de S1, que puede estar en la cresta sacra media, y el platillo superior sobre el que se define el marco de
referencia" (implicancia 138). La cifra YA existe por caso en `experiments/objetivo2/ts_nivel_s1.csv`
(`dz_S1_3mm`, `dz_S1_6mm` = `techo_linea_media_dz_mm` de `ts_piloto_qc.techo_dz`: z maxima de la mascara en la
columna x +-5 mm, y +-10 mm alrededor del punto del platillo de R1, menos la z de ese punto). Es la misma diferencia
que usa el control de nivel. Este script solo la resume para los 72 casos de la cohorte; no recalcula mascaras.

Alcance de la medida: el techo medido es el de la etiqueta dentro de la columna (+-10 mm en AP alrededor del punto del
platillo), no el voxel mas craneal de toda la etiqueta, que podria estar en la cresta sacra media; si la columna
alcanza el arco posterior no se comprobo. La diferencia con el voxel mas craneal sigue sin medirse.

Control de regresion
--------------------
Reproduce las cifras de `experiments/objetivo2/ts_analisis.md` §1 desde el mismo CSV: totales por estado (25 "R1
arriba de TS", 125 concordante, 16 sin S1 en R1, 2 sin techo; 168) y, en "evaluacion, clinico ok" concordante,
n = 51, mediana 6.3, min 3.7, max 15.7 mm de `dz_S1_3mm`. Si no reproduce, no imprime la cohorte.

Uso (local, segundos): `python experiments/registro/r_techo_platillo.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

_RAIZ = Path(__file__).resolve().parents[2]
_OBJ2 = _RAIZ / 'experiments' / 'objetivo2'
sys.path.insert(0, str(_OBJ2))

from e13_muestreo_sap import cohorte  # noqa: E402


def main() -> None:
    niv = pd.read_csv(_OBJ2 / 'ts_nivel_s1.csv').set_index('Caso')
    tot = niv['estado_TS'].value_counts().to_dict()
    ok = niv[(niv['estrato'] == 'evaluacion, clinico ok') & (niv['estado_TS'] == 'concordante')]['dz_S1_3mm']
    obs = (tot.get('R1 arriba de TS'), tot.get('concordante'), tot.get('sin S1 en R1'), tot.get('sin techo'),
           len(niv), len(ok), round(ok.median(), 1), round(ok.min(), 1), round(ok.max(), 1))
    esperado = (25, 125, 16, 2, 168, 51, 6.3, 3.7, 15.7)
    print('CONTROL: observado %s, esperado %s -> %s' % (obs, esperado, 'REPRODUCE' if obs == esperado else
                                                          'NO REPRODUCE'))
    if obs != esperado:
        return

    coh = cohorte(_OBJ2, ('grupo 2', 'grupo 3'))
    sub = niv.loc[niv.index.intersection(coh.index)]
    print('cohorte primaria: %d casos; con dz en ts_nivel_s1: %d' % (len(coh), len(sub)))
    for col in ('dz_S1_6mm', 'dz_S1_3mm'):
        v = sub[col].dropna().to_numpy()
        q1, q3 = np.percentile(v, [25, 75])
        print('%s (mm, techo TS menos platillo R1): n %d, mediana %.1f, RIC [%.1f, %.1f], min %.1f, max %.1f; '
              '>= 10 mm: %d; < 0: %d' % (col, v.size, np.median(v), q1, q3, v.min(), v.max(), int((v >= 10).sum()),
                                         int((v < 0).sum())))
    dif = (sub['dz_S1_6mm'] - sub['dz_S1_3mm']).abs()
    print('|dz_6mm - dz_3mm| maximo: %.1f mm' % dif.max())
    for g in ('grupo 2', 'grupo 3'):
        v = sub.loc[coh.loc[sub.index, 'Grupo'] == g, 'dz_S1_6mm'].dropna()
        print('  %s: n %d, mediana %.1f, min %.1f, max %.1f' % (g, len(v), v.median(), v.min(), v.max()))


if __name__ == '__main__':
    main()
