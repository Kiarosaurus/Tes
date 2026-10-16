# Respuesta del redactor — introduccion — r08 (ronda unica, encargo 2026-10-15b)

Archivo: `overleaf/secciones/introduccion.tex`. Fuentes nuevas: DEC 2026-10-15 (3) ptos 1, 3, 5 y 9;
`experiments/objetivo3/resultados_dec_2026-10-15.md` (variantes :34-63, v2 :83-100, piso :71-81); `capitulo2.tex`
(r08) :40 y :116; `capitulo3.tex` (r24) :38, :289, :417-419, :529-533; fichas `lyu2021ududonet`, `xia2024pndnet`,
`deman1999`. Encabezado (l. 3-17) y Formulacion: solo se envolvieron pasajes en `\REVVISUAL` (#126 sigue ABIERTA).

Cifras: ninguna nueva. "dos pacientes de validacion" (C3 :419, :527); v2 sin cifras (RDEC :87-91, desenlace "no
concluyente, dif. < Peters" en la variante base de los dos modelos); piso solo con su sentido (DEC (3) pto 3; C3 :531).

Lint final: FALLA solo por l. 7 (E-O1, encabezado, #126) y la baja "robustos" de l. 7. GAP: lit 0, dato 7, dec 0.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| E-O1 l. 7 | lint | ESCALADO | Encabezado DESFASADO (#126), decision de la autora; no se reescribe |
| guia-1 | guia | APLICADO | Parrafo nuevo tras el tercer enfoque: sintesis aprendida de componentes como paso intermedio de la MAR no pareada (`lyu2021ududonet`, `xia2024pndnet`; fichas: componentes extraidos de otras imagenes con metal, sin geometria ni pose; ninguna evaluacion de la imagen sintetizada) y brecha con la formula literal del pto 9, la misma de cap2:116. Tercer elemento del aporte alineado con cap2:120 |
| guia-2 | guia | APLICADO | :52: lectura en dos niveles (objetivo de diseno y evaluacion cumplido; hipotesis de equivalencia, que un intervalo entero fuera del margen habria rechazado y que no se sostiene, sin leerse como no equivalencia demostrada), declarada posterior a la prueba de las dos versiones, con remision a `sec:ap-analisis` (C3 :419). :50 sin "haria fallar el objetivo"; :60 sin repetir el desenlace |
| guia-3 | guia | APLICADO | `\REVVISUAL` en l. 15 (reclamo de coherencia de la apariencia, nombrado en E1), pregunta, Obj 3 (comparacion con observaciones reales), contraste de realismo con su GAP, comparacion a ciegas, supuesto del dominio de imagen (:84), parrafo de limitaciones frente a lo real (:94) y :96 hasta "placas y protesis". No se envuelve el proposito de la banda (l. 13, Obj 3): es diseno, no reclamo, y capitulo2-r08 solo marca truncamiento y suficiencia de $B_\delta$ |
| guia-4 | guia | APLICADO | Marca de v2 retirada: evaluacion ejecutada salvo la comparacion a ciegas (con el `\GAPDATO` de C3 :289, dentro de `\REVVISUAL`), no concluyente a la baja en los dos modelos, remision al cap. 4, sin cifras |
| guia-5 | guia | APLICADO | :98 "se tomo en los dos brazos (capitulo de resultados)", sin marca (BITACORA §2 2026-10-15, capitulo3-r23) |
| guia-6 | guia | APLICADO | :50 oracion nueva: el piso de ruido del sintetizador favorece al sintetizador; :96 lo repite como desenlace de los analisis de asimetria. Sin cifras |
| guia-7 | guia | APLICADO | :84 "podia contradecirlo, y su desenlace no concluyente no lo confirma ni lo refuta", dentro de `\REVVISUAL` |
| S01 | estilo | APLICADO | "El desenlace es no concluyente: los datos no permiten afirmar la equivalencia, y la *streak amplitude* ... es menor" (formula de capitulo2-r08) |
| S02 | estilo | APLICADO | "La insercion por copia y pegado no produce rayas, y superarla es un control de cordura ..." |
| S03 | estilo | APLICADO | :60 sin los 13 pacientes ni el desenlace; :84 reescrito por guia-7 |
| S04 | estilo | APLICADO | Oracion tematica de la justificacion reescrita como se propuso |
| S05 | estilo | APLICADO | Queda solo la razon propia, con remision al alcance |
| S06 | estilo | APLICADO | Orden: enfoques 1-2, enfoque 3, MAR no pareada y brecha (guia-1), protocolo fisico como comparador |
| S07 | estilo | APLICADO | Primera oracion sin "no sustituye al sintetizador" |
| S08 | estilo | APLICADO | Cierre: "Ninguno de esos modelos tiene una senal de entrenamiento para los cambios de intensidad que el objeto induce fuera de su mascara" (antecedente explicito, no "esos cambios") |
| S09 | estilo | APLICADO | "En sus simulaciones, esas rayas aparecen fuera del metal: irradian desde el, siguen las direcciones de maxima atenuacion o conectan los objetos metalicos" (ficha `deman1999`, "Donde entra": las tres formas) |
| S10 | estilo | APLICADO | Oracion "El aporte del sintetizador es la combinacion ..." retirada; "El aporte de este trabajo se limita" -> "Lo propio de este trabajo es". La copia exacta fuera de $G$ no se agrega al tercer elemento, para que el aporte coincida con cap2:120 (G-B10 manda sobre E-R5); sigue dicha en l. 13 |
| S11 | estilo | APLICADO (parcial) | Inversion de metricas llevada a `sec:apariencia` con remision; queda en siete oraciones porque la definicion de MAR (primera aparicion en el documento) vive en ese objetivo |
| S12 | estilo | APLICADO | "Ningun objetivo evalua esa adopcion" |
| S13 | estilo | APLICADO | |
| S14 | estilo | APLICADO | Ver guia-7 |
| S15 | estilo | APLICADO | Se conserva el de :50; :60 retirado al reescribir; :80, :92 y :94 -> "por lo que"; :88 con dos puntos |
| S16 | estilo | APLICADO | |
| S17 | estilo | APLICADO | |
| S18 | estilo | APLICADO | "observaciones reales de artefacto" en :52 y :94 ("tornillos reales" y "lo real" retirados) |
| T01 | trazabilidad | APLICADO | Ver guia-4 |
| T02 | trazabilidad | APLICADO | Ver guia-5; fila de MAPA cerrada |
| T03 | trazabilidad | APLICADO | Ver guia-2. La oracion del objetivo cumplido queda fuera de `\REVVISUAL` (no afirma calidad de apariencia) |
| T04 | trazabilidad | APLICADO | Se retiro la clausula en lugar de reatribuirla: el rechazo de la hipotesis va en :52, en los dos niveles. Aviso al orquestador: la fila de BITACORA §2 2026-10-15 ("en la introduccion, 'no equivalencia, que haria fallar el objetivo'") queda sustituida |
| T05 | trazabilidad | APLICADO (parcial) | Ver guia-3. l. 41 or. 6 (proposito de la banda) no se envuelve; l. 98 tampoco (desplazamientos de transferencia, no reclamo de realismo; era opcional) |
| T06 | trazabilidad | APLICADO | Ver guia-6 |

Bajas: aplicadas guia-8 (protocolo fisico primero, como contraste primario; copia y pegado como control de cordura),
guia-9, T07 (corregido: solo los analisis de cortes y de suelo "no cambian el desenlace"; el contraste referido a la
propia sintesis sin metal, descriptivo, queda entero fuera del margen, asi que "ninguno cambia el desenlace" habria
dicho mas que RDEC), T08 (proposito: "esta pensada para que ... puedan aparecer"), T09, S19 (al reescribir :60),
S20-S24, S26-S29. No aplicadas: S25 (el orden del parrafo sigue la enumeracion de :72: cohorte e implante, luego nivel
sacro y forma de la sintesis). ESCALADAS (#126, encabezado): guia-10, guia-11, T10. T11: aviso, `tesis/main.tex` sin
el resultado de prueba (regla 4 raiz).

`\GAPLIT` nuevos: ninguno. La lectura de "no concluyente" remite a `sec:ap-analisis`, donde capitulo3-r24 ya puso el
`\GAPLIT` de la fuente metodologica; la introduccion no nombra Pitman y Morgan, Bland y Altman ni una prueba visual.
`\GAPDATO`: cerrados 2 (v2 en prueba; salto en el borde de $G$); abierto 1 (comparacion visual a ciegas, copiado de
C3 :289 tras cotejarlo).

## Para la autora
- #193: la pregunta de investigacion (l. 21) y la oracion de coherencia de la apariencia (l. 15) quedan en rojo por el
  encargo E1 ("reclamo de coherencia de apariencia del Objetivo 3"), aunque el encabezado sigue bajo #126.
- El desenlace del TOST frente al protocolo fisico y la lectura de dos niveles no van en rojo (criterio de capitulo2-r08:
  la medida de *streak amplitude* frente al protocolo no es realismo visual).

## Decisiones de redaccion
- Lectura del Obj 3 en la introduccion: desenlace con la formula de capitulo2-r08 ("no concluyente: los datos no
  permiten afirmar la equivalencia, y la *streak amplitude* ... menor"), seguido de los dos niveles del pto 1 y de su
  momento ("despues de ver la prueba de equivalencia de las dos versiones"); los tres desenlaces se enuncian sin
  consecuencia para el objetivo. Sustituye la fila de BITACORA §2 2026-10-15 "no equivalencia, que haria fallar el
  objetivo".
- Brecha en la introduccion: los tres enfoques, un parrafo propio para la sintesis aprendida de la MAR no pareada y la
  formula literal del pto 9; el comparador (protocolo fisico) va despues de la brecha, no entre los enfoques.
- Proposito de diseno de $B_\delta$ ("esta pensada para que ... puedan aparecer") no va en `\REVVISUAL`; su
  suficiencia, el truncamiento y la estructura de raya si.
- "Piso de ruido" (termino de C3 :529-531) para la amplitud de solo ruido de cada brazo; fuera del cap. 3, solo el
  sentido ("favorece al sintetizador"), sin cifras.
