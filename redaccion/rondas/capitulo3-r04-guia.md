# Revision guia CS — capitulo3 — r04

Leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (PAT-1 a PAT-27; VIGENTES comprobados; decisiones de §2 respetadas), `capitulo3-r03-guia.md`, `capitulo3-r03-respuesta.md`, `capitulo3-r04-lint.md` (PASA, 0/0/4). Cruces: `introduccion.tex` (redactada, desfasada; cubierta por `\GAPDEC` l. 13), `capitulo1.tex` y `capitulo4.tex` (esqueletos).

Respuesta r03: guia-1 a guia-8 aplicados; no se reportan. guia-9 (motivo de la cohorte de sensibilidad) quedo NO APLICADO con motivo (ninguna fuente lo da) y pregunta a la autora: no se reabre. La definicion del semimaximo local (r02) tampoco se reabre.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T2 | capitulo3.tex:221, 259 (vs 50) | "Pacientes de validacion" aparece solo en l. 221 y l. 259. La particion descrita en l. 50 tiene entrenamiento y 34 de prueba, sin conjunto de validacion. El lector no sabe de donde salen los 3 pacientes que fijan $\Delta$. Si salen de prueba, el margen no estaria "fijado de antemano" respecto de la prueba que decide, y el aislamiento de l. 50 no lo aclara. | En l. 50, decir si la particion tiene un conjunto de validacion, de donde sale y cuantos pacientes tiene. Si no consta, `\GAPDATO`/`\GAPDEC`. |
| guia-2 | media | G-C1 | capitulo3.tex:87, 192, 196 | La brecha (Ec. brecha) se mide contra la envolvente, que es la union de mascaras con cierre de 2 mm y relleno de cavidades cerradas. No se dice si el canal sacro y los forámenes quedan fuera de la envolvente. Si el cierre o el relleno los ocupan, una penetracion foraminal da $b = 0$. El propio capitulo cita la penetracion foraminal como dato de la referencia (l. 253), asi que es parte del fenomeno que SAP debe capturar. | Una oracion en l. 87 o l. 196 que diga si canal y forámenes quedan fuera de la envolvente. Si no se verifico, supuesto en validez de constructo o `\GAPDATO`. |
| guia-3 | media | G-C7 | capitulo3.tex:205 (vs 198) | Patron PAT-22 reincide. "Se asume S1" para la serie navegada sostiene que la referencia sea "solo en S1" (l. 198), que se presenta como hecho. El supuesto no tiene justificacion y no aparece en amenazas. Si la serie navegada incluye tornillos de S2, la comparacion mezcla niveles. | Llevarlo a validez de constructo o externa como supuesto no verificado, y matizar "solo en S1" en l. 198 para la serie navegada. |
| guia-4 | baja | P-MM3 | capitulo3.tex:87 vs 194 | En l. 87 el diametro del corredor se mide "excluidos los extremos", sin decir cuanto. El valor de 8 mm aparece solo en l. 194, que dice que es el mismo recorte de l. 87. Quien reproduzca la medicion del corredor desde §corredor no tiene el valor. | Dar los 8 mm en l. 87 y remitir desde l. 194. |
| guia-5 | baja | P-MM1 | capitulo3.tex:91 vs 187, 239 | La Tabla `tab:diseno` y l. 187 hacen de la viabilidad del corredor una variable dependiente del Objetivo 2 (componente de SAP). Pero l. 91 ya reporta sus resultados (65.3, 23.6, 62.5, 20.8 %; 29 y 27 de 72) en el metodo. La decision de §2 manda al cap. 4 los veredictos y deja en el cap. 3 la caracterizacion de cohorte. Aqui la misma cifra cumple los dos papeles. | Escoger uno de los dos papeles: o la viabilidad es caracterizacion de cohorte (y sale de la variable dependiente), o sus porcentajes pasan al cap. 4. Lo decide la autora. |
| guia-6 | baja | G-T2 | capitulo3.tex:71, 75, 85, 194 | Patron PAT-14 reincide. "Recorte" designa tres cosas: el modelo de recorte de TotalSegmentator ("recorte por defecto/alternativo", termino definido en l. 85), el acortamiento de 8 mm en los extremos del tramo $T$ (l. 194, "El recorte existe porque...") y el recorte de intensidades (l. 71, 75). En l. 194 el lector acaba de leer que todo el Objetivo 2 "depende del recorte por defecto". | Reservar "recorte" para TotalSegmentator y usar otro termino para los extremos (por ejemplo, "exclusion de extremos") y para las intensidades. |
| guia-7 | baja | P-MM3 | capitulo3.tex:73 | El MAE "dentro de $B_{\delta}$" del Objetivo 1 se aplica a volumenes con metal real, pero no se dice alrededor de que mascara se construye la banda (el umbral de 2500 HU aparece recien en l. 176) ni con que ancho (los 12 mm aparecen en l. 174). | En l. 73, decir que mascara y que ancho definen $B_{\delta}$ en esa medicion, o remitir a §sintetizador. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP (arquitectura del sintetizador, algoritmo del eje, heuristica de referencias, ajuste del decodificador) |
| G-T2 | no cumple a medias (guia-1 media; guia-6 baja) |
| G-T3 | cumple ($\sigma_t$/$\sigma_a$ resuelto; $i$/$p$, $\delta$/$\Delta$, $P$/$p$ distintos); el cruce con cap. 1 no es evaluable (esqueleto) |
| G-T4 | cumple dentro del dominio de este revisor; la exactitud de cifras es de auditor-trazabilidad |
| G-T5 | cumple (el orden anunciado en l. 9 coincide con las secciones) |
| G-T6 | cumple (el lint no reporta citas faltantes) |
| G-A7 (cruce) | cumple con GAP (introduccion desalineada, `\GAPDEC` l. 13; evidencia del Obj 4, `\GAPDEC` l. 183) |
| G-A8 (cruce) | cumple con GAP (Obj 2 sin regla, `\GAPDEC` l. 205; fallo de la superioridad del Obj 3, `\GAPDEC` l. 215); l. 162 distingue los controles de implementacion (PAT-15 no reincide) |
| G-B3 (cruce) | no evaluable (capitulo1 en esqueleto) |
| G-C1 | no cumple a medias (guia-2); $h = 2\sigma$ cumple con GAP |
| G-C2 | cumple con GAP (diseno del sintetizador no congelado, l. 170) |
| G-C3 | cumple |
| G-C4 | cumple con GAP (preguntas de la introduccion desfasadas, `\GAPDEC` l. 13) |
| G-C5 | cumple con GAP (inversion de metricas, l. 213) |
| G-C6 | cumple con GAP (regla del Obj 2, copia y pegado, agregacion por paciente) |
| G-C7 | cumple salvo guia-3 (media); cuatro tipos, no pro forma, con fractura confirmada (PAT-27 no reincide) y supuesto mascara-artefacto (PAT-22 corregido en l. 178, reincide en l. 205) |
| G-C8 | cumple con GAP (agregacion por paciente, intervalo de $W_1$, $\Delta$) |
| G-C9 | cumple con GAP (permanencia del protocolo fisico, l. 221; PAT-16 en l. 215 queda cubierto por el `\GAPDEC` de la misma linea) |
| P-MM1 | cumple en orden y ligazon a objetivos (guia-5 baja); la relacion con el marco teorico no es evaluable |
| P-MM2 | cumple |
| P-MM3 | cumple con GAP (heuristica, eje, ajuste del decodificador, protocolo fisico); guia-4 y guia-7 bajas |

