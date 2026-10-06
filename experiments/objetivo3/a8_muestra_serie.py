"""A8 - muestra de una SERIE COMPLETA de cortes, no uno solo (#116, continuacion de A6).

POR QUE EXISTE
--------------
`a6_muestra_minima.py` genera UN corte. Un corte no permite ver lo unico que un clinico mira
primero: si el implante sintetizado es **el mismo objeto a lo largo del eje axial** o si cada corte
inventa un objeto distinto. La coherencia entre cortes vecinos es una propiedad del Diseno A (2.5D,
`diseno_A.md` seccion 4) y hasta ahora **nadie la ha observado**.

Este script recorre todos los cortes cacheados de una serie (= un componente de un paciente),
genera cada uno con `muestrea_ddim`, los compone en el volumen original del caso y escribe:

- `a8_<serie>_original.nii.gz` y `a8_<serie>_compuesta.nii.gz`  (subvolumen recortado, en HU)
- `a8_<serie>.html`           vista 3D navegable (plotly offline, mismo formato que
                              `exploration-3d/outputs/*.html`): hueso de contexto, metal REAL,
                              metal GENERADO y la banda `G`
- `a8_<serie>_cortes.html`    recorrido corte a corte con deslizador: original | compuesta |
                              solo lo generado, en HU y con escala comun
- `a8_<serie>_montaje.png`    rejilla de cortes de la compuesta
- `a8_<serie>_controles.csv`  una fila por corte con los controles y los rangos de HU

NO ES UN RESULTADO DE TESIS
---------------------------
Igual que A6: es diagnostico. Con el `ckpt.pt` de `run01` el modelo esta **pasado de su optimo**
(minimo de validacion en ~25 000 pasos, #134), y las pesas del minimo se perdieron. Lo que salga de
aqui dice como se ve el renderizador actual, no cuanto puede dar.

QUE SERIES SE PUEDEN PEDIR
--------------------------
Solo series de pacientes de las particiones de `--particiones`; por omision `val`, que es lo que el
modelo no vio. El script aborta si el paciente de la serie no esta ahi, porque generar sobre test
romperia la Strict Isolation Rule (`main.tex:111`).

CONTROLES QUE PUEDEN FALLAR (y abortan)
---------------------------------------
- el parche del `.npz` tiene que coincidir **voxel a voxel** con la ventana del volumen original;
- lo generado tiene que ser **cero exacto fuera de `G`**;
- `verificar_composicion` en cada corte: fuera de `G` la compuesta es identica al original.

REANUDABLE
----------
Cada corte generado se guarda en `<out>/_cortes/<serie>_k####.npz`. Si el proceso se corta, volver
a lanzarlo reusa lo ya hecho y sigue donde quedo. `--rehacer` lo ignora y regenera todo.

USO
---
    python a8_muestra_serie.py --serie dataset7_CLINIC_metal_0011_data_c011
    python a8_muestra_serie.py --serie dataset7_CLINIC_metal_0056_data_c001 --pasos 50
    python a8_muestra_serie.py --serie <serie> --solo-html     # ya generado, rehacer vistas
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from pathlib import Path

import numpy as np
import torch

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src' / 'renderizador'))
sys.path.insert(0, str(_RAIZ / 'src' / 'common'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo1'))

from datos import ParchesMetal, caso_de  # noqa: E402
from difusion import Difusion, muestrea_ddim  # noqa: E402
from modelo import UNetDifusion  # noqa: E402
from region import componer, verificar_composicion  # noqa: E402
from ventanas import decodifica_bloque  # noqa: E402

# Umbrales de visualizacion. METAL_HU es el del Objetivo 1 (`e6c_techo_lw.py`); el 300 HU de hueso
# para 3D es el que ya usan `exploration-3d/explorar.py` y `a4_html_componentes.py`, por peticion de
# la autora, para que las tres vistas sean comparables.
METAL_HU = 2500.0
BONE_HU_VIS = 300.0
MARGEN_BB = 8          # voxeles de margen alrededor de la union de ventanas, solo para la vista


def a_hu(bloque: torch.Tensor) -> np.ndarray:
    """De la representacion multi-ventana en [-1, 1] a HU, con la `regla` congelada del Objetivo 1."""
    u = (bloque.detach().cpu().numpy()[0] + 1.0) / 2.0
    return decodifica_bloque(u)


def cortes_de(cache: Path, serie: str) -> list[int]:
    """Cortes cacheados de la serie, ordenados."""
    pat = re.compile(re.escape(serie) + r'_k(\d{4})\.npz$')
    ks = []
    for f in cache.glob(serie + '_k*.npz'):
        m = pat.search(f.name)
        if m is not None:
            ks.append(int(m.group(1)))
    return sorted(ks)


def genera_serie(args, ds, modelo, dif, ks: list[int]) -> dict[int, np.ndarray]:
    """Genera (o reusa del cache) el HU generado de cada corte. Devuelve {k: hu_gen}."""
    dir_c = args.out_dir / '_cortes'
    dir_c.mkdir(parents=True, exist_ok=True)
    pos = {k: i for i, (s, k) in enumerate(ds.indice) if s == args.serie}
    faltan = [k for k in ks if k not in pos]
    if faltan:
        raise SystemExit('cortes sin entrada en el dataset: ' + repr(faltan[:10]))
    hu_gen: dict[int, np.ndarray] = {}
    pendientes = []
    for k in ks:
        ruta = dir_c / (args.serie + '_k%04d.npz' % k)
        if ruta.exists() and not args.rehacer:
            with np.load(ruta) as z:
                hu_gen[k] = z['hu_gen']
        else:
            pendientes.append(k)
    print('cortes: %d en total | %d ya en cache | %d por generar'
          % (len(ks), len(hu_gen), len(pendientes)), flush=True)
    if pendientes:
        print('estimado: ~%.0f min a ~1.05 s por paso y corte en CPU'
              % (len(pendientes) * args.pasos * 1.05 / 60), flush=True)
    t_ini = time.time()
    for n, k in enumerate(pendientes, 1):
        m = ds[pos[k]]
        with torch.no_grad():
            gen = muestrea_ddim(modelo, m['cond'][None], m['g'][None], dif,
                                pasos=args.pasos, semilla=args.semilla)
        gmask = m['g'].numpy()[0].astype(bool)
        fuera = float(np.abs(gen.numpy()[0][:, ~gmask]).max()) if (~gmask).any() else 0.0
        if fuera != 0.0:
            raise RuntimeError('corte %d: lo generado NO es cero fuera de G (%.3e)' % (k, fuera))
        h = a_hu(gen)
        hu_gen[k] = h
        np.savez_compressed(dir_c / (args.serie + '_k%04d.npz' % k), hu_gen=h.astype(np.float32))
        tr = (time.time() - t_ini) / n * (len(pendientes) - n) / 60
        print('  [%d/%d] corte %d listo | faltan ~%.0f min' % (n, len(pendientes), k, tr),
              flush=True)
    return hu_gen


def arma_volumen(args, ks: list[int], hu_gen: dict[int, np.ndarray]):
    """Recorta el volumen original del caso al entorno de la serie e inserta lo compuesto.

    Se usa el volumen REAL del paciente como contexto, no un mosaico de parches: las ventanas de
    256 x 256 se desplazan de corte a corte (`x0` varia), asi que pegar solo parches dejaria el
    hueso roto entre cortes y la vista 3D seria un artefacto del recorte, no del modelo.
    """
    import nibabel as nib
    from p1_decodificador_sd15 import leer_particion, rutas
    from e6b_vae_sd15 import eje_axial

    caso = caso_de(args.serie)
    filas = leer_particion(args.particion)
    ubic = rutas([f for f in filas if f['Caso'] == caso], list(args.data))
    if caso not in ubic:
        raise SystemExit('no se hallo el volumen de %s bajo %s' % (caso, args.data))
    img = nib.load(ubic[caso])
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = tuple(float(z) for z in img.header.get_zooms()[:3])
    plano = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)                      # (k, y, x), marco axial de a1b
    esp = (zooms[eje], zooms[plano[0]], zooms[plano[1]])
    codigos = nib.aff2axcodes(img.affine)
    etiquetas = (codigos[eje], codigos[plano[0]], codigos[plano[1]])

    vent = {}
    for k in ks:
        with np.load(args.cache / (args.serie + '_k%04d.npz' % k)) as z:
            vent[k] = (int(z['y0']), int(z['x0']),
                       z['hu'].astype(np.float32), z['g'].astype(bool), z['metal'].astype(bool))
    y0s = [v[0] for v in vent.values()]
    x0s = [v[1] for v in vent.values()]
    lado_y = max(v[2].shape[0] for v in vent.values())
    lado_x = max(v[2].shape[1] for v in vent.values())
    ya = max(0, min(y0s) - MARGEN_BB)
    yb = min(vol.shape[1], max(y0s) + lado_y + MARGEN_BB)
    xa = max(0, min(x0s) - MARGEN_BB)
    xb = min(vol.shape[2], max(x0s) + lado_x + MARGEN_BB)

    sub_o = vol[ks[0]:ks[-1] + 1, ya:yb, xa:xb].copy()
    sub_c = sub_o.copy()
    sub_g = np.zeros(sub_o.shape, dtype=bool)
    sub_m = np.zeros(sub_o.shape, dtype=bool)
    filas_ctrl = []
    for k in ks:
        y0, x0, hu_npz, g, metal = vent[k]
        h, w = hu_npz.shape
        kk = k - ks[0]
        ventana = vol[k, y0:y0 + h, x0:x0 + w]
        # CONTROL: el parche cacheado tiene que ser la misma ventana del volumen original. Si no lo
        # es, el marco axial o el recorte de a1b no son los que este script supone y todo lo 3D
        # estaria mal colocado sin que se note.
        if ventana.shape == hu_npz.shape:
            d = float(np.abs(ventana - hu_npz).max())
        else:
            d = float('inf')
        if d > 0.0:
            raise RuntimeError('corte %d: el parche del cache difiere del volumen (%.3f HU)' % (k, d))
        hu_sal = componer(hu_npz, hu_gen[k], g)
        verificar_composicion(hu_npz, hu_sal, g)
        sl = (kk, slice(y0 - ya, y0 - ya + h), slice(x0 - xa, x0 - xa + w))
        sub_c[sl] = hu_sal
        sub_g[sl] = g
        sub_m[sl] = metal
        dentro_g = hu_gen[k][g]
        real_g = hu_npz[g]
        filas_ctrl.append({
            'corte': k, 'n_G': int(g.sum()), 'n_metal_real': int(metal.sum()),
            'gen_min': round(float(dentro_g.min()), 1),
            'gen_p50': round(float(np.median(dentro_g)), 1),
            'gen_max': round(float(dentro_g.max()), 1),
            'real_min': round(float(real_g.min()), 1),
            'real_p50': round(float(np.median(real_g)), 1),
            'real_max': round(float(real_g.max()), 1),
            'mae_en_G': round(float(np.abs(dentro_g - real_g).mean()), 1),
            'n_gen_sobre_2500': int((dentro_g > METAL_HU).sum()),
            'n_real_sobre_2500': int((real_g > METAL_HU).sum()),
        })
    return sub_o, sub_c, sub_g, sub_m, esp, etiquetas, filas_ctrl


def superficie(fig, dato: np.ndarray, nivel: float, esp, color: str, opac: float,
               nombre: str, visible, paso: int = 1) -> bool:
    """Isosuperficie, con las coordenadas ya en mm.

    `nivel` es obligatorio: dejarlo al defecto de `marching_cubes` en un CT con metal dibuja metal
    y lo rotula hueso. Ese fallo ya se cometio en A4 y lo detecto la autora mirando los HTML.
    """
    from skimage.measure import marching_cubes
    import plotly.graph_objects as go
    d = dato.astype(np.float32)
    if not (float(d.min()) < nivel < float(d.max())):
        return False
    try:
        v, f, _, _ = marching_cubes(d, level=nivel, spacing=esp, step_size=paso,
                                    allow_degenerate=False)
    except (ValueError, RuntimeError):
        return False
    fig.add_trace(go.Mesh3d(x=v[:, 0], y=v[:, 1], z=v[:, 2],
                            i=f[:, 0], j=f[:, 1], k=f[:, 2],
                            color=color, opacity=opac, name=nombre,
                            showlegend=True, visible=visible))
    return True


def escribe_html_3d(args, sub_o, sub_c, sub_g, esp, etiquetas, paso_ck) -> None:
    import plotly.graph_objects as go
    fig = go.Figure()
    puesto = []
    # Hueso de referencia: sale del ORIGINAL, no de la compuesta, para que no se confunda el
    # contexto del paciente con lo que puso el modelo.
    if superficie(fig, sub_o, BONE_HU_VIS, esp, 'lightsalmon', 0.20,
                  'hueso del paciente (> %.0f HU, del original)' % BONE_HU_VIS, True, 2):
        puesto.append('hueso')
    if superficie(fig, sub_g, 0.5, esp, '#2E86DE', 0.10, 'region de generacion G',
                  'legendonly', 2):
        puesto.append('G')
    gen_metal = (sub_c > METAL_HU) & sub_g
    real_metal = (sub_o > METAL_HU) & sub_g
    if superficie(fig, real_metal, 0.5, esp, '#FF00FF', 0.35,
                  'metal REAL en G (> %.0f HU, %d vox)' % (METAL_HU, int(real_metal.sum())), True):
        puesto.append('real')
    if superficie(fig, gen_metal, 0.5, esp, '#39FF14', 1.0,
                  'metal GENERADO en G (> %.0f HU, %d vox)' % (METAL_HU, int(gen_metal.sum())), True):
        puesto.append('generado')
    fig.update_layout(
        title=('%s - verde = metal GENERADO, magenta translucido = metal REAL. '
               'ckpt en el paso %s, %d pasos DDIM. DIAGNOSTICO, NO es un resultado de tesis.'
               % (args.serie, paso_ck, args.pasos)),
        scene=dict(aspectmode='data',
                   xaxis_title='eje axial %s, mm' % etiquetas[0],
                   yaxis_title='eje %s, mm' % etiquetas[1],
                   zaxis_title='eje %s, mm' % etiquetas[2]))
    ruta = args.out_dir / ('a8_' + args.serie + '.html')
    fig.write_html(ruta, include_plotlyjs=args.plotlyjs)
    print('html 3D: %s  (capas: %s)' % (ruta, ', '.join(puesto)))


def escribe_html_cortes(args, sub_o, sub_c, sub_g, esp, ks, paso_ck) -> None:
    """Recorrido corte a corte con deslizador: original | compuesta | solo lo generado."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    n = sub_o.shape[0]
    solo = np.where(sub_g, sub_c, -1000.0)
    ejes_x = np.arange(sub_o.shape[2]) * esp[2]
    ejes_y = np.arange(sub_o.shape[1]) * esp[1]
    fig = make_subplots(rows=1, cols=3, horizontal_spacing=0.04,
                        subplot_titles=('original', 'compuesta (sintetica)',
                                        'solo lo generado en G'))
    for i in range(n):
        for col, dato in enumerate((sub_o, sub_c, solo), 1):
            fig.add_trace(go.Heatmap(z=dato[i], x=ejes_x, y=ejes_y, zmin=-200, zmax=2000,
                                     colorscale='Gray', showscale=False, visible=(i == n // 2)),
                          row=1, col=col)
    pasos = []
    for i in range(n):
        vis = [False] * (3 * n)
        vis[3 * i:3 * i + 3] = [True, True, True]
        pasos.append(dict(method='update', label=str(ks[0] + i), args=[{'visible': vis}]))
    for c in (1, 2, 3):
        fig.update_yaxes(scaleanchor='x' + (str(c) if c > 1 else ''), scaleratio=1,
                         autorange='reversed', row=1, col=c)
    fig.update_layout(
        sliders=[dict(active=n // 2, currentvalue={'prefix': 'corte '}, steps=pasos)],
        title=('%s - %d cortes, ventana fija de -200 a 2000 HU. ckpt en el paso %s. '
               'DIAGNOSTICO, NO es un resultado de tesis.' % (args.serie, n, paso_ck)))
    ruta = args.out_dir / ('a8_' + args.serie + '_cortes.html')
    fig.write_html(ruta, include_plotlyjs=args.plotlyjs)
    print('html cortes: %s' % ruta)


def escribe_montaje(args, sub_c, ks) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    n = sub_c.shape[0]
    cuantos = min(24, n)
    idx = np.linspace(0, n - 1, cuantos).round().astype(int)
    filas = int(np.ceil(cuantos / 6))
    fig, ax = plt.subplots(filas, 6, figsize=(16, 2.8 * filas), squeeze=False)
    for a in ax.ravel():
        a.set_axis_off()
    for a, i in zip(ax.ravel(), idx):
        a.imshow(sub_c[i], cmap='gray', vmin=-200, vmax=1300)
        a.set_title('corte %d' % (ks[0] + i), fontsize=8)
    fig.suptitle('%s - compuesta, %d de %d cortes. DIAGNOSTICO, NO es un resultado de tesis.'
                 % (args.serie, cuantos, n), fontsize=10)
    fig.tight_layout()
    ruta = args.out_dir / ('a8_' + args.serie + '_montaje.png')
    fig.savefig(ruta, dpi=120)
    plt.close(fig)
    print('montaje: %s' % ruta)


def escribe_nifti(args, sub_o, sub_c, sub_g, esp) -> None:
    """Escribe original, compuesta y G como `.nii.gz` en HU, con el espaciado real del caso.

    POR QUE EXISTE: un clinico no puede juzgar un PNG. En ITK-SNAP, con los HU de verdad, se
    ventanea y se distingue el metal del hueso.
    """
    try:
        import nibabel as nib
    except ModuleNotFoundError:
        print('AVISO: falta nibabel, no se escriben los .nii.gz')
        return
    afin = np.diag([esp[1], esp[2], esp[0], 1.0])
    for nombre, v in (('original', sub_o), ('compuesta', sub_c), ('G', sub_g.astype(np.float32))):
        vol = np.moveaxis(v, 0, 2)                     # (y, x, k): el eje de corte al final
        ruta = args.out_dir / ('a8_' + args.serie + '_' + nombre + '.nii.gz')
        nib.save(nib.Nifti1Image(np.ascontiguousarray(vol, dtype=np.float32), afin), ruta)
        print('nifti: %s' % ruta)
    print('  espaciado en plano %.3f x %.3f mm, grosor %.3f mm' % (esp[1], esp[2], esp[0]))


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--serie', required=True,
                    help='clave caso + componente, p. ej. dataset7_CLINIC_metal_0011_data_c011')
    ap.add_argument('--ckpt', type=Path, default=aqui / 'outputs' / 'a7' / 'run01' / 'ckpt.pt')
    ap.add_argument('--cache', type=Path, default=aqui / 'outputs' / 'a1b_cache')
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--particiones', nargs='+', default=['val'])
    ap.add_argument('--manifiesto', type=Path, default=None,
                    help='si se pasa, solo se generan los cortes del manifiesto (el conjunto de '
                         'entrenamiento R1-R3); por omision se generan TODOS los cortes cacheados '
                         'de la serie, que es lo que da un implante continuo')
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--pasos', type=int, default=50)
    ap.add_argument('--semilla', type=int, default=0)
    ap.add_argument('--hilos', type=int, default=0, help='hilos de torch; 0 deja el defecto')
    ap.add_argument('--max-cortes', type=int, default=0, help='0 = todos')
    ap.add_argument('--rehacer', action='store_true')
    ap.add_argument('--solo-html', action='store_true',
                    help='no genera nada: rearma las vistas con lo que haya en el cache de cortes')
    ap.add_argument('--plotlyjs', default='directory', choices=['directory', 'inline'])
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a8')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    if args.hilos:
        torch.set_num_threads(args.hilos)

    caso = caso_de(args.serie)
    ks = cortes_de(args.cache, args.serie)
    if not ks:
        raise SystemExit('no hay cortes cacheados para la serie %s en %s' % (args.serie, args.cache))
    if args.manifiesto:
        with open(args.manifiesto, newline='', encoding='utf-8') as fh:
            adm = set()
            for r in csv.DictReader(fh):
                if r['Caso'] + '_c%03d' % int(r['comp']) == args.serie:
                    adm.add(int(r['corte']))
        ks = [k for k in ks if k in adm]
    if args.max_cortes:
        ks = ks[:args.max_cortes]
    print('serie %s | caso %s | %d cortes de %d a %d | contiguo: %s'
          % (args.serie, caso, len(ks), ks[0], ks[-1],
             ks == list(range(ks[0], ks[-1] + 1))))

    ck = torch.load(args.ckpt, map_location='cpu', weights_only=False)
    base = int(ck.get('meta', {}).get('base', 64))
    paso_ck = ck.get('paso')
    print('ckpt: %s | base=%d | paso alcanzado: %s' % (args.ckpt, base, paso_ck))
    if 'run01' in str(args.ckpt):
        print('  AVISO: `run01` esta PASADO de su optimo (minimo de validacion en ~25 000, #134). '
              'No es el mejor modelo, es el ultimo.')
    modelo = UNetDifusion(base=base)
    modelo.load_state_dict(ck['modelo'])
    modelo.eval()

    hu_gen: dict[int, np.ndarray] = {}
    if args.solo_html:
        dir_c = args.out_dir / '_cortes'
        for k in list(ks):
            ruta = dir_c / (args.serie + '_k%04d.npz' % k)
            if ruta.exists():
                with np.load(ruta) as z:
                    hu_gen[k] = z['hu_gen']
        ks = [k for k in ks if k in hu_gen]
        if not ks:
            raise SystemExit('--solo-html pero no hay ningun corte en el cache')
        print('--solo-html: %d cortes del cache' % len(ks))
    else:
        # El dataset se carga SIN manifiesto: el manifiesto decide que ENTRENA, no que se puede
        # generar. El aislamiento por paciente lo da `--particiones`, y eso si es inviolable.
        ds = ParchesMetal(args.cache, args.particion, particiones=tuple(args.particiones))
        if caso not in ds.casos:
            raise SystemExit('%s no esta en las particiones %s: se aborta. Generar sobre test '
                             'romperia el aislamiento por paciente.' % (caso, args.particiones))
        dif = Difusion()
        hu_gen = genera_serie(args, ds, modelo, dif, ks)

    sub_o, sub_c, sub_g, sub_m, esp, etiquetas, ctrl = arma_volumen(args, ks, hu_gen)
    print('subvolumen: %s (k, %s, %s) | espaciado %.2f x %.2f x %.2f mm'
          % (sub_o.shape, etiquetas[1], etiquetas[2], esp[0], esp[1], esp[2]))
    print('CONTROL: parche del cache == ventana del volumen original -> PASA')
    print('CONTROL: composicion exacta fuera de G en los %d cortes -> PASA' % len(ks))

    g = sub_g
    print('HU generado dentro de G (toda la serie): min %.0f | p50 %.0f | max %.0f'
          % (sub_c[g].min(), np.median(sub_c[g]), sub_c[g].max()))
    print('HU real    dentro de G (toda la serie): min %.0f | p50 %.0f | max %.0f'
          % (sub_o[g].min(), np.median(sub_o[g]), sub_o[g].max()))
    print('voxeles > %.0f HU dentro de G: generado %d | real %d'
          % (METAL_HU, int((sub_c[g] > METAL_HU).sum()), int((sub_o[g] > METAL_HU).sum())))
    print('MAE dentro de G: %.1f HU  (DIAGNOSTICO; lo dominan los voxeles de metal, que llegan a '
          'miles de HU. No es una metrica de calidad)' % np.abs(sub_c[g] - sub_o[g]).mean())

    ruta_ctrl = args.out_dir / ('a8_' + args.serie + '_controles.csv')
    with open(ruta_ctrl, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(ctrl[0].keys()))
        w.writeheader()
        w.writerows(ctrl)
    print('controles: %s' % ruta_ctrl)

    escribe_nifti(args, sub_o, sub_c, sub_g, esp)
    escribe_montaje(args, sub_c, ks)
    escribe_html_3d(args, sub_o, sub_c, sub_g, esp, etiquetas, paso_ck)
    escribe_html_cortes(args, sub_o, sub_c, sub_g, esp, ks, paso_ck)


if __name__ == '__main__':
    main()
