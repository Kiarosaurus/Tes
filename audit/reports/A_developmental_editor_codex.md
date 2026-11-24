# Informe de edición de desarrollo

**Alcance revisado:** `introduccion.tex`, capítulos 1 y 2 completos, y las unidades autorizadas de capítulo 3. No revisé el sintetizador v2, el protocolo de apariencia ni “Amenazas a la validez”. Trabajé en solo lectura.

Los recuentos son aproximados: conté palabras separadas por espacios en el texto fuente, incluidas expresiones de LaTeX. Los presupuestos son metas editoriales, no una reducción porcentual uniforme. La guía consultada pide que cada bloque cumpla una función argumentativa, que el estado del arte compare trabajos contra los objetivos y que la metodología siga siendo autocontenida y reproducible. La rúbrica también pide diagramas del diseño teórico y del pipeline. En las cuatro unidades revisadas solo encontré dos entornos `figure`, uno en capítulo 1 y otro en capítulo 3.

## Dictamen general

La tesis contiene los componentes necesarios, pero su arquitectura duplica el argumento en varios lugares. La introducción funciona parcialmente como resumen extendido de decisiones, resultados y limitaciones; los fundamentos y el estado del arte vuelven sobre conceptos que luego reaparecen en metodología. El problema no se resuelve suprimiendo detalle reproducible: conviene **asignar una función única a cada bloque**. La introducción debe plantear la necesidad, brecha, objetivos y límites; el marco teórico, definir lo imprescindible; el estado del arte, comparar antecedentes; y metodología, especificar las decisiones implementadas.

Recomiendo mover a anexos los detalles metodológicos ya congelados que no sean necesarios para entender el argumento —por ejemplo, algunas reglas heurísticas, parámetros de búsqueda y comprobaciones de implementación—, siempre que el cuerpo remita a una tabla o algoritmo reproducible en el anexo. No conviene trasladar allí las definiciones de métricas y criterios que el lector necesita para interpretar resultados.

## Hallazgos por unidad

Cada entrada presenta **acción, presupuesto propuesto frente al recuento actual, evidencia y fundamento**. La cita breve identifica el lugar; el diagnóstico y la recomendación constituyen el hallazgo.

### Introducción

- **A-001 — Apertura y contexto** (`introduccion.tex:3–17`; 791 → **450 palabras**). **COMPRIMIR.** Evidencia: «Los modelos de difusión ofrecen un mecanismo» (`:9`). El bloque contextualiza el problema, pero ya adelanta arquitectura, métricas y orden de capítulos (`:13–17`). Conservar el problema de datos metálicos escasos y el límite entre plausibilidad y utilidad; resumir la propuesta en pocas frases. **Figura:** sustituir parte de la prosa por un esquema de una línea: TC sin implante → pose del tornillo → síntesis local de metal y artefacto → evaluación de colocación y apariencia.

- **A-002 — Formulación del problema** (`:19–22`; 38 → **70**). **AMPLIAR** solo lo indispensable. Evidencia: la pregunta pregunta «¿En qué medida la cadena propuesta genera…?» (`:21`). Formula una evaluación, pero no expone claramente la tensión computacional antes de nombrar la solución. Redactar la brecha como incapacidad de los enfoques existentes para generar conjuntamente pose quirúrgicamente restringida y artefacto local evaluable; después formular la pregunta. El incremento sirve a la función exigida por G-A3 de la rúbrica.

- **A-003 — Marco y preámbulo de objetivos** (`:23–29`; 96 → **50**). **COMPRIMIR.** Evidencia: «Los objetivos son los cuatro que desarrolla el Capítulo…» (`:28`). La explicación de cuáles objetivos son componentes, pruebas previas o métricas es metadiscusión que puede condensarse en una oración introductoria; evitar que el lector tenga que descifrar la taxonomía antes de leer los objetivos.

- **A-004 — Objetivo general** (`:30–33`; 123 → **90**). **COMPRIMIR.** Evidencia: «La apariencia se condiciona con una codificación multiventana» (`:32`). El objetivo mezcla propósito con definiciones de corredor, codificación y tipo de tornillo. Retener producto y evaluación en la formulación; dejar definiciones para objetivos específicos o metodología.

