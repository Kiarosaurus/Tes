# Situación actual de MetalSynth-Pelvis

> Corte del estado: 5 de octubre de 2026. Este documento explica el proyecto en lenguaje simple. Distingue entre lo que ya se ejecutó, lo que todavía necesita revisión y lo que solo está planeado. Sus fuentes principales son [`ESTADO.md`](ESTADO.md) y [`04-implicancias.md`](04-implicancias.md).

## Resumen en pocas palabras

La tesis intenta hacer dos cosas:

1. proponer una posición razonable para un tornillo en una pelvis; y
2. modificar una tomografía para que parezca que ese tornillo está realmente allí, con las rayas y zonas oscuras que suele producir el metal.

La primera parte ya tiene una corrida completa. El programa propuso **3,600 posiciones de tornillo en 72 pelvis** y las calificó automáticamente según cuánto saldría el tornillo del hueso. También se hizo una segunda corrida de sensibilidad con **2,450 posiciones en 49 pelvis**.

Eso no significa todavía que un médico haya validado las 3,600 posiciones. Significa que el programa funciona y que sus resultados se pueden comparar con una distribución clínica publicada.

La segunda parte, la que debe crear la apariencia del metal, **cambió mucho en las últimas dos semanas**. Pasó de no tener ninguna imagen a tener dos entrenamientos completos en el clúster y varias muestras sintéticas que se pueden abrir y mirar. Lo que todavía **no** existe es la cadena completa: hoy el modelo *reconstruye* el metal en pacientes que ya lo tenían, pero nunca se ha colocado un tornillo en una pelvis limpia de punta a punta.

Y aparecieron tres cosas que no estaban previstas: el entrenamiento **se degrada** si se prolonga, la representación de la imagen **no puede expresar** una parte del artefacto, y el criterio con que se elige el mejor modelo **puede estar midiendo lo que no importa**. Las tres están medidas y registradas; ninguna estaba en el plan.

## Lo que avanzó en las últimas dos semanas (21 de septiembre al 5 de octubre)

Es el tramo con más experimentos de todo el proyecto. Conviene leerlo como tres frentes.

### Frente 1: el sintetizador pasó de no existir a entrenar dos veces

**Antes de la tabla, de dónde salen los datos**, porque es fácil confundirlo con otra parte de la tesis:

- **La entrada son tomografías de `dataset7` (CLINIC-metal), o sea pacientes que SÍ tienen un implante metálico real.** Eso es a propósito: el renderizador tiene que aprender cómo se ve el metal y su artefacto, así que necesita ejemplos donde el metal exista. Son **47 pacientes** para entrenar y **3 pacientes** para vigilar el entrenamiento, **todos con implante**.
- **Nada de esto tiene que ver con el cribado de fracturas.** Ese cribado (20 de 30, sección 6) se hizo sobre la cohorte del **Objetivo 2**, que es la contraria: pelvis **sin** osteosíntesis, las que reciben el tornillo sintético. Son dos conjuntos de pacientes distintos y dos preguntas distintas. En los pacientes de `dataset7` **no se midió** el porcentaje de fracturas, y no hacía falta: ahí no se coloca ningún tornillo, solo se aprende la apariencia del que ya está.

| Paso | Qué hizo | Resultado |
|---|---|---|
| Preparación de ejemplos | Recortó y guardó los parches de entrenamiento, uno por implante y corte | **23,058 parches** en el disco, de los cuales el criterio de inclusión admite **17,149** |
| Criterio de inclusión | Fijó por escrito **antes** de entrenar qué parches entran | Lista congelada y auditable: **47 pacientes** de entrenamiento y **3** de validación |
| Primera muestra | Llamó por primera vez a la función que genera | **La cadena funciona**: los dos controles de preservación pasan exactos |
| Primer entrenamiento real | 144,500 pasos, 8 horas de GPU | **Sobreajuste**: el modelo empeoró durante las últimas 6 h 30 |
| Segundo entrenamiento | 60,000 pasos, 6 h 20 | Confirmó el sobreajuste **con el instrumento corregido** |
| Muestra de serie completa | 66 cortes consecutivos de un paciente | Dos páginas web navegables y volúmenes para abrir en un visor médico |

