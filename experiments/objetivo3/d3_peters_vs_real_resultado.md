# D3 — Peters frente a real y modelo (DEC 2026-11-24 (23))

> Generado por `d3_peters_vs_real.py` el 2026-11-24 (verificacion independiente de la auditoria; descriptivo, sin regla de decision). Fuentes: `outputs/obj3_pose/peters_final` y `peters_val` (Peters Ti/Fe, 15 pacientes), `outputs/d1_tornillo` (real, n = 18) y `outputs/d2` (modelo, 0101/0102). Las salidas `outputs/d3/` no se versionan.

Peters: 15 pacientes (dataset6_CLINIC_0012_data, dataset6_CLINIC_0016_data, ...); real tornillo: n = 18; modelo: D2, mediana de 0101/0102. Exceso de amplitud (HU).

| anillo (mm) | Peters Ti | Peters Fe | real tornillo | modelo | Ti/real | modelo/real |
|---|---|---|---|---|---|---|
| 0-2 | 5004 | 15736 | 1930 | 1697 | 2.59 | 0.88 |
| 2-4 | 2558 | 10148 | 1199 | 488 | 2.13 | 0.41 |
| 4-6 | 2052 | 7339 | 765 | 97 | 2.68 | 0.13 |
| 6-8 | 1487 | 5364 | 473 | -65 | 3.14 | -0.14 |
| 8-10 | 1138 | 4172 | 174 | -40 | 6.55 | -0.23 |
| 10-12 | 972 | 3482 | 11 | -4 | - | - |
| 12-14 | 815 | 2829 | 48 | -9 | - | - |
| 14-16 | 681 | 2345 | 44 | 4 | - | - |
| 16-18 | 641 | 1998 | 42 | 4 | - | - |
| 18-20 | 538 | 1675 | 14 | 5 | - | - |
| 20-22 | 428 | 1502 | 32 | 4 | - | - |
| 22-24 | 369 | 1268 | 58 | 10 | 6.40 | 0.17 |

Razones solo donde el real supera 50 HU. Pacientes distintos por columna; ver limites en el docstring.