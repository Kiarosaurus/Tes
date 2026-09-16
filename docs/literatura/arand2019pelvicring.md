# arand2019pelvicring — 3D Statistical Model of the Pelvic Ring (variacion anatomica, CT)

- **DOI / URL:** 10.1111/joa.12928 (J. Anat. (2019) 234, pp376-383)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/arand2019pelvicring.pdf

## Que hace (3 lineas maximo)
Construye, desde 50 CT post mortem de adultos japoneses sin lesion, un modelo estadistico 3D de
superficie del anillo pelvico completo (sacro + dos innominados; media global, masculina y femenina),
lo analiza con PCA (PC1-PC5) y mediciones pelvicas, y calcula aparte un modelo MEDIO de valores de gris (HU) por voxel.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; es anatomia computacional descriptiva. Restricciones que
importan para esta tesis:
- **Si hay densidad, pero es un promedio poblacional cualitativo de HU, no un mapa de densidad
  mineral.** Se calcula *"The mean HU value for each voxel"* (Methods — Modelling of 3D statistical
  bone mass, p.377) sobre una grilla de 0.5 mm deformada por TPS. Los autores lo llaman *"an indication
  of bone quality utilizing grey values"* (Abstract, p.376). El paper no reporta ningun valor numerico
  de HU, ninguna calibracion densitometrica ni la dispersion por voxel; el resultado es solo visual
  (Fig. 8) y verbal (alto / intermedio / bajo).
- **Poblacion intacta y envejecida:** *"uninjured Japanese adults"* (Abstract), post mortem, edad media
  74.9 anos. No se menciona exclusion ni presencia de implantes o metal.
- **No propone el modelo de gris como restriccion para colocar tornillos**; solo dice que aporta
  informacion para *"preoperative planning and screw positioning"* (Discussion, p.382).
- **Corredores solo cualitativos:** PC3 y PC4 afectan el diametro / disponibilidad del corredor
  trans-sacro S1, pero las cifras del corredor se remiten a Wagner et al. 2014 y 2017a.
- No declara que el modelo, la malla o el mapa de gris esten disponibles publicamente.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito (varianza PC1-PC5; patron cualitativo de HU: ala sacra baja, cuerpo S1 intermedio, borde pelvico alto)
- [ ] baseline de comparacion
- [x] solo contexto (variabilidad interindividual del anillo pelvico y su efecto sobre el corredor S1)

## Numeros que cito de este paper
Ver la tabla completa en "Evidencia textual". Respuestas a los 5 puntos de verificacion:

1. **Densidad:** SI construye un modelo de distribucion de valores de gris (HU), separado del
   modelo de forma: *"A separate statistical model of the grey value distribution"* (Abstract). Es la
   media de HU por voxel en el espacio de la forma media (grilla isotropica de 0.5 mm deformada por TPS
   con los landmarks homologos), siguiendo el metodo de Kamer 2016. Patron: HU mas altos entre la
   articulacion sacroiliaca y el acetabulo a lo largo del borde pelvico; intermedios periacetabulares y en el
   cuerpo sacro S1; bajos en el ala sacra (el "alar void"), la fosa iliaca y las ramas pubicas cerca de la
   sinfisis. Segun los autores, no hay diferencias sexuales relevantes (sin test reportado). No hay HU
   numericos, calibracion a BMD ni varianza.
2. **Corredores / tornillos:** solo el corredor trans-sacro S1, de forma cualitativa (PC3: disminuye el
   diametro con el sacro mas anterior; PC4: la posicion cranio-caudal del sacro influye en su tamano y
   disponibilidad). En la Discusion se menciona la fijacion con tornillo iliosacro y barra trans-sacra
   citando a Wagner. Ver tabla para S2, dismorfismo, zonas seguras y la regla de 5 mm.
3. **Cohorte:** n=50 (30 H, 20 M), japoneses, post mortem, edad media 74.9 (26-90, DE 16.9); se
   excluyen patologias oseas radiograficas distintas de osteopenia/osteoporosis/osteoartritis. GE
   LightSpeed VCT, 120 kVp, kernel STANDARD, voxel isotropico de 0.63 mm. La segmentacion usa una
   herramienta por umbral (Amira 6.0.0) y luego control/correccion manual corte a corte en axial.
