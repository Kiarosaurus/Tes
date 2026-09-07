# karageorgos2024ddpm — DDPM para reduccion de artefactos metalicos en CT

- **DOI / URL:** doi:10.1109/TMI.2024.3416398 (IEEE Trans Med Imaging, 2024 Oct; 43(10): 3521-3532)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/karageorgos2024ddpm.pdf

Profundidad: texto completo (manuscrito de autor HHS Public Access, 30 paginas incl. figuras y tablas).

## Que hace (3 lineas maximo)

Entrena un DDPM **incondicional** en el dominio de sinograma para inpaintar la traza metalica y **remover** artefactos (MAR).
Los pares de entrenamiento se fabrican insertando objetos metalicos virtuales en CT reales y simulando la adquisicion con CatSim.
Se compara contra NMAR, una U-net de convoluciones parciales (PUnet) y un GAN de inpainting, en test simulado y en 4 CT clinicos con metal virtual.

## Restriccion o supuesto clave

El paper opera en la direccion inversa a la tesis: su objetivo declarado es completar datos faltantes, no generarlos. La frase que lo fija: "a DDPM-based approach is proposed for inpainting of missing sinogram data for improved MAR" (Abstract). El DDPM se entrena solo sobre sinogramas **sin metal** ("The DDPM was unconditionally trained with the ground truth sinograms, S_GT", Sec. II-A), de modo que el modelo generativo nunca aprende la apariencia del metal ni del streaking: la mascara metalica solo entra en inferencia. El supuesto que le impide manejar implantes rigidos como objeto a *sintetizar* es que el metal se trata como region corrupta a descartar, y al final "an estimate of the metal object was added, by thresholding the uncorrected image" (Sec. II-F), es decir el implante se reinyecta por umbralizacion, no se modela. Ademas es 2D: "the metal simulations and MAR techniques were carried out using 2D sinograms and 2D images" (Sec. IV).

