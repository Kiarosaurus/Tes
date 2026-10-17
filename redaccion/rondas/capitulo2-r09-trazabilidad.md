# Auditoria de trazabilidad — capitulo2 — r09

Alcance auditado: `overleaf/secciones/capitulo2.tex`:1-126 y la Tabla A.1 que el capítulo presenta,
`overleaf/secciones/anexos.tex`:13-30. Se cotejaron el encargo del 2026-10-16, la respuesta r08, el lint r09,
las decisiones vigentes, las implicancias, las fichas de las 50 claves citadas y los registros propios pertinentes.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | OC-2, G-T4 | `capitulo2.tex`:98 | "cifras de la ablación de Li et al. [...] pendientes de verificar" | `docs/01-decisiones.md`:981-990, fila #71; `docs/literatura/li2024.md`:81,137,196 | Patron PAT-19 reincide. El GAP es injustificado: la decisión vigente ordena explícitamente presentar `li2024` **sin cifras**; por tanto, verificarlas dejó de ser un dato pendiente. | Retirar el `\GAPDATO`. Atribuir solo la afirmación textual de la ficha: la recuperación desde un único dominio no es eficaz; no transcribir ni calcular cifras de la Tabla I. |
| T02 | media | OC-2, G-T4 | `capitulo2.tex`:112; `anexos.tex`:30 | "Queda pendiente el contraste de realismo" | `docs/01-decisiones.md`:2729-2734; `docs/00-tesis.md`:208-212 | Patrones PAT-19 y PAT-180 reinciden. H5 no es un resultado pendiente: la autora decidió que no se ejecuta y pasa a trabajo futuro; la marca y el resumen de la tabla conservan el estado anterior. | Retirar el `\GAPDATO`; decir que el contraste no se ejecutó y queda como trabajo futuro. Aplicar la misma formulación en la Tabla A.1. |
| T03 | alta | G-T4, OC-3 | `capitulo2.tex`:114 | "la comparación con observaciones reales es la del contraste de realismo" | `docs/01-decisiones.md`:2723-2734; `experiments/objetivo3/EXPERIMENTOS.md`:82-85; `experiments/objetivo3/resultados_prueba_v1.md`:50-52 | La oración presenta como existente el contraste H5 que la decisión declara no ejecutado. La comparación con datos reales que sí consta es E-A1, reconstrucción descriptiva de implantes reales; no es H5 ni incluye el protocolo físico. | Indicar que H5 no se ejecutó. Si se conserva la comparación ya hecha, nombrarla como reconstrucción descriptiva E-A1 y remitir a `sec:ap-reconstruccion`. |
| T04 | alta | G-T4, OC-3 | `capitulo2.tex`:100,124 | "La comparación del Objetivo 3 [...] contrasta ese supuesto" | `docs/01-decisiones.md`:2723-2728; `docs/00-tesis.md`:203-212; `experiments/objetivo3/resultados_prueba_v1.md`:10-36 | El alcance atribuido al contraste es más fuerte que lo ejecutado y que la decisión vigente: se contrastó la amplitud local dentro de la banda, no el realismo visual ni la capacidad general de reproducir los efectos de adquisición. "La banda [...] para los efectos de adquisición" repite ese reclamo amplio. | Acotar el contraste a la amplitud local dentro de la banda y declarar que no sostiene equivalencia ni realismo visual. En l. 124 describir solo que la banda extiende la generación fuera de la máscara. |
| T05 | media | OC-2, OC-3 | `capitulo2.tex`:100,102,104,112,114,124,126; `anexos.tex`:30 | "\REVVISUAL{...}" (nueve apariciones) | `docs/01-decisiones.md`:2732-2734; `redaccion/ENCARGO_2026-10-16.md`, apartado "En todos los capítulos" | La decisión ordena retirar `\REVVISUAL` y reescribir esos pasajes como limitación declarada, pero el capítulo conserva siete marcas y la tabla dos. En l. 126 falta además la limitación explícita de que no se reclama realismo visual. | Retirar las nueve macros. Conservar los hechos respaldados de l. 102 y 104; reescribir T02-T04 y añadir en el cierre que el realismo visual no se reclama y es limitación del Objetivo 3. |

