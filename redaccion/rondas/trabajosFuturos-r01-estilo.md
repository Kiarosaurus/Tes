# Revisión de estilo — trabajosFuturos — r01

## Hallazgos
| ID | Sev | Criterio | Ubicación | Texto actual (máx. 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-01 | baja | E-M8 | `overleaf/secciones/trabajosFuturos.tex:15` | "Un espacio latente que aprobara la compuerta podría recibirla como representación" | "Un espacio latente que aprobara la compuerta podría usar la codificación multiventana como representación." |
| ES-02 | media | E-R2, E-P4 | `overleaf/secciones/trabajosFuturos.tex:19` | "las dos condiciones admiten una extensión directa" | "El muestreador se ejecutó en un solo corredor y con todos sus componentes." Las oraciones siguientes ya presentan por separado las dos evaluaciones futuras; "directa" no tiene un criterio que la sostenga. |
| ES-03 | media | E-M4 | `overleaf/secciones/trabajosFuturos.tex:21` | "la fractura [...] es un factor de confusión de esa causa" | "La fractura, confirmada en 20 de los 30 casos del cribado, impide atribuir el estrechamiento solo a la anatomía sacra." |
| ES-04 | media | E-M4, E-M8 | `overleaf/secciones/trabajosFuturos.tex:23` | "Medir lo primero [...] cerraría los dos supuestos" | "Medir la posición del vóxel más craneal y extender la revisión en cortes permitiría comprobar ambos supuestos." |
| ES-05 | baja | E-M8 | `overleaf/secciones/trabajosFuturos.tex:27` | "su resultado describiría el realismo que este trabajo no reclama" | "Sus resultados describirían el realismo visual que este trabajo no reclama." |
| ES-06 | media | E-O2, E-M1 | `overleaf/secciones/trabajosFuturos.tex:29` | "Las mediciones del Objetivo~3 dejan cuantificado, en cambio" | Patrón PAT-58 reincide: el párrafo acumula ocho oraciones y pasa del diseño de una versión nueva a los defectos medidos. Abrir un párrafo nuevo con: "Las mediciones del Objetivo~3 cuantifican lo que una versión nueva tendría que corregir." |
| ES-07 | media | E-R2 | `overleaf/secciones/trabajosFuturos.tex:35` | "es la pieza que uniría los dos componentes en una misma evaluación" | "La síntesis sobre las poses del muestreador permitiría evaluar juntos los dos componentes." |
| ES-08 | media | E-P4, E-R2 | `overleaf/secciones/trabajosFuturos.tex:35` | "Su expectativa, fijada sin umbral numérico, era que la amplitud variara poco" | Patrón PAT-178 reincide: "poco" no permite contrastar la expectativa y la propia oración reconoce que no hubo umbral. Propuesta: eliminar. |

TOTAL alta=0 media=6 baja=2

## Impresión general
Leída de corrido, la sección suena sobria y distingue con cuidado lo ejecutado, lo no medido y lo propuesto. La acumulación de salvedades solo desborda un párrafo; en el resto, los desvíos son referentes imprecisos o formulaciones vagas. No se detecta informalidad ni certeza mayor que la de las dos fuentes citadas.

## Patrones
| Patrón (una línea, generalizable a otras secciones) | Criterio | Ejemplo antes (máx. 15 palabras) | Ya en bitácora (PAT-n o "nuevo") |
|---|---|---|---|
| Un párrafo crece por salvedades hasta reunir más de siete oraciones y dos funciones | E-O2, E-M1 | "Las mediciones del Objetivo~3 dejan cuantificado, en cambio" | PAT-58 |
| Una expectativa cualitativa se presenta sin un umbral que permita contrastarla | E-P4, E-R2 | "la amplitud variara poco entre grados" | PAT-178 |
