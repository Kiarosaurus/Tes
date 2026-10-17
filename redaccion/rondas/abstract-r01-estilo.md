# Revisión de estilo — abstract — r01

## Hallazgos
| ID | Sev | Criterio | Ubicación | Texto actual (máx. 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-01 | media | E-M4, E-M8 | `overleaf/secciones/abstract.tex:11` | "rates each pose by corridor viability and cortical breach grade, according to how far" | "A placement sampler proposes three-dimensional screw poses in the osseous corridor, and surgical admissibility of placement, proposed here, assesses corridor viability and cortical breach grade; the latter records how far the screw protrudes beyond the bone." |
| ES-02 | media | E-R2, E-M4, E-M8 | `overleaf/secciones/abstract.tex:13` | "passed its checks, and the grade distribution ... lay 0.206 grades" | Patrón PAT-205 reincide: "passed its checks" no identifica los controles y la distancia queda insertada como inciso. Propuesta: "Surgical admissibility of placement passed its identity, monotonicity and resolution checks, and the grade distribution of 3\,600 poses in 72 patients had Wasserstein-1 distances of 0.206 grades to the navigated clinical series and 0.230 to the conventional series." |
| ES-03 | baja | E-M8 | `overleaf/secciones/abstract.tex:13` | "the best one gave 61.72 Hounsfield units" | "The lowest mean absolute error was 61.72 Hounsfield units." |
| ES-04 | media | E-M8, E-P3 | `overleaf/secciones/abstract.tex:13` | "crosses the lower limit of the equivalence margin of 196.3" | "Its 90\,\% confidence interval, from $-477.0$ to $-124.9$ Hounsfield units, crosses the lower equivalence bound of $-196.3$ Hounsfield units; the outcome is inconclusive, and the synthesizer has lower \emph{streak amplitude} than the protocol." |

TOTAL alta=0 media=3 baja=1

## Impresión general
Leído de corrido, el abstract es sobrio, mantiene la estructura del resumen y distingue los resultados de sus límites. Los problemas son locales: dos construcciones traducidas ocultan la relación entre medida y resultado, y dos referentes genéricos restan precisión. No se detecta informalidad ni prosa inflada.

## Patrones
| Patrón (una línea, generalizable a otras secciones) | Criterio | Ejemplo antes (máx. 15 palabras) | Ya en bitácora (PAT-n o "nuevo") |
|---|---|---|---|
| Un resultado se valora sin nombrar los controles que hacen verificable la valoración | E-R2, E-M4 | "passed its checks" | PAT-205 |