Patrones VIGENTES comprobados en el dominio de este revisor: PAT-1 (l. 227 distingue por objetivo: no reincide), PAT-2 (l. 219 con `\GAPDEC`: no reincide), PAT-4 (l. 95 con `\GAPDATO`: no reincide), PAT-13 (l. 58, l. 215: no reincide), PAT-14 (reincide, guia-6), PAT-15 (no reincide), PAT-16 (cubierto por GAP), PAT-22 (reincide, guia-3), PAT-23 (sin parametros nuevos en amenazas; variante en guia-4), PAT-27 (no reincide). PAT-5, PAT-6, PAT-18, PAT-24 a PAT-26 son de estilo y trazabilidad.

## Propuestas de criterio
- Se mantiene la de r01 a r03: un criterio del bloque (c) que exija, para cada objetivo, una regla de exito o fallo fijada a priori.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Supuesto sobre la referencia externa enunciado de pasada y ausente de amenazas | G-C1, G-C7 | "no se reporta en la navegada, donde se asume S1" | PAT-22 |
| Un termino ya definido ("recorte por defecto") se reusa para otra operacion | G-T2 | "El recorte existe porque un tornillo iliosacro entra y sale" | PAT-14 |
| Subconjunto de la particion nombrado sin haberse definido en la descripcion de la particion | G-T2, P-MM3 | "Se mide solo en pacientes de validacion" | nuevo |
| El valor de un parametro se da en una seccion posterior a la que lo usa, con remision hacia atras | P-MM3 | "excluidos los extremos" (l. 87); "Los 8 mm son el mismo recorte" (l. 194) | nuevo |
| La misma cifra propia funciona como caracterizacion de cohorte en el metodo y como variable dependiente en la tabla de diseno | P-MM1 | viabilidad 65.3 % en l. 91 y variable dependiente del Obj 2 | nuevo |
