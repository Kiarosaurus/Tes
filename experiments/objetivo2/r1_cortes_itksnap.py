"""R1 / #53 — posicion exacta del punto de S1 de R1 en cada CT, para abrirla en ITK-SNAP.

POR QUE
-------
El revisor clinico juzgo el nivel de S1 sobre un mosaico sagital de +-60 mm (#53, Hallazgo 1), que no
permite contar vertebras. El 2026-09-14 pidio el corte exacto de cada punto para verlo en el volumen
completo con ITK-SNAP. Este script da esa posicion **en el archivo original**, no en el marco RAS
reorientado donde trabajan R1, E8, E9b y TS.

QUE ESCRIBE (`r1_cortes_itksnap.csv`, una fila por caso de evaluacion)
---------------------------------------------------------------------
- `Archivo`: ruta relativa al repositorio.
- `corte_sagital`, `corte_coronal`, `corte_axial`: indice de corte del punto de S1 (la cruz roja del
  mosaico) en cada plano, **contando desde 0** y, en las columnas `_1`, **desde 1**. No se verifico cual
  de las dos convenciones muestra ITK-SNAP: por eso van ambas y la comprobacion por HU.
- `voxel_ijk_0` / `voxel_ijk_1`: el mismo punto como (i, j, k) en el orden de ejes del archivo.
- `mundo_RAS_mm` (affine NIfTI, convencion de nibabel) y `mundo_LPS_mm` (= -x, -y, z). No se verifico
  cual muestra ITK-SNAP.
- `HU_voxel` y `HU_mediana_3x3x3`: **comprobacion**. Si el cursor de ITK-SNAP no marca ese HU en ese
  voxel, la convencion de indices es la otra.
- `corte_axial_linea_ala_0/_1`: corte axial de la linea amarilla del mosaico (S1 por el metodo del ala).

Ciego: no incluye ningun juicio (clinico, agente ni TS). Comprobacion interna: el HU leido en el marco
RAS de `cargar` debe ser igual al leido en el archivo original en el indice calculado; si no, aborta.

Lee `r1_landmarks.csv`, `r1_estados.csv` y los CT de `data/`. Solo lectura.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd

from r1_landmarks import cargar

PLANOS = {0: 'sagital', 1: 'coronal', 2: 'axial'}  # eje RAS de `cargar` -> plano que corta


def a_original(r: np.ndarray, ornt: np.ndarray, forma: tuple[int, ...]) -> np.ndarray:
    """Indice en el array reorientado a RAS -> indice en el archivo original."""
    out = np.empty(3, dtype=int)
    for k in range(3):
        a = int(ornt[k, 0])
        out[k] = r[a] if ornt[k, 1] > 0 else forma[k] - 1 - r[a]
    return out


def main() -> None:
    """Calcula la tabla y la escribe."""
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, default=here / 'r1_cortes_itksnap.csv')
    args = parser.parse_args()

    r1 = pd.read_csv(here / 'r1_landmarks.csv').set_index('Caso')
    est = pd.read_csv(here / 'r1_estados.csv').set_index('Caso')
    casos = sorted(est.index[est['cohorte'] == 'evaluacion'])
    rutas = {p.name[:-len('.nii.gz')]: p for p in (root / 'data').rglob('dataset*.nii.gz')}
    filas = []
    for caso in casos:
        f = r1.loc[caso]
        fila = {'Caso': caso, 'Archivo': rutas[caso].relative_to(root).as_posix() if caso in rutas else ''}
        if f['S1_hallado'] != 'si' or caso not in rutas:
            fila['nota'] = 'sin punto de S1 en R1 (no hay cruz roja)'
            filas.append(fila)
            continue
        img = nib.load(rutas[caso])
        forma = img.shape[:3]
        ornt = nib.orientations.io_orientation(img.affine)
        zoom = np.array(img.header.get_zooms()[:3], dtype=np.float32)[np.argsort(ornt[:, 0]).astype(int)]
        r = np.rint(np.array([f['S1_x_mm'], f['S1_y_mm'], f['S1_z_mm']]) / zoom).astype(int)
        o = a_original(r, ornt, forma)

        arr, _ = cargar(rutas[caso])
        hu_ras = int(arr[tuple(r)])
        vecinos = np.asarray(arr[r[0] - 1:r[0] + 2, r[1] - 1:r[1] + 2, r[2] - 1:r[2] + 2])
        del arr
        hu_orig = int(np.clip(np.rint(np.asanyarray(img.dataobj[o[0], o[1], o[2]])), -32768, 32767))
        if hu_ras != hu_orig:
            raise SystemExit(f'{caso}: HU RAS {hu_ras} != HU original {hu_orig}; conversion de indices mal')

        eje_archivo = {int(ornt[k, 0]): k for k in range(3)}  # eje RAS -> eje del archivo
        for a, plano in PLANOS.items():
            fila[f'corte_{plano}'] = int(o[eje_archivo[a]])
            fila[f'corte_{plano}_1'] = int(o[eje_archivo[a]]) + 1
            fila[f'eje_archivo_{plano}'] = eje_archivo[a]
        mundo = img.affine @ np.append(o, 1.0)
        fila.update({'voxel_ijk_0': f'{o[0]} {o[1]} {o[2]}', 'voxel_ijk_1': f'{o[0] + 1} {o[1] + 1} {o[2] + 1}',
                     'forma_archivo': f'{forma[0]} {forma[1]} {forma[2]}',
                     'mundo_RAS_mm': f'{mundo[0]:.1f} {mundo[1]:.1f} {mundo[2]:.1f}',
                     'mundo_LPS_mm': f'{-mundo[0]:.1f} {-mundo[1]:.1f} {mundo[2]:.1f}',
                     'HU_voxel': hu_orig, 'HU_mediana_3x3x3': float(np.median(vecinos))})
        if np.isfinite(f['z_s1_ala_mm']):
            rz = int(np.rint(f['z_s1_ala_mm'] / zoom[2]))
            k = eje_archivo[2]
            kz = rz if ornt[k, 1] > 0 else forma[k] - 1 - rz
            fila.update({'corte_axial_linea_ala': kz, 'corte_axial_linea_ala_1': kz + 1})
        filas.append(fila)
        print(f'{caso}: sagital {fila["corte_sagital"]}, coronal {fila["corte_coronal"]}, '
              f'axial {fila["corte_axial"]} (desde 0); HU {hu_orig}', flush=True)

    campos = ['Caso', 'Archivo', 'forma_archivo', 'corte_sagital', 'corte_coronal', 'corte_axial',
              'corte_sagital_1', 'corte_coronal_1', 'corte_axial_1', 'voxel_ijk_0', 'voxel_ijk_1',
              'eje_archivo_sagital', 'eje_archivo_coronal', 'eje_archivo_axial', 'mundo_RAS_mm', 'mundo_LPS_mm',
              'HU_voxel', 'HU_mediana_3x3x3', 'corte_axial_linea_ala', 'corte_axial_linea_ala_1', 'nota']
    pd.DataFrame(filas).reindex(columns=campos).to_csv(args.out, index=False)
    print(f'{len(filas)} casos -> {args.out}')


if __name__ == '__main__':
    main()
