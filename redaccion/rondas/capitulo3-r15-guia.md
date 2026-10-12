# Revision guia CS — capitulo3 — r15

Entrada: `overleaf/secciones/capitulo3.tex` (estado tras el encargo r14, modelo run04), lint
`capitulo3-r15-lint.md` (PASA, solo E-P1 baja), respuesta `capitulo3-r14-respuesta.md`. E13 de r10
(RECHAZADO, BITACORA §2) no se reabre. Cotejado contra `docs/00-tesis.md` (corregido el 2026-10-11,
commit e0536fb), `docs/01-decisiones.md` 2026-10-09 (5)-(8) y 2026-10-11 (1)-(3), implicancias #171 y #172,
`experiments/objetivo3/EXPERIMENTOS.md` y `introduccion.tex` (para G-C4).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-C7 | capitulo3.tex:368 | "El sentido del efecto está registrado para dos de las tres elecciones" ya no es cierto: #171 (corregida) y `00-tesis.md`:148-151 registran que el punto de control elegido queda más cerca del protocolo físico con titanio que el estado final, y la l. 218/328 muestra que además da un $\Delta$ más ancho (163.8 frente a 100.3 HU). Las tres elecciones apuntan en validación hacia concluir equivalencia, y la amenaza al contraste primario lo presenta como no establecido. | Decir el sentido de las tres (material, margen y punto de control, este por dos vías: amplitud más cercana a Ti y margen más ancho), con remisión a las l. 222 y 328; reformular el `\GAPDEC` final sobre lo que sigue abierto (el efecto en la partición de prueba), no sobre el sentido. |
| guia-2 | media | G-C7 | capitulo3.tex:366 | Patron PAT-38 reincide. La amenaza de la evaluación previa de la prueba con el modelo afectado se nombra, pero no se dice que las enmiendas (reentrenamiento, punto de control, sensibilidad, $\Delta$) se fijaron ya conociendo ese resultado (#171, "Hecho") ni qué sesgo puede introducir eso en la corrida final. | Una oración con el efecto: que esas decisiones se tomaron con el resultado de prueba visto y en qué sentido podría haberlas orientado (o por qué no: reglas previas que no usan prueba), sin cifras del modelo afectado. |
| guia-3 | media | G-C7, P-MM1 | capitulo3.tex:366 (y 338) | Patron PAT-140 reincide. La l. 338 promete que "las decisiones ... tomadas después de ver datos se enumeran" en amenazas, y la lista de la l. 366 omite la sensibilidad con el estado final, añadida tras ver en validación la distancia de histograma (l. 222; DEC 2026-10-11 (3), pto. 2). | Añadirla a la enumeración de decisiones posteriores a resultados de validación, con su motivo. |
| guia-4 | media | G-T4, G-C7 | capitulo3.tex:314 | "Después de fijar el hierro, la medición del margen ... mostró que el sintetizador queda mucho más cerca ... con titanio" seguido de "La amplitud del sintetizador evaluado va ... 901 a 1057" atribuye al modelo run04 la observación que motivó el cambio de material, que se hizo el 2026-10-09 (DEC 2026-10-09 (5), "Contexto") con el modelo anterior, archivado por #166, antes de entrenar run04. | Decir que la observación que motivó la regla del material se hizo con un modelo anterior al reentrenamiento, y dar las cifras de run04 como comprobación posterior de que la cercanía se mantiene. |
| guia-5 | media | G-C7, G-T4 | capitulo3.tex:202 | Patron PAT-39 reincide. "el único parámetro heredado de un modelo anterior es el límite de 0.05" lo contradice el propio capítulo: el ancho de cáscara de 1 mm se adoptó en un cotejo con un modelo anterior (l. 218), la regla del material nació de una observación con el modelo anterior (DEC 2026-10-09 (5)) y el salto de borde se midió con otro punto de control (l. 206). | Acotar la frase a los parámetros de lectura de HU, o enumerar todo lo heredado (0.05, cáscara de 1 mm, motivo del cambio de material) con remisión a la validez interna. |
| guia-6 | media | G-T4, OC-2 | capitulo3.tex:222 | Patron PAT-122 reincide. El `\GAPDEC` dice que "el registro de la tesis afirma que la elección ... no acerca el sintetizador al protocolo físico" y que "falta decidir qué se afirma". Esa frase del registro se corrigió el 2026-10-11 (#171, `00-tesis.md`:150-151: el elegido es el que queda más cerca del protocolo físico y la sensibilidad es la lectura conservadora). | Cerrar el GAP y escribir la frase decidida: el elegido, fijado por una regla que no mira el protocolo físico, queda más cerca de él; la sensibilidad con el estado final es la lectura conservadora. |
| guia-7 | media | G-T4, OC-2 | capitulo3.tex:312 | Patron PAT-122 reincide. El `\GAPDATO` declara ausentes los "resultados del protocolo físico sobre los 13 pacientes de prueba", pero `EXPERIMENTOS.md`:68 registra `a19_final` sobre esos 13 como CORRIDO y válido con run04 (no usa el sintetizador). | Decir que el brazo físico ya se corrió sobre los 13 y que sus resultados se presentan en el capítulo 4 (BITACORA §2, 2026-09-29), sin `\GAPDATO`, o reducir el GAP a lo que falte de verdad. |
| guia-8 | media | P-MM3, G-C5 | capitulo3.tex:268, 280, 334, 351 | La población de la reconstrucción de implantes reales (19 pacientes con metal: 11 + 8) se da como hecho en el método y en la Tabla de diseño, mientras `00-tesis.md`:161 da "13 de test con metal" para esa evaluación, tras las auditorías del 11 de octubre. El único `\GAPDEC` está en §Datos (l. 52) y no alcanza a estas secciones; el lector no sabe sobre cuántos pacientes se mide la variable dependiente. | Remitir al `\GAPDEC` de §Datos desde la primera mención en §ap-sintesis/§ap-reconstruccion y en la celda de la tabla, o adoptar la cifra cuando la autora decida. |
| guia-9 | media | G-T2 | capitulo3.tex:107 frente a 384 | La l. 107 habla de 17 pacientes en que el censo "identificó un candidato a tornillo transilíaco-transsacro"; la l. 384 afirma que ninguno de los 56 pacientes de CLINIC-metal lleva ese tornillo. "Candidato a TS" designa ahora objetos que el conteo de la autora descarta como TS, y el lector lee una contradicción. | Nombrar los 17 por lo que el censo mide ("componente alargado y fino, candidato por forma", l. 131) y añadir que el conteo de la autora no confirma ningún TS (remisión a la validez externa). |
| guia-10 | baja | G-T4 | capitulo3.tex:204 | Patron PAT-31 reincide. El tercer desplazamiento de dominio se cuantifica con "0.62 frente a 1.40" sin la condición que el párrafo anterior da a 0.62 (medido en el conjunto previo a los retiros, `\GAPDATO` de la l. 200). | Añadir la condición ("en el conjunto previo a los retiros") o remitir al GAP. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | no cumple (guia-9) |
| G-T3 | cumple ($\Delta$ solo designa el margen; el 0.05 se nombra "límite", sin símbolo) |
| G-T4 | no cumple (guia-4, guia-5, guia-6, guia-7, guia-10) |
| G-T5 | cumple |
| G-T6 | cumple (lint sin E-F) |
| G-C1 | cumple con GAP (0.05 heredado, `\GAPDEC` #172; cabeza de $M$; lotes) |
| G-C2 | cumple con GAP (algoritmo del eje, heurística de referencias, predicción $v$) |
| G-C3 | cumple |
| G-C4 | cumple dentro del cap. 3. Cruce con `introduccion.tex`: la introducción quedó atrás del r14 — l. 48 "un margen ... aún sin medir" (cap. 3: 163.8 HU), l. 90 "el modelo final no está elegido" (cap. 3: elegido) y l. 56 "el protocolo de Peters et al. sobre las poses del muestreador" (cap. 3, l. 274: eje sin perturbar, con `\GAPDEC`). No se reporta como hallazgo de esta sección; corresponde a la ronda de introducción |
| G-C5 | cumple con GAP, salvo la población de la reconstrucción (guia-8) |
| G-C6 | cumple (copia y pegado como cordura, protocolo físico como comparación, sensibilidades declaradas) |
| G-C7 | no cumple (guia-1, guia-2, guia-3, guia-4, guia-5) |
| G-C8 | cumple con GAP (supuesto de la *t*, lectura de desenlaces del TOST, tamaño de efecto) |
| G-C9 | cumple (el protocolo físico publicado es el competidor; la copia y pegado se declara cordura) |
| P-MM1 | cumple, salvo la promesa de la l. 338 (guia-3) |
| P-MM2 | cumple (Figura `fig:pipeline`) |
| P-MM3 | cumple con GAP, salvo guia-8 |

## Propuestas de criterio
- Bloque (c): cuando el conjunto de prueba se evaluó con un modelo que luego se retira, el método debe decir
  qué decisiones posteriores se tomaron con ese resultado visto y su posible efecto. Hoy cabe en G-C7, pero la
  rúbrica no lo nombra y la redacción tiende a reducirlo a una frase de transparencia.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Al sustituir las cifras de un modelo retirado por las del vigente, se reatribuye al vigente la observación que motivó una decisión anterior | G-T4, G-C7 | "mostró que el sintetizador queda más cerca ... La amplitud del sintetizador evaluado va" | nuevo |
| Amenaza a la validez sin su efecto sobre el resultado | G-C7 | "La partición de prueba sí se había evaluado una vez con el modelo afectado" | PAT-38 |
| Lista de decisiones post hoc incompleta frente al método | G-C7, P-MM1 | "Otras tres decisiones siguieron a resultados de validación" (omite la sensibilidad del estado final) | PAT-140 |
| GAP que niega un resultado o una decisión ya registrados | OC-2, G-T4 | "resultados del protocolo físico sobre los 13 pacientes de prueba" (ya corrido) | PAT-122 |
| Generalización que el mismo capítulo contradice | E-P3, G-T4 | "el único parámetro heredado de un modelo anterior es el límite de 0.05" | PAT-39 |
| Cifra que pierde su condición de medición al retomarse | G-T4 | "0.62 frente a 1.40 parches de solo banda" | PAT-31 |
| Recuento de sentido de sesgos que queda atrás de una corrección del registro | G-C7 | "El sentido del efecto está registrado para dos de las tres elecciones" | nuevo |
