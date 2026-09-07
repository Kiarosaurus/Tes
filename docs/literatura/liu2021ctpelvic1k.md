# liu2021ctpelvic1k — CTPelvic1K: datasets CT pelvicos a gran escala y modelos baseline

- **DOI / URL:** https://doi.org/10.1007/s11548-021-02363-8 — repositorio: https://github.com/ICT-MIRACLE-lab/CTPelvic1K
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/liu2021ctpelvic1k.pdf

Profundidad: articulo completo (8 paginas). Varios detalles remitidos por los autores a "Online Resource 1", que NO esta en el PDF.

## Que hace (3 lineas maximo)

Curan un dataset CT pelvico de 1184 volumenes agregando siete fuentes (dos clinicas propias, cinco datasets publicos), anotado en cuatro clases oseas.
Entrenan una cascada 3D U-Net (nnU-Net) multiclase multi-dominio como baseline de segmentacion.
Anaden un post-procesador basado en signed distance function (SDF) que reduce la distancia de Hausdorff frente al post-proceso tradicional por region conexa maxima.

## Restriccion o supuesto clave

No es un paper de sintesis generativa, asi que la pregunta de la plantilla no aplica directamente. La restriccion equivalente y decisiva para esta tesis es que el subconjunto con metal queda fuera del entrenamiento supervisado y en su mayoria sin anotar: "Due to the difficulty of labeling the CLINIC-metal, CLINIC-metal is taken off in our supervised training phase" (Tabla 1, pie) y "The remaining 61 metal-affected CTs are left unannotated" (Our dataset / Data annotation). Es decir: el propio dataset primario asume que anotar hueso bajo artefacto metalico es demasiado dificil, que es exactamente el hueco que la tesis quiere atacar.

## Que toco de aqui
- [x] metodo que reimplemento  (baseline de segmentacion: cascada 3D U-Net / nnU-Net)
- [x] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 1184 volumenes CT totales | "including 1, 184 CT volumes of diverse appearance variations" | Introduction, contribuciones, p. 2 |
| >320K cortes CT | "1, 184 CT volumes (over 320K CT slices)" | Introduction, contribuciones, p. 2 |
| 75 CTs con artefacto metalico | "including 75 CTs with metal artifacts" | Introduction, contribuciones, p. 2 |
| 1109 CTs sin metal anotados | "we have annotations for 1109 metal-free CTs" | Data annotation, p. 3 |
| 14 CTs con metal anotados | "and 14 metal-affected CTs" | Data annotation, p. 3 |
| 61 CTs con metal SIN anotar | "The remaining 61 metal-affected CTs are left unannotated" | Data annotation, p. 3 |
| Dice medio 0.987 (volumen sin metal) | "achieving an average Dice of 0.987 for a metal-free volume" | Abstract, Results, p. 1 |
| HD medio 5.50 voxeles | "an average DC of 0.987 and HD of 5.50 voxels" | Results and discussion, p. 5 |
| SDF reduce 15.1% la HD vs post-proceso tradicional | "SDF post-processor yields a decrease of 15.1% in Hausdorff distance" | Abstract, Results, p. 1 |
| SDF reduce 80.7% la HD vs sin post-proceso | "a decrease of 80.7% and 15.1% in HD" | SDF post-processor, p. 6 |
| 40 casos anotados manualmente al inicio | "two senior experts are invited to pixel-wise annotate 40 cases" | Data annotation, p. 3 |
| 4 clases oseas | "lumbar spine, sacrum, left hip, and right hip" | Introduction, p. 2 |
| Particion 3/5, 1/5, 1/5 (dataset sin metal) | "we randomly select 3/5, 1/5, 1/5 cases in each sub-dataset" | Implementation details, p. 4 |
| Espaciado medio global (0.78, 0.78, 1.46) mm | Tabla 1, fila "Our Datasets" | Tabla 1, p. 3 |
| Licencia CC-BY-NC-SA 4.0 para CLINIC y CLINIC-metal | "open-source them under Creative Commons license CC-BY-NC-SA 4.0" | Our dataset, p. 3 |

## Donde entra en mi tesis

