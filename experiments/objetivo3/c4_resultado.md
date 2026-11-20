# C4 — anisotropía angular del artefacto: resultados (EXPLORATORIO, POST-HOC)

Fuente de las cifras que la tesis puede citar (`overleaf/CLAUDE.md` regla 5). Reglas: `docs/01-decisiones.md` 2026-11-20 (3); protocolo y enmienda v2 en `c4_protocolo.md`; scripts `c4_anisotropia.py` (validación 0101/0102 y real) y `c4b_prueba.py` (13 de prueba). Figura: `c4_fig_desenrollada.png`. Generado el 2026-11-20 en local; las tablas se copian sin edición desde `c4b_resumen.md` y `c4_resumen_distancia.md`.

**Lectura permitida:** η²_exc de un brazo frente a otro y a su control sin metal, por escala angular K. **No** equivalencia, **no** causa, **no** mejora. Referencia real = 2 tornillos de `metal_0039` (otra anatomía y escáner). Peters Ti es una referencia física, no «lo real». La v1 de la métrica (anillos por radio al centroide) quedó invalidada (`c4_resumen_v1_centroide.md` en el directorio de trabajo; control sin metal 0.49, halo liso en `M` elíptico 0.805).

# Parte 1 — 13 pacientes de prueba (c4b)

## C4b — anisotropía angular en los 13 pacientes de PRUEBA (exploratorio; reglas en `01-decisiones.md` 2026-11-20 (3))

η²_exc por paciente (mediana corte → semilla → paciente); mediana entre pacientes con IC95 bootstrap por paciente (B=2000).

## Principal: K=24, [-500, 1300] HU

| brazo | modo | pacientes | η²_exc mediana | IC95 bootstrap |
|---|---|---|---|---|
| control_anatomia_test | crudo | 13 | 0.411 | [0.345, 0.453] |
| peters_Ti_test | crudo | 13 | 0.443 | [0.178, 0.500] |
| peters_Ti_test | residuo | 13 | 0.388 | [0.106, 0.437] |
| run04_mejor_test | crudo | 13 | 0.504 | [0.483, 0.543] |
| run04_mejor_test | residuo | 13 | 0.387 | [0.302, 0.456] |
| run04_60k_test | crudo | 13 | 0.507 | [0.447, 0.546] |
| run04_60k_test | residuo | 13 | 0.352 | [0.272, 0.413] |

Diferencias pareadas por paciente (mediana y IC95 bootstrap):

| contraste | modo | mediana | IC95 |
|---|---|---|---|
| run04_mejor_test − peters_Ti_test | residuo | 0.039 | [-0.046, 0.082] |
| run04_mejor_test − peters_Ti_test | crudo | 0.080 | [0.027, 0.163] |
| run04_mejor_test − control_anatomia_test | crudo | 0.072 | [0.034, 0.143] |
| peters_Ti_test − control_anatomia_test | crudo | 0.007 | [-0.075, 0.081] |
| run04_60k_test − peters_Ti_test | residuo | 0.004 | [-0.058, 0.046] |

## Sensibilidad K=12

| brazo | modo | pacientes | η²_exc mediana | IC95 bootstrap |
|---|---|---|---|---|
| control_anatomia_test | crudo | 13 | 0.330 | [0.268, 0.399] |
| peters_Ti_test | crudo | 13 | 0.220 | [0.134, 0.297] |
| peters_Ti_test | residuo | 13 | 0.128 | [0.063, 0.234] |
| run04_mejor_test | crudo | 13 | 0.390 | [0.340, 0.462] |
| run04_mejor_test | residuo | 13 | 0.240 | [0.217, 0.359] |
| run04_60k_test | crudo | 13 | 0.388 | [0.303, 0.468] |
| run04_60k_test | residuo | 13 | 0.258 | [0.173, 0.319] |

Diferencias pareadas por paciente (mediana y IC95 bootstrap):

| contraste | modo | mediana | IC95 |
|---|---|---|---|
| run04_mejor_test − peters_Ti_test | residuo | 0.124 | [0.060, 0.152] |
| run04_mejor_test − peters_Ti_test | crudo | 0.155 | [0.045, 0.194] |
| run04_mejor_test − control_anatomia_test | crudo | 0.015 | [-0.009, 0.131] |
| peters_Ti_test − control_anatomia_test | crudo | -0.049 | [-0.187, -0.015] |
| run04_60k_test − peters_Ti_test | residuo | 0.088 | [0.031, 0.133] |

## Sensibilidad K=48

