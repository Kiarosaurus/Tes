"""Veredicto de la etapa 0 de v3 (barrido pasos x eta), con la regla de docs/01-decisiones.md 2026-11-20.

Criterio (a), calculable desde los `a15_*_cotejo.csv`: nº de las 7 cascaras criticas de 1 mm (r_lo = 4,5,6,8,9,10,11)
con el p95 sintetico DENTRO de la envolvente real de `metal_0039` (min-max de sus 2 tornillos). Exito si >= 4.
Misma agregacion que a17/A28: semilla -> paciente (agrega) -> mediana entre pacientes.
Criterio (b) (desviacion 0-2 mm <= 279.6 HU, definido con D2 sobre NIfTI) NO se calcula aqui: el barrido uso
--sin-nifti. Las variantes que pasan (a) quedan marcadas "PENDIENTE (b)".
Control: la variante de referencia debe reproducir el cotejo de octubre (--control); tolerancia --tol (HU, p95, 7 cascaras).
Informa TODAS las variantes, tambien las desfavorables. Exploratorio/post-hoc. No elige por si solo.

USO (local, tras copiar los CSV de Khipu):
  python -I eta_veredicto.py --dirs <carpeta_variante> [<carpeta_variante> ...] --control <cotejo_octubre> --out veredicto.md
"""
from __future__ import annotations
import argparse, sys
from pathlib import Path
import numpy as np

REPO = Path(r'D:/UTEC/CICLOX/Salvar-El-Ciclo/PFCII/metalsynth-pelvis')
CRITICAS = [4, 5, 6, 8, 9, 10, 11]
UMBRAL = 4


def perfil_agregado(a17, d: Path, paso: float):
    datos = a17.lee_sintetico(d, paso)
    res = {}
    for et in datos:
        por_caso = [a17.agrega([p for p, _ in datos[et][c].values()]) for c in sorted(datos[et])]
        res[et] = (a17.agrega(por_caso), sorted(datos[et]))
    return res


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dirs', type=Path, nargs='+', required=True)
    ap.add_argument('--control', type=Path, default=None, help='cotejo de octubre de run04_mejor (carpeta)')
    ap.add_argument('--ref-variante', default='p50_e0', help='sufijo de la variante de control')
    ap.add_argument('--tol', type=float, default=1.0, help='tolerancia del control (HU)')
    ap.add_argument('--repo', type=Path, default=REPO)
    ap.add_argument('--data', type=Path, nargs='+', default=None)
    ap.add_argument('--paso-mm', type=float, default=1.0)
    ap.add_argument('--out', type=Path, default=Path('veredicto.md'))
    a = ap.parse_args()
    sys.path.insert(0, str(a.repo / 'experiments' / 'objetivo3'))
    import a17_cotejo as a17                      # reutiliza lector y agregacion (no reimplementa)
    from common.cotejo import bordes
    data = a.data or [a.repo / 'data']
    part = a.repo / 'experiments' / 'objetivo1' / 'p1_particion.csv'
    reales, _ = a17.referencia_real(list(data), part, a.paso_mm)
    R = np.stack(reales); lo, hi = np.nanmin(R, 0), np.nanmax(R, 0)
    b = bordes(a.paso_mm)
    idx = {int(round(b[i])): i for i in range(len(b) - 1)}
    cri = [idx[r] for r in CRITICAS]

    filas, perf = [], {}
    for d in a.dirs:
        for et, (S, casos) in perfil_agregado(a17, d, a.paso_mm).items():
            perf[d.name] = S
            dentro = [r for r, i in zip(CRITICAS, cri)
                      if not np.isnan(S[i, 1]) and not np.isnan(lo[i, 1]) and lo[i, 1] <= S[i, 1] <= hi[i, 1]]
            filas.append((d.name, casos, dentro, S))
    L = ['# Veredicto etapa 0 de v3 (exploratorio, post-hoc)', '',
         'Regla: 01-decisiones.md 2026-11-20. Criterio (a) desde los CSV; (b) 0-2 mm requiere NIfTI (no calculado).', '',
         '## Control de validez', '']
    ctrl = [n for n in perf if n.endswith(a.ref_variante)]
    if a.control and ctrl:
        Sc = perfil_agregado(a17, a.control, a.paso_mm)
        Sc = next(iter(Sc.values()))[0]
        dif = np.nanmax(np.abs(perf[ctrl[0]][cri, 1] - Sc[cri, 1]))
        ok = dif <= a.tol
        L.append('Max |p95 variante %s - p95 octubre| en las 7 cascaras: **%.2f HU** (tol %.2f) -> %s' %
                 (ctrl[0], dif, a.tol, 'REPRODUCE' if ok else 'NO REPRODUCE: el barrido no se interpreta'))
    else:
        ok = None
        L.append('Control NO evaluado (falta --control o la variante %s). **El barrido no es interpretable sin el.**' % a.ref_variante)
    L += ['', '## Cascaras criticas con p95 dentro de la envolvente real', '',
          '| variante | pacientes | dentro (de 7) | cascaras (mm) | criterio (a) >= %d | criterio (b) 0-2 mm |' % UMBRAL,
          '|---|---|---|---|---|---|']
    for n, casos, dentro, S in filas:
        pasa = len(dentro) >= UMBRAL
        L.append('| %s | %d | %d | %s | %s | %s |' % (n, len(casos), len(dentro), ','.join(map(str, dentro)) or '-',
                 'PASA' if pasa else 'no', 'PENDIENTE (b): rerun con NIfTI + d2' if pasa else 'n/a'))
    L += ['', '## p95 sintetico frente a la envolvente real (HU), cascaras criticas', '',
          '| r (mm) | real lo | real hi | ' + ' | '.join(n for n, *_ in filas) + ' |',
          '|---|---|---|' + '---|' * len(filas)]
    for r, i in zip(CRITICAS, cri):
        L.append('| %d-%d | %.0f | %.0f | %s |' % (r, r + 1, lo[i, 1], hi[i, 1], ' | '.join('%.0f' % S[i, 1] for *_, S in filas)))
    L += ['', 'Limites: 2 pacientes de validacion; un checkpoint; el criterio (b) no esta evaluado; resultado exploratorio.']
    a.out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
