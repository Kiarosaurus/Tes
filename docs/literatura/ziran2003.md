# ziran2003 — Tornillos iliosacros guiados por CT con anestesia local

- **DOI / URL:** impreso en el PDF como "doi.10.1302/0301-620X.85B3.13119" (p. 411)
- **Nivel de lectura:** 2 (metodo) — PROPUESTO por Claude
- **Leido a fondo por la autora:** no
- **PDF:** papers/ziran2003.pdf

Nota: no confundir con `ziran2007fluoroscopic`, que es otro paper.

## Que hace (3 lineas maximo)
Serie clinica prospectiva consecutiva: 66 pacientes con lesion inestable del anillo pelvico posterior y 113 tornillos iliosacros (80 en S1, 31 en S2 y 2 en S3), colocados en la sala de CT con anestesia local y sedacion.
Reporta tiempos, dolor, sedacion, costos y precision. No hubo tornillos mal colocados: todos quedaron extraforaminales y dentro del hueso sacro.
Tambien describe los "tornillos de reduccion" y el acceso a corredores estrechos en sacros dismorficos.

## Restriccion o supuesto clave
No aplica: es un paper clinico, no un paper de sintesis generativa.
Supuesto relevante para el muestreador: la precision se reporta solo de forma binaria
("all screws were shown to be extraforaminal and within sacral bone", p. 416). No hay
escala en mm ni grados de brecha, y el criterio de malposicion no se define: NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 113 tornillos: 80 S1, 31 S2, 2 S3 | "113 screws was introduced into the 66 patients; 80 into S1, 31 into S2" | Results, p. 413 |
| 0 tornillos mal colocados | "There were no technical difficulties, logistical problems, or misplaced screws." | Results, p. 415 |
| Corredores de 10 a 14 mm (observacion, no umbral) | "precise placement of 7.3 mm screws, often through very narrow (10 to 14 mm) corridors" | Discussion, p. 417 |
| Tornillo de 7.3 mm | "a guide-wire for a 7.3 mm self-drilling and tapping cancellous screw" | Operative technique, p. 413 |
| Cortes de CT de 5 mm | "Between three and six images (5 mm slice thickness) were obtained" | Operative technique, p. 413 |

## Donde entra en mi tesis
Objetivo 2 (muestreador): sirve como contexto para la geometria del corredor y para la ausencia de un prior ordinal en S2.
- Anchura del corredor: el PDF menciona corredores "10 to 14 mm" en pacientes con dismorfismo sacro y un tornillo de 7.3 mm. Es una observacion, no un umbral de viabilidad. No hay medicion sistematica: NO ENCONTRADO EN EL PDF.
- S2: hay 31 tornillos en S2, pero la precision se reporta solo de forma binaria y agregada (0 malposiciones). No sirve como distribucion ordinal de brecha en S2. Esto respalda que S2 se evalue solo de forma descriptiva.

## Dudas para el asesor
- `gardner2010safezones` atribuye el umbral de 10 mm a Ziran 2003. En el PDF solo aparece "(10 to 14 mm) corridors", como descripcion de casos dismorficos, sin que se proponga un umbral. Conviene citarlo como umbral?
- Ninguna definicion de "misplaced" aparece en el PDF. Sirve el "0/113" como evidencia de algo en la tesis?

