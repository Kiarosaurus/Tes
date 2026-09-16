# jacob2026lgesynthnet — LGESynthNet: sintesis controlada de cicatriz en LGE-MRI cardiaca

- **DOI / URL:** NO ENCONTRADO EN EL PDF. El PDF no imprime DOI ni URL. `refs/raw/jacob2026lgesynthnet.bib`
  trae la cadena `10.1007/978-3-032-17734-6_4` solo como clave de la entrada `@InProceedings`, sin campo
  `doi`, e indica `pages="34--44"`. El PDF local numera sus paginas 1-11 y no muestra la paginacion del
  editor: todas las paginas citadas abajo son las impresas en el PDF (1-11).
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/jacob2026lgesynthnet.pdf

## Que hace (3 lineas maximo)

LDM con ControlNet que sintetiza cicatriz (realce tardio) en cortes de LGE-MRI cardiaca. Lo plantea como
inpainting y lo condiciona con un mapa de bordes de la mascara, la imagen con la region enmascarada y un caption
anatomico (BiomedBERT), con supervision de un modelo de recompensa de segmentacion congelado. Las muestras que
pasan un filtro de calidad (Dice > 0.6) aumentan el entrenamiento de segmentacion y deteccion de LGE.

## Restriccion o supuesto clave

**Modalidad y objeto.** Solo LGE-MRI cardiaca 1.5T. CT aparece solo en Related Work, como dominio donde se
aplicaron otros modelos (*"CT [12, 25]"*, Sec. 2, p. 3). En todo el PDF no hay hueso, metal, implantes, objetos
rigidos ni sintesis de artefactos (ver la tabla de busquedas sin resultado). "Artifacts" aparece una sola vez,
como dificultad de la segmentacion en MRI (*"subtle patterns, imaging artifacts, protocol variability"*, Sec. 1,
p. 1), no como algo que se genere.

**Que supuesto le impide manejar implantes metalicos.** Los tres supuestos que lo impiden estan en el texto,
pero **no coinciden del todo con los que le atribuye `main.tex:48`**:

