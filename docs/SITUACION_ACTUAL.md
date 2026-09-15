# Situación actual de MetalSynth-Pelvis

> Corte del estado: 14 de septiembre de 2026. Este documento resume lo que se puede comprobar en el repositorio a esa fecha. Está escrito como una explicación de trabajo, no como una sección formal de la tesis. Cuando una cifra fue exploratoria, quedó descartada o todavía necesita revisión, se dice de forma explícita.

## Resumen rápido

La tesis busca generar implantes de osteosíntesis y sus artefactos metálicos en tomografías de pelvis. La propuesta tiene dos partes grandes:

1. colocar un tornillo sintético en una posición anatómica y quirúrgicamente razonable; y
2. generar la apariencia del metal y de sus artefactos mediante un modelo de difusión.

Hasta ahora, el avance fuerte está en la preparación de los datos y en la primera parte: ya se auditó la cohorte local, se resolvieron duplicados por paciente, se estudió cómo representar los HU altos, se probó la localización anatómica de S1, se corrió TotalSegmentator sobre toda la colección y ya existe una primera medición del corredor transsacro.

Lo que todavía no existe es el sistema generativo final. No se ha entrenado el VAE, el LDM 2.5D ni ControlNet; tampoco se han generado CT sintéticas finales ni se han comparado contra copy-paste y el protocolo físico. En otras palabras: hay bastante método y evidencia preparatoria, pero aún no hay un modelo de síntesis terminado.

El alcance mínimo defendible se concentra en:

- validar la representación multi-ventana con el VAE;
- terminar el muestreador de colocación restringida; y
- evaluar las colocaciones con SAP.

El renderizador por difusión y la evaluación completa de apariencia siguen siendo el alcance completo, si el tiempo alcanza.

## 1. ¿Qué problema intenta resolver la tesis?

Los implantes metálicos producen valores HU muy altos y artefactos que salen fuera de la máscara del metal: rayas, bandas oscuras y pérdida de señal alrededor del implante. Por eso, un método de inpainting pensado para tumores no se puede copiar directamente. Un tumor es tejido deformable y normalmente se sintetiza dentro de una máscara; un implante es rígido y altera también el espacio que lo rodea.

La propuesta actual combina cuatro ideas:

- una representación de CT con varias ventanas HU;
- tornillos rígidos y paramétricos, en vez de formas extraídas directamente de CT con metal;
- un muestreador que coloque esos tornillos dentro de corredores óseos medidos en cada pelvis; y
- un LDM 2.5D condicionado con ControlNet y una banda extendida alrededor del implante, llamada `B_delta`, para permitir artefactos fuera de la máscara metálica.

La pregunta de fondo ya no es simplemente “¿se puede insertar metal sintético?”. Eso ya tiene antecedentes. La pregunta es si se puede insertar de manera escalable, respetando la anatomía, imitando distribuciones clínicas de colocación y generando una apariencia local más coherente que un copy-paste simple.

La formulación formal vigente está en [`tesis/main.tex`](../tesis/main.tex) y el alcance mínimo/completo está separado en [`docs/00-tesis.md`](00-tesis.md).

## Guía conceptual: R1, QC, máscaras, E9 y Dmax

Esta sección explica cómo se conectan las piezas principales del trabajo. La cadena completa es:

`CT -> R1 ubica la anatomía -> TS crea máscaras anatómicas -> QC decide si el caso es utilizable -> E9 busca corredores -> Dmax indica qué tornillo cabe -> el Objetivo 2 muestrea una pose`.

### ¿Qué es el Objetivo 1?

El **Objetivo 1** trata de la representación de intensidades, no de la colocación del tornillo.

Una CT guarda valores en HU. El hueso, el tejido blando y el metal ocupan rangos muy distintos. Si todo se mete en una sola ventana, se pierde detalle; si se usan solamente las tres ventanas publicadas LW, MW y SW, los valores altos del metal quedan recortados.

Por eso, el Objetivo 1 pregunta algo muy concreto: **¿podemos convertir una CT a una representación multi-ventana, comprimirla con un VAE y reconstruirla sin destruir los HU importantes?**

El recorrido que debe validarse es:

`HU originales -> canales multi-ventana -> VAE -> canales reconstruidos -> HU reconstruidos`.

La métrica principal es MAE en HU dentro del hueso, con un criterio de trabajo menor de 25 HU. E6a y E6c solo probaron la codificación y decodificación matemática, sin VAE. Esas pruebas mostraron que una cuarta ventana para metal (`pub+MTW`) evita el clipping, pero el Objetivo 1 todavía no está cerrado porque falta comprobar el recorrido completo a través de un VAE real.

Este objetivo es importante para el renderizador: si la representación elimina la información del metal antes de entrenar, ningún modelo de difusión podrá recuperarla de manera confiable después.

### ¿Qué es el Objetivo 2?

El **Objetivo 2** trata de la geometría y la colocación, no de generar rayas o apariencia metálica.

Su trabajo es recibir una pelvis y proponer la pose 3D de un tornillo paramétrico:

- en qué nivel sacro se coloca;
- dónde está su centro o punto de paso;
- con qué orientación;
- qué longitud puede tener;
- qué diámetro cabe; y
- qué grado de brecha cortical tendrá.

La pose no debe elegirse en los ejes arbitrarios del archivo ni optimizar siempre una trayectoria “perfecta”. Debe expresarse en un marco anatómico propio de cada paciente, caber en el corredor óseo y, para S1, producir una distribución de grados que pueda compararse con las distribuciones clínicas de cirugía navegada y convencional.

El resultado final del Objetivo 2 será un **muestreador de poses**. E9 y `Dmax` son insumos geométricos de ese muestreador; no son todavía el muestreador completo.

### ¿Qué es R1 y para qué sirven los landmarks de Kaiser?

R1 es el experimento que intenta localizar los puntos anatómicos necesarios para construir el marco de referencia descrito por Kaiser. Los tres tipos de landmark son:

- el platillo superior de S1;
- las dos crestas ilíacas; y
- las dos espinas ilíacas posterosuperiores o EIPS.

Aunque se habla de tres tipos, en el archivo aparecen cinco puntos: S1, cresta derecha, cresta izquierda, EIPS derecha y EIPS izquierda.

Estos puntos son importantes por cuatro razones:

1. **S1 indica el nivel y la altura de trabajo.** Sirve para centrar el recorte donde E9 buscará el corredor. Si R1 se equivoca y marca L5 como S1, toda la búsqueda se desplaza aproximadamente un nivel vertebral y puede medir tejido blando o una región anatómica equivocada.
2. **Las crestas ilíacas definen una referencia coronal.** La línea que une ambas crestas permite expresar la inclinación coronal del tornillo respecto de la pelvis del paciente.
3. **Las EIPS definen una referencia axial.** La línea que une ambas EIPS permite expresar la inclinación axial respecto de la pelvis. En la implementación de E9 también ayudan a exigir que la trayectoria llegue suficientemente lejos hacia cada ilion y no termine por error en un foramen del sacro.
4. **Permiten comparar pacientes.** Una persona puede entrar al escáner rotada o inclinada. Si se usaran solo los ejes `x`, `y`, `z` del archivo, el mismo ángulo significaría cosas distintas entre estudios. Los landmarks convierten esas coordenadas del escáner en una referencia anatómica.

