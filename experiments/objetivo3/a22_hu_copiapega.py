"""A22 - HU constante de la copia y pegado: mediana del metal real de ENTRENAMIENTO (01-decisiones 2026-10-08 pto 9).

Se mide una sola vez, sobre el conjunto con que se entreno el sintetizador (`a5_manifiesto_train.csv`, criterio R2:
47 casos con material ortopedico), en el corte central de cada parche y solo en la mascara del componente objetivo
(`metal`, > 2500 HU). Ningun paciente de validacion ni de test interviene.

Cierra el `\\GAPDATO` de `capitulo3` (valor de HU de la copia y pegado).

USO
---
    python experiments/objetivo3/a22_hu_copiapega.py
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

_AQUI = Path(__file__).resolve().parent


def main() -> None:
    cache = _AQUI / 'outputs' / 'a1b_cache'
    man = _AQUI / 'outputs' / 'a5' / 'a5_manifiesto_train.csv'
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
           'min': float(v.min()), 'fuente': 'a5_manifiesto_train.csv (R2), corte central, mascara del componente'}
    out = _AQUI / 'outputs' / 'a22'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'a22_hu_copiapega.json').write_text(json.dumps(res, indent=2), encoding='utf-8')
    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    main()
