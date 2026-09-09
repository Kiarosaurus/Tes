# grass2016 — Anatomia del corredor oseo transsacro es mas favorable a tornillos en hombres (280 pelvis)

- **DOI / URL:** 10.1007/s11999-016-4954-5 (impreso en la cabecera del PDF y en `refs/raw/grass2016.nbib`; **no hay entrada en `refs/clean/` ni en `refs.bib` todavia**)
- **Nivel de lectura:** 1 (profunda) — candidata a fuente primaria de geometria S1/S2 en mm
- **Leido a fondo por la autora:** no
- **PDF:** papers/grass2016.pdf

**Nota de autoria:** el apellido del primer autor impreso en el paper es **"Gras"**
(Florian Gras PD Dr med), no "Grass". La clave bibtex del proyecto usa `grass2016`
por consistencia con el resto del repositorio; no se cambia en esta ficha.

## Que hace (3 lineas maximo)
Analisis biomorfometrico retrospectivo sobre 280 pelvis sanas segmentadas manualmente
desde CT, con un sistema de analisis de imagen desarrollado por TU Munchen y Stryker
Trauma GmbH, que ajusta el cilindro de mayor diametro inscrito en el corredor
transsacro oseo a nivel de S1 y de S2 en cada especimen.
Reporta diametro maximo del corredor (media, IC 95%) por nivel y por sexo, prevalencia
de dismorfismo sacro (ausencia de corredor S1) y proporcion de pelvis con corredor
igual o mayor a 9 mm segun un umbral clinico propio de los autores.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; la restriccion clave para esta tesis es de
poblacion y de definicion de "corredor viable". La cohorte excluye explicitamente
hardware/implantes: *"Pelves with fractures, pelvic ring deformity, hip dysplasia, or
hardware in situ were excluded"* (Materials and Methods, p. 2306). Ademas, el metodo
mide solo la superficie osea, sin excluir el grosor cortical: *"only bone surfaces
were segmented. This does not facilitate automatic measurement of the inner diameter
of the osseous corridors (excluding the cortical thickness)"* (Discussion, p. 2309).
Es decir, el diametro reportado es un maximo teorico sobre hueso sano, no una medida
lista para trasladar directamente a un corredor "seguro" con margen de tejido blando o
neurovascular en mm.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| S1: 12.8 mm (IC95% 12.1-13.5 mm), n=250/280 sin dismorfismo | "average of maximum cylindrical diameters of the S1 corridor ... was 12.8 mm" | Abstract, p. 2304 |
| S2: 11.6 mm (IC95% 11.3-11.9 mm), n=279/280 | "average of maximum cylindrical diameter of 11.6 mm (95% CI, 11.3–11.9 mm)" | Abstract, p. 2304 |
| S1 por sexo: mujeres 11.7 mm vs hombres 13.5 mm | "females versus males for S1: 11.7 mm ... versus 13.5 mm ... p < 0.01" | Abstract, p. 2305 |
| S2 por sexo: mujeres 10.6 mm vs hombres 12.2 mm | "for S2: 10.6 mm ... versus 12.2 mm ... p < 0.0001" | Abstract, p. 2305 |
| Umbral clinico propio: 9 mm para tornillo de 7.3 mm | "a minimum corridor diameter of at least 9 mm was defined as a cutoff for placing a 7.3-mm cortical screw" | Materials and Methods, p. 2307 |
| Viable con umbral 9 mm en S1: 191/280 (68%) | "fixation would have been possible in 191 (68%) of the pelves" | Results, p. 2307 |
| Viable con umbral 9 mm en S2: 245/280 (88%) | "fixation would have been possible in 245 (88%) of the pelves" | Results, p. 2307 |
| Sin ningun corredor >=9 mm en S1 ni S2 | "was present in 7% of males and 1% of female pelves" | Results, p. 2308 |

## Donde entra en mi tesis
Candidata a aportar las dimensiones en mm del corredor transsacro (S1 y S2, por
sexo) que `mclaren2021corridor` declara haber determinado y no publica. **Con una
salvedad de metodo que hay que resolver antes de citarla como sustituto directo**:
Gras usa un cilindro inscrito ajustado manualmente sobre una plantilla de forma
promedio con registro deformable (metodo TU Munchen / Stryker), mientras que McLaren
usa una malla de contornos corticales expandida hasta tocar la cortical en al menos
tres puntos (ver nota de McLaren en `_index.md`). **Este PDF no menciona a McLaren en
ningun punto ni afirma usar "el mismo software automatizado"**: esa afirmacion viene
del encargo, no del texto leido, y queda **NO ENCONTRADO EN EL PDF** como cita textual
de equivalencia entre ambos metodos. Antes de usar los mm de Gras como si fueran los
mm no publicados de McLaren, habria que verificar independientemente esa equivalencia
de software/algoritmo.

