# Auditoria de trazabilidad — capitulo2 — r04

Seccion: `overleaf/secciones/capitulo2.tex` (Cap. II, 133 lineas). Lint r04: PASA 0/0/0, GAP lit=1 dato=2 dec=9.
Respuesta previa: `capitulo2-r03-respuesta.md`. Los tres hallazgos de r03 estan corregidos: T01 (ida y vuelta, l.126),
T02 (Liu, l.54) y T03 (Wang, l.80). Lo dejado sin aplicar con motivo no se vuelve a reportar: ES-04 (Dice de Ramzan
sin unidad), T06 de r02 (Ramzan Sec. 3.5) y el 46/129 frente a 36.5 % de Herman, ambos a relectura. Las 44 claves
`\cite` existen en `overleaf/referencias.bib`; la nueva, `arand2019pelvicring`, tiene como primer autor a Arand. No abri
ningun PDF.

Revise en especial lo que cambio en r03:
- **Tabla comparativa:** las nueve cifras de la ultima columna coinciden con el cuerpo y con las fichas. La celda de
  Liu et al. pierde la condicion de la tasa de aceptacion (T01), y la de Peters et al. pierde la de su 13.3 % (T02).
- **GAP de ida y vuelta (l.126):** esta justificado. `p1_compuerta.md`:31-38 mide la identidad sin autoencoder y
  `e6c_techo_lw.md`:21 la mide por precision, fuera de la regla (`p1_compuerta.md`:5). La codificacion y la precision
  no estan decididas en DEC: `diseno_A.md`:57 y :69 las marcan como `[SUPUESTO]` y borrador.
