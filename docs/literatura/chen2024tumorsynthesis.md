# chen2024tumorsynthesis — Towards Generalizable Tumor Synthesis (DiffTumor)

## Identidad del metodo

**CONFIRMADO: el metodo se llama DiffTumor.** El titulo del paper es "Towards
Generalizable Tumor Synthesis"; el metodo propuesto dentro de ese paper se nombra
DiffTumor.

Frases donde el paper nombra su propio metodo:

- "we introduce a novel framework, termed DiffTumor" (§1 Introduction, p. 2).
- "we have developed a three-stage tumor synthesis framework, DiffTumor" (§1, p. 2).
- "This work introduces DiffTumor for generalizable tumor synthesis" (§6 Conclusion, p. 8).
- Enlace de codigo en la portada: "Code and Visual Turing Test: https://github.com/MrGiovanni/DiffTumor" (p. 1).

Es decir: "difftumor" es la forma correcta de referirse al metodo, pero el titulo de
la publicacion no contiene esa palabra. Si la clave BibTeX se justifica por el titulo
("tumorsynthesis"), ambas cosas son consistentes: mismo trabajo, nombre de metodo
DiffTumor.

---

- **DOI / URL:** NO ENCONTRADO EN EL PDF (no aparece DOI). El PDF lleva el
  identificador de preprint "arXiv:2402.19470v2 [eess.IV] 28 Mar 2024" en el margen
  de la p. 1, y el repositorio https://github.com/MrGiovanni/DiffTumor
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/chen2024tumorsynthesis.pdf

## Que hace (3 lineas maximo)

Sintetiza tumores abdominales tempranos en CT con un pipeline de tres etapas
(autoencoder 3D VQGAN, modelo de difusion latente condicionado por mascara de tumor
y region sana, y modelo de segmentacion entrenado con los datos sinteticos).
Los tumores sinteticos se inyectan en volumenes de organos sanos para aumentar el
entrenamiento de deteccion y segmentacion.
Sostiene que el modelo de difusion entrenado en un solo organo generaliza a otros
organos y a otras demografias de pacientes.

## Restriccion o supuesto clave

El supuesto que rompe para un implante metalico rigido es doble y esta explicito.

1. **Todo lo que hay fuera de la mascara se conserva sin modificar.** El modelo se
   condiciona en la region sana y declara: "we do not intend to model organ textures
   outside of the tumors" (§3.2, p. 4), con el condicionamiento formal
   "conditioned on both the tumor mask m and the healthy region" (§3.2, p. 4) donde
   la region sana se define como el complemento de la mascara. Un implante metalico
   produce streaking y beam hardening lejos del metal; ese efecto no local es
   estructuralmente imposible bajo este condicionamiento.
2. **Rango HU acotado a tejido blando.** El preprocesamiento trunca la intensidad:
   "the intensity in each scan is truncated to the range [−175, 250]" (Apendice E.2,
   p. 21). Un implante de acero o titanio esta muy por encima de ese techo, de modo
   que el autoencoder y el modelo de difusion nunca ven ese rango.
3. **Tejido deformable y textura suave.** La observacion fundacional del paper es que
   los tumores tempranos tienen "minimal deformation and exhibit relatively simple and
   uniform textures in CT volumes" (§1, p. 2), y sus casos de fallo se juzgan por la
   ausencia de efecto de masa: "Larger tumors fail to display a mass effect,
   characterized by the displacement of normal structures" (Apendice F.2, p. 22). Un
   implante rigido no deforma tejido de la misma manera ni tiene textura continua con
   el fondo: su frontera es un salto de intensidad brusco, no un gradiente.

## Que toco de aqui

- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| +10.7% DSC (generalizacion entre organos) | "notable improvement of 10.7% in the Dice Similarity Coefficient (DSC) for kidney tumors" | §4.2, p. 6 |
| +9.1% DSC (generalizacion demografica) | "generalizable to a variety of CT volumes of varied patient demographics ... +9.1% DSC" | §1, p. 2 |
| +28.6% sensibilidad | "improves early-stage tumor detection (Figure 7; improved sensitivity up to +28.6%)" | §1, p. 2 |
| +6.9% DSC y +16.4% sensibilidad promedio (U-Net, dataset propietario) | "average improvement of 6.9% in DSC and 16.4% in sensitivity with the U-Net backbone" | §4.3, p. 6 |
| Tumores tempranos <2 cm | "early-stage tumors (<2cm) tend to have similar imaging characteristics" | §1, p. 2 |
| Rango HU de trabajo [−175, 250] | "the intensity in each scan is truncated to the range [−175, 250]" | Apendice E.2, p. 21 |
| Nada se modela fuera del tumor | "we do not intend to model organ textures outside of the tumors" | §3.2, p. 4 |
| Un solo tumor anotado basta | "DiffTumor only requires just one annotated tumor to train the Diffusion Model" | §4.4, p. 7 |
| 100 ms por tumor | "creates synthetic tumors in real-time (Figure 6; 100 ms/tumor)" | §1, p. 2 |
| ~50% de sinteticos pasan por reales | "nearly 50% of synthetic samples are still incorrectly identified as real tumors" | §4.1, p. 6 |

