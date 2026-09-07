# deman2007catsim — CatSim: entorno de simulacion de CT

- **DOI / URL:** doi: 10.1117/12.710713 (Proc. of SPIE Vol. 6510, 65102G, Medical Imaging 2007: Physics of Medical Imaging)
- **Nivel de lectura:** 3 (contexto) — ver seccion "Verificacion de nivel"
- **Leido a fondo por la autora:** no
- **PDF:** papers/deman2007catsim.pdf

Profundidad: PDF completo (8 paginas, articulo de conferencia).

## Que hace (3 lineas maximo)
Presenta CatSim, entorno de simulacion de CT de rayos X de GE, construido sobre FreeMat y
orientado a modelado fisico preciso, tiempos bajos de computo y flexibilidad geometrica.
Describe el modelo directo (policromatico, ruido cuantico/electronico, scatter, dosis) y
reporta cuatro experimentos de validacion contra un escaner real y contra Monte Carlo.

## Restriccion o supuesto clave
No es un paper de sintesis generativa, pero tiene una restriccion que afecta directamente
su uso como baseline para artefactos metalicos: el simulador opera sobre objetos analiticos
y aun no soporta objetos voxelizados como entrada general. "CatSim was originally developed
to simulate analytic objects, including cylinders, ellipsoids, boxes, cones, and clipping
planes" (Sec. 2.3, p. 2) y "We are currently extending CatSim to include voxelized objects,
polygonized objects, and dynamic objects" (Sec. 2.3, p. 2). Es decir, en 2007 insertar una
geometria de implante arbitraria dentro de un volumen de CT de paciente no esta soportado
segun el propio texto. Ademas, la simulacion de scatter exige convertir a voxeles: "analytic
objects are first converted to voxelized objects in order to perform the scatter simulation"
(Sec. 2.7, p. 4).

Supuesto adicional: la fuente del espectro es externa y definida por el usuario, no derivada
en el paper — "Every CatSim simulation is based on a user-defined X-ray spectrum file" (Sec. 2.5, p. 4).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [x] baseline de comparacion
- [x] solo contexto

(Antecedente historico del baseline XCIST; el detalle reimplementable no esta aqui.)

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 50 micras (diametro alambre de tungsteno, prueba de resolucion) | "simulating and measuring a 50 micron diameter tungsten wire" | Sec. 3.1, p. 5 |
| 1% (acuerdo en frecuencias de corte MTF 10% y 50%) | "The 10% and 50% cutoff frequencies are identical to within 1%" | Sec. 3.1, p. 5 |
| 120 kV (espectro validado) | "transmission through various thicknesses of Aluminum, using a 120kV spectrum" | Sec. 3.2, p. 5 |
| R2 = 0.9993 (ajuste espectro Al) | "The results matched with R2 = 0.9993" | Sec. 4, p. 8 |
| 21.5 cm (fantoma de agua para ruido) | "simulating and measuring a 21.5cm water phantom" | Sec. 3.3, p. 6 |
| 3% (acuerdo de ruido simulacion vs medicion) | "Simulations and measurements matched to within 3%" | Sec. 4, p. 8 |
| 5% (acuerdo scatter Monte Carlo vs CatSim) | "The results matched to within 5%" | Sec. 4, p. 8 |
| 35 cm fantoma de agua, 40 mm cobertura z (prueba de scatter) | "a 35 cm water phantom for a 40mm z-coverage" | Sec. 3.4, p. 7 |
| 10 minutos para sinograma de scatter 888x984 | "Computation time is 10 minutes for a 888x984 scatter sinogram" | Sec. 3.4, p. 7 |

## Donde entra en mi tesis
Antecedente del brazo de comparacion fisico (XCIST/CatSim). Sirve para: (a) justificar en el
marco teorico que el baseline fisico tiene linaje y validacion publicada; (b) citar las cifras
de validacion del simulador (1% MTF, 3% ruido, 5% scatter, R2=0.9993) como referencia de
que precision declara la familia CatSim/XCIST; (c) documentar que el modelado explicito de
metal NO proviene de este paper. NO sirve como fuente de parametros para reimplementar.

