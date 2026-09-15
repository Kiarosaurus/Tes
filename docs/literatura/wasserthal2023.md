# wasserthal2023 — TotalSegmentator: segmentacion robusta de 104 estructuras anatomicas en CT

- **DOI / URL:** https://doi.org/10.1148/ryai.230024 (Radiology: Artificial Intelligence 2023; 5(5):e230024, p. 1)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wasserthal2023.pdf

## Que hace (3 lineas maximo)
Entrena un nnU-Net sobre 1204 CT de rutina (Hospital Universitario de Basilea) anotados de forma iterativa para segmentar 104 estructuras (27 organos, 59 huesos, 10 musculos, 8 vasos), con un modelo a 1.5 mm y otro a 3 mm isotropicos.
Lo valida con Dice y NSD globales en un test de 65 pacientes y lo compara con un nnU-Net entrenado en BTCV (13 estructuras).
Como ejemplo de uso, lo aplica a 4004 CT de politrauma para correlacionar edad con volumen y atenuacion.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. El supuesto relevante para la tesis es implicito: el PDF no menciona implantes, metal ni artefactos en ninguna seccion, asi que la robustez declarada no esta demostrada para CT con osteosintesis. Ademas, el entrenamiento excluye los casos mas deformados: *"could not segment certain structures because of high ambiguity"* (*"structures highly distorted as a result of abnormality"*, n = 40; Materials and Methods, Training dataset, p. 2). La unica evidencia sobre fracturas es cualitativa: *"robust, accurate results even when structures were distorted (broken bones)"* (Figura 5, p. 6).

El PDF describe la version de 104 estructuras. Nombra como clases oseas *"vertebrae C1-7"*, *"vertebrae T1-12"*, *"vertebrae L1-5"*, *"hip"* y *"sacrum"* (Figura 2, p. 4). No aparece S1 como clase ni los nombres `vertebrae_S1`, `hip_left` o `hip_right` que usa la tesis con TotalSegmentator 2.18.0.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna. Segun el encargo, `tesis/main.tex` solo usa esta fuente para "anatomical masks from TotalSegmentator" | --- | --- |

## Donde entra en mi tesis
Es la fuente citada del software que genera las mascaras anatomicas (no la referencia) de sacro, S1 y ambas caderas con las que se mide el corredor transsacro en CTPelvic1K, con y sin osteosintesis (Objetivo del muestreador; restriccion de contencion y corredor). No se reimplementa ni se citan cifras. La tesis usa la version 2.18.0 con la tarea `total`, que el PDF no describe.

## Dudas para el asesor
1. **Desfase de version.** El PDF valida el modelo de 104 estructuras, sin clase S1. La tesis usa 2.18.0 con `vertebrae_S1`, `hip_left` y `hip_right`. Basta esta cita para respaldar mascaras de una clase que el paper no describe ni valida, o hace falta una fuente de la version 2?
2. **Sin validacion por clase en el PDF.** Los resultados por estructura se remiten a *"Figure S1"* y a un JSON en GitHub (p. 4). No hay suplemento en `papers/`, asi que en el PDF no hay Dice de sacro, cadera ni S1.
3. **Metal.** El PDF no dice nada sobre implantes ni artefactos. Si la tesis no afirma que las mascaras son exactas cerca del metal, no hay problema. Si se necesita esa afirmacion, esta fuente no la sostiene.
4. **Inconsistencia interna del paper.** El Abstract (p. 1) situa el 0.932 vs 0.871 *"on a separate dataset"*. Resultados (p. 5) situa esas mismas cifras *"on our test set"* y da otra cifra para BTCV (0.849). Si alguna vez se cita la comparacion, tomarla de Resultados.
5. **Modelo "fast".** El PDF solo habla de un *"second model on 3-mm isotropic resolution"* (p. 2). No lo llama "fast" ni menciona un recorte grueso de 6 mm, asi que no se puede equiparar con las opciones del software sin otra fuente.

## Evidencia textual

### Respuestas a las preguntas del encargo

