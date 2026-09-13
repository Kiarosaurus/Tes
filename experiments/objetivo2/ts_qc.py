"""QC de TotalSegmentator sobre la cohorte (#29, #48, #49, #50); generaliza `ts_piloto_qc.py`.

POR QUE
-------
El piloto (`ts_piloto_qc.py`, que se conserva sin cambios como evidencia de #49 y #50) mostro
tres cosas: TS no trunca la pelvis; el modelo de recorte cambia la mascara en la articulacion
sacroiliaca y el ala (#49); y un S1 de R1 un nivel arriba produce "ala < 150 HU" midiendo tejido
blando (#50). Este script mide lo mismo en todos los volumenes que corrio `ts_cohorte.sbatch`,
para la revision manual y para las decisiones de #48, #49 y #50. **No decide nada.**

QUE MIDE (por volumen; mismas definiciones que el piloto)
--------------------------------------------------------
1. `ts_qc.csv`, caso x modo x estructura: voxeles, volumen, caja y centroide en mm, caras del
   FOV que toca, mediana HU y fraccion <= 150 HU dentro de la mascara, solape con las otras
   estructuras, techo en la columna media respecto al platillo de S1 de R1 (solo `sacrum` y
   `vertebrae_S1`), y entre los dos recortes: Dice, voxeles exclusivos y diferencia de caja.
2. `ts_qc_esferas.csv`: esferas de E9b, si el volumen tiene S1 en R1. `control_marco_ok`
   compara la mediana HU recalculada con `e9b_densidad_s1.csv`.
3. `ts_qc_tornillos.csv`: componentes de E8 con `candidato_IS = si`. Controles de marco:
   `frac_vol_E8_en_cilindro` y `frac_eje_metal_r2mm` (`frac_eje_metal` no sirve, ver piloto).
4. `ts_qc_errores.csv`: volumenes que fallaron y por que.
5. `laminas/<caso>_planos.png` (y `_tornillos.png`) para la revision manual.

Coordenadas: RAS+ con `cargar` de `r1_landmarks.py`, mm = indice x zoom, el mismo marco que R1,
E8 y E9b. **Reanudable:** salta los casos que ya estan en `ts_qc.csv` o `ts_qc_errores.csv`, y
los que aun no tienen las 8 mascaras (job de TS en curso).

USO
---
Khipu (ver `KHIPU.md`):
    python ts_qc.py --ts-dir ~/metalsynth/data/ts_total --ct-dir ~/metalsynth/data/ts_input \
        --refs-dir . --out-dir ~/metalsynth/data/ts_total_qc
Local, sobre el piloto (prueba):
    python ts_qc.py --ts-dir ../../data/derivados/ts_piloto --out-dir outputs/ts_qc_prueba
"""
from __future__ import annotations

import argparse
import csv
import gc
import traceback
from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd

from e9b_densidad_s1 import ALA_LATERAL_MM, BAJO_PLATILLO_MM, BONE_HU, RADIO_MM
from r1_landmarks import cargar
from ts_piloto_qc import (COLORES, ESTRUCTURAS, MARGEN_MM, METAL_HU, MODOS, RADIO_TORNILLO_MM,
                          VENTANA, caja, caras_fov, eje_tornillo, esfera_local, fraccion,
                          mascara, techo_dz)

CAMPOS = ['Caso', 'modo', 'estructura', 'n_vox', 'vol_ml', 'toca_fov',
          'x_min_mm', 'x_max_mm', 'y_min_mm', 'y_max_mm', 'z_min_mm', 'z_max_mm',
          'cx_mm', 'cy_mm', 'cz_mm', 'hu_p50', 'frac_bajo150', 'solape_otras_vox',
          'techo_linea_media_dz_mm', 'dice_3v6', 'solo_este_modo_vox', 'dif_caja_3v6_max_mm']
CAMPOS_ESF = ['Caso', 'esfera', 'modo', 'n_vox', 'hu_p50', 'hu_p50_e9b', 'control_marco_ok',
              'frac_sobre150', 'frac_en_sacro_S1', 'frac_en_cadera', 'frac_fuera_mascaras',
              'frac_bajo150_recuperada_sacro_S1']
