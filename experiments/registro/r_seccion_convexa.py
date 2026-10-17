"""Prueba de admision de la plantilla `T` (opcion B, v2) estratificada por la forma de la seccion del tornillo.

GAP que atiende
---------------
`overleaf/secciones/capitulo3.tex` l. 287 (ronda capitulo3-r27): "efecto del canal en los cortes en que la seccion del
tornillo es estrictamente convexa, que la prueba de admision, al promediar sobre cortes, no separa (implicancia 178)".
Lo atiende SOLO para la prueba de admision (coincidencia de la parte direccional de `T` con el residuo real); el
efecto del canal sobre la salida del modelo con canal (run05b) exigiria generar con GPU y no se mide aqui.

Entradas
--------
- Los mismos cortes del piloto: `b_piloto_plantilla.cortes_reales` sobre `d1_alcance_rayas.casos()` (entrenamiento de
  run04 y validacion; NO toca la particion de prueba). Necesita los NIfTI de `data/`.
- `experiments/objetivo3/b_piloto/b_por_corte.csv`, brazo `principal` (d, e por corte, ya registrados).

Medida (descriptiva y POSTERIOR: los cortes de forma se fijan aqui, despues de ver el piloto)
------------------------------------------------------------------------------------------
Por corte, sobre la mascara `M` del componente en ese corte: numero de componentes 2D (8-conexo), elongacion
(razon de ejes mayor/menor de los momentos de segundo orden) y solidez (area / area de la envolvente convexa).
"Compacta" = un solo componente 2D y elongacion <= 1.5 (lo mas cercano a un disco: seccion transversal del tornillo,
la que el Teo. 3.5 de `park2017characterization` declara sin rayas en el continuo). Sensibilidad del corte: 1.3 y 2.0.
Se reporta d y e por estrato (mediana por corte y mediana corte -> componente -> paciente, como el piloto) y la
correlacion de Spearman entre elongacion y d en todos los cortes.

Control de regresion
--------------------
Cada corte reconstruido debe coincidir con una fila `principal` de `b_por_corte.csv` en (caso, comp, corte, ref) y en
`n_pix` (pixeles del anillo 2-10 mm valido, misma definicion que `b_piloto_plantilla.mide`), y el numero de cortes
debe ser 228. Si no reproduce, el script lo dice y NO imprime los estratos.

Uso (local, CPU, sin GPU)
-------------------------
    python experiments/registro/r_seccion_convexa.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np
from scipy import ndimage as ndi
from scipy import stats
from skimage.morphology import convex_hull_image

_RAIZ = Path(__file__).resolve().parents[2]
_OBJ3 = _RAIZ / 'experiments' / 'objetivo3'
sys.path.insert(0, str(_OBJ3))

from b_piloto_plantilla import ANILLO_MM, MIN_PIX, cortes_reales  # noqa: E402
from d1_alcance_rayas import casos  # noqa: E402

CORTES_ELONG = (1.3, 1.5, 2.0)   # 1.5 principal; 1.3 y 2.0 sensibilidad. Fijados despues de ver el piloto.


def forma(M: np.ndarray) -> tuple[int, float, float]:
    """(componentes 2D, elongacion, solidez) de la seccion binaria `M`."""
    _, ncomp = ndi.label(M, structure=np.ones((3, 3)))
    yy, xx = np.nonzero(M)
    cov = np.cov(np.vstack([yy, xx]).astype(np.float64))
    ev = np.sort(np.linalg.eigvalsh(cov))
    elong = float(np.sqrt(ev[1] / ev[0])) if ev[0] > 0 else float('inf')
    sol = float(M.sum() / convex_hull_image(M).sum())
    return int(ncomp), elong, sol


def n_pix_anillo(c: dict) -> int:
    """Pixeles del anillo valido de 2-10 mm (misma definicion que `mide`)."""
    dist = ndi.distance_transform_edt(~c['M'], sampling=c['pix'])
    return int((c['valido'] & (dist > ANILLO_MM[0]) & (dist <= ANILLO_MM[1])).sum())


def agrega(filas: list[dict], clave: str) -> dict[str, float]:
    """Mediana corte -> componente -> paciente (igual que el piloto)."""
    por: dict[str, dict[int, list[float]]] = {}
    for f in filas:
        por.setdefault(f['caso'], {}).setdefault(f['comp'], []).append(f[clave])
    return {k: float(np.median([np.median(v) for v in comps.values()])) for k, comps in por.items()}


def main() -> None:
    ref = {}
    with open(_OBJ3 / 'b_piloto' / 'b_por_corte.csv', encoding='utf-8') as fh:
        for f in csv.DictReader(fh):
            if f['brazo'] == 'principal':
                ref[(f['caso'], int(f['comp']), int(f['corte']), int(f['ref']))] = f
    filas, sin_par, npix_mal = [], [], 0
    for i, (caso, part, ruta) in enumerate(casos(), 1):
        for c in cortes_reales(ruta, 8):
            npx = n_pix_anillo(c)
            if npx < MIN_PIX:
                continue
            clave = (caso, c['comp'], c['corte'], c['ref'])
            r = ref.get(clave)
            if r is None:
                sin_par.append(clave)
                continue
            if int(r['n_pix']) != npx:
                npix_mal += 1
            ncomp, elong, sol = forma(c['M'])
            filas.append({'caso': caso, 'comp': c['comp'], 'corte': c['corte'], 'ncomp': ncomp, 'elong': elong,
                          'sol': sol, 'd': float(r['d']), 'e': float(r['e'])})
        print('[%d] %s: %d cortes acumulados' % (i, caso, len(filas)), flush=True)

    ok = len(filas) == len(ref) == 228 and not sin_par and npix_mal == 0
    print('CONTROL: %d cortes reconstruidos, %d en b_por_corte, %d sin par, %d con n_pix distinto -> %s'
          % (len(filas), len(ref), len(sin_par), npix_mal, 'REPRODUCE' if ok else 'NO REPRODUCE'))
    if not ok:
        print('No se reportan estratos.')
        return

    el = np.array([f['elong'] for f in filas])
    d = np.array([f['d'] for f in filas])
    rs = stats.spearmanr(el, d)
    print('elongacion: mediana %.2f, min %.2f, max %.2f; solidez mediana %.3f; cortes con >1 componente 2D: %d'
          % (np.median(el), el.min(), el.max(), np.median([f['sol'] for f in filas]),
             sum(f['ncomp'] > 1 for f in filas)))
    print('Spearman(elongacion, d) en %d cortes: rho = %.3f, p = %.4g' % (len(filas), rs[0], rs[1]))
    print('| corte elong | estrato | cortes | pacientes | d mediana (cortes) | d mediana (pacientes) | '
          'cortes con control | e mediana (pacientes) |')
    for u in CORTES_ELONG:
        for nombre, sel in (('compacta', lambda f: f['ncomp'] == 1 and f['elong'] <= u),
                            ('alargada o multiple', lambda f: not (f['ncomp'] == 1 and f['elong'] <= u))):
            fs = [f for f in filas if sel(f)]
            if not fs:
                print('| %.1f | %s | 0 | - | - | - | - | - |' % (u, nombre))
                continue
            fe = [f for f in fs if np.isfinite(f['e'])]
            dp = agrega(fs, 'd')
            ep = agrega(fe, 'e') if fe else {}
            print('| %.1f | %s | %d | %d | %.3f | %.3f | %d | %s |' % (
                u, nombre, len(fs), len(dp), np.median([f['d'] for f in fs]), np.median(list(dp.values())),
                len(fe), '%.3f (n = %d)' % (np.median(list(ep.values())), len(ep)) if ep else '-'))


if __name__ == '__main__':
    main()