## Donde entra en mi tesis

- **Objetivo 5 (evaluacion downstream).** Precedente cuantitativo directo: sintetizar
  estructuras anomalas y entrenar con ellas mejora Dice en segmentacion. Las cifras
  citables son +10.7% DSC entre organos, +9.1% DSC entre demografias y +6.9% DSC
  promedio con U-Net. Ojo: el paper reporta DSC y NSD, no HD95.
- **Justificacion de la banda extendida B_delta.** Este paper es el ejemplo canonico
  del regimen contrario: sintesis totalmente contenida en la mascara. Sirve para
  argumentar que un metodo tipo DiffTumor, aplicado tal cual a implantes, no podria
  generar streaking fuera del metal.
- **Justificacion del rango multi-ventana en HU.** El truncado a [−175, 250] muestra
  que los pipelines de sintesis de lesiones asumen ventana de tejido blando; la tesis
  necesita codificacion multi-ventana precisamente porque el metal excede ese rango.
- **Protocolo de validacion de realismo.** El Visual Turing Test con cuatro radiologos
  es un molde reusable para validar el realismo de los implantes sinteticos.

## Dudas para el asesor

1. Las mejoras de DSC de DiffTumor se miden sobre la lesion sintetizada (tumor). En
   MetalSynth-Pelvis la metrica objetivo es la segmentacion **osea peri-implante**,
   no la del implante. El precedente sigue siendo valido como argumento, pero no es
   la misma cantidad. Se cita como analogia o se acota explicitamente?
2. El paper no reporta HD95. Si se quiere un precedente cuantitativo de distancia de
   superficie, lo mas cercano aqui es NSD. Se acepta NSD como precedente indirecto o
   se busca otra fuente para HD95?
3. DiffTumor entrena el autoencoder en 9.262 volumenes CT sin etiquetar. Ese orden de
   magnitud no esta disponible para pelvis con implantes. Cuanto de la mejora
   reportada depende de esa escala de preentrenamiento?

## Evidencia textual