1. **Inpainting con contexto.** *"Generation is framed as inpainting, conditioned on (a) a scar edge map"*
   y *"(b) an LGE image with the scar region masked with its mean intensity"* (Sec. 3.1, p. 3). Solo se
   reemplaza la region de la cicatriz; lo demas entra como contexto (*"the masked image provides anatomical
   context"*, p. 3). Todo el condicionamiento y la supervision giran en torno a la mascara: la recompensa es la
   entropia cruzada contra la mascara (p. 3) y el filtro exige *"Dice overlap > 0.6 against the conditioning
   mask"* (Sec. 4.3, p. 7). Ningun termino del objetivo pide cambios de apariencia fuera de ella.
2. **Cambios fuera de la mascara: NO los prohibe de forma explicita, y hay indicios de que existen.**
   - No describe ningun paso de pegado o composicion que restituya los pixeles originales fuera de la mascara.
   - La salida se decodifica completa desde el espacio latente. Los autores atribuyen la perdida de calidad a
     esa compresion: *"compressed through the latent space, resulting in lower SSIM"* (Sec. 5, p. 8).
   - La SSIM de imagen completa frente a la imagen real es 0.587 (Tabla 1, p. 7), aunque la cicatriz ocupa
     *"<1% of the image"* (Sec. 1, p. 2). Inferencia propia: la mayor parte de la diferencia cae fuera de la
     mascara.
   - El propio paper dice que generar fuera del corazon esta subdeterminado: *"making the task
     under-constrained"* (Sec. 1, p. 2).
   - La cicatriz generada no calca la mascara: en el downstream se usa *"the predicted mask—not the original
     ellipsoidal mask"* como GT (Sec. 4.3, p. 7).

   Afirmar que el metodo *"strictly restrict[s] intensity alterations to the inside of the object's mask"*
   no es fiel para este paper. Lo que si esta respaldado es que el diseno no pide, supervisa ni evalua
   ningun efecto fuera de la mascara.
3. **Deformable / no rigido.** No hay afirmacion explicita ni implicita de no-rigidez. Lo que se sintetiza es un
   patron de realce de intensidad dentro de un miocardio que no se deforma, no un objeto con geometria propia.
   Las formas son elipsoides parametricos: *"place an ellipsoid, simulating a scar mask"* (Sec. 3.1, p. 4). La
   rigidez no es un tema del paper. Lo que choca con un implante es otra cosa: formas elipticas simples y la
   ausencia de un objeto con frontera geometrica dura.
4. **Intensidades.** Sin HU ni ventanas (es MRI). Un unico recorte al percentil 98 y normalizacion a [0, 1]:
   *"clipped at the 98th percentile, and normalized to [0, 1]"* (Sec. 4.2, p. 7). Por analogia (inferencia
   propia), ese esquema saturaria cualquier cola de alta intensidad, como la del metal en CT.

**Veredicto sobre `main.tex:48` para este paper: PARCIALMENTE FIEL.** "Bounded inpainting" y "biological tissues"
son fieles. "Deformable" e "implicitly assume non-rigidity" no tienen respaldo textual. "Strictly restrict
intensity alterations to the inside of the object's mask" no esta respaldado y el propio PDF lo contradice
indirectamente (puntos 2 y 3).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| (ninguna cifra citada hoy en `main.tex`; se cita solo como ejemplo de sintesis de lesiones) | — | — |

## Donde entra en mi tesis

- **Related Work / Problem Statement (`main.tex:48`).** Es uno de los cuatro ejemplos de sintesis de lesiones.
  Para este paper la frase necesita otra redaccion (ver Dudas). Se sostiene bien que es inpainting centrado en
  la mascara, entrenado y evaluado solo sobre la region de la lesion, sin mecanismo para efectos no locales. No
  se sostienen el "strictly inside" ni la no-rigidez.
- **Renderizador (Objetivo 3), como analogo arquitectonico mas cercano visto hasta ahora.** Comparte LDM +
  ControlNet + mascara/bordes + imagen enmascarada como contexto. Es evidencia externa de dos riesgos:
  - la decodificacion latente degrada la imagen fuera de la region objetivo (p. 8), lo que refuerza el
    criterio ya registrado de medir no-degradacion en el complemento de B_delta;
  - *"high image quality does not imply alignment to conditioning"* (Sec. 6, p. 9): realismo y fidelidad a la
    mascara deben medirse por separado.
- **Control de calidad por segmentador.** El filtro con Dice > 0.6 contra la mascara condicionante evalua
  *"location and rough shape but not texture quality"* (p. 7). Es un precedente de chequeo de adherencia que no
  certifica realismo.
- **Codificacion multi-ventana (C3).** Aporta solo como analogia debil: una unica normalizacion con recorte al
  percentil 98 en MRI.
- **Fuera de alcance aqui:** sus mejoras de Dice y deteccion son evaluacion downstream, que la tesis no mide.
- **Snowballing:** ninguna referencia cumple las reglas de `_candidatos.md`.
  - Ya estan en el repositorio: ControlNet [28] (`zhang2023controlnet`) y CLAIM [22] (`ramzan2026claim`).
  - DiffLGE [2], FCaS [25], ControlPolypNet [24], ControlNet++ [17], ControlNet-XS [27], Khader 2023 [12],
    Muller-Franzes 2023 [20] y T2I-Adapter [19] son sintesis de anatomia o lesiones o metodologia generica, sin
    metal ni artefactos. No son fuente de ninguna cifra de la tesis y no compiten con el renderizador de
    implantes.
  - EMIDEC [16] y Jacob 2025 [9] son especificos de LGE.
  - No se agrego nada a `_candidatos.md`.

## Dudas para el asesor

1. Para LGESynthNet, `main.tex:48` deberia decir algo como: el metodo acota la generacion a una region de lesion
   enmascarada y no modela ni supervisa efectos fuera de ella. Hoy dice "strictly restrict... inside the mask",
   y este paper decodifica la imagen completa y reconoce cambios fuera de la cicatriz. Tambien sobra "implicitly
   assume non-rigidity", que no tiene respaldo aqui. Conviene revisar si CLAIM y DiffBoost justifican esa parte
   por su cuenta.
2. Las cifras del paper no son consistentes entre secciones, y conviene no citarlas sin decidir cual vale:
   - Resumen e Introduccion: "up-to 6" puntos de Dice y "20" de accuracy. Resultados: "5 points" y "12–17 points".
   - Calculo propio, no escrito en el PDF: 6 y 20 salen de la Tabla 3a (Dice 0.78 vs 0.72; balanced accuracy
     0.93 vs 0.73). 5 y 12-17 salen de la Tabla 2 (N = 300).
   - La leyenda de la Tabla 1 dice *"n = 79 patients, 149 images"*, pero el texto da *"149 (29) for testing"*
     (p. 7). 79 es el numero de pacientes de entrenamiento.
3. La ablacion de la Tabla 3b solo informa SSIM y RMSE, no Dice de condicionamiento. Aun asi, el texto afirma
   *"edge inputs outperform masks"* (p. 8).
4. La etiqueta de ablacion *"initialized from SD1.5+semantic masks"* (Tabla 3b, p. 9) sugiere un backbone SD 1.5,
   pero el PDF no lo declara explicitamente para el modelo principal. Es relevante para la discusion abierta
   del VAE (#36/#39) solo como analogia.

## Evidencia textual

Paginas = numeracion impresa en el PDF (1-11). Frases de 15 palabras o menos. En tablas y figuras se transcriben
los valores de celda.

### Datos, modalidad y cohortes

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Modalidad | "Late Gadolinium Enhancement (LGE) cardiac MRI is the gold standard" | Sec. 1, p. 1 |
| Artefactos solo como dificultad | "challenging due to its subtle patterns, imaging artifacts, protocol variability" | Sec. 1, p. 1 |
| 429 imagenes / 79 pacientes | "Trained on just 429 images (79 patients)" | Abstract, p. 1 |
| 429 positivas / 79 pacientes | "trained on just 429 scar-positive LGE images from 79 patients" | Sec. 1, p. 2 |
| Cicatriz < 1% de la imagen | "myocardial scars, which typically occupy <1% of the image" | Sec. 1, p. 2 |
| 212 pacientes; 159 (1516 imagenes) de entrenamiento | "The dataset included 212 patients, split into 159 (1516 images) for training" | Sec. 4.1, p. 4 |
| 20% validacion; 53 (497 imagenes) de test | "(20% validation split) and 53 (497 images) for testing" | Sec. 4.1, p. 4 |
| Escaner 1.5T | "acquired on 1.5T scanners (MAGNETOM Aera, Siemens Healthineers)" | Sec. 4.1, p. 4 |
| Secuencia | "T1-weighted inversion-recovery gradient-echo sequence" | Sec. 4.1, p. 4 |
| Etiquetas binarias por segmento AHA | "assigning binary labels to each segment (1 = scar present, 0 = no scar)" | Sec. 4.1, p. 4 |
| GT semiautomatico | "Pixel-wise GT was then derived semi-automatically from these labels." | Sec. 4.1, p. 4 |
| Umbral n-SD, n = 1.5 | "method [3] with n = 1.5, favoring sensitivity" | Sec. 4.1, p. 6 |
| Refinado manual | "manually refined by removing clusters in clinically normal segments" | Sec. 4.1, p. 6 |
| Generativo: 429 (79) entrenamiento | "Training used only positive LGE images (patients): 429 (79) for training" | Sec. 4.2, p. 7 |
| Generativo: 59 (17) validacion, 149 (29) test | "59 (17) for validation, and 149 (29) for testing" | Sec. 4.2, p. 7 |
| Leyenda Tabla 1 (inconsistente con lo anterior) | "Results on test set (n = 79 patients, 149 images, positive LGE only)" | Tabla 1, p. 7 |
| Leyenda Tabla 2 | "Results on test set: n = 53 patients, 497 real images + 300 synthetic images." | Tabla 2, p. 8 |
| CT solo como trabajo relacionado | "applied to medical imaging (retinal imaging [10, 14], CT [12, 25], MRI [12])" | Sec. 2, p. 3 |

### Arquitectura, condicionamiento y entrenamiento

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| LDM | "LGESynthNet, a latent diffusion-based framework for controllable enhancement synthesis" | Abstract, p. 1 |
| Inpainting + ControlNet | "Formulated as inpainting using a ControlNet-based architecture" | Abstract, p. 1 |
| Control de tamano, ubicacion y transmuralidad | "enabling explicit control over size, location, and transmural extent" | Abstract, p. 1 |
| Componentes | "latent diffusing U-Net, a ControlNet encoder [28], a text encoder" | Sec. 3.1, p. 3 |
| Condicion (a) | "Generation is framed as inpainting, conditioned on (a) a scar edge map" | Sec. 3.1, p. 3 |
| Bordes por Canny | "(via Canny detection of mask)" | Sec. 3.1, p. 3 |
| Condicion (b): region con intensidad media | "(b) an LGE image with the scar region masked with its mean intensity" | Sec. 3.1, p. 3 |
| Papel de cada entrada | "The edge map guides location; the masked image provides anatomical context." | Sec. 3.1, p. 3 |
| Que aprende | "The model learns to synthesize realistic enhancement textures." | Sec. 3.1, p. 3 |
| Entrenamiento vs inferencia | "conditioned on negative LGE image and the intended scar boundaries" | Fig. 1, p. 2 |
| Fuera del corazon, subdeterminado | "Lack of semantic masks over most of the image (e.g., outside the heart)" | Sec. 1, p. 2 |
| Idem | "further complicates generation by making the task under-constrained" | Sec. 1, p. 2 |
| Recompensa congelada | "incorporate it as a fixed reward model S (similar to [17], frozen unlike [22])" | Sec. 3.1, p. 3 |
| Perdida de recompensa | "compared to the ground truth (GT) M_true using cross-entropy loss" | Sec. 3.1, p. 3 |
| Recompensa solo en pasos tempranos | "reward supervision is applied only at early diffusion steps (t ≤ t_thresh)" | Sec. 3.1, p. 3 |
| t_thresh = 200, lambda_reward = 1 | "The reward-guided model used t_thresh = 200 and λ_reward = 1." | Sec. 4.2, p. 7 |
| Dificultad de la recompensa | "selecting an effective reward model is challenging" | Sec. 3.1, p. 4 |
| 17 segmentos AHA y 3 capas radiales | "subdivision of the myocardium into 17 AHA segments [1] and three radial layers" | Sec. 3.1, p. 4 |
| Ejemplo de caption | "Transmural enhancement in the posteroseptal wall" | Sec. 3.1, p. 4 |
| Caption constante de la ablacion | "LGE image of the heart" | Sec. 3.1, p. 4 |
| Encoder de texto | "We replace ControlNet's default encoder (OpenCLIP ViT-H [15]) with BiomedBERT [18]" | Sec. 3.1, p. 4 |
| 50% de captions descartados | "50% of captions are randomly dropped during training [28]" | Sec. 3.1, p. 4 |
| Forma de la mascara sintetica | "select a random region (e.g., anterolateral, endocardial), and place an ellipsoid" | Sec. 3.1, p. 4 |
| Inferencia solo sobre negativas | "we only use negative LGE images for inference in this study for simplicity" | Sec. 3.1, p. 4 |
| Uso sobre positivas: salvedad | "existing LGE patterns need to be taken into account during text and mask generation" | Sec. 3.1, p. 4 |
| Epocas | "They were trained for 200 epochs, using the final epoch weights" | Sec. 4.2, p. 6 |
| Inferencia: 10 pasos, CFG 9 | "for inference with 10 timesteps and classifier-free guidance scale set to 9" | Sec. 4.2, p. 6 |
| Solo ControlNet entrenado | "Only the ControlNet module was trained; other components were frozen." | Sec. 4.2, pp. 6-7 |
| Hardware | "Models were trained on 4 A100 40GB GPUs (BS 64)." | Sec. 4.2, p. 7 |
| Init SD 1.5 (solo en fila de ablacion) | "initialized from SD1.5+semantic masks" | Tabla 3b, p. 9 |

### Preprocesado e intensidades

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Remuestreo 1 mm y recorte 256x256 | "Inputs are resampled to 1mm isotropic, cropped to 256 × 256" | Sec. 4.2, p. 7 |
| Percentil 98 y [0, 1] | "clipped at the 98th percentile, and normalized to [0, 1]" | Sec. 4.2, p. 7 |

### Metodos comparados

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| ControlNet base | "official ControlNet implementation [28], conditioned on scar edge maps and masked LGE images" | Sec. 4.2, p. 6 |
| SPADE-LC | "SPADE-LC (Limited Context), conditioned on myocardial and scar masks only" | Sec. 4.2, p. 6 |
| SPADE-FC | "SPADE-FC (Full Context), conditioned on scar masks and masked LGE images" | Sec. 4.2, p. 6 |
| Template (TCDM) | "appends conditioning inputs with a reference image-mask pair" | Sec. 4.2, p. 6 |

### Criterios de evaluacion y downstream

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Metricas de calidad | "Image quality is assessed using Structural Similarity Index (SSIM) and Root Mean Square Error (RMSE)" | Sec. 4.4, p. 8 |
| Region de calculo | "computed over the entire image and a cropped region of interest around the myocardium" | Sec. 4.4, p. 8 |
| Consistencia de condicionamiento | "average Dice score and the percentage of samples with Dice > 0.6" | Sec. 4.4, p. 8 |
| Metricas downstream | "segmentation Dice score, Dice on True Positive (TP) images-only" | Sec. 4.4, p. 8 |
| Deteccion por paciente | "patient-level LGE detection metrics: accuracy, balanced accuracy, and confusion matrix" | Sec. 4.4, p. 8 |
| Formato de la matriz de confusion | "Confusion matrix is given as [TN, FP, FN, TP]" | Tabla 3, p. 9 |
| Sinteticas a partir de negativas | "generated from negative LGE images conditioned on parametrically defined scar masks" | Sec. 4.3, p. 7 |
| Filtro Dice > 0.6 | "only samples with Dice overlap > 0.6 against the conditioning mask are retained" | Sec. 4.3, p. 7 |
| Alcance del filtro | "This filter assesses scar location and rough shape but not texture quality." | Sec. 4.3, p. 7 |
| GT = mascara predicha | "the predicted mask—not the original ellipsoidal mask—is used as GT" | Sec. 4.3, p. 7 |
| Motivo | "to better capture realistic scar boundaries" | Sec. 4.3, p. 7 |
| Segmentador | "DenseNet121 [7] backbone (5 down-sampling levels) to jointly predict scar and myocardium" | Sec. 4.3, p. 7 |
| Entrenamiento del segmentador | "trained for 200 epochs with Jaccard loss, geometric and elastic augmentations" | Sec. 4.3, p. 7 |
| Hardware y LR | "on 4 A100 40 GB GPUs (BS 128), and cosine annealing(initial LR 0.001)" | Sec. 4.3, p. 7 |
| Seleccion de modelo | "Best model is selected via validation Dice, sensitivity, and specificity." | Sec. 4.3, p. 7 |
| n = 300 sinteticas | "For hybrid training, n = 300 synthetic samples per generative model are added." | Sec. 4.3, p. 7 |
| Fig. 3: 300 sinteticas | "Model training is augmented with 300 synthetic images generated from 3 methods" | Fig. 3, p. 6 |

### Resultados: Tabla 1 (calidad y condicionamiento; p. 7)

Columnas: SSIM / RMSE imagen completa; SSIM / RMSE recortada alrededor del VI; Dice-TP only; Pass%.

| Experimento (condicionamiento) | SSIM completa | RMSE completa | SSIM recorte | RMSE recorte | Dice-TP only | Pass% |
|---|---|---|---|---|---|---|
| Real Images (—) | 1.0 | 0.00 | 1.0 | 0.00 | 0.465 ± 0.32 | 35.6% |
| SPADE-LC (Semantic Masks) | 0.147 ± 0.02 | 0.088 ± 0.02 | 0.159 ± 0.03 | 0.069 ± 0.03 | 0.362 ± 0.30 | 26.2% |
| SPADE-FC (Semantic Masks + Image Context) | 0.974 ± 0.04 | 0.002 ± 0.01 | 0.986 ± 0.01 | 0.001 ± 0.00 | 0.272 ± 0.30 | 18.8% |
| ControlNet (Semantic edges + Image Context) | 0.571 ± 0.05 | 0.008 ± 0.003 | 0.570 ± 0.06 | 0.009 ± 0.00 | 0.230 ± 0.28 | 12.1% |
| ControlNet + Template (Semantic edges + Reference pair) | 0.130 ± 0.03 | 0.102 ± 0.02 | 0.100 ± 0.03 | 0.093 ± 0.03 | 0.002 ± 0.01 | 0.7% |
| LGESynthNet (Semantic edges + Image Context) | 0.587 ± 0.05 | 0.009 ± 0.00 | 0.582 ± 0.06 | 0.009 ± 0.00 | 0.273 ± 0.30 | 18.1% |

Leyenda: "All diffusion models (DM) use Caption Generation module and BiomedBERT text encoder." (Tabla 1, p. 7)

### Resultados: Tabla 2 (downstream, N = 300 sinteticas; p. 8)

| Experimento | Dice | Dice, TP-only | Accuracy | Bal. Accuracy | Matriz [TN, FP, FN, TP] |
|---|---|---|---|---|---|
| Real Images only | 0.72 | 0.32 | 0.77 | 0.73 | [11, 11, 1, 30] |
| SPADE-LC (real + sinteticas) | 0.77 | 0.31 | 0.85 | 0.86 | [20, 2, 6, 25] |
| SPADE-FC (real + sinteticas) | 0.75 | 0.19 | 0.68 | 0.72 | [21, 1, 16, 15] |
| LGESynthNet (real + sinteticas) | 0.77 | 0.35 | 0.89 | 0.90 | [21, 1, 5, 26] |

### Resultados: Tabla 3 (p. 9)

a) Numero de sinteticas en el downstream:

| N samples | Dice | Dice, TP-only | Accuracy | Bal. Accuracy | Matriz [TN, FP, FN, TP] |
|---|---|---|---|---|---|
| 500 | 0.78 | 0.36 | 0.91 | 0.91 | [21, 1, 4, 27] |
| 1000 | 0.77 | 0.36 | 0.92 | 0.93 | [21, 1, 3, 28] |
| 1500 | 0.77 | 0.37 | 0.91 | 0.91 | [20, 2, 3, 28] |

b) Ablaciones (solo SSIM / RMSE):

