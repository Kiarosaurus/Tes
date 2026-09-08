# moed2006s2screw — Tornillo iliosacro en S2, serie de 49 casos

- **DOI / URL:** 10.1097/00005131-200607000-00002 (tomado de `refs/raw/moed2006s2screw.nbib`;
  **el DOI NO aparece impreso en el PDF**). PMID 16825961. J Orthop Trauma 2006;20(6):378-383.
- **Nivel de lectura:** 1 (profunda) — **propuesto**, ver justificacion abajo. Alternativa defendible: 2
- **Leido a fondo por la autora:** no
- **PDF:** papers/moed2006s2screw.pdf (6 paginas de PDF, numeradas 378 a 383)
- **Profundidad:** PDF completo (texto, figuras y lista de referencias)

## Que hace (3 lineas maximo)

Serie clinica retrospectiva de un solo centro de trauma nivel 1: 49 pacientes y 53 tornillos
iliosacros colocados en el cuerpo de S2 entre 1996 y 2001, cuando S1 no admitia dos puntos de
fijacion. Evalua seguridad (lesion nerviosa iatrogenica intraoperatoria) y eficacia (posicion
del tornillo en TC postoperatoria y mantenimiento de la reduccion). No mide geometria del
corredor: mide desenlaces clinicos.

## Restriccion o supuesto clave

No es un paper de sintesis generativa. El supuesto que importa a esta tesis es otro y es
doble:

1. **El "1 cm" de este paper NO es un diametro de corredor.** Es una distancia entre los
   forametros neurales S1 y S2 medida sobre cortes axiales de TC de 3 mm, y se exige en
   *3 cortes consecutivos*: *"a minimum of 1 cm between the S1 and S2 neural foramina on
   3 sequential preoperative CT 3-mm sections"* (Patients and Methods, p. 379). Kaiser
   atribuye a este paper (su ref. 4) un *"10-mm-diameter corridor"* perpendicular al eje de
   la zona segura. **No son la misma magnitud geometrica.** Aqui es una separacion
   interforaminal en 2D; en Kaiser es un diametro de corredor 3D.
2. **El criterio no se cita: se declara.** El paper enuncia el 1 cm como definicion propia
   de candidatura quirurgica, sin llamada de referencia. **Una fuente o justificacion
   anatomica del valor 1 cm: NO ENCONTRADO EN EL PDF.**

Consecuencia: este paper es, hasta donde alcanza la lectura, un **nodo terminal** de la
cadena del "10 mm" (no reenvia a nadie), pero **para una magnitud distinta** de la que
Kaiser y McLaren usan.

## Que toco de aqui

- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Hallazgos prioritarios del encargo

### 1. Umbral de 10 mm: SI APARECE, pero como 1 cm y con otra definicion

- **Aparece, dos veces, con redaccion casi identica.** Abstract: *"a minimum of 1 cm between
  foramina on 3 sequential preoperative CT slices"* (Patients, p. 378). Metodos:
  *"a minimum of 1 cm between the S1 and S2 neural foramina on 3 sequential preoperative
  CT 3-mm sections"* (p. 379).
- **Lo miden aqui, no lo citan.** Es un criterio de seleccion de pacientes aplicado
  prospectivamente por el protocolo del centro, medido sobre la TC preoperatoria de cada
  paciente. No hay llamada a ninguna referencia en ninguna de las dos apariciones.
- **Pero no es un diametro de corredor** (ver "Restriccion o supuesto clave"). No hay
  ninguna frase que hable de diametro, area, seccion transversal ni eje del corredor.
- Va siempre acompanado de una segunda condicion: *"in conjunction with inadequate available
  space in S1"* (Abstract, p. 378). El 1 cm por si solo no habilita el S2.

### 2. Tasa de malposicion medida en estos 49 casos: NO HAY MALPOSICION REPORTADA, Y NO HAY PORCENTAJE

- **Conteo crudo: 0 tornillos mal colocados de 53.** *"satisfactory screw position in the
  body of S2 was documented on the postoperative plain radiographs and CT scan in all cases"*
  (Results, p. 380). Confirmado en Discusion: *"all the 53 screws in this series were
  inserted without causing injury to the S1 or S2 nerve roots"* (p. 382).
