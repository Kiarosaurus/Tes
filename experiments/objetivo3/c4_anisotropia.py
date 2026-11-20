"""C4: anisotropia angular del artefacto (protocolo: c4_protocolo.md). Solo lectura sobre el repo; exploratorio."""
from __future__ import annotations
import csv, sys
from collections import defaultdict
from pathlib import Path
import numpy as np, nibabel as nib
from scipy import ndimage as ndi

REPO = Path(r'D:/UTEC/CICLOX/Salvar-El-Ciclo/PFCII/metalsynth-pelvis')
OUT3 = REPO / 'experiments/objetivo3/outputs/obj3_pose'
AQUI = Path(__file__).resolve().parent / 'c4'
CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']
BRAZOS = ['run04_mejor', 'run05a_mejor', 'run05b_mejor']
VENT = {'A': (-500.0, 1300.0), 'B': (-1000.0, 3000.0)}
KS = (12, 24, 48)
R_LO, R_HI = 2.0, 10.0
METAL = 2500.0
MIN_N = 5
MODO = 'distancia' if len(sys.argv) > 1 and sys.argv[1] == 'distancia' else 'centroide'


def eta2_exc(img, valid, cy, cx, sy, sx, K, ven, rdist=None):
    """(eta2_exc, std, N) en el anillo 2-10 mm; None si faltan pixeles."""
    lo, hi = VENT[ven]
    yy, xx = np.indices(img.shape)
    dy, dx = (yy - cy) * sy, (xx - cx) * sx
    r = np.hypot(dy, dx) if rdist is None else rdist   # v2: distancia a M; el angulo sigue siendo respecto al centroide
    m = valid & (r >= R_LO) & (r < R_HI)
    if m.sum() < MIN_N * max(KS):
        return None
    v = np.clip(img, lo, hi).astype(np.float64)
    d = np.zeros_like(v)
    ring = np.floor(r).astype(int)
    for j in range(int(R_LO), int(R_HI)):
        mj = m & (ring == j)
        if mj.sum() == 0:
            continue
        d[mj] = v[mj] - np.median(v[mj])
    d, th = d[m], np.arctan2(dy[m], dx[m])
    b = np.minimum(((th + np.pi) / (2 * np.pi) * K).astype(int), K - 1)
    n = d.size
    mu = d.mean()
    sst = float(((d - mu) ** 2).sum())
    if sst <= 0:
        return None
    cnt = np.bincount(b, minlength=K).astype(float)
    sm = np.bincount(b, weights=d, minlength=K)
    ssb = float(sum(c * ((s / c) - mu) ** 2 for c, s in zip(cnt, sm) if c > 0))
    return ssb / sst - (K - 1) / (n - 1), float(d.std()), n


def fila(rows, arm, modo, pac, sem, k, img, valid, cy, cx, sy, sx, M2=None):
    rd = None
    if MODO == 'distancia':
        rd = ndi.distance_transform_edt(~M2, sampling=(sy, sx))
    for ven in VENT:
        for K in KS:
            res = eta2_exc(img, valid, cy, cx, sy, sx, K, ven, rd)
            if res:
                rows.append(dict(brazo=arm, modo=modo, paciente=pac, semilla=sem, corte=k, K=K, ventana=ven,
                                 eta2_exc=res[0], std=res[1], N=res[2]))


def centro(m2):
    y, x = ndi.center_of_mass(m2)
    return y, x


def sinteticos(rows):
    for caso in CASOS:
        z = np.load(OUT3 / f'peters_val/a19_{caso}.npz')
        ks = [int(k) for k in z['ks']]
        cand = [(i, k) for i, k in enumerate(ks) if z['M'][i].any()]
        zoom = nib.load(str(OUT3 / f'delta/run04_mejor/a15_{caso}_original.nii.gz')).header.get_zooms()
        sy, sx = float(zoom[1]), float(zoom[0])
        pac = caso.split('_')[2]
        pre = []
        for i, k in cand:
            M = z['M'][i]
            orig = z['original'][i]
            cy, cx = centro(M)
            valid = (orig > -300) & ~M & (orig < METAL)
            pre.append((i, k, M, orig, cy, cx, valid))
        for i, k, M, orig, cy, cx, valid in pre:
            fila(rows, 'control_anatomia', 'crudo', pac, 0, k, orig, valid, cy, cx, sy, sx, M)
            fila(rows, 'peters_Ti', 'crudo', pac, 0, k, z['Ti_A'][i], valid, cy, cx, sy, sx, M)
            fila(rows, 'peters_Ti', 'residuo', pac, 0, k, z['Ti_A'][i] - z['limpia_A'][i], valid, cy, cx, sy, sx, M)
        for br in BRAZOS:
            for s in range(5):
                f = OUT3 / f'delta/{br}/a15_{caso}_{br}_s{s}_sintetica.nii.gz'
                if not f.exists():
                    continue
                v = nib.load(str(f)).get_fdata(dtype=np.float32)
                for i, k, M, orig, cy, cx, valid in pre:
                    sl = v[:, :, k]
                    fila(rows, br, 'crudo', pac, s, k, sl, valid, cy, cx, sy, sx, M)
                    fila(rows, br, 'residuo', pac, s, k, sl - orig, valid, cy, cx, sy, sx, M)
                print(br, pac, 's%d' % s, flush=True)


