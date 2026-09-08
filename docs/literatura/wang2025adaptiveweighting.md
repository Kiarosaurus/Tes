# wang2025adaptiveweighting — AdaW: pesado adaptativo para MAR multi-ventana

- **DOI / URL:** 10.1109/TMI.2025.3534316 (impreso en la primera pagina, p. 2408).
  IEEE Transactions on Medical Imaging, vol. 44, no. 6, junio 2025, pp. 2408-2423
- **Codigo:** https://github.com/hongwang01/AdaW — "We will release the code at
  https://github.com/hongwang01/AdaW" (Abstract, p. 2408). No verificado que exista
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wang2025adaptiveweighting.pdf (16 paginas, completo, IEEE Xplore)

> Ficha REGENERADA el 2026-09-08 desde el PDF completo. Sustituye por entero la
> version del 2026-09-06, que se habia hecho solo desde el abstract. La marca
> "Profundidad: solo abstract" queda retirada y la regla dura de accesibilidad ya
> no aplica a esta fuente.

## Que hace (3 lineas maximo)

Propone AdaW, un algoritmo de pesado adaptativo que aprende cuanto pesa la perdida de
cada ventana HU en el entrenamiento de una red de MAR multi-ventana, via optimizacion
bi-nivel resuelta con hipergradiente y Frank-Wolfe. No es una red: es un esquema de
entrenamiento que se enchufa sobre backbones existentes (MWLNet, DICDNet, MAIL).

## Restriccion o supuesto clave

**Respuesta a la pregunta central de C3: si, es multi-ventana en HU, pero el
"adaptive weighting" del titulo NO es la parte multi-ventana.**

Hay que separar dos cosas que el titulo mezcla:

1. **El marco multi-ventana no es de este paper.** Es de la referencia [24]
   (Niu & Wang, *Multiple window learning for metal artifact reduction*, SPIE 2021,
   el MWLNet). El propio texto lo dice: *"Motivated by the existing work [24], we
   construct the general multiple-window MAR framework"* (Sec. III, p. 2410), y
   *"Following [24], we set the number of windows B to three"* (Sec. V-A-1, p. 2412).
2. **Lo propio de AdaW es el peso de la perdida de cada ventana**, no la codificacion.
   *"the weighting vector w which reflects the difficulty of learning between
   different windows"* (Sec. IV-A, p. 2411). AdaW se ejecuta solo en entrenamiento:
   *"it does not cause any inference computational overhead"* (Sec. IV-B, p. 2412).

Las tres ventanas son concretas y citables (Sec. V-A-1, p. 2412), dadas como rango
[L, H] en HU, **no** como centro/ancho:

| Ventana | Rango en HU |
|---|---|
| Large Window (LW) | [-1000HU, 2000HU] |
| Medium Window (MW) | [-320HU, 480HU] |
| Small Window (SW) | [-160HU, 240HU] |

Como se combinan: **en cascada secuencial de B etapas, no en paralelo por canales de
entrada.** Cada etapa b reconstruye dentro de su ventana; el resultado pasa a la
etapa siguiente por una "window transfer layer" T (Eq. 1) que reclipa y renormaliza
al rango de la ventana mas estrecha, y se concatena con la entrada: *"C represents
the image concatenation operation along the channel dimension"* (pie de Fig. 1,
p. 2410). **Esto no es la codificacion multi-ventana de entrada que plantea C3: es
un refinamiento progresivo de ventana ancha a ventana estrecha.** La diferencia
importa para el reclamo de novedad y hay que escribirla, no esconderla.

**Respuesta a la pregunta central de la implicancia #2: es REMOCION, no sintesis.**
El paper entero es MAR de remocion: *"The image-domain-based technique aims to
directly recover artifact-removed images from the corresponding corrupted ones"*
(Sec. II-A, p. 2409). No hay una sola linea que proponga generar artefacto como
objetivo. **La implicancia #2 se sostiene tras leer el texto completo.**

