# lakens2017equivalence — Equivalence Tests: A Practical Primer (TOST)

- **DOI / URL:** 10.1177/1948550617697177 (impreso en p. 355 del PDF; coincide con `refs/raw/lakens2017equivalence.bib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/lakens2017equivalence.pdf

Nivel de acceso: texto completo (8 paginas, pp. 355-362, incluye figura, tabla, notas y referencias).

Correspondencia con el raw: autor (Daniel Lakens), titulo, revista (Social Psychological and Personality Science), vol. 8(4), pp. 355-362, 2017 y DOI coinciden con la cabecera de p. 355. El campo `note = {PMID: 28736600}` del raw: NO ENCONTRADO EN EL PDF.

## Que hace (3 lineas maximo)
Tutorial del procedimiento TOST (two one-sided tests) para pruebas de equivalencia con t de medias independientes, dependientes, una muestra, correlaciones y meta-analisis.
Da formulas, analisis de potencia (Tabla 1) y recomendaciones para fijar los limites de equivalencia (SESOI) y preespecificarlos.
Clasifica en cuatro escenarios (Figura 1) los resultados de combinar NHST (IC95 vs 0) con equivalencia (IC90 vs limites).

## Restriccion o supuesto clave
No aplica: no es un paper de sintesis generativa. Supuesto metodologico relevante: la decision de equivalencia exige que AMBAS pruebas unilaterales sean significativas ("both one-sided tests need to be significant to declare equivalence", p. 357), y el TOST con alfa = .05 se lee con un IC90 (nota 2, p. 361). La clasificacion de la Figura 1 usa el IC95 (no el IC90) para decidir la diferencia frente a cero (p. 356).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| IC90 para TOST con alfa 5% | "A 90% confidence interval (CI; 1 − 2α) is used instead of a 95% CI" | Notas, nota 2, p. 361 |
| alfa 5% por prueba unilateral | "because two one-sided tests (each with an α of 5%) are performed" | Notas, nota 2, p. 361 |
| cuatro resultados posibles | "there are four possible outcomes of a study" | Testing for Equivalence, p. 356 |

## Donde entra en mi tesis
Capitulo 3 (`overleaf/secciones/capitulo3.tex`), GAPLIT: fuente metodologica para leer el TOST del Objetivo 3 (IC90 [-477.0, -124.9] HU, margen Delta = 196.3 HU; el IC excluye 0 y cruza -Delta). En la taxonomia de Lakens ese patron corresponde al Escenario B de la Figura 1 ("Not Equivalent and Statistically Different", p. 357), no al Escenario D ("undetermined", p. 356), siempre que el IC95 (no solo el IC90) excluya 0.

## Dudas para el asesor
- Lakens reserva "undetermined" (no concluyente) para el caso en que el IC95 incluye 0 y el IC90 incluye un limite (Escenario D, p. 356). El resultado del Objetivo 3 (IC excluye 0, cruza -Delta) es su Escenario B: "statistically different from zero but not statistically equivalent". ¿Se mantiene la etiqueta "no concluyente, a la baja" (que en terminos de Lakens describe solo la parte de equivalencia) o se adopta la formulacion de Lakens?
- La clasificacion de Lakens decide la diferencia con el IC95. ¿Se ha verificado que el IC95 del contraste del Objetivo 3 tambien excluye 0? (El IC90 por si solo no basta para el Escenario B segun p. 356.)
- Lakens no trata la prueba de no-equivalencia (efecto minimo) ni la lectura direccional ("a la baja"); si se quiere afirmar algo mas que "no se demostro equivalencia" hace falta otra fuente.
- El paper recomienda preespecificar los limites (p. 359), pero no dice explicitamente que no deban cambiarse tras ver los datos.

## Respuestas a las preguntas del encargo

1. **Clasificacion combinada NHST + equivalencia.** Si. Cuatro resultados: "statistically equivalent ... and not statistically different from zero", "statistically different from zero but not statistically equivalent", "statistically different from zero and statistically equivalent", o "undetermined (neither statistically different from zero nor statistically equivalent)" (Testing for Equivalence, p. 356). Figura 1 (p. 357): diferencias de medias con IC90 (lineas gruesas) e IC95 (lineas finas), limites Delta_L = -.5 y Delta_U = .5; escenarios A (equivalente y no diferente), B (no equivalente y diferente), C (equivalente y diferente), D (no equivalente y no diferente).
2. **IC que excluye 0 sin quedar dentro de los limites.** Es el Escenario B: el NHST se rechaza "when the CI around the mean difference does not include 0" (p. 356) y la Figura 1 lo rotula "Not Equivalent and Statistically Different" (p. 357); en el dibujo el IC de B cruza el limite inferior. Lakens lo llama "not statistically equivalent" (no se demostro equivalencia); NO demuestra no-equivalencia: la prueba de no-equivalencia / efecto minimo: NO ENCONTRADO EN EL PDF. La etiqueta "undetermined" se reserva para D (IC95 incluye cero, IC90 incluye un limite, p. 356). IC90 con alfa .05: si, nota 2, p. 361; ademas p. 357 permite decidir por IC90 en lugar de p ("Readers are free to replace decisions based on p values by decisions based on 90% CIs").
3. **Fijar limites antes.** Si para la preespecificacion: "it is expected that equivalence bounds are prespecified" (RCT, CONSORT) y "this should also be considered best practice in psychology" (Setting Equivalence Bounds, p. 359); el abstract anuncia "recommendations to prespecify equivalence bounds" (p. 355); la Discusion habla de rechazar efectos "larger than prespecified equivalence bounds" (p. 360). Prohibicion explicita de cambiar los limites tras ver los datos: NO ENCONTRADO EN EL PDF.
4. **¿Cierra el GAPLIT?** Parcialmente. Cubre: la taxonomia de cuatro resultados con figura, el uso del IC90 para TOST con alfa .05 y la preespecificacion de limites. No cubre: (a) el nombre "no concluyente" para el caso IC excluye 0 + cruza un limite (Lakens lo llama "diferente y no equivalente", Escenario B; "undetermined" es otro caso); (b) la lectura direccional "a la baja"; (c) la prohibicion explicita de cambiar Delta post hoc. Para (b) haria falta una fuente sobre pruebas de efecto minimo / no-equivalencia o sobre lectura de IC frente a un margen (p. ej. CONSORT de equivalencia/no inferioridad, piaggio2006reporting, citado en p. 359); para (c) idem o una fuente de preregistro.

## Evidencia textual
| Cifra / umbral / definicion / criterio | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Unica conclusion correcta con p > alfa | "the only formally correct conclusion is that the data are not surprising" | Introduccion, p. 355 |
| Ejemplo p > .05 | "the outcome is a p value larger than the α level (e.g., p > .05)" | Introduccion, p. 355 |
| Limites ejemplo d = -.3 y d = .3 | "effect sizes of Cohen's d = −.3 and d = .3" | Introduccion, p. 355 |
| Definicion TOST: dos hipotesis nulas compuestas | "Two composite null hypotheses are tested: H01: Δ ≤ −ΔL and H02: Δ ≥ ΔU" | Introduccion, p. 355 |
| Criterio de equivalencia | "When both these one-sided tests can be statistically rejected, we can conclude" | Introduccion, p. 355 |
| SESOI ejemplo d = .3 | "a positive or negative difference of d = .3" | Introduccion, p. 355 |
| 108 articulos con "no effect" | "the words "no effect" had been used in 108 articles" | Introduccion, p. 355 |
| 38% aceptan la nula | "a stable average of around 38% of articles with nonsignificant results accept" | Introduccion, p. 355 |
| Error tipo 1 ejemplo 5% | "than our Type 1 error rate (e.g., 5%)" | Testing for Equivalence, p. 356 |
| Ejemplo .3 en escala de 5 puntos | "raw differences such as .3 scale point on a 5-point scale" | Testing for Equivalence, p. 356 |
| Limites simetricos -.3 / .3 | "equivalence bounds can be symmetric around zero (ΔL = −.3 to ΔU = .3)" | Testing for Equivalence, p. 356 |
| Limites asimetricos -.2 / .4 | "or asymmetric (ΔL = −.2 to ΔU = .4)" | Testing for Equivalence, p. 356 |
| Prueba de inferioridad (limite inferior infinito) | "by setting the lower equivalence bound to ∞" | Testing for Equivalence, p. 356 |
| Cuatro resultados posibles NHST + equivalencia | "there are four possible outcomes of a study" | Testing for Equivalence, p. 356 |
| Resultado: diferente sin equivalencia | "statistically different from zero but not statistically equivalent" | Testing for Equivalence, p. 356 |
| Resultado indeterminado | "undetermined (neither statistically different from zero nor statistically equivalent)" | Testing for Equivalence, p. 356 |
| Escenario A: IC90 excluye limites -.5 y .5 | "the 90% CI around the observed mean difference should exclude the ΔL and ΔU" | Testing for Equivalence, p. 356 |
| Escenario B: NHST rechazado | "rejected (Scenario B) when the CI around the mean difference does not include 0" | Testing for Equivalence, p. 356 |
| Escenario C: IC90 y IC95 | "when the 90% CI exclude the equivalence bounds and the 95% CI exclude zero" | Testing for Equivalence, p. 356 |
| Escenario D: indeterminado | "when the 90% CI includes one of the equivalence bounds and the 95% CI includes zero" | Testing for Equivalence, p. 356 |
| Figura 1: IC90, IC95, limites ±.5 | "90% confidence intervals ... and 95% CIs ... with equivalence bounds ΔL = −.5" | Figura 1, p. 357 |
| Figura 1, etiqueta B | "B: Not Equivalent and Statistically Different" | Figura 1, p. 357 |
| Figura 1, etiqueta D | "D: Not Equivalent and Not Different" | Figura 1, p. 357 |
| Decision por IC90 admitida | "Readers are free to replace decisions based on p values by decisions based on 90% CIs" | TOST, p. 357 |
| Criterio de rechazo t | "The two one-sided tests are rejected if tU ≤ −t(df, α), and tL ≥ t(df, α)" | Ecs. 1-4, p. 357 |
| Ejemplo Eskine d = .81, IC95 [0.19, 1.45] | "(d = .81, 95% CI [0.19, 1.45])" | Ejemplo, p. 357 |
| Control n = 95, M = 5.25, SD = .95 | "control: n = 95, M = 5.25, SD = .95" | Ejemplo, p. 357 |
| Organico n = 89, M = 5.22, SD = .83 | "organic food: n = 89, M = 5.22, SD = .83" | Ejemplo, p. 357 |
| Limite con 33% de potencia | "the equivalence bound to the effect size the original study had 33% power" | Ejemplo, p. 357 |
| n = 21, d = .48 | "With n = 21 in each condition ... the equivalence bound is d = .48" | Ejemplo, p. 357 |
| .384 en escala de 7 puntos, SD .894 | "a difference of .384 on a 7-point scale ... pooled SD of .894" | Ejemplo, p. 357 |
| tL = 3.14, tU = -2.69 | "= tL = 3.14 and ... = tU = −2.69" | Ejemplo, p. 357 |
| p = .001 y .004 | "which correspond to p values of .001 and .004" | Ejemplo, p. 357 |
| Resultado t(182) = -2.69, p = .004 | "the equivalence test is significant, t(182) = −2.69, p = .004" | Ejemplo, p. 357 |
| Ambas pruebas deben ser significativas | "both one-sided tests need to be significant to declare equivalence" | Ejemplo, p. 357 |
| Se reporta la prueba con mayor p | "only the one-sided test with the highest p value is reported" | Ejemplo, p. 357 |
| Tabla 1: limite 0.1 | "1,713 2,604 2,165 3,155 | 1,713 2,604 2,165 3,155" | Tabla 1, p. 358 |
| Tabla 1: limite 0.2 | "429 651 542 789 | 429 652 542 789" | Tabla 1, p. 358 |
| Tabla 1: limite 0.3 | "191 290 241 351 | 191 291 242 351" | Tabla 1, p. 358 |
| Tabla 1: limite 0.4 | "108 163 136 198 | 108 165 136 199" | Tabla 1, p. 358 |
| Tabla 1: limite 0.5 | "69 105 87 127 | 70 106 88 128" | Tabla 1, p. 358 |
| Tabla 1: limite 0.6 | "48 73 61 88 | 49 74 61 89" | Tabla 1, p. 358 |
| Tabla 1: limite 0.7 | "35 54 45 65 | 36 55 45 66" | Tabla 1, p. 358 |
| Tabla 1: limite 0.8 | "27 41 34 50 | 28 43 35 51" | Tabla 1, p. 358 |
| Tabla 1: columnas (potencia 80/90%, alfa .05/.01; aprox. vs exacto) | "80% Power ... 90% Power ... α = .05 ... α = .01" | Tabla 1, p. 358 |
| Ejemplo limites simetricos ±.5 para potencia | "(e.g., ΔL = −.5 and ΔU = .5), the required sample sizes" | Potencia, p. 358 |
| Equivalencia requiere muestras algo mayores | "Equivalence tests require slightly larger sample sizes than traditional null hypothesis tests" | Potencia, p. 358 |
| 176 participantes, d = .3, 80% | "176 participants are required in each condition to achieve 80% power for d = .3" | Medias dependientes, p. 358 |
| dz = .212 | "a study has 80% power for a Cohen's dz of .212" | Medias dependientes, p. 358 |
| Factor raiz de 2 | "The relationship between d and dz is a factor of √2" | Medias dependientes, p. 358 |
| Benchmarks d .2/.5/.8 y dz .14/.35/.57 | "small (.2), medium (.5), and large (.8) ... small (.14), medium (.35), and large (.57)" | Medias dependientes, p. 358 |
| r = .5 iguala d y dz | "This assumes r = .5, when Cohen's d and Cohen's dz are identical" | Medias dependientes, p. 358 |
| Benchmarks de correlacion | "are r = .1, r = .3, and r = .5" | Correlaciones, p. 359 |
| Criterio de rechazo Z | "The two one-sided tests are rejected if ZL ≤ −Zα and ZU ≥ Zα" | Correlaciones, p. 359 |
| Limites estrechos en meta-analisis | "(e.g., ΔL = −.1 and ΔU = .1)" | Meta-analisis, p. 359 |
| Criterio IC90 en meta-analisis | "If the 90% CI falls within the equivalence bounds, ... statistically equivalent" | Meta-analisis, p. 359 |
| 100 participantes, 80%, alfa .05 | "e.g., 100 participants in each between-subject condition" | Setting Equivalence Bounds, p. 359 |
| SESOI Delta = 0.389 | "the SESOI in a null effect significance test is Δ = 0.389" | Setting Equivalence Bounds, p. 359 |
| Limites ±0.414 | "80% power is achieved when ΔL = −0.414 and ΔU = 0.414" | Setting Equivalence Bounds, p. 359 |
| Regla regulatoria 20% | "(e.g., differences up to 20% are not considered to be clinically relevant)" | Setting Equivalence Bounds, p. 359 |
| Preespecificacion de limites | "it is expected that equivalence bounds are prespecified (e.g., CONSORT guidelines" | Setting Equivalence Bounds, p. 359 |
| Preespecificar como buena practica | "this should also be considered best practice in psychology" | Setting Equivalence Bounds, p. 359 |
| Reportar limites en el abstract | "the abstract should also include the equivalence bounds that are used" | Setting Equivalence Bounds, p. 359 |
| 60 participantes, 33% potencia, d = .4 | "60 participants ... has 33% power to detect an effect of d = .4" | Setting Equivalence Bounds, p. 360 |
| 2.5 veces la muestra original | "limits the sample size ... to 2.5 times the sample size of the original" | Setting Equivalence Bounds, p. 360 |
| Limites "preespecificados" (Discusion) | "reject effects larger than prespecified equivalence bounds" | Discusion, p. 360 |
| Control de error al alfa en el limite | "Error rates ... are controlled at the α level when the true effect equals" | Discusion, p. 360 |
| IC mas ancho que los limites en muestras pequenas | "the CI will always be so wide that it is necessarily wider than" | Discusion, p. 360 |
| Ejemplo 0.2 en escala de 7, IC90 [-0.13; 0.17] | "a difference of 0.2 on a 7-point scale with 90% CI [−0.13;0.17]" | Discusion, p. 360 |
| Limites de replicacion ±.1 o ±.05 | "ΔL = −.1 and ΔU = .1 or even ΔL = −.05 and ΔU = .05" | Discusion, p. 361 |
| IC90 = 1 − 2 alfa | "A 90% confidence interval (CI; 1 − 2α) is used instead of a 95% CI" | Nota 2, p. 361 |
| Alfa 5% por cada prueba unilateral | "two one-sided tests (each with an α of 5%) are performed" | Nota 2, p. 361 |
| Lectura "no concluyente" del caso IC excluye 0 y cruza un limite | NO ENCONTRADO EN EL PDF | — |
| Prueba de no-equivalencia / efecto minimo; lectura direccional ("a la baja") | NO ENCONTRADO EN EL PDF | — |
| Prohibicion explicita de cambiar limites tras ver los datos | NO ENCONTRADO EN EL PDF | — |
| PMID 28736600 (campo del raw) | NO ENCONTRADO EN EL PDF | — |
