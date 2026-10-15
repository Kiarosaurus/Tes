# bland1986statistical — Acuerdo entre dos metodos de medicion clinica (Bland y Altman)

- **DOI / URL:** NO ENCONTRADO EN EL PDF (el raw `refs/raw/bland1986statistical.bib` trae `10.1016/S0140-6736(86)90837-8`; el PDF solo imprime "THE LANCET, FEBRUARY 8, 1986" y paginas 307-310)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/bland1986statistical.pdf

## Que hace (3 lineas maximo)
Argumenta que el coeficiente de correlacion no mide el acuerdo entre dos metodos que miden la misma cantidad sin un valor verdadero conocido. Propone graficar la diferencia contra la media de ambos metodos, resumir el acuerdo con el sesgo (media de las diferencias) y los "limites de acuerdo" (media +- 2 DE, o +- 1.96 DE bajo normalidad), con sus IC, y trata la transformacion logaritmica, la repetibilidad y las mediciones repetidas.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; los supuestos relevantes son estadisticos:
- Las diferencias no deben variar sistematicamente con la magnitud: "it was assumed that the differences did not vary in any systematic way" (p. 309). Si la dispersion crece con la media, propone transformacion logaritmica y solo esa.
- La cobertura del 95% de los limites requiere diferencias aproximadamente normales: "If the differences are Normally distributed (Gaussian), 95%" (p. 308). Las mediciones en si no necesitan ser normales.
- El juicio de acuerdo depende de una diferencia aceptable externa al analisis: "How far apart measurements can be ... will be a question of judgment" y "Ideally, it should be defined in advance" (p. 308). El metodo no produce por si solo un veredicto de acuerdo.
- Con promedios de mediciones repetidas por sujeto, la DE de las diferencias queda subestimada: "the standard deviation of the differences will be too small" (p. 310); la correccion publicada es para dos repeticiones por metodo.
- No menciona la prueba de Pitman y Morgan ni ninguna prueba formal de comparacion de varianzas.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Sesgo = media de las diferencias | "the bias, estimated by the mean difference" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Limites de acuerdo = media +- 1.96 DE (aprox. +- 2 DE) | "or, more precisely, between d̄ - 1.96s and d̄ + 1.96s" (simbolo d̄ leido de la imagen; el texto extraido esta corrupto) | Measuring agreement, p. 308 (p. 2 del PDF) |
| 95% de las diferencias dentro de los limites bajo normalidad | "If the differences are Normally distributed (Gaussian), 95%" | Measuring agreement, p. 308 (p. 2 del PDF) |
| EE de los limites aprox. raiz(3 s^2 / n) | "the standard error of d - 2s and d + 2s is about" | Precision of estimated limits of agreement, p. 308 (p. 2 del PDF) |
| IC del 95% con t de n - 1 grados de libertad | "appropriate point of the t distribution with n - 1 degrees of freedom" | Precision of estimated limits of agreement, p. 308 (p. 2 del PDF) |

