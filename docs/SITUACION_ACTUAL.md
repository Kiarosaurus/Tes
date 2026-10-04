# Situación actual de MetalSynth-Pelvis

> Corte del estado: 3 de octubre de 2026. Este documento explica el proyecto en lenguaje simple. Distingue entre lo que ya se ejecutó, lo que todavía necesita revisión y lo que solo está planeado. Sus fuentes principales son [`ESTADO.md`](ESTADO.md) y [`04-implicancias.md`](04-implicancias.md).

## Resumen en pocas palabras

La tesis intenta hacer dos cosas:

1. proponer una posición razonable para un tornillo en una pelvis; y
2. modificar una tomografía para que parezca que ese tornillo está realmente allí, con las rayas y zonas oscuras que suele producir el metal.

La primera parte ya tiene una corrida completa. El programa propuso **3,600 posiciones de tornillo en 72 pelvis** y las calificó automáticamente según cuánto saldría el tornillo del hueso. También se hizo una segunda corrida de sensibilidad con **2,450 posiciones en 49 pelvis**.

Eso no significa todavía que un médico haya validado las 3,600 posiciones. Significa que el programa funciona y que sus resultados se pueden comparar con una distribución clínica publicada.

La segunda parte, la que debe crear la apariencia del metal, todavía no está terminada. Existe código de entrenamiento y se hizo un piloto corto para medir tiempo y memoria, pero **el proyecto aún no ha generado una tomografía sintética final**.

Además, mientras se redactaba la tesis aparecieron decisiones y controles pendientes. Algunos podrían cambiar la interpretación del resultado de las posiciones e incluso obligar a repetir la corrida.

## 1. ¿Qué problema quiere resolver?

Un tornillo metálico no aparece en una tomografía como una pieza limpia y aislada. También produce rayas claras y oscuras alrededor. Por eso no basta con dibujar un tornillo encima de una imagen.

El proyecto busca una cadena como esta:

`pelvis sin metal -> posición del tornillo -> máscara del tornillo -> apariencia del metal y su artefacto`

La idea es que la posición respete la anatomía de cada paciente y que la imagen final conserve la anatomía que no debería cambiar.

El uso futuro sería crear más ejemplos para entrenar sistemas médicos. Sin embargo, esta tesis **no evaluará si esos ejemplos mejoran un segmentador óseo**. Solo intenta evaluar la coherencia geométrica, quirúrgica y visual de lo sintetizado.

## 2. Las palabras más importantes, sin jerga

### Corredor óseo

Es el “túnel” de hueso por el que podría pasar un tornillo. El programa busca una línea y calcula el cilindro más grueso que cabría alrededor de ella sin salir del hueso.

### `Dmax`

Es el diámetro máximo de ese cilindro. No es el diámetro de toda la pelvis ni el de un tornillo real. Es una estimación del espacio disponible en la mejor trayectoria encontrada.

### Pose

Es la posición completa de un tornillo: punto por el que pasa, dirección, longitud y diámetro.

### Brecha cortical

Es cuánto sobresale el tornillo del límite exterior del hueso. El proyecto usa cuatro grados:

- grado 0: no sobresale;
- grado 1: sobresale menos de 2 mm;
- grado 2: sobresale entre 2 y 4 mm;
- grado 3: sobresale más de 4 mm.

Estos cortes son una convención geométrica tomada de literatura previa. No deben presentarse como una garantía universal de seguridad clínica.

### SAP

SAP significa *Surgical Admissibility of Placement*. Es la forma en que el proyecto resume si las posiciones propuestas se parecen a posiciones quirúrgicamente admisibles.

Hoy su resultado más sólido es la distribución de grados de brecha y su comparación con datos clínicos publicados. SAP **no sustituye el juicio de un cirujano**.

### Máscara anatómica

Es un volumen en el que cada vóxel dice si pertenece o no a una estructura, por ejemplo el sacro o un ilion. El proyecto usa máscaras creadas por TotalSegmentator para representar el hueso.

### Banda de generación

Es la región que el sintetizador puede modificar. Incluye el tornillo y unos 12 mm alrededor para permitir que aparezca parte del artefacto metálico fuera del tornillo.

## 3. Estado real de cada objetivo

### Objetivo 1: comprobar si el autoencoder conserva los HU — ejecutado, resultado negativo

Primero se quería usar difusión latente. En ese enfoque, un autoencoder comprime la tomografía antes de generar la imagen.

La prueba exigía un error menor de **25 HU** en hueso. Se evaluaron seis combinaciones en 34 pacientes de prueba. Ninguna pasó. La mejor obtuvo **61.72 HU**.

