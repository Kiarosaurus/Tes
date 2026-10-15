# pitman1939note — Nota sobre correlacion normal (prueba exacta de igualdad de varianzas en pares)

- **DOI / URL:** https://doi.org/10.1093/biomet/31.1-2.9 (DOI tomado de `refs/raw/pitman1939note.bibtex`; el DOI impreso en el PDF: NO ENCONTRADO EN EL PDF)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/pitman1939note.pdf

## Que hace (3 lineas maximo)
Para pares (x, y) de una normal bivariada con correlacion poblacional desconocida, construye u = x/σ1 + y/σ2 y v = x/σ1 − y/σ2, que son normales independientes, y usa la correlacion muestral R entre u y v para obtener una prueba exacta de σ1²/σ2² = 1 y limites fiduciales de ese cociente. Transforma R en una t de Student con n − 2 gl. Al final aplica el mismo truco (u = x + y, v = x − y) a la estimacion de ρ cuando σ1 = σ2.

## Restriccion o supuesto clave
Supuesto unico y explicito: x, y "normally correlated variables" con la densidad normal bivariada escrita en p. 9. Toda la exactitud depende de esa normalidad bivariada; no hay discusion de robustez, de muestras pequenas ni de alternativas no parametricas (NO ENCONTRADO EN EL PDF). La prueba es sobre el cociente de **varianzas** ω = σ1²/σ2², no sobre coeficientes de variacion.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| n − 2 grados de libertad | "is distributed like Fisher's t with n − 2 degrees of freedom" | p. 10 |
| Hipotesis nula ω = 1 | "test the null hypothesis ω = 1, we simply insert this value" | p. 10 |

