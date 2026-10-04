# Auditoria de trazabilidad — capitulo1 — r03

Archivo: `overleaf/secciones/capitulo1.tex` (127 lineas). Lint r03: PASA (0/0/0; GAP lit 4 / dato 1 / dec 7).
Respuesta previa: `capitulo1-r02-respuesta.md` (17 altos/medios aplicados, 0 rechazados; 1 bajo no aplicado, S03, de estilo). No hay RECHAZADOS de trazabilidad que respetar.
Correcciones de trazabilidad de r02 verificadas en el texto: T01 (l.72, `\GAPDEC` con el hecho registrado, `docs/SITUACION_ACTUAL.md`:183), T02 (l.72, "la primera o la segunda vertebra sacra", `smith2006iliosacral`:69) y T03 (l.124, septimo candidato de Guo et al., `capitulo3.tex`:75, 265). Las tres estan aplicadas y tienen fuente.
Contenido nuevo de r02 rastreado: metricas de Peters et al. (l.66), dispersion parecida al endurecimiento y ruido no lineal (l.54, 56), U-Net del borrador (l.102), ida y vuelta de las tres codificaciones (l.46), LeFusion con su cita (l.110), orden de secciones (l.13).
Claves: todas existen en `overleaf/referencias.bib` (se comprobaron tambien `zhang2025lefusion`, `guo2025maisi`, `kazerouni2023diffusionsurvey`, `hinsche2002fluoroscopy` y `ronnenberger2015unet`, cuyo primer autor es Ronneberger). Cada apellido nombrado coincide con el primer autor. Ninguna cita es sujeto gramatical sola. No hay fuentes de fabricante.
Contenido retirado: no aparecen Dice/HD95 como objetivo (el coeficiente de Sorensen-Dice de l.66 es un componente publicado de *bone integrity*, no una evaluacion de segmentacion posterior), ni "31-60 %", ni BFC/ISC. La difusion latente y ControlNet aparecen solo como teoria y como descartadas (l.108).

