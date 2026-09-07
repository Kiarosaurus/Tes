# Candidatos de snowballing

> Papers citados DENTRO de los que ya lei, que podrian importar.
> Claude los agrega al leer. La autora decide LEER o DESCARTAR.
> Al decidir LEER, la entrada pasa a `_index.md` y se descarga el PDF.

Estados: PENDIENTE | LEER | DESCARTADO

Todos los de abajo salieron de la ronda de 10 lecturas del 2026-09-06. Ninguno se
busco fuera del PDF donde aparece: se transcriben tal como los cita la fuente.

## Prioridad maxima — la cadena de la escala de brecha cortical

Las tres fuentes N1 de la tesis (`smith2006iliosacral`, `zwingmann2009navigated` y,
probablemente, `zhang2026pediclescrew`) usan la MISMA escala 0/<2/2-4/>4 mm, y ninguna es
su origen. Sin el ancestro, BFC se cita desde una fuente secundaria.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Gertzbein SD, Robbins SE. Accuracy of pedicular screw placement in vivo. Spine 1990;15:11-4 | smith2006iliosacral (ref. 7) | **Candidata a FUENTE ORIGINAL de la escala 0-3 con umbrales de 2 y 4 mm.** Es el ancestro probable de BFC y, si se confirma, cierra la implicancia #4: las dos escalas que parecian competir descenderian de aqui | 1 | PENDIENTE |
| Vaccaro AR, Rizzolo SJ, Balderston RA, et al. Placement of pedicle screws in the thoracic spine. Part II. JBJS Am 1995;77:1200-6 | smith2006iliosacral (ref. 6) | Segunda de las tres fuentes que Smith cita como origen del metodo de graduacion | 2 | PENDIENTE |
| Mirza SK, Wiggins GC, Kuntz Ct, et al. Accuracy of thoracic vertebral body screw placement. A cadaver study. Spine 2003;28:402-13 | smith2006iliosacral (ref. 8) | Tercera fuente de la escala; ademas diseno cadaverico comparativo | 3 | PENDIENTE |

## Prioridad maxima — el origen real del 2%-15%

`zwingmann2009navigated` NO mide ese rango: lo cita. Si la tesis lo usa, debe citarlo
desde aqui. Ver implicancia #12.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Hinsche AF, Giannoudis PV, Smith RM. Fluoroscopy-based multiplanar image guidance for insertion of sacroiliac screws. Clin Orthop Relat Res. 2002;395:135-144 | zwingmann2009navigated (ref. 13), smith2006iliosacral (ref. 2) | **Fuente original del rango 2%-15% de malposicion**, el unico rango que ambas fuentes N1 escriben literalmente. Aparece en las dos lecturas | 1 | PENDIENTE |
| Templeman D, Schmidt A, Freese J, Weisman I. Proximity of iliosacral screws to neurovascular structures after internal fixation. Clin Orthop Relat Res. 1996;329:194-198 | zwingmann2009navigated (ref. 28), smith2006iliosacral (ref. 3) | Segunda fuente del 2%-15% **y fuente del umbral angular de 4 grados** que `zwingmann2009navigated` cita como limite de dano neurovascular. Toca SAP directamente | 1 | PENDIENTE |
| van den Bosch EW, van Zwienen CM, van Vugt AB. Fluoroscopic positioning of sacroiliac screws in 88 patients. J Trauma. 2002;53:44-48 | zwingmann2009navigated (ref. 32), smith2006iliosacral (ref. 4) | Fuente de la incidencia de lesion neurologica 0.5%-7.7%, con n=88, la serie clinica mas grande de la cadena. Reporta mayor riesgo en S2 | 2 | PENDIENTE |

