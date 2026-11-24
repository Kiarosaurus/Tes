# Auditoría científica prospectiva — TC e imagen musculoesquelética

**Alcance.** Revisé únicamente `review/`: los capítulos y conclusiones indicados, la rúbrica, la data card, el glosario, el código de representación y los resultados del Objetivo 3 disponibles. Las propuestas son recomendaciones, no instrucciones para entrenar o modificar configuraciones. Los resultados exploratorios posteriores que sí aparecen en el manuscrito se interpretan como exploratorios; los nuevos experimentos que el encargo señala como aún no reportados quedan **NO VERIFICABLES**.

## Dictamen

La tesis separa correctamente dos preguntas distintas: si la colocación concuerda con distribuciones clínicas y si la apariencia concuerda con un protocolo de simulación física. No debe colapsar ninguna de ellas en “realismo” sin definir ese constructo. Conviene mantener explícitas estas tres dimensiones:

- **Realismo perceptual:** cuánto se parece una imagen, bajo condiciones de visualización concretas, a ejemplos que una persona considera plausibles o reales.
- **Fidelidad física o anatómica:** cuánto reproduce mecanismos de formación de TC y conserva estructuras e intensidades anatómicas.
- **Utilidad clínica:** si el material ayuda en una tarea clínica o computacional concreta, como segmentar hueso alrededor del implante.

Una prueba de Turing visual solo aportaría evidencia sobre la primera dimensión. No demostraría fidelidad física o anatómica ni utilidad diagnóstica.

La evidencia disponible ya muestra por qué la amplitud de colas no basta: en la banda completa la amplitud sintética mediana es menor que la del protocolo físico (1308 frente a 1574 HU), pero en anillos de 8–12 mm la supera; el perfil sintético es más plano. También hay evidencia de generación de textura no observada en los controles —«estática» y «textura sobrepuesta»— en la evaluación visual exploratoria descrita por la tesis. Por tanto, una cifra de amplitud o un juicio visual aislado no debería decidir si una variante es mejor.

**Prioridad general:** antes de cerrar los experimentos, hace falta fijar qué afirmaciones se harán y evaluar con métricas directas los riesgos de recorte, pérdida anatómica y textura artificial. No veo evidencia de que sea científicamente necesario ejecutar todos los experimentos adicionales de pérdidas de textura, perceptual y adversarial. Son exploratorios mientras no tengan resultados, y su valor depende de una pregunta y un criterio fijados antes de comparar variantes.

---

## Hallazgos

### MED-01 — Definir el constructo y limitar la afirmación de “realismo”

- **Ubicación:** [introduccion.tex:13-15](/home/kiara/audit_ws/review/thesis/secciones/introduccion.tex:13); [capitulo3.tex:614-616](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:614); [conclusiones.tex:30, 38](/home/kiara/audit_ws/review/thesis/secciones/conclusiones.tex:30).
- **Evidencia:** la introducción plantea “coherencia física”; el capítulo 3 dice que la *streak amplitude* crece con “cualquier desviación extrema, tenga o no estructura de raya”. La conclusión declara que “el realismo visual […] no se reclama”.
- **Descripción:** el manuscrito reconoce la diferencia entre apariencia visual y coherencia con el simulador, pero el término “realismo” todavía puede leerse como una afirmación global. Una puntuación perceptual no valida la formación del artefacto por *beam hardening*, *photon starvation* o *partial volume*, ni que la interfaz tornillo-hueso sea anatómicamente correcta.
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** una afirmación no acotada podría convertir resultados de percepción o de métricas indirectas en una conclusión física o clínica que no sustentan.
- **Acción recomendada — INDISPENSABLE antes del cierre experimental:** para cada variante nueva, declarar por anticipado si la pregunta es perceptual, física, anatómica o de tarea. Informar esos resultados por separado. Si ninguna nueva evaluación responde a una pregunta definida, conservarla como trabajo futuro, sin incorporarla como evidencia de mejora.
- **Experimento/analisis propuesto:** comparación exploratoria de las variantes respecto de una métrica perceptual y controles anatómicos definidos por separado. **Pregunta:** ¿la variante altera la plausibilidad visual sin deteriorar anatomía o valores de TC? **Evidencia nueva:** resultados separados por constructo. **Riesgo que resuelve:** confundir apariencia con física o anatomía. **Coste:** medio; requiere lectura y análisis, aunque no necesariamente GPU adicional. **Si se omite:** las variantes no podrán respaldar una afirmación de realismo perceptual y su efecto en fidelidad anatómica seguirá sin medir.
- **Dependencias:** MED-02, MED-03 y MED-06.

