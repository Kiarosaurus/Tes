# xia2024pndnet — PND-Net: red dual-dominio no local inspirada en la fisica para MAR

- **DOI / URL:** 10.1109/TMI.2024.3354925 ("Digital Object Identifier 10.1109/TMI.2024.3354925", p. 2125). Codigo: https://github.com/Ballbo5354/PND-Net (Sec. IV-B, p. 2130)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/xia2024pndnet.pdf

## Que hace (3 lineas maximo)
Red MAR no supervisada (no pareada, estilo CycleGAN) con tres subredes entrenadas en conjunto: NSD-Net descompone el artefacto en el sinograma tambien fuera de la traza de metal, IR-Net refina en imagen, y F-Net sintetiza imagenes con metal a partir de imagenes limpias (ruta de sintesis). Justifica la descomposicion no local con simulacion Monte Carlo (gMCDRR) y proyecciones reales. Datos: DeepLesion simulado y CT clinico (1200 con metal / 2000 limpias, 40 pacientes).

## Restriccion o supuesto clave
Es MAR, no sintesis generativa como objetivo, pero tiene una ruta de sintesis de artefactos (Sec. III-D, Ec. 9, p. 2129) relevante para la tesis:

- **Ruta de sintesis (limpia -> con metal).** Si existe: "we add an artifact synthesis path to achieve unpaired learning" (Sec. III-D, p. 2129). Formula: I_cm = G_FNet(P^-1(P(I_c) + a_S), a_I) (Ec. 9, p. 2129). El artefacto de sinograma a_S se suma a la proyeccion de la imagen limpia, se reconstruye por FBP y luego una red aprendida (F-Net) lo fusiona con el artefacto de imagen a_I. Los componentes a_S y a_I NO se calculan desde una mascara: se extraen de imagenes reales con metal por NSD-Net e IR-Net (a_I = I_sc - I_mc, Sec. III-C, p. 2129). La sintesis es, por tanto, aprendida y no fisica.
- **Fisica que usa.**
  - Endurecimiento (beam hardening) derivado analiticamente de la proyeccion de la mascara: a_BH = -ln{ integral eta(E) exp(-mu_metal(E) P(M)) dE } (Ec. 3, p. 2127), con P(M) = integral de M sobre L y traza M_t = delta(P(M)). Es decir, el termino BH depende solo de la mascara M y del espectro, igual que el canal T de la tesis. Sin embargo esta formula NO se usa para generar artefactos en la ruta de sintesis; se usa para argumentar que BH queda confinado a la traza: "Beam hardening artifacts are located only in the nonzero region" (Sec. II, p. 2127).
  - Modelo del artefacto en sinograma: S_a = a_BH + a_scatter + a_NPVE + a_noise (Ec. 4, p. 2128). Dispersion (scatter), efecto de volumen parcial no lineal (NPVE) y ruido se declaran no locales (fuera de la traza). No se da forma analitica para a_scatter, a_NPVE ni a_noise: NO ENCONTRADO EN EL PDF.
  - Mapa de pesos que usa la proyeccion de la mascara como prior: w_s = P(M) ⊙ M_t + epsilon ⊙ (1 - M_t), epsilon = 0.001 (Sec. III-B, p. 2128).
  - Evidencia MC: fantoma de agua con cuatro barras de titanio; el SPR alrededor de las barras cambia: "metals can also cause changes in scattering" (Sec. II, p. 2127).
- **Advertencia contra la capa aditiva universal.** Si, explicita, contra sumar el artefacto de imagen a una imagen limpia arbitraria (modo de U-DuDoNet):
  - "I_cm cannot be synthesized by directly adding a_I to arbitrary clean CT image" (Sec. III-A, p. 2128).
  - Motivo 1: "residual artifact a_I is closely related to anatomical structures and contains texture information" (Sec. III-A, p. 2128).
  - Motivo 2: "may lead to mode collapse" al sumar una imagen arbitraria y un artefacto con texturas anatomicas (Sec. III-D, p. 2129).
  - Discusion: sintetizar "in this overlapping manner is unreasonable" (Sec. V, p. 2135).
  - Ablacion: M5 (F-Net) frente a M1 (suma simple): "F-Net can greatly improve MAR performance" (Sec. IV-F, p. 2135); Tabla II: M1 PSNR 33.25 dB, M5 36.76 dB.
  - Matiz: el paper SI mantiene la suma en el dominio del sinograma (P(I_c) + a_S, Ec. 9) y escribe la sinograma con metal como P(X) mas un termino que depende solo de metal (Ec. 2, p. 2127). La objecion es a la suma en el dominio imagen de un artefacto extraido de otro paciente, no a toda aditividad.
