# Auditoria de trazabilidad — capitulo3 — r12

Entrada: `overleaf/secciones/capitulo3.tex` (377 lineas, estado tras r11), `capitulo3-r11-respuesta.md`,
`capitulo3-r12-lint.md` (PASA; 15 bajas E-P1, todas cifras propias con fuente abajo). Ningun RECHAZADO en r11.
Escalados de r11 (T01 RMSE/SSIM, guia-8, guia-9, `02-datos.md`) y el desfase de `00-tesis.md`,
`EXPERIMENTOS.md` y `02-datos.md` no se repiten: ya estan con la autora.

Comprobaciones pedidas:
- **Corrida final en prueba (jobs 55453-55455):** ninguna de sus cifras aparece. Las cifras del Obj 3 son de
  validacion (`0101`, `0102`, `metal_0039`), del diseno o del entrenamiento. Los `\GAPDATO` de `:38`, `:306` y
  `:326` siguen siendo verdad (`docs/ESTADO.md`:5-9: salidas sin traer; 8 pacientes sin revisar).
- **#158 sigue ABIERTA:** el capitulo da los hechos y deja la cita del repositorio en `\GAPDEC` (`:296`) y
  `\GAPLIT` (`:298`). Correcto (OC-3).

Abreviaturas: DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; DA0 = `experiments/objetivo3/diseno_A.md`
seccion 0; SON = `sonda_peters.md`; A17/A20/A21 = `a17_cotejo_resultado.md`, `a20_resultados.md`, `a21_resultado.md`;
PET = ficha `peters2025hybrid.md`; TM = `tesis/main.tex`; R11 = fila del inventario de `capitulo3-r11-trazabilidad.md`
con texto sin cambios, re-cotejada.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-5 | `capitulo3.tex:192` | "el optimizador AdamW con tasa de aprendizaje de $10^{-4}$, lotes de 4" | DEC 2026-10-08 A.3 (:2085-2086: "Arquitectura congelada tal como corrio: ... lote 4"); `experiments/objetivo3/a7_entrenar.sbatch`:60 (`--lote 16`); IMP #134 (:9267: "lote 4 -> 16, `base` intacto en 64"); IMP #148 (:10644: `meta` de los `ckpt` de `run01` y `run02`, lote 16 en los dos) | **Patron PAT-20 reincide.** Las fuentes discrepan entre si. La decision dice "tal como corrio" y da lote 4, pero el script de entrenamiento y los metadatos de los dos puntos de control dan 16. El 4 era el del piloto, antes de #134. El texto copia la decision y describe un modelo que no es el evaluado (`mejor_37k` es de `run02`) | Describir lo corrido y marcar la discrepancia, como piden OC-5 y BITACORA §2 2026-10-10: "lotes de 16 \GAPDEC{la decisión que congela la arquitectura registra lotes de 4, pero las dos corridas de entrenamiento usaron 16}". Para la autora: corregir DEC 2026-10-08 A.3 (solo ella edita DEC) |
| T02 | alta | G-T4, OC-3 | `capitulo3.tex:210`, `:320` (y `:376`) | "las dos pelvis de validación sin metal cuyo corredor admite el tornillo"; "un tercer paciente de validación sin metal" | DEC 2026-09-21 (2) (:1384-1386: `CLINIC_0102`, cremallera, y `CLINIC_0019`, accesorio, llevan metal **no ortopedico**; sin metal: `0046`, `0066`, `0101`); IMP #105 (:7725); DEC 2026-10-09 (4) pto 4 (receptores `0101` y `0102`; `0019` fuera por 1.6 mm); el propio capitulo `:262` (los objetos no ortopedicos cuentan "con metal": 19 = 11 + 8); `capitulo3-r08-respuesta.md` A3 (se evito "sin metal" por la cremallera de `0102`) | Uno de los dos receptores (`0102`) y el excluido (`0019`) tienen metal no ortopedico. Por la clasificacion de `:262`, son pacientes "con metal". El capitulo los llama "sin metal" y contradice su propia particion de prueba. Ademas, $\Delta$ se fijo sobre un receptor con un objeto metalico, una condicion que la sintesis sobre pelvis sin metal (13 de prueba) excluye. `:376` enumera en que difieren las condiciones del margen y de la prueba, pero no nombra esta. Las fuentes tambien estan en tension: DEC 2026-09-21 (2) da tres pacientes de validacion sin metal (`0046`, `0066`, `0101`) y DEC 2026-10-09 (4) usa `0101` y `0102` sin decir por que salen `0046` y `0066` | `:210`: "las dos pelvis de validación sin osteosíntesis cuyo corredor admite el tornillo, una de ellas con un objeto metálico no ortopédico". `:320`: "un tercer paciente de validación sin osteosíntesis". En `:376`, añadir que uno de los dos receptores del margen lleva un objeto no ortopédico, que la prueba excluye. Para la autora: por que `0046` y `0066` no son receptores (¿corredor? ¿R2?); si falta, `\GAPDEC` |
| T03 | media | G-T4, G-C7 | `capitulo3.tex:330` frente a `:352` | "Las decisiones de los tres objetivos tomadas después de ver datos se enumeran en la Sección amenazas" | El propio capitulo: `:101` (sensibilidad sin los 2 casos con error de segmentacion, anadida tras verlos; DEC 2026-10-08 pto 22) y `:374` (intervalo por remuestreo de W1, "no estaba preinscrito"; DEC 2026-10-08 pto 18, tomada con la distancia del muestreador ya conocida, pto 17) | **Patron PAT-140 reincide.** La remision promete una enumeracion completa. `:352` lista cuatro decisiones post hoc del Obj 2, pero omite dos analisis anadidos despues de ver datos que el mismo capitulo declara. Quitar el recuento cerrado no basta, porque el verbo "se enumeran" mantiene la promesa | Anadir en `:352`: "..., la escala de lectura de la distancia, la sensibilidad sin los dos casos con error de segmentación y el intervalo por remuestreo de la distancia". O cambiar `:330` a "Las principales decisiones ... se recogen en" |
| T04 | baja | G-T4 | `capitulo3.tex:258` (`\GAPDEC`) | "se mide con RMSE y SSIM ... como preveía ... sobre el complemento de $B_{\delta}$" | TM:102 ("restricted to the complement of $B_{\delta}$"); `:79` ($B_{\delta}$ excluye el metal); DA §7 E-A3 ("fuera de `G`") | La marca pregunta por la preservacion "fuera de $G$" y la presenta como lo que preveia el boceto. Pero el boceto la definia sobre el complemento de $B_{\delta}$, que incluye $M$ y no es la misma region. Esa discrepancia (T01 de r11) era para la autora, y el GAP la borra | Dentro de la marca: "... como preveía la formulación inicial, aunque sobre el complemento de $B_{\delta}$, que incluye $M$ ..." |