## Que toco de aqui
- [x] metodo que reimplemento (la insercion de metal virtual + simulacion CatSim compite/coincide con el baseline fisico de la tesis)
- [x] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Umbral de validez de posicion del metal: 50% de solape con region > 200 HU | "valid only if it overlapped by at least 50% with a region higher than 200 HU" | Sec. II-A, p. 4 |
| Hasta 7 objetos metalicos por imagen | "images with up to seven metal objects" | Sec. II-A, p. 3-4 |
| 11,560 imagenes CT de 512x512 | "A total of 11,560 CT images of size 512x512 pixels were obtained" | Sec. II-A, p. 3 |
| 20,019 sinogramas corruptos; 19,819 train / 200 test | "split into 19,819 training sinograms and 200 test sinograms" | Sec. II-A, p. 4 |
| Umbral de metal en evaluacion: CTN_M > 2500 HU | "the metal object (CTN_M > 2500 HU)" | Sec. II-G, p. 11 |
| Rango de hueso: 150 HU <= CTN_B < 1000 HU | "the patients' bone structure (150 HU <= CTN_B < 1000 HU)" | Sec. II-G, p. 11 |
| Umbralizacion NMAR: aire -1000 HU, tejido blando 0 HU | "regions of air and soft tissue to -1000 HU and 0 HU, respectively" | Sec. II-B, p. 5 |
| Ventana de despliegue: nivel 0, ancho 400 HU | "displayed with a window level of 0 and width of 400 HU" | Fig. 4, p. 23 |
| Segmentacion de traza metalica en el Apendice: > 3000 HU | "The metal trace was segmented as regions exceeding 3000 HU" | Apendice, p. 15 |
| DDPM SSIM 0.964 +/- 0.032 | Tabla I, fila DDPM | Tabla I, p. 28 |
| DDPM PSNR 46.16 +/- 5.88 | Tabla I, fila DDPM | Tabla I, p. 28 |
| DDPM RMSE 12.3 +/- 10.4 | Tabla I, fila DDPM | Tabla I, p. 28 |
| GAN SSIM 0.959 +/- 0.039; PSNR 45.74 +/- 5.22; RMSE 12.6 +/- 9.6 | Tabla I, fila GAN | Tabla I, p. 28 |
| PUnet SSIM 0.945 +/- 0.050; PSNR 44.84 +/- 4.89; RMSE 13.7 +/- 9.6 | Tabla I, fila PUnet | Tabla I, p. 28 |
| NMAR SSIM 0.920 +/- 0.071; PSNR 42.12 +/- 5.94; RMSE 20.2 +/- 19.7 | Tabla I, fila NMAR | Tabla I, p. 28 |
| Significancia DDPM vs NMAR: SSIM p<10^-26, PSNR p<10^-21 | "NMAR (SSIM: p < 10^-26; PSNR: p < 10^-21)" | Abstract, p. 1 |
| Significancia DDPM vs CNN: SSIM p<10^-25, PSNR p<10^-9 | "the CNN (SSIM: p < 10^-25; PSNR: p < 10^-9)" | Abstract, p. 1 |
| Significancia DDPM vs GAN: SSIM p<10^-6, PSNR p<0.05 | "the GAN (SSIM: p < 10^-6; PSNR: p < 0.05)" | Abstract, p. 1 |
| DDPM mejor en 13 de 28 metricas clinicas | "DDPM had the best performance for most metrics (13 out of 28)" | Sec. III-C, p. 12 |
| Pelvis (Paciente 1) DDPM: SSIM_INT 0.989, RMSE_INT 11, RMSE_ROI 20 | Tabla II, columna DDPM, Paciente 1 - pelvis | Tabla II, p. 29 |
| Pelvis (Paciente 1) DDPM: CTN_blue 39+/-22, CTN_orange -93+/-16 | Tabla II, Paciente 1 - pelvis | Tabla II, p. 29 |
| Pelvis (Paciente 1) DDPM: Vol_M 0.323, Vol_B 9.50 (Gr.Tr. 0.095 y 9.41) | Tabla II, Paciente 1 - pelvis | Tabla II, p. 29 |
| Cadera (Paciente 4) DDPM: SSIM_INT 0.800, RMSE_INT 147, RMSE_ROI 52 | Tabla II, Paciente 4 - Hip | Tabla II, p. 29 |
| Cadera (Paciente 4) NMAR: SSIM_INT 0.859, RMSE_INT 113, RMSE_ROI 36 | Tabla II, Paciente 4 - Hip | Tabla II, p. 29 |
| Apendice, mascara con R=1.4: SSIM 0.908, PSNR 45.02, RMSE 11.45 | Tabla III | Tabla III, p. 16 |
| Apendice, mascara con R=1.8: SSIM 0.908, PSNR 44.92, RMSE 11.63 | Tabla III | Tabla III, p. 16 |
| Apendice, mascara con R=0.7: SSIM 0.545, PSNR 16.91, RMSE 54.82 | Tabla III | Tabla III, p. 16 |
| Apendice, mascara con R=0.5: SSIM 0.538, PSNR 17.02, RMSE 57.69 | Tabla III | Tabla III, p. 16 |
| Apendice, traza real (Gr. Truth): SSIM 0.957, PSNR 47.34, RMSE 7.57 | Tabla III | Tabla III, p. 16 |
| Geometria: source-to-iso 540 mm, source-detector 950 mm | "source-to-iso-distance 540 mm, source-to-detector distance 950 mm" | Sec. II-A, p. 3 |
| Detector 1.0 mm x 1.1 mm, 2 filas, 888 columnas, 984 vistas | "2 detector rows, 888 detector columns, 984 views" | Sec. II-A, p. 3 |
| 120 kVp, 200 mA | "120 kVp tube voltage, 200 mA tube current" | Sec. II-A, p. 3 |
| Sinogramas padded a 1024x1024; recortados a 888x894 | "padded to a dimension of 1024x1024" / "original sinogram dimension of 888x894" | Sec. II-A p. 4 / II-F p. 10 |
| DDPM: 200,000 iteraciones, batch 4, N=1000 pasos de difusion | "batch size of 4, N = 1000 diffusion steps ... 200,000 iterations" | Sec. II-E-1, p. 9 |
| lambda = 0.001 en la perdida hibrida | "lambda is a weighting factor, which was set equal to 0.001" | Sec. II-E-1, p. 9 |
| Inferencia: T = 250, r = 10, jump j = 10 | "repeated for T = 250 diffusion steps" / "resampling steps, r = 10" / "jump of j = 10" | Sec. II-E-2, p. 10 |
| PUnet y GAN: 200,000 pasos, batch 4, Adam lr 0.0002 | "200,000 training steps with a batch size of 4 ... learning rate of 0.0002" | Sec. II-C p. 5, II-D p. 7 |
| Perdida PUnet: L = MAE_v + 6MAE_c + 0.05L_p + 120L_style + 0.1L_TV | Ecuacion (2) | Sec. II-C, p. 5 |
| Self-attention en resoluciones 16x16 y 8x8, 4 cabezas | "at the 16x16 and 8x8 resolutions with a four attention heads" | Sec. II-E-1, p. 9 |
| Interpolacion lineal NMAR usa 5 proyecciones adyacentes | "average projection value of five consecutive projection numbers" | Sec. II-B, p. 4 |
| 4 pacientes clinicos MGH (prostata, columna, dental, cadera) | "four patient CT scans ... for prostate, spine, dental and hip regions" | Sec. II-A, p. 4 |
| Protocolo IRB MGH 2016P001950 | "Institutional Review Board of Massachusetts General Hospital (protocol 2016P001950)" | Sec. II-A, p. 4 |
| Financiamiento NIH/NIBIB R01EB031102 | "supported by the NIH/NIBIB grant R01EB031102" | Acknowledgements, p. 15 |

