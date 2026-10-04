# Revision guia CS — capitulo2 — r04

Leido: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md`, `capitulo2-r03-guia.md`,
`capitulo2-r03-respuesta.md`, `overleaf/secciones/capitulo2.tex` (entero), `introduccion.tex` (entero) y
`capitulo3.tex` (ll. 56-265) para G-B10, G-T3 y G-T5; `capitulo4.tex` es esqueleto; `capitulo1.tex` sigue sin
evaluarse (esqueleto). Los aplicados de r03 se comprueban y no reinciden: tabla con "Resultado reportado y su
condicion" y supuesto/convencion en la fila propia (guia-1), Herman con consecuencia (guia-2), densidad de SAP con
Arand y GAP replicado (guia-3), orden de 2.3 hacia el Obj 4 (guia-4), Cassanego con su condicion, Karageorgos en
2.4, "esquema"/"marco", salvedad de plazo en la tabla. No se reabre ningun rechazo (ES-04 es de estilo).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T2, P-EA3 | capitulo2.tex:122 (contra :82, :126, :130) | Patron PAT-14 reincide. "En las fuentes revisadas, la codificacion multiventana sirve para quitar el artefacto" usa para la MAR el termino que BITACORA §2 (capitulo2-r03) reserva a este trabajo, y contradice la l. 82 ("Ninguna las usa como codificacion de la entrada"). El resumen niega asi el tercer elemento del aporte que la l. 126 reclama. | "el esquema multiventana sirve para quitar el artefacto" (o "las ventanas de HU"), como en las ll. 80-82 y 130. |
| guia-2 | media | P-EA3, G-A7 | capitulo2.tex:126 (contra introduccion.tex:60) | Patron PAT-69 reincide. El aporte dice "Ningun objetivo aisla la geometria parametrica ni la codificacion multiventana, como declara la justificacion", pero la introduccion declara que tampoco se aisla la banda $B_{\delta}$, que es parte del tercer elemento que la misma oracion anterior reclama. Leido asi, la banda parece evaluada por separado. | Anadir la banda: "ni la codificacion multiventana ni la banda $B_{\delta}$, porque el Objetivo 3 evalua el sintetizador completo". |
| guia-3 | media | G-B9, G-B5 | capitulo2.tex:84 (contra capitulo3.tex:67) | Patron PAT-84 reincide. El criterio de 25 HU que hace falsable el Obj 1 se ancla en el cap. 3 en errores publicados de MAR (Karageorgos et al. 20.2 y 12.3 HU de RMSE; Yun et al. 12.74 HU) y en que no se encontro un umbral de aprobacion sobre exactitud de valores de TC. El parrafo del Obj 1 compara las fuentes solo por no medir la ida y vuelta, y el lector del estado del arte no ve de donde sale el criterio. Las ll. 36 y 38 dan de esas mismas fuentes otras cifras (SSIM 0.964; sesgo 0.82 HU). | Una o dos oraciones en la l. 84: ninguna fuente revisada fija un umbral de exactitud en HU; los errores de MAR que reportan Karageorgos et al. y Yun et al., con su condicion, son la escala contra la que se fija el criterio (remision a `sec:obj1`). |
| guia-4 | baja | G-T5 | capitulo2.tex:52 (contra :56-68) | Patron PAT-71 reincide. La oracion de orden enumera "las series clinicas" antes que "la colocacion de mascaras de lesion", y el cuerpo va al reves (mascaras en l. 58, series en ll. 60-66). | Reordenar la enumeracion: planificacion, colocacion de mascaras de lesion, series clinicas, geometria del corredor. |
| guia-5 | baja | G-T2 | capitulo2.tex:54, :113 (contra :86, :92) | Patron PAT-14 reincide. "Reduccion" designa la reduccion de la fractura en Liu et al. ("planifica la reduccion", "error medio de reduccion de 2.56 mm", tambien en la tabla) y la reduccion de artefactos en el resto del capitulo ("Los dos resultados son de reduccion", "experimento de reduccion"). El sentido clinico no se glosa, y en la tabla "Error de reduccion" se puede leer como error de MAR. | Glosar en la l. 54 ("reduccion de la fractura, es decir, la recolocacion de los fragmentos") y en la tabla escribir "error de reduccion de la fractura". |
| guia-6 | baja | G-B7 | capitulo2.tex:128 (contra :34) | "Cuando el metal es clinico, las fuentes lo segmentan con un umbral de HU" queda contradicho dos oraciones antes por Zhang y Yu, que segmentan a mano formas de metal de casos clinicos. El contraste en que descansa el primer elemento del aporte se enuncia mas amplio de lo que las fuentes sostienen. | Acotar: "cuando el metal clinico se segmenta de forma automatica, las fuentes usan un umbral de HU", o nombrar las tres fuentes como sujeto. |
| guia-7 | baja | G-T1 | capitulo2.tex:126 (contra capitulo3.tex:56-75, :172; introduccion.tex:46) | "La ida y vuelta de esa codificacion sin autoencoder se midio en los experimentos del Objetivo 1 ... y su resultado se presenta en el capitulo de resultados": la seccion `sec:obj1` solo describe la medicion a traves del autoencoder, y la introduccion y el cap. 3 dicen que ese error esta pendiente. El dato existe (respuesta r03, T01), pero el lector no puede verificarlo en el documento. El pendiente fuera de esta seccion ya esta anotado. | Hasta que el cap. 3 describa esa medicion, remitir a `sec:obj1` solo cuando la describa; mientras tanto, dejar la oracion y senalar en la respuesta que depende de alinear `capitulo3.tex`:172 e `introduccion.tex`:46. |
| guia-8 | baja | G-B8 | capitulo2.tex:117 | Patron PAT-67 reincide en parte. La celda "Poses preinscritas alrededor del corredor medido en cada volumen" presenta dos hechos (preinscripcion; corredor medido por volumen) que el cuerpo del capitulo no dice: la l. 126 solo dice "sin haberse ajustado a ella". | Una clausula en la l. 126 ("una distribucion preinscrita alrededor del corredor medido en cada volumen") o simplificar la celda a lo que dice el cuerpo. |
| guia-9 | baja | G-T2, G-B1 | capitulo2.tex:68 | Patron PAT-3 reincide. "Zona segura" se usa sin definicion (tambien sin ella en `introduccion.tex`:75, su primera aparicion); para un lector de computacion no queda claro si es lo mismo que el corredor oseo. | Glosa corta en la primera aparicion del documento, o decir aqui su relacion con el corredor. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple salvo guia-7 (baja) |
| G-T2 | cumple salvo guia-1 (media), guia-5 y guia-9 (bajas); SAP, S1, SSIM, PSNR, RMSE, MAR, traza metalica, ida y vuelta, segundo corredor bajo S1 definidos antes o en su primera aparicion |
| G-T3 | cumple ($G$, $M$, $B_{\delta}$, $p$ iguales a los de la introduccion y el cap. 3) |
| G-T4 | cumple con GAP (`\GAPDATO` de Li et al., l. 86); cotejo cifra a cifra, del auditor |
| G-T5 | cumple salvo guia-4 (baja); hacia el cap. 3 cumple (l. 132); desde el cap. 1: no evaluable (esqueleto) |
| G-T6 | cumple (lint PASA) |
| G-B5 | cumple a medias: Obj 2 (l. 70), Obj 3 (l. 30, ll. 86-92) y Obj 4 con sus tres componentes (ll. 68, 72-74) cumplen; Obj 1 compara las fuentes, pero sin el origen de su criterio (guia-3) |
| G-B6 | cumple con GAP (`\GAPDEC` del protocolo de busqueda, l. 12) |
| G-B7 | cumple; guia-6 (baja) |
| G-B8 | cumple (enfoque, colocacion/exterior como supuestos, resultado con condicion, fila propia con supuesto y convencion); guia-8 (baja) |
| G-B9 | cumple salvo guia-3 (media) |
| G-B10 | cumple con GAP (l. 124 = `introduccion.tex`:54, mismo `\GAPDEC`). Fuera de esta seccion, sin reporte aqui: `introduccion.tex`:46 y `capitulo3.tex`:172 dan como pendiente el error de ida y vuelta sin autoencoder que la l. 126 da por medido; `introduccion.tex`:60 dice "codificacion de la entrada" frente a "entrada y salida" (l. 82) |
| P-EA1 | cumple (prepublicaciones senaladas: Wu 2025, Chen 2026; fuente de solo resumen senalada) |
| P-EA2 | cumple (fuentes principales con resultados y su condicion) |
| P-EA3 | cumple con GAP salvo guia-1 y guia-2 (medias): resumen en l. 122, aporte en l. 126, reclamo de novedad con `\GAPDEC` en l. 130 |

Patrones VIGENTES de mi dominio comprobados: PAT-3 (reincide, guia-9), PAT-14 (reincide, guia-1 y guia-5),
PAT-19 (no reincide: el GAP de ida y vuelta nombra solo la decision pendiente), PAT-31 (no reincide: fantoma y dos
dimensiones en l. 122; Xie con "cortes simulados"), PAT-64 (no reincide en su forma; en la l. 128 aparece como
generalizacion afirmativa, guia-6), PAT-66 (no reincide: ll. 44, 70, 122 con la misma formula), PAT-67 (reincide
en parte, guia-8), PAT-69 (reincide, guia-2), PAT-70 (no reincide: densidad y apariencia del Obj 4 cubiertas),
PAT-71 (reincide, guia-4), PAT-72 (no reincide), PAT-76 (no reincide: cada bloque de cifras cierra con su
consecuencia), PAT-77 (no reincide), PAT-78 (no reincide: Ziran, Arand y Karageorgos con el uso que les da el
cap. 3), PAT-79 (no evaluable sin fichas; del auditor), PAT-81 (no reincide, l. 86), PAT-83 (no reincide),
PAT-84 (reincide, guia-3). Los de criterio solo E-* (PAT-33, -80, -82, -85, -86) quedan para `revisor-estilo`;
nota para ese revisor: l. 92 "el resultado orienta hacia generar mas alla" es lectura propia sin marca (PAT-85).

## Propuestas de criterio
- Que el estado del arte presente, para cada objetivo con regla de fallo, la literatura de la que sale su umbral
  (hoy cae bajo G-B9 sin precision; motivo de guia-3).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un termino reservado a lo propio se usa para lo ajeno en el resumen | G-T2 | "la codificacion multiventana sirve para quitar el artefacto" | PAT-14 |
| Termino clinico homonimo de uno tecnico, sin glosa | G-T2 | "error medio de reduccion de 2.56 mm" (fractura, no artefacto) | PAT-14 |
| Salvedad de no evaluacion omitida para una parte del aporte | P-EA3 | "Ningun objetivo aisla la geometria ... ni la codificacion" (falta la banda) | PAT-69 |
| Origen del umbral de fallo de un objetivo ausente del estado del arte | G-B9 | 25 HU anclado en RMSE de Karageorgos y Yun solo en el cap. 3 | PAT-84 |
| Enumeracion de orden que no sigue el orden de los parrafos | G-T5 | "las series clinicas, la colocacion de mascaras de lesion" | PAT-71 |
| Celda de la fila propia con hechos que el cuerpo no dice | G-B8 | "Poses preinscritas alrededor del corredor medido" | PAT-67 |
| Generalizacion sobre las fuentes contradicha por una fuente del mismo parrafo | G-B7 | "Cuando el metal es clinico, las fuentes lo segmentan con umbral" | nuevo |
| Resultado propio anunciado en otro capitulo cuyo diseno no describe la medicion | G-T1 | "se midio en los experimentos del Objetivo 1 ... se presenta en resultados" | nuevo |
