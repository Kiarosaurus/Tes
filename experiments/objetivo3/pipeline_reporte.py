"""REPORTE.md del script maestro (docs/01-decisiones.md 2026-11-21 (18)). Lee estado.tsv y los resultados de cada etapa.

Uso: python pipeline_reporte.py <carpeta del pipeline>
Nunca falla: lo que no existe se informa como "sin dato".
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REAL = {'0-2': 1930.0, '2-4': 1199.0, '4-6': 765.0, '6-8': 473.0, '8-10': 174.0}
BRAZOS = ['run04_mejor', 'b_min_l0', 'b_min_l0.8_t1000', 'b_min_l3_t300', 'run04_mejor_p100_e0.3', 'aux_C', 'aux_T', 'aux_P', 'aux_A']


def leer_json(p: Path):
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return None


def d2(p: Path, brazo: str):
    try:
        filas = list(csv.DictReader(open(p, encoding='utf-8')))
        m = {f['anillo_mm']: float(f[brazo + '_med']) for f in filas}
        dev = abs(m['0-2'] - REAL['0-2'])
        e = sum(abs(m[k] - REAL[k]) for k in ('2-4', '4-6', '6-8', '8-10')) / 4
        return dev, e
    except Exception:
        return None


def cascaras(p: Path, brazo: str):
    try:
        for l in p.read_text(encoding='utf-8').splitlines():
            if l.startswith('|'):
                c = [x.strip() for x in l.strip().strip('|').split('|')]
                if c and c[0] == brazo and len(c) > 2 and c[2].isdigit():
                    return int(c[2])
    except Exception:
        pass
    return None


def f(x, fmt='%.3f'):
    return 'sin dato' if x is None else fmt % x


def main() -> None:
    out = Path(sys.argv[1])
    L = ['# REPORTE del script maestro (exploratorio; reglas en docs/01-decisiones.md 2026-11-21 (18) y (18-a))', '']
    L += ['## Estado de las etapas', '', '| grupo | etapa | estado | inicio | fin | nota |', '|---|---|---|---|---|---|']
    ests = sorted(out.glob('estado_*.tsv'))
    if ests:
        for est in ests:
            for l in est.read_text(encoding='utf-8').splitlines():
                c = l.split('\t')
                if len(c) >= 2:
                    L.append('| ' + est.stem.replace('estado_', '') + ' | ' + ' | '.join(c[:5] + [''] * (5 - len(c[:5]))) + ' |')
    else:
        L.append('| (sin estado_*.tsv) | | | | | |')
    for v in ('T', 'P', 'A'):
        p = out / ('lambda_%s.txt' % v)
        if p.exists():
            L.append('')
            L.append('lambda de %s: %s' % (v, p.read_text(encoding='utf-8').strip()))
    L += ['', '## Metricas por brazo (validacion 0101/0102; comparador = control `aux_C` (mismo hardware) o, si no existe, `b_min_l0`)', '',
          '| brazo | razon de textura (original: %s) | frac. M < 2500 HU | salto borde G (HU) | cascaras (a) /7 | D2 0-2 mm (dev, tope 279.6) | E 2-10 mm |' %
          f((leer_json(out / 'res' / 'run04_mejor.json') or {}).get('razon_textura_original', {}).get('mediana'), '%.3f'),
          '|---|---|---|---|---|---|---|']
    d2p = out / 'res' / 'd2_perfil.csv'
    ver = out / 'res' / 'veredicto_cascaras.md'
    for b in BRAZOS:
        j = leer_json(out / 'res' / (b + '.json')) or {}
        g = lambda k: (j.get(k) or {}).get('mediana')
        dd = None
        for cand in (out / 'res' / ('d2_' + b) / 'd2_perfil.csv', d2p):
            if cand.exists():
                dd = d2(cand, b)
                if dd:
                    break
        L.append('| %s | %s | %s | %s | %s | %s | %s |' % (
            b, f(g('razon_textura')), f(g('frac_M_bajo_2500')), f(g('salto_borde_G_HU'), '%.0f'),
            f(cascaras(ver, b), '%d') if ver.exists() else 'sin dato',
            f(dd[0] if dd else None, '%.0f'), f(dd[1] if dd else None, '%.0f')))
    L += ['', '## Criterios de (18) frente al control (si hay dato)', '']
    c = leer_json(out / 'res' / 'aux_C.json') or leer_json(out / 'res' / 'b_min_l0.json') or {}   # control del mismo hardware si existe
    ro = (leer_json(out / 'res' / 'run04_mejor.json') or {}).get('razon_textura_original', {}).get('mediana')
    for v in ('aux_T', 'aux_P', 'aux_A'):
        j = leer_json(out / 'res' / (v + '.json'))
        if not j or ro is None or not c:
            L.append('- %s: sin resultados (etapa no ejecutada o fallida; ver estado).' % v)
            continue
        rt, rc = j['razon_textura']['mediana'], c['razon_textura']['mediana']
        i1 = abs(rt - ro) < abs(rc - ro) if rt is not None and rc is not None else None
        i2 = j['frac_M_bajo_2500']['mediana'] <= c['frac_M_bajo_2500']['mediana']
        L.append('- %s: (i) textura mas cerca de la original que el control: %s (%.3f frente a %.3f); (ii) estatica no mayor: %s (%.3f frente a %.3f). '
                 '(iii) cascaras y (iv) D2: ver tabla.' % (v, i1, rt, rc, i2, j['frac_M_bajo_2500']['mediana'], c['frac_M_bajo_2500']['mediana']))
    a20 = out.parent.parent / 'eta_prueba'
    L += ['', '## Corrida en prueba de 100:0.3 (a20)', '']
    for nm in ('a20_test_base.csv', 'a20_val.csv'):
        L.append('- `%s`: %s' % (nm, 'existe' if (a20 / nm).exists() else 'NO existe'))
    L += ['', 'Al volver: bajar los resultados y correr `experiments/objetivo3/evalua_todo_local.sh` (C4, D2, a24, sesion a ciegas).',
          'Todo es exploratorio y post-hoc; nada entra a `overleaf/` sin decision de la autora.']
    (out / 'REPORTE.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
