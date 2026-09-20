# P1 — compuerta del Objetivo 1: VAE de SD 1.5 preentrenado frente a decodificador afinado

Filas: 68; con error: 0. Modelos: afinado, sd15. Particiones: test. Generado por `p1_decodificador_sd15.py`.

**Regla preinscrita (autora, 2026-09-17):** hay Go si ALGUNA combinacion modelo {sd15, afinado} x configuracion tiene **media por paciente del MAE en hueso con `vae regla` < 25 HU** sobre TODOS los pacientes de test. IC95, mediana, fallos por paciente, RMSE, metal, `bdelta` y subgrupos NO deciden.

## Controles

| Control | coinciden | total |
|---|---|---|
| decodificador afinado distinto del preentrenado | 3 | 3 |
| encoder congelado (hash base = hash al entrenar) | 3 | 3 |
| identidad frente a E6c float | 165 | 165 |
| sd15 frente a E6b | 330 | 330 |

## Veredicto del Go/No-Go (test)

| Modelo | Configuracion | n | media MAE hueso regla | IC95 bootstrap | mediana | pacientes >= 25 | RMSE media | Pasa |
|---|---|---|---|---|---|---|---|---|
| sd15 | `pub` | 34 | 160.13 | [142.42, 180.62] | 136.61 | 34/34 | 407.53 | NO |
| sd15 | `LW20000` | 34 | 209.39 | [191.91, 228.62] | 190.89 | 34/34 | 510.77 | NO |
| sd15 | `pub+asinh` | 34 | 164.76 | [148.81, 182.87] | 146.60 | 34/34 | 397.34 | NO |
| afinado | `pub` | 34 | 72.91 | [59.37, 89.02] | 53.29 | 34/34 | 278.68 | NO |
| afinado | `LW20000` | 34 | 77.03 | [70.12, 84.65] | 70.41 | 34/34 | 193.56 | NO |
| afinado | `pub+asinh` | 34 | 61.72 | [55.12, 68.99] | 53.07 | 34/34 | 171.94 | NO |

**Resultado: NO-GO.** Ninguna combinacion pasa: no hay Objetivo 3.

## MAE en ROI hueso (test): media / mediana por paciente, HU

| Modelo | Configuracion | identidad oraculo | identidad regla | vae oraculo | vae regla |
|---|---|---|---|---|---|
| sd15 | `pub` | 21.80 / 0.14 (n=34) | 21.80 / 0.14 (n=34) | 97.55 / 78.14 (n=34) | 160.13 / 136.61 (n=34) |
| sd15 | `LW20000` | 0.00 / 0.00 (n=34) | 0.00 / 0.00 (n=34) | 121.60 / 111.84 (n=34) | 209.39 / 190.89 (n=34) |
| sd15 | `pub+asinh` | 0.00 / 0.00 (n=34) | 0.00 / 0.00 (n=34) | 104.31 / 89.30 (n=34) | 164.76 / 146.60 (n=34) |
| afinado | `pub` | 21.80 / 0.14 (n=34) | 21.80 / 0.14 (n=34) | 63.56 / 43.36 (n=34) | 72.91 / 53.29 (n=34) |
| afinado | `LW20000` | 0.00 / 0.00 (n=34) | 0.00 / 0.00 (n=34) | 49.65 / 43.80 (n=34) | 77.03 / 70.41 (n=34) |
| afinado | `pub+asinh` | 0.00 / 0.00 (n=34) | 0.00 / 0.00 (n=34) | 52.55 / 44.27 (n=34) | 61.72 / 53.07 (n=34) |

## MAE en ROI metal (test): media / mediana por paciente, HU

| Modelo | Configuracion | identidad oraculo | identidad regla | vae oraculo | vae regla |
|---|---|---|---|---|---|
| sd15 | `pub` | 3325.59 / 3606.11 (n=21) | 3325.59 / 3606.11 (n=21) | 3875.19 / 4385.18 (n=21) | 4719.00 / 5232.57 (n=21) |
| sd15 | `LW20000` | 0.09 / 0.00 (n=21) | 0.09 / 0.00 (n=21) | 2889.40 / 2993.96 (n=21) | 4205.42 / 4376.01 (n=21) |
| sd15 | `pub+asinh` | 0.09 / 0.00 (n=21) | 0.09 / 0.00 (n=21) | 3150.58 / 2978.44 (n=21) | 4212.61 / 4524.92 (n=21) |
| afinado | `pub` | 3325.59 / 3606.11 (n=21) | 3325.59 / 3606.11 (n=21) | 3459.44 / 3900.82 (n=21) | 3775.62 / 4320.38 (n=21) |
| afinado | `LW20000` | 0.09 / 0.00 (n=21) | 0.09 / 0.00 (n=21) | 1676.84 / 1509.87 (n=21) | 2065.01 / 2109.08 (n=21) |
| afinado | `pub+asinh` | 0.09 / 0.00 (n=21) | 0.09 / 0.00 (n=21) | 1917.88 / 1784.60 (n=21) | 2154.20 / 2071.93 (n=21) |