## Donde entra en mi tesis

1. **Evidencia de la implicancia #2 (GAP)**: es difusion aplicada a metal en direccion de REMOCION, no de sintesis; sirve para sostener que la literatura de difusion + metal es MAR.
2. **Baseline fisico (C2 / XCIST-CatSim)**: el paper usa CatSim para insertar metal virtual y generar pares, y cita explicitamente XCIST [23] y CatSim [24]. Es antecedente directo del baseline fisico de comparacion de la tesis y define un protocolo de insercion virtual con el que hay que contrastarse.
3. **Muestreador (C1)**: su criterio de colocacion valida (solape >=50% con region >200 HU) es una restriccion anatomica primitiva comparable, y mucho mas debil, que los mapas de densidad / contencion cortical de la tesis.
4. **Evaluacion**: aporta un conjunto de metricas clinicamente relevantes (CTN bias cerca/lejos del metal, RMSE_INT, RMSE_ROI, SSIM_INT, volumen de metal y hueso) potencialmente reutilizables para juzgar realismo de artefactos sinteticos.
5. **Sensibilidad a la mascara metalica**: Tabla III cuantifica el colapso de calidad cuando la mascara subestima la traza, dato util para justificar la banda extendida B_delta.

## Dudas para el asesor

- El criterio ">=50% de solape con region >200 HU" es la unica restriccion anatomica que usan para colocar metal. Conviene citarlo como ejemplo de lo que la tesis mejora, o es demasiado debil para valer como comparacion?
- Sus metricas CTN_blue / CTN_orange (cerca vs lejos del metal) se pueden invertir como metrica de realismo del streaking generado, en vez de metrica de correccion?
- El paper simula con CatSim y evalua sobre pelvis (marcadores de oro) y cadera (protesis total). Eso reduce la novedad del baseline fisico de la tesis o mas bien lo respalda?

## Evidencia textual

