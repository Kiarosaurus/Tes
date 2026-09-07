# zwingmann2009navigated — Navegacion computarizada en tornillos iliosacros: tasa de malposicion y radiacion

- **DOI / URL:** 10.1007/s11999-008-0632-6 (Clin Orthop Relat Res (2009) 467:1833–1838)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/zwingmann2009navigated.pdf

**Profundidad: texto completo (6 paginas, 1833–1838, incluye referencias).**

## Que hace (3 lineas maximo)
Estudio clinico prospectivo/retrospectivo comparativo (Level II) que compara insercion percutanea de tornillos
iliosacros con navegacion 3D (Iso-C3D + VectorVision) contra fluoroscopia convencional, en fracturas inestables
del anillo pelvico posterior. Mide tiempo operatorio, tiempo y dosis de radiacion, y posicion del tornillo por
TC postoperatoria graduada en 4 niveles de perforacion cortical.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. La restriccion relevante para la tesis es otra: el paper **no reporta un
rango unico de malposicion**; reporta dos brazos con distribuciones distintas de perforacion cortical y, ademas,
cita de terceros un rango de 2%–15% para fluoroscopia. El supuesto operacional que si fija es que la posicion se
evalua solo sobre **un tornillo por paciente, en S1**: "In our treatment algorithm, we used only one screw in all
patients" (Discussion, p. 1837). Las cifras de grado se leen de la Figura 4 y del texto de Resultados, no de una
tabla numerica de malposicion.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Malposicion con fluoroscopia 2%–15% (CITADA de terceros, refs [13, 28]) | "Screw malposition rates with fluoroscopic guidance have been reported to range from 2% to 15%" | Introduction, p. 1834 (repetida en Discussion, p. 1837) |
| Navegado: Grado 0 (sin perforacion) en 69% | "Grade 0 in 69% (Grade 1, 15%; Grade 2, 8%; Grade 3, 8%)" | Results, p. 1836–1837 y Fig. 4 |
| Convencional: Grado 0 (sin perforacion) en 40% | "Grade 0 in 40% (Grade 1, 37%; Grade 2, 11.5%; Grade 3, 11.5%)" | Results, p. 1837 y Fig. 4 |
| Grados 1–3 (alguna perforacion): 31% navegado / 60% convencional | **DERIVADO por complemento de 69% y 40%; el paper NO escribe 31% ni 60%** | Results, p. 1836–1837 y Fig. 4 |
| Umbral de grado 1 | "Grade 0, no perforation; Grade 1, perforation less than 2 mm" | Materials and Methods, p. 1835 |
| Umbral de grados 2 y 3 | "Grade 2, perforation between 2 and 4 mm; and Grade 3, perforation greater than 4 mm" | Materials and Methods, p. 1835 |
| Tolerancia angular clinica: 4 grados (CITADA, ref [28]) | "Malposition of the screw by as little as 4° can cause damage" | Introduction, p. 1834 |
| Lesion neurologica 0.5%–7.7% (CITADA, ref [32]) | "with an incidence of neurologic injury between 0.5% and 7.7%" | Introduction, p. 1834 |
| Muestra navegada: 26 tornillos / 24 pacientes | "We inserted 26 screws in 24 patients using the navigation system" | Abstract, p. 1833 |
| Muestra convencional: 35 tornillos / 32 pacientes | "35 screws in 32 patients using the conventional fluoroscopic technique" | Abstract, p. 1833 |
| Significancia de la diferencia de posicion | "greater percentage of correct screw positions (p = 0.02) in the navigated group" | Results, p. 1836 |
| Cadaver: 2 de 10 tornillos perforan cortical, en ambos grupos (CITADA, ref [8]) | "two of 10 screws penetrated the cortex equally in both groups" | Discussion, p. 1838 |

