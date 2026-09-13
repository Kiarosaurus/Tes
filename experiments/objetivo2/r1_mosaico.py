"""R1 / #26 — mosaico de revision del nivel de S1 (una pagina cada 20 volumenes).

Los dos detectores de S1 de `r1_landmarks.py` fallan por un nivel vertebral (~30 mm) en
casos distintos, y la esfera de 12 mm no absorbe ese error. Ninguna cifra de S1 es
defendible sin mirar. Este script pone en una sola pagina, por volumen, el corte sagital
medio ampliado (+-60 mm) con los dos candidatos:

- cruz roja: S1 por metodo sagital (primario), con la esfera de 12 mm;
- linea amarilla discontinua: z de S1 por metodo del ala (control).

La revision consiste en decir, por teja, si la cruz roja esta en el platillo superior de
S1 (`ok`), un nivel arriba/abajo (`+1` / `-1`) o si no se puede decidir (`?`).

Lee `r1_estados.csv` (salida de `r1_resumen.py`) y `data/`. Escribe PNG en
`outputs/r1_mosaico/` (ignorado por git).
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from r1_landmarks import cargar

POR_PAGINA = 20


def main() -> None:
    """Punto de entrada de linea de comandos."""
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--cohorte', default='evaluacion',
                        help="'evaluacion', 'calibracion' o 'todos'")
    parser.add_argument('--solo-discordantes', action='store_true')
    args = parser.parse_args()

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    d = pd.read_csv(here / 'r1_estados.csv')
    if args.cohorte != 'todos':
        d = d[d['cohorte'] == args.cohorte]
    if args.solo_discordantes:
        d = d[d['s1_discordante']]
    d = d.sort_values('Caso').reset_index(drop=True)
    out = here / 'outputs' / 'r1_mosaico'
    out.mkdir(parents=True, exist_ok=True)
    sufijo = f'{args.cohorte}{"_discordantes" if args.solo_discordantes else ""}'

    for p0 in range(0, len(d), POR_PAGINA):
        bloque = d.iloc[p0:p0 + POR_PAGINA]
        fig, ejes = plt.subplots(4, 5, figsize=(20, 17))
        for ax in ejes.flat:
            ax.axis('off')
        for ax, (_, f) in zip(ejes.flat, bloque.iterrows()):
            ruta = next((root / 'data').rglob(f'{f["Caso"]}.nii*'))
            arr, zoom = cargar(ruta)
            i = int(np.clip(round(f['x_mid'] / zoom[0]), 0, arr.shape[0] - 1))
            sag = np.asarray(arr[i, :, :]).T
            del arr
            ax.imshow(np.clip(sag, -200, 1200), cmap='gray', origin='lower',
                      extent=(0, sag.shape[1] * zoom[1], 0, sag.shape[0] * zoom[2]))
            yc = f['S1_y_mm'] if pd.notna(f.get('S1_y_mm')) else sag.shape[1] * zoom[1] / 2
            zs = [v for v in (f.get('S1_z_mm'), f.get('z_s1_ala_mm')) if pd.notna(v)]
            zc = float(np.mean(zs)) if zs else sag.shape[0] * zoom[2] / 2
            if pd.notna(f.get('S1_z_mm')):
                ax.plot(f['S1_y_mm'], f['S1_z_mm'], 'r+', ms=16, mew=2)
                ax.add_patch(plt.Circle((f['S1_y_mm'], f['S1_z_mm']), 12, fill=False,
                                        ec='red', lw=1))
            if pd.notna(f.get('z_s1_ala_mm')):
                ax.axhline(f['z_s1_ala_mm'], color='yellow', ls='--', lw=1)
            ax.set_xlim(yc - 60, yc + 60)
            ax.set_ylim(zc - 60, zc + 60)
            disc = f.get('s1_discrepancia_mm')
            ax.set_title(f'{f["Caso"].replace("_data", "").replace("dataset", "d")}\n'
                         f'ala-sag = {disc:.0f} mm' if pd.notna(disc) else
                         f'{f["Caso"].replace("_data", "").replace("dataset", "d")}\nun metodo',
                         fontsize=10)
            ax.axis('on')
            ax.tick_params(labelsize=6)
        fig.suptitle('R1: cruz roja = S1 sagital (esfera 12 mm); linea amarilla = S1 por ala.'
                     ' Anterior a la derecha.', fontsize=12)
        fig.tight_layout()
        destino = out / f'mosaico_{sufijo}_{p0 // POR_PAGINA + 1:02d}.png'
        fig.savefig(destino, dpi=55)
        plt.close(fig)
        print(f'Escrito {destino}', flush=True)


if __name__ == '__main__':
    main()
