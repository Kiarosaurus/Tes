# yang2022computeraided — Planificacion automatica y analisis biomecanico de un tornillo en arco para fractura pelvica

- **DOI / URL:** 10.1016/j.cmpb.2022.106810 (Computer Methods and Programs in Biomedicine 220 (2022) 106810; ambos en la portada, p. 1)
- **Nivel de lectura:** 2 (metodo). Lo util para la tesis es el criterio de contencion por
  erosion 3D (distancia de la linea central a la superficie osea) y el caso recto
  (curvatura cero) ilion-S1-ilion; el analisis de elementos finitos (FEA) es contexto.
- **Leido a fondo por la autora:** no
- **PDF:** papers/yang2022computeraided.pdf
- **Profundidad / acceso:** COMPLETO. PDF editorial de Elsevier, 11 paginas numeradas 1-11,
  con referencias completas (40).

> **CORRESPONDENCIA PDF/RAW: SI CORRESPONDE.** Titulo, revista, volumen 220, articulo 106810,
> DOI y lista de autores del PDF (p. 1) coinciden con `refs/raw/yang2022computeraided.nbib`.
> Primer autor: **Qing Yang** (p. 1), igual que el raw ("FAU - Yang, Qing"). La fila de
> `_candidatos.md` que dice "Yang, W." esta equivocada: ningun autor del PDF tiene inicial W
> como primer autor; "Wang" (Yu Wang) es el autor de correspondencia, el ultimo.
>
> **Los dos raw son el mismo articulo.** `refs/raw/yang2022arcplanning.nbib` y
> `refs/raw/yang2022computeraided.nbib` tienen el mismo PMID (35462347), titulo, DOI, volumen,
> autores y abstract. Diferencias encontradas al comparar linea a linea: el de `arcplanning`
> empieza con una linea en blanco y escribe "Copyright (c) 2022"; el de `computeraided` escribe
> "Copyright © 2022". Nada mas.
>
> **El PDF viejo (`papers/yang2022arcplanning.pdf`) queda identificado**: es la ref. [16] de
> este articulo, el paper de congreso de los mismos autores del que sale el algoritmo: "Q.
> Yang, J. Song, C. Cheng, C. Shi, C. Liang, Y. Wang, An Internal Arc Fixation Channel and
> Automatic Planning Algorithm for Pelvic Fracture, 2021 4th Int. Conf. Robot. Control Autom.
> Eng. (2021) RCAE(n.d.), doi:10.1109/RCAE53607.2021.9638862" (Referencias, p. 10). Este DOI
> lo da este PDF; no hay raw para ese paper en `refs/raw/`.

## Que hace (3 lineas maximo)
Sobre 10 pelvis intactas (CT, segmentadas en Mimics) genera canales en arco de curvatura
constante ilion-S1-ilion a partir de retículas de puntos derivados de 3 semillas, y elige el
optimo con un puntaje de distancia a la superficie por erosion 3D (CSV); compara con el canal
recto (curvatura 0) y luego compara tornillo en arco vs recto por FEA en 1 pelvis y 3 posturas.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; no aplica la pregunta sobre implantes metalicos.
Supuestos que importan para el muestreador:
- **Optimo determinista, no distribucion.** El algoritmo termina en un solo canal: "obtain the
  optimal safest IAFC" (Step 8, sec. 2.2, p. 2). No modela malposicion ni error quirurgico.
- **Seguridad = distancia de la linea central a la superficie**, sin diametro del tornillo en
  la planificacion: "distance between the centreline of the IAFC and the surface" (sec. 2.2, p. 2).
  El diametro (7.3 mm) solo aparece en el FEA (sec. 2.4.2, p. 3).
- **Pelvis intactas**, no fracturadas ni con implantes: "ten patients with an intact pelvis"
  (sec. 2.1, p. 2). Planos anatomicos calibrados a mano en SolidWorks (sec. 2.1, p. 2).
- **No hay umbral de CSV aceptable** ni margen en mm; solo se maximiza.
- El abstract afirma un test no parametrico, pero el cuerpo no describe test, estadistico ni
  p-valor (ver Evidencia textual).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
