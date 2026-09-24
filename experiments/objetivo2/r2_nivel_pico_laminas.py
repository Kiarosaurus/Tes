"""R2 / #121 — laminas sagitales completas para juzgar el nivel del pico inferior del corredor.

POR QUE UNA LAMINA NUEVA Y NO EL MOSAICO DE R1
----------------------------------------------
El mosaico de `r1_mosaico.py` recorta +-60 mm alrededor de S1, y el propio revisor clinico objeto
(2026-09-14, #53) que con ese recorte **no se pueden contar vertebras**. Por eso se le preparo la
planilla de ITK-SNAP (`r1_cortes_itksnap.csv`): esa revision **nunca se devolvio**, y sigue con 0 de 61
filas respondidas. Es decir: la via que se completa es la lamina, y la via que permite contar era la que
no se completo.

Esta lamina resuelve las dos cosas a la vez. Es **el sagital completo del volumen**, no un recorte, asi
que la columna lumbar entra en la imagen y las vertebras se pueden contar; y es un PNG, asi que no exige
abrir nada. La pregunta se contesta mirando.

CIEGA
-----
La lamina marca **una sola linea**: la altura del pico inferior. **No** marca S1, no dice a cuantos
milimetros esta de S1, y no lleva ningun juicio previo. Marcar S1 contestaria la pregunta sola.

QUE DIBUJA
----------
Por caso, un PNG con el corte sagital que pasa por el punto de S1 (que fija el plano, no la altura),
en ventana osea, con una linea horizontal continua en la altura a juzgar y una regla de 10 mm.

Lee `e9ts_corredor.csv`, `r1_landmarks.csv` y los CT de `data/`. Escribe en `outputs/r2_nivel_pico/`.

USO
---
    python r2_nivel_pico_laminas.py                      # los 18 casos de la planilla
    python r2_nivel_pico_laminas.py --casos <caso> ...   # casos sueltos
"""
from __future__ import annotations

import argparse
from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd

from r1_cortes_itksnap import a_original
from r1_landmarks import cargar

VENTANA_HU = (-200.0, 1300.0)   # ventana osea amplia: cortical nitida y partes blandas visibles
REGLA_MM = 10.0
# Recorte anteroposterior alrededor de la columna. El sagital completo sale apaisado y las vertebras
# quedan pequenas; recortando el aire y las partes blandas de delante y detras, la lamina se alarga y
# los platillos se ven. No se recorta nada en craneocaudal: contar vertebras exige la lumbar entera.
ANCHO_AP_MM = 190.0


