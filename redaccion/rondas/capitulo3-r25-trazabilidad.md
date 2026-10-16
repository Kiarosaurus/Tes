# Auditoria de trazabilidad — capitulo3 — r25

Alcance de la ronda: cierre de los dos `\GAPLIT` del capitulo (:419 lectura de un IC de equivalencia que cruza un
limite; :437 varianza del logaritmo ~ CV^2 para Pitman y Morgan sobre el logaritmo) con las fichas nuevas
`walker2011understanding`, `lakens2017equivalence` y `bland1996statistics`, mas la prosa que repite esos huecos fuera de
la marca. El inventario cubre `sec:ap-analisis` (:411-437) y los parrafos de Amenazas que dependen de ella (:489-491,
:515, :523-531). El resto del capitulo no cambio desde r24 y no se re-audita (sin argumento nuevo frente a
`capitulo3-r24-respuesta.md`). Lint: PASA (24 bajas E-P1 preexistentes; GAP lit 2, dato 18, dec 0).

Claves en `overleaf/referencias.bib`: `walker2011understanding` (:1314, Walker y Nowacki, 2 autores),
`lakens2017equivalence` (:663, autor unico Lakens), `bland1996statistics` (:81, Bland y Altman, BMJ 313:106; coincide con
la ficha). Implicancia #194 ABIERTA (visto bueno del mapeo pendiente de la autora).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2, E-R6 | capitulo3.tex:419 | "no concluyente se lee como que los datos no permiten afirmar la equivalencia" + `\GAPLIT` | `walker2011understanding.md` (Evidencia :84, :93, :106-107, :117, :123-124, :146-147); `lakens2017equivalence.md` (:65-74, :124-125); DEC 2026-10-15 pto 15 y (3) pto 1; #194 | El `\GAPLIT` ya no se justifica entero: el repositorio tiene fuente para parte de la lectura. Las fichas la sostienen **solo en parte**, y el cierre tiene que respetar cinco matices. (a) **El rotulo es propio.** Ninguna ficha usa "inconclusive" (Walker :146; Lakens :124). Walker rotula el IC que cruza un limite "Equivalence not established" (Fig. 1, p. 193) y escribe "nonequivalence cannot be ruled out" (p. 192). Lakens lo clasifica como escenario B, "statistically different from zero but not statistically equivalent" (p. 356; Fig. 1 "B: Not Equivalent and Statistically Different", p. 357). (b) **Choque literal.** Lakens reserva "undetermined", la traduccion natural de "no concluyente", para el escenario D (IC95 que incluye 0, p. 356). Ese no es el caso de v1. Citar a Lakens junto a "no concluyente" sin decirlo le atribuye la etiqueta contraria. (c) **La direccion se decide con otro intervalo.** Lakens decide la diferencia frente a 0 con el IC95 (Escenario C, p. 356; ficha :18). La tesis la informa cuando el IC90 excluye 0 (:417; DEC pto 15). Lakens no sostiene la regla de direccion tal como esta escrita. El IC95 de v1 [-516.2, -85.7] solo consta en #194 (ABIERTA) y en `_index.md`:844; no esta en `EXPERIMENTOS.md` ni en `resultados_dec_2026-10-15.md`/`resultados_prueba_v1.md`, y en todo caso es una cifra del cap. 4. (d) **Lo que Walker no sostiene.** "Ni como no equivalencia demostrada" y "un intervalo entero fuera del margen la habria rechazado" no estan en la Evidencia de ninguna ficha: la prueba de no equivalencia o de efecto minimo es NO ENCONTRADO (Lakens :125). Walker rotula ademas "not equivalent" un caso analogo en su Fig. 2 (p. 195; :124), y su dicotomia no tiene una categoria "no equivalencia" aparte. (e) **La lectura direccional "a la baja"** tampoco esta en ninguna ficha (Walker :147; Lakens :125) | Quitar el `\GAPLIT` y escribir el mapeo atribuyendo a cada fuente solo lo que dice. Propuesta: "Walker y Nowacki~\cite{walker2011understanding} llaman a ese caso equivalencia no establecida, en el que la no equivalencia no puede descartarse. En la clasificacion de Lakens~\cite{lakens2017equivalence}, un intervalo que cruza un limite y cuyo IC del 95\,\% excluye el cero es estadisticamente diferente y no equivalente; Lakens reserva el caso indeterminado para el intervalo que ademas incluye el cero. 'No concluyente' es el nombre que este trabajo da a los dos casos." Dejar sin cita, y como decision de este trabajo (DEC 2026-10-15 (3) pto 1): "ni como no equivalencia demostrada", "la habria rechazado" y la regla de direccion con el IC90. No dar el IC95 en el cap. 3. Si la autora quiere usarlo en el cap. 4, antes tiene que pasar a `resultados_dec` o a `EXPERIMENTOS.md` (PAT-158). Como #194 sigue ABIERTA, el rotulo de DEC pto 15 no se cambia, solo se mapea |
| T02 | media | G-T4, OC-2, E-R6 | capitulo3.tex:437 | "sobre el logaritmo, de forma aproximada, los coeficientes de variacion" + `\GAPLIT` | `bland1996statistics.md` (Evidencia :71-72, :85-90, :92-95; Restriccion :20-24); `pitman1939note`, `morgan1939test`; `resultados_dec_2026-10-15.md`:130-162; DEC (3) pto 2 | La ficha cubre un solo eslabon: antilogaritmar la DE en escala log y restarle 1 aproxima el CV, "provided the standard deviation is not large compared with the level" (p. 106). Cuatro limites. (a) **Base.** El ejemplo usa log10 (:71); el logaritmo natural es NO ENCONTRADO (:72), y el calculo se hizo con ln (`resultados_dec`:130). El paso "DE de ln ~ CV, varianza de ln ~ CV^2" no esta en el PDF (:92): es una derivacion propia (#194). (b) **Condicion.** Bland y Altman declaran la aproximacion "too large ... to be reliable" con CV 0.496 (:90) y no dan umbral (:95). El CV del protocolo fisico, 0.241 (:437), no queda cubierto por la ficha. (c) **Contexto.** La nota trata el CV intra-sujeto de mediciones duplicadas (:24, :88). Aqui se usa el CV entre pacientes de cada brazo. (d) **Pitman y Morgan.** La ficha no dice nada de esa prueba (:93), y las fichas de Pitman y Morgan no tratan la escala logaritmica | Quitar el `\GAPLIT` y repartir la atribucion. Propuesta: "Bland y Altman~\cite{bland1996statistics} muestran que, si la desviacion estandar no es grande frente al nivel de la medida, el antilogaritmo de la desviacion estandar en escala logaritmica, menos uno, aproxima el coeficiente de variacion. Con el logaritmo natural, eso equivale a que la varianza del logaritmo aproxima el cuadrado del coeficiente de variacion. Esa derivacion, y su uso para leer la prueba de Pitman y Morgan como comparacion de coeficientes de variacion entre pacientes, son de este trabajo; la nota no fija un umbral para el CV." No citar `bland1996statistics` en la oracion de Pitman y Morgan (PAT-194) |
| T03 | media | G-T4, E-R6 | capitulo3.tex:525 | "solo sobre el logaritmo se lee como comparacion aproximada de coeficientes de variacion" | igual que T02 | Patron PAT-168 reincide. La oracion repite fuera de la marca el hueco del `\GAPLIT` de :437, sin cita ni salvedad. Si se cierra solo :437, esta oracion queda afirmando la lectura sin rastro. Tampoco dice que esa aproximacion tiene una condicion de validez (CV pequeno) que el repositorio no acota para el protocolo fisico (CV 0.241) | Al cerrar :437, revisar :525. Opcion corta: "... y solo sobre el logaritmo, con una aproximacion valida para coeficientes de variacion pequenos (Seccion~\ref{sec:ap-analisis}), se lee como comparacion de coeficientes de variacion." Asi el quinto limite incluye la condicion de T02 (b) |
| T04 | media | G-T4 | capitulo3.tex:417 | "nunca se infiere equivalencia de una diferencia no significativa" | `walker2011understanding.md` Evidencia :117 (p. 194); `lakens2017equivalence.md` :52 (p. 355) | La fuente existe y no se cita. Walker: "a nonsignificant result implies only that equivalency ... cannot be ruled out" (p. 194). Tampoco la cita `capitulo1.tex`:128, que da la misma idea | Agregar `\cite{walker2011understanding}` a esa oracion, o en cap. 1 :128, donde se define (y en el cap. 3 basta la remision). Si se cita en el cap. 3: "como advierten Walker y Nowacki~\cite{walker2011understanding}" (E-F3: dos autores, sin *et al.*) |
| T05 | baja | G-T4 | capitulo3.tex:421 | "Se fijo con una formula decidida antes de ver ningun valor" | `walker2011understanding.md` :115-116 (p. 194); `lakens2017equivalence.md` :112-113 (p. 359) | Hecho propio bien sostenido por DEC. La razon metodologica de fijar el margen antes tiene fuente en el repositorio (Walker: "should be determined before the data is recorded", para mantener el error de tipo I) y no se hace visible. Opcional | Si se quiere hacer visible: "... antes de ver ningun valor, como recomiendan Walker y Nowacki~\cite{walker2011understanding} para conservar el error de tipo I". No atribuir a Lakens que prohiba cambiar el margen despues de ver los datos (NO ENCONTRADO, ficha :126) |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :413 | Wilcoxon de rangos con signo, una cola, alfa 0.05, pareado por paciente | `capitulo1.tex`:130 + `wilcoxon1945rankingmethods`; DEC 2026-10-15 pto 12 | si |
| :413 | 13 pacientes; minimo p = 2^-13; sin tamano de efecto | DEC 2026-10-15 pto 12 | si |
| :415 | TOST pareado, sintetizador frente a protocolo fisico con titanio | DEC 2026-10-15 pto 15; `resultados_dec`:39 | si |
| :415 | valor por paciente = mediana de 5 semillas / replicas A y B | DEC 2026-10-15; `resultados_dec`:39 | si |
| :415 | margen 196.3 HU | DEC 2026-10-15 pto 21; #175 | si |
| :415 | IC90 *t* sobre 13 pacientes; supuesto de normalidad e independencia | DEC 2026-10-15 pto 14 | si |
| :415 | sensibilidades: hierro, estado final, sin corredores angostos (10 pacientes) | `resultados_prueba_v1.md`:19-21 (n = 10) | si |
| :417 | lectura fijada el 15 de octubre, despues de v1 y antes del TOST de v2 | DEC 2026-10-15 (cabecera :2563-2566) | si |
| :417 | tres desenlaces (dentro / fuera / cruza) | DEC 2026-10-15 pto 15; `capitulo1.tex`:130 | si (rotulo propio; ver T01) |
| :417 | direccion si el intervalo (IC90) excluye 0 | DEC 2026-10-15 pto 15 | si (Lakens decide con IC95: T01 c) |
| :417 | "nunca se infiere equivalencia de una diferencia no significativa" | Walker p. 194 (ficha :117), sin cita | T04 |
| :417 | solo el modelo evaluado con su margen es confirmatorio; multiplicidad sin corregir | DEC 2026-10-15 pto 15 | si |
| :419 | lectura en dos niveles, fijada despues de ver las dos versiones | DEC 2026-10-15 (3) pto 1 y cabecera :2653-2655 | si |
| :419 | "un intervalo entero fuera del margen la habria rechazado" | DEC (3) pto 1 (implicito); ninguna ficha (Lakens :125 NO ENCONTRADO) | si como decision propia; no citable (T01 d) |
| :419 | "no permite afirmar equivalencia" | Walker p. 192 "nonequivalence cannot be ruled out" (:84); Fig. 1 (:107) | parcial (T01) |
| :419 | "ni como no equivalencia demostrada" | DEC (3) pto 1; ninguna fila de Evidencia | si como decision propia (T01 d) |
| :419 | `\GAPLIT` lectura de IC que cruza un limite | `walker2011understanding`, `lakens2017equivalence` existen | injustificado en parte (T01) |
| :421 | Delta = max(s_sem, r_rep), formula previa a los valores | DEC 2026-10-11 / #175; Walker p. 194 (:115) no citado | si (T05) |
| :421 | s_sem 196.3 HU, r_rep 6.1 HU | DEC 2026-10-15 pto 21 | si |
| :421 | replicas con titanio difieren en 8 y 27 HU | `resultados_validacion_pose.md`:54 | si |
| :423 | estado final s_sem 115.8 HU | #175 (titulo) | si |
| :423 | margen relativo 0.80-1.25 descartado por elegirse tras ver la razon | DEC 2026-10-15 pto 16 | si |
| :425 | regla asimetrica (no eleva la categoria) | DEC 2026-10-15 regla general :2568 | si |
| :425 | IC90 exacto por permutacion, 2^13 cambios de signo | DEC 2026-10-15 pto 14 | si |
| :425 | mismos cortes; suelo -1000 HU en los dos brazos; sin ROIs a < 20 mm de la cabeza | DEC 2026-10-15 ptos 17, 1, 2 | si |
| :425 | direccion declarada del suelo: hacia la equivalencia | DEC 2026-10-15 pto 1 | si |
| :427 | amplitud de solo ruido de cada brazo (13 x 5 semillas) | DEC 2026-10-15 pto 18 | si |
| :427 | margen minimo de equivalencia = mayor limite en valor absoluto del IC90 | DEC 2026-10-15 pto 16 | si |
| :429 | costura en los dos brazos; perfil de 8-16 mm en anillos de 2 mm | DEC 2026-10-15 pto 5 | si |
| :431 | perfil por anillos 0-12 mm, 3 brazos, razon 0-2/6-8, "plano" si < 2 | `resultados_dec`:182-186 | si |
| :433 | contraste pareado, misma semilla y corte; regla de la mitad en 8-12 mm | `resultados_dec`:172-184 | si |
| :433 | banda completa frente a 196.3 HU, descriptiva | `resultados_dec`:187-188 | si |
| :433 | limite: cambiar M cambia la trayectoria | `resultados_dec`:224-226; DEC (3) pto 3 | si |
| :433 | v2 sin sintesis sin metal | `resultados_dec`:180 | si |
| :435 | Bland y Altman: sesgo y limites +-1.96 DE | `bland1986statistical` (ficha, ya auditada en r23-r24) | si |
| :435 | Pitman y Morgan: varianzas pareadas, normal bivariada, *t* con n-2 gl; Morgan por correlacion suma-diferencia, Pitman estandarizada | #189.4-5; fichas `pitman1939note`, `morgan1939test` | si |
| :437 | dos escalas fijadas despues de ver las dos versiones | DEC (3) pto 2 y cabecera | si |
| :437 | Bland y Altman proponen log si las diferencias son proporcionales | `bland1986statistical` p. 309 (#189.1); tambien `bland1996statistics` :66, :69 | si |
| :437 | "aqui no lo son" | `resultados_dec`:152-157 | si |
| :437 | Pitman y Morgan sobre HU compara varianzas | #189.4 | si |
| :437 | sobre el logaritmo compara aproximadamente los CV | DEC (3) pto 2; `bland1996statistics` solo en parte (log10, antilog-1) | parcial (T02) |
| :437 | `\GAPLIT` var(ln) ~ CV^2 | `bland1996statistics` existe; derivacion a ln propia | injustificado en parte (T02) |
| :437 | CV entre pacientes v1 en prueba: 0.076 y 0.241 | `resultados_prueba_v1.md`:41; `resultados_dec`:39 | si |
| :489-491 | dos tandas del 15 de octubre y lo que fijo cada una | DEC 2026-10-15 cabecera; DEC (3) cabecera y ptos 1-6 | si |
| :515 | IC entero bajo -Delta se leeria como no equivalencia | DEC 2026-10-15 pto 15 | si |
| :523 | 13 pacientes; tres modelos, dos margenes, multiplicidad sin corregir | DEC 2026-10-15 ptos 15-16 | si |
| :525 | cinco limites de la lectura de acuerdo | #189 (1-5); DEC (3) pto 2 | si |
| :525 | pendiente persiste en log | `resultados_dec`:155-156 | si |
| :525 | "solo sobre el logaritmo se lee como comparacion aproximada de CV" | sin cita; ver T02 | T03 |
| :529 | 62 341 frente a 124 679 voxeles | `resultados_prueba_v1.md`:45 | si |
| :529 | piso de ruido 893 frente a 184 HU | `resultados_dec`:69, :78 | si |
| :531 | sentido del piso fijado despues de las dos versiones; favorece al sintetizador | DEC (3) pto 3 | si |
| :531 | -455.0 HU, IC90 -647.6 a -262.5 | `resultados_dec`:221; DEC (3) pto 3 | si |
| refs | `bland1996statistics` = BMJ 313:106 (nota del PDF) | `overleaf/referencias.bib`:81-90; ficha :8-11 | si (el raw duplicado sin espacio, BMJ 312:700, sigue marcado VERIFICAR en el `.bib`:79; lo decide la autora) |
| refs | primer autor Walker (2 autores), Lakens (autor unico), Bland y Altman | `overleaf/referencias.bib`:1314, :663, :81 | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Al cerrar una marca GAP, la prosa que repite el mismo hueco fuera de la marca queda sin revisar | G-T4 | ":525 'solo sobre el logaritmo se lee como comparacion aproximada de CV'" | PAT-168 |
| Al cerrar un `\GAPLIT` con una ficha que cubre un solo eslabon, la cita arrastra la derivacion propia contigua | E-R6, OC-2 | "Pitman y Morgan sobre el logaritmo compara CV \cite{bland1996statistics}" (riesgo) | PAT-194 |
| El rotulo propio de un desenlace coincide con el termino que la fuente citada reserva para otro caso | E-R6, G-T4 | "no concluyente" junto a Lakens, que llama "undetermined" solo al escenario D | nuevo |
| La regla citada decide con un intervalo distinto del que usa la tesis (IC95 frente a IC90) y se cita como si fuera la misma | E-R6 | "si el IC90 excluye el cero, direccion \cite{lakens2017equivalence}" (Lakens usa IC95) | nuevo |
