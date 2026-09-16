# macháček2023 — Difusion latente condicionada por mascara para generar imagenes de polipos GI

- **DOI / URL:** 10.1145/3592571.3592978 ("https://doi.org/10.1145/3592571.3592978", p. 1). Version leida:
  ICDAR '23 (4th Workshop on Intelligent Cross-Data Analysis and Retrieval), ACM, 9 pp.
  Codigo: https://github.com/simulamet-host/conditional-polyp-diffusion (§1, p. 2). Rango de
  paginas en el proceedings: NO ENCONTRADO EN EL PDF. Identificador arXiv (zhang2025diffboost
  lo cita como arXiv:2304.05233): NO ENCONTRADO EN EL PDF.
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/macháček2023.pdf

## Que hace (3 lineas maximo)
Sistema "totalmente sintetico" en dos etapas para endoscopia GI 2D: un improved DDPM genera
mascaras binarias de polipo (Kvasir-SEG) y un LDM condicionado por mascara genera la imagen
COMPLETA desde ruido. Evalua con FID/SIM y con segmentacion downstream (UNet++, FPN, DeepLabv3+).

## Restriccion o supuesto clave
**1. Imagen completa, no inpainting.** No hay imagen receptora ni fondo original que recomponer:
- "We introduce a fully synthetic polyp generation system." (§1, p. 2)
- "generate high-fidelity synthetic polyp images conditioned on pre-generated synthetic polyp masks"
  (§1, p. 2)
- Cada muestra cambia toda la escena: "stochastic polyps generations with different input noises"
  (Fig. 5, p. 6).
