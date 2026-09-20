# cassanego2026evolution — Artefacto de tornillos canulados vs macizos de titanio (condilo humeral canino)

- **DOI / URL:** 10.1016/j.tvjl.2026.106691 — The Veterinary Journal 317 (2026) 106691
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/cassanego2026evolution.pdf

Profundidad: texto completo (7 pp. numeradas 1-7, articulo 106691, acceso abierto CC BY). Coincide
con `refs/raw/cassanego2026evolution.bib` (clave del editor `CASSANEGO2026106691`). Sin suplementario.

## Que hace (3 lineas maximo)
Inserta un tornillo transcondilar de titanio en cada uno de 6 miembros toracicos caninos cadavericos
y compara, en MRI de 0.25 T y en CT, el artefacto de 3 tornillos macizos frente a 3 canulados de
tres fabricantes distintos. Califica el artefacto cualitativamente y lo mide en mm en dos planos.

## Restriccion o supuesto clave
No es sintesis generativa. El supuesto que lo limita para esta tesis es metodologico: **todo el
estudio es de titanio** (*"To minimize these effects, titanium screws were used in this study"*,
Discusion, p. 4). El contraste titanio vs acero **no se mide aqui**: solo se cita de terceros
(*"they produce fewer artifacts compared to 316 L stainless steel screws"*, Discusion, p. 4, refs.
Disegi 1992 y Feuerriegel & Sutter 2024). Y el propio paper admite que **la composicion real de los
tornillos se desconoce**: *"The manufacturers did not disclose the precise composition of each
screw."* (M&M, p. 2), lo que deja la atribucion de las diferencias a variaciones de hierro como
conjetura declarada (*"may be due to variations in iron content"*, Discusion, p. 5).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| CT, macizo (frontal/superior, mm): 3.4/3.1, 3.1/3.1, 3.8/3.9 | *"Group 1: solid screw 3.4 3.1"* | Tabla 3, p. 7 |
| CT, canulado (frontal/superior, mm): 4.2/4.2, 4.1/4.0, 3.6/3.1 | *"Group 1: cannulated screw 4.2 4.2"* | Tabla 3, p. 7 |
| Protocolo CT: 120 kVp, 100 mA, 0.6 s, cortes de 0.5 mm | *"extremity helical protocol at 120 kVp, 100 mA, and 0.6 s rotation time"* | M&M, CT, p. 2 |
| Contradiccion cualitativo/cuantitativo en canulado vs macizo | *"artifact values were actually higher for the cannulated screws than for the solid"* | Discusion, p. 4 |
| Composicion de los tornillos desconocida | *"The manufacturers did not disclose the precise composition of each screw."* | M&M, p. 2 |
| Limitacion declarada de la medicion | *"measurements were taken from only one region of interest of the screw"* | Discusion, p. 5 |

## Donde entra en mi tesis
**Implicancia #57 (extension espacial del artefacto en mm).** Publica una medida en mm del artefacto
en CT alrededor de un tornillo (3.1-4.2 mm), pero **no sirve para anclar `B_delta`**:

1. **No declara el punto de referencia de la medida.** El PDF solo dice que sigue el metodo de
   `radzi2014metalartifacts` (*"following previously described methods (Radzi et al., 2014)"*,
   M&M, p. 3), donde la referencia es el **eje central** del tornillo. Aqui esa definicion **no se
   repite**: si es desde el eje o desde la superficie es NO ENCONTRADO EN EL PDF. Sin eso, los
   3.1-4.2 mm no son interpretables como banda peri-implante.
2. **No hay umbral en HU ni ROI definida en atenuacion.** La segmentacion es en 3D Slicer y la
   medicion en Blender, sin valor de umbral (NO ENCONTRADO EN EL PDF). La ROI es geometrica
   (*"the middle third of each screw"*, M&M, p. 3) y ademas sesgada al maximo
   (*"focusing on the areas with the highest artifact values"*, M&M, p. 3).
3. **Especie y anatomia.** Perro, condilo humeral, tornillos de 3.0-3.5 mm. Pelvis, sacro,
   iliosacro y tornillo de 7.3 mm: NO ENCONTRADO EN EL PDF.

Aun asi deja dos cosas utiles y verificables para el argumento:
- Confirma cualitativamente lo que `B_delta` necesita: el artefacto de CT **sale del metal** en dos
  formas simultaneas, *"mild blooming of its margins and linear streak artifacts radiating from the
  screw shaft and head"*, que se extienden *"into the surrounding trabecular bone and soft tissues"*
  (Resultados, CT, p. 3). Ningun numero acompana a esa extension: es descriptivo.