- **Datos (Objetivo 1 al 5):** es el dataset primario. Define de donde salen los volumenes y el subconjunto CLINIC-metal.
- **Objetivo 5 (evaluacion downstream):** aporta el baseline de segmentacion (cascada 3D U-Net / nnU-Net, 4 clases) y las cifras de referencia Dice 0.987 / HD 5.50 voxeles sobre datos SIN metal. Ver la advertencia en Verificacion de nivel, pregunta 2 y 5.
- **Motivacion / gap:** el paper declara los artefactos metalicos como la variacion mas dificil y deja 61 volumenes con metal sin anotar, lo que sostiene el planteamiento de la tesis.
- **Objetivo 1 (multi-ventana, MAE < 25 HU):** el paper no aporta nada sobre ventanas HU ni MAE. NO ENCONTRADO EN EL PDF.

## Dudas para el asesor

1. Los 14 volumenes de CLINIC-metal anotados son el unico set de prueba con metal del paper y el paper no reporta metrica sobre ellos. Es suficiente n=14 para la evaluacion del Objetivo 5, o hay que anotar parte de los 61 restantes?
2. El paper reporta HD (no HD95) y en voxeles, no en mm. La tesis usa HD95 en mm: hay que recalcular el baseline en vez de citar el numero publicado. Se acepta reentrenar el baseline en lugar de comparar contra la cifra impresa?
3. Como se obtiene el tipo de implante presente en CLINIC-metal si el paper no lo describe? Se inspecciona el volumen manualmente y se documenta como dato propio?
4. "Online Resource 1" contiene los detalles del dataset y la seccion "Limitations of the dataset". Se consigue ese material suplementario antes de fijar el protocolo de evaluacion?

## Evidencia textual

