# hinsche2002fluoroscopy — Guia multiplanar fluoroscopica para tornillos sacroiliacos

- **DOI / URL:** 10.1097/00003086-200202000-00014 (el PDF no imprime DOI; tomado de `refs/raw/hinsche2002fluoroscopy.nbib`, PMID 11937873). Clin Orthop Relat Res, 2002 Feb, num. 395, pp. 135-144.
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/hinsche2002fluoroscopy.pdf

## Que hace (3 lineas maximo)
Estudio experimental prospectivo y controlado en banco: 140 tornillos canulados en S1 y S2 de 35 modelos pelvicos de PLASTICO, comparando guia de imagen asistida por computador (fluoroscopia) contra intensificador de imagen convencional.
Prueba dos brocas (guia de 2.8 mm y broca solida de 5 mm) mas una broca canulada a medida, y evalua la seguridad de cada colocacion cortando el sacro con sierra de banda.
Mide divergencia del tornillo respecto al centro de vertebra y pediculo, y tiempo de radiacion por tornillo.

## Restriccion o supuesto clave
El estudio NO es clinico y NO simula una pelvis lesionada. El montaje asume reduccion anatomica previa y ausencia de partes blandas: *"No attempt to create a fracture or displacement was made"* (Experimental Setup, p. 136), y el modelo se describe como situacion *"after anatomic reduction"* (misma frase, p. 136). Los propios autores reconocen que el plastico se desvia de la anatomia real: *"The alar slope of the plastic model seemed to be steeper and the S2 pedicle smaller than the real pelvic anatomy"* (Discussion, p. 141). Ademas, una limitacion de imagen condiciona todo el brazo convencional: *"A true lateral radiograph was not possible"* (Materials, p. 138).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 2%-15% (CITA HEREDADA, no medida aqui) | "has been reported to range between 2% and 15%, even by experienced surgeons" | Introduccion, p. 135 |
| 140 tornillos canulados, 35 modelos pelvicos | "140 cannulated screws were placed into the S1 and S2 vertebral bodies" | Abstract, p. 135 |
| 28 modelos de PLASTICO + 112 tornillos | "28 plastic pelvic models (Synthes, Oberdorf, Switzerland) were used" | Materials and Methods, p. 136 |
| 7 modelos y 28 tornillos adicionales | "28 additional screws were inserted in seven additional plastic models" | Materials and Methods, p. 136 |
| Definicion de colocacion insegura | "unsafe when the screw path perforated one of the cortices while jeopardizing neurovascular structures" | Measurements, p. 138 |
| Diametro del tornillo: 7.3 mm | "cannulated screws (7.3-mm) of the appropriate length were inserted" | Materials, p. 138 |
| Ancho medio pediculo S1: 28.48 mm | "mean width 28.48 mm (range, 28.00-28.75 mm)" | Results, p. 140 |
| Altura media pediculo S1: 24.35 mm | "mean height 24.35 mm (range, 24.00-24.93 mm)" | Results, p. 140 |
| Pediculo S2: 23.37 mm de ancho, 14.96 mm de alto | "was 23.37 mm (range, 23.11-23.96 mm) and 14.96 mm (range, 14.57-15.36 mm)" | Results, p. 140 |
| Guia 2.8 mm en S1: 12 vs 14 seguros, p = 0.142 | "12 versus 14 safe screw placements at the S1 level (p = 0.142)" | Results, p. 140 |
| Guia 2.8 mm en S2: 6 vs 13 seguros, p = 0.0046 | "six versus 13 safe screw placements (p = 0.0046)" | Results, p. 140 |
| Broca 5 mm en S1: 13 seguros en ambas tecnicas, p = 1 | "13 safe screw placements with both techniques (p = 1)" | Results, p. 140 |
| Broca 5 mm en S2: 9 vs 10 seguros, p = 0.686 | "nine (computer-assisted image guidance) versus 10 (image intensifier) safe screw placements" | Results, p. 140 |
| 93% de colocacion segura en S1 (ambas tecnicas, broca 5 mm) | "safe screw placement into the S1 vertebra was identical with both techniques (93%)" | Discussion, p. 141 |
| 71% y 64% de exito en S2 con broca 5 mm | "unacceptable low success rates of 71% with the image-intensifier technique and 64%" | Discussion, p. 142 |
| 82% de los tornillos mal colocados estaban en S2 | "18 of the 22 (82%) misplaced screws were at the S2 level" | Discussion, p. 142 |
| Tiempo de radiacion por tornillo: 4.8 s vs 10.2 s | "4.8 seconds versus 10.2 seconds; p < 0.05" | Discussion, p. 142 |
| Divergencia AP en pediculo S1: 3.98 mm vs 6.59 mm | Tabla 2, fila "Anteroposterior deviation S1 pedicle" | Table 2, p. 140 |
| Divergencia AP en pediculo S2: 2.59 mm vs 5.88 mm | Tabla 2, fila "Anteroposterior deviation S2 pedicle" | Table 2, p. 140 |