## Donde entra en mi tesis
Es la fuente clinica del muestreador: define la distribucion objetivo de malposicion contra la que se compara SAP.
Aporta ademas una **escala ordinal de perforacion cortical en milimetros (0 / <2 / 2–4 / >4 mm)** directamente
reutilizable como graduacion de brecha cortical (BFC), en lugar de un criterio binario. Advertencia para la
redaccion: el paper sostiene DOS tasas de brazos distintos (navegado vs convencional), no un rango continuo.

## Dudas para el asesor
- Si el muestreador debe reproducir una sola distribucion, cual brazo es el correcto: convencional (60% con alguna
  perforacion, tecnica mas frecuente en la practica general) o navegado (31%)? Mezclarlos como "rango 31–60%"
  no tiene respaldo textual en este PDF.
- Se debe adoptar la escala 0/<2/2–4/>4 mm como definicion de BFC, sabiendo que el paper la toma prestada de
  clasificacion de tornillos pediculares (ref [23]) y no de tornillos iliosacros?
- La evaluacion aqui es de UN tornillo en S1 por paciente. Es valido extrapolarla a placas y a multiples implantes?

## Evidencia textual

| Dato / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Rango de malposicion citado de terceros | "Screw malposition rates with fluoroscopic guidance have been reported to range from 2% to 15%" | Introduction, p. 1834 |
| Repeticion del mismo rango en discusion | "have been reported to range from 2% to 15% [13, 28]" | Discussion, p. 1837 |
| Lesion neurologica asociada | "with an incidence of neurologic injury between 0.5% and 7.7% [32]" | Introduction, p. 1834 |
| Umbral angular de dano | "Malposition of the screw by as little as 4° can cause damage to neurovascular structures" | Introduction, p. 1834 |
| Escala de perforacion, grados 0 y 1 | "Grade 0, no perforation; Grade 1, perforation less than 2 mm" | Materials and Methods, p. 1835 |
| Escala de perforacion, grados 2 y 3 | "Grade 2, perforation between 2 and 4 mm; and Grade 3, perforation greater than 4 mm" | Materials and Methods, p. 1835 |
| Origen de la escala | "graded according to an established classification method used for correct pedicle screw placement [23]" | Materials and Methods, p. 1835 |
| Definicion de posicion ideal (cortical) | "An ideal screw position was considered entirely within the cortical margins of the sacrum" | Materials and Methods, p. 1835 |
| Definicion de posicion ideal (orientacion) | "parallel to the respective sacral end plate and the S1 neuroforamina" | Materials and Methods, p. 1835 |
| Criterio de posicion correcta (fluoroscopia) | "considered parallel to the superior S1 vertebral end plate midway between the S1 superior end plate and the S1 neuroforamina" | Materials and Methods, p. 1835 |
| Resultado navegado (grados) | "Grade 0 in 69% (Grade 1, 15%; Grade 2, 8%; Grade 3, 8%)" | Results, p. 1836 y Fig. 4 |
| Resultado convencional (grados) | "Grade 0 in 40% (Grade 1, 37%; Grade 2, 11.5%; Grade 3, 11.5%)" | Results, p. 1837 y Fig. 4 |
| Significancia de la diferencia | "We observed a greater percentage of correct screw positions (p = 0.02)" | Results, p. 1836 |
| Tamano de muestra navegado | "We inserted 26 screws in 24 patients using the navigation system" | Abstract, p. 1833 |
| Tamano de muestra convencional | "35 screws in 32 patients using the conventional fluoroscopic technique" | Abstract, p. 1833 |
| Periodo navegado | "were treated with navigated iliosacral screw placement from February 2006 to April 2008" | Materials and Methods, p. 1834 |
| Periodo convencional | "who had conventional fluoroscopy (conventional group) from December 2000 to February 2006" | Materials and Methods, p. 1834 |
| Subgrupo solo tornillo | "13 navigated screws versus 12 conventional screws" | Materials and Methods, p. 1834 |
| Subgrupo tornillo + fijador externo | "13 navigated screws versus 23 conventional screws" | Materials and Methods, p. 1834 |
| Metodo de medicion de la posicion | "A postoperative CT-based analysis of localization of the transiliosacral screw was evaluated" | Materials and Methods, p. 1835 |
| Cegamiento del evaluador | "by one independent radiologist (EK) not involved in the treatment" | Materials and Methods, p. 1835 |
| Numero de tornillos por paciente | "In our treatment algorithm, we used only one screw in all patients" | Discussion, p. 1837 |
| Nivel de evidencia | "Level of Evidence: Level II, therapeutic study" | Abstract, p. 1833 |
| Test estadistico para posicion | "percentage of correct screw positions between the groups were determined by the Wilcoxon signed rank test" | Materials and Methods, p. 1835 |
| Criterio de inclusion (tipos de fractura) | "including only Types B and C fractures according to the classification of Tile and Pennal" | Materials and Methods, p. 1834 |
| Definicion Tile tipo B | "a Type B fracture is defined as unstable for rotational movement" | Discussion, p. 1837 |
| Definicion Tile tipo C | "Type C fracture is defined as unstable for vertical and rotational movements" | Discussion, p. 1837 |
| Distribucion de fracturas | "75% Type B and 25% Type C versus 60% Type B and 40% Type C" | Materials and Methods, p. 1834 |
| Edad de los grupos | "35 ± 23 years versus 46 ± 20 years (p = 0.017)" | Materials and Methods, p. 1834 |
| Sexo | "male 60% versus 56%) (p = 0.015)" | Materials and Methods, p. 1834 |
| Injury Severity Score | "31 ± 14 [range, 9–57] versus 26 ± 17 [range, 9–59]) (p = 0.088)" | Materials and Methods, p. 1834 |
| Politraumatizados (ISS >= 16) | "(Injury Severity Score of 16 or greater) (79% versus 62%) (p = 0.066)" | Materials and Methods, p. 1834 |
| Cirujanos participantes | "Seven trauma surgeons performed the implantations in the navigation group and nine" | Materials and Methods, p. 1834 |
| Experiencia equivalente | "The level of expertise between surgeons in the two groups was not different (p = 0.24)" | Materials and Methods, p. 1834 |
| Diametro de broca guia | "drilling of a 3.2-mm hole controlled by navigation was performed" | Materials and Methods, p. 1835 |
| Avance del alambre guia | "A guide wire was inserted 1 to 2 cm further" | Materials and Methods, p. 1835 |
| Tornillo usado | "the screws using a 7.0-mm cannulated screw and removed the Kirschner wire" | Materials and Methods, p. 1835 |
| Broca previa | "drilled holes with a cannulated 5-mm drill" | Materials and Methods, p. 1835 |
| Kirschner de referencia | "on two percutaneously placed 3.0-mm Kirschner wires in the iliac crest" | Materials and Methods, p. 1834 |
| Adquisicion Iso-C3D | "which rotates 190° around the operative field" | Materials and Methods, p. 1834 |
| Duracion del escaneo | "Iso-C3D imaging was performed (duration approximately 90 seconds)" | Materials and Methods, p. 1834 |
| Tiempo transeccion-sutura, solo tornillo | "navigated group (72 ± 16 minutes; range, 52–106 minutes) and conventional group (69 ± 38 minutes" | Results, p. 1835 |
| p del tiempo, solo tornillo | "the time from transection until suture was similar (p = 0.42)" | Results, p. 1835 |
| Tiempo, con fijador externo | "navigated group (87 ± 30 minutes; range, 41–142 minutes)" | Results, p. 1835 |
| Tiempo convencional, con fijador | "conventional group (74 ± 24 minutes; range, 37–114 minutes)" | Results, p. 1835 |
| Radiacion navegado, solo tornillo | "63 ± 15 seconds; range, 36–84 seconds; 822 ± 164 cGy/cm2; range, 542–1145 cGy/cm2" | Results, p. 1835 |
| Radiacion convencional, solo tornillo | "141 ± 69 seconds; range, 42–252 seconds; 1843 ± 1052 cGy/cm2; range, 600–3811" | Results, p. 1836 |
| Radiacion navegado, con fijador | "93 ± 44 seconds; range, 46–216 seconds; 1021 ± 408 cGy/cm2" | Results, p. 1836 |
| Radiacion convencional, con fijador | "211 ± 94 seconds; range, 21–384 seconds; 2814 ± 1099 cGy/cm2" | Results, p. 1836 |
| p de radiacion, solo tornillo | "radiation time (p = 0.003) and dose (p = 0.001) were decreased in the navigated group" | Results, p. 1835 |
| Tiempos de radiacion reportados por terceros | "reported to vary between 1.8 and 7.3 minutes [5, 7]" | Discussion, p. 1837 |
| Tiempo extra de setup (estimacion no medida) | "it takes approximately 10 extra minutes to get the navigation system set up" | Discussion, p. 1837 |
| Solapamiento de cirujanos | "only 50% of the surgeons participated in both groups (navigated/conventional)" | Discussion, p. 1837 |
| Retiro de implantes | "All screws are removed after 3 to 4 months" | Discussion, p. 1837 |
| Publicaciones previas sobre navegacion pelvica | "nine publications were listed concerning navigated surgery of the dorsal pelvic ring" | Introduction, p. 1834 |
| Estudios 3D en cadaver o pelvis plastica | "only two studies described three-dimensional computer-assisted screw placement in cadavers or plastic pelves" | Introduction, p. 1834 |
| Cadaver, perforacion cortical | "two of 10 screws penetrated the cortex equally in both groups [8]" | Discussion, p. 1838 |
| Limitacion declarada de la navegacion | "use of a navigation system does not guarantee 100% correct screw placement" | Discussion, p. 1838 |
| Causa sospechada de grados 2 y 3 | "we suspect the Grades 2 and 3 malpositions ... were the result of technical mistakes" | Discussion, p. 1837 |
| Tabla 1: total tornillos navegados | "Total 26" | Table 1, p. 1835 |
| Tabla 1: total tornillos convencionales | "Total 35" | Table 1, p. 1835 |
| Tabla 1: media de tornillos por cirujano (navegacion) | "Mean ± SD 5.7 ± 5.1" | Table 1, p. 1835 |
| Tabla 1: media de tornillos por cirujano (convencional) | "Mean ± SD 12.2 ± 7.6" | Table 1, p. 1835 |
| Tabla 1: media total | "Mean ± SD 15.3 ± 9.4" | Table 1, p. 1835 |