**Aquí "validación" significa una cosa muy concreta, y conviene fijarla.** En aprendizaje automático, *validación* son pacientes que el modelo **no usa para aprender** y que sirven para vigilar si va mejorando o empeorando. Aquí son **3 pacientes con implante**, apartados desde el principio. No tiene nada que ver con "validar clínicamente" ni con el cribado de fracturas: es un termómetro del entrenamiento.

**El dato más importante del primer entrenamiento no fue el modelo, fueron dos defectos encontrados.** El primero: ese termómetro sorteaba datos distintos cada vez que medía, así que la cifra oscilaba un 15 % por *cómo* se medía y no por cómo iba el modelo. El segundo, peor: el programa guardaba un solo archivo y lo sobrescribía, así que **las pesas del mejor momento del entrenamiento se perdieron**. Las dos cosas están corregidas y el segundo entrenamiento ya guarda el mejor modelo aparte.

**Y el sobreajuste resultó real, no un error de medición.** Con el termómetro arreglado, la calidad mejora hasta cerca de los 30,000 pasos y de ahí **empeora**. Entrenar más tiempo no ayuda; lo estropea. Eso llevó a fijar el entrenamiento en **30,000 pasos**.

**Una precisión que hay que hacer, porque antes aquí decía otra cosa.** Las dos corridas **no son independientes**: usan la misma semilla, los mismos datos y la misma tasa de aprendizaje, así que son **la misma trayectoria recorrida dos veces**, una más larga que la otra. Que sus curvas coincidan **no prueba** que el resultado sea reproducible con otra semilla; eso no se ha probado. Lo que sí prueba, y de forma más limpia, es que **el termómetro roto no deformaba la curva promediada**: dos instrumentos distintos midiendo el mismo modelo dan lo mismo.

### Frente 2: tres hallazgos que no estaban previstos

**a) La representación de la imagen tiene un suelo, y recorta parte del artefacto.** El metal produce rayas claras y también **zonas muy oscuras** donde casi no pasa radiación. En las tomografías reales esas zonas bajan hasta −7,159 unidades. La representación que usa el sintetizador **no puede bajar de −1,000**: todo lo que esté por debajo queda aplanado. Medido sobre los 23,058 parches, en el paciente típico afecta al **1 %** de la zona, pero **19 de 77 pacientes pasan del 10 %** y uno llega al **44.9 %**. No es un error de programación: el recorte está donde la decisión de diseño lo puso. Lo que faltaba era saber cuánto cuesta, y ahora se sabe.

**b) El criterio para elegir el mejor modelo puede estar midiendo lo que no importa.** Al comparar los dos modelos guardados sobre la misma serie, con los mismos cortes y la misma semilla, el que la medición de validación llama "mejor" genera **la mitad del metal** que el otro y duplica el salto de valores en el borde de la zona editada. Si la cifra con que se elige el modelo no ordena bien, entonces la cifra de 30,000 pasos se eligió con el instrumento equivocado. **Hay un experimento corriendo ahora mismo para saber si eso pasa en un paciente o en los cinco.**

**c) El conjunto de validación no es lo que el diseño decía.** El diseño dice "5 pacientes con metal". El archivo que el entrenamiento realmente consume dice **3**, los tres con implante real. Los otros dos tienen un objeto metálico incidental y el criterio de inclusión los dejó fuera, pero aparecieron igual en tres de mis mediciones porque las escribí leyendo el disco y no ese archivo. Importa porque sobre esos pacientes se va a calibrar el margen con que se declara si el método funciona, y la base es **más estrecha** de lo que el diseño sugiere: tres pacientes, no cinco.

### Frente 3: se cerró el Objetivo 2 y arrancó el brazo de comparación