R1 no es un detector clínicamente validado. Es una heurística que busca esos puntos y genera láminas para revisarlos. Su pregunta experimental fue: **¿estos landmarks siguen siendo localizables cuando hay metal y artefacto cerca?** Si no lo fueran, el marco de Kaiser no se podría usar en la población de interés.

El hallazgo actual es que, entre 65 pacientes con material ortopédico, el marco completo fue computable con S1 correctamente localizado en 48; además, en 29 los cinco landmarks estaban libres de contaminación según el criterio usado. Esto muestra que el marco es utilizable en una parte importante de la cohorte, pero no automáticamente en todos los casos.

### ¿Qué significa QC?

`QC` significa **Quality Control**, o control de calidad.

No es una red, una máscara ni una métrica clínica. Es el conjunto de comprobaciones que decide si una salida es suficientemente confiable para entrar a un análisis. En este proyecto incluye, por ejemplo:

- verificar que S1 esté en el nivel correcto;
- comprobar que la máscara no esté vacía;
- detectar si S1 o las crestas están cortadas por el campo de visión;
- confirmar que la máscara y la CT tengan la misma rejilla y affine;
- revisar si el metal real queda mayormente dentro de las máscaras óseas;
- comparar los recortes de 3 y 6 mm;
- buscar componentes sueltos o cajas desplazadas; y
- inspeccionar láminas de casos problemáticos.

El QC no demuestra que TotalSegmentator sea perfecto. Su función es detectar fallos conocidos, excluir o revisar los casos dudosos y dejar trazabilidad de por qué cada paciente entra o sale del resultado.

### ¿Qué son las máscaras anatómicas?

Una máscara anatómica es un volumen 3D binario alineado con la CT:

- `1` significa que el vóxel pertenece a una estructura;
- `0` significa que no pertenece a ella.

TotalSegmentator 2.18.0 produjo cuatro máscaras por caso:

- `sacrum.nii.gz`;
- `vertebrae_S1.nii.gz`;
- `hip_left.nii.gz`; y
- `hip_right.nii.gz`.

Cada caso tiene esas cuatro máscaras para dos modos: `default6mm` y `robust3mm`. E9 forma una unión de sacro, S1 y ambas caderas para representar el volumen óseo continuo por el que tendría que pasar una trayectoria transsacra. También aplica un cierre morfológico de 2 mm para que el espacio normal de la articulación sacroilíaca no parta artificialmente el trayecto.

Estas máscaras **no se obtienen diciendo que todo vóxel mayor de 150 HU es hueso**. Son etiquetas anatómicas producidas por una red de segmentación. Esa diferencia importa porque el hueso esponjoso puede tener HU bajos: un umbral simple deja solamente una especie de cáscara cortical incompleta, mientras una máscara anatómica intenta representar toda la estructura.

Las máscaras completas no están guardadas en Git ni fueron copiadas a esta PC. Están en Khipu, con esta estructura:

`~/metalsynth/data/ts_total/<caso>/<modo>/<estructura>.nii.gz`.

Por ejemplo:

`~/metalsynth/data/ts_total/dataset6_CLINIC_0001_data/robust3mm/sacrum.nii.gz`.

Lo que sí está en la PC son los resultados derivados del QC —CSV, resúmenes y láminas— dentro de:

[`experiments/objetivo2/outputs/ts_total_qc/`](../experiments/objetivo2/outputs/ts_total_qc/).

La carpeta `outputs/` está ignorada por Git. Por eso estos derivados existen localmente, pero no forman parte de los archivos versionados del repositorio.

### ¿Qué significa que TS coincidió con el revisor clínico en 57 de 57 casos comparables?

R1 había colocado un punto que supuestamente correspondía al platillo superior de S1. El revisor clínico miró los casos con metal y clasificó ese punto, entre otras categorías, como:

- `ok`: el punto de R1 sí está en S1;
- `+1`: R1 quedó un nivel arriba, normalmente en L5;
- `otro`, `?` o `no hallado`: no hay una decisión binaria suficientemente clara para esta comparación.

Después se usó la máscara `vertebrae_S1` de TotalSegmentator como un **segundo indicador independiente**. Se midió la diferencia vertical entre el techo de esa máscara y el punto S1 de R1.

En los casos `ok`, la diferencia quedó en un rango pequeño y positivo. En los casos `+1`, el punto de R1 quedó aproximadamente 24–34 mm por encima de la S1 segmentada, una separación compatible con haberse ido a la vértebra superior. Los dos grupos quedaron completamente separados.

Había 57 casos que cumplían las condiciones exactas de comparación:

- 51 clasificados `ok` por el revisor;
- 6 clasificados `+1`; y
- techo de `vertebrae_S1` medible en los dos recortes.

TS clasificó los 51 `ok` como concordantes y detectó los 6 `+1` como “R1 arriba de TS”. De ahí sale **57/57**.

No entraron en ese denominador cuatro casos `no hallado`, dos `otro`, uno `?` y un caso `+1` donde no se pudo medir el techo de S1. Por eso 57/57 no significa “TS acertó en los 65 pacientes” ni “TotalSegmentator está validado clínicamente”. Significa solamente que, dentro del subconjunto con una etiqueta clínica binaria clara y una máscara medible, la señal de nivel de TS separó todos los `ok` de los `+1`.

### ¿Por qué esa comparación cambió las cifras de R1?

Las cifras antiguas de R1 contaban como válido cualquier marco donde la heurística hubiera encontrado los cinco puntos. El problema es que “encontrar un punto limpio” no prueba que ese punto sea realmente S1. Un punto colocado sobre L5 puede estar perfectamente lejos del metal y aun así ser anatómicamente incorrecto.

La revisión clínica mostró esos errores de nivel. Además, la comparación con TS hizo visible una inconsistencia de transcripción: `metal_0012` debía ser `+1`, no `ok`, y `metal_0015` era dudoso. Al corregir esas etiquetas y exigir que S1 fuera correcto:

- el marco computable bajó de 49 a 48 pacientes; y
- el marco computable y sin contaminación bajó de 30 a 29.

Es más preciso decir que **TS ayudó a detectar y comprobar el problema, y la corrección de la referencia clínica cambió las cifras de R1**. TS no reemplazó al revisor ni convirtió sus máscaras en ground truth.

### ¿Qué es el corredor de E9?

El corredor es el túnel óseo 3D por el que podría atravesar un tornillo recto sin salir del hueso. En E9 se busca principalmente un corredor **transsacro**: empieza en la cortical externa de un ilion, atraviesa el sacro y termina en la cortical externa del ilion opuesto.

No es una estructura que venga anotada directamente en la CT. Se calcula probando muchos centros y direcciones dentro de las máscaras anatómicas. La versión actual:

- busca centros alrededor del nivel de S1 indicado por R1;
- prueba una rejilla de posiciones cada 3 mm;
- prueba 81 orientaciones, combinando ángulos axiales y coronales entre -20 y +20 grados;
- exige que el trayecto permanezca en la unión ósea;
- comprueba que salga realmente por ambos iliones y no por un agujero del sacro; y
- mide cuánto espacio queda desde el eje hasta el punto no óseo más cercano.

