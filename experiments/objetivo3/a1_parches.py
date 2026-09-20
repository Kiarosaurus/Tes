"""A1 / Diseno A — extraccion de parches 2.5D alrededor del metal real, para el renderizador.

POR QUE
-------
El Objetivo 3 se redisena como inpainting en el espacio de la imagen (`01-decisiones.md`, 2026-09-19;
`experiments/objetivo3/diseno_A.md`). El modelo se entrena con pares reales: en pacientes con metal,
la region de generacion `G = M ∪ B_delta` se borra y el objetivo es el CT real dentro de `G`. Este
script prepara esos pares y **mide** lo que el diseno todavia supone: cuantos cortes hay, si el
parche contiene la banda entera y cuanto ocupa `G` dentro del parche.

DEFINICIONES (identicas a P1, para no introducir una segunda convencion)
------------------------------------------------------------------------
- `M`: metal, HU > 2500 (umbral de cribado, #22).
- `B_delta`: voxeles a distancia euclidea 3D <= 12 mm de `M`, sin `M` (spacing del header).
- `G = M ∪ B_delta`. Fuera de `G` el CT se copia tal cual: por construccion, RMSE = 0 y SSIM = 1
  (las ventanas de SSIM deben quedar integras fuera de `G`).
- Parche: ventana cuadrada de `--parche` px en el plano axial, centrada en el centroide de `G` de ese
  corte y recortada contra los bordes del volumen.

CONTROLES QUE PUEDEN FALLAR
---------------------------
- **Contencion:** `G` del corte debe caber entera en el parche. La fraccion que no cabe se reporta
  por caso y en el resumen; si es alta, el parche es pequeno (decision de la autora).
- **Composicion exacta:** con `--verificar`, se reconstruye el corte pegando el parche sobre el
  original y se comprueba **igualdad bit a bit fuera de `G`**.
- **Particion:** solo se procesan los casos de las particiones pedidas, leidas de `p1_particion.csv`
  (misma particion por paciente que P1, regla de aislamiento de `main.tex:111`).

SALIDA (`--out`)
----------------
`a1_parches.csv` (una fila por corte con metal), `a1_casos.csv` (una fila por caso) y
`a1_parches.md`. Con `--cache` guarda ademas un `.npz` por corte (HU del parche, `M` y `G`), que es
lo unico pesado y queda fuera de git.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

import nibabel as nib
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'objetivo1'))
from p1_decodificador_sd15 import BDELTA_MM, leer_particion, rutas  # noqa: E402
from e6b_vae_sd15 import eje_axial  # noqa: E402
from e6c_techo_lw import METAL_HU  # noqa: E402

PARCHE = 256
MIN_VOX_G = 50  # cortes con menos de esto no aportan par de entrenamiento


def region_generacion(arr: np.ndarray, zooms: tuple[float, ...], mm: float) -> tuple[np.ndarray, np.ndarray]:
    """Mascaras `M` (metal) y `G` (metal mas banda de `mm`), en 3D y con el spacing del header."""
    from scipy.ndimage import distance_transform_edt

    metal = arr > METAL_HU
    if not metal.any():
        return metal, metal
    margen = [int(math.ceil(mm / z)) + 1 for z in zooms]
    nz = np.nonzero(metal)
    sl = tuple(slice(max(0, int(c.min()) - m), min(s, int(c.max()) + m + 1))
               for c, m, s in zip(nz, margen, arr.shape))
    del nz
    sub = metal[sl]
    g = metal.copy()
    g[sl] = (distance_transform_edt(~sub, sampling=zooms) <= mm) | sub
    return metal, g


def ventana(mask2d: np.ndarray, lado: int) -> tuple[int, int, bool]:
    """Origen de la ventana centrada en la mascara y si esta la contiene entera."""
    ys, xs = np.nonzero(mask2d)
    alto, ancho = mask2d.shape
    cabe = (ys.max() - ys.min() + 1 <= lado) and (xs.max() - xs.min() + 1 <= lado)
    y0 = int(round((ys.min() + ys.max()) / 2 - lado / 2))
    x0 = int(round((xs.min() + xs.max()) / 2 - lado / 2))
    return max(0, min(y0, alto - lado)), max(0, min(x0, ancho - lado)), bool(cabe)


def analizar(path: Path, meta: dict, lado: int, mm: float, cache: Path | None,
             verificar: bool) -> tuple[list[dict], dict]:
    """Una fila por corte axial con metal; devuelve tambien el resumen del caso."""
    img = nib.load(path)
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = tuple(float(z) for z in img.header.get_zooms()[:3])
    metal, g = region_generacion(arr, zooms, mm)
    caso = meta['Caso']
    vol = np.moveaxis(arr, eje, 0)
    m3, g3 = np.moveaxis(metal, eje, 0), np.moveaxis(g, eje, 0)
    filas, fuera = [], 0
    for k in range(vol.shape[0]):
        gk = g3[k]
        n_g = int(gk.sum())
        if n_g < MIN_VOX_G:
            continue
        if min(gk.shape) < lado:
            raise RuntimeError(f'corte {gk.shape} menor que el parche de {lado}')
        y0, x0, cabe = ventana(gk, lado)
        fuera += (not cabe)
        sl = (slice(y0, y0 + lado), slice(x0, x0 + lado))
        hu, mk, gk2 = vol[k][sl], m3[k][sl], gk[sl]
        fila = {'Caso': caso, 'particion': meta['particion'], 'Dataset': meta['Dataset'],
                'corte': k, 'y0': y0, 'x0': x0, 'lado': lado,
                'n_metal': int(mk.sum()), 'n_G': int(gk2.sum()), 'n_G_corte': n_g,
                'frac_G_parche': round(float(gk2.mean()), 5), 'cabe': int(cabe),
                'hu_max': round(float(hu.max()), 1)}
        if verificar:
            rec = vol[k].copy()
            rec[sl] = hu  # pegar el parche donde estaba
            if not np.array_equal(rec[~gk], vol[k][~gk]):
                raise RuntimeError(f'{caso} corte {k}: la composicion cambia voxeles fuera de G')
            fila['control_fuera_G'] = 'identico'
        if cache is not None:
            cache.mkdir(parents=True, exist_ok=True)
            np.savez_compressed(cache / f'{caso}_k{k:04d}.npz', hu=hu.astype(np.float32),
                                metal=mk, g=gk2, y0=y0, x0=x0, eje=eje, zooms=np.array(zooms))
        filas.append(fila)
    resumen = {'Caso': caso, 'particion': meta['particion'], 'Dataset': meta['Dataset'],
               'Metal': meta['Metal'], 'cortes_con_G': len(filas), 'cortes_G_no_cabe': fuera,
               'n_metal_vol': int(metal.sum()), 'n_G_vol': int(g.sum()),
               'spacing': ' '.join(f'{z:.4f}' for z in zooms)}
    return filas, resumen


def informe(casos: list[dict], filas: list[dict], out: Path, lado: int, mm: float) -> None:
    """Resumen: cortes por particion, contencion del parche y ocupacion de `G`."""
    import pandas as pd

    c, f = pd.DataFrame(casos), pd.DataFrame(filas)
    L = [f'# A1 — parches 2.5D alrededor del metal (Diseno A)', '',
         f'Parche {lado} x {lado}; banda `B_delta` = {mm:.0f} mm; metal HU > {METAL_HU:.0f}. '
         f'Casos: {len(c)}; cortes con `G`: {len(f)}.', '']
    if not c.empty:
        g = c.groupby('particion').agg(casos=('Caso', 'count'), cortes=('cortes_con_G', 'sum'),
                                       no_cabe=('cortes_G_no_cabe', 'sum'))
        L += ['| Particion | casos | cortes con G | cortes donde G no cabe |', '|---|---|---|---|']
        L += [f'| {i} | {r.casos} | {r.cortes} | {r.no_cabe} |' for i, r in g.iterrows()]
        L.append('')
    if not f.empty:
        L += ['| Magnitud | mediana | p10 | p90 |', '|---|---|---|---|']
        for col in ('n_G', 'n_metal', 'frac_G_parche'):
            v = f[col]
            L.append(f'| {col} | {v.median():.4f} | {v.quantile(0.1):.4f} | {v.quantile(0.9):.4f} |')
        L += ['', f'Cortes donde `G` no cabe en el parche: **{int((f["cabe"] == 0).sum())} de {len(f)}**. '
                  'Si la fraccion es alta, el parche es pequeno: es decision de la autora, no del script.', '']
    if 'control_fuera_G' in f:
        ok = int((f['control_fuera_G'] == 'identico').sum())
        L += [f'**CONTROL de composicion:** {ok} de {len(f)} cortes identicos fuera de `G`.', '']
    (out / 'a1_parches.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'Escrito {out / "a1_parches.md"}', flush=True)


def main() -> None:
    """Extrae los parches de los casos con metal de las particiones pedidas."""
    aqui = Path(__file__).resolve().parent
    raiz = aqui.parents[1]
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--particion', type=Path, default=raiz / 'experiments/objetivo1/p1_particion.csv')
    p.add_argument('--data', type=Path, nargs='+', default=[raiz / 'data'])
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--cache', type=Path, default=None, help='carpeta para los .npz (pesado, fuera de git)')
    p.add_argument('--particiones', nargs='+', default=['train', 'val'])
    p.add_argument('--parche', type=int, default=PARCHE)
    p.add_argument('--bdelta-mm', type=float, default=BDELTA_MM)
    p.add_argument('--solo-metal', action='store_true', default=True)
    p.add_argument('--casos', nargs='*', default=None)
    p.add_argument('--max', type=int, default=None)
    p.add_argument('--verificar', action='store_true', help='control de composicion fuera de G')
    args = p.parse_args()

    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    metas = [m for m in leer_particion(args.particion) if m['particion'] in args.particiones]
    if args.solo_metal:
        metas = [m for m in metas if m['Metal'] == 'si']
    if args.casos:
        metas = [m for m in metas if m['Caso'] in set(args.casos)]
    if args.max:
        metas = metas[:args.max]
    ubic = rutas(metas, args.data)
    faltan = [m['Caso'] for m in metas if m['Caso'] not in ubic]
    if faltan:
        print(f'AVISO: {len(faltan)} volumenes no encontrados: {faltan[:5]}', flush=True)

    filas, casos = [], []
    for i, meta in enumerate(metas, 1):
        if meta['Caso'] not in ubic:
            continue
        try:
            f, c = analizar(ubic[meta['Caso']], meta, args.parche, args.bdelta_mm,
                            args.cache.expanduser() if args.cache else None, args.verificar)
        except Exception as exc:  # un volumen roto no detiene la cohorte
            casos.append({'Caso': meta['Caso'], 'particion': meta['particion'], 'Error': f'{type(exc).__name__}: {exc}'})
            print(f'{meta["Caso"]}: ERROR {exc}', flush=True)
            continue
        filas += f
        casos.append(c)
        print(f'{i}/{len(metas)} {meta["Caso"]}: {c["cortes_con_G"]} cortes con G '
              f'({c["cortes_G_no_cabe"]} no caben)', flush=True)

    campos_f = ['Caso', 'particion', 'Dataset', 'corte', 'y0', 'x0', 'lado', 'n_metal', 'n_G',
                'n_G_corte', 'frac_G_parche', 'cabe', 'hu_max', 'control_fuera_G']
    campos_c = ['Caso', 'particion', 'Dataset', 'Metal', 'cortes_con_G', 'cortes_G_no_cabe',
                'n_metal_vol', 'n_G_vol', 'spacing', 'Error']
    for nombre, campos, datos in (('a1_parches.csv', campos_f, filas), ('a1_casos.csv', campos_c, casos)):
        with (out / nombre).open('w', encoding='utf-8', newline='') as h:
            w = csv.DictWriter(h, fieldnames=campos, extrasaction='ignore')
            w.writeheader()
            w.writerows(datos)
    informe([c for c in casos if 'Error' not in c], filas, out, args.parche, args.bdelta_mm)


if __name__ == '__main__':
    main()
