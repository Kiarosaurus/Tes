# herman2016 — Modelo matematico simple de zona segura para tornillos sacroiliacos (inlet/outlet)

- **DOI / URL:** 10.1002/jor.23396 (frase: "Please cite this article as doi: [10.1002/jor.23396]", p.1 del PDF). Paginacion de revista: NO ENCONTRADO EN EL PDF (version "Accepted Article", sin paginado; las paginas citadas abajo son del PDF)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/herman2016.pdf

## Que hace (3 lineas maximo)
Revision retrospectiva de 94 pacientes / 156 tornillos iliosacros percutaneos con CT postoperatoria como patron de oro.
Propone una regla proporcional de zona segura medida sobre fluoroscopia inlet y outlet (APPP = SIPP +-20%) y la valida contra la brecha cortical vista en CT.
Compara esa regla con la lectura subjetiva de la vista lateral y analiza dismorfismo sacro y nivel S1 vs S2.

## Restriccion o supuesto clave
No es un paper de sintesis generativa, pero su restriccion clave para esta tesis es el marco de referencia: el modelo vive en **proyecciones fluoroscopicas 2D (inlet y outlet)**, no en el volumen CT. "Mathematical determination of the safe-zone was defined on inlet and outlet radiographs" (Patients and Methods, p.5). El CT solo se usa como patron de oro binario de brecha: "Screws were defined as safe if the entire screw was within cortical bone on CT axial images" (p.6). Segundo supuesto explicito: la regla es adimensional y por tanto no entrega milimetros ni pose 3D: "it is a ratio of anatomic landmarks and therefore scale invariant" (Discussion, p.11).

## Respuestas a las preguntas dirigidas

**1. Cual es el modelo matematico, exactamente.**
Primitiva unica: una **recta en un plano de coordenadas proporcionales** (no cilindro, ni cono, ni elipse, ni triangulo). Construccion tal como el paper la escribe:
- En inlet se mide `a` = ancho antero-posterior del ala sacra en su porcion mas estrecha, "from the anterior cortex of the sacral ala to the posterior cortex (length a)" (p.5). La posicion del centro del tornillo desde la cortical anterior se expresa como porcentaje de `a` (APPP).
- En outlet se mide `b` = "the height from the superior margin of the neural foramen to the most inferior part of the superior cortex of the sacral-ala" (p.5). La posicion del centro del tornillo desde el margen inferior se expresa como porcentaje de `b` (SIPP).
- Criterio: "The screw was within the safe-zone if APPP=SIPP+-20%" (p.5).
- Formula explicita en la leyenda de la Figura 1: "the line equation is Y=b/aX" con origen (0,0) "just above the neural foramen" y (a,b) "in the superior posterior part of the sacrum but still anterior to the sacral neural canal" (Figura 1, p.16). Los puntos seguros son los proporcionales: "(0.2a,0.2b), (0.3a,0.3b) etc." (Figura 1, p.16).
En sintesis: zona segura = banda de +-20% alrededor de la recta Y=(b/a)X en coordenadas normalizadas por dos landmarks oseos, uno por vista.

**2. Es reimplementable a partir del PDF solo?**
**Parcialmente, y no para el uso que necesita la tesis.** A favor: la regla completa (landmarks, `a`, `b`, APPP, SIPP, tolerancia +-20%) esta escrita en prosa en Patients and Methods (p.5) y repetida en Discussion (p.9), sin depender de software propietario; la Figura 1 da la ecuacion de la recta. En contra, tres huecos concretos:
- El paper remite la derivacion a un apendice que **no esta en este PDF**: "was determined with mathematical calculations as described in Apppendix A" (p.5), y el PDF solo dice "Additional Supporting Information may be found in the online version" (p.1). Las 25 paginas del PDF no contienen Appendix A.
- Se cita una "Figure 3" para la definicion de brecha cortical (p.6) que **tampoco esta en el PDF** (solo hay Figura 1, 2a, 2b, 2c).
- La tolerancia +-20% aparece como dato dado; el PDF no reporta de donde sale ese valor ni analisis de sensibilidad al variarlo: NO ENCONTRADO EN EL PDF.
Ademas la regla es un **clasificador binario 2D de una posicion ya dada**, no un generador de pose: no define eje de insercion, ni angulo, ni punto de entrada, ni longitud. No permite muestrear una pose 3D.

