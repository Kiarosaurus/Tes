# 02 — Data card

> Lo genera Claude Code a partir de los datos reales en `data/`.
> La autora revisa y corrige. Sin inventar: lo que no se puede medir, se marca.

## Auditoría local — 2026-09-06

El inventario vigente está en
[`experiments/exploration-3d/resumen.md`](../experiments/exploration-3d/resumen.md),
con una fila por volumen en
[`revision.csv`](../experiments/exploration-3d/revision.csv).
Se recalcula desde los NIfTI originales; no cuenta máscaras como imágenes ni
usa el número de cortes como número de estudios. Las medianas y rangos se calculan
por eje, con spacing en mm y dimensiones en vóxeles, en la orientación nativa.

Los archivos locales corresponden a dataset6 y dataset7 de CTPelvic1K. El inventario
local no equivale a toda la colección publicada. La tabla anterior en
`experiments/exploration/dataset_summary.csv` incluía carpetas de máscaras que no
deben sumarse a las CT ni asumirse todavía disponibles en este equipo.

## Resultados medidos al cierre (2026-09-07)


Unidad: volumen CT, no corte. Rangos = mínimo–máximo. Spacing en mm;
dimensiones en vóxeles y ejes nativos del archivo. Candidato HU ≠ metal confirmado.

| Dataset | Volúmenes | Candidatos HU | Metal sí revisado | Pendientes |
|---|---:|---:|---:|---:|
| dataset6 | 103 | 38 | 0 | 103 |
| dataset7 | 75 | 75 | 0 | 75 |

| Dataset | Medida | Mediana [mín–máx] |
|---|---|---|
| dataset6 | Spacing x mm | 0.839 [0.64–1.129] |
| dataset6 | Spacing y mm | 0.839 [0.64–1.129] |
| dataset6 | Spacing z mm | 0.799988 [0.79895–0.801025] |
| dataset6 | Dim x | 512 [512–512] |
| dataset6 | Dim y | 512 [512–512] |
| dataset6 | Dim z | 350 [294–388] |
| dataset7 | Spacing x mm | 0.82 [0.601–1.266] |
| dataset7 | Spacing y mm | 0.82 [0.601–1.266] |
| dataset7 | Spacing z mm | 0.800049 [0.79895–0.801025] |
| dataset7 | Dim x | 512 [512–512] |
| dataset7 | Dim y | 512 [512–512] |
| dataset7 | Dim z | 350 [187–351] |

Grupos de duplicados exactos por vóxeles: 6.
Volúmenes únicos por contenido: 172 (no equivale a pacientes únicos).
Errores de lectura: 0.
Máscaras locales vinculadas por nombre: 0.


## Cobertura respecto de CTPelvic1K (2026-09-07)

Los 178 CT locales son 178 de los 1184 volúmenes que declara `liu2021ctpelvic1k`
(Tabla 1, p. 3). Faltan cinco sub-datasets públicos: ABDOMEN 35, COLONOG 731,
MSD_T10 155, KITS19 44 y CERVIX 41, es decir 1006 volúmenes. Toda tabla que salga
de aquí es un inventario **local**, no la descripción de CTPelvic1K completo.

La correspondencia `dataset6` → CLINIC y `dataset7` → CLINIC-metal no está declarada
en los headers NIfTI. Se infiere por coincidencia de conteo (103 y 75), spacing
(0.85 / 0.83 mm en plano y 0.80 mm en z) y dimensiones (512, 512, ~345 y ~334) con
la Tabla 1. Enunciarla como identificación inferida. Implicancia #18.

## Metal y cuerpos extraños

Se prioriza cualquier volumen con al menos un vóxel mayor que 2500 HU, sin filtro
de tamaño ni exclusión de objetos externos. Es una heurística de trabajo configurable,
no un umbral validado de identificación y no pertenece al protocolo de Peters.
Se conserva el HU escalado sin clipping. Los nombres de dataset y el resultado
negativo del filtro no sustituyen revisión 3D y multiplanar.

Las notas anteriores señalan DIU, electrodos, accesorios, piercing y un falso positivo
en borde del FOV en dataset6; se preservan como antecedentes por confirmar.
La imagen de la compañera se transcribió para metal_0002 y metal_0003 con su origen.
Los tipos de estructura, lateralidad, cantidad y severidad siguen sujetos a revisión.

Se generaron vistas locales en `experiments/exploration-3d/outputs/`. La revisión
preliminar de metal_0002 muestra varias estructuras de fijación, por lo que «1
dominante» no debe interpretarse como inventario exhaustivo. Dataset6_0017 muestra
una estructura pélvica hiperdensa compatible con el antecedente de DIU, pendiente
de confirmación. Ninguno de estos ejemplos equivale a revisión completa del CT.

## Clasificación visual asistida (2026-09-07)