## Dudas para el asesor
1. Si el alcance completo promete "reimplementacion validada de XCIST", la fisica reimplementable
   debe salir de wu2022xcist y del codigo, no de aqui. Confirmar que este paper queda solo como
   cita historica.
2. Las cifras de validacion (1%, 3%, 5%) son de CatSim 2007, no de XCIST. Se pueden citar como
   tolerancias esperadas del brazo fisico, o hay que re-derivarlas con la reimplementacion propia?
3. El paper no menciona metal ni artefactos metalicos. Necesitamos una fuente adicional que
   demuestre que la familia CatSim/XCIST reproduce streaking metalico, o eso queda como
   supuesto a validar experimentalmente en la tesis?

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Proposito del entorno | "We present a new simulation environment for X-ray computed tomography, called CatSim" | Abstract, p. 1 |
| Requisitos de diseno | "accurate physics modeling, low computation times, and geometrical flexibility" | Abstract, p. 1 |
| Lista de efectos fisicos modelados | "polychromaticity, realistic quantum and electronic noise models, finite focal spot size and shape" | Abstract, p. 1 |
| Lista de efectos (continuacion) | "finite detector cell size, detector cross-talk, detector lag or afterglow, bowtie filtration" | Abstract, p. 1 |
| Lista de efectos (continuacion) | "finite detector efficiency, non-linear partial volume, scatter (variance-reduced Monte Carlo), and absorbed dose" | Abstract, p. 1 |
| Modelo directo (ecuacion) | "In energy-integrating mode, CatSim models a CT acquisition by:" | Sec. 2.1, p. 1 |
| Definicion y_i | "y_i is the detector signal at sinogram index i" | Sec. 2.1, p. 1 |
| Definicion k, s | "k is the energy index, s is the beam sub-sampling index" | Sec. 2.1, p. 1 |
| Definicion A_ik | "number of photons arriving at the detector without attenuator for energy bin k" | Sec. 2.1, p. 1 |
| Definicion l_iso | "l_iso is the intersection length between the line with index is and the object" | Sec. 2.1, p. 1 |
| Definicion mu_ok (coef. atenuacion) | "mu_ok is the linear attenuation coefficient of object o at energy k" | Sec. 2.1, p. 1 |
| Definicion termino scatter | "y_i^scatter is the scatter signal computed by the scatter simulation" | Sec. 2.1, p. 1 |
| Definicion DQE | "DQE is the detector quantum efficiency (fraction of photons absorbed)" | Sec. 2.1, p. 1-2 |
| Definicion f_CONV | "f_CONV is a factor to convert from keV to a number electrons" | Sec. 2.1, p. 2 |
| Definicion sigma_electronic | "sigma_electronic is the standard deviation of the electronic noise" | Sec. 2.1, p. 2 |
| Modularidad / callbacks | "CatSim uses the notion of 'callbacks', which are user-provided scripts inserted into the processing chain" | Sec. 2.1, p. 2 |
| Plataforma base | "FreeMat is a free environment for rapid engineering and scientific prototyping" | Sec. 2.2, p. 2 |
| Licencia FreeMat | "FreeMat is available under the GPL license" | Sec. 2.2, p. 2 |
| Tipos de objeto soportados | "analytic objects, including cylinders, ellipsoids, boxes, cones, and clipping planes" | Sec. 2.3, p. 2 |
| Interseccion analitica | "The line intersections are computed in closed form." | Sec. 2.3, p. 2 |
| Limitacion declarada (voxeles) | "We are currently extending CatSim to include voxelized objects, polygonized objects, and dynamic objects." | Sec. 2.3, p. 2 |
| Fantomas mostrados | "head phantom, high-contrast resolution phantom, and thorax phantom" | Fig. 1, p. 3 |
| Ancho de haz finito | "combination of focal spot size, detector cell size, crosstalk, and azimuthal blur" | Sec. 2.4, p. 3 |
| Modelo de foco | "The focal spot is typically a 2D area in a 3D space" | Sec. 2.4, p. 3 |
| Modelo de crosstalk | "including some samples from neighboring cells to model crosstalk" | Sec. 2.4, p. 3 |
| Blur azimutal | "simulating x-rays at small angular increments and summing the signals of multiple sub-views" | Sec. 2.4, p. 3 |
| Wobble de foco | "Focal spot wobble can be modeled by dynamically moving the focal spot back and forth." | Sec. 2.4, p. 3 |
| Espectro: fuente externa | "based on a user-defined X-ray spectrum file, which can for example be downloaded from the NIST website" | Sec. 2.5, p. 4 |
| Espectro: discretizacion | "computed as the sum over a discrete number of energies, which is user defined" | Sec. 2.5, p. 4 |
| Espectro: ponderacion | "energy-weighting can be adjusted depending on the source filtration, the bowtie, and the type of detector" | Sec. 2.5, p. 4 |
| Ruido cuantico | "Quantum noise is modeled by adding Poisson noise on the transmitted x-ray flux" | Sec. 2.6, p. 4 |
| Escalado de conteos | "scaled depending on tube current, distance from the source to each detector cell, detector cell size" | Sec. 2.6, p. 4 |
| Ruido electronico | "Electronic noise is modeled by adding Gaussian noise after converting the x-ray count to electrons" | Sec. 2.6, p. 4 |
| Cuantizacion | "the electron charges are quantized to mimic the finite dynamic range in a real CT scanner" | Sec. 2.6, p. 4 |
| Modelos de scatter | "simplified sinogram-based models, as well as a ray-tracing based scatter simulation (CatScatter)" | Sec. 2.7, p. 4 |
| Scatter requiere voxeles | "analytic objects are first converted to voxelized objects in order to perform the scatter simulation" | Sec. 2.7, p. 4 |
| Dosis | "CatSim also includes a Monte Carlo dose simulation tool (CatDose), which is also based on voxelized objects" | Sec. 2.8, p. 4 |
| Mapa de dosis | "Example of an absorbed dose map for a patient thorax based on a real CT scan." | Fig. (dosis), p. 4 |
| Salida personalizada / DAS | "a simple Data Acquisition System (DAS) model can be constructed to ... match the actual raw data" | Sec. 2.9, p. 5 |
| Insercion en escaner | "it is possible to insert that simulated data onto a scanner itself using offline code" | Sec. 2.9, p. 5 |
| Validacion 1: resolucion espacial | "simulating and measuring a 50 micron diameter tungsten wire on a GE Lightspeed VCT geometry" | Sec. 3.1, p. 5 |
| Reconstruccion usada | "reconstructing using FBP with a standard reconstruction kernel" | Sec. 3.1, p. 5 |
| Criterio de acuerdo MTF | "The 10% and 50% cutoff frequencies are identical to within 1%." | Sec. 3.1, p. 5 |
| MTF50 medida en x | "x-MTF50 = 4.3826 lp/cm" | Fig. 2, p. 5 |
| MTF10 medida en x | "x-MTF10 = 7.0069 lp/cm" | Fig. 2, p. 5 |
| MTF50 medida en y | "y-MTF50 = 4.4217 lp/cm" | Fig. 2, p. 5 |
| MTF10 medida en y | "y-MTF10 = 7.0096 lp/cm" | Fig. 2, p. 5 |
| Validacion 2: espectro | "transmission through various thicknesses of Aluminum, using a 120kV spectrum" | Sec. 3.2, p. 5 |
| Juicio sobre el espectro | "The good agreement between simulations and measurements indicates that the spectrum is fairly accurate." | Sec. 3.2, p. 5 |
| Condiciones fig. atenuacion | "Attenuation in Al measured with detector 120kV, medium Bowtie" | Fig. 3, p. 6 |
| Rango de espesores Al (eje) | eje "mm Aluminum" de 0 a 20 | Fig. 3, p. 6 |
| Ajuste polinomico y R2 | "y = 0.0015x - 0.0661x + 0.96 ... R2 = 0.9993" | Fig. 3, p. 6 |
| Escaner de referencia | "measurements on a GE Lightspeed VCT scanner" | Fig. 3, p. 6 |
| Validacion 3: ruido | "simulating and measuring a 21.5cm water phantom and measuring the standard deviation of the noise" | Sec. 3.3, p. 6 |
| Variable barrida | "image noise as a function of X-ray tube current" | Sec. 3.3, p. 6 |
| Acuerdo de ruido (texto) | "Simulations and measurements agree to within a few percent." | Sec. 3.3, p. 6 |
| Condiciones fig. ruido | "Image Noise Bay 46 v.s. Catsim (QA, 0.625mm)" | Fig. 4, p. 7 |
| Rango de mA (eje) | eje "mA" de 0 a 900 (puntos ~50 a 800) | Fig. 4, p. 7 |
| Rango de ruido (eje) | eje "Image Noise" de 0 a 35 | Fig. 4, p. 7 |
| Validacion 4: scatter | "validated the scatter simulation by comparing to a full Monte Carlo method" | Sec. 3.4, p. 7 |
| Geometria del test de scatter | "a scatter profile for a 35 cm water phantom for a 40mm z-coverage" | Sec. 3.4, p. 7 |
| Ruido del Monte Carlo | "The Monte Carlo simulation is very noise since it simulates photon per photon" | Sec. 3.4, p. 7 |
| Ventaja de velocidad | "several orders of magnitude faster" | Sec. 3.4, p. 7 |
| Validacion pendiente | "Further validation using benchtop experiments are in progress." | Sec. 3.4, p. 7 |
| Tiempo de computo scatter | "Computation time is 10 minutes for a 888x984 scatter sinogram on a modern Linux PC." | Sec. 3.4, p. 7 |
| Rango eje scatter (fig) | eje vertical 0 a 0.000625; eje horizontal 1 a 888 | Fig. 5, p. 8 |
| Resumen de validacion | "We have validated the noise, spectral and spatial resolution characteristics, and shown scatter and dose simulations." | Sec. 4, p. 8 |
| Cifra de acuerdo, ruido | "Simulations and measurements matched to within 3%." | Sec. 4, p. 8 |
| Cifra de acuerdo, resolucion | "Simulations and measurements matched to within 1%." | Sec. 4, p. 8 |
| Cifra de acuerdo, espectro | "The results matched with R2 = 0.9993." | Sec. 4, p. 8 |
| Cifra de acuerdo, scatter | "The results matched to within 5%." | Sec. 4, p. 8 |
| Estado de validacion de dosis | "The results are visually acceptable; numerical validation is in progress." | Sec. 4, p. 8 |
| Trabajo futuro | "We plan to add dynamic objects, polygonized objects, and voxelized objects." | Sec. 4, p. 8 |
| Beam hardening (termino) | NO ENCONTRADO EN EL PDF | — |
| Photon starvation (termino) | NO ENCONTRADO EN EL PDF | — |
| Artefacto metalico / metal artifact | NO ENCONTRADO EN EL PDF | — |
| Valores numericos de mu para metales | NO ENCONTRADO EN EL PDF | — |
| Distancias fuente-isocentro / fuente-detector | NO ENCONTRADO EN EL PDF | — |
| Numero de canales y filas del detector | NO ENCONTRADO EN EL PDF | — |
| Numero de vistas por rotacion | NO ENCONTRADO EN EL PDF | — |
| Tamano de celda de detector en mm | NO ENCONTRADO EN EL PDF | — |
| Tamano de foco en mm | NO ENCONTRADO EN EL PDF | — |
| Filtracion / material y espesor del bowtie | NO ENCONTRADO EN EL PDF | — |
| Numero de bins de energia usados | NO ENCONTRADO EN EL PDF | — |
| Valor de sigma_electronic | NO ENCONTRADO EN EL PDF | — |
| Valor de DQE | NO ENCONTRADO EN EL PDF | — |
| Lista de referencias bibliograficas | NO ENCONTRADO EN EL PDF (el articulo no incluye seccion de referencias) | — |