## Verificacion de nivel

**Conclusion en primer plano: el paper NO contiene el rango "31–60%" como texto. Las dos cifras existen, pero como
complementos aritmeticos de dos tasas de posicion CORRECTA de dos brazos distintos, no como un rango citable.**

### 1. CRITICO — Aparece literalmente el rango 31-60%?

**EL RANGO 31-60% NO APARECE EN ESTE PDF.**

Ni "31%", ni "60%" como tasa de malposicion, ni la construccion "31 to 60" o "31–60". (Advertencia: el numero 31
si aparece en el PDF, pero como Injury Severity Score: "31 ± 14 [range, 9–57]", Materials and Methods, p. 1834.
El numero 60% aparece como proporcion de varones y como proporcion de fracturas Tile tipo B, no como malposicion.)

Todas las tasas de malposicion / posicion que SI aparecen:

| Tasa | Frase original (<=15 palabras) | Seccion / pagina | Origen |
|---|---|---|---|
| 2% a 15% (malposicion con fluoroscopia) | "Screw malposition rates with fluoroscopic guidance have been reported to range from 2% to 15%" | Introduction, p. 1834; repetida en Discussion, p. 1837 | **Citada** de refs [13, 28] |
| 0.5% a 7.7% (lesion neurologica) | "with an incidence of neurologic injury between 0.5% and 7.7% [32]" | Introduction, p. 1834 | **Citada** de ref [32] |
| Navegado: 69% Grado 0; 15% Grado 1; 8% Grado 2; 8% Grado 3 | "Grade 0 in 69% (Grade 1, 15%; Grade 2, 8%; Grade 3, 8%)" | Results, p. 1836 y Fig. 4 | **Propia** |
| Convencional: 40% Grado 0; 37% Grado 1; 11.5% Grado 2; 11.5% Grado 3 | "Grade 0 in 40% (Grade 1, 37%; Grade 2, 11.5%; Grade 3, 11.5%)" | Results, p. 1837 y Fig. 4 | **Propia** |
| 2 de 10 tornillos perforan cortical (cadaver) | "two of 10 screws penetrated the cortex equally in both groups [8]" | Discussion, p. 1838 | **Citada** de ref [8] |