**3. Marco de coordenadas.**
Vistas fluoroscopicas **inlet y outlet** (proyeccion 2D), mas la lateral como comparador. No hay reformateo segun el eje sacro, ni coordenadas de voxel, ni angulos de haz reportados. El CT interviene solo como verificacion: "Computerized tomography (CT) was considered the gold standard for evaluating screw position" (p.5). Angulos de inclinacion del arco en C (grados de inlet/outlet): NO ENCONTRADO EN EL PDF.

**4. Umbral de zona segura y su procedencia; cita el umbral de 10 mm?**
El umbral **propio** del paper es el +-20% proporcional, no una distancia en mm. Si cita el umbral de 10 mm, pero como contexto ajeno, dos veces:
- Introduccion (p.3): "the safe-zone for screw insertion was found to be larger than 10mm in 96% of pelvises [9-12]".
- Discussion (p.11): "up to 1cm of bone available for screw insertion in 96% of patients with sacral dysmorphism [10,12]", atribuido en el texto a "Anatomic studies by Gardner et al and Lee et al". Las referencias 10 y 12 de la lista son Gardner MJ et al., J Ortho Trauma 2010;24(10):622-629, y Lee JJ et al., J Orthop Res 2015;33(2):277-82.
Es decir: la atribucion aqui es **Gardner 2010 / Lee 2015**. El paper NO cita a Ziran 2003 ni a Moed 2006 en su lista de referencias: NO ENCONTRADO EN EL PDF.

**5. Cifras propias.** Ver tabla de Evidencia textual. Resumen: 94 pacientes, 156 tornillos; edad media 39.7 (+-14.86); 54 hombres (57.4%) / 40 mujeres (42.6%); 129 tornillos en S1 (82.7%) y 27 en S2 (17.3%); cortes de CT de 2 mm. **Diametro de tornillo asumido: NO ENCONTRADO EN EL PDF. Ninguna dimension de corredor en mm es medida ni publicada por este estudio: NO ENCONTRADO EN EL PDF.** Dispersion: se reportan DE para edad, ISS, AIS y numero de caracteristicas dismorficas; IC95% solo para las dos exactitudes globales.

**6. Validacion contra medicion independiente.** Si. La regla inlet-outlet se valida contra la CT postoperatoria: sensibilidad 97.1%, especificidad 84.0%, VPP 92.7%, VPN 93.3%, exactitud 92.9% (IC95% 85.1%-1.01%, tal como esta impreso). Se compara contra la lectura subjetiva de la lateral (exactitud 70.0%, IC95% 56.8%-84.6%), p=0.004. **Inconsistencias internas del propio PDF:** sensibilidad 97.1% en Abstract/Results vs "97.2%" en Discussion (p.10); especificidad lateral 61.5% en Results (p.7) vs "64.2%" en Discussion (p.10); el IC95% superior "1.01%" es tipograficamente imposible.

**7. Excluye CT con implantes metalicos?** No, al contrario: la cohorte es **CT postoperatoria con los tornillos puestos**, "pelvic ring fixation that included percutaneous ilio-sacral screws fixation and also had a post-operative CT" (Patients and Methods, p.4). Las exclusiones son "any patient with pelvic fixation at an outside facility, and fractures stabilized with plate osteosynthesis" (p.4). **La geometria NO es de anatomia virgen**; ademas son pelvis fracturadas.