| Cambio | SSIM completa | RMSE completa | SSIM recorte | RMSE recorte |
|---|---|---|---|---|
| Input condition: semantic masks, initialized from SD1.5+semantic masks | 0.497 ± 0.05 | 0.013 ± 0.005 | 0.490 ± 0.07 | 0.013 ± 0.005 |
| Text encoder: OpenCLIP CLIP-ViT-H | 0.554 ± 0.05 | 0.011 ± 0.007 | 0.550 ± 0.06 | 0.011 ± 0.006 |
| Constant text caption | 0.580 ± 0.05 | 0.008 ± 0.003 | 0.572 ± 0.07 | 0.009 ± 0.004 |

### Resultados en texto y figuras

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Resumen: hasta 6 y 20 puntos | "improve downstream segmentation and detection performance, by up-to 6 and 20 points respectively" | Abstract, p. 1 |
| Intro: hasta 6 (Dice) y 20 (accuracy) | "improves Dice by upto 6 points and patient-level accuracy by upto 20 points" | Sec. 1, p. 2 |
| Resultados: 5 y 12-17 puntos | "improving Dice by 5 points and patient accuracy by 12–17 points" | Sec. 5, p. 8 |
| Estabiliza en N = 1000 | "Performance improves with more synthetic samples (Table 3a), stabilizing at N=1000." | Sec. 5, p. 8 |
| Ablacion | "Ablations (Table 3b) show edge inputs outperform masks" | Sec. 5, p. 8 |
| SPADE-FC | "SPADE-FC yields the best image quality but poor conditioning consistency" | Sec. 5, p. 8 |
| SPADE-FC copia la entrada | "often reproducing input images without realistic scar synthesis" | Sec. 5, p. 8 |
| SPADE-LC | "SPADE-LC creates more plausible scars but with incoherent backgrounds." | Sec. 5, p. 8 |
| Perdida por compresion latente | "image information is compressed through the latent space, resulting in lower SSIM" | Sec. 5, p. 8 |
| Pass rates bajos | "All methods show low pass rates, indicating challenges in condition adherence." | Sec. 5, p. 8 |
| SPADE-FC downstream | "SPADE-FC reduces performance despite high image quality" | Sec. 5, p. 8 |
| SPADE-LC downstream | "SPADE-LC improves detection but not Dice." | Sec. 5, p. 8 |
| Fig. 2, paciente 1: SSIM | Valores de imagen: SPADE-LC 0.14; SPADE-FC 0.99; ControlNet+Template 0.15; ControlNet 0.49; LGESynthNet 0.58 | Fig. 2, p. 5 |
| Fig. 2, paciente 1: Dice | Valores de imagen: 0.86; 0.42; 0.0; 0.17; 0.84 (mismo orden) | Fig. 2, p. 5 |
| Fig. 2, paciente 2: SSIM | Valores de imagen: 0.15; 0.99; 0.13; 0.54; 0.62 (mismo orden) | Fig. 2, p. 5 |
| Fig. 2, paciente 2: Dice | Valores de imagen, lectura dudosa: 0.56; 0.71; 0.0; 0.0; 0.64 (mismo orden). VERIFICAR contra el PDF | Fig. 2, p. 5 |
| Fig. 3, pacientes 2 y 3: Dice | Valores de imagen, lectura dudosa. P2: Real-only 0.41, SPADE-LC 0.65, SPADE-FC 0.0, LGESynthNet 0.83. P3: 0.63, 0.70, 0.52, 0.69. VERIFICAR | Fig. 3, p. 6 |
| Fig. 3, paciente 1: Dice | ILEGIBLE en la resolucion de lectura; no se transcribe | Fig. 3, p. 6 |