- **La revisión de los 16 casos del recorte: hecha.** 14 correctos, 2 con error de segmentación y **ninguno** por culpa del recorte. La decisión del recorte de 6 mm se mantiene.
- **El cribado ciego de fracturas: hecho.** Un médico revisó 30 casos sin saber los grupos. **20 de 30 (67 %) tienen fractura confirmada**, y están repartidas por igual: 10 y 10. La fractura **no** explica los corredores estrechos. Eso obligó a reescribir un párrafo de la tesis que afirmaba lo contrario.
- **El tipo de tornillo: decidido.** La trayectoria cruza las dos articulaciones sacroilíacas, así que es un **tornillo transilíaco-transsacro**, y no un iliosacro.
- **El rasterizador del tornillo: escrito.** Era el eslabón que faltaba para que la cadena completa se pueda ejecutar: convierte una posición en una máscara de vóxeles. Antes, el programa calificaba posiciones sin construir nunca la máscara.
- **El brazo de comparación física: corriendo en esta computadora.** Ver la sección siguiente.

### Frente 4: la redacción del documento de entrega

Los capítulos 1, 2 y 3 y parte de la introducción están redactados y el documento compila en **114 páginas**. Y se hizo una auditoría que valía la pena: se revisaron **las 36 decisiones ya cerradas** para comprobar si de verdad habían llegado al documento. **No todas habían llegado**, y dos contenían cifras equivocadas. Nueve hallazgos graves, que se están corrigiendo.

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

### Objetivo 3: crear la apariencia del metal — entrenado dos veces, con muestras, pero la cadena completa sigue sin ejecutarse

Esto es lo que más cambió. Hace dos semanas no había ninguna imagen; hoy hay dos entrenamientos completos y varias muestras que se pueden abrir.

**Lo que ya se ejecutó:**

| | Detalle |
|---|---|
| Ejemplos de entrenamiento | **23,058 parches** preparados, uno por implante y corte |
| Primer entrenamiento | 144,500 pasos, 8 h de GPU. Encontró **sobreajuste** y dos defectos del código |
| Segundo entrenamiento | 60,000 pasos, 6 h 20. **Confirmó** el sobreajuste con la medición corregida |
| Muestras | Un corte suelto, y después **66 cortes consecutivos** de un paciente, con páginas web navegables y volúmenes para visor médico |
| Mediciones nuevas | El suelo de la representación, el salto en el borde de la zona editada y la comparación entre los dos modelos guardados |

**Cuánto cuesta entrenar, ya medido de verdad:** **0.377 segundos por paso** en la partición de GPU que usa el clúster, o sea unas **3 h 10 para los 30,000 pasos** decididos. El piloto de 200 pasos de septiembre proyectaba 0.77 h porque corría en una GPU entera; la cifra real es la de arriba.

**Lo que todavía falta, y es lo importante:**

- **la cadena completa nunca se ha ejecutado.** Hoy el modelo *reconstruye* el metal en pacientes que **ya lo tenían**. Nunca se ha hecho el recorrido entero: pelvis limpia → posición propuesta → máscara del tornillo → apariencia generada. El rasterizador que faltaba ya está escrito, así que esto es ahora el siguiente paso y no un hueco;
- definir el banco final de geometrías de tornillo;
- las métricas de apariencia implementadas (su **definición** ya está decidida, ver abajo); y
- la comparación contra copia y pegado y contra el protocolo físico.

**Un aviso que conviene tener presente al mirar las muestras.** Están hechas con pacientes que ya tenían implante. Cuando se le pida generar sobre una pelvis **limpia**, el modelo estará trabajando en una situación que no vio al entrenar, porque aprendió la apariencia en imágenes que **ya** tenían rayas. El resultado puede ser malo, y saberlo ahora es mejor que descubrirlo en la sustentación.

### Objetivo 4: métricas — SAP existe, y la métrica de apariencia ya está definida por escrito

SAP ya tiene código, controles y resultados.

**Y lo que estaba abierto desde el principio se cerró el 5 de octubre:** cómo se mide la "amplitud de las rayas" cuando el objetivo es **crear** el artefacto y no quitarlo. Las métricas se tomaron de un protocolo publicado que fue diseñado para lo contrario, así que había que decidir cómo se invierten. Lo decidido, en lenguaje simple:

