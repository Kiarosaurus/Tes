"""Version 2 — aplica la regla de eleccion entre run04, run05a y run05b (aprobada por la autora el 2026-10-14, ANTES de
generar con run05a/run05b; `v2_plan.md`, seccion "Regla de eleccion").

ENTRADA: `d2_perfil.csv` de `d2_perfil_sintetico.py` con los tres puntos de control (`mejor.pt` de cada corrida),
generados en validacion (`0101`, `0102`), 5 semillas, pose corregida. Columnas `<punto>_med` = mediana de los dos
pacientes del exceso de amplitud de Peters por anillo (HU).

REGLA
-----
- Referencia real: D1 con piezas tamano tornillo (500-4000 mm3; `d1_d2_resultado.md`), anillos 0-2 / 2-4 / 4-6 / 6-8 /
  8-10 mm = 1930 / 1199 / 765 / 473 / 174 HU.
- Metrica principal `E` = media de |sintetico - real| en los anillos 2-4, 4-6, 6-8 y 8-10 mm.
- Salvaguarda: un candidato se descarta si su desviacion en 0-2 mm (|sintetico - 1930|) supera en mas de 20 % la de
  run04. Los fallos de control de la cadena ya abortan antes (el job no termina).
- Eleccion por simplicidad: se parte de run04; run05a solo reemplaza al elegido si su `E` es al menos 10 % menor; luego
  run05b, igual, frente al elegido en ese momento. Si el elegido sigue siendo run04, la version 2 "no mejora" y no
  hay corrida final con ella.
- El cotejo de `a17` se reporta al lado (si se pasa `--a17`), no decide. Limitacion: 2 pacientes de validacion.

USO
---
    python experiments/objetivo3/v2_eleccion.py --d2 <d2_perfil.csv> [--a17 <a17_resumen.md>] --out <v2_eleccion.md>
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

REAL = {'0-2': 1930.0, '2-4': 1199.0, '4-6': 765.0, '6-8': 473.0, '8-10': 174.0}   # D1 tornillo, d1_d2_resultado.md
ANILLOS_E = ['2-4', '4-6', '6-8', '8-10']
ORDEN = ['run04_mejor', 'run05a_mejor', 'run05b_mejor']   # de mas simple a mas complejo
MEJORA = 0.10
TOLERANCIA_0_2 = 0.20


def lee_d2(ruta: Path) -> dict[str, dict[str, float]]:
    """{punto: {anillo: exceso mediano}} desde d2_perfil.csv."""
    with open(ruta, newline='', encoding='utf-8') as fh:
        filas = list(csv.DictReader(fh))
    out: dict[str, dict[str, float]] = {}
    for f in filas:
        for col, v in f.items():
            if col.endswith('_med') and not col.startswith('real') and v not in ('', None):
                out.setdefault(col[:-4], {})[f['anillo_mm']] = float(v)
    return out


def aplica(perf: dict[str, dict[str, float]]) -> tuple[str, list[dict]]:
    """Devuelve (elegido, tabla por candidato)."""
    faltan = [p for p in ORDEN if p not in perf]
    if faltan:
        raise SystemExit('faltan puntos en d2_perfil.csv: %s' % faltan)
    tabla = []
    for p in ORDEN:
        e = sum(abs(perf[p][a] - REAL[a]) for a in ANILLOS_E) / len(ANILLOS_E)
        tabla.append({'punto': p, 'E': e, 'dev_0_2': abs(perf[p]['0-2'] - REAL['0-2']),
                      **{a: perf[p][a] for a in REAL}})
    tope = (1.0 + TOLERANCIA_0_2) * tabla[0]['dev_0_2']
    for t in tabla:
        t['salvaguarda'] = t['punto'] == ORDEN[0] or t['dev_0_2'] <= tope
    elegido = tabla[0]
    for t in tabla[1:]:
        t['reemplaza'] = bool(t['salvaguarda'] and t['E'] <= (1.0 - MEJORA) * elegido['E'])
        if t['reemplaza']:
            elegido = t
    return elegido['punto'], tabla


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--d2', type=Path, required=True)
    ap.add_argument('--a17', type=Path, default=None, help='resumen de a17 (se adjunta, no decide)')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    elegido, tabla = aplica(lee_d2(args.d2))
    L = ['# Eleccion de la version 2 (regla aprobada el 2026-10-14)', '',
         'Generado por `v2_eleccion.py` desde `%s`. Validacion (`0101`, `0102`), 5 semillas, `mejor.pt` de cada '
         'corrida. Real: D1 tornillo.' % args.d2.name, '',
         '| punto | 0-2 | 2-4 | 4-6 | 6-8 | 8-10 | E (2-10 mm) | dev 0-2 | salvaguarda 0-2 | reemplaza al anterior |',
         '|---|---|---|---|---|---|---|---|---|---|',
         '| real D1 tornillo | %s | | | | |' % ' | '.join('%.0f' % REAL[a] for a in REAL)]
    for t in tabla:
        L.append('| %s | %s | %.1f | %.1f | %s | %s |' % (
            t['punto'], ' | '.join('%.0f' % t[a] for a in REAL), t['E'], t['dev_0_2'],
            'pasa' if t['salvaguarda'] else 'DESCARTADO', '-' if t['punto'] == ORDEN[0]
            else ('si' if t.get('reemplaza') else 'no')))
    L += ['', 'Regla: E = media de |sintetico - real| en 2-4, 4-6, 6-8 y 8-10 mm. Salvaguarda: dev 0-2 <= %.0f %% mas que '
          'la de run04. Se reemplaza al elegido solo con E al menos %.0f %% menor (orden de simplicidad: %s).'
          % (100 * TOLERANCIA_0_2, 100 * MEJORA, ' -> '.join(ORDEN)), '']
    if elegido == ORDEN[0]:
        L.append('**RESULTADO: ningun modelo de la version 2 mejora a run04 en al menos 10 %. La version 2 se reporta '
                 'como "no mejora" y no hay corrida final con ella.**')
    else:
        L.append('**RESULTADO: elegido `%s`.** Sigue: `Delta` en validacion y corrida final en prueba con ese punto.'
                 % elegido)
    L += ['', 'Limitacion: 2 pacientes de validacion; el cotejo de `a17` se reporta pero no decide.']
    if args.a17 is not None and args.a17.exists():
        L += ['', '## Cotejo de a17 (no decide)', '', args.a17.read_text(encoding='utf-8')]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L[:len(tabla) + 12]))
    print('-> %s' % args.out)


if __name__ == '__main__':
    main()
