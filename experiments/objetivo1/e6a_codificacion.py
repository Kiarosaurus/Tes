"""E6a — Go/No-Go del Objetivo 1, parte SIN VAE: la codificacion multi-ventana sola.

`tesis/main.tex` (Obj 1) exige MAE < 25 HU en hueso para el viaje
HU -> multi-ventana -> VAE -> HU. Este experimento mide **solo el primer y el ultimo
tramo**: HU -> ventana -> HU. No necesita VAE ni entrenamiento, y da una **cota inferior
asumible por cualquier decodificador**: ningun VAE puede recuperar informacion que el
recorte de ventana ya destruyo.

Ventanas de `docs/03-glosario.md` (`wang2025adaptiveweighting`, Sec. V-A-1, p. 2412):
LW [-1000, 2000], MW [-320, 480], SW [-160, 240] HU. Normalizacion Eq. 2, p. 2410.

ROI oseo: HU > 150, el umbral de bone integrity de `peters2025hybrid` (implicancia #14).
Se reporta tambien HU > 2500 (ROI de metal segun el cribado vigente) porque es donde el
recorte muerde.

Solo lee `data/`. Escribe `e6a_codificacion.csv` y `e6a_codificacion.md`.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import nibabel as nib
import numpy as np

WINDOWS: dict[str, tuple[float, float]] = {
    'LW': (-1000.0, 2000.0),
    'MW': (-320.0, 480.0),
    'SW': (-160.0, 240.0),
}
BITS: tuple[int | None, ...] = (None, 16, 8)
BONE_HU = 150.0
METAL_HU = 2500.0


def roundtrip(values: np.ndarray, low: float, high: float, bits: int | None) -> np.ndarray:
    """Recorta a [low, high], normaliza, cuantiza y vuelve a HU."""
    clipped = np.clip(values, low, high)
    norm = (clipped - low) / (high - low)
    if bits is not None:
        levels = 2 ** bits - 1
        norm = np.rint(norm * levels) / levels
    return norm * (high - low) + low


def label(bits: int | None) -> str:
    """Nombre corto de la profundidad de cuantizacion."""
    return 'float' if bits is None else f'{bits}b'


def measure(values: np.ndarray) -> dict[str, float]:
    """MAE por ventana y profundidad, mas la cota del decodificador oraculo."""
    out: dict[str, float] = {}
    if values.size == 0:
        return out
    for bits in BITS:
        errors = []
        for name, (low, high) in WINDOWS.items():
            err = np.abs(roundtrip(values, low, high, bits) - values)
            out[f'MAE {name} {label(bits)}'] = float(err.mean())
            errors.append(err)
        # Oraculo: por voxel, el mejor de los tres canales. Cota inferior de cualquier
        # decodificador multicanal, incluido un VAE perfecto.
        out[f'MAE oraculo {label(bits)}'] = float(np.min(np.stack(errors), axis=0).mean())
    return out


def scan(data: Path, out: Path) -> None:
    """Recorre los CT y escribe la tabla por volumen."""
    paths = sorted(data.rglob('*_data.nii*'))
    if not paths:
        raise SystemExit('No se encontraron CT *_data.nii[.gz]. No se escribio nada.')
    rows: list[dict] = []
    for i, path in enumerate(paths):
        case = path.name.split('.nii')[0]
        row: dict[str, object] = {'Caso': case, 'Dataset': path.name.split('_')[0]}
        try:
            arr = nib.load(path).get_fdata(dtype=np.float32)
            row['HU máximo'] = float(arr.max())
            bone = arr[arr > BONE_HU]
            metal = arr[arr > METAL_HU]
            row['n hueso'] = int(bone.size)
            row['n metal'] = int(metal.size)
            row['frac hueso > 2000 HU'] = float((bone > 2000.0).mean()) if bone.size else 0.0
            for key, value in measure(bone).items():
                row[f'{key} (hueso)'] = round(value, 4)
            for key, value in measure(metal).items():
                row[f'{key} (metal)'] = round(value, 4)
            del arr, bone, metal
        except Exception as exc:  # noqa: BLE001 - se registra y se sigue
            row['Error'] = str(exc)
        rows.append(row)
        print(f'{i + 1}/{len(paths)} {case}: '
              f'oraculo hueso float = {row.get("MAE oraculo float (hueso)", "ERR")} HU',
              flush=True)

    fields: list[str] = ['Caso', 'Dataset', 'HU máximo', 'n hueso', 'n metal',
                         'frac hueso > 2000 HU']
    for roi in ('hueso', 'metal'):
        for bits in BITS:
            for name in [*WINDOWS, 'oraculo']:
                fields.append(f'MAE {name} {label(bits)} ({roi})')
    fields.append('Error')
    with (out / 'e6a_codificacion.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    report(rows, out)


def report(rows: list[dict], out: Path) -> None:
    """Resumen en Markdown, con el veredicto Go/No-Go frente al umbral de 25 HU."""
    ok = [r for r in rows if not r.get('Error')]
    lines = ['# E6a — codificacion multi-ventana sola (Objetivo 1, Go/No-Go)', '',
             f'Volumenes leidos: {len(rows)}; con error: {len(rows) - len(ok)}.',
             f'ROI oseo: HU > {BONE_HU:.0f} (bone integrity de `peters2025hybrid`).',
             f'ROI metal: HU > {METAL_HU:.0f}.',
             'Ventanas LW [-1000, 2000], MW [-320, 480], SW [-160, 240] HU.',
             'Sin VAE: esto es una **cota inferior** del error del sistema completo.', '']

    for roi in ('hueso', 'metal'):
        lines += [f'## MAE en ROI de {roi} — mediana [min-max] sobre la cohorte', '',
                  '| Profundidad | ' + ' | '.join([*WINDOWS, 'oraculo']) + ' |',
                  '|---|' + '---|' * (len(WINDOWS) + 1)]
        for bits in BITS:
            cells = []
            for name in [*WINDOWS, 'oraculo']:
                vals = [r[f'MAE {name} {label(bits)} ({roi})'] for r in ok
                        if f'MAE {name} {label(bits)} ({roi})' in r]
                cells.append(f'{np.median(vals):.2f} [{min(vals):.2f}-{max(vals):.2f}]'
                             if vals else 'sin datos')
            lines.append(f'| {label(bits)} | ' + ' | '.join(cells) + ' |')
        lines.append('')

    lines += ['## Veredicto frente al umbral de 25 HU en hueso', '']
    for bits in BITS:
        key = f'MAE oraculo {label(bits)} (hueso)'
        vals = [r[key] for r in ok if key in r]
        if not vals:
            continue
        fails = sum(v >= 25.0 for v in vals)
        lines.append(f'- **{label(bits)}**: la cota del oraculo supera 25 HU en '
                     f'**{fails} de {len(vals)}** volumenes '
                     f'(mediana {np.median(vals):.2f} HU).')
    lines += ['', '## Recorte: fraccion de voxeles oseos sobre el techo de LW (2000 HU)', '']
    for dataset in sorted({r['Dataset'] for r in ok}):
        vals = [r['frac hueso > 2000 HU'] for r in ok if r['Dataset'] == dataset]
        lines.append(f'- {dataset}: mediana {np.median(vals) * 100:.4f}%, '
                     f'maximo {max(vals) * 100:.4f}%.')
    lines += ['', 'Ningun decodificador recupera un voxel recortado en las tres ventanas.',
              'La cota del oraculo asume un decodificador que elige el mejor canal por voxel;',
              'un VAE real solo puede empeorarla.']
    (out / 'e6a_codificacion.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> None:
    """Punto de entrada de linea de comandos."""
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=root / 'data')
    parser.add_argument('--out', type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    scan(args.data, args.out)


if __name__ == '__main__':
    main()
