# han2019atlasplanning — Planificacion automatica por atlas y guia fluoroscopica 3D-2D en trauma pelvico

- **DOI / URL:** 10.1088/1361-6560/ab1456 (Phys Med Biol 64(9):095022, 2019). Version leida: author manuscript HHS/PMC (PMC9113192), paginacion "Page 1-33" del manuscrito.
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/han2019atlasplanning.pdf

## Que hace (3 lineas maximo)
Construye un atlas de 40 pelvis CT (SSM) en el que cada miembro trae 10 "corredores de aceptacion" volumetricos anotados por experto; los registra al CT del paciente sin segmentar (ASM + FFD), transfiere los corredores por MVC y los acumula en un mapa de consenso A_c del que se ajusta una trayectoria recta. Luego proyecta A_c sobre fluoroscopia via registro 3D-2D (validado en 1 cadaver, 4 K-wires).

## Restriccion o supuesto clave
No es un paper generativo; los supuestos relevantes para el muestreador son:
- El corredor se define como "todas las orientaciones seguras": "the volumetric trajectory atlas includes all safe (i.e. non-breaching) trajectory poses" (p. 8, sec. 2.1.3). Es decir, modela el espacio de colocaciones correctas, no la malposicion.
- El corredor se construye con un cilindro de radio de K-wire (1.6 mm), no con el diametro de un tornillo canulado (p. 5, sec. 2.1.1). No hay diametros ni longitudes de tornillo.
- Solo sacros "normales": "this work only considered trans-iliac trans-sacral iliosacral screws in S1 and S2 levels" (p. 17, sec. 4); en dismorfismo sacro los transsacros "are not advisable" (p. 17).
- CT sin artefacto: "high-quality preoperative CT images that were free of artifact" (p. 17, sec. 4). No evaluado sobre CT con metal.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 40 pelvis CT (20 H / 20 M) | "A total of n = 40 pelves (20 male and 20 female..." | sec. 2.1.1, p. 4 |
| 10 trayectorias, 6 categorias | "ten trajectories in total—that cover the majority of percutaneous fixation cases" | sec. 4, p. 17 |
| Radio 1.6 mm del cilindro de corredor | "cylinder of 1.6 mm radius (the radius of a standard percutaneous K-wire)" | sec. 2.1.1, p. 5 |
| PPV >80% en IS S1 y S2 | "iliosacral S1 and S2 trajectories were solved with >80% PPV" | sec. 3.2, p. 12 |
| Distancia media a cortical IS S1 3.9 mm, IS S2 4.1 mm | "3.9 mm for iliosacral S1, and 4.1 mm for iliosacral S2" | sec. 3.2, p. 12 |
| Superficie RMSE 1.8 mm tras FFD | "FFD step further reduced surface RMSE to median 1.8 mm" | sec. 3.1, p. 12 |

## Donde entra en mi tesis
Objetivo 2 (muestreador), seccion de trabajo relacionado / fundamentacion del corredor.
- **No compite con el muestreador.** Han planifica la trayectoria optima/segura (consenso de atlas + recta ajustada) para guiar cirugia; el muestreador de la tesis no busca la trayectoria perfecta, sino que muestrea poses incluyendo malposicion segun `zwingmann2009navigated`. Han no modela ni reporta malposicion graduada, ni tasas por tecnica, ni tornillos reales (solo K-wire de 1.6 mm de radio).
- **No cierra el gap; lo acota.** Aporta un antecedente directo de "corredor oseo volumetrico" como espacio de poses validas para IS S1/S2 y de un criterio de brecha cortical (distancia centerline-cortical; < 0 = brecha; umbral 1.6 mm). Esto respalda la idea de que el muestreador restrinja por corredor y contencion cortical, pero Han no combina eso con un muestreo de malposicion ni con sintesis de imagen.
- **Posible insumo:** el atlas (CT + segmentaciones + corredores de referencia) se declara publico (p. 6). Podria servir como referencia externa para contrastar el corredor medido por volumen (`e9ts_corredor.csv`), pero eso es decision de la autora; no verificado que el enlace siga activo.
- **Advertencia de dominio:** validado solo en CT sin artefacto (p. 17); la tesis trabaja con CLINIC-metal.