## Evidencia textual
| Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Volumen/numero/fecha | "VOL. 85-B, No. 3, APRIL 2003" | pie, p. 411 |
| Cita impresa | "J Bone Joint Surg [Br] 2003; 85-B:411-8." | Abstract, p. 411 |
| Recepcion/aceptacion | "Received 4 January 2002; Accepted after revision 31 July 2002" | p. 411 |
| Copyright | "©2003 British Editorial Society of Bone and Joint Surgery" | p. 411 |
| DOI | "doi.10.1302/0301-620X.85B3.13119" | p. 411 |
| 66 pacientes | "A total of 66 patients with unstable pelvic ring injuries was stabilised" | Abstract, p. 411 |
| 26 min por tornillo | "The mean length of time for the procedure was 26 minutes per screw." | Abstract, p. 411 |
| Costo | "approximately £1840 ($2800) per operation" | Abstract, p. 411 |
| Periodo | "Between July 1996 and July 1999, 550 patients with pelvic fractures" | Patients and Methods, p. 411 |
| 330 / 220 | "330 non-operatively and 220 with stabilisation" | Patients and Methods, p. 411 |
| Tabla I Young-Burgess | APC2 11, APC3 17, LC2 14, LC3 6, VS 18 | Table I, p. 411 |
| Tabla I AO | C1 60, C3 6 | Table I, p. 411 |
| Sexo | "There were 38 men and 28 women" | p. 412 |
| Edad | "mean age of 42 years (12 to 78)" | p. 412 |
| Seguimiento | "The mean follow-up was 25 months (18 to 42)." | p. 412 |
| Mecanismo | "motor-vehicle or motor-cycle accident in 55, a fall in ten" | p. 412 |
| Otras lesiones | "There were other injuries in 43% of the patients." | p. 412 |
| Bilaterales | "there were six bilateral injuries" | p. 412 |
| Indicacion | "unstable pelvic ring injuries (AO types B and C)" | p. 412 |
| Criterio de exclusion | "Exclusion criteria included those who were haemodynamically unstable" | p. 412 |
| Variables registradas | "and the accuracy of placement of the screws" | p. 413 |
| Escala de dolor | "using a subjective pain scale (range 0 to 10)" | p. 413 |
| Dosis de radiacion registrada | "the total radiation dosage" (registrada; el valor no se reporta: NO ENCONTRADO EN EL PDF) | p. 413 |
| Protocolo de CT intraoperatoria | "Between three and six images (5 mm slice thickness) were obtained" | p. 413 |
| Nivel objetivo | "usually in the pedicle of S1 or S2" | p. 413 |
| Fentanilo/Versed | "fentanyl (50 µg increments) and Versed (0.5 mg increments)" | p. 413 |
| Anestesico local | "mixture of 0.5% bupivicaine and 1% lidocaine" | p. 413 |
| Longitud del tornillo | "established using the measuring software provided with the scanner" | p. 413 |
| Calibre | "a guide-wire for a 7.3 mm self-drilling and tapping cancellous screw" | p. 413 |
| Control final | "the final reduction was checked on CT and radiographs" | p. 413 |
| Tornillos por nivel | "80 into S1, 31 into S2 and two into S3" | Results, p. 413 |
| Tiempo | "26 minutes per screw (18 to 45)" | Results, p. 413 |
| Dolor | "The mean level of pain was five out of ten (0 to 9)." | Results, p. 413 |
| Sedacion | "142 µg (0 to 450) of fentanyl and 3.0 mg (0 to 5.0)" | Results, p. 413 |
| Anestesia local | "19 ml (8 to 40) of lidocaine and 11 ml (5 to 16)" | Results, p. 413 |
| Fijacion anterior previa | "In 13 cases of anterior symphyseal plating and in three fractures" | Results, p. 413 |
| Reduccion cerrada | "In another fxive (three with external fixation and two with plating)" | Results, p. 413-415 |
| Dolor en las reducciones | "mean maximum pain score of 6.25 out of 10" | Results, p. 415 |
| Malposicion | "no technical difficulties, logistical problems, or misplaced screws" | Results, p. 415 |
| Anestesia con mascara | "One patient required mask anaesthesia to complete the procedure." | Results, p. 415 |
| Infeccion/no union | "There were no cases of infection or nonunion." | Results, p. 415 |
| Tornillo roto | "healed fracture with a displacement of 5 mm and a broken screw" | Results, p. 415 |
| Costo en quirofano | "ranged from £4934 to £7895 ($7500 to $12 000)" | Results, p. 415 |
| Routt (citado) | "reported 177 patients and found imaging problems in 10%" | Discussion, p. 415 |
| Routt (citado) | "They also described five examples of malpositioned screws." | Discussion, p. 415 |
| Keating (citado, ref 18) | "an incidence of 13% of malpositioned screws, although with no sequelae" | Discussion, p. 415 |
| Templeman (citado, ref 20) | "malposition of the screw by as little as 4˚ could cause damage" | Discussion, p. 415 |
| Cuello de botella (citado, ref 9) | "bottleneck of this safe corridor of bone is the posterior-medial-cephalad area" | Discussion, p. 415 |
| Bordes no visibles (ref 22) | "the cephalad, caudal, and posterior borders were difficult to visualise" | Discussion, p. 415 |
| Redireccion (citado, refs 23-24) | "redirection was required in about 8% of operations" | Discussion, p. 416 |
| Criterio de precision (binario) | "all screws were shown to be extraforaminal and within sacral bone" | Discussion, p. 416 |
| Reducciones cerradas | "began to undertake closed reductions and were successful in six patients" | Discussion, p. 416 |
| Segundo tornillo, S2 | "both an S1 screw and a second screw, usually in S2, were placed" | Discussion, p. 416 |
| Anchura del corredor | "often through very narrow (10 to 14 mm) corridors" | Discussion, p. 417 |
| Precision de CAOS | "The accuracy of such products to within 1 to 2 mm" | Discussion, p. 417 |
| Umbral de corredor de 10 mm / 1 cm como criterio | NO ENCONTRADO EN EL PDF | — |
| Definicion de malposicion o escala de brecha (mm/grados) | NO ENCONTRADO EN EL PDF | — |
| Resultados de precision separados por S1 y S2 | NO ENCONTRADO EN EL PDF | — |
| Protocolo o grosor de corte de la CT postoperatoria | NO ENCONTRADO EN EL PDF | — |