| brazo | modo | pacientes | η²_exc mediana | IC95 bootstrap |
|---|---|---|---|---|
| control_anatomia_test | crudo | 13 | 0.438 | [0.384, 0.476] |
| peters_Ti_test | crudo | 13 | 0.580 | [0.534, 0.645] |
| peters_Ti_test | residuo | 13 | 0.582 | [0.566, 0.685] |
| run04_mejor_test | crudo | 13 | 0.563 | [0.523, 0.584] |
| run04_mejor_test | residuo | 13 | 0.445 | [0.388, 0.496] |
| run04_60k_test | crudo | 13 | 0.535 | [0.494, 0.597] |
| run04_60k_test | residuo | 13 | 0.387 | [0.326, 0.457] |

Diferencias pareadas por paciente (mediana y IC95 bootstrap):

| contraste | modo | mediana | IC95 |
|---|---|---|---|
| run04_mejor_test − peters_Ti_test | residuo | -0.178 | [-0.206, -0.134] |
| run04_mejor_test − peters_Ti_test | crudo | -0.012 | [-0.068, 0.005] |
| run04_mejor_test − control_anatomia_test | crudo | 0.105 | [0.078, 0.163] |
| peters_Ti_test − control_anatomia_test | crudo | 0.149 | [0.104, 0.196] |
| run04_60k_test − peters_Ti_test | residuo | -0.194 | [-0.233, -0.184] |

## Sensibilidad K=24, [-1000, 3000] HU

| brazo | modo | pacientes | η²_exc mediana | IC95 bootstrap |
|---|---|---|---|---|
| control_anatomia_test | crudo | 13 | 0.411 | [0.345, 0.453] |
| peters_Ti_test | crudo | 13 | 0.423 | [0.174, 0.504] |
| peters_Ti_test | residuo | 13 | 0.383 | [0.115, 0.455] |
| run04_mejor_test | crudo | 13 | 0.495 | [0.480, 0.537] |
| run04_mejor_test | residuo | 13 | 0.369 | [0.317, 0.450] |
| run04_60k_test | crudo | 13 | 0.507 | [0.437, 0.536] |
| run04_60k_test | residuo | 13 | 0.354 | [0.267, 0.397] |

Diferencias pareadas por paciente (mediana y IC95 bootstrap):

| contraste | modo | mediana | IC95 |
|---|---|---|---|
| run04_mejor_test − peters_Ti_test | residuo | 0.021 | [-0.048, 0.079] |
| run04_mejor_test − peters_Ti_test | crudo | 0.087 | [0.043, 0.208] |
| run04_mejor_test − control_anatomia_test | crudo | 0.070 | [0.032, 0.135] |
| peters_Ti_test − control_anatomia_test | crudo | -0.015 | [-0.106, 0.055] |
| run04_60k_test − peters_Ti_test | residuo | -0.002 | [-0.066, 0.047] |

Figura: `fig_desenrollada.png` (paciente dataset6_CLINIC_0012_data corte 216; real metal_0039 comp. mayor, corte 122; regla: corte central de los cortes con M; 1er paciente de la lista de prueba, semilla 0).

Limites: referencia real = 2 tornillos de metal_0039 (otra anatomía); run05a/b sin volúmenes de prueba en local; η² no distingue rayas de bordes anatómicos radiales; el ruido del difusor baja η² (controles C0).


# Parte 2 — validación 0101/0102 y real metal_0039 (c4)

## C4 — anisotropía angular (exploratorio; protocolo `c4_protocolo.md`)

η²_exc: 0 = isotrópico (halo liso / ruido), mayor = más estructura angular. Corte → semilla → paciente (mediana) → brazo (mediana; rango entre pacientes).

## Principal: K=24, recorte [-500, 1300] HU

| brazo | modo | pacientes/comp. | semillas | η²_exc mediana | rango entre pacientes | std anillo (HU) |
|---|---|---|---|---|---|---|
| real | crudo | 2 | 1/1 | 0.401 | 0.348 – 0.454 | 285 |
| control_anatomia_real | crudo | 2 | 1/1 | 0.279 | 0.217 – 0.341 | 138 |
| control_anatomia | crudo | 2 | 1/1 | 0.319 | 0.178 – 0.459 | 208 |
| peters_Ti | crudo | 2 | 1/1 | 0.331 | 0.200 – 0.463 | 359 |
| peters_Ti | residuo | 2 | 1/1 | 0.340 | 0.277 – 0.404 | 278 |
| run04_mejor | crudo | 2 | 5/5 | 0.320 | 0.144 – 0.497 | 219 |
| run04_mejor | residuo | 2 | 5/5 | 0.237 | 0.151 – 0.322 | 244 |
| run05a_mejor | crudo | 2 | 5/5 | 0.392 | 0.220 – 0.563 | 248 |
| run05a_mejor | residuo | 2 | 5/5 | 0.284 | 0.257 – 0.311 | 256 |
| run05b_mejor | crudo | 2 | 3/1 | 0.306 | 0.118 – 0.495 | 235 |
| run05b_mejor | residuo | 2 | 3/1 | 0.221 | 0.182 – 0.259 | 250 |

