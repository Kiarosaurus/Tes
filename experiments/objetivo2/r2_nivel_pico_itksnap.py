"""R2 / #121 — posicion del pico inferior del perfil de corredor, para juzgar su nivel en ITK-SNAP.

POR QUE
-------
`e9ts_corredor.csv` trae `pico_inf_z_rel_mm`, la altura del segundo maximo del perfil de diametro de
corredor por debajo de S1. El plan de cierre de #121 supone que ese pico **es S2**, pero eso es una
inferencia geometrica: TotalSegmentator `total` etiqueta `vertebrae_S1` y el **sacro entero**, y **no
hay etiqueta de S2**. En la cohorte del Objetivo 2 el pico cae entre -45.6 y -24.0 mm de S1 (p10-p90),
un rango ancho para un solo nivel vertebral. Antes de llamarlo S2 en la tesis, hay que verificarlo.

Este script **no verifica nada**: prepara la planilla para que lo haga el revisor clinico, con el mismo
procedimiento que ya se uso para confirmar el nivel de S1 (`r1_cortes_itksnap.py`, #53), que el revisor
ya conoce.

CIEGO, Y ESO IMPORTA
--------------------
La planilla **no** dice cual es la respuesta esperada. No lleva `pico_inf_z_rel_mm`, ni el corte de S1,
ni ningun juicio previo. Si llevara "este corte esta 30 mm por debajo de S1", la pregunta se contestaria
sola y la verificacion no valdria nada.

MUESTRA
-------
De los casos de la cohorte del Objetivo 2 (grupos 2 y 3, con QC de nivel) que tienen pico inferior, se
toman `--por-estrato` casos de cada **tercil de la profundidad del pico**. Estratificado a proposito:
si la inferencia falla en algun sitio, sera en los extremos del rango, y una muestra aleatoria simple
los cubriria mal. Semilla fija.

QUE ESCRIBE
-----------
`r2_nivel_pico_itksnap.csv`, una fila por caso, con el corte axial del pico en el **archivo original**
(desde 0 y desde 1), la posicion en mundo, y el HU del voxel para comprobar la convencion de indices,
igual que en R1.

Lee `e9ts_corredor.csv`, `r1_landmarks.csv` y los CT de `data/`. Solo lectura.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd

from r1_cortes_itksnap import a_original
from r1_landmarks import cargar

PLANOS = {0: 'sagital', 1: 'coronal', 2: 'axial'}
SEMILLA = 20260922


def cohorte(here: Path) -> pd.DataFrame:
    """Cohorte del Objetivo 2 con pico inferior medido."""
    e9 = pd.read_csv(here / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
    e9 = e9[(e9.estado_TS == 'concordante') & (e9.S1_toca_fov.isna())]
    e9 = e9[e9.Grupo.isin(['grupo 2', 'grupo 3'])].drop_duplicates('Caso').set_index('Caso')
    return e9[e9.pico_inf_z_rel_mm.notna()]


def muestra(d: pd.DataFrame, por_estrato: int) -> list[str]:
    """`por_estrato` casos de cada tercil de profundidad del pico. Semilla fija."""
    rng = np.random.default_rng(SEMILLA)
    tercil = pd.qcut(d.pico_inf_z_rel_mm, 3, labels=['profundo', 'medio', 'superficial'])
    elegidos: list[str] = []
    for etiqueta in ('profundo', 'medio', 'superficial'):
        casos = sorted(d.index[tercil == etiqueta])
        n = min(por_estrato, len(casos))
        elegidos += list(rng.choice(casos, size=n, replace=False))
    return sorted(elegidos)


def main() -> None:
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--por-estrato', type=int, default=6)
    parser.add_argument('--out', type=Path, default=here / 'r2_nivel_pico_itksnap.csv')
    args = parser.parse_args()

    d = cohorte(here)
    r1 = pd.read_csv(here / 'r1_landmarks.csv').set_index('Caso')
    rutas = {p.name[:-len('.nii.gz')]: p for p in (root / 'data').rglob('dataset*.nii.gz')}
    casos = muestra(d, args.por_estrato)
    print(f'cohorte con pico inferior: {len(d)} casos; muestra: {len(casos)}')

    filas = []
    for caso in casos:
        f = r1.loc[caso]
        z_pico_mm = float(f['S1_z_mm']) + float(d.loc[caso, 'pico_inf_z_rel_mm'])
        img = nib.load(rutas[caso])
        forma = img.shape[:3]
        ornt = nib.orientations.io_orientation(img.affine)
        zoom = np.array(img.header.get_zooms()[:3], dtype=np.float32)[np.argsort(ornt[:, 0]).astype(int)]
        # Mismo sagital y coronal que el punto de S1, a la altura del pico: define un voxel concreto
        # sobre el que comprobar la convencion de indices, sin revelar nada del nivel.
        r = np.rint(np.array([f['S1_x_mm'], f['S1_y_mm'], z_pico_mm]) / zoom).astype(int)
        r = np.clip(r, 1, np.array(forma)[np.argsort(ornt[:, 0]).astype(int)] - 2)
        o = a_original(r, ornt, forma)

        arr, _ = cargar(rutas[caso])
        hu_ras = int(arr[tuple(r)])
        vecinos = np.asarray(arr[r[0] - 1:r[0] + 2, r[1] - 1:r[1] + 2, r[2] - 1:r[2] + 2])
        del arr
        hu_orig = int(np.clip(np.rint(np.asanyarray(img.dataobj[o[0], o[1], o[2]])), -32768, 32767))
        if hu_ras != hu_orig:
            raise SystemExit(f'{caso}: HU RAS {hu_ras} != original {hu_orig}; conversion de indices mal')

        eje_archivo = {int(ornt[k, 0]): k for k in range(3)}
        fila = {'Caso': caso, 'Archivo': rutas[caso].relative_to(root).as_posix(),
                'forma_archivo': f'{forma[0]} {forma[1]} {forma[2]}'}
        for a, plano in PLANOS.items():
            fila[f'corte_{plano}'] = int(o[eje_archivo[a]])
            fila[f'corte_{plano}_1'] = int(o[eje_archivo[a]]) + 1
        mundo = img.affine @ np.append(o, 1.0)
        fila.update({'voxel_ijk_0': f'{o[0]} {o[1]} {o[2]}',
                     'mundo_RAS_mm': f'{mundo[0]:.1f} {mundo[1]:.1f} {mundo[2]:.1f}',
                     'mundo_LPS_mm': f'{-mundo[0]:.1f} {-mundo[1]:.1f} {mundo[2]:.1f}',
                     'HU_voxel': hu_orig, 'HU_mediana_3x3x3': float(np.median(vecinos)),
                     'convencion_indices': '', 'HU_cursor': '',
                     'nivel_del_corte': '', 'vertebra_transicion': '', 'legible': '', 'comentario': ''})
        filas.append(fila)
        print(f'{caso}: axial {fila["corte_axial"]} (desde 0); HU {hu_orig}', flush=True)

    campos = ['Caso', 'Archivo', 'forma_archivo', 'corte_sagital', 'corte_coronal', 'corte_axial',
              'corte_sagital_1', 'corte_coronal_1', 'corte_axial_1', 'voxel_ijk_0', 'mundo_RAS_mm',
              'mundo_LPS_mm', 'HU_voxel', 'HU_mediana_3x3x3', 'convencion_indices', 'HU_cursor',
              'nivel_del_corte', 'vertebra_transicion', 'legible', 'comentario']
    pd.DataFrame(filas).reindex(columns=campos).to_csv(args.out, index=False)
    print(f'{len(filas)} casos -> {args.out}')


if __name__ == '__main__':
    main()
