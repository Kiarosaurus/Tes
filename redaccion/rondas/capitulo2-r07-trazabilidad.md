# Auditoria de trazabilidad — capitulo2 — r07

Alcance: `overleaf/secciones/capitulo2.tex` completo (l. 1-114) y la Tabla `tab:comparacion`
(`overleaf/secciones/anexos.tex`:10-32), que l. 102 presenta como parte del capitulo. Lint r07: PASA, GAP lit = 1,
dato = 2, dec = 0 (coincide con MAPA l. 27, "tras gaps-r03").

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC = `docs/01-decisiones.md`;
DEC15 = DEC 2026-10-15 (l. 2559-2634); DEC1005 = DEC 2026-10-05 (3), tabla de jerarquia (l. 1754-1764);
IMP = `docs/04-implicancias.md`; RP1 = `experiments/objetivo3/resultados_prueba_v1.md`;
EXP3 = `experiments/objetivo3/EXPERIMENTOS.md`; ANX = `overleaf/secciones/anexos.tex`.

Respuesta r06 leida. Lo RECHAZADO (ES-15, unidades de Chen 2026) no se re-reporta. El escalado de Jacob et al. quedo
resuelto por DEC 2026-10-08 pto 32: l. 22 y ANX:21 ya no dan cifras (la nota de MAPA l. 123 que dice que ANX:21 aun
da 0.587 esta desfasada, T10). El escalado de la unidad de los RMSE queda cubierto por BITACORA §2 ("cifra cuya ficha
no trae unidad va sin unidad"); no se reporta.

Lo nuevo frente a r06: DEC15 (pto 9 pose del E-A2, pto 13 cierre de #90, pto 15 desenlaces), RP1 (resultado de prueba
de v1), fichas `han2019atlasplanning`, `goerres2017planning`, `yang2022computeraided` (#180, #192, ABIERTAS),
`lyu2021ududonet`, `xia2024pndnet` (#179, ABIERTA) y el raw `refs/raw/niu2021multiple.bib`.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | OC-2, G-T4 | l. 102, `\GAPDATO` final | "no existe aún resultado del Objetivo~3 porque el modelo final no está elegido" | DEC 2026-10-11 (3) pto 1 (`run04_mejor`); DEC 2026-10-14 (2) pto 1; RP1 l. 10-14, 23; DEC15 pto 15 ("Para v1: `run04_mejor` = no concluyente con diferencia significativa a la baja"); EXP3 l. 85, 93 (`a24` CORRIDO, RP1 HECHO); MAPA l. 50, 132 | Patron PAT-122 reincide (y PAT-19). La marca niega dos hechos registrados: el modelo evaluado esta elegido y la prueba de v1 esta evaluada (n = 13, -301.0 HU, IC90 [-477.0, -124.9], Delta 196.3). Lo que falta de verdad es el contraste de realismo (RP1 l. 61-64, "no hay script"). `introduccion` ya se alineo en r07; el cap. 2 quedo fuera (MAPA l. 20) | "La fila propia describe un diseño ya ejecutado: el muestreador y SAP se ejecutaron, y el sintetizador se evaluó en la partición de prueba frente al protocolo físico, con resultado no concluyente (Capítulo~\ref{cap:resultados})." + `\GAPDATO{evaluación del contraste de realismo sobre la partición de prueba, que no tiene script}` (misma marca que MAPA l. 132). Sin cifras en el cap. 2: van al cap. 4 |
| T02 | alta | G-T4, OC-3 | l. 106, oraciones 3-4 | "prevé comparar ... con la inserción por copia y pegado. Prevé, además, ... según el plazo, como segunda comparación" | DEC1005 pto 5 (Primario = TOST contra el brazo fisico; copia y pegado = "Cordura ... piso, no evidencia de calidad"); DEC15 pto 9 ("E-A2 usa el eje del corredor"; poses del muestreador solo en un exploratorio "solo sintetizador"); DEC15 pto 13 (#90 CERRADA por ejecucion); IMP #90 l. 6464; RP1 l. 14, 23; C3 `sec:ap-brazos` | Patrones PAT-175 y PAT-11 reinciden. Cuatro errores: (a) invierte la jerarquia: la copia y pegado aparece como la comparacion del diseno y el protocolo fisico como "segunda", cuando este es el contraste primario y aquella un control de cordura degenerado (DEC15 pto 12); (b) el protocolo no corre sobre las poses del muestreador sino sobre el eje sin perturbar; (c) "según el plazo" invoca la contingencia retirada; (d) "prevé" para algo ya ejecutado. IMP #183 ("Ademas") ya lo registraba | "El sintetizador se comparó por \emph{streak amplitude} con el protocolo físico de Peters et al., como contraste primario, sobre el eje del corredor sin perturbar de los pacientes de prueba sin metal, para aislar la apariencia de la colocación; la inserción por copia y pegado es solo un control de cordura (Sección~\ref{sec:ap-brazos})." Las poses del muestreador, si se nombran, solo en el exploratorio de DEC15 pto 9 (remision a C3, ya con su `\GAPDATO`, MAPA l. 140) |
| T03 | alta | G-T4, OC-2, OC-3 | ANX:29, fila "Este trabajo", ultima columna (Tabla presentada en l. 102) | "sin resultado del sintetizador, que se comparará ... con ... copia y pegado y, según el plazo, ..." | Las mismas de T01 y T02 | Patrones PAT-122, PAT-175 y PAT-11 reinciden en la tabla del capitulo. Repite los dos errores de l. 102 y l. 106 (sin resultado; jerarquia invertida; plazo). La tabla esta en otro archivo, pero es la Tabla del capitulo y BITACORA §2 (2026-09-30) exige que toda celda tenga respaldo en el cuerpo: al corregir T01-T02 la celda debe cambiar con ellos | "SAP frente a la referencia clínica, ya ejecutado; sintetizador frente al protocolo físico (contraste primario) en la partición de prueba: no concluyente; copia y pegado como control de cordura; realismo pendiente" |
| T04 | media | OC-2, G-T4 | l. 52, 54 y 72, oracion 2 | "la planificación automática, que busca una trayectoria"; "La planificación revisada entrega una trayectoria por tornillo, el artículo no menciona tornillos iliosacros" | IMP #180 (ABIERTA: "el trabajo relacionado del muestreador debe nombrarlos"); IMP #192 (ABIERTA); ficha `han2019atlasplanning` ("only considered trans-iliac trans-sacral iliosacral screws in S1 and S2 levels", sec. 4, p. 17; "n = 40 pelves", sec. 2.1.1, p. 4; "3.9 mm for iliosacral S1, and 4.1 mm", sec. 3.2, p. 12; malposicion graduada NO ENCONTRADO); ficha `goerres2017planning` ("investigation of additional trajectories, such as sacroiliac screws", 5, p. 15-16; "(n = 12) female pelves", 3.1.1, p. 7); claves `han2019atlasplanning` y `goerres2017planning` en `referencias.bib` (l. 450, 386) | La planificacion automatica revisada se reduce a Liu et al., aunque el repositorio tiene dos planificadores leidos y en el `.bib`, uno de ellos sobre el mismo corredor transiliaco-transsacro S1/S2. La carencia de l. 72 sigue siendo cierta para Liu y la brecha de colocacion se sostiene (#180, #192: "el gap del muestreador se mantiene"), pero "la planificación revisada" ya no describe lo revisado. Afin a PAT-148 (exclusividad de un recuento viejo) | Añadir tras Liu: "Goerres et al.~\cite{goerres2017planning} y Han et al.~\cite{han2019atlasplanning} planifican trayectorias pélvicas registrando un atlas de 12 y de 40 pelvis; Han et al. incluyen los corredores transilíaco-transsacros de S1 y S2. Los dos entregan una trayectoria por corredor y ninguno modela una malposición graduada." Ajustar l. 72 a "La planificación revisada entrega una trayectoria por corredor ...". Yang et al. queda fuera hasta que la autora fije la clave (#192 (a)): `yang2022computeraided` no esta en el `.bib` y la ficha de `yang2022arcplanning` es del congreso |
| T05 | media | OC-2, OC-3 | l. 92, oracion 6; l. 112, oraciones 1-3 | "Ningún trabajo revisado sintetiza el artefacto metálico solo en el dominio de imagen" | IMP #179 (ABIERTA: "la brecha del cap. 2 debe acotarse"; "Pendiente de la autora: decidir la reformulacion"); fichas `lyu2021ududonet`, `xia2024pndnet` (claves en `.bib` l. 743, 1420) | La oracion se sostiene por su segunda mitad ("y evalúa su coherencia física": en U-DuDoNet y PND-Net la sintesis no se evalua como producto, #179). Pero la lista de "piezas publicadas" de l. 112 omite la sintesis aprendida de artefactos como paso intermedio de MAR no pareado, que #179 pide incorporar, y la implicancia abierta no deja marca. Afin a PAT-123 (ERRADICADO) | En l. 112, tras las piezas publicadas: `\GAPDEC{si la síntesis aprendida de componentes de artefacto metálico en MAR no pareada (implicancia 179) se nombra entre las piezas publicadas y acota la brecha}`. No redactar la reformulacion hasta que la autora decida |
| T06 | media | OC-3, G-T4 | l. 94, oracion 6; l. 96, oracion 5 | "La banda $B_{\delta}$ trunca por diseño los efectos que estas fuentes describen lejos del metal" | DEC 2026-10-13, l. 2505 ("Diagnostico D1/D2: en tornillos la banda de 12 mm alcanza") y l. 2514; IMP #177 adenda D1/D2 ("11 HU (IC90 incluye 0) a 10-12 mm") | Patron PAT-27 reincide. La convencion y su limitacion son ciertas frente a la literatura, pero callan una medicion propia que una decision de la autora registra y que la acota para piezas del tamaño de un tornillo. Mismo hallazgo que introduccion-r07 T08 | En l. 96, tras la convencion: "En piezas del tamaño de un tornillo, el artefacto real medido en la cohorte no sobrepasa esa banda (Sección~\ref{sec:v2})." Sin cifras de #177 en el cap. 2 |
| T07 | baja | G-T4 | l. 92, oracion 7; l. 106, oracion 6 | "la comparación prevista con el protocolo físico podría contradecir ese supuesto"; "Si el sintetizador alcanza la equivalencia ... es lo que pone a prueba" | RP1 l. 14; DEC15 pto 15; IMP #177 (lectura ABIERTA) | Patron PAT-116 reincide: condicional y "prevista" sobre una comparacion ya ejecutada y clasificada. No debe pasar a "lo contradijo": el porque sigue abierto (#177) | l. 92: "la comparación con el protocolo físico, ya ejecutada, es la que puede contradecir ese supuesto (Sección~\ref{sec:amenazas})". l. 106: "El Objetivo~3 planteó esa equivalencia como pregunta y no como premisa." |
| T08 | baja | E-R6 | l. 44, oracion 5; l. 110, oracion 2 | "sitúan el implante coclear en el centro de una estructura segmentada" | ficha `wang2019cochlear`, "create a 3D tubular binary mask near the center" (Sec. 2.1, p. 3) | La ficha dice "cerca del centro"; el texto lo vuelve exacto en dos lugares | "cerca del centro de una estructura segmentada" (l. 44 y l. 110) |
| T09 | baja | G-T4 | l. 70, oracion 3 | "Su área transversal mínima es de 222~mm² ... frente a 346" | ficha `gardner2010safezones`, "222 mm2 [SD, 67] versus 346 mm2 [SD, 71]" (p. 624) | Son medias de grupo; falta decirlo. Mismo hallazgo que introduccion-r07 T15 | "Su área transversal mínima media es de ..." |
| T10 | baja | OC-2, OC-9 | fuentes, no el texto: MAPA l. 120 y l. 123; `_candidatos.md` l. 47 | GAPLIT Niu: "sin PDF, raw ni ficha"; "anexos.tex:21 aun da SSIM 0.587" | `refs/raw/niu2021multiple.bib` (existe: Niu, Li y Wang, SPIE 11840, 2021); `papers/` sin PDF; `docs/literatura/` sin ficha; ANX:21 sin cifras | El `\GAPLIT` de l. 82 sigue justificado y su texto es exacto ("de la que el repositorio no tiene ficha"). Pero MAPA y `_candidatos` dicen que falta el raw, que ya existe, y `_candidatos` da dos autores (el raw da tres); la nota de MAPA l. 123 sobre ANX:21 ya no vale | Avisar a la autora: actualizar MAPA l. 120 ("falta PDF y ficha; raw en `refs/raw/niu2021multiple.bib`"), `_candidatos` l. 47 y MAPA l. 123. Siguiente paso para cerrar el GAP: PDF y lectura con `lector-papers`, luego `refs/clean/` |

TOTAL alta=3 media=3 baja=4

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 8-10 | Estructura del capitulo y relacion seccion-objetivo | Organizacion propia; objetivos de `introduccion.tex` | si |
| l. 12 | Revision narrativa y dirigida; lista definida por la autora; busquedas con fecha | DEC 2026-10-08 pto 29; MAPA l. 117 | si |
| l. 12 | "De una de las fuentes ... solo se dispuso del resumen" | `_index.md` l. 62 (`zhang2026pediclescrew` ABSTRACT); las demas 44 fichas citadas no son solo abstract (grep de "Profundidad") | si |
| l. 16 | Dos familias; claves de cada una | fichas `chen2024tumorsynthesis`, `ramzan2026claim`, `jacob2026lgesynthnet`, `zhang2025lefusion`, `zhang2025diffboost`, `konz2024anatomicallycontrollable` | si |
| l. 16 | Las rayas irradian desde el metal | `deman1999`, "a number of streaks can be seen radiating from the metals" (Sec. III-D, p. 694) | si |
| l. 18 | DiffTumor, difusion latente; region sana = complemento | `chen2024tumorsynthesis`, "z0^healthy := (1 − m) ⊙ z0" (§3.2, p. 4) | si |
| l. 18 | No modela textura fuera del tumor | id., "we do not intend to model organ textures outside of the tumors" (§3.2, p. 4) | si |
| l. 18 | Saturacion [-175, 250] HU | id., Apendice E.2, p. 21 | si |
| l. 18 | Dice higado 62.5 -> 66.5 %, una de tres redes, cinco particiones | id., Tabla 4, p. 17 (U-Net, promedio 5-fold) | si |
| l. 18 | Cuatro radiologos; cerca de la mitad tomada por real | id., "Four radiologists" (§4.1, p. 5); "nearly 50% of synthetic samples are still incorrectly identified as real" (§4.1, p. 6) | si |
| l. 20 | Difusion en imagen; perdida en la mascara; recomposicion del fondo con ruido | `ramzan2026claim` filas 1, 3, 4, 10 (Sec. 2-2.1, pp. 3-5) | si |
| l. 20 | Adaptado de LeFusion | id., fila 11 (Sec. 2.1, p. 4) | si |
| l. 20 | LeFusion: nodulos en TC, perdida en lesion, fondo real difundido | `zhang2025lefusion`, "Que hace" l. 9 | si |
| l. 20 | Dice 58.89 -> 63.53 (sin unidad) | `ramzan2026claim` filas 50, 52 (Tabla 2, p. 11); BITACORA §2 (cifra sin unidad) | si |
| l. 20 | Sin metricas de fidelidad; fondo solo cualitativo | id., filas 58 (NO ENCONTRADO), 9, 59 | si |
| l. 22 | LGESynthNet, ControlNet, mapa de bordes, imagen enmascarada | `jacob2026lgesynthnet`, Abstract p. 1; Sec. 3.1, p. 3 | si |
| l. 22 | Mejora de Dice sin cifra (resumen frente a resultados) | id., Sec. 1 p. 2 ("upto 6") y Sec. 5 p. 8 ("5 points"); DEC 2026-10-08 pto 32 | si |
| l. 22 | Sin paso que restituya pixeles; SSIM de imagen completa; perdida atribuida a la compresion | id., NO ENCONTRADO (pegado), Sec. 4.4 p. 8, "compressed through the latent space, resulting in lower SSIM" (Sec. 5, p. 8) | si |
| l. 22 | Lectura propia del autoencoder | Marcada "Este trabajo lee" | si |
| l. 24 | DiffBoost: ControlNet sobre Stable Diffusion, imagen completa desde ruido, corte a corte, texto y borde, mezcla por parches aleatorios | `zhang2025diffboost` l. 13-27, 65; Alg. 1, p. 3676 | si |
| l. 24 | Dice 78.46 -> 84.56 % (prostata RM), 94.42 -> 94.78 % (bazo TC), 62.92 -> 71.65 % (mama, eco) | id., §IV-B, pp. 3677-3678; Tabla II, p. 3678 | si |
| l. 24 | Konz: mascara concatenada en cada paso, imagen, desde ruido, [0, 255], Dice 0.8980, 40 pacientes | `konz2024anatomicallycontrollable` l. 9, 12, 26, 28, 29 | si |
| l. 26 | Hu: efecto de masa hasta 1.3 r | `hu2023`, Tabla 1, p. 7426 | si |
| l. 26 | Jin: parche 3D completo, GAN, region de borde supervisada | `jin2021freetumor` l. 9, 14 (Sec. 3.4.1, p. 9) | si |
| l. 26 | Wu (prepublicacion): conserva valores fuera de la mascara | `wu2025freetumor`, "other positions are reserved as the original values" (Sec. 4.2, p. 20); arXiv | si |
| l. 28 | RePaint: DDPM incondicional preentrenado, sin reentrenar, region conocida y remuestreo; 256 x 256 | `lugmayr2022repaint` l. 9, 12, 23 | si |
| l. 28 | El sintetizador no es RePaint ni LeFusion; perdida solo en `G`, sin remuestreo | DEC 2026-10-08 pto 5; MAPA l. 118 | si |
| l. 30 | Cinco miden por segmentacion; dos con similitud; uno con prueba visual | fichas de las cinco claves (Dice en cada una); `jacob` y `diffboost` SSIM/MS-SSIM; `chen2024` Turing | si |
| l. 34 | Zhang y Yu: 15 formas, TC reconstruidas, 120 kVp, Poisson; dispersion y volumen parcial no mencionados | `zhang2018` l. 18, 33, 37 (NO ENCONTRADO) | si |
| l. 34 | Lin: 100 formas, volumen parcial | `lin2019` l. 53, 71 (Sec. 4, p. 10508) | si |
| l. 34 | Wang 2019: mascara tubular, 1090 volumenes, Beer-Lambert, cinco energias | `wang2019cochlear` l. 26, 27, 52, 63 | si |
| l. 34 | Karageorgos: objetos definidos desde TC de metal; CatSim de XCIST | `karageorgos2024ddpm`, "Random metal objects were defined based on CT images of metal objects" (Sec. II-A, p. 3); `wu2022xcist` "image simulation components of XCIST are a new implementation of CatSim" (p. 6) | si |
| l. 36 | 31 % de equipos con difusion | `haneda2025aapm`, Sec. 3.1, p. 11 | si |
| l. 36 | DDPM incondicional en sinograma, entrenado sin metal; metal reinsertado por umbral | `karageorgos2024ddpm` l. 93, 117, 118, 141 | si |
| l. 36 | SSIM 0.964 simulado; 13 de 28 metricas en cuatro TC clinicas con metal disenado a mano | id., Tabla I p. 28; Sec. III-C p. 12; Sec. II-A p. 4 | si |
| l. 38 | Yun: correccion de endurecimiento en proyeccion + difusion latente; CLINIC-metal; mascara por umbral | `yun2026simulationdriven` l. 11-21, 37 | si |
| l. 38 | Sesgo 0.82 HU frente a 3.18-6.30 HU de cuatro metodos | id., Tabla 4, p. 11 ("4.20 3.18 6.30 5.89 0.82") | si |
| l. 38 | CLINIC-metal por inferencia a una carpeta local | BITACORA §2 (2026-09-30); `docs/02-datos.md` | si |
| l. 40 | Peters: calibracion contra fantoma; 14 000 casos; fractales; ocho metricas; 29 escenarios; base del AAPM | `peters2025hybrid` l. 18-20, 44, 47, 157; `haneda2025aapm` | si |
| l. 40 | < 2 %; ruido < 10 % sin artefacto evidente; hasta 13.3 % | id., 3.1, p. 6 (l. 353-354 de la ficha) | si |
| l. 42 | Validacion no cubre el paso hibrido ni la geometria; todo 2D | id., 2.3 p. 3 (filtro de realce); Abstract p. 1 ("all datasets are simulated in 2D") | si |
| l. 44 | Peters: hasta cinco objetos al azar; colocacion realista impracticable; "meaningful locations" | id., 2.3 p. 4; Discussion p. 9 | si |
| l. 44 | Karageorgos: 50 % de solape con > 200 HU | `karageorgos2024ddpm`, Sec. II-A, p. 4 | si |
| l. 44 | Wang 2019: "en el centro" | `wang2019cochlear`, "near the center" | no (T08) |
| l. 44 | Wang 2025: insercion manual, ajuste de tamano, angulo y posicion | `wang2025adaptiveweighting`, Sec. V-A-2, p. 2414 | si |
| l. 46 | XCIST como fundamento, no reimplementado y validado | `CLAUDE.md` raiz; DEC 2026-10-05 (3) "Dependencia" | si |
| l. 46 | Validacion de primer orden; varillas Ti 20 mm y Fe 10 mm | `wu2022xcist`, Validation p. 9; Fig. 11, p. 29 | si |
| l. 46 | Traza distorsionada > 3.0 cm; 274 de 14 000 | `haneda2025aapm`, Sec. 4, p. 16 | si |
| l. 48 | Ren: sondas, ruido y endurecimiento; varilla Ti 12.7 mm; dos crioablaciones; datos del fabricante; implantes ortopedicos | `ren2022metalinsertion` l. 28, 50, 62, 66, 93 | si |
| l. 52 | Planificacion automatica revisada | IMP #180, #192; fichas `han2019atlasplanning`, `goerres2017planning` | no (T04) |
| l. 54 | Liu: 14 casos CTPelvic1K; optimizacion; plan unico | `liu2025pipeline` l. 25, 47-48 | si |
| l. 54 | 2.56 mm y 3.31 grados; 12 casos; 86.7 %; tres cirujanos | id., IV-A p. 16; IV-B pp. 16-17; Abstract p. 2 | si |
| l. 54 | 10.58 ± 3.84 frente a 4.36 ± 3.83 mm | id., Tabla III, p. 38 | si |
| l. 54 | Cresta, pubis, acetabulo; sin iliosacros; no aplica a sacro | id., l. 138 (p. 14, p. 18) | si |
| l. 56 | Zhang 2026, solo resumen: TC sintetica desde TC de haz conico; tornillos pediculares; mitiga artefacto | `zhang2026pediclescrew` l. 3, 17, 31, 35 | si |
| l. 58 | Ramzan: 17 segmentos, volumenes uniformes, comparacion visual con otro generador | `ramzan2026claim` filas 19, 21, 62 | si |
| l. 58 | Chen: elipsoides refinados con radiologos | `chen2024tumorsynthesis`, §3.3, p. 5 | si |
| l. 58 | Jacob: elipsoide en region al azar | `jacob2026lgesynthnet`, Sec. 3.1, p. 4 | si |
| l. 60 | Zwingmann 2009: cuatro niveles, TC posoperatoria; 69 % y 40 %; p = 0.02 | `zwingmann2009navigated` l. 34-38, 43, 83 | si |
| l. 62 | 2.6 % (1832) y 0.1 % (262); cohorte 2009 con cero; malposicion = revision | `zwingmann2013` l. 25-26, 46, 99-100 | si |
| l. 64 | Zwingmann 2010: 63 y 131 tornillos; 81/11/3/5 y 42/22/21/13 + 2 % grado 4 no definido; solapamiento posible | `zwingmann2010percutaneous` l. 12, 23-26, 32; DEC 2026-10-08 pto 31 | si |
| l. 66 | Herman: binaria, por nivel; 36.5 % S1, 14.8 % S2, p = 0.035; ninguno fuera del hueso | `herman2016` l. 68, 128, 141 | si |
| l. 66 | Poses bajo S1 se reportaran al preinscribir | C3 `sec:poses`; MAPA l. 66 (`\GAPDATO` en C3) | si |
| l. 66 | Poses fuera del hueso = grado 3 en SAP | C3 l. 302 | si |
| l. 68 | Kaiser: 104 TC, eje del sacro perpendicular al platillo de S1, area, longitud, angulos | `kaiser2014dysmorphism` l. 17-18, 81, 201 | si |
| l. 68 | McLaren: 433 TC, 352 en S1 | `mclaren2021corridor` l. 67 | si |
| l. 68 | Ramadanov y Zabler: descripcion cualitativa | `ramadanov2025safezone` l. 20, 83 | si |
| l. 70 | Gardner: 50 TC, lado sin lesion; 222 frente a 346 mm2; estudio previo sin diferencia | `gardner2010safezones` l. 55, 72, 238 | si (T09: falta "media") |
| l. 70 | Ziran: 17 pelvis; 7-25 %; 97-140 % ala superior S1 en plano frontal sacro | `ziran2007fluoroscopic` l. 101, 315, 320 | si |
| l. 72 | Cuatro carencias frente al Obj 2 | cuerpo del capitulo; ver T04 para la primera | parcial (T04) |
| l. 74 | Un radiologo; escala de Smith; pediculares; cuatro cadaveres; Herman binaria; Liu margen | `zwingmann2009navigated` l. 70, 84; `smith2006iliosacral` l. 19, 41; `herman2016`; `liu2025pipeline` | si |
| l. 74 | SAP solo perforacion | DEC 2026-10-08 pto 15; MAPA l. 69 | si |
| l. 76 | Arand: 50 TC post mortem; valores de gris; ala menor que cuerpo de S1; sin HU ni calibracion; no lo propone como restriccion | `arand2019pelvicring` l. 9, 16-25, 42-46 | si |
| l. 76 | Densidad fuera de SAP, trabajo futuro | DEC 2026-10-08 pto 14 | si |
| l. 76 | Tres de ocho metricas; inversion de streak amplitude; bone/metal integrity con lectura invertida | DEC 2026-10-05 (3)-(4); DEC 2026-10-08 pto 10 | si |
| l. 80 | Saturaciones <= 600 HU (Chen 250, Hu 189, Jin 600, Wu 500) | `chen2024tumorsynthesis` E.2; `hu2023` p. 7427; `jin2021freetumor` Sec. 4.2; `wu2025freetumor` Tabla A19 | si |
| l. 80 | Umbral 2500 HU en Wang y Li | `wang2025adaptiveweighting` Sec. V-A-2; `li2024` Sec. IV-E | si |
| l. 82 | Tres ventanas; cascada | `wang2025adaptiveweighting` l. 45-49, 108 | si |
| l. 82 | `\GAPLIT` fuente primaria del esquema | Sin ficha ni PDF; raw `refs/raw/niu2021multiple.bib`; `_candidatos.md` l. 47 PENDIENTE | si (marca justificada; T10 sobre MAPA) |
| l. 82 | 26.76 dB / 0.9501 frente a 32.67 dB / 0.9803, datos simulados | id., Sec. V-B, p. 2414 | si |
| l. 82 | 14 volumenes CLINIC-metal; cinco medicos; 30 imagenes | id., Sec. V-A-2 y V-C-3 | si |
| l. 84 | Li: ventanas en perdida y evaluacion; entrada [-1000, 2000] HU; +0.64 dB metal grande | `li2024` l. 38, 45, 58 | si |
| l. 86 | Ida y vuelta sin autoencoder medida en el Obj 1 | `experiments/objetivo1/p1_compuerta.md`:31-38; MAPA l. 68 | si |
| l. 86 | `pub+asinh` en coma flotante de 32 bits | DEC 2026-10-08 pto 1 (l. 2080) | si |
| l. 88 | Rombach: elimina alta frecuencia; cuello de botella | `rombach2022latentdiffusion` l. 22, 57 | si |
| l. 88 | Chen 2026: prepublicacion; congelados; sin ajuste medico; PSNR, SSIM, MSE sin unidades; [-1000, 1000] HU | `chen2026foundationvae` l. 4, 40, 53, 55-56 | si |
| l. 88 | Guo: metricas de similitud; rango no declarado | `guo2025maisi` l. 29, 37, N4 | si |
| l. 90 | RMSE 12.3 (DDPM) y 20.2 (NMAR); NMAR calibra la escala de Peters | `karageorgos2024ddpm` Tabla I; `peters2025hybrid` 2.5, p. 5 | si |
| l. 90 | Yun RMSE 12.74 | `yun2026simulationdriven`, Tabla 1, p. 10 | si |
| l. 92 | De Man en sinograma | `deman1999` l. 21, 138 | si |
| l. 92 | Lin: 31.45 frente a 33.51 dB; entrada LI; problema mal planteado | `lin2019` l. 43-44, 117; Sec. 4 | si |
| l. 92 | Li: rama de imagen desde la reconstruccion con artefacto; `\GAPDATO` de cifras | `li2024` l. 31, 51, 55 (advertencia de transcripcion) | si (marca justificada) |
| l. 92 | "Ningún trabajo revisado sintetiza ... y evalúa su coherencia física" | Se sostiene por la conjuncion; IMP #179 | parcial (T05) |
| l. 92 | "la comparación prevista ... podría contradecir" | RP1; DEC15 pto 15 | no (T07) |
| l. 94 | De Man: 2D, varilla de hierro y amalgama; rayas oscuras y radiales | `deman1999` l. 10-12, 87-89 | si |
| l. 94 | Park: cupping dentro, rayas fuera | `park2015ct` l. 9, 27 | si |
| l. 94 | Glover y Pelc: monocromatico; hueso, no metal | `glover1980nonlinear` l. 14, 35 | si |
| l. 94 | Selles: 25 pacientes, fusion sacroiliaca, hueso y musculo, cerca y contralateral, sin distancia | `selles2023ai` l. 12, 25, 29 | si |
| l. 94 | Li: artefacto global, sin medirlo | `li2024` l. 18, 82 | si |
| l. 96 | Radzi: desde el eje; umbral no publicado; 2.0/2.6/1.6/2.0 mm; 3.5-4.0 mm; un tobillo | `radzi2014metalartifacts` l. 12-23, 39-42 | si |
| l. 96 | Cassanego: 3.1-4.2 mm; metodo de Radzi; 3.0-3.5 mm; seis miembros caninos; punto de medida no declarado | `cassanego2026evolution` l. 12, 35-36, 47-49, 99-104 | si |
| l. 96 | ~12 mm de B_delta como convencion | CLAUDE.md raiz; DEC 2026-10-13 (D1) | parcial (T06) |
| l. 98 | Karageorgos: pelvis con dos marcadores de oro; 7.57; 11.45 (1.4x); 54.82 (0.7x) | `karageorgos2024ddpm` l. 54-58, 171, 173 | si |
| l. 102 | Nueve trabajos en la tabla | ANX:19-27 (nueve filas) | si |
| l. 102 | Muestreador y SAP ejecutados | C3; MAPA | si |
| l. 102 | `\GAPDATO` "modelo final no está elegido" | RP1; DEC15 pto 15; DEC 2026-10-11 (3) | no (T01) |
| l. 104 | Peters validada en fantoma y 2D | `peters2025hybrid` Abstract | si |
| l. 106 | Tres enfoques; ninguno produce a la vez poses y artefacto | Cuerpo del capitulo; DEC 2026-10-08 pto 25 | si |
| l. 106 | Comparacion con copia y pegado y "segunda comparación" con el protocolo, "según el plazo", "sobre las poses del muestreador" | DEC1005 pto 5; DEC15 ptos 9, 12, 13 | no (T02) |
| l. 106 | Protocolo exige proyecciones por pose, 2D, una fila de detector | DEC 2026-10-08 pto 25 (l. 2155); DEC l. 1902 | si |
| l. 106 | "Si el sintetizador alcanza la equivalencia ..." | RP1; DEC15 pto 15 | no (T07) |
| l. 108 | Tres elementos; distribucion preinscrita; sin ajuste a la referencia; ningun objetivo los aisla | `experiments/objetivo2/preinscripcion_muestreador.md`; DEC 2026-10-08 pto 30; `introduccion.tex` §Justificacion | si |
| l. 110 | Wang 2019 mascara tubular, no segmentada; "en el centro" | `wang2019cochlear` l. 63 | no (T08) |
| l. 110 | Zhang y Yu a mano; Karageorgos desde TC de metal; Peters fractales; Yun, Wang, Li por umbral | fichas citadas (filas de l. 34-44, 80) | si |
| l. 110 | Xie: sensibilidad 100 %, Dice 82.92 %, 2500 HU, datos simulados | `xie2024implantsegmentation` l. 47-48 | si |
| l. 110 | El sintetizador se entrena con mascaras umbralizadas | DEC 2026-10-08 ptos 6-7; IMP #128.4 | si |
| l. 112 | Piezas publicadas: metal virtual, difusion frente al artefacto, mascara en imagen, LeFusion, Hu, Jin | fichas citadas | parcial (T05) |
| l. 112 | Combinacion de cuatro rasgos | DEC 2026-10-08 pto 30 | si |
| l. 114 | Supuesto y convencion; evaluacion por coherencia fisica y quirurgica, no por segmentacion | DEC 2026-10-08; `docs/00-tesis.md` Fuera de alcance pto 1 | si |
| ANX:19-27 | Celdas de los nueve trabajos | Mismas fichas que el cuerpo; Jacob sin cifras (DEC 2026-10-08 pto 32) | si |
| ANX:29 | Fila propia: "sin resultado del sintetizador ... según el plazo" | RP1; DEC15 | no (T03) |
| todo | Claves `\cite`: 45 de 45 en `overleaf/referencias.bib`; primer apellido coincide con el `.bib` en todas; ninguna cita es sujeto gramatical sola | `overleaf/referencias.bib` | si |
| todo | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet como metodo vigente, "31-60 %", BFC, ISC) | grep en la seccion: ausente; l. 88 trata la difusion latente como pregunta del Obj 1, no como metodo | si |
| todo | Patrones VIGENTES del dominio | PAT-122 (T01, T03), PAT-19 (T01), PAT-175 y PAT-11 (T02, T03), PAT-27 (T06), PAT-116 (T07), PAT-148 afin (T04); sin reincidencia: PAT-13, PAT-136 (cubierto por T07), PAT-138/158 (EXP3 l. 85, 93 ya tiene RP1 HECHO), PAT-155, PAT-162, PAT-163, PAT-166, PAT-167, PAT-168, PAT-169, PAT-172, PAT-176 | — |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP de resultado propio que niega un modelo elegido y una evaluacion ya hechos | OC-2, G-T4 | "no existe aún resultado del Objetivo~3 porque el modelo final no está elegido" | PAT-122 |
| La seccion promete sobre las poses del muestreador lo que se ejecuto sobre el eje sin perturbar | G-T4 | "ejecutar el protocolo físico sobre las poses del muestreador ... según el plazo" | PAT-175 (y PAT-11) |
| La jerarquia de contrastes se enuncia al reves: el control de cordura como comparacion principal y el contraste primario como "segunda" | G-T4, OC-3 | "prevé comparar ... con la inserción por copia y pegado. Prevé, además, ... segunda comparación" | nuevo |
| Una tabla de otro archivo (anexos) que resume la seccion conserva el estado viejo cuando el encargo solo toca el `.tex` del capitulo | G-T4, G-B8 | Fila "Este trabajo": "sin resultado del sintetizador ... según el plazo" | nuevo |
| Implicancia ABIERTA que pide nombrar o acotar con fichas nuevas no deja marca en el estado del arte | OC-2 | planificadores por atlas (#180) y sintesis aprendida en MAR no pareada (#179) sin mencion | PAT-123 (reincide tras ERRADICADO) |
| Limitacion de una convencion propia redactada solo frente a la literatura, sin la medicion propia que DEC registra | OC-3, G-T4 | "La banda $B_{\delta}$ trunca por diseño los efectos ..." (sin D1) | PAT-27 |
| Condicional o "prevista" sobre una comparacion ya ejecutada y clasificada | G-T4 | "la comparación prevista con el protocolo físico podría contradecir ese supuesto" | PAT-116 |