- **La referencia es la tomografía limpia del mismo paciente.** Eso solo existe en los 14 pacientes de prueba **sin** metal, y ahí es donde se mide. En los pacientes que sí tienen implante no hay referencia limpia, así que ahí **no se mide amplitud**, se mide **discrepancia** contra la imagen real. Esa confusión estaba en el diseño y se corrigió.
- **Las zonas donde se mide se calculan solas a partir de la posición del tornillo**, en vez de dibujarse a mano como hace el protocolo original. Es más reproducible y permite que los dos métodos comparados se midan exactamente igual.
- **Se reporta además cuánta señal quedó aplanada contra el suelo de la representación.** Así el límite conocido del método se publica con un número al lado del resultado, en lugar de quedar como una advertencia en prosa.
- **El contraste contra "copia y pegado" se declara control de cordura y no evidencia de calidad**, porque ese método no produce rayas por construcción y cualquier cosa le gana. El contraste que de verdad decide es el de equivalencia contra la simulación física.

Lo que sigue pendiente es la **implementación**, y decidir cómo se invierten las otras dos métricas de apariencia.

## Lo esperado de aquí en adelante: Peters y el clúster

Son los dos frentes que deciden si el Objetivo 3 llega a tener un resultado.

### El brazo de comparación física (protocolo de Peters et al.)

**Qué es.** La tesis necesita comparar su sintetizador contra algo mejor que "pegar un tornillo". Ese algo es un simulador de física de tomografía, con un protocolo ya publicado que lo usa. La comparación es: ¿se parece lo que genera el modelo a lo que produce la física simulada?

**Qué se logró el 5 de octubre.** El simulador **corre en esta computadora**. Se instaló, se ejecutó su ejemplo completo —simulación más reconstrucción— y produjo su imagen. Cuesta unos **70 segundos por corte**.

**Y se verificó algo que su artículo no dice.** Al meter un objeto metálico en una tomografía de paciente, hay dos formas de hacerlo: proyectar paciente y metal **juntos**, como un solo objeto físico, o proyectarlos por separado y combinar después. La primera es la correcta y la segunda es un atajo. El artículo no lo declara, y la tesis prometía por escrito revisarlo en el código antes de reproducirlo. **Revisado: se proyectan juntos.** El metal se inserta restando agua y añadiendo la aleación en el mismo sitio, antes de proyectar.

**Dos avisos honestos:**

1. **Su script publicado no corre tal como viene.** Falla al escribir su propia configuración. Reproducirlo exige un parche de una línea, aplicado en una copia local y nunca en el clon original, para que quede claro qué se ejecutó y en qué se diferencia de lo publicado.
2. **Lo hecho NO es validar el simulador, y no se va a llamar así.** Validar significa comparar contra mediciones físicas en un maniquí real escaneado en un tomógrafo real, y no hay maniquí, ni tomógrafo, ni mediciones. Además, el propio artículo del simulador no contiene ningún estudio de artefacto metálico y describe su validación como preliminar. Reclamar una validación que sus autores no hicieron sería indefendible. Lo que se hizo se llama **verificación de reproducción**, y eso sí es defendible.

**Qué se espera ahora.** Reproducir su protocolo con **el tornillo y la anatomía de esta tesis**, usando la misma receta verificada: la máscara del tornillo como mapa de material, restando agua y añadiendo la aleación. Es trabajo de ingeniería, no de investigación, y el riesgo principal es el tiempo: a 70 segundos por corte, un volumen entero no es gratis.

**Y una advertencia de alcance.** El protocolo original es **bidimensional, de una sola fila de detector**. El tornillo de esta tesis mide unos 138 mm a lo largo de su eje. Extenderlo a eso es una adaptación explícita que **no hereda** la validación del protocolo original, y así debe escribirse.

### El entrenamiento en el clúster (Khipu)