4. **Variacion:** PC1 tamano 20.4% (20.39%), PC2 forma 14.1% (14.13%), PC3 posicion A-P del sacro 11.4%
   (11.39%), PC4 posicion cranio-caudal del sacro 8.9% (8.85%), PC5 morfologia sacra 6.9%. PC1-PC5 suman
   61.7% en Results y 61.64% en Conclusion (pequena inconsistencia interna). Conclusion: variabilidad
   interindividual "very high". Diferencias sexuales: solo la distancia AIIS es significativa (P = 0.03).
5. **Disponibilidad publica:** ver tabla.

## Donde entra en mi tesis
- **Problem statement (main.tex:52) y Objetivo 2 (main.tex:78):** se cita como fuente de
  "bone density maps" / "pelvic density representations". El paper da un modelo MEDIO poblacional de
  valores de gris, no calibrado, cualitativo y no publicado. Sirve para justificar que la masa osea
  pelvica es heterogenea de forma sistematica (ala sacra baja frente a cuerpo S1 intermedio), y por eso
  conviene un muestreador sensible a la densidad. No es la fuente del mapa que usa el muestreador, que
  trabaja sobre el HU del CT de cada paciente (CTPelvic1K). La regla de 5 mm y la viabilidad del corredor
  oseo no salen de este paper.
- **Rol en _index ("el corredor no es fijo"):** tiene soporte cualitativo en PC3/PC4 y en la Discusion.
  El sacro cambia de posicion frente a los innominados, y eso afecta el tamano y la accesibilidad del
  corredor trans-sacro S1. Encaja con la restriccion de la tesis a S1.

## Dudas para el asesor
- Conviene mantener `arand2019pelvicring` en la frase de "bone density maps"? Otra opcion es
  reformularla: "density-aware constraints, motivated by the systematic heterogeneity of pelvic bone mass
  (e.g., low grey values in the sacral ala) \citep{arand2019pelvicring}".
- El modelo de gris sale de pelvis ancianas, japonesas, post mortem y sin lesion. Es aceptable como
  motivacion cualitativa para CLINIC-metal (con implantes y fracturas), sabiendo que no se usara como
  prior numerico?
- La fuente metodologica del mapa de gris es Kamer 2016, y el analogo sacro con corredores es Wagner
  et al. 2014. Vale la pena leer Wagner 2014 si la tesis va a defender un mapa de densidad sacro?

## Evidencia textual