| Dato / umbral / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Nombre del metodo | "we introduce a novel framework, termed DiffTumor" | §1, p. 2 |
| Nombre del metodo (conclusion) | "This work introduces DiffTumor for generalizable tumor synthesis" | §6, p. 8 |
| Definicion de tumor temprano | "early-stage tumors (<2cm) tend to have similar imaging characteristics in computed tomography (CT)" | §1, p. 2 |
| Criterio de estadificacion del umbral 2 cm | "primary malignant tumor with a diameter less than 2 cm" | Nota al pie 2, p. 2 |
| Costo de anotacion motivante | "could demand up to 25 human years for annotating just one tumor type" | §1, p. 1 |
| Reduccion de complejidad del problema | "simplifying the complexity from N × M to 1 × M" | §1, p. 1 |
| Textura y deformacion de tumores tempranos | "minimal deformation and exhibit relatively simple and uniform textures in CT volumes" | §1, p. 2 |
| Claim de generalizacion 1 (organos) | "generalizable to a range of organs even when the diffusion model was trained on a limited number of tumor examples" | §1, p. 2 |
| Cifra asociada al claim 1 | "(§4.2; +10.7% DSC)" | §1, p. 2 |
| Claim de generalizacion 2 (demografias) | "generalizable to a variety of CT volumes of varied patient demographics, imaging protocols, and healthcare facilities" | §1, p. 2 |
| Cifra asociada al claim 2 | "(§4.3; +9.1% DSC)" | §1, p. 2 |
| Mejora en deteccion | "improved sensitivity up to +28.6%" | §1, p. 2 |
| Velocidad de sintesis | "creates synthetic tumors in real-time (Figure 6; 100 ms/tumor)" | §1, p. 2 |
| Anotaciones necesarias | "one annotated CT volume" | §1, p. 2 |
| Reader study: numero de recortes | "We uniformly crop 360 CT images of the tumor region from three abdominal organs" | §2, p. 3 |
| Reader study: numero de radiologos | "Three expert radiologists, qualified under the Quality Standards Act, participate in the reader study" | §2, p. 3 |
| Reader study: resultado | "The nearly random probability of the precision and recall scores indicates" | §2, p. 3 |
| Radiomics: Random Forest | "Random Forest achieves a precision of 50.3 and a recall of 54.9" | §2, p. 3 |
| Radiomics: AdaBoost | "AdaBoost achieves a precision of 35.4 and a recall of 49.5" | §2, p. 3 |
| Deep features: ResNet | "ResNet achieves a precision of 59.7 and a recall of 55.6" | §2, p. 3 |
| Deep features: DenseNet | "DenseNet achieves a precision of 44.3 and a recall of 61.1" | §2, p. 3 |
| Conclusion de la seccion 2 | "none of the classifiers can distinguish early tumors correctly among the three organs" | §2, p. 4 |
| Numero de features Radiomics | "a 91-dimensional vector can be obtained" | Apendice B, p. 15 |
| Arquitectura base del autoencoder | "we adapt the Vector Quantized Generative Adversarial Networks (VQGAN) architecture, replacing 2D convolutions with their 3D counterparts" | §3.1, p. 4 |
| Volumenes para entrenar el autoencoder | "image reconstruction performed on 9,262 unlabeled three-dimensional CT volumes" | §3.1 / Fig. 3, pp. 4-5 |
| Origen de esos volumenes | "9262 CT scans from the AbdomenAtlas-8K dataset and a private dataset" | Apendice E.2, p. 21 |
| **Supuesto clave: nada fuera del tumor** | "we do not intend to model organ textures outside of the tumors" | §3.2, p. 4 |
| **Condicionamiento del modelo generativo** | "conditioned on a tumor mask that indicates the shape and location of tumors" | §3.2, p. 4 |
| Condicionamiento formal | "conditioned on both the tumor mask m and the healthy region" | §3.2, p. 4 |
| Definicion de region sana | "z0^healthy := (1 − m) ⊙ z0" | §3.2, p. 4 |
| Generacion de mascaras (control geometrico) | "generate realistic tumor-like shapes using ellipsoids and refine them with expert radiologist feedback" | §3.3, p. 5 |
| Grados de libertad ofrecidos | "varying in location, size, shape, texture, and intensity" | §1, p. 2 |
| Repositorio de volumenes sanos | "1,246 volumes with healthy livers, 1,901 with healthy pancreas, and 1,005 with healthy kidneys" | §3.3, p. 5 |
| Datasets de tumores reales | "LiTS [6], MSD-Pancreas [2], and KiTS [33] were used for training and testing" | §4, p. 5 |
| Protocolo de validacion cruzada | "5-fold cross-validation on 118 tumor CT volumes for LiTS and 120 tumor CT volumes" | §4, p. 5 |
| Visual Turing Test: tamano | "Visual Turing Test on 240 CT volumes for three organs" | §4.1, p. 5 |
| Visual Turing Test: composicion | "120 volumes are with real tumors and the remaining 120 volumes are with synthesized tumors" | §4.1, p. 5 |
| Visual Turing Test: lectores | "Four radiologists, with varying levels of experience ranging from junior to senior and professional" | §4.1, p. 5 |
| Visual Turing Test: esfuerzo | "The total Visual Turing Test took 144 hours (2,880 CTs)" | §4.1, p. 5 |
| Visual Turing Test: modo de lectura | "each sample is inspected in a 3D view to be classified as either real or synthetic" | §4.1, p. 5 |
| Sensibilidad de los lectores | "All radiologists are able to identify real tumors with a high sensitivity score (above 90%)" | §4.1, p. 5 |
| Especificidad baja (R1, R3) | "the low specificity scores (below 40%) on the three types of tumors" | §4.1, p. 5 |
| Especificidad de lectores expertos | "the specificity scores are higher than those of R1 and R3, approximating 50%" | §4.1, p. 6 |
| Interpretacion del Turing Test | "nearly 50% of synthetic samples are still incorrectly identified as real tumors" | §4.1, p. 6 |
| Criterio explicito de lectura de la Tabla 1 | "A lower specificity score indicates a higher number of synthetic tumors being identified as real" | Tabla 1, p. 6 |
| Turing Test hígado (R1/R2/R3/R4 especificidad %) | Tabla 1: 31.7 / 22.5 / 39.2 / 45.8 | Tabla 1, p. 6 |
| Turing Test pancreas (especificidad %) | Tabla 1: 22.5 / 44.2 / 34.2 / 38.8 | Tabla 1, p. 6 |
| Turing Test riñon (especificidad %) | Tabla 1: 36.7 / 55.0 / 40.8 / 51.7 | Tabla 1, p. 6 |
| Mejora principal citable en DSC | "notable improvement of 10.7% in the Dice Similarity Coefficient (DSC) for kidney tumors" | §4.2, p. 6 |
| Efecto secundario reportado | "a decrease in the standard deviations of the DSC scores suggests that Segmentation Models become more stable" | §4.2, p. 6 |
| DSC U-Net higado (real → DiffTumor) | Tabla 2: "62.3±28.3" → "70.9±21.1" | Tabla 2, p. 6 |
| DSC U-Net pancreas (real → DiffTumor) | Tabla 2: "56.0±24.8" → "64.8±24.5" | Tabla 2, p. 6 |
| DSC U-Net riñones (real → DiffTumor) | Tabla 2: "75.1±27.2" → "84.2±9.5" | Tabla 2, p. 6 |
| DSC nnU-Net higado / pancreas / riñones (real → DiffTumor) | Tabla 2: 64.3→73.6 ; 59.9→63.6 ; 73.8→84.5 | Tabla 2, p. 6 |
| DSC Swin UNETR higado / pancreas / riñones (real → DiffTumor) | Tabla 2: 65.1→71.4 ; 52.2→62.2 ; 80.6→85.1 | Tabla 2, p. 6 |
| DSC promedio 5-fold higado (U-Net) | Tabla 4: real 62.5 → DiffTumor 66.5 | Tabla 4, p. 17 |
| DSC promedio 5-fold higado (nnU-Net) | Tabla 4: real 62.9 → DiffTumor 68.8 | Tabla 4, p. 17 |
| DSC promedio 5-fold higado (Swin UNETR) | Tabla 4: real 61.8 → DiffTumor 67.9 | Tabla 4, p. 17 |
| DSC promedio 5-fold pancreas (U-Net) | Tabla 5: real 51.2 → DiffTumor 60.0 | Tabla 5, p. 17 |
| DSC promedio 5-fold pancreas (nnU-Net) | Tabla 5: real 53.7 → DiffTumor 61.9 | Tabla 5, p. 17 |
| DSC promedio 5-fold pancreas (Swin UNETR) | Tabla 5: real 52.9 → DiffTumor 61.0 | Tabla 5, p. 17 |
| DSC promedio 5-fold riñon (U-Net) | Tabla 6: real 72.0 → DiffTumor 79.0 | Tabla 6, p. 18 |
| DSC promedio 5-fold riñon (nnU-Net) | Tabla 6: real 76.9 → DiffTumor 82.1 | Tabla 6, p. 18 |
| DSC promedio 5-fold riñon (Swin UNETR) | Tabla 6: real 74.6 → DiffTumor 81.8 | Tabla 6, p. 18 |
| Segunda metrica usada (no HD95) | "The evaluation metrics employed include the Dice Similarity Coefficient (DSC) and the Normalized Surface Distance (NSD)" | Tabla 4, p. 17 |
| Composicion del entrenamiento (higado) | "DiffTumor denotes Segmentation Model trained on 95 CT scans containing real tumors and 116 healthy CT scans" | Tabla 4, p. 17 |
| Mejora demografica (U-Net) | "average improvement of 6.9% in DSC and 16.4% in sensitivity with the U-Net backbone" | §4.3, p. 6 |
| Subgrupo etario de mayor mejora | "improvement for people aged 50–60 is significant, with an enhancement of 18.9% in sensitivity and 9.1% in DSC" | §4.4, p. 7 |
| Sensibilidad promedio demografica (U-Net) | Fig. 4: DiffTumor 72.6% vs real tumors 56.2% | Fig. 4, p. 7 |
| DSC promedio demografica (U-Net) | Fig. 4: DiffTumor 35.4% vs real tumors 28.5% | Fig. 4, p. 7 |
| Anotaciones minimas necesarias | "DiffTumor only requires just one annotated tumor to train the Diffusion Model" | §4.4, p. 7 |
| Hallazgo contraintuitivo | "extensive annotations are not necessary for tumor synthesis, contrary to the experience in computer vision" | Fig. 5, p. 7 |
| Sensibilidad vs. numero de anotaciones (1/3/5/10/20/40/80) | Fig. 5: 68.8 / 63.2 / 75.2 / 68.8 / 66.4 / 67.2 / 62.4 | Fig. 5, p. 7 |
| Colapso con T = 1 | "when T = 1, the model collapses and fails to synthesize realistic textures" | §4.4, p. 7 |
| Timestep elegido | "we opt for a timestep of T = 4 for early tumor synthesis" | §4.4, p. 7 |
| Tiempo por tumor con T = 4 | "a timestep of 4, generating a tumor in 0.2 seconds, provides the most favorable results" | Fig. 6, p. 8 |
| Sensibilidad vs timestep (2/4/10/20/50/100/200) | Fig. 6: 73.6 / 81.6 / 72 / 69.6 / 72.8 / 77.6 / 69.6 | Fig. 6, p. 8 |
| Tiempos por timestep | Fig. 6: T=1 (0.05s), T=4 (0.20s), T=200 (7.37s) | Fig. 6, p. 8 |
| Casos que mejora la sintesis | "tumors characterized by blurry boundaries, small sizes, and peripheral organ locations" | Fig. 7, p. 8 |
| Limitacion de metodos previos (gap declarado) | "these methods need to be redesigned for tumors in other organs, which severely limits the generalization capabilities" | §5, p. 8 |
| Preprocesamiento: espaciado | "resulting in a uniform voxel size of 1.0 × 1.0 × 1.0 mm³" | Apendice E.2, p. 21 |
| **Preprocesamiento: rango HU** | "the intensity in each scan is truncated to the range [−175, 250]" | Apendice E.2, p. 21 |
| Tamaño de parche | "we crop random fixed-sized 96 × 96 × 96 regions" | Apendice E.2, p. 21 |
| Codebook | "We set the codebook size and dimensionality at 16384 and 8, respectively" | Apendice E.2, p. 21 |
| Compresion latente | "reducing the original input volume's size by 1/4 in height, width, and depth" | Apendice E.2, p. 21 |
| Costo de entrenamiento autoencoder | "over a week on a node with four A100 GPUs, completing 200k iterations" | Apendice E.2, p. 21 |
| Costo de entrenamiento difusion | "over the course of a day on a node with an A100 GPU for 60k iterations" | Apendice E.2, p. 21 |
| Epocas de entrenamiento | "trained for 3,000 epochs and models on synthetic and real tumors are trained for 2,000 epochs" | Apendice E.2, pp. 21-22 |
| Inferencia sliding window | "we use the sliding window strategy by setting the overlapping area ratio to 0.75" | Apendice E.2, p. 22 |
| Comparacion con Hu et al. (higado, DSC) | Tabla 7: real 62.3 ; Hu et al. 69.7 ; DiffTumor 70.9 | Tabla 7, p. 22 |
| Comparacion con Hu et al. (pancreas, DSC) | Tabla 7: real 56.0 ; Hu et al. 55.9 ; DiffTumor 64.8 | Tabla 7, p. 22 |
| Comparacion con Hu et al. (riñon, DSC) | Tabla 7: real 75.1 ; Hu et al. 80.8 ; DiffTumor 84.2 | Tabla 7, p. 22 |
| Critica al metodo basado en modelo | "requires significant effort and expertise to identify the proper imaging characteristics of tumors" | Apendice F.1, p. 22 |
| **Tasa de generacion no realista** | "about 50% of the tumors are identified as inauthentic by the more experienced radiologist" | Apendice F.2, p. 22 |
| Modos de fallo declarados | "shape, attenuation and noise distribution" | Apendice F.2, p. 22 |
| Fallo: ausencia de efecto de masa | "Larger tumors fail to display a mass effect, characterized by the displacement of normal structures" | Apendice F.2, p. 22 |
| Fallo: ruido inconsistente con el fondo | "the noise distribution in some synthetic tumors does not match that in the CT background" | Apendice F.2, p. 22 |
| Fallo: borde demasiado nitido | "an edge that is too sharp for a malignant tumor" | Fig. 15(a), p. 23 |
| Fallo: sin deformacion del entorno | "the healthy surrounding renal structure shows no deformation due to the tumor's inherent volume" | Fig. 15(c), p. 23 |
| Fallo: vasos sin desplazamiento | "This tumor shows no mass effect, leaving the vessels without displacement or infiltration" | Fig. 15(f), p. 23 |
| DOI | NO ENCONTRADO EN EL PDF | — |
| HD95 / Hausdorff | NO ENCONTRADO EN EL PDF (usa DSC y NSD) | — |
| Datos de pelvis, hueso o implantes metalicos | NO ENCONTRADO EN EL PDF | — |
| Modelado de efectos fuera de la mascara | NO ENCONTRADO EN EL PDF (declara explicitamente que no lo hace) | — |

