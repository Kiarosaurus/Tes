# Revision guia CS — capitulo2 — r06

Leido: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§1, §2 y §3 enteros),
`capitulo2-r05-guia.md`, `capitulo2-r05-respuesta.md`, `overleaf/secciones/capitulo2.tex` (entero),
`introduccion.tex` (entero) y `capitulo3.tex` (ll. 54-178 y 211-265) para G-A7, G-B10, G-T3, G-T4 y G-T5.
Cotejos puntuales: ficha `kaiser2014dysmorphism` (fenotipos y conglomerados), `docs/01-decisiones.md`
2026-09-08 (2) y (4), `docs/literatura/_index.md` (estado de prepublicacion de las fuentes citadas).
`capitulo1.tex` y `capitulo4.tex` siguen siendo esqueleto.

Aplicados de r05 comprobados y sin reincidencia: condicion simulada de la PSNR/SSIM de Wang et al. en cuerpo
(l. 82) y tabla (l. 121); Gardner et al. presentado en la geometria del corredor (l. 70); dos razones partidas en
l. 132; sujeto acotado en ll. 44 y 72; copia y pegado respaldada en el cuerpo (l. 130); "orden de magnitud" en l. 90.
T02 (unidad de los RMSE) esta ESCALADO: no se reporta. ES-18 RECHAZADO con motivo (G-B10): no se reabre.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-B7, G-T4 | capitulo2.tex:70 (contra :68 y ficha `kaiser2014dysmorphism`) | Patron PAT-87 reincide. "Las mismas mediciones muestran que ... esa variacion no se agrupa de forma consistente por fenotipo": "las mismas" remite a Kaiser y McLaren (l. 68), pero Kaiser et al. agrupan justamente sus mediciones en tres fenotipos por conglomerados (41 % dismorfico). La evidencia de la inconsistencia es Gardner frente al estudio previo, no esas mediciones. | Quitar "Las mismas mediciones" y atribuir la inconsistencia a los estudios que la muestran (Gardner et al. y el estudio que recogen). Si se nombra la agrupacion de Kaiser, presentarla como la alternativa descartada por DEC 2026-09-08 (2), sin citar via Kaiser la definicion de dismorfismo. |
| guia-2 | baja | G-T4 | capitulo2.tex:66 (contra capitulo3.tex:164, introduccion.tex:68) | Patron PAT-31 reincide. "las poses del segundo corredor bajo S1 se reportan de forma descriptiva" pierde la condicion: el cap. 3 y la introduccion marcan con `\GAPDATO` que ese muestreo no esta preinscrito ni ejecutado. Junto a l. 102 ("el muestreador y SAP se ejecutaron"), el lector supone que esas poses existen. | "se reportaran de forma descriptiva cuando se ejecute su muestreo", o replicar el mismo `\GAPDATO` (BITACORA §2, regla de replicar el GAP del cap. 3). |
| guia-3 | baja | G-B10, P-EA3 | capitulo2.tex:84 y :86 (contra introduccion.tex:60, capitulo3.tex:172) | Patron PAT-66 reincide. La carencia de l. 84 dice que ninguna fuente usa las ventanas "como codificacion de la entrada", y el aporte de l. 86, "codificacion de entrada y de salida". La introduccion limita el aporte a "codificacion de la entrada". El cap. 3 dice "entradas y salidas". El aporte queda formulado de dos maneras entre la bisagra de la introduccion y este capitulo. | Unificar con el cap. 3 ("de entrada y de salida") en l. 84. Anotar como pendiente fuera de la seccion que `introduccion.tex`:60 debe decir lo mismo. |
| guia-4 | baja | G-T1, G-T4 | capitulo2.tex:86 (contra introduccion.tex:46, capitulo3.tex:172 y :73) | Patron PAT-88 reincide (sigue de guia-7 r05, pendiente fuera de la seccion). Esta seccion da por medida la ida y vuelta sin autoencoder. La introduccion y el cap. 3 la marcan con `\GAPDEC` como pendiente, y `sec:obj1` solo describe la medicion con autoencoder. | Sin cambio aqui mientras la respuesta lo mantenga como pendiente de alinear `introduccion.tex`:46 y `capitulo3.tex`:172. Si no se alinean, replicar su GAP en l. 86. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple salvo guia-4 (baja) |
| G-T2 | cumple; "zona segura" sin definicion (rechazo r04 con motivo vigente, depende de `introduccion.tex`:75). "Escala", "banda", "marco", "esquema multiventana", "referencia" y "brazo" se usan segun BITACORA §2 |
| G-T3 | cumple ($G$, $M$, $B_{\delta}$, $p$ iguales en la introduccion y el cap. 3) |
| G-T4 | cumple con GAP salvo guia-1 (media) y guia-2 (baja); la unidad de los RMSE (ll. 90, 98) esta escalada (T02) |
| G-T5 | cumple: el orden anunciado en ll. 10 y 52 coincide con el real, y l. 138 da la transicion al cap. 3. Desde el cap. 1: no evaluable (esqueleto) |
| G-T6 | cumple (lint PASA) |
| G-B5 | cumple: Obj 1 (ll. 86-90), Obj 2 (l. 72), Obj 3 (ll. 30, 92-98), Obj 4 (ll. 74-76) |
| G-B6 | cumple con GAP (`\GAPDEC` del protocolo de busqueda, l. 12) |
| G-B7 | cumple salvo guia-1 (media) |
| G-B8 | cumple: enfoque, colocacion, exterior del objeto, resultado con su condicion y fila propia con supuesto y convencion; todas las celdas tienen respaldo en el cuerpo |
| G-B9 | cumple; cada fuente se conecta a un objetivo o a una decision del diseno (Lugmayr l. 28, Ren l. 48, Zhang 2026 l. 56) |
| G-B10 | cumple con GAP: l. 130 coincide con `introduccion.tex`:54 y lleva el mismo `\GAPDEC`; el tercer enfoque coincide con `introduccion.tex`:56; guia-3 (baja) en la formulacion del aporte |
| P-EA1 | cumple: las prepublicaciones de Wu 2025 y Chen 2026 estan senaladas, y tambien la fuente de la que solo se tuvo el resumen. Las demas fuentes de 2025-2026 citadas figuran en `_index.md` como publicadas |
| P-EA2 | cumple (resultados con su condicion en las fuentes principales) |
| P-EA3 | cumple con GAP: el resumen esta en l. 128, el aporte en ll. 132-134 con la salvedad #128.4 y el reclamo estrecho, con `\GAPDEC`, en l. 136; guia-3 (baja) |

