# berk2023washer — Arandela obligatoria en tornillos iliosacros S1-S2? Estudio biomecanico

- **DOI / URL:** https://doi.org/10.3390/medicina59081379 (*Medicina* 2023, 59, 1379; 11 pp.)
- **Nivel de lectura:** 2 (metodo) — nivel propuesto por el asistente, decide la autora
- **Leido a fondo por la autora:** no
- **PDF:** papers/berk2023washer.pdf

**Profundidad:** texto completo (11 paginas, 46 referencias). Sin material suplementario en el PDF.

**Estado bibliografico:** sin entrada en `refs.bib`; existe `refs/raw/berk2023washer.nbib`. Darla de alta es decision de la autora (regla 9).

## Que hace (3 lineas maximo)

Estudio biomecanico en 24 pelvis compuestas con lesion sacroiliaca APC III simulada, que compara
fijacion S1-S2 con dos tornillos canulados de 7.3 mm **con y sin arandela**, en tres disenos de
tornillo (parcialmente roscado corto, totalmente roscado corto, totalmente roscado largo transsacro).
Mide rigidez, ciclos y carga a fallo, angulo de brecha, flexion, inclinacion del tornillo y *cutout* de
la punta bajo carga ciclica creciente con seguimiento optico. **No es un estudio de imagen.**

## Restriccion o supuesto clave

No aplica en el sentido de la plantilla (no es un paper de sintesis generativa). La restriccion
relevante para esta tesis es otra: **el paper documenta el sistema implantado solo por calibre nominal,
longitud y las dos medidas de la arandela**, y declara la geometria fina del tornillo en ningun lugar.
El modelo es de **hueso artificial**, y los autores lo marcan como su limitacion principal:
*"The obvious limitation of this investigation is the chosen artificial bone model."* (Strength &
Limitations, p. 8).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Arandela: diametro 13.0 mm | *"and washers (diameter 13.0 mm, thickness 6.6 mm)"* | Materials and Methods, Set 1, p. 2 |
| Arandela: "thickness" 6.6 mm (**ambiguo**, ver abajo) | *"and washers (diameter 13.0 mm, thickness 6.6 mm)"* | Materials and Methods, Set 1, p. 2 |
| Calibre nominal del tornillo: 7.3 mm | *"two 7.3 mm partially threaded short cannulated self-tapping screws"* | Materials and Methods, Set 1, p. 2 |
| Longitudes cortas: 90 mm (S1) y 65 mm (S2) | *"(lengths: 90 mm for S1 and 65 mm for S2)"* | Materials and Methods, Set 1, p. 2 |
| Longitudes transsacras: 175 mm (S1) y 160 mm (S2) | *"(lengths: 175 mm for S1 and 160 mm for S2)"* | Materials and Methods, Set 3, p. 3 |
| Material: acero inoxidable 316LVM | *"All screws and washers were made of stainless steel (316LVM)"* | Materials and Methods, p. 3 |
| Fabricante: DePuy Synthes | *"the same manufacturer (DePuy Synthes, Zuchwil, Switzerland) provided all implants"* | Materials and Methods, p. 3 |
| Cabeza y arandela NO perforaron la cortical | *"no penetration of the screw heads or washers into the cortices ... occurred"* | Discussion, p. 7 |

> **Aviso sobre el "thickness 6.6 mm".** El paper escribe literalmente *"washers (diameter 13.0 mm,
> thickness 6.6 mm)"* (p. 2) y **no define la magnitud, no da una figura acotada de la arandela y no
> repite el valor en ningun otro punto del PDF**. Un espesor de 6.6 mm en una arandela de 13.0 mm de
> diametro es geometricamente extrano (seria una arandela casi tan alta como la mitad de su ancho). La
> ficha registra el valor **tal como aparece** y marca la ambiguedad: el PDF **no permite decidir** si
> 6.6 mm es espesor axial o el diametro interior del agujero. Cualquier desambiguacion tendria que
> venir de la documentacion del fabricante, que no es este paper. Diametro interior de la arandela:
> **NO ENCONTRADO EN EL PDF**.

