# Respuesta del redactor — capitulo1 — r03

Archivo: `overleaf/secciones/capitulo1.tex`. Reportes leidos: `capitulo1-r03-guia.md`, `-estilo.md`,
`-trazabilidad.md`, `-lint.md` (PASA, 0/0/0). Respuesta previa: `capitulo1-r02-respuesta.md`.
Hallazgos sacados por oscilacion: ninguno.

## Altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 (media) | trazabilidad | APLICADO | Se amplia el `\GAPDEC` existente de §1.3 (no se crea otro): "... y si es del mismo tipo que los tornillos de la referencia clinica, que Zwingmann et al. llaman iliosacros y transiliosacros" (ficha `zwingmann2009navigated`:79, :83, :197; #130 punto 5, ya agregado por el orquestador). No se elige tipo de tornillo (regla 3). MAPA fila #130 anota la discrepancia con #130 punto 3 para la autora |
| S01 (media) | estilo | APLICADO | Cifra copiada de `capitulo3.tex`:85: mediana 0.42 de la fraccion de voxeles sacros a 150 HU o menos a lo largo del eje del corredor mas ancho. Partida en dos oraciones por E-O1 |
| S02 (media) | estilo | APLICADO | La definicion ya no atribuye el proposito de conservar el rango del metal: "las anchas conservan el rango de HU y las estrechas separan los contrastes pequenos del tejido" |
| S03 (media) | estilo | APLICADO | Razon de 0.0001, "elegida de forma arbitraria" (ficha `deman1999`:44, :189, Sec. II-D, p. 693) |
| S04 (media) | estilo | APLICADO | Se agrega la consecuencia de la ficha `deman1999`:209 (Sec. III-E): la severidad del ruido depende de cuanta dispersion y endurecimiento haya; las causas no actuan por separado en su simulacion |
| S05 (media) | estilo | APLICADO | "el articulo de De Man et al. no menciona una medida de hasta donde llegan las rayas de ninguna de las causas que estudia" (ficha `deman1999`:80-95, NO ENCONTRADO; decision §2 del 2026-09-30) |
| S06 (media) | estilo | APLICADO | "respecto de la imagen sin metal del mismo caso" (ficha `peters2025hybrid`:56, :173, *ground truth*); "referencia" queda reservada a la referencia clinica |
| S07 (media) | estilo | APLICADO | "Smith et al. juzgan la posicion de un tornillo frente a una posicion ideal. La definen enteramente ..." (partida por E-O1) |
| S08 (media) | estilo | APLICADO | La extension a Guo et al. se dice con su efecto: "con la misma regla y los mismos pacientes de prueba, lo que eleva a siete las combinaciones que pueden aprobar. El veredicto de esa extension se presenta en el capitulo de resultados" (`capitulo3.tex`:75, :265). Se conserva la oracion porque la pidio trazabilidad en r02 (T03); ver guia-1 |

## Bajos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | NO APLICADO | Sacar la oracion de Guo et al. revertiria T03 de r02 (trazabilidad: sin ella, el recuento de oportunidades de aprobar y de decisiones posteriores a ver datos pierde la condicion, PAT-31). La trazabilidad manda sobre la guia en conflicto; la oracion se acorto a su efecto (S08) |
| guia-2 | guia | APLICADO | Se quita la conclusion comparativa sobre Zwingmann et al.; queda el hecho de definicion: binaria, "sin grados de profundidad" |
| guia-3 | guia | APLICADO | En §1.3, parrafo del marco de Kaiser et al.: regla de longitud util de 5 mm a cada lado y holgura de 1 a 2 mm alrededor de un tornillo de 6.3 a 8 mm (ficha `kaiser2014dysmorphism`:80, :167), con "este trabajo lee" y remision a `sec:corredor` (`capitulo3.tex`:83, :89) |
| guia-4 | guia | APLICADO | Cierre del parrafo de Song et al.: el borrador propone el muestreo determinista de Song et al. y no menciona el calendario de ruido; ambos pendientes (`experiments/objetivo3/diseno_A.md`:71, §5 `[SUPUESTO]`; `capitulo3.tex`:172). Sin el numero de pasos del borrador |
| guia-5 | guia | APLICADO | Dentro del `\GAPLIT` de l.122: "... y de su relacion con el intervalo de confianza del 90 %". Ninguna ficha liga el IC del 90 % con TOST |
| guia-6 | guia | APLICADO | Parrafo nuevo al cierre de §1.3: tercer componente de SAP, fraccion por zona de densidad, motivada por Arand et al. (ficha `arand2019pelvicring`, patron cualitativo: ala sacra baja, cuerpo S1 intermedio), reportada de forma descriptiva (`capitulo3.tex`:166, :189), con el `\GAPDEC` de MAPA:39 en el texto de capitulo2 |
| T02 | trazabilidad | APLICADO | "Las tres se disenaron para evaluar MAR, y su uso para evaluar sintesis exige invertirlas (Seccion apariencia)" (`capitulo3.tex`:215) |
| S09 | estilo | APLICADO | "examino" |
| S10 | estilo | APLICADO | Razon de la convencion de $B_\delta$ |
| S11 | estilo | APLICADO | Abre con "Las fuentes revisadas no juzgan la colocacion con una misma escala." |
| S12 | estilo | APLICADO | "en un modelo entrenado con el objetivo de Ho et al." |
| S13 | estilo | APLICADO | Oracion partida en dos |
| S14 | estilo | APLICADO | "si un brazo supera al otro" |
| S15 | estilo | APLICADO | Margen "fijado por la variabilidad entre semillas del sintetizador y entre corridas repetidas del protocolo fisico" (`capitulo3.tex`:225) |
| S16 | estilo | APLICADO | "y en el Objetivo 2 hubo tres" |

Conteo altos/medios: 9 APLICADOS, 0 RECHAZADOS, 0 ESCALADOS. Bajos: 15 aplicados, 1 no aplicado (guia-1).

## GAP

- Abiertos: 1 `\GAPDEC` en §1.3 (fraccion por zona de densidad de SAP; mismo texto que `capitulo2`, MAPA:39).
- Ampliados: `\GAPDEC` #130 (T01, MAPA:81); `\GAPLIT` de Wilcoxon/TOST/remuestreo (guia-5, MAPA:77; el candidato ya esta PENDIENTE en `_candidatos.md`).
- Cerrados: ninguno.
- Totales del lint: lit=4, dato=1, dec=8.

Lint final: `python scripts/lint_redaccion.py capitulo1 --compilar` -> PASA, alta=0 media=0 baja=0 (107 paginas).
Correcciones laterales: cinco oraciones que las correcciones dejaron sobre el limite de E-O1 se partieron (l.35, l.80, l.82, l.88, l.126).

## Decisiones de redaccion

- La *ground truth* de Peters et al. se dice "la imagen sin metal del mismo caso"; nunca "imagen de referencia" (PAT-14).
- Si un revisor de guia pide quitar una oracion que trazabilidad pidio agregar en una ronda anterior, se conserva y se reduce a su efecto sobre el criterio del parrafo.
- Un parametro que solo propone el borrador de diseno (`diseno_A.md`, `[SUPUESTO]`) se nombra como propuesta del borrador ("el borrador del diseno propone"), nunca como diseno fijado, y con remision al `\GAPDEC` de congelar el diseno del sintetizador.