| Item | Frase original (<= 15 palabras) | Seccion / pagina |
|---|---|---|
| Objetivo = remocion | "a DDPM-based approach is proposed for inpainting of missing sinogram data for improved MAR" | Abstract, p. 1 |
| Entrenamiento incondicional | "The proposed model is unconditionally trained, free from information on metal objects" | Abstract, p. 1 |
| Aim del estudio | "to implement a MAR technique that utilizes a DDPM in the sinogram domain" | Sec. I, p. 3 |
| Generacion de datos por simulacion | "Training data are generated by performing highly realistic CT simulations of real patient images" | Sec. II-A, p. 3 |
| Simulador usado | "our recently developed realistic CT physics models in the CatSim CT simulator" | Sec. II-A, p. 3 |
| Fisica simulada | "realistic quantum noise, electronic noise and beam hardening" | Sec. II-A, p. 3 |
| Geometria nominal | "source-to-iso-distance 540 mm, source-to-detector distance 950 mm" | Sec. II-A, p. 3 |
| Celdas de detector | "1.0 mm x 1.1 mm detector cells, detector quarter offset" | Sec. II-A, p. 3 |
| Tension y corriente | "120 kVp tube voltage, 200 mA tube current" | Sec. II-A, p. 3 |
| Vistas y columnas | "2 detector rows, 888 detector columns, 984 views, a large bowtie filter" | Sec. II-A, p. 3 |
| Datos fuente | "11,560 CT images of size 512x512 pixels ... from the publicly available DeepLesion Dataset" | Sec. II-A, p. 3 |
| Segundo dataset | "and the UCLH Stroke EIT dataset [27], including a wide variety of patient anatomies" | Sec. II-A, p. 3 |
| Origen de las formas metalicas | "Random metal objects were defined based on CT images of metal objects" | Sec. II-A, p. 3 |
| Aumentacion de las formas | "Spatial transformations (including random translation and scaling) were employed" | Sec. II-A, p. 3 |
| Morfologia aplicada | "opening, closing, erosion and dilation were applied to create further variations" | Sec. II-A, p. 3 |
| Numero de objetos | "the resulting metal objects were randomly combined to obtain images with up to seven metal objects" | Sec. II-A, p. 3-4 |
| Umbral de colocacion valida | "valid only if it overlapped by at least 50% with a region higher than 200 HU" | Sec. II-A, p. 4 |
| Tamano del corpus corrupto | "a total of 20,019 corrupted sinograms were generated" | Sec. II-A, p. 4 |
| Split | "split into 19,819 training sinograms and 200 test sinograms from different subjects" | Sec. II-A, p. 4 |
| Datasets clinicos | "we collected four patient CT scans ... for prostate, spine, dental and hip regions" | Sec. II-A, p. 4 |
| Objetos disenados a mano | "we manually designed realistic metal objects for each case" | Sec. II-A, p. 4 |
| Materiales de los implantes | "gold prostate markers, steel spinal cage, amalgam dental fillings and a titanium hip replacement" | Sec. II-A, p. 4 |
| IRB | "Data sharing was approved by the Institutional Review Board of Massachusetts General Hospital" | Sec. II-A, p. 4 |
| Padding de sinogramas | "The sinograms were padded to a dimension of 1024x1024" | Sec. II-A, p. 4 |
| Padding circular | "Circular padding was carried out along the vertical axis exploiting the periodic nature" | Sec. II-A, p. 4 |
| Entrenamiento sin informacion de metal | "The DDPM was unconditionally trained with the ground truth sinograms, S_GT, as the target" | Sec. II-A, p. 4 |
| Reinsercion del metal | "The corrected sinograms are reconstructed and metal objects are re-inserted in the image-domain" | Sec. II-A, p. 4 |
| Umbral aire/tejido en NMAR | "setting pixels corresponding to regions of air and soft tissue to -1000 HU and 0 HU" | Sec. II-B, p. 5 |
| Hueso conserva valores | "Bone regions maintain their original values, due to their high intensity variation" | Sec. II-B, p. 5 |
| LI: ventana de 5 proyecciones | "fit to connect the average projection value of five consecutive projection numbers" | Sec. II-B, p. 4 |
| Arquitectura PUnet | "an encoder network with seven down-sampling layers ... seven decoding layers" | Sec. II-C, p. 5 |
| Entrenamiento PUnet | "trained over 200,000 training steps with a batch size of 4, using the Adam optimizer" | Sec. II-C, p. 5 |
| Learning rate PUnet | "an initial learning rate of 0.0002" | Sec. II-C, p. 5 |
| Perdida PUnet | "L = MAE_v + 6MAE_c + 0.05L_p + 120L_style + 0.1L_TV" | Ec. (2), Sec. II-C, p. 5 |
| Discriminador GAN | "SN-PatchGAN comprises a six-layer convolutional neural network with kernel size of 5" | Sec. II-D, p. 6 |
| Stride del discriminador | "kernel size of 5 and a stride of 2" | Sec. II-D, p. 6 |
| Entrenamiento GAN | "trained over 200,000 training steps with a batch size of 4" | Sec. II-D, p. 7 |
| Arquitectura DDPM | "This U-net consists of 7 encoding and 7 decoding layers" | Sec. II-E-1, p. 9 |
| Bloque residual | "The BigGAN residual block [32] was utilized for up-sampling and down-sampling" | Sec. II-E-1, p. 9 |
| Atencion | "Self-attention modules are also used at the 16x16 and 8x8 resolutions with a four attention heads" | Sec. II-E-1, p. 9 |
| Hiperparametros DDPM | "batch size of 4, N = 1000 diffusion steps and the mean square error (MSE) as a loss function" | Sec. II-E-1, p. 9 |
| Iteraciones DDPM | "for a total of 200,000 iterations" | Sec. II-E-1, p. 9 |
| Lambda | "lambda is a weighting factor, which was set equal to 0.001" | Sec. II-E-1, p. 9 |
| Baseline de inferencia | "We chose to use the NMAR corrected sinogram, S_NMAR, as baseline" | Sec. II-E-2, p. 9 |
| Pasos de inferencia | "The process is repeated for T = 250 diffusion steps" | Sec. II-E-2, p. 10 |
| Resampling | "carried out iteratively at multiple resampling steps, r = 10" | Sec. II-E-2, p. 10 |
| Jump | "The resampling process is carried out at multiple time steps, with a jump of j = 10" | Sec. II-E-2, p. 10 |
| Dimension final | "convert it to the original sinogram dimension of 888x894" | Sec. II-F, p. 10 |
| Reconstruccion | "reconstructed with filtered back-projection" | Sec. II-F, p. 10 |
| Metal por umbral | "defining all voxels above the threshold as metal voxels" | Sec. II-F, p. 10 |
| Metricas estandar | "structural similarity index (SSIM), peak signal-to-noise ratio (PSNR) and root mean square error (RMSE)" | Sec. II-G, p. 11 |
| Test estadistico | "A paired t-test was used to confirm the significance of the DDPM improvement" | Sec. II-G, p. 11 |
| Definicion RMSE_INT | "within the patient skin-line (RMSE_INT) excluding the surrounding air and patient couch" | Sec. II-G, p. 11 |
| Definicion RMSE_ROI | "in a region-specific organ contour (RMSE_ROI): prostate (excluding the metal) in the pelvis" | Sec. II-G, p. 11 |
| ROIs por region | "the spinal cord in the head & neck, and heart in the thorax" | Sec. II-G, p. 11 |
| Definicion SSIM_INT | "Anatomical accuracy was evaluated using the SSIM within the patient skin-line (SSIM_INT)" | Sec. II-G, p. 11 |
| Umbral de metal (volumen) | "the volume estimates of the metal object (CTN_M > 2500 HU)" | Sec. II-G, p. 11 |
| Rango de hueso (volumen) | "the patients' bone structure (150 HU <= CTN_B < 1000 HU)" | Sec. II-G, p. 11 |
| Definicion CTN_blue / CTN_orange | "CTN_blue in close proximity to the metal objects and CTN_orange further away" | Sec. III-C, p. 12 |
| Ventana de despliegue | "displayed with a window level of 0 and width of 400 HU" | Fig. 4 caption, p. 23 |
| Resultado NMAR peor | "NMAR marked the lowest SSIM, PSNR and highest RMSE" | Sec. III-B, p. 11 |
| p-valores SSIM | "DDPM versus GAN (p<10^-6, DF 199, paired SD 0.012)" | Sec. III-B, p. 12 |
| p-valores SSIM (PUnet) | "PUnet (p<10^-25, DF 199, paired SD 0.021)" | Sec. III-B, p. 12 |
| p-valores SSIM (NMAR) | "NMAR (p<10^-26, DF 199, paired SD 0.048)" | Sec. III-B, p. 12 |
| p-valores PSNR | "higher PSNR compared to GAN (p<0.05, DF 199, paired SD 2.81)" | Sec. III-B, p. 12 |
| p-valor RMSE | "RMSE was significantly lower in the case of DDPM, compared to NMAR (p<0.001" | Sec. III-B, p. 12 |
| RMSE sin diferencia | "however no significant differences were found against PUnet and GAN" | Sec. III-B, p. 12 |
| Conteo de metricas ganadas | "DDPM had the best performance for most metrics (13 out of 28)" | Sec. III-C, p. 12 |
| Mejor en pelvis | "DDPM outperformed the other methods in all metrics in the pelvis" | Sec. III-C, p. 12 |
| Falla en cadera | "In the case of the total hip replacement, NMAR marked best performance in most metrics" | Sec. III-C, p. 12 |
| Limitacion de objetos grandes | "significantly larger metal objects still pose a challenge for the AI-based MAR techniques" | Sec. III-C, p. 12 |
| Segmentacion subóptima | "consistently above ground truth for all investigated methods, which indicates ... sub-optimal" | Sec. III-C, p. 12 |
| Limitacion 2D | "the metal simulations and MAR techniques were carried out using 2D sinograms and 2D images" | Sec. IV, p. 14 |
| Latente como trabajo futuro | "apply the DDPM in latent space, similarly as in [34]" | Sec. IV, p. 14 |
| Requiere mascara metalica | "The proposed approach requires a metal mask in the sinogram domain" | Sec. IV, p. 14 |
| Mismatch de mascara degrada MAR | "A mismatch between the metal trace obtained through image segmentation ... reduce the MAR quality" | Sec. IV, p. 14 |
| Brecha simulado-clinico | "the clinical scans were not derived from the same databases that were used to train" | Sec. IV, p. 13 |
| Sesgo del muestreo 2D | "randomly extracting 2-D slices from CT scans, which can potentially underrepresent views" | Sec. IV, p. 13 |
| Umbral de traza en Apendice | "The metal trace was segmented as regions exceeding 3000 HU" | Apendice, p. 15 |
| Ratios de mismatch evaluados | "ratios of segmented area to actual metal trace area equal to 1) 1.4, 2) 1.8, 3) 0.7 and 4) 0.5" | Apendice, p. 15 |
| Conclusion del Apendice | "higher segmentation accuracy leads to more effective MAR" | Apendice, p. 15 |
| Caso del Apendice = pelvis | "A clinical CT scan of the pelvis with two virtually placed gold marker implants" | Apendice, p. 15 |