- **A-005 — Objetivos específicos y resultados** (`:34–57`; 1,469 → **450**). **COMPRIMIR** y **REUBICAR** los resultados al capítulo de resultados. Evidencia: «la media del error absoluto medio… fue de 0.00 HU» (`:48`) y «la diferencia media fue de −301.0 HU» (`:54`). El listado incluye especificaciones largas, decisiones posteriores a resultados, desenlaces y defensa interpretativa de si se cumplió el objetivo. Así, la introducción intenta funcionar como protocolo, resultados y discusión. Mantener cuatro objetivos verificables, sus criterios esenciales y la pregunta evaluativa; trasladar los desenlaces a resultados/discusión. La cronología de la compuerta y el rediseño puede quedar en metodología en una nota breve que identifique desviación del plan. No borrar la distinción entre “objetivo de diseño logrado” y “equivalencia no sostenida”: esa precisión importa, pero debe presentarse donde se reporta el resultado.

- **A-006 — Justificación** (`:58–73`; 1,000 → **450**). **COMPRIMIR**. Evidencia: «ninguno de los tres enfoques revisados… produce a la vez» (`:62`) y «La brecha que queda…» (`:66`). Esta sección anticipa la comparación que reaparece en capítulo 2 y detalla límites del protocolo y contribuciones no aisladas experimentalmente (`:68–72`). Conservar una síntesis de necesidad y brecha, y remitir al estado del arte para la comparación crítica. No enumerar aquí cada limitación de los enfoques ni justificar cada componente del diseño.

- **A-007 — Alcance, supuestos y limitaciones** (`:74–106`; 2,111 → **650**). **COMPRIMIR** y **REUBICAR**. Evidencia: «Quedan fuera de alcance cuatro tareas» (`:80`) seguida de varios párrafos de limitaciones experimentales (`:92–104`). La delimitación del objeto, cohorte y evaluación pertenece a la introducción; los supuestos y limitaciones observadas dependen de resultados y amenazan con anticipar material fuera del alcance auditado. Retener qué se estudia y qué se excluye, con razones breves; mover limitaciones dependientes de evidencia a discusión/amenazas. No describir aquí en detalle hallazgos de cribados o análisis posteriores. El desglose de cuatro exclusiones se puede convertir en tabla compacta (decisión / motivo).

### Capítulo 1 — Marco teórico

- **A-008 — Apertura del capítulo** (`capitulo1.tex:1–28`; 467 → **200**). **COMPRIMIR.** Evidencia: «se presentan los conceptos necesarios» (`:3–7`). La presentación anticipa el mismo temario que el índice y vuelve a explicar qué capítulos siguen. Una introducción breve debe delimitar qué conceptos son necesarios para entender el método y cómo conectan.

- **A-009 — TC y unidades Hounsfield** (`:29–72`; 1,607 → **850**). **COMPRIMIR** y **REEMPLAZAR PARTE POR FIGURA.** Evidencia: «La TC reconstruye…» (`:31`). La sección cubre principios físicos, reconstrucción, valores HU y ventanas; para la contribución bastan HU, saturación/ventaneo y su relevancia para metal y representación. Mantener ecuaciones o definiciones usadas después; recortar explicación general de adquisición que no reaparezca en método. **Figura:** diagrama CT→reconstrucción→volumen HU, con una ilustración conceptual de cómo ventanas distintas representan hueso y metal; marcar que es esquema, no dato experimental.

- **A-010 — Artefactos inducidos por metal** (`:73–92`; 1,047 → **600**). **COMPRIMIR.** Evidencia: «endurecimiento del haz» y otros mecanismos (`:75–81`). Esta física justifica que el artefacto exceda la máscara del tornillo, pero algunas explicaciones detalladas de mecanismos reaparecen en introducción y estado del arte. Priorizar mecanismos pertinentes para el diseño de la banda externa; lo secundario puede quedar citado. **Figura:** corte esquemático con metal, zona oscura y streaks fuera de la máscara, conectando el fenómeno con la región de generación.

- **A-011 — Fijación iliosacra y corredores** (`:93–116`; 1,396 → **900**). **COMPRIMIR** y **REEMPLAZAR PARTE POR FIGURA.** Evidencia: «Los tornillos iliosacros…» (`:95`). La sección presenta anatomía, trayectorias, clasificación y seguridad clínica; la metodología vuelve a detallar marco y búsqueda del corredor (`capitulo3.tex:99–117`). Conservar conceptos anatómicos y distinciones necesarias para entender la unidad experimental y la referencia clínica; dejar procedimiento de medición en metodología. **Figura:** pelvis en vista axial/coronal con eje transiliosacro, corredor y brecha cortical. Aclarar visualmente que tornillo transiliosacro e iliosacro no son sinónimos, conforme al glosario (`docs/03-glosario.md:74–76`).

