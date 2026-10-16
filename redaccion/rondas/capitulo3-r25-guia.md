# Revision guia CS — capitulo3 — r25

Texto revisado: `overleaf/secciones/capitulo3.tex` al abrir la ronda (lint r25: GAP lit=2, dato=18, dec=0; las dos
`\GAPLIT` siguen en :419 y :437). Fichas nuevas leidas: `walker2011understanding`, `lakens2017equivalence`,
`bland1996statistics`; implicancia #194 (ABIERTA, "se aplica en capitulo3-r25", pendiente visto bueno del mapeo).
Las tres claves ya estan en `overleaf/referencias.bib`; `bland1996statistics` corresponde a BMJ 313:106 (la nota del
PDF), con un `% VERIFICAR` por el segundo raw (eso es de trazabilidad). Cruces: `capitulo1.tex:128-130` (definicion de
los tres desenlaces, sin cita) e `introduccion.tex:50-52`. Respuesta previa: `capitulo3-r24-respuesta.md`, sin
RECHAZADOS que afecten a esta ronda.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T4, G-T2 | capitulo3.tex:417; :419 | El `\GAPLIT` de :419 ya tiene fuentes (#194), pero ninguna usa "no concluyente". Walker y Nowacki rotulan el IC que cruza un limite "Equivalence not established" (Fig. 1, p. 193) y dicen que "nonequivalence cannot be ruled out" (p. 192). Lakens llama a ese caso "Not Equivalent" (escenario B) o "undetermined" (escenario D) (p. 356-357), y la Fig. 2 de Walker lo llama "not equivalent" (p. 195). Si se cita sin mapear, "no equivalencia" designa dos cosas: el IC entero fuera (tesis) y el IC que cruza (fuentes) (riesgo PAT-14) | Citar en :417, donde se definen los desenlaces, y mapear sin renombrar: "no concluyente" es el nombre de este trabajo para lo que Walker y Nowacki llaman equivalencia no establecida, sin poder descartar la no equivalencia, y Lakens escenario B o D. Decir que ninguna de las dos fuentes nombra como categoria propia el IC entero fuera ("no equivalencia" es de este trabajo). Rotulos de las fuentes en cursiva y entre comillas. En :419 dejar solo la lectura de dos niveles y retirar la marca |
| guia-2 | media | G-C8 | capitulo3.tex:417; :419 | La direccion se informa "si el intervalo excluye el cero", es decir, el IC del 90 %, que equivale a un contraste bilateral de nivel 0.10. Lakens decide la diferencia frente a cero con el IC del 95 % (escenarios B a D, p. 356), y su escenario B exige ese IC. El texto no dice a que nivel se afirma la direccion | No cambiar la regla fijada el 15 de octubre. Declarar que la direccion se lee con el IC del 90 % y que, en la taxonomia de Lakens, la diferencia se decide con el del 95 %. El IC del 95 % calculado (#194, ABIERTA) entra con la marca de BITACORA §2 2026-10-15: "calculado; consta en una implicancia abierta (implicancia 194)". Cifra al cap. 4. Avisar a capitulo1 (:130) e introduccion (:52), que usan la misma regla |
| guia-3 | media | G-T4 | capitulo3.tex:437 | El `\GAPLIT` de var(ln) y CV^2 solo se cierra en parte. `bland1996statistics` da que el antilogaritmo de la DE en escala log, menos 1, aproxima el CV, "provided the standard deviation is not large" (p. 106). Usa log10 y el error intra-sujeto de duplicados. La ficha marca NO ENCONTRADO para "varianza del log ~ CV^2", para el logaritmo natural y para Pitman y Morgan. Riesgo PAT-194: atribuir a Bland y Altman la aplicacion de Pitman y Morgan sobre ln | Citar `bland1996statistics` solo para lo que da: log cuando la DE crece con la media, y antilog(DE) - 1 ~ CV si la DE es pequena. Dar en una frase el paso propio: con ln, exp(s) - 1 ~ s, luego var(ln) ~ CV^2. Declarar como lectura de este trabajo su uso sobre la dispersion entre pacientes de dos brazos y su uso como base de Pitman y Morgan sobre ln. Con eso la marca se puede retirar |
| guia-4 | media | G-C7 | capitulo3.tex:525 | El cuarto limite de la lectura de acuerdo repite fuera de la marca "solo sobre el logaritmo se lee como comparacion aproximada de coeficientes de variacion", sin cita ni marca (Patron PAT-168 reincide). Le falta la condicion de la fuente: Bland y Altman no dan umbral de "DE pequena" y juzgan 0.496 "too large for the approximation to be reliable" (p. 106). Los CV del propio capitulo son 0.076 y 0.241 (:437), asi que la aproximacion no esta asegurada en el protocolo fisico | Alinear :525 con el cierre de :437. La aproximacion vale si la DE en log es pequena; la fuente no da umbral. Con un CV de 0.241 en el protocolo fisico su validez no esta establecida. La fuente trata error intra-sujeto y no dispersion entre pacientes de dos metodos. Sin cifra nueva |
| guia-5 | media | G-C7 | capitulo3.tex:421; :523-527 | Las fichas nuevas definen el margen como la mayor diferencia aceptable: "maximum clinically acceptable difference" (Walker, p. 192), justificada con "relevant evidence" (p. 194), o el menor efecto de interes (Lakens, p. 359). El $\Delta$ de este trabajo es variabilidad del metodo entre semillas y replicas (:421), no una diferencia juzgada irrelevante para el uso. Amenazas trata el tamano y la dependencia del margen (:495, :527) y, para Bland y Altman, que no se fijo una diferencia aceptable (:525), pero no lo dice del TOST. Que significaria una equivalencia queda sin acotar | Una oracion en Validez de constructo o de la conclusion. El margen no es una diferencia aceptable en el sentido de esas fuentes, sino la variabilidad del propio metodo. Una equivalencia diria que los brazos no se distinguen a la escala de ese ruido, no que su diferencia sea irrelevante. No toca ningun desenlace. Evaluar si abre implicancia (regla 13 raiz): #194 no lo recoge |
| guia-6 | baja | G-T4 | capitulo3.tex:417 | "nunca se infiere equivalencia de una diferencia no significativa" va sin cita, aunque ahora la respaldan dos fichas: "a nonsignificant result implies only that equivalency ... cannot be ruled out" (Walker, p. 194) y Lakens (p. 355) | Anadir `\cite{walker2011understanding}` en esa oracion |

TOTAL alta=0 media=5 baja=1

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | cumple (con la condicion de guia-1 al citar) |
| G-T3 | cumple en la seccion; cap. 1 :130 define los tres desenlaces sin cita y con la misma regla de direccion (aviso en guia-2; #194 lo deja para su proxima ronda) |
| G-T4 | no cumple (guia-1, guia-3, guia-6) |
| G-T5 | cumple |
| G-T6 | cumple (claves nuevas presentes en `referencias.bib`) |
| G-A7 (cruce) | cumple con GAP (contraste de realismo sin script) |
| G-A8 (cruce) | cumple (dos niveles; un IC entero fuera del margen habria rechazado la hipotesis, :419) |
| G-C1 | cumple |
| G-C2 | cumple con GAP |
| G-C3 | cumple |
| G-C4 | cumple |
| G-C5 | cumple |
| G-C6 | cumple |
| G-C7 | no cumple (guia-4, guia-5) |
| G-C8 | no cumple (guia-2) |
| G-C9 | cumple (protocolo fisico como contraste primario; copia y pegado como control de cordura) |
| P-MM1 | cumple |
| P-MM2 | cumple |
| P-MM3 | cumple con GAP |
| OC-2 / OC-3 | cumple (#194 ABIERTA: el mapeo entra como lectura de este trabajo y no cambia ningun desenlace; el IC del 95 % lleva marca, guia-2) |

## Propuestas de criterio
- Al cerrar un `\GAPLIT` con fuentes cuya taxonomia no coincide con la propia, el texto da el rotulo de la fuente y el
  propio y dice cual es de este trabajo (extiende G-T2 a las categorias tomadas de la literatura).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| La prosa fuera de la marca repite como hecho lo que la marca declara sin fuente | G-T4, G-C7 | "solo sobre el logaritmo se lee como comparacion aproximada de coeficientes de variacion" | PAT-168 |
| Categoria propia cerrada con fuentes que usan otro rotulo, o el mismo rotulo para otro caso | G-T2, G-T4 | "no concluyente" frente a "Not Equivalent" (Lakens B) y "not equivalent" (Walker, Fig. 2) | nuevo |
| Regla de lectura que usa un intervalo de nivel distinto del que fija la fuente citada | G-C8 | "Si ademas el intervalo excluye el cero" (IC90; Lakens usa IC95) | nuevo |
