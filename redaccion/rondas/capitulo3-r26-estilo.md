# Revision de estilo — capitulo3 — r26

Lectura completa de `overleaf/secciones/capitulo3.tex` en su estado posterior a r25, en dos pasadas. No se repiten las 25
E-P1 del lint. En la respuesta de r25, S1-S17 quedaron APLICADOS y no hay RECHAZADOS de estilo que reabrir. "Se separan
dos niveles." (:425) es la propuesta S4 de r25 y no se re-reporta. `muestras_autora.md` sigue vacio, asi que la vara es
ESTILO.md §1.1. Fichas cotejadas para E-R6 en el texto nuevo:
- `walker2011understanding`, :19, :48 y :117: coinciden con :419 y :421.
- `lakens2017equivalence`, :66-:71: coinciden con :421.
- `bland1996statisticsmeasurement`, :22, :23, :69 y :90: coinciden con :445 y :447.

No hay hallazgos E-R6. El encargo 2026-10-15c (cierre de GAPDATO) todavia no esta aplicado en el texto revisado; el texto
que agregue no queda cubierto por esta revision.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S1 | media | E-T1, E-R5 | :533 | "los brazos no se distinguen a la escala de ese ruido" | Patron PAT-14 reincide. En el mismo apartado, "piso de ruido" nombra otra magnitud, la amplitud de solo ruido (:433, :539, :541). El margen, en cambio, es "la variabilidad propia del método" (:427). Propuesta: "Una equivalencia diría, así, que los brazos no se distinguen a la escala de esa variabilidad, y no que su diferencia sea irrelevante para algún uso." |
| S2 | media | E-T1, E-F3 | :443, :445, :447, :535 | "Bland y Altman juzgan el acuerdo contra una diferencia aceptable" | Patron PAT-14 reincide. "Bland y Altman" designa dos trabajos en parrafos contiguos (`bland1986statisticalmeasurement` y `bland1996statisticsmeasurement`), y los dos ponen una condicion casi igual para usar el logaritmo (:443 y :445). En :535, dos "Bland y Altman" sin `\cite` llegan despues de que el lector vio ambos trabajos, y no se sabe a cual remiten. La decision de BITACORA §2 (2026-09-30) pide un rasgo que separe a los autores homonimos. Propuesta: en :445, "En una nota posterior, Bland y Altman~\cite{bland1996statisticsmeasurement} indican..."; en :535, "Bland y Altman~\cite{bland1986statisticalmeasurement} juzgan el acuerdo [...]. En el mismo artículo advierten que con promedios [...]". |
| S3 | media | E-R4 | :499 | "Las primeras son posteriores al resultado de la versión~1 [...] Se tomaron después de ver el resultado" | Patron PAT-98 reincide: dos oraciones seguidas dicen que las primeras decisiones son posteriores al resultado de la version 1. Se funden en una: "Las primeras son previas a la prueba de equivalencia de la versión~2 y se tomaron después de ver, de la versión~1 en prueba, su resultado, sus salidas, la dispersión entre pacientes y las asimetrías entre brazos." |
| S4 | media | E-M4 | :254 | "Por esa diferencia, la síntesis sobre pelvis sin metal se repite" | Patron PAT-34 reincide. Al insertar en r25 los dos parrafos del diagnostico (:250, :252), el antecedente de "esa diferencia" quedo en :248, dos parrafos atras, y el parrafo anterior trata de otra cosa (la causa del sesgo del percentil 95). Propuesta: "Como el estado final queda más cerca de lo real dentro de $M$, la síntesis sobre pelvis sin metal se repite con él como análisis de sensibilidad del punto de control (Sección~\ref{sec:ap-analisis})." |
| S5 | baja | E-M8 | :421 | "nombra la equivalencia no establecida cuando tampoco se demuestra la no equivalencia" | Hay tres negaciones encadenadas, y el lector tiene que reconstruir que el caso es el del intervalo que cruza un limite. Propuesta: "En este trabajo, el desenlace no concluyente es la parte de esa equivalencia no establecida en que el intervalo cruza un límite, y cubre los dos casos de Lakens." |
| S6 | baja | E-R4 | :425 | "y no como equivalencia ni como no equivalencia demostrada" | Patron PAT-86 reincide: es la tercera vez en tres parrafos seguidos (:419, :421, :425) que se dice que no se concluye en ningun sentido. Se conserva la formula de la lectura en dos niveles y se quita la coda: "Un desenlace no concluyente se lee como que los datos no permiten afirmar la equivalencia." |
| S7 | baja | E-R4 | :447, :535 | "Con el 0.241 del protocolo físico, la validez de la aproximación no está establecida." | :447 enuncia el limite y remite a Amenazas, y :535 lo repite casi literal. Se elimina la oracion de :447. El parrafo queda con la cifra, el criterio de la fuente y la remision ("Los límites de esta lectura se tratan en la Sección~\ref{sec:amenazas}"). |
| S8 | baja | E-P3 | :445 | "Muestran además que el antilogaritmo de la desviación estándar" | Patron PAT-41 reincide. Segun E-P3, "muestra" queda reservado para lo medido en este trabajo. Propuesta: "Indican además que el antilogaritmo [...]". |
| S9 | baja | E-M8 | :447 | "juzgan demasiado grande para que la aproximación sea fiable un coeficiente de 0.496" | El hiperbaton deja el objeto al final de la oracion. Propuesta: "y juzgan que un coeficiente de 0.496 es demasiado grande para que la aproximación sea fiable~\cite{...}." |
| S10 | baja | E-R1, E-M8 | :419 | "Son los tres desenlaces que este trabajo fija en la Sección" | Patron PAT-152 reincide: la oracion abre con "Son", sin sujeto explicito. Propuesta: "Esa lectura aplica los tres desenlaces que este trabajo fija en la Sección~\ref{sec:mt-estadistica}: ..." |
| S11 | baja | E-R2 | :423 | "Una diferencia a la baja informada por la regla de este trabajo" | La regla es general, pero "a la baja" la ata al resultado de la version 1 sin decirlo, y la correspondencia con Lakens vale para cualquier direccion. Propuesta: "Una dirección informada por la regla de este trabajo corresponde, por tanto, al caso diferente y no equivalente de Lakens solo si también el IC del 95\,\% excluye el cero." |
| S12 | baja | E-R1 | :501 | "Las primeras fijaron [...] Fijaron también [...] fijaron [...] Las últimas fijaron [...] Fijaron además" | Cinco de las seis oraciones del parrafo giran sobre el verbo "fijar". Bastan dos oraciones, una por momento, cada una con su enumeracion: "Las primeras fijaron [...], sustituyeron [...] y, para la versión~2, [...]. Las últimas fijaron [...], el perfil por anillos, el contraste pareado [...]". |
| S13 | baja | E-R1 | :38 | "La generación del sintetizador [...] La generación y la regla de equivalencia" | Dos oraciones seguidas abren con "La generación", y la segunda la usa en otro sentido (el procedimiento fijado, no la corrida). Propuesta para la segunda: "Antes de procesar la partición de prueba se fijaron la generación y la regla de equivalencia; [...]". |
| S14 | baja | E-R1 | :204 | "Salimans y Ho~\cite{...} asumen ese proceso [...] Salimans y Ho evalúan" | Dos oraciones seguidas abren con el mismo sujeto. La segunda queda asi: "Su evaluación de la parametrización usa imágenes naturales, no TC, implantes ni condicionamiento anatómico." |

