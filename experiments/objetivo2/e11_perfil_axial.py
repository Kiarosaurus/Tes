"""E11 / implicancia #97 — perfil de diametro a lo largo del eje de los implantes reales.

POR QUE
-------
El Objetivo 3 condiciona la generacion por una MASCARA del implante. La mascara de sintesis es
parametrica; la de entrenamiento sale de umbralizar metal real. E8 midio **un** diametro por
componente (`d_ext_2500_mm`, mediana 5.00 mm) y las fuentes leidas el 2026-09-19 dan fuste
4.8-4.9 mm, rosca 7.3 mm en los 16/32 mm distales y cabeza 8.0 mm (#97). Lo que falta saber es si
esa estructura **se ve** en el CT o si el volumen parcial la promedia: E8 no lo puede decir porque
no mide la variacion a lo largo del eje.

QUE MIDE
--------
Para cada componente metalico **esbelto** (HU > 2500, longitud >= `--min-largo` y los dos anchos
transversales <= `--max-ancho`, que es lo que deja fuera placas y protesis), su eje principal por
PCA y, en tramos de `--paso` mm a lo largo de ese eje, el **diametro exterior local**: 2 x p95 de la
distancia al eje, el mismo estimador radial de E8 (robusto a canulacion y a fragmentos).

QUE NO MIDE, Y HAY QUE DECLARARLO
---------------------------------
- No identifica cabeza ni rosca: reporta los dos extremos (`A` = t bajo, `B` = t alto) y el centro.
  Cual es la cabeza se decide mirando cual extremo es mas ancho y donde cae respecto al hueso.
- No separa tipos de implante: en la cohorte hay placas y protesis, no solo tornillos. El filtro es
  geometrico (alargado), como en E8.
- El umbral fijo de 2500 HU es el de cribado (#22). El perfil con semimaximo local queda fuera.

SALIDA (`--out`)
----------------
`e11_perfil_axial.csv` (una fila por tramo), `e11_componentes.csv` (una fila por componente, con los
diametros de extremo y centro) y `e11_perfil_axial.md`. Solo lee `data/`.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from scipy import ndimage as ndi

from e8_censo_implantes import METAL_HU, MIN_FRAG_MM3, pca_extension
from r1_landmarks import cargar

PASO_MM = 2.0
MIN_LARGO_MM = 30.0
MAX_ANCHO_MM = 12.0  # deja fuera placas y protesis: un tornillo de 7.3 mm no llega a esto
MIN_VOX_TRAMO = 10
FRAC_EXTREMO = 0.15  # fraccion del largo que cuenta como "extremo"


def perfil(pts_mm: np.ndarray, centro: np.ndarray, u: np.ndarray, paso: float) -> list[dict]:
    """Diametro exterior local (2 x p95 del radio) por tramo de `paso` mm a lo largo del eje."""
    rel = pts_mm - centro
    t = rel @ u
    r = np.linalg.norm(rel - np.outer(t, u), axis=1)
    t0, t1 = float(np.percentile(t, 0.5)), float(np.percentile(t, 99.5))
    filas = []
    for b in np.arange(t0, t1, paso):
        sel = (t >= b) & (t < b + paso)
        n = int(sel.sum())
        if n < MIN_VOX_TRAMO:
            continue
        filas.append({'t_mm': round(float(b - t0 + paso / 2), 2), 'n_vox': n,
                      'd_mm': round(2.0 * float(np.percentile(r[sel], 95)), 3)})
    return filas


def resumen_componente(filas: list[dict], largo: float) -> dict:
    """Diametros medianos en extremo A, centro y extremo B, y el maximo del perfil."""
    if not filas:
        return {}
    t = np.array([f['t_mm'] for f in filas])
    d = np.array([f['d_mm'] for f in filas])
    corte = FRAC_EXTREMO * largo
    a, b = t <= corte, t >= largo - corte
    medio = ~a & ~b
    def med(m):
        return round(float(np.median(d[m])), 2) if m.any() else float('nan')
    return {'d_extremo_A_mm': med(a), 'd_centro_mm': med(medio), 'd_extremo_B_mm': med(b),
            'd_max_mm': round(float(d.max()), 2), 'n_tramos': len(filas)}


def analizar(path: Path, paso: float, min_largo: float, max_ancho: float) -> tuple[list[dict], list[dict]]:
    """Perfil de cada componente esbelto de un volumen."""
    arr, zoom = cargar(path)
    caso = path.name.split('.nii')[0]
    metal = arr > METAL_HU
    if not metal.any():
        return [], [{'Caso': caso, 'comp': 0, 'clase': 'sin metal'}]
    idx = np.argwhere(metal)
    lo, hi = idx.min(0), idx.max(0) + 1
    del idx
    crop = metal[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]]
    del metal
    lab, n = ndi.label(crop, structure=np.ones((3, 3, 3)), output=np.int32)
    vox_mm3 = float(np.prod(zoom))
    tramos, comps = [], []
    for c in range(1, n + 1):
        pts = np.argwhere(lab == c)
        if pts.shape[0] * vox_mm3 < MIN_FRAG_MM3:
            continue
        pts_mm = (pts + lo).astype(np.float32) * zoom
        centro, vt, ext = pca_extension(pts_mm)
        largo = float(ext[0])
        if largo < min_largo or float(ext[1]) > max_ancho or float(ext[2]) > max_ancho:
            continue
        fp = perfil(pts_mm, centro, vt[0], paso)
        fila = {'Caso': caso, 'comp': c, 'clase': 'esbelto', 'L_mm': round(largo, 2),
                'W2_mm': round(float(ext[1]), 2), 'W3_mm': round(float(ext[2]), 2),
                'n_vox': int(pts.shape[0]), 'vol_mm3': round(pts.shape[0] * vox_mm3, 1),
                'hu_max': round(float(arr[tuple((pts + lo).T)].max()), 0)}
        fila.update(resumen_componente(fp, largo))
        comps.append(fila)
        for f in fp:
            tramos.append({'Caso': caso, 'comp': c, **f})
    return tramos, comps


def informe(comps: list[dict], out: Path, paso: float, min_largo: float, max_ancho: float) -> None:
    """Resumen: cuantos componentes muestran un extremo mas ancho que el centro."""
    import pandas as pd

    d = pd.DataFrame([c for c in comps if c.get('clase') == 'esbelto'])
    L = ['# E11 — perfil de diametro a lo largo del eje (implicancia #97)', '',
         f'Componentes esbeltos (HU > {METAL_HU:.0f}, largo >= {min_largo:.0f} mm, anchos <= {max_ancho:.0f} mm): '
         f'{len(d)}; tramos de {paso:.0f} mm; diametro = 2 x p95 del radio, como en E8. El filtro de ancho deja '
         'fuera placas y protesis.', '',
         'El perfil NO identifica cabeza ni rosca: `A` y `B` son los dos extremos del eje principal.', '']
    if d.empty:
        L.append('Sin componentes esbeltos.')
    else:
        anchos = np.maximum(d['d_extremo_A_mm'], d['d_extremo_B_mm']) - d['d_centro_mm']
        L += ['| Magnitud | mediana | p10 | p90 |', '|---|---|---|---|']
        for col in ('d_centro_mm', 'd_extremo_A_mm', 'd_extremo_B_mm', 'd_max_mm', 'L_mm'):
            v = d[col].dropna()
            L.append(f'| {col} | {v.median():.2f} | {v.quantile(0.1):.2f} | {v.quantile(0.9):.2f} |')
        L += ['', f'| Extremo mas ancho que el centro | mediana {anchos.median():.2f} mm | '
                  f'{int((anchos > 1.0).sum())}/{len(d)} superan 1.0 mm | '
                  f'{int((anchos > 2.0).sum())}/{len(d)} superan 2.0 mm |', '',
              '**Lectura (la decide la autora):** si un extremo supera el centro por ~2 mm, el CT esta '
              'resolviendo cabeza (8.0 mm) o rosca (7.3 mm) frente a un cuerpo de ~5 mm, y la mascara '
              'parametrica debe tener esas piezas. Si la diferencia es menor que un voxel, el volumen '
              'parcial las promedia y el cilindro uniforme queda justificado.', '']
    (out / 'e11_perfil_axial.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'Escrito {out / "e11_perfil_axial.md"}', flush=True)


def main() -> None:
    """Recorre los CT con metal y escribe perfil y resumen."""
    aqui = Path(__file__).resolve().parent
    raiz = aqui.parents[1]
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--data', type=Path, default=raiz / 'data')
    p.add_argument('--out', type=Path, default=aqui)
    p.add_argument('--paso', type=float, default=PASO_MM)
    p.add_argument('--min-largo', type=float, default=MIN_LARGO_MM)
    p.add_argument('--max-ancho', type=float, default=MAX_ANCHO_MM)
    p.add_argument('--casos', nargs='*', default=None)
    p.add_argument('--max', type=int, default=None)
    args = p.parse_args()

    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    paths = sorted(args.data.expanduser().rglob('*_data.nii*'))
    if args.casos:
        paths = [q for q in paths if q.name.split('.nii')[0] in set(args.casos)]
    if args.max:
        paths = paths[:args.max]
    if not paths:
        raise SystemExit('No se encontraron CT *_data.nii[.gz]. No se escribio nada.')

    tramos, comps = [], []
    for i, path in enumerate(paths, 1):
        try:
            t, c = analizar(path, args.paso, args.min_largo, args.max_ancho)
        except Exception as exc:  # un volumen roto no detiene la cohorte
            comps.append({'Caso': path.name.split('.nii')[0], 'comp': -1, 'clase': f'ERROR {exc}'})
            print(f'{path.name}: ERROR {exc}', flush=True)
            continue
        tramos += t
        comps += c
        alargados = [x for x in c if x.get('clase') == 'esbelto']
        print(f'{i}/{len(paths)} {path.name.split(".nii")[0]}: {len(alargados)} esbeltos'
              + (f' | centro {alargados[0].get("d_centro_mm")} extremos '
                 f'{alargados[0].get("d_extremo_A_mm")}/{alargados[0].get("d_extremo_B_mm")}' if alargados else ''),
              flush=True)

    campos_t = ['Caso', 'comp', 't_mm', 'n_vox', 'd_mm']
    campos_c = ['Caso', 'comp', 'clase', 'L_mm', 'W2_mm', 'W3_mm', 'n_vox', 'vol_mm3', 'hu_max',
                'd_centro_mm', 'd_extremo_A_mm', 'd_extremo_B_mm', 'd_max_mm', 'n_tramos']
    for nombre, campos, filas in (('e11_perfil_axial.csv', campos_t, tramos),
                                  ('e11_componentes.csv', campos_c, comps)):
        with (out / nombre).open('w', encoding='utf-8', newline='') as h:
            w = csv.DictWriter(h, fieldnames=campos, extrasaction='ignore')
            w.writeheader()
            w.writerows(filas)
    informe(comps, out, args.paso, args.min_largo, args.max_ancho)


if __name__ == '__main__':
    main()
