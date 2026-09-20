# radzi2014metalartifacts — Artefacto de tornillos de titanio y acero en CT, 1.5T y 3T (pilon tibial)

- **DOI / URL:** 10.3978/j.issn.2223-4292.2014.03.06 — http://www.amepc.org/qims/article/view/3553/4700
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/radzi2014metalartifacts.pdf

Profundidad: texto completo (Quant Imaging Med Surg 2014;4(3):163-172, 10 pp.). Coincide con
`refs/raw/radzi2014metalartifacts.nbib`. Sin material suplementario declarado.

## Que hace (3 lineas maximo)
Inserta tres tornillos del mismo tipo en UN tobillo cadaverico humano y repite el escaneo en CT,
1.5T y 3T tras sustituir el juego por cada uno de los cuatro tipos (titanio/acero, macizo/canulado).
Reconstruye el artefacto en 3D por umbralizacion y mide, en mm, la distancia del eje del tornillo
al borde del artefacto en cuatro direcciones anatomicas.

## Restriccion o supuesto clave
No es un paper de sintesis generativa, pero su supuesto de medicion es el que importa aqui: el
artefacto se define como **una superficie cerrada segmentada por umbral** (*"3D artifact models were
reconstructed using adaptive thresholding"*, Abstract, p. 163), no como el alcance del streaking.
El valor del umbral **no se publica** (HU: NO ENCONTRADO EN EL PDF). Ademas, la referencia de la
medida es el **eje central** del tornillo, no su superficie (*"the perpendicular distance from the
central screw axis to the boundary of the artifact"*, Abstract, p. 163), asi que el numero en mm
incluye el radio del propio implante.

**Confusion de protocolo entre grupos (critica):** la MAR del fabricante se aplico solo a los
tornillos de titanio. *"O-MAR post-processing was only applied for the TA and CTA screws"* (M&M, CT,
p. 165). El contraste titanio vs acero en CT **no es un contraste de material a protocolo igual**.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Artefacto en CT, en mm (TA, SS, CTA, CSS): 2.0 / 2.6 / 1.6 / 2.0 | *"from CT were 2.0, 2.6, 1.6 and 2.0 mm"* | Resultados, p. 167 (tambien Abstract, p. 163) |
| Definicion de la medida (referencia = eje, no superficie) | *"perpendicular distance from the central screw axis to the boundary of the artifact"* | Abstract, p. 163 |
| Macizo: rosca Ø 3.5 mm, largo 40 mm | *"(thread Ø =3.5 mm, length =40 mm)"* | M&M, p. 165 |
| Canulado: rosca Ø 4.0 mm, nucleo vacio Ø 2.6 mm | *"thread Ø =4.0 mm, empty core Ø =2.6 mm, length =40 mm"* | M&M, p. 165 |
| Protocolo CT: 120 kVp, 190 mA, corte 1 mm, kernel B | *"Tube voltage of 120 kVp, X-ray tube current of 190 mA"* | M&M, CT, p. 165 |
| MAR solo en titanio (confusion de protocolo) | *"O-MAR post-processing was only applied for the TA and CTA screws"* | M&M, CT, p. 165 |
| Canulado < macizo en las tres modalidades | *"cannulated screws produced smaller artifacts compared to non-cannulated"* | Resultados, p. 167 |

## Donde entra en mi tesis
**Implicancia #57 (extension espacial del artefacto en mm).** Es la **primera fuente leida del
repositorio que publica una distancia en milimetros desde el implante hasta el borde del artefacto
en CT**. Pero la cifra NO es utilizable como calibracion de `B_delta` (~12 mm) por tres razones que
el propio PDF fija:

1. **Mide otra magnitud.** Es la distancia desde el **eje**, no desde la superficie del metal. Con
   rosca de 3.5 mm (radio 1.75 mm), un artefacto de 2.0 mm en CT deja ~0.25 mm fuera del tornillo.
   Los autores lo dicen explicitamente: tres de los cuatro casos de CT dan un artefacto *"smaller or
   of the same size"* que el radio del tornillo (Discusion, p. 167).
2. **Mide el borde de una superficie umbralizada**, no el alcance del streaking. El umbral no se
   publica y el PDF no dice si las estrias entraron o no en la segmentacion del CT (en MRI dice
   explicitamente que las estrias *"were removed as they were considered as a separate entity"*,
   Discusion, p. 169). Por eso **no refuta** `B_delta`: no mide lo que `B_delta` pretende cubrir.
3. **Anatomia y escala equivocadas** para la tesis: tobillo (pilon tibial) de UN cadaver, tornillos
   de 3.5-4.0 mm. Pelvis, sacro, iliosacro y tornillo de 7.3 mm: NO ENCONTRADO EN EL PDF.

**Mascara binaria / material.** El paper es la evidencia de que el material cambia el artefacto en
CT (2.6 mm acero frente a 2.0 mm titanio, +30%), pero **el contraste esta contaminado por la O-MAR
aplicada solo al titanio**, y el PDF **no publica ningun P especifico de titanio vs acero dentro de
CT** (la Tabla 1 solo compara modalidades). O sea: respalda que "el material importa", no cuanto.

**Canulado vs macizo.** Aqui el canulado da artefacto **menor** (1.6 vs 2.0 mm en titanio; 2.0 vs
2.6 mm en acero), pero esta confundido con el **diametro** (4.0 mm canulado frente a 3.5 mm macizo)
y con el **diseno** (*"long threaded screw"* frente a *"self-tapping locking screw"*, M&M, p. 165).
Con mayor diametro y menos artefacto, la unica explicacion coherente del PDF es el volumen de metal,
pero el paper **no lo mide ni lo modela**. Es justo la advertencia que ya traia `_candidatos.md`
(fila G3) sobre no aislar la canulacion.

## Dudas para el asesor
- ¿Vale la pena citar el 2.0/2.6 mm como cota inferior de la extension del artefacto en CT, dejando
  claro en el texto que es distancia **desde el eje** y en tobillo? Mi riesgo: que un lector lo lea
  como cota superior y concluya que `B_delta` de 12 mm esta sobredimensionada.
- La O-MAR solo en titanio invalida el contraste de material en CT. ¿Se registra como implicancia
  para `#57` o basta la advertencia en la ficha?
- No hay entrada de este paper en `refs.bib`; el raw existe (`refs/raw/radzi2014metalartifacts.nbib`).
  El alta la decide la autora (regla 9).

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Artefacto CT: TA 2.0, SS 2.6, CTA 1.6, CSS 2.0 mm | *"from CT were 2.0, 2.6, 1.6 and 2.0 mm"* | Resultados, p. 167; Abstract, p. 163 |
| Artefacto 1.5T MRI: 3.7, 10.9, 2.9, 9 mm | *"from 1.5T MRI they were 3.7, 10.9, 2.9 and 9 mm"* | Resultados, p. 167 |
| Artefacto 3T MRI: 4.4, 15.3, 3.8, 11.6 mm | *"from 3T MRI they were 4.4, 15.3, 3.8 and 11.6 mm"* | Resultados, p. 167 |
| Definicion de la metrica (eje -> borde, 4 direcciones) | *"distance between the central axis of the screw to the boundary"* | M&M, Analisis cuantitativo, p. 166 |
| Las cuatro direcciones ortogonales | *"superior, inferior, medial and lateral with respect to the distal tibia"* | M&M, p. 166 |
| Promedio de las cuatro direcciones por modelo | *"the average distance was calculated from the four directions"* | M&M, p. 166 |
| Funcion de calculo | *"the 'Curve/curve Deviation' function was used"* | M&M, p. 166 |
| Umbralizacion adaptativa como metodo de segmentacion | *"3D artifact models were reconstructed using adaptive thresholding"* | Abstract, p. 163 |
| Valor del umbral (en HU o en cualquier unidad) | NO ENCONTRADO EN EL PDF | — |
| Unidad Hounsfield / "HU" en cualquier parte del texto | NO ENCONTRADO EN EL PDF | — |
| Segmentacion basada en metodo previo | *"Based on a semi-automatic threshold method developed by Rathnayaka [2011]"* | M&M, p. 165 |
| Tornillo macizo: rosca 3.5 mm, largo 40 mm | *"(thread Ø =3.5 mm, length =40 mm)"* | M&M, p. 165 |
| Tornillo canulado: rosca 4.0 mm, nucleo 2.6 mm, largo 40 mm | *"thread Ø =4.0 mm, empty core Ø =2.6 mm, length =40 mm"* | M&M, p. 165 |
| Aleacion de titanio declarada | *"titanium alloy (TA) TiAl6Nb7 self-tapping locking screw"* | M&M, p. 165 |
| Fabricante | *"four different types of metal screws (Synthes, Oberdorf, Switzerland)"* | M&M, p. 165 |
| Diseno distinto entre macizo y canulado (confusion) | *"cannulated TA (CTA) long threaded screw"* | M&M, p. 165 |
| Composicion exacta del acero (p. ej. 316L) | NO ENCONTRADO EN EL PDF | — |
| Numero de tornillos por juego | *"Three metal screws of the same type and material were inserted"* | M&M, p. 165 |
| Diametro de las perforaciones | *"three holes were drilled with a diameter of 2.8 mm"* | M&M, p. 165 |
| Especimen: uno, mujer, 90 anos, pierna izquierda | *"The age of the specimen was 90 years old, and amputated from a left leg"* | M&M, p. 165 |
| Conservacion y descongelado | *"kept frozen at –20 ℃"* ... *"defrosted 24 hours prior"* | M&M, p. 165 |
| Incision quirurgica | *"An L-shaped incision of about 6 cm in the anterolateral approach"* | M&M, p. 165 |
| Escaner CT | *"(Philips Brilliance 256-slice CT)"* | M&M, CT, p. 165 |
| kVp y mA | *"Tube voltage of 120 kVp, X-ray tube current of 190 mA"* | M&M, CT, p. 165 |
| Grosor y espaciado de corte | *"slice thickness of 1 mm, slice spacing of 0.5 mm"* | M&M, CT, p. 165 |
| Kernel de reconstruccion | *"B convolution kernel"* | M&M, CT, p. 165 |
| Tamano de voxel | *"voxel size of 0.21 mm × 0.21 mm × 0.5 mm"* | M&M, CT, p. 165 |
| Reconstruccion iterativa en todos los CT | *"The iDose function (low dose) was used for all of the CT scans"* | M&M, CT, p. 165 |
| **MAR del fabricante solo en titanio (diferencia de protocolo)** | *"O-MAR post-processing was only applied for the TA and CTA screws"* | M&M, CT, p. 165 |
| Motivo declarado de no usar O-MAR en acero | *"screws made of steel introduced grey streaks, thus reducing ... the image quality"* | M&M, CT, p. 165 |
| Escaneres MRI | *"(Siemens Magnetom Avanto)"* 1.5T y *"(Siemens TRIO)"* 3T | M&M, MRI, p. 165 |
| Secuencia MRI | *"3D FLASH VIBE sequence"*; *"TR =11 ms, TE =1.87 ms"* | M&M, MRI, p. 165 |
| Otros parametros MRI | *"flip angle =10°, pixel bandwidth =488, FOV =120 mm × 140 mm"* | M&M, MRI, p. 165 |
| Resolucion MRI | *"slice thickness =0.5 mm ... in-plane resolution =0.5 mm × 0.5 mm"* | M&M, MRI, p. 165 |
| Software de segmentacion y de medicion | *"Amira 5.3 (VSG, France)"*; *"Rapidform 2006, INUS Technology, Korea"* | M&M, p. 165 |
| Registro entre modelos | *"Fine registration is based on the iterative closest point algorithm (ICP)"* | M&M, p. 165 |
| ROI acotada por dos superficies sobre el cuerpo del tornillo | *"two surfaces were demarcated along the body of the screw"* | M&M, p. 166 |
| Exclusion de mediciones ML por solape entre tornillos | *"the measurements in the ML direction were not included"* | M&M/Resultados, p. 167 |
| Prueba estadistica y nivel de significancia | *"A paired t-test with a two-tailed distribution"*; *"A P<0.05 was considered statistically significant"* | Analisis estadistico, p. 167 |
| P, CT vs 1.5T (Ti / acero / CTi / CAcero) | 0.005 / 0.006 / 0.001 / 0.002 | Tabla 1, p. 169 |
| P, CT vs 3T | 0.003 / 0.013 / 0.005 / 0.005 | Tabla 1, p. 169 |
| P, 1.5T vs 3T | 0.020 / 0.063 / 0.027 / 0.032 | Tabla 1, p. 169 |
| Unica comparacion no significativa | *"except 1.5T versus 3T MRI for the SS screws (P=0.063)"* | Resultados, p. 167 |
| **P de titanio vs acero DENTRO de CT** | NO ENCONTRADO EN EL PDF (la Tabla 1 solo compara modalidades) | — |
| **P de canulado vs macizo DENTRO de CT** | NO ENCONTRADO EN EL PDF | — |
| Afirmacion (sin tabla) de significancia por tipo y material | *"Significant differences (P<0.05) were found ... screw types and material types"* | Abstract, p. 163 |
| Desviaciones estandar de las cifras de CT | NO ENCONTRADO EN EL PDF (solo barras de error en Fig. 4, sin valores) | Fig. 4, p. 168 |
| Repetibilidad: valor repetido y original | *"3.2±0.3 mm"* frente a *"(2.9±0.3 mm)"* | Resultados, p. 167 |
| Repetibilidad: diferencia y P | *"small differences of 0.3 mm, but they were statistically insignificant (P=0.18)"* | Resultados, p. 167 |
| Criterio de distancia segura en CT | *"the gap ... can be about 2 mm away from each other"* | Discusion, p. 167 |
| Criterio de distancia segura en MRI | *"the gap should be at least 3 mm"* | Discusion, pp. 167-168 |
| Comparacion artefacto vs radio del tornillo (CT) | *"three (CT: TA, CTA and CSS) were found to be smaller or of the same size"* | Discusion, p. 167 |
| Direccion del efecto de canulacion | *"cannulated screws produced smaller artifacts compared to non-cannulated"* | Resultados, p. 167 |
| Orden de magnitud entre modalidades | *"artifacts generated from the 3T MRI were the largest, followed by 1.5T MRI and CT"* | Resultados, p. 167 |
| Forma no uniforme del artefacto | *"the cross sectional shape of the generated artifacts appeared non uniform"* | Resultados, p. 167 |
| Anisotropia del artefacto en CT | *"slightly elongated in the ML direction compared to the SI direction"* | Discusion, p. 168 |
| Susceptibilidad magnetica del acero | *"SS (3,520×10⁶ to 6,700×10⁶ ppm)"* | Discusion, p. 168 |
| Susceptibilidad magnetica del titanio | *"higher than titanium (182×10⁶ ppm)"* | Discusion, p. 168 |
| Ruido: iDose frente a FBP (unidad no declarada) | *"the values in iDose (9.1) were smaller than FBP (14.0)"* | Discusion, p. 169 |
| CTDI / dosis | *"Calculation of radiation doses were not included in this study"* | Discusion, p. 169 |
| Estrias de acero excluidas de la segmentacion (MRI) | *"these streaks were removed as they were considered as a separate entity"* | Discusion, p. 169 |
| Si las estrias entraron o no en la segmentacion del CT | NO ENCONTRADO EN EL PDF | — |
| Placas: piloto cualitativo, sin cifras | *"the artifacts from the plates did not extend to the articular surface"* | Discusion, p. 169 |
| Umbral clinico de malreduccion (citado de terceros) | *"restricted to less than 2 mm displacement from the original anatomical position"* | Discusion, p. 170 |
| Incongruencia articular detectable (citada de terceros) | *"an articular incongruity as small as 1 mm"* | Discusion, p. 170 |
| Duracion del protocolo MRI | *"our MRI protocol of 13 mins"* | Discusion, p. 170 |
| Limitacion: sin fractura y con pocos tornillos | *"We did not assess the size of artifacts with the presence of fractures"* | Discusion, p. 170 |
| Limitacion: artefactos se suman si hay muchos tornillos | *"the artifacts can be compounded if there are many screws located close"* | Discusion, p. 170 |
| Pelvis, sacro, iliosacro o tornillo de 7.3 mm | NO ENCONTRADO EN EL PDF | — |
| Extension del streaking en mm (separada del borde umbralizado) | NO ENCONTRADO EN EL PDF | — |
| Perfil radial o ley de decaimiento del artefacto | NO ENCONTRADO EN EL PDF | — |
| Valores de atenuacion o de intensidad del artefacto | NO ENCONTRADO EN EL PDF | — |
| Numero total de mediciones o de replicas por condicion | NO ENCONTRADO EN EL PDF | — |
| Cegamiento u observador independiente de la segmentacion | NO ENCONTRADO EN EL PDF | — |
| Kernel o reconstruccion alternativa (monoenergetica, dual-energy) | NO ENCONTRADO EN EL PDF | — |
