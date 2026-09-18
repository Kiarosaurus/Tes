# zhu2023sinogram — Sinogram domain metal artifact correction of CT via deep learning

- **DOI / URL:** https://doi.org/10.1016/j.compbiomed.2023.106710 (p. 1, pie de pagina). Comput Biol Med 155 (2023) 106710.
- **Nivel de lectura:** 3 (contexto) — PROPUESTO por Claude, pendiente de validacion por la autora
- **Leido a fondo por la autora:** no
- **PDF:** papers/zhu2023sinogram.pdf

## Que hace (3 lineas maximo)
Corrige artefactos de metal (beam hardening) en el dominio sinograma con tres modulos: Seg-Net (Attention U-Net que segmenta el metal en el sinograma), Sino-Net (U-Net piramidal sobre un sinograma residual) y un modulo de fusion en imagen.
Entrena y evalua solo con artefactos simulados: inserta metal sintetico de titanio en CT limpios de DeepLesion con un espectro polienergetico (Spektr 3.0, XCOM) y reconstruye por FBP.
Compara solo contra una ablacion (solo Seg-Net) y contra DuDoNet.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Su supuesto central es que la interpolacion lineal del sinograma aproxima el tejido: "Our proposed method assumes that P_LI is an approximate estimate of P_tissue" (p. 3, Sec. 2.1). Ademas supone que "metal areas are local in the projection domain" (p. 6, Sec. 4). El metal se modela como un material homogeneo (titanio) con un solo valor de HU asignado a una mascara delineada a mano (p. 5, Sec. 2.3.1). Los propios autores reconocen un limite: "have not corrected secondary artifacts after interpolation" (p. 7, Sec. 4). El PDF no discute prótesis grandes ni implantes de alta densidad distintos del titanio: NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna por ahora | Solo como contexto. Ver "Evidencia textual" y "Dudas para el asesor" antes de citar cualquier cifra | — |

