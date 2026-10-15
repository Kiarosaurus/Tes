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

## Version 2 en prueba (exploratorio, lecturas previas) — `a20_v2` + `a26`

Fuente: Khipu 56857-56865 (rc=0) -> `outputs/khipu_2026-10-15/v2_prueba/` (`a26/<variante>/`, `a24/`). `Delta` propio
de validacion: run05a 157.1 HU, run05b 107.1 HU; margen comun 196.3. Peters y copia y pegado identicos a v1 (verificado).

| variante | run04_mejor (v1) | run05a | run05b | desenlace (los tres) |
|---|---|---|---|---|
| base | -301.0 [-477.0, -124.9] | -258.9 [-456.7, -61.1] | -264.3 [-456.8, -71.7] | no concluyente, dif. < Peters |
| inter | -295.3 | -254.3 | -269.6 | igual |
| suelo simetrico | -238.3 | -196.2 [-360.9, -31.5] | -201.6 [-360.9, -42.3] | igual |
| sin cabeza | -329.3 | -280.1 | -288.0 | igual |
| anillo 8-10 mm | +478.0 | +489.8 | +480.0 | no equivalencia, dif. > Peters |
| anillo 10-12 mm | +411.7 | +415.2 | +424.9 | no equivalencia, dif. > Peters |

Margen minimo (base): run05a 456.7 HU (29 %), run05b 456.8 (29 %), frente a 477.0 de v1. Acuerdo (base): CV
run05a 0.093, run05b 0.081 (Ti 0.241); Pearson con Ti 0.03 y 0.09 (v1: 0.40); Pitman-Morgan p 7.3e-4 y 1.9e-4.
Permutacion: no baja ninguna categoria. Lectura: la version 2 acerca la media ~40 HU sin cambiar ningun desenlace;
la correlacion por paciente con Peters cae a ~0. Implicancia #190.

## D-extra 3 — E-A1 de v2 con `--delta` 0.03 (el de run04)

Fuente: Khipu 56868/56869 -> `outputs/khipu_2026-10-15/a23_v2/run05{a,b}_d003/`. Medianas, grupo 1 (n = 9):

| modelo / lectura | MAE `G` | MAE `M` | MAE `B_delta` | metal SDC | pacientes con MAE `G` < run04 |
|---|---|---|---|---|---|
| run04, 0.03 | 270.9 | 2312.5 | 198.0 | 0.928 | — |
| run05a, propio (0.05) | 259.5 | 2423.2 | 192.2 | 0.925 | 9 de 13 |
| run05a, 0.03 | 271.8 | 2694.9 | 188.8 | 0.894 | 4 de 13 |
| run05b, propio (0.2) | 242.1 | 2062.0 | 185.7 | 0.948 | 11 de 13 |
| run05b, 0.03 | 246.4 | 2335.3 | 188.2 | 0.930 | 9 de 13 |

Lectura: la ventaja de run05a sobre run04 en E-A1 es de lectura (desaparece con 0.03); la de run05b se sostiene en
parte (9 de 13). Grupo 2 (n = 4): exceso de costura con 0.03 sube a 43.9 (run05a) y 72.8 HU (run05b), frente a 9.0 de
run04: el 0.03 no es una lectura adecuada para esos modelos fuera de distribucion. Implicancia #190.

## D7 — mecanismo del p95

Fuente: `a28_diag_p95.py` sobre Khipu 56866 (`u` de `G`, 0101/0102 x 5 semillas) -> `outputs/obj3_pose/a28/`. Control
de regresion: la decodificacion local reproduce el `elev_p95` de `a15` (diferencia 0.00 HU en las 10 generaciones).

- (a) Con solo LW el p95 entra en la envolvente real en **1 de 7** cascaras (umbral 4): no cumple. LW sube el p95
  +3 a +53 HU; el deficit frente a la envolvente es de 30 a 130 HU.
- (b) En lo real el cambio de decodificacion mueve el p95 0.00 HU (ida y vuelta exacta): cumple, pero es trivial.
- **Veredicto por la regla: modelo.** Implicancia #191.

## #189 — acuerdo en escala logaritmica (pedido de la autora, 2026-10-15)

Fuente: `a26_lecturas.py` ampliado (Bland-Altman sobre ln(difusor) - ln(Peters Ti), devuelto como razon
difusor / Ti; Pitman-Morgan sobre ln; Spearman entre la media del par y |dif - sesgo| en cada escala) ->
`outputs/a26_log/{v1,v2}_<variante>/`. Regresion: todos los campos previos identicos a `outputs/a26/` y a los `a26`
de Khipu (diferencias < 1e-10). POSTERIOR para v1 y v2 (`visto.md`): descriptivo.

