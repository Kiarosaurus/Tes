# zhang2023controlnet — Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet)

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. Identificador en el margen de la p. 1:
  "arXiv:2302.05543v3 [cs.CV] 26 Nov 2023". Venue (ICCV 2023): NO ENCONTRADO EN EL PDF
  (el archivo es la version arXiv v3, sin cabecera de conferencia). URL de codigo: NO
  ENCONTRADO EN EL PDF.
- **Nivel de lectura:** 2 (metodo) — PDF completo, 12 paginas (9 de texto + referencias).
  El material suplementario que el texto cita varias veces NO viene en el PDF.
- **Leido a fondo por la autora:** no
- **PDF:** papers/zhang2023controlnet.pdf

## Que hace (3 lineas maximo)

Congela un modelo de difusion texto-a-imagen preentrenado (Stable Diffusion) y entrena una copia de sus 12 bloques encoder + bloque medio que recibe una imagen de condicion espacial (bordes, profundidad, segmentacion, pose, bocetos).
La copia se conecta al modelo congelado con "zero convolutions" (1x1, pesos y bias en cero), de modo que al inicio no altera la salida; sus salidas se suman a las 12 skip-connections y al bloque medio del U-Net.
Evalua con estudio de usuarios, IoU de re-segmentacion en ADE20K, FID/CLIP y una ablacion sin zero convolutions y con una version "lite".

## Restriccion o supuesto clave

Tres supuestos, explicitos o implicitos, relevantes para implantes metalicos en CT.

