# Auditoria de trazabilidad — introduccion — r03

Alcance acotado por pedido de la autora: l. 23-80 (Objetivos de investigacion, Justificacion, Alcance
y limitaciones / restricciones). El encabezado y la Formulacion del problema (l. 1-21) no se auditan
porque estan DESFASADOS (#126).
Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`; IMP = `docs/04-implicancias.md`; GLO =
`docs/03-glosario.md`.

Respuesta r02 considerada. T01 a T04 estan APLICADOS y verificados en el texto actual (ver inventario).
T05 quedo NO APLICADO con motivo: la oracion sin cita coincide con TM l. 46, y la ficha no alcanza para
decidir. No se re-reporta, porque no hay argumento nuevo. El lint r03 no marca nada dentro del alcance.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | baja | G-T4, OC-2 | l. 46 | "El error de ida y vuelta ... queda pendiente en el diseño del sintetizador" | C3 l. 172 (\GAPDEC "congelar la preinscripción del diseño del sintetizador: ... su error de ida y vuelta sin autoencoder ..."); BITACORA §2, decision 2026-09-30 ("Si la introduccion resume un tramo que el cap. 3 marca con GAP, lleva el mismo GAP") | El contenido es correcto y dice con claridad que el error esta pendiente. Pero C3 marca este mismo tramo con \GAPDEC, y la introduccion lo resume sin la marca. Eso incumple la decision del ciclo que se aplico en r02 al segundo corredor, a $h = 2\sigma$ y a la inversion de las metricas. Como el pendiente no queda visible en el PDF como GAP, tampoco entra en el recuento del lint. | "... no lo verifica ningún objetivo \GAPDEC{error de ida y vuelta de la codificación multiventana sin autoencoder, pendiente de la preinscripción del sintetizador} (Sección~\ref{sec:sintetizador})." |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 28 | Los cuatro objetivos son los del cap. 3; solo Obj 2 y 3 son componentes de la cadena | C3 §Vision general y fig. 1; C3 l. 185; MAPA l. 47 | si |
| l. 28 | Obj 1 es una prueba previa a la cadena; Obj 4 define o adopta las metricas | BITACORA §2 (introduccion-r01); C3 l. 58 ("previa al Objetivo 3"), l. 185 | si |
| l. 28 | \GAPDEC: la pregunta aun promete 2D, Dice, HD95 y aumento convencional | IMP #126 (ABIERTA); introduccion l. 21; MAPA l. 63 | si (GAP justificado) |
| l. 32 | Cadena de difusion en dominio de imagen; implantes y artefacto local; coherencia fisica y quirurgica | TM l. 74; 00T titulo; DEC 2026-09-19 | si |
| l. 32 | Osteosintesis = dispositivos de fijacion osea, como tornillos y placas | `CLAUDE.md` raiz ("implantes de osteosintesis (tornillos, placas)") | si |
| l. 32 | Corredor oseo medido en cada volumen; glosa sin atravesar la cortical | TM l. 52; GLO l. 52-53 | si |
| l. 32 | Codificacion multiventana: varios canales, cada uno con una ventana de HU | TM l. 79; C3 l. 60; 00T l. 68 | si |
| l. 32 | Utilidad para segmentacion = trabajo futuro | 00T §Fuera de alcance 1; TM l. 83 | si |
| l. 37 | Titulo: el autoencoder de un modelo de difusion latente conserva los HU de la codificacion | TM Obj 1 ("HU to multi-window to VAE to HU"); C3 l. 58; BITACORA §2 (2026-09-30) | si |
| l. 37 | MAE < 25 HU en hueso | TM l. 77; 00T l. 23; DEC 2026-09-15 (2); C3 tab:diseno fila 1 | si |
| l. 37 | El autoencoder comprime a un latente donde opera la difusion | `rombach2022latentdiffusion`, "we apply them in the latent space of powerful pretrained autoencoders" (Abstract, p. 1) | si |
| l. 37 | 34 pacientes de prueba | TM l. 77 ("34 held-out patients"); C3 l. 50, tab:diseno | si |
| l. 39 | Tornillo iliosacro (une ilion y sacro), parametrico y rigido | TM l. 78; DEC 2026-09-11 (#41); GLO l. 74-75 (iliosacro no cruza ambas articulaciones) | si |
| l. 39 | Poses en el marco de Kaiser et al.; viabilidad = calibre + holgura radial de Kaiser | DEC 2026-09-08; C3 l. 89, l. 189; BITACORA §2 (introduccion-r01) | si |
| l. 39 | Grado de brecha cortical, escala ordinal de cuatro niveles | TM l. 52; C3 l. 189, l. 194; GLO l. 45-48 | si |
| l. 39 | Referencia clinica = series navegada y convencional de Zwingmann et al., en S1 | TM l. 52; C3 l. 200; 00T l. 35-36 | si |
| l. 39 | S1 = primer segmento del sacro | `kaiser2014dysmorphism`, "first sacral segment" (Fig. 1, p. e120(3)) | si |
| l. 39 | Sin ajustar el muestreador a la referencia | DEC D-O2.1; C3 l. 158, l. 207 | si |
| l. 39 | Wasserstein-1 = suma de diferencias absolutas de las acumuladas | C3 ec. `eq:w1` (l. 200-205) | si |
| l. 41 | *Inpainting* 2.5D en dominio de imagen, sin latente ni proyeccion; 2.5D se remite al marco teorico | TM l. 79; C3 l. 172; BITACORA §2 (glosas) | si |
| l. 41 | $G = M \cup B_\delta$; $B_\delta$ de unos 12 mm; rayas y endurecimiento fuera del metal | TM l. 79; C3 l. 176; GLO l. 36-41 | si |
| l. 41 | Comparacion con copia y pegado (sin artefacto) y protocolo fisico de Peters et al. | C3 l. 185, l. 219 | si |
| l. 43 | SAP, unica metrica introducida; incluye W1; comparacion en Obj 2 | 00T §Fuera de alcance 2; TM l. 80; BITACORA §2 (introduccion-r01) | si |
| l. 43 | *bone integrity*, *metal integrity*, *streak amplitude*, nombres publicados | ficha `peters2025hybrid` l. 358; C3 l. 213; overleaf/CLAUDE.md terminos fijos | si |
| l. 43 | Metricas disenadas para MAR; invertirlas; \GAPDEC de la inversion | C3 l. 215 (mismo \GAPDEC); IMP #17; MAPA l. 42 | si (GAP justificado) |
| l. 46 | Compuerta formulada para difusion latente con ControlNet; veredicto negativo; Obj 3 reformulado despues; regla no modificada | C3 l. 38, l. 174, l. 255; DEC 2026-09-19 | si (historico, no vigente) |
| l. 46 | El veredicto descarto la ruta latente, no la codificacion multiventana, que el sintetizador sigue usando | TM Obj 1 ("the latent route is abandoned"); C3 l. 172 ("usan la codificación multiventana ... sin la etapa de compresión del autoencoder") | si |
| l. 46 | Error de ida y vuelta sin autoencoder no verificado; pendiente en el sintetizador | C3 l. 172 (\GAPDEC) | parcial (T01: falta la marca) |
| l. 48 | Obj 1 a 3 con variable dependiente; Obj 4 sin variable dependiente propia | C3 l. 185, tab:diseno | si |
| l. 48 | 25 HU anterior a la exploracion; regla operativa despues de ella y antes de la prueba que decide | C3 l. 58, l. 255; DEC 2026-09-15 (2), 2026-09-17 (3); IMP #127.4 | si |
| l. 48 | \GAPDEC: distancia W1 que contaria como fallo | C3 l. 207; IMP #127.6; MAPA l. 50 | si (GAP justificado) |
| l. 48 | Superioridad frente a copia y pegado sobre *streak amplitude*, que esa insercion no produce; no dice si las rayas se parecen a las reales | C3 l. 217 | si |
| l. 48 | \GAPDEC: que haria fallar el Obj 3 | C3 l. 217; IMP #127.3; MAPA l. 55 | si (GAP justificado) |
| l. 48 | Obj 4 comprobado con controles de consistencia; \GAPDEC sobre su evidencia | C3 l. 185, l. 198; MAPA l. 49 | si (GAP justificado) |
| l. 52 | Segmentacion depende de datos anotados; artefactos ocultan limites | TM l. 46 (sin cita) | si (T05 r02 no aplicado con motivo; no se re-reporta) |
| l. 52 | CTPelvic1K anota el hueso en 14 de 75 volumenes con metal; 61 sin anotar | `liu2021ctpelvic1k`, "and 14 metal-affected CTs", "including 75 CTs with metal artifacts", "The remaining 61 metal-affected CTs are left unannotated" (p. 2-3) | si |
| l. 52 | Motivacion de fondo: aumento de datos; las condiciones de los datos impiden medir la utilidad | `CLAUDE.md` raiz; TM l. 74, l. 83; 00T §Fuera de alcance 1 | si |
| l. 52 | \GAPDEC: por que la coherencia antes de la utilidad | TM y 00T no dan el eslabon; MAPA l. 64 | si (GAP justificado) |
| l. 54 | Ninguno de los tres enfoques da a la vez distribucion de poses y apariencia | TM l. 54 (Recognized Gap) | si |
| l. 54 | Peters et al.: colocacion aleatoria en entrenamiento; colocacion manual impracticable | `peters2025hybrid`, "location of the metal objects in the training dataset was randomized", "manual metal placement was impractical" (Discussion, p. 9) | si |
| l. 54 | Peters et al.: conjuntos clinicamente representativos, metal en "meaningful locations", sin regla | `peters2025hybrid`, fila l. 217 (Discussion, p. 9); nota l. 285 | si (T03 r02 aplicado) |
| l. 54 | Liu et al. optimizan una unica trayectoria | TM l. 52; ficha `liu2025pipeline` ("formulated as an optimization problem", Sec. III-D.3, p. 11) | si |
| l. 54 | Zwingmann et al.: distribuciones de malposicion distintas por tecnica; lectura propia | C3 l. 200 (69/15/8/8 frente a 40/37/11.5/11.5 %); BITACORA §2 (lectura operativa propia) | si |
| l. 56 | De Man et al.: rayas por endurecimiento, dispersion, ruido y EEGE; irradian desde el metal | `deman1999`, "Beam hardening, scatter, noise and EEGE are the most important causes" (p. 695); "streaks can be seen radiating from the metals" (Sec. III-D, p. 694) | si |
| l. 56 | CLAIM, DiffTumor, LGESynthNet: *inpainting* acotado a la mascara; DiffBoost desde ruido; ninguno con senal fuera de la mascara | TM l. 48; fichas `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`, `zhang2025diffboost` (Alg. 1, p. 3676) | si |
| l. 58 | Geometrias rigidas parametricas frente a umbral fijo | TM l. 54 (C1); DEC 2026-09-11 (#41) | si |
| l. 58 | Xie et al.: el umbral, en cortes simulados, cubrio el implante en exceso | `xie2024implantsegmentation`, ficha l. 29 (Tabla 2, p. 11, datos simulados); TM C1 ("over-coverage in simulated slices") | si (T02 r02 aplicado) |
| l. 58 | Tornillos extraidos con umbral fijo aparecen fragmentados en la cohorte local | C3 l. 54 (sec:datos); TM ("fragmentation of pelvic screws") | si |
| l. 58 | Muestreador comparado con la referencia clinica | TM l. 54 (C2) | si |
| l. 58 | Marco multiventana de MAR, aplicado a reconstruccion o perdida, no a la entrada | TM l. 54; GLO l. 29-32 (aviso #24); fichas `wang2025adaptiveweighting` (l. 49), `li2024` (l. 87, 107) | si (T01 r02 aplicado) |
| l. 58 | Ningun objetivo aisla el aporte de la codificacion; Obj 3 evalua el sintetizador completo | C3 tab:diseno fila 3 (VI = brazo); 00T §Fuera de alcance 10 | si |
| l. 58 | Sin precedente que fije con valor numerico una banda de generacion | GLO l. 39-41; C3 l. 176 | si |
| l. 60 | Distribucion de poses fijada por escrito antes de calcular distancias; ningun parametro de la referencia | C3 l. 158, l. 253; DEC D-O2.1-D-O2.7 | si |
| l. 60 | Latentes preentrenados examinados, incluido uno de TC, excluyen hueso denso y metal; el veredicto no se limita a una arquitectura | TM l. 77 ("generalizes the outcome ..."); 00T l. 26-27 (#93); C3 l. 255 (latente de Guo et al.) | si |
| l. 64 | 178 de los 1 184 volumenes | C3 l. 42 (103 + 75); `docs/02-datos.md`; `liu2021ctpelvic1k`, "including 1, 184 CT volumes" (p. 2) | si |
| l. 64 | Unico implante: tornillo iliosacro parametrico rigido; los reales no aportan geometria | C3 l. 54; DEC 2026-09-11 (#41), 2026-09-20 D3 | si |
| l. 64 | Comparacion solo en S1; segundo corredor sin distribucion ordinal clinica; eje medido | C3 l. 164; 00T l. 36-38; MAPA l. 38 (69 de 72) | si |
| l. 64 | \GAPDATO: muestreo en el segundo corredor | C3 l. 164 (mismo \GAPDATO); `preinscripcion_muestreador.md` §7 | si (GAP justificado; T04 r02 aplicado) |
| l. 64 | Sintesis por parches, en dominio de imagen | TM l. 79; 00T l. 64-66; C3 l. 172 | si |
| l. 68 | Dice y HD95 fuera de alcance; 14 de 75 anotados; no verificado localmente; solo parte local | C3 l. 36; 00T §Fuera de alcance 1; `liu2021ctpelvic1k` (ver l. 52) | si |
| l. 69 | Ablaciones a trabajo futuro, para tiempo de compuerta y muestreador | 00T l. 124-126 (punto 10, "camino critico (VAE y muestreador)") | si |
| l. 69 | \GAPDEC: que restricciones cubriria la ablacion; muestreador perturba el eje y no condiciona por densidad | C3 l. 158, l. 166; 00T punto 10 no las enumera; MAPA l. 65 | si (GAP justificado) |
| l. 70 | Validacion de XCIST preliminar y sin estudio de artefacto metalico | `wu2022xcist`, "qualitative and semi-quantitative first-order evaluation" (Validation, p. 9); ficha l. 156, 165 (metrica de metal NO ENCONTRADO) | si |
| l. 70 | Peters et al. validan su simulacion de artefactos metalicos contra un fantoma fisico, en 2D y para MAR | `peters2025hybrid`, "metal artifact simulation capability is experimentally validated in CT phantom scans" (Abstract, p. 1); "all datasets are simulated in 2D" (Abstract, p. 1); C3 l. 221 | si |
| l. 71 | Gardner et al.: zona segura de S1 menor en dismorficos; estudio previo sin diferencia | `gardner2010safezones`, "cross-sectional area was 36% smaller in dysmorphic" (p. 624); "that study found no difference in the safe zone size" (p. 628); C3 l. 168 | si |
| l. 74 | Supuesto 1: apariencia generable en imagen; De Man: mecanismos no lineales, aislados en el sinograma | TM l. 56; `deman1999`, "Noise artifacts are non-linear artifacts, just like beam hardening and scatter artifacts" (Sec. III-E, p. 694); ficha l. 134-138 | si |
| l. 74 | La comparacion con el protocolo fisico puede contradecirlo | C3 l. 261 | si |
| l. 74 | Supuesto 2: serie navegada sin nivel declarado = S1 | C3 l. 259; DEC 2026-09-17 C (#69) | si |
| l. 74 | Supuesto 3: relacion mascara-artefacto independiente del tipo; entrenamiento con componentes de todo tipo | C3 l. 180, l. 261 | si |
| l. 76 | Convencion 1: $B_\delta$ ~12 mm, ninguna fuente lo calibra, trunca rayas lejanas | C3 l. 176, l. 261; GLO l. 40-41 | si |
| l. 76 | Convencion 2: cortes de 2 mm de tornillos pediculares, via Smith et al.; convencion y supuesto | `gertzbein1990`, Tabla 1 (tramos "0-2 mm / 2.1-4.0 mm", p. 13); `mirza2003` ("The thresholds reported in prior studies were used", p. 405); `smith2006iliosacral` (p. 236); C3 l. 257 | si |
| l. 76 | Convencion 3: grados equiespaciados en W1 | C3 l. 200, l. 261 | si |
| l. 76 | Convencion 4: margen de 5 mm de Kaiser para la longitud util = dos desviaciones estandar | `kaiser2014dysmorphism`, "no less than 5 mm of distance to the cortex on either side" (p. e120(2)); C3 l. 148, l. 158 | si |
| l. 76 | \GAPDEC: justificacion de $h = 2\sigma$ | C3 l. 158 (mismo \GAPDEC); MAPA l. 48 | si (GAP justificado) |
| l. 78 | Referencia de pelvis fracturadas; receptoras sin osteosintesis, no verificadas libres de fractura | C3 l. 52, l. 263; IMP #125 | si |
| l. 78 | Malreduccion estrecharia corredores; fractura no detectada por otra causa | C3 l. 253, l. 263 | si |
| l. 78 | Al menos un paciente con fractura confirmada por medico sin especialidad | C3 l. 253; IMP #125 | si |
| l. 78 | \GAPDATO: cribado ciego de 30 casos, preparado y no realizado | C3 l. 52 (15 + 15); IMP #125; MAPA l. 33 | si (GAP justificado) |
| l. 78 | Cifras principales del Obj 2 dependen de una variante condicionada a una revision no hecha | IMP #123 l. 8578-8582 (ABIERTA, formulada como GAP) | si |
| l. 78 | \GAPDATO: revision de la autora de 16 casos (diferencia de diametro o caja desplazada) | IMP #123 l. 8574, 8586-8587, 8626-8627 (autora 0/16); MAPA l. 32 | si (GAP justificado) |
| l. 78 | Efecto condicional: cambiarian diametros, poses y grados de los casos marcados | IMP #123 l. 8578-8580, 8588 ("El efecto por caso puede ser grande"); l. 8589 (no se concluye que esten mal) | si |
| l. 80 | Reconstruccion no reportada; MAR del fabricante o monoenergetica cambian la apariencia | C3 l. 44; `selles2024marreview` (ficha l. 9, 42; "varies by vendor", Sec. 3.5, p. 6) | si |
| l. 80 | Protocolo fisico validado en 2D y para MAR; la adaptacion no hereda la validacion | C3 l. 221, l. 263; ficha `peters2025hybrid` l. 101, 211 | si |
| l. 80 | \GAPDATO: el sintetizador no genero ninguna muestra | C3 l. 38; IMP #116; MAPA l. 30 | si (GAP justificado) |
| l. 80 | \GAPDEC: equivalencia frente al protocolo fisico, contingencia de plazo | C3 l. 225; IMP #90; MAPA l. 44 | si (GAP justificado) |
| l. 37-80 | Claves citadas existen en `overleaf/referencias.bib`; apellidos nombrados = primer autor (Kaiser, Zwingmann, Peters, Liu, De Man, Xie, Gardner, Smith) | `overleaf/referencias.bib` l. 88, 117, 229, 262, 400, 434, 498, 518, 540, 626, 705, 738, 773, 847, 868, 1040, 1073, 1093, 1179, 1265 | si |
| l. 23-80 | Ninguna cita como sujeto gramatical sola (E-F3) | revision del texto | si |
| l. 23-80 | Sin fuentes de fabricante citadas (P-EA1) | revision del texto | si (no aplica) |
| l. 23-80 | Sin contenido retirado presentado como vigente (downstream como objetivo, difusion latente o ControlNet, "31-60 %", BFC/ISC) | 00T §Fuera de alcance 1, 2, 5; `CLAUDE.md` raiz. ControlNet y latente solo en l. 37, 46, 60, como compuerta e historia; Dice y HD95 solo en l. 68, como exclusion | si |
| l. 23-80 | Patrones VIGENTES de dominio G-T4/E-R6 (PAT-6, 12, 13, 31, 36, 48, 49, 51, 53) | revision del texto: solo PAT-31, en forma leve (T01); PAT-12 en l. 52 ya decidido (T05 r02) | si, salvo T01 |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Al resumir en la introduccion un tramo que el cap. 3 marca con GAP, se dice que falta pero sin la marca | G-T4, OC-2 | "queda pendiente en el diseño del sintetizador (Sección~\ref{sec:sintetizador})" | PAT-31 |
