# mendel2011 — El triangulo sacro lateral: soporte de decision para tornillo SI transverso seguro

- **DOI / URL:** 10.1016/j.injury.2010.03.016 (respaldado por `refs/raw/mendel2011.bib`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/mendel2011.pdf

## Que hace (3 lineas maximo)
Analiza 80 CT pelvicos intactos, reconstruidos en 3D, para identificar el punto anatomico
que limita la insercion transversa segura de un tornillo sacroiliaco (SI) de 7.3 mm.
Propone el "triangulo sacro lateral" (altura BH y anchura BW del cuerpo de S1 en la
proyeccion lateral estricta) como soporte de decision preoperatorio de una sola imagen.
Define una razon umbral (ratioT = 1.5) que predice si hay hueso suficiente para al
menos un tornillo transverso.

## Restriccion o supuesto clave
Este paper no es de sintesis generativa de implantes; es un estudio anatomico/geometrico
de referencia. No aplica la pregunta sobre supuestos que impidan manejar implantes
metalicos rigidos. Sin embargo, registra una restriccion metodologica explicita relevante
para reimplementacion: el metodo solo aborda el curso estrictamente transverso de un
tornillo de 7.3 mm y no evalua trayectorias oblicuas.
> "the proposed reliable method for secure screw placement only addresses the strict
> transverse course of a 7.3 mm SI screw. Additionally, it does not allow us to evaluate
> the screw track in an oblique fashion" (Discussion, p. 1169)

Ademas, la poblacion de validacion son pelvis intactas, no fracturadas ni con implante:
> "the 80 pelves were intact, whereas in the clinical situation, this may not be the case"
> (Discussion, p. 1169)

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Boundary ratio = 1.5 (BW/BH) predice >=1 tornillo | "A boundary ratio of 1.5 represented a reliable variable to determine whether or not a screw can be inserted" | Abstract |
| Valor predictivo positivo 97%, sensibilidad 94% | "A positive predictive value of 97% and a sensitivity of 94% predict enough bone stock" | Results, p. 1166 |
| Correlacion ratioT vs PH: Pearson 0.85, p=0.0001 | "reveals a significant linear correlation to PH (p = 0.0001) with a Pearson coefficient of 0.85" | Results, p. 1166 |
| EJ<=0mm: 100% de los casos con espacio para >=1 tornillo | "With EJ ≤ 0 mm, screw insertion was possible in all cases (100%)" | Abstract |
| n=80 pelvis CT | "Overall, 80 data sets were used for further analysis" | Materials and methods, p. 1165 |
| Tornillo asumido: 7.3 mm canulado | "the dimensions of a commonly used 7.3 mm cannulated screw were assumed" | Materials and methods, p. 1165 |

## Donde entra en mi tesis
Candidata a definicion operacional geometrica y parametrizable de "pelvis apta para
tornillo transverso", alternativa a un escalar tipo Dmax (McLaren). Aporta un umbral
binario (ratioT=1.5) medido y validado estadisticamente en 80 CT, potencialmente util
para el muestreador (restriccion de contencion cortical / zona segura), aunque su
alcance queda limitado a trayectoria estrictamente transversa y a pelvis intactas.

## Dudas para el asesor
- El triangulo se define sobre una proyeccion 2D (lateral estricta) obtenida por un
  algoritmo de alineacion automatico propio de Amira, no descrito paso a paso en el
  paper: ver punto (c) de reimplementabilidad en la respuesta al encargo.
- La formula exacta de ratioT (BW/BH vs BH/BW) no se declara sin ambiguedad en el texto
  corrido; se infiere de la tabla de medias y de la frase de Discusion sobre "S1 body
  depth" vs "S1 anterior body height" (ver Evidencia textual).
- Confirmar si conviene usar el triangulo lateral, el criterio EJ del outlet, o ambos
  como restriccion combinada en el muestreador.

## Evidencia textual

| Dato / criterio | Frase original (maximo 15 palabras) | Seccion / pagina |
|---|---|---|
| Definicion de landmarks del triangulo (BH, BW) | "the anterior height (BH) and superior width (BW) of the first sacral body" | Lateral view, p. 1165 |
| El triangulo lo forman BH, BW y la densidad cortical iliaca | "BH and BW combined with the iliac cortical density of the pelvic brim forming a triangle" | Lateral view, p. 1165-1166 |
| Nombre y autoria de la propuesta | "This lateral sacral triangle is proposed by the author (T.M.) as the reliable key landmark" | Lateral view, p. 1166 |
| Plano de construccion: vista lateral estricta definida por landmarks oseos | "The strict lateral pelvic view was defined by bilaterally overlapping the most anterior as well as superior portions of the lateral margin of the alar slope" | Materials and methods, p. 1165 |
| Alineacion espacial automatica por software (no manual, algoritmo propio no detallado) | "Alignment was performed automatically for each pelvis using a programme code custom-made for Amira" | Materials and methods, p. 1165 |
| Definicion de ratioT (ambigua entre BH y BW) | "The ratio of BH and BW (triangle ratio – ratioT) reveals a significant linear correlation to PH" | Lateral view, p. 1166 |
| Formula de umbral en Discusion (BW>=1.5xBH) | "the dimensions of the S1 body depth are at least 1.5-fold as long as the S1 anterior body height (boundary ratio 1.5)" | Discussion, p. 1168-1169 |
| Umbral 1.5 obtenido por prueba estadistica propia (chi-cuadrado), no citado de otra fuente | "the chi-square test identifies a triangle ratio of 1.5 as a precise boundary value for 0 versus 1 or more screws" | Results, p. 1166 |
| PH (altura del istmo pedicular) es la variable limitante 3D | "the height of the pedicular isthmus (PH) as the limiting variable for secure screw insertion" | Abstract |
| PW (ancho pedicular) no restringe para 7.3 mm | "the width of the pedicular area (pedicle width (PW)) is typically much bigger than PH and therefore does not represent any restriction for a 7.3 mm screw" | Results, p. 1165 |
| PH excluido >18mm en el analisis de correlacion (10 pelvis) | "values of PH beyond 18 mm (10 pelves) were excluded, because the extensive dimensions... allowed trouble-free insertion of 5 or more SI screws" | Lateral view, p. 1166 |
| Umbral 2.0 para >=2 tornillos, seguridad 98% | "The ratios of an assumed boundary value of ≥2 provide enough bone stock for the secure location of two or more screws with a safety of 98%" | Lateral view, p. 1166 |
| Criterio del outlet: EJ (distancia endplate-articulacion) | "the distance between the S1 endplate and the SI joint top level (EJ)" | Abstract |
| Correlacion EJ vs PH: Pearson 0.8, p=0.0001 | "revealed a highly significant reciprocal dependency with a Pearson coefficient of 0.8 (p = 0.0001)" | Outlet view, p. 1167 |
| n=35/80 (44%) con EJ<=0mm | "Thirty-five of 80 pelves (44%), including 25 male and 10 female specimens, displayed an EJ of ≤0 mm" | Outlet view, p. 1167 |
| Tabla 2 - BH grupo sin tornillo (n=14) | "S1 body height (mm) BH 28.8 22.2–48.0" | Table 2, p. 1168 |
| Tabla 2 - BH grupo con >=1 tornillo (n=66) | "14.8 1.0–26.2" (columna BH, fila S1 body height) | Table 2, p. 1168 |
| Tabla 2 - BW grupo sin tornillo (n=14) | "S1 body width (mm) BW 31.6 27.5–36.6" | Table 2, p. 1168 |
| Tabla 2 - BW grupo con >=1 tornillo (n=66) | "33.8 26.1–43.6" (columna BW, fila S1 body width) | Table 2, p. 1168 |
| Tabla 2 - ratioT grupo sin tornillo | "Triangle ratio ratioT 1.16 0.7–1.5" | Table 2, p. 1168 |
| Tabla 2 - ratioT grupo con >=1 tornillo | "3.1 1.15–29.3" (columna ratioT) | Table 2, p. 1168 |
| Tabla 2 - EJ grupo sin tornillo | "S1 endplate–joint distance (mm) EJ 16.8 1.2–30.9" | Table 2, p. 1168 |
| Tabla 2 - EJ grupo con >=1 tornillo | "0.5" media; rango extraido como "16.1–21.8" (posible signo negativo no capturado en la extraccion) | Table 2, p. 1168 |
| Tabla 2 - PH (variable de referencia) grupo sin tornillo | "S1 pedicular isthmus height (mm) PH 4.7 2.5–7.0" | Table 2, p. 1168 |
| Tabla 2 - PH grupo con >=1 tornillo | "13.1 7.5–20.8" (columna PH) | Table 2, p. 1168 |
| Tabla 2 - PW grupo sin tornillo | "Pedicular isthmus width (mm) PW 17.6 9.4–23.2" | Table 2, p. 1168 |
| Tabla 2 - PW grupo con >=1 tornillo | "25.5 13.1–31.0" (columna PW) | Table 2, p. 1168 |
| Distribucion global de posibilidad de insercion (14/80, 18%) | "an impossible transverse insertion for one 7.3 mm screw in the first sacral segment in 14 cases (18%)" | Results, p. 1165 |
| 9/80 (11%) espacio para exactamente 1 tornillo | "In nine samples (11%), there was enough space for one SI screw" | Results, p. 1165 |
| 57/80 (71%) espacio para 2+ tornillos | "in 57 specimens (71%), 2 or more screws could be inserted" | Results, p. 1165 |
| Maximo 7 tornillos en 5 pelvis (todos varones sin anomalia) | "At most, seven SI screws could be inserted within the first sacral segment (five pelves)" | Results, p. 1165 |
| Cross-tabulacion Tabla 1: ratioT<1.5 -> 12 sin tornillo, 4 con tornillo | "Boundary ratioT <1.5 12 4 16" | Table 1, p. 1166 |
| Cross-tabulacion Tabla 1: ratioT>=1.5 -> 2 sin tornillo, 62 con tornillo | "1.5 2 62 64" | Table 1, p. 1166 |
| Solo 2/80 (3%) fallan pese a ratioT>=1.5 | "Only 2 of 80 pelves (3%) did not provide enough space for one 7.3 mm screw, although the ratioT amounted to ≥1.5" | Lateral view, p. 1166 |
| 4/80 (5%) con ratioT<1.5 si tuvieron espacio | "In four cases (5%) with a ratioT lower than 1.5, screw insertion was still possible" | Lateral view, p. 1166 |
| Deteccion de dysplasia propia: 12/14 (86%) con ratioT<1.5 | "After applying the triangle ratio method, 12 of 14 dysplastic pelves were detected (86%)" | Discussion, p. 1169 |
| Metodo: 80 CT humanos segmentados con Amira 4.2 | "80 human computed tomography data sets were segmented with the software Amira 4.2" | Abstract |
| Segmentacion semi-automatica con correccion manual en hueso osteoporotico | "Semi-automatic programme codes were used for the first step... Additional manual segmentation was required in some cases of thin cortical bone areas in osteoporotic pelves" | Materials and methods, p. 1165 |
| Software estadistico y umbral de significancia | "Statistical analysis was performed with SPSS 13 software... significance level p < 0.05" | Materials and methods, p. 1165 |
| Poblacion: pelvis excluidas si tenian trauma, tumor, inflamacion o degeneracion alta | "Pelvic bones showing traumatic residuals as well as tumorous, inflammatory or high-grade degenerative alterations were excluded" | Materials and methods, p. 1165 |
| Poblacion: edad media, altura, peso, sexo | "The mean age was 56 years (range: 18–89) with a mean body height of 173 cm (range: 147–193 cm) and a mean body weight of 76 kg (54–125 kg) including 33 females and 47 males" | Materials and methods, p. 1165 |
| Escaner CT y parametros de adquisicion | "Siemens SOMATOM Sensation... image resolution of 512 × 512 pixels, slice distance of 0.6 mm and kernel B45f" | Materials and methods, p. 1165 |
| Limitacion: solo trayectoria transversa, no oblicua | "the proposed reliable method for secure screw placement only addresses the strict transverse course of a 7.3 mm SI screw" | Discussion, p. 1169 |
| Limitacion: pelvis intactas, no clinicas/fracturadas | "the 80 pelves were intact, whereas in the clinical situation, this may not be the case" | Discussion, p. 1169 |
| Incidencia citada (no medida aqui) de posicion cefalica/dysplasia sacra | "A more cephalic position of the first sacral segment in relation to the iliac crests is observed with an incidence of 30–54%" | Introduction, p. 1164 (cita refs 2,7,15) |
| Complicaciones neurologicas iatrogenicas citadas (no medidas aqui) | "Numerous retrospective studies reported iatrogenic neural complications associated with implant malposition in up to 25% of patients" | Introduction, p. 1164 (cita refs 17,18,22) |
| Diametro/dimensiones exactas de tornillo mas alla de "7.3 mm" | NO ENCONTRADO EN EL PDF | — |
| Angulos en grados del triangulo o de la trayectoria | NO ENCONTRADO EN EL PDF | — |
