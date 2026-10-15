# Revision guia CS — introduccion — r07

Contexto: encargo `redaccion/ENCARGO_2026-10-15.md` (introduccion: retirar el `\GAPDEC` de #90 y actualizar el
resultado del Obj. 3 segun DEC 2026-10-15). Ademas del encargo, revise todo `introduccion.tex`. El texto es el mismo que
se reviso en r06: esa ronda no tuvo respuesta del redactor, asi que sus hallazgos siguen abiertos. Aqui se reportan de
nuevo, actualizados con DEC 2026-10-15. Ninguno fue RECHAZADO, asi que no hay re-aperturas. Los hallazgos del
encabezado (l. 1-21), que el encargo excluye, van con severidad baja para que el redactor los escale.

Lei tambien, para los cruces: `capitulo3.tex` (l. 36-38, 224-250, 323-381, 425-463), `capitulo2.tex` l. 104-106,
`conclusiones.tex` (esqueleto), DEC 2026-10-13, 2026-10-14 (1, 2) y 2026-10-15 (ptos 1-22), y BITACORA §1-§2.
`capitulo3` esta en correccion paralela (r22). Sus numeros de linea son los del archivo actual.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-A8 | introduccion.tex:48, :56, :80 | Patron PAT-122 reincide. :48 da el margen como "aún sin medir", pero cap3:379 lo da medido (196.3 HU). :56 ("Si alcanza la equivalencia...") y :80 ("es la que puede contradecirlo") siguen en condicional, aunque la prueba ya se ejecutó. Ademas, la introduccion no dice que desenlace haria fallar el Obj. 3. DEC 2026-10-15 pto 15 ya lo fija: equivalencia, no equivalencia o no concluyente. El confirmatorio es solo el modelo evaluado, y para v1 el desenlace es no concluyente, por debajo del protocolo fisico. Esa lectura se fijo despues de ver la prueba de v1, y el texto no lo dice (riesgo PAT-13). | En :48, dar $\Delta$ medido en validacion. Agregar los tres desenlaces y decir que su distincion es posterior al resultado de v1; la regla de equivalencia es anterior. Dar el desenlace (no concluyente, sintetizador por debajo) con su condicion: titanio, 13 pacientes, eje del corredor (PAT-31), con remision al cap. 4. En :56 y :80, pasar a hecho. El Obj. 3 va en parrafo propio, porque :48 ya tiene 7 oraciones (PAT-58). |
| guia-2 | media | G-A10, G-T2 | introduccion.tex:90 | Patrones PAT-122, PAT-11 y PAT-133 reinciden (encargo). (1) El `\GAPDATO` dice que no hay resultado del Obj. 3 "porque el modelo final no está elegido". Pero el punto de control esta elegido (cap3:240), y la corrida final esta evaluada (cap3:38, :248). (2) El `\GAPDEC` de la contingencia #90 sigue abierto, aunque #90 esta CERRADA (DEC 2026-10-15 pto 13). (3) "Modelo final" choca con "estado final", que en el cap. 3 es el candidato descartado (PAT-14). (4) La version 2 no se menciona. | Retirar el `\GAPDEC`. Decir en prosa que el Obj. 3 tiene resultado (remision a guia-1) y usar "modelo evaluado". Dejar `\GAPDATO` solo para lo pendiente: contraste de realismo (cap3:38) y version 2 en prueba. De la version 2, una frase: posterior y exploratoria, no reemplaza al modelo evaluado (DEC 2026-10-14 (2)). |
| guia-3 | media | G-A7, G-C4 | introduccion.tex:56 (y :13, :41) | :56 dice que el protocolo fisico se ejecutara "sobre las poses del muestreador ... y según el plazo". Segun cap3:327 y :457, el Obj. 3 se evaluo sobre el eje del corredor sin perturbar y sus resultados no cubren las poses del muestreador. :13 y :41 presentan la cadena como un muestreador que entrega la pose al sintetizador, y ninguna oracion lo aclara (afin a PAT-49). La razon ya esta decidida (DEC 2026-10-15 pto 9: aislar la apariencia de la colocacion, y el coste del protocolo fisico). Tambien hay un analisis exploratorio sobre 5 poses del muestreador, solo con el sintetizador, todavia sin resultado. cap2:106 lleva la misma oracion desfasada: la bisagra G-B10 se mantiene solo si ambos se corrigen igual. | Poner el hecho y la razon del pto 9. Decir en una frase que la comparacion de equivalencia no cubre las poses del muestreador. Nombrar el analisis exploratorio con `\GAPDATO` para su resultado. Avisar al orquestador del cruce con cap2:106. |
| guia-4 | media | G-A8 | introduccion.tex:32 | Patron PAT-45 reincide (de r06, sin respuesta). El objetivo general pide una cadena "que genere ... con coherencia física y quirúrgica", es decir, presupone el resultado. Con el desenlace no concluyente del Obj. 3, la conclusion (G-D1) no podra contestarle con "no" o "en parte". | "... y evaluar la coherencia física y quirúrgica de lo que genera", como :15 y la pregunta de :21. |
| guia-5 | media | G-A10, G-A7 | introduccion.tex:88 | Las limitaciones de la apariencia omiten las amenazas del cap. 3 que condicionan la lectura del resultado obtenido. (a) La metrica no distingue rayas de textura sin direccion, y la estructura de raya no esta medida (cap3:443). (b) El protocolo fisico exagera frente a los tornillos reales, y el percentil 95 del sintetizador queda por debajo (cap3:453). Es decir, el comparador tampoco es la verdad, y la introduccion solo lo dice de las observaciones reales. (c) Hay asimetrias entre brazos medidas en #186 (cortes, piso de ruido) que la DEC 2026-10-15 trata con sensibilidades (ptos 17-18). | Una o dos oraciones con (a) y (b) y remision a `sec:amenazas` para (c), sin cifras de #186 en la introduccion. Si se enuncia el resultado, hacerlo en *streak amplitude*, no en "rayas más débiles" (PAT-61). |
| guia-6 | media | G-A10 | introduccion.tex:90 | Patron PAT-31 reincide. "El segundo se mide en la evaluación del sintetizador" presenta la medida como hecha. DEC 2026-10-15 pto 5 decide medir la costura en la sintesis sobre pelvis sin metal, con los dos brazos, pero la medida es posterior y aun no tiene resultado (regla del encargo). Hasta ahora solo se midio en la reconstruccion de implantes reales (cap3:228). | Decir donde se midio y que en la condicion donde actua se medira (decision posterior), con `\GAPDATO` para el resultado. |
| guia-7 | baja | G-A7, G-C4 | introduccion.tex:41 | El Obj. 3 enumera tres comparaciones y no nombra la reconstruccion de implantes reales. Esa evaluacion es descriptiva, ya se ejecuto (cap3:38) y es fila de `tab:diseno`. | Una clausula: "y, de forma descriptiva, con la reconstrucción de implantes reales (Sección~\ref{sec:ap-reconstruccion})". |
| guia-8 | baja | G-A8 | introduccion.tex:48 | La falsabilidad del Obj. 3 no dice que $\Delta$ lo fija la variabilidad entre semillas del propio sintetizador (cap3:381). Un sintetizador mas variable aprueba con mas facilidad, y las tres elecciones empujan hacia la equivalencia (cap3:433). Debilita la evidencia que podria hacer fallar el objetivo. | Una clausula con remision a `sec:ap-analisis` y `sec:amenazas`. Si no cabe, va en el parrafo nuevo de guia-1. |
| guia-9 | baja | G-A10 | introduccion.tex:88 | La limitacion del truncamiento por $B_{\delta}$ no recoge el acotamiento de cap3:445. En componentes del tamano de un tornillo, la banda de 12 mm contiene el artefacto real medido. Para placas y protesis no esta acotado. | Clausula con esa condicion y remision a `sec:v2`, o solo la remision. |
| guia-10 | baja | G-T2 | introduccion.tex:5 | Patron PAT-14 reincide (encabezado, escalado). "Bandas oscuras" usa "banda", que esta reservada a $B_{\delta}$ (BITACORA §2, 2026-09-29). "Escasez de fotones" no es el termino fijo "inanición de fotones". | "Zonas oscuras"; "inanición de fotones". |
| guia-11 | baja | G-A5 | introduccion.tex:19-21 | Bajo "Formulación del problema" solo hay una pregunta sobre "la cadena propuesta". La tension esta en :9 y :54. La pregunta y el orden los decidio la autora (DEC 2026-10-08 pto 24). Esta fuera del encargo y se escala. | Antes de la pregunta, una oracion con la tension de :54, o una remision a la justificacion computacional. |

