"""Resumen de E9-TS y E10 para la revision de la manana. Solo lee CSV. **No elige nada.**

Lee `e9ts_corredor.csv` y, si existen, `ts_componentes_resumen.csv` y `ts_componentes.csv` (E10).
Escribe `e9ts_resumen.md` con:
1. integridad (casos, errores, filas por caso, politicas de metal);
2. corredor por recorte x F con el implante como hueso (`politica_metal = hueso`):
   - **cohorte del Objetivo 2** (decision #52 a del 2026-09-14): grupos 2 y 3 con QC de nivel;
   - grupo 1 (con y sin los 7 de FOV cortado) y todos, como contraste;
   QC de nivel = `estado_TS = concordante` y S1 sin tocar el FOV;
3. sensibilidad: F frente a F = 0, y 6 mm frente a 3 mm;
4. #52 (c): diferencia de `D_TS` entre el implante como hueso y como espacio ocupado (2500 HU y
   semimaximo local), en los casos con metal en el recorte;
5. densidad en el eje del mejor corredor y paso por metal;
6. E10: que quita cada F, y componentes grandes no principales (candidatos a fragmento de fractura).

USO
---
    python e9ts_resumen.py --e9-dir ~/metalsynth/data/e9ts --e10-dir ~/metalsynth/data/ts_componentes
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

FRACCIONES = [0.0, 0.001, 0.01, 0.05]
UMBRALES = ['viable_TS_10mm', 'viable_TS_d6.5_c1', 'viable_TS_d7.3_c1', 'viable_TS_d8.0_c2']


def md(df: pd.DataFrame, index: bool = True) -> str:
    """DataFrame a tabla Markdown."""
    d = df.reset_index() if index else df
    filas = ['| ' + ' | '.join(map(str, d.columns)) + ' |', '|' + '---|' * len(d.columns)]
    filas += ['| ' + ' | '.join('' if pd.isna(v) else str(v) for v in r) + ' |' for r in d.itertuples(index=False)]
    return '\n'.join(filas)


def verdad(s: pd.Series) -> pd.Series:
    """Columna booleana leida de CSV (True/False como texto)."""
    return s.astype(str).str.lower().eq('true')


def tabla_corredor(d: pd.DataFrame) -> pd.DataFrame:
    """Mediana e IQR de D_TS y porcentaje viable por recorte x F."""
    g = d.groupby(['modo', 'F_limpieza'])
    t = g['D_TS_max_mm'].agg(n='count', D_p25=lambda x: x.quantile(.25), D_p50='median',
                             D_p75=lambda x: x.quantile(.75))
    for u in UMBRALES:
        t[u.replace('viable_TS_', '%_')] = g[u].apply(lambda x: 100 * (x == 'si').mean())
    return t.round(1)


def main() -> None:
    """Calcula y escribe el resumen."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--e9-dir', type=Path, required=True)
    parser.add_argument('--e10-dir', type=Path, default=None)
    parser.add_argument('--modo-principal', choices=['default6mm', 'robust3mm'], default='default6mm',
                        help='recorte de la seccion 5 (densidad); las demas secciones muestran los dos')
    args = parser.parse_args()
    e9_dir = args.e9_dir.expanduser()
    L = ['# E9-TS y E10 — resumen automatico (generado por `e9ts_resumen.py`; no elige nada)', '']

    d = pd.read_csv(e9_dir / 'e9ts_corredor.csv')
    err = d[d['Error'].notna()]
    ok = d[d['Error'].isna()].copy()
    por_caso = ok.groupby('Caso').size()
    L += ['## 1. Integridad', '',
          f'- Casos: {d["Caso"].nunique()}; con error: {err["Caso"].nunique()}; filas validas: {len(ok)}.',
          '- Filas por caso (8 sin metal en el recorte; 24 con metal): '
          + ', '.join(f'{k} filas: {v} casos' for k, v in por_caso.value_counts().sort_index().items()) + '.',
          f'- Filas por politica de metal: {ok["politica_metal"].value_counts().to_dict()}.',
          f'- Variantes reutilizadas por mascara identica (`igual_a_F`): {int(ok["igual_a_F"].notna().sum())} '
          f'de {len(ok)}.', '']
    if len(err):
        L += [md(err[['Caso', 'Error']].set_index('Caso')), '']
    if ok.empty:
        (e9_dir / 'e9ts_resumen.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
        return

    hueso = ok[ok['politica_metal'] == 'hueso']
    qc = hueso[(hueso['estado_TS'] == 'concordante') & hueso['S1_toca_fov'].isna()]
    obj2 = qc[qc['Grupo'].isin(['grupo 2', 'grupo 3'])]
    L += ['## 2. Corredor transsacro por recorte x F (implante como hueso)', '',
          f'### Cohorte del Objetivo 2 (#52 a): grupos 2 y 3, QC de nivel: {obj2["Caso"].nunique()} casos', '',
          md(tabla_corredor(obj2)), '']
    for grupo in ('grupo 3', 'grupo 2', 'grupo 1'):
        sub = qc[qc['Grupo'] == grupo]
        if len(sub):
            L += [f'### QC de nivel, {grupo}: {sub["Caso"].nunique()} casos', '', md(tabla_corredor(sub)), '']
    g1 = qc[qc['Grupo'] == 'grupo 1']
    if len(g1):
        sin7 = g1[~verdad(g1['fov7'])]
        L += [f'### QC de nivel, grupo 1 sin los 7 de FOV cortado: {sin7["Caso"].nunique()} casos', '',
              md(tabla_corredor(sin7)), '']
    L += [f'### Todos, sin QC: {hueso["Caso"].nunique()} casos', '', md(tabla_corredor(hueso)), '']

    p = qc.pivot_table(index='Caso', columns=['modo', 'F_limpieza'], values='D_TS_max_mm')
    L += ['## 3. Sensibilidad (implante como hueso, QC de nivel)', '']
    filas = []
    for modo in ('default6mm', 'robust3mm'):
        for f in FRACCIONES[1:]:
            if (modo, f) in p and (modo, 0.0) in p:
                dif = (p[(modo, f)] - p[(modo, 0.0)]).dropna()
                filas.append({'modo': modo, 'F': f, 'n': len(dif), 'casos_con_cambio': int((dif.abs() > 0).sum()),
                              'dif_mediana_mm': round(float(dif.median()), 2), 'dif_min_mm': round(float(dif.min()), 1),
                              'dif_max_mm': round(float(dif.max()), 1)})
    if filas:
        L += ['Efecto de F (D con F menos D sin limpieza):', '', md(pd.DataFrame(filas), index=False), '']
    for f in FRACCIONES:
        if ('default6mm', f) in p and ('robust3mm', f) in p:
            dif = (p[('default6mm', f)] - p[('robust3mm', f)]).dropna()
            cambia = int(((p[('default6mm', f)] >= 10) != (p[('robust3mm', f)] >= 10)).sum())
            L.append(f'- Recorte, F = {f}: D(6 mm) - D(3 mm) en {len(dif)} casos: mediana {dif.median():.2f} mm, '
                     f'|dif| p90 {dif.abs().quantile(.9):.1f} mm, max {dif.abs().max():.1f} mm; '
                     f'viable 10 mm cambia en {cambia} casos ({100 * cambia / max(len(dif), 1):.0f}%).')
    L.append('')

    L += ['## 4. #52 (c): implante como hueso frente a implante como espacio ocupado', '',
          'Solo casos con voxeles > 2500 HU en el recorte; QC de nivel. `ocupado_2500` es cota superior del '
          'corredor ocupado (2500 HU adelgaza el implante, #46); `ocupado_semimax` sigue la propuesta abierta de #22.', '']
    base = ok[(ok['estado_TS'] == 'concordante') & ok['S1_toca_fov'].isna()]
    filas = []
    for pol in ('ocupado_2500', 'ocupado_semimax'):
        for modo in ('default6mm', 'robust3mm'):
            a = base[(base['politica_metal'] == 'hueso') & (base['modo'] == modo) & (base['F_limpieza'] == 0.0)]
            b = base[(base['politica_metal'] == pol) & (base['modo'] == modo) & (base['F_limpieza'] == 0.0)]
            m = a.set_index('Caso')[['D_TS_max_mm', 'Grupo']].join(b.set_index('Caso')['D_TS_max_mm'], rsuffix='_ocup',
                                                                    how='inner')
            for grupo, s in m.groupby('Grupo'):
                dif = s['D_TS_max_mm'] - s['D_TS_max_mm_ocup']
                filas.append({'politica': pol, 'modo': modo, 'Grupo': grupo, 'n': len(s),
                              'casos_con_cambio': int((dif.abs() > 0).sum()),
                              'dif_mediana_mm': round(float(dif.median()), 2), 'dif_max_mm': round(float(dif.max()), 1),
                              'viable_10mm_se_pierde': int(((s['D_TS_max_mm'] >= 10) & (s['D_TS_max_mm_ocup'] < 10)).sum())})
    L += [md(pd.DataFrame(filas), index=False) if filas else '(sin casos con metal en el recorte)', '']

    b0 = hueso[(hueso['modo'] == args.modo_principal) & (hueso['F_limpieza'] == 0.0)]
    dens = b0.groupby('Grupo').agg(
        n=('Caso', 'count'), hu_p50_eje=('hu_p50_eje', 'median'), frac_bajo150_eje=('frac_bajo150_eje', 'median'),
        casos_eje_a_2mm_de_metal=('frac_eje_metal_r2mm', lambda x: int((x > 0).sum())),
        casos_cilindro_toca_metal=('cilindro_toca_metal', lambda x: int(verdad(x).sum()))).round(3)
    L += [f'## 5. Densidad en el eje del mejor corredor y metal existente ({args.modo_principal}, F = 0, implante como '
          'hueso, todos)', '',
          'Grupos no emparejados; sin contraste causal con/sin metal (decision 2026-09-14). '
          '`casos_cilindro_toca_metal`: el cilindro de diametro D_TS alcanza voxeles > 2500 HU (#52).', '', md(dens), '']

    if args.e10_dir is not None and (args.e10_dir.expanduser() / 'ts_componentes_resumen.csv').exists():
        e10 = args.e10_dir.expanduser()
        r = pd.read_csv(e10 / 'ts_componentes_resumen.csv')
        c = pd.read_csv(e10 / 'ts_componentes.csv')
        L += ['## 6. E10: que quita cada F', '',
              f'- {r["Caso"].nunique()} casos; estructuras con mas de un componente: '
              f'{int((r["n_comp"] > 1).sum())} de {len(r)}.', '']
        filas = []
        no_mayor = c[c['rango'] > 1]
        for f in FRACCIONES[1:]:
            quita = no_mayor[no_mayor['frac_estructura'] < f]
            filas.append({'F': f,
                          'estructuras_afectadas (comp >= 10 vox)': quita.groupby(['Caso', 'modo', 'estructura']).ngroups,
                          'mayor_componente_quitado_ml': round(float(quita['vol_ml'].max()), 2) if len(quita) else 0.0,
                          'mayor_distancia_quitada_mm': round(float(quita['dist_caja_mayor_mm'].max()), 1) if len(quita) else 0.0})
        L += [md(pd.DataFrame(filas), index=False), '']
        grandes = no_mayor[no_mayor['frac_estructura'] >= 0.01].sort_values('frac_estructura', ascending=False)
        L += [f'Componentes no principales con >= 1% de su estructura (una F >= su fraccion los borraria; '
              f'posibles fragmentos de fractura o errores grandes, revisar en lamina): {len(grandes)}', '',
              md(grandes.head(40), index=False) if len(grandes) else '(ninguno)', '']
    else:
        L += ['## 6. E10', '', 'Sin `ts_componentes_resumen.csv`: E10 no termino o no se paso `--e10-dir`.', '']

    (e9_dir / 'e9ts_resumen.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
