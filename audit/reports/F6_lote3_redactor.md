# F6 lote 3 — Reporte del redactor (modo corregir)

Archivos editados: `overleaf/secciones/capitulo3.tex` (solo `sec:datos`) y `overleaf/secciones/capitulo4.tex` (solo tres oraciones). Los saltos de linea se conservaron tal cual estaban: capitulo4 sigue en CRLF (268 CR, sin cambio) y capitulo3 estaba y sigue en LF puro (0 CR). Se hicieron copias previas en el scratchpad de la sesion.

## (a) Que se aplico y que no

Aplicado:
- **Tabla `tab:flujo-cohortes`** (B-033/B-034/A-021, meta 1). Tres columnas (etapa y corte, unidad, recuento), ancho 0.86 de `\linewidth` (menos que las otras tablas del cap. 3, que usan 0.90), sin `Overfull` en el log. Se coloco tras el parrafo de recuento vigente. Se referencia con `\ref` desde cuatro puntos: l.44 (inventario), l.56 (valores vigentes), l.62 (recuentos vigentes) y l.86 (embudo del Objetivo 2).
- **Aclaracion 178/179** (meta 2), en una frase: «una mas que los 178 volumenes, porque dos campos de vision solapados del mismo estudio se unen sin interpolar en una unidad adicional». Ver (e).
- **Compresion de la prosa que narraba recuentos** (meta 3):
  - l.44: se quitaron 103/75 (pasan a la tabla).
  - l.50: se quitaron 65/37/66, y 10 y 1 unidades; se anadio la frase sobre el 179. Se partio en dos la oracion de los tres grupos para que no pase de 40 palabras.
  - l.52: se quito «8 casos» de validacion.
  - l.62: se redujo a una referencia a la tabla mas la explicacion de por que el registro de grupos suma 166 y no 159. Se quitaron todas las demas cifras del parrafo.
  - l.64: se quitaron 103/91/72/49. Se dividio la oracion larga en tres (la comparacion de nivel, la segunda situacion de exclusion y el efecto por grupo).
  - l.66: el detalle «10 de 15 corredores estrechos y 10 de 15 controles» pasa a «10 de 15 en cada uno». Se conserva 20 de 30 (67 %), el caso dudoso y la limitacion de cribado de un medico sin especialidad.
  - l.68: solo se cambio el sujeto personal; se conservan 18/12/7/5 (ver (c)).
- **Voz impersonal en los parrafos editados**: «La autora reviso... y anoto...» (l.48) pasa a «Se revisaron... y se anotaron...»; «lo hallo la autora» (l.60) pasa a «se hallo al revisar los tornillos»; «El lector juzgo... que abrio» (l.68) pasa a «Se juzgaron... que se abrio»; «La revision en cortes de la autora lo confirma» (l.70) pasa a «La revision en cortes lo confirma».
- **Parte B (capitulo4)**:
  - Nota de tabla (l.76): «La distancia entre las dos series se calcula con la Ecuacion~\eqref{eq:w1}.».
  - l.260: «Se juzgo insuficiente el resultado visual del modelo evaluado y se decidio, con el asesor, no redisenar ni reentrenar el sintetizador». Se conserva quien participo en la decision (el asesor).
  - l.264: «Se decidio mantener la envolvente y las cifras del Objetivo~2 (Seccion~\ref{sec:amenazas}).».

No aplicado, con razon:
- No se movio ningun parrafo a anexo (B-033 y B-034 lo proponen) porque la orden pedia solo tabla y compresion, y trasladar mecanica de auditoria cambia la estructura. No se hicieron las figuras F7 (flowchart): la orden pide tabla.
- No se redujo mas la prosa porque lo que quedaba es contenido protegido por la orden: regla de aislamiento, paciente compartido y su efecto (l.54, 56, 58), caracter no exhaustivo (l.60), reglas de seleccion y control de nivel, cribado de fractura y funciones del material ortopedico. La meta de -500 palabras de B-033/B-034 no es alcanzable sin tocar eso (ver (b)).
- Los parrafos de l.46, 54, 58 y 60 (salvo el sujeto personal) no se tocaron: no tienen recuentos que la tabla absorba.

## (b) Palabras (`texcount -brief -inc -q`)