| Dato / criterio | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| Total del dataset | "including 1, 184 CT volumes of diverse appearance variations" | Introduction, contribuciones, p. 2 |
| Numero de cortes | "1, 184 CT volumes (over 320K CT slices)" | Introduction / Conclusion, p. 2 y 6 |
| Volumenes con metal | "including 75 CTs with metal artifacts" | Introduction, contribuciones, p. 2 |
| Numero de fuentes | "we curate a large dataset of pelvic CT images from seven sources" | Data collection, p. 2 |
| Origen de las fuentes | "two of which come from a clinic and five from existing CT datasets" | Data collection, p. 2 |
| ABDOMEN: n / espaciado / tamano / split / origen | "ABDOMEN | 35 | (0.76, 0.76, 3.80) | (512, 512, 73) | 21/7/7 | Public 2015" | Tabla 1, p. 3 |
| COLONOG | "COLONOG | 731 | (0.75, 0.75, 0.81) | (512, 512, 323) | 440/146/145 | Public 2008" | Tabla 1, p. 3 |
| MSD_T10 | "MSD_T10 | 155 | (0.77, 0.77, 4.55) | (512, 512, 63) | 93/31/31 | Public 2019" | Tabla 1, p. 3 |
| KITS19 | "KITS19 | 44 | (0.82, 0.82, 1.25) | (512, 512, 240) | 26/9/9 | Public 2019" | Tabla 1, p. 3 |
| CERVIX | "CERVIX | 41 | (1.02, 1.02, 2.50) | (512, 512, 102) | 24/8/9 | Public 2015" | Tabla 1, p. 3 |
| CLINIC | "CLINIC | 103 | (0.85, 0.85, 0.80) | (512, 512, 345) | 61/21/21 | Collected 2020" | Tabla 1, p. 3 |
| CLINIC-metal | "CLINIC-metal | 75 | (0.83, 0.83, 0.80) | (512, 512, 334) | 0(61)/0/14 | Collected 2020" | Tabla 1, p. 3 |
| Totales | "Our Datasets | 1, 184 | (0.78, 0.78, 1.46) | (512, 512, 273) | 665(61)/222/236" | Tabla 1, p. 3 |
| CLINIC-metal excluido del entrenamiento supervisado | "CLINIC-metal is taken off in our supervised training phase" | Tabla 1, pie, p. 3 |
| Volumenes con metal sin anotacion | "The remaining 61 metal-affected CTs are left unannotated" | Data annotation, p. 3 |
| Uso previsto de los no anotados | "planned for use in unsupervised learning" | Data annotation, p. 3 |
| Anotaciones existentes | "In total, we have annotations for 1109 metal-free CTs and 14 metal-affected CTs" | Data annotation, p. 3 |
| Clases anotadas | "lumbar spine, sacrum, left hip, and right hip" | Introduction, p. 2 |
| Calidad de anotacion declarada | "Their multi-bone labels are carefully annotated by experts" | Introduction, contribuciones, p. 2 |
| Estrategia de anotacion | "We introduce a strategy of Annotation by Iterative Deep Learning (AID)" | Data annotation, p. 3 |
| Paso I de anotacion | "two senior experts are invited to pixel-wise annotate 40 cases of CLINIC" | Data annotation, p. 3 |
| Software de anotacion | "using ITK Snap (Philadelphia, PA) software" | Data annotation, p. 3 |
| Plano de anotacion | "All annotations are performed in the transverse plane" | Data annotation, p. 3 |
| Paso II | "we train a deep network with the updated database and make predictions" | Data annotation, p. 3 |
| Paso III | "some junior annotators refine the labels based on the prediction results" | Data annotation, p. 3 |
| Carga por anotador junior | "each junior annotator is only responsible for part of 100 new data" | Data annotation, p. 3 |
| Control de calidad | "A coordinator will check the quality of refinement by all junior annotators" | Data annotation, p. 3 |
| Casos dificiles | "for hard cases, senior experts are invited to make more precise annotations" | Data annotation, p. 3 |
| Revision final | "we conduct another round of scrutiny for outliers and mistakes" | Data annotation, p. 3 |
| Perfil de anotadores junior | "'Junior annotators' are graduate students in the field of medical image analysis" | Data annotation, p. 3 |
| Perfil del coordinador | "a medical image analysis practitioner with many years of experience" | Data annotation, p. 3 |
| Perfil de expertos senior | "the 'Senior experts' are cooperating doctors in the partner hospital" | Data annotation, p. 3 |
| Metal como variacion mas dificil | "the challenge of the metal artifacts is the most difficult to handle" | Introduction, p. 2 |
| Metrica reportada Dice (abstract) | "achieving an average Dice of 0.987 for a metal-free volume" | Abstract, p. 1 |
| Metricas usadas | "we use Dice coefficient (DC) and Hausdorff distance (HD) as the metrics" | Results and discussion, p. 5 |
| Mejor baseline global | "achieving an average DC of 0.987 and HD of 5.50 voxels" | Results and discussion, p. 5 |
| Tabla 2(a) 2.5D | "ALL | Phi_ALL(2.5D) | .988/9.28 | .979/9.34 | .990/3.58 | .990/3.44 | .978/8.32 | .984/6.17" | Tabla 2(a), p. 5 |
| Tabla 2(a) 3D | "ALL | Phi_ALL(3D) | .988/11.38 | .984/8.13 | .988/4.99 | .990/4.26 | .982/7.80 | .986/6.30" | Tabla 2(a), p. 5 |
| Tabla 2(a) 3D cascade | "ALL | Phi_ALL(3D_cascade) | .989/10.23 | .984/7.24 | .989/4.24 | .991/3.03 | .984/7.49 | .987/5.50" | Tabla 2(a), p. 5 |
| Tabla 2(b) sin post-proceso | "w/o Post | .988/36.27 | .984/38.36 | .988/35.43 | .991/28.70 | .983/11.25 | .987/28.43" | Tabla 2(b), p. 5 |
| Tabla 2(b) MCR | "MCR | .988/12.93 | .984/7.50 | .989/4.24 | .991/3.72 | .978/10.46 | .986/6.48" | Tabla 2(b), p. 5 |
| Tabla 2(b) SDF(5) | "SDF(5) | .989/12.02 | .984/7.24 | .989/4.24 | .991/3.51 | .980/9.54 | .986/6.13" | Tabla 2(b), p. 5 |
| Tabla 2(b) SDF(15) | "SDF(15) | .989/10.40 | .984/7.24 | .989/4.24 | .991/3.35 | .984/7.61 | .987/5.61" | Tabla 2(b), p. 5 |
| Tabla 2(b) SDF(35) | "SDF(35) | .989/10.23 | .984/7.24 | .989/4.24 | .991/3.03 | .984/7.49 | .987/5.50" | Tabla 2(b), p. 5 |
| Tabla 2(b) SDF(55) | "SDF(55) | .989/10.78 | .984/7.24 | .989/4.52 | .991/3.38 | .984/7.49 | .987/5.66" | Tabla 2(b), p. 5 |
| Tabla 3, modelo Phi_ALL por sub-dataset | "Phi_ALL | .987/5.50 | .979/2.88 | .989/5.87 | .987/3.11 | .985/5.77 | .972/5.01 | .982/7.42" | Tabla 3, p. 6 |
| Tabla 3, Phi_CLINIC | "Phi_CLINIC | .692/69.89 | .275/117.09 | .728/71.93 | .254/126.66 | .985/11.16 | .968/9.69 | .983/7.27" | Tabla 3, p. 6 |
| Tabla 3, leave-one-out | "Phi_ex sub-dataset | - | .978/2.77 | .986/7.37 | .984/3.37 | .982/8.33 | .975/4.92 | .975/8.87" | Tabla 3, p. 6 |
| Columnas de Tabla 3 (sin CLINIC-metal) | "ALL | ABDOMEN | COLONOG | MSD_T10 | KITS19 | CERVIX | CLINIC" | Tabla 3, encabezado, p. 6 |
| 'ALL' se refiere solo a lo sin metal | "'ALL' refers to the six metal-free sub-datasets" | Tabla 2, pie, p. 5 |
| Efecto SDF | "SDF post-processor yields a decrease of 80.7% and 15.1% in HD" | SDF post-processor, p. 6 |
| Recorte de valores en el heat map | "we clip some outliers to the boundary value, i.e., 0.95 in DC and 30 in HD" | Fig. 4, pie, p. 6 |
| Licencia base | "All existing sub-datasets are under Creative Commons license CC-BY-NC-SA at least" | Our dataset, p. 3 |
| Licencia CLINIC / CLINIC-metal | "open-source them under Creative Commons license CC-BY-NC-SA 4.0" | Our dataset, p. 3 |
| Formato | "the raw data of COLONOG, CLINIC, and CLINIC-metal are stored in a DICOM format" | Our dataset, p. 3 |
| Reformateo | "We reformat all DICOM images to NIfTI to simplify data processing and de-identify" | Our dataset, p. 3 |
| Cumplimiento IRB | "meeting the institutional review board (IRB) policies of contributing sites" | Our dataset, p. 3 |
| Exclusiones | "we exclude some cases of very low quality or without pelvic region" | Our dataset, p. 3 |
| Recorte de la imagen | "remove the unrelated areas outside the pelvis in our current dataset" | Our dataset, p. 3 |
| Aprobacion etica | "We have obtained the approval from the Ethics Committee of clinical hospital" | Declarations, p. 7 |
| Disponibilidad | "Please refer to https://github.com/ICT-MIRACLE-lab/CTPelvic1K" | Availability of data and material, p. 7 |
| Arquitectura baseline | "3D U-Net cascade version of nnU-Net [14]" | Segmentation module, p. 4 |
| Implementacion | "We implement our method based on open source code of nnU-Net. We also used MONAI" | Implementation details, p. 4 |
| Post-proceso SDF, base de calculo | "We calculate SDF based on the maximum connected region (MCR) of the anatomical structure" | SDF post processor, p. 4 |
| Mortalidad en fracturas pelvicas (cifra citada de [10]) | "the mortality rate can reach 45% at the most severe situation" | Introduction, p. 1 |
| Limite del trabajo previo citado | "the result was not very good (Dice=0.92) with the dataset only having 200 CT slices" | Introduction, p. 2 |
| Tamano de datasets previos | "less than 5 images or 200 slices" | Introduction, p. 2 |
| Trabajo futuro sobre metal | "devising a module for metal-affected CTs and domain-independent pelvic bones segmentation" | Conclusion, p. 7 |
| Financiamiento | "supported in part by the Youth Innovation Promotion Association CAS (grant 2018135)" | Funding, p. 7 |
| Umbral de MAE en HU / ventanas HU | NO ENCONTRADO EN EL PDF | — |
| HD95 | NO ENCONTRADO EN EL PDF (solo HD) | — |
| Tipo de implante metalico en CLINIC-metal | NO ENCONTRADO EN EL PDF | — |
| Metrica cuantitativa sobre CLINIC-metal | NO ENCONTRADO EN EL PDF | — |
| Marca/modelo de escaner y kVp/mAs | NO ENCONTRADO EN EL PDF (remitido a Online Resource 1) | — |

