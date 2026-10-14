# Auditoria de trazabilidad — capitulo3 — r19

Entrada: `overleaf/secciones/capitulo3.tex` (424 lineas, estado tras la respuesta r18), `capitulo3-r18-respuesta.md`
(sin RECHAZADO; T14 ESCALADO parcial), `capitulo3-r19-lint.md` (PASA; 14 bajas E-P1, cuyas cifras tienen fuente abajo).
Se revisa el texto tal como esta hoy. La version 2 del encargo `ENCARGO_2026-10-14.md` no se audita, porque todavia no
esta en el texto.

Fuentes nuevas desde r18, leidas en esta ronda:
- `experiments/objetivo3/resultados_prueba_v1.md` (RP1), evaluacion de prueba de la version 1, 2026-10-13. E-A2:
  principal `run04_mejor`, `Delta` 196.3, frente a Ti: -301.0 HU, IC90 [-477.0, -124.9]; Fe; sin angostos (n = 10);
  `run04_60k` con los dos margenes; Wilcoxon p = 0.000122; fraccion en el suelo 0.000. E-A1 (13 = 9 + 4): MAE en `G`,
  `M` y `B_delta`, SDC y dVol de hueso y metal, **exceso de costura** 6.3 y 9.0 HU. Pendiente: solo el realismo (sin
  script, sin lista de pacientes).
