# Revision guia CS — introduccion — r08

Contexto: encargo `redaccion/ENCARGO_2026-10-15b.md`. Lo que pide a la introduccion: E1, poner en rojo con `\REVVISUAL` el
realismo visual (#193); E2, alinear el texto con DEC 2026-10-15 (3), en concreto la marca de v2 desfasada, el resultado del
Obj. 3 con la lectura del pto 1 y, por cruce, la brecha del pto 9. El texto revisado es el de introduccion-r07: aun no
tiene ningun `\REVVISUAL`, segun grep en `overleaf/secciones`.

Ademas lei, para los cruces: `capitulo2.tex`:102-116, `capitulo3.tex`:38-40, :254-260 y :413-435, `conclusiones.tex`
(sigue siendo esqueleto), DEC 2026-10-15 (1)-(3), `experiments/objetivo3/resultados_dec_2026-10-15.md`, MAPA (filas 137,
140 y 145), #179 y BITACORA §1-§2. `capitulo2` (r08) y `capitulo3` (r24) se corrigen en paralelo, y sus numeros de linea
son los del archivo actual.

Respuesta r07: ningun hallazgo fue RECHAZADO, asi que no hay re-aperturas. Los hallazgos del encabezado (l. 3-21) quedaron
ESCALADOS por #126. Los que siguen vigentes van otra vez con severidad baja (guia-10 y guia-11).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-A3, G-B10 | introduccion.tex:58, :64, :66 | La tension sigue diciendo que "ninguno de los tres enfoques revisados ... produce a la vez" poses y apariencia. DEC 2026-10-15 (3) pto 9 (#179) manda dos cosas. Primero, nombrar la sintesis aprendida de componentes de artefacto como paso intermedio de la MAR no pareada (`lyu2021ududonet` y `xia2024pndnet`, ya en `referencias.bib`). Segundo, acotar la brecha a una sintesis del implante y de su artefacto local, condicionada por la geometria y la pose que propone un muestreador quirurgicamente restringido, y evaluada como producto frente a un protocolo fisico. El cap. 2 aplica el pto 9 en esta ronda (cap2:108 y :114, donde hoy hay un `\GAPDEC` de #179). Si la introduccion no lo aplica tambien, la bisagra se rompe: las dos brechas quedan distintas | En :58, nombrar ese cuarto precedente (la sintesis existe, pero como paso intermedio y sin evaluarse como producto) y reformular la tension con las palabras del pto 9, las mismas que use cap2:108. En :64-66, el aporte debe coincidir con la formulacion final de cap2:114. Coordinar el texto exacto con capitulo2-r08 |
| guia-2 | alta | G-A8, G-A7 | introduccion.tex:50, :52, :60 | Patron PAT-136 reincide. :50 solo da lectura a la no equivalencia ("haría fallar el objetivo"). El desenlace que se obtuvo, no concluyente a la baja, queda sin lectura para el Obj. 3: ni :52 ni :60 ("quedó sin concluir") dicen si el objetivo se cumplio o no. DEC (3) pto 1 lo fija: el Obj. 3 se cumple como objetivo de diseno y evaluacion. La hipotesis de equivalencia no se sostiene: los datos no permiten afirmarla y muestran una amplitud menor. Esa lectura se fijo despues del resultado. Riesgo al aplicarla: si se escribe solo "se cumple como objetivo de diseño y evaluación", el Obj. 3 deja de poder fallar | Despues de :52, una oracion con la lectura del pto 1, marcada como posterior al resultado. Debe separar lo que se cumple (el sintetizador se implemento y se evaluo con el diseno congelado) de lo que podia fallar (la hipotesis de equivalencia, que no se sostiene). En :50, atribuir "haría fallar" a esa hipotesis. Ajustar :60 a la misma formula. Sin cifras nuevas |
| guia-3 | media | OC-2 | introduccion.tex:15, :41, :52, :94, :96 | El encargo E1 no esta aplicado: no hay ningun `\REVVISUAL`. Pasajes que tratan del realismo del artefacto o dependen de el (#193 ABIERTA). :15 es el reclamo "coherencia de la apariencia", que el encargo nombra. :41 es la comparacion con observaciones reales de artefacto. :52 es el contraste de realismo pendiente, con su `\GAPDATO`. :94 trata de la cercania a lo real: el protocolo exagera y el percentil 95 del sintetizador queda por debajo de lo real. :96 es la estructura de raya del artefacto sintetico, que hoy solo sostiene una inspeccion visual (#176) | Envolver cada pasaje en `\REVVISUAL{...}` y dejar los GAP que tengan dentro. No escribir nada de #193 como hecho. Si hace falta una fuente sobre la evaluacion visual de TC sintetica, usar `\GAPLIT` (E3) |
| guia-4 | media | G-A10 | introduccion.tex:52 | Patron PAT-122 reincide (encargo: "marca de v2 desfasada"). El `\GAPDATO{evaluación en prueba de la versión~2}` niega una evaluacion que ya se hizo. Segun `resultados_dec_2026-10-15.md` §Version 2 y DEC (3) pto 5, los dos modelos de v2 se evaluaron en prueba, ambos con desenlace no concluyente a la baja, y se reportan junto a v1 como exploratorios | Retirar la marca. Decir el desenlace sin cifras, con remision al cap. 4 y a `sec:v2`, como manda BITACORA §2 (2026-10-15, capitulo2-r07) para un resultado fuera del cap. 3. Cotejar con cap3:38 ("incompleta"), que capitulo3-r24 tambien corrige |
| guia-5 | media | G-A10 | introduccion.tex:98 | Patron PAT-122 reincide. El `\GAPDATO` sobre el salto de los valores de TC en el borde de $G$, en la sintesis sobre pelvis sin metal, sigue abierto. MAPA (fila 137) lo da CERRADO en el cap. 3 desde r23: se midio en los dos brazos y el texto remite al cap. 4. La fila dice que la introduccion "debe alinearse" | Prosa: "se midió en la síntesis sobre pelvis sin metal para los dos brazos, después de la prueba de la versión 1 (capítulo de resultados)", sin marca. Es el caso D8/costura de BITACORA §2 (2026-10-15, capitulo3-r23) |
| guia-6 | media | G-A10, G-A8 | introduccion.tex:50, :96 | :50 da las tres elecciones que acercan la prueba a la equivalencia, y :96 dice que las asimetrias se "tratan con análisis posteriores", pero sin su sentido. DEC (3) pto 3 (#188, decidida) fija que el piso de ruido del sintetizador favorece al difusor en el contraste primario. Referido a su propia sintesis sin metal, la diferencia se aleja de cero. Quien lea el resultado no concluyente sin ese dato no sabe que otra asimetria empuja tambien hacia la equivalencia | En :96, o junto a las tres elecciones de :50, una clausula: el piso de ruido del sintetizador tambien acerca la comparacion a la equivalencia (`sec:amenazas`). En la introduccion, sin la cifra del pareado, porque es un resultado descriptivo del cap. 4 |
| guia-7 | media | G-A10 | introduccion.tex:84 | Patron PAT-116 reincide. El primer supuesto (generar la apariencia en el dominio de imagen) cierra con "la comparación ..., ya ejecutada y no concluyente, es la que puede contradecirlo". El resultado ya existe, y la oracion no dice que hizo con el supuesto. El lector no sabe si el supuesto sigue en pie | Decir la consecuencia con la lectura del pto 1: el resultado no lo confirma ni lo refuta (no se lee como equivalencia ni como no equivalencia demostrada), con remision a `sec:amenazas` |
| guia-8 | baja | G-A7 | introduccion.tex:41 | Patron PAT-182 reincide (leve). El Obj. 3 enumera las comparaciones y abre con la copia y pegado, antes del protocolo fisico. El papel de cada una solo aparece en :50 y :52: el protocolo fisico es el contraste primario, y la copia y pegado, control de cordura | Nombrar primero el protocolo fisico, como contraste primario, y la copia y pegado como control de cordura |
| guia-9 | baja | G-A8 | introduccion.tex:50 | $\Delta = 196.3$ HU se da como "medido en pacientes de validación" sin decir que son dos. DEC 2026-10-15 pto 15 manda declarar aparte la incertidumbre del margen (n = 2), y cap3:417 lo hace. Esa incertidumbre debilita la evidencia que haria fallar el objetivo | "medido en dos pacientes de validación", con remision a `sec:amenazas` |
| guia-10 | baja | G-T2 | introduccion.tex:5 | Patron PAT-14 reincide (encabezado, escalado por #126). "Bandas oscuras" usa "banda", reservada para $B_{\delta}$. "Escasez de fotones" no es el termino fijo "inanición de fotones" | "Zonas oscuras"; "inanición de fotones". Aplicar al reescribir el encabezado |
| guia-11 | baja | G-A5 | introduccion.tex:19-21 | Repetido de r07 (escalado). Bajo "Formulación del problema" solo hay una pregunta sobre "la cadena propuesta". La tension esta en :58. La pregunta la decidio la autora (DEC 2026-10-08 pto 24) | Al reescribir el encabezado, poner antes de la pregunta una oracion de remision a la tension de :58, en la forma que deje guia-1 |

TOTAL alta=2 media=5 baja=4

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP. El cap. 4 es esqueleto, asi que las remisiones al "capítulo de resultados" llegan a un capitulo vacio |
| G-T2 | no cumple (guia-10) |
| G-T3 | cumple: $M$, $B_{\delta}$, $G$, $\Delta$ y $W_1$ significan lo mismo que en los cap. 1 y 3 |
| G-T4 | no evaluable (lo revisa `auditor-trazabilidad`). Se usa solo para detectar marcas envejecidas (guia-4, guia-5) |
| G-T5 | cumple (orden decidido, DEC 2026-10-08 pto 24) |
| G-T6 | no evaluable (lo revisa `auditor-trazabilidad`) |
| G-A1 | cumple: planteamiento (:3-9), revision preliminar (:5-11, :58-62), proposito (:13, :32) y pregunta (:21) |
| G-A2 | cumple |
| G-A3 | no cumple en el cruce (guia-1): la tension no recoge el precedente de #179 que DEC (3) pto 9 manda nombrar |
| G-A4 | cumple (:5, :60) |
| G-A5 | cumple a medias (guia-11, decision de la autora) |
| G-A6 | cumple |
| G-A7 | cumple a medias (guia-2, guia-8). La reconstruccion de implantes reales ya esta en :41 |
| G-A8 | no cumple (guia-2), con guia-6 y guia-9 como debilitamientos. El Obj. 1 tiene regla de fallo. El Obj. 2 no la tiene, por decision de la autora, y asi se declara. El Obj. 4 es de definicion declarada |
| G-A9 | cumple (orden decidido) |
| G-A10 | cumple a medias (guia-4, guia-5, guia-6, guia-7). Las cuatro exclusiones tienen cada una su razon (PAT-44 no reincide) |
| G-B10 | no cumple en el cruce (guia-1). Hoy cap2:108 repite la tension de :58 con las mismas palabras, pero el pto 9 obliga a cambiar las dos |
| G-C4 | cumple a medias (guia-2): Obj. 3 tiene resultado, pero no su lectura respecto del objetivo |
| G-D1, G-D2 | no evaluable: `conclusiones.tex` es esqueleto. Cuando se redacte, G-D1 dependera de la lectura de guia-2 |

## Propuestas de criterio
- Bloque (a), repetida de r06 y r07: cuando un objetivo ya tiene resultado, la introduccion dice como se lee respecto del
  objetivo (cumplido, no cumplido o no concluyente) y si esa lectura se fijo antes o despues del resultado. Si el objetivo
  se declara cumplido por haberse ejecutado, se nombra que parte suya podia fallar (G-A8).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que niega una evaluacion ya ejecutada y registrada | G-A10 | `\GAPDATO{evaluación en prueba de la versión~2}`; salto en el borde de $G$ | PAT-122 |
| Desenlace obtenido de una prueba de equivalencia sin lectura para el objetivo | G-A8 | "no concluyente ... con una diferencia significativa a la baja" | PAT-136 |
| Supuesto que una prueba ya ejecutada podia contradecir, redactado en condicional | G-A10 | "ya ejecutada y no concluyente, es la que puede contradecirlo" | PAT-116 |
| El control de cordura aparece antes que el contraste primario | G-A7 | "se compara con la inserción por copia y pegado, ... con el protocolo físico" | PAT-182 |
| Una decision que reformula la brecha se aplica en el estado del arte, pero no en la tension de la introduccion | G-A3, G-B10 | "ninguno de los tres enfoques revisados ... produce a la vez" (falta #179) | nuevo |
| Lectura posterior que da por cumplido un objetivo "por ejecutarse" sin decir que parte podia fallar | G-A8 | "el Objetivo 3 se cumple como objetivo de diseño y evaluación" (riesgo al aplicar pto 1) | nuevo |
