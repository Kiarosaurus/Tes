# kaiser2014dysmorphism — Determinantes anatomicos del dismorfismo sacro

- **DOI / URL:** 10.2106/JBJS.M.00895 (impreso en el pie de la p. e120(1) como
  `http://dx.doi.org/10.2106/JBJS.M.00895`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/kaiser2014dysmorphism.pdf

> Profundidad: PDF completo, 8 paginas (e120(1) a e120(8)). El **Appendix esta fuera
> del PDF**: el propio articulo dice que la tabla de scores por quintil y la figura de
> los tres clusters *"are available with the online version of this article as a data
> supplement at jbjs.org"* (Appendix, p. e120(7)). Todo lo que dependa del Appendix
> queda como NO ENCONTRADO EN EL PDF.

## Que hace (3 lineas maximo)

Mide sobre 104 CT de pelvis no lesionadas el corredor oseo de 10 mm de diametro de S1 y
S2 (area, angulacion coronal y axial, longitud) reformateando el CT segun el eje del sacro.
Deriva por regresion logistica y analisis discriminante un *sacral dysmorphism score* =
(angulo coronal de S1) + 2(angulo axial de S1), y agrupa la cohorte en tres fenotipos.

## Restriccion o supuesto clave

No es un paper de sintesis generativa. La restriccion que importa aqui es otra, y es
**el hallazgo central de esta lectura**: el umbral de 10 mm **no se mide ni se deriva en
este trabajo, se elige y se hereda**. Dos frases lo dicen:

- Metodos: *"A 10-mm-diameter corridor perpendicular to the axis of the safe zone was
  chosen as a conservative size for passage of an iliosacral screw"*, con llamada a las
  refs. **29 y 37** (Quantification of the Osseous Safe Corridor, p. e120(2)).
- Discusion: *"has been previously established as a reasonably 'safe'-diameter corridor
  by experienced surgeons"*, con llamada a las refs. **4, 29 y 37** (p. e120(7)).

Los propios autores lo llaman *"our conservative 10-mm threshold"* (Discusion, p. e120(7)),
es decir, un criterio propio de analisis, no un resultado. La unica justificacion interna
es dimensional y no numerica: *"Ten millimeters was chosen to allow 1 to 2 mm of
circumference around a 6.3 to 8-mm-diameter screw"* (Discusion, p. e120(7)).

**Consecuencia directa para la implicancia #7 y la #25: la cadena de citas NO se corta
aqui.** `mclaren2021corridor` dice *"Kaiser et al. recommended 10 mm or greater"*, pero
Kaiser a su vez lo atribuye a sus refs. 4, 29 y 37, que son:

- ref. 4 — Moed BR, Geer BL. *S2 iliosacral screw fixation for disruptions of the posterior
  pelvic ring: a report of 49 cases.* J Orthop Trauma. 2006 Aug;20(6):378-83.
- ref. 29 — Gardner MJ, Morshed S, Nork SE, Ricci WM, Chip Routt ML Jr. *Quantification of
  the upper and second sacral segment safe zones in normal and dysmorphic sacra.*
  J Orthop Trauma. 2010 Oct;24(10):622-9.
- ref. 37 — Ziran BH, Wasan AD, Marks DM, Olson SA, Chapman MW. *Fluoroscopic imaging guides
  of the posterior pelvis pertaining to iliosacral screw placement.* J Trauma. 2007
  Feb;62(2):347-56; discussion 356.

Segundo supuesto, tambien relevante: la cohorte es de **pelvis NO lesionadas**
(*"We studied a large cohort of uninjured pelves to represent the variance in morphology
within the general population"*, Discusion, p. e120(6)), con criterio de exclusion explicito
de *"any pelvic ring injury, radiographic contrast medium or implants obscuring the
lumbosacral junction"* (Materials and Methods, p. e120(2)). **Excluye justamente los CT con
implantes**, que son el caso de uso de esta tesis.

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

Metodo reimplementable: el protocolo de reformateo y las dos definiciones angulares
(coronal y axial) son operacionales sobre un volumen CT, y el score se calcula con ellas.
Es lo unico de la cadena Kaiser -> McLaren que da una **regla de medida**, no solo un umbral.

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 10 mm de diametro de corredor, **elegido, no medido** | "was chosen as a conservative size for passage of an iliosacral screw" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| 10 mm heredado de refs. 4, 29, 37 | "has been previously established as a reasonably 'safe'-diameter corridor" | Discusion, p. e120(7) |
| Score = (angulo coronal S1) + 2(angulo axial S1) | "sacral dysmorphism score = (first sacral coronal angle) + 2(first sacral axial angle)" | Resultados, p. e120(4) |
| >70 sin corredor transsacro (observacion, no umbral propuesto) | "There were no safe transsacral corridors in any subject with a dysmorphic score >70" | Resultados, p. e120(4) |
| 41% de fenotipo dismorfico | "The dysmorphic phenotype was identified in 41% of the cohort" | Resultados, p. e120(4) |
| Area minima S1 417.4 ± 81.1 mm2 | "417.4 ± 81.1" | Tabla II, p. e120(5) |
| Angulacion coronal S1 22.6 ± 11.1 grados | "22.6 ± 11.1" | Tabla II, p. e120(5) |
| Angulacion axial S1 11 ± 10.5 grados | "11 ± 10.5" | Tabla II, p. e120(5) |
| Margen de 5 mm al cortical para longitud util | "no less than 5 mm of distance to the cortex on either side" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| 104 CT de pelvis no lesionadas | "a consecutive series of 104 uninjured pelves" | Materials and Methods, p. e120(2) |

## Donde entra en mi tesis

**Objetivo 2 (muestreador), restriccion anatomica.** Tres usos distintos y no
intercambiables:

1. **Umbral.** Si la tesis usa 10 mm de diametro de corredor como restriccion dura,
   **Kaiser no es la fuente original**: hay que citarlo como el trabajo que lo adopta y
   lo llama conservador, y la fuente primaria esta en sus refs. 4, 29 y 37. Citarlo como
   "Kaiser establecio 10 mm" repetiria el error que ya tiene `mclaren2021corridor`.
2. **Procedimiento operacional sobre CT.** Esto si es aportado aqui y es lo mas valioso:
   el reformateo perpendicular al platillo superior de S1 y las dos definiciones angulares
   con landmarks oseos (crestas iliacas, espinas iliacas posteriores) son calculables sobre
   un volumen segmentado. Cubren parte del hueco que `mclaren2021corridor` dejo abierto
   (angulos de referencia).
3. **Estratificacion del muestreador.** Los tres fenotipos con sus cortes de longitud
   (>120 mm S1; <120 mm S1 y >110 mm S2; corto en ambos) son una particion citable de la
   poblacion anatomica, con medias y DE de longitud y de los dos angulos por cluster
   (Tabla III).

**Distincion transsacro vs iliosacro (mantenida en toda la ficha).** No son lo mismo y el
paper las mide por separado:
- *Iliosacro*: tornillo que entra por el ilion y **termina dentro del sacro**. Kaiser mide
  su longitud maxima (Tabla II, "Maximum iliosacral screw length": S1 119.2 ± 35.7 mm,
  S2 128.1 ± 20.4 mm) y ese es el corredor de 10 mm cuyo tamano se declara conservador
  *"for passage of an iliosacral screw"*.
- *Transsacro / transiliaco-transsacro*: atraviesa el sacro de lado a lado. Requiere
  corredor ipsilateral **y** contralateral: *"it must traverse the ipsilateral and
  contralateral osseous corridors"* (Introduccion, p. e120(2)). El score >70 y el 41% de
  dismorfismo se refieren a la **ausencia de corredor transsacro en S1**, no al iliosacro.
- El titulo dice *iliosacral* pero el desenlace del score es *transsacral*. Al citar hay
  que decir cual de los dos se esta afirmando.

## Dudas para el asesor

1. Si el 10 mm se hereda tres eslabones (McLaren -> Kaiser -> Gardner 2010 / Ziran 2007 /
   Moed 2006), la tesis lo cita desde el origen o adopta un umbral propio justificado por
   el banco de 61 geometrias? El paper da la pista para lo segundo: 10 mm = holgura de
   1 a 2 mm sobre un tornillo de 6.3 a 8 mm.
2. El score >70 es **descriptivo** (ningun sujeto de esta cohorte lo supero y tuvo corredor
   transsacro), no un umbral validado: no hay sensibilidad, especificidad ni valor p en ese
   punto. Se puede usar como corte del muestreador o solo como referencia?
3. La cohorte es **73% de etnias minoritarias en San Francisco** y los autores piden
   investigar la variacion por etnia. CTPelvic1K es mayoritariamente poblacion china.
   Se traslada el score sin ajuste? El propio Kaiser cita un estudio de morfologia sacra
   en poblacion china (su ref. 36) al discutir esa diferencia.
4. Kaiser excluye CT con implantes. La tesis trabaja precisamente sobre CT con implantes
   (CLINIC-metal). La restriccion se aplica al volumen limpio antes de insertar el implante?
5. Hay **tres rangos distintos** en el paper para las mismas cifras de acuerdo y kappa
   (abstract, Resultados y Discusion no coinciden entre si ni con la Tabla I). Cual se cita?

## Discrepancias internas detectadas (relevantes para la implicancia #25)

Se registran porque afectan que cifra exacta se puede citar.

1. **Acuerdo entre revisores.** Abstract: *"ranged from 70% to 81%"*. Resultados
   (p. e120(3)): *"The agreement rates ranged from 75% to 81%"*. Discusion (p. e120(6)):
   *"with high agreement rates (70% to 80%)"*. La **Tabla I** (p. e120(2)) da 75, 80, 70,
   71 y 81, es decir rango real 70 a 81. Solo el abstract coincide con la tabla.
2. **Kappa.** Abstract: *"kappa coefficients ranged from 0.26 to 0.59"*. Discusion:
   *"moderate agreement according to the kappa analysis (0.29 to 0.59)"*. La Tabla I da
   0.37, 0.59, 0.26, 0.36 y 0.59, es decir 0.26 a 0.59. La Discusion no coincide.
3. **Longitud de tornillo iliosacro S1 vs S2.** Resultados (p. e120(3)): *"maximum estimated
   iliosacral screw length were significantly greater in the first sacral segment than in
   the second"*, pero la Tabla II da S1 119.2 ± 35.7 mm y S2 **128.1** ± 20.4 mm, o sea S2
   mayor. La direccion del enunciado contradice la tabla para esa fila.
4. **Lista de referencias.** Las entradas **17 y 22 son identicas** (Templeman D, Schmidt A,
   Freese J, Weisman I. Clin Orthop Relat Res. 1996 Aug;(329):194-8), duplicadas en la
   p. e120(8).

---

## Evidencia textual

Toda cifra, umbral, definicion de escala o criterio de evaluacion del PDF. Frase original
de 15 palabras o menos. Cuando el dato no esta, la fila dice literalmente
`NO ENCONTRADO EN EL PDF`.

### A. El umbral de 10 mm (pregunta prioritaria)

| Dato | Frase original (corta) | Seccion / pagina | Medido aqui o heredado |
|---|---|---|---|
| Corredor de 10 mm de diametro, en Metodos | "10-mm-diameter corridor perpendicular to the axis of the safe zone was chosen" | Quantification of the Osseous Safe Corridor, p. e120(2) | **Elegido**, con llamada a refs. 29 y 37 |
| Medidas hechas sobre ese corredor | "length of a 10-mm-diameter osseous corridor in the first and second sacral segments" | Quantification of the Osseous Safe Corridor, p. e120(2) | Medido aqui (la longitud, no el umbral) |
| Corredor de 10 mm, en Discusion | "the length of an osseous corridor along the safe zone axis of 10 mm in diameter" | Discusion, p. e120(7) | Medido aqui (la longitud) |
| Justificacion dimensional del 10 mm | "chosen to allow 1 to 2 mm of circumference around a 6.3 to 8-mm-diameter screw" | Discusion, p. e120(7) | **Elegido**, razonamiento propio, sin aritmetica publicada |
| Atribucion explicita del 10 mm a terceros | "has been previously established as a reasonably 'safe'-diameter corridor by experienced surgeons" | Discusion, p. e120(7) | **Heredado**, llamada a refs. 4, 29 y 37 |
| Los autores lo llaman umbral propio y conservador | "because of our conservative 10-mm threshold and not because of a substantive difference" | Discusion, p. e120(7) | **Elegido** |
| Criterio de agrupamiento basado en ese corredor | "the length of an osseous corridor for a 10-mm-diameter iliosacral screw ... is the criterion" | Discusion, p. e120(6) | Criterio de analisis |
| **Kaiser mide el umbral de 10 mm sobre datos propios** | — | — | **NO ENCONTRADO EN EL PDF.** Ninguna frase deriva 10 mm de una medicion de esta cohorte |
| **Valor p, IC o curva que respalde 10 mm frente a 8 o 12 mm** | — | — | **NO ENCONTRADO EN EL PDF** |
| **El termino "8 to 12 mm" o un rango previo de umbrales** | — | — | **NO ENCONTRADO EN EL PDF** (ese rango es de `mclaren2021corridor`, no de aqui) |

### B. Sacral dysmorphism score

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Formula, tal como la escribe el paper | "sacral dysmorphism score = (first sacral coronal angle) + 2(first sacral axial angle)" | Resultados, p. e120(4) |
| Formula en prosa | "summation of the first sacral segment coronal angulation and twice the first sacral segment axial angulation" | Discusion, p. e120(7) |
| Ecuacion de regresion logistica de la que se simplifica | "−0.122(first sacral coronal angle) − 0.268(first sacral axial angle)" | Resultados, p. e120(4) |
| AUROC de esa ecuacion | "The calculated area under the receiver operating characteristic curve (AUROC) for this equation was 0.93" | Resultados, p. e120(4) |
| La simplificacion no baja el AUROC | "We then simplified this relationship without decreasing the AUROC" | Resultados, p. e120(4) |
| Umbral >70, enunciado en Resultados | "There were no safe transsacral corridors in any subject with a dysmorphic score >70" | Resultados, p. e120(4) |
| Umbral >70, enunciado en Discusion | "No patient with a dysmorphic score higher than 70 had an osseous corridor that traversed the sacrum" | Discusion, p. e120(7) |
| Umbral >70, enunciado en el abstract | "No subjects with a sacral dysmorphism score >70 had a safe transsacral first sacral corridor" | Abstract, Resultados, p. e120(1) |
| **Naturaleza del >70: descriptiva, no propuesta como corte** | "the higher the sacral dysmorphism score, the lower the likelihood of the presence of a safe transsacral osseous corridor" | Discusion, p. e120(7) |
| Uso que si proponen los autores | "the sacral dysmorphism score can assist the surgeon in determining whether it is technically appropriate" | Discusion, p. e120(7) |
| Score del caso ejemplo | "Her sacral dysmorphism score was 87" | Case Example, p. e120(5) |
| Score del caso ejemplo, en la figura | "the sacral dysmorphism score was calculated as 87" | Fig. 3, pie, p. e120(5) |
| **Media, desviacion estandar y rango del score en la cohorte** | — | **NO ENCONTRADO EN EL PDF.** La tabla por quintil esta solo en el Appendix online |
| **Tabla del score por quintil** | "A table showing the sacral dysmorphism scores by quintile in the cohort" | Appendix, p. e120(7): remite a jbjs.org, **NO ENCONTRADO EN EL PDF** |
| **Sensibilidad, especificidad o valor p en el punto >70** | — | **NO ENCONTRADO EN EL PDF** |
| **Validacion externa o en cohorte independiente del score** | "Future clinical research is recommended to validate and test the ability to use reformatted CT" | Discusion, p. e120(7): declaran que falta, **NO ENCONTRADO EN EL PDF** |

### C. Como se miden los dos angulos sobre un CT (lo mas reutilizable)

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Reformateo de partida | "Each CT scan was reformatted along the axis of the sacrum to obtain cross-sectional imaging" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| Eje del reformateo, definido en la figura | "the axis was perpendicular to the superior end plate of the first sacral segment" | Fig. 1, pie, panel 2, p. e120(3) |
| Segundo reformateo | "Reformats were then made perpendicular to the first and second sacral osseous corridors" | Fig. 1, pie, paneles 3A y 3B, p. e120(3) |
| **Angulo coronal: definicion completa** | "angle subtended by a line drawn perpendicular to the axis of the osseous corridor" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| **Angulo coronal: segundo landmark** | "and a line connecting the top of the iliac crests" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| **Angulo axial: definicion completa** | "angle subtended by a line drawn perpendicular to the axis of the osseous corridor" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| **Angulo axial: segundo landmark** | "and a line connecting the posterior iliac spines" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| Que se mide en cada panel | "coronal and axial angulations of the first and second sacral segments were measured" | Fig. 1, pie, paneles 4A y 4B, p. e120(3) |
| Los angulos son los determinantes principales | "coronal and axial angulations of the corridor in the first sacral segment are the main determinants" | Discusion, p. e120(6) |
| Recomendacion operativa de los autores | "CT scans obtained to evaluate pelvic fractures be reformatted along the axis of the sacrum" | Discusion, p. e120(7) |
| Los angulos medidos son los "verdaderos" del corredor | "measurement of the true axial and coronal angulation of the corridor" | Discusion, p. e120(7) |
| Anotaciones angulares de la figura de metodo (un solo sujeto) | "35.3°", "71.8° (2D)", "64.7° (2D)", "93.6° (2D)", "84.6° (2D)" | Fig. 1, panel 4A, p. e120(3). **Son anotaciones de un caso, no estadisticos de cohorte** |
| Anotaciones angulares del panel axial (un solo sujeto) | "37.2°", "62.8° (2D)", "70.7° (2D)" | Fig. 1, panel 4B, p. e120(3). Idem |
| Anotaciones lineales de la figura de metodo (un solo sujeto) | "88.9 mm (2D)", "91.6 mm (2D)", "11.2 mm (2D)" | Fig. 1, panel 3B, p. e120(3). Idem |
| Anotaciones angulares del caso clinico | "28", "31" | Fig. 3, paneles 2A y 2B, p. e120(5). Un solo caso |
| Lateralidad | "Each subject was measured bilaterally, and there were no differences in any measurements between sides" | Resultados, p. e120(4) |
| **Convencion de signo o direccion positiva de los angulos** | — | **NO ENCONTRADO EN EL PDF** |
| **Definicion del "axis of the osseous corridor" (como se traza)** | — | **NO ENCONTRADO EN EL PDF.** Se usa en tres definiciones y nunca se define |
| **Coordenadas 3D, punto de entrada o vector de referencia** | — | **NO ENCONTRADO EN EL PDF** |
| **Software o algoritmo automatico de medicion** | "Images were processed on an Advantage Workstation 4.4 (GE Healthcare)" | Materials and Methods, p. e120(2). Es medicion manual en estacion; **algoritmo automatico: NO ENCONTRADO EN EL PDF** |

### D. Definicion de corredor seguro y medidas cuantitativas (Tabla II)

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Que es la "safe zone" | "the first and second sacral osseous corridor, or 'safe zone' for iliosacral screw placement" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| **Definicion de area transversal (criterio de minimo)** | "the least of three measurements of a best-fit circle on contiguous slices perpendicular" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| **Definicion de longitud maxima de tornillo iliosacro** | "the longest line that could be drawn along the axis of the osseous corridor" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| **Margen cortical de esa longitud: 5 mm** | "with no less than 5 mm of distance to the cortex on either side" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| Que se determino con el corredor de 10 mm | "The maximum length of this safe corridor was determined for the first and second sacral segments" | Quantification of the Osseous Safe Corridor, p. e120(2) |
| Condicion para tornillo **transsacro** | "it must traverse the ipsilateral and contralateral osseous corridors" | Introduccion, p. e120(2) |
| Condicion de tamano y orientacion | "which must be of sufficient size and complementary orientation to allow screw placement without a cortical breach" | Introduccion, p. e120(2) |
| Area minima S1 (mm2) | "Minimum cross-sectional area (mm2) ... 417.4 ± 81.1" | Tabla II, p. e120(5) |
| Area minima S2 (mm2) | "213.3 ± 87.9" | Tabla II, p. e120(5) |
| Angulacion coronal S1 (grados) | "Coronal angulation (deg) ... 22.6 ± 11.1" | Tabla II, p. e120(5) |
| Angulacion coronal S2 (grados) | "5.2 ± 4.9" | Tabla II, p. e120(5) |
| Angulacion axial S1 (grados) | "Axial angulation (deg) ... 11 ± 10.5" | Tabla II, p. e120(5) |
| Angulacion axial S2 (grados) | "3.4 ± 4.6" | Tabla II, p. e120(5) |
| Longitud maxima de tornillo **iliosacro** S1 (mm) | "Maximum iliosacral screw length (mm) ... 119.2 ± 35.7" | Tabla II, p. e120(5) |
| Longitud maxima de tornillo **iliosacro** S2 (mm) | "128.1 ± 20.4" | Tabla II, p. e120(5) |
| Valor p de las cuatro filas de la Tabla II | "<0.001" | Tabla II, columna P Value, p. e120(5) |
| Enunciado de esas comparaciones (contradice la fila de longitud) | "significantly greater in the first sacral segment than in the second (p < 0.001 for all)" | Resultados, p. e120(3) |
| Area transversal minima observada en S1 | "The smallest cross-sectional area that we measured in a first sacral osseous corridor was 206 mm2" | Discusion, p. e120(7) |
| Area transversal de un tornillo de 8 mm | "an 8-mm iliosacral screw has a cross-sectional area of 50.2 mm2" | Discusion, p. e120(7) |
| Fraccion con paso transsacro "inseguro" | "passage of a transsacral screw was considered 'unsafe' for nearly half of the subjects" | Discusion, p. e120(7) |
| Ninguno tenia corredor unilateral menor a un tornillo de 8 mm | "none had a unilateral corridor that was too small for passage of an 8-mm screw" | Discusion, p. e120(7) |
| Sensibilidad de la trayectoria (cifra **heredada**, ref. 22) | "A change in trajectory of only 4° can result in cortical perforation" | Introduccion, p. e120(2). Cita de su ref. 22 (Templeman 1996) |
| Tasa de lesion neurovascular (cifra **heredada**, refs. 2 y 6) | "low rates of neurovascular injury, ranging from 0% to 1%" | Discusion, p. e120(6) |
| **Rango (min-max) de las cifras de la Tabla II** | — | **NO ENCONTRADO EN EL PDF.** Solo media ± DE |
| **Diametro maximo (Dmax) del corredor en mm** | — | **NO ENCONTRADO EN EL PDF.** Kaiser mide area transversal, no Dmax; Dmax es la metrica de `mclaren2021corridor` |
| **Margen en mm al foramen sacro o al canal** | — | **NO ENCONTRADO EN EL PDF** |
| **Tolerancia angular propia en grados** | — | **NO ENCONTRADO EN EL PDF.** El 4° es cita de terceros |
| **Numero absoluto de sujetos con corredor transsacro seguro** | — | **NO ENCONTRADO EN EL PDF.** Solo "nearly half" |
| **Diametro de tornillo usado en el caso clinico** | — | **NO ENCONTRADO EN EL PDF** |

### E. Las cinco caracteristicas cualitativas de displasia del segmento sacro superior

Enunciado textual, en el orden y con la numeracion del paper (Qualitative Analysis,
p. e120(2)): *"(1) an upper sacral segment not recessed in the pelvis, (2) the presence of
mammillary processes, (3) an acute alar slope, (4) a residual disc between the first and
second sacral segments, and (5) noncircular upper sacral neural foramina."*
La sexta, evaluada aparte: *"The axial CT scan was reviewed for the presence or absence of a
'tongue-in-groove' sacroiliac morphology."*

| Caracteristica (nombre en Tabla I) | Revisor 1 (%) | Revisor 2 (%) | Acuerdo (%) | Kappa | Seccion / pagina |
|---|---|---|---|---|---|
| Upper sacral segment not recessed in pelvis | 33 | 33 | 75 | 0.37 | Tabla I, p. e120(2) |
| Mamillary bodies | 53 | 52 | 80 | 0.59 | Tabla I, p. e120(2) |
| Misshapen sacral foramen | 28 | 31 | 70 | 0.26 | Tabla I, p. e120(2) |
| Residual disc | 35 | 36 | 71 | 0.36 | Tabla I, p. e120(2) |
| Acute alar slope | 35 | 36 | 81 | 0.59 | Tabla I, p. e120(2) |

| Dato agregado | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Prevalencias (abstract) | "as determined by two reviewers, ranged from 28% to 53% in the cohort" | Abstract, Resultados, p. e120(1) |
| Prevalencias (Resultados) | "The prevalences as determined by the two reviewers ranged between 28% to 53%" | Resultados, p. e120(3) |
| Acuerdo (abstract) — coincide con Tabla I | "The rates of agreement between the two reviewers ranged from 70% to 81%" | Abstract, p. e120(1) |
| Acuerdo (Resultados) — **no coincide con Tabla I** | "The agreement rates ranged from 75% to 81%" | Resultados, p. e120(3) |
| Acuerdo (Discusion) — **no coincide con Tabla I** | "with high agreement rates (70% to 80%)" | Discusion, p. e120(6) |
| Kappa (abstract) — coincide con Tabla I | "kappa coefficients ranged from 0.26 to 0.59" | Abstract, p. e120(1) |
| Kappa (Discusion) — **no coincide con Tabla I** | "moderate agreement according to the kappa analysis (0.29 to 0.59)" | Discusion, p. e120(6) |
| Interpretacion cualitativa del kappa | "the kappa values ranged from fair to moderate" | Resultados, p. e120(3) |
| Kappas mas altos | "The highest kappa values were for the presence of mamillary bodies and acute alar slope" | Resultados, p. e120(3) |
| Quien evaluo | "Two orthopaedic traumatologists reviewed each outlet reconstruction" | Qualitative Analysis, p. e120(2) |
| Modo de evaluacion | "independently reviewed the outlet views and an axial CT scan and determined in binary fashion" | Resultados, p. e120(3) |
| Las cualitativas no son determinantes de variabilidad | "We did not find the qualitative characteristics of sacral dysmorphism to be significant determinants of variability" | Discusion, p. e120(6) |
| Escala de interpretacion del kappa que usan | "Landis JR, Koch GG. The measurement of observer agreement for categorical data" | Referencia 35, p. e120(8). **La tabla de interpretacion no se reproduce: NO ENCONTRADO EN EL PDF** |
| **Acuerdo intraobservador** | — | **NO ENCONTRADO EN EL PDF.** Solo interobservador |
| **Intervalos de confianza de los kappas** | — | **NO ENCONTRADO EN EL PDF** |

### F. Los tres fenotipos del analisis de conglomerados

| Fenotipo | Definicion textual | Frecuencia | Seccion / pagina |
|---|---|---|---|
| Cluster 1, Majority | "there was a measurable safe corridor for passage of a long screw in the first sacral segment" | **NO ENCONTRADO EN EL PDF** (no se da el %) | Resultados, p. e120(4) |
| Cluster 1, criterio numerico | "The safe corridor measured >120 mm in the first sacral segment in all subjects" | — | Resultados, p. e120(4) |
| Cluster 2, Dysmorphic | "insertion of a long screw was not possible in the first sacral segment but was possible in the second" | 41% | Resultados, p. e120(4) |
| Cluster 2, criterio numerico | "the safe corridor measured <120 mm in the first sacral segment and >110 mm in the second" | — | Resultados, p. e120(4) |
| Cluster 2, frecuencia | "The dysmorphic phenotype was identified in 41% of the cohort" | 41% | Resultados, p. e120(4) |
| Cluster 3, Minority | "a minority phenotype (12%), in which the measurable safe corridor was short in both sacral segments" | 12% | Resultados, p. e120(4) |
| Conclusion del abstract | "Sacral dysmorphism was found in 41% of the pelves" | 41% | Abstract, Conclusiones, p. e120(1) |
| Prevalencia en Discusion | "we found a 41% prevalence of the condition" | 41% | Discusion, p. e120(6) |
| Base del agrupamiento | "three distinct clusters emerged on the basis of the length of the measurable 10-mm-diameter safe osseous corridor" | — | Resultados, p. e120(4) |
| Definicion de dismorfismo que proponen | "sacral dysmorphism is present when a transsacral screw cannot be safely passed in the first sacral segment" | — | Discusion, p. e120(6) |
| Complemento de esa definicion | "but can be safely placed in the second segment" | — | Discusion, p. e120(6) |
| Ese patron es heredado | "Previous authors have defined this pattern" | — | Discusion, p. e120(6). Llamada a refs. 29 y 30 |
| Comparacion con prevalencias previas (**heredada**) | "prior studies, in which the prevalences ranged from 30% to 50%" | 30-50% | Discusion, p. e120(6). Llamada a refs. 27-29 |
| Explicacion de estar en el extremo alto | "the ethnic composition of our cohort, with a 73% prevalence of minority ethnicities" | 73% | Discusion, p. e120(6) |

**Tabla III — S1, longitud y angulacion por cluster (p. e120(6)):**

| Variable | Cluster 1 Majority | Cluster 2 Dysmorphic | Cluster 3 Minority | P Value |
|---|---|---|---|---|
| Corridor length (mm) | 155.2 ± 12.7 | 87.9 ± 10.7 | 86.6 ± 10.7 | <0.001 |
| Coronal angulation (deg) | 15.8 ± 8.3 | 29.6 ± 9.4 | 23.8 ± 8.4 | <0.001 |
| Axial angulation (deg) | 5.0 ± 6.7 | 18.5 ± 9.5 | 14.9 ± 10.1 | <0.001 |

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Enunciado que respalda la Tabla III | "the angulation of the corridor in the coronal and axial planes varied significantly among the three clusters" | Resultados, p. e120(4) |
| Frecuencia de las cinco cualitativas por cluster | "found to be present significantly more frequently in the dysmorphic cluster (p < 0.007)" | Resultados, p. e120(4) |
| Valores p de la Fig. 2 | "*p < 0.00001. **p = 0.0001" | Fig. 2, pie, p. e120(4) |
| Tongue-in-groove no discrimina | "was not found to differ significantly among the clusters (p = 0.107)" | Fig. 2, pie, p. e120(4) |
| Tongue-in-groove, repetido en el cuerpo | "was not significantly more frequent in the dysmorphic cluster (p = 0.107)" | Resultados, p. e120(5) |
| **Frecuencias numericas exactas de la Fig. 2 por cluster** | — | **NO ENCONTRADO EN EL PDF.** Solo hay barras, sin tabla ni etiquetas de valor |
| **n absoluto de cada cluster** | — | **NO ENCONTRADO EN EL PDF.** Solo 41% y 12% |
| **Tabla III para el segundo segmento sacro (S2)** | — | **NO ENCONTRADO EN EL PDF.** La Tabla III es solo de S1 |
| **Figura de longitudes S1 vs S2 por cluster** | "a figure demonstrating the three clusters graphed according to the first and second sacral corridor lengths" | Appendix, p. e120(7): remite a jbjs.org, **NO ENCONTRADO EN EL PDF** |

### G. Relacion inversa entre angulos y corredor largo

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Enunciado de la relacion (abstract) | "An inverse linear relationship between these angles and a long upper sacral segment corridor" | Abstract, Resultados, p. e120(1) |
| Varianza explicada por los dos angulos | "The most efficient explanation of variance of data (74% accuracy) was achieved with reduction" | Resultados, p. e120(4) |
| A que dos variables se reduce | "to the two variables of first sacral coronal angulation and first sacral axial angulation" | Resultados, p. e120(4) |
| Funcion discriminante | "Model reduction performed in hierarchical fashion resulted in a significant discriminant function (p < 0.0001)" | Resultados, p. e120(4) |
| Coeficientes de la regresion logistica | "−0.122(first sacral coronal angle) − 0.268(first sacral axial angle)" | Resultados, p. e120(4) |
| AUROC | "the AUROC for this equation was 0.93" | Resultados, p. e120(4) |
| Relacion inversa por quintil | "there is an inverse relationship between the magnitude of the sacral dysmorphism score and the probability" | Resultados, p. e120(4) |
| Direccion de la relacion | "The higher this score, the less likely there is a safe transsacral corridor" | Resultados, p. e120(4) |
| Criterio de retencion de componentes | "The number of components retained was based on scree plot analysis and eigenvalues greater than one" | Statistical Analysis, p. e120(2) |
| Primer componente principal | "stressed the importance of anatomic relationships in the lumbar spine and sacrum" | Resultados, p. e120(4) |
| Segundo componente principal | "characterized by racial characteristics, with Latino race carrying the highest factor loading" | Resultados, p. e120(4) |
| Determinantes etnicos identificados | "Latino, African American, and Asian ethnicity were identified as significant determinants of variation" | Discusion, p. e120(6) |
| **Coeficiente r o r2 de la relacion lineal** | — | **NO ENCONTRADO EN EL PDF** |
| **Intervalos de confianza de los coeficientes −0.122 y −0.268** | — | **NO ENCONTRADO EN EL PDF** |
| **Valor p individual de cada coeficiente** | — | **NO ENCONTRADO EN EL PDF** |
| **Cifras por quintil de la relacion inversa** | — | **NO ENCONTRADO EN EL PDF.** Remitidas al Appendix online |

### H. Poblacion y adquisicion

| Dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Tamano y tipo de cohorte | "a consecutive series of 104 uninjured pelves for which computed tomography (CT) scans had been obtained" | Materials and Methods, p. e120(2) |
| Periodo y centro | "during a two-month period in 2010 at a level-I trauma center" | Materials and Methods, p. e120(2) |
| Institucion | "Investigation performed at San Francisco General Hospital, San Francisco, California" | Portada, p. e120(1) |
| **Escaner** | "CT was conducted with a GE LightSpeed VCT sixty-four-slice scanner (GE Healthcare, Waukesha, Wisconsin)" | Materials and Methods, p. e120(2) |
| **Colimacion** | "with a collimation of 64 × 1.25 mm" | Materials and Methods, p. e120(2) |
| Estacion de procesamiento | "Images were processed on an Advantage Workstation 4.4 (GE Healthcare)" | Materials and Methods, p. e120(2) |
| Aprobacion etica | "Institutional review board approval was obtained" | Materials and Methods, p. e120(2) |
| Criterio de inclusion, edad | "an age over eighteen years" | Materials and Methods, p. e120(2) |
| Criterio de inclusion, cobertura | "imaging included the lowest rib-bearing vertebra and the entire pelvis" | Materials and Methods, p. e120(2) |
| **Criterio de exclusion (incluye implantes)** | "any pelvic ring injury, radiographic contrast medium or implants obscuring the lumbosacral junction" | Materials and Methods, p. e120(2) |
| Criterio de exclusion, resto | "lumbar scoliosis of >20°, or spina bifida" | Materials and Methods, p. e120(2) |
| Numero analizado | "One hundred and four consecutive CT scans of uninjured pelves were analyzed" | Resultados, p. e120(3) |
| Sexo | "The demographics of the study population were 60% female" | Resultados, p. e120(3) |
| Edad | "an average age of forty-nine years (range, eighteen to eighty-nine years)" | Resultados, p. e120(3) |
| Etnia | "29% Latino, 26% Asian, 22% white, 18% black, and 5% other" | Resultados, p. e120(3) |
| Talla | "The average height was 165 cm (range, 147 to 196 cm)" | Resultados, p. e120(3) |
| Peso | "average weight was 81 kg (range, 50 to 169 kg)" | Resultados, p. e120(3) |
| IMC | "average body mass index (BMI) was 29 kg/m2 (range, 19 to 50 kg/m2)" | Resultados, p. e120(3) |
| Indicaciones del CT | "flank/abdominal/back pain (65%), hematuria (22%), trauma (3%), and other indications (10%)" | Resultados, p. e120(3) |
| Reformateo para vista outlet | "Volumetric holography was used to create virtual outlet images for qualitative analysis" | Qualitative Analysis, p. e120(2) |
| Correccion de rotacion horizontal | "neutral horizontal rotation was corrected by aligning lumbar spinous processes with the symphysis pubis" | Qualitative Analysis, p. e120(2) |
| Correccion de rotacion vertical | "adjusted to align the superior cortex of the pubis with the second sacral segment body" | Qualitative Analysis, p. e120(2) |
| Software estadistico | "STATA/SE statistical software (College Station, Texas) was used for the analysis" | Resultados, p. e120(3) |
| Tipo de analisis de conglomerados | "Hierarchical cluster analysis was used to test the hypothesis that sacra would cluster" | Statistical Analysis, p. e120(2) |
| Ponderacion de kappa | "Weighted kappa coefficients were used for characteristics with more than two categories" | Statistical Analysis, p. e120(2) |
| Financiamiento | "There were no external sources of funding" | Source of Funding, p. e120(3) |
| **Grosor de corte de reconstruccion o de los reformats** | — | **NO ENCONTRADO EN EL PDF.** Solo se da la colimacion |
| **Resolucion en plano, tamano de pixel o matriz** | — | **NO ENCONTRADO EN EL PDF** |
| **kVp, mAs, pitch o dosis** | — | **NO ENCONTRADO EN EL PDF** |
| **Kernel o algoritmo de reconstruccion** | — | **NO ENCONTRADO EN EL PDF** |
| **Ventana HU usada para medir el hueso cortical** | — | **NO ENCONTRADO EN EL PDF** |
| **Umbral HU para definir la cortical o el corredor** | — | **NO ENCONTRADO EN EL PDF** |

### I. Transsacro vs iliosacro: que mide cada cifra

| Cifra | A que trayectoria se refiere | Evidencia |
|---|---|---|
| Corredor de 10 mm de diametro | **Iliosacro** | "conservative size for passage of an iliosacral screw" (Metodos, p. e120(2)) |
| Longitud maxima 119.2 mm (S1) y 128.1 mm (S2) | **Iliosacro** | "Maximum iliosacral screw length (mm)" (Tabla II, p. e120(5)) |
| Area minima 417.4 mm2 (S1) y 213.3 mm2 (S2) | Corredor oseo, sin trayectoria especificada | "Minimum cross-sectional area (mm2)" (Tabla II, p. e120(5)) |
| Cortes de 120 mm y 110 mm de los clusters | Corredor de 10 mm, "long screw" | "The safe corridor measured >120 mm in the first sacral segment" (Resultados, p. e120(4)) |
| 41% dismorfico | **Transsacro en S1 imposible, S2 posible** | "a transsacral screw cannot be safely passed in the first sacral segment but can be safely placed in the second" (Discusion, p. e120(6)) |
| Score >70 | **Transsacro en S1** | "No subjects with a sacral dysmorphism score >70 had a safe transsacral first sacral corridor" (Abstract, p. e120(1)) |
| "nearly half" inseguro | **Transsacro** | "passage of a transsacral screw was considered 'unsafe' for nearly half of the subjects" (Discusion, p. e120(7)) |
| 4° de cambio de trayectoria | Perforacion cortical, sin distinguir | "A change in trajectory of only 4° can result in cortical perforation" (Introduccion, p. e120(2)) |
| **Definicion en mm de cuando un corredor pasa a ser "transsacro"** | — | **NO ENCONTRADO EN EL PDF.** Los 120 y 110 mm describen clusters, no definen el termino |

### J. Limitaciones declaradas por los autores

No hay seccion titulada "Limitations". Lo que sigue esta disperso en la Discusion.

| Limitacion | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Sesgo del umbral de 10 mm sobre el Cluster 3 | "classified as such because of our conservative 10-mm threshold and not because of a substantive difference" | Discusion, p. e120(7) |
| Un cirujano experto podria pasar tornillos que ellos llaman inseguros | "it would be technically possible to pass it in a transsacral fashion without cortical perforation" | Discusion, p. e120(7) |
| Fraccion de esos casos desconocida | "in an unknown percentage of the subjects for whom we determined the screw passage to be 'unsafe'" | Discusion, p. e120(7) |
| Falta validacion clinica del score | "Future clinical research is recommended to validate and test the ability to use reformatted CT imaging" | Discusion, p. e120(7) |
| **Aplicabilidad a otras poblaciones: si lo declaran** | "Additional research and larger sample sizes are warranted to explore variation in sacral morphology by ethnicity" | Discusion, p. e120(6) |
| Su cohorte esta en el extremo alto de prevalencia | "This is at the higher end of the prevalences reported in other studies" | Discusion, p. e120(6) |
| Las cualitativas no explicaron la variabilidad | "This is likely due to the high prevalence of each characteristic within the cohort" | Discusion, p. e120(6) |
| Marcador poco fiable | "The tongue-in-groove characteristic, seen on axial CT, is a less reliable marker for dysmorphism" | Discusion, p. e120(6) |
| **Aplicabilidad a planificacion automatica: hay una frase A FAVOR** | "may represent an ideal application of computer navigation technology" | Discusion, p. e120(7) |
| Contexto de esa frase | "The complex three-dimensional morphology of the sacral osseous corridor presents a challenge to surgeons" | Discusion, p. e120(7) |
| Uso propuesto del score | "We recommend use of these CT reformats and the sacral dysmorphism score in preoperative planning" | Discusion, p. e120(7) |
| **Frase que diga que el metodo NO sirve para planificacion automatica** | — | **NO ENCONTRADO EN EL PDF** |
| **Declaracion de limitacion por diseno retrospectivo o por tamano de muestra** | — | **NO ENCONTRADO EN EL PDF** |
| **Analisis de reproducibilidad de las medidas cuantitativas (no las cualitativas)** | — | **NO ENCONTRADO EN EL PDF.** El kappa cubre solo las cinco cualitativas |
| **Declaracion sobre generalizacion a pelvis fracturadas** | — | **NO ENCONTRADO EN EL PDF.** La cohorte es de pelvis no lesionadas y no se discute el traslado |

### K. Aritmetica propia (derivacion, NUNCA cita)

**Derivacion propia, no del paper:** el paper afirma que 10 mm deja *"1 to 2 mm of
circumference around a 6.3 to 8-mm-diameter screw"*, pero **no publica la operacion**.
Cualquier reconstruccion de esa cuenta (por ejemplo 8 mm + 2 x 1 mm = 10 mm) es
**derivacion propia** y no puede citarse como resultado de Kaiser. El PDF no contiene esa
aritmetica: **NO ENCONTRADO EN EL PDF**.

### Recuento

**41 entradas cerradas como NO ENCONTRADO EN EL PDF**, repartidas asi: A=3, B=4, C=4,
D=6, E=3, F=5, G=4, H=6, I=1, J=4, K=1. Tres de ellas dependen del Appendix online
(media/DE/rango del score, tabla por quintil, figura de longitudes S1 vs S2 por cluster).
