# E15 — W1 por remuestreo de pacientes y sensibilidad sin CLINIC_0022 / 0024

Generado por `e15_w1_sensibilidad.py` sobre `e13_poses.csv`, d = 7.0 mm (SAP). POSTERIOR y descriptivo (`01-decisiones.md` 2026-10-08 ptos 18 y 22); no cambia ninguna cifra de E13.

| conjunto | casos | poses | % g0 / g1 / g2 / g3 | W1 navegado | W1 convencional |
|---|---|---|---|---|---|
| cohorte primaria (regresion de E13) | 72 | 3600 | 51.5 / 31.4 / 11.1 / 6.0 | 0.206 | 0.230 |
| sin CLINIC_0022 y CLINIC_0024 | 70 | 3500 | 51.8 / 31.4 / 11.1 / 5.7 | 0.203 | 0.237 |

Intervalo del 95 % por remuestreo de pacientes (2000 remuestreos, percentiles, semilla 20261015; se remuestrean casos con reemplazo y se juntan sus poses): W1 navegado **[0.152, 0.313]**, W1 convencional **[0.089, 0.364]**.

El intervalo refleja la variacion entre pacientes de la cohorte local; no incluye la incertidumbre de las series de referencia (26 y 35 tornillos), que se tratan como fijas.
