# Revisión de estilo — capitulo3 — r20

## Hallazgos
| ID | Sev | Criterio | Ubicación | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S1 | media | E-M1 | `overleaf/secciones/capitulo3.tex:202` | «La red, cuya arquitectura no se buscó, es una U-Net» | La parametrización de predicción $v$ se define para un proceso de difusión con preservación de varianza; la oración sobre la arquitectura pasa al párrafo de entrenamiento. |
| S2 | media | E-T2 | `overleaf/secciones/capitulo3.tex:202` | «proceso de difusión con preservación de varianza» | Salimans y Ho~\cite{salimans2022progressive} formulan la predicción $v$ para un proceso con preservación de varianza (\emph{variance-preserving}). |
| S3 | media | E-R2 | `overleaf/secciones/capitulo3.tex:202` | «Esta fuente respalda la definición matemática» | Salimans y Ho evalúan la parametrización en imágenes naturales, no en TC, implantes ni condicionamiento anatómico. |

## Impresión general
El capítulo mantiene una voz técnica y cauta. El agregado de la fuente nueva es preciso, pero el párrafo mezcla arquitectura, definición y alcance, y cierra con una metadeclaración en vez de nombrar directamente el dominio evaluado.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un párrafo creado al insertar una fuente conserva una oración de otra función | E-M1 | «La red [...] es una U-Net» antes de definir $v$ | PAT-33 |
| Se declara qué respalda la fuente en vez de decir directamente qué evaluó | E-R2 | «Esta fuente respalda la definición matemática» | PAT-5 |