## Prioridad alta — tocan una implicancia ABIERTA

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| McLaren, D.A.; Busel, G.A.; Parikh, H.R.; et al. Corridor-diameter-dependent angular tolerance for safe transiliosacral screw placement: An anatomic study of 433 pelves. Eur. J. Orthop. Surg. Traumatol. 2021, 31, 1485-1492 | ramadanov2025safezone | **Es la posible solucion a la implicancia #7.** Fuente original de las tolerancias 1.53 grados (S1) y 1.02 grados (S2) y del ~31% sin corredor viable, sobre 433 pelvis. Es la candidata mas fuerte a definicion OPERACIONAL de zona segura, que es justo lo que `ramadanov2025safezone` no da | 1 | PENDIENTE |
| Herman, A.; Keener, E.; Dubose, C.; Lowe, J.A. Simple mathematical model of sacroiliac screws safe-zone-Easy to implement by pelvic inlet and outlet views. J. Orthop. Res. 2017, 35, 1478-1484 | ramadanov2025safezone | Modelo geometrico de zona segura: compite directamente con el muestreador. Fuente original del 32% de brechas corticales en 156 tornillos, cifra vecina del 31-60% de `zwingmann2009navigated` | 1 | PENDIENTE |
| Tejwani, N.C.; Raskolnikov, D.; McLaurin, T.; Takemoto, R. The role of computed tomography for postoperative evaluation of percutaneous sacroiliac screw fixation and description of a "safe zone". Am. J. Orthop. 2014, 43, 513-516 | ramadanov2025safezone | Fuente original del umbral **>2.7 mm** de penetracion foraminal asociado a deficit neurologico, y de la tasa 23/51. Umbral candidato para BFC e ISC; engancha con la implicancia #4 (umbral de 2 mm de `zhang2026pediclescrew`) | 1 | PENDIENTE |
| AAPM CT Metal Artifact Reduction (CT-MAR) grand challenge benchmark tool. GitHub, xcist/example/tree/main/AAPM_datachallenge | haneda2025aapm | **Toca la implicancia #8.** Herramienta de scoring y rutina FBP/reproyeccion en Python. Podria validar la reimplementacion de XCIST, o reemplazarla como brazo de comparacion ya parametrizado | 2 | PENDIENTE |
| AAPM CT Metal Artifact Reduction (CT-MAR) Grand Challenge Scoring Metrics. GitHub, AAPM_datachallenge/scoring_metric.md | haneda2025aapm | Definiciones matematicas y umbrales operativos de las ocho metricas del reto, incluidas *bone integrity* (150 HU) y *metal integrity* (+250 HU). Reutilizable para BFC e ISC | 2 | PENDIENTE |
| Fan, Y.; Pack, J.; De Man, B. A virtual imaging trial framework to study cardiac CT blooming artifacts. SPIE 2022 | haneda2025aapm, karageorgos2024ddpm | **Toca las implicancias #8 y #9.** Es la validacion citada de que CatSim produce artefactos realistas. Aparece en dos lecturas independientes como la fuente de esa afirmacion. Si el respaldo del realismo de CatSim es debil, cambia el peso del brazo de comparacion | 2 | PENDIENTE |
| Zhang, Y.; Yu, H. Convolutional neural network based metal artifact reduction in X-ray computed tomography. IEEE TMI 2018, 37(6), 1370-1381 | ren2022metalinsertion, yun2026simulationdriven, karageorgos2024ddpm | **Toca la implicancia #9.** Aparece en TRES lecturas independientes como el origen del banco de mascaras/formas metalicas usado para insertar metal sinteticamente. Es la fuente de facto de la geometria de implantes en toda esta literatura, y el punto de comparacion natural del banco propio de 61 geometrias | 1 | PENDIENTE |