Doce agentes `clasificador-metal` revisaron las láminas de los 113 candidatos HU.
Resultado en `experiments/exploration-3d/propuesta_clasificacion.csv`: 113 filas,
**todas `propuesta sin validar`**. Reparto en `Metal`: 65 `sí (propuesto)`,
42 `incierto`, 1 `no (propuesto)`, 5 con valor mixto por convivir varias estructuras.
En `Objeto extraño`: 60 `sí (propuesto)`, 52 `incierto`, 1 mixto. Ningún `no` en esa
columna, porque 16 cortes axiales no demuestran ausencia.

Estas filas **no** son clasificación validada y no entran a `revision.csv` ni a
ninguna cohorte hasta que la autora recorra el volumen. Los conteos de metal
confirmado siguen en 0.

Cuatro límites que la revisión dejó documentados, con sus implicancias:
el umbral no detecta objetos bajo 1500 HU (#19), hay duplicados exactos que cruzan
dataset6 y dataset7 (#20), parte de CLINIC-metal tiene material extracorpóreo y no
osteosíntesis (#21), y `Objeto extraño` carece de definición operativa (#22).

## Revisión 3D de la autora, fusionada el 2026-09-07

La autora revisó en 3D los 178 volúmenes y anotó tipo y cantidad. Sus reglas de lectura
y las cifras resultantes están en `04-implicancias.md`, sección del 2026-09-07.

| Magnitud | Valor |
|---|---:|
| dataset7 con material ortopédico | 72 de 75 |
| ...de contenido único (sin 3 duplicados internos de dataset7) | 69 |
| dataset7 SIN material ortopédico (duplicados cruzados con dataset6) | 3 |
| dataset6 con objeto metálico | 33 de 103 |
| ...solo extracorpóreo (ropa, piel) | 27 |
| ...con DIU | 6 |
| dataset6 sin objeto, candidatos a entrenamiento limpio | 70 |

**Actualización 2026-09-10 (#45, #21; confirmado por la autora).** La unidad de
independencia es el paciente. `Grupo paciente` está lleno en las 178 filas (script
`experiments/exploration-3d/grupo_paciente.py`), con su fuente en `Procedencia paciente`:
**178 volúmenes = 168 pacientes**, 10 grupos con más de un volumen (6 copias exactas por
SHA256, 3 por cortes compartidos confirmados por la autora y `metal_0065`/`0066` por
observación visual). `metal_0068` no tiene material ortopédico. Con eso:

| Recuento por paciente | Volúmenes | Pacientes |
|---|---:|---:|
| dataset7 con material ortopédico | 71 | 65 |
| dataset6 sin objeto | 70 | 69 |

`sin vinculo detectado` no prueba que dos filas sean pacientes distintos: solo que ningún
hash las vincula. `metal_0059` y `metal_0071` tienen además una unión sin pérdida en
`data/derivados/` (`union_0059_0071.md`). La fila de `metal_0068` quedó corregida
(`correcciones_autora.py`).

**Volúmenes fuera de uso:** `experiments/exploration-3d/exclusiones.csv` (11 volúmenes,
ningún archivo borrado; decisión del 2026-09-10 en `01-decisiones.md`). **Particion por
objetivo:** `grupos.csv`, 179 unidades (178 + unión) y 168 pacientes con una unidad en uso:
grupo 1 = 65, grupo 2 = 37, grupo 3 = 66, excluido = 10, reproducibilidad = 1.

`Revisión 3D y cortes` vale `3D completa`, no `completa`: falta el recorrido de cortes.
Ninguna cohorte se asigna todavía.
Copia previa a la fusión: `experiments/exploration-3d/revision.previo-merge.csv`.

## Cohortes y anotaciones

- Entrenamiento candidato: revisión 3D y todos los cortes completa, metal=no,
  objeto extraño=no, revisor, fecha e identidad anonimizada agrupable.
- Prueba metal candidata: metal confirmado tras revisión. Se debe separar
  osteosíntesis pélvica de prótesis, otros implantes y objetos externos según el
  objetivo de evaluación; no todo metal es un caso objetivo de esta tesis.
- Casos pendientes, inciertos, duplicados o grupos de paciente por resolver no
  se admiten automáticamente en entrenamiento. No se ha definido el split final.
- Duplicados exactos: hash sobre forma y HU escalados. No detecta todas las posibles
  repeticiones del mismo paciente ni reemplaza verificación de identidad.
- Máscaras: la disponibilidad local se reporta en el resumen y por archivo en el CSV.
  Vincular por nombre no verifica alineación ni validez de las etiquetas.

Según la ficha `liu2021ctpelvic1k.md` ya verificada, CLINIC-metal tenía 14 volúmenes
anotados de 75 en el artículo. Esa cifra bibliográfica no acredita que las máscaras
estén descargadas localmente ni que su disponibilidad actual haya aumentado.
No se verificó el portal remoto en esta sesión. Sin ground truth local verificado,
la evaluación supervisada Dice/HD95 queda pendiente.

## Reproducibilidad e impacto

Comandos, columnas y limitaciones: [guía de uso](../experiments/exploration-3d/README.md).
Regenerar el resumen tras cada revisión; los conteos HU no son conteos confirmados
de metal. La severidad visual no se presenta como escala clínica validada.
Implicancias #13 y #15: anotación, composición del conjunto y separación de cohortes.