## Inventario

Una fila por unidad verificable, en el orden del `.tex`.

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9 | Dos componentes; compuerta previa; transilíaco-transsacro | TM:74-80; IMP #130 | si (R11) |
| :13 | Cuatro objetivos; SAP unica metrica propia; nombres publicados | TM:80, :96; DEC 2026-09-08 | si (R11) |
| :15, Fig. `fig:pipeline` | Cadena, `M`, `B_delta`, `G`; copia fuera de `G`; caja final con eje sin perturbar | TM:77-79; DA0:27-28 | si (R11) |
| :36 | Dice/HD95 y ablaciones fuera; 14 de 75; 178 de 1 184 | `docs/00-tesis.md` *Fuera de alcance*; `liu2021ctpelvic1k`; DEC 2026-10-08 pto 28 | si (R11) |
| :38 | Compuerta negativa; Obj 2 en dos cohortes; `\GAPDATO` (2 pacientes de validacion, punto de control elegido, sin resultados en prueba); congelado el 9-10-2026 antes de prueba; corrida final | DEC 2026-10-09 (6) pto 1, pto 5; DA0:14-19; `docs/ESTADO.md`:5-28 | si (justificado; sin cifra de prueba) |
| :42-46 | 103/75; MAR y monoenergetica no reportadas (Selles et al.); cribado 2500 HU; revision 3D de 178; `\GAPDATO` multiplanar | `docs/02-datos.md`; ficha `selles2024marreview` | si (R11) |
| :48 | SHA256; 168 = 65/37/66 (recuento previo); 179 unidades; 10 fuera y 1 par | `docs/02-datos.md`:120, :137 | si (como recuento previo; puente en :52) |
| :50 | Aislamiento; validacion 8, prueba 34; Obj 3 reutiliza; Obj 2 sin division | DEC 2026-09-17 (3); DEC 2026-09-21 (2):1384 | si (R11) |
| :52 | `0053` = `0054`; menor espaciado en plano = entrenamiento; 168 -> 167; 65 -> 64; prueba 33; a lo sumo 2.3 HU | IMP #156 (:11251-11264; 0.785 frente a 0.820 mm; "maxima diferencia 2.25 HU") | si (T02 de r11 aplicado) |
| :54 | 103 -> 91 -> 72; control de nivel; 11 de 34; 7 de 57; 1 en borde; 49 | IMP #132, #136 | si (R11) |
| :56-58 | Fractura 20 de 30 (67 %); 10/15 y 10/15; medico recien egresado ciego; 18 + 12; 7 y 5 | IMP #155 act.; IMP :9074 | si (R11) |
| :60 | 64 con material; cuatro funciones; par de reproducibilidad; segundo paciente con femoral (`0053`); fuste de HU bajo en tres pacientes | IMP #155 act. (:11241-11245); IMP #156 (:11249-11250) | si |
| :64-81 | Compuerta; exploracion previa; VAE SD 1.5; canal mas estrecho; 150 HU; MAE; 25 HU; 20.2/12.3/12.74 HU; 2 x 3; ventanas de Wang et al.; 20 000 HU; arcsinh; IC 95 %; orden a priori; 12 mm y 2500 HU; Rombach; Guo et al. y cota por saturacion | R11 fila :64-79, :81; fichas `karageorgos2024ddpm`, `yun2026simulationdriven`, `wang2025adaptiveweighting`, `rombach2022latentdiffusion`, `guo2025maisi` | si (R11) |
| :75 | `\GAPDATO` del ajuste del decodificador | `p1_decodificador_sd15.py` | si (R11) |
| :85-109 | Zwingmann; Ziran 7-25 % y 140 %; Kaiser 5 y 10 mm; 0.42; TS 2.18.0, 6/3 mm, 0.1 %, 104 estructuras; envolvente 2 mm; 72 sin cambio; 8 mm; `D >= d + 2\epsilon`; 9.5 (7.4-11.7); 65.3/23.6 y 62.5/20.8 %; 29 y 27; 5 %; 16 = 14/2/0; 69 frente a 66; 64/57/7/6/48/29/17/3; 61 de 61; 12 de 16 | R11 fila :85-109; IMP #156 (:11260-11261) | si (R11) |
| :95, :101, :105 | `\GAPDATO` del eje, de la sensibilidad sin 2 casos y de la heuristica | IMP #121; DEC 2026-10-08 pto 22; `r1_landmarks.md` | si (justificados) |
| :113, Tabla `tab:geometrias`, :131-137 | Ilion a ilion; McLaren; nominal = rosca; 4.91 mm; 7.0 mm; cabeza 8.0 x 4.5 mm; 4.8/4.9/4.7 mm; 79 de 43; 30 y 12 mm; 6.5/7.3; rosca 16 mm; `\GAPDEC` cabeza; variantes no programadas; 1.5 mm; 316L y Ti-6Al-7Nb; fabricantes (P-EA1) | R11 filas :113-137; DA0:27, :126 | si (R11) |
| :141-182 | 22-09-2026; anclaje; Ec. de pose; Tabla `tab:preinscripcion`; 95 %; 4 grados; 18 = 13/4/1; 39/36/33 mm; 69 de 72; densidad fuera; Arand; Gardner | `preinscripcion_muestreador.md`; IMP #121, #153; DEC 2026-10-08 pto 14 | si (R11) |
| :178 | `\GAPDATO` del segundo corredor | PRE §7 | si (justificado) |
| :186 | *Inpainting* 2.5D en imagen; copia fuera de `G`; arcsinh float32; primera del orden a priori | DEC 2026-10-08 A.1-A.2; DA0:25 | si (R11) |
| :188 | Regla del suelo sin modelo en la banda de entrenamiento y validacion; colas del 5 %; percentil 5 post hoc; rama inaplicable; `\GAPDEC` | DEC 2026-10-05 (:1593-1619; "77 pacientes con metal de entrenamiento y validacion", pto 4 post hoc); DA0:25; IMP #141 ABIERTA | si (justificado) |
| :190 | ControlNet sustituido; presupone base congelada | ficha `zhang2023controlnet`; DEC 2026-09-19 | si (retirado presentado como sustituido) |
| :192 | U-Net 64, (1, 2, 4, 8), atencion abajo; `v`; coseno 1000; AdamW 1e-4; parche 256; 3 cortes; DDIM 50; 5 semillas; no RePaint ni LeFusion | DEC 2026-10-08 A.3-A.5; `a7_entrenar.sbatch`:61-63 | si |
| :192 | **Lotes de 4** | DEC A.3 (4) frente a `a7_entrenar.sbatch`:60, IMP #134 :9267, IMP #148 :10644 (16) | **no (T01)** |
| :192 | `\GAPLIT` de la parametrizacion `v` | MAPA:33 | si (justificado) |
| :194 | Lectura por mezcla; 0.01 y 0.05; caso particular; `\GAPDATO` de la calibracion | DEC 2026-10-07; MAPA:35 | si (R11) |
| :196 | 12 mm; RMSE 7.57/11.45/11.63/54.82/57.69 HU; factores 1.4/1.8/0.7/0.5 | ficha `karageorgos2024ddpm` (Tabla III) | si (R11) |
| :198 | 2500 HU con semimaximo; componente; pose = eje sin perturbar; punto de control definido; 37 500 de 60 000, minimo de validacion; sin pacientes de prueba | DEC D1, D2; DA0:24, :27-28; `docs/ESTADO.md`:375 | si |
| :200-204 | Tres reglas; 0.62; supuesto no verificado; 5 de 40; tres desplazamientos; 0.62 frente a 1.40; 9 de 57; 4.91 mm; salto solo en la reconstruccion; `\GAPDEC`; salto medido una vez, pasado del optimo | DEC 2026-09-21; DEC 2026-10-08 A.6-A.7; DA0:97; IMP #139 | si (R11) |
| :206 | No por la perdida; 30 000 = centro de la meseta en las dos corridas; candidatos 37 500 y 140 000; primer entrenamiento de 144 500 pasos, misma semilla y mismos datos; solo dos | DEC 2026-10-05 (2) (:1658-1670); DEC 2026-10-09 (2) pto 2; IMP #148 (:10635-10652); `docs/ESTADO.md`:389 | si (T06 de r11 y guia-6 aplicados) |
| :208 | Tarea de sintesis en pelvis de validacion sin osteosintesis; dos estadisticos; lectura por mezcla | DEC 2026-10-05 (6) pto 1; DEC 2026-10-07 (2) | si (R11) |
| :210 | Cascaras de 1 mm, 0-12 mm; p50 y p95 sobre 12-15 mm; agregacion por medianas; p50/p75/p95 > 2500 HU; fraccion > 2500 HU solo como control | DEC 2026-10-09 ptos 1-2; DEC 2026-10-07 (2) | si |
| :210 | **"dos pelvis de validación sin metal"** (`0101`, `0102`) | DEC 2026-09-21 (2):1384-1386; IMP #105 :7725 (`0102` cremallera) | **no (T02)** |
| :212 | 2 tornillos de `metal_0039`; `0011` fijador, `0056` placas; sin tornillos de otras particiones; intervalo min-max; desempates; descarta y no prueba; confirmados en cortes | DEC 2026-10-08 (2) (:2179-2187) | si (R11) |
| :214 | 0.5 mm: 8 frente a 7 de 46; pixel 0.896 mm; 1 mm: 11 frente a 5 de 24; post hoc, se reportan los dos; rango entre semillas del perfil 324 frente a 162 HU; reproducido identico | DEC 2026-10-09 ptos 2-3, 6; A17:17-18, :44-47 | si (guia-3 de r11 aplicado) |
| :216 | p95 bajo lo real en 10 u 11 de 12; 150-200 HU mas alla de 3 mm; ~900 HU en `M`; `\GAPDEC` del mecanismo (#157) | DEC 2026-10-09 pto 4; IMP #157 (:11315-11316: -148 y -197 HU a 1 mm) | si (justificado) |
| :218 | 47 pacientes; efecto de anadir pacientes no medido; cuatro veces mas pasos sin mejora | DEC 2026-10-09 (2) pto 3 | si (R11) |
| :222 | Obj 4 sin fila; controles de identidad, monotonia y resolucion; Peters no es contribucion | DEC 2026-10-08 pto 23 | si (R11) |
| :226-250 | SAP con dos componentes; `d` = 7.0, `\epsilon` = 1, `D >= 9` mm; Smith; Ec. brecha; 0/2/4 mm; tramo `T`, 8 mm; 1 + 5 controles; 0.083 mm; 69/15/8/8 y 40/37/11.5/11.5; Ec. W1; 0.29/0.07/0.035 -> 0.395; 26 en 24 y 35 en 32; 15 de 72; 7 de 15; restriccion rechazada | R11 fila :226-250; DEC 2026-10-08 B ptos 15-20 | si (R11) |
| :256-258 | Tres metricas; hueso > 150 HU; volumen y Sorensen-Dice; umbral adaptativo; 5 % alto y bajo; regiones sobre rayas sin corregir; escala 0-4 no se traslada; copia exacta fuera de `G` | PET:174-175, :189-200, :236, :430; DEC 2026-10-09 (8) pto 2 | si (R11) |
| :258 | `\GAPDEC` RMSE/SSIM del protocolo fisico | TM:102; DA §7; DA0 (sin preservacion); `a24_contrastes.py` (sin RMSE/SSIM) | si; region **parcial (T04)** |
| :262 | Verdad de terreno; 33 = 19 (11 + 8) + 14; uno fuera por 1.62 mm; 13 | IMP #156 (:11263-11270); DEC 2026-10-09 (8) pto 3; DA0:50-52 | si (R11) |
| :264-270 | Anillos de 360 grados, guarda de un voxel, 12 mm, 8 mm; desviacion declarada; fraccion en el suelo; pose sin perturbar con `\GAPDEC`; 3.1/3.6/4.7 mm; sensibilidad n = 10; todos los cortes de `G`; 51 frente a 25; uno de cada dos | DEC 2026-10-05 (3)-(4); DA0:27-29, :40-56; DEC 2026-10-09 (4) pto 1, (8) pto 4 | si (R11) |
| :274-278 | Reconstruccion en 19 (11 + 8); MAE en `G`, `M`, `B_delta`; integridades; salto descontado; descriptivo; >= 500 mm3; 10 mm3; 24 cortes; > 15 h; medianas con rango; enmienda con errata; lectura de las integridades | DEC 2026-10-09 (8) ptos 1-2, 6; DA0:71-100 | si (R11) |
| :282 | Primario unico; solo metricas; lecturas humanas del Obj 2; control visual; `\GAPDEC` | DEC D4 pto 1; DEC 2026-10-08 pto 9 | si (justificado) |
| :284 | Tres contrastes; equivalencia primaria; realismo; cordura | DEC 2026-10-05 (3) pto 5; DA0:58-64 | si (R11) |
| :288 | Copia y pegado constante en `M`; 5373 HU; 1 978 270 voxeles; 17 149 parches; 47; corte central; CatSim/XCIST y AAPM | DEC 2026-10-09 (8) pto 5 | si (R11) |
| :290-298 | 2D y MAR; 1 fila, 900 columnas, 1 000 vistas; dispersion escalada a 64; FBP; 138 mm; fractales; fantoma fisico; reproduccion, no validacion; tres materiales; `(HU + 1000)/1000`; cinco desviaciones; `\GAPDEC` #158; `4cf3544`, `4993e87`, BSD 3-Clause; parche de una linea; `\GAPLIT` | PET; DEC 2026-10-05 (5); SON:87-119; IMP #146, #158 ABIERTA | si (R11) |
| :300-304 | Sonda en un paciente de validacion sin metal (`0101`); 72 h; +/-20 HU; 2 %; triple; salidas fijadas; 114.7 h; -2048 HU; +237/+276; camilla; -1000 HU; +3.9/+6.5; 72.8 veces, 10 166 frente a 140; 108.9 h; ~54 h | SON:19-22, :52-70, :123-152; DEC 2026-10-09 (2) pto 1 | si (R11) |
| :306 | Fe y Ti; replicas A y B que solo difieren en la realizacion del ruido, sin semilla fija; uno de cada dos cortes; acero en implantes espinales de 2.5-10 mm; lectura propia; Fe preinscrito; 13 pacientes; control sin metal; `\GAPDATO` | DEC 2026-10-09 (3); `a19_peters_completo.py`:15-16; PET:68; DA0:32-37 | si (T05 de r11 aplicado) |
| :308-312 | Sintetizador mas cerca de Ti; 815/1229, 5380/2205, 2051/1279 HU; regla sin el sintetizador; Ti 7 de 24, Fe 0 de 24, sobre lo real en 24; Ti primario; Fe 9895, Ti 5390 frente a 3092-3838 HU; 13 de 24; material desconocido | A20:45-48; DEC 2026-10-09 (5); A21:5-12; SON:151-152 | si (R11) |
| :316 | Wilcoxon de una cola, 0.05, pareado; mediana por paciente; 13; `\GAPDEC` del tamano de efecto | DEC D4 pto 2 (:1267-1268); DA0:64; `a24_contrastes.py`:87-96 (solo estadistico y p) | si (guia-9 de r11 aplicado) |
| :318 | TOST pareado frente a Ti; `\GAPDEC` #90; mediana de 5 semillas y de A/B; IC 90 % con *t*; 13; 188.7 HU; `\GAPDEC` del supuesto *t*; nunca por no significacion; `\GAPDEC` de desenlaces; sensibilidades Fe y n = 10 | DA0:45-47, :62-67; `a24_contrastes.py`:36-44; DEC 2026-10-09 (6) pto 2; IMP #90 ABIERTA | si (justificados) |
| :320 | Formula previa; `s_sem`; `r_rep` con Fe; 2 receptores; tercero fuera por 1.6 mm; 188.7 y 23.2 HU; Ti 0.4 y 5.2 HU | DEC 2026-10-09 (4) ptos 2-4; A20:18-34 | cifras si |
| :320 | **"un tercer paciente de validación sin metal"** (`0019`) | DEC 2026-09-21 (2):1386 (`0019`, accesorio metalico) | **no (T02)** |
| :324-326 | Realismo con los dos estadisticos; frente a tornillos aislados de prueba; fraccion por paciente; desglose; regla escrita antes; incierto fuera; placas excluidas; `\GAPDATO` de la lista | DEC 2026-10-09 (7); DA0:102-117; `docs/ESTADO.md`:35-36 | si (justificado) |
| :330 | Grado de cierre por objetivo; congela la evaluacion y no el modelo; **"se enumeran"** las decisiones post hoc | DA0:14-19; el propio `:101`, `:374` | parcial **(T03)** |
| Tabla `tab:diseno` | Filas 1-3: 2 x 3, 25 HU, 34, IC 95 %; 72 y 49; W1 sin regla; IC no preinscrito; estratificacion; 13; 19; Ti/Fe; TOST 188.7; fraccion de cascaras; Wilcoxon | R11 fila de la tabla | si (R11) |
| :352 | Circularidad; cuatro decisiones post hoc del Obj 2; 11 de 34 y 7 de 57; 91 | IMP #132, #136; DEC 2026-10-08 pto 17 | cifras si; lista **parcial (T03)** |
| :354 | 10/15 y 10/15; 7 de 15 frente a 2 de 15; `p = 0.109`, Fisher bilateral | IMP #132 | si (R11) |
| :356 | Exploracion previa; 25 HU anterior; rediseno posterior; cota de Guo et al. en prueba; percentil 5, ancho de cascara y material sin pacientes de prueba | DEC 2026-10-05 pto 4 (entrenamiento y validacion); DEC 2026-10-09 pto 2, (5) | si (T03 de r11 aplicado en el Obj 3) |
| :358-364 | Protrusion; `\GAPDATO` canal y foramenes; `\GAPDATO` techo de S1; 2 mm pediculares; Tejwani 2.5/5.0 mm, `p = 0.3`; S1 asumido; equiespaciado; `h = 2\sigma`; aleacion; truncamiento de rayas; Lin et al., Li et al. | R11 fila :356-362; fichas `smith2006iliosacral`, `tejwani2014`, `lin2019`, `li2024` | si (R11) |
| :366 | Suelo con sesgo a la baja; peso por contraste; una sola corrida; regla contra el primario sin conversion fijada | DEC 2026-10-08 A.12; IMP #141 ABIERTA; `:188` | si (T04 de r11 aplicado) |
| :368 | Protocolo fisico sin verdad; los dos materiales exageran; p95 bajo lo real; sentidos opuestos | DEC 2026-10-09 (3) pto 4; IMP #159 | si (R11) |
| :370-372 | Tile B y C; Reilly 6 pelvis, 5-20 mm, 36-90 %; 20 de 30; fraccion local; TS sin S1; protocolo 2D; tres desplazamientos; poses perturbadas fuera | ficha `reilly2003effect`; IMP #132; DA0:127 | si (R11) |
| :374 | 26 y 35 tornillos; W1 sin prueba; `\GAPDATO` del intervalo; multiplicidad; septimo candidato | PRE; DEC 2026-10-08 pto 18 | si (R11) |
| :376 | `\Delta` sobre 2 pacientes; favorece a un sintetizador inestable; `s_sem` de semillas sueltas frente a la mediana de 5; margen solo en corredores que admiten el tornillo (`0019` fuera por 1.6 mm) frente a tres angostos en prueba; sin regla comun; cortes distintos por brazo; 13 pacientes | DEC 2026-10-09 (4) ptos 3-4, (8) pto 4; DA0:43-44, :53-56 | si; omite la condicion de `0102` **(T02)** |
| global | Ninguna cifra de la corrida final en prueba | busqueda en el `.tex`; `docs/ESTADO.md`:5-28 | si |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet como metodo vigente, "31-60 %", BFC/ISC) | `CLAUDE.md` raiz; `docs/00-tesis.md` | ausente, salvo como exclusion (`:36`) o sustitucion (`:190`, figura) |
| global | Implicancias ABIERTAS afirmadas como hecho (#90, #141, #152, #157 p95, #158) | revision del texto | ninguna; todas con GAP o decision en DEC (BITACORA §2 2026-09-29) |
| global | Claves `\cite` en `overleaf/referencias.bib` | 33 claves distintas, iguales a r11 | si |
| global | Cita como sujeto (E-F3); apellido = primer autor | sin cambios desde r11 | si |
| global | Fabricantes y repositorios (P-EA1) | `:137`; repositorio AAPM sin cita y con GAP | si |
| global | Patrones VIGENTES de BITACORA §1 en mi dominio (PAT-11, 19, 20, 31, 39, 116, 120-123, 133, 134, 138, 139, 140) | revision del texto | PAT-20 (T01) y PAT-140 (T03) reinciden. Sin reincidencia de PAT-11, 19, 31, 39, 116, 120-123, 133, 134 y 139. PAT-138 escalado y no se repite |
| global | Decisiones de BITACORA §2 respetadas | §2 2026-10-10 (describir lo corrido y `\GAPDEC` si difiere de DEC) | no en T01; el resto si |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Hiperparametro copiado de una DEC que dice "tal como corrio" pero contradice el script y los metadatos del modelo | G-T4, OC-5 | "lotes de 4" (corridas con `--lote 16`) | PAT-20 |
| Etiqueta de grupo ("sin metal") aplicada a casos que la propia clasificacion del capitulo pone en otro grupo | G-T4, E-T1 | "las dos pelvis de validación sin metal" (una con cremallera) | nuevo |
| Remision que promete enumerar todas las decisiones post hoc y omite analisis anadidos tras ver datos | G-T4, G-C7 | "tomadas después de ver datos se enumeran en la Sección" | PAT-140 |