## Verificacion de nivel

**1. Cuanto mejora la segmentacion aguas abajo al entrenar con lesiones sinteticas?**

Cifras titulares:
- "notable improvement of 10.7% in the Dice Similarity Coefficient (DSC) for kidney
  tumors when using nnU-Net backbone" (§4.2, p. 6).
- "(§4.3; +9.1% DSC)" para generalizacion demografica (§1, p. 2).
- "average improvement of 6.9% in DSC and 16.4% in sensitivity with the U-Net
  backbone" en el dataset propietario (§4.3, p. 6).
- "improved sensitivity up to +28.6%" en deteccion de tumores tempranos (§1, p. 2).

Cifras por tabla (todas DSC %, real → DiffTumor):
- Tabla 2 (p. 6), U-Net: higado 62.3±28.3 → 70.9±21.1; pancreas 56.0±24.8 →
  64.8±24.5; riñones 75.1±27.2 → 84.2±9.5.
- Tabla 4 (p. 17), promedio 5-fold higado: U-Net 62.5 → 66.5; nnU-Net 62.9 → 68.8;
  Swin UNETR 61.8 → 67.9.
- Tabla 5 (p. 17), promedio 5-fold pancreas: U-Net 51.2 → 60.0; nnU-Net 53.7 → 61.9;
  Swin UNETR 52.9 → 61.0.