- Da otra medida del mismo tipo que Radzi con **valores mayores** (3.1-4.2 frente a 1.6-2.6 mm) pese
  a declarar el mismo metodo. Eso refuerza que la cifra depende del umbral y del punto de referencia,
  y que **#57 sigue sin una fuente operacional**.

**Mascara binaria / material.** No aporta nada al contraste titanio vs acero: es un brazo unico de
titanio. Lo que si aporta, y es incomodo para la mascara binaria, es que **entre tornillos nominalmente
del mismo material y del mismo diametro el artefacto cambia** (macizos: 3.1 a 3.9 mm segun fabricante;
la conclusion habla de *"design and material composition"*, p. 5). Si la variacion entre proveedores
de titanio ya es del orden de la medida misma, la mascara binaria de la tesis **no puede pretender
codificar aleacion**, y esa es la lectura defendible del paper.

**Canulado vs macizo.** Aqui la direccion es **opuesta a `radzi2014metalartifacts`** y ademas
**contradictoria dentro del propio paper**: el abstract afirma *"solid screws exhibited more
pronounced metallic artifacts ... compared with cannulated screws"* (p. 1) y la Discusion reconoce lo
contrario en las cifras (*"artifact values were actually higher for the cannulated screws"*, p. 4).
Sumado a que la comparacion esta confundida con **diametro** (3.0 vs 3.5 mm en G3), **largo**
(26/28/30 mm), **diseno de rosca** y **fabricante**, y a que **no hay ninguna prueba estadistica** en
todo el articulo (NO ENCONTRADO EN EL PDF: ningun valor P, ninguna DE, ningun test), la conclusion
util es negativa: **no existe hoy un efecto de canulacion transferible a la tesis**.

## Dudas para el asesor
- Este paper es la fila G6 de la ronda 2026-09-19, marcada como prioridad BAJA. Tras leerlo yo
  propongo N3 (contexto) y **no citar ninguna de sus cifras en `main.tex`**: sin estadistica y sin
  punto de referencia declarado, cualquier numero suyo es fragil. ¿Se conserva la entrada solo como
  apoyo cualitativo del blooming + streaking, o se deja fuera?
- Discrepancia de clave: `cassanego2026evolution` contiene "evolution", palabra que **no aparece en
  el titulo** del articulo ni en el raw. Si la entrada se da de alta, conviene revisar la clave.
