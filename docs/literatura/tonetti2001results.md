# tonetti2001results — Clinical results of percutaneous pelvic surgery: CAS by ultrasound vs standard fluoroscopy

- **DOI / URL:** 10.3109/10929080109146084 (portada Taylor & Francis, p. 1 del PDF); la pagina impresa trae ademas "DOI 10.1002/igs.10010" (p. 204). Computer Aided Surgery 6:204-211 (2001)
- **Nivel de lectura:** 3 (contexto) — PROPUESTO por Claude
- **Leido a fondo por la autora:** no
- **PDF:** papers/tonetti2001results.pdf

## Que hace (3 lineas maximo)
Compara 4 pacientes / 10 tornillos iliosacros colocados con navegacion basada en CT preoperatoria y registro por ultrasonido (CAS) contra una serie historica de 30 pacientes / 51 tornillos por fluoroscopia percutanea.
Evalua posicion con CT postoperatoria: conteo binario de trayectorias "outside bone" y un "security score" continuo (0-100%) solo para los intraoseos.
Fluoroscopia: 12 tornillos fuera de hueso y 7 lesiones neurologicas iatrogenicas; CAS: 0 y 0. Sin pruebas estadisticas.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Restriccion relevante para la tesis: la malposicion es **binaria** (dentro/fuera del hueso, con direccion anterior o foraminal) y no se mide la magnitud de la perforacion en mm. El unico indice graduado es el *"security score"*, que se calcula con las distancias del tornillo a la cortical anterior (A) y al canal/foramen S1 (B), y *"The score was not calculated for negative values"* (Method of Evaluation, p. 208): solo describe margenes de tornillos intraoseos, no grados de brecha. No hay separacion por nivel sacro; el texto describe solo tornillos al cuerpo de S1.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
Ninguno propuesto para `main.tex`. Si la autora decide citarlo como contexto (tasa binaria historica por fluoroscopia), las cifras candidatas son:

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 12 tornillos fuera de hueso (23%), fluoroscopia | "Outside bone trajectories 12 (23%) 0 (0%)" | Table 1, p. 209 |
| 0 fuera de hueso con CAS | "No trajectories outside the bone and no postoperative neurological deficits" | Abstract, p. 204 |
| 7 lesiones neurologicas por tornillo extraoseo (13%) | "Neurological lesion due to screw outside bone 7 (13%) 0 (0%)" | Table 1, p. 209 |
| Curva de aprendizaje | "all the outside-bone trajectories occurred in the first 15 patients" | Discussion, p. 210 |

## Donde entra en mi tesis
Objetivo 2 (muestreador / metrica SAP), solo como contexto historico. **No aporta distribucion ordinal**: ni S1 ni S2, ni tercera distribucion. Sus 12/51 son un conteo binario que, bajo la escala de Smith/Zwingmann, no se puede repartir entre los grados 1, 2 y 3 porque la perforacion no se mide en mm. Los 39 intraoseos corresponderian al grado 0 (inferencia del asistente, no afirmacion del paper). Ademas, mide sobre tornillos (12/51) pero describe la direccion de la malposicion por pacientes (8 + 3 + 1), y los dos brazos usan tornillos de calibre distinto (7 mm frente a 6.5 mm).