## Respuestas a las cinco preguntas del encargo

### 1. Sistema exacto y nivel

- **Fabricante:** DePuy Synthes, Zuchwil, Suiza — *"the same manufacturer (DePuy Synthes, Zuchwil,
  Switzerland) provided all implants"* (M&M, p. 3).
- **Modelo / referencia de catalogo:** **NO ENCONTRADO EN EL PDF.** El paper nunca da nombre de sistema
  ni numero de articulo; solo la descripcion funcional *"7.3 mm ... cannulated self-tapping screws"*.
- **Material:** *"All screws and washers were made of stainless steel (316LVM)"* (M&M, p. 3). **No es
  titanio.**
- **Diametro nominal:** 7.3 mm en los tres sets. La Introduccion menciona ademas el otro calibre de uso
  clinico: *"screws of 6.5 mm or 7.3 mm diameter are used together with washers [5]"* (Intro, p. 1).
- **Nivel:** iliosacro **S1 y S2 simultaneos**, dos tornillos por especimen —
  *"S1-S2 sacroiliac (SI) screw fixation"* (Abstract, p. 1) y *"First, the S1 SI screw was positioned,
  followed by the S2 SI screw."* (M&M, p. 3). El set 3 es **transsacro** (llega a la cortical
  contralateral): *"the screws ranged ... to the contralateral ilium cortex in groups TS w/ and TS w/o"*
  (M&M, p. 3).

### 2. Dimensiones del tornillo

| Magnitud | Valor en el PDF |
|---|---|
| Diametro nominal / de rosca | 7.3 mm, pero **el paper no dice que los 7.3 mm sean el diametro de la rosca**: escribe *"7.3 mm ... screws"* sin calificar la magnitud (p. 2-3) |
| Diametro de fuste | **NO ENCONTRADO EN EL PDF** |
| Diametro de nucleo | **NO ENCONTRADO EN EL PDF** |
| Longitud de rosca (tramo roscado) | **NO ENCONTRADO EN EL PDF** (solo la distincion cualitativa *"partially threaded"* / *"fully threaded"*) |
| Paso de rosca | **NO ENCONTRADO EN EL PDF** |
| Longitud total | 90 mm (S1) y 65 mm (S2) en los sets cortos; 175 mm (S1) y 160 mm (S2) en el transsacro (pp. 2-3) |
| Canulacion (diametro del agujero o de la guia) | **NO ENCONTRADO EN EL PDF.** Los tornillos se declaran *"cannulated self-tapping"* y se insertan sobre guias (*"positioned over a previously placed guidewires"*, p. 3), pero **ningun diametro de canulacion ni de guia aparece** |
| Cabeza (diametro, altura, forma) | **NO ENCONTRADO EN EL PDF.** La cabeza solo se nombra sin medida: *"the screw head eventually breaks into the cortex"* (Discussion, p. 7) y *"no penetration of the screw heads or washers into the cortices"* (p. 7) |

**Conclusion para #97:** este paper **no confirma ni refuta** que el 7.3 mm sea el diametro de la rosca
y que el fuste sea mas fino. Sencillamente **no publica fuste, nucleo ni tramo roscado**.

### 3. Dimensiones de la arandela

- **Frase exacta, unica ocurrencia por set:** *"and washers (diameter 13.0 mm, thickness 6.6 mm)"*
  (M&M, Set 1, p. 2; identica en Set 2, p. 2, y Set 3, p. 3).
- **Diametro exterior:** el paper dice *"diameter 13.0 mm"*. **No escribe "outer"**; que sea el exterior
  es interpretacion, no texto. Registrado como **13.0 mm, sin calificador en el PDF**.
- **Diametro interior:** **NO ENCONTRADO EN EL PDF.**
- **Espesor:** el paper imprime *"thickness 6.6 mm"*. **Se copia tal cual y se senala como AMBIGUO**
  (ver aviso arriba): el PDF no define la magnitud, no la ilustra y no la vuelve a mencionar.
- Contexto funcional de la arandela en el PDF, sin cifras: *"Washers are known as safeguards against
  screw intrusion as well as a technique to retain compressive force"* (Discussion, p. 8) y
  *"they are a standard component in the iliosacral screw placement recommendations from the AO"*
  (Discussion, p. 8).

