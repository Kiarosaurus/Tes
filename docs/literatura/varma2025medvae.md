# varma2025medvae — MedVAE: autoencoders medicos generalizables 2D y 3D

- **DOI / URL:** arXiv:2502.14753 (v2, 2 Jun 2025, segun la marca lateral del PDF, p. 1); https://arxiv.org/abs/2502.14753 (del raw). DOI: NO ENCONTRADO EN EL PDF
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/varma2025medvae.pdf (25 pp.: cuerpo pp. 1-17, referencias pp. 19-22, apendice pp. 23-25; preprint, sin paginacion de revista)

## Que hace (3 lineas maximo)
Entrena seis VAE medicos (cuatro 2D, dos 3D) de un canal, en dos etapas: Etapa 1 con perdida perceptual + adversarial + consistencia de embedding BiomedCLIP + KL; Etapa 2 con capas de proyeccion (2D) o inflado a 3D con parches de 64^3. Los evalua sobre todo como sustituto comprimido de la imagen en clasificadores CAD (AUROC), y en segundo lugar por reconstruccion (PSNR, MS-SSIM) y un estudio de lectores sobre radiografias de torax.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; su restriccion frente a implantes es de omision y de diseno:
- **Nunca define como entra el CT a la red.** No hay HU, ventana, recorte, escala ni normalizacion: NO ENCONTRADO EN EL PDF. Solo se sabe que la entrada es de un canal (*"accepts single-channel, high-resolution medical images"*, §4.3, p. 12). Sin eso no se puede saber si el hueso cortical denso y el metal quedan dentro del rango que el VAE aprendio a reconstruir.
- **Excluye metal activamente en el unico sitio donde lo menciona:** *"remove all samples with metal hardware and casts, which may exhibit spurious correlations"* (§4.4, p. 15; dataset de muneca, tarea de evaluacion). Metal, implante, tornillo o artefacto metalico en el entrenamiento: NO ENCONTRADO EN EL PDF.
- **Optimiza similitud perceptual, no error por pixel en unidades fisicas** (*"maximizing perceptual similarity between the input image x and the reconstructed image"*, §4.3, p. 12). Ninguna metrica en HU ni MAE: NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto (hoy). Candidato a VAE alternativo del Objetivo 3 si P1 da No-Go (fila 6 de prioridad en `_candidatos.md`); su idoneidad NO se puede decidir desde el PDF y exige medirlo con el protocolo de P1.

## Numeros que cito de este paper
Ninguno decidido. Candidatos, solo si la autora adopta MedVAE:

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 1,021,356 imagenes 2D y 31,374 3D, 19 datasets | "1,021,356 2D images and 31,374 3D images obtained from 19 multi-institutional" | §4.2, p. 12 |
| 2D MedVAE f=64, C=4: latente (H/8)x(W/8)x4 | "This autoencoder yields latent representations z_i of size (H/8) × (W/8) × 4." | §4.3, p. 13 |
| Inicializado desde KL-VAE con LoRA rango 4 | "Stage 1 training using LoRA [18] with rank=4 applied to all 2D convolutional layers" | §4.3, p. 13 |
| Abdomen CT, f=16/C=3: MedVAE 44.95 dB / 0.999 frente a KL-VAE 43.51 / 0.998 | Tabla 4, filas "2D MedVAE 16 3" y "KL-VAE 16 3", columna Abdomen CTs | Tabla 4, p. 7 |

## Donde entra en mi tesis
**Relevancia para la tesis.** Objetivo 1 (compuerta del autoencoder) y Objetivo 3 (renderizador), como VAE alternativo al de SD 1.5, que fallo la compuerta (mejor 61.72 HU de MAE en hueso frente al umbral de 25 HU; dato del encargo, no del PDF). Respuestas a las siete preguntas del encargo:

