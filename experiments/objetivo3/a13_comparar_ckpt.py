"""A13 - compara DOS checkpoints sobre los 5 pacientes de validacion, pareado (#145, B1, B2).

LA PREGUNTA
-----------
#145 midio, en **un** paciente, que el checkpoint del minimo de la perdida de validacion
(`mejor.pt`, paso 37 500) es **peor** que el sobreajustado (`run01/ckpt.pt`, paso 140 000) en las
ocho magnitudes de apariencia medidas: genera el 54.8 % del metal real frente al 94.9 %, duplica la
costura y pierde en MAE dentro del metal y en la banda.

Con un paciente no se puede separar dos explicaciones:

- **(A) la perdida de validacion no ordena los modelos por fidelidad en HU** —desacople conocido
  entre la perdida de difusion y la calidad de las muestras—, o
- **(B) `run01` memorizo la apariencia de los implantes de entrenamiento** y este paciente tiene un
  implante parecido, de modo que su ventaja no generalizaria.

Este script repite la comparacion en los **5 pacientes de validacion con metal**. Si el orden se
mantiene en los cinco, (A) gana fuerza; si se mezcla, (B) explica lo de #145 y la perdida sobrevive
como criterio.

DE ESTO DEPENDEN TRES DECISIONES, no una
----------------------------------------
- **B1**, si la saturacion con 47 pacientes entra como limitacion declarada: su evidencia **es** la
  curva de la perdida, asi que si la perdida no mide lo que importa, la saturacion no esta demostrada.
- **B2**, los 30 000 pasos, elegidos por el minimo de esa misma curva (`01-decisiones.md` 2026-10-05 (2)).
- **El mecanismo de `mejor.pt`**, que `guarda()` escribe en el minimo de la perdida.

DISENO, y su limite estadistico declarado de antemano
-----------------------------------------------------
**Pareado al maximo:** los mismos pacientes, las mismas series, **los mismos cortes** y la **misma
semilla** en los dos brazos. Lo unico que cambia es el `ckpt`.

**No se generan series completas.** Serian ~9 h de CPU; se muestrean `--cortes` cortes repartidos
uniformemente por la serie de mayor contenido metalico de cada paciente. La unidad de analisis es el
**paciente**, como en D4.

**Con n = 5 el resultado no puede ser mas fuerte que esto, y conviene saberlo antes de verlo:** una
prueba de signos de una cola con 5 de 5 da `p = 0.031`; 4 de 5 da `p = 0.188`. **Solo el resultado
unanime alcanza significacion**, y aun asi sobre cinco pacientes. Este experimento sirve para
**descartar** que lo de #145 fuera un caso aislado, no para probar una ley.

NO TOCA TEST
------------
Solo particion de validacion. El script aborta si se le piden otras.

USO
---
    python a13_comparar_ckpt.py
    python a13_comparar_ckpt.py --cortes 8 --pasos 50
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
from region import componer, verificar_composicion  # noqa: E402
from ventanas import decodifica_bloque  # noqa: E402

PATRON = re.compile(r'^(?P<serie>.+)_k(?P<k>\d{4})\.npz$')
METAL_HU = 2500.0


def a_hu(bloque: torch.Tensor) -> np.ndarray:
    u = (bloque.detach().cpu().numpy()[0] + 1.0) / 2.0
    return decodifica_bloque(u)


def carga_modelo(ruta: Path):
    ck = torch.load(ruta, map_location='cpu', weights_only=False)
    base = int(ck.get('meta', {}).get('base', 64))
    m = UNetDifusion(base=base)
    m.load_state_dict(ck['modelo'])
    m.eval()
    return m, ck.get('paso')


def anillos2d(g: np.ndarray):
    """Cascaras de un voxel a cada lado del borde de `g`, en 2D. Misma definicion que `a10`."""
    from scipy import ndimage as ndi
    e = ndi.binary_erosion(g, ndi.generate_binary_structure(2, 1), border_value=1)
    d = ndi.binary_dilation(g, ndi.generate_binary_structure(2, 1))
    return g & ~e, d & ~g


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cache', type=Path, default=aqui / 'outputs' / 'a1b_cache')
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--ckpt-a', type=Path,
                    default=aqui / 'outputs' / 'a7' / 'run01' / 'ckpt.pt')
    ap.add_argument('--ckpt-b', type=Path,
                    default=aqui / 'outputs' / 'a7' / 'run02' / 'mejor.pt')
    ap.add_argument('--etiqueta-a', default='run01_140k')
    ap.add_argument('--etiqueta-b', default='mejor_37k')
    ap.add_argument('--cortes', type=int, default=12)
    ap.add_argument('--pasos', type=int, default=50)
    ap.add_argument('--semilla', type=int, default=0)
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a13')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    with open(args.particion, newline='', encoding='utf-8') as fh:
        val = {f['Caso'] for f in csv.DictReader(fh) if f['particion'] == 'val'}

    # serie con mas metal por paciente, y cortes repartidos uniformemente
    metal_por_serie: dict[str, int] = {}
    cortes_por_serie: dict[str, list[int]] = {}
    for f in sorted(args.cache.glob('*.npz')):
        m = PATRON.match(f.name)
        if m is None or caso_de(m.group('serie')) not in val:
            continue
        with np.load(f) as z:
            n = int(z['metal'].sum())
        if n == 0:
            continue
        s = m.group('serie')
        metal_por_serie[s] = metal_por_serie.get(s, 0) + n
        cortes_por_serie.setdefault(s, []).append(int(m.group('k')))

    elegidas: dict[str, str] = {}
    for s, n in metal_por_serie.items():
        c = caso_de(s)
        if c not in elegidas or n > metal_por_serie[elegidas[c]]:
            elegidas[c] = s
    if not elegidas:
        raise SystemExit('ningun paciente de validacion con metal en el cache')

    print('pacientes de validacion con metal: %d' % len(elegidas))
    plan = {}
    for c, s in sorted(elegidas.items()):
        ks = sorted(cortes_por_serie[s])
        idx = np.linspace(0, len(ks) - 1, min(args.cortes, len(ks))).round().astype(int)
        plan[c] = (s, [ks[i] for i in sorted(set(idx))])
        print('  %-34s serie %-40s %3d cortes de %d | metal %d vox'
              % (c, s, len(plan[c][1]), len(ks), metal_por_serie[s]))

    total = sum(len(v[1]) for v in plan.values()) * 2
    print('\ngeneraciones: %d (%d cortes x 2 checkpoints) | estimado ~%.0f min a 52 s cada una'
          % (total, total // 2, total * 52 / 60))

    ma, pa = carga_modelo(args.ckpt_a)
    mb, pb = carga_modelo(args.ckpt_b)
    print('A = %s (paso %s) | B = %s (paso %s)' % (args.etiqueta_a, pa, args.etiqueta_b, pb))
    dif = Difusion()
    ds = ParchesMetal(args.cache, args.particion, particiones=('val',))
    pos = {k: i for i, k in enumerate(ds.indice)}

    filas = []
    t0 = time.time()
    hecho = 0
    for caso, (serie, ks) in sorted(plan.items()):
        acum = {e: {'n2500': 0, 'ae_M': [], 'ae_B': [], 'exc': []} for e in ('A', 'B')}
        real = {'n2500': 0, 'n_M': 0, 'n_B': 0}
        for k in ks:
            i = pos.get((serie, k))
            if i is None:
                continue
            it = ds[i]
            g = it['g'].numpy()[0].astype(bool)
            hu_real = a_hu(it['x0'][None])
            M = (hu_real > METAL_HU) & g      # metal REAL dentro de G
            B = g & ~M
            real['n2500'] += int(M.sum())
            real['n_M'] += int(M.sum())
            real['n_B'] += int(B.sum())
            ins, out = anillos2d(g)
            s_o = abs(float(np.median(hu_real[ins])) - float(np.median(hu_real[out]))) \
                if ins.sum() >= 20 and out.sum() >= 20 else float('nan')
            for et, mod in (('A', ma), ('B', mb)):
                with torch.no_grad():
                    gen = muestrea_ddim(mod, it['cond'][None], it['g'][None], dif,
                                        pasos=args.pasos, semilla=args.semilla)
                hu_sal = componer(hu_real, a_hu(gen), g)
                verificar_composicion(hu_real, hu_sal, g)
                acum[et]['n2500'] += int((hu_sal[g] > METAL_HU).sum())
                if M.any():
                    acum[et]['ae_M'].append(np.abs(hu_sal[M] - hu_real[M]))
                if B.any():
                    acum[et]['ae_B'].append(np.abs(hu_sal[B] - hu_real[B]))
                if np.isfinite(s_o):
                    s_c = abs(float(np.median(hu_sal[ins])) - float(np.median(hu_sal[out])))
                    acum[et]['exc'].append(s_c - s_o)
                hecho += 1
            if hecho % 8 == 0:
                tr = (time.time() - t0) / hecho * (total - hecho) / 60
                print('  [%d/%d] %s k%04d | faltan ~%.0f min' % (hecho, total, caso, k, tr),
                      flush=True)
        fila = {'caso': caso, 'serie': serie, 'cortes': len(ks),
                'n_metal_real': real['n2500'], 'n_M': real['n_M'], 'n_banda': real['n_B']}
        for et, nom in (('A', args.etiqueta_a), ('B', args.etiqueta_b)):
            a = acum[et]
            fila['n2500_' + nom] = a['n2500']
            fila['frac_metal_' + nom] = round(a['n2500'] / real['n2500'], 4) if real['n2500'] else ''
            fila['mae_M_' + nom] = round(float(np.concatenate(a['ae_M']).mean()), 1) if a['ae_M'] else ''
            fila['mae_banda_' + nom] = round(float(np.concatenate(a['ae_B']).mean()), 1) if a['ae_B'] else ''
            fila['exceso_costura_' + nom] = round(float(np.median(a['exc'])), 1) if a['exc'] else ''
        filas.append(fila)
        print('  -> %s listo' % caso, flush=True)

    ruta = args.out_dir / 'a13_comparacion_ckpt_val.csv'
    with open(ruta, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print('\npor paciente: %s' % ruta)

    # --- recuento de ganadores, que es el unico estadistico que n = 5 soporta
    A, B = args.etiqueta_a, args.etiqueta_b
    print('\n%-22s %14s %14s   quien gana' % ('magnitud', A, B))
    criterios = [('frac_metal_', 'mas cerca de 1', lambda x, y: abs(x - 1) < abs(y - 1)),
                 ('mae_M_', 'menor', lambda x, y: x < y),
                 ('mae_banda_', 'menor', lambda x, y: x < y),
                 ('exceso_costura_', 'menor', lambda x, y: x < y)]
    for pre, sent, mejor in criterios:
        gana_a = 0
        n = 0
        for f in filas:
            x, y = f[pre + A], f[pre + B]
            if isinstance(x, float) and isinstance(y, float):
                n += 1
                gana_a += int(mejor(x, y))
        if n:
            print('%-22s %14s %14s   %s gana en %d de %d  (%s)'
                  % (pre.rstrip('_'), '', '', A if gana_a * 2 > n else B,
                     max(gana_a, n - gana_a), n, sent))
    print('\nPrueba de signos de una cola, como referencia: 5 de 5 -> p = 0.031 | 4 de 5 -> p = 0.188.')
    print('Solo el resultado UNANIME alcanza significacion con n = 5, y aun asi sobre cinco pacientes.')
    print('Este experimento descarta que #145 fuera un caso aislado; no prueba una ley.')


if __name__ == '__main__':
    main()
