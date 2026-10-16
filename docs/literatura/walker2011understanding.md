# walker2011understanding — Understanding Equivalence and Noninferiority Testing (Walker y Nowacki, JGIM 2011)

- **DOI / URL:** 10.1007/s11606-010-1513-8 (impreso en p. 192 del PDF; coincide con `DO` y `UR` de `refs/raw/walker2011understanding.ris`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/walker2011understanding.pdf

Verificacion contra el raw: titulo, autores (Walker, Esteban; Nowacki, Amy S.), revista (J Gen Intern Med), volumen 26(2), paginas 192-196 y DOI coinciden con la cabecera del PDF ("J Gen Intern Med 26(2):192–6", p. 192). Diferencia: el PDF trae "© Society of General Internal Medicine 2010" y "Published online September 21, 2010" (p. 192); el raw trae PY 2011 / DA 2011/02/01. Es fecha de version en linea frente a fecha del numero, no contradiccion.

## Que hace (3 lineas maximo)
Tutorial para clinicos sobre pruebas de equivalencia y no inferioridad: invierte las hipotesis del contraste clasico,
define el margen de equivalencia delta, presenta el procedimiento TOST con IC (1-2alfa)x100%, y discute la eleccion
del margen, por que "no diferencia" no implica equivalencia, tamano muestral, medida de efecto, ITT/PP y reporte.

## Restriccion o supuesto clave
No aplica: no es un paper de sintesis generativa. Supuesto metodologico relevante: la regla de decision es binaria;
la equivalencia se establece solo si el IC (1-2alfa) cae entero dentro de (-delta, delta). Frase: "equivalence is
established ... if a (1–2α) × 100% confidence interval ... is contained within the interval (-δ, δ)" (Procedure, p. 193).
Todo lo demas se rotula "Equivalence not established" (Figura 1, p. 193); el paper no nombra una tercera categoria
"inconclusa".

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto (fuente metodologica para la lectura del TOST del Objetivo 3)

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| IC (1-2alfa)x100% | "if a (1–2α) × 100% confidence interval for the difference" | Procedure, p. 193 |
| IC90 <-> alfa = 0.05 | "using a 90% confidence interval yields a 0.05 significance level" | Procedure, p. 193 |
| Margen antes de los datos | "should be determined before the data is recorded" | Equivalence Margin, p. 194 |

## Donde entra en mi tesis
Capitulo 3 (`overleaf/secciones/capitulo3.tex`), GAPLIT sobre la lectura del IC90 del TOST del Objetivo 3
(IC90 [-477.0, -124.9] HU frente a Delta = 196.3 HU; lectura adoptada "no concluyente, a la baja", segun
`docs/01-decisiones.md` 2026-10-15 pto 15 y 2026-10-15 (3) pto 1).

Respuestas al encargo:

1. **Figura de escenarios de IC frente al margen.** Si: la Figura 1 (p. 193), panel "Equivalence study", muestra tres
   IC frente a -δ, 0, +δ. Uno dentro de (-δ, δ) rotulado "Equivalence established"; los otros dos, cada uno cruzando
   uno de los limites (uno -δ, otro +δ), rotulados ambos "Equivalence not established". **No usa la palabra
   "inconclusive" ni equivalente** (termino "inconclusive/inconclusa": NO ENCONTRADO EN EL PDF). No hay un escenario
   "IC completamente fuera del margen = no equivalente" como categoria distinta: la dicotomia es established / not
   established. La lectura mas cercana a "no concluyente" esta en texto: "If the evidence in favor of equivalence is
   not strong enough, nonequivalence cannot be ruled out" (Introduction, p. 192). Ojo: en la Figura 2 (p. 195,
   adaptada de Barker et al.) la columna "Conclusion" rotula el caso Asian como "not equivalent", mientras el texto
   dice "TOST does not conclude equivalence" (p. 194); el paper usa ambas formulas sin distinguirlas. Un escenario
   especifico "IC que excluye 0 y cruza un limite" (el de esta tesis): NO ENCONTRADO EN EL PDF como caso nombrado o
   discutido (no se puede afirmar desde la figura si alguno de los IC dibujados excluye 0).
2. **IC90 / (1-2alfa).** Si, explicito: "(1–2α) × 100% confidence interval" (p. 193) y "using a 90% confidence
   interval yields a 0.05 significance level for testing equivalence" (p. 193); se repite en Reporting of Results
   (p. 196). Justificacion: "tantamount to performing two one-sided tests" (p. 193).
3. **Margen fijado antes y su justificacion.** Si: "the value of the equivalence margin should be determined before
   the data is recorded" para "maintain the type I error at the desired level" (p. 194). Justificacion: "maximum
   clinically acceptable difference" (p. 192); debe justificarse con "relevant evidence and sound clinical
   considerations" (p. 194); en ensayos clinicos, fraccion f del margen de superioridad frente a placebo
   (meta-analisis), p. 194. Exige "Clear statement and justification of the equivalence margin" (p. 195).