**8. Dismorfismo sacro y jerarquia S1 vs S2.** Ambos si. Dismorfismo: 35 pacientes (37.2%) con al menos una caracteristica, sin asociacion con malposicion (Tabla 3, todos los p > 0.29). S1 vs S2: brecha cortical en 46/129 S1 (36.5%) vs 4/27 S2 (14.8%), p=0.035, "indicating higher probability of cortical breech for S1 screws" (p.8). El paper lo atribuye a que en S1 se insertan mas tornillos por vertebra (p.11).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| n = 94 pacientes, 156 tornillos | "94 patients with 156 screws met inclusion criteria" | Abstract, p.2 |
| 32.0% tornillos con brecha cortical | "of which 50 (32.0%) had a cortical breech on CT" | Abstract, p.2 |
| Sensibilidad 97.1% / especificidad 84.0% | "sensitivity and specificity ... were 97.1% and 84.0%" | Abstract, p.2 |
| Exactitud inlet-outlet 92.9% vs lateral 70.0% | "inlet-outlet and lateral safe zones were 92.9% and 70.0%" | Abstract, p.2 |
| Criterio de zona segura +-20% | "The screw was within the safe-zone if APPP=SIPP+-20%" | Patients and Methods, p.5 |
| Ecuacion del modelo | "the line equation is Y=b/aX" | Figura 1 (leyenda), p.16 |
| Umbral 10 mm (ajeno, ref. 9-12) | "safe-zone for screw insertion ... larger than 10mm in 96% of pelvises" | Introduccion, p.3 |
| 1 cm atribuido a Gardner y Lee | "up to 1cm of bone available for screw insertion in 96%" | Discussion, p.11 |
| S1 82.7% vs S2 17.3% de tornillos | "129 (82.7%) screws in S1 and 27 (17.3%) screws in S2" | Resultados, p.8 |
| Brecha S1 36.5% vs S2 14.8%, p=0.035 | "in S1 46 (36.5%) screws and in S2 in 4 (14.8%)" | Resultados, p.8 |
| Dismorfismo 37.2%, sin asociacion | "Thirty-five patients (37.2%) had at least one dysmorphic characteristic" | Resultados, p.8 |
| Edad media 39.7 (+-14.86) anos | "Mean age was 39.7 (+-14.86) years" | Resultados, p.7 |
| Sexo: 54 hombres (57.4%) / 40 mujeres (42.6%) | "included 54 (57.4%) men and 40 (42.6%) women" | Resultados, p.7 |
| Tornillos trans-sacros con mas brecha, p=0.038 | "37 (30.3%) of sacroiliac screws and 13 (38.2%) trans-sacral" | Resultados, p.9 |
| Compromiso neurologico nuevo 3/81 (3.7%) | "only a 3/81 (3.7%) novel post-operative neurologic compromise" | Discussion, p.11 |
| Grosor de corte CT 2 mm | "All sequences were 2mm cuts and with 2D reconstructions" | Discussion, p.12 |
| Malposicion fluoroscopia 2.5% vs navegacion CT 0.1% (Zwingmann) | "standard fluoroscopy (2.5%) vs CT navigation(0.1%)" | Discussion, p.9 |
| Diametro de tornillo | NO ENCONTRADO EN EL PDF | — |
| Dimensiones del corredor en mm (medidas propias) | NO ENCONTRADO EN EL PDF | — |
| Origen del valor +-20% / analisis de sensibilidad | NO ENCONTRADO EN EL PDF | — |
| Angulos de haz inlet/outlet en grados | NO ENCONTRADO EN EL PDF | — |
| Coordenadas de landmarks en el volumen CT | NO ENCONTRADO EN EL PDF | — |
| Appendix A (derivacion matematica) | "as described in Apppendix A" — el apendice no esta en el PDF | Patients and Methods, p.5 |
| Figura 3 (definicion de brecha) | Citada en p.6; la figura no esta en el PDF | Patients and Methods, p.6 |

