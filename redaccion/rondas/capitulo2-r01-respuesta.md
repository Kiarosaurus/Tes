# capitulo2 — r01 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo2.tex`. Se leyeron los cuatro reportes de la ronda
(lint, guia, estilo, trazabilidad). No se abrio ningun PDF: todo sale de fichas de `docs/literatura/`,
de `capitulo3.tex` y de `introduccion.tex`.

Solapes resueltos una sola vez: guia-3 = T07 (salvedad #128.4); guia-4 = ES-01 (parte) = T17 (resumen de
la colocacion); ES-10 = T05 (Zwingmann 2013); ES-12 = guia-11 (McLaren y Ziran); ES-17 = T19 (recuento de
modelos con segmentacion posterior); ES-06 (GAP de Wu) = homonimos.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Parrafo nuevo al final de 2.3, "Las medidas de colocacion publicadas no bastan para calificar una pose generada": grado de Zwingmann asignado por un radiologo sobre TC posoperatoria, sin borde de referencia declarado (ficha `zwingmann2009navigated`, Verificacion pto 2-3); escala de Smith et al. (4 cadaveres, heredada de tornillos pediculares, mas escala angular; ficha `smith2006iliosacral`); definicion binaria de Herman; CSV de Liu como margen de un plan unico (ficha `liu2025pipeline`, l. 147). Se nombran las tres metricas de Peters adoptadas y que se disenaron para MAR. Lo no decidido va con los `\GAPDEC` ya existentes de #11 (angular) y de la inversion de metricas (#16/#17), replicados segun BITACORA §2 ("GAP replicados") |
| guia-2 | guia | APLICADO | El primer elemento se deja en una oracion ("geometria rigida y parametrica, la del tornillo de `sec:geometria`") y un parrafo aparte lo contrasta con lo que las fichas dicen del metal virtual: formas segmentadas a mano (Zhang y Yu), objetos definidos desde TC de metal (Karageorgos), fractales aleatorios (Peters, 2.3 p. 4), mascara tubular (Wang 2019). El umbral se atribuye a los metodos que parten del metal clinico (Karageorgos, Yun, Wang 2025, Li), con Xie como dato de su error. Esos hechos se anadieron tambien en 2.2 (l. 34, 38) |
| guia-3 | guia | APLICADO | Salvedad de #128.4 anadida al final del parrafo del primer elemento, con remision a `sec:sintetizador`, en la misma forma que `introduccion.tex`:58. Resuelve tambien T07 |
| guia-4 | guia | APLICADO | Resumen unico de la carencia: "al azar, con una regla geometrica o a mano" (l. 2.3 carencias y lectura de la tabla). "A mano" se respalda en 2.2 con Wang et al. 2025 (ficha: "carefully adjusting the size, angle, and position", V-A-2) y el elipsoide al azar de Jacob en 2.3 (ficha: "select a random region ... and place an ellipsoid", Sec. 3.1). Cada celda de la tabla tiene ahora oracion de respaldo |
| guia-5 | guia | APLICADO (parcial) | El parrafo de Zhang 2026 y el de mascaras de lesion se separan (ES-09). El nuevo cierra con la consecuencia que las fichas sostienen: la plausibilidad descansa en el azar, la opinion experta o la inspeccion visual (Ramzan: volumen uniforme y comparacion visual, filas 21 y 62; Chen: radiologos; Jacob: region al azar). Se suma como cuarta carencia. No se afirma que ninguno compare con una distribucion clinica: la fila 64 de `ramzan2026claim` ("scar volume distribution using the AHA-17 segment framework") es ambigua. Si la autora quiere esa negacion, conviene una relectura de Ramzan Sec. 3.5 con `lector-papers` |
| guia-6 | guia | APLICADO (parcial) / RECHAZADO en un punto | La oracion del orden dice ahora su criterio real ("de los trabajos que generan imagen a los que fijan sus condiciones") y deja de afirmar que sigue la cadena. RECHAZADO alinear la enumeracion de enfoques de la brecha con el orden de secciones: BITACORA §2 (2026-09-30, capitulo2-r00) y G-B10 exigen enunciar la brecha con las mismas palabras que `introduccion.tex`:54 |
| guia-7 | guia | APLICADO | Karageorgos: SSIM de 0.964 en datos simulados y mejor en 13 de 28 metricas clinicas (ficha, Tabla I p. 28; Sec. III-C p. 12). Yun: sesgo medio de 0.82 HU frente a 3.18-6.30 HU de los cuatro metodos comparados, en una region libre de artefacto de CLINIC-metal (ficha, Tabla 4 p. 11). Sin RMSE para no adelantar una sigla que define el cap. 3 |
| ES-01 | estilo | APLICADO (parcial) | Se quito la frase vacia de apertura y el molde "X, pero Y"; la tabla se lee por columna, con el resumen unico de colocacion (guia-4, T17) y la validacion en fantoma atribuida solo a Peters. Se quito de la brecha la oracion que repetia el inventario ("Los dos primeros..."). No se fundieron los dos parrafos: juntos pasan de 7 oraciones (E-O2, PAT-58). El recuento de enfoques queda solo en la brecha |
| ES-02 | estilo | APLICADO | Sin ", por eso,", ", entonces," ni ", por tanto," en el capitulo: l. 38, 40, 52, 66, 70 y 74 reescritas diciendo la causa |
| ES-03 | estilo | APLICADO | "saturan" / "saturacion" / "intensidad saturada" (decision capitulo3-r04). "Trunca" queda solo para las rayas que corta $B_{\delta}$. La celda de Chen en la tabla ya no da el rango (guia-8) |
| ES-04 | estilo | APLICADO | "Ramzan et al. acotan tanto la perdida como el muestreo: ..." |
| ES-05 | estilo | APLICADO | Oracion eliminada |
| ES-06 | estilo | APLICADO | GAP de 2.1: "frente a los de Lugmayr et al. y de LeFusion"; GAP de novedad: "la prepublicacion de Wu et al." |
| ES-07 | estilo | APLICADO | "no es insertar metal en miles de casos, que ese protocolo hace en 14 000, sino colocarlo en ellos con una restriccion anatomica"; en las carencias se quito "a escala" |
| ES-08 | estilo | APLICADO | El parrafo se partio: XCIST como fundamento (3 oraciones) e insercion en proyeccion (3 oraciones), este abierto por su funcion |
| ES-09 | estilo | APLICADO | Parrafo propio para las mascaras de lesion, con oracion de funcion y consecuencia (ver guia-5) |
| ES-10 | estilo | APLICADO | Igual que T05 |
| ES-11 | estilo | APLICADO | "gradúan la perforacion cortical, que aqui se llama brecha cortical"; despues solo "brecha cortical" (Herman, tabla, carencias) |
| ES-12 | estilo | APLICADO | Igual que guia-11: se quito la oracion de tolerancias angulares de McLaren (el cap. 3 no las usa); para Ziran se dice su uso: razon para no reproducir una pose canonica (`capitulo3.tex`:79) |
| ES-13 | estilo | APLICADO | "... no pasan de 600 HU, mientras que dos fuentes de MAR segmentan el metal clinico con un umbral de 2500 HU" |
| ES-14 | estilo | APLICADO | "Li et al. usan las ventanas de otro modo: ..." (sin "el otro uso publicado") |
| ES-15 | estilo | APLICADO | "Varias fuentes describen el artefacto fuera del metal sin medir su alcance" y "Otras dos fuentes si publican una distancia"; no se uso "cinco ... del metal" porque Glover estudia hueso |
| ES-16 | estilo | APLICADO | "describe el diseno de esa evaluacion" |
| ES-17 | estilo | APLICADO | "los modelos de sintesis de lesiones que se validan por una segmentacion posterior" (restrictiva, sin recuento) |
| ES-18 | estilo | APLICADO | El parrafo abre con "Las fuentes de este capitulo no provienen de una busqueda sistematica documentada", sin "registros" |
| T01 | traza | APLICADO | Subordinada eliminada ("ese paso se usa en su prueba visual..."). Para cerrar la fila de la ficha `hu2023` ("Cuales son los cuatro pasos") hace falta relectura de la Fig. 3 con `lector-papers`; queda para que la autora la encargue |
| T02 | traza | APLICADO | Zhang y Yu: "el articulo no menciona dispersion ni volumen parcial"; Lin: "adoptan un procedimiento similar con 100 formas de metal y declaran tambien el volumen parcial del metal" |
| T03 | traza | APLICADO | Ruido < 10 % "en las regiones sin artefacto evidente"; "en las regiones con artefacto, la discrepancia del ruido llega hasta el 13.3 % en uno de los experimentos" (ficha, 3.1 p. 6) |
| T04 | traza | APLICADO | "de 7 a 25 % en la mayoria de las superficies medidas. En la orientacion del ala superior de S1 en el plano frontal sacro, el coeficiente sube a 97-140 %" (`tesis/main.tex`:52; ficha `ziran2007fluoroscopic`) |
| T05 | traza | APLICADO | "El metaanalisis advierte que la mayoria de los autores solo usa el termino malposicion cuando hubo una revision del tornillo, y este trabajo lee ese cero como efecto de ese criterio" |
| T06 | traza | APLICADO | "La prepublicacion de Chen et al. sobre autoencoders de video"; sin "de otro grupo" |
| T07 | traza | APLICADO | Igual que guia-3 |
| T08 | traza | APLICADO | "Ramadanov y Zabler" |
| T09 | traza | APLICADO | "lo validan con una varilla de titanio de 12.7 mm y lo demuestran en dos casos de crioablacion" |

