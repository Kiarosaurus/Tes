# Revision guia CS — capitulo2 — r07

Leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§1 y §2), `capitulo2.tex`,
`anexos.tex` (Tabla A.1), `introduccion.tex`, `capitulo3.tex` (§obj1, §sintetizador, §apariencia),
`capitulo2-r06-respuesta.md`, `capitulo2-r07-lint.md` (PASA, sin hallazgos).
Respuesta r06: ningun hallazgo de guia RECHAZADO; guia-4 (PAT-88) y guia-3 quedaron pendientes fuera de la seccion.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-B10 | capitulo2.tex:106 | Patron PAT-175 reincide. La bisagra describe una comparacion que ya no es la del diseno: copia y pegado como comparacion principal y el protocolo fisico "sobre las poses del muestreador ... segun el plazo" como segunda. La introduccion (l. 60) y `sec:ap-sintesis` (cap. 3 l. 337, 357) dicen lo contrario: el protocolo corre con el tornillo en el eje del corredor sin perturbar, la equivalencia frente a el es el contraste primario y la copia y pegado es control de cordura. Ademas, si el protocolo corriera sobre las poses del muestreador, el propio diseno produciria a la vez distribucion de poses y apariencia fisica, y debilitaria la tension que la oracion anterior enuncia (cf. PAT-55). | Reescribir las dos oraciones "El diseno ... preve" con la formulacion de la intro l. 60: contraste primario = equivalencia frente al protocolo fisico, en el eje sin perturbar y en 13 pacientes de prueba sin metal; la comparacion no cubre las poses del muestreador; copia y pegado como control de cordura. Cerrar la ultima oracion con el desenlace ("en prueba quedo sin concluir", remision al cap. 4). |
| guia-2 | media | G-B8 | anexos.tex:29 | Patron PAT-122 reincide. La fila propia de la tabla comparativa dice "sin resultado del sintetizador, que se comparara por *streak amplitude* con la insercion por copia y pegado y, segun el plazo, con el protocolo fisico". El resultado existe (intro l. 52) y el orden de los brazos esta invertido respecto del cap. 3. La columna exige "resultado reportado y su condicion". | Dar el resultado con su condicion, como en la intro l. 52: no concluyente frente al protocolo fisico con titanio, en el eje sin perturbar, 13 pacientes de prueba, modelo evaluado de la version 1 (cifras si la decision de bitacora 2026-10-14 lo permite fuera del cap. 4; si no, solo el desenlace con remision). Copia y pegado como control de cordura. |
| guia-3 | media | G-T4 | capitulo2.tex:102 | Patron PAT-122 reincide (y PAT-19). El `\GAPDATO` dice que "no existe aun resultado del Objetivo 3 porque el modelo final no esta elegido", pero el punto de control de la version 1 se eligio en validacion y su prueba ya dio desenlace (intro l. 52; cap. 3 l. 196, `sec:ap-contrastes`). | Decir que el Objetivo 3 tiene desenlace en prueba (cap. 4) y dejar en GAP solo lo pendiente: contraste de realismo y version 2, con las mismas marcas que la intro l. 52, sin duplicar texto nuevo. |
| guia-4 | media | G-T4 | capitulo2.tex:92 | Patron PAT-116 reincide. "La comparacion prevista con el protocolo fisico podria contradecir ese supuesto" trata como futura una comparacion ya ejecutada; la intro (l. 84) dice "ya ejecutada y no concluyente". El supuesto que sostiene la brecha queda descrito distinto en los dos bloques. | Igualar con la intro: la comparacion con el protocolo fisico, ya ejecutada y no concluyente (cap. 4), es la que puede contradecirlo. Revisar tambien que l. 114 no implique lo contrario. |
| guia-5 | baja | G-B5 | capitulo2.tex:94 | El Objetivo 3 incluye un contraste de realismo frente a observaciones reales, con estadisticos que no exigen imagen sin metal (intro l. 41, `sec:ap-realismo`). El capitulo no dice si algun trabajo revisado compara artefacto simulado o sintetico con observaciones reales; Selles et al. (l. 94), que miden HU cerca del implante y en el lado contralateral sin imagen sin metal, solo aparecen como fuente de extension del artefacto. | Una oracion que diga si las fuentes revisadas contrastan apariencia generada con observaciones reales (Peters et al. validan contra fantoma, no contra pacientes), conectada con el contraste de realismo. |

TOTAL alta=1 media=3 baja=1

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple (pendiente fuera de la seccion: l. 86 da por medida la ida y vuelta sin autoencoder y `sec:obj1` no la describe, aunque la intro l. 46 ya da sus cifras; guia-4 de r06, PAT-88) |
| G-T2 | cumple |
| G-T3 | cumple ($M$, $G$, $B_\delta$ iguales a intro y cap. 3) |
| G-T4 | no cumple (guia-3, guia-4) |
| G-T5 | cumple (l. 10 describe el orden real) |
| G-T6 | cumple (lint PASA) |
| G-B5 | cumple, con mejora baja (guia-5); Obj 1, 2 y 4 con carencias explicitas (l. 72, 74-76, 88-90) |
| G-B6 | cumple (revision dirigida declarada, l. 12) |
| G-B7 | cumple |
| G-B8 | no cumple (guia-2: fila propia sin resultado vigente) |
| G-B9 | cumple |
| G-B10 | no cumple (guia-1). La tension en si coincide palabra por palabra con intro l. 58. Pendiente fuera de la seccion: intro l. 66 limita el aporte a la "codificacion de la entrada" y cap. 2 l. 84/86 y cap. 3 l. 196 dicen "entrada y salida" (guia-3 de r06) |
| P-EA1 | cumple (prepublicaciones senaladas) |
| P-EA2 | cumple (resultados con condicion para las fuentes principales; Jacob et al. sin cifras con motivo) |
| P-EA3 | cumple (l. 108-114) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| La seccion promete ejecutar sobre las poses del muestreador lo que una decision fija sobre el eje sin perturbar | G-B10, G-T4 | "Preve, ademas, ejecutar el protocolo fisico sobre las poses del muestreador" | PAT-175 |
| GAP o celda sobre un resultado propio que envejecio: la prueba ya dio desenlace | G-T4, G-B8 | "no existe aun resultado del Objetivo 3 porque el modelo final no esta elegido" | PAT-122 |
| Condicional sobre una comparacion ya ejecutada | G-T4 | "la comparacion prevista con el protocolo fisico podria contradecir ese supuesto" | PAT-116 |
| Capitulo cerrado en rondas previas no se recoteja cuando otro capitulo incorpora un resultado nuevo (aqui, la prueba de la version 1) | G-T4, G-B10 | Intro r07 reporta -301.0 HU; cap. 2 sigue "sin resultado del sintetizador" | nuevo (afin a PAT-176) |
