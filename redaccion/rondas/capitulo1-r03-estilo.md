# Revision de estilo — capitulo1 — r03

Lint de la ronda: PASA, sin hallazgos. Respuesta previa: r02, 0 RECHAZADOS (S03 NO APLICADO por
E-O2, no se re-abre). Vara de tono: ESTILO §1.1 (E-M1 a E-M8). Fichas cotejadas: `deman1999`,
`selles2024marreview`, `peters2025hybrid`, `zhang2023controlnet`, `wang2019cochlear`; cap. 3 l.75,
l.85, l.196, l.225, l.265.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S01 | media | E-P4 | l.35, ultima oracion | "parte de los voxeles sacros queda a 150~HU o menos" | Cantidad vaga con el dato disponible (cap. 3 l.85; afin a PAT-8). "En la cohorte local, a lo largo del eje del corredor mas ancho, la mediana de la fraccion de voxeles sacros a 150~HU o menos fue 0.42, y un hueso definido por ese umbral dejaria fuera esa fraccion (Seccion~\ref{sec:corredor})." |
| S02 | media | E-P3 | l.44, 1a oracion | "para conservar al mismo tiempo el rango del metal y los contrastes" | Patron PAT-39 reincide: la definicion atribuye un proposito que el ejemplo citado no cumple (l.46: con las ventanas de Wang et al. "el metal satura tambien en la ventana ancha"). "La **codificacion multiventana** usa varias ventanas a la vez, una por canal, de modo que las anchas conservan el rango de HU y las estrechas separan los contrastes pequenos del tejido." |
| S03 | media | E-P4 | l.54, ultima oracion | "incluso una razon muy pequena entre radiacion dispersa y primaria" | La ficha `deman1999` (Sec. II-D) da el valor. "En la misma simulacion, una razon entre radiacion dispersa y primaria de 0.0001, elegida de forma arbitraria, ya produce rayas apreciables, muy parecidas a las del haz policromatico \cite{deman1999}." |
| S04 | media | E-M4 | l.56, ultima oracion | "Segun ellos, ese artefacto de ruido es no lineal, como los" | Oracion anadida para llegar a tres (respuesta r02, S07); el lector no sabe que se sigue de la no linealidad. Decir lo que la ficha da (Sec. III-E, "even the amount of scatter and beam hardening have a strong influence on the severity"): "Segun ellos, ese artefacto de ruido es no lineal, como los del endurecimiento del haz y la dispersion, y su severidad depende de cuanta dispersion y endurecimiento haya, de modo que en su simulacion las causas no actuan por separado." |
| S05 | media | E-R6 | l.58, ultima oracion | "De Man et al. no miden en ningun punto hasta donde llegan" | Un NO ENCONTRADO de la ficha redactado como negacion sobre el metodo (afin a PAT-72; decision §2 del 2026-09-30: "el articulo no menciona"). Ademas "estas descripciones" son las del borde y la negacion abarca todo el articulo. "Ninguna de las dos descripciones incluye una distancia, y el articulo de De Man et al. no menciona hasta donde llegan las rayas de ninguna de las causas que estudia." |
| S06 | media | E-T1 | l.66, 2a oracion | "desviaciones mas altas respecto de una imagen de referencia" | Patron PAT-14 reincide: "referencia" esta reservada para la referencia clinica (decision §2 del 2026-09-30). La ficha `peters2025hybrid` (Sec. 2.5) habla de *ground truth* sin metal: "... respecto de la imagen sin metal del mismo caso y el del 5\,\% mas bajas." |
| S07 | media | E-P3 | l.82, 1a oracion | "La posicion de un tornillo se juzga frente a una posicion ideal." | Patron PAT-101 reincide: universal sostenido por una fuente, y el mismo parrafo (y l.84) gradua la perforacion, no la distancia a la posicion ideal. "Smith et al.~\cite{smith2006iliosacral} juzgan la posicion de un tornillo frente a una posicion ideal, que definen enteramente dentro de los margenes corticales del sacro, ..." |
| S08 | media | E-M4 | l.124, ultima oracion | "lo que anadio un septimo candidato examinado sobre los mismos pacientes de prueba" | Patron PAT-52 reincide: la extension se enuncia sin su efecto sobre el criterio que abre el parrafo ("cuantas oportunidades de aprobar da la regla"); ademas "candidato" renombra las "combinaciones" (E-R5). "La compuerta se extendio despues al espacio latente del generador de volumenes de TC de Guo et al.~\cite{guo2025maisi}, con la misma regla y los mismos pacientes de prueba, lo que eleva a siete las combinaciones que pueden aprobar; el veredicto de esa extension se presenta en el capitulo de resultados." (cap. 3 l.75) |
| S09 | baja | E-P3 | l.46, 2a oracion | "El Objetivo~1 examina tres codificaciones" | El Objetivo 1 ya se corrio (l.108: "midio", "el veredicto negativo"). "El Objetivo~1 examino tres codificaciones (Seccion~\ref{sec:obj1})." |
| S10 | baja | E-M4 | l.62, 3a oracion | "cuyo ancho es una convencion de este trabajo" | La razon de que sea convencion queda implicita, aunque l.58 la da. "..., cuyo ancho es una convencion de este trabajo porque las fuentes revisadas no dan hasta donde llegan las rayas (Seccion~\ref{sec:ea-representacion})." |
| S11 | baja | E-M1 | l.84, 1a oracion | "Smith et al. declaran que toman esa escala de la clasificacion" | El parrafo contrasta escalas (Smith, Zwingmann, Hinsche) y abre por el origen de una. Abrir con la funcion: "Las fuentes revisadas no juzgan la colocacion con una misma escala." y seguir con Smith et al. |
| S12 | baja | E-P3 | l.104, 4a oracion | "Con ello, el procedimiento de muestreo de la difusion se elige" | Patron PAT-101 reincide: vale para modelos entrenados con el objetivo de Ho et al., no en general. "Con ello, en un modelo entrenado con el objetivo de Ho et al., el **procedimiento de muestreo** se elige por separado del entrenamiento." |
| S13 | baja | E-M8 | l.90, 1a oracion | "aprende ... una distribucion ..., y los modelos de difusion son una familia" | Tres ideas en una oracion (definicion, familia, revision). "Un modelo generativo aprende, a partir de ejemplos, una distribucion de la que extrae muestras nuevas. Los modelos de difusion son una familia de ellos, y Kazerouni et al.~\cite{kazerouni2023diffusionsurvey} revisan su uso en imagen medica." |
| S14 | baja | E-R5 | l.120, 2a oracion | "pregunta si una condicion supera a la otra ... entre ambos" | "Brazos" en la oracion tematica, "condicion" aqui, y "ambos" concuerda con brazos. "Una prueba de **superioridad** pregunta si un brazo supera al otro, y una de **equivalencia**, si la diferencia entre ambos es tan pequena que se pueden tratar como intercambiables." |
| S15 | baja | E-R2 | l.122, 3a oracion | "con un margen definido por la variabilidad propia del metodo" | No dice de que variabilidad se trata; el cap. 3 (l.225) si. "... con un margen fijado por la variabilidad entre semillas del sintetizador y entre corridas repetidas del protocolo fisico (Seccion~\ref{sec:apariencia})" |
| S16 | baja | E-R4 | l.124, 3a oracion | "hubo, sin embargo, decisiones posteriores a ver datos: ... despues de ver datos" | Repite la condicion dentro de la oracion. "En ambos casos hubo, sin embargo, decisiones posteriores a ver datos: esa regla se fijo conociendo un resultado exploratorio desfavorable que incluia a los pacientes de prueba, y en el Objetivo~2 hubo tres (Seccion~\ref{sec:amenazas})." |