| Cifra / dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| DOI 10.1111/joa.12928; J. Anat. 2019, 234, pp376-383 | "J. Anat. (2019) 234, pp376--383 doi: 10.1111/joa.12928" | Encabezado, p.376 |
| Aceptado 25 nov 2018; online 21 dic 2018 | "Accepted for publication 25 November 2018" | p.376 (pie de columna) |
| Objetivo: modelo estadistico 3D del anillo pelvico completo | "generate a 3D statistical model of the entire pelvic ring" | Abstract, p.376 |
| Modelo de densidad SEPARADO del de forma (valores de gris HU) | "A separate statistical model of the grey value distribution" | Abstract, p.376 |
| Proposito del modelo de gris: masa osea / calidad osea | "an indication of bone quality utilizing grey values" | Abstract, p.376 |
| Radiodensidad como descriptor cuantitativo | "grey values as a quantitative description of radiodensity" | Abstract, p.376 |
| Metodo de masa osea tomado de Kamer 2016 | "according to a method described by Kamer et al." | Methods — Modelling of 3D statistical bone mass, p.377 |
| Grilla de referencia isotropica de 0.5 mm | "an isotropic voxel edge length of 0.5 mm" | Methods — Modelling of 3D statistical bone mass, p.377 |
| Grilla deformada a cada superficie con TPS | "the reference grid was warped to each surface model using TPS transformation" | Methods — Modelling of 3D statistical bone mass, p.377 |
| Estadistico calculado: media de HU por voxel | "The mean HU value for each voxel was calculated" | Methods — Modelling of 3D statistical bone mass, p.377 |
| Visualizacion en cortes de 3 planos y 3D | "visualized as CT slices in all three planes" | Methods — Modelling of 3D statistical bone mass, p.377 |
| Patron de gris distintivo y simetrico | "a distinct and symmetrical pattern of grey value distribution" | Results, p.381 |
| HU mas altos: entre articulacion SI y acetabulo, borde pelvico | "Areas of highest CT grey values were located between the sacro-iliac joint and the acetabulum" | Results, p.381 |
| Masa osea intermedia: periacetabular y cuerpo sacro S1 | "Regions of intermediate bone mass were found periacetabular" / "the area of the sacral body S1" | Results, p.381 |
| HU bajos: ala sacra, fosa iliaca, ramas pubicas cerca de sinfisis | "Low CT grey values were observed in the sacral ala" | Results, p.381 |
| HU bajos del ala sacra = "alar void" | "corresponding to the so-called alar void" | Discussion, p.382 |
| Sin diferencias sexuales relevantes en valores de gris | "without relevant sex-specific differences" | Discussion, p.382 |
| Uso sugerido: planificacion y posicionamiento de tornillos | "fracture care when considering preoperative planning and screw positioning" | Discussion, p.382 |
| Autodeclaracion de primer modelo con gris del anillo completo | "this is first study to demonstrate the generation of a CT-based 3D statistical model" | Discussion, p.382 |
| Valores numericos de HU (media, rangos por region) del modelo de gris | NO ENCONTRADO EN EL PDF | — |
| Calibracion densitometrica (fantoma) o conversion a BMD (mg/cm3) | NO ENCONTRADO EN EL PDF | — |
| Dispersion (DE/varianza) de HU por voxel en el modelo de gris | NO ENCONTRADO EN EL PDF | — |
| Test estadistico de diferencias sexuales en valores de gris | NO ENCONTRADO EN EL PDF | — |
| Cohorte n=50, japoneses adultos | "A series of 50 anonymized pelvic CT scans of Japanese adults" | Methods — CT imaging data, p.377 |
| Sujetos sin lesion | "uninjured Japanese adults" | Abstract, p.376 |
| 30 hombres, 20 mujeres, edad media 74.9 | "30 males and 20 females with a mean age of 74.9 years" | Methods — CT imaging data, p.377 |
| Rango 26-90, DE 16.9; hombres 68.4 (DE 16.4) | "(26–90 years, SD 16.9; males 68.4 years, SD 16.4" | Methods — CT imaging data, p.377 |
| Mujeres 80.3 (DE 6.7) | "females 80.3 years, SD 6.7 years" | Methods — CT imaging data, p.377 |
| CT post mortem, con aprobacion etica local | "CT scans were obtained from postmortem specimens" | Methods — CT imaging data, p.377 |
| Exclusion: patologia osea salvo osteopenia/osteoporosis/osteoartritis | "radiographic signs of bone-related pathologies other than osteopenia, osteoporosis or osteoarthritis were excluded" | Methods — CT imaging data, p.377 |
| Exclusion explicita de implantes / metal / cirugia previa | NO ENCONTRADO EN EL PDF | — |
| Escaner GE LightSpeed VCT | "A standard CT scanner (LightSpeed VCT, GE Healthcare" | Methods — CT imaging data, p.377 |
| 120 kVp y kernel GE STANDARD | "tube peak voltage of 120 kVp and the GE STANDARD reconstruction kernel" | Methods — CT imaging data, p.377 |
| Voxel isotropico de 0.63 mm en todos los scans | "The voxel size was 0.63 x 0.63 x 0.63 mm in all scans" | Methods — CT imaging data, p.377 |
| Datos en HU, formato DICOM | "CT grey values were provided in Hounsfield units (HU)" | Methods — CT imaging data, p.377 |
| Software Amira 6.0.0 | "AMIRA software (Amira version 6.0.0" | Methods — Processing of imaging data, p.377 |
| Segmentacion por umbral + correccion manual corte a corte | "threshold-based image segmentation tool and a subsequent manual slice by slice control" | Methods — Processing of imaging data, p.377 |
| Segmentacion semiautomatica, hueso por hueso | "Threshold based semi-automated segmentation performed separately" | Fig. 1 (leyenda), p.378 |
| Valor del umbral HU de segmentacion | NO ENCONTRADO EN EL PDF | — |
| Landmarks: 37 por innominado, 42 por sacro | "(37 per innominate bone, 42 per sacrum) were manually positioned" | Methods — Processing of imaging data, p.377 |
| 32 landmarks flotantes en canal y foramenes sacros | "32 additional anatomical landmarks were positioned as floating landmarks" | Methods — Processing of imaging data, p.377 |
| Control de landmarks por experto medico | "All landmarks were visually checked for accurate placement by a medical expert" | Methods — Processing of imaging data, p.377 |
| Fiabilidad inter/intra-observador de landmarks o mediciones | NO ENCONTRADO EN EL PDF | — |
| Correspondencia por TPS; alineacion Procrustes sin escala | "aligned to its reference using a non-scaled Procrustes fit" | Methods — 3D statistical surface modelling, p.377 |
| Malla innominado: 50 000 vertices, 100 000 triangulos | "50 000 vertices and 100 000 triangles per innominate bone" | Methods — 3D statistical surface modelling, p.377 |
| Malla sacro: 50 000 vertices, 100 064 triangulos | "50 000 vertices and 100 064 triangles per sacrum" | Methods — 3D statistical surface modelling, p.377 |
| Modelos medios: global, masculino y femenino | "separate male and female mean models were computed" | Methods — 3D statistical surface modelling, p.377 |
| PCA visualizada a +/-3 DE para PC1-PC5 | "Models corresponding to three SD units flanking the mean" | Methods — Analysis, p.377 |
| Mediciones: ASIS, AIIS (externas); promontorio-sinfisis, espinas isquiaticas (internas) | "The distances between the promontory and the symphysis (conjugata vera)" | Methods — Analysis, p.378 |
| Estadistica: Mann-Whitney U y Pearson (SPSS 24) | "The Mann–Whitney U-test and Pearson correlation tests were applied" | Methods — Analysis, p.378 |
| Metricas de validacion del modelo de forma (compactness, generalization, specificity, error de reconstruccion) | NO ENCONTRADO EN EL PDF | — |
| PC1-PC5 = 61.7% de la variacion total | "1st to 5th PCs constituting 61.7% of the total anatomical variation" | Results, p.378 |
| PC1-PC5 = 61.64% (cifra distinta en Conclusion) | "the first five PCs cover only 61.64% of the observed overall variation" | Conclusion, p.382 |
| PC1 tamano 20.39%, PC2 forma 14.13% | "predominantly showed size variation (20.39%) followed by shape variation (14.13%)" | Abstract, p.376 |
| PC1 = 20.4% (tamano) | "contained 20.4% of the overall anatomical variation" | Results, p.378 |
| PC2 = 14.1% (forma) | "which represented 14.1% of the total anatomical variation" | Results, p.378 |
| PC3 = 11.39%, PC4 = 8.85% (disposicion espacial del sacro) | "spatial arrangement of the sacrum to the innominate bones" / "(11.39 and 8.85%)" | Abstract, p.376 |
| PC3 = 11.4%: posicion antero-posterior del sacro | "anterior-posterior position of the sacrum in relation to the innominate bone (11.4%" | Results, p.378 |
| PC3: diametro del corredor trans-sacro S1 disminuye con sacro anterior | "the diameter of the S1 trans-sacral corridor was affected, decreasing" | Results, p.379 |
| PC4 = 8.9% | "constituting 8.9% of the total anatomical variation" | Results, p.379 |
| PC4: posicion cranio-caudal del sacro | "The sacrum varied in its cranio-caudal position relative to the innominate bone" | Results, p.379 |
| PC4: influye en tamano y disponibilidad del corredor S1 | "a clear influence of the trans-sacral corridor of S1 in terms of size and availability" | Results, p.379 |
| PC5 = 6.9%: morfologia sacra | "The 5th PC, constituting 6.9% of the total anatomical variation" | Results, p.380 |
| % de varianza de PC6 en adelante | NO ENCONTRADO EN EL PDF | — |
| Mapa de distancias H vs M, escala 0-8 mm | Escala de color "0 mm" a "8 mm" | Fig. 6, p.380 |
| Mayores desviaciones H vs M: alas iliacas, espina y tuberosidad isquiatica, ramas pubicas inferiores | "Maximum distance deviations were observed in the iliac wings" | Results, p.380 |
| Promontorio-sinfisis: 107.3 mm (H) vs 112.1 mm (M), modelos medios | "measured at 107.3 mm in the male and" / "112.1 mm in the female mean model" | Results, p.380-381 |
| Mayor diferencia sexual >10 mm: espinas isquiaticas | "The largest intersexual differences of > 10 mm were observed between the ischial spines" | Results, p.381 |
| Espinas isquiaticas 94.2 (H) vs 106.8 (M), P = 0.2 | "(94.2 mm in male, 106.8 mm in female, P = 0.2)" | Results, p.381 |
| Solo la distancia AIIS es significativa por sexo, P = 0.03 | "significantly smaller in female than in male pelves (P = 0.03)" | Results, p.381 |
| Resto de diferencias sexuales no significativas | "none of the observed sex specific differences was shown to be significant" | Results, p.381 |
| P promontorio-sinfisis = 0.12; P ASIS = 0.38 | "distance promontory – symphysis (mm), P = 0.12" / "(mm), P = 0.38 (left)" | Fig. 7 (leyenda), p.381 |
| Correlacion ASIS-AIIS r = 0.54 | "(r = 0.54, P < 0.001)" | Results, p.381 |
| Correlacion ASIS-espinas isquiaticas r = 0.42 | "(r = 0.42, P = 0.002)" | Results, p.381 |
| Modelo medio global: 111.3 / 98.4 / 237.7 / 190.0 mm (prom-sinf / espinas isq / ASIS / AIIS) | Fila "Overall mean model 111.3 98.4 237.7 190.0" | Table 1, p.381 |
| Mediana todos (DE) (IC 95%): 113.0 (11.1) (110.7-116.9); 96.6 (9.6) (95.7-101.1); 235.3 (16.0) (233.2-242.3); 189.0 (11.6) (186.7-193.2) | Fila "Median all samples SD (CI)"; en el PDF falta el simbolo entre mediana y DE | Table 1, p.381 |
| Modelo medio masculino: 107.3 / 94.2 / 234.1 / 192.6 mm | Fila "Male mean model" | Table 1, p.381 |
| Mediana hombres (DE) (IC): 108.6 (11.9) (107.5-116.4); 94.9 (9.4) (93.3-100.3); 234.6 (16.8) (229.9-242.4); 192.2* (10.6) (188.3-196.3) | Fila "Median all male samples SD (CI)" | Table 1, p.381 |
| Modelo medio femenino: 112.1 / 106.8 / 239.0 / 185.7 mm | Fila "Female mean model" | Table 1, p.381 |
| Mediana mujeres (DE) (IC): 118.8 (9.5) (112.2-121.1); 100.7 (9.7) (96.3-105.4); 236.6 (14.7) (233.2-247.0); 184.9* (12.4) (180.6-192.3) | Fila "Median all female samples SD (CI)" | Table 1, p.381 |
| Criterio de significancia de la tabla: P < 0.05 | "Values marked with * showed a significant sex-specific variation (P < 0.05)" | Table 1 (nota), p.381 |
| PC2 interpretada como variacion de forma ligada al sexo | "the 2nd PC shows predominantly sex-related shape variations" | Discussion, p.382 |
| Variacion interindividual (tamano) domina sobre la sexual | "predominance of interindividual variation, especially in size, over sex-related variation" | Discussion, p.382 |
| Talla corporal no disponible | "Although not available at the present time" | Discussion, p.382 |
| Alta variabilidad en la disposicion espacial (PC3, PC4) | "a high variability in the spatial arrangement of the three main bone structures" | Discussion, p.382 |
| Corredor S1 atribuido a Wagner: tornillo iliosacro y barra trans-sacra | "pertinent to the ilio-sacral screw and trans-sacral bar fixation" | Discussion, p.382 |
| Forma del innominado y disposicion espacial afectan el corredor | "affect the size and accessibility of the trans-sacral corridor" | Discussion, p.382 |
| Dimensiones numericas del corredor S1 en este estudio (mm) | NO ENCONTRADO EN EL PDF | — |
| Corredor S2 | NO ENCONTRADO EN EL PDF | — |
| Dismorfismo sacro | NO ENCONTRADO EN EL PDF | — |
| Zonas seguras / margen de 5 mm a cortical | NO ENCONTRADO EN EL PDF | — |
| Conclusion: variabilidad interindividual muy alta | "very high interindividual variability in size and shape" | Conclusion, p.382 |
| Modelo previo de Lamecker con 23 CT | "model of the pelvic ring based on 23 CT datasets" | Discussion, p.382 |
| Seccion explicita de limitaciones | NO ENCONTRADO EN EL PDF | — |
| Disponibilidad publica del modelo, mallas, mapa de gris o codigo | NO ENCONTRADO EN EL PDF | — |
| Financiamiento: AO Foundation y DePuy Synthes | "co-funded by the TK System of the AO Foundation" | Acknowledgements, p.382 |