CAMPOS_TOR = ['Caso', 'comp', 'modo', 'L_mm', 'n_puntos_eje', 'frac_eje_metal', 'frac_eje_metal_r2mm',
              'frac_vol_E8_en_cilindro', 'frac_eje_en_sacro_S1', 'frac_eje_en_cadera', 'frac_eje_fuera',
              'n_vox_metal_cilindro', 'frac_metal_en_mascaras']
NAN = float('nan')


def qc_caso(caso: str, ruta_ct: Path, ts_dir: Path, r1: pd.DataFrame, e9b: pd.DataFrame,
            e8: pd.DataFrame, dir_laminas: Path | None) -> tuple[list[dict], list[dict], list[dict]]:
    """Mide un volumen con los dos recortes y, si `dir_laminas`, escribe sus laminas."""
    ref = nib.load(ruta_ct)
    ct, zoom = cargar(ruta_ct)
    zoom = zoom.astype(float)
    forma_full = np.array(ct.shape)
    platillo = None
    if caso in r1.index and r1.loc[caso, 'S1_hallado'] == 'si':
        f = r1.loc[caso]
        platillo = np.array([f['S1_x_mm'], f['S1_y_mm'], f['S1_z_mm']], dtype=float)
    esferas: dict[str, np.ndarray] = {}
    if platillo is not None:
        c_esf = platillo - np.array([0.0, 0.0, BAJO_PLATILLO_MM])
        esferas = {n: c_esf + np.array([dx, 0.0, 0.0])
                   for n, dx in (('cuerpo', 0.0), ('ala_izq', -ALA_LATERAL_MM), ('ala_der', ALA_LATERAL_MM))}
    torn = e8[(e8['Caso'] == caso) & (e8['candidato_IS'] == 'si')]

    # Paso 1: cajas sobre el volumen completo y rejilla igual a la del CT.
    cajas = {}
    for modo in MODOS:
        for est in ESTRUCTURAS:
            p = ts_dir / caso / modo / f'{est}.nii.gz'
            img = nib.load(p)
            if img.shape[:3] != ref.shape[:3] or not np.allclose(img.affine, ref.affine, atol=1e-3):
                raise ValueError(f'{modo}/{est}: rejilla distinta de la del CT')
            m = mascara(p)
            cajas[modo, est] = caja(m)
            del m
    llenas = [cj for cj in cajas.values() if cj is not None]
    if not llenas:
        raise ValueError('las 8 mascaras estan vacias')

    # Recorte comun: mascaras, esferas y tornillos, mas un margen.
    lo = np.min([cj[0] for cj in llenas], axis=0).astype(float)
    hi = np.max([cj[1] for cj in llenas], axis=0).astype(float)
    puntos = [c + s * RADIO_MM for c in esferas.values() for s in (-1.0, 1.0)]
    for _, t in torn.iterrows():
        c, u, L = eje_tornillo(t)
        puntos += [c - (L / 2 + 5) * u, c + (L / 2 + 5) * u]
    if puntos:
        pts_idx = np.array(puntos) / zoom
        lo, hi = np.minimum(lo, np.floor(pts_idx.min(0))), np.maximum(hi, np.ceil(pts_idx.max(0)))
    margen = np.ceil(MARGEN_MM / zoom)
    off = np.maximum(lo - margen, 0).astype(int)
    fin = np.minimum(hi + margen + 1, forma_full).astype(int)
    sl = tuple(slice(off[a], fin[a]) for a in range(3))
    sub = np.array(ct[sl])
    del ct
    gc.collect()
    forma = np.array(sub.shape)

    M = {}
    for modo in MODOS:
        for est in ESTRUCTURAS:
            m = mascara(ts_dir / caso / modo / f'{est}.nii.gz')
            M[modo, est] = m[sl].copy()
            del m
    union = {modo: np.logical_or.reduce([M[modo, e] for e in ESTRUCTURAS]) for modo in MODOS}
    sacro = {modo: M[modo, 'sacrum'] | M[modo, 'vertebrae_S1'] for modo in MODOS}
    cadera = {modo: M[modo, 'hip_left'] | M[modo, 'hip_right'] for modo in MODOS}

    # 1. Estructuras.
    filas = []
    vox_ml = float(np.prod(zoom)) / 1000.0
    for est in ESTRUCTURAS:
        a, b = M[MODOS[0], est], M[MODOS[1], est]
        na, nb, inter = int(a.sum()), int(b.sum()), int((a & b).sum())
        dice = round(2 * inter / (na + nb), 4) if na + nb else NAN
        ca, cb = cajas[MODOS[0], est], cajas[MODOS[1], est]
        dif_caja = (round(float(np.max(np.abs(np.concatenate([(ca[0] - cb[0]) * zoom, (ca[1] - cb[1]) * zoom])))), 1)
                    if ca is not None and cb is not None else NAN)
        for modo, m, n, otro in ((MODOS[0], a, na, b), (MODOS[1], b, nb, a)):
            otras = np.logical_or.reduce([M[modo, e] for e in ESTRUCTURAS if e != est])
            cj = cajas[modo, est]
            fila = {'Caso': caso, 'modo': modo, 'estructura': est, 'n_vox': n,
                    'vol_ml': round(n * vox_ml, 1), 'toca_fov': caras_fov(cj, forma_full)}
            for e_i, eje in enumerate('xyz'):
                fila[f'{eje}_min_mm'] = round(float(cj[0][e_i] * zoom[e_i]), 1) if cj else NAN
                fila[f'{eje}_max_mm'] = round(float(cj[1][e_i] * zoom[e_i]), 1) if cj else NAN
            if n:
                hu = sub[m]
                cen = (np.array(np.nonzero(m)).mean(axis=1) + off) * zoom
                fila.update({'cx_mm': round(float(cen[0]), 1), 'cy_mm': round(float(cen[1]), 1),
                             'cz_mm': round(float(cen[2]), 1), 'hu_p50': float(np.median(hu)),
                             'frac_bajo150': round(float((hu <= BONE_HU).mean()), 3)})
                del hu
            else:
                fila.update({'cx_mm': NAN, 'cy_mm': NAN, 'cz_mm': NAN, 'hu_p50': NAN, 'frac_bajo150': NAN})
            fila.update({
                'solape_otras_vox': int((m & otras).sum()),
                'techo_linea_media_dz_mm': (techo_dz(m, zoom, off, platillo)
                                            if platillo is not None and est in ('sacrum', 'vertebrae_S1') else NAN),
                'dice_3v6': dice,
                'solo_este_modo_vox': int((m & ~otro).sum()),
                'dif_caja_3v6_max_mm': dif_caja,
            })
            filas.append(fila)
            del otras
    gc.collect()

    # 2. Esferas de E9b.
    filas_esf = []
    for nombre, centro in esferas.items():
        s_sl, dentro = esfera_local(forma, zoom, off, centro)
        v = sub[s_sl][dentro]
        if v.size == 0:
            continue
        bajo = v <= BONE_HU
        ref_hu = float(e9b.loc[caso, f'hu_{nombre}']) if caso in e9b.index else NAN
        med = float(np.median(v))
        for modo in MODOS:
            en_sacro = sacro[modo][s_sl][dentro]
            en_cadera = cadera[modo][s_sl][dentro]
            filas_esf.append({
                'Caso': caso, 'esfera': nombre, 'modo': modo, 'n_vox': int(v.size),
                'hu_p50': med, 'hu_p50_e9b': ref_hu,
                'control_marco_ok': bool(abs(med - ref_hu) <= 1.0) if not np.isnan(ref_hu) else '',
                'frac_sobre150': round(float((~bajo).mean()), 3),
                'frac_en_sacro_S1': round(float(en_sacro.mean()), 3),
                'frac_en_cadera': round(float(en_cadera.mean()), 3),
                'frac_fuera_mascaras': round(float((~(en_sacro | en_cadera)).mean()), 3),
                'frac_bajo150_recuperada_sacro_S1': fraccion(en_sacro, bajo),
            })

    # 3. Tornillos de E8.
    filas_tor = []
    for _, t in torn.iterrows():
        c, u, L = eje_tornillo(t)
        pts = c[None, :] + np.arange(-L / 2, L / 2 + 1e-6, 1.0)[:, None] * u[None, :]
        idx = np.rint(pts / zoom).astype(int) - off
        idx = idx[np.all((idx >= 0) & (idx < forma), axis=1)]
        if len(idx) == 0:
            continue
        hu_eje = sub[idx[:, 0], idx[:, 1], idx[:, 2]]
        c_lo = np.maximum(np.floor((pts.min(0) - RADIO_TORNILLO_MM) / zoom).astype(int) - off, 0)
        c_hi = np.minimum(np.ceil((pts.max(0) + RADIO_TORNILLO_MM) / zoom).astype(int) - off + 1, forma)
        c_sl = tuple(slice(c_lo[a], c_hi[a]) for a in range(3))
        ii, jj, kk = np.ogrid[c_lo[0]:c_hi[0], c_lo[1]:c_hi[1], c_lo[2]:c_hi[2]]
        X, Y, Z = ((ii + off[0]) * zoom[0] - c[0], (jj + off[1]) * zoom[1] - c[1],
                   (kk + off[2]) * zoom[2] - c[2])
        tpar = np.clip(X * u[0] + Y * u[1] + Z * u[2], -L / 2, L / 2)
        d2 = (X - tpar * u[0]) ** 2 + (Y - tpar * u[1]) ** 2 + (Z - tpar * u[2]) ** 2
        es_metal = sub[c_sl] > METAL_HU
        metal = (d2 <= RADIO_TORNILLO_MM ** 2) & es_metal
        tramos = np.unique(np.rint(np.broadcast_to(tpar, d2.shape)[(d2 <= 4.0) & es_metal] + L / 2).astype(int))
        for modo in MODOS:
            s_eje = sacro[modo][idx[:, 0], idx[:, 1], idx[:, 2]]
            k_eje = cadera[modo][idx[:, 0], idx[:, 1], idx[:, 2]]
            filas_tor.append({
                'Caso': caso, 'comp': int(t['comp']), 'modo': modo, 'L_mm': L,
                'n_puntos_eje': int(len(idx)),
                'frac_eje_metal': round(float((hu_eje > METAL_HU).mean()), 3),
                'frac_eje_metal_r2mm': round(len(tramos) / len(pts), 3),
                'frac_vol_E8_en_cilindro': round(float(metal.sum()) * float(np.prod(zoom)) / float(t['vol_mm3']), 3),
                'frac_eje_en_sacro_S1': round(float(s_eje.mean()), 3),
                'frac_eje_en_cadera': round(float(k_eje.mean()), 3),
                'frac_eje_fuera': round(float((~(s_eje | k_eje)).mean()), 3),
                'n_vox_metal_cilindro': int(metal.sum()),
                'frac_metal_en_mascaras': fraccion(union[modo][c_sl], metal),
            })

    if dir_laminas is not None:
        laminas(caso, sub, M, union, zoom, off, forma, platillo, esferas, torn, dir_laminas)
    return filas, filas_esf, filas_tor


