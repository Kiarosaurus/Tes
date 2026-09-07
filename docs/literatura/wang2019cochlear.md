# wang2019cochlear — MAR con GAN 3D en CT post-operatoria de implante coclear

- **DOI / URL:** NO ENCONTRADO EN EL PDF (DOI). HAL Id: hal-02196557 — https://hal.inria.fr/hal-02196557. Publicado en MICCAI 2019, pp. 121-129.
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wang2019cochlear.pdf

## Que hace (3 lineas maximo)
Propone MARGANs, una GAN 3D no supervisada que reduce artefactos metalicos en CT post-operatoria de implante coclear.
Para entrenar sin pares reales, **simula fisicamente** el arreglo de electrodos y su beam hardening sobre 1090 CT pre-operatorias "libres de artefacto".
Compara contra dos metodos MAR 2D clasicos (marLI, marBHC) con PSNR, RMSE y SSIM sobre 10 casos clinicos.

## Restriccion o supuesto clave
No es un modelo generativo de sintesis de apariencia: la insercion de metal es un **paso analitico determinista**, no aprendido. El implante se reduce a una mascara tubular binaria colocada por umbralizacion de un mapa de distancia, con un unico valor de HU fijo: "The Hounsfield unit of simulated electrode array was then set to 3071HU" (Sec. 2.1). Es decir, la geometria del implante no proviene de un banco de CAD ni admite pose libre; queda amarrada a la anatomia segmentada (centro de la scala tympani). Ademas los autores reconocen que la fisica es incompleta: el trabajo futuro pasa por "including more physically realistic metal artifacts in the simulation such as noisy detectors and exponential edge-gradient effects" (Sec. 4).

## Que toco de aqui
- [x] metodo que reimplemento (parcial: el pipeline de simulacion de metal como baseline analitico)
- [x] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 3071 HU para el metal simulado | "simulated electrode array was then set to 3071HU" | Sec. 2.1, p. 3 |
| 1090 volumenes pre-op → 1090 sinteticos | "applied on 1090 3D preoperative CT images to create 1090 3D images" | Introduccion, p. 2 |
| 5 energias discretizadas | "beam hardening ... discretized on 5 different energies" | Introduccion, p. 2 |
| 140 kVp, anodo de tungsteno | "for a tungsten anode tube at 140 kV p" | Sec. 2.1, p. 4 |
| 10 imagenes de evaluacion clinica | "evaluation dataset includes 10 temporal bones images" | Sec. 3.1, p. 6 |
| 597 pacientes, 493 izq / 597 der | "include 493 left and 597 right images collected from 597 patients" | Sec. 3.1, p. 5 |
| Voxel 0.2 x 0.2 x 0.2 mm3 | "Imaging voxel size is 0.2 x 0.2 x 0.2 mm3" | Sec. 3.1, p. 6 |
| Volumenes recortados 60 x 50 x 50 | "then cropped as 60 x 50 x 50 volume images" | Sec. 3.1, p. 6 |
| ~1 h CPU de simulacion por imagen | "took about 1 hour on a CPU cluster for each of the 1090 images" | Sec. 3.2, p. 6 |
| 23 h de entrenamiento en 1080Ti | "Training the MARGANs took about 23 hours on one NVIDIA 1080Ti GPU" | Sec. 3.2, p. 6 |
| Trabajo previo con solo 76 pares reales | "trained on 76 pairs of registered pre and post-operative images" | Introduccion, p. 2 |

## Donde entra en mi tesis
- **Antecedentes / gap del renderizador:** es un precedente explicito de *insercion sintetica de metal* en CT para generar pares de entrenamiento. Obliga a reformular el gap: lo nuevo de MetalSynth-Pelvis no es "insertar metal sinteticamente" sino hacerlo (a) con un banco de geometrias reales de osteosintesis y pose 3D muestreada, (b) con un renderizador aprendido (LDM+ControlNet) en vez de proyeccion analitica, y (c) evaluado en tarea aguas abajo de segmentacion osea.
- **Baseline fisico:** su simulacion Beer-Lambert multi-energia sobre proyecciones fan-beam es conceptualmente el mismo lugar que ocupa XCIST/CatSim en mi diseno; sirve para argumentar por que no basta el baseline analitico.
- **Argumento de la banda extendida B_delta:** el paper confirma que el artefacto se manifiesta fuera del metal (streaking, beam hardening), aunque no define ningun radio ni banda.

