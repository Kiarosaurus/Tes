# wu2022xcist — XCIST: toolkit abierto de simulacion X-ray/CT

- **DOI / URL:** 10.1088/1361-6560/ac9174 (Phys Med Biol 67(19); manuscrito de autor HHS Public Access, PMC 2023-09-28)
- **Nivel de lectura:** 2 (vigente desde 2026-09-07; lectura profunda previa conservada)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wu2022xcist.pdf

Profundidad: texto completo del manuscrito de autor (paginas 1-36, incluye Tablas 1-6 y Figuras 1-11). El material suplementario (S1-S14) esta referenciado pero NO incluido en el PDF.

**Actualización de uso, 2026-09-07:** tras adoptar Peters, esta fuente queda en N2
para fundamento técnico y limitaciones de XCIST. No se usa como validación autónoma
de artefactos metálicos ni como configuración sustitutiva de Peters. Los análisis
de N1 y reimplementación más abajo corresponden al encuadre anterior; se conservan
como historial de la lectura, no como decisión vigente. Ver `_index.md` y #17.

## Que hace (3 lineas maximo)
Presenta XCIST, un entorno abierto de simulacion X-ray/CT en Python + C/C++ que reune fantomas digitales, el simulador CatSim reimplementado y algoritmos de reconstruccion.
Describe los modelos fisicos (espectro, foco, dispersion analitica, deteccion con DQE y ruido electronico) y publica tablas de parametros por defecto y por experimento.
Demuestra cuatro experimentos: exactitud geometrica/atenuacion, vistas por rotacion vs mAs, tamano de foco/celda de detector, y causas raiz de artefactos (aliasing, endurecimiento de haz, scatter, ruido).

## Restriccion o supuesto clave
No es un paper de sintesis generativa, pero su restriccion operativa para MetalSynth-Pelvis es que trabaja hacia adelante desde un fantoma: para usar imagenes ya reconstruidas hay que convertirlas primero en fantoma voxelizado asignando materiales por numero CT ("Voxelized phantoms can be produced from patient images by assigning a material [...] based on its CT number", Methods/Phantoms, p.5) y luego re-simular proyecciones y reconstruir. No opera sobre la imagen reconstruida in situ. Ademas, la validacion del propio toolkit se declara preliminar: "The results presented in this report represent a qualitative and semi-quantitative first-order evaluation" (Validation, p.9).

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Distancia fuente-isocentro 540 mm; fuente-detector 950 mm | "Source-to-isocenter distance (mm) [...] 540 / 950" | Tabla 2, p.31 |
| 900 columnas x 16 filas de detector; columna 0.25 mm, fila 1 mm | "detector column count 900 [...] detector column width (mm) 0.25" | Tabla 2, p.31 |
| 1000 vistas por rotacion por defecto | "views/rotation 1000" | Tabla 2, p.31 |
| Espectro 120 kVp, anodo W 7 grados; filtro Al 3.0 mm; bowtie large | "X-ray spectrum 120 kVp, 7 W anode" | Tabla 2, p.31 |
| 20 bins de energia por defecto | "number of energy bins 20" | Tabla 2, p.31 |
| Ruido electronico por defecto 3500 e-; ganancia 17 e-/keV | "electronic noise (st. dev., e-) 3500" | Tabla 2, p.31 |
| Fantoma de metal: Ti 20 mm y Fe 10 mm de diametro | "20-mm-diameter titanium [...] 10-mm-diameter iron" | Figura 11, p.29 |
| Materiales del fantoma del experimento 4: agua, hueso, Ti, Fe | "phantom materials water, bone, Ti, Fe" | Tabla 6, p.36 |
| Aire simulado -995 HU vs -1000 HU esperado | "air (-995 HU versus -1000 HU by definition)" | Discussion Exp.1, p.13 |
| Hueso simulado 1551 HU vs 1552 HU calculado | "expected value for bone (calculated as 1552 HU, simulated as 1551 HU)" | Discussion Exp.1, p.13 |
| Desviaciones estandar 9.8 HU (aire) y 11.8 HU (agua) | "Standard deviations for the air and water regions are 9.8 HU and 11.8 HU" | Results Exp.1, p.11 |
| Se requieren ~1000 o mas vistas/rotacion para suprimir aliasing | "about 1000 or more V/R are required to suppress view aliasing" | Discussion Exp.4, p.15 |
| Espectros precalculados 80 kV a 140 kV en pasos de 10 kV | "7 precalculated spectra: 7-degree takeoff angle, 80 kV to 140 kV" | Tabla 1, p.30 |
| Tiempo de computo: minutos en PC con 12 nucleos CPU | "take a few minutes on a PC with 12 CPU-cores" | Simulation, p.7 |