Por eso el resultado fue **No-Go**: se abandonó la ruta latente con ese autoencoder y el sintetizador se rediseñó para trabajar directamente sobre los valores de la tomografía.

Una aclaración importante: la conversión entre HU y la representación de varias ventanas, cuando se prueba **sin** autoencoder, sí vuelve al valor original prácticamente sin error. El problema medido fue la compresión del autoencoder, no la idea de usar varias ventanas.

### Objetivo 2: proponer posiciones de tornillo — corrida hecha, cierre metodológico pendiente

El programa ya:

- localiza referencias anatómicas;
- usa máscaras del sacro, S1 y ambos iliones;
- busca un corredor óseo;
- propone posiciones alrededor de ese corredor; y
- calcula la brecha cortical de cada posición.

La corrida principal produjo:

| Resultado | Valor |
|---|---:|
| Pelvis | 72 |
| Posiciones | 3,600 |
| Grado 0 | 51.5% |
| Grado 1 | 31.4% |
| Grado 2 | 11.1% |
| Grado 3 | 6.0% |
| Distancia a la serie navegada | 0.206 |
| Distancia a la serie convencional | 0.230 |

La distancia usada es Wasserstein-1: cuanto menor es, más parecidas son las distribuciones. El resultado completo quedó un poco más cerca de la serie navegada, pero **no se definió antes de la corrida qué valor contaría como aprobar o fallar**. Por eso no corresponde decir simplemente “el muestreador fue validado”.

También se encontró que **15 de las 72 pelvis** tienen un corredor menor que 7 mm. En esas pelvis, hasta el eje ideal puede producir brecha si se evalúa con un tornillo de 7 mm.

Al mirar solo las 57 pelvis cuyo corredor sí admite ese calibre, el grado 0 sube a **64.2%**, cerca del **69%** publicado para colocación navegada, y la distancia baja a **0.183**. Este análisis se hizo después de ver el resultado y está declarado como análisis *post hoc*.

La corrida de sensibilidad usó 49 pelvis y 2,450 posiciones. Produjo una distribución parecida y una distancia de **0.186** frente a la serie navegada.

### Objetivo 3: crear la apariencia del metal — todavía no ejecutado de punta a punta

Ya existen:

- extracción y preparación de ejemplos de entrenamiento;
- código del modelo de difusión en el dominio de imagen;
- código de entrenamiento; y
- un piloto de 200 pasos para medir costo computacional.

El piloto usó unos **3.35 GB** de una GPU de 48 GB. El ritmo estable medido fue de unos **0.092 segundos por paso**, que proyecta cerca de **0.77 horas para 30,000 pasos** con esa configuración.

Ese piloto solo midió costo. No midió calidad. El único modelo guardado viene de esa prueba corta y no es un resultado final.

Todavía faltan:

- conectar geometría, pose, máscara, generación y evaluación;
- definir el banco final de geometrías de tornillo;
- conectar la validación al entrenamiento;
- entrenar la corrida final;
- generar las primeras imágenes sintéticas;
- implementar las métricas de apariencia; y
- ejecutar la comparación con copia y pegado y con el protocolo físico.

En términos directos: **todavía no hay una imagen final producida por el sintetizador**.

### Objetivo 4: métricas — SAP existe; las métricas de apariencia siguen pendientes

SAP ya tiene código, controles y resultados. Las métricas de apariencia del metal todavía no están implementadas de punta a punta.

Además, faltan decisiones sobre cómo invertir las métricas de reducción de artefacto para usarlas en síntesis y sobre qué resultado haría fallar el sintetizador.

## 4. Lo que sí se puede afirmar hoy

- La base local fue auditada y los duplicados se manejaron por paciente para evitar mezclar a la misma persona entre entrenamiento y prueba.
- TotalSegmentator se ejecutó y sus máscaras se sometieron a controles de calidad.
- El error del autoencoder se midió y la ruta latente no cumplió la regla fijada.
- El muestreador y SAP existen, corren y produjeron resultados reproducibles.
- Se generaron miles de posiciones, no imágenes sintéticas finales.
- El tiempo de entrenamiento del renderizador no parece ser el principal problema. El problema actual es conectar y evaluar la cadena completa.
- Los capítulos 1, 2 y 3 y parte de la introducción fueron redactados y compilan, pero conservan decisiones marcadas como pendientes.

## 5. Lo que todavía no se debe afirmar