## Impresion general
Leido seguido, el capitulo suena a tesis: define por contraste, cita con verbo preciso y acota a las
fuentes revisadas; la repeticion entre parrafos de r02 desaparecio. Lo que queda es fino: cantidades
dichas en vago aunque el dato existe (S01, S03) y oraciones de apertura o cierre que afirman mas, o menos, que el parrafo (S02, S04, S07, S08).

TOTAL alta=0 media=8 baja=8

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Cantidad vaga ("parte", "muy pequena") cuando la ficha o el cap. 3 dan el valor | E-P4 | "incluso una razon muy pequena entre radiacion dispersa y primaria" | PAT-8 |
| Oracion anadida solo para cumplir el minimo de E-O2, sin consecuencia para el parrafo | E-M4, E-R2 | "Segun ellos, ese artefacto de ruido es no lineal" | nuevo |
| NO ENCONTRADO de la ficha redactado como negacion sobre lo que hicieron los autores | E-R6 | "De Man et al. no miden en ningun punto hasta donde llegan" | PAT-72 |
| "Referencia" usada fuera de la referencia clinica | E-T1 | "respecto de una imagen de referencia" | PAT-14 |
| Oracion de apertura con un universal que solo sostiene la fuente citada o que el parrafo no desarrolla | E-P3 | "La posicion de un tornillo se juzga frente a una posicion ideal." | PAT-101 |
| Definicion que atribuye al concepto un proposito que el ejemplo citado no cumple | E-P3 | "para conservar al mismo tiempo el rango del metal" | PAT-39 |
| Hecho que cierra el parrafo sin su efecto sobre el criterio que el parrafo abrio | E-M4 | "lo que anadio un septimo candidato examinado sobre los mismos pacientes" | PAT-52 |