- **El paper NO escribe ninguna tasa ni porcentaje de malposicion. NO ENCONTRADO EN EL PDF.**
  No se deriva aqui: 0/53 se reporta como conteo, no como tasa.
- **Modalidad de evaluacion:** radiografia simple AP, inlet y outlet, **mas TC 2D de 3 mm**
  postoperatoria (Methods, p. 379-380). Es decir, si hubo TC postoperatoria.
- **Quien evaluo la posicion, si hubo lectura independiente, cegada o por mas de un
  observador: NO ENCONTRADO EN EL PDF.** Tampoco hay kappa ni acuerdo entre observadores.
- **Caveat que la tesis no puede omitir:** el unico compromiso foraminal de la serie **no fue
  un error de insercion**, sino consecuencia de una perdida de reduccion postoperatoria:
  *"acute loss of reduction after injudicious full–weight bearing on the third postoperative
  day was associated with compromise of the S1 neural foramina by the S2 iliosacral screw"*
  (Results, p. 380). El tornillo migro con el hueso; no estaba mal puesto.

### 3. Criterio de colocacion incorrecta: BINARIO, y sin definicion operacional

- El unico calificativo aplicado a la posicion del tornillo es **"satisfactory"**
  (Results, p. 380). No hay grados, no hay milimetros de brecha, no hay categorias.
- **Que cuenta como "satisfactory screw position": NO ENCONTRADO EN EL PDF.** No se define
  umbral de perforacion cortical ni distancia minima al foramen.
- **Cuidado con la unica escala graduada del paper: NO es de posicion del tornillo, es de
  reduccion de la fractura.** *"excellent (4 mm of displacement), good (5 to 10 mm of
  displacement), fair (11 to 20 mm of displacement), and poor (>20 mm of displacement)"*
  (Methods, p. 380), tomada de su ref. 2 (Matta y Tornetta 1996) y medida como
  desplazamiento maximo en las tres proyecciones radiograficas. **Mezclar esta escala con la
  escala ordinal 0-3 de `smith2006iliosacral` seria un error de familia de criterios:** una
  mide desplazamiento del foco de fractura, la otra brecha cortical del tornillo.
  (Nota de transcripcion: el primer grado se imprime *"excellent (4 mm of displacement)"*,
  sin simbolo de desigualdad; si el original decia "<=4 mm" el PDF no lo conserva. No se
  corrige aqui.)

### 4. Poblacion

49 pacientes, 53 tornillos S2, 9 lesiones bilaterales; 29 hombres y 20 mujeres; 14 a 71 anos
(media 32); seguimiento medio 19 meses (rango 6 meses a 6 anos). Seleccionados dentro de 169
pacientes tratados por lesion pelvica posterior inestable en el periodo. Lesion posterior por
hemipelvis: 30 luxacion sacroiliaca, 9 fractura-luxacion sacroiliaca, 14 fractura sacra (6
Zona I, 8 Zona II). Clasificacion: 52 Tipo C (OTA 61-C) y 1 Tipo B (OTA 61-B). 32 tornillos
percutaneos tras reduccion cerrada, 21 en procedimiento abierto. 11 de 49 pacientes (12 de 53
hemipelvis) con dismorfismo sacro; 3 casos adicionales con S1 transicional parcialmente
lumbarizado. **Cuantos tornillos S1 se colocaron en total: NO ENCONTRADO EN EL PDF**, aunque
se declara que el S2 se coloco *"almost uniformly ... in combination with an S1 iliosacral
screw"* (Methods, p. 379).

### 5. Geometria del corredor S2

Lo unico geometrico del paper es el criterio de 1 cm interforaminal y el calibre del implante:
*"a 7.0-mm cannulated screw using a 3.2-mm drill bit as a guide wire"* (Methods, p. 379), y en
Discusion *"the S2 body can safely accept a 6.5-mm or larger cancellous screw"* (p. 382). Cita
ademas, de terceros, la recomendacion de no pasar de 4.5 mm en S2 (Gautier, su ref. 11).
**Diametro del corredor, area transversal, longitud, margenes al foramen o a la cortical,
angulos de trayectoria, punto de entrada y longitud del tornillo: NO ENCONTRADO EN EL PDF**
(8 entradas). El grosor de corte de TC (3 mm) es el unico parametro de adquisicion publicado;
**kVp, mAs, kernel y resolucion en plano: NO ENCONTRADO EN EL PDF.**

