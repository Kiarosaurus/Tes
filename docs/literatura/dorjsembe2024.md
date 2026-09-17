# dorjsembe2024 — Polyp-DDPM: sintesis semantica de polipos por difusion condicionada por mascara

- **DOI / URL:** 10.1109/EMBC53108.2024.10782077 ("DOI: 10.1109/EMBC53108.2024.10782077", pie de p. 1). Version
  leida: 2024 46th Annual International Conference of the IEEE EMBC (IEEE Xplore). Codigo y pesos:
  https://github.com/mobaidoctor/polyp-ddpm (Abstract, p. 1). Numeros de pagina impresos del proceedings:
  NO ENCONTRADO EN EL PDF (el PDF no los trae; las paginas de esta ficha son el orden del PDF, pp. 1-7).
  Identificador arXiv (`_candidatos.md` lo registra como arXiv:2402.04031): NO ENCONTRADO EN EL PDF.
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/dorjsembe2024.pdf

## Que hace (3 lineas maximo)
DDPM 2D en espacio de pixel (adaptado de su Med-DDPM 3D de RM cerebral) que genera la imagen endoscopica
COMPLETA desde ruido, condicionado por una mascara binaria de polipo concatenada por canal a la entrada.
Evalua con FID/IS/KID y con segmentacion downstream (UNet++, FPN, DeepLabv3plus) en tres conjuntos de test.

## Restriccion o supuesto clave
**1. Imagen completa desde ruido, no inpainting.** No hay imagen receptora ni fondo original:
- "transform random noise into realistic polyp images by conditioning on a binary segmentation mask" (Fig. 1, p. 2)
- "The purpose of forward diffusion is to entirely erase the original data structure" (§II, p. 2)
- Cada muestra cambia toda la escena: "showcasing the diversity of synthetic images generated from a single
  input mask" (Fig. 2, p. 3).
- Inpainting, recomposicion del fondo original o preservacion de pixeles fuera de la mascara: NO ENCONTRADO
  EN EL PDF.

**2. Como entra la mascara.** Concatenacion por canal en la entrada del U-Net, en cada paso:
- "concatenating it channel-wise with the segmentation mask image (c) at each timestep (t)" (§II, p. 2)
- "this process results in a 6-channel input for the model" (§II, p. 2); la mascara tiene tres canales
  ("As both the image and mask contain three channels", §II, p. 2). Como se replica la mascara binaria a
  tres canales: NO ENCONTRADO EN EL PDF.
- La mascara codifica solo region: "polyp regions are labeled '1' and normal regions '0'" (§II, p. 2).
  Condiciona por region, no por borde. Sin ControlNet, sin cross-attention de la mascara, sin espacio latente
  (la concatenacion es con la imagen x_t de ancho w y alto h).

**3. Fuera de la mascara.** Todo se genera, pero como contexto generico aprendido de los datos: ningun
mecanismo ni perdida relaciona el contenido fuera de la mascara con el objeto sintetizado (la perdida es L1
sobre el ruido, "utilizing an L1 loss function", §III, p. 3). Metrica de fidelidad o de cambios fuera de la
mascara: NO ENCONTRADO EN EL PDF. Observacion visual, no textual: en Figs. 2-3 (p. 3) varias muestras de
Polyp-DDPM reproducen cuñas negras de encuadre rotado y un recuadro negro en una esquina, es decir contenido
de adquisicion/aumentacion fuera de la mascara, no inducido por el polipo.

**4. Supuesto que le impide manejar implantes metalicos rigidos.**
- Supuesto explicito de tejido deformable/no rigido: NO ENCONTRADO EN EL PDF.
- Implicito: la forma del objeto se trata como deformable y augmentable. Las mascaras nuevas se obtienen con
  "augmentations such as rotation, shifting, scaling, and elastic deformation can be applied" (§II, p. 2), y
  Fig. 3 (p. 3) muestra una columna "Elastic Deformed". Una geometria CAD de tornillo o placa no admite
  deformacion elastica ni escalado libre.
- La condicion es solo forma binaria ("straightforward binary nature of these masks", §II, p. 2): no hay
  intensidad del objeto, material, fisica ni relacion objeto-entorno. Metal, alta intensidad, artefactos, CT,
  HU: NO ENCONTRADO EN EL PDF. Dominio: "synthesizing 2D colored medical images" (§II, p. 2), intensidad
  reescalada a [-1, 1] (§III, p. 3).
