# Respuesta del redactor — capitulo1 — r09

Archivo: `overleaf/secciones/capitulo1.tex`. Esta ronda atiende los reportes `-guia`, `-estilo`, `-trazabilidad`
y `-lint` de r09, y además la sección «capitulo1» de `redaccion/ENCARGO_2026-10-15.md` (DEC 2026-10-15, punto 1).
Lint final: PASA (0/0/0; GAP lit=0 dato=2 dec=0), compilado (146 páginas).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| Encargo :48 (`\GAPDEC` del suelo) | encargo 2026-10-15 | APLICADO | Se retira la marca. Queda dicho que la representación no baja de -1000 HU. La regla preinscrita se declaró no aplicable: su desenlace cambia según el percentil y su rama de cambio de representación quedó bloqueada por el congelamiento (DEC 2026-10-15 pto 1). Su efecto se examina sobre el contraste primario con un análisis posterior que aplica el mismo suelo a los dos brazos, con remisión a `sec:sintetizador` y `sec:amenazas`. Por el encargo, no entran cifras (225.0/1.2 HU) ni el resultado del TOST con recorte. Se quitó además el 196.3 HU de esta oración: ya aparece en el marco estadístico. |
| T01 | trazabilidad | APLICADO | El mismo cambio que el encargo. La sugerencia de incluir 225.0/1.2 HU no se aplica porque el encargo pide «sin cifras de resultados nuevos», y el propio auditor admite la variante sin cifras. |
| guia-1 | guia | APLICADO | Igual que T01. |
| T02 | trazabilidad | APLICADO | Se elimina la oración de :58 («regla preinscrita cuyo desenlace aún no se conoce»). La oración anterior ya remite a `sec:mt-tc`, donde está el tratamiento. |
| guia-2 | guia | APLICADO | Igual que T02. |
| ES-9 | estilo | APLICADO | Igual que T02. |
| guia-3 | guia | APLICADO | :66 dice ahora «usa el protocolo físico como comparación», y :33 dice «descrito» en lugar de «previsto». |
| ES-5 | estilo | APLICADO | :66 abre con «el sintetizador de este trabajo también lo produce, pero con un modelo aprendido y sin simular proyecciones». |
| ES-6 | estilo | APLICADO | El cierre de :66 queda en «Este trabajo usa el protocolo físico como comparación (Sección apariencia)». Se tomó el verbo de guia-3, no el «se prevé» de la propuesta, para no reincidir en PAT-122. |
| guia-4 | guia | APLICADO | En :130 se definen los tres desenlaces según dónde queda el IC90 respecto de ±Δ (DEC 2026-10-15 pto 15). Si el IC excluye el 0, se informa la dirección. Se quitó «ni equivalencia ni diferencia». |
| T04 | trazabilidad | APLICADO | Igual que guia-4. |
| guia-5 | guia | APLICADO | En :128 se añaden dos oraciones. La primera dice que el IC90 de la diferencia media pareada se calcula con la *t* de Student y supone diferencias pareadas aproximadamente normales e independientes (DEC 2026-10-15 pto 14; `capitulo3.tex` §ap-analisis). La segunda describe la sensibilidad exacta por inversión de la prueba de permutación pareada como método, posterior a la prueba de v1, sin resultado. Ninguna afirma una propiedad teórica de la permutación, así que no hace falta `\GAPLIT`. |
| guia-6 | guia | APLICADO | En :128, «con un nivel de significación de 0.05 en cada prueba unilateral», sin $\alpha$. |
| guia-7 | guia | RECHAZADO (en esta sección) | El propio revisor indica que la corrección va en `capitulo3.tex`:202 y que en el capítulo 1 «no hace falta tocar nada». El redactor de capitulo1 no puede editar otra sección. Aviso al orquestador: la notación $v=\alpha_t\epsilon-\sigma_t x$ de capitulo3 choca con $\sigma_t$ del muestreador y debería remitir a la ecuación de `sec:mt-difusion` ($a_n$, $s_n$, $\boldsymbol{\xi}$). |
| guia-8 (baja) | guia | APLICADO | Nuevo párrafo para el Objetivo 3 al final de `sec:mt-estadistica`. En la comparación con el protocolo físico, solo el TOST del modelo principal con su propio margen es confirmatorio. Los análisis posteriores son descriptivos, sin corrección por multiplicidad, y solo pueden bajar la categoría del desenlace (DEC 2026-10-15, regla general y pto 15). El párrafo de :134 se partió en dos (compuerta / extensión a Guo et al.) para no pasar de siete oraciones. Se acotó a «la comparación con el protocolo físico» porque DEC pto 15 trata el TOST y no la prueba de Wilcoxon. |
| T03 | trazabilidad | APLICADO | Se retira «adoptada». Ahora el texto dice que Fay distingue tres convenciones (central, minlike, Blaker; ficha `fay2010two`), define minlike y la atribuye a `fisher.test` bajo `stats` 2.11.0. Como ni DEC, ni #132, ni `experiments/` registran qué programa o convención produjo los valores p, se abre `\GAPDATO`. No se incluye la observación del auditor de que central y minlike coinciden con grupos iguales: es una derivación sin respaldo en el repositorio. |
| ES-1 | estilo | APLICADO | Se elimina «esta atribución se limita a la implementación y versión que examinó». «bajo la versión 2.11.0 del paquete stats» conserva la acotación de PAT-166. |
| ES-2 | estilo | APLICADO | :132 se parte en dos párrafos: remuestreo de la compuerta (4 oraciones) y prueba de Fisher, que abre con la oración temática propuesta. |
| ES-3 | estilo | APLICADO | :31 dice «Los haces de los equipos médicos reales son policromáticos». :62 dice «con un haz monocromático idealizado … ninguno de los dos trabajos reúne». |
| ES-4 | estilo | APLICADO | En :68, «como término de comparación» (BITACORA §2, 2026-09-30). |
| ES-7 | estilo | APLICADO | La oración 2 de :76 pasa a «traslada de un tipo de tornillo al otro solo el umbral de 10 mm y la holgura radial, como convención». La oración «Aun así …» se elimina. La siguiente queda en «McLaren et al. aplican el umbral de 10 mm a corredores transilíaco-transsacros». La oración se partió en dos por E-O1 (lint). |
| ES-8 | estilo | APLICADO | En :108, «cuya arquitectura se describe en la Sección sintetizador». |
| ES-10 (baja) | estilo | APLICADO | «y se le aplican las tolerancias angulares». |
| ES-11 (baja) | estilo | APLICADO | «el modelo de proyecciones en que se basa ese algoritmo». |
| ES-12 (baja) | estilo | APLICADO | En :35 se añade «en su simulación de implantes cocleares» para distinguir a los dos Wang et al. |
| ES-13 (baja) | estilo | APLICADO | «Standring describe además el ala …». |
| ES-14 (baja) | estilo | APLICADO | El párrafo abre con «Cada objetivo produce un resultado de distinta naturaleza y se analiza sobre su propia unidad». |
| ES-15 (baja) | estilo | APLICADO | «que fija los totales marginales de la tabla y enumera las tablas compatibles con ellos». |