## Verificacion de nivel

Criterio de la autora: Nivel 1 = critico, si se equivoca aqui se cae una tesis o el benchmark. Nivel 2 = afecta la redaccion. Nivel 3 = apoyo.
Clasificacion previa (hecha sin leer el PDF): NIVEL 2.

**1. Confirma que la direccion es REMOCION y no sintesis?**
Si, sin ambiguedad. "a DDPM-based approach is proposed for inpainting of missing sinogram data for improved MAR" (Abstract, p. 1). Refuerzo: "The aim of the present study is to implement a MAR technique that utilizes a DDPM in the sinogram domain" (Sec. I, p. 3). El generativo se entrena solo sobre sinogramas sin metal: "The DDPM was unconditionally trained with the ground truth sinograms, S_GT, as the target distribution" (Sec. II-A, p. 4). En terminos del pipeline, el modelo genera contenido *plausible libre de metal*, no artefactos.

**2. Como obtuvo sus datos de entrenamiento? Inserta metal sinteticamente?**
**SI, inserta metal sinteticamente, y este es el hallazgo que cambia el nivel.** Frases exactas:
- "Training data are generated by performing highly realistic CT simulations of real patient images with and without metal objects as well as simulations of metal objects only" (Sec. II-A, p. 3).
- "our recently developed realistic CT physics models in the CatSim CT simulator [23], [24] result in highly realistic CT simulations [25] as well as realistic metal artifacts" (Sec. II-A, p. 3).
- "Random metal objects were defined based on CT images of metal objects obtained from the dataset used in [16]" (Sec. II-A, p. 3).
- "the position of a metal object was considered valid only if it overlapped by at least 50% with a region higher than 200 HU" (Sec. II-A, p. 4).
- "we manually designed realistic metal objects for each case (gold prostate markers, steel spinal cage, amalgam dental fillings and a titanium hip replacement)" (Sec. II-A, p. 4).

