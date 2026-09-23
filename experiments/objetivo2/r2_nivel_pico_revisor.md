# Revision del nivel de un corte axial en ITK-SNAP (#121)

Mismo procedimiento que la revision del nivel de S1 (`r1_revision_itksnap_revisor.md`, #53), que ya
conoces. Cambia la pregunta: alli se juzgaba **un punto**; aqui se juzga **a que altura vertebral cae un
corte axial**.

La planilla es `r2_nivel_pico_itksnap.csv`. Es **ciega**: no trae ningun juicio previo, ni el corte de
S1, ni la respuesta esperada. Eso es deliberado. Si la planilla dijera de que nivel creemos que se
trata, la verificacion no serviria para nada.

## Que se te entrega

1. **Las 18 laminas** de `outputs/r2_nivel_pico/`, una por caso, nombradas por caso. **Con esto basta
   para contestar**; no hace falta abrir ningun software.
2. `r2_nivel_pico_itksnap.csv`, que es donde se anota, y este documento.
3. Opcional, solo si quieres comprobar algo en el volumen: los CT de la columna `Archivo` y las
   columnas de cortes. Son volumenes de CTPelvic1K, dataset publico con licencia CC-BY-NC-SA 4.0: uso
   no comercial y solo para esta revision.
4. Nada mas. Ninguna tabla con juicios, ningun resultado previo.

### Por que una lamina y no el mosaico anterior

En la revision de S1 objetaste, con razon, que el mosaico de +-60 mm **no permite contar vertebras**, y
se te preparo una planilla para ITK-SNAP. Esa planilla sigue **sin responder** (0 de 61), asi que la via
que se completa es la lamina y la via que permitia contar era la que no se completaba. Estas laminas
arreglan eso: son el **sagital completo**, con la columna lumbar dentro de la imagen, asi que se puede
contar mirando el PNG.

## Que hacer en cada caso

1. Abrir la lamina `outputs/r2_nivel_pico/<Caso>.png`. Es un sagital medio: **craneo arriba, anterior a
   la derecha**. La **linea roja** marca la altura a juzgar. La barra amarilla mide 10 mm.

2. **Juzgar el nivel de esa linea.** Contando vertebras desde la columna lumbar, que entra en la imagen:

   > La linea roja, ¿a la altura de que segmento sacro cae?

   Se juzga **la altura**, no un punto: la posicion horizontal de la linea no significa nada.

| `nivel_del_corte` | Significado |
|---|---|
| `S1` | el corte cae a la altura del primer segmento sacro |
| `S2` | a la altura del segundo |
| `S3` | a la altura del tercero |
| `S4+` | mas caudal que S3 |
| `union` | justo en el disco o la union entre dos segmentos; decir cuales en `comentario` |
| `otro` | fuera del sacro (coxis, L5, etc.); detallar en `comentario` |
| `?` | no se puede decidir |

3. Opcional, si algun caso no se deja decidir en la lamina: abrir el CT de `Archivo` en ITK-SNAP e ir a
   `corte_axial` (desde 0) o `corte_axial_1` (desde 1). Para saber cual de las dos convenciones usa tu
   ITK-SNAP, lleva el cursor a `corte_sagital` / `corte_coronal` / `corte_axial` y compara el HU con
   `HU_voxel` (`HU_mediana_3x3x3` es la mediana del entorno); anota `0` o `1` en `convencion_indices` y
   el valor leido en `HU_cursor`. Basta hacerlo una vez.


4. `vertebra_transicion`: `si` si hay una vertebra de transicion lumbosacra (sacralizacion o
   lumbarizacion) que haga ambiguo el conteo; `no` si no la hay; `?` si no se puede decir. Si es `si`,
   explicar en `comentario` como contaste.

5. `legible`: `si` / `no`. Poner `no` cuando el artefacto metalico, el ruido o el campo de vision
   impidan contar las vertebras con seguridad. **Esto no es lo mismo que `?`**: `?` es "no me decido",
   `legible = no` es "la imagen no da para decidirlo". Los dos son respuestas utiles y se reportan.

6. `comentario`: libre. Obligatorio en `union`, `otro`, `?` y `legible = no`.

## Sobre la muestra

Son casos de la cohorte del Objetivo 2, elegidos con semilla fija y **estratificados por la profundidad
del corte respecto de S1**: un tercio de los mas profundos, un tercio intermedios y un tercio de los mas
superficiales. No estan ordenados por esa variable en la planilla, y la planilla no la incluye.

## Despues

El asistente compara tu planilla con la altura medida y reporta el acuerdo por categoria. **No se edita
a mano ninguna otra tabla**, y tu planilla no sobrescribe nada.

Lo que se decide con el resultado:

- Si el corte cae en **S2** de forma consistente, el segundo corredor se reporta en la tesis como
  **corredor de S2**.
- Si no, se reporta como **"el segundo corredor por debajo de S1"**, sin atribuirle nivel vertebral.

Las dos salidas son publicables. No hay una respuesta que convenga mas que la otra.
