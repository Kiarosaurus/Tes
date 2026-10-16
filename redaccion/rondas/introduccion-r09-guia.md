# Revision guia CS — introduccion — r09

Encargo: `redaccion/ENCARGO_2026-10-15c.md` (introduccion: GAPDATO de la sensibilidad del Obj 2 -> e15; alinear el
desenlace con cap. 1 y 3). Fuentes cotejadas: `experiments/objetivo2/e15_w1_sensibilidad.md`,
`experiments/registro/registro_metodos_2026-10-15.md` §7-§9, DEC 2026-10-15 (4), implicancia #195,
`capitulo1.tex` :128-132, `capitulo3.tex` :218, :228, :417-427. Encabezado (l. 3-17) y Formulacion (l. 21) bajo #126:
no se reportan (E-O1 y "robustos" de l. 7 siguen ESCALADOS). Respuesta r08: sin hallazgos RECHAZADOS que reabrir.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-A10, G-T4 | introduccion.tex:94 | Patron PAT-122 reincide: el `\GAPDATO` de la sensibilidad del Obj 2 sin los dos casos fallidos sigue declarando ausente un resultado que e15 ya calculo (registro §8; DEC 2026-10-15 (4) pto 4). Es el cierre que pide el encargo. | Retirar la marca y dar la sensibilidad con su condicion (70 casos, descriptiva y posterior): W1 0.203 y 0.237 frente a 0.206 y 0.230 de la cohorte primaria (navegada / convencional), con remision a `sec:corredor` o a la seccion del cap. 3 que la reporte. Las dos parejas de cifras, sin calcular diferencias (PAT-172) |
| guia-2 | media | G-T4 | introduccion.tex:102 | Patron PAT-168 reincide: la prosa del tercer desplazamiento ("razon entre tipos de parche, medida antes de los ultimos retiros") repite el hueco que el registro §7 cierra para el modelo evaluado (0.638; 0.620 antes de los retiros). Quedara desalineada con el cap. 3 cuando capitulo3-r26 cierre su `\GAPDATO` de :218 y la oracion de :228. | Decir que la razon se midio en el conjunto de entrenamiento del modelo evaluado, sin "antes de los ultimos retiros"; cifra solo si el cap. 3 r26 la da en el mismo lugar (cotejar la redaccion final de cap3 :228) |
| guia-3 | media | G-A10 | introduccion.tex:50 | El margen se presenta solo por su efecto ("un sintetizador mas variable obtiene un margen mas ancho"); falta el limite que #195 (DECIDIDA, opcion a) manda declarar: $\Delta$ es una convencion del estudio basada en la variabilidad propia de los metodos, no una diferencia aceptable para un uso. Sin eso, la hipotesis que el Obj 3 podia rechazar (l. 52) parece de equivalencia en sentido practico. | Una clausula en l. 50: el margen es una convencion de este trabajo, la variabilidad entre semillas y entre replicas, y no una diferencia clinicamente aceptable, con remision a `sec:ap-analisis`/`sec:amenazas`. Sin `haber2008general` ni el detalle de `max(s, r)` (son del cap. 3) |
| guia-4 | baja | G-A8 | introduccion.tex:48 | La lectura del Obj 2 "contra la distancia entre las dos series" no dice que el intervalo por remuestreo de pacientes (e15) solapa para las dos series, de modo que la cohorte no distingue cual esta mas cerca; es lo que esa lectura puede concluir. | Opcional: media oracion con el hecho (intervalos solapados, descriptivo y posterior) y remision al cap. 3; sin los extremos de los intervalos si el parrafo crece (PAT-58) |

TOTAL alta=0 media=3 baja=1

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | cumple (piso de ruido sin definir: decision BITACORA §2 2026-10-15, no se reporta) |
| G-T3 | cumple ($\Delta$, $G$, $M$, $B_\delta$ iguales a cap. 1 y 3) |
| G-T4 | no cumple (guia-1, guia-2) |
| G-T5 | cumple |
| G-T6 | cumple |
| G-A1 | cumple (problema l. 3-7 y 58; revision l. 60-64; proposito l. 13 y objetivo general; pregunta l. 21) |
| G-A2 | cumple |
| G-A3 | cumple (l. 64, formula fija de la brecha) |
| G-A4 | cumple |
| G-A5 | cumple |
| G-A6 | cumple |
| G-A7 | cumple |
| G-A8 | cumple a medias en el Obj 2 (sin regla, declarado en l. 48; guia-4 baja); Obj 1 y Obj 3 cumplen |
| G-A9 | cumple (encabezado bajo #126) |
| G-A10 | no cumple (guia-1, guia-3) |
| G-B10 (cruce con cap. 2) | cumple: l. 64 coincide con la brecha fija de capitulo2-r08 |
| G-C4 (cruce con cap. 3) | cumple: tres desenlaces de l. 50 = cap1:130 y cap3:419; direccion a la baja coherente con IC95 que excluye 0 (#194) |
| G-D1, G-D2 | no evaluable (conclusiones aun no cerradas) |

## Propuestas de criterio
(ninguna)

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP de resultado propio que sigue en pie tras calcularse el dato en un registro nuevo | G-T4, OC-2 | "\GAPDATO{analisis de sensibilidad del Objetivo 2 sin los dos casos ...}" | PAT-122 |
| Prosa fuera de la marca que repite el hueco cerrado en otro capitulo | G-T4 | "la razon entre tipos de parche, medida antes de los ultimos retiros" | PAT-168 |
| Implicancia DECIDIDA que pide declarar un limite se aplica en el metodo y no en la introduccion que resume la misma regla | G-A10, OC-3 | "Ese margen lo fija la variabilidad entre semillas del propio sintetizador" | nuevo (afin a PAT-184) |