| # | Dato | Frase original (<15 palabras) o estado | Seccion / pagina |
|---|---|---|---|
| 1a | Modelo descrito: nnU-Net | "We used the model from the nnU-Net framework" | Materials and Methods, Model, p. 2 |
| 1b | Modelo a 1.5 mm | "One model was trained on CT scans with 1.5-mm isotropic resolution." | Materials and Methods, Model, p. 2 |
| 1c | Modelo a 3 mm (menos RAM y GPU) | "we also trained a second model on 3-mm isotropic resolution" | Materials and Methods, Model, p. 2 |
| 1d | Numero de version del software (p. ej. 2.x) | NO ENCONTRADO EN EL PDF | --- |
| 1e | Nombre de tarea `total` | NO ENCONTRADO EN EL PDF | --- |
| 1f | Modelo llamado "fast" | NO ENCONTRADO EN EL PDF | --- |
| 1g | Recorte o modelo grueso de 6 mm | NO ENCONTRADO EN EL PDF | --- |
| 2a | Sacro como clase | "sacrum" (etiqueta del panel Skeleton) | Figura 2, p. 4 |
| 2b | Cadera como clase | "hip" (etiqueta del panel Skeleton) | Figura 2, p. 4 |
| 2c | Vertebras individuales | "vertebrae C1-7", "vertebrae T1-12", "vertebrae L1-5" | Figura 2, p. 4 |
| 2d | S1 como clase (`vertebrae_S1`) | NO ENCONTRADO EN EL PDF | --- |
| 2e | Lateralidad de cadera (`hip_left`, `hip_right`) y lista completa de nombres de clase | NO ENCONTRADO EN EL PDF (se remite a "Appendix S1", ausente del PDF) | Data Annotation, p. 2 |
| 3a | Dice global, modelo 1.5 mm | "The Dice score was 0.943 (95% CI: 0.938, 0.947)" | Results, Segmentation Evaluation, p. 4 |
| 3b | NSD global, modelo 1.5 mm | "the NSD was 0.966 (95% CI: 0.962, 0.971)" | Results, Segmentation Evaluation, p. 4 |
| 3c | Resultados por clase remitidos fuera del PDF | "Results for each structure independently are shown in Figure S1" | Results, Segmentation Evaluation, p. 4 |
| 3d | Dice por clase: sacro | NO ENCONTRADO EN EL PDF | --- |
| 3e | Dice por clase: S1 | NO ENCONTRADO EN EL PDF | --- |
| 3f | Dice por clase: cadera | NO ENCONTRADO EN EL PDF | --- |
| 4a | CT con implantes metalicos o artefactos en entrenamiento o test | NO ENCONTRADO EN EL PDF | --- |
| 4b | Desempeno con metal | NO ENCONTRADO EN EL PDF | --- |
| 4c | Anormalidades presentes (sin metal entre las categorias) | "645 showed different types of abnormality (tumor, vascular, trauma, inflammation, bleeding" | Results, Characteristics of the Study Sample, p. 4 |
| 4d | Numero de casos con fractura pelvica o hueso pelvico patologico | NO ENCONTRADO EN EL PDF (la Figura 3 solo da barras sin cifras para "trauma", "pelvis" y "bones") | Figura 3, p. 5 |
| 5a | Limitacion declarada | "A limitation of our study was that male patients were overrepresented" | Discussion, p. 8 |
| 5b | Fallo tipico en vertebras | "mixing up neighboring vertebrae and ribs" | Results, Typical failure cases, p. 5 |
| 5c | Exclusion de estructuras muy deformadas | "structures highly distorted as a result of abnormality) (n = 40) were excluded" | Materials and Methods, Training dataset, p. 2 |
| 5d | Fracturas: solo evidencia cualitativa | "even when structures were distorted (broken bones)" | Figura 5, leyenda, p. 6 |
| 5e | Limitacion declarada especifica sobre hueso pelvico, metal o fracturas | NO ENCONTRADO EN EL PDF | --- |
| 6a | Disponibilidad publica | "publicly available (https://github.com/wasserth/TotalSegmentator)" | Conclusion, p. 9 |
| 6b | Distribucion como paquete | "providing it as a pretrained Python package" | Discussion, p. 7 |
| 6c | Licencia o condiciones de uso del software o del modelo | NO ENCONTRADO EN EL PDF | --- |

### Todas las cifras, umbrales, definiciones y criterios del paper

