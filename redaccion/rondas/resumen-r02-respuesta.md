# Resumen r02 — corrección conjunta con el abstract

Modo: corrección única por pedido de la autora. Se revisaron `redaccion/ESTILO.md`, `redaccion/RUBRICA.md`, los reportes r01 y las secciones de introducción, resultados y conclusiones. No se convocaron revisores adicionales. El abstract se reescribió al mismo tiempo, oración por oración.

| Aspecto revisado | Decisión editorial | Trazabilidad interna |
|---|---|---|
| Problema y propósito (P-R1, G-R1) | Abrir con lo que el metal oculta en la imagen; presentar después la escasez de datos y la cadena propuesta. | `introduccion.tex`:3-15, 58-60. |
| Alcance de la cadena (G-T4, PAT-197) | Declarar que los dos componentes se evaluaron por separado; no atribuir a la prueba una síntesis sobre poses perturbadas del muestreador. | `introduccion.tex`:13-15, 41, 52; `conclusiones.tex`:6, 30. |
| Método (P-R1, G-R1) | Explicar la compresión, la colocación, la generación local y la comparación de rayas en el orden en que se realizaron. Mantener la admisibilidad quirúrgica y la glosa del grado de brecha. | `introduccion.tex`:37-43; `conclusiones.tex`:22. |
| Resultado de la compuerta (G-T4) | Conservar seis configuraciones, límite de 25 unidades Hounsfield, menor error de 61.72 y 34 pacientes; explicar el cambio al dominio de imagen. | `conclusiones.tex`:14; `introduccion.tex`:46-48. |
| Colocación (E-P3, G-T4) | Conservar 3\,600 poses en 72 pacientes y las distancias 0.206, 0.230 y 0.395; explicitar que la cercanía es descriptiva, sin regla de decisión. | `conclusiones.tex`:16, 24. |
| Apariencia (E-P3, G-T4) | Conservar 13 pacientes, diferencia de 301.0 unidades Hounsfield a la baja y desenlace no concluyente porque el intervalo cruza el límite de equivalencia. No presentar esto como no equivalencia demostrada. | `introduccion.tex`:52-54; `conclusiones.tex`:18. |
| Límites (E-P3, P-R1) | Separar el juicio visual de la autora, la falta de caída de amplitud con la distancia y la ausencia de evaluación de segmentación. | `conclusiones.tex`:30, 36, 38. |

La reducción retira cifras secundarias de los controles y análisis añadidos, sin cambiar las cifras o los desenlaces conservados. Estructura: 3 oraciones de introducción, 4 de método, 6 de resultados y 3 de conclusiones. Sin citas, siglas, figuras ni tablas. No se abrieron ni cerraron GAP.

Verificación: `python scripts/lint_redaccion.py resumen --compilar` → PASA; documento completo de 194 páginas. Los dos avisos bajos E-P1 corresponden a cifras sin referencia dentro del resumen, donde P-R2 prohíbe citas y referencias. `TOTAL alta=0 media=0 baja=2`.

## Patrones

| Patrón | Criterio | Antes | Corrección |
|---|---|---|---|
| Detalles metodológicos y salvedades desplazan la idea principal en el resumen | P-R1, E-M1 | La compuerta y sus controles ocupaban la apertura del método y gran parte del resultado. | Se presenta primero el problema, luego cada componente, su resultado y su límite. |

## Decisiones de redacción

La equivalencia no establecida se expresa como desenlace de la prueba, sin convertirla en no equivalencia demostrada. La utilidad para entrenar segmentadores se declara no evaluada. Las mismas decisiones se aplicaron en el abstract.
