# schuirmann1987comparison — Dos pruebas unilaterales para equivalencia

- **DOI / URL:** https://doi.org/10.1007/BF01068419
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/schuirmann1987comparison.pdf

## Que hace (3 lineas maximo)
Compara el enfoque de potencia con el procedimiento de dos pruebas unilaterales (TOST) para equivalencia de biodisponibilidad media. Define la no equivalencia como hipótesis nula y demuestra la equivalencia operacional entre TOST a nivel $\alpha$ y un IC de $1-2\alpha$ contenido por completo en el margen de equivalencia.

## Restriccion o supuesto clave
El desarrollo principal supone normalidad, varianzas intra-sujeto iguales, crossover balanceado y, para comparar con potencia, un intervalo simétrico. Los márgenes de equivalencia deben fijarlos expertos del dominio y no se derivan de los datos.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| $\alpha=0.05$ por prueba unilateral | “specific choice of α = 0.05” | Resumen, p. 657 (p. 1 del PDF) |
| IC 90 % para TOST a 5 % | “ordinary 1 − 2α ... confidence interval” | Two One-Sided Tests Procedure, p. 661 (p. 5 del PDF) |

## Donde entra en mi tesis
Justifica declarar equivalencia solo si ambas pruebas unilaterales rechazan no equivalencia o, equivalentemente, si el IC 90 % queda íntegramente dentro de $[\theta_1,\theta_2]$ cuando $\alpha=0.05$. No debe sustituirse por “ausencia de diferencia significativa” ni por un IC 95 %.

## Dudas para el asesor
- ¿Qué margen práctico de equivalencia $[\theta_1,\theta_2]$ se preespecificará para cada métrica?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Comparador | Nivel del enfoque de potencia | “testing the hypothesis of no difference at level 0.05” | Resumen, p. 657 (p. 1 del PDF) |
| Comparador | Potencia exigida | “requiring an estimated power of 0.80” | Resumen, p. 657 (p. 1 del PDF) |
| Definicion | IC equivalente | “usual (shortest) 1 − 2α confidence interval” | Resumen, p. 657 (p. 1 del PDF) |
| Umbral | Nivel TOST estudiado | “specific choice of α = 0.05” | Resumen, p. 657 (p. 1 del PDF) |
| Hipotesis | Nula de no equivalencia | “The null hypothesis, H0, states that ... are not equivalent.” | Statement of the Problem, p. 658 (p. 2 del PDF) |
| Hipotesis | Alternativa de equivalencia | “The alternative hypothesis, H1, states that they are equivalent.” | Statement of the Problem, p. 658 (p. 2 del PDF) |
| Definicion | Intervalo de equivalencia | “The interval [θ1, θ2] may be called the equivalence interval.” | Statement of the Problem, p. 659 (p. 3 del PDF) |
| Criterio | Márgenes fijados externamente | “made by the experts ... (not by the statistician!)” | Statement of the Problem, p. 659 (p. 3 del PDF) |
| Supuesto | Normalidad | “it is assumed that the data arise from a normal distribution” | Statement of the Problem, p. 659 (p. 3 del PDF) |
| Supuesto | Crossover balanceado | “we assume that the study is a balanced crossover study” | Statement of the Problem, p. 659 (p. 3 del PDF) |
| Supuesto | Sin observaciones faltantes | “there are no missing observations from any subject” | Statement of the Problem, p. 659 (p. 3 del PDF) |
| Supuesto | Intervalo simétrico | “assumption that θ1 = −θ2” | Statement of the Problem, p. 659 (p. 3 del PDF) |
| Regla | Rechazar ambas nulas | “if and only if both H01 and H02 are rejected” | Two One-Sided Tests Procedure, p. 660 (p. 4 del PDF) |
| Regla | Nivel por prueba | “at a chosen nominal level of significance α” | Two One-Sided Tests Procedure, p. 660 (p. 4 del PDF) |
| Equivalencia | Contención completa del IC | “confidence interval ... is completely contained in the equivalence interval” | Two One-Sided Tests Procedure, p. 661 (p. 5 del PDF) |
| IC | 90 % cuando $\alpha=0.05$ | “ordinary 1 − 2α (not 1 − α) confidence interval” | Two One-Sided Tests Procedure, p. 661 (p. 5 del PDF) |
