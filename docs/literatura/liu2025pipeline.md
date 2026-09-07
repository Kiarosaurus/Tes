# liu2025pipeline — Pipeline geometrico end-to-end para planificacion preoperatoria de reduccion y fijacion de fractura pelvica

- **DOI / URL:** doi:10.1109/TMI.2024.3429403 (IEEE Trans Med Imaging. 2025 January; 44(1): 79–91). Codigo: https://github.com/JiaxuanLLiu/PelvisFix
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/liu2025pipeline.pdf

## Que hace (3 lineas maximo)
Pipeline automatico de planificacion preoperatoria de cirugia de fractura pelvica en tres etapas: etiquetado de fragmentos (watershed adaptativo), planificacion de reduccion (registro en dos pasos con hueso contralateral espejado + superficies de fractura) y planificacion de fijacion con tornillos.
La etapa de fijacion calcula numero, posicion y direccion de los tornillos por geometria (PCA, centro de Chebyshev, busqueda densa de direcciones) sobre las superficies de fractura adyacentes.
Se valida en 14 casos clinicos de CTPelvic1K y se implementa como modulo de 3D Slicer.

## Restriccion o supuesto clave
No es un metodo generativo de imagen: los tornillos se representan como cajas/cilindros geometricos sobre mallas y nubes de puntos, nunca como intensidades HU ni con artefacto metalico. Ademas produce UN plan optimo determinista, no una distribucion de colocaciones: "The computation of implanted directions of the screws is formulated as an optimization problem subject to safety, fixation ability, and clinical executability constraints" (Sec. III-D.3, p. 11) y "an improved dense search method based on [40] is proposed to obtain the optimal trajectory" (pie de Fig. 6, p. 28). Restriccion anatomica declarada: "It is not yet applicable to bilateral fractures and to sacral fractures because of the limitation of the mirroring process" (Discussion, p. 18).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [x] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 14 casos clinicos de CTPelvic1K | "14 available clinical cases that suffer from unilateral fractures were obtained" | VI. Experimental results, p. 14 |
| 2.56 mm / 3.31 grados de error de reduccion | "translational and rotational accuracy of 2.56 mm and 3.31° in reduction planning" | Abstract, p. 2 |
| 86.7% de aceptacion clinica (C3) | "a clinical acceptance rate of 86.7% was achieved" | Abstract, p. 2 |
| CSV (distancia al borde oseo) 10.58±3.84 mm su metodo vs 4.36±3.83 mm LSM&PCA | "distances from centers of mass and the positions by our method to the bone boundary (Chanel Safety Value, CSV [29])" | Sec. IV-B, p. 16 y Tabla III, p. 38 |
| Restriccion de contencion cortical | "keeping screws from penetrating the cortical bone while the screw head stays at the outer end of the pelvic" | Sec. III-D.3, p. 12 |

## Donde entra en mi tesis
Related Work del Objetivo 2 (muestreador restringido) y encuadre del gap: es el trabajo publicado mas cercano en planificacion geometrica automatica de fijacion pelvica sobre CTPelvic1K, pero optimiza una trayectoria unica en vez de muestrear la distribucion clinica de malposiciones, y no genera apariencia CT ni artefacto metalico. Su metrica CSV (distancia posicion-borde oseo) es candidata a comparacion o validacion cruzada frente a SAP/BFC.

## Dudas para el asesor
- CSV ("Chanel Safety Value", tomado de [29]) mide distancia de la posicion del tornillo al borde oseo. ¿Se adopta como metrica de referencia externa contra la que anclar SAP/BFC, o se mantiene SAP con definicion propia y CSV solo como comparacion cualitativa?
- El paper reporta Likert >=3 como "clinicamente aceptable" con 3 cirujanos. ¿Sirve ese esquema como precedente para justificar un umbral de aceptabilidad en la evaluacion del muestreador, o la tesis se queda solo con la tasa clinica de malposicion?
- El pie de Fig. 6 cita "[40]" y el texto de la misma seccion cita "[45]" para el mismo metodo de busqueda densa de direcciones. Inconsistencia del manuscrito; ¿se cita [45] (Li et al., planificacion por densidad osea) al referirse a ese componente?