De donde sale el "31–60%": 100 − 69 = 31 (navegado, alguna perforacion) y 100 − 40 = 60 (convencional, alguna
perforacion). Los grados suman exactamente 100 en cada brazo (69+15+8+8 = 100; 40+37+11.5+11.5 = 100), asi que la
derivacion es aritmeticamente correcta, **pero es una derivacion de la autora, no una cita**. En la tesis debe
escribirse como calculo propio a partir de las tasas de Grado 0, nunca entre comillas ni atribuido al texto.

### 2. Medicion propia vs cifra citada

- **2%–15%**: CITADA. Atribuida a las refs [13] y [28]: [13] Hinsche AF, Giannoudis PV, Smith RM.
  *Fluoroscopy-based multiplanar image guidance for insertion of sacroiliac screws.* Clin Orthop Relat Res.
  2002;395:135–144; y [28] Templeman D, Schmidt A, Freese J, Weisman I. *Proximity of iliosacral screws to
  neurovascular structures after internal fixation.* Clin Orthop Relat Res. 1996;329:194–198.
- **0.5%–7.7% (lesion neurologica)**: CITADA. Ref [32] van den Bosch EW, van Zwienen CM, van Vugt AB.
  *Fluoroscopic positioning of sacroiliac screws in 88 patients.* J Trauma. 2002;53:44–48.
