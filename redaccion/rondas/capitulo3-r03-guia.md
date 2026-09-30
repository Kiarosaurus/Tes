# Revision guia CS — capitulo3 — r03

Leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (PAT-1 a PAT-20 VIGENTES; decisiones de §2 respetadas), `capitulo3-r02-guia.md`, `capitulo3-r02-respuesta.md`, `capitulo3-r03-lint.md`. Cruces: `introduccion.tex` (redactada, desfasada; `\GAPDEC` l. 13, #126), `capitulo1.tex`, `capitulo2.tex` y `capitulo4.tex` (esqueletos).

Respuesta r02: guia-3 a guia-12 y guia-14 (salvo el semimaximo) se aplicaron y no se reportan. guia-1 (condicion de fallo de la prueba de superioridad) y guia-2 (codificacion del sintetizador) quedan cubiertos por `\GAPDEC` (l. 217 y l. 170). guia-13 (50 poses) y la definicion del semimaximo (guia-14) quedaron sin aplicar y con motivo, asi que no se reabren.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T2 | capitulo3.tex:85, 91 | "Recorte por defecto" y "recorte alternativo" de TotalSegmentator nunca se definen: no se dice que se recorta ni con que diferencia. La l. 91 dice que "todas las cifras del Objetivo 2 dependen del recorte por defecto", pero el lector no sabe que parametro es. | En la primera aparicion (l. 85), una oracion que diga que controla el recorte y en que difieren las dos opciones, o una remision a un GAP. |
| guia-2 | media | G-T2 | capitulo3.tex:95 vs 48 | Patron PAT-14 reincide. "Sin objeto metalico" designa al grupo 3, con 66 pacientes en todo el inventario (l. 48). En la l. 95 designa "69 pacientes sin objeto metalico de la carpeta `dataset6`", que es un subconjunto y aun asi tiene mas pacientes. El lector ve una contradiccion. | Nombrar el conjunto de 69 por su criterio real (por ejemplo, el cribado por HU) y no con la etiqueta del grupo 3, o alinear la cifra. El auditor verifica cual es la correcta. |
| guia-3 | media | G-C1 | capitulo3.tex:180 | El supuesto "la relacion entre mascara y artefacto no depende del tipo de implante" permite entrenar con todo el material ortopedico (placas, protesis) y sintetizar solo tornillos. Tiene mucho peso en el diseno y se enuncia sin ninguna justificacion. Tampoco aparece en §Amenazas. | Justificar el supuesto con una fuente o dato. Si no se puede, llevarlo a validez de constructo o externa como supuesto no verificado, o marcar `\GAPDEC`. |
| guia-4 | baja | G-C7 | capitulo3.tex:182, 257 | Los tres desplazamientos de dominio entre entrenamiento y sintesis (l. 182) son amenazas a la validez externa del Objetivo 3, pero la seccion de validez externa (l. 257) solo trata el Objetivo 2 y el protocolo fisico. | Remitir en validez externa a los desplazamientos de l. 182, en una oracion. |
| guia-5 | baja | P-MM1 | capitulo3.tex:223 vs 259 | $\Delta$ se define en l. 223 solo como "variabilidad propia del metodo bajo condiciones que no deberian cambiar el resultado". Que se mide (semillas del sintetizador) y sobre cuantos pacientes (3) aparece por primera vez en amenazas (l. 259). | Pasar a l. 223 la condicion (varias semillas por caso) y los 3 pacientes de validacion, y dejar en l. 259 solo la amenaza. |
| guia-6 | baja | G-T3 | capitulo3.tex:148, 158, 255 | Hay dos dispersiones con subindice, $\sigma_t$ y $\sigma_a$, pero la convencion se escribe "$h = 2\sigma$" sin subindice. Esa $\sigma$ solo equivale a $\sigma_t$, porque $\sigma_a$ se deriva de otra forma. | Escribir $h = 2\sigma_t$, o decir en l. 158 a cual se refiere. |
| guia-7 | baja | G-T2 | capitulo3.tex:114, 121, 200 | "Referencia clinica" se usa desde la Tabla `tab:geometrias` y la l. 121, pero solo en la l. 200 queda identificada de forma explicita con las dos series de Zwingmann et al. | En la primera aparicion, decir que "referencia clinica" son las series navegada y convencional de Zwingmann et al. |
| guia-8 | baja | G-C1 | capitulo3.tex:196 | El recorte de 8 mm en cada extremo del tramo $T$ tiene su razon cualitativa (entrada y salida por la cortical del ilion), pero el valor queda sin justificar. Ese valor controla cuantas poses llegan a grado 3. | Dar la razon del valor si consta en D-O2.3, o marcar que es una convencion propia. |
| guia-9 | baja | G-C6 | capitulo3.tex:52 | La cohorte de sensibilidad excluye al grupo 2 (objetos no ortopedicos), pero no se dice que hipotesis pone a prueba esa exclusion (por ejemplo, el artefacto de esos objetos sobre la segmentacion o el control de nivel). | Una oracion con el motivo de la sensibilidad. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP (arquitectura del sintetizador, algoritmo del eje, heuristica de referencias, ajuste del decodificador) |
| G-T2 | no cumple (guia-1, guia-2 media; guia-7 baja) |
| G-T3 | cumple salvo guia-6 (baja); $c$/$\mathbf{c}$ e $i$/$p$ resueltos |
| G-T4 | cumple salvo guia-2; la exactitud de las cifras es de auditor-trazabilidad |
| G-T5 | cumple (el orden que anuncia la l. 9 coincide con el de las secciones) |
| G-T6 | cumple (el lint no reporta citas faltantes) |
| G-A7 (cruce) | cumple con GAP (evidencia del Obj 4, `\GAPDEC` l. 185; desalineacion con la introduccion, `\GAPDEC` l. 13) |
| G-A8 (cruce) | cumple con GAP (Obj 2, `\GAPDEC` l. 207; superioridad del Obj 3, `\GAPDEC` l. 217); la l. 162 ya distingue los controles de implementacion |
| G-B3 (cruce) | no evaluable (capitulo1 en esqueleto) |
| G-C1 | no cumple a medias (guia-3); $h = 2\sigma$ cumple con GAP; guia-8 baja |
| G-C2 | cumple con GAP (diseno del sintetizador no congelado, l. 170) |
| G-C3 | cumple |
| G-C4 | cumple con GAP (preguntas de la introduccion desfasadas, `\GAPDEC` l. 13) |
| G-C5 | cumple con GAP (inversion de metricas, l. 215); SAP con componentes descriptivos explicitos en la tabla |
| G-C6 | cumple con GAP (regla del Obj 2, copia y pegado, agregacion); guia-9 baja |
| G-C7 | cumple (cuatro tipos, no pro forma, incluye la exploracion previa de la compuerta); guia-4 baja |
| G-C8 | cumple con GAP (agregacion por paciente, intervalo de $W_1$, $\Delta$) |
| G-C9 | cumple con GAP (permanencia del brazo fisico, l. 223; condicion de fallo frente a copia y pegado, l. 217) |
| P-MM1 | cumple en orden y ligazon a objetivos (guia-5 baja); la relacion con el marco teorico no es evaluable |
| P-MM2 | cumple |
| P-MM3 | cumple con GAP (heuristica, eje, ajuste del decodificador, brazo fisico) |

## Propuestas de criterio
- Se mantiene la de r01 y r02: un criterio del bloque (c) que exija, para cada objetivo, una regla de exito o fallo fijada a priori.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una etiqueta de grupo de la cohorte se reusa para un conjunto definido por otro criterio | G-T2 | "69 pacientes sin objeto metalico de la carpeta dataset6" frente a 66 del grupo 3 | PAT-14 |
| Opcion de herramienta nombrada sin decir que controla, aunque de ella dependen resultados | G-T2 | "con la tarea total y el recorte por defecto" | nuevo |
| Supuesto que sostiene el diseno, enunciado sin justificacion y ausente de amenazas | G-C1, G-C7 | "se asume que la relacion entre mascara y artefacto no depende del tipo" | nuevo |
| Parametro del diseno que se presenta por primera vez en amenazas a la validez | P-MM1 | "el margen Delta se medira sobre 3 pacientes de validacion" | nuevo |