- No se debe decir que el sistema completo ya sintetiza tomografías con metal.
- No se debe decir que las 3,600 posiciones fueron aprobadas por un médico.
- No se debe decir que SAP demuestra seguridad clínica.
- No se debe decir que todas las pelvis usadas estaban libres de fractura. La selección comprobó ausencia de osteosíntesis, no ausencia de fractura.
- No se debe decir que el corredor estrecho siempre es una variación anatómica normal.
- No se debe decir que el modelo mejora la segmentación ósea; esa evaluación está fuera del alcance actual.

## 6. Revisiones y decisiones que todavía pueden cambiar el resultado

### Revisión de 16 casos por diferencias entre dos recortes

Todas las cifras principales del Objetivo 2 usan las máscaras obtenidas con un recorte de 6 mm. Hay 16 casos en los que el resultado difiere de manera importante frente al recorte de 3 mm o aparece una estructura desplazada.

Un agente ya revisó las láminas y encontró 14 casos sin error visible y 2 fallos del recorte de 3 mm, pero esa revisión no reemplaza la revisión humana prevista. La planilla de la autora sigue pendiente.

Archivos:

- [`e9ts_revision_laminas.md`](../experiments/objetivo2/e9ts_revision_laminas.md)
- [`e9ts_revision_laminas_autora.csv`](../experiments/objetivo2/e9ts_revision_laminas_autora.csv)

### Cribado ciego de fracturas en 30 casos

Se confirmó una fractura en `CLINIC_0060`. Ese caso está entre los corredores estrechos. Si las fracturas fueran más frecuentes en ese grupo, parte del estrechamiento atribuido a anatomía normal podría deberse a patología.

Por eso se preparó una revisión ciega de:

- los 15 casos con corredor menor de 7 mm; y
- 15 controles escogidos entre los corredores que sí admiten 7 mm.

El revisor no debe saber a qué grupo pertenece cada caso. Esta revisión está lista, pero sigue sin llenar.

Archivos:

- [`r3_fractura_revisor.md`](../experiments/objetivo2/r3_fractura_revisor.md)
- [`r3_fractura_revisor.csv`](../experiments/objetivo2/r3_fractura_revisor.csv)

### Diferencia entre la envolvente decidida y la implementada

La decisión escrita decía aplicar un cierre y también rellenar cavidades cerradas dentro de la máscara de hueso. El código que produjo los resultados aplicó el cierre, pero no ese relleno.

Hay que decidir entre:

1. corregir la descripción para que diga exactamente lo que se ejecutó; o
2. corregir el código y repetir la medición del corredor y SAP.

**Medición preliminar (2026-10-03).** Sobre los dos únicos casos que tienen máscaras en esta
computadora, añadir el relleno cambia muy poco o nada: 0 vóxeles en uno y 394 en el otro
(0.025 % del hueso, 0.17 cm³), y el diámetro del corredor **no se movió** en ninguno de los dos.

Hay una razón: el relleno existía para tapar el hueco interno de una máscara hecha por umbral de
densidad, que queda como una cáscara. Las máscaras que se usan ahora vienen de un segmentador que ya
entrega el hueso macizo, así que no hay hueco que tapar. Eso apunta a la opción 1, corregir el texto.

**Pero dos casos no son 152.** Para decidirlo con evidencia está preparado `e14_relleno_envolvente.py`,
que mide lo mismo en toda la colección sin rehacer nada. Es un trabajo de minutos y debe correr en
Khipu, porque las máscaras de los 152 casos solo están allá.

Hasta resolverlo, las cifras actuales corresponden a la envolvente **sin relleno de cavidades**.

### Nombre y tipo exacto del tornillo

La trayectoria implementada va desde la cortical externa de un ilion hasta la cortical externa del otro. Es decir, cruza ambas articulaciones sacroilíacas.

Los documentos usan de manera inconsistente “iliosacro”, “transsacro” y “transiliosacro”. Antes de pedir una evaluación clínica de la posición, hay que decidir qué tipo de tornillo representa realmente esa geometría y si la referencia clínica elegida es comparable.

## 7. Aclaración sobre “el último experimento de ver la posición de los tornillos”

Hoy hay tres tareas distintas que podrían confundirse:

| Tarea | Qué se mira | Quién la hace | Estado |
|---|---|---|---|
| E13 / SAP | Las 3,600 posiciones y cuánto salen del hueso | El programa | Ejecutada |
| Revisión de 16 casos | Si las máscaras y el corredor cambian por el recorte | Autora/revisor de imágenes | Pendiente |
| Cribado de 30 casos | Si hay fractura y dónde | Idealmente radiólogo o traumatólogo | Preparado y pendiente |

**No hay todavía en el repositorio una planilla terminada para que un médico califique directamente una muestra de las posiciones sintéticas.** Si eso es lo que se quiere hacer, debe prepararse como una evaluación nueva y no presentarse como si ya formara parte de E13.