### MED-02 — Auditar saturación y representación de HU, en especial dentro de `G`

- **Ubicación:** [capitulo1.tex:51-71](/home/kiara/audit_ws/review/thesis/secciones/capitulo1.tex:51); [capitulo3.tex:204-208, 218-220](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:204); [capitulo4.tex:134-138](/home/kiara/audit_ws/review/thesis/secciones/capitulo4.tex:134).
- **Evidencia:** la compresión `asinh` representa HU en `[-1000, 20000]`; la tesis reconoce que “acota por abajo” la representación y que la regla preinscrita sobre el suelo “no se aplicó”. En la región de medición del protocolo físico, hasta 0.017 de los vóxeles queda bajo el suelo; en el sintetizador, 0.000.
- **Descripción:** la ida y vuelta exacta de la codificación en ciertos canales no implica que la salida generada conserve valores físicos. El límite inferior censura el aire y puede suprimir la cola oscura; el techo superior también puede censurar implante o extremos hiperdensos. No encontré una distribución reportada de saturación en `M`, interfaz tornillo-hueso y `Bδ` por material o paciente. Para metal, la tesis también muestra diferencias respecto de tornillos reales, pero no basta con un umbral binario para describir la distribución de HU.
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** un resultado puede parecer suavemente limitado por ventana mientras pierde extremos de HU relacionados con rayas oscuras, metal y volumen parcial.
- **Acción recomendada — INDISPENSABLE antes del cierre experimental:** cuantificar por paciente y por región (hueso cortical, hueso esponjoso, partes blandas, interfaz, metal y bandas) las fracciones en los límites, percentiles de HU y errores respecto de la fuente cuando existe referencia. Informar valores antes y después del recorte; no interpretar el umbral de 2500 HU como frontera física del metal.
- **Experimento/analisis propuesto:** auditoría de ocupación de límites y distribuciones de HU de las salidas archivadas. **Pregunta:** ¿las variantes cambian colas o intensidades por saturación, y en qué tejidos? **Evidencia nueva:** fracción censurada y distribución regional de HU. **Riesgo que resuelve:** falsa conservación de HU o pérdida asimétrica de cola. **Coste:** bajo-medio, principalmente postproceso en CPU. **Si se omite:** la fidelidad de los extremos de HU quedará NO VERIFICABLE y no debe inferirse de `MAE` o del *windowing* mostrado.
- **Dependencias:** definición de regiones y registro de la transformación de canales; no requiere nuevos entrenamientos.

### MED-03 — Medir preservación anatómica local y aparición de estructuras artificiales

