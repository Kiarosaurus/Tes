"""Inventario, superficies 3D y resumen; un CSV editable por volumen."""
from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path
from collections import Counter, defaultdict

import nibabel as nib
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MANUAL = ['Caso', 'Tipo de estructura observada', 'Cantidad aprox.',
          'Ubicación anatómica', 'Lateralidad', 'Artefactos', 'Severidad', 'Confianza',
          'Metal', 'Objeto extraño', 'Revisión 3D y cortes', 'Revisor', 'Fecha',
          'Notas', 'Ejemplo', 'Grupo paciente']
AUTO = ['Dataset', 'Archivo', 'Máscara local', 'Spacing x mm', 'Spacing y mm',
        'Spacing z mm', 'Dim x', 'Dim y', 'Dim z', 'HU mínimo', 'HU máximo',
        'Umbral HU', 'Vóxeles sobre umbral', 'Candidato HU', 'SHA256 vóxeles',
        'Grupo duplicado', 'Antecedente 2D', 'Cohorte propuesta', 'Error']


def read_csv(path: Path) -> list[dict]:
    """Lee también CSV editado por Excel con BOM."""
    if not path.exists():
        return []
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def save(rows: list[dict], out: Path) -> None:
    """Reemplaza atómicamente, sin borrar campos de revisión."""
    out.mkdir(parents=True, exist_ok=True)
    temp = out / 'revision.tmp'
    with temp.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=MANUAL + AUTO)
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(out / 'revision.csv')


def antecedents(rows: list[dict]) -> None:
    """Conserva observaciones previas y su procedencia, sin confirmarlas."""
    notes = defaultdict(list)
    for filename, fields in [('excluded_clinic_ids.csv', ['estado', 'notas']),
                             ('caracterizacion_metal_d7.csv', ['tipo', 'ortopedico', 'nota'])]:
        for old in read_csv(ROOT / 'experiments/exploration' / filename):
            text = '; '.join(f'{key}={old[key]}' for key in fields if old.get(key))
            if text:
                notes[old['file']].append(f'{filename}: {text}')
    notes['dataset7_CLINIC_metal_0002_data.nii.gz'].append(
        'Tabla compañera.jpeg: Tornillo de fijación | 1 dominante | Pelvis posterior / región sacroilíaca | Por determinar | Sí | Leve–moderada | Alta')
    notes['dataset7_CLINIC_metal_0003_data.nii.gz'].append(
        'Tabla compañera.jpeg: Placa con múltiples tornillos | Múltiples | Región pélvica posterior / ilíaca | Derecha, preliminar | Sí | Moderada | Media–alta')
    for row in rows:
        row['Antecedente 2D'] = ' || '.join(notes.get(Path(row['Archivo']).name, []))


def cohorts(rows: list[dict]) -> None:
    """Solo elegibilidad provisional: nunca asigna pendientes a entrenamiento."""
    groups = defaultdict(list)
    for row in rows:
        key = row['Grupo duplicado'] or row['Caso']
        groups[key].append(row)
    for row in rows:
        row['Cohorte propuesta'] = 'pendiente'
        if row['Error']:
            row['Cohorte propuesta'] = 'error'
            continue
        if row['Grupo duplicado']:
            row['Cohorte propuesta'] = 'resolver duplicado'
            continue
        if (row['Revisión 3D y cortes'] != 'completa' or not row['Revisor']
                or not row['Fecha'] or not row['Grupo paciente']):
            continue
        if row['Metal'] == 'sí':
            row['Cohorte propuesta'] = 'prueba metal candidata'
        elif row['Metal'] == 'no' and row['Objeto extraño'] == 'no':
            row['Cohorte propuesta'] = 'entrenamiento candidato'
        elif row['Objeto extraño'] == 'sí':
            row['Cohorte propuesta'] = 'excluir objeto extraño'
    patients = defaultdict(list)
    for row in rows:
        if row['Grupo paciente']:
            patients[row['Grupo paciente']].append(row)
    for group in patients.values():
        if len(group) > 1:
            for row in group:
                row['Cohorte propuesta'] = 'resolver grupo paciente'