- **A-012 — Difusión y síntesis condicionada** (`:117–144`; 1,107 → **700**). **COMPRIMIR**. Evidencia: «Los modelos de difusión…» (`:119`). Retener forward/reverse diffusion, conditioning e inpainting solo hasta el nivel que requiere el diseño; evitar enseñar diffusion en general si luego se explica el modelo concreto en metodología. La definición de 2.5D debe aparecer una sola vez en el lugar de implementación. **Figura:** diagrama conceptual de difusión condicionada/inpainting, con máscara del implante y banda generable; no usarlo para implicar que el modelo reproduce física de proyección.

- **A-013 — Marco estadístico** (`:145–171`; 1,433 → **900**). **COMPRIMIR**. Evidencia: «intervalo de confianza» y «bootstrap» (`:147–171`). La sección presenta medidas inferenciales que vuelven a explicarse en metodología de objetivos y análisis. Mantener definiciones necesarias para interpretar MAE, Wasserstein-1 e intervalos; eliminar tutoriales generales y conservar en metodología los detalles del remuestreo y las reglas de decisión específicas. Verificar que cada símbolo mantenga el mismo significado entre capítulos (rúbrica G-T3).

### Capítulo 2 — Estado del arte y brecha

- **A-014 — Apertura** (`capitulo2.tex:1–13`; 346 → **150**). **COMPRIMIR.** Evidencia: «Este capítulo revisa…» (`:3–10`). Reducir el resumen del índice; anticipar los criterios comparativos y cómo se relacionan con los objetivos.

- **A-015 — Síntesis de lesiones por diffusion** (`:14–31`; 1,032 → **500**). **COMPRIMIR.** Evidencia: «inpainting…» (`:18–30`). Conservar dos o tres líneas representativas y la limitación que importa: las lesiones se generan dentro de máscara y no modelan intensidad inducida fuera de ella. Evitar repetir conceptos básicos de diffusion del capítulo 1 y la misma conclusión de la introducción.

- **A-016 — Inserción/simulación física de artefactos** (`:32–51`; 1,213 → **650**). **COMPRIMIR**. Evidencia: «Peters et al.» (`:34–50`). La explicación del protocolo parece extensa para una comparación que no es una verdad de terreno; parte de los mismos detalles y límites se repite en introducción (`introduccion.tex:62–68`). Organizar por enfoque, resultado reportado y limitación para este problema; mantener la distinción entre simulator y síntesis en image domain, sin volver a narrar el protocolo paso a paso.

- **A-017 — Planificación y colocación de tornillos** (`:52–83`; 1,788 → **800**). **COMPRIMIR** y **REEMPLAZAR PARTE POR TABLA**. Evidencia: «optimizan una única trayectoria» (`:58–82`). La comparación cubre demasiadas familias y diferencias clínicas antes de llegar a la implicación para el muestreador. Sintetizar los trabajos centrales: optimización de pose única frente a distribución de brechas por técnica. **Tabla:** método/fuente, qué coloca o mide, resultado que informa, límite respecto del objetivo 2; incluir la tesis como fila, como sugiere G-B8.

- **A-018 — Multiventana y extensión espacial** (`:84–107`; 1,573 → **650**). **COMPRIMIR** y **FUSIONAR** con A-015 bajo una discusión breve de condicionamiento y región generada, si la síntesis de lesiones y las representaciones multiventana comparten el argumento. Evidencia: «ninguna… define una banda…» (`:95–106`). La ausencia de precedente para la banda es relevante, pero se repite en introducción (`introduccion.tex:72`) y glosario (`docs/03-glosario.md:36–41`). Mantener atribución precisa: la literatura de MAR adopta multiventana; la tesis la usa como entrada multicanal, decisión que no debe atribuirse al paper.

- **A-019 — Comparación crítica y brecha** (`:108–128`; 1,120 → **650**). **FUSIONAR** con el cierre del capítulo y recortar repetición. Evidencia: «La brecha…» (`:115–128`). Funciona como síntesis, pero vuelve a listar los argumentos y contribuciones ya expuestos en la justificación. Convertir en una tabla comparativa compacta y un párrafo de brecha que coincida exactamente con la formulación de A-002 (rúbrica G-B10).

### Capítulo 3 — unidades incluidas en el alcance

- **A-020 — Visión general** (`capitulo3.tex:11–41`; 810 → **350**). **COMPRIMIR** y **REEMPLAZAR PARTE POR FIGURA**. Evidencia: «La cadena propuesta tiene…» (`:13–21`). La prosa ya contiene el pipeline, cohortes, objetivos, variables y orden experimental. Retener mapa del capítulo y flujo de entradas/salidas; distribuir detalles en subsecciones. **Figura prioritaria:** pipeline de tres bloques —compuerta de representación, muestreador, sintetizador— con cohortes, productos y evaluación, distinguiendo componentes evaluados. Cumple rúbrica P-MT2/P-MM2.

