# peters2025hybrid — Base de datos hibrida y benchmark de evaluacion para MAR en CT

- **DOI / URL:** 10.1002/mp.70020 (Med Phys. 2025;52:e70020)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/peters2025hybrid.pdf

**Actualización de uso, 2026-09-07:** N1 confirmado como protocolo híbrido adoptado
del brazo físico. Su elección no equivale a validación propia de síntesis 3D.
La equivalencia automática entre bone/metal integrity y BFC/ISC propuesta más abajo
queda cuestionada por #16: son antecedentes que requieren adaptación, no definiciones
ya aprobadas de esas métricas. La implementación y validación siguen abiertas en #17.

Profundidad: texto completo (12 paginas). Los Supplements S1-S3 se citan en el PDF pero no
estan incluidos en el archivo leido.

## Que hace (3 lineas maximo)
Calibra y valida la simulacion de artefactos metalicos de CatSim/XCIST contra un fantoma fisico,
y con ella genera 14 000 casos de entrenamiento hibridos (CT clinica + metal virtual) con pares
con/sin metal. Define ademas un benchmark de scoring de MAR con ocho metricas y 29 escenarios
clinicos, base de la AAPM CT-MAR Grand Challenge.

## Restriccion o supuesto clave
El supuesto explicito que rompe cualquier uso como generador de implantes anatomicamente
plausibles es la colocacion aleatoria: "the location of the metal objects in the training dataset
was randomized to enable the creation of a large dataset" y "Ideally, virtual metals would be
placed only in realistic locations, but this was not done since manual metal placement was
impractical" (Discussion, p. 9). Segundo supuesto: "all simulations are limited to the insertion
of metal objects. Concomitant anatomical changes due to surgery, such as swelling, bone ablation
or drilled holes within the patient cannot be covered" (Discussion, p. 9). Tercero: todo es 2D,
"the training database only covers two-dimensional MAR developments" (Discussion, p. 9).

## Que toco de aqui
- [x] metodo que reimplemento (definiciones de bone integrity y metal integrity como base de BFC/ISC)
- [x] numero que cito (umbrales 150 HU y 250 HU, escala 0-4, calibracion NMAR = 2, <2% de desviacion)
- [x] baseline de comparacion (simulacion fisica XCIST/CatSim; NMAR y DDPM-MAR como referencias de score)
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Desviacion simulacion vs real < 2% | "the simulated mean deviated by less than 2% from the experimentally obtained scans" | 3.1, p. 6 |
| Ruido: desviacion < 10%, hasta 13.3% | "the noise level ... deviated by less than 10%" ; "up to 13.3% in Exp 4" | 3.1, p. 6 |
| 14 000 casos simulados | "A total of 14,000 training cases were simulated" | 2.3, p. 4 |
| 12 374 cortes pelvis+torax (DeepLesion) | "A total of 12,374 clinical CT slices in the pelvis and thorax region" | 2.3, p. 3 |
| 1626 cortes de cabeza (UCLH Stroke EIT) | "as well as 1626 slices in the head region from the UCLH Stroke EIT database" | 2.3, p. 3 |
| 29 escenarios clinicos en el benchmark | "The scoring benchmark dataset contains a total of 29 clinical scenarios" | 2.4, p. 4 |
| Escala de score 0 a 4.0 | "a score from 0 (no relevant differences relative to ground truth) to 4.0" | 2.5, p. 5 |
| NMAR calibrado a score 2 | "assigning a score of 2 ... to the popular NMAR algorithm" | 2.5, p. 5 |
| Umbral de hueso 150 HU | "All voxels with a CT number above 150 HU ... are considered bone" | 2.5, p. 5 |
| Margen de metal 250 HU | "plus an empirically determined margin of 250 HU to increase stability" | 2.5, p. 6 |
| Sharpness: percentil 90 del gradiente | "quantified as the 90th percentile gradient magnitude value to minimize the influence of outliers" | 2.5, p. 5 |
| Gradientes de referencia >30 HU y >150 HU | "corresponds to a gradient of >30 HU, whereas for soft tissue & bone ... >150 HU" | 2.5, p. 5 |
| Blur de calibracion de sharpness | "a score of 1-4 corresponding to an image with a Gaussian blur of 0.4, 0.5, 0.75 and 1" | 2.5, p. 5 |
| Ruido: 0 = sin metal, 4 = ~2x | "the noise present in scans without any metal (score 0) to roughly 2x the ground truth noise (score 4)" | 2.5, p. 5 |
| Streak: 5% superior e inferior | "the average over the highest and lowest 5% CT number deviation to ground truth" | 2.5, p. 5 |
| SSIM con rango de datos 5000 HU | "with the data range set to 5000 HU" | 2.5, p. 5 |
| Rango de protones: 2% = score 4 | "linearly increasing to a score of 4 for a range shift of 2%" | 2.5, p. 6 |
| Hasta 5 objetos metalicos por caso | "Up to five virtual metal objects were then inserted in random soft tissue or bone positions" | 2.3, p. 4 |
| Diametro efectivo d = 2 sqrt(A/pi) | "An effective diameter d (in voxels) was computed ... as d = 2 sqrt(A/pi)" | 2.3, p. 4 |
| Perturbacion fractal ±0.67 | "perturbed with a random gain (sampled within ±0.67 times the respective edge length)" | 2.3, p. 4 |
| 120 kVp, 500 mA (generacion) | "an X-ray tube voltage of 120 kVp and a tube current of 500 mA" | 2.3, p. 4 |
| FOV 400 mm (pelvis/torax), 221.6 mm (cabeza) | "field of views were set to 400 mm for the pelvis and thorax datasets and 221.6 mm for the head" | 2.3, p. 4 |
| Imagenes de 256 x 256 | "The resulting metal masks were binary images of size 256 x 256" | 2.3, p. 4 |
| Geometria vendor-neutral 550/950 mm | "a source-to-iso distance of 550 mm and a source-to-detector distance of 950 mm" | 2.1, p. 3 |
| Lightspeed VCT 541/949 mm, 984 vistas | "a source-to-iso distance of 541 mm and a source-to-detector distance of 949 mm were chosen, 984 views" | 2.1, p. 2 |
| Tabla 2: implante de cadera 10-50 mm, 1-2 objetos | Tabla 2, fila "Hip implant (40%) / Titanium or cobalt / 10-50 mm / 1-2" | Tabla 2, p. 4 |
| Tabla 2: implante espinal 2.5-10 mm, 2-4 objetos | Tabla 2, fila "Spinal implant (40%) / Stainless steel / 2.5-10 mm / 2-4" | Tabla 2, p. 4 |
| Tabla 2: marcador fiducial 1-4 mm, oro | Tabla 2, fila "Fiducial marker (20%) / Gold / 1-2 mm (20%) 2-4 mm (80%)" | Tabla 2, p. 4 |
| Tabla 3: bone integrity NMAR/DDPM caso 1 | Tabla 3, "Bone integrity 1.96/0.89" (Caso 1, gold markers) | Tabla 3, p. 8 |
| Tabla 3: metal integrity NMAR/DDPM caso 1 | Tabla 3, "Metal integrity 2.06/1.92" (Caso 1, gold markers) | Tabla 3, p. 8 |
| Tabla 3: overall score caso 1 | Tabla 3, "Overall score 1.78/1.24" | Tabla 3, p. 8 |
| DDPM: 250 pasos de difusion | "repeated for a total of 250 diffusion steps until the final corrected sinogram is obtained" | 2.6, p. 6 |

