"""Tabla de sensibilidad del cribado HU a 1500 / 2500 / 3500 (implicancia #22).

Recuenta la cohorte local a los tres umbrales y reporta cuantos volumenes cambian
de clase `Candidato HU`. Solo lee `data/`; escribe `sensibilidad_hu.csv` y
`sensibilidad_hu.md`. NO toca `revision.csv`.
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import nibabel as nib
import numpy as np

THRESHOLDS: tuple[int, ...] = (1500, 2500, 3500)


def read_csv(path: Path) -> list[dict]:
    """Lee un CSV UTF-8 con BOM y devuelve sus filas como diccionarios."""
    if not path.exists():
        return []
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def scan(data: Path, revision: Path, out: Path) -> None:
    """Cuenta voxeles sobre cada umbral en cada CT y escribe la tabla."""
    previous = {r['Caso']: r for r in read_csv(revision)}
    paths = sorted(data.rglob('*_data.nii*'))
    if not paths:
        raise SystemExit('No se encontraron CT *_data.nii[.gz]. No se escribio nada.')
    rows: list[dict] = []
    for i, path in enumerate(paths):
        case = path.name.split('.nii')[0]
        prev = previous.get(case, {})
        row: dict[str, object] = {
            'Caso': case,
            'Dataset': path.name.split('_')[0],
            'Metal (revision)': prev.get('Metal', ''),
            'Objeto extraño (revision)': prev.get('Objeto extraño', ''),
            'Grupo duplicado': prev.get('Grupo duplicado', ''),
            'Cohorte propuesta': prev.get('Cohorte propuesta', ''),
        }
        try:
            img = nib.load(path)
            data_arr = img.get_fdata(dtype=np.float32)
            voxel_mm3 = float(np.prod(img.header.get_zooms()[:3]))
            row['HU máximo'] = float(data_arr.max())
            row['Voxel mm3'] = round(voxel_mm3, 6)
            for threshold in THRESHOLDS:
                count = int(np.count_nonzero(data_arr > threshold))
                row[f'Vox > {threshold}'] = count
                row[f'mm3 > {threshold}'] = round(count * voxel_mm3, 3)
                row[f'Candidato {threshold}'] = 'sí' if count else 'no'
            del data_arr
        except Exception as exc:  # noqa: BLE001 - se registra y se sigue
            row['Error'] = str(exc)
        rows.append(row)
        print(f'{i + 1}/{len(paths)} {case}: '
              + ' '.join(f'{t}={row.get(f"Vox > {t}", "ERR")}' for t in THRESHOLDS), flush=True)

    fields = ['Caso', 'Dataset', 'HU máximo', 'Voxel mm3']
    for threshold in THRESHOLDS:
        fields += [f'Vox > {threshold}', f'mm3 > {threshold}', f'Candidato {threshold}']
    fields += ['Metal (revision)', 'Objeto extraño (revision)', 'Grupo duplicado',
               'Cohorte propuesta', 'Error']
    with (out / 'sensibilidad_hu.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    report(rows, out)


def report(rows: list[dict], out: Path) -> None:
    """Escribe el resumen en Markdown de la tabla de sensibilidad."""
    ok = [r for r in rows if not r.get('Error')]
    lines = ['# Sensibilidad del cribado HU (implicancia #22)', '',
             f'Volumenes leidos: {len(rows)}; con error: {len(rows) - len(ok)}.',
             'Fuente: `data/` local. No modifica `revision.csv`.', '',
             '## Candidatos por umbral', '',
             '| Dataset | n | ' + ' | '.join(f'cand. {t} HU' for t in THRESHOLDS) + ' |',
             '|---|---:|' + '---:|' * len(THRESHOLDS)]
    for dataset in sorted({r['Dataset'] for r in ok}):
        group = [r for r in ok if r['Dataset'] == dataset]
        counts = [sum(r[f'Candidato {t}'] == 'sí' for r in group) for t in THRESHOLDS]
        lines.append(f'| {dataset} | {len(group)} | ' + ' | '.join(map(str, counts)) + ' |')
    total = [sum(r[f'Candidato {t}'] == 'sí' for r in ok) for t in THRESHOLDS]
    lines.append(f'| **total** | {len(ok)} | ' + ' | '.join(f'**{c}**' for c in total) + ' |')

    lines += ['', '## Cambios de clase', '']
    for low, high in zip(THRESHOLDS, THRESHOLDS[1:]):
        changed = [r for r in ok if r[f'Candidato {low}'] == 'sí' and r[f'Candidato {high}'] == 'no']
        lines.append(f'- De {low} a {high} HU dejan de ser candidatos **{len(changed)}** volumenes.')
        for r in changed:
            lines.append(f'  - `{r["Caso"]}` (mm3 > {low}: {r[f"mm3 > {low}"]}; '
                         f'Metal en revision: {r["Metal (revision)"] or "sin dato"})')

    lines += ['', '## Contraste con la revision 3D de la autora', '',
              '| Umbral | candidatos | Metal=sí y candidato | Metal=sí y NO candidato |',
              '|---:|---:|---:|---:|']
    for threshold in THRESHOLDS:
        cand = [r for r in ok if r[f'Candidato {threshold}'] == 'sí']
        metal = [r for r in ok if r['Metal (revision)'] == 'sí']
        missed = [r for r in metal if r[f'Candidato {threshold}'] == 'no']
        lines.append(f'| {threshold} | {len(cand)} | {len(metal) - len(missed)} | {len(missed)} |')

    lines += ['', '## Cohortes de entrenamiento limpias por umbral', '',
              'Limpio = no candidato al umbral. No sustituye la revision visual.', '',
              '| Umbral | limpios dataset6 | limpios dataset7 | limpios total |',
              '|---:|---:|---:|---:|']
    for threshold in THRESHOLDS:
        per = Counter(r['Dataset'] for r in ok if r[f'Candidato {threshold}'] == 'no')
        lines.append(f'| {threshold} | {per.get("dataset6", 0)} | {per.get("dataset7", 0)} '
                     f'| {sum(per.values())} |')
    (out / 'sensibilidad_hu.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> None:
    """Punto de entrada de linea de comandos."""
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=root / 'data')
    parser.add_argument('--revision', type=Path, default=Path(__file__).parent / 'revision.csv')
    parser.add_argument('--out', type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    scan(args.data, args.revision, args.out)


if __name__ == '__main__':
    main()
