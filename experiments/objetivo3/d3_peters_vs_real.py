"""D3 - perfil radial de Peters (Ti y Fe) frente al real (D1) y al sintetico (D2), con la MISMA metrica que D1.

Pregunta (DEC 2026-11-24 (23)): cuanto se aleja el protocolo fisico de la amplitud real por anillo, y donde queda lo real
respecto de Peters y del modelo. Es DESCRIPTIVO (sin regla de decision) y no sustituye a E-A2.

Metrica (la de D1, `d1_alcance_rayas.py`): exceso = amplitud de Peters (5 % superior - 5 % inferior) de la imagen con metal
menos la de la misma imagen sin metal, en los mismos pixeles de cuerpo fuera de `M`, por anillo de 2 mm de distancia en el
plano a `M`. Peters: salidas de `a19` (`outputs/obj3_pose/peters_final` = 13 de prueba y `peters_val` = 2 de validacion),
condicion A (`Ti_A`, `Fe_A`) frente a `limpia_A`; hasta `--max-cortes` cortes por paciente (mediana), luego mediana de pacientes.
Real: `outputs/d1_tornillo/d1_por_paciente.csv` (componentes de tamano tornillo, D1). Sintetico: `outputs/d2/d2_perfil.csv` (D2,
`run04_mejor`, validacion 0101/0102, mediana de los dos pacientes).

Limites: pacientes distintos en cada columna (Peters 15, real 18, sintetico 2); la referencia real es otro corte del mismo
paciente, la de Peters y el sintetico es el mismo corte sin metal; no se conoce material ni reconstruccion de los tornillos reales.

Salida: `outputs/d3/d3_peters_real_modelo.csv` y `d3_resumen.md`. Resumen versionado: `d3_peters_vs_real_resultado.md`.

USO
---
    python experiments/objetivo3/d3_peters_vs_real.py [--max-cortes 8]
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
from pathlib import Path

import numpy as np
from scipy import ndimage as ndi

from d1_alcance_rayas import BORDES_MM, cuerpo_2d, perfil

_AQUI = Path(__file__).resolve().parent
ANILLOS = 12          # 0-24 mm


def pixel(j: dict) -> tuple[float, float]:
    p = j['pixel_mm']
    return (float(p[0]), float(p[1])) if isinstance(p, list) else (float(p), float(p))


def peters(max_cortes: int) -> tuple[dict[str, np.ndarray], list[str]]:
    res: dict[str, list[np.ndarray]] = {'Ti': [], 'Fe': []}
    nombres: list[str] = []
    archivos = (sorted(glob.glob(str(_AQUI / 'outputs/obj3_pose/peters_final/a19_*.npz')))
                + sorted(glob.glob(str(_AQUI / 'outputs/obj3_pose/peters_val/a19_*.npz'))))
    for f in archivos:
        z = np.load(f)
        j = json.load(open(f[:-4] + '.json'))
        px = pixel(j)
        nombres.append(os.path.basename(f)[4:-4])
        n = len(z['ks'])
        idx = list(range(n))[::max(1, n // max_cortes)][:max_cortes]
        for mat in ('Ti', 'Fe'):
            por_corte = []
            for i in idx:
                m = z['M'][i]
                if m.sum() < 20:
                    continue
                dist = ndi.distance_transform_edt(~m, sampling=px)
                valido = cuerpo_2d(z['original'][i]) & ~m
                por_corte.append(perfil(z[mat + '_A'][i], z['limpia_A'][i], dist, valido))
            res[mat].append(np.nanmedian(np.stack(por_corte), 0) if por_corte else np.full(BORDES_MM.size - 1, np.nan))
    return {k: np.stack(v) for k, v in res.items()}, nombres


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--max-cortes', type=int, default=8)
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'd3')
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    P, nombres = peters(a.max_cortes)
    real = list(csv.DictReader(open(_AQUI / 'outputs/d1_tornillo/d1_por_paciente.csv')))
    mod = {r['anillo_mm']: r for r in csv.DictReader(open(_AQUI / 'outputs/d2/d2_perfil.csv'))}
    filas = []
    for i in range(ANILLOS):
        lab = f'{int(BORDES_MM[i])}-{int(BORDES_MM[i + 1])}'
        rv = np.array([float(x[lab]) for x in real if x[lab] not in ('', 'nan')])
        ti, fe = P['Ti'][:, i], P['Fe'][:, i]
        r = float(np.median(rv))
        m = float(mod[lab]['run04_mejor_med']) if lab in mod else float('nan')
        filas.append(dict(anillo_mm=lab, peters_ti=np.nanmedian(ti), peters_ti_min=np.nanmin(ti), peters_ti_max=np.nanmax(ti),
                          peters_fe=np.nanmedian(fe), real_tornillo=r, real_ic90_lo=float(np.percentile(rv, 5)),
                          real_ic90_hi=float(np.percentile(rv, 95)), modelo_run04_mejor=m,
                          ti_sobre_real=np.nanmedian(ti) / r if r > 50 else float('nan'),
                          modelo_sobre_real=m / r if r > 50 else float('nan'),
                          n_peters=int(np.isfinite(ti).sum()), n_real=int(rv.size)))
    with open(a.out_dir / 'd3_peters_real_modelo.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    L = ['# D3 - Peters frente a real y modelo, por anillo (generado por `d3_peters_vs_real.py`)', '',
         f'Peters: {len(nombres)} pacientes ({", ".join(nombres[:2])}, ...); real tornillo: n = {filas[0]["n_real"]}; '
         'modelo: D2, mediana de 0101/0102. Exceso de amplitud (HU).', '',
         '| anillo (mm) | Peters Ti | Peters Fe | real tornillo | modelo | Ti/real | modelo/real |', '|---|---|---|---|---|---|---|']
    for r in filas:
        f1 = lambda v: '-' if not np.isfinite(v) else f'{v:.0f}'
        f2 = lambda v: '-' if not np.isfinite(v) else f'{v:.2f}'
        L.append(f'| {r["anillo_mm"]} | {f1(r["peters_ti"])} | {f1(r["peters_fe"])} | {f1(r["real_tornillo"])} | '
                 f'{f1(r["modelo_run04_mejor"])} | {f2(r["ti_sobre_real"])} | {f2(r["modelo_sobre_real"])} |')
    L += ['', 'Razones solo donde el real supera 50 HU. Pacientes distintos por columna; ver limites en el docstring.']
    (a.out_dir / 'd3_resumen.md').write_text('\n'.join(L), encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
