# mirza2003 — Precision de tornillos toracicos con fluoroscopia estandar, guia fluoroscopica y guia por CT (cadaver)

- **DOI / URL:** NO ENCONTRADO EN EL PDF (el PDF solo indica: SPINE Volume 28, Number 4, pp 402-413, 2003)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/mirza2003.pdf

## Que hace (3 lineas maximo)
Estudio en 20 especimenes cadavericos de columna toracica: dos cirujanos colocan 337 tornillos transpediculares con cuatro sistemas (fluoroscopia estandar, FluoroNav referencia unica, FluoroNav referencias multiples, StealthStation basado en CT).
Mide tiempo, radiacion y posicion del tornillo por diseccion anatomica con calibrador en seis direcciones (anterior, lateral, medial, inferomedial, inferolateral, superior).
Asigna por direccion un grado 0-3 con cortes 0 / 2 / 4 mm, un grado global (maximo) y un score de severidad (suma, 0-18).

## Restriccion o supuesto clave
No es un paper de sintesis generativa. El supuesto clave para esta tesis es que **la escala 0-3 no nace aqui y no se justifica aqui**: se declara heredada ("The thresholds reported in prior studies were used", Materials and Methods, p. 405, con superindices 16 = Gertzbein & Robbins 1990 y 42 = Vaccaro et al. 1995 Part II). Los propios autores la debilitan: "these 'safe zone' thresholds do not apply to the thoracic spine" y "Safe zone threshold magnitudes are likely different for different directions of screw perforation" (Discussion, p. 411), y aun asi aplican los mismos cortes a las seis direcciones. La medicion es por diseccion y calibrador (limite inferior 0.2 mm), no por CT postoperatoria. Ademas los intervalos textuales dejan sin asignar los valores exactos 2 mm y 4 mm ("greater than 2 mm but less than 4 mm", p. 405).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Escala de 4 grados (0-3), atribuida a estudios previos | "The thresholds reported in prior studies were used: Grade 0 for 0 mm" | Materials and Methods (Screw Perforation Grade), p. 405 |
| Grado 1: >0 y <2 mm | "Grade 1 for a perforation distance greater than 0 mm but less than 2 mm" | Materials and Methods, p. 405 |
| Grado 2: >2 y <4 mm | "Grade 2 for a perforation distance greater than 2 mm but less than 4 mm" | Materials and Methods, p. 405 |
| Grado 3: >4 mm (cita 16, 42) | "Grade 3 for a perforation distance greater than 4 mm." | Materials and Methods, p. 405 |
| Leyenda de la escala | "Perforation Grade (0: no perforation, 1: <2mm, 2: 2-4mm, 3: >4mm)" | Figura 5, p. 407 |
| Grado global = maximo de seis direcciones | "an overall perforation grade equal to the maximum perforation grade of the six directions" | Materials and Methods, p. 405 |
| Limite del calibrador 0.2 mm | "more than 0.2 mm (lower limit of the measurement calipers used)" | Materials and Methods, p. 405 |
| Umbrales no aplicables a columna toracica | "these 'safe zone' thresholds do not apply to the thoracic spine" | Discussion, p. 411 |
| Umbrales distintos por direccion | "Safe zone threshold magnitudes are likely different for different directions of screw perforation." | Discussion, p. 411 |
| Sin umbrales de lesion en cadaver | "it was not possible to define injury thresholds for misplaced screws." | Discussion, p. 411 |
| Grados por tecnica (Tabla 3) | Ver Evidencia textual (filas Grade 0-3) | Tabla 3, p. 410 |

## Donde entra en mi tesis
Auditoria de procedencia de la escala ordinal de brecha cortical del benchmark del muestreador (cadena smith2006iliosacral -> Gertzbein 1990 / Vaccaro 1995 / Mirza 2003 -> zwingmann2009navigated). Respuestas verificadas:

