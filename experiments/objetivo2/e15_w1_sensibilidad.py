"""E15 — intervalo por remuestreo de pacientes del Wasserstein-1 y sensibilidad sin los dos casos con error de
segmentacion (`01-decisiones.md` 2026-10-08 ptos 18 y 22). POSTERIOR y descriptivo: no cambia ninguna cifra de E13.

Lee `e13_poses.csv` (cohorte primaria, 72 casos x 50 poses x 3 diametros) y, al diametro de SAP (7.0 mm):
- W1 contra las dos series de `zwingmann2009navigated`, regresion exacta contra `e13_sap.md`;
- intervalo del 95 % por remuestreo de pacientes (percentiles; `--n-remuestreos`, semilla fija): se remuestrean
  casos con reemplazo y se juntan todas sus poses;
- la misma cifra sin `CLINIC_0022` y `CLINIC_0024`.

USO
---
    python experiments/objetivo2/e15_w1_sensibilidad.py
Escribe `e15_w1_sensibilidad.md` junto al script.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI.parents[1] / 'src' / 'muestreador'))
import sap  # noqa: E402

EXCLUIR = ('dataset6_CLINIC_0022_data', 'dataset6_CLINIC_0024_data')


def w1(grados: np.ndarray) -> tuple[np.ndarray, float, float]:
    dist = sap.distribucion_grados(list(grados), no_evaluables='error')
    return (np.asarray(dist), sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['navegado']),
            sap.wasserstein1_ordinal(dist, sap.ZWINGMANN['convencional']))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--poses', type=Path, default=_AQUI / 'e13_poses.csv')
    ap.add_argument('--n-remuestreos', type=int, default=2000)
    ap.add_argument('--semilla', type=int, default=20261015)
    ap.add_argument('--out', type=Path, default=_AQUI / 'e15_w1_sensibilidad.md')
    args = ap.parse_args()
    p = pd.read_csv(args.poses)
    p = p[p.d_mm == sap.D_SAP_MM]
    casos = sorted(p.Caso.unique())
    if len(casos) != 72:
        raise SystemExit('CONTROL: se esperaban 72 casos, hay %d' % len(casos))
    falt = [c for c in EXCLUIR if c not in casos]
    if falt:
        raise SystemExit('CONTROL: faltan en la cohorte %s' % falt)
    por_caso = {c: p.loc[p.Caso == c, 'grado'].to_numpy() for c in casos}

    dist, wn, wc = w1(p.grado.to_numpy())
    rng = np.random.default_rng(args.semilla)
    boot = []
    for _ in range(args.n_remuestreos):
        sel = rng.choice(len(casos), size=len(casos), replace=True)
        boot.append(w1(np.concatenate([por_caso[casos[i]] for i in sel]))[1:])
    boot = np.array(boot)
    q = np.percentile(boot, [2.5, 97.5], axis=0)
    sin = p[~p.Caso.isin(EXCLUIR)]
    dist_s, wn_s, wc_s = w1(sin.grado.to_numpy())

    L = ['# E15 — W1 por remuestreo de pacientes y sensibilidad sin CLINIC_0022 / 0024', '',
         'Generado por `e15_w1_sensibilidad.py` sobre `e13_poses.csv`, d = %.1f mm (SAP). POSTERIOR y descriptivo '
         '(`01-decisiones.md` 2026-10-08 ptos 18 y 22); no cambia ninguna cifra de E13.' % sap.D_SAP_MM, '',
         '| conjunto | casos | poses | % g0 / g1 / g2 / g3 | W1 navegado | W1 convencional |', '|---|---|---|---|---|---|',
         '| cohorte primaria (regresion de E13) | %d | %d | %.1f / %.1f / %.1f / %.1f | %.3f | %.3f |'
         % (len(casos), len(p), *dist, wn, wc),
         '| sin CLINIC_0022 y CLINIC_0024 | %d | %d | %.1f / %.1f / %.1f / %.1f | %.3f | %.3f |'
         % (sin.Caso.nunique(), len(sin), *dist_s, wn_s, wc_s), '',
         'Intervalo del 95 %% por remuestreo de pacientes (%d remuestreos, percentiles, semilla %d; se remuestrean '
         'casos con reemplazo y se juntan sus poses): W1 navegado **[%.3f, %.3f]**, W1 convencional **[%.3f, %.3f]**.'
         % (args.n_remuestreos, args.semilla, q[0, 0], q[1, 0], q[0, 1], q[1, 1]), '',
         'El intervalo refleja la variacion entre pacientes de la cohorte local; no incluye la incertidumbre de las '
         'series de referencia (26 y 35 tornillos), que se tratan como fijas.']
    args.out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
