# Auditoria de trazabilidad — introduccion — r02

Alcance acotado por pedido de la autora: l. 23-76 (Objetivos de investigacion, Justificacion, Alcance
y limitaciones). Encabezado y Formulacion del problema (l. 1-21) no se auditan (DESFASADO, #126).
Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`; IMP = `docs/04-implicancias.md`; GLO =
`docs/03-glosario.md`.

Respuesta r01 considerada: T01-T09 aplicados y verificados en el texto actual (ver inventario). T10
(insumo de implantes, discrepancia `CLAUDE.md` raiz frente a DEC) fue ESCALADO sin argumento nuevo:
no se re-reporta. La discrepancia TM:77 ("fixed before any run") frente a DEC 2026-09-17 (3) y C3
l. 58/255 ya esta registrada en IMP #127.4-5; el texto sigue el registro, no TM, y no se re-reporta.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | E-R6, G-T4 | l. 56 | "Esa codificación proviene de trabajos de ... MAR \cite{wang2025adaptiveweighting,li2024}" | TM l. 54 (C3 de Recognized Gap); 00T §Fuera de alcance 4; GLO l. 29-32 (aviso #24); fichas `wang2025adaptiveweighting` (l. 49, 145, 175) y `li2024` (l. 87, 107) | Patron PAT-6 reincide. Lo que viene de MAR es el **marco** multiventana, no la **codificacion** de entrada. TM l. 54: "published uses apply the windows to per-window reconstruction stages or to the training loss rather than to the encoding of the input". Wang et al. combinan las ventanas en cascada (ficha l. 49) y toman el marco de la ref. [24]; Li et al. las usan en la perdida perceptual. El GLO advierte que citarlos sin esa salvedad "atribuye un diseño que la fuente no tiene". | "El marco multiventana proviene de trabajos de MAR, que aplican las ventanas a etapas de reconstrucción o a la función de pérdida y no a la codificación de la entrada \cite{wang2025adaptiveweighting,li2024}; no se reclama como propio. Lo que se reclama es su uso como codificación para generar." |
| T02 | media | E-R6 | l. 56 | "umbral fijo de HU, cuyo error cambia de dirección según el valor elegido" | ficha `xie2024implantsegmentation` l. 29-31, 159-161, 171-178; filas 121-122 de Evidencia textual; TM l. 54 | La cita afirma como hecho lo que la fuente plantea como posibilidad. El unico error medido del umbral es sobrecobertura en cortes 2D **simulados** (Tabla 2, p. 11; ficha l. 29). La inversion de sentido aparece solo en la Discusion con modal: "A smaller threshold may lead ..." / "larger thresholds may misidentify ..." (p. 8/10); la ficha lo rotula "solo como posibilidad teorica" (l. 159). | "... cuyo error, según Xie et al., puede ir en uno u otro sentido según el valor elegido \cite{xie2024implantsegmentation}" o, con lo medido: "que en cortes simulados cubrió el implante en exceso \cite{xie2024implantsegmentation}". |
| T03 | baja | E-R6 | l. 52 | "el metal se inserta en ubicaciones clínicamente significativas (\emph{meaningful locations})" | ficha `peters2025hybrid` Evidencia l. 217 y nota l. 281-285 | "Clinically" califica a los conjuntos de pacientes, no a las ubicaciones: "clinically representative patient datasets with virtual metals ... inserted in meaningful locations" (Discussion, p. 9). "Clínicamente significativas" agrega un calificativo que la frase del paper no da a las ubicaciones. | "... en conjuntos de pacientes clínicamente representativos, el metal se inserta en ubicaciones significativas (\emph{meaningful locations}), sin que el artículo describa ..." |
| T04 | baja | G-T4 | l. 62 | "el segundo corredor bajo S1 se reporta de forma descriptiva" | C3 l. 164 (\GAPDATO); MAPA l. 38; `preinscripcion_muestreador.md` §7 | El texto presenta el reporte como hecho del alcance. C3 registra que el muestreo en ese corredor no esta preinscrito ni corrido (solo su eje esta medido en 69 de 72 pacientes). La razon dada (sin distribucion ordinal clinica) si coincide con C3 y 00T l. 36-38. | "... y el segundo corredor bajo S1 se tratará de forma descriptiva (Sección~\ref{sec:poses}), porque ..."; o remitir al \GAPDATO de C3. |
| T05 | baja | G-T4 | l. 50 | "los artefactos metálicos pueden ocultar los límites anatómicos cerca de los implantes" | TM l. 46 (sin cita); introduccion l. 5 (encabezado, fuera de alcance, cita `selles2024marreview,xie2024implantsegmentation`) | Patron PAT-12 reincide, en forma leve: afirmacion de dominio sin `\cite`, cuando el propio capitulo la sostiene en otro parrafo con dos claves del repositorio. TM tampoco la cita, de modo que no es cifra sin fuente. La ficha `selles2024marreview` describe mecanismos y rayas, pero no trae frase literal sobre "ocultar limites": ficha insuficiente para decidir si la sostiene. | Citar solo si la ficha lo respalda tras relectura con `lector-papers`; si no, dejar la oracion como enunciado de TM l. 46, sin cita. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 28 | Los cuatro objetivos son los del cap. 3 | C3 §Vision general y fig. 1; MAPA l. 47 | si |
| l. 28 | \GAPDEC: la pregunta aun promete 2D, Dice, HD95 y aumento convencional; orden Justificacion/Formulacion | IMP #126 (ABIERTA); introduccion l. 21; MAPA l. 63 | si (GAP justificado) |
| l. 28 | Obj 1 = compuerta previa a la cadena, formulada para difusion latente con ControlNet | C3 fig. 1 y l. 174; TM l. 79; BITACORA §2 (introduccion-r01) | si (historico, no vigente) |
| l. 28 | Veredicto negativo; Obj 3 reformulado despues; regla no modificada | 00T l. 24, 69-70; DEC 2026-09-19; C3 l. 38 | si |
| l. 28 | Error de ida y vuelta de la codificacion sin autoencoder no verificado por ningun objetivo | C3 l. 172 (\GAPDEC); MAPA l. 40 | si |
| l. 28 | Obj 2 y 3 = componentes; Obj 4 = metricas | C3 l. 185; 00T §Alcance | si |
| l. 32 | Cadena de difusion en dominio de imagen; implantes y artefacto local; coherencia fisica y quirurgica | TM l. 74; 00T titulo (2026-09-21); DEC 2026-09-19 | si |
| l. 32 | Osteosintesis = dispositivos de fijacion osea, como tornillos y placas | `CLAUDE.md` raiz ("implantes de osteosintesis (tornillos, placas)") | si |
| l. 32 | Colocacion restringida con el corredor oseo medido sobre cada volumen; glosa del corredor | TM l. 52 ("corridor measured on each volume"); GLO l. 52-53 | si |
| l. 32 | Codificacion multiventana, varios canales con ventanas distintas | TM l. 79; C3 l. 60; 00T l. 68 | si |
| l. 32 | Utilidad para segmentacion = trabajo futuro | 00T §Fuera de alcance 1; TM l. 83 | si |
| l. 37 | Ida y vuelta por el autoencoder de un modelo de difusion latente | TM l. 77; C3 l. 58 | si |
| l. 37 | MAE < 25 HU en hueso | TM l. 77; 00T l. 23; DEC 2026-09-15 (2) | si |
| l. 37 | Autoencoder comprime a un latente donde opera la difusion | `rombach2022latentdiffusion`, "we apply them in the latent space of powerful pretrained autoencoders" (Abstract, p. 1) | si |
| l. 37 | 34 pacientes de prueba | TM l. 77 ("34 held-out patients"); DEC 2026-09-17 (3) l. 1051 | si |
| l. 37 | Veredicto reportado sea positivo o negativo | 00T l. 24; DEC 2026-09-19 pto 1 | si |
| l. 39 | Poses 3D de tornillo iliosacro parametrico y rigido | TM l. 78; DEC 2026-09-11 (#41) | si |
| l. 39 | Marco de referencia de Kaiser et al. | DEC 2026-09-08 (marco de Kaiser); 00T l. 28-31 | si |
| l. 39 | Viabilidad = calibre mas holgura radial tomada de Kaiser | C3 l. 89; GLO l. 58-63; DEC 2026-09-11 (2); BITACORA §2 (introduccion-r01) | si |
| l. 39 | Grado de brecha cortical, escala ordinal de cuatro niveles | TM l. 52, l. 96; GLO l. 45-48 | si |
| l. 39 | Referencia clinica = series navegada y convencional de Zwingmann et al., en S1 | TM l. 52; 00T l. 35-36; BITACORA §2 | si |
| l. 39 | S1 = primer segmento del sacro | `kaiser2014dysmorphism`, "first sacral segment" (Fig. 1, p. e120(3)) | si |
| l. 39 | Sin ajustar el muestreador a la referencia | DEC D-O2.1; TM l. 78 ("No parameter ... derived") | si |
| l. 39 | Wasserstein-1 = suma de diferencias absolutas de acumuladas | C3 ec. `eq:w1` (l. 200-205) | si |
| l. 41 | *Inpainting* 2.5D en dominio de imagen, sin latente ni proyeccion | TM l. 79; 00T l. 62-68; C3 l. 172 | si |
| l. 41 | 2.5D se remite al marco teorico | BITACORA §2 (introduccion-r01, glosas) | si |
| l. 41 | $G = M \cup B_\delta$; $B_\delta$ de unos 12 mm | TM l. 79; 00T l. 68; GLO l. 36-41 | si |
| l. 41 | La banda permite rayas y endurecimiento del haz fuera del metal | TM l. 79; GLO l. 38 | si |
| l. 41 | Comparacion con copia y pegado (sin artefacto) y protocolo fisico de Peters et al. | TM l. 62, l. 98; C3 l. 219 | si |
| l. 43 | SAP como unica metrica introducida, incluida Wasserstein-1; comparacion en Obj 2 | 00T §Fuera de alcance 2; TM l. 80; DEC 2026-09-08; BITACORA §2 | si |
| l. 43 | *bone integrity*, *metal integrity*, *streak amplitude*, nombres publicados | TM l. 80; ficha `peters2025hybrid` l. 358; overleaf/CLAUDE.md terminos fijos | si |
| l. 46 | Obj 1 a 3 con variable dependiente; Obj 4 sin fila propia | C3 l. 185, tab:diseno | si |
| l. 46 | 25 HU anterior a la exploracion; regla operativa despues de ella y antes de la prueba que decide | DEC 2026-09-15 (2) ("se mantiene en 25 HU", l. 817, tras E6b 178/178, l. 841); DEC 2026-09-17 (3); C3 l. 58, 255; IMP #127.4 | si |
| l. 46 | \GAPDEC: distancia W1 que contaria como fallo | IMP #127.6; C3 l. 207 | si (GAP justificado) |
| l. 46 | Superioridad frente a copia y pegado sobre rayas, que esa linea base no produce | IMP #127.3; C3 l. 217 | si |
| l. 46 | \GAPDEC: que haria fallar el Obj 3 | IMP #127.3 (ABIERTA) | si (GAP justificado) |
| l. 46 | Obj 4 comprobado con controles de consistencia | C3 l. 198 (seis controles); BITACORA §2 | si |
| l. 46 | \GAPDEC: evidencia del Obj 4 / adopcion de metricas de Peters | IMP #127.6; MAPA l. 49 | si (GAP justificado) |
| l. 50 | Segmentacion depende de datos anotados | TM l. 46 | si |
| l. 50 | Artefactos ocultan limites anatomicos cerca de los implantes | TM l. 46 (sin cita) | parcial (T05) |
| l. 50 | CTPelvic1K anota 14 de 75 volumenes con metal; 61 sin anotar | `liu2021ctpelvic1k`, "and 14 metal-affected CTs", "including 75 CTs with metal artifacts", "The remaining 61 metal-affected CTs are left unannotated" (p. 2-3) | si |
| l. 50 | Motivacion de fondo: aumento de datos para segmentacion peri-implante | `CLAUDE.md` raiz; TM l. 74 | si |
| l. 50 | Las condiciones de los datos impiden medir la utilidad | TM l. 83; 00T §Fuera de alcance 1 | si |
| l. 50 | \GAPDEC: por que la coherencia antes de la utilidad | TM y 00T no dan el eslabon (busqueda en 00T completo y TM l. 46-83) | si (GAP justificado) |
| l. 52 | Ninguno de los tres enfoques resuelve colocacion y apariencia | TM l. 54 (Recognized Gap) | si |
| l. 52 | Peters et al.: colocacion aleatoria en entrenamiento; manual impracticable | `peters2025hybrid`, "location of the metal objects in the training dataset was randomized", "manual metal placement was impractical" (Discussion, p. 9) | si |
| l. 52 | Peters et al.: evaluacion en "meaningful locations", sin regla | `peters2025hybrid`, fila l. 217 (Discussion, p. 9); nota l. 285 | parcial (T03) |
| l. 52 | Liu et al. optimizan una unica trayectoria | TM l. 52; ficha `liu2025pipeline` ("formulated as an optimization problem", Sec. III-D.3, p. 11) | si |
| l. 52 | Zwingmann et al.: distribuciones distintas por tecnica | TM l. 52 (69 % frente a 40 % de grado 0); C3 l. 200 | si |
| l. 52 | Lectura propia: se reproduce una distribucion de poses | BITACORA §2 (lectura operativa propia); TM l. 52 | si |
| l. 54 | De Man et al.: rayas por endurecimiento, dispersion, ruido y EEGE; irradian desde el metal | `deman1999`, "Beam hardening, scatter, noise and EEGE are the most important causes" (p. 695); "streaks can be seen radiating from the metals" (Sec. III-D, p. 694) | si |
| l. 54 | CLAIM, DiffTumor, LGESynthNet: *inpainting* acotado a la mascara; DiffBoost desde ruido | TM l. 48; fichas `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`, `zhang2025diffboost` (Alg. 1, p. 3676) | si |
| l. 54 | Ninguno con mecanismo ni senal fuera de la mascara | TM l. 48 | si |
| l. 56 | Geometrias rigidas parametricas frente a umbral fijo | TM l. 54 (C1); DEC 2026-09-11 (#41) | si |
| l. 56 | Error del umbral cambia de direccion segun el valor | `xie2024implantsegmentation`, filas 121-122 ("may lead", "may misidentify", Discussion p. 8/10) | parcial (T02) |
| l. 56 | 9 de 57 objetos metalicos alargados a 2500 HU, fragmentados | DEC l. 1210 (E8, #46); IMP #46 recuento por paciente (l. 3559); BITACORA §2 | si |
| l. 56 | Muestreador comparado con la referencia clinica | TM l. 54 (C2) | si |
| l. 56 | Codificacion multiventana proviene de MAR; no se reclama | TM l. 54; 00T §Fuera de alcance 4; GLO l. 29-32 | no (T01) |
| l. 56 | Sin precedente que cuantifique una banda de generacion | TM l. 54; GLO l. 39-41 | si |
| l. 58 | Distribucion de poses fijada por escrito antes de calcular distancias | TM l. 107; DEC 2026-09-22 (D-O2.1-D-O2.7); C3 l. 127 | si |
| l. 58 | Ningun parametro del muestreador sale de la referencia | DEC D-O2.1; TM l. 107; C3 l. 158 | si |
| l. 58 | Latentes preentrenados examinados, incluido uno de TC, excluyen hueso denso y metal | TM l. 77; 00T l. 26-27 (#93) | si |
| l. 62 | 178 de los 1 184 volumenes | `docs/02-datos.md` (103 + 75); C3 l. 42; `liu2021ctpelvic1k`, "including 1, 184 CT volumes" (p. 2) | si |
| l. 62 | Unico implante: tornillo iliosacro parametrico rigido; reales sin geometria | DEC 2026-09-11 (#41), 2026-09-20 D3; TM l. 117 | si (T10 r01 escalado, no se re-reporta) |
| l. 62 | Comparacion solo en S1; segundo corredor descriptivo | 00T l. 36-38; TM l. 78; C3 l. 164 | parcial (T04) |
| l. 62 | Sintesis por parches en dominio de imagen | TM l. 79; 00T l. 64-66 | si |
| l. 66 | Dice y HD95 fuera de alcance | 00T §Fuera de alcance 1; DEC 2026-09-08 | si |
| l. 66 | 14 de 75 anotados; no verificado que esten localmente; solo parte local | `liu2021ctpelvic1k` (ver l. 50); C3 l. 36; 00T §Fuera de alcance 1 | si |
| l. 67 | Ablaciones a trabajo futuro, para tiempo de compuerta y muestreador | 00T §Fuera de alcance 10 ("camino critico (VAE y muestreador)"); DEC 2026-09-17 | si |
| l. 68 | Validacion de XCIST preliminar y sin estudio de artefacto metalico | `wu2022xcist`, "qualitative and semi-quantitative first-order evaluation" (Validation, p. 9); "Metrica cuantitativa de artefacto metalico: NO ENCONTRADO" (ficha l. 156, 165) | si |
| l. 68 | Reimplementacion sin validacion en metal que heredar; se adopta Peters | DEC 2026-09-07 (adopcion de Peters); 00T §Fuera de alcance 3; IMP #8 (APLICADA) | si |
| l. 69 | Efecto del dismorfismo no consistente entre estudios | 00T §Fuera de alcance 8; DEC 2026-09-08 (2) | si |
| l. 69 | Gardner et al.: zona segura de S1 menor en dismorficos; estudio previo sin diferencia | `gardner2010safezones`, "cross-sectional area was 36% smaller in dysmorphic" (Resultados, p. 624); "that study found no difference in the safe zone size" (Discusion, p. 628) | si |
| l. 69 | El muestreador mide el corredor en cada volumen | 00T §Fuera de alcance 8; TM l. 78 | si |
| l. 72 | Supuesto 1: apariencia generable en imagen; mecanismos no lineales en sinograma | TM l. 56; `deman1999`, "Noise artifacts are non-linear artifacts" (Sec. III-E, p. 694) | si |
| l. 72 | La comparacion con el protocolo fisico puede contradecirlo | TM l. 56; C3 l. 261 | si |
| l. 72 | Supuesto 2: serie navegada sin nivel declarado = S1 | TM l. 52; DEC 2026-09-17 C (#69); C3 l. 259 | si |
| l. 72 | Convencion 1: $B_\delta$ ~12 mm sin calibracion, trunca rayas lejanas | TM l. 79; GLO l. 40-41 | si |
| l. 72 | Convencion 2: cortes de 2 mm de tornillos pediculares, via Smith et al.; convencion geometrica | TM l. 52; fichas `mirza2003` ("The thresholds reported in prior studies were used", p. 405), `smith2006iliosacral` (p. 236) | si |
| l. 74 | Referencia de pelvis fracturadas; receptoras sin osteosintesis, no verificadas sin fractura | TM l. 109, l. 121 (Tile B y C); IMP #125 | si |
| l. 74 | Malreduccion estrecharia corredores; fractura no detectada por causa distinta | TM l. 121; C3 l. 253, 263 | si |
| l. 74 | Al menos un paciente con fractura confirmada por medico sin especialidad | IMP #125 (CLINIC_0060); C3 l. 253 | si |
| l. 74 | \GAPDATO: cribado ciego de 30 casos, preparado y no realizado | IMP #125 l. 8729; `docs/ESTADO.md` l. 60 (0/30) | si (GAP justificado) |
| l. 74 | Cifras principales del Obj 2 dependen de una variante condicionada a revision no hecha | IMP #123 (ABIERTA); DEC 2026-09-14 (4); C3 l. 91 | si |
| l. 74 | \GAPDATO: revision de la autora de 16 casos | IMP #123; `docs/ESTADO.md` l. 59 (autora 0/16; la del agente es propuesta, l. 74) | si (GAP justificado) |
| l. 76 | Reconstruccion no reportada; MAR del fabricante o monoenergetica cambian la apariencia | TM l. 115; `selles2024marreview` (ficha l. 9, 42; "varies by vendor", Sec. 3.5, p. 6); C3 l. 44 | si |
| l. 76 | Protocolo fisico validado en 2D y para MAR; adaptacion no hereda la validacion | TM l. 119; C3 l. 221, 263 | si |
| l. 76 | \GAPDATO: el sintetizador no genero ninguna muestra | IMP #116; `docs/ESTADO.md` l. 27, 405 | si (GAP justificado) |
| l. 76 | \GAPDEC: equivalencia frente al protocolo fisico, contingencia de plazo | IMP #90; `docs/ESTADO.md` l. 104, 319 | si (GAP justificado) |
| l. 37-76 | Claves citadas existen en `overleaf/referencias.bib` y el apellido nombrado coincide con el primer autor (Kaiser, Zwingmann, Peters, Liu, De Man, Gardner, Smith) | `overleaf/referencias.bib` l. 434, 1265, 705, 540, 117, 229, 868; ademas l. 88, 262, 400, 498, 518, 626, 738, 773, 847, 1040, 1073, 1093, 1179 | si |
| l. 23-76 | Ninguna cita como sujeto gramatical sola (E-F3) | revision del texto | si |
| l. 23-76 | Sin fuentes de fabricante citadas (P-EA1) | revision del texto | si (no aplica) |
| l. 23-76 | Sin contenido retirado como vigente (downstream como objetivo, difusion latente/ControlNet, "31-60 %", BFC/ISC) | 00T §Fuera de alcance 1, 2, 5; `CLAUDE.md` raiz. ControlNet solo en l. 28, como historia; Dice/HD95 solo en l. 66, como exclusion | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| La cita atribuye a la fuente el diseno propio (codificacion de entrada) en vez del marco que si aporta | E-R6 | "Esa codificación proviene de trabajos de MAR \cite{wang...,li2024}" | PAT-6 |
| Un modal de la fuente ("may") se convierte en afirmacion de hecho al citarla | E-R6 | "cuyo error cambia de dirección según el valor elegido \cite{xie...}" | nuevo |
| Al resumir en la introduccion un tramo que el cap. 3 marca con \GAPDATO, el GAP se pierde y queda como hecho | G-T4 | "el segundo corredor bajo S1 se reporta de forma descriptiva" | PAT-31 |
