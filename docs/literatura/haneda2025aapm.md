# haneda2025aapm — AAPM CT metal artifact reduction grand challenge

- **DOI / URL:** 10.1002/mp.70050
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/haneda2025aapm.pdf

Profundidad: PDF completo (19 paginas, Special Report, Medical Physics 2025;52:e70050).

## Que hace (3 lineas maximo)

Reporta el reto AAPM CT-MAR: distribuye 14 000 datasets 2D de entrenamiento generados con
CatSim/XCIST insertando metal virtual en CT clinicas reales, y 29 casos clinicos de scoring
con metal insertado y posicionado a mano. Evalua 26 equipos con ocho metricas de calidad de
imagen normalizadas 0–4 y los compara contra NMAR como referencia.

## Restriccion o supuesto clave

No es un paper de sintesis generativa, pero su supuesto de simulacion es directamente
relevante: el metal virtual del set de entrenamiento se coloca sin anatomia guiando la pose
—"The metal objects were inserted in random soft tissue or bone locations" (Sec. 2.2)— y solo
en los datasets de scoring se recurre a intervencion humana: "here metal objects were manually
designed and positioned to represent realistic anatomy and metal combinations" (Sec. 2.3). Es
decir, el trabajo no ofrece un muestreador automatico de pose anatomicamente plausible; lo
sustituye por diseno manual. Segunda restriccion explicita: el simulador falla para metal
grande, "the metal trace ... may look distorted for large metal objects with diameters larger
than 3.0 cm" (Sec. 4).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

Baseline de comparacion en dos sentidos: (a) confirma XCIST/CatSim como generador de referencia
aceptado por la comunidad AAPM, con parametros publicados; (b) aporta un juego de metricas y
umbrales ya calibrados que podrian complementar SAP/BFC/ISC.

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 14 000 datasets de entrenamiento simulados con CatSim/XCIST | "14,000 CT training datasets were provided ... generated using the CatSim CT simulator" | Sec. 2.1, p. 3 |
| Metal grande (>3.0 cm) distorsiona la traza en XCIST; 274/14 000 afectados | "may look distorted for large metal objects with diameters larger than 3.0 cm" | Sec. 4, p. 16 |
| 29 casos clinicos de scoring final | "a total of 29 clinical uncorrected datasets were provided" | Sec. 2.1, p. 4 |
| Umbral de hueso: 150 HU | "all voxels with a CT number above 150 HU ... were considered bone" | Sec. 2.3, p. 7 |
| Umbral de metal: max HU sin metal + 250 HU | "the highest CT number in the ground truth without metals plus a margin of 250 HU" | Sec. 2.3, p. 7 |
| Escala de puntuacion 0–4, NMAR anclado en 2 | "normalized to a range from 0 ... to 4.0"; "assigning a score of 2 to the popular NMAR" | Sec. 2.3, p. 6 |
| 92% de los equipos usaron deep learning; 31% difusion | "92% of the teams used Deep Learning (DL) approaches"; "31% of the teams used a diffusion model" | Sec. 3.1, p. 11 |
| Mejor score global 0.96 (1er lugar) | "The best overall score achieved so far was 0.96" | Sec. 4, p. 16 |
| Simulado sin metal es indistinguible del clinico original | "visually indistinguishable from the original clinical images" | Sec. 2.2, p. 5 |

## Donde entra en mi tesis

1. **Justificacion del baseline fisico.** Respalda XCIST/CatSim como simulador de referencia de
   la comunidad AAPM y publica geometria y parametros usables para la reimplementacion del
   alcance COMPLETO (Sec. 2.2).
2. **Metricas de evaluacion peri-implante.** Bone integrity (Dice + cambio de volumen sobre
   voxeles >150 HU) es la metrica del paper mas cercana al objetivo de segmentacion osea
   peri-implante de la tesis; puede citarse como precedente para BFC/ISC.
3. **Delimitacion del gap del muestreador.** Evidencia de que la colocacion realista de metal
   sigue siendo manual en el estado del arte del benchmark.
4. **Limite conocido del baseline.** El fallo de la traza para metal >3.0 cm acota que tan
   lejos puede llevarse el brazo XCIST con placas grandes.

## Dudas para el asesor

- Adoptamos la escala 0–4 anclada en NMAR=2 para reportar nuestras metricas, o mantenemos
  metricas absolutas? Anclar a NMAR haria comparables nuestros numeros con este benchmark.
- Bone integrity de este reto (Dice + volumen sobre umbral 150 HU) puede sustituir o solo
  complementar a BFC? Es un umbral global, no cortical.
- El reto es 2D y de una sola fila de detector; nuestra propuesta es 2.5D. Vale la pena
  reportar en su formato 2D para poder compararnos, aunque generemos en 2.5D?

## Evidencia textual

| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Simulador usado | "generated using the CatSim CT simulator in the open-access toolkit XCIST" | Sec. 2.2, p. 5 |
| Marco de generacion | "a hybrid data simulation framework that combined real patient images ... with virtual metal objects" | Abstract, p. 1 |
| Anatomias del entrenamiento | "including lung, abdomen, liver, head, and pelvis—with virtual metal objects" | Abstract, p. 1 |
| Tipos de dato por caso | "CT sinograms (uncorrected and metal-free), CT reconstructed images ..., and metal masks" | Abstract, p. 1 |
| Numero de datasets de entrenamiento | "14,000 CT training datasets were provided" | Sec. 2.1, p. 3 |
| Imagenes body y pacientes | "12,227 'body' images with different anatomies ... from about 1,230 patients" | Sec. 2.2, p. 5 |
| Fuente body | "in the NIH DeepLesion dataset" | Sec. 2.2, p. 5 |
| Imagenes head y pacientes | "1,773 'head' images were collected from 10 patients in the UCLH Stroke EIT Dataset" | Sec. 2.2, p. 5 |
| Criterio de inclusion por tamano de metal preexistente | "Patients scans with very small metal objects (<=30 pixels) were included" | Sec. 2.2, p. 5 |
| Criterio de exclusion | "those with more extensive metal objects were excluded, to avoid pre-existing streaks" | Sec. 2.2, p. 5 |
| Forma del metal virtual | "defined as random shapes synthesized by generating vertices of a random fractal shape" | Sec. 2.2, p. 5 |
| Colocacion del metal (entrenamiento) | "The metal objects were inserted in random soft tissue or bone locations" | Sec. 2.2, p. 5 |
| Materiales metalicos | "amalgam, stainless steel, copper, cobalt, and titanium" | Sec. 2.2, p. 5 |
| Numero de objetos por imagen | "Up to five metal objects of the same material with different shapes were inserted per image" | Sec. 2.2, p. 5 |
| Pre-proceso de las imagenes clinicas | "Moderate spatial frequency boosting was applied to the patient images prior to CT simulation" | Sec. 2.2, p. 5 |
| Criterio de realismo (cualitativo) | "visually indistinguishable from the original clinical images, which is an important property" | Sec. 2.2, p. 5 |
| Geometria: distancias | "source-to-iso-distance 550 mm, source-to-detector distance 950 mm" | Sec. 2.2, p. 5 |
| Geometria: foco y detector | "1.0 mm x 1.0 mm focal spot size ... 1.0 mm x 1.0 mm detector cells with fill factor 90% x 90%" | Sec. 2.2, p. 5 |
| Adquisicion | "120 kVp tube voltage, 500 mA tube current, one detector row, 900 detector columns, 1000 views" | Sec. 2.2, p. 5 |
| Submuestreo de la fuente | "sampled with two sample points, resulting in eight sub-samples total" | Sec. 2.2, p. 5 |
| Rejilla antidispersion | "an anti-scatter grid with an aspect ratio of 9.8, resulting in a scatter kernel width of 49 detector columns" | Sec. 2.2, p. 5 |
| FOV | "FOV for body data was set to 400 mm, and the one for head was 220.16 mm over 512 x 512 pixels" | Sec. 2.2, p. 5 |
| Espectro | "The X-ray source spectrum is defined as a sum over a discrete set of energy levels (i.e., 12 energies)" | Sec. 2.2, p. 5 |
| Diametros de metal de ejemplo (body) | "three stainless steel objects with 9.3, 5.2, and 2.8 mm in diameter" | Sec. 2.2, p. 5 |
| Diametros de metal de ejemplo (head) | "three amalgam objects with 3.1, 2.1, and 1.5 mm in diameter" | Sec. 2.2, p. 5 |
| Origen de los datos de scoring | "The scoring datasets were based on clinical CT scans acquired at the Massachusetts General Hospital" | Sec. 2.3, p. 6 |
| Colocacion del metal (scoring) | "here metal objects were manually designed and positioned to represent realistic anatomy" | Sec. 2.3, p. 6 |
| Colocacion clinica (scoring) | "The metal implants were inserted into clinically realistic locations" | Sec. 2.1, p. 4 |
| Casos de scoring | "a total of 29 clinical cases with the clinically most relevant metal scenarios" | Sec. 2.3, p. 6 |
| Escenarios de metal | "surgical clips, fiducial marker seeds, and dental fillings ... pacemakers, larger dental work, and spinal reconstruction" | Sec. 2.3, p. 6 |
| Escenarios grandes | "up to large, full joint replacements (shoulder and hip)" | Sec. 2.3, p. 6 |
| Numero de metricas | "A total of eight scoring metrics were computed to evaluate MAR quality" | Sec. 2.3, p. 6 |
| Lista de metricas | "CT number (CTN) accuracy, noise, image sharpness, streak amplitude, structural integrity (SSIM), metal integrity, bone integrity, and ... proton beam range" | Sec. 2.3, p. 6 |
| Escala de puntuacion | "normalized to a range from 0 (no relevant differences relative to ground truth) to 4.0" | Sec. 2.3, p. 6 |
| Calibracion de la escala | "The score was calibrated by assigning a score of 2 to the popular NMAR algorithm" | Sec. 2.3, p. 6 |
| Score total | "The total score was computed as the average of the eight scoring metrics" | Sec. 2.3, p. 6 |
| Definicion CTN | "defined as the root-mean-square error (RMSE) between the ground truth and the MAR image" | Sec. 2.3, p. 6 |
| Normalizacion de ruido | "A linear increase from the ground truth noise (score 0) to roughly two times the ground truth noise (score 4)" | Sec. 2.3, p. 6 |
| Definicion de sharpness | "A Sobel filter was applied to determine the absolute gradient magnitude within the respective ROI" | Sec. 2.3, p. 6 |
| Estadistico de sharpness | "quantified as the 90th percentile gradient magnitude value to minimize the influence of outliers" | Sec. 2.3, p. 6 |
| Umbrales de sharpness | "a Gaussian blur with a sigma of 0.4, 0.5, 0.75 and 1 is introduced, respectively" | Sec. 2.3, p. 6 |
| Definicion de streak | "the average over the highest and lowest 5% CT number deviation to ground truth in each ROI" | Sec. 2.3, pp. 6–7 |
| Definicion de structural integrity | "quantified using the structural similarity index (SSIM) within the patient geometry excluding the metal ground truth" | Sec. 2.3, p. 7 |
| Umbral de hueso | "all voxels with a CT number above 150 HU (excluding the metals) were considered bone" | Sec. 2.3, p. 7 |
| Metrica de bone integrity | "determined by the average of two values: volume change and Sorensen–Dice coefficient" | Sec. 2.3, p. 7 |
| Umbral de metal | "the highest CT number in the ground truth without metals plus a margin of 250 HU" | Sec. 2.3, p. 7 |
| Instruccion sobre el metal | "recommended the participants to fill in their estimated metal region with the value at or slightly above the threshold" | Sec. 2.3, p. 7 |
| Umbral de PBR | "A score of zero corresponds to no WET shift, linearly increasing to a score of 4 for a range shift of 2%" | Sec. 2.3, p. 7 |
| Sets adicionales RMSE/PSNR/SSIM | "participants were provided 1,000 new test cases ... (850 from Deep Lesion datasets and 150 from UCLH Stroke EIT dataset)" | Sec. 2.4, p. 7 |
| Rango de clipping para metricas estandar | "clipped to the range of [-2000 6000] HU and normalized to the [0 1] range" | Sec. 3.2, p. 11 |
| Fases del reto | "Phase 1: Training & Development (Oct 30, 2023–Feb 18, 2024)" | Sec. 2.1, p. 3 |
| Fase 2 | "Phase 2: Feedback & Refinement phase (Feb 19, 2024–May 5, 2024)" | Sec. 2.1, p. 3 |
| Fase 3 | "Phase 3: Final Scoring phase (May 6, 2024–May 20, 2024)" | Sec. 2.1, p. 3 |
| Datasets de fase 2 | "a total of five clinical uncorrected datasets were provided in sinogram domain and in image domain" | Sec. 2.1, p. 3 |
| Envios permitidos en fase 2 | "Participants were allowed to submit their results up to three times during Phase 2" | Sec. 2.1, p. 4 |
| Tiempo de fase 3 | "Participants were given 2 weeks to submit the final results" | Sec. 2.1, p. 4 |
| Alcance 2D | "our scope was limited to single-energy CT to ensure broadest applicability" | Sec. 2.1, p. 3 |
| Justificacion del 2D | "the vast majority of MAR research is performed in 2D" | Sec. 2.1, p. 3 |
| Fisica 3D pese al 2D | "extracting only the center row of a 3D CT scanner, but still including scattered radiation of a wide-cone 3D CT geometry" | Sec. 2.1, p. 3 |
| Premios | "an award pool of $4000: $2000 for the first place, $1500 for the second place, and $500 for the third" | Sec. 2.1, p. 3 |
| Equipos registrados | "A total of 106 teams (participants) registered for the CT-MAR Challenge" | Sec. 3.1, p. 11 |
| Equipos que completaron | "with 26 teams completing all phases and submitting final results" | Sec. 3.1, p. 11 |
| Distribucion geografica | "34% were from institutes in the United States, 23% from South Korea, 23% from China, and 8% from Germany" | Sec. 3.1, p. 11 |
| Origen institucional | "77% of the teams were from academic institutes" | Sec. 3.1, p. 11 |
| Dominio de los metodos | "27% of the teams used sinogram domain approaches, 31% used image domain approaches, and 42% worked in both" | Sec. 3.1, p. 11 |
| Uso de DL | "92% of the teams used Deep Learning (DL) approaches and 8% used analytical (non-DL) approaches" | Sec. 3.1, p. 11 |
| Familias de arquitectura | "six families: UNet, ResNet, GAN, Diffusion model, Transformers, and others" | Sec. 3.1, p. 11 |
| Porcentajes por arquitectura (Fig. 7) | "UNET 54%, ResNet 23%, GAN 19%, Diffusion 31%, Transformer 19%, Others 12%, non-DL 8%" | Fig. 7, p. 12 |
| Mejor no-DL | "The highest-ranking non-DL approach placed 15th" | Sec. 3.1, p. 11 |
| Difusion en el ranking | "31% of the teams used a diffusion model, with the highest-ranking team in 5th place and 4 in the top 10" | Sec. 3.1, p. 11 |
| Transformers en el ranking | "the highest ranking team in 4th place and 4 teams ranked in the top 10" | Sec. 3.1, p. 11 |
| Mejor solo-imagen y solo-sinograma | "highest-ranked image-domain-only approach was in 4th place ... sinogram-domain-only approach was in 14th place" | Sec. 3.1, p. 11 |
| Top 3 es dual-domain | "The top 3 teams used dual domain approaches, combining the strengths of both domains" | Sec. 3.1, p. 11 |
| Combinacion sino+imagen | "22% of the teams—including the top three teams—utilized a combination of sinogram- and image-domain approaches" | Abstract, p. 1 |
| Superacion de NMAR | "More than 70% of the teams achieved a better overall score than the popular baseline NMAR method" | Abstract, p. 1 |
| Score final 1er lugar | "1 | 0.96 | Sino, image ... CNN, UNet" | Tabla 1, p. 13 |
| Score final 2do lugar | "2 | 0.98 ... Implicit neural representation, ResNet" | Tabla 1, p. 13 |
| Score final 3er lugar | "3 | 0.99 ... Swin Transformer-based UNet, ResNet" | Tabla 1, p. 13 |
| Mejor equipo con difusion latente (5to) | "5 | 1.06 | Sino, image | Yes | CT number | Latent Diffusion model, Attention UNet" | Tabla 1, p. 13 |
| Score de NMAR | "NMAR | 1.82 | Sino | N/A" | Tabla 1, p. 13 |
| Peor score | "26 | 3.34 | Sino ... UNet, Noise2Noise" | Tabla 1, p. 13 |
| Desglose 1er lugar | "best CT number (0.74), low noise (0.01), streak suppression (1.29), accurate SSIM (0.75), and bone integrity (0.89)" | Sec. 3.1, p. 13 |
| Metal integrity 1er lugar | "1 | ... | Metal integrity 1.46 | Bone integrity 0.89 | PBR 1.79" | Tabla 2, p. 14 |
| Mejor metal integrity (3er lugar) | "3 | 0.99 | 0.82 | 0.01 | 0.54 | 1.48 | 0.98 | 0.96 | 1.09 | 2.03" | Tabla 2, p. 14 |
| Mejor sharpness y PBR (2do lugar) | "2 | 0.98 | 0.81 | 0.19 | 0.52 | 1.65 | 0.95 | 1.09 | 0.99 | 1.62" | Tabla 2, p. 14 |
| Estabilidad del top 5 | "with their individual cases ranking within the top 10 in 90% of cases" | Sec. 3.3, p. 15 |
| Transferencia sim-a-real | "methods trained with simulated metal artifacts generally can be applied directly to data with real metal objects" | Sec. 3.3, p. 15 |
| Condicion de esa transferencia | "for image-domain methods if the simulated artifacts are shown to be very realistic" | Sec. 3.3, p. 15 |
| Sensibilidad de metodos fisicos | "methods based on physics-based corrections may be more sensitive to small deviations of the physics models" | Sec. 3.3, p. 15 |
| Necesidad de reentrenamiento | "We expect retraining and tuning is required for dealing with the domain shift" | Sec. 3.3, p. 15 |
| Efecto adverso del DL | "A side effect of deep learning methods is hallucinations" | Sec. 3.3, p. 15 |
| Manifestacion de la alucinacion | "deep learning methods sometimes restores tissues differently from the ground truth with their own estimations" | Sec. 3.3, p. 15 |
| Practica comun en MAR con DL | "Many deep learning-based MAR studies rely on numerical simulations, where metal artifacts are synthetically introduced" | Sec. 1, p. 2 |
| Falta de estandarizacion | "The simulation settings—such as geometry and metal properties—vary across studies" | Sec. 1, p. 2 |
| Ausencia de benchmark universal | "Despite decades of research in MAR, a universal benchmark for objectively comparing MAR techniques remains absent" | Sec. 1, p. 2 |
| Metricas comunes previas | "Popular quantitative evaluation metrics are RMSE, PSNR, and SSIM" | Sec. 1, p. 2 |
| Limitacion: pocos datos de cabeza | "our training data contained a small percentage of head data due to the limited availability of public head data" | Sec. 4, p. 15 |
| Limitacion: sesgo esperado | "This could result in a bias in MAR performance such as poor MAR in dental regions" | Sec. 4, p. 15 |
| Limitacion: falta de metricas de tarea | "task-based metrics such as lesion detectability are still lacking" | Sec. 4, p. 16 |
| Limitacion: ruido en el ground truth | "the ground truth is not entirely free of artifacts" | Sec. 4, p. 16 |
| Limitacion: voxel fijo | "we fixed the reconstruction voxel size to simplify the development and comparative evaluation" | Sec. 4, p. 16 |
| Limitacion del simulador con metal grande | "the metal trace in the training sinogram generated by the XCIST simulator may look distorted" | Sec. 4, p. 16 |
| Diametro critico | "for large metal objects with diameters larger than 3.0 cm" | Sec. 4, p. 16 |
| Causa | "due to the imperfection of the kernel-based scatter correction, which was typically tuned for tissue/water" | Sec. 4, p. 16 |
| Datasets afectados | "Out of the 14,000 datasets, 274 were affected" | Sec. 4, p. 16 |
| Mejor score alcanzado | "The best overall score achieved so far was 0.96" | Sec. 4, p. 16 |
| Disponibilidad | "All training datasets, scoring datasets, scoring tools, and development tools have been made available via GitHub" | Data Availability, p. 16 |
| Detalles del 1er lugar: datos extra | "an additional 15,000 head images collected from local hospitals and simulated with five types of material" | Sec. 2.5, p. 8 |
| Detalles del 1er lugar: optimizador | "The Mean Squared Error (MSE) loss function and Adam optimizer ... parameters (beta1, beta2) = (0.9, 0.999)" | Sec. 2.5, p. 8 |
| Detalles del 2do lugar: red | "consists of five fully connected layers, each comprising 64 nodes" | Sec. 2.6.1, p. 8 |
| Detalles del 2do lugar: pre-entrenamiento | "pre-trained on 5,000 ground-truth projection datasets randomly sampled from a total of 14,000" | Sec. 2.6.1, p. 8 |
| Detalles del 2do lugar: LR | "trained using the Adam optimizer with a learning rate of 5 x 10^-4" | Sec. 2.6.1, p. 8 |
| Detalles del 3er lugar: DICDNet | "The DICDNet used in the framework consists of 10 stages of X-Net and M-Net" | Sec. 2.7, p. 10 |
| Ventana de display (reconstrucciones) | "The display window for the reconstructed images is W/L = 1000/0 HU" | Fig. 3, p. 6 |
| Ventana de display (Fig. 10) | "The display window was set to [min max] = [-100, 100] HU to observe the tissue regions" | Fig. 10, p. 14 |
| Financiamiento | "supported by the NIH/NIBIB grant R01EB031102" | Acknowledgments, p. 16 |
| Relacion con peters2025hybrid | "A previous publication provides a detailed description of the training datasets and evaluation metrics" | Sec. 2.2, p. 5 |

