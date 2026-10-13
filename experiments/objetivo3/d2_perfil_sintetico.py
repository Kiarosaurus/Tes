"""D2 (#176) - perfil radial del artefacto SINTETICO con la misma metrica que D1, para compararlo con el real.

Para cada receptor de validacion (`0101`, `0102`) y semilla, sobre la salida de `a15` con la pose corregida
(`outputs/obj3_pose/delta/<punto>/`): en los cortes axiales con `M` (hasta `--max-cortes`, repartidos), anillos de
2 mm por distancia en el plano a `M`, pixeles de cuerpo fuera de `M`. Exceso = amplitud de Peters de la sintetica menos
la del original en los mismos pixeles. Aqui la referencia es exacta (mismo corte sin tornillo); en D1 es otro corte.
Agregacion: cortes -> semilla (mediana) -> paciente (mediana de semillas) -> mediana de los dos pacientes.

Salida: `outputs/d2/d2_perfil.csv` y `d2_resumen.md` (con la columna real de `outputs/d1/d1_exceso_por_anillo.csv`).

USO
---
    python experiments/objetivo3/d2_perfil_sintetico.py
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi

from d1_alcance_rayas import BORDES_MM, cuerpo_2d, perfil

_AQUI = Path(__file__).resolve().parent
CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']


def lee(ruta: Path) -> tuple[np.ndarray, tuple[float, float, float]]:
    img = nib.load(str(ruta))
    return np.asarray(img.dataobj, dtype=np.float32), tuple(float(z) for z in img.header.get_zooms()[:3])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--base', type=Path, default=_AQUI / 'outputs' / 'obj3_pose' / 'delta')
    ap.add_argument('--puntos', nargs='+', default=['run04_mejor', 'run04_60k'])
    ap.add_argument('--semillas', type=int, nargs='+', default=[0, 1, 2, 3, 4])
    ap.add_argument('--max-cortes', type=int, default=8)
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'd2')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    res = {}
    for pt in args.puntos:
        por_pac = []
        for caso in CASOS:
            d = args.base / pt
            orig, (sx, sy, _) = lee(d / ('a15_%s_original.nii.gz' % caso))
            M = lee(d / ('a15_%s_M.nii.gz' % caso))[0] > 0.5
            ks = np.nonzero(M.reshape(-1, M.shape[2]).sum(0) >= 20)[0]
            ks = ks[np.unique(np.linspace(0, len(ks) - 1, min(args.max_cortes, len(ks))).round().astype(int))]
            geo = {k: (ndi.distance_transform_edt(~M[:, :, k], sampling=(sx, sy)),
                       cuerpo_2d(orig[:, :, k]) & ~M[:, :, k]) for k in ks}
            por_sem = []
            for s in args.semillas:
                sint = lee(d / ('a15_%s_%s_s%d_sintetica.nii.gz' % (caso, pt, s)))[0]
                por_sem.append(np.nanmedian(np.stack([perfil(sint[:, :, k], orig[:, :, k], *geo[k]) for k in ks]), 0))
                del sint
            por_pac.append(np.nanmedian(np.stack(por_sem), 0))
            print('%s %s: %d cortes, %d semillas' % (pt, caso, len(ks), len(por_sem)), flush=True)
        res[pt] = np.stack(por_pac)
    real = {}
    ruta_real = _AQUI / 'outputs' / 'd1' / 'd1_exceso_por_anillo.csv'
    if ruta_real.exists():
        with open(ruta_real, encoding='utf-8') as fh:
            real = {f['anillo_mm']: f for f in csv.DictReader(fh)}
    anillos = ['%g-%g' % (a, b) for a, b in zip(BORDES_MM[:-1], BORDES_MM[1:])]
    cab = ['anillo_mm'] + ['%s_%s' % (pt, c.split('_')[2]) for pt in args.puntos for c in CASOS] + \
          ['%s_med' % pt for pt in args.puntos] + ['real_d1_med', 'real_d1_ic90_lo', 'real_d1_ic90_hi']
    filas = []
    for j, a in enumerate(anillos):
        f = [a] + ['%.0f' % v for pt in args.puntos for v in res[pt][:, j]]
        f += ['%.0f' % np.nanmedian(res[pt][:, j]) for pt in args.puntos]
        r = real.get(a, {})
        f += [r.get('exceso_med', ''), r.get('ic90_lo', ''), r.get('ic90_hi', '')]
        filas.append(f)
    with open(args.out_dir / 'd2_perfil.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(cab)
        w.writerows(filas)
    L = ['# D2 — perfil radial del artefacto sintetico frente al real (#176)', '',
         'Generado por `d2_perfil_sintetico.py`. Sintetico: validacion (`0101`, `0102`), 5 semillas, pose corregida, '
         'referencia exacta (original). Real: D1 (40 pacientes de entrenamiento y validacion, referencia aproximada). '
         'Exceso de amplitud de Peters por anillo, HU.', '',
         '| anillo (mm) | ' + ' | '.join('%s (mediana 0101/0102)' % pt for pt in args.puntos) + ' | real D1 [IC90] |',
         '|---|' + '---|' * len(args.puntos) + '---|']
    for j, a in enumerate(anillos[:15]):
        r = real.get(a, {})
        L.append('| %s | %s | %s [%s, %s] |' % (a, ' | '.join('%.0f' % np.nanmedian(res[pt][:, j]) for pt in args.puntos),
                                                 r.get('exceso_med', ''), r.get('ic90_lo', ''), r.get('ic90_hi', '')))
    (args.out_dir / 'd2_resumen.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
