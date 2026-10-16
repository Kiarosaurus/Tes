# Auditoria de trazabilidad — capitulo2 — r08

Alcance: `overleaf/secciones/capitulo2.tex` completo (l. 1-116) y la fila "Este trabajo" de la Tabla `tab:comparacion`
(`overleaf/secciones/anexos.tex`:29), que l. 104 presenta como parte del capitulo. Lint r08: PASA (0/0/0), GAP lit = 1,
dato = 2, dec = 2. El texto auditado es el que dejo la respuesta r07 (sin cambios posteriores).

Encargo: `redaccion/ENCARGO_2026-10-15b.md` (E1 `\REVVISUAL` para #193; E2 cerrar `\GAPDEC` con DEC 2026-10-15 (3)
ptos 8 y 9; E3 `\GAPLIT` donde falte fuente). Respuesta r07 leida: nada RECHAZADO; T05 (r07) quedo ESCALADO y hoy lo
resuelve DEC (3) pto 9.

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC = `docs/01-decisiones.md`;
DEC15 = DEC 2026-10-15 (l. 2559-2634); DEC15-3 = DEC 2026-10-15 (3) (l. 2650-2694); DEC1013 = DEC 2026-10-13
(l. 2498-2521); IMP = `docs/04-implicancias.md`; RP1 = `experiments/objetivo3/resultados_prueba_v1.md`;
EXP3 = `experiments/objetivo3/EXPERIMENTOS.md`; ANX = `overleaf/secciones/anexos.tex`; BIB = `overleaf/referencias.bib`.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | OC-2, G-T4 | l. 56, oracion 4 | "Yang et al.\ \GAPDEC{clave bibliográfica de Yang et al. 2022 pendiente de la autora (implicancia 192)}" | DEC15-3 pto 8 ("La clave de Yang et al. 2022 ... es `yang2022computeraided`"); IMP #192 (DECIDIDA, l. 12415) y #180 (CERRADA, l. 12152); BIB l. 1453 (`yang2022computeraided`, primer autor "Yang, Qing"); ficha `yang2022computeraided` (COMPLETO; "ten patients with an intact pelvis", 2.1, p. 2) | Patron PAT-19 reincide (y PAT-122): la marca declara pendiente una decision ya registrada, y la clave ya esta en el `.bib`. Lo que sigue la marca sale de la ficha y es citable | "Yang et al.~\cite{yang2022computeraided} ..." sin `\GAPDEC`. Retirar la fila 148 de MAPA (ver T07) |
| T02 | media | OC-2, OC-3, G-T4 | l. 114, oracion 3 (`\GAPDEC` #179); arrastre en l. 94 oracion 6, l. 108 oracion 2 y l. 110 oracion 1 | "El esquema multiventana proviene de la MAR \GAPDEC{si la síntesis aprendida ... (implicancia 179) ...}" | DEC15-3 pto 9 (nombrar U-DuDoNet y PND-Net; acotar la brecha a "sintesis del implante y de su artefacto local, condicionada por la geometria y la pose de un implante colocado por un muestreador quirurgicamente restringido, y evaluada como producto frente a un protocolo fisico"); IMP #179 (DECIDIDA, l. 12137); fichas `lyu2021ududonet` ("create a plausible artifact-affected CT I^ca by adding the artifact term", Sec. 2, p. 298; "I^ca = I^c + a_S + a_I", Sec. 3, p. 298) y `xia2024pndnet` ("we add an artifact synthesis path to achieve unpaired learning", Sec. III-D, p. 2129; "I_cm cannot be synthesized by directly adding a_I to arbitrary clean CT image", Sec. III-A, p. 2128); BIB l. 743, 1420; `_index.md` l. 200-201 (COMPLETO) | Patron PAT-19 reincide: la marca pregunta lo que DEC15-3 pto 9 ya decidio. Al cerrarla, PAT-168 obliga a revisar la prosa que repite el mismo hueco: "Ninguno de los tres enfoques revisados" (l. 108) deja fuera una cuarta familia que sintetiza artefacto aprendido; "tres elementos que las fuentes revisadas no reúnen" (l. 110) y "Ningún trabajo revisado sintetiza ... solo en el dominio de imagen y evalúa su coherencia física" (l. 94) siguen siendo ciertos solo por su conjuncion (ninguna de las dos fichas evalua la sintesis como producto, #179) | l. 114, en lugar de la marca: "La síntesis aprendida de componentes de artefacto metálico también está publicada, como paso intermedio de la MAR no pareada: Lyu et al.~\cite{lyu2021ududonet} suman a TC limpias componentes de artefacto aprendidos en sinograma e imagen, y Xia et al.~\cite{xia2024pndnet} añaden una ruta de síntesis aprendida; en ninguno la síntesis se evalúa como producto." En l. 108 nombrar la brecha con la formula de pto 9. Sin cifras (PSNR) de esas fichas: no hacen falta |
| T03 | alta | OC-3, G-T4 | l. 98, oracion 7 | "En componentes metálicos del tamaño de un tornillo, el artefacto real ... queda dentro de esa banda" | DEC1013 pto 1 y 3 ("en tornillos la banda de 12 mm alcanza"); IMP #193 (ABIERTA, l. 12438: "`B_delta` de 12 mm trunca rayas que en lo real cruzan el corte", como evidencia); C3 l. 260-262 (exceso mediano por anillo; 18 pacientes de entrenamiento y validacion; componentes de 500 a 4000 mm3; referencia = otro corte "en el que la anatomía cambia") | La oracion tiene respaldo en una decision, pero #193, posterior y ABIERTA, cita expresamente el ancho de la banda como evidencia de realismo insuficiente: el texto da por resuelto un tema abierto (regla 3). Ademas, patron PAT-31 reincide: pierde la condicion de la medicion (mediana por anillo, 18 pacientes de entrenamiento y validacion, referencia en otro corte) y la vuelve "el artefacto real" sin mas | Envolver en `\REVVISUAL` y conservar la condicion: "\REVVISUAL{En componentes de 500 a 4000~mm$^3$, el exceso mediano del artefacto real, medido por anillos alrededor del metal en pacientes de entrenamiento y validación, queda dentro de esa banda (Sección~\ref{sec:v2}).}" Nada de #193 como hecho: no escribir que la banda trunque o no las rayas |
| T04 | media | OC-2, PAT-123 | l. 94, oraciones 7-8; l. 104, oracion 8 (con su `\GAPDATO`); l. 106, oracion 3; l. 114, oracion 4 ("la banda $B_{\delta}$ para los efectos de adquisición"); l. 116, oraciones 1-2; ANX:29 ("Supuesto: el artefacto puede generarse en el dominio de imagen"; "contraste de realismo pendiente") | "Se asume que la apariencia del artefacto puede generarse en el dominio de imagen" | `overleaf/CLAUDE.md` regla 2 (`\REVVISUAL`, pedido de la autora 2026-10-15); ENCARGO E1 (incluye "limitaciones de realismo, la fila 'Este trabajo' de la tabla"); IMP #193 ("Lectura del asistente: las rayas reales son un fenomeno de proyeccion ...; un modelo 2.5D que regenera una banda local no tiene esa informacion"; "Toca: alcance y reclamo del Objetivo 3"); `overleaf/main.tex`:62-64 | Patron PAT-123 reincide: #193 ABIERTA no deja marca en el capitulo. La seccion no tiene ningun `\REVVISUAL`. Los pasajes listados tratan del realismo (contraste de realismo, comparacion con observaciones reales) o dependen de el (el supuesto del dominio de imagen es exactamente lo que #193 pone en duda; "para los efectos de adquisicion" reclama lo que la banda captaria). Ninguno afirma #193 como hecho, pero ninguno queda señalado para la revision con el asesor | Envolver en `\REVVISUAL{...}` cada pasaje listado, con el `\GAPDATO` de l. 104 dentro (ENCARGO E1). En ANX:29, envolver el supuesto y "contraste de realismo pendiente". No reescribir su contenido (#193 sin decidir) |
| T05 | media | G-T4, OC-3 | l. 94, oracion 8; l. 104, oracion 6; l. 108, oracion 6; ANX:29 | "ya ejecutada y no concluyente"; "su resultado, no concluyente"; "en prueba quedó sin concluir" | DEC15 pto 15 ("se reporta la direccion siempre que el IC90 excluya 0"; "Para v1: `run04_mejor` = no concluyente con diferencia significativa a la baja"); DEC15-3 pto 1 ("La hipotesis de equivalencia ... no se sostiene"; "muestran amplitud menor que el protocolo fisico"; "Se declara que esta lectura se fija despues de ver el resultado"); RP1 l. 36 ("difusor < Peters (IC90 excluye 0)"); C3 l. 256 ("con la diferencia a la baja"; "la lectura de sus desenlaces se fijó después de ver el resultado") | Patron PAT-136 reincide: el desenlace se da sin su direccion, que la regla de reporte exige, y sin la lectura que DEC15-3 pto 1 fija para el Objetivo 3. "Quedó sin concluir" deja abierto lo que pto 1 cierra (la hipotesis de equivalencia no se sostiene). C3 ya lo dice; el cap. 2 queda atras (PAT-180) | Sin cifras: "no concluyente, con la amplitud del sintetizador por debajo de la del protocolo físico, en una lectura fijada después de ver el resultado (capítulo de resultados)". En l. 108: "... es una pregunta del Objetivo~3 y no una premisa, y los datos de prueba no permiten afirmarla". Igual en ANX:29 |
| T06 | baja | E-R6 | l. 56, oraciones 1 y 4 | "Otros planificadores automáticos registran sobre la TC del paciente un atlas ..."; Yang "eligen ... un único canal óptimo" | ficha `yang2022computeraided` l. 32-35, 75-77 ("Yang no usa atlas, hace busqueda exhaustiva por paciente"; canal "en arco de curvatura constante"); "we designed the IAFC as a constant-curvature channel" (2.2, p. 2) | La oracion tematica atribuye el registro de un atlas a "otros planificadores", y Yang entra en el mismo parrafo sin decir que no lo usa; el lector puede atribuirselo. Afin a PAT-77 (ERRADICADO). Falta tambien que su canal es en arco, rasgo que lo separa de las trayectorias rectas de Goerres y Han | "Yang et al.~\cite{yang2022computeraided} no usan atlas: buscan, en cada una de 10 pelvis intactas, un único canal en arco que va de un ilion al otro a través de S1, puntuado por su distancia a la superficie ósea." |
| T07 | baja | OC-2, OC-9 | fuentes, no el texto: MAPA l. 148-149; MAPA l. 20 (nota) | Filas del `\GAPDEC` de Yang (#192 (a), "ABIERTA") y de #179 ("ABIERTA") | IMP #179, #192 (DECIDIDAS), #180 (CERRADA); DEC15-3 ptos 8-9 | Las dos filas de la tabla de GAP describen como abiertas implicancias ya decididas; al aplicar T01-T02 deben pasar a CERRADO con su origen | Marcar ambas "CERRADO en capitulo2-r08 (DEC 2026-10-15 (3) ptos 8 y 9)" y anotar en MAPA las marcas `\REVVISUAL` nuevas del capitulo (T04) |

TOTAL alta=1 media=4 baja=2

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 8-10 | Estructura del capitulo y relacion seccion-objetivo | Organizacion propia; objetivos de `introduccion.tex` | si |
| l. 12 | Revision narrativa y dirigida; lista de la autora; busquedas con fecha | DEC 2026-10-08 pto 29; MAPA | si |
| l. 12 | "De una de las fuentes ... solo se dispuso del resumen" | `_index.md` (`zhang2026pediclescrew` ABSTRACT); `goerres2017planning`, `han2019atlasplanning` (l. 205-206) y `yang2022computeraided` (l. 841) COMPLETO; `day2000transsacral` (solo abstract) no se cita | si |
| l. 16 | Dos familias; claves de cada una | fichas `chen2024tumorsynthesis`, `ramzan2026claim`, `jacob2026lgesynthnet`, `zhang2025lefusion`, `zhang2025diffboost`, `konz2024anatomicallycontrollable` | si |
| l. 16 | Rayas que irradian desde el metal | `deman1999`, "a number of streaks can be seen radiating from the metals" (Sec. III-D, p. 694) | si |
| l. 18 | DiffTumor; region sana = complemento; no modela textura fuera; [-175, 250] HU | `chen2024tumorsynthesis` §3.2 p. 4; Apendice E.2 p. 21 | si |
| l. 18 | Dice higado 62.5 -> 66.5 %, una de tres redes, cinco particiones | id., Tabla 4, p. 17 | si |
| l. 18 | Cuatro radiologos; cerca de la mitad tomada por real | id., §4.1, pp. 5-6 | si |
| l. 20 | Difusion en imagen; perdida en la mascara; fondo recompuesto con ruido; adaptado de LeFusion | `ramzan2026claim` filas 1, 3, 4, 10, 11 | si |
| l. 20 | LeFusion: nodulos en TC, perdida en la lesion, fondo real con ruido | `zhang2025lefusion` "Que hace" | si |
| l. 20 | Dice 58.89 -> 63.53 (sin unidad); sin fidelidad; fondo cualitativo | `ramzan2026claim` filas 50, 52, 58, 59; BITACORA §2 | si |
| l. 22 | LGESynthNet; ControlNet; mapa de bordes; imagen enmascarada; mejora de Dice sin cifra | `jacob2026lgesynthnet` Abstract, Sec. 3.1; DEC 2026-10-08 pto 32 | si |
| l. 22 | Sin paso de restitucion; SSIM de imagen completa; cicatriz < 1 % ("suele"); atribucion a la compresion | id., "typically occupy <1% of the image" (Sec. 1, p. 2); Sec. 4.4 y 5, p. 8 | si |
| l. 22 | Lectura propia del autoencoder | marcada "Este trabajo lee" | si |
| l. 24 | DiffBoost: ControlNet sobre Stable Diffusion; desde ruido; texto y borde; parches al azar | `zhang2025diffboost` Alg. 1, p. 3676 | si |
| l. 24 | Dice 78.46 -> 84.56 %, 94.42 -> 94.78 %, 62.92 -> 71.65 % | id., §IV-B; Tabla II, p. 3678 | si |
| l. 24 | Konz: mascara concatenada; [0, 255]; Dice 0.8980; 40 pacientes | `konz2024anatomicallycontrollable` | si |
| l. 26 | Hu 1.3 r; Jin parche 3D GAN con borde; Wu conserva valores fuera | `hu2023` Tabla 1 p. 7426; `jin2021freetumor` Sec. 3.4.1; `wu2025freetumor` Sec. 4.2 | si |
| l. 28 | RePaint: sin reentrenar; region conocida; remuestreo; 256 x 256 | `lugmayr2022repaint` | si |
| l. 28 | El sintetizador no remuestrea ni recompone; perdida solo en la region generada | DEC 2026-10-08 pto 5 | si |
| l. 30 | Cinco por segmentacion; dos con similitud; uno con prueba visual | fichas de las cinco claves | si |
| l. 34 | Zhang y Yu: 15 formas, 120 kVp, Poisson; dispersion y volumen parcial no mencionados | `zhang2018` (NO ENCONTRADO para dispersion) | si |
| l. 34 | Lin 100 formas, volumen parcial; Wang 2019 mascara tubular, 1090 volumenes, Beer-Lambert, cinco energias; Karageorgos objetos desde TC de metal, CatSim de XCIST | `lin2019` p. 10508; `wang2019cochlear`; `karageorgos2024ddpm` Sec. II-A; `wu2022xcist` p. 6 | si |
| l. 36 | 31 % de equipos con difusion | `haneda2025aapm` Sec. 3.1, p. 11 | si |
| l. 36 | DDPM en sinograma sin metal; metal reinsertado por umbral; SSIM 0.964; 13 de 28 | `karageorgos2024ddpm` Tabla I p. 28; Sec. III-C p. 12 | si |
| l. 38 | Yun: correccion en proyeccion + difusion latente; CLINIC-metal por inferencia; mascara por umbral; 0.82 HU frente a 3.18-6.30 HU | `yun2026simulationdriven` Tabla 4, p. 11; BITACORA §2; `docs/02-datos.md` | si |
| l. 40 | Peters: fantoma; 14 000 casos; fractales; ocho metricas; 29 escenarios; base del AAPM; < 2 %; < 10 %; 13.3 % | `peters2025hybrid` 3.1, p. 6; `haneda2025aapm` | si |
| l. 42 | Validacion no cubre el paso hibrido ni la geometria; todo 2D | `peters2025hybrid` 2.3 p. 3; Abstract | si |
| l. 44 | Peters al azar, hasta cinco; "meaningful locations"; Karageorgos 50 % y 200 HU; Wang 2019 "cerca del centro"; Wang 2025 a mano | `peters2025hybrid` 2.3 p. 4; `karageorgos2024ddpm` Sec. II-A p. 4; `wang2019cochlear` "near the center"; `wang2025adaptiveweighting` Sec. V-A-2 | si |
| l. 46 | XCIST como fundamento, no reimplementado; primer orden; Ti 20 mm y Fe 10 mm; > 3.0 cm; 274 de 14 000 | CLAUDE.md raiz; `wu2022xcist` p. 9, Fig. 11; `haneda2025aapm` Sec. 4, p. 16 | si |
| l. 48 | Ren: sondas; Ti 12.7 mm; dos crioablaciones; datos del fabricante; implantes ortopedicos | `ren2022metalinsertion` | si |
| l. 52 | Organizacion de la seccion | propia | si |
| l. 54 | Liu: 14 casos; 2.56 mm y 3.31 grados; 12 casos; 86.7 %; tres cirujanos; 10.58 ± 3.84 frente a 4.36 ± 3.83 mm; sin iliosacros; no aplica a sacro | `liu2025pipeline` IV-A p. 16; IV-B pp. 16-17; Tabla III p. 38; p. 14, 18 | si |
| l. 56 | Goerres: atlas de 12 pelvis femeninas; rama pubica superior e ilion; sacroiliacos como trabajo futuro | `goerres2017planning`, "(n = 12) female pelves" (3.1.1, p. 7); "such as sacroiliac screws" (5, p. 15-16); "Restriccion" l. 18 | si |
| l. 56 | Han: 40 pelvis; transiliaco-transsacros de S1 y S2; recta ajustada al mapa de acumulacion | `han2019atlasplanning`, "n = 40 pelves" (2.1.1, p. 4); "trans-iliac trans-sacral iliosacral screws in S1 and S2 levels" (4, p. 17); "fitting a straight, rigid cylinder to the accumulation map" (2.3.1, p. 10) | si |
| l. 56 | Yang: 10 pelvis; canal unico optimo ilion-S1-ilion | `yang2022computeraided`, "ten patients with an intact pelvis" (2.1, p. 2); "obtain the optimal safest IAFC" (Step 8, p. 2); "IAFC through the sacrum S1" (5, p. 10) | si (cifra); no (T01 marca, T06 atlas) |
| l. 56 | Los tres: una trayectoria por corredor, sin malposicion graduada | fichas Goerres (malposicion no modelada), Han l. 36, Yang "Muestreo de poses o de malposicion: NO ENCONTRADO"; IMP #180, #192 ("el gap del muestreador se mantiene") | si |
| l. 58 | Zhang 2026 solo resumen: TC sintetica desde haz conico; pediculares; mitiga | `zhang2026pediclescrew` | si |
| l. 60 | Ramzan 17 segmentos, volumenes uniformes, comparacion visual; Chen elipsoides con radiologos; Jacob elipsoide al azar | `ramzan2026claim` filas 19, 21, 62; `chen2024tumorsynthesis` §3.3; `jacob2026lgesynthnet` Sec. 3.1 | si |
| l. 62 | Zwingmann 2009: cuatro niveles; 69 % y 40 %; p = 0.02 | `zwingmann2009navigated` | si |
| l. 64 | 2.6 % (1832) y 0.1 % (262); cero malposiciones de 2009; malposicion = revision | `zwingmann2013` | si |
| l. 66 | Zwingmann 2010: 63 y 131; 81/11/3/5 y 42/22/21/13 + 2 % grado 4; solapamiento posible | `zwingmann2010percutaneous`; DEC 2026-10-08 pto 31 | si |
| l. 68 | Herman: binaria, por nivel; 36.5 % y 14.8 %; p = 0.035; ninguno fuera del hueso | `herman2016` | si |
| l. 68 | Poses bajo S1 al preinscribir; grado 3 fuera del hueso; S1 asumido | C3 `sec:poses`, `sec:sap`, `sec:amenazas`; `experiments/objetivo2/EXPERIMENTOS.md`:101 (R2 en pausa) | si |
| l. 70 | Kaiser 104 TC; McLaren 433 y 352; Ramadanov y Zabler cualitativa | `kaiser2014dysmorphism`; `mclaren2021corridor`; `ramadanov2025safezone` | si |
| l. 72 | Gardner 50 TC; 222 frente a 346 mm2 (media); estudio previo; Ziran 17 pelvis, 7-25 %, 97-140 % | `gardner2010safezones` p. 624; `ziran2007fluoroscopic` | si |
| l. 74 | Cuatro carencias; "una trayectoria por corredor" | cuerpo de l. 54-60 | si |
| l. 76 | Un radiologo; escala de Smith; pediculares; cuatro cadaveres; Herman binaria; Liu margen; SAP solo perforacion | `zwingmann2009navigated`; `smith2006iliosacral`; DEC 2026-10-08 pto 15 | si |
| l. 78 | Arand: 50 TC post mortem; ala menor que cuerpo de S1; sin HU; densidad fuera de SAP | `arand2019pelvicring`; DEC 2026-10-08 pto 14 | si |
| l. 78 | Tres de ocho metricas; inversion de streak amplitude | DEC 2026-10-05 (3)-(4); DEC 2026-10-08 pto 10 | si |
| l. 82 | Saturaciones <= 600 HU; umbral 2500 HU | `chen2024tumorsynthesis`, `hu2023`, `jin2021freetumor`, `wu2025freetumor`; `wang2025adaptiveweighting`, `li2024` | si |
| l. 84 | Tres ventanas; cascada; 26.76 dB / 0.9501 frente a 32.67 dB / 0.9803; 14 volumenes; cinco medicos; 30 imagenes | `wang2025adaptiveweighting` Sec. V-B, V-A-2, V-C-3 | si |
| l. 84 | `\GAPLIT` fuente primaria del esquema multiventana | Sin PDF ni ficha (glob `**/niu2021*`: solo `refs/raw/niu2021multiple.bib`); `li2024` l. 58 nombra a Niu, Li y Wang | si (marca justificada) |
| l. 86 | Li: ventanas en perdida y evaluacion; [-1000, 2000] HU; +0.64 dB | `li2024` l. 51, 58 (delta enunciado por el texto) | si |
| l. 88 | Ida y vuelta medida en el Obj 1; `pub+asinh` en 32 bits | `experiments/objetivo1/p1_compuerta.md`; DEC 2026-10-08 pto 1 | si |
| l. 90 | Rombach; Chen 2026 prepublicacion, [-1000, 1000] HU; Guo sin rango | `rombach2022latentdiffusion`; `chen2026foundationvae`; `guo2025maisi` | si |
| l. 92 | RMSE 12.3, 20.2 y 12.74 | `karageorgos2024ddpm` Tabla I; `peters2025hybrid` 2.5; `yun2026simulationdriven` Tabla 1 | si |
| l. 94 | De Man en sinograma; Lin 31.45 frente a 33.51 dB; problema mal planteado | `deman1999`; `lin2019` | si |
| l. 94 | `\GAPDATO` cifras de Li | `li2024` l. 51 ("Advertencia de transcripcion") | si (marca justificada) |
| l. 94 | "Ningún trabajo revisado sintetiza ... y evalúa su coherencia física" | IMP #179 (las fichas no evaluan la sintesis como producto) | si (por la conjuncion; revisar con T02) |
| l. 94 | Supuesto del dominio de imagen; comparacion "ya ejecutada y no concluyente" | RP1 l. 14, 36; DEC15 pto 15; DEC15-3 pto 1; IMP #193 | no (T04, T05) |
| l. 96 | De Man, Park, Glover y Pelc, Selles (25 pacientes), Li | fichas citadas | si |
| l. 98 | Radzi 2.0/2.6/1.6/2.0 mm, 3.5-4.0 mm, un tobillo; Cassanego 3.1-4.2 mm, 3.0-3.5 mm, seis miembros | `radzi2014metalartifacts`; `cassanego2026evolution` | si |
| l. 98 | Banda de unos 12 mm como convencion | CLAUDE.md raiz; DEC1013 | si |
| l. 98 | "el artefacto real medido en la cohorte queda dentro de esa banda" | DEC1013 pto 1, 3; C3 l. 260-262; IMP #193 | no (T03) |
| l. 100 | Karageorgos: pelvis con dos marcadores de oro; 7.57; 11.45 (1.4x); 54.82 (0.7x) | `karageorgos2024ddpm` | si |
| l. 104 | Nueve trabajos en la tabla; muestreador y SAP ejecutados; v2 posterior y exploratoria | ANX:19-27; C3; DEC15-3 pto 5 | si |
| l. 104 | Version 1 comparada en prueba con el protocolo fisico, "no concluyente" | RP1 l. 14, 36; DEC15 pto 15 | parcial (T05) |
| l. 104 | `\GAPDATO` contraste de realismo "que no tiene script" | EXP3 l. 110 ("(sin script) ... realismo (H5) ... POR ESCRIBIR"); RP1 l. 63 | si (marca justificada; falta `\REVVISUAL`, T04) |
| l. 106 | Columnas de la tabla; Peters validada en fantoma y 2D; comparacion con observaciones reales = contraste de realismo | `peters2025hybrid` Abstract; C3 l. 433 | si (falta `\REVVISUAL`, T04) |
| l. 108 | Tres enfoques; ninguno produce a la vez poses y artefacto | cuerpo del capitulo; DEC15-3 pto 9 | parcial (T02) |
| l. 108 | Primario: streak amplitude frente a Peters con titanio; 13 pacientes de prueba sin metal; eje sin perturbar; poses del muestreador fuera; copia y pegado = control de cordura | DEC 2026-10-05 (3) pto 5; DEC15 ptos 9, 12; RP1 l. 14, 23-25 | si |
| l. 108 | Protocolo exige proyecciones por pose, 2D, una fila; sintetizador sobre TC reconstruidas | DEC 2026-10-08 pto 25 | si |
| l. 108 | "en prueba quedó sin concluir" | DEC15-3 pto 1 | parcial (T05) |
| l. 110 | Tres elementos; distribucion preinscrita; sin ajuste a la referencia; ningun objetivo los aisla | `experiments/objetivo2/preinscripcion_muestreador.md`; DEC 2026-10-08 pto 30; `introduccion.tex` | si |
| l. 112 | Wang 2019 mascara tubular "cerca del centro"; Zhang y Yu, Karageorgos, Peters; Yun, Wang, Li por umbral | fichas citadas | si |
| l. 112 | Xie: sensibilidad 100 %, Dice 82.92 %, 2500 HU, simulados; entrenamiento con mascaras umbralizadas | `xie2024implantsegmentation`; DEC 2026-10-08 ptos 6-7; IMP #128.4 | si |
| l. 114 | Piezas publicadas: metal virtual, difusion frente al artefacto, Konz, Ramzan, LeFusion, Hu, Jin | fichas citadas | si |
| l. 114 | `\GAPDEC` #179 | DEC15-3 pto 9; IMP #179 DECIDIDA | no (T02) |
| l. 114 | Combinacion de cuatro rasgos; "la banda $B_{\delta}$ para los efectos de adquisición" | DEC 2026-10-08 pto 30; IMP #193 | si (falta `\REVVISUAL` en el inciso de la banda, T04) |
| l. 116 | Supuesto y convencion; evaluacion por coherencia fisica y quirurgica, no por segmentacion | DEC 2026-10-08; `docs/00-tesis.md` Fuera de alcance pto 1 | si (falta `\REVVISUAL` en el supuesto, T04) |
| ANX:29 | SAP ejecutado; v1 frente a Peters Ti, primario, 13 pacientes, eje sin perturbar: no concluyente; cordura; realismo pendiente | RP1; DEC15 ptos 9, 12, 15 | parcial (T04, T05) |
| todo | Claves `\cite`: todas en BIB (incluidas `goerres2017planning`, `han2019atlasplanning`); `yang2022computeraided` en BIB l. 1453 y aun no citada; primer apellido = `.bib`; ninguna cita sujeto gramatical sola; entradas de dos autores sin "et al." | BIB | si |
| todo | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet como metodo vigente, "31-60 %", BFC, ISC) | grep en la seccion: ausente como vigente; ControlNet y difusion latente solo en trabajos ajenos y en la pregunta del Obj 1 | si |
| todo | Afirmacion de #193 como hecho | Ningun pasaje dice que el realismo sea suficiente o insuficiente; l. 98 afirma un tema que #193 cita como evidencia (T03) | parcial (T03) |
| todo | Patrones VIGENTES del dominio | Reinciden: PAT-19 y PAT-122 (T01, T02), PAT-31 (T03), PAT-123 (T04), PAT-136 (T05), PAT-168 (riesgo en T02), PAT-180 (T05). Sin reincidencia: PAT-11, PAT-13, PAT-27, PAT-116, PAT-138/158 (EXP3 l. 110 al dia), PAT-148, PAT-155, PAT-162 (13 = n analizado), PAT-163, PAT-166, PAT-167, PAT-169, PAT-172, PAT-175, PAT-176, PAT-182, PAT-183 (ANX:29 ya alineada salvo T04-T05) | — |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAPDEC que sigue preguntando una decision ya registrada en `01-decisiones.md` | OC-2, G-T4 | "\GAPDEC{clave bibliográfica de Yang et al. 2022 pendiente de la autora}" | PAT-19 (y PAT-122) |
| Hecho apoyado en una DEC anterior que una implicancia ABIERTA posterior cita como evidencia en contra, redactado sin condicion ni marca | OC-3, G-T4 | "el artefacto real medido en la cohorte queda dentro de esa banda" | nuevo |
| Implicancia ABIERTA con marca propia pedida por la autora (`\REVVISUAL`) que no deja marca en los pasajes que dependen de ella | OC-2 | "Se asume que la apariencia del artefacto puede generarse en el dominio de imagen" | PAT-123 |
| Desenlace de la prueba de equivalencia sin la direccion ni la lectura fijadas por DEC | G-T4, OC-3 | "su resultado, no concluyente, se presenta en el capítulo de resultados" | PAT-136 |