## MAE en ROI bdelta (test): media / mediana por paciente, HU

| Modelo | Configuracion | identidad oraculo | identidad regla | vae oraculo | vae regla |
|---|---|---|---|---|---|
| sd15 | `pub` | 15.25 / 3.82 (n=21) | 15.25 / 3.82 (n=21) | 69.16 / 61.91 (n=21) | 114.73 / 107.78 (n=21) |
| sd15 | `LW20000` | 13.71 / 2.39 (n=21) | 13.71 / 2.39 (n=21) | 99.31 / 87.70 (n=21) | 147.77 / 141.10 (n=21) |
| sd15 | `pub+asinh` | 13.71 / 2.39 (n=21) | 13.71 / 2.39 (n=21) | 78.18 / 69.21 (n=21) | 118.27 / 104.96 (n=21) |
| afinado | `pub` | 15.25 / 3.82 (n=21) | 15.25 / 3.82 (n=21) | 53.99 / 48.91 (n=21) | 64.62 / 60.51 (n=21) |
| afinado | `LW20000` | 13.71 / 2.39 (n=21) | 13.71 / 2.39 (n=21) | 67.54 / 52.20 (n=21) | 88.72 / 79.44 (n=21) |
| afinado | `pub+asinh` | 13.71 / 2.39 (n=21) | 13.71 / 2.39 (n=21) | 59.53 / 51.28 (n=21) | 69.70 / 63.72 (n=21) |

## RMSE en ROI hueso (test): media / mediana por paciente, HU

| Modelo | Configuracion | identidad oraculo | identidad regla | vae oraculo | vae regla |
|---|---|---|---|---|---|
| sd15 | `pub` | 218.50 / 15.12 (n=34) | 218.50 / 15.12 (n=34) | 316.71 / 144.30 (n=34) | 407.53 / 235.86 (n=34) |
| sd15 | `LW20000` | 0.13 / 0.00 (n=34) | 0.13 / 0.00 (n=34) | 307.43 / 228.42 (n=34) | 510.77 / 425.01 (n=34) |
| sd15 | `pub+asinh` | 0.13 / 0.00 (n=34) | 0.13 / 0.00 (n=34) | 296.14 / 176.04 (n=34) | 397.34 / 261.65 (n=34) |
| afinado | `pub` | 218.50 / 15.12 (n=34) | 218.50 / 15.12 (n=34) | 259.81 / 79.88 (n=34) | 278.68 / 102.20 (n=34) |
| afinado | `LW20000` | 0.13 / 0.00 (n=34) | 0.13 / 0.00 (n=34) | 135.56 / 76.47 (n=34) | 193.56 / 113.45 (n=34) |
| afinado | `pub+asinh` | 0.13 / 0.00 (n=34) | 0.13 / 0.00 (n=34) | 150.19 / 81.37 (n=34) | 171.94 / 94.96 (n=34) |

## RMSE en ROI metal (test): media / mediana por paciente, HU

| Modelo | Configuracion | identidad oraculo | identidad regla | vae oraculo | vae regla |
|---|---|---|---|---|---|
| sd15 | `pub` | 4053.92 / 4595.54 (n=21) | 4053.92 / 4595.54 (n=21) | 4533.80 / 5192.47 (n=21) | 5323.55 / 5960.85 (n=21) |
| sd15 | `LW20000` | 2.91 / 0.00 (n=21) | 2.91 / 0.00 (n=21) | 3545.28 / 3774.91 (n=21) | 4868.71 / 5529.07 (n=21) |
| sd15 | `pub+asinh` | 2.91 / 0.00 (n=21) | 2.91 / 0.00 (n=21) | 3845.89 / 3959.07 (n=21) | 4908.80 / 5477.98 (n=21) |
| afinado | `pub` | 4053.92 / 4595.54 (n=21) | 4053.92 / 4595.54 (n=21) | 4150.68 / 4754.05 (n=21) | 4498.77 / 5193.97 (n=21) |
| afinado | `LW20000` | 2.91 / 0.00 (n=21) | 2.91 / 0.00 (n=21) | 2135.92 / 2061.45 (n=21) | 2734.48 / 2696.28 (n=21) |
| afinado | `pub+asinh` | 2.91 / 0.00 (n=21) | 2.91 / 0.00 (n=21) | 2448.15 / 2278.31 (n=21) | 2784.43 / 2544.39 (n=21) |

