# 05 — Bitacora de sesiones con el asesor

> Una entrada por reunion. La autora anota la tarea encargada;
> Claude completa "que se hizo" e "implicancias" al cerrar la tarea.

## 2026-09-07 — revision 3D de la autora y fusion

**Que se hizo:** la autora reviso en 3D los 178 volumenes y anoto tipo y cantidad.
Dicto tres reglas de lectura (dataset6 vacio = sin objeto; dataset7 vacio = con material
ortopedico; en duplicados cruzados prevalece dataset7 y ese volumen no tiene material
ortopedico). Se aplicaron a las 178 filas y se les sumo la investigacion de los agentes.

**Resultado:** dataset7 con material ortopedico 72 de 75, 69 de contenido unico.
dataset6 con objeto 33 de 103, de ellos 27 solo extracorporeo y 6 con DIU. Candidatos a
entrenamiento limpio: 70, o 97 si `Objeto extraño` se restringe a lo intracorporeo.

**Implicancias:** #20 y #21 resueltas en criterio (falta que la autora las escriba en
`01-decisiones.md`); #22 cuantificada; #19 sigue abierta por `CLINIC_0074`.

**Para la proxima reunion:**
- Preguntas que le llevo:
  - El test con metal son 72 volumenes, no 75. Se usan los 69 de contenido unico?
  - Los objetos extracorporeos producen estrias igual: el entrenamiento exige limpio de
    objeto o limpio de artefacto?
- Lo que quedo pendiente: representante en los 3 grupos duplicados internos de dataset7,
  identidad por paciente, recorrido de cortes y `CLINIC_0074`.

## 2026-09-07 — clasificacion visual asistida de los 113 candidatos

**Que se hizo:** doce agentes `clasificador-metal` en paralelo, 9-10 casos cada uno,
sobre las laminas de los 113 candidatos HU. Salida fusionada en
`experiments/exploration-3d/propuesta_clasificacion.csv` (113 filas, cero perdidas,
cero duplicadas). Los CSV por lote quedan como trazabilidad. `revision.csv` intacto.

**Resultado:** 65 `si (propuesto)` en `Metal`, 42 `incierto`, 1 `no`, 5 mixtos.
En `Objeto extraño` ningun `no`: 16 axiales no demuestran ausencia. Metal confirmado
sigue en 0 porque ninguna fila esta validada.

**Implicancias detectadas:** #19, #20, #21 y #22. Las cuatro salen de la revision, no
de bibliografia. #20 y #22 bloquean el split; #19 obliga a decidir si se revisan los
178 en vez de los 113.

**Para la proxima reunion:**
- Preguntas que le llevo:
  - Duplicados exactos que cruzan CLINIC y CLINIC-metal: como se reparte eso sin fuga?
  - Si parte de CLINIC-metal no es osteosintesis pelvica, el test del Objetivo 5 se
    define sobre los 75 o sobre un subconjunto confirmado?
  - `Objeto extraño` incluye mesa, ropa y soportes, o solo lo intracorporeo?
- Lo que quedo pendiente: validar las 113 propuestas, decidir #19, resolver duplicados
  e identidad por paciente.

## 2026-09-07 — auditoria del encargo semanal de Victor

**Fecha de la reunion:** no indicada. Esta entrada registra la revision del encargo
transmitido por la autora, no una reunion cuya realizacion se confirme.

**Tarea encargada (la misma del 2026-09-06):** descripcion de datos (datasets,
numero de imagenes por dataset, mediana y rango de voxel spacing y de dimensiones)
e identificacion de metal (que dataset lo contiene, cuantas imagenes, ejemplos, y
definicion de imagenes de entrenamiento sin metal ni objetos extranos y de prueba).

**Que se hizo:** auditoria de `experiments/exploration-3d` contra las ocho sub-tareas,
escrita en `experiments/exploration-3d/cumplimiento-encargo.md`. Se construyo el
subagente `clasificador-metal` (`.claude/agents/clasificador-metal.md`) y su insumo
visual `experiments/exploration-3d/laminas.py`, que genera laminas PNG deterministas
y `hallazgos.json` con componentes conexos medidos. Se creo
`propuesta_clasificacion.csv` con cabecera. El agente quedo construido y NO ejecutado,
tal como pidio la autora.

**Resultado / hallazgo principal:** la descripcion de datos esta cubierta para lo que
hay en disco; la identificacion de metal esta instrumentada pero no ejecutada. Metal
confirmado: 0 de 178, porque ninguna fila alcanza `completa`. Cohortes: 166
`pendiente` y 12 `resolver duplicado`, ningun split. Y el hallazgo nuevo: en disco hay
178 de los 1184 volumenes de CTPelvic1K; faltan los cinco sub-datasets publicos.
Ademas 38 de los 103 CT de `dataset6` superan 2500 HU, asi que ese sub-dataset no es
un conjunto limpio por defecto.