**Matiz que si obliga a corregir la redaccion:** el paper SI sintetiza artefacto
metalico, pero solo como fabrica de datos de entrenamiento, no como contribucion.
Inserta metal en cortes clinicos limpios: *"we select Fe as the metal material,
manually segment the metal masks from clinical data"* (Sec. V-A-2, p. 2413) y
*"then insert them into the collected clinical slices by carefully adjusting the
size, angle, and position"* (Sec. V-A-2, p. 2414), con simulacion fisica de
haz en abanico, 120 kVp, endurecimiento de haz y efecto de volumen parcial. Es
otra instancia del patron ya registrado en la implicancia #9.

**Dominio: imagen.** El marco reconstruye imagenes CT, no sinogramas; los backbones
(MWLNet encoder-decoder, DICDNet, MAIL) son de dominio imagen. Los unicos metodos de
proyeccion son las lineas base clasicas de comparacion (LI, NMAR, FSMAR, NLSMAR):
*"Since they are processed based on the projection data"* (Sec. V-A-4, p. 2414). Los
datos crudos de fabricante solo hacen falta para simular el set de entrenamiento, no
para inferir. **Consecuencia: es reproducible sobre imagenes ya reconstruidas como
CTPelvic1K.**

**No es un modelo de difusion, ni latente.** La difusion solo aparece citada como
trabajo ajeno: *"some works have been proposed to utilize the prior within a
pre-trained diffusion model"* (Sec. I, p. 2408, refs. [22], [23]).

**Sobre B_delta (banda extendida ~12 mm): no hay ninguna banda, margen ni region
extendida con valor numerico. NO ENCONTRADO EN EL PDF.** Lo unico cercano son
menciones cualitativas a la zona peri-implante: *"the correct recovery of tissue
structures, especially around the metal implants"* (Sec. V-E, p. 2421) y, en la
escala de expertos, *"only a small amount of artifacts in the area near the metal"*
(Sec. V-C-3, p. 2415). Ninguna se cuantifica en mm ni en pixeles. **B_delta sigue sin
precedente publicado en esta fuente.**

## Que toco de aqui

- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

Cambio respecto de la ficha anterior: deja de ser "solo contexto" puro. Ahora aporta
cifras citables (las tres ventanas HU, el umbral de 2500 HU para segmentar metal, y
el uso de CLINIC-metal). Sigue sin ser baseline: no sintetiza nada como contribucion.

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Tres ventanas: LW [-1000HU, 2000HU], MW [-320HU, 480HU], SW [-160HU, 240HU] | "large window (LW): [−1000HU, 2000HU], medium window (MW): [−320HU, 480HU]" | Sec. V-A-1, p. 2412 |
| B = 3 ventanas, siguiendo a [24] | "Following [24], we set the number of windows B to three" | Sec. V-A-1, p. 2412 |
| Umbral 2500 HU para segmentar la mascara metalica clinica | "clinical metals for CLINIC-metal and SpineWeb are segmented with the thresholding of 2,500HU" | Sec. V-A-2, p. 2413 |
| CLINIC-metal: 14 volumenes con metal, dataset pelvico, de la ref. [54] | "it contains 14 metal-corrupted volumes" | Sec. V-A-2, p. 2413 |
| Normalizacion: clip a [L, H] y escalado lineal a [0, 1] | "Ynorm = (Yclamp − L)/(H − L)" | Eq. (2), Sec. III, p. 2410 |
| Escala de calificacion de expertos de 5 niveles, 5 medicos | "experts' ratings are divided into five levels" | Sec. V-C-3, p. 2415 |

**La ref. [54] es CTPelvic1K.** La lista de referencias la da como *"P. Liu et al.,
'Deep learning to segment pelvic bones: Large-scale CT datasets and baseline models,'
Int. J. Comput. Assist. Radiol. Surg., vol. 16, no. 5, pp. 749-756, May 2021"*
(p. 2423). Es exactamente la entrada `liu2021ctpelvic1k` de mi bibliografia. Es
decir: **este paper evalua sobre el mismo subconjunto pelvico que usa mi tesis.**

## Donde entra en mi tesis

