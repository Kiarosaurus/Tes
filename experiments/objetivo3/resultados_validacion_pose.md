# Validacion del Objetivo 3 con la pose corregida (#173) — 2026-10-12

Copia versionada de lo que producen `a17`, `a21` y `a20` sobre las salidas de `a15_cadena_pose.sbatch` (jobs 56243
`run04_mejor` con 0.030 y 56244 `run04_60k` con 0.050, rtxa6000 g002) y `a19_pose.sbatch` (job 56245, etapa `val`,
n006). Los tres jobs terminaron `COMPLETED 0:0`. Sus logs se perdieron (truncados por un `scp`); el CONTROL pose se
recalculo en local: 15 de 15 PASAN (`outputs/obj3_pose/logs/control_pose_local.txt`; `0101` 84 frente a 68 HU, igual
al log original). Receptores: `0101` y `0102`. Referencia real: 2 tornillos aislados de `metal_0039`.

Sustituye a `../obsoletos/objetivo3/a17_cotejo_resultado_run04.md`, `a20_resultados_run04.md` y `a21_resultado.md`
(pose espejada). Implicancias: #174 (cotejo y material, DECIDIDA) y #175 (`Delta`).

## 1. Cotejo de punto de control (`a17 --paso-mm 1`)

Salida: `outputs/obj3_pose/a17_paso1mm/a17_cotejo.md`. Entrada: `outputs/obj3_pose/cotejo/combinado/` (los
`a15_<caso>_cotejo.csv` de los dos puntos de control, concatenados).

| punto de control | dentro p50 | dentro p95 | dentro total (de 24) | M p50 | M p95 | dist. hist. | rango max. entre semillas |
|---|---|---|---|---|---|---|---|
| `run04_mejor` | 9 | 4 | **13** | 3245 | 4856 | 648 | 393 |
| `run04_60k` | 3 | 4 | 7 | 3402 | 4848 | 497 | 270 |

Gana `run04_mejor` (confirmado por la autora, #174 (a)). p95 bajo lo real en 7 de 12 cascaras en los dos; p50 sobre
lo real en 3 (mejor) y 9 (60k). Real: `M` p50 3838 / 3092, p95 5262 / 5304 HU.

## 2. Material del brazo fisico (`a21`)

Salida: `outputs/obj3_pose/a21/a21_cotejo_material.md` (`--dir-a19 outputs/obj3_pose/peters_val`).

| material | dentro total (de 24) | bajo | sobre | M p50 | M p75 | M p95 | dist. hist. |
|---|---|---|---|---|---|---|---|
| Ti | **2** | 0 | 22 | 4462 | 5848 | 8027 | 3741 |
| Fe | 0 | 0 | 24 | 7036 | 9522 | 15398 | 13686 |

Gana Ti por la regla. Lectura de la autora (#174 (b)): ningun material reproduce lo real; Ti es el menos alejado.

## 3. `streak amplitude` en validacion y `Delta` (`a20`)

Salida: `outputs/obj3_pose/a20_val/` (`a20_ea2.csv`, `a20_delta_run04_mejor.json`, `a20_delta_run04_60k.json`).

| brazo | `0101` | `0102` |
|---|---|---|
| difusor `run04_mejor`, semillas 0-4 | 1361, 1269, 1248, 1069, 1226 (mediana 1248) | 1216, 1232, 1182, 1151, 1131 (mediana 1182) |
| difusor `run04_60k`, semillas 0-4 | 1254, 1195, 1164, 1094, 1132 (mediana 1164) | 1187, 1166, 1163, 1116, 1131 (mediana 1163) |
| Peters Ti, A / B | 1885 / 1877 | 1300 / 1273 |
| Peters Fe, A / B | 5246 / 5239 | 2163 / 2168 |

Fraccion de la ROI en el suelo de -1000 HU: 0.000 en todas las semillas.

| punto de control | `s` por caso (rango entre semillas) | `s` | `r` (Fe, \|A-B\| promedio) | **`Delta`** |
|---|---|---|---|---|
| `run04_mejor` (principal) | 291.6 / 100.9 | 196.3 | 6.1 | **196.3 HU** |
| `run04_60k` (sensibilidad) | 160.0 / 71.7 | 115.8 | 6.1 | **115.8 HU** |

Con Ti las replicas difieren en 8 y 27 HU: tampoco fijaria el margen. Diferencia difusor principal menos Peters Ti, en
medianas: -633 HU (`0101`) y -104 HU (`0102`).