El E9 original intentó construir el hueso usando `HU > 150`. Dio corredores demasiado pequeños incluso en pacientes con tornillos transsacros reales y fue declarado no válido. E9-TS conserva la búsqueda geométrica, pero reemplaza esa definición defectuosa de hueso por las máscaras anatómicas de TotalSegmentator.

### ¿Qué es Dmax?

`Dmax`, guardado como `D_TS_max_mm`, es el **diámetro del cilindro recto más grande que cabe completamente dentro del corredor transsacro encontrado**.

Para una trayectoria candidata, el algoritmo calcula la distancia desde cada punto del eje hasta el vóxel no óseo más cercano. La menor de esas distancias es el radio limitante: basta un estrechamiento en cualquier parte para limitar todo el tornillo. El diámetro es:

`D = 2 x distancia mínima del eje al exterior del hueso`.

Se ignoran 8 mm en cada extremo para que la salida normal por la cortical del ilion no reduzca artificialmente el diámetro. Luego se escoge el mayor `D` entre todas las posiciones y orientaciones probadas: ese es `Dmax`.

`Dmax` no es el diámetro del sacro ni el diámetro del tornillo real. Es una estimación de la capacidad geométrica del mejor túnel recto encontrado en esa pelvis.

Después se pregunta si cabe una geometría concreta:

`Dmax >= diámetro del tornillo + 2 x holgura radial`.

Por ejemplo, un tornillo de 6.5 mm con 1 mm libre por cada lado necesita al menos 8.5 mm. Un tornillo de 8 mm con 2 mm por lado necesita 12 mm. Esto explica por qué la tesis reporta varias combinaciones y no solamente el corte de 10 mm.

### ¿Por qué se quieren eliminar las islas pequeñas de las máscaras?

Una “isla” es un grupo pequeño de vóxeles marcado como una estructura anatómica, pero desconectado del cuerpo principal de esa estructura. Puede aparecer por un error de segmentación, ruido, artefacto metálico o diferencias del recorte de TotalSegmentator.

Estas islas son peligrosas porque E9 interpreta cada vóxel positivo como hueso real. Una isla situada lejos puede:

- agrandar o desplazar la caja envolvente de una estructura;
- crear centros candidatos donde no debería haber hueso;
- alterar la distancia al exterior o una salida del trayecto; y
- hacer que los recortes de 3 y 6 mm parezcan anatómicamente más distintos de lo que son.

Se observaron diez casos con cajas desplazadas entre 14 y 98 mm por componentes remotos. Por eso se propuso limpiar componentes muy pequeños.

No se toma simplemente “el componente más grande”, porque una pelvis fracturada puede tener dos fragmentos grandes y ambos ser anatomía real. La regla elegida elimina solamente componentes con menos del 0.1% (`F = 0.001`) del volumen total de su estructura.

En la cohorte principal del Objetivo 2, esta limpieza no cambió `Dmax` ni la viabilidad para ninguna de las fracciones probadas hasta 5%. Eso es una buena señal: el resultado central no depende de las islas observadas. Sin embargo, E10b sigue pendiente para confirmar directamente que `F = 0.001` corrige las diez cajas desplazadas.

### ¿Por qué se mide el diámetro máximo sobre máscaras anatómicas?

Porque la pregunta quirúrgica es volumétrica: **¿qué cilindro puede cruzar el hueso real sin invadir el exterior, un foramen o el canal?** Para responderla se necesita distinguir el interior completo del hueso del espacio no óseo.

Un umbral HU no sirve bien para eso en el sacro. El hueso cortical suele ser denso, pero el esponjoso puede estar por debajo de 150 HU. Con `HU > 150`, el algoritmo ve una cáscara delgada o agujereada y calcula corredores de 1–3 mm donde clínicamente ya existe un tornillo de aproximadamente 7 mm. El problema no era la búsqueda de E9, sino la representación incompleta del hueso.

Las máscaras anatómicas intentan recuperar el volumen entero de sacro, S1 y los iliones, incluso donde los HU son bajos. Sobre esa representación sí tiene sentido aplicar una distancia euclídea al borde y preguntar qué cilindro cabe.

Además, medirlo en cada máscara individual evita asumir que todas las pelvis tienen el mismo corredor. La literatura muestra variación anatómica importante; por eso `Dmax` se mide paciente por paciente y luego condiciona el diámetro, la holgura, la orientación y la longitud que podrá usar el muestreador.

## 2. ¿Cuál es el alcance actual?

### Alcance mínimo viable

Es lo mínimo que se considera defendible incluso si no se llega a terminar todo el renderizador:

1. **Objetivo 1: representación multi-ventana.** El viaje completo `HU -> ventanas -> VAE -> HU` debe conservar el tejido óseo con MAE menor de 25 HU.
2. **Objetivo 2: muestreador quirúrgicamente restringido.** Debe proponer poses de tornillos dentro de la geometría disponible de cada pelvis, usando el marco anatómico de Kaiser y el corredor medido sobre máscaras óseas.
3. **Evaluación de colocación con SAP.** Las poses de S1 deben acercarse a dos distribuciones clínicas ordinales: cirugía navegada y convencional. S2 se mantiene como análisis geométrico y descriptivo, porque no se encontró una distribución clínica ordinal equivalente para ese nivel.

### Alcance completo

Si el tiempo y el cómputo alcanzan, se agrega:

3. **Objetivo 3: renderizador.** LDM 2.5D + ControlNet + `B_delta` para sintetizar el implante y el artefacto.
4. **Objetivo 4: evaluación de apariencia.** Comparación contra copy-paste y contra el protocolo físico adoptado de Peters/XCIST-CatSim, usando SAP y las métricas publicadas de apariencia.
5. **Ablaciones.** Quitar restricciones, multi-ventana o `B_delta` para comprobar si cada componente realmente aporta.

### Lo que está explícitamente fuera

- No se evaluará si los datos sintéticos mejoran una red downstream de segmentación.
- Por lo tanto, Dice y HD95 de una red de segmentación no son resultados finales de esta tesis.
- No se hará una reimplementación independiente y supuestamente validada de XCIST. Se adopta el protocolo de Peters como comparación física, documentando su adaptación y sus límites.
- No se estratificará por fenotipo de dismorfismo sacro ni se usará el score `>70` de Kaiser.
- No se presentará 10 mm como un estándar clínico demostrado. Es una convención geométrica conservadora.
- No se reclamarán como propias las métricas BFC e ISC. Ambas propuestas fueron retiradas.
- No se hará un banco de geometrías extrayendo tornillos reales de CTPelvic1K, salvo que en el futuro sea necesaria una contingencia muy específica.

La exclusión del downstream no es solo por tiempo. En la parte local de CTPelvic1K no hay suficiente anotación ósea verificada alrededor del metal para sostener una evaluación supervisada sólida.

## 3. ¿Qué datos se están usando realmente?

Aquí hubo una corrección importante de alcance: **no se tiene CTPelvic1K completo en disco**.

