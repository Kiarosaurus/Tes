# xie2024implantsegmentation — DiffSeg: segmentacion de implantes metalicos en CT con difusion

- **DOI / URL:** https://doi.org/10.1186/s12880-024-01379-1 (impreso en la cabecera, p. 1).
  BMC Medical Imaging (2024) 24:204. Paginacion del PDF: "Page X of 15"; las paginas citadas
  abajo son esas.
- **Nivel de lectura:** 1 (profunda): se leyeron las 15 paginas, incluidas tablas, pies de
  figura y referencias. **Nivel propuesto en `_index.md`: N2** (ver "Respuestas para la
  implicancia #47", pregunta 6)
- **Leido a fondo por la autora:** no
- **PDF:** papers/xie2024implantsegmentation.pdf (15 paginas, completo)

## Que hace (3 lineas maximo)

Propone DiffSeg, una red de difusion (ResU-Net con codificacion condicional dinamica y un filtro
frecuencial GFParser) que segmenta mascaras de metal **por corte** en CT con artefactos. Entrena y
evalua con artefactos SIMULADOS sobre CT de radioterapia sin metal; valida cualitativamente en CT
clinica y en dos fantomas, y la compara con U-Net, Attention U-Net, R2U-Net, DeepLabV3+ y umbral fijo a 2500 y 3000 HU.

## Restriccion o supuesto clave

No es un paper de sintesis generativa: la difusion se usa para **segmentar**, no para generar
artefacto. Supuestos que limitan lo que se le puede atribuir:

- **El unico ground truth es sintetico.** Las mascaras de referencia son las que se insertaron
  al simular: *"Metal implants were inserted into clean CT images to create CT images with metal
  artifacts"* (Method, Metal artifact generation, p. 3). En CT clinica no hay referencia:
  *"Due to the lack of a corresponding ground truth"* (Results, p. 6), y lo que se usa en su
  lugar son imagenes en ventana [2000,3000] HU que *"are not binary masks"* (p. 6).
- **La comparacion cuantitativa contra el umbral solo existe en datos simulados** (Tabla 2):
  *"threshold segmentation technique applied to simulated data"* (p. 6). En fantoma y clinica
  la comparacion con el umbral es solo visual (Fig. 6c y Fig. 8).
- **Trabaja en 2D por corte** (11,280 / 2,820 *slices*, matriz 512x512). Segmentacion 3D o
  volumetrica: NO ENCONTRADO EN EL PDF.
- **El remedio que propone al fallo del umbral es una red de segmentacion aprendida**, no una
  geometria rigida ni plantillas de implante. Geometrias rigidas o CAD como alternativa al
  umbral: NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito (solo si C1 conserva la cita; ver pregunta 5: respaldo PARCIAL)
- [ ] baseline de comparacion
- [x] solo contexto (fallo del umbral fijo como segmentador de metal; dependencia del umbral)

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| SE 100% del umbral a 2500 y 3000 HU (datos simulados) | "The SE metric for threshold segmentation is 100%" | Results, Comparison of results of DiffSeg and threshold segmentation, p. 6 |
| DSC 82.92% (T2500) y 84.19% (T3000), datos simulados | "82.92% and 84.19% for threshold segmentation based on 2500 HU and 3000 HU" | Abstract, Results, p. 1; Table 2, p. 11 |
| Umbral habitual 2500 HU o 3000 HU (cita a terceros) | "often set at 2500 HU [8, 9, 14] or 3000 HU [7]" | Introduction, p. 2 |
| DiffSeg DSC 95.45% y ACC 97.89% (datos simulados) | "DiffSeg achieved 95.45% and 97.89% in terms of DSC and accuracy" | Conclusions, p. 13; Table 1, p. 8 |

**Aviso de cita:** la contribucion (3) de la Introduccion imprime otras cifras para lo mismo:
*"DiffSeg achieves outstanding accuracy (95.81%) and Dice similarity coefficient (85.33%)"*
(p. 2). No coinciden con el abstract, la Tabla 1 ni las conclusiones (97.89% / 95.45%). Citar
solo las de la Tabla 1.

## Donde entra en mi tesis

- **C1, justificacion** (`tesis/main.tex`, l. 54: *"compensating for thresholding over-coverage
  bias"*). Implicancia #47. Respaldo parcial, ver abajo.
- **Discusion del metodo de extraccion de geometria (E8).** El paper da una frase citable de que
  la direccion del error depende del umbral (p. 10) y de que el umbral puede requerir ajuste por
  material y forma (p. 2). Eso sostiene la redaccion "el umbral deforma" que propone #47, no
  "el umbral siempre sobrecubre".
- **Posible diagnostico para E8 (sugerencia, no del paper):** el par SE / DSC de la Tabla 2
  es la forma en que este paper *demuestra* sobrecobertura (SE = 100% con DSC bajo). El mismo
  par, medido contra una referencia geometrica, distinguiria sobrecobertura de fragmentacion.
- **ISC (metal integrity):** solo contexto. Define DSC, SE, SP y ACC por pixel; no define ninguna
  metrica de integridad de forma ni de tamano en mm.

## Dudas para el asesor

1. La sobrecobertura que mide Xie esta en **cortes 2D simulados** con mascaras de Zhang et al.
   [50] y CT truncada a [-1000, 3071] HU (p. 3). ¿Es aceptable citarla como sesgo del umbral
   en CT clinica pelvica, cuando E8 observa lo contrario (fragmentacion, fuste bajo calibre) en
   tornillos reales de CLINIC-metal?
2. **Observacion propia, no del PDF:** el umbral de 3000 HU queda a 71 HU del techo de
   truncamiento de la simulacion (3071 HU). El paper no discute que HU tiene el metal insertado
   (NO ENCONTRADO EN EL PDF) ni si ese techo condiciona la Tabla 2. ¿Pesa esto para
   extrapolar a CT clinica con escala extendida?
3. Redaccion alternativa de C1 **propuesta, no aplicada** (regla 14): cambiar "compensating for
   thresholding over-coverage bias" por algo del tipo "avoiding the threshold-dependent size
   distortion of fixed-HU metal segmentation (over-coverage in simulated slices,
   \citealp{xie2024implantsegmentation}; fragmentation of pelvic screws in our data)". Decision
   de la autora.
4. Discrepancia interna de la ablacion (aritmetica sobre la Tabla 3, p. 12): DiffSeg_2 (sin
   codificacion dinamica, con GFParser) menos DiffSeg_1 (sin ninguno) da 0.79 puntos, que por
   definicion seria el efecto de GFParser. Pero el texto atribuye el 0.79% a la codificacion
   dinamica y el 1.1% a GFParser (p. 8). No afecta a la tesis; se anota para no citarlo.
5. El paper llama "simulation data" a las barras de titanio del fantoma en la Discusion
   (*"when analyzing titanium rod simulation data"*, p. 8), pero en Metodos son CT de fantoma
   real (p. 3). Y la Fig. 1 se titula *"An illustration of SegDiff"* (p. 4), no DiffSeg.

## Respuestas para la implicancia #47

**1. ¿Afirma que el umbral sobrecubre o sobreestima el implante?**
**Si, con otras palabras.** El termino literal "over-coverage", "overestimation" u
"over-segmentation": NO ENCONTRADO EN EL PDF. Frases que lo afirman:
- *"The mask shape obtained by threshold segmentation covered the ground truth"* (Abstract,
  Results, p. 1).
- *"T2500 and T3000 can outline the metal, although the resulting shape is slightly larger
  than the ground truth"* (Results, Comparison of results of DiffSeg and threshold
  segmentation, p. 6; se refiere a la Fig. 6a-b, datos simulados).
- *"signifying that the segmentation outcomes completely contain the ground truth"* (misma
  seccion, p. 6; datos simulados, Tabla 2).
- *"the shape obtained by T2500 is somewhat prominent and larger than the ideal result"*
  (p. 6; barra de titanio del fantoma, Fig. 6c).
- *"Commonly used thresholds like 2500 HU or 3000 HU provide an approximate shape of the
  metal but may result in artifacts extending beyond the metal itself"* (Discussion, p. 10).

**2. ¿Medicion propia o cita? Condiciones.**
- **Medicion propia, pero solo cuantitativa en datos simulados.** Tabla 2 (p. 11): T2500
  DSC 82.92 / SE 100.0 / SP 98.94 / ACC 96.94; T3000 DSC 84.19 / SE 100.0 / SP 98.95 / ACC 96.95.
  Sin test estadistico ni dispersion (NO ENCONTRADO EN EL PDF).
- **Fantoma:** solo cualitativo (Fig. 6c) sobre *"two 2 cm titanium rods"* del ArcCheck (p. 3).
  T3000 sale *"nearly square and close to the ground truth"* en la barra izquierda (p. 6): la
  sobrecobertura no es uniforme ni siquiera en el mismo corte.
- **Clinica:** sin ground truth y sin metrica del umbral. Solo: *"with DiffSeg yielding a
  smaller segmentation mask"* (p. 8, Fig. 8), que es comparacion relativa entre metodos, no
  contra el tamano real.
- **Umbrales:** 2500 HU y 3000 HU. Los dos se presentan como convencion ajena
  (*"often set at 2500 HU [8, 9, 14] or 3000 HU [7]"*, p. 2), no derivados en el paper.
- **Material:** datos simulados con mascaras de [50] (*"dental fillings, spinal fixation
  screws, hip prostheses, coils, and wires"*, p. 3), material o HU asignado al metal simulado:
  NO ENCONTRADO EN EL PDF. Fantoma de la comparacion con umbral: titanio. El fantoma de acero
  (002H9K, *"oval stainless steel rods"*) aparece solo contra redes (Fig. 5b), no contra el umbral.
- **Anatomia:** CT de radioterapia de *"20 cases of head and neck, 40 cases of chest, and 40
  cases of abdomen"* (p. 3). La pelvis no figura como region del conjunto simulado. Tornillos
  pelvicos o iliosacros como objeto medido: NO ENCONTRADO EN EL PDF.
- **Modalidad:** CT (no CBCT). Escaner de los pacientes: *"Philips Brilliance Big Bore
  scanner"*, pixel 0.975 mm, espesor 0.25 cm (p. 3). kVp, mAs, kernel y reconstruccion: NO
  ENCONTRADO EN EL PDF. Simulacion: haz en abanico, 640 proyecciones, 793 detectores, 107.5 cm
  fuente-isocentro, fuente policromatica de 2x10^7 fotones (p. 3); kVp o espectro: NO ENCONTRADO
  EN EL PDF.

**3. Metodo, datos, metricas y cifras.**
- **Tarea:** segmentacion binaria de metal por corte en CT con artefactos, pensada como paso previo
  de MAR (*"with plans to incorporate DiffSeg into MAR in the future"*, p. 11).
- **Red:** DiffSeg = DPM con ResU-Net (encoder ResNet-34), codificacion condicional dinamica
  (fusion de la mascara actual con la imagen a varias escalas) y GFParser (mapa de atencion
  aprendible en el espacio de Fourier). T = 1000, DPM-Solver con 100 pasos, AdamW 1x10^-4,
  100 epocas, batch 4, 2 RTX 3090 (pp. 4-5).
- **Datos:** 100 pacientes de radioterapia sin metal; 11,280 cortes de entrenamiento y
  validacion y 2,820 de prueba; artefacto simulado segun Yu et al. [49]; 5 pacientes clinicos
  con metal; un caso de CTPelvic1K; fantomas ArcCheck (titanio) y 002H9K (acero) (p. 3).
- **Metricas:** DSC, SE, SP y ACC contadas en pixeles (pp. 5-6); Wilcoxon sobre DSC (p. 6).
- **Cifras (Tabla 1, p. 8, datos simulados):** U-Net 93.52 DSC; Attention U-Net 94.21;
  R2U-Net 94.40; DeepLabV3+ 94.85 (p = 0.16, no significativo); DiffSeg 95.45 DSC, 97.02 SE,
  98.44 SP, 97.89 ACC. Ablacion (Tabla 3, p. 12): DiffSeg_1 93.56, DiffSeg_2 94.35 DSC.

**4. Fragmentacion, subsegmentacion, blooming, volumen parcial, reconstruccion.**
- **Fragmentacion:** si, pero **atribuida a redes CNN, no al umbral**, y precisamente en el caso de
  CLINIC-metal: *"the third-party masks from U-Net and DeepLabV3+are fragmented"* (Results,
  clinical, p. 6, Fig. 4d). En la ablacion: *"the right side of DiffSeg_2 appears
  discontinuous"* (p. 8). Fragmentacion atribuida al umbral: NO ENCONTRADO EN EL PDF. La Fig. 4
  (CLINIC-metal) no incluye umbral.
- **Subsegmentacion:** redes en simulacion, *"U-Net and Attention U-Net exhibit less prominent
  masks compared to the ground truth"* y DeepLabV3+ *"slightly smaller than the ground truth"*
  (p. 6); en clinica, *"missing parts of the screw handle"* (p. 6). **Para el umbral solo como
  posibilidad teorica:** *"larger thresholds may misidentify metal implants as tissue"*
  (Discussion, p. 10), y en sentido contrario *"A smaller threshold may lead to normal tissue
  being mistaken for metal"* (pp. 8/10).
- **Blooming:** NO ENCONTRADO EN EL PDF.
- **Volumen parcial:** solo como ingrediente de la simulacion, *"considering the partial volume
  effect and scattering effect"* (p. 3). No se discute como causa del error del umbral.
- **Dependencia de la reconstruccion o del kernel:** NO ENCONTRADO EN EL PDF. Lo mas cercano:
  *"different thresholds may be needed for metals with varying shapes and materials"* (p. 2) y
  *"influenced by factors such as type, quantity, and size of the metal"* (Limitaciones, p. 11).

**5. Evaluacion de la cita de C1: PARCIALMENTE RESPALDADA.**
- **Respaldado:** que el umbral fijo a 2500 y 3000 HU produjo mascaras que contienen y exceden el
  metal de referencia en los datos del paper (*"completely contain the ground truth"*, p. 6;
  SE 100% con DSC 82.92% / 84.19%, Tabla 2, p. 11), y que el umbral *"may result in artifacts
  extending beyond the metal itself"* (p. 10).
- **No respaldado: el caracter de "bias" general.** La propia Discusion dice que la direccion
  depende del umbral (*"larger thresholds may misidentify metal implants as tissue"*, p. 10) y
  la Introduccion que el umbral depende del material y la forma (p. 2). La sobrecobertura
  medida es de cortes 2D **simulados**; en clinica no hay ground truth (p. 6) ni cifra del umbral.
- **No respaldado: la relacion con C1.** El paper no habla de geometrias rigidas ni no
  biologicas. Su respuesta al fallo del umbral es una red de segmentacion (p. 2, contribucion 1).
  Que la geometria rigida "compense" ese sesgo es una inferencia de la tesis, no del texto.
- **No respaldado para el caso de la tesis:** no mide tornillos pelvicos, ni tamano en mm, ni
  CLINIC-metal con umbral. No contradice E8, pero tampoco lo cubre.

**6. Nivel propuesto: N2** (se confirma el nivel actual de `_index.md`, cambiando el rol). Una
linea: un error al citarlo afecta la **redaccion** de la justificacion de C1, no la contribucion
ni el benchmark (#47 ya registra que C1 se sostiene con otra justificacion). Rol corregido: no es
"posible insumo de ISC" (no define metrica de integridad) sino fuente del fallo del umbral fijo y
de su dependencia del umbral. **Alternativa defendible: N1**, solo si la autora mantiene la
sobrecobertura como unica razon de C1 para usar geometria rigida.

## Evidencia textual

Las frases son literales del PDF, recortadas a 15 palabras o menos. Paginas = "Page X of 15".
Las filas de tablas numericas reproducen la fila tal como aparece.

| # | Dato / criterio | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|---|
| 1 | DOI | "https://doi.org/10.1186/s12880-024-01379-1" | Cabecera, p. 1 |
| 2 | Revista, volumen, articulo | "Xie et al. BMC Medical Imaging (2024) 24:204" | Cabecera, p. 1 |
| 3 | Fechas de recepcion y aceptacion | "Received: 17 June 2024 / Accepted: 25 July 2024" | Declarations, p. 14 |
| 4 | Publicacion en linea | "Published online: 06 August 2024" | Declarations, p. 14 |
| 5 | Aprobacion etica | "approval number: [2020]KY154-01" | Ethics approval, p. 14 |
| 6 | Criterio de fallo del umbral (encuadre) | "the common threshold method often fails to accurately segment metals" | Abstract, Background, p. 1 |
| 7 | Cohorte, 100 pacientes | "A retrospective study was conducted on 100 patients without metal artifacts" | Method, Clinical data, p. 3 |
| 8 | Periodo de adquisicion | "between January 2021 and December 2023" | Method, Clinical data, p. 3 |
| 9 | Regiones anatomicas | "20 cases of head and neck, 40 cases of chest, and 40 cases of abdomen" | Method, Clinical data, p. 3 |
| 10 | Particion 80% | "80% of the data for each type was used for training and validation" | Method, Clinical data, p. 3 |
| 11 | 11,280 cortes de entrenamiento y validacion | "used for training and validation (11,280 slices)" | Method, Clinical data, p. 3 |
| 12 | 2,820 cortes de prueba | "the remaining 20% was used for testing (2,820 slices)" | Method, Clinical data, p. 3 |
| 13 | Demografia | "58 women and 42 men, with a mean age of 48±11 years" | Method, Clinical data, p. 3 |
| 14 | Escaner | "Philips Brilliance Big Bore scanner (Philips Medical Systems, Cleveland, OH, USA)" | Method, Clinical data, p. 3 |
| 15 | Matriz y tamano de pixel | "image matrix size of 512×512 and a pixel size of 0.975 mm" | Method, Clinical data, p. 3 |
| 16 | Espesor de corte | "The scanning layer thickness was 0.25 cm." | Method, Clinical data, p. 3 |
| 17 | 5 pacientes clinicos con metal | "CT images of 5 patients with metal implants" | Method, Clinical data, p. 3 |
| 18 | Tipo de implante clinico | "such as vertebral steel nails and femoral head implants" | Method, Clinical data, p. 3 |
| 19 | Caso de CTPelvic1K | "a case from the CTPelvic1K dataset [48] was randomly selected" | Method, Clinical data, p. 3 |
| 20 | Descripcion de CTPelvic1K | "This dataset primarily consisted of postoperative images with metal artifacts." | Method, Clinical data, p. 3 |
| 21 | Fantoma de titanio | "ArcCheck phantom (Sun Nuclear Corporation, Melbourne, FL) containing two 2 cm titanium rods" | Method, Clinical data, p. 3 |
| 22 | Fantoma de acero | "002H9K phantom (CIRS Inc., Norfolk, VA) containing oval stainless steel rods" | Method, Clinical data, p. 3 |
| 23 | Valor de metal en 002H9K, 11,080 HU | "stored in 16-bit format, with a metal CT value of 11,080 HU" | Method, Clinical data, p. 3 |
| 24 | Normalizacion [0,1] | "Data values were normalized to a range of [0,1]" | Method, Clinical data, p. 3 |
| 25 | Metodo de simulacion (Yu et al. [49]) | "simulating beam hardening and Poisson noise based on the simulation method" | Method, Metal artifact generation, p. 3 |
| 26 | 640 proyecciones | "fan-beam geometry with 640 uniformly sampled projection angles between 0 and 360 degrees" | Method, Metal artifact generation, p. 3 |
| 27 | 793 detectores | "793 detector bins per projection angle" | Method, Metal artifact generation, p. 3 |
| 28 | 107.5 cm fuente-centro de rotacion | "from the X-ray source to the rotation center was set at 107.5 cm" | Method, Metal artifact generation, p. 3 |
| 29 | Fuente policromatica | "a polychromatic X-ray source was utilized" | Method, Metal artifact generation, p. 3 |
| 30 | 2x10^7 fotones y volumen parcial (exponente en superindice en el PDF) | "incident beam X-ray of 2×10^7 photons, considering the partial volume effect and scattering effect" | Method, Metal artifact generation, p. 3 |
| 31 | Sinograma 793x640 | "The sinogram size of the artifact CT was 793×640." | Method, Metal artifact generation, p. 3 |
| 32 | 100 mascaras de Zhang et al. [50] | "100 manually segmented metal implants, such as dental fillings, spinal fixation screws" | Method, Metal artifact generation, p. 3 |
| 33 | Resto de tipos de mascara | "hip prostheses, coils, and wires" | Method, Metal artifact generation, p. 3 |
| 34 | Recorte a 250 pixeles | "The matrix size was reduced to 250 pixels if it exceeded this size." | Method, Metal artifact generation, p. 3 |
| 35 | Zona de colocacion de la mascara | "horizontal directions 150 to 350, vertical directions 180 to 330" | Method, Metal artifact generation, p. 3 |
| 36 | Umbral del body mask (sin valor) | "The body mask is segmented using a threshold value" | Method, Metal artifact generation, p. 3 |
| 37 | Contraste con Wang et al. [8], 90 mascaras | "where a layer of CT was paired with 90 masks" | Method, Metal artifact generation, p. 3 |
| 38 | Una mascara aleatoria por CT | "this study utilized a random metal mask for each CT scan" | Method, Metal artifact generation, p. 3 |
| 39 | Truncamiento [-1000, 3071] HU | "the CT values were truncated to [-1000, 3071] HU to match actual CT values" | Method, Metal artifact generation, p. 3 |
| 40 | Red base | "The ResU-Net network is adopted as the DPM learning network" | Network model, p. 3 |
| 41 | Encoder ResNet-34, 7x7, 64 filtros | "ResNet-34 down-sampling section includes a 7×7 convolutional layer with 64 filters" | Network model, p. 4 |
| 42 | Bloque residual | "Each residual block comprises two 3×3 convolutional layers" | Network model, p. 4 |
| 43 | Decoder | "a 2×2 transposed convolution with a stride of 2" | Network model, p. 4 |
| 44 | DPM-Solver, 100 pasos | "during inference with a sampling step of 100 to speed up sampling" | Network model, p. 4 |
| 45 | Nombre en la Fig. 1 | "An illustration of SegDiff." | Fig. 1, p. 4 |
| 46 | T = 1000 | "linear noise time and noise prediction with a diffusion step T of 1000" | Implementation details, p. 5 |
| 47 | Hardware | "using 2 NVIDIA RTX 3090 GPUs" | Implementation details, p. 5 |
| 48 | Optimizador, lr, epocas | "AdamW optimizer with an initial learning rate of 1×10−4, for 100 epochs" | Implementation details, p. 5 |
| 49 | Batch | "with a batch size of 4" | Implementation details, p. 5 |
| 50 | Comparadores | "U-Net [44], Attention U-Net [45], R2U-Net [46], and DeepLabV3+ [47]" | Implementation details, p. 5 |
| 51 | Cuatro metricas | "Dice similarity coefficient (DSC), sensitivity (SE), specificity (SP), and accuracy (ACC)" | Verification indicators, p. 5 |
| 52 | Definicion DSC | "DSC = 2TP / (FP + 2TP + FN)" (formula) | Verification indicators, p. 5 |
| 53 | Definicion SE | "SE = TP / (TP + FN)" (formula) | Verification indicators, p. 5 |
| 54 | Definicion SP | "SP = TN / (TN + FP)" (formula) | Verification indicators, p. 6 |
| 55 | Definicion ACC | "ACC = (TP + TN) / (TP + FP + TN + FN)" (formula) | Verification indicators, p. 6 |
| 56 | Unidad de conteo: pixel | "true positive, false positive, true negative, and false negative pixels" | Verification indicators, p. 6 |
| 57 | Test estadistico | "a Wilcoxon signed-rank test was conducted to compare DSC" | Results, simulated data, p. 6 |
| 58 | Significancia | "Except for DeeplabV3+, all p-values were less than 0.05" | Results, simulated data, p. 6 |
| 59 | Tabla 1, U-Net | "U-Net 93.52 95.52 97.88 96.65 <0.05" | Table 1, p. 8 |
| 60 | Tabla 1, Attention U-Net | "Attention U-Net 94.21 96.33 97.95 97.20 <0.05" | Table 1, p. 8 |
| 61 | Tabla 1, R2U-Net | "R2U-Net 94.40 96.68 98.12 97.33 <0.05" | Table 1, p. 8 |
| 62 | Tabla 1, DeepLabV3+ | "DeepLabV3+ 94.85 96.77 98.39 97.15 0.16" | Table 1, p. 8 |
| 63 | Tabla 1, DiffSeg | "DiffSeg 95.45 97.02 98.44 97.89" | Table 1, p. 8 |
| 64 | ACC 97.89% en abstract | "the accuracy of DiffSeg for metal segmentation of simulated data was 97.89%" | Abstract, Results, p. 1 |
| 65 | DSC 95.45% en abstract | "and that of DSC was 95.45%" | Abstract, Results, p. 1 |
| 66 | Cifras discrepantes en contribuciones | "DiffSeg achieves outstanding accuracy (95.81%) and Dice similarity coefficient (85.33%)" | Introduction, contribucion (3), p. 2 |
| 67 | Cifras en conclusiones | "DiffSeg achieved 95.45% and 97.89% in terms of DSC and accuracy" | Conclusions, p. 13 |
| 68 | Umbral habitual 2500 / 3000 HU | "often set at 2500 HU [8, 9, 14] or 3000 HU [7]" | Introduction, p. 2 |
| 69 | Dificultad cerca del hueso | "ensuring accuracy with this method can be difficult, especially near high-density anatomical structures like bone" | Introduction, p. 2 |
| 70 | Umbral dependiente de material y forma | "different thresholds may be needed for metals with varying shapes and materials" | Introduction, p. 2 |
| 71 | Umbral relativo de Yazdi [15], 90% | "proposed using 90% of the maximum gray value as the threshold" | Introduction, p. 2 |
| 72 | Pauwels [10], 10-20 s | "with the algorithm typically taking 10–20 s" | Introduction, p. 2 |
| 73 | Hegazy [35], Dice por paciente | "Dice similarity indices of 0.98, 0.97, 0.93, and 0.95" | Introduction, p. 2 |
| 74 | Area afectada mas alla del metal | "the affected area extends beyond the metal itself, posing a challenge" | Introduction, p. 2 |
| 75 | Umbral cubre el ground truth | "The mask shape obtained by threshold segmentation covered the ground truth" | Abstract, Results, p. 1 |
| 76 | DSC del umbral en abstract | "82.92% and 84.19% for threshold segmentation based on 2500 HU and 3000 HU" | Abstract, Results, p. 1 |
| 77 | Definicion T2500 / T3000 | "T2500 and T3000 refer to threshold methods based on 2500 HU and 3000 HU" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 78 | Datos de esa comparacion | "results of DiffSeg and threshold segmentation in simulated and phantom data" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 79 | Umbral mayor que GT (simulado) | "the resulting shape is slightly larger than the ground truth" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 80 | T2500 en barra de titanio | "the shape obtained by T2500 is somewhat prominent and larger than the ideal result" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 81 | T3000 en barra izquierda | "titanium rod segmented by T3000 is nearly square and close to the ground truth" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 82 | T3000 en barra derecha | "the upper side of the right titanium rod appears somewhat prominent" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 83 | Umbral capta la camara de ionizacion | "the threshold method successfully segments the ionization chamber located between the titanium rods" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 84 | Tabla 2 es sobre datos simulados | "quantitative outcomes of the threshold segmentation technique applied to simulated data" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 85 | SE 100% del umbral | "The SE metric for threshold segmentation is 100%" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 86 | Criterio de contencion | "signifying that the segmentation outcomes completely contain the ground truth" | Results, Comparison of DiffSeg and threshold, p. 6 |
| 87 | Tabla 2, T2500 | "T2500 82.92 100.0 98.94 96.94" | Table 2, p. 11 |
| 88 | Tabla 2, T3000 | "T3000 84.19 100.0 98.95 96.95" | Table 2, p. 11 |
| 89 | Tabla 2, DiffSeg | "DiffSeg 95.45 97.02 98.44 97.89" | Table 2, p. 11 |
| 90 | Paneles de la Fig. 6 | "(a)(b) for simulated data, (c) for phantom data" | Fig. 6, p. 11 |
| 91 | Referencia clinica sin GT, ventana [2000,3000] HU | "the display range of [2000,3000] HU was used to display artifact CT images" | Results, clinical data, p. 6 |
| 92 | La referencia clinica no es mascara | "adjusted images are not binary masks and are further checked by a senior physician" | Results, clinical data, p. 6 |
| 93 | Referencia clinica frente a umbral | "Adjusted images have more metal details than the threshold segmentation results." | Results, clinical data, p. 6 |
| 94 | Ventana de visualizacion general | "the display range of (a)-(d) being [-500,1500] HU" | Fig. 3, p. 7 (igual en Figs. 4, 6, 7 y 8) |
| 95 | Ventana del fantoma B | "the phantom image B is displayed in the range of [-1000,3000] HU" | Fig. 5, p. 10 |
| 96 | Subsegmentacion de redes (simulado) | "U-Net and Attention U-Net exhibit less prominent masks compared to the ground truth" | Results, simulated data, p. 6 |
| 97 | DeepLabV3+ menor (simulado) | "The metal shape produced by DeepLabV3+is slightly smaller than the ground truth." | Results, simulated data, p. 6 |
| 98 | Partes faltantes de tornillo (clinico) | "U-Net, Attention U-Net, and DeepLabV3+exhibit missing parts of the screw handle" | Results, clinical data, p. 6 |
| 99 | Caso CLINIC-metal, forma incompleta | "the Attention U-Net segmentation results are incomplete in shape" | Results, clinical data, p. 6 |
| 100 | Fragmentacion (redes, CLINIC-metal) | "the third-party masks from U-Net and DeepLabV3+are fragmented" | Results, clinical data, p. 6 |
| 101 | Definicion DiffSeg_1 | "DiffSeg_1 indicates the lack of dynamic conditional coding and GFParser" | Ablation experiment, p. 8 |
| 102 | Definicion DiffSeg_2 | "DiffSeg_2 indicates the absence of dynamic conditional coding" | Ablation experiment, p. 8 |
| 103 | Discontinuidad en ablacion | "the right side of DiffSeg_2 appears discontinuous" | Ablation experiment, p. 8 |
| 104 | +0.79% atribuido a codificacion dinamica | "leading to a 0.79% enhancement in DSC" | Ablation experiment, p. 8 |
| 105 | +1.1% atribuido a GFParser | "contributing to a 1.1% improvement in DSC for DiffSeg" | Ablation experiment, p. 8 |
| 106 | Tabla 3, DiffSeg_1 | "DiffSeg_1 93.56 96.47 97.09 95.71" | Table 3, p. 12 |
| 107 | Tabla 3, DiffSeg_2 | "DiffSeg_2 94.35 96.65 97.56 96.96" | Table 3, p. 12 |
| 108 | Tabla 3, DiffSeg | "DiffSeg 95.45 97.02 98.44 97.89" | Table 3, p. 12 |
| 109 | Evaluacion MAR usada | "impact of segmentation results on normalized metal artifact reduction (NMAR) [3]" | Influence of segmentation results on MAR, p. 8 |
| 110 | Clinica: DiffSeg mas pequena que el umbral | "with DiffSeg yielding a smaller segmentation mask" | Influence of segmentation results on MAR, p. 8 |
| 111 | NMAR conserva hueso | "NMAR_DiffSeg retained some bone information, highlighted by a red arrow" | Influence of segmentation results on MAR, p. 8 |
| 112 | Explicacion en fantoma | "attributed to its smaller partition result and reduced impact on the partial reconstruction" | Influence of segmentation results on MAR, p. 8 |
| 113 | Umbral simple en CT sin corregir | "rely on simple threshold segmentation in uncorrected CT images" | Discussion, p. 8 |
| 114 | Consecuencia, citada a [36] | "which may result in inaccurate metal segmentation or hinder clinical applications [36]" | Discussion, p. 8 |
| 115 | Simulado: todos segmentan | "both traditional methods and DiffSeg effectively segment the entire metal masks" | Discussion, p. 8 |
| 116 | Clinico: cae el rendimiento | "the traditional method's segmentation performance significantly decreases compared to simulated data" | Discussion, p. 8 |
| 117 | Desviacion de bordes | "resulting in a greater deviation of partial metal boundaries" | Discussion, p. 8 |
| 118 | Barras de titanio llamadas "simulation data" | "when analyzing titanium rod simulation data" | Discussion, p. 8 |
| 119 | Ambiguedad de borde por convolucion | "The inherent property of convolution is easy to cause the boundary ambiguity" | Discussion, p. 8 |
| 120 | Alcance declarado del analisis de umbral | "This study analyzes the impact of different threshold values in medical imaging." | Discussion, p. 8 |
| 121 | Umbral bajo: tejido como metal | "A smaller threshold may lead to normal tissue being mistaken for metal" | Discussion, pp. 8/10 (la frase cruza de pagina) |
| 122 | Umbral alto: metal como tejido | "larger thresholds may misidentify metal implants as tissue" | Discussion, p. 10 |
| 123 | 2500 / 3000 HU dan forma aproximada | "thresholds like 2500 HU or 3000 HU provide an approximate shape of the metal" | Discussion, p. 10 |
| 124 | Artefacto mas alla del metal | "but may result in artifacts extending beyond the metal itself" | Discussion, p. 10 |
| 125 | DiffSeg menor que el umbral | "the segmentation results from DiffSeg are smaller than those from threshold methods" | Discussion, p. 10 |
| 126 | Limitacion 1 | "This exploratory study focuses on metal segmentation" | Discussion, limitaciones, p. 11 |
| 127 | Limitacion 2 | "influenced by factors such as type, quantity, and size of the metal" | Discussion, limitaciones, p. 11 |
| 128 | Tiempo de inferencia, 3 s | "Each batch's inference time in the DPM inference stage is approximately 3 s." | Discussion, limitaciones, p. 11 |
| 129 | Disponibilidad de datos | "available from the corresponding author on reasonable request" | Data availability, p. 14 |
| 130 | Termino literal "over-coverage" / "overestimation" / "over-segmentation" | NO ENCONTRADO EN EL PDF | — |
| 131 | kVp del escaner clinico | NO ENCONTRADO EN EL PDF | — |
| 132 | mAs, CTDI o dosis | NO ENCONTRADO EN EL PDF | — |
| 133 | Kernel o algoritmo de reconstruccion de las CT clinicas | NO ENCONTRADO EN EL PDF | — |
| 134 | Escaner con que se adquirieron los fantomas | NO ENCONTRADO EN EL PDF | — |
| 135 | Escaner de los 5 pacientes con metal, declarado por separado | NO ENCONTRADO EN EL PDF | — |
| 136 | kVp o espectro de la fuente policromatica simulada | NO ENCONTRADO EN EL PDF | — |
| 137 | HU o coeficiente de atenuacion asignado al metal insertado en la simulacion | NO ENCONTRADO EN EL PDF | — |
| 138 | Material (titanio, acero) de las mascaras simuladas de [50] | NO ENCONTRADO EN EL PDF | — |
| 139 | Material del implante de cabeza femoral clinico | NO ENCONTRADO EN EL PDF | — |
| 140 | Valor numerico del umbral del body mask | NO ENCONTRADO EN EL PDF | — |
| 141 | Metricas cuantitativas del umbral sobre fantoma | NO ENCONTRADO EN EL PDF | — |
| 142 | Metricas cuantitativas del umbral sobre CT clinica o CTPelvic1K | NO ENCONTRADO EN EL PDF | — |
| 143 | Sesgo de tamano del umbral en mm (diametro, area o volumen) | NO ENCONTRADO EN EL PDF | — |
| 144 | Tornillos pelvicos o iliosacros como objeto medido | NO ENCONTRADO EN EL PDF | — |
| 145 | Blooming | NO ENCONTRADO EN EL PDF | — |
| 146 | Dependencia del resultado del umbral respecto de la reconstruccion, kernel o FOV | NO ENCONTRADO EN EL PDF | — |
| 147 | Fragmentacion atribuida al umbral | NO ENCONTRADO EN EL PDF | — |
| 148 | Segmentacion 3D o volumetrica | NO ENCONTRADO EN EL PDF | — |
| 149 | Region de pixeles sobre la que se calculan DSC y ACC (corte completo o ROI) | NO ENCONTRADO EN EL PDF | — |
| 150 | Particion por paciente o por corte | NO ENCONTRADO EN EL PDF | — |
| 151 | Identificador del caso de CTPelvic1K usado | NO ENCONTRADO EN EL PDF | — |
| 152 | Tamano de voxel o espesor del caso de CTPelvic1K | NO ENCONTRADO EN EL PDF | — |
| 153 | Numero de cortes clinicos evaluados | NO ENCONTRADO EN EL PDF | — |
| 154 | Acuerdo o metrica de la revision del "senior physician" | NO ENCONTRADO EN EL PDF | — |
| 155 | Test estadistico entre umbral y DiffSeg (p en Tabla 2) | NO ENCONTRADO EN EL PDF | — |
| 156 | Desviacion estandar o IC de las metricas | NO ENCONTRADO EN EL PDF | — |
| 157 | Dimension a la que se refieren los "2 cm" (lado, diametro o longitud) | NO ENCONTRADO EN EL PDF | — |
| 158 | Tamano de las barras de acero del 002H9K | NO ENCONTRADO EN EL PDF | — |
| 159 | Codigo publico | NO ENCONTRADO EN EL PDF | — |
| 160 | Geometrias rigidas, plantillas o CAD como alternativa al umbral | NO ENCONTRADO EN EL PDF | — |
