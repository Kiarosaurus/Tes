# Revision guia CS — resumen — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | P-R4 | abstract.tex:4, :7-17 | El abstract conserva el titulo provisional «TÍTULO DE LA TESIS EN INGLÉS», texto de relleno y palabras clave genericas. Por tanto, no es la traduccion del resumen ni recoge en ingles el titulo nuevo de `main.tex:86`; falta por completo la funcion exigida a la seccion paralela. | Sustituir la plantilla por una traduccion fiel del resumen, traducir el titulo vigente de `main.tex:86` y usar palabras clave equivalentes, conservando las mismas cifras, cautelas y limites del texto en español. |
| guia-2 | media | G-R1 | resumen.tex:7, :9-11 | El resumen presenta la compuerta, el muestreador y el sintetizador, pero no permite señalar el Objetivo 4: formalizar la admisibilidad quirurgica de la colocacion y adoptar las metricas de apariencia. Tampoco resume su resultado, aunque `introduccion.tex:43` lo declara como objetivo y `conclusiones.tex:22` informa su cumplimiento. | Integrar, sin añadir una sigla, una clausula metodologica sobre la formalizacion de la admisibilidad mediante brecha y viabilidad, y una clausula de resultado sobre su implementacion y controles; puede incorporarse a las oraciones existentes para conservar IMRyC. |
| guia-3 | media | G-T2, P-R1 | resumen.tex:7, :9 | Patron PAT-3 reincide: «autoencoder» y la metrica publicada «streak amplitude» intervienen en el metodo y en el desenlace principal sin una glosa funcional suficiente. El lector que solo consulta el resumen no puede saber que pieza se somete a la compuerta ni que magnitud de las rayas expresa la comparacion. | Añadir glosas breves respaldadas por el documento: describir el autoencoder por su funcion de compresion y reconstruccion, y explicar que aspecto del artefacto cuantifica la metrica, conservando su nombre publicado en cursiva. |

TOTAL alta=1 media=2 baja=0

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple: el resumen identifica el problema, la cadena, las condiciones principales, los resultados y los limites; la autonomia terminologica pendiente se recoge en guia-3 |
| G-T2 | no cumple (guia-3): dos terminos centrales aparecen sin glosa funcional suficiente |
| G-T3 | cumple: no introduce simbolos con significados incompatibles con el resto del documento |
| G-T4 | cumple: `resumen-r00-respuesta.md` deja la fuente interna de cada cifra y el resumen conserva sus condiciones principales; la comprobacion material corresponde al auditor de trazabilidad |
| G-T5 | cumple: sigue la progresion problema y proposito, metodo, resultados y conclusiones, con 3/4/6/3 oraciones |
| G-T6 | cumple: el resumen no contiene citas ni referencias bibliograficas, conforme a P-R2 |
| G-R1 | no cumple (guia-2): contiene problema, objetivo general, contribucion y resultados de los Objetivos 1 a 3, pero omite el Objetivo 4 y su resultado |
| P-R1 | no cumple (guia-3): el argumento general se entiende, pero dos conceptos decisivos exigen consultar el cuerpo para identificar la pieza evaluada y la magnitud comparada |
| P-R2 | cumple: no contiene figuras, tablas, citas ni referencias; desarrolla las siglas y conserva `CTPelvic1K` como nombre propio del conjunto y las unidades como simbolos de medida |
| P-R3 | cumple: presenta 3 oraciones de introduccion, 4 metodologicas, 6 de resultados con cifras y 3 de conclusiones |
| P-R4 | no cumple (guia-1): `abstract.tex` sigue siendo la plantilla y no traduce el resumen ni el titulo vigente |

## Propuestas de criterio

Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Termino tecnico usado antes de su definicion formal | G-T2 | «el autoencoder de un modelo de difusion latente» | PAT-3 |
