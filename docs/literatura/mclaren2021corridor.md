# mclaren2021corridor — Tolerancia angular dependiente del diametro del corredor transiliosacro (433 pelvis)

- **DOI / URL:** https://doi.org/10.1007/s00590-021-02913-5 (Eur J Orthop Surg Traumatol, 2021, 31(7):1485-1492; PMID 33649991)
- **Nivel de lectura:** 2 (metodo) — se lee por el procedimiento geometrico, que es lo unico reimplementable
- **Leido a fondo por la autora:** no
- **PDF:** papers/mclaren2021corridor.pdf

> **Nota de citacion:** el PDF **no imprime numeros de pagina de revista** (los pies dicen
> solo "Springer" / "1 3"). Todas las referencias de abajo usan **seccion + pagina del PDF
> (1 a 8)**. El rango 1485-1492 viene de los metadatos, no de una marca visible en el PDF.
> Mapear PDF p.N -> pagina de revista seria inferencia: **NO ENCONTRADO EN EL PDF**.

## Que hace (3 lineas maximo)

Estudio anatomico retrospectivo sobre 433 CTs pelvicas naive de una sola institucion: mapea
digitalmente los contornos corticales de S1 y S2, ajusta una trayectoria recta que cruza ambas
articulaciones SI y la ensancha hasta romper cortical, obteniendo Dmax por segmento.
Con Dmax convierte el margen sobrante en **tolerancia angular** por trigonometria, y reporta que
fraccion de pelvis alcanza el umbral de zona segura (Dmax >= 10 mm) en S1, S2, ambos o ninguno.

## Restriccion o supuesto clave

No es un paper de sintesis generativa; el bloque de supuestos que limita su uso en el muestreador es otro.

1. **La zona segura es un escalar, no una region.** Toda la geometria colapsa en un solo numero por
   segmento: "This geometrically defned the position, alignment and maximum diameter (Dmax) of the
   largest path" (Material and methods, PDF p. 2). Posicion y alineacion se dicen determinadas, pero
   **sus valores no se reportan**: no hay coordenadas, ni angulos de entrada, ni landmarks en el marco
   del CT.
2. **La trayectoria es una recta unica y maximal, no una distribucion.** Se busca el camino mas grande,
   no se muestrea el espacio de poses viables ni las malposiciones. El paper mide capacidad anatomica,
   no comportamiento clinico.
3. **El umbral de 10 mm es heredado, no medido aqui.** "Reported between 8 and 12 mm, the minimal
   corridor for safely placing a transiliosacral screw has not yet been established" y "Kaiser et al.
   recommended 10 mm or greater" (Introduccion, PDF p. 2). Es decir: **el paper adopta 10 mm de la
   literatura y lo declara no establecido**.
4. **La tolerancia angular no es una restriccion del volumen CT: mezcla anatomia con tecnica
   percutanea.** El brazo largo del triangulo es la distancia piel-cuerpo sacro, "estimated to be
   150 mm", y el ancho util es Dmax menos un diametro de tornillo de 7 mm (Material and methods,
   PDF p. 3). Si el punto de partida fuera la cortical iliaca contralateral en vez de la piel, la
   tolerancia **subiria**; los autores lo admiten (Discusion, PDF p. 5).
5. **El modelo no incluye periostio:** "The technique does not account for periosteal thickness"
   (Material and methods, PDF p. 2).

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Zona segura = Dmax >= 10 mm, mismo umbral para S1 y S2 | "Dmax of≥10 mm was defned as the target amount of available space" | Material and methods, PDF p. 2 |
| Tolerancia angular transiliosacra S1 = 1.53 ± 0.57 grados | "was found to be 1.53±0.57 degrees and 1.02±0.33 degrees" | Results, PDF p. 4 |
| Tolerancia angular transiliosacra S2 = 1.02 ± 0.33 grados (Resultados) | "1.53±0.57 degrees and 1.02±0.33 degrees for S1 and S2" | Results, PDF p. 4 |
| Diametro de tornillo asumido = 7 mm | "7 mm (screw diameter) was subtracted from the Dmax value" | Material and methods, PDF p. 3 |
| Distancia piel-cuerpo sacro = 150 mm (estimada, tomada de Templeman) | "The distance from the skin to the sacral body (estimated to be 150 mm)" | Material and methods, PDF p. 3 |
| 68.9% de corredores S1 con zona segura | "68.9% of S1 corridors and 81.1% of S2 corridors had a safe zone" | Results, PDF p. 4 |
| 81.1% de corredores S2 con zona segura | "68.9% of S1 corridors and 81.1% of S2 corridors had a safe zone" | Results, PDF p. 4 |
| 48.3% con zona segura en ambos corredores | "48.3% of the pelves had an osseous corridor that can safely tolerate" | Results, PDF p. 4 |
| 5.1% sin zona segura en ninguno | "while 5.1% were below this 10 mm threshold in both corridors" | Results, PDF p. 4 |
| Sensibilidad: -0.45 grados por cada -5 mm de diametro, desde 20 mm | "a decrease in corridor diameter of every 5 mm results in 0.45 degree decrease" | Results, PDF p. 4 |
| Tolerancia iliosacra simple (CITADA de Templeman) = 4.2 grados | "percutaneous placement of an SI screw has an angular tolerance of 4.2 degrees" | Discusion, PDF p. 5 |
| 17 mm de corredor para dos tornillos; solo 19.2% lo alcanza en S1 | "Only one ffth (19.2%) of sacra measured in our study had adequate space" | Discusion, PDF p. 6 |
| Poblacion: 433 CTs; S2 en 433, S1 en 352 | "of the S1 segment in 352 scans and of the S2 segment in 433 scans" | Material and methods, PDF p. 2 |

