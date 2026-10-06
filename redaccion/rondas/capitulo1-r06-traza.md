# Auditoria de trazabilidad — capitulo1 — r06

Archivo: `overleaf/secciones/capitulo1.tex` (131 lineas). Lint r06: PASA (0/0/0; GAP lit 4 / dato 1 / dec 8;
recuento propio sobre el `.tex`: `\GAPLIT` en :35, :72, :120, :126; `\GAPDATO` en :46; `\GAPDEC` en :46, :72,
:84, :88, :112, :114, :118, :124 — coincide).
Respuesta previa: `capitulo1-r05-respuesta.md` (7 medios aplicados, 0 rechazados). **No hay RECHAZADOS que
respetar**, asi que ningun hallazgo de aqui es re-apertura.

`redaccion/rondas/paridad-r01-trazabilidad.md` se da por buena. De este capitulo cubrio **M-02**: el
`\GAPDEC` de `:72` y la lista de menciones que deben seguir diciendo "iliosacro" (`:72`, `:82` por
`smith2006iliosacral`). El hallazgo M-03 de abajo es el **mismo defecto visto por linea**, con la parte del
`\GAPDEC` que #130 **no** resuelve aislada; no lo cuento como hallazgo nuevo de paridad.

**Reutilizacion declarada:** la auditoria r05 cerro con alta=0 media=0 baja=1 y un inventario de 74 filas
verificadas. r05-respuesta solo toco l.35 (ultima oracion), l.44, l.46, l.54 (apertura), l.64, l.78, l.88,
l.120-l.128 y la figura. Las filas del inventario cuyo texto **no** cambio se marcan `(verif. r05)` y no se
volvieron a rastrear; todo lo demas se rastreo de nuevo contra su fuente, mas los dos hechos nuevos (#130
decidida, #141 ABIERTA) y la comprobacion completa de los 13 GAP.

**Conteo: alta=1 media=6 baja=1**

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | **alta** | G-T4, OC-1 | l.44, primera oracion (y su aplicacion en l.46) | "usa varias ventanas a la vez ... evita así elegir entre conservar el rango" | #141 ABIERTA (`04-implicancias.md`:9707-9737); `src/common/ventanas.py`:44; `experiments/objetivo1/e6c_techo_lw.py`:66, :81 | Afirmacion propia **sin cita** que el propio repositorio desmiente para el extremo inferior: las **nueve** configuraciones candidatas comparten `low = -1000.0` y la `ida` aplica `np.clip`, de modo que la ida y vuelta **sin modelo** sobre un corte real con metal devuelve el minimo al suelo. La codificacion no "evita elegir": resuelve el canje descartando el rango negativo, que es donde se manifiesta la inanicion de fotones que define l.56. l.42 declara la saturacion solo de forma generica y l.46 da el intervalo `[-1000, 20000]` sin decir que ese suelo es comun a las tres codificaciones | Quitar "evita así elegir entre conservar el rango y separar los contrastes" y decir lo que la codificacion hace: usa una ventana por canal para separar contrastes sin perder el **techo** del metal. Anadir que las tres codificaciones del Objetivo~1 comparten el suelo de $-1000$~HU y que ese suelo satura los valores de TC mas bajos del artefacto, y cerrar con `\GAPDEC{si el suelo de $-1000$~HU de la representación multiventana se declara como limitación de alcance o si se cambia la representación}`, **sin ninguna cifra de #141** (ABIERTA), igual que ya se hizo en `capitulo3` §Sintetizador (`MAPA.md`:38) |
| T02 | media | OC-2, G-T4 | l.56 (definicion) y l.62 (las dos consecuencias) | "La inanición de fotones aparece cuando un rayo atraviesa tanto metal..." | #141 ABIERTA, seccion "Por que importa"; l.114 como contraste interno | El capitulo define las tres manifestaciones del artefacto y deriva en l.62 "dos consecuencias para la síntesis", y **para el volumen parcial no lineal si declara el limite** ("no contiene entonces ese mecanismo", l.114). Para la inanicion de fotones no declara nada, aunque hoy consta que la representacion no puede llevarla. La implicancia ABIERTA que pide declarar esa ausencia no deja marca en la seccion que la sufre | Una oracion al cierre de l.56 o de l.62, en prosa y con remision a §Sintetizador y §Amenazas: la representacion que adopta el sintetizador satura por abajo, asi que la inanicion de fotones queda fuera de lo que puede expresar; remitir al `\GAPDEC` de T01 sin duplicarlo (decision de BITACORA §2 2026-10-03 sobre procedimientos con `\GAPDEC` en el cap. 3) |
| T03 | media | OC-2, G-T4 | l.72, `\GAPDEC` y oracion previa ("La Sección~\ref{sec:sap}, sin embargo, ...") | `\GAPDEC{qué tornillo representa el corredor que mide este trabajo ...}` | #130, decision de la autora 2026-10-04 (`04-implicancias.md`:8893-8918), aplicada a `main.tex`:117 | GAP injustificado en **dos de sus tres partes**. #130.1 nombra la geometria **tornillo transiliaco-transsacro (transiliosacro)** y #130.3 fija que `zwingmann2009navigated` es referencia clinica de **distribuciones**, no de equivalencia geometrica. Sigue abierta **solo** la tercera: #130.2 declara aplicables las tolerancias de `mclaren2021corridor` y **no dice nada del umbral de 10~mm ni de la holgura radial de Kaiser et al.**, definidos para el iliosacro. Ademas el "sin embargo" presenta como contradiccion con §SAP lo que #130 ya resolvio | Escribir el hecho con la forma fija de BITACORA §2 2026-10-05 ("tornillo transilíaco-transsacro (transiliosacro)" en la primera aparicion, con tilde) y la clausula de #130.3 sobre Zwingmann et al.; quitar el "sin embargo"; **conservar** "iliosacro" en las dos menciones de `smith2006iliosacral` (:72, :82) y en Kaiser et al. y su umbral. Dejar el `\GAPDEC` reducido a: si el umbral de 10~mm y la holgura radial de Kaiser et al., definidos para el tornillo iliosacro, aplican a un corredor transiliosacro |
| T04 | media | OC-2, G-T4 | l.46 (`\GAPDEC` de la codificacion) y l.114 (`\GAPDEC` de 2.5D) | "la variante que adopta no se ha fijado"; "que solo propone el borrador de su diseño" | `src/common/ventanas.py`:44 (`CONFIG_DISENO_A = 'pub+asinh'`); `src/renderizador/datos.py`:19, :72 ("Se piden 3 cortes contiguos y se genera el central") | Patron PAT-19 reincide y PAT-122 reincide: dos GAP envejecidos. El entrenamiento que ya corrio (#133, #139, ABIERTAS) **fija** las dos cosas en el codigo; lo que falta es preinscribirlas, no decidirlas desde cero. Es el defecto dominante del cap. 3 en r06, aqui dos veces | Mismo criterio que la decision de BITACORA §2 2026-10-03: el GAP dice que el valor **solo consta en el codigo del entrenamiento y no en un registro**. l.46: "qué codificación multiventana y qué precisión numérica preinscribe el sintetizador; el código del entrenamiento usa la compresión arcoseno hiperbólico y no hay registro que la congele". l.114: "número de cortes contiguos ..., tres en el código del entrenamiento y en el borrador de diseño, sin preinscripción". **Sin citar cifras de #133 ni de #139** |
| T05 | media | G-T4, E-R6 | l.104 y l.106 | "arquitectura que aún no se ha fijado"; "no menciona el calendario de ruido; ambos quedan pendientes" | `src/renderizador/modelo.py`:78-85; `src/renderizador/difusion.py`:5, :11, :29-30; `experiments/objetivo3/diseno_A.md`:67-71 | Misma familia que T04, en prosa. El borrador si propone U-Net y DDIM (`diseno_A.md`:69, :71) y el codigo del entrenamiento la implementa con 4 escalas, y **fija el calendario que el borrador no menciona**: coseno de Nichol y Dhariwal, 1000 pasos, muestreo DDIM determinista de 50 pasos. La frase deja al lector creer que no existe ninguna eleccion | "El código del entrenamiento usa una U-Net y el calendario coseno de Nichol y Dhariwal, que el borrador no menciona; ninguno de los dos está preinscrito (Sección~\ref{sec:sintetizador})". No se cita el resultado de ninguna corrida |
| T06 | media | E-R6, G-T4 | l.62, segunda oracion | "las fuentes revisadas no dan hasta dónde llegan las rayas" | `docs/literatura/radzi2014metalartifacts.md`:22-23, :39-40, :89, :92; `_index.md` (fila de `radzi2014metalartifacts`) | Negativo universal sobre "las fuentes revisadas" que una fuente revisada, con entrada en `referencias.bib` y ficha completa, contradice: publica el artefacto en CT en 2.0 / 2.6 / 1.6 / 2.0~mm. Patron PAT-39 y PAT-64 reinciden. La formulacion correcta ya existe en el documento: `introduccion.tex`:80 dice "ninguna fuente revisada **calibra** el ancho" | Usar la formulacion de la introduccion y, si se quiere el hecho, darlo con su condicion segun la ficha: la unica fuente revisada con una distancia en CT la mide **desde el eje del tornillo**, sobre el tobillo de **un** cadaver y con umbral no publicado, de modo que no calibra el ancho de $B_{\delta}$ |
| T07 | media | OC-3, G-T4 | l.80, ultima oracion | "Este trabajo expresa sus poses en ese marco" | #138 ABIERTA (`04-implicancias.md`:9535-9544); `capitulo3.tex`:269 | Implicancia ABIERTA afirmada como resuelta. #138 dice que el techo de la etiqueta `vertebrae_S1` puede estar en la **cresta sacra media** y que "el techo de S1 según la máscara" y "el platillo superior de S1" **no son la misma superficie**; literal: "Eso no esta medido". El capitulo afirma identidad con el marco de Kaiser et al. y reduce lo pendiente a si los puntos "se pueden localizar en volúmenes con metal", que es otra pregunta. `capitulo3.tex`:269 ya lleva el `\GAPDATO` correspondiente | Prosa, sin duplicar el `\GAPDATO` (BITACORA §2 2026-10-03): "Este trabajo ancla ese marco al techo de la etiqueta de S1, que puede no ser el platillo superior, y la Sección~\ref{sec:amenazas} declara esa diferencia como no medida". Mantener la oracion sobre la localizacion con metal, que es un segundo limite |
| T08 | baja | G-T4 | l.31, primera oracion | "Cada lectura del detector corresponde a un rayo de una vista" | `deman2007catsim.md`:79-83 y :152 | La ficha acredita "y_i is the detector signal at sinogram index i" y el indice de submuestreo del haz, pero **no** la nocion de "vista": su propia tabla registra "Numero de vistas por rotacion: NO ENCONTRADO EN EL PDF". El resto de la oracion (lecturas ordenadas por indice = sinograma) si esta | "Cada lectura del detector es la señal en un índice del sinograma, y el conjunto de esas lecturas forma el **sinograma**", que es la frase de la ficha |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.11 | Funcion del capitulo y reparto con los caps. 2 y 3 | estructura propia; `\ref` resueltas (lint PASA) | si (verif. r05) |
| l.13 | Orden de las secciones; el muestreador precede al sintetizador | `capitulo3.tex`:21-33 (`fig:pipeline`) | si (verif. r05) |
| l.13 | Pieza de la propuesta que usa cada seccion | `capitulo3.tex`:13, 20-31, 69, 79, 172, 189 | si (verif. r05) |
| fig. 1.1 | Conceptos -> Obj 1, 2, 3, 4 y protocolo fisico | `capitulo3.tex`:13, 20-31, 172, 189, 213, 219; `introduccion.tex`:43 | si (verif. r05) |
| l.31 | Lectura del detector = indice del sinograma; "rayo de una vista" | `deman2007catsim.md`:79-83; :152 (vistas NO ENCONTRADO) | **parcial (T08)** |
| l.31 | Senal = suma sobre energias de los fotones sin objeto, atenuados por longitud y material | `deman2007catsim.md`:78, :81-83 (Sec. 2.1, p. 1) | si |
| l.31 | Coeficiente de atenuacion lineal por material y energia | `deman2007catsim.md`:83 | si |
| l.31 | Abadi et al. (DukeSim): Beer-Lambert | `abadi2019.md`:1, :51 ("computed using the Beer-Lambert Law", Sec. II-B, p. 1458) | si |
| l.31 | Wang et al. (cocleares): Beer-Lambert discretizada en cinco energias | `wang2019cochlear.md`:52, :56 ("discretized on 5 different energies") | si |
| l.33 | FBP en De Man 1999, en CatSim y en Karageorgos et al. | `deman1999.md`:187 (Herman, Sec. II-C); `deman2007catsim.md`:114 (Sec. 3.1); `karageorgos2024ddpm` Sec. II-F | si (verif. r05) |
| l.33 | Park et al.: FBP supone el modelo monocromatico de Radon; el haz policromatico se aparta de forma no lineal | `park2015ct.md`:9 | si |
| l.33 | Dominio de proyeccion / dominio de imagen; cohorte solo reconstruida; protocolo fisico por proyecciones | `capitulo3.tex`:42-46, 172, 219-221, 261; `docs/02-datos.md`; BITACORA §2 2026-09-29 ("dominio de imagen") | si (verif. r05) |
| l.35 | Agua 0~HU y aire $-1000$~HU por definicion | `wu2022xcist.md`:105-106 ("defined as 0 HU"; "-1000 HU by definition") | si |
| l.35 | Conversion coeficiente-HU apoyada en el coeficiente del agua por energia | `wang2019cochlear.md`:70 (Sec. 2.1, p. 4) | si |
| l.35 | `\GAPLIT` fisica de TC (Beer-Lambert, escala Hounsfield, FBP) | `_candidatos.md`:727 (PENDIENTE); solo anclas en `wu2022xcist` y mencion de la formula en `wang2019cochlear` | si (GAP justificado) |
| l.35 | Hueso = voxeles sobre 150~HU fuera de la geometria metalica | `peters2025hybrid.md`:177 (Sec. 2.5, p. 5) | si (verif. r05) |
| l.35 | Dos fuentes de MAR segmentan el metal clinico con 2500~HU | `wang2025adaptiveweighting.md`:110, :186-187; `li2024.md`:46, :168 (Sec. IV-E, p. 1878) | si |
| l.35 | Los dos umbrales son definiciones operativas, no limites fisicos | `li2024.md`:62; `wang2025adaptiveweighting.md`:309 ("hand-crafted"); `capitulo3.tex`:46 | si |
| l.35 | Cohorte primaria, recorte por defecto, mediana 0.42 de voxeles a 150~HU o menos en las mascaras sacras, a lo largo del eje del corredor mas ancho | `tesis/main.tex`:123 ("median fraction ... was 0.42"); `maintex_cifras.md`:4, :17; `capitulo3.tex`:87 | si |
| l.35 | Consecuencia: el corredor se mide sobre mascaras anatomicas, no con 150~HU | `capitulo3.tex`:87; `tesis/main.tex`:123 ("an HU-based bone definition would exclude much of the corridor") | si (S01 de r05 aplicado) |
| l.37-42 | Ecuacion de la ventana `[w_min, w_max]` llevada a `[0,1]` | `wang2025adaptiveweighting.md`:112, :184 (Eq. 2, p. 2410) | si (verif. r05) |
| l.42 | Saturacion por arriba y por abajo; fraccion inversamente proporcional al ancho; canje rango/contraste | demostracion desde la Ec. `eq:ventana` | si |
| l.44 | Definicion de codificacion multiventana; "evita elegir entre conservar el rango y separar los contrastes" | sin cita; contradicha por #141 (`04-implicancias.md`:9717-9724) | **no (T01)** |
| l.44 | Tres ventanas de Wang et al. `[-1000,2000]`, `[-320,480]`, `[-160,240]`~HU, en cascada y no como canales | `wang2025adaptiveweighting.md`:108, :167-168 (Sec. V-A-1, p. 2412); :49, :145 (cascada) | si |
| l.44 | Ida y vuelta y su error en HU por voxel | `capitulo3.tex`:58, 65 | si (verif. r05) |
| l.46 | Tres codificaciones del Obj 1; techo 2000 < 2500~HU; 20 000~HU; arcoseno hiperbolico sobre `[-1000, 20 000]`~HU | `capitulo3.tex`:69, 71; `tesis/main.tex`:77; DEC (`01-decisiones.md`:1049) | si (verif. r05) |
| l.46 | El suelo de $-1000$~HU es comun a las tres y no se declara | `src/common/ventanas.py`:44; `e6c_techo_lw.py`:66, :81; #141 ABIERTA | **no (T01)** |
| l.46 | `\GAPDATO` forma y parametros del arcoseno hiperbolico, solo en el codigo | `experiments/objetivo1/e6c_techo_lw.py`:61-69; `MAPA.md`:84; #141 no publica la forma | si (GAP justificado) |
| l.46 | Compuerta mide MAE dentro del hueso | `capitulo3.tex`:60-65 | si (verif. r05) |
| l.46 | `\GAPDEC` "la variante que adopta no se ha fijado" | `src/common/ventanas.py`:44 (`'pub+asinh'`); `diseno_A.md`:57 | **no (T04)** |
| l.50 | Selles et al.: rayas claras y oscuras que ocultan estructuras | `selles2024marreview.md`:73 (Sec. 1, p. 1) | si |
| l.50 | Severidad por tamano, forma y aleacion; osteosintesis en categoria intermedia, cualitativa y sin criterio numerico | `selles2024marreview.md`:16, :33, :50 (Tabla 1, p. 6) | si |
| l.52 | Listas de mecanismos: coinciden en endurecimiento, dispersion y efectos de borde | `selles2024marreview.md`:37; `deman1999.md`:69-79, :163 | si |
| l.52 | Selles et al.: endurecimiento, inanicion, dispersion y efectos de borde como principales | `selles2024marreview.md`:37 ("are the main contributors") | si |
| l.52 | De Man et al.: aislamiento en simulacion 2D; principales = endurecimiento, dispersion, ruido y EEGE | `deman1999.md`:161, :166 | si |
| l.52 | Todas las causas producen rayas; sin peso numerico | `deman1999.md`:164; :233 (contribucion relativa NO ENCONTRADO) | si |
| l.54 | Apertura con su condicion: "En la simulación bidimensional de De Man et al." | `deman1999.md`:201; T01 de r05 aplicado | si |
| l.54 | Endurecimiento: absorcion preferente de baja energia y desplazamiento del espectro | `selles2024marreview.md`:66-67 | si |
| l.54 | Park et al.: *cupping* dentro y rayas que corrompen fuera | `park2015ct.md`:9, :27 | si |
| l.54 | De Man et al.: rayas oscuras en direcciones de mayor atenuacion y entre dos o mas metales | `deman1999.md`:196-197 (Sec. III-B, p. 693) | si |
| l.54 | Dispersion y alta densidad electronica del metal | `selles2024marreview.md`:70 | si |
| l.54 | Razon dispersa/primaria de 0.0001, elegida de forma arbitraria, basta para rayas apreciables | `deman1999.md`:44, :189, :199 | si |
| l.56 | Inanicion de fotones: muy pocos fotones y faltan datos de proyeccion esenciales | `selles2024marreview.md`:68-69 | si |
| l.56 | De Man et al. no nombran la inanicion de fotones | `deman1999.md`:71 ("no se nombra con ese termino") | si |
| l.56 | Artefacto de ruido: lineas finas alternas; depende de la atenuacion total integrada; no lineal; acoplado a dispersion y endurecimiento | `deman1999.md`:206-209 (Sec. III-E, p. 694) | si |
| l.56 | La inanicion se define sin decir que el metodo no la representa | #141 ABIERTA; contraste con l.114 | **no (T02)** |
| l.58 | EEGE: rayas tangentes a bordes rectos largos ("según recuerdan"); rayas que irradian desde el metal | `deman1999.md`:204-205 ("is known to cause"; "radiating from the metals") | si |
| l.58 | Selles et al.: efectos de borde como rayas alineadas con el borde del metal | `selles2024marreview.md`:71 | si |
| l.58 | Ninguna de las dos descripciones da distancia; De Man et al. no mide hasta donde llegan las rayas | `deman1999.md`:81-97, :228-230 (NO ENCONTRADO) | si |
| l.60 | Glover y Pelc: integrar el flujo y tomar su logaritmo vuelve no lineal la medida con variacion axial | `glover1980nonlinear.md`:10 | si |
| l.60 | Una discontinuidad = error local; dos o mas = rayas de largo alcance que conectan estructuras | `glover1980nonlinear.md`:30, :35 | si |
| l.60 | Lo estudian en hueso, sin metal, con fuente monocromatica idealizada | `glover1980nonlinear.md`:14 ("Estudia huesos petrosos, no metal"; "idealiza una fuente monocromatica puntual") | si |
| l.60 | De Man et al. dejan fuera el volumen parcial axial al simular en 2D | `deman1999.md`:165-166 | si |
| l.62 | El artefacto no queda dentro del implante; por eso se genera tambien en $B_\delta$ | `deman1999.md`:196-197, :205; `park2015ct.md`:27; `capitulo3.tex`:176 | si |
| l.62 | "las fuentes revisadas no dan hasta dónde llegan las rayas" | `radzi2014metalartifacts.md`:39-40, :89, :92 (2.0/2.6/1.6/2.0~mm en CT) | **no (T06)** |
| l.62 | Los mecanismos se definen sobre las proyecciones; supuesto del dominio de imagen y remision a amenazas | `deman1999.md`:20-23, :138; `capitulo3.tex`:261 | si (verif. r05) |
| l.62 | Las dos consecuencias para la sintesis no incluyen el limite del rango negativo | #141 ABIERTA | **no (T02)** |
| l.64 | MAR reduce el artefacto de una TC ya adquirida; la simulacion fisica lo produce | `docs/03-glosario.md` (MAR); `overleaf/CLAUDE.md` (termino fijo) | si (S02 de r05) |
| l.64 | CatSim pertenece a XCIST y el protocolo de Peters et al. corre sobre el | `wu2022xcist.md` p. 6; `peters2025hybrid.md`:36 | si (verif. r05) |
| l.64 | CatSim modela espectro policromatico, ruido cuantico y electronico, volumen parcial no lineal y dispersion | `deman2007catsim.md`:75-77, :172-181 (Abstract, p. 1) | si |
| l.64 | El sintetizador genera con modelo aprendido, sin simular proyecciones; comparacion prevista | `capitulo3.tex`:172, 219-225 | si (verif. r05) |
| l.66 | Metricas de Peters et al. con sus nombres publicados | `peters2025hybrid.md`:56; #8 APLICADA; BITACORA §2 2026-10-03 | si (verif. r05) |
| l.66 | *Streak amplitude*: 5 % de desviaciones mas altas menos 5 % mas bajas, respecto de la imagen sin metal del mismo caso | `peters2025hybrid.md`:172-183 | si (verif. r05) |
| l.66 | *Bone integrity* con el umbral de 150~HU, cambio de volumen y Sorensen-Dice; *metal integrity* con umbral por region | `peters2025hybrid.md`:177-183, :262 | si (verif. r05) |
| l.66 | Disenadas para MAR; la inversion tiene definicion operativa pendiente; *streak amplitude* unico criterio primario | `capitulo3.tex`:215 (`\GAPDEC`), :217 | si (verif. r05) |
| l.70 | Zwingmann et al.: solo fracturas Tile y Pennal B y C; B inestable a rotacion, C tambien vertical | `zwingmann2009navigated.md`:11, :88-90 | si (verif. r05) |
| l.70 | Via percutanea; su distribucion de grados es la referencia clinica del Obj 2 | `zwingmann2009navigated.md`:83; `capitulo3.tex`:79 | si (verif. r05) |
| l.72 | Smith et al.: entra por el ilion a S1 o S2; tres corticales, dos del ilion y una del ala sacra | `smith2006iliosacral.md`:69-70 ("cross 3 cortices (2 ileum, 1 sacral ala)") | si |
| l.72 | El ala sacra desciende lateral y caudal desde el cuerpo vertebral superior | `routt1997.md`:122 | si (verif. r05) |
| l.72 | `\GAPLIT` anatomia pelvica (cortical, platillo, ala, foramen, tabla externa, articulacion sacroiliaca) | `_candidatos.md`:730 (PENDIENTE); `ebraheim1997.md`:11, :80 usa los terminos sin definirlos | si (GAP justificado) |
| l.72 | Transiliosacro cruza las dos articulaciones y sale por la tabla externa opuesta | `mclaren2021corridor.md`:127; `docs/03-glosario.md`:74-76 | si |
| l.72 | Kaiser et al. eligen 10~mm para el paso de un tornillo iliosacro | `kaiser2014dysmorphism.md`:72, :391 | si |
| l.72 | `\GAPDEC` tipo de tornillo del corredor y de la referencia clinica | #130 **DECIDIDA 2026-10-04** (:8893-8918) | **no (T03)** |
| l.74 | Routt et al.: decubito supino y fluoroscopia en tres planos | `routt1997.md` p. 206 | si (verif. r05) |
| l.74 | Zwingmann et al.: navegacion sobre adquisicion 3D con equipo que rota 190°; TC posoperatoria en ambas series | `zwingmann2009navigated.md`:83, :103 | si (verif. r05) |
| l.76 | Zona segura en el ala; limites; estructuras vecinas (raiz de L5, canal, vasos iliacos) | `routt1997.md` Fig. 2, pp. 212-213 | si (verif. r05) |
| l.76 | Gardner et al.: dos conos unidos por la punta; seccion minima en plano ortogonal al eje | `gardner2010safezones.md` M&M, p. 623 | si (verif. r05) |
| l.76 | La zona segura no es variable de este trabajo | `capitulo3.tex`:168 | si (verif. r05) |
| l.78 | McLaren et al.: un numero por segmento; recta que se expande hasta tocar y atravesar la cortical en al menos tres puntos | `mclaren2021corridor.md`:147-149 ("in at least three locations") | si |
| l.78 | Gardner, Kaiser y McLaren usan un umbral de 10~mm y lo toman de trabajos anteriores | `mclaren2021corridor.md`:33, :130; `gardner2010safezones.md` (refs. 17 y 20); `kaiser2014dysmorphism.md`:29, :72 | si |
| l.78 | McLaren et al. declaran que el corredor minimo no esta establecido | `mclaren2021corridor.md`:104-105 ("has not yet been established") | si |
| l.78 | Kaiser et al.: 1 a 2~mm alrededor de un tornillo de 6.3 a 8~mm, leido por este trabajo como holgura radial por lado | `kaiser2014dysmorphism.md`:36-37, :167, :425-426 (la aritmetica no se publica); `capitulo3.tex`:89 | si |
| l.78 | Medicion sobre mascaras anatomicas de TotalSegmentator y criterio propio de viabilidad | `wasserthal2023`; `capitulo3.tex`:87, 89 | si (S09 de r05) |
| l.80 | Kaiser et al.: reformateo al eje del sacro, perpendicular al platillo superior de S1; angulacion contra crestas y espinas | `kaiser2014dysmorphism.md` Fig. 1, p. e120(3); `capitulo3.tex`:83 | si (verif. r05) |
| l.80 | Regla de longitud util: no menos de 5~mm a la cortical a cada lado, leida como margen cortical | `kaiser2014dysmorphism.md`:80, :228 | si |
| l.80 | "Este trabajo expresa sus poses en ese marco" | #138 ABIERTA (:9535-9544); `capitulo3.tex`:269 | **no (T07)** |
| l.82 | Posicion ideal: dentro de los margenes corticales, paralela al platillo, a media altura entre platillo de S1 y foramen de S1 | `smith2006iliosacral.md`:71-73 | si |
| l.82 | Tres tipos de perforacion: anterior del sacro, canal espinal, platillos vertebrales | `smith2006iliosacral.md`:76-78 | si |
| l.82 | Cuatro grados: 0 sin perforacion, 1 < 2~mm, 2 de 2 a 4~mm, 3 > 4~mm | `smith2006iliosacral.md`:80-83 | si |
| l.82 | Este trabajo la calcula como protrusion fuera de una envolvente osea segmentada | `capitulo3.tex`:189-194, 269 | si (verif. r05) |
| l.84 | Smith et al. declaran tomar la escala de la de tornillos pediculares y le suman una angular | `smith2006iliosacral.md`:79, :84-87 | si |
| l.84 | `\GAPDEC` dimension angular de la escala en SAP | #11; `MAPA.md`:45 | si (GAP justificado) |
| l.84 | Zwingmann et al. aplican la escala de perforacion | `zwingmann2009navigated.md`:230 | si (verif. r05) |
| l.84 | Hinsche et al.: definicion binaria, sin grados de profundidad | `hinsche2002fluoroscopy.md`:29, :66, :90 | si (verif. r05) |
| l.86 | Grados 1 y 2 de 2~mm; grado 3 sin limite superior; equiespaciar es convencion | demostracion desde `smith2006iliosacral.md`:80-83; `capitulo3.tex`:269 | si |
| l.88 | Tres componentes de SAP; el tercero es la fraccion por zona de densidad | `capitulo3.tex`:166, 189 | si (verif. r05) |
| l.88 | Arand et al.: modelo medio de valores de gris del anillo pelvico; ala sacra mas baja que el cuerpo de S1 | `arand2019pelvicring.md`:11, :90, :100-101 | si (S10 de r05) |
| l.88 | SAP reporta esa fraccion de forma descriptiva; `\GAPDEC` fuente y definicion operativa | `capitulo3.tex`:243; `MAPA.md`:43 (D-O2.6 frente a DEC 2026-09-14 #50) | si (GAP justificado) |
| l.92 | Kazerouni et al. revisan difusion en imagen medica | `kazerouni2023diffusionsurvey.md`:8 | si (verif. r05) |
| l.92 | Ho et al.: cadena de Markov que invierte un proceso directo gaussiano; $n_{\max}=1000$ | `ho2020denoising.md`:9, :23 ("We set T = 1000 for all experiments") | si |
| l.92 | Dorjsembe et al.: el proceso directo borra por completo la estructura original | `dorjsembe2024` §II | si (verif. r05) |
| l.93-97 | Ec. `eq:difusion-directa`; cambio declarado de $\bar\alpha_t$ a $\bar\gamma_n$; coseno de Nichol y Dhariwal; $\beta_n \in (0,1)$ | `zhang2025diffboost` Ec. 3; `dorjsembe2024` Ec. (1); `nichol2021improved` Sec. 3.2; BITACORA §2 2026-10-03 | si (verif. r05) |
| l.99-104 | Prediccion del ruido con objetivo simplificado; Ec. `eq:perdida-difusion` como la escribe Rombach et al.; U-Net en Ho et al. y Song et al.; definicion de Ronneberger et al. | `ho2020denoising.md`:9; `rombach2022latentdiffusion` Ec. 1; `song2021ddim` Ap. D.1; `ronnenberger2015unet` | si (verif. r05) |
| l.104 | "El borrador ... propone también una U-Net, arquitectura que aún no se ha fijado" | `diseno_A.md`:69; `src/renderizador/modelo.py`:78-85 | **no (T05)** |
| l.106 | Song et al.: procesos no markovianos, mismo objetivo, muestreo determinista con menos pasos y sin reentrenar | `song2021ddim.md`:25-26 | si (verif. r05) |
| l.106 | Aceleracion de 10 a 50 veces en tiempo de reloj | `song2021ddim.md`:26 ("10x to 50x faster in terms of wall-clock time") | si |
| l.106 | Las tres fuentes evaluan imagenes naturales; ninguna trabaja con TC ni metal | `_index.md` (filas de `ho2020denoising`, `song2021ddim`, `nichol2021improved`) | si (verif. r05) |
| l.106 | "el borrador ... no menciona el calendario de ruido; ambos quedan pendientes" | `diseno_A.md`:67-71 (no lo menciona, correcto); `src/renderizador/difusion.py`:5, :11, :29-30 (si lo fija) | **no (T05)** |
| l.108 | Rombach et al.: concatenacion para condicion alineada y atencion cruzada para no espacial | `rombach2022latentdiffusion.md`:15, :62 (§4.3.2, p. 7) | si |
| l.108 | Dorjsembe et al. concatenan la mascara como canal adicional en cada paso | `dorjsembe2024` §II | si (verif. r05) |
| l.108 | ControlNet: modelo congelado, copia del codificador, convoluciones inicializadas en cero | `zhang2023controlnet` §3.1-3.2 | si (verif. r05) |
| l.110 | Difusion latente en dos etapas; decodificador en una pasada | `rombach2022latentdiffusion.md`:13 | si (verif. r05) |
| l.110 | Perdida perceptual y adversarial para evitar el desenfoque de las perdidas por pixel | `rombach2022latentdiffusion.md`:34, :136-137 (§3.1, p. 3) | si |
| l.110 | La compresion elimina detalle de alta frecuencia | `rombach2022latentdiffusion.md`:127 (§1, p. 2) | si |
| l.110 | Advertencia: la reconstruccion puede ser cuello de botella si se exige exactitud fina por pixel | `rombach2022latentdiffusion.md`:57, :68 (§5, p. 9) | si |
| l.110 | Lectura propia: conservar los HU del hueso con MAE < 25~HU; el veredicto negativo descarto la difusion latente y con ella ControlNet | `capitulo3.tex`:58, 71, 75, 174; DEC 2026-09-19 (`01-decisiones.md`:1140-1144); #141 "No invalida el Objetivo 1" | si |
| l.112 | Lugmayr et al.: modelo preentrenado sin condicion, solo cambia el muestreo; combinan region conocida y generada; retroceden y avanzan en el tiempo de difusion | `lugmayr2022repaint.md`:9, :29 ("goes forward and backward in diffusion time") | si |
| l.112 | La otra forma: modelo condicionado por concatenacion, como el *inpainting* de Rombach et al. | `rombach2022latentdiffusion.md`:104-105 (Tabla 15) | si |
| l.112 | El sintetizador recibe `G` borrada y las mascaras, genera dentro de `G` y copia el resto | `capitulo3.tex`:172, 176 | si (verif. r05) |
| l.112 | `\GAPDEC` atribucion del muestreo frente a Lugmayr et al. y LeFusion | #106, #117; `MAPA.md`:73 | si (GAP justificado) |
| l.114 | 2.5D: cortes axiales con contexto contiguo, sin ser 3D completo | `capitulo3.tex`:172; `diseno_A.md`:60 | si |
| l.114 | `\GAPDEC` numero de cortes, "que solo propone el borrador de su diseño" | `diseno_A.md`:60-61; `src/renderizador/datos.py`:19, :72 | **no (T04)** |
| l.114 | Lectura propia: pocos cortes vecinos aportan informacion axial pero no reproducen la integracion; el sintetizador no contiene el mecanismo | `glover1980nonlinear.md`:37, :39; marcada "este trabajo lee" | si |
| l.118 | Tres tipos de resultado; unidad de analisis por objetivo; la referencia clinica cuenta tornillos | `capitulo3.tex`:71, 207, 223, 242-244, 265 | si (verif. r05) |
| l.118 | `\GAPDEC` agregacion por paciente de poses y regiones de rayas | `MAPA.md`:56; `capitulo3.tex` §Apariencia | si (GAP justificado) |
| l.120 | Wasserstein-1 sobre cuatro grados equiespaciados: suma de diferencias de las acumuladas; unidad el grado; 1 y 3 como valores | `capitulo3.tex`:200-205 (Ec. `eq:w1`) | si (verif. r05) |
| l.120 | `\GAPLIT` fuente de Wasserstein-1 | `_candidatos.md`:728 (PENDIENTE) | si (GAP justificado) |
| l.122 | Superioridad y equivalencia; una diferencia no significativa no responde la segunda; IC del 90 % dentro de $[-\Delta,+\Delta]$ | `capitulo3.tex`:225; BITACORA §2 2026-10-03 (TOST siempre sobre el IC) | si (S03/S06 de r05) |
| l.124 | Wilcoxon pareada y de una cola como prueba de superioridad del Obj 3 | `capitulo3.tex`:223 | si (verif. r05) |
| l.124 | TOST con margen por variabilidad entre semillas y entre corridas repetidas; aun sin preinscribir | `capitulo3.tex`:225, 231 | si (verif. r05) |
| l.124 | `\GAPDEC` si la comparacion de equivalencia pasa a trabajo futuro | #90; `MAPA.md`:48 | si (GAP justificado) |
| l.126 | IC del 95 % por remuestreo de pacientes; media sobre pacientes del error de cada paciente; motivo del remuestreo | `capitulo3.tex`:71, 265 | si (S04/guia-3 de r05) |
| l.126 | `\GAPLIT` Wilcoxon, TOST, relacion con el IC del 90 % y remuestreo | `_candidatos.md`:729 (PENDIENTE); `MAPA.md`:81 | si (GAP justificado) |
| l.128 | Regla fijada antes de correr la prueba que decide; poses y metrica antes de cualquier distancia | `capitulo3.tex`:58, 127; BITACORA §2 2026-09-29 | si (verif. r05) |
| l.128 | Decisiones posteriores a ver datos: resultado exploratorio con pacientes de prueba y tres en el Obj 2 | `capitulo3.tex`:253, 255 | si (verif. r05) |
| l.128 | Seis combinaciones de la regla; multiplicidad sin corregir; veredicto negativo no comprometido | `capitulo3.tex`:69, 71, 265 | si (verif. r05) |
| l.128 | Extension a Guo et al. con la misma regla y los mismos pacientes de prueba; siete combinaciones | DEC 2026-09-19 pto 3 (`01-decisiones.md`:1145-1149); `capitulo3.tex`:75 | si |
| l.128 | "según la decisión que la autorizó, no cambia el diseño del Objetivo~3" | DEC 2026-09-19 pto 3, literal: "Su resultado no cambia el diseno del Objetivo 3" | si (guia-1/S05 de r05) |
| l.128 | El veredicto de la extension se presenta en el capitulo de resultados (prosa, sin `\ref`) | BITACORA §2 2026-09-29; `capitulo4.tex` sin `\label`; `MAPA.md`:44 | si |
| l.130 | MAE promedia valores absolutos; RMSE promedia cuadrados y nunca es menor; RMSE de la MAR como orden de magnitud | `capitulo3.tex`:60-67; BITACORA §2 2026-09-30 ("orden de magnitud") | si (verif. r05) |

## Comprobaciones transversales

- **Claves de cita:** las 33 claves usadas (`abadi2019`, `arand2019pelvicring`, `deman1999`, `deman2007catsim`,
  `dorjsembe2024`, `gardner2010safezones`, `glover1980nonlinear`, `guo2025maisi`, `hinsche2002fluoroscopy`,
  `ho2020denoising`, `kaiser2014dysmorphism`, `karageorgos2024ddpm`, `kazerouni2023diffusionsurvey`, `li2024`,
  `lugmayr2022repaint`, `mclaren2021corridor`, `nichol2021improved`, `park2015ct`, `peters2025hybrid`,
  `rombach2022latentdiffusion`, `ronnenberger2015unet`, `routt1997`, `selles2024marreview`,
  `smith2006iliosacral`, `song2021ddim`, `wang2019cochlear`, `wang2025adaptiveweighting`, `wasserthal2023`,
  `wu2022xcist`, `zhang2023controlnet`, `zhang2025diffboost`, `zhang2025lefusion`, `zwingmann2009navigated`)
  **existen todas en `overleaf/referencias.bib`**.
- **E-F3:** ninguna `\cite` es sujeto gramatical sola. Los dos casos de dos autores llevan la forma correcta:
  "Glover y Pelc" (bib: Glover; Pelc) y "Nichol y Dhariwal" (bib: Nichol; Dhariwal). Cada apellido nombrado
  coincide con el primer autor del `.bib`; "Ronneberger" se escribe bien aunque la clave sea `ronnenberger2015unet`.
  "Selles" va sin tilde, como el `.bib` (PAT-127 no reincide en este capitulo).
- **P-EA1:** ninguna fuente de fabricante ni de catalogo se cita en el capitulo.
- **Regla 4 de `overleaf/CLAUDE.md` (solo abstract):** las unicas fichas con "Profundidad: solo abstract" son
  `song2024bmar.md`:1 y `zhang2026pediclescrew.md`:3, y **ninguna de las dos se cita aqui**.
  `wang2025adaptiveweighting.md`:13 retira esa marca, asi que sus cifras de cuerpo (tres ventanas, 2500 HU)
  son citables.
- **Alcance vigente:** no aparecen Dice ni HD95 como objetivo (el Sorensen-Dice de l.66 es componente publicado
  de *bone integrity*, decision de #8); no aparece "31-60 %"; no aparecen BFC ni ISC; la difusion latente y
  ControlNet solo figuran como teoria y como descartadas por el veredicto negativo (l.110).
- **Implicancias ABIERTAS:** #126 (titulo y pregunta de la introduccion) no se afirma aqui. #133, #134, #139,
  #140 no se citan ni se contradicen; sus cifras no aparecen. #135, #136 (cribado de fractura) no tocan este
  capitulo. #137 (ninguna lectura humana en el Obj 3) tiene su marca en `capitulo3` §Apariencia y el marco
  teorico no enumera los bloques de evaluacion: sin hallazgo. **#138 si se contradice (T07)** y **#141 si
  (T01, T02)**. **#130, decidida, se sigue tratando como pregunta abierta (T03)**.

## Comprobacion de patrones VIGENTES (dominio G-T4 / E-R6 / OC-*)

PAT-11: **reincide** (T04: GAP sobre el estado inicial). PAT-14: no reincide (los dos nombres fijos de Kaiser
et al. estan bien separados en l.78 y l.80). PAT-19: **reincide** (T04, dos veces). PAT-31: no reincide
(l.35 lleva cohorte, recorte y "la mediana"; l.54 abre con la condicion de la simulacion). PAT-39:
**reincide** (T06). PAT-45, PAT-58, PAT-62, PAT-113, PAT-114, PAT-124, PAT-126: fuera de dominio o sin caso.
PAT-52: no reincide (l.124 y l.128 dan la consecuencia). PAT-64: **reincide** (T06, mismo caso). PAT-72: no
reincide (l.56 "no nombran", l.58 "no menciona", que es lo que dicen las fichas). PAT-101: no reincide (l.52
y l.112 acotados a "las fuentes revisadas", y esta vez el acotamiento es el problema, no la falta de el).
PAT-102: no reincide. PAT-115: no reincide (l.66 declara pendiente la inversion y remite). PAT-116: no
reincide (l.128 cita la decision que cierra el condicional). PAT-117: no reincide (la figura asigna
Wasserstein-1 al Obj 4 para la definicion y al Obj 2 para la lectura, como `introduccion.tex`:43).
PAT-118: no reincide (l.35 cierra con la consecuencia). PAT-119: no reincide. PAT-121: fuera de dominio (el
capitulo no reporta lecturas humanas). PAT-122: **reincide** (T04, T05). PAT-123: **reincide** (T02, T07).
PAT-125: no reincide. PAT-127: no reincide.

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| El marco teorico declara el limite de un mecanismo del artefacto (volumen parcial) y calla el de otro que la representacion propia tampoco puede expresar | OC-2, G-T4 | inanicion de fotones definida sin decir que el metodo no la representa | PAT-123 |
| Una ventaja de diseno enunciada como definicion generica ("evita elegir entre X e Y") oculta que la implementacion si eligio | G-T4, E-P3 | "evita así elegir entre conservar el rango y separar los contrastes" | nuevo |
| Un GAP dice "solo lo propone el borrador" cuando el codigo que ya entreno fija el valor; el estandar del capitulo era "solo consta en el codigo y no en un registro" | OC-2, G-T4 | `\GAPDEC{número de cortes ..., que solo propone el borrador de su diseño}` | PAT-19 + PAT-122 |
| Un negativo acotado a "las fuentes revisadas" se escribe sobre la magnitud equivocada: una fuente si la da, lo que falta es que la calibre | E-R6, E-P3 | "las fuentes revisadas no dan hasta dónde llegan las rayas" | PAT-39 + PAT-64 |
| Una decision de la autora resuelve parte de un `\GAPDEC` multiple y el GAP se mantiene entero, o se borraria entero | OC-2, OC-3 | `\GAPDEC` del tornillo: dos partes resueltas por #130, una abierta | nuevo |