## Verificacion de nivel

Criterio de la autora: Nivel 1 = critico, si se equivoca aqui se cae una tesis o el benchmark. Nivel 2 = afecta la redaccion. Nivel 3 = apoyo.
Este paper esta en NIVEL 1, asignado por la autora, con el rol "dataset primario".

**1. Composicion exacta del dataset.**
Total: 1184 volumenes ("including 1, 184 CT volumes of diverse appearance variations", Introduction p. 2), mas de 320K cortes. Siete sub-datasets, "two of which come from a clinic and five from existing CT datasets" (Data collection, p. 2). Segun la Tabla 1 (p. 3), columna "#" y "Source and Year":

| Sub-dataset | # volumenes | Origen (Tabla 1) | Tr/Val/Ts |
|---|---|---|---|
| ABDOMEN | 35 | Public 2015 | 21/7/7 |
| COLONOG | 731 | Public 2008 | 440/146/145 |
| MSD_T10 | 155 | Public 2019 | 93/31/31 |
| KITS19 | 44 | Public 2019 | 26/9/9 |
| CERVIX | 41 | Public 2015 | 24/8/9 |
| CLINIC | 103 | Collected 2020 | 61/21/21 |
| CLINIC-metal | 75 | Collected 2020 | 0(61)/0/14 |
| **Our Datasets** | **1,184** | — | 665(61)/222/236 |

