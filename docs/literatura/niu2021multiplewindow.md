# niu2021multiplewindow — Multiple Window Learning for CT Metal Artifact Reduction (MWLNet)

- **DOI / URL:** doi: 10.1117/12.2596239 (pag. 1, pie de pagina, Proc. SPIE Vol. 11840, 1184015, 2021)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/niu2021multiplewindow.pdf

## Que hace (3 lineas maximo)
Propone MWLNet: red de reduccion (remocion) de artefactos metalicos en CT en el dominio imagen, con varias ramas CNN en cascada, una por ventana HU, conectadas por capas "window transfer" (WT).
Entrena con pares obtenidos insertando metal simulado con CatSim en imagenes sin artefacto (spine, teeth, hip); evalua tambien en imagenes clinicas de cadera y dientes (solo visual).
NO genera artefactos con la red: solo los remueve; la simulacion la hace CatSim aparte.

## Restriccion o supuesto clave
Metodo de remocion, no de sintesis generativa. Supuesto: la tarea es mapear imagen con artefacto a imagen sin artefacto, con pares emparejados simulados ("To obtain the paired training images, CatSim was used", pag. 3, sec. 3). El metal se obtiene por umbral (> 1,900 HU) de imagenes ya afectadas y se reinserta en imagenes limpias; no modela geometria de implante rigido 3D ni posicion quirurgica. No hay mencion de banda de generacion fuera de la mascara del metal.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

(Marcado solo como contexto por defecto; la decision de usarlo como brazo de comparacion es de la autora. Ver "Evidencia textual": remueve artefactos, no los sintetiza; sin codigo ni pesos declarados en el PDF.)

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 3 ventanas: [-1000, 2000], [-320, 480], [-160, 240] | "we selected three windows, i.e., [-1000, 2000], [-320, 480], and [-160, 240]" | sec. 2, pag. 3 |
| Umbral de extraccion de metal > 1,900 HU | "thresholding the regions having larger than 1,900 HU values" | sec. 3, pag. 3 |
| Splits 80/20 | "randomly selected 80% of simulated images for training" | sec. 3, pag. 3 |
| Figura 2 (un caso spine): MWLNet PSNR 34.7 / SSIM 0.98 | (valores en anotacion de figura, no en texto) | Fig. 2, pag. 4 |

## Donde entra en mi tesis
Posible contexto del renderizador (codificacion multi-ventana en HU) y de la literatura de MAR por aprendizaje; no es metodo de sintesis. Candidato a brazo de comparacion solo si se acepta que es un removedor, no un generador (decision de la autora).

## Dudas para el asesor
- Sirve una red de remocion como brazo de comparacion de sintesis de artefactos? Con que metrica comparable?
- Las ventanas del paper ([-320, 480], [-160, 240]) frente a la ventana osea propia del proyecto: justifican la eleccion de ventanas?

## Evidencia textual

