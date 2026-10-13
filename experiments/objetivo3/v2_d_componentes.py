"""Version 2, opcion D-a (`v2_plan.md`) — tabla versionada de componentes tamano tornillo del manifiesto de run04.

QUE HACE
--------
Cruza el manifiesto de entrenamiento de run04 (`a5_manifiesto_train_run04.csv`, 14 182 parches, 39 casos) con
`a1b_componentes.csv` (salida de `a1b_parches_componente.py`, una fila por componente con `vol_mm3`) y marca
`tornillo = 1` en los componentes con volumen en `[--vol-min, --vol-max)` mm3: el mismo rango de D1 tornillo
(500-4000 mm3; `d1_d2_resultado.md`). Escribe una fila por componente (serie) que aparece en el manifiesto.

POR QUE UNA TABLA VERSIONADA
----------------------------
`a1b_componentes.csv` vive en `outputs/` (no se versiona) y el entrenamiento corre en Khipu. Igual que el
manifiesto, el conjunto que se sobremuestrea se congela como archivo auditable: `entrenar.py --componentes` lee esta
tabla y aborta si falta alguna serie del manifiesto.

Esto NO filtra (R4 de `a5_criterio_inclusion.py` sigue sin filtrar): solo dice que se sobremuestrea.

USO (local, donde esta `outputs/a1b/`)
--------------------------------------
    python experiments/objetivo3/v2_d_componentes.py
    python experiments/objetivo3/v2_d_componentes.py --a1b experiments/objetivo3/outputs/a1b/a1b_componentes.csv

Salida: `experiments/objetivo3/v2_d_componentes_run04.csv` y `v2_d_componentes_run04.md` (resumen).
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
VOL_TORNILLO_MM3 = (500.0, 4000.0)  # rango de D1 tornillo (`d1_alcance_rayas.py --vol-max 4000`, VOL_MIN_MM3 = 500)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--a1b', type=Path, default=_AQUI / 'outputs/a1b/a1b_componentes.csv')
    ap.add_argument('--manifiesto', type=Path, default=_AQUI / 'a5_manifiesto_train_run04.csv')
    ap.add_argument('--vol-min', type=float, default=VOL_TORNILLO_MM3[0])
    ap.add_argument('--vol-max', type=float, default=VOL_TORNILLO_MM3[1])
    ap.add_argument('--out', type=Path, default=_AQUI / 'v2_d_componentes_run04.csv')
    args = ap.parse_args()

    if not args.a1b.exists():
        raise SystemExit(f'ABORTA: falta {args.a1b} (salida de a1b_parches_componente.py --out outputs/a1b)')
    with open(args.manifiesto, newline='', encoding='utf-8') as fh:
        parches = Counter((r['Caso'], int(r['comp'])) for r in csv.DictReader(fh))
    with open(args.a1b, newline='', encoding='utf-8') as fh:
        vol = {(r['Caso'], int(r['comp'])): float(r['vol_mm3']) for r in csv.DictReader(fh)}

    faltan = sorted(set(parches) - set(vol))
    if faltan:
        raise SystemExit(f'ABORTA: {len(faltan)} componentes del manifiesto sin fila en {args.a1b}: {faltan[:5]}')

    filas = []
    for (caso, comp), n in sorted(parches.items()):
        v = vol[(caso, comp)]
        filas.append({'Caso': caso, 'comp': comp, 'vol_mm3': v, 'parches': n,
                      'tornillo': int(args.vol_min <= v < args.vol_max)})
    with open(args.out, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['Caso', 'comp', 'vol_mm3', 'parches', 'tornillo'])
        w.writeheader()
        w.writerows(filas)

    n_par = sum(f['parches'] for f in filas)
    t = [f for f in filas if f['tornillo']]
    n_t = sum(f['parches'] for f in t)
    casos_t = sorted({f['Caso'] for f in t})
    L = [f'# Componentes tamano tornillo del manifiesto de run04 (version 2, D-a)', '',
         f'Generado por `v2_d_componentes.py` desde `{args.a1b.name}` y `{args.manifiesto.name}`. '
         f'Rango: [{args.vol_min:.0f}, {args.vol_max:.0f}) mm3.', '',
         '| | componentes | parches | casos |', '|---|---|---|---|',
         f'| manifiesto | {len(filas)} | {n_par} | {len({f["Caso"] for f in filas})} |',
         f'| tamano tornillo | {len(t)} | {n_t} | {len(casos_t)} |', '',
         f'Fraccion natural de parches tamano tornillo: **{n_t / n_par:.4f}**.', '',
         'Factor de sobremuestreo para una fraccion objetivo p: f = p (N - n) / ((1 - p) n), con N y n de arriba.', '']
    for p in (0.25, 0.33, 0.5):
        f = max(1.0, p * (n_par - n_t) / ((1 - p) * n_t)) if n_t else float('nan')
        L.append(f'- p = {p}: f = {f:.2f}')
    L += ['', 'Parches por componente tamano tornillo (para ver cuanto se repite cada uno):', '',
          '| Caso | comp | vol_mm3 | parches |', '|---|---|---|---|']
    L += [f'| {f["Caso"]} | {f["comp"]} | {f["vol_mm3"]:.0f} | {f["parches"]} |' for f in t]
    args.out.with_suffix('.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L[:12]))
    print(f'-> {args.out}')


if __name__ == '__main__':
    main()