## Donde entra en mi tesis

**Objetivo 2 (muestreador de colocacion quirurgicamente restringido), definicion de zona segura
sacroiliaca.** Es la fuente que `ramadanov2025safezone` no pudo ser: aqui SI hay umbral numerico
(Dmax >= 10 mm), SI hay procedimiento geometrico reproducible sobre CT 3D (malla de contornos
corticales + recta expandida hasta romper cortical), y SI hay una tolerancia angular con dispersion
que puede usarse como **escala de perturbacion de pose** en el muestreador.

Dos usos concretos y separados:

- **Restriccion dura del muestreador:** el corredor transiliosacro se puede modelar como cilindro
  recto de diametro <= Dmax que va de tabla externa iliaca a tabla externa iliaca contralateral. Dmax
  se obtiene por el mismo algoritmo (expandir hasta contacto cortical en >= 3 puntos).
- **Escala de las malposiciones a muestrear:** las tolerancias de 1.53 y 1.02 grados dan el orden de
  magnitud de la perturbacion angular que separa "intraoseo" de "brecha cortical" en el caso
  transiliosacro. **Advertencia:** ese numero incluye la distancia piel-sacro de 150 mm, que es un
  parametro quirurgico, no anatomico. Para un muestreador que opera en el volumen CT, lo que se hereda
  directamente es la **geometria de Dmax**; la tolerancia angular hay que recalcularla con el brazo
  correcto o citarla declarando su supuesto.

**Distincion que la tesis debe mantener (y que este paper hace explicita):** *transiliosacro* atraviesa
AMBAS articulaciones SI y sale por la tabla externa contralateral; *iliosacro simple* no. Todas las
mediciones propias del paper son transiliosacras. El 4 / 4.2 grados de tolerancia iliosacra es **cita
de Templeman et al. [10]**, no medicion de McLaren.

Uso secundario para **BFC**: el criterio de rotura es contacto cortical en >= 3 localizaciones
(Material and methods, PDF p. 2). Es un criterio binario de contencion, no una escala graduada en mm:
no reemplaza la escala 0/<2/2-4/>4 mm de `smith2006iliosacral`.

## Dudas para el asesor

1. La tolerancia angular de McLaren mide dificultad **quirurgica percutanea** (brazo de 150 mm desde
   la piel), no margen anatomico puro. Para el muestreador conviene (a) citarla tal cual declarando el
   supuesto, o (b) recalcular la tolerancia con el brazo cortical-a-cortical, que los propios autores
   sugieren como trabajo futuro?
2. El umbral de 10 mm no es de este paper: lo toma de Kaiser et al. y dice explicitamente que el
   corredor minimo "has not yet been established" (rango citado 8-12 mm). Si la tesis usa 10 mm como
   restriccion, hay que citar a Kaiser, o basta declarar el rango 8-12 mm como incertidumbre?
3. **Inconsistencia interna del paper.** Results dice a la vez "48.3% of the pelves had an osseous
   corridor ... in both corridors" y "A total of 352 (81.3%) pelves had both S1 and S2 corridors
   Dmax≥10 mm" (Results, PDF p. 4). Las dos frases afirman lo mismo con cifras distintas (209 vs 352),
   y 352 coincide con el n de escaneos S1. Se cita solo 48.3% (que es el que repite la Discusion) y se
   ignora la segunda frase, o se registra la discrepancia?
4. El 31.1% del abstract y el 31% del cuerpo no describen lo mismo: el abstract dice "patients not
   having a viable corridor for screw passage" (sin segmento), el cuerpo dice "31% of the pelves
   studied did not have a safe 10-mm **S1** corridor". Es el complemento de 68.9%, o sea **solo S1**.
   El "sin corredor viable en absoluto" es 5.1%. Cual se cita?

## Evidencia textual

Todas las frases estan copiadas del PDF tal como aparecen (incluidas sus erratas de ligadura tipo
"defned", "fxation", "signifcant"). Ninguna cifra se completo con conocimiento externo.

