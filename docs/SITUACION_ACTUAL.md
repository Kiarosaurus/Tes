# Situación actual de MetalSynth-Pelvis, explicada para defenderla

> **Corte del estado: 8 de octubre de 2026.** Este documento es una clase, no un registro. Está
> escrito como lo explicaría un profesor del área a una estudiante de computación que sabe IA pero no
> imagen médica, para que pueda **exponer y defender** la tesis. Pone el acento en **por qué** se tomó
> cada decisión y en **qué alternativa había**. Las cifras salen de [`01-decisiones.md`](01-decisiones.md),
> [`04-implicancias.md`](04-implicancias.md), [`ESTADO.md`](ESTADO.md), [`00-tesis.md`](00-tesis.md) y
> `tesis/main.tex`. Donde opino como profesor, lo digo: esas partes son juicio, no resultado.
>
> Convención: **HECHO** = ejecutado y registrado. **ABIERTO** = medido pero sin decisión, o con muy
> pocos datos para afirmarlo. **PENDIENTE** = todavía no existe.

---

## 0. La tesis en un minuto

**El problema.** Las redes que segmentan hueso en tomografías (TC) fallan cerca de los implantes
metálicos: el metal produce rayas claras y oscuras que tapan los bordes del hueso. Para entrenar redes
robustas a eso harían falta muchas TC con metal y con anotaciones, y hay pocas.

**La idea.** Fabricar esos ejemplos: tomar una pelvis **sin** metal, decidir **dónde** iría un tornillo
de forma quirúrgicamente creíble y **pintar** el tornillo con su artefacto alrededor.

**Lo que la tesis evalúa de verdad.** Evalúa la **coherencia física y quirúrgica** de lo fabricado: si
las posiciones se parecen a las de la cirugía real y si el artefacto se parece al de la física. **No**
mide si esos ejemplos mejoran a una red de segmentación. Eso está **fuera de alcance**, decidido y
justificado (sección 3.1). Es lo primero que tienes que tener claro, porque un jurado lo va a preguntar.

**La frase que resume el estado hoy:**

> La ruta latente se puso a prueba y no pasó (resultado negativo, y es un resultado). El muestreador de
> posiciones está implementado, ejecutado y cerrado. El sintetizador de apariencia ya entrena, genera y
> ya ejecutó la cadena completa sobre dos pacientes de validación, pero **todavía no tiene modelo
> elegido ni resultado evaluado**.

---

## 1. Lo mínimo de imagen médica para entender el resto

No hace falta más que esto para seguir el documento.

| Concepto | Qué es, en una línea | Por qué importa aquí |
|---|---|---|
| **TC y HU** | Una TC es un volumen 3D; cada vóxel guarda un número en **unidades Hounsfield (HU)**: aire ≈ −1000, agua = 0, hueso denso ≈ cientos a miles, metal miles | La red trabaja con **valores físicos**, no con colores. Un error de 50 HU en hueso es un error de medición, no de estética |
| **Ventana** | Un rango de HU que se "estira" a la escala de gris visible (p. ej. de −160 a 240 para tejido blando) | Una sola ventana no puede mostrar a la vez aire, hueso y metal. Por eso se usan **varias** |
| **Artefacto metálico** | Rayas claras (*streaking*), endurecimiento del haz y zonas negras por **inanición de fotones** | No queda dentro del tornillo: **se derrama** alrededor. Es lo que la tesis quiere generar |
| **Corredor óseo** | El "túnel" de hueso por donde puede pasar el tornillo sin salirse | Define dónde es razonable colocar el tornillo |
| **Brecha cortical** | Cuánto se sale el tornillo del hueso, en 4 grados: 0 (nada), 1 (< 2 mm), 2 (2–4 mm), 3 (> 4 mm) | Es la escala con que los cirujanos reportan malposiciones |
| **Difusión** | Modelo generativo que aprende a quitar ruido paso a paso; al revés, genera desde ruido | Es la familia de modelos del sintetizador |
| ***Inpainting*** | Rellenar solo una región de la imagen, dejando el resto intacto | Es la formulación del sintetizador: solo se toca la zona del tornillo |

Dos regiones que aparecen todo el tiempo:

- **`M`**: la máscara del implante (los vóxeles del tornillo).
- **`B_δ`**: una **banda de ~12 mm** alrededor de `M`. **`G = M ∪ B_δ`** es la región que el modelo
  puede modificar. La banda existe para que las rayas puedan aparecer **fuera** del metal.

---

## 2. El mapa: dos componentes, cuatro objetivos

El pipeline tiene **dos piezas que se diseñan y evalúan por separado**:

```
pelvis sin metal ──► [MUESTREADOR] ──► pose del tornillo ──► máscara M ──► [SINTETIZADOR] ──► TC con tornillo y artefacto
                     ¿dónde va?                                             ¿cómo se ve?
```

**¿Por qué separarlas?** Porque son dos preguntas con **referencias distintas**. Si la posición es
creíble se juzga contra series clínicas (cirujanos). Si la apariencia es creíble se juzga contra
física. Mezclarlas en una sola métrica haría imposible saber qué pieza falla.