**Conteo: alta=0 media=1 baja=1**

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-3 | l.70-72 (parrafos de la fijacion iliosacra y `\GAPDEC` del tipo de tornillo) | "la distribución de sus grados de brecha forma la referencia clínica del Objetivo 2" | ficha `zwingmann2009navigated`:79 ("navigated iliosacral screw placement", M&M, p. 1834), :83 y :197 ("localization of the transiliosacral screw", M&M, p. 1835), :219 ("guide wire ... across the ileum into the S1 vertebra"); `docs/04-implicancias.md` #130 punto 3 (ABIERTA) | El capitulo presenta la referencia clinica dentro de la fijacion iliosacra y en l.72 declara que los dos tipos de tornillo no son intercambiables. La ficha de Zwingmann et al. registra, sin embargo, que el articulo llama a su tornillo de las dos formas: "iliosacral" en el periodo navegado y "transiliosacral" en la medicion de la posicion. El `\GAPDEC` de l.72 pregunta que tornillo representa el corredor medido, pero no pregunta de que tipo es el tornillo de la referencia clinica, que es el punto 3 de #130. Ademas, #130.3 dice que Zwingmann "gradua tornillos iliosacros", lo que la ficha solo sostiene en parte; hay que informarlo a la autora (no se resuelve aqui, regla 3) | Se amplia el GAP existente, sin crear uno nuevo: `\GAPDEC{qué tornillo representa el corredor que mide este trabajo, que el registro describe de la cortical externa de un ilion a la del ilion opuesto, y con ello si le aplican el umbral de 10~mm y la holgura radial de Kaiser et al., definidos para el tornillo iliosacro, y si es del mismo tipo que los tornillos de la referencia clínica, que Zwingmann et al. llaman iliosacros y transiliosacros}`. Ademas, se anota en MAPA (fila de #130) la discrepancia con #130.3 |
| T02 | baja | G-T4 | l.66, ultima oracion | "Las tres se diseñaron para evaluar MAR; la Sección apariencia describe cómo las usa" | `capitulo3.tex`:215 ("su uso aquí exige invertirlas \GAPDEC{definición operativa de la inversión ...}"); ficha `peters2025hybrid`:256-263 (no da la funcion de puntuacion; el umbral de metal es adaptativo) | La remision promete que la Seccion apariencia describe como usa las metricas el Objetivo 3, pero ahi el uso exige invertirlas y la inversion esta pendiente (`\GAPDEC`). Se pierde la condicion del cap. 3 al retomarlo (PAT-31 reincide, en forma leve) | "Las tres se diseñaron para evaluar MAR, y su uso para evaluar síntesis exige invertirlas (Sección~\ref{sec:apariencia}); el Objetivo~3 toma la \emph{streak amplitude} como su único criterio primario." |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.11 | Funcion del capitulo; reparto con los caps. 2 y 3 | estructura propia; los `\ref` existen (lint PASA) | si |
| l.13 | Orden de las secciones; el muestreador precede al sintetizador en la cadena | `capitulo3.tex`:21-33 (Fig. `fig:pipeline`: muestreador en l.25, sintetizador en l.29) | si |
| l.13 | Que pieza usa cada seccion (compuerta, representacion, corredor, escala, referencia clinica, sintetizador, estadistica) | `capitulo3.tex`:13, 20-31, 69, 79, 172, 189 | si |
| fig. 1.1 | Conceptos -> Obj 1 (compuerta, canales), Obj 2 (muestreador), Obj 3 ($B_\delta$, metricas de apariencia, sintetizador), Obj 4 (SAP), protocolo fisico | `capitulo3.tex`:13, 20-31, 172, 189, 213, 219 | si |
| l.31 | Lectura del detector = indice del sinograma | `deman2007catsim` ("y_i is the detector signal at sinogram index i", Sec. 2.1, p. 1) | si |
| l.31 | Senal = suma sobre las energias, atenuada segun la longitud recorrida en cada material | `deman2007catsim`, defs. A_ik, l_iso, mu_ok (Sec. 2.1, p. 1) | si |
| l.31 | Coeficiente de atenuacion lineal por material y energia | `deman2007catsim` ("mu_ok is the linear attenuation coefficient ...") | si |
| l.31 | Abadi et al. (DukeSim) calculan la atenuacion con Beer-Lambert | `abadi2019`:51 ("computed using the Beer-Lambert Law", Sec. II-B, p. 1458) | si |
| l.31 | Wang et al. (implantes cocleares): Beer-Lambert discretizada en cinco energias | `wang2019cochlear`:52, 56 ("Beer-Lambert law discretized on 5 different energies", Intro, p. 2) | si |
| l.33 | FBP en De Man 1999, CatSim y Karageorgos | `deman1999` Sec. II-C; `deman2007catsim` Sec. 3.1; `karageorgos2024ddpm` Sec. II-F | si |
| l.33 | Park et al.: FBP supone el modelo monocromatico de Radon; el haz policromatico se aparta de forma no lineal | `park2015ct`:9 | si |
| l.33 | La cohorte solo tiene volumenes reconstruidos | `capitulo3.tex`:42-46; `docs/02-datos.md` | si |
| l.33 | Lo medido y lo generado estan en el dominio de imagen; solo el protocolo fisico (previsto) pasa por proyecciones | `capitulo3.tex`:172, 219-221, 261 | si |
| l.35 | Agua 0 HU y aire -1000 HU por definicion | `wu2022xcist` (Discussion Exp. 1, p. 13) | si |
| l.35 | Conversion HU-mu con el coeficiente del agua por energia | `wang2019cochlear` (Sec. 2.1, p. 4) | si |
| l.35 | `\GAPLIT` fisica de TC (Beer-Lambert, escala Hounsfield, FBP) | ninguna ficha enuncia la ley ni la transformacion; MAPA:75; `_candidatos.md` | si (GAP justificado) |
| l.35 | Hueso > 150 HU fuera de la geometria metalica (Peters) | `peters2025hybrid`:177 (Sec. 2.5, p. 5) | si |
| l.35 | Wang y Li segmentan el metal clinico con 2500 HU | `wang2025adaptiveweighting`:110, 186 (Sec. V-A-2, p. 2413); `li2024` Sec. IV-E, p. 1878 | si |
| l.35 | 2500 HU para cribar la cohorte y delimitar el metal real | `capitulo3.tex`:73, 87, 178; DEC 2026-09-20 (2) D1 | si |
| l.35 | Voxeles sacros a 150 HU o menos a lo largo del eje; un hueso por umbral los dejaria fuera | `capitulo3.tex`:85 (mediana 0.42; "dejaria fuera, en la mediana, esa fraccion del corredor") | si |
| l.37-42 | Ventana: saturar en $[w_{\min}, w_{\max}]$ y llevar a [0,1] (Ec. ventana) | `wang2025adaptiveweighting`:112, 184 (Eq. 2, p. 2410) | si |
| l.42 | Saturacion; fraccion del rango inversamente proporcional al ancho | demostracion a partir de la Ec. ventana | si |
| l.44 | Tres ventanas [-1000,2000], [-320,480], [-160,240] HU en cascada, no como canales | `wang2025adaptiveweighting`:108 (Sec. V-A-1, p. 2412); Sec. III, p. 2410 | si |
| l.44 | Ida y vuelta: HU -> representacion -> HU; su error mide la perdida | `capitulo3.tex`:58, 65; `overleaf/CLAUDE.md` terminos fijos | si |
| l.46 | El Obj 1 examina tres codificaciones; la primera con las ventanas de Wang et al. | `capitulo3.tex`:69 | si |
| l.46 | Techo 2000 < 2500 HU: el metal satura en la ventana ancha | `capitulo3.tex`:71 ("cuyo techo de 2000 HU satura el metal") | si |
| l.46 | Techo de 20 000 HU; arcoseno hiperbolico sobre [-1000, 20 000] HU, no lineal | `capitulo3.tex`:69; `tesis/main.tex`:77; DEC 2026-09-17 | si |
| l.46 | `\GAPDATO` forma y parametros del arcoseno hiperbolico | sin formula en TM, DEC ni `experiments/objetivo1/*.md`; `diseno_A.md`:57 solo da el rango; MAPA:80 | si (GAP justificado) |
| l.46 | La compuerta mide la ida y vuelta como MAE en hueso (Ec. mae) | `capitulo3.tex`:60-65 | si |
| l.46 | El sintetizador usa la codificacion multiventana como canales, sin autoencoder | `capitulo3.tex`:172 | si |
| l.46 | `\GAPDEC` codificacion y precision del sintetizador | texto identico a `capitulo2.tex`:86, cotejado con `experiments/` en capitulo2-r03 (BITACORA §2, 2026-10-03); `diseno_A.md`:57, 69 `[SUPUESTO]` | si (GAP justificado) |
| l.50 | Rayas claras y oscuras que ocultan anatomia; severidad segun tamano, forma y aleacion | `selles2024marreview` Sec. 1, p. 1 | si |
| l.50 | Osteosintesis en categoria intermedia, asignada de forma cualitativa, sin criterio numerico | `selles2024marreview` Tabla 1, p. 6; criterio numerico NO ENCONTRADO | si |
| l.52 | Selles: BH, inanicion, dispersion y bordes como principales | `selles2024marreview`:37 ("... are the main contributors", Sec. 1, p. 1) | si |
| l.52 | De Man: simulacion 2D; las mas importantes son BH, dispersion, ruido y EEGE; todas producen rayas; sin peso numerico | `deman1999`:69-75; Conclusiones, p. 695 | si |
| l.54 | BH: absorcion preferente de baja energia | `selles2024marreview` Sec. 1, p. 1 | si |
| l.54 | Park: *cupping* dentro del objeto y rayas fuera de la region | `park2015ct`:9; Intro, p. 2 | si |
| l.54 | De Man: rayas oscuras en las direcciones de mayor atenuacion; rayas que conectan metales | `deman1999` Sec. III-B, p. 693 | si |
| l.54 | Dispersion por la alta densidad electronica | `selles2024marreview`:70 (Sec. 1, p. 1) | si |
| l.54 | Razon de dispersion muy pequena produce rayas, muy parecidas a las policromaticas | `deman1999` Sec. III-C; :201 ("very similar to the polychromatic artifacts", p. 694) | si |
| l.56 | Inanicion: muy pocos fotones; faltan datos de proyeccion esenciales | `selles2024marreview`:68-69 ("missing essential projection data", Sec. 1, p. 1) | si |
| l.56 | De Man no nombra la inanicion; el ruido como lineas finas alternas que dependen de la atenuacion integrada | `deman1999`:71-72; Sec. III-E, p. 694 | si |
| l.56 | El ruido es no lineal, como BH y dispersion | `deman1999`:135-136, 207 ("Noise artifacts are non-linear artifacts, just like ...", Sec. III-E, p. 694) | si |
| l.58 | EEGE: rayas tangentes a bordes rectos largos; rayas que irradian | `deman1999` Sec. III-D, p. 694 | si |
| l.58 | Selles: rayas oscuras o claras alineadas con el borde | `selles2024marreview`:71 | si |
| l.58 | Ninguna da distancia; De Man no mide hasta donde llegan | `deman1999` Respuestas 2 (NO ENCONTRADO); `selles2024marreview` (NO ENCONTRADO) | si |
| l.60 | Volumen parcial no lineal: integrar el flujo y tomar el logaritmo; una discontinuidad da error local, dos o mas dan rayas largas; en hueso, monocromatica | `glover1980nonlinear` Que hace; Sec. II, pp. 240-243; Restriccion | si |
| l.60 | De Man lo deja fuera al simular en 2D | `deman1999`:73-74 (Sec. II-A, p. 691) | si |
| l.62 | Las rayas se extienden fuera del metal | `deman1999` Sec. III-B/D; `park2015ct` Intro, p. 2 | si |
| l.62 | El ancho de $B_\delta$ es una convencion | `capitulo2.tex` §Representacion; #57/#98 ABIERTAS, no se afirma como resuelto | si |
| l.62 | De Man aisla las causas modificando el sinograma | `deman1999` Sec. II-D, p. 693 | si |
| l.62 | Supuesto del dominio de imagen, con remision a amenazas | `capitulo3.tex`:261 | si |
| l.64 | CatSim dentro de XCIST; el protocolo de Peters corre sobre CatSim | `wu2022xcist` (Simulation, p. 6); `peters2025hybrid`:36 | si |
| l.64 | CatSim modela espectro, ruido cuantico y electronico, volumen parcial no lineal y dispersion | `deman2007catsim` Abstract, p. 1 | si |
| l.64 | El trabajo preve usar la simulacion fisica como comparacion | `capitulo3.tex`:219-225 (GAPDATO, GAPDEC #90) | si |
| l.66 | Metricas de Peters adoptadas con sus nombres publicados | `peters2025hybrid` Sec. 2.5; #8 APLICADA; `overleaf/CLAUDE.md` terminos fijos; `capitulo3.tex`:213 | si |
| l.66 | *Streak amplitude*: ROI perpendiculares; diferencia entre el promedio del 5 % mas alto y el del 5 % mas bajo de la desviacion respecto de la referencia | `peters2025hybrid`:172-174 (Sec. 2.5, p. 5) | si |
| l.66 | *Bone integrity*: umbral de 150 HU; cambio de volumen y Sorensen-Dice | `peters2025hybrid`:177-178 (Sec. 2.5, pp. 5-6) | si |
| l.66 | *Metal integrity* analoga, con un umbral adaptativo por region | `peters2025hybrid`:181-183, 262 (Sec. 2.5, p. 6) | si |
| l.66 | Disenadas para MAR; el Obj 3 toma la *streak amplitude* como unico criterio primario | `capitulo3.tex`:215, 217; DEC:1265 ("Endpoint primario unico ... streak amplitude") | parcial (T02) |
| l.70 | Zwingmann: solo fracturas Tile y Pennal B y C; B inestable en rotacion, C en rotacion y vertical | `zwingmann2009navigated`:88-90 (M&M, p. 1834; Discussion, p. 1837) | si |
| l.70 | Colocacion percutanea; los grados forman la referencia clinica del Obj 2 | `zwingmann2009navigated`:11; `capitulo3.tex`:79 | parcial (T01: el tipo de tornillo de la referencia no se hace visible) |
| l.72 | Smith: entra por el ilion y llega a S1 o S2; tres corticales (dos del ilion y una del ala) | `smith2006iliosacral`:69 ("through the ileum into either the S1 or S2 vertebrae"; "intended to cross 3 cortices", M&M, p. 235) | si |
| l.72 | El ala sacra desciende lateral y caudal desde el cuerpo vertebral superior | `routt1997`:122 (Sacral Dysmorphism, p. 206) | si |
| l.72 | `\GAPLIT` anatomia pelvica | ni las fichas ni `docs/03-glosario.md` definen los seis terminos; MAPA:79 | si (GAP justificado) |
| l.72 | El transiliosacro cruza ambas articulaciones SI y sale por la tabla externa opuesta | `mclaren2021corridor` M&M, PDF p. 2 | si |
| l.72 | Los dos tipos son no intercambiables; McLaren es transiliosacro; Kaiser fija 10 mm para el tornillo iliosacro | `docs/03-glosario.md`:74-76; `kaiser2014dysmorphism`:72 ("conservative size for passage of an iliosacral screw", p. e120(2)) | si |
| l.72 | La Sec. SAP trata el tornillo como uno que entra y sale por la cortical del ilion | `capitulo3.tex`:196 | si |
| l.72 | `\GAPDEC` tipo de tornillo del corredor medido, con la geometria registrada | #130 ABIERTA (regla 3); `docs/SITUACION_ACTUAL.md`:183; MAPA (fila #130) | parcial (T01) |
| l.74 | Routt: decubito supino y fluoroscopia en tres planos | `routt1997` (Intro, p. 206) | si |
| l.74 | Zwingmann: fluoroscopia "convencional" frente a navegacion 3D con un equipo que rota 190 grados; series navegada y convencional | `zwingmann2009navigated`:103 (M&M, p. 1834); Abstract | si |
| l.74 | Posicion final evaluada en TC posoperatoria | `zwingmann2009navigated`:83 (M&M, p. 1835) | si |
| l.76 | Zona segura en el ala: limites alares y foraminales; L5, canal y vasos iliacos | `routt1997` Fig. 2, p. 207; pp. 212-213 | si |
| l.76 | Gardner: dos conos unidos por la punta; seccion minima en un plano ortogonal | `gardner2010safezones` M&M, p. 623 | si |
| l.76 | La zona segura no es variable; es antecedente del corredor que mide el muestreador | `capitulo3.tex`:168 | si |
| l.78 | McLaren: recta dentro de los contornos; diametro hasta tocar y atravesar la cortical en tres puntos | `mclaren2021corridor` M&M, PDF p. 2 | si |
| l.78 | Umbral de 10 mm en Gardner, Kaiser y McLaren, tomado de trabajos anteriores; McLaren: el minimo no esta establecido | `gardner2010safezones`:71, 303-304; `kaiser2014dysmorphism` p. e120(2); `mclaren2021corridor`; `capitulo3.tex`:89 | si |
| l.78 | Corredor medido sobre mascaras de TotalSegmentator; criterio de viabilidad propio | `capitulo3.tex`:85, 89; `wasserthal2023` | si |
| l.80 | Kaiser: reformateo perpendicular al platillo de S1; angulacion contra crestas y espinas posteriores | `kaiser2014dysmorphism` Fig. 1, p. e120(3); p. e120(2); `capitulo3.tex`:83 | si |
| l.80 | Poses en el marco de Kaiser; localizacion con metal | `capitulo3.tex`:83, 93-95 | si |
| l.82 | Posicion ideal de Smith; tres tipos de perforacion; grados 0-3 con 2 y 4 mm | `smith2006iliosacral` Screw Position, p. 236 | si |
| l.82 | Grado calculado como protrusion fuera de la envolvente osea segmentada | `capitulo3.tex`:189-194, 257 | si |
| l.84 | Escala tomada de los tornillos pediculares, mas una escala angular | `smith2006iliosacral` Screw Position, p. 236 | si |
| l.84 | `\GAPDEC` dimension angular en SAP | #11 ABIERTA; MAPA:41 | si (GAP justificado) |
| l.84 | Zwingmann aplica la escala de perforacion | `zwingmann2009navigated`:230 (M&M, p. 1835; Fig. 4, p. 1836) | si |
| l.84 | Hinsche: definicion binaria (insegura si perfora comprometiendo estructuras) | `hinsche2002fluoroscopy` Measurements, p. 138 | si |
| l.86 | Grados 1 y 2 de 2 mm; grado 3 abierto; equiespaciar es una convencion | demostracion a partir de Smith; `capitulo3.tex`:200, 261 | si |
| l.90 | Revision de la difusion en imagen medica | `kazerouni2023diffusionsurvey` | si |
| l.90 | Ho: cadena de Markov; ruido gaussiano; $n_{\max} = 1000$ | `ho2020denoising` ("We set T = 1000 for all experiments", Sec. 4, p. 5) | si |
| l.90 | Dorjsembe: el proceso directo borra la estructura | `dorjsembe2024` (§II, p. 2) | si |
| l.90-95 | Forma cerrada (Ec. difusion-directa) en DiffBoost y Dorjsembe; las fuentes escriben $\bar\alpha_t$ | `zhang2025diffboost` Ec. 3, p. 3672; `dorjsembe2024` Ec. (1), p. 2 | si |
| l.95 | Nichol y Dhariwal: calendario coseno; varianzas a partir de cocientes sucesivos | `nichol2021improved` Sec. 3.2, p. 8165 | si |
| l.95 | Zhang et al. (DiffBoost): varianzas en (0,1) | `zhang2025diffboost` ("β_t ∈ (0, 1)", Sec. III-A, p. 3672) | si |
| l.97-102 | Prediccion del ruido; objetivo (Ec. perdida) escrito por Rombach; $n$ uniforme | `ho2020denoising`; `rombach2022latentdiffusion` Ec. 1, §3.2, p. 4 | si |
| l.102 | U-Net en Ho y en Song; definicion de Ronneberger | `ho2020denoising`; `song2021ddim` Ap. D.1, p. 16; `ronnenberger2015unet` Que hace | si |
| l.102 | El borrador del sintetizador propone una U-Net, todavia no fijada | `experiments/objetivo3/diseno_A.md`:67-69 (§5 `[SUPUESTO]`); `capitulo3.tex`:172 (`\GAPDEC` arquitectura) | si |
| l.104 | Song: no markoviano, mismo objetivo, determinista, sin reentrenar; 10 a 50 veces mas rapido en tiempo de reloj frente a Ho | `song2021ddim` ("10× to 50× faster in terms of wall-clock time", Resumen, p. 1); :9 | si |
| l.104 | Las tres fuentes evaluan imagenes naturales, sin TC ni metal | `ho2020denoising`, `song2021ddim`, `nichol2021improved`: Restriccion | si |
| l.106 | Rombach: concatenacion o atencion cruzada; Dorjsembe concatena la mascara | `rombach2022latentdiffusion` Fig. 3, p. 4; §4.3.2; `dorjsembe2024` §II, p. 2 | si |
| l.106 | ControlNet: base congelada, copia entrenable del codificador, convoluciones inicializadas en cero | `zhang2023controlnet` §3.1-3.2, pp. 3-4 | si |
| l.108 | LDM en dos etapas; decodificacion en una pasada; perdida perceptual y adversarial; elimina la alta frecuencia; cuello de botella por pixel | `rombach2022latentdiffusion` §1, §3.1-3.2, §5 | si |
| l.108 | 25 HU como exactitud por pixel ("este trabajo lee"); el Obj 1 como condicion; el veredicto negativo descarto la difusion latente y ControlNet | `capitulo3.tex`:58, 71, 75, 174 | si |
| l.110 | RePaint: modelo incondicional; combina las regiones conocida y desconocida; retrocede y avanza en el tiempo | `lugmayr2022repaint` Que hace (p. 11462) | si |
| l.110 | *Inpainting* de Rombach condicionado por concatenacion | `rombach2022latentdiffusion` Tabla 15, p. 25 | si |
| l.110 | Sintetizador: parche con G borrada, mascaras, copia fuera de G | `capitulo3.tex`:172 | si |
| l.110 | LeFusion de Zhang et al. | `zhang2025lefusion` (ficha y `.bib`, primer autor Zhang, Hantao) | si |
| l.110 | `\GAPDEC` muestreo frente a RePaint y LeFusion | #106, #117 ABIERTAS; MAPA:69 | si (GAP justificado) |
| l.112 | 2.5D: cortes axiales con contexto contiguo, sin ser 3D completo | `capitulo3.tex`:172; `diseno_A.md`:60 | si |
| l.112 | `\GAPDEC` numero de cortes (en el borrador, 3 y se genera el central) | `diseno_A.md`:60-61 `[SUPUESTO]`; MAPA:78 | si (GAP justificado) |
| l.112 | Lectura de Glover: los cortes vecinos no reproducen la integracion | `glover1980nonlinear`; marcada con "este trabajo lee" | si |
| l.116 | Tres tipos de resultado; el Obj 1 promedia por paciente; el Obj 3 se parea por paciente | `capitulo3.tex`:71, 223; tabla :242-244 | si |
| l.116 | El Obj 2 reune poses; la referencia cuenta tornillos | `capitulo3.tex`:207, 265 | si |
| l.116 | `\GAPDEC` agregacion por paciente en el Obj 3 | `capitulo3.tex`:223; MAPA:52 | si (GAP justificado) |
| l.118 | W1 = suma de diferencias absolutas de las FDA; unidad, el grado; valores 1 y 3 | `capitulo3.tex`:200-205 (Ec. w1); demostracion | si |
| l.118 | `\GAPLIT` referencia de W1 | ninguna ficha la define; MAPA:76 | si (GAP justificado) |
| l.120 | Superioridad y equivalencia; IC del 90 % entero dentro de $[-\Delta, +\Delta]$ | `capitulo3.tex`:225 | si |
| l.122 | Wilcoxon pareada de una cola; TOST con margen segun la variabilidad del metodo | `capitulo3.tex`:223, 225 | si |
| l.122 | `\GAPDEC` #90 | `capitulo3.tex`:225; MAPA:44 | si (GAP justificado) |
| l.122 | Con muestras pequenas puede no concluir | `capitulo3.tex`:265 | si |
| l.122 | IC del 95 % por remuestreo de pacientes en la compuerta | `capitulo3.tex`:71 | si |
| l.122 | `\GAPLIT` Wilcoxon, TOST y remuestreo | MAPA:77 | si (GAP justificado) |
| l.124 | Regla fijada antes de la prueba que decide; poses y metrica fijadas antes de cualquier distancia | `capitulo3.tex`:58, 231, 253 | si |
| l.124 | Regla fijada tras una exploracion desfavorable que incluia a los pacientes de prueba; tres decisiones post hoc del Obj 2 | `capitulo3.tex`:58, 253, 255 | si |
| l.124 | Seis combinaciones; multiplicidad sin corregir que solo favorece el aprobado; el veredicto fue negativo | `capitulo3.tex`:69, 71, 75, 265 | si |
| l.124 | Extension al latente de Guo et al.: septimo candidato con los mismos pacientes de prueba | `capitulo3.tex`:75, 255, 265 | si |
| l.126 | MAE en HU (Ec. mae); el RMSE nunca es menor que el MAE; el RMSE de MAR sirve como orden de magnitud | `capitulo3.tex`:60-67 | si |

## Comprobacion de patrones VIGENTES (dominio G-T4 / E-R6)
PAT-9: no reincide (2500 HU sigue la decision D1; la U-Net y los tres cortes se presentan como borrador, no como diseno decidido). PAT-19: no reincide en sentido estricto: los GAP de l.46, l.112 y l.110 se cotejaron con `diseno_A.md` y `experiments/` y son correctos. T01 amplia un GAP, no lo invalida. PAT-31: reincide leve (T02). PAT-73: no reincide. PAT-85: no reincide (las lecturas propias llevan "este trabajo lee" o "asume"). PAT-90: no reincide (las cifras de Peters llevan la cita de Peters). PAT-100: no reincide (TOST sobre el IC). PAT-101, PAT-104 y PAT-105: no reinciden. PAT-106: el `\GAPLIT` de l.35 ya cubre la ley. PAT-107: corregido (l.66). PAT-39: no reincide. PAT-103: no reincide ("si toma algo").

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un GAP sobre la correspondencia entre dos poblaciones pregunta solo por una de ellas, aunque la ficha de la otra registra la misma ambiguedad | G-T4, OC-3 | "qué tornillo representa el corredor que mide este trabajo" (sin el tipo de tornillo de Zwingmann) | nuevo |
| Una remision a otro capitulo promete una descripcion que alli esta pendiente (`\GAPDEC`), y se pierde la condicion | G-T4 | "la Sección apariencia describe cómo las usa el Objetivo 3" | PAT-31 |
