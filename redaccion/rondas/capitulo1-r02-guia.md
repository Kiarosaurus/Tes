# Revision guia CS — capitulo1 — r02

Lecturas cruzadas: `introduccion.tex` (terminos definidos en objetivos), `capitulo2.tex` §2.4-2.5,
`capitulo3.tex` completo. Respuesta previa: `capitulo1-r01-respuesta.md` (0 rechazados; guia-2 escalado
y resuelto con `\GAPDEC`; guia-12 no aplicado por estar en `capitulo3.tex`, no se reabre aqui; titulo de
§1.5 escalado a la autora, no se reporta). Lint r02: PASA, 0/0/0. Los diez medios de r01 se verificaron
aplicados (l.13, l.19-22, l.44, l.62, l.68, l.78, l.112, l.116).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-B3, G-B1 | capitulo1.tex:31, 56, 58 | La ley de Beer-Lambert y el "coeficiente de atenuacion lineal" solo se nombran (l.31), pero l.56 ("efecto exponencial de gradiente de borde") y l.58 ("integrar el flujo y tomar su logaritmo vuelve no lineal la medida") dependen de que la medida sea el logaritmo de una atenuacion exponencial. Un lector de computacion no puede seguir por que esos mecanismos producen rayas. El `\GAPLIT` de l.35 cubre la escala HU y la retroproyeccion filtrada, no la ley de atenuacion; las fichas (`abadi2019`, `wang2019cochlear`) solo la nombran. | Enunciar en una oracion la forma de la ley (decaimiento exponencial con la integral de linea; la medida es su logaritmo) si alguna ficha la sostiene; si no, ampliar el `\GAPLIT` de l.35 para que incluya la ley de Beer-Lambert y el coeficiente de atenuacion lineal. |
| guia-2 | media | G-B2, G-B3 | capitulo1.tex:23, 110-124 (ausente) | El marco desarrolla la metrica del Obj 2 (Wasserstein-1) y la del Obj 1 (error absoluto medio), pero no presenta las metricas de Peters et al. (*streak amplitude*, *bone integrity*, *metal integrity*), resultado previo usado como caja negra y variable dependiente primaria del Obj 3. Solo aparecen en una oracion del cap. 3 (l.213). La fila 5 de la Fig. `fig:mt-conceptos` liga el §1.5 a "los resultados de los Objetivos 1 a 3" sin la magnitud que se compara en el 3. | Un parrafo breve en §1.2 (donde se explican las rayas) o en §1.5 que presente las tres metricas con su definicion desde la ficha `peters2025hybrid`, sus nombres publicados (decision OC, terminos fijos) y la remision a `sec:apariencia`; agregarlas a la fila correspondiente de la figura. |
| guia-3 | baja | G-T2 | capitulo1.tex:106 | El `\GAPDEC` nombra "LeFusion", que el documento presenta recien en el cap. 2 (decision §2: caja mixta nombrada una vez junto al autor). En el cap. 1 el lector no sabe que es. | "...frente a los de Lugmayr et al. y de Zhang et al. (LeFusion, Capitulo 2)" o citar `\cite{zhang2025lefusion}` dentro de la marca. |
| guia-4 | baja | G-T2 | capitulo1.tex:66 | Patron PAT-14 reincide. "su serie" / "En esa serie" designa el estudio completo de Zwingmann et al., mientras l.70 y la decision §2 (capitulo3-r01) reservan "serie" para cada grupo (navegada / convencional). | "En su estudio" / "En ese estudio" en l.66. |
| guia-5 | baja | G-T1 | capitulo1.tex:21 vs 72 | Patron PAT-67 reincide. La fila 3 de la figura liga la "zona segura" al muestreador y a SAP, pero el cuerpo de §1.3 no dice en que pieza interviene, y el cap. 3 no la usa salvo para descartar la estratificacion por fenotipo (l.168). l.11 promete decir para cada concepto donde interviene. | Decir en l.72-74 que la zona segura interviene solo como antecedente del corredor (que es lo que se mide), o quitarla de la fila 3. |
| guia-6 | baja | G-T5 | capitulo1.tex:13 | La oracion de orden ya describe el orden real (PAT-71 corregido) y justifica TC -> artefactos -> difusion, pero no justifica por que §1.3 va entre §1.2 y §1.4: ninguna de las dos depende de ella, y §1.3 remite hacia adelante a §1.5 (l.82). | Una clausula que diga por que la cirugia va antes del modelo generativo (p. ej., el muestreador precede al sintetizador en la cadena), o mover §1.3 si no hay razon. |
| guia-7 | baja | G-B3 | capitulo1.tex:44 | "Las variantes que examina el Objetivo 1 elevan ese techo ... o sustituyen la ventana ancha" omite que la primera de las tres codificaciones usa las ventanas de Wang et al. sin cambio como canales (cap. 3 l.69). El lector no sabe que son tres ni que una es la publicada. | "El Objetivo 1 examina tres codificaciones: las ventanas de Wang et al. como canales, la misma con techo de 20 000 HU y ..." |
| guia-8 | baja | G-T5 | capitulo1.tex:44 | l.11 dice que el capitulo no compara trabajos entre si, pero l.44 contrasta el uso de Wang et al. (cascada, no canales) y su techo de 2000 HU frente al umbral del metal, lo mismo que el cap. 2 (l.82, l.84) hace como comparacion critica. | Dejar en l.44 solo la definicion de codificacion multiventana con las ventanas de Wang et al. como ejemplo, y remitir la comparacion a `sec:ea-representacion`. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple; solo baja (guia-5). Fila 1 de la figura ya respaldada en l.44 (guia-9 r01 aplicado) |
| G-T2 | cumple; solo bajas (guia-3, guia-4). MAE retirado (l.44, 104, 124); brecha cortical unida al cap. 3 (l.78); tipo de tornillo con `\GAPDEC` (l.68) |
| G-T3 | cumple; $N$ / $\mathcal{N}$ queda diferido a la ronda del cap. 3 (guia-12 r01, NO APLICADO con motivo); $\bar\gamma_n$, $n$, $\boldsymbol\xi$, $w_{\min}$, $\Delta$ coherentes con el cap. 3 |
| G-T4 | cumple; Obj 3 con el `\GAPDEC` del cap. 3 (l.112); protocolo fisico en futuro (l.62, l.118); decisiones post hoc segun `sec:amenazas` (l.122) |
| G-T5 | cumple; solo bajas (guia-6, guia-8). PAT-71 corregido |
| G-T6 | cumple (lint y compilacion sin citas indefinidas) |
| G-B1 | no cumple (guia-1); anatomia pelvica cumple con GAP (`\GAPLIT` l.68) |
| G-B2 | no cumple (guia-2); equivalencia sobre el IC del 90 % (l.116) corrige PAT-100 |
| G-B3 | no cumple (guia-1, guia-2); HU y retroproyeccion, arcoseno hiperbolico, Wasserstein-1, Wilcoxon, TOST y remuestreo cumplen con GAP (l.35, l.44, l.114, l.118) |
| G-B4 | cumple (supuesto del dominio de imagen l.60, limite del 2.5D l.108, equiespaciado l.82) |
| P-MT1 | cumple con GAP (muestreo del sintetizador, cortes 2.5D, codificacion adoptada con `\GAPDEC`) |
| P-MT2 | cumple (Fig. `fig:mt-conceptos`; observaciones en guia-2 y guia-5) |
| G-A*, G-B5 a G-B10, G-C*, G-D*, G-R*, P-* de otros bloques | no aplican a esta seccion |

## Propuestas de criterio
- Derivado de G-B2: "cada variable dependiente primaria del bloque (c) tiene su concepto en el bloque
  (b), aunque se defina operativamente en (c)". Hoy queda a criterio del revisor (guia-2).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Ley o modelo solo nombrado, cuya forma usan despues otras oraciones del capitulo, sin enunciarla ni GAP | G-B3, G-B1 | "calculan esa atenuacion con la ley de Beer-Lambert" ... "tomar su logaritmo" | nuevo |
| La metrica primaria de un objetivo falta en el marco teorico mientras las de otros objetivos se desarrollan | G-B2 | §1.5 define Wasserstein-1 y error absoluto medio; *streak amplitude* ausente | nuevo |
| Un termino reservado a una parte se usa para el todo | G-T2 | "En esa serie" (estudio completo) vs "serie navegada" | PAT-14 |
| Celda de figura que liga un concepto a una pieza que el cuerpo no menciona | G-T1 | "zona segura" -> "Muestreador de colocacion (Objetivo 2) y SAP" | PAT-67 |