## Donde entra en mi tesis
Capitulo de metodos, brazo de comparacion fisico frente al renderizador LDM 2.5D + ControlNet: es la fuente de los parametros de geometria, espectro, deteccion y reconstruccion que habria que reimplementar. Tambien alimenta la discusion sobre validacion (Fig. 11 es la unica evidencia de metal, y es cualitativa) y la seccion de limitaciones del baseline.

## Dudas para el asesor
- Si XCIST solo demuestra metal con dos varillas cilindricas (Ti 20 mm, Fe 10 mm) en un fantoma analitico y sin metrica cuantitativa de artefacto, alcanza para llamarlo "baseline fisico validado" o hay que rebajarlo a "referencia fisica cualitativa"?
- La ruta imagen reconstruida -> fantoma voxelizado por numero CT -> re-simulacion introduce un doble ciclo de reconstruccion sobre CTPelvic1K. Es aceptable como comparador, o sesga la comparacion contra el renderizador?
- El PDF no declara licencia del repositorio ni soporte GPU. Se busca esa informacion fuera del paper (fuera de mi alcance como extractor) o se deja como riesgo abierto?

## Evidencia textual

| Dato / umbral / criterio | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| Lenguajes del toolkit | "XCIST code is a hybrid of Python and C/C++" | Software environment, p.4 |
| Operaciones intensivas en C/C++ | "projection and backprojection operations are performed in C/C++" | Software environment, p.4 |
| Repositorio | "All code is maintained as an open-access project on GitHub (github.com/xcist)" | Software environment, p.4 |
| Repositorio (repetido en conclusion) | "publicly available as an open-source project at github.com/xcist" | Conclusion, p.16 |
| Wiki de documentacion | "github.com/xcist/documentation/wiki" | Software environment, p.4; Documentation, p.9 |
| Relacion con CatSim | "image simulation components of XCIST are a new implementation of CatSim" | Simulation, p.6 |
| CatSim previo en Matlab | "developed over the past two decades and previously implemented in Matlab" | Simulation, p.6 |
| Subconjuntos de XCIST | "three major subsets: digital phantoms, the simulator itself (CatSim), and image reconstruction algorithms" | Abstract, p.1 |
| Cuatro subconjuntos (version del cuerpo) | "digital phantoms, projection simulation, reconstruction algorithms, and a (future) dose estimation tool" | Introduction, p.3 |
| Materiales predefinidos (texto) | "At least 161 materials are pre-defined, including 92 elements, 29 compounds and mixtures" | Materials, p.5 |
| Materiales predefinidos (tabla; discrepa con el texto) | "Materials 194 pre-defined" | Tabla 1, p.30 |
| Tejidos biologicos incluidos | "40 biological tissues" | Materials, p.5 |
| Composicion de tejidos XCAT | "elemental composition and density as given by ICRU Report 46" | Phantoms, p.5 |
| Tipos de fantoma soportados | "XCIST currently supports analytic, voxelized, and NURBS-format phantoms" | Phantoms, p.5 |
| Fantomas poligonales | "support for polygonal phantoms will be included in a future release" | Phantoms, p.5 |
| Fantoma desde imagen de paciente | "Voxelized phantoms can be produced from patient images by assigning a material" | Phantoms, p.5 |
| Criterio de asignacion de material | "to each voxel based on its CT number" | Phantoms, p.5 |
| Parametros fundamentales de una simulacion | "source-to-isocenter distance, source-to-detector distance, number of detector columns and rows" | Simulation, p.6 |
| Protocolo de escaneo | "tube voltage, tube current, helical pitch, and rotation time" | Simulation, p.6 |
| Modelo de foco | "CatSim supports a user-defined 3-D finite focal spot" | Simulation, p.6 |
| Modelo de espectro | "can be based on a well-validated spectrum model (FitzGerald et al., 2021)" | Simulation, p.6 |
| Espectros definidos por el usuario | "Alternatively, user-defined X-ray spectrum files can be used" | Simulation, p.6 |
| Secciones eficaces | "cross-section data files [...] are obtained from GEANT4 (Agostinelli et al., 2003)" | Simulation, pp.6-7 |
| Ecuacion de scatter (dada explicitamente) | "S_ik = [(C * A_i * (-log(A_ik / I_air,i))) * H] * w_k" | Simulation, p.7 |
| Origen del modelo de scatter | "analytical convolution-based scatter model is used, inspired by (Ohnesorge, Flohr and Klingenbeck-Regn, 1999)" | Simulation, p.7 |
| Calibracion del scatter | "C is tuned based on scatter measurements, H and w are calculated by Monte Carlo simulation" | Simulation, p.7 |
| Ecuacion de deteccion (dada explicitamente) | "y_i = [Sum_k E_k * Poisson(DQE_ik * (A_ik + S_ik))] * f_conv + Normal(sigma_electronic)" | Simulation, p.7 |
| Que debe especificar el usuario en deteccion | "the user specifies the detector geometry, the scintillator material, the light gain factor" | Simulation, p.7 |
| Ruido electronico como parametro de usuario | "and the electronic noise standard deviation" | Simulation, p.7 |
| Tipo de detector soportado | "CatSim can currently simulate conventional scintillator-type detectors [...] energy integration mode" | Simulation, p.7 |
| Detectores de conteo de fotones | "photon-counting detector models will be included in a future release" | Simulation, p.7 |
| Crosstalk | "modeled as a fraction of the signal being shared with neighboring detector cells" | Simulation, p.7 |
| Tiempo de computo | "take a few minutes on a PC with 12 CPU-cores" | Simulation, p.7 |
| Rango de tiempos de simulacion | "simulation times can range from seconds to hours, depending on the level of detail" | Simulation, pp.7-8 |
| Algoritmo de reconstruccion | "Tang's 3D weighting algorithm (Tang et al., 2006) is an improved version" | Reconstruction, p.8 |
| Kernels de reconstruccion | "a few sample reconstruction kernels including 'soft', 'standard', and 'bone'" | Reconstruction, p.8 |
| Ponderacion de short scan | "Parker weighting (Parker, 1982) is used for short-scan simulations" | Reconstruction, p.8 |
| Reconstruccion usada en los experimentos | "Three-dimensional (3D) FDK cone-beam reconstruction was used" | Experiments, p.10 |
| Estado de la validacion | "qualitative and semi-quantitative first-order evaluation of XCIST's basic capabilities" | Validation, p.9 |
| Validacion futura | "More thorough and rigorous evaluation is planned to validate all of XCIST's features" | Validation, p.9 |
| Escaner de referencia para validacion | "we chose a LightSpeed VCT (GE Healthcare) because low-level specifications are available" | Validation, p.9 |
| Rango validado del modelo de espectro | "validated our spectrum model [...] over the range of 80 kV to 140 kV" | Validation, p.9 |
| Cobertura longitudinal del escaner de referencia | "64-detector-row scanners with 4-cm longitudinal coverage" | Validation, p.9 |
| Validacion de dosis vs Monte Carlo (sin cifras) | "Dose estimates using our method agreed well with GEANT4 estimates of dose" | Dose estimation, p.9 |
| Validacion de ruido y resolucion pendiente | "Validation of the noise and resolution modeling capability is in progress" | Conclusion, p.16 |
| Exactitud del agua | "in precise agreement with the expected value for water (defined as 0 HU, simulated as 0 HU)" | Discussion Exp.1, p.13 |
| Exactitud del aire | "air (-995 HU versus -1000 HU by definition)" | Discussion Exp.1, p.13 |
| Exactitud del hueso | "bone (calculated as 1552 HU, simulated as 1551 HU)" | Discussion Exp.1, p.13 |
| Desviaciones estandar aire/agua | "Standard deviations for the air and water regions are 9.8 HU and 11.8 HU" | Results Exp.1, p.11 |
| Diametro de la imagen simulada Exp.1 | "the diameter of simulated/reconstructed image, 256 mm" | Figura 8, p.26 |
| Umbral de visualizacion aire | "Gray regions represent air (ranging from -1100 to -900 HU, mode = -995 HU)" | Figura 8, p.26 |
| Umbral de visualizacion agua | "gray regions represent water (ranging from -100 HU to 100 HU, mode = 0 HU)" | Figura 8, p.26 |
| Umbral de visualizacion hueso | "gray regions represent bone (greater than 1200 HU, mode = 1551 HU)" | Figura 8, p.26 |
| Metrica de calidad de imagen usada | "calculating the pixelwise root mean square error (RMSE) versus an ideal image" | Experiments Exp.2, p.10 |
| Definicion del ideal para la RMSE | "an ideal image (without noise or aliasing) in a selected ROI in soft tissue" | Experiments Exp.2, p.10 |
| Barrido de vistas por rotacion Exp.2 | "varied the number of V/R from 128 V/R to 1024 V/R in 2X steps" | Experiments Exp.2, p.10 |
| Corrientes de tubo Exp.2 | "setting the X-ray-tube current to 16 mA, 100 mA, or 500 mA" | Experiments Exp.2, p.10 |
| Ruido electronico forzado en Exp.2 | "we set the electronic noise to 20,000" | Experiments Exp.2, p.10 |
| Equivalencia del ruido electronico | "which is equivalent to approximately 20 X-rays for the detector model used" | Experiments Exp.2, p.10 |
| Mejor calidad a 16 mAs | "the best IQ is achieved at only 256 V/R" | Results Exp.2, p.12 |
| Mejor calidad a 500 mAs | "best IQ is achieved with 1024 V/R" | Results Exp.2, p.12 |
| Mejor calidad a 100 mAs | "at 100 mAs, RSME results indicate that the best image quality is achieved when using 512 V/R" | Discussion Exp.2, p.14 |
| Valores RMSE reportados (rejilla mAs x V/R) | "149 HU / 120 HU / 124 HU / 213 HU ... 115 HU / 50 HU / 22 HU / 17 HU" | Figura 9, p.27 |
| Ventana de visualizacion Fig.9 | "window width = 400 HU, window level = -150 HU" | Figura 9, p.27 |
| Tamanos de foco Exp.3 | "we used 0.25-mm and 4-mm FS widths" | Experiments Exp.3, p.10 |
| Anchos de columna de detector Exp.3 | "detector column widths of 0.25 mm, 1 mm, and 2 mm" | Experiments Exp.3, p.10 |
| FOV Exp.3 | "a 260-mm FOV reconstruction shows the entire head cross-section" | Figura 10, p.28 |
| ROI Exp.3 | "The yellow box indicates a 60-mm region of interest" | Figura 10, p.28 |
| Ventana de visualizacion Fig.10 | "window width = 1000 HU, window level = 0 HU" | Figura 10, p.28 |
| Condicion ideal Exp.4 | "large number of V/R, a monoenergetic spectrum, and no simulated scatter or noise" | Experiments Exp.4, p.11 |
| Aliasing forzado Exp.4.2 | "we reduced the number of views per rotation" (360 V/R en Tabla 6) | Experiments Exp.4, p.11; Tabla 6, p.36 |
| Endurecimiento de haz Exp.4.3 | "To demonstrate the effects of beam hardening, we used a poly-energetic spectrum" | Experiments Exp.4, p.11 |
| Espectro policromatico usado | "a realistic polyenergetic spectrum (i.e., 120 kVp), beam hardening artifacts result" | Results Exp.4, p.13 |
| Espectro monocromatico base Exp.4 | "monoenergetic spectrum? 88 keV" | Tabla 6, p.36 |
| Fantoma analitico Exp.4: agua | "200-mm x 300-mm water" | Figura 11, p.29 |
| Fantoma analitico Exp.4: hueso | "40-mm-diameter bone" | Figura 11, p.29 |
| Fantoma analitico Exp.4: titanio | "20-mm-diameter titanium" | Figura 11, p.29 |
| Fantoma analitico Exp.4: hierro | "10-mm-diameter iron" | Figura 11, p.29 |
| Streaks entre varillas de metal | "the streaks between the two metal rods in the noise-only image" | Discussion Exp.4, p.15 |
| Umbral de vistas para suprimir aliasing | "about 1000 or more V/R are required to suppress view aliasing" | Discussion Exp.4, p.15 |
| Indistinguibilidad scatter / beam hardening | "difficult or impossible to discern the difference between beam hardening and scatter" | Discussion Exp.4, p.15 |
| Correcciones por defecto desactivadas | "post-log maximum off / beam-hardening correction off" | Tabla 2, p.31 |
| Correccion de endurecimiento disponible | "Water beam-hardening correction" (categoria Prep) | Tabla 1, p.30 |
| Trayectoria de escaneo disponible | "Helical (axial with table speed = 0)" | Tabla 1, p.30 |
| Detector disponible vs planeado | "Detector: Third generation, curved / Planned: Flat" | Tabla 1, p.30 |
| Reconstruccion iterativa: planeada, no disponible | "Planned features: Helical FDK, Iterative reconstruction" | Tabla 1, p.30 |
| Estimacion de dosis: planeada, no disponible | "Dose estimation [...] Planned features: Kernel-based method" | Tabla 1, p.30 |
| Bowtie disponibles | "Bowtie filters: Large, medium, small" | Tabla 1, p.30 |
| Formatos de salida | "Output files are in the users' choice of DICOM or simple binary format" | Software environment, p.4 |
| Recon por defecto | "recon algorithm FDK equiangular / recon kernel standard / recon unit Hounsfield units (HU)" | Tabla 2, p.32 |
| LAC de agua por defecto | "water LAC (mu, mm-1) 0.02" | Tabla 2, p.32 |
| FOV y matriz por defecto | "field of view (FOV, mm) 500 / XY matrix size (X & Y pixels) 512" | Tabla 2, p.31 |
| Financiamiento | "Award Numbers U01CA231860 and R01EB001838" | Acknowledgements, p.16 |
| Licencia del codigo | NO ENCONTRADO EN EL PDF | — |
| Soporte GPU de XCIST | NO ENCONTRADO EN EL PDF (solo se menciona GPU para Monte Carlo de terceros) | — |
| Limitacion sobre objetos metalicos grandes / distorsion de sinograma con metal | NO ENCONTRADO EN EL PDF | — |
| Metrica cuantitativa de artefacto metalico | NO ENCONTRADO EN EL PDF | — |
| Validacion contra datos reales de paciente con implantes | NO ENCONTRADO EN EL PDF | — |

