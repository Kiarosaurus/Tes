# Respuesta del redactor — capitulo3 — r17 (ultima ronda del ciclo)

Entrada: `capitulo3-r17-{lint,guia,estilo,trazabilidad}.md`, las notas del orquestador (1-5) y su actualizacion a mitad
de la tarea: **#172 DECIDIDA, opcion (A)** (`docs/04-implicancias.md` #172, "Decision de la autora (2026-10-11)").
Por esa actualizacion, la nota 1 (pasar a `\GAPDEC`) queda superada: la decision se escribe como hecho y lo que falta
medir va como `\GAPDATO`, sin cifras nuevas. Fuentes que relei: IMP #156, #163 (barrido y "No cubierto"), #164
(correccion del 2026-10-10 en las fuentes), #166, #172; `exclusiones.csv`:13; DEC 2026-10-11 (3) pto 5 y (4);
`experiments/objetivo2/e9ts_corredor.csv` (corredores de validacion); BITACORA §2 2026-09-29.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Igual que T01/T02 con la decision (A). §Sintetizador: la regla de lectura cierra su parrafo; uno nuevo dice que 0.05 se fijo con modelos anteriores, que con el se calcularon el cotejo y $\Delta$ y procesa la corrida final, que la recalibracion dio 0.030 para el elegido y confirmo 0.05 para el estado final, y que se decidio leer cada punto de control con su limite: lo del estado final queda; lo del elegido se rehace con 0.030 (cotejo, margen si sigue ganando, corrida final, reconstruccion de implantes reales); si cambia el ganador, el estado final pasa a ser el modelo evaluado. `\GAPDATO{cotejo del punto de control y margen $\Delta$ rehechos con el limite calibrado de 0.030 para el punto de control elegido}`. L. 212: "despues recalibrado con el modelo evaluado". §Amenazas (tres elecciones): "La eleccion del punto de control y el margen dependen tambien del limite ..., y se rehacen con el limite calibrado del elegido" |
| guia-2 | guia | APLICADO | §Datos, parrafo nuevo: las auditorias no son exhaustivas; las huellas solo ven copias exactas y cortes compartidos, la comparacion de firmas metalicas solo cubre pacientes con metal; quedan sin cubrir los pacientes sin metal y los vinculos sin metal en comun (#163 "No cubierto"); el paciente compartido no podia detectarse por las huellas y lo hallo la autora al revisar los tornillos (#166 Origen). L. 206: "segun las auditorias de identidad de paciente, la regla ... se mantiene". §Amenazas, validez interna, parrafo nuevo con el sentido de un par no detectado: Obj 1 solo un aprobado; Obj 3 "podria favorecer al sintetizador" (#166 pto 2, en condicional); Obj 2 no es fuga pero cuenta dos pacientes |
| S1 | estilo | APLICADO | "Esa fuga, como la del paciente de prueba retirado antes, solo puede favorecer un aprobado". Para que la comparacion se sostenga (T05), l. 52 dice ahora que la variante adaptada se habia ajustado con la adquisicion de entrenamiento (#156, Objetivo 1) |
| S2 | estilo | APLICADO | "cambiaron los recuentos de la primera auditoria" |
| S3 | estilo | APLICADO | L. 52: "regla de un volumen por paciente"; las otras dos ya lo decian |
| S4 | estilo | APLICADO | Las dos oraciones salen de l. 66. La del paciente con tres adquisiciones pasa a l. 54 (ver T04); la de "las demas adquisiciones repetidas" se elimina, porque l. 54 ya da los siete secundarios y la salida de cohortes |
| S5 | estilo | APLICADO | Parrafo partido: la regla cierra en "sus cifras no cambian"; la historia del limite va en parrafo propio (6 oraciones tras fusionar dos) |
| S6 | estilo | APLICADO | Reordenado: "el ancho de cascara del cotejo, el limite de la lectura de HU, despues recalibrado con el modelo evaluado, y la eleccion del punto de control por cotejo y no por la perdida" |
| S7 | estilo | APLICADO | El caracter descriptivo pasa a la 1.a oracion; "Junto con ella se miden"; se elimina "Es un analisis descriptivo..." |
| S8 | estilo | APLICADO | "El protocolo incluye un control ... Se corre sobre los 13 ..., porque la comparacion ... es pareada, y como no depende del sintetizador ya se corrio" |
| S9 | estilo | APLICADO (con guia-4) | "se tomaron siete decisiones, y todas pudieron orientarse por el. Cinco aplican un criterio registrado antes de esa evaluacion." Las cinco con su criterio, en dos oraciones (E-O1); las otras dos siguen como estaban |
| S10 | estilo | APLICADO | La consecuencia "a las tres" va en la oracion de los receptores, partida por E-O1; los tornillos, en la oracion siguiente con "ademas" |
| T01 | traza | APLICADO | Ver guia-1. No queda "en curso" ni "hoy en recalibracion". El valor 0.030 se da como medido y como el adoptado para el elegido porque #172 ya esta DECIDIDA |
| T02 | traza | APLICADO | §Vision general (dentro del `\GAPDATO`): "el cotejo que elige el modelo que pasa a la evaluacion se rehace con el limite de lectura de HU recalibrado". L. 228: "Con esa regla y con la lectura de limite 0.05, la que se rehace, gana...". El 163.8 HU se presenta como leido con 0.05 en §Analisis (dos sitios), Tabla de diseno y §Amenazas; las demas cifras del elegido quedan cubiertas por "Las del elegido que presenta este capitulo se leyeron con 0.05 y se rehacen con 0.030" |
| T03 | traza | SIN ACCION (resuelto en la fuente) | Corregido en la fuente (fila de `a16` en `EXPERIMENTOS.md`, nota 2 del orquestador). El hallazgo pedia no tocar el capitulo |
| T04 | traza | APLICADO | Verificado: #163 (DECIDIDA) "`0054` tiene ademas un clavo femoral" y la autora eligio `0054` como el que cuenta; la correccion del 2026-10-10 en `exclusiones.csv` (registrada dentro de #164) quita el implante femoral del motivo de `0053`; `exclusiones.csv`:13 da `0053` secundario con primario `0054`; `0052` es uno de los siete secundarios (DEC 2026-10-11 (4) pto 1). Se retira el `\GAPDEC`. L. 54: "Uno de ellos es una tercera adquisicion del paciente del parrafo anterior, cuya adquisicion primaria, que sigue en entrenamiento, lleva ademas un clavo femoral" |

Bajos aplicados: guia-3 y S13 (cifra 61.08 HU y su IC fuera del cap. 3: "con 32 pacientes de prueba, el veredicto
negativo no cambia (capitulo de resultados)", segun BITACORA §2 2026-09-29; la cifra queda en
`experiments/objetivo1/p1_sin_0072.md`:20 para el cap. 4), guia-4 (= S9), guia-5 ("3 de los 11 ... que entonces se
contaban con material ortopedico. Dos de ellos pasaron despues a contarse con objetos no ortopedicos, y el recuento del
11 de octubre deja 9"; "En uno de los 3 revisados"), T05 (= S1), S11 (fusion con "Como en la sintesis ..."; partida
despues por E-O1), S12 (en lugar de "el corredor mas estrecho", los tres corredores excluidos: 1.6, 7.0 y 8.9 mm,
`e9ts_corredor.csv`, default6mm, F = 0.001; el `\GAPDEC` del borde del campo de vision dice ahora "cuyo corredor
mide 8.9 mm"), S14, S15 ("estos dos supuestos"), S16, S17 ("la autora los ubica, en su mayoria, fuera del cuerpo").

Lint final: PASA (alta 0, media 0, baja 11 E-P1); compila, 135 paginas. GAP capitulo3: 2 `\GAPLIT`, 14 `\GAPDATO`,
16 `\GAPDEC` (-1 `\GAPDEC` implante femoral; el `\GAPDATO` del limite "en curso" se sustituye por el del cotejo y el
margen rehechos con 0.030).

## Para la autora

1. La cifra de la sensibilidad sin `0072` (61.08 HU, IC 95 % 54.23-68.57, n = 32) ya no esta en el cap. 3. Hay que
   llevarla al cap. 4, junto a la principal.
2. Las cifras del elegido que el capitulo da (12 de 24, 342 HU, 3297/4641 HU, 810 HU, 977/1238 HU, 901-1057 y
   1188-1360 HU, 163.8 HU) se presentan como leidas con 0.05. Cuando exista el cotejo con 0.030, hay que sustituirlas o
   retirarlas. Si cambia el ganador, se reescribe el §Sintetizador (cotejo y sensibilidad) y el sentido de las tres
   elecciones en §Amenazas.

## Decisiones de redaccion

- **Parametro recalibrado con decision tomada:** se dice el valor medido, la regla de aplicacion decidida y el orden
  de lo que se rehace. Lo que falta medir va en `\GAPDATO`, y las cifras ya presentadas se marcan con la lectura con
  que se obtuvieron ("con la lectura de 0.05"), sin retirarlas.
- **Aislamiento verificado por auditoria:** se dice que cubre la auditoria y que no, y en §Amenazas el sentido de un
  par no detectado en cada objetivo.
- **Cifras de veredicto en el cap. 3:** una sensibilidad del veredicto se enuncia sin la cifra ("el veredicto no
  cambia") y remite al capitulo de resultados.