## Hallazgos bajos

Aplicados: guia-8 (celda de Chen sin rango de HU), guia-9 (brecha cortical), guia-10 (CatSim con aposicion en su
primera aparicion; "traza metalica" glosada como region del sinograma afectada por el metal, segun
`peters2025hybrid` 2.6; "Stable Diffusion" como "el modelo preentrenado"; "transiliosacras" desaparece con la
oracion de McLaren), guia-11 (= ES-12), ES-19, ES-20, ES-21, ES-22, ES-23 (sin 3071 HU), ES-24, ES-25, ES-26,
ES-27 ("la PSNR"), ES-28, ES-29, ES-30 (sin "por separado"; las oraciones de Xie pasan al parrafo del primer
elemento), ES-31 (sin "clinica" y con "segun tres cirujanos"; no se anadio "en 14 casos": la ficha no liga la
aceptacion a esos 14), ES-32, ES-33, T10, T11 (texto del `\GAPDEC` precisado), T12 (352 en S1), T15 ("Selles",
como en el `.bib`), T16 (celda de Wang 2025), T17 (= guia-4), T18, T19 (cinco modelos con LeFusion, sin
afirmar la metrica de este).

No aplicados: T13 (46 de 129 no da 36.5 %; la ficha `herman2016` no lo anota y se deja la cifra de los autores;
conviene relectura con `lector-papers`), T14 (version de `ramzan2026claim`: es cuestion de ficha y de `refs/raw`,
fuera de los archivos que puedo editar).

