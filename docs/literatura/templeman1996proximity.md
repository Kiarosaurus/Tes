# templeman1996proximity — Proximidad de tornillos iliosacros a estructuras neurovasculares (CT postoperatoria)

- **DOI / URL:** NO ENCONTRADO EN EL PDF (la ficha previa tomaba 10.1097/00003086-199608000-00023 del campo AID de `refs/raw/templeman1996proximity.nbib`; el PDF no imprime DOI)
- **Nivel de lectura:** 3 (contexto), PROPUESTO por Claude y pendiente de confirmacion de la autora
- **Leido a fondo por la autora:** no
- **PDF:** papers/templeman1996proximity.pdf (renombrado a la clave el 2026-09-18; antes `templeman1996iliosacralscrews.pdf`, raw duplicado borrado, PMID 8769451). El PDF tiene 4 paginas (pp. 194-197); la lista de referencias se corta en la ref. 2, asi que las refs. 3-12 y la p. 198 no estan en el archivo.

## Que hace (3 lineas maximo)
Serie clinica retrospectiva: CT postoperatoria de 31 pacientes con 57 tornillos iliosacros, todos en el cuerpo de S1 y colocados con fluoroscopia.
Con calibre sobre CT axial mide la distancia del tornillo al foramen S1, a la cortical anterior del ala y al canal sacro, y la distancia foramen-cortical anterior (el "corredor").
Con una estimacion trigonometrica en 2D llega a que la tolerancia angular es de +/- 4 grados.

## Restriccion o supuesto clave
No es un paper de sintesis generativa, asi que no aplica el supuesto sobre implantes metalicos rigidos.
Restricciones que importan para esta tesis:
- Las medidas son distancias continuas en mm, tomadas en el plano axial. El paper no reporta una tasa de malposicion ni una escala ordinal de brecha.
- El "corredor" de 21.7 mm es una dimension antero-posterior en axial, no un diametro perpendicular al eje del tornillo. Los propios autores lo aclaran: "these measurements only represent the dimensions of the axial plane" (p. 196).
- Si el artefacto tocaba una estructura, se registraba 0 mm ("If artifact or the image of the screw entered ... recorded as ... 0 mm", p. 195). O sea, la distancia 0 junta la perforacion real con los casos que el artefacto impedia medir.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
Ninguno queda marcado como citado. Mientras la autora no lo decida, estas son las cifras que se podrian citar (todas verificadas en el PDF):

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Corredor foramen S1 - cortical anterior 21.7 +/- 3.4 mm (16.2-28.9) | "the anterior cortex of the sacrum seen on the CT scan was 21.7 ± 3.4 mm" | Results, p. 195 |
| Tolerancia angular +/- 4 grados | "Trigonometric analysis (pedicle width 21 mm) indicates that the target corridor is ± 4°." | Discussion, p. 197 |
| 7 mm de hueso para un tornillo de 7 mm centrado | "for a 7-mm diameter screw that is centrally placed, only 7 mm of bone" | Discussion, p. 197 |

## Donde entra en mi tesis
Sirve de contexto para el Objetivo 2 (restricciones anatomicas del corredor iliosacro en S1).
- **Rango 2%-15% (RETIRADO):** el PDF no contiene ningun porcentaje de malposicion (ni 2%, ni 15%, ni 0-15%), asi que no puede ser el origen de esa banda. La cita de `zwingmann2013` hacia Templeman no se sostiene en el texto. Lo mas parecido son conteos: 5/57 tornillos que entraban al foramen S1 o no se podian medir, y 1 perforacion anterior. El paper nunca los expresa como porcentaje.
- **Limite de 4 grados:** sale de un modelo 2D idealizado (Fig 2) con distancias aproximadas, y los autores advierten que la tolerancia es menor fuera del eje central. No es un umbral medido.
- **Viabilidad Dmax >= d + 2c:** el 21.7 mm (antero-posterior, axial) no se puede comparar directamente con D_TS medido en los CT locales (diametro perpendicular al eje, mediana 9.5 mm). Miden cosas distintas. El paper no define un corredor perpendicular al eje: NO ENCONTRADO EN EL PDF.
- La SAP con escala 0/<2/2-4/>4 mm sigue anclada a `zwingmann2009navigated`. Este paper no trae escala ordinal.

## Dudas para el asesor
- Los rangos de la distancia a la cortical anterior no coinciden: el abstract dice "0-15.3 mm" (p. 194) y los Results dicen "0—10.5 mm" (p. 196). Cual vale? Ninguno de los dos deberia citarse sin aclararlo.
- Como el protocolo codifica el artefacto que invade una estructura como 0 mm, podemos usar las distancias como referencia de plausibilidad del muestreador, o las descartamos por el sesgo de artefacto y los cortes de 4 mm?
- Se cita el +/- 4 grados como una "estimacion trigonometrica idealizada" y no como un umbral clinico, a pesar de que zwingmann2009 y Kaiser lo presentan como limite?

