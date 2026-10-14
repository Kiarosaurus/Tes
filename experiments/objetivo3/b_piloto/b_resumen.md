# Piloto de la plantilla `T` (opcion B, compuerta) — resultado

Generado por `b_piloto_plantilla.py`. Criterio fijado en `v2_plan.md` antes de correr.

**VEREDICTO: B PASA la compuerta** (C0 PASA, C1 PASA, C2 PASA).

## C0 — controles (A = direccional fuera / rms dentro)

| figura | A |
|---|---|
| disco | 0.0067 |
| elipse | 0.0642 |
| dos_discos | 0.0902 |
| estadio | 0.1383 |

Regla: A_disco < 0.2 x A_dos_discos.

## C1 — estabilidad 360 frente a 720 angulos

Mediana por corte de Spearman: **1.000** (228 cortes; regla >= 0.90).

## C2 — coincidencia con el residuo real en 2-10 mm

lambda0 = 0.0847 por mm (1 / mediana de L_max = 11.80 mm).

| brazo | pacientes (con control) | cortes | rho mediana | d mediana | d0 anatomico mediana | e = d - d0 mediana | p Wilcoxon (e > 0) | cumple |
|---|---|---|---|---|---|---|---|---|
| principal | 18 (13) | 228 | 0.166 | 0.133 | 0.041 | 0.116 | 0.0085 | si |
| lambda_x0.5 | 18 (13) | 228 | 0.175 | 0.140 | 0.041 | 0.119 | 0.0085 | si |
| lambda_x2 | 18 (13) | 228 | 0.156 | 0.123 | 0.040 | 0.116 | 0.0085 | si |
| suavizada | 18 (13) | 228 | 0.172 | 0.125 | 0.050 | 0.114 | 0.0085 | si |

Regla (solo `principal` decide): p < 0.05 (e > 0, pacientes con control anatomico) y mediana de d >= 0.05. Los otros brazos son sensibilidad.

Limites: el residuo real incluye anatomia (referencia = otro corte); 2D paralelo; sin scatter; pacientes de entrenamiento y validacion (no hay modelo: compuerta sobre la plantilla, no evaluacion).