## Dudas para el asesor
- Si un pipeline analitico de insercion ya existia desde 2019, cual es el criterio para sostener que el aporte del renderizador aprendido es sustantivo y no solo cosmetico? Basta con la evaluacion aguas abajo en segmentacion?
- Vale la pena replicar su simulacion (Beer-Lambert, 5 energias, fan-beam) como ablacion "analitico vs aprendido", o eso ya lo cubre XCIST/CatSim?

## Evidencia textual
| Item | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| Direccion del metodo: remocion | "we propose a 3D metal artifact reduction method using convolutional neural networks" | Abstract, p. 1 |
| Simulacion de artefactos sobre imagenes pre-op | "pre-operative 'artifact-free' images on which simulated metal artifacts are created" | Abstract, p. 1 |
| Insercion virtual de electrodos (clave) | "the virtual insertion of electrode arrays and the simulation of beam hardening" | Abstract, p. 1 |
| Ley fisica usada | "simulation of beam hardening based on the Beer-Lambert law" | Abstract, p. 1 |
| Rechazo de pares reales pre/post | "Instead of training the GANs on pairs of pre and postoperative images" | Introduccion, p. 2 |
| Base del entrenamiento | "our approach relies on the physical simulation of artifacts in CT images from pre-operative CT images" | Introduccion, p. 2 |
| Tres pasos de la simulacion | "automatic segmentation of the scala tympani ... estimation of the positions of the electrode arrays" | Introduccion, p. 2 |
| Discretizacion energetica | "Beer-Lambert law discretized on 5 different energies" | Introduccion, p. 2 |
| Escala del dataset sintetico | "applied on 1090 3D preoperative CT images to create 1090 3D images with simulated artifacts" | Introduccion, p. 2 |
| Nombre del modelo y perdida | "3D generative adversarial network (GANs) named MARGANs ... generative loss derived from Retinex theory" | Introduccion, p. 2 |
| Caracter no supervisado | "our method is unsupervised and does not require any registration of pre and post operative images" | Introduccion, p. 2-3 |
| Registro rigido a referencia | "automatically rigidly registered on a reference cochlea CT image where the modiolus axis is along Z" | Sec. 2.1, p. 3 |
| Modelo de forma para segmentar | "segmentation of the cochlea is then performed through a parametric cochlea shape model" | Sec. 2.1, p. 3 |
| Mapa de distancia con signo | "a signed distance map of the ST is generated (Step 2)" | Sec. 2.1, p. 3 |
| Colocacion del implante por umbral | "estimated by thresholding the distance map to create a 3D tubular binary mask near the center" | Sec. 2.1, p. 3 |
| Valor HU del metal y su justificacion | "set to 3071HU (Step 4), which is the maximum observed value on CI metal artifacts" | Sec. 2.1, p. 3 |
| Numero de pasos del pipeline | "ending with the simulated post-operative image after 9 processing steps" | Fig. 2, p. 3 |
| Ecuacion de formacion (policromatica) | "the energy spectrum phi(E_v) must be taken into account" | Sec. 2.1, p. 4 |
| Espectro obtenido de fabricante | "energy spectrum was downloaded from a CT manufacturer dedicated site" | Sec. 2.1, p. 4 |
| Tension del tubo | "for a tungsten anode tube at 140 kV p" | Sec. 2.1, p. 4 |
| Mapas de atenuacion | "computing attenuation maps mu(x,y,z,E_v) (Step 5) for five sample energies" | Sec. 2.1, p. 4 |
| Base de conversion HU→mu | "based on the Hounsfield unit formula and the water absorption coefficients as a function of energy" | Sec. 2.1, p. 4 |
| Proyeccion | "perform fan-beam projection (Step 7) of the 5 attenuation maps to produce sinograms-like images" | Sec. 2.1, p. 4 |
| Suma ponderada con dispersion | "weighted sum of the 5 sinograms (Step 8) ... (including energy spectrum and scatter)" | Sec. 2.1, p. 4 |
| Reconstruccion final | "inverse fan beam projection produces the output image with metallic artifacts (Step 9)" | Sec. 2.1, p. 4 |
| Naturaleza del problema MAR | "removing metal artifact from images is clearly an ill-posed problem" | Sec. 2.2, p. 4 |
| Arquitectura del generador | "similar to U-Net with convolution and deconvolution layers, and batch normalization layers" | Sec. 2.2, p. 4 |
| Entrada volumetrica completa | "the input of the network consist of full 3D images as it easily fits in GPU memory" | Sec. 2.2, p. 4 |
| Discriminador | "eight groups of convolution layers and batch normalization layers combined sequentially" | Sec. 2.2, p. 5 |
| Perdida de contenido | "mean square error (MSE) ... encourage the generator to generate voxels consistent with the artifact free images" | Sec. 2.2, p. 5 |
| Motivo de la perdida Retinex | "using only the MSE loss leads to blurred MAR images with a lack of high frequency image details" | Sec. 2.2, p. 5 |
| Escaner y protocolo | "collected from 597 patients by a GE LightSpeed CT scanner with a standard protocol" | Sec. 3.1, p. 5-6 |
| Sin filtros MAR del fabricante | "(without metal artifact reduction filters) at the Radiology Department of the Nice University Hospital" | Sec. 3.1, p. 6 |
| Resolucion | "Imaging voxel size is 0.2 x 0.2 x 0.2 mm3" | Sec. 3.1, p. 6 |
| Recorte del ROI | "cropped as 60 x 50 x 50 volume images" | Sec. 3.1, p. 6 |
| Dataset de evaluacion | "evaluation dataset includes 10 temporal bones images outside the simulation dataset" | Sec. 3.1, p. 6 |
| Fallo del registro automatico | "all tested rigid registration algorithms fail to register the pre-operative with post-operative images" | Sec. 3.1, p. 6 |
| Registro manual con landmarks | "they were manually registered in 3D using landmarks" | Sec. 3.1, p. 6 |
| Framework | "The proposed GANs were implemented with TensorFlow" | Sec. 3.2, p. 6 |
| Kernel de convolucion | "Convolution kernel size is set to 3 x 3 x 3" | Sec. 3.2, p. 6 |
| Numero de filtros | "the number of filters was N_f = 512" | Sec. 3.2, p. 6 |
| Peso de la perdida Retinex | "the weight of Retinex loss was set as alpha = 0.00002 experimentally" | Sec. 3.2, p. 6 |
| Optimizador y learning rates | "RMSprop optimizer with learning rate l_rg = 1e-4 and l_rd = 1e-3 respectively" | Sec. 3.2, p. 6 |
| Costo de la simulacion | "took about 1 hour on a CPU cluster for each of the 1090 images" | Sec. 3.2, p. 6 |
| Costo del entrenamiento | "about 23 hours on one NVIDIA 1080Ti GPU" | Sec. 3.2, p. 6 |
| Resultado cualitativo | "metal artifacts are significantly reduced in the MARGANs generated images without important geometry distortions" | Sec. 3.3, p. 6 |
| Restauracion de estructura | "some visible internal structures inside the cochlea are restored by the MARGANs" | Sec. 3.3, p. 7 |
| Electrodos marcados a mano | "electrodes positions in yellow and red were manually added to allow for the visual assessment" | Sec. 3.3, p. 7 |
| Metodos comparados | "compared with 2 open-source 2D fast metallic artifacts reduction methods" | Sec. 3.3, p. 7-8 |
| Identidad de los baselines | "projection linear interpolation replacement (marLI) and beam hardening correction (marBHC)" | Sec. 3.3, p. 8 |
| Metricas usadas | "Root Mean Square Error (RMSE), Structural Similarity Index (SSIM) and Peak Signal to Noisy Ratio (PSNR)" | Sec. 3.3, p. 8 |
| Referencia de la metrica | "computed between the pre-operative images and the MAR images generated by those two methods and our approach" | Sec. 3.3, p. 8 |
| Que miden esas metricas | "measure the preservation of visible structures, the errors and quality of the reconstructed images" | Sec. 3.3, p. 8 |
| Resultado cuantitativo (sin cifras) | "our method outperforms those 2 MAR methods for all three metrics" | Sec. 3.3, p. 8 |
| Consistencia espacial | "MARGANs exhibits the best performances with a lower mean value and much lower variance" | Sec. 3.3, p. 8 |
| Explicacion de la ventaja | "it is the only MAR algorithm working directly on 3D images" | Sec. 3.3, p. 8 |
| Limitacion fisica reconocida | "including more physically realistic metal artifacts ... noisy detectors and exponential edge-gradient effects" | Sec. 4, p. 8 |
| Trabajo futuro supervisado | "by using supervised learning with annotated pairs of CT images" | Sec. 4, p. 8 |
| Cifras numericas de PSNR/RMSE/SSIM | Solo aparecen como graficos de barras y boxplots en Fig. 4; ningun valor numerico en el texto | NO ENCONTRADO EN EL PDF |
| Metrica de tarea aguas abajo (segmentacion / localizacion de electrodos) | No se reporta ninguna metrica cuantitativa de tarea posterior | NO ENCONTRADO EN EL PDF |
| Material / composicion del electrodo (platino, titanio, etc.) | El metal se define solo por su HU, no por su material | NO ENCONTRADO EN EL PDF |
| Diametro o longitud del arreglo tubular simulado | Sin dimensiones explicitas del tubo binario | NO ENCONTRADO EN EL PDF |
| Umbral usado sobre el mapa de distancia | "estimated by thresholding the distance map" — valor del umbral no dado | NO ENCONTRADO EN EL PDF |
| Extension espacial del artefacto (banda tipo B_delta) | No se define ninguna distancia o banda alrededor del metal | NO ENCONTRADO EN EL PDF |
| Split train/val/test del dataset de 1090 | No se describe particion | NO ENCONTRADO EN EL PDF |
| DOI del articulo | Solo HAL Id hal-02196557 y paginas 121-129 | NO ENCONTRADO EN EL PDF |
| Codigo o datos publicos de los autores | No hay enlace a repositorio propio | NO ENCONTRADO EN EL PDF |

