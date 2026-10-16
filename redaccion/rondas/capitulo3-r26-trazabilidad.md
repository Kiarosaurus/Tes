# Auditoria de trazabilidad — capitulo3 — r26

Entrada: `overleaf/secciones/capitulo3.tex`, que no cambió desde r25: el lint r26 da los mismos 19 `\GAPDATO` y las
mismas 25 bajas E-P1. Encargo: `redaccion/ENCARGO_2026-10-15c.md`. Fuentes nuevas cotejadas:
`experiments/registro/registro_metodos_2026-10-15.md` (REG), `experiments/objetivo2/e15_w1_sensibilidad.md` (E15),
`experiments/registro/r_razon_banda_run04.py` (RRB), `docs/01-decisiones.md` 2026-10-15 (4) (DEC4, l. 2696-2715),
`docs/04-implicancias.md` #184, #193, #194 y #195 (l. 12252, 12438, 12457 y 12470), y la ficha
`docs/literatura/haber2008general.md` (HAB). Abreviaturas: DEC1 = DEC 2026-10-15 (l. 2559-2634); DEC3 = DEC 2026-10-15 (3)
(l. 2650-2694); RD = `experiments/objetivo3/resultados_dec_2026-10-15.md`; EXP3 = `experiments/objetivo3/EXPERIMENTOS.md`.

Respuesta previa (r25): no re-reporto nada que esté RECHAZADO. T05 de r25 quedó "No aplicada" a propósito, y no la
re-abro.

