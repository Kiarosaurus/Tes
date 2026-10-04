# Revision guia CS — capitulo2 — r03

Leido: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md`, `capitulo2-r02-guia.md`,
`capitulo2-r02-respuesta.md`, `capitulo2-r03-lint.md` (PASA; GAP 1/2/8), `overleaf/secciones/capitulo2.tex`
(entero), `introduccion.tex` (entero) y `capitulo3.tex` (ll. 40-266) para G-B10, G-T3 y G-T5; `capitulo1.tex`
es esqueleto. Fichas cotejadas solo para hallazgos: `herman2016.md` (pto 8, tabla p. 8), `cassanego2026evolution.md`
(especie y sitio), `wu2025freetumor.md` (GAN, no difusion: l. 26 correcta). Los aplicados de r02 se comprueban
y no reinciden (Liu segun ficha, carencia en una formula, CLINIC-metal con inferencia, Herman sin "cota",
salvedad de ida y vuelta). No se reabre ningun rechazo de r02 (AAPM sin expandir; T06 pendiente de relectura;
"entrada y salida" frente a `introduccion.tex`:60, pendiente de la autora fuera de esta seccion).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-B8 | capitulo2.tex:97-111 | La tabla no tiene los supuestos que el criterio pide (enfoque, supuestos, resultados), y la columna "Evaluacion reportada" da casi siempre el nombre de la metrica, no el resultado (solo Peters y Liu llevan cifra), aunque el cuerpo si da los resultados. La fila propia omite el supuesto y la convencion en que la l. 126 dice que descansa la brecha. | Renombrar la ultima columna a resultado reportado con la cifra principal que ya esta en el cuerpo y su condicion (p. ej., Chen 62.5 -> 66.5 % en higado con una de tres redes; Zwingmann grado 0 en 69 y 40 %). Anadir supuestos en una columna o dentro de "Enfoque", y en la fila propia: artefacto generable en el dominio de imagen y el ancho de $B_{\delta}$ como convencion. |
| guia-2 | media | G-B9, G-B5 | capitulo2.tex:62 (contra introduccion.tex:68, :78; capitulo3.tex:164, :259) | Patron PAT-76 reincide. Los porcentajes de Herman et al. por nivel (36.5 % en S1, 14.8 % en el segundo segmento sacro) quedan sin decir que se sigue de ellos para el Obj 2. Se relacionan con dos decisiones del documento: el segundo corredor bajo S1 queda fuera porque no hay distribucion *ordinal* por debajo de S1 (Herman da una binaria), y el nivel S1 de la serie navegada es un supuesto (la brecha cambia con el nivel). La ficha (pto 8) trae ademas que el dismorfismo no se asocio a malposicion, pertinente para la exclusion de alcance por dismorfismo. | Una oracion: el dato por nivel es binario y no da la distribucion ordinal que el segundo corredor necesitaria (remision a `sec:poses`), y la diferencia entre niveles es la razon de que el nivel de la referencia clinica importe (supuesto de la serie navegada, `sec:amenazas`). Si se usa el resultado sobre dismorfismo, con su condicion (malposicion, no area de la zona segura). |
| guia-3 | media | G-B5 | capitulo2.tex:66 (contra introduccion.tex:43; capitulo3.tex:166, :189) | Patron PAT-70 reincide en parte. El Obj 4 define SAP con tres componentes, y la comparacion critica de la l. 66 solo cubre el grado de brecha; la viabilidad se compara en la l. 64. La fraccion por zona de densidad no tiene fuente revisada ni carencia enunciada en el capitulo, y el `\GAPDEC` que la introduccion y el cap. 3 le ponen (fuente y definicion operativa) no se replica. | Anadir en la l. 66 una oracion sobre que medida de densidad dan las fuentes revisadas (el cap. 3 cita a Arand et al. como motivacion) y que le falta para SAP, con el mismo `\GAPDEC` de `introduccion.tex`:43. |
| guia-4 | media | G-T5 | capitulo2.tex:52 (contra :66, :68) | Patron PAT-71 reincide. La oracion de orden dice que la seccion "cierra con las medidas de colocacion y de apariencia del Objetivo 4", pero despues del parrafo del Obj 4 (l. 66) viene el de las carencias del Obj 2 (l. 68). La sintesis del Obj 2 queda separada de su evidencia (ll. 54-64) por un parrafo de otro objetivo. | Pasar el parrafo de la l. 66 despues del de la l. 68, o cambiar la oracion de orden de la l. 52 para que describa el orden real. |
| guia-5 | baja | G-B7 | capitulo2.tex:84 | Patron PAT-79 reincide. A Radzi et al. se les da la condicion ("un solo tobillo cadaverico", tornillos de 3.5 a 4.0 mm); a Cassanego et al. no se les da la suya, que la ficha registra y que es la limitacion mas fuerte frente a $B_{\delta}$: seis miembros toracicos caninos cadavericos, condilo humeral, tornillos de 3.0 a 3.5 mm. | Anadir la especie, el sitio y el calibre de Cassanego et al. en la oracion de las condiciones. |
| guia-6 | baja | G-B9, G-T4 | capitulo2.tex:82-86 (contra capitulo3.tex:176) | El cap. 3 apoya la decision de generar mas alla de la mascara en el experimento de dilatacion de mascara de Karageorgos et al. (RMSE 7.57 frente a 54.82 HU al contraerla), y la seccion del capitulo 2 dedicada a la extension del artefacto no lo examina. El lector del estado del arte no ve la unica evidencia que el metodo cita para el sentido del error de $B_{\delta}$. | Una oracion en la l. 84 o 86 con ese resultado y su condicion (mascara de reduccion en el dominio del sinograma, no banda de generacion), con remision a `sec:sintetizador`. |
| guia-7 | baja | G-T2 | capitulo2.tex:64, :74, :76, :124; :84 | Patron PAT-14 reincide. "Marco" designa el marco de referencia de Kaiser et al. (l. 64) y el esquema multiventana de la MAR (ll. 74, 76, 124). En la l. 84, "punto de referencia" usa la palabra que BITACORA §2 reserva para la referencia clinica. | Mantener "marco" para Kaiser et al. y llamar al otro "esquema multiventana de la MAR" o similar; en la l. 84, "desde donde miden" o "origen de su medida". |
| guia-8 | baja | G-B8 | capitulo2.tex:111 (contra :118) | Patron PAT-69 reincide. La celda de evaluacion de la fila propia pone el protocolo fisico al lado de la copia y pegado, sin la condicion que la l. 118 y la introduccion le dan (en un subconjunto de pacientes y segun el plazo). | "frente a copia y pegado y, segun el plazo, al protocolo fisico". |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | cumple salvo guia-7 (baja); siglas y terminos usados (SAP, S1, SSIM, PSNR, MAR, traza metalica, ida y vuelta) definidos antes o en su primera aparicion |
| G-T3 | cumple ($G$, $M$, $B_{\delta}$, $p$ iguales a los de la introduccion y el cap. 3) |
| G-T4 | cumple con GAP (`\GAPDATO` de Li et al., l. 80); cotejo cifra a cifra, del auditor |
| G-T5 | no cumple en parte (guia-4); hacia el cap. 3 cumple (l. 126); desde el cap. 1: no evaluable (esqueleto) |
| G-T6 | cumple (lint PASA) |
| G-B5 | cumple a medias: Obj 1 (l. 78), Obj 2 (l. 68), Obj 3 (l. 30) y la mitad de apariencia del Obj 4 (l. 66) cumplen; falta el componente de densidad de SAP (guia-3) |
| G-B6 | cumple con GAP (`\GAPDEC` del protocolo de busqueda, l. 12) |
| G-B7 | cumple; guia-5 (baja) |
| G-B8 | no cumple en parte (guia-1): tabla y fila propia presentes, sin supuestos y con resultados solo en dos filas |
| G-B9 | cumple salvo guia-2 (media) y guia-6 (baja) |
| G-B10 | cumple con GAP (l. 118 = `introduccion.tex`:54, mismo `\GAPDEC`). Fuera de esta seccion: la introduccion (l. 58) enuncia el primer elemento del aporte sin el precedente de Wang et al. 2019 que el capitulo concede (l. 122), y dice "codificacion de la entrada" (l. 60) frente a "entrada y salida" (l. 76); no se reporta aqui |
| P-EA1 | cumple (prepublicaciones senaladas: Wu 2025, Chen 2026; fuente de solo resumen senalada) |
| P-EA2 | cumple (fuentes principales con resultados y su condicion) |
| P-EA3 | cumple con GAP (aporte en l. 120 con salvedad de ida y vuelta; reclamo de novedad con `\GAPDEC`, l. 124) |

Patrones VIGENTES de mi dominio comprobados: PAT-3 (no reincide), PAT-14 (reincide, guia-7), PAT-31 (sin
cifras propias; en cifras ajenas se ve como PAT-79, guia-5), PAT-36 (no reincide: "solo las series clinicas",
"solo la simulacion fisica" se sostienen), PAT-49 (no reincide, l. 120), PAT-64 (no reincide: l. 30 partida
por familia), PAT-65 (del auditor), PAT-66 (no reincide: ll. 44, 68, 116 con la misma formula), PAT-67 (no
reincide: cada celda tiene respaldo en el cuerpo), PAT-68 (no reincide), PAT-69 (reincide, guia-8), PAT-70
(reincide en parte, guia-3), PAT-71 (reincide, guia-4), PAT-72 (no reincide), PAT-73 (no reincide), PAT-74
(no reincide), PAT-76 (reincide, guia-2), PAT-77 (no reincide: Wu 2025 fuera de la difusion segun su ficha),
PAT-78 (no reincide), PAT-79 (reincide, guia-5), PAT-81 (no reincide, l. 80). Los de criterio solo E-*
(PAT-18, -33, -39, -59, -75, -80, -82) quedan para `revisor-estilo`.

## Propuestas de criterio
- Que la tabla comparativa del estado del arte incluya en la fila propia los supuestos que el capitulo
  declara como base de la brecha. Hoy cae bajo G-B8 sin precision.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Cifras ajenas sin la consecuencia para el objetivo o la decision de alcance que tocan | G-B9, E-M4 | "el 36.5 % de los tornillos en S1 y el 14.8 % en el segundo" | PAT-76 |
| Objetivo que produce definiciones sin comparacion critica de uno de sus componentes | G-B5 | SAP con tres componentes; densidad sin fuente ni carencia en el cap. 2 | PAT-70 |
| Oracion de orden que no describe el orden real de los parrafos | G-T5 | "Cierra con las medidas ... del Objetivo 4" (cierra con el Obj 2) | PAT-71 |
| Limitacion de un trabajo mas debil que la de su ficha | G-B7 | Cassanego sin "condilo humeral canino, tornillos de 3.0-3.5 mm" | PAT-79 |
| Un termino designa dos cosas en el capitulo | G-T2 | "marco" de Kaiser y "marco multiventana" de la MAR | PAT-14 |
| Salvedad de otro lugar omitida al repetir el hecho | P-EA3, G-B8 | "streak amplitude frente a copia y pegado y al protocolo fisico" | PAT-69 |
| Tabla comparativa sin los supuestos ni los resultados que pide el criterio | G-B8 | columna "Evaluacion reportada" con nombres de metricas, sin cifras | nuevo |
| Evidencia que el metodo cita para un parametro ausente de la seccion del estado del arte que lo discute | G-B9 | dilatacion de mascara de Karageorgos (cap. 3) ausente de la seccion sobre $B_{\delta}$ | nuevo |
