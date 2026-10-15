# morgan1939test — Prueba de igualdad de las dos varianzas en una muestra normal bivariada

- **DOI / URL:** https://doi.org/10.1093/biomet/31.1-2.13
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/morgan1939test.pdf

## Que hace (3 lineas maximo)
Deriva por razon de verosimilitud (Neyman-Pearson) una prueba de $\sigma_1=\sigma_2$ para $n$ pares $(x,y)$ de una normal bivariada con $\rho_{12}$ desconocida. Con $X=\tfrac12(x+y)$, $Y=\tfrac12(x-y)$, la hipotesis equivale a $\rho_{XY}=0$; se refiere $t=r_{XY}\sqrt{n-2}/\sqrt{1-r_{XY}^2}$ a Student con $n-2$ gl. Calcula la potencia y la compara con el cociente de varianzas de Finney.

## Restriccion o supuesto clave
Supone normalidad bivariada de los pares (ec. 1, p. 13). La distribucion nula es independiente de $\rho_{12}$, pero la potencia depende de ella. Prueba igualdad de **varianzas**, no de coeficientes de variacion: el PDF no trata CV ni medias distintas entre brazos. No es paper de sintesis generativa: no aplica la pregunta sobre implantes.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| gl $= n-2$ | "to "Student's" distribution with degrees of freedom f = n - 2" | §1, p. 15 (p. 3 del PDF) |
| $\lambda=(1-r_{XY}^2)^{n/2}$ (ec. 19) | "Hence the likelihood criterion of (12b) is seen to be" | §1, p. 15 (p. 3 del PDF) |