Lint r09 de entrada: sin hallazgos. Las dos oraciones largas que salieron tras editar (:48 y :76, E-O1) se partieron.

GAP: se cerró 1 `\GAPDEC` (suelo, en capitulo1) y se abrió 1 `\GAPDATO` (programa y convención de Fisher). Ninguno es `\GAPLIT`, así que `_candidatos.md` no cambia. `MAPA.md` quedó actualizado.

Aviso al orquestador: `capitulo3.tex`:198 tiene la misma `\GAPDEC` del suelo y la cubre el encargo de capitulo3-r22. En la fila del suelo de `MAPA.md` solo se marcó como cerrada la parte de capitulo1.

## Decisiones de redaccion

- Si una DEC declara no aplicable una regla preinscrita, el texto dice «se declaró no aplicable», da el motivo en una frase y nombra lo que la sustituye, con su carácter (posterior, descriptivo). En el marco teórico no entran cifras del resultado.
- Los desenlaces del TOST se nombran siempre **equivalencia**, **no equivalencia** y **no concluyente**, según dónde queda el IC90 respecto de ±Δ. La dirección se informa siempre que el IC excluya el 0 (DEC 2026-10-15 pto 15). No se usa «no concluye ni equivalencia ni diferencia».
- «Fuente» se reserva para la bibliografía. Para el emisor de rayos X se usa «haz» o «equipo».
- Una convención estadística se define desde la ficha que la documenta, sin decir que la tesis la «adoptó», salvo que un registro del repositorio muestre que se aplicó. Si falta ese registro, va `\GAPDATO`.
