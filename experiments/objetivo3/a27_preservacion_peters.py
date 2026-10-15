"""A27 - preservacion del protocolo fisico fuera de `G` (DEC 2026-10-15 pto 8). POSTERIOR y descriptivo.

Caracteriza la REFERENCIA, no al sintetizador (que vale 0 por construccion fuera de `G`): cuanto cambia la anatomia
del paciente la simulacion SIN metal de Peters (`limpia_A`, `limpia_B`) frente a la TC original, en los cortes
simulados (`ks`), fuera de `G` y dentro del cuerpo.

- RMSE en HU.
- SSIM (`skimage.metrics.structural_similarity`, ventana gaussiana por omision) sobre las dos imagenes recortadas a
  [-1000, 2000] HU, `data_range` = 3000, promediando el mapa SSIM en la region. Rango fijado en DEC 2026-10-15 pto 8.
- Cuerpo (eleccion propia, declarada): por corte, mayor componente conexa de la TC original > -500 HU, con agujeros
  rellenos.

USO:  python experiments/objetivo3/a27_preservacion_peters.py [--npz-dir outputs/obj3_pose/peters_final]
Salida: outputs/obj3_pose/a27/a27_preservacion.csv y .md
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from scipy import ndimage as ndi
from skimage.metrics import structural_similarity

_AQUI = Path(__file__).resolve().parent


def cuerpo(corte: np.ndarray) -> np.ndarray:
    m = corte > -500
    lab, n = ndi.label(m)
    if n == 0:
        return m
    mayor = 1 + int(np.argmax(ndi.sum(m, lab, range(1, n + 1))))
    return ndi.binary_fill_holes(lab == mayor)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--npz-dir', type=Path, default=_AQUI / 'outputs' / 'obj3_pose' / 'peters_final')
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'obj3_pose' / 'a27')
    args = ap.parse_args()
    filas = []
    for ruta in sorted(args.npz_dir.glob('a19_*.npz')):
        z = np.load(ruta)
        caso = ruta.stem[len('a19_'):]
        orig, G = z['original'], z['G']
        for rep in ('A', 'B'):
            sim = z['limpia_%s' % rep]
            err2, n, ssim_sum = 0.0, 0, 0.0
            for k in range(orig.shape[0]):
                reg = cuerpo(orig[k]) & ~G[k]
                if not reg.any():
                    continue
                d = sim[k][reg] - orig[k][reg]
                err2 += float((d.astype(np.float64) ** 2).sum())
                n += int(reg.sum())
                a = np.clip(orig[k], -1000, 2000)
                b = np.clip(sim[k], -1000, 2000)
                _, mapa = structural_similarity(a, b, data_range=3000.0, full=True)
                ssim_sum += float(mapa[reg].sum())
            filas.append({'caso': caso, 'replica': rep, 'cortes': int(orig.shape[0]), 'n_vox': n,
                          'rmse_HU': (err2 / n) ** 0.5 if n else float('nan'),
                          'ssim': ssim_sum / n if n else float('nan')})
            print('%s limpia_%s: RMSE %.1f HU | SSIM %.4f | %d voxeles'
                  % (caso, rep, filas[-1]['rmse_HU'], filas[-1]['ssim'], n), flush=True)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with open(args.out_dir / 'a27_preservacion.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    r = np.array([f['rmse_HU'] for f in filas])
    s = np.array([f['ssim'] for f in filas])
    L = ['# A27 — preservacion del protocolo fisico fuera de `G` (DEC 2026-10-15 pto 8; posterior, descriptivo)', '',
         'Simulacion sin metal de Peters frente a la TC original, cortes simulados, fuera de `G`, dentro del cuerpo.',
         '%d pacientes x 2 replicas.' % (len(filas) // 2), '',
         '| | mediana | rango |', '|---|---|---|',
         '| RMSE (HU) | %.1f | %.1f a %.1f |' % (np.median(r), r.min(), r.max()),
         '| SSIM ([-1000, 2000] HU) | %.4f | %.4f a %.4f |' % (np.median(s), s.min(), s.max()), '',
         'El sintetizador vale RMSE 0 y SSIM 1 en esta region por construccion: no es un resultado.']
    (args.out_dir / 'a27_preservacion.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
