"""A24 - contrastes de E-A2 tal como se congelaron (diseno_A.md seccion 0; 01-decisiones 2026-10-09 (6) y (8)).

Entrada: el CSV de `a20_evaluador_ea2.py` de la corrida final (difusor, Peters y copia y pegado sobre los pacientes
de `casos_ea2_test.txt`) y `Delta` de validacion (`outputs/a20/a20_delta.json`).

Valor por paciente: difusor = mediana de las 5 semillas; Peters = mediana de las replicas A y B (por material);
copia y pegado = su unica corrida.

| Contraste | Prueba |
|---|---|
| PRIMARIO: difusor frente a Peters Ti | TOST pareado: IC90 de la diferencia media con t de Student; equivalencia si cae entera en [-Delta, +Delta] |
| Sensibilidad: frente a Peters Fe | el mismo TOST |
| Sensibilidad: sin los corredores angostos (0016, 0047, 0022) | el TOST primario con n = 10 |
| Cordura: difusor frente a copia y pegado | Wilcoxon de rangos con signo, una cola (difusor > copia y pegado), alfa 0.05 |

Se reporta siempre la fraccion de la ROI en el suelo de -1000 HU, y las metricas de integridad, descriptivas.

USO
---
    python experiments/objetivo3/a24_contrastes.py --csv experiments/objetivo3/outputs/a20/a20_ea2_test.csv
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy import stats

_AQUI = Path(__file__).resolve().parent
ANGOSTOS = {'dataset6_CLINIC_0016_data', 'dataset6_CLINIC_0047_data', 'dataset6_CLINIC_0022_data'}


def tost(d: np.ndarray, delta: float) -> dict:
    """TOST pareado con t de Student: IC90 de la media de `d` y p de las dos pruebas unilaterales."""
    n = d.size
    m, se = float(d.mean()), float(d.std(ddof=1) / np.sqrt(n))
    t = stats.t.ppf(0.95, n - 1)
    lo, hi = m - t * se, m + t * se
    p_inf = float(1 - stats.t.cdf((m + delta) / se, n - 1))   # H0: media <= -delta
    p_sup = float(stats.t.cdf((m - delta) / se, n - 1))       # H0: media >= +delta
    return {'n': n, 'media_HU': m, 'ic90_lo': lo, 'ic90_hi': hi, 'p_tost': max(p_inf, p_sup),
            'equivalente': bool(lo > -delta and hi < delta)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--csv', type=Path, required=True)
    ap.add_argument('--delta-json', type=Path, default=_AQUI / 'outputs' / 'a20' / 'a20_delta.json')
    ap.add_argument('--casos', type=Path, default=_AQUI / 'casos_ea2_test.txt')
    ap.add_argument('--etiqueta', default='mejor_37k')
    args = ap.parse_args()
    delta = json.loads(args.delta_json.read_text(encoding='utf-8'))['Delta_HU']
    casos = [c.strip() for c in args.casos.read_text(encoding='utf-8').split() if c.strip()]
    with open(args.csv, newline='', encoding='utf-8') as fh:
        filas = list(csv.DictReader(fh))

    def valor(caso, brazo, pref):
        v = [float(f['amp_HU']) for f in filas if f['caso'] == caso and f['brazo'] == brazo and f['condicion'].startswith(pref)]
        return float(np.median(v)) if v else float('nan'), len(v)

    tabla = []
    for c in casos:
        dif, ns = valor(c, 'difusor', args.etiqueta + '_s')
        ti, nti = valor(c, 'peters', 'Ti_')
        fe, nfe = valor(c, 'peters', 'Fe_')
        cp, ncp = valor(c, 'copiapega', 'HU_')
        suelo = [float(f['suelo_frac']) for f in filas if f['caso'] == c and f['brazo'] == 'difusor' and f['suelo_frac']]
        tabla.append({'caso': c, 'difusor': dif, 'semillas': ns, 'peters_Ti': ti, 'replicas_Ti': nti, 'peters_Fe': fe,
                      'replicas_Fe': nfe, 'copiapega': cp, 'suelo_frac': float(np.median(suelo)) if suelo else float('nan'),
                      'angosto': c in ANGOSTOS})
    falta = [t['caso'] for t in tabla if np.isnan(t['difusor']) or np.isnan(t['peters_Ti']) or np.isnan(t['copiapega'])]
    if falta:
        raise SystemExit('CONTROL: faltan brazos en %s' % falta)
    incompletos = [t['caso'] for t in tabla if t['semillas'] != 5 or t['replicas_Ti'] != 2 or t['replicas_Fe'] != 2]
    if incompletos:
        print('AVISO: semillas o replicas incompletas en %s' % incompletos)

    D = np.array([t['difusor'] for t in tabla])
    prim = tost(D - np.array([t['peters_Ti'] for t in tabla]), delta)
    fe = tost(D - np.array([t['peters_Fe'] for t in tabla]), delta)
    sel = np.array([not t['angosto'] for t in tabla])
    sin_ang = tost(D[sel] - np.array([t['peters_Ti'] for t in tabla])[sel], delta)
    cp = np.array([t['copiapega'] for t in tabla])
    w = stats.wilcoxon(D, cp, alternative='greater', zero_method='wilcox')

    out = _AQUI / 'outputs' / 'a24'
    out.mkdir(parents=True, exist_ok=True)
    with open(out / 'a24_por_paciente.csv', 'w', newline='', encoding='utf-8') as fh:
        wr = csv.DictWriter(fh, fieldnames=list(tabla[0].keys()))
        wr.writeheader()
        wr.writerows(tabla)
    res = {'Delta_HU': delta, 'primario_Ti': prim, 'sensibilidad_Fe': fe, 'sensibilidad_sin_angostos': sin_ang,
           'cordura_wilcoxon': {'n': int(D.size), 'estadistico': float(w.statistic), 'p_una_cola': float(w.pvalue),
                                'difusor_mayor': bool(w.pvalue < 0.05)}}
    (out / 'a24_contrastes.json').write_text(json.dumps(res, indent=2), encoding='utf-8')

    fmt = lambda r: ('n = %d | diferencia media %+.1f HU | IC90 [%+.1f, %+.1f] | p TOST %.4f | %s'  # noqa: E731
                     % (r['n'], r['media_HU'], r['ic90_lo'], r['ic90_hi'], r['p_tost'],
                        'EQUIVALENTE' if r['equivalente'] else 'no se concluye equivalencia'))
    L = ['# A24 — contrastes de E-A2 (corrida final, diseno congelado)', '',
         '`Delta` = %.1f HU (validacion, 01-decisiones 2026-10-09 (4)).' % delta, '',
         '- **PRIMARIO, difusor frente a Peters Ti:** ' + fmt(prim),
         '- Sensibilidad, frente a Peters Fe: ' + fmt(fe),
         '- Sensibilidad, sin corredores angostos: ' + fmt(sin_ang),
         '- Cordura, difusor > copia y pegado (Wilcoxon, una cola): n = %d | p = %.4g | %s'
         % (D.size, w.pvalue, 'supera el piso' if w.pvalue < 0.05 else 'NO supera el piso'),
         '', 'Fraccion de la ROI en el suelo de -1000 HU (difusor, mediana por paciente): max %.3f.'
         % np.nanmax([t['suelo_frac'] for t in tabla]),
         '', 'Por paciente: `a24_por_paciente.csv`. Con n = %d, "no se concluye equivalencia" puede ser falta de '
         'potencia (declaracion preaceptada, 2026-10-05 (6)).' % D.size]
    (out / 'a24_contrastes.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
