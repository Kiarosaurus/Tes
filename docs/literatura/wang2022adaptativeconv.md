# wang2022adaptativeconv — ACDNet: diccionario convolucional adaptativo para MAR en CT

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. El PDF es la version arXiv:2205.07471v2 (16 Jun 2022), codigo en https://github.com/hongwang01/ACDNet (p. 1). Venue IJCAI 2022: NO ENCONTRADO EN EL PDF (no figura en la copia local).
- **Nivel de lectura:** 3 (contexto) — nivel PROPUESTO por Claude, pendiente de confirmacion de la autora
- **Leido a fondo por la autora:** no
- **PDF:** papers/wang2022adaptativeconv.pdf

## Que hace (3 lineas maximo)
Metodo de reduccion de artefactos metalicos (MAR) solo en dominio imagen: modela el artefacto como diccionario convolucional ponderado (filtros comunes + pesos por imagen) y despliega un algoritmo de gradiente proximal en una red de T etapas (K-net, M-net, X-net).
Entrena con pares simulados DeepLesion + 100 mascaras de Zhang y Yu 2018 (protocolo de Yu et al. 2020); generaliza a CT dental simulado y a CLINIC-metal (pelvis) real.
En CLINIC-metal el metal se segmenta con umbral de 2500 HU, siguiendo a Yu et al. 2020 (p. 5).

## Restriccion o supuesto clave
No es un paper de sintesis generativa: es MAR. Supuestos que limitan su uso para implantes rigidos grandes:
- Ignora la region metalica y solo reconstruye la no metalica: "we ignore the information in the metal region" (p. 2, Sec. 2.1). La mascara no-metal I se asume conocida ("the non-metal mask I is pre-known", p. 3, Sec. 2.1).
- Procesa en 2D corte a corte: "we process CT images slice by slice for fairness" (p. 6, Sec. 5).
- La mascara clinica depende de un umbral fijo, que los propios autores reconocen fragil: "An unsatisfactory threshold possibly makes tissues be wrongly regarded as metals" (p. 6, Sec. 5).
- El metal de entrenamiento viene de 100 mascaras 2D de Zhang y Yu 2018 insertadas en DeepLesion (abdomen/torax), no de geometrias 3D de implantes de osteosintesis (p. 5, Sec. 4.1; p. 8, SM B).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 2500 HU | "the clinical metal masks are segmented with thresholding of 2500 HU" | Sec. 4.1, p. 5 |
| 14 volumenes | "CLINIC-metal [Liu et al., 2021], which contains 14 metal-corrupted volumes" | Sec. 4.1, p. 5 |

## Donde entra en mi tesis
Cadena de procedencia del umbral de 2500 HU usado como cribado heuristico de metal en CLINIC-metal (datos / preprocesamiento). ACDNet no justifica el umbral: lo toma de Yu et al. 2020 (DSCMAR). Contexto adicional: usa CLINIC-metal (pelvis) solo con comparacion visual y segmentacion downstream, sin ground truth limpio (p. 5, Sec. 4.1).

## Dudas para el asesor
- wang2025adaptiveweighting (mismo grupo) atribuye el 2500 HU a DICDNet/DuDoNet; ACDNet lo atribuye a Yu et al. 2020. Cual se cita como origen en la tesis?
- El protocolo de simulacion (Yu et al. 2020 / Zhang y Yu 2018) no reporta aqui espectro (kVp), material del metal ni geometria de haz: cuenta como fuente de parametros de simulacion o solo como antecedente?

## Evidencia textual
Paginas = numeracion del PDF local (13 paginas; texto principal pp. 1-7, Supplementary Material pp. 8-13).

