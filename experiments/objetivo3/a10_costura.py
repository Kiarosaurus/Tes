"""A10 - salto de HU al cruzar el borde de `G`, la "costura" del bloque E-A2 (#139, #96, #112).

POR QUE EXISTE
--------------
#139 midio la costura **una vez**: un corte, un caso, con el `ckpt` de `run01` pasado de su optimo.
Dio **203 HU en la compuesta frente a 30 HU en el original**, un escalon de ~170 HU que no existe en
la imagen real. Esa cifra es el insumo del bloque **E-A2** y esta medida con el modelo equivocado.

Este script la mide sobre **una serie completa** y, sobre todo, la hace **reproducible y comparable
entre `ckpt`**: se le pasan las salidas de `a8_muestra_serie.py` y devuelve el salto del original y
el de la compuesta, en 3D y por corte.

DEFINICION, la misma de #139
----------------------------
Dos cascaras de **un voxel** a cada lado del borde de `G`:

- **anillo interior** = `G` menos su erosion: los voxeles de `G` que tocan el borde;
- **anillo exterior** = la dilatacion de `G` menos `G`: los voxeles de fuera que tocan el borde.

El **salto** es `|mediana(interior) - mediana(exterior)|` en HU. Se mide igual en el original y en la
compuesta, de modo que el original da la **referencia de cuanto salto hay en una imagen real**: no es
cero, porque el borde de `G` cae en tejido con estructura.

COMO SE LEE
-----------
Lo que importa **no es el salto de la compuesta**, es la **diferencia entre los dos saltos**. Un
salto de 200 HU donde la imagen real ya tiene 190 no es una costura; uno de 200 donde la real tiene
30 si. Por eso las dos columnas van siempre juntas y el script imprime el exceso.

CONTROLES QUE PUEDEN FALLAR
---------------------------
- los dos anillos tienen que ser no vacios, y se reporta su tamano: con pocos voxeles la mediana no
  significa nada;
- fuera de `G` la compuesta tiene que ser identica al original, asi que **la mediana del anillo
  exterior tiene que coincidir voxel a voxel entre las dos imagenes**. Si no coincide, la composicion
  esta mal y el resto de la medicion no vale.

USO
---
    python a10_costura.py --dir outputs/a8        --serie dataset7_CLINIC_metal_0011_data_c011
    python a10_costura.py --dir outputs/a8_mejor  --serie dataset7_CLINIC_metal_0011_data_c011
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np


def anillos(g: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Cascaras de un voxel a cada lado del borde de `g`, con vecindad de 6 (conectividad 1).

    Se usa conectividad 1 y no 3 a proposito: con vecindad de 26 la "cascara de un voxel" incluye
    diagonales y engorda el anillo, que es justo lo que la medicion quiere evitar.
    """
    from scipy import ndimage as ndi
    e = ndi.binary_erosion(g, ndi.generate_binary_structure(g.ndim, 1), border_value=1)
    d = ndi.binary_dilation(g, ndi.generate_binary_structure(g.ndim, 1))
    return g & ~e, d & ~g