- Tabla 6 (p. 18), promedio 5-fold riñon: U-Net 72.0 → 79.0; nnU-Net 76.9 → 82.1;
  Swin UNETR 74.6 → 81.8.

Nota de precision para la tesis: las cifras de la Tabla 2 corresponden a fold0 (los
mismos valores reaparecen como fold0 en las Tablas 4-6). Los promedios 5-fold son mas
conservadores y son los que conviene citar. **Advertencia:** la metrica secundaria es
NSD, no HD95: "the Dice Similarity Coefficient (DSC) and the Normalized Surface
Distance (NSD)" (Tabla 4, p. 17). Para HD95: NO ENCONTRADO EN EL PDF.

**2. Que afirma exactamente sobre generalizacion?**

Dos afirmaciones centrales, ambas en §1 (p. 2):
- "DiffTumor can create visually realistic tumors generalizable to a range of organs
  even when the diffusion model was trained on a limited number of tumor examples from
  a specific organ".
- "DiffTumor can develop an AI model to detect and segment real tumors generalizable
  to a variety of CT volumes of varied patient demographics, imaging protocols, and
  healthcare facilities".

La base empirica de la generalizacion entre organos es la observacion de que los
tumores tempranos comparten apariencia: "none of the classifiers can distinguish early
tumors correctly among the three organs" (§2, p. 4). Esa premisa es de tejido blando
parenquimatoso y no se transfiere a hueso ni a metal.

