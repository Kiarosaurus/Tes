# 01 — Log de decisiones

> Solo lo escribe la autora. Formato: una entrada por decision, con fecha.
> Tres lineas bastan. Este archivo es la evidencia de que el trabajo avanzo.

## 2026-09-07 — Reglas de lectura de la revisión 3D de los 178 volúmenes

**Decisión:** la clasificación de material de los 178 CT locales se lee así. En `dataset6`,
columna vacía o `nada` significa que no se encontró implante ni material metálico; con
texto, ese texto es el objeto metálico. En `dataset7`, columna vacía significa que **sí**
hay material ortopédico; con texto, hay material ortopédico **y además** lo anotado.
Dictada por la autora tras revisar en 3D los 178 volúmenes y registrada por el asistente
con instrucción explícita el 2026-09-07.

**Alternativas descartadas:** anotar cada fila de `dataset7` repitiendo «material
ortopédico»; y tratar la columna vacía como «sin revisar», que era la lectura del
inventario automático.

**Por qué:** la revisión es exhaustiva y el material ortopédico es la condición por
defecto de CLINIC-metal, así que anotar solo las excepciones es más rápido y menos
propenso a error que repetir lo constante. Aplicada, da 72 de 75 volúmenes de `dataset7`
con material ortopédico y 70 de `dataset6` sin objeto.

---

## 2026-09-07 — Duplicados: prevalece dataset7 y no tiene material ortopédico

**Decisión:** cuando un grupo de duplicados exactos tiene un volumen en `dataset7` y otro
en `dataset6`, prevalece siempre el de `dataset7` como representante, y ese volumen queda
marcado **sin** material ortopédico, porque ningún volumen de `dataset6` lo tiene. Afecta
a tres grupos: `metal_0061` = `CLINIC_0037`, `metal_0036` = `CLINIC_0048`,
`metal_0064` = `CLINIC_0070`.

**Alternativas descartadas:** conservar el volumen de `dataset6`; conservar los dos y
repartirlos entre entrenamiento y prueba, que es fuga directa.

**Por qué:** son el mismo contenido de vóxeles, así que mantener ambos lados pondría el
mismo volumen en entrenamiento y en prueba. Consecuencia: el conjunto de prueba con metal
no son 75 volúmenes sino 72, y 69 de contenido único. **Queda pendiente** elegir
representante en los tres grupos duplicados internos de `dataset7`
(`0012`/`0021`, `0013`/`0043`, `0046`/`0074`), que esta decisión no cubre.

---

## 2026-09-07 — Prioridad de la revisión 3D sobre la propuesta del agente

**Decisión:** si la autora anotó «sin objeto» y el agente `clasificador-metal` quedó en
`incierto`, manda «sin objeto». Caso resuelto por esta regla: `dataset6_CLINIC_0074_data`,
donde hay una estructura en lazo evidente que **no es metal ni material ortopédico** y por
eso no se anota como objeto. Los desacuerdos por borde del campo de visión
(`CLINIC_0039`, `0058`, `0066`, `0077`) se cierran igual. Confirmado también que
`metal_0059` y `metal_0071` **no son el mismo paciente**, pese a compartir spacing y
HU mínimo.

**Alternativas descartadas:** escalar cada `incierto` del agente a una segunda revisión;
dejar esas filas bloqueadas fuera de toda cohorte.

**Por qué:** el agente no certifica, propone; su `incierto` es ausencia de evidencia en
16 cortes, no evidencia de presencia. La revisión 3D de la autora es la fuente válida.
Los textos preliminares del asistente anterior en `metal_0002` y `metal_0003` se borraron
por la misma razón.

---

## 2026-09-07 — Adopción del protocolo híbrido de Peters

**Decisión:** adoptar `peters2025hybrid` como protocolo del brazo físico de comparación. Decisión comunicada el 2026-09-06 y registrada por el asistente con autorización explícita de la autora el 2026-09-07.

**Alternativa descartada:** una reimplementación independiente de XCIST cuya validación de artefactos metálicos se atribuya a `wu2022xcist`.

**Por qué:** Peters aporta el protocolo específico de simulación y evaluación de artefactos; Wu describe el toolkit y sus limitaciones. La adopción no valida automáticamente la adaptación de MAR 2D a síntesis pélvica 3D: siguen pendientes configuración, controles y métricas (#16–17).

## 2026-09-07 — Prioridad bibliográfica tras adoptar Peters

**Decisión:** `peters2025hybrid` permanece en N1 como protocolo adoptado; `wu2022xcist` pasa de N1 a N2 como fundamento técnico y fuente de limitaciones del simulador. Se incorpora N4 para descartes sin uso vigente, con motivo explícito.

**Alternativas descartadas:** bajar Peters por haber elegido su protocolo; descartar Wu por no validar metal; equiparar descarte de un rol con descarte de todo el paper.

**Por qué:** el nivel mide riesgo sobre el argumento y el benchmark. Peters concentra ahora esa dependencia. Wu todavía exige discusión metodológica, por lo que no es una cita de apoyo N3 ni un descarte N4. Esta recategorización responde al encargo de la autora en este turno.

---

## AAAA-MM-DD — Separacion en muestreador y renderizador

**Decision:** el pipeline se divide en dos componentes evaluados por separado.

**Alternativas descartadas:** un solo modelo end-to-end que coloque y renderice.

**Por que:** permite atribuir el error a geometria o a apariencia, y hace que el
muestreador sea defendible como contribucion independiente.

---
