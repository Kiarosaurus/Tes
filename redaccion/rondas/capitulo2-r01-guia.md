# Revision guia CS — capitulo2 — r01

Leido: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md`, `redaccion/MAPA.md`,
`capitulo2-r00-respuesta.md`, `capitulo2-r01-lint.md`, `overleaf/secciones/capitulo2.tex` (entero),
`introduccion.tex` (entero) y `capitulo3.tex` (ll. 1-40 y 168-261) para los cruces G-B10, G-T3 y G-T5.
`capitulo1.tex` es esqueleto. No hay hallazgos RECHAZADOS previos (r00 fue redaccion sin revisores).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-B5, G-B7 | capitulo2.tex:46, :48, :58, :38 | El Objetivo 4 no tiene comparacion critica. La l. 46 promete "la escala" para el Obj 4 y la l. 58 anuncia carencias "frente a los Objetivos 2 y 4", pero ninguna de las tres carencias dice que les falta a las medidas de colocacion ya publicadas para que haga falta SAP: el grado leido en TC posoperatoria (Zwingmann), la definicion binaria (Herman) y la distancia al borde oseo de Liu et al. (l. 48), que se reporta como resultado y no se compara. La escala de Smith et al., que SAP usa (capitulo3.tex:189), no aparece. De las metricas de Peters (l. 38) solo se dice "ocho metricas", sin cuales se adoptan ni que les falta a las evaluaciones de sintesis de la l. 30. | En la l. 58 (o un parrafo antes) decir, por medida existente, que mide y por que no sirve tal cual para calificar poses generadas sobre una pelvis nueva, con lo que den las fichas; nombrar en 2.2 las tres metricas adoptadas y que se disenaron para MAR. Lo que las fichas no respalden, `\GAPDEC`. |
| guia-2 | media | G-B7 | capitulo2.tex:110 (contra :34, :38, :42) | El primer elemento del aporte se define contra "una mascara de metal segmentada con un umbral fijo de HU", pero el capitulo no identifica ningun trabajo revisado que use esa mascara como mascara de sintesis. La Sec. 2.2 muestra lo contrario: insertar metal virtual de geometria conocida es "practica establecida" (Zhang y Yu, Wang 2019, Karageorgos, Peters, Ren). El umbral aparece solo en MAR (ll. 36, 62). Se ataca una alternativa que ninguna solucion concreta encarna. | Decir en 2.2 que geometria tiene el metal virtual de los simuladores revisados (segun fichas) y frente a cual de ellos se distingue el cilindro parametrico; o reducir el primer elemento a lo que la comparacion sostiene y enlazarlo con el `\GAPDEC` de la l. 112, que ya propone "objeto metalico rigido". |
| guia-3 | media | P-EA3 | capitulo2.tex:110 | El aporte se enuncia mas fuerte que en la introduccion: "en lugar de una mascara ... segmentada con un umbral" omite que el sintetizador si se entrena con mascaras umbralizadas a 2500 HU (introduccion.tex:58; capitulo3.tex:178, :182). Leido solo, el parrafo afirma que el umbral no interviene. | Anadir la salvedad en una oracion con remision a la Seccion `sec:sintetizador`, como hace la introduccion. |
| guia-4 | media | G-B7, G-B8 | capitulo2.tex:106, :99 (contra :40, :58) | La misma carencia de la simulacion fisica se resume de tres formas: "al azar o con una regla de solape" (l. 58), "al azar o a mano" (l. 106) y, en la l. 40, que Peters et al. **no** colocaron a mano por impracticable. La celda "Metal insertado a mano para entrenar" de Wang et al. (l. 99) y la de Jacob et al. "Elipsoide en una region elegida al azar" (l. 93) dan hechos que el cuerpo del capitulo no presenta. | Unificar el resumen de la carencia en ll. 58 y 106; si "a mano" se refiere a Wang 2025, decirlo en 2.4 con su cita, y decir en 2.1 o 2.3 de donde salen las mascaras de Jacob et al. Ninguna celda de la tabla sin oracion de respaldo en el texto. |
| guia-5 | media | G-B5, G-B9 | capitulo2.tex:50, :58 | El parrafo lista tres precedentes de "decidir donde va el objeto" (Zhang 2026, Ramzan, Chen) sin decir que les falta frente al Objetivo 2. Los generadores de mascaras de lesion son el precedente mas cercano de separar colocacion y apariencia, y Ramzan et al. muestrean sobre un modelo clinico; aun asi quedan fuera de las "tres carencias" de la l. 58 y del negativo final, que solo puede cumplirse para tornillos. | Cerrar el parrafo con la consecuencia (p. ej., si alguna de esas fuentes compara la distribucion de sus mascaras con una distribucion clinica medida, segun ficha) y sumarla a las carencias de la l. 58; si la ficha no lo dice, `\GAPDEC`. |
| guia-6 | media | G-T5 | capitulo2.tex:10 | "Las cuatro primeras secciones siguen la cadena propuesta", pero el orden real es Obj 3, Obj 3, Obj 2 y 4, Obj 1: el inverso de la cadena (compuerta, muestreador, sintetizador; capitulo3.tex:9) y distinto del orden de los tres enfoques en la brecha (l. 108) y en la introduccion (l. 54). La oracion que justifica el orden no describe el orden. | Decir el criterio real del orden (p. ej., del precedente mas cercano de la generacion a sus requisitos) o reordenar; alinear la enumeracion de enfoques de la l. 108 con el orden de las secciones. |
| guia-7 | media | P-EA2 | capitulo2.tex:36, :96 | Karageorgos et al. es fila de la tabla ("Similitud y error frente a la imagen sin metal") y Yun et al. evaluan sobre el mismo subconjunto CLINIC-metal que este trabajo, pero de ninguno se reporta un resultado: solo el metodo. La celda de evaluacion de Karageorgos no tiene respaldo en el cuerpo. | Dar un resultado de cada uno con su condicion (el RMSE de Karageorgos ya esta en capitulo3.tex:176; para Yun, lo que de la ficha), o sacar a Karageorgos de la tabla. |
| guia-8 | baja | G-B8 | capitulo2.tex:89-101, :80 | La tabla no tiene las columnas "supuestos" ni "resultados" que sugiere la guia: "Evaluacion reportada" da cifra en dos filas (Peters, Liu) y solo el nombre de la metrica en las demas. El Obj 1 queda fuera de la tabla (l. 80), pero la fila de Chen et al. si da su rango de HU, y la fila propia no da el suyo. | Homogeneizar la columna (metrica y una cifra en todas, o solo metrica en todas) y decidir si el rango de intensidad es columna o sale de la fila de Chen et al. |
| guia-9 | baja | G-T2 | capitulo2.tex:54, :58 (contra :1, :8, :78, :108, :114) | Patron PAT-14 reincide: "brecha" designa en el capitulo la brecha de investigacion (titulo, ll. 8, 108, 114) y la brecha cortical ("miden la brecha por nivel sacro", "grados de brecha"). | En las ll. 54 y 58 escribir siempre "brecha cortical"; "brecha" a secas solo para la del estado del arte. |
| guia-10 | baja | G-T2 | capitulo2.tex:34, :24, :36, :56 | Patron PAT-3 reincide: "CatSim" se usa en la l. 34 y se explica en la l. 38; "Stable Diffusion" (l. 24), "traza metalica" (ll. 36, 42), "transiliosacras" y "S2" (ll. 54, 56) no se definen en ningun capitulo redactado (`capitulo1` es esqueleto). | Adelantar a la l. 34 la aposicion de CatSim; glosa corta de los demas en su primera aparicion o nota para que el marco teorico los cubra. |
| guia-11 | baja | G-B9 | capitulo2.tex:56 | Las tolerancias angulares de McLaren et al. y los coeficientes de variacion de Ziran et al. se reportan sin decir que implican para el Objetivo 2; solo la ultima oracion conecta el parrafo con el muestreador. | Una oracion que diga para que usa este trabajo cada cifra (o que no la usa), o quitar las que no se usen. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple (salvo lo senalado en guia-4: celdas de tabla sin respaldo en el texto) |
| G-T2 | no cumple (guia-9, guia-10; bajas) |
| G-T3 | cumple ($G$, $M$, $B_{\delta}$ y $p$ iguales que en introduccion y capitulo3) |
| G-T4 | cumple con GAP (cifras ajenas con cita; `\GAPDATO` de Li et al.; el cotejo cifra a cifra es del auditor) |
| G-T5 | no cumple (guia-6); transicion desde `capitulo1`: no evaluable (esqueleto); hacia `capitulo3`: cumple (l. 114) |
| G-T6 | cumple (lint: sin citas indefinidas) |
| G-B5 | no cumple (guia-1, guia-5) |
| G-B6 | cumple con GAP (`\GAPDEC` del protocolo de busqueda, l. 12) |
| G-B7 | no cumple (guia-2, guia-4) |
| G-B8 | cumple, con mejora (guia-8); fila propia presente, marcada como diseno con `\GAPDATO` |
| G-B9 | cumple (no es cronologico ni panoramico; guia-5 y guia-11 son tramos puntuales) |
| G-B10 | cumple con GAP (la brecha de la l. 108 repite la tension de introduccion.tex:54 y su `\GAPDEC` #128.1; el encabezado y la Formulacion de la introduccion siguen desfasados, con `\GAPDEC` propio) |
| P-EA1 | cumple (dos prepublicaciones senaladas; fuente de solo resumen senalada; sin fuentes de fabricante) |
| P-EA2 | no cumple (guia-7) |
| P-EA3 | cumple a medias (guia-3); el reclamo de novedad lleva `\GAPDEC` (#56) |

Patrones VIGENTES de mi dominio comprobados: PAT-3 (reincide, guia-10), PAT-14 (reincide, guia-9),
PAT-38 (no aplica: el capitulo remite las amenazas a `sec:amenazas`), PAT-49 (no reincide: la l. 110
declara que ningun objetivo aisla el primer ni el tercer elemento), PAT-57 (no reincide), PAT-61 (no
reincide: el capitulo no da resultados propios), PAT-65 (no detectado; cotejo con fichas a cargo del
auditor). Los de criterio E-* quedan para `revisor-estilo`.

## Propuestas de criterio
- Que toda celda de la tabla comparativa (G-B8) tenga una oracion de respaldo en el cuerpo del
  capitulo. Hoy se reporta por G-B7/G-B8/G-T1, sin criterio propio.
- Que el estado del arte cubra tambien los objetivos que producen definiciones o metricas (aqui el
  Obj 4): la guia pide comparar "contra los objetivos", sin distinguir tipos.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un termino designa dos cosas en el capitulo | G-T2 | "miden la brecha por nivel sacro" / "La brecha es la misma tension" | PAT-14 |
| Termino tecnico usado antes de su definicion | G-T2 | "simulan la adquisicion con CatSim" (se explica cuatro lineas despues) | PAT-3 |
| La misma carencia o conclusion se resume distinto en dos lugares del capitulo | G-B7 | "al azar o con una regla de solape" / "al azar o a mano" | nuevo |
| Celda de tabla o resumen con un hecho que el cuerpo del capitulo no presenta | G-B8, G-T1 | "Metal insertado a mano para entrenar" | nuevo |
| Aporte contrastado con una alternativa que ningun trabajo revisado encarna | G-B7 | "en lugar de una mascara de metal segmentada con un umbral fijo" | nuevo |
| Aporte o limite que pierde su salvedad al repetirse en otro capitulo | P-EA3 | primer elemento sin "el entrenamiento si usa mascaras umbralizadas" | nuevo (variante de PAT-31, que es de cifras) |
| Objetivo que produce definiciones queda sin comparacion critica en el estado del arte | G-B5 | "frente a los Objetivos 2 y 4" y las tres carencias son del 2 | nuevo |
| Oracion que justifica el orden de las secciones y no describe el orden real | G-T5 | "Las cuatro primeras secciones siguen la cadena propuesta" | nuevo |