TOTAL alta=0 media=4 baja=10

## Impresion general
Leido de corrido, el capitulo sigue sobrio, sin muletillas ni inflacion. Las fuentes estadisticas nuevas se citan con la fuerza de sus fichas y con verbos precisos ("advierten", "rotulan", "indican").
El patron dominante esta en el texto nuevo de `sec:ap-analisis`: la misma idea o el mismo autor vuelve en parrafos contiguos. Hay dos trabajos de Bland y Altman sin rasgo que los separe, se repite tres veces que el resultado no concluye en ningun sentido, y el limite de la lectura en coeficientes de variacion se dice dos veces. Ademas, el "ruido" del margen choca con el "piso de ruido".

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Los mismos autores con dos trabajos distintos se citan en parrafos contiguos sin rasgo que los separe, y menciones posteriores quedan sin `\cite` | E-T1, E-F3 | "Bland y Altman juzgan el acuerdo" (:535, tras citar 1986 y 1996) | PAT-14 |
| Un sustantivo comun ("ruido") usado cerca de un termino fijo que lo contiene ("piso de ruido") para otra magnitud | E-T1, E-R5 | "no se distinguen a la escala de ese ruido" | PAT-14 |
| Al insertar parrafos nuevos, una anafora del parrafo siguiente pierde su antecedente | E-M4 | "Por esa diferencia, la síntesis [...] se repite" | PAT-34 |
| La misma salvedad de lectura ("no concluye en ningun sentido") se repite en parrafos contiguos | E-R4 | "y no como equivalencia ni como no equivalencia demostrada" | PAT-86 |
| Dos oraciones seguidas que dicen el mismo momento o la misma condicion | E-R4 | "son posteriores al resultado [...] Se tomaron después de ver el resultado" | PAT-98 |
