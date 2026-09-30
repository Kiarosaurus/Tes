# Revision guia CS — introduccion — r03

Alcance acotado por la autora: `introduccion.tex` l. 23-80 (Objetivos, Justificacion, Alcance y
limitaciones). Encabezado (l. 1-17) y Formulacion del problema (l. 19-21) quedan fuera de alcance (#126);
los hallazgos del lint en l. 7, 13 y 21 tambien. Secciones cruzadas leidas: `capitulo3.tex` (completo),
`capitulo2.tex` (esqueleto) y `conclusiones.tex` (plantilla). Respuesta r02 leida: guia-8 (eslabon
necesidad-evaluacion) quedo NO APLICADO porque ninguna fuente lo escribe, y no se reabre. Los hallazgos
guia-1 a guia-7 y guia-9 de r02 estan resueltos.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-A3, G-A4 | introduccion.tex:54 | La tension es que "ninguno de los tres enfoques produce a la vez" una distribucion clinica de poses y la apariencia del artefacto. Pero la propia tesis corre el protocolo fisico de Peters et al. sobre "las mismas poses de implante" del muestreador (cap3 l. 219), asi que simulacion fisica mas muestreador ya producen las dos cosas. En el alcance revisado nada dice por que hace falta un sintetizador aprendido en lugar de simular sobre las poses muestreadas. Un comite lo preguntara. | En l. 54-56, decir que le falta a la simulacion fisica para este uso (datos de proyeccion o de adquisicion no disponibles, validacion 2D y para MAR, costo), con fuente del repositorio, o `\GAPDEC` si no esta escrito. |
| guia-2 | media | G-A10, G-A7 | introduccion.tex:58 | Patron PAT-51 reincide. El primer elemento de la contribucion, la geometria parametrica, "evita segmentar el metal con un umbral fijo de HU", pero el sintetizador se entrena con mascaras obtenidas con el umbral fijo de 2500 HU (cap3 l. 178), y esa diferencia es un desplazamiento de dominio declarado (cap3 l. 182). Patron PAT-49 reincide: ningun objetivo aisla este elemento, y a diferencia del tercero, no se dice. | Acotar la afirmacion a la mascara de sintesis y mencionar que en el entrenamiento se usa el umbral. Agregar la misma clausula que el tercer elemento ("ningun objetivo aisla ese aporte, porque ..."). |
| guia-3 | media | G-A10 | introduccion.tex:78, 80 | Hay recuentos cerrados ("las limitaciones conocidas son dos"; "las limitaciones son tres") y el cap. 3 declara otras que el lector de la introduccion no ve. En colocacion: la publicacion de TotalSegmentator no reporta exactitud para S1, el control de nivel desequilibra la cohorte por grupos (cap3 l. 253) y la envolvente puede cerrar el canal sacro (l. 257). En apariencia: los tres desplazamientos de dominio (l. 182, 263) y la truncacion de rayas, que la comparacion con el protocolo fisico no puede evaluar (l. 261). Es la misma forma de r02 guia-2 (supuestos), ahora en las limitaciones. | Aplicar la decision de r02: sin recuento cerrado, con la remision a `sec:amenazas`. Nombrar al menos los desplazamientos de dominio del Obj. 3. |
| guia-4 | media | G-T2, G-A7 | introduccion.tex:43 | El Obj. 4 formaliza SAP, pero la introduccion no dice que mide. No aclara que el grado de brecha cortical y la viabilidad del corredor (Obj. 2, l. 39) son componentes de SAP, y el tercer componente, la fraccion por zona de densidad (cap3 l. 189), solo aparece de refilon dentro de un `\GAPDEC` (l. 69). El lector no sabe que evidencia produce el Obj. 4. | En el Obj. 4, enumerar en una oracion los tres componentes de SAP (grado, fraccion por zona de densidad, viabilidad), con remision a `sec:sap`. |
| guia-5 | media | G-A10 | introduccion.tex:64 (y l. 32) | El alcance restringe el trabajo a "un tornillo iliosacro parametrico y rigido" sin dar la razon, y el objetivo general glosa los implantes como "tornillos y placas". G-A10 pide que queda fuera y por que. Las placas y otros tornillos quedan fuera sin motivo explicito. | Dar la razon con fuente (p. ej., la referencia clinica y el marco de Kaiser et al. solo existen para tornillos iliosacros en S1) o `\GAPDEC`, y quitar "placas" de la glosa del objetivo general o acotarla. |
| guia-6 | baja | G-A10 | introduccion.tex:70 | Patron PAT-51 reincide. XCIST/CatSim se excluye porque una reimplementacion "no tendria una validacion en metal que heredar", pero l. 80 dice que adaptar el protocolo de Peters et al. "no hereda esa validacion", y cap3 l. 221 agrega que esa validacion no cubre el paso hibrido con imagenes clinicas. El motivo no distingue la opcion excluida de la adoptada (que ademas corre sobre CatSim/XCIST, cap3 l. 219). | Dar la diferencia real entre las dos opciones (protocolo publicado con metricas y validacion en fantoma frente a ninguna validacion en metal) y decir que el paso hibrido tampoco esta validado. |
| guia-7 | baja | G-T2 | introduccion.tex:32, 39, 71 | Hay terminos clinicos sin glosa: "cortical" (l. 32, primera aparicion), "series navegada y convencional" (l. 39, el lector no sabe que es navegacion quirurgica) y "fenotipo sacro"/"sacros dismorficos" (l. 71). Patron PAT-50 reincide: la exclusion "Estratificacion por fenotipo sacro" se nombra con un termino que el documento no define. | Aposicion corta en cada primera aparicion (decision 2026-09-29 sobre glosas clinicas), p. ej., "operada con navegacion asistida por computador". |
| guia-8 | baja | G-A7 | introduccion.tex:37, 60 | El Obj. 1 se enuncia sobre "el autoencoder de un modelo de difusion latente", pero la Justificacion (l. 60) usa como evidencia la extension a "uno entrenado con TC" (Guo et al., cap3 l. 75), anadida despues del veredicto y evaluada con los mismos pacientes de prueba (cap3 l. 255, 265). El enunciado del objetivo no la incluye. | En el Obj. 1 o en el parrafo de l. 46, una oracion que diga que la compuerta se extendio a un segundo latente despues del veredicto, con la misma regla. |
| guia-9 | baja | G-A10 | introduccion.tex:78 | Patron PAT-38 reincide (parcial). La malreduccion residual de la referencia clinica "estrecharia sus corredores", pero no se dice que efecto tendria en la comparacion de grados: una referencia con mas brechas por anatomia que el muestreador no reproduce. | Media oracion con el sentido del sesgo sobre la distancia de Wasserstein-1, o remitir a `sec:amenazas` si alli se dice. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | no cumple, a medias (guia-4; baja guia-7) |
| G-T3 | cumple ($M$, $B_{\delta}$, $G$, $h$ y $W_1$ se usan igual que en el cap. 3) |
| G-T4 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-T5 | cumple con GAP (orden Justificacion/Formulacion en el `\GAPDEC` de l. 28) |
| G-T6 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-A1 | cumple con GAP (el proposito esta; pregunta e hipotesis quedan bajo el `\GAPDEC` de l. 28, #126) |
| G-A2 | no evaluable (encabezado fuera de alcance) |
| G-A3 | no cumple, a medias (guia-1): la tension esta en l. 54-56 y ya no se contradice, pero no justifica el sintetizador aprendido |
| G-A4 | cumple a medias (guia-1) |
| G-A5 | cumple en el alcance revisado |
| G-A6 | cumple |
| G-A7 | no cumple, a medias (guia-2, guia-4; baja guia-8). Obj. 3 y 4 cumplen con GAP |
| G-A8 | cumple con GAP (Obj. 1 falsable; Obj. 2, 3 y 4 con `\GAPDEC` en l. 48) |
| G-A9 | cumple con GAP (eslabon necesidad-coherencia en el `\GAPDEC` de l. 52; orden en l. 28) |
| G-A10 | no cumple, a medias (guia-2, guia-3, guia-5; bajas guia-6 y guia-9). Las cuatro exclusiones tienen razon (PAT-44 no reincide) |
| G-B10 | no evaluable (capitulo2 es esqueleto) |
| G-C4 | cumple (los cuatro objetivos coinciden con cap3 l. 13, fig. 1 y tab:diseno; el verbo "valida" de cap3 l. 13 ya lo escalo el redactor) |
| G-D1, G-D2 | no evaluable (conclusiones es plantilla) |

## Propuestas de criterio
- Un criterio (G §2.1) que exija que la tension justifique **cada** componente de la contribucion
  frente a la alternativa mas directa que la propia tesis usa como comparacion (ver guia-1).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| El criterio que descarta una alternativa se aplica tambien a la opcion adoptada | G-A10 | "geometrias parametricas, que evitan segmentar el metal con un umbral fijo" (entrenamiento usa 2500 HU) | PAT-51 |
| Contribucion anunciada que ningun objetivo evalua, sin decirlo | G-A7, G-A10 | "El primero son geometrias de implante rigidas y parametricas" | PAT-49 |
| Recuento cerrado de limitaciones o supuestos que omite otros declarados en el metodo | G-A10 | "En la apariencia, las limitaciones son tres" | nuevo (variante de PAT-44; r02 guia-2 en supuestos) |
| Tension que la propia comparacion de la tesis resuelve con la alternativa descartada | G-A3 | "ninguno ... produce a la vez" (Peters corre sobre las poses muestreadas) | nuevo |
| Exclusion de alcance nombrada con un termino que el documento no define | G-A10, G-T2 | "Estratificacion por fenotipo sacro" | PAT-50 |