- **Ubicación:** [introduccion.tex:13](/home/kiara/audit_ws/review/thesis/secciones/introduccion.tex:13); [capitulo3.tex:204, 371-375](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:204); [capitulo4.tex:174-186](/home/kiara/audit_ws/review/thesis/secciones/capitulo4.tex:174).
- **Evidencia:** fuera de `G`, “la preservación […] se cumple por construcción”; dentro de `G`, se regenera el volumen. La mediana del Dice óseo dentro de `G` es 0.677 para el sintetizador y 0.800 para el protocolo físico; la tesis advierte que estas cifras “no indican por sí solas un resultado peor”. En la revisión visual se reportan paneles con “estática” y “textura sobrepuesta”, ausentes en lo real y en el protocolo físico dentro de esa muestra.
- **Descripción:** *bone integrity* con umbral de 150 HU y Dice/cambio de volumen puede pasar por alto adelgazamiento cortical, interrupciones focales, detalles cancelados por volumen parcial o estructura inventada cerca de la interfaz. La restauración exacta fuera de `G` no acredita preservación dentro de `G`. El material no demuestra que las texturas señaladas sean estructuras anatómicas inventadas, pero tampoco ofrece un análisis específico que las descarte.
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** una variante puede producir un artefacto visualmente convincente a costa de alterar hueso o crear patrones no sustentados por la anatomía.
- **Acción recomendada — INDISPENSABLE antes del cierre experimental:** añadir una evaluación regional que separe cortical, esponjoso, partes blandas e interfaz, incluyendo continuidad/contraste del borde óseo y cambios en la imagen fuente fuera de `M`. La inspección de candidatos sospechosos debería comprobarse en cortes ortogonales y en HU, no solo en una ventana de presentación.
- **Experimento/analisis propuesto:** cotejo anatómico y de continuidad en los casos ya generados, idealmente con anotación/revisión independiente de hallazgos sospechosos. **Pregunta:** ¿la variante introduce o elimina rasgos anatómicos locales? **Evidencia nueva:** localización y frecuencia de alteraciones, separadas de la textura del artefacto. **Riesgo que resuelve:** *hallucination* o destrucción de cortical inadvertida por Dice global. **Coste:** medio-alto en tiempo de lectura, bajo en GPU. **Si se omite:** no se podrá sostener preservación anatómica dentro de la región sintetizada; deberá declararse como limitación.
- **Dependencias:** definición anatómica operativa y ventanas reproducibles (MED-07).

### MED-04 — La métrica primaria y el perfil radial no acreditan rayas físicas

- **Ubicación:** [capitulo1.tex:91](/home/kiara/audit_ws/review/thesis/secciones/capitulo1.tex:91); [capitulo3.tex:371-379, 416-418](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:371); [capitulo4.tex:134-164](/home/kiara/audit_ws/review/thesis/secciones/capitulo4.tex:134).
- **Evidencia:** la *streak amplitude* resume el 5 % superior menos el 5 % inferior de desviaciones en un anillo. Los anillos de 8–10 y 10–12 mm exceden el protocolo físico por +478 y +411.7 HU; la razón de amplitudes entre anillos 0–2 y 6–8 mm es 1.92 para el sintetizador y 6.71 para el protocolo físico. La tesis reconoce que los extremos “no tienen por qué tener estructura de raya”.
- **Descripción:** estas métricas capturan colas y perfiles a distancia, pero pueden responder a ruido, discontinuidades o texturas no direccionales; no identifican *beam hardening*, *starvation*, *streaks* ni *partial volume*. El perfil por anillos sí aporta evidencia espacial útil, pero el resultado de los anillos exteriores y la generación nula fuera de `G` limitan cualquier interpretación como reproducción completa del artefacto. La métrica angular posterior también depende de escala sectorial y ruido, que la propia tesis declara.
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** igualdad de amplitud no implica semejanza del patrón ni del mecanismo físico.
- **Acción recomendada — INDISPENSABLE antes del cierre experimental:** reportar conjuntamente amplitud, perfil por anillos y evaluación direccional, describiendo la última como exploratoria y sensible a escala. Para las variantes nuevas, aplicar el mismo cálculo y mostrar datos por paciente, no seleccionar la mejor métrica después de ver el resultado.
- **Experimento/analisis propuesto:** análisis espacial/perfil de las variantes ya generadas, con control nulo sin metal y resúmenes por paciente. **Pregunta:** ¿el cambio de pérdida modifica una estructura direccional y su decaimiento espacial, en vez de solo elevar la varianza? **Evidencia nueva:** separación entre textura de colas y patrón anatómicamente orientado. **Riesgo que resuelve:** mejorar una métrica sin mejorar el artefacto. **Coste:** medio; bajo GPU si hay volúmenes almacenados. **Si se omite:** las variantes podrán compararse por las métricas elegidas, pero no afirmarse que reproducen rayas físicas.
- **Dependencias:** MED-01, MED-02; interpretar la comparación con el protocolo como comparación con un simulador, no verdad de terreno (MED-05).

