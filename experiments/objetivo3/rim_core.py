"""Brillo del borde del tornillo frente a su interior (observacion de la autora, 2026-11-20): EXPLORATORIO.

Definicion igual para TODOS los brazos (para no sesgar por como se define M): metal := HU > 2500 en el propio corte del
brazo. Sintetico/Peters: pixeles > 2500 dentro de M dilatada 3 px. Real: componente conexo > 2500 (metal_0039).
Por corte: borde = pixeles de metal a <= 1.0 mm del no-metal; interior = a >= 1.5 mm. ratio = mediana(borde) / mediana(interior).
ratio > 1: borde mas brillante que el interior. Se informa por paciente (mediana de cortes y semillas).
Uso: METALSYNTH_REPO=<repo> python -I rim_core.py --b-min <carpeta b_min>
"""
from __future__ import annotations
import argparse, os, sys
from collections import defaultdict
from pathlib import Path
import numpy as np, nibabel as nib
from scipy import ndimage as ndi

REPO = Path(os.environ.get('METALSYNTH_REPO', r'D:/UTEC/CICLOX/Salvar-El-Ciclo/PFCII/metalsynth-pelvis'))
OUT3 = REPO / 'experiments/objetivo3/outputs/obj3_pose'
CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']
UMBRAL, R_BORDE, R_NUCLEO, MIN_PIX = 2500.0, 1.0, 1.5, 4


def razon(sl, metal2d, sy, sx):
    d = ndi.distance_transform_edt(metal2d, sampling=(sy, sx))
    borde = metal2d & (d <= R_BORDE)
    nucleo = metal2d & (d >= R_NUCLEO)
    if borde.sum() < MIN_PIX or nucleo.sum() < MIN_PIX:
        return None
    return float(np.median(sl[borde]) / np.median(sl[nucleo])), float(np.median(sl[borde])), float(np.median(sl[nucleo]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--b-min', type=Path, required=True)
    ap.add_argument('--variantes', nargs='+', default=['run04_mejor_p100_e0.3', 'run04_mejor_p50_e0.3'])
    ap.add_argument('--out', type=Path, default=Path(__file__).resolve().parent / 'c4' / 'rim_core_resumen.md')
    a = ap.parse_args()
    res = defaultdict(lambda: defaultdict(list))   # brazo -> paciente -> [(ratio, borde, nucleo)]
    brazos = {'run04_mejor': OUT3 / 'delta/run04_mejor'}
    brazos.update({v: a.b_min / v for v in a.variantes})
    for caso in CASOS:
        z = np.load(OUT3 / f'peters_val/a19_{caso}.npz')
        ks = [int(k) for k in z['ks']]
        cand = [(i, k) for i, k in enumerate(ks) if z['M'][i].any()]
        zoom = nib.load(str(OUT3 / f'delta/run04_mejor/a15_{caso}_original.nii.gz')).header.get_zooms()
        sy, sx = float(zoom[1]), float(zoom[0])
        pac = caso.split('_')[2]
        for i, k in cand:
            Md = ndi.binary_dilation(z['M'][i], iterations=3)
            sl = z['Ti_A'][i]
            r = razon(sl, (sl > UMBRAL) & Md, sy, sx)
            if r:
                res['peters_Ti'][pac].append(r)
        for br, d in brazos.items():
            for s in range(5):
                f = d / f'a15_{caso}_{br}_s{s}_sintetica.nii.gz'
                if not f.exists():
                    continue
                v = nib.load(str(f)).get_fdata(dtype=np.float32)
                for i, k in cand:
                    Md = ndi.binary_dilation(z['M'][i], iterations=3)
                    sl = v[:, :, k]
                    r = razon(sl, (sl > UMBRAL) & Md, sy, sx)
                    if r:
                        res[br][pac].append(r)
        print('paciente', pac, flush=True)
    # real
    sys.path.insert(0, str(REPO / 'experiments/objetivo1'))
    from e6b_vae_sd15 import eje_axial
    img = nib.load(str(REPO / 'data/dataset7/dataset7_CLINIC_metal_0039_data.nii.gz'))
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zo = np.array(img.header.get_zooms()[:3], float)
    pl = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)
    lab, n = ndi.label(vol > UMBRAL)
    tam = ndi.sum(vol > UMBRAL, lab, index=np.arange(1, n + 1)) * float(np.prod(zo))
    for c in [i + 1 for i in np.argsort(-tam) if tam[i] >= 500.0][:2]:
        m3 = lab == c
        for k in [k for k in range(vol.shape[0]) if m3[k].any()]:
            r = razon(vol[k], m3[k], zo[pl[0]], zo[pl[1]])
            if r:
                res['real'][f'metal_0039_c{c}'].append(r)
    L = ['# Brillo borde/interior del tornillo (exploratorio; `rim_core.py`)', '',
         'metal := HU > 2500 en el corte de cada brazo; borde ≤ 1.0 mm del no-metal, interior ≥ 1.5 mm. ratio > 1 = borde más brillante que el interior. Mediana por paciente (cortes y semillas).', '',
         '| brazo | pacientes/componentes | ratio mediana | por paciente | borde HU | interior HU |', '|---|---|---|---|---|---|']
    for br in ['real', 'peters_Ti', 'run04_mejor'] + a.variantes:
        d = res.get(br)
        if not d:
            continue
        pp = {p: np.median([x[0] for x in v]) for p, v in d.items()}
        L.append('| %s | %d | %.3f | %s | %.0f | %.0f |' % (
            br, len(pp), np.median(list(pp.values())), ', '.join('%s %.3f' % (p, v) for p, v in sorted(pp.items())),
            np.median([x[1] for v in d.values() for x in v]), np.median([x[2] for v in d.values() for x in v])))
    L += ['', 'Limites: 2 pacientes sintéticos, 2 tornillos reales (otro paciente/escáner); el real usa componente conexo > 2500 y el sintético M dilatada 3 px (misma regla de metal, distinto origen de la máscara); Peters = referencia física.']
    a.out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