### 4. Que compara y que mide; CT y artefactos

**Comparacion:** tres pares de grupos, cada par = mismo diseno de tornillo **con arandela (w/) frente a
sin arandela (w/o)**: PT (parcialmente roscado corto), FT (totalmente roscado corto), TS (totalmente
roscado largo transsacro).

**Medidas (todas biomecanicas):** rigidez del constructo (N/mm) de la rampa cuasi-estatica; y por
seguimiento optico *"gap angle"* (grados), *"flexion"* (grados), *"screw tilt ilium"* (grados) y
*"screw tip cutout"* (mm) a 1000, 2000 y 3000 ciclos; mas ciclos a fallo y carga a fallo con el criterio
*"Reaching 5° gap angle was arbitrary set as a clinically relevant failure criterion"* (Sec. 2.2, p. 5).

**Resultado principal:** *"significantly higher for the fully threaded short screws with a washer
(3972 ± 600/398.6 ± 30.0) versus its counterpart without a washer (2993 ± 527/349.7 ± 26.4), p = 0.026"*
(Abstract, p. 1). En los otros dos disenos, *"p ≥ 0.359"* (Results, p. 6).

**CT / tomografia / artefacto metalico: NO ENCONTRADO EN EL PDF.** El paper **no menciona tomografia
computarizada, HU, MAR ni artefacto metalico** en ninguna seccion. La unica imagen es radiografia de
verificacion: *"true lateral, inlet and outlet x-rays were captured to verify the positioning"*
(M&M, p. 3) y la Figura 1, *"Inlet (uppercase letters) and outlet (lower case letters) x-rays after
instrumentation"* (p. 3). Esas radiografias muestran el perfil del tornillo y la arandela, pero el
paper **no mide nada sobre ellas**.

### 5. Especimenes

- **24 pelvis compuestas (sinteticas), no cadavericas:** *"Twenty-four composite pelvises (Model 4060®,
  Synbone, Zizers, Switzerland) were used."* (Sec. 2, p. 2).
- **Lesion simulada:** *"An SI joint injury type APC III according to the Young and Burgess
  classification was simulated in all specimens"* (Sec. 2, p. 2), retirando el material de la sinfisis y
  de la articulacion SI.
- **Reparto:** seis grupos de 6 — *"Equal numbers of three right and three left pelvis sides were
  utilized in each group (n = 6)."* (M&M, p. 3).
- **Limitacion declarada por los autores sobre el modelo artificial:** *"it is ethically acceptable to
  proceed with a cadaver investigation"* (Strength & Limitations, p. 8), es decir, este es un primer
  paso en hueso sintetico.

## Relevancia para la tesis (mascara del implante, #95 y #97)

1. **Confirma que la arandela existe y es grande en un sistema iliosacro de 7.3 mm real.** 13.0 mm de
   diametro frente al calibre de 7.3 mm del tornillo: la arandela es, con diferencia, el elemento mas
   ancho del conjunto, y el paper la trata como componente estandar de la recomendacion AO
   (Discussion, p. 8). Eso **respalda cualitativamente #97** en su parte de "la arandela es mucho mas
   grande que el tornillo", que es lo que la mascara parametrica de `main.tex:113` hoy ignora.
2. **No respalda la parte central de #97.** La afirmacion de que el 7.3 mm es el diametro de la rosca y
   el fuste es de ~4.8 mm **no aparece en este PDF**: fuste, nucleo y tramo roscado son NO ENCONTRADO.
   G1 **no cierra** la verificacion; sigue haciendo falta G2 (Gardner 2015) o la documentacion del
   fabricante (T1).
3. **El "thickness 6.6 mm" no es utilizable como espesor sin verificacion externa.** La sospecha que la
   autora ya habia anotado en `_candidatos.md` (que 6.6 mm sea el **diametro interior** y no el espesor)
   **no se puede resolver con este PDF**: el texto no define la magnitud. Si se rasteriza la arandela
   con 6.6 mm de espesor axial sobre la base de esta cita, se estaria fijando un parametro que el paper
   no sustenta. Rasterizar el diametro de 13.0 mm si esta sustentado.