1. **Justificacion de C3 (Related Work y Metodo).** Es la fuente de las tres ventanas
   HU concretas y de la premisa de que una ventana fija no transfiere. Pero hay que
   citarlo con la salvedad de que el marco multi-ventana viene de Niu & Wang [24]:
   AdaW es fuente **secundaria** para eso, igual que `smith2006iliosacral` lo es para
   la escala 0-3.
2. **Evidencia dura para la implicancia #2.** Multi-ventana publicado = remocion.
   Confirmado contra el texto completo, ya no cualitativo.
3. **Enlace con el dataset primario.** Usa CLINIC-metal (CTPelvic1K) como set clinico
   de generalizacion cross-body-site, con las mismas 14 series anotadas que menciona
   la implicancia #13. Util para argumentar que ese subconjunto es el estandar de
   facto de MAR pelvico.
4. **Protocolo de evaluacion sin ground truth.** Su solucion al problema de que
   CLINIC-metal no tiene imagen limpia de referencia (evaluacion visual + puntuacion
   de 5 medicos en escala 1-5) es directamente reutilizable si mi validacion de
   realismo necesita lectura humana.

## Dudas para el asesor

- El marco multi-ventana es de Niu & Wang (SPIE 2021), no de AdaW. Cito el original,
  cito AdaW, o los dos? Si el asesor pide el original y no lo tengo, C3 queda
  respaldada por una fuente secundaria, que es justo el problema que ya arrastro con
  `smith2006iliosacral`.
- La combinacion de ventanas aqui es una **cascada** de ancha a estrecha, no una
  codificacion multicanal de entrada. Mi C3 dice "codificacion multi-ventana en HU".
  Son la misma cosa a ojos de un revisor de TMI, o me conviene precisar que la mia es
  multicanal simultanea y la de ellos secuencial? Lo segundo me da mas novedad pero
  me obliga a defender que la diferencia importa.
- Los autores admiten que el numero y el rango de ventanas se fija a mano y que el
  marco *"cannot achieve dynamic and adaptive reconstruction given any continuous
  window"* (Sec. V-E, p. 2421). Si mi renderizador tambien fija ventanas a mano,
  heredo la misma limitacion. Vale declararla como supuesto de diseno?
- Discrepancia interna del paper: el abstract dice cinco datasets y la conclusion
  dice cuatro. Si cito el numero, cual?

## Evidencia textual

Toda cifra, umbral, definicion de escala o criterio de evaluacion presente en el PDF.

### Configuracion multi-ventana (lo que sostiene C3)

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Numero de ventanas B = 3 | "we set the number of windows B to three" | Sec. V-A-1, p. 2412 |
| Large Window: [-1000HU, 2000HU] | "large window (LW): [−1000HU, 2000HU]" | Sec. V-A-1, p. 2412 |
| Medium Window: [-320HU, 480HU] | "medium window (MW): [−320HU, 480HU]" | Sec. V-A-1, p. 2412 |
| Small Window: [-160HU, 240HU] | "small window (SW): [−160HU, 240HU]" | Sec. V-A-1, p. 2412 |
| Ventanas de prueba cruzada 1: [-800HU, 1200HU] | "[−800HU, 1200HU]" | Tabla X, p. 2421 |
| Ventanas de prueba cruzada 2: [-640HU, 960HU] | "[−640HU, 960HU]" | Tabla X, p. 2421 |
| Ventanas de prueba cruzada 3: [-480HU, 720HU] | "[−480HU, 720HU]" | Tabla X, p. 2421 |
| Centro y ancho de ventana (formato center/width) | NO ENCONTRADO EN EL PDF (las ventanas se dan solo como rango [L, H]) | — |
| Combinacion de ventanas: concatenacion por canal entre etapas | "C represents the image concatenation operation along the channel dimension" | Fig. 1, p. 2410 |
| Transferencia entre etapas por capa de ventana T | "the information flow proceeds through a window transfer layer T" | Sec. III, p. 2410 |
| El marco multi-ventana proviene de la ref. [24] | "Motivated by the existing work [24], we construct the general multiple-window MAR framework" | Sec. III, p. 2410 |
| Motivacion: ventana fija no transfiere | "cannot be finely transferred to predict other windows for accurate artifact removal" | Sec. I, p. 2409 |
| Pocos trabajos multi-ventana | "few works have proposed to reconstruct the CT images under multiple-window configurations" | Abstract, p. 2408 |