### A. Definicion de zona segura y de Dmax

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Umbral de zona segura, definicion operativa | "Dmax of≥10 mm was defned as the target amount of available space" | Material and methods, PDF p. 2 |
| Umbral en el abstract, mismo valor | "had a safe zone (corridor diameter≥10 mm) for transiliosacral placement" | Abstract, Results, PDF p. 1 |
| Umbral aplicado por igual a S1 y S2 | "68.9% of S1 corridors and 81.1% of S2 corridors had a safe zone" | Results, PDF p. 4 |
| Umbral repetido como "10 mm threshold" para ambos | "were below this 10 mm threshold in both corridors" | Results, PDF p. 4 |
| El umbral es heredado, no medido aqui | "Kaiser et al. recommended 10 mm or greater" | Introduccion, PDF p. 2 |
| El minimo NO esta establecido en la literatura | "the minimal corridor for safely placing a transiliosacral screw has not yet been established" | Introduccion, PDF p. 2 |
| Rango de valores previos del corredor minimo | "Reported between 8 and 12 mm" | Introduccion, PDF p. 2 |
| Umbral atribuido tambien en la discusion | "which has previously been defned as 10 mm" | Discusion, PDF p. 4 |
| Umbral distinto para S1 vs S2 | NO ENCONTRADO EN EL PDF (es el mismo 10 mm en ambos) | — |

### B. Procedimiento geometrico (mapeo cortical, trayectoria, expansion)

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Metodo de extraccion de contorno, no propio | "utilizing the 3D methodology for automatic bone contour extraction previously described by Gottschling" | Material and methods, PDF p. 2 |
| Que se construye a partir de la CT | "A highly detailed 3D voxel density mesh of the cortical contours" | Material and methods, PDF p. 2 |
| Que identifica la malla | "was developed for all scans identifying the cortical limits" | Material and methods, PDF p. 2 |
| Limitacion del modelo cortical | "The technique does not account for periosteal thickness" | Material and methods, PDF p. 2 |
| Forma de la trayectoria | "A straight-line path was digitally placed within the cortical contours" | Material and methods, PDF p. 2 |
| Extension del trayecto (definicion de TRANSILIOSACRO) | "extended from the outer table of one posterior ilium, across the near SI joint" | Material and methods, PDF p. 2 |
| Salida contralateral del trayecto | "across the contralateral SI joint, and out the outer table of the opposite ilium" | Material and methods, PDF p. 2 |
| Regla de expansion hasta rotura | "The diameter of the path was increased until it contacted and breached the thickness of the cortex" | Material and methods, PDF p. 2 |
| Criterio de parada, numero de contactos | "in at least three locations" | Material and methods, PDF p. 2 |
| Que queda definido geometricamente | "This geometrically defned the position, alignment and maximum diameter (Dmax) of the largest path" | Material and methods, PDF p. 2 |
| Version resumida en el abstract | "A straight-line path was placed within each osseous corridor and extended across both SI joints" | Abstract, Materials and methods, PDF p. 1 |
| Valores numericos de esa "position" y "alignment" | NO ENCONTRADO EN EL PDF | — |
| Sistema de coordenadas o marco de referencia del CT | NO ENCONTRADO EN EL PDF | — |
| Definicion algoritmica de "breached the thickness of the cortex" (en HU o en mm) | NO ENCONTRADO EN EL PDF | — |
| Codigo, software o datos publicados | NO ENCONTRADO EN EL PDF | — |

### C. Tolerancia angular: procedimiento de calculo

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Metodo prestado, no propio | "Using the trigonometric analytical methods described by Templeman et al." | Material and methods, PDF p. 3 |
| Se calcula solo sobre corredores que llegan a 10 mm | "the angular tolerance was calculated for placing a transiliosacral screw in osseous corridors that had a 10-mm corridor" | Material and methods, PDF p. 3 |
| Paso 1: restar diametro de tornillo | "7 mm (screw diameter) was subtracted from the Dmax value" | Material and methods, PDF p. 3 |
| Paso 2: partir a la mitad | "this value was then divided in half to create the short edges of two right triangles" | Material and methods, PDF p. 3 |
| Paso 3: brazo largo del triangulo (la "average distance" del abstract) | "The distance from the skin to the sacral body (estimated to be 150 mm)" | Material and methods, PDF p. 3 |
| Paso 4: funcion usada | "The inverse tangent function was used to calculate the angle between the long edge and hypotenuse" | Material and methods, PDF p. 3 |
| Paso 5: duplicar | "this angle was multiplied by two to determine the angular tolerance" | Material and methods, PDF p. 3 |
| Descripcion del abstract del mismo calculo | "trigonometric analysis of the Dmax value of the corridor" | Abstract, Materials and methods, PDF p. 1 |
| **Ecuacion escrita en notacion matematica** | NO ENCONTRADO EN EL PDF (el procedimiento esta solo en prosa; los 5 pasos de arriba son la unica forma en que aparece) | Material and methods, PDF p. 3 |
| Origen del valor de 150 mm (medido vs asumido) | "(estimated to be 150 mm) [10]" — estimado y atribuido a la referencia 10 | Material and methods, PDF p. 3 |
| Justificacion de usar la piel como origen | "The percutaneous technique requires insertion through the soft tissue" | Material and methods, PDF p. 3 |
| Valor ilustrado en la figura, tornillo iliosacro | "4.2° =" (Fig. 3a) | Figura 3, PDF p. 3 |
| Valor ilustrado en la figura, transiliosacro S1 | "1.5° =" (Fig. 3b) | Figura 3, PDF p. 3 |