## Verificacion de nivel

Criterio de la autora: Nivel 1 = critico, si se equivoca aqui se cae una tesis o el benchmark.
Nivel 2 = afecta la redaccion. Nivel 3 = apoyo.
Clasificacion previa: NIVEL 2, promovido desde nivel 3 sin leer el PDF, con la justificacion
"reimplementar un simulador exige su fisica, no solo su paper mas nuevo".

**1. Que fisica modela explicitamente**

| Fenomeno | Aparece? | Frase original |
|---|---|---|
| Espectro policromatico | Si | "CatSim incorporates polychromaticity" (Abstract, p. 1); "sum over a discrete number of energies" (Sec. 2.5, p. 4) |
| Ruido cuantico (Poisson) | Si | "Quantum noise is modeled by adding Poisson noise on the transmitted x-ray flux" (Sec. 2.6, p. 4) |
| Ruido electronico (Gaussiano) | Si | "adding Gaussian noise after converting the x-ray count to electrons" (Sec. 2.6, p. 4) |
| Cuantizacion / rango dinamico | Si | "electron charges are quantized to mimic the finite dynamic range" (Sec. 2.6, p. 4) |
| Scatter | Si | "Several X-ray scatter models are included in CatSim" (Sec. 2.7, p. 4) |
| Scatter Monte Carlo de varianza reducida | Si | "scatter (variance-reduced Monte Carlo)" (Abstract, p. 1) |
| Volumen parcial no lineal | Si | "non-linear partial volume" (Abstract, p. 1) |
| Eficiencia finita del detector (DQE) | Si | "DQE is the detector quantum efficiency (fraction of photons absorbed)" (Sec. 2.1, p. 1-2) |
| Foco finito, crosstalk, lag/afterglow, bowtie | Si | "finite focal spot size and shape, detector cross-talk, detector lag or afterglow, bowtie filtration" (Abstract, p. 1) |
| Dosis absorbida | Si | "Monte Carlo dose simulation tool (CatDose)" (Sec. 2.8, p. 4) |
| **Beam hardening** | **No, no se nombra** | NO ENCONTRADO EN EL PDF. El termino no aparece; solo aparece policromaticidad, que es su condicion previa, y una validacion de transmision en Al a 120 kV (Sec. 3.2, p. 5) |
| **Photon starvation** | **No** | NO ENCONTRADO EN EL PDF |
| **Endurecimiento por metal / streaking** | **No** | NO ENCONTRADO EN EL PDF |