### Truncamiento, normalizacion y rango HU

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Clip al rango [L, H] con torch.clamp | "which can be easily achieved by the 'torch.clamp' operator in PyTorch" | Sec. III, p. 2410 |
| Normalizacion lineal a [0, 1] | "Ynorm = (Yclamp − L)/(H − L)" | Eq. (2), p. 2410 |
| Practica previa: normalizar a [0,1] o [-1,1] tras clip de ventana unica | "then normalized into the range [0, 1] or [−1, 1]" | Sec. I, p. 2409 |
| Umbral de segmentacion de metal clinico: 2500 HU | "segmented with the thresholding of 2,500HU" | Sec. V-A-2, p. 2413 |
| Umbral 2500 HU repetido en la discusion | "the metal mask is empirically segmented based on the thresholding of 2500HU" | Sec. V-E, p. 2422 |
| Compresion logaritmica del rango metalico | NO ENCONTRADO EN EL PDF | — |
| Banda extendida / margen peri-implante con valor numerico (B_delta) | NO ENCONTRADO EN EL PDF | — |

### Simulacion de datos de entrenamiento (insercion sintetica de metal)

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 1000 imagenes CT limpias de DeepLesion | "pairing 1,000 clean CT images from DeepLesion [53]" | Sec. V-A-2, p. 2413 |
| Reparto: 900 entrenamiento, 100 validacion | "900 images for training set and 100 images for validation set" | Sec. V-A-2, p. 2413 |
| 90 metales, 80 entrenamiento y 10 validacion | "90 metals with different types collected from [8]" | Sec. V-A-2, p. 2413 |
| Geometria de haz en abanico | "During the simulation, fanbeam CT is adopted" | Sec. V-A-2, p. 2413 |
| Materiales: titanio, hierro, cobre, oro | "the metal materials include titanium, iron, copper, and gold" | Sec. V-A-2, p. 2413 |
| Fuente policromatica de 120 kVp | "A 120 kVp polychromatic X-ray source and an energy spectrum is simulated" | Sec. V-A-2, p. 2413 |
| Fotones incidentes: 2x10^7 | "the incident X-ray has 2 × 10^7 photons" | Sec. V-A-2, p. 2413 |
| Efecto de volumen parcial y endurecimiento de haz modelados | "partial volume effect and beam hardening are both considered" | Sec. V-A-2, p. 2413 |
| 640 vistas de proyeccion en [0, 360] grados | "640 projection views are uniformly sampled in the range [0º, 360º]" | Sec. V-A-2, p. 2413 |
| Resolucion 416 x 416 pixeles | "all the CT images are resized as 416×416 pixels" | Sec. V-A-2, p. 2413 |
| Test sintetico: 200 limpias x 10 metales = 2000 pares | "another 200 clean images and another 10 metals with varying sizes" | Sec. V-A-2, p. 2413 |
| Tamanos de los 10 implantes de test, en pixeles | "[2061, 890, 881, 451, 254, 124, 118, 112, 53, 35] in pixels" | Sec. V-A-2, p. 2413 |
| Agrupacion de metales adyacentes: 400 pares por grupo | "we take every two adjacent metals as one group (i.e., 400 image pairs)" | Sec. V-A-2, p. 2413 |
| Total de pares del test sintetico: 2000 | "a total of 2000 pairs" | Sec. V-A-2, p. 2413 |
| Insercion manual de metal en cortes clinicos (DentalCBCT) | "then insert them into the collected clinical slices by carefully adjusting the size, angle, and position" | Sec. V-A-2, p. 2414 |
| Material insertado: Fe | "we select Fe as the metal material" | Sec. V-A-2, p. 2413 |

