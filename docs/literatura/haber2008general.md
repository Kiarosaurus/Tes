# haber2008general — Acuerdo entre métodos con mediciones replicadas

- **DOI / URL:** 10.1177/0962280206075527 (impreso en p. 151 del PDF; coincide con `doi` y `URL` de `refs/raw/haber2008general.bib`)
- **Nivel de lectura:** 2 (método)
- **Leído a fondo por la autora:** no
- **PDF:** papers/haber2008general.pdf

Verificación contra el raw: título, autores (Michael Haber y Huiman X Barnhart), revista, volumen 17, número 2,
páginas 151--169, año 2008 y DOI coinciden con la cabecera del PDF. Clave renombrada a `haber2008general` por la autora (2026-10-15): coincide con el año del raw y del PDF.

## Qué hace (3 líneas máximo)
Propone coeficientes de acuerdo que comparan el desacuerdo entre dos métodos con el desacuerdo entre réplicas del
mismo método. Distingue el caso sin referencia, que promedia el desacuerdo intramétodo de ambos brazos, del caso con
referencia, que usa solo el desacuerdo de la referencia. Desarrolla versiones basadas en MSD, MAD y MRD.

## Restricción o supuesto clave
No aplica la restricción para síntesis generativa: es un paper metodológico. Para usar sus coeficientes, las réplicas
deben medir el mismo sujeto sin que cambie el valor verdadero y ser no emparejadas; además, antes de usar el ruido
intramétodo como patrón hay que comprobar que ese ruido sea aceptable. Frase: "one must check that the corresponding
within-method disagreement ... [is] acceptable" (Introducción, p. 153).

La transferencia a esta tesis es parcial. El contraste principal usa por paciente la mediana de cinco semillas del
sintetizador y la mediana de dos réplicas de Peters, mientras Haber y Barnhart interpretan sus coeficientes para una
medición individual de cada método (p. 154 y Discusión, p. 167). Tampoco proponen un TOST ni un margen
`Delta = max(s_sem, r_rep)`: sin referencia usan el promedio de dos funciones de desacuerdo; con referencia usan solo
la repetibilidad de la referencia. `max`, rango máximo--mínimo y margen de equivalencia: **NO ENCONTRADO EN EL PDF**.