**Dónde está.** Las dos corridas ya se hicieron. La segunda terminó el 5 de octubre a mediodía, en una partición de GPU compartida, sin tocar el límite de tiempo.

**Lo que ya no es un problema.** El tiempo de cómputo. Los 30,000 pasos decididos son unas **3 h 10**, y la cola del clúster —que en septiembre parecía el cuello de botella— dejó de serlo: la última corrida arrancó **21 horas antes** de lo previsto.

**Lo que sí es un problema, y es más interesante.** El modelo **no mejora con más cómputo**. Las dos corridas muestran que la calidad toca su mejor punto cerca de los 30,000 pasos y de ahí empeora. Si el resultado final no alcanza, **la palanca no es entrenar más tiempo: son más pacientes**. Hoy el entrenamiento usa 47. Esa es una limitación real del trabajo y todavía no está escrita en la tesis.

**Lo que falta decidir antes de la corrida final**, y depende de un experimento que está corriendo:

1. **Si el criterio con que se elige el mejor modelo es válido.** Hoy se elige por una cifra de validación, y hay indicios de que esa cifra no ordena bien los modelos por calidad de imagen. Si se confirma, hay que cambiar el criterio **antes** de congelar el diseño.
2. **Si la saturación con 47 pacientes entra como limitación declarada.** Su evidencia es la misma cifra del punto anterior, así que las dos decisiones se resuelven juntas.

**Qué falta en el clúster, en orden:** medir el margen con que se declarará si el método funciona —sobre los pacientes de validación, nunca sobre los de prueba—, congelar el diseño por escrito, y recién entonces lanzar la corrida final y la evaluación.

## 4. Lo que sí se puede afirmar hoy

- La base local fue auditada y los duplicados se manejaron por paciente para evitar mezclar a la misma persona entre entrenamiento y prueba.
- TotalSegmentator se ejecutó y sus máscaras se sometieron a controles de calidad.
- El error del autoencoder se midió y la ruta latente no cumplió la regla fijada.
- El muestreador y SAP existen, corren y produjeron resultados reproducibles.
- Se generaron miles de posiciones y, desde el 4 de octubre, **también imágenes**: un corte suelto y luego una serie de 66 cortes consecutivos, con sus controles de preservación pasando exactos.
- El renderizador **se entrenó dos veces, con la misma semilla**: la calidad toca su mejor punto cerca de los 30,000 pasos y después empeora. **No** se ha comprobado qué pasa con otra semilla.
- El tiempo de cómputo **no es el problema**. Los 30,000 pasos son unas 3 h 10. El problema es ejecutar y evaluar la cadena completa, y decidir con qué criterio se elige el mejor modelo.
- El simulador de física **corre en local** y se verificó en su código que inserta el metal proyectándolo junto al paciente. Eso cierra un pendiente que la propia tesis tenía escrito.
- La definición de la métrica de apariencia **está decidida y escrita antes de ver los resultados**, con sus parámetros fijados sobre los pacientes de validación.
- El cribado de fracturas está hecho: **20 de 30 pelvis (67 %) tienen fractura confirmada**, repartidas por igual entre los dos grupos, así que la fractura **no** explica los corredores estrechos.
- Los capítulos 1, 2 y 3 y parte de la introducción están redactados y el documento compila en **114 páginas**, con decisiones todavía marcadas como pendientes.

## 5. Lo que todavía no se debe afirmar

- No se debe decir que el sistema completo ya sintetiza tomografías con metal. **Hay imágenes, pero son reconstrucciones sobre pacientes que ya tenían implante.** La cadena completa, desde una pelvis limpia, nunca se ejecutó.
- No se debe decir que las 3,600 posiciones fueron aprobadas por un médico.
- No se debe decir que SAP demuestra seguridad clínica.
- No se debe decir que las pelvis usadas estaban libres de fractura. **Ya está medido: 20 de 30 tienen fractura.** La selección comprobó ausencia de osteosíntesis, no de fractura.
- No se debe decir que el corredor estrecho siempre es una variación anatómica normal.
- No se debe decir que el modelo mejora la segmentación ósea; esa evaluación está fuera del alcance actual.
- **No se debe decir que un modelo es mejor que otro.** La comparación entre los dos modelos guardados dio un resultado contraintuitivo y está en verificación; con un paciente no alcanza.
- **No se debe decir que se validó el simulador de física.** Se reprodujo su protocolo y se verificó su código. Validar exigiría un maniquí y un tomógrafo real, que no hay.
- **No se debe decir que el renderizador puede generar todo el artefacto.** La representación tiene un suelo que aplana las zonas más oscuras, y eso está medido.