### Datasets

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Cinco datasets de sitios corporales distintos (abstract) | "experimental comparisons executed on five datasets with different body sites" | Abstract, p. 2408 |
| Cinco datasets (repetido en contribuciones) | "Through extensive experiments on five datasets" | Sec. I, p. 2409 |
| **Discrepancia interna: cuatro datasets en la conclusion** | "Extensive experiments conducted on four datasets have substantiated" | Sec. VI, p. 2422 |
| Dental: 6 cortes | "The tooth image actually contained is 6 slices" | Sec. V-A-2, p. 2413 |
| CLINIC-metal es pelvico | "This popular clinical pelvic CT dataset is from [54]" | Sec. V-A-2, p. 2413 |
| CLINIC-metal: 14 volumenes con metal | "it contains 14 metal-corrupted volumes" | Sec. V-A-2, p. 2413 |
| CLINIC-metal proviene de CTPelvic1K (ref. [54]) | "Deep learning to segment pelvic bones: Large-scale CT datasets and baseline models" | Referencia [54], p. 2423 |
| SpineWeb: localizacion e identificacion vertebral | "This clinical testing set is from the vertebrae localization and identification dataset" | Sec. V-A-2, p. 2413 |
| DentalCBCT: 200 cortes sin metal | "We acquire another clinical dataset with 200 metal-free slices" | Sec. V-A-2, p. 2413 |
| DentalCBCT: escaner CBCT WuKong Matrix5000, Fussen | "(CBCT WuKong Matrix5000, Fussen)" | Sec. V-A-2, p. 2413 |
| DentalCBCT: 85 kVp | "scanned at a tube voltage of 85 kVp" | Sec. V-A-2, p. 2413 |
| DentalCBCT: 9 mAs | "a tube current of 9 mAs" | Sec. V-A-2, p. 2413 |
| DentalCBCT: 5x10^5 fotones | "we assume the incident X-ray has 5 × 10^5 photons" | Sec. V-A-2, p. 2413 |
| DentalCBCT: nivel medio de ruido 30 | "with the average noise level as 30" | Sec. V-A-2, p. 2413 |
| Cuatro tipos de mascara dental: braces, crowns, fillings, implants | "braces mask, crowns mask, fillings mask, implants mask" | Fig. 2, p. 2414 |
| Uso de CTPelvic1K como dataset de entrenamiento propio | NO ENCONTRADO EN EL PDF (CLINIC-metal se usa solo como test clinico) | — |

### Entrenamiento y arquitectura

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Implementado en PyTorch | "Our proposed AdaW is implemented based on PyTorch [39]" | Sec. V-A-1, p. 2412 |
| Dos GPUs NVIDIA Tesla V100-SMX2 | "on two NVIDIA Tesla V100-SMX2 GPUs" | Sec. V-A-1, p. 2412 |
| Paso mu = 1 en los experimentos | "μ is stepsize, empirically set to 1 in experiments" | Sec. IV-B, p. 2412 |
| Barrido de mu: 0.1, 0.5, 1 | "with varying μ from 0.1 to 1" | Sec. V-D-2, p. 2419 |
| Optimizacion bi-nivel resuelta con Frank-Wolfe | "α* can be easily solved by the Frank-Wolfe algorithm [48], [50]" | Sec. IV-B, p. 2412 |
| Descenso interno de un paso | "we approximately solve the inner optimization with one-step gradient descent" | Sec. IV-B, p. 2411 |
| Sin coste de inferencia adicional | "it does not cause any inference computational overhead" | Sec. IV-B, p. 2412 |
| Backbones usados: MWLNet, DICDNet, MAIL | "encoder-decoder adopted in MWLNet [24], optimized-inspired DICDNet [2]" | Sec. V-A-4, p. 2414 |
| Lineas base clasicas: LI, NMAR, FSMAR, NLSMAR | "including LI [3], NMAR [4], FSMAR [5], and NLSMAR [6]" | Sec. V-A-4, p. 2414 |
| No es difusion (la difusion es de otros) | "utilize the prior within a pre-trained diffusion model for the unsupervised reconstuction" | Sec. I, p. 2408 |
| Modelo de difusion latente propio | NO ENCONTRADO EN EL PDF | — |
| Epocas de entrenamiento (eje de Fig. 9): hasta ~199 | "Training Epoch" (eje x hasta 199) | Fig. 9, p. 2421 |