### D. Tolerancias angulares reportadas (y la discrepancia 1.02 / 1.03)

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| S1 y S2, **abstract-Resultados**: 1.53 y **1.02** | "was 1.53±0.57 degrees and 1.02±0.33 degrees, respectively" | Abstract, Results, PDF p. 1 |
| S1 y S2, **abstract-Discusion**: 1.53 y **1.03**, sin desviacion | "the angular tolerance of 1.53 and 1.03 degrees for the S1 and S2 segments" | Abstract, Discussion, PDF p. 1 |
| S1 y S2, **cuerpo-Resultados**: 1.53 ± 0.57 y **1.02** ± 0.33 | "found to be 1.53±0.57 degrees and 1.02±0.33 degrees for S1 and S2" | Results, PDF p. 4 |
| S1 y S2, **cuerpo-Discusion primer parrafo**: **1.02** ± 0.33 | "was found to be 1.53 ±0.57 degrees and 1.02±0.33 degrees, respectively" | Discusion, PDF p. 4 |
| S1 y S2, **cuerpo-Discusion segundo bloque**: **1.03** ± 0.33 | "reduced the angular tolerance to 1.53±0.57 and 1.03±0.33 degrees" | Discusion, PDF p. 5 |
| Veredicto de la discrepancia | El paper usa **1.02** en las dos secciones de Resultados y **1.03** en las dos de Discusion; misma desviacion 0.33 en ambos. No se explica la diferencia | Comparacion PDF pp. 1, 4, 5 |
| Correlacion tolerancia-diametro | "tightly correlated (r2=0.91; p=0.02)" | Results, PDF p. 4 |
| Sensibilidad lineal declarada | "Starting at 20 mm, a decrease in corridor diameter of every 5 mm results in 0.45 degree" | Results, PDF p. 4 |
| Tolerancia para un SEGUNDO tornillo transiliosacro | "The angular tolerance for placing a second transiliosacral screw ... is 0.93±0.31 degrees" | Discusion, PDF p. 6 |
| Diferencia S2 en subgrupo, no significativa | "averaging a greater S2 angular tolerance of 0.11±0.18 degrees ... (p=0.83)" | Results, PDF p. 4 |
| Umbral de perforacion por cambio de trayectoria (CITADO) | "a change in trajectory of as little as 4° may result in cortical perforation" | Introduccion, PDF p. 2 |
| Tolerancia iliosacra simple previa (CITADA) | "The angular tolerance for iliosacral fxation in a safe osseous corridor has previously been reported to be 4 degrees" | Introduccion, PDF p. 2 |
| Tolerancia iliosacra simple, valor con decimal (CITADA) | "percutaneous placement of an SI screw has an angular tolerance of 4.2 degrees" | Discusion, PDF p. 5 |
| Conclusion sobre la magnitud | "A change in trajectory of less than one degree can result in cortical perforation" | Conclusion, PDF p. 6 |
| Tolerancia iliosacra simple medida por ESTOS autores | NO ENCONTRADO EN EL PDF (el 4 / 4.2 es cita de Templeman, ref. 10) | — |

### E. Porcentajes de zona segura

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| S1 con zona segura: 68.9% (abstract) | "68.9% of S1 corridors and 81.1% of S2 corridors had a safe zone" | Abstract, Results, PDF p. 1 |
| S1 y S2 con zona segura (cuerpo, Resultados) | "In total, 68.9% of S1 corridors and 81.1% of S2 corridors had a safe zone" | Results, PDF p. 4 |
| S1 y S2 con zona segura (cuerpo, Discusion) | "68.9% of S1 corridors and 81.1% of S2 corridors had a safe zone" | Discusion, PDF p. 4 |
| Ambos corredores seguros: 48.3% (abstract) | "48.3% of the pelves had a safe zone for both corridors" | Abstract, Results, PDF p. 1 |
| Ambos corredores seguros: 48.3%, n = 209 | "Of the 209 (48.3%) imaged pelves that had a Dmax≥10 mm for both S1 and S2" | Results, PDF p. 4 |
| Ninguno seguro: 5.1% (abstract) | "while 5.1% had no safe zones" | Abstract, Results, PDF p. 1 |
| Ninguno seguro: 5.1% (cuerpo) | "while 5.1% were below this 10 mm threshold in both corridors" | Results, PDF p. 4 |
| Sin corredor viable: 31.1%, **solo en el abstract** | "approximately 31.1% of patients not having a viable corridor for screw passage" | Abstract, Discussion, PDF p. 1 |
| En el cuerpo la cifra es 31% y es **especifica de S1** | "31% of the pelves studied did not have a safe 10-mm S1 corridor" | Discusion, PDF p. 6 |
| Comparacion con literatura previa | "upward of 90% of patients have at least one safe corridor (68 vs 81% in our study)" | Discusion, PDF p. 6 |
| Subgrupo con S1 mayor que S2 | "171 (81.8%) had a larger S1 corridor with 168 (80.4%) having a larger angular tolerance" | Results, PDF p. 4 |
| Acuerdo entre "corredor mayor" y "tolerancia mayor" | "an agreement of 98.2%" | Results, PDF p. 4 |
| **Frase inconsistente con el 48.3%** | "A total of 352 (81.3%) pelves had both S1 and S2 corridors Dmax≥10 mm" | Results, PDF p. 4 |
| Corredor para dos tornillos | "We estimated a 17-mm osseous corridor would be needed to place two transiliosacral screws" | Discusion, PDF p. 6 |
| Fraccion que admite dos tornillos en S1 | "Only one ffth (19.2%) of sacra measured in our study had adequate space" | Discusion, PDF p. 6 |

