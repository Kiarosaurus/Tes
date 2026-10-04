# Auditoria de trazabilidad — capitulo1 — r05

Archivo: `overleaf/secciones/capitulo1.tex` (129 lineas). Lint r05: PASA (0/0/0; GAP lit 4 / dato 1 / dec 8).
Respuesta previa: `capitulo1-r04-respuesta.md` (7 medios aplicados, 0 rechazados de trazabilidad). No hay RECHAZADOS que respetar.

Correcciones de trazabilidad de r04 verificadas en el texto:
- T01 (l.35): "En la cohorte primaria, con el recorte por defecto, la mediana de la fracción de vóxeles a 150~HU o menos dentro de las máscaras sacras fue 0.42 ... dejaría fuera, en la mediana, esa fracción del corredor". Coincide con `tesis/main.tex`:123 ("inside the sacral masks was 0.42"), `experiments/objetivo2/maintex_cifras.md`:4, :17 (recorte principal `default6mm`, COINCIDE) y `capitulo3.tex`:85. APLICADA.
- T02 (l.124): "con un margen definido por la variabilidad ... y aún sin preinscribir". Coincide con `capitulo3.tex`:225, :231. APLICADA.
- T03 (l.126): "El veredicto de esa extensión se presenta en el capítulo de resultados; si fuera aprobatorio, la multiplicidad de siete combinaciones sí podría haberlo favorecido". Es una deduccion valida de la oracion previa y respeta BITACORA §2 2026-09-29 (veredictos al cap. 4; `capitulo4.tex` sigue vacio). Nota sin hallazgo: #93 (CERRADA) registra que la extension no puede aprobar por la cota de saturacion (42.24 HU > 25 HU); el condicional no contradice ese registro, solo no lo adelanta. No se reabre para no oscilar con T03 de r04.

Contenido modificado en r04 rastreado: apertura de l.54, apertura de l.64, inversion pendiente en l.66 (`capitulo3.tex`:215), holgura de Kaiser movida a l.78 (`kaiser2014dysmorphism`:73, :167; `capitulo3.tex`:89), margen cortical en l.80 (`kaiser2014dysmorphism`:80, :228; `capitulo3.tex`:83), consecuencia 2.5D en l.114 (`capitulo3.tex`:172), apertura de l.128.

Claves: todas existen en `overleaf/referencias.bib`; cada apellido nombrado coincide con el primer autor; ninguna cita es sujeto gramatical sola; no hay fuentes de fabricante.
Contenido retirado: no aparecen Dice/HD95 como objetivo (Sørensen-Dice de l.66 es componente publicado de *bone integrity*), ni "31-60 %", ni BFC/ISC. Difusion latente y ControlNet solo como teoria y como descartadas (l.110).

