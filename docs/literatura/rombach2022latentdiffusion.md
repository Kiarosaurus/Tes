# rombach2022latentdiffusion — High-Resolution Image Synthesis with Latent Diffusion Models

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. Identificador en el margen de la p. 1:
  "arXiv:2112.10752v2 [cs.CV] 13 Apr 2022". Codigo: https://github.com/CompVis/latent-diffusion
  (bajo los autores, p. 1). Venue (CVPR 2022): NO ENCONTRADO EN EL PDF (el PDF es la
  version arXiv v2 y no menciona CVPR).
- **Nivel de lectura:** 2 (metodo) — PDF completo, 45 paginas, incluidos apendices A-H
- **Leido a fondo por la autora:** no
- **PDF:** papers/rombach2022latentdiffusion.pdf

## Que hace (3 lineas maximo)

Separa la sintesis en dos etapas: un autoencoder (perceptual + adversarial, regularizado con KL leve o VQ) que comprime la imagen RGB por un factor f, y un modelo de difusion (UNet) entrenado en ese latente.
Barre f en {1, 2, 4, 8, 16, 32} y concluye que f = 4-16 equilibra eficiencia y fidelidad perceptual; f = 4 y 8 dan los mejores resultados.
Condiciona por concatenacion (entradas espacialmente alineadas: super-resolucion, inpainting, mapas semanticos) o por cross-attention (texto, clases, layouts).

## Restriccion o supuesto clave

Cuatro supuestos, explicitos o implicitos, que chocan con CT pelvica con implantes metalicos.

1. **La compresion se define como perceptual, en imagen natural RGB.** La primera etapa
   "removes high-frequency details but still learns little semantic variation" (§1, p. 2) y
   el latente es un espacio "in which high-frequency, imperceptible details are abstracted
   away" (§3.2, p. 4). "Imperceptible" se juzga para fotos naturales ("Most bits of a digital
   image correspond to imperceptible details", Fig. 2, p. 2). El streaking de baja amplitud
   que la banda B_delta debe expresar es justamente alta frecuencia estructurada: nada en
   el paper garantiza que se conserve.
2. **Los propios autores declaran el limite de precision en pixel.** "the use of LDMs can
   be questionable when high precision is required" y la capacidad de reconstruccion "can
   become a bottleneck for tasks that require fine-grained accuracy in pixel space" (§5,
   p. 9). Un criterio en HU (MAE < 25 HU en hueso) es exactamente ese tipo de tarea.
3. **Perdidas elegidas contra la fidelidad de intensidad por pixel.** El autoencoder se
   entrena con "a perceptual loss [106] and a patch-based [33] adversarial objective" para
   evitar la "bluriness introduced by relying solely on pixel-space losses such as L2 or L1"
   (§3.1, p. 3). Los autores tambien dicen que PSNR/SSIM "favor blurriness over imperfectly
   aligned high frequency details" (§4.4, p. 8). No hay ninguna metrica de error absoluto de
   intensidad ni de sesgo de valor.
4. **Entrada RGB de 3 canales, rango de normalizacion no declarado, solo dominio natural.**
   "given an image x ∈ R^{H×W×3} in RGB space" (§3.1, p. 3). El rango de entrada ([-1, 1] u
   otro), la profundidad de bits y cualquier dominio fuera de imagen natural (medico, CT, HU,
   rango dinamico alto): NO ENCONTRADO EN EL PDF. Todos los autoencoders de la Tabla 8 estan
   "trained on OpenImages, evaluated on ImageNet-Val" (Tabla 8, p. 21).

## Que toco de aqui

- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Factores f probados: 1, 2, 4, 8, 16, 32 | "different downsampling factors f ∈ {1, 2, 4, 8, 16, 32}" | §4.1, p. 5 |
| f = 4-16 equilibran; f = 4 y 8 mejores | "LDM-{4-16} strike a good balance between efficiency and perceptually faithful results" | §4.1, p. 5 |
| Limite de precision en pixel | "reconstruction capability can become a bottleneck for tasks that require fine-grained accuracy in pixel space" | §5, p. 9 |
| Peso KL ~10^-6 | "weight the KL term by a factor ∼ 10^−6" | Apendice G, p. 29 |
| KL f=4, c=3: R-FID 0.27, PSNR 27.53 ± 4.54, SSIM 0.82 ± 0.11 | Tabla 8, fila "4 KL 3" | Tabla 8, p. 21 |
| KL f=8, c=4: R-FID 0.90, PSNR 24.19 ± 4.19, SSIM 0.69 ± 0.15 | Tabla 8, fila "8 KL 4" | Tabla 8, p. 21 |
| KL f=2, c=2: R-FID 0.086, PSNR 32.47 ± 4.19, SSIM 0.93 ± 0.04 | Tabla 8, fila "2 KL 2" | Tabla 8, p. 21 |
| Concatenacion para condicion espacialmente alineada | "By concatenating spatially aligned conditioning information to the input of εθ" | §4.3.2, p. 7 |