## Verificacion de nivel

Este paper esta en NIVEL 1, asignado por la autora, con el rol "baseline fisico".

**1. CRITICO — Modela metal y artefactos metalicos de forma explicita?**

SI modela metal como material, pero NO hay ninguna seccion, metrica ni experimento dedicado al artefacto metalico como tal. El metal aparece unicamente como dos varillas dentro del fantoma analitico del Experimento 4, cuyo objetivo declarado es otro: "Evaluate the effects of view aliasing, beam hardening, X-ray scatter, and electronic and quantum noise" (Experiments, p.10-11). La evidencia de metal es:
- Figura 11 (p.29): "20-mm-diameter titanium" y "10-mm-diameter iron", dentro de "200-mm x 300-mm water", con "40-mm-diameter bone".
- Tabla 6 (p.36): "phantom materials water, bone, Ti, Fe".
- Discussion Exp.4 (p.15): "the streaks between the two metal rods in the noise-only image".
- Results Exp.4 (p.13): "a realistic polyenergetic spectrum (i.e., 120 kVp), beam hardening artifacts result".

Con todas las letras: **el paper NO contiene un estudio de artefacto metalico**. No usa la expresion "metal artifact", no reporta ninguna metrica de artefacto metalico, no compara contra adquisiciones reales con implantes, y no evalua correccion de artefacto metalico (MAR). El streaking entre las varillas se comenta cualitativamente y se atribuye al ruido electronico, no a un modelo especifico de metal. La unica correccion listada es "Water beam-hardening correction" (Tabla 1, p.30), es decir basada en agua, no en metal.