**Conteo: alta=0 media=0 baja=1**

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | baja | G-T4, E-P3 | l.54, primera oracion | "El endurecimiento del haz y la dispersión producen rayas parecidas entre sí." | `deman1999`:201 (*"these artifacts are very similar to the polychromatic artifacts in figure 9"*, Sec. III-C, p. 694); `selles2024marreview`:37, :65, :70 (no compara las rayas de ambas causas) | La apertura nueva de r04 (S06) enuncia como hecho general, sin cita, una observacion que solo la simulacion bidimensional de De Man et al. registra; la ultima oracion del parrafo la da con su condicion ("En la misma simulación ... muy parecidas"). Patron PAT-31 reincide, leve: la condicion se pierde en la oracion que la retoma | "En la simulación de De Man et al., el endurecimiento del haz y la dispersión producen rayas parecidas entre sí." o abrir con la definicion y dejar la semejanza solo en la ultima oracion, que ya la cita |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.11 | Funcion del capitulo; reparto con los caps. 2 y 3 | estructura propia; `\ref` resueltas (lint PASA) | si |
| l.13 | Orden de las secciones; el muestreador precede al sintetizador | `capitulo3.tex`:21-33 (Fig. `fig:pipeline`) | si |
| l.13 | Pieza que usa cada seccion | `capitulo3.tex`:13, 20-31, 69, 79, 172, 189 | si |
| fig. 1.1 | Conceptos -> Obj 1, 2, 3, 4 y protocolo fisico | `capitulo3.tex`:13, 20-31, 172, 189, 213, 219 | si |
| l.31 | Lectura del detector = indice del sinograma; senal = suma sobre energias atenuada por longitud y material; coeficiente de atenuacion lineal | `deman2007catsim` Sec. 2.1, p. 1 | si |
| l.31 | Abadi (DukeSim): Beer-Lambert | `abadi2019`:51 (Sec. II-B, p. 1458) | si |
| l.31 | Wang (cocleares): Beer-Lambert en cinco energias | `wang2019cochlear`:52, 56 | si |
| l.33 | FBP en De Man 1999, CatSim y Karageorgos | `deman1999` Sec. II-C; `deman2007catsim` Sec. 3.1; `karageorgos2024ddpm` Sec. II-F | si |
| l.33 | Park: FBP supone el modelo monocromatico de Radon; desviacion no lineal | `park2015ct`:9 | si |
| l.33 | Cohorte solo con volumenes reconstruidos; medido y generado en dominio de imagen; protocolo fisico previsto | `capitulo3.tex`:42-46, 172, 219-221, 261; `docs/02-datos.md` | si |
| l.35 | Agua 0 HU, aire -1000 HU | `wu2022xcist` (Discussion Exp. 1, p. 13) | si |
| l.35 | Conversion HU-mu con el coeficiente del agua | `wang2019cochlear` (Sec. 2.1, p. 4) | si |
| l.35 | `\GAPLIT` fisica de TC | MAPA (fila del GAPLIT); `_candidatos.md` | si (GAP justificado) |
| l.35 | Hueso > 150 HU fuera del metal (Peters) | `peters2025hybrid`:177 (Sec. 2.5, p. 5) | si |
| l.35 | Wang y Li: metal clinico con 2500 HU; uso propio para cribar y delimitar | `wang2025adaptiveweighting`:110, 186; `li2024` Sec. IV-E; `capitulo3.tex`:73, 87, 178 | si |
| l.35 | Cohorte primaria, recorte por defecto, mediana 0.42 dentro de las mascaras sacras, a lo largo del eje del corredor mas ancho; "en la mediana" | `tesis/main.tex`:123; `maintex_cifras.md`:4, :17 (COINCIDE); `capitulo3.tex`:85 | si (T01 de r04 aplicado) |
| l.37-42 | Ventana (Ec. ventana) | `wang2025adaptiveweighting`:112, 184 (Eq. 2, p. 2410) | si |
| l.42 | Saturacion; fraccion inversamente proporcional al ancho | demostracion desde la Ec. ventana | si |
| l.44 | Definicion de la codificacion multiventana; tres ventanas de Wang en cascada, no como canales | `wang2025adaptiveweighting`:108 (Sec. V-A-1, p. 2412); terminos fijos de `overleaf/CLAUDE.md` | si |
| l.44 | Ida y vuelta y su error en HU | `capitulo3.tex`:58, 65 | si |
| l.46 | Tres codificaciones del Obj 1; techo 2000 < 2500 HU; 20 000 HU; arcoseno sobre [-1000, 20 000] HU | `capitulo3.tex`:69, 71; `tesis/main.tex`:77; DEC (`01-decisiones.md`:1049) | si |
| l.46 | `\GAPDATO` forma del arcoseno hiperbolico | busqueda en `experiments/**/*.md`, `docs/`, `tesis/main.tex`: solo el nombre `pub+asinh`, sin forma ni parametros (`04-implicancias.md`:3825, :5086) | si (GAP justificado) |
| l.46 | Compuerta mide MAE en hueso; sintetizador sin autoencoder; `\GAPDEC` codificacion y precision | `capitulo3.tex`:60-65, 172; MAPA (fila del GAPDEC) | si |
| l.50 | Selles: rayas claras y oscuras; severidad por tamano, forma, aleacion; osteosintesis intermedia, cualitativa | `selles2024marreview` Sec. 1, p. 1; Tabla 1, p. 6 | si |
| l.52 | Listas de causas de Selles y De Man; comunes y distintas; todas producen rayas; sin peso numerico | `selles2024marreview`:37; `deman1999`:69-79, :161 | si |
| l.54 | Apertura: endurecimiento y dispersion producen rayas parecidas | `deman1999`:201 (solo en su simulacion) | parcial (T01) |
| l.54 | BH: absorcion preferente de baja energia | `selles2024marreview` Sec. 1, p. 1 | si |
| l.54 | Park: *cupping* y rayas fuera | `park2015ct`:9 | si |
| l.54 | De Man: rayas oscuras en direcciones de mayor atenuacion y entre metales | `deman1999`:87-88 (Sec. III-B, p. 693) | si |
| l.54 | Dispersion por densidad electronica | `selles2024marreview`:70 | si |
| l.54 | Razon 0.0001, elegida de forma arbitraria; rayas apreciables, parecidas a las policromaticas | `deman1999`:44, :189, :199, :201 | si |
| l.56 | Inanicion: pocos fotones, faltan datos esenciales | `selles2024marreview`:68-69 | si |
| l.56 | De Man no nombra la inanicion; ruido como lineas finas segun atenuacion integrada; no lineal; depende de dispersion y endurecimiento | `deman1999`:71-72, :207-209 (Sec. III-E, p. 694) | si |
| l.58 | EEGE tangente a bordes; rayas que irradian; Selles: rayas alineadas con el borde; ninguna da distancia | `deman1999`:89-90, :81-97 (NO ENCONTRADO); `selles2024marreview`:71; BITACORA §2 2026-09-30 | si |
| l.60 | Glover y Pelc: volumen parcial no lineal; local vs largo alcance; hueso, monocromatica; De Man lo deja fuera | `glover1980nonlinear` Sec. II, pp. 240-243; `deman1999`:73-74 | si |
| l.62 | Rayas fuera del metal; $B_\delta$ convencion; aislamiento por sinograma; supuesto del dominio de imagen | `deman1999` Sec. III-B/D, :138; `park2015ct`; `capitulo2.tex` §Representacion; `capitulo3.tex`:176, 261 | si |
| l.64 | MAR elimina, simulacion produce; CatSim en XCIST; Peters sobre CatSim; lo que modela CatSim; comparacion prevista | `docs/03-glosario.md` (MAR); `wu2022xcist` p. 6; `peters2025hybrid`:36; `deman2007catsim` Abstract; `capitulo3.tex`:219-225 | si |
| l.66 | Metricas de Peters con nombres publicados; *streak amplitude* respecto de la imagen sin metal del mismo caso; *bone* y *metal integrity* | `peters2025hybrid`:56, :172-183, :262; #8 APLICADA; BITACORA §2 2026-10-03 | si |
| l.66 | Disenadas para MAR; inversion con definicion operativa pendiente; *streak amplitude* unico criterio primario | `capitulo3.tex`:215 (`\GAPDEC`), :217 | si |
| l.70 | Zwingmann: Tile y Pennal B y C; percutanea; referencia clinica del Obj 2 | `zwingmann2009navigated`:11, 88-90; `capitulo3.tex`:79 | si |
| l.72 | Smith: entra por el ilion a S1 o S2; tres corticales | `smith2006iliosacral`:69 | si |
| l.72 | Ala sacra desciende lateral y caudal; `\GAPLIT` anatomia pelvica | `routt1997`:122; MAPA (fila del GAPLIT) | si |
| l.72 | Transiliosacro; no intercambiables; Kaiser fija 10 mm para el iliosacro | `mclaren2021corridor` M&M; `docs/03-glosario.md`:74-76; `kaiser2014dysmorphism`:72; `capitulo3.tex`:196 | si |
| l.72 | `\GAPDEC` tipo de tornillo del corredor y de la referencia clinica | #130 ABIERTA; `zwingmann2009navigated`:79, :83, :197 | si (GAP justificado) |
| l.74 | Routt: supino y fluoroscopia en tres planos; Zwingmann: 190 grados; TC posoperatoria | `routt1997` p. 206; `zwingmann2009navigated`:83, 103 | si |
| l.76 | Zona segura de Routt; estructuras vecinas; conos de Gardner; no es variable | `routt1997` Fig. 2, pp. 212-213; `gardner2010safezones` M&M, p. 623; `capitulo3.tex`:168 | si |
| l.78 | McLaren: recta y tres puntos; umbral de 10 mm en los tres; heredado; minimo no establecido | `mclaren2021corridor` M&M; `gardner2010safezones`:71; `kaiser2014dysmorphism`:73, :168 | si |
| l.78 | Kaiser: holgura de 1 a 2 mm alrededor de un tornillo de 6.3 a 8 mm; lectura como holgura radial por lado en `sec:corredor` | `kaiser2014dysmorphism`:37, :167 (Discusion, p. e120(7)); `capitulo3.tex`:89 (en `sec:corredor`, l.81) | si |
| l.78 | Medicion sobre mascaras de TotalSegmentator; criterio en lugar del umbral | `wasserthal2023`; `capitulo3.tex`:85, 89 | si |
| l.80 | Kaiser: reformateo al platillo de S1; angulacion contra crestas y espinas | `kaiser2014dysmorphism` Fig. 1, p. e120(3); `capitulo3.tex`:83 | si |
| l.80 | Regla de longitud util: al menos 5 mm a cada lado; leida como margen cortical | `kaiser2014dysmorphism`:80, :228; `capitulo3.tex`:83 | si |
| l.80 | Poses en el marco de Kaiser; localizacion con metal | `capitulo3.tex`:83, 93-95 | si |
| l.82 | Posicion ideal; tres tipos de perforacion; grados 0-3 con 2 y 4 mm; protrusion | `smith2006iliosacral` p. 236; `capitulo3.tex`:189-194, 257 | si |
| l.84 | Escala de pediculares mas angular; `\GAPDEC` angular; Zwingmann aplica la de perforacion; Hinsche binaria | `smith2006iliosacral` p. 236; #11; `zwingmann2009navigated`:230; `hinsche2002fluoroscopy`:29, :66, :90 | si |
| l.86 | Grados 1 y 2 de 2 mm; grado 3 abierto; equiespaciar es convencion | demostracion desde Smith; `capitulo3.tex`:261 | si |
| l.88 | Tres componentes de SAP; Arand: ala sacra mas baja que S1; reporte descriptivo; `\GAPDEC` | `capitulo3.tex`:166, 189, 243; `arand2019pelvicring`:96, :100-101; MAPA (fila del GAPDEC) | si |
| l.92 | Kazerouni; Ho: Markov, $n_{\max} = 1000$; Dorjsembe: borrar la estructura | `kazerouni2023diffusionsurvey`; `ho2020denoising` Sec. 4, p. 5; `dorjsembe2024` §II | si |
| l.92-97 | Ec. difusion-directa; $\bar\alpha_t$; Nichol coseno; $\beta_n \in (0,1)$ | `zhang2025diffboost` Ec. 3; `dorjsembe2024` Ec. (1); `nichol2021improved` Sec. 3.2 | si |
| l.99-104 | Prediccion del ruido; Ec. perdida en Rombach; U-Net en Ho y Song; Ronneberger; borrador propone U-Net | `ho2020denoising`; `rombach2022latentdiffusion` Ec. 1; `song2021ddim` Ap. D.1; `ronnenberger2015unet`; `experiments/objetivo3/diseno_A.md`:69; `capitulo3.tex`:172 | si |
| l.106 | Song: no markoviano, determinista, sin reentrenar; 10 a 50 veces; imagenes naturales; borrador DDIM sin calendario | `song2021ddim` Resumen, p. 1; fichas `ho2020denoising`, `song2021ddim`, `nichol2021improved`; `diseno_A.md`:71 | si |
| l.108 | Concatenacion o atencion cruzada; Dorjsembe concatena; ControlNet con copia y convoluciones cero | `rombach2022latentdiffusion` Fig. 3; `dorjsembe2024` §II; `zhang2023controlnet` §3.1-3.2 | si |
| l.110 | LDM, perdidas, alta frecuencia, cuello de botella; 25 HU; veredicto negativo descarta LDM y ControlNet | `rombach2022latentdiffusion` §1, §3, §5; `capitulo3.tex`:58, 71, 75, 174 | si |
| l.112 | RePaint; *inpainting* de Rombach; sintetizador con G borrada; LeFusion; `\GAPDEC` | `lugmayr2022repaint`; `rombach2022latentdiffusion` Tabla 15; `capitulo3.tex`:172; `zhang2025lefusion` | si |
| l.114 | 2.5D; `\GAPDEC` cortes (borrador: 3); lectura propia sobre volumen parcial; sintetizador sobre valores reconstruidos | `capitulo3.tex`:172; `diseno_A.md`:60; `glover1980nonlinear` | si (marcada "este trabajo lee") |
| l.118 | Tres tipos de resultado; unidad de analisis por objetivo; `\GAPDEC` agregacion | `capitulo3.tex`:71, 207, 223, 242-244, 265 | si |
| l.120 | W1: suma de diferencias de FDA; unidad grado; 1 y 3; `\GAPLIT` | `capitulo3.tex`:200-205; MAPA | si |
| l.122 | Superioridad y equivalencia; IC del 90 % dentro de $[-\Delta, +\Delta]$ | `capitulo3.tex`:225; BITACORA §2 2026-10-03 | si |
| l.124 | Wilcoxon pareada de una cola | `capitulo3.tex`:223 | si |
| l.124 | TOST con margen por semillas y corridas repetidas, aun sin preinscribir | `capitulo3.tex`:172, 225, 231 | si (T02 de r04 aplicado) |
| l.124 | `\GAPDEC` #90; muestras pequenas; IC 95 % por remuestreo; `\GAPLIT` | `capitulo3.tex`:71, 225, 265; MAPA | si |
| l.126 | Regla fijada antes de la prueba que decide; poses y metrica antes de cualquier distancia; exploracion con pacientes de prueba; tres decisiones post hoc | `capitulo3.tex`:58, 127, 253, 255 | si |
| l.126 | Seis combinaciones; multiplicidad sin corregir; veredicto negativo | `capitulo3.tex`:69, 71, 265 | si |
| l.126 | Extension a Guo et al., misma regla y mismos pacientes; siete combinaciones; veredicto en resultados; condicional sobre la multiplicidad | `capitulo3.tex`:75, 255, 265; #93 CERRADA (`04-implicancias.md`:6766-6789); BITACORA §2 2026-09-29 | si (T03 de r04 aplicado) |
| l.128 | MAE (Ec. mae); RMSE >= MAE; RMSE de MAR como orden de magnitud | `capitulo3.tex`:60-67 | si |

