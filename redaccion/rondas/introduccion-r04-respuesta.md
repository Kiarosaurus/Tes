# introduccion — r04 (corregir, alcance acotado) — respuesta del redactor

Alcance: solo `Objetivos de investigación`, `Justificación` y `Alcance y limitaciones / restricciones`.
No se tocaron el encabezado ni la Formulación del problema. Los títulos no cambian.

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; IMP = `docs/04-implicancias.md`.

Criterio de la ronda, según indicó el orquestador: para bajar la longitud, primero dividir párrafos, remitir al cap. 3 y quitar repeticiones. Solo se agregó texto donde un hallazgo lo exigía (T01, T02, guia-5).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| lint l. 7, 13, 21 (E-O1) | lint | ESCALADO (fuera de alcance) | Encabezado y Formulación, excluidos por la autora y DESFASADOS (#126). Dentro del alcance, el lint no marca nada |
| S01 | estilo | APLICADO (con otra forma) | Partir el párrafo donde proponía el revisor habría dejado una oración sola (E-O2). Por eso la oración de la variable dependiente pasa al párrafo inicial de Objetivos, que ya trata el papel de cada objetivo. Su segunda mitad se funde con la frase del Obj. 4 que decía lo mismo. El párrafo de falsabilidad abre ahora con "No todos los objetivos fijan de antemano qué resultado los haría fallar." Sale "Tampoco" |
| S02 | estilo | APLICADO | Se elimina "Así, la comparación no mide el ajuste ..." |
| S03 | estilo | APLICADO | "El segundo elemento es un muestreador ..., y el tercero, la codificación multiventana usada para generar, junto con la banda $B_{\delta}$" abre el párrafo siguiente |
| S04 | estilo | APLICADO | "identifican el endurecimiento del haz, la dispersión, el ruido y el efecto exponencial de gradiente de borde como las causas principales de las rayas del metal". Fuente: ficha `deman1999`, "the most important causes of metal streak artifacts" (Conclusiones, p. 695) |
| S05 | estilo | APLICADO (con otra forma) | "clasifican el sacro como dismórfico sobre radiografía simple, por rasgos como el ala sacra angulada y ascendente o los forámenes neurales superiores no circulares, sin exigir que estén todos presentes". Fuentes: ficha `gardner2010safezones`, Introducción p. 622 y M&M p. 623 ("plain radiographs", "The presence of all six dysmorphism criteria was not required"). No se escribe "seis criterios". La ficha registra que la Introducción enumera cinco y los Métodos dicen seis, y que los criterios son de Routt et al., que no está en `refs.bib` (PAT-6) |
| S06 | estilo | APLICADO | "Ese control excluyó a 11 de 34 pacientes con objetos no ortopédicos y a 7 de 57 sin objeto". Copiado de C3 l. 253 (y l. 52). Sin porcentajes |
| S07 | estilo | APLICADO | "..., de modo que esa exactitud no se asume y un control verifica el nivel S1 de cada caso. Ese control excluyó ...". El enlace viene de C3 l. 85 ("por lo que esa exactitud no se asume") y de la oración que le sigue, sobre el control de nivel |
| S08 | estilo | APLICADO | El párrafo se divide en "Las cifras principales del Objetivo~2 dependen ...", y sale "además". Queda un párrafo de 6 oraciones (fractura) y otro de 5 (segmentación, nivel S1, envolvente) |
| S09 | estilo | APLICADO | En la exclusión de XCIST queda solo "Esa validación tampoco cubre la síntesis (véanse las limitaciones)", y "corre" pasa a "se ejecuta". El detalle queda en las limitaciones de apariencia, donde se suma "sin cubrir el paso híbrido con imágenes clínicas" (C3 l. 221), que antes solo estaba en la exclusión |
| S10 | estilo | APLICADO | l. 46: "un autoencoder entrenado con TC". l. 62: "los autoencoders preentrenados examinados, incluido uno entrenado con TC". Según la ficha `guo2025maisi`, el latente de Guo et al. es el de su VAE (l. 9, 35) |
| T01 | traza | APLICADO | "Este trabajo prevé ejecutar, además, el protocolo de Peters et al. sobre las poses del muestreador, en un subconjunto de pacientes y según el plazo, como comparación para la apariencia". Fuentes: C3 l. 219 y 221 (subconjunto, \GAPDATO de implementación) e IMP #90. No se añade otra marca: el \GAPDATO de la implementación ya está en C3, y la contingencia de plazo tiene su \GAPDEC en las limitaciones de apariencia. El \GAPDEC que sigue ya no se apoya en un hecho cumplido. Corresponde a IMP #128.1, con la salvedad T01 que la autora ya anotó |
| T02 | traza | APLICADO | Obj. 4: "la viabilidad del corredor \GAPDEC{calibre con que SAP evalúa la viabilidad del corredor, que difiere entre la decisión que define SAP y la corrida del Objetivo~2}". Es el mismo GAP que C3 l. 189. En MAPA se anota que también está en la introducción |

## Hallazgos bajos

| Hallazgo | Decision | Detalle |
|---|---|---|
| S11 | APLICADO | "una utilidad que la escasez de volúmenes con metal anotados impide medir aquí" |
| S12 | APLICADO | "La segmentación ósea automática de la TC pélvica depende de volúmenes anotados" |
| S13 | APLICADO | "prevé ejecutar", "no se ha ejecutado", "que se ejecuta sobre". Dentro de los `\GAP` se conserva "corrida", porque es el nombre de la fila en MAPA |
| S14 | APLICADO (acotado) | "afirmaciones no verificadas sobre la física del artefacto o sobre las fuentes". Sale "la anatomía", porque ninguno de los tres supuestos es anatómico |
| S15 | APLICADO | "que, por diseño, trunca las rayas lejanas" |
| S16 | APLICADO | Sale "Por último" de la envolvente, que ahora cierra otro párrafo |
| S17 | APLICADO (con otra forma) | "formada por las series con navegación computarizada (navegada) y sin ella (convencional) de Zwingmann et al. en S1, el primer segmento del sacro. El muestreador no se ajustó a ellas." La glosa se integra, pero "sin haber ajustado" pasa a una oración corta para no superar 40 palabras (E-O1). El número de oraciones no baja |
| S18 | APLICADO | "En la simulación física, el protocolo físico de Peters et al. simula ..." |
| S19 | APLICADO | "cuyo error ya superaba el criterio" |
| guia-1 | APLICADO | "De esas ventanas, este trabajo solo aporta su empleo como codificación para generar. Ningún objetivo aísla la codificación ni la banda, porque el Objetivo~3 evalúa el sintetizador completo". Fuente: C3 l. 176, donde el ancho es un parámetro de diseño que no se varía |
| guia-2 | APLICADO | "tres desplazamientos de dominio, que limitan la transferencia de lo aprendido sobre metal real a los tornillos paramétricos" (C3 l. 263) |
| guia-3 | APLICADO | "fijó por escrito en su preinscripción". Para el segundo corredor se agrega la aposición "un corredor óseo cuyo nivel vertebral varía entre volúmenes" (C3 l. 164). En l. 58, "desplazamientos de dominio entre entrenamiento y síntesis" |
| guia-4 | NO APLICADO | Cambiar "componentes" de SAP solo en la introducción la separaría de C3 l. 189, que usa el mismo término (E-T1, E-R5). Se deja para decidirlo en todo el documento |
| guia-5 | APLICADO | Obj. 3: "... y con observaciones reales de artefacto \GAPDEC{métrica y análisis de la comparación con observaciones reales de artefacto}". Es el mismo GAP que C3 l. 215 |
| guia-6 | APLICADO en parte | "La síntesis opera en el dominio de imagen, por el veredicto del Objetivo~1, y solo regenera parches alrededor del implante: fuera de la región de generación $G$ copia el volumen de origen" (C3 l. 172). Ninguna fuente da la razón de trabajar por parches. Solo se dice lo que implica, y no se inventa la razón |
| guia-7 | APLICADO | Sale la generalización "el veredicto no se limita a una sola arquitectura". Queda el hallazgo acotado a "los autoencoders preentrenados examinados" (TM, Obj. 1). La cronología ya está en l. 46 |
| T03 | NO APLICADO | Es opcional. El párrafo remite a `sec:amenazas`, donde está la cita de Reilly et al. Se deja fuera para no alargar el párrafo |

## GAP

- Abiertos en la introducción: `\GAPDEC` +2. Los dos ya tenían fila en MAPA, y se anotó que también están aquí: el calibre de la viabilidad de SAP (T02) y la comparación con observaciones reales (guia-5). No hay filas nuevas.
- Cerrados: ninguno. `\GAPLIT`: ninguno, así que no hay candidatos nuevos.
- Totales de la sección según el lint: lit 0, dato 5, dec 16 (antes, 0/5/14).
- Lint: en el alcance, 0 altas y 0 medias. En el archivo, 0/3/1: las tres medias están en l. 7, 13 y 21, fuera del alcance. Compila en 67 páginas.

## Para la autora (escalados)

1. **Encabezado y Formulación (lint l. 7, 13 y 21):** siguen DESFASADOS (#126, #128.7).
2. **Siguen abiertas las preguntas de r03**, recogidas en #128.1 y #128.5: por qué hace falta un sintetizador aprendido si el protocolo físico se ejecutaría sobre las mismas poses, y por qué el trabajo se limita al tornillo iliosacro.
3. **(bajo) "Componentes" de SAP:** ¿las tres partes de SAP se siguen llamando "componentes" en todo el documento (cap. 3 incluido), o pasan a llamarse "medidas"?

Implicancias: sin implicancias nuevas sobre la tesis. T01 ya figura como salvedad en #128.1.

## Decisiones de redaccion

- Si dividir un párrafo sobrecargado deja una oración sola, esa oración pasa al párrafo cuya función comparte (aquí, el párrafo inicial de Objetivos). No queda como párrafo de una oración.
- En un resumen, un brazo o análisis del cap. 3 que no se ha implementado va en futuro de intención ("prevé ejecutar") y con sus condiciones (subconjunto, plazo). Nunca en presente de indicativo.
- En la introducción, *run* se traduce "ejecutar". "Correr" y "corrida" quedan solo dentro de los textos de GAP que ya tienen fila en MAPA.
- Para definir un término clínico por diferencia con lo normal, se nombran dos o tres rasgos concretos de la ficha. No se da un recuento que la ficha marca como inconsistente.
- La pieza que prueba el Objetivo 1 es siempre "el autoencoder" o "los autoencoders", nunca "un latente". "Espacio latente" queda para el espacio, no para el modelo.