## 6. Las revisiones que condicionaban el Objetivo 2: las cuatro, resueltas

> **Cambio importante respecto de la version anterior de este documento.** Las cuatro entradas de esta
> seccion estaban abiertas el 3 de octubre y **las cuatro se resolvieron**. Se conservan con su
> historia porque explican de donde salen las cifras que hoy se citan, y porque dos de ellas obligaron
> a corregir frases que ya estaban escritas en la tesis.

### Revisión de 16 casos por diferencias entre dos recortes

Todas las cifras principales del Objetivo 2 usan las máscaras obtenidas con un recorte de 6 mm. Hay 16 casos en los que el resultado difiere de manera importante frente al recorte de 3 mm o aparece una estructura desplazada.

**RESUELTO.** La revisión se completó: **16 de 16 casos revisados, 14 correctos, 2 con error de segmentación y ninguno por culpa del recorte.** La decisión del recorte de 6 mm se mantiene, y la condición que podía reabrirla quedó evaluada. La revisión la hizo la autora con apoyo de un médico recién egresado y sin especialidad. Quedan anotados los dos casos con error de segmentación, sin decidir qué se hace con ellos.

Archivos:

- [`e9ts_revision_laminas.md`](../experiments/objetivo2/e9ts_revision_laminas.md)
- [`e9ts_revision_laminas_autora.csv`](../experiments/objetivo2/e9ts_revision_laminas_autora.csv)

### Cribado ciego de fracturas en 30 casos

Se confirmó una fractura en `CLINIC_0060`. Ese caso está entre los corredores estrechos. Si las fracturas fueran más frecuentes en ese grupo, parte del estrechamiento atribuido a anatomía normal podría deberse a patología.

Por eso se preparó una revisión ciega de:

- los 15 casos con corredor menor de 7 mm; y
- 15 controles escogidos entre los corredores que sí admiten 7 mm.

**RESUELTO.** El cribado se hizo a ciegas. Resultado: **20 de 30 (67 %) con fractura confirmada, más un caso dudoso que se reporta aparte**, y repartidas **por igual**: 10 de 15 en los corredores estrechos y 10 de 15 en los controles. **La fractura no explica el estrechamiento.**

Hay un matiz que sí es sugerente y no concluyente: la fractura **sacra desplazada** aparece en 7 de 15 estrechos frente a 2 de 15 controles, con p = 0.109. Eso obliga a matizar una frase de la tesis que atribuía el estrechamiento a la anatomía normal, pero no autoriza a concluir lo contrario.

Un límite que hay que declarar con la cifra: lo revisó un **médico recién egresado y sin especialidad**, sobre láminas fijas. Es un cribado válido, **no** una lectura de especialista.

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

**RESUELTO.** La medición se corrió sobre los 152 casos y **ningún caso de la cohorte cambia**: la diferencia mediana del diámetro del corredor es de 0.000 mm. Ninguna cifra publicada depende del relleno, así que se corrige el texto y **no** se repite la medición. Las cifras actuales corresponden a la envolvente **sin relleno de cavidades**, y eso ahora está respaldado con evidencia y no solo supuesto.

### Nombre y tipo exacto del tornillo

La trayectoria implementada va desde la cortical externa de un ilion hasta la cortical externa del otro. Es decir, cruza ambas articulaciones sacroilíacas.