4. **Apoyo al apoyo cortical iliaco.** El paper dice que en su modelo *"no penetration of the screw
   heads or washers into the cortices of the bone model occurred in any group"* (Discussion, p. 7) y que
   un estudio comparable *"described washer penetration in the iliac bone [19]"* (Discussion, p. 7):
   la arandela **se asienta contra la cortical iliaca**, que es exactamente el gradiente alto donde
   `B_delta` deberia ver mas beam hardening. Es contexto, no medida.
5. **Material distinto del supuesto habitual.** 316LVM es **acero inoxidable**, no titanio. Si el
   renderizador o el brazo fisico asumen titanio, este paper documenta que sistemas iliosacros de acero
   estan en uso clinico; el acero atenua mas y produce mas artefacto. El paper **no mide nada de eso**
   (no hay CT), asi que es solo un aviso de supuesto, no evidencia de imagen.
6. **No aporta nada a #95 (gap de dominio entre mascara de entrenamiento y mascara de sintesis):** no
   hay imagen tomografica, umbrales ni mascaras de ningun tipo en este trabajo.

## Dudas para el asesor

1. El unico dato geometrico citable de este paper es **arandela de 13.0 mm de diametro**. El
   *"thickness 6.6 mm"* queda marcado como ambiguo. Se incorpora la arandela a la mascara parametrica
   solo con el diametro, dejando el espesor como parametro declarado sin fuente, o se espera a T1?
2. El sistema es de **acero 316LVM**. La tesis asume implicitamente titanio en alguna parte del
   renderizador o del brazo fisico? Si es asi, hace falta una decision explicita sobre el material.
3. Este paper es de **hueso sintetico y biomecanica pura, sin ninguna imagen tomografica**. Le
   corresponde N2 o N3? El asistente propone **N2** solo porque toca la geometria del implante del
   Objetivo 3; no toca ninguna metrica ni ningun baseline.

## Evidencia textual

Toda cifra, umbral, definicion y criterio que aparece en el PDF.

### Implante (lo que importa para la mascara)

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Calibre nominal 7.3 mm (PT corto) | *"two 7.3 mm partially threaded short cannulated self-tapping screws"* | M&M, Set 1, p. 2 |
| Calibre nominal 7.3 mm (FT corto) | *"two 7.3 mm fully threaded short cannulated self-tapping screws"* | M&M, Set 2, p. 2 |
| Calibre nominal 7.3 mm (TS largo) | *"two 7.3 mm fully threaded long transsacral cannulated self-tapping screws"* | M&M, Set 3, p. 3 |
| Longitud S1 corta 90 mm / S2 corta 65 mm | *"(lengths: 90 mm for S1 and 65 mm for S2)"* | M&M, Set 1, p. 2 |
| Longitud S1 transsacra 175 mm / S2 160 mm | *"(lengths: 175 mm for S1 and 160 mm for S2)"* | M&M, Set 3, p. 3 |
| Arandela, diametro 13.0 mm | *"and washers (diameter 13.0 mm, thickness 6.6 mm)"* | M&M, Set 1, p. 2 |
| Arandela, "thickness" 6.6 mm (ambiguo) | *"and washers (diameter 13.0 mm, thickness 6.6 mm)"* | M&M, Set 1, p. 2 |
| Material 316LVM | *"All screws and washers were made of stainless steel (316LVM)"* | M&M, p. 3 |
| Fabricante | *"the same manufacturer (DePuy Synthes, Zuchwil, Switzerland) provided all implants"* | M&M, p. 3 |
| Calibres clinicos citados: 6.5 o 7.3 mm | *"screws of 6.5 mm or 7.3 mm diameter are used together with washers"* | Introduction, p. 1 |
| Calibre citado de tercero: 7.3 mm parcialmente roscado con arandela | *"recommends cannulated 7.3 mm partially threaded screws with a washer"* | Discussion, p. 8 |
| Comparable con tornillos 7.3 mm totalmente roscados en S1 | *"A comparable study, using fully threaded 7.3 mm sacroiliac S1 screws"* | Discussion, p. 7 |
| Diametro de fuste | **NO ENCONTRADO EN EL PDF** | — |
| Diametro de nucleo | **NO ENCONTRADO EN EL PDF** | — |
| Longitud del tramo roscado | **NO ENCONTRADO EN EL PDF** | — |
| Paso de rosca | **NO ENCONTRADO EN EL PDF** | — |
| Diametro de canulacion / de la guia | **NO ENCONTRADO EN EL PDF** | — |
| Diametro o altura de la cabeza | **NO ENCONTRADO EN EL PDF** | — |
| Diametro interior de la arandela | **NO ENCONTRADO EN EL PDF** | — |
| Numero de catalogo o nombre del sistema | **NO ENCONTRADO EN EL PDF** | — |
| Par de apriete aplicado | **NO ENCONTRADO EN EL PDF**; declarado como limitacion: *"Missing torque data on the tightening force of the screws"* | Strength & Limitations, p. 8 |