## Dudas para el asesor
- El umbral de 9 mm de Gras (para tornillo de 7.3 mm) es distinto del umbral de 10 mm
  que usan Kaiser/McLaren (cadena ya auditada en `_index.md`). Si se usan los mm de
  Gras para respaldar el umbral de 10 mm de McLaren, hay que decidir si se recalculan
  las proporciones viables con el corte de 10 mm que el propio Gras reporta en la
  Discusion (36% y 26% de corredores "too narrow" en S1 y S2, citando a Gardner y
  Moed) en lugar de usar el 68%/88% del corte de 9 mm.
- Falta verificar la afirmacion de "mismo software automatizado que McLaren": este PDF
  no lo confirma ni lo niega.
- La cohorte es de pelvis sanas sin hardware; no hay ninguna cifra aqui sobre
  degradacion por metal o CLINIC-metal.

## Evidencia textual

| Dato / criterio | Frase original (maximo 15 palabras) | Seccion / pagina |
|---|---|---|
| Prevalencia de dismorfismo sacro S1 (sin corredor S1) | "Thirty of 280 pelves (11%) had no transsacral S1 corridor" | Abstract, p. 2304 |
| Diametro maximo S1, cohorte sin dismorfismo (n=250) | "average of maximum cylindrical diameters of the S1 corridor ... was 12.8 mm (95% CI, 12.1–13.5 mm)" | Abstract, p. 2304 |
| Presencia de corredor S2 | "A transverse corridor for S2 was found in 279 of 280 pelves" | Abstract, p. 2304 |
| Diametro maximo S2 | "average of maximum cylindrical diameter of 11.6 mm (95% CI, 11.3–11.9 mm)" | Abstract, p. 2304 |
| Correlacion S1-S2 por sexo | "R value for females, -0.260, p<0.01; for males, -0.311, p<0.001" | Abstract, p. 2304-2305 |
| Dismorfismo por sexo | "females, 16%; males, 7%; p<0.003" | Abstract, p. 2305 |
| Diametro S1 por sexo (version Abstract) | "S1: 11.7 mm [95% CI, 10.6–12.8 mm] versus 13.5 mm [95% CI, 12.6–14.4 mm], p<0.01" | Abstract, p. 2305 |
| Diametro S1 por sexo (version Resultados; IC distinto al Abstract) | "S1: 11.7 mm [95% CI, 11.4–12.0 mm] versus 13.5 mm [95% CI, 12.6–14.4 mm], p<0.01" | Sex-specific Differences, Results, p. 2308 |
| Diametro S2 por sexo | "S2: 10.6 mm [95% CI, 10.1–11.1 mm] versus 12.2 mm [95% CI, 11.8–12.6 mm], p<0.0001" | Abstract y Results, p. 2305 / p. 2308 |
| Poblacion: n total y por sexo (Tabla 1) | "Overall (n = 280) Female (n = 116) Male(n = 164)" | Table 1, p. 2306 |
| Edad: media 63, rango 19-93 | "Range 19-93" (fila Age, Tabla 1); "Mean 63" | Table 1, p. 2306 |
| Indicaciones clinicas de la CT | "polytrauma (20%), CT angiography (70%), and other reasons (10%)" | Abstract y Methods, p. 2304 / p. 2306 |
| Criterios de exclusion (incluye hardware) | "Pelves with fractures, pelvic ring deformity, hip dysplasia, or hardware in situ were excluded" | Materials and Methods, p. 2306 |
| Segmentacion manual, un radiologo | "All segmentations were performed manually by a radiologist (GK)" | Materials and Methods, p. 2306 |
| Software / procedencia del sistema de analisis | "an advanced image analysis system developed by a team from Technische Universität München in cooperation with Stryker Trauma GmbH (Kiel, Germany)" | Materials and Methods, p. 2306 |
| Definicion del metodo: cilindro de mayor diametro sin penetrar cortical | "a fitting procedure identifies the cylinder with the greatest diameter that can be placed in the osseous corridor without penetrating the cortical regions" | Materials and Methods, p. 2306 |
| Limites corticales considerados (cualitativos, sin mm) | "at the superior and anterior sacral surface, neuroforamen wall, or spinal canal" | Materials and Methods, p. 2306 |
| Proyeccion ortogonal para generar imagenes de componente | "the sample meshes are projected along the axis to generate component images for each corridor" | Materials and Methods, p. 2306 |
| Ajuste angular del eje (alpha, beta), sin valores numericos reportados | "the axes can be tilted for each corridor separately by two angles (alpha, beta)" | Materials and Methods, p. 2307 |
| Umbral clinico propio de 9 mm y su justificacion (screw + tolerancia) | "a minimum corridor diameter of at least 9 mm was defined as a cutoff for placing a 7.3-mm cortical screw to get a tolerance of accuracy of 1 mm on each side" | Materials and Methods, p. 2307 |
| Origen del criterio de dismorfismo (ausencia de corredor, no un umbral en mm) | "such pelves were defined as having sacral dysmorphism" | Materials and Methods, p. 2307 |
| Umbral 9 mm, viabilidad S1 | "fixation would have been possible in 191 (68%) of the pelves" | Results, p. 2307 |
| Umbral 9 mm, viabilidad S2 | "fixation would have been possible in 245 (88%) of the pelves" | Results, p. 2307 |
| Dismorfismo por sexo, cuerpo del texto | "found in 19 of 116 (16%) female pelves and 11 of 164 (7%) male pelves" | Results, p. 2308 |
| Viabilidad S1 por sexo con umbral 9 mm | "67 of 116 (58%) female and 126 of 164 (77%) male pelves theoretically would have been placed safely at the S1 level" | Results, p. 2308 |
| Viabilidad S2 por sexo con umbral 9 mm | "97 of 116 (84%) female and 154 of 164 (94%) male pelves would have been placed safely at the S2 level" | Results, p. 2308 |
| Sin ningun corredor viable (S1 o S2) por sexo | "was present in 7% of males and 1% of female pelves" | Results, p. 2308 |
| Umbral alternativo de 10 mm citado de Gardner y Moed (no es medida propia) | "Using the largest 10-mm diameter cutoff, as reported by Gardner et al. [8] and Moed and Geer [24] ... too narrow in 36% and 26%" | Discussion, p. 2309 |
| Comparacion 9 mm vs 10 mm en S1/S2 (propia) | "compared with 32% and 12% when using the 9-mm cutoff" | Discussion, p. 2309 |
| Diametros propios resumidos como media ± (sin etiqueta explicita de DE) | "Measured cylindrical diameters in our study (S1, 13 ± 0.3 mm; S2, 12 ± 2 mm)" | Discussion, p. 2309 |
| Comparacion con Lee et al. (cita externa, no medicion propia) | "similar to those reported by Lee et al. [19] (S1: 14 ± 4 mm; S2 11 ± 3 mm)" | Discussion, p. 2309 |
| Comparacion con Vanderschot et al. (cita externa, no medicion propia) | "larger than those reported by Vanderschot et al. [37]. (S1, 8 ± 0.9 mm; S2, 7 ± 3 mm)" | Discussion, p. 2309 |
| Umbral de dismorfismo de Mendel (cita externa: triangulo 1.5, corredor <7.3 mm) | "A triangle ratio of 1.5 ... represents the boundary ratio for the prevalence of sacral dysmorphism, defined as transsacral corridors with a diameter less than 7.3 mm" | Discussion, p. 2309 |
| Recomendacion clinica de medicion 2D (bordes cualitativos, sin margen en mm) | "the maximum corridor width (anterior border: S1 foramen or iliac wing; posterior border: spinal canal) must be determined" | Discussion, p. 2310 |
| Recomendacion clinica de medicion 2D, plano coronal (bordes cualitativos) | "the corridor height (cranial border: surface of the alar pedicle; caudal border: S1 neuroforamen) must be measured" | Discussion, p. 2310 |
| Limitacion: solo hueso segmentado, sin descontar cortical | "only bone surfaces were segmented. This does not facilitate automatic measurement of the inner diameter" | Discussion, p. 2309 |
| Limitacion: cohorte no necesariamente representa fracturas | "not necessarily representing the cohort group of patients with pelvic ring fractures" | Discussion, p. 2309 |
| Rango de edad de la cohorte (limitacion, cita repetida) | "a wide age range (19-93 years) were analyzed" | Discussion, p. 2309 |
| Rango numerico explicito del diametro (min-max, no solo IC95%) | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Desviacion estandar (DE) formalmente etiquetada de los diametros por nivel/sexo | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Longitud del corredor transsacro en mm | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Angulo de trayectoria en grados respecto a un plano o landmark (valor numerico reportado como resultado) | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Coordenadas 3D del punto de entrada o del punto mapeado | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Margen numerico (mm) entre el corredor y el foramen sacro | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Resolucion / grosor de corte de la CT (mm) | **NO ENCONTRADO EN EL PDF** | Texto completo |
| kVp, mAs u otro parametro de adquisicion de la CT | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Nombre propio del software (mas alla de "advanced image analysis system") | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Procedencia geografica de los pacientes (mas alla de las dos instituciones) | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Frase "upward of 90% at least one safe corridor" o equivalente textual | **NO ENCONTRADO EN EL PDF** | Texto completo |
| Mencion explicita a McLaren o a "mismo software automatizado" | **NO ENCONTRADO EN EL PDF** | Texto completo |
