# chen2026foundationvae — Foundation VAEs for 3D CT Reconstruction, Augmentation, and Generation

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. Identificador en el margen de la p. 1:
  "arXiv:2605.30893v1 [cs.CV] 29 May 2026". Codigo: https://github.com/qic999/Foundation-VAE
  (Abstract, p. 1). Venue en nota al pie p. 1: "Proceedings of the 43rd International
  Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026."
- **Nivel de lectura:** 1 (profunda) — PDF completo, 18 paginas, incluidos apendices A-D
- **Leido a fondo por la autora:** no
- **PDF:** papers/chen2026foundationvae.pdf

## Que hace (3 lineas maximo)

Usa siete VAEs de video preentrenados en imagenes/videos naturales, con encoder y decoder congelados, para reconstruir CT 3D (MSD Lung/Pancreas, LiTS, KiTS19) y usa esas reconstrucciones como aumentacion para nnU-Net.
En el latente fijo de ese VAE entrena un modelo de difusion latente condicionado por mascaras de organos/enfermedad (codificadas con el mismo encoder congelado) y por reportes radiologicos, mas un modulo de consistencia 3D.
Evalua la generacion en CT de torax (CT-RATE + ReXGroundingCT) con FVD, FID 2.5D, CT-CLIP, adherencia a mascaras y AUC de clasificacion multi-etiqueta.

## Restriccion o supuesto clave

Tres supuestos, explicitos o implicitos, que chocan con implantes metalicos y hueso denso.

1. **Rango de intensidad recortado a [-1000, 1000] HU, pero solo declarado para la
   generacion.** En la configuracion experimental de CT Generation (CT-RATE /
   ReXGroundingCT): "intensities are clipped to [−1000, 1000] HU" (§4.1, p. 5). Todo lo
   que supere 1000 HU (hueso cortical denso, metal) queda saturado antes de entrar al VAE.
   Para los experimentos de reconstruccion y aumentacion (MSD Task06/Task07, LiTS, KiTS19;
   Tablas 1-2, p. 3), que son los que sostienen el claim "without medical fine-tuning",
   el rango de recorte y la normalizacion: NO ENCONTRADO EN EL PDF.
2. **El VAE se interpreta como un denoiser que atenua alta frecuencia, y eso se presenta
   como virtud.** "the VAE bottleneck primarily attenuates weakly structured high frequency
   components" (§2, p. 3); la diferencia de reconstruccion "follows the statistics of CT
   acquisition and reconstruction noise, rather than anatomy mismatch" (§2, p. 3); y los
   errores estan "dominated by high-frequency noise and mild streak artifacts rather than
   boundary shifts" (Fig. 2, p. 2). Para la tesis el streaking ES la senal a sintetizar:
   un autoencoder que lo trata como ruido a suprimir es un riesgo directo para la banda
   B_delta.
3. **Calidad medida por fronteras, no por fidelidad de intensidad.** El criterio de exito
   es preservar geometria relevante para segmentacion: el supuesto teorico "requires
   preservation of task relevant structure, rather than perfect pixel fidelity" (Apendice
   A, p. 12). No hay MAE, ni error en HU, ni ROI por tejido (hueso, metal): NO ENCONTRADO
   EN EL PDF. Las unidades de PSNR/SSIM/MSE no se declaran.

## Que toco de aqui

- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Recorte [-1000, 1000] HU (solo generacion, CT-RATE) | "intensities are clipped to [−1000, 1000] HU" | §4.1, p. 5 |
| Resolucion 512 x 512, 100-600 slices | "resampled to 512 × 512 per slice (100–600 slices per volume)" | §4.1, p. 5 |
| 7 VAEs de video, sin adaptacion medica | "apply them to 3D CT volumes without medical adaptation" | Apendice B, p. 13 |
| Encoder y decoder congelados | "With both encoder and decoder frozen, the Foundation VAE reconstructs CT volumes" | Abstract, p. 1 |
| Error dominado por ruido y streaks leves | "Errors are dominated by high-frequency noise and mild streak artifacts" | Fig. 2, p. 2 |
| Mejor PSNR/SSIM/MSE en Lung (IVVAE) | Tabla 1: "31.78 ± 4.11", "0.79 ± 0.10", "64.39 ± 45.95" | Tabla 1, p. 3 |
| +3.9% NSD por aumentacion | "average gain of 3.9% NSD on pancreatic tumor and lung tumor" | §1, p. 2 |
| Compresion 8x8x4 (mayoria) y 16x16x4 (WAN2.2) | Tabla 8: "8×8×4" ; "16×16×4" | Tabla 8, p. 14 |

