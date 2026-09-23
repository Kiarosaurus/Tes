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

import numpy as np
import pandas as pd

from r1_landmarks import cargar

VENTANA_HU = (-200.0, 1300.0)   # ventana osea amplia: cortical nitida y partes blandas visibles
REGLA_MM = 10.0


def main() -> None:
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--planilla', type=Path, default=here / 'r2_nivel_pico_itksnap.csv')
    parser.add_argument('--casos', nargs='*', default=[])
    parser.add_argument('--out-dir', type=Path, default=here / 'outputs' / 'r2_nivel_pico')
    args = parser.parse_args()

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    e9 = pd.read_csv(here / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
    e9 = e9.drop_duplicates('Caso').set_index('Caso')
    r1 = pd.read_csv(here / 'r1_landmarks.csv').set_index('Caso')
    rutas = {p.name[:-len('.nii.gz')]: p for p in (root / 'data').rglob('dataset*.nii.gz')}

    casos = args.casos or list(pd.read_csv(args.planilla).Caso)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for caso in casos:
        f = r1.loc[caso]
        arr, zoom = cargar(rutas[caso])
        zoom = zoom.astype(float)
        ix = int(np.clip(round(float(f['S1_x_mm']) / zoom[0]), 0, arr.shape[0] - 1))
        corte = np.asarray(arr[ix]).astype(np.float32)          # (y, z)
        del arr
        z_pico = float(f['S1_z_mm']) + float(e9.loc[caso, 'pico_inf_z_rel_mm'])

        # Sagital anatomico: eje vertical = z (craneo arriba), eje horizontal = y.
        # `corte.T` queda (z, y) y `origin='lower'` ya pone z=0 abajo. NO se aplica `flipud`: hacerlo
        # volteaba la imagen y dejaba la linea en la altura equivocada (visto al mirar la salida).
        img = corte.T
        alto, ancho = img.shape
        extent = [0.0, ancho * zoom[1], 0.0, alto * zoom[2]]

        fig, ax = plt.subplots(figsize=(6.5, 6.5 * alto * zoom[2] / max(ancho * zoom[1], 1e-6)))
        ax.imshow(img, cmap='gray', vmin=VENTANA_HU[0], vmax=VENTANA_HU[1],
                  extent=extent, origin='lower', aspect='equal')
        ax.axhline(z_pico, color='#ff3b30', lw=1.4)
        ax.text(extent[1] * 0.02, z_pico + 3.0, 'altura a juzgar', color='#ff3b30', fontsize=9)

        # Regla de 10 mm, para que el nivel se pueda estimar sin depender de la escala del PNG.
        x0 = extent[1] * 0.86
        y0 = extent[3] * 0.06
        ax.plot([x0, x0 + REGLA_MM], [y0, y0], color='#ffd60a', lw=2.5)
        ax.text(x0, y0 + 4.0, f'{REGLA_MM:.0f} mm', color='#ffd60a', fontsize=9)

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
