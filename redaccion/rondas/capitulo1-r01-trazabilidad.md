# Auditoria de trazabilidad — capitulo1 — r01

Archivo: `overleaf/secciones/capitulo1.tex` (123 lineas). Lint r01: PASA (0/0/0). Respuesta previa: `capitulo1-r00-respuesta.md` (redaccion inicial; no hay RECHAZADOS previos).
Todas las claves citadas existen en `overleaf/referencias.bib` y el apellido nombrado coincide con el primer autor. Ninguna ficha usada dice "Profundidad: solo abstract". Sin contenido retirado (Dice/HD95 como objetivo, "31-60%", BFC/ISC); ControlNet y la ruta latente aparecen como teoria y como descartadas.

**Conteo: alta=1 media=9 baja=5**

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-3 | l.35 | "umbral que este trabajo usa solo para cribar la cohorte" | `docs/01-decisiones.md` 2026-09-11 (3) (#22) y 2026-09-20 (2) D1 (l.1205-1212); `capitulo3.tex` l.73, 87, 119, 178 | La decision posterior D1 fija 2500 HU tambien como umbral de la mascara `M` de entrenamiento, y el cap. 3 lo usa ademas para delimitar el metal de $B_\delta$ en el Obj 1, para la cota del corredor ocupado y para filtrar los componentes del calibre de 4.91 mm. "Solo para cribar" es falso. La respuesta r00 se apoyo solo en #22. Patron PAT-9 reincide (decision posterior que sustituye a la citada) | "umbral que este trabajo usa para cribar la cohorte y, como en el Capitulo~\ref{cap:propuesta}, para delimitar el metal real (Seccion~\ref{sec:datos})" o dar los usos con remision a `sec:sintetizador` |
| T02 | media | E-R6 | l.31 | "Abadi et al. y Wang et al., en su simulacion de implantes cocleares" | fichas `abadi2019` (Que hace; ev. "computed using the Beer-Lambert Law", Sec. II-B); `wang2019cochlear` (ev. "Beer-Lambert law discretized on 5 different energies") | La aposicion "en su simulacion de implantes cocleares" queda compartida por ambos sujetos; DukeSim (Abadi) no simula implantes cocleares ni metal (ficha: "validacion no incluye metal"). Ademas "energia por energia" para Abadi solo consta en el resumen del lector ("polienergetico"), no en la evidencia | "Abadi et al.~\cite{abadi2019}, en el simulador DukeSim, y Wang et al.~\cite{wang2019cochlear}, en su simulacion de implantes cocleares, calculan esa atenuacion con la ley de Beer-Lambert; Wang et al. la discretizan en cinco energias" |
| T03 | media | G-T4 | l.33 | "todo lo que aqui se mide y se genera ocurre en el dominio de imagen" | `capitulo1.tex` l.62; `capitulo3.tex` l.219, l.261 ("el protocolo fisico, que simula y reconstruye el volumen entero") | El protocolo fisico de comparacion genera el artefacto simulando proyecciones; el propio capitulo lo dice en l.62. La generalizacion queda contradicha dentro del capitulo (PAT-39, ERRADICADO, reaparece) | "de modo que lo que este trabajo mide, y lo que genera el sintetizador, ocurre en el dominio de imagen; solo el protocolo fisico de comparacion pasa por proyecciones simuladas" |
| T04 | media | G-T4, OC-3 | l.62 | "usa la simulacion fisica como comparacion" | `capitulo3.tex` l.221 (`\GAPDATO` "implementacion y resultados del protocolo fisico ... no realizados") y l.225 (`\GAPDEC` #90); BITACORA §2 2026-09-30 ("brazo no implementado va en futuro de intencion") | Se afirma en presente y sin la salvedad un brazo no implementado y cuya permanencia esta pendiente de decision (#90). El mismo capitulo lleva el `\GAPDEC` de #90 en l.118, pero no aqui. Patron PAT-31 reincide | "y preve usar la simulacion fisica como comparacion (Seccion~\ref{sec:apariencia})" |
| T05 | media | E-R6 | l.68 | "Un tornillo iliosacro entra por el ilion y termina dentro del sacro \cite{kaiser...}" | ficha `kaiser2014dysmorphism` l.102-104 ("Distincion transsacro vs iliosacro") | La definicion es del lector de la ficha, no una frase de Kaiser et al. registrada como evidencia. La ficha `smith2006iliosacral` si tiene evidencia equivalente: "placed bilaterally through the ileum into either the S1 or S2 vertebrae" (M&M, p. 235) | Citar `smith2006iliosacral` para la definicion ("Smith et al. lo introducen por el ilion hasta el cuerpo de S1 o S2"), o pedir relectura de Kaiser con `lector-papers` para obtener la frase |
| T06 | media | E-R6, G-T4 | l.70 | "Zwingmann et al. comparan esa guia, que llaman convencional" | ficha `zwingmann2009navigated` (ev. "conventional fluoroscopic technique", Abstract; "conventional fluoroscopy (conventional group)", M&M p. 1834); ficha `routt1997` | "Esa guia" identifica la fluoroscopia en tres planos de Routt et al. con la tecnica convencional de Zwingmann et al. La ficha de Zwingmann no describe las vistas de su grupo convencional (solo cita a Matta y Saucedo como tecnica de referencia). Relacion entre fuentes sin respaldo (PAT-73, ERRADICADO, reaparece) | "Zwingmann et al. comparan la guia fluoroscopica, que llaman convencional, con navegacion ..." |
| T07 | media | G-T4, E-R6 | l.91 | "Nichol y Dhariwal ... obtienen ... las varianzas $\beta_n \in (0, 1)$" | ficha `nichol2021improved` (Ec. 16; "clip βt to be no larger than 0.999", Sec. 3.2); ficha `zhang2025diffboost` ("β_t ∈ (0, 1) represents the variance schedule", Sec. III-A, p. 3672) | El intervalo $(0,1)$ sale de DiffBoost (fila 94 de la respuesta r00), pero la oracion solo cita a Nichol y Dhariwal. Patron PAT-90 reincide | "obtienen, de sus cocientes sucesivos, las varianzas $\beta_n$ de cada paso, que Zhang et al. acotan en $(0,1)$" o quitar el intervalo |
| T08 | media | G-T4 | l.112 | "En los Objetivos 1 y 3 ... el error se promedia por paciente" | `capitulo3.tex` l.223 (`\GAPDEC{como se agregan por paciente las poses y las regiones de medicion de rayas antes de las pruebas}`) | Para el Obj 3 la agregacion por paciente no esta fijada; el cap. 3 la marca con GAP y aqui entra como hecho. Patron PAT-31 reincide | "En el Objetivo 1 el error se promedia por paciente; en el Objetivo 3 las pruebas se parean por paciente, y como se agregan las poses antes de ellas esta pendiente" + mismo `\GAPDEC` |
| T09 | media | G-T4 | l.116 | "la equivalencia solo se concluye cuando la diferencia pareada cae dentro de un margen" | `capitulo3.tex` l.225 ("solo si el IC del 90 % de la diferencia pareada cae entero dentro de un margen") | El criterio es sobre el intervalo de confianza del 90 %, no sobre la diferencia (puntual). Tal como esta, describe un criterio distinto y mas debil que el del metodo | "solo se concluye cuando el intervalo de confianza del 90\,\% de la diferencia pareada cae entero dentro de un margen ..." |
| T10 | media | G-T4, OC-3 | l.120 | "La compuerta fijo su regla antes de correr la prueba que decide, y el muestreador fijo ..." | `capitulo3.tex` l.58 ("La regla se fijo ... conociendo un resultado exploratorio desfavorable"), l.253 (tres decisiones tomadas despues de ver datos), l.255, l.209 (analisis post hoc) | La oracion presenta la proteccion contra el ajuste como completa y omite las salvedades del propio metodo: la regla de la compuerta se fijo tras una exploracion que incluia a los pacientes de prueba, y en el Obj 2 hubo tres decisiones posteriores a ver datos y una estratificacion post hoc. Patron PAT-31 reincide (la condicion se pierde al retomar la cifra/hecho) | Agregar una oracion: "En ambos casos hubo decisiones posteriores a ver datos, que el Capitulo~\ref{cap:propuesta} enumera (Seccion~\ref{sec:amenazas})" |
| T11 | baja | G-T4 | l.35 | "define el hueso como los voxeles sobre 150 HU \cite{peters2025hybrid}" | ficha `peters2025hybrid` l.177 ("above 150 HU, excluding those in the metal ground truth geometry") | Falta la exclusion de la geometria metalica, que el cap. 3 (l.213) si da | "como los voxeles sobre 150~HU fuera de la geometria metalica" |
| T12 | baja | G-T4 | l.35 | "en la cohorte local, una parte del interior del sacro queda bajo 150 HU" | `capitulo3.tex` l.85 ("a lo largo del eje del corredor ..., la mediana de la fraccion de voxeles a 150 HU o menos dentro de las mascaras sacras fue 0.42") | La medicion es a lo largo del eje del corredor y "a 150 HU o menos", no "el interior del sacro" ni "bajo"; perdida de condicion menor | "a lo largo del eje del corredor, una fraccion de los voxeles de las mascaras sacras queda a 150~HU o menos (Seccion~\ref{sec:corredor})" |
| T13 | baja | E-R6 | l.74 | "Los dos primeros lo atribuyen a trabajos previos, y McLaren et al. declaran ..." | ficha `mclaren2021corridor` l.130 ("Kaiser et al. recommended 10 mm or greater"); ficha `gardner2010safezones` l.24 ("A safe zone dimension of 10 mm") | McLaren et al. tambien lo atribuyen (a Kaiser et al.); y el 10 mm de Gardner et al. se aplica a la dimension de la seccion de la zona segura, no al diametro maximo de McLaren ("ese tamano") | "Los tres lo toman de trabajos anteriores, y McLaren et al. declaran ademas que el corredor minimo no esta establecido"; "emplean un umbral de 10~mm sobre el tamano del corredor" |
| T14 | baja | G-T4 | l.104 | "por eso el Objetivo 1 midio la ida y vuelta ... antes de adoptar la ruta latente" | `capitulo3.tex` l.20, l.174 (veredicto negativo; ruta latente descartada) | "Antes de adoptar" sugiere que la ruta se adopto; el veredicto la descarto. El mismo capitulo (l.102) ya dice que "cayo" | "como condicion para adoptar la ruta latente, que el veredicto negativo descarto (Seccion~\ref{sec:obj1})" |
| T15 | baja | G-T4 | l.80 | "Otras fuentes usan definiciones binarias" | ficha `hinsche2002fluoroscopy` (unica citada) | Plural sostenido por una sola cita | "Hinsche et al. ... usan una definicion binaria" (quitar "Otras fuentes") o anadir las demas fichas con su `\cite` |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.11-13 | Funcion del capitulo, orden de secciones, remisiones | estructura propia; `\ref` existentes (lint PASA) | si |
| fig. 1.1 | Grupo de conceptos -> pieza (Obj 1-4, SAP, protocolo fisico) | `capitulo3.tex` l.20-29, tabla de diseno l.242-244 | si |
| l.31 | Lectura del detector = indice del sinograma | `deman2007catsim`: "y_i is the detector signal at sinogram index i" (Sec. 2.1, p. 1) | si |
| l.31 | Senal = suma sobre energias de fotones sin atenuador atenuados por longitud | `deman2007catsim`: defs. A_ik, l_iso, mu_ok (Sec. 2.1, p. 1) | si |
| l.31 | Coef. de atenuacion lineal por material y energia | `deman2007catsim`: "mu_ok is the linear attenuation coefficient of object o at energy k" | si |
| l.31 | Abadi y Wang: Beer-Lambert energia por energia | `abadi2019` Sec. II-B; `wang2019cochlear` Introduccion p. 2 | no (T02) |
| l.33 | FBP en De Man 1999, CatSim y Karageorgos | `deman1999` "direct fan-beam filtered backprojection" (Sec. II-C); `deman2007catsim` "reconstructing using FBP" (Sec. 3.1); `karageorgos2024ddpm` "reconstructed with filtered back-projection" (Sec. II-F) | si |
| l.33 | FBP supone modelo monocromatico de Radon; desvio no lineal policromatico | `park2015ct`: Que hace | si |
| l.33 | Cohorte solo con volumenes reconstruidos | `capitulo3.tex` §Datos; `docs/02-datos.md` | si |
| l.33 | Todo lo medido y generado, en dominio de imagen | contradicho por l.62 y `capitulo3.tex` l.261 | no (T03) |
| l.35 | Agua 0 HU, aire -1000 HU por definicion | `wu2022xcist`: "defined as 0 HU"; "-1000 HU by definition" (Discussion Exp.1, p.13) | si |
| l.35 | Conversion HU-mu con coef. del agua por energia | `wang2019cochlear`: "Hounsfield unit formula and the water absorption coefficients" (Sec. 2.1, p. 4) | si |
| l.35 | `\GAPLIT` fuente de fisica de TC (HU, FBP) | ninguna ficha define la escala como transformacion de mu; MAPA l.75 | si (GAP justificado) |
| l.35 | Hueso > 150 HU (Peters) | `peters2025hybrid` l.177 | parcial (T11) |
| l.35 | Metal clinico segmentado con 2500 HU (Wang, Li) | `wang2025adaptiveweighting` Sec. V-A-2, p. 2413; `li2024` Sec. IV-E, p. 1878 | si |
| l.35 | 2500 HU "solo para cribar" | DEC 2026-09-20 (2) D1; `capitulo3.tex` l.73, 87, 119, 178 | no (T01) |
| l.35 | Parte del sacro bajo 150 HU en la cohorte | `capitulo3.tex` l.85 (mediana 0.42) | parcial (T12) |
| l.37-41 | Ventana: saturar a [w_min, w_max] y escalar a [0,1] (Ec. ventana) | `wang2025adaptiveweighting`: "Ynorm = (Yclamp − L)/(H − L)" (Eq. 2, p. 2410) | si |
| l.42 | Saturacion; fraccion inversamente proporcional al ancho | demostracion desde Ec. ventana | si |
| l.44 | Tres ventanas [-1000,2000], [-320,480], [-160,240] HU; cascada, no canales | `wang2025adaptiveweighting` Sec. V-A-1, p. 2412; Fig. 1 / Sec. III, p. 2410 | si |
| l.44 | Techo 2000 < 2500: el metal satura | derivacion de las dos cifras anteriores | si |
| l.44 | Variantes del Obj 1: techo elevado y arcoseno hiperbolico | `capitulo3.tex` l.69 | si |
| l.44 | Compuerta mide MAE dentro del hueso (Ec. mae) | `capitulo3.tex` l.60-65 | si |
| l.48 | Rayas claras y oscuras que ocultan anatomia | `selles2024marreview`: "bright and dark streaking artifacts that disguise anatomical structures" (Sec. 1, p. 1) | si |
| l.48 | Severidad por tamano, forma y aleacion | `selles2024marreview` (Sec. 1, p. 1) | si |
| l.48 | Osteosintesis "Medium", cualitativa, sin criterio numerico | `selles2024marreview` Tabla 1, p. 6; criterio numerico NO ENCONTRADO | si |
| l.50 | Cuatro contribuyentes principales segun Selles | `selles2024marreview`: "Beam hardening, photon starvation, scattering and edge effects are the main contributors" | si |
| l.50 | De Man: simulacion 2D; mas importantes BH, scatter, ruido, EEGE | `deman1999` Conclusiones, p. 695; Sec. II-A, p. 691 | si |
| l.50 | Todas las causas producen rayas; sin peso numerico | `deman1999` Conclusiones, p. 695; "Contribucion relativa numerica: NO ENCONTRADO" | si |
| l.50 | Sin termino "photon starvation"; ruido como artefacto no lineal | `deman1999` Respuestas 1; Sec. III-E, p. 694 | si |
| l.52 | BH: absorcion preferente de baja energia, espectro hacia arriba | `selles2024marreview` Sec. 1, p. 1 (dos filas) | si |
| l.52 | Park: BH = discrepancia no lineal; cupping dentro, rayas fuera | `park2015ct`: Que hace; Donde entra ("outside the problematic region", Introduccion, p. 2) | si |
| l.52 | De Man: rayas oscuras en direcciones de mayor atenuacion; rayas que conectan metales | `deman1999` Sec. III-B, p. 693 | si |
| l.54 | Inanicion: muy pocos fotones; faltan datos de proyeccion | `selles2024marreview` Sec. 1, p. 1 | si |
| l.54 | Ruido de De Man: lineas finas alternas; depende de atenuacion integrada | `deman1999` Sec. III-E, p. 694 | si |
| l.54 | Dispersion por densidad electronica | `selles2024marreview` Sec. 1, p. 1 | si |
| l.54 | Razon de dispersion muy pequena produce rayas | `deman1999`: "Even a very small scatter-to-primary ratio causes significant streaks" (Sec. III-C) | si |
| l.56 | EEGE: rayas tangentes a bordes rectos largos; rayas que irradian | `deman1999` Sec. III-D, p. 694 | si |
| l.56 | Selles: rayas alineadas con el borde | `selles2024marreview`: "dark or bright streaks in line with the edge of the metal" | si |
| l.56 | Ninguna descripcion da distancia; De Man no mide extension | `deman1999` Respuestas 2 (NO ENCONTRADO); `selles2024marreview` extension NO ENCONTRADO | si |
| l.58 | Volumen parcial no lineal: variacion axial, log del flujo integrado | `glover1980nonlinear`: Que hace | si |
| l.58 | Una discontinuidad local; dos o mas, rayas de largo alcance | `glover1980nonlinear`: Donde entra (Sec. II, pp. 240-243) | si |
| l.58 | Hueso, fuente monocromatica, sin metal | `glover1980nonlinear`: Restriccion | si |
| l.58 | De Man en 2D sin volumen parcial axial | `deman1999`: "axial partial volume effects [16] are beyond the scope" (Sec. II-A) | si |
| l.60 | Rayas fuera del metal | `deman1999` Sec. III-B/D; `park2015ct` Introduccion, p. 2 | si |
| l.60 | Ancho de $B_\delta$ como convencion | `capitulo2.tex` §Representacion; #57/#98 ABIERTAS, no afirmado como resuelto | si |
| l.60 | De Man aisla causas modificando el sinograma | `deman1999` Sec. II-D, p. 693 | si |
| l.60 | Supuesto del dominio de imagen con remision a amenazas | `capitulo3.tex` l.261; #61/#63 ABIERTAS tratadas como supuesto | si |
| l.62 | CatSim en XCIST; protocolo de Peters sobre CatSim | `wu2022xcist` ("new implementation of CatSim", Simulation p.6); `peters2025hybrid` ("modelled in the CatSim CT simulator within ... XCIST", Abstract) | si |
| l.62 | CatSim modela espectro, ruido cuantico y electronico, VP no lineal, dispersion | `deman2007catsim` Abstract, p. 1 (tres filas) | si |
| l.62 | De Man et al. reconstruyen con FBP | `deman2007catsim` Sec. 3.1, p. 5 | si |
| l.62 | Este trabajo usa la simulacion fisica como comparacion | `capitulo3.tex` l.221 (GAPDATO), l.225 (GAPDEC #90) | no (T04) |
| l.66 | Solo fracturas Tile y Pennal B y C | `zwingmann2009navigated` M&M, p. 1834 | si |
| l.66 | B inestable rotacional; C rotacional y vertical | `zwingmann2009navigated` Discussion, p. 1837 | si |
| l.66 | Percutanea, guiada por imagen; grados = referencia clinica del Obj 2 | `zwingmann2009navigated` Que hace; `capitulo3.tex` l.79 | si |
| l.68 | Iliosacro entra por ilion y termina en el sacro (Kaiser) | `kaiser2014dysmorphism` l.104 (texto del lector) | no (T05) |
| l.68 | Tres corticales: dos del ilion, una del ala | `smith2006iliosacral`: "intended to cross 3 cortices (2 ileum, 1 sacral ala)" (M&M, p. 235) | si |
| l.68 | Transiliosacro cruza ambas SI y sale por tabla externa opuesta | `mclaren2021corridor` M&M, PDF p. 2 (dos filas) | si |
| l.70 | Routt: supino, fluoroscopia en tres planos | `routt1997`: "in the supine position using triplanar fluoroscopy" (Introduccion, p.206) | si |
| l.70 | Zwingmann compara "esa guia" (convencional) con navegacion | `zwingmann2009navigated` (no describe vistas del grupo convencional) | no (T06) |
| l.70 | Equipo que rota 190 grados | `zwingmann2009navigated`: "which rotates 190° around the operative field" (M&M, p. 1834) | si |
| l.70 | Posicion final evaluada en TC posoperatoria | `zwingmann2009navigated` M&M, p. 1835 | si |
| l.72 | Zona segura: limites alares y foraminales | `routt1997` Fig. 2, p. 207 (dos filas) | si |
| l.72 | L5 sobre el ala, canal, vasos iliacos anteriores | `routt1997` pp. 207, 212-213 | si |
| l.72 | Dos conos punta a punta; seccion minima en plano ortogonal al eje | `gardner2010safezones` M&M, p. 623 (dos filas) | si |
| l.74 | Recta dentro de contornos; diametro aumentado hasta romper la cortical en al menos tres puntos | `mclaren2021corridor` M&M, PDF p. 2 (l.144-149) | si |
| l.74 | 10 mm en Gardner, Kaiser y McLaren | `gardner2010safezones` p. 624; `kaiser2014dysmorphism` p. e120(2), e120(7); `mclaren2021corridor` PDF p. 2 | si |
| l.74 | Atribucion a terceros (solo Gardner y Kaiser); "no establecido" (McLaren) | idem; McLaren tambien atribuye a Kaiser | parcial (T13) |
| l.74 | Criterio de viabilidad en lugar del umbral | `capitulo3.tex` l.89 | si |
| l.76 | Reformateo por el eje sacro perpendicular a S1 | `kaiser2014dysmorphism`: Fig. 1, pie, p. e120(3) | si |
| l.76 | Angulacion contra crestas iliacas y espinas posteriores | `kaiser2014dysmorphism` p. e120(2) (dos filas) | si |
| l.76 | Poses en el marco de Kaiser; aplicabilidad con metal | `capitulo3.tex` l.83, l.93-95 | si |
| l.78 | Posicion ideal de Smith | `smith2006iliosacral` Screw Position, p. 236 (dos filas) | si |
| l.78 | Tres tipos de perforacion | `smith2006iliosacral` Screw Position, p. 236 (tres filas) | si |
| l.78 | Grados 0-3 con 2 y 4 mm | `smith2006iliosacral` Screw Position, p. 236 (cuatro filas) | si |
| l.80 | Escala tomada de tornillos pediculares; escala angular | `smith2006iliosacral` Screw Position, p. 236 | si |
| l.80 | `\GAPDEC` dimension angular en SAP | #11 ABIERTA; sin decision en `01-decisiones.md`; MAPA l.41 | si (GAP justificado) |
| l.80 | Zwingmann aplica la escala en TC posoperatoria y reporta por tecnica | `zwingmann2009navigated` M&M, p. 1835; Results, pp. 1836-1837 | si |
| l.80 | "Otras fuentes" binarias; Hinsche: insegura si perfora comprometiendo estructuras | `hinsche2002fluoroscopy` Measurements, p. 138 | parcial (T15) |
| l.82 | Grados 1 y 2 de 2 mm; grado 3 abierto; equiespaciado es convencion | demostracion desde los limites de Smith; `capitulo3.tex` l.261 | si |
| l.86 | Difusion en imagen medica | `kazerouni2023diffusionsurvey` | si |
| l.86 | Cadena de Markov que invierte ruido gaussiano; T = 1000 | `ho2020denoising`: Que hace; "We set T = 1000 for all experiments" (Sec. 4, p. 5) | si |
| l.86 | Proposito del proceso directo: borrar la estructura | `dorjsembe2024`: "entirely erase the original data structure" (§II, p. 2) | si |
| l.86-90 | Forma cerrada (Ec. difusion-directa) en DiffBoost y Dorjsembe | `zhang2025diffboost` Ec. 3, p. 3672; `dorjsembe2024` Ec. (1), p. 2 | si |
| l.91 | Fuentes escriben $\bar\alpha_t$ | idem; `nichol2021improved` Ec. 16 | si |
| l.91 | Calendario coseno; beta de cocientes sucesivos | `nichol2021improved` Sec. 3.2, p. 8165 | si |
| l.91 | $\beta_n \in (0,1)$ atribuido a Nichol y Dhariwal | `zhang2025diffboost` Sec. III-A, p. 3672 (otra fuente) | no (T07) |
| l.93-97 | Prediccion del ruido; objetivo (Ec. perdida); t uniforme | `ho2020denoising` Que hace; `rombach2022latentdiffusion` Ec. 1 y "t uniformly sampled" (§3.2, p. 4) | si |
| l.98 | Red U-Net en Ho y Song | `ho2020denoising` Restriccion; `song2021ddim` Restriccion (Ap. D.1, p. 16) | si |
| l.98 | U-Net: rutas contractiva y expansiva simetricas | `ronnenberger2015unet`: Que hace | si |
| l.100 | Song: no markoviano, mismo objetivo, determinista, menos pasos sin reentrenar | `song2021ddim`: Que hace | si |
| l.100 | 10 a 50 veces mas rapido en tiempo de reloj | `song2021ddim`: "10× to 50× faster in terms of wall-clock time" (Resumen, p. 1) | si |
| l.100 | Las tres en imagenes naturales, sin TC ni metal | `ho2020denoising`, `song2021ddim`, `nichol2021improved`: Restriccion | si |
| l.102 | Rombach: concatenacion (alineada) o atencion cruzada | `rombach2022latentdiffusion` Fig. 3, p. 4; §4.3.2, p. 7 | si |
| l.102 | Dorjsembe: mascara concatenada por canal en cada paso | `dorjsembe2024` §II, p. 2 | si |
| l.102 | ControlNet: base congelada, copia del codificador, convoluciones en cero | `zhang2023controlnet` §3.1, p. 4; Fig. 2, p. 3; §3.2, p. 4 | si |
| l.102 | Presupone base congelada y su latente; cayo con la ruta latente | `zhang2023controlnet` Restriccion; `capitulo3.tex` l.174 | si |
| l.104 | Dos etapas; latente de menor resolucion; decodificacion en una pasada | `rombach2022latentdiffusion` §3.2, p. 4 | si |
| l.104 | Perdida perceptual + adversarial contra el desenfoque | `rombach2022latentdiffusion` §3.1, p. 3 | si |
| l.104 | Compresion elimina alta frecuencia | `rombach2022latentdiffusion` §1, p. 2 | si |
| l.104 | Cuello de botella en exactitud por pixel | `rombach2022latentdiffusion` §5, p. 9 | si |
| l.104 | 25 HU; Obj 1 "antes de adoptar la ruta latente" | `capitulo3.tex` l.67-71, l.174 | parcial (T14) |
| l.106 | RePaint: modelo incondicional; combina conocida/desconocida; avanza y retrocede | `lugmayr2022repaint`: Que hace; Donde entra ("goes forward and backward in diffusion time", p. 11462) | si |
| l.106 | Inpainting de Rombach por concatenacion | `rombach2022latentdiffusion` Tabla 15, p. 25 | si |
| l.106 | Sintetizador: parche con G borrada, mascaras, copia fuera de G | `capitulo3.tex` l.172 | si |
| l.106 | `\GAPDEC` muestreo frente a RePaint y LeFusion | #106, #117 ABIERTAS; MAPA l.69 | si (GAP justificado) |
| l.108 | 2.5D: cortes axiales con contexto contiguo; sin ser 3D | `capitulo3.tex` l.172; `experiments/objetivo3/diseno_A.md` l.60-61 | si |
| l.108 | `\GAPDEC` numero de cortes (borrador: 3, central) | `diseno_A.md` l.60-61 `[SUPUESTO]`; MAPA l.78 | si (GAP justificado) |
| l.108 | Lectura de Glover: cortes vecinos no reproducen la integracion | `glover1980nonlinear` Donde entra; redactado como "este trabajo lee" | si |
| l.112 | Tres tipos de resultado por objetivo | `capitulo3.tex` tabla l.242-244 | si |
| l.112 | Obj 1 y 3: error promediado y pruebas pareadas por paciente | `capitulo3.tex` l.71, l.223 (GAPDEC sobre agregacion en Obj 3) | no (T08) |
| l.112 | Obj 2 reune poses; referencia cuenta tornillos | `capitulo3.tex` l.207, l.265 | si |
| l.114 | W1 = suma de diferencias de FDA; unidad grado | `capitulo3.tex` l.200-205 (Ec. w1) | si |
| l.114 | Valores 1 y 3; misma fraccion de grado 0 con distancia distinta | demostracion desde Ec. w1 | si |
| l.114 | `\GAPLIT` referencia de W1 | ninguna ficha la define (solo usos); MAPA l.76 | si (GAP justificado) |
| l.116 | Superioridad vs equivalencia; no significativa no prueba equivalencia | `capitulo3.tex` l.225 | si |
| l.116 | Equivalencia si "la diferencia pareada" cae en el margen | `capitulo3.tex` l.225 (IC 90 %) | no (T09) |
| l.118 | Wilcoxon pareada de una cola | `capitulo3.tex` l.223 | si |
| l.118 | TOST con margen por variabilidad del metodo | `capitulo3.tex` l.225 | si |
| l.118 | `\GAPDEC` #90 | `capitulo3.tex` l.225; MAPA l.44 | si (GAP justificado) |
| l.118 | Muestras pequenas: puede no concluir | `capitulo3.tex` l.265 | si |
| l.118 | `\GAPLIT` Wilcoxon, TOST, IC por remuestreo | solo usos por terceros en fichas; MAPA l.77 | si (GAP justificado) |
| l.120 | IC 95 % por remuestreo de pacientes en la compuerta | `capitulo3.tex` l.71 | si |
| l.120 | Multiplicidad no corregida solo favorece el aprobado | `capitulo3.tex` l.265 | si |
| l.120 | Regla de la compuerta y distribucion del muestreador fijadas antes | `capitulo3.tex` l.58, l.127 (correcto) pero omite l.58 final, l.253, l.255, l.209 | parcial (T10) |
| l.122 | MAE en HU (Ec. mae); RMSE nunca menor que MAE; RMSE de MAR como orden de magnitud | `capitulo3.tex` l.60-67 | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Uso de un parametro descrito segun una decision anterior cuando una posterior lo amplio | G-T4, OC-3 | "umbral que este trabajo usa solo para cribar la cohorte" | PAT-9 (ERRADICADO, reaparece) |
| Salvedad o GAP del metodo perdido al resumirlo en otro capitulo (brazo no implementado, agregacion pendiente, decisiones post hoc) | G-T4, OC-3 | "usa la simulacion fisica como comparacion"; "el error se promedia por paciente" | PAT-31 |
| Cifra de la fuente A en una oracion que solo cita a la fuente B | G-T4, E-R6 | "Nichol y Dhariwal ... las varianzas $\beta_n \in (0,1)$" | PAT-90 |
| Una tecnica de una fuente se identifica con la de otra ("esa guia") sin respaldo en las fichas | E-R6, G-T4 | "Routt ... tres planos. Zwingmann et al. comparan esa guia" | PAT-73 (ERRADICADO, reaparece) |
| Aposicion compartida por dos sujetos que solo vale para uno | E-R6 | "Abadi et al. y Wang et al., en su simulacion de implantes cocleares" | nuevo |
| Definicion atribuida a un autor cuando en la ficha es texto del lector, no evidencia | E-R6 | "Un tornillo iliosacro ... termina dentro del sacro \cite{kaiser2014dysmorphism}" | nuevo |
| Criterio estadistico resumido sobre el estimador puntual cuando el metodo lo define sobre el intervalo | G-T4 | "cuando la diferencia pareada cae dentro de un margen" | nuevo |
| Generalizacion de alcance ("todo lo que ...") que el propio capitulo contradice | G-T4, E-P3 | "todo lo que aqui se mide y se genera ocurre en el dominio de imagen" | PAT-39 (ERRADICADO, reaparece) |