### Diseno experimental

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| 24 pelvis compuestas | *"Twenty-four composite pelvises (Model 4060®, Synbone, Zizers, Switzerland) were used."* | Sec. 2, p. 2 |
| Lesion APC III simulada | *"An SI joint injury type APC III according to the Young and Burgess classification"* | Sec. 2, p. 2 |
| n = 6 por grupo, 3 derechas y 3 izquierdas | *"Equal numbers of three right and three left pelvis sides ... (n = 6)."* | M&M, p. 3 |
| Seis grupos (tres sets con/sin arandela) | *"Specimens were stratified into three sets of two groups each"* | M&M, p. 2 |
| Insercion perpendicular a la articulacion SI, sin perforaciones | *"perpendicular to the SI joint, entirely within the artificial bone, avoiding any perforations"* | M&M, p. 3 |
| Orden de insercion S1 luego S2 | *"First, the S1 SI screw was positioned, followed by the S2 SI screw."* | M&M, p. 3 |
| Tornillos cortos llegan a la linea media | *"The screws ranged to the midline of the sacral vertebra in groups PT w/..."* | M&M, p. 3 |
| Tornillos TS llegan a la cortical iliaca contralateral | *"and to the contralateral ilium cortex in groups TS w/ and TS w/o"* | M&M, p. 3 |
| Verificacion radiografica | *"true lateral, inlet and outlet x-rays were captured to verify the positioning"* | M&M, p. 3 |
| Figura 1: radiografias inlet/outlet | *"Inlet (uppercase letters) and outlet (lower case letters) x-rays after instrumentation"* | Fig. 1, p. 3 |
| Celda de carga 5 kN / 50 Nm | *"The system was equipped with a 5 kN/50 Nm load cell"* | Sec. 2.1, p. 3 |
| Exactitud < 1% entre 10-100% de capacidad | *"operating at less than 1% accuracy within 10–100% loading capacity"* | Sec. 2.1, p. 3 |
| Offset de carga 41 mm | *"applied to the sacrum with 41 mm anterior offset relative to the posterior-superior S1 endplate"* | Sec. 2.1, p. 4 |
| Cuatro marcadores opticos | *"Four retro-reflective marker sets were attached to the sacrum, the iliac crest and both SI screws"* | Sec. 2.1, p. 4 |
| Corte del anillo anterior | *"The anterior pelvis ring was cut by sawing the pelvic ramus at the middle"* | M&M, p. 3 |