### 6. Por que S2 en vez de S1, y comparacion entre niveles

- **Indicacion:** *"Patients with space inadequate for at least 2 points of iliosacral screw
  fixation into the S1 body"* (Methods, p. 379). El motivador es el dismorfismo sacro y el
  limite de tamano de S1 (Introduccion, p. 378).
- **Cifras comparativas S1 vs S2 medidas EN ESTE PAPER: NO ENCONTRADO EN EL PDF.** No hay
  ninguna comparacion estadistica interna entre niveles.
- **Todas las cifras comparativas son citas de terceros**, en Discusion, p. 382:
  van den Bosch (su ref. 12) con 6/31 frente a 1/49 de lesion neurologica segun donde fuera
  el segundo tornillo; Hinsche (su ref. 10) con la concentracion de tornillos mal colocados
  en S2; Carlson (su ref. 13) con *"much less margin for error when inserting an S2, as
  opposed to an S1, iliosacral screw"*; Ziran (su ref. 22) con 31 tornillos en S2 sin evento
  adverso; Griffin (su ref. 23) con 4 fallos de fijacion de 62 pacientes.
- **Dato de direccion contraria, util para el muestreador:** segun Carlson, citado aqui, el
  espacio disponible en S2 *"increased in patients with sacral dysmorphism"* (p. 382). Es
  decir, el nivel condiciona en sentido opuesto al de S1.

### 7. Complicaciones neurologicas o vasculares

- **Cero lesiones nerviosas iatrogenicas intraoperatorias:** *"There were no iatrogenic
  intraoperative neurological injuries that were attributable to iliosacral screw insertion"*
  (Results, p. 380).
- **2 de 49 pacientes** con perdida precoz de fijacion y de reduccion que exigio cirugia de
  revision, ambos con osteopenia sospechada. **1 de esos 2** con lesion de la raiz S1, con
  recuperacion completa dentro del ano.
- **Subgrupo osteopenico:** 5 pacientes identificados como potencialmente osteopenicos (4 de
  55 anos o mas y 1 mujer posmenopausica de 53); fallo en 2 de esos 5 y en ninguno de los 44
  restantes; *"P = 0.008, Fisher exact test"*, riesgo relativo 15.67 (IC 95% 5.24-46.83).
- **Complicaciones vasculares: NO ENCONTRADO EN EL PDF.** Tampoco infeccion, sangrado,
  mortalidad ni tasa de reintervencion expresada como porcentaje (4 entradas).
- **Monitorizacion intraoperatoria (SE-EMG):** corriente de busqueda de 50 mA; umbral de
  seguridad *">8 mA"* para la broca y *">6 mA"* para el tornillo final; estimulos monofasicos
  de 0.2 ms a 3 Hz (Methods, p. 379). Umbrales medidos en los tornillos S2: *"ranged from 8
  to 55 mA (mean 30 mA)"* (p. 381). El sistema fallo en 1 caso por electrodo defectuoso.

### 8. Limitaciones declaradas

**No hay seccion de limitaciones. NO ENCONTRADO EN EL PDF.** Lo mas cercano son tres frases
dispersas: el diseno se declara *"Retrospective analysis of a treatment protocol in a
consecutive patient series"* (Design, p. 378); sobre el hallazgo de la osteopenia,
*"This finding is based on limited data and merits further study"* (Discusion, p. 382); y la
admision de que otros factores pudieron causar los fallos, *"the percutaneous technique, or
some factors other than placing a screw in the S2 body may have contributed"* (p. 382).
**Tamano muestral justificado a priori, poder estadistico, perdidas de seguimiento y
declaracion de sesgo de seleccion: NO ENCONTRADO EN EL PDF** (4 entradas).

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 1 cm entre forametros, 3 cortes consecutivos de 3 mm | *"a minimum of 1 cm between the S1 and S2 neural foramina"* | Patients and Methods, p. 379 |
| 49 pacientes, 53 tornillos S2 | *"9 bilateral injuries with a total of 53 S2 screws inserted"* | Abstract (Patients), p. 378 |
| 0 lesiones nerviosas intraoperatorias | *"There were no intraoperative iatrogenic nerve injuries"* | Abstract (Results), p. 378 |
| Posicion satisfactoria en todos los casos | *"Satisfactory screw position was documented on postoperative CT in all cases"* | Abstract (Results), p. 378 |
| 2 revisiones por perdida de reduccion | *"loss of reduction requiring revision surgery occurred in 2 patients with osteopenia"* | Abstract (Results), p. 378 |
| Tornillo 7.0 mm, broca 3.2 mm | *"a 7.0-mm cannulated screw using a 3.2-mm drill bit"* | Methods, p. 379 |
| S2 admite tornillo de 6.5 mm o mayor | *"the S2 body can safely accept a 6.5-mm or larger cancellous screw"* | Discusion, p. 382 |
| P = 0.008; RR 15.67 (IC 95% 5.24-46.83) | *"P = 0.008, Fisher exact test), with a relative risk of 15.67"* | Results, p. 380 |
| Escala de REDUCCION (no de tornillo): 4 / 5-10 / 11-20 / >20 mm | *"excellent (4 mm of displacement), good (5 to 10 mm of displacement)"* | Methods, p. 380 |

