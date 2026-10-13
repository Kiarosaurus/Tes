"""Version 2, opcion B — PILOTO (compuerta) de la plantilla analitica de endurecimiento del haz. Sin entrenar, local, CPU.

QUE ES `T`
----------
`T = -FBP[ h(lambda * R(M)) ]`, `h(u) = ln(sinh u / u)` (h(0) = 0), con `R` la transformada de Radon paralela de la
mascara del metal en el corte axial (longitudes en mm) y FBP con filtro rampa. Es el termino de artefacto de
`park2017characterization` (Ec. 1.6/2.10) y el corrector de `park2016MAR` (Ec. 15); `hyung2017ml` la usa como entrada
de una red (Ec. 15, sin el termino `c chi`). Depende SOLO de `M`.

`lambda` no se calibra al escaner (`v2_plan.md`; ningun paper da un valor, #178). Regla fijada ANTES de mirar
resultados y sin usar ningun HU: `lambda0 = 1 / mediana(L_max)`, con `L_max` la longitud maxima de metal atravesada
por un rayo en cada corte analizado (asi `u = 1` en el rayo mas largo de un corte tipico: regimen no lineal moderado).
Sensibilidad (no decide): `lambda0 x 0.5` y `x 2`; mascara suavizada (gaussiana sigma 0.5 px) en vez de binaria.

QUE MIDE (criterio en `v2_plan.md`, seccion 1, "Compuerta de B")
----------------------------------------------------------------
- **C0, validez numerica (controles sinteticos, 0.7 mm/px):** disco, elipse, dos discos y estadio (tornillo cortado de
  costado). `A` = rms de la parte direccional de `T` en el anillo 2-10 mm / rms de `T` dentro de `M`. La teoria
  (Teo. 3.5 de Park 2017; Ec. 5.1) predice ~0 fuera del disco: PASA si `A_disco < 0.2 * A_dos_discos`. Si falla, la
  implementacion o la discretizacion dominan y la compuerta no se puede evaluar.
- **C1, estabilidad:** correlacion (Spearman) entre la parte direccional de `T` con 360 y con 720 angulos, en el anillo
  2-10 mm de los cortes reales. PASA si la mediana por corte >= 0.9.
- **C2, coincidencia con lo real (principal):** cortes de componentes tamano tornillo (500-4000 mm3) de entrenamiento de
  run04 y validacion, con la misma seleccion que D1 (`d1_alcance_rayas.py`: sin otro metal en el corte, referencia sin
  metal a 15-40 mm). Residuo real `D = HU(corte) - HU(referencia)`. En el anillo 2-10 mm (cuerpo, fuera del metal) se
  quita a `T` y a `D` su mediana por cascara de 1 mm (queda la parte DIRECCIONAL: rayas y bandas, no el perfil radial,
  que la red ya puede deducir de `M`). `rho` = Spearman(T_dir, D_dir). Nulo: la misma `rho` con `T` rotada alrededor
  del centro del corte (30-150 y 210-330 grados, paso 15; se excluyen los giros cercanos a 0 y 180 porque las rayas
  son simetricas por 180): conserva la cantidad de estructura de `T`, rompe su orientacion. Diferencia por corte
  `d = rho - media(rho_nulo)`. **Control anatomico** (el nulo de D1): lo mismo con `D0 = HU(k2) - HU(referencia)`,
  dos cortes SIN metal (otro lado, 15-40 mm), con la misma `M` y la misma `T` -> `d0`. Detecta que `T` coincida con
  la anatomia alineada con el tornillo (bordes oseos paralelos al tornillo iliosacro) y no con el artefacto. Por
  corte `e = d - d0`; medianas corte -> componente -> paciente (como D1), solo cortes con control. PASA si Wilcoxon
  de una cola (e > 0) entre pacientes da p < 0.05 Y la mediana de `d` entre pacientes >= 0.05.
- **B pasa la compuerta si C0, C1 y C2 pasan** con `lambda0` y mascara binaria. Si no, se sigue solo con D y se
  declara (`01-decisiones.md` 2026-10-13, punto 5).

LIMITES (declarados de antemano)
--------------------------------
`D` contiene anatomia (la referencia es otro corte) ademas del artefacto: eso baja `rho` pero no la sesga hacia `T`
(la anatomia no depende de `M`); el nulo por rotacion la conserva. 2D paralelo frente a CT helicoidal; sin scatter.
Usa pacientes de ENTRENAMIENTO: es una compuerta sobre la plantilla (no hay modelo), no una evaluacion; prueba no se toca.

USO (local; necesita los NIfTI de `data/` y scikit-image)
-------------------------------------------------------
    python experiments/objetivo3/b_piloto_plantilla.py                  # todo (~10-30 min)
    python experiments/objetivo3/b_piloto_plantilla.py --max-casos 3    # prueba rapida
    python experiments/objetivo3/b_piloto_plantilla.py --solo-controles # solo C0 (segundos, sin datos)

Salida: `outputs/b_piloto/` -> `b_resumen.md` (veredicto), `b_por_corte.csv`, `b_por_paciente.csv`, `b_controles.csv`,
`b_controles.png`.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi
from scipy import stats
from skimage.transform import iradon, radon

_AQUI = Path(__file__).resolve().parent
if str(_AQUI) not in sys.path:
    sys.path.insert(0, str(_AQUI))

from d1_alcance_rayas import CUERPO_HU, DZ_MM, METAL_HU, VOL_MIN_MM3, casos, cuerpo_2d  # noqa: E402

VOL_MAX_MM3 = 4000.0           # mismo rango que D1 tornillo y que D-a
ANILLO_MM = (2.0, 10.0)        # donde D2 mide el hueco
LADO = 256                     # recorte centrado en el componente (px)
ANG_BASE, ANG_ALTO = 360, 720
GIROS = [a for a in range(30, 331, 15) if not 160 <= a <= 200]
MIN_PIX = 50
SEMILLA = 20261013
# Umbrales de la compuerta (v2_plan.md). No se tocan despues de ver resultados.
C0_FRAC = 0.2
C1_MIN = 0.9
C2_P, C2_D = 0.05, 0.05


def h(u: np.ndarray) -> np.ndarray:
    """ln(sinh u / u), estable: 0 en u = 0 y forma asintotica para u grande."""
    u = np.abs(np.asarray(u, dtype=np.float64))
    out = np.zeros_like(u)
    chico = (u > 0) & (u < 1e-4)
    out[chico] = u[chico] ** 2 / 6.0
    med = (u >= 1e-4) & (u < 20)
    out[med] = np.log(np.sinh(u[med]) / u[med])
    gr = u >= 20
    out[gr] = u[gr] - np.log(2.0 * u[gr])
    return out


def longitudes(mascara: np.ndarray, pix_mm: float, n_ang: int) -> tuple[np.ndarray, np.ndarray]:
    """Sinograma de longitudes de metal (mm) y angulos (grados), haz paralelo."""
    theta = np.linspace(0.0, 180.0, n_ang, endpoint=False)
    return radon(mascara.astype(np.float64), theta=theta, circle=False) * pix_mm, theta


def plantilla(mascara: np.ndarray, pix_mm: float, lam: float, n_ang: int = ANG_BASE) -> np.ndarray:
    """T = -FBP[h(lambda R(M))] en la misma grilla que `mascara`."""
    L, theta = longitudes(mascara, pix_mm, n_ang)
    return -iradon(h(lam * L), theta=theta, filter_name='ramp', circle=False, output_size=mascara.shape[0])


def direccional(x: np.ndarray, dist: np.ndarray, sel: np.ndarray) -> np.ndarray:
    """Valores de `x` en `sel` menos su mediana por cascara de 1 mm (queda la parte direccional)."""
    out = np.empty(int(sel.sum()))
    d, v = dist[sel], x[sel]
    for lo in np.arange(np.floor(d.min()), np.ceil(d.max()) + 1.0):
        s = (d >= lo) & (d < lo + 1.0)
        if s.any():
            out[s] = v[s] - np.median(v[s])
    return out


def recorta(a: np.ndarray, cy: int, cx: int, valor: float) -> np.ndarray:
    """Ventana LADO x LADO centrada en (cy, cx), rellenando con `valor` fuera del corte."""
    r = LADO // 2
    p = np.pad(a, r, mode='constant', constant_values=valor)
    return p[cy:cy + LADO, cx:cx + LADO]


# --------------------------------------------------------------------------------------------- C0: controles
def controles(pix_mm: float = 0.7) -> list[dict]:
    """Mascaras sinteticas y su `A` (direccional fuera / dentro), con lambda tal que u = 1 en el rayo mas largo."""
    yy, xx = (np.mgrid[:LADO, :LADO] - LADO / 2 + 0.5) * pix_mm
    figs = {
        'disco': yy ** 2 + xx ** 2 <= 3.5 ** 2,
        'elipse': (yy / 3.5) ** 2 + (xx / 8.0) ** 2 <= 1,
        'dos_discos': ((xx - 10) ** 2 + yy ** 2 <= 3.5 ** 2) | ((xx + 10) ** 2 + yy ** 2 <= 3.5 ** 2),
        'estadio': ((np.abs(xx) <= 25) & (np.abs(yy) <= 3.5)) | ((np.abs(xx) - 25) ** 2 + yy ** 2 <= 3.5 ** 2),
    }
    out = []
    for nombre, m in figs.items():
        lam = 1.0 / longitudes(m, pix_mm, ANG_BASE)[0].max()
        T = plantilla(m, pix_mm, lam)
        dist = ndi.distance_transform_edt(~m, sampling=pix_mm)
        sel = (dist > ANILLO_MM[0]) & (dist <= ANILLO_MM[1])
        A = float(np.sqrt(np.mean(direccional(T, dist, sel) ** 2)) / np.sqrt(np.mean(T[m] ** 2)))
        out.append({'figura': nombre, 'A': A, 'T': T, 'M': m})
    return out


def figura_controles(ctrl: list[dict], ruta: Path) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, len(ctrl), figsize=(4 * len(ctrl), 4))
    for a, c in zip(ax, ctrl):
        T = c['T'].copy()
        v = np.percentile(np.abs(T[~c['M']]), 99) or 1.0
        a.imshow(np.clip(T, -v, v), cmap='gray')
        a.contour(c['M'], [0.5], colors='r', linewidths=0.5)
        a.set_title('%s  A=%.3f' % (c['figura'], c['A']))
        a.axis('off')
    fig.tight_layout()
    fig.savefig(ruta, dpi=110)
    plt.close(fig)


# --------------------------------------------------------------------------------------------- cortes reales
def cortes_reales(ruta: Path, max_cortes: int) -> list[dict]:
    """Cortes de componentes 500-4000 mm3 con la seleccion de D1. Devuelve recortes (sin calcular T)."""
    img = nib.load(str(ruta))
    vol = np.asarray(img.dataobj, dtype=np.float32)
    sx, sy, sz = (float(z) for z in img.header.get_zooms()[:3])
    if abs(sx - sy) > 1e-3:
        print('  AVISO: pixel no cuadrado (%.4f x %.4f); se usa la media' % (sx, sy))
    pix = 0.5 * (sx + sy)
    metal = vol > METAL_HU
    lab, n = ndi.label(metal)
    if n == 0:
        return []
    tam = np.bincount(lab.ravel())
    metal_por_corte = metal.reshape(-1, metal.shape[2]).sum(0)
    cache: dict[int, np.ndarray] = {}

    def area(k: int) -> np.ndarray:
        if k not in cache:
            cache[k] = cuerpo_2d(vol[:, :, k])
        return cache[k]

    out = []
    for c in range(1, n + 1):
        if not VOL_MIN_MM3 <= tam[c] * sx * sy * sz <= VOL_MAX_MM3:
            continue
        mc = lab == c
        por_corte = mc.reshape(-1, mc.shape[2]).sum(0)
        ks = [k for k in np.nonzero(por_corte >= 20)[0] if metal_por_corte[k] == por_corte[k]]
        if not ks:
            continue
        ks = [ks[i] for i in np.unique(np.linspace(0, len(ks) - 1, min(max_cortes, len(ks))).round().astype(int))]
        for k in ks:
            b = area(k)
            cand = []                                    # misma busqueda que `d1_alcance_rayas.analiza`
            for sgn in (-1, 1):
                for d in range(int(np.ceil(DZ_MM[0] / sz)), int(DZ_MM[1] / sz) + 1):
                    kk = k + sgn * d
                    if 0 <= kk < vol.shape[2] and metal_por_corte[kk] < 5 and \
                            abs(int(area(kk).sum()) - int(b.sum())) <= 0.2 * b.sum():
                        cand.append((d, sgn, kk))
                        break
            if not cand:
                continue
            cand.sort()
            kr = cand[0][2]
            m2 = mc[:, :, k]
            cy, cx = (int(round(v)) for v in ndi.center_of_mass(m2))
            valido = b & area(kr) & ~metal[:, :, k] & ~metal[:, :, kr]
            fila = {'comp': c, 'corte': int(k), 'ref': int(kr), 'pix': pix,
                    'M': recorta(m2, cy, cx, False),
                    'D': recorta(vol[:, :, k] - vol[:, :, kr], cy, cx, 0.0),
                    'valido': recorta(valido, cy, cx, False), 'D0': None}
            if len(cand) == 2:                           # control anatomico: dos cortes sin metal
                k2 = cand[1][2]
                fila.update(ref2=int(k2), D0=recorta(vol[:, :, k2] - vol[:, :, kr], cy, cx, 0.0),
                            valido0=recorta(valido & area(k2) & ~metal[:, :, k2], cy, cx, False))
            out.append(fila)
    return out


def mide(c: dict, lam: float, suavizar: bool = False, n_ang: int = ANG_BASE,
         rng: np.random.Generator | None = None) -> dict | None:
    """rho observado y nulo de un corte; None si el anillo tiene pocos pixeles."""
    M = c['M']
    dist = ndi.distance_transform_edt(~M, sampling=c['pix'])
    sel = c['valido'] & (dist > ANILLO_MM[0]) & (dist <= ANILLO_MM[1])
    if sel.sum() < MIN_PIX:
        return None
    entrada = ndi.gaussian_filter(M.astype(np.float64), 0.5) if suavizar else M
    T = plantilla(entrada, c['pix'], lam, n_ang)
    d_dir = direccional(c['D'], dist, sel)
    t_dir = direccional(T, dist, sel)
    Tg = [ndi.rotate(T, g, reshape=False, order=1, mode='constant', cval=0.0) for g in GIROS]

    def d_de(D: np.ndarray, s: np.ndarray) -> tuple[float, float]:
        dd = direccional(D, dist, s)
        r = float(stats.spearmanr(direccional(T, dist, s), dd)[0])
        nul = float(np.mean([stats.spearmanr(direccional(t, dist, s), dd)[0] for t in Tg]))
        return r, nul

    rho, nulo = d_de(c['D'], sel)
    d0 = float('nan')
    if c.get('D0') is not None:
        sel0 = sel & c['valido0']
        if sel0.sum() >= MIN_PIX:
            r0, n0 = d_de(c['D0'], sel0)
            d0 = r0 - n0
    return {'rho': rho, 'rho_nulo': nulo, 'd': rho - nulo, 'd0': d0, 'e': (rho - nulo) - d0,
            'n_pix': int(sel.sum()), 'T': T, 'dist': dist, 'sel': sel}


def agrega(filas: list[dict], clave: str) -> dict[str, float]:
    """Mediana corte -> componente -> paciente de `clave`."""
    por = {}
    for f in filas:
        por.setdefault(f['caso'], {}).setdefault(f['comp'], []).append(f[clave])
    return {caso: float(np.median([np.median(v) for v in comps.values()])) for caso, comps in por.items()}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--max-cortes', type=int, default=8)
    ap.add_argument('--max-casos', type=int, default=None)
    ap.add_argument('--solo-controles', action='store_true')
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'b_piloto')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    # C0
    ctrl = controles()
    figura_controles(ctrl, args.out_dir / 'b_controles.png')
    A = {c['figura']: c['A'] for c in ctrl}
    with open(args.out_dir / 'b_controles.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['figura', 'A_direccional_fuera_sobre_dentro'])
        w.writerows([[k, '%.5f' % v] for k, v in A.items()])
    c0 = A['disco'] < C0_FRAC * A['dos_discos']
    print('C0 controles: ' + ', '.join('%s %.4f' % kv for kv in A.items()) + ' -> %s' % ('PASA' if c0 else 'FALLA'))
    if args.solo_controles:
        return

    # cortes reales
    lista = casos()[:args.max_casos]
    reales = []
    for i, (caso, part, ruta) in enumerate(lista, 1):
        cs = cortes_reales(ruta, args.max_cortes)
        for c in cs:
            c.update(caso=caso, particion=part)
        reales += cs
        print('[%d/%d] %s (%s): %d cortes' % (i, len(lista), caso, part, len(cs)), flush=True)
    if not reales:
        raise SystemExit('sin cortes reales: revisar rutas de data/ (grupos.csv)')
    lmax = [longitudes(c['M'], c['pix'], ANG_BASE)[0].max() for c in reales]
    lam0 = 1.0 / float(np.median(lmax))
    print('lambda0 = 1 / mediana(L_max) = 1 / %.2f mm = %.4f por mm' % (np.median(lmax), lam0))

    brazos = {'principal': dict(lam=lam0), 'lambda_x0.5': dict(lam=0.5 * lam0), 'lambda_x2': dict(lam=2 * lam0),
              'suavizada': dict(lam=lam0, suavizar=True)}
    filas: dict[str, list[dict]] = {b: [] for b in brazos}
    estab = []
    for j, c in enumerate(reales, 1):
        for b, kw in brazos.items():
            r = mide(c, **kw)
            if r is None:
                break
            filas[b].append({'caso': c['caso'], 'particion': c['particion'], 'comp': c['comp'], 'corte': c['corte'],
                             'ref': c['ref'], 'n_pix': r['n_pix'], 'rho': r['rho'], 'rho_nulo': r['rho_nulo'],
                             'd': r['d'], 'd0': r['d0'], 'e': r['e']})
            if b == 'principal':
                T2 = plantilla(c['M'], c['pix'], lam0, ANG_ALTO)
                estab.append(float(stats.spearmanr(direccional(r['T'], r['dist'], r['sel']),
                                                   direccional(T2, r['dist'], r['sel']))[0]))
        if j % 20 == 0:
            print('  %d/%d cortes medidos' % (j, len(reales)), flush=True)

    with open(args.out_dir / 'b_por_corte.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['brazo', 'caso', 'particion', 'comp', 'corte', 'ref', 'n_pix', 'rho', 'rho_nulo', 'd', 'd0_anat',
                    'e'])
        for b, fs in filas.items():
            for f in fs:
                w.writerow([b, f['caso'], f['particion'], f['comp'], f['corte'], f['ref'], f['n_pix']]
                           + ['%.4f' % f[k] for k in ('rho', 'rho_nulo', 'd', 'd0', 'e')])

    c1_med = float(np.median(estab))
    c1 = c1_med >= C1_MIN
    res = {}
    for b, fs in filas.items():
        d_pac = agrega(fs, 'd')
        rho_pac = agrega(fs, 'rho')
        fe = [f for f in fs if np.isfinite(f['e'])]
        e_pac = agrega(fe, 'e') if fe else {}
        d0_pac = agrega(fe, 'd0') if fe else {}
        dv, ev = np.array(list(d_pac.values())), np.array(list(e_pac.values()))
        p = float(stats.wilcoxon(ev, alternative='greater').pvalue) if ev.size >= 5 else float('nan')
        res[b] = {'n_pac': dv.size, 'n_pac_ctrl': ev.size, 'n_cortes': len(fs), 'd_med': float(np.median(dv)),
                  'd0_med': float(np.median(list(d0_pac.values()))) if d0_pac else float('nan'),
                  'e_med': float(np.median(ev)) if ev.size else float('nan'),
                  'rho_med': float(np.median(list(rho_pac.values()))), 'p': p,
                  'pasa': bool(p < C2_P and np.median(dv) >= C2_D), 'd_pac': d_pac, 'e_pac': e_pac}
    with open(args.out_dir / 'b_por_paciente.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['brazo', 'caso', 'd_mediana', 'e_mediana'])
        for b, r in res.items():
            w.writerows([[b, k, '%.4f' % v, '%.4f' % r['e_pac'].get(k, float('nan'))] for k, v in r['d_pac'].items()])
    c2 = res['principal']['pasa']
    pasa = c0 and c1 and c2

    L = ['# Piloto de la plantilla `T` (opcion B, compuerta) — resultado', '',
         'Generado por `b_piloto_plantilla.py`. Criterio fijado en `v2_plan.md` antes de correr.', '',
         '**VEREDICTO: B %s la compuerta** (C0 %s, C1 %s, C2 %s).' % (
             'PASA' if pasa else 'NO PASA', 'PASA' if c0 else 'FALLA', 'PASA' if c1 else 'FALLA',
             'PASA' if c2 else 'FALLA'), '',
         '## C0 — controles (A = direccional fuera / rms dentro)', '', '| figura | A |', '|---|---|']
    L += ['| %s | %.4f |' % kv for kv in A.items()]
    L += ['', 'Regla: A_disco < %.1f x A_dos_discos.' % C0_FRAC, '',
          '## C1 — estabilidad 360 frente a 720 angulos', '',
          'Mediana por corte de Spearman: **%.3f** (%d cortes; regla >= %.2f).' % (c1_med, len(estab), C1_MIN), '',
          '## C2 — coincidencia con el residuo real en 2-10 mm', '',
          'lambda0 = %.4f por mm (1 / mediana de L_max = %.2f mm).' % (lam0, np.median(lmax)), '',
          '| brazo | pacientes (con control) | cortes | rho mediana | d mediana | d0 anatomico mediana | '
          'e = d - d0 mediana | p Wilcoxon (e > 0) | cumple |', '|---|---|---|---|---|---|---|---|---|']
    for b, r in res.items():
        L.append('| %s | %d (%d) | %d | %.3f | %.3f | %.3f | %.3f | %.4f | %s |' % (
            b, r['n_pac'], r['n_pac_ctrl'], r['n_cortes'], r['rho_med'], r['d_med'], r['d0_med'], r['e_med'], r['p'],
            'si' if r['pasa'] else 'no'))
    L += ['', 'Regla (solo `principal` decide): p < %.2f (e > 0, pacientes con control anatomico) y mediana de d >= '
          '%.2f. Los otros brazos son sensibilidad.' % (C2_P, C2_D), '',
          'Limites: el residuo real incluye anatomia (referencia = otro corte); 2D paralelo; sin scatter; pacientes de '
          'entrenamiento y validacion (no hay modelo: compuerta sobre la plantilla, no evaluacion).']
    (args.out_dir / 'b_resumen.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L[:6]))
    print('-> %s' % (args.out_dir / 'b_resumen.md'))


if __name__ == '__main__':
    main()
