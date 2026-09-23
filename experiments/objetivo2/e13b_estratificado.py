"""E13b — Wasserstein-1 estratificado por viabilidad del corredor. Analisis POST HOC declarado.

ESTO NO ESTABA PREINSCRITO, Y ESO SE DECLARA
--------------------------------------------
`preinscripcion_muestreador.md` fija un unico analisis: la distribucion de grados sobre toda la cohorte
y su Wasserstein-1 contra las dos series de `zwingmann2009navigated`. Esa sigue siendo **la cifra
principal**, y esta en `e13_sap.md`.

Esta estratificacion se decidio **despues** de ver la corrida 52175, al descubrir que en 15 de 72 casos
el corredor medido es mas estrecho que el tornillo del benchmark, de modo que su eje ideal ya perfora
(#122). Es, por tanto, **exploratoria**: sirve para separar cuanto del desajuste aporta la anatomia de
la cohorte receptora y cuanto el muestreador, no para sustituir el resultado preinscrito. Se reporta
como analisis secundario y asi debe citarse.

Que NO se hace, y por que: **no se restringe la cohorte a los corredores viables**. Seleccionar
pacientes por una variable correlacionada con el resultado subiria el porcentaje de grado 0 y bajaria
el W1 frente al brazo navegado; es el mismo sesgo que D-O2.1 y #120 existen para impedir, y
`zwingmann2009navigated` tampoco excluyo a sus pacientes de anatomia estrecha.

No necesita mascaras ni Khipu: parte de `e13_poses*.csv` y de `e9ts_corredor.csv`, ambos en el repositorio.

USO
---
    python e13b_estratificado.py            # escribe e13b_estratificado.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

_RAIZ = Path(__file__).resolve().parents[2]
_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_RAIZ / 'src' / 'muestreador'))

import sap  # noqa: E402

CORRIDAS = (('Cohorte primaria (72 casos)', 'e13_poses.csv'),
            ('Sensibilidad, grupo 3 (49 casos)', 'e13_poses_g3.csv'))


def corredores(refs_dir: Path) -> pd.Series:
    """`D_TS_max_mm` por caso, de la misma fila de E9-TS que usa el muestreador."""
    e9 = pd.read_csv(refs_dir / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0) & (e9.politica_metal == 'hueso')]
    return e9.drop_duplicates('Caso').set_index('Caso').D_TS_max_mm


def bloque(titulo: str, poses: pd.DataFrame, d_ts: pd.Series, diametro: float) -> list[str]:
    d = poses[poses.d_mm == diametro].copy()
    d['D_TS'] = d.Caso.map(d_ts)
    if d.D_TS.isna().any():
        raise RuntimeError(f'{titulo}: {int(d.D_TS.isna().sum())} poses sin D_TS_max')
    d['viable'] = d.D_TS >= diametro
    L = [f'### {titulo}', '',
         f'- Casos: **{d.Caso.nunique()}**; con `D_TS_max` $\\geq$ {diametro} mm: '
         f'**{d[d.viable].Caso.nunique()}**; mas estrechos: **{d[~d.viable].Caso.nunique()}**.', '',
         '| estrato | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |',
         '|---|---|---|---|---|---|---|---|']
    for etiqueta, sub in (('**todos** (preinscrito)', d),
                          (f'corredor $\\geq$ {diametro} mm', d[d.viable]),
                          (f'corredor $<$ {diametro} mm', d[~d.viable])):
        if not len(sub):
            continue
        dist = sap.distribucion_grados(list(sub.grado))
        wn = sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['navegado'])
        wc = sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['convencional'])
        L += [f'| {etiqueta} | {len(sub)} | {dist[0]:.1f} | {dist[1]:.1f} | {dist[2]:.1f} | '
              f'{dist[3]:.1f} | {wn:.3f} | {wc:.3f} |']
    return L + ['']


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refs-dir', type=Path, default=_AQUI)
    parser.add_argument('--diametro', type=float, default=sap.D_SAP_MM)
    parser.add_argument('--out', type=Path, default=_AQUI / 'e13b_estratificado.md')
    args = parser.parse_args()

    d_ts = corredores(args.refs_dir)
    L = ['# E13b — Wasserstein-1 estratificado por viabilidad del corredor', '',
         '> **Analisis POST HOC declarado.** No estaba en `preinscripcion_muestreador.md`. Se decidio '
         'despues de ver la corrida 52175 y el hallazgo de #122. La cifra principal del Objetivo 2 '
         'sigue siendo la de `e13_sap.md`, calculada sobre toda la cohorte.', '',
         f'Calibre: **{args.diametro} mm**, el del benchmark (D-O2.4). Un caso se considera de corredor '
         f'viable cuando su `D_TS_max` alcanza ese calibre; por debajo, el eje ideal del corredor ya '
         'perfora y el grado 0 es inalcanzable por anatomia.', '']
    for titulo, fichero in CORRIDAS:
        ruta = args.refs_dir / fichero
        if not ruta.exists():
            L += [f'### {titulo}', '', f'`{fichero}` no esta en disco. Saltado.', '']
            continue
        L += bloque(titulo, pd.read_csv(ruta), d_ts, args.diametro)

    L += ['## Lectura', '',
          'La cifra agregada es una **mezcla de dos poblaciones distintas**. En los corredores que '
          'admiten el calibre del benchmark, la distribucion del muestreador queda cerca del brazo '
          'navegado; en los corredores estrechos, practicamente ninguna pose alcanza el grado 0, y no '
          'porque el muestreador las desvie, sino porque el eje optimo de esos pacientes ya perfora. '
          'Por eso el W1 agregado frente al brazo navegado **no debe leerse como una medida limpia del '
          'muestreador**: parte de esa distancia es del emparejamiento entre la cohorte receptora y la '
          'cohorte clinica de referencia.', '',
          'La estratificacion **no se usa para elegir cohorte**. Los dos estratos se reportan juntos, y '
          'la cifra que se defiende es la preinscrita sobre la cohorte completa.', '']
    args.out.write_text('\n'.join(L), encoding='utf-8')
    print(f'escrito {args.out.name}')


if __name__ == '__main__':
    main()
