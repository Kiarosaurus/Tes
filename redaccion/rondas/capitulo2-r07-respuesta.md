# Respuesta del redactor — capitulo2 — r07 (ronda unica)

Archivos editados: `overleaf/secciones/capitulo2.tex`; `overleaf/secciones/anexos.tex`:29 (fila "Este trabajo" de
la Tabla A.1, autorizada por el orquestador para guia-2/T03); `redaccion/MAPA.md`; `docs/literatura/_candidatos.md`
(fila 47, T10). Lint final: PASA (0/0/0), GAP lit=1, dato=2, dec=2. PDF de etapa: `redaccion/.build/etapas/capitulo2-r07.pdf`.

Alineacion del resultado del Objetivo 3 con `introduccion.tex` (parrafos de resultado y del protocolo fisico) y con
`capitulo3.tex` r23 (`sec:ap-sintesis`, `sec:ap-contrastes`, `sec:v2`): contraste primario = equivalencia frente al
protocolo fisico con titanio, 13 pacientes de prueba sin metal, tornillo en el eje del corredor sin perturbar,
desenlace no concluyente (DEC 2026-10-15 pto 15; `experiments/objetivo3/resultados_prueba_v1.md`); copia y pegado =
control de cordura. Sin cifras en el cap. 2 (BITACORA §2 2026-10-14: las cifras de prueba van al cap. 4).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | §Brecha: "prevé ... según el plazo ... sobre las poses del muestreador" sustituido por la formulacion de la introduccion: contraste primario frente al protocolo fisico con titanio, 13 pacientes, eje sin perturbar (`sec:ap-sintesis`); la comparacion no cubre las poses del muestreador; copia y pegado como control de cordura (`sec:ap-contrastes`); cierre "en prueba quedó sin concluir (véanse los objetivos)" |
| guia-2 | guia | APLICADO | `anexos.tex`:29: SAP ejecutado; sintetizador (version 1) frente al protocolo fisico con titanio, contraste primario, 13 pacientes, eje sin perturbar: no concluyente; copia y pegado solo control de cordura; realismo pendiente. Sin cifras |
| guia-3 | guia | APLICADO | `\GAPDATO` "el modelo final no está elegido" retirado. Prosa: la version 1 se comparo en prueba con el protocolo fisico, resultado no concluyente en el capitulo de resultados. Queda solo la marca de realismo, identica a la de la introduccion. La version 2 NO se marca con la `\GAPDATO` de la introduccion: el cap. 3 (r23, l. 289) ya dice que su evaluacion exploratoria se ejecuto (MAPA, fila de v2: la marca de la introduccion "debe alinearse"); copiarla reintroduciria PAT-122. Se remite a `sec:v2` |
| guia-4 | guia | APLICADO | §Representacion: "la comparación prevista ... podría contradecir" -> "ya ejecutada y no concluyente en la partición de prueba, es la que puede contradecir ese supuesto", como la introduccion. l. 114 revisada: no contradice |
| T01 | trazabilidad | APLICADO | Igual que guia-3 |
| T02 | trazabilidad | APLICADO | Igual que guia-1 (jerarquia, pose, plazo y tiempo verbal) |
| T03 | trazabilidad | APLICADO | Igual que guia-2 |
| T04 | trazabilidad | APLICADO | Parrafo nuevo tras Liu et al.: Goerres et al. (atlas de 12 pelvis femeninas; rama pubica superior e ilion; sacroiliacos como trabajo futuro) y Han et al. (40 pelvis; transiliaco-transsacros de S1 y S2; trayectoria recta ajustada al mapa de acumulacion), desde sus fichas; Yang et al. nombrado sin `\cite` con `\GAPDEC` de la clave (#192 (a); `yang2022computeraided` no esta en `referencias.bib`). Cierre: una trayectoria por corredor, ninguno modela malposicion graduada (el gap del muestreador se mantiene, #180/#192). Carencia del Obj 2 ajustada a "una trayectoria por corredor" |
| T05 | trazabilidad | ESCALADO | `\GAPDEC` en §Brecha tras las piezas publicadas: si la sintesis aprendida de artefacto en MAR no pareada (#179) se nombra y acota la brecha. No se redacta la reformulacion (regla 3 y 14; #179 ABIERTA) |
| T06 | trazabilidad | APLICADO | §Representacion, tras la convencion de 12 mm: "En componentes metálicos del tamaño de un tornillo, el artefacto real medido en la cohorte queda dentro de esa banda (Sección sec:v2)". Fuente: DEC 2026-10-13 (D1) y `capitulo3.tex` `sec:v2` ("La banda de 12 mm alcanza..."). Sin cifras de #177 |
| ES-01 | estilo | APLICADO | Igual que guia-1; con la propuesta del revisor, partida en dos oraciones por E-O1 (lint) |
| ES-02 | estilo | APLICADO | Igual que guia-3 |
| ES-03 | estilo | APLICADO | "equivalencia con el protocolo físico"; "simulación física" queda solo para la familia (BITACORA §2 2026-10-05) |
| ES-04 | estilo | APLICADO | Jacob et al.: "aunque la cicatriz suele ocupar menos del 1 % de la imagen, y atribuyen a la compresión del espacio latente que ese SSIM baje. Este trabajo lee esa atribución..." (ficha, "typically occupy <1% of the image", Sec. 1, p. 2). "Suele" traduce "typically" (E-R6) |
| ES-05 | estilo | APLICADO | Eliminada la oracion "Ninguna las usa como codificación de entrada y de salida..." del parrafo de Li et al. |
| ES-06 | estilo | APLICADO | Negativo fusionado en la apertura del parrafo de autoencoders; eliminado el cierre repetido |
| ES-07 | estilo | APLICADO | Aperturas de l. 90, 96 y 98 reescritas con el tema como sujeto (propuesta del revisor); Radzi y Cassanego citados en la apertura y sin `\cite` repetido despues |
| ES-08 | estilo | APLICADO | Funcion dicha una vez al abrir (Zwingmann 2010: "por dos razones, y solo se cita de forma descriptiva"); cierre eliminado |

Bajos aplicados (baratos, sin choque): guia-5 (una oracion: la validacion de Peters et al. es en fantoma y no frente
al artefacto de pacientes con implante, que es lo que compara el contraste de realismo, `sec:ap-realismo`; no se
afirma un negativo universal sobre todas las fuentes, porque no se cotejaron todas las fichas), T07 (cubierto por
guia-1 y guia-4), T08 ("cerca del centro", l. 44 y §Brecha), T09 ("mínima media"), ES-09 ("TC ya reconstruidas, sin
proyecciones"), ES-10 (partido en dos oraciones por E-O1), ES-11, ES-12, ES-13, ES-14, ES-15. T10: MAPA (filas del
`\GAPLIT` de Niu y de Jacob/anexos) y `_candidatos.md` fila 47 actualizados; el `\GAPLIT` sigue (sin PDF ni ficha).

Cambio colateral por lint (E-O1, oraciones de mas de 40 palabras tras las correcciones): §Brecha (presentacion de la
tabla) se partio en dos oraciones y la fila propia se reformulo para no pasar de siete oraciones por parrafo (PAT-58).

## Decisiones de redaccion

- Resultado del Objetivo 3 fuera de la introduccion y del cap. 3: solo el desenlace ("no concluyente", "en prueba quedó
  sin concluir") con remision ("véanse los objetivos" o "capítulo de resultados"), sin cifras; tambien en celdas de
  tabla. La pose se dice "con el tornillo en el eje del corredor sin perturbar" y la copia y pegado siempre "control de
  cordura".
- Al copiar una marca GAP de otra seccion, se coteja antes con la seccion que la redacto por ultimo: la `\GAPDATO` de
  la version 2 de la introduccion ya esta desfasada respecto de `capitulo3` r23 y no se replica; se remite a `sec:v2`.
- Fuente con ficha cuya clave no esta en `referencias.bib` por una decision pendiente (#192): se nombra por autor, sin
  `\cite`, con `\GAPDEC{clave bibliográfica ... pendiente de la autora (implicancia n)}`.
