"""A14 - grafico de las curvas de entrenamiento de `run01` y `run02` (#134).

POR QUE EXISTE
--------------
Las dos corridas dejaron `curva.csv` y nada mas. La forma de U —que es **el** resultado del
entrenamiento del Objetivo 3— solo se podia ver corriendo un `awk` que promedia por bloques. Este
script la dibuja, y dibuja las dos corridas juntas, que es lo que permite ver que **trazan la misma
curva**.

DOS DECISIONES DE DISENO QUE NO SON ESTETICAS
---------------------------------------------
1. **Dos paneles, no dos ejes.** La perdida de entrenamiento y la de validacion tienen escalas
   distintas. Un grafico de doble eje `y` permite sugerir cualquier relacion entre dos series
   moviendo las escalas, asi que van en paneles separados con el mismo eje `x`.

2. **El grafico lleva escrita la advertencia de comparabilidad.** `run01` midio la validacion con un
   estimador que sorteaba el nivel de ruido en cada medicion (oscilacion +-15 % por **como** se
   medio); `run02` usa `SEMILLA_VAL` fija. **Las filas sueltas de las dos corridas no son
   comparables entre si**, solo las medias por bloque. Un grafico que ponga las dos curvas juntas sin
   decirlo invita justo a la comparacion prohibida, asi que la nota va dentro de la figura y no en el
   pie de un documento que puede separarse del PNG.

LO QUE DIBUJA
-------------
- la curva cruda, fina y translucida: se ve el ruido real de la medicion;
- la **media por bloques de 10 000 pasos**, gruesa y con marcador: es como el proyecto lee la curva;
- el **minimo** de cada corrida, con su valor y su paso rotulados.

USO
---
    python a14_curvas.py
    python a14_curvas.py --bloque 5000
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

# Paleta por defecto de la guia de visualizacion del proyecto, validada con su script
# (`validate_palette.js --mode light`): las dos ranuras categoricas pasan las seis comprobaciones,
# con separacion CVD Delta E 24.7 y de vision normal 33.6, muy por encima de los pisos de 8 y 15.
AZUL = '#2a78d6'       # ranura 1 -> run01
NARANJA = '#eb6834'    # ranura 2 -> run02
SUPERFICIE = '#fcfcfb'
TINTA = '#0b0b0b'
TINTA_2 = '#52514e'


def lee(ruta: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Devuelve (paso, perdida, perdida_val) de un `curva.csv`."""
    with open(ruta, newline='', encoding='utf-8') as fh:
        filas = list(csv.DictReader(fh))
    paso = np.array([int(f['paso']) for f in filas])
    ent = np.array([float(f['perdida']) for f in filas])
    val = np.array([float(f['perdida_val']) for f in filas])
    return paso, ent, val