## Evidencia textual

| Dato / umbral / definicion | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| Fractura pelvica = 1%–3% de todas las fracturas | "comprising 1%–3% of all types of fractures" | I. Introduction, p. 2 |
| Mas del 50% de fracturas pelvicas con complicaciones | "Over 50% of pelvic fractures involve complications and multiple injuries" | I. Introduction, p. 2 |
| Mortalidad de fractura pelvica abierta 30%–50% | "The fatality rate of an open pelvic fracture is estimated to be 30%–50%" | I. Introduction, p. 2 |
| Impresion 3D de implante paciente-especifico: hasta 36 horas | "the design, printing, and sterilization may take up to 36 hours" | II-C, p. 4 |
| Dataset usado: CTPelvic1K | "Our method is tested in data set CTPelvic1K [48]" | VI. Experimental results, p. 14 |
| Casos utilizables tras excluir sanos y fracturas de sacro: 14 | "14 available clinical cases that suffer from unilateral fractures were obtained" | VI. Experimental results, p. 14 |
| Resolucion de voxel mediana 0.84×0.84×0.80 mm3 | "median value of the image voxel resolution is 0.84×0.84×0.80 mm3" | VI. Experimental results, p. 14 |
| Tamano mediano de volumen 512×512×350 | "the median size is 512×512×350" | VI. Experimental results, p. 14 |
| Composicion de casos: 1–5 dos cuerpos, 6–11 tres cuerpos, 12–14 complejos | "Cases 1–5, 6–11, 12–14 are respectively 2-body, 3-body and complex multi-body fractures" | VI. Experimental results, p. 14 |
| Ground truth definido por cirujano con >15 anos de experiencia | "manually defined by an expert orthopedic surgeon with > 15 years of experience" | VI. Experimental results, p. 14 |
| Kernel de erosion morfologica alpha = 2 | "The kernel size of morphological erosion operation in Eq. (1)" — valor 2 | Tabla I, p. 36 |
| Kernel de dilatacion morfologica beta = 3 | "The kernel size of morphological dilation operation in Eq. (1)" — valor 3 | Tabla I, p. 36 |
| Radio de la bola PCA r_p = 20 | "we set it to 20, which can form a ball roughly covers the elongated bone" | III-D.3, p. 12 |
| Radio del tornillo s_r = 1.5 | "we set it to 1.5, which is the clinical size and can be set accordingly" | III-D.2, p. 11 |
| Tamano minimo de nube de puntos para implantacion epsilon_n = 50 | "the minimum size for screw implantation after downsampling, it was set to 50" | III-D.1, p. 8 |
| Umbrales de escala (epsilon_s1, epsilon_s2) = radio del tornillo y 20 veces el radio | "they are set to the size of the screw radius and 20 times the screw radius" | III-D.1, p. 9 |
| Valores tabulados de (epsilon_s1, epsilon_s2) = (6,30) | "the parameters to judge the scale of a point cloud in Eq. (9)" — valor (6,30) | Tabla I, p. 36 |
| Peso de balance epsilon_f = 0.5 por defecto | "is a parameter to balance ... and ..., the default is 0.5" | III-D.3, p. 14 |
| Paso de ventana deslizante Delta = 1.5 | "Consequently, we opted to set Δ to 1.5" | IV, p. 15 |
| Ancho de ventana chi = 8 s_r | "χ determines the width of the sliding window in Fig.5, which was set to 8s_r" | IV, p. 15 |
| Valor tabulado de chi = 12 | "The boundary margin width in computing Chebyshev Center" — valor 12 | Tabla I, p. 36 |
| Umbral de contribucion de varianza PCA epsilon_p = 0.6 | "Therefore, ϵp was set to 0.6" | IV, p. 15 |
| Criterio empirico para epsilon_p: varianza >0.6 en hueso fino | "principal variance contributions on the fine bone regions were generally greater than 0.6" | IV, p. 15 |
| Contribuciones de varianza observadas por region: 0.402, 0.488, 0.643, 0.654, 0.672, 0.684, 0.731 | "The results of the exploratory study on principal component contribution values" | Fig. 10, p. 32 |
| Parametros de direccion (phi, Rc, Rr) = (pi/6, 18, 15) | "We set ϕ, Rc, and Rr to π/6, 18, and 15 respectively" | VI. Experimental results, p. 14 |
| d_s = 200 como valor "suficientemente grande" para el tamano pelvico | "we set it to 200, a sufficiently large value for pelvic size" | III-D.3, p. 13 |
| Criterio de punto "unsuitable": distancia menor que el radio del tornillo | "if the distance is less than s_r, a screw implanted in this path will penetrate the bone" | III-D.3, p. 13 |
| Restriccion de contencion cortical | "keeping screws from penetrating the cortical bone while the screw head stays at the outer end of the pelvic" | III-D.3, p. 12 |
| Restriccion de no protrusion y no interferencia entre tornillos | "This box should not protrude from the bone and interfere with previously planned screw bounding boxes" | III-D.3, p. 12 |
| Profundidad minima de insercion: l >= 8 s_r | "the purpose of the constraints is to prevent screws from being implanted at insufficient depth" | III-D.3, p. 14 |
| Origen del factor de profundidad: 2.5 veces el radio en aluminio | "in aluminum, screws should be inserted at a depth of at least 2.5 times the radius" | III-D.3, p. 14 |
| Uso de densidad osea como justificacion del coeficiente 8 | "Since the bone density is close to that of aluminum, the coefficient is set to 8" | III-D.3, p. 14 |
| Histograma de rasgos: 11 bins, 33 elementos | "mapped to the interval [−1,1], which is divided into 11 equal bins" | III-C.1, p. 7 |
| Ocho direcciones a 45 grados para el centro de Chebyshev | "eight evenly distributed directions with a 45° angle between the adjacent directions" | III-D.2, p. 10 |
| Dice de etiquetado de fragmentos: 91.3±7.4% | "our method achieved a mean Dice coefficient of 91.3±7.4%" | IV-A, p. 15 |
| Dice del metodo SOTA de deep learning: 86.2±7.8% | "trained on its publicly available dataset and then tested on our dataset, achieved 86.2±7.8%" | IV-A, p. 15 |
| Mejora sobre SOTA: 5.1% en Dice | "Our method outperformed the SOTA method by 5.1% in terms of Dice coefficient" | IV-A, p. 15 |
| Desplazamiento aceptable en fractura pelvica comun: 5–10 mm | "an acceptable displacement of up to 5–10 mm in reduction surgery [49]" | IV-A, p. 15 |
| Desplazamiento aceptable en acetabulo: 2–3 mm | "the displacement should be controlled within 2–3 mm [50]" | IV-A, p. 15 |
| Errores traslacionales clinicos <= 5 mm salvo Caso 4 (8.38 mm) | "Translational errors in the clinical cases are ≤ 5mm except for Case 4 (8.38mm)" | IV-A, p. 16 |
| Errores rotacionales <= 5 grados salvo Caso 6 (7.5 grados) | "Rotational errors in the clinical cases are ≤ 5°, except for Case 6 (7.5°)" | IV-A, p. 16 |
| No hay valor aceptado de error rotacional en reduccion pelvica | "a universally accepted value for rotational error in reduction surgery ... has yet to be defined" | IV-A, p. 16 |
| Error medio de reduccion global 2.56 mm / 3.31 grados | "The mean translational and rotational error in all types of fracture (2.56mm, 3.31°)" | IV-A, p. 16 |
| Error de reduccion por tipo: 2-body 2.99±1.55 mm / 3.77±0.79 grados | "Reduction Error of Clinical Cases" | Tabla II, p. 37 |
| Error de reduccion 3-body 2.30±1.09 mm / 3.11±1.29 grados | "Reduction Error of Clinical Cases" | Tabla II, p. 37 |
| Error de reduccion 4/5-body 2.38±1.47 mm / 3.15±1.17 grados | "Reduction Error of Clinical Cases" | Tabla II, p. 37 |
| Metodo comparativo [25] (plantilla adaptativa): 2–3 mm y 2–3 grados en simulacion | "reported in [25]: 2–3 mm and 2–3° for the three fracture categories in a simulation study" | IV-A, p. 16 |
| CSV su metodo (todos): 10.58±3.84 mm; LSM&PCA 4.36±3.83 mm | "The contrast experiment on QID and CSV" | Tabla III, p. 38 |
| QID su metodo (todos): 93.88±21.15 mm; centro de masa 65.58±40.76 mm | "The contrast experiment on QID and CSV" | Tabla III, p. 38 |
| Definicion de QID: mayor profundidad implantada = mejor fijacion | "quantified implanted depth (QID) of the screws ... a larger depth indicates better fixation" | IV-B, p. 16 |
| Definicion de CSV: mayor valor = mejor estabilizacion | "which indicated better implanted stabilization with a larger value" | IV-B, p. 16 |
| Escala Likert de 5 puntos, 3 = nivel clinicamente aceptable, 5 = perfecto | "scores corresponding to 1 to 5, 3 being the clinically acceptable level, and 5 seamless" | IV-B, p. 17 |
| Tres indices evaluados: seguridad (C1), fijacion (C2), ejecutabilidad clinica (C3) | "three main indices: safety (C1), fixation (C2), and clinical executability (C3)" | IV-B, p. 16 |
| Encuesta sobre 12 casos, 3 cirujanos expertos, tecnica Delphi modificada, 2 rondas | "on 12 cases treatable by implantation fixation, after undergoing a modified Delphi technique" | IV-B, p. 16 |
| Casos sin consenso entre los tres cirujanos fueron excluidos | "Cases without consensus among the expert surgeons were excluded from the final assessment" | IV-B, p. 17 |
| Tasa de planes con score>=3: 100% C1, 100% C2, 86.7% C3 y global | "were 100% for C1, 100% for C2, 86.7% for C3 and the overall score" | IV-B, p. 17 |
| Scores Likert globales: C1 4.27±0.58, C2 4.00±0.64, C3 3.53±0.78, overall 3.57±0.73 | "Results of the Likert Rating Scale Survey" | Tabla IV, p. 39 |
| Scores Likert 4/5-body: C1 3.80±0.45, C2 3.60±0.55, C3 2.80±0.84, overall 3.00±1.00 | "Results of the Likert Rating Scale Survey" | Tabla IV, p. 39 |
| Tiempo de planificacion por tornillo: 3.82±1.00 s | "completed the planning of a single screw in 3.82±1.00s on the Intel Core i5-10210U" | IV-B, p. 17 |
| Velocidad: ~15 veces mas rapido que la planificacion manual intraoperatoria | "empirically about 15 times faster than manual intraoperative planning" | IV-B, p. 17 |
| Sensibilidad cruzada: CSV baja y offset sube con error de reduccion inaceptable | "CSV decreases significantly while ϑ offset increases significantly" | IV-C, p. 17 |
| Errores de reduccion evaluados: 0.00, 1.29, 3.44, 5.67, 7.45 mm (0.00°, 0.82°, 4.41°, 6.76°, 9.01°) | "the quantified outcomes of implantation planning in a case with different reduction errors" | Tabla V, p. 40 |
| CSV correspondiente: 16.40, 16.40, 15.20, 13.60, 11.60 mm | "CSV was measured with a resolution of 0.40mm" | Tabla V, p. 40 |
| Offset de posicion: 0.00, 0.78, 2.02, 3.55, 22.37 mm | "ϑ Offset(mm)" | Tabla V, p. 40 |
| Resolucion de medicion de CSV: 0.40 mm | "CSV was measured with a resolution of 0.40mm" | Tabla V (titulo), p. 40 |
| Criterio de significancia: p >= 0.05 indica no diferencia significativa | "p-value ≥ 0.05 indicates that there is no significant difference between the results" | IV-C, p. 17 |
| p-values reduccion vs gold standard: QID 0.80/0.78/0.85/0.81; CSV 0.96/0.40/0.56/0.41 | "The quantified effects of the reduction planning on implantation" | Tabla VI, p. 41 |
| Limitacion: la orientacion acetabular no se evita automaticamente | "the acetabular orientation is not avoided automatically in the trajectory of the screws" | V. Discussion, p. 18 |
| Limitacion: mecanismo tornillo a tornillo sacrifica los posteriores | "it will sacrifice the subsequently implanted screw to avoid interfering with the previous ones" | V. Discussion, p. 18 |
| Limitacion: no aplicable a fracturas bilaterales ni de sacro | "not yet applicable to bilateral fractures and to sacral fractures because of the limitation" | V. Discussion, p. 18 |
| Placas de acero excluidas del alcance de la planificacion | "physicians prefer the intraoperative design of steel plate implantation [38]" | III-D, p. 8 |
| Tasa clinica de malposicion de tornillos | NO ENCONTRADO EN EL PDF | — |
| Tasa de brecha o perforacion cortical medida | NO ENCONTRADO EN EL PDF | — |
| Metrica de calidad de imagen (HU, MAE, artefacto metalico) | NO ENCONTRADO EN EL PDF | — |
| Modelado probabilistico o distribucion de poses de implante | NO ENCONTRADO EN EL PDF | — |