**3. Como condiciona la sintesis?**

Solo por **mascara binaria 3D**, no por texto:
- "our diffusion model is conditioned on a tumor mask that indicates the shape and
  location of tumors in the latent feature and the healthy region of CT volumes"
  (§3.2, p. 4).
- Formalmente: "conditioned on both the tumor mask m and the healthy region"
  (§3.2, p. 4), con la region sana definida como el complemento de la mascara.

Control geometrico ofrecido al usuario: la mascara se genera por un procedimiento
parametrico previo, no aprendido: "we generate realistic tumor-like shapes using
ellipsoids and refine them with expert radiologist feedback for clinical plausibility"
(§3.3, p. 5). Los grados de libertad declarados son "varying in location, size, shape,
texture, and intensity" (§1, p. 2). No hay condicionamiento textual ni prompts
semanticos: NO ENCONTRADO EN EL PDF ninguna mencion de condicionamiento por texto.

Implicancia para MetalSynth-Pelvis: es control de forma libre por mascara arbitraria,
sin restriccion anatomica interna. El paper delega la plausibilidad anatomica a la
generacion externa de elipsoides mas revision radiologica; no hay un muestreador
guiado por densidad osea ni por contencion cortical como el que propone la tesis.

**4. Que supuesto NO se cumpliria para un implante metalico rigido?**

Tres supuestos rotos, todos con evidencia:

(a) **Rango HU acotado a tejido blando.** "the intensity in each scan is truncated to
the range [−175, 250]" (Apendice E.2, p. 21). El metal esta muy por encima de 250 HU;
el autoencoder VQGAN nunca vio ese rango y su codebook (16384 entradas, dim 8) no
tiene con que representarlo.

(b) **Continuidad de intensidades y textura suave.** La observacion fundacional exige
lesiones con "minimal deformation and exhibit relatively simple and uniform textures"
(§1, p. 2), y los casos de fallo se penalizan por bordes bruscos: "an edge that is too
sharp for a malignant tumor" (Fig. 15(a), p. 23). Para un implante, el borde brusco es
precisamente lo correcto: el criterio de realismo del paper esta invertido respecto al
del metal.

(c) **Deformabilidad del tejido como mecanismo de interaccion.** El unico efecto
"exterior" que el paper reconoce como deseable es el efecto de masa mecanico:
"Larger tumors fail to display a mass effect, characterized by the displacement of
normal structures" (Apendice F.2, p. 22). Un implante metalico no interactua por
desplazamiento sino por fisica de adquisicion (endurecimiento del haz, dispersion,
fotones starvation). El paper no tiene ningun mecanismo para eso.

**5. Produce efectos FUERA de la mascara?**

**No. Todo queda contenido dentro de la mascara, y el paper lo dice explicitamente.**

Cita literal (§3.2, p. 4): "we focus only on tumor synthesis, and we do not intend to
model organ textures outside of the tumors, which can be easily obtained from healthy
CT volumes."