La colección publicada declara 1184 volúmenes, pero localmente hay 178:

- `dataset6`: 103 volúmenes, identificados por coincidencia de conteo y geometría como CLINIC;
- `dataset7`: 75 volúmenes, identificados de la misma forma como CLINIC-metal.

Esta correspondencia es una inferencia razonable, pero no está escrita dentro de los headers NIfTI. Los otros cinco subconjuntos de la colección, que suman 1006 volúmenes, no están disponibles localmente.

Después de revisar duplicados exactos, cortes compartidos y adquisiciones repetidas, la unidad de independencia dejó de ser el volumen y pasó a ser el paciente:

- 178 volúmenes originales;
- 168 pacientes;
- 11 volúmenes fuera de uso estadístico, sin borrar ningún archivo;
- una unión sin pérdida de `metal_0059` y `metal_0071`;
- 65 pacientes en el grupo 1, con material ortopédico;
- 37 pacientes en el grupo 2, sin osteosíntesis pero con otros objetos o situaciones no limpias;
- 66 pacientes en el grupo 3, limpio.

La partición actual por objetivo es:

- **Objetivo 1:** grupos 1, 2 y 3;
- **Objetivo 2:** grupos 2 y 3; el grupo 1 se usa solo como contraste separado;
- **Objetivo 3:** grupo 3 como anatomía limpia para síntesis;
- **apariencia real:** grupo 1, sin usarlo como fuente de geometría paramétrica.

### ¿Entonces se usa o no la parte metálica de CTPelvic1K?

**Sí se usa, pero no para todo.** Esta es una de las decisiones centrales del proyecto.

La parte con metal se usa para:

- observar artefactos reales;
- caracterizar qué implantes aparecen en la colección;
- hacer una comparación descriptiva de poses y corredores;
- medir cómo cambia el corredor si el metal existente se considera espacio ocupado;
- estudiar si los landmarks anatómicos sobreviven al artefacto; y
- tener un par test-retest (`metal_0065`/`0066`).

No se usa para construir el banco de formas de tornillo. Al segmentar metal con un umbral fijo de 2500 HU, los tornillos salen fragmentados y demasiado delgados. Por eso se decidió usar tornillos paramétricos lisos, con diámetro de 6.5 a 8.0 mm tomado de la literatura, y limitar su longitud según el corredor medido en cada paciente.

Tampoco se usa CLINIC-metal como si tuviera ground truth completo. El paper de CTPelvic1K reporta anotación solo para 14 de 75 casos de ese subconjunto y en el equipo local no se encontraron máscaras óseas vinculadas y verificadas.

La auditoría de datos completa está en [`docs/02-datos.md`](02-datos.md) y la revisión por volumen en [`experiments/exploration-3d/revision.csv`](../experiments/exploration-3d/revision.csv).

## 4. Decisiones importantes que ya se tomaron

### Datos y partición

- La estadística se hace por paciente, no por volumen.
- Un mismo paciente nunca puede aparecer a ambos lados de un split.
- Los duplicados no se borran: se registran, se elige un representante o se reservan para reproducibilidad.
- El nombre CLINIC o CLINIC-metal no basta para decidir si un caso está limpio o contiene la osteosíntesis de interés. Se necesita revisión.

### Metal e implantes

- `2500 HU` sirve solo para **cribado**, porque fue sensible en esta cohorte.
- `2500 HU` no sirve como definición universal de la forma real del implante.
- Para metal integrity se usará el umbral adaptativo por ROI de Peters.
- Para considerar un implante existente como espacio ocupado, la política principal actual es el semimáximo local por objeto; 2500 HU se reporta como una cota que tiende a adelgazar el metal.
- Los implantes sintéticos serán cilindros paramétricos lisos. Rosca, cabeza, canulación y arandela quedan simplificadas y declaradas como limitación.

### Anatomía y corredor

- Se adoptó TotalSegmentator 2.18.0 como herramienta para producir máscaras anatómicas, **no como ground truth**.
- Se usan `sacrum`, `vertebrae_S1`, `hip_left` y `hip_right`.
- Las máscaras se controlan caso por caso; se excluyen discordancias de nivel, S1 vacía y S1 cortada por el FOV según el criterio vigente.
- La limpieza quita componentes menores a `F = 0.001` del volumen de cada estructura, con conectividad 26. La elección fue post hoc y se debe decir así.
- No se conserva solo el componente mayor, porque una fractura real podría separar una estructura en más de un componente legítimo.
- La viabilidad se expresa como `Dmax >= d_implante + 2c`, donde `d_implante` está entre 6.5 y 8.0 mm y `c` es una holgura radial de 1 a 2 mm por lado.
- El corte de 10 mm es una convención de holgura, no una frontera clínica validada.

### Recorte de TotalSegmentator: todavía hay una decisión en transición

La decisión escrita y el texto actual de la tesis dejan el recorte por defecto de 6 mm como principal y el robusto de 3 mm como sensibilidad. Sin embargo, la preferencia más reciente de la autora es invertirlos y usar 3 mm como principal.

Los resultados no permiten decir que ambos sean intercambiables: en 124 casos con QC, la diferencia mediana de `Dmax` es 0 mm, pero el percentil 90 de la diferencia absoluta es 1.3 mm, el máximo es 4.5 mm y la clasificación de viabilidad a 10 mm cambia en 12 casos, es decir, 10%. Por eso hace falta cerrar formalmente esta decisión y mantener el otro recorte como sensibilidad.

### Evaluación

- SAP queda como la única métrica propuesta por la tesis.
- BFC e ISC se retiraron para no renombrar como contribución propia medidas que ya existían.
- Las métricas de apariencia conservarán los nombres publicados por Peters: bone integrity, metal integrity y streak amplitude.
- La escala 0–4 del reto AAPM no se traslada, porque está calibrada alrededor de NMAR y no tiene un equivalente directo en síntesis.
- RMSE y SSIM se usarán fuera de `B_delta`, donde la imagen no debería cambiar. Dentro de la banda, una diferencia respecto del CT limpio es justamente lo esperado.

El registro completo y cronológico está en [`docs/01-decisiones.md`](01-decisiones.md).

## 5. Experimentos realizados hasta la fecha

Los experimentos se pueden entender como una serie de preguntas. Cada prueba intentó responder una duda antes de construir encima de ella. Algunas dieron un resultado útil y otras mostraron que el camino usado era incorrecto. Estas últimas no fueron tiempo perdido: evitaron que la tesis se apoyara en una medición engañosa.

### Primero: revisar qué había realmente en la “caja” de datos

**Inventario y exploración 3D.** Antes de usar los datos había que abrir la caja y contar su contenido. Es parecido a recibir muchas carpetas de fotografías: no se puede asumir que cada archivo es una persona diferente ni que el nombre de la carpeta describe perfectamente lo que aparece en ella.

Se encontraron 178 tomografías locales, todas legibles, pertenecientes solamente a dataset6 y dataset7. Esto aclaró desde el inicio que no se tenía CTPelvic1K completo.

**Revisión visual del metal.** El nombre CLINIC-metal sugería que esos casos tenían metal, pero no decía qué tipo de metal ni si era el que interesa para la tesis. Del mismo modo, CLINIC parecía limpio, pero no se podía confiar únicamente en el nombre.