## Donde entra en mi tesis
Implicancia #12 (origen del rango 2%-15%). **Respuesta a la pregunta central: este paper NO mide ninguna tasa de malposicion clinica en pacientes.** El 2%-15% aparece solo en su Introduccion (p. 135) como cita heredada de sus referencias 5, 11, 20 y 24 (Ebraheim 1993; Keating 1999; Routt 1997; Templeman 1996). Por tanto Hinsche 2002 **no puede sostener un prior clinico de malposicion** para el muestreador: la cadena de citas se corta aqui y sigue rio arriba.

Lo que si aporta, con reservas: (a) una definicion operacional binaria de colocacion insegura (perforacion cortical que compromete estructuras neurovasculares), sin escala graduada ni umbral en milimetros, util como contraste con la escala 0/<2/2-4/>4 mm de `smith2006iliosacral` y `zwingmann2009navigated`; (b) tasas propias de exito por nivel vertebral (93% en S1, 71% y 64% en S2) que son **de banco sobre plastico**, no clinicas; (c) evidencia de que S2 concentra la dificultad (82% de los tornillos mal colocados), lo que sugiere que el muestreador deberia condicionar la distribucion de malposicion por nivel vertebral y no usar una tasa unica; (d) dimensiones del pediculo S1/S2 medidas sobre el modelo de plastico, que aportan escala a la implicancia #7 pero **no definen una zona segura** (no hay margen al foramen, ni angulo, ni tolerancia).

## Dudas para el asesor
1. Si el 2%-15% que la tesis pensaba anclar en Hinsche 2002 es en realidad una cita de tercera mano, conviene (a) subir en la cadena hasta Routt 1997 / Templeman 1996, o (b) reemplazar la afirmacion cuantitativa por una cualitativa hasta conseguir la fuente primaria?
2. Las tasas de 93% / 71% / 64% son sobre plastico, sin fractura ni partes blandas. Se pueden citar como cota superior optimista de exactitud, o es preferible no usarlas para no dar la impresion de dato clinico?
3. Inconsistencia detectada en el propio PDF: el texto habla de *"the 22 (82%) misplaced screws"* (p. 142), pero la Tabla 1 (p. 140) suma 28 colocaciones inseguras sobre los cinco grupos. El PDF no explica que subconjunto son esos 22. Por esa razon **no se derivo ninguna tasa global de malposicion** a partir de los conteos.
4. Vale la pena registrar la distincion "colocacion insegura binaria" (Hinsche) vs "escala graduada 0-3" (Smith/Zwingmann) como dos definiciones no intercambiables de BFC?

## NO ENCONTRADO EN EL PDF

Entradas buscadas explicitamente y ausentes:

