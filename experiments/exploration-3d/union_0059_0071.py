"""Union sin perdida de `metal_0059` y `metal_0071` (implicancia #45, autorizada 2026-09-10).

Los dos volumenes son el mismo escaneo exportado con dos FOV solapados: los cortes 0-215 de
`0059` son bit a bit iguales a los cortes 134-349 de `0071`, y el desfase de 134 cortes es
exactamente la diferencia de origen z del affine. La autora confirmo que son el mismo
paciente y autorizo la union.

Union = `0071[:, :, 0:350]` seguido de `0059[:, :, 216:288]` -> 422 cortes, affine de
`0071`. No se interpola nada: cada voxel del resultado es un voxel de un archivo original.

El script **aborta sin escribir** si falla cualquiera de estas comprobaciones: mismo dtype,
misma matriz de rotacion/escala del affine, mismo origen x/y, desfase z = 134 x dz, los 216
cortes del solape identicos, y la ida y vuelta (`union` recorta de nuevo a los dos
originales exactos).

Lee `data/dataset7`. Escribe `data/derivados/dataset7_CLINIC_metal_0059u0071_union.nii.gz`
(ignorado por git; el nombre NO encaja con `*_data.nii*`, a proposito, para que los scripts
que recorren `data/` no lo cuenten como volumen 179) y `union_0059_0071.md` con hashes.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import nibabel as nib
import numpy as np

DESFASE = 134
CORTES_0071 = 350
DESDE_0059 = 216


def sha(arr: np.ndarray) -> str:
    """SHA256 de forma + voxeles (mismo criterio que `Grupo duplicado`)."""
    h = hashlib.sha256(str(arr.shape).encode() + np.ascontiguousarray(arr).tobytes())
    return h.hexdigest()


def main() -> None:
    """Verifica, une y escribe."""
    root = Path(__file__).resolve().parents[2]
    d7 = root / 'data' / 'dataset7'
    i59 = nib.load(d7 / 'dataset7_CLINIC_metal_0059_data.nii.gz')
    i71 = nib.load(d7 / 'dataset7_CLINIC_metal_0071_data.nii.gz')
    a59, a71 = np.asanyarray(i59.dataobj), np.asanyarray(i71.dataobj)

    fallos: list[str] = []
    if a59.dtype != a71.dtype:
        fallos.append(f'dtype distinto: {a59.dtype} vs {a71.dtype}')
    if a59.shape[:2] != a71.shape[:2]:
        fallos.append(f'matriz en plano distinta: {a59.shape} vs {a71.shape}')
    if not np.allclose(i59.affine[:3, :3], i71.affine[:3, :3]):
        fallos.append('rotacion/escala del affine distinta')
    if not np.allclose(i59.affine[:2, 3], i71.affine[:2, 3]):
        fallos.append('origen x/y distinto')
    dz = float(i71.affine[2, 2])
    if not np.isclose(i59.affine[2, 3] - i71.affine[2, 3], DESFASE * dz, atol=1e-3):
        fallos.append(f'desfase z {i59.affine[2, 3] - i71.affine[2, 3]:.4f} != {DESFASE}*{dz}')
    if a71.shape[2] != CORTES_0071 or a59.shape[2] != DESDE_0059 + 72:
        fallos.append(f'numero de cortes inesperado: 0059={a59.shape[2]}, 0071={a71.shape[2]}')
    if not fallos:
        distintos = [k for k in range(DESDE_0059)
                     if not np.array_equal(a59[:, :, k], a71[:, :, k + DESFASE])]
        if distintos:
            fallos.append(f'{len(distintos)} cortes del solape difieren (p. ej. {distintos[:5]})')
    if fallos:
        raise SystemExit('ABORTADO, no se escribio nada:\n- ' + '\n- '.join(fallos))

    union = np.concatenate([a71[:, :, :CORTES_0071], a59[:, :, DESDE_0059:]], axis=2)
    if not (np.array_equal(union[:, :, :CORTES_0071], a71)
            and np.array_equal(union[:, :, DESFASE:], a59)):
        raise SystemExit('ABORTADO: la union no reproduce los dos originales.')

    cab = i71.header.copy()
    cab.set_data_shape(union.shape)
    cab.set_data_dtype(union.dtype)
    salida_dir = root / 'data' / 'derivados'
    salida_dir.mkdir(parents=True, exist_ok=True)
    salida = salida_dir / 'dataset7_CLINIC_metal_0059u0071_union.nii.gz'
    nib.save(nib.Nifti1Image(union, i71.affine, cab), salida)

    # Relectura desde disco: lo escrito es lo verificado.
    rel = nib.load(salida)
    releido = np.asanyarray(rel.dataobj)
    if not (np.array_equal(releido, union) and np.allclose(rel.affine, i71.affine)):
        salida.unlink()
        raise SystemExit('ABORTADO: la relectura no coincide; archivo borrado.')

    z0 = float(i71.affine[2, 3])
    lineas = [
        '# Union sin perdida `metal_0059` + `metal_0071` (#45)', '',
        'Generado por `union_0059_0071.py`. Autorizado por la autora el 2026-09-10.', '',
        '| | forma | origen z (mm) | SHA256 voxeles |', '|---|---|---|---|',
        f'| `metal_0071` | {a71.shape} | {z0:.3f} | `{sha(a71)[:16]}` |',
        f'| `metal_0059` | {a59.shape} | {float(i59.affine[2, 3]):.3f} | `{sha(a59)[:16]}` |',
        f'| union | {union.shape} | {z0:.3f} | `{sha(union)[:16]}` |', '',
        f'- Solape: cortes 0-{DESDE_0059 - 1} de `0059` = cortes {DESFASE}-{CORTES_0071 - 1} '
        f'de `0071`, {DESDE_0059} cortes identicos bit a bit.',
        f'- Union: cortes 0-{CORTES_0071 - 1} de `0071` + cortes {DESDE_0059}-'
        f'{a59.shape[2] - 1} de `0059`. Sin interpolacion.',
        '- Comprobado: dtype, affine (rotacion, escala, origen x/y, desfase z), solape, ida y '
        'vuelta a los dos originales, y relectura desde disco.',
        f'- Archivo: `data/derivados/{salida.name}` (no versionado; regenerable con el script).',
        '- **Los originales de `data/dataset7` no se tocaron.** En `revision.csv` las dos filas '
        'siguen existiendo; comparten `Grupo paciente`.',
    ]
    (Path(__file__).with_name('union_0059_0071.md')).write_text('\n'.join(lineas) + '\n',
                                                               encoding='utf-8')
    print('\n'.join(lineas))


if __name__ == '__main__':
    main()
