# lyu2020dudonet — DuDoNet++: codificar la proyeccion de la mascara de metal para MAR en CT

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. El PDF local trae el sello "arXiv:2001.00340v1 [eess.IV] 2 Jan 2020" (p. 1).
- **Nivel de lectura:** 2 (metodo) — nivel PROPUESTO por Claude, pendiente de confirmacion por la autora
- **Leido a fondo por la autora:** no
- **PDF:** papers/lyu2020dudonet.pdf

> **Aviso de version.** El PDF local es el preprint de arXiv (10 paginas, titulo
> "DuDoNet++ : Encoding mask projection to reduce CT metal artifacts"), con cuatro
> autores: Yuanyuan Lyu (Z2SKY), Wei-An Lin (UMD), Jingjing Lu (PUMCH), S. Kevin Zhou
> (ICT). **Liao no figura como autor en este PDF**, y el PDF no trae datos de MICCAI 2020
> ni de LNCS. Venue MICCAI/LNCS y paginacion LNCS: NO ENCONTRADO EN EL PDF. Todas las
> paginas citadas abajo son paginas del preprint arXiv, no de la version LNCS.

## Que hace (3 lineas maximo)
Red dual (sinograma + imagen) para reduccion de artefactos metalicos (MAR) que, en vez de la traza binaria de metal de DuDoNet, codifica la proyeccion de la mascara de metal (Mp) en la red de sinograma, y alimenta la red de imagen con la imagen real con artefacto mas la mascara. Entrena con metal simulado sobre DeepLesion (100 mascaras de Zhang & Yu [34]) y prueba en clinica con mascaras obtenidas por umbral de 3000 HU.

## Restriccion o supuesto clave
No es un paper de sintesis generativa: es MAR (elimina artefacto, no lo genera). Supuestos que lo alejan de implantes rigidos grandes en 3D:
- Todo es 2D por corte con geometria fan-beam 2D ("fan-beam geometry with 640 uniformly sampled projection angles", p. 4, sec. 4.1). Tratamiento 3D / espesor de corte: NO ENCONTRADO EN EL PDF.
- El metal es un conjunto fijo de 100 mascaras 2D de [34] insertadas en cortes limpios ("inserting metallic objects into clean CT image Xgt", p. 4, sec. 4.1). Regla de colocacion o plausibilidad anatomica de la insercion: NO ENCONTRADO EN EL PDF.
- El metal se modela con un solo material y una sola densidad (ec. 3: "λm(E)ρmM", p. 2, sec. 2.2). Material/densidad concretos usados en la simulacion: NO ENCONTRADO EN EL PDF.
- En clinica asume que la reproyeccion de la imagen reconstruida sustituye al sinograma real ("we use P(Xma) as a reasonable estimation of Sma", p. 4, sec. 4.1).
- La mascara clinica es binaria por umbral fijo de 3000 HU, sin justificacion ni cita (p. 4, sec. 4.1).
Los autores dicen que el metodo mejora con metal grande (p. 1, abstract; p. 8, sec. 5), pero la mascara mas grande del test mide 2054 (unidades: NO ENCONTRADO EN EL PDF; p. 4, sec. 4.3).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 3000 HU (umbral de metal, dominio imagen, solo datos clinicos de test) | "we first segment M base on a threshold of 3000 HU" | Sec. 4.1 "Clinical Data", p. 4 |
| >100 pixeles sobre 3000 HU (criterio de seleccion de cortes clinicos) | "more than 100 pixels above 3,000 HU and moderate or severe metal artifacts" | Sec. 4.1, p. 4 |
| 100 mascaras de metal de [34] | "use 100 metal masks from [34]" | Sec. 4.1, p. 4 |
| Ventana de tejido blando [-175, +275] HU para metricas | "we use a soft tissue window in the range of [-175, +275] HU" | Sec. 4.3, p. 4 |

