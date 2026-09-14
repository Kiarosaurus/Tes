"""Analisis de la QC de TotalSegmentator sobre la cohorte (#48, #49, #50). Solo lee CSV.

POR QUE
-------
`ts_qc.py` (job 51316) dejo tablas por volumen sin interpretar (`ts_cohorte.md`). Este script
las cuenta **por paciente** (sin los 11 de `exclusiones.csv`) y las cruza con R1 (revisor
clinico y agente) y con E9b. **No decide nada**: alimenta las decisiones de la autora.

QUE MIDE
--------
1. Nivel de S1: `techo_linea_media_dz_mm` de `vertebrae_S1` (techo de la mascara de TS en la
   columna media del platillo de R1, menos el platillo). Estado por caso: `R1 arriba de TS` si
   dz < UMBRAL_NIVEL_MM con los dos recortes; `sin techo` si la columna no toca la mascara.
   El umbral se fijo **mirando esta misma distribucion** (hueco entre -12.7 y +3.1 mm): es
   descriptivo, no validado. La concordancia con el clinico se da tambien como rango de umbrales
   que la dejan igual, para no depender de el.
2. Por que `sacrum` no tiene techo en casos con S1 hallado (pendiente de `ts_cohorte.md`).
3. Efecto del recorte (3 mm vs 6 mm) por estructura y grupo con/sin osteosintesis (#49).
4. Tabla de #50 rehecha: esferas de E9b frente a mascaras de TS y estado de nivel.
5. Fraccion <= 150 HU dentro de las mascaras por grupo (#48).
6. FOV frente a los 7 de FOV cortado de R1.
7. Tornillos de E8 frente a las mascaras (por recorte).

Escribe `ts_analisis.md` (tablas) y `ts_nivel_s1.csv` (un caso por fila), versionables.

USO
---
    python ts_analisis.py [--qc-dir outputs/ts_total_qc]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

UMBRAL_NIVEL_MM = -10.0
MODOS = ['robust3mm', 'default6mm']
ESFERAS = ['cuerpo', 'ala_izq', 'ala_der']


def md(df: pd.DataFrame, index: bool = True) -> str:
    """DataFrame a tabla Markdown sin dependencias extra."""
    d = df.reset_index() if index else df
    filas = ['| ' + ' | '.join(map(str, d.columns)) + ' |', '|' + '---|' * len(d.columns)]
    filas += ['| ' + ' | '.join('' if pd.isna(v) else str(v) for v in r) + ' |' for r in d.itertuples(index=False)]
    return '\n'.join(filas)


def estrato(e: pd.Series) -> str:
    """Grupo de referencia de nivel: clinico en evaluacion, discordancia de R1 en el resto."""
    if e['cohorte'] == 'evaluacion':
        return f"evaluacion, clinico {e['auditoria_S1_clinico']}"
    return f"{e['cohorte']}, {'discordante' if e['s1_discordante'] else 'no discordante'}"


def main() -> None:
    """Calcula las tablas y las escribe."""
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--qc-dir', type=Path, default=here / 'outputs' / 'ts_total_qc')
    args = parser.parse_args()

    q = pd.read_csv(args.qc_dir / 'ts_qc.csv')
    s = pd.read_csv(args.qc_dir / 'ts_qc_esferas.csv')
    t = pd.read_csv(args.qc_dir / 'ts_qc_tornillos.csv')
    excl = pd.read_csv(here.parent / 'exploration-3d' / 'exclusiones.csv', encoding='utf-8-sig')
    grupos = pd.read_csv(here.parent / 'exploration-3d' / 'grupos.csv', encoding='utf-8-sig').set_index('Caso')
    est = pd.read_csv(here / 'r1_estados.csv').set_index('Caso')
    e9b = pd.read_csv(here / 'e9b_densidad_s1.csv').set_index('Caso')

    casos = sorted(set(q['Caso']) - set(excl['Caso']))
    q, s, t = (d[d['Caso'].isin(casos)].copy() for d in (q, s, t))
    L = ['# TS cohorte — analisis de la QC (generado por `ts_analisis.py`)', '',
         f'Volumenes en uso: {len(casos)} (sin los {excl["Caso"].nunique()} de `exclusiones.csv`); '
         f'pacientes: {grupos.loc[casos, "Grupo paciente"].nunique()}. '
         'Procedencia de la referencia de nivel: `auditoria_S1_clinico` = medico ORL; '
         '`auditoria_S1` = agente. **No decide nada.**', '']

    # 1. Nivel de S1.
    v = q[q['estructura'] == 'vertebrae_S1']
    dz = v.pivot(index='Caso', columns='modo', values='techo_linea_media_dz_mm')[MODOS]
    nv = v.pivot(index='Caso', columns='modo', values='n_vox')[MODOS]
    fov = v.pivot(index='Caso', columns='modo', values='toca_fov')[MODOS]
    niv = pd.DataFrame(index=casos)
    niv['Dataset'] = est.loc[casos, 'Dataset']
    niv['Grupo'] = grupos.loc[casos, 'Grupo']
    niv['cohorte'] = est.loc[casos, 'cohorte']
    niv['S1_hallado_R1'] = est.loc[casos, 'S1_hallado']
    niv['auditoria_S1_clinico'] = est.loc[casos, 'auditoria_S1_clinico']
    niv['auditoria_S1_agente'] = est.loc[casos, 'auditoria_S1']
    niv['s1_discordante'] = est.loc[casos, 's1_discordante']
    niv['dz_S1_3mm'] = dz['robust3mm']
    niv['dz_S1_6mm'] = dz['default6mm']
    niv['n_vox_S1_3mm'] = nv['robust3mm']
    niv['S1_toca_fov'] = fov['robust3mm'].fillna('')
    bajo = (dz < UMBRAL_NIVEL_MM).all(axis=1)
    niv['estado_TS'] = np.where(niv['S1_hallado_R1'] != 'si', 'sin S1 en R1',
                                np.where(dz.isna().any(axis=1), 'sin techo',
                                         np.where(bajo, 'R1 arriba de TS', 'concordante')))
    niv['estrato'] = [estrato(est.loc[c]) for c in casos]
    niv.index.name = 'Caso'
    niv.to_csv(here / 'ts_nivel_s1.csv')

    L += ['## 1. Nivel de S1: techo de `vertebrae_S1` de TS frente al platillo de R1', '',
          f'Estado `R1 arriba de TS`: dz < {UMBRAL_NIVEL_MM:g} mm con los dos recortes. '
          f'Diferencia maxima de dz entre recortes: {float((dz["robust3mm"] - dz["default6mm"]).abs().max()):.1f} mm; '
          f'casos cuyo estado cambia con el recorte: '
          f'{int(((dz["robust3mm"] < UMBRAL_NIVEL_MM) != (dz["default6mm"] < UMBRAL_NIVEL_MM)).sum())}.', '']
    tab = pd.crosstab(niv['estrato'], niv['estado_TS'], margins=True, margins_name='total')
    L += [md(tab), '']
    agg = niv.groupby(['estrato', 'estado_TS'])['dz_S1_3mm'].agg(['count', 'median', 'min', 'max']).round(1)
    L += ['dz (3 mm) por estrato y estado:', '', md(agg), '']
    ref = niv[niv['auditoria_S1_clinico'].isin(['ok', '+1']) & niv['dz_S1_3mm'].notna()]
    ok_dz = ref.loc[ref['auditoria_S1_clinico'] == 'ok', ['dz_S1_3mm', 'dz_S1_6mm']].min(axis=1)
    p1_dz = ref.loc[ref['auditoria_S1_clinico'] == '+1', ['dz_S1_3mm', 'dz_S1_6mm']].max(axis=1)
    conc = int(((ref['auditoria_S1_clinico'] == 'ok') != (ref.index.isin(niv.index[bajo]))).sum())
    separados = p1_dz.max() < ok_dz.min()
    L += [f'Concordancia con el clinico (ok / +1, con techo en los dos recortes): **{conc} de {len(ref)}**. '
          f'`+1`: dz (peor recorte) entre {p1_dz.min():.1f} y {p1_dz.max():.1f} mm. `ok`: dz (peor recorte) entre '
          f'{ok_dz.min():.1f} y {ok_dz.max():.1f} mm. '
          + (f'Los dos rangos no se solapan: cualquier umbral mayor que {p1_dz.max():.1f} y de hasta '
             f'{ok_dz.min():.1f} mm da la misma concordancia.' if separados else
             'Los rangos se solapan: la concordancia depende del umbral elegido.'), '']
    disc = niv[(niv['auditoria_S1_clinico'].isin(['ok', '+1', 'otro']))
               & ~(((niv['auditoria_S1_clinico'] == 'ok') & (niv['estado_TS'] == 'concordante'))
                   | ((niv['auditoria_S1_clinico'] == '+1') & (niv['estado_TS'] == 'R1 arriba de TS')))]
    L += ['Casos de evaluacion donde TS no coincide con el clinico, o clinico `otro`:', '',
          md(disc[['auditoria_S1_clinico', 'auditoria_S1_agente', 'dz_S1_3mm', 'dz_S1_6mm', 'n_vox_S1_3mm',
                   'S1_toca_fov', 'estado_TS']]), '']
    otros = niv[(niv['cohorte'] != 'evaluacion') & (niv['estado_TS'] == 'R1 arriba de TS')]
    L += [f'Fuera de evaluacion (sin auditoria), `R1 arriba de TS`: {len(otros)} casos: '
          + ', '.join(f'`{c.replace("_data", "").replace("dataset6_CLINIC_", "C").replace("dataset7_CLINIC_metal_", "m")}` '
                      f'({r.dz_S1_3mm:.0f})' for c, r in otros.sort_values('dz_S1_3mm').iterrows()), '']

    # 2. Techo de sacrum vacio con S1 hallado.
    sac = q[(q['estructura'] == 'sacrum') & q['techo_linea_media_dz_mm'].isna()].copy()
    sac = sac[sac['Caso'].map(est['S1_hallado']) == 'si']
    sac['estado_TS'] = sac['Caso'].map(niv['estado_TS'])
    sac['clinico'] = sac['Caso'].map(niv['auditoria_S1_clinico'])
    expl = sac['estado_TS'].isin(['R1 arriba de TS']) | (sac['clinico'] == '+1')
    L += ['## 2. `sacrum` sin techo con S1 hallado en R1', '',
          f'{len(sac)} filas, {sac["Caso"].nunique()} casos. De ellos, '
          f'{sac.loc[expl, "Caso"].nunique()} casos ({int(expl.sum())} filas) son casos con R1 un nivel arriba '
          '(por TS o por el clinico): la columna media cae sobre L5, anterior al sacro. '
          f'Sin esa explicacion: {sac.loc[~expl, "Caso"].nunique()} casos ({int((~expl).sum())} filas).', '',
          md(sac.loc[~expl, ['Caso', 'modo', 'n_vox', 'estado_TS']], index=False), '']

    # 3. Recorte.
    d3 = q[q['modo'] == 'robust3mm'].set_index(['Caso', 'estructura'])
    d6 = q[q['modo'] == 'default6mm'].set_index(['Caso', 'estructura'])
    rec = d3[['dice_3v6', 'dif_caja_3v6_max_mm']].copy()
    rec['excl_3mm_%'] = 100 * d3['solo_este_modo_vox'] / d3['n_vox'].replace(0, np.nan)
    rec['excl_6mm_%'] = 100 * d6['solo_este_modo_vox'] / d6['n_vox'].replace(0, np.nan)
    rec['grupo'] = np.where(rec.index.get_level_values('Caso').map(grupos['Grupo']) == 'grupo 1',
                            'con osteosintesis (g1)', 'sin osteosintesis (g2+g3)')
    tr = rec.groupby([rec.index.get_level_values('estructura'), 'grupo']).agg(
        n=('dice_3v6', 'count'), dice_p50=('dice_3v6', 'median'), dice_p05=('dice_3v6', lambda x: x.quantile(.05)),
        dice_min=('dice_3v6', 'min'), excl3_p50=('excl_3mm_%', 'median'), excl6_p50=('excl_6mm_%', 'median'),
        caja_max_mm=('dif_caja_3v6_max_mm', 'max')).round(3)
    L += ['## 3. Recorte 3 mm frente a 6 mm (#49)', '', md(tr), '',
          'Peores Dice:', '', md(rec.nsmallest(6, 'dice_3v6').round(3)), '']
    frag = q[q['dif_caja_3v6_max_mm'] > 10].pivot_table(
        index=['Caso', 'estructura'], columns='modo', values=['x_min_mm', 'x_max_mm', 'z_min_mm', 'z_max_mm'])
    frag.columns = [f'{a}_{b}' for a, b in frag.columns]
    frag['dif_caja_mm'] = q[q['dif_caja_3v6_max_mm'] > 10].groupby(['Caso', 'estructura'])['dif_caja_3v6_max_mm'].first()
    L += [f'Cajas que cambian > 10 mm entre recortes (en el piloto, <= 1.6 mm; causa no verificada: islas de '
          f'voxeles o extension distinta de la estructura): {frag.index.get_level_values("Caso").nunique()} '
          f'casos, {len(frag)} estructuras.', '', md(frag.round(1)), '']

    # 4. Tabla de #50 rehecha.
    ss = s[s['modo'] == 'robust3mm'].set_index(['Caso', 'esfera'])
    ev = est[est['cohorte'] == 'evaluacion']

    def fila(nombre: str, cs: list[str]) -> dict:
        cs = [c for c in cs if c in e9b.index and c in niv.index]
        n = len(cs)
        alguna = sum(bool((e9b.loc[c, [f'hu_{k}' for k in ESFERAS]] < 150).any()) for c in cs)

        def ala(c: str, cond) -> bool:
            return any(e9b.loc[c, f'hu_{a}'] < 150 and (c, a) in ss.index and cond(ss.loc[(c, a)])
                       for a in ('ala_izq', 'ala_der'))
        dentro = sum(ala(c, lambda r: r['frac_en_sacro_S1'] >= 0.9) for c in cs)
        fuera = sum(ala(c, lambda r: r['frac_fuera_mascaras'] > 0.5) for c in cs)
        pct = (lambda k: f'{k} ({100 * k / n:.0f}%)') if n else str
        return {'grupo': nombre, 'n': n, 'alguna esfera < 150 HU (E9b)': pct(alguna),
                'ala < 150 con esfera >= 90% en sacrum/S1 de TS': pct(dentro),
                'ala < 150 con esfera > 50% fuera de mascaras': pct(fuera)}
    conc_c = set(niv.index[niv['estado_TS'] == 'concordante'])
    arriba = set(niv.index[niv['estado_TS'] == 'R1 arriba de TS'])
    ok = list(ev.index[ev['auditoria_S1_clinico'] == 'ok'])
    cal = list(e9b.index[e9b['cohorte'] == 'calibracion'])
    t50 = pd.DataFrame([
        fila('evaluacion, clinico ok (E9b de #48)', ok),
        fila('  ... y TS concordante', [c for c in ok if c in conc_c]),
        fila('  ... y TS: R1 arriba', [c for c in ok if c in arriba]),
        fila('evaluacion, clinico +1', list(ev.index[ev['auditoria_S1_clinico'] == '+1'])),
        fila('calibracion, sin auditar (E9b de #48)', cal),
        fila('  ... y TS concordante', [c for c in cal if c in conc_c]),
        fila('  ... y TS: R1 arriba', [c for c in cal if c in arriba]),
    ])
    L += ['## 4. Tabla de #50 rehecha con TS (esferas de E9b, recorte 3 mm)', '',
          'Una esfera con mediana < 150 HU cuenta como "hueso bajo 150" solo si queda >= 90% dentro de '
          '`sacrum` o `vertebrae_S1`. Con 6 mm las fracciones cambian poco (ver `ts_qc_esferas.csv`).', '',
          md(t50, index=False), '']
    s2 = s[s['modo'] == 'robust3mm'].copy()
    s2['estado_TS'] = s2['Caso'].map(niv['estado_TS'])
    s2 = s2[s2['estado_TS'].isin(['concordante', 'R1 arriba de TS'])]
    te = s2.groupby(['estado_TS', 'esfera']).agg(
        n=('Caso', 'count'), en_sacro_S1_p50=('frac_en_sacro_S1', 'median'),
        fuera_p50=('frac_fuera_mascaras', 'median'), fuera_mayoria=('frac_fuera_mascaras', lambda x: int((x > .5).sum())),
        en_cadera_max=('frac_en_cadera', 'max')).round(3)
    L += ['Esferas por estado de nivel (todas las cohortes con S1 en R1):', '', md(te), '']

    # 5. Fraccion <= 150 HU dentro de mascaras.
    fb = q.assign(grupo=q['Caso'].map(grupos['Grupo'])).pivot_table(
        index=['estructura', 'modo'], columns='grupo', values='frac_bajo150', aggfunc='median').round(3)
    L += ['## 5. Fraccion de voxeles <= 150 HU dentro de cada mascara (mediana por grupo) (#48)', '',
          'Grupos de `grupos.csv`: 1 = osteosintesis, 2 = objeto no ortopedico, 3 = limpio. Incluye borde de '
          'la mascara (volumen parcial) y, en grupo 1, voxeles de metal y estriacion. Los grupos no estan '
          'emparejados por edad ni sexo.', '',
          md(fb), '']

    # 6. FOV.
    f = q[q['toca_fov'].notna()]
    ftab = (f.assign(cara=f['estructura'] + ' ' + f['toca_fov']).groupby('Caso')['cara']
            .agg(lambda x: ', '.join(sorted(set(x)))).to_frame('estructuras (ambos recortes)'))
    fov7 = ev.index[(ev['cresta_der_estado'] == 'fuera de FOV') | (ev['cresta_izq_estado'] == 'fuera de FOV')]
    ftab['de los 7 (R1)'] = ftab.index.isin(fov7)
    ftab['Grupo'] = ftab.index.map(grupos['Grupo'])
    L += ['## 6. Mascaras que tocan el borde del FOV', '',
          f'{len(ftab)} volumenes en uso. Los 7 de FOV cortado de R1 estan todos: '
          f'{int(ftab["de los 7 (R1)"].sum())} de {len(fov7)}.', '', md(ftab), '']

    # 7. Tornillos.
    tt = t.pivot_table(index=['Caso', 'comp'], columns='modo',
                       values=['frac_eje_fuera', 'frac_metal_en_mascaras', 'frac_vol_E8_en_cilindro'])
    tt.columns = [f'{a}_{b}' for a, b in tt.columns]
    res = t.groupby('modo')[['frac_eje_fuera', 'frac_metal_en_mascaras']].agg(['median', 'max', 'min']).round(3)
    res.columns = [f'{a}_{b}' for a, b in res.columns]
    L += ['## 7. Tornillos de E8 frente a las mascaras', '',
          f'{t["Caso"].nunique()} pacientes, {len(tt)} componentes (sin `metal_0065`, secundario).', '',
          md(res), '', md(tt.round(3)), '']

    (here / 'ts_analisis.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
