# Revision guia CS — capitulo3 — r06

Insumos leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§1 y §2),
`overleaf/secciones/capitulo3.tex`, `introduccion.tex` (para G-C4, G-T3, G-T5),
`capitulo3-r05-respuesta.md`, `capitulo3-r06-lint.md`, `paridad-r01-trazabilidad.md`,
`docs/04-implicancias.md` (#122, #123, #124, #130, #131, #132, #134, #136, #138, #139, #140),
`redaccion/ENCARGO_2026-10-04.md`.

Ningun hallazgo de r05 fue RECHAZADO (el unico rechazo de la ronda fue S12, de estilo), asi que no
hay re-aperturas. Las marcas GAP no se cuentan como hallazgo, **salvo cuando el texto del GAP afirma
algo falso** (declara no hecho lo que esta hecho y cerrado): ahi el criterio no queda salvado por la
marca y se reporta.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-C7, G-T4 | capitulo3.tex:263 | "las pelvis receptoras, sin fractura conocida, no reproducen": afirmacion falsa. El cribado de #132 hallo fractura en 20 de 30, y la amenaza de validez externa descansa en esa premisa | Reescribir el cierre con las cifras autorizadas: 20 de 30 (67 %) con fractura confirmada mas un caso dudoso aparte; 10 de 15 frente a 10 de 15, identicos. Reordenar el argumento: la fractura **acerca** la anatomia receptora a la poblacion donde el procedimiento existe (Tile B y C); lo que no puede afirmarse es que las poblaciones esten emparejadas (fractura incidental, no graduada, estado de reduccion desconocido). Declarar el lector: medico recien egresado (SERUM, sin especialidad) sobre laminas fijas |
| guia-2 | alta | G-C7, G-T4 | capitulo3.tex:253 | "La ausencia de fractura en esa cohorte no se verifico. Al menos un paciente ... tiene una fractura confirmada": estado pre-#132. La amenaza de validez interna subdeclara el confundidor que ya esta medido | Sustituir por el cribado completo con su grupo de comparacion: 10 de 15 estrechos frente a 10 de 15 controles; fractura sacra desplazada 7 de 15 frente a 2 de 15, p = 0.109, **sugerente no concluyente** (el matiz es obligatorio). No escribir 70 %, 73 % ni 21 de 30 |
| guia-3 | alta | G-T4, OC-2 | capitulo3.tex:52 | `\GAPDATO{cribado ciego de fractura ... preparado y no realizado}`: el GAP declara no hecho algo hecho y cerrado (#132), y la Seccion de datos deja sin caracterizar el confundidor principal de la cohorte | Eliminar el `\GAPDATO` y escribir el resultado en la caracterizacion de la cohorte, con las cifras autorizadas y el nivel de lectura declarado. Quitar su fila de la tabla de GAP de `redaccion/MAPA.md` |
| guia-4 | media | G-C1, G-C7 | capitulo3.tex:209, :253 | "el grado~0 es inalcanzable por anatomia y no por colocacion": #132 §5 retira esa atribucion causal (7 de 15 estrechos tienen fractura sacra desplazada). El analisis post hoc se justifica con una causa derogada | Escribir "inalcanzable por la anatomia receptora **tal como se presenta**" y anadir que una fraccion **no cuantificable** del estrechamiento puede ser patologia y no variabilidad normal. La cifra de #122 no se toca; solo su atribucion causal |
| guia-5 | media | G-T4, OC-2, P-MM3 | capitulo3.tex:91 | `\GAPDATO{revision de la autora de los 16 casos ...}` y "quedo condicionada a una revision pendiente": la revision esta hecha (#123, #131) y no reabrio el recorte. Patron PAT-116 y PAT-19 reinciden | Cerrar el GAP con lo evaluado: **16 de 16 revisados, 14 `ok`, 2 `fallo_ambos`, 0 `fallo_6mm`**; el recorte por defecto se mantiene. Atribuir la revision a "la autora con apoyo de un medico egresado (SERUM, sin especialidad)" (#131). El tratamiento de los dos fallos de segmentacion queda en `\GAPDEC` (bloque B7, bloqueado) |
| guia-6 | media | G-T4, OC-2 | capitulo3.tex:97 | `\GAPDEC{si se declara la segunda lectura ... 61 de 61 ...}`: la decision ya esta tomada (#124, opcion b) y #138 desbloquea nombrar la estructura. PAT-19 reincide | Cerrar el `\GAPDEC` con la frase de `main.tex:121`: acuerdo **61 de 61** y, en la misma oracion, los dos limites (el segundo lector es **la autora**, no un segundo clinico; solo los juicios de nivel son independientes, porque las notas se copiaron tras ver la coincidencia). Nombrar la **cresta sacra media** como la estructura que el revisor acepto como S1 y decir que la etiqueta `vertebrae_S1` la contiene por diseno |
| guia-7 | media | G-C7, G-C1 | capitulo3.tex:257, :83 | El marco se ancla "perpendicular al platillo superior de S1" (:83) pero se mide sobre el techo de la mascara `vertebrae_S1`, que puede ser la cresta sacra media (#138). Esa amenaza no esta en `sec:amenazas` ni como supuesto | Anadir en validez de constructo que el techo de la etiqueta y el platillo superior pueden no ser la misma superficie y que esa diferencia **no esta medida**, con `\GAPDATO`. Declararla como amenaza identificada, **no** como defecto demostrado ni como no-problema (#138 es ABIERTA) |
| guia-8 | media | P-MM3, G-T4 | capitulo3.tex:164 | "un segundo lector ciego a la profundidad medida": no identifica al lector, y el estandar de #124 obliga a decirlo cuando el lector es la autora | "una segunda lectura de la autora, ciega a la profundidad medida" (mismo criterio que `main.tex:121`) |
| guia-9 | media | G-T2 | capitulo3.tex:9, :101, :196 | "tornillo iliosacro" nombra al implante modelado, pero el corredor que se mide y se muestrea cruza **las dos** articulaciones sacroiliacas: es transiliaco-transsacro (#130, aplicado en `main.tex`) | Traducir la primera frase de *Implant geometry source* de `main.tex:117` en :9, :101 y :196. **No sustituir a ciegas**: siguen diciendo "iliosacro" las menciones de `reilly2003effect` (:263), `kaiser2014dysmorphism` y su umbral de 10 mm, y `smith2006iliosacral` (:189) |
| guia-10 | media | P-MM1, G-T2 | capitulo3.tex:56, :13 | El titulo "Validacion de la representacion multiventana" y "El Objetivo~1 **valida** si ..." presuponen el resultado de una compuerta cuyo veredicto fue negativo, y atribuyen a la codificacion multiventana lo que se descarto (la ruta latente). La introduccion ya titula ese objetivo "Evaluar si el autoencoder ..." | Retitular la seccion en los terminos del objetivo de la introduccion (p. ej. "Compuerta de representacion: evaluacion del autoencoder") y cambiar ":13" a "determina si". Decision de BITACORA §2 (2026-09-29, introduccion-r01): nunca "Validar"; PAT-45 reincide |
| guia-11 | media | G-T4, OC-2 | capitulo3.tex:38 | `\GAPDATO{el sintetizador no ha generado todavia ninguna muestra sintetica ...}`: el entrenamiento del Objetivo~3 corrio y #139 registra una muestra de un corte generada el 2026-10-05. El GAP se redacto sobre el estado inicial de la implicancia (PAT-11 reincide) | Reformular el GAP al estado vigente sin afirmar resultados (#134 y #139 son ABIERTAS, OC-3): no existe salida de la cadena completa ni corrida preinscrita, y la prueba de componente no es resultado del Objetivo~3. La saturacion con 47 pacientes y el numero de pasos quedan en `\GAPDEC` (bloque B1, B2, bloqueados) |
| guia-12 | media | G-T2, G-T1 | capitulo3.tex:97, :46, :52, :119 | "cribado" designa tres cosas: el cribado por HU (:46), la deteccion de tipo de implante (:97) y el cribado de fractura (:52). Ademas ":97" afirma "17 pacientes con un tornillo iliosacro detectado en el cribado" mientras ":119" declara que el filtro no afirma que los componentes sean tornillos iliosacros. PAT-14 reincide | Reservar "cribado" para el umbral de 2500~HU y nombrar las otras dos (revision tridimensional de tipo y cantidad; cribado ciego de fractura). En ":97", decir de que procedimiento sale la identificacion de esos 17 casos, para que no contradiga ":119" |
| guia-13 | baja | G-T2 | capitulo3.tex:44, :219 | "referencia de apariencia" y "referencia de mecanismo" usan para otros comparadores la palabra que BITACORA §2 (2026-09-30) reserva a la **referencia clinica**. PAT-14 reincide | Usar las formulas ya decididas: "para comparar la apariencia" / "como comparacion". "Marco de referencia" (Kaiser) y "referencias anatomicas" no entran en la restriccion |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | no cumple (guia-1, guia-3, guia-12: afirmaciones y GAP que el repositorio desmiente) |
| G-T2 | no cumple (guia-9, guia-12, guia-13) |
| G-T3 | cumple (los simbolos de difusion del cap. 1 se declararon propios para no chocar con $\epsilon$, $T$, $t$, $\alpha$ de este capitulo; $h$/$\epsilon$, $D$/$d$, $T$ como tramo evaluado, sin colision interna) |
| G-T4 | no cumple (guia-1 a guia-3, guia-5, guia-6, guia-8, guia-11) |
| G-T5 | cumple (el orden anunciado en :9 es el orden real de las siete secciones; cada seccion remite a la anterior con `\ref`) |
| G-T6 | cumple (sin claves nuevas en esta ronda; el lint no marca referencias ausentes) |
| G-C1 | no cumple (guia-4: la atribucion causal del analisis post hoc esta derogada; guia-7: supuesto del techo de la etiqueta S1 no declarado) |
| G-C2 | cumple con GAP (arquitectura, entrenamiento y muestreo del sintetizador en el `\GAPDEC` de :172) |
| G-C3 | cumple (hay afirmaciones de desempeno y existe `tab:diseno` con los tres objetivos evaluables) |
| G-C4 | cumple con GAP (:13 declara que los objetivos de la introduccion no coinciden con los cuatro de este capitulo; la pregunta de `introduccion.tex:21` lleva su propio `\GAPDEC` en :28) |
| G-C5 | cumple con GAP (variables y metricas en `tab:diseno`; la definicion operativa de la fraccion por zona de densidad queda en el `\GAPDEC` de :166) |
| G-C6 | cumple (tres brazos sobre la misma anatomia y las mismas poses, cohorte de sensibilidad, control de simulacion sin metal, semilla por caso) |
| G-C7 | no cumple (guia-1, guia-2, guia-7) |
| G-C8 | cumple (Wilcoxon pareado de una cola, TOST sobre el IC del 90 %, IC por remuestreo de pacientes, W1 sin inferencia y declarado como tal) |
| G-C9 | cumple con GAP (el protocolo fisico de Peters et al. es el mejor competidor disponible; su implementacion sigue en el `\GAPDATO` de :221 y su permanencia en el `\GAPDEC` de :225) |
| P-MM1 | no cumple (guia-10. Sigue abierto, escalado en r04 y pendiente de la autora en #127, el doble papel de la viabilidad del corredor: caracterizacion de cohorte en :91 y variable dependiente descriptiva en `tab:diseno`; no lo reporto como hallazgo nuevo por estar escalado) |
| P-MM2 | cumple (`fig:pipeline`, con la compuerta como caja previa a la cadena) |
| P-MM3 | no cumple (guia-5, guia-8: procedencia de los lectores. Los algoritmos no descritos (busqueda del eje, heuristica de referencias, ajuste del decodificador) si estan declarados con `\GAPDATO`) |

## Propuestas de criterio
Ninguna. Los tres defectos nuevos de esta ronda (GAP que niega un resultado existente, procedencia
de lector no declarada, cifra de una implicancia CERRADA que su propio cuerpo refuta) caen dentro de
G-T4 y P-MM3 tal como estan redactados, mas OC-2 y OC-3 de `overleaf/CLAUDE.md`.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una marca GAP declara no hecho algo que una implicancia CERRADA ya cerro, y el texto vecino queda en el estado anterior | G-T4, OC-2 | `\GAPDATO{cribado ... preparado y no realizado}` con el CSV lleno en disco | PAT-19 reincide (y PAT-116 en :91) |
| Una amenaza a la validez sostiene su argumento en una premisa que un experimento propio posterior desmiente | G-C7 | "las pelvis receptoras, sin fractura conocida, no reproducen" | nuevo |
| El GAP se redacta sobre el estado inicial de la implicancia y no sobre sus actualizaciones | G-T4 | "no ha generado todavia ninguna muestra sintetica" | PAT-11 reincide |
| Una lectura o juicio humano se declara sin decir quien lo hizo, dejando suponer un clinico | P-MM3, G-T4 | "un segundo lector ciego a la profundidad medida" | nuevo |
| Un titulo de seccion del bloque (c) usa "Validacion" para un objetivo cuyo veredicto fue negativo | P-MM1, G-T5 | "Validacion de la representacion multiventana" | PAT-45 reincide |
| Un sustantivo de procedimiento ("cribado", "referencia", "control") designa tres cosas distintas en el mismo capitulo | G-T2 | "tornillo iliosacro detectado en el cribado" | PAT-14 reincide |

alta=3 media=9 baja=1
