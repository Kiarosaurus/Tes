# 05 — Bitacora de sesiones con el asesor

> Una entrada por reunion. La autora anota la tarea encargada;
> Claude completa "que se hizo" e "implicancias" al cerrar la tarea.

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