### Definiciones de las variables medidas

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Gap angle | *"gap angle, defined as the combined angular displacement of the sacrum in coronal and horizontal plane"* | Sec. 2.2, p. 5 |
| Flexion | *"flexion, defined as the angular flexion displacement of the sacrum relative to the ilium"* | Sec. 2.2, p. 5 |
| Screw tilt ilium | *"the angular displacement of the S1 screw relative to the ilium"* | Sec. 2.2, p. 5 |
| Screw tip cutout | *"the translational displacement of the S1 screw tip relative to the sacrum"* | Sec. 2.2, p. 5 |
| Puntos de evaluacion: 1000, 2000, 3000 ciclos | *"evaluated at three time points of cyclic testing after 1000, 2000, and 3000 cycles"* | Sec. 2.2, p. 5 |
| Por que 3000 ciclos | *"the highest rounded number of cycles when none of the specimens had failed"* | Sec. 2.2, p. 5 |
| **Criterio de fallo: 5 grados de gap angle, declarado arbitrario** | *"Reaching 5° gap angle was arbitrary set as a clinically relevant failure criterion"* | Sec. 2.2, p. 5 |
| Rigidez del constructo | *"construct stiffness was evaluated from the ascending load–displacement curve of the initial quasi-static ramp"* | Sec. 2.2, p. 4 |

### Estadistica

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| SPSS v.27 | *"Statistical analysis was performed with SPSS software (v.27, IBM SPSS, Armonk, NY, USA)"* | Sec. 2.2, p. 5 |
| Normalidad: Shapiro-Wilk | *"Normality of data distribution was screened and proved with Shapiro–Wilk test."* | Sec. 2.2, p. 5 |
| Comparacion por pares: t de muestras independientes | *"were detected with Independent-Samples t-test"* | Sec. 2.2, p. 5 |
| Modelo lineal general de medidas repetidas | *"General Linear Model Repeated Measures test was conducted to identify significant differences"* | Sec. 2.2, p. 5 |
| **Umbral de significacion 0.05** | *"Level of significance was set at 0.05 for all statistical tests."* | Sec. 2.2, p. 5 |
| Correccion por multiplicidad | **NO ENCONTRADO EN EL PDF** | — |
| Calculo de tamano muestral / potencia | **NO ENCONTRADO EN EL PDF** | — |

### Resultados numericos

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Rigidez PT w/ 47.0 ± 11.1 N/mm; PT w/o 29.4 ± 7.4 | *"47.0 ± 11.1 N/mm ... in group PT w/ and 29.4 ± 7.4 N/mm in group PT w/o"* | Results, p. 5 |
| Rigidez FT w/ 33.1 ± 8.2; FT w/o 27.7 ± 9.7 | *"33.1 ± 8.2 N/mm in group FT w/ and 27.7 ± 9.7 N/mm in group FT w/o"* | Results, p. 5 |
| Rigidez TS w/ 31.9 ± 8.4; TS w/o 47.5 ± 18.7 | *"31.9 ± 8.4 N/mm in group TS w/ and 47.5 ± 18.7 N/mm in group TS w/o"* | Results, p. 5 |
| PT: arandela da mas rigidez, p = 0.012 | *"significantly higher stiffness compared to group PT w/o, p = 0.012"* | Results, p. 5 |
| Sets 2 y 3 sin diferencia de rigidez, p ≥ 0.110 | *"No significant differences were detected between the other two pairs of groups ... p ≥ 0.110"* | Results, p. 5 |
| Gap angle y screw tilt: FT w/o peor, p ≤ 0.028 | *"significantly higher values in group FT w/o compared to its paired group FT w/, p ≤ 0.028"* | Results, p. 5 |
| Flexion FT: tendencia, p = 0.083 | *"flexion trended towards higher values in group FT w/o compared to group FT w/, p = 0.083"* | Results, p. 5 |
| Resto de parametros sin diferencias, p ≥ 0.121 | *"with no further significant differences between the group pairs within each set, p ≥ 0.121"* | Results, p. 5 |
| Ciclos/carga a fallo PT w/ 5452 ± 944 / 694.3 ± 47.2 N | *"5452 ± 944/694.3 ± 47.2 N in group PT w/"* | Results, p. 6 |
| PT w/o 5016 ± 531 / 450.8 ± 26.6 N | *"5016 ± 531/450.8 ± 26.6 N in group PT w/o (set 1)"* | Results, p. 6 |
| FT w/ 3972 ± 600 / 398.6 ± 30.0 N | *"3972 ± 600/398.6 ± 30.0 N in group FT w/"* | Results, p. 6 |
| FT w/o 2993 ± 527 / 349.7 ± 26.4 N | *"2993 ± 527/349.7 ± 26.4 N in group FT w/o (set 2)"* | Results, p. 6 |
| TS w/ 3189 ± 1674 / 359.5 ± 83.7 N | *"3189 ± 1674/359.5 ± 83.7 N in group TS w/"* | Results, p. 6 |
| TS w/o 3630 ± 348 / 381.5 ± 17.4 N | *"3630 ± 348/381.5 ± 17.4 N in group TS w/o (set 3)"* | Results, p. 6 |
| FT: arandela mejora ciclos y carga, p = 0.026 | *"significantly higher ... compared to group FT w/o, p = 0.026"* | Results, p. 6 |
| Sets 1 y 3 sin diferencia, p ≥ 0.359 | *"No significant differences were detected between the other two pairs ... p ≥ 0.359"* | Results, p. 6 |
| Modo de fallo unico | *"a fracture of the ilium between the polymethylmethacrylate ilium fixation and the S2 SI screw"* | Results, p. 6 |
| p sobre ciclos, gap angle | *"≤0.038"* | Tabla 1, p. 5 |
| p sobre ciclos, flexion | *"≤0.042"* | Tabla 1, p. 6 |
| p sobre ciclos, screw tilt ilium | *"≤0.011"* | Tabla 1, p. 6 |
| p sobre ciclos, screw tip cutout | *"≥0.216 (PT w/, FT/w, TS/w)"* y *"≤0.023 (PT w/o, FT w/o, TS w/o)"* | Tabla 1, p. 6 |
| p entre grupos, gap angle | 0.751 (PT), 0.028 (FT), 0.236 (TS) | Tabla 1, p. 5 |
| p entre grupos, flexion | 0.973 (PT), 0.083 (FT), 0.132 (TS) | Tabla 1, p. 6 |
| p entre grupos, screw tilt ilium | 0.452 (PT), 0.011 (FT), 0.232 (TS) | Tabla 1, p. 6 |
| p entre grupos, screw tip cutout | 0.139 (PT), 0.121 (FT), 0.742 (TS) | Tabla 1, p. 6 |