## Comprobacion de patrones VIGENTES (dominio G-T4 / E-R6)
PAT-8: no reincide (la semejanza de l.54 lleva la cifra 0.0001 y la cita). PAT-14: no reincide. PAT-19: no reincide (el `\GAPDATO` de l.46 es justo: ningun `.md` de `experiments/` ni de `docs/` da la forma de la compresion; el `\GAPDEC` de l.88 replica el del cap. 2). PAT-31: reincide leve (T01). PAT-39: no reincide. PAT-52: no reincide (l.126 dice ya la consecuencia de la septima combinacion). PAT-58: fuera de dominio. PAT-72: no reincide (l.58 "no menciona"). PAT-101: no reincide (l.52, l.112 acotados a "las fuentes revisadas"). PAT-102: no reincide (l.114 remite a `sec:mt-artefactos` sin repetir a Glover y Pelc). PAT-108: no reincide. PAT-110: no reincide (l.128 no contrapone cifras). PAT-111: no reincide. PAT-112: no reincide (l.72). PAT-113, PAT-114: fuera de dominio. PAT-115: corregido (l.66 dice que la definicion esta pendiente y remite).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Oracion tematica reescrita para abrir con la idea pierde la condicion (simulacion, cohorte) que tenia la oracion de origen | G-T4, E-P3 | "El endurecimiento del haz y la dispersión producen rayas parecidas entre sí." | PAT-31 |
