# fay2010two — Pruebas exactas bilaterales e intervalos concordantes

- **DOI / URL:** https://doi.org/10.32614/RJ-2010-008
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/fay2010two.pdf

## Que hace (3 lineas maximo)
Compara tres definiciones de valor $p$ exacto bilateral para datos discretos: central, minlike y Blaker. Define el intervalo de confianza concordante como la inversión de la misma función de valores $p$ y muestra inconsistencias cuando una prueba minlike se combina con un intervalo central.

## Restriccion o supuesto clave
La afirmación sobre `fisher.test` se documenta bajo la salvedad explícita de que el artículo asume la versión 2.11.0 del paquete `stats`. Para tablas $2\times2$ no pareadas, la aplicación bilateral usual de `fisher.test` entrega un valor $p$ minlike, mientras su intervalo de confianza del odds ratio es central; por ello no son necesariamente concordantes.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Tres definiciones bilaterales | “We list 3 ways to define the two-sided p-value” | Overview of two-sided exact tests, p. 53 (p. 1 del PDF) |
| Ejemplo Fisher: $p_m=0.032$ | “gives $p_m = 0.032$ using the minlike method” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |
| IC central del 95%: $(0.92,14.58)$ | “confidence interval on the odds ratio of (0.92, 14.58)” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |

## Donde entra en mi tesis
Capítulo 1, protocolo estadístico: permite declarar que la prueba exacta bilateral de Fisher ejecutada mediante `fisher.test` usa la convención minlike para el valor $p$, de acuerdo con la versión de `stats` estudiada. También obliga a distinguir ese valor $p$ del intervalo central del odds ratio que devuelve la función; si se reporta un intervalo concordante, debe invertirse la misma función minlike o emplearse una implementación como `exact2x2`.

## Dudas para el asesor
- ¿Se fijará y reportará la versión de R usada para comprobar que la convención descrita para `stats` 2.11.0 sigue vigente?
- ¿La tesis reportará solo el valor $p$ de `fisher.test` o también un intervalo del odds ratio concordante?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Alcance | Datos discretos | “for discrete data there are several different ways” | Abstract, p. 53 (p. 1 del PDF) |
| Definicion | Tres métodos bilaterales | “central, minlike, and blaker methods” | Overview of two-sided exact tests, p. 53 (p. 1 del PDF) |
| Definicion | Central: doble de la cola menor | “2 times the minimum of the one-sided p-values” | Overview of two-sided exact tests, p. 53 (p. 1 del PDF) |
| Definicion | Central acotado por uno | “bounded above by 1” | Overview of two-sided exact tests, p. 53 (p. 1 del PDF) |
| Definicion | Minlike suma resultados no más probables | “likelihoods less than or equal to the observed likelihood” | Overview of two-sided exact tests, p. 54 (p. 2 del PDF) |
| Definicion | Blaker combina ambas colas | “combines the probability of the smaller observed tail” | Overview of two-sided exact tests, p. 54 (p. 2 del PDF) |
| Orden | $p_c\geq p_b$ | “$p_c \geq p_b$ for all cases” | Overview of two-sided exact tests, p. 54 (p. 2 del PDF) |
| Definicion | IC concordante $100(1-\alpha)\%$ | “smallest interval that contains all $\theta_0$” | Overview of two-sided exact tests, p. 54 (p. 2 del PDF) |
| Criterio | Valores no rechazados | “such that $p(\theta_0)>\alpha$” | Overview of two-sided exact tests, p. 54 (p. 2 del PDF) |
| Criterio | Colas centrales $\alpha/2$ | “less than $\alpha/2$ probability” | Overview of two-sided exact tests, p. 53 (p. 1 del PDF) |
| Limitacion | Inconsistencia rara con IC concordantes minlike/Blaker | “will happen very rarely for the minlike and blaker methods” | Overview of two-sided exact tests, p. 54 (p. 2 del PDF) |
| Software | Versión de `stats` evaluada | “we assume version 2.11.0 for the stats package” | A motivating example, p. 53 (p. 1 del PDF) |
| Convencion | `fisher.test` bilateral usa minlike | “gives $p_m = 0.032$ using the minlike method” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |
| Ejemplo | Tabla `c(4,11,50,569)` | “fisher.test(matrix(c(4,11,50,569), 2, 2))” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |
| Ejemplo | Valor $p_m=0.032$ | “gives $p_m = 0.032$” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |
| Ejemplo | IC central del 95% | “but 95% confidence interval” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |
| Ejemplo | IC del OR $(0.92,14.58)$ | “odds ratio of (0.92, 14.58)” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |
| Resultado | `exact2x2` evita la inconsistencia | “the test-CI inconsistency disappears” | Analysis of $2\times2$ tables, unpaired, p. 55 (p. 3 del PDF) |
| Umbral | Significancia tradicional 0.05 | “traditional 0.05 cutoff of significance” | Analysis of $2\times2$ tables, paired, p. 56 (p. 4 del PDF) |
| Limitacion | Métodos minlike y Blaker pueden tener anomalías | “can have other anomalies” | Unavoidable Inconsistencies, p. 57 (p. 5 del PDF) |
| Comparacion | Central evita todas las inconsistencias prueba-IC | “the central method does avoid all test-CI inconsistencies” | Unavoidable Inconsistencies, p. 57 (p. 5 del PDF) |