### Metricas y criterios de evaluacion

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Metricas cuantitativas: PSNR y SSIM | "PSNR/SSIM is adopted for quantitative comparison" | Sec. V-A-3, p. 2414 |
| Sin ground truth limpio en CLINIC-metal y SpineWeb: solo evaluacion visual | "we can only provide visual evaluations on these two testing sets" | Sec. V-A-3, p. 2414 |
| 30 imagenes clinicas de CLINIC-metal para la lectura de expertos | "we randomly select a total of 30 clinical images from the real CLINIC-metal dataset" | Sec. V-C-3, p. 2415 |
| 10 imagenes por ventana | "we randomly select 10 different samples" | Sec. V-C-3, p. 2415 |
| Cinco medicos clinicos como evaluadores | "Five clinical physicians are invited to rate the quality of every image" | Sec. V-C-3, p. 2415 |
| Lectura independiente y no retrospectiva, sin referencia | "independently and non-retrospectively without any label reference" | Sec. V-C-3, p. 2415 |
| Escala de 5 niveles | "experts' ratings are divided into five levels" | Sec. V-C-3, p. 2415 |
| Nivel 5: sin artefactos, tejido claro | "there are no artifacts in the image, and the tissue structure is clear" | Sec. V-C-3, p. 2415 |
| Nivel 4: poco artefacto cerca del metal | "only a small amount of artifacts in the area near the metal" | Sec. V-C-3, p. 2415 |
| Nivel 3: hay artefactos y el tejido circundante esta afectado | "there are artifacts in the image, and the surrounding tissue structure is affected" | Sec. V-C-3, p. 2416 |
| Nivel 2: artefactos significativos, tejido borroso | "there are significant metal artifacts in the image, and the surrounding tissue is blurred" | Sec. V-C-3, p. 2416 |
| Nivel 1: artefactos severos, tejido no observable | "the surrounding tissue structure cannot be observed" | Sec. V-C-3, p. 2416 |
| 150 resultados de puntuacion (30 imagenes x 5 medicos) | "the average score is computed on 150 scoring results collected from five clinical physicians" | Sec. V-C-3, p. 2416 |
| Prueba estadistica: t-test pareado | "with the paired t-test" | Sec. V-C-4, p. 2417 |
| Nivel de significancia 0.05 | "all p-values on PSNR and SSIM are less than the significance level 0.05" | Sec. V-C-1, p. 2415 |