Ninguno decidido. Candidatos, si la autora quiere citar el antecedente:

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 10 pelvis intactas | "ten patients with an intact pelvis from Beijing Jishuitan Hospital" | 2.1, p. 2 |
| Voxel de 1 mm para el CSV | "Transform the pelvis into a voxel model with voxel size of 1 mm" | 2.2 Step 4, p. 2 |
| 1 de 10 pelvis sin canal recto (pelvis 4) | "thus it is impossible to generate an ISFC in the pelvis" | 4, p. 8 |

## Donde entra en mi tesis
Objetivo 2 (muestreador), solo como **contexto / trabajo relacionado**. No compite con el
muestreador:
- **Optimiza, no muestrea.** Busca un unico canal "relativamente optimo" por pelvis con una
  regla lexicografica (max CSV, luego menos minimos en el VDVA, luego max promedio). No hay
  poses multiples, ni malposicion, ni condicionamiento por tecnica. El muestreador de la tesis
  hace lo contrario: muestrea malposicion ordinal de `zwingmann2009navigated` solo en S1.
- **Relacion con `goerres2017planning` y `han2019atlasplanning`.** Los tres son planificacion
  determinista de una trayectoria segura. Diferencias: Goerres y Han transfieren corredores
  anotados por experto desde un atlas (12 y 40 pelvis) y ajustan una recta; Yang no usa atlas,
  hace busqueda exhaustiva por paciente sobre una reticula de puntos derivados y puntua con un
  mapa de distancia por erosion. Yang si cubre ilion-S1-ilion (Goerres no tiene S1); Han si
  tiene IS S1/S2 y reporta distancia media a cortical en mm, Yang reporta CSV sin unidades
  declaradas. Ninguno de los tres modela malposicion graduada.
- **Antecedente del chequeo de contencion.** El CSV = minimo del mapa de distancia a lo largo
  de la trayectoria (Fig. 1, p. 3) es un precedente publicado (revista indexada, a diferencia del
  congreso de la ficha vieja) de puntuar contencion cortical con un transformado de distancia por
  erosion 3D. Sirve como cita de precedente, no como fuente de umbrales.
- **Contexto anatomico:** en la pelvis 4 no hubo canal recto por la altura de S1 (sec. 4, p. 8).
- **Cifra de contexto que conecta con una cadena ya registrada:** "approximately 18%" de dano a
  cola de caballo / tronco lumbosacro, refs. [5-8] (Intro, p. 1). Es la misma familia de cifra
  "18%" de `gardner2010safezones` y `tejwani2014` (implicancias, seccion 12 de la ficha de
  Gardner): NO es el 2-15% y no debe mezclarse.

### Comparacion con la ficha vieja `yang2022arcplanning.md` (pregunta 4)
Son trabajos hermanos de los mismos autores: el PDF viejo es el congreso RCAE 2021 (ref. [16]),
este es la version extendida en revista. Lo que coincide:
- Mismo algoritmo: 3 semillas (entrada, S1 en el plano sagital, salida), reticula 10 x 10 de
  puntos derivados, voxel 1 mm, erosion 3D, CSV = minimo del VDVA, desempates por numero de
  minimos y promedio del VDVA, canal recto como arco de curvatura cero.
- **Las cifras de las pelvis 1-5 son identicas** a la Tabla I de la ficha vieja (Fig. 9, p. 7):
  1: 162.82 mm / 0.0089 / CSV 10; 2: 146.81 / 0.0078 / 10; 3: 141.56 / 0.0053 / 10;
  4: 154.86 / 0.0187 / 8; 5: 150.98 / 0.0126 / 11.
- Misma observacion sobre la pelvis 4 (S1 alto, sin canal recto) y misma fuente de datos
  (Beijing Jishuitan Hospital, Mimics, Geomagic).
Lo que cambia: N = 10 (no 5), se agregan pelvis 6-10, aparece el FEA (Abaqus, 3 posturas,
2 modelos de fractura), el ejemplo de VDVA es otro ([0,1,1,2,3,4,4,3,2,2,1,0,0] aqui; la ficha
vieja trae [0,1,1,2,2,2,2,2,1,1,0,0]), se agrega una funcion opcional de limite de curvatura, y
la cita de la "zona segura" (ref. [18] del congreso) no aparece en este texto.
Consecuencia: las cifras 1-5 de la ficha vieja ahora tienen respaldo en un articulo que si
corresponde a su raw, pero deben citarse desde ESTA ficha y este PDF.

