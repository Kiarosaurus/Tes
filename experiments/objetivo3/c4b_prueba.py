"""C4b: anisotropia angular en los 13 pacientes de PRUEBA (reglas: docs/01-decisiones.md 2026-11-20 (3)); exploratorio.

Reutiliza la metrica v2 (anillos por distancia a M) de c4_anisotropia.py. Brazos: run04_mejor, run04_60k, Peters Ti
(residuo Ti_A - limpia_A) y control sin metal. Bootstrap por paciente (B=2000, semilla fija). Figura desenrollada.
Uso: python -I c4b_prueba.py   (escribe c4/c4b_resumen.md, c4/c4b_filas.csv, c4/fig_desenrollada.png)
"""
from __future__ import annotations
import csv, sys, importlib.util
from collections import defaultdict
from pathlib import Path
import numpy as np, nibabel as nib
from scipy import ndimage as ndi

sys.argv = [sys.argv[0], 'distancia']
_sp = importlib.util.spec_from_file_location('c4', Path(__file__).resolve().parent / 'c4_anisotropia.py')
c4 = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(c4)

REPO, OUT3, AQUI = c4.REPO, c4.OUT3, c4.AQUI
ARMS = ['run04_mejor', 'run04_60k']
B_BOOT = 2000


def casos_test():
    return [l.strip() for l in open(REPO / 'experiments/objetivo3/casos_ea2_test.txt') if l.strip()]


def filas_prueba():
    rows = []
    for caso in casos_test():
        z = np.load(OUT3 / f'peters_final/a19_{caso}.npz')
        ks = [int(k) for k in z['ks']]
        cand = [(i, k) for i, k in enumerate(ks) if z['M'][i].any()]
        zoom = nib.load(str(OUT3 / f'final/run04_mejor/a15_{caso}_original.nii.gz')).header.get_zooms()
        sy, sx = float(zoom[1]), float(zoom[0])
        pac = caso.split('_')[2]
        pre = []
        for i, k in cand:
            M, orig = z['M'][i], z['original'][i]
            cy, cx = c4.centro(M)
            pre.append((i, k, M, orig, cy, cx, (orig > -300) & ~M & (orig < c4.METAL)))
        for i, k, M, orig, cy, cx, valid in pre:
            c4.fila(rows, 'control_anatomia_test', 'crudo', pac, 0, k, orig, valid, cy, cx, sy, sx, M)
            c4.fila(rows, 'peters_Ti_test', 'crudo', pac, 0, k, z['Ti_A'][i], valid, cy, cx, sy, sx, M)
            c4.fila(rows, 'peters_Ti_test', 'residuo', pac, 0, k, z['Ti_A'][i] - z['limpia_A'][i], valid, cy, cx, sy, sx, M)
        for br in ARMS:
            for s in range(5):
                f = OUT3 / f'final/{br}/a15_{caso}_{br}_s{s}_sintetica.nii.gz'
                if not f.exists():
                    print('FALTA', f.name, flush=True)
                    continue
                v = nib.load(str(f)).get_fdata(dtype=np.float32)
                for i, k, M, orig, cy, cx, valid in pre:
                    c4.fila(rows, br + '_test', 'crudo', pac, s, k, v[:, :, k], valid, cy, cx, sy, sx, M)
                    c4.fila(rows, br + '_test', 'residuo', pac, s, k, v[:, :, k] - orig, valid, cy, cx, sy, sx, M)
        print('paciente', pac, 'ok', flush=True)
    return rows


def por_paciente(rows, K=24, ven='A'):
    """{(brazo, modo): {paciente: eta2_exc}} (mediana corte -> semilla -> paciente)."""
    t = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for r in rows:
        if r['K'] == K and r['ventana'] == ven:
            t[(r['brazo'], r['modo'])][r['paciente']][r['semilla']].append(r['eta2_exc'])
    return {k: {p: float(np.median([np.median(v) for v in ss.values()])) for p, ss in d.items()} for k, d in t.items()}