## GAP tras la ronda

Lint: lit = 1, dato = 2, dec = 7 (antes 1/2/5). Abiertos en esta ronda: dos `\GAPDEC` replicados del cap. 3 en
el parrafo del Obj 4 de 2.3 (dimension angular de Smith, #11; inversion de las metricas de Peters, #16/#17);
anotados en las filas existentes de `redaccion/MAPA.md`. Ninguno cerrado. Texto del `\GAPDEC` de protocolo de
busqueda precisado (T11). Sin `\GAPLIT` nuevos, asi que `_candidatos.md` no cambia.

## Relecturas sugeridas para la autora (`lector-papers`)

1. `hu2023`, Fig. 3: cuales son los cuatro pasos usados solo en la prueba visual (T01).
2. `herman2016`, Resultados p. 8: 46 de 129 frente a 36.5 % (T13).
3. `ramzan2026claim`, Sec. 3.5: si la distribucion de volumen por segmento AHA compara mascaras sinteticas con
   las clinicas (guia-5).

## Lint

`python scripts/lint_redaccion.py capitulo2 --compilar`: PASA, alta = 0, media = 0, baja = 0; compila, 87 paginas.

## Decisiones de redaccion

1. Resumen unico de como colocan el metal los trabajos de simulacion y MAR: "al azar, con una regla geometrica
   o a mano", y cada modo respaldado en el cuerpo por su fuente.
2. Un "NO ENCONTRADO EN EL PDF" de la ficha se redacta "el articulo no menciona", nunca "no incluye" o "no hace".
3. La perforacion cortical de Zwingmann et al. se introduce una vez con "que aqui se llama brecha cortical";
   despues, solo "brecha cortical" (tambien en tablas).
4. "Traza metalica" se glosa en su primera aparicion como "la region del sinograma afectada por el metal".
5. Resultado de un metodo frente a comparadores sin nombre: "frente a entre X y Y de los N metodos con que se
   comparan", con los valores de la ficha, sin elegir "el mejor".
6. PSNR es femenina ("la PSNR") en todo el documento, como su expansion.
7. Toda celda de la tabla comparativa tiene una oracion de respaldo en el cuerpo del capitulo.
8. Sin "a escala" (calco de *at scale*): se da la cantidad ("en miles de casos, que ese protocolo hace en 14 000").
