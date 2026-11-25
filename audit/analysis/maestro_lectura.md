# Lectura del REPORTE del script maestro (job 65084, GRUPO=entrena; exploratorio y post hoc). Copia del reporte: maestro_REPORTE_2026-11-24.md
Estado: REF, SMOKE_T/P/A, TRAIN/EVAL/MET de C, T, P y A: todas OK (24 nov 08:22-13:27, ~1 h de entrenamiento por brazo, 3 000 pasos). El grupo `test` (GEN_TEST + a20 de 100:0.3 en los 13 de prueba) NO se ejecuto: `a20_test_base.csv` y `a20_val.csv` no existen (estado.tsv solo tiene REF de 2026-11-21). El \GAPDATO de capitulo3:363 sigue pendiente.
Metricas en validacion (0101/0102), comparador aux_C (misma GPU; razon de textura de la imagen original: 1.358; tope D2 279.6):
| brazo | razon textura | frac M<2500 HU | salto borde G | cascaras (a) /7 | D2 0-2 mm | E 2-10 |
| run04_mejor | 1.379 | 0.191 | 36 | 0 | s/d | s/d |
| b_min_l0 (T4) | 1.233 | 0.397 | 32 | 0 | 585 | 582 |
| 100:0.3 | 1.421 | 0.153 | 36 | 3 | 83 | 362 |
| aux_C (control A6000) | 1.245 | 0.100 | 35 | 0 | 316 | 560 |
| aux_T | 1.329 | 0.128 | 34 | 0 | 288 | 545 |
| aux_P | 1.223 | 0.115 | 35 | 0 | 437 | 588 |
| aux_A | 1.200 | 0.154 | 34 | 0 | 408 | 674 |
Criterios de (18) frente a aux_C: T cumple (i) (|1.329-1.358| = 0.029 frente a 0.113) y falla (ii) (0.128 > 0.100); P falla (i) y (ii); A falla (i) y (ii). Ninguno cumple (i)-(iv); (iv) D2 <= 279.6 tampoco (T 288, C 316, A 408, P 437). Cascaras (a): 0/7 en los cuatro.
Lecturas (descriptivas): (1) por la regla de parada (01-decisiones (24).1) ningun brazo T/P/A pasa a validacion 2 ni a prueba. (2) El control aux_C ya cambia mucho respecto de run04_mejor solo por seguir entrenando (frac M<2500 HU 0.191 -> 0.100; D2 0-2 mm 316 frente a ~233): las diferencias de T/P/A con aux_C son pequenas. (3) El control en la A6000 degrada el D2 0-2 mm (316) menos que el control de la T4 (585): parte de la degradacion de b_min_l0 puede ser configuracion/hardware (#212, #206). (4) 100:0.3 conserva D2 0-2 mm 83 y cascaras 3/7, pero sin la prueba.