### Resultados principales

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| MWDICDNet, promedio en las tres ventanas: 36.66 dB / 0.9868 | "MWDICDNet obtains the average score 36.66dB/0.9868" | Sec. V-B, p. 2414 |
| DICDNet-MW en su propia ventana: 37.26 dB / 0.9891 | "37.26dB/0.9891 vs. 38.26dB/0.9913" | Sec. V-B, p. 2414 |
| DICDNet-MW transferido a SW: 26.76 dB / 0.9501 | "an average PSNR/SSIM score 26.76dB/0.9501 on SW" | Sec. V-B, p. 2414 |
| MWDICDNet en SW: 32.67 dB / 0.9803, supera a DICDNet-MW | "32.67dB/0.9803 vs. 26.76dB/0.9501" | Sec. V-B, p. 2414 |
| Entrada degradada, promedio en 3 ventanas: 22.62 dB / 0.8487 | "22.62±3.39/0.8487±0.0748" | Tabla II, p. 2413 |
| AdaW+MWMAIL en Dental LW: 37.45 dB / 0.9920 vs 36.89 / 0.9914 | "37.45dB/0.9920 vs 36.89dB/0.9914" | Sec. V-C-2, p. 2415 |
| Puntuacion humana, cota superior (imagen ideal): 750 total / 5.00 media | "Upper Bound 750 5" | Tabla VI, p. 2419 |
| Puntuacion humana de la entrada con artefacto: 386 / 2.5733 | "Input 386 2.5733" | Tabla VI, p. 2419 |
| Puntuacion humana LI: 327 / 2.18 | "LI 327 2.18" | Tabla VI, p. 2419 |
| Puntuacion humana NMAR: 460 / 3.0667 | "NMAR 460 3.0667" | Tabla VI, p. 2419 |
| Puntuacion humana FSMAR: 484 / 3.2267 | "FSMAR 484 3.2267" | Tabla VI, p. 2419 |
| Puntuacion humana NLSMAR: 488 / 3.2533 | "NLSMAR 488 3.2533" | Tabla VI, p. 2419 |
| Puntuacion humana MWLNet: 457 / 3.0467 | "MWLNet 457 3.0467" | Tabla VI, p. 2419 |
| Puntuacion humana AdaW+MWLNet: 481 / 3.2067 | "AdaW+MWLNet 481 3.2067" | Tabla VI, p. 2419 |
| Puntuacion humana MWDICDNet: 516 / 3.44 | "MWDICDNet 516 3.44" | Tabla VI, p. 2419 |
| Puntuacion humana AdaW+MWDICDNet: 552 / 3.68 (mejor) | "AdaW+MWDICDNet 552 3.68" | Tabla VI, p. 2419 |
| Puntuacion humana MWMAIL: 535 / 3.5667 | "MWMAIL 535 3.5667" | Tabla VI, p. 2419 |
| Puntuacion humana AdaW+MWMAIL: 545 / 3.6333 | "AdaW+MWMAIL 545 3.6333" | Tabla VI, p. 2419 |
| Significancia de la mejora humana: p < 0.001 | "<0.001" | Tabla VI, p. 2419 |
| Un caso donde AdaW NO es significativo (MWMAIL, MW) | "0.1" | Tabla VIII, p. 2421 |
| Otro caso no significativo (MWLNet, MW en DentalCBCT) | "0.06" | Tabla VIII, p. 2421 |
| Dice, IoU u otra metrica de segmentacion aguas abajo | NO ENCONTRADO EN EL PDF | — |
| Metricas de integridad osea o metalica (tipo AAPM) | NO ENCONTRADO EN EL PDF | — |

### Limitaciones declaradas por los autores

| Limitacion | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Peor que el pesado uniforme en test intra-dominio sintetico | "perform slightly inferior to the simple equal weighting manner under the same-domain testing scene" | Sec. V-E, p. 2421 |
| El potencial de AdaW se agota en generalizacion muy dificil | "In extremely difficult generalization scenarios, the potential of the proposed AdaW would be limited" | Sec. V-E, p. 2421 |
| Sin ground truth limpio no se puede evaluar cuantitativamente | "it is hard to quantitatively evaluate the accuracy of reconstruction images" | Sec. V-E, p. 2421 |
| Hace falta phantom real para analisis cuantitativo futuro | "to collect real phantom data for quantitative analysis" | Sec. V-E, p. 2421 |
| La segmentacion del metal es critica para el tejido peri-implante | "the accurate segmentation of metals is quite important for the correct recovery of tissue structures" | Sec. V-E, p. 2421 |
| Distorsion estructural por mal condicionamiento y suavizado local | "the high ill-posedness of the reconstruction task and the local smoothing process" | Sec. V-E, p. 2421 |
| El marco no reconstruye en una ventana continua arbitraria | "this architecture cannot achieve dynamic and adaptive reconstruction given any continuous window" | Sec. V-E, p. 2421 |
| El umbral fijo de 2500 HU es artesanal y degrada la identificacion | "Such a hand-crafted manner would weaken the identification accuracy of metal implants" | Sec. V-E, p. 2422 |
| Fenomeno presente en todos los MAR profundos, no solo en AdaW | "This unfavorable phenomenon exists in different deep MAR methods" | Sec. V-E, p. 2422 |