- **1. Escala.** Si publica una escala de **cuatro grados numericos 0, 1, 2, 3** (no letras) con cortes 0, 2 y 4 mm: Grado 0 = 0 mm; Grado 1 = >0 y <2 mm; Grado 2 = >2 y <4 mm; Grado 3 = >4 mm (p. 405); la Figura 5 la rotula "0: no perforation, 1: <2mm, 2: 2-4mm, 3: >4mm" (p. 407). Es la forma 0 / <2 / 2-4 / >4 mm. Se aplica por separado a **seis direcciones** (anterior, lateral, medial, inferomedial, inferolateral, superior); las dos primeras son paraespinales y las cuatro ultimas hacia el espacio neural (Figs. 1-4). **No se presenta como propia**: "The thresholds reported in prior studies were used" con citas 16 (Gertzbein & Robbins, Spine 1990) y 42 (Vaccaro et al., JBJS Am 1995;77:1200-6, Part II). Las letras A/B/C que aparecen en la Tabla 3 son grupos de Tukey, no grados. La asignacion de valores exactamente iguales a 2.0 o 4.0 mm: NO ENCONTRADO EN EL PDF.
- **2. Justificacion de los cortes.** Ninguna propia. Solo la atribuye a estudios previos y, en la Discusion, resume a Gertzbein & Robbins: deficits neurologicos con perforaciones >4 mm y "a 4-mm perforation distance marks a 'safe zone.'" (p. 411). Justificacion anatomica del corte de 2 mm en este PDF: NO ENCONTRADO EN EL PDF. Los autores declaran que esos umbrales no aplican a la columna toracica, pueden ser altos para la lumbar y probablemente difieren segun direccion (p. 411).
- **3. Medicion.** Por **diseccion anatomica con calibrador**: anterior, lateral e inferolateral desde la cara lateral antes del corte; medial, inferomedial y superior desde el canal tras seccion mediosagital (pp. 404-405). Limite inferior del calibrador 0.2 mm (p. 405). La unica CT con parametros declarados es la **preoperatoria** para StealthStation: cortes de 2 mm espaciados 1.3 mm (p. 404). El abstract dice que los especimenes se examinaron con radiografias y CT, pero el protocolo y el grosor de corte de una CT postoperatoria: NO ENCONTRADO EN EL PDF. Resultados de brecha medidos en CT: NO ENCONTRADO EN EL PDF.
- **4. Distribuciones.** Tabla 3 (p. 410), orden FluoroNav multi / FluoroNav single / fluoroscopia estandar / StealthStation: Grado 0 = 62 (89%) / 31 (31%) / 75 (80%) / 70 (95%); Grado 1 = 2 (3%) / 5 (5%) / 8 (9%) / 0 (0%); Grado 2 = 4 (6%) / 21 (21%) / 5 (5%) / 1 (1%); Grado 3 = 2 (3%) / 42 (42%) / 6 (6%) / 3 (4%); todas con P = 0.000. Magnitudes por direccion en Tabla 4 (p. 411). Todo es cadaver toracico; nada pelvico ni iliosacro.
- **5. Tolerancias.** Registro de StealthStation hasta intervalo de confianza <2 mm (p. 404); limite del calibrador 0.2 mm (p. 405); citas de terceros: modelo geometrico con tolerancia de 0 mm y 0 grados en T5 a 3.8 mm y 12.7 grados en L5 (ref. 31, p. 408; el PDF imprime "T3.8 mm"); error de punta de 0.97 mm y de trayectoria de 2.7 grados (ref. 15, p. 410); exactitud de sistemas basados en CT de 1 mm y 1.2 mm (refs. 28 y 17, p. 411). Angulos de trayectoria medidos en este estudio: NO ENCONTRADO EN EL PDF.