## Donde entra en mi tesis
- Objetivo de metricas: es la fuente primaria (no `haneda2025aapm`) de las definiciones de las
  ocho metricas del benchmark AAPM. **Bone integrity** (umbral 150 HU + SDC + cambio de volumen)
  es el antecedente directo de BFC; **metal integrity** (umbral max-HU-en-ROI + 250 HU) lo es de ISC.
- Objetivo de renderizado: XCIST/CatSim como baseline fisico, con su validacion cuantitativa
  (<2% de desviacion en numero CT) como referencia del nivel de realismo exigible.
- Justificacion de novedad del muestreador: la colocacion aleatoria declarada explicitamente como
  limitacion ("manual metal placement was impractical") es el hueco que SAP viene a llenar.
- Datos: comparte region pelvica (DeepLesion) pero no usa CTPelvic1K ni segmentacion osea downstream.

## Dudas para el asesor
1. Bone integrity y metal integrity estan definidas como *scores* relativos a un ground truth sin
   metal. BFC e ISC en la tesis miden plausibilidad de una imagen *con* metal sintetizado. Adoptamos
   los umbrales (150 HU / +250 HU) pero redefinimos la comparacion, o buscamos otra base?
2. La escala 0-4 esta calibrada con NMAR = 2. Para la tesis no hay un algoritmo de referencia
   equivalente que ancle el 2. Fijamos el ancla con XCIST, o abandonamos la escala 0-4?
3. El benchmark no incluye osteosintesis pelvica (tornillos iliosacros, placas acetabulares).
   Eso hace que las metricas sean transferibles pero no los escenarios. Se documenta como gap?
4. El paper valida realismo en fantoma fisico, no en paciente. Podemos replicar algo asi sin
   fantoma, o el realismo del renderizador se valida solo con lector experto?

## Evidencia textual

