# B mínima (ajuste fino con término de amplitud angular) — resultados en validación (EXPLORATORIO, POST-HOC)

Reglas: `docs/01-decisiones.md` 2026-11-20 (3), (4), (5), (9), (10). Brazos: **control de ajuste fino** `b_min_l0` (λ = 0) y **B** `b_min_l0.8_t1000` (λ = 0.8, tmax = 1000), ambos de `run04_mejor` (paso 16 500), 3 000 pasos, **en la T4** (no comparables con run04 de la A100/A6000; el contraste válido es B − control). Evaluación: `a15_val_ckpt.sbatch` (jobs 64401 y 64402), 0101/0102, 5 semillas, 50 pasos, eta 0, delta 0.03 (no recalibrado). Integridad de los 64 `.nii.gz` verificada con `gzip -t`.

## Veredicto por la regla fijada (decisión (5).3 y (4).2)
| criterio | umbral | control λ=0 | B λ=0.8 | B − control | ¿cumple? |
|---|---|---|---|---|---|
| (i) C4 K=48, residuo, η²_exc | ≥ +0.05 | 0.299 | 0.337 | **+0.038** (0101 +0.069; 0102 +0.008) | **no** |
| guarda K=12, residuo | no baja > 0.05 | 0.206 | 0.220 | +0.014 | sí |
| (ii) cáscaras críticas con p95 dentro de la envolvente real (de 7) | B ≥ control | 0 | 3 (6, 8 y 9 mm) | +3 | sí |
| (iii) D2: desviación en 0–2 mm = \|exceso − 1930\| ≤ 279.6 HU | ≤ 279.6 | 585 (exceso 1345) | **26** (exceso 1904) | | sí (B); el control no |

**Según la regla fijada, B «no mejora»** (falla (i)); (ii) y (iii) se cumplen. Se informa igual, con todas las cifras.

## Datos descriptivos adicionales (no son parte del criterio)
- Error medio E de `v2_eleccion.py` en 2–10 mm (referencia D1 tornillo 1199/765/473/174): control 582.0 HU; **B 274.8 HU** (run04_mejor 532.8; run05a 418.2; run05b 367.0; eta 100:0.3 361.5).
- C4 K=24 residuo: control 0.252; B 0.314 (+0.062); Peters 0.340. K=48: Peters 0.476 (B 0.337): **la brecha de escala fina frente a Peters no se cierra**.
- a17 (24 cáscaras comparables, p50+p95 dentro de la envolvente real): control 7; B 14.
- Lectura: el término con λ = 0.8 sube sobre todo el perfil **radial** (D2 y p95), y solo modestamente la estructura angular fina. No es equivalencia ni con Peters ni con lo real.

## Limitaciones
2 pacientes de validación; un checkpoint; un λ; hardware T4 (la curva del control separa el efecto del ajuste fino); N = 2 tornillos reales; criterio (c) visual a ciegas **pendiente** (la autora puntúa).

# Parte 1 — C4 (validación)
## C4 sobre variantes (incluye run04_mejor y Peters como referencia) (validación 0101/0102; exploratorio, N = 2 pacientes)

η²_exc por paciente (mediana corte → semilla); entre paréntesis, los dos pacientes. Ventana [-500, 1300] HU.

## K = 12

| brazo | modo | η²_exc mediana | por paciente |
|---|---|---|---|
| run04_mejor | residuo | 0.184 | 0101 0.227, 0102 0.141 |
| b_min_l0 | residuo | 0.206 | 0101 0.224, 0102 0.187 |
| b_min_l0.8_t1000 | residuo | 0.220 | 0101 0.242, 0102 0.198 |
| peters_Ti | residuo | 0.134 | 0101 0.096, 0102 0.172 |
| run04_mejor | crudo | 0.234 | 0101 0.336, 0102 0.133 |
| b_min_l0 | crudo | 0.228 | 0101 0.278, 0102 0.179 |
| b_min_l0.8_t1000 | crudo | 0.250 | 0101 0.328, 0102 0.173 |
| control_anatomia | crudo | 0.256 | 0101 0.340, 0102 0.172 |

## K = 24

| brazo | modo | η²_exc mediana | por paciente |
|---|---|---|---|
| run04_mejor | residuo | 0.237 | 0101 0.322, 0102 0.151 |
| b_min_l0 | residuo | 0.252 | 0101 0.281, 0102 0.224 |
| b_min_l0.8_t1000 | residuo | 0.314 | 0101 0.385, 0102 0.243 |
| peters_Ti | residuo | 0.340 | 0101 0.404, 0102 0.277 |
| run04_mejor | crudo | 0.320 | 0101 0.497, 0102 0.144 |
| b_min_l0 | crudo | 0.317 | 0101 0.422, 0102 0.212 |
| b_min_l0.8_t1000 | crudo | 0.347 | 0101 0.496, 0102 0.199 |
| control_anatomia | crudo | 0.319 | 0101 0.459, 0102 0.178 |

