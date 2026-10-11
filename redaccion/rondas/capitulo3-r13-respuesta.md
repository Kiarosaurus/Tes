# Respuesta del redactor — capitulo3 — r13 (ultima ronda del ciclo)

Modo `corregir`. Archivo editado: `overleaf/secciones/capitulo3.tex` (CRLF conservado). Lint final:
`PASA` (alta 0, media 0, baja 14, todas E-P1 de cifras propias con fuente en el inventario de trazabilidad).
GAP del capitulo: lit 2 / dato 13 / dec 16 (sin cambio en totales: un `\GAPDEC` se cierra y otro se abre).
E13 de r10 sigue RECHAZADO y E8 de r12 ("sin osteosintesis") se mantiene; ninguno se reabre.
Ninguna cifra de la corrida final en prueba; #158 sigue ABIERTA y conserva su `\GAPDEC` y su `\GAPLIT`.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T02 | trazabilidad | ESCALADO | l. 208: ya no se califica el estado metalico de los no receptores; la prosa solo dice "las otras pelvis de validacion sin osteosintesis no alcanzan ese criterio", cierto con cualquiera de las dos fuentes. `\GAPDEC` con la pregunta: el paciente con objeto en el borde del campo de vision (`CLINIC_0066`) es "sin metal" (DEC 2026-09-21 (2), IMP #105) o grupo 2 (`grupos.csv`:67, `ts_nivel_s1.csv`). No se elige fuente |
| T01 | trazabilidad | APLICADO | l. 208: "las dos pelvis de validacion sin osteosintesis cuyo corredor es viable con el criterio de SAP, $D \geq 9$ mm". DEC 2026-10-09 (4) pto 4 ("corredor viable"); `e9ts_corredor.csv` (default6mm, F = 0.001): 10.6 y 12.4 mm frente a 7.0, 8.9 y 1.6 mm. El `\GAPDEC` "descarte no consta" se retira. l. 322: "los unicos de validacion sin osteosintesis con corredor viable"; el de 1.6 mm queda como el mas estrecho de los excluidos. l. 380: "solo en receptores con corredor viable" |
| guia-1 | guia | APLICADO | l. 358 (parrafo nuevo del Obj 3): tres decisiones mas tras resultados de validacion, cada una con su efecto: segunda corrida de la sonda tras dos errores, sin cambiar criterios (`sonda_peters.md`:133; DEC 2026-10-09 (2) pto 1), que dio una segunda oportunidad a la regla del contraste primario; cortes de solo banda (#160, DEC 2026-10-09 (4) pto 1), que suben la amplitud y se decidieron antes de calcularla (#160: "elegir antes de correr `a15_delta.sbatch`"); abandono de 30 000 pasos y eleccion por cotejo (DEC 2026-10-05 (6) pto 1, medido en 5 pacientes de validacion; DEC 2026-10-09 (2) pto 2). Cierre: ninguna uso pacientes de prueba |
| guia-2 | guia | APLICADO | l. 380: el efecto de la cremallera sobre el anillo de 12-15 mm o sobre $s_{\mathrm{sem}}$, y su sentido sobre el margen, "no esta medido". Ninguna fuente lo registra (busqueda de "cremallera"/"zipper" en DEC, IMP y `experiments/objetivo3/*.md`). Sin GAP nuevo: se declara como limitacion |
| guia-3 | guia | APLICADO | l. 38: "antes de procesar ningun paciente de prueba con el sintetizador o con el protocolo fisico", mas una oracion que remite a amenazas por la regla de realismo, que si uso informacion de inclusion de prueba. Mismo cambio cubre E10 y T03 |
| E10 | estilo | APLICADO | Ver guia-3. No se usa "generar ningun caso": la compuerta del Obj 1 ya proceso pacientes de prueba con el autoencoder, y "procesar con el sintetizador o el protocolo fisico" es lo que sostiene DEC 2026-10-09 (3) pto 3 y (6) |
| E1 | estilo | APLICADO | l. 198 queda con la definicion de punto de control y remite al cotejo; los 60 000 pasos pasan a l. 206 junto a los 144 500. El resultado (37 500) solo se da en l. 206 como candidato y en l. 216 como elegido |
| E2 | estilo | APLICADO | l. 204: "un punto de control distinto del evaluado" (fuente: `a10_costura.py` docstring, #139: `ckpt` de `run01`) |
| E3 | estilo | APLICADO | l. 204: "Su medida es el salto ... y el diseno congelado solo la toma en la reconstruccion de implantes reales" |
| E4 | estilo | APLICADO | l. 250: "Que estrecha esos corredores no esta establecido, y la fractura es su confundidor (Seccion amenazas)". Las cifras y la conclusion quedan solo en l. 356 |
| E5 | estilo | APLICADO | l. 286: "La evaluacion del Objetivo 3 ordena tres contrastes: dos sobre la *streak amplitude* y uno, el de realismo, sobre los estadisticos que no exigen una imagen sin metal" |
| E6 | estilo | APLICADO | l. 302: "Esa tolerancia de $\pm 20$ HU se fija en el 2 %" |
| E7 | estilo | APLICADO | l. 370: "una sola ejecucion local del protocolo fisico, la de la verificacion de reproduccion". Fuente: IMP AMPLIACION a #141 y #146 (2026-10-05), "Primera corrida del brazo fisico en local", imagen del repositorio con titanio; no es la sonda. Cubre guia-4 |
| E8 | estilo | APLICADO | l. 358 partido en dos parrafos: Obj 1 y Obj 3 |
| E9 | estilo | APLICADO | l. 360: "El sentido del efecto esta registrado para dos de las tres elecciones" |

Bajos aplicados: guia-4 (con E7); guia-5 (l. 276: definicion del salto, diferencia absoluta de medianas de dos
cascaras de un voxel a cada lado del borde, medida igual en la TC real; fuente `a10_costura.py`, docstring
"DEFINICION, la misma de #139"); guia-6 (l. 326: el histograma entra en la comparacion y el diseno congelado no le
fija resumen por paciente; `diseno_A.md`:103 solo nombra los estadisticos); T03 (con guia-3); E11, E12, E13, E14,
E15, E16, E17, E18, E19 tal como se proponen. Las 14 bajas E-P1 del lint son cifras propias con fuente en el
inventario de trazabilidad r13; no se tocan.

Arreglos al lado (sin hallazgo): tres oraciones que E16, E17 y la division de l. 206 alargaban sobre 40 palabras, y
dos de las nuevas de guia-1 y T01 (l. 322), se partieron para cumplir E-O1 del lint.

## GAP

- Cerrado: `\GAPDEC` "por que los receptores son esas dos pelvis y no las otras dos ... descarte no consta" (T01).
- Abierto: `\GAPDEC` sobre la clasificacion de `CLINIC_0066` (T02).
- Sin `\GAPLIT` nuevo: `_candidatos.md` no cambia. Totales: 2/13/16 -> 2/13/16.
- `redaccion/MAPA.md` actualizado (fila r12 T02 cerrada; fila r13 T02 nueva).

## Escalados para la autora

1. **`CLINIC_0066`: sin metal o grupo 2.** DEC 2026-09-21 (2) e IMP #105 dicen "no lleva metal"; `grupos.csv`:67
   lo pone en grupo 2 ("objeto no ortopedico presente: borde FOV", `incierto`, `autora-regla`). Pregunta: cual
   manda? Si es grupo 2, la frase de DEC 2026-09-21 (2) ("tres no llevan metal") queda desfasada; si es sin metal,
   `grupos.csv` y los recuentos 37/66 que usa el capitulo (l. 48) tendrian que revisarse.
2. **Sin GAP en el texto, para confirmar:** que "corredor viable" en DEC 2026-10-09 (4) pto 4 es el criterio de
   SAP ($D \geq 9$ mm). El texto lo afirma porque los datos lo cumplen (`e9ts_corredor.csv`); si la autora uso otro
   criterio, hay que retocar l. 208, l. 322 y l. 380.
3. Fuera de esta seccion (guia, G-C4): `introduccion.tex`:48 y :56 y `capitulo1.tex`:122, :128 y :132 quedaron
   desfasados frente al cap. 3. Requiere una pasada `documento`.

## Decisiones de redaccion

- Criterio de seleccion de pacientes: se escribe con el criterio que separa a incluidos de excluidos (aqui,
  "corredor viable con el criterio de SAP, $D \geq 9$ mm"), no con una condicion mas debil ("admite el tornillo").
- Cuando dos fuentes del repositorio clasifican distinto a un caso, la prosa se redacta con una propiedad que valga
  con ambas (aqui "sin osteosintesis") y la discrepancia va a `\GAPDEC` con la pregunta, sin elegir fuente.
- Integridad del congelamiento: se nombra la operacion excluida ("procesar con el sintetizador o con el protocolo
  fisico"), no un verbo general ("tocar"), y la excepcion conocida se declara en la misma oracion o la siguiente.
- La lista de decisiones post hoc de amenazas incluye tambien las correcciones de implementacion hechas tras un
  resultado de validacion (segunda corrida de una sonda, ampliacion de los cortes generados), cada una con su efecto.
- "Ejecucion" para una corrida que no es la sonda ni la corrida final (aqui, la verificacion de reproduccion).
- El resultado de una eleccion se da una vez al describir el procedimiento que lo elige y otra al cerrarlo; la
  definicion del objeto elegido no lo adelanta.
