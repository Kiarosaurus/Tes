"""Version 2, opcion B — precalcula el canal `T` (plantilla analitica) para cada parche del cache de A1b.

Calcular `T` cuesta ~0.5-1 s por parche (Radon + FBP de 256 x 256 con 360 angulos): al vuelo frenaria el
entrenamiento. Se calcula una vez, en CPU, para TODOS los `.npz` del cache (entrenamiento, validacion y, si el cache
los tiene, prueba: E-A1 los necesita), y se guarda `T` cruda en float32 junto con la escala de normalizacion.

Salida en `--out`: `{serie}_k{corte:04d}_T.npy` (misma base de nombre que el `.npz`) y `escala.json`
(`escala` = p99 de |T| fuera de `M` en una muestra de parches de ENTRENAMIENTO; solo entrenamiento, para no mirar val
ni prueba). Reanudable: lo ya escrito no se recalcula.

USO
---
    python experiments/objetivo3/v2_b_cache_T.py --cache data/a1b_cache --out data/a1b_cache_T --procesos 24
"""
from __future__ import annotations

import argparse
import json
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np

_RAIZ = Path(__file__).resolve().parents[2]
for _p in (str(_RAIZ / 'src'), str(_RAIZ / 'src' / 'renderizador')):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from datos import PATRON, caso_de, lee_particion  # noqa: E402
from plantilla import LAMBDA_T, N_ANG, pix_plano, plantilla, prueba_igual_al_piloto  # noqa: E402

N_ESCALA = 2000
SEMILLA = 20261014


def uno(tarea: tuple[str, str]) -> str:
    entrada, salida = tarea
    if Path(salida).exists():
        return 'ya'
    with np.load(entrada) as z:
        T = plantilla(z['metal'].astype(bool), pix_plano(z['zooms'], int(z['eje'])))
    tmp = salida + '.tmp.npy'
    np.save(tmp, T)
    Path(tmp).replace(salida)
    return 'hecho'


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cache', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--particion', type=Path, default=_RAIZ / 'experiments/objetivo1/p1_particion.csv')
    ap.add_argument('--procesos', type=int, default=8)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    dif = prueba_igual_al_piloto()
    print('control: T igual a la del piloto (diferencia maxima %.2e)' % dif)
    if dif > 1e-5:
        raise SystemExit('ABORTA: la plantilla de src/ no coincide con la del piloto')

    archivos = sorted(f for f in args.cache.glob('*.npz') if PATRON.match(f.name))
    tareas = [(str(f), str(args.out / (f.name[:-4] + '_T.npy'))) for f in archivos]
    print('%d parches en %s; lambda %.4f por mm; %d angulos' % (len(tareas), args.cache, LAMBDA_T, N_ANG), flush=True)
    hechos = 0
    with Pool(args.procesos) as pool:
        for i, r in enumerate(pool.imap_unordered(uno, tareas, chunksize=16), 1):
            hechos += r == 'hecho'
            if i % 1000 == 0 or i == len(tareas):
                print('  %d/%d (%d nuevos)' % (i, len(tareas), hechos), flush=True)

    train = lee_particion(args.particion, ('train',))
    cand = [f for f in archivos if caso_de(PATRON.match(f.name).group('serie')) in train]
    rng = np.random.default_rng(SEMILLA)
    muestra = rng.choice(len(cand), size=min(N_ESCALA, len(cand)), replace=False)
    vals = []
    for j in muestra:
        f = cand[j]
        with np.load(f) as z:
            m = z['metal'].astype(bool)
        if not m.any():
            continue
        T = np.load(args.out / (f.name[:-4] + '_T.npy'))
        vals.append(np.abs(T[~m]))
    escala = float(np.percentile(np.concatenate(vals), 99))
    info = {'escala': escala, 'lambda_por_mm': LAMBDA_T, 'n_ang': N_ANG, 'parches_muestra': len(vals),
            'regla': 'p99 de |T| fuera de M, parches de entrenamiento con metal (semilla %d)' % SEMILLA,
            'parches_total': len(tareas)}
    (args.out / 'escala.json').write_text(json.dumps(info, indent=2), encoding='utf-8')
    print('escala = %.6g -> %s' % (escala, args.out / 'escala.json'))


if __name__ == '__main__':
    main()
