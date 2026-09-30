# introduccion — r02 (corregir, alcance acotado) — respuesta del redactor

Alcance: solo `Objetivos de investigación`, `Justificación` y `Alcance y limitaciones / restricciones`
(hoy l. 23-80). Encabezado (l. 1-17) y Formulación del problema (l. 19-21) sin tocar.

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; DEC =
`docs/01-decisiones.md`; 00T = `docs/00-tesis.md`; GLO = `docs/03-glosario.md`; IMP = `docs/04-implicancias.md`.

**Cambio de título (Obj. 1).** Antes: "Evaluar una representación multiventana mediante una compuerta
(*Go/No-Go*)". Ahora: "Evaluar si el autoencoder de un modelo de difusión latente conserva los HU de una
codificación multiventana (compuerta *Go/No-Go*)". **Habría que alinear en el cap. 3** (no editado): el
título de sección `\section{Validación de la representación multiventana}\label{sec:obj1}` (C3 l. 56) y
la oración de C3 l. 13, "El Objetivo 1 valida si una representación de la TC conserva ...", que conserva
el verbo "valida" (PAT-45).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| lint l. 7, 13, 21 (E-O1, media) | lint | ESCALADO (fuera de alcance) | Encabezado y Formulación, excluidos por la autora; siguen DESFASADOS (#126). En el alcance, el lint no marca nada |
| guia-1 | guia | APLICADO | Nuevo título del Obj. 1, que nombra el objeto de la prueba (TM Obj 1: "HU to multi-window to VAE to HU"; C3 l. 58). Se añade un párrafo después de la lista: "El veredicto descartó la ruta latente, no la codificación multiventana, que el sintetizador sigue usando, ahora sin la etapa del autoencoder" (TM: "the latent route is abandoned"; C3 fig. 1 y l. 172) |
| guia-2 | guia | APLICADO (con otra formulación) | Se quita el recuento cerrado ("Dos supuestos y dos convenciones"). Supuestos y convenciones se separan en dos párrafos, sin total, con remisión a `sec:amenazas`. Se agregan el supuesto máscara-artefacto (C3 l. 180, 261), la convención de grados equiespaciados en $W_1$ (C3 l. 200, 261) y $h = 2\sigma$ con su `\GAPDEC` (C3 l. 158). Los valores declarados de la preinscripción quedan cubiertos por remisión a `tab:preinscripcion`. El traslado de los 2 mm se describe como "convención geométrica y supuesto explícito", como en TM y C3 l. 257 |
| guia-3 | guia | APLICADO | En el Obj. 4: "Esas métricas se diseñaron para evaluar la reducción de artefactos metálicos (MAR, ...), y usarlas para evaluar síntesis exige invertirlas", con el mismo `\GAPDEC` de C3 l. 215. La sigla MAR se define ahora aquí, que es su primera aparición en el orden del documento, y ya no en la Justificación |
| guia-4 | guia | APLICADO | En la Justificación: "Este trabajo solo aporta su uso como codificación para generar, y ningún objetivo aísla ese aporte, porque el Objetivo 3 evalúa el sintetizador completo" (tab:diseno, fila 3: la variable independiente es solo el brazo; ablaciones fuera de alcance, 00T punto 10). El error de ida y vuelta sin autoencoder se dice una sola vez, en el párrafo que sigue a la lista de objetivos |
| guia-5 | guia | APLICADO + ESCALADO | Se glosa la exclusión: "Retirar una a una las restricciones del muestreador para medir el efecto de cada una". Ninguna fuente dice cuáles serían esas restricciones (00T punto 10 y DEC 2026-09-17 B.1 no las enumeran; C3 l. 166: la densidad no condiciona el muestreo). Queda `\GAPDEC` nuevo |
| guia-6 | guia | APLICADO | Oración temática: "... produce a la vez una distribución clínica de poses del implante y la apariencia de su artefacto". La segunda: "Ninguno de los dos primeros produce esa distribución de poses". Así desaparece la contradicción con "optimizan una única trayectoria" |
| S01 | estilo | APLICADO | "Los objetivos son los cuatro que desarrolla el Capítulo ..., pero solo los Objetivos 2 y 3 son componentes de la cadena propuesta". El `\GAPDEC` de la Formulación pasa al final del párrafo |
| S02 | estilo | APLICADO | En el párrafo de apertura solo quedan la oración temática y el papel del Obj. 1 ("una prueba previa a la cadena") y del Obj. 4. Veredicto, reformulación y error de ida y vuelta pasan a un párrafo que sigue a la lista, cuando "compuerta", "autoencoder" e "ida y vuelta" ya están glosados en el Obj. 1 |
| S04 | estilo | APLICADO | "El criterio se aplica a 34 pacientes de prueba." |
| S06 | estilo | APLICADO | Se divide en dos oraciones y el cuerpo dice "Formalizar", igual que el título. Se aclara qué compara $W_1$: "la distribución de grados del muestreador y la referencia clínica" |
| S08 | estilo | APLICADO (con otra formulación) | "... compara la *streak amplitude*, que esa inserción no produce por construcción. Por sí sola, esa prueba no dice si las rayas generadas se parecen a las reales". La consecuencia es la de C3 l. 217. No se usa la propuesta "solo fallaría si el sintetizador no generara rayas", porque ninguna fuente la escribe. Ya no aparece "línea base" |
| S10 | estilo | APLICADO | Igual que guia-6 |
| S14 | estilo | APLICADO | "Por eso el veredicto no se limita a una sola arquitectura, y el Objetivo 3 responde a él sintetizando en el dominio de imagen" (TM Obj 1: "generalizes the outcome rather than being incidental to one architecture"; "Objective 3 responds by synthesizing in the image domain") |
| S15 | estilo | APLICADO | "La segunda es que ..." (sin "Además"). Se añade el efecto: si la revisión mostrara un fallo de la variante en los casos marcados, cambiarían sus diámetros de corredor y, con ellos, sus poses y grados de brecha (IMP #123: el `D_TS_max`, la pose base y los grados salen de ese recorte; "el efecto por caso puede ser grande"). Queda redactado como condicional, porque #123 dice que no se puede concluir que las cifras estén mal |
| S17 | estilo | APLICADO | "sirven para comparar la apariencia y no como verdad física"; "usarlo como comparación para la síntesis". "Referencia" queda solo para la referencia clínica |
| S18 | estilo | APLICADO (con otra formulación) | "... que sí valida su simulación de artefactos metálicos contra un fantoma físico, aunque en dos dimensiones y para MAR (véanse las limitaciones)" (C3 l. 221; TM: "Their validation compares simulations against a physical phantom"). Ahora se nombra la diferencia con XCIST: el protocolo tiene una validación en metal, y es en 2D |
| T01 | traza | APLICADO | "El marco multiventana proviene de trabajos de MAR, que aplican las ventanas a etapas de reconstrucción o a la función de pérdida y no a la codificación de la entrada \cite{wang2025adaptiveweighting,li2024}" (TM *Recognized Gap*; GLO aviso #24; ficha `li2024`: pérdida multiventana, entrada en un único rango) |
| T02 | traza | APLICADO | "Xie et al. reportan que esa segmentación, en cortes simulados, cubrió el implante en exceso" (TM C1: "over-coverage in simulated slices"; ficha, l. 29: la comparación con el umbral solo existe en datos simulados, Tabla 2). Se retira "cambia de dirección" |

## Hallazgos bajos

| Hallazgo | Decision | Detalle |
|---|---|---|
| guia-7 | APLICADO | Ver S02 |
| guia-8 | NO APLICADO | Ninguna fuente escribe el eslabón que se propone (que el volumen receptor conserva su anotación y que la máscara del implante se conoce). Deducirlo sería completar con conocimiento propio (OC-1). Se suma a la pregunta 1 para la autora |
| guia-9 | APLICADO | Ver T04 |
| S03 | NO APLICADO | El cap. 3 escribe "autoencoder" en redonda. Ponerlo en cursiva solo en la introducción rompería E-T1. Hay que decidirlo para todo el documento (se agrega a las preguntas) |
| S05 | APLICADO | "un tornillo iliosacro, que une el ilion con el sacro, modelado como cuerpo paramétrico y rígido" |
| S07 | APLICADO | "el Objetivo 4 no tiene variable dependiente propia" |
| S09 | APLICADO | Se unen las oraciones 5 y 6: "..., una utilidad que esas mismas condiciones de los datos impiden medir aquí (véase el alcance)" |
| S11 | APLICADO | Enumeración entre paréntesis |
| S12 | APLICADO | Ver T01. "El tercero es la codificación multiventana usada para generar ..."; "Este trabajo solo aporta su uso ..." |
| S13 | APLICADO | "no hay un precedente que fije con un valor numérico una banda de generación fuera de la máscara del implante" (GLO: "ninguna de las fuentes leidas define una banda peri-implante con valor numerico"). El matiz de TM sobre la extensión medida del artefacto no se agrega para no alargar: ya lo desarrolla el estado del arte |
| S16 | APLICADO | "En la colocación, las limitaciones conocidas son dos. La primera es que ..." |
| S19 | APLICADO | "cuyo nivel sacro Zwingmann et al. no declaran" |
| S20 | APLICADO | "aunque De Man et al. caracterizan sus mecanismos como no lineales y los aíslan modificando el sinograma" (ficha `deman1999` l. 134-138) |
| S21 | APLICADO | "... si se mantiene dentro del plazo (véanse las limitaciones)" |
| S22 | NO APLICADO | La oración es la segunda de las dos condiciones que TM *Out of scope* da para la exclusión ("only part of the published collection is held locally"; también C3 l. 36). Si se quita, el argumento de la exclusión queda cojo |
| S23 | APLICADO | Se quita el recuento 9 de 57, que no tiene lugar ni `\ref` en el documento. Ahora se remite a `sec:datos` (C3 l. 54: "Los tornillos extraídos con un umbral fijo de HU aparecen fragmentados"). Sin recuento, "tornillos" es el término de C3 y TM ("fragmentation of pelvic screws") |
| T03 | APLICADO | "En su evaluación, sobre conjuntos de pacientes clínicamente representativos, el metal se inserta en ubicaciones significativas (*meaningful locations*)" (ficha `peters2025hybrid`, fila l. 217) |
| T04 | APLICADO | "El segundo corredor bajo S1 queda fuera de esa comparación y solo se describiría ...; su eje está medido, pero el muestreo de poses en él no \GAPDATO{...}" (C3 l. 164) |
| T05 | NO APLICADO | La corrección propuesta es dejar la oración sin cita, como la da TM l. 46, salvo que la ficha la respalde. Así está hoy. Releer `selles2024marreview` exige pasar por `lector-papers`, que queda fuera del ciclo |

## GAP

- Abiertos en la introducción: 1 `\GAPDATO` (segundo corredor, fila ya existente en MAPA) y 3 `\GAPDEC`: inversión de las métricas de Peters (fila existente), $h = 2\sigma$ (fila existente) y restricciones que cubriría la ablación (**fila nueva**).
- Cerrados: ninguno. `\GAPLIT`: ninguno, así que no hay candidatos nuevos.
- Totales de la sección, según el lint: lit 0, dato 4, dec 9 (antes: 0/3/6).

## Para la autora (escalados)

1. **Ablaciones excluidas (guia-5).** ¿Qué restricciones del muestreador cubriría la ablación "restricción por restricción" que se declaró trabajo futuro? El muestreador vigente perturba el eje del corredor y no condiciona por densidad, y ni 00T punto 10 ni DEC 2026-09-17 las enumeran.
2. **Término "autoencoder" (S03).** ¿Se escribe en cursiva en todo el documento, o se traduce ("autocodificador (*autoencoder*)" en la primera aparición)? Hoy el cap. 3 y la introducción lo escriben en redonda. Conviene sumarlo a la tabla de términos fijos.
3. **Eslabón necesidad-evaluación (guia-8, y la pregunta 1 de r01 sigue abierta).** ¿Por qué un implante sintético aliviaría la escasez de volúmenes con metal anotados (por ejemplo, porque el volumen receptor conserva su anotación y la máscara del implante se conoce)? ¿Y por qué la coherencia se establece antes que la utilidad? Ninguna fuente lo escribe.
4. **Encabezado y Formulación (lint l. 7, 13, 21).** Siguen fuera de alcance y DESFASADOS (#126).
5. **Cap. 3, título de §`sec:obj1` y l. 13** (ver arriba): alinearlos con el nuevo título del Obj. 1.

Implicancias: ninguna nueva sobre la tesis. Lo encontrado ya está en #17, #121, #123 y #126 y en los GAP del cap. 3.

## Decisiones de redaccion

- Título de un objetivo de tipo compuerta: nombra el objeto que se prueba (el autoencoder) y lo que se conserva (los HU de la codificación), no la representación que la cadena mantiene (profundiza PAT-45).
- Supuestos y convenciones se presentan sin recuento cerrado, con remisión a `sec:amenazas` y a `tab:preinscripcion` para los valores declarados. Una afirmación que TM y C3 llaman a la vez convención y supuesto (el traslado de los 2 mm) se nombra con las dos palabras.
- Una contribución que ningún objetivo evalúa por separado se enuncia junto con esa condición: "ningún objetivo aísla ese aporte, porque ...".
- La sigla MAR se define en su primera aparición en el orden del documento. En la introducción hoy es el Obj. 4, ya no la Justificación.
- "Referencia" se reserva para la referencia clínica. Para las observaciones reales y para el protocolo físico se dice "para comparar la apariencia" o "como comparación".
- Un recuento propio que no tiene sección ni `\ref` en el documento no se cita en la introducción: se remite a la sección que describe el hallazgo sin cifra.
- Cuando la introducción resume un tramo que el cap. 3 marca con GAP, lleva el mismo GAP (evita PAT-31). Así se hizo con el segundo corredor, $h = 2\sigma$ y la inversión de las métricas.