## Qué tocó de aquí
- [ ] método que reimplemento
- [ ] número que cito
- [ ] baseline de comparación
- [x] solo contexto (fundamento y límite metodológico de la interpretación de `Delta` en #195)

## Números que cito de este paper
| Cifra | Frase original (corta) | Sección / página |
|---|---|---|
| Ninguna cifra empírica se traslada a la tesis | — | — |

## Dónde entra en mi tesis
Capítulo 3, análisis estadístico y amenazas a la validez del Objetivo 3; capítulo 4, discusión. Respalda únicamente la
idea general de comparar el desacuerdo entre métodos con su variabilidad intramétodo. No valida la fórmula concreta
`Delta = max(s_sem, r_rep)` ni convierte ese ruido en una diferencia clínica o prácticamente aceptable.

### Respuesta dirigida a #195

1. **Sí respalda la intuición general.** El mejor caso se define cuando sustituir o intercambiar un método no aumenta
   sustancialmente el desacuerdo respecto de repetir el mismo método (Introducción, pp. 152--153).
2. **Sin método de referencia**, define
   `psi_G^N = ([G(X,X') + G(Y,Y')]/2) / G(X,Y)`: el numerador es el promedio de los dos desacuerdos intramétodo
   (ecuación 1, p. 153), no su máximo.
3. **Con método de referencia X**, define `psi_G^R = G(X,X') / G(X,Y)` (ecuación 2, p. 153): la escala viene de la
   referencia, no de la variabilidad del método nuevo.
4. **La propia fuente reconoce el efecto cuestionado:** los coeficientes aumentan con la variabilidad intramétodo
   (Discusión, p. 168). Lo juzga razonable solo si esa variabilidad ya es aceptable y el desacuerdo entre métodos no
   aumenta; esto no elimina el riesgo de que un método más ruidoso parezca acordar mejor.
5. **La escala aceptable sigue siendo sustantiva.** El límite de acuerdo aceptable depende de la aplicación (p. 153),
   y la Discusión permite sustituir réplicas por un error de medición aceptable fijado externamente o subjetivamente
   (p. 167). Por tanto, el paper no transforma automáticamente la variabilidad observada en margen de equivalencia.
6. **Conclusión para la tesis:** la fuente basta para respaldar la idea de acuerdo relativo al ruido propio, siempre
   que `Delta` se declare convención del estudio y limitación. No basta para afirmar que `max(s,r)` sea una regla
   publicada o validada; buscar una segunda fuente cercana no corregiría esa falta de correspondencia matemática.

## Dudas para el asesor
- ¿Se acepta presentar `Delta` como una convención inspirada en el acuerdo individual, sin atribuir `max(s,r)` a
  Haber y Barnhart?
- ¿Conviene citar esta fuente en Análisis estadístico o reservarla para Amenazas/Discusión, dado que la prueba ya se
  ejecutó con una regla distinta?
- ¿Se mantiene la denominación "equivalencia" o se acota a "indistinguibilidad a la escala del ruido elegido"?

## Evidencia textual
| Cifra / umbral / definición / criterio | Frase original (máx. 15 palabras) | Sección / página |
|---|---|---|
| Acuerdo ideal pese a error | "even under ‘perfect’ agreement ... differ because of measurement errors" | Introducción, p. 151 |
| Mejor caso | "disagreement ... different methods is similar to ... the same method" | Introducción, p. 152 |
| Interpretación operacional | "does not substantially increase the disagreement" | Introducción, p. 152 |
| Sin referencia: promedio intramétodo | "The numerator is the average disagreement" | Introducción, p. 153 |
| Con referencia | "replicated measurements made by the reference method" | Introducción, p. 153 |
| Condición previa | "within-method disagreement ... [is] acceptable" | Introducción, p. 153 |
| Umbral depende del uso | "will depend on the specific application" | Introducción, p. 153 |
| Requiere réplicas | "we have to use data with replicated measurements" | Introducción, p. 154 |
| Réplicas no emparejadas | "these are unmatched replications" | Introducción, p. 154 |
| Objetivo: una medición futura | "each method is used only once on each subject" | Introducción, p. 154 |
| MAD | "G(X, Y) = MAD(X, Y) = E|X − Y|" | Sec. 3, p. 162 |
| MAD interpretable | "The MAD is easier to interpret" | Sec. 3, p. 162 |
| Promedio ponderado posible | "using a weighted average of G(X, X′) and G(Y, Y′)" | Discusión, p. 166 |
| MAD/MRD preferibles en muchos casos | "the MAD or the MRD will be preferred" | Discusión, p. 166 |
| Referencia estadística | "use the within-methods variability as the reference" | Discusión, p. 166 |
| Solo si la variabilidad es aceptable | "meaningful only when ... within-methods variability ... is acceptable" | Discusión, p. 166 |
| Valor verdadero estable | "true value ... should not change between replicated evaluations" | Discusión, p. 167 |
| Error aceptable externo | "magnitude of an acceptable measurement error" | Discusión, p. 167 |
| Replicar mejora precisión, no el estimando | "will increase the precision ... but ... not affect their expected values" | Discusión, p. 167 |
| Efecto del ruido propio | "they increase with the within-method variability" | Discusión, p. 168 |
| `max(s,r)` | NO ENCONTRADO EN EL PDF | — |
| Rango máximo--mínimo como desacuerdo | NO ENCONTRADO EN EL PDF | — |
| TOST o margen de equivalencia | NO ENCONTRADO EN EL PDF | — |
