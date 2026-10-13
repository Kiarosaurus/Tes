# D1 — alcance del artefacto real por anillo (#176)

> Copia versionada de `outputs/d1/d1_resumen.md` (2026-10-13). Script: `d1_alcance_rayas.py`. Implicancia: #176 (adenda D1).

Generado por `d1_alcance_rayas.py`. 40 pacientes con perfil (20 de nulo); entrenamiento de run04 y validacion. Exceso = amplitud de Peters (5 % superior - 5 % inferior) en el corte con metal menos en un corte de referencia sin metal a 15-40 mm. Nulo = lo mismo entre dos cortes sin metal.

| anillo (mm) | n | exceso mediano | IC90 | nulo mediano | IC90 nulo |
|---|---|---|---|---|---|
| 0-2 | 38 | 2382 | [2084, 2782] | -33 | [-147, 0] |
| 2-4 | 38 | 1462 | [1306, 1636] | -36 | [-186, 1] |
| 4-6 | 38 | 956 | [864, 1051] | -19 | [-150, 15] |
| 6-8 | 38 | 580 | [474, 672] | -25 | [-104, 4] |
| 8-10 | 38 | 399 | [316, 504] | -63 | [-151, 25] |
| 10-12 | 38 | 324 | [230, 397] | -53 | [-216, 54] |
| 12-14 | 38 | 223 | [114, 355] | -123 | [-248, -16] |
| 14-16 | 38 | 170 | [98, 210] | -26 | [-193, 39] |
| 16-18 | 38 | 105 | [69, 146] | -31 | [-140, 81] |
| 18-20 | 38 | 108 | [45, 142] | -54 | [-92, -2] |
| 20-22 | 38 | 83 | [10, 139] | 8 | [-106, 60] |
| 22-24 | 39 | 91 | [40, 134] | 6 | [-108, 81] |
| 24-26 | 39 | 29 | [-24, 93] | 27 | [-81, 151] |
| 26-28 | 39 | -0 | [-33, 67] | 6 | [-40, 92] |
| 28-30 | 39 | 15 | [-40, 39] | -18 | [-46, 64] |
| 30-32 | 39 | 4 | [-31, 34] | 6 | [-55, 97] |
| 32-34 | 39 | 21 | [-46, 43] | 61 | [3, 78] |
| 34-36 | 39 | 14 | [-8, 60] | 80 | [-93, 108] |
| 36-38 | 39 | 0 | [-44, 34] | 94 | [-44, 158] |
| 38-40 | 39 | -19 | [-94, 22] | 36 | [-97, 101] |
| 40-42 | 39 | -27 | [-98, 9] | 3 | [-160, 64] |
| 42-44 | 39 | -37 | [-98, -0] | 10 | [-132, 68] |
| 44-46 | 39 | -11 | [-61, 17] | -11 | [-40, 162] |
| 46-48 | 39 | -24 | [-63, 5] | 31 | [-38, 76] |
| 48-50 | 39 | -2 | [-111, 16] | -1 | [-45, 119] |
| 50-52 | 39 | -28 | [-68, -2] | -10 | [-64, 81] |
| 52-54 | 40 | -34 | [-114, 16] | 60 | [-131, 87] |
| 54-56 | 40 | -35 | [-129, -4] | 15 | [-84, 102] |
| 56-58 | 40 | -58 | [-117, 16] | 84 | [22, 129] |
| 58-60 | 40 | -15 | [-63, 14] | 88 | [-31, 179] |

**Anillo mas lejano cuyo IC90 inferior supera el IC90 superior del nulo: hasta 20 mm** (referencia: `B_delta` = 12 mm).

Limites: la referencia es otro corte (la anatomia cambia); solo cortes sin otro metal; la amplitud por anillo mezcla rayas claras y oscuras con la variacion anatomica del anillo.
