"""Razon de parches de solo banda en el conjunto de entrenamiento de run04 (GAPDATO de `capitulo3`).

Reconstruye el manifiesto de run04 desde `outputs/a5/a5_manifiesto_train.csv` con las retiradas de `a7_run04.sbatch`
(7 secundarios de #163, `metal_0003` por #166, y los 3 componentes no ortopedicos de #167) y comprueba que da 14 182
parches y 39 casos. Razon = parches sin metal (`n_metal` = 0) / parches con metal.

USO: python experiments/registro/r_razon_banda_run04.py
"""
from pathlib import Path

import pandas as pd

A5 = Path(__file__).resolve().parents[1] / 'objetivo3' / 'outputs' / 'a5' / 'a5_manifiesto_train.csv'
SECUNDARIOS = ('0020', '0026', '0027', '0038', '0005', '0052', '0041', '0003')
m = pd.read_csv(A5)
r = m[~m.Caso.apply(lambda c: any('metal_' + s in c for s in SECUNDARIOS))]
no_orto = (r.Caso.str.contains('metal_0045') & r.comp.isin([0, 1])) | (r.Caso.str.contains('metal_0062') & (r.comp == 2))
r = r[~no_orto]
if (len(r), r.Caso.nunique()) != (14182, 39):
    raise SystemExit('CONTROL: el manifiesto reconstruido no es el de run04 (%d, %d)' % (len(r), r.Caso.nunique()))
for nom, d in (('a5 completo (antes de retirar)', m), ('run04', r)):
    nb, nm = int((d.n_metal == 0).sum()), int((d.n_metal > 0).sum())
    print('%-32s solo banda %5d | con metal %5d | razon %.3f' % (nom, nb, nm, nb / nm))