- **A-021 — Datos y auditoría de cohorte** (`:42–71`; 1,562 → **1,200**). **COMPRIMIR**. Evidencia: «178 volúmenes» y funciones de grupos (`:42–71`). El detalle de procedencia y adjudicación es valioso para reproducibilidad, pero la cronología de auditorías/cambios distrae del protocolo final. Ordenar como: universo disponible, criterios de inclusión/exclusión, particiones, revisión y límites de identificación. Trasladar trazas extensas de auditoría a anexo. La data card indica que los 178 volúmenes son subconjunto local, no toda CTPelvic1K, y que la identificación dataset6/dataset7 es inferida (`docs/02-datos.md:53–63`): mantener esas cautelas explícitas, no expandirlas en narrativa repetida.

- **A-022 — Evaluación de representación multiventana** (`:72–94`; 991 → **700**). **COMPRIMIR** y **REUBICAR** la historia exploratoria a una nota metodológica/limitación breve. Evidencia: «Una exploración previa… incluida la partición de prueba» (`:74`). La especificación de métrica, combinaciones y regla es reproducible y debe quedarse. El recuento de secuencia de decisiones y exploraciones se puede condensar; explicar una vez por qué el no-go llevó a evaluar otro dominio. **Figura:** flujo de la compuerta con las seis combinaciones, criterio 25 HU y bifurcación de decisión, sin incluir resultados en el diagrama.

- **A-023 — Introducción al muestreador** (`:95–98`; 147 → **100**). **COMPRIMIR**. Evidencia: «no busca una trayectoria óptima» (`:97`). Funciona como puente, pero repite objetivos e introducción. Dejar la motivación en una frase y remitir a pose preinscrita y SAP.

- **A-024 — Marco y medición del corredor** (`:99–118`; 1,140 → **750**). **COMPRIMIR**; **TRASLADAR A ANEXOS** parámetros operativos secundarios de la búsqueda. Evidencia: la búsqueda «recorre centros candidatos… en una rejilla de 3 mm» (`:109`). La definición del corredor y su viabilidad son centrales; la rejilla completa, criterios de trayectoria, recorte y limpieza pueden tabularse o documentarse como algoritmo de anexo. Mantener en el cuerpo los pasos que permitan replicar el resultado, quizá mediante algoritmo con referencia al anexo. **Figura:** esquema geométrico de búsqueda y extracción de longitud útil.

- **A-025 — Aplicabilidad del marco en volúmenes con metal** (`:119–128`; 591 → **400**). **TRASLADAR A ANEXOS** parte del análisis detallado y **COMPRIMIR** el cuerpo. Evidencia: «57 tenían las cinco referencias localizadas» (`:125`). Esta validación de aplicabilidad es pertinente, pero detalles de heurística, revisión y acuerdo caben en tabla de auditoría/anexo. Dejar resultados mínimos que justifiquen la aplicabilidad y sus límites. Riesgo de extensión: evitar convertir cada análisis de soporte en una nueva subsección narrativa.

- **A-026 — Geometría del implante** (`:129–156`; 823 → **500**). **COMPRIMIR**. Evidencia: «Se mantienen separadas tres geometrías» (`:131`). La tabla de geometrías es una buena representación; la discusión posterior vuelve a justificar cada diámetro y documenta decisiones históricas. Retener valores finales, fuentes, qué geometría se usa en cada cálculo y las incertidumbres materiales que afectan reproducibilidad. Mover historial de cambio de diseño y parámetros no usados a anexo/registro. **Figura opcional:** vista esquemática de cilindro, cabeza y calibre de evaluación acompañando la tabla, si evita prosa adicional.

- **A-027 — Distribución de poses preinscrita** (`:157–201`; 1,069 → **550**). **COMPRIMIR** y **TRASLADAR A ANEXOS** el análisis exploratorio de segundo corredor y decisiones descartadas. Evidencia: «La distribución de poses y la métrica se congelaron…» (`:159`); «segundo corredor bajo S1» (`:196`). Mantener ecuaciones, parámetros, semilla por caso y controles que aseguran comparabilidad. Compactar la justificación repetida del margen y trasladar el examen de S2/S3/S4, densidad ósea y morfología sacra a limitaciones/anexo, indicando claramente que no se muestrearon. **Figura:** pose base y perturbaciones radial/angular en el plano perpendicular; con flechas y parámetros de la tabla, vuelve más accesible la ecuación.