**Metodo de insercion (descripcion):** es una insercion **fisica, no generativa**. (a) Toman imagenes CT reales de dos bancos publicos; (b) toman formas metalicas de un dataset previo y las varian con transformaciones espaciales (traslacion y escalado aleatorios) y operadores morfologicos (apertura, cierre, erosion, dilatacion); (c) combinan hasta siete objetos por imagen y validan la posicion con la regla de solape >=50% sobre region >200 HU (para no colocar metal en aire); (d) simulan la adquisicion con CatSim con geometria nominal explicita (540/950 mm, 120 kVp, 200 mA, 984 vistas, 888 columnas, bowtie grande) incluyendo ruido cuantico, ruido electronico y endurecimiento de haz; (e) la sombra del metal ("metal trace") en el sinograma se usa como mascara de corrupcion. Para los 4 casos clinicos MGH los implantes se disenaron a mano por material y se colocaron virtualmente en el paciente ("virtually placed").
Consecuencia para la tesis: esto es exactamente la via fisica de insercion (CatSim/XCIST) que la tesis ya tiene marcada como baseline. Es competencia directa del renderizador en la funcion "producir CT con implante + artefactos", aunque por un mecanismo distinto (simulacion determinista de fisica, no modelo generativo condicionado).

**3. Usa ventanas HU multiples o normalizacion por ventana?**
No hay codificacion multi-ventana en HU para el modelo. Toda la red opera en el dominio de sinograma, no en HU. Los unicos valores de HU explicitos son umbrales y una ventana de despliegue:
- Ventana de visualizacion: "window level of 0 and width of 400 HU" (Fig. 4, p. 23), es decir aproximadamente [-200, 200] HU (el rango como intervalo NO aparece escrito en el PDF).
- Umbral de colocacion de metal: "> 200 HU" (Sec. II-A, p. 4).
- Umbral de metal para volumetria: "CTN_M > 2500 HU" (Sec. II-G, p. 11).
- Rango oseo para volumetria: "150 HU <= CTN_B < 1000 HU" (Sec. II-G, p. 11).
- Umbralizacion de tejidos en NMAR: aire "-1000 HU", tejido blando "0 HU" (Sec. II-B, p. 5).
- Segmentacion de traza en Apendice: "> 3000 HU" (p. 15).
Normalizacion por ventana: NO ENCONTRADO EN EL PDF. Lo que si hay es la normalizacion del sinograma en NMAR (division pixel a pixel por un sinograma prior), que es otra cosa. Para C3 esto significa: el paper NO ofrece precedente de codificacion multi-ventana; solo aporta un juego de umbrales HU citables (200 / 1000 / 2500 / 3000) y la ventana de despliegue 0/400.