## Dudas para el asesor
- Mirza 2003 es el primer eslabon leido donde la escala aparece literalmente como cuatro grados 0-3 con cortes 2 y 4 mm, pero la atribuye a Gertzbein 1990 (que tiene seis tramos) y a Vaccaro 1995 Part II (no leido). Se cita Mirza como la codificacion de cuatro grados y se mantiene la frase de "convencion geometrica"?
- Los intervalos del paper son abiertos en 2 y 4 mm (">2 mm but <4 mm"), pero el rango medial llega a 2.0 mm (Tabla 4). El muestreador necesita decidir a que grado van los bordes exactos: el paper no lo define.
- La escala se calibra contra medicion por calibrador en diseccion (resolucion 0.2 mm), no contra CT. Transferir sus cortes a brechas detectadas en CT postoperatoria (zwingmann2009navigated) asume una resolucion que la fuente no tenia (implicancia #67).
- Inconsistencias internas verificables: Tabla 3 "Surgeon A perfect screws 31 (91%)" para FluoroNav multi con 35 tornillos (Tabla 1); inferolateral estandar "range, 1–5.1 mm" en texto (p. 408) frente a "1.7–5.1" en Tabla 4; "inferolaterally (15%)" en Discusion (p. 408) frente a 13 (14%) en Tabla 3.

## Evidencia textual

Orden de columnas en Tablas 1-5 salvo indicacion: FluoroNav Multi-reference / FluoroNav Single-reference / Standard Fluoroscopy / Stealth Station.

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Revista y paginas | "SPINE Volume 28, Number 4, pp 402–413" | Encabezado, p. 402 |
| Fecha de aceptacion | "Acceptance date: September 3, 2002." | Nota al pie, p. 402 |
| Diseno: cuatro tecnicas | "accuracy of thoracic vertebral body screw placement using four different intraoperative imaging techniques" | Abstract (Study Design), p. 402 |
| 337 tornillos, dos cirujanos | "two experienced surgeons placed 337 vertebral body screws" | Abstract (Methods), p. 402 |
| 20 especimenes | "in 20 human cadaver thoracic spine specimens" | Abstract (Methods), p. 402 |
| Modalidades de examen | "examined with radiographs, computed tomography, and anatomic dissection to determine screw position" | Abstract (Methods), p. 402 |
| Perforacion mas frecuente lateral | "Screw perforation occurs most frequently in the lateral direction." | Abstract (Results), p. 402; Key Points, p. 412 |
| Tasa previa de perforacion 16-54% | "perforate the cortical margins of the pedicle at a rate ranging from 16% to 54%" | Introduction, p. 403 |
| Unidad de observacion | "The observational unit was the placement and position of one pedicle screw." | Materials and Methods, p. 403 |
| Fase 1: 12 especimenes | "12 thoracic spine cadaver specimens were assigned randomly to two groups" | Materials and Methods, p. 403 |
| Fase 1: 6 + 6 | "six specimens to standard fluoroscopy and six specimens to FluroNav" | Materials and Methods, p. 403 |
| FluoroNav version 2.2, referencia en T1 | "software version 2.2) with a single reference marker positioned at the T1 vertebra" | Materials and Methods, p. 403 |
| Fase 2: 8 especimenes | "eight specimens were randomly assigned to two groups" | Materials and Methods, p. 403 |
| Fase 2: 4 + 4 | "four specimens to FluoroNav with the reference marker positioned at the surgical level" | Materials and Methods, p. 403 |
| FluoroNav version 2.3.2 | "Surgical Navigation Technologies, software version 2.3.2)" | Materials and Methods, p. 403 |
| StealthStation version Mach 3.0.5 | "software version Mach 3.0.5" | Materials and Methods, p. 403 |
| Secuencia aleatoria 1-12 | "used to create a random sequence of numbers from 1 to 12" | Materials and Methods, p. 403 |
| Especimenes con costillas | "10 cm of rib retained on each side, and intact parietal pleura" | Specimen Preparation, p. 403 |
| Fluoroscopio | "a standard fluoroscope (Model 9600; Orthopedic Equipment Corporation" | Standard Fluoroscopy, p. 403 |
| Sin laminotomia | "Neither surgeon performed a laminectomy or laminotomy for pedicle palpation." | Standard Fluoroscopy, p. 403 |
| Entrenamiento FluoroNav | "one practice session on plastic bone models and two practice sessions on human cadavers" | FluoroNav: Single Reference, p. 404 |
| Multi-referencia: un nivel arriba y abajo | "placed a pedicle screw one level above the array level" | FluoroNav: Multiple References, p. 404 |
| CT preoperatoria StealthStation | "helical Elscint scan with 2-mm-thick slices spaced 1.3 mm apart" | Stealth Station, p. 404 |
| Tolerancia de registro <2 mm | "until the 'registration confidence interval' was less than 2 mm" | Stealth Station, p. 404 |
| Dosimetros | "dosimeters were placed on the specimen, the surgeon's dominant hand, and the surgeon's waist" | Data Collection, p. 404 |
| Medicion por calibrador (externa) | "exposed screws in the anterior, lateral, and inferolateral directions using calipers" | Data Collection, p. 404 |
| Medicion tras corte mediosagital | "cut the specimen in half through the midsagittal plane, and measured perforation magnitudes" | Data Collection, p. 404 |
| Seis direcciones | "Perforation magnitude measured in six directions." | Figura 1, p. 404 |
| Espacio neural: medicion radial | "measured in the radial direction using the pedicle as the center" | Figura 2, p. 405 |
| Definicion tornillo perfecto | "threads, core, and tip of the screw are completely contained within the cortical margins" | Classification Accuracy, p. 404 |
| Definicion airball | "The screw shaft is completely out of the thoracic vertebral body" | Classification Accuracy, p. 404 |
| Definicion perforacion anterior | "maximal distance in the sagittal plane between the screw tip and the point of exit" | Classification Accuracy, p. 404 |
| Definicion perforacion lateral | "maximal distance in the coronal plane between the lateral cortex of the vertebra" | Classification Accuracy, p. 404 |
| Definicion inferolateral | "penetrates the lateral half of the inferior pedicle quadrant" | Classification Accuracy, p. 405 |
| Inferolateral medida antes del corte | "measured from the lateral aspect of the vertebral column before specimen sagittal sectioning" | Classification Accuracy, p. 405 |
| Definicion inferomedial | "penetrates the medial half of the inferior pedicle quadrant" | Classification Accuracy, p. 405 |
| Inferomedial medida desde el canal | "measured from within the spinal canal after sectioning of the specimens" | Classification Accuracy, p. 405 |
| Definicion medial | "Medial perforation distance is the maximal distance in the coronal plane" | Classification Accuracy, p. 405 |
| Definicion superior | "penetrates the cortical margin of the pedicle in the superior quadrant" | Classification Accuracy, p. 405 |
| Segmento expuesto costilla/apofisis: longitud | "The distance measurement for the perforation is the length of the screw segment" | Classification Accuracy, p. 405 |
| Limite del calibrador 0.2 mm | "more than 0.2 mm (lower limit of the measurement calipers used)" | Classification Accuracy, p. 405 |
| Segmentos expuestos = seguros | "These were considered safe perforations with a low risk for clinical consequences." | Classification Accuracy, p. 405 |
| Seis grados por tornillo | "Six perforation severity grades were assigned to each screw" | Screw Perforation Grade, p. 405 |
| Umbrales heredados | "The thresholds reported in prior studies were used: Grade 0 for 0 mm" | Screw Perforation Grade, p. 405 |
| Grado 1 | "Grade 1 for a perforation distance greater than 0 mm but less than 2 mm" | Screw Perforation Grade, p. 405 |
| Grado 2 | "Grade 2 for a perforation distance greater than 2 mm but less than 4 mm" | Screw Perforation Grade, p. 405 |
| Grado 3 (superindices 16, 42) | "Grade 3 for a perforation distance greater than 4 mm." | Screw Perforation Grade, p. 405 |
| Ref. 16 | "Gertzbein SD, Robbins SE. Accuracy of pedicular screw placement in vivo." | References, p. 413 |
| Ref. 42 (titulo) | "Placement of pedicle screws in the thoracic spine: Part II." | References, p. 413 |
| Ref. 42 (revista) | "J Bone Joint Surg [Am] 1995;77:1200–6." | References, p. 413 |
| Segmento expuesto graduado por distancia lateral | "assigned a perforation grade based on the lateral perforation distance" | Screw Perforation Grade, p. 405 |
| <0.2 mm = grado 0 | "lateral perforation grade of 0 if the lateral perforation distance was less than 0.2 mm" | Screw Perforation Grade, p. 405 |
| Grado global = maximo | "an overall perforation grade equal to the maximum perforation grade of the six directions" | Screw Perforation Grade, p. 405 |
| Grado 0 no implica perfecto | "Grade 0 screws, however, were not classified as perfect if they had exposed segments" | Screw Perforation Grade, p. 405 |
| Score de severidad = suma | "a perforation severity score equal to the sum of the six directional perforation grades" | Screw Perforation Severity Score, pp. 405-406 |
| Score maximo 18 | "ranging from 0 to a possible maximum of 18." | Figuras 6 y 7, pp. 408-409 |
| Lineas de 2 y 4 mm | "The horizontal lines are the 2-mm and 4-mm mark boundary lines" | Figuras 3 y 4, pp. 406-407 |
| Origen de las lineas | "for perforation severity grading schemes reported in prior studies of pedicle screw position." | Figuras 3 y 4, pp. 406-407 |
| Leyenda de grados | "Perforation Grade (0: no perforation, 1: <2mm, 2: 2-4mm, 3: >4mm)" | Figura 5, p. 407 |
| Estadistica: ANOVA | "analysis of variance (ANOVA) for unbalanced groups (alpha = 0.05)" | Statistical Analysis, p. 406 |
| Estadistica: chi cuadrado | "P values for χ2 comparisons across the four groups (alpha = 0.05) are presented." | Statistical Analysis, p. 406 |
| Presentacion sin esquema de grados | "quantitative comparison of the imaging systems without an arbitrary grading scheme" | Statistical Analysis, p. 406 |
| Tiempo fluoroscopia estandar | "Standard fluoroscopy averaged 1.6 minutes per screw for insertion time" | Results, p. 406 |
| Tiempo FluoroNav single | "3.3 minutes (2.1 × standard fluoroscopy) for FluroNav—single reference" | Results, p. 406 |
| Tiempo FluoroNav multi | "3.7 minutes (2.3 × standard fluoroscopy) for FluroNav—multiple reference" | Results, p. 406 |
| Tiempo StealthStation | "6.8 minutes (5.6 × standard fluoroscopy) for Stealth Station." | Results, p. 406 |
| Radiacion especimen, estandar | "121 mrem for standard fluoroscopy" | Results (Radiation Exposure), p. 406 |
| Radiacion especimen, single | "44 mrem (0.36 × standard fluoroscopy) for FluroNav—single reference" | Results, p. 406 |
| Radiacion especimen, multi | "2317 mrem (19 × standard fluoroscopy) for FluroNav—multiple reference" | Results, p. 406 |
| Radiacion especimen, Stealth | "1833 mrem (15 × standard fluoroscopy) for Stealth Station." | Results, p. 406 |
| Radiacion cuerpo del cirujano | "minimal measurable exposure (1 mrem) was recorded for all the fluoroscopy systems" | Results, p. 406 |
| Mano cirujano A | "Surgeon A had 1 mrem of hand exposure per procedure with standard fluoroscopy" | Results, p. 406 |
| Mano cirujano A (resto) | "4 mrem with FluroNav—multiple reference, and 0 mrem with Stealth Station." | Results, p. 407 |
| Mano cirujano B | "Surgeon B had 31 mrem of hand exposure per procedure with standard fluoroscopy" | Results, p. 407 |
| Mano cirujano B (resto) | "3 mrem with FluroNav—multiple reference, and 0 mrem with Stealth Station." | Results, p. 407 |
| Single: peor en perfectos y grado 0 | "FluroNav—single reference had the lowest rate of perfect screws" | Results (Accuracy), p. 407 |
| Sin perforacion superior | "No perforations occurred in the superior quadrant of the pedicle" | Results, p. 408 |
| Medial solo en estandar | "Medial perforations occurred only in the standard Fluoroscopy group (5%)" | Results, p. 408 |
| Magnitud medial | "averaged 1.2 mm per perforation (range, 0.5–2 mm)." | Results, p. 408 |
| Inferolateral estandar 14% | "higher rate of inferolateral perforation (14%) than FluroNav—multiple reference (0%)" | Results, p. 408 |
| Inferolateral Stealth 0%, single 67% | "and Stealth Station (0%), but not as high as that for FluroNav—single reference (67%)" | Results, p. 408 |
| Magnitud inferolateral estandar | "Inferolateral perforations in the standard fluoroscopy group averaged 3.2 mm (range, 1–5.1 mm)." | Results, p. 408 |
| Segmento expuesto Stealth 30% | "The Stealth Station group had a 30% rate of screws with an exposed surface" | Results, p. 408 |
| Segmento expuesto otros | "rates of 19% for the standard fluoroscopy group, 13% for the FluorNav—multiple reference" | Results, p. 408 |
| Segmento expuesto single | "and 67% for the FluorNav—single reference group." | Results, p. 408 |
| Equivalencia de tres grupos | "groups were equivalent in their rates of perfect screws, airball screws" | Results, p. 408 |
| Sin efecto por cirujano | "Analyzing the screw position data by surgeon did not change the differences" | Results, p. 408 |
| T1: especimenes | "Total number of specimens 4 6 6 4" | Tabla 1, p. 409 |
| T1: % mujeres | "Specimen gender (% female) 50% 100% 67% 50%" | Tabla 1, p. 409 |
| T1: procedimientos | "Total number of procedures 8 12 12 8" | Tabla 1, p. 409 |
| T1: tornillos | "Total number of screws 70 99 94 74" | Tabla 1, p. 409 |
| T1: edad | "77 ± 6 (52–102) 77 ± 9 (66–89) 90 ± 7 (83–97) 68 ± 20 (36–98)" | Tabla 1, Specimen age (y), p. 409 |
| T1: nivel toracico | "4.9 ± 2.6 (1–9) 4.7 ± 2.5 (1–9) 4.4 ± 2.3 (1–8) 5.2 ± 2.8 (1–10)" | Tabla 1, Thoracic level, p. 409 |
| T1: diametro (mm) | "5.6 ± 0.5 (5–6) 5.3 ± 0.5 (5–6) 5.4 ± 0.5 (5–6) 5 ± 0.7 (4–6)" | Tabla 1, Screw diameter, p. 409 |
| T1: longitud (mm) | "38.4 ± 3.8 (30–45) 35.2 ± 3.5 (30–40) 41.6 ± 4.4 (35–50) 40.1 ± 3.2 (35–45)" | Tabla 1, Screw length, p. 409 |
| T1: min por tornillo | "3.7 ± 1.8 (2–8) 3.3 ± 1.5 (2–6) 1.6 ± 0.8 (1–3) 6.8 ± 2.2 (4–10)" | Tabla 1, Time per screw, p. 409 |
| T1: min por procedimiento | "32.6 ± 11.4 (22–60) 34.6 ± 9.1 (23–56) 18.6 ± 1.9 (16–23) 65.1 ± 18.3 (48–110)" | Tabla 1, p. 409 |
| T1 cirujano A: tornillos | "Number of screws 35 49 47 37" | Tabla 1, Surgeon A, p. 409 |
| T1 cirujano A: diametro | "5.5 ± 0.6 (5–6) 5.1 ± 0.3 (5–6) 5.3 ± 0.5 (5–6) 5.5 ± 0.5 (5–6)" | Tabla 1, Surgeon A, p. 409 |
| T1 cirujano A: longitud | "38.7 ± 3.5 (35–45) 34.8 ± 2.7 (30–40) 40.1 ± 3.4 (35–45) 39.9 ± 3.4 (35–45)" | Tabla 1, Surgeon A, p. 409 |
| T1 cirujano A: min por tornillo | "4.1 ± 1.9 (2–8) 3.5 ± 1.5 (2–6) 1.6 ± 0.8 (1–3) 7.6 ± 2.3 (5–12)" | Tabla 1, Surgeon A, p. 409 |
| T1 cirujano A: min por procedimiento | "36.3 ± 14.2 (25–60) 37.3 ± 10.2 (25–56) 18.1 ± 1.8 (16–21) 75.8 ± 19.3 (58–110)" | Tabla 1, Surgeon A, p. 409 |
| T1 cirujano B: tornillos | "Number of screws 35 50 47 37" | Tabla 1, Surgeon B, p. 409 |
| T1 cirujano B: diametro | "5.7 ± 0.4 (5–6) 5.5 ± 0.5 (5–6) 5.5 ± 0.5 (5–6) 4.5 ± 0.6 (4–6)" | Tabla 1, Surgeon B, p. 409 |
| T1 cirujano B: longitud | "38.0 ± 4.1 (30–45) 35.6 ± 4.1 (30–40) 43.2 ± 4.7 (35–50) 40.4 ± 3 (35–45)" | Tabla 1, Surgeon B, p. 409 |
| T1 cirujano B: min por tornillo | "3.3 ± 1.5 (2–7) 3.2 ± 1.1 (2–5) 1.6 ± 0.9 (1–3) 5.9 ± 1.8 (4–10)" | Tabla 1, Surgeon B, p. 409 |
| T1 cirujano B: min por procedimiento | "28.9 ± 5.7 (22–36) 32 ± 6.9 (23–46) 19.1 ± 1.9 (17–23) 54.4 ± 8.4 (48–70)" | Tabla 1, Surgeon B, p. 409 |
| T1: definicion de procedimiento | "One procedure consists of 8 screws each in the FluoroNav single reference" | Pie de Tabla 1, p. 409 |
| T1: 9 tornillos en multi y Stealth | "9 screws each in the FluoroNav multiple references and Stealth Station groups." | Pie de Tabla 1, p. 409 |
| T2: tornillos por especimen | "Number of screws per specimen 17.5 16.5 15.7 18.5" | Tabla 2, p. 410 |
| T2: tornillos por procedimiento | "Number of screws per procedure 8.8 8.3 7.8 9.3" | Tabla 2, p. 410 |
| T2: especimen (mrem) | "2317 ± 482 (1510–2690) 44 ± 16 (30–80) 121 ± 20 (100–150) 1833 ± 423 (1440–2550)" | Tabla 2, p. 410 |
| T2: cuerpo del cirujano | "1 ± 0 (1–1) 1 ± 0 (1–1) 1 ± 0 (1–1) 0 —" | Tabla 2, p. 410 |
| T2: mano del cirujano | "3.3 ± 4.0 (1–10) 1 ± 0 (1–1) 16.0 ± 22 (1–60)* 0 —" | Tabla 2, p. 410 |
| T2: mano cirujano A | "3.6 ± 4.1 (1–10) 1 ± 0 (1–1) 1 ± 0 (1–1) 0 —" | Tabla 2, p. 410 |
| T2: mano cirujano B | "3.1 ± 3.8 (1–10) 1 ± 0 (1–1) 31.0 ± 22.7 (1–60)* 0 —" | Tabla 2, p. 410 |
| T3: perfectos | "Perfect screws 60 (86%) 31 (31%) 70 (74%) 51 (69%) 0.000" | Tabla 3, p. 410 |
| T3: airball | "Airball screws 1 (1.4%) 26 (26%) 0 (0%) 3 (4%) 0.000" | Tabla 3, p. 410 |
| T3: pleural | "Pleural perforation 1 (1.4%) 7 (7%) 0 (0%) 0 (0%) 0.003" | Tabla 3, p. 410 |
| T3: medial | "Medial perforation 0 (0%) 0 (0%) 5 (5%) 0 (0%) 0.004" | Tabla 3, p. 410 |
| T3: inferomedial | "Inferomedial perforation 3 (4%) 1 (1%) 0 (0%) 0 (0%) 0.051" | Tabla 3, p. 410 |
| T3: inferolateral | "Inferolateral perforation 0 (0%) 66 (67%) 13 (14%) 0 (0%) 0.000" | Tabla 3, p. 410 |
| T3: superior | "Superior perforation 0 (0%) 0 (0%) 0 (0%) 0 (0%) —" | Tabla 3, p. 410 |
| T3: anterior | "Anterior perforation 2 (3%) 27 (27%) 2 (2%) 3 (4%) 0.000" | Tabla 3, p. 410 |
| T3: lateral | "Lateral perforation 3 (4%) 37 (37%) 2 (2%) 4 (5%) 0.000" | Tabla 3, p. 410 |
| T3: expuesto costilla/TP | "Exposed between rib & TP 9 (13%) 66 (67%) 18 (19%) 22 (30%) 0.000" | Tabla 3, p. 410 |
| T3: Grado 0 | "Grade 0 perforation 62 (89%) 31 (31%) 75 (80%) 70 (95%) 0.000" | Tabla 3, p. 410 |
| T3: Grado 1 | "Grade 1 perforation 2 (3%) 5 (5%) 8 (9%) 0 (0%) 0.000" | Tabla 3, p. 410 |
| T3: Grado 2 | "Grade 2 perforation 4 (6%) 21 (21%) 5 (5%) 1 (1%) 0.000" | Tabla 3, p. 410 |
| T3: Grado 3 | "Grade 3 perforation 2 (3%) 42 (42%) 6 (6%) 3 (4%) 0.000" | Tabla 3, p. 410 |
| T3: perfectos cirujano A | "Surgeon A perfect screws 31 (91%) 15 (31%) 37 (79%) 29 (78%) 0.000" | Tabla 3, p. 410 |
| T3: perfectos cirujano B | "Surgeon B perfect screws 28 (80%) 16 (32%) 33 (70%) 22 (60%) 0.000" | Tabla 3, p. 410 |
| T3: airball cirujano A | "Surgeon A airball screws 0 (0%) 5 (10%) 0 (0%) 2 (5%) 0.042" | Tabla 3, p. 410 |
| T3: airball cirujano B | "Surgeon B airball screws 1 (3%) 21 (42%) 0 (0%) 1 (3%) 0.000" | Tabla 3, p. 410 |
| T3: grado medio | "0.23 ± 0.68 (0.07–0.39) 1.8 ± 1.3 (1.5–2.0) 0.38 ± 0.86 (0.21–0.56) 0.15 ± 0.63 (0.0–0.30)" | Tabla 3, Screw Perforation Grade, p. 410 |
| T3: score medio | "0.23 ± 0.68 (0.07–0.39) 3.3 ± 3.2 (2.6–3.9) 0.45 ± 1.1 (0.22–0.67) 0.24 ± 1.1 (0.0–0.49)" | Tabla 3, Perforation Severity Score, p. 410 |
| T3: definicion de perfecto | "screws that had no metal exposed out of any of the bony margins" | Pie de Tabla 3, p. 410 |
| T3: segmento expuesto como "seguro" | "We considered this a "safe" protrusion, away from neural structures" | Pie de Tabla 3, p. 410 |
| T3: letras = grupos Tukey | "The superscript letters A, B, and C mark related groups for pair-wise contrasts" | Pie de Tabla 3, p. 410 |
| T4: medial (mm) | "Medial: 0; 0; 5, 1.2 ± 0.8 (0.5–2.0); 0" | Tabla 4, p. 411 |
| T4: inferomedial (mm) | "Inferomedial: 3, 2.8 ± 1.2 (1.9–4.2); 1, 3.1; 0; 0" | Tabla 4, p. 411 |
| T4: inferolateral (mm) | "Inferolateral: 0; 66, 4.1 ± 1.6 (0.1–8.4); 13, 3.2 ± 1.5 (1.7–5.1); 0" | Tabla 4, p. 411 |
| T4: lateral (mm) | "Lateral: 3, 2.6 ± 1.1 (1.7–3.8); 37, 4.4 ± 1.7 (1.4–8.0); 2, 4.5 ± 2.2 (3.0–6.1); 4, 5.0 ± 2.1 (2.5–7.5)" | Tabla 4, p. 411 |
| T4: superior (mm) | "Superior: 0; 0; 0; 0" | Tabla 4, p. 411 |
| T4: anterior (mm) | "Anterior: 2, 12.0 ± 2.8 (10–14); 27, 4.5 ± 1.6 (1.7–9.5); 2, 7.7 ± 0.4 (7.4–7.9); 3, 8.9 ± 6.1 (2.0–13.6)" | Tabla 4, p. 411 |
| T4: expuesto costilla/TP (mm) | "Exposed: 9, 18.7 ± 7.9 (6–27.9); 66, 19.4 ± 9.4 (3.3–36.2); 18, 12.1 ± 7.3 (2.2–26.2); 22, 15.7 ± 6.5 (8.2–34.8)" | Tabla 4, p. 411 |
| T4: solo tornillos perforados | "calculated using only screws that perforated in the direction marked by each row." | Pie de Tabla 4, p. 411 |
| T5: potencia | "Sample size calculations are for alpha = 0.05 and power = 0.80." | Pie de Tabla 5, p. 411 |
| T5: columnas | "Standard Fluoroscopy vs. FluoroNav Multi-reference / vs. Stealth Station / FluoroNav Multi-reference vs. Stealth Station" | Tabla 5, p. 411 |
| T5: perfectos | "Frequency of perfect screws 363 screws 437 screws 96 screws" | Tabla 5, p. 411 |
| T5: grado 0 | "Frequency of grade 0 screws 597 screws 77 screws 154 screws" | Tabla 5, p. 411 |
| T5: grado medio | "Average perforation grade 396 screws 163 screws 1,069 screws" | Tabla 5, p. 411 |
| T5: score medio | "Average perforation severity score 271 screws 445 screws 60,445 screws" | Tabla 5, p. 411 |
| Tolerancia geometrica (ref. 31) | "maximum permissible error tolerances ranged from 0 mm and 0° at T5 to T3.8 mm" | Discussion, p. 408 |
| Tolerancia angular en L5 (ref. 31) | "and 12.7° at L5." | Discussion, p. 408 |
| Tasas de desvio con fluoroscopia | "even experienced surgeons misdirect the screws medially (5%) and inferolaterally (15%)" | Discussion, p. 408 |
| Magnitudes promedio | "averaging 1 mm in the medial direction and 3 mm in the inferolateral direction" | Discussion, p. 408 |
| Error de sonda (ref. 15) | "mean probe tip error of 0.97 mm and a mean trajectory angle error of 2.7°" | Discussion, p. 410 |
| Single: airball y pleura | "26% of the screws completely missing the thoracic vertebral body and 7%" | Discussion, p. 411 |
| Choi (ref. 10) | "placed 106 pedicle screws from T1 to S1 in six cadavers." | Discussion, p. 411 |
| Choi: violaciones | "They noted 19 cortical violations (17.9%): 6.6% medial and 11.3% lateral." | Discussion, p. 411 |
| Exactitud CT (refs. 28, 17) | "The reported accuracy for CT-based systems is 1 mm and 1.2 mm" | Discussion, p. 411 |
| Violacion cortical 1.25% (ref. 5) | "the cortical violation rate reported is 1.25%." | Discussion, p. 411 |
| CT + fluoroscopia virtual 17.9% | "had a cortical violation rate of 17.9% in a cadaver study." | Discussion, p. 411 |
| Kim (ref. 21) | "evaluated 120 thoracic pedicle screws placed from T1 to T12 in five cadavers" | Discussion, p. 411 |
| Kim: 19.2% | "23 screws (19.2%) had cortical violations." | Discussion, p. 411 |
| Laser (ref. 34) | "cortical violation rate of 1.6% for screws placed from T5 to L5." | Discussion, p. 411 |
| Series clinicas con CT | "has a reported range of 0%, 4.6%, 5%, 8% and 8.5%." | Discussion, p. 411 |
| Gertzbein segun Mirza: serie | "described their experience with 40 patients who had 5-mm screws placed in T8–S1" | Discussion, p. 411 |
| Gertzbein segun Mirza: 72% | "They reported a 72% rate for screws with no cortical perforation" | Discussion, p. 411 |
| Gertzbein segun Mirza: 9.6% hasta 2 mm | "9.6% for screws with perforation up to 2 mm beyond the cortex" | Discussion, p. 411 |
| Gertzbein segun Mirza: 9% hasta 4 mm | "9% for screws with a perforation distance up to 4 mm beyond the cortex" | Discussion, p. 411 |
| Gertzbein segun Mirza: deficits >4 mm | "neurologic deficits in patients with screw perforation distances greater than 4 mm" | Discussion, p. 411 |
| Gertzbein segun Mirza: zona segura 4 mm | "concluded that a 4-mm perforation distance marks a "safe zone."" | Discussion, p. 411 |
| Critica: no aplica a toracica | "these "safe zone" thresholds do not apply to the thoracic spine" | Discussion, p. 411 |
| Critica: alta para lumbar | "and may be high for the lumbar spine." | Discussion, p. 411 |
| Critica: dependencia de direccion | "Safe zone threshold magnitudes are likely different for different directions of screw perforation." | Discussion, p. 411 |
| Cadaver: sin umbral de lesion | "it was not possible to define injury thresholds for misplaced screws." | Discussion, p. 411 |
| Sin patron por nivel | "The current study did not show any clear pattern of screw misplacement by vertebral level." | Discussion, p. 411 |
| Belmont (ref. 7): serie | "examined 279 pedicle screws placed at T1–T12 in 40 patients." | Discussion, p. 411 |
| Belmont: 43% por CT postoperatoria | "Using postoperative CT scans, they found 43% of the screws perforating the cortical margins" | Discussion, p. 411 |
| Aumento de radiacion 15-20x | "by 15- to 20-fold (from 44 mrem to 1833 and 2317 mrem)" | Discussion, p. 411 |
| Aumento de tiempo 2-6x | "the time required for screw placement 2- to 6-fold" | Discussion, pp. 411-412 |
| Limite anual de mano | "maximum limit for annual hand radiation exposure is 50 rem (50,000 mrem)." | Discussion, p. 412 |
| NCRP 5 rem | "is 5 rem, with cumulative exposure of 1 rem times age" | Discussion, p. 412 |
| Dosis diagnosticas (1) | "16 mrem for posteroanterior chest radiograph, 420 mrem for L-spine radiograph" | Discussion, p. 412 |
| Dosis diagnosticas (2) | "and 4000 mrem for head CT" | Discussion, p. 412 |
| Assaker (ref. 5): cuatro cadaveres | "compared pedicle screws placed with image guidance and fluoroscopy in four cadavers." | Discussion, p. 412 |
| Assaker: 13.5 vs 4 min | "for the image guidance group was 13.5 minutes, as compared with 4 minutes" | Discussion, p. 412 |
| Efecto de aprendizaje | "Figure 6 shows some learning effect for surgeon A." | Limitations, p. 412 |
| Donantes de edad avanzada | "This study used specimens from older donors." | Limitations, p. 412 |
| Costo | "The systems tested in the current protocol each cost more the $300,000 in 2001." | Limitations, p. 412 |
| Conclusion: 6x tiempo | "does not justify the 6-fold increase in procedure time" | Conclusions, p. 412 |
| Conclusion: 20x radiacion | "and the 20-fold increase in radiation exposure to the patient." | Conclusions, p. 412 |
| DOI | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Grados con letras (A/B/C/D) para la brecha | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Justificacion anatomica propia de los cortes 2 y 4 mm | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Asignacion de valores exactos 2.0 y 4.0 mm a un grado | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Protocolo o grosor de corte de CT postoperatoria | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Resultados de brecha medidos sobre CT | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Fiabilidad interobservador (kappa/ICC) de la medicion | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Cegamiento de los medidores respecto del sistema de imagen | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Angulos de trayectoria medidos en este estudio | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Artefacto metalico / volumen parcial | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Tornillo iliosacro / sacro / pelvis | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
