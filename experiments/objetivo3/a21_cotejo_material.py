"""A21 - material del brazo fisico: cual (Fe o Ti) se parece mas a los tornillos REALES (01-decisiones 2026-10-09 (5)).

Regla escrita y subida antes de correr esto (commit f9d27cc). **El difusor no entra en ningun paso.**

- **Real:** los 2 tornillos aislados de `metal_0039`, con `a17.referencia_real` y cascaras de 1 mm.
- **Fisico:** salidas de `a19` (`0101`, `0102`; replicas A y B), cortes simulados que contienen `M`. Por corte,
  `common.cotejo.perfil_corte` sobre la reconstruccion con metal. Histograma dentro de `M` con
  `common.cotejo.histograma_m`.
- **Agregacion:** corte -> replica -> paciente -> material, por medianas.
- **Regla:** mas cascaras dentro de la envolvente real (p50 + p95); desempate por distancia de histograma;
  empate persistente lo decide la autora.

USO
---
    python experiments/objetivo3/a21_cotejo_material.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np

_AQUI = Path(__file__).resolve().parent
_RAIZ = _AQUI.parents[1]
sys.path.insert(0, str(_RAIZ / 'src'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo1'))
sys.path.insert(0, str(_AQUI))

from common.cotejo import agrega, bordes, histograma_m, perfil_corte  # noqa: E402
from a17_cotejo import referencia_real  # noqa: E402

PASO = 1.0
CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']


def main() -> None:
    out_dir = _AQUI / 'outputs' / 'a21'
    out_dir.mkdir(parents=True, exist_ok=True)
    reales, hists = referencia_real([_RAIZ / 'data'], _AQUI.parent / 'objetivo1' / 'p1_particion.csv', PASO)
    R = np.stack(reales)
    lo, hi = R.min(0), R.max(0)
    med_p50 = float(np.median([h['hu_p50'] for h in hists]))
    med_p95 = float(np.median([h['hu_p95'] for h in hists]))
    b = bordes(PASO)

    tabla, filas = [], []
    for mat in ('Fe', 'Ti'):
        por_caso = []
        for caso in CASOS:
            z = np.load(_AQUI / 'outputs' / 'a19' / ('a19_%s.npz' % caso))
            meta = json.loads((_AQUI / 'outputs' / 'a19' / ('a19_%s.json' % caso)).read_text(encoding='utf-8'))
            pix = tuple(meta['pixel_mm'])
            con_m = [i for i in range(len(z['ks'])) if z['M'][i].any()]
            prf_rep, h_rep = [], []
            for rep in ('A', 'B'):
                img = z['%s_%s' % (mat, rep)]
                prf_rep.append(agrega([perfil_corte(img[i], z['M'][i], pix, paso=PASO) for i in con_m]))
                h = histograma_m(np.concatenate([img[i][z['M'][i]] for i in con_m]))
                h_rep.append(h)
            por_caso.append((agrega(prf_rep), {q: float(np.median([h['hu_%s' % q] for h in h_rep]))
                                               for q in ('p50', 'p75', 'p95')}, len(con_m)))
            print('%s %s: %d cortes con M; M p50 %.0f p95 %.0f'
                  % (mat, caso, len(con_m), por_caso[-1][1]['p50'], por_caso[-1][1]['p95']))
        S = agrega([p for p, _, _ in por_caso])
        hs = {q: float(np.median([h[q] for _, h, _ in por_caso])) for q in ('p50', 'p75', 'p95')}
        comp = ~np.isnan(S) & ~np.isnan(lo)
        dentro = comp & (S >= lo) & (S <= hi)
        bajo = comp & (S < lo)
        sobre = comp & (S > hi)
        tabla.append({'material': mat, 'dentro_p50': int(dentro[:, 0].sum()), 'dentro_p95': int(dentro[:, 1].sum()),
                      'dentro_total': int(dentro.sum()), 'comparables': int(comp.sum()),
                      'bajo': int(bajo.sum()), 'sobre': int(sobre.sum()),
                      'M_p50': round(hs['p50'], 1), 'M_p75': round(hs['p75'], 1), 'M_p95': round(hs['p95'], 1),
                      'dist_hist': round(abs(hs['p50'] - med_p50) + abs(hs['p95'] - med_p95), 1)})
        for i in range(len(b) - 1):
            filas.append({'material': mat, 'r_lo_mm': b[i], 'r_hi_mm': b[i + 1],
                          'fis_p50': round(float(S[i, 0]), 1), 'real_lo_p50': round(float(lo[i, 0]), 1),
                          'real_hi_p50': round(float(hi[i, 0]), 1), 'fis_p95': round(float(S[i, 1]), 1),
                          'real_lo_p95': round(float(lo[i, 1]), 1), 'real_hi_p95': round(float(hi[i, 1]), 1)})

    tabla.sort(key=lambda t: (-t['dentro_total'], t['dist_hist']))
    empate = tabla[0]['dentro_total'] == tabla[1]['dentro_total'] and tabla[0]['dist_hist'] == tabla[1]['dist_hist']
    with open(out_dir / 'a21_perfiles.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    L = ['# A21 — material del brazo fisico frente a los tornillos reales de `metal_0039`', '',
         'Regla: `01-decisiones.md` 2026-10-09 (5), escrita antes de correr (commit f9d27cc). Cascaras de 1 mm. '
         '**El difusor no interviene.**', '',
         'Real: `M` p50 %s HU, p95 %s HU (los 2 tornillos).' % ('/'.join('%.0f' % h['hu_p50'] for h in hists),
                                                               '/'.join('%.0f' % h['hu_p95'] for h in hists)), '',
         '| material | dentro p50 | dentro p95 | dentro total | comparables | bajo | sobre | M p50 | M p75 | M p95 | dist. hist. |',
         '|---|---|---|---|---|---|---|---|---|---|---|']
    L += ['| %(material)s | %(dentro_p50)d | %(dentro_p95)d | %(dentro_total)d | %(comparables)d | %(bajo)d | %(sobre)d | '
          '%(M_p50).0f | %(M_p75).0f | %(M_p95).0f | %(dist_hist).0f |' % t for t in tabla]
    L += ['', ('**Empate persistente: lo decide la autora.**' if empate else
               '**Gana por la regla: `%s`** -> material primario del TOST; el otro, sensibilidad.' % tabla[0]['material']),
          '', 'Con 1 paciente de referencia el cotejo descarta, no prueba. Perfiles: `a21_perfiles.csv`.']
    (out_dir / 'a21_cotejo_material.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
