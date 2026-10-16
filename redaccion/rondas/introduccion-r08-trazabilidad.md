# Auditoria de trazabilidad — introduccion — r08

Alcance: `overleaf/secciones/introduccion.tex` completo (l. 1-98). Encargo: `redaccion/ENCARGO_2026-10-15b.md`
(E1 `\REVVISUAL`; E2 alinear con DEC 2026-10-15 (3); E3 `\GAPLIT` si falta fuente). Respuesta previa:
`introduccion-r07-respuesta.md` (nada RECHAZADO; T09-T13 y el encabezado l. 3-21 ESCALADOS por #126, ABIERTA).

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; 00T = `docs/00-tesis.md`;
DEC15 = `docs/01-decisiones.md` 2026-10-15 (l. 2559-2634); DEC15-3 = 2026-10-15 (3) (l. 2650-2694); IMP =
`docs/04-implicancias.md`; EXP3 = `experiments/objetivo3/EXPERIMENTOS.md`; RP1 =
`experiments/objetivo3/resultados_prueba_v1.md`; RDEC = `experiments/objetivo3/resultados_dec_2026-10-15.md`;
P1C = `experiments/objetivo1/p1_compuerta.md`; BIT = `redaccion/BITACORA.md`.

El texto es el de r07 con su respuesta aplicada; lo nuevo es DEC15-3 (lecturas posteriores del Obj 3, v2 corrida,
#180 CERRADA) y la regla de `\REVVISUAL` (`overleaf/CLAUDE.md` l. 44-46). Ningun `\REVVISUAL` existe todavia en
`overleaf/secciones/` (solo la definicion en `overleaf/main.tex`).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | OC-2, G-T4 | l. 52, oracion 6, `\GAPDATO` final | "\GAPDATO{evaluación en prueba de la versión~2 del sintetizador}" | RDEC l. 83-100 (Khipu 56857-56865, rc=0: run05a -258.9 [-456.7, -61.1], run05b -264.3 [-456.8, -71.7], "no concluyente, dif. < Peters" en todas las variantes); IMP #190 DECIDIDA; DEC15-3 pto 5; 00T l. 177-179 ("Corrido el 2026-10-15"); EXP3 l. 96 ("evaluacion exploratoria en prueba CORRIDA") | Patron PAT-122 reincide (y PAT-19). La marca niega una evaluacion ya corrida y decidida como reporte lado a lado. Es la "marca de v2 desfasada" que nombra el encargo (E2). BIT §2 2026-10-14 mandaba el `\GAPDATO` solo "hasta que existan" | Retirar la marca: "... que se reporta junto al modelo evaluado y no en su lugar (Sección~\ref{sec:v2}); su evaluación exploratoria en prueba también quedó no concluyente, con diferencia a la baja (capítulo de resultados)." Sin cifras de v2 (C3 l. 479: ninguna se presenta como resultado principal) |
| T02 | media | OC-2, G-T4 | l. 98, oracion 7, `\GAPDATO` final | "la medida se añadió después de la prueba ... \GAPDATO{salto ... sin metal, para el sintetizador y el protocolo físico}" | RP1 l. 46 ("costura mediana difusor 4.3 HU, Peters 1.2 HU (pto 5)"); DEC15 pto 5; `redaccion/MAPA.md` l. 137 ("CERRADO en `capitulo3` en r23 ... Sigue abierto solo en `introduccion` ..., que debe alinearse"); BIT §2 2026-10-15 (medicion ejecutada sobre prueba que no depende de lectura abierta: sin marca, remision) | Patron PAT-122 reincide; afin a PAT-180 (seccion no recotejada cuando otra incorpora el resultado). El GAP declara ausente una medicion hecha en los dos brazos | "... la medida se añadió después de la prueba de la versión~1 y se tomó en los dos brazos (capítulo de resultados)." Retirar la marca y cerrar la fila de MAPA l. 137 |
| T03 | media | G-T4, OC-3 | l. 52, oracion 2 | "El resultado es, así, no concluyente respecto de la equivalencia, con una diferencia significativa" | DEC15-3 pto 1 ("El Objetivo 3 se cumple como objetivo de diseno y evaluacion ... La hipotesis de equivalencia ... no se sostiene ... no se lee como equivalencia ni como no equivalencia demostrada. Se declara que esta lectura se fija despues"); 00T l. 202-204 | Patron PAT-136 reincide. El encargo (E2) pide el resultado del Obj 3 "con la lectura del pto 1", y la oracion solo da la categoria: falta que la hipotesis de equivalencia no se sostiene, que no equivale a no equivalencia demostrada y que el objetivo de diseno y evaluacion se cumplio. Lo posterior de la lectura si esta (l. 50) | "... con una diferencia significativa a la baja (...). Los datos no permiten afirmar la equivalencia, de modo que la hipótesis de equivalencia con el protocolo físico no se sostiene, sin que el resultado se lea como no equivalencia demostrada. El Objetivo~3 se cumple como objetivo de diseño y evaluación: el sintetizador se implementó y se evaluó con el diseño congelado." La ultima oracion fuera de `\REVVISUAL`; lo que diga de calidad de apariencia, dentro (DEC15-3, encabezado: #193 queda fuera) |
| T04 | media | G-T4, OC-3 | l. 50, oracion 6 | "no equivalencia, que haría fallar el objetivo, si el intervalo cae entero fuera" | Re-apertura con argumento nuevo: BIT §2 2026-10-15 (fila de desenlaces) fijo esta forma citando la propia introduccion (r07, guia-1), pendiente de visto bueno; DEC15 pto 15 no dice que la no equivalencia haga fallar el objetivo; DEC15-3 pto 1, posterior, separa el objetivo (cumplido como diseno y evaluacion) de la hipotesis de equivalencia | Patron PAT-176 reincide: una decision nueva cambia la base de una forma fijada en la ronda anterior. Con pto 1, lo que un desenlace de no equivalencia refutaria es la hipotesis, no el objetivo de diseno; la clausula queda sin fuente de la autora y en tension con T03 | "no equivalencia, que refutaría la hipótesis de equivalencia, si el intervalo cae entero fuera del margen". Avisar al orquestador para corregir la fila de BIT §2 (y MAPA l. 145, que la cita como "fijado") |
| T05 | media | OC-2 (`overleaf/CLAUDE.md` regla 2, `\REVVISUAL`), OC-3 | l. 15 or. 3; l. 41 or. 5-7; l. 52 or. 5; l. 84 or. 2-3; l. 94 completo; l. 96 or. 1-2 | "La coherencia de la apariencia se cuantifica..."; "Queda pendiente el contraste de realismo..." | `overleaf/CLAUDE.md` l. 44-46; ENCARGO E1 (contraste de realismo, juicios de apariencia, reclamo de coherencia de apariencia del Obj 3, limitaciones de realismo); IMP #193 ABIERTA; DEC15-3 encabezado ("Queda fuera ... el realismo visual (#193) y lo que de el dependa en el reclamo del Objetivo 3") | Ningun pasaje de la seccion lleva `\REVVISUAL`, y los listados tratan del realismo del artefacto o dependen de el: reclamo de coherencia de apariencia (l. 15), banda que "permite" rayas y comparacion con observaciones reales (l. 41), contraste de realismo con su `\GAPDATO` (l. 52), supuesto de generar el artefacto en dominio de imagen y la comparacion que "puede contradecirlo" (l. 84), limitaciones frente a lo real (l. 94) y estructura de raya no medida con su `\GAPDATO` (l. 96). La pregunta (l. 21, "artefactos coherentes") esta en el encabezado DESFASADO (#126): envolverla sin reescribirla | Envolver cada pasaje en `\REVVISUAL{...}` sin cambiar su texto; los `\GAPDATO` de l. 52 y l. 96 quedan dentro. Opcional, a criterio de la autora: l. 98 or. 1 (los desplazamientos limitan la transferencia de la apariencia aprendida) |
| T06 | media | G-T4, G-C7 | l. 50, oracion 5 | "Las tres elecciones ... acercan además la prueba a concluir equivalencia" | DEC15-3 pto 3 ("el piso del brazo aprendido favorece al difusor en el contraste primario ... -301.0 -> -455.0 HU, IC90 [-647.6, -262.5]"); RDEC l. 71-81, 228-230; IMP #188 DECIDIDA; 00T l. 205 | Afin a PAT-140 (recuento de sesgos incompleto). La oracion enumera lo que acerca la prueba a la equivalencia y omite el piso de ruido, que una decision de la autora fija con el mismo sentido. El lector cree que el sesgo conocido son solo las tres elecciones | Anadir: "La amplitud de solo ruido del sintetizador, mayor que la del protocolo físico, también lo favorece en esa comparación (Sección~\ref{sec:amenazas})." Las cifras (893 frente a 184 HU; -455.0 HU) quedan para el cap. 3/4 |
| T07 | baja | G-T4, PAT-27 | l. 96, oracion 5 | "asimetrías de cortes, de ruido y de suelo ... tratadas con análisis posteriores" | RDEC l. 62-63 ("Ninguna variante sube la categoria del difusor; las que corrigen asimetrias ... achican la diferencia 6-63 HU sin cambiar el desenlace"); IMP #186 CERRADA; DEC15-3 pto 7 | El resultado de esos analisis existe y esta decidido; la oracion lo deja como tratamiento sin desenlace | "... tratadas con análisis posteriores, ninguno de los cuales cambia el desenlace (Sección~\ref{sec:amenazas})." |
| T08 | baja | G-T4, OC-3 | l. 41, oracion 6 | "La banda permite que las rayas ... aparezcan fuera del metal" | IMP #176 ABIERTA (inspeccion: "moteado claro/oscuro, no rayas radiales"); IMP #193 ABIERTA; RDEC l. 201-205 (perfil del difusor "plano por la regla") | Proposito de diseno redactado como capacidad cumplida, en un tema con dos implicancias abiertas que lo ponen en duda. Sin cifra en juego | "La banda está pensada para que las rayas ... puedan aparecer fuera del metal", dentro del `\REVVISUAL` de T05 |
| T09 | baja | G-T4 | l. 50, oracion 1 | "la regla de equivalencia se fijó antes de procesar la partición de prueba" | C3 l. 40 ("antes de procesar ningún paciente de prueba con el sintetizador o con el protocolo físico"; la regla de realismo "sí usó información de inclusión de la partición de prueba"); C3 l. 465 (el Obj 1 ya habia procesado la particion) | Patron PAT-13 reincide (leve): sin el calificador de C3, la oracion dice mas que el registro | "... se fijó antes de procesar ningún paciente de prueba con el sintetizador o con el protocolo físico" |
| T10 | baja | E-R2, E-P3, G-T4 | l. 7, oracion 4; l. 9, oraciones 4-5 | "limita el desarrollo de modelos robustos"; "ControlNet permite incorporar condiciones espaciales" | IMP #126 ABIERTA; `introduccion-r07-respuesta.md` (T09-T13, S01-S14 ESCALADOS) | Patrones PAT-174 y PAT-173 persisten en el encabezado, sin cambio desde r07. Sin argumento nuevo: se registra solo para el recuento de patrones | Ninguna en esta ronda; se resuelve al reescribir el encabezado (#126) |
| T11 | baja | OC-5 | fuentes, no el texto | TM sin el resultado de prueba de v1 ni de v2 | TM l. 98 (aun "a non-conclusive equivalence result is a possible and reportable outcome"; sin "301" ni "196.3"); EXP3 l. 85, 96 (ya al dia) | Patrones PAT-138 y PAT-158 reinciden solo en TM: las cifras del Obj 3 tienen fuente en RP1, RDEC, 00T y DEC, no en TM | Aviso a la autora (regla 4 raiz: TM solo por pedido). Sin efecto sobre el texto |

Conteo: alta = 0, media = 6 (T01-T06), baja = 5 (T07-T11).

`\GAPLIT` (E3): ninguna afirmacion de la seccion necesita fuente nueva. La lectura del TOST no concluyente se apoya en
DEC15-3 pto 1 y en `sec:mt-estadistica`; la introduccion no menciona Pitman y Morgan, Bland y Altman ni una prueba de
Turing visual.

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 3 | Segmentacion relevante para lesiones, reconstruccion 3D, planificacion | sin fuente; TM l. 46 mas acotado | no (ESCALADO r07 T12, #126) |
| l. 3 | El desempeno depende de que el entrenamiento represente las variaciones | TM l. 46 | si |
| l. 3 | Fracturas, protocolos y metal; metal entre lo mas dificil \cite{liu2021ctpelvic1k} | `liu2021ctpelvic1k`, "the challenge of the metal artifacts is the most difficult to handle" (Introduction, p. 2) | si |
| l. 5 | Implantes; bandas oscuras, regiones brillantes, rayas; ocultan limites \cite{selles2024marreview} | `selles2024marreview`, "disguise anatomical structures" (Sec. 1, p. 1) | si |
| l. 5 | Reducen la calidad para modelos de segmentacion \cite{xie2024implantsegmentation} | `xie2024implantsegmentation` (segmentacion del metal) | no (ESCALADO r07 T09) |
| l. 5 | Mecanismos: endurecimiento, "escasez de fotones", reconstruccion; exige proyeccion | `selles2024marreview` (lista distinta), sin `\cite`; TM l. 56 | no (ESCALADO r07 T10) |
| l. 7 | 1 184 volumenes; 75 con metal; 1 109 y 14 anotados; 61 sin anotar ni usar | `liu2021ctpelvic1k` (p. 2-3; Tabla 1 "taken off in our supervised training phase") | si |
| l. 7 | Representacion reducida limita modelos robustos | inferencia sin marca | no (T10) |
| l. 9 | Difusion sintetiza imagenes medicas \cite{kazerouni2023diffusionsurvey}; latente reduce costo \cite{rombach2022latentdiffusion} | fichas respectivas (Sec. 3; Abstract) | si (contexto retirado: T10) |
| l. 9 | ControlNet: mapas de segmentacion o mascaras \cite{zhang2023controlnet} | `zhang2023controlnet` (§1, p. 2); "mascaras" sin fila | parcial (ESCALADO r07 T11, T13) |
| l. 11 | Sintesis de tumores evaluada en tarea posterior \cite{chen2024tumorsynthesis}; plausibilidad antes que utilidad | `chen2024tumorsynthesis`; DEC 2026-10-08 pto 26 | si |
| l. 13 | Cadena de dos componentes; muestreador en el corredor; sintetizador en dominio de imagen; $G$ y copia | TM l. 78-79; C3 l. 15, 196; DEC 2026-09-19 pto 2 | si |
| l. 15 | Coherencia fisica y quirurgica, no utilidad; grados frente a distribuciones clinicas; metricas del protocolo; compuerta | 00T §Fuera de alcance 1; TM l. 62, 77, 78, 80 | si (sin `\REVVISUAL`: T05) |
| l. 17 | Orden del documento | `overleaf/CLAUDE.md` §Estructura | si |
| l. 21 | Pregunta de investigacion | TM l. 62; DEC 2026-10-08 pto 24 | si (ESCALADO #126; `\REVVISUAL`: T05) |
| l. 28 | Cuatro objetivos; 2 y 3 componentes; 1 previo; 4 sin variable dependiente | C3 l. 13; BIT §2 (introduccion-r01) | si |
| l. 32 | Objetivo general; osteosintesis; corredor; multiventana; unico implante transiliaco-transsacro | TM l. 74, 77, 78, 117; IMP #130 | si |
| l. 37 | MAE < 25 HU; seis combinaciones; 34 pacientes; aprueba si alguna cumple; autoencoder \cite{rombach2022latentdiffusion} | TM l. 77; C3 l. 87; P1C l. 18-25; IMP #156 | si |
| l. 39 | Tornillo transiliaco-transsacro, cilindro rigido; marco de Kaiser et al.; calibre + holgura | TM l. 117; C3 l. 107, 123; `kaiser2014dysmorphism` | si |
| l. 39 | Grado de brecha ordinal de cuatro niveles; referencia clinica navegada/convencional en S1; W1 | TM l. 52, 78; `zwingmann2009navigated`; C3 `eq:w1` | si |
| l. 41 | *Inpainting* 2.5D en dominio de imagen; $G = M \cup B_\delta$; ~12 mm | TM l. 79; C3 l. 196, 210 | si |
| l. 41 | La banda "permite" rayas y zonas oscuras fuera del metal | diseno (TM l. 79); IMP #176, #193 ABIERTAS | parcial (T08) |
| l. 41 | Comparacion con copia y pegado, protocolo fisico, observaciones reales; reconstruccion de implantes reales | C3 tabla `tab:diseno` (l. 452); DEC 2026-10-08 pto 11 | si (sin `\REVVISUAL`: T05) |
| l. 43 | SAP unica metrica propia; 7.0 mm y 1 mm; solo grados comparados; metricas de Peters invertidas | DEC 2026-10-08 ptos 10, 14, 16, 23 | si |
| l. 46 | Compuerta para latente + ControlNet; No-Go; reformulacion; autoencoder de TC; 0.00 / 21.80 HU, n = 34; arcoseno en float32 | TM l. 77, 79; C3 l. 87, 91; P1C l. 33-38; DEC 2026-10-08 pto 1 | si |
| l. 48 | Regla del Obj 1 tras exploracion, antes de la prueba; 25 HU anterior; Obj 2 sin regla; Obj 4 de definicion | DEC 2026-09-15 (2); C3 l. 74; DEC 2026-10-08 ptos 17, 23 | si |
| l. 50 | Regla fijada antes de procesar la particion de prueba | C3 l. 40 (con calificador) | parcial (T09) |
| l. 50 | Lectura de desenlaces posterior al resultado | DEC15 pto 15; DEC15-3 pto 1; RP1 l. 30-32 | si |
| l. 50 | Titanio; *streak amplitude*; 13 pacientes sin metal; eje del corredor sin perturbar | RP1 l. 14; DEC15 pto 9; 00T l. 188 (13 tras excluir `CLINIC_0034`) | si |
| l. 50 | IC 90 % de la diferencia media pareada dentro de $[-\Delta, +\Delta]$; $\Delta$ = 196.3 HU en validacion | C3 tabla l. 452; 00T l. 159; DEC15 pto 21 | si |
| l. 50 | Margen fijado por la variabilidad entre semillas del sintetizador | 00T l. 159 (`s` del difusor = 196.3, `r` = 6.1) | si |
| l. 50 | Tres elecciones en validacion acercan a la equivalencia | DEC15 pto 16; C3 l. 487 | parcial (omite el piso: T06) |
| l. 50 | Tres desenlaces; "no equivalencia, que haria fallar el objetivo" | DEC15 pto 15 (desenlaces); BIT §2 2026-10-15 (forma); DEC15-3 pto 1 | parcial (T04) |
| l. 52 | -301.0 HU; IC90 -477.0 a -124.9; cruza el limite inferior; entero bajo cero | RP1 l. 14, 36; RDEC l. 39; 00T l. 162-165 | si |
| l. 52 | No concluyente con diferencia significativa a la baja | DEC15 pto 15 ("Para v1: `run04_mejor` = no concluyente con diferencia significativa a la baja") | si (falta pto 1: T03) |
| l. 52 | Modelo evaluado = punto de control de la v1 elegido en validacion | DEC 2026-10-11 (3) pto 1; 00T l. 154-158 | si |
| l. 52 | Supera a copia y pegado; control de cordura que no cuenta a favor | RP1 l. 23-25 (p = 0.000122 = 2^-13); DEC15 pto 12 | si |
| l. 52 | \GAPDATO: contraste de realismo sin script | EXP3 l. 110 ("realismo (H5) ... POR ESCRIBIR"); RP1 l. 63 | si (GAP justificado; `\REVVISUAL`: T05) |
| l. 52 | v2 entrenada despues del resultado; posterior, exploratoria, junto y no en lugar | 00T l. 171-179; DEC 2026-10-14 (2); DEC15-3 pto 5 | si |
| l. 52 | \GAPDATO: evaluacion en prueba de la v2 | RDEC l. 83-100; IMP #190; EXP3 l. 96 | no (T01) |
| l. 56 | 14 de 75 anotados; 61 sin anotar; motivacion de aumento de datos no medida; razon de coherencia antes | `liu2021ctpelvic1k` (p. 3); 00T §Fuera de alcance 1; DEC 2026-10-08 pto 26 | si |
| l. 58 | Ninguno de los tres enfoques produce poses y apariencia | TM l. 54 | si |
| l. 58 | Peters et al.: metal al azar; manual impracticable; "meaningful locations" sin regla | `peters2025hybrid` (Discussion, p. 9) | si |
| l. 58 | Liu et al. optimizan una unica trayectoria; Zwingmann et al. distribuciones por tecnica; lectura propia | `liu2025pipeline` (Sec. III-D.3, p. 11); `zwingmann2009navigated`; BIT §2 | si |
| l. 60 | Protocolo ejecutado en 13 pacientes sin metal, eje sin perturbar; razon (aislar, costo) | RP1 l. 14; DEC15 pto 9 | si |
| l. 60 | \GAPDATO: exploratorio con poses del muestreador | EXP3 l. 109-110 ("falta D9"; "POR ESCRIBIR"); MAPA l. 140 | si (GAP justificado) |
| l. 60 | Peters necesita proyecciones por pose, 2D de una fila, metal fractal \cite{peters2025hybrid} | DEC 2026-10-08 pto 25; 00T l. 216-218 | si |
| l. 60 | Equivalencia es pregunta del Obj 3, no premisa; en prueba quedo sin concluir | DEC 2026-10-08 pto 25; DEC15 pto 15 | si |
| l. 62 | De Man et al.: endurecimiento, dispersion, ruido, EEGE; rayas irradian \cite{deman1999} | `deman1999` (Conclusiones, p. 695; Sec. III-D, p. 694) | si |
| l. 62 | CLAIM, DiffTumor, LGESynthNet acotados a mascara; DiffBoost desde ruido | fichas `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`, `zhang2025diffboost`; TM l. 48 | si |
| l. 64 | Xie et al.: umbral cubrio en exceso en cortes simulados; objetos alargados fragmentados en la cohorte | `xie2024implantsegmentation` (Abstract); C3 l. 228 | si |
| l. 64 | Entrenamiento con mascaras umbralizadas = desplazamiento; ningun brazo coloca geometria por umbral | C3 l. 226; `sec:ap-brazos` | si |
| l. 66 | Sin precedente de banda con valor; ventanas de HU de MAR \cite{wang2025adaptiveweighting,li2024}; aporte = combinacion | TM l. 54, 79; fichas; DEC 2026-10-08 pto 30 | si |
| l. 68 | Distribucion de poses fijada antes de cualquier distancia; sin parametros de la referencia | TM l. 107; C3 l. 151, 461 | si |
| l. 68 | Ninguna de seis bajo de 25 HU; saturacion del AE de TC ya superaba | P1C l. 20-25; TM l. 77; IMP #156 | si |
| l. 72 | 178 de 1 184 volumenes \cite{liu2021ctpelvic1k} | `docs/02-datos.md` l. 136; `liu2021ctpelvic1k` | si |
| l. 72 | Unico implante con distribucion clinica de grados; otros con corredores por atlas \cite{goerres2017planning,han2019atlasplanning} | DEC 2026-10-08 pto 27; fichas `goerres2017planning`, `han2019atlasplanning`; IMP #180 CERRADA (DEC15-3 pto 8) | si |
| l. 72 | Distribucion y marco de Kaiser de tornillos iliosacros; referencia externa | IMP #130 pto 3 | si |
| l. 74 | Comparacion solo en S1; segundo corredor sin distribucion; eje medido | C3 l. 188; 00T l. 62-64 | si |
| l. 74 | \GAPDATO: preinscripcion y corrida en el segundo corredor | MAPA l. 66; `experiments/objetivo2/EXPERIMENTOS.md` §6 | si (GAP justificado) |
| l. 74 | Sintesis por parches; solo genera $G$ | C3 l. 196, 202 | si |
| l. 78 | Dice/HD95 fuera; 14 casos; disponibilidad local no verificada | 00T §Fuera de alcance 1 | si |
| l. 79 | Ablaciones a trabajo futuro | DEC 2026-10-08 pto 28 | si |
| l. 80 | XCIST preliminar sin estudio de metal \cite{wu2022xcist}; Peters valida contra fantoma | `wu2022xcist` (Validation, p. 9); `peters2025hybrid` (Abstract) | si |
| l. 81 | Gardner et al.: rasgos; 222 frente a 346 mm² (medias); estudio previo sin diferencia | `gardner2010safezones` (p. 624, 628) | si |
| l. 84 | Supuesto 1; De Man no lineal y en sinograma; comparacion ya ejecutada y no concluyente | TM l. 56; `deman1999` (Sec. III-E); DEC15 pto 15 | si (`\REVVISUAL`: T05) |
| l. 84 | Supuestos 2 (serie navegada = S1) y 3 (mascara-artefacto) | C3 l. 495, 501 | si |
| l. 86 | 12 mm sin calibrar en fuentes; limites de 2 mm via Smith et al.; equiespaciados; $\sigma$ = 2.5 mm; ~95 % | `gertzbein1990`, `mirza2003`, `smith2006iliosacral`; DEC 2026-10-08 pto 19; `kaiser2014dysmorphism` | si |
| l. 88 | Referencia de pelvis fracturadas; grado 0 inalcanzable; cribado 30 casos, 20 de 30, 10 por grupo | TM l. 109, 121; C3 l. 463, 509; IMP #132, #136 | si |
| l. 90 | 16 casos revisados: 14 conformes, 2 fallan con ambas; variante se mantiene | C3 `sec:corredor`; MAPA l. 56 | si |
| l. 90 | \GAPDATO: sensibilidad sin los dos casos | `experiments/objetivo2/` (sin resultado; solo `e9ts_revision_laminas.md`) | si (GAP justificado) |
| l. 92 | TotalSegmentator sin exactitud para S1 \cite{wasserthal2023}; 11 de 34 y 7 de 57 | `wasserthal2023` (NO ENCONTRADO el Dice de S1); C3 l. 461 | si |
| l. 92 | \GAPDATO: envolvente y canal sacro/foramenes | MAPA l. 106; C3 l. 491 | si (GAP justificado) |
| l. 94 | Reconstruccion no reportada; MAR del fabricante \cite{selles2024marreview} | `selles2024marreview` (Sec. 3.5, p. 6) | si |
| l. 94 | Protocolo validado en 2D y para MAR; exagera con los dos materiales; p95 sintetico bajo lo real | C3 l. 469, 507; IMP #191 (p95 del modelo); RDEC l. 192-205 | si (`\REVVISUAL`: T05) |
| l. 96 | Metrica sin estructura de raya; \GAPDATO de estructura direccional | C3 l. 497; MAPA l. 135; IMP #176 (solo inspeccion visual) | si (GAP justificado; `\REVVISUAL`: T05) |
| l. 96 | Banda de 12 mm contiene el artefacto real de tornillo; mas alla de 10 mm no se separa del nulo | IMP #177 adenda D1/D2 (11 HU a 10-12 mm, IC90 incluye 0); DEC 2026-10-13 ptos 1, 3; C3 l. 499 | si |
| l. 96 | Placas y protesis no acotadas | IMP #177 adenda D1 (20-25 mm con piezas grandes) | si |
| l. 96 | Asimetrias de cortes, ruido y suelo medidas despues y tratadas | IMP #186 CERRADA; DEC15 ptos 1, 17, 18; RDEC l. 62-63 | parcial (T07) |
| l. 98 | Tres desplazamientos; mascara de sintesis con cabeza | C3 l. 226; DEC15 pto 2 | si |
| l. 98 | Medida del primero (auditoria) y del tercero (razon, antes de los retiros) | C3 l. 226, 228 | si |
| l. 98 | Segundo medido en la reconstruccion de implantes reales; en sintesis sin metal anadido despues | RP1 l. 56-57 (exceso de costura E-A1); DEC15 pto 5 | si |
| l. 98 | \GAPDATO: salto en el borde en la sintesis sin metal, dos brazos | RP1 l. 46 (4.3 y 1.2 HU); MAPA l. 137 | no (T02) |
| l. 1-98 | Claves citadas (25) existen en `overleaf/referencias.bib`; apellidos nombrados = primer autor | grep en `overleaf/referencias.bib` (25 de 25) | si |
| l. 1-98 | Ninguna cita como sujeto gramatical sola (E-F3); sin fuentes de fabricante (P-EA1) | revision del texto | si |
| l. 1-98 | Contenido retirado: Dice/HD95 solo como exclusion; latente/ControlNet como historia (l. 37, 46) y contexto (l. 9); sin "31-60 %", BFC ni ISC | 00T §Fuera de alcance; `CLAUDE.md` raiz | parcial (T10) |
| l. 1-98 | Implicancias: #193 ABIERTA no se afirma resuelta, pero nada esta marcado con `\REVVISUAL`; #176 ABIERTA tocada por l. 41; #177 con su lectura decidida (DEC15 pto 15, DEC15-3 pto 1); #186 CERRADA; #188, #190 DECIDIDAS sin reflejo (T01, T06); #180 CERRADA | IMP; DEC15-3 | parcial (T01, T05, T06, T08) |
| l. 1-98 | GAP: 0 `\GAPLIT`, 8 `\GAPDATO`, 0 `\GAPDEC` | `introduccion-r08-lint.md` (dato=8, dec=0) | si (conteo); 2 desfasados (T01, T02) |
| l. 1-98 | Patrones VIGENTES del dominio | PAT-122 (T01, T02), PAT-19 (T01), PAT-136 (T03), PAT-176 (T04), PAT-140 afin (T06), PAT-27 (T07), PAT-13 (T09), PAT-173 y PAT-174 (T10), PAT-138 y PAT-158 (T11), PAT-180 afin (T02); sin reincidencia: PAT-11, PAT-20, PAT-31, PAT-116, PAT-148, PAT-155, PAT-168, PAT-171, PAT-172, PAT-175 | — |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP de resultado propio que sigue negando una evaluacion corrida y decidida | OC-2, G-T4 | "\GAPDATO{evaluación en prueba de la versión~2 del sintetizador}" | PAT-122 |
| Una marca cerrada en el capitulo de metodo sigue abierta en la introduccion que la copio | OC-2, G-T4 | "\GAPDATO{salto de los valores de TC en el borde de $G$ ...}" | PAT-180 |
| Resultado de un objetivo dado solo con su categoria cuando una decision fija ya su lectura para el objetivo | G-T4, OC-3 | "El resultado es, así, no concluyente respecto de la equivalencia" | PAT-136 |
| Recuento de lo que favorece la equivalencia que omite un sesgo con el mismo sentido fijado despues | G-T4, G-C7 | "Las tres elecciones ... acercan además la prueba a concluir equivalencia" | PAT-140 |
| Pasaje sobre una implicancia abierta que la autora pidio senalar queda sin la marca visual acordada | OC-2 | "Queda pendiente el contraste de realismo frente a los tornillos reales" | nuevo |
| Proposito de diseno redactado como capacidad cumplida cuando una implicancia abierta lo pone en duda | G-T4, OC-3 | "La banda permite que las rayas ... aparezcan fuera del metal" | nuevo |