## K = 48

| brazo | modo | η²_exc mediana | por paciente |
|---|---|---|---|
| run04_mejor | residuo | 0.274 | 0101 0.358, 0102 0.189 |
| b_min_l0 | residuo | 0.299 | 0101 0.332, 0102 0.266 |
| b_min_l0.8_t1000 | residuo | 0.337 | 0101 0.401, 0102 0.274 |
| peters_Ti | residuo | 0.476 | 0101 0.596, 0102 0.356 |
| run04_mejor | crudo | 0.382 | 0101 0.560, 0102 0.205 |
| b_min_l0 | crudo | 0.361 | 0101 0.462, 0102 0.261 |
| b_min_l0.8_t1000 | crudo | 0.380 | 0101 0.528, 0102 0.232 |
| control_anatomia | crudo | 0.333 | 0101 0.465, 0102 0.201 |

Limites: 2 pacientes de validación; 1 checkpoint; Peters = referencia física, no «lo real».


# Parte 2 — D2

# D2 — perfil radial del artefacto sintetico frente al real (#176)

Generado por `d2_perfil_sintetico.py`. Sintetico: validacion (`0101`, `0102`), 5 semillas, pose corregida, referencia exacta (original). Real: D1 (40 pacientes de entrenamiento y validacion, referencia aproximada). Exceso de amplitud de Peters por anillo, HU.

| anillo (mm) | b_min_l0 (mediana 0101/0102) | b_min_l0.8_t1000 (mediana 0101/0102) | real D1 [IC90] |
|---|---|---|---|
| 0-2 | 1345 | 1904 | 2381.9 [2084.1, 2781.7] |
| 2-4 | 424 | 812 | 1462.2 [1305.6, 1635.5] |
| 4-6 | 18 | 416 | 955.8 [864.5, 1051.3] |
| 6-8 | -72 | 196 | 579.7 [473.6, 672.2] |
| 8-10 | -87 | 88 | 399.0 [316.1, 504.2] |
| 10-12 | -90 | -10 | 323.9 [230.1, 396.8] |
| 12-14 | -30 | -3 | 222.5 [114.2, 354.8] |
| 14-16 | -5 | 4 | 170.1 [97.6, 209.8] |
| 16-18 | -2 | 5 | 104.8 [69.3, 145.6] |
| 18-20 | 0 | 9 | 108.5 [44.9, 142.2] |
| 20-22 | 2 | 7 | 83.2 [10.2, 139.4] |
| 22-24 | 3 | 8 | 90.8 [40.0, 133.6] |
| 24-26 | 1 | 4 | 29.0 [-23.6, 92.6] |
| 26-28 | -3 | -1 | -0.0 [-33.1, 67.1] |
| 28-30 | -0 | 1 | 14.8 [-39.7, 39.2] |


# Parte 3 — cáscaras críticas (A28)

# Veredicto etapa 0 de v3 (exploratorio, post-hoc)

Regla: 01-decisiones.md 2026-11-20. Criterio (a) desde los CSV; (b) 0-2 mm requiere NIfTI (no calculado).

## Control de validez

Control NO evaluado (falta --control o la variante p50_e0). **El barrido no es interpretable sin el.**

## Cascaras criticas con p95 dentro de la envolvente real

| variante | pacientes | dentro (de 7) | cascaras (mm) | criterio (a) >= 4 | criterio (b) 0-2 mm |
|---|---|---|---|---|---|
| b_min_l0 | 2 | 0 | - | no | n/a |
| b_min_l0.8_t1000 | 2 | 3 | 6,8,9 | no | n/a |

## p95 sintetico frente a la envolvente real (HU), cascaras criticas

| r (mm) | real lo | real hi | b_min_l0 | b_min_l0.8_t1000 |
|---|---|---|---|---|
| 4-5 | 759 | 832 | 603 | 832 |
| 5-6 | 691 | 759 | 571 | 769 |
| 6-7 | 596 | 775 | 530 | 720 |
| 8-9 | 516 | 714 | 445 | 573 |
| 9-10 | 496 | 632 | 422 | 514 |
| 10-11 | 533 | 659 | 414 | 462 |
| 11-12 | 487 | 629 | 396 | 393 |

Limites: 2 pacientes de validacion; un checkpoint; el criterio (b) no esta evaluado; resultado exploratorio.