### Contexto citado (cifras de terceros)

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| EMIDEC: Dice | "The EMIDEC challenge [16] reported Dice scores between 0.27–0.71" | Sec. 2, p. 3 |
| EMIDEC: accuracy | "classification accuracies from 62–91%" | Sec. 2, p. 3 |
| CLAIM (Ramzan): Dice | "use pixel-space DMs to synthesize LGE scar, achieving Dice upto 0.635" | Sec. 2, p. 3 |
| DiffLGE (Deng): limite | "relied on paired multi-sequence inputs and lacked explicit control" | Sec. 2, p. 3 |
| Hueco declarado | "no studies explore their use for conditional LGE synthesis" | Sec. 2, p. 3 |

### Discusion y limitaciones declaradas

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Inpainting simplifica | "Framing the task as inpainting reduces generation complexity" | Sec. 6, p. 9 |
| Calidad no implica alineacion | "high image quality does not imply alignment to conditioning" | Sec. 6, p. 9 |
| Limitacion: un centro, GT semiautomatico | "Limitations include the use of single-center data and semi-automated GT masks" | Sec. 6, p. 9 |
| Idem | "based on segment-level labels" | Sec. 6, p. 9 |
| Limitacion: formas elipticas | "we have prompted the DM with simple, elliptical scar shapes" | Sec. 6, p. 9 |
| Trabajo futuro | "expanding the data to multi-center, multi-vendor cohorts" | Sec. 6, p. 9 |
| Trabajo futuro | "exploring more realistic clinical patterns of LGE occurrence" | Sec. 6, p. 9 |
| Limitacion: recompensa | "large-scale, generalizable models are not readily available" | Sec. 3.1, p. 4 |
| Conflicto de interes | "The authors AJJ and PS are employees of Siemens Healthineers." | Disclosure, p. 9 |

