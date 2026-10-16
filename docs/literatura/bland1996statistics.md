# bland1996statistics — Statistics Notes: Measurement error proportional to the mean (Bland y Altman, BMJ 1996)

- **DOI / URL:** NO ENCONTRADO EN EL PDF (el PDF solo imprime "BMJ 1996;313:106"; el DOI 10.1136/bmj.313.7049.106 viene del raw `refs/raw/bland1996statistics .bib`, con espacio en el nombre)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/bland1996statistics.pdf

> Correspondencia raw/PDF: el PDF es una sola pagina (BMJ vol. 313, p. 106, 13 julio 1996) y
> contiene SOLO la nota "Measurement error proportional to the mean". NO contiene la nota
> "Logarithms" (BMJ 312:700), que aparece unicamente como referencia 3 del PDF. El raw que
> corresponde es `refs/raw/bland1996statistics .bib` (Bland106), no `refs/raw/bland1996statistics.bib` (Bland700).
> La pagina incluye ademas, arriba, el final de un articulo ajeno sobre la edicion nigeriana del BMJ; no se ficha.

## Que hace (3 lineas maximo)
Con mediciones duplicadas de cotinina salival en 20 escolares muestra que la DE intra-sujeto crece con la media,
lo detecta (Kendall tau, pendiente log DE vs log media) y lo resuelve con transformacion logaritmica. Antilogaritmando
la DE intra-sujeto en log obtiene un factor multiplicativo (DE geometrica) y, si es pequena, su exceso sobre 1 aproxima el CV intra-sujeto.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; no aplica la pregunta sobre implantes. Supuestos relevantes:
la aproximacion "a_sigma_w - 1 ~ CV" exige que la DE "is not large compared with the level of the measurement" (p. 106);
con CV = 49.6% los autores la declaran "too large for the approximation to be reliable" (p. 106).
Los logaritmos usados en el ejemplo son en base 10 (leyenda de Fig 2: "after log10 transformation").
El analisis es de error de medicion intra-sujeto (duplicados de un mismo metodo), no de concordancia entre dos metodos.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| a_sigma_w - 1 ~ CV (condicional) | "a_sigma_w - 1 is approximately equal to the standard deviation expressed as a proportion" | p. 106, col. derecha |
| Condicion de validez | "Provided the standard deviation is not large compared with the level of the measurement" | p. 106, col. derecha |
| CV = 49.6% (aproximacion no fiable) | "This is rather too large for the approximation to be reliable." | p. 106, col. derecha |