## Dudas para el asesor
- Los dos raw (`yang2022arcplanning.nbib` y `yang2022computeraided.nbib`) son el mismo articulo:
  la autora decide cual clave queda y que pasa con el PDF del congreso (ref. [16]), que hoy esta
  bajo una clave cuyo raw no le corresponde (implicancia #180). No se edito nada en `refs/`.
- La fila de `_candidatos.md` atribuye el paper a "Yang, W."; el PDF y el raw dicen Yang, Qing.
- El CSV no declara unidades (por el voxel de 1 mm parece mm, pero no esta escrito): si se cita,
  citarlo como "valor de distancia en voxeles", no en mm.
- El abstract habla de un test no parametrico que el cuerpo no reporta. Vale la pena citar
  resultados biomecanicos? (No tocan la tesis; recomendacion: no.)

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Titulo | "Computer-aided automatic planning and biomechanical analysis of a novel arc screw" | Titulo, p. 1 |
| Revista, volumen, articulo | "Computer Methods and Programs in Biomedicine 220 (2022) 106810" | Encabezado, p. 1 |
| DOI | "https://doi.org/10.1016/j.cmpb.2022.106810" | Pie, p. 1 |
| Autores | "Qing Yang, Siru Feng, Jian Song, Chang Cheng, Chendi Liang, Yu Wang" | Portada, p. 1 |
| Fechas | "Received 7 December 2021 Revised 28 March 2022 Accepted 10 April 2022" | Article info, p. 1 |
| Incidencia (contexto, citada) | "Pelvic fractures account for 1%–3% of all fractures" | 1, p. 1 |
| Incidencia mayor (citada) | "and 2% of all major fractures treated [1]" | 1, p. 1 |
| Dano neurologico 18% (citado, refs. 5-8) | "caused by the insertion of the sacroiliac screw is approximately 18%" | 1, p. 1 |
| Hipotesis 1 | "There is truly an optimal IAFC in the pelvis" | 1, p. 2 |
| Datos: origen y N | "ten patients with an intact pelvis from Beijing Jishuitan Hospital" | 2.1, p. 2 |
| Segmentacion | "imported into the software Mimics to segment and reconstruct the complete 3D" | 2.1, p. 2 |
| Calibracion de planos | "sagittal plane, coronal plane, and transverse plane were manually calibrated" | 2.1, p. 2 |
| Formato de entrada al algoritmo | "pelvic model in STL format was used in the channel generation algorithm" | 2.1, p. 2 |
| Tipo de canal | "we designed the IAFC as a constant-curvature channel" | 2.2, p. 2 |
| Definicion CSV | "distance between the centreline of the IAFC and the surface ... as ... (CSV)" | 2.2, p. 2 |
| Interpretacion CSV | "the lower the CSV, the higher is the risk of the channel passing" | 2.2, p. 2 |
| Definicion VDVA | "We can obtain an array of each IAFC, which we define as ... (VDVA)" | 2.2, p. 2 |
| Ejemplo VDVA | "One of VDVA example forms is [0,1,1,2,3,4,4,3,2,2,1,0,0]" | 2.2, p. 2 |
| Origen del algoritmo | "The generation and selection of the optimal IAFC algorithm [16]" | 2.2, p. 2 |
| Numero de pasos | "The methodology consists of an eight approach given below" | 2.2, p. 2 |
| Semillas | "select one point near S1 on the sagittal plane ... as the middle seed point" | 2.2 Step 1, p. 2 |
| Quien elige las semillas (manual/automatico) | NO ENCONTRADO EN EL PDF (Step 1 dice "Select", sin agente) | 2.2, p. 2 |
| Filtro de puntos | "Remove the points that fell outside the pelvis during the derivation." | 2.2 Step 2, p. 2 |
| Separacion de la reticula | "The interval between the derived points is 5 mm" | 2.2 Step 2, p. 2 |
| Tamano de la reticula | "the number is a square lattice of 10 × 10" | 2.2 Step 2, p. 2 |
| Maximo de candidatos | "At most 100 × 100 × 100 arc channels can be obtained." | 2.2 Step 3, p. 2 |
| Voxel | "voxel model with voxel size of 1 mm × 1 mm × 1 mm" | 2.2 Step 4, p. 2 |
| Erosion 3D | "Corrode the pelvis model with the 3D erode algorithm [17]" | 2.2 Step 4, p. 2 |
| Criterio 1 | "Filter out the channels with the largest CSV in the IAFCs." | 2.2 Step 6, p. 2 |
| Criterio 2 | "filter the IAFCs with the least number of minimum values in the VDVA" | 2.2 Step 7, p. 2 |
| Criterio 3 | "Identify the IAFC with the maximum average value of VDVA" | 2.2 Step 8, p. 2 |
| Formula CSV | "CSV = min({VDVA_i})" | Fig. 1, p. 3 |
| Limite de curvatura opcional | "we add the function of IAFCs curvature limitation to the algorithm" | 2.2, p. 2 |
| Canal recto | "The straight line is an arc with zero curvature." | 2.3, p. 2-3 |
| Mismo criterio para el recto | "procedures for selection and calculation of all ISFCs were the same" | 2.3, p. 3 |
| FEA: software y modelos | "completed using the software Abaqus, and two pelvic posterior ring fractures" | 2.4, p. 3 |
| FEA: una sola pelvis | "selected one of the ten cases of pelvis used in the channel planning" | 2.4, p. 3 |
| FEA: criterio de eleccion | "the CSV between the IAFC and ISFC ... was less than two" | 2.4, p. 3 |
| Cargas de validacion | "500 N and 800 N vertically downward concentrated static forces were applied" | 2.4.1, p. 3 |
| Espesor cortical | "generally set at 1.5–2 mm, and it was defined as 2 mm" | 2.4.2, p. 3 |
| Material del tornillo | "The material used for the IAFS and ISFS was Ti6-al4-v." | 2.4.2, p. 3 |
| Diametro del tornillo (solo FEA) | "The diameter of both IAFS and ISFS is 7.3mm" | 2.4.2, p. 3 |
| Malla pelvica | "the pelvic mesh size was selected as 2–3 mm in this study" | 2.4.2, p. 4 |
| Malla de implantes | "The implant components were meshed 1 mm" | 2.4.2, p. 4 |
| Modulo de Young cortical / trabecular | Tabla 1: "Cortical bone 17000"; "Trabecular bone 150" (Mpa) | Tabla 1, p. 4 |
| Modulo cartilago / Ti | Tabla 1: "Cartilage 24.3"; "Ti6Al4V 110000" | Tabla 1, p. 4 |
| Poisson | Tabla 1: cortical "0.3", trabecular "0.2", cartilago "0.4", Ti "0.3" | Tabla 1, p. 4 |
| Inconsistencia femur | Texto: "so it was also set as cortical bone"; Tabla 1: "Femoral ... Cortical bone 150" | 2.4.2 y Tabla 1, p. 4 |
| Ligamento anterior | "simulated using 28 springs with the isometric stiffness value of 500 N/mm" | 2.4.3, p. 5 |
| Ligamento posterior | "simulated using 67 springs with the isometric stiffness value of 500 N/mm" | 2.4.3, p. 5 |
| Cargas "Standing up" | Tabla 3: "-369.4 105.9 1541.2 0.000 1.321 8.340" | Tabla 3, p. 5 |
| Cargas "Going upstairs" | Tabla 3: "-357.3 370.0 2062.8 0.000 2.968 18.739" | Tabla 3, p. 5 |
| Cargas "Walking" | Tabla 3: "-390.1 234.4 1938.7 0.000 1.988 12.551" | Tabla 3, p. 5 |
| Origen de cargas | "loading parameters referred to the measured data ... by Bergmann et al." | 2.4.4, p. 6 |
| Validacion 500 N: DSI / sacro / ISFS (MPa) | Tabla 4: "Maximum stress (Mpa) 8.641 19.04 74.244" | Tabla 4, p. 6 |
| Validacion 500 N: deformacion (mm) | Tabla 4: "Maximum deformation (mm) 2.914 2.371 2.065" | Tabla 4, p. 6 |
| Validacion 800 N: tension (MPa) | Tabla 4: "Maximum stress (Mpa) 13.826 30.468 118.795" | Tabla 4, p. 6 |
| Validacion 800 N: deformacion (mm) | Tabla 4: "Maximum deformation (mm) 4.662 3.794 3.304" | Tabla 4, p. 6 |
| Resultado CSV | "We can see that the CSV of IAFCs is higher than that of ISFCs." | 3.2, p. 6 |
| CSV del canal recto por pelvis | Solo grafico (Fig. 8); tabla numerica NO ENCONTRADO EN EL PDF | Fig. 8, p. 6 |
| Unidades del CSV | NO ENCONTRADO EN EL PDF (eje "CSV" sin unidad) | Fig. 8, p. 6 |
| Personalizacion | "This shows that IAFC has obvious personalised characteristics." | 3.2, p. 6 |
| Pelvis 1: CSV / largo / curvatura | Fig. 9: "1 10 162.82 0.0089" | Fig. 9, p. 7 |
| Pelvis 2 | Fig. 9: "2 10 146.81 0.0078" | Fig. 9, p. 7 |
| Pelvis 3 | Fig. 9: "3 10 141.56 0.0053" | Fig. 9, p. 7 |
| Pelvis 4 | Fig. 9: "4 8 154.86 0.0187" | Fig. 9, p. 7 |
| Pelvis 5 | Fig. 9: "5 11 150.98 0.0126" | Fig. 9, p. 7 |
| Pelvis 6 | Fig. 9: "6 9 141.65 0.0100" | Fig. 9, p. 7 |
| Pelvis 7 | Fig. 9: "7 9 152.10 0.0170" | Fig. 9, p. 7 |
| Pelvis 8 | Fig. 9: "8 8 137.86 0.0104" | Fig. 9, p. 7 |
| Pelvis 9 | Fig. 9: "9 10 143.68 0.0154" | Fig. 9, p. 7 |
| Pelvis 10 | Fig. 9: "10 8 174.45 0.0190" | Fig. 9, p. 7 |
| Unidades de largo | Fig. 9: "Length(mm)" | Fig. 9, p. 7 |
| Unidades de curvatura | NO ENCONTRADO EN EL PDF | Fig. 9, p. 7 |
| Resultado FEA cualitativo | "the stress on the ilium and the screw of the affected side decreased significantly" | 3.3, p. 8 |
| Tensiones y deformaciones por postura | Solo en contornos (Figs. 10-11) y barras (Fig. 12); tabla NO ENCONTRADO EN EL PDF | Figs. 10-12, p. 7-9 |
| Limitacion: 3 posturas | "only the loads under 'standing up', 'going upstairs' and 'walking' were loaded" | 4, p. 8 |
| Limitacion: carga estatica | "dynamic loading should be considered in future work" | 4, p. 8 |
| Limitacion: FEA en una pelvis | "only one pelvic model was performed to verify" | 4, p. 8 |
| Pelvis 4 sin canal recto | "because the S1 part of the pelvis is higher than the position" | 4, p. 8 |
| Pelvis 4 sin canal recto (2) | "thus it is impossible to generate an ISFC in the pelvis" | 4, p. 8 |
| Recto descartado en la seleccion | "The ISFC is a special case of an arc channel" | 4, p. 8 |
| Fluencia Ti-6Al-4V (citada, ref. 37) | "the yield strength of the Ti-6Al-4 V is 789–1013 Mpa" | 4, p. 9 |
| Tension maxima ISFS al caminar | "the maximum stress of the ISFS under the 'walking' load reached 1025 Mpa" | 4, p. 9 |
| Fatiga del hueso | "The fatigue strength of the bone is 37–57 Mpa" | 4, p. 9 |
| Tension sacro con IAFS al caminar | "IAFS repair reached 597.614 MPa, far exceeding the fatigue strength" | 4, p. 9 |
| Exactitud de reduccion (citada, ref. 38) | "the reduction accuracy is within 2 to 3 mm [38]" | 4, p. 10 |
| Escala de Matta (citada, ref. 39) | "excellent at 4 mm or less, good at 5–10 mm, fair at 10–20 mm" | 4, p. 10 |
| Escala de Matta: pobre | "and poor at more than 20 mm" | 4, p. 10 |
| Perforacion en arco | "able to drill out arc channels of constant-curvature in the Sawbone model" | 4, p. 10 |
| Alcance: solo S1 | "we only discussed the possibility of a IAFC through the sacrum S1" | 5, p. 10 |
| Trabajo futuro S2 | "continue to investigate whether there is a IAFC through sacrum S2" | 5, p. 10 |
| Etica | "Clinical Trial Permission No. 202009-04-01" | Ethics approval, p. 10 |
| Test no parametrico (abstract) | "The nonparametric test proved that the sacroiliac dislocation model ... was significantly different" | Abstract, p. 1 |
| Nombre del test, estadistico, p-valor | NO ENCONTRADO EN EL PDF | — |
| Umbral de CSV minimo aceptable / margen en mm | NO ENCONTRADO EN EL PDF | — |
| Diametro del tornillo en la planificacion | NO ENCONTRADO EN EL PDF (solo FEA, 7.3 mm) | — |
| Resolucion / espesor de corte del CT | NO ENCONTRADO EN EL PDF | — |
| Tasas de malposicion medidas o validacion clinica | NO ENCONTRADO EN EL PDF | — |
| Muestreo de poses o de malposicion | NO ENCONTRADO EN EL PDF | — |
| Paso de muestreo a lo largo del arco / tiempo de computo | NO ENCONTRADO EN EL PDF | — |
| Sexo / edad de las 10 pelvis | NO ENCONTRADO EN EL PDF | — |

## Candidatos de snowballing (propuestos, NO agregados a `_candidatos.md`)
| Referencia (tal como la trae el PDF) | Regla que cumple | Nota |
|---|---|---|
| [16] Q. Yang, J. Song, C. Cheng, C. Shi, C. Liang, Y. Wang, An Internal Arc Fixation Channel and Automatic Planning Algorithm for Pelvic Fracture, 2021 4th Int. Conf. Robot. Control Autom. Eng. (2021), doi:10.1109/RCAE53607.2021.9638862 | Metodo que compite (planificacion) | Ya esta en el repo como `papers/yang2022arcplanning.pdf`; falta un raw que le corresponda. Decision de la autora (#180) |
| [5] E. Gautier, K. Bächler, P.F. Heini, L.P. Nolte, Accuracy of computer-guided screw fixation of the sacroiliac joint, Clin. Orthop. Relat. Res. (2001) 310–317 | Tasa clinica de malposicion; fuente de la cifra 18% | Ya existe `refs/raw/gautier2001accuracy.nbib` (sin rastrear en git) |
| [7] C. Collinge, D. Coons, J. Aschenbrenner, Risks to the superior gluteal neurovascular bundle during percutaneous iliosacral screw insertion: an anatomical cadaver study, J. Orthop. Trauma 19 (2005) 96–101 | Fuente de la cifra 18% (cadena paralela a 2-15%) | Distinto del Collinge 2005 (254-258) citado por Zwingmann. Nivel 3 |
| [8] D. Demetriades et al., Pelvic fractures: Epidemiology and predictors of associated abdominal injuries and outcomes, J. Am. Coll. Surg. 195 (2002) 1–10 | Fuente de la cifra 18% | Probablemente epidemiologia sin malposicion; nivel 4, no perseguir salvo que se cite el 18% |
| [23] D. Wagner, L. Kamer, T. Sawaguchi, H. Noser, M. Uesugi, A. Baranowski, D. Gruszka, P.M. Rommens, Space available for trans-sacral implants to treat fractures of the pelvis assessed by virtual implant positioning, Arch. Orthop. Trauma Surg. 139 (2019) 1385–1391 | Metodo que compite (posicionamiento virtual de implantes trans-sacros en CT) | Distinto de Wagner 2017 (J Orthop Res) ya listado desde `mclaren2021corridor`. Nivel 2 |
| [22] J. Riehl, J. Widmaier, A simulator model for sacroiliac screw placement, J. Surg. Educ. 69 (2012) 282–285 | Posible: simulador de colocacion | Encaje dudoso (entrenamiento quirurgico, probablemente fisico); nivel 4 |
