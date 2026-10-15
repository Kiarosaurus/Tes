"""A28 - mecanismo del p95 bajo lo real (#152, #157; DEC 2026-10-15 pto 7). POSTERIOR, validacion, no cambia nada.

Pregunta: el p95 sintetico queda bajo la envolvente real en 7 de 12 cascaras de 1 mm (`a17_paso1mm`, run04_mejor:
4, 5, 6, 8, 9, 10 y 11 mm). Es el decodificador (`regla_suave` deja los canales estrechos en sus techos) o el modelo?

1. **Sintetico.** `u` crudo de todo `G` guardado por `a15 --guardar-u-g` (Khipu `a15_diag.sbatch MODO=p95`;
   0101/0102, 5 semillas, delta 0.03). Se decodifica dos veces: `regla_suave` (delta 0.03, la de la corrida) y
   **solo LW** (asinh, [-1000, 20000]). Perfil de 1 mm con `common.cotejo` (el mismo de `a15`/`a17`); agregacion
   corte -> semilla -> paciente -> mediana entre pacientes, como `a17`. Control: la decodificacion `regla_suave`
   reproduce el `elev_p95` del `_cotejo.csv` de Khipu.
2. **Control real.** Los 2 tornillos de `metal_0039` (la referencia de `a17`): cada corte se codifica
   (`codifica_bloque`) y se decodifica de las dos formas; mismo perfil. Mide cuanto mueve el p95 el cambio de
   decodificacion sin modelo.
3. **Regla (DEC 2026-10-15 pto 7, fijada antes):** mecanismo = decodificador solo si (a) con LW el p95 sintetico entra
   en la envolvente real en >= 4 de las 7 cascaras **y** (b) en lo real el cambio de decodificacion mueve el p95
   menos de la mitad de lo que lo mueve en lo sintetico. Si no: modelo o indeterminado.
   **Operacionalizacion de (b), eleccion propia declarada:** mediana sobre las 7 cascaras de |corrimiento real| frente
   a 0.5 x mediana de |corrimiento sintetico|; se reporta tambien cascara por cascara.

USO:  python experiments/objetivo3/a28_diag_p95.py --dir-diag <.../diag_p95/run04_mejor>
Salida: outputs/obj3_pose/a28/a28_diag_p95.csv y .md
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

_AQUI = Path(__file__).resolve().parent
_RAIZ = _AQUI.parents[1]
for p in (_RAIZ / 'src', _RAIZ / 'experiments' / 'objetivo1', _RAIZ / 'experiments' / 'objetivo2', _AQUI):
    sys.path.insert(0, str(p))

from common.ventanas import canales_diseno_a, codifica_bloque, decodifica_bloque  # noqa: E402
from common.cotejo import METAL_HU, agrega, bordes, perfil_corte  # noqa: E402
from a11_rasterizar_tornillo import BANDA_MM, D_CUERPO_MM, pose_a_marco_crudo, rasteriza  # noqa: E402

CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']
CASO_REF = 'dataset7_CLINIC_metal_0039_data'
CASCARAS_BAJO = [4, 5, 6, 8, 9, 10, 11]          # r_lo (mm) con p95 bajo la envolvente en a17_paso1mm (run04_mejor)
PASO = 1.0
DELTA = 0.03


def decodifica(u: np.ndarray, canales: dict) -> tuple[np.ndarray, np.ndarray]:
    """`u` (N, 3) en orden LW, MW, SW -> (HU con regla_suave, HU solo LW)."""
    suave = decodifica_bloque(u.T[:, :, None], canales, delta=DELTA)[:, 0]
    lw = np.asarray(canales['LW'][1](u[:, 0]), dtype=np.float32)
    return suave.astype(np.float32), lw


def carga_caso(caso: str, data: list[Path], particion: Path, ejes: Path):
    import nibabel as nib
    from p1_decodificador_sd15 import leer_particion, rutas
    from e6b_vae_sd15 import eje_axial
    ubic = rutas([f for f in leer_particion(particion) if f['Caso'] == caso], data)
    with open(ejes, newline='', encoding='utf-8') as fh:
        e = [r for r in csv.DictReader(fh) if r['Caso'] == caso and r['modo'] == 'default6mm' and not r['Error']][0]
    c = np.array([float(e['c_x_mm']), float(e['c_y_mm']), float(e['c_z_mm'])])
    u = np.array([float(e['u_x']), float(e['u_y']), float(e['u_z'])])
    img = nib.load(ubic[caso])
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = np.array(img.header.get_zooms()[:3], dtype=float)
    c, u = pose_a_marco_crudo(img, c, u)
    M3, _, _ = rasteriza(arr.shape[:3], zooms, c, u, float(e['L_TS_mejor_mm']), D_CUERPO_MM, True, False, 0.0,
                         BANDA_MM)
    plano = [i for i in range(3) if i != eje]
    return np.moveaxis(arr, eje, 0), np.moveaxis(M3, eje, 0), (zooms[plano[0]], zooms[plano[1]])


def perfil(vol: np.ndarray, M: np.ndarray, esp2d, excluir=None) -> np.ndarray:
    ks = [k for k in range(vol.shape[0]) if M[k].any()]
    return agrega([perfil_corte(vol[k], M[k], esp2d, excluir=None if excluir is None else excluir[k], paso=PASO)
                   for k in ks])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir-diag', type=Path, required=True)
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--particion', type=Path, default=_RAIZ / 'experiments' / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--ejes', type=Path, default=_RAIZ / 'experiments' / 'objetivo2' / 'outputs' / 'e9ts_ejes_corredor.csv')
    ap.add_argument('--envolvente', type=Path, default=_AQUI / 'outputs' / 'obj3_pose' / 'a17_paso1mm' / 'a17_perfiles.csv')
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'obj3_pose' / 'a28')
    args = ap.parse_args()
    canales = canales_diseno_a()
    b = bordes(PASO)
    idx = [int(np.where(np.isclose(b[:-1], r))[0][0]) for r in CASCARAS_BAJO]

    # --- 1. sintetico ---
    por_caso = {'suave': [], 'lw': []}
    for caso in CASOS:
        vol, M, esp2d = carga_caso(caso, args.data, args.particion, args.ejes)
        with open(args.dir_diag / ('a15_%s_cotejo.csv' % caso), newline='', encoding='utf-8') as fh:
            ref = [f for f in csv.DictReader(fh) if abs(float(f['paso_mm']) - PASO) < 1e-6]
        sem = {'suave': [], 'lw': []}
        for s in range(5):
            z = np.load(args.dir_diag / ('a15_%s_run04_mejor_s%d_marcasG.npz' % (caso, s)))
            if abs(float(z['delta']) - DELTA) > 1e-9:
                raise SystemExit('CONTROL: delta %s != %s' % (z['delta'], DELTA))
            hs, hl = decodifica(z['u'], canales)
            for nom, h in (('suave', hs), ('lw', hl)):
                sal = vol.copy()
                sal[z['k'], z['y'], z['x']] = h
                sem[nom].append(perfil(sal, M, esp2d))
            kh = np.array([float(f['elev_p95']) for f in sorted((f for f in ref if int(f['semilla']) == s),
                                                                key=lambda f: float(f['r_lo_mm']))])
            dif = np.nanmax(np.abs(sem['suave'][-1][:, 1] - kh))
            print('%s s%d: control regla_suave vs cotejo de Khipu, max |dif p95| = %.2f HU' % (caso, s, dif), flush=True)
            if dif > 1.0:
                raise SystemExit('CONTROL FALLA: la decodificacion local no reproduce a15')
        for nom in sem:
            por_caso[nom].append(agrega(sem[nom]))
    S = {nom: agrega(v) for nom, v in por_caso.items()}        # (12, 2)

    # --- 2. control real (metal_0039, los 2 tornillos de a17) ---
    import nibabel as nib
    from scipy import ndimage as ndi
    from p1_decodificador_sd15 import leer_particion, rutas
    from e6b_vae_sd15 import eje_axial
    ubic = rutas([f for f in leer_particion(args.particion) if f['Caso'] == CASO_REF], list(args.data))
    img = nib.load(ubic[CASO_REF])
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = np.array(img.header.get_zooms()[:3], dtype=float)
    plano = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)
    esp2d = (zooms[plano[0]], zooms[plano[1]])
    metal = vol > METAL_HU
    lab, n = ndi.label(metal)
    tam = ndi.sum(metal, lab, index=np.arange(1, n + 1)) * float(np.prod(zooms))
    comps = [i + 1 for i in np.argsort(-tam) if tam[i] >= 500.0]
    if len(comps) != 2:
        raise SystemExit('CONTROL: se esperaban 2 tornillos en %s' % CASO_REF)
    ks = sorted({k for c in comps for k in range(vol.shape[0]) if (lab[k] == c).any()})
    dec = {'suave': vol.copy(), 'lw': vol.copy()}
    for k in ks:
        u = codifica_bloque(vol[k], canales)                                  # (3, H, W)
        hs, hl = decodifica(u.reshape(3, -1).T, canales)
        dec['suave'][k] = hs.reshape(vol[k].shape)
        dec['lw'][k] = hl.reshape(vol[k].shape)
    R = {}
    for nom in dec:
        R[nom] = agrega([perfil(dec[nom], lab == c, esp2d, excluir=metal & (lab != c)) for c in comps])
    orig = agrega([perfil(vol, lab == c, esp2d, excluir=metal & (lab != c)) for c in comps])

    # --- 3. regla ---
    env = {}
    with open(args.envolvente, newline='', encoding='utf-8') as fh:
        for f in csv.DictReader(fh):
            if f['etiqueta'] == 'run04_mejor':
                env[float(f['r_lo_mm'])] = (float(f['real_lo_p95']), float(f['real_hi_p95']))
    filas = []
    for i, r in zip(idx, CASCARAS_BAJO):
        lo, hi = env[float(r)]
        filas.append({'r_lo_mm': r, 'real_lo_p95': lo, 'real_hi_p95': hi,
                      'sint_p95_suave': S['suave'][i, 1], 'sint_p95_lw': S['lw'][i, 1],
                      'sint_p50_suave': S['suave'][i, 0], 'sint_p50_lw': S['lw'][i, 0],
                      'lw_dentro': bool(lo <= S['lw'][i, 1] <= hi),
                      'corr_sint_p95': S['lw'][i, 1] - S['suave'][i, 1],
                      'corr_real_p95': R['lw'][i, 1] - R['suave'][i, 1],
                      'corr_real_p95_vs_orig': R['suave'][i, 1] - orig[i, 1]})
    n_dentro = sum(f['lw_dentro'] for f in filas)
    cs = float(np.median([abs(f['corr_sint_p95']) for f in filas]))
    cr = float(np.median([abs(f['corr_real_p95']) for f in filas]))
    a_ok, b_ok = n_dentro >= 4, cr < 0.5 * cs
    veredicto = ('decodificador' if a_ok and b_ok else
                 'modelo' if not a_ok else 'indeterminado (LW entra, pero el control real tambien se mueve)')
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with open(args.out_dir / 'a28_diag_p95.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    L = ['# A28 — mecanismo del p95 (DEC 2026-10-15 pto 7; validacion, posterior)', '',
         '0101/0102 x 5 semillas, run04_mejor, `u` de `G` (Khipu 56866). Control real: 2 tornillos de `metal_0039`. '
         'Cascaras de 1 mm con p95 bajo lo real en `a17_paso1mm`.', '',
         '| r (mm) | envolvente real p95 | sint. regla_suave | sint. solo LW | LW dentro | corrimiento sint. | '
         'corrimiento real |', '|---|---|---|---|---|---|---|']
    L += ['| %d-%d | [%.0f, %.0f] | %.0f | %.0f | %s | %+.1f | %+.2f |'
          % (f['r_lo_mm'], f['r_lo_mm'] + 1, f['real_lo_p95'], f['real_hi_p95'], f['sint_p95_suave'],
             f['sint_p95_lw'], 'si' if f['lw_dentro'] else 'no', f['corr_sint_p95'], f['corr_real_p95'])
          for f in filas]
    L += ['', '- (a) LW dentro de la envolvente: **%d de 7** (umbral 4) -> %s' % (n_dentro, 'cumple' if a_ok else 'no cumple'),
          '- (b) mediana |corrimiento real| %.2f HU frente a 0.5 x mediana |corrimiento sintetico| = %.1f HU -> %s'
          % (cr, 0.5 * cs, 'cumple' if b_ok else 'no cumple'),
          '- Ida y vuelta real con regla_suave frente al original (p95, mediana |dif| en las 7): %.2f HU'
          % float(np.median([abs(f['corr_real_p95_vs_orig']) for f in filas])), '',
          '**Veredicto por la regla: %s.**' % veredicto, '',
          'Limite del control: sin modelo, la ida y vuelta es exacta en las dos decodificaciones, asi que (b) no puede '
          'captar la amplificacion del error del modelo por LW; solo descarta que el cambio de decodificacion mueva '
          'por si solo el p95 de lo real.']
    (args.out_dir / 'a28_diag_p95.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
