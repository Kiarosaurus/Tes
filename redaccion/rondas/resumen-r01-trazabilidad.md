# Auditoría de trazabilidad — resumen — r01

## Hallazgos
| ID | Sev | Criterio | Ubicación | Afirmación (max 15 palabras) | Fuente buscada | Problema | Corrección |
|---|---|---|---|---|---|---|---|
| T01 | baja | G-T4 | `overleaf/secciones/resumen.tex:9` | «la mejor dio 61.72» | `experiments/objetivo1/p1_compuerta.md:18-25`; `docs/00-tesis.md:55-61` | La cifra coincide exactamente, pero pierde la unidad HU; el antecedente permite inferirla, aunque queda menos precisa que la fuente. | Escribir «la mejor dio 61.72 unidades Hounsfield». |

## Inventario
| Ubicación | Unidad verificable | Fuente (ruta:línea o clave + fila de evidencia) | OK |
|---|---|---|---|
| `overleaf/secciones/resumen.tex:5` | Hay pocos volúmenes anotados con metal en TC pélvica. | `docs/literatura/liu2021ctpelvic1k.md:18,32-35` (75 con metal; 14 anotados; 61 sin anotar) | sí |
| `overleaf/secciones/resumen.tex:5` | Los artefactos metálicos pueden ocultar límites anatómicos. | `docs/literatura/selles2024marreview.md:71-73` (Evidencia textual: rayas que ocultan estructuras anatómicas) | sí |
| `overleaf/secciones/resumen.tex:5` | La escasez motiva sintetizar implantes como aumento de datos. | `overleaf/secciones/introduccion.tex:60`; `docs/00-tesis.md:247-251` | sí |
| `overleaf/secciones/resumen.tex:5` | La utilidad del aumento presupone plausibilidad; esta tesis evalúa primero coherencia. | `overleaf/secciones/introduccion.tex:11,60`; `docs/00-tesis.md:26-31` | sí |
| `overleaf/secciones/resumen.tex:5` | Ningún enfoque revisado reúne distribución de poses y apariencia del artefacto. | `overleaf/secciones/capitulo2.tex:114-116`; `overleaf/secciones/introduccion.tex:62-66` | sí |
| `overleaf/secciones/resumen.tex:5` | La cadena inserta un tornillo transilíaco-transsacro y su artefacto local. | `docs/00-tesis.md:7-16,80-82,114-120` | sí |
| `overleaf/secciones/resumen.tex:5` | La cadena opera sobre TC pélvica receptora sin implante/osteosíntesis de CTPelvic1K. | `overleaf/secciones/capitulo3.tex:15,21`; `docs/00-tesis.md:195-205`; `docs/literatura/liu2021ctpelvic1k.md:12,30` | sí |
| `overleaf/secciones/resumen.tex:5` | Se evaluó la coherencia quirúrgica y física, no la utilidad downstream. | `docs/00-tesis.md:26-31,247-251` | sí |
| `overleaf/secciones/resumen.tex:7` | La compuerta es previa a la cadena. | `docs/00-tesis.md:53-61,121-122`; `overleaf/secciones/capitulo3.tex:20` | sí |
| `overleaf/secciones/resumen.tex:7` | El criterio examina MAE óseo menor que 25 HU en un autoencoder latente. | `experiments/objetivo1/p1_compuerta.md:1-5`; `docs/00-tesis.md:55-61` | sí |
| `overleaf/secciones/resumen.tex:7` | El criterio estaba fijado antes de la prueba decisiva. | `docs/00-tesis.md:55-61,121-125`; `overleaf/secciones/introduccion.tex:50` | sí |
| `overleaf/secciones/resumen.tex:7` | El muestreador propone poses tridimensionales alrededor del corredor medido por volumen. | `experiments/objetivo2/preinscripcion_muestreador.md:25-43,45-71` | sí |
| `overleaf/secciones/resumen.tex:7` | El grado de brecha representa cuánto sobresale el tornillo del hueso. | `experiments/objetivo2/preinscripcion_muestreador.md:83-98`; `docs/literatura/zwingmann2009navigated.md:68-75` | sí |
| `overleaf/secciones/resumen.tex:7` | La distribución se compara con dos series clínicas publicadas. | `experiments/objetivo2/preinscripcion_muestreador.md:100-106`; `docs/literatura/zwingmann2009navigated.md:74-78` | sí |
| `overleaf/secciones/resumen.tex:7` | El sintetizador es difusión en dominio de imagen con codificación multiventana. | `docs/00-tesis.md:114-120`; `docs/01-decisiones.md:2829-2837` | sí |
| `overleaf/secciones/resumen.tex:7` | Genera solo el implante y una banda de unos 12 mm. | `docs/00-tesis.md:114-120,195-205` | sí |
| `overleaf/secciones/resumen.tex:7` | La apariencia se compara por equivalencia con el protocolo físico publicado. | `docs/00-tesis.md:168-179,195-205`; `experiments/objetivo3/resultados_prueba_v1.md:10-20` | sí |
| `overleaf/secciones/resumen.tex:7` | Copia y pegado es control y no genera artefacto. | `experiments/objetivo3/resultados_prueba_v1.md:23-26`; `docs/00-tesis.md:170-176,203-205` | sí |
| `overleaf/secciones/resumen.tex:9` | La compuerta dio veredicto negativo y motivó el dominio de imagen. | `experiments/objetivo1/p1_compuerta.md:16-27`; `docs/00-tesis.md:55-61,114-122` | sí |
| `overleaf/secciones/resumen.tex:9` | Se evaluaron seis combinaciones sobre 34 pacientes. | `experiments/objetivo1/p1_compuerta.md:3-5,18-25` | sí |
| `overleaf/secciones/resumen.tex:9` | Ninguna combinación bajó de 25 HU. | `experiments/objetivo1/p1_compuerta.md:18-27` | sí |
| `overleaf/secciones/resumen.tex:9` | La mejor combinación dio 61.72. | `experiments/objetivo1/p1_compuerta.md:18-25`; `docs/00-tesis.md:55-58` | no: T01 |
| `overleaf/secciones/resumen.tex:9` | Se calificaron 3 600 poses en 72 pacientes. | `experiments/objetivo2/e13_sap.md:7-12,40-46`; `docs/00-tesis.md:74-79` | sí |
| `overleaf/secciones/resumen.tex:9` | Wasserstein-1 fue 0.206 grados frente a la serie navegada. | `experiments/objetivo2/e13_sap.md:40-50` | sí |
| `overleaf/secciones/resumen.tex:9` | Wasserstein-1 fue 0.230 grados frente a la serie convencional. | `experiments/objetivo2/e13_sap.md:40-50` | sí |
| `overleaf/secciones/resumen.tex:9` | Las dos series clínicas están separadas por 0.395 grados. | `docs/00-tesis.md:83-86`; `overleaf/secciones/capitulo4.tex:62-65,76,80` | sí |
| `overleaf/secciones/resumen.tex:9` | Las dos distancias del muestreador son menores que 0.395 grados. | `experiments/objetivo2/e13_sap.md:44-50`; `docs/00-tesis.md:83-86` | sí |
| `overleaf/secciones/resumen.tex:9` | El Objetivo 2 carece de regla de decisión; la lectura es descriptiva. | `docs/00-tesis.md:83-86`; `overleaf/secciones/capitulo4.tex:80-82` | sí |
| `overleaf/secciones/resumen.tex:9` | Los intervalos por remuestreo no ordenan las series por cercanía. | `experiments/objetivo2/e15_w1_sensibilidad.md:1-12`; `overleaf/secciones/capitulo4.tex:82` | sí |
| `overleaf/secciones/resumen.tex:9` | El contraste primario usa 13 pacientes de prueba sin metal. | `experiments/objetivo3/resultados_prueba_v1.md:10-14`; `docs/00-tesis.md:195-205` | sí |
| `overleaf/secciones/resumen.tex:9` | La diferencia media pareada fue −301.0 HU. | `experiments/objetivo3/resultados_prueba_v1.md:12-15` | sí |
| `overleaf/secciones/resumen.tex:9` | El IC del 90 % fue [−477.0, −124.9] HU. | `experiments/objetivo3/resultados_prueba_v1.md:12-15` | sí |
| `overleaf/secciones/resumen.tex:9` | El margen de equivalencia fue 196.3 HU. | `experiments/objetivo3/resultados_prueba_v1.md:12-17,34-37`; `docs/00-tesis.md:168-176` | sí |
| `overleaf/secciones/resumen.tex:9` | El IC cruza el límite inferior del margen. | `experiments/objetivo3/resultados_prueba_v1.md:28-39`; `docs/00-tesis.md:170-176` | sí |
| `overleaf/secciones/resumen.tex:9` | El desenlace es no concluyente y la amplitud sintética es menor. | `experiments/objetivo3/resultados_prueba_v1.md:28-39`; `docs/01-decisiones.md:2658-2661` | sí |
| `overleaf/secciones/resumen.tex:9` | Wilcoxon dio p = 0.000122 frente a copia y pegado. | `experiments/objetivo3/resultados_prueba_v1.md:23-26`; `docs/00-tesis.md:170-176` | sí |
| `overleaf/secciones/resumen.tex:9` | Superar copia y pegado no cuenta a favor del sintetizador. | `experiments/objetivo3/resultados_prueba_v1.md:23-26`; `docs/00-tesis.md:203-205` | sí |
| `overleaf/secciones/resumen.tex:11` | La distribución queda más cerca de cada serie que ellas entre sí. | `experiments/objetivo2/e13_sap.md:40-50`; `docs/00-tesis.md:83-86` | sí |
| `overleaf/secciones/resumen.tex:11` | La equivalencia con el protocolo físico no se estableció. | `experiments/objetivo3/resultados_prueba_v1.md:12-20,28-39`; `docs/01-decisiones.md:2658-2661` | sí |
| `overleaf/secciones/resumen.tex:11` | El realismo visual no se reclama; la autora lo juzgó insuficiente. | `docs/04-implicancias.md:12446-12452`; `docs/01-decisiones.md:2717-2734` | sí |
| `overleaf/secciones/resumen.tex:11` | La autora y su asesor decidieron no rediseñar el sintetizador. | `docs/01-decisiones.md:2717-2728` | sí |
| `overleaf/secciones/resumen.tex:11` | El perfil no reproduce la caída de amplitud con la distancia. | `experiments/objetivo3/outputs/a29/a29_perfil.md:3-22`; `docs/00-tesis.md:211-220` | sí |
| `overleaf/secciones/resumen.tex:11` | La evaluación de segmentación ósea quedó fuera de alcance. | `docs/00-tesis.md:243-251`; `docs/01-decisiones.md:2832-2837` | sí |
| `overleaf/secciones/resumen.tex:11` | Ningún resultado mide utilidad para entrenar una red. | `docs/00-tesis.md:243-251`; `overleaf/secciones/conclusiones.tex:38` | sí |

TOTAL alta=0 media=0 baja=1

## Patrones
sin patrones
