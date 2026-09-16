# zhang2018 — CNN-MAR: reduccion de artefacto metalico con CNN y prior de tejido en CT

- **DOI / URL:** 10.1109/TMI.2018.2823083 (cabecera de cada pagina: version aceptada, "not been fully edited"; volumen, numero y paginas finales: NO ENCONTRADO EN EL PDF). Codigo: https://github.com/yanbozhang007/CNN-MAR.git (nota al pie 1, p. 2)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/zhang2018.pdf

## Que hace (3 lineas maximo)

Propone CNN-MAR (tarea de **remocion**): una CNN de 5 capas fusiona la imagen sin corregir, la corregida por BHC y la corregida por LI; la salida se aplana en tejido blando para formar un prior, cuya reproyeccion reemplaza la traza del metal antes de FBP. Los pares de entrenamiento se **fabrican** insertando metal sobre CT clinicos reproyectados con un modelo policromatico + Poisson en fan-beam 2D.

## Restriccion o supuesto clave

No es un paper generativo; interesa por su **protocolo de simulacion**, que es el que `lin2019` declara reutilizar ("similar procedures as in [33]"). Supuestos operativos, todos explicitos en el PDF:

- **Pseudo-proyeccion desde imagen clinica:** no usan datos crudos. Parten de DICOM reconstruidos, convierten HU a atenuacion lineal, separan agua/hueso con umbral blando y reproyectan (*"we simulate the metal artifacts based on clinical CT images"*, Sec. II-A-1, p. 2). Por tanto, la referencia "metal-free" es tambien una reconstruccion FBP simulada, no el DICOM original.
- **Metal insertado como mascara 2D en imagen, artefacto generado en proyeccion:** *"one or more binary metal shapes are placed into proper anatomical positions"* (Sec. II-A-1, p. 3); luego proyeccion policromatica (Ec. 11), Poisson (Ec. 9) y FBP.
- **Fisica modelada:** solo policromatismo (beam hardening) y ruido de Poisson: *"where beam hardening and Poisson noise are simulated"* (Sec. II-A-1, p. 2). Scatter se nombra solo como causa en la introduccion; su simulacion: NO ENCONTRADO EN EL PDF. Volumen parcial del metal: NO ENCONTRADO EN EL PDF (discrepancia con `lin2019`, que si lo declara).
- **Geometria 2D:** fan-beam equiangular, 984 vistas, 920 bins, 59.5 cm fuente-isocentro, imagenes 512 x 512 (Sec. IV-A, p. 6). Espesor de corte, helicoidal o cono en la simulacion: NO ENCONTRADO EN EL PDF.
- **Supuesto de tejido de dos materiales** (agua equivalente + hueso) con energia monocromatica equivalente E0 cuyo valor numerico: NO ENCONTRADO EN EL PDF.

Para esta tesis la restriccion relevante es la inversa de la de `lin2019`: aqui el artefacto **si** se fabrica en proyeccion, pero **sin exigir sinograma real**, lo que debilita el argumento "CTPelvic1K no trae crudos, luego no hay via de proyeccion".

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 74 CT sin metal, 15 formas de metal | *"74 metal-free CT images and 15 metal shapes are collected."* | Sec. IV-A, p. 5 |
| 100 casos en la base | *"In this work, a database is created with 100 cases."* | Sec. IV-A, p. 5 |
| Materiales: titanio, hierro, cobre, oro | *"The metal materials include titanium, iron, copper and gold."* | Sec. IV-A, p. 5 |
| Umbrales agua/hueso 100 y 1500 HU | *"corresponding to 100 HU and 1500 HU, respectively."* | Sec. IV-A, p. 6 |
| Fuente 120 kVp | *"A 120 kVp x-ray source is simulated"* | Sec. IV-A, p. 6 |
| 2 x 10^7 fotones por bin en blank scan | *"expected to receive 2 × 10^7 photons in the case of blank scan"* | Sec. IV-A, p. 6 |
| 984 vistas, 920 bins | *"984 projection views over a rotation and 920 detector bins in a row"* | Sec. IV-A, p. 6 |
| 59.5 cm fuente-centro de rotacion | *"The distance between the x-ray source and the rotation center is 59.5 cm."* | Sec. IV-A, p. 6 |
| Imagen 512 x 512 | *"each image consists of 512 × 512 pixels."* | Sec. IV-A, p. 6 |
| RMSE en HU, caso 1 (protesis bilaterales de cadera): 155.0 sin corregir, 29.1 CNN-MAR | Tabla I, fila Case 1 | Tabla I, p. 9 |
| RMSE excluye pixeles metalicos | *"with respect to the reference images, where the metallic pixels are excluded"* | Sec. V-A, p. 7 |

