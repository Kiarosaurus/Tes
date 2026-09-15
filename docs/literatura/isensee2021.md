# isensee2021 — nnU-Net: metodo autoconfigurable de segmentacion biomedica

- **DOI / URL:** 10.1038/s41592-020-01008-z. Impreso como "https://doi.org/10.1038/s41592-020-01008-z" en la cabecera de la p. 1. Revista: Nature Methods, seccion ARTICLES. Volumen, numero y paginas 18(2):203-211: NO ENCONTRADO EN EL PDF (vienen solo de `refs/raw/isensee2021.nbib`). En el PDF: "Received: 1 April 2020; Accepted: 29 October 2020; Published online: 07 December 2020" (p. 9). Identidad contrastada con el raw: coinciden titulo, cinco autores y DOI.
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/isensee2021.pdf

## Que hace (3 lineas maximo)
Presenta nnU-Net, un metodo que configura solo todo el pipeline de segmentacion: preprocesado, arquitectura, entrenamiento y postprocesado. Lo hace con tres grupos de parametros: fijos, basados en reglas (derivadas del "dataset fingerprint") y empiricos (elegidos por validacion cruzada).
Se evalua sin intervencion manual en 11 retos, 23 datasets y 53 tareas, y alcanza el estado del arte en 33 de las 53.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Para la tesis importan tres supuestos implicitos:
1. **Ninguna tarea es osea, pelvica, vertebral ni con metal.** Los datasets CT (etiqueta "CT" en la Fig. 3) son D3, D6, D7, D8, D9, D10, D11, D14, D17 y D18: higado, pulmon, pancreas, vasos hepaticos, bazo, colon, 13 organos abdominales, rinon y organos toracicos (Fig. 5, p. 7). El PDF no menciona hueso, implantes ni artefactos.
2. **CT con intensidades cuantitativas.** La normalizacion CT se justifica porque *"intensity values are quantitative and reflect physical properties of the tissue"* (Methods, p. 10). Recorta a los percentiles 0.5 y 99.5 del foreground. El PDF no discute que pasa con valores extremos como el metal.
3. **Limpieza por componente mayor, no por tamano.** El postprocesado quita *"all but the largest connected component"* (Methods, p. 11) y solo se aplica si mejora el Dice de validacion cruzada. No hay umbral de tamano ni de fraccion.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna. En `tesis/main.tex` (l. 76) la cita solo identifica el metodo: "TotalSegmentator 2.18.0 ... which is built on nnU-Net \citep{isensee2021}" | --- | --- |

## Donde entra en mi tesis
Objetivo 2 (muestreador): es la referencia del metodo sobre el que se construye TotalSegmentator (`wasserthal2023`), que genera las mascaras de sacro, S1 y caderas. Esa afirmacion la respalda `wasserthal2023`, no este PDF. No se reimplementa ni se citan cifras. **No sirve de precedente para la limpieza por fraccion F (0.1% del volumen de la estructura):** nnU-Net solo evalua quedarse con el componente mayor, lo decide por Dice en validacion cruzada y no define umbrales de tamano.

## Dudas para el asesor
1. **Postprocesado de nnU-Net frente a la limpieza de la tesis.** nnU-Net quita todo menos el componente mayor, primero con todo el foreground junto y luego por clase, solo si mejora el Dice medio y no baja el de ninguna clase (Methods, p. 11). La tesis conserva las componentes por encima de una fraccion F. Son reglas distintas. El PDF no dice que postprocesado usa TotalSegmentator, ni que conectividad usa nnU-Net.
2. **Material que no esta en el PDF.** El articulo remite a Supplementary Notes 1-8 y a Supplementary Software (p. 11). El PDF local no los incluye y tampoco trae Extended Data. Los detalles del aumento de datos (Supplementary Note 4), la descripcion de los datasets (Note 1) y los pipelines por dataset (Note 6) no se pueden verificar aqui.
3. **Inconsistencia interna sobre configuraciones (solo importa si algun dia se citan).** Por defecto se generan tres (2D, 3D full resolution, cascada 3D; p. 4 y Fig. 2, p. 3). Entre las seleccionables, Methods enumera cuatro, con la 3D low resolution aparte (p. 11).
4. **Dato de contexto, sin cifra.** Los agradecimientos nombran a J. Wasserthal entre quienes contribuyeron a la participacion en el Decathlon (p. 11). No afecta a ninguna afirmacion de la tesis.

