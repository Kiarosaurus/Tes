# sayres2014comparison — Tornillos canulados grandes vs pequenos en osteotomia de calcaneo

- **DOI / URL:** 10.1177/1071100714549191 (Foot Ankle Int. 2015;36(1):32-36; epub 2014-09-04)
- **Nivel de lectura:** 3 (contexto) — *nivel propuesto por el asistente, decide la autora*
- **Leido a fondo por la autora:** no
- **PDF:** papers/sayres2014comparison.pdf

Profundidad: PDF completo (5 pp., pp. 32-36 incluidas referencias).

## Que hace (3 lineas maximo)
Serie retrospectiva de 272 pies operados de osteotomia de calcaneo (1996-2012) que compara
tasa de consolidacion y de retiro de material entre tornillos canulados de 7.3, 6.5 y 4.5 mm.
**Para esta tesis solo importa un parrafo:** el unico pasaje verificado del repositorio que
publica el **diametro de la cabeza** de un canulado de 7.3 mm.

## Restriccion o supuesto clave
No es un paper de sintesis. Su supuesto implicito es el que interesa: el clinico distingue
"7.3 mm" (rosca) de la cabeza, y atribuye el problema clinico a la cabeza, no al calibre
nominal — *"Removal appeared to be more closely correlated to the prominence of the screw
head"* (Discusion, p. 35, citando a Abbasian). Y no se avellana: *"No countersink was used in
attempt to minimize the incision size"* (Operative Technique, p. 33), asi que la cabeza queda
**sobresaliendo de la cortical**, que es exactamente el escenario de artefacto que #97 supone
para la cabeza y la arandela en la cortical iliaca.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| **Cabeza de 8.0 mm para el tornillo de 7.3 mm** | *"The diameter of the heads of 7.3 mm and 6.5 mm cannulated screws is 8.0 mm"* | Discusion, p. 34 (CUERPO, no solo figura) |
| Altura de cabeza 4.5 mm (7.3 y 6.5 mm) | *"the head height thickness of the 7.3 mm and 6.5 mm cannulated screws is 4.5 mm"* | Discusion, p. 34 |
| Cabeza de 6.0 mm para el de 4.5 mm | *"the diameter of a 4.5 mm cannulated screw head is 6.0 mm"* | Discusion, p. 34 |
| Altura de cabeza 3.0 mm (4.5 mm) | *"the height of the 4.5 mm screw head is 3.0 mm"* | Discusion, p. 34 |
| Fabricante | *"cannulated screws (Synthes, West Chester PA) were placed under manual power"* | Operative Technique, p. 33 |
| Paso de rosca (numero) | **NO ENCONTRADO EN EL PDF** (solo *"large pitch of the screw threads"*, cualitativo, p. 32) | — |
| Diametro de fuste | **NO ENCONTRADO EN EL PDF** | — |
| Diametro de nucleo | **NO ENCONTRADO EN EL PDF** | — |
| Longitud roscada | **NO ENCONTRADO EN EL PDF** | — |
| Diametro de la canulacion | **NO ENCONTRADO EN EL PDF** | — |
| Material del tornillo | **NO ENCONTRADO EN EL PDF** | — |
| Arandela | **NO ENCONTRADO EN EL PDF** | — |

## Respuesta directa a la pregunta 5 del encargo
**SI. El cuerpo del articulo atribuye explicitamente una cabeza de 8.0 mm al tornillo de
7.3 mm, en texto corrido de la Discusion (p. 34), no solo en una figura:**
*"The diameter of the heads of 7.3 mm and 6.5 mm cannulated screws is 8.0 mm, whereas the
diameter of a 4.5 mm cannulated screw head is 6.0 mm (Figure 2)."*
La misma cifra se repite en el pie de la Figura 2 (p. 35): *"The 7.3 mm cannulated screws have
a head diameter of 8.0 mm"*. Con esto, la afirmacion G5 de `_candidatos.md` deja de ser
provisional y el "8.2 mm" del otro documento de deep-research **no tiene respaldo aqui**.

**Tres avisos antes de citarla:**
1. **La cifra no lleva fuente ni numero de catalogo.** No se cita al fabricante ni una ficha
   tecnica; es medicion o dato de los autores, sin metodo declarado. Es nodo TERMINAL para la
   cabeza de 8.0 mm, con el mismo patron que Moed para el "1 cm".
