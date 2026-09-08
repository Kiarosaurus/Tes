# Cumplimiento del encargo de Víctor — auditoría de `exploration-3d`

Auditoría hecha el 2026-09-07 sobre el contenido real de la carpeta, no sobre lo que
el README dice que la carpeta hace. Unidad: volumen CT.

Veredicto corto: **la primera mitad del encargo (descripción de datos) está cubierta
para los datos que hay en disco; la segunda mitad (identificación de metal y
definición de cohortes) está instrumentada pero no ejecutada.** Nada en la carpeta
finge lo contrario: los conteos de metal confirmado están en 0 y las cohortes en
`pendiente`.

## 1. Data description

| Sub-tarea | Estado | Dónde | Reserva |
|---|---|---|---|
| Datasets | **Parcial** | `resumen.md`, `docs/02-datos.md` | Solo hay `dataset6` y `dataset7` en `data/`. Faltan 5 de los 7 sub-datasets de CTPelvic1K |
| Nº de imágenes por dataset | **Cumplido** | `resumen.md` | dataset6 = 103, dataset7 = 75, total 178 CT, 0 errores de lectura |
| Mediana de voxel spacing + rango | **Cumplido** | `resumen.md` | Por eje, en mm, orientación nativa. dataset6 0.839 [0.64–1.129] en x,y; dataset7 0.82 [0.601–1.266] |
| Mediana de dimensiones + rango | **Cumplido** | `resumen.md` | x=y=512 fijo en ambos; z mediana 350, rango 294–388 (d6) y 187–351 (d7) |

**Lo que falta y por qué importa.** El encargo dice «datasets», en plural y sin
restringir. Localmente hay 178 de los 1184 volúmenes que el paper declara
(`liu2021ctpelvic1k`, Tabla 1, p. 3): faltan ABDOMEN 35, COLONOG 731, MSD_T10 155,
KITS19 44 y CERVIX 41, es decir 1006 volúmenes. La tabla que se le entregue a Víctor
tiene que decir explícitamente que es un inventario **local**, no la descripción de
CTPelvic1K completo. Si él esperaba las siete filas, esto es una descarga pendiente,
no un error de medición.

**Correspondencia dataset6/dataset7 → CLINIC/CLINIC-metal.** No está declarada en
ningún header. Se sostiene por tres coincidencias con la Tabla 1 del paper: número de
volúmenes (103 y 75), spacing declarado (0.85 / 0.83 mm en plano, 0.80 mm en z) y
dimensiones (512, 512, ~345 y ~334). Es una inferencia consistente, no un dato del
archivo. Conviene decirla como inferencia.

## 2. Identify the images with metal

| Sub-tarea | Estado | Dónde | Reserva |
|---|---|---|---|
| ¿Qué dataset contiene metal? | **Parcial** | `resumen.md`, `revision.csv` | 75/75 de dataset7 y 38/103 de dataset6 superan 2500 HU. Candidato HU ≠ metal. dataset6 no está limpio por defecto |
| ¿Cuántas imágenes? | **NO cumplido** | `resumen.md`, columna «Metal sí revisado» | 0 confirmadas. Solo hay 113 candidatos por umbral |
| Mostrar ejemplos de metal | **Parcial** | `outputs/`, tabla final del README | 3 casos con vistas (metal_0002, metal_0003, CLINIC_0017), anotados como revisión parcial |
| Definir train (sin metal / objetos extraños) y test | **NO cumplido** | `resumen.md`, «Elegibilidad provisional» | 166 `pendiente`, 12 `resolver duplicado`, 0 asignados. No hay split |

**Por qué está bloqueado, en concreto:**

1. La barrera de `explorar.py:cohorts` exige `Revisión 3D y cortes = completa` más
   revisor, fecha y `Grupo paciente`. De las 178 filas, 175 tienen las 16 columnas
   manuales vacías y 3 están a medias (`CLINIC_0017`, `metal_0002`, `metal_0003`):
   `Revisión 3D y cortes = parcial`, revisor `Codex (propuesta visual preliminar)`,
   `Grupo paciente` vacío. Ninguna llega a `completa`, así que ninguna cohorte se
   asigna. `metal_0002` y `metal_0003` ya tienen `Metal = sí`, pero como la revisión
   es parcial no cuentan en «Metal sí revisado»: por eso ese conteo es 0 y no 2.
   Nota de proceso: esas tres filas las escribió un asistente directamente en
   `revision.csv`. El agente nuevo tiene prohibido hacerlo; escribe en
   `propuesta_clasificacion.csv` y la autora traslada lo que valida.
