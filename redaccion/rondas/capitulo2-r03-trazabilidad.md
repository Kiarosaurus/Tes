# Auditoria de trazabilidad — capitulo2 — r03

Seccion: `overleaf/secciones/capitulo2.tex` (Cap. II, 126 lineas). Lint r03: PASA 0/0/0, GAP lit=1 dato=2 dec=8.
Respuesta previa: `capitulo2-r02-respuesta.md`. Alli se dejaron sin aplicar, con motivo: T06 (Ramzan Sec. 3.5, a
relectura) y el 46/129 frente a 36.5 % de Herman (a relectura). No los vuelvo a reportar. Los hallazgos T01 a T05 de r02
estan corregidos (ver inventario). Las 43 claves `\cite` existen en `overleaf/referencias.bib`, y los apellidos
nombrados coinciden con el primer autor de cada entrada. No abri ningun PDF.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2 | l.120 | "El error de ida y vuelta de esa codificacion sin autoencoder no lo verifica ningun objetivo \GAPDEC{...}" | `experiments/objetivo1/p1_compuerta.md`:31-38 (columna "identidad", MAE en hueso sin autoencoder: `pub+asinh` 0.00/0.00 HU, `LW20000` 0.00/0.00, `pub` 21.80/0.14; n = 34); :13 (control "identidad frente a E6c float", 165/165); `experiments/objetivo1/e6c_techo_lw.md`:21 (`pub+asinh` 0.00 / 0.01 / 0.13 / 2.07 HU en hueso a float/16/12/8 bits); `experiments/objetivo3/diseno_A.md`:57-58 ("Identidad exacta en hueso y metal (E6c: 0.00 HU a float; P1: 0.00 en identidad)") | El GAP da por pendiente un error que ya esta medido. La corrida de la compuerta del Objetivo 1 (P1) reporta la ida y vuelta sin autoencoder de las tres codificaciones como control de identidad, y E6c la mide sobre los 178 volumenes. Lo que falta es otra cosa: la decision sobre que codificacion y que precision adopta el sintetizador, y su preinscripcion. Ademas, "no lo verifica ningun objetivo" es inexacto: el Objetivo 1 lo midio, aunque no como criterio de decision. Se parece al PAT-19 (ERRADICADO). El texto es copia exacta del GAP de `introduccion.tex`:46, y el de `capitulo3.tex`:172 tiene el mismo problema | Separar lo medido de lo pendiente: "La compuerta del Objetivo 1 midio como control la ida y vuelta de esa codificacion sin autoencoder (Capitulo 4), pero ningun objetivo la preinscribe como criterio \GAPDEC{que codificacion multiventana y que precision adopta el sintetizador, pendiente de la preinscripcion del sintetizador}". Siguiendo la decision de BITACORA §2 (capitulo3-r00), la cifra va al cap. 4. Avisar a la autora de que la misma correccion alcanza a la introduccion y al cap. 3 |
| T02 | baja | E-P3 | l.54 | "14 casos clinicos de CTPelvic1K, el conjunto de datos de este trabajo" | `liu2025pipeline.md` Evidencia (VI p. 14: 14 casos con fractura unilateral, sin sacro); `capitulo3.tex`:42 (178 de 1 184 volumenes locales, correspondencia inferida) | Liu et al. excluyen sanos y fracturas de sacro, y la ficha no dice de que subconjuntos salen los 14 casos. La aposicion puede leerse como que esos casos estan en la cohorte local, y eso no esta verificado | "de CTPelvic1K, el conjunto del que proceden los datos de este trabajo" o "la coleccion de la que este trabajo dispone de 178 volumenes (Seccion `sec:datos`)" |
| T03 | baja | E-P3 (PAT-31) | l.74 | "Evaluan ademas sobre el subconjunto CLINIC-metal ... con una lectura visual de cinco medicos" | `wang2025adaptiveweighting.md` Evidencia: "it contains 14 metal-corrupted volumes" (V-A-2 p. 2413); "30 clinical images from the real CLINIC-metal dataset" (V-C-3 p. 2415); `capitulo3.tex`:36 (75 volumenes en CLINIC-metal, 14 anotados) | Patron PAT-31 reincide, en grado menor. La version de CLINIC-metal de Wang et al. tiene 14 volumenes, y la lectura se hizo sobre 30 imagenes. La carpeta local que se le asocia tiene 75. Sin la condicion, parece que evaluaron sobre el conjunto local entero | "Evaluan ademas sobre 14 volumenes del subconjunto CLINIC-metal ..., con una lectura visual de cinco medicos sobre 30 imagenes" |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.8 | Comparacion por objetivos; tabla con fila propia | `redaccion/MAPA.md`:18 | si |
| l.10 | Orden de las secciones y su ligadura con Obj 1-4 y $B_\delta$ | estructura del capitulo | si |
| l.12 | Sin busqueda sistematica; lista de la autora; fichas con frase y pagina; candidatos; busquedas dirigidas fechadas | `CLAUDE.md` raiz reglas 2, 15; `_candidatos.md` | si |
| l.12 | Una sola fuente con solo resumen, sin cifra | `zhang2026pediclescrew.md` ("Profundidad: solo abstract"); `wang2025adaptiveweighting.md`:13 (etiqueta retirada); l.56 sin cifras | si |
| l.12 | \GAPDEC protocolo de busqueda | `MAPA.md`:68 | si |
| l.16 | Dos familias (inpainting acotado; corte entero desde ruido) | fichas chen2024, ramzan, jacob, lefusion; diffboost, konz | si |
| l.16 | Rayas que irradian desde el metal | `deman1999.md` | si |
| l.18 | DiffTumor: latente, mascara + region sana; no modela textura fuera; [-175, 250] HU | `chen2024tumorsynthesis.md` §3.2 p. 4; Ap. E.2 p. 21 | si |
| l.18 | Dice en higado 62.5 -> 66.5 %, una de tres redes, media de cinco particiones; cuatro radiologos, cerca de la mitad | idem Tabla 4 p. 17; §4.1 pp. 5-6 | si |
| l.20 | Ramzan: RM cardiaca, dominio de imagen, perdida en mascara, fondo con ruido; adaptado de LeFusion | `ramzan2026claim.md` filas 1-4, 10-11, 74 | si |
| l.20 | LeFusion: nodulos en TC, perdida en lesion, exterior real con ruido | `zhang2025lefusion.md` | si |
| l.20 | Dice 58.89 -> 63.53 en mejor configuracion; sin fidelidad; fondo cualitativo | `ramzan2026claim.md` filas 50, 52, 58, 59 | si |
| l.22 | LGESynthNet: latente + ControlNet; bordes + imagen enmascarada; decodifica todo; sin restitucion | `jacob2026lgesynthnet.md` Sec. 3.1 p. 3; "Buscado sin resultado" | si |
| l.22 | SSIM 0.587; cicatriz < 1 %; atribuido a compresion; lectura propia; Dice 0.72 -> 0.77 con 300 | idem Tabla 1 p. 7; Sec. 1, 5; Tabla 2 p. 8; BITACORA §2 | si |
| l.24 | DiffBoost: ControlNet sobre SD, desde ruido, corte a corte; texto + borde; parches al azar | `zhang2025diffboost.md` §III, Alg. 1 | si |
| l.24 | 78.46 -> 84.56; 94.42 -> 94.78; 62.92 -> 71.65 % | idem Tabla II p. 3678 | si |
| l.24 | Konz: mascara concatenada, dominio de imagen, desde ruido; [0, 255]; Dice 0.8980; 40 pacientes | `konz2024anatomicallycontrollable.md` Sec. 2-3, Tabla 1 | si |
| l.26 | Hu: analitico, efecto de masa hasta 1.3 r | `hu2023.md` Tabla 1 p. 7426 | si |
| l.26 | Jin: parche 3D, GAN, region de borde | `jin2021freetumor.md` Sec. 3.4.1 p. 9 | si |
| l.26 | Wu 2025: prepublicacion; conserva el exterior | `wu2025freetumor.md` Ec. 1; `.bib` @misc | si |
| l.28 | RePaint: sin reentrenar; region conocida conservada; 256 x 256; sin TC ni metal | `lugmayr2022repaint.md` Sec. 5.1 | si |
| l.28 | Sintetizador genera una region y copia el resto | `capitulo3.tex`:172 | si |
| l.28 | \GAPDEC muestreo de la difusion | #106, #117 ABIERTAS; `MAPA.md`:69 | si |
| l.30 | Cinco con segmentacion posterior; dos con similitud; uno con prueba visual | fichas respectivas | si |
| l.30 | Ningun modelo trata metal; negacion partida por familia | fichas (Metal NO ENCONTRADO); BITACORA §2 introduccion-r05 | si |
| l.34 | Insercion de metal virtual es practica establecida en MAR | fichas zhang2018, lin2019, wang2019cochlear, karageorgos | si |
| l.34 | Zhang y Yu: 15 formas segmentadas a mano; TC reconstruidas; 120 kVp; Poisson; "el articulo no menciona" dispersion ni volumen parcial | `zhang2018.md` Sec. IV-A pp. 5-6; II-A-1 p. 2; filas NO ENCONTRADO | si |
| l.34 | Lin: 100 formas; volumen parcial declarado | `lin2019.md` Sec. 4 p. 10508 | si |
| l.34 | Wang 2019: mascara tubular, 1090 volumenes, Beer-Lambert, cinco energias | `wang2019cochlear.md` Intro p. 2; Sec. 2.1 p. 3 | si |
| l.34 | Karageorgos: objetos definidos a partir de TC de metal; CatSim dentro de XCIST | `karageorgos2024ddpm.md` Evidencia "Origen de las formas metalicas" (II-A p. 3); "Simulador usado"; Candidatos [23] | si |
| l.34 | En los cuatro, el artefacto se genera para una red que lo elimina | fichas (direccion = remocion) | si |
| l.36 | Haneda: 31 % de los equipos con difusion | `haneda2025aapm.md` Evidencia Sec. 3.1 p. 11 | si |
| l.36 | Karageorgos: difusion en sinograma, solo sinogramas sin metal; traza metalica glosada | `karageorgos2024ddpm.md` Abstract; II-A p. 4 | si |
| l.36 | Metal reinsertado umbralizando la imagen sin corregir | idem "Metal por umbral" (II-F p. 10); "Restriccion o supuesto clave" | si |
| l.36 | SSIM 0.964 sobre datos simulados | idem Tabla I p. 28 | si |
| l.36 | Cuatro TC clinicas con metal disenado a mano e insertado de forma virtual; mejor en 13 de 28 | idem "Objetos disenados a mano" (II-A p. 4); "13 out of 28" (III-C p. 12) | si (T03 r02 corregido) |
| l.38 | Yun: correccion de endurecimiento en proyeccion + LDM; CLINIC-metal; metal por umbral | `yun2026simulationdriven.md`:11, 36-37 (Sec. 2.4.2 p. 8) | si |
| l.38 | Salvedad de correspondencia inferida | `capitulo3.tex`:42; BITACORA §2 capitulo2-r02 | si |
| l.38 | Sesgo medio de 0.82 HU frente a 3.18-6.30 HU de cuatro metodos | `yun...md`:110, 192-193 (Tabla 4 p. 11) | si |
| l.38 | Ninguno genera el implante | `karageorgos...md` Abstract; `yun...md`:18 | si |
| l.40 | Peters: CatSim calibrado contra fantoma en equipo comercial; 14 000 casos; fractales aleatorios | `peters2025hybrid.md` 2.1, 2.3 p. 4 | si |
| l.40 | Ocho metricas, 29 escenarios, base del desafio | idem 2.4 p. 4; `haneda2025aapm.md` | si |
| l.40 | < 2 % valor medio; ruido < 10 % sin artefacto evidente; hasta 13.3 % | idem 3.1 p. 6; Verificacion 4d-4f | si |
| l.42 | Validacion sin paso hibrido ni geometria generica; todo 2D; sin osteosintesis 3D | idem Verificacion 3a-3b, 4b; NO ENCONTRADO | si |
| l.42 | Adaptacion que no hereda la validacion | `capitulo3.tex`:221 | si |
| l.44 | Resumen "al azar, con una regla geometrica sobre la anatomia o a mano" | BITACORA §2 capitulo2-r02; cuerpo l.44 | si |
| l.44 | Peters: hasta cinco objetos al azar en tejido blando o hueso; ubicaciones realistas ideales, impracticables; *meaningful locations* sin regla | `peters2025hybrid.md` 2.3 p. 4; Discussion p. 9 | si |
| l.44 | Karageorgos: solape >= 50 % con region > 200 HU | `karageorgos...md` II-A p. 4 | si |
| l.44 | Wang 2019: centro de una estructura segmentada | `wang2019cochlear.md` Sec. 2.1 p. 3 | si |
| l.44 | Wang 2025: mascaras clinicas segmentadas, insertadas a mano en cortes dentales; tamano, angulo, posicion | `wang2025adaptiveweighting.md`:66-69, 209 (V-A-2 pp. 2413-2414) | si |
| l.44 | Carencia: posicion ligada a la anatomia ya existe; falta distribucion comparada con la clinica | idem; `wang2019cochlear.md`; `karageorgos...md` | si (T02 r02 corregido) |
| l.46 | Simulador = fundamento tecnico, sin reimplementacion validada | `CLAUDE.md` raiz (XCIST/CatSim); `capitulo3.tex`:219 | si (T04 r02 corregido) |
| l.46 | Wu: evaluacion cualitativa y semicuantitativa de primer orden; Ti 20 mm y Fe 10 mm en fantoma analitico | `wu2022xcist.md`:98, 136-137 (Validation p. 9; Fig. 11 p. 29) | si |
| l.46 | Traza distorsionada con objetos de mas de 3.0 cm; 274 de 14 000 | `haneda2025aapm.md`:43, 180-182 (Sec. 4 p. 16) | si |
| l.46 | Ni validacion ni limite establecidos con osteosintesis (no afirma resuelta la opcion 2 de #8) | `wu2022xcist.md`; `haneda...md`; #8 ABIERTA, sin afirmarse resuelta | si |
| l.48 | Cohorte de volumenes reconstruidos | `yun...md`:93; `docs/02-datos.md` | si |
| l.48 | Ren: sondas de ablacion; ruido y endurecimiento; varilla de Ti de 12.7 mm; dos crioablaciones; datos del fabricante; revisar con mas metal (modal conservado) | `ren2022metalinsertion.md` Sec. 2.1.3, 2.5, 4 | si |
| l.52 | Cuatro grupos de la seccion; necesidades de Obj 2 y 4 | estructura; `introduccion.tex` objetivos | si |
| l.54 | Liu: 14 casos de CTPelvic1K | `liu2025pipeline.md`:25, 48 (VI p. 14) | si (T02: aposicion) |
| l.54 | Etiqueta fragmentos; planifica reduccion; numero, posicion, direccion | idem "Que hace"; Verificacion 2 (III-D p. 8) | si |
| l.54 | Optimizacion con seguridad, fijacion, ejecutabilidad; plan unico por tornillo | idem Verificacion 1-2 (III-D.3 pp. 11, 13) | si |
| l.54 | 2.56 mm y 3.31 grados; 86.7 % segun tres cirujanos | idem:26-27, 98 (Abstract p. 2; IV-B p. 17) | si |
| l.54 | 10.58 ± 3.84 frente a 4.36 ± 3.83 mm | idem:28, 90 (Tabla III p. 38) | si |
| l.54 | Casos de cresta iliaca, pubis y acetabulo; "el articulo no menciona tornillos iliosacros"; no se aplica a fracturas de sacro | idem:51 (p. 14); Verificacion 4 (NO ENCONTRADO); :112 (Discussion p. 18) | si (ES-01/guia-1 r02 aplicado; BITACORA §2) |
| l.54 | Sin distribucion de colocaciones ni imagen o artefacto | idem:116-117 (NO ENCONTRADO) | si |
| l.56 | Zhang 2026: solo resumen; sCT desde TC de haz conico; tornillos pediculares; mitiga el artefacto | `zhang2026pediclescrew.md` | si |
| l.58 | Ramzan: 17 segmentos; volumenes uniformes; comparacion visual con otro generador | `ramzan2026claim.md` filas 18-21, 62 | si (T06 r02 no se re-reporta) |
| l.58 | Chen: elipsoides refinados con radiologos; Jacob: elipsoide al azar | `chen2024...md` §3.3 p. 5; `jacob...md` Sec. 3.1 p. 4 | si |
| l.60 | Zwingmann 2009: cuatro niveles; TC posoperatoria; "brecha cortical" | `zwingmann2009navigated.md` M&M p. 1835; BITACORA §2 | si |
| l.60 | Grado 0: 69 % y 40 %; p = 0.02 | idem Results pp. 1836-1837 | si |
| l.60 | Dos series = referencia clinica; distribuciones en sec:sap | `capitulo3.tex`:200 | si |
| l.60 | Metaanalisis: 2.6 % (1832) y 0.1 % (262); cohorte 2009 con cero; criterio de revision; lectura propia | `zwingmann2013.md` Abstract p. 1257; Fig. 2 p. 1261; Discusion p. 1264 | si |
| l.62 | Zwingmann 2010: 63 y 131 tornillos; 81/11/3/5 %; 42/22/21/13 % + 2 % en grado 4 no definido; solape posible | `zwingmann2010percutaneous.md` pp. 1501-1503; #113 | si |
| l.62 | \GAPDEC Zwingmann 2010 | #113 ABIERTA; `MAPA.md`:70 | si |
| l.62 | Herman: definicion binaria; 36.5 % en S1 y 14.8 % en el segundo segmento sacro; p = 0.035 | `herman2016.md`:68, 127-128 (Resultados p. 8); :102 (P&M p. 6) | si (46/129 no se re-reporta) |
| l.62 | Ningun tornillo integramente fuera del hueso | idem:141 (Resultados p. 7) | si |
| l.62 | Poses que no atraviesan hueso = grado 3 en SAP; sin equivalente en Herman | `capitulo3.tex`:196, 162 | si (guia-5 r02 aplicado; PAT-78 no reincide) |
| l.64 | Kaiser: 104 TC de pelvis no lesionadas; marco calculable | `kaiser2014dysmorphism.md`:81 (M&M p. e120(2)) | si |
| l.64 | McLaren: 433 TC, 352 en S1 | `mclaren2021corridor.md` M&M p. 2 | si |
| l.64 | Ziran: diecisiete pelvis; CV de 7 a 25 % en la mayoria; 97-140 % en el ala superior de S1, plano frontal sacro | `ziran2007fluoroscopic.md` pp. 348-352 | si |
| l.64 | Variacion como razon para no usar una pose canonica | `capitulo3.tex` sec:muestreador | si |
| l.64 | Ramadanov y Zabler: descripcion cualitativa | `ramadanov2025safezone.md`; `.bib` (dos autores) | si |
| l.64 | Marco y viabilidad en sec:corredor; distribucion de poses propia | `capitulo3.tex` sec:corredor, :189 | si |
| l.66 | Zwingmann: un radiologo; borde no declarado; escala de Smith | `zwingmann2009navigated.md` Verificacion 2026-09-16; M&M p. 1835 | si |
| l.66 | Smith: cuatro cadaveres; heredada de pediculares; escala angular | `smith2006iliosacral.md` M&M p. 235; p. 236 | si |
| l.66 | SAP calcula el grado sobre pose y segmentacion | `capitulo3.tex`:189-194 | si |
| l.66 | \GAPDEC dimension angular | #11 ABIERTA; `MAPA.md`:41 | si |
| l.66 | Tres de las ocho metricas de Peters, disenadas para MAR frente a la imagen sin metal | `capitulo3.tex`:213-215; `peters2025hybrid.md` | si |
| l.66 | \GAPDEC inversion de metricas | #16, #17 ABIERTAS; `MAPA.md`:42 | si |
| l.68 | Cuatro carencias; la tercera con el resumen fijado y sin comparacion con distribucion clinica | l.54, l.60-62, l.44, l.58; BITACORA §2 capitulo2-r02 | si |
| l.68 | Sin generador de poses comparado con distribucion clinica, en las fuentes revisadas | negativo acotado | si |
| l.72 | Sintesis que declara saturacion <= 600 HU (Chen, Hu, Jin, Wu 2025) | `chen2024...md` Ap. E.2; `hu2023.md`; `jin2021freetumor.md` Sec. 4.2; `wu2025freetumor.md` Tabla A19 | si |
| l.72 | Dos fuentes de MAR con umbral de 2500 HU sobre metal clinico | `wang2025...md`:110 (V-A-2 p. 2413); `li2024.md`:46 (IV-E p. 1878) | si |
| l.74 | Tres ventanas; peso aprendido por ventana; cascada, no canales | `wang2025...md`:45-54, 108 (V-A-1 p. 2412; III p. 2410) | si |
| l.74 | Marco atribuido a un trabajo anterior; \GAPLIT | idem III p. 2410; `_candidatos.md`; `MAPA.md`:71 | si |
| l.74 | PSNR 26.76 dB y SSIM 0.9501 frente a 32.67 dB y 0.9803 | idem:276-277 (V-B p. 2414) | si |
| l.74 | CLINIC-metal por inferencia; cinco medicos; sin imagen limpia | idem:111, 255-266 (V-A-3, V-C-3); `capitulo3.tex`:42 | parcial (T03) |
| l.76 | Li: ventanas en perdida y evaluacion; entrada [-1000, 2000] HU; +0.64 dB en el metal mas grande | `li2024.md`:38, 45, 58 (III-D p. 1870; IV-B.4 p. 1873) | si |
| l.76 | Ninguna usa las ventanas como codificacion de entrada de un generador; techo de 2000 HU satura el metal | fichas; #39 | si |
| l.76 | Entrada y salida del sintetizador en codificacion multiventana; variantes de techo | `capitulo3.tex`:172, 69 | si |
| l.78 | Rombach: compresion quita alta frecuencia; cuello de botella | `rombach2022latentdiffusion.md` §1, §5 | si |
| l.78 | Chen 2026: prepublicacion; autoencoders de video congelados en TC; PSNR, SSIM, MSE; "el articulo no menciona" unidades ni region; [-1000, 1000] HU | `chen2026foundationvae.md` §1, §4.1; filas NO ENCONTRADO | si |
| l.78 | Guo: autoencoder con TC; similitud, no HU; rango no declarado | `guo2025maisi.md` Tabla 1; NO ENCONTRADO | si |
| l.80 | De Man: mecanismos aislados en el sinograma | `deman1999.md` | si |
| l.80 | Lin: 31.45 frente a 33.51 dB; variante con sinograma interpolado; problema mal planteado | `lin2019.md` Tabla 1 p. 10509; Sec. 2 p. 10506 | si |
| l.80 | Li: rama de solo imagen por debajo; \GAPDATO de cifras | `li2024.md`:51; `MAPA.md`:72 | si |
| l.80 | Sin sintesis de artefacto solo en imagen; supuesto que la comparacion con el protocolo fisico podria contradecir | #61; `capitulo3.tex`:261 | si |
| l.82 | De Man (varilla de hierro, amalgama, 2D); Park (*cupping* frente a rayas); Glover y Pelc (monocromatico, hueso); Selles (25 pacientes, regiones no definidas por distancia); Li (global) | fichas respectivas; `li2024.md`:18 | si |
| l.84 | Radzi: desde el eje; umbral no publicado; 2.0/2.6/1.6/2.0 mm; tornillos de 3.5-4.0 mm; un tobillo | `radzi2014metalartifacts.md` pp. 163-167 | si |
| l.84 | Cassanego: 3.1-4.2 mm; metodo del anterior; referencia no declarada | `cassanego2026evolution.md` Tabla 3 p. 7; M&M p. 3 | si |
| l.84 | $B_\delta$ de unos 12 mm = convencion | TM:79; `capitulo3.tex`:176 | si |
| l.86 | Sin banda numerica previa; Hu 1.3 r; Jin sin mm; truncamiento de rayas lejanas | fichas; `capitulo3.tex`:261 | si |
| l.90 | Muestreador y SAP ejecutados; \GAPDATO sin muestras sinteticas | `capitulo3.tex`:38; #116; `MAPA.md`:30 | si |
| l.101-109 | Celdas de los nueve trabajos | cuerpo l.18-74 y fichas | si (T05 r02 corregido) |
| l.111 | Fila propia (poses preinscritas, $G = M \cup B_\delta$, copia del resto, SAP, *streak amplitude*, protocolo fisico) | `capitulo3.tex`:172, 189, 217-219 | si |
| l.116 | Lectura por columnas | l.40-44, l.74-76 | si |
| l.118 | Brecha con las palabras de la introduccion; protocolo en un subconjunto y segun el plazo; \GAPDEC sintetizador aprendido | `introduccion.tex`:54; `capitulo3.tex`:221, 225; #128.1; `MAPA.md`:66 | si |
| l.120 | Tres elementos; segundo sin ajuste; ningun objetivo aisla el primero ni el tercero | `introduccion.tex`:58-60; `capitulo3.tex`:207 | si |
| l.120 | Ida y vuelta sin autoencoder no verificada; \GAPDEC | `p1_compuerta.md`:31-38; `e6c_techo_lw.md`:21 | no (T01) |
| l.122 | Mascara tubular de Wang 2019 que no proviene de segmentar metal | `wang2019cochlear.md` Sec. 2.1 p. 3 | si |
| l.122 | Formas de Zhang y Yu, Karageorgos, Peters; umbral solo en metal clinico (Yun, Wang 2025, Li) | fichas; `yun...md`:37; `wang2025...md`:110; `li2024.md`:46 | si (T01 r02 corregido; PAT-77 no reincide) |
| l.122 | Xie: cortes simulados, 2500 HU, SE 100 %, Dice 82.92 %; lectura propia | `xie2024implantsegmentation.md`:47-48, 282-287 (Results p. 6; Tabla 2 p. 11) | si |
| l.122 | Salvedad: entrenamiento con mascaras umbralizadas; desplazamiento de dominio | `capitulo3.tex`:178, 182 | si (PAT-69 no reincide) |
| l.124 | Piezas ya publicadas | secciones 2.1-2.4 | si |
| l.124 | \GAPDEC reformulacion de la novedad | #56 (act. 2026-09-21), ABIERTA; `MAPA.md`:73 | si |
| l.126 | Supuesto y convencion; evaluacion por coherencia, no por segmentacion | #61; `docs/00-tesis.md` Fuera de alcance pto 1 | si |
| global | 43 claves `\cite` | todas en `overleaf/referencias.bib` (recuento 43/43) | si |
| global | Apellido nombrado = primer autor del `.bib` | `.bib` (Liu J., Karageorgos, Herman, Xie, Wang Z./Wang H., Wu M./Wu L., Zhang Y./Zhang L., etc.) | si |
| global | Contenido retirado (Dice/HD95 como objetivo, latente/ControlNet vigente, "31-60%", BFC/ISC) | texto completo | si: ausente |
| global | Cita como sujeto gramatical (E-F3); dos autores sin "et al." (PAT-74) | texto completo | si: ninguna |
| global | Fuentes de fabricante | ninguna | si |
| global | Prepublicaciones senaladas (`wu2025freetumor`, `chen2026foundationvae`) | `.bib` @misc | si |
| global | Implicancias ABIERTAS afirmadas como hecho (#8, #11, #16/#17, #56, #57, #61, #106/#117, #113, #116, #128) | todas como GAP, supuesto o sin afirmar | si |
| global | Fichas "solo abstract" con cifras de cuerpo | `zhang2026pediclescrew` sin cifras | si |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un GAP replicado de otra seccion arrastra una ausencia que un experimento propio ya midio | G-T4, OC-2 | "error de ida y vuelta ... sin autoencoder, pendiente" (P1 y E6c lo midieron) | PAT-19 |
| Un dato ajeno sobre un subconjunto compartido pierde el tamano de la version que uso la fuente | E-P3 | "Evaluan ademas sobre el subconjunto CLINIC-metal" (14 volumenes, 30 imagenes) | PAT-31 |