- Sin anatomia receptora: al generar la escena entera no puede insertar un objeto en un volumen dado
  conservando la anatomia del paciente, que es lo que exige el renderizador de la tesis.
- No mide correspondencia mascara-imagen generada (NO ENCONTRADO EN EL PDF); la validez de las etiquetas solo
  se infiere indirectamente por la segmentacion downstream.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna cifra necesaria (downstream fuera de alcance). Solo mecanismo, si se cita: | | |
| Imagen completa desde ruido, condicionada por mascara binaria | "transform random noise into realistic polyp images by conditioning on a binary segmentation mask" | Fig. 1, p. 2 |
| Via de entrada de la mascara | "conditions the diffusion model through channel-wise concatenation of mask images" | §I, p. 1 |

## Donde entra en mi tesis
- Related Work / Problem Statement (`tesis/main.tex` l. 48): encaja en la familia "Globally conditioned
  methods" junto a DiffBoost y `macháček2023` (sintesis de la imagen entera desde ruido). Difiere de DiffBoost
  en que condiciona con la mascara de region concatenada, no con su borde; si se cita como ejemplo adicional,
  la clausula "using the mask only as an edge constraint" debe quedar atribuida solo a DiffBoost (mismo caso
  que `macháček2023`).
- Reclamo de novedad de B_delta: no lo reduce. Genera todo fuera de la mascara, pero sin mecanismo ni senal
  de entrenamiento que relacione esas intensidades con el objeto, y sin medirlas.
- La frase "None of these works states an assumption of tissue non-rigidity" sigue siendo correcta: el paper
  no la enuncia; lo mas cercano es la deformacion elastica de mascaras como aumentacion (§II, p. 2), que es una
  eleccion de datos, no un supuesto declarado sobre el tejido.
- Downstream (IoU, F1, Acc, Prec): no se usa; la evaluacion de segmentacion esta fuera de alcance.

## Dudas para el asesor
1. Aporta citarlo ademas de DiffBoost y `macháček2023`? Es el mismo dominio (polipos 2D, Kvasir-SEG) y la
   misma familia; se distingue solo por ser DDPM en pixel con concatenacion de la mascara.
2. Inconsistencias a no heredar si se cita:
   - Llama "qualitative evaluation" a la segmentacion downstream (§III, p. 3), que es cuantitativa.
   - Lista "rotation" y "random rotation" como aumentaciones distintas (§III, p. 3).
   - "generally improved performance across all models" con datos mixtos (p. 5), pero en Test set-1 FPN
     R900 = 0.7730, R900+S900 Polyp-DDPM = 0.7730 y R900+S1000 Polyp-DDPM = 0.7380 (Tabla 2, p. 5).
   - Test set-3: "notable improvements ... when trained with synthetic images" (p. 6), pero S900 UNet++ 0.5295
     y FPN 0.5530 quedan bajo R900 (0.6329 y 0.6242); solo DeepLabv3plus sube (0.5682 frente a 0.5262).
   - Test set-3: patron "across all metrics" (p. 6), pero en R900+S1000 DeepLabv3plus LDM (0.6093) supera a
     Polyp-DDPM (0.5804) (Tabla 2, p. 5).
   - Redondeos por truncamiento: FID 78.4797 citado como 78.47; KID 0.0755 como 0.07; KID SinGAN-Seg 0.1468
     como 0.14 (Tabla I y §III-A, p. 4).
   - En Tabla I el IS de LDM y de Polyp-DDPM es identico en ambas columnas de referencia, pero el de
     SinGAN-Seg cambia (3.5943 frente a 3.3607) (p. 4), aunque el IS no depende del conjunto real.
   - FID/IS/KID usan 1,000 sinteticas de mascaras HyperKvasir (§III, p. 4), mientras la segmentacion usa 900
     sinteticas de las mismas mascaras; como se eligieron las 900 no se dice.
3. Comparacion con SinGAN-Seg declarada "unfair" por los propios autores (§III, p. 3), y HyperKvasir es a la
   vez su entrenamiento y el Test set-2.
4. §II (p. 2) describe que el ruido predicho "is then subtracted from the pure noise", redaccion que no
   coincide literalmente con la Ec. (3); irrelevante para la tesis, anotado solo por precision.