| Item | Evidencia (frase original <=15 palabras) | Seccion / pagina |
|---|---|---|
| (1) Ventana 1 (amplia): centro/ancho no dados; limites -1000 a 2000 HU | "we selected three windows, i.e., [-1000, 2000], [-320, 480], and [-160, 240]" | sec. 2, pag. 3 |
| (1) Ventana 2: -320 a 480 HU; Ventana 3: -160 a 240 HU (se dan como limites [L, H], no centro/ancho; NO se dan centro/ancho explicitos) | "[-320, 480]" y "[-160, 240]" en Fig. 1 | Fig. 1, pag. 3 |
| (1) Ejemplos de ventanas de inspeccion citados | "e.g., [-160, 240] for abdomen and [-500, 1300] for spine bone" | sec. 1, pag. 2 |
| (1) Normalizacion de ventanas a [0, 1] | "All input and output images are normalized into [0, 1]" | sec. 2, pag. 2 |
| (1) Transformacion de ventana (Eq. 1) | "I_out = Clip(I_in x (H_i - L_i) + L_i; L_o, H_o) - L_o / (H_o - L_o)" | sec. 2, Eq. 1, pag. 2 |
| (1) Umbral de extraccion de metal | "thresholding the regions having larger than 1,900 HU values" | sec. 3, pag. 3 |
| (1) Rango de normalizacion usado por metodos previos | "further normalized into [0, 1] or [-1, 1]" | sec. 1, pag. 2 |
| (2) Combinacion: cascada con ramas conectadas por capas WT; no es multicanal unico | "multiple branches ... connected to each other via our designed window transfer (WT) layers" | sec. 2, pag. 2 |
| (2) Entradas rama 1: imagen con artefacto; rama 2: dos imagenes (artefacto + prediccion de rama 1) | "takes two images as inputs, ... transformed from the artifact-affected image and the predicted image" | sec. 2, pag. 3 |
| (2) Rama 3: tres entradas (artefacto + dos predicciones) | "third branch has three input images" | sec. 2, pag. 3 |
| (2) Salida: una imagen predicha por rama, en su ventana | "I_out^w is the predicted image in the w-th branch" | sec. 2, Eq. 2, pag. 3 |
| (2) Gradientes de ramas inferiores optimizan las superiores | "gradients computed from the lower branches will help optimize the upper branches" | sec. 2, pag. 3 |
| (3) Arquitectura de cada rama | "all branches have the same encoder-decoder architecture as in ADN and LDM-DN" | sec. 2, pag. 2 |
| (3) Parametros por rama distintos | "but with different parameters" | sec. 2, pag. 2 |
| (3) Perdida L1 sumada sobre ramas (Eq. 2) | "we use the L1 loss to compute the difference" | sec. 2, pag. 3 |
| (3) Pares con/sin artefacto por simulacion con CatSim, insertando metal en imagenes limpias | "CatSim was used to simulate metal artifacts by inserting metals into the artifact-free images" | sec. 3, pag. 3 |
| (3) Metal extraido de imagenes con artefacto por umbral | "metal objects were extracted from the artifact-affected images" | sec. 3, pag. 3 |
| (3) Optimizador, learning rate, epocas, batch size | NO ENCONTRADO EN EL PDF | - |
| (3) Parametros de simulacion CatSim (geometria, espectro, ruido, etc.) | NO ENCONTRADO EN EL PDF | - |
| (4) Simula o solo remueve: la red solo remueve; CatSim simula | "reduce metal artifacts"; "multiple-window learning method for CT MAR" | sec. 1-2, pag. 2 |
| (5) Datasets: spine 136 cortes (75 con / 61 sin artefacto) | "136 slices (75 with metal artifacts and 61 without metal artifacts)" | sec. 3, pag. 3 |
| (5) Teeth 152 cortes (90 con / 62 sin) | "152 slices (90 with metal artifacts and 62 without" | sec. 3, pag. 3 |
| (5) Hip 100 cortes (20 con / 80 sin) | "100 slices (20 with metal artifacts and 80 without" | sec. 3, pag. 3 |
| (5) Tamano de imagen | "The size of all images is 512 x 512" | sec. 3, pag. 3 |
| (5) Split | "80% of simulated images for training, and the rest ... for testing" | sec. 3, pag. 3 |
| (5) Uso de CLINIC-metal / CTPelvic1K o fuente nombrada de los datos | NO ENCONTRADO EN EL PDF | - |
| (5) Imagenes clinicas (cadera, dientes) evaluadas | "evaluated on both simulated and clinical images" | sec. 4, pag. 4 |
| (5) Metricas: PSNR y SSIM en ventana [-160, 240] (comparacion cualitativa y perfiles) | "PSNR, SSIM, profiling, and visual evaluation, which were computed in the narrow window" | sec. 4, pag. 4 |
| (5) Fig. 2 spine: Uncorrected PSNR 23.8 / SSIM 0.95 | "PSNR: 23.8 SSIM: 0.95" | Fig. 2, pag. 4 |
| (5) Fig. 2 spine: NMAR PSNR 24.8 / SSIM 0.92 | "PSNR: 24.8 SSIM: 0.92" | Fig. 2, pag. 4 |
| (5) Fig. 2 spine: SWLNet-S PSNR 19.2 / SSIM 0.93 | "PSNR: 19.2 SSIM: 0.93" | Fig. 2, pag. 4 |
| (5) Fig. 2 spine: MWLNet PSNR 34.7 / SSIM 0.98 | "PSNR: 34.7 SSIM: 0.98" | Fig. 2, pag. 4 |
| (5) Metricas promediadas sobre todo el conjunto de prueba (tabla) | NO ENCONTRADO EN EL PDF | - |
| (5) Metricas cuantitativas en imagenes clinicas | NO ENCONTRADO EN EL PDF | - |
| (5) Baselines comparados: SWLNet (ventana unica) y NMAR | "single window learning baseline (SWLNet) and NMAR" | sec. 4, pag. 4 |
| (5) Hallazgo: NMAR genera artefactos secundarios | "NMAR reduced some artifacts near metal objects but generated secondary artifacts" | sec. 4, pag. 4 |
| (5) Hallazgo: ventana unica grande desplaza valores HU | "predicted HU values are significantly shifted from the ground truth" | sec. 4, pag. 4 |
| (6) Limitaciones declaradas por los autores | NO ENCONTRADO EN EL PDF | - |
| (6) Limitacion implicita citada de datos pareados clinicos / simulados | "simulated images cannot perfectly reflect real imaging conditions" | sec. 1, pag. 2 |
| (7) Codigo y/o pesos disponibles | NO ENCONTRADO EN EL PDF | - |
| (7) Posible integracion con otros marcos | "can be easily coupled with other deep learning methods" | sec. 5, pag. 6 |