- **A-028 — Admisibilidad quirúrgica (SAP)** (`:339–366`; 985 → **650**). **COMPRIMIR**. Evidencia: «SAP tiene dos componentes» (`:341`) y la definición de brecha (`:343–350`). La ecuación de breach, escala, unidad de Wasserstein-1 y referencia clínica son necesarias. En cambio, el razonamiento repetido sobre no ajustar parámetros, la ausencia de regla de decisión y el rechazo de restringir cohorte (`:361–365`) puede reducirse a una nota de diseño y una limitación. La explicación de los seis controles puede remitirse a tabla. **Figura:** esquema de medición de protrusión máxima y asignación de grados; tabla pequeña de distribuciones clínicas puede acompañar la ecuación W1. **No eliminar** la distinción entre comparación descriptiva y prueba de equivalencia.

## Repeticiones entre capítulos con ubicaciones

- **Brecha y necesidad de poses + apariencia:** introducción `:62–68, :72`; estado del arte `capitulo2.tex:32–51, :52–83, :108–128`; marco teórico `capitulo1.tex:73–92, :93–116`; metodología `capitulo3.tex:95–98, :157–160`. Asignar: introducción formula; capítulo 2 prueba con literatura; capítulo 1 define términos; capítulo 3 especifica el procedimiento.
- **Difusión, inpainting y generación fuera de máscara:** introducción `:9, :41`; capítulo 1 `capitulo1.tex:117–144`; capítulo 2 `capitulo2.tex:14–31, :84–107`; capítulo 3 visión general `capitulo3.tex:11–41`. Conservar teoría mínima en capítulo 1, comparación en capítulo 2 y especificación en capítulo 3.
- **Brecha cortical, corredor y comparación clínica:** introducción `:39, :43`; capítulo 1 `capitulo1.tex:93–116`; metodología `capitulo3.tex:99–118, :157–200, :339–365`. Objetivos solo deben nombrar la métrica; definición formal y protocolo, una vez en metodología, apoyados por teoría concisa.
- **Datos metálicos anotados escasos y límites de cohorte:** introducción `:7, :60, :76–78`; capítulo 3 `:42–71`. Introducción puede conservar la cifra publicada como motivo; auditoría local y composición exacta deben estar solo en datos/metodología.
- **Atribución de multiventana y banda de 12 mm:** introducción `:41, :72`; capítulo 2 `:84–107`; capítulo 3 `:41`; glosario `docs/03-glosario.md:25–41`. Definir la adopción y su novedad una vez; preservar la salvedad de atribución.

## Nuevo índice propuesto

1. **Introducción:** contexto y tensión computacional; pregunta; objetivos; contribución esperada; alcance y exclusiones deliberadas. Sin resultados detallados ni limitaciones descubiertas después.
2. **Fundamentos:** TC/HU y representación; artefactos metálicos; anatomía y corredor; conceptos de diffusion necesarios; métricas y estadística estrictamente usadas.
3. **Estado del arte y brecha:** síntesis de lesiones; MAR/simulación física; planificación de tornillos; tabla comparativa común y brecha final alineada con la pregunta.
4. **Metodología:** visión general (figura); cohortes; compuerta; corredor y geometría; distribución preinscrita; SAP. Anexo para auditorías extensas, parámetros de búsqueda y controles secundarios.
5. **Resultados y discusión** y capítulos posteriores quedan fuera de esta ronda.

## Estimación de reducción

| Unidad | Palabras actuales | Propuesta | Reducción |
|---|---:|---:|---:|
| Introducción | 5,628 | 2,210 | 3,418 |
| Capítulo 1 | 7,057 | 4,200 | 2,857 |
| Capítulo 2 | 7,072 | 2,750 | 4,322 |
| Capítulo 3, alcance auditado | 8,273 | 4,950 | 3,323 |
| **Total revisado** | **28,030** | **14,110** | **13,920** |

Para páginas, la referencia general disponible es el documento completo de unas 58,000 palabras en 207 páginas (≈280 palabras/página). A esa densidad, la reducción equivale a **unas 50 páginas**. Es una estimación, no una conversión exacta: ecuaciones, tablas y las nuevas figuras alteran la paginación. Las figuras sugeridas reemplazan explicación repetida y pueden conservar o incluso aumentar páginas aunque reduzcan palabras; el objetivo es mejorar legibilidad y flujo, además de acortar.