| Cifra / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Umbral metal 2500 HU (citado a Yu et al. 2020) | "Following [Yu et al., 2020], the clinical metal masks are segmented with thresholding of 2500 HU." | Sec. 4.1 Clinical Data, p. 5 |
| Limitacion del umbral | "An unsatisfactory threshold possibly makes tissues be wrongly regarded as metals" | Sec. 5, p. 6 |
| Umbral adoptado como practica SOTA | "we adopt the thresholding manner to simply segment the metal for clinical data" | Sec. 5, p. 6 |
| Definicion de mascara no-metal | "I is a binary non-metal mask" | Sec. 2.1, p. 2 |
| Metal ignorado | "we ignore the information in the metal region" | Sec. 2.1, p. 2 |
| Modelo de descomposicion | "I ⊙ Y = I ⊙ X + I ⊙ A" (Eq. 1) | Sec. 2.1, p. 2 |
| N = 6, d = 32 | "In all our experiments below, N = 6 and d = 32." | nota al pie, p. 3 |
| p = 9, d = 32, N = 6 | "In our experiments, p = 9, d = 32, and N = 6." | SM A.2, p. 8 |
| N_p = 32 | "In all our experiments, N_p = 32." | SM A.1, p. 8 |
| Kernel C_p 3x3x1x32 | "in our experiment, the value is set to 3 × 3 × 1 × 32" | SM A.2, p. 8 |
| Inicializacion con LI | "X_LI is the restored CT image by the conventional linear interpolation (LI)" | SM A.2, p. 8 |
| Pesos de perdida | "μ_T is set to 1; μ_t (t = 0, 1, ..., T−1) is 0.1" | Sec. 3, p. 5 |
| ω1 = ω2 = 5x10^-4 | "ω1 and ω2 are empirically set to 5 × 10^-4" | Sec. 3, p. 5 |
| Batch 32, GPU | "trained on an NVIDIA Tesla V100-SMX2 GPU with a batch size of 32" | Sec. 3, p. 5 |
| LR 2x10^-4, epochs de decaimiento | "initial learning rate is 2 × 10^-4 and divided by 2 at epochs [50, 100, 150, 200]" | Sec. 3, p. 5 |
| 300 epochs | "The total number of epochs is 300." | Sec. 3, p. 5 |
| Parche 64x64 | "The size of input image patch is 64 × 64 pixels" | Sec. 3, p. 5 |
| 1,200 imagenes DeepLesion | "we randomly choose 1,200 clean CT images from the public DeepLesion dataset" | Sec. 4.1, p. 5 |
| 100 mascaras de Zhang y Yu 2018 | "collect 100 metal masks from [Zhang and Yu, 2018]" | Sec. 4.1, p. 5 |
| Split 90/1000 train | "90 metal masks together with 1000 clean CT images for training" | Sec. 4.1, p. 5 |
| Split 10/200 test | "10 ones together with the remaining 200 clean CT images for testing" | Sec. 4.1, p. 5 |
| Evaluacion por mascara | "take every two testing metal masks as one group for performance evaluation" | Sec. 4.1, p. 5 |
| Datos dentales (cross-body-site) | "clean dental CT images [Yu et al., 2020] are adopted" | Sec. 4.1, p. 5 |
| DeepLesion region anatomica | "DeepLesion dataset (mainly focusing on abdomen and thorax)" | SM B, p. 8 |
| Factores de simulacion | "poly-chromatic X-ray, partial volume effect, beam hardening, and Poisson noise" | SM B, p. 8 |
| 640 vistas en 0-360 | "640 projection views are uniformly spaced between 0-360 degrees." | SM B, p. 9 |
| Imagen 416x416, sinograma 641x640 | "synthesized CT images is 416 × 416 pixels ... sinogram data is 641 × 640" | SM B, p. 9 |
| Espectro (kVp), material del metal | NO ENCONTRADO EN EL PDF | — |
| Tamano de mascaras (pixeles) grande/pequeno | NO ENCONTRADO EN EL PDF (Tabla 1 solo dice "Large Metal → Small Metal") | Tabla 1, p. 5 |
| CLINIC-metal: 14 volumenes, 4 estructuras oseas | "14 metal-corrupted volumes with pixel-wise annotations of multiple bone structures" | Sec. 4.1, p. 5 |
| Estructuras | "sacrum, left hip, right hip, and lumbar spine" | Sec. 4.1, p. 5 |
| Metrica | "We adopt the PSNR/SSIM for quantitative comparison on synthesized data" | Sec. 4.1, p. 5 |
| Clinico solo visual | "only visual comparison on clinical data due to the lack of clean CT images" | Sec. 4.1, p. 5 |
| Ventana / rango HU para PSNR/SSIM | NO ENCONTRADO EN EL PDF | — |
| Multi-ventana (entrada o perdida) | NO ENCONTRADO EN EL PDF (entrada de un solo canal gris: "with only one gray channel") | SM A.1, p. 8 |
| ACDNet promedio 40.68/0.9933 | Tabla 1, fila "ACDNet (Ours)", columna Average: "40.68/0.9933" | Tabla 1, p. 5 |
| ACDNet metal grande 37.91/0.9872 | Tabla 1, fila "ACDNet (Ours)": "37.91/0.9872" (Large Metal) | Tabla 1, p. 5 |
| ACDNet metal pequeno 42.64/0.9965 | Tabla 1, fila "ACDNet (Ours)": "42.64/0.9965" (Small Metal) | Tabla 1, p. 5 |
| Input promedio 27.06/0.7586 | Tabla 1, fila "Input", Average: "27.06/0.7586" | Tabla 1, p. 5 |
| DuDoNet++ promedio 39.69/0.9886 | Tabla 1, fila "DuDoNet++": "39.69/0.9886" | Tabla 1, p. 5 |
| DuDoNet promedio 31.14/0.9814 | Tabla 1, fila "DuDoNet": "31.14/0.9814" | Tabla 1, p. 5 |
| LI promedio 29.27/0.9347 | Tabla 1, fila "LI": "29.27/0.9347" | Tabla 1, p. 5 |
| Parametros 1,602,809 | Tabla 2: "ACDNet (Ours) 1,602,809 0.3138" | Tabla 2, p. 6 |
| DuDoNet 25,834,251 | Tabla 2: "DuDoNet [Lin et al., 2019] 25,834,251 0.4225" | Tabla 2, p. 6 |
| Tiempo en 2000 imagenes 416x416 | "average testing time (seconds) computed on 2000 images with size 416 × 416" | Tabla 2, p. 6 |
| Ejemplo Fig. 3 46.08/0.9970 | Fig. 3: "ACDNet (Ours) 46.08 / 0.9970" | Fig. 3, p. 5 |
| Metal grande ejemplo 38.88/0.9931 (input 24.39/0.6616) | Fig. 5 SM: "ACDNet (Ours) 38.88 / 0.9931" | Fig. 5 SM, p. 12 |
| Dental (a) 41.41/0.9903, (b) 45.40/0.9954 | Tabla 2 SM: "41.41/0.9903" y "45.40/0.9954" (ACDNet) | Tabla 2 SM, p. 11 |
| T = 10 etapas | "The total stage T is 10" | Fig. 3 SM, p. 10 |
| 3 Resblocks (1 para K) | "we adopt 3 Resblocks to construct the backbone of deep proximal networks" | SM D.2, p. 10 |
| Ablacion Resblocks 39.46 / 40.26 / 40.68 / 40.34 | Fig. 4 SM: "Average PSNR with different number of Resblocks at every stage" | Fig. 4 SM, p. 10 |
| Orden de actualizacion 40.24-40.68 dB | "our method is insensitive to the order" | SM D.2, Tabla 1 SM, p. 10 |
| U-Net segmentacion: 103 volumenes, 35,518 cortes | "It consists of 103 clean volumes (35,518 slices)." | SM C, p. 9 |
| U-Net: LR, epochs, batch | "converges after 42 epochs of training with the batch size of 12" | SM C, p. 9 |
| U-Net: decaimiento LR | "initial learning rate is 2 × 10^-4 and divided by 2 every 20 epochs" | SM C, p. 9 |
| Dice promedio 95.46 vs 94.77 (DuDoNet++), input 92.45 | Tabla 3 SM, fila "Average DC": "92.45 ... 94.77 95.46" | Tabla 3 SM, p. 11 |
| Mejora 0.69 y 0.08 | "improvement (0.69) of our method over DuDoNet++ is rational" | SM E.1, p. 11 |
| p < 0.05, t pareado | "all P-values are less than the significance level 0.05" | SM E.1, p. 11 |

