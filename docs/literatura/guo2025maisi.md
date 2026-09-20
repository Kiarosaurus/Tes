# guo2025maisi — MAISI: Medical AI for Synthetic Imaging

- **DOI / URL:** 10.1109/WACV61041.2025.00435 (impreso en el PDF, p. 4430; coincide con `refs/raw/guo2025maisi.bib`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/guo2025maisi.pdf (articulo WACV 2025, pp. 4430-4441, 12 paginas de PDF: 8 de cuerpo y 4 de referencias. **El material suplementario, Secs. A, B y C, NO viene en el PDF**)

## Que hace (3 lineas maximo)
Genera volumenes CT 3D (hasta 512 x 512 x 768) con tres redes: un VAE-GAN 3D de compresion entrenado en 39,206 CT + 18,827 RM, un LDM 3D condicionado por region corporal y spacing (10,277 CT), y un ControlNet que condiciona por mascaras de 127 estructuras o por mascaras de tumor (inpainting). Introduce "tensor splitting parallelism" para caber en memoria de GPU.

## Restriccion o supuesto clave
El PDF no menciona metal, implantes, protesis, tornillos ni artefactos metalicos en ninguna parte (NO ENCONTRADO EN EL PDF). El supuesto implicito es anatomia sin hardware: el control de calidad de las muestras exige que *"the median Hounsfield Unit (HU) intensity values for major organs"* esten *"within the established normal range from training data"* (Sec. 4.1, p. 4435), y el condicionamiento del ControlNet se limita a *"segmentation masks ... or masked images and tumor masks"* (Sec. 3.3, p. 4434). **La normalizacion de intensidad del CT (rango de HU, recorte, escala) NO ENCONTRADO EN EL PDF**: el texto remite los detalles de datos y entrenamiento al suplementario (*"can be found in Supplementary Sec. A"*; *"provided in Supplementary Sec. B"*, Sec. 4.1, p. 4435), que no esta en el archivo. Por tanto el PDF no permite saber si el hueso cortical denso y el metal quedan dentro o fuera del rango.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto (por ahora: candidato a VAE de contingencia del Objetivo 1; ninguna cifra del PDF responde la compuerta)

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 39,206 CT + 18,827 RM (entrenamiento del VAE) | "comprising 39,206 3D CT volumes and 18,827 3D MRI volumes" | Sec. 3, p. 4433 |
| 37,243 / 1,963 CT (train / val del VAE) | "37,243 CT volumes for training and 1,963 CT volumes for validation" | Sec. 4.1, p. 4434 |
| Regiones CT del VAE | "covering the chest, abdomen, and head and neck regions" | Sec. 4.1, p. 4434 |
| 10,277 CT (LDM) | "trained on 10,277 CT volumes from diverse datasets" | Sec. 1, p. 4431 |
| 512 x 512 x 768 | "up to a landmark volume dimension of 512 × 512 × 768" | Abstract, p. 4430 |
| 127 estructuras (ControlNet) | "including 127 anatomical structures, as additional conditions" | Abstract, p. 4430 |
| PSNR/SSIM/LPIPS del VAE en OOD | ver Tabla 1 en Evidencia textual (sin HU, sin MAE) | Tabla 1, p. 4435 |

## Donde entra en mi tesis

### Respuestas a las 7 preguntas del encargo

1. **Arquitectura del VAE.** 3D: *"Given a CT volume x ∈ R^{H×W×D}"* y *"A 3D discriminator"* (Sec. 3.1, p. 4433); VAE con perdidas L1 + LPIPS + adversarial + KL (Ec. 1). Latente *"z ∈ R^{h×w×d} with much smaller spatial dimensions"* (Sec. 3.1). **Factor de compresion espacial: NO ENCONTRADO EN EL PDF. Canales latentes: NO ENCONTRADO EN EL PDF. Tamano de parche de entrenamiento del VAE: NO ENCONTRADO EN EL PDF.** Volumen maximo generado 512 x 512 x 768 (Abstract); spacing flexible, condicionado como vector de tres flotantes en mm (Sec. 3.2); ejemplo 0.86 x 0.86 x 0.92 mm3 (Fig. 1). Para el LDM los volumenes se remuestrean a multiplos de 128 (Sec. 4.1, p. 4435). (La ficha `chen2026foundationvae.md` atribuye a MAISI 4x4x4 y 4 canales en su Tabla 8: esa cifra es de Chen, no de este PDF.)
2. **Datos del VAE.** CT y RM: 37,243 + 1,963 CT (torax, abdomen, cabeza y cuello) y 17,887 + 940 RM (cerebro, cerebro sin craneo, torax, *"below-abdomen"*) (Sec. 4.1). **"Pelvis" como region del VAE: NO ENCONTRADO EN EL PDF** (la categoria *"lower-body"* existe solo como condicion del LDM, Sec. 3.2; el volumen de la Fig. 1 se ve hasta la pelvis, pero eso es una observacion de figura, no un dato del texto). Nombres de los datasets del VAE: NO ENCONTRADO EN EL PDF (remitido al suplementario). **Presencia de implantes metalicos en los datos: NO ENCONTRADO EN EL PDF.**
3. **Normalizacion de intensidad de CT.** **NO ENCONTRADO EN EL PDF**: ni rango de HU, ni recorte, ni escala. La unica mencion de HU es el filtro de calidad de mediana por organo (Sec. 4.1). La pregunta critica queda sin respuesta desde este documento.
4. **Metricas de reconstruccion del VAE.** Solo LPIPS, SSIM y PSNR, en tres conjuntos fuera de distribucion (MSD Task07 pancreas, MSD Task08 vasos hepaticos, BraTS18 RM T1 post-contraste), frente a VAEs dedicados entrenados en 80% y probados en el 20% restante (Tabla 1, Sec. 4.2, p. 4435). MAISI VAE: PSNR 37.266 / 36.559 / 39.003 dB, SSIM 0.978 / 0.970 / 0.977. **MAE, error en HU, error en hueso y rango de datos del PSNR: NO ENCONTRADO EN EL PDF.** En Task08 el VAE dedicado supera a MAISI en las tres metricas.
5. **Difusion y ControlNet.** Si existen. LDM 3D con U-Net condicionado en tiempo, region corporal (one-hot de 4: cabeza-cuello, torax, abdomen, *"lower-body"*) y spacing (Sec. 3.2). ControlNet entrenado con el LDM congelado; condiciones: mascaras de segmentacion de 127 estructuras, o imagen enmascarada + mascara de tumor para inpainting, pasadas por un *"compact encoder network"* al espacio latente (Sec. 3.3). **Mascara de implante: NO ENCONTRADO EN EL PDF.** El texto solo afirma que MAISI *"can be fine-tuned ... without retraining the two foundation models"* (Sec. 3.3); no hay ningun experimento con una clase nueva de alta densidad.
6. **Computo y disponibilidad.** Entrenado en *"NVIDIA V100 and A100 GPUs"* (Sec. 4.1); la memoria de 512^3 *"can still quickly reach"* el limite de una A100 80G (Sec. 3.1); VAEs dedicados de comparacion: 619 / 669 / 672 h en una V100 de 32G (Tabla 1). Limitacion declarada: *"still demand substantial computational resources"* (Sec. 5). Codigo en *"MONAI Tutorial"* y demo en *"NVIDIA NIM"* (nota al pie, p. 4430). **Horas / epocas / numero de GPUs de MAISI, tiempo y memoria de inferencia, disponibilidad explicita de pesos y licencia: NO ENCONTRADO EN EL PDF.**
7. **Metal / implantes.** No genera ni menciona CT con metal; tampoco lo declara como limitacion. Las limitaciones de Sec. 5 son sesgo demografico y costo de computo. NO ENCONTRADO EN EL PDF.

### Relevancia para la tesis
- **No resuelve la compuerta del Objetivo 1 desde el papel.** Sin rango de HU ni MAE en HU, el PSNR de 36.6-39.0 dB no se puede convertir a un error en HU en hueso >150 HU. La unica via es medir la ida y vuelta con la misma regla preinscrita (pacientes separados, MAE en hueso < 25 HU). El rango de recorte hay que leerlo del suplementario o del codigo de MONAI, y ninguno de los dos es citable hoy (no hay raw del suplementario).
- **Riesgo estructural:** es un VAE **3D** cuyo latente no es compatible con el U-Net ni con el ControlNet de SD 1.5. Adoptarlo arrastra el LDM y el ControlNet de MAISI (3D), no solo el autoencoder: cambia el renderizador 2.5D declarado y el computo. Esto choca con la contingencia registrada como "un solo VAE" y conviene que la autora lo evalúe antes de preinscribir (b).
- **Dominio de entrenamiento distinto al de CLINIC-metal:** el VAE declara torax, abdomen y cabeza-cuello; pelvis y metal no aparecen. Si el recorte fuera estrecho (como el [-1000, 1000] de Chen para generacion), MAISI tendria el mismo problema que SD en hueso denso y en el metal.
- **Precedente del renderizador:** LDM + ControlNet condicionado por mascaras en CT **3D**, con inpainting de tumor y un dataset propio de lesiones oseas (Fig. 6a). Refuerza que "ControlNet en CT" no es novedad (en linea con `zhang2025diffboost`); la novedad debe apoyarse en metal + artefacto fuera de la mascara (B_delta), que MAISI no toca.
- La mejora de Dice (Fig. 6) es downstream y queda fuera de alcance; no citar.

## Dudas para el asesor
- Contingencia MAISI como compuerta nueva: se acepta que el cambio de VAE implique cambiar tambien a su LDM/ControlNet 3D, o la contingencia solo vale si se puede usar el VAE de MAISI con un difusor 2.5D propio?
- El rango de HU esta en el suplementario / codigo, fuera del PDF. Se autoriza conseguir el suplementario (y su raw) antes de preinscribir, o se mide directamente sin conocer el recorte?
- Si el recorte de MAISI resulta cubrir hueso pero no metal (> ~3000 HU), el metal se representaria fuera del VAE (p. ej., reinsercion por mascara)? Eso toca el diseno del renderizador.

## Evidencia textual

| # | Dato | Frase original (<= 15 palabras) | Seccion / pagina |
|---|---|---|---|
| 1 | Volumen maximo | "up to a landmark volume dimension of 512 × 512 × 768" | Abstract, p. 4430 |
| 2 | Spacing del ejemplo | "voxel spacing of 0.86 × 0.86 × 0.92 mm3" | Fig. 1, p. 4430 |
| 3 | Estructuras del ControlNet | "including 127 anatomical structures, as additional conditions" | Abstract, p. 4430 |
| 4 | Codigo | "The code is available at MONAI Tutorial." | Nota al pie, p. 4430 |
| 5 | Demo | "The online demo is available at NVIDIA NIM." | Nota al pie, p. 4430 |
| 6 | CT del VAE | "(i.e., 39,206 3D CT volumes)" | Sec. 1, p. 4431 |
| 7 | CT del LDM | "The latent diffusion model is trained on 10,277 CT volumes" | Sec. 1, p. 4431 |
| 8 | Reclamo de novedad | "MAISI is the first attempt to generate realistic 3D CT images larger than 512^3 voxels" | Sec. 1, p. 4431 |
| 9 | Tres redes | "three 3D networks including two foundation models" | Sec. 1, p. 4431 |
| 10 | Perdidas del VAE | "L1 loss, LPIPS loss, KL loss, Adv loss" | Fig. 2, p. 4432 |
| 11 | CT + RM del VAE | "comprising 39,206 3D CT volumes and 18,827 3D MRI volumes" | Sec. 3, p. 4433 |
| 12 | Tipo de VAE | "the volume compression network (i.e., VAE-GAN [50])" | Sec. 3, p. 4433 |
| 13 | Perdidas | "perceptual loss Lpips, adversarial loss Ladv, and L1 reconstruction loss" | Sec. 3.1, p. 4433 |
| 14 | KL | "adding Kullback-Leibler (KL) regularization Lreg toward a standard normal" | Sec. 3.1, p. 4433 |
| 15 | Entrada 3D | "Given a CT volume x ∈ R^{H×W×D} in grayscale voxel space" | Sec. 3.1, p. 4433 |
| 16 | Latente | "latent representation z = E(x) ∈ R^{h×w×d} with much smaller spatial dimensions" | Sec. 3.1, p. 4433 |
| 17 | Discriminador | "A 3D discriminator, denoted as C" | Sec. 3.1, p. 4433 |
| 18 | Limite de memoria | "can still quickly reach the hardware limitation of modern GPUs (e.g., NVIDIA A100 80G)" | Sec. 3.1, p. 4433 |
| 19 | Ventana deslizante | "the direct adaptation of sliding window inference is not self-sufficient" | Sec. 3.1, p. 4433 |
| 20 | TSP | "Feature maps are first partitioned into smaller segments with overlaps" | Fig. 3, p. 4433 |
| 21 | Backbone | "The neural backbone εθ is defined as a time-conditional U-Net" | Sec. 3.2, p. 4434 |
| 22 | Region corporal | "4-dimensional one-hot vectors for head-neck, chest, abdomen, and lower-body regions" | Sec. 3.2, p. 4434 |
| 23 | Origen de la region | "either through segmentation ground truth or predated segmentation masks" | Sec. 3.2, p. 4434 |
| 24 | Spacing como condicion | "three float numbers representing the physical size of each voxel" | Sec. 3.2, p. 4434 |
| 25 | Condiciones del ControlNet | "segmentation masks for conditional generation based on masks, or masked images and tumor masks" | Sec. 3.3, p. 4434 |
| 26 | Codificador de condicion | "we employ a compact encoder network to transform the additional condition" | Sec. 3.3, p. 4434 |
| 27 | LDM congelado | "it is trained with the frozen latent diffusion model" | Sec. 3.3, p. 4434 |
| 28 | Ajuste sin reentrenar | "without retraining the two foundation models" | Sec. 3.3, p. 4434 |
| 29 | Split CT del VAE | "37,243 CT volumes for training and 1,963 CT volumes for validation" | Sec. 4.1, p. 4434 |
| 30 | Regiones CT del VAE | "covering the chest, abdomen, and head and neck regions" | Sec. 4.1, p. 4434 |
| 31 | Split RM del VAE | "17,887 MRI volumes for training and 940 MRI volumes for validation" | Sec. 4.1, p. 4434 |
| 32 | Regiones RM | "spanning the brain, skull-stripped brain, chest, and below-abdomen regions" | Sec. 4.1, p. 4434 |
| 33 | RM a futuro | "to potentially support MRI modality in future work" | Sec. 4.1, p. 4434 |
| 34 | Remuestreo | "we resample the dimensions of volumes to the multiples of 128" | Sec. 4.1, p. 4435 |
| 35 | Mascaras del ControlNet | "segmentation masks with 127 anatomical structures are derived from annotated ground truth or pre-trained models" | Sec. 4.1, p. 4435 |
| 36 | Detalles de datos fuera del PDF | "can be found in Supplementary Sec. A" | Sec. 4.1, p. 4435 |
| 37 | Frameworks | "We implement all networks using PyTorch [2] and MONAI [6]" | Sec. 4.1, p. 4435 |
| 38 | GPUs | "The models are trained using the NVIDIA V100 and A100 GPUs." | Sec. 4.1, p. 4435 |
| 39 | Unica mencion de HU | "the median Hounsfield Unit (HU) intensity values for major organs" | Sec. 4.1, p. 4435 |
| 40 | Criterio del filtro HU | "are within the established normal range from training data" | Sec. 4.1, p. 4435 |
| 41 | Entrenamiento fuera del PDF | "More details about model training are provided in Supplementary Sec. B." | Sec. 4.1, p. 4435 |
| 42 | Tabla 1, Task07 MAISI (LPIPS/SSIM/PSNR/GPU) | "MAISI VAE 0.038 0.978 37.266 0h" | Tabla 1, p. 4435 |
| 43 | Tabla 1, Task07 dedicado | "Dedicated VAE 0.047 0.971 34.750 619h" | Tabla 1, p. 4435 |
| 44 | Tabla 1, Task08 MAISI | "MAISI VAE 0.046 0.970 36.559 0h" | Tabla 1, p. 4435 |
| 45 | Tabla 1, Task08 dedicado | "Dedicated VAE 0.041 0.973 37.110 669h" | Tabla 1, p. 4435 |
| 46 | Tabla 1, BraTS18 MAISI | "MAISI VAE 0.026 0.977 39.003 0h" | Tabla 1, p. 4435 |
| 47 | Tabla 1, BraTS18 dedicado | "Dedicated VAE 0.030 0.975 38.971 672h" | Tabla 1, p. 4435 |
| 48 | Columna GPU | "additional GPU hours for training with one 32G V100 GPU" | Tabla 1, p. 4435 |
| 49 | Conjuntos OOD | "(i.e., unseen during training), including MSD Pancreas Tumor" | Sec. 4.2, p. 4435 |
| 50 | Modalidad BraTS | "BraTS18 [4] (post-contrast T1-weighted MRI)" | Sec. 4.2, p. 4435 |
| 51 | Sin reentrenar | "this application required no additional training" | Sec. 4.2, p. 4435 |
| 52 | Split del dedicado | "separately on each dataset using 80% of the data" | Sec. 4.2, p. 4435 |
| 53 | Test | "testing on the remaining 20% of the data" | Sec. 4.2, p. 4435 |
| 54 | Conclusion del VAE | "achieved comparable results without additional GPU resource expenditure" | Sec. 4.2, p. 4435 |
| 55 | Metrica de sintesis | "We use the Fréchet Inception Distance (FID) [27]" | Sec. 4.3, p. 4435 |
| 56 | Tabla 2, MAISI DM (Task06/LIDC/COVID) | "MAISI DM 4.349 6.200 8.346" | Tabla 2, p. 4435 |
| 57 | Tabla 2, HA-GAN | "HA-GAN [62] 98.208 116.260 98.064" | Tabla 2, p. 4435 |
| 58 | Referencia externa | "whole-body CT scans from patients with various types of cancer and negative controls" | Sec. 4.3, pp. 4435-4436 |
| 59 | Tabla 3, DDPM (Ax/Sag/Cor/Avg) | "DDPM [29] 18.524 23.696 25.604 22.608" | Tabla 3, p. 4436 |
| 60 | Tabla 3, LDM | "LDM [50] 16.853 10.191 10.093 12.379" | Tabla 3, p. 4436 |
| 61 | Tabla 3, HA-GAN | "HA-GAN [62] 17.432 10.266 13.572 13.757" | Tabla 3, p. 4436 |
| 62 | Tabla 3, MAISI DM | "MAISI DM 3.301 5.838 9.109 6.083" | Tabla 3, p. 4436 |
| 63 | Fig. 5, salida pequena | "Output Size: 256 × 256 × 256 ... Voxel Spacing: 1 × 1 × 1" | Fig. 5, p. 4436 |
| 64 | Fig. 5, salida grande | "Output Size: 512 × 512 × 512 ... Voxel Spacing: 1.5 × 1.5 × 1.5" | Fig. 5, p. 4436 |
| 65 | Lesion osea | "and an in-house bone lesion dataset" | Sec. 4.4, p. 4436 |
| 66 | Protocolo downstream | "we performed 5-fold cross-validation and reported the average Dice Similarity Coefficient" | Sec. 4.4, p. 4436 |
| 67 | Mejora media CT Generation | "an average DSC improvement of 4% across the five tumor types" | Sec. 4.4, p. 4437 |
| 68 | Mejora media Inpainting | "average improvement of 6.5% in DSC for liver, lung, and pancreas tumors" | Sec. 4.4, p. 4437 |
| 69 | OOD hepatico | "on 303 liver tumor samples from MSD Task08" | Sec. 4.4, p. 4437 |
| 70 | Fig. 6a, lesion osea (Real / MAISI) | "0.504" / "0.539" / "3.6%" | Fig. 6a, p. 4437 |
| 71 | Fig. 6b, higado (Real / DiffTumor / Gen / Inpaint) | "0.662" / "0.684" / "0.688" / "0.714" | Fig. 6b, p. 4437 |
| 72 | Fig. 6c, pulmon (Real / Gen / Inpaint) | "0.581" / "0.635" / "0.649" | Fig. 6c, p. 4437 |
| 73 | Fig. 6d, pancreas (Real / DiffTumor / Gen / Inpaint) | "0.433" / "0.511" / "0.482" / "0.507" | Fig. 6d, p. 4437 |
| 74 | Fig. 6e, colon (Real / Gen) | "0.449" / "0.485" | Fig. 6e, p. 4437 |
| 75 | Fig. 6f, Task08 (Real / DiffTumor / Gen / Inpaint) | "0.553" / "0.608" / "0.615" / "0.630" | Fig. 6f, p. 4437 |
| 76 | Definicion del % de Fig. 6 | "The percentage of relative improvement compared to Real Only" | Fig. 6, p. 4437 |
| 77 | Significancia | "All reported improvements are significant under the Wilcoxon signed rank test." | Fig. 6, p. 4437 |
| 78 | Limitacion demografica | "(such as age, ethnicity, and gender differences) in generated anatomy has not been extensively validated" | Sec. 5, p. 4437 |
| 79 | Limitacion de computo | "still demand substantial computational resources" | Sec. 5, p. 4437 |

**Inconsistencia interna (Fig. 6):** el pie dice *"relative improvement"*, pero los porcentajes coinciden con diferencias absolutas en puntos de Dice (p. ej., 0.714 - 0.662 = 0.052 frente a "5.1%"; relativo seria ~7.9%). No afecta a la tesis (downstream fuera de alcance).

### Datos buscados y NO ENCONTRADO EN EL PDF
| # | Dato buscado | Estado |
|---|---|---|
| N1 | Factor de compresion espacial del VAE | NO ENCONTRADO EN EL PDF |
| N2 | Numero de canales latentes | NO ENCONTRADO EN EL PDF |
| N3 | Tamano de parche / volumen de entrenamiento del VAE | NO ENCONTRADO EN EL PDF |
| N4 | Rango de HU de normalizacion / recorte (clip) | NO ENCONTRADO EN EL PDF |
| N5 | Escala de intensidad (p. ej. a [0,1] o [-1,1]) | NO ENCONTRADO EN EL PDF |
| N6 | MAE o error de reconstruccion en HU | NO ENCONTRADO EN EL PDF |
| N7 | Error de reconstruccion en hueso o por tejido | NO ENCONTRADO EN EL PDF |
| N8 | Rango de datos usado para el PSNR | NO ENCONTRADO EN EL PDF |
| N9 | "Pelvis" como region de entrenamiento del VAE | NO ENCONTRADO EN EL PDF |
| N10 | Nombres de los datasets de entrenamiento (VAE y LDM) | NO ENCONTRADO EN EL PDF |
| N11 | Implantes metalicos / protesis en los datos | NO ENCONTRADO EN EL PDF |
| N12 | Generacion de metal o artefacto metalico | NO ENCONTRADO EN EL PDF |
| N13 | Metal declarado como limitacion | NO ENCONTRADO EN EL PDF |
| N14 | Condicionamiento por mascara de implante | NO ENCONTRADO EN EL PDF |
| N15 | Lista de las 127 estructuras | NO ENCONTRADO EN EL PDF |
| N16 | Tamano del conjunto de entrenamiento del ControlNet | NO ENCONTRADO EN EL PDF |
| N17 | Numero de pasos T / scheduler del LDM | NO ENCONTRADO EN EL PDF |
| N18 | Numero de GPUs, epocas u horas de entrenamiento de MAISI | NO ENCONTRADO EN EL PDF |
| N19 | Tiempo de inferencia | NO ENCONTRADO EN EL PDF |
| N20 | Memoria de inferencia | NO ENCONTRADO EN EL PDF |
| N21 | Disponibilidad explicita de pesos de MAISI | NO ENCONTRADO EN EL PDF |
| N22 | Licencia de codigo o pesos | NO ENCONTRADO EN EL PDF |
| N23 | Variante 2D o 2.5D del VAE | NO ENCONTRADO EN EL PDF |
