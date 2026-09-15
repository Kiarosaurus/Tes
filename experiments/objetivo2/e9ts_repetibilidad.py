"""Compara dos corridas de `e9ts_corredor.py` fila a fila (control de repetibilidad que puede fallar).

POR QUE
-------
La corrida con `--modo-laminas robust3mm` (2026-09-14) repite todo el calculo de E9-TS solo para cambiar
las laminas. Su CSV deberia ser identico al de la primera corrida (51505): mismo codigo, mismas mascaras,
mismos CT. Si difiere, el calculo no es determinista o cambio un insumo, y hay que saberlo antes de citar
cifras con el recorte de 3 mm.

Compara por (Caso, modo, F_limpieza, politica_metal) todas las columnas de resultado salvo `segundos`.
Imprime `IDENTICO` o `DIFIERE` con el detalle; sale con codigo 1 si difiere o si no hay filas en comun.

USO
---
    python e9ts_repetibilidad.py --a ~/metalsynth/data/e9ts/e9ts_corredor.csv --b ~/metalsynth/data/e9ts_3mm/e9ts_corredor.csv
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

CLAVE = ['Caso', 'modo', 'F_limpieza', 'politica_metal']
IGNORAR = {'segundos'}


def main() -> int:
    """Compara y devuelve 0 si las dos corridas son identicas."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--a', type=Path, required=True)
    parser.add_argument('--b', type=Path, required=True)
    parser.add_argument('--tol', type=float, default=0.0, help='tolerancia absoluta en columnas numericas')
    args = parser.parse_args()

    a = pd.read_csv(args.a.expanduser()).set_index(CLAVE).sort_index()
    b = pd.read_csv(args.b.expanduser()).set_index(CLAVE).sort_index()
    solo_a, solo_b = a.index.difference(b.index), b.index.difference(a.index)
    comunes = a.index.intersection(b.index)
    print(f'filas: A {len(a)}, B {len(b)}, en comun {len(comunes)}, solo A {len(solo_a)}, solo B {len(solo_b)}')
    if len(comunes) == 0:
        print('DIFIERE: ninguna fila en comun; el control no compara nada.')
        return 1
    cols = [c for c in a.columns if c in b.columns and c not in IGNORAR]
    a, b = a.loc[comunes, cols], b.loc[comunes, cols]
    distintas = {}
    for c in cols:
        x, y = a[c], b[c]
        numericas = all(pd.api.types.is_numeric_dtype(s) and not pd.api.types.is_bool_dtype(s) for s in (x, y))
        if numericas:
            dif = (x - y).abs()
            malas = ~((dif <= args.tol) | (x.isna() & y.isna()))
            if malas.any():
                distintas[c] = (int(malas.sum()), float(np.nanmax(dif[malas])))
        else:
            malas = ~((x.astype(str) == y.astype(str)) | (x.isna() & y.isna()))
            if malas.any():
                distintas[c] = (int(malas.sum()), float('nan'))
    if not distintas and len(solo_a) == 0 and len(solo_b) == 0:
        print(f'IDENTICO: {len(comunes)} filas x {len(cols)} columnas (tolerancia {args.tol}).')
        return 0
    print('DIFIERE:')
    for c, (n, m) in sorted(distintas.items(), key=lambda kv: -kv[1][0]):
        print(f'  {c}: {n} filas distintas, max |dif| {m}')
    if len(solo_a) or len(solo_b):
        print(f'  filas sin pareja: solo A {len(solo_a)}, solo B {len(solo_b)}')
    return 1


if __name__ == '__main__':
    sys.exit(main())
