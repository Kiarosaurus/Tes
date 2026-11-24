"""Cuantifica dos observaciones visuales de la autora (2026-11-21), EXPLORATORIO:
(1) cambio brusco en el borde de la region generada G; (2) pixeles muy solidos ('estatica') sobre el implante.

(1) salto en el borde de G: por corte, mediana de |sintetica - original| en el anillo de 1 px DENTRO del borde de G (fuera de G la sintetica
    es copia exacta, |dif| = 0), sobre pixeles de cuerpo (original > -300) y sin M. Referencia fisica: |Ti_A - limpia_A| de Peters en los mismos pixeles.
(2) estatica en M: fraccion de pixeles de M (dentro del corte) con |HU - mediana 3x3| > 1500 HU, y fraccion de M por debajo de 2500 HU.
    Peters: mismo calculo con su M. (El real no se calcula: su M se define por umbral y sesgaria.)
Uso: METALSYNTH_REPO=<repo> python -I borde_estatica.py --b-min <carpeta b_min>
"""
from __future__ import annotations
import argparse, os
from collections import defaultdict
from pathlib import Path
import numpy as np, nibabel as nib
from scipy import ndimage as ndi

REPO = Path(os.environ.get('METALSYNTH_REPO', r'D:/UTEC/CICLOX/Salvar-El-Ciclo/PFCII/metalsynth-pelvis'))
OUT3 = REPO / 'experiments/objetivo3/outputs/obj3_pose'
CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']
ARMS = ['run04_mejor', 'run04_mejor_p50_e0.3', 'run04_mejor_p100_e0.3', 'b_min_l0', 'b_min_l0.8_t1000', 'b_min_l3_t300']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--b-min', type=Path, required=True)
    ap.add_argument('--out', type=Path, default=Path(__file__).resolve().parent / 'c4' / 'borde_estatica_resumen.md')
    a = ap.parse_args()
    dirs = {'run04_mejor': OUT3 / 'delta/run04_mejor'}
    dirs.update({k: a.b_min / k for k in ARMS[1:]})
    salto = defaultdict(lambda: defaultdict(list))
    estat = defaultdict(lambda: defaultdict(list))
    gris = defaultdict(lambda: defaultdict(list))
    struct = ndi.generate_binary_structure(2, 1)
    for caso in CASOS:
        pac = caso.split('_')[2]
        z = np.load(OUT3 / f'peters_val/a19_{caso}.npz')
        ks = [int(k) for k in z['ks']]
        cand = [(i, k) for i, k in enumerate(ks) if z['M'][i].any()]
        for br, d in dirs.items():
            G3 = nib.load(str(d / f'a15_{caso}_G.nii.gz')).get_fdata(dtype=np.float32) > 0.5
            for s in range(5):
                f = d / f'a15_{caso}_{br}_s{s}_sintetica.nii.gz'
                if not f.exists():
                    continue
                v = nib.load(str(f)).get_fdata(dtype=np.float32)
                for i, k in cand:
                    G2, M, orig = G3[:, :, k], z['M'][i], z['original'][i]
                    borde = G2 & ~ndi.binary_erosion(G2, struct) & ~M & (orig > -300)
                    if borde.sum() >= 20:
                        salto[br][pac].append(float(np.median(np.abs(v[:, :, k] - orig)[borde])))
                    sl = v[:, :, k]
                    med = ndi.median_filter(sl, size=3)
                    if M.sum() >= 20:
                        estat[br][pac].append(float(np.mean(np.abs(sl - med)[M] > 1500)))
                        gris[br][pac].append(float(np.mean(sl[M] < 2500)))
        # Peters como referencia fisica
        for i, k in cand:
            G2 = nib.load(str(dirs['run04_mejor'] / f'a15_{caso}_G.nii.gz')).get_fdata(dtype=np.float32)[:, :, k] > 0.5
            M, orig = z['M'][i], z['original'][i]
            borde = G2 & ~ndi.binary_erosion(G2, struct) & ~M & (orig > -300)
            if borde.sum() >= 20:
                salto['peters_Ti'][pac].append(float(np.median(np.abs(z['Ti_A'][i] - z['limpia_A'][i])[borde])))
            sl = z['Ti_A'][i]
            med = ndi.median_filter(sl, size=3)
            if M.sum() >= 20:
                estat['peters_Ti'][pac].append(float(np.mean(np.abs(sl - med)[M] > 1500)))
                gris['peters_Ti'][pac].append(float(np.mean(sl[M] < 2500)))
        print('paciente', pac, flush=True)
    L = ['# Observaciones visuales de la autora cuantificadas (exploratorio; `borde_estatica.py`)', '',
         'Validación 0101/0102, semillas 0–4, cortes con M de Peters. Mediana por paciente (cortes y semillas); entre paréntesis, los dos pacientes.', '',
         '| brazo | salto en el borde de G, mediana \\|Δ\\| 1 px dentro (HU) | M con \\|HU − mediana 3×3\\| > 1500 HU | M por debajo de 2500 HU |', '|---|---|---|---|']
    def fmt(d, f='%.0f'):
        pp = {p: np.median(v) for p, v in d.items()}
        return (f % np.median(list(pp.values()))) + ' (' + ', '.join(f'{p} ' + (f % v) for p, v in sorted(pp.items())) + ')'
    for br in ['peters_Ti'] + ARMS:
        L.append('| %s | %s | %s | %s |' % (br, fmt(salto[br]) if salto[br] else '-', fmt({p: np.array(v) * 100 for p, v in estat[br].items()}, '%.1f %%'),
                                             fmt({p: np.array(v) * 100 for p, v in gris[br].items()}, '%.1f %%')))
    L += ['', 'Límites: 2 pacientes; Peters = referencia física; un solo umbral de «estática» (1500 HU) y de «gris» (2500 HU); el real no se calcula porque su M se define por umbral.']
    a.out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