- El inpainting solo se menciona como capacidad general del LDM ("exceptional results in tasks
  related to image inpainting", §3.2, p. 3) y en trabajo ajeno (PolypConnect [10], §2, p. 2); el
  metodo propio no inpaintea. Recomposicion del fondo original: NO ENCONTRADO EN EL PDF.
- Fuera de la mascara TODO se genera, por diseno, pero como contexto generico: ningun mecanismo
  liga el contenido fuera de la mascara al objeto sintetizado, y ninguna metrica mide fidelidad o
  cambios fuera de la mascara (NO ENCONTRADO EN EL PDF).

**2. Arquitectura (lo que dice y lo que no).**
- LDM de Rombach et al.: "developed by CompVis and trained on the LAION-400M dataset" (§3.2, p. 3);
  Fig. 1 rotula la caja verde "Pre-Trained Latent Diffusion" (p. 3). Si se ajusta desde esos
  pesos o se entrena desde cero: NO ENCONTRADO EN EL PDF (Tabla 2 reporta epocas 88 a 922).
- VAE/autoencoder concreto, factor de compresion, reentrenamiento: NO ENCONTRADO EN EL PDF; solo
  "operates through a series of denoising autoencoders and diffusion models" (§3.2, p. 3).
- Como entra la mascara (concatenacion, ControlNet, cross-attention): NO ENCONTRADO EN EL PDF en
  el texto. Fig. 1 solo dibuja bloques "Q KV" en el "Denoising U-Net" y flechas "Train Condition"
  / "Conditions to Generate Polyps" (p. 3), sin explicacion. Observacion visual, no textual: el
  panel "Condition" de Fig. 4 (p. 5) es un mapa coloreado, mientras Fig. 5 (p. 6) muestra mascaras
  binarias.
- Resolucion, canales/espacio de color, muestreador y pasos: NO ENCONTRADO EN EL PDF. Es 2D por
  construccion (imagenes endoscopicas); la palabra "2D" no aparece.

**3. Supuesto que le impide manejar implantes metalicos rigidos.**
- Supuesto explicito de tejido deformable/no rigido: NO ENCONTRADO EN EL PDF.
- Implicito: la forma del objeto es una muestra de una distribucion aprendida y se busca que
  varie: "Note the variability of shapes and amount of polyps in the generated masks." (Fig. 2,
  p. 5); "they should differ in other aspects, such as rotation." (§3.3, p. 3). Es lo opuesto a
  una geometria CAD rigida y fija.
- Sin anatomia receptora: al generar la escena entera no puede insertar un objeto en un volumen
  dado conservando la anatomia del paciente, que es lo que exige el renderizador de la tesis.
- La condicion es solo forma binaria: no hay intensidad del objeto, ni fisica, ni relacion
  objeto-entorno. Metal, alta intensidad, artefactos, HU, CT: NO ENCONTRADO EN EL PDF.
- No mide si la imagen generada respeta la mascara (correspondencia mascara-imagen: NO ENCONTRADO
  EN EL PDF); la validez de las etiquetas solo se infiere indirectamente por la segmentacion.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna cifra necesaria (downstream fuera de alcance). Solo mecanismo, si se cita: | | |
| Generacion de imagen completa desde ruido | "stochastic polyps generations with different input noises" | Fig. 5, p. 6 |
| Sistema sin imagen real de fondo | "We introduce a fully synthetic polyp generation system." | §1, p. 2 |

## Donde entra en mi tesis
- Related Work / Problem Statement (`tesis/main.tex` l. 48): encaja en la familia "Globally
  conditioned methods" junto a DiffBoost (sintesis de la imagen entera desde ruido). Difiere en que
  condiciona con la mascara de region, no con su borde; si se cita como segundo ejemplo, la
  clausula "using the mask only as an edge constraint" debe quedar atribuida solo a DiffBoost.
- Reclamo de novedad de B_delta: no lo reduce. Genera todo fuera de la mascara, pero sin
  mecanismo ni senal de entrenamiento que relacione esas intensidades con el objeto, y sin medirlas.
- La frase "None of these works states an assumption of tissue non-rigidity" sigue siendo
  correcta para este paper.

## Dudas para el asesor
1. Vale la pena citarlo como segundo ejemplo de la familia global (workshop ACM) o basta DiffBoost?
2. Inconsistencia a no heredar: el texto afirma "precision is always better when the synthetic data
   is in the training data" (§4.2, p. 4), pero en Tabla 3 (p. 7) la precision de 700R+1000S es menor
   que la de 700R+0S en los tres modelos (0.8235 vs 0.8535; 0.8323 vs 0.8623; 0.8252 vs 0.8699), y
   lo mismo en Tabla 4 (0.8517 vs 0.8742; 0.8504 vs 0.8761; 0.8628 vs 0.8678).
3. §3.1 dice que el improved DDPM se entrena "to generate synthetic polyp images" (p. 2) cuando
   genera mascaras, y describe el muestreo "by first adding noise to a randomly selected mask image
   from the training set" (pp. 2-3), lo que sugiere partir de mascaras reales ruidosas; no se aclara.
4. Observacion visual (no textual): las imagenes generadas de Fig. 5 (p. 6) reproducen un recuadro
   negro en la esquina inferior izquierda y el recorte octogonal del endoscopio, o sea contenido de
   adquisicion fuera de la mascara aprendido de los datos, no inducido por el objeto.

## Evidencia textual
| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| DOI | "https://doi.org/10.1145/3592571.3592978" | Pie y ACM Reference Format, p. 1 |
| Venue y fecha | "ICDAR '23, June 12–15, 2023, Thessaloniki, Greece" | p. 1 |
| Workshop | "4th Workshop on Intelligent Cross-Data Analysis and Retrieval (ICDAR '23)" | ACM Reference Format, p. 1 |
| Extension | "ACM, New York, NY, USA, 9 pages." | ACM Reference Format, p. 1 |
| ISBN | "ACM ISBN 979-8-4007-0186-3/23/06" | Pie, p. 1 |
| Keywords | "diffusion model, polyp generative model, polyp segmentation, generating synthetic data" | p. 1 |
| Tipo de marco | "conditional DPM framework to generate synthetic gastrointestinal (GI) polyp images" | Abstract, p. 1 |
| Cantidad generable | "our system can generate an unlimited number of high-fidelity synthetic polyp images" | Abstract, p. 1 |
| Resultado titular | "the best micro-imagewise intersection over union (IOU) of 0.7751 was achieved from DeepLabv3+" | Abstract, p. 1 |
| Dependencia de arquitectura | "achieving good segmentation performance with synthetic data heavily depends on model architectures." | Abstract, p. 1 |
| Sistema sin imagen real | "We introduce a fully synthetic polyp generation system." | §1, p. 2 |
| Imagen condicionada por mascara | "generate high-fidelity synthetic polyp images conditioned on pre-generated synthetic polyp masks" | §1, p. 2 |
| Datos sinteticos publicados | "https://huggingface.co/datasets/deepsynthbody/conditional-polyp-diffusion" | §1, p. 2 |
| Cifra ajena (PolypConnect [10]) | "The results show 5.1% improvement in mean intersection over union (IOU)" | §2, p. 2 |
| PolypConnect es conversion/inpainting | "which can convert non-polyp images into polyp images" | §2, p. 2 |
| Generador de mascaras | "we use an improved diffusion model [25] to generate synthetic polyp masks" | §3.1, p. 2 |
| Dataset de mascaras | "capture the distribution of the masks of the Kvasir-SEG dataset" | §3.1, p. 2 |
| Redaccion confusa (imagenes vs mascaras) | "used to train the improved diffusion model to generate synthetic polyp images" | §3.1, p. 2 |
| Muestreo descrito desde mascara real | "by first adding noise to a randomly selected mask image from the training set" | §3.1, pp. 2-3 |
| Reversion del ruido | "This noise would then be gradually reversed through multiple steps" | §3.1, p. 3 |
| Caja verde de Fig. 1 | "The green box represents the conditional latent diffusion model" | Fig. 1, p. 3 |
| Rotulo del LDM | "Pre-Trained Latent Diffusion" | Fig. 1, p. 3 |
| Rotulos de condicion | "Train Condition" / "Conditions to Generate Polyps" / "Denoising U-Net" con "Q KV" | Fig. 1, p. 3 |
| Origen del LDM | "developed by CompVis and trained on the LAION-400M dataset [32]" | §3.2, p. 3 |
| Componentes del LDM | "operates through a series of denoising autoencoders and diffusion models" | §3.2, p. 3 |
| Inpainting solo como capacidad general | "has shown exceptional results in tasks related to image inpainting [9]" | §3.2, p. 3 |
| Justificacion por pocos datos | "they can be trained with a limited amount of real data points" | §3.2, p. 3 |
| Criterio FID | "compares the distribution of the generated images compared to real images" | §3.3, p. 3 |
| Definicion sim(r,g) | "number of pixels that are same for both images divided by the total area" | §3.3, p. 3 |
| Formula sim | "sim(r, g) = #(r == g) / (width ∗ height)" | §3.3, p. 3 |
| Vecino mas cercano r* | "we find the closest real image r∗ as the real image with the highest similarity" | §3.3, p. 3 |
| Definicion SIM(R,G) | "we simply take average of the pairs with highest similarities." | §3.3, p. 3 |
| Interpretacion de SIM (variacion buscada) | "they should differ in other aspects, such as rotation." | §3.3, p. 3 |
| Segmentadores | "UNet++ [44], feature pyramid network (FPN) [22], and DeepLabv3+ [5]" | §3.4, p. 3 |
| Esquemas i-ii | "i) 700 of real polyp images; ii) using 1000 synthetic polyp images;" | §3.4, p. 3 |
| Esquema iii | "iii) a combination of 700 real and 1000 synthetic polyp images." | §3.4, p. 3 |
| Real fijo en 100 | "we fixed the number of real images to 100 samples" | §3.4, p. 3 |
| Barrido sintetico | "increased the number of synthetic samples from 0 to 1000 sequentially in steps of 100" | §3.4, p. 3 |
| Motivo de limitar a 100 | "limited this experiment to using only 100 real images because of the time limitation" | §3.4, p. 3 |
| Plan futuro 200-700 | "we will test with different number of real images from 200 to 700" | §3.4, p. 3 |
| Test | "We tested these models with 300 real images and masks" | §3.4, p. 3 |
| Test independiente | "which were not used to train either the diffusion model or the segmentation models." | §3.4, p. 3 |
| Origen del test | "(from the segmentation data of HyperKvasir dataset [4])" | §3.4, p. 3 |
| Metricas downstream | "measured micro and micro-imagewise IOU, F1, Accuracy, and Precision" | §3.4, p. 3 |
| Definicion micro | "pixels over all images and all classes and then computing scores" | §3.4, p. 3 |
| Definicion micro-imagewise | "summing TP, FP, FN, and TN pixels for each image" | §3.4, p. 3 |
| Promedio imagewise | "Finally, average scores over the dataset were calculated." | §3.4, p. 3 |
| Peso por imagen | "In the micro-imagewise calculations, all images contributed equally to the final score." | §3.4, p. 4 |
| Desbalance de clases | "the second method takes into account class imbalance for each image." | §3.4, p. 4 |
| Hardware | "Nvidia A100 80GB graphic processing units (GPUs), AMD EPYC 7763 64-cores processor with 2TB RAM" | §4, p. 4 |
| Software | "Pytorch [26], the Pytorch-lightning libraries, and the Pytorch segmentation library [14]" | §4, p. 4 |
| n para Tabla 1 (generadas) | "We have generated 1000 masks for each of our saved model" | §4.1, p. 4 |
| n para Tabla 1 (reales) | "compare them with 1000 real training masks in Table 1." | §4.1, p. 4 |
| Tabla 1 iteraciones | Iter: 0 / 50k / 100k / 150k / 200k / 230k | Tabla 1, p. 4 |
| Tabla 1 FID mascaras | 140.14 / 128.95 / 117.14 / 105.63 / 88.41 / 141.44 | Tabla 1, p. 4 |
| Tabla 1 SIM mascaras | 88.22 / 89.46 / 90.81 / 91.31 / 92.49 / 88.38 | Tabla 1, p. 4 |
| Modelo de mascaras elegido | "We selected the model from iteration 200, 000 based on the results from Table 1." | §4.1, p. 4 |
| Criterio de seleccion | "the model achieves lowest FID value together with high SIM values" | §4.1, p. 4 |
| Inspeccion visual | "We also inspected the generated masks visually to confirm this conclusion." | §4.1, p. 4 |
| Sin validacion clinica de mascaras | "would be required in order to determine if masks are correct." | §4.1, p. 4 |
| Limite de SIM | "high SIM score doesn't necessary imply that model is producing identical masks" | §4.1, p. 4 |
| Fig. 3 SIM ejemplos | 95.89 / 98.11 / 93.45 / 84.62 / 87.98 | Fig. 3, p. 5 |
| Variabilidad de forma buscada | "Note the variability of shapes and amount of polyps in the generated masks." | Fig. 2, p. 5 |
| n para Tabla 2 | "produced 1000 generated images which we used for further evaluation in Table 2." | §4.1, p. 4 |
| Tabla 2 epocas | Epoch: 88 / 103 / 135 / 892 / 913 / 922 | Tabla 2, p. 4 |
| Tabla 2 FID polipos | 119.34 / 113.83 / 104.78 / 112.66 / 150.97 / 150.85 | Tabla 2, p. 4 |
| Modelo de imagen elegido | "the model which achieved lowest FID score is at Epoch = 135." | §4.1, p. 4 |
| Degradacion tardia | "quality of generated images deteriorates at later stages of training, reason may be overfitting." | §4.1, p. 4 |
| Fig. 4 | "Generated synthetic polyps conditioned on the same mask illustrating changes in quality during training stages." | Fig. 4, p. 5 |
| Prueba de generalizacion | "We conditioned the model on one mask and generated multiple samples" | §4.1, p. 4 |
| Imagen completa desde ruido | "All other columns show the corresponding stochastic polyps generations with different input noises." | Fig. 5, p. 6 |
| lr y optimizador | "We used a learning rate of 0.0001 with the Adam optimizer [19]" | §4.2, p. 4 |
| Perdida | "DiceLoss [35] was used in the training process as the loss function" | §4.2, p. 4 |
| Encoder | "The encoder model of resnet34 was input as the encoder network for all three models" | §4.2, p. 4 |
| Epocas y checkpoint | "calculated from the best checkpoints and the test dataset after training 50 epochs" | §4.2, p. 4 |
| Solo reales mejor en FPN/UNet++ | "some models like FPN and UNet++ show the best IOU, F1, and accuracy" | §4.2, p. 4 |
| DeepLabv3 con sinteticos | "DeepLabv3 shows the best performance when some synthetic data is included in the training data" | §4.2, p. 4 |
| Mejor IoU imagewise | "the best micro-imagewise IOU of 0.7751 is achieved from DeepLabv3+" | §4.2, p. 4 |
| Afirmacion sobre precision (contradicha por Tablas 3-4) | "precision is always better when the synthetic data is in the training data" | §4.2, p. 4 |
| Mejor precision 100R+200S | "Unet++ and FPN shows best precision values (micro and micro-imagewise)" | §4.2, p. 4 |
| Configuracion de esa precision | "consist of 100 real samples and 200 synthetic samples" | §4.2, p. 4 |
| Advertencia metodologica | "should not conclude performance gain or degrade of using synthetic data" | §4.2, p. 4 |
| Criterio de Fig. 6 (base) | "The baseline predictions are from the model trained with only real data." | Fig. 6, p. 8 |
| Criterio de Fig. 6 (UNet++*) | "Unet++(*) is selected based on using the high IOU value in Table 3." | Fig. 6, p. 8 |
| Criterio de Fig. 6 (FPN*) | "FPN(*) is selected using the highest Precision in Tables 3 and 4." | Fig. 6, p. 8 |
| Criterio de Fig. 6 (DLab*) | "DeepLabv3(*)[Dlab(*)] is selected using high IOU values in Table 4." | Fig. 6, p. 8 |
| Conclusion sobre novedad | "the generated synthetic data are unique and realistic and not a simple copy" | §5, p. 4 |
| Conclusion downstream | "these improvements are correlated with model architectures." | §5, p. 4 |
| Limitacion declarada | "Generating multiple images conditioned on the same input to train the segmentation models" | §5, p. 6 |
| Mejora futura | "the quality of generated images can be improved using the style-transfer technique [11]" | §5, p. 6 |
| Evaluacion futura | "Cross-dataset evaluations should be performed to measure the effect of using synthetic data" | §5, p. 6 |
| Financiacion | "financially supported by the Research Council of Norway under contract 270053." | Acknowledgments, p. 6 |
| Tabla 3 definicion | "Micro metrics calculated on the test dataset (300 real images and masks)." | Tabla 3, p. 7 |
| Tabla 4 definicion | "These metrics take into account class imbalance." | Tabla 4, p. 7 |
| Criterio de resaltado | "The best value of each column is highlighted using underlined text." | Tablas 3-4, p. 7 |
| Parametros de modelos | "Unet++ (26.1M)" / "FPN (23.2M)" / "DeepLabv3plus (22.4M)" | Tablas 3-4, p. 7 |
| Orden de columnas | #R, #Syn, luego IOU / F1 / Acc / Prec para Unet++ \| FPN \| DeepLabv3plus | Tablas 3-4, p. 7 |
| T3 700R/0S | 0.7471 0.8552 0.9509 0.8535 \| 0.7663 0.8677 0.9571 0.8623 \| 0.7457 0.8543 0.9492 0.8699 | Tabla 3, p. 7 |
| T3 0R/1000S | 0.6852 0.8132 0.9375 0.8009 \| 0.6784 0.8084 0.9276 0.7685 \| 0.6580 0.7938 0.9301 0.7658 | Tabla 3, p. 7 |
| T3 700R/1000S | 0.7151 0.8339 0.9421 0.8235 \| 0.7300 0.8439 0.9481 0.8323 \| 0.7401 0.8506 0.9492 0.8252 | Tabla 3, p. 7 |
| T3 100R/0S | 0.6970 0.8215 0.9400 0.7912 \| 0.6840 0.8123 0.9371 0.8209 \| 0.6983 0.8224 0.9404 0.8304 | Tabla 3, p. 7 |
| T3 100R/100S | 0.6937 0.8192 0.9382 0.7692 \| 0.7304 0.8442 0.9501 0.8509 \| 0.7200 0.8372 0.9466 0.8305 | Tabla 3, p. 7 |
| T3 100R/200S | 0.7066 0.8281 0.9418 0.8804 \| 0.7382 0.8494 0.9466 0.8763 \| 0.7040 0.8263 0.9429 0.8383 | Tabla 3, p. 7 |
| T3 100R/300S | 0.7309 0.8445 0.9488 0.8536 \| 0.7269 0.8419 0.9459 0.8219 \| 0.7556 0.8608 0.9500 0.8521 | Tabla 3, p. 7 |
| T3 100R/400S | 0.6830 0.8116 0.9386 0.8333 \| 0.7304 0.8442 0.9459 0.8375 \| 0.7298 0.8438 0.9450 0.8342 | Tabla 3, p. 7 |
| T3 100R/500S | 0.6815 0.8106 0.9366 0.8152 \| 0.7244 0.8402 0.9421 0.8209 \| 0.7212 0.8380 0.9454 0.8427 | Tabla 3, p. 7 |
| T3 100R/600S | 0.7083 0.8292 0.9432 0.8287 \| 0.7284 0.8429 0.9491 0.8668 \| 0.7037 0.8261 0.9392 0.8405 | Tabla 3, p. 7 |
| T3 100R/700S | 0.7195 0.8369 0.9460 0.8420 \| 0.7436 0.8530 0.9498 0.8107 \| 0.7083 0.8292 0.9457 0.8347 | Tabla 3, p. 7 |
| T3 100R/800S | 0.6752 0.8061 0.9402 0.8495 \| 0.7387 0.8497 0.9462 0.8278 \| 0.7338 0.8465 0.9476 0.8770 | Tabla 3, p. 7 |
| T3 100R/900S | 0.7069 0.8283 0.9441 0.8319 \| 0.7290 0.8432 0.9463 0.8234 \| 0.7116 0.8315 0.9413 0.8171 | Tabla 3, p. 7 |
| T3 100R/1000S | 0.7513 0.8580 0.9506 0.8468 \| 0.7214 0.8382 0.9457 0.8126 \| 0.7154 0.8341 0.9401 0.8337 | Tabla 3, p. 7 |
| T4 700R/0S | 0.7551 0.8222 0.9509 0.8742 \| 0.7681 0.8429 0.9571 0.8761 \| 0.7528 0.8317 0.9492 0.8678 | Tabla 4, p. 7 |
| T4 0R/1000S | 0.7232 0.8013 0.9375 0.8128 \| 0.6977 0.7903 0.9276 0.7757 \| 0.7018 0.7896 0.9301 0.8062 | Tabla 4, p. 7 |
| T4 700R/1000S | 0.7442 0.8185 0.9421 0.8517 \| 0.7371 0.8128 0.9481 0.8504 \| 0.7751 0.8465 0.9492 0.8628 | Tabla 4, p. 7 |
| T4 100R/0S | 0.7136 0.8005 0.9400 0.7985 \| 0.6587 0.7613 0.9371 0.8039 \| 0.7116 0.8040 0.9404 0.8506 | Tabla 4, p. 7 |
| T4 100R/100S | 0.7146 0.7976 0.9382 0.7931 \| 0.7357 0.8212 0.9501 0.8483 \| 0.7183 0.8048 0.9466 0.8420 | Tabla 4, p. 7 |
| T4 100R/200S | 0.7433 0.8193 0.9418 0.8768 \| 0.7000 0.7842 0.9466 0.8856 \| 0.7197 0.8031 0.9429 0.8554 | Tabla 4, p. 7 |
| T4 100R/300S | 0.7392 0.8168 0.9488 0.8570 \| 0.7302 0.8126 0.9459 0.8357 \| 0.7337 0.8097 0.9500 0.8503 | Tabla 4, p. 7 |
| T4 100R/400S | 0.7097 0.7867 0.9386 0.8444 \| 0.7512 0.8268 0.9459 0.8683 \| 0.7366 0.8153 0.9450 0.8604 | Tabla 4, p. 7 |
| T4 100R/500S | 0.7088 0.7874 0.9366 0.8551 \| 0.7376 0.8200 0.9421 0.8410 \| 0.7264 0.8085 0.9454 0.8369 | Tabla 4, p. 7 |
| T4 100R/600S | 0.7238 0.7987 0.9432 0.8584 \| 0.7348 0.8147 0.9491 0.8639 \| 0.7054 0.7944 0.9392 0.8287 | Tabla 4, p. 7 |
| T4 100R/700S | 0.7230 0.7988 0.9460 0.8471 \| 0.7319 0.8147 0.9498 0.8010 \| 0.7317 0.8135 0.9457 0.8502 | Tabla 4, p. 7 |
| T4 100R/800S | 0.7081 0.7884 0.9402 0.8692 \| 0.7502 0.8274 0.9462 0.8622 \| 0.7548 0.8322 0.9476 0.8725 | Tabla 4, p. 7 |
| T4 100R/900S | 0.7244 0.8025 0.9441 0.8329 \| 0.7441 0.8242 0.9463 0.8534 \| 0.7314 0.8115 0.9413 0.8570 | Tabla 4, p. 7 |
| T4 100R/1000S | 0.7385 0.8145 0.9506 0.8495 \| 0.7302 0.8086 0.9457 0.8386 \| 0.7343 0.8125 0.9401 0.8574 | Tabla 4, p. 7 |
| Mecanismo de entrada de la mascara (concatenacion / ControlNet / cross-attention) | NO ENCONTRADO EN EL PDF | — |
| VAE/autoencoder concreto, factor de compresion, canales latentes | NO ENCONTRADO EN EL PDF | — |
| LDM ajustado desde pesos LAION o entrenado desde cero | NO ENCONTRADO EN EL PDF | — |
| Hiperparametros de entrenamiento de los generadores (lr, batch) | NO ENCONTRADO EN EL PDF | — |
| Resolucion de entrada/salida | NO ENCONTRADO EN EL PDF | — |
| Canales / espacio de color | NO ENCONTRADO EN EL PDF | — |
| Dataset y numero de imagenes para entrenar el LDM | NO ENCONTRADO EN EL PDF | — |
| Particion train/val de Kvasir-SEG | NO ENCONTRADO EN EL PDF | — |
| Muestreador y numero de pasos de inferencia | NO ENCONTRADO EN EL PDF | — |
| Conjunto de referencia del FID de Tabla 2 | NO ENCONTRADO EN EL PDF | — |
| Recomposicion del fondo original / inpainting propio | NO ENCONTRADO EN EL PDF | — |
| Error de reconstruccion del autoencoder | NO ENCONTRADO EN EL PDF | — |
| Metrica de fidelidad o cambios fuera de la mascara | NO ENCONTRADO EN EL PDF | — |
| Metrica de correspondencia mascara-imagen generada | NO ENCONTRADO EN EL PDF | — |
| Evaluacion clinica/experta de las imagenes generadas | NO ENCONTRADO EN EL PDF | — |
| Dice o HD95 como metrica de evaluacion | NO ENCONTRADO EN EL PDF | — |
| Semillas, repeticiones o pruebas de significancia | NO ENCONTRADO EN EL PDF | — |
| Supuesto explicito de tejido deformable / no rigido | NO ENCONTRADO EN EL PDF | — |
| Metal, implantes, objetos de alta intensidad o artefactos | NO ENCONTRADO EN EL PDF | — |
| CT, HU o ventanas de intensidad | NO ENCONTRADO EN EL PDF | — |
| Variante 2.5D o 3D | NO ENCONTRADO EN EL PDF | — |
| Rango de paginas en el proceedings | NO ENCONTRADO EN EL PDF | — |
| Identificador arXiv:2304.05233 | NO ENCONTRADO EN EL PDF | — |
