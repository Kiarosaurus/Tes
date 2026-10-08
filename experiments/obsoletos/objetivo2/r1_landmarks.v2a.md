# R1 — legibilidad de los landmarks de Kaiser (implicancia #26)

Volumenes en `r1_landmarks.csv`: 178; con error: 0.
Cohorte de calibracion (dataset6 sin objeto, sin duplicados): 70.
Cohorte de evaluacion (dataset7 contenido unico, regla provisional #20): 69.

**Lectura obligatoria:** heuristica sin validacion experta. Las cifras son cota superior condicionada a que los puntos hayan caido en su sitio; ver laminas en `outputs/r1_qc/`. Contaminado no es irrecuperable.

## Envolvente nula (maximo en calibracion)

| Tipo | oscuro (HU < -200) | brillante (HU > 2500) |
|---|---|---|
| S1 | 0.00034 | 0.00000 |
| cresta | 0.02628 | 0.00000 |
| eips | 0.08636 | 0.00000 |

## Cohorte `calibracion` (n = 70)

| Landmark | limpio | contaminado | fuera de FOV | no hallado |
|---|---|---|---|---|
| S1 | 61 | 0 | 0 | 9 |
| cresta_der | 66 | 0 | 4 | 0 |
| cresta_izq | 66 | 0 | 4 | 0 |
| eips_der | 70 | 0 | 0 | 0 |
| eips_izq | 70 | 0 | 0 | 0 |

- Marco de Kaiser **computable** (5 puntos hallados y en FOV): **57 de 70**.
- Marco **computable y sin contaminacion** en los 5 puntos: **57 de 70**.
- S1 con discrepancia > 10 mm entre metodo sagital y metodo del ala: 24 de 60 con ambos metodos.
- S1 bajo la cresta (mm): mediana 33.6, rango -29.4 a 61.9.

## Cohorte `evaluacion` (n = 69)

| Landmark | limpio | contaminado | fuera de FOV | no hallado |
|---|---|---|---|---|
| S1 | 54 | 10 | 0 | 5 |
| cresta_der | 55 | 7 | 7 | 0 |
| cresta_izq | 61 | 2 | 6 | 0 |
| eips_der | 66 | 3 | 0 | 0 |
| eips_izq | 66 | 3 | 0 | 0 |

- Marco de Kaiser **computable** (5 puntos hallados y en FOV): **59 de 69**.
- Marco **computable y sin contaminacion** en los 5 puntos: **39 de 69**.
- S1 con discrepancia > 10 mm entre metodo sagital y metodo del ala: 18 de 55 con ambos metodos.
- S1 bajo la cresta (mm): mediana 34.9, rango -11.1 a 130.2.
- `S1`: metal a <= 12 mm en 8, a <= 25 mm en 19 de 64; distancia mediana 38.8 mm.
- `cresta_der`: metal a <= 12 mm en 6, a <= 25 mm en 13 de 69; distancia mediana 56.0 mm.
- `cresta_izq`: metal a <= 12 mm en 2, a <= 25 mm en 7 de 69; distancia mediana 78.2 mm.
- `eips_der`: metal a <= 12 mm en 2, a <= 25 mm en 10 de 69; distancia mediana 53.9 mm.
- `eips_izq`: metal a <= 12 mm en 2, a <= 25 mm en 4 de 69; distancia mediana 63.0 mm.

### Volumenes de evaluacion sin marco legible

| Caso | S1 | cresta_der | cresta_izq | eips_der | eips_izq | S1 discordante |
|---|---|---|---|---|---|---|
| dataset7_CLINIC_metal_0000_data | contaminado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0002_data | limpio | limpio | fuera de FOV | limpio | limpio | si |
| dataset7_CLINIC_metal_0003_data | limpio | fuera de FOV | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0006_data | limpio | contaminado | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0009_data | contaminado | limpio | limpio | limpio | limpio | si |
| dataset7_CLINIC_metal_0015_data | limpio | fuera de FOV | fuera de FOV | limpio | limpio | no |
| dataset7_CLINIC_metal_0016_data | no hallado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0017_data | limpio | limpio | limpio | contaminado | contaminado | no |
| dataset7_CLINIC_metal_0019_data | limpio | limpio | limpio | limpio | contaminado | no |
| dataset7_CLINIC_metal_0020_data | limpio | limpio | limpio | contaminado | contaminado | no |
| dataset7_CLINIC_metal_0022_data | no hallado | fuera de FOV | fuera de FOV | limpio | limpio | no |
| dataset7_CLINIC_metal_0023_data | no hallado | fuera de FOV | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0024_data | contaminado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0029_data | limpio | contaminado | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0031_data | limpio | contaminado | limpio | limpio | limpio | si |
| dataset7_CLINIC_metal_0032_data | limpio | limpio | contaminado | limpio | limpio | no |
| dataset7_CLINIC_metal_0037_data | limpio | limpio | limpio | contaminado | limpio | no |
| dataset7_CLINIC_metal_0041_data | contaminado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0042_data | contaminado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0045_data | no hallado | contaminado | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0051_data | contaminado | limpio | limpio | limpio | limpio | si |
| dataset7_CLINIC_metal_0053_data | no hallado | fuera de FOV | fuera de FOV | limpio | limpio | no |
| dataset7_CLINIC_metal_0054_data | limpio | fuera de FOV | fuera de FOV | limpio | limpio | no |
| dataset7_CLINIC_metal_0055_data | contaminado | limpio | contaminado | limpio | limpio | no |
| dataset7_CLINIC_metal_0062_data | contaminado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0063_data | contaminado | contaminado | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0067_data | limpio | contaminado | limpio | limpio | limpio | si |
| dataset7_CLINIC_metal_0069_data | limpio | contaminado | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0070_data | contaminado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0071_data | limpio | fuera de FOV | fuera de FOV | limpio | limpio | no |