El condicionamiento refuerza esto: el modelo recibe la region sana como condicion fija,
"conditioned on both the tumor mask m and the healthy region" (§3.2, p. 4), donde la
region sana es el complemento de la mascara. La sintesis reconstruye solo lo que esta
dentro de m; el resto se preserva del volumen sano de origen.

**Esto respalda directamente la banda extendida B_delta de la tesis.** DiffTumor es el
precedente canonico de que sintetizar lesiones mejora la segmentacion, pero lo logra en
un regimen donde la anomalia es local por construccion. Un implante metalico viola esa
localidad. Si la tesis usara el mismo condicionamiento, el streaking no podria
aparecer: no es una limitacion de entrenamiento, es una limitacion de la formulacion.
La banda B_delta (~12 mm) es exactamente la modificacion que rompe ese supuesto.

**6. Valida realismo con lectores humanos o solo con metricas?**

Con **ambos**, y el protocolo de lectores es explicito y reusable:
- Diseño: "Visual Turing Test on 240 CT volumes for three organs" (§4.1, p. 5), con
  "120 volumes are with real tumors and the remaining 120 volumes are with synthesized
  tumors" (§4.1, p. 5).
- Lectores: "Four radiologists, with varying levels of experience ranging from junior
  to senior and professional" (§4.1, p. 5).
- Esfuerzo: "The total Visual Turing Test took 144 hours (2,880 CTs)" (§4.1, p. 5).
- Modo de lectura: "each sample is inspected in a 3D view" (§4.1, p. 5).
- Criterio de exito declarado: "A lower specificity score indicates a higher number of
  synthetic tumors being identified as real" (Tabla 1, p. 6).

Cifras: sensibilidad de los lectores "above 90%" para reales; especificidad "below 40%"
para R1 y R3 y "approximating 50%" para R2 y R4; conclusion "nearly 50% of synthetic
samples are still incorrectly identified as real tumors" (§4.1, pp. 5-6). Tabla 1
(p. 6) da especificidades por organo y lector (higado 31.7/22.5/39.2/45.8; pancreas
22.5/44.2/34.2/38.8; riñon 36.7/55.0/40.8/51.7).

Reconocimiento de limite: "about 50% of the tumors are identified as inauthentic by the
more experienced radiologist" (Apendice F.2, p. 22). Es decir, el realismo declarado no
es total y el propio paper lo admite.

Ademas hay un segundo reader study, distinto del Turing Test, para validar la premisa
de similitud entre organos: 360 recortes, tres radiologos expertos (§2, p. 3).

**7. Nivel que sostiene la evidencia: NIVEL 2, confirmado, pero por una razon distinta
a la registrada.**

La justificacion original ("precedente que apoya, no es un riesgo") es correcta en su
conclusion pero incompleta en su razonamiento. Este paper no solo apoya: **aporta el
argumento negativo mas fuerte disponible para justificar B_delta**, porque declara
explicitamente que no modela nada fuera de la mascara. Eso lo vuelve un precedente
doble: cuantitativo (Objetivo 5) y contrastivo (justificacion de diseño del
renderizador). En una frase: **NIVEL 2 se sostiene, porque afecta la redaccion de dos
secciones (precedente downstream y motivacion de B_delta) pero no define el benchmark
ni una cifra cuyo error tumbe la tesis** — el riesgo maximo de un error aqui es citar
la cifra de fold0 (+10.7% / 70.9 DSC) creyendo que es el promedio 5-fold (66.5), lo que
es corregible y no estructural.