## Evidencia textual
| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| DOI | "DOI: 10.1109/EMBC53108.2024.10782077" | Pie, p. 1 |
| Venue | "2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)" | Pie, p. 1 |
| ISBN / precio | "979-8-3503-7149-9/24/$31.00 ©2024 IEEE" | Pie, p. 1 |
| Keywords | "diffusion models, semantic polyp synthesis, polyp segmentation" | p. 1 |
| Que propone | "a diffusion-based method for generating realistic images of polyps conditioned on masks" | Abstract, p. 1 |
| FID titular | "achieving a Fréchet Inception Distance (FID) score of 78.47, compared to scores above 95.82" | Abstract, p. 1 |
| IoU titular | "achieving an Intersection over Union (IoU) of 0.7156, versus less than 0.6828" | Abstract, p. 1 |
| IoU real (referencia del abstract) | "and 0.7067 for real data" | Abstract, p. 1 |
| Codigo publico | "https://github.com/mobaidoctor/polyp-ddpm" | Abstract, p. 1 |
| Cifra epidemiologica de contexto | "third most common and second deadliest cancer globally [1]" | §I, p. 1 |
| Cifra ajena (SinGAN-Seg) | "initial training on the HyperKvasir dataset [7] of 1,000 images" | §I, p. 1 |
| Problema de GANs | "A prevalent issue with GAN models is the mode collapse problem." | §I, p. 1 |
| Descripcion de LDM [9] | "generating masks with an improved diffusion model, and then conditioning a latent diffusion model" | §I, p. 1 |
| Critica a LDM [9] | "due to the need for two diffusion models" | §I, p. 1 |
| Antecedente propio | "builds upon our previous work, Med-DDPM [11]" | §I, p. 1 |
| Via de condicionamiento | "conditions the diffusion model through channel-wise concatenation of mask images" | §I, p. 1 |
| Titulo de Med-DDPM [11] | "Conditional diffusion models for semantic 3D brain MRI synthesis" | Ref. [11], p. 7 |
| Adaptacion 3D a 2D | "modifying the architecture to generate conditional 2D polyp images from segmentation masks" | §II, p. 2 |
| Dominio de imagen | "synthesizing 2D colored medical images" | §II, p. 2 |
| Difusion directa | Ec. (1): x_t = sqrt(ᾱ_t) x_0 + sqrt(1 − ᾱ_t) ε | §II, Ec. (1), p. 2 |
| Schedule | "we employed a cosine noise schedule [12]" | §II, Ec. (2), p. 2 |
| Parametro s | "parameter s represents a small offset value" | §II, p. 2 |
| Borrado completo de la estructura | "The purpose of forward diffusion is to entirely erase the original data structure" | §II, p. 2 |
| Codificacion de la mascara | "polyp regions are labeled '1' and normal regions '0'" | §II, p. 2 |
| Denoiser | "U-Net architecture with initial feature maps of 64 channels" | §II, p. 2 |
| Embedding temporal | "sinusoidal position embeddings to encode the timestep (t)" | §II, p. 2 |
| Bloques | "wide ResNet blocks, consisting of 2D convolutional layers, fully connected layers, group normalization" | §II, p. 2 |
| Bloques (cont.) | "SiLU activation layers, and skip connections" | §II, p. 2 |
| Concatenacion en cada paso | "concatenating it channel-wise with the segmentation mask image (c) at each timestep (t)" | §II, p. 2 |
| Canales de imagen y mascara | "As both the image and mask contain three channels" | §II, p. 2 |
| Entrada de 6 canales | "this process results in a 6-channel input for the model" | §II, p. 2 |
| Dimensiones w, h | "where w and h are the width and height of the image" | §II, p. 2 |
| Objetivo de entrenamiento | "The model is trained to predict the noise added to the input data" | §II, p. 2 |
| Paso inverso | Ec. (3): σ_t = sqrt(β_t), β_t ∈ (0,1) | §II, Ec. (3), p. 2 |
| Mascaras sin generador | "there is no need for specialized generative models to produce them" | §II, p. 2 |
| Naturaleza de la mascara | "straightforward binary nature of these masks" | §II, p. 2 |
| Aumentacion de mascaras (incluye elastica) | "augmentations such as rotation, shifting, scaling, and elastic deformation can be applied" | §II, p. 2 |
| Entrenamiento (Fig. 1a) | "transform random noise into realistic polyp images by conditioning on a binary segmentation mask" | Fig. 1, p. 2 |
| Inferencia (Fig. 1c) | "performs inference on a given input mask to generate corresponding synthetic images" | Fig. 1, p. 2 |
| Diversidad por mascara | "showcasing the diversity of synthetic images generated from a single input mask" | Fig. 2, p. 3 |
| Muestras con mascaras aumentadas | "Synthetic image samples generated by conditioning on augmented masks derived from the original mask images" | Fig. 3, p. 3 |
| Tipos de aumentacion en Fig. 3 | "Original", "Elastic Deformed", "Rotated", "Shifted", "Scaled Up", "Scaled Down" | Fig. 3, p. 3 |
| Particion | "employing the same train and test splits as those used by LDM [9]" | §III, p. 3 |
| Resolucion | "The images were resized to 256x256 pixels" | §III, p. 3 |
| Rango de intensidad | "pixel intensity was rescaled to the range [-1, 1]" | §III, p. 3 |
| n train / test del generador | "Our model was trained using 900 images and subsequently tested on 100 test images" | §III, p. 3 |
| Baselines preentrenados | "employed pretrained models of LDM [9] and SinGAN-Seg [6] from their official repositories" | §III, p. 3 |
| Entrenamiento de SinGAN-Seg | "trained on 1000 images from the HyperKvasir dataset [7] and incorporated style transfer" | §III, p. 3 |
| Comparacion reconocida como desigual | "presented an unfair comparison" | §III, p. 3 |
| Iteraciones, lr, batch | "trained using 100,000 iterations with a learning rate of 10-4, a batch size of 32" | §III, p. 3 |
| Canales, pasos, perdida | "64 input channels, employing only 250 timesteps, and utilizing an L1 loss function" | §III, p. 3 |
| Aumentacion en entrenamiento | "augmentation techniques such as rotation, horizontal flipping, and random rotation" | §III, p. 3 |
| Segmentacion llamada cualitativa | "as a qualitative evaluation of synthetic images, we utilized the same segmentation models" | §III, p. 3 |
| Segmentadores | "UNet++, FPN, and DeepLabv3plus—as [9]" | §III, p. 3 |
| Epocas de segmentacion | "altering the number of epochs to 100" | §III, p. 3 |
| Esquema R (baseline) | "initially trained on 900 real images from the Kvasir-SEG training set to establish baseline scores" | §III, p. 3 |
| Esquema S | "exclusively on synthetic images to evaluate their potential as substitutes" | §III, pp. 3-4 |
| Esquema R+S | "trained on a combination of real and synthetic images to assess their data augmentation capabilities" | §III, p. 4 |
| S900 | "900 synthetic images were generated based on the mask images from the HyperKvasir dataset" | §III, p. 4 |
| Limite de SinGAN-Seg | "SinGAN-Seg can only use the mask images from its default training set" | §III, p. 4 |
| S1000 | "we created 1,000 synthetic images conditioned on new segmentation masks" | §III, p. 4 |
| Origen de mascaras S1000 | "derived by augmenting the original mask images from the Kvasir-SEG training set" | §III, p. 4 |
| Exclusion de SinGAN-Seg en S1000 | "because it cannot generate images based on new segmentation masks" | §III, p. 4 |
| Test sets 1-2 | "100 test images from the Kvasir-SEG dataset, 1,000 images from the HyperKvasir dataset" | §III, p. 4 |
| Test set 3 | "and 196 images from the ETIS-LaribPolypDB dataset [13]" | §III, p. 4 |
| Metricas de imagen | "Fréchet Inception Distance (FID), Inception Score (IS), and Kernel Inception Distance (KID)" | §III, p. 4 |
| n sinteticas para FID/IS/KID | "comparing 1,000 synthetic images, generated based on mask images from the HyperKvasir dataset" | §III, p. 4 |
| n reales para FID/IS/KID | "with 1,000 real images" | §III, p. 4 |
| Conjuntos de referencia | "against real images from two different datasets: Kvasir-SEG and HyperKvasir" | §III, p. 4 |
| Metricas downstream | "Intersection over Union (IoU), F1 Score, Accuracy, and Precision scores" | §III, p. 4 |
| Hardware | "trained on a Tesla V100-SXM2 32 GB GPU card" | §III, p. 4 |
| HyperKvasir no visto por Polyp-DDPM | "serves as unseen data for our proposed method and LDM" | §III-A, p. 4 |
| Colapso de SinGAN-Seg | "suffers from mode collapse and produces only slightly varied images" | §III-A, p. 4 |
| Comparacion con LDM | "our model is able to generate more diverse images with precise details than LDM" | §III-A, p. 4 |
| Evaluacion visual (evaluador no especificado) | "Visual assessment of these comparisons reveals" | §III-A, p. 4 |
| FID/KID propios en Kvasir-SEG | "lowest Fréchet Inception Distance (FID) score of 78.47 and the Kernel Inception Distance (KID)" / "score of 0.07" | §III-A, p. 4 |
| FID/KID propios en HyperKvasir | "an FID of 81.10 and a KID of 0.07 on real images" | §III-A, p. 4 |
| LDM en Kvasir-SEG | "LDM had the second-best scores with an FID of 95.82 and a KID of 0.09" | §III-A, p. 4 |
| LDM en HyperKvasir | "an FID of 97.01 and a KID of 0.09 on the HyperKvasir dataset" | §III-A, p. 4 |
| SinGAN-Seg en HyperKvasir | "SinGAN-Seg recorded significantly higher FID and KID scores of 131.33 and 0.14" | §III-A, p. 4 |
| IS de SinGAN-Seg | "SinGAN-Seg achieved the highest Inception Score" | §III-A, p. 4 |
| Criterio de resaltado Tabla I | "The best scores are highlighted in bold." | Tabla I, p. 4 |
| Condicion de Tabla I | "Synthetic images generated based on mask images from the HyperKvasir dataset." | Tabla I, p. 4 |
| Columnas Tabla I | Kvasir-SEG: FID↓ IS↑ KID↓ \| HyperKvasir: FID↓ IS↑ KID↓ | Tabla I, p. 4 |
| Tabla I LDM [9] | 95.8243 2.3096 0.0920 \| 97.0121 2.3096 0.0942 | Tabla I, p. 4 |
| Tabla I SinGAN-Seg [6] | 141.1729 3.5943 0.1553 \| 131.3347 3.3607 0.1468 | Tabla I, p. 4 |
| Tabla I Ours | 78.4797 2.7361 0.0704 \| 81.1045 2.7361 0.0755 | Tabla I, p. 4 |
| Tabla I "[10] vs [7]" | 3.6111 3.2925 0.0000 \| 3.6111 3.2925 0.0000 | Tabla I, p. 4 |
| T1 UNet++ S900 | "the UNet++ model attained an IoU score of 0.7156 and an F1 score of 0.8342" | §III-B, p. 4 |
| T1 UNet++ S900 baselines | "achieved IoUs of 0.6828 and 0.6694, and F1 scores of 0.8115 and 0.8020" | §III-B, p. 4 |
| T1 UNet++ R900 | "results obtained using 900 real images (IoU 0.7067, F1 score 0.8281)" | §III-B, p. 4 |
| T1 FPN/DLv3+ S900 | "IoU scores of 0.7027 and 0.6999, and F1 scores of 0.8254 and 0.8235" | §III-B, p. 4 |
| T1 FPN/DLv3+ R900 | "which recorded IoUs of 0.7730 and 0.7217, and F1 scores of 0.8720 and 0.8384" | §III-B, p. 4 |
| T1 S1000 Polyp-DDPM | "achieving IoU scores of 0.7081 for UNet++, 0.6914 for FPN, and 0.6908" | §III-B, p. 4 |
| T1 S1000 LDM | "LDM recorded IoU scores of 0.6235 for UNet++, 0.6290 for FPN, and 0.6425" | §III-B, p. 5 |
| Afirmacion sobre mixtos | "generally improved performance across all models, showcasing the augmentative capability of synthetic images" | §III-B, p. 5 |
| T1 R900+S900 Polyp-DDPM | "Polyp-DDPM achieved IoU scores of 0.7484 on UNet++, 0.7730 on FPN, and 0.7496" | §III-B, p. 5 |
| T1 R900+S1000 Polyp-DDPM | "achieved IoUs of 0.7448 on UNet++, 0.7380 on FPN, and" / "0.7364 on DeepLabv3plus" | §III-B, pp. 5-6 |
| T1 R900+S900 SinGAN-Seg | "the SinGAN-Seg model achieved superior results, recording an IoU of 0.7792 on UNet++" | §III-B, p. 6 |
| T1 R900+S1000 LDM | "LDM also showed superior results on FPN and DeepLabv3plus" / "achieving an IoU of 0.7065" | §III-B, p. 6 |
| T2 S900 Polyp-DDPM | "IoUs of 0.7739, 0.7735, and 0.7723 and F1 scores of 0.8725, 0.8723, and 0.8715" | §III-B, p. 6 |
| T2 SinGAN-Seg | "SinGAN-Seg model did not show superior results in this experiment" | §III-B, p. 6 |
| T3 afirmacion | "notable improvements were achieved by the Polyp-DDPM model when trained with synthetic images" | §III-B, p. 6 |
| T3 S900 Polyp-DDPM | "yielded IoU scores of 0.5295 for UNet++, 0.5530 for FPN, and 0.5682 for DeepLabv3plus" | §III-B, p. 6 |
| T3 R900 | "which were 0.6329 for UNet++, 0.6242 for FPN, and 0.5262 for DeepLabv3plus" | §III-B, p. 6 |
| T3 R900+S900 Polyp-DDPM | "IoU scores reaching 0.6028 (UNet++), 0.6516 (FPN), and 0.6544 (DeepLabv3plus)" | §III-B, p. 6 |
| T3 patron generalizado | "consistently observed in experiments involving 1,000 synthetic images" / "across all metrics" | §III-B, p. 6 |
| Conclusion mixtos | "Polyp-DDPM demonstrated superior results with the UNet++ model, while LDM achieved higher accuracy" | §IV, p. 6 |
| Limitacion declarada | "the performance of synthetic images alone did not always match that of real images" | §IV, p. 6 |
| Afirmacion de cierre | "not only sets a new benchmark in synthetic image generation for medical imaging" | §IV, p. 6 |
| Parametros de segmentadores | "UNet++ (26.1M)" / "FPN (23.2M)" / "DeepLabv3plus (22.4M)" | Tabla 2, p. 5 |
| Definicion R / S | "'R' denotes real images (the baseline), 'S' indicates synthetic images used in training" | Tabla 2, p. 5 |
| Criterio de resaltado Tabla 2 | "Best results are highlighted in bold, relative to the baseline." | Tabla 2, p. 5 |
| Test sets de Tabla 2 | "Test 100 images of Kvasir-SEG dataset" / "1000 images of HyperKvasir dataset" / "196 images of ETIS-LaribPolypDB dataset" | Tabla 2 (notas a-c), p. 5 |
| Orden de columnas Tabla 2 | IoU / F1 / Acc / Prec para UNet++ \| FPN \| DeepLabv3plus | Tabla 2, p. 5 |
| T1 R900 | 0.7067 0.8281 0.9460 0.8383 \| 0.7730 0.8720 0.9596 0.8786 \| 0.7217 0.8384 0.9461 0.8012 | Tabla 2, p. 5 |
| T1 S900 LDM | 0.6694 0.8020 0.9361 0.7905 \| 0.6391 0.7798 0.9215 0.7035 \| 0.6780 0.8081 0.9365 0.7779 | Tabla 2, p. 5 |
| T1 S900 SinGAN-Seg | 0.6828 0.8115 0.9372 0.7758 \| 0.6560 0.7922 0.9386 0.8564 \| 0.6520 0.7894 0.9343 0.8042 | Tabla 2, p. 5 |
| T1 S900 Polyp-DDPM | 0.7156 0.8342 0.9464 0.8203 \| 0.7027 0.8254 0.9432 0.8075 \| 0.6999 0.8235 0.9445 0.8324 | Tabla 2, p. 5 |
| T1 R900+S900 LDM | 0.7466 0.8549 0.9553 0.8832 \| 0.7459 0.8545 0.9528 0.8376 \| 0.7456 0.8542 0.9537 0.8541 | Tabla 2, p. 5 |
| T1 R900+S900 SinGAN-Seg | 0.7792 0.8759 0.9602 0.8684 \| 0.7710 0.8707 0.9597 0.8882 \| 0.7488 0.8564 0.9546 0.8609 | Tabla 2, p. 5 |
| T1 R900+S900 Polyp-DDPM | 0.7484 0.8561 0.9545 0.8616 \| 0.7730 0.8720 0.9594 0.8734 \| 0.7496 0.8569 0.9554 0.8744 | Tabla 2, p. 5 |
| T1 S1000 LDM | 0.6235 0.7681 0.9167 0.6890 \| 0.6290 0.7723 0.9214 0.7160 \| 0.6425 0.7823 0.9248 0.7243 | Tabla 2, p. 5 |
| T1 S1000 Polyp-DDPM | 0.7081 0.8291 0.9450 0.8195 \| 0.6914 0.8176 0.9380 0.7682 \| 0.6908 0.8171 0.9388 0.7780 | Tabla 2, p. 5 |
| T1 R900+S1000 LDM | 0.7065 0.8280 0.9460 0.8382 \| 0.7445 0.8535 0.9545 0.8741 \| 0.7409 0.8512 0.9530 0.8574 | Tabla 2, p. 5 |
| T1 R900+S1000 Polyp-DDPM | 0.7448 0.8537 0.9533 0.8499 \| 0.7380 0.8492 0.9518 0.8443 \| 0.7364 0.8482 0.9505 0.8272 | Tabla 2, p. 5 |
| T2 R900 | 0.8921 0.9430 0.9825 0.9442 \| 0.9105 0.9532 0.9856 0.9547 \| 0.8903 0.9420 0.9818 0.9254 | Tabla 2, p. 5 |
| T2 S900 LDM | 0.7167 0.8349 0.9493 0.8371 \| 0.6743 0.8055 0.9330 0.7278 \| 0.7162 0.8346 0.9475 0.8104 | Tabla 2, p. 5 |
| T2 S900 SinGAN-Seg | 0.7201 0.8373 0.9476 0.8024 \| 0.6866 0.8142 0.9463 0.8704 \| 0.6889 0.8158 0.9429 0.8095 | Tabla 2, p. 5 |
| T2 S900 Polyp-DDPM | 0.7739 0.8725 0.9604 0.8649 \| 0.7735 0.8723 0.9600 0.8585 \| 0.7723 0.8715 0.9603 0.8687 | Tabla 2, p. 5 |
| T2 R900+S900 LDM | 0.8940 0.9440 0.9829 0.9521 \| 0.8900 0.9418 0.9819 0.9312 \| 0.8914 0.9426 0.9823 0.9418 | Tabla 2, p. 5 |
| T2 R900+S900 SinGAN-Seg | 0.8931 0.9435 0.9824 0.9342 \| 0.8741 0.9328 0.9794 0.9350 \| 0.8630 0.9264 0.9773 0.9237 | Tabla 2, p. 5 |
| T2 R900+S900 Polyp-DDPM | 0.8930 0.9434 0.9826 0.9442 \| 0.9060 0.9507 0.9848 0.9514 \| 0.9030 0.9490 0.9844 0.9519 | Tabla 2, p. 5 |
| T2 S1000 LDM | 0.6450 0.7842 0.9242 0.6980 \| 0.6657 0.7993 0.9312 0.7251 \| 0.6798 0.8094 0.9377 0.7648 | Tabla 2, p. 5 |
| T2 S1000 Polyp-DDPM | 0.7722 0.8714 0.9602 0.8668 \| 0.7658 0.8674 0.9574 0.8324 \| 0.7549 0.8604 0.9552 0.8267 | Tabla 2, p. 5 |
| T2 R900+S1000 LDM | 0.8351 0.9101 0.9720 0.8998 \| 0.8811 0.9368 0.9807 0.9464 \| 0.8940 0.9440 0.9829 0.9503 | Tabla 2, p. 5 |
| T2 R900+S1000 Polyp-DDPM | 0.8895 0.9415 0.9820 0.9430 \| 0.8770 0.9345 0.9796 0.9248 \| 0.8805 0.9365 0.9802 0.9266 | Tabla 2, p. 5 |
| T3 R900 | 0.6329 0.7752 0.9784 0.7343 \| 0.6242 0.7686 0.9783 0.7425 \| 0.5262 0.6895 0.9664 0.5926 | Tabla 2, p. 5 |
| T3 S900 LDM | 0.3664 0.5363 0.9431 0.4250 \| 0.2544 0.4056 0.8845 0.2644 \| 0.2434 0.3915 0.8800 0.2541 | Tabla 2, p. 5 |
| T3 S900 SinGAN-Seg | 0.3209 0.4859 0.9457 0.4250 \| 0.3150 0.4791 0.9445 0.4168 \| 0.2358 0.3816 0.9022 0.2673 | Tabla 2, p. 5 |
| T3 S900 Polyp-DDPM | 0.5295 0.6923 0.9680 0.6131 \| 0.5530 0.7122 0.9705 0.6373 \| 0.5682 0.7246 0.9739 0.6940 | Tabla 2, p. 5 |
| T3 R900+S900 LDM | 0.5978 0.7483 0.9752 0.6922 \| 0.5647 0.7218 0.9704 0.6277 \| 0.4851 0.6533 0.9597 0.5353 | Tabla 2, p. 5 |
| T3 R900+S900 SinGAN-Seg | 0.5472 0.7074 0.9701 0.6357 \| 0.5007 0.6673 0.9634 0.5675 \| 0.4790 0.6477 0.9618 0.5564 | Tabla 2, p. 5 |
| T3 R900+S900 Polyp-DDPM | 0.6028 0.7522 0.9753 0.6889 \| 0.6516 0.7890 0.9799 0.7525 \| 0.6544 0.7911 0.9819 0.8289 | Tabla 2, p. 5 |
| T3 S1000 LDM | 0.1837 0.3104 0.8284 0.1897 \| 0.3031 0.4652 0.9173 0.3289 \| 0.2294 0.3732 0.8749 0.2414 | Tabla 2, p. 5 |
| T3 S1000 Polyp-DDPM | 0.5059 0.6719 0.9651 0.5845 \| 0.5026 0.6689 0.9638 0.5705 \| 0.4555 0.6259 0.9555 0.5053 | Tabla 2, p. 5 |
| T3 R900+S1000 LDM | 0.4731 0.6424 0.9589 0.5301 \| 0.5358 0.6977 0.9691 0.6260 \| 0.6093 0.7572 0.9770 0.7259 | Tabla 2, p. 5 |
| T3 R900+S1000 Polyp-DDPM | 0.6530 0.7901 0.9805 0.7723 \| 0.6399 0.7804 0.9795 0.7566 \| 0.5804 0.7345 0.9744 0.6928 | Tabla 2, p. 5 |
| Recomposicion del fondo original / inpainting | NO ENCONTRADO EN EL PDF | — |
| Mecanismo que relacione contenido fuera de la mascara con el objeto | NO ENCONTRADO EN EL PDF | — |
| Metrica de fidelidad o cambios fuera de la mascara | NO ENCONTRADO EN EL PDF | — |
| Metrica de correspondencia mascara-imagen generada | NO ENCONTRADO EN EL PDF | — |
| Evaluacion clinica/experta o identidad de quien hizo la evaluacion visual | NO ENCONTRADO EN EL PDF | — |
| Dice o HD95 como metrica | NO ENCONTRADO EN EL PDF | — |
| Semillas, repeticiones o pruebas de significancia | NO ENCONTRADO EN EL PDF | — |
| Supuesto explicito de tejido deformable / no rigido | NO ENCONTRADO EN EL PDF | — |
| Metal, implantes, objetos de alta intensidad o artefactos | NO ENCONTRADO EN EL PDF | — |
| CT, HU o ventanas de intensidad | NO ENCONTRADO EN EL PDF | — |
| Variante 2.5D o 3D de Polyp-DDPM | NO ENCONTRADO EN EL PDF | — |
| Como se replica la mascara binaria a tres canales | NO ENCONTRADO EN EL PDF | — |
| Optimizador del generador | NO ENCONTRADO EN EL PDF | — |
| Valor del offset s del schedule coseno | NO ENCONTRADO EN EL PDF | — |
| Numero de pasos de muestreo en inferencia (distinto de los 250 de entrenamiento) | NO ENCONTRADO EN EL PDF | — |
| Niveles del U-Net, ubicacion de atencion, numero de parametros del generador | NO ENCONTRADO EN EL PDF | — |
| Criterio de seleccion del checkpoint del generador | NO ENCONTRADO EN EL PDF | — |
| Parametros de la aumentacion de mascaras (angulos, rangos de escala, deformacion elastica) | NO ENCONTRADO EN EL PDF | — |
| Hiperparametros de segmentacion distintos de las epocas (lr, perdida, encoder) | NO ENCONTRADO EN EL PDF | — |
| Seleccion de las 900 mascaras HyperKvasir para S900 | NO ENCONTRADO EN EL PDF | — |
| Implementacion de FID/IS/KID (extractor, subconjuntos KID) | NO ENCONTRADO EN EL PDF | — |
| Definicion textual de la fila "[10] vs [7]" de Tabla I | NO ENCONTRADO EN EL PDF | — |
| Tiempo de entrenamiento o de inferencia | NO ENCONTRADO EN EL PDF | — |
| Numeros de pagina impresos del proceedings | NO ENCONTRADO EN EL PDF | — |
| Identificador arXiv:2402.04031 | NO ENCONTRADO EN EL PDF | — |
