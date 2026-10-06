"""A11 - rasteriza el tornillo parametrico a voxeles: `M`, `B_delta` y `G` (#139, bloque E-A2).

POR QUE EXISTE
--------------
Es la pieza que falta para que la cadena completa se pueda ejecutar. Hoy el muestreador entrega una
pose **analitica** —centro `c` y direccion `u` en mm— y `src/muestreador/sap.py` la califica
**sin construir ninguna mascara**: mide la brecha sobre el eje con un campo signado y un calibre.
Nunca hubo un paso que convierta la pose en voxeles. Por eso #139 dice que la cadena
"pose -> `M` -> generacion" **no se ha ejecutado nunca**: no existia el eslabon del medio.

Este script es ese eslabon. De una pose a `M = voxeles cuyo centro cae dentro del solido`
(`diseno_A.md` seccion 6), luego `B_delta` por distancia euclidea 3D con el espaciado del header, y
`G = M union B_delta`.

MARCO DE COORDENADAS: el mismo de SAP, y no es negociable
---------------------------------------------------------
`sap._indices` define `idx = (pts - origen) / zoom`, con `origen = [s.start for s in sl] * zoom`
(`e9ts_corredor.py`:272). O sea: los milimetros son **indice de voxel por espaciado**, ejes alineados,
sin rotacion de la afin. Este script usa **exactamente** esa convencion. Si usara otra, `M` quedaria
en un sitio distinto del que SAP califico y las dos mitades del Objetivo 2 y 3 dejarian de hablar del
mismo tornillo, sin que nada avisara.

GEOMETRIA: tres diametros distintos, y aqui se usa el del CUERPO
----------------------------------------------------------------
`main.tex` (*Implant geometry source*) separa tres geometrias con propositos distintos, y mezclarlas
es el error que esa seccion existe para evitar:

| Geometria | Para que | Aqui |
|---|---|---|
| calibre nominal 6.5-8.0 mm | viabilidad del corredor | **no se usa** |
| **cuerpo ~4.91 mm** | lo que se **sintetiza** | **este es el que se rasteriza** (D3, 2026-09-20) |
| calibre de medicion 7.0 mm | brecha en SAP | **no se usa** |

El 4.91 mm es la mediana de `d_centro` medida en E11 sobre los tornillos reales de la cohorte, y
coincide con el fuste de catalogo de 4.8 mm. **Un cilindro de 6.5-8.0 mm sobrestimaria la seccion de
metal por mas del doble**, que es literalmente lo que `main.tex` advierte.

**Rosca: no se modela.** Sin fuente textual para su perfil (`diseno_A.md` seccion 6), un cilindro
liso es la simplificacion declarada. **Cabeza:** la unica medida publicada hallada, 8.0 mm de diametro
y 4.5 mm de alto, asentada sin fresado (`sayres2014comparison`). **Arandela:** 1.5 mm de grosor y
13.0 mm de diametro exterior, de un catalogo de **otro** fabricante (`doublemedical2021trauma`), asi
que va **apagada por defecto** y declarada cuando se use. **Canulacion:** el 2.9 mm que circula en
listados aparece en la guia del fabricante solo como canulacion de brocas y destornilladores, no del
tornillo; queda como **parametro libre**, solido por defecto.

CONTROLES QUE PUEDEN FALLAR
---------------------------
1. **Volumen rasterizado frente al analitico.** El cilindro tiene volumen cerrado; si la rasterizacion
   se desvia mas de `--tol-vol` (2 % por defecto), el muestreo de centros de voxel no es suficiente a
   esta resolucion y hay que declararlo o submuestrear.
2. **`M` conexa.** Un tornillo es un solido. Si sale en dos pedazos, la pose o el recorte estan mal.
3. **Diametro medido sobre la mascara.** `2 x max` del `distance_transform_edt` dentro de `M` tiene
   que coincidir con el nominal dentro de un voxel. Es el mismo estadistico con que E8 midio los
   tornillos reales, asi que el sintetico y el real se miden igual.
4. **`M` dentro del campo de vision**, sin tocar el borde del volumen.
5. **Si el receptor se declara limpio**, ningun voxel de `G` del CT original puede pasar de 2500 HU.
   Si pasa, el "receptor limpio" no lo es y la muestra no sirve para E-A2.

LO QUE ESTE SCRIPT NO HACE
--------------------------
No genera apariencia. Entrega `M` y `G` para que el renderizador los consuma. Y **no decide la pose**:
la lee de `e9ts_ejes_corredor.csv` o la recibe por argumentos, de modo que la pose sigue siendo del
muestreador del Objetivo 2 y este script no se convierte en un segundo muestreador encubierto.

USO
---
    python a11_rasterizar_tornillo.py --caso dataset6_CLINIC_0019_data
    python a11_rasterizar_tornillo.py --caso dataset6_CLINIC_0019_data --perturbar --semilla 0
    python a11_rasterizar_tornillo.py --caso ... --diam-cuerpo 4.91 --arandela --nifti
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo1'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo2'))

# Geometria, toda con fuente. Ninguna cifra de aqui se cambia sin cambiar su fuente.
D_CUERPO_MM = 4.91      # mediana de `d_centro` en E11; catalogo 4.8 mm (`synthes2003guide`). D3.
D_CABEZA_MM = 8.0       # `sayres2014comparison`
H_CABEZA_MM = 4.5       # `sayres2014comparison`, asentada sin fresado
D_ARANDELA_MM = 13.0    # tres fuentes coinciden
H_ARANDELA_MM = 1.5     # `doublemedical2021trauma`, OTRO fabricante: declarado
BANDA_MM = 12.0         # `B_delta`, `diseno_A.md` seccion 3
METAL_HU = 2500.0       # umbral de cribado por HU del Objetivo 1


def solido(p: np.ndarray, c: np.ndarray, u: np.ndarray, largo_mm: float,
           d_cuerpo: float, con_cabeza: bool, con_arandela: bool,
           d_canulacion: float) -> np.ndarray:
    """True en los puntos `p` (mm, forma (..., 3)) que caen dentro del tornillo.

    Coordenadas locales: `s` a lo largo del eje medido desde el centro, `r` radial. El cuerpo ocupa
    `|s| <= largo/2`. La cabeza y la arandela se apilan en el extremo **positivo** de `u`, que es el
    de entrada: `main.tex` dice que la cabeza se asienta sin fresado, asi que sobresale del cuerpo.
    """
    d = p - c
    s = d @ u
    r = np.linalg.norm(d - s[..., None] * u, axis=-1)

    dentro = (np.abs(s) <= largo_mm / 2.0) & (r <= d_cuerpo / 2.0)
    base = largo_mm / 2.0
    if con_cabeza:
        dentro |= (s > base) & (s <= base + H_CABEZA_MM) & (r <= D_CABEZA_MM / 2.0)
        base += H_CABEZA_MM
    if con_arandela:
        dentro |= (s > base) & (s <= base + H_ARANDELA_MM) & (r <= D_ARANDELA_MM / 2.0)
    if d_canulacion > 0.0:
        # el canal atraviesa cuerpo, cabeza y arandela por el eje
        dentro &= ~(r <= d_canulacion / 2.0)
    return dentro


def volumen_analitico(largo_mm: float, d_cuerpo: float, con_cabeza: bool,
                      con_arandela: bool, d_canulacion: float) -> float:
    """Volumen cerrado del solido, en mm3. Referencia del control 1."""
    v = np.pi * (d_cuerpo / 2.0) ** 2 * largo_mm
    alto_canal = largo_mm
    if con_cabeza:
        v += np.pi * (D_CABEZA_MM / 2.0) ** 2 * H_CABEZA_MM
        alto_canal += H_CABEZA_MM
    if con_arandela:
        v += np.pi * (D_ARANDELA_MM / 2.0) ** 2 * H_ARANDELA_MM
        alto_canal += H_ARANDELA_MM
    if d_canulacion > 0.0:
        v -= np.pi * (d_canulacion / 2.0) ** 2 * alto_canal
    return float(v)


def rasteriza(forma, zoom: np.ndarray, c: np.ndarray, u: np.ndarray, largo_mm: float,
              d_cuerpo: float, con_cabeza: bool, con_arandela: bool, d_canulacion: float,
              banda_mm: float, submuestreo: int = 1) -> tuple[np.ndarray, np.ndarray, dict]:
    """`M` y `G` sobre el volumen entero, calculadas solo en la caja que las contiene.

    No se recorre el volumen completo: el tornillo mas su banda ocupan una fraccion minima. Se acota
    una caja alrededor del segmento y se evalua ahi; fuera es False por construccion.

    SUBMUESTREO, y por que no es un adorno
    --------------------------------------
    `diseno_A.md` seccion 6 dice `M = voxeles cuyo centro cae dentro`. Con `submuestreo = 1` eso es
    literal, y **falla el control de volumen**: un cuerpo de 4.91 mm sobre voxeles de ~0.98 mm tiene
    solo ~5 voxeles de ancho, y discretizar su seccion circular deja un sesgo de area de varios por
    ciento. Cuando el eje es **oblicuo** los errores de cada corte se cancelan en parte; cuando el eje
    queda **alineado con un eje de voxel** —que pasa, porque el eje del corredor se busca en una
    rejilla angular— el mismo error se repite en todos los cortes y **no se cancela**: medido en
    `dataset6_CLINIC_0102_data`, con `u = [1, 0, 0]`, el volumen salia **+7.3 %**.

    Con `submuestreo = n` cada voxel se evalua en `n^3` puntos y entra si **mas de la mitad** cae
    dentro. Es la regla de ocupacion por mayoria, consistente con "el centro cae dentro" en el limite
    `n -> infinito` y mucho menos sesgada a `n = 3`. El coste es `n^3` evaluaciones en una caja
    pequena, no en el volumen.
    """
    from scipy import ndimage as ndi
    u = np.asarray(u, dtype=float) / np.linalg.norm(u)
    c = np.asarray(c, dtype=float)
    radio_max = max(d_cuerpo, D_CABEZA_MM if con_cabeza else 0.0,
                    D_ARANDELA_MM if con_arandela else 0.0) / 2.0
    alcance = largo_mm / 2.0 + (H_CABEZA_MM if con_cabeza else 0.0) \
        + (H_ARANDELA_MM if con_arandela else 0.0)
    margen = radio_max + banda_mm + 2.0 * float(zoom.max())
    extremos = np.stack([c - alcance * u, c + alcance * u])
    lo = np.maximum(0, np.floor((extremos.min(axis=0) - margen) / zoom).astype(int))
    hi = np.minimum(np.array(forma), np.ceil((extremos.max(axis=0) + margen) / zoom).astype(int) + 1)
    if np.any(hi <= lo):
        raise SystemExit('la caja del tornillo cae fuera del volumen: revisar la pose')

    ejes = [np.arange(lo[i], hi[i]) * zoom[i] for i in range(3)]
    malla = np.stack(np.meshgrid(*ejes, indexing='ij'), axis=-1)
    if submuestreo <= 1:
        m_caja = solido(malla, c, u, largo_mm, d_cuerpo, con_cabeza, con_arandela, d_canulacion)
    else:
        # desplazamientos de los `n^3` subpuntos dentro del voxel, centrados en su centro
        off = (np.arange(submuestreo) + 0.5) / submuestreo - 0.5
        acum = np.zeros(malla.shape[:-1], dtype=np.int16)
        for dx in off:
            for dy in off:
                for dz in off:
                    p = malla + np.array([dx * zoom[0], dy * zoom[1], dz * zoom[2]])
                    acum += solido(p, c, u, largo_mm, d_cuerpo, con_cabeza, con_arandela,
                                   d_canulacion)
        m_caja = acum * 2 > submuestreo ** 3

    M = np.zeros(forma, dtype=bool)
    sl = tuple(slice(lo[i], hi[i]) for i in range(3))
    M[sl] = m_caja
    if not M.any():
        raise SystemExit('`M` salio vacia: la pose o la geometria no producen ningun voxel')

    # `B_delta` por distancia euclidea 3D con el espaciado real, igual que en P1
    dist = ndi.distance_transform_edt(~m_caja, sampling=zoom)
    g_caja = m_caja | (dist <= banda_mm)
    G = np.zeros(forma, dtype=bool)
    G[sl] = g_caja

    # Control 3: diametro medido sobre la mascara, mismo estadistico que E8 en los reales.
    # Se mide sobre el CUERPO SOLO, no sobre `M` entera. La primera version uso `M` completa y el
    # maximo del `distance_transform_edt` caia dentro de la CABEZA, que tiene 8.0 mm: el control
    # marcaba una desviacion de ~1 mm que no existia en el fuste. El defecto era del control.
    # Volumen FRACCIONARIO: ocupacion media de cada voxel con una rejilla fina. No es una mascara
    # candidata —el Diseno A necesita `M` binaria— sino el diagnostico que separa "el codigo de la
    # geometria esta bien" de "una mascara binaria a esta resolucion no puede representar el volumen".
    nf = 4
    offf = (np.arange(nf) + 0.5) / nf - 0.5
    frac = np.zeros(malla.shape[:-1], dtype=np.float32)
    for dx in offf:
        for dy in offf:
            for dz in offf:
                p_ = malla + np.array([dx * zoom[0], dy * zoom[1], dz * zoom[2]])
                frac += solido(p_, c, u, largo_mm, d_cuerpo, con_cabeza, con_arandela, d_canulacion)
    frac /= nf ** 3

    cuerpo = m_caja & solido(malla, c, u, largo_mm, d_cuerpo * 1.6, False, False, 0.0)
    d_edt = ndi.distance_transform_edt(cuerpo, sampling=zoom)
    meta = {'caja_lo': lo.tolist(), 'caja_hi': hi.tolist(),
            'd_medido_mm': round(float(2.0 * d_edt.max()), 3),
            'n_cuerpo': int(cuerpo.sum()),
            'vol_frac_mm3': float(frac.sum()) * float(np.prod(zoom))}
    return M, G, meta


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--caso', required=True)
    ap.add_argument('--ejes', type=Path,
                    default=aqui.parent / 'objetivo2' / 'outputs' / 'e9ts_ejes_corredor.csv')
    ap.add_argument('--modo', default='default6mm', help='columna `modo` del CSV de ejes')
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--particiones', nargs='+', default=['train', 'val'],
                    help='NUNCA test mientras no sea la evaluacion final preinscrita')
    ap.add_argument('--diam-cuerpo', type=float, default=D_CUERPO_MM)
    ap.add_argument('--largo-mm', type=float, default=0.0,
                    help='0 = usa `L_TS_mejor_mm` del CSV de ejes, que es el corredor medido')
    ap.add_argument('--sin-cabeza', action='store_true')
    ap.add_argument('--arandela', action='store_true',
                    help='anade la arandela; su grosor viene de OTRO fabricante y hay que declararlo')
    ap.add_argument('--canulacion-mm', type=float, default=0.0, help='0 = solido')
    ap.add_argument('--banda-mm', type=float, default=BANDA_MM)
    ap.add_argument('--perturbar', action='store_true',
                    help='aplica una pose del muestreador del Objetivo 2 en vez del eje central')
    ap.add_argument('--semilla', type=int, default=0)
    ap.add_argument('--tol-vol', type=float, default=0.02)
    ap.add_argument('--submuestreo', type=int, default=1,
                    help='subpuntos por lado dentro de cada voxel; 1 = regla literal del centro, que '
                         'sesga el volumen varios por ciento con ejes alineados')
    ap.add_argument('--receptor-limpio', action='store_true',
                    help='exige que ningun voxel de `G` del CT original pase de 2500 HU')
    ap.add_argument('--nifti', action='store_true')
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a11')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    if 'test' in [p.lower() for p in args.particiones]:
        raise SystemExit('CONTROL: se pidio test. Abortado: la cadena se ensaya en validacion '
                         '(Strict Isolation Rule, main.tex:111).')

    import nibabel as nib
    from p1_decodificador_sd15 import leer_particion, rutas

    filas = leer_particion(args.particion)
    permitidos = {f['Caso'] for f in filas if f['particion'] in args.particiones}
    if args.caso not in permitidos:
        raise SystemExit('%s no esta en %s: abortado' % (args.caso, args.particiones))
    ubic = rutas([f for f in filas if f['Caso'] == args.caso], list(args.data))
    if args.caso not in ubic:
        raise SystemExit('no se hallo el volumen de %s' % args.caso)

    # --- pose: del CSV de ejes del Objetivo 2, no de aqui
    with open(args.ejes, newline='', encoding='utf-8') as fh:
        cand = [r for r in csv.DictReader(fh)
                if r['Caso'] == args.caso and r['modo'] == args.modo and not r['Error']]
    if not cand:
        raise SystemExit('sin eje para %s en modo %s dentro de %s'
                         % (args.caso, args.modo, args.ejes.name))
    e = cand[0]
    c = np.array([float(e['c_x_mm']), float(e['c_y_mm']), float(e['c_z_mm'])])
    u = np.array([float(e['u_x']), float(e['u_y']), float(e['u_z'])])
    largo = args.largo_mm or float(e['L_TS_mejor_mm'])
    print('caso %s | eje del corredor: c=%s u=%s | L=%.1f mm | D_TS_max=%.1f mm'
          % (args.caso, np.round(c, 1).tolist(), np.round(u, 4).tolist(),
             largo, float(e['D_TS_max_mm'])))

    if args.perturbar:
        from muestreador.muestreo import muestrear_poses, rng_de_caso
        cs, us = muestrear_poses(c, u, largo, 1, rng_de_caso(args.caso, args.semilla))
        c, u = cs[0], us[0]
        print('  pose perturbada por el muestreador del Objetivo 2 (semilla %d): c=%s u=%s'
              % (args.semilla, np.round(c, 1).tolist(), np.round(u, 4).tolist()))

    img = nib.load(ubic[args.caso])
    zoom = np.array(img.header.get_zooms()[:3], dtype=float)
    forma = img.shape[:3]
    print('volumen %s | espaciado %s mm' % (forma, np.round(zoom, 3).tolist()))

    M, G, meta = rasteriza(forma, zoom, c, u, largo, args.diam_cuerpo,
                           not args.sin_cabeza, args.arandela, args.canulacion_mm, args.banda_mm,
                           submuestreo=args.submuestreo)
    print('submuestreo: %d^3 = %d subpuntos por voxel, ocupacion por mayoria'
          % (args.submuestreo, args.submuestreo ** 3))
    vox_mm3 = float(np.prod(zoom))
    v_ras = int(M.sum()) * vox_mm3
    v_ana = volumen_analitico(largo, args.diam_cuerpo, not args.sin_cabeza,
                              args.arandela, args.canulacion_mm)
    err = (v_ras - v_ana) / v_ana

    from scipy import ndimage as ndi
    _, n_comp = ndi.label(M)
    toca_borde = any(M.take(i, axis=ax).any() for ax in range(3) for i in (0, -1))

    print('\n--- CONTROLES ---')
    v_frac = meta['vol_frac_mm3']
    err_frac = (v_frac - v_ana) / v_ana
    print('1a. GEOMETRIA (volumen fraccionario, rejilla 4^3): %.1f mm3 | analitico %.1f mm3 | '
          'error %+.2f %% -> %s'
          % (v_frac, v_ana, 100 * err_frac, 'PASA' if abs(err_frac) <= args.tol_vol else 'FALLA'))
    print('    Controla el CODIGO: si pasa, el solido parametrico esta bien construido.')
    print('1b. CUANTIZACION de la mascara binaria: %.1f mm3 | error %+.2f %% | tolerancia declarada '
          '%.0f %% -> %s'
          % (v_ras, 100 * err, 100 * args.tol_vol, 'dentro' if abs(err) <= args.tol_vol else 'FUERA'))
    print('    NO es un defecto corregible por codigo: el cuerpo tiene ~%.1f voxeles de ancho y una'
          % (args.diam_cuerpo / float(zoom.max())))
    print('    mascara binaria a esa resolucion no puede representar su seccion circular. El')
    print('    submuestreo no converge (medido en 0102: +7.3, -2.2 y +7.1 %% con n = 1, 2 y 3). El')
    print('    sesgo depende de la ORIENTACION de la pose frente a la rejilla y es maximo con ejes')
    print('    alineados a ella. Ver #142.')
    print('2. componentes conexas de `M`: %d -> %s' % (n_comp, 'PASA' if n_comp == 1 else 'FALLA'))
    print('3. diametro medido sobre `M`: %.2f mm | nominal %.2f mm | diferencia %.2f mm '
          '(un voxel = %.2f mm) -> %s'
          % (meta['d_medido_mm'], args.diam_cuerpo, abs(meta['d_medido_mm'] - args.diam_cuerpo),
             zoom.max(), 'PASA' if abs(meta['d_medido_mm'] - args.diam_cuerpo) <= zoom.max() else 'REVISAR'))
    print('4. `M` toca el borde del volumen: %s -> %s' % (toca_borde, 'FALLA' if toca_borde else 'PASA'))

    hu = img.get_fdata(dtype=np.float32)
    n_sobre = int((hu[G] > METAL_HU).sum())
    print('5. voxeles del CT ORIGINAL dentro de `G` por encima de %.0f HU: %d%s'
          % (METAL_HU, n_sobre,
             (' -> ' + ('PASA' if n_sobre == 0 else 'FALLA')) if args.receptor_limpio else
             ' (informativo; use --receptor-limpio para exigir 0)'))
    if args.receptor_limpio and n_sobre:
        raise SystemExit('CONTROL 5 FALLA: el receptor no esta limpio, no sirve para E-A2')

    print('\n`M`: %d voxeles (%.1f mm3) | `G`: %d | banda `G\\M`: %d | G/M = %.1f'
          % (int(M.sum()), v_ras, int(G.sum()), int(G.sum() - M.sum()),
             G.sum() / max(1, M.sum())))

    if args.nifti:
        afin = np.diag(list(zoom) + [1.0])
        for nombre, v in (('M', M), ('G', G)):
            ruta = args.out_dir / ('a11_%s_%s.nii.gz' % (args.caso, nombre))
            nib.save(nib.Nifti1Image(v.astype(np.uint8), afin), ruta)
            print('nifti: %s' % ruta)

    ruta = args.out_dir / ('a11_%s_controles.csv' % args.caso)
    fila = {'caso': args.caso, 'modo': args.modo, 'perturbada': args.perturbar,
            'semilla': args.semilla, 'largo_mm': round(largo, 2),
            'diam_cuerpo_mm': args.diam_cuerpo, 'cabeza': not args.sin_cabeza,
            'arandela': args.arandela, 'canulacion_mm': args.canulacion_mm,
            'banda_mm': args.banda_mm, 'submuestreo': args.submuestreo,
            'n_M': int(M.sum()), 'n_G': int(G.sum()),
            'vol_ras_mm3': round(v_ras, 1), 'vol_ana_mm3': round(v_ana, 1),
            'err_vol_rel': round(err, 4), 'vol_frac_mm3': round(v_frac, 1),
            'err_vol_frac_rel': round(err_frac, 4), 'n_componentes': n_comp,
            'd_medido_mm': meta['d_medido_mm'], 'toca_borde': toca_borde,
            'n_original_sobre_2500': n_sobre}
    with open(ruta, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(fila.keys()))
        w.writeheader()
        w.writerow(fila)
    print('controles: %s' % ruta)


if __name__ == '__main__':
    main()