| Item | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| Simulador usado | "modelled in the CatSim CT simulator within the open-access toolkit XCIST" | Abstract, p. 1 |
| Todo en 2D | "Since most MAR research is performed in 2D, all datasets are simulated in 2D" | Abstract, p. 1 |
| Validacion experimental | "metal artifact simulation capability is experimentally validated in CT phantom scans" | Abstract, p. 1 |
| Acuerdo cuantitativo | "the mean CT number deviation between simulation and real data was less than 2%" | Abstract / Results, p. 1 |
| Total de escenarios | "In total, 14,000 metal scenarios in the head, thorax and pelvis regions were simulated" | Abstract, p. 1 |
| Familias de metricas | "CT number accuracy, noise, image sharpness, streak amplitude, structural integrity, and the effect on range" | Abstract, p. 1 |
| Rango de metales | "small metal implants such as fiducial markers up to large metal implants such as hip replacements" | Abstract, p. 1 |
| Disponibilidad publica | "Both the simulation tools and the benchmark with the test cases were made publicly available" | Abstract, p. 1 |
| Reclamo de primicia | "This is the first comprehensive evaluation benchmark covering a large number of clinically realistic metal artifact scenarios" | Conclusions, p. 1 |
| Falta de benchmark previo | "there is no universally accepted evaluation benchmark and by necessity every study uses its own custom evaluation" | 1 Introduction, p. 2 |
| Falta de ground truth clinico | "The evaluation of metal artifacts is particularly hampered by the absence of a reliable ground truth" | 1 Introduction, p. 2 |
| Evaluacion clinica actual | "Analysis in real patient data is typically limited to a time-consuming visual evaluation" | 1 Introduction, p. 2 |
| Escaner modelado | "we used a 64-row CT scanner, the Lightspeed VCT scanner (GE HealthCare, Chicago, IL, USA)" | 2.1, p. 2 |
| Geometria Lightspeed | "source-to-iso distance of 541 mm and a source-to-detector distance of 949 mm ... 984 views" | 2.1, p. 2 |
| Detector Lightspeed | "888 detector columns (1.0239 mm pitch), 64 detector rows (pitch 1.09 mm)" | 2.1, p. 2 |
| Crosstalk | "Crosstalk between columns/rows was set to 2.5%/2% for X-ray photons, and 4%/4.5% for optical photons" | 2.1, p. 2 |
| Flujo de fotones | "a flux density of 2 * 10^6 photons/mA/mm^2/s at 1 m distance" | 2.1, p. 2 |
| Ruido electronico | "an electronic noise equivalent to 2.98 X-ray photons, and a detector gain factor of 0.1 electrons per keV" | 2.1, p. 2 |
| Rejilla antidispersion | "an anti-scatter grid with an aspect ratio of 9.8, resulting in a scatter kernel width of 49 detector columns" | 2.1, p. 2 |
| Correccion de senal negativa | "any negative values ... are replaced by values obtained from a one-dimensional 3-tap [0.5, 0, 0.5] filter convolution" | 2.1, p. 3 |
| Umbral de starvation | "any values x below e^(-13) ... are replaced by e^(-13) * (1 + 50x)" | 2.1, p. 3 |
| Filtros de correccion de ruido | "7-tap [-1/7, -1/7, -1/7, 6/7, -1/7, -1/7, -1/7] and one-dimensional 5-tap [-1/16, -1/4, 5/8, -1/4, -1/16]" | 2.1, p. 3 |
| Geometria vendor-neutral | "a source-to-iso distance of 550 mm and a source-to-detector distance of 950 mm" | 2.1, p. 3 |
| Foco y detector | "focal spot ... set to 1 x 1 mm, detector cell size was 1 x 1 mm with a 90% fill factor" | 2.1, p. 3 |
| Muestreo | "1 detector row with 900 columns was simulated, with a total of 1000 views" | 2.1, p. 3 |
| Espectro y submuestras | "source spectrum was sampled at 12 energies ... total of eight subsamples (2 x 2 x 2)" | 2.1, p. 3 |
| Reconstruccion | "The popular filtered back projection by Feldkamp, Davis & Kress algorithm (FDK) was used" | 2.1, p. 3 |
| Fantoma de validacion | "a CIRS tissue equivalent thorax phantom ... comprising cortical and trabecular bone, spinal cord, and plastic water" | 2.2, p. 3 |
| Metal central | "In the central position, stainless steel (density 8.00 g/cm3, diameter 12.70 mm) was used" | 2.2, p. 3 |
| Metales perifericos | "stainless steel (12.35 mm), aluminum (density 2.70 g/cm3, 7.90 mm), titanium-zirconium-molybdenum (TZM) alloy" | 2.2, p. 3 |
| TZM y cobre | "(TZM) alloy (density 10.22 g/cm3, 11.92 mm) and copper (density 8.96 g/cm3, 6.30 mm)" | 2.2, p. 3 |
| Protocolo de escaneo | "scanned with a 1.0-second rotation, a tube voltage of 120 kVp, a tube current of 500 mA" | 2.2, p. 3 |
| FOV del fantoma | "a large body bowtie filter, a field of view of 400 mm, and a standard reconstruction kernel" | 2.2, p. 3 |
| Configuraciones | "Four different metal configurations were scanned (Figure 1 and Table 1)" | 2.2, p. 3 |
| Fantoma cardiaco | "solid metal rods (32 mm molybdenum, 25 mm TZM and 25 mm Al) in a cardiac phantom" | 2.2, p. 3 |
| Marco hibrido | "A hybrid data simulation framework was used ... combining clinical CT scans with virtual metal objects" | 2.3, p. 3 |
| Fuente clinica pelvis/torax | "12,374 clinical CT slices in the pelvis and thorax region were collected from the NIH DeepLesion database" | 2.3, p. 3 |
| Fuente clinica cabeza | "1626 slices in the head region from the UCLH Stroke EIT database" | 2.3, p. 3 |
| Filtro de realce previo | "we compensated for this by applying a frequency boosting filter prior to the CT simulation" | 2.3, p. 3 |
| Construccion del filtro | "resulting 1D frequency-boosting filter was then assigned radially across all Fourier angles" | 2.3, p. 3 |
| Geometrias metalicas | "random fractal shapes were generated ... allowed for a larger variation of the metal geometry" | 2.3, p. 4 |
| Semilla hexagonal | "a hexagonal shape was initialized and its midpoints along each edge were perturbed with a random gain" | 2.3, p. 4 |
| Criterio de parada | "repeated until the length of each edge falls below one voxel" | 2.3, p. 4 |
| COLOCACION (clave) | "Up to five virtual metal objects were then inserted in random soft tissue or bone positions" | 2.3, p. 4 |
| Materiales por region | "within the CT scans with different material types and diameters (Table 2)" | 2.3, p. 4 |
| Contenido de cada caso | "each containing a sinogram with and without metal, the respective reconstructions, and a metal-only mask" | 2.3, p. 4 |
| Categorias de artefacto | "Gjesteby et al. categorized metal artifacts based on the metal object size and composition" | 2.4, p. 4 |
| Rango de categorias | "images ranging from only minor shading (category I) to thick bright/dark bands obliterating substantial parts" | 2.4, p. 4 |
| Escenarios del benchmark | "a total of 29 clinical scenarios, covering all categories in the clinically most relevant metal scenarios" | 2.4, p. 4 |
| Tamanos cubiertos | "small-sized metal objects (surgical clips, fiducial marker seeds, and dental fillings), medium-sized objects" | 2.4, p. 4 |
| Objetos grandes | "up to large, full joint replacements (shoulder and hip)" | 2.4, p. 4 |
| Peso de lo dental | "about half the scenarios concern dental work" | 2.4, p. 4 |
| Orientacion del metal | "matched with masks obtained from clinical CT scans with the clinical MAR applied to determine a realistic metal object orientation" | 2.4, p. 4 |
| Fuente de pacientes del benchmark | "Patient datasets were selected from the Massachusetts General Hospital (MGH) clinical database" | 2.4, p. 4 |
| Aprobacion etica | "institutional review board approval no. 2022P000798" | 2.4, p. 4 |
| ROI de calculo | "Metrics are calculated within a region of interest (ROI) covering the patient and the CT couch" | 2.5, p. 5 |
| Exclusiones del ROI | "excluding the surrounding air as well as the metal object itself and adjacent voxels" | 2.5, p. 5 |
| Escala de puntaje | "a score from 0 (no relevant differences relative to ground truth) to 4.0 (no improvement over uncorrected image)" | 2.5, p. 5 |
| Calibracion con NMAR | "the scoring is calibrated by assigning a score of 2 ... to the popular NMAR algorithm" | 2.5, p. 5 |
| Score global | "The overall score was then calculated as the unweighted mean of all individual scores" | 2.5, p. 5 |
| Codigo de scoring | "A python version of the benchmark tool is made available via GitHub [https://github.com/xcist/example/tree/main/AAPM_datachallenge/]" | 2.5, p. 5 |
| Metrica 1: CT number accuracy | "assessed as the voxel-wise root-mean square error (RMSE) between the ground truth and the MAR image" | 2.5, p. 5 |
| Formula RMSE | "RMSE = sqrt( sum_N |CTN_gt - CTN_MAR|^2 / N )" (Ec. 1) | 2.5, p. 5 |
| Motivo del RMSE | "to avoid errors from light and dark streaks canceling each other out" | 2.5, p. 5 |
| Metrica 2: Noise | "the standard deviation within a circular ROI in homogenous soft tissue that is least affected" | 2.5, p. 5 |
| Escala de Noise | "a linear increase from the ground truth noise ... to roughly 2x the ground truth noise (score 4)" | 2.5, p. 5 |
| Metrica 3: Sharpness | "assessed via the preservation of gradients. A Sobel filter is applied to ROIs containing sharp gradients" | 2.5, p. 5 |
| Tejidos del gradiente | "(soft tissue & bone or soft & adipose tissue) to determine the absolute gradient magnitude" | 2.5, p. 5 |
| Umbral de gradiente blando | "For soft tissue and adipose, this corresponds to a gradient of >30 HU" | 2.5, p. 5 |
| Umbral de gradiente oseo | "for soft tissue & bone this corresponds to a gradient of > 150 HU between the respective tissues" | 2.5, p. 5 |
| Cuantificacion de sharpness | "quantified as the 90th percentile gradient magnitude value ... then averaged over the two gradient types" | 2.5, p. 5 |
| Calibracion de sharpness | "score of 0 corresponding to an unaltered image, and a score of 1-4 ... Gaussian blur of 0.4, 0.5, 0.75 and 1" | 2.5, p. 5 |
| Metrica 4: Streak | "assessed within ROIs perpendicular to strong streak artifacts in the uncorrected images" | 2.5, p. 5 |
| Calculo de streak | "the average over the highest and lowest 5% CT number deviation to ground truth in each ROI is calculated" | 2.5, p. 5 |
| Definicion final de streak | "The remaining streak amplitude is then defined as the difference between the two" | 2.5, p. 5 |
| Metrica 5: Structural integrity | "quantified using the structural similarity index (SSIM) ... with the data range set to 5000 HU" | 2.5, p. 5 |
| Salida de SSIM | "supports both the calculation of the index and of a 2D SSIM map" | 2.5, p. 5 |
| Metrica 6: BONE INTEGRITY (definicion) | "All voxels with a CT number above 150 HU, excluding those in the metal ground truth geometry, are considered bone" | 2.5, p. 5 |
| Bone integrity, componentes | "assessed via the change of volume as well as with the Sorensen-Dice coefficient (SDC) between the NMAR and the ground truth image" | 2.5, pp. 5-6 |
| Formula SDC | "SDC = 2(X∩Y)/(X+Y) with X and Y as the cardinalities of the two masks" | 2.5, p. 6 |
| Agregacion de bone integrity | "The overall bone integrity score is then averaged over the volume and the SDC score" | 2.5, p. 6 |
| Metrica 7: METAL INTEGRITY (definicion) | "evaluated analogous to the bone integrity, comparing the metal mask obtained from the image to the documented ground truth" | 2.5, p. 6 |
| Umbral de metal integrity | "all voxels above the highest CT number within a ROI covering the metal ground truth and adjacent tissue" | 2.5, p. 6 |
| Margen de metal integrity | "plus an empirically determined margin of 250 HU to increase stability is considered metal" | 2.5, p. 6 |
| Metrica 8: Proton beam range | "CT numbers are translated into the tissues' different stopping power relative to water (SPR)" | 2.5, p. 6 |
| WET | "The SPR multiplied with the voxel size corresponds to the water-equivalent thickness (WET)" | 2.5, p. 6 |
| Escala de rango de protones | "a score of zero corresponds to no WET shift, linearly increasing to a score of 4 for a range shift of 2%" | 2.5, p. 6 |
| Curva CTN-a-SPR | "the clinically validated CTN-to-SPR translation curve from MGH is applied to the CT images" | 2.5, p. 6 |
| MAR de ejemplo (DDPM) | "employs a denoising diffusion probabilistic model (DDPM) that is unconditionally trained" | 2.6, p. 6 |
| Inpainting de sinograma | "the metal corrupted regions of the sinogram are treated as missing information" | 2.6, p. 6 |
| Pasos de difusion | "The iterative process is repeated for a total of 250 diffusion steps" | 2.6, p. 6 |
| Resampling | "a resampling approach similar to Lugmayr et al. is employed that involves alternating noising and denoising" | 2.6, p. 6 |
| Resultado de validacion | "Strong streak artifacts resulting from the metal inserts are well-replicated across all cases" | 3.1, p. 6 |
| Acuerdo en HU | "the simulated mean deviated by less than 2% from the experimentally obtained scans" | 3.1, p. 6 |
| Acuerdo en ruido | "the noise level (defined as 2SD) deviated by less than 10%" | 3.1, p. 6 |
| Discrepancia mayor en ruido | "larger discrepancies in noise were observed (up to 13.3% in Exp 4, Figure 3)" | 3.1, p. 6 |
| Sesgo residual | "The bias is attributable to remaining imperfections in the physics models used in the simulations" | 3.1, p. 6 |
| Juicio global de realismo | "Overall, the nature and the amplitude of the metal artifacts are well replicated" | 3.1, p. 6 |
| Contenido generado por caso | "a sinogram with metal, a label sinogram (no metals), a reconstructed image with metal, a label reconstructed image" | 3.2, p. 6 |
| Ejemplo pelvico | "Two stainless steel metals with 8.0 and 7.4 mm in effective diameter were inserted here" | 3.2, p. 6 |
| Ejemplo de cabeza | "two amalgam metals with 3.6 and 2.1 mm in effective diameter were inserted" | 3.3, p. 8 |
| Interpretacion de scores | "with the scoring correctly reflecting improvements relative to the uncorrected image (4.0)" | 3.3, p. 8 |
| LIMITACION: sin cambios anatomicos | "all simulations are limited to the insertion of metal objects" | 4 Discussion, p. 9 |
| LIMITACION: cirugia no modelada | "Concomitant anatomical changes due to surgery, such as swelling, bone ablation or drilled holes ... cannot be covered" | 4 Discussion, p. 9 |
| LIMITACION: alucinacion de features | "special attention must be paid regarding feature hallucination of such regions" | 4 Discussion, p. 9 |
| LIMITACION: sesgo vendor-neutral | "a vendor-neutral geometry was used ... potentially introducing a bias to algorithms trained on that data" | 4 Discussion, p. 9 |
| LIMITACION: desbalance cabeza/cuerpo | "the imbalance between head and body datasets, directly affecting the respective performance" | 4 Discussion, p. 9 |
| LIMITACION: extraccion 2D aleatoria | "obtained by randomly extracting 2-D slices from CT scans, which can potentially underrepresent views" | 4 Discussion, p. 9 |
| LIMITACION: COLOCACION ALEATORIA | "the location of the metal objects in the training dataset was randomized to enable the creation of a large dataset" | 4 Discussion, p. 9 |
| LIMITACION: colocacion realista no hecha | "Ideally, virtual metals would be placed only in realistic locations, but this was not done" | 4 Discussion, p. 9 |
| Razon de la limitacion | "since manual metal placement was impractical" | 4 Discussion, p. 9 |
| LIMITACION: solo 2D | "the training database only covers two-dimensional MAR developments" | 4 Discussion, p. 9 |
| Extension a 3D | "an application of the MAR benchmark to 3D is generally feasible, special attention will be needed" | 4 Discussion, p. 9 |
| Disparidad residual en fantoma | "certain dark shadows between lung and plastic water were exclusively present in empirical results" | 4 Discussion, p. 9 |
| Disparidad en varillas | "simulations displayed stronger streak artifacts near some rods" | 4 Discussion, p. 9 |
| Causa atribuida | "may be traced back to imperfections within the physics models employed or offsets of the detector or phantom" | 4 Discussion, p. 9 |
| Datos de entrenamiento publicos | "The training data are publicly available on the MAR Grand Challenge repositorium" | 4 Discussion, p. 9 |
| Colocacion "meaningful" en benchmark | "clinically representative patient datasets with virtual metals, such as dental fillings and hip prosthesis, inserted in meaningful locations" | 4 Discussion, p. 9 |
| Uso restringido del benchmark | "This scoring benchmark should not be used for parameter tuning but only for final evaluation and scoring" | 4 Discussion, p. 9 |
| LIMITACION: ROIs sin MAR | "ROI for noise and streak amplitude were placed in regions without or with artifacts, based on the images without MAR" | 4 Discussion, p. 10 |
| LIMITACION: umbrales empiricos | "Metal and bone integrity metrics depend on the empirically determined threshold values for the respective materials" | 4 Discussion, p. 10 |
| LIMITACION: dependencia de kVp | "may vary for images acquired with other tube voltages" | 4 Discussion, p. 10 |
| LIMITACION: sin metrica de lesiones | "no dedicated metric for the detection of small imaging features ... was included" | 4 Discussion, p. 10 |
| Gold standard clinico | "visual inspection by experienced physicians remains the gold standard" | 4 Discussion, p. 10 |
| LIMITACION: solo single-energy | "the presented results and algorithms focus on single-energy CT data as the current clinical standard" | 4 Discussion, p. 10 |
| Modelo unico para todo el cuerpo | "the dataset was formed to train a single model in all body parts" | 4 Discussion, p. 10 |
| Financiamiento | "supported by the NIH/NIBIB grant R01EB031102" | Acknowledgments, p. 10 |
| Conflicto de interes | "The authors have no relevant conflicts of interest to disclose" | COI, p. 10 |
| Licencia de datos/codigo | NO ENCONTRADO EN EL PDF | — |
| Numero de version del toolkit | NO ENCONTRADO EN EL PDF | — |
| Metrica cuantitativa de realismo de tipo perceptual (FID, lectura humana) | NO ENCONTRADO EN EL PDF | — |
| Casos de osteosintesis pelvica (tornillos iliosacros, placas acetabulares) | NO ENCONTRADO EN EL PDF | — |
| Dice o HD95 de segmentacion osea downstream | NO ENCONTRADO EN EL PDF | — |