- **4 grados de malposicion tolerable**: CITADA. Ref [28] Templeman et al.
- **69% / 15% / 8% / 8% y 40% / 37% / 11.5% / 11.5%**: MEDICION PROPIA de estos autores, por TC postoperatoria.
- **2 de 10 tornillos en cadaver**: CITADA. Ref [8] Day AC, Stott PM, Boden BP. *The accuracy of computer-assisted
  percutaneous iliosacral screw placement.* Clin Orthop Relat Res. 2007;463:179–186.

### 3. Definicion operacional de "malposicion"

No hay una definicion en prosa de la palabra "malposition". Lo que hay es una **definicion de posicion ideal** mas
una **escala de perforacion en milimetros**; la malposicion queda implicitamente definida como todo lo que no es
Grado 0.

Literal (Materials and Methods, p. 1835):
- "An ideal screw position was considered entirely within the cortical margins of the sacrum"
- "and parallel to the respective sacral end plate and the S1 neuroforamina"
- "Grade 0, no perforation; Grade 1, perforation less than 2 mm"
- "Grade 2, perforation between 2 and 4 mm; and Grade 3, perforation greater than 4 mm"
- Procedencia de la escala: "graded according to an established classification method used for correct pedicle
  screw placement [23]" — ref [23] Smith HE, Yuan PS, Sasso R, Papadopolous S, Vaccaro AR. Spine. 2006;31:234–238.

Umbral angular (no usado como criterio de graduacion, solo mencionado como riesgo, Introduction, p. 1834):
"Malposition of the screw by as little as 4° can cause damage to neurovascular structures".

### 4. Muestra, diseno y medicion

- Diseno: "Level of Evidence: Level II, therapeutic study" (Abstract, p. 1833). Grupo navegado recolectado de
  forma prospectiva ("We prospectively collected the data of our patients", Materials and Methods, p. 1834);
  grupo control historico y retrospectivo ("given our retrospective analysis", Discussion, p. 1837;
  "the retrospective control group", Discussion, p. 1837). Series temporales consecutivas, no aleatorizadas.