1. Tasa propia de malposicion expresada como porcentaje sobre el total de 140 tornillos: **NO ENCONTRADO EN EL PDF**.
2. Datos de pacientes reales o de cadaveres: **NO ENCONTRADO EN EL PDF** (todos los especimenes son modelos pelvicos de plastico de Synthes).
3. Margen numerico entre el tornillo y el foramen sacro: **NO ENCONTRADO EN EL PDF**.
4. Tolerancia angular del corredor sacro o angulo de insercion del tornillo: **NO ENCONTRADO EN EL PDF** (el unico angulo del texto, ">45 grados cefalico", describe una proyeccion de fluoroscopia sugerida, no una tolerancia del corredor).
5. Identidad, numero o cegamiento de quien evaluo las colocaciones: **NO ENCONTRADO EN EL PDF** (solo dice que la insercion la hizo "an experienced pelvic surgeon").
6. Evaluacion postoperatoria por CT o radiografia de la colocacion final: **NO ENCONTRADO EN EL PDF** (la evaluacion fue fisica: corte con sierra de banda e inspeccion visual).
7. Escala graduada de malposicion con umbrales en milimetros (tipo 0/<2/2-4/>4 mm): **NO ENCONTRADO EN EL PDF** (el criterio es binario seguro/inseguro).
8. Dosis de radiacion en mGy, mSv o producto dosis-area: **NO ENCONTRADO EN EL PDF** (solo tiempo de radiacion en segundos).
9. Explicacion de la discrepancia entre los "22 misplaced screws" del texto y los 28 conteos inseguros de la Tabla 1: **NO ENCONTRADO EN EL PDF**.

## Evidencia textual