## Verificacion de nivel

**1. Direccion: es REMOCION, confirmado.**
Si. El objetivo declarado es reducir artefactos: "we propose a 3D metal artifact reduction method using convolutional neural networks for post-operative cochlear implant imaging" (Abstract, p. 1), y la conclusion lo reitera: "we presented an unsupervised framework for generating images with reduced metal artifacts from CI postoperative images" (Sec. 4, p. 8). El producto final es la imagen sin metal.

**2. CRITICO — Como construyo los pares de entrenamiento: INSERTA Y SIMULA.**
**La degradacion de Nivel 2 a Nivel 3 es un ERROR, y hay que decirlo con todas las letras.** El paper NO usa pares reales pre/post-operatorios: deliberadamente los descarta y en su lugar **inserta virtualmente el implante en CT pre-operatorias y simula sus artefactos** para fabricar los pares. Frases literales que lo resuelven:

- "The generative model is trained on a large number of pre-operative 'artifact-free' images on which simulated metal artifacts are created." (Abstract, p. 1)
- "This simulation involves the segmentation of the scala tympani, **the virtual insertion of electrode arrays** and the simulation of beam hardening based on the Beer-Lambert law." (Abstract, p. 1)
- "Instead of training the GANs on pairs of pre and postoperative images, our approach relies on the physical simulation of artifacts in CT images from pre-operative CT images." (Introduccion, p. 2)
- "This approach was applied on 1090 3D preoperative CT images to create 1090 3D images with simulated artifacts. The 1090 image pairs are then used to train an original 3D generative adversarial network." (Introduccion, p. 2)

