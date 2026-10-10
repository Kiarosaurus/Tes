"""A19 - brazo fisico de Peters completo (D4; sonda viable en `sonda_peters.md`; #159 opcion 2).

QUE HACE
--------
Para cada paciente receptor, con el tornillo en la misma pose que el difusor (eje del corredor de E9-TS, como
`a15`), simula con XCIST **cortes axiales alternos** de todos los que toca `G` (`--k 2`, salida preinscrita de
la sonda por coste). Por corte, siete simulaciones con el pipeline de `a18` (fantoma `(HU+1000)/1000`, realce
de frecuencias del repositorio AAPM y la misma `M` binaria):

    calibracion (solo para el realce) | sin metal A | sin metal B | Fe A | Fe B | Ti A | Ti B

- **A/B = test-retest** del brazo fisico (01-decisiones 2026-10-08 pto 13). Es un componente de `Delta`.
- **Fe** = material preinscrito (sustituto del acero, que XCIST no trae). **Ti** = sensibilidad (#159,
  opcion 2, elegida por la autora el 2026-10-09).
- Ruido de Poisson sin semilla fijable (DLL/so de XCIST): todas las simulaciones de un corte corren en serie
  dentro del mismo proceso, asi que A y B tienen realizaciones distintas (verificado en la sonda).

NO calcula la `streak amplitude`: guarda los cortes reconstruidos y la geometria. Las ROIs de E-A2 (planos
perpendiculares a `u`) las mide el evaluador comun, igual para el difusor y para este brazo.

PARTICION: por omision solo validacion (`Delta` se mide solo ahi, 01-decisiones 2026-10-05 (6)). Test
exige `--corrida-final`, que se usa solo despues de congelar `diseno_A.md`.

USO
---
    python experiments/objetivo3/a19_peters_completo.py --casos dataset6_CLINIC_0101_data --trabajadores 8
    python experiments/objetivo3/a19_peters_completo.py --casos dataset6_CLINIC_0102_data --max-cortes 1   # humo
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import sys
import time
from multiprocessing import get_context
from pathlib import Path

os.environ.setdefault('TQDM_DISABLE', '1')          # XCIST imprime una barra por vista; en un log de Slurm sobra

import numpy as np

_AQUI = Path(__file__).resolve().parent
_RAIZ = _AQUI.parents[1]
sys.path.insert(0, str(_AQUI))
from a18_sonda_peters import realce, simula  # noqa: E402  (mismo pipeline que la sonda)

METAL_HU = 2500.0
CONDICIONES = [('limpia_A', None, 1), ('limpia_B', None, 2), ('Fe_A', 'Fe', 11), ('Fe_B', 'Fe', 12),
               ('Ti_A', 'Ti', 21), ('Ti_B', 'Ti', 22)]


def geometria(caso: str, data: list[Path], particion: Path, permitidas: list[str], ejes: Path, modo: str):
    """Volumen axial, `M`, `G`, espaciado y pose, exactamente como `a15` (pose = eje del corredor)."""
    import nibabel as nib
    sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo1'))
    from p1_decodificador_sd15 import leer_particion, rutas
    from e6b_vae_sd15 import eje_axial
    from a11_rasterizar_tornillo import BANDA_MM, D_CUERPO_MM, rasteriza
    filas = [f for f in leer_particion(particion) if f['Caso'] == caso]
    if not filas or filas[0]['particion'] not in permitidas:
        raise SystemExit('CONTROL: %s no esta en %s' % (caso, permitidas))
    ubic = rutas(filas, data)
    with open(ejes, newline='', encoding='utf-8') as fh:
        cand = [r for r in csv.DictReader(fh) if r['Caso'] == caso and r['modo'] == modo and not r['Error']]
    if not cand:
        raise SystemExit('sin eje para %s en modo %s' % (caso, modo))
    e = cand[0]
    c = np.array([float(e['c_x_mm']), float(e['c_y_mm']), float(e['c_z_mm'])])
    u = np.array([float(e['u_x']), float(e['u_y']), float(e['u_z'])])
    img = nib.load(ubic[caso])
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = np.array(img.header.get_zooms()[:3], dtype=float)
    M3, G3, _ = rasteriza(arr.shape[:3], zooms, c, u, float(e['L_TS_mejor_mm']), D_CUERPO_MM,
                          True, False, 0.0, BANDA_MM)
    plano = [i for i in range(3) if i != eje]
    vol, M, G = (np.moveaxis(x, eje, 0) for x in (arr, M3, G3))
    if int((vol[G] > METAL_HU).sum()):
        raise SystemExit('CONTROL receptor limpio FALLA en %s: hay metal en `G`' % caso)
    pose = {'c_mm': c.tolist(), 'u': u.tolist(), 'largo_mm': float(e['L_TS_mejor_mm']), 'eje_axial': int(eje),
            'zooms': zooms.tolist(), 'plano': plano, 'D_TS_max_mm': float(e['D_TS_max_mm'])}
    return vol, M, G, (float(zooms[plano[0]]), float(zooms[plano[1]])), pose


def un_corte(tarea: dict) -> dict:
    """Las siete simulaciones de un corte, en serie y en este proceso. Devuelve imagenes y controles."""
    orig = np.maximum(tarea['orig'], -1000.0)          # relleno del escaner (-2048) = aire (sonda, corrida 1)
    m, pix, d = tarea['M'], tarea['pix'], Path(tarea['dir'])
    vf0 = ((orig + 1000.0) / 1000.0).astype(np.float32)
    t0 = time.time()
    rec0, _ = simula(d / 'cal', vf0, None, None, pix, 0)
    corr = float(np.corrcoef(rec0.ravel(), orig.ravel())[0, 1])
    vfb, _ = realce(vf0, orig, rec0)
    out = {'k': tarea['k'], 'corr_calibracion': corr}
    blando = (orig > -100) & (orig < 100)
    for nom, mat, sem in CONDICIONES:
        img, _ = simula(d / nom, vfb, m if mat else None, mat, pix, sem + 100 * tarea['k'])
        out[nom] = img.astype(np.float32)
    # control (no criterio): sesgo sin metal en tejido blando, como V2 de la sonda; se cancela en Fe - limpia
    out['sesgo_blando_HU'] = float(np.median((out['limpia_A'] - orig)[blando])) if blando.any() else float('nan')
    out['segundos'] = time.time() - t0
    shutil.rmtree(d, ignore_errors=True)               # sinogramas intermedios: ~25 MB por corte
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--casos', nargs='+', default=['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data'])
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--particion', type=Path, default=_AQUI.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--ejes', type=Path, default=_AQUI.parent / 'objetivo2' / 'outputs' / 'e9ts_ejes_corredor.csv')
    ap.add_argument('--modo', default='default6mm')
    ap.add_argument('--k', type=int, default=2, help='un corte de cada k entre los que toca `G` (sonda: k = 2)')
    ap.add_argument('--trabajadores', type=int, default=max(1, (os.cpu_count() or 2) // 2))
    ap.add_argument('--max-cortes', type=int, default=0, help='solo para humo: 0 = todos')
    ap.add_argument('--corrida-final', action='store_true',
                    help='permite test; solo tras congelar diseno_A.md (orden 2026-10-05 (6))')
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'a19')
    ap.add_argument('--tmp-dir', type=Path, default=None, help='directorio de trabajo de XCIST (por omision, out-dir/tmp)')
    args = ap.parse_args()
    permitidas = ['val', 'test'] if args.corrida_final else ['val']
    args.out_dir.mkdir(parents=True, exist_ok=True)
    tmp = args.tmp_dir or (args.out_dir / 'tmp')

    for caso in args.casos:
        vol, M, G, esp2d, pose = geometria(caso, list(args.data), args.particion, permitidas, args.ejes, args.modo)
        if abs(esp2d[0] - esp2d[1]) > 1e-3 or vol.shape[1] != vol.shape[2]:
            raise SystemExit('%s: se esperaba corte cuadrado con pixel isotropo' % caso)
        ks_g = [k for k in range(vol.shape[0]) if G[k].any()]
        ks = ks_g[::args.k]
        if args.max_cortes:
            ks = ks[:args.max_cortes]
        print('%s | cortes con G %d -> simulados %d (k = %d) | %d trabajadores'
              % (caso, len(ks_g), len(ks), args.k, args.trabajadores), flush=True)
        tareas = [{'k': k, 'orig': vol[k].astype(np.float32), 'M': M[k], 'pix': esp2d[0],
                   'dir': str(tmp / caso / ('k%04d' % k))} for k in ks]
        t0 = time.time()
        res = []
        with get_context('spawn').Pool(args.trabajadores) as pool:
            for i, r in enumerate(pool.imap_unordered(un_corte, tareas), 1):
                res.append(r)
                print('  [%d/%d] corte %d | %.0f s | corr calibracion %.3f' % (i, len(ks), r['k'], r['segundos'],
                                                                              r['corr_calibracion']), flush=True)
        res.sort(key=lambda r: r['k'])
        idx = [ks.index(r['k']) for r in res]
        npz = args.out_dir / ('a19_%s.npz' % caso)
        np.savez_compressed(npz, ks=np.array(ks), original=vol[ks], M=M[ks], G=G[ks],
                            **{nom: np.stack([r[nom] for r in res]) for nom, _, _ in CONDICIONES})
        corr = [r['corr_calibracion'] for r in res]
        meta = {'caso': caso, 'pose': pose, 'pixel_mm': esp2d, 'k': args.k, 'cortes_G': len(ks_g),
                'cortes_simulados': ks, 'corr_calibracion_min': min(corr), 'corr_calibracion_mediana': float(np.median(corr)),
                'sesgo_blando_HU_mediana': float(np.nanmedian([r['sesgo_blando_HU'] for r in res])),
                'sesgo_blando_HU_max_abs': float(np.nanmax(np.abs([r['sesgo_blando_HU'] for r in res]))),
                'segundos_por_corte_mediana': float(np.median([r['segundos'] for r in res])),
                'segundos_total': time.time() - t0, 'condiciones': [c[0] for c in CONDICIONES],
                'gecatsim': __import__('importlib.metadata', fromlist=['version']).version('gecatsim'),
                'orden_ok': idx == sorted(idx)}
        (args.out_dir / ('a19_%s.json' % caso)).write_text(json.dumps(meta, indent=2), encoding='utf-8')
        aviso = '' if min(corr) >= 0.95 else '  AVISO: algun corte con correlacion de calibracion < 0.95'
        print('%s listo: %s | %.1f h | corr min %.3f%s' % (caso, npz.name, meta['segundos_total'] / 3600, min(corr), aviso),
              flush=True)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