### F. Sexo, edad, BMI

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Sexo en S1 (abstract) | "Females had a less frequent Dmax ≥ 10 mm at S1, 52% vs 67% (p=0.001)" | Abstract, Results, PDF p. 1 |
| Sexo en S2 (abstract) | "and at S2, 64% vs 86% (p<0.001)" | Abstract, Results, PDF p. 1 |
| Sexo en S1 y S2 (cuerpo) | "Fewer females had Dmax≥10 mm than males at S1, 52% vs 67% (p=0.001)" | Results, PDF p. 4 |
| Edad NO significativa en S1 | "Age was a not signifcant factor ... S1, 62.5±17.3 vs 62.8±16.0 (p=0.88)" | Results, PDF p. 4 |
| Edad NO significativa en S2 | "S2 segments, 62.4±16.4 vs 63.4±18.5 (p=0.68)" | Results, PDF p. 4 |
| BMI NO significativo en S1 | "BMI was also not a signifcant factor ... S1, 26.9±4.6 vs 26.9±5.7 (p=0.99)" | Results, PDF p. 4 |
| BMI NO significativo en S2 | "nor S2 segments, 26.9±4.8 vs 26.9±5.6 (p=0.97)" | Results, PDF p. 4 |
| Modelo estadistico y alfa | "using binomial logistic regression with α<0.05" | Material and methods, PDF p. 2 |
| Variables evaluadas como predictores | "Gender, age, and BMI were evaluated as independent predictors" | Abstract, Materials and methods, PDF p. 1 |
| Diferencia previa por sexo (CITADA) | "determined female corridors at both sacral segment are smaller on average" | Introduccion, PDF p. 2 |

### G. Poblacion y datos

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| n total y tipo de CT | "433 Naïve pelvic CT scans of patients were retrospectively reviewed" | Material and methods, PDF p. 2 |
| Origen de los datos | "out of the radiology database and cross-referenced with clinical information from the electronic medical record" | Material and methods, PDF p. 2 |
| Numero de instituciones | "from one institution" | Material and methods, PDF p. 2 |
| Criterio de exclusion global | "All patients with prior history of trauma or arthroplasty were excluded" | Material and methods, PDF p. 2 |
| CTs disponibles antes de filtrar | "Available Pelvis CTs in EMR: 505" | Figura 1 (STROBE), PDF p. 2 |
| Primera exclusion | "72 Excluded: 62 Prior History of Arthroplasty, 10 Prior History of Pelvic Trauma" | Figura 1 (STROBE), PDF p. 2 |
| n analizado para S2 | "Pelvis CTs Reviewed for S2 Segment: 433" | Figura 1 (STROBE), PDF p. 2 |
| Segunda exclusion (solo S1) | "81 S1 Segment Data Compromised: 62 Incomplete Imaging, 19 Prior Implant Placement" | Figura 1 (STROBE), PDF p. 2 |
| n analizado para S1 | "Pelvis CTs Reviewed for S1 Segment: 352" | Figura 1 (STROBE), PDF p. 2 |
| Motivo de exclusion en texto | "compromised data in the SI region due to previous implant placement or incomplete imaging" | Material and methods, PDF p. 2 |
| Proporcion de mujeres | "Of the 433 included patients, 177 (40.9%) were female" | Results, PDF p. 4 |
| Edad media | "The average age of the population was 62.6 years" | Results, PDF p. 4 |
| BMI medio | "with an average BMI of 26.9" | Results, PDF p. 4 |
| Nivel de evidencia | "Level of evidence IV Level Retrospective Cohort" | Abstract, PDF p. 1 |
| Aprobacion etica | "The study was reviewed and approved by an institutional IRB committee" | Ethical approval, PDF p. 7 |
| Financiamiento | "The authors did not receive support from any organization for the submitted work" | Funding, PDF p. 6 |
| **Resolucion, espaciado de voxel o grosor de corte** | NO ENCONTRADO EN EL PDF | — |
| **Fabricante, modelo de escaner o protocolo (kVp, mAs)** | NO ENCONTRADO EN EL PDF | — |
| **Nombre del dataset o de la institucion** | NO ENCONTRADO EN EL PDF ("one institution", sin nombre) | — |
| **Rango de fechas de adquisicion** | NO ENCONTRADO EN EL PDF | — |
| Distribucion completa de Dmax (valores) | Solo grafico: "Histogram of maximum diameter (Dmax) vs number of patients for S1 and S2"; eje 1-26 mm | Figura 4, PDF p. 4 |
| **Dmax medio ± DE en mm para S1 y S2** | NO ENCONTRADO EN EL PDF (solo el histograma de Fig. 4; no hay tabla numerica) | — |