**2. CRITICO — Trae parametros y ecuaciones para reimplementarlo?**

En buena medida SI. Esto ATENUA la implicancia #8 respecto de lo que dejo deman2007.

Lo que SI da (Tabla 2, pp.31-32, mas Tablas 3-6, pp.33-36):
- Geometria fuente-detector: "Source-to-isocenter distance (mm) 540" y SDD "950".
- Geometria de fuente: "source target angle (degrees) 7", "focal spot type uniform", "focal spot width (mm) 1", "focal spot length (z)(mm) 1".
- Celdas de detector: "detector geometry type third generation, curved", "detector row count 16", "detector column count 900", "Detector column offset (columns) 0.25" [tal como aparece en la tabla], "detector column width (mm) 1", "detector row height (z)(mm) 1". (La tabla presenta los valores en columna y la asignacion exacta columna-a-valor es ambigua en el manuscrito de autor; los valores del bloque son 900 / 0.25 / 1 / 1.)
- Numero de vistas: "views/rotation 1000" (por defecto); barridos de 128 a 4000 en los experimentos.
- Espectro: "X-ray spectrum 120 kVp, 7 W anode"; libreria "7 precalculated spectra: 7-degree takeoff angle, 80 kV to 140 kV in 10-kV steps" (Tabla 1, p.30).
- Prefiltro: "X-ray source filter material aluminum", "X-ray source filter thickness (mm) 3.0".
- Bowtie: "bowtie filter large"; opciones "Large, medium, small" (Tabla 1, p.30).
- Bins de energia: "number of energy bins 20".
- Deteccion / DQE: la ecuacion explicita "y_i = [Sum_k E_k * Poisson(DQE_ik * (A_ik + S_ik))] * f_conv + Normal(sigma_electronic)" (p.7), mas "detector material Lumex", "detector depth (mm) 3", "detector type detector gain (e-/keV) 17", "detector column fill fraction 0.9", "detector row fill fraction 0.9".
- Ruido electronico: "electronic noise (st. dev., e-) 3500" por defecto; "20,000" forzado en el Experimento 2.
- Scatter: ecuacion explicita "S_ik = [(C * A_i * (-log(A_ik / I_air,i))) * H] * w_k" (p.7).
- Protocolo y reconstruccion: "rotation time (s) 1.0", "patient table speed (mm/s) 0.0", "X-ray-tube current (mA) 200", "field of view (FOV, mm) 500", "XY matrix size 512", "recon algorithm FDK equiangular", "recon kernel standard", "water LAC (mu, mm-1) 0.02".

