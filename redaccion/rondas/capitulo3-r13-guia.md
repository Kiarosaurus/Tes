# Revision guia CS — capitulo3 — r13

Leidos: `RUBRICA.md`, `overleaf/CLAUDE.md`, `BITACORA.md` (§1 y §2), `capitulo3-r12-respuesta.md`, `capitulo3-r12-guia.md`,
`capitulo3-r13-lint.md` (PASA). Para cruces: `introduccion.tex` l. 30-64 y `capitulo1.tex` l. 120-134. Cotejo puntual:
`docs/01-decisiones.md` 2026-10-09 (4)-(8). Los cinco hallazgos de guia r12 quedaron aplicados o escalados con `\GAPDEC`
(l. 360, l. 198, l. 358, l. 31, "corrida") y no se repiten. En r12 no hay hallazgos de guia RECHAZADOS que reabrir.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C7 | capitulo3.tex:358 frente a :304-306, :272, :206 y :332 | Patron PAT-140 reincide. La l. 332 promete que amenazas enumera las decisiones tomadas despues de ver datos. En el Obj 3 faltan tres: (a) corregir dos errores y volver a correr la sonda despues de que fallara, y esa segunda corrida es la que mantuvo la equivalencia como contraste primario; (b) generar tambien los cortes de solo banda (#160, DEC 2026-10-09 (4)), decidido al ver en validacion que la mitad de las regiones caia en cortes no generados; (c) dejar el criterio de 30 000 pasos y elegir el punto de control por cotejo, decidido al ver que la perdida no ordenaba la fidelidad de los HU. | Anadirlas a la lista del Obj 3 en una oracion, cada una con su efecto: (a) dio una segunda oportunidad a la regla que fijaba el contraste primario; (b) sube la amplitud del sintetizador. Aclarar que ninguna uso pacientes de prueba |
| guia-2 | media | G-C7 | capitulo3.tex:380 | Patron PAT-38 reincide. "Uno de los dos receptores lleva, ademas, un objeto metalico no ortopedico, una condicion que la sintesis sobre pelvis sin metal excluye" cierra el parrafo sin decir que efecto tiene. Ese receptor fija $\Delta$, el punto de control y el material. No se dice si el artefacto de la cremallera puede entrar en el anillo de 12 a 15 mm o en $s_{\mathrm{sem}}$, ni en que sentido moveria el margen. | Decir el sentido del sesgo, si consta (por ejemplo, rayas propias que ensanchan $s_{\mathrm{sem}}$ o elevan la referencia del perfil). Si no consta, decir que el efecto no esta medido y remitir al `\GAPDEC` de l. 208 |
| guia-3 | media | G-C7 | capitulo3.tex:38 frente a :328 y :358 | Patron PAT-13 reincide. La l. 38 dice que el diseno del Obj 3 se fijo "antes de tocar ningun paciente de prueba". Pero la referencia de realismo forma parte de ese diseno (DEC 2026-10-09 (6) pto 3, que (7) sustituye). Se escribio con 3 de 11 pacientes de prueba ya revisados en cortes, y la lista anterior salio de clasificar los implantes de esos pacientes, como reconoce la propia l. 358. La afirmacion general es mas fuerte que la amenaza que la matiza. | Acotar l. 38: antes de procesar ningun paciente de prueba con el sintetizador o el protocolo fisico. Remitir a `sec:amenazas` por la regla de realismo |
| guia-4 | baja | G-T2 | capitulo3.tex:370 | Patron PAT-14 reincide. "Una sola corrida local del protocolo fisico" usa "corrida" fuera de la sonda y la corrida final (BITACORA §2, 2026-10-10). Ademas no se sabe si se refiere a la sonda o a la verificacion de reproduccion de l. 294. | Nombrar cual: "la sonda de viabilidad" o "la verificacion de reproduccion en local" |
| guia-5 | baja | G-C5, P-MM3 | capitulo3.tex:276, :204 | La reconstruccion de implantes reales mide "el salto de los valores de TC al cruzar el borde de $G$, descontado el de la TC real". No se dice sobre que voxeles se calcula ni con que estadistico. El MAE y las integridades si tienen definicion operativa. | Una oracion con la definicion operativa del salto (voxeles a cada lado del borde, estadistico), o `\GAPDATO` si solo consta en el codigo |
| guia-6 | baja | G-C5 | capitulo3.tex:326 | El contraste de realismo nombra dos estadisticos, el perfil radial y el histograma en $M$. El resumen por paciente solo usa la fraccion de cascaras del perfil, y no se dice como entra el histograma: si se compara o solo se reporta. | Decir el papel del histograma: descriptivo, sin resumen, o con el desempate del cotejo |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | no cumple (guia-4, leve) |
| G-T3 | cumple ($\Delta$, $s_{\mathrm{sem}}$, $r_{\mathrm{rep}}$, $h$/$\epsilon$, $T$ sin choques dentro del capitulo) |
| G-T4 | cumple con GAP (las cifras son de `auditor-trazabilidad`) |
| G-T5 | cumple |
| G-T6 | cumple (lint sin citas indefinidas) |
| G-A7 (cruce) | cumple con GAP del lado del cap. 3. Del lado de `introduccion.tex`:41, la reconstruccion de implantes reales sigue sin nombrarse; se reporta en su seccion |
| G-A8 (cruce, lado del bloque c) | cumple con GAP (`\GAPDEC` de los desenlaces del TOST, l. 320) |
| G-C1 | cumple con GAP (regla del suelo, cabeza de $M$, semimaximo) |
| G-C2 | cumple con GAP (lote 16 con `\GAPDEC`) |
| G-C3 | cumple |
| G-C4 | cumple con GAP. El cruce con otras secciones sigue roto, pero no se evalua aqui: `introduccion.tex`:48 ("aun sin medir") y :56 ("sobre las poses del muestreador") contradicen l. 270 y l. 320. `capitulo1.tex`:122 ("14 valores"), :128 ("aun sin preinscribir", "corridas repetidas") y :132 ("en el Objetivo 2 hubo tres") estan desfasados frente a l. 264, l. 322 y l. 354 |
| G-C5 | no cumple (guia-5, guia-6, leves) |
| G-C6 | cumple: lineas base, emparejamiento por paciente, elegibilidad por ancho del corredor declarada (l. 380) |
| G-C7 | no cumple (guia-1, guia-2, guia-3). Los cuatro tipos son explicitos y no pro forma, y el sesgo conjunto de r12 ya esta con `\GAPDEC` (l. 360). Pero la lista post hoc sigue incompleta, una amenaza no tiene efecto y la integridad del congelamiento se afirma mas fuerte que lo registrado |
| G-C8 | cumple con GAP (supuesto del IC con *t*, tamano de efecto del Wilcoxon) |
| G-C9 | cumple: el protocolo fisico es la linea base fuerte; la copia y pegado es control de cordura declarado |
| P-MM1 | cumple |
| P-MM2 | cumple (Figura 3.1 con realismo y reconstruccion) |
| P-MM3 | no cumple (guia-5, leve) |

## Propuestas de criterio
- La misma de r10 a r12: coherencia entre el diseno descrito y el registro congelado (`diseno_A.md` §0, DEC 2026-10-09 (6)-(8)) como criterio propio del bloque (c).
- Nueva: la tabla de cruces del cap. 1 (marco estadistico) contra el cap. 3 no tiene ronda que la revise. Tres cifras o estados del cap. 1 quedaron atras del cap. 3 en esta serie de rondas. Conviene una pasada `documento` antes de cerrar el cap. 3.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Lista de decisiones post hoc que omite correcciones de implementacion hechas tras ver un resultado de validacion | G-C7 | lista del Obj 3 sin la segunda sonda ni los cortes de solo banda | PAT-140 |
| Dato de amenaza que cierra el parrafo sin su efecto sobre el resultado | G-C7 | "Uno de los dos receptores lleva, ademas, un objeto metalico no ortopedico" | PAT-38 |
| Afirmacion general de integridad del congelamiento que la lista de amenazas matiza despues | G-C7 | "antes de tocar ningun paciente de prueba" (realismo con 3 de 11 revisados) | PAT-13 |
| "Corrida" para una ejecucion que no es la sonda ni la corrida final | G-T2 | "una sola corrida local del protocolo fisico" | PAT-14 |