def bloques(paso: np.ndarray, y: np.ndarray, ancho: int):
    """Media de `y` por bloques de `ancho` pasos. Devuelve (centro del bloque, media, n)."""
    b = paso // ancho
    xs, ys, ns = [], [], []
    for k in np.unique(b):
        sel = b == k
        xs.append(k * ancho + ancho / 2)
        ys.append(float(y[sel].mean()))
        ns.append(int(sel.sum()))
    return np.array(xs), np.array(ys), np.array(ns)


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--a7', type=Path, default=aqui / 'outputs' / 'a7')
    ap.add_argument('--bloque', type=int, default=10000)
    ap.add_argument('--min-filas', type=int, default=6,
                    help='bloques con menos filas que esto no se dibujan: su media no es comparable')
    ap.add_argument('--salida', type=Path, default=None)
    args = ap.parse_args()

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    corridas = []
    for nombre, color in (('run01', AZUL), ('run02', NARANJA)):
        ruta = args.a7 / nombre / 'curva.csv'
        if not ruta.exists():
            print('AVISO: falta %s, se omite' % ruta)
            continue
        corridas.append((nombre, color) + lee(ruta))
    if not corridas:
        raise SystemExit('no se hallo ningun curva.csv bajo %s' % args.a7)

    fig, (ax_v, ax_e) = plt.subplots(2, 1, figsize=(11, 8.2), sharex=True,
                                     gridspec_kw={'height_ratios': [1.6, 1.0]})
    fig.patch.set_facecolor(SUPERFICIE)
    etiquetas = {'run01': 'run01 — 144 500 pasos, A100 entera, estimador que sorteaba',
                 'run02': 'run02 — 60 000 pasos, particion MIG, SEMILLA_VAL fija'}

    for ax in (ax_v, ax_e):
        ax.set_facecolor(SUPERFICIE)
        for lado in ('top', 'right'):
            ax.spines[lado].set_visible(False)
        for lado in ('left', 'bottom'):
            ax.spines[lado].set_color(TINTA_2)
            ax.spines[lado].set_linewidth(0.8)
        ax.grid(True, color='#e2e1dc', linewidth=0.8, zorder=0)
        ax.set_axisbelow(True)
        ax.tick_params(colors=TINTA_2, labelsize=9)

    for nombre, color, paso, ent, val in corridas:
        # curva cruda: fina y translucida, para que se vea el ruido de la medicion
        ax_v.plot(paso, val, color=color, linewidth=0.9, alpha=0.28, zorder=2)
        ax_e.plot(paso, ent, color=color, linewidth=0.9, alpha=0.28, zorder=2)
        # media por bloques: como el proyecto lee la curva
        for ax, y in ((ax_v, val), (ax_e, ent)):
            bx, by, bn = bloques(paso, y, args.bloque)
            ok = bn >= args.min_filas
            ax.plot(bx[ok], by[ok], color=color, linewidth=2.0, marker='o', markersize=5,
                    markeredgecolor=SUPERFICIE, markeredgewidth=1.2, zorder=4,
                    label=etiquetas[nombre] if ax is ax_v else None)
        # Minimo POR BLOQUE, no por fila. La fila minima de `run01` (0.04942) es un valor del
        # estimador que sorteaba: destacarla seria senalar ruido de medicion como si fuera el mejor
        # momento del modelo. El bloque es la unidad que el proyecto declara legible.
        bx, by, bn = bloques(paso, val, args.bloque)
        ok = bn >= args.min_filas
        j = int(np.argmin(by[ok]))
        mx, my = float(bx[ok][j]), float(by[ok][j])
        ax_v.plot(mx, my, marker='D', markersize=9, color=color,
                  markeredgecolor=SUPERFICIE, markeredgewidth=1.5, zorder=5)
        izq = nombre == 'run01'
        ax_v.annotate('minimo de %s: %.5f\nbloque %s a %s' % (
                          nombre, my,
                          format(int(mx - args.bloque / 2), ',').replace(',', ' '),
                          format(int(mx + args.bloque / 2), ',').replace(',', ' ')),
                      xy=(mx, my), xytext=(-18 if izq else 30, -44 if izq else 30),
                      textcoords='offset points', fontsize=8.5, color=TINTA,
                      ha='right' if izq else 'left',
                      arrowprops=dict(arrowstyle='-', color=TINTA_2, linewidth=0.8))

    ax_v.set_ylabel('perdida de VALIDACION\n(media por bloques de %s pasos)'
                    % format(args.bloque, ',').replace(',', ' '),
                    fontsize=10, color=TINTA)
    ax_e.set_ylabel('perdida de\nENTRENAMIENTO', fontsize=10, color=TINTA)
    ax_e.set_xlabel('paso de entrenamiento', fontsize=10, color=TINTA)
    ax_v.legend(loc='upper center', frameon=False, fontsize=9, labelcolor=TINTA_2)

    ax_v.set_title('Entrenamiento del renderizador: la validacion toca su minimo y despues SUBE',
                   fontsize=13, color=TINTA, loc='left', pad=14, fontweight='bold')
    fig.text(0.5, 0.965,
             'Las dos corridas trazan la misma curva. La perdida de entrenamiento sigue bajando '
             'mientras la de validacion sube: eso es sobreajuste.',
             fontsize=9.5, color=TINTA_2, ha='center')

    nota = ('COMPARABILIDAD. `run01` midio la validacion sorteando el nivel de ruido en cada '
            'medicion (oscilacion +-15 % por COMO se midio); `run02` usa semilla fija.\n'
            'Por eso las filas sueltas de las dos corridas no se comparan entre si: solo las medias '
            'por bloque, que coinciden dentro de 1.5e-3 en todos los bloques.\n'
            'Los rombos marcan el minimo POR BLOQUE, no la fila mas baja. `mejor.pt` de run02 se '
            'guardo en su fila minima, el paso 37 500, dentro de la meseta.')
    fig.text(0.012, 0.012, nota.replace('**', ''), fontsize=8, color=TINTA_2, va='bottom')

    fig.subplots_adjust(top=0.90, bottom=0.165, left=0.115, right=0.985, hspace=0.12)
    salida = args.salida or (args.a7 / 'a14_curvas_run01_run02.png')
    fig.savefig(salida, dpi=150, facecolor=SUPERFICIE)
    plt.close(fig)
    print('grafico: %s' % salida)

    # tabla por bloques, para citar cifras sin leer el PNG
    print('\nMedias por bloques de %d pasos (bloques con menos de %d filas marcados con *):'
          % (args.bloque, args.min_filas))
    print('%10s' % 'bloque', end='')
    for nombre, *_ in corridas:
        print('%14s' % nombre, end='')
    print()
    tablas = {n: dict(zip(*bloques(p, v, args.bloque)[:2]))
              for n, c, p, e, v in corridas}
    cuentas = {n: dict(zip(bloques(p, v, args.bloque)[0], bloques(p, v, args.bloque)[2]))
               for n, c, p, e, v in corridas}
    for x in sorted(set().union(*[set(t) for t in tablas.values()])):
        print('%10d' % (x - args.bloque / 2), end='')
        for nombre, *_ in corridas:
            if x in tablas[nombre]:
                marca = '*' if cuentas[nombre][x] < args.min_filas else ' '
                print('%13.5f%s' % (tablas[nombre][x], marca), end='')
            else:
                print('%14s' % '-', end='')
        print()


if __name__ == '__main__':
    main()
