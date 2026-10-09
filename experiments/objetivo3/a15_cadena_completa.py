"""A15 - LA CADENA COMPLETA, por primera vez: pelvis limpia -> pose -> `M` -> generacion (#139).

QUE ES ESTO
-----------
Hasta hoy el Objetivo 3 solo ha hecho **reconstruccion**: pedirle al modelo que regenere un implante
en un paciente que **ya lo tenia**. El caso de uso de la tesis es el contrario: **colocar un tornillo
donde no habia nada**. Ese recorrido —pose del muestreador, rasterizado de `M`, banda `B_delta`,
generacion, composicion— **nunca se ha ejecutado**, y es lo que #139 registra como el hueco central.

Este script lo ejecuta. No inventa ninguna pieza: encadena las que ya existen, y **usa las mismas
convenciones que el entrenamiento**, que es lo unico que hace valida la salida.

POR QUE IMPORTA MAS QUE CUALQUIER OTRO EXPERIMENTO PENDIENTE
------------------------------------------------------------
Es el unico que puede **invalidar el Objetivo 3 entero**. El renderizador aprendio la apariencia del
metal en pacientes que **ya tenian** streaking, y con mascaras de implantes **reales**, irregulares y
recortadas por umbral de densidad. Aqui se le pide generar sobre una pelvis **limpia** y con una
mascara de **cilindro parametrico liso**. Son dos desplazamientos de dominio a la vez, los dos
registrados y **ninguno medido**. Si el resultado es malo, conviene saberlo ahora.

DE DONDE SALE CADA PIEZA, y por que no se reimplementa ninguna
--------------------------------------------------------------
- **La pose** la da el muestreador del Objetivo 2, leida de `e9ts_ejes_corredor.csv`. Este script
  **no decide donde va el tornillo**; si lo hiciera seria un segundo muestreador encubierto.
- **`M`, `B_delta` y `G`** los construye `a11_rasterizar_tornillo.rasteriza`, en el marco de
  coordenadas de SAP. Se importa, no se copia.
- **La ventana de 256 x 256** la calcula `a1b_parches_componente.ventana_coords`, la misma que recorto
  los parches de entrenamiento.
- **La codificacion multiventana** es `common.ventanas`. La lectura de HU es, por omision, la `regla_suave`
  decidida para el Objetivo 3 (`DELTA_OBJ3 = 0.05`, 01-decisiones.md 2026-10-07); `--regla-v1` reproduce
  las corridas anteriores, que leian con la `regla` congelada del Objetivo 1 (#152).
- **La composicion y su control** son `common.region`.

EL CONDICIONAMIENTO, replicado EXACTAMENTE como en el entrenamiento
--------------------------------------------------------------------
`datos.ParchesMetal` arma 8 canales y este script arma los mismos, en el mismo orden:

1-3. corte **k-1** codificado en las tres ventanas, **con `G` borrada** (a -1000 HU);
4-6. corte **k+1**, igual;
7.   `M`;
8.   `G`.

**El corte central no entra en el condicionamiento.** El modelo solo ve a sus dos vecinos: asi se
entreno, y darle de mas aqui produciria una muestra que el entrenamiento no respalda. En los extremos
de la serie, donde el vecino no existe, se repite el central, igual que hace `ParchesMetal`.

CONTROLES QUE PUEDEN FALLAR
---------------------------
1. **Receptor limpio**: ningun voxel del CT original dentro de `G` por encima de 2500 HU. Si falla, el
   paciente no sirve para este ensayo.
2. **Cero fuera de `G`** en lo generado, antes de componer.
3. **Composicion exacta**: fuera de `G` la salida es identica bit a bit al original.
4. Los de `a11`: volumen del solido, `M` conexa, diametro medido y `M` dentro del campo de vision.

QUE EMITE, y para que sirve
---------------------------
Ademas de los volumenes y las laminas, calcula los **dos estadisticos del criterio de seleccion de
modelo** fijado en `01-decisiones.md` 2026-10-05 (6): el **perfil radial de HU** alrededor del metal y
el **histograma de HU dentro de `M`**. Se comparan despues contra los mismos estadisticos medidos en
implantes reales (`a12_roi_parametros.py`). Por eso acepta **varios checkpoints** y los corre
**pareados**: mismos cortes, misma pose, misma semilla.

NUNCA TOCA TEST
---------------
Aborta si el paciente no esta en las particiones pedidas. Por omision, `val`.

USO
---
    python a15_cadena_completa.py --caso dataset6_CLINIC_0101_data
    python a15_cadena_completa.py --caso dataset6_CLINIC_0101_data --cortes 0   # todos
    python a15_cadena_completa.py --caso dataset6_CLINIC_0101_data --cortes 0 --semillas 0 1 2 3 4

COTEJO DE CHECKPOINT (01-decisiones.md 2026-10-07 (2) y 2026-10-08 (2))
-------------------------------------------------------------------------
Con `--semillas`, cada checkpoint se genera una vez por semilla y, ademas de lo anterior, escribe
`_cotejo.csv`: perfil 2D en cascaras de 0.5 mm (o las de `--pasos-cotejo-mm`, columna `paso_mm`) con la elevacion de la mediana y del p95 sobre el anillo
de 12-15 mm, agregado corte -> paciente por semilla, y el histograma dentro de `M` sobre voxeles
> 2500 HU. Lo calcula `common.cotejo`, la misma funcion que mide la referencia real (`a17_cotejo.py`).
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
from pathlib import Path

import numpy as np
import torch

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src'))
sys.path.insert(0, str(_RAIZ / 'src' / 'renderizador'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo1'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo2'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from common.ventanas import DELTA_OBJ3, canales_diseno_a, codifica_bloque, decodifica_bloque  # noqa: E402
from common.region import componer, verificar_composicion  # noqa: E402
from difusion import Difusion, muestrea_ddim  # noqa: E402
from modelo import UNetDifusion  # noqa: E402
from a11_rasterizar_tornillo import rasteriza, D_CUERPO_MM, BANDA_MM, METAL_HU  # noqa: E402
from a1b_parches_componente import ventana_coords  # noqa: E402
from common.cotejo import agrega, bordes, histograma_m, perfil_corte  # noqa: E402

LADO = 256


def rellena(a: np.ndarray, valor, lado: int = LADO) -> np.ndarray:
    """Igual que `datos.ParchesMetal._rellena`: completa hasta `lado` con el valor de fondo."""
    h, w = a.shape
    if (h, w) == (lado, lado):
        return a
    out = np.full((lado, lado), valor, dtype=a.dtype)
    out[:min(h, lado), :min(w, lado)] = a[:lado, :lado]
    return out


def parche(vol, M, G, k, y0, x0, lado=LADO):
    """Recorta (hu, metal, g) del corte `k` en la ventana dada, con el relleno del entrenamiento."""
    sl = (slice(y0, y0 + lado), slice(x0, x0 + lado))
    return (rellena(vol[k][sl], -1000.0),
            rellena(M[k][sl], False),
            rellena(G[k][sl], False))


def cond_de(vol, M, G, k, y0, x0, canales):
    """Los 8 canales del condicionamiento, en el orden exacto de `datos.ParchesMetal.__getitem__`."""
    _, m_c, g_c = parche(vol, M, G, k, y0, x0)
    ctx = []
    for j in (k - 1, k + 1):
        jj = j if 0 <= j < vol.shape[0] else k          # en el borde se repite el central
        hu_v, _, g_v = parche(vol, M, G, jj, y0, x0)
        hu_v = hu_v.copy()
        hu_v[g_v] = -1000.0                             # el vecino tambien lleva `G` borrada
        ctx.append(codifica_bloque(hu_v, canales) * 2.0 - 1.0)
    cond = np.concatenate(ctx + [m_c.astype(np.float32)[None], g_c.astype(np.float32)[None]], axis=0)
    return cond.astype(np.float32), g_c, m_c


def a_hu(bloque: torch.Tensor, delta: float | None = None) -> np.ndarray:
    u = (bloque.detach().cpu().numpy()[0] + 1.0) / 2.0
    return decodifica_bloque(u, delta=delta)


def estadisticos(hu: np.ndarray, M: np.ndarray, G: np.ndarray, esp, paso_mm: float):
    """Perfil radial de HU por cascaras desde `M`, e histograma dentro de `M`.

    Son los dos estadisticos del criterio de seleccion de modelo (DEC 2026-10-05 (6)). Se eligieron
    porque **se miden sin verdad de terreno**, que es lo que permite compararlos contra implantes
    reales, donde no existe una version sin metal del mismo paciente.
    """
    from scipy import ndimage as ndi
    dist = ndi.distance_transform_edt(~M, sampling=esp)
    bordes = np.arange(0.0, BANDA_MM + paso_mm + 1e-9, paso_mm)
    perfil = []
    for i in range(len(bordes) - 1):
        sel = (dist > bordes[i]) & (dist <= bordes[i + 1]) & G
        if sel.sum() < 20:
            continue
        v = hu[sel]
        perfil.append({'r_lo_mm': round(float(bordes[i]), 2),
                       'r_hi_mm': round(float(bordes[i + 1]), 2),
                       'n': int(sel.sum()),
                       'hu_p50': round(float(np.median(v)), 1),
                       'hu_p05': round(float(np.percentile(v, 5)), 1),
                       'hu_p95': round(float(np.percentile(v, 95)), 1)})
    dentro = hu[M]
    hist = {'n_M': int(M.sum()),
            'hu_p05': round(float(np.percentile(dentro, 5)), 1),
            'hu_p25': round(float(np.percentile(dentro, 25)), 1),
            'hu_p50': round(float(np.median(dentro)), 1),
            'hu_p75': round(float(np.percentile(dentro, 75)), 1),
            'hu_p95': round(float(np.percentile(dentro, 95)), 1),
            'frac_sobre_2500': round(float((dentro > METAL_HU).mean()), 4)}
    return perfil, hist


def resumen_marcas(marcas: dict, canales: dict, sal: np.ndarray, ruta: str) -> None:
    """Guarda el `u` crudo de los 3 canales dentro de `M` y dice que marca LW donde la `regla` da techo.

    Responde a #152: los HU bajos dentro de `M` caen en los techos de SW (~236) y MW (~472). Si LW marca
    metal en esos voxeles, el modelo genero metal y la `regla` lo oculto; si no, el modelo no lo genero.
    """
    k = np.concatenate(marcas['k'])
    y = np.concatenate(marcas['y'])
    x = np.concatenate(marcas['x'])
    u = np.concatenate(marcas['u'])
    hu_regla = sal[k, y, x].astype(np.float32)
    hu_lw = np.asarray(canales['LW'][1](u[:, 0]), dtype=np.float32)
    np.savez_compressed(ruta, k=k, y=y, x=x, u=u, hu_regla=hu_regla, hu_lw=hu_lw)
    n = hu_regla.size
    print('  marcas dentro de `M`: n = %d -> %s' % (n, Path(ruta).name))
    for nom, lo, hi in (('techo SW', 200.0, 236.5), ('techo MW', 440.0, 472.5)):
        s = (hu_regla >= lo) & (hu_regla <= hi)
        if not s.any():
            print('    %s: 0 voxeles' % nom)
            continue
        print('    %s: %d voxeles (%.3f) | LW ahi: p05 %.0f p50 %.0f p95 %.0f HU, sobre %.0f: %.3f'
              ' | u_MW p50 %.4f | u_SW p50 %.4f'
              % (nom, s.sum(), s.mean(), np.percentile(hu_lw[s], 5), np.median(hu_lw[s]),
                 np.percentile(hu_lw[s], 95), METAL_HU, (hu_lw[s] > METAL_HU).mean(),
                 np.median(u[s, 1]), np.median(u[s, 2])))
    print('    LW sola en toda `M`: sobre %.0f HU = %.3f (la `regla` da %.3f)'
          % (METAL_HU, (hu_lw > METAL_HU).mean(), (hu_regla > METAL_HU).mean()), flush=True)


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--caso', required=True)
    ap.add_argument('--ejes', type=Path,
                    default=aqui.parent / 'objetivo2' / 'outputs' / 'e9ts_ejes_corredor.csv')
    ap.add_argument('--modo', default='default6mm')
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--particiones', nargs='+', default=['val'])
    ap.add_argument('--ckpt', type=Path, nargs='+',
                    default=[aqui / 'outputs' / 'a7' / 'run01' / 'ckpt.pt',
                             aqui / 'outputs' / 'a7' / 'run02' / 'mejor.pt'])
    ap.add_argument('--etiquetas', nargs='+', default=['run01_140k', 'mejor_37k'])
    ap.add_argument('--diam-cuerpo', type=float, default=D_CUERPO_MM)
    ap.add_argument('--banda-mm', type=float, default=BANDA_MM)
    ap.add_argument('--perturbar', action='store_true',
                    help='usa una pose perturbada del muestreador en vez del eje central del corredor')
    ap.add_argument('--semilla-pose', type=int, default=0)
    ap.add_argument('--cortes', type=int, default=24, help='0 = todos los cortes con `M`')
    ap.add_argument('--pasos', type=int, default=50)
    ap.add_argument('--semilla', type=int, default=0)
    ap.add_argument('--semillas', type=int, nargs='+', default=None,
                    help='una generacion por semilla y salida `_cotejo.csv` (cotejo de checkpoint)')
    ap.add_argument('--paso-perfil-mm', type=float, default=1.0)
    ap.add_argument('--pasos-cotejo-mm', type=float, nargs='+', default=[0.5],
                    help='ancho de las cascaras del `_cotejo.csv` (columna `paso_mm`); varios a la vez')
    ap.add_argument('--nifti', action='store_true', default=True)
    ap.add_argument('--sin-nifti', dest='nifti', action='store_false',
                    help='no escribe los volumenes .nii.gz (ahorra memoria; perfil, resumen y marcas si)')
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a15')
    ap.add_argument('--delta', type=float, default=DELTA_OBJ3,
                    help='rampa de la lectura `regla_suave` (v2, #152); por omision la decidida, 0.05')
    ap.add_argument('--regla-v1', dest='delta', action='store_const', const=None,
                    help='lee con la `regla` v1 del Objetivo 1, solo para reproducir corridas anteriores')
    ap.add_argument('--dispositivo', default='cpu',
                    help="'cpu' o 'cuda'. Con la misma semilla CPU y GPU NO dan el mismo ruido: "
                         'no mezclar dispositivos entre pacientes de un mismo cotejo')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    if len(args.etiquetas) != len(args.ckpt):
        raise SystemExit('--etiquetas y --ckpt tienen que tener la misma longitud')
    if 'test' in [p.lower() for p in args.particiones]:
        raise SystemExit('CONTROL: se pidio test. Abortado (Strict Isolation Rule, main.tex:111).')

    import nibabel as nib
    from p1_decodificador_sd15 import leer_particion, rutas
    from e6b_vae_sd15 import eje_axial

    # --- paciente y pose -------------------------------------------------------------------------
    filas = leer_particion(args.particion)
    permitidos = {f['Caso'] for f in filas if f['particion'] in args.particiones}
    if args.caso not in permitidos:
        raise SystemExit('%s no esta en %s' % (args.caso, args.particiones))
    ubic = rutas([f for f in filas if f['Caso'] == args.caso], list(args.data))
    if args.caso not in ubic:
        raise SystemExit('no se hallo el volumen de %s' % args.caso)

    with open(args.ejes, newline='', encoding='utf-8') as fh:
        cand = [r for r in csv.DictReader(fh)
                if r['Caso'] == args.caso and r['modo'] == args.modo and not r['Error']]
    if not cand:
        raise SystemExit('sin eje para %s en modo %s' % (args.caso, args.modo))
    e = cand[0]
    c = np.array([float(e['c_x_mm']), float(e['c_y_mm']), float(e['c_z_mm'])])
    u = np.array([float(e['u_x']), float(e['u_y']), float(e['u_z'])])
    largo = float(e['L_TS_mejor_mm'])
    print('caso %s | D_TS_max %.1f mm | largo del corredor %.1f mm'
          % (args.caso, float(e['D_TS_max_mm']), largo))
    if float(e['D_TS_max_mm']) < args.diam_cuerpo:
        print('  AVISO: el corredor medido (%.1f mm) es MAS ESTRECHO que el cuerpo del tornillo '
              '(%.2f mm). El tornillo perforara por construccion.'
              % (float(e['D_TS_max_mm']), args.diam_cuerpo))
    if args.perturbar:
        from muestreador.muestreo import muestrear_poses, rng_de_caso
        cs, us = muestrear_poses(c, u, largo, 1, rng_de_caso(args.caso, args.semilla_pose))
        c, u = cs[0], us[0]
        print('  pose perturbada por el muestreador del Objetivo 2 (semilla %d)' % args.semilla_pose)

    # --- volumen y mascaras ----------------------------------------------------------------------
    img = nib.load(ubic[args.caso])
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = np.array(img.header.get_zooms()[:3], dtype=float)
    M3, G3, meta = rasteriza(arr.shape[:3], zooms, c, u, largo, args.diam_cuerpo,
                             True, False, 0.0, args.banda_mm)
    plano = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)
    M = np.moveaxis(M3, eje, 0)
    G = np.moveaxis(G3, eje, 0)
    esp2d = (zooms[plano[0]], zooms[plano[1]])
    esp3d = (zooms[eje], zooms[plano[0]], zooms[plano[1]])
    print('volumen %s | `M` %d voxeles | `G` %d | diametro medido %.2f mm'
          % (vol.shape, int(M.sum()), int(G.sum()), meta['d_medido_mm']))

    # CONTROL 1: receptor limpio
    n_sobre = int((vol[G] > METAL_HU).sum())
    print('CONTROL 1 receptor limpio: voxeles del original en `G` sobre %.0f HU = %d -> %s'
          % (METAL_HU, n_sobre, 'PASA' if n_sobre == 0 else 'FALLA'))
    if n_sobre:
        raise SystemExit('el receptor no esta limpio: no sirve para el caso de uso de sintesis')

    ks = [k for k in range(vol.shape[0]) if M[k].any()]
    if not ks:
        raise SystemExit('`M` no toca ningun corte')
    if args.cortes:
        idx = np.linspace(0, len(ks) - 1, min(args.cortes, len(ks))).round().astype(int)
        ks = [ks[i] for i in sorted(set(idx))]
    print('cortes con `M`: %d | se generan %d' % (sum(1 for k in range(vol.shape[0]) if M[k].any()),
                                                  len(ks)))

    ventanas = {}
    for k in ks:
        ys, xs = np.nonzero(M[k])
        y0, x0, cabe = ventana_coords(ys, xs, vol.shape[1], vol.shape[2], LADO)
        ventanas[k] = (y0, x0, cabe)
    n_no_cabe = sum(1 for v in ventanas.values() if not v[2])
    if n_no_cabe:
        print('  AVISO: en %d cortes el componente no cabe en la ventana de %d' % (n_no_cabe, LADO))

    canales = canales_diseno_a()
    dif = Difusion()
    semillas = args.semillas if args.semillas else [args.semilla]
    total = len(ks) * len(args.ckpt) * len(semillas)
    print('generaciones: %d (%d cortes x %d checkpoints x %d semillas)'
          % (total, len(ks), len(args.ckpt), len(semillas)))
    cotejo = []

    resumen = []
    t0 = time.time()
    hecho = 0
    for ruta_ck, et in zip(args.ckpt, args.etiquetas):
        ck = torch.load(ruta_ck, map_location='cpu', weights_only=False)
        modelo = UNetDifusion(base=int(ck.get('meta', {}).get('base', 64)))
        modelo.load_state_dict(ck['modelo'])
        modelo.to(args.dispositivo).eval()
        print('\n--- %s (paso %s) | %s ---' % (et, ck.get('paso'), args.dispositivo), flush=True)

        for semilla in semillas:
            sal = vol.copy()
            marcas = {'k': [], 'y': [], 'x': [], 'u': []}   # `u` crudo de los 3 canales dentro de `M` (#152)
            for k in ks:
                y0, x0, _ = ventanas[k]
                cond, g_c, m_c = cond_de(vol, M, G, k, y0, x0, canales)
                hu_c, _, _ = parche(vol, M, G, k, y0, x0)
                gt = torch.from_numpy(g_c.astype(np.float32)[None])[None].to(args.dispositivo)
                with torch.no_grad():
                    gen = muestrea_ddim(modelo, torch.from_numpy(cond)[None].to(args.dispositivo), gt,
                                        dif, pasos=args.pasos, semilla=semilla).cpu()
                # CONTROL 2: cero exacto fuera de `G`
                fuera = float(np.abs(gen.numpy()[0][:, ~g_c]).max()) if (~g_c).any() else 0.0
                if fuera != 0.0:
                    raise RuntimeError('corte %d: lo generado no es cero fuera de G (%.3e)' % (k, fuera))
                hu_sal = componer(hu_c, a_hu(gen, args.delta), g_c)
                verificar_composicion(hu_c, hu_sal, g_c)   # CONTROL 3
                h = min(LADO, vol.shape[1] - y0)
                w = min(LADO, vol.shape[2] - x0)
                sal[k, y0:y0 + h, x0:x0 + w] = hu_sal[:h, :w]
                yy, xx = np.nonzero(m_c[:h, :w])
                u_c = (gen.numpy()[0] + 1.0) / 2.0                   # (3, LADO, LADO), orden LW, MW, SW
                marcas['k'].append(np.full(yy.size, k, dtype=np.int32))
                marcas['y'].append((yy + y0).astype(np.int32))
                marcas['x'].append((xx + x0).astype(np.int32))
                marcas['u'].append(u_c[:, yy, xx].T.astype(np.float32))
                hecho += 1
                if hecho % 8 == 0:
                    tr = (time.time() - t0) / hecho * (total - hecho) / 60
                    print('  [%d/%d] corte %d | faltan ~%.0f min' % (hecho, total, k, tr), flush=True)

            sel = np.zeros_like(M)
            sel[ks] = True
            Ms, Gs = M & sel, G & sel
            perfil, hist = estadisticos(sal, Ms, Gs, esp3d, args.paso_perfil_mm)
            print('  HU dentro de `M`: p05 %.0f | p50 %.0f | p95 %.0f | fraccion sobre %.0f HU: %.3f'
                  % (hist['hu_p05'], hist['hu_p50'], hist['hu_p95'], METAL_HU, hist['frac_sobre_2500']))
            resumen.append(dict(etiqueta=et, paso=ck.get('paso'), semilla=semilla, **hist))
            if args.semillas:
                h2 = histograma_m(sal[Ms])
                for paso_c in args.pasos_cotejo_mm:
                    prf = agrega([perfil_corte(sal[k], M[k], esp2d, paso=paso_c) for k in ks])
                    b = bordes(paso_c)
                    for i in range(len(b) - 1):
                        cotejo.append({'caso': args.caso, 'etiqueta': et, 'semilla': semilla, 'paso_mm': paso_c,
                                       'r_lo_mm': b[i], 'r_hi_mm': b[i + 1],
                                       'elev_p50': round(float(prf[i, 0]), 2),
                                       'elev_p95': round(float(prf[i, 1]), 2),
                                       'M_p50': h2['hu_p50'], 'M_p75': h2['hu_p75'], 'M_p95': h2['hu_p95'],
                                       'M_frac_sobre_2500': h2['frac_sobre_2500']})
                print('  cotejo semilla %d: cascaras de %s mm | M>2500 p50 %.0f'
                      % (semilla, '/'.join('%g' % x for x in args.pasos_cotejo_mm), h2['hu_p50']), flush=True)

            base = args.out_dir / ('a15_%s_%s' % (args.caso, et)
                                   + ('_s%d' % semilla if args.semillas else ''))
            resumen_marcas(marcas, canales, sal, str(base) + '_marcas.npz')
            with open(str(base) + '_perfil.csv', 'w', newline='', encoding='utf-8') as fh:
                w_ = csv.DictWriter(fh, fieldnames=list(perfil[0].keys()))
                w_.writeheader()
                w_.writerows(perfil)
            if args.nifti:
                afin = np.diag([esp3d[1], esp3d[2], esp3d[0], 1.0])
                nib.save(nib.Nifti1Image(np.ascontiguousarray(np.moveaxis(sal, 0, 2),
                                                              dtype=np.float32), afin),
                         str(base) + '_sintetica.nii.gz')
            print('  salidas: %s_*' % base.name)

    # --- original y mascaras, una sola vez -------------------------------------------------------
    if args.nifti:
        afin = np.diag([esp3d[1], esp3d[2], esp3d[0], 1.0])
        for nom, v in (('original', vol), ('M', M.astype(np.float32)), ('G', G.astype(np.float32))):
            nib.save(nib.Nifti1Image(np.ascontiguousarray(np.moveaxis(v, 0, 2), dtype=np.float32),
                                     afin),
                     args.out_dir / ('a15_%s_%s.nii.gz' % (args.caso, nom)))

    ruta = args.out_dir / ('a15_%s_resumen.csv' % args.caso)
    with open(ruta, 'w', newline='', encoding='utf-8') as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(resumen[0].keys()))
        w_.writeheader()
        w_.writerows(resumen)
    print('\nresumen: %s' % ruta)
    if cotejo:
        ruta = args.out_dir / ('a15_%s_cotejo.csv' % args.caso)
        with open(ruta, 'w', newline='', encoding='utf-8') as fh:
            w_ = csv.DictWriter(fh, fieldnames=list(cotejo[0].keys()))
            w_.writeheader()
            w_.writerows(cotejo)
        print('cotejo: %s' % ruta)
    print('\nLos dos estadisticos de aqui se comparan contra los de implantes REALES, que calcula\n'
          '`a12_roi_parametros.py` sobre los pacientes de validacion. Ese cotejo es el criterio de\n'
          'seleccion de checkpoint fijado en `01-decisiones.md` 2026-10-05 (6). **Ningun checkpoint\n'
          'queda elegido por este script**: aqui se mide, la eleccion es de la autora.')


if __name__ == '__main__':
    main()
