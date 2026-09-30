# Revision guia CS — capitulo3 — r05

Leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (PAT-1 a PAT-36; VIGENTES comprobados; decisiones de §2 respetadas), `capitulo3-r04-guia.md`, `capitulo3-r04-respuesta.md`, `capitulo3-r05-lint.md` (PASA, 0/0/4). Cruces: `introduccion.tex` (redactada, desfasada; cubierta por `\GAPDEC` l. 13), `capitulo1.tex`, `capitulo2.tex`, `capitulo4.tex` (esqueletos). Para el hallazgo guia-1 se cotejo `docs/01-decisiones.md` :1272-1277 y :1398-1401.

Respuesta r04: guia-1 a guia-4, guia-6 y guia-7 aplicados; no se reportan. guia-5 (doble papel de la viabilidad, PAT-30) quedo NO APLICADO con motivo (decision de la autora, escalada a #127): no se reabre, aunque el texto sigue igual (l. 91 y Tabla `tab:diseno`).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T2, P-MM3 | capitulo3.tex:223 (vs 48, 54) | Patron PAT-14 reincide. "Prueba y reprueba" designa en l. 54 el unico paciente adquirido dos veces con el mismo implante (en l. 48, "par de reproducibilidad"). En l. 223 designa corridas repetidas del protocolo fisico, que es lo que dice DEC :1276 ("test-retest del brazo fisico"). El lector no sabe si $\Delta$ usa ese paciente ni que varia entre dos corridas del protocolo fisico. Tampoco sabe si el protocolo fisico, que corre sobre un subconjunto aun sin fijar (l. 221), incluye los 3 pacientes de validacion. | Usar un solo nombre para el paciente adquirido dos veces. En l. 223, decir que se repite en el protocolo fisico (semilla de ruido, corrida completa) y que corre sobre los casos de validacion; si no consta, `\GAPDEC`. |
| guia-2 | media | G-C7, G-C5 | capitulo3.tex:176, 213, 223 (vs 257) | Patron PAT-22 reincide. La banda "trunca a proposito las rayas lejanas" (l. 176), y el protocolo fisico genera rayas en todo el volumen (l. 225). La *streak amplitude* primaria se mide "en regiones perpendiculares a las rayas" (l. 213), pero no se dice si esas regiones quedan dentro de $B_{\delta}$. Si alguna cae fuera, el sintetizador da amplitud nula por construccion y la prueba de equivalencia frente al protocolo fisico queda sesgada. El truncamiento no figura en validez de constructo. | Decir donde se ubican las regiones de medicion respecto de $B_{\delta}$ (o `\GAPDEC`), y anadir a validez de constructo que el truncamiento a 12 mm limita lo que la comparacion con el protocolo fisico puede mostrar. |
| guia-3 | media | G-C5 | capitulo3.tex:182, 215 | Se nombran dos evaluaciones sin variable, metrica ni analisis, y ninguna esta en la Tabla `tab:diseno`: "se evalua por la continuidad de los numeros de TC a traves del borde de la banda" (l. 182) y "el realismo se juzga contra observaciones reales de artefacto" (l. 215). En l. 182 tampoco se dice como se cuantifica el primer desplazamiento (mascara umbralizada frente a cilindro liso). | Para cada una, dar metrica y analisis y anadirla a la tabla como descriptiva, o `\GAPDEC`/`\GAPDATO` con lo que falta. |
| guia-4 | baja | G-C7 | capitulo3.tex:251 | "La cohorte primaria pierde, en proporcion, mas pacientes del grupo 2 que el conjunto de partida" no dice que amenaza supone para el Objetivo 2, ni en que direccion podria sesgar la distribucion de grados. Queda como dato suelto dentro de validez interna. | Una clausula que diga que sesgo introduce esa perdida (o por que no lo introduce), o moverla a caracterizacion de cohorte. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP (arquitectura del sintetizador, algoritmo del eje, heuristica de referencias, ajuste del decodificador) |
| G-T2 | no cumple a medias (guia-1) |
| G-T3 | cumple ($\delta$/$\Delta$, $i$/$p$, $P$/$p$, $\sigma_t$/$\sigma_a$, $h$/$\epsilon$ distintos); cruce con cap. 1 no evaluable (esqueleto) |
| G-T4 | cumple dentro del dominio de este revisor; la exactitud de cifras es de auditor-trazabilidad |
| G-T5 | cumple (el orden anunciado en l. 9 coincide con las secciones) |
| G-T6 | cumple (el lint no reporta citas faltantes) |
| G-A7 (cruce) | cumple con GAP (introduccion desalineada, `\GAPDEC` l. 13; evidencia del Obj 4, `\GAPDEC` l. 185) |
| G-A8 (cruce) | cumple con GAP (Obj 2 sin regla, `\GAPDEC` l. 207; fallo de la superioridad del Obj 3, `\GAPDEC` l. 217); l. 162 distingue controles de implementacion (PAT-15 no reincide) |
| G-B3 (cruce) | no evaluable (capitulo1 en esqueleto) |
| G-C1 | cumple con GAP ($h = 2\sigma$, l. 158; valor de 8 mm, l. 196; envolvente y forámenes, l. 255) |
| G-C2 | cumple con GAP (diseno del sintetizador no congelado, l. 172) |
| G-C3 | cumple |
| G-C4 | cumple con GAP (preguntas de la introduccion desfasadas, `\GAPDEC` l. 13) |
| G-C5 | no cumple a medias (guia-3; guia-2 en la ubicacion de las regiones de rayas); inversion de metricas con GAP (l. 215) |
| G-C6 | cumple con GAP (regla del Obj 2, copia y pegado, agregacion por paciente) |
| G-C7 | cumple a medias: cuatro tipos, no pro forma; S1 en la serie navegada y envolvente ya en constructo; falta el truncamiento de la banda (guia-2, media) y guia-4 (baja) |
| G-C8 | cumple con GAP (agregacion por paciente, intervalo de $W_1$, $\Delta$) |
| G-C9 | cumple con GAP (permanencia del protocolo fisico, `\GAPDEC` l. 223; PAT-16 cubierto por el `\GAPDEC` de l. 217) |
| P-MM1 | cumple en orden y ligazon a objetivos; PAT-30 sigue presente pero escalado (guia-5 r04, no se reabre); relacion con el marco teorico no evaluable |
| P-MM2 | cumple |
| P-MM3 | cumple con GAP (heuristica, eje, ajuste del decodificador, protocolo fisico); guia-1 |

Patrones VIGENTES comprobados en el dominio de este revisor: PAT-2 (l. 221 con `\GAPDEC`: no reincide), PAT-14 (reincide, guia-1), PAT-15 (no reincide), PAT-21 (recortes definidos en l. 85: no reincide), PAT-22 (reincide, guia-2), PAT-23 (amenazas no introducen parametros nuevos: no reincide), PAT-26 (circularidad solo en l. 251; S1 navegada solo en l. 255: no reincide), PAT-27 (fractura confirmada, l. 251: no reincide), PAT-28 (validacion definida en l. 50: no reincide), PAT-29 (8 mm en l. 87, $B_{\delta}$ en l. 73: no reincide), PAT-30 (escalado, no se reporta), PAT-31 (l. 255: no reincide), PAT-35 (8 mm con `\GAPDEC`; 12 mm declarado como parametro de diseno sin respaldo en l. 176: no reincide), PAT-36 (l. 221 "unico de los tres brazos" acotado: no reincide). PAT-5, PAT-6, PAT-7, PAT-24, PAT-25, PAT-32 a PAT-34 son de estilo y trazabilidad.

## Propuestas de criterio
- Se mantiene la de r01 a r04: un criterio del bloque (c) que exija, para cada objetivo, una regla de exito o fallo fijada a priori.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un termino ya usado para un control de datos se reusa para otra operacion | G-T2 | "prueba y reprueba del protocolo fisico" vs paciente adquirido dos veces | PAT-14 |
| Decision de diseno cuya consecuencia sobre la comparacion no figura en amenazas | G-C7 | "trunca a proposito las rayas lejanas" | PAT-22 |
| Evaluacion nombrada en el texto sin metrica ni analisis, y ausente de la tabla de diseno | G-C5 | "se evalua por la continuidad de los numeros de TC" | nuevo |
| Dato de sesgo en amenazas sin decir que amenaza supone | G-C7 | "pierde, en proporcion, mas pacientes del grupo 2" | nuevo |