### MED-05 — El protocolo físico es comparador, no verdad física; falta validación frente a una referencia física

- **Ubicación:** [capitulo3.tex:442-452, 626, 632](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:442); [conclusiones.tex:22, 30](/home/kiara/audit_ws/review/thesis/secciones/conclusiones.tex:22).
- **Evidencia:** la tesis dice que validar el simulador exigiría “un fantoma con material metálico conocido, escaneado en un tomógrafo real” y que no se dispone de esos recursos. También señala que la reconstrucción de la cohorte es desconocida y que el protocolo se validó en dos dimensiones y para MAR.
- **Descripción:** comparación con CatSim/Peters permite coherencia con ese protocolo bajo sus supuestos, pero no prueba que el artefacto sintético sea el que produciría el escáner, reconstrucción o aleación reales. Tampoco separa efectos del material, geometría, parámetros de adquisición, espesor de corte, endurecimiento, inanición y volumen parcial axial.
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** inferir “fidelidad física” de la equivalencia con el protocolo excedería la evidencia.
- **Acción recomendada — TRABAJO FUTURO:** validar el simulador y el sintetizador con adquisiciones de fantoma bajo parámetros de adquisición documentados o con una cohorte de protocolo/reconstrucción conocida. En este manuscrito, mantener la conclusión como comparación con el protocolo físico.
- **Pregunta:** ¿el patrón concuerda con artefactos adquiridos en condiciones controladas? **Evidencia nueva:** medidas reales con material y adquisición conocidos. **Riesgo que resuelve:** sesgo común entre dos métodos alejados de la adquisición clínica. **Coste:** muy alto; requiere fantoma, escáner y protocolo. **Si se omite:** la fidelidad a la física del escáner queda no demostrada.
- **Dependencias:** recursos externos; no bloquea cerrar el experimento actual si se mantiene el reclamo acotado.

### MED-06 — La evaluación perceptual actual es descriptiva, no una prueba de Turing

- **Ubicación:** [capitulo3.tex:526-542](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:526); [conclusiones.tex:30, 38](/home/kiara/audit_ws/review/thesis/secciones/conclusiones.tex:30).
- **Evidencia:** el criterio visual se añadió después de ver resultados, lo puntuó “una sola lectora” y cubre dos pacientes, una semilla y seis paneles por brazo. La tesis calcula que el umbral de 4/6 pares tiene probabilidad 0.34 bajo azar. Los puntajes de protocolo físico y real son 5.00 y 4.83, pero la tesis aclara que no es prueba de discriminación y que ambos están cerca del techo.
- **Descripción:** el cegamiento es nominal: la lectora conoce los modelos y sus defectos. La escala de 1–5 no tiene anclas completas en el manuscrito (consta un marcador editorial pendiente), la ventana es única y la fuente real procede de otro paciente y escáner. Esta condición no justifica clasificar la salida como indistinguible de TC real.
- **Severidad:** alta para cualquier reclamo de realismo; baja para el objetivo actual, que lo excluye. **Confianza:** alta.
- **Acción recomendada — TRABAJO FUTURO:** si se pretende una prueba tipo Turing, diseñarla como estudio independiente con varios lectores, suficientes pacientes y casos, orden aleatorio, ciego efectivo, opción de respuesta forzada “real/sintético” e incertidumbre/confianza; fijar ventanas y presentación antes del estudio. Analizar por paciente y lector. No llamarla evaluación clínica ni utilidad diagnóstica.
- **Pregunta:** ¿los lectores distinguen imágenes reales y sintéticas bajo presentación controlada? **Evidencia nueva:** tasa de discriminación y variabilidad entre lectores/casos. **Riesgo que resuelve:** confundir un puntaje alto o un sesgo de una autora con indistinguibilidad perceptual. **Coste:** alto en coordinación y lectura, poco GPU. **Si se omite:** ninguna conclusión de Turing/perceptual generalizable.
- **Dependencias:** MED-01 y MED-07; no necesario para la tesis si mantiene la exclusión explícita de realismo.

