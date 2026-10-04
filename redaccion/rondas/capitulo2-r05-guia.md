# Revision guia CS — capitulo2 — r05

Leido: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§1 y §2 enteros),
`capitulo2-r04-guia.md`, `capitulo2-r04-respuesta.md`, `overleaf/secciones/capitulo2.tex` (entero),
`introduccion.tex` (entero) y `capitulo3.tex` (ll. 54-78, 168-179, grep de `sec:obj1`) para G-A7, G-B10, G-T3 y
G-T5. Cotejos puntuales: ficha `wang2025adaptiveweighting` (Sec. V-B, p. 2414), ficha `gardner2010safezones`,
`docs/01-decisiones.md` 2026-09-08 (4). `capitulo1.tex` y `capitulo4.tex` siguen siendo esqueleto.
Aplicados de r04 comprobados y sin reincidencia: "esquema multiventana" en l. 124, banda en la salvedad del aporte
(l. 128), escala publicada del criterio de 25 HU (l. 86), orden de 2.3 (l. 52), "reduccion de la fractura" (l. 54 y
tabla), acotacion de las fuentes que umbralizan (l. 130), celda del muestreador respaldada en l. 128. No se reabre el
rechazo de guia-9 (zona segura): la ficha de Gardner no trae una frase de definicion que copiar, asi que el motivo
sigue en pie.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | P-EA2, G-T4 | capitulo2.tex:80, :117 | Patron PAT-31 reincide. Tras el cambio de orden de r04 (ES-02), la PSNR de 26.76/32.67 dB y el SSIM de 0.9501/0.9803 siguen a la oracion de CLINIC-metal, que "carece de imagen sin artefacto"; el lector los atribuye a ese conjunto, donde no pueden calcularse. La ficha los da en la prueba sintetica (Sec. V-B, p. 2414). La celda de la tabla tampoco tiene la condicion. | Dar la condicion junto a las cifras ("en su conjunto de prueba sintetico, una red que no se entreno...") en l. 80 y en la celda de Wang et al. |
| guia-2 | media | G-B9, G-B6 | capitulo2.tex:68 (contra capitulo3.tex:168, introduccion.tex:75; DEC 2026-09-08 (4)) | Patron PAT-84 reincide. Gardner et al. es la fuente que la decision incorpora como respaldo para medir el corredor en cada volumen (S1 y segundo nivel), y el cap. 3 y el alcance la usan para no estratificar por dismorfismo. El parrafo del estado del arte sobre la geometria del corredor, que justifica justamente medir por volumen y no reproducir una pose canonica, no la presenta: solo Kaiser, McLaren, Ramadanov y Ziran. | Una o dos oraciones en l. 68 con el resultado de Gardner et al. (area minima de la zona segura en S1, 222 frente a 346 mm2, y el estudio previo sin diferencia) y su consecuencia para el Obj 2: medir el corredor en cada volumen. |
| guia-3 | baja | G-A7, P-EA3 | capitulo2.tex:128 (contra introduccion.tex:58, :60) | Patron PAT-66 reincide. "Como declara la justificacion de la introduccion, ningun objetivo aisla la geometria parametrica, y tampoco la codificacion ni la banda, porque el Objetivo 3 evalua el sintetizador completo": la introduccion da para la geometria otra razon ("ningun brazo de comparacion coloca geometrias extraidas por umbral"). La oracion atribuye a la introduccion una razon que esta solo da para la codificacion y la banda. | Partir la razon: la geometria no se aisla porque ningun brazo coloca geometrias umbralizadas; la codificacion y la banda, porque el Obj 3 evalua el sintetizador completo. |
| guia-4 | baja | G-B7 | capitulo2.tex:44, :70 (contra :38) | Patron PAT-87 reincide. "Los trabajos de insercion y de MAR revisados colocan el metal al azar, con una regla geometrica ... o a mano" y "Los trabajos de la Seccion ea-simulacion colocan el metal ..." incluyen a Yun et al., cuyo metal es clinico y "entra como una mascara conocida" (l. 38), y a Zhang y Yu y Lin et al., cuya colocacion el cuerpo no describe. | Acotar el sujeto: "Los trabajos revisados que insertan metal y describen su colocacion ...", o nombrarlos. |
| guia-5 | baja | G-B8 | capitulo2.tex:119 | Patron PAT-67 reincide. La celda propia dice que el sintetizador "se comparara por *streak amplitude* con la insercion por copia y pegado"; el cuerpo del capitulo no nombra nunca la insercion por copia y pegado (solo el protocolo fisico, l. 126). | Una clausula en l. 98 o l. 134 con las dos comparaciones previstas del Obj 3, o quitar la copia y pegado de la celda. |
| guia-6 | baja | G-T2 | capitulo2.tex:86 (contra :52, :72) | Patron PAT-14 reincide. "Escala" designa la escala ordinal de grados de brecha (ll. 52, 72) y, en l. 86, tanto el orden de magnitud de los errores ("La escala mas proxima la dan", "Con esa escala") como la calibracion de las metricas de Peters et al. ("calibran la escala de sus metricas"), tres sentidos en dos parrafos. | En l. 86 usar "orden de magnitud", como `capitulo3.tex`:67, y reservar "escala" a la de brecha cortical. |
| guia-7 | baja | G-T1 | capitulo2.tex:82 (contra introduccion.tex:46, capitulo3.tex:172) | Patron PAT-88 reincide. "La ida y vuelta de esas variantes sin autoencoder se midio en los experimentos del Objetivo 1 ... se presenta en el capitulo de resultados": ni `sec:obj1` describe esa medicion ni el cap. 4 existe, y la introduccion la da como pendiente (`\GAPDEC`). El dato existe segun la respuesta r03, asi que el fallo esta en las otras dos secciones; en esta, la afirmacion no se puede verificar en el documento. | Mantener mientras la respuesta lo registre como pendiente de alinear `introduccion.tex`:46 y `capitulo3.tex`:172 (ya anotado en r04); no requiere cambio en esta seccion si el orquestador lo escala. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple salvo guia-7 (baja) |
| G-T2 | cumple salvo guia-6 (baja); "zona segura" sin definicion en el documento (rechazo r04 con motivo vigente; depende de `introduccion.tex`:75). "Volumen parcial" y "fantoma" quedan para el marco teorico (esqueleto) |
| G-T3 | cumple ($G$, $M$, $B_{\delta}$, $p$ iguales a la introduccion y el cap. 3) |
| G-T4 | cumple con GAP salvo guia-1 (media); los RMSE van sin unidad aqui y con HU en `capitulo3.tex`:67 (pendiente 3 de la respuesta r04, del auditor) |
| G-T5 | cumple (orden anunciado en ll. 10 y 52 = orden real; transicion al cap. 3 en l. 134); desde el cap. 1: no evaluable |
| G-T6 | cumple (lint PASA) |
| G-B5 | cumple: Obj 1 (ll. 84-86, con escala del criterio), Obj 2 (l. 70), Obj 3 (ll. 30, 88-94), Obj 4 (ll. 72-74) |
| G-B6 | cumple con GAP (`\GAPDEC` del protocolo de busqueda, l. 12); guia-2 (media) en cobertura de la geometria del corredor |
| G-B7 | cumple; guia-4 (baja) |
| G-B8 | cumple (enfoque, colocacion/exterior, resultado con condicion, fila propia con supuesto y convencion); guia-1 (condicion de Wang) y guia-5 (bajas en la tabla) |
| G-B9 | cumple salvo guia-2 (media) |
| G-B10 | cumple con GAP (l. 126 = `introduccion.tex`:54, mismo `\GAPDEC`; tercer enfoque en l. 124 = `introduccion.tex`:56). Fuera de esta seccion, sin reporte aqui: `introduccion.tex`:60 dice "codificacion de la entrada" frente a "entrada y salida" (l. 82 y `capitulo3.tex`:172); la Formulacion del problema (`introduccion.tex`:21) sigue con Dice/HD95, con `\GAPDEC` en l. 28 |
| P-EA1 | cumple (prepublicaciones de Wu 2025 y Chen 2026 senaladas; fuente de solo resumen senalada) |
| P-EA2 | cumple salvo guia-1 (media) |
| P-EA3 | cumple con GAP (resumen l. 124, aporte l. 128-130 con salvedad #128.4, reclamo estrecho con `\GAPDEC` l. 132); guia-3 (baja) |

Patrones VIGENTES comprobados: PAT-14 (reincide, guia-6), PAT-19 (no reincide en esta seccion: los nueve `\GAPDEC`
nombran decisiones no tomadas; el de l. 82 coincide con el borrador no congelado de `capitulo3.tex`:172),
PAT-31 (reincide, guia-1; el resto de cifras llevan condicion), PAT-66 (reincide, guia-3; la formula de colocacion
de ll. 44, 70, 124 es la decidida), PAT-67 (reincide, guia-5), PAT-69 (no reincide: l. 130), PAT-70 (no reincide),
PAT-71 (no reincide), PAT-76 (no reincide), PAT-79 (no reincide en Liu y Herman), PAT-83 (no reincide), PAT-84
(reincide, guia-2), PAT-87 (reincide, guia-4), PAT-88 (reincide, guia-7). De criterio solo E-* (PAT-80, -85,
-86, -89) quedan para `revisor-estilo`; notas para ese revisor: l. 82 tiene ocho oraciones con tres funciones
(Li et al., delimitacion del reclamo, estado de la medicion propia); l. 62 "solo el segundo sirve de comparacion
para un muestreador" es lectura propia sin marca (PAT-85); l. 12 usa "referencias" en sentido bibliografico.

## Propuestas de criterio
- Sin propuestas nuevas.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Reordenar oraciones deja una cifra junto a una condicion que no es la suya | P-EA2, G-T4 | CLINIC-metal "carece de imagen sin artefacto" seguido de PSNR 26.76 dB | PAT-31 |
| Fuente que una decision incorpora como respaldo del diseno, ausente del estado del arte | G-B9 | Gardner (medir corredor por volumen) solo en cap. 3 y alcance | PAT-84 |
| Remision a otra seccion que le atribuye una razon que esa seccion da para otra cosa | G-A7 | "Como declara la justificacion ... porque el Objetivo 3 evalua" (geometria) | PAT-66 |
| Sujeto colectivo "los trabajos de la seccion" que incluye fuentes a las que no aplica | G-B7 | "Los trabajos de la Seccion colocan el metal" (Yun no coloca) | PAT-87 |
| Termino de una escala de medida reusado como "orden de magnitud" | G-T2 | "La escala mas proxima la dan los errores de la MAR" | PAT-14 |
