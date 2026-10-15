# Resultados de las mediciones de DEC 2026-10-15 (posteriores; se completa a medida que llegan)

> Cada bloque cita su script y su salida. Lo visto se registra en `visto.md`.

## D4 — diferencia de diametro entre mascaras (semimaximo local frente a 2500 HU)

Fuente: `experiments/objetivo2/e8_componentes.csv` (E8 ya media `d_ext_2500_mm` y `d_ext_semimax_mm` por componente),
filtrado a pacientes de entrenamiento de `p1_particion.csv` y `vol_mm3` en [500, 4000]. Calculo del 2026-10-15.

- 32 componentes (todos de clase `alargado`) de 23 pacientes de entrenamiento.
- `d_ext_semimax - d_ext_2500`: mediana **-0.24 mm**, IQR [-0.54, 0.02], p10 -1.32, p90 0.39.
- Medianas: 5.17 mm a 2500 HU y 5.02 mm a semimaximo.
- Lectura (sin regla, dato de la limitacion): en tornillos la mascara por semimaximo seria de mediana un cuarto de
  milimetro mas estrecha, por debajo de un voxel. La sensibilidad no se entreno (coste); su efecto sobre el modelo no
  se midio.

## D8 — preservacion del protocolo fisico fuera de `G`

Fuente: `a27_preservacion_peters.py` -> `outputs/obj3_pose/a27/`. 13 pacientes de E-A2 x 2 replicas, cortes simulados,
fuera de `G`, dentro del cuerpo (> -500 HU, mayor componente, agujeros rellenos).

| | mediana | rango |
|---|---|---|
| RMSE (HU) | 31.4 | 20.1 a 42.4 |
| SSIM ([-1000, 2000] HU) | 0.9069 | 0.8268 a 0.9653 |

El sintetizador vale 0 / 1 por construccion en esta region (no es resultado).

## Variantes de `a20` sobre la version 1 (run04_mejor) y comparador parametrico — posteriores para v1

Fuente: `a20_v1_variantes.sh` (lote local terminado 2026-10-15 04:15; 13 pacientes x 5 brazos por variante, sin
filas faltantes salvo `ruido_A-B` sin geometria, esperado) -> `outputs/obj3_pose/a20_variantes/a20_test_<v>.csv`;
lecturas con `a26_lecturas.py` -> `outputs/a26/v1_<v>/`. `Delta` propio = comun = 196.3 HU.

**Difusor (run04_mejor) frente a Peters Ti** (media de la diferencia, IC90 *t*; permutacion coincide a <2 HU en todas):

| variante | Peters Ti | difusor | difusor - Ti, IC90 | desenlace | CV dif. / CV Ti | Pitman-Morgan p |
|---|---|---|---|---|---|---|
| base | 1594.7 | 1293.7 | -301.0 [-477.0, -124.9] | no concluyente, dif. < Peters | 0.076 / 0.241 | 3.8e-5 |
| inter (cortes k=2) | 1594.7 | 1299.3 | -295.3 [-473.6, -117.1] | no concluyente, dif. < Peters | 0.071 / 0.241 | 2.2e-5 |
| suelo simetrico | 1532.0 | 1293.7 | -238.3 [-384.1, -92.4] | no concluyente, dif. < Peters | 0.076 / 0.204 | 3.9e-4 |
| sin cabeza (20 mm) | 1614.3 | 1285.0 | -329.3 [-510.4, -148.3] | no concluyente, dif. < Peters | 0.075 / 0.247 | 1.7e-5 |
| anillo 8-10 mm | 410.2 | 888.2 | +478.0 [+393.9, +562.2] | no equivalencia, dif. > Peters | 0.123 / 0.230 | 0.61 |
| anillo 10-12 mm | 313.5 | 725.1 | +411.7 [+350.9, +472.5] | no equivalencia, dif. > Peters | 0.124 / 0.196 | 0.21 |
| anillo 12-14 mm | 259.5 | 0.0 | -259.5 | trivial: el difusor vale 0 por construccion fuera de `G` | — | — |
| anillo 14-16 mm | 230.8 | 0.0 | -230.8 | trivial (idem) | — | — |

**Comparador parametrico** (DEC 2026-10-15 (2), descriptivo; misma lectura aplicada solo como descripcion):

| variante | parametrico | param. - Ti, IC90 | lectura con 196.3 | difusor - param. |
|---|---|---|---|---|
| base | 1495.7 | -98.9 [-287.3, +89.4] | no concluyente | -202.0 |
| inter | 1495.7 | -98.9 [-287.3, +89.4] | no concluyente | -196.4 |
| suelo simetrico | 1495.7 | -36.3 [-191.5, +118.9] | equivalencia | -202.0 |
| sin cabeza | 1495.9 | -118.4 [-314.1, +77.3] | no concluyente | -210.9 |
| anillo 8-10 mm | 307.5 | -102.7 [-149.5, -55.8] | equivalencia | +580.7 |
| anillo 10-12 mm | 83.2 | -230.3 [-260.9, -199.7] | no equivalencia | +642.0 |

Copia y pegado: amplitud 0.0 en todas las variantes (sin artefacto por construccion).

Lectura (descriptiva, sin regla nueva):
- Ninguna variante sube la categoria del difusor; las que corrigen asimetrias (#186: `inter`, `suelo`) achican la
  diferencia 6-63 HU sin cambiar el desenlace.
- El perfil del difusor es plano: queda por debajo de Peters en la banda completa y por encima en 8-12 mm
  (+412 a +478 HU), donde Peters y el parametrico (D1, datos reales) ya decaen.
- El parametrico, sin aprendizaje, queda mas cerca de Peters que el difusor en la banda completa (-98.9 frente a
  -301.0 HU) y alcanza equivalencia con suelo simetrico. Implicancia #187.
- 12-16 mm no compara nada: es el techo de `B_delta` (#176 H2). El residuo de Peters ahi (231-260 HU) esta en el orden
  de su piso de ruido (184 HU, #186).

## D-extra 2 — piso de ruido de cada brazo

Fuente: Khipu 56867 (`a15_diag.sbatch MODO=nulo`, rc=0) -> `outputs/khipu_2026-10-15/obj3_pose/nulo/a20_nulo.csv`
(13 x 5 semillas, `run04_mejor`, `G` sin `M`). Peters: `ruido_A-B` de la variante `base`.

| brazo | piso (sin metal) | con metal | piso / con metal | con metal - piso |
|---|---|---|---|---|
| difusor run04_mejor | 893 [766, 1055] | 1308 | 0.69 | 397 |
| Peters Ti | 184 | 1574 | 0.12 | 1388 |

Medianas por paciente, HU. Implicancia #188.
