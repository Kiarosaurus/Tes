# Respuesta del redactor — capitulo3 — r19 (modo corregir + encargo 2026-10-14)

Entradas: `capitulo3-r19-guia.md`, `-estilo.md`, `-trazabilidad.md`, `-lint.md`; `redaccion/ENCARGO_2026-10-14.md`
(V1-V4). Ronda unica del ciclo (tope 1, pedido de la autora). Ningun hallazgo se saco por oscilacion.

Lint final: `python scripts/lint_redaccion.py capitulo3 --compilar` -> **PASA**, alta=0 media=0 baja=22 (todas E-P1,
cifras con fuente en la tabla de abajo o en rondas previas). GAP: lit=2 dato=15 dec=16. Compila, 143 pp., sin
referencias indefinidas. PDF de etapa: `redaccion/.build/etapas/capitulo3-r19.pdf`.

## Hallazgos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 (media) | guia | APLICADO | :38 dice que la corrida final y la reconstruccion de implantes reales se ejecutaron y evaluaron con el diseno preinscrito y remite al cap. de resultados; marca reducida al realismo. :218 "sus resultados se presentan en el capitulo de resultados". :329 sin `\GAPDATO` (ver T03). Sin cifras de veredicto en el cap. 3 (BITACORA §2 2026-09-29, PAT-151) |
| guia-2 (media) | guia | APLICADO | §Amenazas: se quita "siete decisiones"/"Cinco"; se anade la nueva aplicacion de la regla del material a las que aplican criterio previo, y la lectura de que ningun material reproduce lo real y el control de pose a las expuestas, con remision al parrafo siguiente |
| guia-3 (media) | guia | APLICADO | Validez de constructo, parrafo nuevo: la *streak amplitude* adaptada mide la dispersion de las colas y crece con cualquier desviacion extrema; no distingue rayas de textura sin direccion. La observacion de #176 (ABIERTA, inspeccion visual) entra solo dentro de un `\GAPDATO` |
| guia-4 (media) | guia | ESCALADO | Desfase entre `introduccion.tex` (:48 Delta "sin medir", :56 poses del muestreador, :90 "modelo final no elegido") y el cap. 3. Fuera de la seccion y del encargo ("Lo que NO se toca": introduccion). Para la autora: ciclo propio de la introduccion |
| guia-5 (baja) | guia | APLICADO | En `sec:v2`: "modelo evaluado" y "corrida final" siguen designando la v1; la ejecucion de la v2 en prueba se llama "evaluacion exploratoria de la version 2" |
| guia-6 (baja) | guia | APLICADO | Intervenciones nombradas por su funcion ("sobremuestreo", "peso por distancia", "canal de endurecimiento del haz"); modelos "modelo con sobremuestreo" (run05a) y "modelo con canal" (run05b); simbolo del canal $\Gamma_M$ (no usado en el documento); el estadistico `e` de la compuerta se nombra "ganancia neta", sin simbolo |
| guia-7 (baja) | guia | APLICADO | :305 "La evaluacion preinscrita del Objetivo 3 es solo metrica"; en `sec:v2` la comparacion visual a ciegas es "descriptiva y no interviene en ninguna decision" |
| guia-8 (baja) | guia | APLICADO | :210 anade que una medicion propia acota el truncamiento solo para piezas del tamano de un tornillo, no para placas ni protesis, con remision a `sec:v2`; la amenaza de constructo lo repite con su condicion, sin duplicar cifras |
| S1 (media) | estilo | APLICADO | :38 y :222: "del sintetizador y del protocolo fisico"; "El sintetizador y el protocolo fisico habian usado la misma pose equivocada" |
| S2 (media) | estilo | APLICADO | :204 "de la corrida final y de su sensibilidad con el estado final", acotado a la version 1 (T07) |
| S3 (media) | estilo | APLICADO | "tornillo parametrico" en :40, :220 (dos), :222 (dos), :323 y :391. Se conserva "tornillo sintetico" en :15, que nombra lo que devuelve la cadena (BITACORA §2 2026-09-30) |
| S4 (media) | estilo | APLICADO | :327 fundido segun la propuesta: "la respondio de nuevo con la pose corregida el protocolo completo [...]: el artefacto fue medible en todos los cortes simulados" |
| S5 (media) | estilo | APLICADO | :383 "El veredicto de viabilidad de esa segunda corrida se tomo con la pose equivocada" |
| S6 (media) | estilo | APLICADO | :329 sujeto explicito ("El protocolo fisico completo se corre...") y causas separadas; el `\GAPDATO` se retira (T03) |
| S7 (media) | estilo | APLICADO | :335 sin "sin probar que el titanio lo reproduzca" |
| S8 (media) | estilo | APLICADO | ", por tanto," retirado en los cierres de :405 (ahora parrafo de la banda), :407 y :417; se conserva el de "Ninguna de las cifras se transfiere, por tanto," |
| S9 (baja) | estilo | APLICADO | :212 "y, segun las auditorias"; :214 "y un filtro de forma habria descartado"; :226 reescrito con T04, sin "de modo que" |
| S10 (baja) | estilo | APLICADO | :315 "Los tres materiales son"; :349 "Los dos estadisticos son" |
| S11 (baja) | estilo | APLICADO | :220 "detiene" en las dos oraciones |
| S12 (baja) | estilo | APLICADO | :391 dos primeras oraciones fundidas y vueltas a partir: "se decidio despues de que la autora viera generaciones que incluian la particion de prueba [...]. La posicion del implante se midio despues [...]" |
| S13 (baja) | estilo | APLICADO | :40 "La segunda enmienda, del 12 de octubre, corrigio [...]" |
| S14 (baja) | estilo | APLICADO | :335 "No esta establecido si"; :204 "porque no habia una de uso exclusivo disponible" |
| S15 (baja) | estilo | APLICADO | Absorbido por T02: la marca de :38 se reduce al realismo |
| T01 (alta) | trazabilidad | APLICADO | :218, texto propuesto. Fuente: `resultados_prueba_v1.md`:10-40; EXP:92; DEC 2026-10-13 pto 1 |
| T02 (media) | trazabilidad | APLICADO | :38 prosa "ya se ejecutaron y se evaluaron con el diseno preinscrito"; marca `\GAPDATO{evaluacion del contraste de realismo sobre la particion de prueba, que no tiene script}` (`resultados_prueba_v1.md` §Pendiente; #177). MAPA actualizado |
| T03 (media) | trazabilidad | APLICADO | :329 "Ya se corrio con la pose corregida, y su amplitud sobre esos 13 pacientes se evaluo junto con la de la corrida final (capitulo de resultados)"; `\GAPDATO` retirado (MAPA: fila cerrada) |
| T04 (alta) | trazabilidad | APLICADO | :226 "Con el modelo evaluado, ese salto se midio en la reconstruccion de implantes reales (capitulo de resultados). Fuera de ella solo hay una medicion [...] y no estima el salto del modelo evaluado en la sintesis sobre pelvis sin metal." Cifras de E-A1 (6.3 / 9.0 HU) al cap. 4 (PAT-151) |
| T05 (media) | trazabilidad | ESCALADO | #90 sigue ABIERTA (regla 3 de `overleaf/CLAUDE.md`): no se borra la marca. Se reescribe como "cierre formal de la contingencia de plazo [...]: la comparacion ya se ejecuto como contraste primario". Para la autora: cerrar #90 por ejecucion; despues se retira el `\GAPDEC` |
| T06 (alta) | trazabilidad | ESCALADO | Fuentes desfasadas fuera de `overleaf/` (TES :117, :149-156; DAE :29, :32-34; DEC 2026-10-11 (3) ptos 1 y 3; `tesis/main.tex`:79; EXP :83-84, y EXP:41 sigue "NO LANZADO" para run05a; EXP:95 `v2_plan.md` "PLANIFICADO"). No se editan (reglas raiz 3, 4 y 14; regla 6 de `overleaf/CLAUDE.md`). El capitulo usa lo vigente: `resultados_prueba_v1.md`, #177, DEC 2026-10-13, 2026-10-14 y 2026-10-14 (2), `v2_plan.md`, `run05/v2_eleccion.md`, `b_piloto/b_resumen.md`, `d1_d2_resultado.md` |
| T07 (baja) | trazabilidad | APLICADO | :204 acotado a la version 1; :214 "En la version 1, [...]" y "La version 2 tampoco filtra, pero sobremuestrea por tamano"; GPU de la v2 declarada en `sec:v2`; "modelo evaluado" sigue siendo run04 |
| T08 (baja) | trazabilidad | APLICADO | :289 "; su valor se presenta en el capitulo de resultados" (sin la cifra 0.000, PAT-151) |
| lint (14 E-P1, baja) | lint | sin cambio | Cifras con fuente cotejada en el inventario de T; las 8 E-P1 nuevas estan en `sec:v2`, con fuente en la tabla de abajo |

## Encargo 2026-10-14 (V1-V4)

Todo en la subseccion nueva `\subsection{Version 2 del sintetizador}\label{sec:v2}`, al final de §Sintetizador, mas
un parrafo en §Amenazas (validez interna), dos remisiones (:38, :355) y los ajustes de guia-5 a guia-8 y T07.

- **V1 (motivo):** aplicado en los dos primeros parrafos y el tercero. El resultado de prueba de la v1 (#177) entra
  **sin cifras** (no se concluyo equivalencia con Ti, intervalo entero bajo cero, supera la copia y pegado) con remision
  al cap. de resultados, porque las cifras de veredicto van al cap. 4 (BITACORA §2 2026-09-29; PAT-151). Las cifras de
  D1/D2 si entran (son de diagnostico, entrenamiento y validacion). Declaracion obligatoria: "La version 2 se decidio
  despues de ver salidas del modelo evaluado sobre la particion de prueba y ese resultado. Es, por eso, posterior y
  exploratoria, y se reporta junto a la version 1 y nunca en su lugar." Opcion de banda ancha descartada (DEC
  2026-10-13 pto 3).
- **V2 (intervenciones, compuerta, entrenamiento):** aplicado. Canal descrito como "informacion previa (*prior*)
  analitica y aproximada del endurecimiento del haz, y no como un modelo del artefacto ni como un simulador". Limites de
  las fichas (2D paralelo, sin dispersion ni ruido; Teo. 3.5; Xia et al. sobre la parte no local). #178 entra como
  `\GAPDATO`; #181 como medicion (C0, C1, C2) y "efecto moderado" (DEC 2026-10-14 pto 2), sin la lectura
  interpretativa de #181 ("lleva informacion de direccion").
- **V3 (regla y resultado):** aplicado; resultado de #182 como medicion; "no mejora"; run04 sigue como modelo
  principal; limitacion de 2 pacientes y 4 HU ("no se distingue del ruido de esa muestra", DEC 2026-10-14 (2) pto 3).
- **V4 (exploratorio y amenazas):** aplicado en `sec:v2` (declaracion previa a prueba, procedimiento, tres modelos sin
  ganador, comparacion visual a ciegas descriptiva, motivo) con `\GAPDATO` de los resultados, y en §Amenazas (decision
  posterior a ver salidas y resultado de prueba de la v1; evaluacion declarada tras la regla; reuso de la particion con
  dos modelos mas; ninguna cifra de la v2 en prueba como resultado principal).
- **No aplicado (por regla):** #179 (brecha del cap. 2) y #180 (trabajo relacionado del Obj 2), fuera de alcance.

### Fuente de cada cifra nueva

| Cifra (cap. 3, `sec:v2`) | Fuente |
|---|---|
| exceso real 1930 / 1199 / 765 / 473 / 174 HU; 18 pacientes; 500-4000 mm3; referencia a 15-40 mm; ultimo anillo separado del nulo 8-10 mm | `experiments/objetivo3/d1_d2_resultado.md` §D1 (tabla y linea "hasta 10 mm") |
| sintetico run04 1697 / 488 / 97 / -65 / -40 HU; validacion 0101/0102, 5 semillas, referencia exacta | `d1_d2_resultado.md` §D2; `run05/v2_eleccion.md` |
| 2888 de 14 182 parches; 0.2036; 45 componentes; 24 casos; 0.5; 3.91; peso 3; anillo 2-10 mm; 896 / 3 | `v2_plan.md` §1 D-a, D-b; `run05/run05a_meta.json` (`v2_D`, `datos_val`); DEC 2026-10-14 pto 1 |
| 5 de 40 componentes eran tornillos | `v2_plan.md` §1 D-a (ya en el cap. 3, :214) |
| Ec. del canal; 2D paralelo, sin dispersion ni ruido; rayas solo si no estrictamente convexo; Park et al. lambda fijo | fichas `park2017characterization` (Ec. 1.6/2.10, Sec. 1 p. 3-4, Teo. 3.3/3.5), `park2016MAR` (Ec. 15), `hyung2017ml` (Ec. 15; Sec. III.A p. 4), `xia2024pndnet` (Sec. II p. 2127), `wang2021streak` (Sec. 1) |
| lambda 0.0847 por mm; 11.80 mm | `b_piloto/b_resumen.md` §C2; `v2_plan.md` "Resultado de la compuerta" |
| C0 0.0067 / 0.0902, regla 0.2; C1 1.000 en 228 cortes, regla 0.9; C2 e 0.116, p 0.0085, 13 pacientes con control, d 0.133, rho 0.166; regla p < 0.05 y d >= 0.05; sensibilidades 0.114-0.119 | `b_piloto/b_resumen.md`; `v2_plan.md` "Compuerta de B"; DEC 2026-10-14 pto 2 |
| 60 000 pasos; minimo en 21 000; 0.0597 y 0.0596 | `run05/run05a_curva.csv` y `run05b_curva.csv` (`perdida_val` minima; calculado como minimo de columna, no recalculado) |
| run04 0.0540 en 16 500 | #168 "Evidencia textual (log)": "MEJOR VALIDACION: 0.05403 en el paso 16500"; EXP:35 (paso) |
| GPU: run05a en porcion compartida, ultimo tramo en tarjeta del tipo de run04; run05b entero en porcion exclusiva; run04 en otro tipo | `docs/ESTADO.md` (run05a: shard `a100_3g`, tramo final `rtxa6000`; run05b: MIG `a100_3g` exclusiva, jobs 56721-56724); #168 (run04 en `shard:rtxa6000`) |
| E 532.8 / 418.2 / 367.0; dev 0-2 233.0 / 284 / 540; tope 279.6; 4 HU; cotejo 13 / 13 / 9 | `run05/v2_eleccion.md`; #182; DEC 2026-10-14 (2) pto 1 |
| salvaguarda 20 %; reemplazo 10 %; orden de simplicidad; 13 pacientes, 5 semillas | `v2_plan.md` "Regla de eleccion"; DEC 2026-10-14 pto 3; DEC 2026-10-14 (2) pto 2 |

### GAP nuevos para la tabla de `redaccion/MAPA.md` (ya anotados)

| Marca | Que falta | Origen |
|---|---|---|
| `\GAPDATO` | Evaluacion del contraste de realismo sobre la particion de prueba, que no tiene script (§Vision general; sustituye a la marca de "todo resultado del Obj 3") | guia-1, T02; #177 |
| `\GAPDATO` | Resultados de la evaluacion exploratoria de la version 2 sobre la particion de prueba (generaciones en curso) | encargo V4; DEC 2026-10-14 (2) |
| `\GAPDATO` | Efecto del canal en cortes con seccion de tornillo estrictamente convexa, que la compuerta no separa | encargo V2; #178, #181 |
| `\GAPDATO` | Medicion de la estructura direccional del artefacto sintetico dentro de `G` (solo hay inspeccion visual, #176) | guia-3; #176 |
| cerrado | `\GAPDATO` de la amplitud del protocolo fisico sobre los 13 de prueba | T03 |
| reformulado | `\GAPDEC` #90 (contingencia de plazo) | T05 |

Balance: `\GAPDATO` 13 -> 15 (-2 retirados, +4 nuevos, contando la reformulada de :38 como nueva); `\GAPLIT` 2 y
`\GAPDEC` 16 sin cambio. Sin `\GAPLIT` nuevo: nada que anadir a `_candidatos.md`.

## Para la autora (escalados)

1. **T06:** actualizar fuentes de contenido desfasadas: `docs/00-tesis.md` :117 y :149-156; ENMIENDA de
   `experiments/objetivo3/diseno_A.md` :29 y :32-34; DEC 2026-10-11 (3) ptos 1 y 3 (o cerrar #175); `tesis/main.tex`:79;
   `EXPERIMENTOS.md` :83-84 (a CORRIDO / EVALUADO con remision a `resultados_prueba_v1.md`), :41 (run05a ya corrido) y
   :95 (`v2_plan.md` ya no es solo PLANIFICADO).
2. **T05:** cerrar #90 por ejecucion; despues se retira el `\GAPDEC` de §Analisis estadistico.
3. **guia-4:** actualizar `introduccion.tex` en su propio ciclo (Delta medido, evaluacion sobre el eje sin perturbar,
   modelo elegido; ahora tambien la version 2 exploratoria).
4. **Opcional:** el encargo V1 lista cifras del resultado de prueba de la v1; se dejaron fuera del cap. 3 (van al cap.
   4). Si la autora las quiere en el cap. 3, basta con anadir la diferencia media y su IC90 en la segunda oracion de
   `sec:v2`.

## Decisiones de redaccion

- Version 2: "modelo evaluado" y "corrida final" quedan para la version 1; run05a = "modelo con sobremuestreo", run05b
  = "modelo con canal"; su ejecucion en prueba = "evaluacion exploratoria de la version 2". Las intervenciones se
  nombran por su funcion ("sobremuestreo", "peso por distancia", "canal de endurecimiento del haz") y nunca "D" / "B";
  el canal es $\Gamma_M$ y el estadistico de su compuerta, "ganancia neta" (sin simbolo), para no chocar con $D$, $B_{\delta}$, $T$.
- "Prior" se escribe "informacion previa (*prior*)" la primera vez; el canal se describe como informacion previa
  analitica y aproximada, no como modelo del artefacto ni simulador.
- Resultado de prueba de una version ya evaluada usado como motivo en el cap. 3: solo su sentido (que se concluyo o no
  y hacia donde), sin cifras, con remision al capitulo de resultados (extiende PAT-151).
- Tres articulos con el mismo primer autor (Park): se distinguen por la lista de autores cuando son tres ("Park, Choi y
  Seo", "Park, Hwang y Seo") y por "Park et al." cuando son mas.
- "Exceso de amplitud" = amplitud de colas (5 % alto menos 5 % bajo) en el anillo menos la de una referencia sin
  metal; se define en negrita en `sec:v2` y se reutiliza con ese nombre.
