# Auditoria de trazabilidad — capitulo2 — r05

Seccion: `overleaf/secciones/capitulo2.tex` (Cap. II, 135 lineas). Lint r05: PASA 0/0/0, GAP lit=1 dato=2 dec=9
(recontados en el texto: dec en l.12, 28, 64, 72, 74 x2, 82, 126, 132; dato en l.88 y 98; lit en l.80).
Respuesta previa: `capitulo2-r04-respuesta.md`. Los cinco hallazgos de r04 estan aplicados: T01 (12 casos, l.54 y
l.115), T02 (Peters, "en uno de los experimentos", l.113), T03 (remision en texto plano, anotada en MAPA), T04
("distribucion ordinal clinica", l.66) y T05 (celda propia, l.119). No re-reporto lo que la respuesta dejo como
pendiente fuera de la seccion (1: `introduccion.tex`:46 y `capitulo3.tex`:172; 2: `\label` del cap. 4; 4: "zona
segura") ni lo mandado antes a relectura (Ramzan Sec. 3.5, Herman p. 8, Hu Fig. 3). Las 44 claves `\cite` existen en
`overleaf/referencias.bib` (conteo exacto 44/44). No abri ningun PDF.

Revise en especial lo que cambio en r04:
- **Parrafo nuevo del criterio de la compuerta (l.86):** las tres cifras coinciden con las fichas (`karageorgos2024ddpm.md`:41, 44,
  Tabla I p. 28; `yun2026simulationdriven.md`:97, 187, Tabla 1 p. 10) y la condicion "sobre datos simulados" es correcta
  para las dos. El respaldo de que la escala, y no una equivalencia, fija el criterio esta en DEC 2026-09-15 (2)
  (`01-decisiones.md`:814-829). Dos problemas: el 20.2 queda con la unica cita de Peters et al. (T01), y la
  omision de la unidad, que respeta la decision de BITACORA §2 (capitulo2-r03), choca con DEC y con `capitulo3.tex`:67,
  que dan HU (T02).
- **Ida y vuelta sin autoencoder (l.82):** respaldada (`experiments/objetivo1/p1_compuerta.md`:5, 31-38, columnas de
  identidad; `e6c_techo_lw.md`:7-21, "Sin VAE"). El `\GAPDEC` de codificacion y precision sigue justificado.
- **"12 casos" del 86.7 % (l.54, l.115):** coincide con `liu2025pipeline.md`:96, 98.
- **Salvedad de $B_\delta$ en el aporte (l.128):** coincide con `introduccion.tex`:60 para la codificacion y la banda, pero la
  razon que se atribuye a la introduccion para la geometria no es la suya (T08, baja).
- **"Clinica" en el negativo bajo S1 (l.66):** coincide con `capitulo3.tex`:164. Frente a Smith et al. (cadaveres) el negativo
  ahora se sostiene.
- **"Esquema multiventana" para la MAR:** l.80, 82, 124, 132, conforme a BITACORA §2 (capitulo2-r03). "Codificacion
  multiventana" queda solo para el uso propio (l.82, 84, 128, 132).

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, E-R6 | l.86 | "Para el algoritmo de MAR con que Peters et al. calibran ... el RMSE es de 20.2" | `peters2025hybrid.md`:49, 158 (NMAR = 2, 2.5 p. 5; ninguna fila con 20.2); `karageorgos2024ddpm.md`:44 (NMAR RMSE 20.2, Tabla I p. 28) | La oracion no dice quien reporta el 20.2, y su unica cita es `peters2025hybrid`. En IEEE, el numero entre corchetes queda pegado a la cifra y el lector se la atribuye a Peters et al., cuya ficha no la trae. La cifra es de Karageorgos et al., medida en sus datos simulados | "En esos mismos datos, Karageorgos et al. reportan un RMSE de 20.2 para el algoritmo de MAR con que Peters et al.~\cite{peters2025hybrid} calibran la escala de sus metricas." |
| T02 | media | G-T4, OC-5 (ficha insuficiente) | l.86 (y l.94) | "RMSE ... de 12.3 ... es de 20.2 ... de 12.74" | `karageorgos2024ddpm.md`:41, 44, 142 (sin unidad); `yun2026simulationdriven.md`:97, 105 (sin unidad); `01-decisiones.md`:821-824 ("RMSE 20.2 HU", "12.3 HU", "12.74 HU"); `capitulo3.tex`:67 (en HU); `04-implicancias.md`:5153 ("Cifra en HU") | No es error del texto: sin unidad, cumple BITACORA §2 (capitulo2-r03, "cifra cuya ficha no trae unidad va sin unidad"). Pero dos fuentes del repositorio difieren: DEC 2026-09-15 (2), decision de la autora, da las tres en HU, y las fichas no dan unidad. Ademas, el parrafo usa esas cifras como escala de un criterio en HU, y esa funcion depende de que esten en HU. El cap. 3 las da en HU y el cap. 2 no. Ya esta en los pendientes del redactor (r04, pendiente 3); lo subo a hallazgo porque el parrafo nuevo lo vuelve argumento del capitulo | Relectura con `lector-papers` de `karageorgos2024ddpm` (Tabla I p. 28, Tabla III p. 16, Sec. II-G) y de `yun2026simulationdriven` (Tabla 1 p. 10, Sec. 2.4.2) para la unidad del RMSE. Si la confirma, agregar "HU" en l.86 y l.94. Si no, reportar a la autora la discrepancia con DEC y con `capitulo3.tex`:67 |
| T03 | baja | E-P3, G-T4 (PAT-31) | l.86 | "La escala mas proxima la dan los errores de la MAR sobre datos simulados" | `04-implicancias.md`:6531-6535 (analisis del asesor: RMSE de imagen completa fuera del metal; hueso sin tope en la tesis); `karageorgos2024ddpm.md`:49-53 (RMSE_ROI de 20-52 en casos clinicos); ficha sin la region de la Tabla I | Patron PAT-31 reincide en forma leve. El parrafo retoma cifras medidas sobre la imagen para anclar un criterio medido solo en hueso, y no dice sobre que region se midieron. La ficha no registra esa region; solo la da el analisis del asesor en #91 | Tras la relectura de T02, agregar la region ("en la imagen completa", si la ficha lo confirma). Si no se confirma, dejarlo asi y no afirmar ninguna region |
| T04 | baja | E-R6 | l.86 | "Yun et al. reportan un RMSE de 12.74 para su modelo de difusion latente" | `yun2026simulationdriven.md`:97 (MLD-MAR); l.38 del mismo capitulo (correccion en proyeccion + LDM); `04-implicancias.md`:5179 ("12.74 HU es la tuberia entera") | El 12.74 es el error del metodo completo, que incluye la correccion del endurecimiento del haz en proyeccion. No es el error del modelo de difusion latente solo. La l.38 lo describe bien, y la l.86 lo acota al modelo | "... para su metodo, que combina la correccion en proyeccion con la difusion latente" o "para su metodo completo" |
| T05 | baja | G-T4, E-T1 (PAT-14) | l.86 | "La escala mas proxima ... la escala de sus metricas ... Con esa escala" | l.72 ("escala de cuatro grados de Smith"); `peters2025hybrid.md`:89 (escala 0-4) | Patron PAT-14 reincide. En el mismo parrafo, "escala" significa dos cosas: el orden de magnitud de los errores y la puntuacion 0-4 de Peters et al. Justo en la oracion de T01, eso vuelve mas probable que el lector crea que el 20.2 pertenece a la escala de Peters | Para los errores, "orden de magnitud" (como `capitulo3.tex`:67 y DEC); "escala" solo para la puntuacion de Peters |
| T06 | baja | G-B8, G-T1 (PAT-67) | l.119 (tabla, fila propia) | "se comparara por *streak amplitude* con la insercion por copia y pegado" | cuerpo del cap. 2 (la insercion por copia y pegado no aparece fuera de la tabla); `capitulo3.tex`:217 | Patron PAT-67 reincide. La celda tiene fuente en el cap. 3, pero ninguna oracion del cuerpo del cap. 2 presenta la comparacion con la insercion por copia y pegado. BITACORA §2 (capitulo2-r01) pide que toda celda tenga una oracion de respaldo en el cuerpo | Nombrarla en l.126 junto al protocolo fisico ("... como comparacion para la apariencia, junto con la insercion por copia y pegado"), o quitarla de la celda |
| T07 | baja | G-T1, G-T4 (PAT-88) | l.82 | "La ida y vuelta ... sin autoencoder se midio en los experimentos del Objetivo 1" | `p1_compuerta.md`:31-38; `e6c_techo_lw.md`:7; `capitulo3.tex` sec:obj1 (l.56-75, sin esa medicion); `introduccion.tex`:46 ("no lo verifica ningun objetivo") | Patron PAT-88 reincide: el resultado esta en el repositorio, pero el diseno del Obj 1 en el cap. 3 no describe esa medicion, y la introduccion afirma lo contrario. El cap. 2 es el que coincide con los datos. No reabro lo que la respuesta dejo pendiente (1); lo anoto porque el patron sigue VIGENTE | Fuera de la seccion: describir la medicion de identidad en `capitulo3.tex` sec:obj1 y alinear `introduccion.tex`:46 (pendiente 1 del redactor) |
| T08 | baja | E-R6 | l.128 | "Como declara la justificacion ..., ningun objetivo aisla la geometria ..., porque el Objetivo 3 evalua ..." | `introduccion.tex`:58 (geometria: "porque ningun brazo de comparacion coloca geometrias extraidas por umbral"); :60 (codificacion y banda: "porque el Objetivo 3 evalua el sintetizador completo") | La oracion atribuye a la introduccion una sola razon para las tres piezas. Para la geometria, la introduccion da otra | "Como declara la justificacion de la introduccion, ningun objetivo aisla la geometria parametrica, porque ningun brazo coloca geometrias extraidas por umbral, ni la codificacion ni la banda, porque el Objetivo 3 evalua el sintetizador completo." |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.8 | Comparacion por objetivos; tabla con fila propia | `redaccion/MAPA.md` (fila capitulo2) | si |
| l.10 | Orden de las secciones y su relacion con los Obj 1-4 y con $B_\delta$ | estructura del capitulo | si (PAT-71 no reincide) |
| l.12 | Sin busqueda sistematica; lista de la autora; fichas con frase y pagina; candidatos; busquedas dirigidas fechadas | `CLAUDE.md` raiz, reglas 2 y 15; `_candidatos.md` | si |
| l.12 | Una sola fuente de la que solo se tuvo el resumen, sin cifras | `zhang2026pediclescrew.md` ("solo abstract") | si |
| l.12 | \GAPDEC protocolo de busqueda | `MAPA.md` | si |
| l.16 | Dos familias; rayas que irradian desde el metal | fichas de chen2024, ramzan, jacob, lefusion, diffboost, konz; `deman1999.md` | si |
| l.18 | DiffTumor: latente, mascara + region sana; sin textura exterior; [-175, 250] HU; Dice 62.5 -> 66.5 % con una de tres redes, cinco particiones; cuatro radiologos, cerca de la mitad | `chen2024tumorsynthesis.md` §3.2 p. 4; Ap. E.2 p. 21; Tabla 4 p. 17; §4.1 pp. 5-6 | si |
| l.20 | Ramzan: RM, dominio de imagen, perdida en mascara, fondo con ruido; adaptado de LeFusion; Dice 58.89 -> 63.53; fondo cualitativo | `ramzan2026claim.md`; `zhang2025lefusion.md` | si |
| l.22 | LGESynthNet: latente + ControlNet; bordes + imagen enmascarada; sin restitucion; Dice 0.72 -> 0.77 con 300; SSIM 0.587; cicatriz < 1 %; lectura propia | `jacob2026lgesynthnet.md` Sec. 3.1; Tablas 1-2 | si |
| l.24 | DiffBoost: ControlNet sobre SD, desde ruido; parches al azar; 78.46 -> 84.56, 94.42 -> 94.78, 62.92 -> 71.65 % | `zhang2025diffboost.md` §III; Tabla II p. 3678 | si |
| l.24 | Konz: mascara concatenada; [0, 255]; Dice 0.8980; 40 pacientes | `konz2024anatomicallycontrollable.md` | si |
| l.26 | Hu: 1.3 r; Jin: GAN, region de borde; Wu 2025 prepublicacion, conserva el exterior | `hu2023.md` Tabla 1; `jin2021freetumor.md` 3.4.1; `wu2025freetumor.md` Ec. 1 | si |
| l.28 | RePaint: sin reentrenar; 256 x 256; sin TC ni metal; sintetizador genera una region y copia el resto; \GAPDEC muestreo | `lugmayr2022repaint.md` 5.1; `capitulo3.tex`:172; #106/#117 ABIERTAS | si |
| l.30 | Cinco con segmentacion; dos con similitud; uno con prueba visual; negacion partida por familia | fichas respectivas | si |
| l.34 | Zhang y Yu 15 formas, 120 kVp, Poisson, "no menciona"; Lin 100 formas; Wang 2019 tubular, 1090 volumenes, cinco energias; Karageorgos CatSim/XCIST | `zhang2018.md`; `lin2019.md`; `wang2019cochlear.md`; `karageorgos2024ddpm.md` II-A | si |
| l.36 | Haneda 31 %; Karageorgos sinograma, traza, reinsercion por umbral, SSIM 0.964, 13 de 28 en cuatro TC clinicas | `haneda2025aapm.md` 3.1 p. 11; `karageorgos2024ddpm.md` Tabla I, III-C | si |
| l.38 | Yun: correccion en proyeccion + LDM; CLINIC-metal por inferencia; metal por umbral; 0.82 HU frente a 3.18-6.30 HU de cuatro metodos | `yun2026simulationdriven.md`:41, 110, 192-193 (Tabla 4 p. 11) | si |
| l.40 | Peters: CatSim calibrado; 14 000 casos; fractales; ocho metricas; 29 escenarios; < 2 %; < 10 %; 13.3 % en un experimento | `peters2025hybrid.md` 2.1-2.4, 3.1 p. 6 | si |
| l.42 | La validacion no cubre el paso hibrido, la geometria generica ni la osteosintesis 3D | idem; `capitulo3.tex`:221 | si |
| l.44 | Peters al azar / *meaningful locations*; Karageorgos >= 50 % en > 200 HU; Wang 2019 centro; Wang 2025 a mano; formula de la carencia | fichas; BITACORA §2 capitulo2-r02 | si |
| l.46 | Wu 2022: primer orden, Ti 20 mm, Fe 10 mm; Haneda > 3.0 cm, 274 de 14 000 | `wu2022xcist.md`; `haneda2025aapm.md` | si |
| l.48 | Ren: sondas, varilla Ti 12.7 mm, dos crioablaciones, datos del fabricante, modal | `ren2022metalinsertion.md` | si |
| l.52 | Orden de 2.3 | l.54-74 | si (PAT-71 no reincide) |
| l.54 | Liu: 14 casos de CTPelvic1K; optimizacion; plan unico; 2.56 mm y 3.31 grados; encuesta sobre 12 casos, 86.7 %, tres cirujanos; 10.58 ± 3.84 frente a 4.36 ± 3.83 mm; sin iliosacros; no sacro | `liu2025pipeline.md`:25-28, 85, 90, 96, 98, 112, 116-117 | si (T01 r04 corregido; PAT-79 no reincide) |
| l.56 | Zhang 2026 solo resumen; sin cifras | `zhang2026pediclescrew.md` | si |
| l.58 | Ramzan 17 segmentos; Chen elipsoides; Jacob elipsoide al azar | fichas | si |
| l.60 | Zwingmann 2009: cuatro niveles; 69 % y 40 %; p = 0.02 | `zwingmann2009navigated.md` | si |
| l.62 | Metaanalisis: 2.6 % (1832), 0.1 % (262); cero de 2009; criterio de revision | `zwingmann2013.md` | si |
| l.64 | Zwingmann 2010: 63 y 131; 81/11/3/5; 42/22/21/13 + 2 %; solape; \GAPDEC | `zwingmann2010percutaneous.md`; #113 ABIERTA | si |
| l.66 | Herman 36.5 % y 14.8 %, p = 0.035; ninguno del todo fuera; "distribucion ordinal clinica por debajo de S1"; S1 asumido | `herman2016.md`; `capitulo3.tex`:164, 196, 259 | si (T04 r04 corregido) |
| l.68 | Kaiser 104; McLaren 433 / 352; Ramadanov y Zabler; Ziran 17 pelvis, 7-25 %, 97-140 % | fichas respectivas | si (PAT-76 no reincide) |
| l.70 | Cuatro carencias frente al Obj 2 | l.44, 54, 58, 60-64 | si |
| l.72 | Zwingmann radiologo, borde; Smith cuatro cadaveres, escala heredada y angular; Herman binaria; Liu margen; \GAPDEC angular | `smith2006iliosacral.md`; #11 ABIERTA | si |
| l.74 | Arand 50 TC *post mortem*; sin HU ni calibracion; \GAPDEC densidad; tres de ocho metricas de Peters; \GAPDEC inversion | `arand2019pelvicring.md`; `04-implicancias.md` #50; #16/#17 ABIERTAS | si |
| l.78 | Saturacion <= 600 HU (Chen, Hu, Jin, Wu 2025); umbral 2500 HU (Wang 2025, Li) | fichas | si |
| l.80 | Wang 2025: tres ventanas, cascada, peso aprendido; \GAPLIT; PSNR/SSIM; 14 volumenes CLINIC-metal por inferencia; cinco medicos, 30 imagenes; 26.76 dB / 0.9501 frente a 32.67 / 0.9803; lectura propia | `wang2025adaptiveweighting.md`; `MAPA.md`; `_candidatos.md` | si |
| l.82 | Li: ventanas en perdida y evaluacion; entrada [-1000, 2000] HU; +0.64 dB; techo < 2500 HU; "no reclama el esquema" | `li2024.md`:38, 45, 58 | si |
| l.82 | Ida y vuelta de las variantes sin autoencoder medida en el Obj 1, fuera de la regla | `p1_compuerta.md`:5, 31-38; `e6c_techo_lw.md`:7-21 | si (PAT-88, T07) |
| l.82 | \GAPDEC codificacion y precision del sintetizador | `diseno_A.md` (borrador, `[SUPUESTO]`); DEC sin decision; `MAPA.md` | si (justificado) |
| l.84 | Rombach; Chen 2026 prepublicacion, [-1000, 1000] HU, "no menciona"; Guo sin rango declarado | fichas | si |
| l.86 | Sin umbral publicado de aprobacion (acotado a fuentes revisadas) | DEC 2026-09-15 (2) (`01-decisiones.md`:818-819); `04-implicancias.md`:5146-5149 | si |
| l.86 | Karageorgos RMSE 12.3 (difusion) sobre datos simulados | `karageorgos2024ddpm.md`:41 (Tabla I p. 28) | si (unidad: T02) |
| l.86 | RMSE 20.2 del algoritmo con que Peters calibra | `karageorgos2024ddpm.md`:44; `peters2025hybrid.md`:49, 158 | parcial (T01, T02) |
| l.86 | Yun RMSE 12.74 | `yun2026simulationdriven.md`:97, 187 | parcial (T04) |
| l.86 | Escala, no equivalencia, fija el criterio (remite a sec:obj1) | DEC 2026-09-15 (2) :827-829; `capitulo3.tex`:67 | si (T03, T05) |
| l.88 | De Man; Lin 31.45 frente a 33.51 dB; problema mal planteado; Li con \GAPDATO; "se asume" | `lin2019.md`; `li2024.md`; `MAPA.md`; #61 | si (PAT-85 no reincide) |
| l.90 | De Man, Park, Glover y Pelc, Selles (25 pacientes), Li | fichas | si |
| l.92 | Radzi 2.0/2.6/1.6/2.0 mm, desde el eje, un tobillo; Cassanego 3.1-4.2 mm, seis miembros; $B_\delta$ ~12 mm como convencion | `radzi2014metalartifacts.md`; `cassanego2026evolution.md`; TM:79; `capitulo3.tex`:176 | si |
| l.94 | Karageorgos: pelvis con dos marcadores de oro virtuales; RMSE 7.57, 11.45 (1.4), 54.82 (0.7); lectura propia | `karageorgos2024ddpm.md`:54, 56, 58, 171, 173 | si (sin unidad, como l.86: T02) |
| l.98 | Muestreador y SAP ejecutados; \GAPDATO sin muestras sinteticas | `capitulo3.tex`:38; `ESTADO.md`:115, 710 | si |
| l.109-117 | Nueve filas: cifras y condicion | cuerpo y fichas | si |
| l.119 | Fila propia: supuesto, convencion, poses preinscritas, $G$, SAP ejecutado, *streak amplitude*, copia y pegado, protocolo segun el plazo | `capitulo3.tex`:125-134, 172, 217, 225 | parcial (T06) |
| l.124 | Lectura por columnas; esquema multiventana para quitar | l.40-44, 80-82 | si |
| l.126 | Brecha con las palabras de la introduccion; protocolo en un subconjunto segun el plazo; \GAPDEC sintetizador aprendido | `introduccion.tex`:54; #128.1 | si |
| l.128 | Tres elementos; perturbacion del eje del corredor segun distribucion preinscrita; sin ajuste; ningun objetivo aisla | `capitulo3.tex`:125-134; `introduccion.tex`:58, 60 | parcial (T08) |
| l.130 | Wang 2019 tubular; Zhang y Yu, Karageorgos, Peters; umbral automatico (Yun, Wang 2025, Li); Xie 2500 HU, sensibilidad 100 %, Dice 82.92 %; salvedad de mascaras umbralizadas | fichas; `xie2024implantsegmentation.md`; `capitulo3.tex`:178, 182 | si (PAT-69, PAT-87 no reinciden) |
| l.132 | Piezas publicadas; formulacion posible; \GAPDEC novedad | #56 ABIERTA | si |
| l.134 | Supuesto y convencion; evaluacion por coherencia, no por segmentacion | #61; `docs/00-tesis.md` Fuera de alcance 1 | si |
| global | 44 claves `\cite` | `overleaf/referencias.bib` (44/44) | si |
| global | Apellido nombrado = primer autor; dos autores sin "et al." (Zhang y Yu, Ramadanov y Zabler, Glover y Pelc) | `.bib` | si |
| global | Cita como sujeto gramatical (E-F3) | texto completo | si: ninguna |
| global | Contenido retirado (Dice/HD95 como objetivo, latente/ControlNet como metodo vigente, "31-60%", BFC/ISC) | texto completo | si: no aparece; el sintetizador propio es de dominio de imagen |
| global | Fuentes de fabricante | ninguna | si |
| global | Prepublicaciones senaladas (`wu2025freetumor`, `chen2026foundationvae`) | `.bib` @misc | si |
| global | Implicancias ABIERTAS afirmadas como hecho (#11, #16/#17, #56, #61, #106/#117, #113, #128) | todas como GAP, supuesto o formulacion posible | si |
| global | Fichas "solo abstract" con cifras del cuerpo | `zhang2026pediclescrew` sin cifras | si |
| global | Patrones VIGENTES: PAT-14 (T05), PAT-19 (no), PAT-31 (T03), PAT-66 (no), PAT-67 (T06), PAT-69 (no), PAT-70 (no), PAT-71 (no), PAT-76 (no), PAT-79 (no), PAT-80 (no), PAT-83 (no), PAT-84 (no), PAT-85 (no), PAT-86 (no: la formula repetida es decision §2), PAT-87 (no), PAT-88 (T07), PAT-89 (no) | texto completo | ver hallazgos |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Cifra de la fuente A en una oracion cuya unica `\cite` es la fuente B, citada por otro motivo | G-T4, E-R6 | "con que Peters et al. \cite{peters} calibran ..., el RMSE es de 20.2" | nuevo |
| Una decision de estilo (omitir la unidad sin ficha) deja la cifra distinta entre capitulos y de DEC | G-T4, OC-5 | cap. 2 "RMSE de 12.3"; cap. 3 y DEC "12.3 HU" | nuevo |
| Se atribuye a otra seccion una razon que esa seccion da solo para una parte | E-R6 | "Como declara la justificacion ..., ningun objetivo aisla ..., porque ..." (dos razones distintas) | PAT-64 (afin) |