Patrones VIGENTES comprobados (los de dominio G-* y G-T4):
- Reinciden: PAT-31 (guia-2), PAT-66 (guia-3), PAT-87 (guia-1) y PAT-88 (guia-4).
- No reinciden: PAT-14 ("escala" solo para escalas de medida y la de Peters), PAT-64 (los negativos de ll. 30, 84, 88 y 128 valen para todo su grupo), PAT-67 (cada celda tiene respaldo), PAT-69 (l. 134), PAT-71 (ll. 10 y 52), PAT-76 (cada cifra tiene su consecuencia en el mismo parrafo o en el siguiente), PAT-84 (las fuentes del cap. 3 que faltan aqui, Tejwani, Reilly, Sayres, Zhu y Gardner 2015, sostienen amenazas o la geometria, no un parametro que el cap. 2 discuta), PAT-90 (l. 90) y PAT-91 (escalado).
- PAT-80, -82, -85, -86, -89, -92 y -93 son de criterio E-* y quedan para `revisor-estilo`.

Nota para `auditor-trazabilidad`: la fila de `jacob2026lgesynthnet` en `_index.md` dice "hoy no se cita ninguna
cifra" por una discrepancia interna del articulo (Dice de 6 frente a 5 puntos), y l. 22 y la tabla citan Dice de
0.72 a 0.77 y SSIM de 0.587.

## Propuestas de criterio
- Sin propuestas nuevas.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Anafora "las mismas mediciones" atribuye una conclusion a fuentes que muestran lo contrario | G-B7, G-T4 | "Las mismas mediciones muestran que ... no se agrupa ... por fenotipo" (Kaiser agrupa) | PAT-87 |
| Resultado de un tramo no ejecutado redactado en presente, sin el GAP del cap. 3 | G-T4 | "las poses del segundo corredor bajo S1 se reportan de forma descriptiva" | PAT-31 |
| La carencia y el aporte nombran distinto el mismo uso de la codificacion | G-B10 | "codificacion de la entrada" (l. 84) / "de entrada y de salida" (l. 86) | PAT-66 |
