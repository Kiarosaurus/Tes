"""E8 / implicancias #41 y #13 — censo morfologico del metal en dataset7 (CLINIC-metal).

POR QUE
-------
#41: C1 no tiene insumo de geometrias. La via (a) propone extraerlas de los implantes de los
75 CLINIC-metal, pero nadie ha medido que hay dentro: `revision.csv` solo dice "material
ortopedico" (regla de la autora, no observacion por volumen, #37) y la ubicacion la
propusieron agentes desde laminas. #13 dejo pendiente "mirar los volumenes para saber que
metal contienen". Este script no decide #41: mide dos cosas que la decision necesita.

1. **Que formas hay.** Componentes conexas de HU > 2500 dentro del cuerpo, con extension
   por PCA: longitud (eje 1), anchos (ejes 2 y 3), volumen.
2. **Cuanto depende la geometria del umbral.** Para cada objeto alargado: diametro por
   volumen / longitud a HU > 2500 (`d_eq`, se hunde con implantes canulados), diametro
   exterior radial a HU > 2500 (`d_ext_2500`) y el mismo con umbral de **semimaximo local**
   (fondo del casquete 3-6 mm + mitad de la diferencia hasta el p95 del objeto,
   `d_ext_semimax`). Si la via (a) se adopta, la diferencia entre ellos es la incertidumbre
   con la que naceria el banco.

Los objetos se forman **fusionando fragmentos colineales** de HU > 2500: en el piloto un
mismo tornillo salia partido en 2 piezas (`metal_0008`, `metal_0000`). `n_fragmentos` lo
registra; que un objeto se parta ya es un dato sobre la via (a).

CLASES MORFOLOGICAS (descriptivas, NO tipos de implante)
-------------------------------------------------------
- `alargado`: L >= 30 mm, L / W2 >= 4 y W2 <= 15 mm (tornillo, aguja, varilla).
- `laminar`: L >= 30 mm, W2 / W3 >= 2.5 y W3 <= 8 mm (placa).
- `masivo`: volumen >= 15 000 mm3 (protesis, cemento, conglomerado).
- `otro`: el resto (incluye componentes fusionados tornillo+placa).

CANDIDATO A TORNILLO ILIOSACRO / TRANSSACRO (propuesta de script, sin validar)
-----------------------------------------------------------------------------
`alargado` con eje principal |u_x| >= cos(40 grados) (sobre todo izquierda-derecha), centroide
entre 70 mm bajo y 15 mm sobre el platillo de S1 de R1, a menos de 60 mm por detras y 20 mm
por delante de ese punto, y que llegue a menos de 30 mm del plano medio. Requiere que R1
haya localizado S1 en el volumen. Es un filtro geometrico: la lamina de QC es la prueba.

Lee `data/dataset7` y `r1_landmarks.csv`. Escribe `e8_componentes.csv` (una fila por
componente) y laminas en `outputs/e8_qc/` (ignorado por git).
"""
from __future__ import annotations

import argparse
import csv
import gc
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import ndimage as ndi

METAL_HU = 2500.0
BODY_HU = -400.0
MIN_MM3 = 50.0
MIN_FRAG_MM3 = 10.0
CASQUETE_MM = (3.0, 6.0)


from r1_landmarks import cargar  # misma carga y mismas coordenadas RAS+ en mm que R1


def cuerpo_reducido(arr: np.ndarray, f: int = 4) -> np.ndarray:
    """Mascara de cuerpo gruesa (paso f), rellena corte a corte. Solo para dentro/fuera."""
    crudo = np.asarray(arr[::f, ::f, ::f]) > BODY_HU
    lab, n = ndi.label(crudo)
    if n == 0:
        return np.ones_like(crudo)
    body = lab == (int(np.argmax(ndi.sum(crudo, lab, range(1, n + 1)))) + 1)
    for k in range(body.shape[2]):
        body[:, :, k] = ndi.binary_fill_holes(body[:, :, k])
    return body