## Verificacion de nivel

**1. Confirma o desmiente la relacion con peters2025hybrid.** CONFIRMADA, y de forma mas fuerte
que lo supuesto. No es solo "mismo numero de revista": este paper cita a peters2025hybrid como
su publicacion companera y descarga en ella la definicion formal del benchmark. La referencia 2
del paper es literalmente "Nils P, Haneda E, Zhang J, et al. A hybrid training database and
evaluation benchmark for assessing metal artifact reduction methods for imaging and therapy.
Med Phys. 2025. doi:10.1002/mp.70020" (Referencias, p. 16). Y en el cuerpo: "A previous
publication provides a detailed description of the training datasets and evaluation metrics, so
we provide only a brief overview here" (Sec. 2.2, p. 5), y "a full description is given in the
previous publication" respecto de las ocho metricas (Sec. 2.3, p. 6), y "The respective ROIs for
analysis were illustrated in the supplemental document of our previous publication" (Sec. 2.3,
p. 7). Ademas Nils Peters es coautor de este paper. Conclusion: peters2025hybrid define el
protocolo, haneda2025aapm es su aplicacion competitiva. La justificacion escrita sin leer el PDF
era correcta.

**2. Como se generaron los datos.** Dos regimenes distintos, ambos por insercion de metal
virtual en CT clinicas reales, no adquisiciones con fantomas ni casos con metal real:
- Entrenamiento: "a hybrid data simulation framework that combined real patient images ... with
  virtual metal objects" (Abstract, p. 1) y "generated using the CatSim CT simulator in the
  open-access toolkit XCIST" (Sec. 2.2, p. 5). Simulador nombrado: **CatSim, dentro del toolkit
  XCIST**. Fuentes clinicas: NIH DeepLesion y UCLH Stroke EIT Dataset (Sec. 2.2, p. 5).
