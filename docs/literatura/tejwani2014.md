# tejwani2014 — CT postoperatoria de tornillos SI percutaneos y "safe zone" en el foramen S1

- **DOI / URL:** DOI NO ENCONTRADO EN EL PDF. URL del articulo NO ENCONTRADO EN EL PDF (solo aparece el sitio de la revista, www.amjorthopedics.com). Cita impresa en el PDF: Am J Orthop. 2014;43(11):513-516.
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/tejwani2014.pdf

## Que hace (3 lineas maximo)
Serie retrospectiva de un solo centro (46 pacientes, 51 tornillos SI percutaneos por fluoroscopia) con CT postoperatoria a <24 h, que mide en PACS cuanto penetra el tornillo en el foramen S1.
Relaciona esa penetracion con deficit neurologico nuevo y con revision quirurgica.
Propone una "safe zone": penetracion pequena en el tercio superior del foramen S1 en cortes axiales, con reduccion adecuada; el limite en mm varia en el texto (2 mm / 2.1 mm / 2.7 mm / 3 mm).

## Restriccion o supuesto clave
No es un paper de sintesis generativa; se registra el supuesto clinico-metodologico clave.
- La zona segura es condicional a la reduccion: "This potential safe zone is predicated on adequate reduction of the SI joint." (p. 516, Discussion).
- Solo se evalua penetracion hacia el foramen S1; la tabla rotula los 51 tornillos como "S1 screws" pese a que 3 casos llevaron tornillo S2 (p. 514, Surgery; p. 515, Results). No hay datos de S2.
- La definicion de la zona no tiene geometria en mm respecto de landmarks ni marco de referencia: es "superior one-third of the foramen on axial CT images" mas un limite de profundidad que el propio texto no fija de forma unica (2, 2.1, 2.7 o 3 mm segun la seccion).
- Resolucion de CT heterogenea (5.0 mm o 2.5 mm de corte) y la tasa de penetracion detectada depende de ella (p. 515, Results; p. 515, Discussion).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 23/51 tornillos (45%) con violacion del foramen S1 | "Twenty-three of the 51 screws (45%) had some violation of the S1 foramen" | Results, p. 515 |
| 43% de tornillos con penetracion (discrepa del 45%) | "resulted in neural foramen penetration in 43% of SI screws" | Discussion, p. 516 |
| Escala de 3 categorias: intraoseo / skived (<2 mm) / extruido | "skived (less than 2 mm of partial penetration into the S1 foramen)" | Postoperative Assessment, p. 514 |
| Dismorfico: 11/21 (52%); normal: 12/30 (40%) | "Eleven of 21 (52%) screws showed some penetration of the S1 foramen" | Results, p. 515 |
| Penetracion media 3.3 mm (1.6-5.7) dismorfico; 2.7 mm (1.4-7) normal | "measured 3.3 mm (range, 1.6-5.7 mm) in dysmorphic sacrum" | Results, p. 515 |
| 2.5 mm CT: 20/32 pacientes (62.5%) con penetracion | "20 (62.5%) had evidence of screw penetration" | Results, p. 515 |
| Todas las violaciones en el tercio superior del foramen | "All violations were in the superior one-third position of the foramen." | Results, p. 515 |
| Deficit neurologico nuevo: 2/46 (4%) | "Two of 46 (4%; 1 with dysmorphism, 1 without) had a new neurologic deficit" | Results, p. 515 |
| Zona segura: hasta 2 mm de penetracion foraminal | "up to 2 mm of foramen penetration is safe and does not result in neurologic deficit" | Discussion, p. 516 |
| Zona segura ampliada: hasta 3 mm (contradice lo anterior) | "expanded to include skiving of the S1 neural foramen up to 3 mm" | Discussion, p. 516 |
| Rango citado 2%-15% de malposicion por fluoroscopia, sin numero de referencia en la frase | "Malpositioned screws using fluoroscopic guidance have been reported in 2% to 15% of patients" | Introduccion, p. 514 |