Lo que NO da:
- Los valores numericos de C, H y w del modelo de scatter: solo dice "C is tuned based on scatter measurements, H and w are calculated by Monte Carlo simulation" (p.7). NO ENCONTRADO EN EL PDF.
- La curva DQE_ik como funcion de la energia: se declara como termino de la ecuacion pero sin tabla ni formula. NO ENCONTRADO EN EL PDF.
- El perfil geometrico del bowtie ("Bowtie DAT" en Figura 4, p.22, es un archivo externo). Valores: NO ENCONTRADO EN EL PDF.
- Los espectros numericos: se remiten a FitzGerald et al. 2021 y al archivo "Spectrum DAT". NO ENCONTRADO EN EL PDF.
- El detalle de la asignacion numero-CT -> material para fantomas voxelizados. NO ENCONTRADO EN EL PDF.
- Los archivos suplementarios S1-S14 (fantomas, especificaciones), citados repetidamente en las Tablas 2-6, no estan en este PDF: "Refer to Web version on PubMed Central for supplementary material" (p.16).
- Cualquier parametro especifico de metal (composicion exacta de Ti/Fe usada, densidad, longitud de las varillas). NO ENCONTRADO EN EL PDF.

Efecto sobre la implicancia #8: **se atenua, no se cierra**. Hay suficiente para reimplementar un simulador CT generico con geometria y espectro plausibles; NO hay suficiente para reclamar una "reimplementacion validada" con metal, porque faltan la calibracion del scatter, la DQE, el bowtie, y toda validacion con metal.