### H. Parametrizacion del corredor: lo que si esta y lo que no

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Limites anatomicos superior e inferior del corredor | "bound superiorly and inferiorly by the L5 nerve root and S1 sacral nerve root" | Introduccion, PDF p. 2 |
| Limites anterior y posterior | "anteriorly by the lumbar nerve roots, and posteriorly by the spinal canal" | Introduccion, PDF p. 2 |
| Borde craneal del corredor | "the cranial border of the transiliosacral corridor described to be at the level of the iliac fossa" | Introduccion, PDF p. 2 |
| Landmarks superficiales del punto de entrada | "relies on previously described superfcial landmarks of ASIS and greater trochanter" | Material and methods, PDF p. 3 |
| Construccion geometrica del punto de entrada | "Two perpendicular lines are drawn ... dividing the exposed feld into quadrants" | Material and methods, PDF p. 3 |
| Cuadrante de la incision | "Typically, incision will be made in the postero-superior quadrant" | Material and methods, PDF p. 3 |
| Vista fluoroscopica de referencia | "A true lateral sacral radiograph is obtained lining up the iliac cortical densities and greater sciatic notches" | Material and methods, PDF p. 3 |
| Analogia del punto de inicio | "in a similar fashion to a 'perfect circle' for interlocking screws in tibial or femoral nailing" | Material and methods, PDF p. 3 |
| Profundidad de anclaje del pin | "The pin is malleted into the cortex of 2–3 mm and then advanced" | Material and methods, PDF p. 3 |
| Vistas de confirmacion de trayectoria | "Further confrmation with inlet and outlet views are obtained to ensure appropriate trajectory" | Material and methods, PDF p. 3 |
| Vista de confirmacion de longitud | "obturator-oblique view on the exiting side is obtained to confrm length of the screw" | Material and methods, PDF p. 3 |
| **Coordenadas 3D del punto de entrada o de salida** | NO ENCONTRADO EN EL PDF | — |
| **Angulos de referencia del corredor (craneocaudal, anteroposterior)** | NO ENCONTRADO EN EL PDF | — |
| **Margen minimo en mm al foramen sacro** | NO ENCONTRADO EN EL PDF | — |
| **Margen minimo en mm a la cortical** | NO ENCONTRADO EN EL PDF (el criterio es contacto/rotura, no una distancia) | — |
| **Longitud media del corredor o del tornillo en mm** | NO ENCONTRADO EN EL PDF | — |
| **Diametros de tornillo distintos de 7 mm** | NO ENCONTRADO EN EL PDF (7 mm es el unico valor usado) | — |
| **Landmarks oseos en coordenadas de imagen** | NO ENCONTRADO EN EL PDF (los landmarks citados son superficiales: ASIS, trocanter mayor) | — |

### I. Transiliosacro vs iliosacro simple (distincion explicita)

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Definicion de transiliosacro (cruza ambas SI) | "to accommodate a transiliosacral screw across both sacroiliac joints" | Abstract, Background, PDF p. 1 |
| Por que es mas dificil que el iliosacro | "longer screw path, smaller osseous corridor, and increased number of structures at risk" | Introduccion, PDF p. 2 |
| Fijacion adicional que aporta | "achieve additional fxation in the cortex of the contralateral ilium" | Introduccion, PDF p. 2 |
| Estructuras en riesgo en ambos lados | "Both the ipsilateral and contralateral neurovascular structures must be navigated" | Introduccion, PDF p. 2 |
| Hipotesis comparativa | "angular tolerance for transiliosacral screw placement would be more constrained than ... iliosacral fxation" | Abstract, Hypothesis, PDF p. 1 |
| Conclusion comparativa | "signifcantly more difcult than SI screw placement which has four degrees of angular tolerance" | Conclusion, PDF p. 6 |
| Apoyo clinico citado (73 tornillos) | "Gardner and Routt who placed 73 transiliosacral screws over a 21-month period" | Discusion, PDF p. 5 |
| Que encontraron ellos | "screw starting point and trajectory were more constrained during transiliosacral instrumentation" | Discusion, PDF p. 5 |
| Base del 4.2 grados: n de la fuente citada | "A previous study analyzing post-op CT scans from 31 patients" | Discusion, PDF p. 5 |

