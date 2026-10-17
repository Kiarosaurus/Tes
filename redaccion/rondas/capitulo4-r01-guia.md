# Revision guia CS — capitulo4 — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C10 | capitulo4.tex:14, :92 | Las secciones de los Objetivos~1 y~3 abren con la interpretación («veredicto negativo» y «desenlace no concluyente») antes de presentar las tablas y los datos que la sostienen. El orden contradice la regla del bloque de mostrar datos primero e interpretarlos después, aunque tras las tablas sí haya discusión separada. | Abrir cada sección con la población, la medida y la tabla; trasladar el veredicto del Objetivo~1 y la categoría del contraste primario al párrafo inmediatamente posterior a sus respectivas tablas. |
| guia-2 | media | G-C11 | capitulo4.tex:145, :181 | Las tablas del perfil por anillos y de reconstrucción de implantes reales reportan medianas entre pacientes sin una medida de variabilidad para cada resultado. En la primera solo la razón final tiene percentiles; en la segunda ninguna mediana de los grupos de 9 y 4 pacientes tiene dispersión. | Añadir una medida de dispersión por resultado y grupo (por ejemplo, percentiles 25 y 75) o, si no puede resumirse, remitir al resultado por paciente y declarar explícitamente la limitación. |

TOTAL alta=0 media=2 baja=0

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple: el capítulo identifica cohortes, condiciones, métricas y remite al diseño; la dispersión incompleta se recoge en guia-2 |
| G-T2 | cumple |
| G-T3 | cumple: conserva $G$, $M$, $B_{\delta}$, $\Delta$ y la notación de los capítulos anteriores |
| G-T4 | cumple: la respuesta de r00 deja la fuente de cada cifra; la comprobación material de esas fuentes corresponde al auditor de trazabilidad |
| G-T5 | no evaluable: `conclusiones.tex` y `trabajosFuturos.tex`, que siguen al capítulo, todavía contienen texto de plantilla |
| G-T6 | cumple: `guo2025maisi`, `zwingmann2009navigated` y `lakens2017equivalence` están en `refs.bib` |
| G-C10 | no cumple (guia-1) |
| G-C11 | no cumple (guia-2) |
| G-C12 | cumple: explicita supuestos y limitaciones y valida cuantitativamente frente al protocolo físico, sin reclamar realismo visual |
| P-RE1 | cumple: cubre el objetivo general y los cuatro objetivos específicos; el Objetivo~4 se integra con SAP y las métricas de apariencia |
| P-RE2 | cumple: incluye resultados negativos de la compuerta, corredores estrechos, contraste no concluyente y objetos fuera de distribución, además de los casos favorables |
| P-RE3 | cumple: la discusión se organiza por Objetivo~1, Objetivos~2 y~4, Objetivo~3 y limitaciones |

## Propuestas de criterio

Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una sección de resultados anuncia el veredicto antes de mostrar los datos que lo sostienen | G-C10 | «La compuerta del Objetivo~1 dio un veredicto negativo» | nuevo |
| Una tabla resume varios pacientes con medianas, pero omite su dispersión | G-C11 | «medianas entre pacientes de prueba con metal» | nuevo |