## Evidencia textual
| Item | Frase original (<15 palabras) | Seccion / pagina PDF |
|---|---|---|
| Definicion de longitud `a` (inlet) | "anterior to posterior width was measure from the anterior cortex ... (length a)" | Patients and Methods, p.5 |
| Definicion de longitud `b` (outlet) | "height from the superior margin of the neural foramen to the ... superior cortex" | Patients and Methods, p.5 |
| Definicion de APPP | "proportion of the screw position from the anterior to posterior cortex" | Patients and Methods, p.5 |
| Definicion de SIPP | "superior-inferior proportional position (SIPP) ... center of the screw" | Patients and Methods, p.5 |
| Criterio de zona segura | "safe zone was defined if the percent on inlet is within +-20%" | Patients and Methods, p.5 |
| Regla operativa equivalente | "The screw was within the safe-zone if APPP=SIPP+-20%" | Patients and Methods, p.5 |
| Ecuacion de la recta | "A simple calculation will show that the line equation is Y=b/aX" | Figura 1, p.16 |
| Origen (0,0) | "Point (0,0) is just above the neural foramen" | Figura 1, p.16 |
| Punto (a,b) | "(a,b) is in the superior posterior part of the sacrum" | Figura 1, p.16 |
| Escala invariante / solo proporciones | "This method does not require the exact measurements but only proportions" | Figura 1, p.16 |
| Escala invariante (Discussion) | "it is a ratio of anatomic landmarks and therefore scale invariant" | Discussion, p.11 |
| Marco de medicion | "safe-zone was defined on inlet and outlet radiographs" | Patients and Methods, p.5 |
| Sitio de medicion | "measured in the narrowest portion of the sacral ala corridor" | Patients and Methods, p.5 |
| Patron de oro | "Computerized tomography (CT) was considered the gold standard" | Patients and Methods, p.5 |
| Definicion de tornillo seguro | "safe if the entire screw was within cortical bone on CT axial images" | Patients and Methods, p.6 |
| Definicion de brecha cortical | "any portion of the screw crossing the cortical margin on any ... reconstructions" | Patients and Methods, p.6 |
| Criterio de inseguridad en lateral | "Screws were deemed to be unsafe if the screw breached the iliac cortical density" | Patients and Methods, p.5 |
| Criterio de inclusion | "age > 18 years at the time of injury, pelvic ring fixation" | Patients and Methods, p.4 |
| Criterio de inclusion (CT postop) | "percutaneous ilio-sacral screws fixation and also had a post-operative CT" | Patients and Methods, p.4 |
| Criterio de exclusion | "pelvic fixation at an outside facility, and fractures stabilized with plate osteosynthesis" | Patients and Methods, p.4 |
| Periodo de reclutamiento | "from January 2011 to December 2014" | Patients and Methods, p.4 |
| Flujo de la cohorte | "294 patients with pelvis fractures, of which 215 had operative fixation" | Resultados, p.7 |
| Pacientes con CT | "94 patients had postoperative CT available for evaluation" | Resultados, p.7 |
| Edad media y DE | "Mean age was 39.7 (+-14.86) years" | Resultados, p.7 |
| Sexo | "54 (57.4%) men and 40 (42.6%) women" | Resultados, p.7 |
| ISS medio | "mean injury severity score was 27.31 (+-12.8)" | Resultados, p.7 |
| Malposicion por paciente | "43 (45.7%) patients had a mal-positioned screw" | Resultados, p.7 |
| Malposicion por tornillo | "106 (68.0%) screws safe and 50 (32.0%) screws were mal-positioned" | Resultados, p.8 |
| Reparto de la brecha | "25 (50%) screws breeched the anterior cortex and 25 (50%) ... neural foramen" | Resultados, p.8 |
| Clasificacion por el modelo | "111 (71.2%) screws were deemed safe on inlet-outlet radiographs" | Resultados, p.8 |
| Exactitud del modelo | "Overall accuracy of the mathematical calculated safe zone was 92.9%" | Resultados, p.8 |
| Sens/Esp del modelo | "Sensitivity and specificity were 97.1% and 84.0%, respectively" | Resultados, p.8 |
| VPP/VPN del modelo | "Positive and negative predictive values were 92.7% and 93.3%" | Resultados, p.8 |
| Asociacion modelo-CT | "statistically significant association ... (See Table 4, p value<0.001)" | Resultados, p.8 |
| IC95% de ambas exactitudes | "lateral ... (70.0%, 95% confidence interval of 56.8%-84.6%)" | Resultados, p.8 |
| IC95% inlet-outlet (tal cual, erratico) | "inlet-outlet safe zone (92.9%, 95% confidence interval of 85.1%-1.01%)" | Resultados, p.8 |
| Comparacion de exactitudes | "significant difference between subjective ... assessment of the lateral (p value=0.004)" | Resultados, p.8 |
| Exactitud de la lateral | "lateral x-rays accuracy was 70.0%. Sensitivity and specificity were 74.0% and 61.5%" | Resultados, p.7 |
| Lateral disponible solo en parte | "Lateral x-rays were saved and available in 40 patients" | Resultados, p.7 |
| Nivel S1/S2 | "129 (82.7%) screws in S1 and 27 (17.3%) screws in S2" | Resultados, p.8 |
| Brecha por nivel | "in S1 46 (36.5%) screws and in S2 in 4 (14.8%)" | Resultados, p.8 |
| Significancia S1 vs S2 | "difference was found to be statistically significant (p value=0.035)" | Resultados, p.8 |
| Tipo de tornillo | "122 (78.2%) screws were sacroiliac screws and 34 (21.8%) were trans-sacral" | Resultados, p.9 |
| Brecha por tipo de tornillo | "37 (30.3%) of sacroiliac screws and 13 (38.2%) trans-sacral screws" | Resultados, p.9 |
| Significancia tipo de tornillo | "statistically significant (p value=0.038)" | Resultados, p.9 |
| Dismorfismo: prevalencia | "Thirty-five patients (37.2%) had at least one dysmorphic characteristic" | Resultados, p.8 |
| Dismorfismo: sin asociacion | "no specific dysmorphic characteristics ... associated with mal-positioned screws" | Resultados, p.8 |
| Lista de caracteristicas dismorficas | "Co-linear sacrum and iliac crest / Up sloping sacral ala / Mamillary bodies / L5 sacralization / Large neural foramen / Sacral ala indentation" | Tabla 3, p.20 |
| Num. caracteristicas dismorficas (media+-DE) | "1.19 (+-1.89)" vs "1.04 (+-1.87)", p=0.664 | Tabla 3, p.20 |
| Umbral 10 mm (contexto ajeno) | "safe-zone ... was found to be larger than 10mm in 96% of pelvises" | Introduccion, p.3 |
| Atribucion del 1 cm | "Gardner et al and Lee et al ... up to 1cm of bone ... in 96%" | Discussion, p.11 |
| Definicion previa de zona segura (contexto) | "being in the center-center position on both views" | Introduccion, p.3 |
| Incidencia de malposicion en la literatura | "between 0.1 and 15% with neurologic injury reported in as many as 7.7%" | Discussion, p.9 |
| Comparacion Zwingmann | "standard fluoroscopy (2.5%) vs CT navigation(0.1%)" | Discussion, p.9 |
| Ningun tornillo totalmente fuera | "no incidence of a screw being placed completely outside the cortical bone" | Resultados, p.7 |
| Complicacion neurologica nueva | "only a 3/81 (3.7%) novel post-operative neurologic compromise" | Discussion, p.11 |
| Algoritmo intraoperatorio propuesto | "An intraoperative algorithm for K-wire or the center of screw position" | Patients and Methods, p.5 |
| Aplicacion en tiempo real | "On Inlet the surgeon needs to identify the anterior and posterior sacral ala cortexes" | Discussion, p.9 |
| Sesgo de lector unico | "both CT and fluoroscopic images where reviewed by the same author" | Discussion, p.12 |
| Grosor de corte CT | "All sequences were 2mm cuts and with 2D reconstructions" | Discussion, p.12 |
| Numero de cirujanos | "performed by four different fellowship trained trauma surgeons" | Discussion, p.12 |
| Conclusion (32%) | "Standard subjective fluoroscopic evaluation has a 32% incidence of screw mal-positioning" | Conclusion, p.12 |
| Software estadistico | "using SPSS (c) 16.0 (Chicago, Illinois)" | Statistical analysis, p.6 |
| Pruebas estadisticas | "Wilcoxon-Mann-Whitney rank sum test ... chi-square test" | Statistical analysis, p.6 |
| Nivel de significancia | "All p values reported are two-sided with p<0.05" | Statistical analysis, p.6 |
| Fechas editoriales | "Received 13 June 2016; Revised 5 August 2016; Accepted 19 August 2016" | p.1 |
| Apendice A ausente | "as described in Apppendix A" (no incluido en el PDF) | Patients and Methods, p.5 |
| Figura 3 ausente | Citada como "(Figure 3)"; no aparece en el PDF | Patients and Methods, p.6 |
| Diametro de tornillo | NO ENCONTRADO EN EL PDF | — |
| Longitud de tornillo | NO ENCONTRADO EN EL PDF | — |
| Valores absolutos de `a` y `b` en mm | NO ENCONTRADO EN EL PDF | — |
| Justificacion del margen +-20% | NO ENCONTRADO EN EL PDF | — |
| Angulos de arco en C (inlet/outlet, grados) | NO ENCONTRADO EN EL PDF | — |
| Protocolo de adquisicion CT (kVp, mAs, fabricante) | NO ENCONTRADO EN EL PDF | — |
| Uso o mencion de MAR / artefacto metalico en la CT | NO ENCONTRADO EN EL PDF | — |
| Definicion de dismorfismo (criterio/umbral por caracteristica) | NO ENCONTRADO EN EL PDF | — |
| Acuerdo inter/intra-observador (kappa) | NO ENCONTRADO EN EL PDF | — |
| Paginacion en la revista | NO ENCONTRADO EN EL PDF | — |

