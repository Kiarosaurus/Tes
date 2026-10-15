"""A29 - perfil radial por brazo y contraste pareado del difusor (#187 c, #188). POSTERIOR y descriptivo.

Regla fijada antes de correr en `resultados_dec_2026-10-15.md`, seccion "Perfil por anillos y contraste pareado":
- (i)  8-12 mm: si el difusor pareado queda bajo la mitad del sin parear, el exceso de #187 es piso de regeneracion;
- (ii) forma: razon de decaimiento por paciente = amplitud(0-2 mm) / amplitud(6-8 mm); D1 real = 1930 / 473 = 4.1;
       brazo "plano" si su razon mediana es < 2;
- (iii) banda completa pareada: media de (difusor pareado - Peters Ti) con IC90 *t*, frente a `Delta` comun 196.3.

Valor por paciente igual que `a26`: difusor = mediana de 5 semillas; Peters Ti = mediana de A y B; parametrico = su
unica fila. Entradas: CSV de `a20` por anillo (`--dir-anillos`, `a20_test_rAA_BB.csv`) y, opcional, los de
`a20_pareado.sbatch` (`--dir-pareado`, `a20_pareado_<variante>.csv`).

USO
---
    python experiments/objetivo3/a29_perfil.py --dir-anillos outputs/obj3_pose/a20_variantes \\
        [--dir-pareado outputs/khipu_<fecha>/pareado] --out-dir outputs/a29
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy import stats

_AQUI = Path(__file__).resolve().parent
ANILLOS = ['r00_02', 'r02_04', 'r04_06', 'r06_08', 'r08_10', 'r10_12']
D1_REAL = {'r00_02': 1930.0, 'r02_04': 1199.0, 'r04_06': 765.0, 'r06_08': 473.0, 'r08_10': 174.0, 'r10_12': 11.0}
DELTA_COMUN = 196.3


def por_paciente(ruta: Path, casos: list[str]) -> dict[str, np.ndarray]:
    """Amplitud por paciente de cada brazo presente en el CSV."""
    with open(ruta, newline='', encoding='utf-8') as fh:
        filas = [f for f in csv.DictReader(fh) if f['amp_HU'] not in ('', 'nan')]

    def med(caso: str, pred) -> float:
        v = [float(f['amp_HU']) for f in filas if f['caso'] == caso and pred(f)]
        return float(np.median(v)) if v else float('nan')
    brazos = {
        'peters_Ti': lambda f: f['brazo'] == 'peters' and f['condicion'].startswith('Ti_'),
        'parametrico': lambda f: f['brazo'] == 'parametrico',
        'difusor': lambda f: f['brazo'] == 'difusor' and not f['condicion'].endswith('_pareado'),
        'difusor_pareado': lambda f: f['brazo'] == 'difusor' and f['condicion'].endswith('_pareado'),
    }
    out = {}
    for b, pred in brazos.items():
        x = np.array([med(c, pred) for c in casos])
        if not np.isnan(x).all():
            out[b] = x
    return out


def ic_t(d: np.ndarray) -> tuple[float, float, float]:
    n = d.size
    m, se = float(d.mean()), float(d.std(ddof=1) / np.sqrt(n))
    t = stats.t.ppf(0.95, n - 1)
    return m, m - t * se, m + t * se


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir-anillos', type=Path, required=True)
    ap.add_argument('--dir-pareado', type=Path, default=None)
    ap.add_argument('--casos', type=Path, default=_AQUI / 'casos_ea2_test.txt')
    ap.add_argument('--out-dir', type=Path, required=True)
    args = ap.parse_args()
    casos = [c.strip() for c in args.casos.read_text(encoding='utf-8').split() if c.strip()]

    perfil: dict[str, dict[str, np.ndarray]] = {}
    for a in ANILLOS:
        perfil[a] = por_paciente(args.dir_anillos / ('a20_test_%s.csv' % a), casos)
        if args.dir_pareado:
            rp = args.dir_pareado / ('a20_pareado_%s.csv' % a)
            if rp.exists():
                perfil[a].update({k: v for k, v in por_paciente(rp, casos).items() if k == 'difusor_pareado'})
    brazos = [b for b in ('peters_Ti', 'parametrico', 'difusor', 'difusor_pareado') if b in perfil[ANILLOS[0]]]

    res: dict = {'perfil_mediana': {}, 'decaimiento': {}, 'regla_i': {}, 'regla_iii': None}
    L = ['# A29 — perfil radial por brazo (prueba, v1, 13 pacientes)', '',
         'Mediana entre pacientes de la amplitud por anillo (HU). D1 real = exceso mediano de `d1_d2_resultado.md` '
         '(otra metrica de referencia: forma, no nivel).', '',
         '| anillo | ' + ' | '.join(brazos) + ' | D1 real |', '|---' * (len(brazos) + 2) + '|']
    for a in ANILLOS:
        meds = {b: float(np.nanmedian(perfil[a][b])) for b in brazos if b in perfil[a]}
        nval = {b: int(np.isfinite(perfil[a][b]).sum()) for b in meds}
        res['perfil_mediana'][a] = meds
        res.setdefault('n_pacientes', {})[a] = nval
        L.append('| %s | ' % a + ' | '.join('%.0f%s' % (meds[b], '' if nval[b] == len(casos) else ' (n=%d)' % nval[b])
                                         if b in meds else '—' for b in brazos) + ' | %.0f |' % D1_REAL[a])

    L += ['', '## (ii) Forma: razon amplitud(0-2) / amplitud(6-8) por paciente', '',
          '| brazo | razon mediana [p25, p75] | plano (< 2) |', '|---|---|---|']
    for b in brazos:
        if b not in perfil['r06_08']:
            continue
        r = perfil['r00_02'][b] / perfil['r06_08'][b]
        r = r[np.isfinite(r)]                         # Peters: anillo 0-2 sin ROIs validas en algunos pacientes
        q = np.percentile(r, [25, 50, 75])
        res['decaimiento'][b] = {'mediana': float(q[1]), 'p25': float(q[0]), 'p75': float(q[2]),
                                 'plano': bool(q[1] < 2.0)}
        res['decaimiento'][b]['n'] = int(r.size)
        L.append('| %s (n=%d) | %.2f [%.2f, %.2f] | %s |' % (b, r.size, q[1], q[0], q[2], 'si' if q[1] < 2 else 'no'))
    L.append('| D1 real | %.2f | no |' % (D1_REAL['r00_02'] / D1_REAL['r06_08']))

    if 'difusor_pareado' in brazos:
        L += ['', '## (i) 8-12 mm: difusor pareado frente a sin parear', '']
        for a in ('r08_10', 'r10_12'):
            if 'difusor_pareado' in perfil[a]:
                p, s = float(np.median(perfil[a]['difusor_pareado'])), float(np.median(perfil[a]['difusor']))
                res['regla_i'][a] = {'pareado': p, 'sin_parear': s, 'piso': bool(p < 0.5 * s)}
                L.append('- %s: pareado %.0f HU, sin parear %.0f HU -> %s' % (
                    a, p, s, 'exceso atribuido al piso de regeneracion' if p < 0.5 * s else 'no se atribuye al piso'))
        rb = args.dir_pareado / 'a20_pareado_base.csv'
        if rb.exists():
            base = por_paciente(rb, casos)
            ref = por_paciente(args.dir_anillos / 'a20_test_base.csv', casos)['peters_Ti']
            d = base['difusor_pareado'] - ref
            m, lo, hi = ic_t(d)
            r_p = float(stats.pearsonr(base['difusor_pareado'], ref)[0])
            res['regla_iii'] = {'media': m, 'ic90': [lo, hi], 'Delta_comun': DELTA_COMUN, 'pearson_Ti': r_p,
                                'mediana_pareado': float(np.median(base['difusor_pareado'])),
                                'mediana_Ti': float(np.median(ref))}
            L += ['', '## (iii) Banda completa pareada (descriptivo; no cambia el desenlace confirmatorio)', '',
                  '- difusor pareado - Peters Ti: %+.1f HU, IC90 [%+.1f, %+.1f] (Delta comun %.1f); '
                  'mediana pareado %.0f, Ti %.0f; Pearson con Ti %.2f'
                  % (m, lo, hi, DELTA_COMUN, res['regla_iii']['mediana_pareado'], res['regla_iii']['mediana_Ti'], r_p)]
    else:
        L += ['', 'Sin CSV pareados: reglas (i) y (iii) pendientes de `a20_pareado.sbatch` (Khipu).']

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / 'a29_perfil.json').write_text(json.dumps(res, indent=2), encoding='utf-8')
    (args.out_dir / 'a29_perfil.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