Observacion adicional para la autora: si en algun momento la tesis quisiera usar
DiffTumor como **baseline generativo** en lugar de solo como precedente, subiria a
Nivel 1, porque entonces el rango HU [−175, 250] y el condicionamiento sin banda
exterior dejarian de ser contexto y pasarian a ser parametros de una comparacion.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| [37] Qixin Hu, Yixiong Chen, Junfei Xiao, Shuwen Sun, Jieneng Chen, Alan L Yuille, Zongwei Zhou. Label-free liver tumor segmentation. CVPR 2023 | Metodo competidor directo (sintesis basada en modelo, no aprendida) y unico baseline generativo de la Tabla 7. Sintesis por operaciones de imagen explicitas (elipsoides, deformacion elastica, ruido sal, filtrado gaussiano, escalado, recorte) — mas cercano en espiritu a una sintesis fisica de implantes que el propio DiffTumor. Fuente de las cifras Hu et al. de Tablas 2, 3 y 7 |
| [67] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Bjorn Ommer. High-resolution image synthesis with latent diffusion models. CVPR 2022 | Base del difusor latente que la tesis tambien usa. Ya esta en papers/ como rombach2022latentdiffusion |
| [22] Patrick Esser, Robin Rombach, Bjorn Ommer. Taming transformers for high-resolution image synthesis. CVPR 2021 | Arquitectura VQGAN que DiffTumor adapta a 3D; relevante si la tesis necesita un autoencoder 3D con rango HU extendido |
| [64] Chongyu Qu et al. Abdomenatlas-8k: Annotating 8,000 abdominal ct volumes for multi-organ segmentation in three weeks. NeurIPS 2023 | Fuente de los 9.262 volumenes de preentrenamiento; da el orden de magnitud de datos sanos que este tipo de pipeline asume disponible |
| [39] Fabian Isensee et al. nnu-net: a self-configuring method for deep learning-based biomedical image segmentation. Nature Methods 2021 | Backbone de segmentacion downstream; candidato para el Objetivo 5 de la tesis |
| [32] Ali Hatamizadeh et al. Swin unetr: Swin transformers for semantic segmentation of brain tumors in mri images. MICCAI Brainlesion 2021 | Tercer backbone downstream usado; util para argumentar que la mejora no depende de la arquitectura |
| [76] Joost JM Van Griethuysen et al. Computational radiomics system to decode the radiographic phenotype. Cancer research 2017 | Metrica/herramienta (pyradiomics, 91 features) que podria validar realismo de estructuras sinteticas de forma cuantitativa, alternativa a los lectores humanos |
| [16] Linda C Chu et al. Utility of ct radiomics features in differentiation of pancreatic ductal adenocarcinoma from normal pancreatic tissue. AJR 2019 | Precedente de uso de radiomics como criterio discriminativo entre tejido real y no real |
| [80] Zihan Wei et al. Pancreatic image augmentation based on local region texture synthesis for tumor segmentation. ICANN 2022 | Sintesis por textura de region local: hace el gap MENOR de lo afirmado, porque es otro precedente de aumentacion por sintesis local previa a DiffTumor |
| [18] Shiyi Du, Xiaosong Wang, Yongyi Lu, Yuyin Zhou, Shaoting Zhang, Alan Yuille, Kang Li, Zongwei Zhou. Boosting dermatoscopic lesion segmentation via diffusion models with visual and textual prompts. arXiv 2023 | Sintesis de lesiones con prompts visuales Y textuales: es el control de condicionamiento que DiffTumor no tiene. Posible relacion con papers/zhang2025diffboost.pdf ya en el repo — verificar si es el mismo trabajo |
| [86] Jie Yang et al. Class-aware adversarial lung nodule synthesis in ct images. ISBI 2019 | Sintesis de nodulos en CT; otro precedente de aumentacion por lesiones sinteticas que reduce la novedad reclamada |
| [41] Qiangguo Jin et al. Free-form tumor synthesis in computed tomography images via richer generative adversarial network. Knowledge-Based Systems 2021 | Sintesis de forma libre en CT; competidor conceptual del renderizador |
| [56] Fei Lyu et al. Pseudo-label guided image synthesis for semi-supervised covid-19 pneumonia infection segmentation. IEEE TMI 2022 | Sintesis de lesiones no tumorales en CT torax con ganancia downstream; precedente adicional del Objetivo 5 |
| [57] Fei Lyu et al. Learning from synthetic ct images via test-time training for liver tumor segmentation. IEEE TMI 2022 | Aborda la brecha sintetico-real en tiempo de test; relevante si la aumentacion de la tesis introduce domain shift |
| [6] Patrick Bilic et al. The liver tumor segmentation benchmark (lits). arXiv 2019 | Fuente original del dataset y de las cifras de DSC de higado |
| [2] Michela Antonelli et al. The medical segmentation decathlon. arXiv 2021 | Fuente original de MSD-Pancreas y de las cifras de pancreas |
| [33] Nicholas Heller et al. An international challenge to use artificial intelligence to define the state-of-the-art in kidney and kidney tumor segmentation. 2021 | Fuente original de KiTS y de las cifras de riñon (incluida la de +10.7% DSC) |
| [11] Richard J Chen, Ming Y Lu, Tiffany Y Chen, Drew FK Williamson, Faisal Mahmood. Synthetic data in machine learning for medicine and healthcare. Nature Biomedical Engineering 2021 | Referencia general citable para el argumento de que los datos sinteticos son validos en medicina |
| [26] Cong Gao et al. Synthetic data accelerates the development of generalizable learning-based algorithms for x-ray image analysis. Nature Machine Intelligence 2023 | Precedente de datos sinteticos en imagen por rayos X con simulacion fisica; el mas cercano al baseline XCIST/CatSim de la tesis |
| [38] Qixin Hu, Alan Yuille, Zongwei Zhou. Synthetic data as validation. arXiv 2023 | Propone usar datos sinteticos como conjunto de validacion, no solo de entrenamiento; podria afectar el diseño del Objetivo 5 |

