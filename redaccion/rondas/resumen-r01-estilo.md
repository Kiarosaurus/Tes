# Revisión de estilo — resumen — r01

## Hallazgos
| ID | Sev | Criterio | Ubicación | Texto actual (máx. 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-01 | media | E-T1, E-R5 | `overleaf/main.tex:86` | "difusión multiventana en el dominio de imagen" | Patrón PAT-56 reincide: el título da un nombre nuevo a la codificación multiventana. Propuesta: "Síntesis condicionada de tornillos transilíaco-transsacros y de su artefacto metálico local en TC pélvica mediante difusión con codificación multiventana en el dominio de imagen". |
| ES-02 | media | E-M8 | `overleaf/secciones/resumen.tex:5` | "esa escasez motiva sintetizar implantes como aumento de datos" | "Los artefactos de implantes metálicos pueden ocultar los límites del hueso en la tomografía computarizada pélvica. La escasez de volúmenes con implantes y anotación ósea motiva usar la síntesis del implante y de su artefacto como aumento de datos." |
| ES-03 | media | E-T1, E-R5 | `overleaf/secciones/resumen.tex:7` | "valores codificados en varias ventanas de unidades Hounsfield" | "El sintetizador usa un modelo de difusión en el dominio de imagen con codificación multiventana de los valores en unidades Hounsfield; regenera solo el implante y una banda de unos 12~mm a su alrededor." |
| ES-04 | media | E-M4, E-M8, E-P3 | `overleaf/secciones/resumen.tex:7` | "Su apariencia se comparó por equivalencia con un protocolo publicado de simulación física" | Patrón PAT-34 reincide: "Su" remite gramaticalmente al sintetizador, y "apariencia" amplía a todo el aspecto visual una comparación basada en una métrica. Propuesta: "La \emph{streak amplitude} del artefacto sintetizado se comparó por equivalencia con el protocolo físico; la inserción por copia y pegado, que no genera artefacto, sirvió como control." |
| ES-05 | baja | E-M8 | `overleaf/secciones/resumen.tex:9` | "la mejor dio 61.72" | "El menor error absoluto medio fue de 61.72 unidades Hounsfield." |
| ES-06 | media | E-P3, E-R5 | `overleaf/secciones/resumen.tex:11` | "la equivalencia de la apariencia con el protocolo físico no se estableció" | "La equivalencia de la \emph{streak amplitude} con la del protocolo físico no se estableció." |
| ES-07 | media | E-M8 | `overleaf/secciones/resumen.tex:11` | "decidió no rediseñar el sintetizador, cuyo perfil no reproduce la caída" | "El realismo visual del artefacto sintético no se reclama, porque la autora lo juzgó insuficiente. A partir de ese juicio, la autora y su asesor decidieron no rediseñar el sintetizador; el perfil por anillos de la salida no reproduce la caída de la amplitud con la distancia al metal." |

TOTAL alta=0 media=6 baja=1

## Impresión general
Leído de corrido, el resumen mantiene un registro sobrio y separa con claridad el alcance, los resultados negativos y lo no medido. La principal pérdida de precisión ocurre cuando la métrica \emph{streak amplitude} pasa a llamarse "apariencia", y cuando la codificación multiventana recibe formulaciones distintas. No se detecta informalidad ni un patrón general de prosa inflada.

## Patrones
| Patrón (una línea, generalizable a otras secciones) | Criterio | Ejemplo antes (máx. 15 palabras) | Ya en bitácora (PAT-n o "nuevo") |
|---|---|---|---|
| Un término fijo recibe un nombre nuevo o una paráfrasis en pasajes de síntesis | E-T1, E-R5 | "difusión multiventana" | PAT-56 |
| Una métrica de apariencia local se generaliza como si evaluara toda la apariencia | E-P3, E-R5 | "Su apariencia se comparó por equivalencia" | nuevo |
| Un posesivo retoma un antecedente gramatical distinto del objeto medido | E-M4, E-M8 | "Su apariencia se comparó" | PAT-34 |