def main() -> None:
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--planilla', type=Path, default=here / 'r2_nivel_pico_itksnap.csv')
    parser.add_argument('--casos', nargs='*', default=[])
    parser.add_argument('--marcar-s1', action='store_true',
                        help='dibuja el punto de S1 de R1 (para revalidar el nivel de S1, #53)')
    parser.add_argument('--sin-pico', action='store_true',
                        help='no dibuja la altura del pico inferior')
    parser.add_argument('--perfiles', type=Path, default=here / 'outputs' / 'e9ts_ejes_perfiles.csv',
                        help='perfiles con el eje por altura; con el se marca el PUNTO del corredor '
                             'en vez de una linea de altura (#121)')
    parser.add_argument('--out-dir', type=Path, default=here / 'outputs' / 'r2_nivel_pico')
    args = parser.parse_args()

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    # Eje del corredor por altura. Si esta, la lamina marca el PUNTO por donde pasa el corredor; si no,
    # cae a la linea de altura, que es ambigua cuando el sacro esta inclinado.
    perf = None
    if args.perfiles.exists():
        pf = pd.read_csv(args.perfiles)
        perf = pf[(pf.modo == 'default6mm') & (pf.F_limpieza == 0.0)
                  & (pf.politica_metal == 'hueso')].dropna(subset=['u_x'])

    e9 = pd.read_csv(here / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
    e9 = e9.drop_duplicates('Caso').set_index('Caso')
    r1 = pd.read_csv(here / 'r1_landmarks.csv').set_index('Caso')
    rutas = {p.name[:-len('.nii.gz')]: p for p in (root / 'data').rglob('dataset*.nii.gz')}

    casos = args.casos or list(pd.read_csv(args.planilla).Caso)
    casos = [c for c in casos if c in rutas]
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for caso in casos:
        f = r1.loc[caso]
        # Indices en el ARCHIVO ORIGINAL, con la misma conversion que `r1_cortes_itksnap.py`, para que
        # la lamina se pueda abandonar y seguir en ITK-SNAP sin ir a buscar otra tabla.
        img = nib.load(rutas[caso])
        forma_o = img.shape[:3]
        ornt = nib.orientations.io_orientation(img.affine)
        zoom_o = np.array(img.header.get_zooms()[:3])[np.argsort(ornt[:, 0]).astype(int)]
        eje_archivo = {int(ornt[k, 0]): k for k in range(3)}

        arr, zoom = cargar(rutas[caso])
        zoom = zoom.astype(float)
        ix = int(np.clip(round(float(f['S1_x_mm']) / zoom[0]), 0, arr.shape[0] - 1))
        corte = np.asarray(arr[ix]).astype(np.float32)          # (y, z)
        del arr
        z_pico = (None if args.sin_pico
                  else float(f['S1_z_mm']) + float(e9.loc[caso, 'pico_inf_z_rel_mm']))

        # Sagital anatomico: eje vertical = z (craneo arriba), eje horizontal = y.
        # `corte.T` queda (z, y) y `origin='lower'` ya pone z=0 abajo. NO se aplica `flipud`: hacerlo
        # volteaba la imagen y dejaba la linea en la altura equivocada (visto al mirar la salida).
        img = corte.T
        # Recorte AP centrado en el punto de S1, que esta sobre la columna. Solo cambia el encuadre:
        # ni la altura de la linea ni la escala se tocan.
        media = ANCHO_AP_MM / 2.0
        y0 = max(0.0, float(f['S1_y_mm']) - media)
        y1 = min(img.shape[1] * zoom[1], float(f['S1_y_mm']) + media)
        j0 = int(np.floor(y0 / zoom[1]))
        j1 = max(j0 + 2, int(np.ceil(y1 / zoom[1])))
        img = img[:, j0:j1]
        alto, ancho = img.shape
        extent = [j0 * zoom[1], j1 * zoom[1], 0.0, alto * zoom[2]]

        fig, ax = plt.subplots(figsize=(5.0, 5.0 * alto * zoom[2] / max(ancho * zoom[1], 1e-6)))
        ax.imshow(img, cmap='gray', vmin=VENTANA_HU[0], vmax=VENTANA_HU[1],
                  extent=extent, origin='lower', aspect='equal')
        ancho_mm = extent[1] - extent[0]
        if z_pico is not None:
            fila_eje = None
            if perf is not None:
                cand = perf[(perf.Caso == caso)
                            & np.isclose(perf.z_rel_S1_mm, float(e9.loc[caso, 'pico_inf_z_rel_mm']))]
                if len(cand):
                    fila_eje = cand.iloc[0]
            if fila_eje is not None:
                # PUNTO por donde pasa el corredor, y su seccion. El eje es casi perpendicular al plano
                # sagital (mediana 8.5 grados de la horizontal izq-der, maximo 27), asi que el circulo
                # es la seccion **proyectada**, no exacta. Va declarado en las instrucciones.
                cy, cz = float(fila_eje.c_y_mm), float(fila_eje.c_z_mm)
                rad = float(fila_eje.D_TS_mejor_mm) / 2.0
                ax.add_patch(plt.Circle((cy, cz), rad, fill=False, color='#ff3b30', lw=1.2, ls='--'))
                ax.plot([cy], [cz], marker='+', color='#ff3b30', markersize=16, markeredgewidth=2.0)
                ax.annotate('punto a juzgar', xy=(cy, cz),
                            xytext=(cy - ancho_mm * 0.30, cz + ancho_mm * 0.16),
                            color='#ff3b30', fontsize=9,
                            arrowprops=dict(arrowstyle='->', color='#ff3b30', lw=1.0),
                            annotation_clip=False)
                z_pico = cz
            else:
                ax.axhline(z_pico, color='#ff3b30', lw=1.4)
                ax.text(extent[0] + ancho_mm * 0.03, z_pico + 4.0, 'altura a juzgar',
                        color='#ff3b30', fontsize=9)
        if args.marcar_s1:
            # Cruz sobre el punto de S1 de R1, igual que en el mosaico de `r1_mosaico.py`.
            ax.plot([float(f['S1_y_mm'])], [float(f['S1_z_mm'])], marker='+', color='#ff3b30',
                    markersize=16, markeredgewidth=2.0)
            # El rotulo va PEGADO a la cruz, no en el margen: en la primera version quedaba al otro
            # lado de la imagen y no se veia a que se refería. Y se coloca ARRIBA o ABAJO segun donde
            # caiga la cruz: con la cruz en el tercio superior, el rotulo se salia de la lamina y
            # pisaba el titulo (visto en `metal_0054`, que tiene solo 28 mm de volumen sobre S1).
            ys1, zs1 = float(f['S1_y_mm']), float(f['S1_z_mm'])
            arriba = zs1 < extent[2] + 0.65 * (extent[3] - extent[2])
            dz = ancho_mm * (0.16 if arriba else -0.16)
            dy = -ancho_mm * 0.30 if ys1 > extent[0] + ancho_mm * 0.45 else ancho_mm * 0.18
            ax.annotate('punto a juzgar', xy=(ys1, zs1), xytext=(ys1 + dy, zs1 + dz),
                        color='#ff3b30', fontsize=9,
                        arrowprops=dict(arrowstyle='->', color='#ff3b30', lw=1.0),
                        annotation_clip=False)

        # Regla de 10 mm, para que el nivel se pueda estimar sin depender de la escala del PNG.
        x0 = extent[0] + ancho_mm * 0.70
        y0 = extent[3] * 0.04
        ax.plot([x0, x0 + REGLA_MM], [y0, y0], color='#ffd60a', lw=2.5)
        ax.text(x0, y0 + 5.0, f'{REGLA_MM:.0f} mm', color='#ffd60a', fontsize=9)

        # Pie con los indices de ITK-SNAP del punto marcado.
        if args.marcar_s1:
            y_marca, z_marca = float(f['S1_y_mm']), float(f['S1_z_mm'])
            punto_completo = True
        elif 'fila_eje' in dir() and fila_eje is not None:
            y_marca, z_marca = float(fila_eje.c_y_mm), float(fila_eje.c_z_mm)
            punto_completo = True
        else:
            y_marca, z_marca = float(f['S1_y_mm']), z_pico
            punto_completo = False
        r_ras = np.rint(np.array([float(f['S1_x_mm']), y_marca, z_marca]) / zoom_o)
        r_ras = np.clip(r_ras.astype(int), 0,
                        np.array(forma_o)[np.argsort(ornt[:, 0]).astype(int)] - 1)
        o = a_original(r_ras, ornt, forma_o)
        k_ax = int(o[eje_archivo[2]])
        if punto_completo:
            pie = (f'ITK-SNAP (desde 0): sagital {int(o[eje_archivo[0]])}, '
                   f'coronal {int(o[eje_archivo[1]])}, axial {k_ax}   |   desde 1: '
                   f'{int(o[eje_archivo[0]]) + 1}, {int(o[eje_archivo[1]]) + 1}, {k_ax + 1}')
        else:
            # Sin el eje por altura solo se conoce la ALTURA, y dar un sagital o un coronal seria
            # inventar un punto. Solo ocurre si falta `e9ts_ejes_perfiles.csv` (#121).
            pie = (f'ITK-SNAP: corte axial {k_ax} (desde 0) / {k_ax + 1} (desde 1). '
                   'Solo la altura esta medida.')
        pie += chr(10) + 'Para recorrer en horizontal, varia el corte AXIAL.'
        ax.set_xlabel(pie, fontsize=7, color='#444444', labelpad=4)

        ax.set_title(caso, fontsize=9)
        ax.set_xticks([])
        ax.set_yticks([])
        fig.tight_layout()
        salida = args.out_dir / f'{caso}.png'
        fig.savefig(salida, dpi=140)
        plt.close(fig)
        print(f'{caso} -> {salida.name}', flush=True)

    print(f'{len(casos)} laminas en {args.out_dir}')


if __name__ == '__main__':
    main()