1. **Todo el metodo descansa en un modelo base congelado y en su espacio latente fijo.**
   "ControlNet locks the production-ready large diffusion models" (Abstract, p. 1) y la
   copia entrenable "reuses their deep and robust encoding layers pretrained with billions
   of images" (Abstract, p. 1). La condicion se codifica para calzar con el latente de SD:
   "convert 512 × 512 pixel-space images into smaller 64 × 64 latent images" (§3.2, p. 5).
   El PDF no dice que pasa si el autoencoder (VAE) cambia, ni si habria que reentrenar el
   U-Net base: NO ENCONTRADO EN EL PDF. El VAE ni siquiera aparece dibujado en la Fig. 3
   (p. 4); solo text encoder, time encoder y bloques del U-Net llevan candado.
   *Observacion de la extractora (no afirmada por el paper):* si el VAE se reemplaza o
   reentrena, el U-Net congelado queda operando sobre un latente para el que no fue
   entrenado, y la ventaja que el paper atribuye a la copia preentrenada ("strong
   backbone", §3.1, p. 4) deja de estar respaldada por este PDF.
2. **Dominio de imagen natural, RGB, 512 x 512.** "All models are trained with
   general-domain data." (Fig. 7, p. 6). No hay imagen medica, monocanal, rango dinamico
   extendido ni unidades fisicas (HU): NO ENCONTRADO EN EL PDF.
3. **"Localizado" se afirma pero no se define ni se mide.** El paper habla de "spatially
   localized input conditions" (§1, p. 2), pero la inyeccion es aditiva sobre el mapa de
   caracteristicas completo en 13 puntos: "The outputs are added to the 12 skip-connections
   and 1 middle block of the U-net" (§3.2, p. 4). Ningun mecanismo confina el efecto a la
   region de la condicion y no hay metrica de preservacion fuera de ella: NO ENCONTRADO EN
   EL PDF. Ademas, ante condiciones ambiguas "the model tries to interpret input shapes"
   (Fig. 11, p. 8): el control es semantico, no una restriccion geometrica dura.

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Zero convolution = 1x1 con pesos y bias en cero | "1 × 1 convolution with both weight and bias initialized to zero" | Fig. 2 (leyenda), p. 3 |
| Copia de 12 bloques encoder + 1 bloque medio | "trainable copy of the 12 encoding blocks and 1 middle block of Stable Diffusion" | §3.2, p. 4 |
| Inyeccion en 12 skip-connections + bloque medio | "The outputs are added to the 12 skip-connections and 1 middle block of the U-net" | §3.2, p. 4 |
| Base SD 1.5 (o 2.1) | "Stable Diffusion V1.5 (or V2.1, as they use the same U-net architecture)" | Fig. 3 (leyenda), p. 4 |
| Latente 64x64 desde 512x512 | "convert 512 × 512 pixel-space images into smaller 64 × 64 latent images" | §3.2, p. 5 |
| +23% memoria, +34% tiempo por iteracion (A100 40GB) | "requires only about 23% more GPU memory and 34%" | §3.2, pp. 4-5 |
| Robusto con <50k y >1m | "robust with small (<50k) and large (>1m) datasets" | Abstract, p. 1 |
| No colapsa con 1k imagenes (cualitativo) | "The training does not collapse with limited 1k images" | §4.5, p. 8 |
| Costo: 200k muestras, una RTX 3090Ti, 5 dias (profundidad) | "use 200k training samples, one single NVIDIA RTX 3090Ti, and 5 days of training" | §4.3, p. 7 |
| Industrial: miles de GPU-horas, >12M imagenes | "thousands of GPU hours, and more than 12M training images" | §4.3, p. 7 |
| Convergencia subita, <10K pasos | "usually in less than 10K optimization steps" | §3.3, p. 5 |

## Donde entra en mi tesis
- **Renderizador (metodo):** manual de implementacion del condicionamiento por mascara de
  implante (y banda B_delta) sobre el LDM 2.5D: zero convolutions, copia entrenable del
  encoder, encoder de condicion E(·) de 4 capas, reemplazo del 50% de prompts por cadena
  vacia, CFG Resolution Weighting.
- **Justificacion de datos limitados (redaccion, con cautela):** las cifras <50k / 1k
  existen, pero la de 1k es una sola figura cualitativa (Fig. 10) en imagen natural y con
  el modelo base preentrenado intacto.
- **Tension con el cambio de VAE (E6b, #36/#39):** el PDF no cubre el escenario de VAE
  distinto al del modelo base; no sirve como respaldo de ControlNet sobre un LDM cuyo VAE
  o U-Net se reentrenen.
- **B_delta / streaking fuera de la mascara:** la arquitectura no confina el efecto a la
  region condicionada (suma sobre el mapa completo), lo que es compatible con generar
  streaking fuera del metal, pero el paper no ofrece ninguna garantia ni metrica de
  preservacion de la anatomia lejos de la condicion.

## Dudas para el asesor
1. Si el VAE de SD 1.5 no sirve para hueso en HU (E6b) y se reemplaza, el U-Net base debe
   reentrenarse sobre el nuevo latente. En ese caso ya no hay "modelo base preentrenado con
   billions of images" que proteger: ¿sigue justificado ControlNet frente a condicionar
   directamente (p. ej. concatenar la mascara) en un LDM entrenado desde CLINIC-metal? El
   PDF no compara esas opciones.
2. ¿Se puede citar "robust with small (<50k)" y "1k images" para 65 pacientes? La evidencia
   de 1k es cualitativa (Fig. 10, un ejemplo) y en dominio natural. *Observacion de la
   extractora:* en 2.5D los cortes de un mismo paciente no son muestras independientes, y el
   paper no discute datos correlacionados.
3. El paper no define "spatially localized" ni mide efecto fuera de la condicion. ¿Hace
   falta una metrica propia de preservacion fuera de B_delta?
4. El material suplementario (parametros de entrenamiento e inferencia, gradiente de las
   zero convolutions, ejemplos extendidos de tamano de datos, detalles de la ablacion) no
   esta en el PDF. ¿Se consigue para la implementacion?
5. Inconsistencias menores del PDF: el abstract dice ">1m" y la Fig. 10 muestra "3m
   images"; la Tabla 1 dice "Average User Ranking (AUR)" y el texto "Average Human Ranking
   (AHR)".
6. `refs.bib` registra la version ICCV 2023; el PDF local es arXiv v3. Para citar paginas o
   frases, ¿se usa esta version o hace falta la de ICCV?

## Evidencia textual

| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Identificador arXiv | "arXiv:2302.05543v3 [cs.CV] 26 Nov 2023" | Margen, p. 1 |
| Afiliacion | "Stanford University" | Cabecera, p. 1 |
| Base congelada | "ControlNet locks the production-ready large diffusion models" | Abstract, p. 1 |
| Reutiliza encoder preentrenado | "reuses their deep and robust encoding layers pretrained with billions of images" | Abstract, p. 1 |
| Definicion de zero convolutions | "(zero-initialized convolution layers) that progressively grow the parameters from zero" | Abstract, p. 1 |
| Proposito de zero convolutions | "ensure that no harmful noise could affect the finetuning" | Abstract, p. 1 |
| Condiciones probadas (abstract) | "edges, depth, segmentation, human pose, etc., with Stable Diffusion" | Abstract, p. 1 |
| Tamanos de datos | "robust with small (<50k) and large (>1m) datasets" | Abstract, p. 1 |
| Prompt por defecto | "a high-quality, detailed, and professional image" | Fig. 1 (leyenda), p. 1 |
| Tamano tipico de datasets de condicion | "are usually about 100K in size, which is 50,000 times smaller" | §1, p. 2 |
| Referencia de escala: LAION-5B | "than the LAION-5B [79] dataset that was used to train Stable Diffusion" | §1, p. 2 |
| Riesgo de fine-tuning directo | "with limited data may cause overfitting and catastrophic forgetting" | §1, p. 2 |
| Necesidad de arquitecturas a medida | "designing deeper or more customized neural architectures might be necessary" | §1, p. 2 |
| Mitigacion del olvido (antecedentes) | "restricting the number or rank of trainable parameters" | §1, p. 2 |
| Pesos iniciales en cero | "with weights initialized to zeros so that they progressively grow during the training" | §1, p. 2 |
| Proteccion del backbone | "protects the large-scale pretrained backbone in the trainable copy from being damaged" | §1, p. 2 |
| Costo: una GPU de consumo (tareas como profundidad) | "on a single NVIDIA RTX 3090Ti GPU can achieve results competitive" | §1, p. 2 |
| Claim de localidad | "can add spatially localized input conditions to a pretrained text-to-image diffusion model" | §1, p. 2 |
| Lista de condiciones (1) | "Canny edges, Hough lines, user scribbles, human key points, segmentation maps" | §1, p. 2 |
| Lista de condiciones (2) | "shape normals, depths, and cartoon line drawings" | §1, p. 2 |
| Fine-tuning directo: riesgos | "can lead to overfitting, mode collapse, and catastrophic forgetting" | §2.1, p. 2 |
| Zero convolution: definicion exacta | "1 × 1 convolution with both weight and bias initialized to zero" | Fig. 2 (leyenda), p. 3 |
| Bloque congelado + copia | "we lock the original block and create a trainable copy" | Fig. 2 (leyenda), p. 3 |
| Mapas 2D | "x and y are usually 2D feature maps, i.e., x ∈ R^{h×w×c}" | §3.1, p. 4 |
| Congelamiento de Θ | "we lock (freeze) the parameters Θ of the original block" | §3.1, p. 4 |
| Clon entrenable | "simultaneously clone the block to a trainable copy with parameters Θc" | §3.1, p. 4 |
| Justificacion del congelamiento | "the locked parameters preserve the production-ready model trained with billions of images" | §3.1, p. 4 |
| Ecuacion del bloque ControlNet | "yc = F(x; Θ) + Z(F(x + Z(c; Θz1); Θc); Θz2)" (Ec. 2) | §3.1, p. 4 |
| Primer paso: salida identica | "both of the Z(·;·) terms in Equation (2) evaluate to zero" (Ec. 3: yc = y) | §3.1, p. 4 |
| Sin ruido dañino al inicio | "harmful noise cannot influence the hidden states of the neural network layers" | §3.1, p. 4 |
| Funcion de zero convolutions | "Zero convolutions protect this backbone by eliminating random noise as gradients" | §3.1, p. 4 |
| Gradiente de zero convolutions | NO ENCONTRADO EN EL PDF ("We detail ... in supplementary materials", §3.1, p. 4) | — |
| Estructura de SD: bloques totales | "the full model contains 25 blocks, including the middle block" | §3.2, p. 4 |
| Bloques de muestreo | "Of the 25 blocks, 8 blocks are down-sampling or up-sampling convolution layers" | §3.2, p. 4 |
| Bloques principales | "main blocks that each contain 4 resnet layers and 2 Vision Transformers" | §3.2, p. 4 |
| Encoder/decoder | "Both the encoder and decoder contain 12 blocks" | §3.2, p. 4 |
| Texto codificado con CLIP | "Text prompts are encoded using the CLIP text encoder" | §3.2, p. 4 |
| Timestep codificado | "diffusion timesteps are encoded with a time encoder using positional encoding" | §3.2, p. 4 |
| Que se copia | "trainable copy of the 12 encoding blocks and 1 middle block of Stable Diffusion" | §3.2, p. 4 |
| Resoluciones del encoder | "12 encoding blocks are in 4 resolutions (64 × 64, 32 × 32, 16 × 16, 8 × 8)" | §3.2, p. 4 |
| Donde se inyecta | "The outputs are added to the 12 skip-connections and 1 middle block of the U-net" | §3.2, p. 4 |
| Version base | "Stable Diffusion V1.5 (or V2.1, as they use the same U-net architecture)" | Fig. 3 (leyenda), p. 4 |
| Bloques bloqueados en la figura | "The locked, gray blocks show the structure of Stable Diffusion V1.5" | Fig. 3 (leyenda), p. 4 |
| Generalidad a otros modelos | "this ControlNet architecture is likely to be applicable with other models" | §3.2, p. 4 |
| Eficiencia: sin gradiente en el encoder congelado | "no gradient computation is required in the originally locked encoder" | §3.2, p. 4 |
| Hardware de la medicion de costo | "As tested on a single NVIDIA A100 PCIE 40GB" | §3.2, p. 4 |
| Sobrecosto de memoria y tiempo | "requires only about 23% more GPU memory and 34% more time" | §3.2, pp. 4-5 |
| Espacio latente como dominio | "Stable Diffusion uses latent images as the training domain" | §3.2, p. 5 |
| Autoencoder de SD | "uses a pre-processing method similar to VQ-GAN [19]" | §3.2, p. 5 |
| Tamano de imagen y latente | "convert 512 × 512 pixel-space images into smaller 64 × 64 latent images" | §3.2, p. 5 |
| Condicion llevada al tamano del latente | "from an input size of 512 × 512 into a 64 × 64 feature space vector" | §3.2, p. 5 |
| Encoder de condicion E(·) | "a tiny network E(·) of four convolution layers with 4 × 4 kernels and 2 × 2 strides" | §3.2, p. 5 |
| Canales e inicializacion de E(·) | "using 16, 32, 64, 128, channels respectively, initialized with Gaussian weights" | §3.2, p. 5 |
| Entrenamiento de E(·) | "trained jointly with the full model" | §3.2, p. 5 |
| Objetivo de entrenamiento | "L = E[ ‖ε − εθ(zt, t, ct, cf)‖²₂ ]" (Ec. 5) | §3.3, p. 5 |
| Mismo objetivo que el fine-tuning | "This learning objective is directly used in finetuning diffusion models with ControlNet" | §3.3, p. 5 |
| Prompts vaciados | "we randomly replace 50% text prompts ct with empty strings" | §3.3, p. 5 |
| Motivo del vaciado | "increases ControlNet's ability to directly recognize semantics in the input conditioning images" | §3.3, p. 5 |
| Convergencia subita | "abruptly succeeds in following the input conditioning image" | §3.3, p. 5 |
| Pasos hasta convergencia | "usually in less than 10K optimization steps" | §3.3, p. 5 |
| Nombre del fenomeno | "we call this the “sudden convergence phenomenon”" | §3.3, p. 5 |
| Paso de convergencia en ejemplo | "(e.g., the 6133 steps marked in bold)" | Fig. 4 (leyenda), p. 5 |
| Calidad durante todo el entrenamiento | "ControlNet always predicts high-quality images during the entire training" | Fig. 4 (leyenda), p. 5 |
| CFG: condicion en ambas ramas | "adding it to both εuc and εc will completely remove CFG guidance" | §3.4, p. 5 |
| CFG: condicion solo en εc | "using only εc will make the guidance very strong" | §3.4, p. 5 |
| CFG Resolution Weighting | "wi = 64/hi, where hi is the size of ith block" | §3.4, p. 6 |
| Tamanos de bloque para CFG-RW | "h1 = 8, h2 = 16, ..., h13 = 64" | §3.4, p. 6 |
| Composicion de multiples ControlNets | "No extra weighting or linear interpolation is necessary for such composition" | §3.4, p. 6 |
| Condiciones evaluadas (1) | "Canny Edge [11], Depth Map [69], Normal Map [87], M-LSD lines [24]" | §4, p. 6 |
| Condiciones evaluadas (2) | "HED soft edge [91], ADE20K segmentation [96], Openpose [12], and user sketches" | §4, p. 6 |
| Parametros de entrenamiento e inferencia | NO ENCONTRADO EN EL PDF ("See also the supplementary material", §4, p. 6) | — |
| Dominio de entrenamiento | "All models are trained with general-domain data." | Fig. 7 (leyenda), p. 6 |
| Sin prompt: reconocimiento semantico | "The model has to recognize semantic contents in the input condition images" | Fig. 7 (leyenda), p. 6 |
| Ablacion (1) | "replacing the zero convolutions with standard convolution layers initialized with Gaussian weights" | §4.2, p. 6 |
| Ablacion (2): ControlNet-lite | "replacing each block's trainable copy with one single convolution layer" | §4.2, p. 6 |
| Cuatro escenarios de prompt | "(1) no prompt; (2) insufficient prompts ... (3) conflicting prompts ... (4) perfect prompts" | §4.2, p. 6 |
| Muestras de la ablacion | "We show a random batch of 6 samples without cherry-picking" | Fig. 8 (leyenda), p. 7 |
| Resolucion de la ablacion | "Images are at 512 × 512" | Fig. 8 (leyenda), p. 7 |
| Fallo de ControlNet-lite | "not strong enough to interpret the conditioning images" | §4.2, p. 7 |
| Escenarios donde falla lite | "fails in the insufficient and no prompt conditions" | §4.2, p. 7 |
| Fallo sin zero convolutions | "performance of ControlNet drops to about the same as ControlNet-lite" | §4.2, p. 7 |
| Interpretacion del fallo | "the pretrained backbone of the trainable copy is destroyed during finetuning" | §4.2, p. 7 |
| Estudio de usuarios: bocetos | "We sample 20 unseen hand-drawn sketches" | §4.3, p. 7 |
| Estudio de usuarios: participantes | "We invited 12 users to rank these 20 groups of 5 results" | §4.3, p. 7 |
| Criterios del estudio | "“the quality of displayed images” and “the fidelity to the sketch”" | §4.3, p. 7 |
| Numero de rankings | "we obtain 100 rankings for result quality and 100 for condition fidelity" | §4.3, p. 7 |
| Escala de ranking (texto) | "users rank each result on a scale of 1 to 5 (lower is worse)" | §4.3, p. 7 |
| Escala de ranking (tabla) | "(1 to 5 indicates worst to best)" | Tabla 1 (leyenda), p. 6 |
| Nombre de la metrica (texto) | "Average Human Ranking (AHR)" | §4.3, p. 7 |
| Nombre de la metrica (tabla) | "Average User Ranking (AUR)" | Tabla 1 (leyenda), p. 6 |
| Escalas de guia de SGD | "default edge-guidance scale (β = 1.6)" ; "high edge-guidance scale (β = 3.2)" | §4.3, p. 7 |
| Tabla 1 PITI (sketch) calidad / fidelidad | "1.10 ± 0.05" / "1.02 ± 0.01" | Tabla 1, p. 6 |
| Tabla 1 Sketch-Guided β=1.6 | "3.21 ± 0.62" / "2.31 ± 0.57" | Tabla 1, p. 6 |
| Tabla 1 Sketch-Guided β=3.2 | "2.52 ± 0.44" / "3.28 ± 0.72" | Tabla 1, p. 6 |
| Tabla 1 ControlNet-lite | "3.93 ± 0.59" / "4.09 ± 0.46" | Tabla 1, p. 6 |
| Tabla 1 ControlNet | "4.22 ± 0.43" / "4.28 ± 0.45" | Tabla 1, p. 6 |
| Costo del modelo industrial SDv2-D2I | "trained with a large-scale NVIDIA A100 cluster, thousands of GPU hours" | §4.3, p. 7 |
| Datos del modelo industrial | "more than 12M training images" | §4.3, p. 7 |
| Costo de ControlNet de profundidad | "use 200k training samples, one single NVIDIA RTX 3090Ti, and 5 days of training" | §4.3, p. 7 |
| Prueba de distincion: entrenamiento de usuarios | "We use 100 images generated by each SDv2-D2I and ControlNet to teach 12 users" | §4.3, p. 7 |
| Prueba de distincion: imagenes | "we generate 200 images and ask the users to tell which model generated" | §4.3, p. 7 |
| Precision de los usuarios | "The average precision of the users is 0.52 ± 0.17" | §4.3, p. 7 |
| Criterio: casi indistinguible | "the two method yields almost indistinguishable results" | §4.3, p. 7 |
| Fidelidad de condicion: segmentador | "OneFormer [35] achieves an Intersection-over-Union (IoU) with 0.58 on the ground-truth set" | §4.3, p. 7 |
| Protocolo de re-segmentacion | "apply OneFormer to detect the segmentations again to compute the reconstructed IoUs" | §4.3, pp. 7-8 |
| Tabla 2 IoU ADE20K (GT; VQGAN; LDM; PITI; lite; ControlNet) | "0.58 ± 0.10; 0.21 ± 0.15; 0.31 ± 0.09; 0.26 ± 0.16; 0.32 ± 0.12; 0.35 ± 0.14" | Tabla 2, p. 7 |
| Conjunto de FID | "over randomly generated 512×512 image sets" | §4.3, p. 8 |
| Metricas de Tabla 3 | "We report FID, CLIP text-image score, and CLIP aesthetic scores" | Tabla 3 (leyenda), p. 7 |
| Tabla 3 Stable Diffusion (FID; CLIP; CLIP-aes) | "6.09; 0.26; 6.32" | Tabla 3, p. 7 |
| Tabla 3 VQGAN (seg.)* | "26.28; 0.17; 5.14" | Tabla 3, p. 7 |
| Tabla 3 LDM (seg.)* | "25.35; 0.18; 5.15" | Tabla 3, p. 7 |
| Tabla 3 PITI (seg.) | "19.74; 0.20; 5.77" | Tabla 3, p. 7 |
| Tabla 3 ControlNet-lite | "17.92; 0.26; 6.30" | Tabla 3, p. 7 |
| Tabla 3 ControlNet | "15.27; 0.26; 6.31" | Tabla 3, p. 7 |
| Asterisco de Tabla 3 | "Methods marked with “*” are trained from scratch" | Tabla 3 (leyenda), p. 7 |
| Comparacion cualitativa | "ControlNet can robustly handle diverse conditioning images and achieves sharp and clean results" | §4.4, p. 8 |
| Tamanos de dataset mostrados | "1k images" ; "50k images" ; "3m images" | Fig. 10, p. 8 |
| No colapso con 1k | "The training does not collapse with limited 1k images" | §4.5, p. 8 |
| Resultado con 1k | "allows the model to generate a recognizable lion" | §4.5, p. 8 |
| Escalabilidad | "The learning is scalable when more data is provided" | §4.5, p. 8 |
| Condicion ambigua | "the results look like the model tries to interpret input shapes" | Fig. 11 (leyenda), p. 8 |
| Transferencia a modelos derivados | "ControlNets do not change the network topology of pretrained SD models" | §4.5, p. 8 |
| Aplicacion directa a modelos de la comunidad | "it can be directly applied to various models in the stable diffusion community" | §4.5, p. 8 |
| Sin reentrenar al transferir | "Transfer pretrained ControlNets to community models [16, 61] without training the neural networks again" | Fig. 12 (leyenda), p. 8 |
| Modelos de la transferencia | "SD 1.5" ; "Comic Diffusion" ; "Protogen 3.4" | Fig. 12, p. 8 |
| Conclusion: aplicabilidad | "likely to be applicable to a wider range of conditions" | §5, pp. 8-9 |
| DOI | NO ENCONTRADO EN EL PDF | — |
| Venue ICCV 2023 (cabecera, paginas de actas) | NO ENCONTRADO EN EL PDF (el PDF es arXiv v3) | — |
| URL de codigo o pesos | NO ENCONTRADO EN EL PDF | — |
| Material suplementario (anexos) | NO ENCONTRADO EN EL PDF | — |
| Hiperparametros: learning rate, batch size, optimizador, numero de pasos por condicion | NO ENCONTRADO EN EL PDF | — |
| Tamano del dataset de entrenamiento por cada condicion | NO ENCONTRADO EN EL PDF (solo 200k para profundidad, §4.3) | — |
| GPU-horas de ControlNet expresadas como GPU-horas | NO ENCONTRADO EN EL PDF (solo "5 days" en una RTX 3090Ti, §4.3) | — |
| Evaluacion cuantitativa del efecto del tamano de datos | NO ENCONTRADO EN EL PDF (Fig. 10 es solo cualitativa) | — |
| Tamano minimo de datos en que el metodo falla | NO ENCONTRADO EN EL PDF | — |
| Declaracion explicita de que el VAE/autoencoder queda congelado | NO ENCONTRADO EN EL PDF (se congela "Stable Diffusion"; el VAE no aparece en Fig. 3) | — |
| Efecto de cambiar o reentrenar el VAE; necesidad de reentrenar el U-Net base | NO ENCONTRADO EN EL PDF | — |
| Uso de ControlNet sobre un modelo base entrenado desde cero o en pocos datos | NO ENCONTRADO EN EL PDF | — |
| Definicion operativa de "spatially localized" o mecanismo que confine el efecto a una region | NO ENCONTRADO EN EL PDF | — |
| Metrica de preservacion de la imagen fuera de la region condicionada | NO ENCONTRADO EN EL PDF | — |
| Mascaras binarias de un objeto (no mapas semanticos de escena) como condicion | NO ENCONTRADO EN EL PDF (solo segmentacion ADE20K) | — |
| Seccion de limitaciones o casos de fallo del metodo completo | NO ENCONTRADO EN EL PDF (solo fallos en ablaciones y CFG, §3.4 y §4.2) | — |
| Imagen medica, CT, entrada monocanal o unidades fisicas (HU) | NO ENCONTRADO EN EL PDF | — |
| Datos 3D o 2.5D / cortes correlacionados | NO ENCONTRADO EN EL PDF | — |
| Resoluciones distintas de 512 x 512 | NO ENCONTRADO EN EL PDF | — |