**Tabla 1 completa, medias (DE) a 1000 / 2000 / 3000 ciclos** (Tabla 1, pp. 5-6):

| Parametro | Grupo | 1000 | 2000 | 3000 |
|---|---|---|---|---|
| Gap angle (grados) | PT w/ | 0.50 (0.39) | 0.84 (0.66) | 1.19 (0.87) |
| Gap angle | PT w/o | 0.47 (0.20) | 0.92 (0.36) | 1.45 (0.56) |
| Gap angle | FT w/ | 0.28 (0.30) | 0.74 (0.50) | 1.30 (0.65) |
| Gap angle | FT w/o | 1.31 (0.49) | 3.52 (2.04) | 6.46 (4.47) |
| Gap angle | TS w/ | 2.68 (2.33) | 3.67 (2.58) | 4.84 (2.76) |
| Gap angle | TS w/o | 1.26 (1.07) | 2.26 (1.43) | 3.23 (1.67) |
| Flexion (grados) | PT w/ | 1.09 (1.31) | 2.47 (2.27) | 3.22 (2.61) |
| Flexion | PT w/o | 0.96 (0.30) | 2.10 (0.71) | 3.81 (0.77) |
| Flexion | FT w/ | 0.87 (0.27) | 1.80 (0.58) | 2.90 (0.90) |
| Flexion | FT w/o | 3.32 (2.62) | 6.03 (5.03) | 9.91 (6.80) |
| Flexion | TS w/ | 4.47 (3.24) | 6.65 (4.13) | 10.63 (5.94) |
| Flexion | TS w/o | 2.23 (1.77) | 3.93 (2.62) | 5.62 (3.53) |
| Screw tilt ilium (grados) | PT w/ | 0.68 (0.57) | 1.38 (0.88) | 1.92 (1.02) |
| Screw tilt ilium | PT w/o | 0.71 (0.13) | 1.48 (0.27) | 2.59 (0.27) |
| Screw tilt ilium | FT w/ | 0.50 (0.23) | 1.13 (0.48) | 1.87 (0.75) |
| Screw tilt ilium | FT w/o | 2.12 (1.05) | 5.25 (2.64) | 9.34 (4.47) |
| Screw tilt ilium | TS w/ | 3.17 (2.24) | 4.73 (2.78) | 7.26 (3.87) |
| Screw tilt ilium | TS w/o | 1.88 (1.25) | 3.30 (1.82) | 4.75 (2.29) |
| Screw tip cutout (mm) | PT w/ | 0.12 (0.07) | 0.23 (0.18) | 0.28 (0.22) |
| Screw tip cutout | PT w/o | 0.09 (0.07) | 0.23 (0.15) | 0.60 (0.09) |
| Screw tip cutout | FT w/ | 0.17 (0.09) | 0.35 (0.08) | 0.37 (0.22) |
| Screw tip cutout | FT w/o | 0.54 (0.48) | 0.98 (1.02) | 1.76 (1.27) |
| Screw tip cutout | TS w/ | 0.57 (0.37) | 1.33 (0.90) | 2.96 (2.02) |
| Screw tip cutout | TS w/o | 0.89 (1.05) | 1.51 (1.29) | 1.82 (1.96) |