### J. Limitaciones declaradas por los autores

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Novedad reclamada | "this is the first paper describing the angular tolerance for percutaneous transiliosacral screw placement" | Discusion, PDF p. 5 |
| Limitacion 1: periostio | "our model did not account for the contour or thickness of the periosteum" | Discusion, PDF p. 5 |
| Efecto de esa limitacion | "may have artifcially decreased the angular tolerance by a small, but unknown margin" | Discusion, PDF p. 5 |
| Limitacion 2: sin validacion intraoperatoria | "we did not evaluate the safety of screw placement in the intraoperative setting" | Discusion, PDF p. 5 |
| Efecto de fractura real | "fracture comminution or displacement, may increase the difculty of this procedure" | Discusion, PDF p. 5 |
| Limitacion 3: eleccion del punto de partida | "An argument could be made that the start point should have been the contralateral cortex of the ilium" | Discusion, PDF p. 5 |
| Consecuencia numerica de esa eleccion | "which would have increased the angular tolerance" | Discusion, PDF p. 5 |
| Trabajo futuro que proponen | "future studies could use these fndings to analyze impacts of starting points at the ilium's cortex" | Discusion, PDF p. 5 |
| Limitacion 4: dismorfismo no identificado | "dysmorphic pelves were not specifcally identifed" | Discusion, PDF p. 5 |
| Naturaleza del dismorfismo | "sacral dysmorphism is likely a spectrum with multiple anatomic variables, making identifcation difcult" | Discusion, PDF p. 5 |
| Advertencia sobre subestimacion | "with the rate of cortical perforation likely underestimated" | Discusion, PDF p. 6 |
| Recomendacion de uso: planificacion manual | "Thorough preoperative planning is essential for addressing these factors" | Discusion, PDF p. 6 |
| Enfasis en variacion individual | "understanding an individual's anatomic variations may be more important to the operative plan" | Discusion, PDF p. 5 |
| Limitacion sobre 2D vs 3D (critica a otros metodos) | "it cannot quantify the volume of the safe corridor for a three-dimensional implant" | Discusion, PDF p. 5 |
| **Declaracion de que el metodo NO es aplicable a planificacion automatica** | NO ENCONTRADO EN EL PDF (no hay ninguna frase que lo afirme ni lo niegue) | — |
| **Validacion contra colocaciones reales (accuracy, tasa de brecha propia)** | NO ENCONTRADO EN EL PDF | — |
| **Tasa de malposicion o de brecha cortical medida por estos autores** | NO ENCONTRADO EN EL PDF | — |
| Cifras de terceros: mal-union | "Keating et al. reported mal-union in 44% of vertically unstable pelvic ring injuries" | Introduccion, PDF p. 2 |
| Cifras de terceros: zona segura en sacros dismorficos | "the S1 safe zone was 36% smaller in dysmorphic sacra" | Discusion, PDF p. 6 |
| Cifras de terceros: transsacro imposible en dismorficos | "none of the dysmorphic sacra would tolerate the screw trajectory for transsacral fxation" | Discusion, PDF p. 6 |
| Cifras de terceros: prevalencia de dismorfismo | "a prevalence of sacral dysmorphism as high as 50%" | Discusion, PDF p. 6 |
| Cifras de terceros: serie S2 | "Moed and Greer who used iliosacral screws in the S2 corridor to treat 49 patients" | Discusion, PDF p. 6 |

## Verificacion de nivel propuesto

