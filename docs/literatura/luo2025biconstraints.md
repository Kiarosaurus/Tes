# luo2025biconstraints — Bi-Constraints Diffusion (BCDMAR) para MAR con guia de degradacion

- **DOI / URL:** 10.1109/TMI.2024.3442950 (p. 3552, "Digital Object Identifier 10.1109/TMI.2024.3442950")
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/luo2025biconstraints.pdf

## Que hace (3 lineas maximo)
Propone BCDMAR: difusion score-based (VP-SDE) condicionada por una imagen pre-corregida (adaptive LI, concatenada) para MAR en CT 2D.
En cada paso de muestreo aplica un termino de fidelidad con un operador de degradacion (MAD) que simula el artefacto sobre la estimacion limpia a partir de la mascara de metal.
Evalua en DeepLesion simulado (MSE/PSNR/SSIM) y cualitativamente en clinico (DeepLesion, SpineWeb).

## Restriccion o supuesto clave
- La "degradation guidance" NO es un canal de condicion de la red: es un termino de fidelidad de datos aplicado como gradiente en el muestreo, `||D(x̂0|t, M) - x_ma||²` (Eq. 18-20, Alg. 2, p. 3556). La red solo recibe `x_t`, el prior `c` (imagen pre-corregida) y `t` (Fig. 1, p. 3555).
- El operador MAD `D(x, M)` se calcula desde la imagen limpia y la mascara de metal: segmentacion agua/hueso por umbrales T1/T2 (Eq. 7), atenuacion polienergetica por material (Eq. 8-9), insercion de metal (ej. titanio) en la mascara, proyeccion polienergetica (Eq. 10) y FBP (Eq. 11) (pp. 3554-3555). Es decir, el artefacto se genera fisicamente via sinograma, no desde un mapa analitico en imagen.
- Los autores reconocen la brecha simulado-real: "we employ a linear degradation operator to simplify the process" y "there is a gap between the simulation and real clinical scenarios" (Sec. IV, p. 3562).
- Mascaras de entrenamiento simplificadas a formas geometricas: "simplify these segmented masks into stochastic geometric masks (e.g. circles and triangles)" (Sec. II-C, p. 3556). No hay modelado de tornillos/placas con geometria real.
- Trabajo 2D en 256x256 (Sec. III-A.1, p. 3557); no hay variante 2.5D ni 3D.
- Valores de T1, T2, E0 y del espectro I(E): NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna seleccionada aun (nivel 3, solo contexto) | — | — |

## Donde entra en mi tesis
- Trabajo relacionado del renderizador: ejemplo de difusion condicionada en MAR (tarea inversa) que usa un modelo fisico de degradacion (mascara -> sinograma polienergetico -> FBP) como restriccion durante el muestreo, no como canal de entrada.
- Relevante para la discusion del canal de condicion analitico del artefacto: BCDMAR muestra una alternativa (guia por fidelidad de datos con forward model) frente a concatenar un mapa de artefacto como condicion. Su ablacion (Tabla II) solo compara MEP vs MAD y presencia/ausencia de prior; no evalua un canal de artefacto como condicion de la red.
- Las ventanas de visualizacion reportadas ([-375, 560] HU, [-1000, 1000/1200/1400] HU) no definen codificacion multi-ventana de entrada; NO ENCONTRADO EN EL PDF cualquier normalizacion HU de la entrada.