## Donde entra en mi tesis
`overleaf/secciones/capitulo3.tex`, §Analisis estadistico (`\GAPLIT` de capitulo3-r22; DEC 2026-10-15 pto 22; implicancia #185): comparacion de la dispersion entre pacientes de difusor frente a Peters sobre los mismos 13 pacientes. Respalda: (a) que la prueba es exacta bajo normalidad bivariada con correlacion desconocida; (b) el estadistico R y su transformacion t = R√(n−2)/√(1−R²) con n − 2 gl, que es exactamente lo implementado.

**Atribucion Pitman frente a Morgan (para citar bien):**
- **Aporta Pitman (en este PDF):** la transformacion a u, v independientes; R como correlacion de u y v; la expresion de R en funcion de w = S1/S2, r y ω; la t con n − 2 gl; R² ~ B(1/2, (n−2)/2); limites fiduciales para ω; un ejemplo numerico (datos de Finney, n = 173, t = 2.902).
- **Matiz importante:** para la prueba de varianzas, Pitman define u, v **estandarizados por σ1, σ2** (no x + y y x − y literalmente). La forma "correlacion entre x + y y x − y" aparece en el PDF solo en p. 11, para la **estimacion de ρ con σ1 = σ2**, no para la prueba de varianzas. Que bajo ω = 1 la R de Pitman coincida con corr(x + y, x − y) es una consecuencia algebraica (al imponer σ1 = σ2 la escala comun se cancela), pero esa frase no esta escrita en el PDF: NO ENCONTRADO EN EL PDF.
- **No aporta Pitman:** el nombre "Pitman-Morgan"; cualquier aplicacion a datos reales distinta del ejemplo de Finney; cualquier discusion de CV, transformacion logaritmica, potencia, tamano muestral minimo o robustez a no normalidad (todo NO ENCONTRADO EN EL PDF). La nota editorial (p. 9) dice que Morgan trato el mismo problema "following quite different lines": lo que aporta Morgan debe salir de la ficha de `morgan1939test`, no de aqui.

## Dudas para el asesor
- La comparacion de #185 se reporta como CV (0.076 frente a 0.241), pero Pitman prueba igualdad de **varianzas**. Si las medias por brazo difieren, igualdad de varianzas no equivale a igualdad de CV. ¿Se aplico la prueba sobre valores en escala log (donde la varianza aproxima CV²) o sobre valores crudos? La redaccion debe decir cual.
- Con n = 13, ¿basta declarar el supuesto de normalidad bivariada, o conviene un chequeo (o una alternativa robusta) dado que el PDF no discute robustez?
- ¿Se cita a Pitman solo, o "Pitman y Morgan" como par? Por la nota editorial son derivaciones independientes del mismo problema; la forma t con n − 2 gl esta explicita en Pitman.

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Contexto | Problema heredado de Finney 1938 | "Finney (1938) discussed the distribution of the ratio of estimates" | p. 9 (p. 1 del PDF; numero no impreso, rango 9-12 del raw) |
| Contexto | Finney: test con ρ conocido | "a test for significance could be applied when the population correlation coefficient is known" | p. 9 |
| Critica a Finney | Adaptacion con r muestral insatisfactoria | "this adaptation is not completely satisfactory" | p. 9 |
| Aporte | Prueba exacta con ρ desconocido | "an exact test for significance can be obtained" | p. 9 |
| Aporte | Limites fiduciales del cociente | "fiducial limits for the ratio of the population variances determined" | p. 9 |
| Supuesto | Normalidad bivariada | "Suppose that x, y are normally correlated variables" | p. 9 |
| Datos | n pares observados | "are n pairs of observed values of x, y" | p. 9 |
| Definicion | S1, S2 = sumas de cuadrados; r = correlacion muestral | S1 = Σ(xs − x̄)², S2 = Σ(ys − ȳ)² (formula, no frase) | p. 9 |
| Definicion | u, v estandarizados | u = x/σ1 + y/σ2, v = x/σ1 − y/σ2 (formula) | p. 9 |
| Propiedad | u, v independientes | "are independent normal variables with variances 2(1+ρ), 2(1−ρ)" | p. 9 |
| Propiedad | Correlacion nula entre us, vs | "constitute a sample from a normal bi-variate population with zero correlation" | pp. 9-10 |
| Estadistico | R = correlacion de u y v | "Hence the distribution of their correlation coefficient ... is known" | p. 10 |
| Definicion | ω y w | ω = σ1²/σ2², w = S1/S2 (formula) | p. 10 |
| Estadistico | R en funcion de muestra y ω | R = (w − ω)/√{(w + ω)² − 4r²wω} (formula) | p. 10 |
| Prueba | Hipotesis nula de igualdad de varianzas | "test the null hypothesis ω = 1, we simply insert this value" | p. 10 |
| Distribucion | R² beta | "We know that R² has a B(½, ½n − 1) distribution" | p. 10 |
| Distribucion | z de Student | "is distributed like 'Student's' z for a sample of n − 1" | p. 10 |
| Estadistico | t = R√(n−2)/√(1−R²) | t = R√(n−2)/√(1−R²) = (w − ω)√(n−2)/√{4(1−r²)wω} (formula) | p. 10 |
| Distribucion / gl | t con n − 2 gl | "is distributed like Fisher's t with n − 2 degrees of freedom" | p. 10 |
| Criterio | Region de aceptacion | "we can determine k such that P{|t| ≤ k} = α" | p. 10 |
| Intervalo | Limites fiduciales | P{w(K − √(K²−1)) ≤ ω ≤ w(K + √(K²−1))} = α (formula) | p. 11 |
| Intervalo | Definicion de K | K = 1 + 2(1 − r²)k²/(n − 2) (formula) | p. 11 |
| Ejemplo | n = 173 | "n = 173" (datos de Finney 1938, p. 192) | p. 11 |
| Ejemplo | w = (5.299)²/(4.766)² | "w = S1/S2 = (5·299)²/(4·766)²" | p. 11 |
| Ejemplo | r = 0.878 | "r = 0·878" | p. 11 |
| Ejemplo | t = 2.902 | "putting ω = 1, we obtain t = 2·902" | p. 11 |
| Ejemplo | Aproximacion normal para n grande | "As n is large the distribution of t is approximately normal" | p. 11 |
| Criterio | Significativo al 1% | "the value of t is significant at the 1% level" | p. 11 |
| Ejemplo | Menor significancia que Finney | "the exact test gives less significance than Finney's" | p. 11 |
| Comparacion | Caso ρ = 0: w/(w+ω) beta | "has a B{½(n − 1), ½(n − 1)} distribution" | p. 11 |
| Distribucion | R² ~ B(½, ½(n−2)) para todo ρ | "As shown above, for any value of ρ" ... "has a B{½, ½(n−2)} distribution" | p. 11 |
| Extension | Estimacion de ρ con σ1 = σ2 | "the distribution required for the estimation of ρ when the standard deviations ... are the same" | p. 11 |
| Extension | Suma y diferencia literal (solo para estimar ρ) | "u = x + y, v = x − y" | p. 11 |
| Extension | Varianzas de x + y y x − y | "independent normal variables with variances 2σ²(1+ρ), 2σ²(1−ρ)" | p. 11 |
| Extension | Chi-cuadrado con n − 1 gl | "each distributed like χ² with n − 1 degrees of freedom" | p. 11 |
| Extension | Mismas medias: χ² con n gl | "is distributed like χ² with n degrees of freedom" | p. 12 |
| Extension | Beta con medias iguales | "w/(1 + w) has a B{½(n − 1), ½n} distribution" | p. 12 |
| Extension | Equivalencia con ANOVA | "corresponds exactly to the treatment of fraternal correlation by the analysis of variance" | p. 12 |
| Nota editorial | Morgan, mismo problema, otra via | "the two treatments ... follow quite different lines" | p. 9 (nota al pie, ED.) |
| Formulacion | Prueba como correlacion literal de (x+y) y (x−y) para varianzas | NO ENCONTRADO EN EL PDF (se formula con u, v estandarizados; bajo ω = 1 es equivalente algebraicamente) | — |
| Nombre | "Pitman-Morgan test" | NO ENCONTRADO EN EL PDF | — |
| Supuesto | Robustez a no normalidad | NO ENCONTRADO EN EL PDF | — |
| Supuesto | Tamano muestral minimo | NO ENCONTRADO EN EL PDF | — |
| Alcance | Comparacion de coeficientes de variacion | NO ENCONTRADO EN EL PDF | — |
| Alcance | Transformacion logaritmica previa | NO ENCONTRADO EN EL PDF | — |
| Criterio | Unilateral frente a bilateral explicito | NO ENCONTRADO EN EL PDF (solo P{|t| ≤ k}, forma bilateral) | p. 10 |
| Potencia | Analisis de potencia | NO ENCONTRADO EN EL PDF | — |
| Metadatos | DOI impreso | NO ENCONTRADO EN EL PDF | — |
| Referencias | Finney 1938 y De Lury 1938 | "FINNEY, D. J. (1938). Biometrika, 30, 190–2." | p. 12 |
