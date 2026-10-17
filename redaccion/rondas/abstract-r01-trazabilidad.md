# Auditoria de trazabilidad — abstract — r01

Archivo auditado: `overleaf/secciones/abstract.tex` (19 lineas). Fuente directa fijada por el encargo: traduccion fiel de `overleaf/secciones/resumen.tex` r01, cotejada oracion por oracion con `abstract-r00-respuesta.md`. Lint r01: PASA, sin hallazgos ni marcas GAP. Respuesta previa: `abstract-r00-respuesta.md`; no contiene rechazos que deban reabrirse. Encargo: `redaccion/ENCARGO_2026-10-16.md`. No se abrio ningun PDF.

El titulo coincide con el titulo ingles final de DEC 2026-10-16 (7), punto 6, sin el prefijo del proyecto. El cuerpo conserva las 3/4/6/3 oraciones, las cifras, signos, unidades, poblaciones y cautelas del resumen r01. No contiene citas IEEE ni claves bibliograficas que auditar; su ausencia cumple P-R2. No aparecen `\GAPLIT`, `\GAPDATO`, `\GAPDEC`, `\REVVISUAL`, el rango retirado 31--60 %, BFC, ISC, Dice ni HD95. La difusion latente se menciona solo en la compuerta que la descarto; el metodo vigente se presenta como difusion en el dominio de imagen. La evaluacion downstream se declara fuera de alcance y no se afirma realismo visual. Se comprobaron los patrones VIGENTES de trazabilidad de la Bitacora; ninguno reincide.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | Sin hallazgos. | — |

