"""A4 / Diseno A — vista 3D interactiva de los componentes muestreados, coloreada por propuesta (#104).

PARA QUE
--------
Complemento de `a3_laminas_componentes.py`. Las laminas son proyecciones y un corte: sirven para
juzgar forma, pero no para ver **donde esta** el objeto respecto al cuerpo. Esa pregunta aparecio
sola al revisar (#105): hay componentes que **no estan dentro del paciente** —electrodos, cursores
de cremallera, botones de ropa— y en una proyeccion recortada eso no se distingue de un implante.

Aqui cada caso produce **un HTML navegable** (mismo formato que `exploration-3d/outputs/*.html`:
plotly, `marching_cubes`, offline) con:

- la **silueta del paciente** a 300 HU, marfil y casi transparente, como referencia de "dentro o
  fuera del cuerpo";
- el **hueso** a 1500 HU, apagado por defecto (se enciende desde la leyenda);
- cada **componente muestreado**, coloreado por lo que propone el filtro automatico:
  **verde = tornillo**, naranja = otro implante, gris = fragmento.

El color es **la hipotesis del filtro, no la verdad**. Es justo lo que hay que contrastar: si algo
verde esta flotando fuera de la piel, el filtro se equivoco y eso es el dato que se busca.

QUE NO CAMBIA
-------------
No toca la planilla ni los veredictos. Es solo otra forma de mirar la misma muestra.

SALIDA (`--out`)
----------------
`html/<caso>.html`, uno por caso con componentes en la muestra. Comparte `plotly.min.js` en la
carpeta de salida (`--plotlyjs directory`), asi funciona sin internet.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'objetivo1'))
from p1_decodificador_sd15 import leer_particion, rutas  # noqa: E402
from e6c_techo_lw import METAL_HU  # noqa: E402
from a1b_parches_componente import MIN_COMP_MM3  # noqa: E402

# Colores neon para los componentes MUESTREADOS: el objetivo es localizarlos de un vistazo entre
# todo el metal del caso, no que quede bonito.
COLOR = {'tornillo': '#39FF14',        # verde neon
         'otro implante': '#FF00FF',   # magenta neon
         'fragmento': '#00E5FF'}       # cian neon
COLOR_OTROS = '#8899AA'   # el resto del metal del caso: apagado y translucido, solo de referencia
OPACIDAD_OTROS = 0.25

# CUERPO: el borde aire/tejido esta cerca de -400 HU, NO en 300.
# La primera version uso 300 HU copiando `exploration-3d/explorar.py` y rotulo eso como "piel": es
# falso, 300 HU es hueso. Medido en `dataset7_CLINIC_metal_0004_data`: HU > -400 da el 29.7% del
# volumen (el paciente) y HU > 300 solo el 1.3% (hueso y metal). Entre -600 y -200 la fraccion
# apenas cambia, asi que -400 cae en una meseta y no es un valor delicado.
CUERPO_HU = -400.0
# Hueso: **300 HU**, el mismo que usa `exploration-3d/explorar.py`, por peticion de la autora para
# que las dos vistas sean comparables. A 150 HU (el `BONE_HU` del resto de la tesis) entra tambien
# tejido denso y la malla crece sin aportar; 300 deja hueso limpio.
BONE_HU_VIS = 300.0
CONTEXTO_HUESO = (BONE_HU_VIS, 3, 'lightsalmon', 0.25, True)


def superficie(fig, mascara: np.ndarray, affine: np.ndarray, color: str, opacidad: float,
               nombre: str, visible, paso: int = 1, nivel: float | None = None) -> bool:
    """Anade una isosuperficie al `fig`. False si no se pudo.

    `nivel` es OBLIGATORIO para arrays de HU. La primera version lo dejaba en `None` y
    `marching_cubes` caia en su valor por defecto, `(max + min) / 2`: en un CT con metal eso son
    **~7200 HU**, asi que las capas rotuladas "piel" y "hueso" dibujaban en realidad **metal**.
    Ese fue el fallo que la autora detecto mirando los HTML, no el valor del umbral.
    """
    from skimage.measure import marching_cubes
    import plotly.graph_objects as go

    es_bool = mascara.dtype == bool
    dato = mascara.astype(np.float32) if es_bool else mascara
    if nivel is None:
        nivel = 0.5 if es_bool else None
    if nivel is None:
        raise ValueError(f'{nombre}: falta `nivel` para un array de HU')
    if not (float(dato.min()) < nivel < float(dato.max())):
        return False
    try:
        v, f, _, _ = marching_cubes(dato, level=nivel, step_size=paso, allow_degenerate=False)
    except (ValueError, RuntimeError):
        return False
    xyz = nib.affines.apply_affine(affine, v)
    fig.add_trace(go.Mesh3d(x=xyz[:, 0], y=xyz[:, 1], z=xyz[:, 2],
                            i=f[:, 0], j=f[:, 1], k=f[:, 2],
                            color=color, opacity=opacidad, name=nombre,
                            showlegend=True, visible=visible))
    return True


def mascara_cuerpo(arr: np.ndarray, umbral: float = CUERPO_HU) -> np.ndarray:
    """Cuerpo del paciente: tejido por encima de `umbral`, componente mayor y huecos rellenos.

    El componente mayor descarta mesa, tubos y ruido sueltos; rellenar huecos evita que el aire
    intestinal o los pulmones abran agujeros en la superficie. Medido en un caso de prueba: 28.5%
    del volumen, y el 99.9% del metal de ese paciente queda dentro.
    """
    cuerpo = arr > umbral
    if not cuerpo.any():
        return cuerpo
    lab, _ = ndi.label(cuerpo)
    tam = np.bincount(lab.ravel())
    tam[0] = 0
    return ndi.binary_fill_holes(lab == int(tam.argmax()))


def main() -> None:
    aqui = Path(__file__).resolve().parent
    raiz = aqui.parents[1]
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--planilla', type=Path, default=aqui / 'a3_revision_componentes.csv')
    p.add_argument('--particion', type=Path, default=raiz / 'experiments/objetivo1/p1_particion.csv')
    p.add_argument('--data', type=Path, nargs='+', default=[raiz / 'data'])
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--min-comp-mm3', type=float, default=MIN_COMP_MM3)
    p.add_argument('--casos', nargs='*', default=None)
    p.add_argument('--sin-contexto', action='store_true',
                   help='omite piel y hueso; mas liviano, pero se pierde el "dentro o fuera"')
    args = p.parse_args()

    import plotly.graph_objects as go

    out = args.out.expanduser().resolve()
    (out / 'html').mkdir(parents=True, exist_ok=True)
    filas = list(csv.DictReader(open(args.planilla, encoding='utf-8')))
    por_caso: dict[str, list[dict]] = {}
    for r in filas:
        if args.casos and r['Caso'] not in args.casos:
            continue
        por_caso.setdefault(r['Caso'], []).append(r)

    metas = {m['Caso']: m for m in leer_particion(args.particion)}
    ubic = rutas(list(metas.values()), args.data)

    for i, (caso, cs) in enumerate(sorted(por_caso.items()), 1):
        if caso not in ubic:
            print(f'{caso}: NO ENCONTRADO', flush=True)
            continue
        img = nib.load(ubic[caso])
        arr = img.get_fdata(dtype=np.float32)
        zooms = tuple(float(z) for z in img.header.get_zooms()[:3])
        vox = float(np.prod(zooms))

        fig = go.Figure()
        if not args.sin_contexto:
            cuerpo = mascara_cuerpo(arr, CUERPO_HU)
            superficie(fig, cuerpo, img.affine, 'ivory', 0.12,
                       f'cuerpo del paciente (> {CUERPO_HU:.0f} HU)', True, 4)
            del cuerpo
            nivel, paso, color, op, _ = CONTEXTO_HUESO
            superficie(fig, arr, img.affine, color, op,
                       f'hueso ({nivel:.0f} HU)', True, paso, nivel=nivel)

        etiquetas, n = ndi.label(arr > METAL_HU)
        tam = np.bincount(etiquetas.ravel())
        validos = [j for j in range(1, n + 1) if tam[j] * vox >= args.min_comp_mm3]

        # 1) Todo el metal que NO esta en la muestra, en una sola capa translucida. Sirve de
        #    referencia: deja ver cuanto metal tiene el caso y cual es el que se esta calificando.
        metal = etiquetas > 0
        muestreado = np.zeros_like(metal)
        for r in cs:
            ci = int(r['comp'])
            if ci < len(validos):
                muestreado |= etiquetas == validos[ci]
        otros = metal & ~muestreado
        if otros.any():
            superficie(fig, otros, img.affine, COLOR_OTROS, OPACIDAD_OTROS,
                       f'resto del metal del caso ({int(otros.sum())} vox)', True)
        del metal, muestreado, otros

        # 2) Los componentes muestreados, opacos y en neon, encima de todo lo anterior.
        puestos = 0
        for r in cs:
            ci = int(r['comp'])
            if ci >= len(validos):
                continue
            prop = r['propuesta_auto']
            ver = (r.get('veredicto') or '').strip()
            etiqueta = (f"comp {ci} — {float(r['vol_mm3']):.0f} mm3 — {prop}"
                        + (f" — VEREDICTO: {ver}" if ver else ''))
            if superficie(fig, etiquetas == validos[ci], img.affine,
                          COLOR.get(prop, '#FFFF00'), 1.0, etiqueta, True):
                puestos += 1

        fig.update_layout(
            title=(f'{caso} — {puestos} componentes muestreados en NEON. '
                   'Verde = tornillo, magenta = otro implante, cian = fragmento. '
                   'Gris translucido = resto del metal del caso. '
                   'El color es la PROPUESTA del filtro, no la verdad.'),
            scene=dict(aspectmode='data', xaxis_title='R (+) / L (-), mm',
                       yaxis_title='A (+) / P (-), mm', zaxis_title='S (+) / I (-), mm'))
        fig.write_html(out / 'html' / f'{caso}.html', include_plotlyjs='directory')
        print(f'{i}/{len(por_caso)} {caso}: {puestos} componentes', flush=True)
        del arr, etiquetas

    print(f'Escritos en {out / "html"}', flush=True)


if __name__ == '__main__':
    main()
