# Auditoria de trazabilidad — introduccion — r04

Alcance acotado por pedido de la autora: l. 23-82 (Objetivos de investigacion, Justificacion, Alcance
y limitaciones / restricciones). El encabezado y la Formulacion del problema (l. 1-21) no se auditan
porque estan DESFASADOS (#126).
Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`; IMP = `docs/04-implicancias.md`; GLO =
`docs/03-glosario.md`.

Respuesta r03 considerada. T01 (r03) esta APLICADO: l. 46 lleva el mismo \GAPDEC que C3 l. 172. Los
agregados de r03 (guia-1 a guia-8, S13) se rastrearon uno por uno; figuran en el inventario. El lint r04
no marca nada dentro del alcance (sus tres medias estan en l. 7, 13 y 21).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2, OC-3 | l. 54, ultima oracion | "Este trabajo corre, además, el protocolo de Peters et al. sobre las poses del muestreador" | C3 l. 219, 221 (\GAPDATO "implementación y resultados del protocolo físico de Peters et al., no realizados"; subconjunto reducido de pacientes con \GAPDEC); C3 l. 225; IMP #90 (ABIERTA, act. 2026-09-21: el brazo fisico entero es la contingencia de plazo); BITACORA §2, decision 2026-09-30 (resumen de tramo con GAP lleva el mismo GAP) | Patron PAT-31 reincide. La oracion, agregada en r03, dice en presente indicativo que el trabajo corre el protocolo fisico. En C3 ese brazo esta sin implementar ni correr (\GAPDATO l. 221), se limita a un subconjunto de pacientes y depende del plazo (#90, que la autora dejo como contingencia). La introduccion solo dice que la comparacion "depende del plazo" en l. 82, dos subsecciones despues. En l. 54 la afirmacion pierde las tres condiciones, y el \GAPDEC que la sigue se apoya en ella como si fuera un hecho. | "Este trabajo prevé correr, además, el protocolo de Peters et al. sobre las poses del muestreador, en un subconjunto de pacientes, como comparación para la apariencia (Sección~\ref{sec:apariencia}) \GAPDATO{implementación y resultados del protocolo físico de Peters et al., no realizados} \GAPDEC{por qué hace falta ...}". Si se quiere evitar dos marcas seguidas, basta con "prevé correr" y una remision a la contingencia de l. 82. |
| T02 | media | G-T4, OC-2 | l. 43 (y l. 39) | "SAP reúne tres componentes ...: el grado de brecha ... y la viabilidad del corredor" | C3 l. 189 (\GAPDEC "calibre con que SAP evalúa la viabilidad del corredor: la decisión que define SAP fija el calibre nominal de 6.5 a 8.0 mm, y la corrida del Objetivo 2 usó los calibres de 4.91, 7.0 y 7.3 mm con una holgura de 1 mm"); MAPA (fila del \GAPDEC de calibre de SAP); BITACORA §2, decision 2026-09-30 | Patron PAT-31 reincide. El componente de viabilidad de SAP se agrego en r03 (guia-4) y lleva el \GAPDEC de C3 para la fraccion por zona de densidad, pero no el de C3 para la viabilidad. En C3, la decision que define SAP y lo que se corrio difieren en el calibre (PAT-20). La introduccion lo resume como "definidos en el Objetivo 2", y l. 39 dice "el calibre del tornillo" sin decir cual. Con eso la viabilidad parece cerrada, cuando C3 la marca abierta. | Añadir a la viabilidad el mismo GAP que C3: "... y la viabilidad del corredor, definidos en el Objetivo~2 \GAPDEC{calibre con que SAP evalúa la viabilidad del corredor, que difiere entre la decisión que define SAP y la corrida del Objetivo~2}, y la fracción por zona de densidad ósea \GAPDEC{...}". Anotar en MAPA que esa fila tambien esta en `introduccion` §Objetivos. |
| T03 | baja | G-T4 | l. 80, oraciones 2-3 | "Una malreducción residual en la referencia clínica estrecharía los corredores de sus pacientes" | C3 l. 263 (`reilly2003effect`: desplazamiento craneal de 5 a 20 mm reduce entre 36 y 90 % el area en S1, en seis pelvis cadavericas) | El mecanismo tiene fuente en el repositorio (Reilly et al.). El texto no la cita, pero el parrafo remite a `sec:amenazas`, donde si esta, asi que la fuente no queda oculta. En r03 se inventario como OK y no se reporto; es una observacion nueva, sin error de fondo. | Opcional: "... estrecharía los corredores de sus pacientes, como sugiere el efecto del desplazamiento de una fractura sacra medido por Reilly et al.~\cite{reilly2003effect} en pelvis cadavéricas, de una forma que ...". Si se añade, conservar la condicion "en pelvis cadavéricas" y "desplazamiento" (PAT-31), porque Reilly no mide malreduccion residual. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 28 | Los cuatro objetivos son los del cap. 3; solo Obj 2 y 3 son componentes de la cadena | C3 l. 9, fig. `fig:pipeline`, l. 185; MAPA l. 47 | si |
| l. 28 | Obj 1 es una prueba previa a la cadena; Obj 4 define o adopta las metricas | BITACORA §2 (introduccion-r01); C3 l. 20, 58, 185 | si |
| l. 28 | \GAPDEC: la pregunta aun promete 2D, Dice, HD95 y aumento convencional | IMP #126 (ABIERTA); introduccion l. 21; MAPA l. 63 | si (GAP justificado) |
| l. 32 | Cadena de difusion en dominio de imagen; implantes y artefacto local; coherencia fisica y quirurgica | TM l. 74; 00T titulo; DEC 2026-09-19 | si |
| l. 32 | Osteosintesis = dispositivos de fijacion osea, como tornillos y placas | `CLAUDE.md` raiz ("implantes de osteosintesis (tornillos, placas)") | si |
| l. 32 | Corredor oseo medido en cada volumen; glosa "sin atravesar la cortical" | TM l. 52; GLO l. 52-53 | si |
| l. 32 | Codificacion multiventana: varios canales, cada uno con una ventana de HU | TM l. 77, 79; C3 l. 60 | si |
| l. 32 | Unico implante sintetizado: tornillo iliosacro; utilidad para segmentacion fuera del objetivo | DEC 2026-09-11 (#41); C3 l. 9, 36; 00T §Fuera de alcance 1 | si |
| l. 37 | Titulo: el autoencoder de un modelo de difusion latente conserva los HU de la codificacion | TM l. 77 ("HU to multi-window to VAE to HU"); C3 l. 58; BITACORA §2 (2026-09-30) | si |
| l. 37 | MAE < 25 HU en hueso | TM l. 77; 00T l. 23; DEC 2026-09-15 (2); C3 l. 71, tab:diseno fila 1 | si |
| l. 37 | El autoencoder comprime a un latente donde opera la difusion | `rombach2022latentdiffusion`, "we apply them in the latent space of powerful pretrained autoencoders" (Abstract, p. 1) | si |
| l. 37 | 34 pacientes de prueba | TM l. 77 ("34 held-out patients"); C3 l. 50, 71 | si |
| l. 39 | Tornillo iliosacro (une ilion y sacro), parametrico y rigido | TM l. 78; DEC 2026-09-11 (#41); GLO l. 74-75 | si |
| l. 39 | Poses en el marco de Kaiser et al.; viabilidad = calibre + holgura radial de Kaiser | DEC 2026-09-08; C3 l. 83, 89; BITACORA §2 (introduccion-r01) | parcial (T02: calibre abierto en C3 l. 189) |
| l. 39 | Grado de brecha cortical, escala ordinal de cuatro niveles | TM l. 52; C3 l. 79, 189, 194; GLO l. 45-48 | si |
| l. 39 | Referencia clinica = series navegada y convencional de Zwingmann et al., en S1 | TM l. 52; C3 l. 79, 200; 00T l. 35-36 | si |
| l. 39 | S1 = primer segmento del sacro | `kaiser2014dysmorphism`, "first sacral segment" (Fig. 1, p. e120(3)) | si |
| l. 39 | Serie navegada con navegacion computarizada; convencional sin ella | `zwingmann2009navigated`, titulo de la ficha (l. 1); "before the navigation system was available in our department" (Materials and Methods, p. 1834, ficha l. 299) | si |
| l. 39 | Sin ajustar el muestreador a la referencia | DEC D-O2.1; C3 l. 79, 158, 207 | si |
| l. 39 | Wasserstein-1 = suma de diferencias absolutas de las acumuladas | C3 ec. `eq:w1` (l. 200-205) | si |
| l. 41 | *Inpainting* 2.5D en dominio de imagen, sin latente ni proyeccion; 2.5D se remite al marco teorico | TM l. 79; C3 l. 172; BITACORA §2 (glosas) | si |
| l. 41 | $G = M \cup B_\delta$; $B_\delta$ de unos 12 mm; rayas y endurecimiento fuera del metal | TM l. 79; C3 l. 15, 176; GLO l. 36-41 | si |
| l. 41 | Comparacion con copia y pegado (sin artefacto) y protocolo fisico de Peters et al. | C3 l. 185, 219 | si |
| l. 43 | SAP, unica metrica introducida; incluye W1; comparacion en Obj 2 | 00T §Fuera de alcance 2; TM l. 80; C3 l. 13; BITACORA §2 (introduccion-r01) | si |
| l. 43 | SAP con tres componentes; solo los grados se comparan; los otros dos descriptivos | C3 l. 189, tab:diseno fila 2 | si, salvo T02 |
| l. 43 | \GAPDEC: fuente y definicion de la fraccion por zona de densidad | C3 l. 166 (mismo \GAPDEC); MAPA l. 39 | si (GAP justificado) |
| l. 43 | *bone integrity*, *metal integrity*, *streak amplitude*, nombres publicados | ficha `peters2025hybrid` l. 358; C3 l. 213; overleaf/CLAUDE.md terminos fijos | si |
| l. 43 | Metricas disenadas para MAR; invertirlas; \GAPDEC de la inversion | C3 l. 215 (mismo \GAPDEC); IMP #17; MAPA l. 42 | si (GAP justificado) |
| l. 46 | Compuerta formulada para difusion latente con ControlNet; veredicto negativo; Obj 3 reformulado despues; regla no modificada | C3 l. 38, 174, 255; DEC 2026-09-19; TM l. 77 | si (historico, no vigente) |
| l. 46 | Latente entrenado con TC examinado despues del veredicto, misma regla y mismos pacientes | TM l. 77 ("A CT-trained latent was examined next, under the same rule and on the same held-out patients"); C3 l. 75, 255 | si |
| l. 46 | El veredicto descarto la ruta latente, no la codificacion multiventana | TM l. 77 ("the latent route is abandoned"); C3 l. 172 | si |
| l. 46 | \GAPDEC: error de ida y vuelta sin autoencoder | C3 l. 172 (mismo \GAPDEC); MAPA l. 40 | si (T01 r03 aplicado) |
| l. 48 | Obj 1 a 3 con variable dependiente; Obj 4 sin variable dependiente propia | C3 l. 185, tab:diseno | si |
| l. 48 | Regla operativa despues de una exploracion con los pacientes de prueba, ya por encima del criterio; antes de la prueba que decide; 25 HU anterior y sin moverse | C3 l. 58, 255; DEC 2026-09-15 (2), 2026-09-17 (3); IMP #127.4 | si |
| l. 48 | \GAPDEC: distancia W1 que contaria como fallo | C3 l. 207; IMP #127.6; MAPA l. 50 | si (GAP justificado) |
| l. 48 | Superioridad frente a copia y pegado sobre *streak amplitude*, que esa insercion no produce; no dice si las rayas se parecen a las reales | C3 l. 217 | si |
| l. 48 | \GAPDEC: que haria fallar el Obj 3 | C3 l. 217; IMP #127.3; MAPA l. 55 | si (GAP justificado) |
| l. 48 | Obj 4 comprobado con controles de consistencia; \GAPDEC sobre su evidencia | C3 l. 185, 198; MAPA l. 49 | si (GAP justificado) |
| l. 52 | Segmentacion depende de datos anotados; artefactos ocultan limites | TM l. 46 (sin cita) | si (T05 r02 no aplicado con motivo; no se re-reporta) |
| l. 52 | CTPelvic1K: hueso anotado en 14 de 75 volumenes con metal; 61 sin anotar | `liu2021ctpelvic1k`, "and 14 metal-affected CTs", "including 75 CTs with metal artifacts", "The remaining 61 metal-affected CTs are left unannotated" (p. 2-3) | si |
| l. 52 | Motivacion de fondo: aumento de datos; las condiciones de los datos impiden medir la utilidad | `CLAUDE.md` raiz; TM l. 74, 83; 00T §Fuera de alcance 1 | si |
| l. 52 | \GAPDEC: por que la coherencia antes de la utilidad | MAPA l. 64 | si (GAP justificado) |
| l. 54 | Ninguno de los tres enfoques da a la vez distribucion de poses y apariencia | TM l. 54 (Recognized Gap) | si |
| l. 54 | Peters et al.: colocacion aleatoria en entrenamiento; colocacion manual impracticable | `peters2025hybrid`, "location of the metal objects in the training dataset was randomized", "manual metal placement was impractical" (Discussion, p. 9) | si |
| l. 54 | Peters et al.: conjuntos clinicamente representativos, metal en "meaningful locations", sin regla | `peters2025hybrid`, fila l. 217 (Discussion, p. 9); nota l. 285 | si |
| l. 54 | Liu et al. optimizan una unica trayectoria | TM l. 52; ficha `liu2025pipeline` ("formulated as an optimization problem", Sec. III-D.3, p. 11) | si |
| l. 54 | Zwingmann et al.: distribuciones de malposicion distintas por tecnica; lectura propia | C3 l. 79, 200 (69/15/8/8 frente a 40/37/11.5/11.5 %); BITACORA §2 (lectura operativa propia) | si |
| l. 54 | El trabajo corre el protocolo de Peters et al. sobre las poses del muestreador | C3 l. 219 (mismas poses); C3 l. 221 (\GAPDATO no realizado; subconjunto); IMP #90 (contingencia) | no (T01) |
| l. 54 | \GAPDEC: por que hace falta un sintetizador aprendido | MAPA l. 66; ninguna fuente (TM, 00T, DEC) da la razon | si (GAP justificado) |
| l. 56 | De Man et al.: rayas por endurecimiento, dispersion, ruido y EEGE; irradian desde el metal | `deman1999`, "Beam hardening, scatter, noise and EEGE are the most important causes" (p. 695); "streaks can be seen radiating from the metals" (Sec. III-D, p. 694) | si |
| l. 56 | CLAIM, DiffTumor, LGESynthNet: *inpainting* acotado a la mascara; DiffBoost desde ruido; ninguno con senal fuera de la mascara | TM l. 48; fichas `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`, `zhang2025diffboost` (Alg. 1, p. 3676) | si |
| l. 58 | Geometrias rigidas parametricas como mascara de sintesis, frente a umbral fijo | TM l. 54 (C1); DEC 2026-09-11 (#41); C3 l. 101 | si |
| l. 58 | Xie et al.: el umbral, en cortes simulados, cubrio el implante en exceso | `xie2024implantsegmentation`, ficha l. 29 (Tabla 2, p. 11, datos simulados); TM C1 | si |
| l. 58 | Tornillos extraidos con umbral fijo aparecen fragmentados en la cohorte local | C3 l. 54 (sec:datos) | si |
| l. 58 | El entrenamiento usa mascaras umbralizadas de metal real; su diferencia con el cilindro es un desplazamiento de dominio | C3 l. 178, 182 | si |
| l. 58 | Ningun objetivo aisla el aporte: ningun brazo coloca geometrias extraidas por umbral | C3 l. 219 (tres brazos, mismas poses de implante); C3 l. 101, sec:geometria; DEC 2026-09-11 (#41) | si |
| l. 58 | Muestreador comparado con la referencia clinica | TM l. 54 (C2); C3 l. 79 | si |
| l. 60 | Sin precedente que fije con valor numerico una banda de generacion | GLO l. 39-41; C3 l. 176 | si |
| l. 60 | Varias ventanas de HU vienen de MAR, aplicadas a reconstruccion o perdida, no a la entrada | TM l. 54; GLO l. 29-32 (aviso #24); fichas `wang2025adaptiveweighting` (l. 49), `li2024` (l. 87, 107) | si |
| l. 60 | Ningun objetivo aisla la codificacion; Obj 3 evalua el sintetizador completo | C3 tab:diseno fila 3 (VI = brazo); 00T §Fuera de alcance 10 | si |
| l. 62 | Distribucion de poses fijada por escrito antes de calcular distancias; ningun parametro de la referencia | C3 l. 127, 158, 253; DEC D-O2.1-D-O2.7 | si |
| l. 62 | Latentes preentrenados examinados, incluido uno de TC, excluyen hueso denso y metal; el veredicto no se limita a una arquitectura | TM l. 77 ("The finding generalizes the outcome ... defined over intensity ranges that exclude dense bone and metal"); 00T l. 26-27 (#93); C3 l. 75, 255 | si |
| l. 66 | 178 de los 1 184 volumenes | C3 l. 42 (103 + 75); `docs/02-datos.md`; `liu2021ctpelvic1k`, "including 1, 184 CT volumes" (p. 2) | si |
| l. 66 | Unico implante: tornillo iliosacro parametrico rigido; los reales no aportan geometria | C3 l. 54; DEC 2026-09-11 (#41), 2026-09-20 D3 | si |
| l. 66 | Referencia clinica y marco de Kaiser se refieren a tornillos iliosacros | `zwingmann2009navigated`, "were treated with navigated iliosacral screw placement" (M&M, p. 1834); `kaiser2014dysmorphism`, "for passage of an iliosacral screw" | si |
| l. 66 | \GAPDEC: razon para restringir al tornillo iliosacro | MAPA l. 67; DEC #41 fija la geometria, no el tipo | si (GAP justificado) |
| l. 66 | Comparacion solo en S1; segundo corredor sin distribucion ordinal clinica; eje medido | C3 l. 164; 00T l. 36-38; MAPA l. 38 (69 de 72) | si |
| l. 66 | \GAPDATO: muestreo en el segundo corredor | C3 l. 164 (mismo \GAPDATO); `preinscripcion_muestreador.md` §7 | si (GAP justificado) |
| l. 66 | Sintesis por parches, en dominio de imagen | TM l. 79; 00T l. 64-66; C3 l. 172 | si |
| l. 70 | Dice y HD95 fuera de alcance; 14 de 75 anotados; no verificado localmente; solo parte local | C3 l. 36; 00T §Fuera de alcance 1; `liu2021ctpelvic1k` (ver l. 52) | si |
| l. 71 | Ablaciones a trabajo futuro, para tiempo de compuerta y muestreador | 00T l. 124-126 (punto 10, "camino critico (VAE y muestreador)") | si |
| l. 71 | \GAPDEC: que restricciones cubriria la ablacion | C3 l. 158, 166; MAPA l. 65 | si (GAP justificado) |
| l. 72 | Validacion de XCIST preliminar y sin estudio de artefacto metalico | `wu2022xcist`, "qualitative and semi-quantitative first-order evaluation" (Validation, p. 9); ficha l. 156, 165 | si |
| l. 72 | Peters et al.: corre sobre ese simulador, publica metricas, valida contra fantoma fisico; 2D, MAR, sin paso hibrido | `peters2025hybrid`, "metal artifact simulation capability is experimentally validated in CT phantom scans"; "all datasets are simulated in 2D" (Abstract, p. 1); ficha l. 101, 211; C3 l. 219, 221 | si |
| l. 73 | Gardner et al.: sacro dismorfico descrito por rasgos radiograficos | `gardner2010safezones`, "angulated upsloping sacral ala, atrophic residual transverse processes" (Introduccion, p. 622, ficha l. 317-318) | si |
| l. 73 | Gardner et al.: zona segura de S1 menor en dismorficos; estudio previo sin diferencia | `gardner2010safezones`, "cross-sectional area was 36% smaller in dysmorphic" (p. 624); "that study found no difference in the safe zone size" (p. 628); C3 l. 168 | si |
| l. 76 | Supuesto 1: apariencia generable en imagen; De Man: mecanismos no lineales, aislados en el sinograma | TM l. 56; `deman1999`, "Noise artifacts are non-linear artifacts, just like beam hardening and scatter artifacts" (Sec. III-E, p. 694); ficha l. 134-138 | si |
| l. 76 | La comparacion con el protocolo fisico puede contradecirlo, si se mantiene en plazo | C3 l. 225, 261; IMP #90 | si |
| l. 76 | Supuesto 2: serie navegada sin nivel declarado = S1 | C3 l. 259; ficha `zwingmann2009navigated` l. 301 (NO ENCONTRADO de forma explicita); DEC 2026-09-17 C (#69) | si |
| l. 76 | Supuesto 3: relacion mascara-artefacto independiente del tipo; entrenamiento con componentes de todo tipo | C3 l. 180, 261 | si |
| l. 78 | Convencion 1: $B_\delta$ ~12 mm, ninguna fuente lo calibra, trunca rayas lejanas | C3 l. 176, 261; GLO l. 40-41 | si |
| l. 78 | Convencion 2: limites de grado de 2 mm de ancho, de tornillos pediculares, via Smith et al.; convencion y supuesto | `gertzbein1990`, Tabla 1 (tramos "0-2 mm / 2.1-4.0 mm", p. 13); `mirza2003` ("The thresholds reported in prior studies were used", p. 405); `smith2006iliosacral` (p. 236); C3 l. 194, 257 | si |
| l. 78 | Convencion 3: grados equiespaciados en W1 | C3 l. 200, 261 | si |
| l. 78 | Convencion 4: margen de 5 mm de Kaiser para la longitud util = dos desviaciones estandar | `kaiser2014dysmorphism`, "no less than 5 mm of distance to the cortex on either side" (p. e120(2)); C3 l. 83, 158, tab:preinscripcion | si |
| l. 78 | \GAPDEC: justificacion de $h = 2\sigma$ | C3 l. 158 (mismo \GAPDEC); MAPA l. 48 | si (GAP justificado) |
| l. 80 | Referencia de pelvis fracturadas; receptoras sin osteosintesis, no verificadas libres de fractura | C3 l. 52, 253, 263; IMP #125 | si |
| l. 80 | Malreduccion residual estrecharia corredores; fractura no detectada, por otra causa | C3 l. 253, 263 (`reilly2003effect`) | si, sin cita (T03) |
| l. 80 | Corredor mas estrecho que el tornillo de medicion: el eje ya perfora, grado 0 inalcanzable; W1 puede moverse sin el muestreador | C3 l. 209 | si |
| l. 80 | Al menos un paciente con fractura confirmada por medico sin especialidad | C3 l. 253; IMP #125 | si |
| l. 80 | \GAPDATO: cribado ciego de 30 casos, preparado y no realizado | C3 l. 52 (15 + 15); IMP #125; MAPA l. 33 | si (GAP justificado) |
| l. 80 | Cifras principales del Obj 2 dependen de una variante condicionada a una revision no hecha | C3 l. 91; IMP #123 (ABIERTA, formulada como GAP) | si |
| l. 80 | \GAPDATO: revision de la autora de 16 casos | C3 l. 91 (mismo \GAPDATO); MAPA l. 32 | si (GAP justificado) |
| l. 80 | TotalSegmentator no reporta exactitud para la etiqueta de S1 | `wasserthal2023`, fila 3e "Dice por clase: S1 — NO ENCONTRADO EN EL PDF" y fila 2d (S1 no es clase en la version del PDF); C3 l. 85, 263 | si |
| l. 80 | El control de nivel excluyo, en proporcion, mas pacientes con objetos no ortopedicos; efecto sobre la distribucion | C3 l. 52 (11 de 34 frente a 7 de 57), l. 253 | si |
| l. 80 | Envolvente osea: cierre que podria ocupar canal y foramenes; \GAPDATO | C3 l. 87, 257 (mismo \GAPDATO); MAPA l. 57 | si (GAP justificado) |
| l. 82 | Reconstruccion no reportada; MAR del fabricante o monoenergetica cambian la apariencia | C3 l. 44; `selles2024marreview` (ficha l. 9, 42; "varies by vendor", Sec. 3.5, p. 6) | si |
| l. 82 | Protocolo fisico validado en 2D y para MAR; la adaptacion no hereda la validacion | C3 l. 221, 263; ficha `peters2025hybrid` l. 101, 211 | si |
| l. 82 | Tres desplazamientos de dominio; solo el tercero cuantificado | C3 l. 182 (0.62 frente a 1.40) | si |
| l. 82 | \GAPDEC: metrica de los dos primeros desplazamientos | C3 l. 182 (mismo \GAPDEC); MAPA l. 59 | si (GAP justificado) |
| l. 82 | $B_\delta$ trunca las rayas y el protocolo fisico no; la comparacion no puede mostrar las rayas lejanas | C3 l. 261 | si |
| l. 82 | \GAPDATO: el sintetizador no genero ninguna muestra | C3 l. 38; IMP #116; MAPA l. 30 | si (GAP justificado) |
| l. 82 | \GAPDEC: equivalencia frente al protocolo fisico, contingencia de plazo | C3 l. 225; IMP #90; MAPA l. 44 | si (GAP justificado) |
| l. 37-82 | Claves citadas existen en `overleaf/referencias.bib`; apellidos nombrados = primer autor (Kaiser, Zwingmann, Peters, Liu, De Man, Xie, Gardner, Smith; `wasserthal2023` sin apellido nombrado) | `overleaf/referencias.bib` l. 117, 229, 262, 434, 498, 518, 540, 626, 705, 773, 847, 868, 1040, 1051, 1073, 1093, 1265 y las de l. 56 (88, 400, 738, 1179) | si |
| l. 23-82 | Ninguna cita como sujeto gramatical sola (E-F3) | revision del texto | si |
| l. 23-82 | Sin fuentes de fabricante citadas (P-EA1) | revision del texto | si (no aplica) |
| l. 23-82 | Sin contenido retirado presentado como vigente (downstream como objetivo, difusion latente o ControlNet, "31-60 %", BFC/ISC) | 00T §Fuera de alcance 1, 2, 5; `CLAUDE.md` raiz. Latente y ControlNet solo en l. 37, 46 y 62, como compuerta e historia; Dice y HD95 solo en l. 70, como exclusion | si |
| l. 23-82 | Patrones VIGENTES de dominio G-T4/E-R6 (PAT-6, 31, 49, 51, 53) | revision del texto: PAT-31 reincide dos veces (T01, T02); PAT-6 (Gardner, Kaiser), PAT-49 (l. 58, 60), PAT-51 (l. 72) y PAT-53 sin reincidencia | si, salvo T01 y T02 |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un agregado de la ronda resume un tramo del cap. 3 que lleva GAP (o una contingencia) y lo omite | G-T4, OC-2 | "Este trabajo corre, además, el protocolo de Peters et al. sobre las poses" | PAT-31 |
| Un componente se resume con el GAP de otro componente, pero sin el suyo propio | G-T4, OC-2 | SAP: GAP en la fraccion de densidad, ninguno en la viabilidad (C3 l. 189) | PAT-31 |