- `experiments/objetivo3/EXPERIMENTOS.md` (EXP):92, `resultados_prueba_v1.md` **HECHO** (#177). EXP:83 sigue con
  "`a23` ... resumen PENDIENTE" y EXP:84 con "`a24` ... LISTO, probado con datos de juguete".
- DEC 2026-10-13 pto 1: "La version 1 ya se evaluo tal como estaba preinscrita: no se concluye equivalencia con
  Peters Ti [...] (-301 HU, IC90 [-477.0, -124.9]) y supera la copia y pegado (#177)". DEC 2026-10-13 pto 4 y DEC
  2026-10-14 (2) declaran la version 2 posterior y exploratoria; el resultado principal sigue siendo run04.
- IMP #176-#182, todas ABIERTAS. #177: "Pendiente de la autora: nada que decidir sobre este resultado (el diseno
  estaba congelado)". #176, #178, #179, #180, #181 y #182 tocan la version 2, el cap. 2 o el cap. 4; ninguna
  contradice una afirmacion del cap. 3 sobre la version 1, salvo lo senalado en T07.
- `experiments/objetivo3/v2_plan.md` (V2P): version 2 planificada, entrenada y elegida por regla ("no mejora", #182).
  Su analisis exploratorio en prueba queda declarado y sin correr (EXP:40 `a20_v2` "POR CORRER").

Abreviaturas: DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; TES = `docs/00-tesis.md`; DAT =
`docs/02-datos.md`; EXP = `experiments/objetivo3/EXPERIMENTOS.md`; DAE = `experiments/objetivo3/diseno_A.md`; RVP =
`experiments/objetivo3/resultados_validacion_pose.md`; RP1 = `experiments/objetivo3/resultados_prueba_v1.md`; V2P =
`experiments/objetivo3/v2_plan.md`; A17p = `outputs/obj3_pose/a17_paso1mm/a17_cotejo.md`; A21p =
`outputs/obj3_pose/a21/a21_cotejo_material.md`; R18 = fila del inventario de `capitulo3-r18-trazabilidad.md` con
texto sin cambios desde entonces (o cambiado solo por la respuesta r18 de forma que lo cubre su fila), cotejada de
nuevo.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-2 | `capitulo3.tex:218` | "La corrida final sobre la partición de prueba se hizo solo con él, y su evaluación está pendiente." | RP1:10-40; EXP:92 ("HECHO (#177)"); DEC 2026-10-13 pto 1 ("La version 1 ya se evaluo tal como estaba preinscrita"); IMP #177 | **Patron PAT-122 reincide** (como afirmacion, no como GAP; afin a PAT-11). E-A2 (`a20` -> `a24`) y E-A1 (`a23`) ya se evaluaron el 2026-10-13 sobre la corrida final. Lo unico pendiente es el contraste de realismo (RP1:42-45). "Su evaluación está pendiente" es falso para el contraste primario, el control de cordura, las sensibilidades y la reconstruccion de implantes reales | "La corrida final sobre la partición de prueba se hizo solo con él, y sus resultados se presentan en el capítulo de resultados." Si se quiere el matiz: "salvo el contraste de realismo, cuya evaluación está pendiente (Sección~\ref{sec:ap-realismo})" |
| T02 | media | OC-2, G-T4 | `capitulo3.tex:38` (`\GAPDATO`) | "evaluación de esas dos ejecuciones [...]; los resultados del Objetivo~3 [...] no están disponibles" | RP1 (E-A2 y E-A1 completos); EXP:92; DEC 2026-10-13 pto 1 | **Patron PAT-122 reincide.** GAP injustificado en su mayor parte: las dos ejecuciones ya estan evaluadas y sus resultados existen (RP1). Solo falta el realismo, que no tiene script, y la lista de pacientes de su referencia, que ya tiene su propio `\GAPDATO` en `:351`. La oracion previa ("ya se ejecutaron") tambien queda corta | Prosa: "La generación de los dos brazos sobre la partición de prueba y la reconstrucción de implantes reales ya se ejecutaron y se evaluaron, y sus resultados se presentan en el capítulo de resultados." Marca reducida a lo que falta: "\GAPDATO{evaluación del contraste de realismo sobre la partición de prueba}", o retirarla y remitir al `\GAPDATO` de `:351`. Actualizar la fila de MAPA |
| T03 | media | OC-2, G-T4 | `capitulo3.tex:329` | "Su amplitud se evalúa junto con la de la corrida final" + `\GAPDATO{evaluación de la streak amplitude del protocolo físico ...}` | RP1:5-6 (`a20_ea2_test.csv`: "Peters 65 filas"), RP1:14-21 (TOST frente a Ti y Fe, n = 13) | **Patron PAT-122 reincide.** La amplitud del protocolo fisico sobre los 13 pacientes de prueba ya esta evaluada: entra en el TOST primario y en la sensibilidad con hierro de RP1. El GAP declara ausente un dato que existe (PAT-19) | "Su amplitud sobre los 13 pacientes de prueba se evaluó junto con la de la corrida final." Retirar el `\GAPDATO` (MAPA: -1 `\GAPDATO`) |
| T04 | alta | G-T4, OC-5 | `capitulo3.tex:226` | "Ese salto solo se midió una vez, sobre un caso, un corte y un punto de control distinto" | RP1:35-38 (columna "exceso costura": 6.3 HU en el grupo 1, n = 9, y 9.0 HU en el grupo 2, n = 4, con `run04_mejor`); `a23_ea1.py`:15 ("exceso de costura: salto de mediana a traves del borde de `G` en lo generado, menos el del real"); `a10_costura.py`:5 (#139, la medicion unica) | **Patron PAT-122 reincide** (afirmacion envejecida). El salto en el borde de `G` ya se midio con el modelo evaluado en la reconstruccion de implantes reales de los 13 pacientes de prueba, como lo describe `:297`. La medicion unica de #139 deja de ser la unica, y "no estima el del modelo evaluado" ya no vale para E-A1. Lo que sigue sin medirse es el salto en la sintesis sobre pelvis sin metal, que es lo que pide el `\GAPDEC` | "Fuera de la reconstrucción de implantes reales, ese salto solo se midió una vez [...], de modo que en la síntesis sobre pelvis sin metal no hay medida del modelo evaluado." La cifra de E-A1 va al capitulo de resultados (PAT-151) |
| T05 | media | OC-3, G-T4 | `capitulo3.tex:341` (`\GAPDEC` #90) | "la contingencia de plazo [...], que permitía pasar esta comparación a trabajo futuro, sigue abierta" | IMP #90 (:6464, :8120) ABIERTA; DEC 2026-10-13 pto 1; RP1:14 (TOST primario frente a Ti ya calculado) | **Patron PAT-116 reincide.** La comparacion de equivalencia ya se ejecuto y se evaluo como contraste primario (RP1; DEC 2026-10-13). La contingencia de #90 era no entregarla, y el hecho registrado la deja sin efecto. Formalmente #90 sigue ABIERTA, asi que el GAP no puede borrarse solo, pero su texto ("permitía pasar ... a trabajo futuro") describe una opcion que ya no puede ocurrir | Escalar a la autora: cerrar #90 por ejecucion (la comparacion se entrego). Despues se retira el `\GAPDEC` (MAPA: -1 `\GAPDEC`). Mientras tanto, se reescribe asi: "\GAPDEC{cierre formal de la contingencia de plazo (implicancia 90): la comparación ya se ejecutó como contraste primario}" |
| T06 | alta | G-T4, OC-5, OC-3 | Fuentes: TES:117, :149-156; DAE:29, :32-34; DEC 2026-10-11 (3) ptos 1-4 (:2465-2474); `tesis/main.tex`:79; EXP:83-84; IMP #175 ABIERTA | (fuente) "12 frente a 10"; "`Delta` 163.8 / 100.3"; "corrida final ... en curso"; "`a24` LISTO, probado con datos de juguete" | RP1:7, :14 (TOST evaluado con `Delta` 196.3 de RVP §3); EXP:63, :92; IMP #174, #175, #177 | **Patron PAT-138 / PAT-158 reincide. Re-apertura de T14 (r18, ESCALADO), con argumento nuevo:** el resultado primario de prueba ya se calculo con 196.3 HU (RP1:14). Las fuentes que conservan 163.8 / 100.3 contradicen ahora un resultado evaluado, y no solo una cifra de validacion: TES:156, DAE:32-34 y DEC 2026-10-11 (3) pto 3. DEC 2026-10-11 (3) no tiene una entrada posterior que lo sustituya, y #175, la que lo hace, sigue ABIERTA. Hay otros desfases. `tesis/main.tex`:79 conserva "12 of 24 ... against 10". TES:117 sigue con "la corrida final de test sigue en curso". EXP se contradice a si mismo: :83 da el resumen de `a23` como PENDIENTE y :84 da `a24` como "probado con datos de juguete", mientras que :92 da RP1 como HECHO. El capitulo copia la fuente correcta (RVP, RP1), pero la regla del auditor exige marcar la discrepancia entre fuentes | Escalar a la autora: (1) DEC: una entrada que sustituya los ptos 1 y 3 de 2026-10-11 (3) (13 frente a 7; 196.3 / 115.8), o cerrar #175; (2) TES :117 y :149-156; (3) DAE ENMIENDA :29 y :32-34; (4) `tesis/main.tex`:79; (5) EXP :83-84 a CORRIDO / EVALUADO con remision a RP1. El redactor no puede editar ninguno de ellos |
| T07 | baja | G-T4, PAT-20 | `capitulo3.tex:204`, `:214`, `:212` | "corren en tarjetas gráficas del mismo tipo y de uso exclusivo"; "se reportan y no se filtran"; "El modelo evaluado" | V2P:24-31 (R4 cambia a sobremuestreo, "Se declara como cambio de la version 2"), V2P:72-73 (run05b en `a100_3g`, compartida); DEC 2026-10-14 pto 1; DEC 2026-10-14 (2) pto 2 | Las tres frases son ciertas para la version 1, que es lo unico que el texto describe hoy. Cuando entre la version 2 (encargo 2026-10-14), dejaran de ser ciertas sin acotarse: la v2 sobremuestrea por tamano, corre en otra GPU y suma dos modelos evaluados en prueba (de forma exploratoria). Es un aviso para el redactor, no un error del texto actual | Al incorporar la v2, acotar cada una a "el modelo de la versión 1" o declarar el cambio de la v2 junto a ella (V2P:30-31). "El modelo evaluado" sigue siendo run04 para el contraste primario (DEC 2026-10-14 (2) pto 1) |
| T08 | baja | PAT-116, G-T4 | `capitulo3.tex:289` | "Si esa fracción no es nula, la cola inferior queda censurada y la amplitud medida es una cota" | RP1:24-25 ("Fraccion de la ROI en el suelo de -1000 HU: 0.000 (maximo por paciente)"); RVP:47 (0.000 en validacion) | **Patron PAT-116 reincide (leve).** Es un condicional sobre un resultado que ya se conoce: la fraccion es nula en validacion y en prueba. Como metodo es correcto, pero el lector no sabe que la rama no se activo | Sin cambio en el metodo. Se puede agregar la remision "(su valor se presenta en el capítulo de resultados)", o dejarlo y dar el 0.000 en el cap. 4 |

## Inventario

Una fila por unidad verificable, en el orden del `.tex`. "R18" indica texto sin cambios (o cambiado por la respuesta
r18 tal como pedia su fila) y cotejado contra la misma fuente.

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9-15, Fig. `fig:pipeline` | Dos componentes; compuerta; cuatro objetivos; SAP como unica metrica propia; `M`, `B_delta`, `G`; evaluacion sobre el eje sin perturbar | R18; DAE:56-57 | si (R18) |
| :36 | Dice y HD95 y ablaciones fuera de alcance; 14 de 75; 178 de 1 184 | TES *Fuera de alcance*; `liu2021ctpelvic1k` | si (R18) |
| :38 | Compuerta negativa; Obj 2 ejecutado; modelo elegido en validacion; dos brazos y E-A1 ejecutados | IMP #174 (a); EXP:63, :83; RP1:3-6 | si |
| :38 | `\GAPDATO` "evaluación de esas dos ejecuciones [...] no están disponibles" | RP1; EXP:92; DEC 2026-10-13 pto 1 | **GAP injustificado (T02)** |
| :40 | Congelado el 9-10; enmiendas del 11-10 y del 12-10; regla de realismo con informacion de prueba; corrida final con pose corregida; generaciones con pose equivocada archivadas sin evaluar | DAE:21-48; IMP #173; OBS:112-133 (`a15_final_run04` archivado) | si |
| :44-48 | 103 y 75; correspondencia inferida; MAR no reportada (Selles et al.); 2500 HU; revision 3D de 178; `\GAPDATO` multiplanar | R18; DAT:162; ficha `selles2024marreview` | si (R18) |
| :50 | SHA256; 168 = 65 + 37 + 66; 179 unidades; 10 + 1 | DAT:120, :136-137 | si (R18) |
| :52 | Aislamiento; validacion 8, prueba 34; Obj 3 reutiliza; Obj 2 con grupos 2 y 3 | R18 | si (R18) |
| :54 | Adquisicion repetida; primaria por espaciado; 33; 2.3 HU | IMP #156; `experiments/objetivo1/p1_sin_0053.md` | si (R18) |
| :56 | Recuento del 11-10; siete secundarios; tercera adquisicion y clavo femoral; paciente compartido, primario el de prueba | DEC 2026-10-11 (4) pto 1; IMP #163, #166 | si (R18) |
| :58 | Fuga en la compuerta remitida a §Amenazas | IMP #166; `p1_sin_0072.md` | si (R18) |
| :60 | Auditorias no exhaustivas; huellas y firmas metalicas; sin cubrir los pacientes sin metal; hallado por la autora | IMP #163 "No cubierto"; IMP #166 Origen | si (R18) |
| :62 | 166 = 159; 118 (125), 8, 33; 20 + 13; 9/10/14; 59/41/66 por volumen | DEC 2026-10-11 (4) pto 2; DAT:149-160 | si (R18) |
| :64 | 103 -> 91 -> 72; dos situaciones del control; 11 de 34; 7 de 57; 1 en el borde; 49 | IMP #132, #136 | si (R18) |
| :66-68 | 20 de 30 (67 %); 10/15 y 10/15; caso dudoso; medico recien egresado; 18 + 12; 7 y 5 | IMP #132, #155 | si (R18) |
| :70 | Cuatro funciones; tornillos fragmentados; fuste con HU bajos en tres pacientes | IMP #155, #163 | si (R18) |
| :74-91 | Compuerta; exploracion previa; VAE de SD 1.5; lectura del Obj 1; 150 HU; MAE; 25 HU; 20.2 / 12.3 / 12.74 HU; 2 x 3; dos volumenes de entrenamiento = adquisiciones de prueba; `\GAPDATO` del decodificador; ventanas de Wang; 20 000 HU; arcsinh; IC 95 %; orden a priori; 12 mm / 2500 HU; Rombach; Guo | fichas `karageorgos2024ddpm`, `yun2026simulationdriven`, `wang2025adaptiveweighting`, `rombach2022latentdiffusion`, `guo2025maisi`, `peters2025hybrid`, `haneda2025aapm`; IMP #156, #166 | si (R18) |
| :95-119 | Zwingmann; Ziran 7-25 % y 140 %; Kaiser 5 y 10 mm; 0.42; TS 2.18.0; 6 y 3 mm; 0.1 %; 104 estructuras; 2 mm; 72; 8 mm; 9.5 (7.4-11.7) mm; 65.3/23.6 y 62.5/20.8 %; 29 y 27; 5 %; 16 = 14 + 2 + 0; `\GAPDATO` x 3; 69 frente a 66; 64; 57/7/6/48/29/17/3; 0 TS segun la autora; 61 de 61; 12 de 16 | R18; fichas `zwingmann2009navigated`, `ziran2007fluoroscopic`, `kaiser2014dysmorphism`, `wasserthal2023`, `isensee2021`, `mclaren2021corridor` | si (R18) |
| :123-147, Tabla `tab:geometrias` | Ilion a ilion; McLaren; 4.91 mm; 7.0 mm; cabeza 8.0 x 4.5 mm; 4.8 / 4.9 / 4.7 mm; 79 componentes de 43 volumenes; 30 y 12 mm; `\GAPDEC` de la cabeza; 1.5 mm; 316L y Ti-6Al-7Nb; fabricantes como documentacion no revisada por pares (P-EA1) | R18; fichas `gardner2010safezones`, `sayres2014comparison`, `synthes2003guide`, `gardner2015screw`, `zhu2022optimalposition`, `doublemedical2021trauma` | si (R18) |
| :151-192, Tabla `tab:preinscripcion` | 22-09-2026; anclaje; Ec. de pose; 5.0 y 2.5 mm; 2.07 grados; 138 mm; 3 sigma; 50; semilla 20260922; 95 %; 4 grados; tres controles; 18 = 13 + 4 + 1; 39/36/33 mm; 69 de 72 + `\GAPDATO`; Arand; Gardner | R18; `experiments/objetivo2/preinscripcion_muestreador.md` | si (R18) |
| :196-200 | *Inpainting* 2.5D; arcsinh en float32; regla del suelo con percentil 5 + `\GAPDEC`; ControlNet sustituido | R18; IMP #141 ABIERTA; ficha `zhang2023controlnet` | si (R18) |
| :202 | U-Net 64 (1, 2, 4, 8); $v$ + `\GAPLIT`; coseno 1000; AdamW 1e-4; lote 16 + `\GAPDEC`; 256; 3 cortes; DDIM 50; RePaint; LeFusion | R18; IMP #162 ABIERTA; fichas `song2021ddim`, `lugmayr2022repaint`, `zhang2025lefusion` | si (R18) |
| :204 | 5 semillas; tarjetas del mismo tipo y exclusivas para lo que se compara; E-A1 en una porcion compartida | DAE:46-48; EXP:63 (rtxa6000 g002), :83 ("shard rtxa6000") | si; acotar a la v1 al entrar la v2 **(T07)** |
| :206 | Mezcla de canales; 0.01 y 0.05; caso particular; Obj 1 sin cambio | DEC 2026-10-07; IMP #152 | si (R18) |
| :208 | 0.05 fijado con modelos anteriores; 0.030 y 0.05 recalibrados; cada punto de control con su limite; cotejo, margen, corrida final y E-A1 calculados asi | IMP #172; EXP:63, :83 (`a23` con 0.030); RVP:3-4 | si |
| :210 | 12 mm; RMSE 7.57 / 11.45 / 11.63 / 54.82 / 57.69 HU; 1.4 / 1.8 / 0.7 / 0.5 | ficha `karageorgos2024ddpm` | si (R18) |
| :212 | 2500 HU; semimaximo + `\GAPDEC`; componente conexo; eje sin perturbar; punto de control elegido por cotejo; aislamiento segun las auditorias | R18; DAE:41-45 | si |
| :214 | Tres reglas; 0.62 + `\GAPDATO`; supuesto no verificado; 5 de 40; no se filtra | DEC 2026-09-21; V2P:26 ("5 de 40") | si; R4 cambia en la v2 **(T07)** |
| :216 | 14 182 parches de 39 casos; 896 de 3; secundarios; 3 componentes | EXP:26-27; TES:121-123; IMP #167; V2P:29 | si (R18) |
| :218 | Reentrenamiento; modelos afectados; prueba evaluada con uno; repetidos cotejo, `Delta` y copia y pegado; ninguna cifra de un modelo afectado; heredados | IMP #171; R18 | si |
| :218 | "y su evaluación está pendiente" | RP1; EXP:92; DEC 2026-10-13 pto 1 | **no (T01)** |
| :220 | Error de pose detectado por la autora; eje en volumen reorientado; tornillo reflejado y fuera del sacro; control de pose > 5 % de `M` bajo -500 HU o mediana > 150 HU bajo la del eje; cordura, no preinscrito; 15 = 2 + 13 | IMP #173 (:11948-11972); RVP:5-6 ("15 de 15 PASAN") | si |
| :222 | Que se rehizo y que no; dos brazos con la misma pose; recuento de cortes como excepcion; sonda no repetida | IMP #173 Alcance (:11960-11964); IMP #174 (c); IMP #160 | si |
| :224 | Tres desplazamientos; 0.62 frente a 1.40; primera razon anterior a los retiros | DEC 2026-10-08 A.6-A.7; TES:125-127 | si (R18) |
| :226 | 9 de 57; 4.91 mm; salto medido solo en E-A1 segun el diseno + `\GAPDEC` | DAE §0 l. 97; `a23_ea1.py`:15 | si |
| :226 | "Ese salto solo se midió una vez [...] no estima el del modelo evaluado" | RP1:35-38 (exceso de costura en E-A1 con `run04_mejor`); `a10_costura.py`:5 | **no (T04)** |
| :228 | 60 000 pasos; minimo en 16 500; candidatos fijados antes; solo dos; 39 casos | IMP #168; DEC 2026-10-11 (2) pto 1 | si (R18) |
| :230-236 | Tarea de sintesis; dos receptores con $D \geq 9$ mm, uno con cremallera; 1.6 / 7.0 / 8.9 mm + `\GAPDEC`; cascaras de 1 mm; 0.896 mm; p50 y p95 sobre 12-15 mm; medianas; p50/p75/p95 > 2500 HU; 2 tornillos de un paciente confirmados en cortes; intervalo; desempates | R18; `experiments/objetivo2/e9ts_corredor.csv`; RVP:7 | si (R18) |
| :238 | 13 de 24 frente a 7; 9 frente a 3; 4 frente a 4; sin empate; 393 frente a 270 HU | RVP:19-20; A17p:16-17 | si |
| :240 | p95 bajo lo real en 7 de 12 en los dos; `\GAPDEC` (#157); 3245 / 4856 y 3402 / 4848 HU; medianas reales 3465 y 5283 HU; 497 frente a 648 HU | RVP:19-23 (3465 = (3838 + 3092) / 2; 5283 = (5262 + 5304) / 2, derivacion declarada en la respuesta r18) | si |
| :242 | Sensibilidad con el estado final; motivo con pose equivocada; 1164 / 1163 frente a 1248 / 1182 HU; Ti 1881 / 1287 HU; elegido mas cerca del Ti; lectura conservadora | RVP:42-45 (Ti 1881 = mediana de 1885 y 1877; 1287 = de 1300 y 1273); IMP #174 (a), #175 | si |
| :245-273 | SAP, $D \geq 9$ mm; Smith; Ec. de brecha; 0/2/4 mm; tramo $T$ y 8 mm; 1 + 5 controles; 0.083 mm; 69/15/8/8 y 40/37/11.5/11.5 %; W1; 0.29 / 0.07 / 0.035 -> 0.395; 26 en 24 y 35 en 32; 15 de 72; restriccion rechazada | R18; fichas `smith2006iliosacral`, `zwingmann2009navigated` | si (R18) |
| :279-281 | Tres metricas; 150 HU; Sorensen-Dice; umbral adaptativo; 5 %; limitacion de Peters; escala 0-4; `\GAPDEC` RMSE/SSIM | ficha `peters2025hybrid` | si (R18) |
| :285 | 33; 19 = 9 + 10; 14 sin metal; uno fuera por 1.62 mm; 13 | DEC 2026-10-11 (4) pto 3; DAT:154, :157; TES:163-168 | si (R18) |
| :287-293 | Anillos de 360 grados; guarda de un voxel; 12 mm; 8 mm; fraccion en el suelo; pose sin perturbar + `\GAPDEC`; 3.1 / 3.6 / 4.7 mm; n = 10; 51 frente a 25 con la pose anterior; uno de cada dos | R18; IMP #160; RP1:16 (n = 10) | si; el condicional del suelo ya tiene resultado **(T08)** |
| :297-301 | Cohorte de diseno 19; MAE en `G`, `M` y `B_delta`; integridades; salto con el real descontado; >= 500 mm3; 10 mm3; 6 sin componentes; 13 = 9 + 4; 24 cortes; > 15 h; enmienda con errata | DEC 2026-10-11 (4) pto 3; DEC 2026-10-09 (8); RP1:31-38 (13 = 9 + 4; columnas coinciden con lo descrito); `a23_ea1.py`:15 | si |
| :305-307 | Criterio primario unico; sin lector clinico; control visual + `\GAPDEC`; tres contrastes; cordura | R18 | si (R18) |
| :311 | Tres brazos; 5371 HU; 1 781 741 voxeles; 14 182 parches; 39 casos; CatSim/XCIST; AAPM; reimplementacion fuera de alcance | EXP fila `a22`; DEC 2026-10-11 (3) pto 5; fichas `deman2007catsim`, `wu2022xcist`, `haneda2025aapm` | si (R18) |
| :313-321 | 2D/MAR; 900 columnas; 1 000 vistas; 64; 138 mm; fractales; fantoma; tres materiales; $(\mathrm{HU}+1000)/1000$; cinco desviaciones; 459 mm; $[0.5, 3]$; `\GAPDEC` #158; `4cf3544`, `4993e87`, BSD; parche de una linea; `\GAPLIT` | ficha `peters2025hybrid`; IMP #146, #158 ABIERTA | si (R18) |
| :323-327 | Criterios de la sonda (72 h; +/-20 HU; 2 %; triple); pose anterior a la correccion; salidas fijadas; -2048 HU; camilla; segunda corrida; un corte de cada dos; veredicto confirmado por el protocolo completo con la pose corregida | `sonda_peters.md`; IMP #174 (c); EXP fila `a19_pose` | si |
| :329 | Fe y Ti; A y B sin semilla; uno de cada dos cortes; 2.5-10 mm; Fe preinscrito; control sin metal; 13; ya corrido con la pose corregida | DEC 2026-10-09 (3); ficha `peters2025hybrid`; EXP:63; RP1:5 (job 56245) | si |
| :329 | "Su amplitud se evalúa junto con la de la corrida final" + `\GAPDATO` | RP1:5-6, :14-21 | **GAP injustificado (T03)** |
| :331 | Observacion con modelo afectado y pose equivocada; se mantiene; Fe 5243 / 2166 y Ti 1881 / 1287 HU; sintetizador 1069-1361 y 1131-1232 HU; regla sin sintetizador | RVP:42-45 (Fe 5243 = mediana de 5246 y 5239; 2166 = de 2163 y 2168); IMP #161, #171, #175 | si |
| :333 | Misma regla; A y B como semillas; Ti 2 de 24 frente a 0 de 24 con Fe, sobre lo real en 24; Ti primario, Fe sensibilidad; cambio posterior | RVP:31-34; A21p:9-10; IMP #174 (b) | si |
| :335 | Ningun material reproduce lo real; Ti 22 de 24 sobre lo real; `M` 7036 y 4462 HU; 3092 a 3838 HU; escaner sin material; mismo alcance que el cotejo | RVP:23, :31-34; IMP #174 (b) | si |
| :339 | Wilcoxon de una cola, 0.05, pareado; mediana por paciente; 13; `\GAPDEC` del tamano de efecto | DEC D4 pto 2; RP1:23 (n = 13, una cola) | si (R18) |
| :341 | TOST pareado frente a Ti; medianas de 5 semillas y de A/B; IC 90 %; 196.3 HU; *t* + `\GAPDEC`; `\GAPDEC` del desenlace; sensibilidades con Fe, estado final y n = 10 | RVP:51; RP1:12-21 (mismos contrastes); IMP #175 | si |
| :341 | `\GAPDEC` de la contingencia de plazo (#90) | IMP #90 ABIERTA; DEC 2026-10-13 pto 1; RP1:14 | GAP superado por la ejecucion **(T05)** |
| :343 | Formula previa; $s_{\mathrm{sem}}$ como rango; $r_{\mathrm{rep}}$ con Fe; dos receptores; 196.3 y 6.1 HU; $\Delta$ = 196.3 HU; Ti 8 y 27 HU | RVP:49-54; DEC 2026-10-09 (4) | si |
| :345 | El margen lo fija el sintetizador; estado final 115.8 HU; dos margenes | RVP:52; DEC 2026-10-11 (3) pto 4 (lectura); RP1:17-21 | si |
| :349-351 | Realismo; tornillos aislados de prueba; fraccion de cascaras; histograma sin resumen; regla; incierto fuera; placas fuera; `\GAPDATO` de la lista | DEC 2026-10-09 (7); IMP #167; RP1:42-45 (sigue pendiente) | si |
| :355, Tabla `tab:diseno` | Grado de cierre; congelado y enmendado el 11 y el 12; run04 entrenado antes de la enmienda; fila 1 (34; IC 95 %); fila 2 (72 y 49); fila 3 (13; 196.3 HU; "13 de los 19"; Ti con Fe como sensibilidad) | DAE:21-48; DEC 2026-10-11 (2)-(4); RVP:51 | si |
| :377-381 | Circularidad; post hoc del Obj 2; 11 de 34; 7 de 57; 91; 10/15; 7 de 15 frente a 2 de 15; $p = 0.109$; exploracion del Obj 1; fuga del afinado con 32 pacientes; Guo | R18; `p1_sin_0072.md` | si (R18) |
| :383-385 | Percentil 5; sonda dos veces, con la pose equivocada y confirmada despues; cortes de solo banda; cascara y cotejo antes de run04; material con Ti por 2 frente a 0; sensibilidad por la distancia en `M` | R18; IMP #174 (a)-(c) | si |
| :387 | Regla de realismo con 3 de 11; dos pasan al grupo 2; 9; tornillo no listado | DEC 2026-10-09 (7); DEC 2026-10-11 (4) | si (R18) |
| :389 | Siete decisiones tras la evaluacion previa; cinco con criterio previo; dos sin regla | IMP #171, #172, #167 | si (R18) |
| :391 | Pose corregida tras ver sinteticas de prueba; posicion medida sin criterio de evaluacion; archivadas; evaluacion previa tambien con pose equivocada; control de pose no detuvo ningun caso | IMP #173 Origen y Medido (:11948-11951); RVP:5-6 | si |
| :393-395 | Tres elecciones sobre dos receptores; un unico paciente con tornillos; limite calibrado; sentido conjunto; 196.3 frente a 115.8 HU; `\GAPDEC` #162 | IMP #162 ABIERTA; IMP #175; RVP:51-52 | si |
| :397 | Aislamiento hasta donde llegan las auditorias; sentido por objetivo | IMP #163, #166 | si (R18) |
| :399-409 | Protrusion; `\GAPDATO` x 2; 2 mm; Tejwani 2.5 y 5.0 mm, $p = 0.3$; S1 asumido en la serie navegada; equiespaciado; $h = 2\sigma$; 19 de 39; Lin, Li | fichas `smith2006iliosacral`, `tejwani2014`, `lin2019`, `li2024`; IMP #167 | si (R18) |
| :411-413 | Suelo; una sola ejecucion local como apoyo de la diferencia entre brazos; los dos materiales exageran; p95 bajo lo real; lectura del desenlace no fijada | IMP #141 ABIERTA; A21p; RVP:22; RP1:27-29 (sigue sin fijar) | si |
| :415 | Tile B y C; Reilly, 6 pelvis, 5-20 mm, 36-90 %; 20 de 30 | ficha `reilly2003effect`; IMP #155 | si (R18) |
| :417 | Fraccion local; S1 sin exactitud; 2D; desplazamientos; poses perturbadas fuera; 0 TS en 56; candidatos por forma | IMP #165, #167 | si (R18) |
| :419-423 | 26 y 35; W1 sin prueba; `\GAPDATO`; multiplicidad; septimo candidato; `Delta` sobre 2 pacientes; corredores viables; 3 angostos; objeto en un receptor; cortes distintos; 13 | R18 | si (R18) |
| fuentes | TES, DAE, DEC 2026-10-11 (3), `tesis/main.tex`:79 y EXP:83-84 frente a RVP, RP1 y EXP:63/:92 | ver T06 | discrepancia **(T06)** |
| global | Afirmaciones que el resultado de prueba de la v1 deja desfasadas (evaluacion pendiente, resultados no disponibles, amplitud de Peters por evaluar, salto medido una sola vez) | RP1; EXP:92; DEC 2026-10-13 pto 1 | **4 lugares (T01-T04)**; ninguna cifra de RP1 entra en el cap. 3, lo que es correcto (PAT-151) |
| global | Version 2 (DEC 2026-10-13, 2026-10-14, 2026-10-14 (2); IMP #176-#182; V2P) | revision del texto | no aparece; nada del texto la contradice para la v1; avisos para el encargo **(T07)** |
| global | Ninguna cifra de modelos afectados ni de la pose espejada (188.7, 5373, 163.8, 100.3, 23.2, 12 de 24, 342, 810, 749, 977, 2051, 5380, 901, 7 de 24, 9895, sonda) | busqueda en el `.tex` | si (ausentes) |
| global | Contenido retirado (Dice y HD95 como objetivo, difusion latente o ControlNet vigentes, "31-60 %", BFC/ISC) | `CLAUDE.md` raiz; TES | ausente; solo como exclusion (`:36`) o sustitucion (`:200`, figura) |
| global | Implicancias ABIERTAS (#90, #138, #141, #157, #158, #162, #168, #173, #175, #176-#182) | revision del texto | como GAP o limitacion; #90 superada por la ejecucion **(T05)**; #173 y #175 usadas como medidas, criterio de la respuesta r18 (encargo de la autora) |
| global | Claves `\cite` en `overleaf/referencias.bib`; E-F3; apellido = primer autor | sin claves ni citas nuevas desde r18 | si |
| global | Fabricantes y repositorios (P-EA1) | `:147`; repositorio AAPM con `\GAPDEC` y `\GAPLIT` (`:319`, `:321`) | si |
| global | Patrones VIGENTES de BITACORA §1 en mi dominio (PAT-11, 13, 19, 20, 39, 116, 120-123, 133, 134, 138, 140-158) | revision del texto | Reinciden PAT-122 (T01-T04), PAT-19 (T03), PAT-116 (T05, T08), PAT-138 y PAT-158 (T06). PAT-20 es un riesgo al entrar la v2 (T07). No reinciden PAT-11 (salvo en T01), 13, 39, 120, 121, 123, 133, 134, 140-157 |
| global | Decisiones de BITACORA §2 respetadas | §2 r18 (definicion de "corrida final"; implicancia ABIERTA solo por redaccion con cifras en EXP entra como medida) | si; no se reportan como error las cifras de #175 |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Afirmacion o GAP de estado ("pendiente", "no disponible", "se evalua junto con") que la evaluacion posterior deja falsa | OC-2, G-T4 | "La corrida final [...] se hizo solo con él, y su evaluación está pendiente" | PAT-122 |
| Afirmacion de unicidad de una medicion ("solo se midió una vez") que una evaluacion posterior con el modelo vigente desmiente | G-T4, E-P3 | "Ese salto solo se midió una vez, sobre un caso, un corte" | PAT-122 / PAT-148 |
| GAPDEC sobre una contingencia que la ejecucion registrada ya deja sin efecto, con la implicancia formalmente abierta | OC-3, G-T4 | "la contingencia de plazo [...] que permitía pasar esta comparación a trabajo futuro" | PAT-116 |
| Fuentes de contenido (TES, DAE, DEC, TM, EXP) con cifras de validacion sustituidas que ahora contradicen un resultado de prueba ya evaluado | G-T4, OC-5 | DEC 2026-10-11 (3) "`Delta` 163.8 HU" frente a RP1 "`Delta` 196.3" | PAT-138 / PAT-158 |

alta=3 media=3 baja=2