**2. Modela metal de forma explicita? Seccion o figura dedicada a artefactos metalicos?**

No. NO ENCONTRADO EN EL PDF una seccion, figura o parrafo dedicado a metal o a artefactos
metalicos. Las unicas apariciones de un material metalico son instrumentales, no de artefacto:
- "a 50 micron diameter tungsten wire" (Sec. 3.1, p. 5), usado como objeto puntual para medir MTF.
- "various thicknesses of Aluminum, using a 120kV spectrum" (Sec. 3.2, p. 5), usado para validar el espectro.

La Fig. 1 (p. 3) muestra un fantoma de cabeza tipo Forbild en el que visualmente se aprecian
estrias, pero el pie de figura solo dice "head phantom, high-contrast resolution phantom, and
thorax phantom"; el texto no atribuye esas estrias a metal ni discute artefactos. No se debe
citar esa figura como evidencia de simulacion de artefacto metalico.

**3. Parametros numericos concretos para reimplementar**

Insuficientes. Lo que si aparece: espectro de 120 kV con "medium Bowtie" (Fig. 3, p. 6);
geometria nombrada pero no cuantificada, "a GE Lightspeed VCT geometry" (Sec. 3.1, p. 5);
espesor de corte 0.625 mm en la prueba de ruido (Fig. 4, p. 7); tamano de sinograma de scatter
888x984 (Sec. 3.4, p. 7); fantomas de 21.5 cm y 35 cm de agua y cobertura z de 40 mm; alambre
de tungsteno de 50 micras; corriente de tubo barrida hasta ~800 mA (Fig. 4, p. 7).

