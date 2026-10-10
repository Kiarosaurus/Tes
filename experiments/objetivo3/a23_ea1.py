"""A23 - E-A1: reconstruccion del implante REAL (diseno_A.md seccion 0; 01-decisiones 2026-10-09 (8)).

QUE HACE
--------
Para cada paciente con metal de la particion pedida:
1. Extrae los parches por **componente** con la misma funcion del entrenamiento (`a1b.analizar`): componentes
   de metal > 2500 HU de al menos **500 mm3**, cada uno con su `B_delta`.
2. Por componente, hasta `--cortes` cortes repartidos (24 por omision). Genera `G` con `mejor_37k`, 5 semillas, y
   lee con `regla_suave` (`delta = 0.05`), como `a15`.
3. Mide, dentro de `G` y frente al CT real:
   - **discrepancia**: MAE en HU en `G`, en `M` y en `B_delta`;
   - **`bone integrity`**: SDC y cambio relativo de volumen del hueso (> 150 HU fuera de `M`);
   - **`metal integrity`**: lo mismo con el metal (> 2500 HU);
   - **exceso de costura**: salto de mediana a traves del borde de `G` en lo generado, menos el del real
     (como `a13`/`a10`).

**Sin `streak amplitude`:** no hay verdad de terreno sin metal (01-decisiones 2026-10-05 (3)).

AGREGACION: mediana sobre parches (componente x corte) -> una cifra por paciente y semilla -> mediana de las
semillas por paciente. Se reportan por separado los pacientes con material ortopedico (`grupo 1`) y con objetos
(`grupo 2`), segun `experiments/exploration-3d/grupos.csv`.

PARTICION: por omision `val`, que sirve de prueba de humo. **Test exige `--corrida-final`.**

USO
---
    python experiments/objetivo3/a23_ea1.py --cortes 2 --semillas 0 --dispositivo cpu             # humo en val
    python experiments/objetivo3/a23_ea1.py --particiones test --corrida-final --dispositivo cuda  # corrida final
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
from pathlib import Path

import numpy as np
import torch

_AQUI = Path(__file__).resolve().parent
_RAIZ = _AQUI.parents[1]
for p in (_RAIZ / 'src' / 'renderizador', _RAIZ / 'src' / 'common', _RAIZ / 'src',
          _RAIZ / 'experiments' / 'objetivo1', _AQUI):
    sys.path.insert(0, str(p))

from datos import ParchesMetal, caso_de  # noqa: E402
from difusion import Difusion, muestrea_ddim  # noqa: E402
from modelo import UNetDifusion  # noqa: E402
from region import componer, verificar_composicion  # noqa: E402
from ventanas import DELTA_OBJ3, decodifica_bloque  # noqa: E402
from a20_evaluador_ea2 import sdc  # noqa: E402

METAL_HU, HUESO_HU, MIN_MM3 = 2500.0, 150.0, 500.0


def anillos2d(g: np.ndarray):
    """Cascaras de un voxel a cada lado del borde de `g` (misma definicion que `a10`/`a13`)."""
    from scipy import ndimage as ndi
    e = ndi.binary_erosion(g, ndi.generate_binary_structure(2, 1), border_value=1)
    d = ndi.binary_dilation(g, ndi.generate_binary_structure(2, 1))
    return g & ~e, d & ~g


def metricas(sal: np.ndarray, real: np.ndarray, M: np.ndarray, g: np.ndarray) -> dict:
    """Las medidas de E-A1 en un parche; NaN donde la region esta vacia."""
    B = g & ~M
    mae = lambda r: float(np.abs(sal[r] - real[r]).mean()) if r.any() else float('nan')  # noqa: E731
    hb, rb = (sal > HUESO_HU) & g & ~M, (real > HUESO_HU) & g & ~M
    hm, rm = (sal > METAL_HU) & g, (real > METAL_HU) & g
    dv = lambda x, y: float((x.sum() - y.sum()) / y.sum()) if y.sum() else float('nan')  # noqa: E731
    ins, out = anillos2d(g)
    exc = float('nan')
    if ins.sum() >= 20 and out.sum() >= 20:
        s_r = abs(float(np.median(real[ins])) - float(np.median(real[out])))
        s_s = abs(float(np.median(sal[ins])) - float(np.median(sal[out])))
        exc = s_s - s_r
    return {'mae_G': mae(g), 'mae_M': mae(M & g), 'mae_B': mae(B), 'hueso_sdc': sdc(hb, rb), 'hueso_dvol': dv(hb, rb),
            'metal_sdc': sdc(hm, rm), 'metal_dvol': dv(hm, rm), 'exceso_costura': exc}


def grupos() -> dict[str, str]:
    with open(_RAIZ / 'experiments' / 'exploration-3d' / 'grupos.csv', newline='', encoding='utf-8-sig') as fh:
        return {f['Caso']: f['Grupo'] for f in csv.DictReader(fh)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--particiones', nargs='+', default=['val'])
    ap.add_argument('--corrida-final', action='store_true', help='permite test (diseno_A.md CONGELADO)')
    ap.add_argument('--particion', type=Path, default=_AQUI.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--ckpt', type=Path, default=_AQUI / 'outputs' / 'a7' / 'run02' / 'mejor.pt')
    ap.add_argument('--cortes', type=int, default=24, help='maximo de cortes por componente, repartidos')
    ap.add_argument('--semillas', type=int, nargs='+', default=[0, 1, 2, 3, 4])
    ap.add_argument('--pasos', type=int, default=50)
    ap.add_argument('--dispositivo', default='cpu')
    ap.add_argument('--casos', nargs='*', default=None, help='subconjunto (por omision, todos los de la particion con metal)')
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'a23')
    args = ap.parse_args()
    if 'test' in args.particiones and not args.corrida_final:
        raise SystemExit('CONTROL: test sin --corrida-final. Abortado.')
    args.out_dir.mkdir(parents=True, exist_ok=True)
    cache = args.out_dir / 'cache'

    # 1. parches por componente, con la funcion del entrenamiento
    from p1_decodificador_sd15 import BDELTA_MM, leer_particion, rutas
    from a1b_parches_componente import PARCHE, analizar
    metas = [m for m in leer_particion(args.particion) if m['particion'] in args.particiones and m['Metal'] == 'si']
    if args.casos:
        metas = [m for m in metas if m['Caso'] in set(args.casos)]
    ubic = rutas(metas, list(args.data))
    gr = grupos()
    for m in metas:
        if not any(cache.glob('%s_c*_k*.npz' % m['Caso'])):
            parches, comps, res = analizar(ubic[m['Caso']], m, PARCHE, BDELTA_MM, MIN_MM3, cache, False)
            print('%s: %d componentes >= %.0f mm3, %d parches' % (m['Caso'], len(comps), MIN_MM3, len(parches)), flush=True)

    # 2. muestra de cortes por componente
    ds = ParchesMetal(cache, args.particion, particiones=tuple(args.particiones))
    pos = {k: i for i, k in enumerate(ds.indice)}
    plan = []
    for serie in sorted(ds.por_caso):
        ks = sorted(ds.por_caso[serie])
        idx = np.linspace(0, len(ks) - 1, min(args.cortes, len(ks))).round().astype(int)
        plan += [(serie, ks[i]) for i in sorted(set(idx))]
    total = len(plan) * len(args.semillas)
    print('parches a generar: %d x %d semillas = %d' % (len(plan), len(args.semillas), total), flush=True)

    ck = torch.load(args.ckpt, map_location='cpu', weights_only=False)
    modelo = UNetDifusion(base=int(ck.get('meta', {}).get('base', 64)))
    modelo.load_state_dict(ck['modelo'])
    modelo.to(args.dispositivo).eval()
    dif = Difusion()

    filas, hecho, t0 = [], 0, time.time()
    for serie, k in plan:
        it = ds[pos[(serie, k)]]
        caso = caso_de(serie)
        crudo = ds._carga(serie, k)
        real, M, g = crudo['hu'], crudo['metal'], crudo['g']
        for sem in args.semillas:
            with torch.no_grad():
                gen = muestrea_ddim(modelo, it['cond'][None].to(args.dispositivo), it['g'][None].to(args.dispositivo),
                                    dif, pasos=args.pasos, semilla=sem).cpu()
            u = (gen.numpy()[0] + 1.0) / 2.0
            sal = componer(real, decodifica_bloque(u, delta=DELTA_OBJ3), g)
            verificar_composicion(real, sal, g)
            filas.append({'caso': caso, 'grupo': gr.get(caso, '?'), 'serie': serie, 'corte': k, 'semilla': sem,
                          'n_M': int(M.sum()), 'n_G': int(g.sum()), **metricas(sal, real, M, g)})
            hecho += 1
            if hecho % 20 == 0:
                print('  [%d/%d] faltan ~%.0f min' % (hecho, total, (time.time() - t0) / hecho * (total - hecho) / 60), flush=True)

    claves = list(filas[0].keys())
    with open(args.out_dir / 'a23_parches.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=claves)
        w.writeheader()
        w.writerows(filas)

    med = ['mae_G', 'mae_M', 'mae_B', 'hueso_sdc', 'hueso_dvol', 'metal_sdc', 'metal_dvol', 'exceso_costura']
    pac = []
    for caso in sorted({f['caso'] for f in filas}):
        fc = [f for f in filas if f['caso'] == caso]
        por_sem = {s: {m: float(np.nanmedian([f[m] for f in fc if f['semilla'] == s])) for m in med}
                   for s in args.semillas}
        pac.append({'caso': caso, 'grupo': fc[0]['grupo'], 'componentes': len({f['serie'] for f in fc}),
                    'parches': len({(f['serie'], f['corte']) for f in fc}),
                    **{m: float(np.nanmedian([por_sem[s][m] for s in args.semillas])) for m in med}})
    with open(args.out_dir / 'a23_pacientes.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(pac[0].keys()))
        w.writeheader()
        w.writerows(pac)
    for gnom in sorted({p['grupo'] for p in pac}):
        sub = [p for p in pac if p['grupo'] == gnom]
        print('%s (n = %d): ' % (gnom, len(sub)) + ' | '.join(
            '%s %.3g [%.3g, %.3g]' % (m, np.nanmedian([p[m] for p in sub]), np.nanmin([p[m] for p in sub]),
                                      np.nanmax([p[m] for p in sub])) for m in med))
    print('-> %s' % (args.out_dir / 'a23_pacientes.csv'))


if __name__ == '__main__':
    main()