La revisión fue como separar a mano objetos de una caja que venía mal etiquetada. En dataset7 se encontraron 71 volúmenes con material ortopédico, correspondientes a 65 pacientes. En dataset6 también aparecieron objetos metálicos, principalmente objetos externos o DIU. La conclusión fue sencilla: **las carpetas ayudan a orientarse, pero no sirven por sí solas para formar las cohortes**.

**Duplicados y pacientes repetidos.** Luego se buscó si una misma persona aparecía más de una vez. La analogía sería tener dos fotos diferentes del mismo alumno y contarlas como si fueran dos alumnos distintos. Eso inflaría el tamaño de la muestra y podría poner a la misma persona en entrenamiento y evaluación.

Después de revisar archivos idénticos, cortes compartidos y adquisiciones repetidas, los 178 volúmenes quedaron agrupados en 168 pacientes. Desde entonces, la regla es contar y separar por paciente.

### E1: usar un “detector de humo” para encontrar posible metal

E1 probó varios valores HU —1500, 2500 y 3500— para decidir cuáles tomografías merecían una revisión más detallada.

Un umbral HU funciona aquí como un detector de humo: avisa que puede haber algo muy denso, pero no dice exactamente qué objeto es ni dibuja bien su forma. Puede activarse por un tornillo, un DIU, un accesorio externo o incluso otro objeto muy brillante.

Con 2500 HU se marcaron 113 candidatos y no se perdió ningún caso que después fue identificado como material en la revisión. Por eso 2500 HU se conserva como una buena **alarma de cribado**. No se usa como segmentación definitiva del tornillo.

### E6a y E6c: comprobar si la “cámara” puede ver hueso y metal a la vez

Una CT tiene un rango de intensidades enorme. Una analogía útil es fotografiar una habitación oscura que también tiene una lámpara muy brillante. Si se ajusta la exposición para ver la habitación, la lámpara queda completamente blanca; si se ajusta para la lámpara, se pierde el resto.

Las ventanas HU son como varias exposiciones de la misma escena. Cada una conserva mejor un rango diferente.

**E6a** probó las tres ventanas publicadas: LW, MW y SW. El problema fue que la ventana más amplia terminaba en 2000 HU. Todo lo que estaba por encima quedaba “quemado”, como una zona blanca sin detalle. Incluso usando un decodificador ideal que escogía la mejor ventana para cada vóxel, 50 de 178 volúmenes fallaron el criterio de MAE menor de 25 HU. En el metal, el error llegó a miles de HU.

La conclusión de E6a fue que **las tres ventanas originales no alcanzan para sintetizar metal**.

**E6c** probó techos más altos y añadió una cuarta ventana especial para metal. Es como agregar una fotografía con una exposición hecha específicamente para la lámpara. La configuración `pub+MTW` no tuvo fallos en hueso antes del VAE y conservó mucho mejor el metal: su MAE mediana fue 0.07 HU a 16 bits, 1.10 HU a 12 bits y 17.72 HU a 8 bits.

Esta es la mejor representación explorada hasta ahora. Sin embargo, todavía falta pasarla por el VAE. Hasta que eso ocurra, es como haber comprobado que las fotografías de entrada son buenas, pero no que sobreviven a la compresión y descompresión del sistema completo.

### R1: colocar señales de tránsito antes de buscar una ruta

R1 buscó S1, las crestas ilíacas y las EIPS. Estos landmarks funcionan como señales de tránsito o puntos de un GPS: le dicen al algoritmo dónde está dentro de la pelvis y cómo está orientado el paciente.

Sin estas señales, E9 podría buscar el corredor en la vértebra equivocada o describir un ángulo respecto del escáner en vez de respecto del cuerpo. Sería como decir “avanza hacia la derecha” sin saber hacia dónde está mirando el mapa.

En los 65 pacientes con material ortopédico, R1 logró construir el marco completo con S1 clínicamente confirmado en 48. En 29, además, las cinco regiones estaban libres de contaminación según el criterio usado. El acuerdo entre la revisión automática asistida y el revisor fue kappa 0.81.

El resultado no dice que R1 sea perfecto. Dice que el sistema de referencia se puede usar en una parte importante de los casos, siempre que exista QC.

### E8: intentar copiar la forma real de los tornillos

E8 preguntó si convenía recortar los tornillos que ya aparecen en CLINIC-metal y reutilizar esas formas.

La prueba se parece a intentar reconstruir un objeto mirando solamente su sombra más brillante. Si se exige que todo esté por encima de 2500 HU, algunas partes del tornillo desaparecen y la forma queda cortada.

Se encontraron candidatos a tornillo iliosacro o transsacro en al menos 17 de 65 pacientes. Sin embargo, 9 de 57 objetos alargados aparecieron fragmentados y el diámetro mediano extraído quedó cerca de 5 mm, por debajo de los calibres publicados de 6.5–8.0 mm.

Por eso se decidió no copiar esas formas defectuosas. El tornillo sintético será un cilindro paramétrico con dimensiones tomadas de la literatura. Los tornillos reales siguen siendo útiles como referencia visual y como contraste.

### E9 inicial: intentar medir un túnel usando un mapa incompleto

E9 busca el corredor, es decir, el túnel de hueso por donde podría pasar un tornillo. La primera versión decía que todo vóxel mayor de 150 HU era hueso.

El problema es parecido a dibujar un túnel mirando solamente sus paredes más blancas. El hueso cortical sí suele verse muy brillante, pero el hueso esponjoso del interior puede tener valores bajos. El mapa terminaba mostrando una cáscara fina y con agujeros, no el volumen óseo completo.

Como resultado, E9 calculó corredores de solo 1–3 mm en lugares donde ya había tornillos reales cercanos a 7 mm. Esa contradicción mostró que la entrada era incorrecta. **El E9 original se declaró no válido y sus cifras no se usan.**

### E9b: poner pequeñas “sondas” para entender el error

E9b colocó pequeñas esferas en el cuerpo y las alas de S1 para medir sus HU. Es como introducir termómetros en tres puntos concretos para saber si una regla general representa bien todo el lugar.

Al principio parecía que entre 35% y 43% de los casos tenían alguna esfera por debajo de 150 HU. Eso apoyaba la idea de que el hueso esponjoso podía quedar fuera del umbral.

Después se descubrió que varias esferas estaban un nivel arriba o fuera de la anatomía correcta. Por eso esas proporciones se retiraron como evidencia. La prueba sí dejó una lección útil: **antes de interpretar la densidad, había que confirmar primero el nivel anatómico y que la sonda estuviera realmente dentro del sacro**.

### Piloto de TotalSegmentator: probar la herramienta en dos casos antes de usarla en todos

Antes de correr TotalSegmentator sobre toda la colección se hizo un piloto. Es como probar una máquina nueva con dos piezas antes de enviarle toda la producción.

Se probaron los recortes de 3 y 6 mm. Ambos funcionaron, pero sus máscaras no fueron idénticas: el Dice entre ellas quedó entre 0.93 y 0.97 y hubo diferencias especialmente en las alas y en la dirección superior-inferior.