## Donde entra en mi tesis
Capitulo de trabajos relacionados, seccion de definicion de zona segura y de malposicion. Sirve para dos cosas concretas: (i) una **definicion binaria y estricta de malposicion** ("cualquier porcion del tornillo cruzando el margen cortical") que el muestreador puede adoptar como criterio de contencion cortical, y (ii) **prevalencias de malposicion medidas con CT postoperatoria** (32% por tornillo, 45.7% por paciente) y su reparto por nivel (S1 36.5% vs S2 14.8%) y por tipo (trans-sacro 38.2% vs iliosacro 30.3%), utiles como contexto de plausibilidad de las poses muestreadas. No entra como fuente geometrica del corredor.

## Dudas para el asesor
- La regla APPP=SIPP+-20% vive en el plano de proyeccion inlet/outlet. Convertirla a una restriccion en el marco del voxel exigiria fijar los angulos de inlet y outlet, que el paper no reporta. Vale la pena intentar esa conversion asumiendo angulos de otra fuente, o se descarta la regla como restriccion geometrica y se conserva solo como criterio binario de malposicion?
- Su cohorte es CT **postoperatoria con metal y con fracturas**. Sus prevalencias sirven como referencia de realismo, pero su anatomia no es virgen. Conviene citar sus tasas de malposicion junto a las de zwingmann2009navigated, o mezclan poblaciones demasiado distintas?
- El PDF tiene inconsistencias internas (97.1% vs 97.2%; 61.5% vs 64.2%; IC95% "85.1%-1.01%"). Cito solo los valores de Abstract/Resultados y anoto la discrepancia?