## Sensibilidad: K=12, [-500, 1300]

| brazo | modo | pacientes/comp. | semillas | η²_exc mediana | rango entre pacientes | std anillo (HU) |
|---|---|---|---|---|---|---|
| real | crudo | 2 | 1/1 | 0.365 | 0.330 – 0.400 | 285 |
| control_anatomia_real | crudo | 2 | 1/1 | 0.265 | 0.188 – 0.343 | 138 |
| control_anatomia | crudo | 2 | 1/1 | 0.256 | 0.172 – 0.340 | 208 |
| peters_Ti | crudo | 2 | 1/1 | 0.153 | 0.144 – 0.162 | 359 |
| peters_Ti | residuo | 2 | 1/1 | 0.134 | 0.096 – 0.172 | 278 |
| run04_mejor | crudo | 2 | 5/5 | 0.234 | 0.133 – 0.336 | 219 |
| run04_mejor | residuo | 2 | 5/5 | 0.184 | 0.141 – 0.227 | 244 |
| run05a_mejor | crudo | 2 | 5/5 | 0.289 | 0.187 – 0.390 | 248 |
| run05a_mejor | residuo | 2 | 5/5 | 0.219 | 0.198 – 0.240 | 256 |
| run05b_mejor | crudo | 2 | 3/1 | 0.216 | 0.106 – 0.327 | 235 |
| run05b_mejor | residuo | 2 | 3/1 | 0.164 | 0.157 – 0.171 | 250 |

## Sensibilidad: K=48, [-500, 1300]

| brazo | modo | pacientes/comp. | semillas | η²_exc mediana | rango entre pacientes | std anillo (HU) |
|---|---|---|---|---|---|---|
| real | crudo | 2 | 1/1 | 0.382 | 0.337 – 0.427 | 285 |
| control_anatomia_real | crudo | 2 | 1/1 | 0.261 | 0.191 – 0.331 | 138 |
| control_anatomia | crudo | 2 | 1/1 | 0.333 | 0.201 – 0.465 | 208 |
| peters_Ti | crudo | 2 | 1/1 | 0.445 | 0.285 – 0.604 | 359 |
| peters_Ti | residuo | 2 | 1/1 | 0.476 | 0.356 – 0.596 | 278 |
| run04_mejor | crudo | 2 | 5/5 | 0.382 | 0.205 – 0.560 | 219 |
| run04_mejor | residuo | 2 | 5/5 | 0.274 | 0.189 – 0.358 | 244 |
| run05a_mejor | crudo | 2 | 5/5 | 0.411 | 0.251 – 0.571 | 248 |
| run05a_mejor | residuo | 2 | 5/5 | 0.328 | 0.292 – 0.363 | 256 |
| run05b_mejor | crudo | 2 | 3/1 | 0.332 | 0.153 – 0.510 | 235 |
| run05b_mejor | residuo | 2 | 3/1 | 0.264 | 0.207 – 0.321 | 250 |

## Sensibilidad: K=24, [-1000, 3000]

| brazo | modo | pacientes/comp. | semillas | η²_exc mediana | rango entre pacientes | std anillo (HU) |
|---|---|---|---|---|---|---|
| real | crudo | 2 | 1/1 | 0.380 | 0.348 – 0.412 | 289 |
| control_anatomia_real | crudo | 2 | 1/1 | 0.279 | 0.217 – 0.341 | 138 |
| control_anatomia | crudo | 2 | 1/1 | 0.319 | 0.178 – 0.459 | 208 |
| peters_Ti | crudo | 2 | 1/1 | 0.322 | 0.160 – 0.485 | 445 |
| peters_Ti | residuo | 2 | 1/1 | 0.320 | 0.204 – 0.436 | 366 |
| run04_mejor | crudo | 2 | 5/5 | 0.317 | 0.143 – 0.491 | 223 |
| run04_mejor | residuo | 2 | 5/5 | 0.233 | 0.145 – 0.322 | 256 |
| run05a_mejor | crudo | 2 | 5/5 | 0.386 | 0.218 – 0.554 | 252 |
| run05a_mejor | residuo | 2 | 5/5 | 0.281 | 0.248 – 0.314 | 267 |
| run05b_mejor | crudo | 2 | 3/1 | 0.298 | 0.106 – 0.490 | 239 |
| run05b_mejor | residuo | 2 | 3/1 | 0.210 | 0.162 – 0.259 | 268 |

Lectura: ver `c4_protocolo.md`. Limitaciones: real = otro paciente/escáner; 2 tornillos; 2 pacientes sintéticos de validación; run05b con semillas incompletas (0101 s0–2, 0102 s0); η² no distingue rayas de bordes anatómicos radiales; modo crudo incluye anatomía.