- **Limitaciones declaradas.** Las proyecciones clinicas son reproyecciones de imagenes del fabricante: "we adopt forward projection to simulate real projection data" (Sec. V, p. 2135). Saturacion de HU del metal en datos reales (Sec. V, p. 2135).
- **Evaluacion de la calidad de las imagenes sintetizadas I_cm:** NO ENCONTRADO EN EL PDF (solo se mide la salida MAR).
- **Metricas cuantitativas sobre datos clinicos:** NO ENCONTRADO EN EL PDF (comparacion clinica solo visual, Figs. 6-8, 10).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna cifra citada por ahora (ver Evidencia textual) | — | — |

## Donde entra en mi tesis
- Metodo del renderizador / canal de condicion analitico T: la Ec. 3 es un respaldo publicado de que el termino de endurecimiento puede escribirse solo desde la proyeccion de la mascara P(M) y el espectro. A la vez, el paper sostiene que BH queda confinado a la traza y que el resto del artefacto (scatter, NPVE, ruido) es no local y no se deriva de M; apoya que T no basta solo y justifica la banda B_delta mas un generador aprendido.
- Estado del arte: ejemplo de sintesis de artefactos aprendida (F-Net) en lugar de suma aditiva; argumento citable contra la superposicion aditiva en el dominio imagen.
- Contexto pelvico: incluye un caso clinico pelvico (Fig. 10, p. 2134), solo cualitativo.

## Dudas para el asesor
- La Ec. 3 calcula el termino BH solo desde P(M), igual que T = -FBP[h(lambda R(M))]. Pero el paper dice que ese termino esta confinado a la traza y que la parte no local (scatter, NPVE, ruido) es dependiente de la anatomia y del paciente. Un canal T aditivo unico solo cubriria la componente BH. Hace falta declarar explicitamente que T es una condicion parcial (prior de BH) y no un modelo del artefacto completo?
- PND-Net rechaza sumar en el dominio imagen un artefacto a una imagen limpia arbitraria porque el artefacto lleva textura anatomica y causa colapso de modo. En la tesis, T entra como canal de condicion (no como suma a la salida) y el difusor genera la apariencia final. Basta eso para esquivar la objecion, o hay que mostrar con una ablacion que el difusor no copia T de forma aditiva (por ejemplo, comparar salida frente a imagen limpia + T)?
- La Ec. 2 escribe P(X^m) = P(X) + termino que depende solo del metal. Observacion propia (no del paper): con espectro polienergetico y mu dependiente de E, esa separacion parece una aproximacion; el PDF no la discute. Conviene confirmar si la aditividad de T en el sinograma esta igual de justificada (o igual de aproximada) en la tesis.
- La parte no local en PND-Net se aprende de imagenes reales con metal (NSD-Net). Con CLINIC-metal disponible, tiene sentido un termino aprendido residual sobre T en lugar de un T unico?
- Los datos clinicos del paper son reconstrucciones del fabricante reproyectadas (no crudos). Si la tesis calcula R(M) sobre CT reconstruido, aplica la misma limitacion?

## Evidencia textual

