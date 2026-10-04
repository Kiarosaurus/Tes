# Revision de estilo — capitulo1 — r05

Lint de la ronda: PASA, sin hallazgos. Respuesta previa: r04, sin RECHAZADOS; S07 NO APLICADO con
motivo (sin respaldo en la ficha `deman1999`) y no se re-reporta. Vara de tono: ESTILO §1.1 (E-M1 a
E-M8); `muestras_autora.md` sigue vacio. Cap. 3 cotejado: l.75 (extension a Guo et al.: "el veredicto
... se presenta en el capitulo de resultados"), l.85 (0.42 y su consecuencia: el corredor se mide
sobre mascaras), l.215 (inversion de metricas en `\GAPDEC`, sin definicion: PAT-115 queda resuelto
con "esta pendiente"), l.265 (multiplicidad). Se respetan las decisiones de BITACORA §2: "que el
veredicto negativo descarto" (l.110) y el titulo de 1.5 (escalado en r01) no se reportan.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S01 | media | E-R4, E-M4 | l.35, ultima oracion | "Un hueso definido por ese umbral dejaria fuera, en la mediana, esa fraccion del corredor" | Tras partir la oracion en r04, la ultima solo reformula la anterior (fraccion a 150 HU o menos = fraccion que el umbral deja fuera) y no dice que se sigue. La consecuencia esta en cap. 3 l.85: "Por eso el corredor se mide sobre mascaras anatomicas y no con ese umbral (Seccion~\ref{sec:corredor})." (el "en la mediana" ya va en la oracion de la cifra; el parrafo sigue en 7 oraciones) |
| S02 | media | E-P3, E-T1 | l.64, 1a oracion | "La MAR elimina el artefacto ...; este trabajo no hace ni lo uno ni lo otro" | Dos problemas. "Elimina" sube la certeza frente al propio nombre del metodo (reduccion de artefactos metalicos). Y "este trabajo no hace ... lo otro" choca con la ultima oracion del parrafo, que preve usar la simulacion fisica como comparacion (Patron PAT-39 reincide). "La MAR reduce el artefacto de una TC ya adquirida, y la simulacion fisica lo produce reproduciendo la adquisicion; el sintetizador de este trabajo no hace ni lo uno ni lo otro." |
| S03 | media | E-R1 | l.120, l.122, l.124 (aperturas) | "Para comparar distribuciones ..." / "Para los brazos pareados ..." / "Para la superioridad, ..." | Tres parrafos seguidos abren con "Para + objetivo"; la correccion de PAT-114 en r04 (l.124) creo el tercero. Conservar l.120. l.122: "El Objetivo~3 plantea dos preguntas sobre sus brazos pareados." (se quita tambien el redundante "distintas"). l.124: "La prueba de superioridad del Objetivo~3 es la de rangos con signo de Wilcoxon, pareada y de una cola." |
| S04 | media | E-M1, E-O2 | l.124, oraciones 4-6 | "En el Objetivo~1, la incertidumbre de una media por paciente se expresa ..." | El parrafo trata de las pruebas del Objetivo 3 y cierra con el remuestreo del Objetivo 1, otra funcion (cf. PAT-33). Partir: el parrafo del Objetivo 3 queda con sus tres primeras oraciones; nuevo parrafo: "La incertidumbre de la media por paciente del Objetivo~1 se expresa con un intervalo de confianza por remuestreo de pacientes. La media se vuelve a calcular sobre muestras de pacientes tomadas con reemplazo, y el intervalo sale de la distribucion de esas medias; la compuerta reporta asi el intervalo del 95\,\% (Seccion~\ref{sec:obj1}). Se remuestrean pacientes porque el paciente es la unidad de analisis del Objetivo~1." y al final el `\GAPLIT` actual, que cubre ambos parrafos |
| S05 | media | E-M4, E-P3 | l.126, ultima oracion | "si fuera aprobatorio, la multiplicidad de siete combinaciones si podria haberlo favorecido" | El condicional contrafactico mezcla tiempos ("fuera ... podria haberlo") y el "si" enfatico responde a una objecion que nadie hizo; ademas, leido junto a l.110 ("que el veredicto negativo descarto"), invita a dudar de un veredicto que el capitulo da por cerrado. Decir la consecuencia sin hipotesis, como cap. 3 l.265: "El veredicto de esa extension se presenta en el capitulo de resultados, y la multiplicidad de siete combinaciones solo podria comprometerlo si fuera aprobatorio (Seccion~\ref{sec:amenazas})." |
| S06 | baja | E-T1 | l.122, 2a oracion | "pregunta si un brazo supera al otro" | BITACORA §2 (2026-09-29): "brazo" solo en plural generico. "pregunta si una condicion supera a la otra" |
| S07 | baja | E-R4 | l.44, 1a oracion | "de modo que las anchas conservan el rango de HU y las estrechas separan" | Repite casi literal la ultima oracion de l.42. "La codificacion multiventana usa varias ventanas a la vez, una por canal, y evita asi elegir entre las dos propiedades." |
| S08 | baja | E-INF (registro) | l.46, 3a oracion | "queda bajo el umbral de 2500~HU del metal, asi que el metal satura" | "Asi que" es de registro oral; el capitulo usa "de modo que". "..., de modo que el metal satura tambien en la ventana ancha." |
| S09 | baja | E-R1 | l.78 oraciones 6-7; l.80 oracion 4 | "que la Seccion~\ref{sec:corredor} lee como ..." / "La Seccion~\ref{sec:corredor} describe" | Tres remisiones seguidas a la misma seccion, dos con la misma formula. Ultima oracion de l.78: "Esa seccion describe tambien como este trabajo mide el corredor, sobre mascaras anatomicas de TotalSegmentator \cite{wasserthal2023}, y que criterio de viabilidad adopta en lugar de ese umbral." |
| S10 | baja | E-M4 | l.88, 2a oracion | "Su motivacion es la heterogeneidad de la masa osea pelvica" | "Su" puede remitir a SAP o al tercer componente. "La motivacion de esa fraccion es la heterogeneidad de la masa osea pelvica que describen Arand et al. ..." |

## Impresion general
Leido seguido, el capitulo suena a tesis: define por contraste, acota a las fuentes revisadas y dice
para que sirve cada concepto. Lo que queda son efectos de las correcciones previas: una oracion
partida que se volvio tautologia (S01), aperturas repetidas que aparecieron al reescribir otras (S03)
y un parrafo con dos funciones (S04).

TOTAL alta=0 media=5 baja=5

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Al partir una oracion larga, la segunda mitad queda como reformulacion de la primera y no como su consecuencia | E-R4, E-M4 | "Un hueso definido por ese umbral dejaria fuera ... esa fraccion" | nuevo |
| Al reescribir la apertura de un parrafo para quitar un tic, nace otra serie de aperturas iguales en los parrafos vecinos | E-R1 | "Para comparar ..." / "Para los brazos ..." / "Para la superioridad ..." | nuevo |
| Afirmacion general sobre "este trabajo" que el mismo parrafo contradice | E-P3 | "este trabajo no hace ni lo uno ni lo otro" | PAT-39 |
| Condicional contrafactico sobre un resultado que el propio capitulo da por cerrado en otro lugar | E-M4, E-P3 | "si fuera aprobatorio, ... si podria haberlo favorecido" | nuevo |