2. **Erratum de imprenta en el pie de la Figura 2 (p. 35):** dice *"the 4.3 mm cannulated
   screws have a head diameter of 6.0 mm"*, donde todo el resto del paper dice 4.5 mm. No
   afecta al 8.0 mm, pero conviene citar el cuerpo (p. 34), no el pie de figura.
3. **La atribucion es al sistema de Synthes** que ellos usaron; el paper no declara que sea
   universal para todo canulado de 7.3 mm.

## Donde entra en mi tesis
- **Implicancia #97.** Cierra el tercer hueco de los cuatro pedidos: **cabeza = 8.0 mm**
  (verificado). Sumado a `zhu2022optimalposition` (paso 2.5 mm, rosca 16 mm, fuste 4.8 mm),
  quedan verificados paso, longitud roscada, fuste y cabeza. **Siguen sin fuente verificada:**
  nucleo, canulacion y **arandela** (G1/T1).
- **Implicancia #95.** Refuerza que el implante no es un cilindro de diametro constante: la
  cabeza (8.0 mm de diametro, 4.5 mm de altura) es un volumen **mas ancho que la rosca** y,
  sin avellanado, queda sobre la cortical. Un cilindro liso de 6.5-8.0 mm en todo el trayecto
  (`main.tex:113`) reproduce por casualidad el diametro de la cabeza y sobreestima el resto.
- **NO aplicar sin decision de la autora (regla 14).**

## Limites de traslado a iliosacro
1. **Anatomia: calcaneo, no pelvis.** *"insert 2 screws upward into the calcaneus from the
   posterior aspect of the heel"* (Discusion, p. 34). "Sacrum", "iliosacral", "sacroiliac",
   "pelvis" y "S1/S2": NO ENCONTRADO EN EL PDF.
2. **La indicacion es opuesta a la de la tesis.** Aqui el hallazgo clinico es que **conviene
   bajar a 4.5 mm**; en iliosacro el calibre de 7.3 mm es el estandar de todas las fuentes ya
   leidas (`ziran2003`, `gardner2011transiliac-transsacral`, `mendel2011`, `grass2016`). La
   conclusion clinica **no se traslada**; solo la dimension del dispositivo.
3. **El mecanismo del desenlace es tejido blando, no hueso.** El desenlace es dolor en el talon
   y retiro del material por prominencia bajo la almohadilla grasa; nada de brecha cortical,
   corredor oseo ni lesion neurologica. No aporta nada al muestreador ni al benchmark SAP/BFC.
4. **Sin avellanado por decision de los cirujanos** (p. 33): en iliosacro la cabeza suele
   apoyarse en la tabla externa del ilion, a veces con arandela. Son montajes distintos.
5. **Sin geometria del cuerpo del tornillo.** No da fuste, nucleo, paso ni longitud roscada:
   para esas cuatro hay que ir a `zhu2022optimalposition` y a G1/G2/T1.

## Que dice del CT, la imagen y los artefactos
- **CT: NO ENCONTRADO EN EL PDF.** "Computed tomography", "CT", "artifact", "Hounsfield", "HU"
  y "MAR": ninguna mencion.
- Toda la imagen es **radiografia simple y fluoroscopia intraoperatoria**: *"Position was
  checked on intraoperative fluoroscopy, then fixation was achieved"* (Operative Technique,
  p. 33) y *"These 2-week postoperative radiographs show osteotomies fixed with two 7.3 mm
  cannulated screws"* (pie de la Figura 1, p. 33).
- Las Figuras 2 y 3 (p. 35) son **fotografias de los tornillos reales**, no imagen medica. Son
  la ilustracion de donde salen las cifras de cabeza, pero las cifras estan tambien en texto.
- No hay ninguna medicion de imagen: la revision es de historias clinicas y radiografias, sin
  criterio cuantitativo ni observador cegado declarado.

## Evidencia textual

