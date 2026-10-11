# Respuesta del redactor — capitulo3 — r11

Modo `corregir`. Archivo editado: `overleaf/secciones/capitulo3.tex` (CRLF conservado). Lint final:
`PASA` (alta 0, media 0, baja 15, todas E-P1 de cifras propias con fuente en el inventario de trazabilidad).
GAP del capitulo: lit 2 / dato 13 / dec 12 (antes 2/13/9). E13 de r10 sigue RECHAZADO (BITACORA §2) y no se reabre.
Ninguna cifra de la corrida final en prueba; #158 sigue ABIERTA y conserva su `\GAPDEC`.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 | trazabilidad | ESCALADO | El texto ya no promete RMSE/SSIM: describe lo congelado (fuera de `G` la preservacion es exacta por construccion en el sintetizador; en el protocolo fisico el diseno congelado solo tiene la simulacion sin metal) y abre `\GAPDEC` sobre la medicion de preservacion del boceto (`tesis/main.tex`:102) que `diseno_A.md` §0 y `a19`/`a20`/`a23`/`a24` no contienen. Region: "fuera de $G$". BITACORA §2 2026-09-29 (decision y codigo difieren). Resuelve tambien E26 |
| T02 | trazabilidad | APLICADO | En l. 52, tras la fusion de `0053`/`0054`: "los pacientes pasan de 168 a 167, y los del grupo 1, de 65 a 64" (IMP #156; `grupos.csv`: 167 grupos de paciente, 64 con grupo 1). l. 48 queda como recuento previo a esa revision y el puente evita el salto a "Los 64" de l. 60. `docs/02-datos.md`:120-137 no se toca (listado para la autora) |
| T03 | trazabilidad | APLICADO | l. 350 sin recuento cerrado y con la escala de lectura de W1; l. 354 con el percentil 5 de la regla del suelo (decidido sobre entrenamiento y validacion, l. 188), "ninguna de esas tres decisiones uso pacientes de prueba" |
| guia-1 | guia | APLICADO | Igual que T03 |
| guia-2 | guia | APLICADO | Sin regla escrita en DEC ni en `diseno_A.md` §0: DEC 2026-10-09 (4) pto 4 excluye `0019` por corredor de 1.6 mm y DEC 2026-10-09 (8) pto 4 mantiene en prueba los tres corredores angostos. No se inventa regla: se declara en validez de la conclusion que $\Delta$ se midio solo en receptores cuyo corredor admite el tornillo, que el diseno no da una regla comun y que solo la sensibilidad n = 10 comparte esa condicion |
| guia-3 | guia | APLICADO | l. 214: "el mayor rango entre semillas de su perfil radial, sobre cascaras y receptores, es de 324 HU, frente a 162 HU" (`a17_cotejo.py`:156-168, `max_rango_semillas_HU`; `a17_cotejo_resultado.md`:44-47). Se distingue asi de $s_{\mathrm{sem}}$ |
| E1 | estilo | APLICADO | Definicion de **diseno congelado** y **corrida final** en l. 38 (DEC 2026-10-09 (6); `diseno_A.md` §0: ningun script toca prueba sin `--corrida-final`). l. 328 remite a `sec:vision` |
| E2 | estilo | APLICADO | "Punto de control" sale de l. 38 ("el modelo que pasa a la evaluacion") y se define en l. 198; l. 206 sin negrita |
| E3 | estilo | APLICADO | l. 212 (dos usos), l. 222, l. 276 y l. 306 sin "referencia" para lo que no es referencia clinica ni de realismo |
| E4 | estilo | APLICADO | l. 268 "se mantienen"; l. 324 "queda fuera de la referencia de realismo" |
| E5 | estilo | APLICADO | Quitados "y eso tambien se reporta" (l. 214) y "Se reportan los resultados con los dos materiales" (l. 308) |
| E6 | estilo | APLICADO | l. 258: "en la Seccion `sec:ap-reconstruccion`, una vez presentadas las dos evaluaciones". Resuelve guia-10 |
| E7 | estilo | APLICADO | l. 268 en una oracion; el `\GAPDEC` se conserva |
| E8 | estilo | APLICADO | "Es un analisis descriptivo que no entra en ninguna decision del Objetivo 3" sustituye a "Todas son descriptivas" en l. 274; borrada la ultima oracion de l. 276 |
| E9 | estilo | APLICADO | Igual que T03 |
| E10 | estilo | APLICADO | l. 364 ya no presenta la regla del suelo como operativa: se evalua contra el primario, no fija como expresar la perdida en HU (remite a l. 188); el sesgo se describe por su sentido en los dos contrastes (DEC 2026-10-08 A.12). Resuelve T04 |
| E11 | estilo | APLICADO | Sin "apenas/mucho mas/muy inferiores": solo el orden. Las cifras de #141 no se usan porque la implicancia esta ABIERTA |
| E12 | estilo | APLICADO | l. 206, 208 y 218 abren afirmando |
| E13 | estilo | APLICADO | Las dos oraciones de uso de la particion por objetivo pasan al final de l. 50 |
| E14 | estilo | APLICADO | Cohorte del protocolo fisico, control sin metal y su `\GAPDATO` pasan al final del parrafo del protocolo completo (l. 306) |
| E15 | estilo | APLICADO | "...sobre un caso, un corte y un punto de control pasado de su optimo, de modo que no estima el del modelo evaluado". "Sin converger" se cambio por "pasado de su optimo", que es lo que dice IMP #139 |

## Bajos

Aplicados: guia-4 (con E3), guia-5 (`\ref` a `sec:ap-sintesis` en l. 204), guia-6 (el primer entrenamiento corrio 144 500 pasos
con la misma semilla y los mismos datos; `docs/ESTADO.md`:383-388), guia-7 y E17 (arandela y canulacion solo para variantes
no programadas), guia-8 (`\GAPDEC` del supuesto distribucional del IC con *t*: ninguna fuente lo enuncia; `a24_contrastes.py`
y `diseno_A.md` §0 no lo mencionan), guia-9 (`\GAPDEC`: DEC D4 pto 2 preve tamano de efecto e IC, pero §0 y `a24` solo
calculan el valor p; mismo tratamiento que T01), guia-10 (con E6), guia-11 (soportes de cortes distintos en el par, declarado
en validez de la conclusion; DEC 2026-10-09 (4) y `diseno_A.md` §0 "cada brazo se mide en sus cortes producidos"), E16, E18,
E19, E20, E21, E22, E23, E24, E25, E26 (con T01), E27, T04 (con E10), T05 ("solo difieren en la realizacion del ruido del
simulador, que no admite semilla fija"; `a19_peters_completo.py`:15-16), T06 ("el centro de la meseta de esa curva en las dos
corridas"; DEC 2026-10-05 (2)).

Cambio colateral: al aplicar E-O1 (lint) se partieron siete oraciones de mas de 40 palabras que mis correcciones habian creado
(l. 206, 208, 302, 306, 318, 376).

## Escalados para la autora (con pregunta)

1. **T01, preservacion fuera de `G` en el protocolo fisico.** El boceto (`tesis/main.tex`:102) mide RMSE y SSIM sobre el
   complemento de $B_{\delta}$; `diseno_A.md` §7 decia "fuera de `G`"; el diseno congelado y su codigo no la miden. Pregunta:
   ¿se anade esa medicion (y sobre que region) como enmienda antes de evaluar, o se retira del boceto y queda solo el control
   sin metal?
2. **guia-9, tamano de efecto del Wilcoxon de cordura.** DEC D4 pto 2 lo promete y `a24_contrastes.py` no lo calcula.
   Pregunta: ¿se reporta (con que medida e IC) o se retira la promesa?
3. **guia-8, supuesto del IC con *t* (n = 13).** Ninguna fuente lo enuncia. Pregunta: ¿se declara el supuesto como
   limitacion, se comprueba sobre las diferencias, o se cambia el IC?
4. **Fuera de la seccion (no es GAP):** `docs/02-datos.md`:120-137 sigue en 168 pacientes / grupo 1 = 65 /
   reproducibilidad = 1, previo a #156; `grupos.csv` da 167 / 64 y dos unidades marcadas `reproducibilidad`. Actualizarlo es
   de la autora (regla de no tocar `docs/`).

## GAP

- Nuevos `\GAPDEC` (3): preservacion RMSE/SSIM del protocolo fisico (T01); tamano de efecto del Wilcoxon (guia-9);
  supuesto distribucional del IC con *t* (guia-8). Anotados en `redaccion/MAPA.md`.
- Sin `\GAPLIT` nuevo: `_candidatos.md` no cambia. Sin GAP cerrados.
- Totales (lint): 2/13/9 -> 2/13/12 (lit/dato/dec).

## Decisiones de redaccion

- "**Diseno congelado**" y "**corrida final**" se definen en la vision general del capitulo 3 (`sec:vision`) y las demas
  secciones remiten ahi; "corrida final" = la unica que procesa la particion de prueba.
- "**Punto de control**" (*checkpoint*) se define en el parrafo de los pares de entrenamiento (`sec:sintetizador`); antes de
  esa definicion se dice "el modelo que pasa a la evaluacion".
- El rango entre semillas del cotejo se nombra siempre "rango entre semillas del perfil radial"; $s_{\mathrm{sem}}$ queda
  solo para la *streak amplitude*.
- Las replicas A y B del protocolo fisico "solo difieren en la realizacion del ruido del simulador, que no admite semilla
  fija" (no "salvo la semilla").
- Una promesa de DEC anterior al congelamiento que el diseno congelado y su codigo no recogen (RMSE/SSIM, tamano de efecto)
  se trata como la cabeza de `M`: se describe lo congelado y la promesa va a `\GAPDEC` (extension de BITACORA §2 2026-09-29).
- En amenazas, las decisiones posteriores a ver datos se listan sin recuento cerrado.