def salto(img: np.ndarray, interior: np.ndarray, exterior: np.ndarray) -> tuple[float, float, float]:
    """Devuelve (mediana interior, mediana exterior, |salto|) en HU."""
    a = float(np.median(img[interior]))
    b = float(np.median(img[exterior]))
    return a, b, abs(a - b)


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir', type=Path, required=True,
                    help='carpeta con las salidas de a8_muestra_serie.py')
    ap.add_argument('--serie', required=True)
    ap.add_argument('--etiqueta', default='', help='nombre del ckpt, solo para el informe')
    ap.add_argument('--out', type=Path, default=None)
    args = ap.parse_args()
    # `--dir` se resuelve contra el directorio de trabajo, y si ahi no existe, contra la carpeta del
    # script: asi funciona tanto desde la raiz del repositorio como desde `experiments/objetivo3`.
    d = args.dir.resolve()
    if not d.is_dir():
        d = (aqui / args.dir).resolve()

    import nibabel as nib
    base = d / ('a8_' + args.serie + '_')
    vols = {}
    for nombre in ('original', 'compuesta', 'G'):
        ruta = Path(str(base) + nombre + '.nii.gz')
        if not ruta.exists():
            raise SystemExit('falta %s' % ruta)
        vols[nombre] = nib.load(ruta).get_fdata(dtype=np.float32)
    o, c = vols['original'], vols['compuesta']
    g = vols['G'] > 0.5

    print('serie %s | %s | subvolumen %s | voxeles en G: %d'
          % (args.serie, args.etiqueta or args.dir.name, o.shape, int(g.sum())))

    ins, out = anillos(g)
    print('anillos 3D: interior %d voxeles | exterior %d' % (int(ins.sum()), int(out.sum())))
    if not ins.any() or not out.any():
        raise SystemExit('CONTROL: algun anillo quedo vacio; la medicion no es interpretable')

    # CONTROL: fuera de G la compuesta es identica al original, asi que el anillo exterior tiene que
    # coincidir voxel a voxel. Si falla, la composicion esta mal y lo demas no vale.
    dif = float(np.abs(c[out] - o[out]).max())
    print('CONTROL: maxima |compuesta - original| en el anillo EXTERIOR = %.3e (debe ser 0)' % dif)
    if dif != 0.0:
        raise SystemExit('CONTROL FALLA: la compuesta cambia fuera de G')

    io_, oo, so = salto(o, ins, out)
    ic, oc, sc = salto(c, ins, out)
    print('\n--- SALTO EN 3D, sobre toda la serie ---')
    print('                 interior   exterior   |salto|')
    print('original         %8.1f   %8.1f   %7.1f' % (io_, oo, so))
    print('compuesta        %8.1f   %8.1f   %7.1f' % (ic, oc, sc))
    print('EXCESO de la compuesta sobre el original: %+.1f HU' % (sc - so))
    print('  Lo que importa es este exceso, no el salto absoluto: el borde de `G` cae en tejido con')
    print('  estructura, asi que la imagen real tampoco tiene salto cero.')

    # por corte, para ver si el exceso es parejo o lo produce un tramo
    filas = []
    for k in range(o.shape[2]):
        gk = g[:, :, k]
        if not gk.any():
            continue
        ik, ok_ = anillos(gk)
        if ik.sum() < 20 or ok_.sum() < 20:
            continue
        _, _, s_o = salto(o[:, :, k], ik, ok_)
        _, _, s_c = salto(c[:, :, k], ik, ok_)
        filas.append({'corte_idx': k, 'n_interior': int(ik.sum()), 'n_exterior': int(ok_.sum()),
                      'salto_original': round(s_o, 1), 'salto_compuesta': round(s_c, 1),
                      'exceso': round(s_c - s_o, 1)})
    if filas:
        ex = np.array([f['exceso'] for f in filas])
        q = np.percentile(ex, [0, 25, 50, 75, 100])
        print('\n--- EXCESO POR CORTE, %d cortes con anillos de >= 20 voxeles ---' % len(filas))
        print('  p50 %+.1f HU | IQR %+.1f a %+.1f | rango %+.1f a %+.1f'
              % (q[2], q[1], q[3], q[0], q[4]))
        print('  cortes con exceso > 100 HU: %d de %d' % (int((ex > 100).sum()), len(filas)))
        ruta = args.out or (d / ('a10_costura_' + args.serie + '.csv'))
        with open(ruta, 'w', newline='', encoding='utf-8') as fh:
            w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
            w.writeheader()
            w.writerows(filas)
        print('por corte: %s' % ruta)

    print('\nRecordatorio: #139 midio 203 HU en la compuesta frente a 30 en el original, UN corte, '
          'con el ckpt de `run01` pasado de su optimo. Esa cifra no es comparable a la 3D de aqui '
          'sin mirar la columna por corte.')


if __name__ == '__main__':
    main()