1. **Arquitectura.** VAE totalmente convolucional (*"using a fully convolutional VAE"*, §4.3, p. 12). Cuatro modelos 2D: f=16/C=1 y f=64/C=1 entrenados desde cero; f=16/C=3 y f=64/C=4 inicializados desde *"a previously-developed natural image autoencoder (KL-VAE) [41]"* (p. 13), con LoRA de rango 4 sobre todas las convoluciones 2D. **f es factor sobre el AREA**, no por eje: f=16 da (H/4)x(W/4); f=64 da (H/8)x(W/8). Dos modelos 3D: f=64 -> (H/4)x(W/4)x(S/4)x1 y f=512 -> (H/8)x(W/8)x(S/8)x1, ambos de un canal latente (p. 14). La ref. [41] es Rombach et al., *"High-resolution image synthesis with latent diffusion models"*, CVPR 2022 (p. 21). **"Stable Diffusion": NO ENCONTRADO EN EL PDF**; que checkpoint de KL-VAE se uso: NO ENCONTRADO EN EL PDF. **Compatibilidad con el latente de SD: NO ENCONTRADO EN EL PDF.** El 2D f=64/C=4 tiene la misma forma que el latente KL f=8/4c de `rombach2022latentdiffusion` (ver esa ficha), pero (a) LoRA modifica todas las convoluciones, (b) la entrada es de 1 canal y como se adapto la primera capa desde un VAE RGB es NO ENCONTRADO EN EL PDF, y (c) en 2D la Etapa 2 congela encoder y decoder y entrena capas de proyeccion; las evaluaciones de latente usan *"the projected latent"* (p. 14), y si el decodificador consume el latente proyectado o el original es NO ENCONTRADO EN EL PDF. Conclusion operativa: **misma forma no implica mismo espacio**; un ControlNet preentrenado sobre SD 1.5 no se puede suponer compatible (liga con #74).
2. **Datos.** 2D: dos datasets de radiografia de torax y seis de mamografia (p. 12); *"no MRI or CT slices were included in the 2D MedVAE training set"* (p. 8). 3D: RM de cabeza (14,296), RM de rodilla (3,564), CT de cabeza/cuello (10,156), CT de cuerpo entero (1,434) y CT de torax (1,924) (p. 12). El CT de cuerpo entero se describe como *"(head, neck, abdomen, chest, lower limb)"* (p. 12). **Pelvis: NO ENCONTRADO EN EL PDF** (ni la palabra ni la region). Hueso: solo como motivo de un recorte de evaluacion (*"to include both soft-tissue and bony features"*, p. 16) y como tareas de fractura. **Implantes: NO ENCONTRADO**; el metal se excluye en la tarea de muneca (p. 15).
3. **Normalizacion de intensidad de CT.** Rango de HU, recorte, ventana, escala, normalizacion y tratamiento de valores altos: **todo NO ENCONTRADO EN EL PDF**. Entrada: 1 canal (p. 12). Rango de datos con que se calcula el PSNR: NO ENCONTRADO EN EL PDF. **La pregunta critica (si hueso cortical denso y metal quedan fuera) no se puede responder desde el paper**; hay que leer el codigo o el preprocesado del repositorio, que no esta en el PDF.
4. **Fidelidad de reconstruccion.** Solo PSNR y MS-SSIM (p. 7), en unidades no declaradas; **MAE y cualquier error en HU: NO ENCONTRADO EN EL PDF**. Sin ROI de hueso, solo volumen completo recortado a 160^3 (320x320x160 en AMOS y CQ500). CT, 2D f=16/C=3: MedVAE 48.56 / 44.95 / 34.83 / 33.34 dB (cabeza / abdomen / TotalSegmentator / pulmon) frente a KL-VAE 47.65 / 43.51 / 34.14 / 32.62 (Tabla 4, p. 7). Ventaja de ~0.7-1.4 dB sobre KL-VAE. **Comparacion con "el VAE de SD" como tal: NO ENCONTRADO**; el comparador es "KL-VAE [41]".
5. **Utilidad downstream.** AUROC de clasificadores entrenados sobre el latente (Tablas 1-2). CT 3D f=64: fractura de columna 83.7 frente a 82.9 en alta resolucion; craneo 87.0 frente a 63.9 (DE 7.3 y 6.3, p. 5). Rasgos finos: PSNR en recortes de fractura de muneca (37.61 dB, f=16/C=3, Tabla 3) y lectura de 3 radiologos en 50 radiografias de torax con fractura (Likert -2 a 2; MedVAE f=64 obtiene 1.36 en artefactos frente a 1.97 de la imagen original, Fig. 3, p. 8). **Ningun rasgo fino de CT evaluado por lectores**; el estudio de lectores es solo en radiografia.
6. **Pesos, licencia, computo.** Codigo: *"Our code is available at https://github.com/StanfordMIMI/MedVAE."* (p. 1). **Pesos descargables: NO ENCONTRADO EN EL PDF. Licencia: NO ENCONTRADO EN EL PDF.** Computo de entrenamiento: 8 A100 (2D), 4 A6000 o 1 A6000 (3D) (pp. 13-14).
7. **Uso como latente para difusion.** **NO ENCONTRADO EN EL PDF.** El paper solo cita, como motivacion, que latentes comprimidos mejoran *"efficiency of downstream diffusion model training [41]"* (p. 10). No entrena ni evalua ningun modelo generativo sobre sus latentes; su uso es CAD.

**Riesgo adicional para la compuerta "pacientes separados":** todos los datasets de evaluacion de reconstruccion 3D (TotalSegmentator [52], CQ500 [8], AMOS [27], LIDC [1], MRNet [2], ADNI, HABS, A4, OASIS) aparecen tambien en la lista de datasets de entrenamiento (§4.2, p. 12), igual que CANDID-PTX [13] del estudio de lectores. Particion paciente entre entrenamiento del VAE y evaluacion de reconstruccion: NO ENCONTRADO EN EL PDF. Las cifras de PSNR pueden no ser fuera de muestra.

**Lectura para la decision de la autora:** MedVAE no aporta ninguna evidencia a favor ni en contra de pasar la compuerta de 25 HU en hueso. Es candidato solo por estar entrenado con CT; su unica via de evaluacion es correr el protocolo de P1 sobre sus pesos, verificando antes en el codigo la normalizacion de HU. Adoptarlo rompe el supuesto de ControlNet sobre SD 1.5 salvo prueba contraria.

## Dudas para el asesor
- Si MedVAE (o cualquier VAE no-SD) entra, hay que reentrenar ControlNet y la UNet de difusion sobre su latente? El PDF no da ninguna base para suponer compatibilidad con SD 1.5.
- El 3D f=64 comprime (H/4)x(W/4)x(S/4) con 1 canal: encaja en un LDM 2.5D o obliga a cambiar el diseno del renderizador?
- Vale la pena medir P1 sobre MedVAE sin conocer su normalizacion de HU, o primero se inspecciona el preprocesado del repositorio?
- Inconsistencia de la Tabla 4: lista "2D MedVAE 64 3" y "KL-VAE 64 3", pero §4.3 solo define 2D MedVAE f=64 con C=1 y C=4. Que modelo se evaluo realmente en CT a f=64?

## Evidencia textual

| # | Cifra / umbral / definicion / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| 1 | 6 autoencoders 2D y 3D | "a family of six large-scale 2D and 3D autoencoders" | Abstract, p. 1 |
| 2 | 1,052,730 imagenes de entrenamiento | "novel two-stage training approach with 1,052,730 medical images" | Abstract, p. 1 |
| 3 | 20 datasets de evaluacion | "Across diverse tasks obtained from 20 medical image datasets" | Abstract, p. 1 |
| 4 | Hasta 70x en throughput | "(up to 70x improvement in throughput)" | Abstract, p. 1 |
| 5 | Codigo publico | "Our code is available at https://github.com/StanfordMIMI/MedVAE." | Abstract, p. 1 |
| 6 | Almacenamiento hasta 512x | "reduce storage requirements (up to 512x)" | §1, p. 2 |
| 7 | 20 datasets, 4 modalidades | "derived from 20 multi-institutional, open-source medical datasets with 4 imaging modalities" | §1, p. 2 |
| 8 | 8 regiones anatomicas | "and 8 anatomical regions" | §1, p. 2 |
| 9 | Definicion de f (2D, sobre area) | "f represents the downsizing factor applied to the 2D area of the image" | §2.1, p. 3 |
| 10 | Definicion de C | "C represents a pre-specified number of latent channels" | §2.1, p. 3 |
| 11 | f en 3D (sobre volumen) | "the downsizing factor f is applied to the 3D volume of the image" | §2.1, p. 3 |
| 12 | 1,021,356 2D + 31,374 3D, 19 datasets | "1,021,356 2D images and 31,374 3D images obtained from 19 multi-institutional" | §4.2, p. 12 |
| 13 | Datos 2D | "We collect images from two chest X-ray datasets and six FFDM datasets" | §4.2, p. 12 |
| 14 | CT de cuerpo entero (regiones) | "high-resolution whole-body (head, neck, abdomen, chest, lower limb) CTs" | §4.2, p. 12 |
| 15 | 14,296 RM de cabeza; 3,564 RM de rodilla | "T2-weighted head MRI datasets (14,296), one knee MRI dataset (3,564)" | §4.2, p. 12 |
| 16 | 10,156 CT cabeza/cuello; 1,434 CT cuerpo entero | "two head/neck CT datasets (10,156), two whole-body CT datasets (1,434)" | §4.2, p. 12 |
| 17 | 1,924 CT de torax | "and two chest CT datasets (1,924)" | §4.2, p. 12 |
| 18 | Sin CT ni RM en el entrenamiento 2D | "no MRI or CT slices were included in the 2D MedVAE training set" | §2.4, p. 8 |
| 19 | Entrada de 1 canal | "Each MedVAE autoencoder accepts single-channel, high-resolution medical images x_i as input" | §4.3, p. 12 |
| 20 | VAE totalmente convolucional | "using a fully convolutional VAE" | §4.3, p. 12 |
| 21 | Objetivo: similitud perceptual | "maximizing perceptual similarity between the input image x and the reconstructed image" | §4.3, p. 12 |
| 22 | Ejemplo f=16, C=3 | "downsizing the image area by 16x and adding two additional channels" | §4.3, p. 13 |
| 23 | Perdidas perceptual y adversarial | "a perceptual loss term [54] and a patch-based adversarial objective [24]" | §4.3, p. 13 |
| 24 | Consistencia BiomedCLIP (L2) | "we apply an L2 penalty between BiomedCLIP embeddings corresponding to the input image" | §4.3, p. 13 |
| 25 | Peso KL 1e-6 | "the penalty is assigned a low weight of 1e-6" | §4.3, p. 13 |
| 26 | 2D f=16, C=1: (H/4)x(W/4)x1, desde cero | "Stage 1 training is performed from scratch." | §4.3, p. 13 |
| 27 | Adversarial tras 3125 pasos | "consistency loss for the first 3125 steps; then, the patch-based adversarial objective is applied" | §4.3, p. 13 |
| 28 | 100K pasos, 8 A100, batch 32 (f=16/C=1 y f=64/C=1) | "train for 100K steps using 8 NVIDIA A100 GPUs and a batch size of 32" | §4.3, p. 13 |
| 29 | f=16, C=3 y f=64, C=4 parten de KL-VAE [41] | "We first initialize the VAE with weights from a previously-developed natural image autoencoder (KL-VAE) [41]" | §4.3, p. 13 |
| 30 | LoRA rango 4 en todas las conv 2D | "Stage 1 training using LoRA [18] with rank=4 applied to all 2D convolutional layers" | §4.3, p. 13 |
| 31 | 50k pasos con LoRA | "We train with all four loss functions for 50k steps using 8 A100 GPUs" | §4.3, p. 13 |
| 32 | 2D f=64, C=1: (H/8)x(W/8)x1 | "latent representations z_i of size (H/8) × (W/8) × 1" | §4.3, p. 13 |
| 33 | 2D f=64, C=4: (H/8)x(W/8)x4 | "This autoencoder yields latent representations z_i of size (H/8) × (W/8) × 4." | §4.3, p. 13 |
| 34 | Etapa 2 (2D): encoder y decoder congelados | "We freeze all parameters in the encoder and decoder of the VAE." | §4.3, p. 13 |
| 35 | Evaluacion con latente proyectado | "All downstream evaluations of latent representation quality are performed with the projected latent" | §4.3, p. 14 |
| 36 | Etapa 2: 50K pasos (f=16 C=1, f=16 C=3, f=64 C=4) | "Stage 2 training is performed for 50K steps using 8 NVIDIA A100 GPUs" | §4.3, p. 14 |
| 37 | Etapa 2: 60K pasos (f=64 C=1) | "Stage 2 training is performed for 60K steps using 8 NVIDIA A100 GPUs" | §4.3, p. 14 |
| 38 | Paso a 3D por inflado de kernels | "lifting the 2D VAE architecture to 3D using a kernel centering inflation strategy" | §4.3, p. 14 |
| 39 | BiomedCLIP descartado en 3D | "to enforce feature consistency is inadequate for 3D settings" | §4.3, p. 14 |
| 40 | Parches 3D de 64^3 | "using random cubic patches of size 64 × 64 × 64" | §4.3, p. 14 |
| 41 | Perdidas 3D calculadas por corte | "The perceptual loss and the patch-based adversarial objective are calculated per-slice" | §4.3, p. 14 |
| 42 | 3D f=64: (H/4)x(W/4)x(S/4)x1 | "The latent representations z_i are of size (H/4)×(W/4)×(S/4)×1." | §4.3, p. 14 |
| 43 | 3D f=64 parte del 2D f=16, C=1 | "initialize the VAE with weights from 2D Base Autoencoder (Stage 1) with f = 16" | §4.3, p. 14 |
| 44 | 3D f=64: 35K pasos, 4 A6000, batch 32 | "35K steps using 4 NVIDIA A6000 GPUs and a batch size of 32" | §4.3, p. 14 |
| 45 | 3D f=512: (H/8)x(W/8)x(S/8)x1 | "3D MedVAE with f = 512 and C = 1: The latent representations" | §4.3, p. 14 |
| 46 | 3D f=512: 140K pasos, 1 A6000, batch 8 | "140K steps using 1 NVIDIA A6000 GPU and a batch size of 8" | §4.3, p. 14 |
| 47 | Metricas de reconstruccion: PSNR y MS-SSIM | "We report peak signal-to-noise ratio (PSNR) and the multi-scale structural similarity index measure (MS-SSIM)" | §2.4, p. 7 |
| 48 | Recorte central 160^3 en evaluacion 3D | "a center crop of volume dimensions 160×160×160 was extracted" | §4.5, p. 16 |
| 49 | 320x320x160 en AMOS y CQ500 para incluir hueso | "expanded to dimensions 320 × 320 × 160 to include both soft-tissue and bony features" | §4.5, p. 16 |
| 50 | Fuentes de CT de evaluacion | "whole-body CTs are obtained from TotalSegmentator dataset [52]" | §4.5, p. 16 |
| 51 | Muestra 2D: 1000 imagenes, 4 corridas | "on a random sample of 1000 images for each image type" | §4.6, p. 17 |
| 52 | Muestra 3D: 100 volumenes, una corrida | "PSNR and MS-SSIM on a single random sample of 100 images for each image type" | §4.6, p. 17 |
| 53 | CT, f=16, C=3: 2D MedVAE 48.56/1.000 (cabeza), 44.95/0.999 (abdomen), 34.83/0.995 (TS), 33.34/0.989 (pulmon) | Tabla 4, fila "2D MedVAE 16 3" | Tabla 4, p. 7 |
| 54 | CT, f=16, C=3: KL-VAE 47.65/1.000, 43.51/0.998, 34.14/0.994, 32.62/0.989 | Tabla 4, fila "KL-VAE 16 3" | Tabla 4, p. 7 |
| 55 | CT, "f=64, C=3": 2D MedVAE 41.98/0.999, 39.49/0.995, 30.35/0.984, 29.59/0.977 | Tabla 4, fila "2D MedVAE 64 3" | Tabla 4, p. 7 |
| 56 | CT, "f=64, C=3": KL-VAE 40.95/0.997, 38.07/0.995, 29.85/0.982, 28.83/0.974 | Tabla 4, fila "KL-VAE 64 3" | Tabla 4, p. 7 |
| 57 | CT, 3D MedVAE f=64: 39.03/0.999, 36.61/0.993, 31.35/0.987, 28.79/0.975 | Tabla 4, fila "3D MedVAE 64 1" | Tabla 4, p. 7 |
| 58 | CT, 3D MedVAE f=512: 30.85/0.991, 29.47/0.960, 26.34/0.949, 24.76/0.934 | Tabla 4, fila "3D MedVAE 512 1" | Tabla 4, p. 7 |
| 59 | Inconsistencia: C=3 a f=64 no definido en Metodos | Tabla 4 lista "64 3"; §4.3 define f=64 solo con C=1 y C=4 | Tabla 4, p. 7; §4.3, pp. 13-14 |
| 60 | 2D, f=16/C=3: MedVAE 37.57/0.993 (mamo), 43.55/0.997 (torax), 39.41/0.994 (MSK) | Tabla 3, fila "2D MedVAE 16 3" | Tabla 3, p. 7 |
| 61 | 2D, f=16/C=3: KL-VAE 36.11/0.989, 41.45/0.996, 38.29/0.992 | Tabla 3, fila "KL-VAE 16 3" | Tabla 3, p. 7 |
| 62 | 2D, f=64/C=4: MedVAE 33.13/0.969, 38.88/0.990, 34.73/0.972; KL-VAE 31.88/0.959, 36.37/0.987, 33.49/0.966 | Tabla 3, filas "2D MedVAE 64 4" y "KL-VAE 64 4" | Tabla 3, p. 7 |
| 63 | Rasgos finos, recortes de fractura de muneca: MedVAE 37.61 (f16 C3) y 32.30 (f64 C4); KL-VAE 36.55 y 31.04 dB | Tabla 3, columna "Wrist X-rays (FG)" | Tabla 3, p. 7 |
| 64 | 7677 imagenes con fractura para PSNR fino | "we extract 7677 images containing fractures from GRAZPEDWRI-DX" | §4.5, p. 16 |
| 65 | Mas canales latentes, mejor reconstruccion | "increasing the number of latent channels C improves perceptual quality" | §2.4, p. 8 |
| 66 | Ablacion Etapa 1 sin consistencia: 37.27 dB / 0.992 | "Stage 1 training without the embedding consistency loss term achieves a PSNR of 37.27" | §2.5, p. 9 |
| 67 | AUROC 2D, promedio: alta resolucion 69.2; MedVAE f16 C1 69.5; MedVAE f64 C4 64.7 | Tabla 1, columna "Average" | Tabla 1, p. 4 |
| 68 | AUROC 2D, promedio KL-VAE: 63.2 (f16 C3), 59.9 (f64 C4) | Tabla 1, filas "KL-VAE" | Tabla 1, p. 4 |
| 69 | Criterio "preserva perfectamente" | "performance equals or exceeds performance when training with high-resolution images" | Tabla 1, leyenda, p. 4 |
| 70 | 10.0% sobre KL-VAE a f=16 (2D) | "a 10.0% improvement over KL-VAE at a downsizing factor of f = 16" | §2.2, pp. 5-6 |
| 71 | 8.0% sobre KL-VAE a f=64 (2D) | "and a 8.0% improvement at a downsizing factor of f = 64" | §2.2, p. 6 |
| 72 | 37.9% sobre KL-VAE a f=64 (3D) | "3D MedVAE demonstrates a 37.9% improvement over KL-VAE" | §2.2, p. 6 |
| 73 | 11.4% sobre KL-VAE a f=512 (3D) | "a 11.4% improvement over KL-VAE at a downsizing factor of f = 512" | §2.2, p. 6 |
| 74 | AUROC 3D f=64: columna 83.7±2.8 vs 82.9±2.2; craneo 87.0±7.3 vs 63.9±6.3; rodilla 68.4 vs 69.9; promedio 79.7 vs 72.2 | Tabla 2, filas "3D MedVAE 64 1" y "High-Resolution" | Tabla 2, p. 5 |
| 75 | AUROC 3D f=512: promedio 59.8 (MedVAE) | Tabla 2, fila "3D MedVAE 512 1" | Tabla 2, p. 5 |
| 76 | 2D MedVAE f=512 C=1 promedio 61.6, por encima del 3D (59.8) | Tabla 8, fila "2D MedVAE 512 1" | Apendice Tabla 8, p. 25 |
| 77 | Etapas: promedio AUROC 62.7 -> 68.6 (f16 C3) y 60.8 -> 64.7 (f64 C4) | Tabla 6, filas "Stage 1" y "Stage 2" | Apendice Tabla 6, p. 24 |
| 78 | Etapas 3D: promedio 59.2 -> 79.7 (f=64) | Tabla 7, filas "64 1" | Apendice Tabla 7, p. 24 |
| 79 | Cabeza CT f=64: 2D MedVAE-Decoder 35.01 vs 3D MedVAE 39.03 dB | Tabla 9, columna "Head CTs" | Apendice Tabla 9, p. 25 |
| 80 | VerSe: 160 CT de columna, split 50/25/25, 224x224x160 | "The final size of a volume after preprocessing was 224 × 224 × 160." | §4.4, p. 15 |
| 81 | CQ500: 378 CT de cabeza, 80/20, 224x224x44 | "CQ500 dataset [8], which includes 378 head CT images" | §4.4, p. 15 |
| 82 | Exclusion de metal en muneca | "remove all samples with metal hardware and casts, which may exhibit spurious correlations" | §4.4, p. 15 |
| 83 | Canales promediados antes del clasificador 2D | "applying the mean operation across the channel dimension if more than one channel" | §4.4, p. 15 |
| 84 | HRNet: 100 epocas, batch 256, lr 1e-4 | "We train for 100 epochs using a batch size of 256" | §4.4, p. 15 |
| 85 | SEResNet-152: batch 20 latentes / 10 originales | "a batch size of 20 for latents, a batch size of 10" | §4.4, p. 16 |
| 86 | Eficiencia 2D a f=64: latencia 69x, throughput 70x | "the latency decreases by 69x, the throughput increases by 70x" | §2.3, p. 6 |
| 87 | Eficiencia 3D a f=512: latencia 62x, throughput 55x | "the latency decreases by 62x, the throughput increases by 55x" | §2.3, p. 6 |
| 88 | Batch maximo 32x (2D) y 512x (3D) | "and the maximum batch size increases by 512x" | §2.3, p. 6 |
| 89 | Entradas supuestas: 1024x1024 (2D), 256^3 (3D), 1 canal | "input volume size of 256 × 256 × 256 with 1 channel" | §2.3, p. 6 |
| 90 | Lectores: escala Likert de 5 puntos, -2 a 2 | "scored on a 5-point Likert scale ranging from -2 to 2" | §2.4, p. 8 |
| 91 | 50 radiografias de torax con fractura | "A total of 50 unique chest X-rays with fractures, randomly sampled from CANDID-PTX" | §2.4, p. 8 |
| 92 | 3 radiologos | "Our study involved three radiologists as expert readers." | §2.4, p. 8 |
| 93 | Fidelidad +2.8 frente a bicubica | "rated image fidelity for 2D MedVAE to be 2.8 points higher than bicubic" | §2.4, p. 8 |
| 94 | Rasgos clinicos +2.8 | "2D MedVAE also better preserved clinically-relevant features (2.8 points)" | §2.4, p. 8 |
| 95 | Artefactos: 2.6 puntos | "Artifacts ... were more frequent in interpolated images (2.6 points)" | §2.4, p. 8 |
| 96 | Fig. 3: original 1.97/1.97/1.97; MedVAE f16 1.96/1.96/1.89; MedVAE f64 1.96/1.98/1.36 | Valores impresos sobre las barras (fidelidad / rasgos / artefactos) | Fig. 3, p. 8 |
| 97 | Fig. 3: bicubica f16 -0.31/-0.26/-0.54; f64 -1.3/-1.47/-1.45 | Valores impresos sobre las barras | Fig. 3, p. 8 |
| 98 | IC 95% entre tres lectores | "we report mean scores and 95% confidence intervals across three readers" | §4.6, p. 17 |
| 99 | Lectores cegados | "Readers are blinded to both the method and the downsizing factor" | Apendice Fig. 5, p. 23 |
| 100 | Definicion del criterio "artefactos" | "Artifacts can include image distortions, noise, blurring, or other visual anomalies" | §4.5, p. 17 |
| 101 | Latente para difusion: solo motivacion citada | "improve efficiency of downstream diffusion model training [41]" | §3, p. 10 |
| 102 | Rango de HU, recorte, ventana o normalizacion de CT | NO ENCONTRADO EN EL PDF | — |
| 103 | MAE o cualquier error en HU | NO ENCONTRADO EN EL PDF | — |
| 104 | Rango de datos (data range) usado en el PSNR | NO ENCONTRADO EN EL PDF | — |
| 105 | ROI de hueso en la evaluacion de reconstruccion | NO ENCONTRADO EN EL PDF | — |
| 106 | Pelvis como region de entrenamiento o evaluacion | NO ENCONTRADO EN EL PDF | — |
| 107 | Implantes o metal en el entrenamiento | NO ENCONTRADO EN EL PDF | — |
| 108 | Mencion de "Stable Diffusion" | NO ENCONTRADO EN EL PDF | — |
| 109 | Checkpoint concreto del KL-VAE de partida | NO ENCONTRADO EN EL PDF | — |
| 110 | Adaptacion de la primera capa de 3 canales a 1 canal | NO ENCONTRADO EN EL PDF | — |
| 111 | Compatibilidad del latente con el de SD / ControlNet | NO ENCONTRADO EN EL PDF | — |
| 112 | Si el decodificador 2D consume el latente proyectado | NO ENCONTRADO EN EL PDF | — |
| 113 | Particion paciente entre entrenamiento del VAE y evaluacion de reconstruccion | NO ENCONTRADO EN EL PDF | — |
| 114 | Pesos descargables | NO ENCONTRADO EN EL PDF | — |
| 115 | Licencia | NO ENCONTRADO EN EL PDF | — |
| 116 | Uso del latente para entrenar un modelo de difusion | NO ENCONTRADO EN EL PDF | — |
| 117 | DOI | NO ENCONTRADO EN EL PDF | — |