El piloto permitió comprobar la instalación, descubrir qué controles hacían falta y preparar una corrida completa que pudiera reanudarse si algo fallaba.

### TotalSegmentator en toda la cohorte: colorear automáticamente cada hueso

TotalSegmentator puede imaginarse como un sistema que toma la CT y colorea cada estructura en una lámina transparente distinta: una para el sacro, una para S1 y una para cada cadera. Esas láminas son las máscaras anatómicas.

Se procesaron 179 casos con dos recortes por caso. En total fueron 358 corridas, todas completadas sin error, en aproximadamente 6 horas y 27 minutos.

Este paso no midió todavía el corredor. Produjo los “mapas de hueso” que E9 necesitaba para medirlo correctamente.

### Comparación de TS con el revisor: comprobar que el mapa señala el piso correcto

R1 podía encontrar un punto limpio pero equivocarse de vértebra, igual que un GPS puede encontrar una calle real pero ubicarla una cuadra más arriba.

Se comparó el punto de S1 de R1 con el techo de la máscara `vertebrae_S1` de TotalSegmentator y con la clasificación del revisor clínico. En los 57 casos que tenían una decisión clínica clara (`ok` o un nivel arriba) y una máscara medible, TS separó correctamente los 51 `ok` de los 6 casos `+1`.

Esta comparación ayudó a detectar errores de nivel y una transcripción incorrecta. Al corregirla, el número de marcos válidos de R1 pasó de 49 a 48 y el de marcos válidos y sin contaminación pasó de 30 a 29.

Esto no significa que TS sea un juez perfecto. Es una segunda regla que coincidió con el revisor en ese subconjunto y que sirve para evitar medir el corredor en el nivel equivocado.

### E10: barrer las migas sin botar una pieza real

Las máscaras de TotalSegmentator a veces contienen pequeños grupos de vóxeles separados del hueso principal. Se parecen a migas que quedaron lejos de una pieza grande. Algunas son errores, pero una fractura verdadera también puede separar el hueso en dos piezas importantes.

E10 midió esas piezas para elegir una limpieza prudente. Se probaron cuatro opciones: no limpiar y borrar componentes menores al 0.1%, 1% o 5% de cada estructura.

En los 72 pacientes de la cohorte principal, ninguna opción cambió `Dmax` ni la decisión de si el tornillo cabía. Se eligió 0.1% (`F = 0.001`) porque es la limpieza menos agresiva de las probadas. No se usa la regla “quedarse solo con la pieza más grande”, ya que podría borrar una parte real de una pelvis fracturada.

### E9-TS: buscar la pajilla más gruesa que atraviesa el túnel

E9-TS repitió la búsqueda del corredor, pero esta vez sobre las máscaras anatómicas rellenas. La analogía es probar muchas pajillas rectas, con distintas posiciones e inclinaciones, dentro de un túnel. La pajilla no puede atravesar las paredes ni salir por un agujero equivocado.

El algoritmo prueba muchos centros y 81 orientaciones. Para cada ruta calcula el cilindro más ancho que cabe; luego se queda con el mayor. Ese diámetro es `Dmax`.

Se procesaron 152 casos sin errores. Después del QC, el resultado principal quedó en 72 de los 103 pacientes sin osteosíntesis. Con el recorte de 6 mm, la mediana de `Dmax` fue 9.5 mm y 29 de 72 pacientes superaron la convención de 10 mm. Con 3 mm, la mediana fue 9.4 mm y 27 de 72 superaron 10 mm.

Este es el resultado geométrico principal disponible hasta ahora. Todavía no equivale a tener el muestreador terminado: indica cuánto espacio hay, pero falta usarlo para generar la distribución completa de posiciones y grados de brecha.

### Repetición de E9-TS: volver a medir con la misma regla

La corrida se repitió para comprobar que el cálculo no cambiara por azar o por diferencias de ejecución. Es parecido a usar dos veces la misma regla sobre el mismo objeto.

Las 2352 filas y sus 43 columnas fueron idénticas. Esto demuestra reproducibilidad computacional: el programa repite el mismo cálculo. No demuestra por sí solo que el corredor sea clínicamente correcto; esa es una pregunta diferente.

### E10b: comprobar que la escoba realmente quitó las migas

Antes de la limpieza se habían visto diez casos donde una pequeña isla desplazaba mucho la caja que rodeaba la máscara, entre 14 y 98 mm. E10b fue preparado para comparar esas cajas antes y después de aplicar `F = 0.001`.

El script pasó una prueba local de 8 de 8 casos, pero la salida completa todavía no está en el repositorio. Por eso este control sigue pendiente. Su propósito no es volver a elegir `F`, sino verificar directamente que la limpieza elegida hace lo que se esperaba.

## 6. Resultado actual del corredor

El cálculo E9-TS procesó 152 casos en los que se había localizado S1. Para el resultado principal se usan solo los grupos 2 y 3, es decir, pelvis sin osteosíntesis, y después se aplica el QC de nivel. El embudo es:

`103 pacientes sin osteosíntesis -> 91 con S1 localizada -> 72 con QC aceptado`.

La pérdida no es balanceada: salen 11 de 34 casos del grupo 2 y 7 de 57 del grupo 3 por discordancia de nivel, más un caso por borde del FOV. Esto puede sesgar la comparación entre grupos y debe aparecer como limitación.

Con `F = 0.001`:

| Resultado en los 72 pacientes | Recorte 6 mm | Recorte 3 mm |
|---|---:|---:|
| `Dmax` p25 | 7.4 mm | 7.8 mm |
| `Dmax` mediana | 9.5 mm | 9.4 mm |
| `Dmax` p75 | 11.7 mm | 11.7 mm |
| Cumple convención de 10 mm | 29/72 (40.3%) | 27/72 (37.5%) |
| Viable para 6.5 mm + 1 mm por lado | 65.3% | 62.5% |
| Viable para 7.3 mm + 1 mm por lado | 54.2% | 51.4% |
| Viable para 8.0 mm + 2 mm por lado | 23.6% | 20.8% |

La lectura más importante no es que “el corredor mide 10 mm”, sino que la viabilidad cambia con el diámetro del implante, la holgura elegida y el recorte del segmentador. Por eso la fórmula `Dmax >= d_implante + 2c` es más informativa que un único corte universal.

También se midió la densidad a lo largo del mejor eje, ya dentro de las máscaras anatómicas. En la cohorte sin osteosíntesis, la mediana de la fracción de vóxeles con HU menor o igual a 150 fue aproximadamente 0.42. Esto confirma que definir “hueso” solo como `HU > 150` excluiría una parte importante del corredor sacro.

En 52 pacientes con metal y QC, si TotalSegmentator trata el implante como hueso, 53.8% parece cumplir 10 mm con el recorte de 6 mm. Al marcar el metal como ocupado mediante semimáximo local, la viabilidad baja a 40.4%. Este grupo se reporta como contraste y no se mezcla con la cohorte principal sin osteosíntesis.

Los resultados automáticos completos están en [`experiments/objetivo2/outputs/e9ts_3mm/e9ts_resumen.md`](../experiments/objetivo2/outputs/e9ts_3mm/e9ts_resumen.md).