Lo que falta y seria imprescindible para reimplementar: distancias fuente-isocentro y
fuente-detector, numero de canales/filas, tamano de celda de detector, numero de vistas,
tamano de foco, material y perfil del bowtie, numero de bins de energia, sigma_electronic,
DQE, f_CONV, y cualquier coeficiente de atenuacion tabulado. Todos ellos: NO ENCONTRADO EN EL PDF.
El paper delega los coeficientes y el espectro a una fuente externa (NIST) en vez de tabularlos
(Sec. 2.5, p. 4).

**4. Como valida el simulador contra datos reales? Metrica y cifra**

Cuatro validaciones, tres contra un escaner real (GE Lightspeed VCT / "Bay 46") y una contra
Monte Carlo:

| Prueba | Objeto | Metrica | Cifra |
|---|---|---|---|
| Resolucion espacial | alambre de tungsteno 50 micras | frecuencias de corte MTF 10% y 50% | "identical to within 1%" (Sec. 3.1, p. 5) |
| Espectro | espesores de Al, 120 kV | R2 del ajuste senal vs espesor | "R2 = 0.9993" (Fig. 3, p. 6; Sec. 4, p. 8) |
| Ruido de imagen | fantoma de agua 21.5 cm | desv. estandar del ruido central vs mA | "agree to within a few percent" (Sec. 3.3, p. 6); "to within 3%" (Sec. 4, p. 8) |
| Scatter | fantoma de agua 35 cm, 40 mm z | perfil de scatter vs Monte Carlo completo | "matched to within 5%" (Sec. 4, p. 8) |
| Dosis | torax de CT real | ninguna metrica numerica | "visually acceptable; numerical validation is in progress" (Sec. 4, p. 8) |