4. **Basta para cerrar el GAPLIT?** Parcialmente. Respalda: IC90 para TOST con alfa = 0.05, margen pre-especificado,
   y que un IC que cruza un limite = "equivalence not established", con la lectura asimetrica "nonequivalence cannot
   be ruled out". **No respalda** el rotulo "no concluyente" como categoria con nombre propio, ni la lectura
   direccional "a la baja" (IC que excluye 0 pero cruza -Δ). Ademas, la Figura 2 rotula un caso analogo como
   "not equivalent", lo que puede leerse en contra del rotulo "no concluyente". Falta una fuente que distinga
   explicitamente los escenarios (dentro / fuera / cruzando un limite) y nombre el caso cruzado como inconcluso
   o indeterminado; candidatos citados por el propio paper: Piaggio et al. 2006 (extension CONSORT, ref. 16) y
   Kaul y Diamond 2006 (ref. 6), ademas de `lakens2017equivalence` (ya en `refs/raw/`, sin leer aqui).

## Dudas para el asesor
- El paper solo ofrece "equivalence not established" / "nonequivalence cannot be ruled out". Es aceptable citarlo
  como respaldo de "no concluyente" o hay que restringir la frase de la tesis a "equivalencia no establecida"?
- La Figura 2 usa "not equivalent" para un IC que no cae dentro del margen. Conviene evitar que la tesis lo cite
  para el rotulo "no concluyente"?
- La direccion "a la baja" (IC que excluye 0) no esta tratada en este paper: requiere otra fuente o se presenta
  como lectura descriptiva propia?