## Donde entra en mi tesis

- **Objetivo 1 (Go/No-Go, HU -> multi-ventana -> VAE -> HU, MAE < 25 HU en hueso).** Cita
  primaria para justificar por que el Go/No-Go es necesario: los autores del LDM declaran que
  la reconstruccion del autoencoder puede ser cuello de botella cuando se exige precision en
  pixel (§5, p. 9), y su autoencoder se optimiza con perdidas perceptual/adversarial, no de
  intensidad (§3.1, p. 3). Coherente con E6b (VAE de SD 1.5 congelado falla 178/178), aunque
  el paper no evalua CT ni HU.
- **#36 / #39, opcion 3 (otro VAE con menor compresion).** La Tabla 8 (p. 21) muestra que, en
  imagen natural, bajar f sube PSNR/SSIM (KL: f=8 c=4 24.19 dB; f=4 c=3 27.53 dB; f=2 c=2
  32.47 dB) y que subir canales latentes a f fijo tambien ayuda (f=16: c=8 21.94 dB, c=16
  24.08 dB; f=32: c=16 20.38 dB, c=64 22.27 dB). Contrapeso del mismo paper: f pequeno
  entrena lento ("small downsampling factors for LDM-{1,2} result in slow training
  progress", §4.1, p. 5). Ninguna cifra es en HU: sirven para argumentar direccion, no para
  predecir si se cumple 25 HU.
- **Implicancia #66 (streaks de alta frecuencia en B_delta).** Respaldo textual directo del
  riesgo: la compresion "removes high-frequency details" (§1, p. 2) y PSNR/SSIM no capturan
  bien alta frecuencia (§4.4, p. 8). Un MAE en hueso tampoco lo haria.
- **Objetivo 3 (renderizador).** Manual de implementacion: Ec. 2-3 (p. 4-5), cross-attention
  (§3.3, p. 4), concatenacion para condiciones alineadas (§4.3.2, p. 7; Tabla 15, p. 25) y
  reescalado del latente KL por su desviacion estandar (§4.3.2, p. 7; Apendice D.1, p. 20;
  Apendice G, p. 29). ControlNet no aparece en este paper.

## Dudas para el asesor

1. `main.tex` dice "Stable Diffusion 1.5 backbone". Este PDF no menciona Stable Diffusion
   (NO ENCONTRADO EN EL PDF). La configuracion f=8, c=4, KL coincide con una fila de la Tabla 8
   y con el z-shape "32 × 32 × 4" del modelo texto-imagen (Tabla 15, p. 25), pero que el VAE
   de SD 1.5 sea esa fila no se puede verificar desde aqui. Hace falta otra fuente para citar
   el VAE de SD 1.5?
2. La Tabla 8 no declara el rango de datos del PSNR, ni que significa el "±", ni que es la
   columna PSIM. Basta usarla para argumentar la direccion del trade-off (menor f, mejor
   reconstruccion) sin trasladar magnitudes a HU?
3. Observacion de la extractora (aritmetica sobre valores del PDF, no afirmada por el paper):
   en la Tabla 8, pasar de KL f=8 c=4 a KL f=4 c=3 sube el PSNR 3.34 dB (24.19 -> 27.53) con
   menos canales latentes. Tambien la cifra de Fig. 1 "ours (f = 4) PSNR: 27.4 R-FID: 0.58"
   coincide con la fila VQ f=4 |Z|=8192 (27.43, 0.58), no con la KL. Conviene citar la tabla
   y no la figura.
4. El rango de entrada ([-1, 1]) no esta en el PDF. Si el pipeline o la tesis lo atribuyen a
   este paper, la fuente tendria que ser el codigo del repositorio, no el articulo.
5. Para mascaras espacialmente alineadas el paper usa concatenacion (Tabla 15: super
   resolucion, inpainting y mapas semanticos con "concat"). Vale la pena mencionar la
   concatenacion como alternativa mas simple a ControlNet en la justificacion del Objetivo 3?
   Como se construye exactamente la entrada de inpainting (mascara + imagen enmascarada): NO
   ENCONTRADO EN EL PDF.

## Evidencia textual

| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Identificador arXiv | "arXiv:2112.10752v2 [cs.CV] 13 Apr 2022" | Margen, p. 1 |
| Codigo | "https://github.com/CompVis/latent-diffusion" | Cabecera, p. 1 |
| Idea central | "we apply them in the latent space of powerful pretrained autoencoders" | Abstract, p. 1 |
| Claim de equilibrio | "a near-optimal point between complexity reduction and detail preservation" | Abstract, p. 1 |
| Fig. 1: f=4 propio | "ours (f = 4) PSNR: 27.4 R-FID: 0.58" | Fig. 1, p. 1 |
| Fig. 1: DALL-E f=8 | "DALL-E (f = 8) PSNR: 22.8 R-FID: 32.01" | Fig. 1, p. 1 |
| Fig. 1: VQGAN f=16 | "VQGAN (f = 16) PSNR: 19.9 R-FID: 4.98" | Fig. 1, p. 1 |
| Fig. 1: menos submuestreo = mas calidad | "Boosting the upper bound on achievable quality with less agressive downsampling" | Fig. 1, p. 1 |
| Fig. 1: datos de la figura | "Images are from the DIV2K [1] validation set, evaluated at 512² px" | Fig. 1, p. 1 |
| Fig. 1: donde se calculan las metricas | "Reconstruction FIDs [29] and PSNR are calculated on ImageNet-val" | Fig. 1, p. 1 |
| Costo de DMs en pixel | "often takes hundreds of GPU days (e.g. 150 - 1000 V100 days" | §1, p. 1 |
| Costo de muestreo en pixel | "producing 50k samples takes approximately 5 days [15] on a single A100 GPU" | §1, p. 2 |
| Pasos de muestreo en pixel | "a large number of steps (e.g. 25 - 1000 steps in [15])" | §1, p. 2 |
| **La compresion perceptual quita alta frecuencia** | "a perceptual compression stage which removes high-frequency details" | §1, p. 2 |
| Definicion de compresion semantica | "the actual generative model learns the semantic and conceptual composition of the data" | §1, p. 2 |
| Bits imperceptibles | "Most bits of a digital image correspond to imperceptible details" | Fig. 2, p. 2 |
| Compresion leve propuesta | "a separate mild compression stage that only eliminates imperceptible details" | Fig. 2, p. 2 |
| Sin compresion espacial excesiva | "we do not need to rely on excessive spatial compression" | §1, p. 2 |
| Autoencoder reutilizable | "we need to train the universal autoencoding stage only once" | §1, p. 2 |
| Claim de reconstruccion fiel | "This ensures extremely faithful reconstructions and requires very little regularization of the latent space" | §1 (iii), p. 2 |
| Resolucion convolucional | "render large, consistent images of ∼ 1024² px" | §1 (iv), p. 2 |
| Trade-off de compresion en trabajos previos | "less compression comes at the price of high computational cost" | §2, p. 3 |
| **Perdidas del autoencoder** | "an autoencoder trained by combination of a perceptual loss [106] and a patch-based [33] adversarial objective" | §3.1, p. 3 |
| Motivo de las perdidas | "avoids bluriness introduced by relying solely on pixel-space losses such as L2 or L1" | §3.1, p. 3 |
| **Entrada RGB, 3 canales** | "given an image x ∈ R^{H×W×3} in RGB space" | §3.1, p. 3 |
| Forma del latente | "z ∈ R^{h×w×c}" | §3.1, p. 4 |
| Definicion de f | "the encoder downsamples the image by a factor f = H/h = W/w" | §3.1, p. 4 |
| f potencia de 2 | "different downsampling factors f = 2^m, with m ∈ N" | §3.1, p. 4 |
| Motivo de regularizar | "In order to avoid arbitrarily high-variance latent spaces" | §3.1, p. 4 |
| **Definicion KL-reg** | "imposes a slight KL-penalty towards a standard normal on the learned latent" | §3.1, p. 4 |
| **Definicion VQ-reg** | "uses a vector quantization layer [96] within the decoder" | §3.1, p. 4 |
| Compresion leve basta | "we can use relatively mild compression rates and achieve very good reconstructions" | §3.1, p. 4 |
| Claim de preservacion de detalle | "our compression model preserves details of x better (see Tab. 8)" | §3.1, p. 4 |
| Objetivo DM | "L_DM = E_{x,ε∼N(0,1),t}[‖ε − εθ(x_t, t)‖²₂]" (Ec. 1) | §3.2, p. 4 |
| t uniforme | "with t uniformly sampled from {1, . . . , T}" | §3.2, p. 4 |
| **Latente sin alta frecuencia** | "latent space in which high-frequency, imperceptible details are abstracted away" | §3.2, p. 4 |
| Objetivo LDM | "L_LDM := E_{E(x),ε∼N(0,1),t}[‖ε − εθ(z_t, t)‖²₂]" (Ec. 2) | §3.2, p. 4 |
| Decodificacion en un paso | "decoded to image space with a single pass through D" | §3.2, p. 4 |
| **Dos vias de condicionamiento** | "We condition LDMs either via concatenation or by a more general cross-attention mechanism" | Fig. 3, p. 4 |
| Codificador de condicion | "a domain specific encoder τθ that projects y to an intermediate representation" | §3.3, p. 4 |
| Cross-attention | "Q = W_Q · φ_i(z_t), K = W_K · τθ(y), V = W_V · τθ(y)" | §3.3, p. 4 |
| Objetivo LDM condicional | "L_LDM := E[‖ε − εθ(z_t, t, τθ(y))‖²₂]" (Ec. 3) | §3.3, p. 5 |
| **KL frente a VQ en reconstruccion** | "reconstruction capabilities of VQ-regularized first stage models slightly fall behind those of their continuous counterparts" | §4, p. 5 |
| VQ a veces mejor en muestras | "LDMs trained in VQ-regularized latent spaces sometimes achieve better sample quality" | §4, p. 5 |
| Presupuesto fijo del barrido | "we fix the computational resources to a single NVIDIA A100" | §4.1, p. 5 |
| **Factores f del barrido** | "different downsampling factors f ∈ {1, 2, 4, 8, 16, 32}" | §4.1, p. 5 |
| Duracion del barrido | "2M steps of class-conditional models on the ImageNet [12] dataset" | §4.1, p. 5 |
| f pequeno: lento | "small downsampling factors for LDM-{1,2} result in slow training progress" | §4.1, p. 5 |
| f grande: fidelidad estancada | "overly large values of f cause stagnating fidelity after comparably few training steps" | §4.1, p. 5 |
| Causa: perdida de informacion | "too strong first stage compression resulting in information loss" | §4.1, p. 5 |
| **Rango de equilibrio** | "LDM-{4-16} strike a good balance between efficiency and perceptually faithful results" | §4.1, p. 5 |
| Brecha FID LDM-1 vs LDM-8 | "FID [29] gap of 38 between pixel-based diffusion (LDM-1) and LDM-8" | §4.1, p. 5 |
| Datos complejos piden menos compresion | "Complex datasets such as ImageNet require reduced compression rates to avoid reducing quality" | §4.1, p. 5 |
| **Mejores f** | "LDM-4 and -8 offer the best conditions for achieving high-quality synthesis results" | §4.1, p. 5 |
| Exceso de compresion | "Too much perceptual compression as in LDM-32 limits the overall sample quality" | Fig. 6, p. 6 |
| Pasos DDIM de Fig. 7 | "indicate {10, 20, 50, 100, 200} sampling steps using DDIM" | Fig. 7, p. 6 |
| Muestras para FID de Fig. 7 | "FID scores assessed on 5000 samples" | Fig. 7, p. 6 |
| Pasos de entrenamiento Fig. 7 | "trained for 500k (CelebA) / 2M (ImageNet) steps on an A100" | Fig. 7, p. 6 |
| FID CelebA-HQ | "a new state-of-the-art FID of 5.11" | §4.2, p. 5 |
| Tabla 1 CelebA-HQ LDM-4 (FID; Prec; Recall) | "5.11; 0.72; 0.49" | Tabla 1, p. 6 |
| Tabla 1 FFHQ LDM-4 | "4.98; 0.73; 0.50" | Tabla 1, p. 6 |
| Tabla 1 LSUN-Churches LDM-8* | "4.02; 0.64; 0.52" | Tabla 1, p. 6 |
| Tabla 1 LSUN-Bedrooms LDM-4 | "2.95; 0.66; 0.48" | Tabla 1, p. 6 |
| Tabla 2 LDM-KL-8 (FID; IS; params) | "23.31; 20.03±0.33; 1.45B; 250 DDIM steps" | Tabla 2, p. 6 |
| Tabla 2 LDM-KL-8-G | "12.63; 30.29±0.42; 1.45B; 250 DDIM steps, c.f.g. s = 1.5" | Tabla 2, p. 6 |
| Tabla 3 LDM-4 (FID; IS; Prec; Recall; params) | "10.56; 103.49±1.24; 0.71; 0.62; 400M" | Tabla 3, p. 7 |
| Tabla 3 LDM-4-G | "3.60; 247.67±5.59; 0.87; 0.48; 400M" | Tabla 3, p. 7 |
| Modelo texto-imagen | "a 1.45B parameter KL-regularized LDM conditioned on language prompts on LAION-400M" | §4.3.1, p. 7 |
| **Concatenacion para condicion alineada** | "By concatenating spatially aligned conditioning information to the input of εθ" | §4.3.2, p. 7 |
| Mapas semanticos concatenados | "concatenate downsampled versions of the semantic maps with the latent image representation" | §4.3.2, p. 7 |
| Resolucion de entrenamiento | "We train on an input resolution of 256² (crops from 384²)" | §4.3.2, p. 7 |
| **SNR depende de la escala del latente** | "the signal-to-noise ratio (induced by the scale of the latent space) significantly affects the results" | §4.3.2, p. 7 |
| Reescalado del latente | "a rescaled version, scaled by the component-wise standard deviation" | §4.3.2, p. 7 |
| SR por concatenacion | "directly conditioning on low-resolution images via concatenation" | §4.4, p. 7 |
| Autoencoder de SR | "the f = 4 autoencoding model pretrained on OpenImages (VQ-reg." | §4.4, p. 8 |
| Degradacion de SR | "a bicubic interpolation with 4×-downsampling" | §4.4, p. 8 |
| PSNR/SSIM vs percepcion | "these metrics do not align well with human perception" | §4.4, p. 8 |
| **PSNR/SSIM favorecen borroso** | "favor blurriness over imperfectly aligned high frequency details" | §4.4, p. 8 |
| Tabla 5 LDM-4 100 steps (FID; IS; PSNR; SSIM) | "2.8†/4.8‡; 166.3; 24.4±3.8; 0.69±0.14" | Tabla 5, p. 8 |
| Tabla 5 Image Regression | "15.2; 121.1; 27.9; 0.801" | Tabla 5, p. 8 |
| Tabla 5 SR3 | "5.2; 180.1; 26.4; 0.762" | Tabla 5, p. 8 |
| Tabla 4 SR (Pixel-DM vs LDM-4), Task 1 / Task 2 | "16.0% / 30.4%; 29.4% / 70.6%" | Tabla 4, p. 8 |
| Tabla 4 Inpainting (LAMA vs LDM-4), Task 1 / Task 2 | "13.6% / 21.0%; 31.9% / 68.1%" | Tabla 4, p. 8 |
| Aceleracion en inpainting | "a speed-up of at least 2.7× between pixel- and latent-based diffusion models" | §4.5, p. 8 |
| Mejora de FID en inpainting | "while improving FID scores by a factor of 1.6×" | §4.5, p. 8 |
| Tabla 6 LDM-1 (train; sampling@256; @512; h/epoch; FID@2k) | "0.11; 0.26; 0.07; 20.66; 24.74" | Tabla 6, p. 8 |
| Tabla 6 LDM-4 (KL, w/ attn) | "0.32; 0.97; 0.34; 7.66; 15.21" | Tabla 6, p. 8 |
| Tabla 6 LDM-4 (VQ, w/ attn) | "0.33; 0.97; 0.34; 7.04; 14.99" | Tabla 6, p. 8 |
| Tabla 6 LDM-4 (VQ, w/o attn) | "0.35; 0.99; 0.36; 6.66; 15.95" | Tabla 6, p. 8 |
| Tabla 7 LDM-4 big w/ ft (40-50% FID; LPIPS; All FID; LPIPS) | "9.39; 0.246±0.042; 1.50; 0.137±0.080" | Tabla 7, p. 9 |
| Tabla 7 LaMa† | "12.31; 0.243±0.038; 2.23; 0.134±0.080" | Tabla 7, p. 9 |
| Criterio "hard examples" de Tabla 7 | "hard examples where 40-50% of the image region have to be inpainted" | Tabla 7, p. 9 |
| Parametros del modelo grande | "has 387M parameters instead of 215M" | §4.5, p. 8-9 |
| Limitacion: muestreo lento | "their sequential sampling process is still slower than that of GANs" | §5, p. 9 |
| **Limitacion: alta precision** | "the use of LDMs can be questionable when high precision is required" | §5, p. 9 |
| Perdida pequena en f=4 | "the loss of image quality is very small in our f = 4 autoencoding models" | §5, p. 9 |
| **Limitacion: cuello de botella en pixel** | "reconstruction capability can become a bottleneck for tasks that require fine-grained accuracy in pixel space" | §5, p. 9 |
| SR ya limitada por eso | "our superresolution models (Sec. 4.4) are already somewhat limited in this respect" | §5, p. 9 |
| SNR alto en latente KL sin reescalar | "this ratio is very high" | Apendice D.1, p. 20 |
| Varianza del latente VQ | "the VQ-regularized space has a variance close to 1" | Apendice D.1, p. 20 |
| Lista de autoencoders | "various autoencoding models trained on the OpenImages dataset in Tab. 8" | Apendice D.2, p. 20 |
| **Tabla 8: dominio de entrenamiento y evaluacion** | "Complete autoencoder zoo trained on OpenImages, evaluated on ImageNet-Val" | Tabla 8, p. 21 |
| Tabla 8: columnas | "f, \|Z\|, c, R-FID ↓, R-IS ↑, PSNR ↑, PSIM ↓, SSIM ↑" | Tabla 8, p. 21 |
| Tabla 8: significado de † | "† denotes an attention-free autoencoder" | Tabla 8, p. 21 |
| Tabla 8 VQGAN f16 \|Z\|16384 c256 (R-FID; PSNR; PSIM; SSIM) | "4.98; 19.9±3.4; 1.83±0.42; 0.51±0.18" | Tabla 8, p. 21 |
| Tabla 8 VQGAN f16 \|Z\|1024 c256 | "7.94; 19.4±3.3; 1.98±0.43; 0.50±0.18" | Tabla 8, p. 21 |
| Tabla 8 DALL-E f8 \|Z\|8192 | "32.01; 22.8±2.1; 1.95±0.51; 0.73±0.13" | Tabla 8, p. 21 |
| Tabla 8 VQ f32 \|Z\|16384 c16 (R-FID; R-IS; PSNR; PSIM; SSIM) | "31.83; 40.40±1.07; 17.45±2.90; 2.58±0.48; 0.41±0.18" | Tabla 8, p. 21 |
| Tabla 8 VQ f16 \|Z\|16384 c8 | "5.15; 144.55±3.74; 20.83±3.61; 1.73±0.43; 0.54±0.18" | Tabla 8, p. 21 |
| Tabla 8 VQ f8 \|Z\|16384 c4 | "1.14; 201.92±3.97; 23.07±3.99; 1.17±0.36; 0.65±0.16" | Tabla 8, p. 21 |
| Tabla 8 VQ f8 \|Z\|256 c4 | "1.49; 194.20±3.87; 22.35±3.81; 1.26±0.37; 0.62±0.16" | Tabla 8, p. 21 |
| Tabla 8 VQ f4 \|Z\|8192 c3 | "0.58; 224.78±5.35; 27.43±4.26; 0.53±0.21; 0.82±0.10" | Tabla 8, p. 21 |
| Tabla 8 VQ f4† \|Z\|8192 c3 (sin atencion) | "1.06; 221.94±4.58; 25.21±4.17; 0.72±0.26; 0.76±0.12" | Tabla 8, p. 21 |
| Tabla 8 VQ f4 \|Z\|256 c3 | "0.47; 223.81±4.58; 26.43±4.58; 0.62±0.24; 0.80±0.11" | Tabla 8, p. 21 |
| Tabla 8 VQ f2 \|Z\|2048 c2 | "0.16; 232.75±5.09; 30.85±4.12; 0.27±0.12; 0.91±0.05" | Tabla 8, p. 21 |
| Tabla 8 VQ f2 \|Z\|64 c2 | "0.40; 226.62±4.83; 29.13±3.46; 0.38±0.13; 0.90±0.05" | Tabla 8, p. 21 |
| Tabla 8 KL f32 c64 | "2.04; 189.53±3.68; 22.27±3.93; 1.41±0.40; 0.61±0.17" | Tabla 8, p. 21 |
| Tabla 8 KL f32 c16 | "7.3; 132.75±2.71; 20.38±3.56; 1.88±0.45; 0.53±0.18" | Tabla 8, p. 21 |
| Tabla 8 KL f16 c16 | "0.87; 210.31±3.97; 24.08±4.22; 1.07±0.36; 0.68±0.15" | Tabla 8, p. 21 |
| Tabla 8 KL f16 c8 | "2.63; 178.68±4.08; 21.94±3.92; 1.49±0.42; 0.59±0.17" | Tabla 8, p. 21 |
| **Tabla 8 KL f8 c4** | "0.90; 209.90±4.92; 24.19±4.19; 1.02±0.35; 0.69±0.15" | Tabla 8, p. 21 |
| **Tabla 8 KL f4 c3** | "0.27; 227.57±4.89; 27.53±4.54; 0.55±0.24; 0.82±0.11" | Tabla 8, p. 21 |
| **Tabla 8 KL f2 c2** | "0.086; 232.66±5.16; 32.47±4.19; 0.20±0.09; 0.93±0.04" | Tabla 8, p. 21 |
| Tabla 10 LDM-8 (FID; IS; params) | "17.41; 72.92±2.6; 395M; 200 DDIM steps, 2.9M train steps" | Tabla 10, p. 22 |
| Tabla 10 LDM-4-G scale 1.5 | "3.60; 247.67±5.59; 400M" | Tabla 10, p. 22 |
| Fig. 17: presupuesto | "for a fixed number of 35 V100 days" | Fig. 17, p. 22 |
| Tabla 11 LDM-4 100 steps +15 ep. (FID; IS; PSNR; SSIM) | "2.6† / 4.6‡; 169.76±5.03; 24.4±3.8; 0.69±0.14" | Tabla 11, p. 23 |
| Tabla 11 Pixel-DM 100 steps +15 ep. | "5.1† / 7.1‡; 163.06±4.67; 24.1±3.3; 0.59±0.12" | Tabla 11, p. 23 |
| Tabla 12 CelebA-HQ (f; z-shape; \|Z\|) | "4; 64 × 64 × 3; 8192" | Tabla 12, p. 24 |
| Tabla 12 LSUN-Churches (f; params) | "8; 294M" | Tabla 12, p. 24 |
| Tabla 13 z-shapes LDM-1/2/4/8/16/32 | "256×256×3; 128×128×2; 64×64×3; 32×32×4; 16×16×8; 88×8×32" (sic) | Tabla 13, p. 24 |
| Tabla 13 pasos de difusion y schedule | "1000; linear" | Tabla 13, p. 24 |
| Tabla 14 iteraciones CelebA | "All models are trained for 500k iterations" | Tabla 14, p. 25 |
| **Tabla 15 texto-imagen (f; z-shape; condicionamiento)** | "8; 32 × 32 × 4; CA" | Tabla 15, p. 25 |
| **Tabla 15 super-resolucion** | "4; 64 × 64 × 3; concat" | Tabla 15, p. 25 |
| **Tabla 15 inpainting** | "4; 64 × 64 × 3; concat; 215M" | Tabla 15, p. 25 |
| **Tabla 15 mapa semantico** | "8; 32 × 32 × 4; concat" | Tabla 15, p. 25 |
| Hardware de inpainting | "except for the inpainting model which was trained on eight V100" | Tabla 15, p. 25 |
| Class-conditional por cross-attention | "a single learnable embedding layer with a dimensionality of 512" | Apendice E.2.1, p. 26 |
| Tabla 17 texto-imagen (seq-length; depth; dim) | "77; 32; 1280" | Tabla 17, p. 26 |
| Tabla 17 layout-imagen | "92; 16; 512" | Tabla 17, p. 26 |
| Recortes de inpainting | "random crops of size 256 × 256 and evaluate on crops of size 512 × 512" | Apendice E.2.2, p. 26 |
| Muestras para FID/Prec/Recall | "based on 50k samples from our models" | Apendice E.3.1, p. 26 |
| Diferencias de FID por script | "slightly varying scores of 7.76 (torch-fidelity) vs. 7.77" | Apendice E.3.1, p. 27 |
| FID texto-imagen | "comparing generated samples with 30000 samples from the validation set" | Apendice E.3.2, p. 27 |
| FID layout | "the 2048 unaugmented examples of the COCO Segmentation Challenge split" | Apendice E.3.3, p. 27 |
| Filtro de SR | "images with a shorter size less than 256 px are removed" | Apendice E.3.4, p. 27 |
| Muestras de eficiencia | "based on 5k samples" | Apendice E.3.5, p. 27 |
| Protocolo de estudio de usuario | "use the 2-alternative force-choice paradigm to assess human preference scores" | Apendice E.3.6, p. 27 |
| Tiempo de visualizacion | "humans viewed the images for 3 seconds before responding" | Apendice E.3.6, p. 27 |
| Tabla 18 VQGAN-f-4 primera etapa (compute; params; R-FID) | "29; 55M; 0.58††" | Tabla 18, p. 28 |
| Tabla 18 VQGAN-f-8 primera etapa | "66; 68M; 1.14††" | Tabla 18, p. 28 |
| Unidad de compute | "Compute during training in V100-days" | Tabla 18, p. 28 |
| Conversion A100 a V100 | "assuming a ×2.2 speedup of A100 vs V100" | Apendice F, p. 28 |
| **Entrenamiento adversarial del autoencoder** | "We train all our autoencoder models in an adversarial manner following [23]" | Apendice G, p. 29 |
| Discriminador | "a patch-based discriminator Dψ is optimized to differentiate original images from reconstructions" | Apendice G, p. 29 |
| Proposito de L_reg | "regularize the latent z to be zero centered and obtain small variance" | Apendice G, p. 29 |
| KL de bajo peso | "a low-weighted Kullback-Leibler-term" | Apendice G, p. 29 |
| Regularizacion minima | "To obtain high-fidelity reconstructions we only use a very small regularization" | Apendice G, p. 29 |
| **Peso KL** | "weight the KL term by a factor ∼ 10^−6" | Apendice G, p. 29 |
| Alternativa VQ | "or choose a high codebook dimensionality \|Z\|" | Apendice G, p. 29 |
| Objetivo del autoencoder | "L_rec(x, D(E(x))) − L_adv(D(E(x))) + log Dψ(x) + L_reg(x; E, D)" (Ec. 25) | Apendice G, p. 29 |
| Muestreo del latente KL | "z = E_μ(x) + E_σ(x) · ε =: E(x), where ε ∼ N(0, 1)" | Apendice G, p. 29 |
| Estimacion de la varianza | "from the first batch in the data" | Apendice G, p. 29 |
| **Reescalado a desviacion unitaria** | "the rescaled latent has unit standard deviation" | Apendice G, p. 29 |
| Latente VQ | "we extract z before the quantization layer" | Apendice G, p. 29 |
| DOI | NO ENCONTRADO EN EL PDF | — |
| Venue CVPR 2022 | NO ENCONTRADO EN EL PDF (version arXiv v2) | — |
| Rango de normalizacion de la entrada ([-1, 1], [0, 1] u otro) | NO ENCONTRADO EN EL PDF | — |
| Profundidad de bits / rango dinamico de la entrada | NO ENCONTRADO EN EL PDF | — |
| Autoencoders con entrada distinta de 3 canales RGB | NO ENCONTRADO EN EL PDF | — |
| Forma concreta de L_rec (L1, L2) | NO ENCONTRADO EN EL PDF | — |
| Pesos de la perdida perceptual y de la adversarial | NO ENCONTRADO EN EL PDF | — |
| Hiperparametros de entrenamiento del autoencoder (iteraciones, batch, lr, resolucion) | NO ENCONTRADO EN EL PDF (solo compute y parametros de VQGAN-f-4/f-8 en Tabla 18) | — |
| Definicion de la metrica PSIM | NO ENCONTRADO EN EL PDF | — |
| Significado de "±" en Tabla 8 y rango de datos del PSNR | NO ENCONTRADO EN EL PDF | — |
| Error absoluto de intensidad (MAE) o sesgo de valor tras reconstruccion | NO ENCONTRADO EN EL PDF | — |
| Error por banda de frecuencia o analisis espectral de la reconstruccion | NO ENCONTRADO EN EL PDF | — |
| Dominios fuera de imagen natural (medico, CT, HU) | NO ENCONTRADO EN EL PDF | — |
| Datos volumetricos, 2.5D o 3D | NO ENCONTRADO EN EL PDF | — |
| Stable Diffusion / SD 1.5 | NO ENCONTRADO EN EL PDF | — |
| ControlNet | NO ENCONTRADO EN EL PDF | — |
| Construccion exacta de la entrada de inpainting (mascara + imagen enmascarada) | NO ENCONTRADO EN EL PDF | — |
| Peso KL especifico por fila de la Tabla 8 | NO ENCONTRADO EN EL PDF (solo el valor general ∼10^−6) | — |