Ninguna validacion involucra metal, artefactos, ni HU de imagen reconstruida en presencia de
un implante.

**5. Hay detalle de implementacion que NO estaria en wu2022xcist?**

Lo unico con valor de implementacion propio es la ecuacion del modelo directo de la Sec. 2.1
(p. 1) con la definicion de cada termino (A_ik, l_iso, mu_ok, DQE, f_CONV, sigma_electronic,
y_i^scatter), el mecanismo de "callbacks" (Sec. 2.1, p. 2), y la dependencia de FreeMat
(Sec. 2.2, p. 2) — esta ultima es historica y esta obsoleta frente a XCIST en Python.

Fuera de eso, **el paper es una descripcion de alto nivel del entorno**: enumera efectos
modelados sin dar sus formulas ni sus parametros, y remite a recursos externos para espectro
y coeficientes de atenuacion. No contiene la fisica en detalle reimplementable. Si la
comparacion contra wu2022xcist se hizo o no, no se puede establecer desde este PDF.

**6. Nivel que sostiene la evidencia: 3**

Nivel 3. Es un paper de presentacion de software: enumera los efectos fisicos y reporta
validaciones agregadas, pero no aporta ni las ecuaciones detalladas, ni los parametros de
geometria, ni tratamiento alguno de metal, que es justo lo que el brazo de comparacion de
MetalSynth-Pelvis necesita. La justificacion de promocion a nivel 2 ("reimplementar un
simulador exige su fisica") es correcta como principio pero no se cumple en este PDF: la
fisica reimplementable no esta aqui. Recomendacion: revertir a nivel 3, rol "antecedente
historico del baseline", y mantener wu2022xcist como la unica fuente nivel 1 del baseline
fisico. Valor residual citable: las cuatro cifras de validacion (1%, 3%, 5%, R2=0.9993) y la
limitacion documentada de objetos analiticos vs voxelizados.

## Candidatos de snowballing detectados

El articulo **no incluye seccion de referencias bibliograficas**. Solo cita tres recursos
externos mediante URL en el cuerpo del texto:

| Cita como aparece | Por que podria importar |
|---|---|
| "downloaded from the NIST website http://physics.nist.gov/PhysRefData/XrayMassCoef/tab3.html" (Sec. 2.5, p. 4) | Fuente original de los coeficientes de atenuacion masica por energia. Es exactamente la tabla que haria falta para asignar mu(E) al titanio o acero inoxidable del implante en un renderizador fisico o en la validacion del render por difusion. No es un paper, es una base de datos. |
| "More details on the Forbild phantoms is found on the Forbild website http://www.imp.uni-erlangen.de/forbild/english/forbild/" (Sec. 2.3, p. 2) | Definicion original de los fantomas analiticos usados como objeto de prueba estandar. Relevante solo si se quiere un fantoma de referencia comparable entre el brazo fisico y el brazo generativo. Prioridad baja. |
| "FreeMat ... can be downloaded from http://freemat.sourceforge.net/" (Sec. 2.2, p. 2) | Plataforma de ejecucion de CatSim en 2007. Obsoleta frente a XCIST/Python. No es candidato util. |

Ninguno de los tres cumple con ser "metodo que compite con el renderizador" ni "metrica que
valida el realismo de artefactos". El unico con valor real es la tabla NIST, y es un recurso
de datos, no una referencia bibliografica citable en el sentido de `_candidatos.md`.

Papers candidatos propiamente dichos: ninguno.