## Dudas para el asesor
1. El operador MAD (simulacion polienergetica tipo CNNMAR) podria servir como generador del canal analitico de artefacto desde la mascara, o eso equivale a reintroducir la simulacion fisica (XCIST/CatSim) declarada fuera de alcance como brazo?
2. Conviene tratar la guia de degradacion como restriccion en muestreo (estilo DPS, sin reentrenar) en vez de canal de entrada ControlNet? El paper no compara ambas opciones.
3. La Tabla I etiqueta BCDMAR como "self-supervised" pese a entrenar con pares simulados (Alg. 1 usa x0 y c); citar con cuidado esa etiqueta.
4. No hay metricas cuantitativas en datos clinicos (solo Figs. 5-6), y las cifras de la Tabla I son de mascaras geometricas en DeepLesion, no de tornillos pelvicos.

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Revista/volumen | "IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 44, NO. 9, SEPTEMBER 2025" | Encabezado, p. 3552 |
| Fechas | "Received 24 May 2024; revised 29 July 2024; accepted 3 August 2024." | p. 3552 |
| Definicion MAD | "transforms a metal-free image x to a degraded image ... with the metal mask M" | Sec. II-A, p. 3554 |
| Inspiracion MAD | "metal artifact degradation operator D(·, M) inspired by CNNMAR [3]" | Sec. II-A, p. 3554 |
| Problema con MAD (Eq. 6) | "MAD imposes constraints on the measurement image, which includes the metal-affected region." | Sec. II-A, p. 3554 |
| Motivacion vs MEP | "the removed metal trace also contains valuable information about tissues surrounding metal implants" | Sec. I-A, p. 3554 |
| Segmentacion de tejidos (umbral) | "if x_i falls below a certain threshold T1 is regarded as water equivalent" | Sec. II-A, Eq. 7, p. 3554 |
| Umbral hueso | "x_i exceeds another threshold T2 is considered as bone equivalent" | Sec. II-A, p. 3554 |
| Valores T1, T2 | NO ENCONTRADO EN EL PDF | — |
| Material metalico | "specify the metal material commonly used in clinical settings (e.g. titanium)" | Sec. II-A, p. 3554 |
| Energia E0 / espectro I(E) | NO ENCONTRADO EN EL PDF (valores numericos) | — |
| Efectos fisicos incluidos | "nonlinear partial volume effect and scatter are also taken into consideration" | Sec. II-A, p. 3555 |
| Reconstruccion degradada | "the degraded image ... could be reconstructed with y_ma by filter back projection (FBP)" | Sec. II-A, Eq. 11, p. 3555 |
| Paso de muestreo bi-restriccion | "the solution x is constrained by the combination of both conditional prior and degradation posterior" | Sec. II-C, p. 3556 |
| Aproximacion posterior | "p(x_ma|x_t) ≃ p(x_ma|x̂0|t)" | Sec. II-B, Eq. 17-18, p. 3556 |
| Prior condicional c | "c is obtained by partially refining the corresponding metal-affected image x_ma" | Sec. II-C, p. 3556 |
| Opciones de c | "linear interpolation (LI) ... MA and LI (MA&LI) ... adaptive LI" | Sec. II-C, p. 3556 |
| Mascaras simplificadas | "simplify these segmented masks into stochastic geometric masks (e.g. circles and triangles)" | Sec. II-C, p. 3556 |
| Arquitectura | "uses an improved UNet [28] as its backbone" | Sec. II-C, p. 3556 |
| Embedding temporal | "TimeEmb is inserted in every ResBlocks in the network" | Fig. 1, p. 3555 |
| Condicion por concatenacion | Fig. 1 muestra c concatenado (simbolo "Concat") con x_t | Fig. 1, p. 3555 |
| Sin mascaras manuales en entrenamiento | "our model does not rely on manually labeled metal masks during the training" | Sec. I, p. 3553 |
| Dataset simulado | "utilizing 16,360 metal-free images from 88 patients for our training set" | Sec. III-A.1, p. 3557 |
| Resolucion | "CT images were resized into 256 × 256 in all experiments" | Sec. III-A.1, p. 3557 |
| Geometria proyeccion | "fanbeam geometry was applied, where 512 rays were used and 512 angles" | Sec. III-A.1, p. 3557 |
| Rango angular | "evenly spaced from 0° to 360°" | Sec. III-A.1, p. 3557 |
| Fuente rayos X | "A 120 kVP x-ray source was used" | Sec. III-A.1, p. 3557 |
| Ruido Poisson | "the photon number was set to 2 × 10^7 for Poisson noise simulation" | Sec. III-A.1, p. 3557 |
| Test set | "we used 200 metal-free images from 72 patients" | Sec. III-A.1, p. 3557 |
| Mascaras test | "randomly assigned with one of 10 manually segmented metal masks" | Sec. III-A.1, p. 3557 |
| Tamano implantes test | "The sizes of the metal implants range from 32 to 2054 pixels" | Sec. III-A.1, p. 3557 |
| DeepLesion | "annotated with over 32,000 lesions" | Sec. III-A.1, p. 3557 |
| SpineWeb | "The SpineWeb dataset consists of 21,239 images" | Sec. III-A.1, p. 3557 |
| Mascara clinica (umbral HU) | "Regions exceeding 2500 HU values were identified as the metal regions." | Sec. III-A.1, p. 3557 |
| Optimizador | "The parameter of the Adam optimizer is (0.9, 0.999)" | Sec. III-A.2, p. 3557 |
| Learning rate | "initial learning rate is set as 1 × 10^−4" | Sec. III-A.2, p. 3557 |
| Entrenamiento | "16k simulation samples over 40 epochs, using a single Nvidia 4090 GPU" | Sec. III-A.2, p. 3557 |
| Tiempo entrenamiento | "for a total of 48 hours" | Sec. III-A.2, p. 3557 |
| Pasos de difusion | "The time step T is set to 1000" | Sec. III-A.2, p. 3557 |
| Noise schedule | "β_t linearly increases from 0.0001 to 0.02" | Sec. III-A.2, p. 3557 |
| λ por defecto | "We set λ = 0.5 to balance the data consistency and the realism" | Sec. III-A.2, p. 3557 |
| Metricas | "mean square error (MSE), peak signal-to-noise ratio (PSNR), and ... SSIM" | Sec. III-A.3, p. 3557 |
| Definicion SSIM | "SSIM, a perceptual metric, estimates the structural information" | Sec. III-A.3, p. 3558 |
| PSNR MA | "The average PSNR of metal-affected images is 15.7." | Sec. III-B.1, p. 3558 |
| Tabla I MA | MSE 3.13e-2, PSNR 15.70, SSIM 0.6696 | Tabla I, p. 3557 |
| Tabla I LI | MSE 2.12e-3, PSNR 28.09, SSIM 0.8197 | Tabla I, p. 3557 |
| Tabla I Score-IP | 0.5 dias; MSE 7.82e-4, PSNR 31.89, SSIM 0.8134 | Tabla I, p. 3557 |
| Tabla I ADN | 0.2 dias; MSE 4.86e-4, PSNR 34.30, SSIM 0.9312 | Tabla I, p. 3557 |
| Tabla I CNNMAR | 1.5 dias; MSE 7.71e-4, PSNR 35.85, SSIM 0.9412 | Tabla I, p. 3557 |
| Tabla I DANNet | 6 dias; MSE 6.14e-4, PSNR 37.30, SSIM 0.9678 | Tabla I, p. 3557 |
| Tabla I DuDoNet | 2 dias; MSE 9.04e-4, PSNR 37.78, SSIM 0.9696 | Tabla I, p. 3557 |
| Tabla I ACDNet | 2.7 dias; MSE 8.25e-4, PSNR 39.18, SSIM 0.9757 (mejor SSIM) | Tabla I, p. 3557 |
| Tabla I BCDMAR | "self-supervised"; 2 dias; MSE 2.59e-4, PSNR 40.62, SSIM 0.9755 | Tabla I, p. 3557 |
| Clinico: sin metricas cuantitativas | NO ENCONTRADO EN EL PDF (solo comparacion visual, Figs. 5-6) | Sec. III-C, pp. 3558-3560 |
| Pipeline clinico | "A simple threshold is used to segment the metal masks." | Sec. III-C, p. 3558 |
| Prior clinico | "pre-corrected image is generated by interpolating the metal-affected sinogram" | Sec. III-C, p. 3558 |
| Ventana display sim./clinico | "The display window is [−375, 560] HU." | Figs. 2-6, pp. 3557-3559 |
| Ablacion: baseline | "score-based diffusion model with the MEP data-fidelity term as the baseline" | Sec. III-D.1, p. 3560 |
| Tabla II Baseline (MEP) | MSE 4.76e-4, PSNR 32.33, SSIM 0.8275 | Tabla II, p. 3560 |
| Tabla II Model A (MAD) | MSE 4.20e-4, PSNR 34.82, SSIM 0.8528 | Tabla II, p. 3560 |
| Tabla II Model B (solo adaptive LI) | MSE 1.03e-2, PSNR 21.12, SSIM 0.604 | Tabla II, p. 3560 |
| Tabla II Model C (MAD + adaptive LI) | MSE 2.59e-4, PSNR 40.62, SSIM 0.9755 | Tabla II, p. 3560 |
| Model B sin restriccion | "it is affected by noise due to the lack of the degradation posterior constraint" | Sec. III-D.1, p. 3561 |
| Consistencia (repeticiones) | "outcomes of three repeated experiments under different constraint conditions" | Sec. III-D.2, p. 3561 |
| Incertidumbre Model A | "variation of the results ... particularly in the dark bands" | Sec. III-D.2, p. 3561 |
| Tabla III w/o prior | MSE 4.20e-4, PSNR 34.82, SSIM 0.8528 | Tabla III, p. 3561 |
| Tabla III MA | MSE 9.24e-4, PSNR 30.91, SSIM 0.6817 | Tabla III, p. 3561 |
| Tabla III MA&LI | MSE 3.01e-4, PSNR 39.36, SSIM 0.9645 | Tabla III, p. 3561 |
| Tabla III LI | MSE 1.68e-4, PSNR 40.02, SSIM 0.9737 | Tabla III, p. 3561 |
| Tabla III adaptive LI | MSE 2.59e-4, PSNR 40.62, SSIM 0.9755 | Tabla III, p. 3561 |
| Adaptive LI definicion | "the weighted sum of the MA image and the LI image" | Sec. III-D.3, p. 3561 |
| Prior MA produce rayas | "it introduces severe stripe artifacts" | Sec. III-D.3, p. 3561 |
| Tabla IV λ=2.0 | MSE 3.35e-4, PSNR 35.97, SSIM 0.8443 | Tabla IV, p. 3561 |
| Tabla IV λ=1.0 | MSE "1.66e4" (asi impreso), PSNR 39.05, SSIM 0.9242 | Tabla IV, p. 3561 |
| Tabla IV λ=0.5 | MSE 2.59e-4, PSNR 40.62, SSIM 0.9755 | Tabla IV, p. 3561 |
| Tabla IV λ=0.25 | MSE 2.15e-3, PSNR 29.76, SSIM 0.8981 | Tabla IV, p. 3561 |
| λ=2.0 efecto | "When λ = 2.0, the outcome presents severe stripe artifacts." | Sec. III-D.4, p. 3561 |
| λ=1.0 mejora | "the PSNR of the results reaches 39.05 (increased by 3.08)" | Sec. III-D.4, p. 3562 |
| λ=0.25 efecto | "leads to significant disruption in the prior distribution" | Sec. III-D.4, p. 3562 |
| Ventana ablacion | "The display window is[−1000, 1400] HU." | Fig. 7, p. 3560 |
| Limitacion (operador lineal) | "we employ a linear degradation operator to simplify the process" | Sec. IV, p. 3562 |
| Limitacion (brecha sim-real) | "there is a gap between the simulation and real clinical scenarios" | Sec. IV, p. 3562 |
| Trabajo futuro | "study a learnable metal artifact simulation method as a more realistic degradation operator" | Sec. IV, p. 3562 |
| Codigo disponible | NO ENCONTRADO EN EL PDF | — |
| Evaluacion 3D / 2.5D | NO ENCONTRADO EN EL PDF | — |
| Metricas restringidas a ROI peri-metal | NO ENCONTRADO EN EL PDF | — |
| Test estadistico de significancia | NO ENCONTRADO EN EL PDF | — |
