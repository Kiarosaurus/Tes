"""Coherencia cruzada del Objetivo 2: codigo, preinscripcion, controles y `main.tex` dicen lo mismo.

POR QUE
-------
Las cifras del Objetivo 2 viven en cuatro sitios a la vez: constantes de `src/muestreador/`, tablas de
`preinscripcion_muestreador.md`, salidas de E12/E13 y prosa de `tesis/main.tex`. Un cambio en uno y no
en los otros no rompe nada visible: simplemente hace que la tesis afirme algo que el codigo no hace.
Este script falla cuando eso pasa.

USO
---
    python verificar_coherencia.py      # codigo de salida != 0 si alguna comprobacion falla
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

_RAIZ = Path(__file__).resolve().parents[2]
_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_RAIZ / 'src' / 'muestreador'))

import muestreo  # noqa: E402
import sap  # noqa: E402

_ok: list[bool] = []


def chk(nombre: str, cond: bool, detalle: str = '') -> None:
    _ok.append(bool(cond))
    print(('  OK  ' if cond else ' FALLA') + f' {nombre} {detalle}')


def main() -> int:
    print('--- coherencia del Objetivo 2 ---')

    e9 = pd.read_csv(_AQUI / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
    qc = e9[(e9.estado_TS == 'concordante') & (e9.S1_toca_fov.isna())]
    n72 = qc[qc.Grupo.isin(['grupo 2', 'grupo 3'])].Caso.nunique()
    n49 = qc[qc.Grupo == 'grupo 3'].Caso.nunique()
    chk('cohorte primaria = 72 (D-O2.2)', n72 == 72, f'({n72})')
    chk('cohorte de sensibilidad = 49', n49 == 49, f'({n49})')
    chk('los casos de FOV cortado son solo de grupo 1 (#119)',
        e9[e9.fov7.astype(str) == 'True'].Grupo.unique().tolist() == ['grupo 1'])

    chk('D_SAP_MM = 7.0 (D-O2.4, #118)', sap.D_SAP_MM == 7.0)
    chk('limites de grado = los de main.tex', sap.LIMITES_GRADO == (2.0, 4.0))
    chk('Zwingmann navegado 69/15/8/8', list(sap.ZWINGMANN['navegado']) == [69., 15., 8., 8.])
    chk('Zwingmann convencional 40/37/11.5/11.5',
        list(sap.ZWINGMANN['convencional']) == [40., 37., 11.5, 11.5])
    chk('holgura de Kaiser = 5 mm', muestreo.HOLGURA_KAISER_MM == 5.0)
    chk('sigma_t = 2.5 mm', abs(muestreo.HOLGURA_KAISER_MM / muestreo.FACTOR_SIGMA - 2.5) < 1e-9)
    sa = np.degrees(muestreo.sigma_angular_rad(138.0))
    chk('sigma_a con L = 138 mm ~ 2.07 grados', abs(sa - 2.07) < 0.01, f'({sa:.3f})')

    for v, g in ((0.0, 0), (1.999, 1), (2.0, 2), (4.0, 2), (4.001, 3)):
        chk(f'grado({v}) = {g}', sap.grado(v) == g)
    chk('W1 de una distribucion consigo misma = 0',
        sap.wasserstein1_ordinal(sap.ZWINGMANN['navegado'], sap.ZWINGMANN['navegado']) == 0)
    chk('W1 maximo = 3',
        sap.wasserstein1_ordinal(np.array([1., 0, 0, 0]), np.array([0, 0, 0, 1.])) == 3.0)

    piloto = _AQUI / 'e13_poses_piloto.csv'
    if piloto.exists():
        d = pd.read_csv(piloto)
        chk('ninguna pose sin grado (#120 opcion b)', d.grado.isna().sum() == 0)
        g7 = d[d.d_mm == sap.D_SAP_MM]
        tope = muestreo.TRUNCAMIENTO_SIGMA * muestreo.HOLGURA_KAISER_MM / muestreo.FACTOR_SIGMA
        chk(f'desvio del centro dentro del truncamiento ({tope} mm)',
            g7.desvio_centro_mm.max() <= tope, f'(max {g7.desvio_centro_mm.max()})')
        chk('la fraccion de grado 0 decrece al ensanchar el cilindro',
            (d[d.d_mm == 4.91].grado == 0).mean() >= (d[d.d_mm == 7.0].grado == 0).mean()
            >= (d[d.d_mm == 7.3].grado == 0).mean())

    chk('la semilla por caso es reproducible',
        np.array_equal(muestreo.rng_de_caso('x').normal(size=4),
                       muestreo.rng_de_caso('x').normal(size=4)))
    chk('casos distintos reciben poses distintas',
        not np.array_equal(muestreo.rng_de_caso('x').normal(size=4),
                           muestreo.rng_de_caso('y').normal(size=4)))

    e13 = (_AQUI / 'e13_muestreo_sap.py').read_text(encoding='utf-8')
    chk('el control de pose sin perturbar usa D_TS_max, no el calibre de SAP (#122)',
        'evaluar_pose(hueso, zoom, origen, c, u0, largo, d_ts, sdf=sdf)' in e13)
    chk('el resumen ya no afirma que se excluyen casos (#122)',
        'sus cifras no se usan):' not in e13)

    pre = (_AQUI / 'preinscripcion_muestreador.md').read_text(encoding='utf-8')
    for s in ('72 casos', '49 casos', '7.0 mm', '2.5 mm', '2.07', '20260922', '0.083 mm'):
        chk(f'la preinscripcion menciona {s!r}', s in pre)

    tex = (_RAIZ / 'tesis' / 'main.tex').read_text(encoding='utf-8')
    for s in ('Three geometries', '7.0~mm cannulated screws', '0.083~mm',
              'graded~3 rather than discarded', 'Pre-registration of the placement sampler',
              'not used as a calibration objective', 'Distribution comparison'):
        chk(f'main.tex contiene {s!r}', s in tex)

    # --- las cifras que `main.tex` afirma tienen que salir de los CSV de la corrida ---
    d_ts = pd.read_csv(_AQUI / 'e9ts_corredor.csv')
    d_ts = d_ts[(d_ts.modo == 'default6mm') & (d_ts.F_limpieza == 0.0)
                & (d_ts.politica_metal == 'hueso')].drop_duplicates('Caso').set_index('Caso').D_TS_max_mm
    for fichero, esperado in (
            ('e13_poses.csv', dict(casos=72, n=3600, dist=[51.5, 31.4, 11.1, 6.0], wn=0.206, wc=0.230,
                                   estrechos=15, viables=57, n_via=2850, g0_via=64.2, wn_via=0.183,
                                   wc_via=0.482, g0_est=3.3, wn_est=1.122)),
            ('e13_poses_g3.csv', dict(casos=49, n=2450, dist=[54.9, 30.4, 9.9, 4.8], wn=0.186, wc=0.299,
                                      estrechos=8, viables=41, n_via=2050, g0_via=64.6, wn_via=0.175))):
        ruta = _AQUI / fichero
        if not ruta.exists():
            continue
        d = pd.read_csv(ruta)
        d = d[d.d_mm == sap.D_SAP_MM].copy()
        d['viable'] = d.Caso.map(d_ts) >= sap.D_SAP_MM
        e = esperado
        chk(f'{fichero}: {e["casos"]} casos', d.Caso.nunique() == e['casos'])
        chk(f'{fichero}: {e["n"]} poses', len(d) == e['n'])
        dist = sap.distribucion_grados(list(d.grado))
        chk(f'{fichero}: distribucion {e["dist"]}',
            all(abs(a_ - b_) < 0.05 for a_, b_ in zip(dist, e['dist'])),
            f'({[round(x, 1) for x in dist]})')
        chk(f'{fichero}: W1 navegado {e["wn"]}',
            abs(sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['navegado']) - e['wn']) < 5e-4)
        chk(f'{fichero}: W1 convencional {e["wc"]}',
            abs(sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['convencional']) - e['wc']) < 5e-4)
        chk(f'{fichero}: {e["estrechos"]} corredores estrechos',
            d[~d.viable].Caso.nunique() == e['estrechos'])
        chk(f'{fichero}: {e["viables"]} corredores viables', d[d.viable].Caso.nunique() == e['viables'])
        via = sap.distribucion_grados(list(d[d.viable].grado))
        chk(f'{fichero}: viables n={e["n_via"]}', int(d.viable.sum()) == e['n_via'])
        chk(f'{fichero}: viables g0 {e["g0_via"]}%', abs(via[0] - e['g0_via']) < 0.05, f'({via[0]:.1f})')
        chk(f'{fichero}: viables W1 navegado {e["wn_via"]}',
            abs(sap.wasserstein1_ordinal(via, sap.ZWINGMANN['navegado']) - e['wn_via']) < 5e-4)
        if 'wc_via' in e:
            chk(f'{fichero}: viables W1 convencional {e["wc_via"]}',
                abs(sap.wasserstein1_ordinal(via, sap.ZWINGMANN['convencional']) - e['wc_via']) < 5e-4)
        if 'g0_est' in e:
            est = sap.distribucion_grados(list(d[~d.viable].grado))
            chk(f'{fichero}: estrechos g0 {e["g0_est"]}%', abs(est[0] - e['g0_est']) < 0.05)
            chk(f'{fichero}: estrechos W1 navegado {e["wn_est"]}',
                abs(sap.wasserstein1_ordinal(est, sap.ZWINGMANN['navegado']) - e['wn_est']) < 5e-4)

    for s in ('51.5 / 31.4 / 11.1 / 6.0', '54.9 / 30.4 / 9.9 / 4.8', '0.206~grades', '0.230',
              '0.186 and 0.299', '64.2', '0.183~grades', '64.6', '0.175', '3.3', '1.122',
              '0.482', 'declared post-hoc', 'considered and rejected'):
        chk(f'main.tex declara {s!r}', s in tex)

    # --- lo que main.tex afirma del segundo corredor tiene que salir de la planilla (#121) ---
    rev = _AQUI / 'r2_nivel_pico_revisor.csv'
    if rev.exists():
        rv = pd.read_csv(rev)
        e9b = pd.read_csv(_AQUI / 'e9ts_corredor.csv')
        e9b = e9b[(e9b.modo == 'default6mm') & (e9b.F_limpieza == 0.0)
                  & (e9b.politica_metal == 'hueso')].drop_duplicates('Caso').set_index('Caso')
        rv['z'] = [e9b.loc[c, 'pico_inf_z_rel_mm'] for c in rv.Caso]
        rv['D'] = [e9b.loc[c, 'pico_inf_D_mm'] for c in rv.Caso]
        cuenta = rv.nivel_del_punto.value_counts().to_dict()
        chk('segundo corredor: 18 casos juzgados', len(rv) == 18)
        chk('segundo corredor: S2 13 / S3 4 / S4 1',
            (cuenta.get('S2'), cuenta.get('S3'), cuenta.get('S4')) == (13, 4, 1), str(cuenta))
        for niv, prof, diam in (('S2', 30.0, 8.8), ('S3', 40.5, 7.4), ('S4', 51.0, 3.8)):
            s = rv[rv.nivel_del_punto == niv]
            chk(f'{niv}: profundidad mediana {prof} mm', abs(-s.z.median() - prof) < 0.05,
                f'({-s.z.median()})')
            chk(f'{niv}: diametro mediano {diam} mm', abs(s.D.median() - diam) < 0.05,
                f'({s.D.median()})')
        chk('la inversion existe: un S2 a 39 mm y algun S3 a 36 o 33 mm',
            (-rv[rv.nivel_del_punto == 'S2'].z.min() == 39.0)
            and set([-x for x in rv[rv.nivel_del_punto == 'S3'].z]) >= {36.0, 33.0})
        for s in ('at S2 in', 'at S3 in 4 and at S4 in 1', '30, 40.5 and 51~mm',
                  '8.8, 7.4 and 3.8~mm', 'second corridor below S1', 'not as S2',
                  'rather than verified as free of fracture'):
            chk(f'main.tex declara {s!r}', s in tex)

    e12 = _AQUI / 'e12_sap_control.md'
    if e12.exists():
        txt = e12.read_text(encoding='utf-8')
        chk('E12 declara la resolucion de 0.083 mm', '0.083 mm' in txt)
        chk('E12: C6 da diferencia 0.0 en todos los casos', txt.count('diferencia **0.0 mm**') >= 1)
        chk('E12: ningun barrido deja poses sin grado',
            'Poses sin grado en el barrido: **0**' in txt
            and 'Poses sin grado en el barrido: **1' not in txt)

    print(f'\n{sum(_ok)}/{len(_ok)} comprobaciones pasan')
    return 0 if all(_ok) else 1


if __name__ == '__main__':
    raise SystemExit(main())
