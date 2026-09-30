# introduccion — r01 (corregir, alcance acotado) — respuesta del redactor

Alcance: solo `Objetivos de investigación`, `Justificación` y `Alcance y limitaciones / restricciones`
(hoy l. 23-76). Encabezado (l. 1-17) y Formulación del problema (l. 19-21) sin tocar. Títulos sin
cambios. Siglas: MAR sigue definiéndose en Justificación; SAP en el Obj. 4.

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| lint l. 7, 13, 21 (E-O1, media) | lint | ESCALADO (fuera de alcance) | Encabezado y Formulación, excluidos por la autora. Siguen DESFASADOS (#126) |
| guia-1 | guia | APLICADO | "Los Objetivos 1 a 3 tienen ... una variable dependiente; el Objetivo 4 no tiene fila propia ..., porque su producto son las métricas que usan los Objetivos 2 y 3" (C3 l. 185) |
| guia-2 | guia | APLICADO | El primer párrafo ya no dice que los objetivos "corresponden a las piezas de la cadena". El Obj. 1 aparece como compuerta previa a la cadena (C3 fig. 1): evaluó la ruta latente y su veredicto llevó el Obj. 3 al dominio de imagen. Se agrega que el error de ida y vuelta de la codificación sin autoencoder no lo verifica ningún objetivo, con remisión al `\GAPDEC` de C3 §Sintetizador |
| guia-3 | guia | APLICADO + ESCALADO | Obj. 4: Wasserstein-1 queda como parte de la definición de SAP y "esa comparación se ejecuta en el Objetivo 2" (C3 l. 13 y tab:diseno). El `\GAPDEC` del Obj. 4 se amplía: "si la adopción de las métricas de Peters et al. cuenta como parte evaluable del objetivo" |
| guia-4 | guia | APLICADO + ESCALADO | Se agrega el eslabón que sí tiene fuente: las mismas condiciones de los datos impiden medir la utilidad (TM *Out of scope*; 00T punto 1). Que la coherencia deba establecerse *antes* de la utilidad no está en TM ni en 00T: `\GAPDEC` nuevo en Justificación |
| guia-5 | guia | ESCALADO | Poner la Justificación antes de la Formulación cambia el orden de subsecciones y toca la Formulación, que está fuera del encargo. Se agrega al `\GAPDEC` de l. 28 ("y decidir si la justificación la precede") |
| guia-6 | guia | APLICADO | La razón para excluir XCIST/CatSim viene de DEC 2026-09-07 (alternativa descartada: una reimplementación "cuya validación de artefactos metálicos se atribuya a `wu2022xcist`") y de la ficha `wu2022xcist` ("qualitative and semi-quantitative first-order evaluation", Validation p. 9; sin estudio de artefacto metálico). Se cita `\cite{wu2022xcist}` |
| guia-7 | guia | APLICADO | Glosas en la primera aparición: osteosíntesis ("dispositivos de fijación ósea, como tornillos y placas"; `CLAUDE.md` raíz); corredor óseo (`docs/03-glosario.md`); autoencoder (ficha `rombach2022latentdiffusion`, con cita); tornillo iliosacro ("el que une el ilion con el sacro"); S1 ("primer segmento del sacro", ficha `kaiser2014dysmorphism`, "first sacral segment"); *inpainting* (C3 §Sintetizador; fichas CLAIM y LGESynthNet); Wasserstein-1 (C3 ec. `eq:w1`). **2.5D solo se remite al marco teórico**: la única definición del repositorio (`diseno_A.md` §2.5D) está marcada `[SUPUESTO]` en un borrador sin congelar |
| S01 | estilo | APLICADO | "En su conjunto de evaluación, el metal se inserta en ubicaciones clínicamente significativas (*meaningful locations*), sin que el artículo describa la regla con que se eligen" (ficha `peters2025hybrid`: "inserted in meaningful locations", Discussion p. 9; la ficha anota que no hay regla ni criterio para "meaningful") |
| S02 | estilo | APLICADO | Título del Obj. 1: "Evaluar una representación multiventana mediante una compuerta (*Go/No-Go*)". C3 conserva "Validación de la representación multiventana" como título de sección; no es archivo de este encargo |
| S03 | estilo | APLICADO | Título del Obj. 4: "... y adoptar las métricas de apariencia de Peters et al."; cuerpo: "métricas de Peters et al." (BITACORA §2). "Protocolo físico" queda solo para el brazo |
| S04 | estilo | APLICADO + ESCALADO | Se eliminó la repetición de la oración de apertura. El nexo que propone el revisor ("antes de medir esa utilidad hace falta establecer ...") no tiene fuente: va como `\GAPDEC` (ver guia-4) |
| S05 | estilo | APLICADO | Se nombran los tres enfoques en la oración temática: simulación física, planificación quirúrgica determinista y síntesis de lesiones por difusión (TM *Recognized Gap*) |
| S06 | estilo | APLICADO | "... y este trabajo lee ese resultado como indicación de que lo que se reproduce es una distribución de poses y no una pose única" (BITACORA §2, lectura propia) |
| S07 | estilo | APLICADO | "El tercer enfoque ... no resuelve la apariencia del artefacto, porque este no queda dentro del implante" |
| S08 | estilo | APLICADO | La evidencia se separa: el error del umbral fijo cambia de dirección según el valor elegido (`\cite{xie2024implantsegmentation}`; ficha: la dirección del error depende del umbral, p. 10), y en la cohorte local 9 de 57 objetos metálicos alargados extraídos con 2500 HU aparecen fragmentados (DEC 2026-09-20 (2); #46, recuento por paciente: "Alargados: 57, de ellos 9 fragmentados"). Se dice "objetos metálicos alargados" y no "tornillos", porque así los cuenta #46. "Auditoría local" ya no aparece sin referente |
| S09 | estilo | APLICADO | Oración temática: "La justificación metodológica tiene dos partes: el muestreador no se construye con los datos contra los que se compara, y el veredicto negativo del Objetivo 1 aporta un hallazgo propio" |
| S10 | estilo | APLICADO | "El alcance queda acotado en cuatro puntos: la cohorte, el implante, el nivel sacro y la forma de la síntesis." Se quitó la salvedad repetida |
| S11 | estilo | APLICADO | Igual que guia-6: el ítem de XCIST/CatSim tiene ahora su razón, así que "cada uno por una razón distinta" se mantiene |
| S12 | estilo | APLICADO | "Gardner et al. reportan una zona segura de S1 menor en sacros dismórficos, pero recogen un estudio previo que no halló diferencia" (misma formulación que C3 l. 168) |
| S13 | estilo | APLICADO | "Dos supuestos y dos convenciones sostienen el diseño". Supuestos: dominio de imagen y serie navegada en S1. Convenciones: ancho de $B_{\delta}$ y escala de 2 mm (TM: "adopted here as a geometric convention") |
| S14 | estilo | APLICADO | Se agrega el efecto: una malreducción residual en la referencia clínica estrecharía sus corredores de una forma que las pelvis receptoras no reproducen, y una fractura no detectada los estrecharía por una causa distinta de la variabilidad anatómica (C3 l. 253, 263) |
| S15 | estilo | APLICADO | "... fractura confirmada por un médico sin especialidad" (#125; C3 l. 253). Igual que T04 |
| S16 | estilo | APLICADO | Dos oraciones, cada una con su efecto. Reconstrucción no reportada: pudo incluir una MAR del fabricante o una reconstrucción monoenergética, que cambian la apariencia del artefacto (`\cite{selles2024marreview}`, C3 l. 44), y por eso esas observaciones son referencia de apariencia y no verdad física. Protocolo 2D y para MAR: usarlo como referencia de síntesis exige una adaptación que no hereda su validación (C3 l. 221) |
| T01 | traza | APLICADO | Se borró "El orden de los objetivos también es el orden en que se decidieron". Queda solo lo que respalda DEC 2026-09-19: la compuerta se formuló para difusión latente con ControlNet, el Obj. 3 se reformuló después del veredicto y la regla no se modificó. Se integró al primer párrafo y desapareció el párrafo del orden |
| T02 | traza | APLICADO (con otra formulación) | Se quitó la atribución a McLaren et al. El criterio de viabilidad queda como "calibre del tornillo más una holgura radial tomada de" Kaiser et al. (C3 l. 89; BITACORA §2). No se usó la propuesta "procedimiento de medición de McLaren", porque C3 define el diámetro con su propio procedimiento (doble de la distancia libre mínima a la envolvente, l. 87) y solo dice que McLaren *emplea* un procedimiento reproducible: atribuirle la medición sería repetir PAT-6 |
| T03 | traza | APLICADO | "... su criterio de 25 HU es anterior a una exploración que incluía a los pacientes de prueba, y su regla operativa se escribió después de ella, pero antes de la prueba que decide (Sección `sec:obj1`)" (C3 l. 58 y 255). Se quitó del Obj. 1 la frase de la regla fijada antes, para no duplicarla |
| T04 | traza | APLICADO | Ver S15 |
| T05 | traza | APLICADO | La generalización se acota al protocolo revisado: "El protocolo de simulación física revisado, el de Peters et al., simula la formación del artefacto, pero coloca el metal al azar ..." (C3 l. 219: "simula la física de formación del artefacto"). No se cita CatSim/XCIST para "reproducen el mecanismo": la ficha `deman2007catsim` no trata metal (#8) |
| T06 | traza | APLICADO | "... cuyos cortes de 2 mm provienen de la literatura de tornillos pediculares \cite{gertzbein1990,mirza2003} y llegan a la fijación iliosacra a través de Smith et al. \cite{smith2006iliosacral}" (TM *Problem Statement*; fichas: Mirza "The thresholds reported in prior studies were used", p. 405; Smith "prior established classification methods ... pedicle screw", p. 236). No se atribuyen los cuatro grados a Gertzbein (#58) |

## Hallazgos bajos

| Hallazgo | Decision | Detalle |
|---|---|---|
| guia-8 | APLICADO | Ver T02 |
| guia-9 | APLICADO | Ver S09 |
| guia-10 | APLICADO | Ver S14 y S16 |
| S17, S18 | APLICADO | La salvedad "no se mide segmentación" queda en el objetivo general y en Justificación; se quitó del primer párrafo de Objetivos y del Alcance |
| S19 | APLICADO | "se restringe con el corredor óseo medido sobre cada volumen" |
| S20 | APLICADO | "es decir, su nivel en una escala ordinal de cuatro niveles" |
| S21 | APLICADO (con otra formulación) | "las zonas oscuras del endurecimiento del haz". No se usó "bandas oscuras" porque "banda" nombra a $B_{\delta}$ (PAT-14) |
| S22 | APLICADO | "inserción por copia y pegado" |
| S23 | APLICADO | "dependen de datos anotados" |
| S24 | APLICADO | Ver T05 |
| S25 | APLICADO | De Man et al. como sujeto; no se añadió "fuera de su contorno", que la ficha no dice |
| S26 | APLICADO | "el objeto generado induce fuera de su máscara" |
| S27 | APLICADO | "La contribución de este trabajo es ..." |
| S28 | APLICADO | "se compara con la referencia clínica" |
| S29 | APLICADO | Dos oraciones; "En las fuentes revisadas no hay un precedente ..." |
| S30 | APLICADO | "los espacios latentes preentrenados examinados, incluido uno entrenado con TC". No se usó "autoencoders evaluados", porque el latente de Guo et al. no se corrió: solo se examinó su rango (C3 l. 75) |
| S31 | NO APLICADO | Pasar a "DSC y HD95" dejaría las siglas atadas al encabezado, que está DESFASADO y se va a reescribir. Se revisa cuando se reescriba |
| S32 | APLICADO | "La comparación con el protocolo físico es la que puede contradecirlo" (misma formulación que C3 l. 261) |
| T07 | APLICADO | Ver S01 |
| T08 | APLICADO | Ver S08 (9 de 57, "objetos metálicos alargados") |
| T09 | APLICADO | "... y no está verificado que esas anotaciones estén disponibles localmente" (C3 l. 36; 00T punto 1) |
| T10 | ESCALADO | El texto no cambia. Discrepancia del repositorio, ya señalada en r00 §4.3: el `CLAUDE.md` raíz y la actualización de #116 dicen "insumo de implantes PENDIENTE DE DEFINIR", mientras DEC 2026-09-11 (#41) y 2026-09-20 D3 fijan el tornillo paramétrico |

## GAP

- Abierto, `\GAPDEC` (1): "por qué esa coherencia debe establecerse antes de medir la utilidad para segmentación, o si se justifica por sí misma" (Justificación).
- Ampliados (2): `\GAPDEC` de l. 28 (se suma decidir si la justificación precede a la Formulación); `\GAPDEC` del Obj. 4 (se suma si la adopción de las métricas de Peters et al. es evaluable).
- Cerrados: ninguno. `\GAPLIT`: ninguno, así que no hay candidatos nuevos.
- Totales en la sección, según el lint: lit 0, dato 3, dec 6.

## Para la autora (escalados)

1. **Nexo entre la necesidad y lo que se evalúa (guia-4, S04).** ¿Por qué hay que establecer la coherencia física y quirúrgica antes de medir la utilidad para segmentación? ¿O esa coherencia se justifica por sí sola? Ninguna fuente lo dice.
2. **Orden de la introducción (guia-5).** ¿La Justificación pasa antes de la Formulación del problema, para que el embudo quede como necesidad, luego brecha, luego problema y luego objetivos? Conviene decidirlo al reescribir la Formulación (#126).
3. **Objetivo 4 (guia-3).** ¿La adopción de las métricas de Peters et al. cuenta como parte evaluable del objetivo, o solo como una decisión de diseño?
4. **Insumo de implantes (T10).** ¿Se actualiza el `CLAUDE.md` raíz ("PENDIENTE DE DEFINIR") para que coincida con el tornillo paramétrico decidido el 2026-09-11 y el 2026-09-20?
5. **Encabezado y Formulación (lint l. 7, 13, 21).** Siguen fuera de alcance y DESFASADOS.

Implicancias: ninguna nueva sobre la tesis. Lo encontrado ya está en #8, #46, #125, #126 y #127.

## Decisiones de redaccion

- Objetivo cuyo resultado se desconoce o fue negativo: el título usa "Evaluar" o "Determinar si", nunca "Validar" (S02).
- En la introducción, la compuerta del Obj. 1 se presenta como "previa a la cadena" y no como una de sus piezas (igual que la fig. 1 del cap. 3).
- La distancia de Wasserstein-1 se atribuye como comparación al Obj. 2 y como definición al Obj. 4 (SAP), nunca como evidencia de ambos.
- Cuando un tipo de artefacto se describe junto a $B_{\delta}$, se dice "zonas oscuras" y no "bandas oscuras", porque "banda" queda reservada para $B_{\delta}$ (PAT-14).
- Un recuento de objetos metálicos extraídos por umbral se nombra como lo cuenta su fuente ("objetos metálicos alargados"), no como "tornillos".
- Viabilidad del corredor en la introducción: "calibre del tornillo más una holgura radial tomada de Kaiser et al." McLaren et al. no se citan como fuente del criterio ni de la medición.
- Supuestos y convenciones se enumeran por separado. Convención = valor fijado por este trabajo (ancho de $B_{\delta}$, cortes de 2 mm). Supuesto = afirmación sobre el mundo que no se verificó.
- Glosas de términos del dominio clínico en la introducción: una aposición corta en su primera aparición, con fuente del glosario o de la ficha. Si la única definición está en un borrador sin congelar (2.5D), se remite al marco teórico.
