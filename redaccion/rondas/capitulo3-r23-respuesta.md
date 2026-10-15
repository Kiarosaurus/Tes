# Respuesta del redactor — capitulo3 — r23 (ronda unica)

Archivo: `overleaf/secciones/capitulo3.tex`. Lint final: `python scripts/lint_redaccion.py capitulo3 --compilar` ->
PASA (alta 0, media 0, baja 23 E-P1 preexistentes; GAP lit=0, dato=20, dec=3; 154 paginas).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | :248 (D7): "El diagnostico ya se ejecuto con esa regla" + `\GAPDATO` "calculado con la regla fijada; consta en una implicancia abierta (191)". :287 (v2): la evaluacion exploratoria "ya se ejecuto"; marca con #184 y #190. :509: "no se ha medido" sustituido por "se midio despues ... y su valor se presenta en el capitulo de resultados". Sin cifras de #188-#191 |
| guia-2 | guia | APLICADO + ESCALADO | :509: el sintetizador regenera toda `G`, y su amplitud incluye la diferencia regenerada-original, que puede ser no nula sin implante (estructural, sin cifra). El sentido sobre el contraste primario no esta fijado: `\GAPDEC{... (implicancia 188)}` |
| guia-3 | guia | APLICADO | :216 fecha el cambio ("El 15 de octubre, despues de ver el resultado de la version 1, se decidio no entrenarlo"). Lista de :473 ampliada con la sustitucion del semimaximo y, para v2, margen comun, E-A1 con 0.030 y protocolo a ciegas (DEC 2026-10-15 ptos 4, 10, 16, 19) |
| guia-4 | guia | APLICADO + ESCALADO | :411: "Para el Objetivo 3, la no equivalencia haria fallar el objetivo" (`introduccion`:50; BITACORA §2 2026-10-15). Que significa "no concluyente" para el objetivo no lo fija ninguna fuente: `\GAPDEC` |
| guia-5 | guia | APLICADO | Junto con T09: forma del artefacto parametrico desde DEC 2026-10-15 (2): `M` a 5371 HU; en la banda y en el plano perpendicular al eje, (1/2) A signo(cos 2 beta), dos lobulos claros y dos oscuros; A = mediana de D1 por anillo, interpolada linealmente, constante bajo 1 mm; fuera, TC original. Parrafo partido en dos (E-O2). Angulo como `\beta` (theta ya lo usa el cap. 1) |
| guia-6 | guia | APLICADO | :495: la fraccion del protocolo fisico bajo -1000 HU (medida en prueba) dice cuanto baja ese brazo del suelo, pero no lo compara con lo real; esa comparacion sigue apoyada en la verificacion de reproduccion |
| guia-7 (baja) | guia | APLICADO | Distancia con signo de `eq:brecha`: `s` -> `\mathrm{dist}` |
| guia-8 (baja) | guia | APLICADO con GAP | El procedimiento (remuestreo de pacientes, 2000) solo consta en el docstring de `d1_alcance_rayas.py`: `\GAPDATO` segun BITACORA §2 2026-10-03 |
| S1 | estilo | APLICADO | :143 "se aparta de esa decision"; :411 "esa multiplicidad no se corrige"; :477 "Ni el margen minimo ni el margen comun miden ...; de ese efecto solo se conoce el sentido" |
| S2 | estilo | APLICADO | :327 "caracterizan al brazo de comparacion y no son un resultado del sintetizador" |
| S3 | estilo | APLICADO | Formula definida una vez en :417 ("el 15 de octubre, despues de ver el resultado de la version 1 en la particion de prueba"); en :143, :230, :335, :337 y :363, "el 15 de octubre" |
| S4 | estilo | APLICADO | DEC pto 9 no da umbral: "La expectativa, fijada antes de generar y sin umbral numerico, es que..." |
| S5 | estilo | APLICADO | "una diferencia medida sobre dos pacientes" |
| S6 | estilo | APLICADO | Se quito "sin embargo"; sujeto explicito ("La desviacion en 0--2 mm de los dos modelos nuevos") |
| S7 | estilo | APLICADO | Regla asimetrica solo en :417; quitada de :473 y :509 |
| S8 | estilo | APLICADO | Punto de control y aislamiento pasan a abrir el parrafo del entrenamiento (:232), que se parte en dos |
| S9 | estilo | APLICADO | :327 partido en "Fuera de $G$, ..."; inciso "para el que valen cero por construccion" eliminado |
| S10 | estilo | APLICADO | :232 y :365 sin conectores encadenados |
| S11 | estilo | APLICADO | DEC pto 7 no distingue modelo de indeterminado: "En otro caso la causa no se atribuye a la lectura" |
| S12-S16, S18 (bajas) | estilo | APLICADO | S12 :200 sin recuento ni ordinales; S13 corredor como motivo; S14 "con la diferencia a la baja" + IC del 90 % (sin "significativa", E-P2); S15 oracion eliminada; S16 margen 0.80-1.25 movido a :415; S18 "la perdida vale" |
| S17 (baja) | estilo | APLICADO | Fundido en la reescritura de T04 |
| T01 | traza | APLICADO | Ver guia-1 (:509) |
| T02 | traza | ESCALADO (desde r22) | `docs/00-tesis.md`:91, :333-335 y `EXPERIMENTOS.md`:96 siguen sin alinear con DEC 2026-10-15 D2/D4 y con #190; no las edita el redactor. El `.tex` sigue a la DEC |
| T03 | traza | APLICADO | `\GAPLIT` retirado; citas `bland1986statistical` (diferencia frente a media, sesgo, limites +-1.96 DE), `pitman1939note` y `morgan1939test` (igualdad de varianzas pareadas, normal bivariada, t con n-2 gl; suma-diferencia atribuida a Morgan, variables estandarizadas a Pitman). Sin el nombre compuesto. `_candidatos.md` 810-811 y MAPA actualizados |
| T04 | traza | APLICADO + ESCALADO | "La prueba compara varianzas y no coeficientes de variacion"; el CV (0.076/0.241, admitido por BITACORA §2 2026-10-15) queda como dato descriptivo aparte. `\GAPDEC{escala de la lectura de acuerdo (HU o razon) y supuestos no cumplidos (implicancia 189)}`. Nada del recalculo en log entra como metodo |
| T05 | traza | APLICADO | Prosa: los analisis anadidos "ya se ejecutaron sobre la particion de prueba, y sus resultados se presentan en el capitulo de resultados". La marca queda solo para su lectura (#187, #188, #189 ABIERTAS) |
| T06 | traza | APLICADO | Ver guia-1 (:287) |
| T07 | traza | APLICADO | D4 con cifra y n (`resultados_dec_2026-10-15.md` D4: 32 componentes de 23 pacientes; mediana -0.24 mm, IQR -0.54 a 0.02; "su efecto sobre el modelo no se midio"). D8 y costura remitidos al cap. 4 (BITACORA §2 2026-10-14), sin marca |
| T08 | traza | APLICADO | :248 y :363 con marca "calculado/calculada; consta en una implicancia abierta (191 / 187)", sin cifras ni veredicto |
| T09 | traza | APLICADO | Ver guia-5 |
| T10 | traza | APLICADO | Lo visto incluye la dispersion entre pacientes y las asimetrias entre brazos de la v1 en prueba y las amplitudes de validacion del otro modelo nuevo (`visto.md`) |
| T11 (baja) | traza | NO APLICADO | Se mantiene 184 HU (#186, BITACORA §2 2026-10-15); unificar 183.5 en `resultados_prueba_v1.md`:46 es de la autora |

Arreglo adyacente no senalado: :419 decia que la amplitud de solo ruido del sintetizador se genera "sobre los mismos
receptores"; en el capitulo "receptores" son las dos pelvis de validacion, y DEC pto 18 la mide en los 13 pacientes de
prueba. Corregido a "sobre los mismos 13 pacientes".

Para la autora (escalados): T02 (fuentes desfasadas); `\GAPDEC` de no concluyente para el Obj 3 (guia-4); escala y
supuestos de la lectura de acuerdo (#189, T04); sentido del piso de ruido sobre el contraste primario (#188, guia-2).
La introduccion conserva la marca de costura y la de v2 "en prueba" con la redaccion anterior: debe alinearse.

## Decisiones de redaccion

- Medicion ya ejecutada cuyo resultado solo sostiene una implicancia ABIERTA: la prosa dice que se ejecuto y la marca
  dice "calculado; consta en una implicancia abierta (n)"; nunca "no medido", "aun no" ni "no se ha ejecutado".
- Medicion ejecutada sobre prueba que no depende de una lectura abierta (D8, costura): sin marca, remision al capitulo
  de resultados; dato de entrenamiento que sostiene una limitacion (D4): cifra con su n en el metodo.
- Prueba de Pitman y Morgan: "prueba de igualdad de varianzas pareadas de Pitman y Morgan", con las dos citas; nunca
  "Pitman-Morgan" ni prueba de coeficientes de variacion. "Bland-Altman" -> "analisis de acuerdo de Bland y Altman".
- Analisis decididos el 15 de octubre: la salvedad "despues de ver el resultado de la version 1 en la particion de
  prueba" se dice una vez (seccion de analisis); en lo demas, "el 15 de octubre".
- Angulo en el plano del implante: `\beta` (theta reservado por el cap. 1); distancia con signo a la envolvente:
  `\mathrm{dist}`.