Las dos fuentes clinicas son CLINIC y CLINIC-metal ("Collected 2020"); las cinco publicas son ABDOMEN, COLONOG, MSD_T10, KITS19 y CERVIX. El PDF cita las fuentes publicas solo por numero de referencia ([3,12,15,28]): las citas completas estan en References p. 7 pero el paper no mapea explicitamente cual referencia corresponde a cual sub-dataset. Ese mapeo: NO ENCONTRADO EN EL PDF.

**2. CRITICO — CLINIC-metal tiene ground truth de segmentacion osea?**
**Respuesta: solo parcialmente. 14 de 75 volumenes estan anotados; 61 NO lo estan.** Con todas las letras: **CLINIC-metal NO tiene ground truth completo.**
Frases literales:
- "In total, we have annotations for 1109 metal-free CTs and 14 metal-affected CTs." (Data annotation, p. 3)
- "The remaining 61 metal-affected CTs are left unannotated and planned for use in unsupervised learning." (Data annotation, p. 3)
- "Due to the difficulty of labeling the CLINIC-metal, CLINIC-metal is taken off in our supervised training phase." (pie de Tabla 1, p. 3)
- Tabla 1 confirma el split de CLINIC-metal: "0(61)/0/14", es decir cero de entrenamiento supervisado (61 disponibles sin etiqueta), cero de validacion, 14 de test.

Sobre COMO se obtuvo la anotacion: el paper describe un unico pipeline para todo el dataset, semiautomatico e iterativo (AID), no una anotacion manual pura: "We introduce a strategy of Annotation by Iterative Deep Learning (AID) to speed up our annotation process" (p. 3). Arranca con 40 casos de CLINIC (no de CLINIC-metal) anotados manualmente por dos expertos senior con ITK-SNAP en plano transversal; luego una red predice, anotadores junior (estudiantes de posgrado) corrigen, un coordinador (profesional de analisis de imagen medica) revisa, y los casos dificiles van a expertos senior (medicos del hospital socio). Hay una ronda final de revision de outliers. El paper afirma de forma general "Their multi-bone labels are carefully annotated by experts" (p. 2). **El PDF no describe un procedimiento especifico ni un control de calidad separado para los 14 volumenes con metal, ni reporta acuerdo inter-observador: NO ENCONTRADO EN EL PDF.**

**Consecuencia para el Objetivo 5:** la evaluacion downstream con Dice y HD95 en la zona peri-implante depende de esos 14 volumenes anotados como unica referencia con metal real. Es una muestra pequena, de calidad no caracterizada explicitamente en la zona de artefacto, y producida por un pipeline que arrancó desde datos sin metal. Registrar esto como implicancia para decision de la autora (no lo hago yo, regla 14).

