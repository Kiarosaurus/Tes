"""QC del piloto de TotalSegmentator (#29, #48, #49) sobre `metal_0008` y `CLINIC_0002`.

POR QUE
-------
E9 quedo NO VALIDO porque la mascara HU > 150 deja fuera el esponjoso del ala sacra (#48).
El piloto de Khipu (job 51300; TS 2.18.0; `--task total --roi_subset sacrum vertebrae_S1
hip_left hip_right`) corrio cada caso con dos modelos de recorte (#49): `robust3mm`
(`--robust_crop`) y `default6mm`. Este script **no decide nada**: da cifras y laminas para que
la autora decida si TS sirve para medir el corredor y que recorte usar.

QUE MIDE
--------
1. `ts_piloto_qc.csv`, por caso x modo x estructura: voxeles, volumen, caja en mm, caras del
   FOV que toca, mediana HU y fraccion de voxeles <= 150 HU dentro de la mascara (esponjoso
   que un umbral perderia), solape con las otras estructuras, techo en la linea media respecto
   al platillo de S1 de R1, y entre recortes: Dice, voxeles exclusivos y diferencia de caja.
2. `ts_piloto_qc_esferas.csv`: las tres esferas de E9b (cuerpo de S1, alas). Fraccion dentro
   de sacrum u vertebrae_S1, dentro de las caderas y fuera; y que parte de los voxeles
   <= 150 HU recupera la mascara. La mediana HU se recalcula como **control del marco de
   coordenadas** contra `e9b_densidad_s1.csv` (debe coincidir).
3. `ts_piloto_qc_tornillos.csv`, componentes de E8 con `candidato_IS = si`: fraccion del eje
   dentro de cada mascara y fraccion del metal (> 2500 HU, cilindro de 4 mm) etiquetado como
   hueso. Controles de marco: `frac_vol_E8_en_cilindro` (el cilindro debe contener casi todo el
   volumen del componente de E8) y `frac_eje_metal_r2mm` (tramos de 1 mm del eje con metal a
   <= 2 mm). `frac_eje_metal` (metal exactamente en el voxel del eje) NO sirve de control: en el
   piloto dio 0-5% con el eje visiblemente sobre el tornillo (causa no verificada).
4. Laminas en `outputs/ts_piloto_qc/` (ignorado por git): axial por las esferas, coronal por
   S1 y sagital medio, por modo, mas una fila de diferencias entre recortes; y axiales por el
   centro de cada tornillo.

LIMITACIONES
------------
- El log de TS da el tamano del recorte, no su posicion: "toca FOV" y la diferencia de cajas
  entre modos son indicios indirectos de recorte, no la caja real.
- El S1 de R1 en `CLINIC_0002` (calibracion) no tiene revision clinica; en `metal_0008` si.
- Dos casos: no estiman tasas de fallo. Las esferas son sondas a distancia fija (ver E9b).

Lee `data/`, `data/derivados/ts_piloto/`, `r1_landmarks.csv`, `e9b_densidad_s1.csv` y
`e8_componentes.csv`, sin modificarlos.
"""
from __future__ import annotations

import gc
from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd

from e9b_densidad_s1 import ALA_LATERAL_MM, BAJO_PLATILLO_MM, BONE_HU, RADIO_MM
from r1_landmarks import cargar

CASOS = ['dataset7_CLINIC_metal_0008_data', 'dataset6_CLINIC_0002_data']
MODOS = ['robust3mm', 'default6mm']
ESTRUCTURAS = ['sacrum', 'vertebrae_S1', 'hip_left', 'hip_right']
COLORES = {'sacrum': 'tab:orange', 'vertebrae_S1': 'red', 'hip_left': 'cyan', 'hip_right': 'lime'}
MARGEN_MM = 20.0
METAL_HU = 2500
RADIO_TORNILLO_MM = 4.0
VENTANA = (-200, 1200)

Caja = tuple[np.ndarray, np.ndarray]


def mascara(path: Path) -> np.ndarray:
    """Mascara de TS a RAS+ como bool, con la misma reorientacion que `cargar`."""
    img = nib.load(path)
    ornt = nib.orientations.io_orientation(img.affine)
    return nib.orientations.apply_orientation(np.asanyarray(img.dataobj) > 0, ornt)


