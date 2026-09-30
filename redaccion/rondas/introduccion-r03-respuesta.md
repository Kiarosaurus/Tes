# introduccion — r03 (corregir, alcance acotado) — respuesta del redactor

Alcance: solo `Objetivos de investigación`, `Justificación` y `Alcance y limitaciones / restricciones`
(hoy l. 23-82). No se tocaron el encabezado (l. 1-17) ni la Formulación del problema (l. 19-21).

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`; GLO = `docs/03-glosario.md`.

Cambio de título: la cuarta exclusión pasa de "Estratificación por fenotipo sacro" a "Estratificación por
dismorfismo sacro" (S10, guia-7). El párrafo de la contribución se dividió en dos (S08).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| lint l. 7, 13, 21 (E-O1, media) | lint | ESCALADO (fuera de alcance) | Están en el encabezado y en la Formulación, que la autora excluyó; siguen DESFASADOS (#126). Dentro del alcance, el lint no marca nada |
| S01 | estilo | APLICADO | "Su regla operativa se escribió después de una exploración que incluía a los pacientes de prueba y que ya había quedado por encima del criterio, pero antes de la prueba que decide. El criterio de 25~HU es anterior a esa exploración y no se movió" (C3 l. 58, l. 255). Queda en dos oraciones para no pasar de 40 palabras (E-O1) |
| S02 | estilo | APLICADO | "cuatro tareas, cada una por una razón distinta" |
| S03 | estilo | APLICADO | "cuyos límites de grado, de 2~mm de ancho, provienen de ..." (C3 l. 194, 257) |
| S04 | estilo | APLICADO | "El uso de varias ventanas de HU proviene de trabajos de MAR, que las aplican a ..." |
| guia-1 | guia | ESCALADO | Ninguna fuente (TM, 00T, DEC, IMP) dice qué le falta a la simulación física para prescindir de un sintetizador aprendido. Al final de l. 54 se añade el hecho que plantea la pregunta: "Este trabajo corre, además, el protocolo de Peters et al. sobre las poses del muestreador, como comparación para la apariencia" (C3 l. 219), seguido de `\GAPDEC{por qué hace falta un sintetizador aprendido ...}`. No se propone ninguna razón (costo, datos de proyección): completarla sería inventar (regla 1) |
| guia-2 | guia | APLICADO | Se acota el primer elemento: "como máscara de síntesis, que evitan segmentar con un umbral fijo de HU el metal que se coloca". Se añade: "El entrenamiento del sintetizador sí usa máscaras umbralizadas de metal real, y su diferencia con el cilindro paramétrico es uno de los desplazamientos de dominio del sintetizador" (C3 l. 178, 182), y la cláusula de PAT-49: "Ningún objetivo aísla este aporte, porque ningún brazo de comparación coloca geometrías extraídas por umbral" (DEC 2026-09-11 #41; C3 l. 219, sec:geometria) |
| guia-3 | guia | APLICADO | Sin recuentos cerrados ("son dos", "son tres"). Se abre con "Las limitaciones se resumen aquí por componente, y la Sección~\ref{sec:amenazas} las discute en detalle", igual que la decisión de r02 para supuestos. En la colocación se agregan la falta de exactitud publicada para S1 de TotalSegmentator (C3 l. 85, 263), el desequilibrio por grupos del control de nivel, con su efecto (C3 l. 253), y la envolvente que podría ocupar el canal sacro, con el mismo `\GAPDATO` de C3 l. 257. En la apariencia se agregan los tres desplazamientos de dominio (C3 l. 182), con el mismo `\GAPDEC` para los dos no cuantificados, y la truncación de rayas, que la comparación con el protocolo físico no puede evaluar (C3 l. 261) |
| guia-4 | guia | APLICADO | En el Obj. 4: "SAP reúne tres componentes (Sección~\ref{sec:sap}): el grado de brecha cortical de cada pose y la viabilidad del corredor, definidos en el Objetivo~2, y la fracción por zona de densidad ósea" (C3 l. 189). La fracción lleva el mismo `\GAPDEC` que C3 l. 166 (decisión 2026-09-30, PAT-31). Se añade que solo los grados se comparan con la referencia clínica y que los otros dos componentes se reportan de forma descriptiva (C3 l. 189) |
| guia-5 | guia | APLICADO en parte + ESCALADO | La glosa "como tornillos y placas" se conserva, porque define osteosíntesis (`CLAUDE.md` raíz). El objetivo general la acota: "El único implante que se sintetiza es un tornillo iliosacro". En el alcance se dice el hecho verificable: "La referencia clínica y el marco de Kaiser et al. se refieren a tornillos iliosacros" (TM l. 52; ficha `kaiser2014dysmorphism`, "for passage of an iliosacral screw"). DEC #41 fija la geometría paramétrica, pero no da la razón del tipo de implante. Por eso se pone `\GAPDEC{razón declarada para restringir el implante al tornillo iliosacro y dejar fuera placas y otros tornillos}`, sin presentar esa coincidencia como el motivo |

## Hallazgos bajos

| Hallazgo | Decision | Detalle |
|---|---|---|
| S05 | APLICADO | "... no forma parte de este objetivo; el alcance delimita ambas restricciones". Se quita "queda para un trabajo futuro" |
| S06 | APLICADO | "en ubicaciones que el artículo llama pertinentes (\emph{meaningful locations}), sin que describa la regla" (ficha `peters2025hybrid`, fila l. 217) |
| S07 | APLICADO | "... de que el muestreador ha de reproducir una distribución de poses" |
| S08 | APLICADO | El párrafo se divide. El segundo empieza en "El tercer elemento ...", y la oración sobre la falta de precedente para $B_{\delta}$ va justo después |
| S09 | APLICADO | "... porque ninguna de las fuentes revisadas reporta para él una distribución ordinal clínica. Su eje está medido, pero el muestreo de poses en él no se ha corrido \GAPDATO{...}" |
| S10 | APLICADO | Nuevo título y última oración: "Por eso el muestreador no estratifica por dismorfismo y mide, en cambio, ..." |
| S11 | APLICADO (con otra formulación) | "Además de los valores declarados ..., el diseño fija otras convenciones". **No** se usa "cuatro convenciones", que es lo que proponía el revisor, porque reintroduce el recuento cerrado que r02 retiró (BITACORA §2, 2026-09-30) |
| S12 | APLICADO | "La cuarta fija la escala de las perturbaciones del eje" (C3 l. 261) |
| S13 | APLICADO | "estrecharía los corredores de sus pacientes". Se añade el efecto con respaldo en C3 l. 209: en un corredor más estrecho que el tornillo de medición, el eje ya perfora y el grado 0 es inalcanzable por anatomía. "Por eso ambas diferencias pueden mover la distancia de Wasserstein-1 sin que intervenga el muestreador". El texto usa el modal y no afirma en qué sentido se mueve la distancia |
| S14 | APLICADO | "o si su comparación decisiva es la de equivalencia" |
| S15 | APLICADO | l. 52: "Liu et al.~\cite{...} publican anotaciones óseas para 14 de los 75 ... y dejan sin anotar los 61 restantes". También en l. 70 |
| guia-6 | APLICADO | El protocolo adoptado "corre sobre ese mismo simulador, publica sus métricas y valida su simulación ... contra un fantoma físico. Esa validación es en dos dimensiones, para MAR y sin cubrir el paso híbrido con imágenes clínicas, así que tampoco la opción adoptada llega validada para síntesis" (C3 l. 219, 221) |
| guia-7 | APLICADO en parte | Serie navegada: "los tornillos se colocaron con navegación computarizada; en la convencional, sin ella" (ficha `zwingmann2009navigated`, título). Dismorfismo: "Gardner et al. describen el sacro dismórfico por un conjunto de rasgos radiográficos que difieren de los del sacro normal" (ficha `gardner2010safezones`, Introducción p. 622). "Cortical" queda sin glosa: GLO define la brecha cortical, pero no la cortical, y ninguna ficha revisada la define |
| guia-8 | APLICADO | En l. 46: "También después del veredicto se examinó, con la misma regla y sobre los mismos pacientes de prueba, un latente entrenado con TC (Sección~\ref{sec:amenazas})" (TM Obj 1: "examined next, under the same rule and on the same held-out patients"; C3 l. 255) |
| guia-9 | APLICADO | Ver S13 |
| T01 | APLICADO | "... no lo verifica ningún objetivo \GAPDEC{error de ida y vuelta de la codificación multiventana sin autoencoder, pendiente de la preinscripción del sintetizador} (Sección~\ref{sec:sintetizador})" |

## GAP

- Abiertos en la introducción. `\GAPDATO` +1: envolvente y canal sacro, que ya tenía fila en MAPA (se anota "También en introduccion"). `\GAPDEC` +5. Tres ya tenían fila y se anotan: la fracción por zona de densidad, el error de ida y vuelta (fila de la preinscripción del sintetizador) y la métrica de los desplazamientos de dominio. Dos son **filas nuevas**: por qué hace falta un sintetizador aprendido (guia-1) y la razón de restringir el implante al tornillo iliosacro (guia-5).
- Cerrados: ninguno. `\GAPLIT`: ninguno, así que no hay candidatos nuevos.
- Totales de la sección, según el lint: lit 0, dato 5, dec 14 (antes 0/4/9).
- Lint: dentro del alcance, 0 altas y 0 medias. En el archivo, 0/3/1, las tres medias en l. 7, 13 y 21, fuera de alcance. Compila (67 páginas).

## Para la autora (escalados)

1. **Sintetizador aprendido frente a simulación física (guia-1).** El protocolo físico de Peters et al. se corre sobre las mismas poses del muestreador. ¿Qué le falta a esa combinación para que haga falta un sintetizador por difusión? Por ejemplo: costo por muestra, que no necesite datos de proyección, validación solo en 2D o escala del aumento de datos. Solo cuenta una razón que usted haya decidido; ninguna fuente del repositorio la escribe.
2. **Tipo de implante (guia-5).** ¿Por qué el trabajo se limita al tornillo iliosacro y deja fuera las placas y otros tornillos? ¿Es porque la referencia clínica (Zwingmann et al.) y el marco de Kaiser et al. solo existen para ese tornillo, o hay otra razón?
3. **Encabezado y Formulación (lint l. 7, 13, 21).** Siguen fuera de alcance y DESFASADOS (#126).

Siguen abiertas las preguntas de r02 (ablación, "autoencoder" en cursiva, eslabón necesidad-evaluación y título de `sec:obj1` en el cap. 3).

Implicancias: ninguna nueva sobre la tesis. guia-1 y guia-5 son decisiones de redacción del argumento, ya registradas como GAP en MAPA; no cambian el alcance ni los datos.

## Decisiones de redaccion

- Las limitaciones se presentan como los supuestos: sin recuento cerrado, agrupadas por componente (colocación, apariencia) y con remisión a `sec:amenazas`. Cada limitación que se resume lleva su efecto sobre el resultado (PAT-38) y el mismo GAP que tiene en el cap. 3 (PAT-31).
- Cuando una tensión de la justificación se debilita por un hecho del propio diseño (p. ej., el protocolo físico se corre sobre las poses muestreadas), se enuncia el hecho y se marca `\GAPDEC` con la pregunta. No se inventa la razón.
- Una coincidencia verificable que podría explicar una restricción de alcance (la referencia clínica y el marco solo cubren tornillos iliosacros) se dice como hecho, sin "por eso", y la razón declarada queda en `\GAPDEC`.
- Un término del cap. 3 que la introducción no ha definido ("calibre de medición", "control de nivel") se reemplaza por una descripción corta ("el tornillo con que se mide la brecha", "el control que verifica el nivel S1 de cada caso").
- "Tareas" es el nombre de las exclusiones de alcance. "Componentes" queda para las piezas de la cadena y para los objetos metálicos (PAT-14).
- Los límites de la escala de brecha son "límites de grado, de 2 mm de ancho", nunca "cortes" (en TC, "corte" es un corte tomográfico).
