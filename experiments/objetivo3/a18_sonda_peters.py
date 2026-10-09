"""A18 - sonda de viabilidad del brazo fisico de Peters (protocolo: `sonda_peters.md`, 01-decisiones 2026-10-09 (2)).

QUE HACE
--------
Un corte de un receptor limpio de validacion con el tornillo de `a15`, simulado con XCIST segun la
configuracion del ejemplo AAPM (`peters/AAPM_MAR_*.cfg`). Cinco simulaciones:

0. **Pasada de calibracion** sin metal, solo para el realce de frecuencias del repositorio AAPM.
1. Sin metal (A).   2. Sin metal (B, test-retest).   3. Con `Fe` (sustituto del acero; XCIST no trae acero).
4. Con `Ti` (sensibilidad).

**Ruido independiente en cada simulacion.** El ruido de Poisson lo genera la biblioteca C de XCIST
(`rndpoi`), y la DLL de Windows no exporta `setall`, asi que no se puede fijar la semilla. Por eso
`Delta_fis = Fe - A` y la referencia de ruido `A - B` llevan, las dos, dos realizaciones independientes:
misma estructura de ruido, comparacion justa.

**Fantoma** (fuente: `repos/xcist-example/AAPM_datachallenge/simulation_scripts/readme.md`):
- agua con densidad relativa `(HU + 1000) / 1000`, como en el repositorio;
- realce de frecuencias del documento `AAPM_freq_boost.docx`: cociente de las medias radiales de la FFT
  original/reconstruida, aplicado en 2D y calculado para cada imagen. El tope del cociente, [0.5, 3], es
  propio: el documento no lo da.
- metal: la misma `M` binaria que usa el difusor (y binaria como en Peters). Dentro de `M` el agua del
  paciente se pone a 0 en vez de restarle densidad 1 (`run.py` resta 1, lo que deja hueso residual bajo el
  metal). Desviacion declarada.

**Medidas y criterios:** V1, V2 y V3 de `sonda_peters.md`, fijados antes de correr. El estadistico de
artefacto es el de Peters (promedio del 5 % superior menos el del 5 % inferior de la desviacion), en un
anillo axial de una guarda de un pixel a 12 mm alrededor de `M`. Es una adaptacion de la sonda: en E-A2 los
anillos estan en planos perpendiculares al eje del tornillo, y aqui hay un solo corte axial.

USO
---
    python experiments/objetivo3/a18_sonda_peters.py                     # 0101, salida en outputs/a18/
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import sys
import time
from pathlib import Path

import numpy as np

_RAIZ = Path(__file__).resolve().parents[2]
_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_RAIZ / 'src'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo1'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo2'))
sys.path.insert(0, str(_AQUI))

from a11_rasterizar_tornillo import BANDA_MM, D_CUERPO_MM, rasteriza  # noqa: E402

CFGS = ['AAPM_MAR_phantom.cfg', 'AAPM_MAR_protocol.cfg', 'AAPM_MAR_physics.cfg', 'AAPM_MAR_scanner.cfg',
        'AAPM_MAR_recon.cfg']
TOPE_REALCE = (0.5, 3.0)
V2_HU = 20.0
V3_VECES = 3.0
V1_HORAS = 72.0
RECORTE_EXTREMO_MM = 8.0
N_E_A2 = 14


def carga_corte(caso: str, data: list[Path], particion: Path, ejes: Path, modo: str):
    """Volumen, `M` (como en `a15`) y el corte con mayor area de `M`."""
    import nibabel as nib
    from p1_decodificador_sd15 import leer_particion, rutas
    from e6b_vae_sd15 import eje_axial
    filas = leer_particion(particion)
    fila = [f for f in filas if f['Caso'] == caso]
    if not fila or fila[0]['particion'] != 'val':
        raise SystemExit('CONTROL: %s no esta en validacion' % caso)
    ubic = rutas(fila, data)
    with open(ejes, newline='', encoding='utf-8') as fh:
        e = [r for r in csv.DictReader(fh) if r['Caso'] == caso and r['modo'] == modo and not r['Error']][0]
    c = np.array([float(e['c_x_mm']), float(e['c_y_mm']), float(e['c_z_mm'])])
    u = np.array([float(e['u_x']), float(e['u_y']), float(e['u_z'])])
    img = nib.load(ubic[caso])
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = np.array(img.header.get_zooms()[:3], dtype=float)
    M3, G3, _ = rasteriza(arr.shape[:3], zooms, c, u, float(e['L_TS_mejor_mm']), D_CUERPO_MM,
                         True, False, 0.0, BANDA_MM)
    plano = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)
    M = np.moveaxis(M3, eje, 0)
    n_g = int(np.moveaxis(G3, eje, 0).reshape(M.shape[0], -1).any(1).sum())
    areas = M.reshape(M.shape[0], -1).sum(1)
    k = int(np.argmax(areas))
    ks = np.nonzero(areas)[0]
    n_eval = int((((ks - ks.min()) * zooms[eje] >= RECORTE_EXTREMO_MM)
                  & ((ks.max() - ks) * zooms[eje] >= RECORTE_EXTREMO_MM)).sum())
    esp2d = (float(zooms[plano[0]]), float(zooms[plano[1]]))
    return vol[k].astype(np.float32), M[k], esp2d, k, len(ks), max(n_eval, 1), n_g


def simula(dirtrab: Path, vf_paciente: np.ndarray, metal: np.ndarray | None, material: str | None,
           pix_mm: float, semilla: int) -> tuple[np.ndarray, float]:
    """Una simulacion XCIST + reconstruccion FDK en `dirtrab`; devuelve la imagen en HU y los segundos."""
    import gecatsim as xc
    from gecatsim.reconstruction.pyfiles import recon
    dirtrab.mkdir(parents=True, exist_ok=True)
    for f in CFGS:
        shutil.copy(_AQUI / 'peters' / f, dirtrab / f)
    n = vf_paciente.shape[0]
    vf = vf_paciente.copy()
    capas = [('water', 'phantom.vf')]
    if metal is not None:
        vf[metal] = 0.0
        np.ascontiguousarray(metal.astype(np.float32)).tofile(dirtrab / 'metal.vf')
        capas.append((material, 'metal.vf'))
    np.ascontiguousarray(vf.astype(np.float32)).tofile(dirtrab / 'phantom.vf')
    js = {'n_materials': len(capas), 'mat_name': [m for m, _ in capas],
          'volumefractionmap_filename': [f for _, f in capas],
          'volumefractionmap_datatype': ['float'] * len(capas), 'cols': [n] * len(capas),
          'rows': [n] * len(capas), 'slices': [1] * len(capas), 'x_size': [pix_mm] * len(capas),
          'y_size': [pix_mm] * len(capas), 'z_size': [100.0] * len(capas),
          'x_offset': [n / 2 + 0.5] * len(capas), 'y_offset': [n / 2 + 0.5] * len(capas),
          'z_offset': [1.0] * len(capas), 'density_scale': [1.0] * len(capas)}
    (dirtrab / 'sim.json').write_text(json.dumps(js, indent=2))
    cwd = os.getcwd()
    os.chdir(dirtrab)
    try:
        t0 = time.time()
        ct = xc.CatSim(*[f[:-4] for f in CFGS])
        ct.resultsName = 'out'
        ct.recon.fov = n * pix_mm
        np.random.seed(semilla)          # solo el ruido electronico de numpy; el de Poisson va en C sin semilla
        ct.run_all()
        cfg = ct.get_current_cfg()
        cfg.do_Recon = 1
        cfg.waitForKeypress = 0
        recon.recon(cfg)
        seg = time.time() - t0
        sal = sorted(dirtrab.glob('out_%dx%dx1.raw' % (n, n)))
        img = np.fromfile(sal[0], dtype=np.float32).reshape(n, n)
    finally:
        os.chdir(cwd)
    return img, seg


def realce(vf: np.ndarray, orig_hu: np.ndarray, rec_hu: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Realce de frecuencias del repositorio AAPM: cociente de medias radiales de |FFT| original/reconstruida."""
    n = vf.shape[0]
    fy, fx = np.meshgrid(np.fft.fftfreq(n), np.fft.fftfreq(n), indexing='ij')
    r = np.sqrt(fx ** 2 + fy ** 2)
    bins = np.minimum((r / r.max() * (n // 2)).astype(int), n // 2)
    A = np.abs(np.fft.fft2(orig_hu + 1000.0))
    B = np.abs(np.fft.fft2(rec_hu + 1000.0))
    ra = np.bincount(bins.ravel(), A.ravel()) / np.maximum(np.bincount(bins.ravel()), 1)
    rb = np.bincount(bins.ravel(), B.ravel()) / np.maximum(np.bincount(bins.ravel()), 1)
    cociente = np.clip(ra / np.maximum(rb, 1e-6), *TOPE_REALCE)
    out = np.real(np.fft.ifft2(np.fft.fft2(vf) * cociente[bins]))
    return np.maximum(out, 0.0).astype(np.float32), cociente


def amplitud(x: np.ndarray) -> float:
    """Estadistico de Peters: promedio del 5 % superior menos el del 5 % inferior."""
    x = np.sort(np.asarray(x, dtype=np.float64))
    m = max(1, int(round(0.05 * x.size)))
    return float(x[-m:].mean() - x[:m].mean())


def orienta(rec: np.ndarray, orig: np.ndarray) -> tuple[int, bool]:
    """Rotacion (k*90) y volteo que mejor alinean la reconstruccion con el original (correlacion)."""
    mejor = None
    for t in (False, True):
        for k in range(4):
            r = np.rot90(rec.T if t else rec, k)
            c = np.corrcoef(r.ravel(), orig.ravel())[0, 1]
            if mejor is None or c > mejor[0]:
                mejor = (c, k, t)
    return mejor[1], mejor[2]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--caso', default='dataset6_CLINIC_0101_data')
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--particion', type=Path, default=_AQUI.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--ejes', type=Path, default=_AQUI.parent / 'objetivo2' / 'outputs' / 'e9ts_ejes_corredor.csv')
    ap.add_argument('--modo', default='default6mm')
    ap.add_argument('--semillas', type=int, nargs=2, default=[1, 2], help='solo ruido electronico (numpy)')
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'a18')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    sA, sB = args.semillas

    orig, m, esp2d, k, n_cortes_m, n_eval, n_g = carga_corte(args.caso, list(args.data), args.particion,
                                                        args.ejes, args.modo)
    if abs(esp2d[0] - esp2d[1]) > 1e-3 or orig.shape[0] != orig.shape[1]:
        raise SystemExit('se esperaba un corte cuadrado con pixel isotropo: %s %s' % (orig.shape, esp2d))
    pix = esp2d[0]
    print('%s | corte %d | M %d px | pixel %.3f mm | cortes axiales con M %d, con G %d'
          % (args.caso, k, int(m.sum()), pix, n_cortes_m, n_g), flush=True)
    # El relleno del escaner fuera del FOV (-2048 HU) es aire para la fisica: se lleva a -1000 antes de todo
    # (corrida 1: sin esto, el realce se calculo con el relleno y metio +250 HU; ver `sonda_peters.md`).
    orig = np.maximum(orig, -1000.0)
    vf0 = ((orig + 1000.0) / 1000.0).astype(np.float32)

    tiempos = {}
    rec0, tiempos['calibracion'] = simula(args.out_dir / 'sim0_calibracion', vf0, None, None, pix, sA)
    rot, tr = orienta(rec0, orig)
    def al(x):  # noqa: E306
        return np.rot90(x.T if tr else x, rot)
    rec0 = al(rec0)
    print('orientacion: rot90 x%d, traspuesta %s | corr %.3f' % (rot, tr, np.corrcoef(rec0.ravel(), orig.ravel())[0, 1]))
    vfb, cociente = realce(vf0, orig, rec0)

    imgs = {}
    for nom, metal, mat, sem in (('limpia_A', None, None, sA), ('limpia_B', None, None, sB),
                                 ('Fe_A', m, 'Fe', sA + 10), ('Ti_A', m, 'Ti', sA + 20)):
        img, seg = simula(args.out_dir / ('sim_' + nom), vfb, metal, mat, pix, sem)
        imgs[nom] = al(img)
        tiempos[nom] = seg
        print('  %s: %.0f s' % (nom, seg), flush=True)

    from scipy import ndimage as ndi
    dist = ndi.distance_transform_edt(~m, sampling=esp2d)
    lab, nlab = ndi.label(orig > -500)            # cuerpo = el componente mayor; la camilla queda fuera
    tam = ndi.sum(np.ones_like(orig), lab, range(1, nlab + 1))
    cuerpo = ndi.binary_fill_holes(lab == 1 + int(np.argmax(tam)))
    anillo = (dist > min(esp2d)) & (dist <= 12.0) & ~m
    ref = (dist > 12.0) & (dist <= 15.0) & cuerpo
    blando = cuerpo & (orig > -100) & (orig < 100) & (dist > 15.0)

    # V1: truncamiento y coste
    yy, xx = np.mgrid[:orig.shape[0], :orig.shape[1]]
    centro = (orig.shape[0] - 1) / 2
    r_mm = np.hypot(yy - centro, xx - centro) * pix
    radio_fov = orig.shape[0] * pix / 2
    trunc = bool((r_mm[cuerpo] > radio_fov - 2 * pix).any())
    seg_sim = float(np.mean([tiempos[x] for x in ('limpia_A', 'limpia_B', 'Fe_A', 'Ti_A')]))
    horas = N_E_A2 * n_g * 2 * 2 * seg_sim / 3600   # todos los cortes axiales que toca `G`
    v1 = (not trunc) and horas <= V1_HORAS

    # V2: fidelidad sin metal
    d = imgs['limpia_A'] - orig
    sesgo_ref, sesgo_blando = float(np.median(d[ref])), float(np.median(d[blando]))
    v2 = abs(sesgo_ref) <= V2_HU and abs(sesgo_blando) <= V2_HU

    # V3: artefacto frente a ruido
    a_ruido = amplitud((imgs['limpia_A'] - imgs['limpia_B'])[anillo])
    a_fe = amplitud((imgs['Fe_A'] - imgs['limpia_A'])[anillo])
    a_ti = amplitud((imgs['Ti_A'] - imgs['limpia_A'])[anillo])
    v3 = a_fe >= V3_VECES * a_ruido

    np.savez_compressed(args.out_dir / 'a18_imagenes.npz', original=orig, M=m, **imgs, cociente=cociente)
    res = {'caso': args.caso, 'corte': k, 'pixel_mm': pix, 'M_px': int(m.sum()), 'orientacion_rot90': rot,
           'orientacion_traspuesta': tr, 'tiempos_s': tiempos, 'cortes_axiales_G_receptor': n_g,
           'horas_brazo_completo': horas, 'truncamiento': trunc, 'V1': v1,
           'sesgo_anillo_12_15_HU': sesgo_ref, 'sesgo_blando_HU': sesgo_blando, 'V2': v2,
           'amp_ruido_HU': a_ruido, 'amp_Fe_HU': a_fe, 'amp_Ti_HU': a_ti,
           'razon_Fe_ruido': a_fe / a_ruido if a_ruido else float('nan'), 'V3': v3,
           'HU_M_Fe_p50': float(np.median(imgs['Fe_A'][m])), 'HU_M_Ti_p50': float(np.median(imgs['Ti_A'][m]))}
    (args.out_dir / 'a18_resultado.json').write_text(json.dumps(res, indent=2, default=float))
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 5, figsize=(22, 5))
        for a, (t, x, w) in zip(ax, (('original', orig, (-160, 240)), ('sin metal (sim)', imgs['limpia_A'], (-160, 240)),
                                     ('Fe (sim)', imgs['Fe_A'], (-160, 240)),
                                     ('Fe - sin metal', imgs['Fe_A'] - imgs['limpia_A'], (-300, 300)),
                                     ('sin metal A - B', imgs['limpia_A'] - imgs['limpia_B'], (-300, 300)))):
            a.imshow(x, cmap='gray', vmin=w[0], vmax=w[1])
            a.contour(m, levels=[0.5], colors='r', linewidths=0.5)
            a.set_title(t)
            a.axis('off')
        fig.tight_layout()
        fig.savefig(args.out_dir / 'a18_sonda.png', dpi=90)
    except Exception as exc:  # la figura es apoyo, no resultado
        print('figura no generada: %s' % exc)

    sig = {True: 'PASA', False: 'FALLA'}
    L = ['# A18 — sonda de viabilidad del brazo fisico de Peters', '',
         'Protocolo y criterios: `sonda_peters.md` (fijados antes de correr). Caso `%s`, corte %d, `M` %d px.'
         % (args.caso, k, int(m.sum())), '',
         '| | Medida | Valor | Umbral | Veredicto |', '|---|---|---|---|---|',
         '| V1 | truncamiento del cuerpo | %s | no | %s |' % ('si' if trunc else 'no', sig[not trunc]),
         '| V1 | coste proyectado del brazo completo | %.1f h (%.0f s por simulacion x %d cortes con `G` x 14 x 2 x 2) | <= %.0f h | %s |'
         % (horas, seg_sim, n_g, V1_HORAS, sig[horas <= V1_HORAS]),
         '| V2 | sesgo sin metal, anillo 12-15 mm | %+.1f HU | +/-%.0f HU | %s |' % (sesgo_ref, V2_HU, sig[abs(sesgo_ref) <= V2_HU]),
         '| V2 | sesgo sin metal, tejido blando | %+.1f HU | +/-%.0f HU | %s |' % (sesgo_blando, V2_HU, sig[abs(sesgo_blando) <= V2_HU]),
         '| V3 | amplitud Fe / ruido test-retest | %.0f / %.0f HU = %.1fx | >= %.0fx | %s |'
         % (a_fe, a_ruido, res['razon_Fe_ruido'], V3_VECES, sig[v3]), '',
         'Titanio (sensibilidad, descriptivo): amplitud %.0f HU. Mediana dentro de `M`: Fe %.0f HU, Ti %.0f HU.'
         % (a_ti, res['HU_M_Fe_p50'], res['HU_M_Ti_p50']), '',
         '**Veredicto: %s.**' % ('VIABLE (V1, V2 y V3 pasan)' if (v1 and v2 and v3) else
                                 'NO VIABLE tal como se fijo: aplicar la salida preinscrita de `sonda_peters.md`'), '',
         'El coste usa los cortes axiales con `G` del receptor de validacion como proxy de los de test (no se tocan los de '
         'test). Orientacion de la reconstruccion alineada por correlacion con el original (rot90 x%d, traspuesta %s). '
         'La amplitud del difusor NO se calcula aqui (seria mirar el contraste primario).' % (rot, tr)]
    (args.out_dir / 'a18_sonda.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
