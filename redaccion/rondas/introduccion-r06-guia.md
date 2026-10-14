# Revision guia CS — introduccion — r06

Contexto: encargo `redaccion/ENCARGO_2026-10-14_introduccion.md`, que viene de capitulo3-r19 guia-4 (desfase del
Objetivo 3). Revise todo `introduccion.tex`. Los hallazgos que caen en el encabezado (l. 1-21), que el encargo
excluye, van con severidad baja para que el redactor los escale. Secciones cruzadas que lei: `capitulo3.tex`
(l. 1-92, 194-451), `capitulo2.tex` §Brecha (l. 100-114), `capitulo4.tex` (esqueleto) y `conclusiones.tex`
(esqueleto). Tambien lei `docs/00-tesis.md` (T06), DEC 2026-10-08 C (pto 24: pregunta y orden de la introduccion
decididos) y las implicancias #90, #126, #128, #174-#177 y #182. Lei la respuesta r05: no reabro S03, S12 ni guia-2
r05. La pregunta y el orden de las subsecciones son decision de la autora (DEC 2026-10-08 pto 24) y no se reportan.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-A8, G-C4 | introduccion.tex:48, :56, :80 | La falsabilidad del Obj. 3 describe una prueba que ya se hizo. :48 dice que el margen está "aún sin medir", y cap3:377 lo da medido: $\Delta$ = 196.3 HU. :56 ("Si alcanza la equivalencia ... es lo que pone a prueba") y :80 ("es la que puede contradecirlo") siguen en condicional, aunque cap3:246 da el resultado (no se concluyó equivalencia). La introducción tampoco lleva el `\GAPDEC` de cap3:375/:451. Según ese GAP, no está fijado cómo se lee un intervalo entero por debajo de $-\Delta$, que es justo el desenlace obtenido. Sin ese GAP, el lector no sabe si el Obj. 3 falló. | En :48, dar $\Delta$ como medido en validación y remitir a `sec:ap-analisis`. Dar el resultado como medición (encargo I2) con su condición: titanio, 13 pacientes, eje sin perturbar (PAT-31). Replicar el `\GAPDEC` de cap3:375 sobre la lectura del desenlace. En :56 y :80, decir que la comparación se ejecutó y remitir a ese mismo GAP. :48 ya tiene 7 oraciones, así que el Obj. 3 debe ir en un párrafo propio (PAT-58). |
| guia-2 | media | G-A7, G-C4 | introduccion.tex:56 (y :13, :41) | :56 dice que el protocolo de Peters et al. se ejecutará "sobre las poses del muestreador ... y según el plazo". Cap3:325 y :363 dicen otra cosa: se ejecutó sobre el eje del corredor sin perturbar, en los 13 pacientes, como contraste primario. Además, :13 y :41 presentan la cadena como un muestreador que entrega la pose al sintetizador, y ninguna oración dice que la apariencia no se evalúa sobre las poses del muestreador. Es afín a PAT-49 (aporte que ningún objetivo evalúa, sin decirlo). Aviso fuera de alcance: cap2:106 lleva la misma oración desfasada, así que la bisagra (G-B10) se mantendrá solo si cap2 se corrige igual. | Poner el hecho de cap3:325/:363 y, en una frase, su consecuencia: ningún objetivo evalúa la apariencia sobre las poses del muestreador. Remitir al `\GAPDEC` de cap3:325 para la razón, sin inventarla (encargo I1). |
| guia-3 | media | G-A10, G-T2 | introduccion.tex:90 | Patron PAT-122 reincide: el `\GAPDATO` dice que "no existe aún resultado del Objetivo 3 porque el modelo final no está elegido". Cap3:238 lo eligió (paso 16 500), y cap3:38 da la corrida final como evaluada. Patron PAT-11 reincide: el `\GAPDEC` de la contingencia de plazo sigue la implicancia #90 en su estado inicial, y #90 quedó CERRADA el 2026-10-14. Además, "modelo final" choca con "estado final" (cap3:228), que en el capítulo 3 es el candidato **descartado** (PAT-14). | Decir en prosa que el punto de control está elegido por cotejo de apariencia en validación, con remisión a `sec:sintetizador`. No usar "cáscaras" sin definirlas (PAT-3). Retirar el `\GAPDEC` #90 y poner el hecho. Dejar `\GAPDATO` solo para lo que sigue pendiente: el contraste de realismo (cap3:38) y, si se nombra, la versión 2 en prueba (cap3:275). Usar "modelo evaluado" o "punto de control elegido", nunca "modelo final". Aviso: cap3:375 conserva un `\GAPDEC` sobre el cierre formal de #90. |
| guia-4 | media | G-A8 | introduccion.tex:32 | Patron PAT-45 reincide. El objetivo general pide una cadena "que genere implantes ... con coherencia física y quirúrgica", es decir, presupone el resultado. El contraste primario de la apariencia no concluyó equivalencia (cap3:246). Así redactado, el objetivo solo se cumple si el resultado es favorable, y la conclusión (G-D1) no podrá responderle con un "no". | Redactar el objetivo en términos de evaluación: "... y evaluar la coherencia física y quirúrgica de lo que genera". Así lo hacen :15 y la pregunta de :21 ("en qué medida"). |
| guia-5 | media | G-A10, G-A7 | introduccion.tex:88 | Las limitaciones de la apariencia omiten las amenazas del cap. 3 que condicionan la lectura del resultado obtenido. (a) El criterio primario no distingue las rayas de una textura sin dirección, y la estructura de raya no está medida (cap3:441, `\GAPDATO` #176). (b) En validación, el protocolo físico queda por encima de los tornillos reales y el percentil 95 del sintetizador por debajo (cap3:451). (c) $\Delta$ y las otras dos elecciones salen de dos receptores y empujan en el mismo sentido (cap3:429-431). Preventivo: la fórmula del encargo I2, "el sintetizador da rayas más débiles", afirma que hay rayas, algo que el diseño no mide (afín a PAT-61). | Agregar una o dos oraciones con (a) y (b), con el `\GAPDATO` de cap3:441 replicado o remitido, y remitir a `sec:amenazas` para (c). Enunciar el resultado como "una *streak amplitude* menor que la del protocolo físico", no como "rayas más débiles". |
| guia-6 | media | G-A10 | introduccion.tex:90 | Patron PAT-31 reincide. Dice que el segundo desplazamiento de dominio "se mide en la evaluación del sintetizador". Según cap3:226, su medida (el salto en el borde de $G$) solo se toma en la reconstrucción de implantes reales, donde el contexto sí trae metal, y no en la síntesis sobre pelvis sin metal, donde actúa el desplazamiento (`\GAPDEC` en cap3:226). La introducción da la limitación por cubierta cuando el capítulo 3 la deja abierta. | Decir dónde se mide y que no se mide en la condición en que actúa, con remisión al `\GAPDEC` de cap3:226. |
| guia-7 | baja | G-A7, G-C4 | introduccion.tex:41 | El Obj. 3 enumera tres comparaciones de la apariencia, pero no nombra la reconstrucción de implantes reales. Esa evaluación es descriptiva, ya se ejecutó y ocupa la fila 3 de `tab:diseno` (cap3:331, :402). | Agregar una cláusula: "y, de forma descriptiva, con la reconstrucción de implantes reales (Sección~\ref{sec:ap-reconstruccion})". |
| guia-8 | baja | G-A10 | introduccion.tex:90 | La introducción no menciona la versión 2 del sintetizador, aunque el cap. 3 le dedica `sec:v2` y un párrafo de amenazas (cap3:427). Si un lector la encuentra solo en el cap. 3, no sabe si cambia el modelo del Obj. 3. | A lo sumo una frase (encargo I2): es posterior y exploratoria. Por la regla fijada antes de generar no mejora, y el modelo evaluado sigue siendo la versión 1. Sus resultados de prueba van en `\GAPDATO`. |
| guia-9 | baja | G-A10 | introduccion.tex:88 | La limitación del truncamiento por $B_{\delta}$ no recoge el acotamiento de cap3:443. En componentes del tamaño de un tornillo, el artefacto real no se separa del control nulo más allá de 10 mm, y la banda de 12 mm lo contiene. Para placas y prótesis no está acotado. | Si cabe sin crecer el párrafo, una cláusula con esa condición y remisión a `sec:v2`. Si no cabe, solo la remisión. |
| guia-10 | baja | G-T2 | introduccion.tex:5 | Patron PAT-14 reincide. "Bandas oscuras" usa "banda", que BITACORA §2 (2026-09-29) reserva para $B_{\delta}$ (:13, :41). "Escasez de fotones" no es el término fijo "inanición de fotones" (`overleaf/CLAUDE.md`), que sí usa el cap. 1. El encabezado está fuera del encargo, así que esto se escala. | "Zonas oscuras" e "inanición de fotones". |
| guia-11 | baja | G-A5 | introduccion.tex:19-21 | La subsección "Formulación del problema" contiene solo la pregunta, y la pregunta trata de "la cadena propuesta". El problema computacional (la tensión) está en :9 y :54, así que la sección cumple su función. Aun así, un lector que busque el problema bajo ese título encuentra el método. Se respetan la pregunta y el orden decididos (DEC 2026-10-08 pto 24). Fuera del encargo, así que se escala. | Antes de la pregunta, una oración que enuncie el problema con la fórmula de :54, o una remisión a la justificación computacional. |

alta=0 media=6 baja=5

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP. Aviso: el cap. 4 es esqueleto, así que las remisiones al "capítulo de resultados" llegan hoy a un capítulo vacío |
| G-T2 | no cumple (guia-3, guia-10) |
| G-T3 | cumple: $M$, $B_{\delta}$, $G$, $\Delta$ y $W_1$ se usan igual que en el cap. 3 |
| G-T4 | no evaluable (lo revisa `auditor-trazabilidad`) |
| G-T5 | cumple (orden decidido, DEC 2026-10-08 pto 24) |
| G-T6 | no evaluable (lo revisa `auditor-trazabilidad`) |
| G-A1 | cumple: planteamiento (:3-9), revisión preliminar (:5-11, :54-58), propósito (:13, :32) y pregunta (:21) |
| G-A2 | cumple |
| G-A3 | cumple: la tensión está en :9 y :54 |
| G-A4 | cumple (:5, :56) |
| G-A5 | cumple a medias (baja guia-11) |
| G-A6 | cumple |
| G-A7 | no cumple en el cruce con el cap. 3 (guia-2, guia-5, guia-7) |
| G-A8 | no cumple (guia-1, guia-4). El Obj. 2 no tiene regla de fallo, por decisión de la autora (DEC 2026-10-08 ptos 14-17), y así se declara; no se reporta. El Obj. 4 es un objetivo de definición declarado |
| G-A9 | cumple |
| G-A10 | cumple a medias (guia-3, guia-5, guia-6, guia-8, guia-9). Las cuatro tareas y los cuatro puntos de alcance están cubiertos (PAT-44 no reincide) |
| G-B10 | cumple: cap2:106 enuncia la misma tensión con las mismas palabras. Riesgo: cap2:106 arrastra el desfase de guia-2 |
| G-C4 | no cumple en el cruce (guia-1, guia-2, guia-7) |
| G-D1, G-D2 | no evaluable: conclusiones es esqueleto |

## Propuestas de criterio
- Bloque (a): cuando un objetivo ya tiene resultado, la introducción debe decir cómo se lee ese resultado
  respecto del objetivo (cumplido, no cumplido, no concluyente), o declarar que la lectura está pendiente. Hoy cabe en
  G-A8, pero la rúbrica solo pide que el objetivo pueda fallar.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP o futuro de intención que niega una evaluación ya ejecutada y registrada | G-A10, G-C4 | "prevé ejecutar ... según el plazo"; "el modelo final no está elegido" | PAT-122 |
| GAP sobre una implicancia redactado en su estado inicial, aunque ya está CERRADA | G-A10 | `\GAPDEC` de la contingencia de plazo (#90, CERRADA 2026-10-14) | PAT-11 |
| Objetivo general redactado con el resultado como propiedad del producto | G-A8 | "que genere implantes ... con coherencia física y quirúrgica" | PAT-45 |
| Limitación resumida como cubierta cuando el método solo la mide en otra condición | G-A10 | "el segundo se mide en la evaluación del sintetizador" | PAT-31 |
| Resultado enunciado con un fenómeno que la métrica no distingue | G-A7 | "el sintetizador da rayas más débiles" (la métrica no distingue rayas) | PAT-61 |
| "Banda" usada fuera de $B_{\delta}$ en el mismo capítulo | G-T2 | "bandas oscuras, regiones brillantes" | PAT-14 |
