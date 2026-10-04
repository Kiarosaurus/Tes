# Auditoria de trazabilidad — capitulo2 — r02

Seccion: `overleaf/secciones/capitulo2.tex` (Cap. II, 126 lineas). Lint r02: PASA 0/0/0, GAP lit=1 dato=2 dec=7.
Respuesta previa: `capitulo2-r01-respuesta.md`. No aplicados alli con motivo: T13 (46/129 frente a 36.5 %, a
relectura) y T14 (version de `ramzan2026claim`, fuera de lo editable); no se re-reportan. Los nueve hallazgos T01-T09
de r01 se verificaron corregidos (ver inventario). Todas las claves `\cite` (43) existen en `overleaf/referencias.bib`.
Ningun PDF abierto.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | E-R6, G-T4 | l.122 | "Los metodos que parten del metal clinico lo segmentan con un umbral \cite{karageorgos2024ddpm,...}" | `karageorgos2024ddpm.md`, Evidencia: "Random metal objects were defined based on CT images of metal objects" (II-A p. 3); "we manually designed realistic metal objects for each case" (II-A p. 4); "Metal por umbral: defining all voxels above the threshold" (II-F p. 10); "Caso del Apendice": "two virtually placed gold marker implants" | Karageorgos et al. nunca parten de metal clinico: su metal es siempre virtual (formas de un banco previo en entrenamiento; objetos disenados a mano y colocados virtualmente en los 4 casos clinicos). El umbral de II-F se aplica a la imagen sin corregir para reinsertar una estimacion del metal que ellos mismos insertaron, y el de 2500 HU es para la volumetria de evaluacion. Ademas, la oracion anterior del mismo parrafo los clasifica entre los que insertan "objetos definidos a partir de imagenes de TC de metal": el parrafo los pone en los dos grupos | Quitar `karageorgos2024ddpm` de esa cita: "Los metodos que parten del metal clinico lo segmentan con un umbral de HU \cite{yun2026simulationdriven,wang2025adaptiveweighting,li2024}". Si se quiere conservar el dato: "y Karageorgos et al. reinsertan el metal que simulan umbralizando la imagen sin corregir" |
| T02 | media | E-R6, G-T4 (PAT-64) | l.44 (ultima oracion); l.68 | "El problema ... abierto no es insertar metal en miles de casos ... sino colocarlo ... con una restriccion anatomica" | `wang2019cochlear.md`, Evidencia: "automatic segmentation of the scala tympani ... estimation of the positions of the electrode arrays" (Intro p. 2); "thresholding the distance map to create a 3D tubular binary mask near the center" (Sec. 2.1 p. 3); "applied on 1090 3D preoperative CT images" (Intro p. 2) | Patron PAT-64 reincide. El mismo parrafo cita a Wang et al. 2019, que colocan el implante en 1090 volumenes anclado a una estructura anatomica segmentada: insertan en del orden de mil casos **con** una restriccion anatomica. Lo que ninguna fuente hace es otra cosa (una distribucion de poses comparada con la clinica, que es lo que dice l.68 in fine). En l.68 la tercera carencia agrupa ese anclaje anatomico bajo "una regla geometrica", lo que oculta la excepcion | l.44: "El problema de colocacion que queda abierto no es insertar metal en miles de casos, que ese protocolo hace en 14 000, ni anclarlo a una estructura segmentada, como hacen Wang et al. en el oido, sino generar en cada pelvis una distribucion de poses comparable con la clinica". En l.68, si se mantiene el resumen fijado en BITACORA §2, anadir tras el: "y el anclaje de Wang et al. a una estructura segmentada produce una sola posicion por volumen" |
| T03 | baja | E-P3 (PAT-31) | l.36 | "en los casos clinicos su metodo fue el mejor en 13 de 28 metricas" | `karageorgos2024ddpm.md`, "Que hace": "4 CT clinicos con metal virtual"; Evidencia: "we manually designed realistic metal objects for each case" (II-A p. 4); "13 out of 28" (III-C p. 12) | Patron PAT-31 reincide. La cifra coincide, pero se pierde la condicion: los cuatro casos clinicos llevan metal virtual disenado a mano, no implantes reales. Leido junto a l.122 (T01), refuerza la idea erronea de que el metodo trabaja sobre metal clinico | "en cuatro TC clinicas con metal insertado de forma virtual, su metodo fue el mejor en 13 de 28 metricas" |
| T04 | baja | E-R6 | l.46 | "El simulador ... es un fundamento tecnico y no un metodo de comparacion validado en metal" | `peters2025hybrid.md`, Evidencia 3.1 p. 6: "Strong streak artifacts resulting from the metal inserts are well-replicated across all cases"; "less than 2%"; `wu2022xcist.md` (validacion de primer orden); `CLAUDE.md` raiz ("XCIST/CatSim queda como fundamento tecnico ..., su reimplementacion validada esta declarada fuera de alcance") | La fuente de la oracion es la decision de alcance, que habla de la reimplementacion validada propia, no de que el simulador carezca de validacion en metal. Seis lineas antes (l.40) el capitulo reporta que Peters et al. calibraron los modelos de artefacto metalico de CatSim contra un fantoma con insertos metalicos (<2 %). "No validado en metal" contradice ese parrafo | "El simulador sobre el que se ejecuta ese protocolo entra en este trabajo como fundamento tecnico. La validacion que publican sus autores, Wu et al., es ..." (sin "no validado en metal"); la limitacion de la validacion de Peters ya esta en l.42 |
| T05 | baja | G-B8, G-T4 (PAT-67) | l.106, l.109 (tabla) | Karageorgos: "Similitud y error frente a la imagen sin metal"; Wang 2025: "PSNR y SSIM" | Cuerpo l.36 (Karageorgos: solo SSIM y 13 de 28) y l.74 (Wang: solo PSNR); fichas: `karageorgos2024ddpm.md` Tabla I (RMSE 12.3); `wang2025adaptiveweighting.md` (26.76 dB/0.9501, 32.67 dB/0.9803) | Patron PAT-67 reincide en menor grado, contra la decision §2 "toda celda ... tiene una oracion de respaldo". El "error" de Karageorgos y el SSIM de Wang estan en las fichas pero no en el cuerpo | Ajustar las celdas a lo que dice el cuerpo ("SSIM frente a la imagen sin metal; metricas clinicas"; "PSNR; lectura de cinco medicos") o anadir en el cuerpo "y el RMSE" / "y el SSIM" con su cifra |
| T06 | baja | G-T4 (ficha insuficiente) | l.58 | "juzgan las mascaras resultantes por comparacion visual con las de otro generador" / "En los tres ... descansa en ... la inspeccion visual" | `ramzan2026claim.md` filas 62 (comparacion visual con DiffMask, Sec. 3.4 p. 8) y 64 ("scar volume (ML) distribution using the AHA-17 segment framework", Sec. 3.5 p. 11) | La fila 62 sostiene la comparacion visual, pero la fila 64 registra una evaluacion adicional por distribucion de volumen por segmento que podria ser cuantitativa. Si lo es, "descansa en ... la inspeccion visual" queda corto para Ramzan. El redactor ya lo senalo (respuesta r01, guia-5) sin cerrarlo | Relectura de `ramzan2026claim` Sec. 3.5 con `lector-papers`. Mientras, acotar: "y las comparan visualmente con las de otro generador y por su volumen por segmento" o dejar la oracion de sintesis solo para Chen y Jacob |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.8 | Comparacion por objetivos; tabla con fila propia | `redaccion/MAPA.md`:18 | si |
| l.10 | Orden: de generar imagen a fijar condiciones; secciones ligadas a Obj 1-4 | estructura del capitulo | si |
| l.12 | Sin busqueda sistematica documentada; lista definida por la autora | `CLAUDE.md` raiz regla 9; `_candidatos.md` | si |
| l.12 | Cada ficha copia frase y pagina de cada cifra que se cita | fichas citadas (Evidencia o "Numeros que cito" con seccion/pagina) | si (T10 r01 corregido) |
| l.12 | Snowballing a candidatos; busquedas dirigidas con fecha | `CLAUDE.md` raiz regla 15; `_candidatos.md` | si |
| l.12 | Una sola fuente con solo resumen, sin cifra | `zhang2026pediclescrew.md`:3 ("Profundidad: solo abstract"); l.56 sin cifras | si |
| l.12 | \GAPDEC protocolo de busqueda | `MAPA.md`:68 | si |
| l.16 | Dos familias (inpainting acotado; corte desde ruido) | fichas chen2024, ramzan, jacob, lefusion; diffboost, konz | si |
| l.16 | Rayas irradian desde el metal | `deman1999.md` | si |
| l.18 | DiffTumor: latente, mascara + region sana; no modela textura fuera; [-175, 250] HU | `chen2024tumorsynthesis.md` §3.2 p. 4; Apendice E.2 p. 21 | si |
| l.18 | Dice higado 62.5 -> 66.5 %, una de tres redes, media de cinco particiones | idem Tabla 4 p. 17 | si |
| l.18 | Cuatro radiologos; cerca de la mitad tomada por real | idem §4.1 pp. 5-6 | si |
| l.20 | Ramzan: RM cardiaca, dominio de imagen, perdida en mascara, fondo con ruido en cada paso; adaptado de LeFusion | `ramzan2026claim.md` filas 1-4, 10-11, 74 | si |
| l.20 | LeFusion: nodulos en TC, perdida en lesion, exterior real con ruido | `zhang2025lefusion.md` | si |
| l.20 | Dice 58.89 -> 63.53, mejor configuracion; sin fidelidad; fondo cualitativo | `ramzan2026claim.md` filas 50, 52, 58, 59 | si (T14 r01 no se re-reporta) |
| l.22 | LGESynthNet: latente + ControlNet; mapa de bordes + imagen enmascarada; decodifica todo | `jacob2026lgesynthnet.md` Sec. 3.1 p. 3 | si |
| l.22 | Sin paso de restitucion fuera de mascara | idem "Buscado sin resultado" | si |
| l.22 | SSIM 0.587; cicatriz < 1 %; atribuido a compresion latente | idem Tabla 1 p. 7; Sec. 1 p. 2; Sec. 5 p. 8 | si |
| l.22 | Lectura propia del SSIM ("Este trabajo lee") | BITACORA §2 (2026-09-29) | si |
| l.22 | Dice 0.72 -> 0.77 con 300 sinteticas | idem Tabla 2 p. 8; Sec. 4.3 p. 7 | si |
| l.24 | DiffBoost: ControlNet sobre SD, desde ruido, corte a corte; texto + borde; mezcla de parches al azar | `zhang2025diffboost.md` §III-B/C/D, Alg. 1 | si |
| l.24 | 78.46 -> 84.56; 94.42 -> 94.78; 62.92 -> 71.65 % | idem Tabla II p. 3678 | si |
| l.24 | Konz: mascara concatenada, dominio de imagen, desde ruido; [0, 255]; Dice 0.8980; 40 pacientes | `konz2024anatomicallycontrollable.md` Sec. 2-3, Tabla 1 | si |
| l.26 | Hu: analitico, efecto de masa 1.3 r | `hu2023.md` Tabla 1 p. 7426 | si (T01 r01 corregido: subordinada retirada) |
| l.26 | Jin: parche 3D, GAN, region de borde | `jin2021freetumor.md` Sec. 3.4.1 p. 9 | si |
| l.26 | Wu 2025 prepublicacion; conserva exterior | `wu2025freetumor.md` Ec. 1; `.bib` @misc | si |
| l.26 | Ventanas <= 600 HU | `hu2023.md`, `jin2021freetumor.md` Sec. 4.2, `wu2025freetumor.md` Tabla A19 | si |
| l.28 | RePaint: sin reentrenar; 256 x 256; sin TC ni metal | `lugmayr2022repaint.md` Sec. 5.1 | si |
| l.28 | Sintetizador genera region y copia el resto | `capitulo3.tex` sec:sintetizador; TM:79 | si |
| l.28 | \GAPDEC muestreo de la difusion | #106, #117 ABIERTAS; `MAPA.md`:69 | si |
| l.30 | Cinco modelos con segmentacion posterior (incl. LeFusion) | fichas; `zhang2025lefusion.md` "Dudas" | si (T19 r01 aplicado) |
| l.30 | Dos con similitud; uno con prueba visual | `jacob...md` Tabla 1; `zhang2025diffboost.md` Tabla I; `chen2024...md` §4.1 | si |
| l.30 | Ningun modelo trata metal; acotado sin mecanismo fuera; ninguna senal de entrenamiento | fichas (Metal NO ENCONTRADO); negacion partida por subgrupo (BITACORA §2 introduccion-r05) | si |
| l.34 | Insercion de metal virtual = practica establecida en MAR | fichas zhang2018, lin2019, wang2019, karageorgos | si |
| l.34 | Zhang y Yu: 15 formas segmentadas a mano de casos clinicos; TC reconstruidas | `zhang2018.md` Sec. IV-A p. 5; Sec. II-A-1 p. 2 ("we manually segment metals") | si |
| l.34 | 120 kVp, Poisson; el articulo no menciona dispersion ni volumen parcial | idem Sec. IV-A p. 6; filas NO ENCONTRADO | si (T02 r01 corregido) |
| l.34 | Lin: 100 formas; procedimiento similar; volumen parcial declarado | `lin2019.md` Sec. 4 p. 10508 | si |
| l.34 | Wang 2019: electrodos, mascara tubular, 1090 volumenes, Beer-Lambert, 5 energias | `wang2019cochlear.md` Intro p. 2; Sec. 2.1 p. 3 | si |
| l.34 | Karageorgos: objetos definidos a partir de TC de metal; CatSim en XCIST | `karageorgos2024ddpm.md` II-A p. 3 | si |
| l.34 | En los cuatro, el artefacto se genera para una red de remocion | fichas (direccion = remocion) | si |
| l.36 | Karageorgos: difusion en sinograma, solo sinogramas sin metal; traza metalica glosada | idem Abstract; II-A p. 4; `peters2025hybrid` 2.6 (glosa) | si |
| l.36 | Metal reinsertado umbralizando la imagen sin corregir | idem II-F p. 10 | si |
| l.36 | SSIM 0.964 en datos simulados | idem Tabla I p. 28 | si |
| l.36 | Mejor en 13 de 28 metricas en casos clinicos | idem III-C p. 12 (casos con metal virtual) | parcial (T03) |
| l.38 | Yun: correccion de endurecimiento en proyeccion + LDM | `yun2026simulationdriven.md` "Que hace" | si |
| l.38 | CLINIC-metal de CTPelvic1K; metal = mascara dada por umbral | idem Sec. 2.4.2 p. 8 | si |
| l.38 | Sesgo medio 0.82 HU frente a 3.18-6.30 HU de cuatro metodos, region libre de artefacto | idem Tabla 4 p. 11 ("4.20 3.18 6.30 5.89 0.82") | si |
| l.38 | 31 % de equipos AAPM con difusion | `haneda2025aapm.md` Sec. 3.1 p. 11 | si |
| l.38 | Ninguno genera el implante (no ve metal / metal dado) | `karageorgos...md` Abstract; `yun...md` "Restriccion" | si |
| l.40 | Peters: calibra CatSim contra fantoma en equipo comercial | `peters2025hybrid.md` 2.1 (Lightspeed VCT) | si |
| l.40 | 14 000 casos; TC clinica + metal fractal aleatorio | idem 2.3 p. 4 | si |
| l.40 | Ocho metricas, 29 escenarios, base del desafio AAPM | idem 2.4 p. 4; `haneda2025aapm.md` | si |
| l.40 | < 2 % valor medio; ruido < 10 % sin artefacto evidente; hasta 13.3 % en un experimento | idem 3.1 p. 6; Verificacion 4d-4f | si (T03 r01 corregido) |
| l.42 | Validacion no cubre paso hibrido ni geometria generica; todo 2D; sin osteosintesis 3D | idem Verificacion 3a-3b, 4b; Abstract; NO ENCONTRADO | si |
| l.42 | Adaptacion sin validacion heredada (sec:apariencia) | `capitulo3.tex`:213-219 | si |
| l.44 | Hasta cinco objetos al azar en tejido blando o hueso; lo ideal, ubicaciones realistas; manual impracticable | idem 2.3 p. 4; Discussion p. 9 | si |
| l.44 | Evaluacion en *meaningful locations* sin regla | idem Discussion p. 9 | si |
| l.44 | Karageorgos: solape >= 50 % con region > 200 HU | `karageorgos...md` II-A p. 4 | si |
| l.44 | Wang 2019: centro de estructura segmentada | `wang2019cochlear.md` Sec. 2.1 p. 3 | si |
| l.44 | Wang 2025: mascaras segmentadas de clinica, insertadas a mano en cortes dentales sin metal | `wang2025adaptiveweighting.md` V-A-2 pp. 2413-2414 | si |
| l.44 | Problema abierto = colocar con restriccion anatomica | contradicho por `wang2019cochlear.md` Sec. 2.1 | no (T02) |
| l.46 | Simulador = fundamento tecnico, "no validado en metal" | `CLAUDE.md` raiz; `peters2025hybrid.md` 3.1 | parcial (T04) |
| l.46 | XCIST: validacion cualitativa y semicuantitativa de primer orden; Ti 20 mm y Fe 10 mm en fantoma analitico | `wu2022xcist.md` Validation p. 9; Fig. 11 p. 29 | si |
| l.46 | Traza distorsionada > 3.0 cm; 274 de 14 000 | `haneda2025aapm.md` Sec. 4 p. 16 | si |
| l.48 | Cohorte de volumenes reconstruidos | `yun...md` ("does not provide sinogram data"); `docs/02-datos.md` | si |
| l.48 | Ren: sondas de ablacion; ruido y endurecimiento; validado con varilla de Ti 12.7 mm; demostrado en dos crioablaciones | `ren2022metalinsertion.md` Sec. 2.1.3, 2.5 | si (T09 r01 corregido) |
| l.48 | Requiere datos de proyeccion del fabricante; revisar con mas metal (ortopedico) | idem Sec. 4 | si |
| l.52 | Dos grupos: planificacion y series clinicas; necesidades de Obj 2 y 4 | estructura; `introduccion.tex` objetivos | si |
| l.54 | Liu: 14 casos de CTPelvic1K; fragmentos, reduccion, numero/posicion/direccion | `liu2025pipeline.md` VI p. 14; III-D p. 8 | si |
| l.54 | Optimizacion con seguridad, fijacion, ejecutabilidad; plan unico | idem III-D.3 pp. 11, 13 | si |
| l.54 | 2.56 mm y 3.31 grados; 86.7 % segun tres cirujanos | idem Abstract p. 2; IV-A/B pp. 16-17 | si |
| l.54 | 10.58 ± 3.84 frente a 4.36 ± 3.83 mm | idem IV-B p. 16; Tabla III p. 38 | si |
| l.54 | No aplica a sacro; sin distribucion; sin imagen | idem Discussion p. 18 | si |
| l.56 | Zhang 2026: solo resumen; sCT desde TC de haz conico; tornillos pediculares; mitiga el artefacto | `zhang2026pediclescrew.md`:3, 17-38 | si |
| l.58 | Ramzan: 17 segmentos; volumenes uniformes; comparacion visual con otro generador | `ramzan2026claim.md` filas 18-21, 62 | si (T06: fila 64) |
| l.58 | Chen: elipsoides refinados con radiologos | `chen2024...md` §3.3 p. 5 | si |
| l.58 | Jacob: elipsoide en region del miocardio al azar | `jacob2026lgesynthnet.md` Sec. 3.1 p. 4 | si |
| l.58 | Plausibilidad por azar, opinion experta o inspeccion visual | idem; Ramzan fila 64 sin cerrar | parcial (T06) |
| l.60 | Zwingmann 2009: cuatro niveles; TC posoperatoria; "brecha cortical" | `zwingmann2009navigated.md` M&M p. 1835 | si |
| l.60 | Grado 0: 69 % y 40 %; p = 0.02 | idem Results pp. 1836-1837 | si |
| l.60 | Dos series = referencia clinica; distribuciones en sec:sap | BITACORA §2; `capitulo3.tex`:200 | si |
| l.60 | Metaanalisis: 2.6 % (1832) y 0.1 % (262) | `zwingmann2013.md` Abstract p. 1257 | si |
| l.60 | Cohorte 2009 con cero; criterio de revision advertido; lectura propia | idem Fig. 2 p. 1261; Discusion p. 1264 | si (T05 r01 corregido) |
| l.62 | Zwingmann 2010: 63 y 131; 81/11/3/5 %; 42/22/21/13 % + 2 % grado 4 no definido | `zwingmann2010percutaneous.md` p. 1501-1503 | si |
| l.62 | Solapamiento posible con 2009 | idem; #113 | si |
| l.62 | \GAPDEC Zwingmann 2010 | #113 ABIERTA; `MAPA.md`:70 | si |
| l.62 | Herman: binaria; 36.5 % S1, 14.8 % S2, p = 0.035; TC posoperatoria | `herman2016.md` Resultados p. 8; P&M pp. 4-6 | si (T13 r01, no se re-reporta) |
| l.62 | Ningun tornillo integramente fuera; lectura como cota | idem Resultados p. 7; TM:52 | si |
| l.64 | Kaiser: marco calculable sobre TC | `kaiser2014dysmorphism.md`; TM:52 | si |
| l.64 | McLaren: 433 TC, 352 en S1 | `mclaren2021corridor.md` M&M p. 2 | si (T12 r01 aplicado) |
| l.64 | Ziran: 17 pelvis; CV 7-25 % en la mayoria; 97-140 % ala superior de S1 en plano frontal sacro | `ziran2007fluoroscopic.md` pp. 348-352; TM:52 | si (T04 r01 corregido) |
| l.64 | Variacion como razon para no reproducir pose canonica | `capitulo3.tex` sec:muestreador | si |
| l.64 | Ramadanov y Zabler: descripcion cualitativa | `ramadanov2025safezone.md`; `.bib` (dos autores) | si (T08 r01 corregido) |
| l.64 | Marco y viabilidad en sec:corredor; distribucion propia | `capitulo3.tex` sec:corredor | si |
| l.66 | Zwingmann: un radiologo sobre TC posoperatoria; borde de referencia no declarado | `zwingmann2009navigated.md` Verificacion 2026-09-16 filas 2 y 3 (NO ENCONTRADO) | si |
| l.66 | Escala tomada de Smith (ref. [23]) | idem M&M p. 1835; References | si |
| l.66 | Smith: cuatro cadaveres; heredada de pediculares; suma escala angular | `smith2006iliosacral.md` M&M p. 235; Screw Position p. 236 | si |
| l.66 | Herman binaria; Liu margen de plan unico | `herman2016.md`; `liu2025pipeline.md` | si |
| l.66 | SAP calcula el grado sobre pose y segmentacion | `capitulo3.tex`:189-194 | si |
| l.66 | \GAPDEC dimension angular | #11 ABIERTA (`04-implicancias.md`:528); `capitulo3.tex`:189; `MAPA.md`:41 | si |
| l.66 | Obj 4 adopta tres de ocho metricas de Peters, disenadas para MAR frente a imagen sin metal | `capitulo3.tex`:213-215; `introduccion.tex`:43; `peters2025hybrid.md` | si |
| l.66 | \GAPDEC inversion de metricas | #16, #17 ABIERTAS (`04-implicancias.md`:82, 97); `MAPA.md`:42 | si |
| l.68 | Cuatro carencias frente al Obj 2 | l.54, l.60-62, l.44, l.58 | parcial (T02 en la tercera) |
| l.68 | Sin generador de poses comparado con distribucion clinica, en fuentes revisadas | negativo acotado | si |
| l.72 | Sintesis <= 600 HU; dos fuentes de MAR con umbral de 2500 HU | ver l.26; `wang2025...md` V-A-2 p. 2413; `li2024.md` IV-E p. 1878 | si |
| l.74 | Tres ventanas de Wang 2025; peso aprendido por ventana; cascada | `wang2025...md` V-A-1 p. 2412; III p. 2410 | si |
| l.74 | Marco atribuido a trabajo anterior; \GAPLIT | idem III p. 2410; `_candidatos.md` PENDIENTE; `MAPA.md`:71 | si |
| l.74 | PSNR 26.76 frente a 32.67 dB en la ventana estrecha | idem V-B p. 2414 | si |
| l.74 | CLINIC-metal; cinco medicos; sin imagen limpia | idem V-A-3, V-C-3 | si |
| l.76 | Li: ventanas en perdida y evaluacion; entrada [-1000, 2000] HU; +0.64 dB | `li2024.md` III-D p. 1870; IV-B.4 p. 1873 | si |
| l.76 | Ninguna usa ventanas como codificacion de entrada de un generador; techo de 2000 HU satura el metal | fichas; TM:77 | si |
| l.78 | Rombach: compresion quita alta frecuencia; cuello de botella | `rombach2022latentdiffusion.md` §1, §5 | si |
| l.78 | Chen 2026 prepublicacion; autoencoders de video a TC; metricas sin unidades; [-1000, 1000] HU | `chen2026foundationvae.md` §1, §4.1 | si (T06 r01 corregido) |
| l.78 | Guo: autoencoder con TC; similitud, no HU; rango no declarado | `guo2025maisi.md` Tabla 1; NO ENCONTRADO | si |
| l.80 | De Man: mecanismos aislados en sinograma | `deman1999.md` | si |
| l.80 | Lin: 31.45 frente a 33.51 dB; variante con sinograma interpolado; mal planteado | `lin2019.md` Tabla 1 p. 10509; Sec. 2 p. 10506 | si |
| l.80 | Li: rama de solo imagen por debajo; \GAPDATO de cifras | `li2024.md` "Advertencia de transcripcion"; `MAPA.md`:72 | si |
| l.80 | Sin precedente de sintesis solo en imagen; supuesto a prueba | #61; `capitulo3.tex` sec:amenazas | si |
| l.82 | De Man, Park, Glover y Pelc, Selles (25 pacientes), Li (global) | fichas respectivas | si |
| l.84 | Radzi 2.0/2.6/1.6/2.0 mm; desde el eje; umbral no publicado; 3.5-4.0 mm; un tobillo | `radzi2014metalartifacts.md` pp. 163-167 | si |
| l.84 | Cassanego 3.1-4.2 mm; metodo del anterior; referencia no declarada | `cassanego2026evolution.md` Tabla 3 p. 7; M&M p. 3 | si |
| l.84 | B_delta ~12 mm = convencion | TM:79; #57 | si |
| l.86 | Sin banda numerica previa; Hu 1.3 r; Jin sin mm; truncamiento de rayas lejanas | fichas; TM:79 | si |
| l.90 | Muestreador y SAP ejecutados; \GAPDATO sin muestras | #116; `MAPA.md`:30 | si |
| l.101-109 | Celdas de los nueve trabajos | cuerpo l.18-74 y fichas | parcial (T05) |
| l.111 | Fila propia | `capitulo3.tex` sec:muestreador, sec:sintetizador, sec:apariencia | si |
| l.116 | Lectura por columnas (colocacion; fuera del objeto; fantoma 2D; multiventana acotada) | l.40-44, l.74-76 | si |
| l.118 | Brecha con las palabras de la introduccion; protocolo sobre poses; \GAPDEC sintetizador aprendido | `introduccion.tex`:54; #128.1; `MAPA.md`:66 | si |
| l.120 | Tres elementos; segundo sin ajuste; ningun objetivo aisla primero ni tercero | `introduccion.tex`:58-60; TM:52 | si |
| l.122 | Formas de las fuentes (Zhang y Yu, Karageorgos, Peters, Wang 2019) | fichas | si |
| l.122 | Metodos con metal clinico segmentan por umbral (incluye Karageorgos) | `karageorgos...md` II-A, II-F | no (T01) |
| l.122 | Xie: cortes simulados, 2500 HU, SE 100 %, Dice 82.92 %; lectura propia | `xie2024implantsegmentation.md` Results p. 6; Tabla 2 p. 11 | si |
| l.122 | Salvedad #128.4: entrenamiento con mascaras umbralizadas; desplazamiento de dominio | `capitulo3.tex`:182; `introduccion.tex`:58 | si (T07 r01 corregido) |
| l.124 | Piezas publicadas (insercion, difusion frente a metal, Konz/Ramzan, LeFusion, Hu/Jin, MAR) | secciones 2.1-2.4 | si |
| l.124 | \GAPDEC reformulacion de novedad | #56 act. 2026-09-21; `MAPA.md`:73 | si |
| l.126 | Supuesto y convencion; evaluacion por coherencia, no por segmentacion | #61; TM:79; `docs/00-tesis.md` Fuera de alcance pto 1 | si |
| global | Claves `\cite` (43, incl. `smith2006iliosacral`) | todas en `overleaf/referencias.bib` | si |
| global | Contenido retirado (Dice/HD95 como objetivo, latente/ControlNet vigente, "31-60%", BFC/ISC) | texto completo | si: ausente |
| global | Cita como sujeto gramatical (E-F3) | texto completo | si: ninguna |
| global | Entradas de dos autores (Zhang y Yu, Ramadanov y Zabler, Glover y Pelc) | `.bib` | si |
| global | Fuentes de fabricante | ninguna | si |
| global | Prepublicaciones senaladas (`wu2025freetumor`, `chen2026foundationvae`) | `.bib` @misc | si |
| global | Implicancias ABIERTAS afirmadas como hecho | #11, #16/#17, #56, #57, #61, #106/#117, #113, #116, #128 van como GAP o supuesto | si |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una fuente se agrupa en una categoria que su propia ficha (y el mismo parrafo) contradice | E-R6, G-T4 | "Los metodos que parten del metal clinico ... \cite{karageorgos2024ddpm,...}" | nuevo |
| Negativo de sintesis ("queda abierto") que una fuente citada en el mismo parrafo ya cubre | E-R6 | "no es insertar metal en miles de casos, sino colocarlo con restriccion anatomica" | PAT-64 |
| Cifra ajena pierde su condicion (metal virtual en casos clinicos) | E-P3 | "en los casos clinicos su metodo fue el mejor en 13 de 28" | PAT-31 |
| Celda de tabla con metrica que el cuerpo no presenta | G-B8 | Karageorgos "Similitud y error"; Wang "PSNR y SSIM" | PAT-67 |