## Donde entra en mi tesis
Cap. 3 (`overleaf/secciones/capitulo3.tex`), GAPLIT de la varianza del logaritmo y la prueba de Pitman-Morgan sobre ln
(implicancia #189: Bland-Altman en razon/log). Respalda parcialmente: transformar a log cuando el error es proporcional a
la media, antilogaritmar para volver a un factor/razon, y que el antilog de la DE en log menos 1 aproxima el CV cuando la DE es pequena.
NO respalda: varianza de ln ~ CV^2 enunciada asi, uso de logaritmo natural (el ejemplo usa log10), ni nada sobre Pitman-Morgan.

## Dudas para el asesor
- La nota da CV ~ antilog(DE_log) - 1, con log10 en el ejemplo. El paso "DE de ln ~ CV" (porque exp(s) - 1 ~ s si s es pequeno)
  NO esta en el PDF; es una derivacion propia. ¿Basta con citar esta nota y explicitar la derivacion, o hace falta una fuente que
  lo enuncie directamente con ln (y como varianza ~ CV^2)?
- La nota trata error intra-sujeto con duplicados; ¿es aceptable como respaldo para comparar varianzas de dos metodos (Pitman-Morgan) en escala log?
- La nota "Logarithms" (BMJ 312:700), cuyo raw ya esta en `refs/raw/`, no esta en este PDF; ¿se necesita su PDF por separado?

## Evidencia textual
| Dato / criterio | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Numero de la serie | "This is the 23rd in a series of occasional notes on medical statistics" | p. 106, margen izq. |
| Cita bibliografica impresa | "BMJ 1996;313:106" | p. 106, margen izq. |
| DOI | NO ENCONTRADO EN EL PDF | — |
| Indice previo de error: DE intra-sujeto | "the within-subject standard deviation as a practical index of measurement error" | p. 106, col. central |
| Condicion de uso de la DE intra-sujeto | "should be used when the measurement error was not related to the magnitude" | p. 106, col. central |
| Diagnostico recomendado | "plot the subject standard deviation against the subject mean to check this" | p. 106, col. central |
| Datos: duplicados de cotinina salival | "Duplicate salivary cotinine measurements for a group of Scottish schoolchildren (ng/ml)" | p. 106, Tabla 1 |
| Tamano de muestra: 20 sujetos | Tabla 1 lista "Subject No" 1 a 20 con "1st" y "2nd" | p. 106, Tabla 1 |
| Diferencia absoluta equivale a DE con dos medidas | "which is equivalent to a standard deviation versus mean plot when we have only two" | p. 106, col. central |
| Relacion variabilidad-magnitud | "there is a clear relationship, the variability increasing with the magnitude" | p. 106, col. central |
| Kendall tau = 0.62, P = 0.0001 (escala original) | "Kendall's tau = 0.62, P = 0.0001" | p. 106, col. central |
| Log casi siempre resuelve el problema | "a logarithmic transformation of the data almost always solves the problem" | p. 106, col. central |
| Chequeo: log DE vs log media | "we can check by plotting log standard deviation against log mean" | p. 106, col. central |
| Pendiente = 0.9 | "For these data the slope is 0.9" | p. 106, col. central |
| Criterio: pendiente ~1 indica log | "subject standard deviation is roughly proportional to the subject mean and a log transformation is indicated" | p. 106, col. central |
| Kendall tau = 0.07, P = 0.7 (tras log) | "There is now no evidence of a relationship (Kendall's tau = 0.07, P = 0.7)" | p. 106, col. central |
| Base del logaritmo usada: 10 | "Absolute difference against mean after log10 transformation" | p. 106, leyenda Fig 2 |
| Logaritmo natural (ln) | NO ENCONTRADO EN EL PDF | — |
| sigma_w en log = 0.175 | "the within-subject standard deviation as sigma_w = 0.175" | p. 106, col. central |
| Hay que antilogaritmar para interpretar | "we need to antilog it before we can interpret it easily" | p. 106, col. central |
| a_sigma_w = 1.496 | "For the cotinine data, a_sigma_w = 1.496" | p. 106, col. central |
| Antilog de la DE es una razon | "When we antilog sigma_w we have a ratio, not a quantity measured in" | p. 106, col. central |
| Restar en log = dividir en natural | "Subtracting on the logarithmic scale is equivalent to dividing on the natural scale" | p. 106, col. central |
| Definicion: DE geometrica | "a related quantity sometimes referred to as the geometric standard deviation" | p. 106, col. central |
| Una DE a cada lado: multiplicar/dividir | "we should multiply and divide by a_sigma_w" | p. 106, col. central |
| 95%: 1.96 sigma_w | "expected to be less than 1.96 sigma_w for 95% of observations" | p. 106, col. derecha |
| Factor a^1.96 ~ a^2 | "multiply and divide on the natural scale by a^1.96 or approximately a^2" | p. 106, col. derecha |
| 1.496^2 = 2.238 | "we would divide and multiply by 1.496^2 = 2.238" | p. 106, col. derecha |
| Ejemplo 2 ng/ml -> 0.9 a 4.5 ng/ml | "between 2/2.238 = 0.9 and 2 x 2.238 = 4.5 ng/ml" | p. 106, col. derecha |
| Multiplicar en natural = sumar en log | "Multiplying on the natural scale is equivalent to adding on the log scale." | p. 106, col. derecha |
| Condicion de la aproximacion al CV | "Provided the standard deviation is not large compared with the level of the measurement" | p. 106, col. derecha |
| a_sigma_w - 1 ~ DE relativa | "a_sigma_w - 1 is approximately equal to the standard deviation expressed as a proportion" | p. 106, col. derecha |
| Definicion de CV | "The ratio of standard deviation to mean is called a coefficient of variation" | p. 106, col. derecha |
| a_sigma_w - 1 es el CV intra-sujeto | "here a_sigma_w - 1 is the within-subject coefficient of variation" | p. 106, col. derecha |
| CV estimado = 0.496 (49.6%) | "variation is 1.496 - 1 = 0.496 or 49.6%" | p. 106, col. derecha |
| Limite de la aproximacion | "This is rather too large for the approximation to be reliable." | p. 106, col. derecha |
| Criterio de interpretacion de precision | "The precision of a method of measurement must be interpreted in the light of its intended use." | p. 106, col. derecha |
| Varianza del log ~ CV^2 | NO ENCONTRADO EN EL PDF | — |
| Prueba de Pitman-Morgan | NO ENCONTRADO EN EL PDF | — |
| Limites de concordancia entre dos metodos en escala log | NO ENCONTRADO EN EL PDF | — |
| Umbral numerico de "CV pequeno" | NO ENCONTRADO EN EL PDF | — |
