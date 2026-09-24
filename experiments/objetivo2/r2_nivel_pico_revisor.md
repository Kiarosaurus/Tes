# Revision del nivel del segundo corredor (#121)

Misma mecanica que la revalidacion de S1 (`r1_revision_laminas_revisor.csv`): se mira una lamina y se
dice a que segmento sacro corresponde una marca. Cambia **que** esta marcado.

La planilla es `r2_nivel_pico_revisor.csv`, **18 casos**. Es **ciega**: no trae ningun juicio previo, ni
la marca de S1, ni la respuesta esperada.

## Que esta marcado, y que NO

La cruz roja es **el punto por donde pasa el segundo corredor oseo** del caso: el centro de la
trayectoria transsacra mas ancha que el metodo encuentra por debajo de S1. El circulo discontinuo es su
**seccion**, de diametro `D_corredor_mm` (esta en la planilla, tipicamente 7-9 mm).

**Esto es distinto de la version anterior de esta revision**, que esta en
`r2_nivel_pico_revisor.ANTERIOR.md`. Alli se marcaba una **linea horizontal** a la altura del corredor,
y con el sacro inclinado esa linea puede cruzar dos segmentos: fue precisamente la objecion que se
levanto. Ahora se marca el punto, asi que la pregunta tiene una sola respuesta. **Si viste la version
con linea, ignorala: las laminas se regeneraron.**

**Salvedad honesta sobre el circulo:** el eje del corredor sale casi perpendicular al plano de la
lamina (mediana 8.5 grados respecto de la horizontal izquierda-derecha, maximo 27 sobre estos 18
casos), asi que el circulo es la seccion **proyectada**, no exacta. Sirve para ver el calibre, no para
medir.

## Que se te entrega

1. **Las 18 laminas** de `outputs/r2_nivel_pico/`, una por caso. Con esto basta.
2. `r2_nivel_pico_revisor.csv`, donde se anota, y este documento.
3. Opcional: los CT de la columna `Archivo`, si algun caso no se decide en la lamina. Son volumenes de
   CTPelvic1K, dataset publico con licencia CC-BY-NC-SA 4.0: uso no comercial y solo para esta revision.

## Que hacer en cada caso

1. Abrir `outputs/r2_nivel_pico/<Caso>.png`. Sagital medio: **craneo arriba, anterior a la derecha**.
   La barra amarilla mide 10 mm.

2. **Juzgar en que segmento sacro cae la cruz**, contando vertebras desde la columna lumbar, que entra
   en la imagen.

   | `nivel_del_punto` | Significado |
   |---|---|
   | `S1` | la cruz esta en el primer segmento sacro |
   | `S2` | en el segundo |
   | `S3` | en el tercero |
   | `S4+` | mas caudal que S3 |
   | `union` | justo en el disco o la union entre dos segmentos; decir cuales en `comentario` |
   | `otro` | fuera del cuerpo sacro (canal, foramen, ligamentos, ilion); detallar en `comentario` |
   | `?` | no se puede decidir |

   `otro` es una respuesta util y esperable: el corredor no tiene por que pasar por el centro del
   cuerpo vertebral. Si cae en un foramen o en el canal, decirlo es informacion, no un fallo.

3. `vertebra_transicion`: `si` / `no` / `?`, segun haya o no una vertebra de transicion lumbosacra que
   haga ambiguo el conteo. **Solo estas tres respuestas**; lo demas va en `comentario`.

4. `legible`: `si` / `no`. `no` cuando el artefacto, el ruido o el campo de vision impidan contar con
   seguridad. Distinto de `?`, que es "no me decido".

5. `revisor`: quien juzga. `comentario`: libre; obligatorio en `union`, `otro`, `?` y `legible = no`.

## Si la lamina no basta

La planilla trae `corte_sagital`, `corte_coronal` y `corte_axial` del **mismo punto** que muestra la
cruz, en indices del archivo original, en las dos convenciones (desde 0 y desde 1). Los mismos numeros
salen al pie de cada lamina.

**Para recorrer el volumen en horizontal, varia el corte AXIAL.** El sagital mueve izquierda-derecha y
el coronal anterior-posterior.

Para saber cual de las dos convenciones usa tu ITK-SNAP, lleva el cursor a los tres indices "desde 0" y
compara el HU con `HU_voxel` (`HU_mediana_3x3x3` es la mediana del entorno). Basta hacerlo una vez.

## Sobre la muestra

18 casos de la cohorte del Objetivo 2, elegidos con semilla fija y **estratificados por la profundidad
del corredor respecto de S1**: un tercio de los mas profundos, un tercio intermedios, un tercio de los
mas superficiales. No estan ordenados por esa variable en la planilla, y la planilla no la incluye.

## Que se decide con el resultado

- Si la cruz cae en **S2** de forma consistente, el segundo corredor se reporta en la tesis como
  **corredor de S2**, y se puede muestrear poses en ese nivel.
- Si no, se reporta como **"el segundo corredor por debajo de S1"**, sin atribuirle nivel vertebral.

Las dos salidas son publicables. Ninguna conviene mas que la otra.