## Donde entra en mi tesis

- **Cadena del umbral de 10 mm (implicancias #7 y #25).** Es la tercera de las tres fuentes a
  las que `kaiser2014dysmorphism` atribuye el umbral, y la primera de las tres que se lee. El
  resultado **no cierra la cadena y ademas la complica**: el numero 1 cm si esta aqui y no se
  cita a nadie, pero designa una separacion interforaminal en 2D, no un diametro de corredor.
  Si la tesis cita a Moed como origen del "corredor de 10 mm", esta citando mal.
- **Prior clinico de malposicion (implicancia #12).** **No lo resuelve.** El paper no publica
  tasa de malposicion, publica 0/53 con criterio binario y sin definicion operacional. Como
  prior de una distribucion de malposiciones es inservible: una serie con cero eventos, muestra
  auto-seleccionada por un criterio anatomico estricto, y evaluada por el propio equipo tratante.
- **Condicionamiento del muestreador por nivel sacro (S1 vs S2).** Aporta el criterio de
  *indicacion* del nivel (S2 solo cuando S1 no admite dos puntos, o hay dismorfismo) y el
  calibre tipico del implante en S2. No aporta geometria del corredor.
- **Objetivo 3 / banco de geometrias.** Diametros citables para el banco: 7.0 mm colocado,
  6.5 mm como minimo declarado seguro, 4.5 mm como recomendacion mas conservadora de terceros.

## Dudas para el asesor

1. Si el "1 cm" de Moed es separacion interforaminal en cortes axiales y el "10 mm" de Kaiser
   y McLaren es diametro de corredor perpendicular al eje, **el umbral de la tesis debe
   declararse con una sola de las dos definiciones**. Cual se adopta? Mezclarlas hace el
   criterio del muestreador no auditable.
2. Con Moed leido, la cadena del 10 mm queda con dos fuentes vivas (Gardner 2010, Ziran 2007).
   Vale la pena leer las dos antes de fijar la restriccion dura del Objetivo 2, o se declara en
   la tesis que el umbral es una convencion heredada sin medicion primaria?
3. Una serie con 0 eventos de malposicion **no puede** ser prior. Se acepta cerrar la
   implicancia #12 declarando que la tesis no usara un prior clinico numerico, y que el
   muestreador se justifica por variabilidad anatomica y no por una tasa publicada?
4. `_candidatos.md` registra este paper como *"J Orthop Trauma. 2006 Aug;20(6):378-83"*; el PDF
   y `refs/raw/` dicen **July 2006**. Se corrige la fila de candidatos?

## Evidencia textual

Toda cifra, umbral, definicion de escala o criterio de evaluacion del PDF. Paginas segun la
numeracion impresa de la revista (378-383).

| Item | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Criterio de candidatura, 1 cm (abstract) | *"a minimum of 1 cm between foramina on 3 sequential preoperative CT slices"* | Abstract, Patients, p. 378 |
| Criterio de candidatura, 1 cm (metodos) | *"a minimum of 1 cm between the S1 and S2 neural foramina"* | Patients and Methods, p. 379 |
| Condicion acompanante del criterio | *"in conjunction with inadequate available space in S1"* | Abstract, Patients, p. 378 |
| Numero de cortes exigidos | *"on 3 sequential preoperative CT 3-mm sections"* | Patients and Methods, p. 379 |
| Indicacion del nivel S2 | *"space inadequate for at least 2 points of iliosacral screw fixation into the S1 body"* | Patients and Methods, p. 379 |
| Diseno del estudio | *"Retrospective analysis of a treatment protocol in a consecutive patient series"* | Abstract, Design, p. 378 |
| Entorno | *"Level 1 trauma center"* | Abstract, Setting, p. 378 |
| Periodo de reclutamiento | *"Between January 1, 1996, and July 31, 2001"* | Patients and Methods, p. 379 |
| Poblacion base del periodo | *"169 patients with structurally unstable pelvic injuries involving the posterior ring were treated"* | Patients and Methods, p. 379 |
| N de pacientes y tornillos | *"9 bilateral injuries with a total of 53 S2 screws inserted"* | Abstract, Patients, p. 378 |
| Sexo | *"There were 29 males and 20 females"* | Patients and Methods, p. 379 |
| Edad | *"ranging in age from 14 to 71 years (mean 32 years)"* | Patients and Methods, p. 379 |
| Seguimiento | *"Follow-up averaged 19 months (range 6 months to 6 years)"* | Abstract, Patients, p. 378 |
| Estado neurologico preoperatorio | *"Forty-four patients demonstrated intact function of the ipsilateral lumbosacral plexus"* | Patients and Methods, p. 379 |
| Deficit preoperatorio | *"In 5 patients, a varying degree of neurological dysfunction involving the L4/L5 distribution"* | Patients and Methods, p. 379 |
| Tipo de lesion posterior | *"a sacroiliac dislocation in 30, a sacroiliac fracture/dislocation in 9, and a sacral fracture in 14"* | Patients and Methods, p. 379 |
| Zonas de fractura sacra | *"(Zone I in 6 and Zone II in 8)"* | Patients and Methods, p. 379 |
| Clasificacion OTA | *"Type C (OTA 61-C) in 52 and Type B (OTA 61-B) in 1"* | Patients and Methods, p. 379 |
| Mecanismo | *"motor vehicle crash in 30, a pedestrian struck by a motor vehicle in 8"* | Patients and Methods, p. 379 |
| Fracturas abiertas | *"4 of the pelvic injuries were open"* | Patients and Methods, p. 379 |
| Via de insercion | *"32 were inserted percutaneously after closed manipulation ... and 21 ... open procedure"* | Patients and Methods, p. 379 |
| Prevalencia de dismorfismo en la serie | *"Eleven of the 49 patients (12 of the 53 hemipelves) had sacral dysmorphism"* | Patients and Methods, p. 379 |
| Criterio cualitativo de dismorfismo | *"as evidenced by mamillary processes and a residual disk space between the S1 and S2 bodies"* | Patients and Methods, p. 379 |
| Vertebra transicional | *"In 3 additional cases, S1 was a transitional vertebra, being partially lumbarized"* | Patients and Methods, p. 379 |
| Grosor de corte de TC | *"two-dimensional computerized tomography (CT) with 3-mm slice thickness"* | Abstract, Patients, p. 378 |
| Proyecciones radiograficas | *"anteroposterior, inlet and outlet pelvic x-rays"* | Abstract, Patients, p. 378 |
| Vista fluoroscopica adicional | *"supplemented by a lateral sacral view, visualizing the S1/S2 segmentation line"* | Patients and Methods, p. 379 |
| Blanco de la vista lateral | *"The lateral fluoroscopic view was used to target the center of the S2 body"* | Patients and Methods, p. 379 |
| Funcion de la vista inlet | *"path of the drill bit or screw is maintained within the confines of the sacral ala"* | Patients and Methods, p. 379 |
| Funcion de la vista outlet | *"the outlet view is used to target a path between the S1 and S2 foramina"* | Patients and Methods, p. 379 |
| Implante usado | *"a 7.0-mm cannulated screw using a 3.2-mm drill bit as a guide wire"* | Patients and Methods, p. 379 |
| Construccion de fijacion | *"almost uniformly placed in combination with an S1 iliosacral screw"* | Patients and Methods, p. 379 |
| Fijacion posterior alternativa | *"a transiliac bar was used in 6 cases and a transiliac plate in 1 case"* | Patients and Methods, p. 379 |
| Fijacion anterior | *"an external fixator in 28 patients and a plate in 17 patients"* | Patients and Methods, p. 379 |
| Sin fijacion anterior | *"In 4 patients, no anterior fixation was applied"* | Patients and Methods, p. 379 |
| Parametros del estimulo SE-EMG | *"Monopolar monophasic square-wave stimuli of 0.2-millisecond duration were delivered at 3 Hz"* | Patients and Methods, p. 379 |
| Corriente de busqueda | *"A searching current of 50 mA was initially applied to the drill bit"* | Patients and Methods, p. 379 |
| Umbral de zona segura de la broca | *"A current threshold of >8 mA was selected as the safe zone"* | Patients and Methods, p. 379 |
| Umbral del tornillo final | *"corresponds to a final screw current threshold of >6 mA"* | Patients and Methods, p. 379 |
| Bloqueo neuromuscular | *"a response of 3 or 4 twitches to the train of 4 stimuli"* | Patients and Methods, p. 379 |
| Umbrales medidos en los tornillos S2 | *"Current thresholds for the S2 screws ranged from 8 to 55 mA (mean 30 mA)"* | Resultados, p. 381 |
| Fallo tecnico del monitoreo | *"successful in all cases except one, in which the replacement for a defective electrode lead"* | Resultados, p. 381 |
| Escala de REDUCCION, grado excelente | *"excellent (4 mm of displacement)"* | Patients and Methods, p. 380 |
| Escala de REDUCCION, grado bueno | *"good (5 to 10 mm of displacement)"* | Patients and Methods, p. 380 |
| Escala de REDUCCION, grado regular | *"fair (11 to 20 mm of displacement)"* | Patients and Methods, p. 380 |
| Escala de REDUCCION, grado malo | *"poor (>20 mm of displacement)"* | Patients and Methods, p. 380 |
| Como se mide esa escala | *"graded using the maximal displacement measured on the 3 standard radiographic views"* | Patients and Methods, p. 380 |
| Descarga postoperatoria | *"non–weight-bearing status on the affected side for 12 weeks postoperatively"* | Patients and Methods, p. 380 |
| Resultado neurologico intraoperatorio | *"There were no iatrogenic intraoperative neurological injuries that were attributable to iliosacral screw insertion"* | Resultados, p. 380 |
| Posicion del tornillo (criterio binario) | *"satisfactory screw position in the body of S2 was documented ... in all cases"* | Resultados, p. 380 |
| Modalidad de verificacion postoperatoria | *"documented on the postoperative plain radiographs and CT scan"* | Resultados, p. 380 |
| Calidad de reduccion obtenida | *"graded as excellent or good in 51 and fair in 2"* | Resultados, p. 380 |
| Mantenimiento de la reduccion | *"maintained throughout the follow-up period in 47 of the 49 patients"* | Resultados, p. 380 |
| Fallos de fijacion | *"loss of screw fixation and fracture reduction requiring revision surgery occurred in 2 older patients"* | Resultados, p. 380 |
| Subgrupo osteopenico | *"5 patients were identified as being potentially osteopenic"* | Resultados, p. 380 |
| Definicion operacional de osteopenia sospechada | *"(4 aged 55 or older and 1 postmenopausal woman aged 53 years)"* | Resultados, p. 380 |
| Distribucion del fallo | *"Fixation failure occurred in 2 of these 5 patients and in none of the remaining 44"* | Resultados, p. 380 |
| Significacion estadistica | *"P = 0.008, Fisher exact test"* | Resultados, p. 380 |
| Riesgo relativo | *"a relative risk of 15.67 (95% confidence interval 5.24–46.83)"* | Resultados, p. 380 |
| Caso 1: causa del fallo | *"S2 screw purchase was thought to be adequate but not ideal"* | Resultados, p. 380 |
| Caso 2: mecanismo del dano nervioso | *"acute loss of reduction after injudicious full–weight bearing on the third postoperative day"* | Resultados, p. 380 |
| Caso 2: lesion resultante | *"compromise of the S1 neural foramina by the S2 iliosacral screw and injury to the S1 nerve root"* | Resultados, p. 380 |
| Caso 2: recuperacion | *"Full return of function was noted by the patient within 1 year"* | Resultados, p. 380 |
| Cero lesiones radiculares atribuibles a insercion | *"all the 53 screws in this series were inserted without causing injury to the S1 or S2 nerve roots"* | Discusion, p. 382 |
| Calibre declarado seguro para S2 | *"the S2 body can safely accept a 6.5-mm or larger cancellous screw"* | Discusion, p. 382 |
| Reclamo de tamano de serie | *"this series represents the largest clinical series specifically evaluating the insertion of the S2 iliosacral screw"* | Discusion, p. 382 |
| Zona segura S2, afirmacion cualitativa | *"the S2 body offers a smaller target, or 'safe zone,' for iliosacral screw insertion"* | Discusion, p. 382 |
| Motivo historico del rechazo de S2 | *"almost universally avoided because of a perceived increased risk for nerve root injury"* | Discusion, p. 382 |
| Justificacion de 2 puntos de fijacion | *"Biomechanical studies suggest improved stability using 2 points of posterior fixation"* | Discusion, p. 381 |
| Limitacion declarada sobre la osteopenia | *"This finding is based on limited data and merits further study"* | Discusion, p. 382 |
| Confusion de causa admitida | *"some factors other than placing a screw in the S2 body may have contributed"* | Discusion, p. 382 |
| Recomendacion de precaucion | *"should be used with caution in patients with suspected pelvic osteopenia"* | Conclusiones, p. 382 |
| Recomendacion de retiro | *"any screw with questionable intraoperative purchase should be removed"* | Discusion, p. 382 |
| CITA de terceros: S2 vs S1 en van den Bosch | *"second screw of a 2-screw construct was inserted in S2 (6/31) sustained neurological injury"* | Discusion, p. 382 |
| CITA de terceros: brazo comparador de van den Bosch | *"as compared to those with both screws in S1 (1/49)"* | Discusion, p. 382 |
| CITA de terceros: Hinsche | *"most of the misplaced screws, no matter which method was used, occurred at the S2 level"* | Discusion, p. 382 |
| CITA de terceros: limite de la vista outlet | *"the routine outlet radiographic view did not show the S2 pedicle well enough"* | Discusion, p. 382 |
| CITA de terceros: Gautier, calibre maximo | *"recommended screws no larger than 4.5 mm but only when deemed necessary"* | Discusion, p. 382 |
| CITA de terceros: Carlson, margen de error | *"much less margin for error when inserting an S2, as opposed to an S1, iliosacral screw"* | Discusion, p. 382 |
| CITA de terceros: Carlson, efecto del dismorfismo | *"this available space increased in patients with sacral dysmorphism"* | Discusion, p. 382 |
| CITA de terceros: Routt, 5 pacientes dismorficos | *"5 patients with sacral dysmorphism limiting the S1 space available"* | Discusion, p. 382 |
| CITA de terceros: Ziran | *"Ziran et al inserted 31 screws into S2 without an adverse event"* | Discusion, p. 382 |
| CITA de terceros: Griffin, distribucion | *"56 with 1 screw in S1 and another in S2"* | Discusion, p. 382 |
| CITA de terceros: Griffin, fallos | *"Fixation failure occurred in 4 of the 62 patients"* | Discusion, p. 382 |
| Numero de volumen y paginas | *"J Orthop Trauma 2006;20:378–383"* | Encabezado del abstract, p. 378 |
| **DOI impreso en el PDF** | — | **NO ENCONTRADO EN EL PDF** |
| **Fuente o justificacion del valor 1 cm** | — | **NO ENCONTRADO EN EL PDF** (se enuncia sin llamada de referencia) |
| **Tasa de malposicion expresada como porcentaje** | — | **NO ENCONTRADO EN EL PDF** (solo 0 de 53 como conteo) |
| **Definicion operacional de "satisfactory screw position"** | — | **NO ENCONTRADO EN EL PDF** |
| **Escala graduada de posicion del tornillo con umbrales en mm** | — | **NO ENCONTRADO EN EL PDF** (la escala en mm es de reduccion, no de tornillo) |
| **Numero de tornillos con brecha cortical** | — | **NO ENCONTRADO EN EL PDF** |
| **Quien evaluo la TC postoperatoria; cegamiento; numero de observadores** | — | **NO ENCONTRADO EN EL PDF** |
| **Acuerdo entre observadores o kappa** | — | **NO ENCONTRADO EN EL PDF** |
| **Diametro del corredor S2 en mm** | — | **NO ENCONTRADO EN EL PDF** |
| **Area transversal del corredor S2** | — | **NO ENCONTRADO EN EL PDF** |
| **Longitud del corredor o del tornillo colocado** | — | **NO ENCONTRADO EN EL PDF** |
| **Angulos de trayectoria (coronal, axial o cualquier otro)** | — | **NO ENCONTRADO EN EL PDF** |
| **Punto de entrada o coordenadas en la tabla externa iliaca** | — | **NO ENCONTRADO EN EL PDF** |
| **Margen en mm al foramen o a la cortical alcanzado por el tornillo** | — | **NO ENCONTRADO EN EL PDF** |
| **Tolerancia angular de la trayectoria** | — | **NO ENCONTRADO EN EL PDF** |
| **Comparacion estadistica S1 vs S2 hecha en esta serie** | — | **NO ENCONTRADO EN EL PDF** (todas las comparaciones son citas) |
| **Numero total de tornillos S1 colocados en la serie** | — | **NO ENCONTRADO EN EL PDF** |
| **Dimensiones del corredor S1 medidas aqui** | — | **NO ENCONTRADO EN EL PDF** |
| **Puntaje cuantitativo de dismorfismo sacro** | — | **NO ENCONTRADO EN EL PDF** (criterio solo cualitativo) |
| **Complicaciones vasculares** | — | **NO ENCONTRADO EN EL PDF** |
| **Tasa de infeccion u otras complicaciones no neurologicas** | — | **NO ENCONTRADO EN EL PDF** |
| **Mortalidad** | — | **NO ENCONTRADO EN EL PDF** |
| **Tasa de reintervencion expresada como porcentaje** | — | **NO ENCONTRADO EN EL PDF** (solo 2 de 49) |
| **kVp, mAs, kernel o resolucion en plano de la TC** | — | **NO ENCONTRADO EN EL PDF** (solo grosor de corte de 3 mm) |
| **Fabricante o modelo del tomografo** | — | **NO ENCONTRADO EN EL PDF** |
| **Fabricante del tornillo canulado de 7.0 mm** | — | **NO ENCONTRADO EN EL PDF** |
| **Seccion explicita de limitaciones** | — | **NO ENCONTRADO EN EL PDF** |
| **Calculo de tamano muestral o poder estadistico** | — | **NO ENCONTRADO EN EL PDF** |
| **Perdidas de seguimiento** | — | **NO ENCONTRADO EN EL PDF** |
| **Declaracion de sesgo de seleccion** | — | **NO ENCONTRADO EN EL PDF** |
| **Composicion etnica de la cohorte** | — | **NO ENCONTRADO EN EL PDF** |
| **Tiempo quirurgico o tiempo de radiacion por tornillo** | — | **NO ENCONTRADO EN EL PDF** |
| **Resultado funcional con escala validada** | — | **NO ENCONTRADO EN EL PDF** |

**Total de entradas cerradas como NO ENCONTRADO EN EL PDF en esta tabla: 31.**

### Observaciones de auditoria

- **Discrepancia de mes.** `_candidatos.md` registra *"J Orthop Trauma. 2006 Aug;20(6):378-83"*.
  El PDF imprime *"Volume 20, Number 6, July 2006"* en todas sus paginas, y `refs/raw/` dice
  July. Se conserva July.
- **Discrepancia de ano en una cita interna.** Moed cita a Hinsche como *"Clin Orthop.
  2001;395:135-144"* (su ref. 10), mientras que la ficha `hinsche2002fluoroscopy.md` y
  `refs.bib` lo fechan en 2002. Mismo volumen y paginas. No se resuelve aqui.
- **El paper se llama a si mismo la mayor serie de S2**, pero **no reporta cuantos tornillos S1
  se pusieron**, asi que su propia serie no permite calcular ninguna tasa comparativa por nivel.
- **La cita de Ziran en Discusion (su ref. 22) es Ziran 2002 en J Bone Joint Surg Br**, no el
  Ziran 2007 de J Trauma que `_candidatos.md` registra como una de las tres fuentes del 10 mm.
  Son referencias distintas del mismo primer autor.
