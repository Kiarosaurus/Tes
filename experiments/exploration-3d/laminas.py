"""Laminas PNG deterministas por caso, para clasificacion visual preliminar.

No decide nada: solo renderiza vistas reproducibles y mide los componentes
por encima de un umbral HU. Candidato HU no equivale a metal confirmado.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import nibabel as nib  # noqa: E402
import numpy as np  # noqa: E402
from skimage.measure import label  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PLANES = ('Sagital (A->, S^)', 'Coronal (R->, S^)', 'Axial (R->, A^)')
HUESO = (-200, 2000)
METAL = (500, 4000)


def locate(case: str, data: Path) -> Path:
    """Encuentra el NIfTI del caso; falla si no es exactamente uno."""
    paths = sorted(data.rglob(f'{case}.nii*'))
    if len(paths) != 1:
        raise SystemExit(f'Se esperaba un unico archivo para {case}; hay {len(paths)}.')
    return paths[0]


def components(mask: np.ndarray, volume: np.ndarray, affine: np.ndarray,
               spacing: np.ndarray, minimum: int) -> list[dict]:
    """Mide componentes conexos del umbral, ordenados por tamano."""
    labels, count = label(mask, connectivity=1, return_num=True)
    if not count:
        return []
    coordinates = np.argwhere(labels)
    identifiers = labels[tuple(coordinates.T)]
    order = np.argsort(identifiers, kind='stable')
    coordinates, identifiers = coordinates[order], identifiers[order]
    intensities = volume[tuple(coordinates.T)]
    starts = np.concatenate(([0], np.cumsum(np.bincount(identifiers, minlength=count + 1)[1:])))
    found = []
    for index in range(1, count + 1):
        ijk = coordinates[starts[index - 1]:starts[index]]
        if len(ijk) < minimum:
            continue
        low, high = ijk.min(0), ijk.max(0)
        centre = ijk.mean(0)
        ras = nib.affines.apply_affine(affine, centre)
        found.append({
            'voxeles': int(len(ijk)),
            'volumen_mm3': round(float(len(ijk) * np.prod(spacing)), 2),
            'hu_max': round(float(intensities[starts[index - 1]:starts[index]].max()), 1),
            'centroide_ijk': [int(round(v)) for v in centre],
            'centroide_ras_mm': [round(float(v), 1) for v in ras],
            'lado_por_x_ras': 'derecha' if ras[0] > 5 else 'izquierda' if ras[0] < -5 else 'central',
            'bbox_mm': [round(float((high[a] - low[a] + 1) * spacing[a]), 1) for a in range(3)],
            'cortes_axiales_ijk': [int(low[2]), int(high[2])],
            'toca_borde_fov': bool((low == 0).any() or (high == np.array(mask.shape) - 1).any()),
        })
    return sorted(found, key=lambda item: item['voxeles'], reverse=True)


def draw(volume: np.ndarray, mask: np.ndarray, spacing: np.ndarray,
         case: str, out: Path, hu: float) -> None:
    """Escribe proyecciones, ortogonales y una malla de cortes axiales."""
    aspect = [spacing[[j for j in range(3) if j != a][1]] / spacing[[j for j in range(3) if j != a][0]]
              for a in range(3)]
    figure, axes = plt.subplots(2, 3, figsize=(15, 9))
    for axis in range(3):
        axes[0, axis].imshow(volume.max(axis=axis).T, origin='lower', cmap='gray',
                             vmin=METAL[0], vmax=METAL[1], aspect=aspect[axis])
        axes[0, axis].set_title(f'MIP {PLANES[axis]}')
        axes[1, axis].imshow(mask.sum(axis=axis).T, origin='lower', cmap='inferno',
                             aspect=aspect[axis])
        axes[1, axis].set_title(f'Voxeles > {hu:g} HU acumulados')
    figure.suptitle(f'{case} — proyecciones; ejes en indices de voxel RAS. '
                    'Densidad alta no implica metal')
    figure.tight_layout()
    figure.savefig(out / 'proyecciones.png', dpi=110)
    plt.close(figure)

    ijk = (np.argwhere(mask).mean(0).round().astype(int) if mask.any()
           else (np.array(volume.shape) // 2))
    figure, axes = plt.subplots(2, 3, figsize=(15, 9))
    for axis in range(3):
        plane = np.take(volume, int(ijk[axis]), axis=axis).T
        overlay = np.ma.masked_where(~np.take(mask, int(ijk[axis]), axis=axis).T,
                                     np.ones_like(plane))
        for row, (low, high) in enumerate((HUESO, METAL)):
            axes[row, axis].imshow(plane, origin='lower', cmap='gray',
                                   vmin=low, vmax=high, aspect=aspect[axis])
            axes[row, axis].imshow(overlay, origin='lower', cmap='autumn',
                                   alpha=.45, aspect=aspect[axis])
            axes[row, axis].set_title(f'{PLANES[axis]} {ijk[axis]} — ventana {low}/{high}')
    figure.suptitle(f'{case} — ortogonales por el centroide del umbral (indices RAS, base 0)')
    figure.tight_layout()
    figure.savefig(out / 'ortogonales.png', dpi=110)
    plt.close(figure)

    zs = np.argwhere(mask.any(axis=(0, 1))).ravel()
    span = (int(zs.min()), int(zs.max())) if zs.size else (0, volume.shape[2] - 1)
    indices = np.unique(np.linspace(max(span[0] - 5, 0),
                                    min(span[1] + 5, volume.shape[2] - 1), 16).astype(int))
    figure, axes = plt.subplots(4, 4, figsize=(14, 14))
    for ax, index in zip(axes.ravel(), indices):
        ax.imshow(volume[:, :, index].T, origin='lower', cmap='gray',
                  vmin=HUESO[0], vmax=HUESO[1], aspect=aspect[2])
        ax.imshow(np.ma.masked_where(~mask[:, :, index].T, np.ones(mask.shape[:2]).T),
                  origin='lower', cmap='autumn', alpha=.45, aspect=aspect[2])
        ax.set_title(f'axial {index}', fontsize=9)
    for ax in axes.ravel()[len(indices):]:
        ax.axis('off')
    figure.suptitle(f'{case} — axiales {indices[0]}-{indices[-1]}; no recorre todo el CT')
    figure.tight_layout()
    figure.savefig(out / 'axiales.png', dpi=100)
    plt.close(figure)


def sheet(case: str, args: argparse.Namespace) -> dict:
    """Genera laminas y hallazgos medibles de un caso."""
    path = locate(case, args.data)
    original = nib.load(path)
    if original.header.get_xyzt_units()[0] != 'mm':
        raise SystemExit(f'{case}: unidades espaciales no declaradas en mm; '
                         'los tamanos en mm serian falsos.')
    img = nib.as_closest_canonical(original)
    volume = img.get_fdata(dtype=np.float32)
    spacing = nib.affines.voxel_sizes(img.affine)
    mask = volume > args.hu
    out = args.out / 'outputs' / 'laminas' / case
    out.mkdir(parents=True, exist_ok=True)
    draw(volume, mask, spacing, case, out, args.hu)
    facts = {
        'caso': case,
        'archivo': path.relative_to(args.data).as_posix(),
        'umbral_hu': args.hu,
        'minimo_voxeles_componente': args.min,
        'hu_max_volumen': round(float(volume.max()), 1),
        'voxeles_sobre_umbral': int(mask.sum()),
        'spacing_mm': [round(float(v), 4) for v in spacing],
        'dimensiones': [int(v) for v in volume.shape],
        'componentes': components(mask, volume, img.affine, spacing, args.min)[:12],
        'laminas': sorted(p.name for p in out.glob('*.png')),
        'advertencia': ('Umbral e indices son medidas, no diagnostico. No establece '
                        'composicion quimica, modelo del dispositivo ni ausencia de objetos.'),
    }
    (out / 'hallazgos.json').write_text(json.dumps(facts, ensure_ascii=False, indent=2),
                                        encoding='utf-8')
    return facts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('casos', nargs='+', help='identificadores de revision.csv')
    parser.add_argument('--data', type=Path, default=ROOT / 'data')
    parser.add_argument('--out', type=Path, default=HERE)
    parser.add_argument('--hu', type=float, default=2500)
    parser.add_argument('--min', type=int, default=5, help='voxeles minimos por componente')
    args = parser.parse_args()
    for case in args.casos:
        facts = sheet(case, args)
        print(json.dumps(facts, ensure_ascii=False))


if __name__ == '__main__':
    main()