| variante | modelo | razon sesgo [limites 95 %] | Shapiro p (log) | Pitman-Morgan log r (p) | hetero HU rho (p) | hetero log rho (p) |
|---|---|---|---|---|---|---|
| base | run04_mejor | 0.831 [0.533, 1.296] | 0.38 | -0.83 (4.7e-4) | 0.15 (0.62) | 0.15 (0.62) |
| base | run05a_mejor | 0.857 [0.517, 1.420] | 0.90 | -0.74 (3.8e-3) | 0.24 (0.44) | 0.12 (0.69) |
| base | run05b_mejor | 0.854 [0.525, 1.390] | 0.72 | -0.78 (1.7e-3) | 0.26 (0.39) | 0.12 (0.71) |
| congelado | run04_60k | 0.778 [0.490, 1.236] | 0.45 | -0.83 (4.1e-4) | 0.20 (0.51) | 0.03 (0.91) |
| inter | run04_mejor | 0.835 [0.534, 1.306] | 0.63 | -0.85 (2.6e-4) | 0.13 (0.67) | 0.12 (0.69) |
| suelo | run04_mejor | 0.859 [0.577, 1.278] | 0.15 | -0.77 (2.1e-3) | 0.14 (0.64) | 0.13 (0.67) |
| sincabeza | run04_mejor | 0.817 [0.521, 1.279] | 0.33 | -0.84 (2.9e-4) | 0.14 (0.64) | 0.15 (0.63) |
| r08_10 | run04_mejor | 2.206 [1.194, 4.074] | 0.62 | -0.58 (0.038) | -0.27 (0.37) | -0.58 (0.037) |
| r10_12 | run04_mejor | 2.341 [1.383, 3.965] | 0.84 | -0.48 (0.097) | -0.09 (0.76) | -0.37 (0.22) |

v2 en `inter`, `suelo`, `sincabeza` y anillos 8-12 mm: mismo patron que v1 (razones 0.84-0.89 y 2.22-2.39; tablas
en `outputs/a26_log/v2_*`). **12-16 mm: no aplica** — el difusor vale 0 HU en los 13 pacientes (fuera de `G`, techo
de `G`), ln no definido; ya era trivial.

Lectura:
- En HU la dispersion de las diferencias **no crece** con la magnitud (Spearman 0.15, p 0.62). Lo que viola el
  supuesto de Bland-Altman (p. 309) es una **pendiente**: la diferencia baja al subir la media (r suma-diferencia
  -0.89), porque el difusor varia menos entre pacientes que Peters.
- En log esa pendiente **sigue** (Pitman-Morgan log r -0.83, p 4.7e-4): las diferencias no son proporcionales a la
  media, asi que el log no arregla el supuesto. Bland-Altman avisan que con una relacion asi los limites quedan
  "too far apart rather than too close" (p. 309): conservadores.
- Como resumen en razon: el difusor da ~0.83 veces la amplitud de Peters Ti; el 95 % de los pacientes caeria entre
  0.53 y 1.30 veces. En los anillos 8-12 mm, entre 2.2 y 2.4 veces (por encima).