**4. Espacio latente o imagen? Que arquitectura?**
Trabaja en el **espacio de senal directo (sinograma 2D)**, no en latente. La red es una U-net mejorada de 7 capas de codificacion y 7 de decodificacion, con bloques residuales BigGAN para up/down-sampling y self-attention a 16x16 y 8x8 con cuatro cabezas; embedding del paso temporal por bloque residual. El latente aparece solo como trabajo futuro: "use of pre-trained autoencoders to lower the dimension of the input sinograms, and apply the DDPM in latent space, similarly as in [34]" (Sec. IV, p. 14; [34] es Rombach et al.). Baselines: PUnet (convoluciones parciales) y GAN de inpainting con convoluciones gated y discriminador SN-PatchGAN.

**5. Anatomias y datasets. Incluye pelvis u osteosintesis?**
Datasets de entrenamiento: DeepLesion (NIH) y UCLH Stroke EIT Dataset. Evaluacion clinica: 4 CT del MGH, uno por region: prostata (pelvis), columna (torax), dental (cabeza) y cadera. **Pelvis: si** (Paciente 1, marcadores de oro en prostata; y el caso del Apendice es tambien pelvis con dos marcadores de oro; Paciente 4, cadera, con protesis total). **Osteosintesis (tornillos/placas de fijacion de fractura): NO ENCONTRADO EN EL PDF**; el implante mas cercano es una "steel spinal cage". No se usa CTPelvic1K ni ningun dataset de pelvis con fijacion interna.

**6. Metricas y cifras.**
Metricas estandar: SSIM, PSNR, RMSE (test N=200). Metricas clinicas: CTN_blue (cerca del metal), CTN_orange (lejos), CTN_average, RMSE_INT (dentro de la skin-line), RMSE_ROI (organo especifico), SSIM_INT, Vol_M y Vol_B. Cifras principales en la tabla "Numeros que cito de este paper" (Tablas I, II y III y p-valores del Abstract y de Sec. III-B). Resumen: DDPM 0.964 SSIM / 46.16 PSNR / 12.3 RMSE frente a NMAR 0.920 / 42.12 / 20.2; mejor en 13 de 28 metricas clinicas; pierde frente a NMAR en el caso de protesis total de cadera.

**7. Dice explicitamente que su modelo NO puede generar artefactos?**
NO ENCONTRADO EN EL PDF una frase que diga eso literalmente. Lo mas cercano son afirmaciones sobre el entrenamiento libre de metal y sobre limitaciones: "The proposed model is unconditionally trained, free from information on metal objects" (Abstract, p. 1) y "does not use any information on the metal trace during the training process" (Sec. IV, p. 13). Sobre limitaciones de los datos sinteticos si hay declaracion explicita: "the clinical scans were not derived from the same databases that were used to train the models" (Sec. IV, p. 13), usada para explicar la caida de rendimiento respecto al test simulado; y "The training dataset was obtained by randomly extracting 2-D slices from CT scans, which can potentially underrepresent views" (Sec. IV, p. 13). Tambien: "The AI methods are only limited by the representation power of the networks and the richness of the training data" (Sec. IV, p. 13).

**8. Nivel que sostiene la evidencia:**
**NIVEL 1.** Aplicando el criterio dado: el paper SI inserta metal sinteticamente (CatSim + formas metalicas transformadas + regla de colocacion >=50% sobre >200 HU) para fabricar sus pares, es decir toca directamente el terreno del renderizador y del baseline fisico de la tesis, e incluye evaluacion en pelvis y en cadera; equivocarse al describirlo comprometeria el argumento de novedad y la definicion del benchmark.