## 7. Métricas: cuáles son y de dónde vienen

Conviene separar las métricas finales de tesis de los controles internos del pipeline.

### Métricas finales

| Métrica | Para qué sirve | Origen real |
|---|---|---|
| MAE en HU | Decide si la representación multi-ventana + VAE conserva intensidades óseas. | MAE es una métrica estándar. El corte **25 HU es una decisión de diseño de esta tesis**; en el repositorio no aparece una fuente que lo valide clínicamente. Debe presentarse como criterio fijado a priori o conseguir una justificación bibliográfica. |
| SAP | Evalúa si las poses sintéticas son quirúrgicamente admisibles y si su distribución parece clínica. | Es la **única métrica propia**. Usa los grados de brecha de Smith, las dos distribuciones de Zwingmann y distancia Wasserstein-1 para comparar distribuciones. |
| Cortical Breach Grade | Clasifica la salida del tornillo respecto de la cortical en cuatro grados: 0, <2 mm, 2–4 mm y >4 mm. | Escala tomada de `smith2006iliosacral`; las frecuencias clínicas objetivo vienen de `zwingmann2009navigated`. |
| Viabilidad del corredor | Comprueba si cabe un tornillo con holgura. | El procedimiento de `Dmax` viene de `mclaren2021corridor`; el marco anatómico y la holgura dimensional vienen de `kaiser2014dysmorphism`. La fórmula explícita `Dmax >= d_implante + 2c` es una operacionalización propia. |
| Fracción de zona por densidad | Describe cuánto del eje o volumen candidato cae en rangos de densidad definidos. | Componente propio de SAP, motivado por el uso de mapas de densidad en `arand2019pelvicring`. Todavía debe quedar completamente cerrado en la implementación final. |
| Bone integrity | Comprueba cuánto hueso se pierde o inventa después de sintetizar, excluyendo el implante. | Protocolo de `peters2025hybrid`: máscara por encima de 150 HU, cambio de volumen y Sorensen-Dice. En sacro se debe explicar que 150 HU no representa todo el esponjoso. |
| Metal integrity | Comprueba si el metal generado conserva la geometría CAD esperada. | `peters2025hybrid`: comparación de máscaras con umbral adaptativo igual al máximo HU del tejido adyacente en el ROI más 250 HU. No es un umbral absoluto de 250 HU. |
| Streak amplitude | Compara la amplitud de las rayas sintéticas con la distribución observada en CT reales con metal. | `peters2025hybrid`: diferencia entre los promedios de los extremos superior e inferior del 5% de desviación HU en ROIs perpendiculares al streak. Aquí se adapta de remoción a síntesis. |
| RMSE y SSIM fuera de `B_delta` | Verifican que el modelo no modifique regiones donde no debe hacerlo. | Métricas estándar, también usadas en el protocolo Peters/AAPM. La restricción al exterior de `B_delta` es una adaptación de esta tesis. |

### Controles internos, no resultados clínicos finales

- Dice entre máscaras de los recortes 3 y 6 mm: mide sensibilidad del segmentador.
- Cohen kappa entre agente y revisor: mide acuerdo en la localización de S1.
- Fracción del eje fuera de máscara y fracción de metal dentro de máscara: QC de TotalSegmentator.
- Conteo de componentes, cambio de caja y vóxeles eliminados: QC de limpieza.
- SHA256 y coincidencia de cortes: integridad y duplicados.

Que aparezca Dice en estos controles no contradice que Dice/HD95 downstream estén fuera de alcance. Son preguntas distintas.

### Dos umbrales que todavía necesitan cuidado

1. **MAE < 25 HU:** no se encontró una fuente clínica o física en la bibliografía actual. Se puede conservar como criterio ingenieril fijado antes del experimento, pero no se debe presentar como estándar publicado.
2. **`B_delta` de aproximadamente 12 mm:** tampoco se encontró un paper que publique ese tamaño. La idea de extender la región está bien motivada por el artefacto fuera de la máscara, pero el valor debe seleccionarse mediante un protocolo explícito —por ejemplo, análisis de perfiles en datos de entrenamiento y ablación— sin ajustarlo con el test final.

## 8. Papers principales que ya sostienen la tesis

Estos trabajos ya están en el repositorio y tienen una función concreta:

| Paper | Por qué se necesita |
|---|---|
| `liu2021ctpelvic1k` | Define la colección de datos, sus subconjuntos y la limitación de anotaciones de CLINIC-metal. |
| `wang2025adaptiveweighting` | Da las tres ventanas HU publicadas y el umbral de 2500 HU usado sobre CLINIC-metal. También deja claro que multi-ventana viene de MAR, no de síntesis. |
| `peters2025hybrid` | Es la fuente principal del protocolo físico, la simulación con XCIST/CatSim y las métricas bone integrity, metal integrity y streak amplitude. |
| `haneda2025aapm` | Muestra la aplicación del protocolo en el reto AAPM y ayuda a delimitar qué partes del benchmark sí y no se pueden trasladar. |
| `kaiser2014dysmorphism` | Proporciona el marco de referencia anatómico computable en CT, los landmarks, calibres y la justificación dimensional de la holgura. |
| `mclaren2021corridor` | Proporciona el procedimiento reproducible para medir `Dmax` y discutir la convención de 10 mm. |
| `gardner2010safezones` | Justifica tratar S1 y S2 por separado y aporta geometría y calibres. |
| `zwingmann2009navigated` | Da las dos distribuciones clínicas de cuatro grados que SAP intentará reproducir en S1. |
| `smith2006iliosacral` | Define los umbrales de los cuatro grados de brecha cortical. |
| `vandenbosch2002` | Justifica conservar S1/S2 como variable, pero también demuestra por qué no se debe inventar un prior ordinal para S2. |
| `wasserthal2023` | Es la cita del software TotalSegmentator, con la limitación de que el paper corresponde a una versión anterior. |
| `isensee2021` | Es la base nnU-Net de TotalSegmentator. |
| `chen2024tumorsynthesis` | Muestra el paradigma de síntesis de lesiones limitado al interior de una máscara y ayuda a justificar `B_delta`. |
| `rombach2022latentdiffusion` y `zhang2023controlnet` | Son las bases arquitectónicas del LDM y ControlNet que todavía falta implementar. |
| `xie2024implantsegmentation` | Ayuda a explicar por qué un umbral fijo puede distorsionar la forma del metal, aunque su evidencia no es específica de tornillos pélvicos reales. |

## 9. Papers o fuentes que todavía hacen falta

### Prioridad alta: conseguir o corregir