## Evidencia textual

Paginacion: se usan paginas del PDF (1-14). Las pp. 1-12 son el articulo (cuerpo, Methods, referencias y declaraciones) y las pp. 13-14 el Nature Research Reporting Summary. En las paginas no se ve paginacion impresa de la revista: NO ENCONTRADO EN EL PDF. Nature Methods no numera las secciones, asi que se usa el encabezado o subencabezado.

### Respuestas a las preguntas del encargo

| # | Dato | Frase original (<15 palabras) o estado | Seccion / pagina |
|---|---|---|---|
| 1a | Que es nnU-Net (Abstract) | "nnU-Net, a deep learning-based segmentation method that automatically configures itself" | Abstract, p. 1 |
| 1b | Que configura | "including preprocessing, network architecture, training and post-processing for any new task" | Abstract, p. 1 |
| 1c | Modelo de las decisiones | "modeled as a set of fixed parameters, interdependent rules and empirical decisions" | Abstract, p. 1 |
| 1d | Definicion en Results | "nnU-Net is a deep learning-based segmentation method that automatically configures itself" | Results, p. 2 |
| 1e | Tres grupos de parametros | "three parameter groups: fixed, rule-based and empirical parameters" | Results, nnU-Net development, p. 2 |
| 1f | Dataset fingerprint | "a standardized dataset representation comprising key properties such as image size" | Results, nnU-Net development, p. 2 |
| 1g | Reglas heuristicas | "modeled in the form of interdependent heuristic rules" | Results, nnU-Net development, p. 2 |
| 1h | Parametros empiricos | "Learn only the remaining decisions empirically from the data ('empirical parameters')." | Introduccion, p. 1 |
| 1i | Holistico | "its automated configuration covers the entire segmentation pipeline" | Introduccion, p. 1 |
| 1j | Origen del nombre | "(hence the name nnU-Net, 'no new net')" | Discussion, p. 6 |
| 1k | "self-configuring" en el titulo | "nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation" | Titulo, p. 1 (tambien en los metadatos del archivo) |
| 1l | "self-configuring" en el cuerpo (Abstract, Results, Discussion, Methods) | NO ENCONTRADO EN EL PDF. El cuerpo usa "automatically configures itself" (1a, 1d) | --- |
| 2a | Configuraciones por defecto: 3 | "By default, nnU-Net generates three different U-Net configurations" | Results, nnU-Net application, p. 4 |
| 2b | Cuales | "a two-dimensional (2D) U-Net, a 3D U-Net that operates at full image resolution" | Results, nnU-Net application, p. 4 |
| 2c | Cascada | "a 3D U-Net cascade in which the first U-Net operates on downsampled images" | Results, nnU-Net application, p. 4 |
| 2d | Figura 2: hasta tres | "Up to three configurations are trained in a five-fold cross-validation." | Fig. 2 (leyenda), p. 3 |
| 2e | Figura 2: seleccion entre tres | "From 2D U-Net, 3D U-Net or 3D cascade, choose the best model" | Fig. 2 (tabla, Ensemble selection), p. 3 |
| 2f | Methods: cuatro seleccionables (inconsistencia con 2a-2e) | "2D, 3D full-resolution, 3D low-resolution or the full-resolution U-Net of the cascade" | Methods, Empirical parameters, p. 11 |
| 2g | Como elige | "based on the average foreground Dice coefficient computed via cross-validation on the training data" | Methods, Empirical parameters, p. 11 |
| 2h | Ensembles de dos | "or an ensemble of any two of these configurations" | Methods, Empirical parameters, p. 11 |
| 2i | Como se ensambla | "Models are ensembled by averaging softmax probabilities." | Methods, Empirical parameters, p. 11 |
| 2j | Seleccion tras CV | "nnU-Net empirically chooses the best performing configuration or ensemble" | Results, nnU-Net application, p. 4 |
| 2k | Disparo de la cascada | "covers less than 12.5% of the median image shape" | Methods, Configuration of the 3D U-Net cascade, p. 11 |
| 3a | Cuantos datasets (Abstract) | "including highly specialized solutions on 23 public datasets" | Abstract, p. 1 |
| 3b | Retos, datasets y tareas | "11 international biomedical image segmentation challenges comprising 23 different datasets and 53 segmentation tasks" | Results, p. 4 |
| 3c | Desarrollo y validacion | "exclusively developed on a set of ten development datasets" (Medical Segmentation Decathlon) | Results, p. 4 |
| 3d | Datasets adicionales | "demonstrated in 13 additional datasets" | Introduccion, p. 2 |
| 3e | Modalidades | "magnetic resonance imaging (MRI), computed tomography (CT), electron microscopy (EM) and fluorescence microscopy (FM)" | Results, p. 4 |
| 3f | Lista de datasets D1-D23 | D1-D10 MSD (brain tumor, heart, liver, hippocampus, prostate, lung, pancreas, hepatic vessel, spleen, colon); D11 BCV-Abdomen; D12 PROMISE12; D13 ACDC; D14 LiTS; D15 MSLes; D16 CHAOS; D17 KiTS; D18 SegTHOR; D19 CREMI; D20-D23 Cell Tracking Challenge | Fig. 5 (tabla), p. 7 |
| 3g | Datasets CT (etiqueta de la Fig. 3) | D3 liver, D6 lung, D7 pancreas, D8 hepatic vessel, D9 spleen, D10 colon, D11 BCV (13 organos abdominales), D14 LiTS, D17 KiTS, D18 SegTHOR (heart, aorta, esophagus, trachea) | Fig. 3 y Fig. 5, pp. 5 y 7 |
| 3h | CHAOS en MRI, no en CT | "left and right kidneys (blue and green, respectively) in T1 in-phase MRI (D16)" | Fig. 1 (leyenda), p. 2 |
| 3i | Tarea de CT oseo, pelvis o vertebras | NO ENCONTRADO EN EL PDF | --- |
| 3j | Datos con implantes metalicos | NO ENCONTRADO EN EL PDF | --- |
| 3k | Artefactos (metalicos o de otro tipo) | NO ENCONTRADO EN EL PDF | --- |
| 3l | Resultados en hueso, pelvis, vertebras o metal | NO ENCONTRADO EN EL PDF | --- |
| 3m | Resultado global | "nnU-Net sets a new state of the art in 33 of 53 target structures" | Results, p. 4 |
| 3n | Descripcion detallada de los datasets | "(see Supplementary Note 1 for detailed dataset descriptions)". No esta en el PDF | Fig. 5 (leyenda), p. 7 |
| 4a | Postprocesado por defecto | "empirically opts for 'non-largest component suppression' as a post-processing step" | Results, nnU-Net application, p. 4 |
| 4b | Condicion general | "if performance gains are measured" | Results, nnU-Net application, p. 4 |
| 4c | Uso extendido (refs. 18 y 25) | "Connected component-based post-processing is commonly used in medical image segmentation" | Methods, Post-processing, p. 11 |
| 4d | Justificacion | "by removing all but the largest connected component" | Methods, Post-processing, p. 11 |
| 4e | Como se decide | "automatically benchmarks the effect of suppressing smaller components on the cross-validation results" | Methods, Post-processing, p. 11 |
| 4f | Paso 1: foreground junto | "First, all foreground classes are treated as one component." | Methods, Post-processing, p. 11 |
| 4g | Criterio de aceptacion (i) | "improves the average foreground Dice coefficient" | Methods, Post-processing, p. 11 |
| 4h | Criterio de aceptacion (ii) | "and does not reduce the Dice coefficient for any of the classes" | Methods, Post-processing, p. 11 |
| 4i | Paso 2: por clase | "decides whether the same procedure should be performed for individual classes" | Methods, Post-processing, p. 11 |
| 4j | Figura 2: regla | "does all-but-largest-component-suppression increase cross-validation performance?" | Fig. 2 (tabla, Configuration of post-processing), p. 3 |
| 4k | Figura 2: ramas | "Yes, apply; reiterate for individual classes" / "No, do not apply" | Fig. 2 (tabla), p. 3 |
| 4l | Umbral de tamano o fraccion en el postprocesado | NO ENCONTRADO EN EL PDF | --- |
| 4m | Conectividad usada (6/18/26 vecinos) | NO ENCONTRADO EN EL PDF | --- |
| 4n | Supuesto "una sola instancia de la estructura" (estaba en el preprint) | NO ENCONTRADO EN EL PDF. Solo aparece "nnU-Net follows this assumption", referido a quitar falsos positivos en organos | Methods, Post-processing, p. 11 |
| 5a | Adaptacion suboptima posible | "there might be segmentation tasks for which nnU-Net's automatic adaptation is suboptimal" | Discussion, p. 7 |
| 5b | Sesgo hacia Dice | "nnU-Net was developed with a focus on the Dice coefficient as performance metric" | Discussion, p. 7 |
| 5c | Propiedades no contempladas | "dataset properties that are yet unconsidered could exist" | Discussion, p. 8 |
| 5d | Caso CREMI | "manual adaptation of the loss function, as well as EM-specific preprocessing" | Discussion, p. 8 |
| 5e | Casos muy especificos | "nnU-Net should be seen as a good starting point for necessary modifications" | Discussion, p. 9 |
| 5f | Casos recurrentes | "nnU-Net's heuristics could be extended accordingly" | Discussion, p. 8 |
| 5g | Limitacion de la practica de evaluacion (no de nnU-Net) | "evaluation is rarely performed on more than two datasets" | Discussion, p. 7 |
| 5h | Limitacion declarada sobre metal, artefactos o hueso | NO ENCONTRADO EN EL PDF | --- |
| 6a | Codigo en GitHub | "nnU-Net's source code is available on GitHub (https://github.com/MIC-DKFZ/nnUNet)" | Methods, Implementation details, p. 11 |
| 6b | PyPI | "can install nnU-Net via PyPI" | Methods, Implementation details, p. 11 |
| 6c | Code availability | "The nnU-Net repository is available as Supplementary Software." | Code availability, p. 11 |
| 6d | Versiones actualizadas | "Updated versions can be found at https://github.com/mic-dkfz/nnunet." | Code availability, p. 11 |
| 6e | Modelos preentrenados | "Pretrained models for all datasets in this study are available" (https://zenodo.org/record/3734294) | Code availability, p. 11 |
| 6f | Datos | "All 23 datasets used in this study are publicly available" | Data availability, p. 11 |
| 6g | Reporting Summary: codigo | "Our code is publicly available at github.com/mic-dkfz/nnunet." | Reporting Summary, Software and code, p. 13 |
| 6h | Licencia del codigo o de los modelos | NO ENCONTRADO EN EL PDF. La unica licencia impresa es la del articulo: "© The Author(s), under exclusive licence to Springer Nature America, Inc. 2020" | p. 9 |

### Metadatos contrastados con `refs/raw/`

| Dato | Frase original (<15 palabras) o estado | Seccion / pagina |
|---|---|---|
| Titulo | "nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation" | Titulo, p. 1 |
| Autores | "Fabian Isensee, Paul F. Jaeger, Simon A. A. Kohl, Jens Petersen and Klaus H. Maier-Hein" | p. 1 |
| DOI | "https://doi.org/10.1038/s41592-020-01008-z" | Cabecera, p. 1 |
| Fechas | "Received: 1 April 2020; Accepted: 29 October 2020; Published online: 07 December 2020" | p. 9 |
| Volumen 18, numero 2, pp. 203-211 | NO ENCONTRADO EN EL PDF | --- |
| Contribucion igual | "These authors contributed equally: Fabian Isensee and Paul F. Jaeger." | Pie, p. 1 |
| Supplementary Notes, Supplementary Software, Extended Data | NO ENCONTRADO EN EL PDF (solo se remite a ellos en linea) | p. 9 (Online content) y p. 12 |

### Todas las cifras, umbrales, definiciones y criterios del paper

Nota de alcance (regla 6 de `CLAUDE.md`). No se transcriben uno por uno los rangos por tarea de la Fig. 3 (53 graficos con tipografia pequena, lectura visual poco fiable) ni los valores de eje de la Fig. 4b. El PDF no trae tablas de resultados numericos por dataset: estan en material suplementario que no esta incluido.

| Cifra / criterio | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| 70% de los retos | "accounting for 70% of international image analysis competitions in the biomedical sector" | Introduccion, p. 1 |
| Desarrollo en 10 datasets | "developed and validated on the ten datasets provided by the Medical Segmentation Decathlon" | Introduccion, p. 1 |
| 53 tareas | "Altogether, we report results on 53 segmentation tasks" | Introduccion, p. 2 |
| Batch > 1 basta | "in practice any batch size larger than one already results in robust training" | Results, p. 2 |
| Regla patch/topologia/batch | "until the network can be trained with a batch size of at least two" | Results, p. 4 |
| Principios de diseno | "a compilation of guiding principles ... is provided in Supplementary Note 2" | Results, p. 4 |
| Entrenamiento desde cero | "nnU-Net was trained from scratch using only the provided challenge data" | Results, p. 4 |
| Figura 2: learning rate | "Poly learning rate schedule (initial, 0.01)" | Fig. 2 (tabla), p. 3 |
| Figura 2: perdida | "Dice and cross-entropy" | Fig. 2 (tabla), p. 3 |
| Figura 2: plantilla | "Encoder–decoder with skip-connection ('U-Net-like') and instance normalization, leaky ReLU, deep supervision" | Fig. 2 (tabla), p. 3 |
| Figura 2: optimizador | "SGD with Nesterov momentum (μ = 0.99)" | Fig. 2 (tabla), p. 3 |
| Figura 2: entrenamiento | "1,000 epochs × 250 minibatches, foreground oversampling" | Fig. 2 (tabla), p. 3 |
| Figura 2: inferencia | "Sliding window with half-patch size overlap, Gaussian patch center weighting" | Fig. 2 (tabla), p. 3 |
| Figura 2: normalizacion CT | "If CT, global dataset percentile clipping & z score with global foreground mean" | Fig. 2 (tabla), p. 3 |
| Figura 2: normalizacion no CT | "Otherwise, z score with per image mean and s.d." | Fig. 2 (tabla), p. 3 |
| Figura 2: remuestreo de imagen | "If anisotropic, in-plane with third-order spline, out-of-plane with nearest neighbor" | Fig. 2 (tabla), p. 3 |
| Figura 2: remuestreo de anotacion | "Convert to one-hot encoding"; anisotropico: "in-plane with linear interpolation" | Fig. 2 (tabla), p. 3 |
| Figura 2: spacing objetivo | "If anisotropic, lowest resolution axis tenth percentile, other axes median." | Fig. 2 (tabla), p. 3 |
| Figura 2: disparo de la cascada | "covers less than 12.5% of the median resampled image shape" | Fig. 2 (tabla), p. 3 |
| Figura 2: low resolution | "until the configured patch size covers 25% of the median image shape" | Fig. 2 (tabla), p. 3 |
| Figura 2: CV de 5 particiones | "trained in a five-fold cross-validation" | Fig. 2 (leyenda), p. 3 |
| KiTS: MICCAI >= 50% | "has consistently hosted at least 50% of all annual biomedical image analysis challenges" | Results, p. 4 |
| KiTS: >100 participantes | "With more than 100 competitors, the KiTS challenge was the largest competition" | Results, p. 4 |
| KiTS: grid search | "Only one submission (rank 18 of 100) reported the selection" | Results, p. 4 |
| KiTS: top 15 | "the top 15 methods were derived from the (3D) U-Net architecture from 2016" | Results, p. 4 |
| KiTS: top 15 (figura) | "All top 15 contributions were encoder–decoder architectures with skip-connections, 3D convolutions" | Fig. 4 (leyenda), p. 6 |
| 22 datasets adicionales | "in line with our results from 22 additional datasets (Fig. 3)" | Results, p. 4 |
| Fingerprints de 23 datasets | "We extracted the data fingerprints of 23 biomedical segmentation datasets." | Results, p. 4 |
| Fecha de leaderboards | "all remaining leaderboards were last accessed on 12 December 2019" | Fig. 3 (leyenda), p. 5 |
| Cell Tracking Challenge | "(D20–D23) was last accessed on 30 July 2020" | Fig. 3 (leyenda), p. 5 |
| CHAOS: subtareas | "we only participated in two of the five subtasks" | Fig. 3 (leyenda), p. 5 |
| Escalas de la Fig. 3 | "DC, Dice score (higher is better)"; "SL, other score (lower is better)"; "SH, other score (higher is better)" | Fig. 3 (leyenda), p. 5 |
| Variantes en 10 datasets | "The following variations were evaluated across ten different datasets" | Results, p. 6 |
| Cinco de nueve variantes | "five of the nine variants achieved rank 1 in at least one of the datasets" | Results, p. 6 |
| Sin mejora consistente | "none of them exhibited consistent improvements across the ten tasks" | Results, p. 6 |
| Configuracion original primera | "The original nnU-Net configuration showed the best generalization and ranked first" | Results, p. 6 |
| Variantes: perdidas | "two alternative loss functions (cross-entropy and TopK10)" | Fig. 6 (leyenda), p. 8 |
| Variantes: convoluciones | "using three instead of two convolutions per resolution" | Fig. 6 (leyenda), p. 8 |
| Variante: momentum | "Momentum, μ = 0.9" | Fig. 6 (leyenda del grafico), p. 8 |
| Ablaciones adicionales | "ablation experiments for further design choices can be found in Supplementary Note 8" | Fig. 6 (leyenda), p. 8 |
| Bootstrap | "One thousand virtual validation sets were generated via bootstrapping (drawn with replacement)." | Fig. 6 (leyenda), p. 8 |
| Estado del arte en la mayoria | "nnU-Net sets a new state of the art for the majority of tasks" | Discussion, p. 6 |
| CREMI | "nnU-Net's performance is highly competitive (rank 6 of 39)" | Discussion, p. 8 |
| Recorte a region no nula | "nnU-Net crops the provided training cases to their non-zero region." | Methods, Dataset fingerprints, p. 10 |
| Fingerprint de intensidad | "the 0.5 and 99.5 percentiles of the intensity values in the foreground regions" | Methods, Dataset fingerprints, p. 10 |
| Batch de 2 | "most 3D U-Net configurations were trained with a batch size of only two" | Methods, Fixed parameters, p. 10 |
| Instance normalization | "We therefore used instance normalization for all U-Net models." | Methods, Fixed parameters, p. 10 |
| Leaky ReLU | "(negative slope, 0.01)" | Methods, Fixed parameters, p. 10 |
| Deep supervision | "added in the decoder to all but the two lowest resolutions" | Methods, Fixed parameters, p. 10 |
| Mapas iniciales | "the initial number of feature maps is set to 32" | Methods, Fixed parameters, p. 10 |
| Tope de mapas | "capped at 320 and 512 for 3D and 2D U-Nets, respectively" | Methods, Fixed parameters, p. 10 |
| Epocas | "trained for 1,000 epochs, with one epoch being defined as iteration over 250 mini-batches" | Methods, Training schedule, p. 10 |
| Optimizador | "Nesterov momentum (μ = 0.99) and an initial learning rate of 0.01" | Methods, Training schedule, p. 10 |
| Politica poly | "(1 − epoch/epoch_max)^0.9" | Methods, Training schedule, p. 10 |
| Perdida | "The loss function is the sum of cross-entropy and Dice loss" | Methods, Training schedule, p. 10 |
| Pesos de deep supervision | "w2 = ½ × w1, w3 = ¼ × w1, etc. and are normalized to sum to 1" | Methods, Training schedule, p. 10 |
| Oversampling | "66.7% of samples are from random locations"; "33.3% of patches are guaranteed to contain" foreground | Methods, Training schedule, p. 10 |
| Minimo de patches con foreground | "rounded with a forced minimum of 1" | Methods, Training schedule, p. 10 |
| Detalle del aumento de datos | "Details are provided in Supplementary Note 4." No esta en el PDF | Methods, Training schedule, p. 10 |
| Solapamiento | "Adjacent predictions overlap by half of the size of a patch." | Methods, Inference, p. 10 |
| TTA | "Test time augmentation by mirroring along all axes is applied." | Methods, Inference, p. 10 |
| Normalizacion por defecto | "The default setting for all modalities, except for CT images, is z-scoring." | Methods, Intensity normalization, p. 10 |
| Mascara por recorte >= 25% | "If cropping resulted in an average size decrease of 25% or more" | Methods, Intensity normalization, p. 10 |
| Recorte CT | "uses the 0.5 and 99.5 percentiles of the foreground voxels for clipping" | Methods, Intensity normalization, p. 10 |
| Interpolacion por defecto | "The default setting for image data is third-order spline interpolation." | Methods, Resampling, p. 10 |
| Umbral de anisotropia (remuestreo) | "(maximum axis spacing ÷ minimum axis spacing > 3)" | Methods, Resampling, p. 10 |
| Spacing objetivo | "uses the median value of the spacings found in the training cases" | Methods, Target spacing, p. 10 |
| Percentil 10 | "the lowest resolution axis is selected to be the tenth percentile" | Methods, Target spacing, p. 10 |
| Condicion del percentil 10 | "if both voxel and spacing anisotropy ... are greater than three" | Methods, Target spacing, p. 10 |
| Batch minimo | "we require a minimum batch size of two" | Methods, Adaptation of network topology, p. 10 |
| Sin GPU para configurar | "no GPU is required to run the adaptation process" | Methods, Adaptation of network topology, p. 10 |
| Tope de downsampling | "would reduce the feature map size to less than four voxels" | Methods, Architecture topology, p. 11 |
| Factor 2 entre ejes | "within a factor of two of the lower resolution axis" | Methods, Architecture topology, p. 11 |
| Kernels por defecto | "The default kernel size for convolutions is 3×3×3 and 3×3" | Methods, Architecture topology, p. 11 |
| Kernel fuera de plano | "(defined as a spacing ratio larger than two)" | Methods, Architecture topology, p. 11 |
| Paso de reduccion del patch | "The reduction in one step amounts to 2nd voxels of that axis" | Methods, Adaptation to GPU memory budget, p. 11 |
| Tope del batch (5%) | "do not exceed 5% of the total number of voxels of all training cases" | Methods, Batch size, p. 11 |
| Paso de spacing de la cascada | "the target spacing is increased stepwise by 1%" | Methods, Configuration of the 3D U-Net cascade, p. 11 |
| Parada de la cascada | "surpasses 25% of the current median image shape" | Methods, Configuration of the 3D U-Net cascade, p. 11 |
| Anisotropia en la cascada | "(the difference between lowest and highest resolution axes is a factor of two)" | Methods, Configuration of the 3D U-Net cascade, p. 11 |
| Implementacion | "implemented in Python 3.8.5 using PyTorch framework 1.6.0" | Methods, Implementation details, p. 11 |
| Aumento de datos | "Batchgenerators 0.21 (ref. 53) is used for data augmentation." | Methods, Implementation details, p. 11 |
| Otras bibliotecas | "SimpleITK 1.2.4 and pandas 1.1.1" (tambien tqdm 4.48.2, SciPy 1.5.2, NumPy 1.19.1, entre otras) | Methods, Implementation details, p. 11 |
| Experimentos en 23 datasets | "conducted the experiments on the 23 selected datasets" | Author contributions, p. 12 |
| Conflictos | "The authors declare no competing interests." | Competing interests, p. 12 |
| Reporting Summary: fecha | "Last updated by author(s): 15.10.2020" | p. 13 |
| Tamano muestral | "We evaluate our algorithm on 23 publicly available datasets." | Reporting Summary, Sample size, p. 14 |
| Exclusiones | "No data was excluded from the analysis." | Reporting Summary, Data exclusions, p. 14 |
| Replicacion | "perform only one submission (i.e. one replication) to avoid overfitting" | Reporting Summary, Replication, p. 14 |
| Entrenamientos fallidos | "we have not observed failed trainings or configurations" | Reporting Summary, Replication, p. 14 |
| Ablaciones | "cross-validation results (1 run) from which 1000 bootstrap subsets were sampled" | Reporting Summary, Replication, p. 14 |
| Ciego | "did not have access to labels of the corresponding test data" | Reporting Summary, Blinding, p. 14 |

### Contraste con la ficha anterior (preprint arXiv:1904.08128v2)

| Afirmacion de la ficha del preprint | Estado en el articulo publicado | Evidencia |
|---|---|---|
| (a) No es precedente de la limpieza por fraccion F: solo evalua el componente mayor, decidido por Dice en CV, sin umbral de tamano | **Se mantiene** | 4a-4l; umbral y conectividad NO ENCONTRADOS (4l, 4m) |
| (a') Supuesto de "una sola instancia" (B.3 del preprint) | **No se puede verificar**: esa frase no esta en el PDF publicado | 4n |
| (b) Sin CT oseo ni metal; los CT son de abdomen, pulmon y torax | **Se mantiene**. Los cuatro datasets nuevos (D20-D23) son de microscopia de fluorescencia, no CT | 3g-3l, Fig. 5 |
| (b') "Intensities ... consistent between scanners" y rangos de recorte CT por dataset | **No se puede verificar**: no estan en el PDF (eran suplemento del preprint) | --- |
| (c) "self-configuring" NO ENCONTRADO en el PDF | **Cambia**: ahora esta en el titulo (p. 1). En el cuerpo sigue sin aparecer | 1k, 1l |
| (d) Inconsistencia sobre las configuraciones por defecto (3 frente a 4) | **Se mantiene**: 3 por defecto (p. 4, Fig. 2) y 4 seleccionables en Methods (p. 11). La tabla F del preprint (4 corridas) no esta en el PDF | 2a-2f |
| (e1) 19 datasets, 49 tareas, 10 retos; estado del arte en 29 de 49 | **Cambia**: 23 datasets, 53 tareas, 11 retos; 33 de 53 | 3b, 3m |
| (e2) Inconsistencia Abstract "19 competitions" frente a 10 retos | **Desaparece**: el Abstract habla de 23 datasets y el cuerpo es coherente (10 + 13 = 23) | 3a, 3c, 3d |
| (e3) "Sum" frente a "averaged" en la perdida | **No se puede verificar**: el PDF solo dice "sum" (Methods) y "Dice and cross-entropy" (Fig. 2) | Perdida, p. 10 |
| (e4) Discrepancias numericas de LiTS (C.2 frente a F.28/F.6) y desviacion 39.36 frente a 39.39 | **No se puede verificar**: el PDF no trae esas secciones | --- |
| (e5) Umbral del 15% del patch en el aumento de datos de la cascada | **No se puede verificar**: remitido a Supplementary Note 4 | Methods, Training schedule, p. 10 |
| (e6) "Nvidia Apex/Amp", tiempos de entrenamiento y 11 GB de GPU | **No se puede verificar** en el PDF publicado | --- |
| (e7) Code availability, Zenodo 3734294, CREMI 6/39, leaderboards del 12-12-2019 | **Se mantiene**. Ademas el CTC tiene fecha de acceso propia (30-07-2020) | 6a-6e; Fig. 3 |
| (e8) Duda 2 del preprint: "la cita no aparece en `tesis/`" | **Superada**: `tesis/main.tex` l. 76 ya cita `isensee2021` (no depende del PDF) | --- |
| (e9) Duda 1 del preprint: el PDF no coincide con el raw | **Resuelta**: el PDF es el articulo de Nature Methods del raw | Metadatos |