- Muestra: 26 tornillos / 24 pacientes navegados (feb 2006 – abr 2008); 35 tornillos / 32 pacientes
  convencionales (dic 2000 – feb 2006). Un solo tornillo por paciente.
- Subgrupos: solo tornillo (13 navegados vs 12 convencionales); tornillo + fijador externo (13 vs 23).
- Medicion de posicion: **TC postoperatoria**, "A postoperative CT-based analysis of localization of the
  transiliosacral screw was evaluated by one independent radiologist (EK) not involved in the treatment"
  (Materials and Methods, p. 1835). No radiografia simple, no navegacion, para la evaluacion final.
- Estadistica de la posicion: Wilcoxon signed rank test (Materials and Methods, p. 1835).
- Limitaciones declaradas: "the relatively small number of patients"; "the techniques were performed
  sequentially" (Discussion, p. 1837).

### 5. Navegacion vs sin navegacion — SI, son dos brazos separados

**Si compara, y son dos distribuciones distintas, no un rango.** Esta es la observacion mas importante para el
muestreador.

| Brazo | Grado 0 | Grado 1 (<2 mm) | Grado 2 (2–4 mm) | Grado 3 (>4 mm) | Alguna perforacion (derivado) | n |
|---|---|---|---|---|---|---|
| Navegado (3D) | 69% | 15% | 8% | 8% | 31% | 26 tornillos / 24 pacientes |
| Convencional (fluoroscopia) | 40% | 37% | 11.5% | 11.5% | 60% | 35 tornillos / 32 pacientes |

Diferencia significativa: "We observed a greater percentage of correct screw positions (p = 0.02) in the navigated
group" (Results, p. 1836). Las columnas 31% y 60% son complementos calculados, no texto del paper.

### 6. Anatomia

Iliosacro / transiliosacro percutaneo, entrada por ilion hacia **S1**:
- "a guide wire was placed across the ileum into the S1 vertebra" (Materials and Methods, p. 1835).
- Referencia de la posicion: "the S1 superior end plate and the S1 neuroforamina" (Materials and Methods, p. 1835).
- Un solo tornillo: "we used only one screw in all patients" (Discussion, p. 1837).
- **S2: NO ENCONTRADO EN EL PDF** como nivel instrumentado o evaluado. El texto menciona en la discusion la
  controversia sobre el numero de tornillos ("placement of two screws [5, 8, 28]", Discussion, p. 1837), pero sin
  especificar S2 y sin datos propios.
- Poblacion: fracturas inestables del anillo pelvico posterior, Tile y Pennal tipos B y C, incluyendo
  "posterior sacroiliac ligamentous injuries" (Introduction, p. 1833).

### 7. Graduacion de brecha cortical

**SI, hay graduacion ordinal, no binaria.** Cuatro niveles con umbrales metricos explicitos: 0 mm / <2 mm /
2–4 mm / >4 mm (Materials and Methods, p. 1835; distribucion en Fig. 4, p. 1836). Es directamente utilizable como
escala de BFC. Nota de rigor: la escala se toma prestada de clasificacion de tornillos pediculares (ref [23]), y
el paper no reporta ni direccion de la perforacion (anterior, foraminal, canal) ni volumen de brecha, solo
profundidad maxima en milimetros.

### 8. Nivel que sostiene la evidencia