## Donde entra en mi tesis

- **Objetivo 1 (codificacion multi-ventana en HU, Go/No-Go MAE < 25 HU en hueso > 150 HU).**
  Es el antecedente que parece contradecir el experimento E6b (VAE de SD 1.5 congelado
  falla 178/178). La lectura del PDF muestra que no son comparables: (a) el unico recorte
  declarado es [-1000, 1000] HU y solo para generacion; (b) no se reporta error en HU ni
  por tejido; (c) no hay pelvis ni metal; (d) no se evaluan VAEs de imagen 2D tipo SD.
  Sirve para la seccion de Related Work / justificacion del Objetivo 1 como contraste:
  la transferencia "sin fine-tuning" se valida con PSNR/SSIM/segmentacion en torax/abdomen,
  no con fidelidad de HU en hueso denso.
- **Renderizador y B_delta.** La afirmacion de que el VAE congelado actua como
  "boundary-preserving denoiser" y atenua componentes de alta frecuencia incluyendo
  "mild streak artifacts" (Fig. 2, p. 2) es un argumento a favor de verificar que el
  autoencoder del renderizador no borre el streaking que la banda B_delta debe producir.
- **Condicionamiento por mascara codificada con el mismo encoder** (§3.1, p. 4): alternativa
  de diseno a ControlNet para inyectar la mascara del implante; solo contexto.

## Dudas para el asesor

1. El claim "without medical fine-tuning" se apoya en Tablas 1-2 (MSD, LiTS, KiTS19), cuyo
   preprocesamiento de intensidad no se declara. El recorte [-1000, 1000] HU aparece solo en
   §4.1 para CT-RATE. Basta citar el recorte de §4.1 como explicacion de la discrepancia con
   E6b, o hay que marcar el rango de reconstruccion como no verificable?
2. Unidades de MSE/PSNR no declaradas. Observacion de la extractora (aritmetica sobre valores
   del PDF, no afirmada por el paper): MSE de 77.97 (WAN2.1, Lung, Tabla 1) es imposible si la
   imagen estuviera en [0,1] o [-1,1] sin reescalar, porque el error cuadratico maximo seria
   1 o 4. La escala real es desconocida.
3. Inconsistencia interna: la Introduccion dice que MedVAE cae a "PSNR dropping to 20.34 and
   SSIM to 0.52 on Lung" y "MSE exceeding 600 and 1000" (§1, p. 1), pero la Tabla 1 (p. 3)
   reporta para MedVAE 30.06 / 0.74 / 88.36 (Lung) y 36.00 / 0.91 / 17.98 (Pancreas).
   Tambien WAN2.1 y WAN2.2 tienen valores identicos en Lung (Tabla 1). Se cita alguna cifra
   de reconstruccion con esta incertidumbre?
4. El numero de clases de mascara no es consistente: "masks for 124 anatomical structures"
   (§3.1, p. 4), "126 classes in total" (Apendice C, p. 14), "124 classes, excluding
   background" (Tabla 10, p. 15).
5. No se nombra cual de los siete VAEs es "la" Foundation VAE usada en generacion (Tablas 3,
   6, 7). Tampoco como se mapea un volumen CT monocanal a la entrada RGB/temporal de un VAE
   de video. Sin eso, el resultado no es reproducible como argumento contra E6b.
6. La Tabla 6 compara con FID 2.19 / 4.78, que coinciden con la columna Axial de la Tabla 3,
   no con el promedio (2.29 / 4.35). No afecta a la tesis, pero conviene no citar la Tabla 6
   como "FID promedio".

## Evidencia textual

| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Venue | "Proceedings of the 43rd International Conference on Machine Learning, Seoul, South Korea" | Nota al pie, p. 1 |
| Identificador arXiv | "arXiv:2605.30893v1 [cs.CV] 29 May 2026" | Margen, p. 1 |
| Codigo | "https://github.com/qic999/Foundation-VAE" | Abstract, p. 1 |
| Claim central: encoder y decoder congelados | "With both encoder and decoder frozen, the Foundation VAE reconstructs CT volumes" | Abstract, p. 1 |
| Claim: supresion de ruido de adquisicion | "reconstructs CT volumes with preserved anatomy while suppressing acquisition noise" | Abstract, p. 1 |
| Claim: sin fine-tuning medico | "transferred as a general CT interface without medical fine-tuning" | §1, p. 2 |
| Nunca expuesto a datos medicos | "Although E and D are never exposed to medical data" | §2, p. 3 |
| Sin adaptacion medica (Apendice B) | "apply them to 3D CT volumes without medical adaptation" | Apendice B, p. 13 |
| Numero de VAEs de video | "We consider seven publicly released video VAEs as candidate Foundation VAE backbones" | Apendice B, p. 13 |
| Operador de reconstruccion | "x̃ := T(x) = D(E(x))" (Ec. 1) | §2, p. 3 |
| Mejora NSD por aumentacion | "yields an average gain of 3.9% NSD on pancreatic tumor and lung tumor" | §1, p. 2 |
| Mejora FVD y CT-CLIP (abstract) | "achieves 3.9% lower average FVD with 36.2% higher CT CLIP score" | Abstract, p. 1 |
| Mejora AUC multi-enfermedad | "improves multi-disease generation faithfulness across 18 types by 2.76% AUC" | Abstract, p. 1 |
| Colapso de MedVAE en Lung (texto) | "with PSNR dropping to 20.34 and SSIM to 0.52 on Lung" | §1, p. 1 |
| Colapso de MedVAE en Pancreas (texto) | "PSNR 18.78 with SSIM 0.33 on Pancreas, alongside MSE exceeding 600 and 1000" | §1, p. 1 |
| Costo de entrenar MAISI | "using 37,243 CT volumes, 8 32G V100 GPUs, and 300 epochs" | §1, p. 2 |
| Parches de MAISI | "multi stage patch cropping from [64, 64, 64] to [128, 128, 128]" | §1, p. 2 |
| Origen del error de reconstruccion | "Errors are dominated by high-frequency noise and mild streak artifacts rather than boundary shifts" | Fig. 2, p. 2 |
| Interpretacion como denoiser | "consistent with T(·) acting as a boundary-preserving denoiser" | Fig. 2, p. 2 |
| Datasets de reconstruccion (Fig. 2) | "on MSD (Antonelli et al., 2022) Task06 Lung and Task07 Pancreas" | Fig. 2, p. 2 |
| Discrepancia = ruido, no anatomia | "follows the statistics of CT acquisition and reconstruction noise, rather than anatomy mismatch" | §2, p. 3 |
| Donde se concentra el error | "concentrate on grain like fluctuations in low contrast soft tissue regions" | §2, p. 3 |
| Cuello de botella atenua alta frecuencia | "the VAE bottleneck primarily attenuates weakly structured high frequency components" | §2, p. 3 |
| Metrica resumen de desviacion | "the deviation between x and x̃ is consistently summarized by voxel wise MSE" | §2, p. 3 |
| Metricas de Tabla 1 (sin unidades) | "Reconstruction performance across four CT datasets" ; columnas PSNR↑, SSIM↑, MSE↓ | Tabla 1, p. 3 |
| Tabla 1 WAN2.1 (Lung PSNR/SSIM/MSE; Pancreas PSNR/SSIM/MSE; LiTS PSNR/SSIM; KiTS19 PSNR/SSIM) | "30.93±4.06, 0.76±0.10, 77.97±55.12; 39.18±1.38, 0.94±0.02, 8.58±2.93; 39.32±1.69, 0.93±0.03; 40.22±1.68, 0.94±0.03" | Tabla 1, p. 3 |
| Tabla 1 WAN2.2 | "30.93±4.06, 0.76±0.10, 77.97±55.12; 39.06±1.50, 0.95±0.02, 8.99±3.31; 39.25±1.84, 0.94±0.03; 40.32±1.84, 0.95±0.03" | Tabla 1, p. 3 |
| Tabla 1 VideoVAE+ | "30.94±4.35, 0.77±0.11, 80.43±59.08; 40.12±1.66, 0.95±0.02, 7.00±3.05; 39.92±1.97, 0.95±0.03; 41.07±1.91, 0.96±0.03" | Tabla 1, p. 3 |
| Tabla 1 IVVAE | "31.78±4.11, 0.79±0.10, 64.39±45.95; 40.43±1.54, 0.96±0.02, 6.45±2.52; 40.33±1.89, 0.95±0.02; 41.38±1.90, 0.96±0.03" | Tabla 1, p. 3 |
| Tabla 1 CVVAE | "29.61±3.27, 0.75±0.11, 93.91±57.96; 35.34±0.90, 0.93±0.02, 20.87±4.14; 36.46±1.19, 0.93±0.03; 36.63±1.61, 0.93±0.03" | Tabla 1, p. 3 |
| Tabla 1 WFVAE | "30.98±4.29, 0.78±0.10, 79.23±58.11; 39.53±1.43, 0.95±0.02, 7.99±2.83; 40.04±1.79, 0.95±0.02; 40.79±1.81, 0.96±0.03" | Tabla 1, p. 3 |
| Tabla 1 LeanVAE | "30.66±4.33, 0.78±0.10, 86.29±62.76; 39.29±1.44, 0.95±0.02, 8.50±3.10; 39.64±1.78, 0.95±0.03; 40.53±1.80, 0.95±0.03" | Tabla 1, p. 3 |
| Tabla 1 MedVAE (referencia medica) | "30.06±3.60, 0.74±0.11, 88.36±59.05; 36.00±1.13, 0.91±0.03, 17.98±5.78; 34.11±5.13, 0.85±0.11; 33.76±7.17, 0.91±0.06" | Tabla 1, p. 3 |
| Tabla 1 MAISI (referencia medica) | "29.78±2.99, 0.73±0.09, 86.25±54.54; 36.97±0.92, 0.93±0.02, 13.88±3.09; 37.35±1.23, 0.92±0.02; 37.08±1.30, 0.92±0.03" | Tabla 1, p. 3 |
| Claim comparativo de reconstruccion | "off the shelf video VAEs achieve reconstruction quality comparable to a CT specific VAE" | §2, p. 3 |
| Segmentador downstream | "Segmentation performance of nnU-Net trained on data reconstructed by each VAE" | Tabla 2, p. 3 |
| Tabla 2 indices de clase | "indices 1 and 2 denote organ and tumor/lesion classes respectively" | Tabla 2, p. 3 |
| Tabla 2 Real Data (Lung DSC/NSD; Pancreas DSC1/NSD1/DSC2/NSD2; LiTS DSC1/DSC2; KiTS19 DSC1/DSC2) | "66.4±29.2, 70.2±31.6; 82.2±8.0, 79.2±9.6, 42.8±32.8, 39.8±32.4; 94.7±5.3, 57.2±27.8; 95.5±3.9, 83.2±19.1" | Tabla 2, p. 3 |
| Tabla 2 WAN2.1 | "71.9±24.7, 75.3±28.7; 82.2±8.0, 79.0±10.2, 45.2±31.9, 41.9±31.9; 94.3±6.7, 57.1±29.3; 95.4±4.4, 83.6±18.2" | Tabla 2, p. 3 |
| Tabla 2 WAN2.2 | "70.2±20.9, 72.9±24.2; 82.0±8.1, 79.0±9.5, 47.2±31.7, 45.0±31.8; 95.1±4.9, 60.8±26.8; 96.0±3.5, 85.0±15.6" | Tabla 2, p. 3 |
| Tabla 2 VideoVAE+ | "68.0±21.3, 72.6±24.2; 82.2±8.3, 79.3±10.0, 47.1±32.7, 44.7±32.2; 94.8±5.1, 58.2±26.9; 95.7±3.6, 83.6±18.7" | Tabla 2, p. 3 |
| Tabla 2 IVVAE | "70.2±20.5, 73.3±24.0; 82.0±8.3, 78.5±10.4, 47.2±31.8, 44.3±32.3; 95.3±4.7, 61.6±26.4; 95.7±3.5, 83.8±18.7" | Tabla 2, p. 3 |
| Tabla 2 CVVAE | "67.0±26.7, 70.9±29.2; 79.4±9.2, 74.7±10.4, 36.7±31.3, 34.5±28.8; 93.5±8.1, 52.4±29.6; 94.5±4.0, 78.8±23.3" | Tabla 2, p. 3 |
| Tabla 2 WFVAE | "68.0±27.4, 71.3±29.0; 81.3±8.4, 77.9±10.8, 46.9±30.2, 44.4±30.2; 95.1±4.4, 59.5±27.0; 95.4±4.3, 85.5±14.7" | Tabla 2, p. 3 |
| Tabla 2 LeanVAE | "69.2±21.6, 72.5±24.7; 82.0±8.0, 78.6±10.1, 44.1±32.8, 41.9±31.7; 94.9±5.0, 59.4±26.5; 95.5±4.4, 83.7±16.3" | Tabla 2, p. 3 |
| Tabla 2 MedVAE | "71.5±19.3, 74.7±23.6; 80.7±8.7, 77.0±10.7, 42.4±33.6, 40.5±33.4; 94.3±6.0, 57.4±28.0; 94.8±3.5, 77.9±25.4" | Tabla 2, p. 3 |
| Tabla 2 MAISI | "71.0±19.5, 74.5±21.0; 80.3±8.7, 75.8±10.5, 35.0±31.9, 32.0±30.2; 93.6±7.7, 38.5±34.5; 94.4±5.2, 79.5±22.5" | Tabla 2, p. 3 |
| Protocolo de aumentacion | "we train the segmenter directly on (x̃, y), using the reconstruction as the primary training view" | §2, p. 3 |
| Supuesto teorico: estabilidad | "This assumption requires preservation of task relevant structure, rather than perfect pixel fidelity" | Apendice A, p. 12 |
| Teorema 1: cota de riesgo | "R_P(θ̂) − R_P(θ⋆) ≤ 2Lℓεφ" (Ec. 15) | Apendice A, p. 12 |
| Definicion de NSD y tolerancia | "τ is the tolerance (in voxels or millimeters)" | Apendice A.1, p. 13 |
| Proxy empirico de distorsion | "A smaller ε̂φ means higher segmentation consistency" (Ec. 26) | Apendice A.1, p. 13 |
| VAE congelado en generacion | "We keep the Foundation VAE encoder E and decoder D frozen" | §3, p. 4 |
| Perdida de difusion | "L = E[ ‖ε − εθ([zt; zm], r, t)‖² ]" (Ec. 4) | §3, p. 4 |
| Mascaras de organos | "which provides masks for 124 anatomical structures" | §3.1, p. 4 |
| Mascara codificada con el mismo encoder | "we encode the mask volume with the same frozen Foundation VAE encoder" | §3.1, p. 4 |
| Condicionamiento por concatenacion | "we concatenate zm with the noised latent zt along the channel dimension" | §3.1, p. 4 |
| Text encoder congelado | "using a frozen text encoder τ(·) to obtain text embeddings" | §3.1, p. 4 |
| Modulo 3D: inicializacion | "The kernel is initialized as a Dirac delta (identity mapping)" | §3.2, p. 4 |
| Datasets de generacion | "CT-RATE (Ai et al., 2024) and ReXGroundingCT (Baharoon et al., 2025) are used" | §4.1, p. 4 |
| Tamano total | "the dataset contains 4,961 training volumes and 80 test volumes" | §4.1, p. 4 |
| Subconjunto normal | "2,395 no-disease training volumes and 30 no-disease test volumes" | §4.1, p. 4 |
| Subconjunto enfermo (train) | "2,566 diseased training volumes with 6,342 disease masks" | §4.1, p. 4 |
| Subconjunto enfermo (test) | "a diseased test set of 50 volumes with 297 disease masks" | §4.1, pp. 4-5 |
| Split downstream | "500 training volumes and 200 test volumes are additionally sampled from CT-RATE" | §4.1, p. 5 |
| Resolucion | "All volumes are resampled to 512 × 512 per slice (100–600 slices per volume)" | §4.1, p. 5 |
| **Recorte de intensidad (generacion)** | "intensities are clipped to [−1000, 1000] HU" | §4.1, p. 5 |
| Definicion FVD | "computed on features extracted by the CT-CLIP vision encoder" | §4.1, p. 5 |
| Criterio FVD | "Lower values indicate better 3D coherence" | §4.1, p. 5 |
| Definicion FID 2.5D | "encoded by a fixed RadImageNet ResNet-50" | §4.1, p. 5 |
| Definicion CT-CLIP | "by cosine similarity for image-to-image (I2I) and text-to-image (T2I) retrieval" | §4.1, p. 5 |
| Criterio CT-CLIP | "Higher scores indicate text–image consistency and greater anatomical and pathology fidelity" | §4.1, p. 5 |
| Tabla 3 Normal GenerateCT (FVD; FID Ax/Sag/Cor/Avg; CT-CLIP I2I/T2I/Avg; Mem; Tiempo) | "0.5738; 12.53/18.59/15.09/15.40; 3.40/1.30/2.35; 80G; 230s (512×512×201)" | Tabla 3, p. 6 |
| Tabla 3 Normal MedSyn | "0.7048; 10.37/13.97/12.16/12.17; 22.99/27.80/25.40; 7G; 180s (256×256×256)" | Tabla 3, p. 6 |
| Tabla 3 Normal MAISI | "0.4444; 6.76/7.17/10.55/8.16; –; 30G; 590s (512×512×128)" | Tabla 3, p. 6 |
| Tabla 3 Normal Ours | "0.3035; 2.19/2.32/2.36/2.29; 76.48/42.23/59.35; 22G; 190s (512×512×128)" | Tabla 3, p. 6 |
| Tabla 3 Disease GenerateCT | "0.8265; 14.50/26.11/26.19/22.26; 13.26/6.83/10.05; 80G; 230s" | Tabla 3, p. 6 |
| Tabla 3 Disease MedSyn | "0.6318; 7.69/12.13/8.87/9.56; 14.35/11.66/13.01; 7G; 180s" | Tabla 3, p. 6 |
| Tabla 3 Disease MAISI | "0.6433; 4.79/6.11/8.44/6.45; –; 30G; 590s" | Tabla 3, p. 6 |
| Tabla 3 Disease Ours | "0.5088; 4.78/4.11/4.17/4.35; 59.24/43.73/51.49; 22G; 190s" | Tabla 3, p. 6 |
| Resumen generacion (normal) | "reaching FVD 0.30 and FID_Avg 2.29 under no-disease prompts" | §4.2, p. 6 |
| Resumen generacion (enfermedad) | "coherence under disease prompts with FVD 0.51 and FID_Avg 4.35" | §4.2, p. 6 |
| CT-CLIP resumen | "CT-CLIP Avg scores of 59.35 for no-disease prompts and 51.49 for disease prompts" | §4.2, p. 6 |
| Adherencia a mascara: metodo | "applying pre-trained VISTA3D and TotalSegmentator to segment lungs, heart, pulmonary vessels, and ribs" | §4.4, p. 7 |
| Tabla 4 MAISI (Lung Dice/IoU; Heart; Vessel; Rib) | "75.94/62.97; 66.86/52.20; 13.50/7.27; 15.20/8.88" | Tabla 4, p. 7 |
| Tabla 4 Ours | "79.48/75.46; 80.36/77.09; 63.38/48.11; 70.23/61.40" | Tabla 4, p. 7 |
| Vasos | "For vessels, Dice increases from 13.50 to 63.38" | §4.4, p. 7 |
| Costillas | "for ribs from 15.20 to 70.23" | §4.4, p. 7 |
| Limitacion: vasos finos | "Vessel structures remain the most challenging, with occasional loss of fine branches" | §4.4, p. 7 |
| Baseline de clasificacion | "achieving a mean AUC of 67.95" | §4.5, p. 7 |
| Datos sinteticos para clasificacion | "we generate 500 synthetic CT volumes and fine-tune the classifier" | §4.5, p. 7 |
| Mejora AUC | "improves the mean AUC to 70.71, corresponding to a +2.76 absolute gain" | §4.5, p. 7 |
| Tabla 5 Real (ArtCal, Atel, Cardio, CorCal, Emph, Hernia, Lymph, MedMat, Nodule, PeriEf) | "71.53, 55.67, 76.73, 69.72, 66.23, 58.27, 71.00, 75.44, 61.39, 79.42" | Tabla 5, p. 8 |
| Tabla 5 Real (Bronch, Cons, FibSeq, Mosaic, Opacity, PeriTh, PleEf, SeptTh, Avg) | "52.32, 69.06, 65.74, 63.38, 66.69, 64.14, 79.13, 77.25, 67.95" | Tabla 5, p. 8 |
| Tabla 5 +1xMedSyn (primer bloque) | "74.65, 67.66, 76.58, 70.18, 62.55, 63.99, 74.50, 81.27, 63.98, 77.32" | Tabla 5, p. 8 |
| Tabla 5 +1xMedSyn (segundo bloque) | "50.03, 71.06, 59.69, 63.82, 75.55, 60.61, 83.41, 77.77, 69.70 (+1.75)" | Tabla 5, p. 8 |
| Tabla 5 +1xGenerateCT (primer bloque) | "70.77, 68.31, 73.13, 71.24, 67.27, 63.92, 74.63, 80.24, 67.80, 75.24" | Tabla 5, p. 8 |
| Tabla 5 +1xGenerateCT (segundo bloque) | "53.63, 72.59, 61.55, 55.46, 74.84, 62.64, 82.70, 80.47, 69.80 (+1.85)" | Tabla 5, p. 8 |
| Tabla 5 +1xOurs (primer bloque) | "76.99, 61.94, 82.06, 72.84, 68.64, 64.38, 73.81, 79.38, 65.70, 76.41" | Tabla 5, p. 8 |
| Tabla 5 +1xOurs (segundo bloque) | "56.99, 70.00, 66.09, 61.72, 72.09, 63.78, 82.61, 77.25, 70.71 (+2.76)" | Tabla 5, p. 8 |
| Abreviatura MedMat | "MedMat = Medical material" | Tabla 5, p. 8 |
| Ablacion del VAE: diseno | "the Foundation VAE is replaced with MedVAE (Varma et al., 2025a)" | §4.6, p. 8 |
| Tabla 6 Normal (FID; CT-CLIP) | "MedVAE 11.28, 20.76; Foundation VAE 2.19, 59.35" | Tabla 6, p. 8 |
| Tabla 6 Disease | "MedVAE 10.54, 15.32; Foundation VAE 4.78, 51.49" | Tabla 6, p. 8 |
| Resumen ablacion | "CT-CLIP improves by over 30 points in both cases" | §4.6, p. 8 |
| Tabla 7 organ mask sola (FVD; FID_Avg; CT-CLIP_Avg) | "0.5172; 3.72; 43.40" | Tabla 7, p. 9 |
| Tabla 7 + single disease mask + single prompt | "0.4805; 3.76; 46.14" | Tabla 7, p. 9 |
| Tabla 7 + multi disease mask + multi prompt | "0.5088; 4.35; 51.49" | Tabla 7, p. 9 |
| Claim de related work | "Evaluating seven recent video VAEs, we find that their latent spaces" | §5.1, p. 9 |
| Limitacion: calidad de mascara | "controllability depends on conditioning mask quality" | §6, p. 9 |
| Limitacion: casos raros | "rare disease categories and long-tail co-occurrences remain challenging" | §6, p. 9 |
| **Limitacion: sensibilidad al preprocesamiento** | "automated metrics are sensitive to preprocessing and segmentation model bias" | §6, p. 9 |
| Limitacion: dependencia institucional | "Training data may also encode institution-specific characteristics" | §6, p. 9 |
| Alcance declarado de los resultados | "interpreted as evidence of feasibility rather than a guarantee of universal performance" | §6, p. 9 |
| Uso no clinico | "The approach is not intended for diagnostic or clinical decision-making" | Impact Statement, p. 10 |
| Tabla 8 WAN2.1 (Comp; C; Latente; Total; Rel.) | "8×8×4; 16; 16×64×64×4; 262,144; 4.0×" | Tabla 8, p. 14 |
| Tabla 8 WAN2.2 | "16×16×4; 48; 48×32×32×4; 196,608; 3.0×" | Tabla 8, p. 14 |
| Tabla 8 VideoVAE+ | "8×8×4; 4; 4×64×64×4; 65,536; 1.0×" | Tabla 8, p. 14 |
| Tabla 8 IVVAE | "8×8×4; 16; 16×64×64×4; 262,144; 4.0×" | Tabla 8, p. 14 |
| Tabla 8 CVVAE | "8×8×4; 4; 4×64×64×4; 65,536; 1.0×" | Tabla 8, p. 14 |
| Tabla 8 WFVAE | "8×8×4; 8; 8×64×64×4; 131,072; 2.0×" | Tabla 8, p. 14 |
| Tabla 8 LeanVAE | "8×8×4; 4; 4×64×64×4; 65,536; 1.0×" | Tabla 8, p. 14 |
| Tabla 8 MedVAE | "4×4×4; 1; 1×128×128×4; 65,536; 1.0×" | Tabla 8, p. 14 |
| Tabla 8 MAISI | "4×4×4; 4; 4×128×128×4; 262,144; 4.0×" | Tabla 8, p. 14 |
| Claim de tamano latente | "VideoVAE+, CVVAE, and LeanVAE match MedVAE in total latent size" | Tabla 8, p. 14 |
| Mascaras VISTA3D | "(127-class organ and lesion segmentation)" | Apendice C, p. 14 |
| Clases finales | "resulting in 126 classes in total" | Apendice C, p. 14 |
| Clases en Tabla 10 | "Organ label indices used in this work (124 classes, excluding background)" | Tabla 10, p. 15 |
| Split en Apendice C | "4,961 training cases and 80 validation cases across 18 disease categories" | Apendice C, p. 14 |
| Hardware | "Generative inference is performed on NVIDIA B200 GPUs" | Apendice C, p. 14 |
| Hardware downstream | "downstream evaluations are conducted on NVIDIA A100 GPUs" | Apendice C, p. 14 |
| Tabla 9 (Generativo train/test; Downstream train/test): Normal | "2,395 / 30 / 103 / 23" | Tabla 9, p. 15 |
| Tabla 9 Arterial wall calcification; Atelectasis; Bronchiectasis | "308/4/51/87; 571/11/90/75; 234/3/36/27" | Tabla 9, p. 15 |
| Tabla 9 Cardiomegaly; Consolidation; Coronary artery wall calcification | "111/3/20/40; 490/7/71/64; 291/7/55/81" | Tabla 9, p. 15 |
| Tabla 9 Emphysema; Hiatal hernia; Interlobular septal thickening | "411/9/71/58; 9/0/1/37; 154/3/29/24" | Tabla 9, p. 15 |
| Tabla 9 Lung nodule; Lung opacity; Lymphadenopathy | "1301/31/207/119; 1096/21/161/120; 475/9/73/82" | Tabla 9, p. 15 |
| Tabla 9 Medical material | "195 / 4 / 40 / 27" | Tabla 9, p. 15 |
| Tabla 9 Mosaic; Peribronchial thickening; Pericardial effusion | "101/1/11/22; 184/3/29/33; 116/4/29/26" | Tabla 9, p. 15 |
| Tabla 9 Pleural effusion; Pulmonary fibrotic sequela; Total | "200/4/45/43; 574/10/87/73; 4,961/80/500/200" | Tabla 9, p. 15 |
| Etiquetas oseas pelvicas presentes en la lista de mascaras | Tabla 10: "sacrum 97", "left hip 95", "right hip 96", "vertebrae S1 127" | Tabla 10, p. 15 |
| Fallo multi-mascara | "the model may ignore one of the input masks" | Apendice D, p. 16 |
| Fallo en hallazgos pequenos | "synthesizing small-scale findings, such as pulmonary nodules, remains challenging" | Apendice D, p. 16 |
| DOI | NO ENCONTRADO EN EL PDF | — |
| Rango HU / recorte en experimentos de reconstruccion y aumentacion (MSD Task06/Task07, LiTS, KiTS19) | NO ENCONTRADO EN EL PDF (el unico recorte declarado es el de §4.1, para CT-RATE) | — |
| Normalizacion de intensidad antes del encoder ([0,1], [-1,1] u otra) | NO ENCONTRADO EN EL PDF | — |
| Unidades / escala de MSE, PSNR (data range) y SSIM | NO ENCONTRADO EN EL PDF | — |
| MAE o cualquier error expresado en HU | NO ENCONTRADO EN EL PDF | — |
| Evaluacion por ROI de tejido (hueso, umbral en HU, metal) | NO ENCONTRADO EN EL PDF | — |
| Datos de pelvis o CT con implantes metalicos (como objeto de evaluacion) | NO ENCONTRADO EN EL PDF (solo aparece la categoria "Medical material" de CT-RATE, sin definir) | — |
| VAEs de imagen 2D (p. ej. Stable Diffusion) evaluados | NO ENCONTRADO EN EL PDF (solo 7 VAEs de video + MedVAE y MAISI) | — |
| Adaptacion de canales (CT monocanal a entrada de VAE de video) | NO ENCONTRADO EN EL PDF | — |
| Mapeo del eje de slices a la dimension temporal del VAE de video | NO ENCONTRADO EN EL PDF | — |
| Cual de los siete VAEs es la "Foundation VAE" usada en generacion (Tablas 3, 6, 7) | NO ENCONTRADO EN EL PDF | — |
| Resolucion, spacing y tamano de entrada en los experimentos de reconstruccion | NO ENCONTRADO EN EL PDF | — |
| Valor de la tolerancia τ del NSD | NO ENCONTRADO EN EL PDF | — |
| Definicion del hallazgo "Medical material" | NO ENCONTRADO EN EL PDF | — |
| Evaluacion con lectores humanos / radiologos | NO ENCONTRADO EN EL PDF | — |
| HD95 / Hausdorff | NO ENCONTRADO EN EL PDF | — |
| Hiperparametros del difusor (pasos T, scheduler, text encoder concreto) | NO ENCONTRADO EN EL PDF | — |
| Limitacion explicita sobre rango dinamico o estructuras de alta intensidad | NO ENCONTRADO EN EL PDF | — |
