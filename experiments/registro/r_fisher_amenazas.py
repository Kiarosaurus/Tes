"""Recalculo de los valores p de Fisher de las amenazas a la validez (cribado de fractura, #132; tablas de
`docs/04-implicancias.md` 2026-10-04/05). Prueba exacta bilateral de `scipy.stats.fisher_exact`, cuya convencion
bilateral es la *minlike* (suma de las tablas con probabilidad <= la observada; `fay2010two`). Cierra el GAPDATO
"programa y convencion bilateral" si reproduce las cifras registradas.

USO: python experiments/registro/r_fisher_amenazas.py
"""
import scipy
from scipy.stats import fisher_exact

TABLAS = {  # (si estrecho, n estrecho, si control, n control, p registrado)
    'fractura (cualquiera)': (10, 15, 10, 15, 1.000),
    'fractura sacra': (9, 15, 5, 15, 0.272),
    'fractura desplazada': (8, 15, 4, 15, 0.264),
    'fractura sacra y desplazada': (7, 15, 2, 15, 0.109),
}
print('scipy', scipy.__version__)
for nom, (a, na, b, nb, reg) in TABLAS.items():
    p = fisher_exact([[a, na - a], [b, nb - b]], alternative='two-sided')[1]
    print('%-30s p = %.3f | registrado %.3f | %s' % (nom, p, reg, 'IGUAL' if round(p, 3) == reg else 'DISTINTO'))