Entro a la lista desde `_candidatos.md` como candidato **nivel 1** ("posible solucion a la
implicancia #7"). **La lectura lo sostiene, pero solo en parte, y conviene decirlo con precision.**

**1. Da una definicion OPERACIONAL de zona segura? SI, parcialmente.**
Da lo que `ramadanov2025safezone` no da: un **umbral numerico** (Dmax >= 10 mm, "Dmax of≥10 mm was
defned as the target amount of available space", Material and methods, PDF p. 2), un
**procedimiento geometrico 3D reproducible** (malla de contornos corticales -> recta de tabla externa
a tabla externa -> expansion hasta contacto cortical en >= 3 puntos, misma seccion) y una **poblacion
grande** (433 CTs). Los cuatro huecos de Ramadanov (umbral, geometria 3D, n, dispersion) quedan
cubiertos.

**2. Que NO da, y esto limita cuanto puede cerrar la implicancia #7.**
La salida es **un escalar por segmento**, no una region parametrizada. El paper dice que el metodo
determina "position, alignment and maximum diameter" pero **solo publica el diametro**: no hay
coordenadas, ni angulos de referencia, ni margen en mm al foramen o a la cortical, ni longitud de
corredor, ni Dmax medio en mm (solo el histograma de la Fig. 4). Todo eso es
**NO ENCONTRADO EN EL PDF**. Para implementar el muestreador hay que **reimplementar el algoritmo**,
no leer parametros del paper.

**3. Que exactamente es reimplementable.**
El algoritmo de Dmax, si. Es descriptible en cinco pasos, todos citados en la seccion B de arriba.
La dependencia externa es el extractor de contorno de Gottschling et al. (ref. 31), que este paper
usa pero no describe.

**4. La tolerancia angular no es una restriccion anatomica pura.**
Es una funcion de Dmax que mete dos parametros quirurgicos: 7 mm de tornillo y 150 mm de piel a sacro
(este ultimo "estimated", tomado de Templeman). Los autores admiten que con origen en la cortical
iliaca contralateral el numero seria mayor. Un muestreador que opera en el volumen CT deberia usar
**Dmax**, y tratar 1.53 / 1.02 grados como referencia clinica citable, no como su restriccion interna.

**5. Discrepancias internas que quedan registradas, no resueltas.**
(a) 1.02 en Resultados vs 1.03 en Discusion, con la misma DE de 0.33.
(b) "48.3% ... in both corridors" y "352 (81.3%) pelves had both S1 and S2 corridors Dmax≥10 mm" en el
mismo parrafo de Resultados.
(c) 31.1% en el abstract sin segmento vs 31% en el cuerpo declarado como S1.
Ninguna se explica en el PDF. Que la tesis cite una u otra es decision de la autora.

**6. Nivel que sostiene la evidencia: 1.**
Es la unica fuente disponible con umbral numerico, procedimiento 3D y n grande para la restriccion del
Objetivo 2. Si se cita mal (por ejemplo, presentando 1.53 grados como margen anatomico, o 31.1% como
"pacientes sin ningun corredor" cuando el 5.1% es esa cifra), se rompe la justificacion del muestreador
en la sustentacion. Ese es exactamente el criterio de N1 de la autora.

## Candidatos de snowballing detectados

Transcritos tal como aparecen en la lista de referencias (PDF pp. 7-8). No se busco ni se descargo
ninguno. Ya estaban en `_candidatos.md` y **no se duplican**: Templeman et al. 1996 (ref. 10 aqui) y
van den Bosch et al. 2002 (ref. 12 aqui); ver nota anadida bajo la tabla de `_candidatos.md`.

| Cita como aparece | Por que podria importar |
|---|---|
| Gottschling H, SM, Reimers N., Fischer F., Homeier A., Burgkart R. (2009) A System for Performing Automated Measurements on Large Bone Databases. WCMPBE (ref. 31) | Es **el algoritmo que McLaren usa y no describe**. Sin el, el procedimiento de Dmax no es reimplementable. Nivel 1 |
| Gras F, Gottschling H, Schroder M, et al. (2016) Transsacral osseous corridor anatomy is more amenable to screw insertion in males: a biomorphometric analysis of 280 pelves. CORR 474(10):2304-2311 (ref. 28) | Fuente de la diferencia por sexo y del software automatizado; segunda cohorte grande (280 pelvis) con medidas 3D de corredor. Nivel 1 |
| Kaiser SP, Gardner MJ, Liu J, Routt ML Jr, Morshed S (2014) Anatomic determinants of sacral dysmorphism and implications for safe iliosacral screw placement. JBJS Am 96(14):e120 (ref. 19) | **Fuente original del umbral de 10 mm** que McLaren adopta, y de un sistema de puntuacion de dismorfismo para planificacion. Nivel 1 |
| Lee JJ, Rosenbaum SL, Martusiewicz A, et al. (2015) Transsacral screw safe zone size by sacral segmentation variations. J Orthop Res 33(2):277-282 (ref. 18) | Segunda fuente que McLaren cita para "previously been defned as 10 mm". Necesaria para saber de donde sale el umbral. Nivel 1 |
| Gardner MJ, Morshed S, Nork SE, Ricci WM, Routt ML Jr (2010) Quantifcation of the upper and second sacral segment safe zones in normal and dysmorphic sacra. J Orthop Trauma 24(10):622-629 (ref. 9) | Cuantifica zona segura S1/S2 en 28 sacros normales y 22 dismorficos; fuente del "36% smaller" y del "none ... would tolerate". Define la cola anatomica que el muestreador debe cubrir. Nivel 2 |
| Wagner D, Kamer L, Sawaguchi T, et al. (2017) Critical dimensions of trans-sacral corridors assessed by 3D CT models: relevance for implant positioning in fractures of the sacrum. J Orthop Res 35(11):2577-2584 (ref. 29) | Modelo estadistico 3D de dimensiones criticas del corredor; competidor directo de la parametrizacion del muestreador y posible fuente de geometria que McLaren no publica. Nivel 2 |
| Mendel T, Noser H, Wohlrab D, Stock K, Radetzki F (2011) The lateral sacral triangle—A decision support for secure transverse sacroiliac screw insertion. Injury 42(10):1164-1170 (ref. 36) | Construccion geometrica explicita (triangulo sacro lateral) para trayectoria transversa segura; alternativa parametrizable a Dmax. Nivel 2 |
| Zhao Y, Li J, Wang D, Lian W (2012) Parameters of lengthened sacroiliac screw fxation: a radiological anatomy study. Eur Spine J 21(9):1807-1814 (ref. 37) | El titulo promete **parametros** de trayectoria iliosacra alargada, que es justo lo que falta aqui (angulos, longitudes). Nivel 2 |
| Hasenboehler EA, Stahel PF, Williams A, et al. (2011) Prevalence of sacral dysmorphia in a prospective trauma population: implications for a "safe" surgical corridor for sacro-iliac screw placement. Patient Saf Surg 5(1):8 (ref. 39) | Fuente de la prevalencia de dismorfismo (~50%) que determina que fraccion de la poblacion cae fuera del corredor estandar. Nivel 3 |