| Dato | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Rango 2%-15% de mala colocacion con lesion neurovascular, **citado de terceros (refs. 5, 11, 20, 24), no medido aqui** | "has been reported to range between 2% and 15%, even by experienced surgeons" | Introduccion, p. 135 |
| Diseno del estudio | "A prospective controlled experimental study was done to assess the value" | Abstract, p. 135 |
| Montaje simulado, 140 tornillos, 35 modelos | "140 cannulated screws were placed into the S1 and S2 vertebral bodies" | Abstract, p. 135 |
| Especimen: **plastico**, no paciente ni cadaver | "28 plastic pelvic models (Synthes, Oberdorf, Switzerland) were used" | Materials and Methods, p. 136 |
| Primer bloque: 112 tornillos | "the insertion of 112 cannulated screws in the S1 and S2 vertebral bodies" | Materials and Methods, p. 136 |
| Operador | "by an experienced pelvic surgeon" | Materials and Methods, p. 136 |
| Segundo bloque: 28 tornillos, 7 modelos | "28 additional screws were inserted in seven additional plastic models" | Materials and Methods, p. 136 |
| Brocas comparadas | "two drills were used: a 2.8-mm guide wire and a 5-mm solid drill" | Materials and Methods, p. 136 |
| Broca a medida (canulada hibrida) | "consisting of a 2.8-mm guide wire inserted in a 5-mm cannulated drill" | Materials and Methods, p. 136 |
| Sin fractura: montaje post-reduccion | "No attempt to create a fracture or displacement was made" | Experimental Setup, p. 136 |
| Referencia dinamica fijada con tornillo cortical de 3.5 mm | "fixed securely with a 3.5-mm cortical screw to the contralateral iliac crest" | Fluoroscopy-Based Technique, pp. 136-138 |
| Limitacion de imagen: sin lateral verdadera | "A true lateral radiograph was not possible" | Materials, p. 138 |
| Diametro del tornillo implantado | "cannulated screws (7.3-mm) of the appropriate length were inserted" | Materials, p. 138 |
| Metodo de evaluacion: seccion fisica | "the sacrums of the plastic models were cut with a band saw vertically into slices" | Measurements, p. 138 |
| Planos de corte | "The cuts were placed in the midsagittal and transforaminal (alar pedicle) planes" | Measurements, p. 138 |
| Inspeccion visual | "each pelvis was inspected visually for screw perforation" | Measurements, p. 138 |
| **Criterio de colocacion insegura (binario)** | "unsafe when the screw path perforated one of the cortices while jeopardizing neurovascular structures" | Measurements, p. 138 |
| Instrumento de medida y su resolucion | "measured directly with a vernier caliper with a gradation of 0.05 mm" | Measurements, p. 138 |
| Metrica de divergencia | "the difference (divergence) from the midpedicle and midvertebral position (target) to the final screw position" | Measurements, pp. 138-139 |
| Software y umbral estadistico | "Where p < 0.05, the null hypothesis was rejected" | Statistical Analysis, p. 140 |
| Ancho medio del pediculo S1 (modelo de plastico) | "mean width 28.48 mm (range, 28.00-28.75 mm)" | Results, p. 140 |
| Altura media del pediculo S1 | "mean height 24.35 mm (range, 24.00-24.93 mm)" | Results, p. 140 |
| Dimensiones del pediculo S2 | "was 23.37 mm (range, 23.11-23.96 mm) and 14.96 mm (range, 14.57-15.36 mm)" | Results, p. 140 |
| Guia 2.8 mm, S1: sin diferencia significativa | "12 versus 14 safe screw placements at the S1 level (p = 0.142)" | Results, p. 140 |
| Guia 2.8 mm, S2: diferencia significativa a favor del intensificador | "six versus 13 safe screw placements (p = 0.0046)" | Results, p. 140 |
| Broca 5 mm, S1: empate | "13 safe screw placements with both techniques (p = 1)" | Results, p. 140 |
| Broca 5 mm, S2: sin diferencia | "nine (computer-assisted image guidance) versus 10 (image intensifier) safe screw placements" | Results, p. 140 |
| Broca a medida equivalente a la solida | "The results with the custom-made drill were identical to the results with the 5-mm solid drill" | Results, p. 140 |
| Tabla 1, grupo I (broca a medida + guia): seguros 13 (S1), 9 (S2); inseguros 1 (S1), 5 (S2) | "I ... 13 9 1 5" | Table 1, p. 140 |
| Tabla 1, grupo II (guia 2.8 mm + computador): 12, 6, 2, 8 | "II 2.8-mm guide wire with computer-assisted image guidance 12 6* 2 8*" | Table 1, p. 140 |
| Tabla 1, grupo III (broca 5 mm + computador): 13, 9, 1, 5 | "III 5-mm solid drill with computer-assisted image guidance 13 9 1 5" | Table 1, p. 140 |
| Tabla 1, grupo IV (guia 2.8 mm + intensificador): 14, 13, 0, 1 | "IV 2.8-mm guide wire with conventional image intensifier 14 13 0 1" | Table 1, p. 140 |
| Tabla 1, grupo V (broca 5 mm + intensificador): 13, 10, 1, 4 | "V 5-mm solid drill with conventional image intensifier 13 10 1 4" | Table 1, p. 140 |
| Marca de significancia en las tablas | "*p < 0.05 (Computer-assisted image guidance versus image intensifier)" | Table 1, p. 140 |
| Tabla 2: desviacion AP, vertebra S1 | "1.64 (-4-2.75)" vs "3.24 (-8.5-1.5)" | Table 2, p. 140 |
| Tabla 2: desviacion AP, pediculo S1 (significativa) | "3.98* (-9.5--1)" vs "6.59* (-11-2.5)" | Table 2, p. 140 |
| Tabla 2: desviacion vertical, pediculo S1 | "3.93 (-3-8.5)" vs "3.93 (-1-6)" | Table 2, p. 140 |
| Tabla 2: desviacion AP, vertebra S2 | "1.73 (-3.75-7)" vs "2.95 (-7-2.25)" | Table 2, p. 140 |
| Tabla 2: desviacion AP, pediculo S2 (significativa) | "2.59* (-4.75-4.75)" vs "5.88* (-9.5-1.25)" | Table 2, p. 140 |
| Tabla 2: desviacion vertical, pediculo S2 | "2.32 (-2-5.5)" vs "2.84 (-5.5-5)" | Table 2, p. 140 |
| Unidades de la Tabla 2 | "Mean results (and range) are expressed in millimeters" | Table 2, p. 140 |
| Solo se reporta la divergencia de la broca solida | "the results for the 5-mm solid drill ... are shown" | Discussion, p. 141 |
| Guia flexible descartada para el sistema navegado | "Given its specific unsuitability for use with the computer-assisted, image-guidance system" | Discussion, p. 141 |
| Zona critica anatomica (definicion cualitativa del corredor) | "The critical area of the screw path is the narrowest portion of the sacral ala" | Discussion, p. 141 |
| Definicion del pediculo sacro | "junction between the sacral body and the alar wing just cephalad to the sacral foramen" | Discussion, p. 141 |
| Capacidad del corredor segun literatura citada | "described the area as sufficient to accommodate two 7.3-mm screws" | Discussion, p. 141 |
| Dimensiones reales del pediculo sacro (Noojin, citado, 13 pacientes por CT) | "mean height of 27.76 mm and mean width of 28.05 mm" | Discussion, p. 141 |
| El modelo de plastico se desvia de la anatomia real | "The alar slope of the plastic model seemed to be steeper and the S2 pedicle smaller" | Discussion, p. 141 |
| Direcciones de perforacion, sin patron | "The screw perforations did not follow any particular pattern and were found in all directions" | Discussion, p. 141 |
| Causa del fallo de la guia de 2.8 mm | "Bending of the thin guide wire ... misled the surgeon's orientation" | Discussion, p. 141 |
| Tasa de colocacion segura en S1, ambas tecnicas | "safe screw placement into the S1 vertebra was identical with both techniques (93%)" | Discussion, p. 141 |
| Con broca solida, un solo tornillo por grupo perforo el ala | "only one screw per group perforated the ala superiorly" | Discussion, p. 142 |
| Colocacion central mas consistente con guia por computador | "the computer-assisted, image-guided system led to more consistent central screw placement" | Discussion, p. 142 |
| Significancia por plano | "significant in the horizontal (axial) plane at the sacral pedicles of S1 and S2" | Discussion, p. 142 |
| Valores p por plano axial | "(p = 0.0073, p = 0.0001)" | Discussion, p. 142 |
| Sin significancia en el plano vertical | "did not reach significant levels in the vertical (sagittal) plane" | Discussion, p. 142 |
| Concentracion de la malposicion en S2 | "18 of the 22 (82%) misplaced screws were at the S2 level" | Discussion, p. 142 |
| Tasas de exito en S2 con broca rigida de 5 mm | "unacceptable low success rates of 71% with the image-intensifier technique and 64%" | Discussion, p. 142 |
| Direccion dominante de la perforacion en S2 | "Most of these screws (five of nine) perforated the S2 pedicle inferiorly" | Discussion, p. 142 |
| Limite de la proyeccion outlet estandar | "The routine outlet view did not show the S2 pedicle sufficiently" | Discussion, p. 142 |
| Proyeccion adicional propuesta (unico angulo del PDF) | "outlet view more than 45 degrees cephalad and outlet-oblique" | Discussion, p. 142 |
| Diametro recomendado en S2 por literatura citada | "recommended only the use of 4.5-mm screws, even with CT-based computer-assisted surgery" | Discussion, p. 142 |
| Tiempo de radiacion por tornillo, propio | "4.8 seconds versus 10.2 seconds; p < 0.05" | Discussion, p. 142 |
| Tiempo de radiacion clinico citado (Routt, ref. 20) | "177 patients with 244 screws a mean radiation time per screw of 2.1 minutes" | Discussion, pp. 142-143 |
| Rango del tiempo citado | "(range, 1.2-4.6 minutes), including preoperative imaging" | Discussion, p. 143 |
| Conclusion limitada a S1 | "allowed safe placement of sacroiliac joint screws into the S1 vertebra" | Discussion, p. 143 |
| El propio paper se declara preclinico | "have led to initiation of a clinical trial" | Discussion, p. 143 |