**3. Puede operar sobre imagenes CT ya reconstruidas (CTPelvic1K) o exige datos crudos?**

No exige proyecciones crudas del escaner. La ruta declarada es convertir la imagen en fantoma: "Voxelized phantoms can be produced from patient images by assigning a material or a mixture of materials to each voxel based on its CT number" (Phantoms, p.5). Es decir, XCIST genera sus propias proyecciones a partir del fantoma y luego reconstruye: "these components must be modeled [...] to produce projection data. Then the projection data must be reconstructed to produce CT images" (Introduction, p.3). Consecuencia practica para MetalSynth-Pelvis: la comparacion no seria imagen-contra-imagen directa sobre CTPelvic1K, sino imagen -> fantoma -> re-simulacion -> re-reconstruccion, con un ciclo extra de reconstruccion que el renderizador LDM no sufre. El PDF no cuantifica el error introducido por ese ciclo. NO ENCONTRADO EN EL PDF.

**4. Codigo abierto? Donde, licencia, lenguaje, dependencias, GPU o CPU?**

- Abierto: si. "All code is maintained as an open-access project on GitHub (github.com/xcist)" (p.4) y "publicly available as an open-source project at github.com/xcist" (p.16).
- Licencia: NO ENCONTRADO EN EL PDF.
- Lenguaje: "XCIST code is a hybrid of Python and C/C++" (p.4); "the projection and backprojection operations are performed in C/C++" (p.4).
- Dependencias: no se lista un archivo de dependencias. Solo se menciona que los datos de seccion eficaz "are obtained from GEANT4 (Agostinelli et al., 2003)" (pp.6-7). Resto: NO ENCONTRADO EN EL PDF.
- GPU: **el PDF no declara en ningun momento que XCIST tenga proyectores en GPU**. La unica mencion de GPU es sobre Monte Carlo de terceros: "Monte Carlo becomes more practical by using graphics processing units (GPUs) for faster processing" (Dose estimation, p.8), y ahi mismo se aclara que esa es otra clase de herramienta. La unica referencia al hardware propio es CPU: "take a few minutes on a PC with 12 CPU-cores" (p.7). Conclusion: la acusacion de yun2026simulationdriven ("only compatible with its own CPU-based reconstruction module") **es consistente con este PDF**; el paper no ofrece nada que la contradiga, y tampoco menciona proyectores diferenciables. Diferenciabilidad: NO ENCONTRADO EN EL PDF.