## Verificacion de nivel

**1. Que hace exactamente: trayectoria optima o distribucion de colocaciones?**
Trayectoria unica optima. No hay modelado de variabilidad.
- "The computation of implanted directions of the screws is formulated as an optimization problem subject to safety, fixation ability, and clinical executability constraints" (Sec. III-D.3, p. 11).
- "an improved dense search method based on [40] is proposed to obtain the optimal trajectory" (pie de Fig. 6, p. 28).
- "The center with the largest radius of the approximate maximum internal tangent circle is the desired position" (Sec. III-D.2, p. 10).
- Modelado de distribucion o muestreo estocastico de poses: NO ENCONTRADO EN EL PDF.

**2. Compite directamente con un muestreador de colocacion de implantes?**
Compite parcialmente en el "donde y con que pose" geometrico, pero no en el objetivo de muestrear malposiciones ni en la sintesis de imagen.
- A favor de la competencia: "we decouple it into computing the number, positions, and directions of the implanted screws" (Sec. III-D, p. 8).
- Lo que la descarta como muestreador: el objetivo declarado es el optimo clinico, no la variabilidad — "Further research will be conducted to improve the performance on clinical applicability, ensuring that automated planning schemes can achieve the clinical optimum" (Discussion, p. 19). Y la salida es un plan unico por tornillo: "The implantation planning result of the i-th screw can then be generated as {ϑ, v, l_f, l_b}" (Sec. III-D.3, p. 13).
- No genera imagen CT ni artefacto: NO ENCONTRADO EN EL PDF ninguna mencion de sintesis de imagen, HU o artefacto metalico.