def reales(rows):
    sys.path.insert(0, str(REPO / 'experiments/objetivo1'))
    from e6b_vae_sd15 import eje_axial
    img = nib.load(str(REPO / 'data/dataset7/dataset7_CLINIC_metal_0039_data.nii.gz'))
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = np.array(img.header.get_zooms()[:3], dtype=float)
    plano = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)
    sy, sx = zooms[plano[0]], zooms[plano[1]]
    dz = zooms[eje]
    lab, n = ndi.label(vol > METAL)
    vox = float(np.prod(zooms))
    tam = ndi.sum(vol > METAL, lab, index=np.arange(1, n + 1)) * vox
    comps = [i + 1 for i in np.argsort(-tam) if tam[i] >= 500.0][:2]
    for c in comps:
        m3 = lab == c
        ks = [k for k in range(vol.shape[0]) if m3[k].any()]
        cs = np.array([centro(m3[k]) for k in ks])
        for k in ks:
            cy, cx = centro(m3[k])
            sl = vol[k]
            valid = (sl > -300) & ~m3[k] & (sl < METAL)
            fila(rows, 'real', 'crudo', 'metal_0039_c%d' % c, 0, k, sl, valid, cy, cx, sy, sx, m3[k])
        gap = int(np.ceil(15.0 / dz))
        kc = (list(range(max(ks) + gap, min(vol.shape[0], max(ks) + gap + 12))) +
              list(range(max(0, min(ks) - gap - 12), max(0, min(ks) - gap))))
        for k in kc:
            sl = vol[k]
            prox = m3[max(ks)] if k > max(ks) else m3[min(ks)]
            cy, cx = centro(prox)
            valid = (sl > -300) & (sl < METAL) & ~prox
            fila(rows, 'control_anatomia_real', 'crudo', 'metal_0039_c%d' % c, 0, k, sl, valid, cy, cx, sy, sx, prox)
        print('real c%d' % c, len(ks), 'cortes;', len(kc), 'controles', flush=True)


def resumen(rows):
    por = defaultdict(list)
    for r in rows:
        por[(r['brazo'], r['modo'], r['K'], r['ventana'], r['paciente'], r['semilla'])].append(r)
    nivel = defaultdict(lambda: defaultdict(list))
    for (br, mo, K, ve, pa, se), rs in por.items():
        nivel[(br, mo, K, ve)][pa].append((np.median([x['eta2_exc'] for x in rs]), np.median([x['std'] for x in rs])))
    L = ['# C4 — anisotropía angular (exploratorio; protocolo `c4_protocolo.md`)', '',
         'η²_exc: 0 = isotrópico (halo liso / ruido), mayor = más estructura angular. '
         'Corte → semilla → paciente (mediana) → brazo (mediana; rango entre pacientes).', '']
    for (K, ve, titulo) in [(24, 'A', '## Principal: K=24, recorte [-500, 1300] HU'),
                            (12, 'A', '## Sensibilidad: K=12, [-500, 1300]'),
                            (48, 'A', '## Sensibilidad: K=48, [-500, 1300]'),
                            (24, 'B', '## Sensibilidad: K=24, [-1000, 3000]')]:
        L += [titulo, '', '| brazo | modo | pacientes/comp. | semillas | η²_exc mediana | rango entre pacientes | std anillo (HU) |',
              '|---|---|---|---|---|---|---|']
        orden = ['real', 'control_anatomia_real', 'control_anatomia', 'peters_Ti', 'run04_mejor', 'run05a_mejor', 'run05b_mejor']
        for br in orden:
            for mo in ('crudo', 'residuo'):
                d = nivel.get((br, mo, K, ve))
                if not d:
                    continue
                pm = {p: (np.median([a for a, _ in v]), np.median([b for _, b in v]), len(v)) for p, v in d.items()}
                e = [x[0] for x in pm.values()]
                L.append('| %s | %s | %d | %s | %.3f | %.3f – %.3f | %.0f |' % (
                    br, mo, len(pm), '/'.join(str(x[2]) for x in pm.values()), np.median(e), min(e), max(e),
                    np.median([x[1] for x in pm.values()])))
        L.append('')
    L += ['Lectura: ver `c4_protocolo.md`. Limitaciones: real = otro paciente/escáner; 2 tornillos; 2 pacientes sintéticos '
          'de validación; run05b con semillas incompletas (0101 s0–2, 0102 s0); η² no distingue rayas de bordes '
          'anatómicos radiales; modo crudo incluye anatomía.']
    (AQUI / ('c4_resumen_%s.md' % MODO)).write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


def validez():
    """C0: la metrica debe dar ~0 en un halo liso (M elipse oblicua) y >0 con rayas angulares."""
    yy, xx = np.indices((512, 512))
    cy = cx = 256
    M = ((yy - cy) / 9.0) ** 2 + ((xx - cx) / 3.0) ** 2 <= 1
    dist = ndi.distance_transform_edt(~M, sampling=(0.9, 0.9))
    rng = np.random.default_rng(0)
    th = np.arctan2(yy - cy, xx - cx)
    liso = 1500 * np.exp(-dist / 6.0)
    out = []
    for nombre, img in [('halo liso', liso), ('halo liso + ruido 150 HU', liso + rng.normal(0, 150, liso.shape)),
                        ('halo + 8 rayas (+-30%)', liso * (1 + 0.3 * np.cos(8 * th))),
                        ('halo + 8 rayas + ruido 150 HU', liso * (1 + 0.3 * np.cos(8 * th)) + rng.normal(0, 150, liso.shape))]:
        rd = ndi.distance_transform_edt(~M, sampling=(0.9, 0.9)) if MODO == 'distancia' else None
        r = eta2_exc(img, ~M, cy, cx, 0.9, 0.9, 24, 'A', rd)
        out.append((nombre, r[0]))
    return out


def main():
    AQUI.mkdir(exist_ok=True)
    print('C0 validez (modo %s):' % MODO, [(n, round(v, 3)) for n, v in validez()])
    rows = []
    reales(rows)
    sinteticos(rows)
    with open(AQUI / ('c4_filas_%s.csv' % MODO), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    resumen(rows)


if __name__ == '__main__':
    main()
