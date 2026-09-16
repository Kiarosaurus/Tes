# ramzan2026claim — CLAIM: sintesis de cicatriz miocardica en LGE guiada por AHA-17

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. URL: arXiv:2506.15549v2 [cs.CV], 25 Jun 2025 (sello lateral, p.1). Codigo: https://github.com/farheenjabeen/CLAIM-Scar-Synthesis (abstract, p.1). Venue "Artificial Intelligence in Healthcare": NO ENCONTRADO EN EL PDF (el PDF es preprint arXiv, sin mencion de revista/conferencia).
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/ramzan2026claim.pdf (14 paginas)

## Que hace (3 lineas maximo)
Genera cicatrices de infarto en MRI cardiaca de realce tardio (LGE) con un modelo de difusion
condicionado por mascara, mas un modulo (SMILE) que muestrea mascaras de cicatriz plausibles
sobre el modelo clinico AHA de 17 segmentos del ventriculo izquierdo.
Entrena en alternancia el generador y un segmentador nnU-Net (joint training) y evalua el
beneficio downstream en Dice sobre EMIDEC y un dataset privado.

## Restriccion o supuesto clave
CLAIM es inpainting acotado en el sentido mas estricto de los cuatro papers agrupados en
`main.tex` linea 48: la perdida esta enmascarada y la composicion de pixeles es explicita.

- Perdida enmascarada (Sec. 2.1, p.4): "to ensure that the diffusion model operates only on
  manipulating the specified scar regions" con `L1(e_t, e^_t; M_f) = ||M_f * e_t - M_f * e^_t||_2^2` (Ec. 1).
- Reinsercion explicita de pixeles en cada paso de muestreo (Sec. 2.1, p.5):
  `x^_{N_{t-1}} = o_{N_{t-1}} (x) M_f + x_{N_{t-1}} (x) (1 - M_f)`, donde `o` es lo generado y
  `x_{N_{t-1}}` es la imagen real ruidificada hacia adelante. Frase: "The background mask (1-M_f)
  is applied ... to preserve the non-lesion regions."
- Se distancia explicitamente del esquema tipo LDM de condicionar con el fondo (Sec. 1, p.2):
  "these methods explicitly integrate forward-diffused background directly during the iterative
  diffusion process".