| Elemento | Frase original (max. 15 palabras) | Ubicacion |
|---|---|---|
| Revista, volumen | "IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 43, NO. 6, JUNE 2024" | Encabezado, p. 2125 |
| DOI | "Digital Object Identifier 10.1109/TMI.2024.3354925" | p. 2125 |
| Componentes del artefacto metalico | "beam hardening, scatter, noise and the nonlinear partial volume effect (NPVE)" | Sec. I, p. 2125 |
| Critica a metodos previos | "only remove beam hardening artifacts in the sinogram domain" | Sec. I, p. 2126 |
| Rechazo de la sintesis aditiva | "Instead of using U-DuDoNet based on the additive attribute, we design a fusion network" | Sec. I, p. 2126 |
| Imagen con metal (definicion) | "X^m = mu(x,E) + mu_metal(E) ⊙ M, where M in {0,1}" | Sec. II, p. 2126-2127 |
| Endurecimiento desde la mascara (Ec. 3) | "a_BH = P(X^m) - P(X) = -ln{ integral eta(E) exp(-mu_metal(E)P(M)) dE }" | Sec. II, Ec. 3, p. 2127 |
| BH confinado a la traza | "Beam hardening artifacts are located only in the nonzero region" | Sec. II, p. 2127 |
| Traza de metal | "metal trace M_t, and M_t = delta(P(M))" | Sec. II, p. 2127 |
| Componentes no locales | "scatter, NPVE and noise are not only restricted to the metal trace region" | Sec. II, p. 2127 |
| Fantoma MC | "water phantom inserted with four metal rods whose resolution is 512 x 512 x 130" | Sec. II, p. 2127 |
| Voxel del fantoma | "voxel size of 0.49 mm x 0.49 mm x 3.0 mm" | Sec. II, p. 2127 |
| Fotones y energia MC | "simulated with 10x10^10 source photons for beam energy of 50-120 KeV" | Sec. II, p. 2127 |
| Detector MC | "projection image is 1024 x 768 with a pixel size of 0.6 mm x 0.6 mm" | Sec. II, p. 2127 |
| Geometria MC | "isocenter (SID) and detector (SDD) are 100 and 150 cm, respectively" | Sec. II, p. 2127 |
| Herramienta MC | "We employ an in-house MC simulation tool gMCDRR" | Sec. II, p. 2127 |
| Interacciones modeladas | "photoelectric effect, Rayleigh scattering, and Compton scattering" | Sec. II, p. 2127 |
| Resultado MC (SPR) | "the SPR around the metal rods is apparently reduced" | Sec. II, p. 2127 |
| Material de barras | "Water phantom with four titanium rods inserted for MC simulation" | Fig. 1, p. 2127 |
| Fantoma real | "realistic cone beam CT projections of a head phantom" | Fig. 2, p. 2127 |
| Modelo de artefacto en sinograma (Ec. 4) | "S_a = a_BH + a_scatter + a_NPVE + a_noise" | Sec. II, Ec. 4, p. 2128 |
| MAR en imagen (Ec. 6) | "I_mc = P^-1(S_m - S_a) = I_m - I_a" | Sec. II, Ec. 6, p. 2128 |
| Por que no sumar a_I | "a_I is closely related to anatomical structures and contains texture information" | Sec. III-A, p. 2128 |
| Por que no sumar a_I | "I_cm cannot be synthesized by directly adding a_I to arbitrary clean CT image" | Sec. III-A, p. 2128 |
| Mapa de pesos | "w_s = P(M) ⊙ M_t + epsilon ⊙ (1 - M_t)" | Sec. III-B, p. 2128 |
| Valor de epsilon | "nonzero minor value epsilon = 0.001 represents scatter and NPVE" | Sec. III-B, p. 2128 |
| Kernels del bloque no local | "kernel sizes of 3 x 3, 5 x 5 and 3 x 3" | Sec. III-B, p. 2128 |
| Arquitectura NSD-Net | "mask pyramid U-Net [38] with three encoding and decoding blocks" | Sec. III-B, p. 2128 |
| Arquitectura IR-Net | "a residual U-Net [39] with a depth of 4" | Sec. III-C, p. 2128 |
| Artefacto de imagen | "a_I = I_sc - I_mc" | Sec. III-C, p. 2129 |
| Ruta de sintesis | "we add an artifact synthesis path to achieve unpaired learning" | Sec. III-D, p. 2129 |
| Colapso de modo | "image artifact that contains anatomical textures may lead to mode collapse" | Sec. III-D, p. 2129 |
| Ecuacion de sintesis (Ec. 9) | "I_cm = G_FNet(P^-1(P(I_c) + a_S), a_I)" | Sec. III-D, Ec. 9, p. 2129 |
| Arquitectura F-Net | "mask pyramid U-Net [38] whose depth and initial number of filters are 4 and 32" | Sec. III-D, p. 2129 |
| Perdidas | "four losses: (a) adversarial, (b) cycle, (c) LI prior and (d) IC" | Sec. III-E, p. 2129 |
| Estilo de entrenamiento | "which imitates CycleGAN's [40] training style" | Sec. III-E, p. 2129 |
| Prior LI con blur | "Gaussian [31] blur operation H_sigma=3 with sigma = 3 and L1 loss" | Sec. III-E3, p. 2130 |
| Pesos de perdida (simulacion) | "alpha1 = 100, alpha2 = 10 and alpha3 = 1 for the simulation data" | Sec. III-E, p. 2130 |
| Pesos de perdida (clinico) | "For clinical data, we set alpha1 = 120, alpha2 = 10 and alpha3 = 2" | Sec. III-E, p. 2130 |
| Datos simulados (entrenamiento) | "randomly select 1000 clean CT images and 90 metal masks" | Sec. IV-A, p. 2130 |
| Fuente simulada | "from a public dataset called DeepLesion [42]" | Sec. IV-A, p. 2130 |
| Datos simulados (prueba) | "250 CT images from 15 patients and the remaining 10 metal masks for testing" | Sec. IV-A, p. 2130 |
| Geometria de simulacion | "600 projection views and 641 detector bins" | Sec. IV-A, p. 2130 |
| Geometria de simulacion | "SID) and detector (SDD) are 107.5 and 150 cm, respectively" | Sec. IV-A, p. 2130 |
| Escaner clinico | "SOMATOM Force (Siemens Healthcare) with 120 kVp tube voltage" | Sec. IV-A, p. 2130 |
| Corte clinico | "512 x 512 are reconstructed with a slice thickness of 1.5 mm" | Sec. IV-A, p. 2130 |
| Datos clinicos | "1200 metal-corrupted images and 2000 clean CT images from 40 patients" | Sec. IV-A, p. 2130 |
| Particion clinica | "randomly split into 1000 images for unpaired training and 200 images for testing" | Sec. IV-A, p. 2130 |
| Umbral de metal | "metallic implants are segmented with a threshold of 2500 HU" | Sec. IV-A, p. 2130 |
| Herramienta de preproceso | "implemented with ASTRA Toolbox [43]" | Sec. IV-A, p. 2130 |
| Hardware | "NVIDIA TITAN Xp graphics processing unit (GPU) with 12 G of memory" | Sec. IV-B, p. 2130 |
| FP/FBP | "The FP and FBP operations are implemented with the ODL library" | Sec. IV-B, p. 2130 |
| Epocas y optimizador | "300 epochs using the Adam optimizer [44] with (beta1, beta2) = (0.5, 0.999)" | Sec. IV-B, p. 2130 |
| Tasa de aprendizaje | "initial learning rate is 2 x 10^-4, and the mini-batch size is 1" | Sec. IV-B, p. 2130 |
| LR discriminadores | "two other Adam optimizers with the same learning rate of 1 x 10^-4" | Sec. IV-B, p. 2130 |
| Metricas | "peak signal-to-noise ratio (PSNR), root mean square error (RMSE), and ... (SSIM)" | Sec. IV-C, p. 2130 |
| Ventana de evaluacion | "MAR image with a window range of [-175, +275] HU" | Sec. IV-C, p. 2130 |
| Baselines | "LIMAR [5] and NMAR [13] are traditional methods" | Sec. IV-C, p. 2130 |
| Baselines supervisados | "DuDoNet [19], DuDoNet++ [23], and InDuDoNet+ [27]" | Sec. IV-C, p. 2130 |
| Baselines no supervisados | "ADN [30] and U-DuDoNet [31] are unsupervised methods" | Sec. IV-C, p. 2130 |
| Ventana Fig. 5 | "The display window is [-320 600] HU" | Fig. 5, p. 2131 |
| Mejora de RMSE | "its RMSE is reduced by 14.95 HU and 6.50 HU" (vs ADN y U-DuDoNet) | Sec. IV-D2, p. 2131 |
| S-PND-Net | "trained for 200 epochs using an Adam optimizer" | Sec. IV-D3, p. 2131 |
| S-PND-Net batch | "learning rate is 2x10^-4, and the mini-batch size is set to 2" | Sec. IV-D3, p. 2131 |
| Tabla I, Uncorrected | SSIM 0.843±0.060; RMSE 101.83±30.07 HU; PSNR 25.33±1.91 dB | Tabla I, p. 2132 |
| Tabla I, LIMAR | 0.945±0.016; 38.38±8.58; 34.03±2.30 | Tabla I, p. 2132 |
| Tabla I, NMAR | 0.948±0.015; 37.72±9.00; 34.81±2.28 | Tabla I, p. 2132 |
| Tabla I, DuDoNet | 15.34M params; 0.973±0.011; 21.89±7.21; 39.31±3.30 | Tabla I, p. 2132 |
| Tabla I, DuDoNet++ | 15.45M; 0.977±0.010; 17.52±6.50; 40.71±2.79 | Tabla I, p. 2132 |
| Tabla I, InDuDoNet+ | 1.75M; 0.976±0.010; 17.36±6.19; 41.02±2.97 | Tabla I, p. 2132 |
| Tabla I, S-PND-Net | 0.979±0.009; 17.41±5.42; 40.93±2.50 | Tabla I, p. 2132 |
| Tabla I, ADN | 27.98M; 0.950±0.019; 38.47±15.14; 34.07±3.06 | Tabla I, p. 2132 |
| Tabla I, U-DuDoNet | 13.99M; 0.964±0.010; 30.02±6.21; 35.80±1.75 | Tabla I, p. 2132 |
| Tabla I, PND-Net | 12.22M; 0.967±0.013; 23.52±6.33; 38.06±2.29 | Tabla I, p. 2132 |
| Ventana clinica | "The display window is [-110 560] HU" | Fig. 6, p. 2132 |
| Umbral de segmentacion osea | "the spine is segmented with a threshold of 200 HU" | Fig. 7, p. 2133 |
| Generalizacion multicentro | "multicentre real data whose CT scanner, acquisition parameters and HU range are" (distintos) | Sec. IV-E2, p. 2133 |
| Ventana multicentro | "The display window is [-375 400] HU" | Fig. 8, p. 2134 |
| Caso pelvico | "the uncorrected CT image of a clinical pelvic case" | Fig. 10, p. 2134 |
| Tabla II, M1 (NSD+IR) | SSIM 0.951; RMSE 37.63 HU; PSNR 33.25 dB | Tabla II, p. 2135 |
| Tabla II, M2 | 0.952; 36.93; 33.98 | Tabla II, p. 2135 |
| Tabla II, M3 | 0.958; 35.80; 34.25 | Tabla II, p. 2135 |
| Tabla II, M4 | 0.965; 29.21; 36.55 | Tabla II, p. 2135 |
| Tabla II, M5 (+F-Net) | 0.963; 28.14; 36.76 | Tabla II, p. 2135 |
| Tabla II, M6 (completo) | 0.967; 23.52; 38.06 | Tabla II, p. 2135 |
| M1/M3/M4 usan suma | "M1, M3, and M4 utilize a simple addition operator similar to that of U-DuDoNet" | Sec. IV-F, p. 2135 |
| Efecto de F-Net | "F-Net can greatly improve MAR performance" | Sec. IV-F, p. 2135 |
| Saturacion de HU | "HU value of metallic implants tends to saturate due to the limited CT range" | Sec. V, p. 2135 |
| Critica a superposicion | "directly synthesizing the artifact-contaminated image in this overlapping manner is unreasonable" | Sec. V, p. 2135 |
| Limitacion | "we adopt forward projection to simulate real projection data" | Sec. V, p. 2135 |
| Evaluacion de las imagenes sintetizadas I_cm | NO ENCONTRADO EN EL PDF | — |
| Metricas cuantitativas en datos clinicos | NO ENCONTRADO EN EL PDF | — |
| Forma analitica de a_scatter, a_NPVE, a_noise | NO ENCONTRADO EN EL PDF | — |
| Espectro eta(E) concreto o mu_metal usados para Ec. 3 | NO ENCONTRADO EN EL PDF | — |
