"""Medianas por brazo de la bone/metal integrity (SDC y cambio relativo de volumen) en E-A2 (prueba, v1).

Cierra el \\GAPDATO de capitulo4 (r00/r01), seccion Analisis anadidos, ultimo parrafo: "medianas por brazo del
coeficiente de Sorensen-Dice y del cambio relativo de volumen del hueso y del metal en la sintesis sobre pelvis sin
metal". No es un analisis nuevo: resume columnas ya calculadas por `a20_evaluador_ea2.py --corrida-final` (componentes
descriptivos preinscritos, cap. 3 sec:ap-reconstruccion). Descriptivo y posterior; sin prueba de hipotesis.

Entrada: experiments/objetivo3/outputs/obj3_pose/a20_test/a20_ea2_test.csv (CSV congelado de v1).
Agregacion (la de a24_contrastes.py): valor por paciente = mediana de las 5 semillas (difusor) o de las replicas
A y B (Peters, por material); luego mediana, minimo y maximo entre pacientes.
Control de regresion: diferencia media de amp_HU difusor run04_mejor - Peters Ti = -301.0 HU (n = 13) y mediana del
ruido de Peters (ruido_A-B) = 183.5 HU, ambas en resultados_prueba_v1.md. Si no reproduce, aborta.

Uso: python experiments/registro/r_integridad_ea2.py
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parents[2]
CSV = RAIZ / 'experiments/objetivo3/outputs/obj3_pose/a20_test/a20_ea2_test.csv'
COLS = ('hueso_sdc', 'hueso_dvol', 'metal_sdc', 'metal_dvol')
BRAZOS = {'difusor run04_mejor': ('difusor', 'run04_mejor_'), 'difusor run04_60k': ('difusor', 'run04_60k_'),
          'Peters Ti': ('peters', 'Ti_'), 'Peters Fe': ('peters', 'Fe_'), 'copia y pegado': ('copiapega', 'HU_')}


def por_paciente(filas: list[dict], brazo: str, pref: str, col: str) -> dict[str, float]:
    """Mediana por paciente de `col` sobre las filas del brazo con condicion que empieza por `pref`."""
    out: dict[str, list[float]] = {}
    for f in filas:
        if f['brazo'] == brazo and f['condicion'].startswith(pref):
            v = float(f[col])
            if not math.isnan(v):
                out.setdefault(f['caso'], []).append(v)
    return {c: float(np.median(v)) for c, v in out.items()}


def main() -> None:
    with CSV.open(newline='') as fh:
        filas = list(csv.DictReader(fh))
    # Control de regresion
    d = por_paciente(filas, 'difusor', 'run04_mejor_', 'amp_HU')
    t = por_paciente(filas, 'peters', 'Ti_', 'amp_HU')
    dif = np.array([d[c] - t[c] for c in sorted(d)])
    ruido = np.median(list(por_paciente(filas, 'peters', 'ruido_A-B', 'amp_HU').values()))
    print(f'control: n={len(dif)} dif media={dif.mean():.1f} (esperado -301.0); ruido Peters={ruido:.1f} (183.5)')
    assert len(dif) == 13 and round(dif.mean(), 1) == -301.0 and round(ruido, 1) == 183.5, 'NO REPRODUCE'
    print('| brazo | n | ' + ' | '.join(COLS) + ' |')
    for nombre, (b, p) in BRAZOS.items():
        celdas, ns = [], set()
        for col in COLS:
            v = np.array(list(por_paciente(filas, b, p, col).values()))
            ns.add(len(v))
            celdas.append(f'{np.median(v):.3f} [{v.min():.3f}, {v.max():.3f}]' if len(v) else 'nan')
        print(f'| {nombre} | {"/".join(map(str, sorted(ns)))} | ' + ' | '.join(celdas) + ' |')


if __name__ == '__main__':
    main()