TOTAL alta=2 media=3 baja=0

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| `capitulo2.tex`:8-10 | Función, orden y relación de las secciones con los objetivos | Organización del capítulo; `overleaf/secciones/introduccion.tex` | si |
| `capitulo2.tex`:12 | Revisión narrativa dirigida, fichas por fuente y búsquedas registradas | `redaccion/MAPA.md`:23-28; `docs/literatura/_index.md` | si |
| `capitulo2.tex`:12,60 | Una fuente disponible solo como resumen y sin cifras citadas | `docs/literatura/zhang2026pediclescrew.md`; `_index.md` (ABSTRACT) | si |
| `capitulo2.tex`:16 | Dos familias de síntesis por difusión y claves que las componen | fichas `chen2024tumorsynthesis`, `ramzan2026claim`, `jacob2026lgesynthnet`, `zhang2025lefusion`, `zhang2025diffboost`, `konz2024anatomicallycontrollable` | si |
| `capitulo2.tex`:16 | Rayas que irradian desde el metal | `deman1999`, Evidencia textual, Sec. III-D, p. 694 | si |
| `capitulo2.tex`:18 | DiffTumor: condicionamiento, región sana, alcance y `[-175,250]` HU | `chen2024tumorsynthesis`, Evidencia textual, Sec. 3.2 y Ap. E.2 | si |
| `capitulo2.tex`:18 | Dice 62.5 a 66.5 %, cinco particiones, una de tres redes | `chen2024tumorsynthesis`, Evidencia textual, Tabla 4 | si |
| `capitulo2.tex`:18 | Cuatro radiólogos y cerca de la mitad tomada por real | `chen2024tumorsynthesis`, Evidencia textual, Sec. 4.1 | si |
| `capitulo2.tex`:20 | Ramzan: imagen, pérdida en máscara, fondo recompuesto y LeFusion | `ramzan2026claim`, Evidencia textual; `zhang2025lefusion`, "Qué hace" | si |
| `capitulo2.tex`:20 | Dice 58.89 a 63.53; sin fidelidad; fondo cualitativo | `ramzan2026claim`, Evidencia textual | si |
| `capitulo2.tex`:22 | LGESynthNet, ControlNet, bordes, región enmascarada y decodificación completa | `jacob2026lgesynthnet`, Evidencia textual, Sec. 3.1 | si |
| `capitulo2.tex`:22 | Cicatriz menor del 1 %, SSIM global y atribución a compresión | `jacob2026lgesynthnet`, Evidencia textual, Sec. 1, 4.4 y 5 | si |
| `capitulo2.tex`:24 | DiffBoost: modelo, condiciones, mezcla aleatoria y corte completo | `zhang2025diffboost`, Evidencia textual, Alg. 1 | si |
| `capitulo2.tex`:24 | Dice 78.46/84.56, 94.42/94.78 y 62.92/71.65 % | `zhang2025diffboost`, Evidencia textual, Tabla II | si |
| `capitulo2.tex`:24 | Konz: máscara concatenada, `[0,255]`, Dice 0.8980, 40 pacientes | `konz2024anatomicallycontrollable`, Evidencia textual | si |
| `capitulo2.tex`:26 | Hu: efecto hasta 1.3 radios | `hu2023`, Evidencia textual, Tabla 1 | si |
| `capitulo2.tex`:26 | Jin: parche 3D y supervisión de borde; Wu: exterior conservado | `jin2021freetumor`, Evidencia textual, Sec. 3.4.1; `wu2025freetumor`, Sec. 4.2 | si |
| `capitulo2.tex`:28 | RePaint: región conocida, remuestreo, sin reentrenar, 256 x 256 | `lugmayr2022repaint`, Evidencia textual | si |
| `capitulo2.tex`:28 | Sintetizador propio: pérdida local, sin recomponer cada paso | `docs/01-decisiones.md`, 2026-10-08 pto. 5; `capitulo3.tex`, `sec:sintetizador` | si |
| `capitulo2.tex`:30 | Cinco modelos con segmentación; dos con similitud; uno con radiólogos | fichas de las cinco claves citadas | si |
| `capitulo2.tex`:34 | Zhang y Yu: 15 formas, 120 kVp, Poisson; dos mecanismos no mencionados | `zhang2018`, Evidencia textual y filas NO ENCONTRADO | si |
| `capitulo2.tex`:34 | Lin: 100 formas y volumen parcial | `lin2019`, Evidencia textual, p. 10508 | si |
| `capitulo2.tex`:34 | Wang: máscara tubular, 1090 volúmenes, Beer-Lambert, cinco energías | `wang2019cochlear`, Evidencia textual | si |
| `capitulo2.tex`:34 | Karageorgos: objetos desde TC de metal y CatSim/XCIST | `karageorgos2024ddpm`, Evidencia textual; `wu2022xcist` | si |
| `capitulo2.tex`:36 | 31 % de equipos AAPM usó difusión | `haneda2025aapm`, Evidencia textual, Sec. 3.1 | si |
| `capitulo2.tex`:36 | DDPM de sinograma; SSIM 0.964; 13 de 28 métricas | `karageorgos2024ddpm`, Evidencia textual, Tabla I y Sec. III-C | si |
| `capitulo2.tex`:38 | Yun: método, CLINIC-metal inferido, máscara y 0.82/3.18-6.30 HU | `yun2026simulationdriven`, Evidencia textual, Tabla 4; `docs/02-datos.md` | si |
| `capitulo2.tex`:40 | U-DuDoNet: componentes aditivos en sinograma e imagen, TC verosímil | `lyu2021ududonet`:47-57, Evidencia textual | si |
| `capitulo2.tex`:40 | PND-Net: ruta aprendida y objeción a sumar artefacto arbitrario | `xia2024pndnet`:54-90, Evidencia textual | si |
| `capitulo2.tex`:40 | Sin geometría/pose ni evaluación de la imagen sintetizada; clínica visual | `lyu2021ududonet`:103-106; `xia2024pndnet`:148-150 | si |
| `capitulo2.tex`:42 | Peters: fantoma, 14 000 casos, ocho métricas, 29 escenarios | `peters2025hybrid`, Evidencia textual, Sec. 2.3 y 3.1; `haneda2025aapm` | si |
| `capitulo2.tex`:42 | Desviaciones <2 %, <10 % y hasta 13.3 % | `peters2025hybrid`, Evidencia textual, Sec. 3.1 | si |
| `capitulo2.tex`:44 | Validación no cubre paso híbrido, geometría ni 3D pélvica | `peters2025hybrid`, Evidencia textual, Abstract y Sec. 2.3 | si |
| `capitulo2.tex`:46 | Colocación: Peters aleatoria; Karageorgos 50 %/200 HU; Wang anatómica/manual | fichas `peters2025hybrid`, `karageorgos2024ddpm`, `wang2019cochlear`, `wang2025adaptiveweighting` | si |
| `capitulo2.tex`:48 | XCIST como fundamento; varillas 20/10 mm; >3.0 cm; 274/14 000 | `CLAUDE.md`; `wu2022xcist`, Evidencia textual; `haneda2025aapm`, Sec. 4 | si |
| `capitulo2.tex`:50 | Ren: sonda, Ti 12.7 mm, dos casos, proyecciones del fabricante | `ren2022metalinsertion`, Evidencia textual | si |
| `capitulo2.tex`:56 | Liu: 14 casos y procedimiento de planificación | `liu2025pipeline`, Evidencia textual, Sec. IV-A | si |
| `capitulo2.tex`:56 | 2.56 mm, 3.31 grados; 12 casos; 86.7 %; tres cirujanos | `liu2025pipeline`, Evidencia textual, Sec. IV-B y Tabla III | si |
| `capitulo2.tex`:56 | 10.58 ± 3.84 frente a 4.36 ± 3.83 mm | `liu2025pipeline`, Evidencia textual, Tabla III | si |
| `capitulo2.tex`:56 | Sin iliosacros; no aplica a fracturas de sacro | `liu2025pipeline`, Evidencia textual y restricción | si |
| `capitulo2.tex`:58 | Goerres: atlas de 12 pelvis femeninas y tornillos futuros | `goerres2017planning`, Evidencia textual, Sec. 3.1.1 y 5 | si |
| `capitulo2.tex`:58 | Han: 40 pelvis, S1/S2 y cilindro recto | `han2019atlasplanning`, Evidencia textual, Sec. 2.1.1, 2.3.1 y 4 | si |
| `capitulo2.tex`:58 | Yang: 10 pelvis, sin atlas, canal en arco por S1 | `yang2022computeraided`, Evidencia textual, Sec. 2.1-2.2 y 5 | si |
| `capitulo2.tex`:62 | Ramzan 17 segmentos; Chen y Jacob con elipsoides | fichas `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet` | si |
| `capitulo2.tex`:64 | Zwingmann 2009: cuatro niveles, 69/40 %, p=0.02 | `zwingmann2009navigated`, Evidencia textual | si |
| `capitulo2.tex`:66 | Metaanálisis: 2.6 % (1832), 0.1 % (262), cero y criterio de revisión | `zwingmann2013`, Evidencia textual | si |
| `capitulo2.tex`:68 | Zwingmann 2010: n y distribuciones completas, grado 4 y posible solape | `zwingmann2010percutaneous`, Evidencia textual; DEC 2026-10-08 pto. 31 | si |
| `capitulo2.tex`:70 | Herman: 36.5/14.8 %, p=0.035, binaria y ninguno fuera | `herman2016`, Evidencia textual | si |
| `capitulo2.tex`:70 | Segundo corredor descriptivo; grado 3; S1 asumido | `capitulo3.tex`, `sec:poses`, `sec:sap`, `sec:amenazas` | si |
| `capitulo2.tex`:72 | Kaiser 104 TC; McLaren 433/352; Ramadanov cualitativo | fichas `kaiser2014dysmorphism`, `mclaren2021corridor`, `ramadanov2025safezone` | si |
| `capitulo2.tex`:74 | Gardner: 50 TC y 222/346 mm² | `gardner2010safezones`, Evidencia textual, p. 624 | si |
| `capitulo2.tex`:74 | Ziran: 17 pelvis, 7-25 % y 97-140 % | `ziran2007fluoroscopic`, Evidencia textual | si |
| `capitulo2.tex`:76 | Cuatro carencias y negativo acotado a fuentes revisadas | síntesis de `capitulo2.tex`:54-74 | si |
| `capitulo2.tex`:78 | Escalas de Zwingmann, Smith, Herman y margen de Liu | fichas `zwingmann2009navigated`, `smith2006iliosacral`, `herman2016`, `liu2025pipeline` | si |
| `capitulo2.tex`:78 | SAP usa solo perforación | `docs/01-decisiones.md`, 2026-10-08 pto. 15; `capitulo3.tex`, `sec:sap` | si |
| `capitulo2.tex`:80 | Arand: 50 TC post mortem, relación S1 y ausencia de HU | `arand2019pelvicring`, Evidencia textual | si |
| `capitulo2.tex`:80 | Densidad fuera de SAP y como trabajo futuro | `docs/01-decisiones.md`, 2026-10-08 pto. 14 | si |
| `capitulo2.tex`:82 | Tres de ocho métricas e inversión de lectura | `peters2025hybrid`; DEC 2026-10-05 (3)-(4) y 2026-10-08 pto. 10 | si |
| `capitulo2.tex`:86 | Saturaciones hasta 600 HU y umbral de 2500 HU | fichas `chen2024tumorsynthesis`, `hu2023`, `jin2021freetumor`, `wu2025freetumor`, `wang2025adaptiveweighting`, `li2024` | si |
| `capitulo2.tex`:88 | Tres ventanas, cascada y métricas 26.76/0.9501 frente a 32.67/0.9803 | `wang2025adaptiveweighting`, Evidencia textual | si |
| `capitulo2.tex`:88 | 14 volúmenes, cinco médicos, 30 imágenes | `wang2025adaptiveweighting`, Evidencia textual | si |
| `capitulo2.tex`:88 | `\GAPLIT` de fuente primaria multiventana | solo `refs/raw/niu2021multiple.bib`; no hay ficha `docs/literatura/niu2021multiple.md` | si, justificado |
| `capitulo2.tex`:90 | Li: pérdida/evaluación multiventana, `[-1000,2000]`, +0.64 dB | `li2024`, Evidencia textual | si |
| `capitulo2.tex`:92 | Ida y vuelta medida; asinh en 32 bits | `experiments/objetivo1/p1_compuerta.md`; DEC 2026-10-08 pto. 1 | si |
| `capitulo2.tex`:94 | Rombach; Chen `[-1000,1000]`; Guo sin rango declarado | fichas `rombach2022latentdiffusion`, `chen2026foundationvae`, `guo2025maisi` | si |
| `capitulo2.tex`:96 | RMSE 12.3, 20.2 y 12.74, sin unidad añadida | fichas `karageorgos2024ddpm`, `peters2025hybrid`, `yun2026simulationdriven` | si |
| `capitulo2.tex`:98 | De Man y Lin; PSNR 31.45 frente a 33.51 dB | fichas `deman1999`, `lin2019` | si |
| `capitulo2.tex`:98 | Li solo imagen por debajo de cuatro dominios | `li2024`:81,137-143 | si; el GAP no (T01) |
| `capitulo2.tex`:100 | MAR no pareada usa sinograma y no evalúa síntesis | `lyu2021ududonet`:103-104; `xia2024pndnet`:148-149 | si |
| `capitulo2.tex`:100 | Alcance atribuido al contraste propio | DEC 2026-10-16; resultados v1 | no (T04) |
| `capitulo2.tex`:102 | Mecanismos y extensión cualitativa; Selles n=25 | fichas `deman1999`, `park2015ct`, `glover1980nonlinear`, `selles2023ai`, `li2024` | si |
| `capitulo2.tex`:102 | Banda trunca por diseño efectos lejanos | `docs/01-decisiones.md`:990 | si |
| `capitulo2.tex`:104 | Radzi: cuatro distancias, calibres y un tobillo | `radzi2014metalartifacts`, Evidencia textual | si |
| `capitulo2.tex`:104 | Cassanego: 3.1-4.2 mm, calibres y seis miembros | `cassanego2026evolution`, Evidencia textual | si |
| `capitulo2.tex`:104 | Banda de unos 12 mm como convención | `CLAUDE.md`; decisiones vigentes del sintetizador | si |
| `capitulo2.tex`:104 | Componentes 500-4000 mm³; anillos; entrenamiento/validación; 10 mm | `capitulo3.tex`, `sec:v2`; `experiments/objetivo3/EXPERIMENTOS.md`:93-95 | si |
| `capitulo2.tex`:106 | Karageorgos: 7.57, 11.45 (1.4x), 54.82 (0.7x) | `karageorgos2024ddpm`, Evidencia textual | si |
| `capitulo2.tex`:110 | Diez trabajos y estructura de la tabla | `anexos.tex`:19-30 | si |
| `capitulo2.tex`:112 | SAP y muestreador ejecutados; v1 comparada; v2 exploratoria | `capitulo3.tex`:38; DEC 2026-10-15 (3) pto. 5 | si |
| `capitulo2.tex`:112 | Contraste H5 pendiente | DEC 2026-10-16 pto. 2 | no (T02) |
| `capitulo2.tex`:114 | Síntesis comparativa de columnas; validación de Peters | cuerpo del capítulo; `peters2025hybrid`, Evidencia textual | si |
| `capitulo2.tex`:114 | Contraste con observaciones reales existente | DEC 2026-10-16; registros E-A1/H5 | no (T03) |
| `capitulo2.tex`:116 | Brecha acotada y precedente MAR no pareada | DEC 2026-10-15 (3) pto. 9; fichas Lyu/Xia | si |
| `capitulo2.tex`:118 | Primario, Ti, n=13, sin metal, eje sin perturbar y cordura | `resultados_prueba_v1.md`:10-36; `docs/00-tesis.md`:186-196 | si |
| `capitulo2.tex`:118 | Protocolo físico 2D/una fila; sintetizador sobre TC reconstruida | DEC 2026-10-08 pto. 25; `capitulo3.tex`, `sec:ap-sintesis` | si |
| `capitulo2.tex`:118 | No concluyente y sintetizador por debajo; lectura posterior | `resultados_prueba_v1.md`:34-37; `docs/00-tesis.md`:162-165,202-204 | si |
| `capitulo2.tex`:120 | Geometría, muestreador preinscrito y comparación sin ajuste | `preinscripcion_muestreador.md`; `capitulo3.tex`, `sec:geometria`, `sec:poses` | si |
| `capitulo2.tex`:120 | Codificación y banda; ningún objetivo las aísla | DEC 2026-10-08 pto. 30; `introduccion.tex` | si |
| `capitulo2.tex`:122 | Precedentes de máscaras y Xie 2500 HU/100 %/82.92 % | fichas citadas, en particular `xie2024implantsegmentation` | si |
| `capitulo2.tex`:122 | Entrenamiento con máscaras umbralizadas y desplazamiento de dominio | DEC 2026-10-08 ptos. 6-7; implicancia #128.4 | si |
| `capitulo2.tex`:124 | Piezas publicadas y combinación propia | fichas citadas; DEC 2026-10-08 pto. 30 | parcial (T04) |
| `capitulo2.tex`:126 | Supuesto, convención y evaluación física/quirúrgica | `docs/00-tesis.md`:203-212, Fuera de alcance; decisiones vigentes | parcial (T05: falta limitación y sobra macro) |
| `anexos.tex`:19 | Fila Chen | `capitulo2.tex`:18; `chen2024tumorsynthesis` | si |
| `anexos.tex`:20 | Fila Ramzan | `capitulo2.tex`:20,62; `ramzan2026claim` | si |
| `anexos.tex`:21 | Fila Jacob | `capitulo2.tex`:22,62; `jacob2026lgesynthnet` | si |
| `anexos.tex`:22 | Fila Zhang/DiffBoost | `capitulo2.tex`:24; `zhang2025diffboost` | si |
| `anexos.tex`:23 | Fila Peters | `capitulo2.tex`:42,46; `peters2025hybrid` | si |
| `anexos.tex`:24 | Fila Karageorgos | `capitulo2.tex`:34,36,46; `karageorgos2024ddpm` | si |
| `anexos.tex`:25 | Fila Lyu | `capitulo2.tex`:40; `lyu2021ududonet`:47-57,103-104 | si |
| `anexos.tex`:26 | Fila Liu | `capitulo2.tex`:56; `liu2025pipeline` | si |
| `anexos.tex`:27 | Fila Zwingmann | `capitulo2.tex`:64; `zwingmann2009navigated` | si |
| `anexos.tex`:28 | Fila Wang multiventana | `capitulo2.tex`:46,88; `wang2025adaptiveweighting` | si |
| `anexos.tex`:30 | Fila propia: método, SAP, v1, n=13, desenlace y cordura | `capitulo2.tex`:112-126; fuentes propias ya inventariadas | parcial (T02, T05) |
| todo | Las 50 claves `\cite` existen en `overleaf/referencias.bib`; apellidos coinciden; ninguna cita es sujeto aislado | `overleaf/referencias.bib` | si |
| todo | Fuentes de fabricante tratadas como literatura primaria | no hay fuentes de fabricante citadas en la sección | si |
| todo | Contenido retirado: downstream como objetivo, ControlNet/latente vigente, 31-60 %, BFC/ISC | búsqueda en `capitulo2.tex`; Dice, ControlNet y latente solo describen trabajos ajenos | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que sigue pendiente después de una decisión que lo cierra o excluye | OC-2, G-T4 | "Queda pendiente el contraste de realismo" | PAT-19 |
| Capítulo cerrado no recotejado después de una decisión transversal nueva | G-T4 | "la comparación con observaciones reales es la del contraste de realismo" | PAT-180 |
| Al cerrar un GAP, la prosa y tabla que repiten el estado viejo quedan sin revisar | G-T4, G-C7 | "contraste de realismo pendiente" | PAT-168 |