- **GAP de densidad (l.74):** esta justificado. D-O2.6 (`01-decisiones.md`:1502-1506) calcula la fraccion sobre E9b,
  que el 2026-09-14 (#50) se retiro como evidencia de densidad (`04-implicancias.md`:8799).
- **Herman (l.66):** las cifras y la lectura propia estan bien respaldadas. La negacion sobre la distribucion ordinal
  bajo S1 pierde el calificativo "clinica" que tiene en el cap. 3 (T04).
- **Orden de 2.3 (l.52):** describe el orden real.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | E-P3, G-T4 (PAT-31) | l.113 (tabla, fila Liu); l.54 | "Error de reduccion de 2.56 mm y 3.31 grados en 14 casos; aceptacion de 86.7 %" | `liu2025pipeline.md`:96 ("on 12 cases treatable by implantation fixation", IV-B p. 16); :98 ("86.7% for C3 and the overall score", IV-B p. 17); :25 (14 casos, VI p. 14) | Patron PAT-31 reincide. La encuesta de los tres cirujanos se hizo sobre 12 casos, no sobre los 14. En la tabla, "en 14 casos" va junto a la tasa, y la columna promete dar "su condicion", asi que el lector le atribuye n = 14. El cuerpo (l.54) tiene la misma ambiguedad: "prueban su planificacion en 14 casos ... aceptacion ... del 86.7 % segun tres cirujanos". La cifra coincide con la ficha y el error esta en la condicion. Es un argumento nuevo, no una re-apertura: la columna de condicion se agrego en r03 | Tabla: "... en 14 casos; aceptacion de 86.7 % en 12 casos, segun tres cirujanos". Cuerpo l.54: "y, en una encuesta sobre 12 de esos casos, una tasa de aceptacion clinica del 86.7 % segun tres cirujanos" |
| T02 | baja | E-P3 (PAT-31) | l.111 (tabla, fila Peters) | "discrepancia del ruido de hasta 13.3 % en regiones con artefacto" | `peters2025hybrid.md`:195, 464 ("up to 13.3% in Exp 4", 3.1 p. 6); cuerpo l.40 ("en uno de los experimentos") | La celda deja fuera la condicion que el cuerpo si da: el 13.3 % sale de un solo experimento. Como el "hasta" ya lo acota, el error de fondo es menor | "... hasta 13.3 % en regiones con artefacto, en uno de los experimentos" |
| T03 | baja | G-T4 | l.126 | "su resultado se presenta en el capitulo de resultados" | `overleaf/secciones/capitulo4.tex` (solo `\chapter`, sin `\label` ni contenido) | La remision apunta a un capitulo que todavia esta vacio y no se puede referenciar. Cumple la decision de BITACORA §2 (capitulo3-r00: los veredictos van al cap. 4), pero el lector no puede comprobarla | Cuando exista, poner `\label{cap:resultados}` en el cap. 4 y usar `Capitulo~\ref{cap:resultados}`. Si el cap. 4 no se escribe antes de la entrega, anotar la remision en la fila del `\GAPDEC` de MAPA (l.40) |
| T04 | baja | E-P3, G-T4 (PAT-66) | l.66 | "ninguna de las fuentes revisadas da la distribucion ordinal que haria falta" | `capitulo3.tex`:164 ("ninguna ... reporta una distribucion ordinal **clinica** por debajo de S1"); `smith2006iliosacral.md`:69, 195 (grados de 0 a 3 por tornillo en S1 y S2, sobre cuatro cadaveres) | Sin el calificativo "clinica", el negativo no se sostiene frente a Smith et al., que dan grados ordinales de tornillos en S2 sobre cadaveres. Ademas, la misma conclusion queda redactada distinto en el cap. 3 | "ninguna de las fuentes revisadas da una distribucion ordinal clinica por debajo de S1, que haria falta para comparar ..." |
| T05 | baja | G-T4 | l.117 (tabla, fila propia) | "Diseno, sin resultado del sintetizador: SAP frente a la referencia clinica; ..." | l.96 ("el muestreador y SAP se ejecutaron"); `capitulo3.tex`:243 | La celda mete la comparacion de SAP con la referencia clinica dentro de "Diseno", aunque esa comparacion ya se corrio. No hay error de cifra: se diluye la distincion entre lo ejecutado y lo pendiente que la l.96 si hace | "SAP frente a la referencia clinica, ejecutado (resultado en el capitulo de resultados); sin resultado del sintetizador: *streak amplitude* frente a ..." |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.8 | Comparacion por objetivos; tabla con fila propia | `redaccion/MAPA.md`:18 | si |
| l.10 | Orden de las secciones y su relacion con los Obj 1-4 y con $B_\delta$ | estructura del capitulo | si |
| l.12 | Sin busqueda sistematica; lista de la autora; fichas con frase y pagina; candidatos; busquedas dirigidas fechadas | `CLAUDE.md` raiz, reglas 2 y 15; `_candidatos.md` | si |
| l.12 | Una sola fuente de la que solo se tuvo el resumen, sin cifras | `zhang2026pediclescrew.md` ("solo abstract"); `wang2025adaptiveweighting.md`:13 (etiqueta retirada); `song2024bmar` no se cita | si |
| l.12 | \GAPDEC protocolo de busqueda | `MAPA.md`:68 | si |
| l.16 | Dos familias (*inpainting* acotado; corte entero desde ruido) | fichas de chen2024, ramzan, jacob, lefusion, diffboost, konz | si |
| l.16 | Rayas que irradian desde el metal | `deman1999.md` | si |
| l.18 | DiffTumor: difusion latente, mascara + region sana; no modela la textura de fuera; [-175, 250] HU | `chen2024tumorsynthesis.md` §3.2 p. 4; Ap. E.2 p. 21 | si |
| l.18 | Dice en higado de 62.5 a 66.5 %, con una de tres redes, media de cinco particiones; cuatro radiologos, cerca de la mitad tomada por real | idem, Tabla 4 p. 17; §4.1 pp. 5-6 | si |
| l.20 | Ramzan: RM cardiaca, dominio de imagen, perdida dentro de la mascara, fondo real con ruido; esquema adaptado de LeFusion | `ramzan2026claim.md` filas 1-4, 10-11, 74 | si |
| l.20 | LeFusion: nodulos pulmonares en TC, perdida en la lesion, exterior real con ruido | `zhang2025lefusion.md` | si |
| l.20 | Dice de 58.89 a 63.53 en la mejor configuracion; sin metricas de fidelidad; fondo evaluado de forma cualitativa | `ramzan2026claim.md` filas 50, 52, 58, 59 | si (ES-04 no se re-reporta) |
| l.22 | LGESynthNet: latente + ControlNet; mapa de bordes + imagen enmascarada; decodifica la imagen completa; sin paso de restitucion | `jacob2026lgesynthnet.md` Sec. 3.1 p. 3; "Buscado sin resultado" | si |
| l.22 | Dice de 0.72 a 0.77 con 300 imagenes; SSIM 0.587; cicatriz < 1 %; perdida atribuida a la compresion; lectura propia | idem, Tabla 2 p. 8; Tabla 1 p. 7; Sec. 1 y 5; BITACORA §2 | si |
| l.24 | DiffBoost: ControlNet sobre SD, desde ruido, corte a corte; texto + borde; parches al azar | `zhang2025diffboost.md` §III, Alg. 1 | si |
| l.24 | 78.46 -> 84.56; 94.42 -> 94.78; 62.92 -> 71.65 % | idem, Tabla II p. 3678 | si |
| l.24 | Konz: mascara concatenada, dominio de imagen, desde ruido; [0, 255]; Dice 0.8980; 40 pacientes | `konz2024anatomicallycontrollable.md` Sec. 2-3, Tabla 1 | si |
| l.26 | Hu: sintesis analitica; efecto de masa hasta 1.3 r | `hu2023.md` Tabla 1 p. 7426 | si |
| l.26 | Jin: parche 3D, GAN, region de borde | `jin2021freetumor.md` Sec. 3.4.1 p. 9 | si |
| l.26 | Wu 2025: prepublicacion; conserva el exterior | `wu2025freetumor.md` Ec. 1; `.bib` @misc | si |
| l.28 | RePaint: sin reentrenar; region conocida conservada; 256 x 256; sin TC ni metal | `lugmayr2022repaint.md` Sec. 5.1 | si |
| l.28 | El sintetizador genera una region y copia el resto | `capitulo3.tex`:172 | si |
| l.28 | \GAPDEC muestreo de la difusion | #106 y #117 ABIERTAS; `MAPA.md`:69 | si |
| l.30 | Cinco con segmentacion posterior; dos con similitud; uno con prueba visual; negacion partida por familia | fichas respectivas; BITACORA §2 introduccion-r05 | si (PAT-64 no reincide) |
| l.34 | Insertar metal virtual es practica establecida en la MAR | fichas de zhang2018, lin2019, wang2019cochlear, karageorgos | si |
| l.34 | Zhang y Yu: 15 formas; 120 kVp; Poisson; "el articulo no menciona" dispersion ni volumen parcial | `zhang2018.md` Sec. IV-A pp. 5-6; filas NO ENCONTRADO | si (PAT-72 no reincide) |
| l.34 | Lin: 100 formas; volumen parcial | `lin2019.md` Sec. 4 p. 10508 | si |
| l.34 | Wang 2019: mascara tubular; 1090 volumenes; Beer-Lambert en cinco energias | `wang2019cochlear.md` Intro p. 2; Sec. 2.1 p. 3 | si |
| l.34 | Karageorgos: objetos a partir de TC de metal; CatSim dentro de XCIST | `karageorgos2024ddpm.md` II-A p. 3 | si |
| l.36 | Haneda: 31 % de los equipos usaron difusion | `haneda2025aapm.md` Sec. 3.1 p. 11 | si |
| l.36 | Karageorgos: difusion en el sinograma, solo sin metal; traza glosada; reinsercion por umbral; SSIM 0.964; 13 de 28 en cuatro TC clinicas con metal virtual | `karageorgos2024ddpm.md` Abstract; II-A p. 4; II-F p. 10; Tabla I p. 28; III-C p. 12 | si |
| l.38 | Yun: correccion en proyeccion + LDM; CLINIC-metal (por inferencia); metal por umbral; 0.82 HU frente a 3.18-6.30 HU de cuatro metodos | `yun2026simulationdriven.md`:11, 36-37, 110, 192-193; `capitulo3.tex`:42 | si |
| l.38 | Ni Karageorgos ni Yun generan el implante | fichas respectivas | si |
| l.40 | Peters: CatSim calibrado contra fantoma; 14 000 casos; fractales; ocho metricas; 29 escenarios; base del desafio | `peters2025hybrid.md` 2.1, 2.3, 2.4 p. 4; `haneda2025aapm.md` | si |
| l.40 | < 2 %; ruido < 10 % sin artefacto evidente; hasta 13.3 % en uno de los experimentos | `peters2025hybrid.md`:42-43, 194-195, 462-464 (3.1 p. 6) | si |
| l.42 | La validacion no cubre el paso hibrido ni la geometria generica; todo en 2D; sin osteosintesis 3D; adaptacion que no hereda la validacion | idem, Verificacion 3a-3b, 4b; `capitulo3.tex`:221 | si |
| l.44 | Peters: hasta cinco objetos al azar; lo ideal, impracticable; *meaningful locations* sin regla | `peters2025hybrid.md` 2.3 p. 4; Discussion p. 9 | si |
| l.44 | Karageorgos >= 50 % con region > 200 HU; Wang 2019 en el centro de una estructura; Wang 2025 insercion a mano en cortes dentales | `karageorgos...md` II-A p. 4; `wang2019cochlear.md` Sec. 2.1; `wang2025...md`:66-69, 209 | si |
| l.44 | Carencia con la formula fijada | BITACORA §2 capitulo2-r02 | si |
| l.46 | Simulador = fundamento tecnico; Wu: primer orden, Ti 20 mm y Fe 10 mm; Haneda: > 3.0 cm, 274 de 14 000 | `CLAUDE.md` raiz; `wu2022xcist.md`:98, 136-137; `haneda...md`:43, 180-182 | si |
| l.48 | Ren: sondas de ablacion; varilla de Ti de 12.7 mm; dos crioablaciones; datos del fabricante; revision con mas metal (modal conservado) | `ren2022metalinsertion.md` Sec. 2.1.3, 2.5, 4 | si |
| l.52 | Orden de 2.3: planificacion, series, lesiones, corredor; carencias del Obj 2 antes que las medidas del Obj 4 | l.54-74 | si (PAT-71 no reincide) |
| l.54 | Liu: 14 casos de CTPelvic1K, "coleccion de la que proceden los datos" | `liu2025pipeline.md`:25 | si (T02 r03 corregido) |
| l.54 | Etiqueta, reduccion, numero/posicion/direccion; optimizacion con tres restricciones; plan unico | idem, "Que hace"; III-D | si |
| l.54 | 2.56 mm y 3.31 grados | idem:26, 85 | si |
| l.54 | 86.7 % segun tres cirujanos | idem:27, 96-98 (12 casos) | parcial (T01) |
| l.54 | 10.58 ± 3.84 frente a 4.36 ± 3.83 mm | idem, Tabla III p. 38 | si |
| l.54 | Cresta, pubis, acetabulo; no menciona iliosacros; no se aplica al sacro; sin distribucion ni imagen | idem:51, 112, 116-117 | si (PAT-79 no reincide) |
| l.56 | Zhang 2026: solo resumen; sCT desde TC de haz conico; pediculares; mitiga el artefacto; sin cifras | `zhang2026pediclescrew.md` | si |
| l.58 | Ramzan (17 segmentos, volumen uniforme, comparacion visual); Chen (elipsoides + radiologos); Jacob (elipsoide al azar) | fichas respectivas | si (PAT-86 no reincide: una sola vez) |
| l.60 | Zwingmann 2009: cuatro niveles; TC posoperatoria; grado 0 en 69 % y 40 %; p = 0.02; referencia clinica | `zwingmann2009navigated.md` M&M p. 1835; Results pp. 1836-1837; `capitulo3.tex`:200 | si |
| l.62 | Metaanalisis: 2.6 % (1832) y 0.1 % (262); cero en la cohorte de 2009; criterio de revision; lectura propia | `zwingmann2013.md` Abstract; Fig. 2; Discusion p. 1264 | si |
| l.64 | Zwingmann 2010: 63 y 131 tornillos; 81/11/3/5 %; 42/22/21/13 % + 2 % en grado 4; posible solape; \GAPDEC | `zwingmann2010percutaneous.md` pp. 1501-1503; #113 ABIERTA; `MAPA.md`:70 | si |
| l.66 | Herman: TC posoperatoria; binaria; por nivel; 36.5 % en S1 y 14.8 % en el segundo segmento; p = 0.035 | `herman2016.md`:68, 109, 127-128 | si (46/129 no se re-reporta) |
| l.66 | Sin distribucion ordinal para el segundo corredor; poses descriptivas | `capitulo3.tex`:164 | parcial (T04) |
| l.66 | Lectura propia: el nivel importa; S1 se asume en la serie navegada | `capitulo3.tex`:259 | si (PAT-78 no reincide) |
| l.66 | Ningun tornillo del todo fuera del hueso; las poses fuera del hueso reciben grado 3 en SAP | `herman2016.md`:181 (Resultados p. 7); `capitulo3.tex`:196 | si |
| l.68 | Kaiser 104 TC; McLaren 433 y 352 en S1; Ramadanov y Zabler, cualitativo; Ziran 17 pelvis, CV de 7-25 % y de 97-140 %; consecuencia para el muestreador | `kaiser2014dysmorphism.md`:81; `mclaren2021corridor.md`:67; `ramadanov2025safezone.md`; `ziran2007fluoroscopic.md` pp. 348-352; `capitulo3.tex` sec:muestreador | si (PAT-76 no reincide) |
| l.70 | Cuatro carencias frente al Obj 2 | l.44, l.54, l.58, l.60-64 | si |
| l.72 | Zwingmann: un radiologo; borde no declarado; escala de Smith; Smith: cuatro cadaveres, escala heredada, escala angular; Herman binaria; Liu, margen de un plan | `zwingmann2009navigated.md`; `smith2006iliosacral.md`:66, 79, 84-87 | si |
| l.72 | SAP calcula el grado; \GAPDEC dimension angular | `capitulo3.tex`:189; #11 ABIERTA; `MAPA.md`:41 | si |
| l.74 | Fraccion por zona de densidad como componente de SAP | `capitulo3.tex`:189; D-O2.6 (`01-decisiones.md`:1502) | si |
| l.74 | Arand como motivacion del diseno (sec:poses) | `capitulo3.tex`:166 (dentro de sec:poses, l.125-169) | si |
| l.74 | Arand: 50 TC *post mortem*, adultos sin lesion, modelo medio de valores de gris por voxel; ala sacra baja | `arand2019pelvicring.md`:96, 101, 110-111, 115 | si |
| l.74 | Sin HU numericos ni calibracion; lo relaciona con la planificacion y la colocacion, no como restriccion | idem:106-107 (NO ENCONTRADO), 104; "Restriccion o supuesto clave" | si |
| l.74 | \GAPDEC fraccion por zona de densidad | D-O2.6 frente a DEC 2026-09-14 (#50); `04-implicancias.md`:8799; `MAPA.md`:39; mismo texto que `introduccion.tex`:43 | si (justificado) |
| l.74 | Tres de ocho metricas de Peters, disenadas para la MAR; \GAPDEC inversion | `capitulo3.tex`:213-215; #16 y #17 ABIERTAS; `MAPA.md`:42 | si |
| l.78 | Saturacion <= 600 HU (Chen, Hu, Jin, Wu 2025); umbral de 2500 HU (Wang 2025, Li) | fichas; `wang2025...md`:110; `li2024.md`:46 | si |
| l.80 | Wang 2025: tres ventanas; peso aprendido; en cascada; \GAPLIT del esquema | `wang2025...md`:45-54, 108; `MAPA.md`:71; `_candidatos.md` | si |
| l.80 | 26.76 dB / 0.9501 frente a 32.67 dB / 0.9803; lectura propia | idem:276-277 (V-B p. 2414) | si |
| l.80 | 14 volumenes de CLINIC-metal (por inferencia); 30 imagenes; cinco medicos | idem V-A-2, V-C-3; `capitulo3.tex`:42 | si (T03 r03 corregido) |
| l.82 | Li: ventanas en la perdida y en la evaluacion; entrada [-1000, 2000] HU; +0.64 dB; techo por debajo de 2500 HU | `li2024.md`:38, 45, 58; #39 | si |
| l.82 | Entrada y salida del sintetizador; variantes de techo (sec:obj1) | `capitulo3.tex`:172, 56-75 | si |
| l.84 | Rombach; Chen 2026 (prepublicacion, [-1000, 1000] HU, "no menciona"); Guo (similitud, rango no declarado); sin error en HU dentro del hueso | fichas respectivas; filas NO ENCONTRADO | si |
| l.86 | De Man; Lin 31.45 frente a 33.51 dB; problema mal planteado; Li con \GAPDATO; "se asume" | `lin2019.md` Tabla 1, Sec. 2; `li2024.md`:51; `MAPA.md`:72; #61 | si (PAT-85 no reincide) |
| l.88 | De Man, Park, Glover y Pelc, Selles (25 pacientes), Li | fichas respectivas | si |
| l.90 | Radzi: desde el eje; 2.0/2.6/1.6/2.0 mm; tornillos de 3.5-4.0 mm; un tobillo | `radzi2014metalartifacts.md` pp. 163-167 | si |
| l.90 | Cassanego: 3.1-4.2 mm; tornillos de 3.0-3.5 mm; condilo humeral; seis miembros toracicos caninos cadavericos | `cassanego2026evolution.md`:12, 35-36, 55, 98-104 | si |
| l.90 | $B_\delta$ de unos 12 mm como convencion | TM:79; `capitulo3.tex`:176 | si |
| l.92 | Sin banda numerica previa; Hu, Jin | fichas | si |
| l.92 | Karageorgos: caso de pelvis con dos marcadores de oro virtuales; RMSE 7.57; 11.45 con 1.4 veces el area; 54.82 con 0.7 | `karageorgos2024ddpm.md`:54, 56, 58, 171, 173 (Tabla III p. 16; Apendice p. 15); sin unidad en la ficha | si (PAT-84 corregido) |
| l.96 | Lectura de la tabla; muestreador y SAP ejecutados; \GAPDATO sin muestras sinteticas | `capitulo3.tex`:38; #116; `MAPA.md`:30 | si |
| l.107-115 | Ultima columna de las nueve filas: cifra y condicion | cuerpo l.18-80 y fichas | parcial (T01, T02) |
| l.117 | Fila propia: supuesto, convencion, poses preinscritas, $G = M \cup B_\delta$, SAP, *streak amplitude*, protocolo fisico segun el plazo | l.132; `capitulo3.tex`:172, 189, 217, 225 | si (T05, baja) |
| l.122 | Lectura por columnas | l.40-44, l.80-82 | si |
| l.124 | Brecha con las palabras de la introduccion; protocolo en un subconjunto y segun el plazo; \GAPDEC sintetizador aprendido | `introduccion.tex`:54; `capitulo3.tex`:221, 225; #128.1; `MAPA.md`:66 | si |
| l.126 | Tres elementos; segundo sin ajuste | `introduccion.tex`:58-60; `capitulo3.tex`:207 | si |
| l.126 | Ida y vuelta sin autoencoder medida en el Obj 1, fuera de la regla | `p1_compuerta.md`:5, 13, 31-38; `e6c_techo_lw.md`:21 | si (T01 r03 corregido) |
| l.126 | "se presenta en el capitulo de resultados" | `capitulo4.tex` vacio | parcial (T03) |
| l.126 | \GAPDEC codificacion y precision del sintetizador | `diseno_A.md`:57 (`[SUPUESTO]` `pub+asinh`), :69 (float32, borrador); DEC sin decision; `MAPA.md`:40 | si (justificado) |
| l.126 | Ningun objetivo aisla la geometria ni la codificacion | `introduccion.tex` justificacion | si |
| l.128 | Mascara tubular de Wang 2019; formas de Zhang y Yu, Karageorgos, Peters; umbral en metal clinico (Yun, Wang 2025, Li) | fichas; `yun...md`:37; `wang2025...md`:110; `li2024.md`:46 | si (PAT-77 no reincide) |
| l.128 | Xie: cortes simulados, 2500 HU, sensibilidad 100 %, Dice 82.92 %; lectura propia; entrenamiento con mascaras umbralizadas | `xie2024implantsegmentation.md`:47-48, 282-287; `capitulo3.tex`:178, 182 | si (PAT-69 no reincide) |
| l.130 | Piezas ya publicadas; \GAPDEC reformulacion de la novedad | secciones 2.1-2.4; #56 ABIERTA; `MAPA.md`:73 | si |
| l.132 | Supuesto y convencion; evaluacion por coherencia, no por segmentacion | #61; `docs/00-tesis.md` Fuera de alcance, punto 1 | si |
| global | 44 claves `\cite` (se agrega `arand2019pelvicring`) | todas en `overleaf/referencias.bib` | si |
| global | Apellido nombrado = primer autor del `.bib` (Arand, Herman, Liu, Karageorgos, Wang, Zhang, Chen, Wu, etc.) | `.bib` | si |
| global | Contenido retirado (Dice/HD95 como objetivo, latente/ControlNet como metodo vigente, "31-60%", BFC/ISC) | texto completo | si: no aparece; ControlNet y Dice solo como literatura |
| global | Cita como sujeto gramatical (E-F3); entradas de dos autores sin "et al." | texto completo | si: ninguna |
| global | Fuentes de fabricante | ninguna | si |
| global | Prepublicaciones senaladas (`wu2025freetumor`, `chen2026foundationvae`) | `.bib` @misc | si |
| global | Implicancias ABIERTAS afirmadas como hecho (#8, #11, #16/#17, #56, #61, #106/#117, #113, #116, #128) | todas como GAP, supuesto o sin afirmar | si |
| global | Fichas "solo abstract" con cifras del cuerpo | `zhang2026pediclescrew` sin cifras | si |
| global | Coherencia con otras secciones: `introduccion.tex`:46 y `capitulo3.tex`:172 siguen dando la ida y vuelta como no verificada | pendiente declarado en `capitulo2-r03-respuesta.md` (Pendientes 1) y en `MAPA.md`:40 | fuera de alcance (no se reporta) |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| En una celda de resultado, un n junto a una tasa medida sobre un subconjunto distinto | E-P3, G-T4 | "en 14 casos; aceptacion de 86.7 % segun tres cirujanos" (encuesta sobre 12) | PAT-31 |
| Un negativo sobre la literatura pierde, al repetirse en otro capitulo, el calificativo que lo hacia cierto | E-P3, G-B7 | "ninguna ... da la distribucion ordinal" (cap. 3: "ordinal clinica"; Smith da grados en cadaver) | PAT-66 |