alta=0 media=6 baja=5

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP. El cap. 4 es esqueleto, asi que las remisiones al "capítulo de resultados" llegan a un capitulo vacio |
| G-T2 | no cumple (guia-2, guia-10) |
| G-T3 | cumple: $M$, $B_{\delta}$, $G$, $\Delta$ y $W_1$ se usan igual que en el cap. 3 |
| G-T4 | no evaluable (lo revisa `auditor-trazabilidad`) |
| G-T5 | cumple (orden decidido, DEC 2026-10-08 pto 24) |
| G-T6 | no evaluable (lo revisa `auditor-trazabilidad`) |
| G-A1 | cumple: planteamiento (:3-9), revision preliminar (:5-11, :54-58), proposito (:13, :32), pregunta (:21) |
| G-A2 | cumple |
| G-A3 | cumple: la tension esta en :9 y :54 |
| G-A4 | cumple (:5, :56) |
| G-A5 | cumple a medias (guia-11) |
| G-A6 | cumple |
| G-A7 | no cumple en el cruce con el cap. 3 (guia-3, guia-5, guia-7) |
| G-A8 | no cumple (guia-1, guia-4, guia-8). El Obj. 2 no tiene regla de fallo, por decision de la autora, y asi se declara. El Obj. 4 es de definicion declarada |
| G-A9 | cumple |
| G-A10 | cumple a medias (guia-2, guia-5, guia-6, guia-9). Las cuatro tareas excluidas y los cuatro puntos de alcance estan cubiertos (PAT-44 no reincide) |
| G-B10 | cumple: cap2:106 enuncia la misma tension con las mismas palabras. Riesgo: arrastra la misma oracion desfasada (guia-3) |
| G-C4 | no cumple en el cruce (guia-1, guia-3, guia-7) |
| G-D1, G-D2 | no evaluable: conclusiones es esqueleto. guia-4 condiciona G-D1 |

