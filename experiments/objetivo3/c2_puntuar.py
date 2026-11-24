"""C2: puntua c2/c2_respuestas.csv contra la clave. Descriptivo, exploratorio (ver c2_protocolo.md).
Uso: python -I c2_puntuar.py [ruta_respuestas]"""
import csv, math, sys
from pathlib import Path
from collections import defaultdict
d = Path(__file__).resolve().parent / 'c2'
resp = Path(sys.argv[1]) if len(sys.argv) > 1 else d / 'c2_respuestas.csv'
clave = {r['id']: r['brazo'] for r in csv.DictReader(open(d / 'clave_NO_ABRIR.csv'))}
def wilson(k, n, z=1.96):
    if n == 0: return (float('nan'),) * 2
    p = k / n; den = 1 + z*z/n
    c = (p + z*z/(2*n)) / den; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den
    return c - h, c + h
t = defaultdict(lambda: [0, 0]); sin = 0
for r in csv.DictReader(open(resp)):
    if r['juicio'] not in ('real', 'sint'): sin += 1; continue
    b = clave[r['id']]; t[b][1] += 1; t[b][0] += r['juicio'] == 'real'
print('brazo | juzgados real / n | % | IC95 Wilson'); 
for b in ['real', 'peters_Ti', 'run04_mejor', 'run05a', 'run05b']:
    k, n = t[b]; lo, hi = wilson(k, n)
    print(f'{b:12s} {k}/{n}  {100*k/max(n,1):5.1f}%  [{100*lo:.0f}, {100*hi:.0f}]')
print('sin respuesta:', sin, '| Exploratorio: N=6 por brazo; no confirmatorio.')