TOTAL alta=0 media=0 baja=0

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| `overleaf/secciones/abstract.tex:6` | Titulo: sintesis condicionada de tornillos transiliaco-transsacros y artefactos locales | `docs/01-decisiones.md:2823-2849`, punto 6; `docs/00-tesis.md:7-16` | si |
| `overleaf/secciones/abstract.tex:6` | Metodo del titulo: difusion en imagen con codificacion multiventana | `docs/01-decisiones.md:2845-2849`; `docs/00-tesis.md:7-12,114-120` | si |
| `overleaf/secciones/abstract.tex:9` | Los artefactos metalicos pueden ocultar limites del hueso | `overleaf/secciones/resumen.tex:5`; ficha `selles2024marreview`, Evidencia textual sobre ocultamiento anatomico | si |
| `overleaf/secciones/abstract.tex:9` | Escasean los volumenes con implante y anotacion osea | `overleaf/secciones/resumen.tex:5`; ficha `liu2021ctpelvic1k`, Evidencia textual sobre 75 casos con metal, 14 anotados y 61 sin anotar | si |
| `overleaf/secciones/abstract.tex:9` | Esa escasez motiva sintetizar implante y artefacto como aumento de datos | `overleaf/secciones/resumen.tex:5`; `overleaf/secciones/introduccion.tex:60`; `docs/00-tesis.md:247-251` | si |
| `overleaf/secciones/abstract.tex:9` | Medir utilidad presupone plausibilidad de lo sintetizado | `overleaf/secciones/resumen.tex:5`; `overleaf/secciones/introduccion.tex:60`; `docs/00-tesis.md:26-31` | si |
| `overleaf/secciones/abstract.tex:9` | Ningun enfoque revisado reune distribucion de poses y apariencia del artefacto | `overleaf/secciones/resumen.tex:5`; `overleaf/secciones/introduccion.tex:62-66`; `overleaf/secciones/capitulo2.tex:114-116` | si |
| `overleaf/secciones/abstract.tex:9` | La cadena inserta un tornillo transiliaco-transsacro y su artefacto local | `overleaf/secciones/resumen.tex:5`; `docs/00-tesis.md:7-16,80-82,114-120` | si |
| `overleaf/secciones/abstract.tex:9` | La cadena usa TC pelvica sin implante de CTPelvic1K | `overleaf/secciones/resumen.tex:5`; `overleaf/secciones/capitulo3.tex:15,21`; `docs/00-tesis.md:195-205` | si |
| `overleaf/secciones/abstract.tex:9` | CTPelvic1K es un conjunto publico | `overleaf/secciones/resumen.tex:5`; ficha `liu2021ctpelvic1k`, Identificacion y Evidencia textual | si |
| `overleaf/secciones/abstract.tex:9` | Se evaluo coherencia quirurgica y fisica | `overleaf/secciones/resumen.tex:5`; `docs/00-tesis.md:26-31` | si |
| `overleaf/secciones/abstract.tex:11` | La compuerta preliminar tenia criterio fijado de antemano | `overleaf/secciones/resumen.tex:7`; `docs/00-tesis.md:55-61,121-125`; `overleaf/secciones/introduccion.tex:50` | si |
| `overleaf/secciones/abstract.tex:11` | La compuerta examino el autoencoder de un modelo de difusion latente | `overleaf/secciones/resumen.tex:7`; `experiments/objetivo1/p1_compuerta.md:1-5`; `overleaf/secciones/introduccion.tex:37` | si |
| `overleaf/secciones/abstract.tex:11` | El autoencoder comprime y reconstruye la imagen | `overleaf/secciones/resumen.tex:7`; `overleaf/secciones/introduccion.tex:37` | si |
| `overleaf/secciones/abstract.tex:11` | Criterio: MAE oseo menor que 25 HU | `overleaf/secciones/resumen.tex:7`; `experiments/objetivo1/p1_compuerta.md:3-5`; `docs/00-tesis.md:55-58` | si |
| `overleaf/secciones/abstract.tex:11` | El muestreador propone poses tridimensionales en el corredor oseo | `overleaf/secciones/resumen.tex:7`; `experiments/objetivo2/preinscripcion_muestreador.md:25-71`; `overleaf/secciones/introduccion.tex:39` | si |
| `overleaf/secciones/abstract.tex:11` | SAP fue propuesta en este trabajo | `overleaf/secciones/resumen.tex:7`; `overleaf/secciones/introduccion.tex:43`; `overleaf/secciones/conclusiones.tex:22` | si |
| `overleaf/secciones/abstract.tex:11` | SAP califica por viabilidad del corredor y grado de brecha cortical | `overleaf/secciones/resumen.tex:7`; `overleaf/secciones/introduccion.tex:43`; `docs/00-tesis.md:83-86` | si |
| `overleaf/secciones/abstract.tex:11` | El grado de brecha depende de cuanto sobresale el tornillo del hueso | `overleaf/secciones/resumen.tex:7`; `experiments/objetivo2/preinscripcion_muestreador.md:83-98`; ficha `zwingmann2009navigated`, Evidencia textual sobre grados | si |
| `overleaf/secciones/abstract.tex:11` | Sintetizador: difusion en imagen con codificacion multiventana de HU | `overleaf/secciones/resumen.tex:7`; `docs/00-tesis.md:114-120`; `overleaf/secciones/introduccion.tex:41` | si |
| `overleaf/secciones/abstract.tex:11` | Regenera solo el implante y una banda de unos 12 mm | `overleaf/secciones/resumen.tex:7`; `docs/00-tesis.md:114-120`; `overleaf/secciones/introduccion.tex:41` | si |
| `overleaf/secciones/abstract.tex:11` | *Streak amplitude* mide rayas respecto de la imagen sin metal | `overleaf/secciones/resumen.tex:7`; `overleaf/secciones/capitulo3.tex:345` | si |
| `overleaf/secciones/abstract.tex:11` | Se comparo por equivalencia con un protocolo fisico publicado | `overleaf/secciones/resumen.tex:7`; `docs/00-tesis.md:168-179,195-205`; `experiments/objetivo3/resultados_prueba_v1.md:10-20` | si |
| `overleaf/secciones/abstract.tex:11` | Copia y pegado fue control y no produce artefacto | `overleaf/secciones/resumen.tex:7`; `experiments/objetivo3/resultados_prueba_v1.md:23-26`; `docs/00-tesis.md:203-205` | si |
| `overleaf/secciones/abstract.tex:13` | La compuerta dio veredicto negativo y motivo el dominio de imagen | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo1/p1_compuerta.md:16-27`; `docs/00-tesis.md:55-61,114-122` | si |
| `overleaf/secciones/abstract.tex:13` | Se evaluaron seis configuraciones en 34 pacientes de prueba | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo1/p1_compuerta.md:3-5,18-25` | si |
| `overleaf/secciones/abstract.tex:13` | Ninguna configuracion bajo de 25 HU | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo1/p1_compuerta.md:18-27` | si |
| `overleaf/secciones/abstract.tex:13` | La mejor configuracion dio 61.72 HU | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo1/p1_compuerta.md:18-25`; `docs/00-tesis.md:55-58` | si |
| `overleaf/secciones/abstract.tex:13` | SAP paso sus controles | `overleaf/secciones/resumen.tex:9`; `overleaf/secciones/conclusiones.tex:16,22`; `experiments/objetivo2/e13_sap.md:7-12` | si |
| `overleaf/secciones/abstract.tex:13` | Se calificaron 3 600 poses en 72 pacientes | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo2/e13_sap.md:7-12,40-46`; `docs/00-tesis.md:74-79` | si |
| `overleaf/secciones/abstract.tex:13` | W1 fue 0.206 grados frente a la serie navegada | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo2/e13_sap.md:40-50` | si |
| `overleaf/secciones/abstract.tex:13` | W1 fue 0.230 grados frente a la serie convencional | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo2/e13_sap.md:40-50` | si |
| `overleaf/secciones/abstract.tex:13` | Las series clinicas estan separadas por 0.395 grados | `overleaf/secciones/resumen.tex:9`; `docs/00-tesis.md:83-86`; `overleaf/secciones/capitulo4.tex:62-65,76,80` | si |
| `overleaf/secciones/abstract.tex:13` | 0.206 y 0.230 son menores que 0.395 | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo2/e13_sap.md:44-50`; `docs/00-tesis.md:83-86` | si |
| `overleaf/secciones/abstract.tex:13` | La lectura es descriptiva y el objetivo no tiene regla de decision | `overleaf/secciones/resumen.tex:9`; `docs/00-tesis.md:83-86`; `overleaf/secciones/conclusiones.tex:16` | si |
| `overleaf/secciones/abstract.tex:13` | Los intervalos por remuestreo no ordenan las series por cercania | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo2/e15_w1_sensibilidad.md:1-12`; `overleaf/secciones/capitulo4.tex:82` | si |
| `overleaf/secciones/abstract.tex:13` | El contraste primario uso 13 pacientes de prueba sin metal | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:10-14`; `docs/00-tesis.md:195-205` | si |
| `overleaf/secciones/abstract.tex:13` | Diferencia media pareada de *streak amplitude*: -301.0 HU | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:12-15` | si |
| `overleaf/secciones/abstract.tex:13` | IC del 90 %: [-477.0, -124.9] HU | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:12-15` | si |
| `overleaf/secciones/abstract.tex:13` | Margen de equivalencia: 196.3 HU | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:12-17,34-37`; `docs/00-tesis.md:168-176` | si |
| `overleaf/secciones/abstract.tex:13` | El IC cruza el limite inferior del margen | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:28-39`; `docs/00-tesis.md:170-176` | si |
| `overleaf/secciones/abstract.tex:13` | Desenlace no concluyente, con amplitud sintetica menor | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:28-39`; `docs/00-tesis.md:211-216` | si |
| `overleaf/secciones/abstract.tex:13` | Wilcoxon frente a copia y pegado dio p = 0.000122 | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:23-26`; `docs/00-tesis.md:170-176` | si |
| `overleaf/secciones/abstract.tex:13` | Superar copia y pegado es cordura y no favorece al sintetizador | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:23-26`; `docs/00-tesis.md:203-205` | si |
| `overleaf/secciones/abstract.tex:13` | Copia y pegado no produce rayas | `overleaf/secciones/resumen.tex:9`; `experiments/objetivo3/resultados_prueba_v1.md:23-26`; `overleaf/secciones/conclusiones.tex:20,24` | si |
| `overleaf/secciones/abstract.tex:15` | La distribucion queda mas cerca de cada serie que ellas entre si | `overleaf/secciones/resumen.tex:11`; `experiments/objetivo2/e13_sap.md:40-50`; `docs/00-tesis.md:83-86` | si |
| `overleaf/secciones/abstract.tex:15` | Esa lectura de cercania se declara descriptiva | `overleaf/secciones/resumen.tex:11`; `overleaf/secciones/conclusiones.tex:16,24` | si |
| `overleaf/secciones/abstract.tex:15` | No se establecio equivalencia con el protocolo fisico | `overleaf/secciones/resumen.tex:11`; `experiments/objetivo3/resultados_prueba_v1.md:12-20,28-39` | si |
| `overleaf/secciones/abstract.tex:15` | No se reclama realismo visual; la autora lo juzgo insuficiente | `overleaf/secciones/resumen.tex:11`; `docs/00-tesis.md:217-220`; `overleaf/secciones/conclusiones.tex:30` | si |
| `overleaf/secciones/abstract.tex:15` | Autora y asesor decidieron no redisenar el sintetizador | `overleaf/secciones/resumen.tex:11`; `docs/01-decisiones.md:2717-2728`; `docs/00-tesis.md:217-220` | si |
| `overleaf/secciones/abstract.tex:15` | La salida no reproduce la caida de amplitud con la distancia | `overleaf/secciones/resumen.tex:11`; `experiments/objetivo3/outputs/a29/a29_perfil.md:3-22`; `docs/00-tesis.md:211-220` | si |
| `overleaf/secciones/abstract.tex:15` | La evaluacion de segmentacion osea quedo fuera de alcance | `overleaf/secciones/resumen.tex:11`; `docs/00-tesis.md:243-251`; `docs/01-decisiones.md:2832-2837` | si |
| `overleaf/secciones/abstract.tex:15` | Ningun resultado mide utilidad para entrenar una red | `overleaf/secciones/resumen.tex:11`; `docs/00-tesis.md:243-251`; `overleaf/secciones/conclusiones.tex:38` | si |
| `overleaf/secciones/abstract.tex:18-19` | Las cinco palabras clave traducen las cinco del resumen | `overleaf/secciones/resumen.tex:14-15`; `abstract-r00-respuesta.md:30-32` | si |

## Patrones
sin patrones