### Geometria del tornillo (lo que busca #97)
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| **Diametro de cabeza, 7.3 y 6.5 mm** | *"The diameter of the heads of 7.3 mm and 6.5 mm cannulated screws is 8.0 mm"* | Discusion, p. 34 (cuerpo) |
| Diametro de cabeza, 4.5 mm | *"the diameter of a 4.5 mm cannulated screw head is 6.0 mm"* | Discusion, p. 34 |
| **Altura de cabeza, 7.3 y 6.5 mm** | *"the head height thickness of the 7.3 mm and 6.5 mm cannulated screws is 4.5 mm"* | Discusion, p. 34 |
| Altura de cabeza, 4.5 mm | *"the height of the 4.5 mm screw head is 3.0 mm"* | Discusion, p. 34 |
| Repeticion en figura | *"The 7.3 mm cannulated screws have a head diameter of 8.0 mm"* | Pie Figura 2, p. 35 |
| **Errata del pie de figura** | *"the 4.3 mm cannulated screws have a head diameter of 6.0 mm"* | Pie Figura 2, p. 35 |
| Fabricante | *"(Synthes, West Chester PA)"* | Operative Technique, p. 33 |
| Canulado (via de retiro) | *"a 0.062 in K-wire was inserted into the cannulated shaft"* | Operative Technique, p. 33 |
| Tornillo con cabeza (headed) | *"the first to compare ... union rates between different sized headed screws"* | Discusion, p. 34 |
| Rosca gruesa, sin cifra | *"large pitch of the screw threads for fixation in cancellous bone"* | Introduccion, p. 32 |
| Cabeza mas pequena en el 6.5 mm | *"6.5 mm cannulated screws were used due to their slightly smaller head and thread diameter"* | Introduccion, p. 32 |
| Sin avellanado | *"No countersink was used in attempt to minimize the incision size"* | Operative Technique, p. 33 |
| Paso de rosca (valor numerico) | NO ENCONTRADO EN EL PDF | — |
| Diametro de fuste | NO ENCONTRADO EN EL PDF | — |
| Diametro de nucleo (root/core) | NO ENCONTRADO EN EL PDF | — |
| Longitud roscada | NO ENCONTRADO EN EL PDF | — |
| Longitud total del tornillo | NO ENCONTRADO EN EL PDF | — |
| Diametro de la canulacion (agujero) | NO ENCONTRADO EN EL PDF | — |
| Parcialmente roscado (para el propio estudio) | NO ENCONTRADO EN EL PDF (solo al describir a Abbasian, p. 35) | — |
| Material (titanio / acero / ASTM) | NO ENCONTRADO EN EL PDF | — |
| Arandela / washer | NO ENCONTRADO EN EL PDF | — |
| Referencia o catalogo de las cifras de cabeza | NO ENCONTRADO EN EL PDF | — |