## Donde entra en mi tesis
- Cadena de procedencia del umbral de metal en HU (marco de datos / cribado del metal): es la fuente UNICA que xie2024implantsegmentation da para 3000 HU (p. 2 de xie2024). En este PDF el 3000 HU aparece en p. 4, sec. 4.1, solo en el test clinico, **sin justificacion ni cita**: la cadena termina aqui sin origen fisico. No respalda el 2500 HU del proyecto.
- Contexto de simulacion de metal para entrenamiento de MAR (insercion 2D de mascaras de [34] sobre DeepLesion, Poisson + volumen parcial, espectro de [20]). Referencia de "como se simula en la literatura MAR", no del renderizador.
- Evaluacion en una sola ventana de tejido blando [-175, +275] HU. Ventana osea u otras ventanas: NO ENCONTRADO EN EL PDF. Contrasta con la codificacion multi-ventana de la tesis.
- Datos clinicos: no hay pelvis clinica. CL es columna con fusion espinal; region anatomica de las 30 cortes DL: NO ENCONTRADO EN EL PDF. La pelvis solo aparece en simulacion (protesis de cadera, Fig. 6c, p. 7).

## Dudas para el asesor
- El PDF local es el preprint arXiv (sin Liao como autor); la entrada pedida es MICCAI 2020 LNCS. Hay que conseguir la version LNCS o cambiar la clave/cita a arXiv? La pagina "p. 2" que cita xie2024 no coincide con la p. 4 de este preprint.
- Si el 3000 HU no tiene justificacion aqui, basta citarlo como "umbral usado en la literatura MAR" o hace falta un fundamento fisico propio para el 2500 HU de la tesis?

