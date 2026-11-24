# D3 — Peters frente a real y modelo (DEC 2026-11-24 (23) y (23-a))

> Generado por `d3_peters_vs_real.py` el 2026-11-24 (verificacion independiente de la auditoria; descriptivo, sin regla de decision). Fuentes: `outputs/obj3_pose/peters_final` y `peters_val` (Peters Ti/Fe, 15 pacientes), `outputs/d1_tornillo` (real, n = 18), `outputs/d2` (modelo en validacion, 2 pacientes) y `outputs/obj3_pose/final/run04_mejor` (modelo en los 13 de prueba, 5 semillas, para la segunda tabla). Las salidas `outputs/d3/` no se versionan.

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

## Mismos 13 pacientes de prueba, plano axial (2.a version)

(a) exceso = amplitud(img) - amplitud(ref); (b) amplitud(img - ref). Peters Ti y sintetizador `run04_mejor` (5 semillas); real solo (a).

| anillo (mm) | Ti (a) | sintetizador (a) | real tornillo (a) | Ti (b) | sintetizador (b) |
|---|---|---|---|---|---|
| 0-2 | 5004 | 1457 | 1930 | 5935 | 2230 |
| 2-4 | 2558 | 583 | 1199 | 3110 | 1502 |
| 4-6 | 1931 | 220 | 765 | 2323 | 1177 |
| 6-8 | 1404 | 73 | 473 | 1743 | 1059 |
| 8-10 | 1054 | 45 | 174 | 1391 | 1011 |
| 10-12 | 829 | 10 | 11 | 1204 | 872 |
| 12-14 | 728 | 1 | 48 | 1039 | 670 |
| 14-16 | 677 | 7 | 44 | 975 | 563 |
| 16-18 | 523 | 8 | 42 | 921 | 485 |
| 18-20 | 401 | 0 | 14 | 852 | 476 |
| 20-22 | 367 | 0 | 32 | 803 | 400 |
| 22-24 | 323 | 0 | 58 | 761 | 342 |