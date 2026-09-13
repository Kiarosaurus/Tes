"""R1 / implicancia #26 — resumen de `r1_landmarks.csv` con criterio calibrado.

COHORTES POR PACIENTE (2026-09-10; una unidad por paciente, sin reclasificar nada)
---------------------------------------------------------------------------------
- `calibracion`: dataset6 con `Objeto extraño = no` (`revision.csv`) que no este en
  `exclusiones.csv`. Da la distribucion nula de cada metrica en la misma anatomia y
  protocolo, sin metal.
- `evaluacion`: `grupo 1` de `grupos.csv` (material ortopedico presente, una unidad por
  paciente; incluye la union `metal_0059u0071`). Copias exactas internas: indice menor
  (#20, contenido identico).

Si existe `r1_auditoria_s1_agente.csv`, se cruza con el nivel de S1 auditado a ojo
(procedencia agente, no autora).

CRITERIO (no inventado: sale de la cohorte de calibracion)
---------------------------------------------------------
Para cada tipo de landmark, el umbral de `oscuro` y de `brillante` es el **maximo** observado
en calibracion (envolvente nula). Un landmark de evaluacion esta `contaminado` si supera la
envolvente en cualquiera de las dos. Contaminado NO significa irrecuperable, y no
contaminado NO significa localizado: es una particion para decidir que revisar a ojo.

El marco de Kaiser necesita los cinco puntos (S1, dos crestas, dos EIPS). Un volumen tiene
el marco `computable` si los cinco estan hallados y con `fov_ok`; `legible` si ademas
ninguno esta contaminado.

Solo lee CSV. Escribe `r1_landmarks.md`.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

LANDMARKS = ('S1', 'cresta_der', 'cresta_izq', 'eips_der', 'eips_izq')
TIPO = {'S1': 'S1', 'cresta_der': 'cresta', 'cresta_izq': 'cresta',
        'eips_der': 'eips', 'eips_izq': 'eips'}
DISCREPANCIA_MM = 10.0


def cohortes(rev: pd.DataFrame, grupos: pd.DataFrame,
             excl: pd.DataFrame) -> tuple[set[str], set[str]]:
    """Calibracion y evaluacion por paciente (revision.csv, grupos.csv, exclusiones.csv)."""
    oe = next(c for c in rev.columns if c.startswith('Objeto'))
    fuera = set(excl['Caso'])
    cal = rev[(rev['Dataset'] == 'dataset6') & (rev[oe] == 'no') & ~rev['Caso'].isin(fuera)]
    ev = grupos[grupos['Grupo'] == 'grupo 1']
    for nombre, d in (('calibracion', cal), ('evaluacion', ev)):
        if d['Grupo paciente'].duplicated().any():
            raise SystemExit(f'Cohorte {nombre} con pacientes repetidos. Abortado.')
    return set(cal['Caso']), set(ev['Caso'])


def estado(fila: pd.Series, nombre: str, umbral: dict[str, tuple[float, float]]) -> str:
    """`no hallado` / `fuera de FOV` / `contaminado` / `limpio` para un landmark."""
    if fila.get(f'{nombre}_hallado') != 'si':
        return 'no hallado'
    if fila.get(f'{nombre}_fov_ok') != 'si':
        return 'fuera de FOV'
    t_osc, t_bri = umbral[TIPO[nombre]]
    if fila[f'{nombre}_oscuro'] > t_osc or fila[f'{nombre}_brillante'] > t_bri:
        return 'contaminado'
    return 'limpio'


def main() -> None:
    """Punto de entrada de linea de comandos."""
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--csv', type=Path, default=here / 'r1_landmarks.csv')
    parser.add_argument('--revision', type=Path,
                        default=root / 'experiments' / 'exploration-3d' / 'revision.csv')
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    rev = pd.read_csv(args.revision)
    exp3d = args.revision.parent
    cal, ev = cohortes(rev, pd.read_csv(exp3d / 'grupos.csv'),
                       pd.read_csv(exp3d / 'exclusiones.csv'))
    faltan = ev - set(df['Caso'])
    if faltan:
        raise SystemExit(f'Unidades de evaluacion sin fila en r1_landmarks.csv: {faltan}')
    auditoria = here / 'r1_auditoria_s1_agente.csv'
    if auditoria.exists():
        df = df.merge(pd.read_csv(auditoria), on='Caso', how='left')
    clinico = here / 'r1_auditoria_s1_clinico.csv'
    if clinico.exists():
        # Llenada por un medico cirujano otorrinolaringologo (revisor clinico externo, informado
        # por la autora el 2026-09-11). Renombrado por la autora de _autora a _clinico.
        c = pd.read_csv(clinico, dtype=str).fillna('')
        sin_cruz = c['juicio_autora'].str.strip().eq('otro') & c['comentario'].str.contains(
            'no hay círculo rojo')
        c['auditoria_S1_clinico'] = np.where(sin_cruz, 'no hallado',
                                             c['juicio_autora'].str.strip())
        c.loc[c['auditoria_S1_clinico'] == '', 'auditoria_S1_clinico'] = np.nan
        df = df.merge(c[['Caso', 'auditoria_S1_clinico']], on='Caso', how='left')
    df['cohorte'] = np.where(df['Caso'].isin(cal), 'calibracion',
                             np.where(df['Caso'].isin(ev), 'evaluacion', 'otro'))

    # Envolvente nula por tipo de landmark, solo sobre puntos hallados y dentro del FOV.
    umbral: dict[str, tuple[float, float]] = {}
    c = df[df['cohorte'] == 'calibracion']
    for tipo in ('S1', 'cresta', 'eips'):
        osc, bri = [], []
        for nombre in [n for n in LANDMARKS if TIPO[n] == tipo]:
            ok = c[(c[f'{nombre}_hallado'] == 'si') & (c[f'{nombre}_fov_ok'] == 'si')]
            osc += ok[f'{nombre}_oscuro'].dropna().tolist()
            bri += ok[f'{nombre}_brillante'].dropna().tolist()
        umbral[tipo] = (float(np.max(osc)), float(np.max(bri)))

    for nombre in LANDMARKS:
        df[f'{nombre}_estado'] = [estado(f, nombre, umbral) for _, f in df.iterrows()]
    est = df[[f'{n}_estado' for n in LANDMARKS]]
    df['marco_computable'] = (~est.isin(['no hallado', 'fuera de FOV'])).all(axis=1)
    df['marco_legible'] = (est == 'limpio').all(axis=1)
    disc = df['s1_discrepancia_mm'].abs()
    df['s1_discordante'] = disc > DISCREPANCIA_MM

    L: list[str] = ['# R1 — legibilidad de los landmarks de Kaiser (implicancia #26)', '']
    errores = df['Error'].notna().sum() if 'Error' in df else 0
    L += [f'Volumenes en `r1_landmarks.csv`: {len(df)}; con error: {errores}.',
          f'Cohorte de calibracion (dataset6 sin objeto, una unidad por paciente): '
          f'{(df["cohorte"] == "calibracion").sum()}.',
          f'Cohorte de evaluacion (`grupo 1` de grupos.csv, una unidad por paciente): '
          f'{(df["cohorte"] == "evaluacion").sum()}.', '',
          '**Lectura obligatoria:** heuristica sin validacion experta. Las cifras son cota '
          'superior condicionada a que los puntos hayan caido en su sitio; ver laminas en '
          '`outputs/r1_qc/`. Contaminado no es irrecuperable.', '',
          '## Envolvente nula (maximo en calibracion)', '',
          '| Tipo | oscuro (HU < -200) | brillante (HU > 2500) |', '|---|---|---|']
    for tipo, (o, b) in umbral.items():
        L.append(f'| {tipo} | {o:.5f} | {b:.5f} |')

    for coh in ('calibracion', 'evaluacion'):
        d = df[df['cohorte'] == coh]
        n = len(d)
        L += ['', f'## Cohorte `{coh}` (n = {n})', '',
              '| Landmark | limpio | contaminado | fuera de FOV | no hallado |',
              '|---|---|---|---|---|']
        for nombre in LANDMARKS:
            vc = d[f'{nombre}_estado'].value_counts()
            L.append(f'| {nombre} | {vc.get("limpio", 0)} | {vc.get("contaminado", 0)} | '
                     f'{vc.get("fuera de FOV", 0)} | {vc.get("no hallado", 0)} |')
        L += ['', f'- Marco de Kaiser **computable** (5 puntos hallados y en FOV): '
                  f'**{int(d["marco_computable"].sum())} de {n}**.',
              f'- Marco **computable y sin contaminacion** en los 5 puntos: '
              f'**{int(d["marco_legible"].sum())} de {n}**.',
              f'- S1 con discrepancia > {DISCREPANCIA_MM:.0f} mm entre metodo sagital y metodo '
              f'del ala: {int(d["s1_discordante"].sum())} de '
              f'{int(d["s1_discrepancia_mm"].notna().sum())} con ambos metodos.']
        if 'auditoria_S1_clinico' in d and d['auditoria_S1_clinico'].notna().any():
            vc = d['auditoria_S1_clinico'].value_counts()
            ok = d['auditoria_S1_clinico'] == 'ok'
            L += [f'- **Nivel de S1 segun revisor clinico (medico ORL, referencia):** '
                  + ', '.join(f'{k} {v}' for k, v in vc.items())
                  + f'; sin revisar {int(d["auditoria_S1_clinico"].isna().sum())}.',
                  f'- Marco computable **con S1 correcto segun revisor clinico**: '
                  f'**{int((d["marco_computable"] & ok).sum())} de {n}**; ademas sin '
                  f'contaminacion: **{int((d["marco_legible"] & ok).sum())} de {n}**.']
            if 'auditoria_S1' in d:
                mapa = {'ok': 'ok', '+1 nivel': '+1', 'error grosero': 'otro',
                        'ambiguo': '?', 'no hallado': 'no hallado'}
                ag = d['auditoria_S1'].map(mapa)
                ambos = ag.notna() & d['auditoria_S1_clinico'].notna()
                a_ok, c_ok = (ag == 'ok')[ambos], ok[ambos]
                po = float((a_ok == c_ok).mean())
                pe = float(a_ok.mean() * c_ok.mean() + (1 - a_ok.mean()) * (1 - c_ok.mean()))
                kappa = (po - pe) / (1 - pe) if pe < 1 else float('nan')
                L.append(f'- Acuerdo agente vs revisor clinico ({int(ambos.sum())} casos): '
                         f'categoria exacta {float((ag == d["auditoria_S1_clinico"])[ambos].mean()):.3f}; '
                         f'ok/no-ok {po:.3f}, kappa de Cohen {kappa:.2f}.')
        if 'auditoria_S1' in d and d['auditoria_S1'].notna().any():
            vc = d['auditoria_S1'].value_counts()
            ok = d['auditoria_S1'] == 'ok'
            L += [f'- Auditoria visual del nivel de S1 (agente): '
                  + ', '.join(f'{k} {v}' for k, v in vc.items())
                  + f'; sin auditar {int(d["auditoria_S1"].isna().sum())}.',
                  f'- Marco computable **con S1 auditado ok**: '
                  f'**{int((d["marco_computable"] & ok).sum())} de {n}**; ademas sin '
                  f'contaminacion: **{int((d["marco_legible"] & ok).sum())} de {n}**.']
        s = d['s1_bajo_cresta_mm'].dropna()
        if len(s):
            L.append(f'- S1 bajo la cresta (mm): mediana {s.median():.1f}, '
                     f'rango {s.min():.1f} a {s.max():.1f}.')
        if coh == 'evaluacion':
            for nombre in LANDMARKS:
                dm = d.loc[d[f'{nombre}_hallado'] == 'si', f'{nombre}_dist_metal_mm'].dropna()
                if len(dm):
                    L.append(f'- `{nombre}`: metal a <= 12 mm en {int((dm <= 12).sum())}, '
                             f'a <= 25 mm en {int((dm <= 25).sum())} de {len(dm)}; '
                             f'distancia mediana {dm.median():.1f} mm.')
            fallan = d[~d['marco_legible']]
            L += ['', '### Volumenes de evaluacion sin marco legible', '',
                  '| Caso | ' + ' | '.join(LANDMARKS) + ' | S1 discordante |',
                  '|---|' + '---|' * (len(LANDMARKS) + 1)]
            for _, f in fallan.iterrows():
                L.append(f'| {f["Caso"]} | ' + ' | '.join(f[f"{n}_estado"] for n in LANDMARKS)
                         + f' | {"si" if f["s1_discordante"] else "no"} |')

    out = args.csv.with_suffix('.md')
    out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    df.to_csv(args.csv.with_name('r1_estados.csv'), index=False)
    print('\n'.join(L))


if __name__ == '__main__':
    main()
