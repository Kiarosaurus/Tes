"""A16 - fija el `delta` de `regla_suave` (v2, #152) SOBRE VALIDACION, contra la verdad.

LA PREGUNTA
-----------
#152 mostro que la `regla` v1 del Objetivo 1 convierte en techo de SW (~236 HU) o de MW (~472 HU) el
metal que LW si marca, cuando el modelo deja el canal estrecho en `u ~ 0.989`. La v2 mezcla los
canales con una rampa de ancho `delta` (`src/common/ventanas.py`). Este script elige `delta`.

POR QUE ASI, Y NO CON `a15`
---------------------------
Elegir `delta` mirando la fraccion de metal de `a15` seria circular: se escogeria la lectura que da el
resultado buscado. Aqui se genera sobre parches de **validacion con metal real**, donde existe la
verdad (`x0`), y se mide el **error de lectura en HU** de cada `delta`. Es la tarea del decodificador:
devolver los HU correctos. `a15` no interviene.

CRITERIO, FIJADO ANTES DE VER EL RESULTADO
------------------------------------------
- **Primario:** `delta` que minimiza la mediana entre pacientes del MAE de HU dentro de `G`.
- **Parsimonia:** entre los `delta` a menos de `EMPATE_HU` = 1 HU de ese minimo, el MENOR (conserva
  mas precision de SW). Anadido tras la prueba de humo con 2 pasos (cifras sin valor), ANTES de la
  corrida real, junto con la grilla hasta 0.5: el argmin caia en el borde de la grilla original.
- **Salvaguarda:** el MAE fuera del metal real (`G` sin `M`) no empeora frente a la v1. Si el
  elegido la viola, se toma el mayor `delta` que la cumple.
- **Cota de robustez, reportada:** distancia al tope `1 - u` que deja el modelo en los canales MW y SW
  donde la verdad esta saturada (`u_verdad = 1`), p50 / p95 / p99.

LIMITE DECLARADO
----------------
Es reconstruccion sobre validacion: si el modelo memorizo apariencias parecidas, puede dejar los
canales mas cerca del tope que en el uso real (pose sintetica), y el `delta` saldria corto. La cota de
robustez y su cotejo con las marcas de `a15` (`u ~ 0.989`, solo como contraste) lo vigilan.
Unidad de analisis: el paciente. `n = 5`.

NO TOCA TEST.

USO
---
    python a16_calibrar_delta.py
    python a16_calibrar_delta.py --cortes 6 --pasos 50
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from pathlib import Path

import numpy as np
import torch

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src' / 'renderizador'))
sys.path.insert(0, str(_RAIZ / 'src' / 'common'))
sys.path.insert(0, str(_RAIZ / 'src'))

from datos import ParchesMetal, caso_de  # noqa: E402
from difusion import Difusion, muestrea_ddim  # noqa: E402
from modelo import UNetDifusion  # noqa: E402
from ventanas import decodifica_bloque, EPS  # noqa: E402

PATRON = re.compile(r'^(?P<serie>.+)_k(?P<k>\d{4})\.npz$')
METAL_HU = 2500.0
DELTAS = (EPS, 0.02, 0.03, 0.05, 0.075, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50)   # EPS = v1; 0.5 = maximo
EMPATE_HU = 1.0   # parsimonia: dentro de 1 HU del minimo se prefiere el `delta` menor (mas SW)


def carga_modelo(ruta: Path):
    ck = torch.load(ruta, map_location='cpu', weights_only=False)
    m = UNetDifusion(base=int(ck.get('meta', {}).get('base', 64)))
    m.load_state_dict(ck['modelo'])
    m.eval()
    return m, ck.get('paso')


def plan_val(cache: Path, particion: Path, cortes: int) -> dict[str, tuple[str, list[int]]]:
    """Serie con mas metal por paciente de validacion, y `cortes` cortes repartidos (como `a13`)."""
    with open(particion, newline='', encoding='utf-8') as fh:
        val = {f['Caso'] for f in csv.DictReader(fh) if f['particion'] == 'val'}
    metal: dict[str, int] = {}
    ks_de: dict[str, list[int]] = {}
    for f in sorted(cache.glob('*.npz')):
        m = PATRON.match(f.name)
        if m is None or caso_de(m.group('serie')) not in val:
            continue
        with np.load(f) as z:
            n = int(z['metal'].sum())
        if n == 0:
            continue
        s = m.group('serie')
        metal[s] = metal.get(s, 0) + n
        ks_de.setdefault(s, []).append(int(m.group('k')))
    elegidas: dict[str, str] = {}
    for s, n in metal.items():
        c = caso_de(s)
        if c not in elegidas or n > metal[elegidas[c]]:
            elegidas[c] = s
    plan = {}
    for c, s in sorted(elegidas.items()):
        ks = sorted(ks_de[s])
        idx = np.linspace(0, len(ks) - 1, min(cortes, len(ks))).round().astype(int)
        plan[c] = (s, [ks[i] for i in sorted(set(idx))])
    return plan


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cache', type=Path, default=aqui / 'outputs' / 'a1b_cache')
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--ckpt', type=Path, nargs='+',
                    default=[aqui / 'outputs' / 'a7' / 'run01' / 'ckpt.pt',
                             aqui / 'outputs' / 'a7' / 'run02' / 'mejor.pt'])
    ap.add_argument('--etiquetas', nargs='+', default=['run01_140k', 'mejor_37k'])
    ap.add_argument('--cortes', type=int, default=6)
    ap.add_argument('--pasos', type=int, default=50)
    ap.add_argument('--semilla', type=int, default=0)
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a16')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    plan = plan_val(args.cache, args.particion, args.cortes)
    if not plan:
        raise SystemExit('ningun paciente de validacion con metal en el cache')
    print('pacientes de validacion con metal: %d' % len(plan))
    for c, (s, ks) in plan.items():
        print('  %-34s %-42s %d cortes' % (c, s, len(ks)))
    total = sum(len(v[1]) for v in plan.values()) * len(args.ckpt)
    print('generaciones: %d | deltas: %s' % (total, ', '.join('%.3g' % d for d in DELTAS)), flush=True)

    dif = Difusion()
    ds = ParchesMetal(args.cache, args.particion, particiones=('val',))
    pos = {k: i for i, k in enumerate(ds.indice)}

    # por (ckpt, caso): voxeles de G con u generado, u verdad y HU verdad
    datos: dict[tuple[str, str], dict[str, list]] = {}
    t0 = time.time()
    hecho = 0
    for ruta, et in zip(args.ckpt, args.etiquetas):
        modelo, paso = carga_modelo(ruta)
        print('\n--- %s (paso %s) ---' % (et, paso), flush=True)
        for caso, (serie, ks) in plan.items():
            d = datos.setdefault((et, caso), {'u': [], 'u_v': [], 'hu_v': []})
            for k in ks:
                i = pos.get((serie, k))
                if i is None:
                    continue
                it = ds[i]
                g = it['g'].numpy()[0].astype(bool)
                u_v = (it['x0'].numpy() + 1.0) / 2.0
                with torch.no_grad():
                    gen = muestrea_ddim(modelo, it['cond'][None], it['g'][None], dif,
                                        pasos=args.pasos, semilla=args.semilla)
                u = (gen.numpy()[0] + 1.0) / 2.0
                d['u'].append(u[:, g].T.astype(np.float32))
                d['u_v'].append(u_v[:, g].T.astype(np.float32))
                d['hu_v'].append(decodifica_bloque(u_v)[g].astype(np.float32))
                hecho += 1
                if hecho % 6 == 0:
                    tr = (time.time() - t0) / hecho * (total - hecho) / 60
                    print('  [%d/%d] %s k%04d | faltan ~%.0f min' % (hecho, total, caso, k, tr),
                          flush=True)

    # --- crudo primero: si el analisis falla, la generacion no se pierde ------------------------
    for (et, caso), d in datos.items():
        if d['u']:
            np.savez_compressed(args.out_dir / ('a16_%s_%s.npz' % (et, caso)),
                                u=np.concatenate(d['u']), u_v=np.concatenate(d['u_v']),
                                hu_v=np.concatenate(d['hu_v']))

    # --- analisis -------------------------------------------------------------------------------
    filas = []
    huecos = {'MW': [], 'SW': []}
    for (et, caso), d in datos.items():
        if not d['u']:
            continue
        u = np.concatenate(d['u'])
        u_v = np.concatenate(d['u_v'])
        hu_v = np.concatenate(d['hu_v']).astype(np.float64)
        for j, nom in ((1, 'MW'), (2, 'SW')):
            sat = u_v[:, j] >= 1.0 - 1e-6
            if sat.any():
                huecos[nom].append(1.0 - u[sat, j])
        metal = hu_v > METAL_HU
        for delta in DELTAS:
            hu = decodifica_bloque(u.T, delta=None if delta == EPS else delta)
            err = np.abs(hu - hu_v)
            filas.append({'ckpt': et, 'caso': caso, 'delta': delta, 'n_G': int(err.size),
                          'n_metal': int(metal.sum()),
                          'mae_G': round(float(err.mean()), 2),
                          'mae_no_metal': round(float(err[~metal].mean()), 2) if (~metal).any() else '',
                          'mae_metal': round(float(err[metal].mean()), 2) if metal.any() else '',
                          'frac_metal_recuperado': round(float((hu[metal] > METAL_HU).mean()), 4)
                          if metal.any() else ''})

    ruta = args.out_dir / 'a16_delta_val.csv'
    with open(ruta, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print('\npor paciente y delta: %s' % ruta)

    print('\ncota de robustez: 1 - u del modelo donde la verdad satura (todos los voxeles juntos)')
    for nom, v in huecos.items():
        if v:
            v = np.concatenate(v)
            print('  %s: n = %d | p50 %.4f | p95 %.4f | p99 %.4f'
                  % (nom, v.size, *np.percentile(v, [50, 95, 99])))

    for et in args.etiquetas:
        print('\n%s: mediana entre pacientes' % et)
        print('  %7s %9s %13s %10s %12s' % ('delta', 'MAE G', 'MAE no metal', 'MAE metal', 'metal rec.'))
        med = {}
        for delta in DELTAS:
            fs = [f for f in filas if f['ckpt'] == et and f['delta'] == delta]
            def m(c):
                v = [f[c] for f in fs if f[c] != '']
                return float(np.median(v)) if v else float('nan')
            med[delta] = (m('mae_G'), m('mae_no_metal'), m('mae_metal'), m('frac_metal_recuperado'))
            print('  %7.3f %9.1f %13.1f %10.1f %12.3f' % (delta, *med[delta]))
        v1_nm = med[EPS][1]
        ok = [d for d in DELTAS if med[d][1] <= v1_nm + 1e-9]
        arg = min(DELTAS, key=lambda d: med[d][0])
        pars = min(d for d in DELTAS if med[d][0] <= med[arg][0] + EMPATE_HU)
        elegido = pars if pars in ok else max(ok)
        print('  -> argmin MAE G: %.3f | parsimonia (+%.0f HU): %.3f | cumple salvaguarda: %s'
              ' | ELEGIDO por el criterio: %.3f'
              % (arg, EMPATE_HU, pars, 'si' if pars in ok else 'NO', elegido))


if __name__ == '__main__':
    main()