1. **Texto completo de `zhang2026pediclescrew`.** Actualmente solo hay abstract. Es importante porque podría solaparse con el reclamo de novedad del muestreador y porque usa otra escala de brecha. Sin el texto completo no conviene citar sus cifras ni afirmar con seguridad en qué se diferencia.
2. **Versión publicada correcta de `isensee2021`.** El archivo local identificado como `isensee2021.pdf` es el preprint arXiv de 2020, mientras que la referencia bibliográfica apunta al artículo de Nature Methods de 2021. Hace falta el PDF correcto o declarar que se consultó el preprint.
3. **Fuente versionada de TotalSegmentator 2.18.0.** El paper de Wasserthal describe la versión 1 y un modelo de 104 estructuras; no valida la clase `vertebrae_S1`, la versión 2.18.0 ni el comportamiento con metal. Se necesita citar documentación/model card/release del software para las clases y parámetros, mientras la validez bajo metal debe seguir sustentándose con el QC propio.
4. **Fuente citable para defender 3 mm como recorte principal**, si esa será la decisión final. El README dice que el recorte robusto es “better”, pero el paper no compara 3 contra 6 mm para S1. Si no aparece una fuente específica, la elección debe justificarse únicamente con la sensibilidad local y mantener 6 mm como análisis secundario.

### Prioridad alta: lectura personal antes de sustentar

5. **Releer directamente `zwingmann2009navigated` y `smith2006iliosacral`.** Ya existen fichas detalladas, pero la autora todavía registra esta lectura como deuda. SAP depende por completo de que los grados, denominadores y distribuciones se expliquen sin mezclar pacientes, tornillos, S1/S2 ni técnicas quirúrgicas.
6. **Revisar directamente `peters2025hybrid` junto con el código/documento oficial de scoring AAPM.** Es necesario antes de implementar las métricas para no convertir `+250 HU` en umbral absoluto, no trasladar por error la escala 0–4 y respetar los ROIs del protocolo.

### Prioridad media: cerrar la novedad y la reproducibilidad

7. **Paper original de multiple-window learning de Niu y Wang, SPIE 2021.** `wang2025adaptiveweighting` es una fuente secundaria para el origen de multi-ventana. Hace falta si la tesis quiere describir con precisión quién introdujo el enfoque; no hace falta para usar las tres ventanas concretas de Wang 2025.
8. **Fuente clásica de SSIM y definición/implementación exacta usada por el benchmark.** Conviene incluirla si se quiere reportar SSIM comparable y no solo citar a Peters de manera indirecta.
9. **Fuente metodológica para Wasserstein-1**, si la universidad exige citar la definición matemática de cada métrica. Hoy está elegida como distancia de distribuciones, pero el repositorio no muestra una referencia matemática específica para ella.
10. **Estudio de validación de segmentación de S1 bajo implantes metálicos, si existe.** El paper actual de TotalSegmentator no lo cubre. Si una búsqueda dirigida no encuentra uno, eso no bloquea la tesis: se presenta como vacío de evidencia y se mantiene el QC local y la revisión clínica como soporte.

### Vacíos que probablemente se cierran mejor con experimentos, no con papers

- El valor exacto de 25 HU para el Go/No-Go.
- El ancho de `B_delta`, hoy cercano a 12 mm.
- La fracción `F = 0.001` para limpiar componentes.
- Elegir 3 o 6 mm como recorte principal.
- La adaptación de las métricas de MAR a síntesis.

Buscar antecedentes es útil, pero estas cifras son decisiones del método local. Lo correcto es fijar cómo se eligieron, evitar usar el test para ajustarlas, hacer sensibilidad y declararlas como propias o post hoc cuando corresponda.

## 10. Qué falta hacer, en orden práctico

### Para cerrar el mínimo viable

1. Correr E10b completo y confirmar que `F = 0.001` elimina los desplazamientos de caja sin borrar componentes anatómicos importantes.
2. Cerrar la decisión 3 mm vs 6 mm y alinear [`docs/01-decisiones.md`](01-decisiones.md), [`docs/00-tesis.md`](00-tesis.md) y [`tesis/main.tex`](../tesis/main.tex).
3. Ejecutar E6b: entrenar o probar el VAE con la representación candidata de cuatro canales. E6a/E6c solo dan una cota inferior sin VAE, así que el Objetivo 1 todavía no ha pasado el Go/No-Go real.
4. Terminar el muestreador de poses, no solo la medición de `Dmax`: punto de entrada, orientación, longitud, nivel y muestreo de grados de brecha.
5. Implementar SAP completo y comprobar la comparación Wasserstein-1 contra las dos distribuciones de Zwingmann en S1.
6. Completar la revisión clínica prevista para los casos dudosos y documentar el sesgo del embudo 103 -> 91 -> 72.

### Para cerrar el alcance completo

7. Implementar el VAE/LDM 2.5D y ControlNet. Hoy `src/` sigue vacío y el código está concentrado en experimentos.
8. Definir `B_delta` sin contaminar el test final y hacer su ablación.
9. Implementar el baseline copy-paste.
10. Adaptar y ejecutar el brazo físico Peters/XCIST-CatSim con la misma anatomía y las mismas poses.
11. Generar las salidas sintéticas y medir SAP, bone integrity, metal integrity, streak amplitude, RMSE y SSIM.
12. Hacer las ablaciones y, si se mantiene en el protocolo, una evaluación visual ciega por lectores.

## 11. Lectura honesta del progreso

El proyecto no está “recién empezando”. Ya se hizo el trabajo incómodo que suele causar problemas más adelante: inventario real, procedencia, duplicados, unidad por paciente, definición de cohortes, límites del dataset, auditoría del metal, validación del nivel anatómico, selección de máscaras y sensibilidad del corredor.

Al mismo tiempo, todavía no se puede afirmar que MetalSynth-Pelvis sintetiza metal de forma coherente, porque el modelo generativo no está entrenado. Tampoco se puede decir que el Objetivo 1 está aprobado: `pub+MTW` pasa la prueba sin VAE, pero falta el round-trip completo. Y SAP aún está formulada, no evaluada sobre poses generadas por el muestreador final.

La situación más precisa es esta:

- **datos y cohortes:** avanzados;
- **fundamento bibliográfico y decisiones de alcance:** avanzados, con algunos PDFs/fuentes pendientes;
- **medición anatómica del corredor:** avanzada y con resultados reproducibles;
- **muestreador de poses completo:** pendiente;
- **representación atravesando el VAE:** pendiente;
- **renderizador de difusión:** pendiente;
- **comparación física y evaluación final:** pendiente.

La prioridad razonable es cerrar Objetivo 1 y Objetivo 2 antes de abrir más frentes bibliográficos o visuales. Esos dos objetivos forman el mínimo defendible y, además, son la base que necesita cualquier renderizador posterior.

## 12. Archivos de referencia para retomar el trabajo

- Estado cronológico: [`docs/ESTADO.md`](ESTADO.md)
- Definición y alcance: [`docs/00-tesis.md`](00-tesis.md)
- Decisiones: [`docs/01-decisiones.md`](01-decisiones.md)
- Datos: [`docs/02-datos.md`](02-datos.md)
- Métricas y términos: [`docs/03-glosario.md`](03-glosario.md)
- Riesgos e implicancias: [`docs/04-implicancias.md`](04-implicancias.md)
- Índice de papers: [`docs/literatura/_index.md`](literatura/_index.md)
- Resultado del corredor: [`experiments/objetivo2/outputs/e9ts_3mm/e9ts_resumen.md`](../experiments/objetivo2/outputs/e9ts_3mm/e9ts_resumen.md)
- Documento formal actual: [`tesis/main.tex`](../tesis/main.tex)