Valor de trazabilidad: es la fuente a la que `tejwani2014` atribuye *"screw misplacements as high as 24%"*; la misma cifra reaparece en la cadena de `gardner2010safezones` (implicancia #12, entrada "Gardner NO usa el 2%-15%"). **El PDF imprime 23%, no 24%.** 12/51 = 23.5% (calculo del asistente), asi que el 24% podria ser un redondeo distinto hecho por quien cita. El paper no declara el denominador del porcentaje.

## Dudas para el asesor
- El 7 (13%) de lesiones neurologicas no tiene denominador declarado: 7/51 = 13.7% y 7/30 = 23.3% (calculos del asistente). Ninguno redondea exactamente a 13. Si se cita, conviene citar el conteo (7) y no el porcentaje.
- La direccion de la malposicion se cuenta "in eight patients", "in three patients", "in one patient" (p. 209), sumando 12, igual que los 12 tornillos. No queda claro si la unidad es paciente o tornillo.
- Los "four cases" con tornillo demasiado corto (C negativo) no quedan claramente dentro o fuera de los 39 intraoseos, y el score *"was not calculated for negative values"*.
- La CAS de este paper es navegacion sobre CT **preoperatoria** con registro por ultrasonido; no hay CT intraoperatoria. No debe equipararse sin mas al brazo "navegado" de `zwingmann2009navigated`.
- Discrepancia de la capa de texto del PDF (OCR) frente a la imagen de la Tabla 2: la capa de texto dice B = 1.2, C = 1.5 y A = 8.1 donde la imagen muestra 7.2, 7.5 y 8.7. Los valores de la imagen son consistentes con la formula del score (p. ej., A = 3.6 y B = 7.2 dan 67%, que coincide con la tabla; comprobacion del asistente). En esta ficha se usan los valores de la imagen.

## Respuestas a preguntas especificas
1. **Tecnica, n y niveles.** Dos brazos: CAS = navegacion basada en CT preoperatoria (cortes de 3 mm) con registro por ultrasonido y guia pasiva de perforacion, mas una vista fluoroscopica lateral de control; y fluoroscopia percutanea estandar (serie historica). CAS: 4 pacientes, 10 tornillos. Fluoroscopia: 30 pacientes, 51 tornillos (Abstract, p. 204; Table 1, p. 209). Nivel: el texto solo describe tornillos al cuerpo de S1 (*"Two screws are placed into the S1 body"*, p. 205; *"pushed through the S1 body up to the mid-sagittal line"*, p. 205). **Conteo por nivel S1/S2: NO ENCONTRADO EN EL PDF.** Tornillos en S2: NO ENCONTRADO EN EL PDF.
2. **Evaluacion de la posicion.** Con CT postoperatoria en cada paciente, reconstruida en planos transverso, coronal y sagital relativos al eje del tornillo; las medidas se toman en el transverso (p. 208). Grosor de corte de la CT postoperatoria: NO ENCONTRADO EN EL PDF. Quien leyo y si hubo cegamiento: NO ENCONTRADO EN EL PDF. Escala: (a) binaria dentro/fuera del hueso, con direccion (anterior, foramen S1 o ambas); (b) security score continuo de 0 a 100% a partir de A y B, solo para los intraoseos. **No es ordinal ni compatible con Smith/Zwingmann**: no mide mm de perforacion. Escala ordinal de brecha cortical: NO ENCONTRADO EN EL PDF.
3. **Tasas.** Fluoroscopia: 12 fuera de hueso, 23% (Table 1): 8 anteriores, 3 foraminales (S1) y 1 anterior y foraminal (p. 209). Ademas hubo 4 tornillos demasiado cortos (C negativo). CAS: 0 de 10. Security score medio: 63% en fluoroscopia (n = 39 intraoseos) y 62% en CAS (n = 10) (Table 2, p. 209). **Tasa por nivel: NO ENCONTRADO EN EL PDF.**
4. **Complicaciones neurologicas.** Fluoroscopia: 18 pacientes con deficit postoperatorio (7 tronco lumbosacro, 5 raiz S1, 6 cauda equina), de los cuales 8 ya eran conocidos antes de la cirugia. De los 10 nuevos, 6 se explican por trayectorias extraoseas; se suma 1 paciente fallecido con trayectoria extraosea, registrado como posible lesion iatrogenica: total 7. De las otras 5 trayectorias extraoseas, 2 no tuvieron deficit y 3 ya tenian deficit previo (p. 209). CAS: sin lesiones. La relacion es de asociacion por conteo; **no hay relacion con magnitud en mm**, porque la magnitud no se mide.
5. **Distribucion ordinal S2 o tercera distribucion para SAP: NO.** No hay grados, no hay mm de perforacion y no hay nivel S2. A lo sumo es un punto binario historico (fluoroscopia 12/51 frente a CAS 0/10) con n muy pequeno en CAS y sin pruebas estadisticas (*"No statistical comparison tests were done"*, p. 208).

## Evidencia textual
| Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Revista y paginas | "Computer Aided Surgery 6:204-211 (2001)" | Encabezado, p. 204 |
| DOI (portada T&F) | "DOI: 10.3109/10929080109146084" | Portada, p. 1 del PDF |
| DOI (pagina impresa) | "DOI 10.1002/igs.10010" | Pie, p. 204 |
| Fechas | "Received November 15, 2000; accepted June 23, 2001." | Pie, p. 204 |
| Diseno: serie historica | "with comparison to a historical series of patients treated using percutaneous fluoroscopy" | Abstract, p. 204 |
| CAS: 4 pacientes, 10 tornillos | "Four patients were instrumented using a CAS system, with 10 screws" | Abstract, p. 204 |
| Fluoroscopia: 30 pacientes, 51 tornillos | "Thirty patients were treated by percutaneous fluoroscopic screwing, with 51 screws" | Abstract, p. 204 |
| Criterio: CT | "screw placement evaluation on CT-scan" | Abstract, p. 204 |
| CAS radiacion | "average radiation time was 0.35 min per patient and 0.14 min per screw" | Abstract, p. 204 |
| Fluoro radiacion | "average radiation time was 1.03 min per patient and 0.6 min per screw" | Abstract, p. 204 |
| 12 extraoseos y 7 deficits | "Twelve screws had outside-bone trajectories, and iatrogenic neurological deficits ... seven patients" | Abstract, p. 204 |
| Tiempo operatorio medio | "average operative time was 50 min in the CAS group and 35 min" | Abstract, p. 204 |
| Cirugia abierta: complicaciones de herida (ref. 2) | "with a 6-25% incidence of wound complications like hematoma and infection" | Introduction, p. 204 |
| Letournel 1978 | "first report of an iliosacral screwing technique was published by Letournel in 1978" | Introduction, p. 204 |
| Matta y Saucedo 1989 | "In 1989, Matta and Saucedo introduced fluoroscopic operative control" | Introduction, p. 204 |
| Nivel S1 | "Two screws are placed into the S1 body through the iliosacral joint" | Introduction, p. 205 |
| Corredor (ref. 11) | "narrow corridor with sectional dimensions of 22 mm by 11 mm (mean values)" | Introduction, p. 205 |
| Estructuras en riesgo | "proximity of the neurologic trunk to the prolumbosacral trunk and S1 root" | Introduction, p. 205 |
| Fluoro: control lateral | "Before crossing the S1-S2 foramen, the drill trajectory was checked" | Material and Methods, p. 205 |
| Fluoro: profundidad | "the pin was pushed through the S1 body up to the mid-sagittal line" | Material and Methods, p. 205 |
| Fluoro: broca | "A cannulated drill of 4 mm diameter was placed along the pin guide" | Material and Methods, p. 205 |
| Fluoro: tornillo | "cannulated screw of 7 mm diameter and 32 mm thread length" | Material and Methods, p. 205 |
| CAS: CT preoperatoria | "CT-scan acquisition of nearly 50 images with 3-mm slice thickness" | Material and Methods, p. 205 |
| CAS: planificacion | "Each trajectory was defined by an entry point and a direction" | Material and Methods, p. 205 |
| CAS: sonda | "standard ultrasound probe of 7.5 MHz frequency" | Material and Methods, p. 205 |
| CAS: campo de la sonda | "examination field of 2 cm width and 5 cm depth" | Material and Methods, p. 205 |
| CAS: imagenes US | "nearly 30 ultrasound images of the interface between soft tissue and the sacrum" | Material and Methods, p. 206 |
| CAS: registro | "registered with the preoperative 3D CT-scan model ... surface-based registration algorithm" | Material and Methods, p. 206 |
| CAS: control fluoroscopico | "the trajectory was controlled with reference to one fluoroscopic lateral view" | Passive Drilling Guidance, p. 207 |
| CAS: tornillo | "The implant was a 6.5-mm diameter screw for cancellous bones" | Passive Drilling Guidance, p. 207 |
| CAS: rosca | "with a 32 mm-long thread and a washer" | Passive Drilling Guidance, p. 207 |
| Fluoro: sexo y edad | "23 males and 7 females, with an average age of 34.7 years" | Patient Population, p. 207 |
| Fluoro: rango de edad | "(range: 17 to 60 years)" | Patient Population, p. 207 |
| Fluoro: Tile | "B1 lesions were found in 3 cases, C1 in 17 cases, C2 in 4" | Patient Population, pp. 207-208 |
| Fluoro: Tile (cont.) | "and C3 in 5 cases" | Patient Population, p. 208 |
| Fluoro: fractura aislada | "One patient presented an isolated fracture of the sacrum." | Patient Population, p. 208 |
| Fluoro: configuracion 1 | "A single iliosacral lag screw was implanted in 13 patients" | Patient Population, p. 208 |
| Fluoro: configuracion 2 | "two screws were implanted unilaterally in 12 patients" | Patient Population, p. 208 |
| Fluoro: configuracion 3 | "In three cases, bilateral screwing ... using one screw for each side" | Patient Population, p. 208 |
| Fluoro: configuracion 4 | "2 patients had two screws implanted in both articulations" | Patient Population, p. 208 |
| Fluoro: deficit preoperatorio | "eight neurologic lesions of the lumbosacral trunk or S1 root" | Patient Population, p. 208 |
| Fluoro: sin lesion preop. | "and 13 patients with no lesions" | Patient Population, p. 208 |
| Fluoro: no evaluables preop. | "For nine patients ... the clinical preoperative examination was impossible" | Patient Population, p. 208 |
| CAS: periodo | "From February 2000 to April 2000, this new technique was used" | Patient Population, p. 208 |
| CAS: sexo | "in four patients; one male and three females" | Patient Population, p. 208 |
| CAS: edad | "average age was 48.5 years (range: 34 to 71 years)" | Patient Population, p. 208 |
| CAS: indicaciones | "Two patients had a recent unilateral traumatic lesion of the sacral ala" | Patient Population, p. 208 |
| CAS: tumor | "circular fusion of the pelvic ring because of tumor reconstruction" | Patient Population, p. 208 |
| CAS: dos tornillos por fusion | "Each iliosacral fusion was done with two screws." | Patient Population, p. 208 |
| CAS: sin deficit preop. | "Preoperative neurological examinations found no deficits in the lower limbs." | Patient Population, p. 208 |
| Fluoro: periodo de la serie historica | NO ENCONTRADO EN EL PDF | — |
| Evaluacion: CT postoperatoria | "A postoperative CT scan was performed for each patient" | Method of Evaluation, p. 208 |
| Planos de reconstruccion | "reconstruction using the transverse and coronal planes relative to the axis" | Method of Evaluation, p. 208 |
| Plano sagital | "perpendicular to the screw's axis in the narrowest zone of the sacral ala" | Method of Evaluation, p. 208 |
| Plano de medida | "measurements were done in the transverse plane (Fig. 6)" | Method of Evaluation, p. 208 |
| Grosor de corte de la CT postoperatoria | NO ENCONTRADO EN EL PDF | — |
| Lector / cegamiento | NO ENCONTRADO EN EL PDF | — |
| Definicion de A | "A was the distance from the screw to the anterior cortex" | Method of Evaluation, p. 208 |
| Definicion de B | "distance from the screw to the spinal canal or to the S1 foramen" | Method of Evaluation, p. 208 |
| Definicion de C | "distance from the tip of the screw to the mid-sagittal line" | Method of Evaluation, p. 208 |
| Score = 0% | "If A or B = 0, the security score is 0%" | Method of Evaluation, p. 208 |
| Score = 100% | "If A = B, the security score is 100% because the screw is accurately centered" | Method of Evaluation, p. 208 |
| Score no definido para negativos | "The score was not calculated for negative values." | Method of Evaluation, p. 208 |
| Formula A >= B | "For A ≥ B: score = [- 200 A/(A + B)] + 200" | Method of Evaluation, p. 208 |
| Formula B > A | "for B > A: score = [- 200 B/(A + B)] + 200" | Method of Evaluation, p. 208 |
| Aflojamiento | "radiographic evaluation at 3 months to detect any loosening" | Method of Evaluation, p. 208 |
| Escala de dolor | "visual evaluation scale (from 0 to 10)" | Method of Evaluation, p. 208 |
| Estadios OMS | "0 = no antalgic drug used; 1 = peripheral action antalgic drug" | Method of Evaluation, p. 208 |
| Estadios OMS (cont.) | "2 = minor central antalgic; 3 = major central antalgic" | Method of Evaluation, p. 208 |
| Majeed | "Majeed clinical grading was done at 6 months" | Method of Evaluation, p. 208 |
| Sin estadistica | "No statistical comparison tests were done because of the small number" | Method of Evaluation, p. 208 |
| Escala ordinal de brecha cortical en mm | NO ENCONTRADO EN EL PDF | — |
| Fluoro: longitud de tornillos | "average length of the screws was 85.5 mm (range: 65 to 110 mm)" | Results, p. 208 |
| Fluoro: tiempo operatorio | "25 min for one screw and 40 min for two screws" | Results, p. 208 |
| Fluoro: radiacion por paciente | "1.03 min (range: 0.1 to 3.1 min)" | Results, p. 208 |
| Fluoro: radiacion por tornillo | "average duration of radiation exposure per screw was 0.6 min" | Results, p. 208 |
| Fluoro: kV/mA medidos en 16 | "voltage and intensity of the radiation exposure was measured for 16 patients" | Results, p. 208 |
| Fluoro: kV | "average voltage of 74.9 kV per patient (range: 64 to 110 kV)" | Results, p. 208 |
| Fluoro: mA | "average intensity of 3.6 mA per patient (range: 2.1 to 7.1 mA)" | Results, p. 208 |
| Fluoro: 12 mal colocados | "the fluoroscopic group found 12 misplaced screws" | Results, p. 209 |
| Direccion: anterior | "In eight patients the screws were misplaced to the anterior" | Results, p. 209 |
| Direccion: foraminal | "in three patients the misplaced screws crossed the S1 root foramen" | Results, p. 209 |
| Direccion: ambas | "in one patient the misplacement was both anterior and foraminal" | Results, p. 209 |
| Tornillos cortos | "In four cases the screws were too short, with negative C values" | Results, p. 209 |
| Medias solo intraoseos | "calculated only for inside-bone trajectories (n = 39)" | Results, p. 209 |
| Score medio fluoro | "The average score was 63% (see Table 2)." | Results, p. 209 |
| Neuro postop.: sin deficit / con deficit | "11 patients with no deficit and 18 patients with a deficit" | Results, p. 209 |
| Neuro: tipo de lesion | "7 patients with a lesion of the lumbosacral trunk, 5 ... S1 root" | Results, p. 209 |
| Neuro: cauda equina | "and 6 patients with a cauda equina lesion" | Results, p. 209 |
| Neuro: fallecido | "One patient died in the resuscitation unit, so no evaluation was possible" | Results, p. 209 |
| Neuro: previas | "Of these 18 neurological lesions, 8 were already known preoperatively." | Results, p. 209 |
| Neuro: nuevas explicadas | "Of the 10 preoperatively unknown lesions, 6 can be explained by outside-bone trajectories." | Results, p. 209 |
| Neuro: total asociado | "seven neurological lesions were found with outside-bone trajectories" | Results, p. 209 |
| Extraoseos sin nuevo deficit | "no neurologic deficit was found in two cases, and three cases had a deficit" | Results, p. 209 |
| Fluoro: dolor | "average value of 3.2 (range: 0 to 8)" | Results, p. 209 |
| Fluoro: OMS medio | "The average OMS stage was 0.7" | Results, p. 209 |
| Fluoro: OMS desglose | "no antalgic drugs-17 patients; peripheral action antalgic drugs-4 patients" | Results, p. 209 |
| Fluoro: OMS desglose (cont.) | "minor central antalgic-7 patients; major central antalgic-1 patient" | Results, p. 209 |
| Fluoro: Majeed | "had a mean of 78.5 (range: 22 to 100)" | Results, p. 209 |
| Fluoro: aflojamiento | "Loosening of the implanted screws was observed in three patients" | Results, p. 209 |
| CAS: longitud de tornillos | "average length of 76 mm (range: 70 to 85 mm)" | Results, p. 209 |
| CAS: tiempo operatorio | "50 min for one screw and 60 min for two screws" | Results, p. 209 |
| CAS: radiacion | "average irradiation time per patient was 0.35 min (range: 0.1 to 0.5 min)" | Results, p. 209 |
| CAS: kV | "average voltage was 78 kV per patient (range: 68 to 89 kV)" | Results, p. 209 |
| CAS: mA | "average intensity was 3.1 mA per patient (range: 3.1 to 3.2 mA)" | Results, p. 209 |
| CAS: todos bien colocados | "All the screws were well placed, with an average score of 62%" | Results, p. 209 |
| CAS: sin lesion neurologica | "no postoperative neurological lesions was found" | Results, p. 209 |
| CAS: dolor | "mean value of 4.25 on the visual scale (range: 1 to 6)" | Results, p. 209 |
| CAS: OMS | "the average OMS stage was 0.5" | Results, p. 210 |
| CAS: Majeed | "average Majeed score was 81.5 (range: 62 to 100)" | Results, p. 210 |
| CAS: aflojamiento | "Implant loosening was observed in one 71-year-old patient" | Results, p. 210 |
| Tabla 1: pacientes | "Number of patients 30 4" | Table 1, p. 209 |
| Tabla 1: tornillos | "Number of screws 51 10" | Table 1, p. 209 |
| Tabla 1: extraoseos | "Outside bone trajectories 12 (23%) 0 (0%)" | Table 1, p. 209 |
| Tabla 1: lesion neurologica | "Neurological lesion due to screw outside bone 7 (13%) 0 (0%)" | Table 1, p. 209 |
| Tabla 1: radiacion/paciente | "Irradiation duration (min/patient) 1.03 (0.1-3.1) 0.35 (0.1-0.5)" | Table 1, p. 209 |
| Tabla 1: radiacion/tornillo | "Irradiation duration (min/screw) 0.6 0.14" | Table 1, p. 209 |
| Tabla 1: dolor | "Visual evaluation of pain 3.2 (0-8) 4.25 (1-6)" | Table 1, p. 209 |
| Tabla 1: OMS | "OMS stages 0.7 0.5 (0-2-0-0)" | Table 1, p. 209 |
| Tabla 1: aflojamiento | "Loosening of implant 3 1" | Table 1, p. 209 |
| Tabla 1: Majeed | "Majeed grading 78.5 (22-100) 81.5 (62-100)" | Table 1, p. 209 |
| Denominador de 23% y 13% | NO ENCONTRADO EN EL PDF | — |
| Tabla 2: medias fluoro (n = 39) | A 6.8, B 6.6, C 7.5 mm, score 63% (fila de la tabla, leida de la imagen) | Table 2, p. 209 |
| Tabla 2: medias CAS (n = 10) | A 5.6, B 4.3, C 2 mm, score 62% (fila de la tabla, leida de la imagen) | Table 2, p. 209 |
| Tabla 2: rango de scores CAS | valores por tornillo de 0 a 100% (P4 Sup = 0; P4 Inf = 100) | Table 2, p. 209 |
| Tabla 2: nota | "The mean values of the fluoroscopic group were calculated using only the inside-bone trajectories" | Table 2 (nota), p. 209 |
| Tasa por nivel S1/S2 | NO ENCONTRADO EN EL PDF | — |
| Conteo de tornillos en S2 | NO ENCONTRADO EN EL PDF | — |
| Sin estadistica (discusion) | "Despite the insufficient statistical analysis, the tendencies are clear." | Discussion, p. 210 |
| Curva de aprendizaje | "all the outside-bone trajectories occurred in the first 15 patients" | Discussion, p. 210 |
| Mismo score intraoseo | "the score of placement is the same in both groups for the inside-bone screws" | Discussion, p. 210 |
| Factor principal | "the most important factor is the choice of entry point" | Discussion, p. 210 |
| Gruetzner (ref. 7): tiempo | "average operative time of 50 to 105 min" | Discussion, p. 210 |
| Gruetzner (ref. 7): radiacion | "very high radiation exposure of 1.83 to 4.33 min" | Discussion, p. 210 |
| Gruetzner (ref. 7): malposicion | "These authors found two wrong trajectories for 12 screws." | Discussion, p. 210 |
| Stockle (ref. 13): modelos | "nine wrong trajectories for 60 screws" | Discussion, p. 210 |
| Stockle (ref. 13): radiacion | "average irradiation time of 6 s per screw" | Discussion, p. 210 |
| Limitacion del registro | "segmentation is done manually, being very delicate" | Discussion, p. 210 |

## Candidatos de snowballing
Ninguna referencia nueva cumple las reglas de `_candidatos.md` sin estar ya registrada o descartada:

| Cita tal como aparece | N. de ref | Estado en `_candidatos.md` |
|---|---|---|
| Gruetzner PA, Vock B, Holz F, Wentzensen A. Virtual fluoroscopy in acute treatment of pelvic ring disruptions. Syllabus of CAOS USA 2000, p 197. | 7 | Descartada en la ronda de Hinsche (congreso). Aqui se le atribuye *"two wrong trajectories for 12 screws"* (p. 210): binario, sin nivel. No se repropone; queda la nota |
| Kahler DM, Mallik K. Computer guided percutaneous iliosacral screw fixation ... compared to conventional technique. Syllabus of CAOS USA 2000, p 185-187. | 12 | Descartada en la ronda de Hinsche (congreso). El titulo sugiere navegado vs convencional; en este PDF no se le atribuye ninguna tasa |
| Stockle U, Konig B, Hofstetter R, Nolte LP, Haas NP. Virtual fluoroscopy: safe zones for pelvic screw fixations. Syllabus of CAOS USA 2000, p 199. | 13 | Descartada en la ronda de Hinsche. Modelos pelvicos, no clinica |
| Tonetti J, Cloppet O, Clerc M, et al. [Optimal placement of the iliosacral screws: 3D computed tomography simulation]. Rev Chir Orthop 2000;86:360-369. | 11 | Ya registrada (ronda 2026-09-18, "Tonetti 2000") |
| Shuler TE, Boone DC, Gruen GS, Peitzman AB. ... J Trauma 1995;38:453-458. | 2 | Ya registrada |
| Routt ML Jr, Simonian PT, Mills WJ. Iliosacral screw fixation: early complications ... 1997;11:584-589. | 19 | LEIDA (`routt1997early`) |
| Templeman D, et al. Proximity of iliosacral screws ... 1996;329:194-198. | 10 | LEIDA (`templeman1996proximity`) |