## Propuestas de criterio
- Bloque (a), repetida de r06: cuando un objetivo ya tiene resultado, la introduccion dice como se lee respecto del
  objetivo (cumplido, no cumplido, no concluyente) y si esa lectura se fijo antes o despues del resultado.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Prosa o GAP que niega una medicion o ejecucion ya registrada | G-A8, G-A10 | "un margen $[-\Delta, +\Delta]$, aún sin medir"; "el modelo final no está elegido" | PAT-122 |
| GAP sobre una implicancia redactado en su estado inicial, aunque esta CERRADA | G-A10 | `\GAPDEC` de la contingencia de plazo (#90, CERRADA) | PAT-11 |
| Medida decidida y aun sin resultado redactada como ya tomada | G-A10 | "el segundo se mide en la evaluación del sintetizador" | PAT-31 |
| Lectura de desenlaces fijada despues del resultado, presentada sin decir que es posterior | G-A8 | (riesgo al aplicar DEC 2026-10-15 pto 15 en :48) | PAT-13 |
| Objetivo general con el resultado como propiedad del producto | G-A8 | "que genere implantes ... con coherencia física y quirúrgica" | PAT-45 |
| "Banda" fuera de $B_{\delta}$ | G-T2 | "bandas oscuras, regiones brillantes" | PAT-14 |