| Objetivo | Pregunta | Estado |
|---|---|---|
| **1. Compuerta de la representación** | ¿Se puede comprimir la TC con un autoencoder preentrenado sin perder los HU del hueso? | **HECHO. Resultado: No-Go** |
| **2. Muestreador de colocación** | ¿Se pueden proponer posiciones de tornillo cuya distribución de errores se parezca a la cirugía real? | **HECHO y cerrado** |
| **3. Sintetizador** | ¿Se puede generar el tornillo y su artefacto con apariencia físicamente coherente? | **En curso**: entrena y genera; sin modelo elegido ni evaluación |
| **4. Métricas** | ¿Con qué se mide todo esto? | SAP (propia) **HECHA**; apariencia: métricas de Peters et al., con su definición operativa **decidida** |

---

## 3. Las decisiones, en el orden en que se tomaron

Te las cuento **en orden cronológico**, porque casi todas son consecuencia de la anterior: el
proyecto cambió de modelo por un resultado, y ese cambio arrastró a todo lo demás. Para cada una:
**qué se decidió, por qué, y qué alternativa había**.

### 3.1 Primero, recortar el alcance (septiembre)

**Decisión: la evaluación de segmentación (Dice, HD95) queda fuera.**

- **Por qué.** No es por falta de tiempo, y conviene decirlo así. Son **dos condiciones de los datos**,
  auditables: del subconjunto con metal (CLINIC-metal, 75 volúmenes) la publicación anota solo 14, y en
  local hay **178 de los 1 184** volúmenes publicados de CTPelvic1K. Un resultado de segmentación
  descansaría en una cohorte demasiado pequeña y mal anotada para sostener una afirmación de robustez.
- **Alternativa.** Hacer el experimento igual, con pocos casos. Se descartó porque un resultado débil
  en el experimento que más le importa al lector sería peor que declararlo trabajo futuro.
- **Cómo defenderlo.** "La tesis valida lo que se puede validar con los datos disponibles: que lo
  sintetizado sea coherente. Sin eso, medir utilidad no tendría sentido; con eso, queda como siguiente
  paso." (Ojo: el documento todavía tiene abierto *por qué* la coherencia debe establecerse antes de la
  utilidad; es un `\GAPDEC` de la introducción. Prepárate esa respuesta.)

**Decisión: no inventar métricas nuevas de apariencia.** Se retiraron dos métricas propias (BFC, ISC)
y se adoptaron las del protocolo de **Peters et al. (2025)** con sus nombres publicados: *bone
integrity*, *metal integrity*, *streak amplitude*.

- **Por qué.** Renombrar medidas ajenas y llamarlas contribución es un punto débil clásico frente a un
  jurado. La única métrica propia que queda es **SAP** (colocación).

**Decisión: el brazo de comparación física es el protocolo de Peters, no una reimplementación propia
de un simulador (XCIST/CatSim).**

- **Por qué.** Validar un simulador propio es una tesis en sí misma. Peters et al. publicaron un
  protocolo **híbrido** (imágenes clínicas + simulación) con código, y se puede reproducir.
- **Matiz que hay que saber decir:** **reproducir no es validar.** Validar un simulador exige
  compararlo contra un fantoma real escaneado en un tomógrafo real, y aquí no hay eso. Además, el
  artículo del simulador describe su propia validación como preliminar. Lo que se hace se llama
  **verificación de reproducción** (decisión 2026-10-05 (5)).

### 3.2 El plan original: difusión latente con Stable Diffusion 1.5 + ControlNet

Este es **el modelo de IA que se pensaba usar al principio**, y conviene entender por qué tenía sentido.

- **Qué era.** *Latent diffusion*: un **autoencoder (VAE)** comprime la imagen a un espacio latente
  pequeño, la difusión trabaja ahí, y el decodificador vuelve a la imagen. **Stable Diffusion 1.5** da
  el autoencoder y la red de difusión ya entrenados; **ControlNet** añade el condicionamiento (la
  máscara del tornillo) sin reentrenar la base.
- **Por qué tenía sentido.** Con pocos datos médicos, **partir de un modelo preentrenado** es la jugada
  estándar: no hay que aprender desde cero qué es una imagen. Y el latente abarata mucho el cómputo.
- **El riesgo que nadie había medido.** Ese autoencoder se entrenó con **fotos naturales**. Nada
  garantizaba que conservara **números físicos** (HU) al comprimir y descomprimir una TC.

**Decisión clave: poner una compuerta Go/No-Go antes de construir nada encima (Objetivo 1).** La regla
se fijó **por escrito antes de correr la prueba** (2026-09-17 (3)):

- error medio absoluto (MAE) en hueso **< 25 HU**, promediado por paciente sobre **34 pacientes de
  prueba**;
- seis combinaciones: autoencoder preentrenado o con **decodificador afinado** (encoder congelado) ×
  tres codificaciones multiventana;
- **basta con que pase una**; si no pasa ninguna, el Objetivo 3 no se ejecuta por esa ruta.

**¿Por qué 25 HU?** No hay umbral publicado de "aprobado" para la precisión en HU. Se ancló en el error
que alcanzan los métodos de reducción de artefactos sobre la misma escala (RMSE de 20.2 HU para NMAR;
12.3 y 12.74 HU para métodos aprendidos). Es un **orden de magnitud**, no una equivalencia, y así está
declarado.

**¿Por qué varias ventanas (codificación multiventana)?** Una TC va de −1000 a miles de HU; un modelo
de imagen trabaja con tres canales en [0, 1]. Meter todo ese rango en un canal aplasta el hueso. La
solución, tomada de trabajos de **reducción** de artefactos, es usar **tres ventanas** como tres
canales: una ancha (LW) para todo el rango, una media (MW, −320 a 480 HU) y una estrecha (SW, −160 a
240 HU). La ancha se comprime con **arcoseno hiperbólico (asinh)** hasta 20 000 HU para que quepa el
metal. Importante: **la tesis no reclama la multiventana como invento**; reclama **usarla para generar**
artefactos en vez de para quitarlos, junto con la banda `B_δ`.