Es decir: **es un precedente directo de insercion sintetica de metal en CT para generar datos pareados**, exactamente la operacion que MetalSynth-Pelvis propone. La justificacion de la bajada ("remueve, no inserta") es falsa: remueve *como tarea final*, pero **para lograrlo inserta**, y la insercion es la mitad del metodo (toda la Sec. 2.1 y la Fig. 2 de 9 pasos). El argumento restante ("otra anatomia, otra escala") es cierto pero no toca el nucleo metodologico.

**3. Fisica de la simulacion: analitica, en dominio de proyecciones, NO aprendida.**
Es un forward model fisico explicito, no un modelo generativo. Cadena de 9 pasos (Fig. 2, p. 3): registro rigido a cocleas de referencia → segmentacion parametrica de la coclea → mapa de distancia con signo de la scala tympani → umbralizacion para obtener "a 3D tubular binary mask near the center of the ST" → asignacion de 3071 HU → conversion a mapas de atenuacion mu(x,y,z,E_v) "based on the Hounsfield unit formula and the water absorption coefficients as a function of energy" para 5 energias → "fan-beam projection (Step 7) of the 5 attenuation maps to produce sinograms-like images" → "weighted sum of the 5 sinograms (Step 8) ... (including energy spectrum and scatter)" → "inverse fan beam projection produces the output image with metallic artifacts (Step 9)". El espectro es de tubo de tungsteno a 140 kVp descargado de un sitio de fabricante. Base teorica: Beer-Lambert policromatica (Eq. 1, p. 4). Costo: ~1 h de CPU por volumen.
Diferencia clave con mi renderizador: aqui la apariencia sale de fisica cerrada; el aprendizaje (MARGANs) actua *despues*, en la direccion inversa.