## Candidatos de snowballing
| Cita tal como aparece | N. ref | Por que |
|---|---|---|
| Carlson DA, Scheid DK, Maar DC, Baele JR, Kaehr DM. Safe placement of S1 and S2 iliosacral screws: the "Vestibule" concept. J Orthop Trauma 2000;14:264-9. | 8 | Geometria del corredor en S1 y S2 |
| Day CS, Prayson MJ, Shuler TE, Towers J, Gruen GS. Trans-sacral versus modified pelvic landmarks for percutaneous iliosacral screw placement... Am J Orthop 2000;29(Suppl):16-21. | 9 | Cuello de botella del corredor medido en CT |
| Ebraheim NA, Xu R, Biyani A, Nadaud MC. Morphologic considerations of the first sacral pedicle for iliosacral screw placement. Spine 1997;22:841-6. | 10 | Geometria del pediculo de S1 |
| Goldberg BA, Lindsey RW, Foglar C, et al. Imaging assessment of sacroiliac screw placement relative to the neuroforamen. Spine 1998;23:585-9. | 11 | Evaluacion por imagen de la brecha foraminal |
| Noojin FK, Malkani AL, Haikal L, Lundquist C, Voor MJ. Cross-sectional geometry of the sacral ala... J Orthop Trauma 2000;14:31-5. | 12 | Geometria del corredor (ya existe docs/literatura/noojin2000cross.md) |
| Keating JF, Werier J, Blachut P, et al. Early fixation of the vertically unstable pelvis... J Orthop Trauma 1999;13:107-13. | 18 | Tasa de malposicion de 13% (posible distribucion) |
| Ziran BH, Wason AG, Olsen S, Chapman MW. Radiographic anatomy of the iliosacral corridor. Procs Orthopaedic Trauma Association, 1996:192. | 22 | Geometria del corredor; posible origen del umbral de 10 mm (resumen de congreso) |
| Amongero ME, Wilber JH. Upper sacral morphology and its relation to sacroiliac screw fixation. Orthop Trans 1995;19:435. | 6 | Morfologia de S1 y S2 para el corredor |
