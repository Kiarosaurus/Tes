# Respuesta del redactor — capitulo3 — r06

Archivo editado: `overleaf/secciones/capitulo3.tex`. Edicion mecanica de un encabezado en
`overleaf/secciones/capitulo4.tex` (decision de la autora, 2026-10-05). Tabla de GAP de
`redaccion/MAPA.md` actualizada. Sin `\GAPLIT` nuevos, asi que no se toca
`docs/literatura/_candidatos.md`.

Lint final: `python scripts/lint_redaccion.py capitulo3 --compilar` -> **PASA**, alta=0 media=0
baja=4, 110 paginas, 0 errores de LaTeX y 0 citas indefinidas. Las cuatro bajas son las mismas
cuatro `E-P1` conservadas con motivo desde r04 (`:73`, `:190`, `:208`, `:267`): las cifras de esas
lineas estan definidas y citadas en el parrafo o la ecuacion inmediatamente anterior, y meter una
cita o un `\ref` redundante solo para apagar el lint seria esquivarlo. Se dejan y se declara.

Cifras usadas en esta ronda, todas de la lista autorizada por la autora (2026-10-05) y verificadas
contra su fuente: 20 de 30 (67 %) mas un dudoso aparte y 10 de 15 frente a 10 de 15 (#136, tabla de
verificacion del 2026-10-05); 7 de 15 frente a 2 de 15 con p = 0.109 (#132 §5; `tesis/main.tex`:109);
15 de 72 corredores estrechos (`experiments/objetivo2/e13b_estratificado.md`:9; `tesis/main.tex`:109);
16 de 16 con 14 `ok`, 2 `fallo_ambos`, 0 `fallo_6mm` (#131 §1); 61 de 61 (#124; `tesis/main.tex`:121);
0 de 72 casos que cambian con el relleno de la envolvente (#131 §2).

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | §Validez externa reescrita y reordenada: la referencia clinica viene de pelvis fracturadas, *que es la poblacion en la que el procedimiento se practica*; Reilly et al. queda como mecanismo de estrechamiento de esa serie; luego, que la anatomia receptora **tampoco** esta libre de fractura (20 de los 30 casos cribados, remision a §Datos), lo que la **acerca** a esa poblacion; y por ultimo lo que no puede afirmarse: que esten emparejadas, porque la fractura es incidental, no graduada ni clasificada por especialista y con estado de reduccion desconocido. La mencion de `reilly2003effect` conserva "tornillos iliosacros" |
| guia-2 | guia | APLICADO | §Validez interna: fuera "La ausencia de fractura en esa cohorte no se verifico" y "Al menos un paciente ...". Entra el cribado con grupo de comparacion en parrafo propio: 10 de 15 frente a 10 de 15 (no explica el estrechamiento) y fractura sacra desplazada 7 de 15 frente a 2 de 15 con $p = 0.109$, declarada **sugerente y no concluyente** con n = 15 por grupo, y la fraccion no cuantificable |
| guia-3 | guia | APLICADO | Eliminado el `\GAPDATO` de §Datos. El resultado se escribe en la caracterizacion de la cohorte, en parrafo propio, con el nivel de lectura declarado (medico recien egresado y sin especialidad, sobre laminas fijas, sin conocer el grupo) y la consecuencia: la cohorte receptora no es una coleccion de pelvis sanas y ninguna cifra del corredor depende de ello. Fila quitada de `MAPA.md` (ver nota 1) |
| guia-4 | guia | APLICADO | §SAP: "el grado~0 es inalcanzable por la anatomia receptora **tal como se presenta**, no por la colocacion", mas "Que estrecha esos corredores no esta establecido", el 7 de 15 con su matiz y "una fraccion no cuantificable del estrechamiento puede ser patologia y no variabilidad anatomica normal". La cifra de #122 no se toca: se escribe **15 de los 72** (ver nota 2) |
| guia-5 | guia | APLICADO | §Corredor: cerrado el `\GAPDATO`. Texto: la revision se hizo sobre laminas, **por la autora con apoyo de un medico egresado y sin especialidad**, y cubrio los 16 casos; 14 conformes, 2 fallaron con los dos recortes, ninguno solo con el de 6~mm, que es el unico veredicto que habria reabierto la decision; el recorte por defecto se mantiene "con la condicion evaluada y no solo declarada". Los dos fallos quedan en `\GAPDEC` (bloque B7, bloqueado) |
| guia-6 | guia | APLICADO | §Marco con metal: cerrado el `\GAPDEC` con la frase de `main.tex`:121 traducida: acuerdo **61 de 61** y, en la misma oracion, los dos limites. Nombrada la **cresta sacra media** como la estructura aceptada como S1 por detras del cuerpo vertebral en 12 de los 16 casos de la revision del recorte, y declarado que `vertebrae_S1` la contiene por diseno al etiquetar la vertebra completa. **No** se afirma nada sobre si el nivel esta bien o mal determinado (#138 ABIERTA) |
| guia-7 | guia | APLICADO | §Amenazas, validez de constructo: el marco se define perpendicular al platillo superior, el control de nivel y las medidas usan el techo de la etiqueta, "las dos superficies pueden no coincidir, y esa diferencia no esta medida", con `\GAPDATO` nuevo. Redactado como amenaza identificada, no como defecto demostrado |
| guia-8 | guia | APLICADO | §Poses: "una segunda lectura de la autora, ciega a la profundidad medida" |
| guia-9 | guia | APLICADO | Traducida la primera frase de *Implant geometry source* de `main.tex`:117 en §Geometria (trayectoria de cortical externa a cortical externa cruzando **las dos** articulaciones sacroiliacas; implante **transiliaco-transsacro**; tolerancias de `mclaren2021corridor` aplicables por ser del mismo corredor). Cambiadas tambien `:9` ("un tornillo transiliaco-transsacro (transiliosacro)"), `:101` (dos menciones) y `:196`. **Sin sustituir a ciegas:** siguen diciendo "iliosacro" `reilly2003effect` en validez externa, `kaiser2014dysmorphism` con su corredor de 10~mm y "corredor iliosacro" en el traslado de la escala de `smith2006iliosacral`, que es el objeto que esos autores describen |
| guia-10 | guia | APLICADO (en la forma que fijo la autora) | Titulo `\section{Evaluación de la representación multiventana}` con el mismo `\label{sec:obj1}`, y `:13` "El Objetivo~1 **evalua** si". **No** se adoptaron ni el titulo propuesto por el revisor ("Compuerta de representacion: evaluacion del autoencoder") ni "determina si": la autora fijo las dos formas el 2026-10-05, y "evalua" es la que ya usa la introduccion. Mismo encabezado corregido en `capitulo4.tex`:5, por orden expresa de la autora, para no dejar dos nombres del mismo objetivo en el documento |
| guia-11 | guia | APLICADO | §Vision general: el `\GAPDATO` pasa a decir que **la cadena completa** (muestrear la pose en S1, rasterizar $M$, generar la apariencia sobre una pelvis sin osteosintesis) **no se ha ejecutado nunca**, de modo que no existe resultado del Objetivo~3. Sin ninguna cifra ni afirmacion de #133 ni de #139. La saturacion con 47 pacientes (B1) y el numero de pasos (B2) no se redactan |
| guia-12 | guia | APLICADO en parte | "Cribado" queda siempre calificado y nunca designa dos cosas sin marca: **cribado por HU** (umbral de 2500~HU) y **cribado ciego de fractura**, que es el nombre que el propio revisor reserva para el segundo. En `:97` la identificacion de los 17 casos se atribuye al **censo morfologico del metal**, con `\ref` a §Geometria, y ese censo se nombra en negrita en §Geometria, donde ya estaba su caveat: "no afirma que los componentes sean tornillos transiliaco-transsacros, sino que son candidatos por su forma". Asi desaparece la contradiccion con `:119`. **No** se renombro la revision tridimensional de tipo y cantidad: `:46` ya la nombra por lo que es y no usa la palabra "cribado" para ella |
| S01 | estilo | APLICADO | Mismo defecto que guia-10, resuelto con la decision de la autora. Ver guia-10 |
| S02 | estilo | APLICADO | "Referencia" vuelve a quedar reservada a la **referencia clinica**: `:44` "las observaciones reales de artefacto, cuya reconstruccion es desconocida, se usan para comparar la apariencia y no como verdad fisica"; `:54` "de comparacion de apariencia"; `:219` "es el brazo que aporta el mecanismo, porque es el unico de los tres que simula la fisica de formacion del artefacto"; `:231` "su comparacion"; encabezado de `tab:diseno` "**Comparacion**" |
| S03 | estilo | APLICADO | Variadas las dos aperturas de la serie: "Para la comparabilidad con el protocolo fisico se usan dos pruebas unilaterales ..." y "Fuera de la banda, el RMSE y el indice de similitud estructural (SSIM, ...) contra la TC original comprueban la preservacion ..." |
| S04 | estilo | APLICADO | Soltado el molde en `:160`: "La semilla se deriva del identificador de cada caso."; el contraste con el generador pasa a la oracion siguiente ("con un generador que avanzara de caso en caso"). `:166` y `:168` se dejan, como propone el propio hallazgo |
| S05 | estilo | APLICADO | §Sintetizador: "Ninguna de las fuentes revisadas da un valor para el ancho. Karageorgos et al. si dan el sentido del error en su propio dominio: ...". La lectura deja de atribuirse a "las fuentes revisadas" |
| S06 | estilo | APLICADO | Parrafo del corredor partido: el primero queda con la razon de usar mascaras y el 0.42 (con `\ref` a §Compuerta por el umbral de 150~HU del protocolo adoptado); el segundo, con TotalSegmentator, los dos recortes, la limpieza y la salvedad de exactitud de S1 |
| S07 | estilo | APLICADO | "La convencion propia **fija** ese margen **en** dos desviaciones estandar" (`:158`) y "$h$ **coincide con** el radio del corredor de 10~mm de Kaiser et al." (`:83`) |
| T01 | traza | APLICADO | Mismo hallazgo que guia-11, con su texto. Fila de #116 reescrita en `MAPA.md` (ver nota 3) |
| T02 | traza | APLICADO | §Corredor: primero el hecho de #131 §2 (CERRADA) —aplicar el relleno de cavidades cerradas no cambia el diametro en ninguno de los 72 pacientes de la cohorte— y el `\GAPDEC` queda solo para corregir la decision. La salvedad de que `outputs/e14_relleno.csv` no esta en disco y que esas cifras solo constan en #131 va a `MAPA.md`, no al texto |
| T03 | traza | APLICADO | `\GAPDATO` del decodificador reescrito con el criterio de BITACORA §2 (2026-10-03): la perdida L1 y AdamW **constan en el codigo del experimento**, y el resto solo como valores por omision de ese codigo, no en un registro |
| T04 | traza | APLICADO | El `\GAPDEC` unico se parte en dos: "Para el primero falta la metrica" (mascara umbralizada frente a cilindro liso) y, para el segundo, "el salto de los valores de TC al cruzar el borde de la banda ya se midio una vez, sobre un caso, un corte y un modelo sin converger", con `\GAPDEC` de preinscripcion del bloque. **Sin escribir 203 ni 30~HU** |
| T05 | traza | APLICADO | En §Datos el control de nivel dice ahora que compara el techo de la mascara de S1, "etiqueta de vertebra completa que incluye el arco posterior", con el punto del platillo superior de la localizacion automatica. La amenaza y su `\GAPDATO` van en validez de constructo (ver guia-7) |
| T06 | traza | APLICADO | §Apariencia: "Toda la evaluacion del Objetivo~3 es metrica, a diferencia de la del Objetivo~2, que incorpora lecturas humanas del nivel vertebral y del corredor", con `\GAPDEC` nuevo de #137. No se elige ninguna de las dos opciones de la implicancia |

## Hallazgos de severidad baja

Aplicados los nueve, por baratos y sin conflicto: **guia-13** y la parte de `:219` de S02 (formulas
"para comparar la apariencia" / "como comparacion"; "marco de referencia" y "referencias
anatomicas" quedan, que no entran en la restriccion); **S08** (las dos cercanias al fuste de
4.8~mm se funden en una oracion y la cabeza abre parrafo, pero la fusion se reparte en dos
oraciones para no pasar de 40 palabras, E-O1); **S09** (verbo preciso en las seis procedencias:
"resulta de", "se toma de", "procede de", "se forman con" en `:50` y `:178`, "se toma de la
referencia clinica"); **S10** (26 y 35 tornillos con remision a §SAP); **S11**, resuelto con la
redaccion de guia-12, que es mas precisa que "cribado por HU" porque los 17 casos salen del censo
morfologico y no del umbral solo; **S12** (la resolucion de 0.083~mm se queda en §SAP y validez de
constructo remite a ella sin perder la condicion del fantoma); **T07** ("Con el recorte por
defecto, el diametro ... mediana de 9.5~mm"); **T08** ("Selles et al.", como el `.bib` y
`capitulo1.tex`:50); **T09** ("la imagen entera" en las dos apariciones reales de la frase, §
Apariencia y validez de constructo; `:257` no contiene esa expresion, asi que la correccion se
aplico donde si estaba).

Ninguno RECHAZADO y ninguno ESCALADO: los dos puntos que habrian sido escalables en esta ronda
—el titulo de `sec:obj1` y la regla del `dudoso`— llegaron con decision de la autora del 2026-10-05.

## GAP cerrados, abiertos y por que

**Cerrados (3).**

1. `\GAPDATO` del cribado ciego de fractura (#125, cerrada por #132): el cribado existe, esta
   cerrado y verificado contra el CSV; el GAP afirmaba lo contrario.
2. `\GAPDATO` de la revision de los 16 casos del recorte (#123, cerrada por #131): 16 de 16
   revisados y la condicion de reapertura evaluada.
3. `\GAPDEC` del acuerdo 61 de 61 (#124, decision (b) tomada y aplicada a `main.tex`).

**Abiertos (5).**

1. `\GAPDATO` de la diferencia en milimetros entre el techo de la etiqueta de S1 y el platillo
   superior (#138 ABIERTA dice literal "Eso no esta medido"): es el supuesto que sostiene el marco
   de referencia y no estaba declarado en ninguna parte.
2. `\GAPDEC` del tratamiento de los dos casos con error de segmentacion (`CLINIC_0022`,
   `CLINIC_0024`): bloque B7, bloqueado.
3. `\GAPDEC` de si el Objetivo~3 se evalua solo con metricas o lleva una lectura humana (#137
   ABIERTA, que declara que "el silencio no" es legitimo).
4. `\GAPDEC` de la continuidad de los valores de TC en el borde de la banda, que nace de partir en
   dos el `\GAPDEC` unico de los desplazamientos de dominio (T04): los dos no estan en el mismo
   estado, y el GAP unico daba por no medido lo que ya se midio una vez.
5. `\GAPDEC` de si el suelo de $-1000$~HU de la representacion multiventana se declara como
   limitacion de alcance o se cambia la representacion, por el aviso de #141 (ABIERTA). Esta en
   §Sintetizador, donde el capitulo adopta esa codificacion para las entradas y salidas, y
   **sin ninguna cifra de #141**: el texto solo dice que la codificacion acota por abajo los
   valores representables porque su ventana ancha empieza en $-1000$~HU, que es lo que ya declara
   §Compuerta sobre la codificacion de arcoseno hiperbolico.

Sobre #141 y el aviso del orquestador: el capitulo **no** afirmaba ni insinuaba que la codificacion
multiventana conserve el rango de HU del artefacto —lo mas cercano era la descripcion del rango
$[-1000, 20\,000]$~HU en §Compuerta y el `\GAPDEC` de congelar la preinscripcion—, pero adoptaba la
codificacion para el sintetizador sin decir que acota por abajo. Se anadio una oracion y el
`\GAPDEC` para no cerrar la puerta.

Balance de marcas del capitulo: 0 `\GAPLIT`, 9 `\GAPDATO` (eran 10) y 25 `\GAPDEC` (eran 22).

## Decisiones de redaccion

Para la bitacora. Las cuatro deberian aplicarse igual en las otras secciones.

1. **Nombre del implante (de #130, decidido por la autora).** Primera aparicion:
   "tornillo transiliaco-transsacro (transiliosacro)"; despues, "tornillo
   transiliaco-transsacro". En el documento se escribe con tilde, **transilíaco-transsacro**, por
   coherencia con "crestas ilíacas", "espinas ilíacas" y "articulaciones sacroilíacas", que el
   capitulo ya acentua. `capitulo1.tex`:72 usa hoy solo "transiliosacro": al corregir esa seccion
   conviene alinearla con esta forma. **No se sustituye** donde la mencion describe lo que hizo
   otra fuente (`reilly2003effect`, `kaiser2014dysmorphism` y su umbral de 10~mm,
   `smith2006iliosacral`).
2. **Nivel de un lector no especialista: se describe, no se sigla.** Se escribe "un medico recien
   egresado y sin especialidad" y no "SERUM": la expansion de esa sigla **no consta en ninguna
   fuente del repositorio** (solo aparece abreviada en #131, #132 y #136), y definirla en el
   documento seria completarla con conocimiento propio. El limite que la autora exige —cribado
   valido, no lectura de especialista— se escribe entero y en la misma oracion que la cifra.
3. **"Cribado" va siempre calificado.** "Cribado por HU" para el umbral de 2500~HU, "cribado ciego
   de fractura" para el de #132, y **"censo morfologico del metal"** para el filtro geometrico de
   E8/E11 del que salen los 17 casos y los 79 componentes. Ningun procedimiento se nombra "el
   cribado" a secas.
4. **Cifra con riesgo de colision: se da en recuento y no en porcentaje.** Los corredores estrechos
   se escriben "**15 de los 72** pacientes de la cohorte primaria" y no "20.8 %", porque el mismo
   capitulo usa 20.8 % para la viabilidad del criterio $D \geq d + 2\epsilon$ con el recorte
   alternativo, y dos 20.8 % distintos a cuatro parrafos de distancia se leen como el mismo dato.

## Notas sobre `redaccion/MAPA.md`

1. **Las filas de guia-3, guia-5 y guia-6 no se borraron: se marcaron cerradas con el sitio que
   sigue abierto.** Las dos primeras cubren ademas `introduccion` §Alcance, que esta fuera de mi
   seccion y **sigue** con el GAP (A-04 y A-06 de la auditoria de paridad). Borrar la fila entera
   habria hecho desaparecer del mapa un GAP vivo en otro archivo, que es justo el fallo de #135.
   La fila de #124 si queda cerrada sin pendiente: `capitulo3` era su unico sitio.
2. La cifra "15 de 72" quedo anotada con su fuente buena (`e13b_estratificado.md`:9 y
   `main.tex`:109), no con el encabezado de #122, que trae 16 y 22 % (A-07).
3. La fila de #116 pasa a decir que lo que falta es la **cadena completa**, y deja anotado que
   `introduccion` §Alcance y `capitulo2` §Comparacion critica y brecha siguen diciendo "nunca
   genero una muestra" y hay que corregirlos con el mismo criterio.
