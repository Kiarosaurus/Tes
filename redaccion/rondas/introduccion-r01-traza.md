# Auditoria de trazabilidad — introduccion — r01

Alcance acotado por pedido de la autora: l. 23-76 (Objetivos de investigacion, Justificacion, Alcance
y limitaciones). El encabezado y la Formulacion del problema (l. 1-22) no se auditan (DESFASADO, #126).
Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`; IMP = `docs/04-implicancias.md`.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-1 | l. 48 | "El orden de los objetivos también es el orden en que se decidieron." | DEC (encabezados fechados), 00T, TM | Afirmacion propia sin fuente y contradicha por DEC. SAP como unica metrica (Obj 4) se decidio el 2026-09-08 (DEC l. 144), antes de la regla operativa de la compuerta del Obj 1 (2026-09-17 (3), DEC l. 1044). El Obj 2 se preinscribio el 2026-09-22 (D-O2.1-D-O2.7, DEC l. 1407), despues del rediseno del Obj 3 (2026-09-19, DEC l. 1136). El orden 1-2-3-4 no es el orden de las decisiones. | Borrar la oracion y dejar solo lo que DEC respalda: "La compuerta del Objetivo 1 se formuló para ... ; el Objetivo 3 se reformuló después de conocer ese veredicto (DEC 2026-09-19) ...". |
| T02 | media | E-R6, G-T4 | l. 39 | "con el criterio de viabilidad del corredor de McLaren et al." | C3 l. 89; DEC 2026-09-11 (2) (#31); 00T l. 32-34 y §Fuera de alcance 6-7; BITACORA §2 (capitulo3-r01) | Patron PAT-6 reincide. El criterio que usa la tesis es $D \geq d + 2\epsilon$, con holgura de Kaiser et al. leida como operacionalizacion propia. El de McLaren et al. es el corredor de 10 mm, que toman de Kaiser y que C3 conserva solo como convencion de comparacion. Lo que aporta McLaren es el procedimiento reproducible de medicion del diametro (00T §6). | "... y con el procedimiento de medición del diámetro del corredor de McLaren et al.~\cite{mclaren2021corridor}", sin atribuirle el criterio de viabilidad. |
| T03 | media | G-T4, OC-3 | l. 37 y l. 46 | "su criterio de 25~HU y su regla de decisión se escribieron antes de correr la prueba que decide" | IMP #127.4 (ABIERTA); C3 l. 255; DEC 2026-09-17 (3) | Literalmente es compatible con la decision de BITACORA §2 ("fijada antes de correr la prueba que decide"). Pero el parrafo presenta al Obj 1 como el unico que fija su fallo de antemano y calla lo que #127.4 (ABIERTA) y C3 l. 255 registran: la regla operativa y sus seis combinaciones se fijaron despues de una exploracion que incluia a los 34 pacientes de prueba y que ya habia fallado el criterio. Solo el umbral de 25 HU es anterior a la exploracion. | Separar umbral y regla: "El Objetivo~1 sí lo fija: su criterio de 25~HU es anterior a toda corrida, y su regla operativa se escribió antes de la prueba que decide, aunque después de una exploración que incluía a los pacientes de prueba (Sección~\ref{...})". |
| T04 | media | G-T4 | l. 76 | "al menos un paciente de la cohorte del Objetivo~2 tiene una fractura confirmada" | IMP #125 (ACTUALIZACION 2026-09-23); C3 l. 253 | Patron PAT-31 reincide. #125 dice que la confirmacion la hizo un medico recien licenciado y sin especialidad, y que "esa salvedad debe acompañar a cualquier cifra que se derive". C3 la conserva ("confirmada por un médico sin especialidad"); la introduccion la pierde. | "... tiene una fractura confirmada por un médico sin especialidad". |
| T05 | media | G-T4, OC-1 | l. 54 | "Los simuladores físicos reproducen el mecanismo del artefacto, pero no colocan el metal ..." | TM l. 50 y l. 54 (Recognized Gap); fichas `peters2025hybrid`, `deman2007catsim`, `wu2022xcist` | Patron PAT-12 reincide. Es una generalizacion sobre la literatura sin `\cite`, aunque las fuentes estan en el repositorio. La unica evidencia de "no colocan" es la de Peters et al. (ficha: colocacion aleatoria en entrenamiento, Discussion p. 9). No hay ficha que respalde la afirmacion para los simuladores en general. | Acotarla al simulador revisado: "El simulador físico revisado reproduce el mecanismo del artefacto, pero no coloca ...", y dejar que la oracion siguiente sobre Peters et al. la sostenga. Si se quiere mencionar CatSim/XCIST, citar `\cite{deman2007catsim,wu2022xcist}` solo por "reproducen el mecanismo". |
| T06 | media | G-T4, OC-1 | l. 74 | "cuyos cortes de 2~mm provienen de la literatura de tornillos pediculares" | TM l. 52 (`gertzbein1990`, `mirza2003`, `smith2006iliosacral`); claves presentes en `overleaf/referencias.bib` | Patron PAT-12 reincide. La procedencia de la escala es una afirmacion sobre la literatura sin cita, y las fichas existen. | "... provienen de la literatura de tornillos pediculares \cite{gertzbein1990,mirza2003} y llegan a la fijación iliosacra a través de Smith et al.~\cite{smith2006iliosacral}". Mantener la formulacion de TM, que no atribuye los cuatro grados a Gertzbein (#58). |
| T07 | baja | E-R6 | l. 54 | "reservan la colocación experta para su conjunto de evaluación" | ficha `peters2025hybrid` l. 280-285 | "Experta" es la lectura de la ficha, que ella misma rotula como tal. El PDF dice "meaningful locations" y "realistic metal object orientation" y, segun la ficha, no describe ninguna regla anatomica. La cita afirma algo mas que la frase del paper. | "... y reservan para su conjunto de evaluación una colocación en ubicaciones realistas, sin regla anatómica publicada". |
| T08 | baja | G-T4 | l. 58 | "los tornillos pélvicos extraídos así aparecen fragmentados" | DEC l. 623 y l. 1210 (E8, #46); `docs/ESTADO.md:892` | Falta la proporcion. El dato medido es 9 de 57 objetos fragmentados a 2500 HU, con un fuste mediano de unos 5 mm. Sin el n, la frase se lee como si todos aparecieran fragmentados. | "... en la auditoría local, 9 de 57 tornillos extraídos así aparecen fragmentados y la mayoría queda más delgada que los calibres publicados". |
| T09 | baja | G-T4 | l. 68 | "De los 75 volúmenes con metal de CTPelvic1K, la publicación anota 14" | 00T §Fuera de alcance 1 (#13, #18); C3 l. 36 | La razon registrada es "anotacion osea **verificada**" en la cohorte local. C3 agrega que no esta verificado que las 14 mascaras esten disponibles localmente. La introduccion da solo la cifra publicada, que es correcta, y omite la condicion que sostiene la exclusion. | Agregar: "... y no está verificado que esas anotaciones estén disponibles localmente". |
| T10 | baja | G-T4 | l. 64 | "El único implante que se coloca y se sintetiza es un tornillo iliosacro paramétrico y rígido" | DEC 2026-09-11 (#41 APLICADA), DEC 2026-09-20 D3; 00T; TM l. 117; `CLAUDE.md` raiz; IMP #116 (actualizacion 2026-09-24) | El texto coincide con DEC, TM y 00T. Pero el `CLAUDE.md` raiz y la actualizacion de #116 (2026-09-24) dicen que el insumo de implantes sigue "PENDIENTE DE DEFINIR". No es error del texto (BITACORA §2: decision de DEC = hecho). Es una discrepancia del repositorio que ya advirtio el redactor (r00 §4.3). | Sin cambio en el texto. Escalar a la autora: actualizar `CLAUDE.md` raiz o declarar que falta decidir. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 28 | Los cuatro objetivos coinciden con los del cap. 3 | C3 §Vision general; MAPA l. 47 | si |
| l. 28 | GAPDEC: la pregunta aun promete 2D, Dice, HD95 y aumento convencional | IMP #126 (ABIERTA); introduccion l. 21; MAPA l. 63 | si (GAP justificado) |
| l. 28 | Se evalua coherencia fisica y quirurgica, no el efecto en segmentacion | 00T §Fuera de alcance 1; TM l. 62 | si |
| l. 32 | Cadena por difusion en dominio de imagen, implantes y artefacto local, coherencia fisica y quirurgica | TM l. 74; DEC 2026-09-19; 00T titulo | si |
| l. 32 | Colocacion restringida con criterios medidos sobre cada volumen | TM l. 52 ("corridor measured on each volume"), l. 78 | si |
| l. 32 | Codificacion multiventana de los HU | TM l. 79 ("multi-window encoding is kept") | si |
| l. 32 | Utilidad para segmentacion = trabajo futuro | 00T §Fuera de alcance 1; TM l. 83 | si |
| l. 37 | Compuerta Go/No-Go, ida y vuelta por el autoencoder de un modelo de difusion latente | TM l. 77 | si |
| l. 37 | MAE < 25 HU en hueso | TM l. 77 ("below a 25~HU threshold"); 00T l. 23 | si |
| l. 37 | Regla fijada antes de correr la prueba que decide | DEC 2026-09-17 (3); BITACORA §2; C3 l. 38 | parcial (T03) |
| l. 37 | 34 pacientes de prueba | TM l. 77 ("34 held-out patients"); 00T l. 26 | si |
| l. 37 | Veredicto reportado como resultado, positivo o negativo | 00T l. 24 (#91, DEC 2026-09-19 pto 1) | si |
| l. 39 | Poses 3D de un tornillo parametrico rigido alrededor del corredor medido | TM l. 78, l. 107; DEC 2026-09-11 (#41) | si |
| l. 39 | Marco de referencia de Kaiser et al. | DEC 2026-09-08 (marco de Kaiser); 00T l. 28-31; ficha `kaiser2014dysmorphism` | si |
| l. 39 | Criterio de viabilidad del corredor de McLaren et al. | C3 l. 89; DEC 2026-09-11 (2) | no (T02) |
| l. 39 | Grado de brecha cortical, escala ordinal de cuatro niveles | TM l. 52 ("four-level cortical-breach scale"), l. 96 | si |
| l. 39 | Referencia clinica = series navegada y convencional de Zwingmann et al., en S1 | TM l. 52; 00T l. 35-36; BITACORA §2 | si |
| l. 39 | Sin ajustar el muestreador a la referencia | DEC D-O2.1; TM l. 52, l. 78 ("No parameter ... derived") | si |
| l. 41 | *Inpainting* 2.5D en dominio de imagen, sin latente ni proyeccion | TM l. 79; DEC 2026-09-19; 00T l. 62-68 | si |
| l. 41 | $G = M \cup B_\delta$, $M$ mascara del implante | TM l. 79 | si |
| l. 41 | $B_\delta$ de unos 12 mm | TM l. 79 ("$\sim$12mm"); 00T l. 68 | si |
| l. 41 | La banda permite rayas y endurecimiento del haz fuera del metal | TM l. 79 | si |
| l. 41 | Comparacion con copia y pegado y con el protocolo fisico de Peters et al. | TM l. 62, l. 98; C3 tab:diseno; IMP #90 (contingencia, con GAPDEC en l. 76) | si |
| l. 43 | SAP como unica metrica introducida | DEC 2026-09-08 (BFC/ISC retiradas); 00T §Fuera de alcance 2; TM l. 80 | si |
| l. 43 | Wasserstein-1 frente a la referencia clinica | TM l. 80, l. 96 | si |
| l. 43 | *bone integrity*, *metal integrity*, *streak amplitude* con nombres publicados | TM l. 80; ficha `peters2025hybrid`; overleaf/CLAUDE.md terminos fijos | si |
| l. 46 | Cada objetivo tiene variable dependiente en el cap. 3 | C3 tab:diseno | si |
| l. 46 | Obj 1 fija su fallo de antemano (25 HU, regla) | DEC 2026-09-15 (2), 2026-09-17 (3); IMP #127.4; C3 l. 255 | parcial (T03) |
| l. 46 | GAPDEC: distancia W1 que contaria como fallo | IMP #127.6; DEC D-O2.1 (sin umbral); TM l. 96 ("reported as measured") | si (GAP justificado) |
| l. 46 | Superioridad frente a copia y pegado sobre las rayas, que esa linea base no produce | IMP #127.3 | si |
| l. 46 | GAPDEC: que haria fallar el Obj 3 | IMP #127.3 (ABIERTA) | si (GAP justificado) |
| l. 46 | Obj 4 comprobado con controles de consistencia | C3 §SAP (seis controles); BITACORA §2 | si |
| l. 46 | GAPDEC: evidencia del Obj 4 | IMP #127.6 (ABIERTA); MAPA l. 49 | si (GAP justificado) |
| l. 48 | El orden de los objetivos es el orden de las decisiones | DEC l. 144, l. 1044, l. 1136, l. 1407 | no (T01) |
| l. 48 | Compuerta formulada para difusion latente con ControlNet; veredicto negativo | TM l. 79 ("replaces ... ControlNet-guided Stable Diffusion 1.5"); 00T l. 24 | si (historico, no vigente) |
| l. 48 | Obj 3 reformulado despues del veredicto; la regla no se modifico | DEC 2026-09-19; 00T l. 69-70; TM l. 77 | si |
| l. 52 | La segmentacion depende de datos anotados y los artefactos ocultan limites | TM l. 46 | si |
| l. 52 | CTPelvic1K anota 14 de 75 volumenes con metal; 61 sin anotar | `liu2021ctpelvic1k`, Evidencia: "and 14 metal-affected CTs", "including 75 CTs with metal artifacts", "The remaining 61 metal-affected CTs are left unannotated" (Data annotation p. 3; Introduction p. 2) | si |
| l. 52 | Motivacion de fondo: aumento de datos para segmentacion peri-implante | `CLAUDE.md` raiz; TM l. 74 | si |
| l. 54 | Ninguno de los tres enfoques revisados resuelve colocacion y apariencia | TM l. 54 (Recognized Gap) | si |
| l. 54 | Los simuladores fisicos no colocan metal restringido y a escala | TM l. 50, l. 54 (sin cita) | parcial (T05) |
| l. 54 | Peters et al. colocan al azar en entrenamiento; la colocacion manual era impracticable | `peters2025hybrid`, Evidencia: "location ... in the training dataset was randomized", "manual metal placement was impractical" (Discussion p. 9) | si |
| l. 54 | Peters et al. usan colocacion experta en evaluacion | ficha `peters2025hybrid` l. 280-285 ("meaningful locations", lectura de la ficha) | parcial (T07) |
| l. 54 | Liu et al. optimizan una unica trayectoria | `liu2025pipeline`, "Trayectoria unica optima"; "formulated as an optimization problem" (Sec. III-D.3, p. 11) | si |
| l. 54 | Zwingmann et al. reportan distribuciones distintas segun tecnica | TM l. 52 (69 % frente a 40 % de grado 0); ficha `zwingmann2009navigated` | si |
| l. 56 | De Man et al.: rayas por endurecimiento del haz, dispersion, ruido y EEGE | `deman1999`, "Beam hardening, scatter, noise and EEGE are the most important causes" (Conclusiones, p. 695) | si |
| l. 56 | De Man et al. muestran rayas irradiando desde el metal | `deman1999`, "a number of streaks can be seen radiating from the metals" (Sec. III-D, p. 694) | si |
| l. 56 | CLAIM, DiffTumor y LGESynthNet: *inpainting* acotado a la mascara | fichas `ramzan2026claim` (l. 157, "RESPALDA"), `chen2024tumorsynthesis`, `jacob2026lgesynthnet` (l. 59, "Bounded inpainting ... fieles"); TM l. 48 | si |
| l. 56 | DiffBoost sintetiza el corte entero desde ruido | `zhang2025diffboost`, "Augment x_0 by n times ε ~ N(0; 1)" (Alg. 1, p. 3676) | si |
| l. 56 | Ninguno tiene mecanismo ni senal de entrenamiento fuera de la mascara | TM l. 48; `jacob2026lgesynthnet` l. 48-49 | si |
| l. 58 | C1: geometrias rigidas parametricas frente a umbral fijo de HU | TM l. 54 (C1); DEC 2026-09-11 (#41) | si |
| l. 58 | Tornillos extraidos por umbral aparecen fragmentados en la auditoria local | DEC l. 1210 (9 de 57, E8, #46); C3 l. 54 | parcial (T08) |
| l. 58 | C2: muestreador comparado con la distribucion clinica | TM l. 54 (C2) | si |
| l. 58 | C3: multiventana tomada de MAR, no reclamada | 00T §Fuera de alcance 4; TM l. 54; `li2024` ("multi-window network [11]", Sec. I, p. 1867); `wang2025adaptiveweighting` | si |
| l. 58 | Sin precedente publicado que cuantifique una banda de generacion | TM l. 54 ("no published precedent ... was found") | si |
| l. 60 | Distribucion de poses fijada por escrito antes de calcular distancias | TM l. 107; DEC D-O2.7 | si |
| l. 60 | Ningun parametro del muestreador se toma de la referencia | DEC D-O2.1; TM l. 107 | si |
| l. 60 | Latentes preentrenados, incluido uno de TC, excluyen hueso denso y metal | TM l. 77; 00T l. 26-27 (#93) | si |
| l. 64 | Coherencia fisica y quirurgica como alcance | 00T; TM l. 83 | si |
| l. 64 | 178 de los 1 184 volumenes | `docs/02-datos.md` l. 29-30 (103 + 75); C3 l. 42; `liu2021ctpelvic1k`, "including 1, 184 CT volumes" (p. 2) | si |
| l. 64 | Un unico implante: tornillo iliosacro parametrico y rigido; los reales no aportan geometria | DEC 2026-09-11 (#41), 2026-09-20 D3; TM l. 117 | si (T10: discrepancia del repositorio) |
| l. 64 | Comparacion solo en S1; segundo corredor descriptivo, sin distribucion ordinal | 00T l. 36-38; TM l. 52, l. 78; DEC D-O2.5; BITACORA §2 | si |
| l. 64 | Sintesis por parches en dominio de imagen | TM l. 79; 00T l. 64-66 | si |
| l. 68 | Dice y HD95 fuera de alcance | 00T §Fuera de alcance 1; DEC 2026-09-08 | si |
| l. 68 | 14 de 75 anotados; solo parte local | `liu2021ctpelvic1k` (ver l. 52); 00T §Fuera de alcance 1 (#13, #18) | parcial (T09) |
| l. 69 | Ablaciones a trabajo futuro, para liberar tiempo para compuerta y muestreador | 00T §Fuera de alcance 10 ("camino critico (VAE y muestreador)") | si |
| l. 70 | XCIST/CatSim fuera; se adopta Peters et al. | 00T §Fuera de alcance 3; IMP #8 (APLICADA); DEC 2026-09-07 | si |
| l. 71 | Efecto del dismorfismo no consistente entre estudios | 00T §Fuera de alcance 8; DEC 2026-09-08 (2) | si |
| l. 71 | Gardner et al. contrastan con un estudio previo sin diferencia | `gardner2010safezones`, "that study found no difference in the safe zone size" (Discusion, p. 628) | si |
| l. 71 | El muestreador mide el corredor en cada volumen | 00T §Fuera de alcance 8; TM l. 78 | si |
| l. 74 | Supuesto 1: apariencia generable en dominio de imagen; mecanismos no lineales en sinograma | TM l. 56; `deman1999`, "Noise artifacts are non-linear artifacts ..." (Sec. III-E, p. 694) | si |
| l. 74 | Supuesto 2: $B_\delta$ de unos 12 mm sin calibracion, trunca rayas lejanas | TM l. 79 ("deliberately truncates far-field streaks"), l. 54 | si |
| l. 74 | Supuesto 3: cortes de 2 mm de la literatura de tornillos pediculares; convencion geometrica | TM l. 52 ("2~mm bin width ... geometric convention") | parcial (T06, sin cita) |
| l. 74 | Supuesto 4: la serie navegada, sin nivel declarado, corresponde a S1 | TM l. 52; DEC 2026-09-17 C (#69); IMP #127.12 | si |
| l. 76 | Referencia de pelvis fracturadas; receptoras sin osteosintesis, no verificadas libres de fractura | TM l. 109, l. 121; IMP #125 | si |
| l. 76 | Al menos un paciente con fractura confirmada | IMP #125 (CLINIC_0060, confirmada por medico sin especialidad); C3 l. 253 | parcial (T04) |
| l. 76 | GAPDATO: cribado ciego de 30 casos, preparado y no realizado | IMP #125; `experiments/objetivo2/r3_fractura_revisor.csv` (columnas `revisor`/`fractura` vacias) | si (GAP justificado) |
| l. 76 | Cifras del Obj 2 dependen de un recorte condicionado a una revision no hecha | IMP #123 (ABIERTA); DEC 2026-09-14 (4) | si |
| l. 76 | GAPDATO: 16 casos de la revision | IMP #123 (16 filas; 14 por diametro + 2 por caja, MAPA l. 32); `e9ts_revision_laminas_autora.csv` (`veredicto` vacio) | si (GAP justificado) |
| l. 76 | Observaciones reales con reconstruccion no reportada | TM l. 115 | si |
| l. 76 | Protocolo fisico validado en 2D y para MAR | TM l. 119 ("two-dimensional and evaluates MAR"), l. 50 | si |
| l. 76 | GAPDATO: el sintetizador no genero ninguna muestra | IMP #116 (actualizacion 2026-09-24: `muestrea_ddim` sin llamador) | si (GAP justificado) |
| l. 76 | GAPDEC: equivalencia frente al protocolo fisico, contingencia de plazo | IMP #90 (actualizacion 2026-09-21: decidido solo en chat, no en DEC) | si (GAP justificado) |
| l. 39-71 | Claves citadas presentes en `overleaf/referencias.bib` y primer autor coincidente (Kaiser, McLaren, Zwingmann, Peters, Liu, De Man, Gardner) | `overleaf/referencias.bib` l. 434, 593, 1265, 705, 540, 117, 229; mas 88, 400, 498, 518, 738, 1040, 1179 | si |
| l. 23-76 | Ninguna cita como sujeto gramatical sola (E-F3) | revision del texto | si |
| l. 23-76 | Sin contenido retirado presentado como vigente (downstream, difusion latente/ControlNet, "31-60 %", BFC/ISC) | 00T §Fuera de alcance 1, 2, 5; `CLAUDE.md` raiz. ControlNet solo en l. 48, como historia | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Afirmacion de cronologia del proyecto ("orden en que se decidieron") sin cotejar las fechas de DEC | G-T4 | "El orden de los objetivos también es el orden en que se decidieron." | nuevo |
| La cita atribuye a la fuente un criterio que el metodo toma de otra o construye | E-R6 | "con el criterio de viabilidad del corredor de McLaren et al." | PAT-6 |
| Salvedad registrada en la implicancia o en otra seccion que se pierde al resumir en la introduccion | G-T4 | "tiene una fractura confirmada" (sin "por un médico sin especialidad") | PAT-31 |
| Generalizacion sobre la literatura sin `\cite` aunque las fichas existen | G-T4 | "Los simuladores físicos reproducen el mecanismo ... pero no colocan" | PAT-12 |
| Al resumir la preinscripcion en la introduccion, se omite la salvedad abierta del cap. 3 sobre la exploracion previa | G-T4, OC-3 | "su criterio de 25~HU y su regla ... se escribieron antes" | PAT-13 |