Matiz importante para la redaccion: el paper **no debilita** la implicancia #2 en cuanto al modelo generativo (su DDPM sigue siendo de remocion y se entrena sin ver metal), pero **si obliga a reformularla con precision**: la insercion de metal sintetico con simulacion fisica ya esta publicada y es rutinaria; lo no publicado, segun este PDF, es sintetizar metal y artefactos con un modelo generativo condicionado. Formular el gap como "nadie inserta metal sintetico" seria falso a la luz de este paper.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| [23] Wu M et al., "XCIST—an open access x-ray/CT simulation toolkit," Phys. Med. Biol., vol. 67, no. 19, p. 194002, Sep. 2022, doi: 10.1088/1361-6560/ac9174 | Es el baseline fisico declarado de la tesis; aqui aparece como la herramienta que sostiene la insercion de metal. Ya existe papers/wu2022xcist.pdf. |
| [24] Man BD et al., "CatSim: a new computer assisted tomography simulation environment," SPIE Medical Imaging 2007, pp. 856-863, doi: 10.1117/12.710713 | Fuente original del simulador con el que se generan los artefactos metalicos "realistas"; define el estandar contra el que se mide el renderizador. Ya existe papers/deman2007catsim.pdf. |
| [25] Fan Y, Pack J, De Man B, "A virtual imaging trial framework to study cardiac CT blooming artifacts," 2022, doi: 10.1117/12.2646407 | Es la validacion citada de que la simulacion CatSim produce artefactos realistas; fuente de la afirmacion de realismo, no verificada en este PDF. |
| [12] Meyer E, Raupach R, Lell M, Schmidt B, Kachelriess M, "Normalized metal artifact reduction (NMAR) in computed tomography," Med. Phys., vol. 37, no. 10, pp. 5482-5493, 2010 | Baseline no-AI de referencia en MAR; sigue ganando en el caso de protesis grande. Metodo competidor y fuente de umbrales de segmentacion por tejido. |
| [16] Zhang Y and Yu H, "Convolutional Neural Network Based Metal Artifact Reduction in X-Ray CT," IEEE TMI, vol. 37, no. 6, pp. 1370-1381, 2018 | Fuente del banco de formas metalicas usado para la insercion sintetica; es el origen real de la geometria de implantes de este paper. Compite con el banco de 61 geometrias de la tesis. |
| [33] Lugmayr A et al., "RePaint: Inpainting using Denoising Diffusion Probabilistic Models," arXiv, Aug. 2022 | Fuente de los hiperparametros de inferencia (T, r, j) y del esquema de resampling; cualquier cifra de inferencia citada viene de ahi. |
| [34] Rombach R et al., "High-Resolution Image Synthesis with Latent Diffusion Models," CVPR 2022 | Es la base del renderizador latente de la tesis y aqui se invoca como via de eficiencia futura. Ya existe papers/rombach2022latentdiffusion.pdf. |
| [38] Saharia C et al., "Palette: Image-to-Image Diffusion Models," SIGGRAPH 2022, doi: 10.1145/3528233.3530757 | Difusion supervisada condicionada; el propio paper la senala como la via para que el modelo aprenda rasgos especificos de la distorsion metalica. Es la ruta mas cercana a sintesis condicionada. |
| [28] Bal M and Spies L, "Metal artifact reduction in CT using tissue-class modeling and adaptive prefiltering," Med. Phys., vol. 33, no. 8, pp. 2852-2859, 2006 | Fuente original del esquema adaptativo de umbrales por clase de tejido (-1000/0 HU) que aqui se reusa. |
| [18] Gottschalk TM, Maier A, Kordon F, Kreher BW, "DL-based inpainting for metal artifact reduction for cone beam CT using metal path length information," Med. Phys., vol. 50, no. 1, pp. 128-141, 2023 | Metodo competidor que usa longitud de trayecto en el metal; podria aportar una forma de modelar la banda de influencia del metal mas alla de la mascara (relevante para B_delta). |
| [3] De Man B et al., "Metal streak artifacts in X-ray computed tomography: a simulation study," IEEE Trans. Nucl. Sci., vol. 46, no. 3, pp. 691-696, 1999 | Fuente original de los mecanismos fisicos citados (photon starvation, beam hardening, bandas oscuras); base para justificar que el artefacto se manifiesta fuera del metal. |
| [1] Giantsoudi D et al., "Metal artifacts in computed tomography for radiation therapy planning: dosimetric effects and impact of MAR," Phys. Med. Biol., vol. 62, no. 8, p. R49, 2017 | Fuente de la afirmacion de impacto clinico de los artefactos; util si la tesis necesita justificar la relevancia del problema con cifra citable. |
