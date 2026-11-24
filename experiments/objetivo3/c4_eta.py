"""C4 sobre las variantes del barrido eta (criterio (b)/angular), validacion 0101/0102, exploratorio.

Reglas: docs/01-decisiones.md 2026-11-20 (2), (3), (5), (6). Metrica C4 v2 (anillos por distancia a M).
Brazos: run04_mejor (delta/), variantes eta (b_min/), Peters Ti (residuo) y control sin metal.
Uso: METALSYNTH_REPO=<repo> python -I c4_eta.py --b-min <carpeta con run04_mejor_p*_e*>
"""
from __future__ import annotations
import argparse, csv, sys, importlib.util
from collections import defaultdict
from pathlib import Path
import numpy as np, nibabel as nib

sys.argv_orig = sys.argv
sys.argv = [sys.argv[0], 'distancia']
_sp = importlib.util.spec_from_file_location('c4', Path(__file__).resolve().parent / 'c4_anisotropia.py')
c4 = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(c4)
sys.argv = sys.argv_orig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--b-min', type=Path, required=True)
    ap.add_argument('--variantes', nargs='+', default=['run04_mejor_p100_e0.3', 'run04_mejor_p50_e0.3'])
    ap.add_argument('--out', type=Path, default=Path(__file__).resolve().parent / 'c4' / 'c4_eta_resumen.md')
    a = ap.parse_args()
    OUT3 = c4.OUT3
    brazos = {'run04_mejor': OUT3 / 'delta/run04_mejor'}
    brazos.update({v: a.b_min / v for v in a.variantes})
    rows = []
    for caso in c4.CASOS:
        z = np.load(OUT3 / f'peters_val/a19_{caso}.npz')
        ks = [int(k) for k in z['ks']]
        cand = [(i, k) for i, k in enumerate(ks) if z['M'][i].any()]
        zoom = nib.load(str(OUT3 / f'delta/run04_mejor/a15_{caso}_original.nii.gz')).header.get_zooms()
        sy, sx = float(zoom[1]), float(zoom[0])
        pac = caso.split('_')[2]
        pre = []
        for i, k in cand:
            M, orig = z['M'][i], z['original'][i]
            cy, cx = c4.centro(M)
            pre.append((i, k, M, orig, cy, cx, (orig > -300) & ~M & (orig < c4.METAL)))
        for i, k, M, orig, cy, cx, valid in pre:
            c4.fila(rows, 'control_anatomia', 'crudo', pac, 0, k, orig, valid, cy, cx, sy, sx, M)
            c4.fila(rows, 'peters_Ti', 'residuo', pac, 0, k, z['Ti_A'][i] - z['limpia_A'][i], valid, cy, cx, sy, sx, M)
        for br, d in brazos.items():
            for s in range(5):
                f = d / f'a15_{caso}_{br}_s{s}_sintetica.nii.gz'
                if not f.exists():
                    print('FALTA', f, flush=True)
                    continue
                v = nib.load(str(f)).get_fdata(dtype=np.float32)
                for i, k, M, orig, cy, cx, valid in pre:
                    c4.fila(rows, br, 'residuo', pac, s, k, v[:, :, k] - orig, valid, cy, cx, sy, sx, M)
                    c4.fila(rows, br, 'crudo', pac, s, k, v[:, :, k], valid, cy, cx, sy, sx, M)
                print(br, pac, 's%d' % s, flush=True)
    a.out.parent.mkdir(exist_ok=True)
    with open(a.out.with_suffix('.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    t = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for r in rows:
        if r['ventana'] == 'A':
            t[(r['K'], r['modo'], r['brazo'])][r['paciente']][r['semilla']].append(r['eta2_exc'])
    L = ['# C4 sobre variantes del barrido eta (validación 0101/0102; exploratorio, N = 2 pacientes)', '',
         'η²_exc por paciente (mediana corte → semilla); entre paréntesis, los dos pacientes. Ventana [-500, 1300] HU.', '']
    for K in (12, 24, 48):
        L += ['## K = %d' % K, '', '| brazo | modo | η²_exc mediana | por paciente |', '|---|---|---|---|']
        for modo in ('residuo', 'crudo'):
            for br in ['run04_mejor'] + a.variantes + ['peters_Ti', 'control_anatomia']:
                d = t.get((K, modo, br))
                if not d:
                    continue
                pp = {p: float(np.median([np.median(v) for v in ss.values()])) for p, ss in d.items()}
                L.append('| %s | %s | %.3f | %s |' % (br, modo, np.median(list(pp.values())),
                         ', '.join('%s %.3f' % (p, v) for p, v in sorted(pp.items()))))
        L.append('')
    L.append('Limites: 2 pacientes de validación; 1 checkpoint; Peters = referencia física, no «lo real».')
    a.out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('listo', a.out)


if __name__ == '__main__':
    main()
