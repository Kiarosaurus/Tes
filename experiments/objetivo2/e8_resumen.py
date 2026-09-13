"""E8 — resumen de `e8_componentes.csv` (implicancias #41 y #13).

Todo es **propuesta de script sin validar**: clases morfologicas, no tipos de implante. Se
reporta sobre la misma cohorte de evaluacion de R1 (`r1_estados.csv`: `grupo 1` de
`grupos.csv`, una unidad por paciente, con la union `0059u0071`) y, aparte, sobre todos los
archivos analizados.

Contraste de calibre: el rango 6.0-8.0 mm es la envolvente de los calibres de tornillo
iliosacro recogidos en la tabla de #31 (`wagner2017` 6.0-7.3; `gardner2010safezones` y
`lee2014` 6.5-8.0; `grass2016` 7.3). Es un contraste de orden de magnitud, **no** el calibre
real de estos implantes, que ningun documento del repositorio registra.

Solo lee CSV. Escribe `e8_componentes.md`.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

CALIBRE_PUBLICADO = (6.0, 8.0)


def main() -> None:
    """Punto de entrada."""
    here = Path(__file__).resolve().parent
    c = pd.read_csv(here / 'e8_componentes.csv')
    est = pd.read_csv(here / 'r1_estados.csv')
    ev = set(est.loc[est['cohorte'] == 'evaluacion', 'Caso'])
    L: list[str] = ['# E8 — censo morfologico del metal en dataset7 (#41, #13)', '',
                    'Propuesta de script sin validar. Clases morfologicas, no tipos de implante. '
                    'Laminas en `outputs/e8_qc/`.', '']
    errores = c['Error'].notna().sum()
    L.append(f'Volumenes: {c["Caso"].nunique()}; con error: {errores}.')

    obj = c[c['clase'].isin(['alargado', 'laminar', 'masivo', 'otro'])]
    dentro = obj[obj['frac_dentro_cuerpo'] >= 0.5]
    for nombre, casos in (('evaluacion (`grupo 1`, una unidad por paciente)', ev),
                          ('todos los archivos analizados (75 de dataset7 + union derivada)',
                           set(c['Caso']))):
        d = dentro[dentro['Caso'].isin(casos)]
        n = len(casos)
        L += ['', f'## Cohorte: {nombre} (n = {n})', '',
              '| Clase (objetos dentro del cuerpo) | objetos | volumenes con >= 1 |',
              '|---|---|---|']
        for clase in ('alargado', 'laminar', 'masivo', 'otro'):
            s = d[d['clase'] == clase]
            L.append(f'| {clase} | {len(s)} | {s["Caso"].nunique()} |')
        cand = d[d['candidato_IS'] == 'si']
        L += ['', f'- Volumenes con **>= 1 candidato a tornillo iliosacro/transsacro**: '
                  f'**{cand["Caso"].nunique()} de {n}** ({len(cand)} objetos).',
              f'- Volumenes sin ningun objeto dentro del cuerpo: '
              f'{n - d["Caso"].nunique()}.']

    a = dentro[(dentro['clase'] == 'alargado') & dentro['Caso'].isin(ev)]
    if len(a):
        L += ['', '## Objetos alargados (cohorte de evaluacion)', '',
              f'- Objetos: {len(a)}; formados por mas de un fragmento a HU > 2500: '
              f'**{int((a["n_fragmentos"] > 1).sum())}**.',
              '', '| Medida (mm) | mediana | p10 | p90 |', '|---|---|---|---|']
        for col in ('L_mm', 'd_eq_2500_mm', 'd_ext_2500_mm', 'd_ext_semimax_mm'):
            s = a[col].dropna()
            L.append(f'| `{col}` | {s.median():.2f} | {s.quantile(.1):.2f} | '
                     f'{s.quantile(.9):.2f} |')
        dd = (a['d_ext_2500_mm'] - a['d_ext_semimax_mm']).dropna()
        s = a['d_ext_semimax_mm'].dropna()
        lo, hi = CALIBRE_PUBLICADO
        L += ['', f'- `d_ext_2500 - d_ext_semimax`: mediana {dd.median():.2f} mm '
                  f'(p10 {dd.quantile(.1):.2f}, p90 {dd.quantile(.9):.2f}).',
              f'- `d_ext_semimax` dentro de {lo}-{hi} mm: {int(s.between(lo, hi).sum())} de '
              f'{len(s)}; por debajo: {int((s < lo).sum())}; por encima: '
              f'{int((s > hi).sum())}.',
              f'- Umbral de semimaximo local: mediana {a["hu_umbral_semimax"].median():.0f} HU '
              f'(p10 {a["hu_umbral_semimax"].quantile(.1):.0f}, '
              f'p90 {a["hu_umbral_semimax"].quantile(.9):.0f}); HU p50 del objeto: mediana '
              f'{a["hu_p50"].median():.0f}.']
        cand = a[a['candidato_IS'] == 'si'].sort_values('Caso')
        L += ['', '### Candidatos a tornillo iliosacro/transsacro', '',
              '| Caso | L | fragmentos | d_ext_2500 | d_ext_semimax | dz a S1 | HU p50 |',
              '|---|---|---|---|---|---|---|']
        for _, f in cand.iterrows():
            L.append(f'| {f["Caso"]} | {f["L_mm"]:.0f} | {int(f["n_fragmentos"])} | '
                     f'{f["d_ext_2500_mm"]:.2f} | {f["d_ext_semimax_mm"]:.2f} | '
                     f'{f["dz_S1_mm"]:.0f} | {int(f["hu_p50"])} |')
    (here / 'e8_componentes.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