## Verificacion de nivel

**1. CRITICO — Definiciones matematicas de las ocho metricas.**
Parcialmente. Solo hay **dos formulas explicitas numeradas o inline**: RMSE (Ec. 1) y SDC. Las otras
seis se definen en prosa con procedimiento y umbrales concretos (suficiente para reimplementar, pero
sin formula cerrada). Las ocho metricas son: CT number accuracy, noise, image sharpness, streak
amplitude, structural integrity, bone integrity, metal integrity, proton beam range.

Definicion integra de **bone integrity** (Seccion 2.5, pp. 5-6):
"All voxels with a CT number above 150 HU, excluding those in the metal ground truth geometry, are
considered bone. Bone integrity is assessed via the change of volume as well as with the
Sorensen-Dice coefficient (SDC) between the NMAR to the ground truth image. The SDC = 2(X∩Y)/(X+Y)
with X and Y as the cardinalities of the two masks there quantifies the similarity of the two sets.
The overall bone integrity score is then averaged over the volume and the SDC score."

Definicion integra de **metal integrity** (Seccion 2.5, p. 6):
"Metal integrity is evaluated analogous to the bone integrity, comparing the metal mask obtained
from the image to the documented ground truth. For this, all voxels above the highest CT number
within a ROI covering the metal ground truth and adjacent tissue plus an empirically determined
margin of 250 HU to increase stability is considered metal."