def pca_extension(pts_mm: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Ejes principales y extension (p0.5-p99.5) a lo largo de cada uno."""
    centro = pts_mm.mean(0)
    x = pts_mm - centro
    if len(x) > 50_000:
        x_fit = x[np.linspace(0, len(x) - 1, 50_000).astype(int)]
    else:
        x_fit = x
    _, _, vt = np.linalg.svd(x_fit, full_matrices=False)
    proy = x @ vt.T
    ext = np.percentile(proy, 99.5, axis=0) - np.percentile(proy, 0.5, axis=0)
    return centro, vt, ext


def diametro_radial(pts_mm: np.ndarray, centro: np.ndarray, u: np.ndarray) -> float:
    """Diametro exterior: 2 x mediana, por tramos de 5 mm del eje, del p95 de la distancia al eje.

    Se descarta el 10% de cada extremo (cabeza, punta). A diferencia del diametro por
    volumen / longitud, no se hunde con implantes canulados (huecos) ni con fragmentos.
    """
    rel = pts_mm - centro
    t = rel @ u
    r = np.linalg.norm(rel - np.outer(t, u), axis=1)
    t0, t1 = np.percentile(t, 0.5), np.percentile(t, 99.5)
    margen = 0.1 * (t1 - t0)
    vals = []
    for b in np.arange(t0 + margen, t1 - margen, 5.0):
        sel = (t >= b) & (t < b + 5.0)
        if sel.sum() >= 10:
            vals.append(np.percentile(r[sel], 95))
    return 2.0 * float(np.median(vals)) if vals else float('nan')


def semimaximo(arr: np.ndarray, idx: np.ndarray, zoom: np.ndarray, centro: np.ndarray,
               u: np.ndarray) -> tuple[float, float, float]:
    """Diametro exterior a umbral de semimaximo local, y los niveles de fondo y umbral."""
    pad = int(np.ceil(CASQUETE_MM[1] / zoom.min())) + 1
    a0 = np.maximum(idx.min(0) - pad, 0)
    a1 = np.minimum(idx.max(0) + 1 + pad, arr.shape)
    sub = np.asarray(arr[a0[0]:a1[0], a0[1]:a1[1], a0[2]:a1[2]]).astype(np.float32)
    m = np.zeros(sub.shape, dtype=bool)
    m[tuple((idx - a0).T)] = True
    dist = ndi.distance_transform_edt(~m, sampling=zoom)
    casquete = (dist >= CASQUETE_MM[0]) & (dist <= CASQUETE_MM[1]) & (sub < METAL_HU)
    if not casquete.any():
        return float('nan'), float('nan'), float('nan')
    fondo = float(np.median(sub[casquete]))
    pico = float(np.percentile(sub[m], 95))
    umbral = fondo + (pico - fondo) / 2.0
    # Voxeles del grupo o de su vecindad inmediata (<= 3 mm) sobre el umbral.
    nucleo = np.argwhere((sub >= umbral) & (dist <= CASQUETE_MM[0]))
    if len(nucleo) < 10:
        return float('nan'), fondo, umbral
    return diametro_radial((nucleo + a0).astype(np.float32) * zoom, centro, u), fondo, umbral


def fusionar(frags: list[dict]) -> list[list[int]]:
    """Agrupa fragmentos colineales de un mismo objeto (union-find).

    Con HU > 2500 un tornillo de baja densidad o canulado se parte en piezas (piloto:
    `metal_0008`, `metal_0000`). Dos fragmentos se unen si sus ejes difieren < 15 grados, el
    centroide de cada uno esta a <= 5 mm de la recta del otro y el hueco entre sus extremos a
    lo largo del eje es <= 20 mm. Solo fragmentos con L / W2 >= 2 (no se unen manchas).
    """
    padre = list(range(len(frags)))

    def raiz(i: int) -> int:
        while padre[i] != i:
            padre[i] = padre[padre[i]]
            i = padre[i]
        return i

    lin = [i for i, f in enumerate(frags) if f['ext'][1] > 0 and f['ext'][0] / f['ext'][1] >= 2]
    cos_max = np.cos(np.deg2rad(15.0))
    for a in range(len(lin)):
        for b in range(a + 1, len(lin)):
            fi, fj = frags[lin[a]], frags[lin[b]]
            ui, uj = fi['vt'][0], fj['vt'][0]
            if abs(float(ui @ uj)) < cos_max:
                continue
            d = fj['centro'] - fi['centro']
            ti = float(d @ ui)
            if (np.linalg.norm(d - ti * ui) > 5.0
                    or np.linalg.norm(d - float(d @ uj) * uj) > 5.0):
                continue
            hueco = abs(ti) - fi['ext'][0] / 2.0 - fj['ext'][0] / 2.0
            if hueco <= 20.0:
                padre[raiz(lin[a])] = raiz(lin[b])
    grupos: dict[int, list[int]] = {}
    for i in range(len(frags)):
        grupos.setdefault(raiz(i), []).append(i)
    return list(grupos.values())


def lamina(arr: np.ndarray, zoom: np.ndarray, filas: list[dict], destino: Path,
           titulo: str, s1: np.ndarray | None) -> None:
    """MIP axial y coronal del metal sobre MIP oseo, con candidatos numerados."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    step = 2
    sub = np.asarray(arr[::step, ::step, ::step])
    z = zoom * step
    fig, ejes = plt.subplots(1, 2, figsize=(14, 7))
    for ax, eje, (h, v), nombre in ((ejes[0], 2, (0, 1), 'axial (MIP en z)'),
                                     (ejes[1], 1, (0, 2), 'coronal (MIP en y)')):
        mip = np.clip(sub, -200, 3000).max(axis=eje).T
        ax.imshow(mip, cmap='gray', origin='lower', vmin=0, vmax=3000,
                  extent=(0, mip.shape[1] * z[h], 0, mip.shape[0] * z[v]))
        for f in filas:
            color = 'red' if f['candidato_IS'] == 'si' else (
                'yellow' if f['clase'] == 'alargado' else 'cyan')
            ax.text(f['cx_mm'] if h == 0 else f['cy_mm'], f['cy_mm'] if v == 1 else f['cz_mm'],
                    str(f['comp']), color=color, fontsize=8, weight='bold')
        if s1 is not None:
            ax.plot(s1[h], s1[v], 'g+', ms=14, mew=2)
        ax.set_title(nombre, fontsize=9)
    fig.suptitle(titulo + '  (rojo = candidato IS; amarillo = alargado; cian = otro;'
                 ' cruz verde = S1 de R1)', fontsize=9)
    fig.tight_layout()
    fig.savefig(destino, dpi=70)
    plt.close(fig)


def analizar(path: Path, r1: pd.Series | None, qc_dir: Path | None) -> list[dict]:
    """Una fila por componente metalico de un volumen."""
    arr, zoom = cargar(path)
    caso = path.name.split('.nii')[0]
    metal = arr > METAL_HU
    if not metal.any():
        return [{'Caso': caso, 'comp': 0, 'clase': 'sin metal'}]
    idx = np.argwhere(metal)
    lo, hi = idx.min(0), idx.max(0) + 1
    del idx
    crop = metal[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]]
    del metal
    lab, n = ndi.label(crop, structure=np.ones((3, 3, 3)), output=np.int32)
    objetos = ndi.find_objects(lab)
    body = cuerpo_reducido(arr)
    x_mid = s1 = None
    if r1 is not None and r1.get('S1_hallado') == 'si':
        s1 = np.array([r1['S1_x_mm'], r1['S1_y_mm'], r1['S1_z_mm']], dtype=np.float32)
        x_mid = float(r1['x_mid'])

    vox_mm3 = float(np.prod(zoom))
    frags: list[dict] = []
    for c, sl in enumerate(objetos, start=1):
        if sl is None:
            continue
        comp = lab[sl] == c
        if comp.sum() * vox_mm3 < MIN_FRAG_MM3:
            continue
        idx_c = np.argwhere(comp) + lo + np.array([s.start for s in sl])
        centro, vt, ext = pca_extension(idx_c.astype(np.float32) * zoom)
        frags.append({'idx': idx_c, 'centro': centro, 'vt': vt, 'ext': ext})
    del lab, crop

    filas: list[dict] = []
    for grupo in fusionar(frags):
        idx_g = np.concatenate([frags[i]['idx'] for i in grupo])
        vol = len(idx_g) * vox_mm3
        if vol < MIN_MM3:
            continue
        pts = idx_g.astype(np.float32) * zoom
        centro, vt, ext = pca_extension(pts)
        bi = np.minimum(idx_g // 4, np.array(body.shape) - 1)
        dentro = float(body[bi[:, 0], bi[:, 1], bi[:, 2]].mean())
        hu = np.asarray(arr[idx_g[:, 0], idx_g[:, 1], idx_g[:, 2]])
        L, W2, W3 = (float(e) for e in ext)
        if vol >= 15000:
            clase = 'masivo'
        elif L >= 30 and W2 > 0 and L / W2 >= 4 and W2 <= 15:
            clase = 'alargado'
        elif L >= 30 and W3 > 0 and W2 / W3 >= 2.5 and W3 <= 8:
            clase = 'laminar'
        else:
            clase = 'otro'
        fila = {'Caso': caso, 'comp': len(filas) + 1, 'clase': clase,
                'n_fragmentos': len(grupo),
                'vol_mm3': round(vol, 1), 'L_mm': round(L, 1), 'W2_mm': round(W2, 1),
                'W3_mm': round(W3, 1), 'ux': round(float(vt[0, 0]), 3),
                'uy': round(float(vt[0, 1]), 3), 'uz': round(float(vt[0, 2]), 3),
                'cx_mm': round(float(centro[0]), 1), 'cy_mm': round(float(centro[1]), 1),
                'cz_mm': round(float(centro[2]), 1), 'frac_dentro_cuerpo': round(dentro, 3),
                'hu_p50': int(np.median(hu)), 'hu_max': int(hu.max()),
                'candidato_IS': 'no'}
        if clase == 'alargado':
            fila['d_eq_2500_mm'] = round(2.0 * np.sqrt(vol / (np.pi * L)), 2)
            fila['d_ext_2500_mm'] = round(diametro_radial(pts, centro, vt[0]), 2)
            d_sm, fondo, umbral = semimaximo(arr, idx_g, zoom, centro, vt[0])
            fila['d_ext_semimax_mm'] = round(d_sm, 2)
            fila['hu_fondo'] = round(fondo, 0)
            fila['hu_umbral_semimax'] = round(umbral, 0)
            if s1 is not None and dentro >= 0.5:
                dz = centro[2] - s1[2]
                dy = centro[1] - s1[1]
                llega = float(np.min(np.abs(pts[:, 0] - x_mid)))
                if (abs(vt[0, 0]) >= np.cos(np.deg2rad(40)) and -70 <= dz <= 15
                        and -60 <= dy <= 20 and llega <= 30):
                    fila['candidato_IS'] = 'si'
            if s1 is not None:
                fila['dz_S1_mm'] = round(float(centro[2] - s1[2]), 1)
                fila['dy_S1_mm'] = round(float(centro[1] - s1[1]), 1)
        filas.append(fila)
        del idx_g, pts, hu
    if qc_dir is not None and filas:
        lamina(arr, zoom, filas, qc_dir / f'{caso}.png',
               f'{caso}: {sum(f["candidato_IS"] == "si" for f in filas)} candidatos IS', s1)
    return filas


def main() -> None:
    """Punto de entrada de linea de comandos."""
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--data', type=Path, default=root / 'data' / 'dataset7')
    parser.add_argument('--r1', type=Path, default=here / 'r1_landmarks.csv')
    parser.add_argument('--out', type=Path, default=here)
    parser.add_argument('--casos', nargs='*')
    parser.add_argument('--patron', default='*_data.nii*')
    parser.add_argument('--no-qc', action='store_true')
    parser.add_argument('--max', type=int, default=None, help='lote de N volumenes nuevos')
    args = parser.parse_args()

    r1 = pd.read_csv(args.r1).set_index('Caso') if args.r1.exists() else None
    paths = sorted(args.data.glob(args.patron))
    if args.casos:
        paths = [p for p in paths if any(c in p.name for c in args.casos)]
    qc_dir = None if args.no_qc else args.out / 'outputs' / 'e8_qc'
    if qc_dir is not None:
        qc_dir.mkdir(parents=True, exist_ok=True)

    campos = ['Caso', 'comp', 'clase', 'n_fragmentos', 'vol_mm3', 'L_mm', 'W2_mm', 'W3_mm',
              'ux', 'uy', 'uz', 'cx_mm', 'cy_mm', 'cz_mm', 'frac_dentro_cuerpo', 'hu_p50',
              'hu_max', 'd_eq_2500_mm', 'd_ext_2500_mm', 'd_ext_semimax_mm', 'hu_fondo',
              'hu_umbral_semimax',
              'dz_S1_mm', 'dy_S1_mm', 'candidato_IS', 'Error']
    destino = args.out / 'e8_componentes.csv'
    hechos: set[str] = set()
    if destino.exists():
        hechos = set(pd.read_csv(destino, usecols=['Caso'])['Caso'])
        print(f'Reanudando: {len(hechos)} volumenes ya en {destino.name}.')
    nuevos = 0
    with destino.open('a' if hechos else 'w', encoding='utf-8', newline='') as handle:
        w = csv.DictWriter(handle, fieldnames=campos, extrasaction='ignore')
        if not hechos:
            w.writeheader()
        for i, path in enumerate(paths):
            caso = path.name.split('.nii')[0]
            if caso in hechos:
                continue
            if args.max is not None and nuevos >= args.max:
                break
            nuevos += 1
            fila_r1 = r1.loc[caso] if (r1 is not None and caso in r1.index) else None
            try:
                filas = analizar(path, fila_r1, qc_dir)
            except Exception as exc:  # noqa: BLE001 - se registra y se sigue
                filas = [{'Caso': caso, 'Error': f'{type(exc).__name__}: {exc}'}]
            w.writerows(filas)
            handle.flush()
            gc.collect()
            print(f'{i + 1}/{len(paths)} {caso}: {len(filas)} componentes, '
                  f'{sum(f.get("candidato_IS") == "si" for f in filas)} candidatos IS',
                  flush=True)
    print(f'Escrito {destino}.')


if __name__ == '__main__':
    main()