**3. CRITICO — cuantos volumenes tiene CLINIC-metal y que tipo de metal contienen?**
- Cantidad: 75. "including 75 CTs with metal artifacts" (Introduction, p. 2); Tabla 1, fila CLINIC-metal, columna "#": 75.
- Tipo de metal: **NO ENCONTRADO EN EL PDF.** El paper habla siempre de "metal artifacts" como variacion de apariencia, nunca del objeto que los produce. La unica evidencia visual es el panel etiquetado "Metal artifact" en la Fig. 1 (p. 2), sin descripcion textual del implante. **No hay ninguna frase que diga si son tornillos, placas, protesis de cadera u otro material.** No se puede afirmar en la tesis que CLINIC-metal contenga implantes de osteosintesis apoyandose en este paper.

**4. Estructuras anotadas y numero de clases.**
Cuatro clases oseas: "a deep multi-class network for segmenting lumbar spine, sacrum, left hip, and right hip" (Abstract, p. 1) y "including lumbar spine, sacrum, left hip, and right hip, instead of simply segmenting out the whole pelvis" (Introduction, p. 2). Fig. 5 confirma la codificacion de color: "the white, green, blue, and yellow parts ... represent the sacrum, left hip bone, right hip bone, and lumbar spine, respectively" (pie de Fig. 5, p. 7). No hay clase de femur ni de implante. Nota: el ilion no se anota por separado; la clase es "hip" (hueso coxal) izquierdo y derecho.

**5. Cifras de baseline y sobre que subconjuntos.**
El paper reporta DC y HD (HD en voxeles; NO HD95). Mejor configuracion global: DC 0.987 / HD 5.50 voxeles con la cascada 3D U-Net. **Advertencia decisiva: todas las cifras son sobre los seis sub-datasets SIN metal** ("'ALL' refers to the six metal-free sub-datasets", pie de Tabla 2, p. 5) y la Tabla 3 no incluye columna CLINIC-metal.

Tabla 2 (p. 5), formato Dice/HD, columnas: Whole | Sacrum | Left hip | Right hip | Lumbar spine | Average:

| Exp | Modelo | Whole | Sacrum | Left hip | Right hip | Lumbar spine | Average |
|---|---|---|---|---|---|---|---|
| (a) | Phi_ALL(2.5D) | .988/9.28 | .979/9.34 | .990/3.58 | .990/3.44 | .978/8.32 | .984/6.17 |
| (a) | Phi_ALL(3D) | .988/11.38 | .984/8.13 | .988/4.99 | .990/4.26 | .982/7.80 | .986/6.30 |
| (a) | Phi_ALL(3D_cascade) | .989/10.23 | .984/7.24 | .989/4.24 | .991/3.03 | .984/7.49 | .987/5.50 |
| (b) | w/o Post | .988/36.27 | .984/38.36 | .988/35.43 | .991/28.70 | .983/11.25 | .987/28.43 |
| (b) | MCR | .988/12.93 | .984/7.50 | .989/4.24 | .991/3.72 | .978/10.46 | .986/6.48 |
| (b) | SDF(5) | .989/12.02 | .984/7.24 | .989/4.24 | .991/3.51 | .980/9.54 | .986/6.13 |
| (b) | SDF(15) | .989/10.40 | .984/7.24 | .989/4.24 | .991/3.35 | .984/7.61 | .987/5.61 |
| (b) | SDF(35) | .989/10.23 | .984/7.24 | .989/4.24 | .991/3.03 | .984/7.49 | .987/5.50 |
| (b) | SDF(55) | .989/10.78 | .984/7.24 | .989/4.52 | .991/3.38 | .984/7.49 | .987/5.66 |

Tabla 3 (p. 6), "Average Dice/HD" de cada modelo probado en cada dataset:

