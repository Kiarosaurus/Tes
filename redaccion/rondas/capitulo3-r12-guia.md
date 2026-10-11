# Revision guia CS — capitulo3 — r12

Leidos: `RUBRICA.md`, `overleaf/CLAUDE.md`, `BITACORA.md` (§1, §2 y §3), `capitulo3-r11-respuesta.md`, `capitulo3-r11-guia.md`,
`capitulo3-r12-lint.md` (PASA). Para cruces: `introduccion.tex` l. 23-64. Cotejo puntual: `docs/01-decisiones.md` 2026-10-09 (5)-(8),
`experiments/objetivo3/diseno_A.md` §0. Los once hallazgos de r11 quedaron aplicados o escalados con `\GAPDEC` y no se
reportan de nuevo. No hay hallazgos RECHAZADOS en r11 que reabrir.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C7 | capitulo3.tex:356, :308-310, :320 | El punto de control (l. 212), el material del comparador (l. 308) y $\Delta$ (l. 320) se fijaron sobre los mismos dos receptores de validacion y los mismos dos tornillos reales. Ademas, el titanio, que ya estaba mas cerca del sintetizador (815/1229 frente a 2051/1279 HU), paso a primario. Amenazas solo dice que la regla "no usa el sintetizador" y no dice en que sentido sesga la prueba de equivalencia: hacia concluir equivalencia. | En validez interna (o de la conclusion), una oracion: los dos brazos se ajustaron al mismo paciente de referencia, y el cambio de material desplaza la comparacion hacia la equivalencia aunque la regla sea independiente del sintetizador |
| guia-2 | media | G-C5, P-MM3 | capitulo3.tex:198 | Patron PAT-134 reincide. "El semimaximo local por objeto entra como sensibilidad" promete otra mascara de entrenamiento. Pero solo hubo dos entrenamientos con los mismos datos (l. 206), y el diseno congelado (`diseno_A.md` §0) no programa esa sensibilidad. | Decir que esa sensibilidad (DEC D1) no se entreno ni entra en la corrida final, o abrir un `\GAPDEC`, como con la rosca y la arandela en l. 133 |
| guia-3 | media | G-C7 | capitulo3.tex:356, :352 frente a :326, :101, :330 | Patron PAT-140 reincide. La l. 330 promete enumerar en amenazas las decisiones tomadas despues de ver datos. Faltan dos: (a) la regla de la referencia de realismo, escrita con la revision de la autora de los pacientes de prueba ya empezada (l. 326; DEC 2026-10-09 (7): 3 de 11 revisados, uno con un tornillo que la lista anterior no veia); (b) la sensibilidad del Obj 2 sin los dos casos con error de segmentacion (l. 101). Por (a), "Ninguna de esas tres decisiones uso pacientes de prueba" se lee como si ninguna decision del Obj 3 hubiera usado la particion de prueba. | Anadir (a) en el parrafo del Obj 3, con su efecto: usa la informacion de inclusion de prueba, no resultados. Anadir (b) en la lista del Obj 2 |
| guia-4 | baja | P-MM2 | capitulo3.tex:31 | La ultima caja de la Figura 3.1 solo nombra la comparacion con copia y pegado y con el protocolo fisico. Omite el contraste de realismo frente a tornillos reales de prueba (l. 284, l. 324) y la reconstruccion de implantes reales (l. 274), las dos con fila en la Tabla 3.3. | Anadir "y frente a tornillos reales (realismo)" o una caja paralela para la reconstruccion |
| guia-5 | baja | G-T2 | capitulo3.tex:133, :174, :186, :206 | Patron PAT-14 reincide. "Corrida final" esta definida (l. 38) y §2 reserva "corrida" para la sonda y la corrida final. Aun asi, "todas las corridas del Objetivo 3", "corridas de entrenamiento", "en las dos corridas" (entrenamiento y cohortes del muestreador) usan la palabra para entrenamientos y ejecuciones del muestreador. En l. 133 se lee como si la corrida final fuera una de "todas las corridas". | "Todos los entrenamientos/generaciones", "en los dos entrenamientos", "en las dos cohortes" |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | no cumple (guia-5, leve) |
| G-T3 | cumple ($s_{\mathrm{sem}}$/$r_{\mathrm{rep}}$, "limite" de la rampa y *t* en texto se sostienen) |
| G-T4 | cumple con GAP (las cifras son de `auditor-trazabilidad`) |
| G-T5 | cumple |
| G-T6 | cumple (lint sin citas indefinidas) |
| G-A7 (cruce) | cumple con GAP del lado del cap. 3. El cruce para `introduccion` sigue abierto: la l. 41 no nombra la reconstruccion de implantes reales |
| G-A8 (cruce, lado del bloque c) | cumple con GAP (`\GAPDEC` de los desenlaces del TOST) |
| G-C1 | cumple con GAP (regla del suelo y cabeza de $M$ con `\GAPDEC`) |
| G-C2 | cumple (guia-6 de r11 resuelto: duracion y configuracion del primer entrenamiento) |
| G-C3 | cumple |
| G-C4 | cumple con GAP. Cruce no evaluable aqui: `introduccion.tex`:48 ($\Delta$ "aun sin medir") y :56 ("sobre las poses del muestreador") siguen contradiciendo l. 268 y l. 320; se reportan en su seccion |
| G-C5 | no cumple (guia-2) |
| G-C6 | cumple: elegibilidad por ancho del corredor declarada (l. 376); IC con *t* y tamano de efecto con `\GAPDEC` |
| G-C7 | no cumple (guia-1, guia-3): los cuatro tipos son explicitos y no pro forma, pero falta el sesgo de seleccion comun de los brazos y la lista post hoc esta incompleta |
| G-C8 | cumple con GAP (supuesto del IC con *t*, tamano de efecto del Wilcoxon) |
| G-C9 | cumple: el protocolo fisico es la linea base fuerte; la copia y pegado es control de cordura declarado |
| P-MM1 | cumple |
| P-MM2 | no cumple (guia-4, leve) |
| P-MM3 | no cumple (guia-2) |

## Propuestas de criterio
- Se repite la de r10 y r11: coherencia entre el diseno descrito y el registro congelado (`diseno_A.md` §0) como criterio propio del bloque (c). guia-2 es otro caso.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Sensibilidad decidida antes del congelamiento, que el diseno congelado no programa, sigue anunciada | G-C5, P-MM3 | "el semimaximo local por objeto entra como sensibilidad" | PAT-134 |
| Lista de decisiones post hoc incompleta, con un cierre que exagera la integridad de la particion de prueba | G-C7 | "Ninguna de esas tres decisiones uso pacientes de prueba" (falta la regla de realismo) | PAT-140 |
| Varias elecciones de diseno (modelo, comparador, margen) calibradas sobre la misma muestra, sin amenaza conjunta | G-C7 | material y punto de control con los dos tornillos de un paciente | nuevo |
| Termino definido ("corrida final") cuyo nucleo se sigue usando para otras ejecuciones | G-T2 | "Todas las corridas del Objetivo 3 ... no entran en la corrida final" | PAT-14 |