### Cifras citadas de terceros (no medidas aqui)

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Tasa de retirada de implante hasta 57% | *"amounting up to 57% in follow-up cohort studies [7]"* | Introduction, p. 1 |
| Complicaciones tras retirada 3-20% | *"complications following IR are common and range between 3 and 20% [12–14]"* | Introduction, p. 2 |
| Opinion experta sobre arandela | *"We routinely utilize a washer if there is fracture displacement"* | Discussion, p. 7 |

### Declaraciones cualitativas relevantes para la geometria

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Nada perforo la cortical en este modelo | *"no penetration of the screw heads or washers into the cortices ... occurred in any group"* | Discussion, p. 7 |
| En un estudio comparable si hubo penetracion iliaca de la arandela | *"described washer penetration in the iliac bone [19]"* | Discussion, p. 7 |
| Apriete a juicio del operador | *"were tightened according to the operator's best judgment"* | M&M, p. 3 |
| Funcion de la arandela | *"Washers are known as safeguards against screw intrusion"* | Discussion, p. 8 |
| La arandela es componente estandar AO | *"they are a standard component in the iliosacral screw placement recommendations from the AO"* | Discussion, p. 8 |
| Limitacion: hueso artificial | *"The obvious limitation of this investigation is the chosen artificial bone model."* | Limitations, p. 8 |
| Limitacion: sin datos de par de apriete | *"Missing torque data on the tightening force of the screws ... is another limitation"* | Limitations, p. 8 |
| La sinfisis no se fijo | *"In our test setup, the symphysis was not fixed"* | Discussion, p. 8 |

### Items buscados y ausentes

| Item | Estado |
|---|---|
| Tomografia computarizada (CT) | **NO ENCONTRADO EN EL PDF** |
| Unidades Hounsfield (HU) | **NO ENCONTRADO EN EL PDF** |
| Artefacto metalico, streaking, beam hardening, MAR | **NO ENCONTRADO EN EL PDF** |
| Titanio | **NO ENCONTRADO EN EL PDF** (el material es acero 316LVM) |
| Corredor oseo, zona segura, diametro de corredor, umbral de 10 mm | **NO ENCONTRADO EN EL PDF** |
| Tasa de malposicion o escala de brecha cortical | **NO ENCONTRADO EN EL PDF** |
| Dismorfismo sacro | **NO ENCONTRADO EN EL PDF** (se nombra solo en el titulo de la ref. [2]) |
| Angulos de trayectoria del tornillo | **NO ENCONTRADO EN EL PDF** |
| Densidad osea del modelo Synbone (g/cm3 o HU) | **NO ENCONTRADO EN EL PDF** |
| Frecuencia, amplitud y rampa del protocolo de carga ciclica | **NO ENCONTRADO EN EL PDF** (remite a su ref. [26]: *"The loading protocol was adopted identically from a previous study [26]"*, p. 4) |
| Financiamiento | *"No external funding sources were utilized"* (p. 9) |