## Candidatos de snowballing
Referencias en estilo autor-ano, sin numeracion: n. ref = NO ENCONTRADO EN EL PDF.

| Cita tal como aparece | n. ref | Por que |
|---|---|---|
| [Yu et al., 2020] Lequan Yu, Zhicheng Zhang, Xiaomeng Li, and Lei Xing. Deep sinogram completion with image prior for metal artifact reduction in CT images. IEEE Transactions on Medical Imaging, 40(1):228–238, 2020. | NO ENCONTRADO EN EL PDF | ACDNet le atribuye el umbral de 2500 HU (p. 5) y el protocolo de simulacion (p. 5, p. 8) |
| [Zhang and Yu, 2018] Yanbo Zhang and Hengyong Yu. Convolutional neural network based metal artifact reduction in X-ray computed tomography. IEEE Transactions on Medical Imaging, 37(6):1370–1381, 2018. | NO ENCONTRADO EN EL PDF | Origen de las 100 mascaras de metal y de la simulacion (p. 5, p. 8-9) |
| [Liao et al., 2019] Haofu Liao, Wei-An Lin, S Kevin Zhou, and Jiebo Luo. ADN: Artifact disentanglement network for unsupervised metal artifact reduction. IEEE Transactions on Medical Imaging, 39(3):634–643, 2019. | NO ENCONTRADO EN EL PDF | Citado como fuente del protocolo de simulacion (p. 9) |
| [Lin et al., 2019] ... DuDoNet: Dual domain network for CT metal artifact reduction. CVPR, pages 10512–10521, 2019. | NO ENCONTRADO EN EL PDF | Citado como fuente del protocolo de simulacion (p. 9); wang2025adaptiveweighting le atribuye el 2500 HU |
| [Wang et al., 2021a] ... DICDNet: Deep interpretable convolutional dictionary network for metal artifact reduction in CT images. IEEE TMI, 2021. | NO ENCONTRADO EN EL PDF | wang2025adaptiveweighting le atribuye el 2500 HU; verificar cadena |
