# zhang2025diffboost — DiffBoost: segmentacion medica mejorada con difusion guiada por texto

- **DOI / URL:** 10.1109/TMI.2024.3519307 ("Digital Object Identifier 10.1109/TMI.2024.3519307",
  nota al pie, p. 3670). Codigo: https://github.com/NUBagciLab/DiffBoost (Abstract, p. 3670).
  Version leida: publicada, "IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 44, NO. 9, SEPTEMBER
  2025" (cabecera, p. 3670), pp. 3670-3682 (13 pp., texto completo, copia licenciada IEEE
  Xplore para UTEC). Toda pagina citada abajo es la paginacion impresa de la revista.
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/zhang2025diffboost.pdf

## Que hace (3 lineas maximo)
Ajusta un Stable Diffusion + ControlNet 2D sobre RadImageNet con dos condiciones (texto
modalidad/organo/categoria via CLIP, y mapa de bordes HED), lo afina por tarea con el borde de
la mascara, genera imagenes COMPLETAS desde ruido y las mezcla por parches aleatorios con las
reales para entrenar un segmentador (AttentionUNet) en prostata MRI, bazo CT y mama US.

## Restriccion o supuesto clave
El supuesto que le impide manejar implantes metalicos NO es el que le atribuye
`tesis/main.tex` (l. 48). En la version publicada DiffBoost no es inpainting acotado ni
restringe intensidades al interior de la mascara:
- Genera la imagen entera desde ruido: "Augment x_0 by n times ε ~ N(0; 1)" y
  "x_i = D(ε_i, c_t + c_aug_i, c_e)" (Alg. 1, p. 3676). La mascara solo entra como borde
  condicionante: "incorporate the edge derived from the segmentation mask into the generation
  condition" (§III-C, p. 3674).
- La mezcla con la imagen real es por parches aleatorios de toda la imagen, sin relacion con
  la mascara: "loss = l(C(m · x_0 + (1 − m) · x_i), y)" (Alg. 1, p. 3676); "Every patch with
  values lower than a specific threshold α is converted to 1" (§III-D, p. 3675). La etiqueta y
  no cambia: la geometria queda fijada por el borde.
- Los cambios de intensidad son globales y buscados: "Augmented samples show notable
  variances in intensity distribution (diversity)" (Fig. 3, p. 3676); "albeit there may be
  disparities in intensity" (Fig. 2, p. 3675).
- Supuesto explicito de tejido deformable/no rigido: NO ENCONTRADO EN EL PDF. Hace lo
  contrario de deformar: fija la geometria con bordes, y lo declara limitacion: "edge map
  (ControlNet) as a condition on image generation can limit the anatomical variation" (§VI,
  p. 3680).
- Metal, implantes, objetos rigidos, artefactos de CT: NO ENCONTRADO EN EL PDF. Ventanas HU o
  truncamiento: NO ENCONTRADO EN EL PDF; lo unico sobre rango es "Data Range Is Between 0-1 for
  Computation" (titulo de Tabla I, p. 3677), referido a las metricas de generacion. El hueso
  solo aparece como calidad de borde: "mixed facts about the quality of boundary information
  in soft and bone tissue locations" (§VI, p. 3681).

