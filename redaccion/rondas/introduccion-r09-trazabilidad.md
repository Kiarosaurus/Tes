# Auditoria de trazabilidad — introduccion — r09

Archivo: `overleaf/secciones/introduccion.tex` (estado previo a la respuesta de r09). Encargo:
`redaccion/ENCARGO_2026-10-15c.md` (introduccion: GAPDATO de la sensibilidad del Obj 2 -> e15). Fuentes nuevas cotejadas:
`experiments/objetivo2/e15_w1_sensibilidad.md` (E15), `experiments/registro/registro_metodos_2026-10-15.md` (REG),
`docs/01-decisiones.md` 2026-10-15 (4) (DEC4, l. 2696-2715). Encabezado (l. 3-17) y Formulacion (l. 21) siguen bajo #126
(ABIERTA): sus hallazgos ya ESCALADOS en r08 (guia-10, guia-11, T10; E-O1 y "robustos" de l. 7, PAT-173/174) no se
re-reportan.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2 | l. 94, ultima oracion | "con una sensibilidad sin los dos casos fallidos \GAPDATO{analisis de sensibilidad ... sin los dos casos ...}" | E15 :5-8; REG §8 :81-86; DEC4 pto 4 (l. 2711-2715); DEC 2026-10-08 pto 22 (l. 2143-2145) | Patron PAT-19 y PAT-122 reinciden: el GAPDATO declara ausente un resultado que ya existe. E15 da, sin `CLINIC_0022` y `CLINIC_0024` (70 casos, 3 500 poses), W1 0.203 frente a la serie navegada y 0.237 frente a la convencional; DEC4 pto 4 lo da por cerrado, descriptivo y sin cambiar cifras confirmatorias. PAT-168: la prosa fuera de la marca ("con una sensibilidad sin ...") tambien debe revisarse al cerrarla | Retirar la marca. Dos formas validas: (a) segun BITACORA §2 2026-10-15 (capitulo3-r23, medicion ejecutada sin lectura abierta): "..., y la variante se mantiene; una sensibilidad posterior y descriptiva sin los dos casos fallidos se reporta en el capitulo de resultados"; (b) con cifras, solo si van tambien las primarias para que se lean: "la distancia de Wasserstein-1 pasa de 0.206 a 0.203 frente a la serie navegada y de 0.230 a 0.237 frente a la convencional (72 y 70 casos)" (E15 :7-8). No escribir "no cambia el resultado": ninguna fuente lo dice. Alinear la formula con la que adopte capitulo3-r26 para el mismo cierre |
| T02 | media | OC-5, G-T4 | (fuentes de T01) | Cifras 0.203 / 0.237 de la sensibilidad del Obj 2 | `experiments/objetivo2/EXPERIMENTOS.md` (sin "e15", "0022" ni "remuestreo"); `docs/00-tesis.md`:65-70 (solo la sensibilidad de 49 volumenes) | Patron PAT-158 reincide: E15 y REG §8 no estan registrados en `EXPERIMENTOS.md` ni en `00-tesis.md`, que es de donde OC-5 manda copiar las cifras propias. No hay discrepancia (E15 reproduce 0.206 / 0.230 de `00-tesis.md`:68), solo atraso de la fuente | Si se usa la forma (b) de T01, citar en la respuesta la fuente `e15_w1_sensibilidad.md`:8 y avisar al orquestador / la autora para que `EXPERIMENTOS.md` (objetivo2) registre E15 (no lo edita el redactor) |
| T03 | baja | G-T4, E-R6 | l. 50, or. 4 | "Ese margen lo fija la variabilidad entre semillas del propio sintetizador" | DEC 2026-10-15 pto 21 (l. 2632-2633: 196.3 / `r` 6.1); #195 decision (implicancias l. 2489-2492); `resultados_validacion_pose.md`:51 | La regla es `Delta = max(s, r)` (rango entre semillas del sintetizador o prueba y reprueba del protocolo fisico); en el modelo evaluado gana `s` (196.3 frente a 6.1), asi que el hecho es cierto, pero la oracion lo da como regla general. #195 (DECIDIDA, opcion a) declara como limitacion justo que la regla favorece al metodo mas ruidoso | "Ese margen es el mayor entre la variabilidad entre semillas del sintetizador y la del protocolo fisico repetido, y en el modelo evaluado lo fija la del sintetizador, de modo que ..." (sin cifras de `r`; detalle en `sec:amenazas`) |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 3 | Metal, condicion mas dificil para segmentar pelvis | `liu2021ctpelvic1k` ficha :50 (encabezado bajo #126) | si |
| l. 5 | Artefactos ocultan limites y reducen calidad | `selles2024marreview`, `xie2024implantsegmentation` (no recotejado; #126, sin cambios desde r08) | si (r08) |
| l. 7 | 1 184 volumenes; 75 con metal (14 + 61) | `liu2021ctpelvic1k` ficha :30, :34, :35 | si |
| l. 7 | 1 109 sin metal anotados; 14 con metal anotados; 61 sin anotar | ficha :33-35 | si |
| l. 7 | "limita el desarrollo de modelos robustos" | PAT-174; ESCALADO #126 en r08 | escalado |
| l. 9 | Difusion latente reduce costo; ControlNet incorpora condiciones | `rombach2022latentdiffusion`, `zhang2023controlnet`; PAT-173 ESCALADO #126 | escalado |
| l. 11 | Evaluacion por tarea posterior en sintesis de tumores | `chen2024tumorsynthesis` (r08) | si |
| l. 13 | Dos componentes; dominio de imagen sin latente ni proyeccion; copia fuera de $G$ | DEC 2026-10-08 A.5; `00-tesis.md` | si |
| l. 15 | Coherencia de colocacion vs distribuciones clinicas; apariencia vs protocolo y copia y pegado | `00-tesis.md`; DEC 2026-10-08 pto 24; `\REVVISUAL` (#193) | si |
| l. 21 | Pregunta de investigacion | DEC 2026-10-08 pto 24; `\REVVISUAL`; #126 | si |
| l. 28 | Cuatro objetivos; Obj 1 previo; Obj 4 sin VD propia | DEC 2026-10-08 pto 23 | si |
| l. 32 | Unico implante: tornillo transilíaco-transsacro | `00-tesis.md`:71-73; #130 | si |
| l. 37 | MAE < 25 HU; seis combinaciones (2 x 3); 34 pacientes de prueba | `experiments/objetivo1/p1_compuerta.md`:25, :33-38 | si |
| l. 39 | Marco de Kaiser; holgura radial; escala de cuatro niveles; Zwingmann en S1; W1 | `kaiser2014dysmorphism`, `zwingmann2009navigated`; DEC 2026-10-08 ptos 15-17 | si |
| l. 41 | Banda de unos 12 mm; contraste primario Peters; copia y pegado como control de cordura | `00-tesis.md`; BITACORA §2 2026-10-15 (capitulo2-r07) | si |
| l. 41 | Comparacion con observaciones reales por estadisticos sin referencia | DEC 2026-10-08 pto 11; `\REVVISUAL` | si |
| l. 43 | Calibre 7.0 mm, holgura 1 mm | DEC 2026-10-08 pto 16 (l. 2127) | si |
| l. 43 | SAP con dos componentes; W1 en Obj 2 | DEC 2026-10-08 ptos 14, 17, 23 | si |
| l. 46 | Ida y vuelta sin autoencoder: 0.00 HU en dos codificaciones, 21.80 HU en la tercera (n = 34) | `p1_compuerta.md`:33-38 (columna identidad) | si |
| l. 46 | Codificacion adoptada: asinh en float32 | DEC 2026-10-08 pto 1 (l. 2080); REG §1 | si |
| l. 48 | Regla del Obj 1 posterior a exploracion, anterior a la prueba; 25 HU anterior | BITACORA §2 2026-09-29 (PAT-13); r08 | si |
| l. 48 | Obj 2 sin regla de decision; escala de lectura entre series | DEC 2026-10-08 pto 17 (l. 2129-2132) | si |
| l. 48 | Obj 4: controles identidad, monotonia, resolucion | DEC 2026-10-08 pto 23 | si |
| l. 50 | Regla de equivalencia previa; lectura posterior | DEC 2026-10-15 encabezado (l. 2563-2566), pto 15 | si |
| l. 50 | 13 pacientes de prueba; eje sin perturbar | `resultados_prueba_v1.md`:14; DEC 2026-10-15 pto 9 | si |
| l. 50 | IC90 entero dentro de $[-\Delta,+\Delta]$; $\Delta$ = 196.3 HU en dos pacientes de validacion | DEC 2026-10-15 ptos 15, 21; `resultados_validacion_pose.md`:51 | si |
| l. 50 | "Ese margen lo fija la variabilidad entre semillas del propio sintetizador" | #195 decision; DEC pto 21 | T03 |
| l. 50 | Tres elecciones en validacion acercan a la equivalencia | DEC 2026-10-15 pto 16 (#162 (3)) | si |
| l. 50 | Piso de ruido del sintetizador mayor y favorable al sintetizador | DEC 2026-10-15 (3) pto 3 (l. 2668-2672) | si |
| l. 50 | Desenlaces no equivalencia / no concluyente | DEC 2026-10-15 pto 15; DEC4 pto 1 (conserva los tres) | si |
| l. 52 | Diferencia media -301.0 HU; IC -477.0 a -124.9 HU | `resultados_prueba_v1.md`:14; `resultados_dec_2026-10-15.md`:39 | si |
| l. 52 | Cruza el limite inferior y queda bajo cero; "no concluyente", streak amplitude menor | DEC 2026-10-15 pto 15 (direccion con IC90); DEC4 pto 1 ("a la baja" respaldado tambien por IC95 [-516.2, -85.7], REG §9); C3 :419, :423 | si |
| l. 52 | Modelo evaluado = punto de control de v1 elegido en validacion | DEC 2026-10-15 pto 15 (`run04_mejor`) | si |
| l. 52 | Lectura en dos niveles, posterior a las dos versiones | DEC 2026-10-15 (3) pto 1 (l. 2658-2662) | si |
| l. 54 | Copia y pegado no produce rayas; el sintetizador la supera; no cuenta a su favor | DEC 2026-10-15 pto 12 (degeneracion) | si |
| l. 54 | `\GAPDATO` contraste de realismo sin script | `experiments/objetivo3/EXPERIMENTOS.md`:110 ("realismo (H5)" POR ESCRIBIR); REG :4-5 (nada nuevo del Obj 3 en test); dentro de `\REVVISUAL` | si (justificado) |
| l. 54 | v2 posterior y exploratoria; evaluacion ejecutada | DEC 2026-10-15 (3) pto 5; `resultados_dec_2026-10-15.md`:83-100 | si |
| l. 54 | `\GAPDATO` comparacion visual a ciegas sin script | `objetivo3/EXPERIMENTOS.md`:110 ("D3 a ciegas" POR ESCRIBIR); MAPA :151 | si (justificado) |
| l. 54 | v2 no concluyente en sus dos modelos, a la baja | `resultados_dec_2026-10-15.md`:90; DEC4 pto 2 | si |
| l. 58 | 14 de 75 anotados, 61 sin anotar | `liu2021ctpelvic1k` ficha :34-35 | si |
| l. 58 | Coherencia antes que utilidad | DEC 2026-10-08 pto 26 | si |
| l. 60 | Peters: metal al azar en entrenamiento; "meaningful locations" sin regla | `peters2025hybrid` ficha (r07-r08) | si |
| l. 60 | Liu 2025 optimiza una trayectoria; Zwingmann distribuciones por tecnica | `liu2025pipeline`, `zwingmann2009navigated` (r08) | si |
| l. 62 | De Man: causas de rayas; tres formas fuera del metal | `deman1999` ficha, "Donde entra" (r08, S09) | si |
| l. 62 | Difusion de lesiones acotada a mascara o corte entero desde ruido | `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`, `zhang2025diffboost` (r08) | si |
| l. 64 | MAR no pareada: componentes de otras imagenes con metal; sin evaluacion de la imagen sintetizada | `lyu2021ududonet`, `xia2024pndnet` (r08 guia-1); DEC 2026-10-15 (3) pto 9 | si |
| l. 64 | Formula de la brecha | DEC 2026-10-15 (3) pto 9 (literal); BITACORA §2 capitulo2-r08 | si |
| l. 66 | Eje sin perturbar: aisla apariencia y limita costo | DEC 2026-10-15 pto 9 (l. 2595-2596) | si |
| l. 66 | `\GAPDATO` exploratorio con poses del muestreador | `objetivo3/EXPERIMENTOS.md`:109-110 ("falta D9", POR ESCRIBIR) | si (justificado) |
| l. 66 | Peters: proyecciones por pose, 2D una fila, fractales | DEC 2026-10-08 pto 25; `peters2025hybrid` ficha | si |
| l. 68 | Xie: segmentacion por umbral cubre en exceso en cortes simulados | `xie2024implantsegmentation` ficha (r08) | si |
| l. 68 | Objetos alargados fragmentados; entrenamiento con mascaras umbralizadas | DEC 2026-10-08 pto 6 (E8 9 de 57; E11 4.91 mm) | si |
| l. 70 | Sin precedente que fije numericamente una banda; ventanas en MAR en reconstruccion o perdida | `wang2025adaptiveweighting`, `li2024` (r08); DEC 2026-10-08 pto 30 | si |
| l. 72 | Preinscripcion antes de cualquier W1; ningun parametro de Zwingmann | `00-tesis.md`:65-66 | si |
| l. 72 | Ninguna combinacion bajo 25 HU; saturacion del autoencoder TC ya supera | `p1_compuerta.md`:25; `00-tesis.md`:50 (r07-r08) | si |
| l. 76 | 178 de 1 184 volumenes | `docs/02-datos.md` (r07-r08) | si |
| l. 76 | Rama pubica: corredores por atlas, sin distribucion de grados | `goerres2017planning`, `han2019atlasplanning` (r08) | si |
| l. 78 | Segundo corredor sin distribucion clinica; eje medido | MAPA :66 (69 de 72); #121 | si |
| l. 78 | `\GAPDATO` preinscripcion y corrida en segundo corredor | MAPA :66; `objetivo2/EXPERIMENTOS.md` §6 (solo nivel, R2); REG no lo cubre | si (justificado) |
| l. 82 | Dice y HD95 fuera de alcance; 14 anotados | `00-tesis.md` Fuera de alcance pto 1 | si |
| l. 83 | Ablaciones de anclaje y escala diferidas | DEC 2026-10-08 pto 28 | si |
| l. 84 | XCIST validacion preliminar sin metal; Peters valida contra fantoma | `wu2022xcist`, `peters2025hybrid` fichas (r08) | si |
| l. 85 | Gardner: 222 mm$^2$ dismorfico frente a 346 mm$^2$ normal en S1 | `gardner2010safezones` ficha :72, :347 | si |
| l. 88 | Supuesto del dominio de imagen; De Man no lineal, aislado en sinograma | `deman1999` ficha; `\REVVISUAL` | si |
| l. 88 | Serie navegada asumida en S1 | `zwingmann2009navigated` ficha (r08) | si |
| l. 90 | Limites de grado de 2 mm desde pediculares via Smith | `gertzbein1990`, `mirza2003`, `smith2006iliosacral` (r08) | si |
| l. 90 | Desviacion estandar = mitad de 5 mm; ~95 % dentro | DEC 2026-10-08 pto 19 | si |
| l. 92 | Cribado: 30 casos (15 + 15), fractura en 20 de 30, 10 por grupo; medico sin especialidad | C3 (8 apariciones de los recuentos); #125 (r07-r08) | si |
| l. 94 | 16 casos revisados: 14 conformes, 2 fallaron con las dos variantes, 0 solo con la principal | MAPA :56; #123, #131 CERRADAS | si |
| l. 94 | `\GAPDATO` sensibilidad del Obj 2 sin los dos casos | E15 :8; REG §8; DEC4 pto 4 | T01, T02 |
| l. 96 | TotalSegmentator sin exactitud para S1 | `wasserthal2023` ficha (r08) | si |
| l. 96 | Discordancia de nivel: 11 de 34 y 7 de 57 | C3 (recuentos presentes); r05 PAT-65 | si |
| l. 96 | `\GAPDATO` envolvente y canal sacro / forámenes | MAPA :106; `objetivo2/` sin comprobacion (solo laminas de revision, `e9ts_revision_laminas.md`:41, no es la medicion); REG no lo cubre | si (justificado) |
| l. 98 | Reconstruccion no reportada; MAR o monoenergetica cambian apariencia | `selles2024marreview` ficha (r08); `\REVVISUAL` | si |
| l. 98 | Peters con dos materiales mayor que lo real; p95 del sintetizador por debajo en validacion | DEC 2026-10-15 (3) pto 6 (#191); C3 §Amenazas; `\REVVISUAL` | si |
| l. 100 | `\GAPDATO` estructura direccional dentro de $G$ | MAPA :135; #176 ABIERTA; REG no lo cubre; `\REVVISUAL` | si (justificado) |
| l. 100 | Banda de 12 mm contiene lo real; mas alla de 10 mm no se separa del control | C3 :262 (anillo 8-10 mm el mas lejano), :517; DEC 2026-10-15 (2) (medianas D1); dentro de `\REVVISUAL` (#193 la cita como truncamiento, no lo contradice para tamano tornillo) | si |
| l. 100 | Cortes y suelo no cambian el desenlace; piso favorece al sintetizador | DEC 2026-10-15 ptos 1, 17, 18; DEC (3) pto 3; `resultados_dec_2026-10-15.md`:34-63 | si |
| l. 102 | Tres desplazamientos de dominio; costura en los dos brazos (capitulo de resultados) | DEC 2026-10-08 ptos 6-7; DEC 2026-10-15 pto 5; MAPA :137 | si |
| l. 102 | Razon de tipos de parche medida antes de los ultimos retiros | REG §7 (0.638; 0.620 antes); el texto no da cifra y remite a `sec:sintetizador` | si |
| todo | #193 (ABIERTA) afirmada como hecho | Pasajes de realismo dentro de `\REVVISUAL` (l. 15, 21, 41, 54 x2, 88, 98, 100); proposito de $B_\delta$ (l. 13, 41) fuera por BITACORA §2 introduccion-r08; "Obj 3 se cumple" decidido en DEC (3) pto 1 | si |
| todo | Alcance retirado (Dice/HD95 como objetivo, difusion latente o ControlNet vigentes, "31-60 %", BFC/ISC) | l. 9 ControlNet en contexto (PAT-173, escalado #126); l. 46 dice que el veredicto descarto la difusion latente; l. 82 Dice/HD95 como exclusion | si |
| todo | Citas IEEE: claves en `referencias.bib`, sin cita como sujeto, apellidos del primer autor | Sin cambios de claves desde r08 (lint: sin citas indefinidas); "Peters et al.~\cite", "Walker" no aparece | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un registro nuevo cierra un GAPDATO el mismo dia y la seccion que lo replica conserva la marca | G-T4, OC-2 | "con una sensibilidad sin los dos casos fallidos \GAPDATO{...}" | PAT-19 / PAT-122 |
| Resultado nuevo en `experiments/` no asentado en `EXPERIMENTOS.md` ni `00-tesis.md` | OC-5, G-T4 | E15 (0.203 / 0.237) ausente de `objetivo2/EXPERIMENTOS.md` | PAT-158 |
| Regla de varias ramas (`max(s, r)`) resumida por la rama que gano en el caso | G-T4, E-R6 | "Ese margen lo fija la variabilidad entre semillas del propio sintetizador" | nuevo |
