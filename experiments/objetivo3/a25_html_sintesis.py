"""A25 - HTML para explorar la sintesis (salidas `.nii.gz` de `a15 --nifti`), en 3D y en cortes.

Para cada paciente y punto de control de la carpeta de `a15` que se pase con `--dir` (obligatorio), escribe en
`<carpeta>/html/<etiqueta>/`:

- `<caso>_s<k>_3d.html`: superficies en mm RAS. Hueso (300 HU) del CT sintetico, metal (> 2500 HU) sintetico, el
  tornillo rasterizado (`M`), el borde de la region generada (`G`) y el artefacto (|sintetica - original| > 300 HU
  dentro de `G`). Las capas se prenden y apagan en la leyenda.
- `<caso>_s<k>_cortes.html`: cortes sagital, coronal y axial por el centro de `M`; filas: original, sintetica y
  diferencia (sintetica - original). Ventana osea por omision.

Es una herramienta de inspeccion visual: no mide nada ni sustituye a `a20`/`a24`. Superficie a un umbral de HU
no es una segmentacion.

USO
---
    python experiments/objetivo3/a25_html_sintesis.py --dir experiments/objetivo3/outputs/a15_final_run04/run04_60k
    python experiments/objetivo3/a25_html_sintesis.py --dir experiments/objetivo3/outputs/a15_final_run04/run04_mejor_d003
    python experiments/objetivo3/a25_html_sintesis.py --dir experiments/objetivo3/outputs/a15_delta_run04 --semillas 0 1 2 3 4
    python experiments/objetivo3/a25_html_sintesis.py --dir <carpeta> --casos dataset6_CLINIC_0012_data --cdn
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import nibabel as nib
import numpy as np

_AQUI = Path(__file__).resolve().parent
PATRON = re.compile(r'^a15_(?P<caso>.+_data)_(?P<et>.+)_s(?P<s>\d+)_sintetica\.nii\.gz$')
HUESO_HU, METAL_HU, ARTEFACTO_HU = 300.0, 2500.0, 300.0


def lee(ruta: Path) -> tuple[np.ndarray, np.ndarray]:
    """Volumen en orientacion RAS canonica y su afin."""
    img = nib.as_closest_canonical(nib.load(str(ruta)))
    return img.get_fdata(dtype=np.float32), img.affine


def superficie(fig, vol: np.ndarray, afin: np.ndarray, nivel: float, paso: int, color: str, opacidad: float,
               nombre: str, visible: bool | str = True) -> None:
    """Agrega a `fig` la isosuperficie de `vol` en `nivel`, en mm RAS; si no hay cruce, no agrega nada."""
    import plotly.graph_objects as go
    from skimage.measure import marching_cubes
    if not vol.min() < nivel < vol.max():
        return
    v, f, _, _ = marching_cubes(vol, level=nivel, step_size=paso, allow_degenerate=False)
    xyz = nib.affines.apply_affine(afin, v)
    fig.add_trace(go.Mesh3d(x=xyz[:, 0], y=xyz[:, 1], z=xyz[:, 2], i=f[:, 0], j=f[:, 1], k=f[:, 2],
                            color=color, opacity=opacidad, name=nombre, showlegend=True, visible=visible))


def html_3d(destino: Path, titulo: str, orig: np.ndarray, sint: np.ndarray, M: np.ndarray, G: np.ndarray,
            afin: np.ndarray, js) -> None:
    """Escena 3D con hueso, metal, `M`, borde de `G` y artefacto."""
    import plotly.graph_objects as go
    fig = go.Figure()
    superficie(fig, sint, afin, HUESO_HU, 4, 'ivory', .12, 'hueso sintetico (300 HU, paso 4)')
    superficie(fig, sint, afin, METAL_HU, 1, 'red', 1, 'metal sintetico (> 2500 HU)')
    superficie(fig, M.astype(np.float32), afin, .5, 1, 'cyan', .5, 'tornillo rasterizado (M)', 'legendonly')
    superficie(fig, G.astype(np.float32), afin, .5, 2, 'lightgreen', .15, 'borde de la region generada (G)',
               'legendonly')
    art = np.where(G, np.abs(sint - orig), 0).astype(np.float32)
    superficie(fig, art, afin, ARTEFACTO_HU, 1, 'orange', .45, 'artefacto: |sintetica - original| > 300 HU en G')
    fig.update_layout(title=titulo + ' — superficies por umbral de HU, no segmentacion',
                      scene=dict(aspectmode='data', xaxis_title='R (+) / L (-), mm',
                                 yaxis_title='A (+) / P (-), mm', zaxis_title='S (+) / I (-), mm'))
    fig.write_html(destino, include_plotlyjs=js)


def html_cortes(destino: Path, titulo: str, orig: np.ndarray, sint: np.ndarray, M: np.ndarray, afin: np.ndarray,
                vmin: float, vmax: float, js) -> None:
    """3 x 3 cortes por el centro de `M`: original, sintetica y diferencia."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    ijk = np.round(np.argwhere(M).mean(0)).astype(int) if M.any() else np.array(orig.shape) // 2
    esp = nib.affines.voxel_sizes(afin)
    nombres = ('Sagital', 'Coronal', 'Axial')
    fig = make_subplots(rows=3, cols=3, horizontal_spacing=.04, vertical_spacing=.06,
                        subplot_titles=[f'{n} {p} ({ijk[e]})' for p in ('original', 'sintetica', 'diferencia')
                                        for e, n in enumerate(nombres)])
    dif = sint - orig
    for fila, (vol, lo, hi, cmap) in enumerate([(orig, vmin, vmax, 'Gray'), (sint, vmin, vmax, 'Gray'),
                                                (dif, -1000, 1000, 'RdBu_r')], 1):
        for col, eje in enumerate(range(3), 1):
            plano = np.take(vol, ijk[eje], axis=eje).T
            ejes = [j for j in range(3) if j != eje]
            fig.add_trace(go.Heatmap(z=plano, x=np.arange(plano.shape[1]) * esp[ejes[0]],
                                     y=np.arange(plano.shape[0]) * esp[ejes[1]], zmin=lo, zmax=hi,
                                     colorscale=cmap, showscale=(col == 3 and fila in (2, 3)),
                                     colorbar=dict(len=.3, y=1.0 - (fila - .5) / 3, title='HU')),
                          row=fila, col=col)
            ancla = 'x' + (str((fila - 1) * 3 + col) if (fila - 1) * 3 + col > 1 else '')
            fig.update_yaxes(scaleanchor=ancla, scaleratio=1, row=fila, col=col)
    fig.update_layout(title=f'{titulo} — cortes por el centro de M; ventana [{vmin:.0f}, {vmax:.0f}] HU; '
                            'diferencia en [-1000, 1000] HU', height=1150)
    fig.write_html(destino, include_plotlyjs=js)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir', type=Path, required=True,
                    help='carpeta de a15 con los .nii.gz (o una carpeta con subcarpetas por punto de control)')
    ap.add_argument('--out', type=Path, default=None, help='por omision <dir>/html')
    ap.add_argument('--semillas', type=int, nargs='+', default=[0])
    ap.add_argument('--casos', nargs='*', default=None, help='subconjunto de casos (por omision, todos)')
    ap.add_argument('--etiquetas', nargs='*', default=None, help='subconjunto de puntos de control')
    ap.add_argument('--ventana', type=float, nargs=2, default=[-200, 2000], metavar=('MIN', 'MAX'))
    ap.add_argument('--cdn', action='store_true', help='plotly desde CDN (HTML chicos; necesita internet)')
    ap.add_argument('--solo-cortes', action='store_true', help='no genera la vista 3D (mas rapido)')
    args = ap.parse_args()
    if not args.dir.is_dir():
        raise SystemExit('no existe la carpeta %s' % args.dir)
    out = args.out or args.dir / 'html'
    js = 'cdn' if args.cdn else True

    sinteticas = sorted(p for p in args.dir.rglob('*_sintetica.nii.gz') if out not in p.parents)
    trabajos = []
    for p in sinteticas:
        m = PATRON.match(p.name)
        if not m:
            continue
        caso, et, s = m['caso'], m['et'], int(m['s'])
        if s in args.semillas and (not args.casos or caso in args.casos) and (not args.etiquetas or et in args.etiquetas):
            trabajos.append((caso, et, s, p))
    if not trabajos:
        raise SystemExit('no hay sinteticas que cumplan el filtro en %s' % args.dir)
    print('%d volumenes -> %s' % (len(trabajos), out))

    for caso, et, s, p in trabajos:
        base = p.parent
        faltan = [n for n in ('original', 'M', 'G') if not (base / f'a15_{caso}_{n}.nii.gz').exists()]
        if faltan:
            print('  SALTO %s %s s%d: faltan %s' % (caso, et, s, faltan))
            continue
        orig, afin = lee(base / f'a15_{caso}_original.nii.gz')
        sint, _ = lee(p)
        M = lee(base / f'a15_{caso}_M.nii.gz')[0] > .5
        G = lee(base / f'a15_{caso}_G.nii.gz')[0] > .5
        destino = out / et
        destino.mkdir(parents=True, exist_ok=True)
        titulo = f'{caso} | {et} | semilla {s}'
        html_cortes(destino / f'{caso}_s{s}_cortes.html', titulo, orig, sint, M, afin, *args.ventana, js)
        if not args.solo_cortes:
            html_3d(destino / f'{caso}_s{s}_3d.html', titulo, orig, sint, M, G, afin, js)
        print('  %s %s s%d -> %s' % (caso, et, s, destino))


if __name__ == '__main__':
    main()
