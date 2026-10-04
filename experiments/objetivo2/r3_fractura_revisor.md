# Cribado de fractura en la cohorte del Objetivo 2 (#125)

## Para la autora: que pedir y como explicarlo

> Esta primera seccion es para ti, no para el medico. Las de abajo son las que el lee.

### La tarea, en una frase

Hay que mirar **30 tomografias de pelvis** y decir, en cada una, **si se ve una fractura, donde, y si la
imagen alcanza para decidirlo**. Nada mas. No se le pide diagnostico, ni opinion sobre tornillos, ni
nada que tenga que ver con el programa.

### Por que lo necesitas, en lenguaje llano

El programa mide, en cada pelvis, el **ancho del tunel de hueso** por donde cabria un tornillo. En 15 de
las 72 pelvis ese tunel salio **mas angosto** que el tornillo de referencia, y la tesis lo esta
explicando como **variacion normal entre personas**.

El problema: en una de esas 15 ya se confirmo una **fractura**. Y una fractura desplazada **angosta el
tunel**. Si varias de esas 15 estuvieran fracturadas, lo que la tesis llama "anatomia normal" seria en
realidad **hueso roto sin detectar**. Eso cambiaria como se interpreta el resultado.

Por eso hay que mirar.

### Por que son 30 y no 15

Si solo miraras las 15 angostas y aparecieran tres fracturas, **no sabrias si eso es mucho o poco**:
quiza en cualquier grupo de 15 pelvis de esta coleccion aparecerian tres.

Por eso van **15 angostas + 15 normales, mezcladas y sin etiqueta**. Al final se cuenta cuantas
fracturas cayeron en cada grupo. Si hay mas entre las angostas, la sospecha se confirma; si estan
repartidas, es solo la tasa de fondo de la coleccion.

**El medico no debe saber a que grupo pertenece cada caso.** Si lo supiera, buscaria mas fuerte en las
angostas y el resultado dejaria de servir. Por eso el reparto esta en un archivo aparte,
`r3_fractura_grupos.csv`, que **no se entrega**.

### Que le entregas

1. La carpeta con las **60 imagenes** (dos por caso).
2. `r3_fractura_revisor.csv`, que es donde anota.
3. Este documento, desde la seccion *Por que esta revision existe* hacia abajo.

**No** le des `r3_fractura_grupos.csv`.

### Que le dices

> Son 30 tomografias de pelvis, anonimas y mezcladas. En cada una necesito que me digas tres cosas:
> si ves fractura (si / no / dudoso), donde esta si la hay (sacro, ilion, ambos u otro), y si la imagen
> te permite juzgarlo.
>
> "Dudoso" es una respuesta valida y util: prefiero un dudoso honesto a un "no" forzado. Son imagenes
> fijas, no el estudio completo, asi que no se puede descartar fractura con seguridad y no te estoy
> pidiendo que lo hagas.
>
> Es para investigacion, no son pacientes en atencion y no se emite ningun diagnostico. Voy a reportar
> tu revision indicando tu grado de formacion.

### Que haces tu antes y despues

**Antes:** confirma que las 60 imagenes esten, y que `r3_fractura_grupos.csv` **no** vaya en el envio.

**Despues:** me pasas el CSV lleno. Se cuenta cuantas fracturas hay en cada grupo y eso decide si la
interpretacion de los 15 tuneles angostos cambia o no.

### Lo unico que tienes que vigilar

- Que anote **su especialidad** en la columna `revisor`. Un medico recien egresado es un cribado valido,
  pero **no** es lectura de especialista, y la tesis tiene que decirlo tal cual.
- Que no fuerce respuestas. Un `dudoso` no es un fracaso de la revision: es informacion.
- Que no mire el archivo de grupos.

---

## Por que esta revision existe