### Qué tarea le corresponde a quién

De las dos revisiones preparadas, **solo una necesita a un médico**:

- **La revisión de 16 casos (recorte) no es clínica.** Se juzga si la máscara del hueso quedó cortada o
  incompleta, comparando dos versiones de la misma imagen. Es un juicio sobre el procesamiento, no sobre
  el paciente, y lo hace la autora.
- **El cribado de 30 casos sí es clínico**, y es la tarea que encaja con un médico general o recién
  egresado: decir si ve fractura, dónde, y si la imagen permite juzgarlo. `dudoso` es respuesta válida.
  La planilla ya pide la especialidad del revisor, precisamente para que el resultado se reporte con su
  nivel de formación y no como lectura de especialista.

La revisión de las **posiciones de los tornillos** —la que sí querría un traumatólogo de pelvis— todavía
no está preparada, y la sección 8 describe lo que haría falta para montarla.

## 8. Cómo pedirle ayuda a un médico para revisar las posiciones

### ¿A qué médico conviene pedirle?

Para juzgar si una trayectoria es quirúrgicamente razonable, la mejor persona sería un **traumatólogo u ortopedista con experiencia en cirugía de pelvis y acetábulo**.

Un **radiólogo** puede ayudar muy bien a identificar el nivel anatómico, la salida del tornillo fuera del hueso y su relación con el canal o los forámenes. Sin embargo, no conviene atribuirle una validación de técnica quirúrgica si esa no es su experiencia.

Si solo se consigue un médico general, su revisión todavía puede registrarse, pero hay que escribir claramente su grado de formación y no llamarla revisión de especialista.

### Qué pedirle exactamente

No conviene decir solamente “¿puede ver si los tornillos están bien?”. Esa pregunta es ambigua. La tarea debe separar, por caso:

1. **¿La imagen permite juzgar la trayectoria?** `sí / no / dudoso`.
2. **¿El nivel anatómico es el esperado?** Por ejemplo, S1 u otro nivel.
3. **¿El tornillo permanece dentro del corredor óseo?** `sí / no / dudoso`.
4. **Si sale del hueso, por dónde y cuánto aproximadamente?** Canal, foramen, parte anterior, parte superior u otra dirección.
5. **¿La orientación, el punto de entrada y la longitud parecen plausibles para la técnica que se quiere representar?**
6. **¿Hay alguna estructura en riesgo que el cálculo automático no esté representando?**
7. **Comentario libre.**

No se le debe mostrar de antemano el grado calculado por SAP si se quiere una lectura independiente. Las posiciones deberían estar barajadas y mostrar solo un identificador anónimo.

Tampoco conviene pedirle que revise las 3,600 posiciones. Primero hay que fijar por escrito el propósito de la revisión y seleccionar una muestra que lo responda. Por ejemplo, comprobar si el grado automático coincide con el juicio humano requiere incluir casos de todos los grados; estimar la frecuencia real de posiciones aceptables requiere otro tipo de muestreo. Esa selección debe decidirse antes de mirar los resultados del médico.

### Mensaje listo para copiar

> Hola, Dr./Dra. [apellido]. Soy Kiara y estoy desarrollando una tesis sobre generación de tomografías pélvicas con tornillos de fijación. Una parte del proyecto propone automáticamente trayectorias de tornillo a partir de la anatomía de cada pelvis. Ya puedo medir con un programa cuánto se sale cada trayectoria del hueso, pero necesito una revisión clínica independiente para saber si las posiciones mostradas también parecen anatómica y quirúrgicamente razonables.
>
> ¿Podría ayudarme revisando una muestra de casos anonimizados? En cada caso le mostraría la tomografía en varios planos con el eje y el volumen del tornillo superpuestos. Le pediría indicar si el caso es evaluable, si la trayectoria permanece en el corredor óseo, si existe perforación y en qué dirección, y si la orientación, entrada y longitud le parecen plausibles para la técnica representada. “Dudoso” sería una respuesta válida; no necesito que fuerce una decisión.
>
> La revisión es para investigación: no corresponde a pacientes en atención, no busca emitir diagnósticos ni pedirle que certifique la seguridad del programa. Su evaluación se reportaría con su especialidad y nivel de experiencia, según usted autorice. Antes de empezar le enseñaría unos pocos ejemplos para confirmar que las imágenes y las preguntas sean suficientes.
>
> Si este tipo de fijación no está dentro de su práctica habitual, ¿podría indicarme qué especialista sería el más adecuado?

Antes de enviar el mensaje, se debe reemplazar “tornillo de fijación” por el nombre anatómico ya resuelto y comprobar que las imágenes estén anonimizadas y que su uso y transferencia cumplan las reglas de la universidad y del conjunto de datos.

