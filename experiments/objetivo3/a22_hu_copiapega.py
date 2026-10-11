"""A22 - HU constante de la copia y pegado: mediana del metal real de ENTRENAMIENTO (01-decisiones 2026-10-08 pto 9).

Se mide sobre el conjunto con que se entreno el sintetizador, en el corte central de cada parche y solo en la
mascara del componente objetivo (`metal`, > 2500 HU). Ningun paciente de validacion ni de test interviene.
Por omision, el de run04 (`a5_manifiesto_train_run04.csv`, 39 casos, 14 182 parches; 01-decisiones 2026-10-11 (2)
punto 3). El valor de 2026-10-09 (8) (5373 HU) salio de `outputs/a5/a5_manifiesto_train.csv` (47 casos, run02):
se reproduce con `--manifiesto outputs/a5/a5_manifiesto_train.csv --out-dir outputs/a22_run02`.

Cierra el `\\GAPDATO` de `capitulo3` (valor de HU de la copia y pegado).

USO
---
    python experiments/objetivo3/a22_hu_copiapega.py                 # run04 -> outputs/a22_run04/
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

_AQUI = Path(__file__).resolve().parent


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--manifiesto', type=Path, default=_AQUI / 'a5_manifiesto_train_run04.csv')
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'a22_run04')
    args = ap.parse_args()
    cache = _AQUI / 'outputs' / 'a1b_cache'
    man = args.manifiesto
    vals, casos, faltan, n_parches = [], set(), 0, 0
    with open(man, newline='', encoding='utf-8') as fh:
        for f in csv.DictReader(fh):
            ruta = cache / ('%s_c%03d_k%04d.npz' % (f['Caso'], int(f['comp']), int(f['corte'])))
            if not ruta.exists():
                faltan += 1
                continue
            z = np.load(ruta)
            n_parches += 1
            if z['metal'].any():
                vals.append(z['hu'][z['metal']].astype(np.float32))
                casos.add(f['Caso'])
    if faltan:
        raise SystemExit('CONTROL: faltan %d parches del manifiesto en el cache' % faltan)
    v = np.concatenate(vals)
    res = {'HU_copiapega': float(np.median(v)), 'n_voxeles': int(v.size), 'n_parches': n_parches,
           'n_casos_con_metal': len(casos), 'p25': float(np.percentile(v, 25)), 'p75': float(np.percentile(v, 75)),
           'min': float(v.min()), 'fuente': '%s (R2), corte central, mascara del componente' % man.name}
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    (out / 'a22_hu_copiapega.json').write_text(json.dumps(res, indent=2), encoding='utf-8')
    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    main()
