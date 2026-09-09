# E6a — codificacion multi-ventana sola (Objetivo 1, Go/No-Go)

Volumenes leidos: 178; con error: 0.
ROI oseo: HU > 150 (bone integrity de `peters2025hybrid`).
ROI metal: HU > 2500.
Ventanas LW [-1000, 2000], MW [-320, 480], SW [-160, 240] HU.
Sin VAE: esto es una **cota inferior** del error del sistema completo.

## MAE en ROI de hueso — mediana [min-max] sobre la cohorte

| Profundidad | LW | MW | SW | oraculo |
|---|---|---|---|---|
| float | 0.95 [0.00-274.49] | 107.63 [40.69-468.81] | 218.19 [119.76-572.61] | 0.95 [0.00-274.49] |
| 16b | 0.96 [0.01-274.51] | 107.63 [40.69-468.82] | 218.20 [119.76-572.61] | 0.96 [0.00-274.50] |
| 8b | 3.88 [2.92-277.22] | 108.19 [41.34-469.36] | 218.32 [119.90-572.73] | 2.18 [1.04-275.57] |

## MAE en ROI de metal — mediana [min-max] sobre la cohorte

| Profundidad | LW | MW | SW | oraculo |
|---|---|---|---|---|
| float | 3588.80 [540.00-6843.72] | 5108.80 [2060.00-8363.72] | 5348.80 [2300.00-8603.72] | 3588.80 [540.00-6843.72] |
| 16b | 3588.80 [540.00-6843.72] | 5108.80 [2060.00-8363.72] | 5348.80 [2300.00-8603.72] | 3588.80 [540.00-6843.72] |
| 8b | 3588.80 [540.00-6843.72] | 5108.80 [2060.00-8363.72] | 5348.80 [2300.00-8603.72] | 3588.80 [540.00-6843.72] |

## Veredicto frente al umbral de 25 HU en hueso

- **float**: la cota del oraculo supera 25 HU en **50 de 178** volumenes (mediana 0.95 HU).
- **16b**: la cota del oraculo supera 25 HU en **50 de 178** volumenes (mediana 0.96 HU).
- **8b**: la cota del oraculo supera 25 HU en **52 de 178** volumenes (mediana 2.18 HU).

## Recorte: fraccion de voxeles oseos sobre el techo de LW (2000 HU)

- dataset6: mediana 0.0000%, maximo 1.3107%.
- dataset7: mediana 1.2398%, maximo 6.5476%.

Ningun decodificador recupera un voxel recortado en las tres ventanas.
La cota del oraculo asume un decodificador que elige el mejor canal por voxel;
un VAE real solo puede empeorarla.