- Scoring: CT clinicas del Massachusetts General Hospital, "The final scoring datasets were
  generated by the CatSim simulator using the same CT scanner geometry as the training datasets"
  (Sec. 2.3, p. 6), con metal "manually designed and positioned" (Sec. 2.3, p. 6).
- No hay adquisiciones de fantoma fisico ni casos clinicos con metal real como ground truth: el
  ground truth es siempre la imagen clinica pre-insercion. "the original ground truth originates
  from public datasets, which already contain some noise and possibly artifacts" (Sec. 4, p. 16).

**3. Casos pelvicos y osteosintesis.** Pelvis SI esta cubierta; osteosintesis pelvica NO.
- Pelvis en entrenamiento: "including lung, abdomen, liver, head, and pelvis" (Abstract, p. 1).
- Pelvis en scoring: "pelvis with a prosthesis" (Fig. 10, p. 14) y "ROI placements ... pelvis
  with a prosthesis (right)" (Fig. 11, p. 15). El caso pelvico ejemplar es **protesis de cadera**,
  no tornillos ni placas: "In the pelvis case, the streaks from the hip prosthesis were
  successfully eliminated" (Sec. 3.3, p. 15).
- Osteosintesis aparece solo fuera de la pelvis: "spinal screws or rods" (Sec. 1, p. 2), "spinal
  reconstruction" (Sec. 2.3, p. 6), "chest and spine with screws" (Sec. 3.3, p. 11 / Fig. 10).
