# Revision de estilo — capitulo1 — r11

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-1 | media | E-R1 | l.13, oraciones 3--6 | "La Sección..." (cuatro oraciones consecutivas) | Sustituir la serie por: "Las secciones de TC y artefactos sustentan la compuerta y la representación; la de fijación iliosacra, el muestreador; y las de difusión y estadística, el sintetizador y la lectura de resultados, respectivamente." Conservar las remisiones en los nombres de cada sección. Patron PAT-119 reincide |
| ES-2 | media | E-O2, E-M1 | l.35, parrafo completo | "Los valores de TC se expresan... En la cohorte primaria..." | Iniciar un párrafo nuevo con "En la cohorte primaria, con el recorte por defecto..." y dejar allí también la consecuencia para la medición del corredor. El párrafo actual tiene ocho oraciones y pasa de definir HU y dos umbrales a justificar una decisión anatómica. Patron PAT-58 reincide |
| ES-3 | media | E-R2 | l.55, oracion 4 | "Esa regla se declaró no aplicable" | "Esa regla no es aplicable: su desenlace cambia según el percentil con que se resume la pérdida, y la rama que habría cambiado la representación quedó bloqueada por el congelamiento del diseño." La formulación actual anuncia una declaración en vez de dar el hecho. Patron PAT-5 reincide |
| ES-4 | baja | E-R2, E-R4 | l.99, oraciones 2--4 | "motiva tenerla en cuenta" / "deja la densidad como motivación" | "La menor densidad del ala sacra respecto del cuerpo de S1 motiva evaluar la densidad ósea en trabajos futuros; no forma parte de SAP porque la medición sobre la que se calculaba su componente se retiró como evidencia de densidad (Sección~\ref{sec:poses})." |
| ES-5 | baja | E-M8 | l.103, oracion 2 | "Los modelos de difusión son una familia de ellos" | "Los modelos de difusión son una familia de modelos generativos, y Kazerouni et al.~\cite{kazerouni2023diffusionsurvey} revisan su uso en imagen médica." |
| ES-6 | media | E-M8 | l.145, oraciones 4--5 | "Recalculados con la prueba bilateral... se obtienen los mismos valores" | "El recálculo con la prueba bilateral de \texttt{scipy.stats.fisher\_exact}, en SciPy 1.15.3 y con la convención \emph{minlike}, reproduce los valores de las cuatro tablas." Así se evita que el participio "Recalculados" quede referido a los valores mientras la principal usa una construcción impersonal. |
| ES-7 | media | E-R2 | l.151, oracion 3 | "se declaran sin corrección por multiplicidad" | "Los análisis añadidos después de conocer su resultado son descriptivos, no se corrigen por multiplicidad y solo pueden bajar la categoría del desenlace, nunca subirla (Sección~\ref{sec:amenazas})." Patron PAT-5 reincide |
| ES-8 | baja | E-M8 | l.147, oracion 1 | "La protección contra ajustar el resultado a los datos depende" | "La protección frente al ajuste del resultado a los datos depende de qué se fija antes de observarlos y de cuántas oportunidades de aprobación admite la regla." |

TOTAL alta=0 media=5 baja=3

## Impresion general
Leído seguido, el capítulo mantiene un registro sobrio, preciso y sin afirmaciones de realismo visual.
El defecto dominante es residual: algunas formulaciones describen que algo "se declara" en vez de decir el hecho, y un párrafo aún conserva funciones acumuladas de rondas anteriores.
No reaparecen las ambigüedades terminológicas ni las justificaciones separadas que se corrigieron en r10.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Serie de oraciones contiguas abiertas con el mismo sujeto de navegación | E-R1 | "La Sección..." (cuatro veces) | PAT-119 |
| Párrafo ampliado hasta mezclar definición, evidencia propia y justificación metodológica | E-O2, E-M1 | "Los valores de TC se expresan... En la cohorte primaria..." | PAT-58 |
| Metadeclaración que sustituye el hecho metodológico | E-R2 | "se declaró no aplicable" / "se declaran sin corrección" | PAT-5 |