## RMSE en ROI bdelta (test): media / mediana por paciente, HU

| Modelo | Configuracion | identidad oraculo | identidad regla | vae oraculo | vae regla |
|---|---|---|---|---|---|
| sd15 | `pub` | 75.41 / 34.24 (n=21) | 75.41 / 34.24 (n=21) | 157.88 / 139.74 (n=21) | 258.25 / 249.73 (n=21) |
| sd15 | `LW20000` | 67.13 / 21.13 (n=21) | 67.13 / 21.13 (n=21) | 225.67 / 219.75 (n=21) | 349.35 / 349.67 (n=21) |
| sd15 | `pub+asinh` | 67.13 / 21.13 (n=21) | 67.13 / 21.13 (n=21) | 182.92 / 171.57 (n=21) | 277.48 / 260.14 (n=21) |
| afinado | `pub` | 75.41 / 34.24 (n=21) | 75.41 / 34.24 (n=21) | 124.68 / 105.98 (n=21) | 158.58 / 140.35 (n=21) |
| afinado | `LW20000` | 67.13 / 21.13 (n=21) | 67.13 / 21.13 (n=21) | 160.82 / 141.31 (n=21) | 228.50 / 216.07 (n=21) |
| afinado | `pub+asinh` | 67.13 / 21.13 (n=21) | 67.13 / 21.13 (n=21) | 144.15 / 123.29 (n=21) | 176.96 / 164.56 (n=21) |

## Hueso con `vae regla` por subgrupo (test, descriptivo): media / mediana, HU

| Modelo | Configuracion | Dataset | Metal | n | MAE | RMSE |
|---|---|---|---|---|---|---|
| sd15 | `pub` | dataset6 | no | 14 | 135.91 / 136.24 | 224.40 / 225.19 |
| sd15 | `pub` | dataset6 | si | 6 | 122.10 / 117.55 | 209.88 / 206.29 |
| sd15 | `pub` | dataset7 | si | 14 | 200.66 / 197.50 | 675.36 / 636.71 |
| sd15 | `LW20000` | dataset6 | no | 14 | 188.70 / 180.58 | 388.79 / 381.37 |
| sd15 | `LW20000` | dataset6 | si | 6 | 174.15 / 171.24 | 372.61 / 362.07 |
| sd15 | `LW20000` | dataset7 | si | 14 | 245.18 / 255.02 | 691.97 / 672.50 |
| sd15 | `pub+asinh` | dataset6 | no | 14 | 145.20 / 143.56 | 248.04 / 255.35 |
| sd15 | `pub+asinh` | dataset6 | si | 6 | 128.99 / 122.27 | 228.57 / 221.70 |
| sd15 | `pub+asinh` | dataset7 | si | 14 | 199.65 / 208.55 | 618.98 / 622.50 |
| afinado | `pub` | dataset6 | no | 14 | 52.26 / 50.09 | 85.67 / 80.52 |
| afinado | `pub` | dataset6 | si | 6 | 46.13 / 44.61 | 89.13 / 85.56 |
| afinado | `pub` | dataset7 | si | 14 | 105.03 / 90.30 | 552.93 / 524.59 |
| afinado | `LW20000` | dataset6 | no | 14 | 67.91 / 66.97 | 109.05 / 108.68 |
| afinado | `LW20000` | dataset6 | si | 6 | 60.91 / 60.42 | 104.32 / 103.12 |
| afinado | `LW20000` | dataset7 | si | 14 | 93.06 / 92.67 | 316.31 / 337.45 |
| afinado | `pub+asinh` | dataset6 | no | 14 | 53.72 / 51.10 | 85.46 / 82.51 |
| afinado | `pub+asinh` | dataset6 | si | 6 | 46.99 / 46.15 | 84.03 / 81.85 |
| afinado | `pub+asinh` | dataset7 | si | 14 | 76.03 / 80.58 | 296.10 / 346.72 |

## Curvas de entrenamiento (ultimo registro; `val` no elige checkpoint)

| Configuracion | paso | l1 train | l1 val | val hueso regla MAE (paso 0 -> final) | s por paso | mem GB |
|---|---|---|---|---|---|---|
| `pub` | 30000 | 0.012194 | 0.011857 | 151.641 -> 70.31 | 1.249 | 24.75 |
| `LW20000` | 30000 | 0.010811 | 0.010423 | 208.475 -> 79.985 | 1.246 | 24.56 |
| `pub+asinh` | 30000 | 0.011908 | 0.011325 | 156.016 -> 61.844 | 1.259 | 24.56 |

Tiempo por fila: mediana 177 s; total 3.22 h.