La cohorte del Objetivo 2 se construyo con un criterio: **pelvis sin osteosintesis** (#52 a). Nunca se
verifico que fueran **pelvis sin fractura**, que no es lo mismo. El 2026-09-23 se confirmo que
`CLINIC_0060` tiene una fractura.

Eso importa por una razon concreta, no por prolijidad. `reilly2003effect`, ya citado en la tesis, midio
que **5-20 mm de desplazamiento craneal de una fractura de zona II reducen entre 36% y 90%** el area
disponible para tornillos iliosacros en S1. Y **#122** reporta que en **15 de 72** volumenes el corredor
medido es mas estrecho que el calibre del tornillo del benchmark, hoy presentado como **variabilidad
anatomica**.

`CLINIC_0060` tiene un corredor de **6.2 mm**: **esta dentro de esos 15**. Si mas de ellos tuvieran
fractura, parte de lo que la tesis atribuye a anatomia seria en realidad patologia no detectada, y hay
que decirlo antes de que lo diga otro.

## Diseno: ciego y con grupo de comparacion

**30 casos**, barajados con semilla fija, **sin indicar a que grupo pertenece ninguno**:

- **15** con corredor **estrecho** (`D_TS_max < 7.0 mm`), que son todos los que hay en la cohorte;
- **15** de **control**, tomados al azar de los 57 con corredor que si admite el calibre.

El grupo de comparacion no es un adorno. Si solo se miraran los 15 estrechos y aparecieran, digamos,
tres fracturas, no se sabria si eso es mucho o poco: podria ser la tasa de fondo de la coleccion. Con
los dos grupos, la comparacion contesta la pregunta que importa —**¿hay mas fractura entre los
corredores estrechos?**— y no solo si hay fractura.

Por eso la planilla **no dice** a que grupo pertenece cada caso. El reparto esta en
`r3_fractura_grupos.csv`, que **no se entrega al revisor** y solo se abre al analizar.

## Que abrir por caso

Rutas en el CSV, relativas a `experiments/objetivo2/`. Las 60 laminas estan en disco.

1. **`lamina_corredor`** (`outputs/e9ts/laminas/<caso>.png`): a la izquierda el perfil de diametro por
   altura; a la derecha un corte coronal por el centro del mejor corredor.
2. **`lamina_mascaras`** (`outputs/ts_total_qc/laminas/<caso>_planos.png`): las mascaras de
   TotalSegmentator en tres planos. `sacrum` naranja, `vertebrae_S1` rojo, `hip_left` cian,
   `hip_right` verde.

Si un caso no se decide con las laminas, los CT estan en `data/` y las mascaras completas en Khipu
(`~/metalsynth/data/ts_total/`).

## Que hay que contestar

| Columna | Que poner |
|---|---|
| `revisor` | quien juzga, y si tiene especialidad. **Ponlo explicito**: importa para lo que se puede afirmar |
| `fractura` | `si` / `no` / `dudoso` |
| `donde` | solo si `fractura = si`: `sacro`, `ilion`, `ambos`, `otro`. Detallar en `comentario` |
| `legible` | `si` / `no`, segun se pueda juzgar con lo que se ve |
| `comentario` | libre. Obligatorio en `si`, `dudoso` y `legible = no` |

**`dudoso` es una respuesta valida y util.** Un cribado sobre cortes sueltos no demuestra ausencia de
fractura (#19, #21); solo detecta la que se ve. Forzar un `no` donde no se ve nada convertiria una
limitacion declarada en una afirmacion falsa.

## Lo que se decide con el resultado

- **Si no aparece fractura en ninguno de los dos grupos:** #122 se reporta como esta, y la limitacion se
  escribe con respaldo en vez de con prudencia.
- **Si aparece y se concentra en los estrechos:** la interpretacion de #122 cambia, y una parte de los
  15 corredores estrechos pasa de "anatomia" a "patologia no detectada". Es un resultado publicable y
  hay que escribirlo.
- **Si aparece repartida por igual:** es tasa de fondo de la coleccion, se declara como limitacion de
  CTPelvic1K y #122 no se toca.

Las tres salidas son reportables. Ninguna conviene mas que otra.

## Limite de partida, que se declara

`CLINIC_0060` lo confirmo **un medico recien licenciado, sin especialidad**. Es una confirmacion real y
se cuenta como tal, pero **no es lectura de radiologo ni de traumatologo**, y asi debe figurar en
cualquier cifra que salga de aqui. Lo mismo vale para quien conteste esta planilla: por eso la columna
`revisor` pide la especialidad.