### Cohorte, criterios y desenlaces
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Casos revisados | *"There were 411 cases that were found"* | Metodos, p. 33 |
| Poblacion final | *"The records of 255 patients (272 feet) met our inclusion criteria"* | Metodos, p. 33 |
| Periodo | *"between January 1996 and April 2012"* | Metodos, p. 33 |
| Seguimiento minimo | *"a postoperative follow-up period of at least 2 years"* | Metodos, p. 33 |
| Exclusion por edad | *"under 18 years of age at the time of surgery (15 feet)"* | Metodos, p. 33 |
| Exclusion por otro material | *"other screw sizes or other types of fixation (67 feet)"* | Metodos, p. 33 |
| Exclusion por registro | *"incomplete medical records or no clear documentation of screw size (57 feet)"* | Metodos, p. 33 |
| Edad media | *"The average patient age was 55.0 (range, 18-82) years"* | Metodos, p. 33 |
| Sexo | *"177 feet belonging to females and 95 belonging to males"* | Metodos, p. 33 |
| Lateralidad | *"The ratio of left feet to right feet was 138 to 134"* | Metodos, p. 33 |
| Reparto por calibre | *"130 osteotomies ... 7.3 mm ... 27 ... 6.5 mm ... 115 ... 4.5 mm"* | Metodos, p. 33 |
| Osteotomia medializante | *"A medializing calcaneal osteotomy was performed in 216 feet (79.4%)"* | Metodos, p. 33 |
| Cuna lateral de cierre | *"A lateral closing wedge calcaneal osteotomy was performed in 52 feet (19.1%)"* | Metodos, p. 33 |
| Desplazamiento de la osteotomia | *"After sliding the osteotomy approximately 1 cm"* | Operative Technique, p. 33 |
| **Consolidacion** | *"The union rate for all groups was 100%."* | Resultados, p. 33 |
| Retiro, 7.3 mm | *"38 feet (29.2%) had the screws removed at an average of 1.63 years"* | Resultados, p. 34 |
| Retiro, 4.5 mm | *"15 feet (13.0%) had the screws removed at an average of 1.00 years"* | Resultados, p. 34 |
| Retiro, 6.5 mm | *"9 feet (33.3%) had them removed at an average of 3.1 years"* | Resultados, p. 34 |
| Prueba estadistica | *"using the chi-square test (P < .05)"* | Resultados, p. 33 |
| Causa del retiro (7.3 mm) | *"Posterior heel pain was cause for hardware removal in 32 of the 38 feet"* | Resultados, p. 34 |
| Causa del retiro (4.5 mm) | *"the cause of hardware removal in 14 of 15 feet"* | Resultados, p. 34 |
| Rango de consolidacion en la literatura | *"reported in the literature to be very high (90% to 100%)"* | Discusion, p. 34 |
| Tasa maxima de retiro citada | *"has been reported to be as high as 53%"* | Discusion, p. 34 |
| Nivel de evidencia | *"Level of Evidence: Level IV, retrospective case series."* | Abstract, p. 32 |
| Fiabilidad / cegamiento / kappa | NO ENCONTRADO EN EL PDF | — |
| Definicion operacional de "union" | NO ENCONTRADO EN EL PDF | — |
| Potencia estadistica / tamano muestral | NO ENCONTRADO EN EL PDF | — |

### Imagen
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Fluoroscopia intraoperatoria | *"Position was checked on intraoperative fluoroscopy, then fixation was achieved"* | Operative Technique, p. 33 |
| Radiografia postoperatoria | *"These 2-week postoperative radiographs show osteotomies fixed with two 7.3 mm cannulated screws"* | Pie Figura 1, p. 33 |
| Revision de imagen | *"pre- and postoperative radiographs were reviewed to determine union rates"* | Metodos, p. 33 |
| CT / tomografia | NO ENCONTRADO EN EL PDF | — |
| Artefacto metalico / MAR | NO ENCONTRADO EN EL PDF | — |
| HU / Hounsfield / ventanas | NO ENCONTRADO EN EL PDF | — |

### Cifras de terceros citadas (no medidas aqui)
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Abbasian, union global | *"found an overall 97% union rate"* | Discusion, p. 34 |
| Abbasian, retiro por tipo | *"47% of patients (8 of 17) ... 11% (2 of 18) ... 6% (2 of 32)"* | Discusion, p. 35 |
| DiDomenico | *"a delayed union rate of 5.88% in a study of 34 feet"* | Discusion, p. 34 |
| Konan, carga | *"loaded to 4500 N to determine at what force they failed"* | Discusion, p. 35 |
| Konan, fuerza maxima | *"higher maximum force (median 1779 N) than the cannulated screw (median 826 N)"* | Discusion, p. 35 |
| Costo de tornillos sin cabeza | *"The cost of headless screws is nearly double that of headed screws"* | Discusion, p. 34 |

## Dudas para el asesor
1. ¿Se acepta el **8.0 mm de cabeza** citando un paper de **calcaneo**, declarando que es la
   geometria del dispositivo (Synthes) y no la indicacion? Es la unica cifra verificada de
   cabeza que hay hoy en el repositorio.
2. La cifra **no lleva fuente ni catalogo**. ¿Se cita igual, o se espera la ficha tecnica T1
   de Synthes, que no es paper revisado por pares (regla 9)?
3. Si se modela la cabeza: ¿entra tambien la **altura de 4.5 mm** y el hecho de que **no se
   avellana**? Para la mascara iliosacra eso decide si la cabeza queda dentro o fuera de la
   cortical iliaca, que es lo que mas artefacto emitiria (#97, punto 3).
4. ¿Conviene una nota en `main.tex` de que el nominal de 7.3 mm y la cabeza de 8.0 mm **casi
   coinciden**, de modo que el cilindro liso actual reproduce la cabeza pero no el fuste?