- Anatomias totales cubiertas: pulmon, abdomen, higado, cabeza, pelvis (entrenamiento); cabeza
  con empastes, torax/columna con tornillos, pelvis con protesis, hombro y cadera con
  reemplazos articulares, prostata con marcadores de oro (scoring).
- Implantes de osteosintesis pelvica (tornillos iliosacros, placas de anillo pelvico):
  **NO ENCONTRADO EN EL PDF**.

**4. Metricas y umbrales.** Ocho metricas, todas normalizadas a la misma escala:
- Escala: "normalized to a range from 0 (no relevant differences relative to ground truth) to 4.0
  (no improvement over uncorrected image or our defined worst case)" (Sec. 2.3, p. 6).
- Anclaje: "The score was calibrated by assigning a score of 2 to the popular NMAR algorithm"
  (Sec. 2.3, p. 6). NMAR obtuvo 1.82 en la practica (Tabla 1, p. 13).
- CT number: RMSE excluyendo la geometria del metal (Sec. 2.3, p. 6).
- Noise: score 0 = ruido del ground truth, score 4 = "roughly two times the ground truth noise"
  (Sec. 2.3, p. 6).
- Sharpness: percentil 90 del gradiente Sobel; scores 1 a 4 corresponden a "Gaussian blur with a
  sigma of 0.4, 0.5, 0.75 and 1" (Sec. 2.3, p. 6).