| Unidad | Antes | Despues | Cambio |
|---|---|---|---|
| `sec:datos` (prosa; `texcount` no cuenta el contenido del `tabular`) | 1573 | 1506 | -67 |
| capitulo3, cuerpo | 29560 | 29493 | -67 |
| capitulo4, cuerpo | 4676 | 4672 | -4 |

El ahorro neto de la seccion es de 67 palabras, no de 330 + 170. La tabla absorbe cifras, pero la prosa que las rodeaba era sobre todo contenido protegido, y las oraciones que se partieron para cumplir E-O1 anadieron conectores. La tabla en si tiene unas 110 palabras que `texcount` no cuenta. Si la autora quiere la reduccion de B-033/B-034, hace falta decidir que parrafo se traslada a anexo.

## (c) Cifras que solo quedan en prosa (no estan en la tabla)

- l.44: 1\,184 volumenes de CTPelvic1K (cita).
- l.48: 2500 HU; 56 pacientes de CLINIC-metal; tres planos; tres pacientes (l.70).
- l.52: 34 pacientes de prueba en la particion del Objetivo 1.
- l.54: 34 y 33 de prueba; 2.3 HU.
- l.56 y 62: siete volumenes secundarios; el 166 y el 159 aparecen tambien en la tabla.
- l.64: 11 de 34, 7 de 57 y un paciente mas (la resta 91-72 = 19 = 11 + 7 + 1 no se escribe).
- l.66: 30 casos, 15 y 15, 20 de 30 (67 %), 10 de 15 en cada grupo, un caso dudoso.
- l.68: 18 casos sobre laminas, 12 sobre el volumen, 7 corredores estrechos y 5 controles.
- l.70: cuatro funciones, tres pacientes.

## (d) Cifras de la tabla y linea del texto original (capitulo3 antes de editar)

| Cifra en la tabla | Linea original |
|---|---|
| 178 volumenes; dataset6 103; dataset7 75 | l.44 |
| 168 pacientes; grupo 1: 65; grupo 2: 37; grupo 3: 66 | l.50 |
| 179 unidades; 10 fuera de uso; 1 reservada como par de reproducibilidad | l.50 |
| 166 volumenes en uso; grupo 1: 59; grupo 2: 41; grupo 3: 66 | l.62 |
| 159 pacientes; entrenamiento 118 con 125 volumenes; validacion 8; prueba 33 | l.62 (validacion 8 tambien en l.52) |
| Prueba 33: 20 dataset6, 13 CLINIC-metal; 9 ortopedico, 10 no ortopedicos, 14 sin objeto | l.62 |
| Objetivo 2: 103; 91 con S1 localizado; 72 tras el control de nivel | l.64 |
| Cohorte de sensibilidad 49 | l.64 |
| Fecha de corte «11 de octubre» | l.56 |

Fechas de corte: solo el recuento vigente tiene fecha en el texto (11 de octubre, l.56). El inventario local y la primera auditoria no estan fechados en `sec:datos`; la tabla no inventa fecha para ellos.

## (e) Lo que no se pudo aclarar

- La aclaracion de 179 frente a 178 se apoya en la palabra «adicional» del texto original (l.50: dos campos de vision solapados se unen en «una unidad adicional»). Ademas, `tesis/main.tex` l.136 dice «179 unidades (178 + union)». No se verifico mas alla.
- No se aclaro, porque el texto no lo permite, como se pasa de las 179 unidades (menos 10 fuera de uso y una reservada) a los 168 pacientes de la primera auditoria ni a los 166 volumenes en uso del recuento vigente. En la tabla estan ambas cifras en filas distintas, sin una relacion aritmetica escrita. Tampoco consta si las 179 unidades corresponden a la primera auditoria o al recuento vigente; por eso la fila «Particion» no lleva corte.

## Lint

`python3 scripts/lint_redaccion.py capitulo3 --compilar`: el documento compila (207 paginas), sin citas ni referencias indefinidas. El lint del capitulo marca 8 medias (E-O1) y 50 bajas, ninguna nueva en `sec:datos` tras partir mis dos oraciones largas. Quedan dos bajas preexistentes en `sec:datos` (l.48 y l.54, cifras sin cita en la linea, no tocadas). Las medias restantes estan fuera de `sec:datos`. `capitulo4`: PASA, 0 hallazgos.
