"""A5 / Diseno A — criterio de inclusion del conjunto de entrenamiento (R1-R3) y su validacion.

DE DONDE SALE
-------------
De la reevaluacion de #109 (2026-09-21), despues de que la revision de 40 laminas (#104) mostrara
que el criterio anterior acertaba 16 de 40. Lo que se descarto ahi y **no** se reimplementa aqui:
filtrar por **forma** (PCA tipo tornillo) o por **volumen** (>= 200 mm3). El renderizador aprende la
relacion **mascara -> artefacto**, que es fisica y no depende de si el objeto es tornillo, placa o
fragmento; filtrar por forma tira datos que ensenan justo lo que se quiere aprender.

LA PREGUNTA QUE DECIDE CADA REGLA
---------------------------------
No "¿esto es un tornillo?" sino **"¿este ejemplo ensena algo que en sintesis sera falso?"**.

- **R1 — dentro del cuerpo.** Un electrodo o una cremallera tienen contexto de aire y piel; en
  sintesis el tornillo va en hueso. Es una brecha de contexto real. Se decide con `mascara_cuerpo()`
  (> -400 HU, componente mayor, huecos rellenos), la misma de A4.
- **R2 — el caso tiene material ortopedico.** Version barata de R1 a nivel de caso, y **solo en la
  direccion que concluye**: si el caso NO tiene material ortopedico, ningun componente suyo puede ser
  un implante. La direccion contraria no dice nada (#110, verificada contra los 40 veredictos con
  cero contradicciones).
- **R3 — el parche contiene metal del componente objetivo.** Ataca el numero mas grande de #104: el
  **42.5%** de los parches no tiene ningun voxel del implante. Ensenarian "rellena una banda vacia",
  y en sintesis toda `G` tiene metal por construccion. **No se eliminan del todo**: la banda mas alla
  de la punta es real, asi que se conserva una proporcion declarada (`--ratio-banda`).

- **R4 NO es un filtro.** Tamano y forma se reportan como estratificacion. Aqui solo se imprimen.

QUE MIDE ESTE SCRIPT
--------------------
1. Cuantos parches, componentes y casos sobreviven a cada regla (sobre `a1b_parches.csv`).
2. El **acuerdo del criterio contra los 40 veredictos de la autora**, sobre **la misma muestra** ya
   revisada — la regla fijada de antemano en #104 prohibe generar una muestra nueva para esto.

El criterio se evalua como binario **incluir / excluir**, no como clasificador de tipo: eso es lo
que la reevaluacion de #109 concluyo que importa.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import nibabel as nib
import numpy as np

_AQUI = Path(__file__).resolve().parent
_RAIZ = _AQUI.parents[1]
for _p in (str(_RAIZ / 'experiments/objetivo1'), str(_AQUI)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from a4_html_componentes import CUERPO_HU, mascara_cuerpo  # noqa: E402
from e6c_techo_lw import METAL_HU  # noqa: E402
from p1_decodificador_sd15 import leer_particion, rutas  # noqa: E402

# Veredictos de la autora que corresponden a "debe entrar al entrenamiento".
# `dudoso` se excluye del calculo de acuerdo, no se fuerza a un lado.
INCLUIR = {'tornillo', 'otro implante', 'fragmento'}
EXCLUIR = {'externo', 'diu', 'no es metal'}


def tipo_caso(revision: Path) -> dict[str, str]:
    with open(revision, newline='', encoding='utf-8-sig') as fh:
        return {r['Caso']: (r['Tipo de estructura observada'] or '')
                for r in csv.DictReader(fh)}


def con_ortopedico(tipo: str) -> bool:
    """R2. El texto puede traer mojibake por la codificacion original de `revision.csv`."""
    return 'ortop' in tipo.lower().replace('�', 'o')


def fraccion_dentro(caso: str, comps: list[int], ruta: Path,
                    min_mm3: float = 10.0) -> dict[int, float]:
    """R1. Fraccion de cada componente que cae dentro del cuerpo. Una carga de volumen por caso."""
    from scipy import ndimage as ndi

    img = nib.load(ruta)
    arr = img.get_fdata(dtype=np.float32)
    vox = float(np.prod(img.header.get_zooms()[:3]))
    cuerpo = mascara_cuerpo(arr, CUERPO_HU)
    etiquetas, n = ndi.label(arr > METAL_HU)
    tam = np.bincount(etiquetas.ravel())
    validos = [j for j in range(1, n + 1) if tam[j] * vox >= min_mm3]
    out: dict[int, float] = {}
    for ci in comps:
        if ci >= len(validos):
            continue
        m = etiquetas == validos[ci]
        out[ci] = float((m & cuerpo).sum()) / float(max(m.sum(), 1))
    del arr, cuerpo, etiquetas
    return out


def _conjunto(filas: list[dict], tipos: dict[str, str], args, out: Path, part: str) -> list[dict]:
    """Aplica R2 + R3 a una particion y escribe su manifiesto. Devuelve los parches incluidos.

    **R1-R3 se aplican IGUAL a `train` y a `val`.** Aplicarlas solo a entrenamiento dejaria una
    validacion con casos cuyo unico metal es un accesorio (#105): ahi no hay implante que generar,
    asi que cualquier metrica medida sobre ellos —en particular el margen `Delta` de D4— saldria
    diluida y artificialmente favorable.
    """
    r2 = [r for r in filas if con_ortopedico(tipos.get(r['Caso'], ''))]
    con_metal = [r for r in r2 if int(r['n_metal']) > 0]
    solo_banda = [r for r in r2 if int(r['n_metal']) == 0]
    rng = np.random.default_rng(args.semilla)
    cupo = int(round(args.ratio_banda * len(con_metal)))
    idx = rng.permutation(len(solo_banda))[:min(cupo, len(solo_banda))]
    final = con_metal + [solo_banda[i] for i in sorted(idx)]
    man = sorted(final, key=lambda r: (r['Caso'], int(r['comp']), int(r['corte'])))
    with open(out / f'a5_manifiesto_{part}.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['Caso', 'comp', 'corte', 'n_metal', 'n_G'],
                           extrasaction='ignore')
        w.writeheader(); w.writerows(man)
    nb = sum(1 for r in man if int(r['n_metal']) == 0)
    print(f'  [{part}] {len(filas)} -> {len(man)} parches ({len(man) - nb} con metal, {nb} banda) | '
          f'{len({r["Caso"] for r in man})} casos de {len({r["Caso"] for r in filas})}', flush=True)
    return man


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--parches', type=Path, default=_AQUI / 'outputs/a1b/a1b_parches.csv')
    p.add_argument('--planilla', type=Path, default=_AQUI / 'a3_revision_componentes.csv')
    p.add_argument('--revision', type=Path,
                   default=_RAIZ / 'experiments/exploration-3d/revision.csv')
    p.add_argument('--particion', type=Path,
                   default=_RAIZ / 'experiments/objetivo1/p1_particion.csv')
    p.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--dentro-min', type=float, default=0.5,
                   help='R1: fraccion minima del componente dentro del cuerpo')
    p.add_argument('--ratio-banda', type=float, default=0.62,
                   help='R3: parches de solo banda por cada uno con metal. 0.62 = todos los disponibles (decision 2026-09-21); 1.40 seria el de sintesis, inalcanzable')
    p.add_argument('--semilla', type=int, default=20260921)
    p.add_argument('--particiones', nargs='+', default=['train', 'val'],
                   help='R1-R3 se aplican IGUAL a train y val: val tambien debe cumplir R2')
    args = p.parse_args()

    out = args.out.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    tipos = tipo_caso(args.revision)

    # ---------- 1. Efecto de cada regla sobre el conjunto ----------
    P = list(csv.DictReader(open(args.parches, encoding='utf-8')))
    manifiestos = {}
    for _part in args.particiones:
        _tr = [r for r in P if r['particion'] == _part]
        manifiestos[_part] = _conjunto(_tr, tipos, args, out, _part)
    tr = [r for r in P if r['particion'] == 'train']

    def resumen(nombre: str, sub: list[dict]) -> dict:
        return {'criterio': nombre, 'parches': len(sub),
                'componentes': len({r['Caso'] + '|' + r['comp'] for r in sub}),
                'casos': len({r['Caso'] for r in sub})}

    pasos = [resumen('train completo (A1b)', tr)]
    r2 = [r for r in tr if con_ortopedico(tipos.get(r['Caso'], ''))]
    pasos.append(resumen('R2: caso con material ortopedico', r2))
    con_metal = [r for r in r2 if int(r['n_metal']) > 0]
    solo_banda = [r for r in r2 if int(r['n_metal']) == 0]
    pasos.append(resumen('R3: parche con metal del componente', con_metal))

    rng = np.random.default_rng(args.semilla)
    cupo = int(round(args.ratio_banda * len(con_metal)))
    idx = rng.permutation(len(solo_banda))[:min(cupo, len(solo_banda))]
    banda = [solo_banda[i] for i in sorted(idx)]
    final = con_metal + banda
    pasos.append(resumen(f'R3 + banda al {args.ratio_banda:.0%}', final))

    with open(out / 'a5_conjunto.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(pasos[0].keys()))
        w.writeheader(); w.writerows(pasos)

    # MANIFIESTO: una fila por parche que entra al entrenamiento. Es el conjunto congelado por la
    # decision del 2026-09-21, y lo que lee `src/renderizador/datos.py`. Se versiona: el conjunto
    # deja de ser logica recalculable y pasa a ser un artefacto auditable.
    man = sorted(final, key=lambda r: (r['Caso'], int(r['comp']), int(r['corte'])))
    with open(out / 'a5_manifiesto_train.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['Caso', 'comp', 'corte', 'n_metal', 'n_G'],
                           extrasaction='ignore')
        w.writeheader(); w.writerows(man)
    n_banda = sum(1 for r in man if int(r['n_metal']) == 0)
    print(f'  manifiesto: {len(man)} parches ({len(man) - n_banda} con metal, {n_banda} solo banda; '
          f'ratio {n_banda / max(len(man) - n_banda, 1):.2f})', flush=True)
    for d in pasos:
        print(f"  {d['criterio']:42s} {d['parches']:6d} parches | "
              f"{d['componentes']:4d} comp | {d['casos']:3d} casos", flush=True)

    # ---------- 2. Acuerdo contra los 40 veredictos, sobre la MISMA muestra ----------
    V = list(csv.DictReader(open(args.planilla, encoding='utf-8')))
    metas = {m['Caso']: m for m in leer_particion(args.particion)}
    ubic = rutas(list(metas.values()), args.data)
    por_caso: dict[str, list[int]] = {}
    for r in V:
        por_caso.setdefault(r['Caso'], []).append(int(r['comp']))

    dentro: dict[tuple[str, int], float] = {}
    for i, (caso, comps) in enumerate(sorted(por_caso.items()), 1):
        if caso not in ubic:
            continue
        for ci, f in fraccion_dentro(caso, comps, ubic[caso]).items():
            dentro[(caso, ci)] = f
        print(f'  R1 {i}/{len(por_caso)} {caso}', flush=True)

    filas, tp = [], {'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}
    for r in V:
        ver = r['veredicto'].strip().lower()
        fd = dentro.get((r['Caso'], int(r['comp'])))
        r1 = fd is not None and fd >= args.dentro_min
        r2ok = con_ortopedico(tipos.get(r['Caso'], ''))
        incluye = bool(r1 and r2ok)
        fila = {**{k: r[k] for k in ('Caso', 'comp', 'vol_mm3', 'veredicto')},
                'frac_dentro': None if fd is None else round(fd, 4),
                'R1_dentro': int(r1), 'R2_ortopedico': int(r2ok),
                'criterio_incluye': int(incluye)}
        if ver in INCLUIR:
            tp['TP' if incluye else 'FN'] += 1
        elif ver in EXCLUIR:
            tp['FP' if incluye else 'TN'] += 1
        else:
            fila['nota'] = 'excluido del acuerdo (dudoso)'
        filas.append(fila)

    with open(out / 'a5_acuerdo.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), extrasaction='ignore')
        w.writeheader(); w.writerows(filas)

    n = sum(tp.values())
    acc = (tp['TP'] + tp['TN']) / n if n else 0.0
    prec = tp['TP'] / (tp['TP'] + tp['FP']) if (tp['TP'] + tp['FP']) else float('nan')
    rec = tp['TP'] / (tp['TP'] + tp['FN']) if (tp['TP'] + tp['FN']) else float('nan')
    print(f"\n  ACUERDO binario incluir/excluir sobre {n} componentes "
          f"({len(V) - n} 'dudoso' excluidos):")
    print(f"    TP {tp['TP']}  FP {tp['FP']}  TN {tp['TN']}  FN {tp['FN']}")
    print(f"    exactitud {acc:.0%} | precision {prec:.0%} | recall {rec:.0%}")
    print(f"  Comparar con el criterio anterior (#104): 16 de 40 = 40% de acuerdo exacto de TIPO.")
    print(f"  Escrito en {out}", flush=True)


if __name__ == '__main__':
    main()
