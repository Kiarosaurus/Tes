"""Metricas de textura y estatica para el script maestro (docs/01-decisiones.md 2026-11-21 (18) punto 4). EXPLORATORIO.

Sobre salidas de `a15` (NIfTI: original, M, G, sintetica por semilla) en validacion, cortes con M:
- `razon_textura`: desviacion estandar de la alta frecuencia (x - caja 5 px) dentro de G (tejido blando, sin M dilatada 6 px) dividida por la de un anillo
  justo fuera de G (15 px), tambien en tejido blando; 1 = textura igual a la de afuera. Referencia: el mismo cociente en la imagen original.
- `frac_M_bajo_2500`: fraccion de pixeles de M por debajo de 2500 HU ("gris" dentro del implante).
- `salto_borde_G`: mediana de |sintetica - original| en el anillo de 1 px dentro del borde de G.
Mediana por paciente (cortes y semillas). Uso:
    python textura_metricas.py --dir <carpeta a15> --etiqueta <etiq> [--casos 0101 0102] --out salida.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi

CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']
ST = ndi.generate_binary_structure(2, 1)


def alta_frec(sl: np.ndarray) -> np.ndarray:
    return sl - ndi.uniform_filter(sl, size=5, mode='reflect')


def desv(hp: np.ndarray, m: np.ndarray) -> float | None:
    return float(np.sqrt(np.mean(hp[m] ** 2))) if m.sum() >= 50 else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', type=Path, required=True)
    ap.add_argument('--etiqueta', required=True)
    ap.add_argument('--casos', nargs='+', default=CASOS)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    res = {'etiqueta': a.etiqueta, 'por_paciente': {}}
    rt, ro, fm, sj = {}, {}, {}, {}
    for caso in a.casos:
        pac = caso.split('_')[2]
        d = a.dir
        G = nib.load(str(d / f'a15_{caso}_G.nii.gz')).get_fdata(dtype=np.float32) > 0.5
        M = nib.load(str(d / f'a15_{caso}_M.nii.gz')).get_fdata(dtype=np.float32) > 0.5
        O = nib.load(str(d / f'a15_{caso}_original.nii.gz')).get_fdata(dtype=np.float32)
        ks = [k for k in range(M.shape[2]) if M[:, :, k].any()]
        r_t, r_o, f_m, s_j = [], [], [], []
        for s in range(5):
            f = d / f'a15_{caso}_{a.etiqueta}_s{s}_sintetica.nii.gz'
            if not f.exists():
                continue
            V = nib.load(str(f)).get_fdata(dtype=np.float32)
            for k in ks:
                g2, m2, o2, v2 = G[:, :, k], M[:, :, k], O[:, :, k], V[:, :, k]
                blando = (o2 > -50) & (o2 < 150)
                dentro = g2 & blando & ~ndi.binary_dilation(m2, ST, iterations=6)
                fuera = ndi.binary_dilation(g2, ST, iterations=15) & ~ndi.binary_dilation(g2, ST, iterations=2) & blando & ~g2
                borde = g2 & ~ndi.binary_erosion(g2, ST) & ~m2 & (o2 > -300)
                sv, so, ov = desv(alta_frec(v2), dentro), desv(alta_frec(v2), fuera), desv(alta_frec(o2), dentro)
                oo = desv(alta_frec(o2), fuera)
                if sv and so:
                    r_t.append(sv / so)
                if ov and oo:
                    r_o.append(ov / oo)
                if m2.sum() >= 20:
                    f_m.append(float(np.mean(v2[m2] < 2500)))
                if borde.sum() >= 20:
                    s_j.append(float(np.median(np.abs(v2 - o2)[borde])))
        rt[pac], ro[pac], fm[pac], sj[pac] = (float(np.median(x)) if x else None for x in (r_t, r_o, f_m, s_j))
    def med(dic):
        v = [x for x in dic.values() if x is not None]
        return float(np.median(v)) if v else None
    res['razon_textura'] = {'mediana': med(rt), 'por_paciente': rt}
    res['razon_textura_original'] = {'mediana': med(ro), 'por_paciente': ro}
    res['frac_M_bajo_2500'] = {'mediana': med(fm), 'por_paciente': fm}
    res['salto_borde_G_HU'] = {'mediana': med(sj), 'por_paciente': sj}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2), encoding='utf-8')
    print(json.dumps({k: v['mediana'] for k, v in res.items() if isinstance(v, dict) and 'mediana' in v}))


if __name__ == '__main__':
    main()