## Donde entra en mi tesis
Capitulo 3, §Analisis estadistico (`overleaf/secciones/capitulo3.tex`, cierra el `\GAPLIT` de capitulo3-r22): fuente primaria de la lectura de acuerdo descriptiva entre el sintetizador y el protocolo fisico de `peters2025hybrid` sobre los 13 pacientes pareados (DEC 2026-10-15 pto 22, implicancia #185). Respalda: (i) que la correlacion por paciente (r = 0.40 en #185) no mide acuerdo; (ii) la definicion de sesgo y limites de acuerdo; (iii) el grafico diferencia contra media; (iv) los supuestos que hay que verificar antes de reportar limites. No respalda la prueba de Pitman y Morgan (fila 811 de `_candidatos.md` sigue PENDIENTE).

## Dudas para el asesor
- El paper juzga el acuerdo contra una diferencia aceptable "defined in advance". La tesis no tiene una diferencia aceptable fijada para la lectura de acuerdo: basta con declararla descriptiva, o conviene reutilizar el margen del TOST como referencia?
- #185 reporta r(suma, diferencia) = -0.89: la diferencia depende fuertemente de la magnitud, que es justo el supuesto que el paper pide verificar. Se reportan limites en escala logaritmica (razon), como propone el paper, o solo el grafico?
- Con 5 semillas por paciente en el difusor, se usa la media por paciente? El paper advierte que eso subestima la DE de las diferencias y solo da la correccion para dos repeticiones por metodo.
- Con n = 13, los IC de los limites seran anchos (el paper ya los ve anchos con n = 17). Se reportan los IC de los limites?

## Evidencia textual

Paginacion: paginas de la revista 307-310 = paginas 1-4 del PDF. La extraccion de texto del PDF corrompe simbolos (d̄, raiz, +-); donde una frase los contiene, el simbolo se tomo de la imagen de la pagina.

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Alcance | Comparar metodo nuevo con uno establecido | "comparison of a new measurement technique with an established one" | Summary, p. 307 (p. 1 del PDF) |
| Argumento | Correlacion engañosa | "The use of correlation is misleading." | Summary, p. 307 (p. 1 del PDF) |
| Definicion | Valor verdadero desconocido | "The true values remain unknown." | Introduction, p. 307 (p. 1 del PDF) |
| Definicion | Distinto de calibracion | "This is very different from calibration" | Introduction, p. 307 (p. 1 del PDF) |
| Definicion | Ningun metodo es correcto | "neither provides an unequivocally correct measurement" | Introduction, p. 307 (p. 1 del PDF) |
| Argumento | r no es indicador de acuerdo | "as an indicator of agreement. It is no such thing." | Introduction, p. 307 (p. 1 del PDF) |
| Datos | 17 sujetos, dos lecturas por medidor (tabla) | "Two measurements were made with a Wright peak flow meter" | Sample data, p. 307 (p. 1 del PDF); tabla con sujetos 1-17 |
| Datos | Muestra no representativa | "in no way representative of any defined population" | Sample data, p. 307 (p. 1 del PDF) |
| Grafico | Linea de igualdad | "draw the line of equality on which all points would lie" | Plotting data, p. 307 (p. 1 del PDF) |
| Cifra | r = 0.94, p < 0.001 | "For the data in fig 1, r=0.94 (p<0.001)." | Inappropriate use of correlation coefficient, p. 307 (p. 1 del PDF) |
| Argumento (1) | r mide relacion, no acuerdo | "r measures the strength of a relation between two variables, not the agreement" | Inappropriate use of correlation coefficient, p. 307 (p. 1 del PDF) |
| Argumento (1) | Correlacion perfecta con cualquier recta | "perfect correlation if the points lie along any straight line" | Inappropriate use of correlation coefficient, p. 307 (p. 1 del PDF) |
| Argumento (2) | Cambio de escala no afecta r | "A change in scale of measurement does not affect the correlation" | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Cifra | Pendiente 2.0, correlacion 1.0 (calibrador) | "perfect straight line with slope 2.0. The correlation would be 1.0" | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Argumento (3) | r depende del rango | "Correlation depends on the range of the true quantity in the sample." | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Cifra | r = 0.88 bajo 500 l/min; 0.90 sobre | "less than 500 l/min, r is 0.88" | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Argumento (3) | Correlacion alta casi garantizada | "a high correlation is almost guaranteed" | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Argumento (4) | Prueba de significancia irrelevante | "The test of significance is irrelevant to the question of agreement." | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Argumento (5) | Mal acuerdo con r alto | "Data which seem to be in poor agreement can produce quite high correlations." | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Cifra | Edad gestacional 35 sem. frente a 34-39.5; r = 0.85 | "gestations between 34 and 39.5 weeks by the other, but r was high" | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Cifra | Oldham: r 0.992 a 0.996 | "found a correlation of 0.992" | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Argumento | r = 0.94 oculta desacuerdo | "conceals considerable lack of agreement between the two instruments" | Inappropriate use of correlation coefficient, p. 308 (p. 2 del PDF) |
| Criterio | Acuerdo exacto improbable | "It is most unlikely that different methods will agree exactly" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Criterio | Pregunta: cuanto difiere el metodo nuevo | "by how much the new method is likely to differ from the old" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Umbral (ejemplo) | 10 l/min aceptable | "differed by more than, say, 10 l/min" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Umbral (ejemplo) | 100 l/min no aceptable | "if the meters could differ by 100 l/min" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Criterio | Diferencia aceptable es juicio | "will be a question of judgment" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Criterio | Fijarla a priori | "Ideally, it should be defined in advance" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Grafico | Diferencia contra media | "A plot of the difference between the methods against their mean" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Cifra | Discrepancias hasta 80 l/min | "with discrepancies of up to 80 l/min" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Grafico | Media como mejor estimacion del valor verdadero | "the mean of the two measurements is the best estimate we have" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Grafico | No graficar contra un solo metodo | "It would be a mistake to plot the difference against either value" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Definicion | Sesgo = media de diferencias | "the bias, estimated by the mean difference" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Definicion | Ajuste por sesgo consistente | "If there is a consistent bias we can adjust for it" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Cifra | Media de diferencias -2.1; s = 38.8 l/min | "is -2.1 l/min and s is 38.8 l/min" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Definicion | Limites aprox. media +- 2s | "most of the differences to lie between d̄ - 2s and d̄ + 2s" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Supuesto | Normalidad de diferencias da 95% | "If the differences are Normally distributed (Gaussian), 95%" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Definicion | 1.96 DE | "or, more precisely, between d̄ - 1.96s and d̄ + 1.96s" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Supuesto | Por que las diferencias tienden a ser normales | "we have removed a lot of the variation between subjects" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Supuesto | Las mediciones no necesitan ser normales | "The measurements themselves do not have to follow a Normal distribution" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Criterio | Verificar con histograma | "We can check the distribution of the differences by drawing a histogram." | Measuring agreement, p. 308 (p. 2 del PDF) |
| Criterio | Asimetria o colas largas invalidan normalidad | "If this is skewed or has very long tails" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Criterio | Intercambiables si limites no son clinicamente importantes | "Provided differences within d̄ ± 2s would not be clinically important" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Definicion | Nombre "limites de acuerdo" | "We shall refer to these as the \"limits of agreement\"." | Measuring agreement, p. 308 (p. 2 del PDF) |
| Cifra | Limites -79.7 y 75.5 l/min | "d̄ - 2s = -2.1 - (2×38.8) = -79.7 l/min" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Cifra | 80 por debajo o 76 por encima | "may be 80 l/min below or 76 l/min above the large meter" | Measuring agreement, p. 308 (p. 2 del PDF) |
| Criterio | Limites son estimaciones muestrales | "The limits of agreement are only estimates" | Precision of estimated limits of agreement, p. 308 (p. 2 del PDF) |
| Definicion | EE de la media: raiz(s^2/n) | "The standard error of d is √(s²/n)" | Precision of estimated limits of agreement, p. 308 (p. 2 del PDF) |
| Definicion | EE de los limites aprox. raiz(3s^2/n) | "the standard error of d - 2s and d + 2s is about √(3s²/n)" | Precision of estimated limits of agreement, p. 308 (p. 2 del PDF) |
| Definicion | t con n - 1 gl | "t distribution with n - 1 degrees of freedom" | Precision of estimated limits of agreement, p. 308 (p. 2 del PDF) |
| Cifra | EE de la media 9.4 | "The standard error of d̄ is thus 9.4." | Precision of estimated limits of agreement, p. 308 (p. 2 del PDF) |
| Cifra | 16 gl, t = 2.12 | "we have 16 degrees of freedom and t=2.12" | Precision of estimated limits of agreement, pp. 308-309 |
| Cifra | IC95 del sesgo -22.0 a 17.8 l/min | "giving -22.0 to 17.8 l/min" | Precision of estimated limits of agreement, p. 309 (p. 3 del PDF) |
| Cifra | EE del limite 16.3 l/min | "The standard error of the limit d̄ - 2s is 16.3 l/min." | Precision of estimated limits of agreement, p. 309 (p. 3 del PDF) |
| Cifra | IC95 limite inferior -114.3 a -45.1 | "giving -114.3 to -45.1 l/min" | Precision of estimated limits of agreement, p. 309 (p. 3 del PDF) |
| Cifra | IC95 limite superior 40.9 a 110.1 | "the 95% confidence interval is 40.9 to 110.1 l/min" | Precision of estimated limits of agreement, p. 309 (p. 3 del PDF) |
| Criterio | IC anchos por n pequeño | "These intervals are wide, reflecting the small sample size" | Precision of estimated limits of agreement, p. 309 (p. 3 del PDF) |
| Cifra | Oximetria: sesgo 0.42 pp, IC 0.13 a 0.70 | "the mean difference is 0.42 percentage points" | Example showing good agreement, p. 309 (p. 3 del PDF) |
| Cifra | Oximetria: limites -2.0 y 2.8 | "the limits of agreement (-2.0 and 2.8) are small enough" | Example showing good agreement, p. 309 (p. 3 del PDF) |
| Supuesto | Diferencia no sistematica con la magnitud | "it was assumed that the differences did not vary in any systematic way" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Criterio | Dispersion creciente con la media | "The scatter of the differences increases as the VCF increases." | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Criterio | Consecuencia de ignorarlo | "wider apart than necessary for small VCF" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Criterio | Diferencias proporcionales: log | "If the differences are proportional to the mean, a logarithmic transformation" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Cifra | Log: sesgo -0.008; limites -0.226 y 0.243 | "The mean difference is -0.008 on the log scale" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Cifra | Antilogs 0.80 y 1.27 | "If we take the antilogs of these limits we get 0.80 and 1.27." | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Definicion | Antilog = razon adimensional | "is a dimensionless ratio" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Cifra | 20% por debajo a 27% por encima | "by 20% below to 27% above" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Criterio | Solo la transformacion logaritmica | "we do not recommend the use of any other in this context" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Criterio | Relacion compleja: limites conservadores | "limits of agreement which are too far apart rather than too close" | Relation between difference and mean, p. 309 (p. 3 del PDF) |
| Criterio | Repetibilidad limita el acuerdo | "the repeatabilities of two methods of measurement limit the amount of agreement" | Repeatability, p. 309 (p. 3 del PDF) |
| Criterio | Media de diferencias repetidas debe ser cero | "The mean difference should here be zero" | Repeatability, pp. 309-310 |
| Definicion | Coeficiente de repetibilidad (BSI): 2 DE | "We expect 95% of differences to be less than two standard deviations." | Repeatability, p. 310 (p. 4 del PDF) |
| Cifra | Suma de cuadrados 13 479; DE 28.2 l/min (17 pares) | "The sum of the differences squared is 13 479" | Repeatability, p. 310 (p. 4 del PDF) |
| Cifra | Coef. de repetibilidad 56.4 (mini) y 43.2 (grande) | "The coefficient of repeatability is twice this, or 56.4 l/min" | Repeatability, p. 310 (p. 4 del PDF) |
| Alcance | Mas de dos repeticiones: ANOVA, fuera del articulo | "which is beyond the scope of this article" | Repeatability, p. 310 (p. 4 del PDF) |
| Criterio | Promediar repeticiones subestima la DE | "the standard deviation of the differences will be too small" | Measuring agreement using repeated measurements, p. 310 (p. 4 del PDF) |
| Definicion | DE corregida s_c = raiz(s_D^2 + 1/4 s1^2 + 1/4 s2^2) | "The corrected standard deviation of differences, s_c, is" | Measuring agreement using repeated measurements, p. 310 (p. 4 del PDF) |
| Criterio | Aproximacion raiz(2 s_D^2) puede sobreestimar | "this approximation may produce an overestimate" | Measuring agreement using repeated measurements, p. 310 (p. 4 del PDF) |
| Cifra | s_D = 33.2, s1 = 21.6, 28.2 l/min | "For the PEFR we have s_D=33.2, s1=21.6" | Measuring agreement using repeated measurements, p. 310 (p. 4 del PDF). Nota: el impreso rotula 28.2 como s_c, pero la formula lo usa como s2 |
| Cifra | s_c = 37.7 frente a 38.8; aproximacion 47.0 | "or 37.7 l/min. Compare this with the estimate 38.8" | Measuring agreement using repeated measurements, p. 310 (p. 4 del PDF) |
| Argumento | Ni correlacion ni regresion son apropiadas | "neither the correlation coefficient ... nor techniques such as regression analysis are appropriate" (12 palabras con elision) | Discussion, p. 310 (p. 4 del PDF) |
| Alcance | Mismo metodo para repetibilidad u observadores | "to compare measurements by two observers" | Discussion, p. 310 (p. 4 del PDF) |
| Referencia | Version estadistica previa del metodo | "In a statistical journal we have proposed an alternative analysis" | Introduction, p. 307 (p. 1 del PDF); ref. 1 |
| Supuesto | Prueba de Pitman y Morgan | NO ENCONTRADO EN EL PDF | — |
| Supuesto | Prueba formal de normalidad de diferencias (solo histograma) | NO ENCONTRADO EN EL PDF | — |