**Implicancias detectadas:** #18 (cobertura de datasets e identificacion inferida de
CLINIC/CLINIC-metal), que ademas cuantifica #15. Sin cambios en #13, #16 ni #17.

**Para la proxima reunion:**
- Preguntas que le llevo:
  - La descripcion de datos debe cubrir los siete sub-datasets de CTPelvic1K o basta
    con CLINIC y CLINIC-metal, que son los descargados?
  - Con 0 mascaras locales y 14 de 75 anotados segun el paper, sobre que se evalua el
    downstream con metal?
  - Acepta una clasificacion visual propuesta por agente y validada por mi, o exige
    revision manual desde cero?
- Lo que quedo pendiente: correr `clasificador-metal` sobre los 113 candidatos HU y
  los 65 no candidatos de `dataset6`, resolver los 6 grupos de duplicados, establecer
  identidad por paciente y recien entonces definir el split.

## 2026-09-07 — seguimiento documental solicitado por la autora

No corresponde a una nueva reunión confirmada. Se registró la adopción de Peters
en `01-decisiones.md` con autorización explícita. Peters permanece N1 como protocolo
adoptado; Wu/XCIST baja de N1 a N2 por su función técnica y de discusión de límites.
Se añadió N4 de descartes, actualmente vacío. Índice y fichas quedaron armonizados.
Impacto: seguimiento de #8 y #17; no hay nueva validación experimental ni cambio del
alcance mínimo. Pendiente: adaptar/validar el protocolo y armonizar `00-tesis.md`.

## 2026-09-06 — preparación del encargo semanal de Víctor

**Cierre de ejecución:** 2026-09-07, America/Lima (la sesión cruzó medianoche).
Inventario sin errores: dataset6 103 CT / 38 candidatos HU; dataset7 75 CT / 75
candidatos HU. Seis grupos de duplicados verificados, 172 contenidos únicos,
cero máscaras locales vinculadas por nombre y tres revisiones visuales parciales.

**Fecha de la reunión original:** no indicada; esta fecha corresponde al registro
del encargo transmitido por la autora, no a una reunión cuya realización se confirme.

**Tarea encargada:** describir datasets, número de imágenes, mediana/rango de
spacing y dimensiones; identificar presencia y cantidad de metal, mostrar ejemplos
y definir imágenes limpias para entrenamiento e imágenes de prueba.

**Qué se hizo:** se preparó `experiments/exploration-3d` con un script para
inventario de NIfTI, vistas 3D por varios umbrales, visor de cortes navegable y
resumen. Un único `revision.csv` reúne estadísticas, duplicados, antecedentes 2D,
elegibilidad y clasificación manual respetando las ocho columnas de la compañera.
Se ejecutó la auditoría de los CT locales; resultados en `resumen.md` y data card.

**Resultado / hallazgo principal:** HU prioriza casos, pero no certifica metal ni
ausencia de objetos. Dataset6 también debe revisarse. Los duplicados y estudios
de un mismo paciente deben resolverse antes de separar cohortes. Se prepararon
ejemplos interactivos y observaciones preliminares; no se dio por terminada la
revisión de ningún volumen ni se inventó un split definitivo.

**Decisión comunicada por la autora:** adoptar `peters2025hybrid`. Se aplicó a
`tesis/main.tex`, con adaptación a síntesis explícita y sin trasladar automáticamente
su validación MAR 2D. Se aclaró la auditoría de cohortes y la premisa de degradación.

**Implicancias detectadas:** #15 (datos/split), #16 (significado de ISC/BFC),
#17 (adaptación y validación del protocolo); #8 aplicada a redacción por autorización.

**Para la próxima reunión:**
- Revisar los ejemplos y confirmar taxonomía de osteosíntesis, prótesis, otros
  implantes y objetos externos; mantener dudas como `incierto`.
- Completar revisión 3D y multiplanar, identidad por paciente, representantes de
  duplicados y disponibilidad de máscaras para downstream.
- Definir métricas propias BFC/ISC separadas de integridad ósea/metálica de Peters.
- Registrar la decisión de Peters en `01-decisiones.md` y armonizar `00-tesis.md`
  (archivos reservados a la autora).

---

## AAAA-MM-DD

**Tarea encargada:**

**Que se hizo:**

**Resultado / hallazgo principal:**

**Implicancias detectadas:** (numeros de entrada en 04-implicancias.md, o "ninguna")

**Para la proxima reunion:**
- Preguntas que le llevo:
- Lo que quedo pendiente:

---