## Evidencia textual

| Dato / criterio | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Revista, numero, paginas | "CLINICAL ORTHOPAEDICS AND RELATED RESEARCH Number 329, pp 194-198" | Cabecera, p. 194 |
| n = 31 pacientes, 57 tornillos | "postoperative computed tomography scans of 31 patients who had 57 iliosacral screws" | Abstract, p. 194 |
| Sexo: 16 hombres, 15 mujeres | "Thirty-one patients (16 males and 15 females)" | Materials and Methods, p. 194 |
| 28 lesiones unilaterales, 3 bilaterales | "for 28 unilateral and 3 bilateral injuries" | Materials and Methods, p. 194 |
| Indicaciones: 15 luxaciones SI, 12 fracturas sacras | "15 sacroiliac dislocations; 12 sacral fractures" | Materials and Methods, p. 195 |
| Indicaciones: 2 pseudoartrosis, 2 fusiones SI | "2 sacral nonunions; and 2 sacroiliac fusions" | Materials and Methods, p. 195 |
| Placa de banda de tension en 6 pacientes | "A transiliac tension band plate was added in 6 patients" | Materials and Methods, p. 195 |
| Tecnica: intensificador de imagenes (fluoroscopia) | "Screw insertion was performed in all cases with an image intensifier" | Materials and Methods, p. 195 |
| Tecnica de referencia | "as described by Matta and Saucedo" | Materials and Methods, p. 195 |
| Proyeccion cefalica: broca justo encima del foramen | "directed from the level of the S1 foramen cephalad to lie just above" | Materials and Methods, p. 195 |
| Proyeccion caudal: broca al centro del cuerpo de S1 | "caudad view was used to direct the drill bit into the center" | Materials and Methods, p. 195 |
| Prono: 22 procedimientos (18 abiertos, 4 percutaneos) | "prone for 22 procedures, with 18 procedures done by open reduction" | Materials and Methods, p. 195 |
| Supino: 9 pacientes | "Nine patients were positioned supine." | Materials and Methods, p. 195 |
| Tornillo canulado en supino | "percutaneous insertion of a cannulated screw" | Materials and Methods, p. 195 |
| Nivel: los 57 tornillos en el cuerpo de S1 | "A total of 57 screws were inserted into the body of S1." | Materials and Methods, p. 195 |
| 24 pacientes con 2 tornillos | "In 24 patients 2 screws were inserted into the body of S1" | Materials and Methods, p. 195 |
| 1 paciente bilateral con 3 tornillos | "in 1 patient with bilateral lesions 3 screws were inserted" | Materials and Methods, p. 195 |
| 6 pacientes con 1 tornillo | "in 6 patients only 1 screw was inserted" | Materials and Methods, p. 195 |
| Tornillos en S2 | NO ENCONTRADO EN EL PDF | — |
| Calibre / longitud de los tornillos usados | NO ENCONTRADO EN EL PDF (solo el ejemplo hipotetico de 7 mm, p. 197) | — |
| Equipo CT | "obtained on a Somaton Plus unit (Siemens Medical, Iselin, NJ)" | Materials and Methods, p. 195 |
| Reconstruccion y ventana | "standard reconstruction algorithm displayed with optimal bone windowing" | Materials and Methods, p. 195 |
| Colimacion 4 mm, cortes contiguos o solapados 1 mm | "collimator widths of 4 mm with either contiguous or overlapped slices (1-mm overlap)" | Materials and Methods, p. 195 |
| Instrumento de medida | "Measurements were made with a metric caliper" | Materials and Methods, p. 195 |
| Calibracion con escala de 5 cm | "calibrated against the standard 5-cm scale displayed on each image" | Materials and Methods, p. 195 |
| Definicion del corredor | "width of the sacrum between the first sacral foramen and the sacral ala" | Materials and Methods, p. 195 |
| Corredor = dimension AP del ala sobre el foramen S1 | "The anteroposterior dimension of the sacral ala above the first sacral foramen" | Results, p. 195 |
| Criterio 0 mm (artefacto o tornillo en la estructura) | "If artifact or the image of the screw entered the first sacral foramen" | Materials and Methods, p. 195 |
| Criterio 0 mm (continuacion) | "or penetrated the anterior cortex of the ala, this was recorded as ... 0 mm" | Materials and Methods, p. 195 |
| Estadistica: media +/- DE | "Results were expressed as the mean plus or minus the standard deviation." | Materials and Methods, p. 195 |
| Corredor 21.7 +/- 3.4 mm (16.2-28.9) | "was 21.7 ± 3.4 mm (range, 16.2–28.9 mm)" | Results, p. 195 |
| Fig 1: definicion de las medidas 1-4 | "4 = the foramen to anterior cortex dimension" | Fig 1, p. 195 |
| Distancia al foramen S1: 3 +/- 2.9 mm (0-10.5) | "distance from the screws to the S1 foramen was 3 mm ± 2.9 mm" | Results, p. 196 |
| 5 tornillos en el foramen o sin medicion posible | "Five screws either appeared to enter the S1 foramen or there was too much scatter" | Results, p. 196 |
| Sin secuelas neurologicas en esos 5 | "There were no neurologic sequelae in any of the 5 patients." | Results, p. 196 |
| Distancia a la cortical anterior: 4.8 +/- 4.5 mm (0-10.5, Results) | "to the screws was 4.8 mm ± 4.5 mm (range, 0—10.5 mm)" | Results, p. 196 |
| Rango a la cortical anterior segun el abstract: 0-15.3 (discrepa) | "average closest distance to the anterior cortex ... was 4.8 mm (range, 0-15.3 mm)" | Abstract, p. 194 |
| 1 perforacion de la cortical anterior con reingreso | "a screw penetrated the anterior cortex of the ala and reentered the sacral body" | Results, p. 196 |
| Distancia al canal sacro: 3.1 mm (0-13) | "distance from the screw to the sacral canal was 3.1 mm, with a range of 0 to 13 mm" | Results, p. 196 |
| Punta a cortical anterior: 15.9 mm (0-42.4) | "was 15.9 mm (range, 0-42.4 mm)" | Results, p. 196 |
| 3 tornillos de punta problematicos, sin consecuencias | "There were no neurologic consequences related to the 3 screws." | Results, p. 196 |
| 1 complicacion iatrogenica | "There was 1 iatrogenic complication in this series." | Results, p. 196 |
| Complicacion: perdida de dorsiflexion del pie | "Postoperative examination revealed loss of foot dorsiflexion." | Results, p. 196 |
| Densidad de S1 60% mayor que el ala (citado de otra fuente, ref. 12) | "bone density of the body of S1 is 60% greater than that of the sacral ala" | Discussion, p. 196 |
| Mirkovic (ref. 9): vena iliaca interna a 2.4 mm | "the internal iliac vein was 2.4 mm" | Discussion, p. 196 |
| Mirkovic (ref. 9): raices L4-L5 a 1 mm | "the nerve roots of L4 and L5 were 1 mm" | Discussion, p. 196 |
| Corredor medido solo en el plano axial | "these measurements only represent the dimensions of the axial plane" | Discussion, pp. 196-197 |
| La zona 3D de insercion no se determino | "the 3-dimensional zone for screw insertion could not be determined" | Discussion, pp. 196-197 |
| Aritmetica: 7 mm de hueso alrededor de un tornillo de 7 mm | "for a 7-mm diameter screw that is centrally placed, only 7 mm of bone" | Discussion, p. 197 |
| Supuesto trigonometrico: piel-ilion aprox. 10 cm | "distance from the skin to the outer aspect of the ilium was approximately 10 cm" | Discussion, p. 197 |
| Supuesto trigonometrico: ilion-cuerpo 5 cm | "and from the ilium to the body 5 cm" | Discussion, p. 197 |
| Resultado: +/- 4 grados con ancho de pediculo de 21 mm | "Trigonometric analysis (pedicle width 21 mm) indicates that the target corridor is ± 4°." | Discussion, p. 197 |
| Menor tolerancia fuera del eje central | "The tolerance for angular misdirection is less for screws not aligned along the central axis" | Discussion, p. 197 |
| Supuestos de la Fig 2 | "the diagram assumes perfect initial placement of the screw in the outer ilium" | Fig 2, p. 197 |
| Formula trigonometrica explicita | NO ENCONTRADO EN EL PDF | — |
| Porcentaje de malposicion (2%, 15%, 0-15%) | NO ENCONTRADO EN EL PDF | — |
| Escala ordinal de brecha cortical | NO ENCONTRADO EN EL PDF | — |
| Manejo o reduccion del artefacto metalico (MAR) | NO ENCONTRADO EN EL PDF (solo la regla de 0 mm y "too much scatter") | — |
| Numero de observadores / concordancia | NO ENCONTRADO EN EL PDF | — |

Nota de Claude (verificacion propia, no esta en el PDF): arctan(10.5 / 150) da aprox. 4.0 grados. Eso sale de tomar medio ancho de 21 mm y 100 + 50 mm desde la mano del cirujano. Encaja con las cifras del paper, pero el paper no publica la formula.

## Candidatos de snowballing

| Cita tal como aparece | N. ref | Por que |
|---|---|---|
| "Mirkovic et al" (referencia completa NO ENCONTRADO EN EL PDF: la lista se corta en la ref. 2) | 9 | Geometria del corredor: distancias de la vena iliaca interna y de las raices L4-L5 a la cortical anterior del ala sacra |

No aparece ninguna referencia sobre el origen del 2-15% ni sobre escalas de brecha.