- Streak: "the average over the highest and lowest 5% CT number deviation to ground truth"
  (Sec. 2.3, pp. 6–7).
- Structural integrity: SSIM dentro de la geometria del paciente excluyendo el metal (Sec. 2.3, p. 7).
- Bone integrity: umbral **150 HU**; "the average of two values: volume change and Sorensen–Dice
  coefficient" (Sec. 2.3, p. 7).
- Metal integrity: umbral = maximo HU del ground truth sin metal **+ 250 HU** (Sec. 2.3, p. 7).
- PBR: "A score of zero corresponds to no WET shift, linearly increasing to a score of 4 for a
  range shift of 2% relative to the largest beam range of the treatment field" (Sec. 2.3, p. 7).
- Score total = promedio de las ocho metricas sobre los 29 casos (Sec. 2.3, p. 6; Tabla 2, p. 14).
- Umbral de aprobado/reprobado o corte de aceptabilidad clinica: **NO ENCONTRADO EN EL PDF**
  (la escala es continua y comparativa, no define un umbral de "suficientemente bueno").

**5. Criterio de realismo de artefactos metalicos sinteticos.** SI existe, pero es **cualitativo
y visual**, no una metrica. Cita literal: "As a result, simulated and reconstructed images
without virtually inserted metal objects were visually indistinguishable from the original
clinical images, which is an important property of the hybrid data simulation framework"
(Sec. 2.2, p. 5). Notar que el criterio se enuncia sobre la imagen SIN metal (que el pipeline de
simulacion no degrade la anatomia base), no sobre el realismo del artefacto en si. El unico
enunciado sobre realismo del artefacto es condicional y sin metrica: "for image-domain methods
if the simulated artifacts are shown to be very realistic" (Sec. 3.3, p. 15), y una validacion
previa por acuerdo visual: "we observed good agreement in metal artifact appearance between
simulation and measurements" (Sec. 2.2, p. 5), delegada a la referencia 2.
Una definicion cuantitativa y directamente reutilizable de realismo de artefacto (distancia,
score perceptual, test de discriminacion): **NO ENCONTRADO EN EL PDF**.