## Evidencia textual
| Cifra / umbral / definicion / criterio | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| alfa habitual 0.05 | "its value is frequently set at 0.05 or lower" | Introduction, p. 192 |
| Definicion error tipo I | "This error is called the type I error" | Introduction, p. 192 |
| Hipotesis de equivalencia invertidas | "simply those of a traditional comparative study reversed" | Introduction, p. 192 |
| Lectura cuando no se establece equivalencia | "nonequivalence cannot be ruled out" | Introduction, p. 192 |
| Definicion margen de equivalencia | "the margin is the maximum clinically acceptable difference" | Introduction, p. 192 |
| Notacion delta | "The equivalence margin, denoted by δ" | Introduction, p. 192 |
| Criterio de equivalencia | "its efficacy is within δ units from that of the current therapy" | Introduction, p. 192 |
| Ejemplo HIV: 562 pacientes | "a clinical trial in 562 HIV patients" | Introduction, p. 192 |
| Endpoint 400 copias/ml, semana 48 | "HIV RNA level of 400 copies/ml or less at week 48" | Introduction, p. 192 |
| delta = 12 puntos porcentuales | "was set at δ=12 percentage points" | Introduction, p. 192 |
| Criterio de no inferioridad | "no more than δ units less than that of the current therapy" | Introduction, p. 192 |
| delta = 0 reduce a superioridad | "δ=0, then the problem simplifies to a traditional one-sided superiority test" | Introduction, p. 192 |
| TOST, regla con IC (1-2alfa) | "(1–2α) × 100% confidence interval ... is contained within the interval (-δ, δ)" | Procedure, p. 193 |
| Por que 1-2alfa | "tantamount to performing two one-sided tests" | Procedure, p. 193 |
| IC90 <-> alfa 0.05 | "using a 90% confidence interval yields a 0.05 significance level" | Procedure, p. 193 |
| Extension a otros parametros | "extended to testing equivalency in other parameters like means" | Procedure, p. 193 |
| Tasas 50.8% y 51.3% | "the response rates were 50.8% and 51.3%" | Procedure, p. 193 |
| IC95 (-9, 8) dentro de (-12, 12) | "95% confidence interval ... was (-9, 8)" | Procedure, p. 193 |
| Equivalencia a nivel 0.025 | "declared equivalent at the 0.025 significance level" | Procedure, p. 193 |
| Regla de no inferioridad | "lower limit of a (1–2α) × 100% confidence interval ... is above -δ" | Procedure, p. 193 |
| OASIS-5: resultado a 9 dias | "refractory ischemia at 9 days after acute coronary syndrome" | Procedure, p. 193 |
| Margen RR 1.185 (meta-analisis) | "the noninferiority margin for the relative risk was set at 1.185" | Procedure, p. 193 |
| 18.5% mayor | "at most, 18.5% higher than the true risk" | Procedure, p. 193 |
| Riesgos 5.8% y 5.7%, RR 1.01 (0.90, 1.13) | "were 5.8% and 5.7% [RR=1.01, 95% confidence interval (0.90, 1.13)]" | Procedure, p. 193 |
| Sangrado RR 0.52 (0.44, 0.61) | "RR=0.52, 95% confidence interval (0.44, 0.61)" | Procedure, p. 193 |
| Figura 1, caso dentro del margen | "Equivalence established" | Figura 1, p. 193 |
| Figura 1, casos que cruzan un limite | "Equivalence not established" | Figura 1, p. 193 |
| Tabla 1, hipotesis nula de equivalencia | "The therapies are not equivalent" | Tabla 1, p. 193 |
| p-valor de equivalencia | "reported as the larger of the two p-values" | Procedure, p. 194 |
| Recomendacion de reporte | "report both a confidence interval and the p-value" | Procedure, p. 194 |
| Margen: paso mas critico | "the most critical step in equivalence/noninferiority testing" | Equivalence Margin, p. 194 |
| Justificacion del margen | "justified in terms of relevant evidence and sound clinical considerations" | Equivalence Margin, p. 194 |
| Fraccion f del IC frente a placebo | "set the value of δ to a fraction, f, of the lower limit" | Equivalence Margin, p. 194 |
| f = 0.50 (FDA, mortalidad) | "the FDA has suggested a value of f of 0.50" | Equivalence Margin, p. 194 |
| Margen fijado antes | "should be determined before the data is recorded" | Equivalence Margin, p. 194 |
| Motivo: error tipo I | "essential to maintain the type I error at the desired level" | Equivalence Margin, p. 194 |
| No diferencia no implica equivalencia | "a nonsignificant result implies only that equivalency ... cannot be ruled out" | No Difference..., p. 194 |
| Barker: margen 5 puntos, alfa 0.05 | "α=0.05 and an equivalence margin of 5 percentage points" | No Difference..., p. 194 |
| 3 grupos, 7 vacunas | "three minority groups (Black, Hispanic, and Asian) for seven different vaccines" | No Difference..., p. 194 |
| 9 de 21 contradictorios | "yielded contradictory results in 9 out of 21 comparisons" | No Difference..., p. 194 |
| Regla clasica IC95 vs TOST IC90 | "rejected if a 95% confidence interval does not cover zero" | No Difference..., p. 194 |
| Intervalo (-0.05, 0.05) | "the 90% confidence interval is included within (-0.05, 0.05)" | No Difference..., p. 194 |
| Caso Asian en texto | "TOST does not conclude equivalence" | No Difference..., p. 194 |
| Caso Asian en figura | "not equivalent" | Figura 2, p. 195 |
| Figura 2, delta = 5 | "two one-sided test (TOST) (δ=5) procedures" | Figura 2 (leyenda), p. 195 |
| Definicion potencia | "Power is the probability of correctly establishing the research hypothesis" | Sample Size, p. 194 |
| n = 562, potencia 0.80, delta 12 | "n=562 gave the abacavir-indinavir trial a power of approximately 0.80" | Sample Size, p. 194 |
| n = 1,300 para delta 8 | "a sample of n=1,300 would have been required" | Sample Size, p. 195 |
| Eficacias supuestas 33% y 28% | "true efficacies are 33% and 28%" | Sample Size, p. 195 |
| Tabla 2: potencia 0.80, alfa 0.05 | "Sample Size to Achieve 0.80 Power ... at the α=0.05" | Tabla 2, p. 195 |
| Tabla 2: margen 0.06 -> 26,185 | "0.06 26,185" | Tabla 2, p. 195 |
| Tabla 2: margen 0.07 -> 6,547 | "0.07 6,547" | Tabla 2, p. 195 |
| Tabla 2: margen 0.08 -> 2,910 | "0.08 2,910" | Tabla 2, p. 195 |
| Tabla 2: margen 0.09 -> 1,637 | "0.09 1,637" | Tabla 2, p. 195 |
| Tabla 2: margen 0.10 -> 1,048 | "0.10 1,048" | Tabla 2, p. 195 |
| Tabla 2: margen 0.11 -> 728 | "0.11 728" | Tabla 2, p. 195 |
| Tabla 2: margen 0.12 -> 535 | "0.12 535" | Tabla 2, p. 195 |
| Medida de efecto fijada desde el inicio | "critical to determine the measure to be used from the outset" | Measure of Effect, p. 195 |
| ITT anticonservador en equivalencia | "ITT makes it easier to establish equivalency/noninferiority" | Analysis of Data, p. 195 |
| Criterio ITT y PP concordantes | "clearly established when both ITT and PP analyses agree" | Analysis of Data, p. 195 |
| Criterio de reporte: margen | "Clear statement and justification of the equivalence margin" | Reporting of Results, p. 195 |
| Criterio de reporte: IC 1-2alfa | "correct procedure to test equivalence at significance level α ... (1–2α)" | Reporting of Results, p. 196 |
| Le Henanff: 162 informes 2003-2004 | "identified 162 reports of equivalence/noninferiority trials" | Conclusions, p. 196 |
| 80% sin justificar margen | "about 80% of the reports did not justify their choice" | Conclusions, p. 196 |
| 28% sin margen en tamano muestral | "28% did not take into consideration the margin" | Conclusions, p. 196 |
| Termino "inconclusive" para IC que cruza un limite | NO ENCONTRADO EN EL PDF | — |
| Caso "IC excluye 0 y cruza un limite" tratado explicitamente | NO ENCONTRADO EN EL PDF | — |
