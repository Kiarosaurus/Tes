# D1 (piezas tamano tornillo) y D2 (sintetico) — 2026-10-13

> Copias versionadas de `outputs/d1_tornillo/d1_resumen.md` (`d1_alcance_rayas.py --vol-max 4000`) y `outputs/d2/d2_resumen.md` (`d2_perfil_sintetico.py`). Implicancia: #176.

## D1 — alcance del artefacto real por anillo (#176)

Generado por `d1_alcance_rayas.py`. 18 pacientes con perfil (13 de nulo); entrenamiento de run04 y validacion, componentes de 500 a 4000 mm3. Exceso = amplitud de Peters (5 % superior - 5 % inferior) en el corte con metal menos en un corte de referencia sin metal a 15-40 mm. Nulo = lo mismo entre dos cortes sin metal.

| anillo (mm) | n | exceso mediano | IC90 | nulo mediano | IC90 nulo |
|---|---|---|---|---|---|
| 0-2 | 18 | 1930 | [1605, 2157] | -28 | [-209, 25] |
| 2-4 | 18 | 1199 | [1031, 1453] | -57 | [-195, 32] |
| 4-6 | 18 | 765 | [642, 907] | -10 | [-49, 99] |
| 6-8 | 18 | 473 | [341, 543] | -18 | [-202, 23] |
| 8-10 | 18 | 174 | [93, 304] | -53 | [-293, 55] |
| 10-12 | 18 | 11 | [-32, 198] | -42 | [-244, 102] |
| 12-14 | 18 | 48 | [-60, 149] | -110 | [-248, 68] |
| 14-16 | 18 | 44 | [-46, 109] | 14 | [-384, 197] |
| 16-18 | 18 | 42 | [-62, 67] | 23 | [-247, 145] |
| 18-20 | 18 | 14 | [-48, 104] | -36 | [-77, 35] |
| 20-22 | 18 | 32 | [-5, 99] | 28 | [-112, 105] |
| 22-24 | 18 | 58 | [1, 131] | -3 | [-126, 169] |
| 24-26 | 18 | 19 | [-39, 81] | 20 | [-119, 99] |
| 26-28 | 18 | -17 | [-86, 63] | -31 | [-147, 22] |
| 28-30 | 18 | -40 | [-88, 39] | -41 | [-57, 38] |
| 30-32 | 18 | -53 | [-102, -14] | -34 | [-58, 30] |
| 32-34 | 18 | -64 | [-84, 21] | 61 | [-41, 78] |
| 34-36 | 18 | -38 | [-63, 5] | 23 | [-139, 80] |
| 36-38 | 18 | -40 | [-91, 4] | 75 | [-110, 101] |
| 38-40 | 18 | -27 | [-105, 38] | -1 | [-140, 63] |
| 40-42 | 18 | -41 | [-91, 14] | -52 | [-203, 37] |
| 42-44 | 18 | -27 | [-72, 10] | -42 | [-132, 66] |
| 44-46 | 18 | -28 | [-66, -0] | -9 | [-62, 170] |
| 46-48 | 18 | -49 | [-84, 15] | -27 | [-182, 76] |
| 48-50 | 18 | -62 | [-140, -19] | -21 | [-107, 119] |
| 50-52 | 18 | -48 | [-161, -21] | 16 | [-71, 85] |
| 52-54 | 18 | -39 | [-131, -4] | 55 | [-131, 87] |
| 54-56 | 18 | -69 | [-146, -37] | 37 | [-131, 141] |
| 56-58 | 18 | -74 | [-137, -14] | 83 | [-43, 183] |
| 58-60 | 18 | -26 | [-76, 26] | 63 | [-56, 201] |

**Anillo mas lejano cuyo IC90 inferior supera el IC90 superior del nulo: hasta 10 mm** (referencia: `B_delta` = 12 mm).

Limites: la referencia es otro corte (la anatomia cambia); solo cortes sin otro metal; la amplitud por anillo mezcla rayas claras y oscuras con la variacion anatomica del anillo.

## D2 — perfil radial del artefacto sintetico frente al real (#176)

Generado por `d2_perfil_sintetico.py`. Sintetico: validacion (`0101`, `0102`), 5 semillas, pose corregida, referencia exacta (original). Real: D1 (40 pacientes de entrenamiento y validacion, referencia aproximada). Exceso de amplitud de Peters por anillo, HU.

| anillo (mm) | run04_mejor (mediana 0101/0102) | run04_60k (mediana 0101/0102) | real D1 [IC90] |
|---|---|---|---|
| 0-2 | 1697 | 1463 | 2381.9 [2084.1, 2781.7] |
| 2-4 | 488 | 428 | 1462.2 [1305.6, 1635.5] |
| 4-6 | 97 | 59 | 955.8 [864.5, 1051.3] |
| 6-8 | -65 | -68 | 579.7 [473.6, 672.2] |
| 8-10 | -40 | -101 | 399.0 [316.1, 504.2] |
| 10-12 | -4 | -39 | 323.9 [230.1, 396.8] |
| 12-14 | -9 | -19 | 222.5 [114.2, 354.8] |
| 14-16 | 4 | -8 | 170.1 [97.6, 209.8] |
| 16-18 | 4 | -9 | 104.8 [69.3, 145.6] |
| 18-20 | 5 | -3 | 108.5 [44.9, 142.2] |
| 20-22 | 4 | -1 | 83.2 [10.2, 139.4] |
| 22-24 | 10 | 0 | 90.8 [40.0, 133.6] |
| 24-26 | 1 | -0 | 29.0 [-23.6, 92.6] |
| 26-28 | 0 | -1 | -0.0 [-33.1, 67.1] |
| 28-30 | -1 | -2 | 14.8 [-39.7, 39.2] |