## Donde entra en mi tesis
- Objetivo 2 (muestreador), implicancia #7 (fuente operacional de zona segura): es la unica definicion de "safe zone" de este paper y es foraminal-cualitativa (tercio superior del foramen S1 en axial + limite de profundidad inconsistente), no una region geometrica en mm respecto de landmarks. Computable en CT solo si se segmenta el foramen S1; no encaja directamente con la holgura cortical de 5 mm de kaiser2014dysmorphism ni con Dmax >= d_implante + 2c de mclaren2021corridor.
- Implicancia #58 (escala de brecha): aporta un criterio iliosacro propio de 3 categorias con corte unico de 2 mm (intraoseo / skived <2 mm / extruido), sin cita de origen y sin conteos por categoria. No sirve como prior ordinal.
- Implicancias #12/#28 y #59 (S1 vs S2): no aporta nada sobre S2; solo S1.
- Contexto de la discusion del benchmark: la tasa de penetracion detectada sube con CT de 2.5 mm (62.5% de pacientes), argumento de que la frecuencia de brecha depende de la resolucion de la imagen de referencia.
- Posible origen citado del rango "2% to 15%" (ver Dudas).

## Dudas para el asesor
1. El paper es internamente inconsistente en el umbral de la zona segura: abstract "superior 2 mm" y ">2.7 mm"; Results "<2.1 mm"; Discussion "up to 3 mm" y "up to 2 mm". Si se cita, cual cifra se toma, o se cita solo como definicion cualitativa (tercio superior del foramen S1 en axial)?
2. Conteo de deficit inconsistente: abstract "4 unchanged / 6 new"; Results "2 unchanged / 8 new" y luego "remaining 4"; Discussion "only 1 patient" iatrogenico frente a 2/46 en Results y Tabla.
3. Conteo de tornillos: 41 pacientes con 1 tornillo + 2 transiliacos + 3 casos con 2 tornillos (S1 y S2) no suma 51 salvo supuestos no declarados; el abstract habla de "51 fractures or widenings" y la seccion Surgery reparte diametros en 42 + 4 fracturas.
4. La Tabla llama "S1 screws" a los 51 tornillos aunque 3 casos llevaron S2: los porcentajes deben leerse como mezcla no desagregada o como solo-S1?
5. La escala de 3 categorias (intraoseo/skived/extruido) no reporta cuantos tornillos cayeron en cada una ni cita su origen. Aporta algo a #58 mas alla de mostrar que otro grupo iliosacro usa un corte de 2 mm?
6. La frase "2% to 15% of patients" (p. 514) no lleva numero de referencia. Conviene cruzarla con la nota de keating1999iliosacral, que no publica ese rango.
7. Afirman que el CT de 2.5 mm detecta mas penetracion con "P = .3", lo que no es significativo. Usar solo como observacion descriptiva?

