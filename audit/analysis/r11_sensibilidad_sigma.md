# R-11 (C): sensibilidad de W1 a la convencion h = k*sigma del muestreador
Origen: Khipu job 65079 (audit_r11.sbatch, CPU, 72 casos x 50 poses = 3600 poses por d), FACTOR_SIGMA 4.0 / 2.0 / 1.0.
Tabla copiada de la salida de e13_sap_fs{4.0,2.0,1.0}.md pegada por la autora; CSV/MD originales en ~/audit_khipu/r11/ (pendientes de bajar a local).
Control: FACTOR_SIGMA=2.0, d=7.0 -> W1 0.206 (navegado) / 0.230 (convencional) = cifras de e13_sap.md. Inclinacion mediana 0.74 / 1.48 / 2.96 grados (escala x2 por paso).
Umbral de lectura de la tesis: 0.395 (distancia entre las dos referencias de Zwingmann). Descriptivo; sin regla de decision.

| FACTOR_SIGMA (sigma) | d (mm) | %g0 | %g1 | %g2 | %g3 | W1 navegado | W1 convencional |
|---|---|---|---|---|---|---|---|
| 4.0 (x0.5) | 4.91 | 84.8 | 13.3 | 1.8 | 0.1 | 0.378 | 0.773 |
| 4.0 (x0.5) | 7.0 SAP | 68.8 | 24.6 | 5.8 | 0.8 | 0.168 | 0.559 |
| 4.0 (x0.5) | 7.3 | 65.6 | 26.8 | 6.8 | 0.9 | 0.189 | 0.516 |
| 2.0 (x1, decidido) | 4.91 | 70.3 | 20.4 | 6.9 | 2.3 | 0.138 | 0.533 |
| 2.0 (x1, decidido) | 7.0 SAP | 51.5 | 31.4 | 11.1 | 6.0 | 0.206 | 0.230 |
| 2.0 (x1, decidido) | 7.3 | 48.6 | 32.5 | 12.3 | 6.7 | 0.247 | 0.174 |
| 1.0 (x2) | 4.91 | 41.8 | 25.1 | 15.1 | 17.9 | 0.542 | 0.183 |
| 1.0 (x2) | 7.0 SAP | 27.9 | 26.8 | 17.4 | 27.8 | 0.901 | 0.506 |
| 1.0 (x2) | 7.3 | 26.0 | 26.9 | 18.7 | 28.5 | 0.947 | 0.552 |

Lectura (descriptiva): en d=7.0 solo sigma x1 deja ambas distancias bajo 0.395. sigma x0.5 queda cerca del navegado y lejos del convencional; sigma x2 queda lejos de ambos.
No se recomienda ajustar sigma (seria calibracion post hoc contra la referencia). Candidato a apendice de sensibilidad.