## Impacto sobre la tesis (propuesta del lector)

**(a) Ajustes que obliga o gaps que abre**

- **NO resuelve la implicancia #32.** El titulo promete implementabilidad, pero lo que entrega es un **clasificador binario 2D sobre fluoroscopia**, no una definicion geometrica del corredor oseo. No mide Dmax, no publica milimetros propios, no define un procedimiento de contorno oseo sobre el sacro y explicitamente renuncia a las medidas absolutas ("does not require the exact measurements but only proportions", Figura 1). El hueco de ancestro publicado del procedimiento de Dmax sobre el sacro **sigue abierto**.
- **Abre un gap nuevo (menor pero real): traduccion de marco.** Es la tercera fuente del repositorio que define zona segura en un marco que no es el del voxel (tras los angulos de haz fluoroscopico ya detectados). Sugiero que la tesis declare de forma explicita en trabajos relacionados que la literatura de zona segura se reparte en tres marcos incompatibles (voxel/CT reformateado, proyeccion fluoroscopica, medida cadaverica), y que solo el primero es directamente usable por el muestreador.
- **Refuerza la cadena de atribucion del umbral de 10 mm y la desplaza.** Aqui el 10 mm / 1 cm se atribuye a **Gardner 2010 y Lee 2015**, no a Ziran 2003 ni a Moed 2006 (que no aparecen en su bibliografia). Esto agrega una rama a la cadena abierta del repositorio y sugiere que Gardner 2010 es el nodo que hay que leer para cerrarla.
- **Aporta un supuesto reutilizable para el muestreador:** definicion estricta de brecha cortical (cualquier porcion del tornillo cruza la cortical) y el hallazgo de que ningun tornillo quedo integramente fuera del hueso. Esto acota el rango de malposiciones fisicamente plausibles que conviene muestrear (perforaciones parciales, no desplazamientos groseros).
- **Contradice parcialmente el manejo del dismorfismo:** aqui el dismorfismo NO se asocia a brecha cortical, y S1 muestra MAS brechas que S2. Si la tesis condiciona el muestreo solo en S1 por considerarlo el nivel de referencia, este paper da un argumento empirico independiente de que S1 es justamente el nivel de mayor riesgo, lo que apoya esa eleccion.
- **No cambia baseline.** peters2025hybrid sigue intacto; este paper no es un brazo de comparacion.

**(b) Nivel sugerido: 2 (metodo).** El modelo no se reimplementa, pero sus definiciones operacionales (malposicion, brecha cortical) y sus prevalencias por nivel y tipo de tornillo si se citan y condicionan el diseno del muestreador.

**(c) Acceso y paginas.** Acceso: PDF completo local, version "Accepted Article" del Journal of Orthopaedic Research (25 paginas en el PDF, sin paginacion de revista). Cuerpo pp.3-12; referencias pp.13-15; leyendas de figuras p.16; Tablas 1-4 pp.17-21; Figuras 1, 2a, 2b, 2c pp.22-25. **Faltan en el PDF: Appendix A y Figure 3.**
