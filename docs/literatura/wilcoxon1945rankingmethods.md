# wilcoxon1945rankingmethods — Comparaciones individuales mediante rangos

- **DOI / URL:** http://www.jstor.org/stable/3001968 (URL estable indicada en el PDF; el DOI del RAW corresponde a una reimpresión de 1992)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wilcoxon1945rankingmethods.pdf

## Que hace (3 lineas maximo)
Propone procedimientos de rangos para comparar dos tratamientos, distinguiendo experimentos no pareados y comparaciones pareadas. Para pares, ordena por magnitud las diferencias ignorando el signo y evalúa la suma menor de rangos con un mismo signo.

## Restriccion o supuesto clave
Para el caso pareado, el artículo formula la hipótesis nula como diferencias positivas y negativas distribuidas normalmente alrededor de cero. Los ceros, el supuesto moderno de simetría y una corrección formal para empates no quedan desarrollados como reglas completas en este PDF.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 15 pares; suma negativa 24 | “The sum of the negative rank numbers is −24.” | Paired Comparisons, p. 80 (p. 2 del PDF) |
| 8 pares; suma negativa 3 | “The sum of the negative rank numbers is −3.” | Paired Comparisons, p. 80 (p. 2 del PDF) |

## Donde entra en mi tesis
Fuente primaria para justificar una comparación pareada no paramétrica basada en rangos con signo: calcular diferencias por unidad pareada, ordenar sus magnitudes sin signo, reponer los signos y usar la suma menor de rangos positivos o negativos. La ficha no convierte el procedimiento original en una prueba unilateral o bilateral moderna sin declarar esa elección.

## Dudas para el asesor
- ¿Se reportará explícitamente la convención para diferencias cero, empates y alternativa bilateral?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Diseño | Dos categorías | “replications ... unpaired” / “a number of paired comparisons” | Introducción, p. 80 (p. 2 del PDF) |
| Definicion | Diferencias pareadas con signo | “some of which may be positive and some negative” | Introducción, p. 80 (p. 2 del PDF) |
| Definicion | Sustitución por rangos | “scores 1, 2, 3, ... n are substituted” | Introducción, p. 80 (p. 2 del PDF) |
| Ejemplo | Número de pares | “There were 15 such differences” | Paired Comparisons, p. 80 (p. 2 del PDF) |
| Ejemplo | Suma de rangos negativos | “The sum of the negative rank numbers is −24.” | Paired Comparisons, p. 80 (p. 2 del PDF) |
| Criterio | Probabilidad del ejemplo | “between 0.019 and 0.054 for 15 pairs” | Paired Comparisons, p. 80 (p. 2 del PDF) |
| Ejemplo | Segunda suma negativa | “The sum of the negative rank numbers is −3.” | Paired Comparisons, p. 80 (p. 2 del PDF) |
| Criterio | Probabilidad del segundo ejemplo | “probability between 0.024 and 0.055” | Paired Comparisons, p. 80 (p. 2 del PDF) |
| Empates | Rango medio | “those tests are assigned the mean rank value” | Unpaired Experiments, p. 80 (p. 2 del PDF) |
| Supuesto | Centro bajo la nula | “positive and negative differences normally distributed about zero” | Discussion, p. 81 (p. 3 del PDF) |
| Algoritmo | Orden por magnitud | “assigned to the differences in order of magnitude neglecting signs” | Discussion, p. 81 (p. 3 del PDF) |
| Algoritmo | Restitución del signo | “negative differences receive a negative sign” | Discussion, p. 81 (p. 3 del PDF) |
| Estadistico | Menor suma con un signo | “whichever is less” | Tabla II, p. 82 (p. 4 del PDF) |
| Umbral | Niveles tabulados | “probabilities of 0.05 and 0.01 respectively” | p. 80 (p. 2 del PDF) |
| Alcance | Diferencias cero | NO ENCONTRADO EN EL PDF | — |
| Alcance | Definición explícita de prueba bilateral moderna | NO ENCONTRADO EN EL PDF | — |