**NIVEL 1, pero con reformulacion obligatoria del rol asignado.** El paper sostiene con solidez una escala de
brecha cortical en milimetros y dos tasas de perforacion medidas por TC (31% navegado, 60% convencional, ambas
derivadas por complemento); **no sostiene la formulacion "tasa 31–60%" como cifra citable del paper**, porque ese
rango no aparece en el texto y porque une dos poblaciones tecnicamente distintas. El rol registrado debe pasar de
"tasa 31–60%" a "dos tasas de perforacion cortical por brazo, derivadas de 69% y 40% de Grado 0, mas escala
0/<2/2–4/>4 mm".

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| 13. Hinsche AF, Giannoudis PV, Smith RM. Fluoroscopy-based multiplanar image guidance for insertion of sacroiliac screws. Clin Orthop Relat Res. 2002;395:135–144. | **Fuente original del rango 2%–15% de malposicion.** Una de las dos referencias a las que Zwingmann atribuye la tasa clinica de fluoroscopia. |
| 28. Templeman D, Schmidt A, Freese J, Weisman I. Proximity of iliosacral screws to neurovascular structures after internal fixation. Clin Orthop Relat Res. 1996;329:194–198. | **Fuente original del rango 2%–15% y del umbral de 4 grados.** Doble origen de cifras citables (tasa + tolerancia angular). |
| 32. van den Bosch EW, van Zwienen CM, van Vugt AB. Fluoroscopic positioning of sacroiliac screws in 88 patients. J Trauma. 2002;53:44–48. | Fuente de la incidencia de lesion neurologica 0.5%–7.7%; n=88, serie clinica grande de posicion de tornillos sacroiliacos. |
| 23. Smith HE, Yuan PS, Sasso R, Papadopolous S, Vaccaro AR. An evaluation of image-guided technologies in the placement of percutaneous iliosacral screws. Spine. 2006;31:234–238. | **Fuente original de la escala 0/<2/2–4/>4 mm** que la tesis usaria como BFC. Verificar la definicion primaria antes de adoptarla. |
| 8. Day AC, Stott PM, Boden BP. The accuracy of computer-assisted percutaneous iliosacral screw placement. Clin Orthop Relat Res. 2007;463:179–186. | Tasa de perforacion cortical en cadaver (2 de 10 tornillos); baseline experimental controlado para validar el muestreador. |
| 12. Goldberg BA, Lindsey RW, Foglar C, Hedrick TD, Miclau T, Hadad JL. Imaging assessment of sacroiliac screw placement relative to the neuroforamen. Spine. 1998;23:585–589. | Metrica de posicion relativa al neuroforamen; posible metrica alternativa o complementaria a SAP/ISC. |
| 29. Tile M, Pennal GF. Pelvic disruption: principles of management. Clin Orthop Relat Res. 1980;151:56–64. | Clasificacion Tile/Pennal B y C usada como criterio de inclusion; define la poblacion anatomica del muestreador. |
| 5. Briem D, Windolf J, Rueger JM. [Percutaneous, 2D-fluoroscopic navigated iliosacral screw placement in the supine position: technique, possibilities, and limits] Unfallchirurg. 2007;110:393–401. | Revision de navegacion iliosacra (las "nine publications"); metodo que compite con el muestreador y fuente de tiempos de radiacion 1.8–7.3 min. |
| 7. Collinge C, Coons D, Tornetta P, Aschenbrenner J. Standard multiplanar fluoroscopy versus a fluoroscopically based navigation system for the percutaneous insertion of iliosacral screws: a cadaver study. J Orthop Trauma. 2005;19:254–258. | Comparacion directa navegacion vs fluoroscopia en cadaver; segunda fuente del rango 1.8–7.3 minutos de radiacion. |
| 16. Matta JM, Saucedo T. Internal fixation of pelvic ring fractures. Clin Orthop Relat Res. 1989;242:83–97. | Define la tecnica fluoroscopica de referencia (vistas inlet/outlet) sobre la que se juzga la posicion "correcta". |
| 31. Tonetti J, Carrat L, Lavallee S, Pittet L, Merloz P, Chirossel JP. Percutaneous iliosacral screw placement using image guided techniques. Clin Orthop Relat Res. 1998;354:103–110. | Colocacion guiada por imagen; metodo competidor y posible fuente de precision geometrica. |
| 11. Gautier E, Bachler R, Heini PF, Nolte LP. Accuracy of computer-guided screw fixation of the sacroiliac joint. Clin Orthop Relat Res. 2001;393:310–317. | Estudio de exactitud (accuracy) en articulacion sacroiliaca; metrica candidata para validar SAP. |