**6. Metodos generativos participantes y ganador.** Hubo muchos generativos, pero **ninguno gano**.
- Difusion: 31% de los equipos; "the highest-ranking team in 5th place and 4 in the top 10"
  (Sec. 3.1, p. 11). El 5to lugar es "Latent Diffusion model, Attention UNet" con score **1.06**
  (Tabla 1, p. 13) — arquitectura muy cercana a la de la tesis, aplicada a MAR y no a sintesis.
  Otros con difusion: 6to (1.09), 8vo (1.16, "Diffusion model for image-to-image translation
  (I2SB)"), 9no (1.21), 12mo (1.45), 16to (1.58), 18vo (1.68), 25to (2.86, "Adversarial diffusion
  model").
- GAN: 19% de los equipos; mejores posiciones 10mo (1.39, "GAN family with Transformer based
  Model"), 11mo (1.42), 14to y 17mo ("GAN based LaMa"), 23ro (2.32, "StyleGAN3") (Tabla 1, p. 13).
- Ganador: 1er lugar con score **0.96**, no generativo — "CNN, UNet" (Tabla 1, p. 13), descrito
  como "a dual-learning framework" con "dual cycle consistency constraints" (Sec. 2.5, p. 7).
- Detalle relevante: los tres primeros son dual-domain, "The top 3 teams used dual domain
  approaches" (Sec. 3.1, p. 11), y el mejor de todos es un metodo con fisica explicita: "the
  physical mechanisms that produce metal artifacts are explicitly integrated into both mappings"
  (Sec. 2.5, p. 7).

**7. Sugiere que insertar metal sintetico en CT ya es practica estandar y resuelta?**
Respuesta: **es practica extendida, pero explicitamente NO resuelta ni estandarizada**, y el
paper mismo lo dice. El gap de la tesis no se cierra; se reencuadra.
- A favor de "es practica comun": "Many deep learning-based MAR studies rely on numerical
  simulations, where metal artifacts are synthetically introduced into randomly selected clinical
  CT images" (Sec. 1, p. 2). Y funciona para transferir: "methods trained with simulated metal
  artifacts generally can be applied directly to data with real metal objects" (Sec. 3.3, p. 15).
- Contra "esta resuelto", cuatro evidencias:
  (a) Falta de estandarizacion: "The simulation settings—such as geometry and metal
      properties—vary across studies" (Sec. 1, p. 2).
  (b) El simulador fisico falla justo en el regimen de implantes grandes: "the metal trace in the
      training sinogram generated by the XCIST simulator may look distorted ... for large metal
      objects with diameters larger than 3.0 cm" (Sec. 4, p. 16), con "274 were affected" de
      14 000 (Sec. 4, p. 16).
  (c) La colocacion realista no esta automatizada: en entrenamiento el metal va "in random soft
      tissue or bone locations" (Sec. 2.2, p. 5) y solo se logra realismo anatomico cuando
      "metal objects were manually designed and positioned" (Sec. 2.3, p. 6).
  (d) El realismo del artefacto queda como condicion no verificada: "if the simulated artifacts
      are shown to be very realistic" (Sec. 3.3, p. 15).
- Matiz importante para la redaccion de la tesis: este paper insertar metal sintetico lo hace
  para entrenar MAR (quitar artefacto), no para aumentacion de datos de segmentacion osea. No
  se encontro ningun uso de metal sintetico como aumentacion para segmentacion:
  **NO ENCONTRADO EN EL PDF**.

**8. Nivel que sostiene la evidencia: NIVEL 2.** Confirma y parametriza el baseline XCIST/CatSim
y aporta umbrales citables (150 HU, +250 HU, escala 0–4, NMAR=2), pero no evalua sintesis de
implantes ni segmentacion osea peri-implante, asi que ningun resultado de la tesis se cae si
este paper se lee mal; solo cambia como se redacta el baseline y como se justifican las metricas.

Observacion adicional para la autora (no altera el nivel): el 5to lugar del reto usa "Latent
Diffusion model, Attention UNet" (Tabla 1, p. 13). Es difusion latente aplicada a MAR, direccion
inversa a la de la tesis, pero conviene que la redaccion no de a entender que la difusion latente
es inedita en el dominio de artefactos metalicos en CT.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| Ref. 2 — Nils P, Haneda E, Zhang J, et al. "A hybrid training database and evaluation benchmark for assessing metal artifact reduction methods for imaging and therapy." Med Phys. 2025. doi:10.1002/mp.70020 | Fuente original de TODAS las definiciones de metricas y umbrales que este paper solo resume; ya esta en refs.bib como peters2025hybrid, confirma su rol de protocolo de validacion. |
| Ref. 1 — Gjesteby L, De Man B, Jin Y, et al. "Metal artifact reduction in CT: where are we after four decades?" IEEE Access. 2016;4:5826-5849 | Define las categorias de severidad de artefacto usadas para armar los 29 casos ("all categories of artifacts from minor shading to substantial degradation, as defined by Gjesteby et al."); escala citable para clasificar severidad. |
| Ref. 44 — AAPM CT Metal Artifact Reduction (CT-MAR) Grand Challenge Scoring Metrics. GitHub, AAPM_datachallenge/scoring_metric.md | Definiciones matematicas y umbrales operativos de las ocho metricas; fuente directa si se quiere reusar bone integrity o metal integrity. |
| Ref. 38 — AAPM CT Metal Artifact Reduction (CT-MAR) grand challenge benchmark tool. GitHub xcist/example/tree/main/AAPM_datachallenge | Herramienta de scoring y rutina FBP/reproyeccion 2D en Python; podria validar la reimplementacion de XCIST del alcance COMPLETO. |
| Ref. 49 — Wang Z, Bovik AC, Sheikh HR, Simoncelli EP. "Image quality assessment: from error visibility to structural similarity." IEEE Trans Image Process. 2004;13(4):600-612 | Implementacion concreta de SSIM adoptada por el benchmark; necesaria si se reporta SSIM comparable. |
| Ref. 45 — Fan Y, Pack J, De Man B. "A virtual imaging trial framework to study cardiac CT blooming artifacts." SPIE 2022 | Fuente del "spatial frequency boosting" aplicado a las imagenes clinicas antes de simular; paso de preprocesamiento que la tesis tendria que replicar o justificar omitir. |
| Ref. 61 — Fan F, Ritschl L, Beister M, et al. "Simulation-driven training of vision transformers enables metal artifact reduction of highly truncated CBCT scans." Med Phys. 2021;51(5):3360-3375 | Entrenamiento guiado por simulacion de artefacto metalico; compite conceptualmente con el renderizador y con el supuesto de transferencia sim-a-real. |
| Ref. 42 — Yan K, Wang X, Lu L, Summers RM. DeepLesion. J Med Imaging. 2018;5(3):1 | Dataset base de las 12 227 imagenes body incluida pelvis; alternativa o complemento a CTPelvic1K para el brazo de comparacion. |
| Ref. 32 — Moon SG, Hong SH, Choi JY, et al. "Metal artifact reduction by the alteration of technical factors in multidetector computed tomography: a 3-dimensional quantitative assessment." J Comput Assist Tomogr. 2008;32(4):630-633 | Cuantificacion 3D de severidad de artefacto metalico; posible metrica alternativa a SAP. |
| Ref. 33 — Stradiotti P, Curti A, Castellazzi G, Zerbi A. "Metal-related artifacts in instrumented spine. Techniques for reducing artifacts in CT and MRI: state of the art." Eur Spine J. 2009 | Artefacto de instrumentacion de osteosintesis (tornillos/barras) en columna; lo mas cercano al escenario clinico de la tesis dentro de las referencias de este paper. |
| Ref. 7 — Meyer E, Raupach R, Lell M, Schmidt B, Kachelriess M. "Normalized metal artifact reduction (NMAR) in computed tomography." Med Phys. 2010;37(10):5482-5493 | Metodo de referencia contra el que se calibro toda la escala 0–4 (NMAR = 2); imprescindible si la tesis adopta esa escala. |
| Ref. 55 — Park HS, Seo JK, Jeon K. "Implicit neural representation-based method for metal-induced beam hardening artifact reduction in X-ray CT imaging." Med Phys. 2025;52(4):2201-2211 | Metodo del 2do lugar; representacion implicita como alternativa no generativa al renderizador. |
| Ref. 16 — Wang H, Li Y, He N, Ma K, Meng D, Zheng Y. "DICDNet: deep interpretable convolutional dictionary network for metal artifact reduction in CT images." IEEE Trans Med Imaging. 2022;41(4):869-880 | Componente del 3er lugar y metodo image-domain de referencia repetidamente citado; baseline plausible. |

---

Nota de cumplimiento: no se edito ningun otro archivo del repositorio.
