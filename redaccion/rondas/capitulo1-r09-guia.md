# Revision guia CS — capitulo1 — r09

Entrada: `overleaf/secciones/capitulo1.tex`, lint `capitulo1-r09-lint.md` (PASA, 1 GAPDATO y 1 GAPDEC),
respuesta `capitulo1-r08-respuesta.md` (sin RECHAZADOS) y encargo `redaccion/ENCARGO_2026-10-15.md`
(DEC 2026-10-15). Para coherencia se leyeron `introduccion.tex` (objetivos) y `capitulo3.tex`
(:91, :157-160, :198, :202, :375-377, :419, :451).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T4, G-B4 | capitulo1.tex:48 | Patron PAT-19 reincide (y PAT-133). El `\GAPDEC` del suelo pregunta como convertir la perdida a HU y que hacer si es mayor, pero DEC 2026-10-15 (1) cierra las dos partes: la regla es no aplicable y la sustituyen analisis posteriores. | Quitar la marca entera. Decir en una frase que la regla quedo no aplicable (su desenlace dependia del percentil elegido y su rama de cambio la bloquea el congelamiento) y que el efecto del suelo se mide en el contraste primario, posterior, con remision a `sec:sintetizador`/`sec:amenazas`. Sin cifras nuevas (encargo). |
| guia-2 | media | G-T4, G-B3 | capitulo1.tex:58 | Patrones PAT-116 y PAT-11 reinciden. «Depende de una regla preinscrita cuyo desenlace aun no se conoce»: la DEC de 2026-10-15 (1) declara la regla no aplicable y fija con que se trata el suelo. | Sustituir por una remision al tratamiento vigente («el efecto de ese suelo se mide en el contraste primario, Seccion X»), sin repetir lo que dice :48. |
| guia-3 | media | G-T4 | capitulo1.tex:66 (y :33) | Patron PAT-122 reincide. «Preve usar el protocolo fisico como comparacion» contradice :130 («se preinscribio y ejecuto como contraste primario»). En :33, «previsto» admite la misma lectura. | Pasar a hecho («usa el protocolo fisico como comparacion») en :66, y en :33 «descrito» en vez de «previsto». |
| guia-4 | media | G-B2, G-B3 | capitulo1.tex:128-130 | El marco solo enuncia el desenlace «equivalencia» y cierra con «puede no concluir ni equivalencia ni diferencia». DEC 2026-10-15 (15) fija tres desenlaces (equivalencia, no equivalencia, no concluyente) y obliga a reportar la direccion cuando el IC90 excluye 0. El resultado de v1, «no concluyente con diferencia significativa a la baja», no se puede leer con este aparato, y la ultima oracion lo contradice. | Definir los tres desenlaces por la posicion del IC90 respecto de $\pm\Delta$ y añadir que, si el IC90 excluye 0, se informa la direccion aunque el desenlace sea no concluyente. Quitar «ni diferencia». |
| guia-5 | media | G-B2 | capitulo1.tex:128-130 | Patron PAT-129 reincide. El capitulo 3 (:377) calcula el IC90 del TOST con la *t* de Student sobre 13 diferencias pareadas, y DEC 2026-10-15 (14) añade el IC exacto por inversion de la prueba de permutacion pareada. El marco no presenta ninguno de los dos ni el supuesto de la *t*. | Una o dos oraciones: el IC90 se obtiene con la *t* y supone diferencias pareadas aproximadamente normales e independientes; la alternativa sin ese supuesto invierte la prueba de permutacion por cambio de signo. Solo con cita si hay ficha; si no, `\GAPLIT`. |
| guia-6 | media | G-T3 | capitulo1.tex:128 frente a :101 | Patron PAT-14 reincide. :101 explica que se evita $\alpha$ porque en el Capitulo 3 nombra otra magnitud (el angulo de rotacion, `capitulo3.tex`:157-160), pero :128 usa $\alpha=0.05$ como nivel de significacion. | En :128 escribir «con nivel de significacion de 0.05», sin simbolo, como hace `capitulo3.tex`:375. |
| guia-7 | media | G-T3, G-B3 | capitulo1.tex:110 frente a capitulo3.tex:202 | Patron PAT-113 reincide. El marco define $\mathbf{v}_n=a_n\boldsymbol{\xi}-s_n\mathbf{x}_0$ con simbolos propios para no chocar con el Cap. 3. El metodo (:202) vuelve a definir $v=\alpha_t\epsilon-\sigma_t x$ con la notacion de la fuente, y $\sigma_t$ ya nombra la dispersion del muestreador (:157). | Hay que corregirlo en el capitulo 3: que remita a la Ecuacion de :110 y use $a_n$, $s_n$, $\boldsymbol{\xi}$. En el capitulo 1 no hace falta tocar nada, salvo que la autora decida otra notacion. |
| guia-8 | baja | G-B2 | capitulo1.tex:134 | El parrafo sobre la proteccion contra ajustar el resultado a los datos solo trata los Objetivos 1 y 2. Para el Objetivo 3, el principal, faltan la regla de DEC 2026-10-15 (las sensibilidades posteriores solo pueden bajar la categoria del desenlace, nunca subirla) y la multiplicidad declarada sin correccion de sus analisis descriptivos (punto 15). | Añadir una oracion para el Objetivo 3: lo confirmatorio es solo `run04_mejor`; los analisis posteriores son descriptivos y solo pueden bajar la categoria del desenlace. Remitir a `sec:amenazas`. Partir el parrafo si pasa de siete oraciones. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | no cumple (guia-3, guia-4) |
| G-T2 | cumple |
| G-T3 | no cumple (guia-6, guia-7) |
| G-T4 | no cumple (guia-1, guia-2, guia-3) |
| G-T5 | cumple (orden justificado en :13 y coherente con la Figura `fig:mt-conceptos`) |
| G-T6 | cumple (lint PASA) |
| G-B1 | cumple |
| G-B2 | no cumple (guia-4, guia-5, guia-8) |
| G-B3 | no cumple (guia-2, guia-4, guia-7) |
| G-B4 | no cumple (guia-1); la compresion arcoseno hiperbolico cumple con GAP (`\GAPDATO` :46) |
| P-MT1 | cumple, salvo lo señalado en guia-4 y guia-5 |
| P-MT2 | cumple (Figura `fig:mt-conceptos` alineada con los objetivos de la introduccion; remision a `fig:pipeline`) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que una DEC nueva ya cerro sigue en la seccion que no era el foco del encargo | G-T4 | `\GAPDEC{cómo expresar en HU la pérdida de la regla del suelo...}` | PAT-19 |
| Oracion de remision que anuncia como pendiente el desenlace de una regla ya declarada no aplicable | G-T4 | «regla preinscrita cuyo desenlace aún no se conoce» | PAT-116 |
| Verbo en futuro de intencion para un brazo ya ejecutado, en otro parrafo del mismo capitulo | G-T4 | «prevé usar el protocolo físico como comparación» | PAT-122 |
| El marco estadistico enuncia solo el desenlace favorable de una prueba y no los que el diseño fija despues | G-B2 | «puede no concluir ni equivalencia ni diferencia» | nuevo |
| Un simbolo que el capitulo declara evitar por choque reaparece unas lineas despues | G-T3 | «Para pruebas con $\alpha=0.05$» tras evitar $\alpha$ | PAT-14 |
