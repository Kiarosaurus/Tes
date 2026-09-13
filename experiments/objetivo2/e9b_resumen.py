"""Resumen de E9b con y sin los 7 pacientes de FOV cortado (decision pendiente de la autora).

Cohortes:
- `evaluacion con los 7`: `grupo 1` con S1 correcto segun el revisor clinico.
- `evaluacion sin los 7`: la anterior sin los pacientes con alguna cresta fuera del FOV.
- `calibracion`: dataset6 sin objeto con S1 hallado (nivel de S1 **no** auditado).

Solo lee CSV. Escribe `e9b_densidad_s1.md`.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def main() -> None:
    """Tablas de densidad por cohorte."""
    here = Path(__file__).resolve().parent
    d = pd.read_csv(here / 'e9b_densidad_s1.csv').set_index('Caso')
    est = pd.read_csv(here / 'r1_estados.csv').set_index('Caso')
    ev = est[est['cohorte'] == 'evaluacion']
    ok = ev.index[ev['auditoria_S1_clinico'] == 'ok']
    fov = ev.index[(ev['cresta_der_estado'] == 'fuera de FOV') | (ev['cresta_izq_estado'] == 'fuera de FOV')]
    cohortes = {
        'evaluacion con los 7 (S1 ok clinico)': [c for c in ok if c in d.index],
        'evaluacion sin los 7': [c for c in ok if c in d.index and c not in fov],
        'solo los 7 (con S1 ok)': [c for c in ok if c in d.index and c in fov],
        'calibracion (sin metal; S1 no auditado)': list(d.index[d['cohorte'] == 'calibracion']),
    }
    L = ['# E9b — densidad del esponjoso de S1 (sonda para E9)', '',
         'Mediana de HU en esferas de 6 mm (cuerpo de S1 y alas a 25 mm del plano medio, 12 mm '
         'bajo el platillo). `< 150` = la esfera queda fuera de la mascara HU > 150.', '',
         '| Cohorte | n | HU cuerpo (mediana) | cuerpo < 150 | HU ala izq | ala izq < 150 | '
         'HU ala der | ala der < 150 | alguna esfera < 150 |', '|---|---|---|---|---|---|---|---|---|']
    for nombre, casos in cohortes.items():
        s = d.loc[casos]
        n = len(s)
        if n == 0:
            continue
        bajo = {k: int((s[f'hu_{k}'] < 150).sum()) for k in ('cuerpo', 'ala_izq', 'ala_der')}
        alguna = int(((s['hu_cuerpo'] < 150) | (s['hu_ala_izq'] < 150) | (s['hu_ala_der'] < 150)).sum())
        L.append(f'| {nombre} | {n} | {s["hu_cuerpo"].median():.0f} | {bajo["cuerpo"]} | '
                 f'{s["hu_ala_izq"].median():.0f} | {bajo["ala_izq"]} | {s["hu_ala_der"].median():.0f} | '
                 f'{bajo["ala_der"]} | {alguna} ({100 * alguna / n:.0f}%) |')
    (here / 'e9b_densidad_s1.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