def laminas(caso: str, sub: np.ndarray, M: dict, union: dict, zoom: np.ndarray, off: np.ndarray,
            forma: np.ndarray, platillo: np.ndarray | None, esferas: dict, torn: pd.DataFrame,
            destino: Path) -> None:
    """Axial/coronal/sagital por modo mas diferencias; axiales por cada tornillo."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    leyenda = [Line2D([], [], color=c, lw=2, label=e) for e, c in COLORES.items()]

    def ext(p: int, q: int) -> tuple[float, float, float, float]:
        return (off[p] * zoom[p], (off[p] + forma[p]) * zoom[p], off[q] * zoom[q], (off[q] + forma[q]) * zoom[q])

    def contornos(ax, corte, modo: str, e) -> None:
        for est in ESTRUCTURAS:
            m2 = corte(M[modo, est]).T
            if m2.any():
                ax.contour(m2.astype(np.uint8), levels=[0.5], colors=COLORES[est],
                           linewidths=0.9, extent=e, origin='lower')

    if platillo is not None:
        centro = platillo - np.array([0.0, 0.0, BAJO_PLATILLO_MM])
        ref_txt = 'S1 de R1'
        leyenda.append(Line2D([], [], color='yellow', lw=1, label='esferas E9b (6 mm)'))
    else:
        centro = (off + forma / 2) * zoom
        ref_txt = 'centro del recorte (sin S1 en R1)'
    k = int(np.clip(round(centro[2] / zoom[2]) - off[2], 0, forma[2] - 1))
    j = int(np.clip(round(centro[1] / zoom[1]) - off[1], 0, forma[1] - 1))
    i = int(np.clip(round(centro[0] / zoom[0]) - off[0], 0, forma[0] - 1))
    cortes = [
        (f'axial z={centro[2]:.0f} mm', lambda a: a[:, :, k], (0, 1), 'x (-> derecha)', 'y (-> anterior)'),
        (f'coronal y={centro[1]:.0f} mm', lambda a: a[:, j, :], (0, 2), 'x (-> derecha)', 'z (-> craneal)'),
        (f'sagital x={centro[0]:.0f} mm', lambda a: a[i, :, :], (1, 2), 'y (-> anterior)', 'z (-> craneal)'),
    ]
    fig, ejes = plt.subplots(3, 3, figsize=(16, 14))
    for col, (titulo, corte, (p, q), xl, yl) in enumerate(cortes):
        e = ext(p, q)
        base = np.clip(corte(sub), *VENTANA).T
        for fil, modo in enumerate(list(MODOS) + ['diferencia']):
            ax = ejes[fil, col]
            ax.imshow(base, cmap='gray', origin='lower', extent=e)
            if modo == 'diferencia':
                u3, u6 = corte(union[MODOS[0]]).T, corte(union[MODOS[1]]).T
                rgba = np.zeros(u3.shape + (4,))
                rgba[u3 & ~u6] = (1.0, 0.0, 0.0, 1.0)
                rgba[u6 & ~u3] = (0.0, 0.5, 1.0, 1.0)
                ax.imshow(rgba, origin='lower', extent=e, interpolation='nearest')
                ax.set_title(f'{titulo} | rojo solo 3 mm: {int((u3 & ~u6).sum())} vox, '
                             f'azul solo 6 mm: {int((u6 & ~u3).sum())} vox', fontsize=9)
            else:
                contornos(ax, corte, modo, e)
                ax.set_title(f'{modo} | {titulo}', fontsize=9)
            for nombre, c in esferas.items():
                if (p, q) == (1, 2) and nombre != 'cuerpo':
                    continue
                ax.add_patch(plt.Circle((c[p], c[q]), RADIO_MM, fill=False, ec='yellow', lw=0.8))
            ax.set_xlabel(f'{xl} mm', fontsize=8)
            ax.set_ylabel(f'{yl} mm', fontsize=8)
            ax.tick_params(labelsize=7)
    fig.legend(handles=leyenda, loc='lower center', ncol=5, fontsize=10)
    fig.suptitle(f'{caso}: contornos TS por recorte (cortes por {ref_txt}); '
                 f'fila 3 = diferencia de la union de las 4 mascaras', fontsize=12)
    fig.tight_layout(rect=(0, 0.03, 1, 0.97))
    fig.savefig(destino / f'{caso}_planos.png', dpi=80)
    plt.close(fig)

    if len(torn):
        fig, ejes = plt.subplots(len(torn), 2, figsize=(14, 5 * len(torn)), squeeze=False)
        for fil, (_, t) in enumerate(torn.iterrows()):
            c, u, L = eje_tornillo(t)
            kt = int(np.clip(round(c[2] / zoom[2]) - off[2], 0, forma[2] - 1))
            e = ext(0, 1)
            for col, modo in enumerate(MODOS):
                ax = ejes[fil, col]
                ax.imshow(np.clip(sub[:, :, kt], *VENTANA).T, cmap='gray', origin='lower', extent=e)
                contornos(ax, lambda a: a[:, :, kt], modo, e)
                a0, a1 = c - L / 2 * u, c + L / 2 * u
                ax.plot([a0[0], a1[0]], [a0[1], a1[1]], color='magenta', lw=0.8, ls='--')
                ax.set_xlim(c[0] - L / 2 - 25, c[0] + L / 2 + 25)
                ax.set_ylim(c[1] - 45, c[1] + 45)
                ax.set_title(f'comp {int(t["comp"])} | {modo} | axial z={c[2]:.0f} mm; magenta = eje E8',
                             fontsize=9)
                ax.set_xlabel('x (-> derecha) mm', fontsize=8)
                ax.set_ylabel('y (-> anterior) mm', fontsize=8)
        fig.legend(handles=leyenda[:4], loc='lower center', ncol=4, fontsize=10)
        fig.tight_layout(rect=(0, 0.03, 1, 1))
        fig.savefig(destino / f'{caso}_tornillos.png', dpi=80)
        plt.close(fig)


def abrir(ruta: Path, campos: list[str]):
    """Abre un CSV en modo anexar; escribe la cabecera si es nuevo."""
    nuevo = not ruta.exists()
    h = ruta.open('a', encoding='utf-8', newline='')
    w = csv.DictWriter(h, fieldnames=campos)
    if nuevo:
        w.writeheader()
    return h, w


def main() -> None:
    """Recorre los casos de `--ts-dir`; reanudable por lotes (`--max`)."""
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--ts-dir', type=Path, required=True, help='<caso>/<modo>/<estructura>.nii.gz')
    parser.add_argument('--ct-dir', type=Path, default=root / 'data', help='busca dataset*.nii.gz recursivamente')
    parser.add_argument('--refs-dir', type=Path, default=here,
                        help='r1_landmarks.csv, e9b_densidad_s1.csv, e8_componentes.csv')
    parser.add_argument('--out-dir', type=Path, default=here / 'outputs' / 'ts_qc')
    parser.add_argument('--casos', nargs='*', default=None)
    parser.add_argument('--sin-laminas', action='store_true')
    parser.add_argument('--max', type=int, default=None)
    args = parser.parse_args()

    ts_dir = args.ts_dir.expanduser()
    refs = args.refs_dir.expanduser()
    out = args.out_dir.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    dir_lam = None if args.sin_laminas else out / 'laminas'
    if dir_lam is not None:
        dir_lam.mkdir(exist_ok=True)
    r1 = pd.read_csv(refs / 'r1_landmarks.csv').set_index('Caso')
    e9b = pd.read_csv(refs / 'e9b_densidad_s1.csv').set_index('Caso')
    e8 = pd.read_csv(refs / 'e8_componentes.csv')
    rutas = {p.name[:-len('.nii.gz')]: p for p in args.ct_dir.expanduser().rglob('dataset*.nii.gz')}
    casos = args.casos or sorted(d.name for d in ts_dir.iterdir() if d.is_dir() and not d.name.startswith('_'))
    hechos: set[str] = set()
    for nombre in ('ts_qc.csv', 'ts_qc_errores.csv'):
        if (out / nombre).exists():
            hechos |= set(pd.read_csv(out / nombre)['Caso'])
    print(f'{len(casos)} casos en {ts_dir}; {len(hechos)} ya procesados', flush=True)

    salidas = {'est': abrir(out / 'ts_qc.csv', CAMPOS), 'esf': abrir(out / 'ts_qc_esferas.csv', CAMPOS_ESF),
               'tor': abrir(out / 'ts_qc_tornillos.csv', CAMPOS_TOR),
               'err': abrir(out / 'ts_qc_errores.csv', ['Caso', 'Error'])}
    nuevos = 0
    try:
        for caso in casos:
            if caso in hechos:
                continue
            faltan = [f'{m}/{e}' for m in MODOS for e in ESTRUCTURAS
                      if not (ts_dir / caso / m / f'{e}.nii.gz').exists()]
            if faltan:
                print(f'{caso}: incompleto ({len(faltan)} mascaras faltan), se salta', flush=True)
                continue
            if args.max is not None and nuevos >= args.max:
                break
            nuevos += 1
            try:
                if caso not in rutas:
                    raise FileNotFoundError('CT no encontrado en --ct-dir')
                filas, esf, tor = qc_caso(caso, rutas[caso], ts_dir, r1, e9b, e8, dir_lam)
            except Exception as exc:  # un caso roto no detiene la cohorte
                salidas['err'][1].writerow({'Caso': caso, 'Error': f'{type(exc).__name__}: {exc}'})
                salidas['err'][0].flush()
                print(f'{caso}: ERROR {exc}', flush=True)
                traceback.print_exc()
                continue
            finally:
                gc.collect()
            for clave, datos in (('est', filas), ('esf', esf), ('tor', tor)):
                salidas[clave][1].writerows(datos)
                salidas[clave][0].flush()
            print(f'{caso}: ok ({len(esf) // 2} esferas, {len(tor) // 2} tornillos)', flush=True)
    finally:
        for h, _ in salidas.values():
            h.close()


if __name__ == '__main__':
    main()