def report(rows: list[dict], out: Path) -> None:
    """Medianas y rangos por eje, sin contar máscaras como imágenes."""
    lines = ['# Resumen de la exploración 3D', '',
             'Unidad: volumen CT, no corte. Rangos = mínimo–máximo. Spacing en mm;',
             'dimensiones en vóxeles y ejes nativos del archivo. Candidato HU ≠ metal confirmado.', '',
             '| Dataset | Volúmenes | Candidatos HU | Metal sí revisado | Pendientes |',
             '|---|---:|---:|---:|---:|']
    for dataset in sorted({r['Dataset'] for r in rows}):
        group = [r for r in rows if r['Dataset'] == dataset]
        confirmed = sum(r['Metal'] == 'sí' and r['Revisión 3D y cortes'] == 'completa' for r in group)
        lines.append(f"| {dataset} | {len(group)} | {sum(r['Candidato HU'] == 'sí' for r in group)} | {confirmed} | {sum(r['Revisión 3D y cortes'] != 'completa' for r in group)} |")
    lines += ['', '| Dataset | Medida | Mediana [mín–máx] |', '|---|---|---|']
    for dataset in sorted({r['Dataset'] for r in rows}):
        for field in AUTO[3:9]:
            values = [float(r[field]) for r in rows if r['Dataset'] == dataset and r[field] != '']
            if values:
                lines.append(f'| {dataset} | {field} | {np.median(values):.6g} [{min(values):.6g}–{max(values):.6g}] |')
    hashes = Counter(r['SHA256 vóxeles'] for r in rows if r['SHA256 vóxeles'])
    lines += ['', f'Grupos de duplicados exactos por vóxeles: {sum(n > 1 for n in hashes.values())}.',
              f'Volúmenes únicos por contenido: {len(hashes)} (no equivale a pacientes únicos).',
              f'Errores de lectura: {sum(bool(r["Error"]) for r in rows)}.',
              f'Máscaras locales vinculadas por nombre: {sum(bool(r["Máscara local"]) for r in rows)}.',
              '', '## Elegibilidad provisional', '']
    lines += [f'- {key}: {value}' for key, value in sorted(Counter(r['Cohorte propuesta'] for r in rows).items())]
    lines += ['', 'La asignación definitiva requiere revisión, resolver duplicados y agrupar por paciente.',
              'Las máscaras se vinculan por nombre; aún deben verificarse alineación y etiquetas.',
              'No se infiere ausencia de metal a partir del nombre dataset6 ni del filtro HU.']
    (out / 'resumen.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def scan(args: argparse.Namespace) -> None:
    """Relee HU escalados originales; conserva anotaciones al reejecutar."""
    previous = {r['Caso']: r for r in read_csv(args.out / 'revision.csv')}
    paths = sorted(args.data.rglob('*_data.nii*'))
    if not paths:
        raise SystemExit('No se encontraron CT *_data.nii[.gz]. No se modificó el CSV.')
    rows = []
    for i, path in enumerate(paths):
        case = path.name.split('.nii')[0]
        row = dict.fromkeys(MANUAL + AUTO, '')
        row.update({key: previous.get(case, {}).get(key, '') for key in MANUAL})
        row.update({'Caso': case, 'Dataset': path.name.split('_')[0],
                    'Archivo': path.relative_to(args.data).as_posix(), 'Umbral HU': args.hu})
        try:
            img = nib.load(path)
            if len(img.shape) != 3:
                raise ValueError(f'Se esperaba CT 3D: {img.shape}')
            if img.header.get_xyzt_units()[0] != 'mm':
                raise ValueError('Unidades espaciales no declaradas en mm')
            data = img.get_fdata(dtype=np.float32)
            if not np.isfinite(data).all():
                raise ValueError('HU no finitos')
            for axis, spacing, dim in zip('xyz', img.header.get_zooms(), img.shape):
                row[f'Spacing {axis} mm'] = float(spacing)
                row[f'Dim {axis}'] = dim
            row['HU mínimo'], row['HU máximo'] = float(data.min()), float(data.max())
            row['Vóxeles sobre umbral'] = int(np.count_nonzero(data > args.hu))
            row['Candidato HU'] = 'sí' if row['Vóxeles sobre umbral'] else 'no'
            digest = hashlib.sha256(str(data.shape).encode())
            digest.update(np.ascontiguousarray(data, dtype='<f4').data)
            row['SHA256 vóxeles'] = digest.hexdigest()
            masks = list(args.data.rglob(path.name.replace('_data', '_mask')))
            row['Máscara local'] = ' | '.join(p.relative_to(args.data).as_posix() for p in masks)
            del data
        except Exception as exc:
            row['Error'] = str(exc)
        rows.append(row)
        print(f'{i+1}/{len(paths)} {case}: {row["Candidato HU"] or row["Error"]}', flush=True)
    counts = Counter(r['SHA256 vóxeles'] for r in rows if r['SHA256 vóxeles'])
    for row in rows:
        sha = row['SHA256 vóxeles']
        row['Grupo duplicado'] = sha if sha and counts[sha] > 1 else ''
    missing = set(previous) - {r['Caso'] for r in rows}
    if missing:
        raise SystemExit(f'Faltan {len(missing)} casos previamente inventariados; no se sobrescribe el CSV.')
    cohorts(rows)
    antecedents(rows)
    save(rows, args.out)
    report(rows, args.out)


def view(args: argparse.Namespace) -> None:
    """HTML offline: superficies físicas RAS y cortes en el máximo HU."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from skimage.measure import marching_cubes
    rows = read_csv(args.out / 'revision.csv')
    selected = [r for r in rows if r['Caso'] == args.case]
    if len(selected) != 1:
        raise SystemExit('Caso inexistente; usar el identificador completo de revision.csv.')
    img = nib.as_closest_canonical(nib.load(args.data / selected[0]['Archivo']))
    data = img.get_fdata(dtype=np.float32)
    fig = go.Figure()
    for threshold, step, color, opacity in [(300, 4, 'ivory', .12), (1500, 1, 'orange', .6), (2500, 1, 'red', 1), (3500, 1, 'cyan', 1)]:
        if not data.min() < threshold < data.max():
            continue
        vertices, faces, _, _ = marching_cubes(data, level=threshold, step_size=step, allow_degenerate=False)
        xyz = nib.affines.apply_affine(img.affine, vertices)
        fig.add_trace(go.Mesh3d(x=xyz[:, 0], y=xyz[:, 1], z=xyz[:, 2],
                               i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
                               color=color, opacity=opacity, name=f'{threshold} HU (paso {step})', showlegend=True,
                               visible=True if threshold in (300, 2500) else 'legendonly'))
    fig.update_layout(title=f'{args.case} — superficies HU, no segmentación de metal',
                      scene=dict(aspectmode='data', xaxis_title='R (+) / L (−), mm',
                                 yaxis_title='A (+) / P (−), mm', zaxis_title='S (+) / I (−), mm'))
    destination = args.out / 'outputs'
    destination.mkdir(exist_ok=True, parents=True)
    fig.write_html(destination / f'{args.case}.html',
                   include_plotlyjs=getattr(args, 'plotlyjs', True))
    ijk = tuple(int(i) for i in np.unravel_index(np.argmax(data), data.shape))
    spacing = nib.affines.voxel_sizes(img.affine)
    if getattr(args, 'cortes_html', True):
        slices = make_subplots(rows=1, cols=3, subplot_titles=('Sagital', 'Coronal', 'Axial'))
        for col, (axis, index) in enumerate(zip(range(3), ijk), 1):
            plane = np.take(data, index, axis=axis).T
            plane_axes = [j for j in range(3) if j != axis]
            slices.add_trace(go.Heatmap(z=plane, x=np.arange(plane.shape[1]) * spacing[plane_axes[0]],
                                       y=np.arange(plane.shape[0]) * spacing[plane_axes[1]],
                                       zmin=-200, zmax=2000, colorscale='Gray', showscale=False), row=1, col=col)
            slices.update_yaxes(scaleanchor='x' + (str(col) if col > 1 else ''), scaleratio=1, row=1, col=col)
            slices.update_xaxes(title_text='mm desde origen del plano', row=1, col=col)
        slices.update_layout(title=f'Cortes por el máximo HU {ijk}; no sustituyen recorrer todo el CT')
        slices.write_html(destination / f'{args.case}_cortes.html',
                          include_plotlyjs=getattr(args, 'plotlyjs', True))
    import matplotlib.pyplot as plt
    preview, axes = plt.subplots(1, 3, figsize=(13, 5))
    for axis, ax in enumerate(axes):
        plane_axes = [j for j in range(3) if j != axis]
        ax.imshow(np.take(data, ijk[axis], axis=axis).T, origin='lower', cmap='gray',
                  vmin=-200, vmax=2000, aspect=spacing[plane_axes[1]] / spacing[plane_axes[0]])
        ax.set_title(f'{("Sagital", "Coronal", "Axial")[axis]}: {ijk[axis]}')
    preview.suptitle(f'{args.case} — cortes por máximo HU, revisión parcial')
    preview.tight_layout()
    preview.savefig(destination / f'{args.case}_cortes.png', dpi=150)
    plt.close(preview)
    print(destination / f'{args.case}.html')


def views(args: argparse.Namespace) -> None:
    """Genera las vistas 3D en lote; no rehace las que ya existen."""
    rows = read_csv(args.out / 'revision.csv')
    if not rows:
        raise SystemExit('Ejecutar inventario primero.')
    cases = [row['Caso'] for row in rows
             if not row['Error'] and (args.todos or row['Candidato HU'] == 'sí')]
    part, total = (int(v) for v in getattr(args, 'parte', '1/1').split('/'))
    cases = cases[part - 1::total]
    destination = args.out / 'outputs'
    done = failed = skipped = 0
    for i, case in enumerate(cases, 1):
        args.case = case
        if (destination / f'{case}.html').exists() and not args.rehacer:
            skipped += 1
            print(f'{i}/{len(cases)} {case}: ya existe', flush=True)
            continue
        try:
            view(args)
            done += 1
        except Exception as exc:
            failed += 1
            print(f'{i}/{len(cases)} {case}: FALLO {exc}', flush=True)
    size = sum(p.stat().st_size for p in destination.glob('*.html')) / 2 ** 20
    print(f'Generadas {done}, saltadas {skipped}, fallidas {failed}. '
          f'HTML en outputs/: {size:.0f} MB.')


def cuts(args: argparse.Namespace) -> None:
    """Visor local con deslizadores para recorrer todos los cortes y cambiar ventana."""
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider, RadioButtons
    rows = read_csv(args.out / 'revision.csv')
    selected = [r for r in rows if r['Caso'] == args.case]
    if len(selected) != 1:
        raise SystemExit('Caso inexistente.')
    img = nib.as_closest_canonical(nib.load(args.data / selected[0]['Archivo']))
    data = img.get_fdata(dtype=np.float32)
    spacing = nib.affines.voxel_sizes(img.affine)
    fig, axes = plt.subplots(1, 3, figsize=(15, 7))
    fig.subplots_adjust(bottom=.32)
    artists, sliders = [], []
    names = ['Sagital (A→, S↑)', 'Coronal (R→, S↑)', 'Axial (R→, A↑)']
    for axis, ax in enumerate(axes):
        plane_axes = [j for j in range(3) if j != axis]
        index = data.shape[axis] // 2
        art = ax.imshow(np.take(data, index, axis=axis).T, origin='lower',
                        cmap='gray', vmin=-200, vmax=2000,
                        aspect=spacing[plane_axes[1]] / spacing[plane_axes[0]])
        ax.set_title(names[axis])
        artists.append(art)
        slider = Slider(fig.add_axes([.12 + axis * .29, .2, .23, .03]),
                        'Corte', 0, data.shape[axis] - 1, valinit=index, valstep=1)
        sliders.append(slider)
    def update(_: float) -> None:
        for axis, (art, slider) in enumerate(zip(artists, sliders)):
            art.set_data(np.take(data, int(slider.val), axis=axis).T)
        fig.canvas.draw_idle()
    for slider in sliders:
        slider.on_changed(update)
    windows = {'Hueso': (-200, 2000), 'Tejido': (-160, 240), 'Metal': (-1000, max(4000, float(data.max())))}
    radio = RadioButtons(fig.add_axes([.42, .01, .17, .14]), list(windows))
    def window(label: str) -> None:
        for art in artists:
            art.set_clim(*windows[label])
        fig.canvas.draw_idle()
    radio.on_clicked(window)
    fig.suptitle(args.case + ' — HU originales; índices canónicos RAS, base 0')
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'data')
    parser.add_argument('--out', type=Path, default=HERE)
    sub = parser.add_subparsers(dest='command', required=True)
    inventory = sub.add_parser('inventario')
    inventory.add_argument('--hu', type=float, default=2500)
    viewer = sub.add_parser('ver')
    viewer.add_argument('case')
    batch = sub.add_parser('vistas', help='las vistas 3D de todos los candidatos')
    batch.add_argument('--todos', action='store_true', help='incluir los no candidatos')
    batch.add_argument('--rehacer', action='store_true', help='regenerar las existentes')
    batch.add_argument('--con-cortes', dest='cortes_html', action='store_true',
                       help='ademas el HTML de cortes (pesa ~8 MB por caso)')
    batch.add_argument('--parte', default='1/1', help='reparto entre procesos, p.ej. 2/3')
    batch.add_argument('--plotlyjs', default='directory', choices=['directory', 'inline'],
                       help='directory comparte un plotly.min.js en outputs/ y sigue offline')
    mpr = sub.add_parser('cortes')
    mpr.add_argument('case')
    sub.add_parser('resumen')
    args = parser.parse_args()
    if args.command == 'inventario':
        scan(args)
    elif args.command == 'ver':
        view(args)
    elif args.command == 'vistas':
        views(args)
    elif args.command == 'cortes':
        cuts(args)
    else:
        rows = read_csv(args.out / 'revision.csv')
        if not rows:
            raise SystemExit('Ejecutar inventario primero.')
        cohorts(rows)
        antecedents(rows)
        save(rows, args.out)
        report(rows, args.out)


if __name__ == '__main__':
    main()