**RESUELTO.** Los documentos usaban de manera inconsistente "iliosacro", "transsacro" y "transiliosacro". La decisión: es un **tornillo transilíaco-transsacro**, y las tolerancias angulares de la fuente que las publica **sí** le aplican, porque se midieron sobre ese mismo corredor. La serie clínica con la que se compara se conserva como **referencia de distribución**, no como prueba de que su implante fuera el mismo.

Con una regla que hay que respetar al corregir el documento: donde el texto describe **lo que hicieron otros autores**, sigue diciendo "iliosacro", porque cambiarlo sería atribuirles algo que no dijeron.

## 7. Aclaración sobre “el último experimento de ver la posición de los tornillos”

Hoy hay tres tareas distintas que podrían confundirse:

| Tarea | Qué se mira | Quién la hace | Estado |
|---|---|---|---|
| E13 / SAP | Las 3,600 posiciones y cuánto salen del hueso | El programa | Ejecutada |
| Revisión de 16 casos | Si las máscaras y el corredor cambian por el recorte | Autora con apoyo médico | **Hecha**: 14 correctos, 2 errores de segmentación, 0 por el recorte |
| Cribado de 30 casos | Si hay fractura y dónde | Médico recién egresado, sin especialidad | **Hecho**: 20 de 30 con fractura, repartidas por igual |

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

## 9. El experimento medico que estaba preparado: YA SE HIZO

> **Esta seccion es historica.** El cribado de fracturas se ejecuto y su resultado esta en la seccion 6:
> 20 de 30 con fractura confirmada, repartidas por igual entre los dos grupos. Se conserva el mensaje
> de abajo porque sirve de plantilla si hay que pedir una segunda lectura, esta vez de especialista.

El único paquete médico listo hoy no pregunta por la calidad de las posiciones. Pregunta si existe **fractura** en 30 casos ciegos. Para esa tarea el mensaje correcto sería:

> Hola, Dr./Dra. [apellido]. En mi tesis medí automáticamente el espacio disponible para un tornillo en tomografías pélvicas. Encontré algunos corredores muy estrechos, pero la base fue seleccionada por no tener material de osteosíntesis, no por estar libre de fractura. Necesito una revisión ciega de 30 casos anonimizados para registrar si se observa fractura (`sí`, `no` o `dudoso`), dónde se encuentra y si las imágenes permiten juzgarla. Los casos están mezclados y no le diría cuáles tienen corredor estrecho para no influir en su lectura. ¿Podría ayudarme con esta revisión o recomendarme un radiólogo o traumatólogo que pueda hacerla?

Las instrucciones exactas ya están en [`r3_fractura_revisor.md`](../experiments/objetivo2/r3_fractura_revisor.md). No debe entregarse al revisor el archivo `r3_fractura_grupos.csv`, porque revelaría los grupos y rompería el cegamiento.

## 10. Próximos pasos, en orden práctico

Los cuatro primeros puntos de la versión anterior de esta lista **ya están hechos**: el tipo de tornillo está decidido, la envolvente quedó medida sobre los 152 casos, la revisión de los 16 casos se completó y el cribado de fracturas se hizo. Lo que queda, en orden:

1. **Esperar el experimento que está corriendo**: la comparación de los dos modelos guardados sobre los cinco pacientes de validación. De él dependen tres decisiones a la vez: con qué criterio se elige el mejor modelo, si los 30,000 pasos se eligieron bien, y si la saturación con 47 pacientes entra como limitación declarada. **Es el cuello de botella actual, y es barato.**
2. **Ejecutar la cadena completa por primera vez**, sobre un paciente de validación **sin** metal: posición propuesta, máscara del tornillo, apariencia generada. Todas las piezas existen; nunca se encadenaron.
3. **Medir el margen con que se declarará si el método funciona**, usando solo pacientes de validación. Tiene una parte bloqueada: necesita el brazo de física funcionando sobre esta anatomía.
4. **Reproducir el protocolo de física con el tornillo de esta tesis**, con la receta ya verificada en su código.
5. **Congelar el diseño del Objetivo 3 por escrito** y recién entonces lanzar la corrida final y la evaluación.
6. **Decidir las dos cosas del conjunto de validación**: si los dos pacientes con objeto incidental cuentan, y cuántos pacientes tendrá el subconjunto del brazo físico, porque de eso depende el número real de la prueba estadística principal.
7. **Resolver las decisiones de redacción marcadas** en los capítulos y alinear título, pregunta, objetivos y alcance.
8. **Corregir dos cifras equivocadas** que la auditoría encontró dentro de decisiones ya cerradas.

