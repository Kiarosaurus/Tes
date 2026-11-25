# REPORTE del script maestro (exploratorio; reglas en docs/01-decisiones.md 2026-11-21 (18) y (18-a))

## Estado de las etapas

| grupo | etapa | estado | inicio | fin | nota |
|---|---|---|---|---|---|
| entrena | REF | OK | 2026-11-24T08:22:30-05:00 | 2026-11-24T08:28:20-05:00 |  |
| entrena | SMOKE_T | OK | 2026-11-24T08:28:20-05:00 | 2026-11-24T08:31:24-05:00 |  |
| entrena | SMOKE_P | OK | 2026-11-24T08:31:24-05:00 | 2026-11-24T08:33:39-05:00 |  |
| entrena | SMOKE_A | OK | 2026-11-24T08:33:39-05:00 | 2026-11-24T08:35:58-05:00 |  |
| entrena | TRAIN_C | OK | 2026-11-24T08:35:58-05:00 | 2026-11-24T09:33:56-05:00 |  |
| entrena | EVAL_C | OK | 2026-11-24T09:33:56-05:00 | 2026-11-24T09:47:05-05:00 |  |
| entrena | MET_C | OK | 2026-11-24T09:47:05-05:00 | 2026-11-24T09:47:57-05:00 |  |
| entrena | TRAIN_T | OK | 2026-11-24T09:47:57-05:00 | 2026-11-24T10:46:28-05:00 |  |
| entrena | EVAL_T | OK | 2026-11-24T10:46:28-05:00 | 2026-11-24T10:59:29-05:00 |  |
| entrena | MET_T | OK | 2026-11-24T10:59:29-05:00 | 2026-11-24T11:00:29-05:00 |  |
| entrena | TRAIN_P | OK | 2026-11-24T11:00:29-05:00 | 2026-11-24T11:59:06-05:00 |  |
| entrena | EVAL_P | OK | 2026-11-24T11:59:06-05:00 | 2026-11-24T12:12:08-05:00 |  |
| entrena | MET_P | OK | 2026-11-24T12:12:08-05:00 | 2026-11-24T12:13:01-05:00 |  |
| entrena | TRAIN_A | OK | 2026-11-24T12:13:01-05:00 | 2026-11-24T13:13:13-05:00 |  |
| entrena | EVAL_A | OK | 2026-11-24T13:13:13-05:00 | 2026-11-24T13:26:44-05:00 |  |
| entrena | MET_A | OK | 2026-11-24T13:26:44-05:00 | 2026-11-24T13:27:39-05:00 |  |

lambda de T: 0.02

lambda de P: 0.05

## Metricas por brazo (validacion 0101/0102; comparador = control `aux_C` (mismo hardware) o, si no existe, `b_min_l0`)

| brazo | razon de textura (original: 1.358) | frac. M < 2500 HU | salto borde G (HU) | cascaras (a) /7 | D2 0-2 mm (dev, tope 279.6) | E 2-10 mm |
|---|---|---|---|---|---|---|
| run04_mejor | 1.379 | 0.191 | 36 | 0 | sin dato | sin dato |
| b_min_l0 | 1.233 | 0.397 | 32 | 0 | 585 | 582 |
| b_min_l0.8_t1000 | 1.325 | 0.262 | 34 | 3 | 26 | 275 |
| b_min_l3_t300 | 1.524 | 0.111 | 33 | 2 | 152 | 215 |
| run04_mejor_p100_e0.3 | 1.421 | 0.153 | 36 | 3 | 83 | 362 |
| aux_C | 1.245 | 0.100 | 35 | 0 | 316 | 560 |
| aux_T | 1.329 | 0.128 | 34 | 0 | 288 | 545 |
| aux_P | 1.223 | 0.115 | 35 | 0 | 437 | 588 |
| aux_A | 1.200 | 0.154 | 34 | 0 | 408 | 674 |

## Criterios de (18) frente al control (si hay dato)

- aux_T: (i) textura mas cerca de la original que el control: True (1.329 frente a 1.245); (ii) estatica no mayor: False (0.128 frente a 0.100). (iii) cascaras y (iv) D2: ver tabla.
- aux_P: (i) textura mas cerca de la original que el control: False (1.223 frente a 1.245); (ii) estatica no mayor: False (0.115 frente a 0.100). (iii) cascaras y (iv) D2: ver tabla.
- aux_A: (i) textura mas cerca de la original que el control: False (1.200 frente a 1.245); (ii) estatica no mayor: False (0.154 frente a 0.100). (iii) cascaras y (iv) D2: ver tabla.

## Corrida en prueba de 100:0.3 (a20)

- `a20_test_base.csv`: NO existe
- `a20_val.csv`: NO existe

Al volver: bajar los resultados y correr `experiments/objetivo3/evalua_todo_local.sh` (C4, D2, a24, sesion a ciegas).
Todo es exploratorio y post-hoc; nada entra a `overleaf/` sin decision de la autora.