**5. Relacion declarada con CatSim**

Lo reimplementa y lo contiene como subconjunto. "The image simulation components of XCIST are a new implementation of CatSim (De Man et al., 2007), developed over the past two decades and previously implemented in Matlab (although not previously available in an open-access form)" (Simulation, p.6). Tambien: "currently consists of three major subsets: digital phantoms, the simulator itself (CatSim), and image reconstruction algorithms" (Abstract, p.1) y "XCIST builds on the CatSim simulation tool, the realistic XCAT phantoms and the 3D reconstruction capability" (Conclusion, p.16).

**6. Como se valido XCIST contra datos reales o Monte Carlo?**

Muy poco, y el propio paper lo admite. Evidencia:
- Estado global: "The results presented in this report represent a qualitative and semi-quantitative first-order evaluation" (Validation, p.9); "More thorough and rigorous evaluation is planned" (p.9); "Validation of the noise and resolution modeling capability is in progress" (p.16).
- Contra valores esperados de HU (auto-consistencia, no datos reales): aire -995 vs -1000 HU; agua 0 vs 0 HU; hueso 1551 vs 1552 HU (Discussion Exp.1, p.13). Desviaciones 9.8 y 11.8 HU (p.11).
- Contra Monte Carlo: solo para DOSIS, y sin cifras. "we compared our dose estimation method with Monte Carlo simulation (GEANT4). Dose estimates using our method agreed well with GEANT4 estimates" (Dose estimation, p.9). El PDF no da error porcentual ni metrica. NO ENCONTRADO EN EL PDF.
- Contra un escaner real: se declara en curso, no completado: "We are characterizing XCIST using a widely available third-generation 64-detector-row scanner" (p.9). Metricas de esa comparacion: NO ENCONTRADO EN EL PDF.
- Modelo de espectro: validado en "80 kV to 140 kV" y para angulos de cono de escaneres de 64 filas (p.9), pero remitiendo a FitzGerald et al. 2021.

Metricas cuantitativas propias reportadas: solo RMSE en HU frente a una imagen ideal simulada (Fig. 9, valores de 17 a 213 HU), no frente a datos reales.

**7. Declara limitaciones sobre alta atenuacion, objetos grandes o precision del sinograma con metal?**

NO ENCONTRADO EN EL PDF. El paper no discute objetos de alta atenuacion, ni diametros maximos de objeto metalico, ni fidelidad del sinograma con metal. La unica mencion cercana a alta atenuacion es sobre trayectos largos en tejido, no sobre metal: "this effect occurs when the attenuation is high due to long path lengths through tissue including bone" (Discussion Exp.2, p.14), y "reducing the effect of limited X-ray penetration" (Discussion Exp.4, p.15). Por lo tanto, el hallazgo de haneda2025aapm sobre distorsion del trazo metalico para diametros mayores a 3.0 cm **no esta anticipado ni contradicho por este PDF**; es informacion externa al paper. Notese que las varillas metalicas demostradas aqui son de 2.0 cm y 1.0 cm de diametro, ambas por debajo de ese umbral.

**8. Nivel que sostiene la evidencia**

La evidencia sostiene **NIVEL 1 solo parcialmente, y solo en su faceta de fuente de parametros; como "baseline fisico validado para metal" la evidencia sostiene NIVEL 2**: el paper entrega geometria, espectro, bins, ruido y ecuaciones suficientes para reimplementar un simulador CT generico, pero no contiene ningun estudio, metrica ni validacion de artefacto metalico, y declara su propia validacion como "first-order" y "in progress".