- Discrepancia interna abstract vs Discusion sobre canulado/macizo en CT: ¿se registra como
  implicancia o basta esta ficha?

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Objetivo: dos tipos de tornillo de titanio, tres fabricantes | *"two types of titanium screws—cannulated and solid—from three different manufacturers"* | Abstract, p. 1 |
| Especie y sitio anatomico | *"implanted in the canine humeral condyle"* | Abstract, p. 1 |
| Numero de especimenes | *"Six canine forelimbs were used"* | M&M, Especimenes, p. 2 |
| Conservacion y descongelado | *"stored at –20 °C until use"*; *"thawed at room temperature for approximately 24 h"* | M&M, p. 2 |
| G1 macizo | *"Group 1 - 3.5 × 30 mm solid cortical screw"* | M&M, p. 2 |
| G1 canulado | *"3.5 × 30 mm partially threaded cannulated (cancellous) screw"* | M&M, p. 2 |
| G2 macizo y canulado | *"3.5 × 28 mm solid cortical screw; 3.5 × 26 mm fully threaded conical compression cannulated"* | M&M, p. 2 |
| G3 macizo y canulado | *"3.5 × 30 mm solid screw; 3.0 × 26 mm fully threaded conical compression cannulated"* | M&M, p. 2 |
| **Composicion del metal desconocida** | *"The manufacturers did not disclose the precise composition of each screw."* | M&M, p. 2 |
| Nombre de los fabricantes | NO ENCONTRADO EN EL PDF (solo "Group 1/2/3") | — |
| Diametro del canal interno de los canulados | NO ENCONTRADO EN EL PDF | — |
| Un solo tornillo por miembro (implantacion) | *"A drill hole was created through the midpoint of the condyle."* | M&M, p. 2 |
| Tornillos autoperforantes, sin terraja | *"Tapping was not required, as all screws were self-tapping."* | M&M, p. 2 |
| Escaner CT | *"multislice Aquilion Serve 80-channel scanner (Canon Medical Systems; Otawara, Japan)"* | M&M, CT, p. 2 |
| kVp, mA y rotacion | *"extremity helical protocol at 120 kVp, 100 mA, and 0.6 s rotation time"* | M&M, CT, p. 2 |
| Grosor e intervalo de corte | *"helical mode with 0.5 mm slice thickness and 0.5 mm interval"* | M&M, CT, p. 2 |
| Dosis: CTDIvol, DLP, SSDE | *"CTDIvol was 6.3 mGy, with a dose–length product (DLP) of 81.0 mGy·cm"*; *"SSDE of 14.9 mGy"* | M&M, CT, p. 2 |
| Filtros de reconstruccion | *"using bone and soft-tissue reconstruction filters"* | M&M, CT, p. 2 |
| Visor DICOM | *"(RadiAnt DICOM Viewer; Medixant, Poznan, Poland)"* | M&M, CT, p. 2 |
| **Algoritmo MAR del fabricante aplicado** | NO ENCONTRADO EN EL PDF (solo se cita la existencia de MAR en general) | — |
| **Diferencias de protocolo CT entre grupos** | NO ENCONTRADO EN EL PDF: se describe un unico protocolo para todos | M&M, CT, p. 2 |
| Kernel nombrado (identificador del filtro oseo) | NO ENCONTRADO EN EL PDF | — |
| Justificacion de parametros basicos | *"basic acquisition parameters were selected to ensure adequate analysis"* | Discusion, p. 4 |
| Equipo y campo de MRI | *"low-field system (Vet-MR Grande, 0.25 T; Esaote)"* | M&M, MRI, p. 2 |
| Secuencias MRI | *"Turbo 3D T1-weighted gradient-echo"*, *"SE DP/T2"*, *"STIR"*, *"fast FLAIR"* | M&M, MRI, p. 2 |
| Parametros de secuencia MRI (TR, TE, FOV, matriz) | NO ENCONTRADO EN EL PDF | — |
| **Escala cualitativa de conspicuidad (4 niveles)** | *"conspicuity (none, mild, moderate, or marked)"* | M&M, MRI, p. 2 |
| **Escala cualitativa de limitacion anatomica (4 niveles)** | *"(no, mild, moderate, or severe limitation)"* | M&M, MRI, p. 2 |
| Patrones de artefacto en MRI | *"signal void/blooming, geometric distortion of surrounding structures, or a combination"* | M&M, MRI, p. 2 |
| Tipos de artefacto calificados en CT | *"beam hardening, streak artifacts and/or blooming of the screw margins"* | M&M, CT, p. 2 |
| Region calificada en MRI | *"focused on the intracondylar portion of the screw"* | M&M, MRI, p. 2 |
| Exclusion de la cabeza del tornillo en el grado cualitativo | *"Artifacts restricted to the screw head ... were not independently graded."* | M&M, MRI, p. 2 |
| Numero de observadores, cegamiento o kappa | NO ENCONTRADO EN EL PDF | — |
| Software de segmentacion y numero de cortes | *"segmented in 3D Slicer 5.8.1 (approximately 100 slices on average)"* | M&M, Analisis cuantitativo, p. 3 |
| Software de medicion | *"rendered, and measured in Blender 4.5"* | M&M, p. 3 |
| Metodo heredado | *"following previously described methods (Radzi et al., 2014)"* | M&M, p. 3 |
| ROI de medicion | *"Measurements were taken in the middle third of each screw"* | M&M, p. 3 |
| Sesgo declarado hacia el maximo | *"focusing on the areas with the highest artifact values"* | M&M, p. 3 |
| Planos de medicion | *"in both frontal and superior planes"* | M&M, p. 3 |
| Mismo procedimiento en CT | *"The same approach was used to assess artifacts in CT images."* | M&M, p. 3 |
| **Umbral de segmentacion en HU (o cualquier unidad)** | NO ENCONTRADO EN EL PDF | — |
| **Punto de referencia de la medida (eje o superficie del tornillo)** | NO ENCONTRADO EN EL PDF | — |
| **CT, macizo: G1 3.4 / 3.1 mm** | *"Group 1: solid screw 3.4 3.1"* | Tabla 3, p. 7 |
| **CT, macizo: G2 3.1 / 3.1 mm** | *"Group 2: solid screw 3.1 3.1"* | Tabla 3, p. 7 |
| **CT, macizo: G3 3.8 / 3.9 mm** | *"Group 3: solid screw 3.8 3.9"* | Tabla 3, p. 7 |
| **CT, canulado: G1 4.2 / 4.2 mm** | *"Group 1: cannulated screw 4.2 4.2"* | Tabla 3, p. 7 |
| **CT, canulado: G2 4.1 / 4.0 mm** | *"Group 2: cannulated screw 4.1 4.0"* | Tabla 3, p. 7 |
| **CT, canulado: G3 3.6 / 3.1 mm** | *"Group 3: cannulated screw 3.6 3.1"* | Tabla 3, p. 7 |
| MRI Turbo 3D T1, macizo: 4.8/5.6, 3.9/4.6, 6.2/6.1 mm | *"Group 1: solid screw 4.8 5.6"* (y filas G2, G3) | Tabla 2, p. 5 |
| MRI Turbo 3D T1, canulado: 6.5/6.0, 6.7/7.5, 4.8/5.1 mm | *"Group 1: cannulated screw 6.5 6.0"* (y filas G2, G3) | Tabla 2, p. 5 |
| Desviaciones estandar, IC o n por medida | NO ENCONTRADO EN EL PDF (un valor por tornillo y plano) | — |
| **Prueba estadistica, valores P o nivel de significancia** | NO ENCONTRADO EN EL PDF | — |
| Grado cualitativo del artefacto CT en macizos | *"artifact conspicuity was visually graded as mild to, at most, mild–moderate"* | Resultados, CT, p. 3 |
| Grado cualitativo del artefacto CT en canulados | *"the blooming halo around the metallic core was slightly narrower"* | Resultados, CT, p. 3 |
| Mecanismos atribuidos en CT | *"consistent with beam-hardening and photon-starvation effects"* | Resultados, CT, p. 3 |
| El artefacto sale del metal (cualitativo, sin mm) | *"extending into the surrounding trabecular bone and soft tissues"* | Resultados, CT, p. 3 |
| Las estrias no aumentan con el canulado | *"Streak artifacts did not extend further into the surrounding bone"* | Resultados, CT, p. 3 |
| **Extension del streaking en mm** | NO ENCONTRADO EN EL PDF | — |
| Impacto clinico: sin limitacion | *"The humeral condyle articular surface remained fully evaluable"* | Resultados, CT, p. 3 |
| Afirmacion del abstract (macizo peor en CT) | *"solid screws exhibited more pronounced metallic artifacts ... compared with cannulated"* | Abstract, p. 1 |
| **Contradiccion en la Discusion (canulado peor en cifras)** | *"artifact values were actually higher for the cannulated screws than for the solid"* | Discusion, p. 4 |
| Resumen del abstract por grupo | *"higher for cannulated screws in G1 and G2, whereas in G3 solid screw produced greater artifact"* | Abstract, p. 1 |
| Extremos en MRI | *"the solid screw from Group 3 produced the largest artifact, while that from Group 2 ... smallest"* | Discusion, p. 4 |
| Extremos en CT | *"the cannulated screw from Group 3 exhibited the lowest artifact values"* | Discusion, p. 5 |
| **Limitacion declarada: una sola ROI** | *"measurements were taken from only one region of interest of the screw"* | Discusion, p. 5 |
| Atribucion del efecto a la geometria | *"implant geometry can significantly influence the generation of artifacts in CT imaging"* | Discusion, p. 5 |
| Titanio vs acero: solo citado, no medido | *"they produce fewer artifacts compared to 316 L stainless steel screws"* | Discusion, p. 4 |
| Composicion tipica de implantes AO (citada de Disegi 1992) | *"approximately 99.5% titanium, with small amounts of residual elements"* | Discusion, p. 5 |
| Conjetura sobre la causa de la variacion entre fabricantes | *"may be due to variations in iron content"* | Discusion, p. 5 |
| Conclusion (sin estadistica que la respalde) | *"Both design and material composition of the screw have a significant impact on image quality."* | Conclusiones, p. 5 |
| Aprobacion etica | *"(CEUA No. 000.141; August 1, 2024–2025)"* | Ethical statement, p. 5 |
| Uso declarado de IA generativa en la redaccion | *"the authors used ChatGPT to improve readability and language"* | Declaracion, p. 6 |
| Financiamiento | *"(FAPESP) (grant nº 2023/16693–7 and nº 2024/21341–5 and nº 2025/08860–6)"* | Funding, p. 7 |
| Pelvis, sacro, iliosacro o tornillo de 7.3 mm | NO ENCONTRADO EN EL PDF | — |
| Acero inoxidable medido experimentalmente | NO ENCONTRADO EN EL PDF (brazo unico de titanio) | — |
| Valores de atenuacion, HU o perfiles de intensidad | NO ENCONTRADO EN EL PDF | — |
| Fracturas presentes en los especimenes | NO ENCONTRADO EN EL PDF (condilo intacto, perforacion unica) | — |
