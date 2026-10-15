"""A26 - lecturas del TOST fijadas en `01-decisiones.md` 2026-10-15 (D14, D15, D16, D-extra, #185, #186).

No reemplaza a `a24_contrastes.py` (el analisis congelado): lo complementa con lo decidido el 2026-10-15, que es
PREVIO al TOST de prueba de la version 2 y POSTERIOR para la version 1 (`visto.md`).

Por modelo (`--etiquetas`), sobre el CSV de `a20` de una variante (`--csv`, `--variante`):
- valor por paciente igual que `a24`: difusor = mediana de 5 semillas; Peters Ti = mediana de A y B;
- TOST con *t* contra Peters Ti, con el `Delta` propio (`--delta-json`) y con el margen comun (`--delta-comun`, el de
  run04, pto 16);
- **desenlace** (pto 15): equivalencia / no equivalencia / no concluyente, mas la direccion si el IC90 excluye 0;
- **IC90 exacto por permutacion pareada** (pto 14): inversion de la prueba de cambios de signo (2^n) sobre la media;
  la sensibilidad solo puede BAJAR la categoria (regla general de la entrada);
- **margen minimo de equivalencia** (pto 16): max(|limite inferior|, |limite superior|) del IC90 con *t*;
- **acuerdo** (#185, pto 22): Bland-Altman (sesgo, limites al 95 %) y Pitman-Morgan (igualdad de varianzas pareadas);
- descriptivos de las asimetrias (#186): fraccion de la ROI de Peters Ti bajo -1000 HU, voxeles por brazo, y el
  exceso de costura de cada brazo (pto 5).

USO
---
    python experiments/objetivo3/a26_lecturas.py --csv <a20_test_base.csv> --variante base \\
        --etiquetas run04_mejor --delta-json outputs/obj3_pose/a20_val/a20_delta_run04_mejor.json \\
        --out-dir outputs/a26/v1_base
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
from pathlib import Path

import numpy as np
from scipy import stats

_AQUI = Path(__file__).resolve().parent
ORDEN = {'equivalencia': 2, 'no concluyente': 1, 'no equivalencia': 0}


def ic_t(d: np.ndarray) -> tuple[float, float, float]:
    n = d.size
    m, se = float(d.mean()), float(d.std(ddof=1) / np.sqrt(n))
    t = stats.t.ppf(0.95, n - 1)
    return m, m - t * se, m + t * se


def desenlace(lo: float, hi: float, delta: float) -> str:
    """DEC 2026-10-15 pto 15."""
    if lo > -delta and hi < delta:
        return 'equivalencia'
    if hi < -delta or lo > delta:
        return 'no equivalencia'
    return 'no concluyente'


def direccion(lo: float, hi: float) -> str:
    if hi < 0:
        return 'difusor < Peters'
    if lo > 0:
        return 'difusor > Peters'
    return 'sin direccion (IC90 incluye 0)'


def ic_permutacion(d: np.ndarray, nivel: float = 0.90) -> tuple[float, float]:
    """IC exacto por inversion de la prueba de cambios de signo sobre la media (bilateral, alfa = 1 - nivel)."""
    n = d.size
    signos = np.array(list(itertools.product((-1.0, 1.0), repeat=n)))      # 2^n x n

    def p(theta: float) -> float:
        x = d - theta
        s = signos @ x
        return float(np.mean(np.abs(s) >= abs(x.sum()) - 1e-9))

    alfa = 1.0 - nivel
    m, rango = float(d.mean()), float(d.max() - d.min()) + 1.0

    def borde(signo: float) -> float:
        a, b = m, m + signo * rango                    # p(a) grande, p(b) chica
        while p(b) > alfa:
            b += signo * rango
        for _ in range(60):
            c = 0.5 * (a + b)
            if p(c) > alfa:
                a = c
            else:
                b = c
        return a
    return borde(-1.0), borde(1.0)


def pitman_morgan(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    """Igualdad de varianzas pareadas: correlacion entre suma y diferencia (t con n - 2 gl)."""
    r, p = stats.pearsonr(x + y, x - y)
    return float(r), float(p)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--csv', type=Path, required=True)
    ap.add_argument('--variante', default='base')
    ap.add_argument('--etiquetas', nargs='+', required=True)
    ap.add_argument('--delta-json', type=Path, nargs='+', required=True, help='uno por etiqueta, mismo orden')
    ap.add_argument('--delta-comun', type=float, default=196.3, help='margen comun (Delta de run04_mejor, pto 16)')
    ap.add_argument('--casos', type=Path, default=_AQUI / 'casos_ea2_test.txt')
    ap.add_argument('--out-dir', type=Path, required=True)
    args = ap.parse_args()
    if len(args.delta_json) != len(args.etiquetas):
        raise SystemExit('un --delta-json por etiqueta')
    casos = [c.strip() for c in args.casos.read_text(encoding='utf-8').split() if c.strip()]
    with open(args.csv, newline='', encoding='utf-8') as fh:
        filas = list(csv.DictReader(fh))

    def col(caso, brazo, pref, clave='amp_HU'):
        v = [float(f[clave]) for f in filas if f['caso'] == caso and f['brazo'] == brazo
             and f['condicion'].startswith(pref) and f.get(clave, '') not in ('', 'nan')]
        return float(np.median(v)) if v else float('nan')

    Ti = np.array([col(c, 'peters', 'Ti_') for c in casos])
    desc = {'peters_Ti_suelo_frac_max': float(np.nanmax([col(c, 'peters', 'Ti_', 'suelo_frac') for c in casos])),
            'peters_Ti_n_vox_mediana': float(np.median([col(c, 'peters', 'Ti_', 'n_vox') for c in casos])),
            'peters_Ti_costura_mediana': float(np.nanmedian([col(c, 'peters', 'Ti_', 'exceso_costura') for c in casos])),
            'peters_ruido_amp_mediana': float(np.nanmedian([col(c, 'peters', 'ruido_A-B') for c in casos]))}
    res = {'variante': args.variante, 'csv': str(args.csv), 'delta_comun': args.delta_comun, 'peters': desc,
           'modelos': {}}
    filas_pac = []
    for et, rj in zip(args.etiquetas, args.delta_json):
        D = np.array([col(c, 'difusor', et + '_s') for c in casos])
        if np.isnan(D).any() or np.isnan(Ti).any():
            raise SystemExit('CONTROL: faltan brazos para %s en %s' % (et, args.csv))
        delta_p = float(json.loads(rj.read_text(encoding='utf-8'))['Delta_HU'])
        d = D - Ti
        m, lo, hi = ic_t(d)
        plo, phi = ic_permutacion(d)
        lect = {}
        for nom, dl in (('propio', delta_p), ('comun', args.delta_comun)):
            cat_t, cat_p = desenlace(lo, hi, dl), desenlace(plo, phi, dl)
            final = cat_t if ORDEN[cat_p] >= ORDEN[cat_t] else cat_p + ' (baja por permutacion)'
            lect[nom] = {'Delta_HU': dl, 'desenlace_t': cat_t, 'desenlace_permutacion': cat_p, 'desenlace': final}
        ba_sd = float(d.std(ddof=1))
        r_pm, p_pm = pitman_morgan(D, Ti)
        res['modelos'][et] = {
            'n': int(d.size), 'media_HU': m, 'ic90_t': [lo, hi], 'ic90_permutacion': [plo, phi],
            'direccion': direccion(lo, hi), 'margen_minimo_HU': float(max(abs(lo), abs(hi))),
            'margen_minimo_frac_Ti': float(max(abs(lo), abs(hi)) / Ti.mean()), 'lecturas': lect,
            'shapiro_p': float(stats.shapiro(d).pvalue),
            'bland_altman': {'sesgo': m, 'lim_inf': m - 1.96 * ba_sd, 'lim_sup': m + 1.96 * ba_sd},
            'pitman_morgan': {'r': r_pm, 'p': p_pm},
            'cv_difusor': float(D.std(ddof=1) / D.mean()), 'cv_Ti': float(Ti.std(ddof=1) / Ti.mean()),
            'pearson_r': float(stats.pearsonr(D, Ti)[0]),
            'costura_mediana': float(np.nanmedian([col(c, 'difusor', et + '_s', 'exceso_costura') for c in casos])),
            'n_vox_mediana': float(np.median([col(c, 'difusor', et + '_s', 'n_vox') for c in casos]))}
        for c, a, b in zip(casos, D, Ti):
            filas_pac.append({'variante': args.variante, 'etiqueta': et, 'caso': c, 'difusor': a, 'peters_Ti': b,
                              'dif': a - b})

    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    (out / 'a26_lecturas.json').write_text(json.dumps(res, indent=2), encoding='utf-8')
    with open(out / 'a26_por_paciente.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas_pac[0].keys()))
        w.writeheader()
        w.writerows(filas_pac)
    L = ['# A26 — lecturas de DEC 2026-10-15, variante `%s`' % args.variante, '',
         'CSV: `%s`. Peters Ti: suelo max %.3f | voxeles (mediana) %.0f | costura %.1f HU | ruido A-B %.1f HU.'
         % (args.csv.name, desc['peters_Ti_suelo_frac_max'], desc['peters_Ti_n_vox_mediana'],
            desc['peters_Ti_costura_mediana'], desc['peters_ruido_amp_mediana']), '',
         '| modelo | media | IC90 t | IC90 perm. | Delta propio -> desenlace | comun -> desenlace | direccion | margen min. |',
         '|---|---|---|---|---|---|---|---|']
    for et, r in res['modelos'].items():
        lp, lc = r['lecturas']['propio'], r['lecturas']['comun']
        L.append('| %s | %+.1f | [%+.1f, %+.1f] | [%+.1f, %+.1f] | %.1f -> %s | %.1f -> %s | %s | %.1f HU (%.0f %%) |'
                 % (et, r['media_HU'], *r['ic90_t'], *r['ic90_permutacion'], lp['Delta_HU'], lp['desenlace'],
                    lc['Delta_HU'], lc['desenlace'], r['direccion'], r['margen_minimo_HU'],
                    100 * r['margen_minimo_frac_Ti']))
    L += ['', '| modelo | CV difusor | CV Ti | r Pearson | Pitman-Morgan r (p) | Bland-Altman | costura | voxeles |',
          '|---|---|---|---|---|---|---|---|']
    for et, r in res['modelos'].items():
        ba = r['bland_altman']
        L.append('| %s | %.3f | %.3f | %.2f | %.2f (%.2g) | %+.1f [%+.1f, %+.1f] | %.1f | %.0f |'
                 % (et, r['cv_difusor'], r['cv_Ti'], r['pearson_r'], r['pitman_morgan']['r'], r['pitman_morgan']['p'],
                    ba['sesgo'], ba['lim_inf'], ba['lim_sup'], r['costura_mediana'], r['n_vox_mediana']))
    L += ['', 'Confirmatorio: solo `run04_mejor` con su `Delta` en la variante `base` (pto 15). Todo lo demas es '
          'descriptivo; multiplicidad declarada, sin correccion.']
    (out / 'a26_lecturas.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