Consecuencia para implantes metalicos: por construccion, CLAIM no puede producir NINGUN efecto
fuera de `M_f` (streaking, beam hardening, banda extendida B_delta). El fondo esta congelado
por diseno, no por falta de capacidad del generador. Ademas, su patologia objetivo es una
region de intensidad difusa y bordes mal definidos ("poorly defined contours owing to low soft
tissue contrast", Sec. 1, p.2), lo opuesto a un cuerpo rigido de borde duro.

Sobre NO-RIGIDEZ: el paper NUNCA enuncia un supuesto de deformabilidad ni de no-rigidez del
tejido como premisa del generador -> NO ENCONTRADO EN EL PDF. El termino "non-rigid" aparece
solo como metodo de registro dentro de SMILE (Sec. 2.2, p.6: "non-rigid registration (i.e. fast
symmetric forces demons method)"), es decir aplicado al warping de mascaras entre espacio
plantilla y sujeto, no como supuesto sobre la fisica del objeto sintetizado.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| EMIDEC: 100 casos (67 patologicos, 33 normales) | "provides 100 labeled short-axis DE-MRI ... includes 67 pathological and 33 normal cases" | Sec. 3.1, p.7 |
| Privado out-of-domain: 80 casos patologicos | "We used 80 pathological cases from a private dataset" | Sec. 3.1, p.7 |
| Baseline Dice 58.89 vs CLAIM (J) 63.53 | Tabla 2, filas "Baseline" y "CLAIM (J) (Ours)" | Tabla 2, p.11 |
| Composicion de pixeles con mascara de fondo | "The background mask (1-M_f) is applied ... to preserve the non-lesion regions" | Sec. 2.1, p.5 |

## Donde entra en mi tesis
Estado del arte de sintesis de lesiones (Sec. de related work, `main.tex` linea 48). Es el
ejemplo mas limpio de "bounded inpainting" con reinsercion explicita de pixeles, y por lo tanto
el contraejemplo mas util para justificar la banda de generacion extendida B_delta del
renderizador. Tambien es analogo metodologico del muestreador: SMILE es un muestreador de
localizacion guiado por un atlas clinico (AHA-17), igual que el muestreador de esta tesis usa
mapas de densidad osea y zonas seguras. NO es baseline: modalidad, organo y metricas no son
comparables.

## Dudas para el asesor
- Citar SMILE como precedente de "muestreador clinico separado del renderizador" fortalece la
  arquitectura de dos componentes de la tesis, o confunde al lector por venir de cardiologia?
- La frase de `main.tex` linea 48 agrupa cuatro papers bajo dos supuestos que solo se cumplen
  parcialmente (ver implicancia #56). Conviene dividirla en dos frases, una por atributo?
- CLAIM no reporta ninguna metrica de fidelidad de imagen (FID/SSIM/PSNR/LPIPS): solo Dice de
  segmentacion. Vale la pena usarlo como argumento de que el campo evalua sintesis por proxy
  downstream, justo lo que esta tesis declara fuera de alcance?

## Evidencia textual

| # | Dato / umbral / criterio | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|---|
| 1 | Perdida de ruido restringida a la mascara de cicatriz | "to ensure that the diffusion model operates only on manipulating the specified scar regions" | Sec. 2.1, p.4 |
| 2 | Ecuacion de perdida enmascarada (Ec. 1) | "L1(et, e^t; Mf) = ||Mf * et - Mf * e^t||^2_2" | Ec. 1, p.4 |
| 3 | Reinsercion explicita de pixeles (composicion m*gen + (1-m)*orig) | "x^{Nt-1} = o{Nt-1} (x) Mf + x{Nt-1} (x) (1 - Mf)" | Sec. 2.1, p.5 |
| 4 | Proposito de la composicion: preservar el fondo | "The background mask (1-Mf) is applied to ... preserve the non-lesion regions" | Sec. 2.1, p.5 |
| 5 | Objetivo declarado: generar con "background preserving" | "synthesize pathological images with diverse scar patterns with background preserving" | Sec. 2.1, p.5 |
| 6 | Problema que motiva el diseno: alucinacion en el fondo | "unintended alterations and contextual artifacts appear in background (non-lesion) regions" | Sec. 1, p.2 |
| 7 | Rechazo explicito del condicionamiento tipo LDM sobre el fondo | "explicitly integrate forward-diffused background directly during the iterative diffusion process" | Sec. 1, p.2 |
| 8 | Esquema de inpainting heredado (RePaint [19]) | "synthesize images by using an inpainting scheme [19] to fill the pathological regions" | Sec. 1, p.2 |
| 9 | Unica evaluacion del fondo: cualitativa, no metrica | "the background regions remain preserved in all methods" | Sec. 3.4, p.8 |
| 10 | Base generativa: DDPM, NO latente, NO Stable Diffusion | "a conditional diffusion model based on Denoising Diffusion Probabilistic Model (DDPM)" | Sec. 2, p.3 |
| 11 | Modelo adaptado de LeFusion | "Our diffusion model is adapted from the one used in LeFusion [16], a lesion-focused diffusion model" | Sec. 2.1, p.4 |
| 12 | Backbone del denoiser | "The diffusion model (often implemented as a UNet parameterized by theta)" | Sec. 2.1, p.4 |
| 13 | Condicionamiento de textura: histograma de control (NO ControlNet) | "with the guidance of a control histogram h that produced from the specified scar regions" | Sec. 2.1, p.4 |
| 14 | Dimensionalidad del generador (2D / 2.5D / 3D) declarada | NO ENCONTRADO EN EL PDF (solo se dice "3D blob" dentro de SMILE, Sec. 2.2, p.6) | — |
| 15 | Uso de ControlNet | NO ENCONTRADO EN EL PDF | — |
| 16 | Uso de Stable Diffusion / autoencoder latente | NO ENCONTRADO EN EL PDF (LDM [20] solo se cita para contrastar) | — |
| 17 | Condicionamiento por prompt de texto | NO ENCONTRADO EN EL PDF | — |
| 18 | Guia clinica: modelo AHA de 17 segmentos | "conditions a diffusion-based generator on the clinically adopted AHA 17-segment model" | Abstract, p.1 |
| 19 | Division anatomica usada para muestrear localizacion | "divides the LV myocardium into 17 segments in basal, middle and apical regions" | Sec. 2.2, p.5 |
| 20 | Segmentos por nivel | "basal (regions 1-6), middle (regions 7-12) and apical (regions 13-17) slices" | Sec. 2.2, p.6 |
| 21 | Muestreo de tamano de cicatriz | "We sampled a list of scar volumes for each myocardial region from a uniform distribution" | Sec. 2.2, p.6 |
| 22 | Control de textura de la mascara | "Texture was controlled via anisotropy, and volume by adjusting porosity, followed by erosion" | Sec. 2.2, p.6 |
| 23 | Tamano de kernel de erosion | "a randomly selected kernel (1x1 to 7x7)" | Sec. 2.2, p.6 |
| 24 | Post-proceso de la mascara | "Post-processing included hole filling, Gaussian smoothing, and removal of isolated regions" | Sec. 2.2, p.6 |
| 25 | Registro NO RIGIDO (solo como metodo de registro, no como supuesto) | "followed by non-rigid registration (i.e. fast symmetric forces demons method [30])" | Sec. 2.2, p.6 |
| 26 | Transferencia plantilla->sujeto usa no-rigido + rigido | "using non-rigid (fast symmetric forces demons) and then rigid registration" | Sec. 2.2, p.6 |
| 27 | Supuesto explicito de no-rigidez o deformabilidad del tejido sintetizado | NO ENCONTRADO EN EL PDF | — |
| 28 | Atlas AHA-17 usado | "The AHA-17 atlas/template is provided by Bai W., et al. [29]" | Nota al pie 6, p.6 |
| 29 | Perdida de segmentacion (Ec. 2) | "Lseg(Mf, M^f) = LDice(Mf, M^f) + LWCE(Mf, M^f)" | Ec. 2, p.5 |
| 30 | Backbone de segmentacion | "The segmentation model is based on ... nnUNet [25]" | Nota al pie 5, p.5 |
| 31 | EMIDEC: total de casos etiquetados | "provides 100 labeled short-axis DE-MRI (Delayed Enhancement MRI)" | Sec. 3.1, p.7 |
| 32 | EMIDEC: reparto patologico/normal | "This includes 67 pathological and 33 normal cases" | Sec. 3.1, p.7 |
| 33 | Dataset privado (out-of-domain) | "We used 80 pathological cases from a private dataset" | Sec. 3.1, p.7 |
| 34 | EMIDEC: normales 33, patologicos 67 (tabla) | Tabla 1, fila EMIDEC: "33 | 67" | Tabla 1, p.7 |
| 35 | EMIDEC: pixel spacing | Tabla 1: "1.25x1.25, 2x2" mm | Tabla 1, p.7 |
| 36 | EMIDEC: grosor de corte / distancia | Tabla 1: "8" mm / "10" mm | Tabla 1, p.7 |
| 37 | EMIDEC: volumen de cicatriz (media+-sd) | Tabla 1: "23.68+-15.81" | Tabla 1, p.7 |
| 38 | Privado: 0 normales, 80 patologicos | Tabla 1, fila Private: "0 | 80" | Tabla 1, p.7 |
| 39 | Privado: pixel spacing | Tabla 1: "0.89x0.89,1.7x1.7" mm | Tabla 1, p.7 |
| 40 | Privado: grosor de corte / distancia | Tabla 1: "8-10" mm / "10" mm | Tabla 1, p.7 |
| 41 | Privado: volumen de cicatriz (media+-sd) | Tabla 1: "14.33+-13.62" | Tabla 1, p.7 |
| 42 | Split de patologicos EMIDEC | "57 real pathological cases for training image synthesis models and 10 for testing" | Sec. 3.2, p.7 |
| 43 | Split de normales EMIDEC | "We split 33 normal cases into 28 cases for testing image synthesis models and 5 for validation" | Sec. 3.2, p.7 |
| 44 | Preproceso de intensidad para sintesis | "the image intensity was rescaled between -1 and 1" | Sec. 3.2, p.7 |
| 45 | Recorte de imagen para sintesis | "images were cropped from the center based on the bounding boxes obtained from the corresponding masks" | Sec. 3.2, p.7 |
| 46 | Entrenamiento del generador: epocas y LR | "trained for 50,000 epochs with a learning rate of 1e-4 using Adam optimizer" | Sec. 3.2, p.7 |
| 47 | Entrenamiento de segmentacion: epocas, LR, optimizador | "trained for 1000 epochs and stochastic gradient descent (SGD) ... learning rate of 1e-2" | Sec. 3.2, p.7 |
| 48 | Esquema de LR de segmentacion | "'polyLR' scheme: (1 - epoch/epoch_max)^0.9" | Sec. 3.2, p.7 |
| 49 | Definicion de subconjuntos P, N', N'', P' | "P: 57 real pathological cases. N': (28x2) synthetic pathological cases generated from 28 normal cases" | Fig. 5 / Tabla 2, p.10-11 |
| 50 | Baseline (solo datos reales), Dice | Tabla 2, "Baseline ... P ... 58.89" | Tabla 2, p.11 |
| 51 | Baseline, precision / sensibilidad / especificidad | Tabla 2: "70.99 | 62.35 | 99.35" | Tabla 2, p.11 |
| 52 | Mejor Dice global: CLAIM (J) con P+P'+N'' | Tabla 2: "CLAIM (J) (Ours) ... 63.53 | 73.88 | 64.71 | 99.07" | Tabla 2, p.11 |
| 53 | CLAIM (J) con P+N' | Tabla 2: "63.07 | 74.13 | 63.52 | 99.11" | Tabla 2, p.11 |
| 54 | CLAIM (J) con P+N'' | Tabla 2: "63.27 | 73.77 | 64.32 | 99.07" | Tabla 2, p.11 |
| 55 | LeFusion+DiffMask (P+N'), Dice | Tabla 2: "LeFusion [16] | DiffMask | ... | 59.50" | Tabla 2, p.11 |
| 56 | Sensibilidad maxima NO es de CLAIM (J) | Tabla 2: LeFusion+SMILE P+N' sensibilidad "63.97" (negrita) | Tabla 2, p.11 |
| 57 | Metricas reportadas para segmentacion | "We report the performance of each method using Dice score, precision, sensitivity and specificity" | Sec. 3.5, p.9 |
| 58 | Metricas de fidelidad de imagen (FID, SSIM, PSNR, LPIPS) | NO ENCONTRADO EN EL PDF | — |
| 59 | Medida cuantitativa de degradacion FUERA de la mascara | NO ENCONTRADO EN EL PDF (solo afirmacion cualitativa, item 9) | — |
| 60 | Criterio de evaluacion del fondo: imagen de diferencia (cualitativo) | "plotted the difference image between input normal images and output synthetic images" | Sec. 3.4, p.8 |
| 61 | Efecto del joint training en intensidad de la lesion | "shows high intensity (brighter) in the scar regions as compared to the models trained without" | Sec. 3.4, p.8 |
| 62 | Criterio de evaluacion de mascaras: comparacion visual vs DiffMask | "our generated masks display varied forms, sizes and locations" | Sec. 3.4, p.8 |
| 63 | Limitacion de DiffMask (esfera de control) | "This ball shaped sphere can be used for enclosed organs (such as lungs, kidneys etc.)" | Sec. 3.4, p.8 |
| 64 | Evaluacion adicional: volumen de cicatriz por segmento AHA (bull's eye) | "assessed the performance ... in terms of scar volume (ML) distribution using the AHA-17 segment framework" | Sec. 3.5, p.11 |
| 65 | DISCREPANCIA interna: abstract/contribucion afirma robustez out-of-domain | "showing its improved robustness against domain shift" | Contribuciones, p.3 |
| 66 | DISCREPANCIA interna: el resultado matiza esa afirmacion | "segmentation performance on out-of-domain data increased initially and then dropped" | Sec. 3.5, p.9 |
| 67 | DISCREPANCIA interna (2): joint training no siempre mejor | "our model based on joint training did not always produce better results on out-of-domain-data" | Sec. 3.5, p.9-10 |
| 68 | Causa atribuida al fallo out-of-domain | "The reason for worse performance on external data is mainly the significant volume differences" | Sec. 3.5, p.10 |
| 69 | Resultados out-of-domain: solo en figura de barras, sin tabla numerica | Fig. 5(b) "Private (out-of-domain data)", ejes Dice 0.05-0.5 sin valores tabulados | Fig. 5, p.10 |
| 70 | Mencion de metal o implantes metalicos | NO ENCONTRADO EN EL PDF | — |
| 71 | Mencion de unidades Hounsfield (HU) | NO ENCONTRADO EN EL PDF | — |
| 72 | Mencion de MAR / artefacto metalico / streaking / beam hardening | NO ENCONTRADO EN EL PDF | — |
| 73 | Mencion de CT | Solo en trabajo relacionado: "lung nodules in computed tomography images [12, 13]" | Sec. 1, p.2 |
| 74 | Modalidad y organo del trabajo | "short-axis LGE-MRI scans with scar labelled by our cardiologists" | Sec. 3.1, p.7 |
| 75 | Numero de pagina / DOI de revista | NO ENCONTRADO EN EL PDF (preprint arXiv 2506.15549v2) | p.1 |

## Impacto sobre la tesis (propuesta del lector)

**(a) Veredicto sobre la implicancia #56 (frase de `main.tex` linea 48), atributo por atributo:**

- **"bounded inpainting" -> RESPALDA, y es el caso mas fuerte de los cuatro.** No solo la
  perdida esta enmascarada (Ec. 1, p.4: "operates only on manipulating the specified scar
  regions"), sino que el muestreo compone pixeles paso a paso con la mascara. A diferencia de
  `jacob2026lgesynthnet`, aqui la imagen completa NO pasa por un latente: el fondo son los
  pixeles reales difundidos hacia adelante.
- **"strictly restrict intensity alterations to the inside of the object's mask" -> RESPALDA,
  con formula explicita.** `x^_{N_{t-1}} = o_{N_{t-1}} (x) M_f + x_{N_{t-1}} (x) (1 - M_f)`
  (Sec. 2.1, p.5). Es exactamente la composicion `m*generado + (1-m)*original` que la frase de
  la tesis atribuye al grupo. CLAIM es el unico de los cuatro donde esa atribucion es literal.
  Matiz honesto: el fondo conservado es el fondo *ruidificado* del paso t-1, no el original
  intacto; el paper no mide cuanto difiere el fondo final del original (item 59).
- **"non-rigidity" -> NO RESPALDA.** El paper no enuncia en ningun punto un supuesto de
  deformabilidad o no-rigidez del tejido (item 27: NO ENCONTRADO EN EL PDF). El unico uso de
  "non-rigid" es como algoritmo de registro dentro de SMILE, para warpear mascaras entre
  plantilla y sujeto (items 25 y 26). Atribuirle "assume non-rigidity" es una lectura del
  lector de la tesis, no una afirmacion del paper. Nota: SMILE si *depende operativamente* de
  que el miocardio sea registrable no-rigidamente, lo que es evidencia indirecta; pero eso es
  el muestreador de mascaras, no el renderizador, y la frase de `main.tex` habla del modelo de
  sintesis.

**Estado consolidado de #56 tras los cuatro papers:** "bounded inpainting" se sostiene en 3 de 4
(cae con `zhang2025diffboost`). "Strictly inside the mask" se sostiene en 2 de 4 (cae con
`zhang2025diffboost` y `jacob2026lgesynthnet`). **"Non-rigidity" no esta enunciada explicitamente
en NINGUNO de los cuatro PDFs** (confirmado aqui el tercer caso; ver fichas previas). La frase
actual es insostenible tal como esta escrita.

**(b) Obliga a ajustar:**

- **Redaccion: SI.** Recomiendo separar la frase en dos y dejar de atribuir "non-rigidity" a los
  papers. Propuesta para la autora (no aplicada, regla 14): afirmar la restriccion que SI esta
  documentada (composicion de pixeles enmascarada / perdida enmascarada) citando
  `chen2024tumorsynthesis` y `ramzan2026claim` como los casos literales, y tratar la no-rigidez
  como *observacion propia* sobre el dominio de aplicacion (tumores, cicatrices, polipos), no
  como supuesto declarado por los autores.
- **Alcance: no.** Modalidad (LGE-MRI), organo (VI) y ausencia total de metal/CT/HU (items 70-73)
  confirman que CLAIM es analogo metodologico, no competencia ni baseline.
- **Supuesto: refuerza el de la tesis.** La composicion explicita de pixeles es el argumento
  positivo mas claro a favor de la banda extendida B_delta (~12 mm): si el fondo se recompone
  con los pixeles originales, el streaking fuera del metal es matematicamente imposible.
- **Baseline: no.** No entra como brazo de comparacion.
- **Gap nuevo: SI, uno pequeno.** CLAIM no reporta ninguna metrica de fidelidad de imagen
  (item 58) ni ninguna medida de preservacion cuantitativa del fondo (item 59): valida sintesis
  solo por Dice downstream. Como esta tesis declara la evaluacion downstream FUERA DE ALCANCE,
  conviene documentar que el estado del arte de sintesis de lesiones carece de metricas
  directas de coherencia fisica, que es justamente lo que esta tesis propone medir.

**(c) Nivel sugerido: 2 (metodo).** Se necesita el detalle exacto de la Ec. 1, la formula de
composicion de p.5 y SMILE para sostener el argumento de #56 y el precedente del muestreador;
no se reimplementa nada.

**(d) Acceso y paginas:** acceso completo (texto completo, 14 paginas, preprint arXiv
2506.15549v2, 25 Jun 2025). Sin paywall. Figuras y tablas legibles. Resultados out-of-domain
solo en grafico de barras sin tabla numerica (item 69): no hay cifras citables para ese
experimento.
