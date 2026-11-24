"""C2b: puntua c2b_respuestas.csv contra la clave (regla: docs/01-decisiones.md 2026-11-20 (9)). Descriptivo, exploratorio.

Por brazo: puntaje medio, mediana y fraccion con "borde brillante". Pares (mismo paciente y corte) frente a una referencia
(--ref, por omision run04_mejor): cuantos pares tienen puntaje mayor, igual y menor. "Mejora visual" = media >= ref + 0.5 Y
mayor en >= 4 de 6 pares.
Uso: python -I c2b_puntuar.py --clave c2/clave_b_NO_ABRIR.csv --resp c2/c2b_respuestas.csv [--ref run04_mejor]
"""
import argparse, csv
from collections import defaultdict
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('--clave', required=True)
ap.add_argument('--resp', required=True)
ap.add_argument('--ref', default='run04_mejor')
a = ap.parse_args()
clave = {r['id']: r for r in csv.DictReader(open(a.clave))}
pun = defaultdict(list)
bor = defaultdict(list)
par = defaultdict(dict)    # (caso, corte) -> {brazo: puntaje}
sin = 0
for r in csv.DictReader(open(a.resp)):
    c = clave[r['id']]
    if r['puntaje'] == '':
        sin += 1
        continue
    s = int(r['puntaje'])
    pun[c['brazo']].append(s)
    bor[c['brazo']].append(int(r['borde_brillante']))
    par[(c['caso'], c['corte_k'])][c['brazo']] = s
print('brazo | n | media | mediana | % borde brillante')
for b in sorted(pun, key=lambda x: -np.mean(pun[x])):
    print('%-26s %2d  %.2f  %.1f  %3.0f%%' % (b, len(pun[b]), np.mean(pun[b]), np.median(pun[b]), 100 * np.mean(bor[b])))
print('\nPares frente a', a.ref, '(mayor/igual/menor) y regla de mejora visual:')
for b in sorted(pun):
    if b in (a.ref, 'real'):
        continue
    d = [par[k][b] - par[k][a.ref] for k in par if b in par[k] and a.ref in par[k]]
    if not d:
        continue
    mas, ig, men = sum(x > 0 for x in d), sum(x == 0 for x in d), sum(x < 0 for x in d)
    ok = (np.mean(pun[b]) >= np.mean(pun[a.ref]) + 0.5) and mas >= 4
    print('%-26s %d/%d/%d de %d  media %+.2f  -> %s' % (b, mas, ig, men, len(d), np.mean(pun[b]) - np.mean(pun[a.ref]),
                                                      'MEJORA VISUAL' if ok else 'no cumple'))
print('\nsin respuesta:', sin, '| Exploratorio: 6 paneles por brazo; no confirmatorio.')