2. Hay 6 grupos de duplicados exactos por vóxeles (12 volúmenes, 172 contenidos
   únicos). Mientras no se elija representante, esos 12 no pueden entrar a ninguna
   cohorte sin arrastrar fuga entre train y test.
3. `Grupo paciente` no se puede llenar con el nombre del archivo: el hash detecta
   copias idénticas, no estudios repetidos del mismo paciente reorientados o
   recortados. Sin identidad por paciente no hay split defendible.
4. 0 máscaras locales vinculadas por nombre. El paper declara 14 de 75 anotados en
   CLINIC-metal; eso es bibliografía, no ground truth en disco. La evaluación
   supervisada del test con metal sigue sin insumo local (implicancia #13).

**Lo que sí queda demostrado y es entregable ya:** el umbral de 2500 HU marca los
75/75 de dataset7, lo que es consistente con el nombre CLINIC-metal, y marca 38 de
dataset6, lo que refuta que dataset6 sea utilizable como conjunto limpio sin revisar.
Ese segundo dato es el hallazgo útil de la semana y contradice la lectura ingenua
«dataset6 = sin metal, dataset7 = con metal».

## 3. Qué falta para cerrar el encargo

En orden de bloqueo:

1. Revisión visual de los 113 candidatos HU y de los 65 no candidatos de dataset6
   (el umbral no prueba ausencia). Es el cuello de botella; para eso se construyó el
   agente `clasificador-metal`.
2. Resolver los 6 grupos de duplicados e imponer identidad por paciente.
3. Recién entonces, `explorar.py resumen` produce conteos de metal y cohortes reales.
4. Aparte, decidir con el asesor si el entregable cubre los 7 sub-datasets o solo
   CLINIC y CLINIC-metal.

## 3-bis. Ejecutado el 2026-09-07

Doce agentes cubrieron los 113 candidatos: `propuesta_clasificacion.csv`, 113 filas,
todas `propuesta sin validar`. Eso mueve la sub-tarea «mostrar ejemplos» de parcial a
cubierta y da material para «qué dataset contiene metal», pero **no** cambia el conteo
de metal confirmado ni desbloquea el split: hace falta tu validación, resolver los
duplicados y fijar identidad por paciente. Implicancias #19-22.

## 4. Agente `clasificador-metal`

Construido y ya ejecutado sobre los 113 candidatos. Definición en
`.claude/agents/clasificador-metal.md`; insumo visual en `laminas.py`.

`python experiments/exploration-3d/laminas.py <caso>` escribe en
`outputs/laminas/<caso>/`: `proyecciones.png` (MIP en tres ejes en ventana de metal,
más el acumulado de vóxeles sobre umbral), `ortogonales.png` (los tres planos por el
centroide del umbral, en ventana de hueso y de metal, con el umbral superpuesto),
`axiales.png` (16 axiales que cubren la extensión del umbral) y `hallazgos.json`
(componentes conexos con vóxeles, volumen mm³, HU máximo, centroide, bbox en mm,
rango de cortes axiales, lado geométrico por el signo de x en RAS y si tocan el borde
del FOV). Determinista y sin GUI; `--hu` y `--min` son configurables.

El agente lee esas láminas y propone filas en `propuesta_clasificacion.csv`, que ya
existe con su cabecera. **No escribe en `revision.csv`**: la validación la hace la
autora y recién entonces la fila pasa al CSV de revisión. El agente tiene prohibido
escribir `completa`, proponer cohortes, afirmar ausencia de objetos a partir de 16
cortes, e inventar material, modelo o lateralidad clínica. Ante duda, `incierto`.

Verificado en `dataset7_CLINIC_metal_0003_data`: 40 111 vóxeles sobre 2500 HU
repartidos en varios componentes conexos, con estriado visible en los axiales. Ese
recuento de componentes **no** es un recuento de implantes: el artefacto fusiona
piezas vecinas y parte otras.