def caja(m: np.ndarray) -> Caja | None:
    """Indices minimo y maximo por eje de los voxeles activos; None si esta vacia."""
    idx = [np.flatnonzero(m.any(axis=tuple(a for a in range(3) if a != ax))) for ax in range(3)]
    if any(i.size == 0 for i in idx):
        return None
    return np.array([i[0] for i in idx]), np.array([i[-1] for i in idx])


def caras_fov(cj: Caja | None, forma: np.ndarray) -> str:
    """Caras del volumen que toca la mascara (p. ej. 'z+'); vacio si ninguna."""
    if cj is None:
        return ''
    caras = [f'{e}-' for a, e in enumerate('xyz') if cj[0][a] == 0]
    caras += [f'{e}+' for a, e in enumerate('xyz') if cj[1][a] == forma[a] - 1]
    return ','.join(caras)


def esfera_local(forma: np.ndarray, zoom: np.ndarray, off: np.ndarray,
                 centro: np.ndarray) -> tuple[tuple[slice, ...], np.ndarray]:
    """Recorte y mascara de la esfera de E9b en el volumen recortado (mismos voxeles que E9b)."""
    c = centro / zoom - off
    r = np.ceil(RADIO_MM / zoom).astype(int)
    lo = np.maximum(np.floor(c - r).astype(int), 0)
    hi = np.minimum(np.ceil(c + r).astype(int) + 1, forma)
    ii, jj, kk = np.ogrid[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]]
    d2 = ((ii - c[0]) * zoom[0]) ** 2 + ((jj - c[1]) * zoom[1]) ** 2 + ((kk - c[2]) * zoom[2]) ** 2
    return tuple(slice(lo[a], hi[a]) for a in range(3)), d2 <= RADIO_MM ** 2


def eje_tornillo(t: pd.Series) -> tuple[np.ndarray, np.ndarray, float]:
    """Centro (mm), direccion unitaria y longitud de un componente de E8."""
    u = np.array([t['ux'], t['uy'], t['uz']], dtype=float)
    return np.array([t['cx_mm'], t['cy_mm'], t['cz_mm']], dtype=float), u / np.linalg.norm(u), float(t['L_mm'])


def techo_dz(m: np.ndarray, zoom: np.ndarray, off: np.ndarray, platillo: np.ndarray) -> float:
    """z maxima de la mascara en la columna media (x +-5, y +-10 mm) menos el platillo de R1."""
    i0, i1 = (int(round((platillo[0] + s) / zoom[0])) - off[0] for s in (-5.0, 5.0))
    j0, j1 = (int(round((platillo[1] + s) / zoom[1])) - off[1] for s in (-10.0, 10.0))
    col = m[max(i0, 0):max(i1 + 1, 0), max(j0, 0):max(j1 + 1, 0), :]
    ks = np.flatnonzero(col.any(axis=(0, 1))) if col.size else np.array([])
    return round(float((ks[-1] + off[2]) * zoom[2] - platillo[2]), 1) if ks.size else float('nan')


def fraccion(num: np.ndarray, den: np.ndarray) -> float:
    """Fraccion de `den` que tambien esta en `num`; NaN si `den` esta vacio."""
    n = int(den.sum())
    return round(float((num & den).sum()) / n, 3) if n else float('nan')


