# Auditoria de trazabilidad — introduccion — r05

Alcance acotado por pedido de la autora: l. 23-84 (Objetivos de investigacion, Justificacion y Alcance
y limitaciones / restricciones). El encabezado y la Formulacion del problema (l. 1-21) no se auditan
porque estan DESFASADOS (#126).
Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`; IMP = `docs/04-implicancias.md`; GLO =
`docs/03-glosario.md`.

Respuesta r04 considerada. T01 (r04) esta APLICADO: l. 54 dice "prevé ejecutar ... en un subconjunto de
pacientes y según el plazo", y la contingencia tiene su \GAPDEC en l. 84. T02 (r04) esta APLICADO: l. 43
lleva el \GAPDEC del calibre de SAP, igual al de C3 l. 189. T03 (r04) fue NO APLICADO con motivo (remision a
`sec:amenazas`, donde esta Reilly et al.), asi que no se re-reporta. Los cambios de estilo de r04 (S04 De Man,
S05 Gardner, S06/S07 control de nivel, S10 autoencoder, guia-1, guia-6, guia-7) se rastrearon uno por uno y
figuran en el inventario. El lint r05 no marca nada dentro del alcance (sus tres medias y su baja estan en
l. 7, 13 y 21).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | baja | G-T4 | l. 82, oraciones 3-4 | "un control verifica el nivel S1 ... Ese control excluyó a 11 de 34 ... y a 7 de 57" | C3 l. 52 ("La discordancia de nivel excluyó a 11 de 34 ... y a 7 de 57 ..., y un paciente más se excluyó porque S1 tocaba el borde"); IMP l. 4548-4549 (grupo 3: 57 - 7 - 1 = 49; el caso de borde es `CLINIC_0010`, grupo 3); DEC l. 748-749 | Las cifras 11/34 y 7/57 coinciden con la fuente, pero ahi corresponden a la discordancia de nivel. Si "ese control" se lee como el control de nivel de C3 (discordancia mas borde del campo de vision), excluyo a 8 de 57 pacientes sin objeto, no a 7. La lectura de la oracion anterior ("verifica el nivel S1") salva el numero, pero el lector que vaya a C3 encuentra que el control tiene dos causas. C3 l. 253 tiene la misma formulacion, asi que la introduccion la copio de ahi; C3 l. 52 es la precisa. La conclusion (mas perdida del grupo 2) no cambia. | "La discordancia de nivel excluyó a 11 de 34 pacientes con objetos no ortopédicos y a 7 de 57 sin objeto". Avisar al orquestador de que C3 l. 253 lleva la misma imprecision. |
| T02 | baja | G-T4, E-R6 | l. 82, oracion 2 | "Si esa revisión mostrara un fallo ..., cambiarían sus diámetros de corredor" | IMP #123 (ABIERTA): condicion de reapertura "el recorte de 6 mm se mantiene como principal salvo que esta revision muestre un fallo suyo"; "todo el Objetivo 2 se calcula sobre `default6mm`"; C3 l. 91 | La consecuencia se acota a los casos marcados ("sus diámetros", "sus poses y grados"). Segun #123, un fallo reabre la eleccion del recorte principal, y de esa eleccion salen todas las cifras de la cohorte (72 casos, viabilidad, W1), no solo las de los 16 casos. La primera oracion del parrafo ya dice que las cifras principales dependen de la variante, asi que el error de fondo es menor: la segunda lo achica. | "Si esa revisión mostrara un fallo de la variante, se reabriría su elección como variante principal, y con ella cambiarían los diámetros de corredor, las poses y los grados de brecha de la cohorte." |
| T03 | baja | G-T4 | l. 46, oracion 3 | "se examinó ... un autoencoder entrenado con TC (Sección~\ref{sec:amenazas})" | C3 l. 75 (sec:obj1: extension de la compuerta al latente de Guo et al., cota por saturacion); C3 l. 255 y 265 (sec:amenazas, solo lo mencionan como amenaza) | La remision lleva a amenazas, donde el autoencoder de TC aparece como riesgo de validez, y no a la seccion que describe la extension y su cota (C3 l. 75, `sec:obj1`). La afirmacion tiene respaldo, pero el lector que siga la remision no encuentra que se examino ni como. | Cambiar la remision a `Sección~\ref{sec:obj1}`, o dar las dos: "(Secciones~\ref{sec:obj1} y~\ref{sec:amenazas})". |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 28 | Los cuatro objetivos son los del cap. 3; solo Obj 2 y 3 son componentes de la cadena; Obj 1 previo | C3 l. 9, fig. `fig:pipeline`, l. 185; BITACORA §2 (introduccion-r01) | si |
| l. 28 | Obj 1 a 3 con variable dependiente; Obj 4 sin variable dependiente propia, define o adopta metricas | C3 l. 185, `tab:diseno` (tres filas) | si |
| l. 28 | \GAPDEC: la pregunta aun promete 2D, Dice, HD95 y aumento convencional | IMP #126 (ABIERTA); introduccion l. 21; MAPA l. 63 | si (GAP justificado) |
| l. 32 | Cadena de difusion en dominio de imagen; implantes y artefacto local; coherencia fisica y quirurgica | TM l. 74; 00T titulo; DEC 2026-09-19 | si |
| l. 32 | Osteosintesis = dispositivos de fijacion osea, como tornillos y placas | `CLAUDE.md` raiz ("implantes de osteosintesis (tornillos, placas)") | si |
| l. 32 | Corredor oseo medido en cada volumen; glosa "sin atravesar la cortical" | TM l. 52; GLO l. 52-53 | si |
| l. 32 | Codificacion multiventana: varios canales, cada uno con una ventana de HU | TM l. 77, 79; C3 l. 60 | si |
| l. 32 | Unico implante: tornillo iliosacro; utilidad para segmentacion fuera del objetivo | DEC 2026-09-11 (#41); C3 l. 9, 36; 00T §Fuera de alcance 1 | si |
| l. 37 | Titulo: el autoencoder de un modelo de difusion latente conserva los HU (compuerta Go/No-Go) | TM l. 77; C3 l. 58; BITACORA §2 (2026-09-30) | si |
| l. 37 | MAE < 25 HU en hueso | TM l. 77; 00T l. 23; DEC 2026-09-15 (2); C3 l. 71, `tab:diseno` fila 1 | si |
| l. 37 | El autoencoder comprime a un espacio latente, donde opera la difusion, y reconstruye | `rombach2022latentdiffusion`, "we apply them in the latent space of powerful pretrained autoencoders" (Abstract, p. 1) | si |
| l. 37 | 34 pacientes de prueba | TM l. 77 ("34 held-out patients"); C3 l. 50, 71 | si |
| l. 39 | Tornillo iliosacro (une ilion y sacro), parametrico y rigido | TM l. 78; DEC 2026-09-11 (#41); GLO l. 74-75 | si |
| l. 39 | Poses en el marco de Kaiser et al.; viabilidad = calibre + holgura radial de Kaiser | DEC 2026-09-08; C3 l. 83, 89; BITACORA §2 (introduccion-r01); calibre abierto con \GAPDEC en l. 43 | si |
| l. 39 | Grado de brecha cortical, escala ordinal de cuatro niveles | TM l. 52; C3 l. 79, 189, 194; GLO l. 45-48 | si |
| l. 39 | Referencia clinica = series navegada y convencional de Zwingmann et al., en S1 | TM l. 52, 78; C3 l. 79, 200; 00T l. 35-36 | si |
| l. 39 | S1 = primer segmento del sacro | `kaiser2014dysmorphism`, "first sacral segment" (Fig. 1, p. e120(3)) | si |
| l. 39 | Serie navegada con navegacion computarizada; convencional sin ella | `zwingmann2009navigated`, titulo; "before the navigation system was available in our department" (M&M, p. 1834) | si |
| l. 39 | El muestreador no se ajusto a la referencia | TM l. 78 ("No parameter of the sampler is derived from those distributions"); DEC D-O2.1; C3 l. 79, 207 | si |
| l. 39 | Wasserstein-1 = suma de diferencias absolutas de las acumuladas | C3 ec. `eq:w1` (l. 200-205) | si |
| l. 41 | *Inpainting* 2.5D en dominio de imagen, sin latente ni proyeccion; 2.5D se remite al marco teorico | TM l. 79; C3 l. 172; BITACORA §2 (glosas) | si |
| l. 41 | $G = M \cup B_\delta$; $B_\delta$ de unos 12 mm; rayas y endurecimiento fuera del metal | TM l. 79; C3 l. 15, 176; GLO l. 36-41 | si |
| l. 41 | Comparacion con copia y pegado (sin artefacto), protocolo fisico de Peters et al. y observaciones reales | C3 l. 185, 215, 219; TM l. 127 | si |
| l. 41 | \GAPDEC: metrica y analisis de la comparacion con observaciones reales | C3 l. 215 (mismo \GAPDEC); MAPA l. 61 | si (GAP justificado) |
| l. 43 | SAP, unica metrica introducida; incluye W1; comparacion ejecutada en el Obj 2 | TM l. 80; 00T §Fuera de alcance 2; C3 l. 13; BITACORA §2 (introduccion-r01) | si |
| l. 43 | SAP con tres componentes; solo los grados se comparan; los otros dos descriptivos | C3 l. 189, `tab:diseno` fila 2 | si |
| l. 43 | \GAPDEC: calibre de la viabilidad (decision frente a corrida) | C3 l. 189 (mismo \GAPDEC: 6.5-8.0 mm frente a 4.91/7.0/7.3 mm); MAPA l. 54 | si (T02 r04 aplicado) |
| l. 43 | \GAPDEC: fuente y definicion de la fraccion por zona de densidad | C3 l. 166 (mismo \GAPDEC); MAPA l. 39 | si (GAP justificado) |
| l. 43 | *bone integrity*, *metal integrity*, *streak amplitude*, nombres publicados; disenadas para MAR | TM l. 80; ficha `peters2025hybrid` l. 358; C3 l. 213, 215 | si |
| l. 43 | \GAPDEC: inversion de cada metrica | C3 l. 215 (mismo \GAPDEC); IMP #17; MAPA l. 42 | si (GAP justificado) |
| l. 46 | Compuerta formulada para difusion latente con ControlNet; veredicto negativo; Obj 3 reformulado despues; regla no modificada | TM l. 77 ("that redesign was decided after seeing this result", "the gate rule ... is not modified"); C3 l. 38, 174, 255 | si (historico, no vigente) |
| l. 46 | Autoencoder entrenado con TC examinado despues del veredicto, misma regla y mismos pacientes | TM l. 77 ("A CT-trained latent was examined next, under the same rule and on the same held-out patients"); C3 l. 75; ficha `guo2025maisi` l. 70 ("VAE-GAN"), l. 23 (39 206 CT + 18 827 RM) | si (remision: T03) |
| l. 46 | El veredicto descarto la ruta latente, no la codificacion multiventana, que sigue sin autoencoder | TM l. 77 ("the latent route is abandoned"), l. 79 ("The multi-window encoding is kept ... with no compression stage"); C3 l. 172 | si |
| l. 46 | \GAPDEC: error de ida y vuelta sin autoencoder | C3 l. 172 (mismo \GAPDEC); MAPA l. 40 | si (GAP justificado) |
| l. 48 | Regla operativa despues de una exploracion con los pacientes de prueba cuyo error superaba el criterio; antes de la prueba que decide; 25 HU anterior y sin moverse | C3 l. 58, 255; DEC 2026-09-15 (2), 2026-09-17 (3); IMP #127.4 | si |
| l. 48 | \GAPDEC: distancia W1 que contaria como fallo | C3 l. 207; MAPA l. 50 | si (GAP justificado) |
| l. 48 | Superioridad frente a copia y pegado sobre *streak amplitude*, que esa insercion no produce; no dice si las rayas se parecen a las reales | C3 l. 217 | si |
| l. 48 | \GAPDEC: que haria fallar el Obj 3 | C3 l. 217; MAPA l. 55 | si (GAP justificado) |
| l. 48 | Obj 4 comprobado con controles de consistencia; \GAPDEC sobre su evidencia | C3 l. 185, 198; MAPA l. 49 | si (GAP justificado) |
| l. 52 | Segmentacion depende de volumenes anotados; artefactos ocultan limites | TM l. 46 (sin cita; T05 r02 no aplicado con motivo, no se re-reporta) | si |
| l. 52 | CTPelvic1K: hueso anotado en 14 de 75 volumenes con metal; 61 sin anotar | `liu2021ctpelvic1k`, "and 14 metal-affected CTs", "including 75 CTs with metal artifacts", "The remaining 61 metal-affected CTs are left unannotated" (p. 2-3) | si |
| l. 52 | Motivacion de fondo: aumento de datos; la escasez de volumenes con metal anotados impide medir la utilidad | `CLAUDE.md` raiz; TM l. 74; 00T §Fuera de alcance 1; C3 l. 36 | si |
| l. 52 | \GAPDEC: por que la coherencia antes de la utilidad | MAPA l. 64; IMP #128.2 | si (GAP justificado) |
| l. 54 | Ninguno de los tres enfoques da a la vez distribucion de poses y apariencia | TM l. 54 (Recognized Gap) | si |
| l. 54 | Peters et al.: colocacion aleatoria en entrenamiento; colocacion manual impracticable | `peters2025hybrid`, "location of the metal objects in the training dataset was randomized", "manual metal placement was impractical" (Discussion, p. 9) | si |
| l. 54 | Peters et al.: conjuntos clinicamente representativos, metal en "meaningful locations", sin regla | `peters2025hybrid`, fila l. 217 (Discussion, p. 9); nota l. 285 | si |
| l. 54 | Liu et al. optimizan una unica trayectoria | TM l. 52; ficha `liu2025pipeline` ("formulated as an optimization problem", Sec. III-D.3, p. 11) | si |
| l. 54 | Zwingmann et al.: distribuciones distintas por tecnica; lectura propia ("este trabajo lee") | C3 l. 79, 200 (69/15/8/8 frente a 40/37/11.5/11.5 %); BITACORA §2 (lectura operativa propia) | si |
| l. 54 | Se preve ejecutar el protocolo de Peters et al. sobre las poses, en un subconjunto y segun el plazo | C3 l. 219 (mismas poses), l. 221 (subconjunto reducido, \GAPDATO no realizado), l. 225; IMP #90 (ABIERTA, act. 2026-09-21) | si (T01 r04 aplicado) |
| l. 54 | \GAPDEC: por que hace falta un sintetizador aprendido | MAPA l. 66; IMP #128.1 | si (GAP justificado) |
| l. 56 | De Man et al.: endurecimiento, dispersion, ruido y EEGE como causas principales; rayas irradiando desde el metal | `deman1999`, "Beam hardening, scatter, noise and EEGE are the most important causes of metal streak artifacts" (Conclusiones, p. 695); "a number of streaks can be seen radiating from the metals" (Sec. III-D, p. 694) | si |
| l. 56 | CLAIM, DiffTumor, LGESynthNet: *inpainting* acotado a la mascara; DiffBoost desde ruido; ninguno con senal fuera de la mascara | TM l. 48; fichas `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`, `zhang2025diffboost` (Alg. 1, p. 3676) | si |
| l. 58 | Geometrias rigidas parametricas como mascara de sintesis, frente a umbral fijo | TM l. 54 (C1); DEC 2026-09-11 (#41); C3 l. 101 | si |
| l. 58 | Xie et al.: el umbral, en cortes simulados, cubrio el implante en exceso | `xie2024implantsegmentation`, ficha l. 29 (Tabla 2, p. 11, datos simulados) | si |
| l. 58 | Tornillos extraidos con umbral fijo aparecen fragmentados en la cohorte local | C3 l. 54 (`sec:datos`); IMP #95 (E8: 10 de 62 objetos alargados partidos) | si |
| l. 58 | Entrenamiento con mascaras umbralizadas; su diferencia con el cilindro es un desplazamiento de dominio | C3 l. 178, 182; IMP #95 (ABIERTA, "sin medir") | si |
| l. 58 | Ningun objetivo aisla el aporte: ningun brazo coloca geometrias extraidas por umbral | C3 l. 219 (tres brazos, mismas poses); C3 `sec:geometria` | si |
| l. 60 | Muestreador comparado con la referencia clinica; codificacion multiventana y banda como tercer elemento | TM l. 54 (C2, C3); C3 l. 79, 176 | si |
| l. 60 | Sin precedente que fije con valor numerico una banda de generacion | GLO l. 39-41; C3 l. 176; TM l. 79 ("No published value calibrates it") | si |
| l. 60 | Varias ventanas de HU vienen de MAR, aplicadas a reconstruccion o perdida, no a la entrada | TM l. 54; GLO l. 29-32 (aviso #24); fichas `wang2025adaptiveweighting` (l. 49), `li2024` (l. 87, 107) | si |
| l. 60 | Ningun objetivo aisla la codificacion ni la banda; el Obj 3 evalua el sintetizador completo | C3 `tab:diseno` fila 3 (VI = brazo); C3 l. 176 (ancho = parametro de diseno); 00T §Fuera de alcance 10 | si |
| l. 62 | Distribucion de poses fijada por escrito en la preinscripcion antes de calcular distancias; ningun parametro de la referencia | C3 l. 127, 158, 253; DEC D-O2.1-D-O2.7 | si |
| l. 62 | Autoencoders preentrenados examinados, incluido uno de TC, sobre rangos que excluyen hueso denso y metal | TM l. 77 ("the pretrained latents available here, including one trained on CT, are defined over intensity ranges that exclude dense bone and metal"); IMP #93 (CERRADA); C3 l. 75 | si |
| l. 62 | El Obj 3 responde sintetizando en el dominio de imagen | TM l. 77, 79; DEC 2026-09-19 (4) | si |
| l. 66 | 178 de los 1 184 volumenes | C3 l. 42 (103 + 75); `docs/02-datos.md`; `liu2021ctpelvic1k`, "including 1, 184 CT volumes" (p. 2) | si |
| l. 66 | Unico implante: tornillo iliosacro parametrico rigido; los reales no aportan geometria | C3 l. 54; DEC 2026-09-11 (#41), 2026-09-20 D3 | si |
| l. 66 | Referencia clinica y marco de Kaiser se refieren a tornillos iliosacros | `zwingmann2009navigated`, "were treated with navigated iliosacral screw placement" (M&M, p. 1834); `kaiser2014dysmorphism`, "for passage of an iliosacral screw" | si |
| l. 66 | \GAPDEC: razon para restringir al tornillo iliosacro | MAPA l. 67; IMP #128.5 | si (GAP justificado) |
| l. 66 | Comparacion solo en S1; segundo corredor de nivel variable, sin distribucion ordinal clinica; eje medido | C3 l. 164 (S2 en 13, S3 en 4, S4 en 1; 69 de 72); TM l. 78; 00T l. 36-38 | si |
| l. 66 | \GAPDATO: muestreo en el segundo corredor | C3 l. 164 (mismo \GAPDATO); MAPA l. 38 | si (GAP justificado) |
| l. 66 | Sintesis en dominio de imagen por parches; fuera de $G$ copia el volumen de origen | TM l. 79; C3 l. 172 | si |
| l. 70 | Dice y HD95 fuera de alcance; 14 de 75 anotados; no verificado localmente; solo parte local | C3 l. 36; 00T §Fuera de alcance 1; `liu2021ctpelvic1k` (ver l. 52) | si |
| l. 71 | Ablaciones a trabajo futuro, para tiempo de compuerta y muestreador | 00T punto 10 ("camino critico (VAE y muestreador)") | si |
| l. 71 | \GAPDEC: que restricciones cubriria la ablacion | C3 l. 158, 166; MAPA l. 65; IMP #128.6 | si (GAP justificado) |
| l. 72 | Validacion de XCIST preliminar y sin estudio de artefacto metalico | `wu2022xcist`, "qualitative and semi-quantitative first-order evaluation" (Validation, p. 9); ficha l. 156, 165 | si |
| l. 72 | Peters et al.: se ejecuta sobre ese simulador, publica metricas, valida contra fantoma fisico | `peters2025hybrid`, "metal artifact simulation capability is experimentally validated in CT phantom scans" (Abstract, p. 1); C3 l. 219 | si |
| l. 73 | Gardner et al.: clasificacion sobre radiografia simple, con rasgos como ala angulada y ascendente o foramenes no circulares, sin exigir todos | `gardner2010safezones`, "evaluated the plain radiographs" (M&M, p. 623, ficha l. 127); "angulated upsloping sacral ala" y "misshapen noncircular-appearing upper sacral neural foramina" (Introduccion, p. 622, filas l. 317-318); "The presence of all six dysmorphism criteria was not required" (M&M, p. 623, fila l. 320) | si (sin recuento de criterios, ficha l. 139-141) |
| l. 73 | Gardner et al.: zona segura de S1 menor en dismorficos; estudio previo sin diferencia | `gardner2010safezones`, "cross-sectional area was 36% smaller in dysmorphic" (p. 624, fila l. 346); "that study found no difference in the safe zone size" (p. 628, fila l. 382); C3 l. 168 | si |
| l. 76 | Supuesto 1: apariencia generable en imagen; De Man: mecanismos no lineales, aislados en el sinograma | TM l. 56; `deman1999`, "Noise artifacts are non-linear artifacts, just like beam hardening and scatter artifacts" (Sec. III-E, p. 694); ficha l. 134-138 | si |
| l. 76 | La comparacion con el protocolo fisico puede contradecirlo, si se mantiene en plazo | C3 l. 225, 261; IMP #90 | si |
| l. 76 | Supuesto 2: serie navegada sin nivel declarado = S1 | C3 l. 259; ficha `zwingmann2009navigated` l. 301; DEC 2026-09-17 C (#69) | si |
| l. 76 | Supuesto 3: relacion mascara-artefacto independiente del tipo; entrenamiento con componentes de todo tipo | C3 l. 180, 261 | si |
| l. 78 | Convencion 1: $B_\delta$ ~12 mm, ninguna fuente lo calibra, trunca rayas lejanas | C3 l. 176, 261; TM l. 79 | si |
| l. 78 | Convencion 2: limites de grado de 2 mm, de tornillos pediculares, via Smith et al.; convencion y supuesto | `gertzbein1990`, Tabla 1 ("0-2 mm / 2.1-4.0 mm", p. 13); `mirza2003` ("The thresholds reported in prior studies were used", p. 405); `smith2006iliosacral` (p. 236); C3 l. 194, 257 | si |
| l. 78 | Convencion 3: grados equiespaciados en W1 | C3 l. 200, 261 | si |
| l. 78 | Convencion 4: margen de 5 mm de Kaiser para la longitud util = dos desviaciones estandar | `kaiser2014dysmorphism`, "no less than 5 mm of distance to the cortex on either side" (p. e120(2)); C3 l. 83, 158, `tab:preinscripcion` | si |
| l. 78 | \GAPDEC: justificacion de $h = 2\sigma$ | C3 l. 158 (mismo \GAPDEC); MAPA l. 48 | si (GAP justificado) |
| l. 80 | Referencia de pelvis fracturadas; receptoras sin osteosintesis, no verificadas libres de fractura | C3 l. 52, 253, 263; IMP #125 | si |
| l. 80 | Malreduccion residual estrecharia corredores; fractura no detectada, por otra causa | C3 l. 253, 263 (`reilly2003effect`, via remision a `sec:amenazas`) | si (T03 r04 no aplicado con motivo) |
| l. 80 | Corredor mas estrecho que el tornillo de medicion: el eje ya perfora, grado 0 inalcanzable; W1 puede moverse sin el muestreador | C3 l. 209 | si |
| l. 80 | Al menos un paciente con fractura confirmada por medico sin especialidad | C3 l. 253; IMP #125 ("medico recien licenciado y sin especialidad") | si |
| l. 80 | \GAPDATO: cribado ciego de 30 casos, preparado y no realizado | C3 l. 52 (15 + 15); IMP #125; MAPA l. 33 | si (GAP justificado) |
| l. 82 | Cifras principales del Obj 2 dependen de una variante condicionada a una revision no hecha | C3 l. 91; IMP #123 (ABIERTA, redactada como GAP) | si |
| l. 82 | \GAPDATO: revision de la autora de 16 casos | C3 l. 91 (mismo \GAPDATO); MAPA l. 32 | si (GAP justificado) |
| l. 82 | Un fallo cambiaria diametros, poses y grados de los casos marcados | IMP #123 (la condicion reabre el recorte principal de toda la cohorte) | parcial (T02) |
| l. 82 | TotalSegmentator no reporta exactitud para la etiqueta de S1; no se asume; un control verifica el nivel | `wasserthal2023`, fila 3e ("Dice por clase: S1 — NO ENCONTRADO EN EL PDF") y 2d; C3 l. 85 ("por lo que esa exactitud no se asume"), l. 52 | si |
| l. 82 | El control excluyo a 11 de 34 con objetos no ortopedicos y a 7 de 57 sin objeto | C3 l. 52 (discordancia de nivel: 11/34 y 7/57; mas 1 por borde); C3 l. 253; IMP l. 4474, 4548-4549; DEC l. 748-749 | parcial (T01) |
| l. 82 | Si el corredor difiriera entre grupos, la distribucion heredaria la composicion | C3 l. 253 | si |
| l. 82 | Envolvente osea: cierre que podria ocupar canal y foramenes; \GAPDATO | C3 l. 87, 257 (mismo \GAPDATO); MAPA l. 57 | si (GAP justificado) |
| l. 84 | Reconstruccion no reportada; MAR del fabricante o monoenergetica cambian la apariencia | C3 l. 44; `selles2024marreview` (ficha l. 9, 42; "varies by vendor", Sec. 3.5, p. 6) | si |
| l. 84 | Protocolo fisico validado en 2D y para MAR, sin cubrir el paso hibrido; la adaptacion no hereda la validacion | C3 l. 221, 263; ficha `peters2025hybrid` l. 102, 458, 470 (4l: validacion de imagenes hibridas NO ENCONTRADO EN EL PDF) | si |
| l. 84 | Tres desplazamientos de dominio que limitan la transferencia; solo el tercero cuantificado | C3 l. 182 (0.62 frente a 1.40), l. 263; IMP #95, #96 (ABIERTAS); capitulo3-r05-respuesta guia-3 (TM l. 79 dice "first and third are quantified"; la discrepancia ya se resolvio en C3 con DEC R3) | si |
| l. 84 | \GAPDEC: metrica de los dos primeros desplazamientos | C3 l. 182 (mismo \GAPDEC); MAPA l. 59 | si (GAP justificado) |
| l. 84 | $B_\delta$ trunca las rayas y el protocolo fisico no; la comparacion no puede mostrar las rayas lejanas | C3 l. 261 | si |
| l. 84 | \GAPDATO: el sintetizador no genero ninguna muestra | C3 l. 38; IMP #116; MAPA l. 30 | si (GAP justificado) |
| l. 84 | \GAPDEC: equivalencia frente al protocolo fisico, contingencia de plazo | C3 l. 225; IMP #90; MAPA l. 44 | si (GAP justificado) |
| l. 37-84 | Claves citadas existen en `overleaf/referencias.bib`; apellidos nombrados = primer autor (Kaiser, Zwingmann, Peters, Liu [liu2021ctpelvic1k, liu2025pipeline], De Man, Xie, Gardner, Smith) | `overleaf/referencias.bib` l. 88, 117, 229, 262, 400, 434, 498, 518, 540, 626, 705, 738, 773, 847, 868, 1040, 1051, 1073, 1093, 1179, 1265 | si |
| l. 23-84 | Ninguna cita como sujeto gramatical sola (E-F3) | revision del texto (l. 37, 56, 60, 72, 82 y 84 van con \cite al final de la clausula) | si |
| l. 23-84 | Sin fuentes de fabricante citadas (P-EA1) | revision del texto | si (no aplica) |
| l. 23-84 | Sin contenido retirado presentado como vigente (downstream como objetivo, difusion latente o ControlNet, "31-60 %", BFC/ISC) | 00T §Fuera de alcance 1, 2, 5; `CLAUDE.md` raiz. Latente y ControlNet solo en l. 37, 46 y 62, como compuerta e historia; Dice y HD95 solo en l. 70, como exclusion | si |
| l. 23-84 | Patrones VIGENTES de dominio G-T4/E-R6 (PAT-31, 38, 39, 49, 51, 54, 55, 57) | PAT-31: sin reincidencia en los agregados de r04 (T01 es imprecision heredada de C3 l. 253, no perdida de condicion en un resumen); PAT-38 (l. 80, 82), PAT-39 (l. 82, "cifras principales"), PAT-49 (l. 58, 60), PAT-51 (l. 72), PAT-54 (l. 76-80), PAT-55 (l. 54), PAT-57 (l. 41) sin reincidencia | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Se copia de la fuente la formulacion menos precisa cuando la misma fuente trae una mas precisa en otro lugar | G-T4 | "El control de nivel excluyó a ... 7 de 57" (C3 l. 253 frente a l. 52) | nuevo |
| La consecuencia de una condicion de reapertura se acota a los casos revisados, no a la decision que reabre | G-T4, E-R6 | "cambiarían sus diámetros de corredor" (la condicion reabre el recorte de toda la cohorte) | nuevo |