## Donde entra en mi tesis

- **Related Work / implicancias #61 y #63.** Es la fuente original del protocolo de insercion de metal que `lin2019` omitia. Cierra la parte de #63 sobre "que materiales, coeficientes y geometrias": materiales titanio/hierro/cobre/oro, coeficientes de XCOM (sin valores en el PDF), 15 formas segmentadas a mano de casos clinicos, fan-beam 2D.
- **Precedente de via hibrida imagen -> proyeccion -> imagen sin datos crudos.** Toda la cadena parte de CT reconstruidos. Esto hace tecnicamente posible generar **pares emparejados** (sin metal / con metal, misma anatomia, mismo pipeline FBP) sobre CTPelvic1K, lo que toca la eleccion del brazo fisico (`peters2025hybrid`) y la posicion de XCIST como fuera de alcance. Decision de la autora; no se afirma aqui que deba adoptarse.
- **Evaluacion de realismo:** los pares simulados servirian como referencia fisica simplificada (BH + Poisson, 2D) para comparar distribuciones de un renderizador generativo. Limites textuales: sin scatter, sin volumen parcial declarado, 2D, y **ninguna validacion del realismo del simulador frente a artefacto real** (NO ENCONTRADO EN EL PDF); el unico caso real es un clip quirurgico craneal evaluado solo cualitativamente.
- **Respuestas dirigidas:**
  1. **Protocolo:** ver seccion anterior y tabla final. Implantes simulados: *"dental fillings, spine fixation screws, hip prostheses, coiling, wires, etc."* (p. 5). Casos de prueba: protesis bilaterales de cadera (caso 1), dos tornillos de fijacion y un metal redondo en la escapula (caso 2), empastes dentales (caso 3). **Anatomia pelvica:** el texto solo dice *"hip prostheses"*; las Fig. 1, 2 y 7 muestran cortes pelvicos (observacion visual del lector, no enunciado). Tamanos de implantes en mm o px, material por caso y geometria de tornillos: NO ENCONTRADO EN EL PDF.
  2. **Extension espacial del artefacto:** ninguna cifra en mm, px o radio. Solo cualitativo: *"A severe dark strip presents between two hip prostheses"* (p. 6), estructuras oseas *"near the metals"* borrosas (p. 7), y *"the spatial distribution of metal artifacts in an image is not uniform"* (p. 6), usado para muestrear parches. La transicion de N = 5 pixeles es del procesamiento de tejido, no del artefacto. **No aporta ni contradice B_delta (#57).**
  3. **Dominio:** hibrido. CNN en imagen (parches 64 x 64) + reemplazo de la traza en proyeccion + FBP. Por que: *"the CNN can hardly remove all artifacts and mild artifacts typically remain"* (Sec. VI, p. 11); sin prior reproyectado *"most of the streaks that are tangent to the metals are preserved"* (Sec. V-C-1, p. 8); *"Their strengths are complementary."* (Sec. VI, p. 11). Es argumento de **remocion**, no de generacion; afirmacion sobre generar artefacto directamente en imagen: NO ENCONTRADO EN EL PDF.
  4. **Metricas:** RMSE **en HU** (Tabla I, "UNIT: HU") excluyendo pixeles metalicos, y SSIM (Tabla II). Ventanas de visualizacion en HU por figura. Sin metrica por region peri-metal ni PSNR.
  5. **Datos pareados / referencia de realismo:** si como mecanismo (ver arriba), con las limitaciones listadas. El codigo publico enlazado es de CNN-MAR; si incluye el simulador: NO ENCONTRADO EN EL PDF.

## Dudas para el asesor

- Si el protocolo de Zhang & Yu fabrica sinogramas a partir de CT reconstruidos, el argumento "sin datos crudos no hay via de proyeccion" (#6, #61) deja de sostenerse tal cual. Se reformula como costo/alcance (2D, sin scatter, reimplementacion) o se reconsidera un brazo fisico ligero de este tipo junto a `peters2025hybrid`?
- La referencia "metal-free" de Zhang es una FBP simulada, no el CT original. Si se usara para evaluar el renderizador, la comparacion debe hacerse contra esa FBP (mismo ruido/reconstruccion) o contra el CT de CTPelvic1K?
- La simulacion es 2D por corte (fan-beam). Es aceptable como referencia para un renderizador 2.5D, sabiendo que no modela consistencia entre cortes ni cono?
- `lin2019` declara volumen parcial del metal "similar a [33]", pero este PDF no lo menciona. Se cita a Zhang solo por lo que dice explicitamente?

## Evidencia textual

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Estado editorial | *"This article has been accepted for publication in a future issue of this journal"* | Cabecera, p. 1 |
| DOI | *"Citation information: DOI 10.1109/TMI.2018.2823083, IEEE Transactions on Medical Imaging"* | Cabecera, p. 1 |
| Causas fisicas del artefacto (contexto, no simuladas todas) | *"severe beam hardening, photon starvation, scatter, and so on"* | Sec. I, p. 1 |
| Morfologia del artefacto | *"strong star-shape or streak artifacts to the reconstructed CT images [1]"* | Sec. I, p. 1 |
| LI distorsiona cerca de metal grande | *"LI usually introduces new artifacts and distorts structures near large metals [12]"* | Sec. I, p. 1 |
| Ninguna estrategia unica basta | *"hard to achieve satisfactory results for all cases using a single MAR strategy"* | Sec. I, p. 1 |
| Precedente Park et al. con cadera de titanio | *"Their simulation studies showed promising results over hip prostheses of titanium."* | Sec. I, p. 1 |
| Limite de correccion BH con alto Z | *"limited capability for artifact reduction in the presence of high-Z metal"* | Sec. I, p. 1 |
| Codigo abierto | *"The source codes of our proposed method are open"* (URL en nota 1) | Sec. I, p. 2 |
| Efectos simulados | *"where beam hardening and Poisson noise are simulated"* | Sec. II-A-1, p. 2 |
| Base clinica en vez de fantomas | *"we simulate the metal artifacts based on clinical CT images"* | Sec. II-A-1, p. 2 |
| Origen de los CT | *"collected from online resources and "the 2016 Low-dose CT Grand Challenge" training dataset"* | Sec. II-A-1, p. 2 |
| Origen de las formas de metal | *"we manually segment metals and store them as small binary images"* | Sec. II-A-1, p. 2 |
| Conversion HU a atenuacion | *"its pixel values are converted from CT values to linear attenuation coefficients"* | Sec. II-A-1, p. 2 |
| Segmentacion agua/hueso | *"a soft threshold-based weighting method [41] is applied to segment the image x"* | Sec. II-A-1, p. 2 |
| Definicion umbral T1 | *"Pixels with values below a certain threshold T1 are viewed as water equivalent"* | Sec. II-A-1, p. 2 |
| Modelo de atenuacion por material | *"product of the known energy-dependent mass attenuation coefficient and the unknown energy-independent density"* | Sec. II-A-1, p. 2 |
| Energia monocromatica equivalente | *"let us assume that the equivalent monochromatic energy is E0"* | Sec. II-A-1, pp. 2-3 |
| Espectro y detector en I(E) | *"known energy dependence of both the incident x-ray source spectrum and the detector sensitivity"* | Sec. II-A-1, p. 3 |
| Ruido de Poisson | *"Approximately, the measured data follow the Poisson distribution"* | Sec. II-A-1, Ec. 9, p. 3 |
| Termino r_j | *"mean number of background events and read-out noise variance"* | Sec. II-A-1, p. 3 |
| Referencia sin metal | *"The metal-free image is reconstructed using filtered backprojection (FBP)"* | Sec. II-A-1, p. 3 |
| Insercion del metal | *"one or more binary metal shapes are placed into proper anatomical positions"* | Sec. II-A-1, p. 3 |
| Atenuacion del metal | *"assign metal pixels with linear attenuation coefficient of this material at energy E0"* | Sec. II-A-1, p. 3 |
| Metal desplaza tejido | *"pixel values in x^b and x^w are set to be zero"* | Sec. II-A-1, p. 3 |
| Reconstruccion con artefacto | *"the image x^art containing artifacts is reconstructed"* | Sec. II-A-1, p. 3 |
| BHC de primer orden | *"BHC approach [44] adopts a first-order model of beam hardening error"* | Sec. II-A-2, p. 3 |
| Ajuste de BHC | *"fitted to the correlation using a least squares cubic spline fit"* | Sec. II-A-2, p. 3 |
| LI | *"metal-affected projections are identified and replaced with the linear interpolation"* | Sec. II-A-2, p. 3 |
| LI sin reinsertar metal | *"metals are not inserted back into the LI images"* | Sec. II-A-2, p. 4 |
| Arquitectura CNN | *"comprised of an input layer, an output layer and L = 5 convolutional layers"* | Sec. II-B, p. 4 |
| Entrada/salida de la red | "Input Data 3@64× 64"; "Output 1@64× 64" | Fig. 3, p. 5 |
| Umbral minimo hueso-agua del prior | *"the bone-water threshold is not less than 350 HU"* | Sec. III-B, p. 4 |
| Hueso poco atenuante | *"larger regions are segmented with half of the bone-water threshold"* | Sec. III-B, p. 4 |
| Transicion de 5 pixeles (tejido, no artefacto) | *"we introduce an N = 5 pixel transition between water and other tissues"* | Sec. III-B, p. 4 |
| Relleno de pixeles metalicos del prior | *"the metal pixels are replaced with their nearest pixel values"* | Sec. III-B, p. 5 |
| Tamano de la base | *"74 metal-free CT images and 15 metal shapes are collected."* | Sec. IV-A, p. 5 |
| Tipos de implante simulados | *"such as dental fillings, spine fixation screws, hip prostheses, coiling, wires, etc."* | Sec. IV-A, p. 5 |
| Materiales | *"The metal materials include titanium, iron, copper and gold."* | Sec. IV-A, p. 5 |
| Ajuste manual de pose y material | *"We carefully adjust the sizes, angles, positions and inserted metal materials"* | Sec. IV-A, p. 5 |
| Numero de casos | *"In this work, a database is created with 100 cases."* | Sec. IV-A, p. 5 |
| T1 y T2 en HU | *"corresponding to 100 HU and 1500 HU, respectively."* | Sec. IV-A, p. 6 |
| Fuente de coeficientes | *"Mass attenuation coefficients of water, bone and metals are obtained for the XCOM database"* | Sec. IV-A, p. 6 |
| Geometria | *"an equi-angular fan-beam geometry is assumed."* | Sec. IV-A, p. 6 |
| Tension del tubo | *"A 120 kVp x-ray source is simulated"* | Sec. IV-A, p. 6 |
| Fotones incidentes | *"expected to receive 2 × 10^7 photons in the case of blank scan"* | Sec. IV-A, p. 6 |
| Vistas y detectores | *"984 projection views over a rotation and 920 detector bins in a row"* | Sec. IV-A, p. 6 |
| Distancia fuente-isocentro | *"The distance between the x-ray source and the rotation center is 59.5 cm."* | Sec. IV-A, p. 6 |
| Tamano de imagen | *"each image consists of 512 × 512 pixels."* | Sec. IV-A, p. 6 |
| Kernel | *"the convolutional kernel is 3 × 3 in each layer."* | Sec. IV-B, p. 6 |
| Pesos primera capa | *"the convolutional weights are 3 × 3 × 3 × 32 in the first layer"* | Sec. IV-B, p. 6 |
| Padding | *"We set the padding to 1 in each layer"* | Sec. IV-B, p. 6 |
| Numero y tamano de parches | *"10,000 patch samples with the size of 64 × 64 are extracted"* | Sec. IV-B, p. 6 |
| Artefacto no uniforme en la imagen | *"the spatial distribution of metal artifacts in an image is not uniform"* | Sec. IV-B, p. 6 |
| Muestreo de parches | *"patches with strongest artifacts in each corrected image, and the rest patches are randomly selected"* | Sec. IV-B, p. 6 |
| Proporcion de parches fuertes | *"very similar with different proportions between 50% to 80%"* | Sec. IV-B, p. 6 |
| Particion train/val | *"80% of the data is used for training and the rest is for validation"* | Sec. IV-B, p. 6 |
| Hardware | *"A GeForce GTX 970 GPU is used for acceleration."* | Sec. IV-B, p. 6 |
| Tiempo de entrenamiento | *"The training code runs about 25.5 hours and stops after 2000 iterations."* | Sec. IV-B, p. 6 |
| Inconsistencia iteraciones/epocas | *"the obtained network after 2000 training epochs is used in this work"* | Sec. V-C-4, p. 10 |
| Caso 1 | *"case 1, two hip prostheses"* | Sec. IV-C, p. 6 |
| Caso 2 | *"case 2, two fixation screws and a round metal inserted in bone"* | Sec. IV-C, p. 6 |
| Caso 2, localizacion | *"two fixation screws and a metal inserted in the shoulder blade"* | Fig. 9, p. 7 |
| Caso 3 | *"case 3: four dental fillings."* | Fig. 10, p. 8 |
| Casos de prueba excluidos del entrenamiento | *"These cases are not used in the CNN training."* | Sec. IV-C, p. 6 |
| Comparadores | *"compared to the BHC, LI and a famous prior image based method NMAR"* | Sec. IV-C, p. 6 |
| Metrica RMSE | *"metal-free images as references to compute the root mean square error (RMSE)"* | Sec. IV-C, p. 6 |
| Metrica SSIM | *"and the structural similarity (SSIM) index"* | Sec. IV-C, p. 6 |
| Escaner real | *"Siemens SOMATOM Sensation 16 CT scanner with 120 kVp and 496 mAs"* | Sec. IV-D, p. 6 |
| Geometria real | *"1160 projection views over a rotation and 672 detector bins in a row"* | Sec. IV-D, p. 6 |
| FOV real | *"The FOV is 25 cm in radius"* | Sec. IV-D, p. 6 |
| Distancia real fuente-isocentro | *"distance from the x-ray source to the rotation center is 57 cm"* | Sec. IV-D, p. 6 |
| Artefacto entre protesis de cadera | *"A severe dark strip presents between two hip prostheses in the original image"* | Sec. V-A, p. 6 |
| NMAR: aire y agua | *"air and water regions are set to -1000 HU and 0 HU"* | Sec. V-A, p. 7 |
| Dano cerca del metal con LI | *"the bony structures near the metals, as highlighted in the magnified ROI, are blurred"* | Sec. V-A, p. 7 |
| Causa: perdida cerca de metal grande | *"This is due to the significant information loss near a large metal."* | Sec. V-A, p. 7 |
| Ventana caso 1 | *"Case 1: bilateral hip prostheses."* / *"The display window is [-400 400] HU."* | Fig. 7, p. 7 |
| Ventana caso 2 | *"The display window is [-360 310] HU."* | Fig. 9, p. 7 |
| Ventana caso 3 | *"The display window is [-1000 1400] HU."* | Fig. 10, p. 8 |
| Ventana caso clinico | *"The display window is [-100 200] HU."* | Fig. 11, p. 8 |
| RMSE sin pixeles metalicos | *"with respect to the reference images, where the metallic pixels are excluded"* | Sec. V-A, p. 7 |
| Ruido incluido en RMSE | *"the artifact induced error is slightly smaller than the values listed"* | Sec. V-A, p. 7 |
| Resultado RMSE | *"the CNN-MAR achieves the smallest RMSEs for all these three cases"* | Sec. V-A, p. 7 |
| Escala SSIM | *"The SSIM index lies between 0 and 1"*; *"a higher value means better image quality"* | Sec. V-A, p. 7 |
| Resultado SSIM | *"CNN-MAR has the highest SSIM for the three cases"* | Sec. V-A, p. 8 |
| Unidad de Tabla I | "RMSE OF EACH IMAGE IN THE NUMERICAL SIMULATION STUDY. (UNIT: HU)." | Tabla I, p. 9 |
| RMSE caso 1 (HU) | Original 155.0 · BHC 86.3 · LI 46.2 · NMAR1 121.2 · NMAR2 35.4 · CNN 33.1 · CNN-MAR 29.1 | Tabla I, p. 9 |
| RMSE caso 2 (HU) | Original 71.5 · BHC 44.4 · LI 54.5 · NMAR1 50.4 · NMAR2 41.4 · CNN 31.5 · CNN-MAR 22.8 | Tabla I, p. 9 |
| RMSE caso 3 (HU) | Original 320.3 · BHC 183.5 · LI 107.3 · NMAR1 234.9 · NMAR2 82.3 · CNN 83.4 · CNN-MAR 58.4 | Tabla I, p. 9 |
| SSIM caso 1 | Original 0.565 · BHC 0.576 · LI 0.576 · NMAR1 0.887 · NMAR2 0.935 · CNN 0.940 · CNN-MAR 0.943 | Tabla II, p. 9 |
| SSIM caso 2 | Original 0.883 · BHC 0.854 · LI 0.931 · NMAR1 0.955 · NMAR2 0.950 · CNN 0.965 · CNN-MAR 0.977 | Tabla II, p. 9 |
| SSIM caso 3 | Original 0.522 · BHC 0.536 · LI 0.886 · NMAR1 0.833 · NMAR2 0.942 · CNN 0.932 · CNN-MAR 0.967 | Tabla II, p. 9 |
| Caso clinico | *"The patient is a 59 year-old female with diffused subarachnoid hemorrhage"* | Sec. V-B, p. 8 |
| Resultado clinico (cualitativo) | *"there still is only one tiny dark streak"* | Sec. V-B, p. 8 |
| Aporte de la reproyeccion | *"some artifacts can be alleviated by the forward projection"* | Sec. V-C-1, p. 8 |
| Streaks tangentes persisten sin prior | *"most of the streaks that are tangent to the metals are preserved"* | Sec. V-C-1, p. 8 |
| Peso de la traza en el sinograma | *"metal-affected projections account for a very small proportion in the sinogram"* | Sec. V-C-1, p. 8 |
| Perdida peri-metal con metal grande | *"a low-contrast feature in the vicinity of metal may suffer from missing or distortion"* | Sec. V-C-1, p. 8 |
| Tres canales mejor que dos | *"three-channel input images remarkably improve the image quality"* | Sec. V-C-2, p. 9 |
| Rol de BHC | *"Without the BHC, some artifacts are wrongly classified as tissue structures and preserved"* | Sec. V-C-2, p. 9 |
| Ablaciones sobre 10 casos | *"average RMSE and SSIM over ten simulated metal artifact cases"* | Sec. V-C-3, p. 9 |
| CNN por defecto | *"The default CNN has 5 convolutional layers, 32 filters per layer"* | Fig. 14, p. 10 |
| Eleccion de tamano medio | *"we employ a medium size CNN in this work"* | Sec. V-C-3, p. 10 |
| Tamanos de entrenamiento probados | *"trained with 100, 500, 2000 and 10000 patches"* | Sec. V-C-4, p. 10 |
| Dependencia de los datos | *"the performance of the proposed method strongly depends on the size of training data"* | Sec. V-C-4, p. 10 |
| Generalizacion fuera de tipo de metal | *"validation data is from the multiple dental fillings cases"* | Sec. V-C-4, p. 10 |
| Necesidad de variedad | *"crucial to include a wider variety of metal artifacts cases as the training data"* | Sec. V-C-4, p. 10 |
| Epocas probadas | *"after 100, 200, 1000 and 2000 training epochs"* | Sec. V-C-5, p. 11 |
| Limite de la CNN en imagen | *"the CNN can hardly remove all artifacts and mild artifacts typically remain"* | Sec. VI, p. 11 |
| Limite del prior | *"the prior image usually suffers from misclassification of tissues"* | Sec. VI, p. 11 |
| Complementariedad | *"Their strengths are complementary."* | Sec. VI, p. 11 |
| Sensibilidad a segmentacion del metal | *"may be compromised in the case of inaccurate metal segmentation [51]"* | Sec. VI, p. 11 |
| Trabajo 2D | *"works on 2D image slices, it can be directly extended to 3D volumetric images"* | Sec. VI, p. 11 |
| Costo 3D | *"3D data will require more training time"* | Sec. VI, p. 11 |
| Origen parcial de los datos | *"Part of the benchmark images in our database are obtained from"* (AAPM 2016) | Agradecimientos, p. 11 |
| **Volumen, numero y paginas finales de la revista** | **NO ENCONTRADO EN EL PDF** | — |
| **Valor numerico de E0** | **NO ENCONTRADO EN EL PDF** | — |
| **Valores numericos de coeficientes de atenuacion (agua, hueso, metales)** | **NO ENCONTRADO EN EL PDF** (solo remite a XCOM) | — |
| **Forma del espectro, filtracion o anodo** | **NO ENCONTRADO EN EL PDF** (solo "120 kVp") | — |
| **Valor de r_j (fondo / ruido de lectura)** | **NO ENCONTRADO EN EL PDF** | — |
| **Simulacion de scatter** | **NO ENCONTRADO EN EL PDF** (scatter solo como causa en Sec. I) | — |
| **Efecto de volumen parcial del metal** | **NO ENCONTRADO EN EL PDF** | — |
| **Tamano de pixel o FOV de la simulacion** | **NO ENCONTRADO EN EL PDF** | — |
| **Espesor de corte / simulacion 3D o helicoidal** | **NO ENCONTRADO EN EL PDF** | — |
| **Tamano de los implantes simulados (mm o pixeles)** | **NO ENCONTRADO EN EL PDF** | — |
| **Material asignado a cada caso de prueba** | **NO ENCONTRADO EN EL PDF** | — |
| **Descripcion geometrica de las 15 formas de metal** | **NO ENCONTRADO EN EL PDF** | — |
| **Numero de pacientes y distribucion anatomica de los 74 CT** | **NO ENCONTRADO EN EL PDF** | — |
| **Mencion textual de pelvis, sacro, ilion o tornillo iliosacro** | **NO ENCONTRADO EN EL PDF** (solo "hip prostheses"; pelvis visible en Fig. 1, 2, 7) | — |
| **Extension espacial del artefacto en mm, pixeles o radio** | **NO ENCONTRADO EN EL PDF** | — |
| **Banda peri-implante o metrica por region peri-metal** | **NO ENCONTRADO EN EL PDF** | — |
| **PSNR** | **NO ENCONTRADO EN EL PDF** | — |
| **Validacion del realismo del simulador frente a artefacto real** | **NO ENCONTRADO EN EL PDF** | — |
| **Afirmacion sobre generar artefacto directamente en dominio imagen** | **NO ENCONTRADO EN EL PDF** | — |
| **Proporcion exacta de parches fuertes finalmente usada** | **NO ENCONTRADO EN EL PDF** (solo rango 50%-80%) | — |
| **Numero de casos de la base usados para entrenar vs validar** | **NO ENCONTRADO EN EL PDF** (solo 80% de parches) | — |
| **Optimizador y tasa de aprendizaje** | **NO ENCONTRADO EN EL PDF** | — |
| **Ventana o normalizacion en HU de la entrada de la CNN** | **NO ENCONTRADO EN EL PDF** | — |
| **Valores numericos de las Fig. 14-17 (solo graficos de barras/curvas)** | **NO ENCONTRADO EN EL PDF** | — |
| **Desviacion estandar o prueba estadistica de las metricas** | **NO ENCONTRADO EN EL PDF** | — |
| **Metrica cuantitativa en el caso clinico real** | **NO ENCONTRADO EN EL PDF** | — |
| **Si el repositorio incluye el simulador de artefactos** | **NO ENCONTRADO EN EL PDF** | — |
| **Evaluacion downstream (segmentacion)** | **NO ENCONTRADO EN EL PDF** | — |