| Cifra / criterio | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Fechas editoriales | "Received January 25, 2023; revision requested February 27; revision received May 16" | Cabecera, p. 1 |
| Aceptacion | "accepted June 14" | Cabecera, p. 1 |
| Financiacion | "Authors declared no funding for this work." | Cabecera, p. 1 |
| 1204 CT, anos de muestreo | "1204 CT examinations (from 2012, 2016, and 2020)" | Abstract, p. 1 |
| 104 estructuras y su composicion | "segment 104 anatomic structures (27 organs, 59 bones, 10 muscles, and eight vessels)" | Abstract, p. 1 |
| 4004 CT de cuerpo entero | "applied to a second dataset of 4004 whole-body CT examinations" | Abstract, p. 1 |
| Dice 0.943 en test | "showed a high Dice score (0.943) on the test set" | Abstract, p. 1 |
| 0.932 vs 0.871 (Abstract) | "on a separate dataset (Dice score, 0.932 vs 0.871; P < .001)" | Abstract, p. 1 |
| Correlacion edad-volumen aortico | "age and aortic volume [rs = 0.64; P < .001]" | Abstract, p. 1 |
| Correlacion edad-atenuacion musculatura dorsal | "autochthonous dorsal musculature [rs = −0.74; P < .001]" | Abstract, p. 1 |
| DOI del dataset | "The annotated dataset (https://doi.org/10.5281/zenodo.6802613)" | Abstract, Conclusion, p. 1 |
| IC 95% del Dice | "Dice similarity coefficient (0.943; 95% CI: 0.938, 0.947) on the test set" | Key Points, p. 2 |
| Aprobacion etica | "(EKNZ BASEC Req-2022–00495)" | Materials and Methods, p. 2 |
| 1368 CT muestreados | "1368 CT examinations were randomly sampled from 2012, 2016, and 2020" | Training dataset, p. 2 |
| Exclusion extremidades | "CT series of upper and lower extremities (n = 37)" | Training dataset, p. 2 |
| Exclusion cortes faltantes | "CT series with missing slices (n = 87)" | Training dataset, p. 2 |
| Exclusion por ambiguedad | "could not segment certain structures because of high ambiguity" (n = 40) | Training dataset, p. 2 |
| Remuestreo | "All images were resampled to 1.5-mm isotropic resolution." | Training dataset, p. 2 |
| Particion entrenamiento/validacion | "a training dataset of 1082 patients (90%), a validation dataset of 57 patients (5%)" | Training dataset, p. 2 |
| Particion test | "and a test dataset of 65 patients (5%)" | Training dataset, p. 2 |
| Politrauma inicial | "whole-body CT between 2011 and 2020 ... (n = 4102)" | Aging study dataset, p. 2 |
| Exclusiones del estudio de edad | "unknown age (n = 30) or incomplete images (n = 33)" | Aging study dataset, p. 2 |
| Exclusion sin contraste | "without administration of a contrast agent (n = 35) were excluded" | Aging study dataset, p. 2 |
| Protocolo del estudio de edad | "contrast-enhanced, whole-body CT in an arteriovenous split-bolus phase" | Aging study dataset, p. 2 |
| Software de anotacion | "The Nora Imaging Platform was used for manual segmentation" | Data Annotation, p. 2 |
| Supervision de la anotacion | "supervised by two physicians with 3 (M.S.) and 6 (H.C.B.) years" | Data Annotation, p. 2 |
| Anotacion iterativa | "retrained after review and refinement of five patients, 20 patients, and 100 patients" | Data Annotation, p. 2 |
| Particion final del flujo | "1139 patients: train+validate set" / "65 patients: final test set" | Figura 1B, p. 3 |
| Separacion del modelo final | "This final model was independent of the intermediate models" | Data Annotation, p. 2 |
| Hardware de medicion | "Intel Core i9 3.5-GHz CPU and NVIDIA GeForce RTX 3090 GPU" | Model, p. 2 |
| Definicion de NSD (umbral 3 mm) | "measures how often the surface distance is less than 3 mm" | Statistical Analysis, p. 2 |
| Rango de las metricas | "Both metrics range between 0 (worst) and 1 (best)" | Statistical Analysis, p. 3 |
| BTCV: 13 estructuras | "that dataset provided labels for only 13 structures" | Statistical Analysis, p. 3 |
| IC por bootstrap | "nonparametric percentile bootstrapping with 10 000 iterations" | Statistical Analysis, p. 3 |
| Prueba estadistica | "A Wilcoxon signed rank test was used to compare the Dice and NSD" | Statistical Analysis, p. 3 |
| Umbral de significancia | "P values less than .05 were considered to indicate statistically significant" | Statistical Analysis, p. 3 |
| Criterio de segmentacion fallida | "failed if the volume ... was too small to be anatomically plausible" | Aging study dataset (Statistical Analysis), p. 3 |
| Umbrales de volumen minimo por estructura | NO ENCONTRADO EN EL PDF (se remite a "Table S1") | p. 3 |
| Cuartiles de edad y correccion | "Patients were grouped into four age quartiles" | Statistical Analysis, p. 4 |
| Limites de cuartil | "Q1 <41", "Q2 41-59", "Q3 59-78", "Q4 >78" (ejes) | Figura 6, p. 8 |
| Umbral con Bonferroni | "Bonferroni correction was performed, and P values less than .0001" | Statistical Analysis, p. 4 |
| Diversidad de adquisicion | "CT images from eight different sites and 16 different scanners" | Characteristics of the Study Sample, p. 4 |
| Fabricante predominante | "most images were acquired using a Siemens manufacturer" | Characteristics of the Study Sample, p. 4 |
| Doble energia | "Dual-energy CT images obtained using different tube voltages were also included." | Characteristics of the Study Sample, p. 4 |
| Kernels | "Different kernels (soft-tissue kernel, bone kernel)" | Characteristics of the Study Sample, p. 4 |
| Sin anormalidad | "A total of 404 patients showed no signs of abnormality" | Characteristics of the Study Sample, p. 4 |
| Informacion faltante | "not available for 155 patients because of missing radiology reports" | Characteristics of the Study Sample, p. 4 |
| Rango de edad del estudio de edad | "uniform age distribution, ranging from 18 to 100 years" | Characteristics of the Study Sample, p. 4 |
| Distribucion por sexo | "(2543 men [63.5%] and 1461 women [36.5%])" | Characteristics of the Study Sample, p. 4 |
| Dice 3 mm | "The 3-mm model showed a lower Dice score of 0.840 (95% CI: 0.836, 0.844)" | Segmentation Evaluation, p. 4 |
| NSD 3 mm | "but the NSD was 0.966 (95% CI: 0.962, 0.969)" | Segmentation Evaluation, p. 4 |
| Comparacion Dice con BTCV en test propio | "higher Dice coefficient (0.932 [95% CI: 0.920, 0.942] vs 0.871" | Segmentation Evaluation, p. 5 |
| IC del modelo BTCV en test propio | "vs 0.871 [95% CI: 0.855, 0.887], respectively; P < .001)" | Segmentation Evaluation, p. 5 |
| Comparacion NSD en test propio | "NSD score (0.971 [95% CI: 0.961, 0.979] vs 0.921 [95% CI: 0.907, 0.936]" | Segmentation Evaluation, p. 5 |
| Ubicacion de la comparacion (Resultados) | "P < .001) on our test set" | Segmentation Evaluation, p. 5 |
| Dice en dataset BTCV | "it achieved a Dice coefficient of 0.849 (95% CI: 0.833, 0.862)" | Segmentation Evaluation, p. 5 |
| NSD en dataset BTCV | "NSD score of 0.932 (95% CI: 0.920, 0.943)" | Segmentation Evaluation, p. 5 |
| nnU-Net BTCV sobre BTCV | "(Dice coefficient, 0.839 [95% CI: 0.821, 0.856]; NSD score, 0.915" | Segmentation Evaluation, p. 5 |
| IC NSD nnU-Net BTCV sobre BTCV | "0.915 [95% CI: 0.900, 0.930])" | Segmentation Evaluation, p. 5 |
| Fallos tipicos | "missing small parts of the colon or iliac arteries" | Typical failure cases, p. 5 |
| Porcentajes de fallo | "Percentage of cases with this failure:" 35% colon, 1% vertebrae, 12% ribs, 11% iliac artery | Figura 4, p. 6 |
| Etiqueta del fallo vertebral | "mixing neighboring vertebrae classes" | Figura 4, p. 6 |
| Aviso de los autores | "Users should be aware that these problems may occur." | Figura 4, leyenda, p. 6 |
| Casos patologicos | "it generated robust results on patients with major abnormalities" | Performance on pathologic cases, p. 5 |
| Tamanos de estudio del benchmark de tiempo | "512 × 512 × 280 voxels", "512 × 512 × 458 voxels", "512 × 512 × 824 voxels" | Runtime, p. 5 |
| Tiempo, 1.5 mm | "1 min 17 sec", "2 min 49 sec", "3 min 32 sec" (pequeno/mediano/grande) | Tabla, p. 7 |
| RAM y GPU, 1.5 mm | RAM "7.6", "10.6", "11.8" GB; GPU "6.1", "8.5", "11.4" GB | Tabla, p. 7 |
| Tiempo, 3 mm | "34 sec", "53 sec", "1 min 23 sec" | Tabla, p. 7 |
| RAM y GPU, 3 mm | RAM "7.4", "8.4", "10.6" GB; GPU "5.2", "7.4", "7.5" GB | Tabla, p. 7 |
| Requisitos minimos | "Our model requires less than 12 GB of RAM and does not require a GPU." | Discussion, p. 7 |
| Correlacion clavicula | "attenuation in the clavicle (rs = −0.53; P < .0001)" | Evaluation of age-related differences, p. 6 |
| Correlacion caderas | "hips (rs = −0.61; P < .0001 [Fig 6])" | Evaluation of age-related differences, p. 6 |
| Idem en figura | "rs = −0.611, ps < 0.0001" (hip attenuation) | Figura 6A, p. 8 |
| Correlacion L4 | "lumbar vertebra 4, rs = −0.55; P < .0001" | Evaluation of age-related differences, p. 6 |
| Musculatura dorsal | "autochthonous dorsal musculature (rs = −0.74; P < .0001)" | Evaluation of age-related differences, p. 6 |
| Gluteos | "gluteus maximus: rs = −0.51", "gluteus medius: rs = −0.61", "gluteus minimus: rs = −0.79" | Evaluation of age-related differences, p. 6 |
| Iliopsoas | "(rs = −0.57 [P < .0001] and rs = −0.61 [P < .0001])" | Evaluation of age-related differences, p. 6 |
| Idem en figura | "rs = −0.610, ps < 0.0001" (iliopsoas volume) | Figura 6C, p. 8 |
| Aorta | "the aorta and patient age (rs = 0.64; P < .0001)" | Evaluation of age-related differences, p. 6 |
| Idem en figura | "rs = 0.644, ps < 0.0001" (aorta volume) | Figura 6E, p. 8 |
| Arterias iliacas | "less positive for the iliac arteries (rs = 0.33; P < .0001)" | Evaluation of age-related differences, p. 6 |
| Rinon y pancreas | "kidney volume (rs = −0.49; P < .0001) and pancreas volume (rs = −0.49" | Evaluation of age-related differences, p. 7 |
| Bigotes de los box plots | "25th percentile subtracted by 1.5 times the IQR" | Figura 6, leyenda, p. 8 |
| Dice resumido en la Discusion | "demonstrated high accuracy (Dice coefficient of 0.943)" | Discussion, p. 7 |
| Chen et al: 50 estructuras | "the algorithm reported by Chen et al (6) segments 50 different structures" | Discussion, p. 7 |
| Shiyam Sundar et al: 120 estructuras | "Shiyam Sundar et al (19) segments 120 structures" | Discussion, p. 7 |
| Shiyam Sundar: RAM | "the model requires 256 GB of RAM" | Discussion, p. 7 |
| Shiyam Sundar: tamano | "training data consist of fewer than 100 individuals" | Discussion, p. 7 |
| Tragardh et al: 100 estructuras | "segments 100 structures" | Discussion, p. 7 |
| Tragardh: muestras | "the 339 training samples are homogeneous" | Discussion, p. 7 |
| Descargas | "More than 4500 researchers have already downloaded our model" | Discussion, p. 7 |
| Acceso al dataset | "it does not require any access requests" | Discussion, p. 7 |
| Rango de kVp en entrenamiento | eje "Kilovoltage peak" de 80 a 140 (sin cifras por barra) | Figura 3, p. 5 |
| Rango de corriente de tubo | eje "Tube current" de 0 a 2500 (sin cifras por barra) | Figura 3, p. 5 |
| Trabajo futuro | "we plan to add more anatomic structures to our dataset and model" | Discussion, p. 9 |