**Resultado: No-Go.** La mejor combinación (decodificador afinado + asinh) dio **61.72 HU** (IC95
[55.12, 68.99]); los **34 de 34** pacientes quedaron por encima de 25 HU en todas las combinaciones. Los
controles descartaron que fuera falta de entrenamiento. Dentro de la banda, 69.89 HU.

- **Lectura:** los latentes de imágenes naturales **no transportan** los HU del hueso denso con esa
  tolerancia.
- **¿Y un autoencoder entrenado con TC?** Se miró **MAISI**, que sí es de TC. Se descartó **sin
  correrlo**: su propio código recorta la salida a [−1000, 1000] HU, y solo ese recorte, sin ningún
  modelo, ya da **42.24 HU** de error. Ningún peso puede bajar de esa cota.
- **Por qué esto es un buen resultado para la tesis.** Porque la regla se fijó antes, el criterio no se
  movió y el negativo se reporta como resultado. Es exactamente lo que un jurado quiere ver: el
  proyecto **se puso una prueba que podía fallar, y falló**.

**Alternativas que había y por qué no:**

| Alternativa | Por qué no |
|---|---|
| Subir el umbral a 70 HU después de ver el resultado | Mover el criterio tras ver los datos invalida la prueba |
| Usar igual el decodificador afinado "como exploratorio" | Mostraría imágenes que la propia compuerta rechazó |
| MedVAE u otro latente médico | Excluye metal en su entrenamiento (#94) |
| Quedarse solo con Objetivos 1 y 2 | La autora quiso mantener la generación; el asesor (asistente) propuso recortar y ella lo rechazó (2026-09-17) |

### 3.3 El rediseño: difusión directamente sobre la imagen (Objetivo 3, "Diseño A")

**Decisión (2026-09-19): quitar el autoencoder y hacer difusión en el espacio de la imagen, por
parches alrededor del implante.** Es una decisión **posterior** al resultado del Objetivo 1, y así se
declara.

- **Por qué.** Si no hay compresión, **no hay error de ida y vuelta**: lo que el modelo no toca queda
  idéntico vóxel a vóxel. La multiventana, sin autoencoder, vuelve al valor original con error ~0
  (medido).
- **Consecuencia que tienes que saber explicar:** sin latente preentrenado, **ControlNet pierde su
  objeto** (ControlNet existe para condicionar una base congelada). Y como no hay una base preentrenada
  de TC en píxeles, **el modelo se entrena desde cero**. Eso no es una preferencia: es una consecuencia
  del No-Go.

#### El modelo concreto, pieza por pieza

| Pieza | Qué es | Por qué |
|---|---|---|
| **Red** | **U-Net de difusión** tipo DDPM/ADM, cuatro niveles (64, 128, 256, 512 canales), con atención; float32 | Es la arquitectura estándar y probada de difusión en píxeles; nada exótico que defender |
| **Entrada: 11 canales** | 3 cortes axiales contiguos × 3 ventanas = 9 canales de imagen, + `M` + `G` | Es **2.5D**: ve los cortes vecinos para tener continuidad en 3D, pero genera solo el **corte central** (3 canales de salida). Un modelo 3D completo costaría mucho más memoria y datos |
| **Condicionamiento** | Por **concatenación**: las máscaras y el contexto entran como canales extra | Es lo más simple y no requiere una base congelada (que ya no existe) |
| **Formulación** | ***Inpainting* de `G`**: la red recibe el parche con `G` borrada y rellena solo `G`. Fuera de `G` se **copia** el original | La preservación del resto de la anatomía vale **por construcción**, no por medición. Es una garantía fuerte y fácil de defender |
| **Pérdida** | Error cuadrático **solo dentro de `G`**, promediado por imagen | Fuera de `G` no hay nada que aprender. Y promediar por imagen evita que las prótesis grandes dominen el aprendizaje |
| **Objetivo de predicción** | Predicción de **`v`** (en vez de ruido `ε`) | Más estable cuando la señal tiene un rango dinámico grande, como aquí, donde el metal satura las ventanas estrechas |
| **Planificador de ruido** | **Coseno** (Nichol y Dhariwal), 1 000 pasos | Estándar para imágenes; reparte mejor el ruido que el lineal |
| **Muestreo** | **DDIM determinista**, 50 pasos, semilla fija | Rápido y reproducible: misma semilla, misma imagen (en el mismo dispositivo, ver 3.8) |
| **Optimizador** | AdamW, tasa 1e-4, lote 4, parches de 256 × 256 | Valores por omisión del código; **no** están congelados en un registro (es un `\GAPDEC` abierto) |

**Alternativas que había, en mi opinión de profesor:**

- **Difusión 3D completa.** Más fiel al artefacto, que es 3D. Pero con 47 pacientes de entrenamiento y
  GPU compartida, era inviable. El 2.5D es un compromiso razonable y declarado.
- **Modelos más ligeros (GAN, U-Net de regresión).** Una U-Net que prediga directamente la imagen
  sería más barata, pero promedia: produce rayas borrosas. La difusión genera **variabilidad** (varias
  muestras por caso), que es justo lo que se quiere para aumento de datos.
- **No usar IA: solo simulación física (Peters) sobre las poses del muestreador.** Esta es **la
  pregunta más peligrosa de tu defensa**, y el documento todavía la tiene abierta como `\GAPDEC`:
  *si la física puede correrse sobre las mismas poses, ¿para qué un sintetizador aprendido?* Los
  argumentos que el repositorio sí permite: el protocolo físico es **2D de una sola fila de detector**,
  cuesta **~70 s por corte**, y su validación no cubre implantes pélvicos en 3D. Pero la respuesta
  completa (coste por volumen, escala, generalidad) **no está escrita ni medida**. Prepárala con la
  autora y el asesor antes de exponer.

### 3.4 Con qué datos aprende el sintetizador

El sintetizador aprende de pacientes que **ya tienen** metal: ahí el implante real da a la vez la
máscara y la apariencia objetivo. Luego, en uso, se le pide pintar un tornillo en una pelvis **limpia**.

**Decisión D1: la máscara de entrenamiento se obtiene con umbral de 2500 HU** (el semimáximo local queda
como sensibilidad). Por qué: es el único umbral validado en esta cohorte (0 falsos negativos en 113
candidatos). Consecuencia aceptada: a 2500 HU algunos tornillos salen fragmentados, mientras que la
máscara sintética es un cilindro liso. Eso es un **desplazamiento de dominio declarado**.

**Decisión D2: la unidad de entrenamiento es el *componente* de metal, no el corte.** Este es un buen
ejemplo de **decisión forzada por una medición**:

- Primero se recortaba un parche de 256 × 256 por corte. Se midió: **en el 20.1 % de los cortes** la
  región `G` no cabía en el parche.
- La causa no era el tamaño del parche: algunos pacientes tienen metal repartido por toda la pelvis
  (hasta 380 mm). `G` estaba mal definida.
- El argumento de fondo: en síntesis se coloca **un** tornillo. Entrenar con varios implantes a la vez
  y usar con uno es otra brecha. Con un parche por componente, **0 de 1 217** parches se salían en el
  peor caso.
- Alternativa descartada: agrandar el parche (el cómputo crece con el cuadrado del lado y aun así no
  cubría 380 mm).

**Criterio de inclusión (R1–R4), fijado antes de entrenar:**

- **R1**: el componente está **dentro del cuerpo** (fuera quedan cremalleras, electrodos).
- **R2**: el caso tiene **material ortopédico declarado** en la auditoría.
- **R3**: el parche contiene metal del componente, más **todos** los parches de "solo banda"
  disponibles.
- **R4**: tamaño y forma **no** filtran: se reportan.

La idea más importante de esta decisión: la pregunta no es *"¿esto es un tornillo?"*, sino **"¿este
ejemplo enseña algo que en síntesis será falso?"**. El modelo aprende la relación *máscara →
artefacto*, que es física. Filtrar por forma tiraba datos: en una muestra revisada, solo **5 de 40**
componentes eran tornillos. Sobre esas mismas láminas, el criterio nuevo coincidió con la revisión
humana en **36 de 39** decisiones de incluir o excluir; el anterior, basado en forma, acertaba el tipo
en **16 de 40**.

**Resultado:** **241 componentes de 47 pacientes** para entrenar; **validación = 3 pacientes** con
implante real (`metal_0011`, `metal_0039`, `metal_0056`). Ojo con dos cosas:

- **La validación es pequeña y desbalanceada**: `0011` aporta el **60 %** de los parches.
- **"Validación" aquí es el término de aprendizaje automático**: pacientes que el modelo no usa para
  aprender y que sirven para vigilarlo. No tiene nada que ver con validar clínicamente.

**Tres desplazamientos de dominio, declarados (no escondidos):**

1. Máscara de entrenamiento por umbral (irregular) frente a cilindro liso en síntesis.
2. El contexto de entrenamiento **ya tiene rayas** del implante real; la pelvis limpia no.
3. Los parches de solo banda son **menos frecuentes** en entrenamiento (0.62 por parche con metal) que lo
   que la geometría predice para la síntesis (1.40). 1.40 no era alcanzable con los datos que hay.

Saber nombrar estos tres desplazamientos es de lo que más te va a proteger en la defensa: un jurado
que los encuentra solo piensa que no los viste; uno que los ve declarados piensa que los mediste.

### 3.5 El tornillo: tres geometrías para tres preguntas

Un detalle que parece menor y que es de los más finos del proyecto:

| Geometría | Para qué | Por qué ese valor |
|---|---|---|
| Envolvente **6.5–8.0 mm** | ¿**Cabe** un tornillo en este corredor? | Calibre nominal publicado |
| Cilindro **~4.91 mm** | Lo que se **sintetiza** | El cuerpo real del tornillo es más fino que su rosca. Medido sobre los tornillos reales del dataset (mediana 4.91 mm), y coincide con el catálogo (4.8 mm) dentro de un cuarto de vóxel |
| Cilindro **7.0 mm** | Con qué se **mide** la brecha cortical | Es el calibre de la serie clínica de referencia. Medir con otro calibre metería un sesgo dentro de la comparación |

El tipo de tornillo se fijó como **transilíaco-transsacro**: la trayectoria cruza las dos articulaciones
sacroilíacas, de cortical a cortical. Cuando el texto describe trabajos ajenos, sigue diciendo
"iliosacro", porque cambiarlo les atribuiría algo que no dijeron.

**Alternativa descartada:** un cilindro de 6.5–8.0 mm en todo el trayecto **sobreestima el metal en más
del doble** de área. La lección: no se elige "el número del catálogo"; se elige **el número que
corresponde a la pregunta**.

### 3.6 El muestreador de posiciones (Objetivo 2): cómo y por qué

**Qué hace.** Para cada pelvis: segmenta el hueso, busca el corredor de S1, y propone **50 posiciones**
perturbando ese eje. Luego mide cuánto se sale cada posición del hueso (grado de brecha).

**El modelo de IA que usa: TotalSegmentator (v2.18.0, basado en nnU-Net).** Es un segmentador
preentrenado y público; aquí no se entrena nada.

- **Por qué no un umbral de HU para el hueso.** Se intentó y falló: dentro del sacro, la mediana de la
  fracción de vóxeles por debajo de 150 HU sobre el eje del corredor era **0.42**. El hueso esponjoso
  tiene HU bajos, y un umbral lo "ahueca".
- **Precaución declarada:** su publicación no reporta precisión para la etiqueta de S1 que se usa, así
  que esa precisión no se asume; las máscaras pasan control de calidad por caso.

**La decisión más importante del Objetivo 2 (D-O2.1): el muestreador NO se calibra contra la serie
clínica.** Este es el razonamiento que más vale la pena que domines:

- La referencia clínica es **Zwingmann et al. (2009)**: dos distribuciones de grados de brecha, una con
  **navegación** (69 % grado 0) y otra **convencional** (40 % grado 0).
- La tentación: ajustar los parámetros del muestreador hasta reproducir esos porcentajes.
- **Por qué no:** si ajustas a los datos y luego te comparas con los mismos datos, la comparación no
  prueba nada. SAP, la única métrica propia, se quedaría vacía.
- **Lo que se hizo:** la perturbación sale de una **fuente independiente** (la holgura cortical de 5 mm
  de Kaiser et al.), bajo la convención declarada de que 5 mm = 2σ. De ahí σ = **2.5 mm** de traslación
  y un σ angular por caso (**2.07°** en la mediana). **Nada** se tomó de Zwingmann, ni siquiera la
  tolerancia de 4° que ese artículo cita. Todo se escribió **antes** de calcular la primera distancia.
- **Se aceptó de antemano** que la distancia podía salir alta. Un resultado alto honesto vale más que
  uno bajo forzado.

**¿Por qué Wasserstein-1?** Porque los grados son **ordinales**: confundir grado 0 con 1 es menos grave
que confundir 0 con 3. Wasserstein-1 mide cuánta "masa" hay que mover y **cuán lejos**, en unidades de
grado. Otras distancias (KL, χ²) tratarían los grados como categorías sin orden.

**Resultado (HECHO):**

| | Grado 0 | 1 | 2 | 3 | W1 a navegada | W1 a convencional |
|---|---|---|---|---|---|---|
| **Muestreador, 72 pelvis, 3 600 poses** | 51.5 % | 31.4 % | 11.1 % | 6.0 % | **0.206** | 0.230 |
| Zwingmann, navegada | 69 % | 15 % | 8 % | 8 % | — | — |
| Zwingmann, convencional | 40 % | 37 % | 11.5 % | 11.5 % | — | — |

**Lo que hay detrás del agregado.** En **15 de las 72** pelvis el corredor mide menos de 7 mm, así que
hasta el eje ideal perfora: el grado 0 es **inalcanzable por la anatomía**, no por el muestreador.
Separando (análisis *post hoc*, declarado como tal): en las **57** pelvis viables, el grado 0 sube a
**64.2 %** y W1 a la navegada baja a **0.183**; en las 15 estrechas, el grado 0 es 3.3 %. **El resultado
que se defiende es el agregado preinscrito**; la estratificación va al lado para explicar de dónde sale
la distancia. Restringir la cohorte a las viables se rechazó: sería seleccionar pacientes por una
variable ligada al resultado.

**El cribado de fracturas.** ¿Por qué hay corredores tan estrechos? Un médico (licenciado, sin
especialidad) revisó a ciegas 30 pelvis: **20 de 30 tienen fractura**, 10 y 10 en cada grupo. La
fractura sacra **desplazada** aparece en 7 de 15 estrechos frente a 2 de 15 controles (p = 0.109). La
lectura honesta: una fracción **no cuantificable** del estrechamiento puede ser patología. Y una frase
que **no** debes decir nunca: "pelvis sanas" o "intactas". Son pelvis **sin osteosíntesis**.

**Límites que ya están declarados:** el eje se busca en una rejilla de 5° mientras la tolerancia citada
es de 1.53° (sesgo conservador: el muestreador parece peor de lo que sería); SAP mide sobre una máscara
de hueso, no sobre una cortical segmentada.

**Alternativa que había, en mi opinión:** un planificador que optimice "la mejor trayectoria". Se
descartó con razón: la cirugía real **no** produce una sola trayectoria, sino una distribución de
errores, y la variabilidad anatómica entre personas es grande. Para aumento de datos, la variabilidad
es lo que interesa.

### 3.7 El entrenamiento del sintetizador (octubre)

**Dos corridas en el clúster (Khipu):** `run01` (144 500 pasos, 8 h) y `run02` (60 000 pasos, 6 h 20,
a 0.377 s/paso).

**Hallazgo: sobreajuste.** La pérdida de validación baja hasta una **meseta entre ~20 000 y ~40 000
pasos** y luego sube. Entrenar más **empeora** el modelo.

**Decisión (2026-10-05 (2)): 30 000 pasos**, el centro de la meseta.

- **Qué tipo de elección es:** una elección de hiperparámetro **hecha sobre validación**, no fijada de
  antemano. Es legítimo (para eso existe validación) y no toca los pacientes de prueba, pero hay que
  decirlo así.
- **Matiz que un jurado puede atacar:** las dos corridas **no son independientes** (misma semilla, mismos
  datos). Que sus curvas coincidan no prueba reproducibilidad con otra semilla.

**Dos defectos de ingeniería que se encontraron por el camino**, y que vale la pena contar como
lecciones: el medidor de validación sorteaba datos distintos cada vez (la cifra oscilaba ~15 % por
*cómo* se medía), y el programa sobrescribía un solo archivo, de modo que **las pesas del mejor momento
se perdieron** en la primera corrida. Ambos se corrigieron; ahora se guarda `mejor.pt` en cada mínimo
(en `run02`, el paso 37 500).

### 3.8 Tres hallazgos incómodos, y cómo cambiaron el plan

Este tramo es el más instructivo del proyecto, porque muestra **cómo se corrige un diseño midiendo**.

**a) El suelo de −1000 HU (#141).** La codificación multiventana no puede bajar de −1000 HU, pero las
zonas negras del artefacto (inanición de fotones) bajan mucho más. Medido sin modelo: en el paciente
típico se recorta ~1 % de la banda, pero **19 de 77** pacientes pasan del 10 % y uno llega al 44.9 %.

- **Por qué no se detectó antes:** el Objetivo 1 solo estudió el **techo** de la representación (el
  metal), y medía error en **hueso**. El suelo nunca fue variable.
- **Decisión:** no cambiar la representación a mitad de camino (habría que rehacer todo), sino
  **preinscribir la regla** que decidirá si se declara como limitación o se cambia, y **reportar como
  cifra** la fracción de vóxeles aplastados junto al resultado. El sesgo es siempre **a la baja** y solo
  afecta al sintetizador, no al brazo físico.
- **Alternativa, en mi opinión:** si se hubiera previsto, una compresión asinh **simétrica** (que cubra
  también el negativo) lo habría evitado desde el principio. Es una buena línea de "trabajo futuro".

**b) La pérdida de validación no sirve para elegir el modelo (#145, decisión 2026-10-05 (6)).**
Comparando los dos checkpoints sobre los mismos cortes y la misma semilla, el de **menor pérdida**
(`mejor.pt`) parecía generar mucho menos metal. Conclusión: la pérdida de difusión **no ordena** los
modelos por lo que la tesis mide (fidelidad de HU, apariencia).

- **Decisión:** el modelo se elegirá por **apariencia**, no por pérdida.
- **Una corrección que vale oro, y que debes saber contar:** la primera propuesta era elegir por qué tan
  bien **reconstruye implantes reales**. Se descartó porque esa tarea **premia memorizar**: los
  implantes de validación se parecen a los de entrenamiento, y el modelo más sobreentrenado ganaría por
  una razón que no sirve para el uso real (poner un tornillo **donde no había nada**).
- **Criterio adoptado:** generar sobre pelvis **limpias** de validación con cada checkpoint candidato, y
  comparar dos estadísticos contra los implantes reales: el **perfil radial de HU** alrededor del metal
  (mediana y percentil 95, como elevación sobre el anillo de 12–15 mm) y el **histograma de HU dentro
  de `M`**. Gana el que más cáscaras tenga dentro del rango real de los 3 pacientes de referencia. Con
  n = 3, el cotejo **descarta**, no prueba.
- **Por qué el percentil 95:** las rayas viven en las **colas** de la distribución; la mediana sola no
  las ve.

**c) El decodificador estaba borrando metal (#152, la más importante de la última semana).** Al
generar, varios valores se repetían **exactos** en pacientes y semillas distintos (~236 y ~472 HU).

- **La causa:** la regla de lectura del Objetivo 1 toma "el canal más estrecho no saturado". Si el
  modelo deja un canal estrecho **casi** saturado (p. ej. 0.989 en vez de 1.0), la regla cree que no
  está saturado y devuelve **el techo de esa ventana**, aunque el canal ancho diga "metal". En ~95 % de
  esos vóxeles el canal ancho marcaba metal: **el modelo sí generaba metal; el decodificador lo borraba.**
- **Consecuencia:** buena parte de "el modelo de menor pérdida genera la mitad del metal" era **del
  decodificador, no del modelo**. Y peor: también recortaba la cola clara de las rayas en la banda, así
  que cualquier amplitud de rayas medida así saldría subestimada.
- **Decisión (2026-10-07):** para el Objetivo 3, una **mezcla suave**: se parte del canal ancho y cada
  canal estrecho pesa menos cuanto más cerca está de saturar (rampa entre 0.01 y 0.05). La regla del
  Objetivo 1 es un **caso particular** de esta, así que **el Objetivo 1 no cambia ni una cifra**. El
  valor 0.05 se fijó sobre validación con un criterio escrito antes del resultado.
- **La lección de método, que la propia bitácora subraya:** *un valor que se repite exacto en
  condiciones distintas es un artefacto de medición hasta que se demuestre lo contrario.*

### 3.9 La cadena completa ya corrió (ABIERTO)

Por primera vez se encadenó todo: **pelvis limpia → pose sobre el corredor → rasterizado de `M` →
generación**, sobre **dos pacientes de validación** (`0101` y `0102`), con los dos checkpoints
candidatos.

- **Los tres controles pasan:** la pelvis receptora no tenía metal en `G`; fuera de `G` no se toca nada;
  la composición es idéntica al original fuera de `G`.
- **Con el decodificador nuevo, los dos checkpoints generan metal de forma parecida** dentro de `M`
  (fracción de `M` sobre 2500 HU entre 0.928 y 0.992 en las cuatro corridas). Antes, con el decodificador viejo,
  parecían muy distintos.
- **Por qué esto todavía no es un resultado:** dos pacientes, una semilla, un tornillo por paciente, y
  las implicancias siguen ABIERTAS. Además, **CPU y GPU no dan el mismo ruido con la misma semilla**
  (#151): todo cotejo debe hacerse en un solo dispositivo.

### 3.10 Cómo se evaluará el sintetizador (decidido, sin ejecutar)

Esto ya está **preinscrito** (2026-10-05 (3) y (4)): se fijó antes de tocar los pacientes de prueba.

- **Endpoint primario único: *streak amplitude*** (Peters et al.): la diferencia entre el promedio del
  5 % superior y el del 5 % inferior de la desviación respecto a la imagen sin metal. Mide **el vano
  entre rayas claras y oscuras**, que es justo lo que el sintetizador dice generar.
- **Dónde se puede medir:** solo donde hay **verdad de terreno sin metal**, es decir, en los **14
  pacientes de prueba sin metal** (se compara la imagen sintética contra la original del mismo
  paciente). En los 20 pacientes de prueba con implante real no existe esa referencia: ahí se mide
  **discrepancia**, que es otra cosa y se llama distinto.
- **Las regiones de medición se derivan de la pose**, no se dibujan a mano como en el artículo
  original: anillos completos de un vóxel de guarda hasta 12 mm, en todos los cortes con metal menos
  8 mm por extremo. Es más reproducible y es idéntico para los dos métodos comparados.
- **Jerarquía de contrastes:**

| Contraste | Prueba | Qué demuestra |
|---|---|---|
| **Primario**: contra el brazo físico | **TOST** de equivalencia con margen `Δ` | Que el sintetizador es comparable a la física |
| **Realismo**: contra artefactos reales | distancia entre distribuciones | Que lo generado se parece a lo que existe |
| **Cordura**: contra copia y pegado | Wilcoxon de una cola | Solo un piso. **No es evidencia de calidad** |

**¿Por qué TOST y no un test de diferencia?** Este es un punto de estadística que puede salvarte en la
defensa: con n = 14, un p > 0.05 en un test de diferencia significa casi siempre **falta de potencia**,
no igualdad. Para afirmar "comparable" hace falta un test de **equivalencia**: se concluye solo si el
intervalo de confianza del 90 % de la diferencia cae entero dentro de [−Δ, +Δ].

**¿De dónde sale Δ?** No hay un margen publicado. Se definirá como la **variabilidad propia del método**
(entre semillas del mismo caso y entre repeticiones del brazo físico), medida **solo en validación**.
La idea: si el método no se distingue de la física más de lo que se distingue de sí mismo, "comparable"
está justificado. **Δ todavía no está medido**, y con 3 pacientes de validación la n es pequeña; eso se
declara.

**¿Por qué el contraste contra copia y pegado es "cordura"?** Porque copiar y pegar un tornillo no
produce rayas por construcción: su amplitud vale ~0, y **cualquier cosa** que genere algo le gana.
Presentarlo como evidencia sería tramposo, y la tesis lo dice explícitamente.

**Se acepta de antemano** que el resultado honesto puede ser *"no se pudo concluir equivalencia con esta
n"*. El Objetivo 1 ya demostró que un negativo bien hecho es reportable.

---

## 4. ¿Qué modelos de IA se usan, en una tabla?

| Modelo | Dónde | Estado | Por qué este |
|---|---|---|---|
| **VAE de Stable Diffusion 1.5** (preentrenado y con decodificador afinado) | Objetivo 1 | **Probado y descartado** (No-Go, 61.72 HU) | Era la base natural de la difusión latente con ControlNet |
| **MAISI** (autoencoder de TC) | Objetivo 1, extensión | **Descartado sin correr** (su recorte ya da 42.24 HU) | Era el candidato "de TC" para el latente |
| **TotalSegmentator 2.18.0** (nnU-Net) | Objetivo 2 | **En uso** | Un umbral de HU no representa el hueso esponjoso |
| **U-Net de difusión propia** (DDPM/ADM, predicción `v`, DDIM) | Objetivo 3 | **En uso**, entrenada desde cero | No existe base preentrenada de TC en píxeles; sin autoencoder no hay error de ida y vuelta |
| **ControlNet** | Objetivo 3 (plan original) | **Retirado** | Necesita una base congelada que ya no existe |

Aparte, el proyecto usa agentes de lenguaje como **herramientas de apoyo** (leer artículos, proponer
una clasificación visual preliminar de metal, revisar la redacción). Ninguno produce resultados de la
tesis por sí solo: sus propuestas las revisa la autora.

---

## 5. Lo que se puede afirmar hoy, y lo que no

**Se puede afirmar:**

- La compuerta del Objetivo 1 se fijó antes, se corrió, y dio **No-Go**; los latentes disponibles, incluido
  uno de TC, no cubren el rango del hueso denso y el metal.
- El muestreador y SAP existen, corren y produjeron **3 600 posiciones en 72 pelvis**, con W1 = 0.206 a la
  serie navegada, sin ningún parámetro ajustado a esa serie.
- El cribado de fracturas está hecho (20 de 30), y la fractura no explica por sí sola los corredores
  estrechos.
- El sintetizador **entrena** (meseta entre ~20 000 y ~40 000 pasos), **genera**, y la **cadena completa
  corrió** sobre dos pacientes de validación con sus controles en verde.
- El brazo físico **corre en local**, y se verificó en su código que proyecta paciente y metal **juntos**.
- El endpoint primario del Objetivo 3 está **definido por completo antes de ver resultados**.

**No se debe afirmar:**

- Que el sistema "ya sintetiza TC con metal" como resultado: **no hay modelo elegido ni evaluación**.
- Que un checkpoint es mejor que otro.
- Que las posiciones fueron aprobadas por un médico, o que SAP demuestra seguridad clínica.
- Que las pelvis son sanas o sin fractura.
- Que se **validó** el simulador físico (se **reprodujo**).
- Que el sintetizador genera **todo** el artefacto (el suelo de −1000 HU lo impide).
- Que el entrenamiento es reproducible con otra semilla (no se ha probado).
- Que los ejemplos mejoran la segmentación (fuera de alcance).

---

## 6. ¿Pudo hacerse mejor? Mi lectura como profesor

Esto es **opinión**, no resultado. Sirve para que no te tomen por sorpresa.

1. **El orden de la apuesta fue correcto.** Poner la compuerta del autoencoder **antes** de construir
   encima ahorró semanas. Muchos proyectos descubren ese problema al final.
2. **Lo que yo habría medido antes: el suelo de la representación.** El Objetivo 1 estudió el techo
   (metal) y el error en hueso, pero no el rango negativo del artefacto. Con una compresión simétrica
   desde el inicio, #141 no existiría. Es un aprendizaje legítimo y una línea clara de trabajo futuro.
3. **Lo que yo habría decidido antes: cómo se elige el modelo.** Que la pérdida de difusión no ordene
   bien la calidad es conocido en la práctica; definir el criterio de apariencia antes de entrenar
   habría evitado elegir 30 000 pasos con un instrumento que después se vio débil.
4. **La debilidad estructural más grande: el desplazamiento de dominio.** El modelo aprende en
   pacientes que ya tienen rayas y con máscaras irregulares, y se usa en pelvis limpias con máscaras
   lisas. Alternativas posibles: entrenar con máscaras suavizadas o paramétricas, o con contexto
   recortado. Ninguna es gratis y la decisión sigue abierta.
5. **La pregunta que más te conviene preparar:** *¿por qué un sintetizador aprendido si existe la
   simulación física?* La tesis todavía no la tiene escrita (`\GAPDEC`). Sin una respuesta cuantitativa
   (coste por volumen, escala, cobertura 3D), es el flanco más expuesto.
6. **Lo que está muy bien hecho y debes enfatizar:** la preinscripción sistemática (compuerta,
   muestreador, criterio de inclusión, endpoint), la negativa a calibrar contra la referencia, y que los
   tres hallazgos incómodos se encontraron **midiendo** y están registrados. Un trabajo que mide su
   propio techo es más defendible que uno que no lo buscó.

---

## 7. Próximos pasos, en orden

1. **Clasificar el tipo de implante** de los 3 pacientes de referencia (`metal_0011`, `0039`, `0056`).
   Si no son tornillos, el cotejo para elegir checkpoint se revisa.
2. **Correr el cotejo** del perfil radial y del histograma (sintético frente a real) y **elegir
   checkpoint**.
3. **Sonda de viabilidad de Peters**: un corte con el tornillo y la anatomía de esta tesis. Su protocolo
   es 2D de una fila de detector y el tornillo mide unos 138 mm a lo largo de su eje (la longitud
   mediana del corredor): si esa extensión no es
   viable, el contraste primario se queda sin brazo y hay que replantearlo.
4. **Medir `Δ`** sobre validación, **congelar** `diseno_A.md`, y recién entonces la corrida final y la
   evaluación sobre los pacientes de prueba.
5. **Redacción**: el capítulo 3 ya declara el decodificador nuevo y el criterio de selección
   (`capitulo3-r08`); quedan las decisiones marcadas como `\GAPDEC` en todo el documento, el capítulo de
   resultados y el resumen.

---

## 8. Archivos para profundizar

| Para | Archivo |
|---|---|
| Por dónde va el proyecto | [`ESTADO.md`](ESTADO.md) |
| Cada decisión con su porqué | [`01-decisiones.md`](01-decisiones.md) |
| Hallazgos y riesgos | [`04-implicancias.md`](04-implicancias.md) (#141 suelo, #145 pérdida, #149–#152 cadena y decodificador) |
| Alcance | [`00-tesis.md`](00-tesis.md) |
| Diseño del sintetizador | [`diseno_A.md`](../experiments/objetivo3/diseno_A.md) |
| Código del modelo | `src/renderizador/modelo.py`, `difusion.py`, `entrenar.py` |
| Lectura de HU (decodificador) | `src/common/ventanas.py` |
| Resultado del muestreador | [`e13_sap.md`](../experiments/objetivo2/e13_sap.md), [`e13b_estratificado.md`](../experiments/objetivo2/e13b_estratificado.md) |
| Cribado de fracturas | [`r3_fractura_revisor.md`](../experiments/objetivo2/r3_fractura_revisor.md) |
| Brazo físico (copia parcheada) | `experiments/objetivo3/peters/` |
| Documento de entrega | [`overleaf/`](../overleaf/) |
