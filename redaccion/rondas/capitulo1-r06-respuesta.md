# Respuesta del redactor — capitulo1 — r06

Archivo editado: `overleaf/secciones/capitulo1.tex` (131 -> 134 lineas).
Leidos: `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§1 VIGENTES y §2, incluidas las cuatro filas del
2026-10-05), `redaccion/MAPA.md` (fila 17 y tabla de GAP), los tres informes de r06 y
`capitulo1-r05-respuesta.md`. Fuentes cotejadas de nuevo: `docs/04-implicancias.md` #130 (decidida
2026-10-04), #138 y #141 (ABIERTAS), `tesis/main.tex` (parrafo *Implant geometry source*),
`capitulo2.tex`:96, `capitulo3.tex`:103, :109, :127, :182, :206, :265, :269,
`src/renderizador/difusion.py`, `src/renderizador/datos.py`, `src/renderizador/modelo.py`,
`src/common/ventanas.py`, `experiments/objetivo3/diseno_A.md` §4 y §5,
`docs/literatura/deman2007catsim.md`:79-83, :152.

Lint final: **PASA** (alta=0, media=0, baja=0; GAP lit=4, dato=1, dec=9; documento completo compilado,
111 paginas, 0 errores, 0 citas indefinidas).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 (alta) | guia | APLICADO | §1.3 escribe como hecho lo decidido en #130 (2026-10-04, aplicado a `main.tex`:117): el corredor medido va de la cortical externa de un ilion, cruzando las dos articulaciones sacroiliacas, a la contralateral; el implante que representa es un tornillo transiliaco-transsacro; le aplican las tolerancias angulares de McLaren et al. por ser del mismo corredor. La marca queda reducida a lo unico que #130 no decidio: si el umbral de 10 mm y la holgura radial de Kaiser et al. aplican a ese corredor. |
| guia-2 (alta) | guia | APLICADO | Se retira el "sin embargo". El capitulo afirma ahora que ese tornillo entra y sale por la cortical del ilion y que por eso §SAP excluye los extremos de la trayectoria al calificar la brecha; la remision a `sec:sap` se conserva sin oposicion, y se agrega una a `sec:geometria`. |
| guia-4 (alta) | guia | APLICADO | Se quita "evita asi elegir entre conservar el rango y separar los contrastes". §1.1 dice ahora que la codificacion usa una ventana por canal para separar los contrastes del tejido **sin perder el techo del metal**, y un parrafo propio anade que las tres codificaciones comparten el suelo de $-1000$~HU de su ventana ancha y se diferencian por el techo y por la forma de la compresion. Sin ninguna cifra de #141 (ABIERTA). |
| guia-3 (media) | guia | APLICADO | Primera aparicion en el orden del documento: "\textbf{tornillo transiliaco-transsacro} (transiliosacro)", con tilde, y despues solo la forma acentuada (BITACORA §2, 2026-10-05). Intactas las menciones de `smith2006iliosacral` (dos) y el umbral de 10 mm de `kaiser2014dysmorphism`. |
| guia-5 (media) | guia | APLICADO | El parrafo nuevo cierra con el molde de `capitulo3.tex`:75: ese suelo satura los valores de TC mas bajos del artefacto, y un error de ida y vuelta medido dentro del hueso no muestra si la representacion los conserva, con remision a `sec:amenazas` y `\GAPDEC` sobre el suelo. |
| guia-6 (media) | guia | APLICADO | Fila 3 de `fig:mt-conceptos`: "Tornillo transiliaco-transsacro, con el iliosacro como antecedente, zona segura, corredor oseo, marco de referencia y escala de brecha cortical". |
| guia-7 (media) | guia | APLICADO + ESCALADO | §1.5 presenta la prueba exacta de Fisher, bilateral, sobre tablas de $2\times2$, y dice que con 15 casos por grupo un valor $p$ alto no distingue la ausencia de asociacion de una muestra demasiado pequena para detectarla, de modo que esas comparaciones se leen como sugerentes y no como concluyentes (`sec:amenazas`). El nombre de la prueba sale de #132 (CERRADA), que la registra como "Fisher bilateral". **ESCALADO:** nombrar la prueba en `capitulo3.tex`:265 no es editable desde esta seccion. |
| S01 (alta) | estilo | APLICADO | §1.2 adopta la formulacion del cap. 2: el ancho de $B_{\delta}$ es una convencion de este trabajo, y las dos fuentes revisadas que publican una distancia la miden de un modo que no sirve para calibrar ese ancho. Se retira el negativo "no dan hasta donde llegan las rayas", que `capitulo2.tex`:96 contradice con cifras. |
| S02 (media) | estilo | APLICADO | Mismo cambio que guia-3; se aplico una sola vez, cubriendo tambien M-02 de `paridad-r01-trazabilidad.md`. |
| S03 (media) | estilo | APLICADO | "prevé usar el protocolo fisico como comparacion"; "simulacion fisica" queda solo para la familia de metodos, en la primera oracion del parrafo. |
| S04 (media) | estilo | APLICADO | Los tres comodines de procedencia: "describe la fijacion iliosacra y, con ella, el corredor oseo ..."; "La serie navegada y la serie convencional son los dos grupos de esa comparacion"; "el intervalo del 95 % se obtiene de la distribucion de esas medias". "Salir" queda solo con su sentido fisico o anatomico. |
| S05 (media) | estilo | APLICADO | Resuelto con guia-1 y guia-2: el hecho se escribe, el "sin embargo" se retira y la marca se estrecha al umbral de 10 mm y la holgura radial de Kaiser et al. |
| S06 (media) | estilo | APLICADO con variante | Se agrega la consecuencia pedida, pero sin repetir el sujeto ni la escala de dos oraciones antes (E-R4, PAT-98): "El Objetivo~2 puede comparar sus distribuciones con la referencia clinica porque esa escala es la de perforacion; con una definicion binaria como la de Hinsche et al. no habria grados que comparar". |
| T01 (alta) | traza | APLICADO | Correccion adoptada tal como la propone este informe, que es la mas precisa de las dos sobre `:44`. Se anade el `\GAPDEC{si el suelo de $-1000$~HU de la representacion multiventana se declara como limitacion de alcance o si se cambia la representacion para cubrir los valores de TC mas bajos del artefacto}`, con el mismo texto que `capitulo3.tex`:182, y sin cifras de #141. |
| T02 (media) | traza | APLICADO | El parrafo de la inanicion de fotones cierra con el limite en prosa y sin duplicar la marca (BITACORA §2, 2026-10-03): la representacion satura los valores de TC por debajo de $-1000$~HU, asi que no puede expresar las lecturas de este mecanismo que caigan bajo ese suelo, y la decision sobre ese limite esta pendiente (`sec:sintetizador`). No se afirma que fraccion del artefacto queda fuera, porque esa medida solo consta en #141. |
| T03 (media) | traza | APLICADO | Las dos partes decididas de #130 se escriben como hecho: la geometria (#130.1, #130.2) en el parrafo del tipo de tornillo, y la clausula de #130.3 en el parrafo donde se define la referencia clinica, para no repetir alli el nombre del tipo ni alargar el otro parrafo ("Esa referencia es externa: entra como distribucion de grados y no como evidencia de que el implante de este trabajo sea el mismo"). |
| T04 (media) | traza | APLICADO | Los dos GAP envejecidos pasan al criterio de BITACORA §2 (2026-10-03). Codificacion: "que codificacion multiventana y que precision numerica preinscribe el sintetizador; el codigo de su entrenamiento usa la compresion arcoseno hiperbolico y no hay registro que la congele", y la prosa dice "no esta preinscrita" en vez de "no se ha fijado". 2.5D: "tres en el borrador de su diseno y en el codigo de su entrenamiento, sin preinscripcion", y la prosa atribuye los tres cortes a los dos. Sin cifras de #133 ni de #139. |
| T05 (media) | traza | APLICADO | Comprobado en `src/renderizador/modelo.py` (U-Net de 4 escalas), `difusion.py` (coseno de Nichol y Dhariwal, muestreo DDIM determinista) y `diseno_A.md` §5 (propone U-Net y DDIM, no menciona el calendario). §1.4 dice ahora que el codigo del entrenamiento implementa la U-Net y usa ese muestreo y el calendario coseno, y que ninguno esta preinscrito. No se cita el resultado de ninguna corrida. |
| T06 (media) | traza | APLICADO | Mismo cambio que S01. Se adopta la formulacion del cap. 2 ("la dan y no sirve para calibrar") en lugar del negativo universal; no se repiten en el cap. 1 las cifras de Radzi et al. ni de Cassanego et al., que el cap. 2 ya da con su condicion. |
| T07 (media) | traza | APLICADO | §1.3 ya no afirma el marco como resuelto: "Este trabajo expresa sus poses en ese marco, pero lo ancla al techo de la etiqueta de S1 de la segmentacion automatica. Ese techo puede estar en la cresta sacra media y no en el platillo superior, y esa diferencia no esta medida (`sec:amenazas`)". En prosa y sin duplicar el `\GAPDATO` de `capitulo3.tex`:269. Se conserva la oracion de la localizacion con metal. |

## Hallazgos bajos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-8 | guia | ESCALADO | Titulo de §1.5. Escalado desde r01 y sin resolver: la autora decide si §1.5 se renombra o si "marco" deja de estar reservado al de Kaiser et al. Se deja el titulo como esta y **no** se abre marca, porque el titulo de capitulo que impone la plantilla ("MARCO TEORICO") ya usa la palabra en un tercer sentido y renombrar una u otra cosa excede lo que puede decidir el redactor. |
| guia-9, S08 | guia, estilo | APLICADO | "umbral del cribado por HU con que este trabajo selecciona la cohorte y delimita el metal clinico de sus volumenes" (BITACORA §2, 2026-10-05). |
| S07 | estilo | APLICADO | "Wang et al.~\cite{wang2025adaptiveweighting} y Li et al.~\cite{li2024} segmentan el metal clinico con 2500~HU". |
| S09 | estilo | APLICADO | La negrita de "satura" pasa a su primera aparicion, dentro de la definicion de ventana; la segunda queda en redonda. |
| S10 | estilo | APLICADO | "regiones de medicion" en las dos metricas de Peters et al. que las nombran. |
| S11 | estilo | APLICADO con variante | Se elimina la oracion que repetia el pie de la figura, pero la remision se conserva: `(Figura~\ref{fig:mt-conceptos})` pasa al parrafo de funcion del capitulo, donde dice que de cada concepto se dice en que pieza interviene. Asi el parrafo de orden baja a seis oraciones y la figura no queda sin referencia en el texto. |
| T08 | traza | APLICADO | "El \textbf{sinograma} es el conjunto de lecturas del detector, cada una indexada por la linea que su rayo recorre en el objeto": se retira "vista", que la ficha registra como NO ENCONTRADO EN EL PDF, y se usa la linea con indice que si acredita. |

## Correcciones de borde, no pedidas por ningun revisor

- Las oraciones nuevas de guia-1/T03, T02, T05, T07 y S01 superaban las 40 palabras (E-O1) al escribirlas;
  se partieron antes de cerrar, y por eso el parrafo del tipo de tornillo quedo en dos: el del tornillo
  iliosacro de Smith et al. y el del transiliaco-transsacro de este trabajo (6 oraciones, evita PAT-58).
- `:46` decia "la variante que adopta no se ha fijado" junto a un `\GAPDEC` que ya dice que el codigo usa
  la compresion arcoseno hiperbolico. Se cambio a "no esta preinscrita" para que la prosa no contradiga su
  propia marca (misma familia que T04).
- En §1.5 se evito "umbral" para el nivel de significacion: el capitulo ya lo usa para los umbrales en HU
  y para el de 10 mm (PAT-14).

## GAP abiertos y cerrados

- **Abierto (1, `\GAPDEC`):** suelo de $-1000$~HU de la representacion multiventana, en §1.1. Mismo texto
  que `capitulo3.tex`:182. Registrado en la tabla de `MAPA.md`.
- **Cerrado (0 marcas, 1 pregunta):** el `\GAPDEC` del tipo de tornillo **no desaparece pero pierde dos de
  sus tres partes**, que #130 decidio y ahora se escriben como hecho. Lo que queda preguntado es solo el
  umbral de 10 mm y la holgura radial de Kaiser et al.
- **Reformulados sin cambiar de tipo (4):** codificacion y precision del sintetizador, cortes contiguos
  2.5D (ambos por T04), el `\GAPLIT` de pruebas estadisticas (ahora cubre tambien la prueba exacta de
  Fisher, guia-7) y la prosa de U-Net, muestreo y calendario (T05, sin marca propia).
- **Totales:** 4 `\GAPLIT`, 1 `\GAPDATO`, 9 `\GAPDEC` (antes 8).
- **Ningun `\GAPLIT` nuevo**, asi que no hay candidatos que agregar a `docs/literatura/_candidatos.md`.
  La fuente de la prueba exacta de Fisher entra en el `\GAPLIT` de pruebas estadisticas, que ya figura como
  PENDIENTE en ese archivo.

## Escalado a la autora

1. **Titulo de §1.5** (guia-8, escalado desde r01): "Marco estadistico de la evaluacion" frente a reservar
   "marco" al de Kaiser et al. Sin cambio en el texto.
2. **`capitulo3.tex`:265** (guia-7): el valor $p = 0.109$ se sostiene en una prueba que el cap. 3 no nombra.
   El cap. 1 ya la presenta; falta nombrarla alli, y esa seccion no es editable en esta ronda.
3. **Etiqueta de #130** (observacion de T03 y de #140 punto 2): la entrada sigue rotulada ABIERTA aunque su
   cuerpo registra la decision del 2026-10-04 y los caps. 1 y 3 ya la aplicaron. No se edito
   `docs/04-implicancias.md`.

## Decisiones de redaccion

| Decision | Origen | Alcance |
|---|---|---|
| El nombre del implante de #130 se introduce **aqui**, que es su primera aparicion en el orden del documento: "\textbf{tornillo transiliaco-transsacro} (transiliosacro)" con tilde, y despues la forma acentuada a secas. Esto **deja sin efecto** la fila de BITACORA §2 del 2026-10-03 "En el cap. 1 no se usa transsacro", que era provisional mientras #130 estuviera sin decidir | guia-3, S02, T03 | todo el documento |
| La clausula de #130.3 (la referencia clinica entra como distribucion de grados y no como evidencia de equivalencia geometrica) va **donde se define la referencia clinica**, no donde se define el tipo de tornillo; asi no se repite el nombre del tipo ni crece el parrafo de la geometria | T03 | `introduccion`, `capitulo2`, `capitulo4` cuando nombren la referencia clinica |
| Limite de una representacion propia: se enuncia por lo que la representacion hace ("separa contrastes sin perder el techo del metal"), nunca como ausencia de canje ("evita elegir entre X e Y"), y el extremo que si eligio se declara con su `\GAPDEC` en la seccion que lo define | guia-4, T01 | toda seccion que describa la codificacion multiventana |
| Mecanismo fisico que la representacion no puede expresar: se declara en el parrafo que define el mecanismo, en prosa y con remision a la marca, sin duplicarla y sin citar la magnitud de una implicancia ABIERTA | T02 | `capitulo2` §Representacion multiventana, `capitulo4` |
| GAP envejecido por una corrida posterior: "el codigo de su entrenamiento usa X y no hay registro que lo congele" o "..., sin preinscripcion"; nunca "no se ha fijado" ni "solo lo propone el borrador" cuando el codigo ya lo fija. La prosa vecina se revisa para que no contradiga la marca | T04, T05 | `introduccion` §Alcance, `capitulo2` §Comparacion critica, `capitulo3` |
| Negativo sobre una magnitud que la literatura si publica: se dice que la publican y que no sirve para calibrar, con la formulacion del cap. 2; las cifras se dan una sola vez, en el capitulo que las discute | S01, T06 | todo el documento |
| "Protocolo fisico" para el brazo de comparacion; "simulacion fisica" solo para la familia de metodos, y no las dos cosas en un mismo parrafo sin distinguirlas | S03 | todo el documento |
| El verbo "salir" queda reservado a su sentido fisico o anatomico; la procedencia de un concepto, de un grupo o de un intervalo se dice con el verbo que corresponde ("con ella", "son los dos grupos de", "se obtiene de") | S04 | todo el documento |
| Las regiones en que se mide la *streak amplitude* se llaman "regiones de medicion", para no competir con la region de generacion $G$ | S10 | `capitulo3` §Apariencia, `capitulo4` |
| La prueba de las tablas $2\times2$ se nombra "prueba exacta de Fisher, bilateral" (forma de #132), y el nivel de significacion no se llama "umbral", palabra ya tomada por los umbrales en HU y por el de 10 mm | guia-7 | `capitulo3` §Amenazas, `capitulo4` |
| Una oracion de remision a una figura no repite su pie; si es la unica referencia a la figura, la remision se traslada entre parentesis a la oracion cuyo contenido la figura resume | S11 | todo el documento |