**3. Trabaja sobre CT pelvica? Dataset y tamano**
Si. "Our method is tested in data set CTPelvic1K [48], which contains healthy pelvis cases and different types of pelvis fracture cases" (Sec. VI, p. 14). Tamano efectivo: "14 available clinical cases that suffer from unilateral fractures were obtained" (p. 14). La encuesta clinica se hizo "on 12 cases treatable by implantation fixation" (p. 16). No se indica que se use el subconjunto CLINIC-metal: NO ENCONTRADO EN EL PDF.

**4. Coloca tornillos iliosacrales o solo reduce fragmentos?**
Hace ambas cosas (reduce y coloca tornillos), pero los tornillos NO son iliosacrales. Son tornillos de fijacion perpendiculares/adyacentes a la superficie de fractura en ilion, pubis y acetabulo: "Cases 1–5, 6–11, 12–14 are respectively 2-body, 3-body and complex multi-body fractures involving fractures of the iliac crest, pubic bone, and acetabular" (p. 14). El sacro queda explicitamente fuera: "not yet applicable to bilateral fractures and to sacral fractures" (Discussion, p. 18). Mencion de tornillos iliosacrales: NO ENCONTRADO EN EL PDF.

**5. Zonas seguras, corredores oseos, densidad osea o contencion cortical como restriccion?**
Contencion cortical: SI, explicita. "keeping screws from penetrating the cortical bone while the screw head stays at the outer end of the pelvic" (Sec. III-D.3, p. 12) y "This box should not protrude from the bone and interfere with previously planned screw bounding boxes" (p. 12). El criterio operacional es geometrico: "if the distance is less than s_r, a screw implanted in this path will penetrate the bone" (p. 13).
Restriccion de seguridad nombrada: "To introduce the safety constraint, two point sets ... are computed" (p. 12) y el indice C1 se llama "safety" (p. 16).
Densidad osea: solo como analogia para fijar un coeficiente, no como mapa. "Since the bone density is close to that of aluminum, the coefficient is set to 8 for better fixation" (p. 14). En Related Work se menciona que la planificacion puede basarse en "the geometric shape of fractured bones, bone density, or multi-parametric statistics [28]" (Sec. II-C, p. 4), pero este metodo no construye mapa de densidad.
Zonas seguras anatomicas / corredores oseos: NO ENCONTRADO EN EL PDF; al contrario, se declara la carencia: "the acetabular orientation is not avoided automatically in the trajectory of the screws, which is intentionally avoided in clinical practice" (Discussion, p. 18).

