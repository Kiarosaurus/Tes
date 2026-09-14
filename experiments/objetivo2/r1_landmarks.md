# R1 — legibilidad de los landmarks de Kaiser (implicancia #26)

Volumenes en `r1_landmarks.csv`: 179; con error: 0.
Cohorte de calibracion (dataset6 sin objeto, una unidad por paciente): 69.
Cohorte de evaluacion (`grupo 1` de grupos.csv, una unidad por paciente): 65.

**Lectura obligatoria:** heuristica sin validacion experta. Las cifras son cota superior condicionada a que los puntos hayan caido en su sitio; ver laminas en `outputs/r1_qc/`. Contaminado no es irrecuperable.

## Envolvente nula (maximo en calibracion)

| Tipo | oscuro (HU < -200) | brillante (HU > 2500) |
|---|---|---|
| S1 | 0.00034 | 0.00000 |
| cresta | 0.02628 | 0.00000 |
| eips | 0.08636 | 0.00000 |

## Cohorte `calibracion` (n = 69)

| Landmark | limpio | contaminado | fuera de FOV | no hallado |
|---|---|---|---|---|
| S1 | 60 | 0 | 0 | 9 |
| cresta_der | 65 | 0 | 4 | 0 |
| cresta_izq | 65 | 0 | 4 | 0 |
| eips_der | 69 | 0 | 0 | 0 |
| eips_izq | 69 | 0 | 0 | 0 |

- Marco de Kaiser **computable** (5 puntos hallados y en FOV): **56 de 69**.
- Marco **computable y sin contaminacion** en los 5 puntos: **56 de 69**.
- S1 con discrepancia > 10 mm entre metodo sagital y metodo del ala: 24 de 59 con ambos metodos.
- S1 bajo la cresta (mm): mediana 34.2, rango -29.4 a 61.9.

## Cohorte `evaluacion` (n = 65)

| Landmark | limpio | contaminado | fuera de FOV | no hallado |
|---|---|---|---|---|
| S1 | 51 | 10 | 0 | 4 |
| cresta_der | 54 | 5 | 6 | 0 |
| cresta_izq | 57 | 3 | 5 | 0 |
| eips_der | 62 | 3 | 0 | 0 |
| eips_izq | 62 | 3 | 0 | 0 |

- Marco de Kaiser **computable** (5 puntos hallados y en FOV): **57 de 65**.
- Marco **computable y sin contaminacion** en los 5 puntos: **37 de 65**.
- S1 con discrepancia > 10 mm entre metodo sagital y metodo del ala: 16 de 54 con ambos metodos.
- **Nivel de S1 segun revisor clinico (medico ORL, referencia):** ok 51, +1 7, no hallado 4, otro 2, ? 1; sin revisar 0.
- Marco computable **con S1 correcto segun revisor clinico**: **48 de 65**; ademas sin contaminacion: **29 de 65**.
- Acuerdo agente vs revisor clinico (65 casos): categoria exacta 0.908; ok/no-ok 0.938, kappa de Cohen 0.81.
- Auditoria visual del nivel de S1 (agente): ok 53, +1 nivel 4, no hallado 4, ambiguo 2, error grosero 2; sin auditar 0.
- Marco computable **con S1 auditado ok**: **51 de 65**; ademas sin contaminacion: **32 de 65**.
- S1 bajo la cresta (mm): mediana 35.5, rango 4.2 a 57.2.
- `S1`: metal a <= 12 mm en 8, a <= 25 mm en 20 de 61; distancia mediana 38.1 mm.
- `cresta_der`: metal a <= 12 mm en 6, a <= 25 mm en 13 de 65; distancia mediana 56.0 mm.
- `cresta_izq`: metal a <= 12 mm en 3, a <= 25 mm en 8 de 65; distancia mediana 78.9 mm.
- `eips_der`: metal a <= 12 mm en 2, a <= 25 mm en 10 de 65; distancia mediana 47.1 mm.
- `eips_izq`: metal a <= 12 mm en 2, a <= 25 mm en 4 de 65; distancia mediana 58.7 mm.

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
| dataset7_CLINIC_metal_0051_data | contaminado | limpio | limpio | limpio | limpio | si |
| dataset7_CLINIC_metal_0053_data | no hallado | fuera de FOV | fuera de FOV | limpio | limpio | no |
| dataset7_CLINIC_metal_0054_data | limpio | fuera de FOV | fuera de FOV | limpio | limpio | no |
| dataset7_CLINIC_metal_0055_data | contaminado | limpio | contaminado | limpio | limpio | no |
| dataset7_CLINIC_metal_0062_data | contaminado | limpio | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0063_data | contaminado | limpio | contaminado | limpio | limpio | no |
| dataset7_CLINIC_metal_0067_data | limpio | contaminado | limpio | limpio | limpio | si |
| dataset7_CLINIC_metal_0069_data | limpio | contaminado | limpio | limpio | limpio | no |
| dataset7_CLINIC_metal_0070_data | contaminado | limpio | limpio | limpio | limpio | no |
