# E6c — barrido del techo de LW (implicancia #39)

Volumenes leidos: 178; con error: 0.
ROI oseo HU > 150; ROI de metal HU > 2500.
Submuestreo determinista a 1,000,000 voxeles por ROI.
MAE del decodificador oraculo (mejor canal por voxel): **cota inferior**.
Sin VAE (#36 sigue abierta). La columna de bits es el sustituto medible de
la precision efectiva de la representacion latente.

## MAE oraculo en ROI de hueso — mediana sobre la cohorte (HU)

| Configuracion | float | 16b | 12b | 8b |
|---|---|---|---|---|
| `pub` | 0.94 | 0.95 | 1.02 | 2.18 |
| `LW3000` | 0.50 | 0.50 | 0.60 | 1.97 |
| `LW4000` | 0.20 | 0.21 | 0.31 | 2.17 |
| `LW6000` | 0.01 | 0.02 | 0.19 | 2.70 |
| `LW10000` | 0.00 | 0.02 | 0.25 | 3.72 |
| `LW20000` | 0.00 | 0.03 | 0.40 | 6.24 |
| `pub+MTW` | 0.00 | 0.01 | 0.08 | 1.31 |
| `pub+asinh` | 0.00 | 0.01 | 0.13 | 2.07 |

## MAE oraculo en ROI de metal — mediana sobre la cohorte (HU)

| Configuracion | float | 16b | 12b | 8b |
|---|---|---|---|---|
| `pub` | 3588.80 | 3588.80 | 3588.80 | 3588.80 |
| `LW3000` | 2630.81 | 2630.82 | 2630.85 | 2631.44 |
| `LW4000` | 1908.24 | 1908.25 | 1908.35 | 1910.03 |
| `LW6000` | 956.96 | 956.97 | 957.24 | 961.52 |
| `LW10000` | 169.08 | 169.12 | 169.70 | 179.04 |
| `LW20000` | 0.00 | 0.08 | 1.28 | 20.62 |
| `pub+MTW` | 0.00 | 0.07 | 1.10 | 17.72 |
| `pub+asinh` | 0.00 | 0.14 | 2.00 | 32.02 |

## Go/No-Go del Objetivo 1 (MAE < 25 HU en hueso)

| Configuracion | float | 16b | 12b | 8b |
|---|---|---|---|---|
| `pub` | 50/178 | 50/178 | 50/178 | 52/178 |
| `LW3000` | 45/178 | 45/178 | 45/178 | 45/178 |
| `LW4000` | 40/178 | 40/178 | 40/178 | 40/178 |
| `LW6000` | 19/178 | 19/178 | 20/178 | 21/178 |
| `LW10000` | 3/178 | 3/178 | 3/178 | 4/178 |
| `LW20000` | 0/178 | 0/178 | 0/178 | 0/178 |
| `pub+MTW` | 0/178 | 0/178 | 0/178 | 0/178 |
| `pub+asinh` | 0/178 | 0/178 | 0/178 | 0/178 |

Celda = volumenes que FALLAN el umbral de 25 HU, sobre el total.

