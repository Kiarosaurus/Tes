# Revision de estilo — capitulo1 — r06

Lint de la ronda: PASA (alta=0 media=0 baja=0). Respuesta previa: r05, 0 RECHAZADOS (todo APLICADO),
de modo que no hay nada vetado con motivo; tampoco hay re-aperturas en este informe. Vara de tono:
ESTILO §1.1 (E-M1 a E-M8); `muestras_autora.md` sigue vacio.

Novedades de la etapa aplicadas a este capitulo: BITACORA §2 (2026-10-05) sobre el nombre del
implante (#130) y sobre el nivel del lector no especialista. **"SERUM" no aparece** en el capitulo y
la unica caracterizacion de lector es "un lector de computacion que no conoce la fisica de la
tomografia ni la cirugia de la pelvis" (l.11): correcto, se describe y no se sigla.

Patrones VIGENTES comprobados uno por uno: **PAT-14** reincide (S03), **PAT-126** reincide (S04),
**PAT-122** reincide (S02), **PAT-64** reincide (S01). **No reinciden**: PAT-31 (toda cifra retomada
lleva su condicion: 0.42 con cohorte, recorte y "en la mediana" en l.35; 10-50 veces "en tiempo de
reloj" y "no medida sobre TC" en l.106; 0.0001 "en la misma simulacion" en l.54), PAT-45 (no hay
titulos de objetivo aqui), PAT-58 (ningun parrafo pasa de siete oraciones; l.35 y l.13 estan en
siete), PAT-62 ("se fija", "es una convencion", nunca "equivale a"), PAT-119 (las aperturas de §1.5
que r05 reescribio no formaron serie nueva), PAT-124 (el molde "A y no B" aparece en l.31, l.50 y
l.130, nunca en tres parrafos seguidos) y PAT-125 (los negativos en plural de l.52, l.84 y l.112
nombran enseguida las fuentes que los sostienen; la excepcion es l.62, que va como S01).
No se re-reporta la oracion de Kazerouni et al. (l.92): su forma actual es de S16-r01 y S13-r03 de
este mismo revisor.

Cap. 2 y cap. 3 cotejados: `capitulo2.tex`:96 (Radzi et al. y Cassanego et al. con distancias en mm),
`capitulo3.tex`:46 ("cribado por HU"), :109 (el implante es un tornillo transiliaco-transsacro y le
aplican las tolerancias de McLaren et al.), :206 (entrada y salida por la cortical del ilion).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S01 | alta | E-R6, E-P3 | l.62, 2a oracion | "porque las fuentes revisadas no dan hasta donde llegan las rayas" | Patron PAT-64 reincide, y en el peor sitio: la remision es a `sec:ea-representacion`, que es justo donde `capitulo2.tex`:96 dice lo contrario ("Otras dos fuentes si publican una distancia en milimetros, y ninguna sirve para calibrar $B_{\delta}$", con 2.0-2.6~mm de Radzi et al. y 3.1-4.2~mm de Cassanego et al.). Leido junto al cap. 2, el capitulo niega lo que el documento cita cuatro paginas despues con cifras. Misma formulacion que el cap. 2: "... alrededor de la mascara del implante, cuyo ancho es una convencion de este trabajo porque las dos fuentes revisadas que publican una distancia la miden de un modo que no sirve para fijarla (Seccion~\ref{sec:ea-representacion})." |
| S02 | media | E-T1 | l.72, oraciones 3-4 | "Un tornillo transiliosacro, en cambio, cruza las dos articulaciones sacroiliacas" | BITACORA §2 (2026-10-05, #130): primera aparicion "tornillo transiliaco-transsacro (transiliosacro)" y despues "tornillo transiliaco-transsacro", con tilde. `capitulo3.tex` ya usa esa forma cinco veces (:9, :103, :109, :127, :206) y el cap. 1 es la primera aparicion en el orden del documento. Las dos menciones de l.72 cuelgan de `mclaren2021corridor`, que no esta en la lista de excepciones: "Un tornillo transiliaco-transsacro (transiliosacro), en cambio, cruza las dos articulaciones sacroiliacas y sale por la tabla externa del ilion opuesto" y "las de McLaren et al. son de tornillos transiliaco-transsacros". Siguen diciendo "iliosacro" el termino en negrita de Smith et al. (l.72, l.82), el umbral de 10~mm de Kaiser et al. y lo que Zwingmann et al. llaman asi dentro del `\GAPDEC`. Coincide con M-02 de `paridad-r01-trazabilidad.md`: se aplica una sola vez |
| S03 | media | E-T1, E-R5 | l.64, ultima oracion | "preve usar la simulacion fisica como comparacion (Seccion~\ref{sec:apariencia})" | Patron PAT-14 reincide dentro de un mismo parrafo: "la simulacion fisica" nombra primero la familia de metodos (sentido del cap. 2) y al cerrar nombra el brazo de comparacion, que el documento llama "protocolo fisico" (l.33, l.124 y BITACORA §2 2026-09-29). La primera oracion se conserva; la ultima: "Este trabajo genera la apariencia del artefacto con un modelo aprendido, sin simular proyecciones, y preve usar el protocolo fisico como comparacion (Seccion~\ref{sec:apariencia})." |
| S04 | media | E-R5, E-T1 | l.13, l.74, l.126 | "de la que salen el corredor oseo" / "De esa comparacion salen" / "el intervalo ... sale de" | Patron PAT-126 reincide, agravado porque en este capitulo "salir" tiene sentido anatomico literal cuatro veces (l.54 el espectro, l.72 dos veces el tornillo, l.76 el tornillo que sale de la zona segura). Tres sentidos de procedencia distintos con el mismo comodin: concepto que viene de una seccion, grupos que vienen de una comparacion, intervalo que viene de una distribucion. l.13: "La Seccion~\ref{sec:mt-iliosacra} describe la fijacion iliosacra y, con ella, el corredor oseo, la escala de brecha cortical y la referencia clinica del Objetivo~2." l.74: "La serie navegada y la serie convencional son los dos grupos de esa comparacion." l.126: "y el intervalo del 95\,\% se obtiene de la distribucion de esas medias" |
| S05 | media | E-P3, E-M4 | l.72, ultima oracion y su `\GAPDEC` | "La Seccion~\ref{sec:sap}, sin embargo, trata el tornillo de este trabajo como uno que..." | Patron PAT-122 reincide: el `\GAPDEC` pregunta "que tornillo representa el corredor que mide este trabajo" cuando #130 lo decidio y `capitulo3.tex`:109 ya lo afirma como hecho ("El implante que representa es, por tanto, un tornillo transiliaco-transsacro"); el "sin embargo" presenta como tension algo que el registro cerro. Decir el hecho y dejar en el `\GAPDEC` solo lo que sigue abierto: "El corredor que mide este trabajo va de la cortical externa de un ilion a la del ilion opuesto, de modo que representa un tornillo transiliaco-transsacro (Seccion~\ref{sec:geometria}) \GAPDEC{si al tornillo transiliaco-transsacro de este trabajo le aplican el umbral de 10~mm y la holgura radial de Kaiser et al., definidos para el tornillo iliosacro, y si es del mismo tipo que los tornillos de la referencia clinica, que Zwingmann et al. llaman iliosacros y transiliosacros}" |
| S06 | media | E-M4 | l.84, ultima oracion | "consideran insegura una colocacion cuya trayectoria perfora una de las corticales..." | El parrafo abre con la funcion correcta ("Las fuentes revisadas no juzgan la colocacion con una misma escala") y cierra con el tercer caso, sin decir que se sigue: el lector tiene que adivinar por que importa la heterogeneidad. El capitulo ya tiene los dos datos (l.70: la distribucion de Zwingmann et al. es la referencia clinica; l.84: Zwingmann et al. aplican la escala de perforacion). Cerrar con la consecuencia: "La comparacion del Objetivo~2 es posible porque Zwingmann et al. califican con la escala de perforacion; una definicion binaria como la de Hinsche et al. no produce una distribucion de grados que se pueda comparar con ella." |
| S07 | baja | E-F3 | l.35, 4a oracion | "Dos fuentes de MAR segmentan el metal clinico con 2500~HU" | BITACORA §2 (2026-09-30): "Una cifra ajena lleva como sujeto a los autores que la reportan". El sujeto generico deja la cifra sin dueno y, de paso, repite el recuento anunciado que r04 (S06) quito en otras cinco oraciones. "Wang et al.~\cite{wang2025adaptiveweighting} y Li et al.~\cite{li2024} segmentan el metal clinico con 2500~HU, umbral con que este trabajo ..." |
| S08 | baja | E-T1 | l.35, 4a oracion | "umbral con que este trabajo criba la cohorte y delimita el metal clinico" | BITACORA §2 (2026-10-05): el procedimiento se nombra siempre calificado, "cribado por HU", como en `capitulo3.tex`:46. El verbo suelto deja el mismo procedimiento sin nombre en el cap. 1. "..., umbral del cribado por HU con que este trabajo selecciona la cohorte y delimita el metal clinico de sus volumenes (Secciones~\ref{sec:datos} y~\ref{sec:sintetizador})" |
| S09 | baja | E-F1 (E-M5) | l.42, 2a oracion | "Lo que cae fuera de la ventana se \textbf{satura}" | La negrita cae en la segunda aparicion del termino: la primera esta en l.37, dentro de la definicion de ventana ("que se satura y se lleva linealmente a $[0,1]$"). Llevar la negrita a l.37 ("que se \textbf{satura} y se lleva linealmente a $[0,1]$") y dejar l.42 en redonda |
| S10 | baja | E-T1 | l.66, ultima parte | "con un umbral que se adapta a cada region" | En un capitulo donde "region de generacion $G$" es termino fijo, "cada region" a secas obliga a elegir entre tres sentidos en el mismo parrafo. El propio documento ya tiene el nombre en l.118 ("las regiones de medicion de rayas"): "La \emph{streak amplitude} mide las rayas en regiones de medicion perpendiculares a ellas ..." y "... con un umbral que se adapta a cada region de medicion" |
| S11 | baja | E-R4 | l.13, ultima oracion | "La Figura~\ref{fig:mt-conceptos} relaciona cada grupo de conceptos con la pieza..." | La oracion repite palabra por palabra el pie de la figura ("Conceptos del capitulo y pieza de la propuesta que los usa") y es la septima de un parrafo que ya asigna cada seccion a su pieza. Eliminar: la figura entra por su pie y el parrafo baja a seis oraciones |

## Impresion general
Leido seguido, el capitulo sigue sonando a tesis: define por contraste, acota a las fuentes revisadas
y dice en que pieza interviene cada concepto; el ritmo ya no delata correccion automatica. Lo que
queda no es pulido del mismo sitio: casi todo entra por fuera (el nombre del implante que decidio la
autora, el `\GAPDEC` que esa decision dejo viejo, y el negativo de l.62 que el cap. 2 contradice con
cifras). El unico patron propio del capitulo es de nomenclatura: un mismo nombre para dos cosas
(simulacion fisica, region) y un verbo comodin de procedencia donde "salir" ya significa otra cosa.

TOTAL alta=1 media=5 baja=5

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Negativo sobre "las fuentes revisadas" cuya remision apunta a la seccion que lo contradice con cifras | E-R6, E-P3 | "las fuentes revisadas no dan hasta donde llegan las rayas" | PAT-64 |
| Verbo comodin de procedencia ("salir de") en un capitulo donde ese verbo tiene sentido literal | E-R5, E-T1 | "De esa comparacion salen la serie navegada y la serie convencional" | PAT-126 |
| El nombre generico de una familia de metodos se usa tambien para el brazo de comparacion propio | E-T1, E-R5 | "preve usar la simulacion fisica como comparacion" | PAT-14 |
| Decision de la autora que fija un nombre: el capitulo que lo define primero en el documento es el ultimo en recibirla | E-T1 | "Un tornillo transiliosacro, en cambio, cruza las dos articulaciones" | nuevo |
| Oracion de remision a una figura que repite el pie de la figura | E-R4 | "relaciona cada grupo de conceptos con la pieza de la propuesta" | nuevo |