En primer plano, para la autora: **el brazo de comparacion prometido como "reimplementacion validada de XCIST" no es sostenible con lo que este PDF documenta.** El metal existe en XCIST solo como dos varillas cilindricas en una figura cualitativa; falta la calibracion del scatter, la DQE y el bowtie para una reimplementacion fiel; el pipeline exige convertir CTPelvic1K en fantoma voxelizado y re-simular, agregando un ciclo de reconstruccion; y no hay evidencia en el PDF de soporte GPU ni de proyectores diferenciables. La formulacion honesta seria "referencia fisica cualitativa parcialmente reimplementable", no "baseline validado".

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| FitzGerald P et al. (2021) 'Semiempirical, parameterized spectrum estimation for x-ray computed tomography', Medical Physics, 48(5), pp. 2199-2213 | Fuente original del modelo de espectro de XCIST y del unico rango validado (80-140 kV). Sin ella no se puede reimplementar el espectro. |
| De Man B et al. (2007) 'CatSim: a new computer assisted tomography simulation environment', Proc. SPIE 6510 | Base declarada del simulador. Ya leida (deman2007); confirma que XCIST no agrega modelo de metal sobre CatSim. |
| Ohnesorge B, Flohr T and Klingenbeck-Regn K (1999) 'Efficient object scatter correction algorithm for third and fourth generation CT scanners', European Radiology, 9(3), pp. 563-569 | Fuente del modelo analitico de scatter cuya calibracion (C, H, w) el paper no publica. Necesaria para cerrar el hueco de reimplementacion. |
| Tang X et al. (2006) 'A three-dimensional-weighted cone beam filtered backprojection (CB-FBP) algorithm...', Physics in Medicine and Biology, 51(4), pp. 855-74 | Algoritmo de reconstruccion concreto que habria que reimplementar para igualar el brazo fisico. |
| Feldkamp LA, Davis LC and Kress JW (1984) 'Practical cone-beam algorithm', JOSA A, 1(6), p. 612 | Reconstruccion FDK efectivamente usada en los cuatro experimentos; define el pipeline reproducible. |
| Segars WP et al. (2010; 2013; 2015) fantomas XCAT | Fuente de los fantomas anatomicos; alternativa/complemento a usar CTPelvic1K como fuente de anatomia. |
| Abadi E et al. (2019) 'DukeSim: A Realistic, Rapid, and Scanner-Specific Simulation Framework in Computed Tomography', IEEE TMI, 38(6), pp. 1457-65 | Simulador competidor scanner-specific; podria ser mejor brazo fisico que XCIST, o evidencia de que el gap es menor. |
| O'Connell J and Bazalova-Carter M (2021) 'fastCAT: Fast cone beam CT (CBCT) simulation', Medical Physics, 48(8), pp. 4448-4458 | Otra alternativa rapida de simulacion; relevante si XCIST resulta demasiado lento o solo CPU. |
| Ghadiri H et al. (2013) 'A Fast and Hardware Mimicking Analytic CT Simulator', IEEE NSS/MIC | Simulador analitico alternativo citado como la otra clase de herramientas ray-tracing. |
| Badal A and Bandano A (2009) 'Accelerating Monte Carlo simulations of photon transport in a voxelized geometry using a massively parallel graphics processing unit', Medical Physics, 36(11) | Ruta GPU explicita para simulacion de transporte; contrapunto directo a la limitacion CPU de XCIST. |
| Bert J et al. (2013) 'Geant4-based Monte Carlo simulations on GPU for medical applications', PMB, 58, pp. 5593-5611 | Idem: referencia de Monte Carlo acelerado en GPU como baseline fisico alternativo. |
| Agostinelli S et al. (2003) 'Geant4 - a simulation toolkit', Nucl Instrum Meth A, 506(3), pp. 250-303 | Fuente de las secciones eficaces usadas por XCIST y gold standard declarado para validacion fisica. |
| ICRU (1992) Report No. 46: Photon, electron, proton, and neutron interaction data for body tissues | Fuente de densidades y composiciones elementales de tejidos; util para asignar materiales a voxeles de CTPelvic1K. |
| Abadi E et al. (2020) 'Virtual clinical trials in medical imaging: a review', Journal of Medical Imaging, 7 | Marco conceptual de ensayos clinicos virtuales; encuadra el argumento de por que simular en vez de adquirir. |
| Rui X et al. (2015) 'Ultra-low dose CT attenuation correction for PET/CT: analysis of sparse view data acquisition and reconstruction algorithms', PMB, 60(19) | Fuente original del compromiso mAs vs vistas/rotacion citado en el Experimento 2. |
| Parker D (1982) 'Optimal short scan convolution reconstruction for fanbeam CT', Med Phys, 9(2) | Ponderacion usada para short scan; parametro necesario si se reimplementa el brazo fisico. |