| Modelo | ALL | ABDOMEN | COLONOG | MSD_T10 | KITS19 | CERVIX | CLINIC |
|---|---|---|---|---|---|---|---|
| Phi_ABDOMEN | .604/92.81 | .979/5.84 | .577/104.04 | .980/3.74 | .360/158.02 | .305/92.07 | .342/148.12 |
| Phi_COLONOG | .985/5.84 | .975/3.29 | .989/5.65 | .974/4.41 | .982/8.41 | .969/5.17 | .974/9.24 |
| Phi_MSD_T10 | .534/96.14 | .979/2.97 | .501/106.86 | .987/3.36 | .245/170.39 | .085/112.72 | .261/151.61 |
| Phi_KITS19 | .704/68.29 | .255/120.31 | .746/70.75 | .267/121.57 | .986/5.65 | .973/5.14 | .977/9.25 |
| Phi_CERVIX | .973/14.75 | .969/4.30 | .974/18.74 | .967/6.55 | .979/7.78 | .973/4.49 | .974/10.17 |
| Phi_CLINIC | .692/69.89 | .275/117.09 | .728/71.93 | .254/126.66 | .985/11.16 | .968/9.69 | .983/7.27 |
| Phi_ALL | .987/5.50 | .979/2.88 | .989/5.87 | .987/3.11 | .985/5.77 | .972/5.01 | .982/7.42 |
| Phi_ex sub-dataset | - | .978/2.77 | .986/7.37 | .984/3.37 | .982/8.33 | .975/4.92 | .975/8.87 |

**Para el Objetivo 5:** el punto de comparacion mas cercano al escenario clinico sin metal es Phi_ALL sobre CLINIC (.982/7.42) o el conjunto ALL (.987/5.50). **No existe una cifra publicada sobre CLINIC-metal contra la cual comparar directamente: la tesis tendra que producir ese baseline por si misma.**

**6. Reporta desempeno degradado en presencia de metal?**
**No cuantitativamente.** La premisa central de la tesis NO esta respaldada por una cifra en este paper. Lo unico que existe es cualitativo/declarativo:
- "Among the above-mentioned appearance variations, the challenge of the metal artifacts is the most difficult to handle." (Introduction, p. 2)
- "Due to the difficulty of labeling the CLINIC-metal, CLINIC-metal is taken off in our supervised training phase." (Tabla 1, pie, p. 3)
- "Existing methods ... achieve limited accuracy when dealing with image appearance variations due to the multi-site domain shift, the presence of contrasted vessels, coprolith and chyme, bone fractures, low dose, metal artifacts, etc." (Abstract, p. 1) — aqui el metal es uno mas de una lista, no se aisla.
- Trabajo futuro: "devising a module for metal-affected CTs" (Conclusion, p. 7).
**Una cifra de degradacion por metal: NO ENCONTRADO EN EL PDF.** La Fig. 6 muestra dos pacientes pero del sub-dataset CLINIC, no CLINIC-metal ("Patient 1 in CLINIC sub-dataset").

**7. Licencia, disponibilidad y restricciones.**
- "All existing sub-datasets are under Creative Commons license CC-BY-NC-SA at least, and we will keep the license unchanged." (Our dataset, p. 3)
- "For CLINIC and CLINIC-metal sub-datasets, we will open-source them under Creative Commons license CC-BY-NC-SA 4.0." (Our dataset, p. 3)
- Acceso: "we ... open source the images, annotations, codes, and trained baseline models at https://github.com/ICT-MIRACLE-lab/CTPelvic1K" (Abstract, p. 1); repetido en Availability of data and material y Code availability (p. 7).
- Restricciones implicitas de CC-BY-NC-SA 4.0: uso **no comercial**, atribucion y obra derivada bajo la misma licencia. Relevante porque los volumenes sinteticos con implantes serian obra derivada.
- Tabla 1: la columna de ticks "indica que podemos acceder a la informacion del fabricante del equipo de adquisicion"; solo COLONOG, CLINIC y CLINIC-metal la tienen.
- Etica: "We have obtained the approval from the Ethics Committee of clinical hospital." (p. 7)
- Un acuerdo de uso de datos (DUA) o registro previo: NO ENCONTRADO EN EL PDF.

**8. Resolucion, espaciado y protocolos. Son heterogeneos?**
**Si, marcadamente heterogeneos**, sobre todo en el eje z. Todos los volumenes son 512x512 en plano (columna "Mean size" de la Tabla 1). Espaciado medio en plano entre 0.75 y 1.02 mm; espaciado entre cortes entre 0.80 mm (CLINIC y CLINIC-metal) y 4.55 mm (MSD_T10), casi 6x de diferencia. Numero medio de cortes entre 63 (MSD_T10) y 345 (CLINIC).
- CLINIC-metal: espaciado medio (0.83, 0.83, 0.80) mm, tamano medio (512, 512, 334). Es de los mas finos del dataset, favorable para 2.5D.
- El paper reconoce explicitamente la heterogeneidad: "diverse appearance variations", "domain shift arising from different sites" (Introduction, p. 2), y la demuestra con la Tabla 3 (modelos entrenados en un solo sub-dataset caen a Dice 0.085-0.36 en otros).
- Protocolos de adquisicion detallados (kVp, mAs, algoritmo de reconstruccion, fabricante concreto, uso de contraste por sub-dataset): **NO ENCONTRADO EN EL PDF.** El paper remite: "More details about our dataset are given in Online Resource 1" (p. 3), material no incluido en este PDF.

