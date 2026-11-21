"""Calibra lambda con la regla de docs/01-decisiones.md 2026-11-21 (18) punto 2 a partir del log de un humo de `entrenar.py`.

lambda = 0.1 x L_v / L_termino, redondeado a una cifra significativa y acotado a [0.001, 1000].
Uso: python pipeline_lambda.py <log> <termino: tex|per>   (imprime el lambda; sale con 1 si no hay cifras finitas)
"""
from __future__ import annotations

import math
import re
import sys


def main() -> int:
    log, t = sys.argv[1], sys.argv[2]
    lv = lt = None
    for linea in open(log, encoding='utf-8', errors='replace'):
        m = re.search(r'^paso \d+/\d+ .*\| L_v ([0-9.eE+-]+) .*?L_%s ([0-9.eE+-]+)' % t, linea)
        if m:
            lv, lt = float(m.group(1)), float(m.group(2))
    if lv is None or not (math.isfinite(lv) and math.isfinite(lt)) or lt <= 0:
        print('sin cifras finitas', file=sys.stderr)
        return 1
    lam = 0.1 * lv / lt
    lam = float('%.1g' % lam)
    lam = min(max(lam, 1e-3), 1e3)
    print('%g' % lam)
    return 0


if __name__ == '__main__':
    sys.exit(main())