**Resultado del encargo, por GAPDATO** (19 en total):
- **Las nuevas fuentes cierran 10:** :85 (en parte, ver T03), :105, :111, :115, :218, :262, :291 (la segunda, #184),
  :423 (#194), :531 y, por arrastre, la cifra fuera de marca de :228.
- **Siguen justificados 9:** :38 y :453 (realismo; EXP3:110 "POR ESCRIBIR"; DEC 2026-10-09, l. 2394, "Hoy faltan 8"),
  :48 (REG no lo cubre), :188 (REG no lo cubre), :281 (#178 ABIERTA), :291 (la primera, comparación a ciegas sin
  script, EXP3:110), :343 (D9; EXP3:109 "falta D9"), :509 x2 (REG no lo cubre; #138 ABIERTA) y :515 (#176 ABIERTA).
- **#193 (ABIERTA):** los pasajes de realismo visual están en `\REVVISUAL`, con una excepción: :214 y :264 afirman fuera
  de la marca que la banda basta y que el truncamiento está acotado, cosa que #193 cita como evidencia en contra (T12).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2 | :423 | "ese intervalo se calculó ... \GAPDATO{calculado; consta en una implicancia abierta (implicancia 194)}" | #194 (l. 12457: "DECIDIDA 2026-10-15 (4) pto 1"); DEC4 pto 1 (l. 2705: "IC95 [-516.2, -85.7] HU, excluye 0"); RD:235; REG §9 | Los patrones PAT-19 y PAT-11 reinciden. El GAP se escribió con #194 ABIERTA (BITACORA §2, r23/r25). #194 ya está DECIDIDA y DEC4 ordena escribir la lectura en el cap. 3. La cifra existe | Retirar el `\GAPDATO` y escribir: "Para la versión~1, ese intervalo, calculado sobre los mismos 13 pacientes, va de $-516.2$ a $-85.7$~HU y excluye el cero: el resultado es el caso diferente y no equivalente de Lakens~\cite{lakens2017equivalence}". Fuente en la respuesta: RD:235 |
| T02 | media | G-T4, OC-2 | :291 (2.ª marca) | "\GAPDATO{lectura de la reconstrucción ... versión~2: calculada; consta en una implicancia abierta (implicancia 184)}" | #184 (l. 12252: "DECIDIDA 2026-10-15 (4) pto 2"); DEC4 pto 2 (l. 2707-2708); RD:104-116 | Los patrones PAT-11 y PAT-122 reinciden. La lectura ya está decidida: lado a lado, exploratoria; la ventaja de run05a desaparece con 0.03 y la de run05b se sostiene en parte, 9 de 13 | Retirar el `\GAPDATO`. Sin cifras en el cap. 3, que reserva los resultados de prueba: "...y sus resultados se presentan junto a los de la versión~1, lado a lado y sin elegir ganador, en el capítulo de resultados". Si se quiere dar la lectura: con el límite de 0.030, la ventaja del modelo con sobremuestreo desaparece y la del modelo con canal se mantiene en 9 de 13 pacientes (RD:110-114). Hay que nombrar los modelos con los términos del capítulo, no "run05a/b" |
| T03 | media | G-T4, OC-2 | :85 | "\GAPDATO{parámetros del ajuste del decodificador ... el resto solo como valores por omisión ...}" | REG §2 (l. 18-31); verificado contra `p1_decodificador_sd15.py`:750-759 (`--pasos` 30\_000, `--lote-entreno` 4, `--lr` 1e-4, `--warmup` 500, `--semilla` 0) | El patrón PAT-19 reincide: REG registra la pérdida L1; AdamW con lr $10^{-4}$, 500 pasos de calentamiento y sin decaimiento de pesos; un lote de 4 cortes; y la parada por número fijo, 30\,000 pasos (1-2 épocas). PAT-133: el "número de cortes" del GAP no consta como total. REG solo dice "cortes axiales completos de los pacientes `train`" y una reserva de mezcla de 3\,000 cortes | Sustituir el GAP por la descripción de REG §2. Para el total de cortes queda un GAP reducido: `\GAPDATO{número total de cortes de entrenamiento del decodificador}`. Otra opción es no dar total y decir "30\,000 pasos de 4 cortes, entre una y dos épocas". La reserva de 3\,000 cortes no debe presentarse como el número de cortes |
| T04 | media | G-T4, OC-2 | :105 | "\GAPDATO{descripción completa del algoritmo de búsqueda del eje del corredor ...}" | REG §3 (l. 33-48), fuente `e9ts_corredor.py` + `e9_corredor.py` | El patrón PAT-19 reincide: el algoritmo ya está registrado. Se buscan centros en una rejilla de 3 mm en el plano sagital de S1 (de 3 a 75 mm bajo el platillo; de 45 mm detrás a 10 mm delante), con 81 direcciones de ±20° en pasos de 5°. Cada tramo óseo es continuo, con salida a tejido blando por los dos extremos. Se toma la trayectoria de $D$ máximo | Retirar el GAP y resumir REG §3, pasos 2-5, en dos o tres oraciones. Lo que ya está en :105 no se repite: la envolvente, $D = 2\times$ la distancia mínima y la exclusión de 8 mm. Separar S1 de S2 por picos a $\geq 12$ mm es una heurística declarada en REG; si se nombra, va como tal |
| T05 | media | G-T4, OC-2 | :115 | "\GAPDATO{descripción de la heurística de localización de las referencias anatómicas ...}" | REG §4 (l. 50-61), fuente `r1_landmarks.py` v2 2026-09-10 | El patrón PAT-19 reincide. La heurística está registrada: crestas, platillo de S1, EIPS y la legibilidad por esfera de 12 mm, con fracción oscura bajo $-200$ HU y brillante sobre 2500 HU. REG la califica de "cota superior de localizabilidad, revisada por láminas" | Retirar el GAP y resumir REG §4. Mantener la salvedad de :117 ("La localización heurística de crestas y espinas ilíacas no se ha revisado clínicamente"): REG dice revisada por láminas, no por un clínico. Hay que cotejar que ambas cosas no se contradigan |
| T06 | media | G-T4, OC-2 | :218 | "razón de 0.62 ... \GAPDATO{razón de parches de solo banda ... modelo evaluado ...}" | REG §7 (l. 76-79); RRB (control `(14182, 39)`, l. 19-20) | El patrón PAT-19 reincide. La razón del modelo evaluado está medida: 5\,526 parches de solo banda frente a 8\,656 con metal, razón 0.638, sobre los 14\,182 parches de 39 casos (coincide con :220). Antes de los retiros era 0.620 | Retirar el GAP: "...que estaban en razón de 0.62 en el conjunto al que se aplicó el criterio y de 0.638 en el conjunto de entrenamiento del modelo evaluado (5\,526 frente a 8\,656 parches)". Fuente en la respuesta: REG §7 / RRB |
| T07 | media | G-T4 | :228 | "Son 0.62 frente a 1.40 ... la primera razón se midió en el conjunto anterior" | REG §7 (0.638 en run04) | El patrón PAT-168 aparece de forma preventiva: si T06 cierra la marca, esta oración repite fuera de la marca el hueco ya cerrado y deja la cifra vieja como la del modelo | "Son 0.638 frente a 1.40 parches de solo banda por parche con metal" y retirar la salvedad de la medición previa. El 1.40 sigue saliendo de #112 (l. 7514), una cifra calculada del corredor, sin cambios |
| T08 | media | G-T4, OC-2 | :262 | "\GAPDATO{procedimiento del intervalo del 90\,\% del exceso por anillo ... solo consta en el código ...}" | REG §5 (l. 63-67); verificado en `d1_alcance_rayas.py`:156-161 (`B: int = 2000`, `np.nanpercentile(meds, 5/95)`) | El patrón PAT-19 reincide: el procedimiento está registrado. Se agrega por medianas (corte, componente, paciente). El IC90 de la mediana entre pacientes sale de remuestrear pacientes con reemplazo, 2\,000 veces, con los percentiles 5 y 95 | Retirar el GAP: "Ese intervalo es el de la mediana entre pacientes, por remuestreo de pacientes con reemplazo (2\,000 remuestreos, percentiles 5 y 95)" |
| T09 | media | G-T4, OC-2 | :111 | "se añade un análisis de sensibilidad sin ellos \GAPDATO{análisis de sensibilidad ... sin los dos casos ...}" | E15 l. 8 (70 casos, 3\,500 poses; W1 0.203 navegado, 0.237 convencional); REG §8; DEC4 pto 4; DEC 2026-10-08 pto 22 (l. 2143: `CLINIC_0022`, `CLINIC_0024`) | Los patrones PAT-19 y PAT-122 reinciden: la sensibilidad ya se corrió | Retirar el GAP. El cap. 3 no da las W1 primarias, que quedan para el cap. 4. Por eso basta con "...y se añade un análisis de sensibilidad sin ellos, con 70 pacientes, cuyo resultado se presenta en el capítulo de resultados". Si se dan cifras, van con su condición (PAT-31): $d = 7.0$ mm, posterior y descriptiva |
| T10 | media | G-T4, OC-2 | :531 | "con un intervalo por remuestreo de pacientes ... \GAPDATO{intervalo por remuestreo ... Wasserstein-1}" | E15 l. 10-12 (IC95, 2\,000 remuestreos, percentiles, semilla 20261015: navegado [0.152, 0.313], convencional [0.089, 0.364]); REG §8 | Los patrones PAT-19 y PAT-122 reinciden: el intervalo está calculado. El texto no dice su nivel (95 %). E15 l. 12 agrega un límite que el capítulo no recoge: el intervalo no incluye la incertidumbre de las series de referencia (26 y 35 tornillos), que se tratan como fijas. Ese límite pertenece justo a esta amenaza | Retirar el GAP: "...con un intervalo del 95\,\% por remuestreo de pacientes (2\,000 remuestreos), un análisis descriptivo que no estaba preinscrito. Ese intervalo refleja la variación entre pacientes de la cohorte local y trata como fijas las dos series de la referencia clínica". La lectura de REG §8 ("los intervalos se solapan") es un resultado y va al cap. 4 |
| T11 | media | OC-3, G-T4, E-R6 | :427, :429, :533, :537 | "Se fijó con una fórmula decidida antes de ver ningún valor, $\Delta = \max(s, r)$" | #195 (l. 12489-12492: DECIDIDA opción (a)); DEC4 pto 3 (l. 2709-2710); HAB (Evidencia: "The numerator is the average disagreement", p. 153; "they increase with the within-method variability", p. 168; `max(s,r)` NO ENCONTRADO EN EL PDF) | La decisión no está aplicada. El texto ya recoge tres puntos: margen más ancho con más variabilidad (:429), 2 pacientes y medianas de 5 semillas (:537), y que no es la diferencia clínicamente aceptable (:533). Faltan dos: (1) presentar $\Delta$ como convención inspirada en el acuerdo individual de `haber2008general`, que no se cita en ninguna parte; (2) declarar que `max(s, r)` no es la regla de esa fuente y que $s$ y $r$ son estimadores heterogéneos. La fuente usa el promedio sin referencia y solo la referencia con referencia. $s$ es el rango entre 5 semillas y $r$ es $|A-B|$ de 2 réplicas | En :427, tras la fórmula: "Es una convención de este trabajo, inspirada en la idea de Haber y Barnhart~\cite{haber2008general} de comparar el desacuerdo entre métodos con el desacuerdo entre réplicas de cada método." En Amenazas (:537): "Haber y Barnhart no usan el máximo: sin método de referencia promedian los dos desacuerdos intramétodo y, con referencia, usan solo el de la referencia; además, sus coeficientes crecen con la variabilidad intramétodo. Los dos términos del margen son además estimadores distintos: un rango entre cinco semillas y una diferencia entre dos réplicas." El patrón PAT-194 es un riesgo: no hay que atribuir `max`, el rango ni el TOST a Haber y Barnhart (HAB l. 93-95) |
| T12 | alta | OC-3, OC-2 | :214 y :264 | "La banda de 12~mm alcanza, entonces, para el artefacto real de estas piezas" | #193 ABIERTA (l. 12443-12444: "`B_delta` de 12 mm trunca rayas que en lo real cruzan el corte"); BITACORA §2 2026-10-15 (capitulo2-r08, l. 455: entra en `\REVVISUAL` el "truncamiento y suficiencia de $B_\delta$"); capitulo3-r25-estilo:34 lo derivó a trazabilidad | Los patrones PAT-191 y PAT-195 reinciden. :264 da por suficiente la banda, y :214 da el truncamiento por acotado ("Una medición propia posterior acota ese truncamiento..."). Las dos afirmaciones quedan fuera de `\REVVISUAL`. Una implicancia ABIERTA posterior cita el truncamiento de la banda como evidencia en contra. :517 dice lo mismo pero sí está envuelta, así que el capítulo es incoherente consigo mismo. r25 no lo atendió | Envolver en `\REVVISUAL` la oración de :214 ("Una medición propia posterior acota...") y en :264 las oraciones "La banda de 12 mm alcanza, entonces, ... y la opción de ensancharla se descartó: el déficit medido está dentro de la banda y no en su ancho". Acotar :264 a lo medido: "En componentes del tamaño de un tornillo, el exceso real no se separa del control nulo más allá de 10~mm" (DEC (2) / D1), sin "alcanza". La decisión de no ensancharla es un hecho de diseño de v2 y puede quedarse fuera de la marca si se redacta como decisión y no como suficiencia |
| T13 | alta | G-T4, OC-5 | :252 | "El control sobre parches reales resultó trivial, porque su ida y vuelta es exacta" | RD:125 ("cambio de decodificación mueve el p95 0.00 HU ... cumple, pero es trivial"); EXP3:108 (`a28_diag_p95.py` "control real en `metal_0039`" CORRIDO); EXP3:110 ("(sin script) ... control con imágenes reales de D7 ... POR ESCRIBIR") | Las dos fuentes discrepan entre sí. EXP3:110 da como no hecho el control que EXP3:108 y RD:125 dan como corrido. El texto copia la versión correcta (RD), pero EXP3 contradice una afirmación del capítulo. El patrón PAT-158 reincide | El texto no se toca. La autora corrige EXP3:110 y quita "control con imágenes reales de D7" de la fila sin script. Se reporta para que la fuente de contenido quede alineada (overleaf/CLAUDE.md regla 5) |
| T14 | media | OC-5, G-T4 | :111, :218, :262, :531 (al cerrar T06-T10) | cifras nuevas 0.638, 0.203/0.237, [0.152, 0.313], [0.089, 0.364] | `experiments/objetivo2/EXPERIMENTOS.md` (sin "e15"); EXP3 (sin `registro/`) | Los patrones PAT-138 y PAT-158 reinciden. La regla 5 de overleaf/CLAUDE.md pide que las cifras propias se copien de `tesis/main.tex` o de `experiments/*/EXPERIMENTOS.md`. Ni E15 ni REG/RRB tienen fila en un `EXPERIMENTOS.md` (REG vive en `experiments/registro/`, sin índice) | Al aplicar T06-T10, citar en la respuesta del redactor la ruta exacta (E15 l. 8 y 10; REG §5, §7 y §8; RRB). La autora agrega filas a `objetivo2/EXPERIMENTOS.md` (e15) y a `objetivo3/EXPERIMENTOS.md` (r_razon_banda_run04) |

## Inventario
Texto sin cambios desde r25. Las unidades que no tocan las fuentes nuevas, sus decisiones ni los GAP se heredan del
inventario de `capitulo3-r25-trazabilidad.md` y `capitulo3-r24-trazabilidad.md`. Abajo se recotejan todas las marcas
GAP, todas las unidades que tocan REG, E15, RRB, DEC4, #184, #193, #194, #195 y HAB, y las cifras del análisis
estadístico y de las amenazas del Objetivo 3.

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :38 | `\REVVISUAL`+`\GAPDATO` contraste de realismo sin script | EXP3:110 "POR ESCRIBIR"; #193 ABIERTA | si (GAP justificado) |
| :38 | v2: evaluación en prueba ejecutada salvo comparación a ciegas | EXP3:96 "CORRIDA"; EXP3:110 | si |
| :48 | `\GAPDATO` revisión multiplanar | REG no lo cubre; MAPA:64 | si (justificado) |
| :54 | media cambia a lo sumo 2.3 HU sin el paciente | heredado r24/r25 | si (sin cambio) |
| :85 | `\GAPDATO` ajuste del decodificador | REG §2; `p1_decodificador_sd15.py`:750-759 | no (T03) |
| :85 | ventanas $[-1000,2000]$, $[-320,480]$, $[-160,240]$; techo 20\,000; asinh | REG §1 (l. 11-14) | si |
| :105 | `\GAPDATO` algoritmo del eje del corredor | REG §3 | no (T04) |
| :105 | cierre de 2 mm, exclusión de 8 mm, $D$ = doble de la distancia mínima | REG §3 pasos 1 y 4 | si |
| :111 | 16 casos: 14 conformes, 2 fallan con ambos recortes | MAPA:56; #123/#131 | si |
| :111 | `\GAPDATO` sensibilidad sin los dos casos | E15 l. 8; DEC 2026-10-08 pto 22 (l. 2143) | no (T09) |
| :115 | `\GAPDATO` heurística de referencias | REG §4 | no (T05) |
| :115 | región contaminada por fracción oscura o de metal | REG §4 l. 60 (< -200 HU; > 2500 HU) | si |
| :188 | `\GAPDATO` segundo corredor; 69 de 72 con eje | MAPA:66; REG no lo cubre | si (justificado) |
| :200 | 225.0 HU (p95) y 1.2 HU (mediana); $\Delta = 196.3$ | DEC1 pto 1 (l. 2572); DEC1 pto 21 (l. 2633) | si |
| :206 | lote de 16 (corrige el 4) | DEC1 pto 3 (l. 2578-2579) | si |
| :214 | truncamiento acotado por medición posterior | #193 ABIERTA | no (T12) |
| :216 | $-0.24$ mm, RIC $-0.54$ a 0.02; 32 componentes, 23 pacientes | RD §D4 (l. 5); DEC1 pto 4 | si (heredado r24) |
| :218 | razón 0.62 antes de los retiros | REG §7 ("0.620 antes de las retiradas") | si |
| :218 | `\GAPDATO` razón del modelo evaluado | REG §7; RRB | no (T06) |
| :220 | 14\,182 parches, 39 casos | RRB l. 19 (control); REG §7 | si |
| :228 | 0.62 frente a 1.40 | REG §7 (0.638); #112 l. 7514 (1.40) | no (T07) |
| :248 | 7 de 12 cáscaras; p50/p95 3245/4856, 3402/4848; 497 frente a 648 HU | heredado r24/r25; `\REVVISUAL` en la 1.ª oración | si |
| :250-252 | regla de D7: $\geq 4$ de 7; resultado 1 de 7; control trivial | DEC1 pto 7 (l. 2587-2591); RD:123-126; DEC3 pto 6 | si en texto; fuentes discrepan (T13) |
| :254 | 1164/1163 frente a 1248/1182; Ti 1881/1287 | heredado r24/r25 | si |
| :258 | `\REVVISUAL` atenuación desde unos 4 mm | #193 | si (marcado) |
| :262 | `\GAPDATO` IC90 por anillo | REG §5; `d1_alcance_rayas.py`:156-161 | no (T08) |
| :264 | 1930, 1199, 765, 473, 174 HU (real) | DEC 2026-10-15 (2) l. 2645 | si |
| :264 | "La banda de 12 mm alcanza ... para el artefacto real" | #193 ABIERTA | no (T12) |
| :281 | `\GAPDATO` cortes convexos (#178) | #178 ABIERTA (l. 12104) | si (justificado) |
| :287 | $E$ 532.8 / 418.2 / 367.0; 284 y 540 frente a 233.0, tope 279.6 | heredado r24/r25 | si |
| :289 | `\REVVISUAL` juicio visual de la autora | #193 | si (marcado) |
| :291 | margen común 196.3; límite 0.030 para v2 | DEC1 pto 16 (l. 2620-2622); pto 19 (l. 2628-2629) | si |
| :291 | `\REVVISUAL`+`\GAPDATO` comparación a ciegas sin script | DEC1 pto 10; EXP3:110 | si (justificado) |
| :291 | `\GAPDATO` lectura de E-A1 de v2 (#184 "abierta") | #184 DECIDIDA; DEC4 pto 2; RD:104-116 | no (T02) |
| :343 | 5 poses, sintetizador, 5 semillas; expectativa sin umbral | DEC1 pto 9 (l. 2595-2599) | si |
| :343 | `\GAPDATO` resultado del exploratorio con poses | EXP3:109-110 ("falta D9") | si (justificado) |
| :359, :361, :363 | `\REVVISUAL` lector, QC y contraste de realismo | #193; BITACORA §2 l. 455 y 464 | si (marcado) |
| :415 | Wilcoxon de una cola; $2^{-13}$; sin tamaño de efecto | DEC1 pto 12 (l. 2608-2609) | si |
| :417 | TOST pareado, Ti, $\Delta = 196.3$, IC90 *t* con supuesto | DEC1 ptos 14, 15 y 21 | si |
| :419 | tres desenlaces; dirección si el IC excluye 0; solo el modelo evaluado es confirmatorio | DEC1 pto 15 (l. 2615-2619); DEC4 pto 1 | si |
| :419 | Walker y Nowacki: no significativo => no puede descartarse la equivalencia | `walker2011understanding` (verificado r25, ficha :117) | si |
| :421 | mapeo con Walker ("equivalence not established") y Lakens (B "undetermined") | DEC4 pto 1 (l. 2702-2706); #194; fichas (verificadas r25) | si |
| :423 | `\GAPDATO` IC95 v1 | RD:235; REG §9; DEC4 pto 1 | no (T01) |
| :425 | dos niveles; "no concluyente" no es equivalencia ni no equivalencia demostrada | DEC3 pto 1 (l. 2658-2662) | si |
| :427 | $\Delta = \max(s,r)$ fijado antes; $s = 196.3$, $r = 6.1$; Ti 8 y 27 HU | DEC1 pto 21 (l. 2632-2633); Ti heredado r24 | si en cifras; falta #195 (T11) |
| :429 | estado final $s = 115.8$; margen 0.80-1.25 descartado | DEC1 pto 16 (l. 2622-2623); 115.8 heredado r24 | si |
| :431 | regla asimétrica; IC90 por permutación $2^{13}$; mismos cortes; suelo; 20 mm de la cabeza | DEC1 regla general (l. 2568-2569), ptos 2, 14, 17 y 1 | si |
| :433 | piso de ruido; margen mínimo de equivalencia | DEC1 ptos 18 y 16 | si |
| :435 | costura en dos brazos; anillos de 8 a 16 mm | DEC1 pto 5 (l. 2583-2584) | si |
| :437 | perfil por anillos 0-12 mm; razón 0-2/6-8; plano si < 2 | DEC3 pto 4 (l. 2673-2677) | si |
| :439 | contraste pareado; 8-12 mm; límite de la trayectoria DDIM | DEC3 ptos 3-4 | si |
| :441 | Bland y Altman, sesgo ± 1.96 DE; Pitman y Morgan, *t* con $n-2$ | `bland1986statisticalmeasurement`, `pitman1939note`, `morgan1939test` (verificados r24/r25) | si |
| :443 | dos escalas; Pitman y Morgan sobre HU y sobre ln | DEC3 pto 2 (l. 2663-2667) | si |
| :445 | Bland y Altman 1996: log si DE proporcional; antilog(DE) - 1 ≈ CV; log10 y duplicados; derivación propia sin cita | `bland1996statisticsmeasurement` (verificado r25); #194 l. 12463-12464 | si |
| :447 | CV 0.076 y 0.241; 0.496 "too large" | #185 (l. 12286); ficha (verificada r25) | si |
| :451, :453 | `\REVVISUAL`+`\GAPDATO` lista de pacientes de realismo | DEC 2026-10-09, l. 2394 ("Hoy faltan 8"); #193 | si (justificado) |
| :469 | Tabla, fila 2: "IC por remuestreo de pacientes, no preinscrito" | E15 l. 3 y 10 (POSTERIOR, descriptivo, IC95) | si (puede añadirse "del 95 %", baja, ya cubierta en T10) |
| :479 | sensibilidad sin los dos casos e intervalo, posteriores a los datos | E15 l. 3; DEC4 pto 4 | si |
| :481 | 7 de 15 frente a 2 de 15, $p = 0.109$, Fisher bilateral | REG §6 (reproduce 0.109, *minlike*) | si |
| :499-501 | dos momentos del 15 de octubre; listas de decisiones | DEC1 cabecera (l. 2563-2566); DEC3 cabecera (l. 2653-2656) | si |
| :509 | `\GAPDATO` canal sacro y forámenes | REG no lo cubre | si (justificado) |
| :509 | `\GAPDATO` techo de S1 frente al platillo | #138 ABIERTA; MAPA:59 | si (justificado) |
| :515 | `\REVVISUAL`+`\GAPDATO` estructura direccional (#176) | #176 ABIERTA (l. 12039) | si (justificado) |
| :517 | `\REVVISUAL` banda y truncamiento | #193; DEC (2)/D1 | si (marcado; incoherente con :214/:264, T12) |
| :523, :525, :529 | `\REVVISUAL` suelo frente a realismo, brazos desplazados, tipo de tornillo | #193 | si (marcado) |
| :531 | `\GAPDATO` intervalo W1 | E15 l. 10 | no (T10) |
| :533 | margen ≠ diferencia clínicamente aceptable (Walker y Nowacki) | `walker2011understanding` (ficha :85, verificada r25); #195 | si |
| :537 | 2 pacientes; rango de semillas sueltas frente a mediana de 5 | #195 decisión (l. 12491-12492) | si en parte; falta la heterogeneidad $s$/$r$ y Haber (T11) |
| :539 | 62\,341 y 124\,679 vóxeles; piso 893 frente a 184 HU | DEC3 pto 3 (l. 2668-2669); vóxeles heredado r24 | si |
| :541 | $-455.0$ HU, IC90 $[-647.6, -262.5]$ | DEC3 pto 3 (l. 2671) | si |
| todo el cap. | contenido retirado (Dice/HD95 como objetivo, difusión latente/ControlNet vigente, "31-60 %", BFC/ISC) | :36 (fuera de alcance), :87, :202 (descartados) | si (sin contradicción) |
| claves `\cite` nuevas o afectadas | `walker2011understanding`, `lakens2017equivalence`, `bland1996statisticsmeasurement`, `bland1986statisticalmeasurement`, `pitman1939note`, `morgan1939test`; `haber2008general` existe (referencias.bib:472) pero no se cita | `overleaf/referencias.bib` | si (claves existen; primer autor = apellido nombrado; E-F3 respetado: "Walker y Nowacki~\cite", "Lakens~\cite", "Bland y Altman~\cite") |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que remite a una implicancia "abierta" ya decidida y con cifra disponible | G-T4, OC-2 | "\GAPDATO{calculado; consta en una implicancia abierta (implicancia 194)}" | PAT-11 / PAT-19 |
| GAPDATO de "consta solo en el código" se mantiene después de que un registro de métodos lo documenta | G-T4, OC-2 | "solo consta en el código del experimento y no en un registro" | PAT-19 |
| Suficiencia o truncamiento de $B_\delta$ afirmados fuera de `\REVVISUAL` mientras otro pasaje los envuelve | OC-3, OC-2 | "La banda de 12 mm alcanza, entonces, para el artefacto real" | PAT-191 / PAT-195 |
| Al cerrar un GAP de razón o cifra, la misma cifra vieja sobrevive en otro párrafo fuera de la marca | G-T4 | "Son 0.62 frente a 1.40 ... se midió en el conjunto anterior" | PAT-168 |
| Decisión DECIDIDA que pide citar una fuente de respaldo conceptual queda sin la cita ni sus límites | OC-3, E-R6 | $\Delta = \max(s,r)$ sin `haber2008general` ni "no es la regla del paper" | nuevo |
| Resultados nuevos en `experiments/registro/` o en un `.md` suelto sin fila en `EXPERIMENTOS.md` | OC-5, G-T4 | e15 y r_razon_banda_run04 sin fila en los índices | PAT-138 / PAT-158 |
