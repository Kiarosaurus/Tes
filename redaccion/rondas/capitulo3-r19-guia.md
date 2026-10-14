# Revision guia CS — capitulo3 — r19

Entrada: `overleaf/secciones/capitulo3.tex` (estado tras la respuesta r18), lint `capitulo3-r19-lint.md` (PASA, 14 E-P1
baja), respuesta `capitulo3-r18-respuesta.md` (nada RECHAZADO; guia-1 a guia-7 de r18 aplicados y verificados en el
texto). Cotejado con `redaccion/ENCARGO_2026-10-14.md` (V1-V4), `docs/01-decisiones.md` 2026-10-13, 2026-10-14 y
2026-10-14 (2), `docs/04-implicancias.md` #164, #176, #177 y #182, y `experiments/objetivo3/EXPERIMENTOS.md`:92
(`resultados_prueba_v1.md` HECHO). Para G-C4 se leyo `introduccion.tex`.

Nota de alcance: se revisa el texto de hoy, sin la seccion de la version 2. Lo que el encargo ya pide (V1-V4) **no se
repite como hallazgo**. Abajo va lo que el encargo no cubre y lo que se rompe en el texto vigente cuando entre la
version 2 (guia-5 a guia-8, todos de severidad baja y preventivos).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T4 | capitulo3.tex:38, :218, :329 | Patron PAT-122 reincide. El `\GAPDATO` de :38 dice que "los resultados del Objetivo 3 sobre esa partición no están disponibles". :218 dice que la evaluación de la corrida final "está pendiente", y el `\GAPDATO` de :329 da por pendiente la amplitud del protocolo físico en prueba. DEC 2026-10-13 (1) (decidida) dice que la versión 1 "ya se evaluó tal como estaba preinscrita", y EXP:92 da `resultados_prueba_v1.md` como HECHO (TOST, sensibilidades, Wilcoxon y reconstrucción de implantes reales). El encargo V1 solo pide remitir al resultado si ya se cita, y no nombra estos tres pasajes. | Decir que la evaluación preinscrita de la versión 1 en prueba se hizo y remitir al capítulo de resultados, sin cifras (DEC 2026-09-29: los veredictos van al cap. 4). Mantener como `\GAPDATO` solo lo que sigue pendiente: el contraste de realismo, que no tiene script ni lista de pacientes según #177. |
| guia-2 | media | G-C7 | capitulo3.tex:389 | Patron PAT-140 reincide. Dice que "con ese resultado ya visto, se tomaron siete decisiones", y que solo dos "no salen de una regla previa y son las expuestas". Tras la evaluación con el modelo afectado (10 de octubre, #164) se tomaron también la corrección de la pose, el control de pose, la nueva aplicación de la regla del material y la lectura de que el titanio es "el menos alejado" (:385, :391). De ellas, el control de pose y esa lectura tampoco salen de una regla previa. El recuento cerrado y la lista de expuestas quedan cortos. | Quitar el recuento cerrado o completarlo. Añadir a las expuestas el control de pose y la lectura del material, con remisión a :385 y :391, sin repetir lo que esos párrafos ya dicen. |
| guia-3 | media | G-C7 | capitulo3.tex:287, :405 | Falta una amenaza de constructo sobre el criterio primario. :287 justifica los anillos sin orientación porque las colas "encuentran las rayas claras y las oscuras en cualquier punto del anillo". No dice la otra cara: el estadístico de colas también crece con cualquier desviación extrema sin estructura de raya. La *streak amplitude* adaptada mide, por tanto, la dispersión de las colas y no la presencia de rayas. La inspección de la versión 1 describe dentro de `G` "moteado claro/oscuro, no rayas radiales" (#176, ABIERTA, inspección y no medición), y DEC 2026-10-13 (1) recoge que la autora juzga de baja calidad ese artefacto. | En validez de constructo, una o dos oraciones: el criterio primario no distingue rayas de textura sin dirección, así que una amplitud equivalente no prueba que haya rayas. La observación de #176 entra como `\GAPDATO` o `\GAPDEC` y no como hecho (OC-3). |
| guia-4 | media | G-C4 | introduccion.tex:48, :56, :90 frente a capitulo3.tex:291, :341 | Criterio de cruce entre bloques. La introducción dice que el margen $\Delta$ está "aún sin medir" (:48); el capítulo 3 da 196.3 HU (:341). También dice que el protocolo de Peters et al. se ejecutará "sobre las poses del muestreador" (:56), mientras que el capítulo 3 evalúa sobre el eje del corredor sin perturbar (:291). Por último, dice que "el modelo final no está elegido" (:90), y el capítulo 3 lo eligió (:238). El objetivo experimental del capítulo 3 ya no es el que anuncia el bloque (a). La corrección cae fuera de esta sección y del encargo. | Escalar a la autora: actualizar la introducción en su propio ciclo con el diseño congelado del capítulo 3. El capítulo 3 no cambia. |
| guia-5 | baja | G-T2 | capitulo3.tex:40, :212 | Preventivo (afín a PAT-14). "Corrida final" está definida como la que procesa la partición de prueba "con el modelo evaluado y la pose corregida", y "modelo evaluado" designa en todo el capítulo al punto de control de run04. El encargo V4 trae corridas de la versión 2 sobre la partición de prueba, y su `v2_plan` también las llama "corridas finales". Con los mismos nombres, los dos términos designarían dos cosas. | Al redactar V2-V4, dar nombres propios a las ejecuciones y a los modelos de la versión 2 (p. ej., "evaluación exploratoria de la versión 2"). Dejar "corrida final" y "modelo evaluado" para la versión 1, o redefinirlos una sola vez en `sec:vision`. |
| guia-6 | baja | G-T3 | capitulo3.tex:15, :107, :256 | Preventivo. El encargo nombra "D" y "B" a las dos intervenciones, `T` al canal analítico y `e` al estadístico de la compuerta. El capítulo ya usa $D$ para el diámetro del corredor (:107), $B_{\delta}$ para la banda (:15) y $T$ para el tramo de SAP (:256). La BITACORA §2 2026-10-03 ya evitó $T$ por el mismo motivo. | En la subsección nueva, nombrar las intervenciones por su función (sobremuestreo y peso de la pérdida; canal de endurecimiento del haz) y dar al canal un símbolo que el capítulo no use. |
| guia-7 | baja | G-T4 | capitulo3.tex:305 | Preventivo (afín a PAT-39). "Toda la evaluación del Objetivo 3 es métrica" dejará de ser cierta cuando entre la comparación visual a ciegas D3 de la versión 2 (DEC 2026-10-14 (2) (2)). | Acotar la frase a la versión 1, o decir en la subsección nueva que D3 es descriptiva y no forma parte de la decisión. |
| guia-8 | baja | G-C7 | capitulo3.tex:210, :405 | Preventivo (afín a PAT-120). Cuando entre D1/D2 (encargo V1; DEC 2026-10-13 (3): "en tornillos la banda de 12 mm alcanza"), :210 seguirá diciendo que la banda "trunca a propósito las rayas lejanas", cuya extensión ninguna fuente mide. :405 tampoco reflejará que la medición propia acota ese truncamiento para piezas del tamaño de un tornillo, y no para placas ni prótesis. | Al incorporar D1/D2, ajustar :210 y la amenaza de :405 con su condición (componentes de 500 a 4000 mm$^3$; referencia en otro corte) y remitir a la subsección nueva, sin duplicar sus cifras. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | cumple (hoy; riesgo de guia-5 al incorporar la versión 2) |
| G-T3 | cumple (hoy; riesgo de guia-6) |
| G-T4 | no cumple (guia-1) |
| G-T5 | cumple |
| G-T6 | cumple (el lint no reporta E-F) |
| G-C1 | cumple con GAP (cabeza de $M$, regla del suelo en HU, lotes) |
| G-C2 | cumple con GAP (algoritmo del eje, heurística de referencias, predicción $v$, repositorio AAPM); la corrección de la pose y el control de pose ya están descritos (:220-222) |
| G-C3 | cumple |
| G-C4 | no cumple en el cruce con la introducción (guia-4); dentro del capítulo 3, cumple |
| G-C5 | cumple con GAP |
| G-C6 | cumple |
| G-C7 | no cumple (guia-2, guia-3; guia-8 preventivo; la declaración post hoc de la versión 2 la cubre el encargo V4) |
| G-C8 | cumple con GAP (supuesto de la *t*, desenlaces del TOST, tamaño de efecto) |
| G-C9 | cumple (protocolo físico como comparación principal, que DEC 2026-10-13 (3) mantiene) |
| P-MM1 | cumple |
| P-MM2 | cumple (Figura `fig:pipeline`) |
| P-MM3 | cumple con GAP |

## Propuestas de criterio
- Bloque (c): cuando una métrica publicada se adapta y se retira parte de su definición (aquí, la orientación de las
  regiones hacia la raya), la sección de validez de constructo debe decir qué deja de distinguir la métrica adaptada.
  Hoy cabe en G-C7, pero la rúbrica no lo nombra.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP o prosa que niega una evaluación ya hecha y registrada en DEC y EXP | G-T4 | "los resultados del Objetivo 3 sobre esa partición no están disponibles" | PAT-122 |
| Recuento cerrado de decisiones post hoc que no se actualiza al añadir otras en párrafos vecinos | G-C7 | "se tomaron siete decisiones" (faltan control de pose y lectura del material) | PAT-140 |
| Métrica adaptada justificada solo por lo que detecta, sin decir qué más la mueve | G-C7 | "el 5 % superior y el inferior encuentran las rayas" | nuevo |
| Nombres de una iteración nueva del método que chocan con términos o símbolos ya definidos | G-T2, G-T3 | intervención "D" frente a $D$; "corrida final" para dos versiones | PAT-14 |
