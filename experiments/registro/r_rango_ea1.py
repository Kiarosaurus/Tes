"""Rango entre pacientes (minimo y maximo) de la reconstruccion de implantes reales E-A1 (prueba, v1, run04_mejor, 0.030).

Cierra la promesa del diseno (cap. 3 sec:ap-reconstruccion: "por ultimo entre pacientes, con su rango") que
`resultados_prueba_v1.md` no resume (solo medianas). No es un analisis nuevo: resume columnas ya calculadas por
`a23` en su salida por paciente. Descriptivo y posterior; sin prueba de hipotesis.

Entrada: experiments/objetivo3/outputs/obj3_pose/a23_final_run04_d003/a23_pacientes.csv (una fila por paciente).
Control de regresion: las medianas por grupo deben reproducir la tabla E-A1 de resultados_prueba_v1.md. Si no, aborta.

Uso: python experiments/registro/r_rango_ea1.py
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parents[2]
CSV = RAIZ / 'experiments/objetivo3/outputs/obj3_pose/a23_final_run04_d003/a23_pacientes.csv'
COLS = ('mae_G', 'mae_M', 'mae_B', 'hueso_sdc', 'hueso_dvol', 'metal_sdc', 'metal_dvol', 'exceso_costura')
ESPERADO = {
    'grupo 1': (270.9, 2312.5, 198.0, 0.717, -0.041, 0.928, -0.078, 6.3),
    'grupo 2': (199.8, 2747.9, 165.8, 0.534, 0.324, 0.753, -0.255, 9.0),
}


def main() -> None:
    with CSV.open(newline='') as fh:
        filas = list(csv.DictReader(fh))
    for grupo, esperado in ESPERADO.items():
        sub = [f for f in filas if f['grupo'] == grupo]
        print(f'{grupo}: n={len(sub)}')
        for col, esp in zip(COLS, esperado):
            v = np.array([float(f[col]) for f in sub])
            dec = 1 if col in ('mae_G', 'mae_M', 'mae_B', 'exceso_costura') else 3
            med = round(float(np.median(v)), dec)
            if abs(med - esp) > 10 ** -dec / 2 + 1e-9:
                raise SystemExit(f'control de regresion falla: {grupo} {col} mediana {med} != {esp}')
            print(f'  {col}: mediana {med:.{dec}f} [{v.min():.{dec}f}, {v.max():.{dec}f}]')
    print('control de regresion: medianas reproducen resultados_prueba_v1.md')


if __name__ == '__main__':
    main()