- Pitman-Morgan sobre ln compara aproximadamente los CV: ahora si se puede decir que el difusor tiene **menor
  variabilidad relativa** que Peters (p 4.7e-4), lo que antes (HU crudos) solo era descriptivo (#189 punto 4).
  Normalidad de ln(D) - ln(Ti): Shapiro p 0.15-0.90, sin rechazo (n = 13, poca potencia).

## Perfil por anillos y contraste pareado (#187 c, #188) — REGLA FIJADA ANTES DE CORRER (2026-10-15)

Propuesta del asistente como asesor (pedido de la autora: "aplica tu recomendacion y realiza los experimentos que
consideres"). Todo es POSTERIOR y descriptivo: no puede cambiar el desenlace confirmatorio (regla general de DEC
2026-10-15).

Motivo: en 8-10 mm el difusor da 888 HU y su nulo (sin metal) 893 HU; el "difusor sobre Peters en 8-12 mm" de #187
puede ser piso de regeneracion, no artefacto. Peters ya se mide contra su propia simulacion sin metal
(`a20`, `costura`: "Peters: ref = su simulacion sin metal"); el difusor, contra la TC original. El analogo justo es
**difusor pareado** = sintetica con metal (semilla s) - sintetica sin metal (`--sin-metal`, misma semilla s, mismo
corte, mismo `delta`): DDIM con `eta` 0 y `torch.Generator(seed)` por corte, asi que el ruido inicial es el mismo.

Mediciones:
1. Local (v1): `a20_v1_variantes.sh r00_02 r02_04 r04_06 r06_08` -> perfil completo 0-12 mm de Peters Ti,
   parametrico y difusor sin parear.
2. Khipu (v1): `a20 difusor --ref-etiqueta run04_mejor_nulo --ref-dir <nulo>` en `base` y en los 6 anillos 0-12 mm.
   v2 no tiene nulo (`--sin-metal` no esta definido para entrada 12): se declara.

Lectura fijada:
- (i) Si en 8-12 mm el difusor pareado queda por debajo de la mitad del sin parear, el exceso de #187 en 8-12 mm se
  atribuye al piso de regeneracion (#188), no al artefacto.
- (ii) Forma: decaimiento por paciente = amplitud(0-2 mm) / amplitud(6-8 mm) por brazo; se compara con D1 real
  (1930 / 473 = 4.1, medianas de exceso). Brazo "plano" si su razon es < 2.
- (iii) Banda completa pareada: media de (difusor pareado - Peters Ti) con IC90 *t*, contra `Delta` comun 196.3,
  como descriptivo. No reemplaza ni eleva el desenlace confirmatorio.

### Resultado (ii) — perfil por anillos, v1, local (`a29_perfil.py` -> `outputs/a29/`; corrida 12:44-14:23)

| anillo (mm) | Peters Ti | parametrico | difusor | D1 real (exceso) |
|---|---|---|---|---|
| 0-2 | 3864 (n = 10) | 1865 | 1828 | 1930 |
| 2-4 | 1808 | 1469 | 1234 | 1199 |
| 4-6 | 894 | 948 | 949 | 765 |
| 6-8 | 613 | 598 | 946 | 473 |
| 8-10 | 448 | 306 | 919 | 174 |
| 10-12 | 338 | 83 | 727 | 11 |

Razon 0-2 / 6-8 por paciente (mediana [p25, p75]): Peters 6.71 [5.89, 7.54] (n = 10: en 3 pacientes el anillo 0-2 no
tiene ROIs validas en los cortes que Peters simula); parametrico 3.16; **difusor 1.92 [1.82, 2.21] -> plano por la
regla**; D1 real 4.08. Lectura: junto al tornillo el difusor da el nivel real (1828 frente a 1930) pero desde 4 mm
queda en una meseta de ~950 HU, del orden de su piso sin metal (893, #188). Peters cae mas rapido que lo real. D1 es
otra metrica (exceso sobre un corte sin metal): comparar forma, no nivel. (i) y (iii) esperan `a20_pareado.sbatch`.

### Resultados (i) y (iii) — contraste pareado (Khipu 56968, rc=0, 13 x 5 x 7 variantes; `outputs/khipu_pareado/`)

| anillo (mm) | difusor sin parear | difusor pareado | Peters Ti | D1 real |
|---|---|---|---|---|
| 0-2 | 1828 | 1749 | 3864 (n = 10) | 1930 |
| 2-4 | 1234 | 1201 | 1808 | 1199 |
| 4-6 | 949 | 789 | 894 | 765 |
| 6-8 | 946 | 794 | 613 | 473 |
| 8-10 | 919 | 725 | 448 | 174 |
| 10-12 | 727 | 616 | 338 | 11 |

- **(i)** 8-10 mm: pareado 725 frente a 919 sin parear; 10-12 mm: 616 frente a 727. Ninguno baja de la mitad: por la
  regla, **la meseta de 8-12 mm no se atribuye al piso de regeneracion**.
- **(ii) pareado:** razon 0-2 / 6-8 = 2.42 [2.09, 2.59]: no plano por la regla, pero lejos de lo real (4.08) y de Peters.
- **(iii)** banda completa: difusor pareado - Peters Ti = **-455.0 HU, IC90 [-647.6, -262.5]**, entero bajo -196.3
  (descriptivo; la categoria confirmatoria sigue siendo "no concluyente, a la baja"). Mediana pareado 1112, Ti 1574;
  Pearson con Ti 0.02.
- **Limite (no anticipado en la regla):** con la misma semilla, cambiar el canal `M` cambia toda la trayectoria de
  muestreo DDIM, asi que "con metal - sin metal" mezcla el efecto del metal con la divergencia de la muestra en toda
  `G`. El pareado no aisla un artefacto "puro"; separa solo el ruido inicial comun. Lectura: lejos del tornillo, la
  presencia del metal cambia la textura generada (600-725 HU) sin reproducir la caida real (174 y 11 HU).
- **Sentido del piso sobre el contraste primario (#188):** referir el difusor a su propia sintesis sin metal baja su
  amplitud (1308 -> 1112 de mediana) y aleja la diferencia de cero (-301.0 -> -455.0): el piso del brazo aprendido
  **favorece al difusor** en el contraste primario, es decir, lo acerca a la equivalencia.