## 11. Lectura honesta del progreso

El proyecto tiene un resultado defendible del Objetivo 1, aunque negativo, y un resultado cuantitativo grande del Objetivo 2 **que en estas dos semanas quedó cerrado**: los tres controles que lo condicionaban —la revisión de los 16 casos, el cribado de fracturas y la envolvente— están resueltos con evidencia.

El Objetivo 3 dejó de ser un hueco. Tiene dos entrenamientos, muestras que se pueden mirar y una métrica definida por escrito antes de ver resultados. Pero sigue sin ejecutar su caso de uso: **colocar un tornillo en una pelvis limpia**.

Y hay algo que conviene decir con claridad, porque es el patrón de estas dos semanas: **los tres hallazgos más importantes del tramo son problemas, no logros.** El entrenamiento se degrada si se prolonga. La representación no puede expresar parte del artefacto. El criterio con que se elige el mejor modelo puede estar midiendo lo que no importa. Los tres se encontraron midiendo, no suponiendo, y los tres están registrados con su evidencia.

Eso **no** es mala señal. Un trabajo que mide su propio techo y lo publica es más defendible que uno que no lo buscó. Lo que sería mala señal es que aparecieran en la sustentación.

La forma más precisa de decirlo hoy es:

> La representación latente fue puesta a prueba y no pasó. El muestreador de posiciones está implementado, ejecutado y **cerrado**, con sus controles humanos resueltos. El sintetizador de apariencia ya entrena, ya genera imágenes y ya tiene su métrica definida, pero **todavía no ha ejecutado la cadena completa ni evaluado nada**, y antes de hacerlo hay que resolver con qué criterio se elige el modelo.

## 12. Archivos clave para retomar

- Estado general: [`ESTADO.md`](ESTADO.md)
- Hallazgos y riesgos: [`04-implicancias.md`](04-implicancias.md)
- Mapa de experimentos del Objetivo 2: [`EXPERIMENTOS.md`](../experiments/objetivo2/EXPERIMENTOS.md)
- Resultado principal de SAP: [`e13_sap.md`](../experiments/objetivo2/e13_sap.md)
- Análisis por corredor viable/estrecho: [`e13b_estratificado.md`](../experiments/objetivo2/e13b_estratificado.md)
- Revisión de los 16 casos: [`e9ts_revision_laminas.md`](../experiments/objetivo2/e9ts_revision_laminas.md)
- Cribado de fracturas: [`r3_fractura_revisor.md`](../experiments/objetivo2/r3_fractura_revisor.md)
- Documento de entrega: [`overleaf/`](../overleaf/)
- Decisiones tomadas, con su fundamento: [`01-decisiones.md`](01-decisiones.md)
- Diseño del sintetizador: [`diseno_A.md`](../experiments/objetivo3/diseno_A.md)
- Muestras sintéticas que se pueden abrir: `experiments/objetivo3/outputs/a8/` y `a8_mejor/` (páginas web navegables y volúmenes para visor médico)
- El suelo de la representación, medido: `experiments/objetivo3/a9_suelo_representacion.py`
- Rasterizador del tornillo, el eslabón que faltaba: `experiments/objetivo3/a11_rasterizar_tornillo.py`
- Parámetros de las zonas de medición: `experiments/objetivo3/a12_roi_parametros.py`
- Brazo de física, copia ejecutable y parcheada: `experiments/objetivo3/peters/`
- Auditoría de las decisiones ya cerradas: `redaccion/rondas/paridad-r01-trazabilidad.md`