def boot(vals, rng):
    v = np.asarray(vals)
    m = [np.median(rng.choice(v, v.size)) for _ in range(B_BOOT)]
    return float(np.median(v)), float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def figura(rows_dummy=None):
    """Desenrollada (distancia a M x angulo) y recorte: real (metal_0039 c1, corte central), Peters y run04 (1er paciente de prueba)."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    lo, hi = c4.VENT['A']

    def desenrolla(img, M2, valid, cy, cx, sy, sx, nb=72):
        d = ndi.distance_transform_edt(~M2, sampling=(sy, sx))
        yy, xx = np.indices(img.shape)
        th = np.arctan2((yy - cy) * sy, (xx - cx) * sx)
        b = np.minimum(((th + np.pi) / (2 * np.pi) * nb).astype(int), nb - 1)
        v = np.clip(img, lo, hi).astype(float)
        out = np.full((8, nb), np.nan)
        for j in range(2, 10):
            m = valid & (d >= j) & (d < j + 1)
            if m.sum() == 0:
                continue
            vv = v - np.median(v[m])
            for q in range(nb):
                mq = m & (b == q)
                if mq.any():
                    out[j - 2, q] = vv[mq].mean()
        return out

    def recorte(img, cy, cx, L=80):
        p = np.pad(img, L, constant_values=-1000)
        y, x = int(round(cy)) + L, int(round(cx)) + L
        return np.clip(p[y - L:y + L, x - L:x + L], lo, hi)

    paneles = []
    sys.path.insert(0, str(REPO / 'experiments/objetivo1'))
    from e6b_vae_sd15 import eje_axial
    img = nib.load(str(REPO / 'data/dataset7/dataset7_CLINIC_metal_0039_data.nii.gz'))
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zo = np.array(img.header.get_zooms()[:3], float)
    pl = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)
    lab, _ = ndi.label(vol > c4.METAL)
    tam = ndi.sum(vol > c4.METAL, lab, index=np.arange(1, lab.max() + 1))
    c = int(np.argmax(tam)) + 1
    m3 = lab == c
    ks = [k for k in range(vol.shape[0]) if m3[k].any()]
    k = ks[len(ks) // 2]
    cy, cx = c4.centro(m3[k])
    sl = vol[k]
    paneles.append(('Real (metal_0039)', recorte(sl, cy, cx),
                    desenrolla(sl, m3[k], (sl > -300) & ~m3[k] & (sl < c4.METAL), cy, cx, zo[pl[0]], zo[pl[1]])))
    caso = casos_test()[0]
    z = np.load(OUT3 / f'peters_final/a19_{caso}.npz')
    ksx = [int(q) for q in z['ks']]
    cand = [i for i, q in enumerate(ksx) if z['M'][i].any()]
    i = cand[len(cand) // 2]
    kk = ksx[i]
    zoom = nib.load(str(OUT3 / f'final/run04_mejor/a15_{caso}_original.nii.gz')).header.get_zooms()
    sy, sx = float(zoom[1]), float(zoom[0])
    M, orig = z['M'][i], z['original'][i]
    cy, cx = c4.centro(M)
    valid = (orig > -300) & ~M & (orig < c4.METAL)
    paneles.append(('Peters Ti', recorte(z['Ti_A'][i], cy, cx), desenrolla(z['Ti_A'][i], M, valid, cy, cx, sy, sx)))
    for br in ARMS:
        v = nib.load(str(OUT3 / f'final/{br}/a15_{caso}_{br}_s0_sintetica.nii.gz')).get_fdata(dtype=np.float32)[:, :, kk]
        paneles.append((br + ' (s0)', recorte(v, cy, cx), desenrolla(v, M, valid, cy, cx, sy, sx)))
    fig, ax = plt.subplots(2, len(paneles), figsize=(3.1 * len(paneles), 5.6))
    for j, (t, rec, des) in enumerate(paneles):
        ax[0, j].imshow(rec, cmap='gray', vmin=lo, vmax=hi)
        ax[0, j].set_title(t, fontsize=9)
        ax[0, j].axis('off')
        im = ax[1, j].imshow(des, cmap='RdBu_r', vmin=-400, vmax=400, aspect='auto',
                             extent=[-180, 180, 10, 2])
        ax[1, j].set_xlabel('ángulo (°)', fontsize=8)
        if j == 0:
            ax[1, j].set_ylabel('distancia a M (mm)', fontsize=8)
    fig.colorbar(im, ax=ax[1, :], shrink=0.8, label='HU − mediana del anillo')
    fig.savefig(AQUI / 'fig_desenrollada.png', dpi=170, bbox_inches='tight')
    plt.close(fig)
    return caso, kk, k


def main():
    AQUI.mkdir(exist_ok=True)
    rows = filas_prueba()
    with open(AQUI / 'c4b_filas.csv', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    rng = np.random.default_rng(20261120)
    L = ['# C4b — anisotropía angular en los 13 pacientes de PRUEBA (exploratorio; reglas en `01-decisiones.md` 2026-11-20 (3))', '',
         'η²_exc por paciente (mediana corte → semilla → paciente); mediana entre pacientes con IC95 bootstrap por paciente (B=2000).', '']
    for K, ven, titulo in [(24, 'A', 'Principal: K=24, [-500, 1300] HU'), (12, 'A', 'Sensibilidad K=12'),
                           (48, 'A', 'Sensibilidad K=48'), (24, 'B', 'Sensibilidad K=24, [-1000, 3000] HU')]:
        pp = por_paciente(rows, K, ven)
        L += ['## ' + titulo, '', '| brazo | modo | pacientes | η²_exc mediana | IC95 bootstrap |', '|---|---|---|---|---|']
        for key in [('control_anatomia_test', 'crudo'), ('peters_Ti_test', 'crudo'), ('peters_Ti_test', 'residuo'),
                    ('run04_mejor_test', 'crudo'), ('run04_mejor_test', 'residuo'),
                    ('run04_60k_test', 'crudo'), ('run04_60k_test', 'residuo')]:
            if key in pp:
                m, a, b = boot(list(pp[key].values()), rng)
                L.append('| %s | %s | %d | %.3f | [%.3f, %.3f] |' % (key[0], key[1], len(pp[key]), m, a, b))
        L += ['', 'Diferencias pareadas por paciente (mediana y IC95 bootstrap):', '', '| contraste | modo | mediana | IC95 |', '|---|---|---|---|']
        for (a_, b_, mo) in [('run04_mejor_test', 'peters_Ti_test', 'residuo'), ('run04_mejor_test', 'peters_Ti_test', 'crudo'),
                             ('run04_mejor_test', 'control_anatomia_test', 'crudo'), ('peters_Ti_test', 'control_anatomia_test', 'crudo'),
                             ('run04_60k_test', 'peters_Ti_test', 'residuo')]:
            A = pp.get((a_, mo))
            B = pp.get((b_, 'crudo' if b_.startswith('control') else mo))
            if A and B:
                dif = [A[p] - B[p] for p in A if p in B]
                m, lo_, hi_ = boot(dif, rng)
                L.append('| %s − %s | %s | %.3f | [%.3f, %.3f] |' % (a_, b_, mo, m, lo_, hi_))
        L.append('')
    caso, kk, k_real = figura()
    L += ['Figura: `fig_desenrollada.png` (paciente %s corte %d; real metal_0039 comp. mayor, corte %d; regla: corte central de los cortes con M; 1er paciente de la lista de prueba, semilla 0).' % (caso, kk, k_real), '',
          'Limites: referencia real = 2 tornillos de metal_0039 (otra anatomía); run05a/b sin volúmenes de prueba en local; η² no distingue rayas de bordes anatómicos radiales; el ruido del difusor baja η² (controles C0).']
    (AQUI / 'c4b_resumen.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('listo')


if __name__ == '__main__':
    main()