## Evidencia textual
| Cifra / criterio / definicion | Frase original (maximo 15 palabras) | Seccion / pagina |
|---|---|---|
| Fracturas pelvicas = 3% de fracturas esqueleticas | "Pelvic injuries account for 3% of all skeletal fractures." | Introduccion, p. 513 |
| Malposicion reportada hasta 24% (ref. 5, Tonetti) | "reports have found screw misplacements as high as 24%" | Introduccion, p. 513 |
| Complicacion neurologica hasta 18% (refs. 6-9) | "neurologic complication rates up to 18%" | Introduccion, p. 513 |
| Displasia sacra 20%-40% (ref. 10) | "Sacral dysplasia has been reported to occur in up to 20% to 40%" | Introduccion, p. 514 |
| Malposicion por fluoroscopia 2%-15% de pacientes (sin numero de referencia en la frase) | "Malpositioned screws using fluoroscopic guidance have been reported in 2% to 15% of patients" | Introduccion, p. 514 |
| Compromiso neurologico 0.5%-7.7% (sin numero de referencia en la frase) | "with an incidence of neurologic compromise between 0.5% and 7.7%" | Introduccion, p. 514 |
| 4 grados de desvio pueden danar estructuras (ref. 14) | "As little as 4° of misdirection can result in damage to neurovascular structures" | Introduccion, p. 514 |
| Periodo del estudio | "between July 1, 2005, and June 30, 2010" | Materials and Methods, p. 514 |
| Tecnica de referencia: Routt 1995 | "according to the method described by Routt in 1995" | Materials and Methods, p. 514 |
| Cohorte: 46 pacientes, 26 hombres, 20 mujeres | "46 patients who met the inclusion criteria were 26 men and 20 women" | Materials and Methods, p. 514 |
| Edad media 42 (16-73) | "a mean age of 42 years (range, 16 to 73 years)" | Materials and Methods, p. 514 |
| Mecanismo: 13 accidentes de transito, 19 aplastamiento | "Motor vehicle accidents accounted for 13 cases; 19 were crush injuries" | Materials and Methods, p. 514 |
| Mecanismo: 14 caidas de altura | "14 were falls from height" | Materials and Methods, p. 514 |
| Dismorfismo sacro 17 (37%) | "Seventeen patients (37%) met the radiographic criteria for sacral dysmorphism." | Materials and Methods, p. 514 |
| Criterios radiograficos de dismorfismo usados | NO ENCONTRADO EN EL PDF | — |
| Politrauma 42/46 | "Forty-two of the 46 patients were polytrauma patients" | Materials and Methods, p. 514 |
| Deficit neurologico al ingreso: 6 | "Six patients presented with some neurologic deficit at the time of injury" | Materials and Methods, p. 514 |
| Young-Burgess: 3 VS, 13 LC (y 17 APC, 7 sacras, 6 combinadas) | "there were 3 vertical shear injuries, 13 lateral compression–type injuries" | Materials and Methods, p. 514 |
| Denis: 3 zona 1, 3 zona 2, 1 zona 3 | "there were 3 Denis zone 1, 3 Denis zone 2, and 1 Denis zone 3" | Materials and Methods, p. 514 |
| Cobertura del CT | "The pelvic CT scan included the entire pelvis from the ilium" | Materials and Methods, p. 514 |
| Grosor de corte CT: 5.0 o 2.5 mm | "Each scan consisted of either a 5.0-mm or a 2.5-mm sequential axial image." | Materials and Methods, p. 514 |
| Analisis en PACS (Centricity 2.1) con algoritmo oseo | "was used to analyze each scan with a bone algorithm" | Materials and Methods, p. 514 |
| Desplazamiento inicial: ensanchamiento SI a nivel S1 con calibre digital | "SI joint widening at the level of the S1 and was measured using digital calipers" | Materials and Methods, p. 514 |
| kVp, mAs, fabricante del tomografo, kernel especifico | NO ENCONTRADO EN EL PDF | — |
| Tiempo a cirugia 4 dias (2-15) | "Mean time to surgery was 4 days (range, 2 to 15 days)" | Surgery, p. 514 |
| 51 tornillos en 46 pacientes | "A total of 51 SI screws were implanted in 46 patients." | Surgery, p. 514 |
| 1 tornillo en 41 pacientes; 2 transiliacos | "stabilized with 1 screw in 41 patients, 2 cases required a transiliac screw" | Surgery, p. 514 |
| 2 tornillos (S1 y S2) en 3 casos | "2 screws (S1 and S2) were placed in each of the remaining 3 cases" | Surgery, p. 514 |
| Diametro 7.3 o 7.5 mm, canulados, parcialmente roscados | "partially threaded 7.3- or 7.5-mm–diameter cannulated screws" | Surgery, p. 514 |
| 42 fracturas con 7.3/7.5 mm; 4 con 6.5 mm | "in 42 fractures and 6.5-mm screws (Synthes, Inc) in 4 fractures" | Surgery, p. 514 |
| 11 casos con tornillo totalmente roscado (fractura sacra) | "In 11 cases where the fracture was through the sacrum, fully threaded" | Surgery, p. 514 |
| Longitud de los tornillos | NO ENCONTRADO EN EL PDF | — |
| Guia: fluoroscopia con vistas inlet, outlet y lateral sacra | "Screw insertion was performed under fluoroscopic guidance with inlet, outlet, and lateral sacral views." | Surgery, p. 514 |
| Navegacion o guia por CT intraoperatoria | NO ENCONTRADO EN EL PDF (solo fluoroscopia en esta cohorte) | — |
| 2 cirujanos | "One of 2 fellowship-trained trauma surgeons performed the surgeries." | Surgery, p. 514 |
| CT postoperatoria dentro de 24 h | "Pelvic CT was also obtained within 24 hours of surgery" | Postoperative Assessment, p. 514 |
| Medicion de penetracion con herramienta PACS | "Using the measurement tool on the PACS system, we measured the penetration" | Postoperative Assessment, p. 514 |
| Criterio: intraoseo | "intraosseous (completely contained within the sacral bone)" | Postoperative Assessment, p. 514 |
| Criterio: skived, <2 mm de penetracion parcial en foramen S1 | "skived (less than 2 mm of partial penetration into the S1 foramen)" | Postoperative Assessment, p. 514 |
| Criterio: extruido | "extruded (the screw not contained by the bone)" | Postoperative Assessment, p. 514 |
| Fuente bibliografica de la escala de 3 categorias | NO ENCONTRADO EN EL PDF | — |
| Conteo de tornillos por categoria (intraoseo / skived / extruido) | NO ENCONTRADO EN EL PDF | — |
| Evaluacion en radiografias y en cortes axiales de CT | "evaluated on the radiographic images as well as the axial images of the CT scans" | Postoperative Assessment, p. 514 |
| Numero de observadores / concordancia inter-observador de la medicion | NO ENCONTRADO EN EL PDF | — |
| Seguimiento medio 12 meses (8 meses-2 anos) | "The mean follow-up time was 12 months (range, 8 months to 2 years)." | Results, p. 514 |
| 2 fallecidos por lesiones asociadas | "Two patients expired secondary to associated injuries." | Results, p. 514 |
| Criterio de reduccion: Matta, dentro de 1 cm | "According to Matta's criteria of anatomic reduction within 1 cm" | Results, p. 514 |
| Deficit postoperatorio 10/46; 4 sin cambio (abstract) | "10 of 46 patients had postoperative neurologic deficit, 4 of which were unchanged" | Abstract, p. 513 |
| Deficit postoperatorio 10/46; 2 sin cambio (Results, discrepa) | "10 of 46 patients had postoperative neurologic deficit, 2 of which were unchanged" | Results, p. 514 |
| Abstract: 6 con deficit nuevo; penetracion 2.1 y 7.0 mm en 2 | "CT showed neural foramen penetration of 2.1 and 7.0 mm in 2 patients" | Abstract, p. 513 |
| Results: 8 con deficit nuevo; >2.1 mm en solo 2 | "CT showed neural foramen penetration greater than 2.1 mm in only 2 patients." | Results, p. 514 |
| Revision de ambos tornillos con mejoria | "Both patients underwent screw revision, resulting in improved neurologic deficit." | Results, p. 515 |
| 4 pacientes sin penetracion recuperan a las 2-6 semanas | "return to presurgical status by 6 weeks without necessitating screw removal" | Results, p. 515 |
| Penetracion en 23/51 tornillos (45%) | "Twenty-three of the 51 screws (45%) had some violation of the S1 foramen" | Results, p. 515 |
| Dismorfico: 17 pacientes, 21 tornillos S1 | "17 patients with dysmorphic sacrums in which 21 S1 screws were placed" | Results, p. 515 |
| Dismorfico: 11/21 (52%) con penetracion | "Eleven of 21 (52%) screws showed some penetration of the S1 foramen" | Results, p. 515 |
| Normal: 29 pacientes, 30 tornillos S1 | "29 patients with normal sacral morphology in which 30 S1 screws were placed" | Results, p. 515 |
| Normal: 12/30 (40%) con penetracion | "Twelve of 30 (40%) screws penetrated the S1 foramen." | Results, p. 515 |
| Localizacion: tercio superior del foramen | "All violations were in the superior one-third position of the foramen." | Results, p. 515 |
| Deficit nuevo asociado a cirugia 2/46 (4%) | "Two of 46 (4%; 1 with dysmorphism, 1 without) had a new neurologic deficit" | Results, p. 515 |
| CT alta resolucion en 32; 5.0 mm en 14 | "High-resolution CTs were obtained in 32 patients, while 14 patients underwent the standard 5.0-mm–cut CTs" | Results, p. 515 |
| CT 2.5 mm: 20/32 (62.5%) con penetracion | "20 (62.5%) had evidence of screw penetration" | Results, p. 515 |
| Tasa de penetracion en el subgrupo de CT 5.0 mm | NO ENCONTRADO EN EL PDF | — |
| Comparacion 2.5 vs 5.0 mm, P = .3 | "were more likely to show neural foramen penetration (P = .3)" | Results, p. 515 |
| Penetracion media dismorfico 3.3 mm (1.6-5.7) | "measured 3.3 mm (range, 1.6-5.7 mm) in dysmorphic sacrum" | Results, p. 515; Tabla, p. 515 |
| Penetracion media normal 2.7 mm (1.4-7) | "2.7 mm (range, 1.4-7 mm) in normal sacrum" | Results, p. 515; Tabla, p. 515 |
| Abstract: penetracion media global 3.3 mm (1.4-7.0) | "23 of 51 screws had some foramen penetration with an average of 3.3 mm" | Abstract, p. 513 |
| Umbral: <2.1 mm sin deficit (Results) | "foramen penetration of less than 2.1 mm on CT did not result in neurologic deficit" | Results, p. 515 |
| Umbral: sin correlacion salvo >2.7 mm (abstract) | "did not correlate with neurologic deficit unless the penetration was greater than 2.7 mm" | Abstract, p. 513 |
| Criterio de retiro: penetracion >2.1 mm | "screw removal if foramen penetration is greater than 2.1 mm" | Abstract, p. 513 |
| Revision por penetracion en 2/10 con deficit | "cause of revision surgery in 2 of 10 patients with postoperative neurologic deficit" | Abstract, p. 513 |
| Definicion safe zone (abstract): 2 mm superiores del foramen | "safe zone for screw insertion encompassing the superior 2 mm of the sacral foramen" | Abstract, p. 513 |
| Tabla: totales 46 pacientes / 51 tornillos / 23 con / 28 sin penetracion / 2 deficit nuevo | "Radiologic Results of Screw Penetration on Computed Tomography" (titulo de la Tabla; cifras en celdas) | Tabla, p. 515 |
| Pelvis fracturas = 5% de ingresos por trauma | "represent approximately 5% of all trauma admissions and 3% of all skeletal fractures" | Discussion, p. 515 |
| Tecnica de Letournel: 1 o 2 tornillos de 6.5-7.3 mm | "1 or 2 large screws (6.5-7.3 mm in diameter)" | Discussion, p. 515 |
| Arco medio de 67 grados entre inlet y outlet | "with the average arc (67º) between the ideal inlet and outlet" | Discussion, p. 515 |
| Ebraheim (ref. 6): raiz S1 a 8.7 mm inferior y 7.8 mm medial | "8.7 mm inferior and 7.8 mm medial to the starting point for a pedicle screw" | Discussion, p. 516 |
| Safe zone ampliada a skiving de hasta 3 mm | "expanded to include skiving of the S1 neural foramen up to 3 mm" | Discussion, p. 516 |
| Penetracion en 43% de tornillos (discrepa del 45%) | "resulted in neural foramen penetration in 43% of SI screws" | Discussion, p. 516 |
| Hasta 2 mm no correlaciona con deficit | "screw penetration up to 2 mm does not correlate with neurologic deficit" | Discussion, p. 516 |
| Deficit iatrogenico por perforacion en 1 paciente (discrepa de 2/46) | "Iatrogenic neurologic deficit secondary to perforation of the foramina occurred in only 1 patient." | Discussion, p. 516 |
| Definicion safe zone (discusion): tercio superior del foramen en CT axial | "small amounts of penetration in the superior one-third of the foramen on axial CT images" | Discussion, p. 516 |
| Condicion de la safe zone: reduccion adecuada | "This potential safe zone is predicated on adequate reduction of the SI joint." | Discussion, p. 516 |
| Colocacion ideal: rozar el borde superior del foramen S1 | "Our ideal screw placement skives the superior S1 foramen allowing for a larger screw diameter" | Discussion, p. 516 |
| Landmarks, coordenadas o dimensiones en mm de la safe zone respecto del hueso | NO ENCONTRADO EN EL PDF | — |
| Lesion nerviosa iatrogenica 0%-6% (refs. 14, 21) | "Iatrogenic nerve injuries are reported to occur in 0% to 6%" | Discussion, p. 516 |
| Criterio de indicacion de CT postoperatoria | "A postoperative CT is not indicated unless there are findings of a postoperative nerve injury." | Discussion, p. 516 |
| Conclusion: hasta 2 mm de penetracion es seguro | "up to 2 mm of foramen penetration is safe and does not result in neurologic deficit" | Discussion, p. 516 |
| Datos de malposicion o penetracion en S2 | NO ENCONTRADO EN EL PDF | — |
| Distribucion ordinal de grados de brecha (cualquier nivel) | NO ENCONTRADO EN EL PDF | — |
| Tasa de malposicion detectada en radiografias (cifra) | NO ENCONTRADO EN EL PDF (solo afirma que ninguna radiografia mostro malposicion obvia, p. 515) | — |
| Tasa de penetracion por paciente en la cohorte completa | NO ENCONTRADO EN EL PDF | — |
| Brecha cortical fuera del foramen (anterior, canal, cuerpo) | NO ENCONTRADO EN EL PDF | — |
| Umbral de 10 mm | NO ENCONTRADO EN EL PDF | — |
