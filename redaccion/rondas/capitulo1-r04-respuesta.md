# Respuesta del redactor — capitulo1 — r04

Archivo: `overleaf/secciones/capitulo1.tex`. Reportes leidos: `capitulo1-r04-guia.md`, `-estilo.md`,
`-trazabilidad.md`, `-lint.md` (PASA, 0/0/0). Respuesta previa: `capitulo1-r03-respuesta.md`.
Hallazgos sacados por oscilacion: ninguno.

## Altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 (media) | guia | APLICADO | §1.1, cifra 0.42: se restituyen "en la mediana" y "del corredor", y el ambito "dentro de las mascaras sacras", como en `capitulo3.tex`:85. Se une con T01 y S01 |
| S01 (media) | estilo | APLICADO | El parrafo vuelve a 7 oraciones: se elimina la apertura "Dos umbrales de HU reaparecen en todo el documento" (tambien PAT-114) y "Ambos" pasa a "Los dos umbrales". La fusion en una sola oracion propuesta daba 63 palabras (lint E-O1), asi que la cifra y su consecuencia quedan en dos oraciones cortas. Condicion: "En la cohorte primaria, con el recorte por defecto" (`capitulo3.tex`:52, :85; `maintex_cifras.md`:17, fila 10, recorte 6 mm) |
| S02 (media) | estilo | APLICADO | §1.2, metricas de Peters: "exige invertirlas; la definicion operativa de esa inversion esta pendiente para cada metrica (Seccion apariencia)". Respaldo: `\GAPDEC` de `capitulo3.tex`:215. No se agrega otro `\GAPDEC` aqui: el pendiente se dice en prosa y remite al GAP del cap. 3 |
| S03 (media) | estilo | APLICADO | La justificacion del umbral de 10 mm de Kaiser et al. (holgura de 1 a 2 mm, lectura como holgura radial por lado) pasa al parrafo del corredor (l.78, 7 oraciones). En el del marco de referencia queda la regla de 5 mm leida como margen cortical (5 oraciones). Se elimina "por su parte" |
| S04 (media) | estilo | APLICADO | §1.4, 2.5D: se quita la segunda caracterizacion de Glover y Pelc (PAT-102) y se remite a `sec:mt-artefactos`; se dice la consecuencia: el sintetizador opera sobre valores reconstruidos (`capitulo3.tex`:172), no contiene ese mecanismo y a lo sumo aprende la apariencia que deja en los cortes, como lectura de este trabajo |
| S05 (media) | estilo | APLICADO | Junto con T03 (baja): "El veredicto de esa extension se presenta en el capitulo de resultados; si fuera aprobatorio, la multiplicidad de siete combinaciones si podria haberlo favorecido". Se deriva de la oracion previa ("solo puede favorecer un veredicto aprobatorio") sin adelantar el veredicto (BITACORA §2 2026-09-29) |
| S06 (media) | estilo | APLICADO | PAT-114. l.64 abre con el contenido ("La MAR elimina... la simulacion fisica lo produce...; este trabajo no hace ni lo uno ni lo otro") y se elimina la oracion que lo repetia. l.124 abre con "Para la superioridad, el diseno del Objetivo 3 usa". l.128 abre con "El error absoluto medio y la raiz del error cuadratico medio, los dos errores por voxel del documento, no son intercambiables". Ademas l.54 abre con "El endurecimiento del haz y la dispersion producen rayas parecidas" y l.35 pierde su anuncio de recuento. Se conservan los recuentos que enumeran de verdad (l.62, l.118, l.122) |

## Bajos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-2 | guia | APLICADO | Caption y ultima oracion de la introduccion del capitulo: "pieza de la propuesta" en lugar de "pieza de la cadena"; se quita la remision a `fig:pipeline` del caption. "precede en la cadena al sintetizador" se conserva (el muestreador si es pieza de la cadena) |
| guia-3 | guia | APLICADO (parcial) | El `\GAPDATO` ya no niega que el dato exista: "que solo constan en el codigo del experimento y no en un registro de sus resultados". No se da la forma ni el parametro: si el codigo de `experiments/` cuenta como fuente es decision de la autora (propuesta de criterio de guia). MAPA fila del `\GAPDATO` actualizada |
| guia-4 | guia | APLICADO | "la escala de brecha y la viabilidad del corredor" (`capitulo3.tex`:189) |
| guia-5 | guia | NO APLICADO | Pide no tocar l.11; corresponde a `capitulo3` remitir a `sec:mt-tc` y `sec:mt-artefactos` (PAT-113). Queda para la proxima ronda de `capitulo3` |
| S07 | estilo | NO APLICADO | Leer el artefacto de ruido de De Man et al. como analogo de la inanicion seria una interpretacion nueva sin respaldo en la ficha `deman1999` ni en `docs/`; el texto conserva el hecho negativo sin forzar la relacion |
| S08 | estilo | APLICADO | "su error es la diferencia, en HU, entre el valor original de cada voxel y el recuperado" |
| S09 | estilo | APLICADO | "... de modo que la aceleracion que reportan Song et al. no esta medida sobre TC" |
| T01 | trazabilidad | APLICADO | Ver guia-1 / S01 |
| T02 | trazabilidad | APLICADO | "con un margen definido por la variabilidad ... y aun sin preinscribir" (`capitulo3.tex`:225, :231) |
| T03 | trazabilidad | APLICADO | Ver S05 |

## GAP

Sin GAP nuevos ni cerrados. Se modifica el texto del `\GAPDATO` de la compresion arcoseno hiperbolico
(guia-3). Totales del lint: lit=4, dato=1, dec=8.

Lint final (`--compilar`): PASA, alta=0 media=0 baja=0. Una pasada intermedia dio 3 medias E-O1
(oraciones de 63, 42 y 44 palabras en l.35, l.66, l.78), corregidas partiendo las oraciones.

## Decisiones de redaccion

- Una cifra del cap. 3 retomada en el marco teorico lleva su cohorte y variante ("en la cohorte
  primaria, con el recorte por defecto") y el calificador estadistico en la oracion de consecuencia
  ("en la mediana"), aunque eso obligue a partirla en dos oraciones.
- Un `\GAPDATO` sobre un dato que existe solo en codigo dice "solo consta en el codigo del
  experimento y no en un registro", no "no consta en las fuentes", mientras la autora no decida si
  el codigo de `experiments/` cuenta como fuente.
- Cuando el marco teorico menciona un procedimiento cuya definicion esta en `\GAPDEC` en el cap. 3
  (p. ej., la inversion de las metricas de Peters et al.), lo dice en prosa ("esta pendiente") y
  remite a la seccion, sin duplicar el `\GAPDEC`.