**9. Nivel que sostiene la evidencia.**
**Nivel 1, confirmado, pero con el rol matizado:** es legitimamente el dataset primario y la fuente de la composicion, licencia y baseline arquitectonico, pero NO puede sostener por si solo ni la premisa de degradacion por metal (no hay cifra) ni la caracterizacion del implante en CLINIC-metal (no se describe), asi que esos dos puntos necesitan otra fuente o experimento propio.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| [19] Lee PY, Lai JY, Hu YS, Huang CY, Tsai YC, Ueng WD (2012) Virtual 3D planning of pelvic fracture reduction and implant placement. Biomed Eng Appl Basis Commun 24(03):245–262 | Compite directamente con el **muestreador**: planificacion virtual 3D de colocacion de implante en pelvis. Es la referencia mas cercana a "donde y con que pose va el implante" citada en este paper. Podria reducir el gap afirmado. |
| [14] Isensee F, Jager PF, Kohl SA, Petersen J, Maier-Hein KH (2019) Automated design of deep learning methods for biomedical image segmentation. arXiv:1904.08128 | Es el nnU-Net, la arquitectura exacta del baseline downstream del Objetivo 5. Fuente original del metodo a reimplementar. |
| [24] Perera S, Barnes N, He X, Izadi S, Kohli P, Glocker B (2015) Motion segmentation of truncated signed distance function based volumetric surfaces. WACV | Fuente original de la SDF usada en el post-procesador. Metrica/criterio de distancia que podria validar o reemplazar un criterio de contencion cortical (BFC). |
| [25] Philbrick KA et al. (2019) RIL-contour: a medical imaging dataset annotation tool for and with deep learning. J Digit Imaging 32(4):571–581 | Fuente original de la estrategia AID de anotacion iterativa. Importa si hay que anotar los 61 volumenes con metal sin ground truth. |
| [10] Guo Q, Zhang L, Zhou S, Zhang Z, Liu H, Zhang L, Talmy T, Li Y (2020) Clinical features and risk factors for mortality in patients with open pelvic fractures: a retrospective study of 46 cases. J Orthop Surg | Fuente original de la cifra "mortality rate can reach 45%" que este paper cita en la Introduccion. Si esa cifra va a la tesis, hay que citarla de aqui. |
| [13] Hemke R, Buckless CG, Tsao A, Wang B, Torriani M (2020) Deep learning for automated segmentation of pelvic muscles, fat, and bone from body composition CT. Skelet Radiol 49(3):387–395 | Fuente original de la cifra "Dice=0.92 with the dataset only having 200 CT slices" usada por Liu et al. para justificar el gap de escala. |
| [3] Bennett L, Zhoubing X, Juan Eugenio I, Martin S, Thomas Robin L, Arno K (2015) 2015 MICCAI multi-atlas labeling beyond the cranial vault – workshop and challenge | Una de las cinco fuentes publicas del dataset (probablemente ABDOMEN/CERVIX). Necesaria para citar correctamente la procedencia de los datos. |
| [12] Heller N et al. (2019) The kits19 challenge data: 300 kidney tumor cases... arXiv:1904.00445 | Fuente original del sub-dataset KITS19. Procedencia de datos. |
| [15] Johnson CD et al. (2008) Accuracy of CT colonography for detection of large adenomas and cancers. N Engl J Med | Fuente original del sub-dataset COLONOG (731 volumenes, el mas grande). Procedencia de datos. |
| [28] Simpson AL et al. (2019) A large annotated medical image dataset for the development and evaluation of segmentation algorithms. arXiv:1902.09063 | Fuente original del sub-dataset MSD_T10 (Medical Segmentation Decathlon). Procedencia de datos. |