## Prioridad media — compiten con un componente

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Goerres, J.; Uneri, A.; Jacobson, M.; et al. Planning, guidance, and quality assurance of pelvic screw placement using deformable image registration. Phys. Med. Biol. | liu2025pipeline | Planificacion y control de calidad de colocacion de tornillos pelvicos. Compite con el muestreador por una via distinta a la de `liu2025pipeline` (registro deformable, no optimizacion geometrica) | 2 | PENDIENTE |
| Yang, W.; Feng, S.; Song, J.; et al. Computer-aided automatic planning and biomechanical analysis of a novel arc screw for pelvic fracture internal fixation. Comput. Methods Programs Biomed. 2022, 220, 106810 | liu2025pipeline | Planificacion automatica de tornillo en fractura pelvica; competidor directo del Objetivo 2 | 2 | PENDIENTE |
| Aregger, F.C.; Gewiess, J.; Albers, C.E.; et al. Evaluation of the true lateral fluoroscopic projection for the relation of the S1 recess/foramen to safe corridors in transiliac-transsacral screw placement in human cadaveric pelves. Eur. J. Orthop. Surg. Traumatol. 2024, 35, 31 | ramadanov2025safezone | Define zona segura por la diagonal del cuerpo de S1 y reporta 10/14 pelvis con corredor viable. Definicion geometrica alternativa; segunda opcion si McLaren no sirve | 2 | PENDIENTE |
| Ferrero, A.; et al. Technical note: insertion of digital lesions in the projection domain for dual-source, dual-energy CT. Med. Phys. 2017, 44(5), 1655-1660 | ren2022metalinsertion | Fuente original del marco de insercion en dominio de proyeccion que `ren2022` extiende. Antecedente aun mas antiguo de la insercion sintetica (implicancia #9) | 2 | PENDIENTE |
| Chen, B.; et al. Lesion insertion in the projection domain: methods and initial results. Med. Phys. 2015, 42(12), 7034-7042 | ren2022metalinsertion | Segunda fuente base del pipeline de insercion; define el estandar de validacion "insertar y comparar contra el real", que es un protocolo directamente reutilizable | 2 | PENDIENTE |
| De Man, B.; et al. Metal streak artifacts in X-ray computed tomography: a simulation study. IEEE Trans. Nucl. Sci. 1999, 46(3), 691-696 | ren2022metalinsertion, karageorgos2024ddpm | Fuente clasica de los mecanismos fisicos (photon starvation, beam hardening, bandas oscuras) y de la contribucion Compton. Cuestiona el supuesto de dispersion despreciable de `ren2022`, que es donde cuelga la frase que sostiene el gap | 2 | PENDIENTE |
| Choi, D.; Yun, S.; Hyun, S.; Cho, S. Metal artifact reduction algorithm with conditional latent diffusion model for dental cone-beam CT. J. Appl. Clin. Med. Phys. 2025, 26, e70317 | yun2026simulationdriven | LDM **condicional** aplicado a artefactos metalicos, del mismo grupo. Precedente metodologico directo del renderizador; toca el reclamo de novedad (implicancia #9) | 2 | PENDIENTE |
| Fan, F.; Ritschl, L.; Beister, M.; et al. Simulation-driven training of vision transformers enables metal artifact reduction of highly truncated CBCT scans. Med. Phys. 2021, 51(5), 3360-3375 | haneda2025aapm | Otro caso de entrenamiento guiado por simulacion de artefacto metalico. Suma a la implicancia #9 | 3 | PENDIENTE |
| Hu, Q.; Chen, Y.; Xiao, J.; et al. Label-free liver tumor segmentation. CVPR 2023 | chen2024tumorsynthesis | Sintesis basada en modelo, no aprendida: es la alternativa analitica dentro del paradigma de sintesis de lesiones, y el unico baseline generativo de DiffTumor. Util para encuadrar "generativo vs analitico" | 2 | PENDIENTE |
| Lin, W.-A.; et al. DuDoNet: dual domain network for CT metal artifact reduction. CVPR 2019 | ren2022metalinsertion | Consumidor tipico de datos sinteticos de metal; util para definir el protocolo de datos de la tarea aguas abajo | 3 | PENDIENTE |

| Lee PY, Lai JY, Hu YS, et al. Virtual 3D planning of pelvic fracture reduction and implant placement. Biomed Eng Appl Basis Commun 2012;24(03):245-262 | liu2021ctpelvic1k | Planificacion virtual 3D de colocacion de implante en fractura pelvica: tercer competidor directo del muestreador, junto a `liu2025pipeline` y Goerres | 2 | PENDIENTE |
| Day AC, Stott PM, Boden BP. The accuracy of computer-assisted percutaneous iliosacral screw placement. Clin Orthop Relat Res. 2007;463:179-186 | zwingmann2009navigated (ref. 8) | Tasa de perforacion cortical en cadaver (2 de 10 tornillos); baseline experimental de exactitud iliosacra | 2 | PENDIENTE |
| Goldberg BA, Lindsey RW, Foglar C, et al. Imaging assessment of sacroiliac screw placement relative to the neuroforamen. Spine 1998;23:585-589 | zwingmann2009navigated (ref. 12) | Metrica de posicion relativa al neuroforamen: posible componente de SAP que hoy no existe | 2 | PENDIENTE |
| Tile M, Pennal GF. Pelvic disruption: principles of management. Clin Orthop Relat Res. 1980;151:56-64 | zwingmann2009navigated (ref. 29) | Clasificacion Tile/Pennal B y C usada como criterio de inclusion; define la poblacion anatomica sobre la que el muestreador deberia operar | 3 | PENDIENTE |
| CT Metal Artifact Reduction (CT-MAR): An AAPM Grand Challenge. aapm.org/GrandChallenge/CT-MAR/ | peters2025hybrid (ref. 35) | Fuente institucional de la definicion oficial de las metricas. **Contiene el mapeo a la escala 0-4 que NO esta en el PDF de `peters2025hybrid`**; imprescindible si se cita la escala | 2 | PENDIENTE |
| FitzGerald P, et al. Semiempirical, parameterized spectrum estimation for x-ray computed tomography. Med Phys 2021;48(5):2199-2213 | wu2022xcist | Fuente original del modelo de espectro de XCIST y del unico rango validado (80-140 kV). Necesaria si se reimplementa el brazo fisico (implicancia #8) | 2 | PENDIENTE |
| Abadi E, et al. DukeSim: A Realistic, Rapid, and Scanner-Specific Simulation Framework in Computed Tomography. IEEE TMI 2019;38(6):1457-65 | wu2022xcist | Simulador competidor scanner-specific. Si XCIST no sirve como brazo de comparacion (#8 agravada), este es el reemplazo mas obvio | 2 | PENDIENTE |
| Isensee F, Jager PF, Kohl SA, et al. Automated design of deep learning methods for biomedical image segmentation (nnU-Net). arXiv:1904.08128 | liu2021ctpelvic1k | Es la arquitectura exacta del baseline downstream de CTPelvic1K. Imprescindible para el Objetivo 5: sin ella no hay contra que comparar Dice | 2 | PENDIENTE |

## Prioridad media — marco anatomico y pose

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Tsumura et al. 2005 (simulacion de colocacion optima con tolerancia de 5 grados) | vanbosse2011pelvicpositioning | Simula colocacion optima con una tolerancia angular explicita; compite conceptualmente con el muestreador y da un umbral de tolerancia citable | 2 | PENDIENTE |
| Lembeck et al. 2005 (el tilt pelvico degrada la navegacion de implantes) | vanbosse2011pelvicpositioning | El caso mas cercano a malposicion causada por error de referencia; conecta el marco de coordenadas con la tasa de malposicion, que es el benchmark del minimo viable | 2 | PENDIENTE |
| McKibbin 1970 (definicion de posicion anatomica pelvica) | vanbosse2011pelvicpositioning | Define el marco anatomico operacionalizado con landmarks oseos visibles en CT (sinfisis y ambas EIAS). Solo importa si se decide reportar la pose en marco anatomico y no en el marco del CT | 3 | PENDIENTE |

## Reglas para proponer un candidato

Solo se propone si cumple al menos una:
- Es la fuente original de una cifra, escala o umbral que yo pienso citar.
- Es un metodo que compite directamente con el muestreador o el renderizador.
- Reporta la tasa clinica de malposicion o de brecha cortical.
- Define una metrica que podria reemplazar o validar SAP, BFC o ISC.
- Cualquier trabajo que pudiera hacer que mi gap sea MENOR de lo que afirmo,
  que ya haya intentado algo parecido, o que contradiga alguno de mis supuestos.
  Estos son los candidatos MAS importantes, no los menos.

No se proponen papers "de contexto general" ni surveys adicionales.

## Descartados en el filtrado (para que no se vuelvan a proponer)

Las 10 lecturas arrojaron mas de 60 referencias. Se descartaron por la regla de
"contexto general o survey": revisiones de estado del arte (Moolenaar 2022,
Gjesteby 2016, Stradiotti 2009), fuentes metodologicas genericas (SSIM de Wang 2004,
DDIM de Song 2021, VQGAN de Esser 2021, RePaint, Palette, escala Likert), baselines
de MAR ya cubiertos por `selles2024marreview` (NMAR de Meyer 2010, DICDNet,
InDuDoNet+, O-MAR, Huang 2015), y datasets alternativos que no reemplazan a
CTPelvic1K (DeepLesion, AbdomenAtlas-8K, LDCT-and-Projection-data).

Excepcion: **NMAR (Meyer et al. 2010)** aparecio en tres lecturas y es el ancla de
calibracion de la escala 0-4 del reto AAPM (NMAR = 2). Si se adopta ese protocolo de
evaluacion (implicancia #8, opcion 3), deja de ser contexto y pasa a ser
imprescindible. Queda anotado aqui, no en la tabla, hasta que esa decision se tome.
