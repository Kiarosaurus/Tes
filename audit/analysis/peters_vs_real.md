# Peters vs real vs modelo por anillo (D1/D2), verificacion independiente
Script: peters_vs_real_anillos.py (usa perfil/cuerpo_2d/amplitud de experiments/objetivo3/d1_alcance_rayas.py sin modificarlo). Metrica D1: exceso = amplitud(5 % sup - 5 % inf) de la imagen con metal menos la misma sin metal (limpia_A), mismos pixeles, anillos de 2 mm desde M, hasta 8 cortes por paciente; 15 pacientes de Peters (13 prueba + 2 validacion).
Real (tornillo, n=18): reproduce exactamente d1_d2_resultado.md. Modelo: D2 (run04_mejor, validacion 0101/0102, 5 semillas).

| anillo mm | Peters Ti med (min..max) | Peters Fe med | real tornillo med | modelo run04_mejor | Ti/real | modelo/real | pac. Ti > max(real) |
|---|---|---|---|---|---|---|---|
| 0-2 | 5004 (2754..6100) | 15736 | 1930 | 1697 | 2.6 | 0.88 | 10/15 |
| 2-4 | 2558 (1133..4047) | 10148 | 1199 | 488 | 2.1 | 0.41 | 3/15 |
| 4-6 | 2052 (500..2749) | 7339 | 765 | 97 | 2.7 | 0.13 | 8/15 |
| 6-8 | 1487 (363..2259) | 5364 | 473 | n/d aqui | 3.1 | n/d | 10/15 |
| 8-10 | 1138 (209..1617) | 4172 | 174 | n/d | 6.6 | n/d | 11/15 |
Lectura: Peters Ti sobreestima 2.1-3.1x entre 0 y 8 mm; el modelo subestima (0.88, 0.41, 0.13). Lo real queda entre ambos. Cuidado: pacientes distintos (real 18 entrenamiento/validacion, modelo 2 de validacion, Peters 15); referencia real = otro corte; limpia_A como referencia de Peters. "pac. Ti > max(real)" compara con el maximo de pacientes reales (mas estricto que el IC90).
Distinta metrica que E-A2 (campo de desviacion sintetico - original sin metal en B_delta; amplitud por region), por eso los niveles absolutos de E-A2 (Ti ~1000-1500 HU) no son los de D1.
