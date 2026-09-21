"""A3 / Diseno A — laminas de componentes metalicos para la revision de la autora (#104).

PARA QUE
--------
A1b partio el metal de la cohorte en **363 componentes** y cada uno es una unidad de entrenamiento
(decision D2, #102). Pero #104 mostro que esos componentes son en buena parte **fragmentos**
(volumen mediano 458 mm3, frente a ~1450 mm3 de un tornillo de 4.8 x 80 mm) y que el 52% queda por
debajo de 500 mm3. Hace falta un **umbral declarado** de que cuenta como implante, y un umbral
elegido sin mirar los datos es tan arbitrario como uno elegido mirandolos demasiado.

Estas laminas son el termino medio que ya usa el proyecto (laminas de E9-TS, decision #53): el filtro
automatico propone, una muestra se revisa a ojo, y el acuerdo entre los dos **queda medido**. Lo que
se valida aqui no es cada componente, es el **criterio**.

QUE NO ES
---------
No es un juicio clinico. Distinguir "objeto alargado y fino" de "placa, protesis o fragmento" es
geometria, no diagnostico, y por eso lo puede llenar la autora (a diferencia de #53, que fue a un
revisor medico). Las laminas son cortes y proyecciones: **no demuestran ausencia de error** (#19, #21).

MUESTREO
--------
Estratificado por volumen en escala logaritmica, con semilla fija, para que la muestra cubra desde el
fragmento diminuto hasta la protesis grande. Se **sobremuestrea a proposito la franja de 100-500 mm3**,
que es donde caeria el umbral propuesto (200 mm3) y donde la decision se juega.

SALIDA
------
Un PNG por componente en `--out/laminas/`, mas `a3_revision_componentes.csv`, la planilla que llena la
autora (columnas `veredicto` y `nota` vacias). El CSV se versiona; los PNG no (van a `outputs/`).
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import nibabel as nib  # noqa: E402
import numpy as np  # noqa: E402
from scipy import ndimage as ndi  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'objetivo1'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'objetivo2'))
from p1_decodificador_sd15 import leer_particion, rutas  # noqa: E402
from e6c_techo_lw import METAL_HU  # noqa: E402
from e6b_vae_sd15 import eje_axial  # noqa: E402
from e8_censo_implantes import pca_extension  # noqa: E402
from a1b_parches_componente import MIN_COMP_MM3  # noqa: E402

BINS_MM3 = [0, 50, 100, 200, 500, 1000, 5000, 10 ** 9]
CUPO = [4, 5, 8, 8, 5, 5, 5]  # sobremuestrea 100-500 mm3: ahi cae el umbral en discusion
VENTANA = (-200.0, 1800.0)  # ventana osea ancha, para que el metal no tape el hueso


def muestrea(comps: list[dict], cupo: list[int], semilla: int) -> list[dict]:
    """Muestra estratificada por volumen, con semilla fija."""
    rng = np.random.default_rng(semilla)
    sel: list[dict] = []
    for i in range(len(BINS_MM3) - 1):
        lo, hi = BINS_MM3[i], BINS_MM3[i + 1]
        grupo = [c for c in comps if lo <= float(c['vol_mm3']) < hi]
        if not grupo:
            continue
        idx = rng.permutation(len(grupo))[:cupo[i]]
        sel += [grupo[j] for j in sorted(idx)]
    return sel


def medidas(comp: np.ndarray, zooms: tuple[float, ...]) -> dict[str, float]:
    """Largo y los dos anchos por eje principal, como en E11 (PCA, no caja alineada)."""
    pts = np.argwhere(comp).astype(np.float64) * np.array(zooms)
    if len(pts) < 4:
        return {'largo_mm': 0.0, 'ancho2_mm': 0.0, 'ancho3_mm': 0.0}
    _, _, ext = pca_extension(pts)
    e = sorted(float(v) for v in ext)
    return {'largo_mm': round(e[2], 1), 'ancho2_mm': round(e[1], 1), 'ancho3_mm': round(e[0], 1)}


def lamina(arr: np.ndarray, comp: np.ndarray, zooms: tuple[float, ...], info: dict,
           destino: Path) -> None:
    """Tres proyecciones de la mascara (forma) mas un corte de CT con el contorno encima."""
    # Recorte a la caja del componente mas un margen: sin esto el objeto sale diminuto en el cuadro
    # y la lamina no sirve para juzgar forma, que es justo para lo que existe.
    nz = np.nonzero(comp)
    marg = [max(4, int(round(8.0 / z))) for z in zooms]
    cj = tuple(slice(max(0, int(c.min()) - m), min(s, int(c.max()) + m + 1))
               for c, m, s in zip(nz, marg, comp.shape))
    csub = comp[cj]

    fig, ax = plt.subplots(1, 4, figsize=(17, 4.6))
    nombres = ['proyeccion axial', 'proyeccion 1', 'proyeccion 2']
    for a in range(3):
        proy = csub.max(axis=a).T
        ejes = [i for i in range(3) if i != a]
        asp = zooms[ejes[0]] / zooms[ejes[1]] if zooms[ejes[1]] else 1.0
        ax[a].imshow(proy, cmap='gray', origin='lower', aspect=asp, interpolation='nearest')
        ax[a].set_title(f'{nombres[a]} ({proy.shape[1]}x{proy.shape[0]} vox)', fontsize=9)
        ax[a].set_xticks([]); ax[a].set_yticks([])

    k = int(round(nz[0].mean()))
    # el CT se recorta tambien, pero con mas margen: hay que ver el hueso alrededor
    marg2 = [max(30, int(round(60.0 / z))) for z in zooms[1:]]
    c2 = tuple(slice(max(0, int(c.min()) - m), min(s, int(c.max()) + m + 1))
               for c, m, s in zip(nz[1:], marg2, comp.shape[1:]))
    corte = arr[k][c2]
    ax[3].imshow(corte, cmap='gray', vmin=VENTANA[0], vmax=VENTANA[1],
                 aspect=zooms[2] / zooms[1] if zooms[1] else 1.0, interpolation='nearest')
    if comp[k][c2].any():
        ax[3].contour(comp[k][c2], levels=[0.5], colors='red', linewidths=1.1)
    ax[3].set_title(f'CT, corte {k} (ventana osea); rojo = componente', fontsize=9)
    ax[3].set_xticks([]); ax[3].set_yticks([])

    fig.suptitle(
        f"{info['Caso']}  comp {info['comp']}   |   volumen {float(info['vol_mm3']):.0f} mm3   "
        f"|   PCA largo {info['largo_mm']} / anchos {info['ancho2_mm']} y {info['ancho3_mm']} mm   "
        f"|   {info['cortes']} parches   |   referencia: tornillo 4.8 x 80 mm = ~1450 mm3\n"
        f"ITK-SNAP: cursor en vóxel (x, y, z) = {info['voxel_itksnap']}   "
        f"[indice 0; si el visor numera desde 1, sumar 1]",
        fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(destino, dpi=95)
    plt.close(fig)


def fila_de(caso: str, ci: int, c: dict, med: dict, info: dict, ruta: Path, raiz: Path) -> dict:
    """Una fila de la planilla. Unica definicion, para que `--solo-planilla` no diverja."""
    return {'Caso': caso, 'comp': ci, 'particion': c['particion'],
            'vol_mm3': round(float(c['vol_mm3']), 1),
            'largo_mm': med['largo_mm'], 'ancho2_mm': med['ancho2_mm'],
            'ancho3_mm': med['ancho3_mm'], 'parches': c['cortes'],
            'voxel_itksnap': info['voxel_itksnap'], 'corte_axial': info['corte_axial'],
            'propuesta_auto': propone(float(c['vol_mm3']), med),
            'lamina': str(ruta.relative_to(raiz)).replace('\\', '/'),
            'veredicto': '', 'nota': ''}


def main() -> None:
    aqui = Path(__file__).resolve().parent
    raiz = aqui.parents[1]
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--componentes', type=Path, default=aqui / 'outputs/a1b/a1b_componentes.csv')
    p.add_argument('--particion', type=Path, default=raiz / 'experiments/objetivo1/p1_particion.csv')
    p.add_argument('--data', type=Path, nargs='+', default=[raiz / 'data'])
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--planilla', type=Path, default=aqui / 'a3_revision_componentes.csv')
    p.add_argument('--semilla', type=int, default=20260920)
    p.add_argument('--min-comp-mm3', type=float, default=MIN_COMP_MM3)
    p.add_argument('--forzar', action='store_true',
                   help='sobrescribe la planilla aunque tenga veredictos (no usar a la ligera)')
    p.add_argument('--solo-planilla', action='store_true',
                   help='rehace la planilla sin volver a dibujar los PNG')
    args = p.parse_args()

    out = args.out.expanduser().resolve()  # `--out` puede venir relativo
    (out / 'laminas').mkdir(parents=True, exist_ok=True)
    comps = list(csv.DictReader(open(args.componentes, encoding='utf-8')))
    sel = muestrea(comps, CUPO, args.semilla)
    print(f'muestra: {len(sel)} de {len(comps)} componentes', flush=True)

    metas = {m['Caso']: m for m in leer_particion(args.particion)}
    ubic = rutas(list(metas.values()), args.data)
    por_caso: dict[str, list[dict]] = {}
    for c in sel:
        por_caso.setdefault(c['Caso'], []).append(c)

    filas = []
    for i, (caso, cs) in enumerate(sorted(por_caso.items()), 1):
        if caso not in ubic:
            print(f'{caso}: NO ENCONTRADO', flush=True)
            continue
        img = nib.load(ubic[caso])
        arr = img.get_fdata(dtype=np.float32)
        zooms = tuple(float(z) for z in img.header.get_zooms()[:3])
        eje = eje_axial(img)
        vox = float(np.prod(zooms))
        etiquetas, n = ndi.label(arr > METAL_HU)
        tam = np.bincount(etiquetas.ravel())
        # MISMO orden que a1b: los validos se enumeran 1..n y se filtran por volumen
        validos = [j for j in range(1, n + 1) if tam[j] * vox >= args.min_comp_mm3]
        for c in cs:
            ci = int(c['comp'])
            if ci >= len(validos):
                print(f'{caso} comp {ci}: fuera de rango', flush=True)
                continue
            comp = etiquetas == validos[ci]
            med = medidas(comp, zooms)
            # Centroide en indices del ARCHIVO (x, y, z), que es lo que se teclea en ITK-SNAP.
            nzc = np.nonzero(comp)
            centro = tuple(int(round(float(a.mean()))) for a in nzc)
            info = {**c, **med, 'voxel_itksnap': f'{centro[0]}, {centro[1]}, {centro[2]}'}
            ruta = out / 'laminas' / f'{caso}_c{ci:03d}.png'
            if args.solo_planilla:
                info['corte_axial'] = int(round(float(
                    np.nonzero(np.moveaxis(comp, eje, 0))[0].mean())))
                filas.append(fila_de(caso, ci, c, med, info, ruta, raiz))
                del comp
                continue
            # El panel de CT tiene que ser AXIAL. El eje axial no es siempre el 0 del archivo
            # (en esta cohorte la orientacion es ('L','P','S') y el axial es el eje 2), asi que se
            # mueve primero, igual que hace `a1b_parches_componente.py`. Sin esto el corte sale
            # sagital y su numero no corresponde al que muestra ITK-SNAP.
            arr_ax = np.moveaxis(arr, eje, 0)
            comp_ax = np.moveaxis(comp, eje, 0)
            zooms_ax = tuple(zooms[i] for i in [eje] + [j for j in range(3) if j != eje])
            info['corte_axial'] = int(round(float(np.nonzero(comp_ax)[0].mean())))
            lamina(arr_ax, comp_ax, zooms_ax, info, ruta)
            filas.append(fila_de(caso, ci, c, med, info, ruta, raiz))
            del comp
        del arr, etiquetas
        print(f'{i}/{len(por_caso)} {caso}: {len(cs)} laminas', flush=True)

    # Orden alfabetico por caso y, dentro del caso, por numero de componente: es el mismo orden en
    # que aparecen los PNG en la carpeta, asi la revision se hace bajando la lista sin buscar.
    filas.sort(key=lambda r: (r['Caso'], int(r['comp'])))
    # SEGURO: nunca pisar una planilla que ya tenga veredictos escritos a mano.
    if args.planilla.exists() and not args.forzar:
        with open(args.planilla, newline='', encoding='utf-8') as fh:
            llenos = sum(1 for r in csv.DictReader(fh) if (r.get('veredicto') or '').strip())
        if llenos:
            print(f'ABORTA: {args.planilla.name} ya tiene {llenos} veredictos. '
                  f'Usa --planilla <otro.csv> o --forzar si de verdad quieres sobrescribir.')
            return
    with open(args.planilla, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print(f'Escrita planilla {args.planilla} ({len(filas)} filas)', flush=True)


def propone(vol: float, med: dict[str, float]) -> str:
    """Lo que diria el filtro automatico propuesto en #104. Es la hipotesis a contrastar."""
    if vol < 200.0:
        return 'fragmento'
    if med['largo_mm'] >= 30.0 and med['ancho2_mm'] <= 12.0:
        return 'tornillo'
    return 'otro implante'


if __name__ == '__main__':
    main()