## Donde entra en mi tesis
- Trabajo relacionado sobre MAR y sobre la segmentacion de metal. Sirve para verificar la atribucion de xie2024implantsegmentation (implicancia #47). Zhu critica la segmentacion por umbral simple en CT sin corregir porque "can make the metal projection data inaccurate or cause difficulties in clinical applications" (p. 4, Sec. 2.2.1). No dice textualmente que produzca una "inaccurate metal segmentation". La critica esta dentro de la justificacion de segmentar en el dominio sinograma. No cita ninguna referencia ni presenta evidencia cuantitativa que compare contra un umbral.
- Antecedente de que se pueden insertar implantes sinteticos en CT limpios con simulacion polienergetica (Spektr + XCOM, beam hardening, volumen parcial, ruido por photon starvation). Aqui se usa para entrenar MAR, no como aumentacion para segmentacion.
- La anatomia de las figuras (Figs. 5, 6 y 8) es pelvica, con metal en la cadera. El texto no dice que sea pelvis: NO ENCONTRADO EN EL PDF.

## Dudas para el asesor
- En la Tabla 1 (p. 6), Seg-Net y "Our Method" tienen un RMSE casi igual (188.65 vs 182.79), pero su PSNR difiere en unos 12 dB (18.39 vs 30.32). Eso es numericamente sospechoso. Ademas, el MAE de Sma cambia entre la Tabla 1 (242.23) y la Tabla 2 (210.17) sin que el texto explique por que. Conviene no citar estas cifras como referencia fuerte.
- El texto (p. 6) dice que el perfil de HU usa la "120th column", pero el pie de la Fig. 7 dice "column 152, row 280 to row 300". Es inconsistente.
- El PDF no dice en que rango o ventana de HU se calculan PSNR, SSIM y WPSNR, ni define WPSNR: NO ENCONTRADO EN EL PDF. La ventana [-1000, 1000] HU es solo la de visualizacion en las figuras.
- La implicancia #47 esta cerrada en la redaccion. Si la tesis cita a xie2024implantsegmentation parafraseando a Zhu, habria que revisar si "inaccurate metal segmentation" deforma el original ("metal projection data inaccurate"). Esa decision es de la autora.

## Evidencia textual
| Dato / cifra / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Critica al umbral simple (pregunta 1) | "only uses simple threshold segmentation in uncorrected CT images or relies on a certain metal mask" | Sec. 2.2.1, p. 4 |
| Consecuencia atribuida al umbral | "can make the metal projection data inaccurate or cause difficulties in clinical applications" | Sec. 2.2.1, p. 4 |
| Robustez de la segmentacion en sinograma frente a imagen | "more robust in dealing with reconstructed metal artifacts than image domain-based segmentation methods" | Sec. 1, contribucion 1, p. 2 |
| Otros metodos no segmentan metal en sinograma | "they are not able to accurately segment metal regions in the sinogram domain" | Sec. 1, p. 2 |
| Umbral HU o de sinograma para metal | NO ENCONTRADO EN EL PDF | — |
| Umbral de binarizacion de I_mt en el modulo de fusion | NO ENCONTRADO EN EL PDF (solo dice "after I_mt is binarized") | Sec. 2.2, p. 4 |
| PSNR 18.22 -> 30.32 | "PSNR ... of the CT image before and after correction was 18.22 and 30.32" | Resumen, p. 1 |
| SSIM 0.75 -> 0.99 | "structural similarity index measure (SSIM) improved from 0.75 to 0.99" | Resumen, p. 1 |
| WPSNR 21.69 -> 35.68 | "weighted peak signal-to-noise ratio (WPSNR) increased from 21.69 to 35.68" | Resumen, p. 1 |
| Tabla 1, Sma: MAE 242.23, RMSE 361.70, PSNR 18.22, SSIM 75.34%, WPSNR 21.69 | "Metal Image (Sma) 242.23 361.70 18.22 75.34% 21.69" | Tabla 1, p. 6 |
| Tabla 1, Seg-Net: 31.82, 188.65, 18.39, 99.07%, 22.28 | "Seg-Net Image 31.82 188.65 18.39 99.07% 22.28" | Tabla 1, p. 6 |
| Tabla 1, metodo propuesto: 31.15, 182.79, 30.32, 99.10%, 35.68 | "Our Method (Icorr) 31.15 182.79 30.32 99.10% 35.68" | Tabla 1, p. 6 |
| Datos de la Tabla 1: simulados de DeepLesion | "intuitive comparison ... on the Deep Lesion simulation data" | Sec. 3.1, p. 6 |
| Tabla 2, Sma: 210.17, 511.09, 15.07, 84.34%, 21.12 | "Metal Image (Sma) 210.17 511.09 15.07 84.34% 21.12" | Tabla 2, p. 7 |
| Tabla 2, metodo propuesto: 69.57, 324.07, 34.10, 96.08%, 40.39 | "Our Method (Icorr) 69.57 324.07 34.10 96.08% 40.39" | Tabla 2, p. 7 |
| Tabla 2, DuDoNet: 84.23, 663.43, 18.43, 88.51%, 24.39 | "DuDoNet 84.23 663.43 18.43 88.51% 24.39" | Tabla 2, p. 7 |
| SSIM/WPSNR: propuesto vs DuDoNet | "achieved a score of 96.09% and 40.39 in the SSIM and WPSNR" | Sec. 4, p. 7 (el texto dice 96.09%; la Tabla 2 dice 96.08%) |
| Metricas usadas | "including the average absolute error (MAE), root mean square error (RMSE)" | Sec. 3.2, p. 6 |
| Unidades y rango de HU de las metricas | NO ENCONTRADO EN EL PDF | — |
| Definicion de WPSNR | NO ENCONTRADO EN EL PDF | — |
| Ventana de visualizacion | "The display window for all images is set to [-1000, 1000] HU." | Pie de la Fig. 5, p. 5 |
| Perfil de HU, columna 120 (texto) | "data selected from the 120th column of the image" | Sec. 3.2, p. 6 |
| Perfil de HU, columna 152 (figura) | "The change map in CT values in column 152, row 280 to row 300" | Pie de la Fig. 7, p. 6 |
| HU media ± DE: sin corregir vs corregida | "were 52.08 ± 502.66 and 31.27 ± 59.72, respectively" | Sec. 3.2, p. 6 |
| Dataset fuente | "We utilize this dataset due to its high diversity" (DeepLesion) | Sec. 2.3.1, p. 5 |
| 80 volumenes de entrenamiento | "selected 80 volumetric CT images from it" | Sec. 2.3.1, p. 5 |
| 3 categorias de implante, 6500 imagenes de entrenamiento | "3 categories of metallic implants to synthesize 6500 training images" | Sec. 2.3.1, p. 5 |
| 20 volumenes de evaluacion + 2500 imagenes | "remaining 20 volumetric CTs were used for evaluation and verification, along with 2500" | Sec. 2.3.1, p. 5 |
| Diseno de los implantes | "size, shape, and location of metallic implants were carefully designed to mimic" | Sec. 2.3.1, p. 5 |
| Mascaras manuales, material titanio | "manually delineated the metal masks and assigned them calculated HU values for titanium" | Sec. 2.3.1, p. 5 |
| Valor numerico de HU del titanio | NO ENCONTRADO EN EL PDF | — |
| Insercion en CT limpio | "inserting the implants into clean CT images" | Sec. 2.3.1, p. 5 |
| Beam hardening | "To account for the non-linear beam-hardening factor ... we implemented the method" [42] | Sec. 2.3.1, p. 5 |
| Espectro 120 kVp (escrito "KeV"), Spektr 3.0 | "A polychromatic X-ray source with a peak voltage of 120 KeV" | Sec. 2.3.1, p. 5 |
| Sin filtrado del haz | "generated using the Spektr 3.0 toolkit [43] with no filtering" | Sec. 2.3.1, p. 5 |
| Atenuacion del metal | "X-ray attenuation coefficients for metal materials were based on the XCOM database" | Sec. 2.3.1, p. 5 |
| Volumen parcial y ruido | "partial volume effects and photon starvation-induced noise were also considered" | Sec. 2.3.1, p. 5 |
| Ruido Poisson (nombrado como tal) | NO ENCONTRADO EN EL PDF | — |
| Scatter | NO ENCONTRADO EN EL PDF | — |
| Geometria: 720 vistas en 0-360°, sinograma 720 x 1024 | "evenly sampled 720 projection views over a range of 0–360°" | Sec. 2.3.1, p. 5 |
| Datos clinicos reales con metal | NO ENCONTRADO EN EL PDF. Solo afirma "unrealistic to obtain CT images without metal" | Sec. 4, p. 7 |
| Alcance espacial del artefacto en mm | NO ENCONTRADO EN EL PDF | — |
| Artefacto en imagen (cualitativo) | "manifested as severe strip artifacts in the image domain, affecting the overall quality" | Resumen, p. 1 |
| Supuesto P_LI ≈ tejido | "Our proposed method assumes that P_LI is an approximate estimate of P_tissue" | Sec. 2.1, p. 3 |
| Lambda del sinograma residual | "a value of λ = 0.4 was chosen for experimentation" | Sec. 2.2, p. 4 |
| Perdidas | Dice para Seg-Net (Ec. 7) y "the L1 loss is used" para Sino-Net (Ec. 9) | Sec. 2.2.1-2.2.2, pp. 4-5 |
| Entrada de Seg-Net | "W1 × L1 = 720 × 1024, C1 = 64" | Pie de la Fig. 3, p. 4 |
| Radon en MATLAB | "radon function in MATLAB R2021a was utilized to obtain the sinograms" | Sec. 2.3.2, p. 5 |
| Entrenamiento de Seg-Net | "learning rate was set to 3 * 10^-3 ... 10^-5 over ... 100 epochs" | Sec. 2.3.2, p. 5 |
| Batch | "The batch size for training samples was 3." | Sec. 2.3.2, p. 5 |
| Entrenamiento de Sino-Net | "learning rate of 2 * 10^-3, and training was conducted over 500 epochs" | Sec. 2.3.2, pp. 5-6 |
| Hardware | "The main equipment used in this study was the Nvidia RTX 3060" | Sec. 2.3.2, p. 6 |
| Sobre-expansion del metal segmentado | "some metal information was over-expanded, causing distortion" | Sec. 4, p. 6 |
| Limitacion: artefactos secundarios | "have not corrected secondary artifacts after interpolation" | Sec. 4, p. 7 |
| Disponibilidad de datos | "not publicly available but may be obtained from the authors" | Data availability, p. 7 |

## Candidatos de snowballing
| Cita tal como aparece | n. ref | Por que |
|---|---|---|
| Y. Zhang, H. Yu, Convolutional neural network based metal artifact reduction in X-ray computed tomography, IEEE Trans. Med. Imag. 37 (2018) 1370–1381. | [41] | Procedimiento de insercion simulada de metal en CT limpio que Zhu sigue |
| H.S. Park, Y.E. Chung, J.K. Seo, Computed tomographic beam-hardening artefacts: mathematical characterization and analysis, Philos Trans A Math Phys Eng Sci 373 (2015). | [42] | Modelo de beam hardening usado para simular el artefacto; puede describir su estructura espacial |
| B. Meng, J. Wang, L. Xing, Sinogram preprocessing and binary reconstruction for determination of the shape and location of metal objects in computed tomography (CT), Med. Phys. 37 (2010) 5867–5875. | [5] | Segmentacion o localizacion de metal; posible fuente sobre los limites del umbral |