**6. Reporta alguna tasa de malposicion o de brecha cortical?**
NO ENCONTRADO EN EL PDF. Lo mas cercano son (a) la tasa de aceptabilidad clinica Likert, "were 100% for C1, 100% for C2, 86.7% for C3 and the overall score" (p. 17), que es aceptabilidad de un plan automatico, no malposicion intraoperatoria; y (b) la metrica CSV como distancia al borde oseo (Tabla III, p. 38), que es un margen, no una tasa de brecha.

**7. Nivel que sostiene la evidencia**
NIVEL 2. La evidencia no sostiene el nivel 1 con el que llego (promocion hecha solo desde el titulo): el metodo produce un plan optimo determinista sobre una pelvis ya reducida, sin distribucion de poses, sin tasa de malposicion, sin zonas seguras anatomicas y sin ninguna sintesis de imagen, de modo que no puede tumbar el benchmark del muestreador; pero si obliga a redactar el gap con precision porque planifica geometria de tornillos en pelvis sobre CTPelvic1K y define dos metricas de fijacion (CSV, QID) cercanas al espiritu de SAP/BFC.
Caveat para la autora: si SAP se define como margen a la cortical, CSV es un antecedente directo y la comparacion pasa a ser obligatoria; en ese escenario la clasificacion sube a nivel 1 por la via de la metrica, no por la via del metodo.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| [29] Yang W, Feng S, Song J, Cheng C, Liang C, and Wang Y, "Computer-aided automatic planning and biomechanical analysis of a novel arc screw for pelvic fracture internal fixation," Computer Methods and Programs in Biomedicine, vol. 220, p. 106810, 2022. | Fuente original de la metrica CSV (Chanel Safety Value) usada aqui como margen al borde oseo; candidata a validar o competir con SAP/BFC. Ademas es planificacion automatica de tornillo en pelvis. |
| [30] Goerres J, Uneri A, Jacobson M, Ramsay B, De Silva T, Ketcha M, Han R, Manbachi A, Vogt S, Kleinszig G et al. "Planning, guidance, and quality assurance of pelvic screw placement using deformable image registration," Physics in Medicine and Biology, vol. 62, no. 23, p. 9018, 2017. | Metodo de planificacion de colocacion de tornillos pelvicos por registro deformable: competidor directo del muestreador y posible reduccion del gap declarado. |
| [45] Li H, Xu J, Zhang D, He Y, and Chen X, "Automatic surgical planning based on bone density assessment and path integral in cone space for reverse shoulder arthroplasty," IJCARS, vol. 17, no. 6, pp. 1017–1027, 2022. | Planificacion automatica basada explicitamente en evaluacion de densidad osea; es la base del buscador de direcciones que este paper extiende. Directamente relevante al muestreador restringido por densidad. |
| [49] Smith W, Shurnas P, Morgan S, Agudelo J, Luszko G, Knox EC, and Georgopoulos G, "Clinical outcomes of unstable pelvic fractures in skeletally immature patients," JBJS, vol. 87, no. 11, pp. 2423–2431, 2005. | Fuente original del umbral de desplazamiento aceptable 5–10 mm citado aqui. Umbral citable para tolerancias del muestreador. |
| [50] Halvorson JJ, LaMothe J, Martin CR, Grose A, Asprinio DE, Wellman D, and Helfet DL, "Combined acetabulum and pelvic ring injuries," JAAOS, vol. 22, no. 5, pp. 304–314, 2014. | Fuente original del umbral 2–3 mm de desplazamiento acetabular. Umbral citable y mas estricto que el pelvico general. |
| [25] Han R, Uneri A, Vijayan RC, Wu P, Vagdargi P, Sheth N, Vogt S, Kleinszig G, Siewerdsen JH, "Fracture reduction planning and guidance in orthopaedic trauma surgery via multi-body image registration," Medical Image Analysis, vol. 68, p. 101917, 2021. | Fuente de las cifras de comparacion 2–3 mm y 2–3 grados; baseline alternativo de planificacion geometrica. |
| [19] Liu Y, Yibulayimu S, Sang Y, Zhu G, Wang Y, Zhao C, and Wu X, "Pelvic fracture segmentation using a multi-scale distance-weighted neural network," MICCAI 2023, pp. 312–321. | Baseline SOTA de segmentacion de fractura pelvica con el que se compara el Dice 86.2±7.8%; relevante al Objetivo 5 (downstream). |
| [46] District H, "Standardization administration of china," 2014. | Fuente original del criterio "profundidad >= 2.5 veces el radio" del que deriva el factor 8; umbral citable de profundidad de anclaje. |
| [28] Wong JSY, Lau JCK, Chui KH, Tiu KL, Lee KB, and Li W, "Three-dimensional-guided navigation percutaneous screw fixation of fragility fractures of the pelvis," Journal of Orthopaedic Surgery, vol. 27, no. 1, 2019. | Citado como base de planificacion por densidad osea y estadistica multiparametrica; fijacion percutanea navegada en pelvis, cercana a corredores oseos. |
| [9] Moolenaar J, Tumer N, and Checa S, "Computer-assisted preoperative planning of bone fracture fixation surgery: A state-of-the-art review," Front. Bioeng. Biotechnol. 10:1037048, 2022. | Revision del estado del arte del pipeline completo; fuente de la cifra de 36 horas y mapa util para acotar el gap del Objetivo 2. |
| [48] Liu P, Han H, Du Y, Zhu H, Li Y, Gu F, Xiao H, Li J, Zhao C, Xiao L et al. "Deep learning to segment pelvic bones: large-scale CT datasets and baseline models," IJCARS, vol. 16, pp. 749–756, 2021. | Dataset primario de la tesis (CTPelvic1K); confirma que ya hay planificacion geometrica publicada sobre el mismo dataset. |
| [51] Takashi Y and Roberto JM, "Likert scale," Encyclopedia of Gerontology and Population Aging, p. 2938–2941, 2022. | Fuente de la escala Likert de 5 puntos con corte >=3 como aceptable, usada aqui como criterio de evaluacion clinica. |