**4. Anatomia, dataset, tamano.**
Anatomia: hueso temporal / oido interno, coclea (scala tympani y scala vestibuli), implante coclear (arreglo de electrodos). Dataset de simulacion: "493 left and 597 right images collected from 597 patients by a GE LightSpeed CT scanner" (Sec. 3.1, p. 5-6), sin filtros MAR, del Nice University Hospital; total usado 1090 volumenes. Voxel 0.2 x 0.2 x 0.2 mm3, recortados a 60 x 50 x 50. Dataset de evaluacion: 10 huesos temporales fuera del set de simulacion, con pares pre/post reales registrados manualmente con landmarks porque "all tested rigid registration algorithms fail". No es dataset publico ni hay split declarado.

**5. Tarea aguas abajo: NO. Solo calidad de imagen.**
No hay evaluacion cuantitativa de segmentacion ni de localizacion. Las metricas son PSNR, RMSE y SSIM calculadas contra la imagen pre-operatoria registrada, sobre 10 casos, mas la varianza entre cortes del paciente #4 como proxy de consistencia 3D. El resultado se enuncia sin cifras: "our method outperforms those 2 MAR methods for all three metrics" (Sec. 3.3, p. 8) y "MARGANs exhibits the best performances with a lower mean value and much lower variance" (Sec. 3.3, p. 8). Los valores numericos solo existen como barras/boxplots en Fig. 4 → **NO ENCONTRADO EN EL PDF**. La unica referencia a posicion de electrodos es cualitativa: "electrodes positions in yellow and red were manually added to allow for the visual assessment" (Sec. 3.3, p. 7).

**6. Nivel que sostiene la evidencia: NIVEL 2 (no 3).**
Es un precedente metodologico directo de insercion sintetica de metal con fisica analitica para generar pares de entrenamiento, por lo que obliga a reformular como se enuncia el gap del renderizador; no llega a Nivel 1 porque no aporta cifras de benchmark ni evalua tarea aguas abajo.

## Candidatos de snowballing detectados
| Cita como aparece | Por que podria importar |
|---|---|
| [8] Wang, J., Zhao, Y., Noble, J.H., Dawant, B.M.: "Conditional generative adversarial networks for metal artifact reduction in CT images of the ear." MICCAI 2018, pp. 3-11 | Precedente de GAN condicional para metal en CT; usa 76 pares reales pre/post registrados. Es la fuente de la cifra "76 pairs" y el contraejemplo de entrenar con pares reales en vez de sintetizarlos. |
| [11] Zhang, Y., Yu, H.: "Convolutional neural network based metal artifact reduction in X-ray computed tomography." IEEE TMI 37(6), 1370-1381 (2018) | El propio paper dice de el: "A simulation dataset was built for training the CNN" (p. 2). Otro precedente de generacion sintetica de datos con metal. |
| [1] Demarcy, T. et al.: "Automated analysis of human cochlea shape variability from segmented uCT images." Comput. Med. Imaging Graph. 59 (2017), 1-12 | Fuente del modelo parametrico de forma que hace posible colocar el implante segun la anatomia; analogo funcional a mi muestreador guiado por anatomia. |
| [4] Kalender, W.A., Hebel, R., Ebersberger, J.: "Reduction of CT artifacts caused by metallic implants." Radiology 164(2), 576-577 (1987) | Baseline clasico marLI (interpolacion lineal en proyecciones); referencia obligada si comparo contra MAR clasico. |
| [7] Verburg, J.M., Seco, J.: "CT metal artifact reduction method correcting for beam hardening and missing projections." PMB 57(9), 2803-2818 (2012) | Baseline marBHC; modelo de beam hardening que compite/complementa la fisica que quiero replicar. |
| [9] Wunderlich, A., Noo, F.: "Image covariance and lesion detectability in direct fan-beam X-ray computed tomography." PMB 53(10), 2471-2493 (2008) | Citado como fuente de la conversion HU → coeficientes de absorcion del agua por energia; es el sustento numerico del forward model. |
| [2] Gjesteby, L. et al.: "Deep Neural Network for CT Metal Artifact Reduction with a Perceptual Loss Function." CT Meeting 2018, pp. 439-443 | DestreakNet: post-procesamiento tras NMAR; compite en el espacio de metodos aprendidos para artefacto metalico. |
| [3] Huang, X. et al.: "Metal artifact reduction on cervical CT images by deep residual learning." BioMedical Engineering OnLine 17(175) (2018) | RL-ARCNN, MAR aprendido en dominio imagen en otra anatomia osea; referencia de contexto para el estado del arte de MAR con DL. |