El limite real para metal es otro: generacion 2D por corte ("we split them into 2D with a
slice depth of one", §IV-B, p. 3677), salida gris por promedio de canales ("cross-channel
average block in the final output stage", §III-A, p. 3674) sin semantica HU, y realismo
validado solo por similitud de pixel (MAE/MSE/RMSE/SSIM/MS-SSIM, §IV-A y Tabla I,
pp. 3676-3677), sin criterio fisico de artefacto ni modelo de efectos no locales.

Identidad: NO es Du et al. 2023 (dermatoscopia). Autores: Zhang, Yao, Wang, Jha, Durak, Keles,
Medetalibeyoglu y Bagci (p. 3670), Northwestern; tareas prostata MRI, bazo CT, mama US
(Tabla II, p. 3678); Du et al. no figura en sus 56 referencias (pp. 3681-3682). "dermatoscopic":
NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna cifra es necesaria para la tesis (downstream fuera de alcance). Si se cita como precedente de ControlNet medico: | | |
| 1.35 millones de imagenes (RadImageNet) | "RadImageNet constitutes a collection of 1.35 million radiologic images" | §III-B, p. 3674 |
| Generacion 2D corte a corte | "we split them into 2D with a slice depth of one" | §IV-B, p. 3677 |
| +7.78% / +0.38% / +13.87% (mejoras RELATIVAS de Dice, no puntos) | "Ultrasound breast (+13.87%), CT spleen (+0.38%), and MRI prostate (+7.78%)" | Abstract, p. 3670 |

Nota de verificacion (calculo propio, no cifra del paper, sobre Tabla II p. 3678):
84.56/78.46 = 1.0778, 94.78/94.42 = 1.0038 y 71.65/62.92 = 1.1388; los porcentajes del
abstract son relativos. En puntos Dice: +6.10 (prostata), +0.36 (bazo), +8.73 (mama).

## Donde entra en mi tesis
- Related Work / Problem Statement (`tesis/main.tex` l. 48): mal clasificado dentro de
  "bounded inpainting for deformable biological tissues". Encaja como sintesis de imagen
  completa condicionada por bordes y texto, que preserva la geometria de la etiqueta y altera
  intensidades globalmente, sin semantica HU ni modelo de efectos no locales.
- Reclamo de novedad del renderizador: precedente publicado (TMI 2025) de ControlNet sobre
  Stable Diffusion ajustado en imagen medica que incluye CT pelvica ("including CT scans of the
  chest, abdomen, and pelvis", §III-B, p. 3674). La novedad no puede apoyarse en "usar
  ControlNet en CT"; debe apoyarse en B_delta, multi-ventana HU y metal.
- Motivacion de la codificacion multi-ventana: contraste util, porque su salida es gris
  promediada desde RGB sin ninguna ventana HU declarada.

## Dudas para el asesor
1. main.tex:48 agrupa DiffBoost con DiffTumor, CLAIM y LGESynthNet. La version publicada
   confirma que DiffBoost no cumple la frase (Alg. 1, p. 3676). Se reescribe por familias
   (inpainting acotado vs. sintesis global condicionada) o se retira DiffBoost?
2. Dos de sus tres tareas son organos (prostata, bazo), no lesiones. Es correcto llamarlo
   "lesion synthesis model"?
3. Los checkpoints son publicos ("We release all checkpoints", §III-B, p. 3674). Tiene
   sentido mencionarlo solo como referencia de inicializacion 2D, sabiendo que no maneja HU?
   (No se propone adoptarlo.)
4. Inconsistencias que siguen en la version publicada y conviene no heredar: (a) α es umbral
   de mezcla por parches (§III-D, p. 3675) y "weighting factor in our pre-designed combination
   loss function" (§V-B, p. 3679); Alg. 1 lo llama ademas "loss balance hyper-parameter α"
   y lo pasa a generate-random-patch (p. 3676); (b) MS-SSIM 0.636 en texto (§IV-A, p. 3676)
   vs 0.6666 en Tabla I (p. 3677); (c) HD95 definida como "average distance" (§IV-B,
   p. 3677); (d) el rango 0.2-0.8 se atribuye a la "data augmentation ratio" cuando la figura
   es de α (§V-B, p. 3680; Fig. 6(b), p. 3680); (e) errata "384/64 × 384.64" (§III-D, p. 3675).
5. Snowballing: [24] Machacek y [41] Polyp-DDPM siguen citados con el mismo numero
   (p. 3681 y p. 3682). Posibles candidatos nuevos que la ronda anterior habia descartado en
   bloque ([20]-[40]) y que podrian caer en la regla "ya intento algo parecido": [35] Med-DDPM
   (sintesis semantica 3D condicionada por mascara, Dice 65.31% a 66.75% segun §II-B,
   p. 3672) y [36] DiffuseExpand (ampliacion de datos 2D para segmentacion con difusion).
   Decide la autora.

## Diferencias frente al preprint arXiv:2310.12868v2
Solo lo comprobado en el PDF nuevo frente a lo que decia la ficha vieja:
- Metadatos: la cabecera "VOL. XX, NO. XX, XXXX 2024" y el sello "arXiv:2310.12868v2 [cs.CV]
  14 Dec 2024" ya no estan (NO ENCONTRADO EN EL PDF, venian del preprint). Ahora se imprimen
  vol. 44, no. 9, septiembre 2025, pp. 3670-3682, DOI, fechas y financiacion (p. 3670). La
  extension sigue siendo 13 pp. y 56 referencias.
- Afiliacion: la frase "All authors belong to Machine & Hybrid Intelligence Lab in
  Northwestern University" ya no esta (NO ENCONTRADO EN EL PDF, venia del preprint); ahora
  dice "Machine and Hybrid Intelligence Laboratory, Northwestern University, Chicago" (p. 3670).
- Redaccion: "R. Rombach [11] conducts" pasa a "Rombach et al. [11] conducts"
  (§III-A, pp. 3672-3673); "a text-based guidance" pasa a "text-based guidance" (§II-B, p. 3672).
- Parche de mezcla: la ficha vieja transcribia "384/64×384/64"; el PDF publicado imprime
  "384/64 × 384.64" (§III-D, p. 3675). No se puede saber aqui si es cambio o error de la ficha.
- Formato de refs.: [24] ahora "R. Macháček et al., ... 2023, arXiv:2304.05233"; [41] ahora
  "... 2024, arXiv:2402.04031". Mismos numeros.
- Sin cambios comprobados en: metodo (Alg. 1), mezcla por parches, datasets y tamanos de
  muestra, Tablas I y II, las cuatro inconsistencias (duda 4 a-d) y las limitaciones de §VI.
  Nada de esto altera el veredicto sobre main.tex:48, el nivel N2 ni el rol "solo contexto".

## Evidencia textual
| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Revista, volumen, numero, fecha | "IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 44, NO. 9, SEPTEMBER 2025" | Cabecera, p. 3670 |
| Pagina final | "IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 44, NO. 9, SEPTEMBER 2025" con folio 3682 | Cabecera, p. 3682 |
| DOI | "Digital Object Identifier 10.1109/TMI.2024.3519307" | Nota al pie, p. 3670 |
| Fechas editoriales | "Received 13 October 2024; revised 24 November 2024; accepted 12 December 2024." | Nota al pie, p. 3670 |
| Publicacion y version | "Date of publication 17 December 2024; date of current version 12 September 2025." | Nota al pie, p. 3670 |
| Copyright / ISSN | "1558-254X © 2024 IEEE. Personal use is permitted" | Pie, p. 3670 |
| Financiacion 1 | "supported in part by NIH NCI under Grant R01-CA246704" | Nota al pie, p. 3670 |
| Financiacion 2 | "in part by NIH/NIDDK under Grant U01 DK127384-02S1" | Nota al pie, p. 3670 |
| Autor de correspondencia | "(Corresponding author: Ulas Bagci.)" | Nota al pie, p. 3670 |
| Acceso | "Authorized licensed use limited to: Universidad de Ingeniería y Tecnología (UTEC)." | Pie, pp. 3670-3682 |
| Descarga | "Downloaded on September 15,2026 at 06:31:04 UTC from IEEE Xplore." | Pie, p. 3670 |
| Autores (1) | "Zheyuan Zhang, Lanhong Yao, Bin Wang, Debesh Jha, ... Gorkem Durak, Elif Keles," | p. 3670 |
| Autores (2) | "Alpay Medetalibeyoglu, and Ulas Bagci" | p. 3670 |
| Afiliacion | "Machine and Hybrid Intelligence Laboratory, Northwestern University, Chicago, IL 60611 USA" | Nota al pie, p. 3670 |
| Codigo y checkpoints | "Source code with checkpoints are available at https://github.com/NUBagciLab/DiffBoost." | Abstract, p. 3670 |
| Bordes como guia | "incorporating edge information of objects to guide the synthesis process" | Abstract, p. 3670 |
| Numero de muestras sintetizables | "we can generate an arbitrary number of synthetic images with diverse appearances" | Abstract, p. 3670 |
| Mejoras titulares | "Ultrasound breast (+13.87%), CT spleen (+0.38%), and MRI prostate (+7.78%)" | Abstract, p. 3670 |
| Reclamo de primicia | "a first-ever text-guided diffusion model for general medical image segmentation tasks" | Abstract, p. 3670 |
| Index terms | "Medical image segmentation, image synthesis, data augmentation, score-based generative models" | p. 3670 |
| Tipo de modelo | "a text-guided diffusion model-based (DDPM) data augmentation approach, called DiffBoost" | §I, p. 3671 |
| Paso 1 | "Pretraining on large medical datasets" | §I, p. 3671 |
| Paso 2 | "Fine-tuning on downstream task" | §I, p. 3671 |
| Paso 3 | "Integration with Downstream Task Training" | §I, p. 3671 |
| Perdida combinada | "a carefully designed combination loss ensures both real and synthetic samples contribute equally" | §I, p. 3671 |
| Cifra ajena citada (Med-DDPM, ref. [35]) | "improving segmentation accuracy from 65.31% to 66.75% in terms of Dice score" | §II-B, p. 3672 |
| Polyp-DDPM (ref. [41]) | "authors in [41] introduce Diffusion-Based semantic polyp synthesis" | §II-B, p. 3672 |
| Gap declarado | "leveraging text-based guidance with a pixel-level aligned diffusion model remains under investigated" | §II-B, p. 3672 |
| Rango de β_t | "β_t ∈ (0, 1) represents the variance schedule across diffusion steps" | §III-A, p. 3672 |
| Muestreo directo de x_t | "x_t = √ᾱ_t x_0 + √(1 − ᾱ_t) ε" (Ec. 3) | §III-A, p. 3672 |
| Objetivo simplificado | "L_simple = E_{t,x_0,ε}[‖ε − ε_θ(x_t, t)‖²]" (Ec. 11) | §III-A, p. 3672 |
| Espacio latente | "Rombach et al. [11] conducts the diffusion training in latent feature space" | §III-A, pp. 3672-3673 |
| Tipos de condicionamiento | "two types of conditioning input: text c_t and edge information c_e" | §III-A, p. 3673 |
| Diseno en ramas | "a branch design comprising the original branch for stable diffusion with text conditioning" | §III-A, p. 3673 |
| Codificacion del texto | "conditioning inputs such as the text prompts with CLIP encoding [15]" | §III-A, p. 3673 |
| Bloque de texto congelado | "Frozen Block" (icono sobre "Text condition block") | Fig. 1, p. 3673 |
| Prompts de ejemplo (aumentacion) | "US,breast,enhance contrast" / "MRI,prostate,darkened image" / "CT,spleen,median filter" | Fig. 1, p. 3673 |
| Salida en grises | "we incorporate a cross-channel average block in the final output stage" | §III-A, p. 3674 |
| Inicializacion desde SD | "using pre-trained checkpoints from stable diffusion algorithm rather than training from scratch" | §III-B, p. 3674 |
| Regiones RadImageNet (incluye CT pelvis) | "RadImageNet encompasses 11 anatomical regions, including CT scans of the chest, abdomen, and pelvis" | §III-B, p. 3674 |
| Tamano RadImageNet | "RadImageNet constitutes a collection of 1.35 million radiologic images" | §III-B, p. 3674 |
| Estructura del prompt | "a triplet: a combination of data modality, organ name, and category name" | §III-B, p. 3674 |
| Detector de bordes | "we employ the Holistically-Nested Edge Detection (HED) algorithm proposed by [43]" | §III-B, p. 3674 |
| Bordes en tejido blando | "precise edges not only for the skull but also for soft-tissue organs" | §III-B, p. 3674 |
| Hardware preentrenamiento | "utilizing 6 NVIDIA RTX A6000 GPUs, each equipped with 48GB memory" | §III-B, p. 3674 |
| Batch preentrenamiento | "a batch size of 384 in total (48 for each under the DDP setting)" | §III-B, p. 3674 |
| Duracion y lr preentrenamiento | "approximately seven days to complete, with a learning rate set at 10^-5" | §III-B, p. 3674 |
| Checkpoints liberados | "We release all checkpoints and provide sample results" | §III-B, p. 3674 |
| Diferencias de intensidad aceptadas | "share similar anatomical information regardless of potential intensity differences" | §III-B, p. 3674 |
| Condicion en ajuste fino | "incorporate the edge derived from the segmentation mask into the generation condition" | §III-C, p. 3674 |
| Hardware ajuste fino | "a single NVIDIA RTX A6000 GPU for each subtask training" | §III-C, p. 3674 |
| Batch y optimizador ajuste fino | "maintaining a batch size of 48 while employing the AdamW optimizer" | §III-C, p. 3674 |
| lr y epocas ajuste fino | "learning rate is set at 10^-6, and the fine-tuning process is performed over 100 epochs" | §III-C, p. 3674 |
| Control de fuga de datos | "we exclusively use image-text pairs from the training set" | §III-C, p. 3674 |
| Texto de aumentacion | "adding augmentation text c_aug, like "enhanced contrast", and "high resolution,"" | §III-D, p. 3675 |
| Compatibilidad con perdidas | "our method is compatible with various segmentation loss designs" | §III-D, p. 3675 |
| Resolucion y parche | "given a dimension of 384 × 384, as is customary in our studies, and a patch size of 64" | §III-D, p. 3675 |
| Matriz aleatoria (con errata impresa) | "a random matrix with a dimension of 384/64 × 384.64 from a uniform distribution" | §III-D, p. 3675 |
| Criterio de umbral α | "Every patch with values lower than a specific threshold α is converted to 1" | §III-D, p. 3675 |
| Reescalado de la mascara de mezcla | "resized back to its original dimensions using a nearest-neighbor interpolation technique" | §III-D, p. 3675 |
| α como razon de mezcla | "the hyperparameter α governs the mixing ratio" | §III-D, p. 3675 |
| α = 0 | "α = 0 (meaning that patches are from generated samples only)" | §III-D, p. 3675 |
| α = 1 | "α = 1 (meaning that patches are from original images only)" | §III-D, p. 3675 |
| Categorias RadImageNet mostradas | "MR, hip, normal" / "CT, abdomen, normal" / "MR, ankle, osseous disruption" | Fig. 2, p. 3675 |
| Realismo anatomico declarado | "Both the original and synthesized images maintain congruent anatomical structures" | Fig. 2, p. 3675 |
| Discrepancia de intensidad admitida | "albeit there may be disparities in intensity" | Fig. 2, p. 3675 |
| Variacion global de intensidad | "Augmented samples show notable variances in intensity distribution (diversity)" | Fig. 3, p. 3676 |
| Entradas de Alg. 1 | "(x_0, c_t, c_e, y) represents the image, text, edge, and label pairs" | Alg. 1, p. 3676 |
| α en Alg. 1 (tercer rol) | "segmentation loss function l with loss balance hyper-parameter α" | Alg. 1, p. 3676 |
| Generacion desde ruido (imagen completa) | "Augment x_0 by n times ε ~ N(0; 1)" | Alg. 1, p. 3676 |
| Muestra sintetica | "x_i = D(ε_i, c_t + c_aug_i, c_e), i ~ 1, ..., n" | Alg. 1, p. 3676 |
| Mascara de mezcla | "m = generate-random-patch(α, patch size)" | Alg. 1, p. 3676 |
| Mezcla y etiqueta intacta | "loss = l(C(m · x_0 + (1 − m) · x_i), y)" | Alg. 1, p. 3676 |
| Metricas de generacion | "Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Square Error (RMSE)" | §IV-A, p. 3676 |
| Rechazo de FID/IS | "render these metrics less effective in accurately assessing the performance of our approach" | §IV-A, p. 3676 |
| Comparador de generacion | "Pix2Pix takes the same edge information as guidance" | §IV-A, p. 3676 |
| Cifras en texto DiffBoost (1) | "The diffusion model achieved an MAE score of 0.087, an MSE of 0.023" | §IV-A, p. 3676 |
| Cifras en texto DiffBoost (2), MS-SSIM discrepa de Tabla I | "an RMSE of 0.144, an SSIM of 0.636, and an MS-SSIM of 0.636" | §IV-A, p. 3676 |
| Cifras en texto Pix2Pix (1) | "Pix2Pix GAN method achieved an MAE score of 0.147, an MSE of 0.0538" | §IV-A, p. 3676 |
| Cifras en texto Pix2Pix (2) | "an RMSE of 0.2219, an SSIM of 0.4583, and an MS-SSIM of 0.5325" | §IV-A, p. 3676 |
| Criterio de equilibrio | "strike a balance between the two (segmentation and data diversity)" | §IV-A, p. 3676 |
| Interpretacion MS-SSIM | "higher MS-SSIM scores indicate better structural consistency with the ground truth" | §IV-A, p. 3677 |
| Rango para metricas de generacion | "Data Range Is Between 0-1 for Computation" | Tabla I (titulo), p. 3677 |
| Tabla I Pix2Pix (MAE/MSE/RMSE/SSIM/MS-SSIM) | 0.1469±0.0556 / 0.0538±0.0366 / 0.2219±0.0676 / 0.4583±0.1105 / 0.5325±0.1557 | Tabla I, p. 3677 |
| Tabla I DiffBoost (MAE/MSE/RMSE/SSIM/MS-SSIM) | 0.0873±0.0363 / 0.0229±0.0163 / 0.1441±0.0463 / 0.6356±0.1252 / 0.6666±0.1491 | Tabla I, p. 3677 |
| Valores de α mostrados | "Alpha: 0.0" ... "Alpha: 1.0" (0.0, 0.2, 0.4, 0.6, 0.8, 1.0) | Fig. 4, p. 3677 |
| Modalidades y organos | "ultrasound, CT, and MRI modalities across various organs like breast [45], spleen [46]" | §IV-B, p. 3677 |
| 3D tratado como 2D | "we split them into 2D with a slice depth of one" | §IV-B, p. 3677 |
| Segmentador | "the standard AttentionUNet [47] as the segmentation backbone with MONAI implementation" | §IV-B, p. 3677 |
| Aumentaciones espaciales | "Random Rotate, Random Scale, and Random Mirror, Random Resolution" | §IV-B, p. 3677 |
| Aumentaciones de intensidad | "Random Contrast, Random Gamma, Random Brightness, Random Noise" | §IV-B, p. 3677 |
| Definicion DeepStack | "the combination of all previous transforms implemented in nnUNet [4]" | §IV-B, p. 3677 |
| Validacion | "all experiments were conducted under 3-fold cross-validation" | §IV-B, p. 3677 |
| Metricas de region | "region-level metrics such as Dice coefficient (Dice), Precision, and Recall" | §IV-B, p. 3677 |
| Metricas de forma | "95% Hausdorff Distance (HD95) and Average Symmetric Surface Distance (ASSD)" | §IV-B, p. 3677 |
| Interpretacion de la mejora | "learning more robust and intensity-independent features, particularly the morphology" | §IV-B, p. 3677 |
| Reduccion de dispersion | "DiffBoost also leads to a reduction in standard deviation across datasets" | §IV-B, p. 3677 |
| Definicion (imprecisa) de HD95 | "This metric measures the average distance between the predicted segmentation boundary and the ground truth" | §IV-B, p. 3677 |
| Prostata en texto | "The Dice coefficient increases from 78.46% to 84.56% (7.8% improvement)" | §IV-B, pp. 3677-3678 |
| Mama en texto | "from 62.92% to 71.65% (13.87% improvement) for breast cancer segmentation" | §IV-B, p. 3678 |
| Bazo en texto | "(Dice coefficient of 94.42%), the improvement from DiffBoost was marginal (94.78%)" | §IV-B, p. 3678 |
| DeepStack no garantiza mejora | "combining multiple data augmentation techniques (like DeepStack) doesn't always guarantee better performance" | §IV-B, p. 3678 |
| n prostata | "Task 1: Prostate MRI Segmentation (Sample Size: 32 )" | Tabla II, p. 3678 |
| n bazo | "Task 2: Spleen CT Segmentation (Sample Size: 41)" | Tabla II, p. 3678 |
| n mama | "Task 3: Breast Cancer Ultrasound Segmentation (Sample Size: 147)" | Tabla II, p. 3678 |
| Orden de columnas T1/T2 | Dice / Precision / Recall / HD95 (mm) / ASSD (mm) | Tabla II, p. 3678 |
| T1 Baseline | 78.46±10.36 / 77.72±11.89 / 81.35±13.11 / 11.93±8.04 / 3.12±1.32 | Tabla II, p. 3678 |
| T1 RandomContrast | 81.23±8.79 / 82.13±10.25 / 82.10±12.07 / 10.41±6.31 / 2.59±1.00 | Tabla II, p. 3678 |
| T1 RandomGamma | 79.30±9.05 / 79.37±11.15 / 82.17±11.98 / 11.65±7.07 / 2.84±1.44 | Tabla II, p. 3678 |
| T1 RandomBrightness | 79.18±8.07 / 80.97±10.02 / 79.81±12.54 / 11.10±9.07 / 2.91±1.18 | Tabla II, p. 3678 |
| T1 RandomNoise | 80.68±7.29 / 80.34±10.38 / 82.55±10.33 / 12.04±9.43 / 2.68±1.06 | Tabla II, p. 3678 |
| T1 RandomResolution | 78.63±8.54 / 80.82±10.85 / 78.79±12.56 / 12.22±11.25 / 2.85±1.33 | Tabla II, p. 3678 |
| T1 RandomMirror | 79.23±11.32 / 85.08±9.93 / 76.19±15.94 / 9.31±5.46 / 2.55±1.18 | Tabla II, p. 3678 |
| T1 RandomRotate | 82.12±9.03 / 85.62±8.33 / 80.53±12.67 / 8.47±7.47 / 2.30±1.39 | Tabla II, p. 3678 |
| T1 RandomScale | 83.11±7.29 / 84.59±9.26 / 83.18±10.53 / 9.64±7.84 / 2.37±1.06 | Tabla II, p. 3678 |
| T1 DeepStack | 78.97±9.40 / 81.86±10.21 / 78.99±14.33 / 9.32±4.61 / 2.7±1.17 | Tabla II, p. 3678 |
| T1 DiffBoost | 84.56±6.69 / 86.70±6.50 / 83.98±10.53 / 7.75±8.88 / 2.06±1.40 | Tabla II, p. 3678 |
| T2 Baseline | 94.42±2.76 / 95.12±2.84 / 93.92±4.67 / 5.18±4.43 / 0.94±0.68 | Tabla II, p. 3678 |
| T2 RandomContrast | 94.29±2.55 / 95.15±3.43 / 93.66±4.29 / 8.18±12.58 / 1.35±1.38 | Tabla II, p. 3678 |
| T2 RandomGamma | 94.69±1.98 / 95.37±2.80 / 94.15±3.31 / 5.59±5.42 / 1.14±1.43 | Tabla II, p. 3678 |
| T2 RandomBrightness | 93.84±2.82 / 94.17±3.83 / 93.77±4.68 / 6.57±6.04 / 1.23±1.04 | Tabla II, p. 3678 |
| T2 RandomNoise | 93.84±3.28 / 94.59±3.71 / 93.44±5.53 / 6.32±5.15 / 1.29±0.94 | Tabla II, p. 3678 |
| T2 RandomResolution | 93.99±3.01 / 94.66±4.22 / 93.68±5.04 / 7.84±7.74 / 1.29±1.12 | Tabla II, p. 3678 |
| T2 RandomMirror | 91.95±4.89 / 92.92±5.05 / 91.52±7.46 / 22.89±38.69 / 3.23±3.30 | Tabla II, p. 3678 |
| T2 RandomRotate (mejor precision) | 93.76±4.46 / 95.49±3.17 / 92.6±7.65 / 6.15±6.27 / 1.17±1.01 | Tabla II, p. 3678 |
| T2 RandomScale | 93.98±2.65 / 94.82±4.11 / 93.44±4.21 / 5.96±5.39 / 1.09±0.81 | Tabla II, p. 3678 |
| T2 DeepStack | 93.66±3.36 / 93.73±4.60 / 93.99±5.55 / 8.3±8.28 / 1.39±1.15 | Tabla II, p. 3678 |
| T2 DiffBoost (precision bajo baseline) | 94.78±1.95 / 94.14±3.13 / 95.55±2.68 / 4.88±3.83 / 0.9±0.55 | Tabla II, p. 3678 |
| Unidades de distancia en T3 | "HD95 (pixel)" / "ASSD (pixel)" | Tabla II, p. 3678 |
| T3 Baseline | 62.92±25.79 / 63.34±31.15 / 76.59±24.50 / 138.19±118.30 / 38.20±38.20 | Tabla II, p. 3678 |
| T3 RandomContrast | 64.81±27.36 / 65.83±30.89 / 73.93±27.96 / 123.24±105.32 / 34.96±33.83 | Tabla II, p. 3678 |
| T3 RandomGamma | 66.43±25.11 / 67.66±29.26 / 75.40±25.51 / 117.96±113.57 / 33.63±34.13 | Tabla II, p. 3678 |
| T3 RandomBrightness | 63.65±27.58 / 65.56±31.79 / 73.42±26.95 / 125.58±111.85 / 37.63±39.78 | Tabla II, p. 3678 |
| T3 RandomNoise | 66.24±25.52 / 67.29±30.73 / 75.79±22.92 / 132.05±120.47 / 35.65±34.14 | Tabla II, p. 3678 |
| T3 RandomResolution | 67.89±25.64 / 68.15±29.01 / 77.03±23.88 / 127.33±124.93 / 34.42±37.11 | Tabla II, p. 3678 |
| T3 RandomMirror (mejor precision) | 70.15±25.55 / 70.85±28.77 / 78.45±25.14 / 102.08±105.71 / 29.83±36.53 | Tabla II, p. 3678 |
| T3 RandomRotate | 69.15±27.57 / 69.99±30.95 / 77.87±25.20 / 118.18±129.85 / 34.33±44.07 | Tabla II, p. 3678 |
| T3 RandomScale | 69.15±26.05 / 68.96±29.15 / 79.24±25.84 / 113.74±117.50 / 32.01±36.97 | Tabla II, p. 3678 |
| T3 DeepStack | 63.85±25.63 / 63.64±30.05 / 76.33±23.94 / 144.79±120.06 / 37.94±38.56 | Tabla II, p. 3678 |
| T3 DiffBoost | 71.65±24.52 / 70.22±27.89 / 81.91±22.39 / 95.18±103.41 / 26.98±32.55 | Tabla II, p. 3678 |
| Dataset de las ablaciones | "with various network architectures on the prostate MRI segmentation dataset" | §V, p. 3678 |
| Definicion de razon de aumentacion | "The data augmentation ratio, defined as n in Algorithm 1" | §V-A, p. 3679 |
| Meseta de la razon | "when this ratio exceeds a factor of 10, the marginal performance enhancements begin to plateau" | §V-A, p. 3679 |
| α como peso de perdida (inconsistente con §III-D) | "α acts as a weighting factor in our pre-designed combination loss function" | §V-B, p. 3679 |
| Rango de meseta (atribuido a la razon, no a α) | "high-performance plateau when the data augmentation ratio resides within the wide range of 0.2-0.8" | §V-B, p. 3680 |
| Valores ensayados de n | Eje: 0, 3, 5, 10, 20, 30, 40, 50 | Fig. 6(a), p. 3680 |
| Valores ensayados de α | Eje: 0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1 | Fig. 6(b), p. 3680 |
| Valores ensayados de parche | Eje: 1, 32, 64, 96, 128, 384 | Fig. 6(c), p. 3680 |
| Meseta segun leyenda | "The marginal performance gain is limited once the ratio is larger than 10." | Fig. 6, p. 3680 |
| Parche = imagen | "selection between real and synthetic samples occurs on a case-by-case basis" | §V-C, p. 3680 |
| Parche = 1 | "when the patch size is set to 1, selection occurs at the pixel level" | §V-C, p. 3680 |
| Parche optimo | "optimal performance was noted when the patch size was set to a median spatial level" | §V-C, p. 3680 |
| Backbones CNN | "basic UNet [52], Residual UNet [53], ResNet50 UNet [54]" | §V-D, p. 3680 |
| Backbone transformer | "the recent transformer structure like SwinUNETR [55]" | §V-D, p. 3680 |
| Limitacion 1: texto categorico | "our current text input is a combination of several categorical labels" | §VI, p. 3680 |
| Limitacion 1b: sin texto natural | "We have not tested how the model will perform under natural texts" | §VI, p. 3680 |
| Limitacion 2: bordes restringen variacion | "edge map (ControlNet) as a condition on image generation can limit the anatomical variation" | §VI, p. 3680 |
| Limitacion 2b: bordes verdaderos | "This potential limitation can be substantial if true edges are used instead of edgemaps" | §VI, p. 3681 |
| Limitacion 2 no observada | "This is not the case in our experiments, luckily" | §VI, p. 3681 |
| Postura sobre fidelidad | "High-fidelity synthetic scans are not always necessary for successful medical image segmentation" | §VI, p. 3681 |
| Hueso y tejido blando | "mixed facts about the quality of boundary information in soft and bone tissue locations" | §VI, p. 3681 |
| Hueso como borde limpio | "the skull in MRI can lead to clean edge guidance" | §VI, p. 3681 |
| Limitacion 3: tejido blando | "there were cases where the soft tissue boundaries were not clear" | §VI, p. 3681 |
| Sin consenso sobre tejido blando | "we did not have a clear consensus whether soft tissue generation is always inferior" | §VI, p. 3681 |
| Limitacion 4: sin otros GAN | "we did not benchmark other GAN-based methods like StyleGAN [56]" | §VI, p. 3681 |
| Trabajo futuro | "exploring techniques to accelerate the sampling process within the diffusion model" | §VI, p. 3681 |
| Ref. [24] | "R. Macháček et al., "Mask-conditioned latent diffusion for generating gastrointestinal polyp images,"" | Refs., p. 3681 |
| Ref. [35] | "Z. Dorjsembe, H.-K. Pao, S. Odonchimed, and F. Xiao, "Conditional diffusion models..."" | Refs., p. 3682 |
| Ref. [36] | "S. Shao, X. Yuan, ... "DiffuseExpand: Expanding dataset for 2D medical image segmentation"" | Refs., p. 3682 |
| Ref. [41] | "Z. Dorjsembe, H.-K. Pao, and F. Xiao, "Polyp-DDPM: Diffusion-based semantic polyp synthesis"" | Refs., p. 3682 |
| Numero de referencias | Ultima entrada "[56] T. Karras, S. Laine, and T. Aila" | Refs., p. 3682 |
| Sello arXiv:2310.12868v2 (preprint) | NO ENCONTRADO EN EL PDF (venia del preprint) | — |
| Cabecera "VOL. XX, NO. XX, XXXX 2024" (preprint) | NO ENCONTRADO EN EL PDF (venia del preprint) | — |
| Frase "All authors belong to Machine & Hybrid Intelligence Lab" (preprint) | NO ENCONTRADO EN EL PDF (venia del preprint) | — |
| Frase "R. Rombach [11] conducts" (preprint) | NO ENCONTRADO EN EL PDF (venia del preprint; ahora "Rombach et al. [11]") | — |
| Ventanas HU, truncamiento o normalizacion de CT | NO ENCONTRADO EN EL PDF | — |
| Metal, implantes, objetos rigidos o artefactos de CT | NO ENCONTRADO EN EL PDF | — |
| Segmentacion de hueso como tarea | NO ENCONTRADO EN EL PDF | — |
| Inpainting o generacion restringida a la mascara | NO ENCONTRADO EN EL PDF | — |
| Supuesto explicito de tejido deformable / no rigido | NO ENCONTRADO EN EL PDF | — |
| Variante 2.5D o 3D del generador | NO ENCONTRADO EN EL PDF | — |
| Muestreador y numero de pasos de inferencia | NO ENCONTRADO EN EL PDF | — |
| Particion train/test por fold (n por particion) | NO ENCONTRADO EN EL PDF | — |
| Pruebas de significancia estadistica (p-valores) | NO ENCONTRADO EN EL PDF | — |
| Valores numericos de Fig. 6 y Fig. 7 | NO ENCONTRADO EN EL PDF (solo graficos) | — |
| Du et al. 2023 / "dermatoscopic" | NO ENCONTRADO EN EL PDF | — |