### Buscado en el PDF sin resultado

| Dato buscado | Resultado | Seccion / pagina |
|---|---|---|
| Hueso | NO ENCONTRADO EN EL PDF | — |
| Metal | NO ENCONTRADO EN EL PDF | — |
| Implantes, protesis o dispositivos | NO ENCONTRADO EN EL PDF | — |
| Objetos rigidos o rigidez | NO ENCONTRADO EN EL PDF | — |
| Tejido deformable o supuesto de no-rigidez | NO ENCONTRADO EN EL PDF | — |
| Sintesis o simulacion de artefactos | NO ENCONTRADO EN EL PDF | — |
| Dimensionalidad declarada (2D / 2.5D / 3D) del generador | NO ENCONTRADO EN EL PDF (solo "256 × 256" e "images", p. 7) | — |
| Paso de pegado o composicion de pixeles originales fuera de la mascara | NO ENCONTRADO EN EL PDF | — |
| Restriccion explicita de cambios de intensidad al interior de la mascara | NO ENCONTRADO EN EL PDF | — |
| HU, ventanas o multi-ventana | NO ENCONTRADO EN EL PDF | — |
| Especificacion del autoencoder latente (canales, factor de reduccion) | NO ENCONTRADO EN EL PDF | — |
| HD95 u otra metrica de distancia | NO ENCONTRADO EN EL PDF | — |
| Pruebas estadisticas o intervalos de confianza | NO ENCONTRADO EN EL PDF | — |
| Muestras generadas antes del filtro para el downstream (tasa de rechazo) | NO ENCONTRADO EN EL PDF | — |
| Disponibilidad de codigo | NO ENCONTRADO EN EL PDF | — |
| Evaluacion por lectores humanos | NO ENCONTRADO EN EL PDF | — |
