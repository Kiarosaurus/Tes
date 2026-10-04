# Auditoria de trazabilidad — capitulo1 — r04

Archivo: `overleaf/secciones/capitulo1.tex` (129 lineas). Lint r04: PASA (0/0/0; GAP lit 4 / dato 1 / dec 8).
Respuesta previa: `capitulo1-r03-respuesta.md` (9 altos/medios aplicados, 0 rechazados; guia-1 no aplicado). No hay RECHAZADOS de trazabilidad que respetar.
Correcciones de trazabilidad de r03 verificadas en el texto: T01 (l.72, el `\GAPDEC` ya incluye el tipo de tornillo de la referencia clinica, ficha `zwingmann2009navigated`:79, :83, :197; MAPA:81 anota la discrepancia con #130.3) y T02 (l.66, "su uso para evaluar síntesis exige invertirlas", `capitulo3.tex`:215). Las dos estan aplicadas.
Contenido nuevo de r03 rastreado: mediana 0.42 (l.35), definicion de la codificacion multiventana (l.44), razon de dispersion "elegida de forma arbitraria" (l.54), acoplamiento ruido-dispersion-endurecimiento (l.56), negativo sobre De Man (l.58), "imagen sin metal del mismo caso" (l.66), margen de 5 mm y holgura de 1 a 2 mm de Kaiser (l.80), Hinsche (l.84), parrafo de Arand y fraccion por zona de densidad (l.88), borrador del muestreo (l.106), `\GAPLIT` ampliado (l.124), extension a Guo et al. (l.126).
Claves: todas existen en `overleaf/referencias.bib` (incluida la nueva en el capitulo, `arand2019pelvicring`, primer autor Arand). Cada apellido nombrado coincide con el primer autor. Ninguna cita es sujeto gramatical sola. No hay fuentes de fabricante.
Contenido retirado: no aparecen Dice/HD95 como objetivo (Sorensen-Dice de l.66 es componente publicado de *bone integrity*), ni "31-60 %", ni BFC/ISC. Difusion latente y ControlNet solo como teoria y como descartadas (l.110).

**Conteo: alta=0 media=0 baja=3**

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | baja | G-T4 | l.35, ultimas dos oraciones | "En la cohorte local ... la mediana ... fue 0.42 ... dejaría fuera esa fracción" | `capitulo3.tex`:85; `tesis/main.tex`:123; `experiments/objetivo2/maintex_cifras.md`:17 (fila 10, "Fraccion del eje <= 150 HU (6 mm)", recorte `default6mm`) | La cifra coincide (0.42), pero pierde dos condiciones de su fuente: es la cohorte primaria con el recorte por defecto (no "la cohorte local" en general, que en el documento tiene varios recuentos), y el cap. 3 dice que un hueso por umbral dejaria fuera "en la mediana" esa fraccion; sin "en la mediana", la segunda oracion la presenta como valor de cada caso (PAT-31 reincide, leve) | "En la cohorte primaria, con el recorte por defecto, la mediana de la fracción de vóxeles sacros a 150~HU o menos fue 0.42 a lo largo del eje del corredor más ancho. Un hueso definido por ese umbral dejaría fuera, en la mediana, esa fracción del corredor (Sección~\ref{sec:corredor})." |
| T02 | baja | G-T4 | l.124, segunda oracion | "con un margen fijado por la variabilidad entre semillas ... y entre corridas repetidas" | `capitulo3.tex`:172 (`\GAPDEC` incluye "margen de equivalencia"), :225 (`\GAPDEC` "qué cambia entre dos corridas repetidas"), :231 ("el margen $\Delta$ queda pendiente de preinscripción"), :265 (3 pacientes de validacion) | "Fijado" se lee como margen ya fijado; el cap. 3 fija solo su definicion y deja el valor pendiente de preinscripcion, con una de sus dos componentes sin definir. La remision a `sec:apariencia` no basta para recuperar la condicion (PAT-31 reincide, leve) | "... con un margen definido por la variabilidad entre semillas del sintetizador y entre corridas repetidas del protocolo físico, y aún sin preinscribir (Sección~\ref{sec:apariencia})" |
| T03 | baja | G-T4, E-M4 | l.126, ultimas dos oraciones | "lo que eleva a siete las combinaciones que pueden aprobar. El veredicto ... en resultados" | `capitulo3.tex`:75, :255, :265; `docs/04-implicancias.md` #93 (CERRADA: la extension se decide por una cota de saturacion calculada sin modelo sobre los 34 de prueba); BITACORA §2 2026-09-29 (veredictos al cap. 4) | Respetando la decision de §2 (el veredicto va al cap. 4), el parrafo deja el recuento en siete sin decir que se sigue: la oracion previa concluye que la multiplicidad no compromete el veredicto porque fue negativo, y esa conclusion solo cubre seis combinaciones. El lector no sabe si con siete se sostiene (PAT-52, debilidad sin su consecuencia) | "... lo que eleva a siete las combinaciones que pueden aprobar. El veredicto de esa extensión, y con él si la multiplicidad de siete combinaciones compromete el de la compuerta, se presenta en el capítulo de resultados (Sección~\ref{sec:amenazas})." |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.11 | Funcion del capitulo; reparto con los caps. 2 y 3 | estructura propia; `\ref` existen (lint PASA) | si |
| l.13 | Orden de las secciones; el muestreador precede al sintetizador | `capitulo3.tex`:21-33 (Fig. `fig:pipeline`) | si |
| l.13 | Pieza que usa cada seccion | `capitulo3.tex`:13, 20-31, 69, 79, 172, 189 | si |
| fig. 1.1 | Conceptos -> Obj 1, 2, 3, 4 y protocolo fisico | `capitulo3.tex`:13, 20-31, 172, 189, 213, 219 | si |
| l.31 | Lectura del detector = indice del sinograma | `deman2007catsim` (Sec. 2.1, p. 1) | si |
| l.31 | Senal = suma sobre energias, atenuada segun longitud por material | `deman2007catsim` Sec. 2.1, p. 1 | si |
| l.31 | Coeficiente de atenuacion lineal por material y energia | `deman2007catsim` ("mu_ok is the linear attenuation coefficient") | si |
| l.31 | Abadi (DukeSim): Beer-Lambert | `abadi2019`:51 (Sec. II-B, p. 1458) | si |
| l.31 | Wang (cocleares): Beer-Lambert en cinco energias | `wang2019cochlear`:52, 56 (Intro, p. 2) | si |
| l.33 | FBP en De Man 1999, CatSim y Karageorgos | `deman1999` Sec. II-C; `deman2007catsim` Sec. 3.1; `karageorgos2024ddpm` Sec. II-F | si |
| l.33 | Park: FBP supone el modelo monocromatico de Radon | `park2015ct`:9 | si |
| l.33 | Cohorte solo con volumenes reconstruidos; medido y generado en dominio de imagen; protocolo fisico previsto | `capitulo3.tex`:42-46, 172, 219-221, 261; `docs/02-datos.md` | si |
| l.35 | Agua 0 HU, aire -1000 HU | `wu2022xcist` (Discussion Exp. 1, p. 13) | si |
| l.35 | Conversion HU-mu con el coeficiente del agua | `wang2019cochlear` (Sec. 2.1, p. 4) | si |
| l.35 | `\GAPLIT` fisica de TC | MAPA:75; `_candidatos.md` | si (GAP justificado) |
| l.35 | Hueso > 150 HU fuera del metal (Peters) | `peters2025hybrid`:177 (Sec. 2.5, p. 5) | si |
| l.35 | Wang y Li: metal clinico con 2500 HU; uso propio para cribar y delimitar | `wang2025adaptiveweighting`:110, 186; `li2024` Sec. IV-E; `capitulo3.tex`:73, 87, 178; DEC 2026-09-20 (2) D1 | si |
| l.35 | Mediana 0.42 de voxeles sacros a <=150 HU a lo largo del eje | `capitulo3.tex`:85; `tesis/main.tex`:123; `maintex_cifras.md`:17 (COINCIDE) | parcial (T01: sin cohorte, recorte ni "en la mediana") |
| l.37-42 | Ventana (Ec. ventana) | `wang2025adaptiveweighting`:112, 184 (Eq. 2, p. 2410) | si |
| l.42 | Saturacion; fraccion inversamente proporcional al ancho | demostracion desde la Ec. ventana | si |
| l.44 | Definicion de la codificacion multiventana (anchas: rango; estrechas: contraste) | demostracion desde l.42; `overleaf/CLAUDE.md` terminos fijos | si |
| l.44 | Tres ventanas de Wang en cascada, no como canales | `wang2025adaptiveweighting`:108 (Sec. V-A-1, p. 2412) | si |
| l.44 | Ida y vuelta y su error | `capitulo3.tex`:58, 65 | si |
| l.46 | Tres codificaciones del Obj 1; techo 2000 < 2500 HU; 20 000 HU; arcoseno sobre [-1000, 20 000] HU | `capitulo3.tex`:69, 71; `tesis/main.tex`:77; DEC 2026-09-17 | si |
| l.46 | `\GAPDATO` forma del arcoseno hiperbolico | MAPA:80 (solo en `src/common/ventanas.py`) | si (GAP justificado) |
| l.46 | Compuerta mide MAE en hueso; sintetizador usa la codificacion sin autoencoder | `capitulo3.tex`:60-65, 172 | si |
| l.46 | `\GAPDEC` codificacion y precision del sintetizador | MAPA:40 (texto del cap. 2, cotejado con `experiments/`) | si (GAP justificado) |
| l.50 | Selles: rayas claras y oscuras; severidad por tamano, forma, aleacion; osteosintesis intermedia, cualitativa | `selles2024marreview` Sec. 1, p. 1; Tabla 1, p. 6 | si |
| l.52 | Listas de causas de Selles y De Man; todas producen rayas; sin peso numerico | `selles2024marreview`:37; `deman1999`:69-79, :161 (Conclusiones, p. 695) | si |
| l.54 | BH: absorcion preferente de baja energia | `selles2024marreview` Sec. 1, p. 1 | si |
| l.54 | Park: *cupping* y rayas fuera | `park2015ct`:9 | si |
| l.54 | De Man: rayas oscuras en direcciones de mayor atenuacion y entre metales | `deman1999`:87-88 (Sec. III-B, p. 693) | si |
| l.54 | Dispersion por densidad electronica | `selles2024marreview`:70 | si |
| l.54 | Razon 0.0001, elegida de forma arbitraria; rayas apreciables, parecidas a las policromaticas | `deman1999`:44, :189 (Sec. II-D, p. 693); :199, :201 (Sec. III-C, p. 694) | si |
| l.56 | Inanicion: pocos fotones, faltan datos esenciales | `selles2024marreview`:68-69 | si |
| l.56 | De Man no nombra la inanicion; ruido como lineas finas segun atenuacion integrada | `deman1999`:71-72, :208 | si |
| l.56 | Ruido no lineal; severidad depende de dispersion y endurecimiento | `deman1999`:207, :209 (Sec. III-E, p. 694) | si |
| l.58 | EEGE tangente a bordes; rayas que irradian; Selles: rayas alineadas con el borde | `deman1999`:89-90 (Sec. III-D); `selles2024marreview`:71 | si |
| l.58 | Ninguna da distancia; De Man no menciona medida de alcance | `deman1999`:81-97 (NO ENCONTRADO); decision §2 2026-09-30 ("el articulo no menciona") | si |
| l.60 | Glover y Pelc: volumen parcial no lineal; local vs largo alcance; hueso, monocromatica; De Man lo deja fuera | `glover1980nonlinear` Sec. II, pp. 240-243; `deman1999`:73-74 | si |
| l.62 | Rayas fuera del metal; $B_\delta$ convencion; aislamiento por sinograma; supuesto del dominio de imagen | `deman1999` Sec. III-B/D, :138; `park2015ct`; `capitulo2.tex` §Representacion; `capitulo3.tex`:176, 261 | si |
| l.64 | CatSim en XCIST; Peters sobre CatSim; lo que modela CatSim; comparacion prevista | `wu2022xcist` p. 6; `peters2025hybrid`:36; `deman2007catsim` Abstract; `capitulo3.tex`:219-225 | si |
| l.66 | Metricas de Peters con nombres publicados; *streak amplitude* respecto de la imagen sin metal del mismo caso | `peters2025hybrid`:56, :172-174 (*ground truth*); #8 APLICADA; BITACORA §2 2026-10-03 | si |
| l.66 | *Bone* y *metal integrity* | `peters2025hybrid`:177-183, :262 | si |
| l.66 | Disenadas para MAR, inversion; *streak amplitude* unico criterio primario | `capitulo3.tex`:215, 217 | si (T02 de r03 aplicado) |
| l.70 | Zwingmann: Tile y Pennal B y C; percutanea; referencia clinica del Obj 2 | `zwingmann2009navigated`:11, 88-90; `capitulo3.tex`:79 | si |
| l.72 | Smith: entra por el ilion a S1 o S2; tres corticales | `smith2006iliosacral`:69 | si |
| l.72 | Ala sacra desciende lateral y caudal | `routt1997`:122 | si |
| l.72 | `\GAPLIT` anatomia pelvica | MAPA:79 | si (GAP justificado) |
| l.72 | Transiliosacro; no intercambiables; Kaiser fija 10 mm para el iliosacro; Sec. SAP | `mclaren2021corridor` M&M; `docs/03-glosario.md`:74-76; `kaiser2014dysmorphism`:72; `capitulo3.tex`:196 | si |
| l.72 | `\GAPDEC` tipo de tornillo del corredor y de la referencia clinica | #130 ABIERTA; `zwingmann2009navigated`:79, :83, :197; MAPA:81 | si (GAP justificado; T01 de r03 aplicado) |
| l.74 | Routt: supino y fluoroscopia en tres planos; Zwingmann: 190 grados; TC posoperatoria | `routt1997` p. 206; `zwingmann2009navigated`:83, 103 | si |
| l.76 | Zona segura de Routt; conos de Gardner; no es variable | `routt1997` Fig. 2, pp. 212-213; `gardner2010safezones` M&M, p. 623; `capitulo3.tex`:168 | si |
| l.78 | McLaren: recta y tres puntos; umbral de 10 mm en los tres, tomado de trabajos previos; minimo no establecido; TotalSegmentator | `mclaren2021corridor` M&M; `gardner2010safezones`:71; `kaiser2014dysmorphism` p. e120(2); `capitulo3.tex`:85, 89; `wasserthal2023` | si |
| l.80 | Kaiser: reformateo al platillo de S1; angulacion contra crestas y espinas | `kaiser2014dysmorphism` Fig. 1, p. e120(3); `capitulo3.tex`:83 | si |
| l.80 | Regla de longitud util: al menos 5 mm a cada lado | `kaiser2014dysmorphism`:80, :228 (p. e120(2)) | si |
| l.80 | 10 mm como holgura de 1 a 2 mm alrededor de un tornillo de 6.3 a 8 mm | `kaiser2014dysmorphism`:36-37, :167 (Discusion, p. e120(7)); lectura propia remitida a `capitulo3.tex`:83, 89 | si |
| l.80 | Poses en el marco de Kaiser; localizacion con metal | `capitulo3.tex`:83, 93-95 | si |
| l.82 | Posicion ideal; tres tipos de perforacion; grados 0-3 con 2 y 4 mm; protrusion | `smith2006iliosacral` p. 236; `capitulo3.tex`:189-194, 257 | si |
| l.84 | Escala de pediculares mas angular; `\GAPDEC` angular | `smith2006iliosacral` p. 236; #11; MAPA:41 | si |
| l.84 | Zwingmann aplica la escala de perforacion | `zwingmann2009navigated`:230 | si |
| l.84 | Hinsche: definicion binaria, sin grados | `hinsche2002fluoroscopy`:29, :90 (Measurements, p. 138); :66 (escala graduada NO ENCONTRADO) | si |
| l.86 | Grados 1 y 2 de 2 mm; grado 3 abierto; equiespaciar es convencion | demostracion desde Smith; `capitulo3.tex`:200, 261 | si |
| l.88 | Tres componentes de SAP (brecha, corredor, fraccion por zona de densidad) | `capitulo3.tex`:189 | si |
| l.88 | Arand: modelo medio de valores de gris; ala sacra mas baja que cuerpo de S1 | `arand2019pelvicring`:96, :100-101 (Methods p. 377; Results p. 381) | si |
| l.88 | Motivacion en `sec:poses`; reporte descriptivo, sin comparar con la referencia clinica | `capitulo3.tex`:166, 189, 243 | si |
| l.88 | `\GAPDEC` fraccion por zona de densidad | MAPA:39 (D-O2.6 frente a #50; definicion solo en `src/muestreador/sap.py`); mismo texto que `capitulo2.tex`:76 | si (GAP justificado) |
| l.92 | Kazerouni: revision en imagen medica; Ho: Markov, $n_{\max} = 1000$; Dorjsembe: borrar la estructura | `kazerouni2023diffusionsurvey`; `ho2020denoising` Sec. 4, p. 5; `dorjsembe2024` §II | si |
| l.92-97 | Ec. difusion-directa en DiffBoost y Dorjsembe; $\bar\alpha_t$; Nichol coseno; $\beta_n \in (0,1)$ | `zhang2025diffboost` Ec. 3, Sec. III-A; `dorjsembe2024` Ec. (1); `nichol2021improved` Sec. 3.2 | si |
| l.99-104 | Prediccion del ruido; Ec. perdida en Rombach; U-Net en Ho y Song; Ronneberger | `ho2020denoising`; `rombach2022latentdiffusion` Ec. 1; `song2021ddim` Ap. D.1; `ronnenberger2015unet` | si |
| l.104 | Borrador propone U-Net, no fijada | `experiments/objetivo3/diseno_A.md`:69; `capitulo3.tex`:172 | si |
| l.106 | Song: no markoviano, determinista, sin reentrenar; 10 a 50 veces mas rapido | `song2021ddim` Resumen, p. 1 | si |
| l.106 | Las tres fuentes en imagenes naturales | fichas `ho2020denoising`, `song2021ddim`, `nichol2021improved` (Restriccion) | si |
| l.106 | Borrador propone muestreo determinista de Song; no menciona calendario de ruido | `diseno_A.md`:71 ("Muestreo DDIM, 50 pasos"; sin linea de calendario); `capitulo3.tex`:172 | si |
| l.108 | Concatenacion o atencion cruzada; Dorjsembe concatena; ControlNet | `rombach2022latentdiffusion` Fig. 3; `dorjsembe2024` §II; `zhang2023controlnet` §3.1-3.2 | si |
| l.110 | LDM, perdidas, alta frecuencia, cuello de botella; 25 HU; veredicto negativo descarta LDM y ControlNet | `rombach2022latentdiffusion` §1, §3, §5; `capitulo3.tex`:58, 71, 75, 174 | si |
| l.112 | RePaint; *inpainting* de Rombach; sintetizador con G borrada; LeFusion; `\GAPDEC` | `lugmayr2022repaint`; `rombach2022latentdiffusion` Tabla 15; `capitulo3.tex`:172; `zhang2025lefusion`; MAPA:69 | si |
| l.114 | 2.5D; `\GAPDEC` cortes (borrador: 3); lectura de Glover | `capitulo3.tex`:172; `diseno_A.md`:60; MAPA:78; `glover1980nonlinear` | si |
| l.118 | Tres tipos de resultado; unidad de analisis por objetivo; `\GAPDEC` agregacion | `capitulo3.tex`:71, 207, 223, 242-244, 265; MAPA:52 | si |
| l.120 | W1: suma de diferencias de FDA; unidad grado; 1 y 3; `\GAPLIT` | `capitulo3.tex`:200-205; MAPA:76 | si |
| l.122 | Superioridad y equivalencia; IC del 90 % dentro de $[-\Delta, +\Delta]$ | `capitulo3.tex`:225; BITACORA §2 2026-10-03 | si |
| l.124 | Wilcoxon pareada de una cola | `capitulo3.tex`:223 | si |
| l.124 | TOST con margen por semillas y corridas repetidas | `capitulo3.tex`:225, 231 | parcial (T02: margen aun sin preinscribir) |
| l.124 | `\GAPDEC` #90; muestras pequenas; IC 95 % por remuestreo; `\GAPLIT` Wilcoxon/TOST/remuestreo | `capitulo3.tex`:71, 225, 265; MAPA:44, 77 | si |
| l.126 | Regla fijada antes de la prueba que decide; poses y metrica antes de cualquier distancia; exploracion desfavorable con pacientes de prueba; tres decisiones post hoc del Obj 2 | `capitulo3.tex`:58, 127, 253, 255 | si |
| l.126 | Seis combinaciones; multiplicidad sin corregir; veredicto negativo | `capitulo3.tex`:69, 71, 265 | si |
| l.126 | Extension a Guo et al., misma regla y mismos pacientes; siete combinaciones; veredicto en resultados | `capitulo3.tex`:75, 255, 265; #93 CERRADA | parcial (T03) |
| l.128 | MAE (Ec. mae); RMSE >= MAE; RMSE de MAR como orden de magnitud | `capitulo3.tex`:60-67 | si |

## Comprobacion de patrones VIGENTES (dominio G-T4 / E-R6)
PAT-19: no reincide (el `\GAPDEC` de l.88 replica el del cap. 2 y MAPA:39 registra que la definicion implementada esta en codigo; el de l.46 sigue el texto cotejado del cap. 2). PAT-31: reincide leve (T01, T02). PAT-52: reincide leve (T03). PAT-72: no reincide (l.58 usa "no menciona", decision §2). PAT-101: no reincide ("En las fuentes revisadas", l.112). PAT-102: no reincide. PAT-106: cubierto por el `\GAPLIT` de l.35. PAT-107: no reincide (metricas de Peters en l.66). PAT-108: no reincide (U-Net, muestreo y calendario remiten a `sec:sintetizador`). PAT-110: no reincide. PAT-111: no reincide (l.56 dice ya la consecuencia). PAT-112: corregido (l.72). PAT-14: no reincide en el capitulo (nota fuera de alcance: `capitulo3.tex`:213 aun dice "respecto de la referencia" donde el cap. 1 dice "imagen sin metal del mismo caso"; corresponde al cap. 3). PAT-8, PAT-39, PAT-67, PAT-71, PAT-97, PAT-98, PAT-109: no reinciden.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Cifra o parametro del cap. 3 retomado en otro capitulo sin su cohorte, variante o estado de preinscripcion | G-T4, E-P3 | "En la cohorte local ... la mediana ... fue 0.42"; "un margen fijado por la variabilidad" | PAT-31 |
| Recuento de oportunidades que cambia (seis -> siete) sin decir si la conclusion previa sobre ellas se sostiene | E-M4 | "eleva a siete las combinaciones que pueden aprobar" tras "no lo compromete" | PAT-52 |