### Qué material habría que preparar para esa revisión

- una explicación de una página, sin código ni jerga de aprendizaje automático;
- una definición exacta del tornillo y de la técnica que se representa;
- cortes axial, coronal y sagital, idealmente con posibilidad de recorrer el volumen;
- el eje y el grosor real del tornillo superpuestos;
- una planilla con opciones cerradas y un campo de comentario;
- una muestra definida antes de recibir respuestas;
- casos barajados, sin mostrar el resultado de SAP;
- nombre, especialidad y experiencia del revisor, con su autorización; y
- una regla para resolver casos `dudoso` o imágenes no evaluables.

Si es posible, dos revisores permitirían medir cuánto concuerdan entre sí. Si solo participa uno, también sirve, pero debe declararse como limitación.

## 9. Si la ayuda que se busca es para el experimento ya preparado

El único paquete médico listo hoy no pregunta por la calidad de las posiciones. Pregunta si existe **fractura** en 30 casos ciegos. Para esa tarea el mensaje correcto sería:

> Hola, Dr./Dra. [apellido]. En mi tesis medí automáticamente el espacio disponible para un tornillo en tomografías pélvicas. Encontré algunos corredores muy estrechos, pero la base fue seleccionada por no tener material de osteosíntesis, no por estar libre de fractura. Necesito una revisión ciega de 30 casos anonimizados para registrar si se observa fractura (`sí`, `no` o `dudoso`), dónde se encuentra y si las imágenes permiten juzgarla. Los casos están mezclados y no le diría cuáles tienen corredor estrecho para no influir en su lectura. ¿Podría ayudarme con esta revisión o recomendarme un radiólogo o traumatólogo que pueda hacerla?

Las instrucciones exactas ya están en [`r3_fractura_revisor.md`](../experiments/objetivo2/r3_fractura_revisor.md). No debe entregarse al revisor el archivo `r3_fractura_grupos.csv`, porque revelaría los grupos y rompería el cegamiento.

## 10. Próximos pasos, en orden práctico

1. Decidir qué tornillo representa la trayectoria: iliosacro o transiliosacro.
2. Resolver si se conserva la envolvente ósea realmente ejecutada o si se corrige el código y se repite E9-TS/SAP.
3. Completar la revisión humana de los 16 casos de recorte.
4. Conseguir un radiólogo o traumatólogo para el cribado ciego de fracturas de 30 casos.
5. Si se desea validación clínica directa de las posiciones, escribir y congelar primero su protocolo, preparar las imágenes y recién después solicitar la lectura médica.
6. Terminar la cadena del Objetivo 3: geometría, pose, máscara, generación y métricas.
7. Generar y revisar las primeras imágenes sintéticas antes de una corrida final.
8. Resolver las decisiones de redacción marcadas en los capítulos y alinear título, pregunta, objetivos y alcance.

## 11. Lectura honesta del progreso

El proyecto ya tiene un resultado defendible del Objetivo 1, aunque sea negativo, y un resultado cuantitativo grande del Objetivo 2. Eso es bastante más avanzado que el estado del 14 de septiembre.

Al mismo tiempo, el resultado del Objetivo 2 todavía depende de controles humanos y de una decisión sobre la máscara ósea. El Objetivo 3 sigue incompleto porque nunca produjo una muestra final.

La forma más precisa de decirlo es:

> La representación latente fue puesta a prueba y no pasó; el muestreador de posiciones ya fue implementado y ejecutado, pero su cierre clínico y metodológico sigue pendiente; el sintetizador de apariencia tiene código y un piloto de costo, pero todavía no ha generado ni evaluado imágenes finales.

## 12. Archivos clave para retomar

- Estado general: [`ESTADO.md`](ESTADO.md)
- Hallazgos y riesgos: [`04-implicancias.md`](04-implicancias.md)
- Mapa de experimentos del Objetivo 2: [`EXPERIMENTOS.md`](../experiments/objetivo2/EXPERIMENTOS.md)
- Resultado principal de SAP: [`e13_sap.md`](../experiments/objetivo2/e13_sap.md)
- Análisis por corredor viable/estrecho: [`e13b_estratificado.md`](../experiments/objetivo2/e13b_estratificado.md)
- Revisión de los 16 casos: [`e9ts_revision_laminas.md`](../experiments/objetivo2/e9ts_revision_laminas.md)
- Cribado de fracturas: [`r3_fractura_revisor.md`](../experiments/objetivo2/r3_fractura_revisor.md)
- Documento de entrega: [`overleaf/`](../overleaf/)
