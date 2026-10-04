# Revision de estilo — capitulo2 — r03

Vara de tono: `redaccion/ESTILO.md` §1.1 (E-M1 a E-M8). `redaccion/muestras_autora.md` sigue vacio.
Lint r03: PASA (0/0/0); nada de lo que sigue repite al lint. La respuesta r02 aplico todos los hallazgos
de estilo (ES-11 con otra consecuencia, con motivo aceptable); no hay re-aperturas.
Ubicacion = linea de `overleaf/secciones/capitulo2.tex`. Fichas abiertas para E-P3/E-R6:
`chen2024tumorsynthesis`, `ramzan2026claim`, `karageorgos2024ddpm`, `chen2026foundationvae`,
`peters2025hybrid`. Comprobados los patrones VIGENTES PAT-3, 6, 14, 18, 31, 33, 36, 39, 49, 59, 64 a 82;
reinciden PAT-80 y PAT-14 (este ultimo, leve).

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-01 | media | E-M1, E-M4 | l. 22, ultima oracion | "En la segmentación posterior, su Dice pasa de 0.72 a 0.77" | Patron PAT-80 reincide. El parrafo trata de lo que ocurre fuera de la mascara y culmina en la lectura propia ("Este trabajo lee ese resultado como indicio..."); el Dice llega despues y cierra fuera de tema. Llevarlo tras la segunda oracion, donde se describe el metodo: "...y decodifica la imagen completa desde el espacio latente. En la segmentación posterior, su Dice pasa de 0.72 a 0.77 al añadir 300 imágenes sintéticas. El artículo no describe..." y cerrar el parrafo con la lectura propia. |
| ES-02 | media | E-O2, E-M1 | l. 60 | "Un metaanálisis del mismo primer autor \cite{zwingmann2013} agrupa tasas de malposición" | El parrafo tiene ocho oraciones y dos funciones: la serie de 2009 como referencia clinica y la tasa agregada del metaanalisis. Partir en "Un metaanálisis" y abrir el segundo parrafo con su tesis, que hoy es la ultima oracion: "La tasa agregada de malposición y el grado ordinal miden constructos distintos, y solo el segundo sirve de comparación para un muestreador de colocación. Un metaanálisis del mismo primer autor..." (sigue igual hasta "efecto de ese criterio"). |
| ES-03 | media | E-P3 | l. 80, quinta oracion | "la síntesis no tiene que separar esas contribuciones" | Lectura propia enunciada como hecho y sin fuente, justo antes de declarar que la posibilidad "queda como supuesto". Calibrar con el verbo del supuesto: "Los dos resultados son de reducción, que Lin et al. describen como un problema mal planteado porque paciente y metal contribuyen a la misma traza del sinograma; se asume que la síntesis, que no separa esas contribuciones, no hereda esa desventaja." |
| ES-04 | baja | E-P1 | l. 20, cuarta oracion | "el Dice de la segmentación de cicatriz sube de 58.89 a 63.53" | Unica cifra de Dice del capitulo sin escala (las demas llevan % o son fracciones). Dar la unidad que usa la Tabla 2 de la fuente (verificar en la ficha `ramzan2026claim`, fila 50): "...sube de 58.89 a 63.53\,\% en su mejor configuración." |
| ES-05 | baja | E-R4 | l. 30, cuarta oracion | "Ninguno de los modelos de síntesis de esta sección trata implantes metálicos ni su artefacto." | Repite la oracion tematica del mismo parrafo ("Ni la evaluación ni el mecanismo de estos modelos cubren el artefacto metálico"). Eliminar. |
| ES-06 | baja | E-R2 | l. 42, segunda oracion | "Todo el conjunto es bidimensional" | "Conjunto" es ambiguo: el capitulo llama asi al conjunto de evaluacion (l. 40), y la ficha dice que todos los conjuntos de datos se simulan en 2D ("all datasets are simulated in 2D", Abstract, p. 1). "Todos sus conjuntos de datos se simulan en dos dimensiones, y la validación tampoco cubre la osteosíntesis pélvica en tres dimensiones." |
| ES-07 | baja | E-R2 | l. 44, sexta oracion | "como hace ese protocolo en 14\,000" | "Ese protocolo" remite a Peters et al., nombrado cuatro oraciones antes; la oracion anterior es de Wang et al. 2025. "...como hace el protocolo de Peters et al. en 14\,000 casos, ni ligar su posición..." |
| ES-08 | baja | E-R4 | l. 58, ultima oracion, frente a l. 68, cuarta | "En los tres, la plausibilidad de la colocación descansa en el azar, en la opinión experta" | La misma oracion aparece casi literal diez lineas despues en la misma seccion. La decision de BITACORA §2 fija la formula de la simulacion, no esta. Dejarla en l. 58 y en l. 68 decir la carencia: "Los generadores de máscaras de lesión separan la colocación de la apariencia, pero ninguno compara sus colocaciones con una distribución clínica medida." |
| ES-09 | baja | E-M1 | l. 64, sexta oracion | "Una descripción cualitativa de la zona segura, como la de Ramadanov y Zabler" | "De ese tipo" remite a los procedimientos computables de la segunda oracion, pero la oracion llega despues de Ziran et al. y de su consecuencia. Pasarla tras la oracion de Kaiser y McLaren: "...352 de ellas en S1. Una descripción cualitativa de la zona segura, como la de Ramadanov y Zabler~\cite{...}, no da un procedimiento de ese tipo." |
| ES-10 | baja | E-M8 | l. 76, cuarta oracion | "Ninguna las usa como codificación de la entrada de un modelo que genera, y el techo" | Dos ideas en una oracion (el uso de las ventanas y la saturacion del metal). Partir: "Ninguna las usa como codificación de la entrada de un modelo que genera. Además, el techo de 2000~HU de su ventana ancha queda por debajo del umbral de 2500~HU con que se segmenta el metal, y lo satura." |
| ES-11 | baja | E-M4 | l. 80, segunda oracion | "De Man et al. aíslan sus mecanismos modificando el sinograma" | La consecuencia para la pregunta del parrafo queda implicita. "De Man et al. aíslan sus mecanismos modificando el sinograma, es decir, los describen en el dominio de proyección, y los autores de las redes de MAR..." |
| ES-12 | baja | E-T1 | l. 84, quinta oracion | "Cassanego et al. no declaran el punto de referencia de su medida" | Patron PAT-14 reincide (leve): BITACORA §2 reserva "referencia" para la referencia clinica. "...y Cassanego et al. no declaran desde qué punto miden." |
| ES-13 | baja | E-R1 | l. 120, oraciones 2 a 4 | "El primero es ... El segundo es ... El tercero es" | Tres oraciones con la misma estructura ordinal. BITACORA §2 (introduccion-r05) pide abrir cada elemento por el objeto, no por el ordinal. "Las fuentes revisadas no reúnen una geometría de implante rígida y paramétrica..., un muestreador de colocación cuya distribución... y el uso de la codificación multiventana para generar..." y en la ultima oracion nombrar los elementos: "Ningún objetivo aísla la geometría paramétrica ni la codificación multiventana..." |
| ES-14 | baja | E-M8 | l. 122, segunda oracion | "Lo que la separa de ella es el objeto que modela, ... y que su pose" | Coordinacion de un sintagma nominal con una subordinada ("el objeto ... y que su pose la propone"). "La separan de ella dos rasgos: modela un tornillo de osteosíntesis con su calibre (Sección~\ref{sec:geometria}), y su pose la propone el muestreador en lugar de fijarse en el centro de una estructura segmentada." |
| ES-15 | baja | E-R5, E-P3 | l. 126, tercera oracion | "que se validan por una segmentación posterior ... este trabajo evalúa lo sintetizado" | "Se validan" es un nombre nuevo para lo que l. 30 llama "miden lo sintetizado por una segmentación posterior"; y "evalúa lo sintetizado" en presente, cuando l. 90 dice que no hay muestras (PAT-81, leve). "A diferencia de los modelos de síntesis de lesiones, que miden lo sintetizado por una segmentación posterior (Sección~\ref{sec:ea-lesiones}), el diseño de este trabajo evalúa lo sintetizado por su coherencia física y quirúrgica (véase el alcance en la introducción)." |

## Impresion general

Leida seguida, la seccion suena sobria y cercana a la guia: cada fuente con verbo, condicion y consecuencia, sin inflacion ni conectores de relleno, y los parrafos abren por su funcion.
Lo que queda es de acabado: una oracion de dato que cierra fuera de tema (l. 22), un parrafo de ocho oraciones con dos funciones (l. 60) y una lectura propia sin calibrar (l. 80).
Sin hallazgos altos.

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Oracion de dato ajeno despues de la lectura propia, que cierra el parrafo fuera de tema | E-M1, E-M4 | "En la segmentación posterior, su Dice pasa de 0.72 a 0.77" | PAT-80 |
| Lectura propia que sostiene un supuesto, enunciada como hecho sin "se asume" ni "este trabajo lee" | E-P3 | "la síntesis no tiene que separar esas contribuciones" | nuevo |
| Oracion de cierre repetida casi literal en otro parrafo de la misma seccion, fuera de las formulas fijadas en §2 | E-R4 | "En los tres, la plausibilidad de la colocación descansa en el azar" | nuevo |
| Palabra reservada por §2 usada en su sentido corriente | E-T1 | "el punto de referencia de su medida" | PAT-14 |
