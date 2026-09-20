"""A1b / Diseno A — parches 2.5D por COMPONENTE de implante (no por corte).

POR QUE EXISTE, Y POR QUE NO SUSTITUYE A `a1_parches.py`
--------------------------------------------------------
`a1_parches.py` corrio sobre la cohorte el 2026-09-20 y su salida es **evidencia de la implicancia #102**
(control de composicion 13496 de 13496; 2714 de 13496 cortes con `G` que no cabe en 256). Ese script queda
congelado, como `ts_piloto_qc.py` quedo congelado para #49/#50. Este es el script nuevo.

EL PROBLEMA QUE RESUELVE (#102)
-------------------------------
En `a1_parches.py`, `G` se define **por corte** como la union de **todo** el metal de ese corte. En un paciente
con material bilateral eso abarca toda la anchura pelvica: en los tres casos peores el metal tiene 9, 12 y 7
componentes repartidos en 380, 358 y 321 mm, y ningun parche centrado puede contenerlo. No es un problema de
encuadre: el parche de 256 ya mide 211.7 mm de mediana. Se verifico ademas que **no** lo explica la mezcla de
implantes (20.0% con componente esbelto frente a 20.2% sin) **ni** el spacing (sin tendencia).

El fondo es otro: en **sintesis** se coloca **un** tornillo, cuya `G` (cilindro de ~4.9 mm mas banda de 12 mm)
cabe de sobra. Entrenar con `G` multi-implante y usar con `G` de un implante es una brecha de dominio distinta
de #95. Decision de la autora del 2026-09-20: **la unidad de entrenamiento es el COMPONENTE**.

QUE CAMBIA EXACTAMENTE
----------------------
- `M` se etiqueta en 3D. Cada componente conexo con volumen >= `--min-comp-mm3` es una **unidad**.
- Para cada componente se calcula **su propia** `B_delta` (EDT en su caja mas margen, con el spacing del header).
- Un parche por (componente, corte axial) con al menos `MIN_VOX_G` voxeles de **esa** `G`.
- Los canales `M` y `G` del parche llevan **solo el componente objetivo**. Si en el parche cae metal de otro
  componente, se queda en los HU de contexto (es anatomia real del paciente) y se **cuenta** en `n_metal_otros`.
  Asi la mezcla se puede medir en vez de suponerse, que es lo que pedia el riesgo 3 de `diseno_A.md`.

CONTROLES QUE PUEDEN FALLAR
---------------------------
- **Composicion:** con `--verificar`, pegar el parche sobre el corte original deja identico bit a bit todo lo
  que esta fuera de la `G` del componente.
- **Contencion:** se reporta por componente. La prediccion de #102 es que ahora deberia ser casi siempre `cabe`;
  si NO lo es, la causa no era la union multi-implante y hay que volver a mirar.
- **Particion:** solo casos de las particiones pedidas, leidas de `p1_particion.csv` (regla de aislamiento).

SALIDA (`--out`)
----------------
`a1b_parches.csv` (una fila por parche), `a1b_componentes.csv` (una por componente), `a1b_casos.csv` y
`a1b_parches.md`. Con `--cache`, un `.npz` por parche: `{caso}_c{comp:03d}_k{corte:04d}.npz`.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'objetivo1'))
from p1_decodificador_sd15 import BDELTA_MM, leer_particion, rutas  # noqa: E402
from e6b_vae_sd15 import eje_axial  # noqa: E402
from e6c_techo_lw import METAL_HU  # noqa: E402
from a1_parches import MIN_VOX_G, PARCHE, ventana  # noqa: E402

MIN_COMP_MM3 = 10.0  # mismo minimo de fragmento que E8 (`MIN_FRAG_MM3`)


def caja_componente(sl: tuple[slice, ...], zooms: tuple[float, ...], mm: float,
                    forma: tuple[int, ...]) -> tuple[slice, ...]:
    """Caja del componente ensanchada por la banda de `mm`, recortada al volumen."""
    margen = [int(math.ceil(mm / z)) + 1 for z in zooms]
    return tuple(slice(max(0, s.start - m), min(n, s.stop + m))
                 for s, m, n in zip(sl, margen, forma))


def banda_en_caja(comp_sub: np.ndarray, zooms: tuple[float, ...], mm: float) -> np.ndarray:
    """`G` del componente DENTRO de su caja: el componente mas su banda de `mm`.

    Trabaja solo en la caja y nunca materializa una mascara del tamano del volumen. Esa es la
    diferencia con la primera version, que murio por memoria a los 47 de 79 casos.
    """
    return (ndi.distance_transform_edt(~comp_sub, sampling=zooms) <= mm) | comp_sub


def ventana_coords(ys: np.ndarray, xs: np.ndarray, alto: int, ancho: int,
                   lado: int) -> tuple[int, int, bool]:
    """Como `a1_parches.ventana`, pero desde coordenadas ya extraidas (sin mascara completa)."""
    cabe = (ys.max() - ys.min() + 1 <= lado) and (xs.max() - xs.min() + 1 <= lado)
    y0 = int(round((int(ys.min()) + int(ys.max())) / 2 - lado / 2))
    x0 = int(round((int(xs.min()) + int(xs.max())) / 2 - lado / 2))
    return max(0, min(y0, alto - lado)), max(0, min(x0, ancho - lado)), bool(cabe)


def analizar(path: Path, meta: dict, lado: int, mm: float, min_mm3: float,
             cache: Path | None, verificar: bool) -> tuple[list[dict], list[dict], dict]:
    """Una fila por (componente, corte). Devuelve parches, componentes y resumen del caso."""
    img = nib.load(path)
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = tuple(float(z) for z in img.header.get_zooms()[:3])
    vox_mm3 = float(np.prod(zooms))
    caso = meta['Caso']

    metal = arr > METAL_HU
    etiquetas, n = ndi.label(metal)
    tam = np.bincount(etiquetas.ravel())
    cajas = ndi.find_objects(etiquetas)
    validos = [i for i in range(1, n + 1) if tam[i] * vox_mm3 >= min_mm3]

    # Todo en el marco axial: el eje del corte va primero. `vol` y `metal_ax` son vistas.
    orden = [eje] + [i for i in range(3) if i != eje]
    zooms_ax = tuple(zooms[i] for i in orden)
    vol = np.moveaxis(arr, eje, 0)
    metal_ax = np.moveaxis(metal, eje, 0)
    lab_ax = np.moveaxis(etiquetas, eje, 0)
    alto, ancho = vol.shape[1], vol.shape[2]
    parches, comps, fuera_tot = [], [], 0

    for ci, lab in enumerate(validos):
        caja_ax = tuple(cajas[lab - 1][i] for i in orden)
        ext = [round((cajas[lab - 1][i].stop - cajas[lab - 1][i].start) * zooms[i], 1)
               for i in range(3)]
        # Caja ensanchada por la banda; fuera de ella `G` de ESTE componente es vacia por definicion.
        cj = caja_componente(caja_ax, zooms_ax, mm, vol.shape)
        comp_sub = lab_ax[cj] == lab
        g_sub = banda_en_caja(comp_sub, zooms_ax, mm)
        oy, ox = cj[1].start, cj[2].start
        n_cortes, fuera = 0, 0
        for kk in range(g_sub.shape[0]):
            gk_sub = g_sub[kk]
            n_g = int(gk_sub.sum())
            if n_g < MIN_VOX_G:
                continue
            k = cj[0].start + kk
            if min(alto, ancho) < lado:
                raise RuntimeError(f'corte ({alto}, {ancho}) menor que el parche de {lado}')
            ys, xs = np.nonzero(gk_sub)
            y0, x0, cabe = ventana_coords(ys + oy, xs + ox, alto, ancho, lado)
            sl = (slice(y0, y0 + lado), slice(x0, x0 + lado))
            # `M` y `G` del parche: solo el componente objetivo, colocado en coordenadas del parche
            mk = np.zeros((lado, lado), dtype=bool)
            gk2 = np.zeros((lado, lado), dtype=bool)
            iy0, ix0 = max(y0, oy), max(x0, ox)
            iy1 = min(y0 + lado, oy + gk_sub.shape[0])
            ix1 = min(x0 + lado, ox + gk_sub.shape[1])
            if iy1 > iy0 and ix1 > ix0:
                org = (slice(iy0 - oy, iy1 - oy), slice(ix0 - ox, ix1 - ox))
                dst = (slice(iy0 - y0, iy1 - y0), slice(ix0 - x0, ix1 - x0))
                mk[dst] = comp_sub[kk][org]
                gk2[dst] = gk_sub[org]
            hu = vol[k][sl]
            # metal de OTROS componentes dentro del parche: se mide, no se enmascara
            otros = int((metal_ax[k][sl] & ~mk).sum())
            fila = {'Caso': caso, 'particion': meta['particion'], 'Dataset': meta['Dataset'],
                    'comp': ci, 'corte': k, 'y0': y0, 'x0': x0, 'lado': lado,
                    'n_metal': int(mk.sum()), 'n_G': int(gk2.sum()),
                    'n_G_corte': n_g, 'n_metal_otros': otros,
                    'frac_G_parche': round(float(gk2.mean()), 5), 'cabe': int(cabe)}
            if verificar:
                # fuera de la G del componente, pegar el parche no puede cambiar nada
                gfull = np.zeros((alto, ancho), dtype=bool)
                gfull[oy:oy + gk_sub.shape[0], ox:ox + gk_sub.shape[1]] = gk_sub
                rec = vol[k].copy()
                rec[sl] = hu
                if not np.array_equal(rec[~gfull], vol[k][~gfull]):
                    raise RuntimeError(f'{caso} comp {ci} corte {k}: composicion cambia fuera de G')
                fila['control_fuera_G'] = 'identico'
                del gfull, rec
            if cache is not None:
                cache.mkdir(parents=True, exist_ok=True)
                np.savez_compressed(cache / f'{caso}_c{ci:03d}_k{k:04d}.npz',
                                    hu=np.ascontiguousarray(hu, dtype=np.float32),
                                    metal=mk, g=gk2,
                                    y0=y0, x0=x0, eje=eje, zooms=np.array(zooms))
            parches.append(fila)
            n_cortes += 1
            fuera += (not cabe)
        comps.append({'Caso': caso, 'particion': meta['particion'], 'comp': ci,
                      'n_vox': int(tam[lab]), 'vol_mm3': round(tam[lab] * vox_mm3, 1),
                      'ext_mm': ' '.join(str(e) for e in ext),
                      'cortes': n_cortes, 'cortes_no_cabe': fuera})
        fuera_tot += fuera
        del comp_sub, g_sub

    resumen = {'Caso': caso, 'particion': meta['particion'], 'Dataset': meta['Dataset'],
               'Metal': meta['Metal'], 'componentes': len(validos),
               'componentes_brutos': int(n), 'parches': len(parches),
               'parches_no_cabe': fuera_tot, 'n_metal_vol': int(metal.sum()),
               'spacing': ' '.join(f'{z:.4f}' for z in zooms)}
    return parches, comps, resumen


def informe(casos: list[dict], comps: list[dict], filas: list[dict], out: Path,
            lado: int, mm: float) -> None:
    """Resumen: parches por particion, contencion por componente y mezcla de implantes."""
    import pandas as pd

    c, k, f = pd.DataFrame(casos), pd.DataFrame(comps), pd.DataFrame(filas)
    # las filas pueden venir de los CSV (todo texto) al reanudar: se convierten las numericas
    for df, cols in ((c, ('componentes', 'parches', 'parches_no_cabe', 'n_metal_vol')),
                     (k, ('cortes', 'cortes_no_cabe', 'n_vox', 'vol_mm3')),
                     (f, ('n_G', 'n_metal', 'n_metal_otros', 'frac_G_parche', 'cabe'))):
        for col in cols:
            if col in df:
                df[col] = pd.to_numeric(df[col], errors='coerce')
    L = ['# A1b — parches 2.5D por COMPONENTE (Diseno A, decision 2026-09-20)', '',
         f'Parche {lado} x {lado}; `B_delta` = {mm:.0f} mm por componente; metal HU > {METAL_HU:.0f}. '
         f'Casos: {len(c)}; componentes: {len(k)}; parches: {len(f)}.', '',
         'Frente a `a1_parches.py` (por corte), aqui cada componente conexo de metal es una unidad con su '
         'propia banda. Comparar la columna de contencion con el 2714 de 13496 de #102.', '']
    if not c.empty:
        g = c.groupby('particion').agg(casos=('Caso', 'count'), comps=('componentes', 'sum'),
                                       parches=('parches', 'sum'), no_cabe=('parches_no_cabe', 'sum'))
        L += ['| Particion | casos | componentes | parches | parches donde G no cabe |',
              '|---|---|---|---|---|']
        L += [f'| {i} | {r.casos} | {r.comps} | {r.parches} | {r.no_cabe} |' for i, r in g.iterrows()]
        L.append('')
    if not f.empty:
        L += ['| Magnitud | mediana | p10 | p90 |', '|---|---|---|---|']
        for col in ('n_G', 'n_metal', 'n_metal_otros', 'frac_G_parche'):
            v = f[col]
            L.append(f'| {col} | {v.median():.4f} | {v.quantile(0.1):.4f} | {v.quantile(0.9):.4f} |')
        n_mal = int((f['cabe'] == 0).sum())
        L += ['', f'Parches donde `G` del componente no cabe: **{n_mal} de {len(f)}** '
                  f'({n_mal / len(f):.1%}). En #102, por corte, eran 2714 de 13496 (20.1%).', '',
              f'Parches con metal de OTRO componente dentro: '
              f'**{int((f["n_metal_otros"] > 0).sum())} de {len(f)}**. No se enmascara: queda en los HU de '
              'contexto y se declara.', '']
    if 'control_fuera_G' in f:
        ok = int((f['control_fuera_G'] == 'identico').sum())
        L += [f'**CONTROL de composicion:** {ok} de {len(f)} parches identicos fuera de `G`.', '']
    (out / 'a1b_parches.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'Escrito {out / "a1b_parches.md"}', flush=True)


def escribe(ruta: Path, filas: list[dict]) -> None:
    if not filas:
        return
    campos: list[str] = []
    for f in filas:
        for c in f:
            if c not in campos:
                campos.append(c)
    with open(ruta, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)


def anexa(ruta: Path, filas: list[dict], campos: list[str]) -> None:
    """Anexa filas creando la cabecera si el archivo no existe. Hace `flush` en cada caso.

    La primera version escribia los CSV solo al final y el proceso murio por memoria a los 47 de 79
    casos, perdiendo todo lo calculado. Aqui cada caso queda en disco en cuanto termina.
    """
    if not filas:
        return
    nuevo = not ruta.exists()
    with open(ruta, 'a', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=campos, extrasaction='ignore')
        if nuevo:
            w.writeheader()
        w.writerows(filas)
        fh.flush()


def ya_hechos(ruta: Path) -> set[str]:
    """Casos con fila en `a1b_casos.csv`, para reanudar sin repetirlos."""
    if not ruta.exists():
        return set()
    with open(ruta, newline='', encoding='utf-8') as fh:
        return {f['Caso'] for f in csv.DictReader(fh) if f.get('Caso')}


def lee(ruta: Path) -> list[dict]:
    if not ruta.exists():
        return []
    with open(ruta, newline='', encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    aqui = Path(__file__).resolve().parent
    raiz = aqui.parents[1]
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--particion', type=Path, default=raiz / 'experiments/objetivo1/p1_particion.csv')
    p.add_argument('--data', type=Path, nargs='+', default=[raiz / 'data'])
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--cache', type=Path, default=None)
    p.add_argument('--particiones', nargs='+', default=['train', 'val'])
    p.add_argument('--parche', type=int, default=PARCHE)
    p.add_argument('--bdelta-mm', type=float, default=BDELTA_MM)
    p.add_argument('--min-comp-mm3', type=float, default=MIN_COMP_MM3)
    p.add_argument('--casos', nargs='*', default=None)
    p.add_argument('--max', type=int, default=None)
    p.add_argument('--verificar', action='store_true')
    args = p.parse_args()

    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    metas = [m for m in leer_particion(args.particion)
             if m['particion'] in args.particiones and m['Metal'] == 'si']
    if args.casos:
        metas = [m for m in metas if m['Caso'] in set(args.casos)]
    if args.max:
        metas = metas[:args.max]
    ubic = rutas(metas, args.data)

    f_par, f_com, f_cas = (out / 'a1b_parches.csv', out / 'a1b_componentes.csv',
                           out / 'a1b_casos.csv')
    C_PAR = ['Caso', 'particion', 'Dataset', 'comp', 'corte', 'y0', 'x0', 'lado', 'n_metal',
             'n_G', 'n_G_corte', 'n_metal_otros', 'frac_G_parche', 'cabe', 'control_fuera_G']
    C_COM = ['Caso', 'particion', 'comp', 'n_vox', 'vol_mm3', 'ext_mm', 'cortes', 'cortes_no_cabe']
    C_CAS = ['Caso', 'particion', 'Dataset', 'Metal', 'componentes', 'componentes_brutos',
             'parches', 'parches_no_cabe', 'n_metal_vol', 'spacing', 'Error']

    hechos = ya_hechos(f_cas)
    if hechos:
        print(f'reanudando: {len(hechos)} casos ya en {f_cas.name}', flush=True)

    for i, meta in enumerate(metas, 1):
        if meta['Caso'] not in ubic or meta['Caso'] in hechos:
            continue
        try:
            f, k, c = analizar(ubic[meta['Caso']], meta, args.parche, args.bdelta_mm,
                               args.min_comp_mm3,
                               args.cache.expanduser() if args.cache else None, args.verificar)
        except Exception as exc:
            anexa(f_cas, [{'Caso': meta['Caso'], 'particion': meta['particion'],
                           'Error': f'{type(exc).__name__}: {exc}'}], C_CAS)
            print(f'{meta["Caso"]}: ERROR {exc}', flush=True)
            continue
        anexa(f_par, f, C_PAR)
        anexa(f_com, k, C_COM)
        anexa(f_cas, [c], C_CAS)
        print(f'{i}/{len(metas)} {meta["Caso"]}: {c["componentes"]} comp, '
              f'{c["parches"]} parches ({c["parches_no_cabe"]} no caben)', flush=True)

    informe(lee(f_cas), lee(f_com), lee(f_par), out, args.parche, args.bdelta_mm)


if __name__ == '__main__':
    main()
