# Revision guia CS — capitulo2 — r02

Leido: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md`, `capitulo2-r01-guia.md`,
`capitulo2-r01-respuesta.md`, `overleaf/secciones/capitulo2.tex` (entero), `introduccion.tex` (entero),
`capitulo3.tex` (ll. 36-43 y 170-227) y `capitulo1.tex` (esqueleto) para G-B10, G-T3 y G-T5. Para el
hallazgo guia-1 se cotejo la ficha `docs/literatura/liu2025pipeline.md` (pto 4) y para guia-5 la ficha
`herman2016.md`. El RECHAZO de r01 (alinear la enumeracion de enfoques con el orden de secciones, guia-6
parcial) no se reabre: la BITACORA §2 fija que la brecha repite las palabras de la introduccion.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-B7 | capitulo2.tex:54, :68, :107 (contra :50) | La limitacion concreta de Liu et al. frente al Obj 2 esta mal enunciada. Cuerpo: "no se aplica a fracturas de sacro"; carencias y tabla: "no cubre el sacro". La ficha (pto 4) dice lo que importa: sus tornillos **no son iliosacros** (ilion, pubis, acetabulo) y la mencion de iliosacros es NO ENCONTRADO. En una seccion titulada "tornillos iliosacros", el lector supone que Liu planifica ese tornillo. | Decir en l. 54 que los tornillos que planifica no son iliosacros y que el metodo no se aplica a fracturas de sacro; usar la misma formulacion en l. 68 y en la celda de l. 107. |
| guia-2 | media | G-B7 | capitulo2.tex:44 (contra :44, :68) | Patron PAT-66 reincide. La l. 44 da como problema abierto "colocarlo ... con una restriccion anatomica", pero el mismo parrafo presenta dos trabajos que ya colocan con restriccion anatomica: el solape con una region de mas de 200 HU (Karageorgos) y el centro de una estructura segmentada (Wang 2019). La l. 68 resume la carencia de otra forma (distribucion comparada con una clinica medida). Se ataca un vacio que las fuentes citadas llenan en parte. | Enunciar en l. 44 la carencia con la formulacion de la l. 68 (restriccion por el corredor quirurgico y distribucion comparable con la clinica), o decir que restriccion falta en esas reglas. |
| guia-3 | media | G-B7, P-EA3 | capitulo2.tex:122 (contra :120) | La oracion tematica anuncia que la geometria parametrica "se distingue" de las formas de las fuentes, pero el parrafo solo las enumera y no dice en que se distingue. La mascara tubular de Wang et al. 2019 es tambien una geometria regular definida por el disenador. El resto del parrafo contrasta con el umbral de metodos de MAR, que no colocan metal (riesgo PAT-68). | Decir, con lo que den las fichas, que rasgo del tornillo parametrico no tiene ninguna forma listada (p. ej., que modela un implante de osteosintesis con su calibre en una pose muestreada), o acotar el primer elemento y remitir al `\GAPDEC` de la l. 124. |
| guia-4 | media | G-T4 | capitulo2.tex:38, :74 (contra capitulo3.tex:42) | Patron PAT-69 reincide. "El subconjunto CLINIC-metal de CTPelvic1K, el mismo que usa este trabajo" pierde dos salvedades del cap. 3: la correspondencia de la carpeta local con CLINIC-metal se **infiere** (no esta declarada), y la cohorte local tiene 178 volumenes, 103 de ellos atribuidos a CLINIC y no a CLINIC-metal. Leido solo, afirma que la cohorte es CLINIC-metal. | "el subconjunto CLINIC-metal de CTPelvic1K, al que corresponde por inferencia una de las dos carpetas locales (Seccion `sec:datos`)", o formula equivalente, en ambas lineas. |
| guia-5 | media | G-B9, G-T4 | capitulo2.tex:62 (contra capitulo3.tex:196) | "Este trabajo lee ese dato como cota del rango de colocaciones que el muestreador debe poder producir" atribuye a Herman et al. un uso en el diseno que el cap. 3 no tiene (no cita a Herman). Ademas el cap. 3 califica con grado 3 las poses que no atraviesan hueso en lugar de descartarlas: el muestreador si produce poses fuera del hueso. No se sabe si la "cota" es un limite superior ni que parte del metodo la respeta. | Decir que implica el dato para el Obj 2 de modo compatible con `sec:sap` (p. ej., como dato de la referencia que las poses fuera del hueso no tienen), o quitar la lectura; si es un criterio de diseno pendiente, `\GAPDEC`. |
| guia-6 | media | P-EA3 | capitulo2.tex:120, :76 (contra introduccion.tex:46, :60; capitulo3.tex:172) | Patron PAT-69 reincide. El tercer elemento del aporte ("uso de la codificacion multiventana para generar") omite la salvedad de la introduccion: el error de ida y vuelta de la codificacion sin autoencoder no lo verifica ningun objetivo y la codificacion no esta congelada (`\GAPDEC` en intro l. 46 y cap. 3 l. 172). La l. 76 dice "codificacion de entrada y de salida", la introduccion (l. 60) "de la entrada". | Anadir la salvedad en una oracion con el mismo `\GAPDEC` (BITACORA §2, GAP replicados); unificar "entrada y salida" con la introduccion (el cap. 3 respalda "entradas y salidas", asi que es la introduccion la que debe alinearse). |
| guia-7 | baja | G-B10 | capitulo2.tex:118 (contra introduccion.tex:54) | La brecha repite la tension de la introduccion, pero la oracion del protocolo fisico omite sus condiciones ("en un subconjunto de pacientes y segun el plazo"), que la introduccion si da (BITACORA §2, introduccion-r04). | Anadir las dos condiciones. |
| guia-8 | baja | G-B8, G-T1 | capitulo2.tex:106 (contra :36) | Patron PAT-67 reincide. La celda de Karageorgos "Similitud y error frente a la imagen sin metal": el cuerpo da el SSIM y las 13 de 28 metricas, pero ninguna medida de error. | Dar en l. 36 la medida de error de la ficha o quitar "y error" de la celda. |
| guia-9 | baja | G-T2 | capitulo2.tex:62, :38 | Patron PAT-3 reincide: "S2" (Herman) y la sigla "AAPM" se usan sin definir; S1 esta definido en la introduccion, S2 no. BITACORA §2 reserva evitar "S2" para el segundo corredor, y aqui designa el nivel sacro. | "el segundo segmento sacro (S2)" en su primera aparicion; expandir AAPM o nombrar el desafio sin la sigla. |
| guia-10 | baja | P-EA2 | capitulo2.tex:64 | Kaiser et al. es fuente principal del Obj 2 (marco y holgura radial), pero no se da ningun resultado de los autores, solo que definen un marco calculable. | Una cifra o resultado de la ficha, con su condicion, o remitir a `sec:corredor` si alli se dan. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple (salvo guia-8, baja) |
| G-T2 | no cumple (guia-9, baja); "brecha cortical" ya unica (PAT-14 no reincide) |
| G-T3 | cumple ($G$, $M$, $B_{\delta}$, $p$ iguales que en introduccion y capitulo3) |
| G-T4 | no cumple (guia-4, guia-5); resto cumple con GAP (`\GAPDATO` de Li et al.; cotejo cifra a cifra es del auditor) |
| G-T5 | cumple (l. 10 describe el orden real; hacia `capitulo3` l. 126); desde `capitulo1`: no evaluable (esqueleto) |
| G-T6 | cumple (lint PASA) |
| G-B5 | cumple (Obj 1 l. 78, Obj 2 l. 68, Obj 3 l. 30, Obj 4 l. 66) |
| G-B6 | cumple con GAP (`\GAPDEC` del protocolo de busqueda, l. 12) |
| G-B7 | no cumple (guia-1, guia-2, guia-3) |
| G-B8 | cumple, con mejora (guia-8); fila propia presente y marcada como diseno con `\GAPDATO` |
| G-B9 | cumple salvo guia-5 |
| G-B10 | cumple con GAP (l. 118 = introduccion.tex:54 con el mismo `\GAPDEC`; guia-7 baja; Formulacion de la introduccion desfasada con `\GAPDEC` propio) |
| P-EA1 | cumple (las dos entradas `@misc` arXiv, Wu 2025 y Chen 2026, senaladas como prepublicacion; fuente de solo resumen senalada) |
| P-EA2 | cumple (Karageorgos y Yun con resultados); mejora en guia-10 |
| P-EA3 | cumple a medias (guia-3, guia-6); reclamo de novedad con `\GAPDEC` (#56) |

Patrones VIGENTES de mi dominio comprobados: PAT-3 (reincide, guia-9), PAT-14 (no reincide), PAT-31 (no
reincide en cifras), PAT-36 (no reincide: "solo las series clinicas" abarca Zwingmann 2010 y Herman),
PAT-49 (no reincide, l. 120), PAT-57 (no reincide), PAT-61 (no aplica: sin resultados propios), PAT-65
(cotejo del auditor), PAT-66 (reincide, guia-2), PAT-67 (reincide, guia-8), PAT-68 (riesgo en guia-3),
PAT-69 (reincide, guia-4 y guia-6), PAT-70 (erradicado en esta seccion: Obj 4 comparado en l. 66), PAT-71
(no reincide, l. 10). Los de criterio E-* quedan para `revisor-estilo`.

## Propuestas de criterio
- Que en el estado del arte la limitacion atribuida a un trabajo sea la que su ficha da como mas pertinente
  al objetivo, no una derivada (aqui "no cubre el sacro" frente a "no planifica tornillos iliosacros").
  Hoy cae bajo G-B7 sin precision.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| La misma carencia se resume distinto en dos lugares del capitulo | G-B7 | "colocarlo con una restriccion anatomica" / "distribucion ... con una distribucion clinica medida" | PAT-66 |
| Salvedad dada en otro capitulo omitida al repetir el hecho | P-EA3, G-T4 | "CLINIC-metal ..., el mismo que usa este trabajo" (correspondencia inferida) | PAT-69 |
| Celda de tabla con un hecho que el cuerpo no presenta | G-B8 | "Similitud y error frente a la imagen sin metal" | PAT-67 |
| Termino usado antes de su definicion | G-T2 | "el 14.8 % en S2" | PAT-3 |
| Lectura propia de una fuente le asigna al diseno un uso que el capitulo de metodo no tiene o contradice | G-B9, G-T4 | "lee ese dato como cota del rango ... que el muestreador debe poder producir" | nuevo |
| Limitacion de una solucion concreta resumida en forma distinta y mas debil que la que da su ficha | G-B7 | "no cubre el sacro" (ficha: sus tornillos no son iliosacros) | nuevo |