Observaciones para la tesis:
- Ninguna de las dos da la formula del *mapeo a la escala 0-4*: se dice solo que "the scoring is
  calibrated by assigning a score of 2 ... to the popular NMAR algorithm" (2.5, p. 5). La funcion de
  transferencia exacta no aparece en el PDF; habria que leerla del codigo en GitHub.
- Bone integrity mezcla dos sub-scores (cambio de volumen y SDC) con promedio simple no ponderado.
  El "cambio de volumen" no se formula (no se dice si es absoluto, relativo o con signo):
  NO ENCONTRADO EN EL PDF.
- El umbral de metal integrity es *adaptativo por ROI* (max HU en el ROI + 250 HU), no un umbral fijo.
  Esto importa: ISC no puede usar "250 HU" como umbral absoluto.

**2. CRITICO — Construccion de la base hibrida y colocacion.**
Simulador: CatSim dentro de XCIST ("modelled in the CatSim CT simulator within the open-access
toolkit XCIST", Abstract p. 1). CT clinicas: NIH DeepLesion (12 374 cortes pelvis/torax) y UCLH
Stroke EIT (1626 cortes de cabeza) (2.3, p. 3). Geometrias: fractales aleatorios a partir de un
hexagono con perturbacion ±0.67 de la longitud de arista (2.3, p. 4).

Colocacion — frase clave (2.3, p. 4):
"Up to five virtual metal objects were then inserted in **random soft tissue or bone positions**
within the CT scans with different material types and diameters."

Confirmado y ampliado en Discussion (p. 9):
"the location of the metal objects in the training dataset was **randomized** to enable the creation
of a large dataset. Ideally, virtual metals would be placed only in realistic locations, but this
was not done since **manual metal placement was impractical**."

Matiz importante: la colocacion aleatoria aplica al **dataset de entrenamiento (14 000 casos)**.
El **benchmark de scoring (29 escenarios)** si usa colocacion manual/realista: "clinically
representative patient datasets with virtual metals ... inserted in **meaningful locations**"
(Discussion, p. 9) y "matched with masks obtained from clinical CT scans with the clinical MAR
applied to determine a **realistic metal object orientation**" (2.4, p. 4). El PDF no describe
regla anatomica alguna ni criterio cuantitativo para "meaningful"; es colocacion manual experta.

**Lectura para la tesis:** es evidencia fuerte a favor del reclamo de novedad. El trabajo mas
reciente y completo del area declara por escrito que la colocacion anatomicamente plausible a escala
es impracticable manualmente y por eso la abandona. Un muestreador que produzca poses de una
distribucion clinica de malposiciones es exactamente el componente ausente. Ademas, tampoco modelan
los cambios anatomicos de la cirugia ("bone ablation or drilled holes ... cannot be covered",
Discussion p. 9), lo que refuerza el hueco donde entran BFC y la contencion cortical.

**3. Casos pelvicos y osteosintesis.**
Pelvis SI, como region de imagen: "12,374 clinical CT slices in the pelvis and thorax region were
collected from the NIH DeepLesion database" (2.3, p. 3); reconstruccion "400 mm for the pelvis and
thorax datasets" (2.3, p. 4); Figura 5a muestra un caso pelvico con marcadores de oro.

Metal en pelvis: solo **protesis de cadera**. Tabla 2 (p. 4): "Hip implant (40%) / Titanium or
cobalt / 10-50 mm / 1-2". Figura 2 (p. 5): "Prosthetic hips (Ti, n=3, cat V)".

Osteosintesis: SI, pero **espinal y de tejido blando, no pelvica**. Figura 2 (p. 5) lista:
"Spinal screws (Ti, n=2, cat III)", "Spinal rods (Ti, n=2, cat II)", "Large spinal reconstruction
(Ti, n=2, cat IV)", "Surgical clips (titanium, n=1, cat. I)". Tabla 2 (p. 4): "Spinal implant (40%)
/ Stainless steel / 2.5-10 mm / 2-4".

**Tornillos iliosacros, placas acetabulares o cualquier osteosintesis del anillo pelvico:
NO ENCONTRADO EN EL PDF.** Este es el gap concreto que la tesis ocupa: el benchmark cubre el
material (titanio, acero) y la region (pelvis), pero no la combinacion tornillo/placa en pelvis.

**4. Validacion del realismo de los artefactos.**
Es **cuantitativa y fisica**, contra un fantoma escaneado, no acuerdo visual ni metrica perceptual.
Frases literales:
- "the metal artifact simulation capability is experimentally validated in CT phantom scans
  containing various metal types and -geometries" (Abstract, p. 1).
- "Within specified regions of interest, the mean CT number deviation between simulation and real
  data was less than 2%, making the simulation tool suitable for the aspired tasks" (Abstract, p. 1).
- "In regions without obvious metal artifacts, the noise level (defined as 2SD) deviated by less
  than 10%; however, in regions with obvious metal artifacts, larger discrepancies in noise were
  observed (up to 13.3% in Exp 4)" (3.1, p. 6).
- "Overall, the nature and the amplitude of the metal artifacts are well replicated" (3.1, p. 6).

O sea: dos criterios cuantitativos (desviacion de media HU en ROI, desviacion de ruido 2SD en ROI)
mas inspeccion de imagenes de diferencia (Figura 3). No hay FID, ni estudio de lectores, ni test de
discriminacion humano-vs-sintetico. **Metrica perceptual de realismo: NO ENCONTRADO EN EL PDF.**

Para la tesis: este es un protocolo replicable *si hay fantoma fisico*. Sin fantoma, la parte
transferible es la comparacion ROI-a-ROI de media HU y de 2SD entre regiones peri-implante
sintetizadas y regiones peri-implante reales de CLINIC-metal, con los umbrales <2% y <10% como
referencia de la literatura (no como criterio de aprobacion propio, porque el diseno experimental
es distinto).

**5. Disponibilidad publica.**
- Codigo de scoring: "A python version of the benchmark tool is made available via GitHub
  [https://github.com/xcist/example/tree/main/AAPM_datachallenge/]" (2.5, p. 5).
- Datos de entrenamiento: "The training data are publicly available on the MAR Grand Challenge
  repositorium" (Discussion, p. 9), ref. 55: "MAR Grand Challenge training dataset repositorium.
  Published 2024. https://rpi.box.com/s/7p8tkqj5ewhtdad2h8kx975i9qg6b7a4" (Referencias, p. 12).
- Proyeccion/reconstruccion: "one can use the forward projection and reconstruction code distributed
  via the XCIST GitHub website" (Discussion, p. 9), ref. 45.
- Reto: ref. 35, "CT Metal Artifact Reduction (CT-MAR): An AAPM Grand Challenge. Published 2024.
  https://www.aapm.org/GrandChallenge/CT-MAR/" (p. 11).
- **Licencia: NO ENCONTRADO EN EL PDF.** El PDF no nombra ninguna licencia para el codigo ni para
  los datos. Hay que verificarla en el repositorio antes de citar reutilizacion.

**6. Reusabilidad de las metricas para una imagen SINTETIZADA (analisis propio, no del paper).**
Estructura del problema: en el benchmark, el par es (ground truth sin metal, imagen MAR) y el score
crece con la *desviacion* respecto al ground truth sin metal. La tesis genera metal donde no lo
habia, asi que su par natural es (imagen original sin metal, imagen sintetizada con metal) y aqui la
desviacion **debe existir** dentro y alrededor del implante: no es error, es la senal buscada. La
inversion no es simetrica y hay que evaluar metrica por metrica.

| Metrica | Sobrevive a la inversion? | Razon |
|---|---|---|
| CT number accuracy (RMSE) | Solo fuera de la banda B_delta | Dentro de B_delta un RMSE alto es el objetivo, no un fallo. Reusable como *restriccion de no-alteracion* en el complemento de B_delta: RMSE ~ 0 lejos del implante. |
| Noise | SI, casi tal cual | Compara SD en ROI homogeneo. En la tesis: el ruido lejos del implante no debe cambiar, y cerca debe subir de forma consistente con lo real. La escala 0-4 no aplica; el estadistico si. |
| Image sharpness (Sobel, p90) | SI, invertida | Es una metrica de una sola imagen (no requiere ground truth para el estadistico, solo para la escala). Reusable para verificar que el renderizador no emborrona la interfaz hueso/tejido fuera del metal. Los umbrales >30 HU y >150 HU son directamente adoptables. |
| Streak amplitude | SI, esta es la mas util | Definida como diferencia entre el promedio del 5% superior y el 5% inferior de desviacion en ROIs perpendiculares al streak. Para la tesis: se compara la amplitud de streak sintetizada contra la distribucion de amplitudes medidas en CLINIC-metal real. Es un estadistico de realismo, no de correccion. |
| Structural integrity (SSIM) | Solo fuera de B_delta | Igual que RMSE: dentro de B_delta se espera SSIM bajo por diseno. |
| **Bone integrity** (150 HU + SDC + volumen) | **SI, con reinterpretacion — base de BFC** | El ground truth sin metal existe en la tesis (es el CT original). La mascara osea a 150 HU antes y despues de sintetizar debe coincidir salvo donde el implante ocupa hueso legitimamente. Un SDC bajo *fuera* del volumen del implante = hueso destruido o inventado = fallo del renderizador. Esto es exactamente BFC, pero medido como perdida de continuidad cortical en lugar de solidez del score 0-4. Nota critica: hay que excluir el volumen del implante del calculo, igual que el paper excluye "those in the metal ground truth geometry". |
| **Metal integrity** (max HU en ROI + 250 HU) | **SI, invertida — base de ISC** | En el paper: verifica que el MAR no borro ni deformo el metal. En la tesis: verifica que el metal *sintetizado* reproduce la geometria del implante del banco (la mascara CAD es el ground truth exacto, ventaja sobre el paper). SDC entre mascara umbralizada y mascara CAD. El umbral adaptativo por ROI se traslada sin cambio. Es la metrica que mejor sobrevive porque la tesis tiene ground truth geometrico perfecto. |
| Proton beam range (WET) | NO | Requiere plan de tratamiento con protones y la curva CTN-a-SPR de MGH. Fuera del alcance de segmentacion osea. |

Resumen: sobreviven **metal integrity** (casi directa, y con mejor ground truth que en el paper),
**bone integrity** (con exclusion del volumen del implante), **streak amplitude** (como comparacion
distribucional contra CLINIC-metal), **sharpness** y **noise** (como restricciones de no-degradacion).
RMSE y SSIM sobreviven solo restringidas al complemento de B_delta. Proton range no aplica.
Ninguna sobrevive con su escala 0-4 intacta, porque el ancla NMAR = 2 no tiene analogo en sintesis.

**7. Limitaciones declaradas.**
Sobre realismo de la simulacion (Discussion, p. 9):
- "all simulations are limited to the insertion of metal objects. Concomitant anatomical changes due
  to surgery, such as swelling, bone ablation or drilled holes within the patient cannot be covered."
- "This is especially relevant for the application of the data in deep learning-based MAR algorithms,
  where special attention must be paid regarding feature hallucination of such regions."
- "certain dark shadows between lung and plastic water were exclusively present in empirical results
  ... and simulations displayed stronger streak artifacts near some rods."
- "The former may stem from off-focal radiation while the latter may be traced back to imperfections
  within the physics models employed or offsets of the detector or phantom that are not entirely
  considered in simulation."
- "While those factors could be further refined in future work, they play a secondary role for the
  purpose of AI-based MAR training and MAR performance evaluation."

Sobre generalizacion del benchmark:
- "a vendor-neutral geometry was used for the metal simulation, potentially introducing a bias to
  algorithms trained on that data" (p. 9).
- "A second limitation is the imbalance between head and body datasets, directly affecting the
  respective performance" (p. 9).
- "the training database only covers two-dimensional MAR developments" (p. 9).
- "This scoring benchmark should not be used for parameter tuning but only for final evaluation and
  scoring of a new MAR approach" (p. 9).
- "Metal and bone integrity metrics depend on the empirically determined threshold values for the
  respective materials and may vary for images acquired with other tube voltages" (p. 10).
- "ROI for noise and streak amplitude were placed in regions without or with artifacts, based on the
  images without MAR, and thus may be impaired by artifacts introduced by the MAR itself" (p. 10).
- "no dedicated metric for the detection of small imaging features was included. For this, visual
  inspection by experienced physicians remains the gold standard" (p. 10).
- "the presented results and algorithms focus on single-energy CT data as the current clinical
  standard" (p. 10).

**8. Nivel que sostiene la evidencia: NIVEL 1, confirmado.**
Es la fuente primaria y unica de las definiciones y umbrales (150 HU, +250 HU, escala 0-4 anclada en
NMAR = 2, Sobel p90, streak 5%) sobre los que se construyen BFC e ISC, y ademas declara por escrito
la limitacion de colocacion aleatoria que sostiene el reclamo de novedad del muestreador: un error
de lectura aqui invalida a la vez las metricas propias y el argumento de gap.

Advertencia de nivel 1: el mapeo exacto de cada metrica a la escala 0-4 **no esta en el PDF** y solo
puede recuperarse del codigo en GitHub. Si la tesis va a citar la escala, hay que leer ese codigo o
citar solo el ancla NMAR = 2.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| 1. Gjesteby L, Man BDE, Jin Y, et al. Metal artifact reduction in CT: where are we after four decades? IEEE Access. 2016;4:5826-5849. doi:10.1109/ACCESS.2016.2608621 | Fuente original de la taxonomia de categorias I-V de artefacto metalico que estructura los 29 escenarios del benchmark. Si la tesis reporta cobertura de escenarios, la escala es de aqui, no de Peters. |
| 5. Meyer E, Raupach R, Lell M, Schmidt B, Kachelriess M. Normalized metal artifact reduction (NMAR) in computed tomography. Med Phys. 2010;37(10):5482-5493. doi:10.1118/1.3484490 | Es el ancla numerica de toda la escala 0-4 (NMAR = 2). Sin este paper la escala no es interpretable. Tambien es el baseline analitico contra el que se compara el DDPM. |
| 16. Karageorgos G, Zhang J, Peters N, et al. A denoising diffusion probabilistic model for metal artifact reduction in CT. IEEE Trans Med Imaging. 2024;43:3521-3532. doi:10.1109/TMI.2024.3416398 | Metodo de difusion que compite conceptualmente con el renderizador de la tesis (difusion sobre CT con metal), aunque en direccion inversa (corrige en vez de generar). Ya esta en papers/ como karageorgos2024ddpm. |
| 34. Wu M, Fitzgerald P, Zhang J, et al. XCIST—an open access x-ray/CT simulation toolkit. Phys Med Biol. 2022;67(19). doi:10.1088/1361-6560/ac9174 | Herramienta del baseline fisico de la tesis. Ya esta en papers/ como wu2022xcist. |
| 35. CT Metal Artifact Reduction (CT-MAR): An AAPM Grand Challenge. Published 2024. https://www.aapm.org/GrandChallenge/CT-MAR/ | Fuente institucional del reto y de la definicion oficial de las metricas; complementa haneda2025aapm. |
| 36. De Man B, Basu S, Chandra N, et al. CatSim: a new computer assisted tomography simulation environment. 2007:65102G | Fuente original del simulador. Necesaria si la tesis describe el modelo fisico del baseline. |
| 43. Yan K, Wang X, Lu L, Summers RM. DeepLesion: automated mining of large-scale lesion annotations and universal lesion detection with deep learning. J Med Imaging. 2018;5(03):1. doi:10.1117/1.JMI.5.3.036501 | Fuente de los 12 374 cortes de pelvis/torax. Dataset alternativo o complementario a CTPelvic1K; hay que saber si tiene segmentacion osea (probablemente no). |
| 44. Nir G, Dowrick T, Avery J, Holder D. UCLH Stroke EIT Dataset—Radiology Data. 2017. doi:10.5281/zenodo.838704 | Fuente de los cortes de cabeza. Baja relevancia para pelvis, pero define el desbalance declarado como limitacion. |
| 46. Kanopoulos N, Vasanthavada N, Baker RL. Design of an image edge detection filter using the Sobel operator. IEEE J Solid-State Circuits. 1988;23(2):358-367 | Fuente original del operador que define la metrica de sharpness (percentil 90). Citable si la tesis adopta la metrica. |
| 47. Wang Z, Bovik AC, Sheikh HR, Simoncelli EP. Image quality assessment: from error visibility to structural similarity. IEEE Trans Image Process. 2004;13(4):600-612 | Fuente original de SSIM, la metrica de structural integrity. |
| 48. van der Walt S, Schonberger JL, Nunez-Iglesias J, et al. scikit-image: image processing in Python. PeerJ. 2014;2:e453 | Implementacion concreta de SSIM usada (importa para reproducir con data_range = 5000 HU). |
| 49. Dice LR. Measures of the amount of ecologic association between species. Ecology. 1945;26(3):297-302 | Fuente original del SDC, nucleo matematico de bone integrity y metal integrity, y por tanto de BFC e ISC. |
| 51. Peters N, Wohlfahrt P, Hofmann C, et al. Reduction of clinical safety margins in proton therapy enabled by the clinical implementation of dual-energy CT. Radiother Oncol. 2022;166:71-78 | Fuente del umbral de 2% de range shift que ancla el score de protones. Solo relevante si la tesis discute por que descarta esa metrica. |
| 54. Lugmayr A, Danelljan M, Romero A, Yu F, Timofte R, Van Gool L. RePaint: inpainting using denoising diffusion probabilistic models. 2022. http://arxiv.org/abs/2201.09865 | Esquema de resampling (noising/denoising alternado) para inpainting con difusion. Directamente aplicable al renderizador si la banda B_delta se trata como region a completar. |
| 56. Bhadra S, Kelkar VA, Brooks FJ, Anastasio MA. On hallucinations in tomographic image reconstruction. IEEE Trans Med Imaging. 2021;40(11):3249-3260 | Riesgo de alucinacion de features en regiones peri-metal generadas por deep learning. Ataca de frente la validez del renderizador; puede obligar a un control explicito en la evaluacion. |
| 58. Zhang Y, Mao Y, Lu X, et al. From single to universal: tiny lesion detection in medical imaging. Artif Intell Rev. 2024;57(8):192 | Citado como el sustituto algoritmico de la inspeccion visual para features pequenos. Podria aportar una metrica que cubra el hueco que Peters declara abierto. |
| 59. Ho J, Salimans T. Classifier-Free Diffusion Guidance. 2022. http://arxiv.org/abs/2207.12598 | El paper lo propone explicitamente como via para condicionar la generacion por region corporal. Compite o complementa el condicionamiento por ControlNet de la tesis. |

## Verificacion 2026-09-16

| Pregunta | Respuesta | Frase original (<15 palabras) | Seccion/pagina |
|---|---|---|---|
| 1a. Paciente y metal proyectados JUNTOS en una sola simulacion polienergetica | NO ENCONTRADO EN EL PDF. No hay frase que diga que el haz atraviesa paciente y metal en la misma proyeccion. | NO ENCONTRADO EN EL PDF | — |
| 1b. Sinogramas o imagenes de paciente y metal simulados por separado y sumados | NO ENCONTRADO EN EL PDF. Tampoco se describe suma de sinogramas ni de imagenes. | NO ENCONTRADO EN EL PDF | — |
| 1c. Que SI dice sobre la combinacion: el metal se inserta en la imagen CT clinica (dominio imagen) | Insercion en posiciones de la CT; no dice el paso de proyeccion posterior | "virtual metal objects were then inserted in random soft tissue or bone positions" | 2.3, p. 4 |
| 1c (cont.) | Marco hibrido = CT clinica + objetos virtuales | "combining clinical CT scans with virtual metal objects" | 2.3, p. 3 |
| 1c (cont.) | Las imagenes clinicas son entrada de la simulacion | "which was applied to all images used as input to the simulations" | 2.3, pp. 3-4 |
| 1d. Espectro de 12 energias | Si, en la geometria vendor-neutral de generacion; no dice explicitamente si paciente y metal comparten esa proyeccion | "The source spectrum was sampled at 12 energies." | 2.1, p. 3 |
| 1e. Salidas por caso | Se generan sinograma con y sin metal; no se dice como se obtiene cada uno | "each containing a sinogram with and without metal, the respective reconstructions" | 2.3, p. 4 |
| 1f. Correccion de beam hardening | Solo correccion de agua, aplicada a todos los sinogramas | "water beam hardening correction was applied to all sinograms" | 2.1, p. 3 |
| 2a. Conversion HU -> atenuacion/material de la imagen clinica | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF | — |
| 2b. Descomposicion agua/hueso o material unico | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF | — |
| 2c. Materiales de los metales virtuales | Si: amalgama, titanio o cobalto, acero inoxidable, oro (Tabla 2) | Tabla 2, "Spinal implant (40%) / Stainless steel / 2.5-10 mm / 2-4" | Tabla 2, p. 4 |
| 3a. Motivo del filtro de frequency boosting | Compensar el doble emborronamiento (imagen clinica ya reconstruida + simulacion) | "would duplicate blurring already present in the clinical input CT images" | 2.3, p. 3 |
| 3b. Como se estima | Cociente empirico de espectros de Fourier (promedio polar) entre imagenes originales y simuladas | "the polar average of the absolute value of the Fourier transform was computed" | 2.3, p. 3 |
| 3b (cont.) | Cociente entre original y simulada | "The ratio of this frequency response was computed between original and simulated images" | 2.3, p. 3 |
| 3b (cont.) | Promediado en 64 cortes | "then averaged over 64 slices in the volume" | 2.3, p. 3 |
| 3b (cont.) | Filtro 1D asignado radialmente -> filtro 2D en Fourier | "assigned radially across all Fourier angles" | 2.3, p. 3 |
| 3c. Numero de "typical CT images" usadas | NO ENCONTRADO EN EL PDF (solo "a number of") | "For a number of typical CT images and their simulated counterparts" | 2.3, p. 3 |
| 3d. Frecuencias concretas, ganancia o curva publicada del filtro | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF | — |
| 3e. Estimacion via MTF | NO ENCONTRADO EN EL PDF. El termino MTF no aparece; la estimacion es el cociente de espectros descrito en 3b. | NO ENCONTRADO EN EL PDF | — |
| 3f. Cita a Fan 2022 como origen | Si: la frase del filtro lleva la ref. 45, que es Fan, Pack, De Man 2022 (doi 10.1117/12.2646407, mismo DOI que docs/literatura/fan2022.md) | "applying a frequency boosting filter prior to the CT simulation.45" | 2.3, p. 3; ref. 45, p. 11 |
| 3f (cont.) | Texto de la ref. 45 | "Fan Y, Pack J, De Man B. A virtual imaging trial framework" | Referencias, p. 11 |
| 4a. Objeto de validacion | Fantoma fisico CIRS de torax con varillas metalicas, no imagenes hibridas | "Simulation accuracy was assessed in a CIRS tissue equivalent thorax phantom" | 2.2, p. 3 |
| 4b. Escaner real y modelo comparado | Lightspeed VCT (64 filas), no la geometria vendor-neutral usada para los 14 000 casos | "experimental validation of the metal artifact physics models, we used a 64-row CT scanner" | 2.1, p. 2 |
| 4b (cont.) | Geometria de entrenamiento distinta a la validada | "For all training data simulations, a nominal vendor-neutral CT geometry was used" | 2.1, p. 2 |
| 4c. Configuraciones | 4 configuraciones (Tabla 1: 0 = solo solid water; 1-3 con acero, aluminio, cobre, TZM) | "Four different metal configurations were scanned" | 2.2, p. 3 |
| 4d. Metrica 1: media CT en ROIs con y sin artefacto | < 2% | "with and without artifacts—the simulated mean deviated by less than 2%" | 3.1, p. 6 |
| 4e. Metrica 2: ruido (2SD) sin artefacto | < 10% | "the noise level (defined as 2SD) deviated by less than 10%" | 3.1, p. 6 |
| 4f. Ruido en ROIs con artefacto | hasta 13.3% | "larger discrepancies in noise were observed (up to 13.3% in Exp 4" | 3.1, p. 6 |
| 4g. Streaking por metal | Evaluado cualitativamente (Figura 3) y dentro de las ROIs con artefacto | "Strong streak artifacts resulting from the metal inserts are well-replicated across all cases" | 3.1, p. 6 |
| 4h. Discrepancias residuales | Streaks y sesgo leve en imagenes de diferencia | "show some remaining discrepancies in streaks and a slight bias" | 3.1, p. 6 |
| 4i. Metales grandes | Desviaciones mayores; detalle en Supplement S2, no incluido en el PDF | "For larger metal objects, the observed deviations were more prominent" | 3.1, p. 6 |
| 4j. Fantoma cardiaco adicional | Se menciona el experimento; resultados numericos NO ENCONTRADO EN EL PDF | "Additional experiments were performed with solid metal rods" | 2.2, p. 3 |
| 4k. Beam hardening como metrica propia de esta validacion | NO ENCONTRADO EN EL PDF. Solo se remite a evaluacion previa (ref. 37). | "evaluated the modeling accuracy of CatSim regarding the X-ray spectrum and beam hardening" | 2.1, p. 2 |
| 4l. Validacion de imagenes hibridas (CT clinica + metal virtual) contra paciente real con metal | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF | — |
| 4m. Alcance declarado de la validacion | Limitado al setup de escaner usado | "cylindrical metal implants for the specific CT scanner setup used here" | 4 Discussion, p. 9 |
| 5a. 2D o 3D | 2D para todos los datasets | "Since most MAR research is performed in 2D, all datasets are simulated in 2D" | Abstract, p. 1 |
| 5b. Detector de generacion | Una sola fila de detector (el termino "fan-beam" NO ENCONTRADO EN EL PDF) | "1 detector row with 900 columns was simulated, with a total of 1000 views" | 2.1, p. 3 |
| 5c. Reconstruccion | FDK | "filtered back projection by Feldkamp, Davis & Kress algorithm (FDK) was used" | 2.1, p. 3 |
| 5d. Scatter | Si, convolucional; calculado en una fila y escalado a 64 filas | "The scattering process in CatSim is simulated using a modified convolution-based approach" | 2.1, p. 2 |
| 5d (cont.) | Escalado de scatter | "computed for a single detector row and scaled to mimic scatter for 64 detector rows" | 2.1, p. 3 |
| 5d (cont.) | Parametros no listados heredados del modelo Lightspeed | "All other parameters were the same as for the Lightspeed VCT model" | 2.1, p. 3 |
| 5e. Submuestras | 8 submuestras (foco ancho x foco largo x rotacion) | "for a total of eight subsamples (2 × 2 × 2)" | 2.1, p. 3 |
| 5f. Celda de detector finita | Proyector distance-driven, sin submuestreo de detector | "A distance-driven projector was used to model the finite detector cell size" | 2.1, p. 3 |
| 5g. Volumen parcial (termino explicito o modelado no lineal) | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF | — |
| 5h. Extension a 3D | Requiere repetir y ampliar el modelado | "the presented modelling steps within XCIST need to be repeated and expanded" | 4 Discussion, p. 9 |
| 6a. Limitacion de hibridacion declarada: doble blur | Unica inconsistencia imagen clinica/simulacion explicitada; se compensa con el filtro | "would duplicate blurring already present in the clinical input CT images" | 2.3, p. 3 |
| 6b. Ruido o artefactos ya presentes en la imagen clinica de entrada re-proyectados | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF | — |
| 6c. Error de la conversion HU -> atenuacion como limitacion | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF | — |
| 6d. Solo insercion de metal | Sin cambios anatomicos quirurgicos | "all simulations are limited to the insertion of metal objects" | 4 Discussion, p. 9 |
| 6e. Sesgo de geometria vendor-neutral | Declarado | "vendor-neutral geometry was used for the metal simulation, potentially introducing a bias" | 4 Discussion, p. 9 |
| 6f. Imperfecciones del modelo fisico | Declaradas como secundarias para entrenamiento/evaluacion MAR | "play a secondary role for the purpose of AI-based MAR training" | 4 Discussion, p. 9 |