## Evidencia textual
| Cifra / umbral / definicion / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| 48 de 234 estudios con artefacto metalico (Boas et al. [3]) | "Boas et al. [3] reported that 48 out of 234 medical scans contained" | Sec. 1, p. 1 |
| Mejora >4 dB sobre DuDoNet (claim de contribucion) | "We boost the MAR performance of DuDoNet by a large margin (over 4dB)" | Sec. 1, p. 2 |
| Definicion mascara de metal M | "M(x) = δ[x ∈ metal]" (ec. 4) | Sec. 2.2, p. 2 |
| Definicion proyeccion de mascara Mp | "where Mp = P(M) is the metal mask projection" | Sec. 2.2, p. 2 |
| Definicion traza binaria Mt | "Mt = δ[Mp > 0]" (ec. 7) | Sec. 3.1, p. 3 |
| Padding de sinograma | "periodic padding along the direction of projection angles and zero padding" | Sec. 3.1, p. 3 |
| 64 kernels 3x3 en capa inicial IE-Net | "an initial convolutional layer with 64 3 × 3 kernels" | Sec. 3.2, p. 4 |
| U-Net de profundidad 4, salida 64 canales | "We use a 4-depth U-Net to output a 64-ch feature map" | Sec. 3.2, p. 4 |
| Pesos de perdida = 1 | "We empirically set them to 1." | Sec. 3.2, p. 4 |
| Simulacion: Poisson + volumen parcial, siguiendo [34] | "metal artifact simulation pipeline with consideration of Poisson noise and partial volume effect" | Sec. 4.1, p. 4 |
| Ground truth de sinograma: metal reemplazado por agua | "We replace the pixel value of metal mask in Xgt with water" | Sec. 4.1, p. 4 |
| 4,200 cortes limpios de DeepLesion | "We randomly select 4,200 clean CT images from a large scale CT datebase DeepLesion" | Sec. 4.1, p. 4 |
| 100 mascaras de metal de [34] | "use 100 metal masks from [34]" | Sec. 4.1, p. 4 |
| Tipos de implante en las mascaras | "dental fillings, spine fixed crews, hip prostheses, coiling and wires, etc." | Sec. 4.1, p. 4 |
| Particion 4,000 img x 90 mascaras (train) | "We combine 4,000 images with 90 masks for training" | Sec. 4.1, p. 4 |
| Particion 200 img x 10 mascaras (test) | "200 images with 10 masks for testing" | Sec. 4.1, p. 4 |
| 360,000 casos train / 2,000 test | "yielding 360,000 cases for training and 2,000 cases for testing" | Sec. 4.1, p. 4 |
| 640 angulos en 0-360 grados, 641 detectores | "640 uniformly sampled projection angles between 0-360 degree and 641 detector channels" | Sec. 4.1, p. 4 |
| Sinograma 641x640 (DuDoNet original 321x320) | "the sinogram size is 321×320, which is smaller" | Sec. 4.1, p. 4 |
| Distancia fuente-centro de rotacion 105.84 cm | "The distance from the X-ray source and the rotation center is set to 105.84 cm" | Sec. 4.1, p. 4 |
| Espectro polienergetico tomado de [20] (kVp del espectro: NO ENCONTRADO EN EL PDF) | "we assume a same spectrum η(E) as in [20]" | Sec. 4.1, p. 4 |
| Flujo incidente 2x10^7 fotones (ruido Poisson) | "an incident flux photon number of 2 × 10^7 to simulate Poisson noise" | Sec. 4.1, p. 4 |
| Redimension a 416x416 | "we resize all the CT images to 416 × 416" | Sec. 4.1, p. 4 |
| Umbral de metal clinico 3000 HU (sin justificacion ni cita) | "we first segment M base on a threshold of 3000 HU" | Sec. 4.1, p. 4 |
| Sinograma clinico estimado por reproyeccion | "we use P(Xma) as a reasonable estimation of Sma" | Sec. 4.1, p. 4 |
| DeepLesion: 928,020 imagenes, 32,120 cortes clave | "includes 928,020 CT images and 32,120 key slices are annotated" | Sec. 4.1, p. 4 |
| CL: paciente con barras y tornillos tras fusion espinal | "a patient with metal rods and screws after spinal fusion" | Sec. 4.1, p. 4 |
| CL: GE Discovery CT750 HD, 120 kVp, 275 mAs | "acquired on a GE Discovery CT750 HD scanner with 120 kVp and 275 mAs" | Sec. 4.1, p. 4 |
| 30 cortes DL y 10 cortes CL | "We randomly select 30 slices from DL and 10 slices from CL" | Sec. 4.1, p. 4 |
| Criterio clinico: >100 pixeles sobre 3000 HU | "more than 100 pixels above 3,000 HU and moderate or severe metal artifacts" | Sec. 4.1, p. 4 |
| Adam (0.5, 0.999) | "We use the Adam optimizer with (β1, β2) = (0.5, 0.999)" | Sec. 4.2, p. 4 |
| LR 0.0002, se divide a la mitad cada 30 epocas | "The learning rate starts from 0.0002, and is halved for every 30 epochs" | Sec. 4.2, p. 4 |
| GPU 2080Ti 11 GB, 201 epocas, batch 2 | "for 201 epochs with a batch size of 2" | Sec. 4.2, p. 4 |
| Metricas imagen: PSNR y SSIM | "We use peak signal-to-noise ratio (PSNR) and structural similarity index (SSIM)" | Sec. 4.3, p. 4 |
| Rango dinamico CT -1024 a +3071 HU | "a much larger dynamic range of -1024 to +3071 HU" | Sec. 4.3, p. 4 |
| Ventana de evaluacion [-175, +275] HU (unica ventana reportada) | "we use a soft tissue window in the range of [-175, +275] HU" | Sec. 4.3, p. 4 |
| Metrica sinograma: MSE | "we use mean square error (MSE) to compare the enhanced Sse with Sgt" | Sec. 4.3, p. 4 |
| Tamanos de las 10 mascaras de test (unidades: NO ENCONTRADO EN EL PDF) | "[32, 53, 111, 115, 115, 242, 448, 878, 879, 2054]" | Sec. 4.3, p. 4 |
| Agrupacion por tamano en pares | "we group every two masks from large to small" | Sec. 4.3, p. 4 |
| Radiologo con ~20 anos de experiencia | "A proficient radiologist with about 20 years of reading experience" | Sec. 4.3, p. 4 |
| Escala de rating 1 (muy bueno) a 4 (no efectivo) | "with a rating from 1, indicating very good MAR performance, to 4" | Sec. 4.3, p. 5 |
| Test estadistico | "We use paired T-test to compare the ratings between every two methods" | Sec. 4.3, p. 5 |
| Mp vs Mt: >=4.1 dB PSNR; MSE 0.95219 -> 0.00074 | "improves the performance for at least 4.1 dB in PNSR" | Sec. 4.4, p. 5 |
| Padding: +0.15 dB, -0.00048 MSE (grupo metal mas grande) | "PSNR gain of 0.15 dB and a MSE reduction of 0.00048" | Sec. 4.4, p. 5 |
| Dual dominio: +3.0 dB vs IE-Net, +9.5 dB vs SEp-Net | "much better than the IE-Net (3.0 dB higher) and SEP-Net (9.5 dB higher)" | Sec. 4.4, p. 5 |
| Dual dominio: -0.0001 MSE | "benefits from dual domain learning with a reduction of 0.0001 in MSE" | Sec. 4.4, p. 5 |
| Con Xma: +0.00033 MSE, +0.7 dB | "affected with an increment of 0.00033 in MSE" / "improved by 0.7 dB" | Sec. 4.4, p. 6 |
| Tabla 1, promedio DuDoNet++: 37.20 dB / 97.1% / 8.8E-4 | "DuDoNet++ ... 37.20/97.1/8.8E-4" (fila Average) | Tabla 1, p. 5 |
| Tabla 1, promedio Xma: 24.58 dB / 86.9% / 4.5E+0 | "Xma ... 24.58/86.9/4.5E+0" (fila Average) | Tabla 1, p. 5 |
| Tabla 2, grupo metal mas grande, DuDoNet++: 34.60/96.2/3.4E-3 | "DuDoNet++ 34.60/96.2/3.4E-3" | Tabla 2, p. 6 |
| Tabla 2, promedios: DuDoNet 31.11/94.4; DuDoNet* 33.01/96.0; CNNMAR 27.16/92.0; NMAR 25.35/90.3; LI 24.28/89.5; cGAN-CT 20.23/85.5 | "Baseline DuDoNet [20] ... 31.11/94.4/1.5E-2" | Tabla 2, p. 6 |
| +4.2 dB vs DuDoNet; -99.4% MSE vs CNNMAR | "overall improvement of 4.2 dB in PSNR compared with DuDoNet and 99.4%" | Sec. 4.5, p. 6 |
| Fig. 6c (protesis de cadera, simulado) DuDoNet++: 34.93/95.0, MSE 0.00063 | "Figure 6c considers a hip prosthesis with strong star-like artifacts" | Sec. 4.5 y Fig. 6, p. 7 |
| Significancia vs cGAN-CT, LI, NMAR, CNNMAR | "(all P values ≤ 0.03)" | Sec. 4.6, p. 7 |
| Tabla 3: DuDoNet++ 1.27±0.13 (DL), 1.40±0.16 (CL) | "DuDoNet++ 1.27±0.13 n.a. 1.40±0.16 n.a." | Tabla 3, p. 8 |
| Tabla 3: DuDoNet* 1.46±0.11 (P 0.312), 1.70±0.21 (P 0.278) | "DuDoNet* 1.46±0.11 0.312 1.70±0.21 0.278" | Tabla 3, p. 8 |
| Justificacion/cita del umbral 3000 HU | NO ENCONTRADO EN EL PDF | — |
| Datos clinicos de pelvis con metal | NO ENCONTRADO EN EL PDF | — |

## Candidatos de snowballing
| Cita tal como aparece | N. ref | Por que |
|---|---|---|
| Y. Zhang and H. Yu. Convolutional neural network based metal artifact reduction in x-ray computed tomography. IEEE Transactions on Medical Imaging, 37(6):1370–1381, June 2018. | [34] | Origen del pipeline de simulacion/insercion de metal y de las 100 mascaras (incluye protesis de cadera); posible origen de umbrales de metal |
| W.-A. Lin, H. Liao, C. Peng, X. Sun, J. Zhang, J. Luo, R. Chellappa, and S. K. Zhou. Dudonet: Dual domain network for ct metal artifact reduction. CVPR, pages 10512–10521, 2019. | [20] | Origen del espectro η(E) usado en la simulacion. Ya leido como lin2019 segun el encargo: no agregar de nuevo |