## Dudas para el asesor
1. El corredor de Han se define con radio de K-wire (1.6 mm), no de tornillo (la tesis usa envolvente 6.5-8.0 mm de diametro). Sirve como referencia de corredor o solo como antecedente conceptual?
2. Usar el atlas publico de Han como validacion externa del corredor medido con TotalSegmentator, o queda fuera de alcance?
3. Inconsistencias internas del PDF (ver abajo): el caption de la Fig. 6 llama "K-wire diameter" a 1.6 mm, mientras el texto dice "radius"; el abstract dice centerline "within 3-5 mm" del cortex, pero las medias de sec. 3.2 van de 3.7 a 6.5 mm; se usa "AIIS to PSIS" y "AIIS to PIIS" indistintamente. Citar solo desde el cuerpo (sec. 3.2)?

## Evidencia textual
| Dato | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| Metodo de planificacion: atlas + ASM + trayectorias | "an atlas of pelvis shapes and reference trajectories is registered to the patient CT via ASM" | sec. 2, p. 4 |
| Sin segmentacion del paciente | "without the need for manual segmentation or annotation of the CT" | sec. 2, p. 4 |
| Fuente de datos del atlas | "CT images drawn from the Cancer Imaging Archive" | sec. 2.1.1, p. 4 |
| N CT del atlas | "A total of n = 40 pelves (20 male and 20 female" | sec. 2.1.1, p. 4 |
| Rango de edad | "age 18–68 years (median 46.5)" | sec. 2.1.1, p. 4 |
| Tamano de volumen | "processed to volume size of 512 × 512 × 500 voxels" | sec. 2.1.1, p. 4 |
| Tamano de voxel | "from 0.63 × 0.63 × 1.00 mm3 to 0.98 × 0.98 × 1.25 mm3" | sec. 2.1.1, p. 4 |
| Reproducibilidad de segmentacion manual | "overlap Dice coefficient of 0.93 ± 0.01" | sec. 2.1.1, p. 5 |
| Repeticiones para reproducibilidad | "A selection of segmentations was repeated four times" | sec. 2.1.1, p. 5 |
| Niveles sacros segmentados | "only the first three levels (S1–S3) were segmented" | sec. 2.1.1, p. 5 |
| Vertices de malla pelvica | "closed, triangulated surface mesh ... with 5000 equidistant vertices" | sec. 2.1.1, p. 5 |
| Registro de plantilla a 39 superficies | "deformably registered to all remaining 39 surfaces via coherent point drift" | sec. 2.1.1, p. 5 |
| Lista de corredores (10) | "(left and right) AIIS to PSIS; (left and right) superior pubic ramus" | sec. 2.1.1, p. 5 |
| Lista de corredores (cont.) | "anterior column to iliac crest; (left and right) posterior column; and iliosacral" | sec. 2.1.1, p. 5 |
| Niveles IS | "iliosacral trajectories (at levels S1 and S2)" | sec. 2.1.1, p. 5 |
| Definicion de corredor: todas las orientaciones | "manually defined to include all possible orientations in the desired bone corridors" | sec. 2.1.1, p. 5 |
| Superficies de entrada | "standard trajectory entry surfaces (in both antegrade and retrograde manner) were manually annotated" | sec. 2.1.1, p. 5 |
| Radio del cilindro (margen) | "cylinder of 1.6 mm radius (the radius of a standard percutaneous K-wire)" | sec. 2.1.1, p. 5 |
| Criterio de contencion | "If the cylinder was entirely contained in the closed bone surface" | sec. 2.1.1, p. 5 |
| Vertices de malla de corredor | "mesh representation ... created with 500 equidistant vertices" | sec. 2.1.1, p. 5 |
| Atlas publico | "available in the public domain and can be downloaded from: https://istar.jhu.edu/downloads/" | sec. 2.1.1, p. 6 |
| Cobertura del CT | "complete scans covering the pelvis from iliac crest to ischium" | sec. 2.1.1, p. 6 |
| RANSAC subconjunto | "A subset of vertices (n = 100) denoted by RANSAC" | sec. 2.1.2, p. 6 |
| RANSAC repeticiones | "This process is repeated for 50 times" | sec. 2.1.2, p. 6 |
| Piramide multiresolucion | "isotropic downsampling [4×, 2×, 1×], Gaussian smoothing kernel width (voxels) [4, 2, 1]" | sec. 2.1.2, p. 7 |
| Componentes principales | "number of principal components [2, 4, 8, 12]" | sec. 2.1.2, p. 7 |
| Criterio de convergencia | "falling below a particular threshold (set to 0.5δ in the current work)" | sec. 2.1.2, p. 7 |
| Limite de downsampling | "Beyond 8 × downsampling, bone gradients were no longer salient" | sec. 2.1.2, p. 7 |
| Varianza explicada | "first 12 principal components constituted more than 90% of the total variance" | sec. 2.1.2, p. 7 |
| Filtro sinc en FFD | "sinc smoothing function with passband at 10% of Nyquist frequency" | sec. 2.1.2, p. 7 |
| Transferencia de trayectorias | "mean value coordinates (MVC) method (Ju et al 2005) was used to interpolate" | sec. 2.1.3, p. 8 |
| Mapa de acumulacion | "A total accumulation map Ac is computed by taking the normalized sum" | sec. 2.1.3, p. 8 |
| Interpretacion de A_c | "values closer to 1 indicate greater consensus of the atlas" | sec. 2.1.3, p. 8 |
| Similitud 3D-2D | "GO was used as a similarity metric (De Silva et al 2016)" | sec. 2.2.1, p. 8 |
| Umbrales de gradiente GO | "thresholds t1 and t2 are defined as the median gradient magnitude" | sec. 2.2.1, p. 8 |
| CMA-ES poblacion y sigma | "population size of 200 was used, and the initial standard deviation ... σ = 15 mm and 15°" | sec. 2.2.1, p. 9 |
| Tiempo de registro 3D-2D | "average registration runtime of 12.8 s in the cadaver studies" | sec. 2.2.1, p. 9 |
| Separacion angular (trabajo previo) | "three radiographs separated by at least 20° from each other" | sec. 2.2.2, p. 9 |
| Validacion cruzada | "evaluated in a leave-one-out cross-validation of the atlas" | sec. 2.3.1, p. 9 |
| Metrica: RMSE de superficie | "computed by the surface root mean square error (RMSE) between every vertex" | sec. 2.3.1, p. 10 |
| Metrica: PPV y umbral 0.5 | "positive predictive value (PPV) for values of the accumulation volume above 0.5" | sec. 2.3.1, p. 10 |
| Significado del umbral 0.5 | "(indicating consensus by over half of the atlas)" | sec. 2.3.1, p. 10 |
| Trayectoria optima | "fitting a straight, rigid cylinder to the accumulation map between the two entry/exit surfaces" | sec. 2.3.1, p. 10 |
| Criterio de brecha cortical | "negative values indicate breach of the bone cortex" | sec. 2.3.1, p. 10 |
| Corredores de sensibilidad | "superior pubic ramus and iliosacral S1 trajectories were chosen as challenging examples" | sec. 2.3.1, p. 10 |
| Cadaver: n y K-wires | "placement of four K-wires in a fresh human cadaver" | sec. 2.3.2, p. 10 |
| Corredores en cadaver | "AIIS to PSIS, anterior column to iliac crest (left), superior ramus (left), and iliosacral (at S1)" | sec. 2.3.2, p. 10-11 |
| CBCT de cadaver | "reconstructed at 0.42 × 0.42 × 0.42 mm3 with a volume size of 880 × 512 × 568" | sec. 2.3.2, p. 11 |
| Radio K-wire en cadaver | "four K-wires (Stryker, Kalamazoo MI) of 1.6 mm radius" | sec. 2.3.2, p. 11 |
| Malposicion intencional | "The superior ramus K-wire was slightly misplaced on purpose" | sec. 2.3.2, p. 11 |
| N radiografias | "(4 K-wires) × (3 stages) × (4 views) = 48 radiographs" | sec. 2.3.2, p. 11 |
| Landmarks para PDE | "Up to 10 unambiguous anatomical landmarks were identified" | sec. 2.3.2, p. 11 |
| RMSE tras ASM (LOO) | "median surface distance error of 2.2 mm RMSE (0.3 mm interquartile range [IQR])" | sec. 3.1, p. 11 |
| RMSE tras FFD (LOO) | "FFD step further reduced surface RMSE to median 1.8 mm (0.2 mm IQR)" | sec. 3.1, p. 12 |
| Significancia ASM vs FFD | "statistically significant reduction ... (Student t-test p ≪ 0.05)" | sec. 3.1, p. 12 |
| RMSE en cadaver | "surface RMSE of 2.2 mm (0.9 mm IQR) after ASM registration and 1.6 mm" | sec. 3.1, p. 12 |
| RMSE cadaver FFD IQR | "(0.5 mm IQR) after FFD" | sec. 3.1, p. 12 |
| Error en cuerpo de rama/alas | "body of the ramus and iliac wings, which show error within ~1 mm" | sec. 3.1, p. 12 |
| Error uniforme | "fairly uniform registration (~1 mm surface RMSE) across most of the pelvis" | sec. 3.1, p. 12 |
| PPV general | "The results demonstrate >90% overlap between the automatically determined plans" | sec. 3.2, p. 12 |
| PPV IS | "iliosacral S1 and S2 trajectories were solved with >80% PPVAc for all cases" | sec. 3.2, p. 12 |
| IS mas dificil | "The iliosacral trajectories were the most challenging due to high anatomical variation" | sec. 3.2, p. 12 |
| Umbrales de seguridad graficados | "lower thresholds marked by red horizontal lines at 1.6 mm (typical K-wire radius)" | sec. 3.2, p. 12 |
| Umbral de brecha | "and 0 mm (below which the trajectory has breached cortical bone)" | sec. 3.2, p. 12 |
| Distancia media a cortical AIIS-PSIS / cresta / rama | "5.4 mm for AIIS to PSIS 5.1 mm for iliac crest, 3.7 mm for superior ramus" | sec. 3.2, p. 12 |
| Distancia media columna posterior / IS | "6.5 mm for posterior column, 3.9 mm for iliosacral S1, and 4.1 mm" | sec. 3.2, p. 12 |
| Outliers | "A small number of outliers (1–2 each) was observed for the superior ramus" | sec. 3.2, p. 12 |
| FFD necesario para PPV > 0.90 | "To achieve PPV > 0.90, the FFD refinement was required" | sec. 3.2, p. 13 |
| RMSE requerido | "bringing atlas-to-CT surface RMSE below 2.0 mm" | sec. 3.2, p. 13 |
| FFD mejora PPV | "The FFD stage significantly improved PPV (student t-test p < 0.05)" | sec. 3.2, p. 13 |
| PDE en cadaver | "overall median PDE of 2.1 mm (0.3 mm IQR) after registration" | sec. 3.3, p. 13 |
| Precision intra-observador landmarks | "intra-observer precision of 1.98 ± 1.95 mm" | sec. 3.3, p. 13 |
| Precision inter-observador landmarks | "inter-observer precision of 4.37 ± 3.30 mm" | sec. 3.3, p. 13 |
| Geometria del sistema | "source to detector distance ~1200 mm and magnification of 1.80" | sec. 3.3, p. 14 |
| Efecto de error en z | "a 5 mm error in z corresponds to a 0.7% change in magnification" | sec. 3.3, p. 14 |
| Error traslacional | "In-plane translational error was within ~2 mm" | sec. 3.3, p. 14 |
| Error fuera de plano | "out-of-plane translational errors were higher (up to ~6 mm)" | sec. 3.3, p. 14 |
| Error rotacional | "within the plane of the detector (α) were low (median 0.02°)" | sec. 3.3, p. 14 |
| Error rotacional fuera de plano | "higher out-of-plane (β, γ), ~4°" | sec. 3.3, p. 14 |
| PPV_P fluoroscopia | "PPVP achieved >95% in AIIS to PIIS and iliosacral S1 trajectory" | sec. 3.4, p. 14 |
| PPV_P rama y cresta | ">90% in superior pubic ramus and iliac crest trajectory" | sec. 3.4, p. 14 |
| PPV_P por trayectoria | "AIIS to PSIS 94.5%" / "Superior pubic ramus 91.7%" | Tabla 2, p. 32 |
| PPV_P por trayectoria (cont.) | "Iliac crest 92.2%" / "Iliosacral S1 97.4%" | Tabla 2, p. 32 |
| K-wires en cadaver dentro del corredor | "three of the K-wires (AIIS to PSIS iliac crest, iliosacral S1) ... reside entirely within" | sec. 3.4, p. 14 |
| Tiempo preoperatorio | "Preoperative runtime (ASM, FFD, and trajectory registration ...) was ~9 min in total" | sec. 3.4, p. 15 |
| Tiempo de inicializacion | "initialization time is 12.8 ± 3.2 s" | sec. 3.4, p. 15 |
| Tiempo 3D-2D sucesivo | "reducing the 3D–2D registration runtime to 5.0 ± 2.1 s" | sec. 3.4, p. 15 |
| Tiempo de overlay | "Augmentation/overlay of the fluoroscopic image requires just 0.2 ± 0.1 s" | sec. 3.4, p. 15 |
| Runtime tolerable | "tolerable runtime in step-and-shoot guidance is likely ~3–10 s" | sec. 3.4, p. 15 |
| Tiempos por paso | "ASM 40.7 ± 1.8"; "FFD 0.7 ± 0.1"; "Trajectory planning 490.5 ± 30.0" (s) | Tabla 3, p. 33 |
| Resumen de precision | "surface registration accuracy of 1.8 mm in cross-validation and 1.6 mm in a cadaver" | sec. 4, p. 15 |
| PDE y runtime resumen | "showing mean PDE ~2.0 mm and runtime ~12 s" | sec. 4, p. 15 |
| Registro 3D-2D < 2 mm | "provided accurate patient registration (<2 mm)" | sec. 4, p. 16 |
| Tiempo por registro 3D-2D | "yielding ~13 s computation time for each registration" | sec. 4, p. 16 |
| Tiempos CPU | "currently implemented on CPU, yielding ~3 min and ~9 min respectively" | sec. 4, p. 16 |
| Limitacion: dismorfismo sacro | "trans-sacral iliosacral screws are not advisable (Miller and Routt 2012)" | sec. 4, p. 17 |
| Limitacion: solo TITS S1/S2 | "only considered trans-iliac trans-sacral iliosacral screws in S1 and S2 levels" | sec. 4, p. 17 |
| Limitacion: CT sin artefacto | "high-quality preoperative CT images that were free of artifact" | sec. 4, p. 17 |
| Robustez a artefactos (afirmada, no medida) | "also robust to high-frequency artifacts (e.g. streaking and ring artifacts)" | sec. 4, p. 17 |
| Dosis CBCT (trabajo citado) | "ASM was found to perform comparably over a dose range ~15–35 mGy" | sec. 4, p. 17 |
| Trabajo previo: atlas de 12 | "atlas of 12 single-sided female hip bones and 3 relevant trajectories" | sec. 1, p. 3 |
| Mortalidad (contexto, citada) | "carry a high rate of mortality (8.3%) (Yoshihara and Yoneoka 2014)" | sec. 1, p. 2 |
| Fluoroscopia (contexto, citada) | "extended fluoroscopy runtimes (exceeding 120 s total (Gras et al 2010))" | sec. 1, p. 2 |
| Abstract: centerline vs cortex | "centerline trajectory within 3–5 mm of the bone cortex" | Abstract, p. 1-2 |
| Abstract: 3D-2D | "0.3 ± 0.8 mm accuracy (in-plane translation) and <4° accuracy" | Abstract, p. 2 |
| Inconsistencia caption Fig. 6 | "1.6 mm (K-wire diameter) and 0.0 mm from the cortex boundary" | Fig. 6, p. 26 |
| Diametro de tornillo | NO ENCONTRADO EN EL PDF | — |
| Longitud de tornillo / trayectoria (cifra en texto) | NO ENCONTRADO EN EL PDF (solo eje "Position along Trajectory (mm)" en Fig. 6, p. 26) | — |
| Error de trayectoria planificada en grados (angular) | NO ENCONTRADO EN EL PDF | — |
| Error de punto de entrada/salida en mm | NO ENCONTRADO EN EL PDF | — |
| Tasas de malposicion / grados de brecha (escala ordinal) | NO ENCONTRADO EN EL PDF | — |
| Corredor supraacetabular explicito | NO ENCONTRADO EN EL PDF (el corredor AIIS a PSIS es el mas cercano; no se le llama supraacetabular) | — |
| Zonas seguras neurovasculares cuantificadas | NO ENCONTRADO EN EL PDF | — |
| Evaluacion en CT con implantes metalicos | NO ENCONTRADO EN EL PDF | — |