### MED-07 — Ventanas, ITK-SNAP y rejilla: comparabilidad defendible, cobertura limitada

- **Ubicación:** [capitulo3.tex:534-538](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:534); [capitulo1.tex:51-67](/home/kiara/audit_ws/audit_ws/review/thesis/secciones/capitulo1.tex:51).
- **Evidencia:** los paneles visuales usan `[-500, 1300] HU`; una observación informal fue en ITK-SNAP sobre un solo caso. La descripción disponible fija cortes y ventanas, pero no verifica todos los detalles de visualización, como escala espacial común, nivel de zoom, interpolación y revisión multiplanar.
- **Descripción:** la ventana fija y común es defendible para comparar paneles si se aplica idénticamente a real y sintético; hace reproducible esa visualización. No es una evaluación exhaustiva de TC pélvica: recorta valores fuera del intervalo, comprime o elimina contraste de estructuras, y no equivale a inspección de HU nativos. **NO VERIFICABLE** si la rejilla existente garantiza escalas espaciales idénticas, o si incluye vistas multiplanares; el material citado no basta para establecerlo.
- **Severidad:** media. **Confianza:** alta para la limitación de ventana; media para los detalles no registrados.
- **Impacto:** cambios de ventana o escala podrían cambiar visibilidad de rayas, cortical fina, hueso esponjoso, partes blandas, estática y borde del implante.
- **Acción recomendada — RECOMENDABLE si hay capacidad:** documentar el protocolo de visualización (misma ventana, escala física/zoom, interpolación y presentación) y añadir lectura en ventanas de hueso y partes blandas junto con HU nativos; para casos sospechosos, revisar vistas ortogonales. Mantener la rejilla como mecanismo de comparación solo si iguala esas condiciones y los paneles se aleatorizan.
- **Pregunta:** ¿los defectos aparentes persisten bajo ventanas y planos defendibles? **Evidencia nueva:** sensibilidad de los juicios a condiciones de visualización. **Riesgo que resuelve:** que saturación de presentación o escala de la rejilla explique la preferencia. **Coste:** bajo, sin GPU. **Si se omite:** el resultado visual solo será válido para la ventana/presentación documentada.
- **Dependencias:** protocolo ciego MED-06; revisión anatómica MED-03.

### MED-08 — No permitir que los barridos exploratorios reutilicen la prueba para elegir variantes

- **Ubicación:** [capitulo3.tex:297-333, 588-602](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:297); [capitulo3.tex:640-648](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:640).
- **Evidencia:** la tesis documenta que la partición de prueba orientó decisiones de versión 2 y ajuste fino; varias comparaciones son post hoc. Para los resultados exploratorios más recientes, constan límites de dos pacientes en validación, un punto de control, criterios no todos evaluados o fallos de control que hacen el barrido “no interpretable”.
- **Descripción:** con GPU limitada y una autora/evaluadora, un barrido de muchas pérdidas, muestras y semillas aumenta el riesgo de selección por resultado y de confundir cambio de sampler con cambio de modelo. **NO VERIFICABLE**: resultados de los experimentos actuales de pérdidas de textura, perceptual o adversarial que el encargo indica aún no disponibles.
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** las mejoras aparentes podrían ser inestables, escogidas por validación reducida o no separables del ruido entre semillas.
- **Acción recomendada — INDISPENSABLE antes del cierre experimental:** no elegir ni ajustar con la partición de prueba. Para cualquier resultado nuevo, congelar previamente la pregunta, métricas primarias, baselines, variantes que se informarán, manejo de fallos, unidad de análisis y regla de selección. Presentar todas las variantes intentadas, incluidos negativos e incompletos, como exploratorios; reservar prueba para una única evaluación final si todavía se desea una afirmación confirmatoria.
- **Experimento/analisis propuesto:** comparación pareada de variantes ya autorizadas con baseline y control sin término, mismas condiciones de evaluación y más de una semilla donde el coste lo permita. **Pregunta:** ¿un cambio concreto mejora una métrica objetivo de forma repetible y no a costa de otras? **Evidencia nueva:** diferencias por paciente y semilla frente a control. **Riesgo que resuelve:** selección oportunista y efectos de semilla o continuación del entrenamiento. **Coste:** medio-alto de GPU; dado el recurso, limitar el número de brazos mediante una pregunta prioritaria. **Si se omite:** no afirmar mejora del método; presentar las corridas como exploración inconclusa.
- **Dependencias:** MED-01 a MED-04; no iniciar nuevo barrido si aún no se cerró el registro de evaluación.