## Donde entra en mi tesis
Cap. 3, §Analisis estadistico (`\GAPLIT` de capitulo3-r22, DEC 2026-10-15 pto 22, #185): fuente primaria de la prueba de varianzas pareadas implementada como correlacion entre $(x+y)$ y $(x-y)$ con $t$ de $n-2$ gl (13 pacientes, difusor frente a Peters). Morgan respalda: la derivacion como razon de verosimilitud, la reduccion a $\rho_{XY}=0$ via suma y diferencia, el estadistico $t$, los gl, la regla bilateral y la independencia nula respecto de $\rho_{12}$. Morgan NO respalda: la denominacion "Pitman-Morgan" ni ninguna contribucion de Pitman (Pitman no figura en sus referencias, p. 19); la comparacion de CV; la robustez ante no normalidad; un ejemplo con datos reales. La reduccion a suma y diferencia con $\rho_{XY}$ debe atribuirse a Morgan en este PDF; lo que aporte Pitman 1939 debe salir de su propia ficha.

## Dudas para el asesor
- La cifra reportada es CV (0.076 frente a 0.241), pero la prueba de Morgan contrasta $\sigma_1=\sigma_2$. Si la prueba se aplico sobre valores crudos y las medias de los brazos difieren, el p = 3.8e-5 contrasta varianzas, no CV. Se aplico sobre valores normalizados (p. ej. por la media del brazo, o log)? Conviene declararlo.
- Con $n=13$, se verifico o se discute la normalidad bivariada que exige la derivacion?
- La prueba es bilateral en el PDF; se reporta bilateral el p = 3.8e-5?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Supuesto | Muestra de pares de una normal bivariada | "A sample of n pairs of variables (x, y) has been drawn" | §1, p. 13 (p. 1 del PDF) |
| Supuesto | Densidad normal bivariada | "from the bivariate normal distribution whose probability law is" | §1, p. 13 (p. 1 del PDF) |
| Contexto | Criterio previo de Finney: cociente de varianzas | "What is the probability law of the ratio, ω" | §1, p. 13 (p. 1 del PDF) |
| Limitacion del previo | Cociente depende de $\rho_{12}$ | "dependent on the population correlation ρ12, which will be in general unknown" | §1, p. 13 (p. 1 del PDF) |
| Objetivo | Criterio libre de parametros no especificados | "whose sampling distribution will be independent of ρ12" | §1, p. 13 (p. 1 del PDF) |
| Metodo | Razon de verosimilitud de Neyman-Pearson | "The likelihood ratio method of approach of Neyman and Pearson" | §1, pp. 13-14 (pp. 1-2 del PDF) |
| Definicion | Varianzas muestrales con divisor $n$ (ec. 7) | "s1² = Σ(xi − x̄)²/n" | §1(a), p. 14 (p. 2 del PDF) |
| Definicion | Hipotesis contrastada | "obtained by putting σ1 = σ2 = σ in (6)" | §1(c), p. 14 (p. 2 del PDF) |
| Estadistico | Criterio de razon de verosimilitud (ec. 12a-b) | "The likelihood ratio criterion is then" | §1(e), p. 14 (p. 2 del PDF) |
| Criterio | Direccion de evidencia | "less and less likely as λ moves from 1 to 0" | §1(f), p. 14 (p. 2 del PDF) |
| Transformacion | Suma y diferencia (ec. 13-14) | "Write x = X+Y, y = X−Y" ; "X = ½(x+y), Y = ½(x−y)" | §1, p. 15 (p. 3 del PDF) |
| Equivalencia | Igualdad de varianzas sii correlacion nula (ec. 16) | "necessary and sufficient condition ... σ1 = σ2, is that ρXY = 0" | §1, p. 15 (p. 3 del PDF) |
| Estadistico | Correlacion muestral de las transformadas | "the sample correlation coefficient between the transformed variables, i.e. rXY" | §1, p. 15 (p. 3 del PDF) |
| Distribucion nula | Ley de $r_{XY}$ bajo $\rho_{XY}=0$ (ec. 17) | "this coefficient has the well-known probability law" | §1, p. 15 (p. 3 del PDF) |
| Formula | $r_{XY}=(s_1^2-s_2^2)/\{(s_1^2+s_2^2)^2-4r_{12}^2s_1^2s_2^2\}^{1/2}$ (ec. 18) | "Making use of the transformations (14), it is found that" | §1, p. 15 (p. 3 del PDF) |
| Relacion RV-correlacion | $\lambda=(1-r_{XY}^2)^{n/2}$ (ec. 19) | "Hence the likelihood criterion of (12b) is seen to be" | §1, p. 15 (p. 3 del PDF) |
| Estadistico | $t=r_{XY}\sqrt{n-2}/\sqrt{1-r_{XY}^2}$ (ec. 20) | "or (b) alternatively referring" [seguido de ec. 20] | §1, p. 15 (p. 3 del PDF) |
| gl | Student con $n-2$ | "to "Student's" distribution with degrees of freedom f = n − 2" | §1, p. 15 (p. 3 del PDF) |
| Regla | Bilateral, por valor absoluto | "rejecting the hypothesis when \|rXY\| or \|t\| fall beyond" | §1, p. 15 (p. 3 del PDF) |
| Propiedad | Nula independiente de $\rho_{12}$ | "The test ... is independent of the unknown correlation ρ12" | §1, p. 15 (p. 3 del PDF) |
| Potencia | Depende de $\rho_{12}$ | "detect real differences between σ1 and σ2 will depend on the value of ρ12" | §2, p. 15 (p. 3 del PDF) |
| Umbral | $\alpha$ de ejemplo | "where α, for example, equals 0·05" | §2, p. 15 (p. 3 del PDF) |
| Definicion | Hipotesis en terminos de cociente $\gamma$ (ec. 22) | "γ = σ1/σ2 = 1" | §2, p. 16 (p. 4 del PDF) |
| Formula | $\rho_{XY}$ en funcion de $\gamma$ y $\rho_{12}$ (ec. 24) | "a relation similar to (18) holds between ρXY, γ = σ1/σ2 and ρ12" | §2, p. 16 (p. 4 del PDF) |
| Propiedad | Simetria $\gamma$ vs $\gamma^{-1}$ | "as likely to reject ... when σ1 = 2σ2 as when σ1 = ½σ2" | §2, p. 16 (p. 4 del PDF) |
| Configuracion | Curvas de potencia (Fig. 1) | "taking α = 0·10 and sample size n = 25" | §2, p. 16 (p. 4 del PDF) |
| Configuracion | Valores de $\rho_{12}$ en Fig. 1 | "ρ12 = 0, ρ12 = 0·5, and ρ12 = 0·8" | §2, p. 16 (p. 4 del PDF) |
| Resultado | Mas potencia con $\rho_{12}$ alta | "the test is more powerful when ρ12 is large" | §2, p. 16 (p. 4 del PDF) |
| Umbral | Corte bilateral para $n=25$, $\alpha=0.10$ | "for the case n = 25, when \|rXY\| > 0·3365" | Nota al pie, p. 16 (p. 4 del PDF) |
| Configuracion | Tamanos tabulados | "for this case of n = 25 and also for n = 12 and n = 100" | §2, p. 16 (p. 4 del PDF) |
| Cifra | Potencia, $n=12$, $\rho_{XY}=0.4$, prueba (a) | tabla: "0·379" (fila $\rho_{XY}$ 0·4, columna n = 12, Test (a)) | Tabla, p. 18 (p. 6 del PDF) |
| Cifra | Potencia, $n=12$, $\rho_{XY}=0.6$, prueba (a) | tabla: "0·710" | Tabla, p. 18 (p. 6 del PDF) |
| Cifra | Potencia, $n=12$, $\rho_{XY}=0.8$, prueba (a) | tabla: "0·965" | Tabla, p. 18 (p. 6 del PDF) |
| Cifra | Potencia, $n=25$, $\rho_{XY}=0.6$, prueba (a) | tabla: "0·953" | Tabla, p. 18 (p. 6 del PDF) |
| Cifra | Potencia, $n=100$, $\rho_{XY}=0.2$, prueba (a) | tabla: "0·642" | Tabla, p. 18 (p. 6 del PDF) |
| Cifra | $\gamma$ para $\rho_{XY}=0.6$ con $\rho_{12}=0$ / 0.5 / 0.8 | tabla: "2·00" / "1·84" / "1·55" | Tabla, p. 18 (p. 6 del PDF) |
| Contexto | Con $\rho_{12}$ conocida, RV no depende solo de $\omega$ (ec. 25) | "This is not solely a function of Finney's criterion ω" | §3, p. 17 (p. 5 del PDF) |
| Limitacion | Distribucion de ec. 25 no obtenida | "I have not succeeded in determining the sampling distribution of the λ of (25)" | §3, p. 17 (p. 5 del PDF) |
| Comparacion | $\rho_{12}=0$: mejor el cociente de varianzas | "the test based on ω or the ratio of sample variances is the better" | §3, p. 19 (p. 7 del PDF) |
| Comparacion | $\rho_{12}$ conocida: $\omega$ ligeramente mejor | "when ρ12 is known, the ω test is slightly the better" | §3, p. 19 (p. 7 del PDF) |
| Recomendacion | $\rho_{12}$ desconocida: usar $r_{XY}$ | "the rXY of (18) appears the appropriate test criterion to use" | §3, p. 19 (p. 7 del PDF) |
| Atribucion | Mencion de Pitman | NO ENCONTRADO EN EL PDF | Referencias, p. 19 (p. 7 del PDF) |
| Atribucion | Nombre "Pitman-Morgan" | NO ENCONTRADO EN EL PDF | — |
| Alcance | Comparacion de coeficientes de variacion | NO ENCONTRADO EN EL PDF | — |
| Alcance | Robustez ante no normalidad | NO ENCONTRADO EN EL PDF | — |
| Alcance | Prueba unilateral | NO ENCONTRADO EN EL PDF | — |
| Alcance | Ejemplo numerico con datos reales | NO ENCONTRADO EN EL PDF | — |