def main() -> None:
    """Calcula las tablas y laminas del QC del piloto."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    here = Path(__file__).resolve().parent
    root = here.parents[1]
    base_ts = root / 'data' / 'derivados' / 'ts_piloto'
    out_png = here / 'outputs' / 'ts_piloto_qc'
    out_png.mkdir(parents=True, exist_ok=True)
    r1 = pd.read_csv(here / 'r1_landmarks.csv').set_index('Caso')
    e9b = pd.read_csv(here / 'e9b_densidad_s1.csv').set_index('Caso')
    e8 = pd.read_csv(here / 'e8_componentes.csv')
    rutas = {p.name.split('.nii')[0]: p for p in (root / 'data').glob('dataset*/*_data.nii.gz')}
    filas: list[dict] = []
    filas_esf: list[dict] = []
    filas_tor: list[dict] = []
    leyenda = [Line2D([], [], color=c, lw=2, label=e) for e, c in COLORES.items()]
    leyenda.append(Line2D([], [], color='yellow', lw=1, label='esferas E9b (6 mm)'))

    for caso in CASOS:
        print(f'== {caso}', flush=True)
        ref = nib.load(rutas[caso])
        ct, zoom = cargar(rutas[caso])
        zoom = zoom.astype(float)
        forma_full = np.array(ct.shape)
        f = r1.loc[caso]
        platillo = np.array([f['S1_x_mm'], f['S1_y_mm'], f['S1_z_mm']], dtype=float)
        c_esf = platillo - np.array([0.0, 0.0, BAJO_PLATILLO_MM])
        esferas = {n: c_esf + np.array([dx, 0.0, 0.0])
                   for n, dx in (('cuerpo', 0.0), ('ala_izq', -ALA_LATERAL_MM), ('ala_der', ALA_LATERAL_MM))}
        torn = e8[(e8['Caso'] == caso) & (e8['candidato_IS'] == 'si')]

        # Paso 1: cajas sobre el volumen completo (borde del FOV) y rejilla igual a la del CT.
        cajas: dict[tuple[str, str], Caja | None] = {}
        for modo in MODOS:
            for est in ESTRUCTURAS:
                p = base_ts / caso / modo / f'{est}.nii.gz'
                img = nib.load(p)
                if img.shape[:3] != ref.shape[:3] or not np.allclose(img.affine, ref.affine, atol=1e-3):
                    raise ValueError(f'{p}: rejilla distinta de la del CT')
                m = mascara(p)
                cajas[modo, est] = caja(m)
                del m
                gc.collect()

        # Recorte comun: todas las mascaras, esferas y tornillos, mas un margen.
        puntos = [c + s * RADIO_MM for c in esferas.values() for s in (-1.0, 1.0)]
        for _, t in torn.iterrows():
            c, u, L = eje_tornillo(t)
            puntos += [c - (L / 2 + 5) * u, c + (L / 2 + 5) * u]
        pts_idx = np.array(puntos) / zoom
        llenas = [cj for cj in cajas.values() if cj is not None]
        lo = np.minimum(np.min([cj[0] for cj in llenas], axis=0), np.floor(pts_idx.min(0)))
        hi = np.maximum(np.max([cj[1] for cj in llenas], axis=0), np.ceil(pts_idx.max(0)))
        margen = np.ceil(MARGEN_MM / zoom)
        off = np.maximum(lo - margen, 0).astype(int)
        fin = np.minimum(hi + margen + 1, forma_full).astype(int)
        sl = tuple(slice(off[a], fin[a]) for a in range(3))
        sub = np.array(ct[sl])
        del ct
        gc.collect()
        forma = np.array(sub.shape)

        M: dict[tuple[str, str], np.ndarray] = {}
        for modo in MODOS:
            for est in ESTRUCTURAS:
                m = mascara(base_ts / caso / modo / f'{est}.nii.gz')
                M[modo, est] = m[sl].copy()
                del m
                gc.collect()
        union = {modo: np.logical_or.reduce([M[modo, e] for e in ESTRUCTURAS]) for modo in MODOS}
        sacro = {modo: M[modo, 'sacrum'] | M[modo, 'vertebrae_S1'] for modo in MODOS}
        cadera = {modo: M[modo, 'hip_left'] | M[modo, 'hip_right'] for modo in MODOS}

        # 1. Estructuras.
        vox_ml = float(np.prod(zoom)) / 1000.0
        for est in ESTRUCTURAS:
            a, b = M['robust3mm', est], M['default6mm', est]
            na, nb, inter = int(a.sum()), int(b.sum()), int((a & b).sum())
            dice = round(2 * inter / (na + nb), 4) if na + nb else float('nan')
            ca, cb = cajas['robust3mm', est], cajas['default6mm', est]
            dif_caja = (round(float(np.max(np.abs(np.concatenate([(ca[0] - cb[0]) * zoom, (ca[1] - cb[1]) * zoom])))), 1)
                        if ca is not None and cb is not None else float('nan'))
            for modo, m, n, otro in (('robust3mm', a, na, b), ('default6mm', b, nb, a)):
                otras = np.logical_or.reduce([M[modo, e] for e in ESTRUCTURAS if e != est])
                hu = sub[m]
                cj = cajas[modo, est]
                fila = {'Caso': caso, 'modo': modo, 'estructura': est, 'n_vox': n,
                        'vol_ml': round(n * vox_ml, 1), 'toca_fov': caras_fov(cj, forma_full)}
                for e_i, eje in enumerate('xyz'):
                    fila[f'{eje}_min_mm'] = round(float(cj[0][e_i] * zoom[e_i]), 1) if cj else float('nan')
                    fila[f'{eje}_max_mm'] = round(float(cj[1][e_i] * zoom[e_i]), 1) if cj else float('nan')
                fila.update({
                    'hu_p50': float(np.median(hu)) if n else float('nan'),
                    'frac_bajo150': round(float((hu <= BONE_HU).mean()), 3) if n else float('nan'),
                    'solape_otras_vox': int((m & otras).sum()),
                    'techo_linea_media_dz_mm': (techo_dz(m, zoom, off, platillo)
                                                if est in ('sacrum', 'vertebrae_S1') else float('nan')),
                    'dice_3v6': dice,
                    'solo_este_modo_vox': int((m & ~otro).sum()),
                    'dif_caja_3v6_max_mm': dif_caja,
                })
                filas.append(fila)
                del otras, hu
        gc.collect()

        # 2. Esferas de E9b.
        for nombre, centro in esferas.items():
            s_sl, dentro = esfera_local(forma, zoom, off, centro)
            v = sub[s_sl][dentro]
            bajo = v <= BONE_HU
            ref_hu = e9b.loc[caso, f'hu_{nombre}'] if caso in e9b.index else float('nan')
            for modo in MODOS:
                en_sacro = sacro[modo][s_sl][dentro]
                en_cadera = cadera[modo][s_sl][dentro]
                filas_esf.append({
                    'Caso': caso, 'esfera': nombre, 'modo': modo, 'n_vox': int(v.size),
                    'hu_p50': float(np.median(v)), 'hu_p50_e9b': ref_hu,
                    'control_marco_ok': bool(abs(float(np.median(v)) - ref_hu) <= 1.0),
                    'frac_sobre150': round(float((~bajo).mean()), 3),
                    'frac_en_sacro_S1': round(float(en_sacro.mean()), 3),
                    'frac_en_cadera': round(float(en_cadera.mean()), 3),
                    'frac_fuera_mascaras': round(float((~(en_sacro | en_cadera)).mean()), 3),
                    'frac_bajo150_recuperada_sacro_S1': fraccion(en_sacro, bajo),
                })

        # 3. Tornillos de E8.
        for _, t in torn.iterrows():
            c, u, L = eje_tornillo(t)
            pts = c[None, :] + np.arange(-L / 2, L / 2 + 1e-6, 1.0)[:, None] * u[None, :]
            idx = np.rint(pts / zoom).astype(int) - off
            idx = idx[np.all((idx >= 0) & (idx < forma), axis=1)]
            hu_eje = sub[idx[:, 0], idx[:, 1], idx[:, 2]]
            c_lo = np.maximum(np.floor((np.minimum(pts.min(0), pts.max(0)) - RADIO_TORNILLO_MM) / zoom).astype(int) - off, 0)
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

        # 4. Laminas.
        def ext(p: int, q: int) -> tuple[float, float, float, float]:
            return (off[p] * zoom[p], (off[p] + forma[p]) * zoom[p],
                    off[q] * zoom[q], (off[q] + forma[q]) * zoom[q])

        k = int(np.clip(round(c_esf[2] / zoom[2]) - off[2], 0, forma[2] - 1))
        j = int(np.clip(round(platillo[1] / zoom[1]) - off[1], 0, forma[1] - 1))
        i = int(np.clip(round(platillo[0] / zoom[0]) - off[0], 0, forma[0] - 1))
        cortes = [
            (f'axial z={c_esf[2]:.0f} mm', lambda a: a[:, :, k], (0, 1), 'x (-> derecha)', 'y (-> anterior)'),
            (f'coronal y={platillo[1]:.0f} mm', lambda a: a[:, j, :], (0, 2), 'x (-> derecha)', 'z (-> craneal)'),
            (f'sagital x={platillo[0]:.0f} mm', lambda a: a[i, :, :], (1, 2), 'y (-> anterior)', 'z (-> craneal)'),
        ]
        fig, ejes = plt.subplots(3, 3, figsize=(16, 14))
        for col, (titulo, corte, (p, q), xl, yl) in enumerate(cortes):
            e = ext(p, q)
            base = np.clip(corte(sub), *VENTANA).T
            for fil, modo in enumerate(MODOS + ['diferencia']):
                ax = ejes[fil, col]
                ax.imshow(base, cmap='gray', origin='lower', extent=e)
                if modo == 'diferencia':
                    u3, u6 = corte(union['robust3mm']).T, corte(union['default6mm']).T
                    rgba = np.zeros(u3.shape + (4,))
                    rgba[u3 & ~u6] = (1.0, 0.0, 0.0, 1.0)
                    rgba[u6 & ~u3] = (0.0, 0.5, 1.0, 1.0)
                    ax.imshow(rgba, origin='lower', extent=e, interpolation='nearest')
                    ax.set_title(f'{titulo} | rojo solo 3 mm: {int((u3 & ~u6).sum())} vox, '
                                 f'azul solo 6 mm: {int((u6 & ~u3).sum())} vox', fontsize=9)
                else:
                    for est in ESTRUCTURAS:
                        m2 = corte(M[modo, est]).T
                        if m2.any():
                            ax.contour(m2.astype(np.uint8), levels=[0.5], colors=COLORES[est],
                                       linewidths=0.9, extent=e, origin='lower')
                    ax.set_title(f'{modo} | {titulo}', fontsize=9)
                for centro in esferas.values():
                    if (p, q) == (1, 2) and abs(centro[0] - platillo[0]) > 1e-6:
                        continue
                    ax.add_patch(plt.Circle((centro[p], centro[q]), RADIO_MM, fill=False, ec='yellow', lw=0.8))
                ax.set_xlabel(f'{xl} mm', fontsize=8)
                ax.set_ylabel(f'{yl} mm', fontsize=8)
                ax.tick_params(labelsize=7)
        fig.legend(handles=leyenda, loc='lower center', ncol=5, fontsize=10)
        fig.suptitle(f'{caso}: contornos TS por recorte; fila 3 = diferencia de la union de las 4 mascaras',
                     fontsize=12)
        fig.tight_layout(rect=(0, 0.03, 1, 0.97))
        destino = out_png / f'{caso}_planos.png'
        fig.savefig(destino, dpi=80)
        plt.close(fig)
        print(f'Escrito {destino}', flush=True)

        if len(torn):
            fig, ejes = plt.subplots(len(torn), 2, figsize=(14, 5 * len(torn)), squeeze=False)
            for fil, (_, t) in enumerate(torn.iterrows()):
                c, u, L = eje_tornillo(t)
                kt = int(np.clip(round(c[2] / zoom[2]) - off[2], 0, forma[2] - 1))
                e = ext(0, 1)
                for col, modo in enumerate(MODOS):
                    ax = ejes[fil, col]
                    ax.imshow(np.clip(sub[:, :, kt], *VENTANA).T, cmap='gray', origin='lower', extent=e)
                    for est in ESTRUCTURAS:
                        m2 = M[modo, est][:, :, kt].T
                        if m2.any():
                            ax.contour(m2.astype(np.uint8), levels=[0.5], colors=COLORES[est],
                                       linewidths=0.9, extent=e, origin='lower')
                    a0, a1 = c - L / 2 * u, c + L / 2 * u
                    ax.plot([a0[0], a1[0]], [a0[1], a1[1]], color='magenta', lw=0.8, ls='--')
                    ax.set_xlim(c[0] - L / 2 - 25, c[0] + L / 2 + 25)
                    ax.set_ylim(c[1] - 45, c[1] + 45)
                    ax.set_title(f'comp {int(t["comp"])} | {modo} | axial z={c[2]:.0f} mm; '
                                 f'magenta = eje E8', fontsize=9)
                    ax.set_xlabel('x (-> derecha) mm', fontsize=8)
                    ax.set_ylabel('y (-> anterior) mm', fontsize=8)
            fig.legend(handles=leyenda[:-1], loc='lower center', ncol=4, fontsize=10)
            fig.tight_layout(rect=(0, 0.03, 1, 1))
            destino = out_png / f'{caso}_tornillos.png'
            fig.savefig(destino, dpi=80)
            plt.close(fig)
            print(f'Escrito {destino}', flush=True)

        del sub, M, union, sacro, cadera
        gc.collect()

    for nombre, datos in (('ts_piloto_qc.csv', filas), ('ts_piloto_qc_esferas.csv', filas_esf),
                          ('ts_piloto_qc_tornillos.csv', filas_tor)):
        df = pd.DataFrame(datos)
        df.to_csv(here / nombre, index=False)
        print(f'\n{nombre}\n{df.to_string(index=False)}', flush=True)


if __name__ == '__main__':
    main()