### MED-09 — Interpretación de SAP/W1: comparación de distribuciones, no validez clínica

- **Ubicación:** [introduccion.tex:37-43](/home/kiara/audit_ws/review/thesis/secciones/introduccion.tex:37); [conclusiones.tex:16, 22](/home/kiara/audit_ws/review/thesis/secciones/conclusiones.tex:16); [capitulo3.tex:606, 610](/home/kiara/audit_ws/review/thesis/secciones/capitulo3.tex:606).
- **Evidencia:** la tesis reporta W1 de 0.206 y 0.230 grados frente a las series clínica navegada y convencional, y declara que no hay regla de decisión. También reconoce que SAP mide protrusión fuera de una envolvente ósea, no perforación de cortical segmentada, y que los grados y su escala equiespaciada son convenciones.
- **Descripción:** W1 sirve para comparar las distribuciones ordinales definidas; no valida exactitud de poses, perforación clínicamente relevante ni seguridad del implante. La anatomía/segmentación y resolución de la referencia limitan su interpretación.
- **Severidad:** media. **Confianza:** alta.
- **Impacto:** evitaría que “cercano a la referencia” se interprete como desempeño clínico o quirúrgico validado.
- **Acción recomendada — INDISPENSABLE antes del cierre experimental:** conservar el resultado como descriptivo, declarar escala convencional y dependencia de la envolvente segmentada. No requiere ampliar experimentos de síntesis.
- **Pregunta/análisis:** no se propone un experimento adicional costoso; la pregunta pertinente para una etapa posterior sería si SAP concuerda con evaluación clínica/anatómica de perforación. **Evidencia nueva:** anotación experta y referencia anatómica adecuada. **Riesgo:** validez de constructo. **Coste:** alto en anotación, no GPU. **Si se omite:** W1 seguirá siendo válida solo como distancia entre distribuciones definidas por el trabajo.
- **Dependencias:** disponibilidad de evaluación experta y referencia mejorada.

---

## Priorización de cierre

**Indispensable:** limitar y congelar las afirmaciones exploratorias (MED-01, MED-08), cuantificar recorte y HU (MED-02), y documentar una comprobación de preservación anatómica local y artefactos artificiales (MED-03). Además, presentar la evidencia física con sus límites, usando perfiles radiales y direccionalidad como métricas complementarias, no como prueba autónoma de rayas (MED-04). Son análisis de riesgo alto que pueden hacerse principalmente sobre resultados existentes; no exigen, por sí mismos, ampliar el entrenamiento.

**Recomendable:** fortalecer la presentación visual con ventanas y escala registradas, HU nativos y lectura multiplanar de los casos seleccionados (MED-07). Con una sola evaluadora, una revisión cualitativa bien documentada es más realista para el cierre que una afirmación estadística de Turing.

**Trabajo futuro:** adquisición con fantoma para fidelidad a la física del escáner (MED-05) y estudio perceptual independiente si se quiere reclamar realismo visual (MED-06). La utilidad para segmentación u otra tarea clínica también queda fuera de lo que prueban estos experimentos; no debe inferirse de una prueba visual.

No recomiendo convertir cada pérdida propuesta en un brazo de entrenamiento obligatorio. Con una sola GPU en cola, la decisión de añadir cada variante debería depender de una hipótesis concreta y de un control que permita interpretar el cambio. El material disponible no permite concluir si los experimentos de pérdidas perceptual, adversarial o textura actuales mejoran realismo, anatomía o física.