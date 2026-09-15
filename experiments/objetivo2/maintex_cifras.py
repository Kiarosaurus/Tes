"""Recalcula las cifras del parrafo `Corridor measurement on the local cohort` de `tesis/main.tex`.

POR QUE
-------
Las cifras de ese parrafo salieron de `outputs/`, que git ignora. Este script las rehace solo desde
tablas versionadas y comprueba que `main.tex` dice exactamente eso.

ENTRADAS (versionadas)
----------------------
- `e9ts_corredor.csv`: copia de la salida de E9-TS (jobs 51505 y 51523, 2026-09-14).
- `../exploration-3d/grupos.csv`: reparto por objetivo (#35).

Cohorte y QC como `e9ts_resumen.py`: grupos 2 y 3; QC de nivel = `estado_TS == concordante` y S1 sin
tocar el FOV. Recorte principal 6 mm (decision 2026-09-14 (4)); F = 0.001 (decisiones (3) y (5));
implante como hueso, salvo en el contraste de ocupacion del grupo 1.

CONTROL QUE PUEDE FALLAR
------------------------
Cada frase se construye con el valor recalculado y se busca literal en `main.tex`. Si alguna no
aparece, la cifra impresa no coincide con la tabla: se marca `DIFIERE` y el script sale con codigo 1.
No cubre las cifras de R1 del parrafo `Field limitation`.

Escribe `maintex_cifras.md`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
F_PRINCIPAL = 0.001
PRINCIPAL, SENSIBILIDAD = 'default6mm', 'robust3mm'
MEDIDAS = ['D_TS_max_mm', 'L_TS_mejor_mm', 'D_IS_izq_max_mm', 'D_IS_der_max_mm', 'hu_p50_eje',
           'frac_bajo150_eje', 'viable_TS_10mm', 'viable_TS_d6.5_c1', 'viable_TS_d6.5_c2',
           'viable_TS_d7.3_c1', 'viable_TS_d7.3_c2', 'viable_TS_d8.0_c1', 'viable_TS_d8.0_c2']


def qc_nivel(d: pd.DataFrame) -> pd.DataFrame:
    """Filtro de QC de nivel de `e9ts_resumen.py`."""
    return d[(d['estado_TS'] == 'concordante') & d['S1_toca_fov'].isna()]


def pct_viable(d: pd.DataFrame) -> float:
    """Porcentaje de casos viables a 10 mm."""
    return float((d['viable_TS_10mm'] == 'si').mean() * 100)


def main() -> int:
    """Recalcula, busca cada frase en `main.tex` y escribe el informe."""
    tex = (RAIZ / 'tesis' / 'main.tex').read_text(encoding='utf-8')
    c = pd.read_csv(AQUI / 'e9ts_corredor.csv')
    c = c[c['Error'].isna()]
    g = pd.read_csv(RAIZ / 'experiments' / 'exploration-3d' / 'grupos.csv')

    hueso = c[c['politica_metal'] == 'hueso']
    base = hueso[(hueso['F_limpieza'] == F_PRINCIPAL) & (hueso['modo'] == PRINCIPAL)]
    obj2 = base[base['Grupo'].isin(['grupo 2', 'grupo 3'])]
    qc = qc_nivel(obj2)
    g2, g3 = obj2[obj2['Grupo'] == 'grupo 2'], obj2[obj2['Grupo'] == 'grupo 3']
    n_fov = int(obj2['S1_toca_fov'].notna().sum())
    sens = qc_nivel(hueso[(hueso['F_limpieza'] == F_PRINCIPAL) & (hueso['modo'] == SENSIBILIDAD)
                          & hueso['Grupo'].isin(['grupo 2', 'grupo 3'])])

    # Limpieza: ninguna medida cambia entre F en la cohorte del Objetivo 2 (los dos recortes).
    todas_f = qc_nivel(hueso[hueso['Grupo'].isin(['grupo 2', 'grupo 3'])])
    todas_f = todas_f[todas_f['Caso'].isin(qc['Caso'])]
    variables = todas_f.groupby(['Caso', 'modo'])[MEDIDAS].nunique(dropna=False)
    cols_cambian = sorted(variables.columns[(variables > 1).any(axis=0)])
    cambian = variables[(variables[['D_TS_max_mm', 'viable_TS_10mm']] > 1).any(axis=1)]
    otras = variables[(variables > 1).any(axis=1)]

    # Contraste de ocupacion, grupo 1 (casos sin metal en el recorte no tienen filas ocupadas).
    g1 = qc_nivel(c[(c['Grupo'] == 'grupo 1') & (c['modo'] == PRINCIPAL) & (c['F_limpieza'] == F_PRINCIPAL)])
    g1_h = g1[g1['politica_metal'] == 'hueso'].set_index('Caso')['viable_TS_10mm']

    def pct_politica(pol: str) -> float:
        s = g1[g1['politica_metal'] == pol].set_index('Caso')['viable_TS_10mm']
        return float((s.reindex(g1_h.index).fillna(g1_h) == 'si').mean() * 100)

    p_semi, p_2500 = pct_politica('ocupado_semimax'), pct_politica('ocupado_2500')
    uno = {1: 'one'}.get(n_fov, str(n_fov))
    d = qc['D_TS_max_mm']

    filas = [
        ('Cohorte sin osteosintesis', f'Among {int((g["Elegible Obj2"] == "si").sum())} patients without osteosynthesis'),
        ('Con S1 localizado', f'{obj2["Caso"].nunique()} had a located S1'),
        ('Pasan la QC de nivel', f'{qc["Caso"].nunique()} passed level quality control'),
        ('Discordancia, grupo 2',
         f'excluded {int((g2["estado_TS"] == "R1 arriba de TS").sum())} of {g2["Caso"].nunique()} patients with non-orthopaedic objects'),
        ('Discordancia, grupo 3',
         f'{int((g3["estado_TS"] == "R1 arriba de TS").sum())} of {g3["Caso"].nunique()} clean patients'),
        ('S1 en el borde del FOV', f'{uno} further patient was excluded because S1 reached the field-of-view border'),
        ('Mediana e IQR de D_TS (6 mm)',
         f'median of {d.median():.1f}~mm (IQR {d.quantile(0.25):.1f}--{d.quantile(0.75):.1f})'),
        ('Viables a 10 mm, 6 mm y 3 mm',
         f'met in {int((qc["viable_TS_10mm"] == "si").sum())} of {qc["Caso"].nunique()} patients with the default crop '
         f'and in {int((sens["viable_TS_10mm"] == "si").sum())} with the robust crop'),
        ('Limpieza sin efecto en D_TS ni viabilidad (F en 0-0.05, ambos recortes)',
         'Component cleaning changed neither the transsacral corridor diameter nor its 10~mm viability in this '
         'cohort at any tested fraction up to 5\\%'
         if cambian.empty else f'CAMBIAN D_TS o viabilidad en {len(cambian)} caso x recorte'),
        ('Fraccion del eje <= 150 HU (6 mm)', f'inside the sacral masks was {qc["frac_bajo150_eje"].median():.2f}'),
        ('Grupo 1: hueso -> semimaximo',
         f'from {pct_viable(g1[g1["politica_metal"] == "hueso"]):.1f}\\% to {p_semi:.1f}\\% in {g1_h.index.nunique()} patients with the default crop'),
        ('Grupo 1: 2500 HU igual que semimaximo',
         'gave the same proportion' if abs(p_2500 - p_semi) < 0.05 else f'2500 HU da {p_2500:.1f}% frente a {p_semi:.1f}%'),
    ]

    L = ['# Cifras de `main.tex` recalculadas (`Corridor measurement on the local cohort`)', '',
         'Generado por `maintex_cifras.py` desde `e9ts_corredor.csv` y `grupos.csv` (versionados).',
         f'Recorte principal `{PRINCIPAL}`, sensibilidad `{SENSIBILIDAD}`, F = {F_PRINCIPAL}. '
         'Cada frase se busca literal en `tesis/main.tex`. No cubre `Field limitation` (R1).', '',
         '| # | Cifra | Frase buscada | Resultado |', '|---|---|---|---|']
    fallos = 0
    for i, (nombre, frase) in enumerate(filas, 1):
        ok = frase in tex
        fallos += not ok
        L.append(f'| {i} | {nombre} | `{frase}` | {"COINCIDE" if ok else "**DIFIERE**"} |')
    L += ['', f'**{len(filas) - fallos} de {len(filas)} cifras coinciden.**', '',
          f'Informativo (no impreso en `main.tex`): medidas que cambian con F en la cohorte: {cols_cambian or "ninguna"}, '
          f'en {len(otras)} caso x recorte: {sorted(set(otras.index.get_level_values(0)))}.', '']
    (AQUI / 'maintex_cifras.md').write_text('\n'.join(L), encoding='utf-8')
    print('\n'.join(L))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
