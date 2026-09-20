# zhu2022optimalposition — Posicion optima de tornillos canulados en cuello femoral

- **DOI / URL:** 10.1002/jor.25503 (J Orthop Res. 2023;41(7):1546-1554; recibido 2022, epub 2022-12-20)
- **Nivel de lectura:** 2 (metodo) — *nivel propuesto por el asistente, decide la autora*
- **Leido a fondo por la autora:** no
- **PDF:** papers/zhu2022optimalposition.pdf

Profundidad: PDF completo (9 pp., pp. 1546-1554 + referencias).

## Que hace (3 lineas maximo)
Calcula sobre 34 TC de cadera la posicion "optima" de tres tornillos canulados en triangulo
invertido para fractura de cuello femoral, con la distancia punta-hueso subcondral medida en
fluoroscopia virtual AP y lateral. Valida con analisis de elementos finitos y con 20 vs 23
pacientes operados. **Para esta tesis solo importa una frase: la del modelo CAD del tornillo.**

## Restriccion o supuesto clave
No es un paper de sintesis generativa. El supuesto que si lo condiciona todo aqui es que el
tornillo se representa como un cilindro: en la etapa de imagen, *"7.3 mm diameter splines were
drawn in the coronal and sagittal planes to represent the cannulated screws"* (2.2, p. 1547).
Solo en el modelo de elementos finitos aparece una geometria por piezas
(*"thread diameter, 7.3 mm; thread length, 16 mm; thread pitch, 2.5 mm; and shaft diameter,
4.8 mm"*, 2.3, p. 1548). **Es exactamente la distincion que plantea la implicancia #97:** el
mismo paper usa 7.3 mm como envolvente para planificar y 4.8 mm de fuste para simular fisica.
El paper no comenta esa diferencia ni la justifica, y **no cita ninguna fuente para esas cuatro
cifras**: para el paso de rosca es un nodo TERMINAL, igual que Moed para el "1 cm".

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Paso de rosca 2.5 mm | *"thread pitch, 2.5 mm"* | 2.3 Finite element analysis, p. 1548 |
| Longitud roscada 16 mm | *"thread length, 16 mm"* | 2.3, p. 1548 |
| Diametro de fuste 4.8 mm | *"shaft diameter, 4.8 mm"* | 2.3, p. 1548 |
| Diametro de rosca 7.3 mm | *"thread diameter, 7.3 mm"* | 2.3, p. 1548 |
| Calibres clinicos 6.5 / 7.0 / 7.3 mm | *"cannulated screws (6.5, 7.0, or 7.3 mm)"* | Introduccion, p. 1547 |
| Fabricante del tornillo implantado | *"7.3-mm-diameter cannulated screws (Smith & Nephew)"* | 2.5, p. 1550 |
| Diametro de CABEZA | **NO ENCONTRADO EN EL PDF** | — |
| Diametro de nucleo (core/root) | **NO ENCONTRADO EN EL PDF** | — |
| Diametro de canulacion | **NO ENCONTRADO EN EL PDF** | — |
| Material del tornillo | **NO ENCONTRADO EN EL PDF** | — |
| Arandela | **NO ENCONTRADO EN EL PDF** | — |

## Donde entra en mi tesis
- **Implicancia #97 (mascara del implante).** Primera fuente verificada del repositorio con
  **paso de rosca, longitud roscada y diametro de fuste** de un canulado de 7.3 mm. Confirma
  las tres cifras que el deep-research daba "sin verificar" (G4 en `_candidatos.md`: paso
  2.5 mm, rosca 16 mm, fuste 4.8 mm) y **descarta el 2.75 mm de paso** que proponia el otro
  documento de deep-research. **No cierra #97:** faltan cabeza, nucleo, canulacion y arandela.
- **Implicancia #95 (brecha entre mascara de entrenamiento y de sintesis).** Respalda que
  "7.3 mm" y "el cuerpo del tornillo" son dos magnitudes distintas. Con 4.8 mm de fuste, el
  cilindro liso de 6.5-8.0 mm de `main.tex:113` sobreestima el area transversal en casi todo
  el trayecto, y **queda cerca del 5.00 mm medido en E8** sobre CLINIC-metal.
- **NO aplicar sin decision de la autora (regla 14).** Ademas: es cuello femoral, no iliosacro;
  ver "Limites de traslado".

## Limites de traslado a iliosacro
1. **Anatomia distinta.** Todo el paper es cuello y cabeza femoral (*"the coronal plane was
   parallel to the axis of the femoral neck"*, 2.2, p. 1547). El corredor S1/S2, la cortical
   iliaca, los forámenes sacros y el dismorfismo **no aparecen**: "sacrum", "iliosacral",
   "sacroiliac" y "pelvis" NO ENCONTRADO EN EL PDF (el unico hueso pelvico mencionado es la
   espina iliaca anterosuperior, y solo como sitio del tracker, 2.5, p. 1550).
2. **La geometria SI puede trasladarse, la indicacion no.** Lo citable es el dispositivo
   (canulado parcialmente roscado de 7.3 mm), no la pose ni las distancias. Las razones
   (triangulo invertido, distancia apex-subcondral, angulo de Pauwels) son femorales.
3. **Longitud roscada de 16 mm en hueso esponjoso corto.** En iliosacro el tramo roscado
   publicado por otras fuentes puede ser 16 o 32 mm; este PDF solo documenta 16 mm y en femur.
4. **No hay fuente ni numero de catalogo.** Las cuatro cifras del modelo CAD aparecen sin cita
   y sin declarar el fabricante de ESE modelo; el fabricante (Smith & Nephew) se declara para
   los tornillos implantados en los pacientes, en otra seccion, sin dimensiones.

## Que dice del CT, la imagen y los artefactos
- **CT si, artefacto no.** Protocolo declarado: *"120 kV, 250 mA; field of view, 320 mm;
  matrix, 512 x 512; and slice thickness, 0.625 mm"* (2.1, p. 1547), en un *"Revolution
  256-slice CT; GE Healthcare"*. Segmentacion manual en MIMICS 21.0.
- **Los TC de planificacion son SIN metal**; el metal solo aparece en el TC postoperatorio
  (*"CT images, were obtained within 24 h after surgery to assess whether the screw had
  penetrated"*, 2.6, p. 1550), usado con criterio **binario** de penetracion.
- **"artifact", "metal artifact", "MAR", "Hounsfield" y "HU": NO ENCONTRADO EN EL PDF.** El
  paper no comenta como midio area y perimetro del triangulo en un TC con tres tornillos, que
  es justo donde el artefacto haria dudosa la medicion. Es una omision citable como limitacion
  ajena, no como resultado.
- La otra imagen es fluoroscopia (virtual y real con arco en C Siemens) y radiografia.

## Evidencia textual

### Geometria del tornillo (lo que busca #97)
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Calibres clinicos habituales | *"three partially threaded cannulated screws (6.5, 7.0, or 7.3 mm)"* | Introduccion, p. 1547 |
| Representacion en imagen = cilindro | *"7.3 mm diameter splines were drawn in the coronal and sagittal planes"* | 2.2, p. 1547 |
| **Diametro usado en las razones de la Tabla 1** | *"according to the screw diameter (Ds1 = Ds2 = 7 mm)"* | 2.2, p. 1548 |
| Diametro de rosca (modelo FEA) | *"thread diameter, 7.3 mm"* | 2.3, p. 1548 |
| Longitud de rosca (modelo FEA) | *"thread length, 16 mm"* | 2.3, p. 1548 |
| **Paso de rosca (modelo FEA)** | *"thread pitch, 2.5 mm"* | 2.3, p. 1548 |
| **Diametro de fuste (modelo FEA)** | *"shaft diameter, 4.8 mm"* | 2.3, p. 1548 |
| Fabricante (tornillos implantados) | *"7.3-mm-diameter cannulated screws (Smith & Nephew)"* | 2.5, p. 1550 |
| Canulado, parcialmente roscado | *"use of three parallel partially threaded cannulated screws"* | 2.4, p. 1550 |
| Diametro de cabeza | NO ENCONTRADO EN EL PDF | — |
| Altura de cabeza | NO ENCONTRADO EN EL PDF | — |
| Diametro de nucleo (root/core) | NO ENCONTRADO EN EL PDF | — |
| Diametro de la canulacion / agujero | NO ENCONTRADO EN EL PDF | — |
| Longitud total del tornillo (mm) | NO ENCONTRADO EN EL PDF (solo *"approximately 5 mm shorter than that measured on fluoroscopy"*, 3.1, p. 1550) | 3.1, p. 1550 |
| Material (titanio / acero / ASTM) | NO ENCONTRADO EN EL PDF | — |
| Arandela / washer | NO ENCONTRADO EN EL PDF | — |
| Referencia bibliografica de las 4 cifras del CAD | NO ENCONTRADO EN EL PDF (aparecen sin cita) | 2.3, p. 1548 |

### Adquisicion y procesamiento de imagen
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Escaner | *"Revolution 256-slice CT; GE Healthcare"* | 2.1, p. 1547 |
| Parametros | *"120 kV, 250 mA; field of view, 320 mm; matrix, 512 x 512"* | 2.1, p. 1547 |
| Grosor de corte | *"slice thickness, 0.625 mm"* | 2.1, p. 1547 |
| Software de segmentacion | *"(MIMICS) Research software (version 21.0; Materialise NV)"* | 2.2, p. 1547 |
| Eje del cuello femoral | *"determined using the Reikerals method"* | 2.2, p. 1547 |
| Segmentacion manual | *"After outlining the bone cortex, layer-by-layer, a 3D mask ... was obtained"* | 2.2, p. 1547 |
| TC postoperatorio | *"CT images, were obtained within 24 h after surgery"* | 2.6, p. 1550 |
| Artefacto metalico / MAR / HU | NO ENCONTRADO EN EL PDF | — |
| Ventanas HU | NO ENCONTRADO EN EL PDF | — |

### Cohorte y criterios
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| n de TC para la planificacion | *"included 34 CT images, contributed by 16 men and 18 women, 23-72 years"* | 3.1, p. 1550 |
| Fechas de adquisicion | *"between June 1, 2021, and June 7, 2021"* | 2.1, p. 1547 |
| Criterio de inclusion | *"clear visualization of the anatomy of the proximal femur"* | 2.1, p. 1547 |
| Exclusion | *"unclosed epiphysis or proximal femur deformity due to fracture, osteoarthritis, avascular necrosis"* | 2.1, p. 1547 |
| Grupo Modificado | *"Modified group-20 patients, including 13 men and 7 women, 43-59 years"* | 3.3, p. 1551 |
| Grupo Convencional | *"Conventional group-23 patients, including 10 men and 13 women, 36-55 years"* | 3.3, p. 1551 |
| Criterio de desenlace (binario) | *"no incidence of cannulated screw penetration into the femoral neck or head"* | 3.3, p. 1551 |
| Seguimiento | *"All patients were followed up for at least 10 months"* | 3.3, p. 1551 |
| Significacion | *"with a p <= 0.05 considered significant"* | 2.7, p. 1550 |
| Robot / arco en C | *"TiRobot system (TINAVI Medical Technologies), a C-arm X-ray system (Siemens)"* | 2.5, p. 1550 |
| Fiabilidad interobservador / kappa | NO ENCONTRADO EN EL PDF | — |

### Umbrales y criterios clinicos citados (todos de terceros)
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Espesor de cartilago | *"The cartilage thickness of the femoral head is 2-3 mm"* | Introduccion, p. 1547 |
| Espesor de hueso subcondral | *"with a 1-2 mm thickness of the subchondral bone"* | Introduccion, p. 1547 |
| Umbral TAD | *"a TAD <= 25 mm can effectively avoid cutting out of the screw"* | Introduccion, p. 1547 |
| Recomendacion de punta (cita ref. 15) | *"the screw tip should be located within 5 mm of the subchondral bone"* | Introduccion, p. 1547 |
| Recomendacion alternativa (cita ref. 16) | *"others have suggested a distance of 5-10 mm"* | Introduccion, p. 1547 |
| Falta de respaldo de esos umbrales | *"However, reliability data for these recommendations are lacking."* | Introduccion, p. 1547 |
| Ajuste practico de longitud | *"approximately 5 mm shorter than that measured on fluoroscopy images"* | 3.1, p. 1550 |

### Parametros del modelo de elementos finitos
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Angulo de fractura | *"a femoral neck fracture (Pauwels angle, 70 grados) modeled"* | 2.3, p. 1548 |
| Friccion tornillo-hueso | *"the coefficient of friction between the screw shaft and the bone was set at 0.3"* | 2.3-2.4, pp. 1548-1549 |
| Friccion en la fractura | *"the friction coefficient between these surfaces set at 0.46"* | 2.4, p. 1549 |
| Carga | *"a force of 2100 N was applied to the center of the femoral head"* | 2.4, p. 1549 |
| Orientacion | *"the assembled model was abducted 10 grados and tilted posteriorly by 9 grados"* | 2.4, p. 1549 |
| Supuesto de material oseo | *"synthetic composite bone was assumed to be homogeneous and isotropic"* | 2.4, p. 1549 |
| Modulo de Young / Poisson (valores) | NO ENCONTRADO EN EL PDF (*"were assigned by Ansys"*) | 2.4, p. 1549 |
| Modulo del tornillo | NO ENCONTRADO EN EL PDF | — |
| Tamano de malla / n de nodos | NO ENCONTRADO EN EL PDF | — |
| Desplazamiento maximo femur | *"8.874"* (Convencional) frente a *"6.523"* (Modificado), en mm | Tabla 2, p. 1552 |
| Tension maxima del implante | *"487.4"* frente a *"398.5"* MPa | Tabla 2, p. 1552 |

### Resultados geometricos (Tabla 1 y Tabla 4)
| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Razon anterior AP | *"La1/Ln1 0.16 0.1-0.2"* | Tabla 1, p. 1551 |
| Razon posterior AP | *"Lp1/Ln1 0.28 0.16-0.43"* | Tabla 1, p. 1551 |
| Razon inferior lateral | *"Li2/Ln2 0.55 0.51-0.59"* | Tabla 1, p. 1551 |
| Distancia apex-subcondral maxima medida | *"Di2 (mm) 6.68 4.27-8.93"* | Tabla 1, p. 1551 |
| Area del triangulo | *"160.85 +/- 23.45"* frente a *"224.54 +/- 40.02"* mm2, *"<0.001"* | Tabla 4, p. 1553 |
| Perimetro | *"51.94 +/- 9.65"* frente a *"61.37 +/- 10.63"* mm, *"0.004"* | Tabla 4, p. 1553 |
| Tiempo de consolidacion | *"4.4 +/- 1.3"* frente a *"3.7 +/- 0.9"* meses, *"0.06"* | Tabla 4, p. 1553 |
| Harris | *"87.4 +/- 13.1"* frente a *"90.0 +/- 3.3"*, *"0.61"* | Tabla 4, p. 1553 |

### Inconsistencias internas detectadas
| Que | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Diametro 7.3 mm en la construccion de splines... | *"7.3 mm diameter splines were drawn"* | 2.2, p. 1547 |
| ...pero 7 mm al calcular las razones | *"according to the screw diameter (Ds1 = Ds2 = 7 mm)"* | 2.2, p. 1548 |
| Conclusion escribe mal el implante | *"a method for optimal placement of cannulate screws"* | 5 Conclusion, p. 1553 |

## Dudas para el asesor
1. ¿Se acepta citar un paper **femoral** para las dimensiones del dispositivo (paso, rosca,
   fuste) declarando explicitamente que la indicacion iliosacra viene de otra fuente? Es la
   unica cifra verificada de paso de rosca que hay hoy en el repositorio.
2. El propio paper usa **dos geometrias distintas del mismo tornillo** (cilindro de 7.3 mm
   para planificar, fuste de 4.8 mm para el FEA) sin comentarlo. ¿Es argumento suficiente para
   que `main.tex` separe "envolvente de viabilidad" (#31) de "mascara de metal" (#95, #97)?
3. Las cuatro cifras del CAD van **sin cita y sin numero de catalogo**. ¿Basta como fuente
   primaria, o hay que esperar a G1/G2/T1 antes de tocar `main.tex:113`?
4. El paper mide area y perimetro del triangulo sobre TC postoperatorio **con tres tornillos y
   sin mencionar artefacto**. ¿Vale como ejemplo citable de la limitacion que motiva la tesis?
