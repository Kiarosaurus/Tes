# Auditoria de paridad `tesis/main.tex` -> `overleaf/` — BLOQUE 0 del ENCARGO 2026-10-04 — r01

> Alcance ejecutado: **todas** las entradas marcadas CERRADA en `docs/04-implicancias.md`
> (36 entradas, listadas abajo), mas `#130`, que su encabezado llama ABIERTA pero cuyo cuerpo
> contiene decision de la autora y aplicacion a `tesis/main.tex` (ver hallazgo M-04).
> Dos comprobaciones por entrada: **paridad** (esta en `overleaf/secciones/`?) y **cifra**
> (cuadra con `experiments/`, `docs/literatura/` o `tesis/main.tex`?).
> No se edito ningun `.tex`, ni `01-decisiones.md`, ni `04-implicancias.md`.
>
> **Metodo de recuento.** No hubo herramienta de shell disponible en esta sesion: los CSV se
> leyeron integros con la herramienta de lectura y se contaron fila por fila. Cada recuento
> declara abajo el criterio exacto, el cruce de archivos y el resultado, de modo que sea
> reproducible con `pandas` o con `Group-Object` sin volver a abrir nada.

## Las dos pruebas de control pasan

- **#135 detectada** (fila #132, hallazgo A-01): `overleaf/secciones/capitulo3.tex:263` afirma
  todavia lo contrario de #132. Y **ademas de la linea que #135 nombra, hay tres sitios mas**
  con el mismo defecto: `capitulo3.tex:253`, `capitulo3.tex:52` e `introduccion.tex:82`.
- **#136 detectada y ampliada** (hallazgo A-08): el recuento propio da **20 de 30 (67%)** con
  `fractura = si`, **10 frente a 10** por grupo. Pero el aviso de #136 **dejo sin marcar una
  tercera cifra falsa** de #132: la seccion 4 dice *"21 casos con `fractura = si` (14 sacro,
  7 ilion)"*; el recuento da **20 (14 sacro, 6 ilion)**.

---

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| A-01 | alta | G-T4, OC-3 | `overleaf/secciones/capitulo3.tex:263` | "las pelvis receptoras, sin fractura conocida, no reproducen" | #132 CERRADA; `r3_fractura_revisor.csv` | Patron #135: afirmacion FALSA en el documento de entrega. El cribado hallo fractura en 20 de 30 | Reescribir el cierre con el texto del bloque A1: 20 de 30 (67%) con fractura confirmada mas un caso dudoso, lector sin especialidad, y el argumento reordenado (acerca, no aleja) |
| A-02 | alta | G-T4, OC-3 | `overleaf/secciones/capitulo3.tex:253` | "Al menos un paciente ... tiene una fractura confirmada" | #132 CERRADA (cierra #125) | Estado pre-#132 (era la redaccion de #125). "Al menos un paciente" es ahora 20 de 30 | Sustituir por la cifra del cribado ciego con grupo de comparacion: 10 de 15 estrechos frente a 10 de 15 controles, identicos, y 7/15 frente a 2/15 en sacra desplazada (p = 0.109, sugerente no concluyente) |
| A-03 | alta | OC-2, G-T4 | `overleaf/secciones/capitulo3.tex:52` | `\GAPDATO{cribado ... preparado y no realizado}` | `r3_fractura_revisor.csv` (30/30 lleno) | GAP injustificado **que afirma algo falso**: el cribado SI se realizo y esta cerrado en #132 | Eliminar el `\GAPDATO` y escribir el resultado. Quitar la fila correspondiente de la tabla de GAP de `redaccion/MAPA.md:33` |
| A-04 | alta | OC-3, G-T4 | `overleaf/secciones/introduccion.tex:82` | "las pelvis receptoras no reproducen" + mismo `\GAPDATO` falso | #132 CERRADA | Tercera y cuarta repeticion del defecto de #135, en el bloque (a) | Mismo tratamiento que A-01 y A-03, en version resumida de §Alcance |
| A-05 | alta | OC-3, G-T4 | `overleaf/secciones/capitulo3.tex:209`, `:253`, `introduccion.tex:82` | "el grado 0 es inalcanzable por anatomia" | #132 §5, que **retira** esa redaccion de #122 | #132 dice literal: *"esa redaccion ya no se sostiene tal cual"*; 7 de 15 estrechos tienen fractura sacra desplazada. El texto presenta como anatomia lo retirado | Escribir "inalcanzable por la anatomia receptora **tal como se presenta**" y anadir que una fraccion **no cuantificable** puede ser patologia y no variabilidad normal. #122 no se toca en su cifra; solo su atribucion causal |
| A-06 | alta | OC-2, G-T4 | `overleaf/secciones/capitulo3.tex:91`, `introduccion.tex:84` | `\GAPDATO{revision de la autora de los 16 casos}`; "una revision que no se hizo" | #123 y #131 CERRADAS; `e9ts_revision_laminas_autora.csv` | GAP injustificado: la revision esta hecha, 16 de 16, y el recorte de 6 mm se mantiene con la condicion **evaluada** | Eliminar los dos `\GAPDATO` y escribir: 16 de 16 revisados, **14 `ok`, 2 `fallo_ambos`, 0 `fallo_6mm`**; los dos fallos son errores de segmentacion (`CLINIC_0022`, `CLINIC_0024`) y no de recorte. Revisor: **la autora con apoyo de un medico egresado (SERUM, sin especialidad)** |
| A-07 | alta | G-T4 | `docs/04-implicancias.md:8490` y `:8503` (encabezado y cuerpo de #122) | "En **16 de 72** pelvis"; "**22% de la cohorte (16/72)**" | `e13b_estratificado.md:9`; `tesis/main.tex:109` | **CIFRA NO CUADRA dentro de una CERRADA**, mismo tipo que #136. El propio cuerpo de #122 explica que los 16 eran un control mal especificado y que los estrechos reales son **15**; la fuente dice 15 y 57, y `main.tex` dice "15 of the 72" | La cifra citable es **15 de 72 (20.8%)**. No escribir 16 ni 22% en `overleaf/`. Conviene que la autora corrija el encabezado de #122 (yo no edito ese archivo) |
| A-08 | alta | G-T4 | `docs/04-implicancias.md:9075` (#132 §4) | "`donde` ... lleno en los **21** casos con `fractura = si` (14 sacro, **7 ilion**)" | `r3_fractura_revisor.csv` | **Tercera cifra falsa de #132, que el aviso de #136 no marco.** El recuento da 20 con `si`: 14 sacro y **6** ilion. Y si se contara el `dudoso` para llegar a 21, su columna `donde` esta **vacia**, con lo que la frase "no tiene huecos" se cae por los dos lados | No citar 21 ni "7 ilion". Las cifras citables son 20, 14 sacro, 6 ilion. Pedir a la autora que extienda el aviso de #136 a esta seccion |
| A-09 | alta | OC-3, G-T4 | `overleaf/secciones/introduccion.tex:13`, `:15`, `:21` | "síntesis condicionada bidimensional"; "se evaluará ... Dice (DSC) y HD95" | `docs/00-tesis.md` *Fuera de alcance* pto 1; `CLAUDE.md` raiz; `main.tex` *Why downstream evaluation is excluded* | **Contenido retirado presentado como vigente y como objetivo**: evaluacion downstream de segmentacion y sintesis 2D. El `\GAPDEC` de la linea 28 avisa, pero las tres frases siguen **afirmandolo** | Reescribir las tres frases con el alcance vigente (coherencia fisica y quirurgica; Dice/HD95 fuera de alcance, como ya hace `capitulo3.tex:36`). Ya registrado como #126, pero el texto afirmativo no puede quedarse mientras se decide |
| M-01 | media | OC-2, G-T4 | `overleaf/secciones/capitulo3.tex:97` | `\GAPDEC{si se declara la segunda lectura ... 61 de 61}` | #124 CERRADA 2026-10-04, opcion (b) | GAP injustificado: la decision **ya esta tomada** (opcion b) y aplicada a `main.tex:121`. `redaccion/MAPA.md:34` tambien lo da por abierto | Cerrar el `\GAPDEC` con la frase de `main.tex:121`: acuerdo **61 de 61**, con los dos limites obligatorios en la misma oracion (el segundo lector es **la autora, no un segundo clinico**; **solo los juicios de nivel** son independientes, porque las notas se copiaron tras ver la coincidencia) |
| M-02 | media | G-T4 | `overleaf/secciones/introduccion.tex:39`; `capitulo3.tex:101`, `:196`; `capitulo1.tex:72` (`\GAPDEC`) | "tornillo iliosacro, que une el ilion con el sacro" | #130, decidida 2026-10-04 y aplicada a `main.tex:117` | Decision tomada y no propagada. El corredor medido va de cortical externa de un ilion a la contralateral cruzando **ambas** articulaciones: es **transiliaco-transsacro** | Traducir la primera frase de *Implant geometry source* de `main.tex:117`. **No sustituir a ciegas:** deben seguir diciendo "iliosacro" las menciones de `smith2006iliosacral` (capitulo1.tex:72, 82), `kaiser2014dysmorphism` y su umbral de 10 mm, `reilly2003effect` (capitulo3.tex:263) y `liu2025pipeline` (capitulo2.tex:50, 54, 72; anexos.tex:25) |
| M-03 | media | G-T4 | `redaccion/ENCARGO_2026-10-04.md:99-109` (bloque A3) | "**#124** — Herman et al. es referencia de distribucion" | `docs/04-implicancias.md:8639` (#124) y `:8899` (#130 pto 3) | **El encargo cita la implicancia equivocada.** #124 es "61 de 61 del nivel S1" (`MAPA.md:34` lo confirma). El contenido de A3 es **#130 punto 3**, y #130 figura como **ABIERTA** en su encabezado. El *contenido* si tiene respaldo: `main.tex:52` lo trae aplicado y la ficha `herman2016.md:167` acredita los dos tipos (*"trans-sacro 38.2% vs iliosacro 30.3%"*) | Al redactar A3, citar **#130** como fuente, no #124, y escribir solo lo que la ficha sostiene: Herman mide **distribucion de grados**, su serie mezcla los dos tipos y no reporta longitud ni punto final de cada tornillo. Destino: `capitulo2.tex:74` |
| M-04 | media | G-T4 | `docs/04-implicancias.md:4514` y `:5627` frente a `:6110-6111` | #55 y #62 aparecen ABIERTAS en su encabezado y "CERRADA" en la tabla resumen de la ronda 2026-09-17 | el propio archivo | **Dos fuentes del mismo archivo discrepan en el estado.** Un redactor que lea el encabezado las trata como GAP; uno que lea la tabla, como hecho. Mismo problema de etiqueta en **#130** | Que la autora unifique la etiqueta. Mientras no lo haga: el contenido de ambas **ya esta propagado** y correctamente matizado (`capitulo3.tex:85` para #55; `capitulo2.tex:62` para #62), asi que no hace falta tocar `overleaf/` por esto |
| M-05 | media | G-T4 | `docs/04-implicancias.md:9121-9125` (#132, tabla de `D_TS` por estado) | "Sin fractura \| **10** \| `D_TS` mediana **6.7 mm**" | `r3_fractura_revisor.csv` + `r3_fractura_grupos.csv` | Esa fila cuenta el `dudoso` **dentro** de "sin fractura", justo lo contrario de lo que hace la fila de "fractura cualquiera" que #136 corrigio. Bajo la regla autorizada (`dudoso` se reporta **aparte**) son **n = 9** y mediana **5.9 mm** | No citar esa tabla sin recalcularla. Si entra, decir n = 9 y 5.9 mm, y el caso dudoso aparte. Ademas la tabla **no es comparacion limpia** (el muestreo fue estratificado por `D_TS`), como #132 ya advierte |
| M-06 | media | G-T4, P-MM3 | `overleaf/secciones/capitulo3.tex:164` | "un segundo lector ciego a la profundidad medida" | `r2_nivel_pico_revisor.csv`, columna `revisor` = `autora` (18 filas) | No identifica al lector. #124 fija el estandar: cuando el segundo lector es la autora, hay que decirlo; no hacerlo deja al lector suponer un clinico | "una segunda lectura de la autora, ciega a la profundidad medida". Mismo criterio que la frase de `main.tex:121` |
| M-07 | media | G-T4, P-MM3 | `overleaf/secciones/capitulo3.tex:91`; `introduccion.tex:84` | "revision de la autora de los 16 casos" | `e9ts_revision_laminas_autora.csv`, columna `revisor`; #131 | Procedencia incompleta. #131 la corrigio el 2026-10-04: el juicio **no es solo de la autora** | Al escribir A-06, atribuirla a "la autora con apoyo de un medico egresado (SERUM, sin especialidad)". El sufijo `_autora` del archivo se conserva por compatibilidad y no acredita autoria unica |
| M-08 | media | OC-5 | `overleaf/secciones/capitulo4.tex` (4 secciones vacias) | — | `e13_sap.md`, `e13b_estratificado.md`, `e9ts_resumen.md` | **Ninguna cifra de resultado del Objetivo 2 esta en `overleaf/`**: los seis Wasserstein-1, las cuatro distribuciones de grado y el 15/57 viven solo en `main.tex:109` y en `experiments/`. No es un fallo de #122 ni de #121: es que el capitulo no se ha redactado | Fuera del bloque A. Dejar constancia para que, cuando se redacte el cap. 4, la fuente sean `e13_sap.md` y `e13b_estratificado.md` y **no** el encabezado de #122 (ver A-07) |
| B-01 | baja | G-T4, E-R6 | `docs/04-implicancias.md:9123` (#132) | "Fractura desplazada \| 12 \| **6.2 mm**" | recuento propio sobre los dos CSV | La mediana de los 12 valores es **6.25 mm** (media de 6.2 y 6.3). Se publica 6.2 sin declarar el redondeo | Si la cifra entra, escribir 6.25 mm o declarar el criterio de redondeo. La de "no desplazada" (10.4 mm) **si** es exacta |
| B-02 | baja | G-T4 | `overleaf/secciones/capitulo2.tex:66` | "el 36.5 % de los tornillos en S1 y el 14.8 % en el segundo segmento" | `docs/literatura/herman2016.md:68`, `:127` | Falta el `n`. La ficha da los denominadores: **46/129 en S1 y 4/27 en S2** | Anadir los denominadores; con 4 de 27 el lector pondera solo el `p = 0.035` |
| B-03 | baja | G-T4 | `docs/04-implicancias.md:8962` (#131 §3) | cita literal: "se reconoce parte de la **medula** ... como parte de S1" (12 de 16) | `e9ts_revision_laminas_autora.csv` | La cita literal **ya no existe en la fuente**: el CSV dice hoy "cresta sacra media" (la autora corrigio la nomenclatura el 2026-10-04). El original esta en `e9ts_revision_laminas_autora.raw.csv`. El recuento de 12 **si** se sostiene | Si la nota se cita, citarla del `.raw.csv` y decir que el termino se corrigio. Nada que cambiar en `overleaf/` |

---

## Inventario: una fila por implicancia CERRADA

| # | Que ordena (una linea) | Estado paridad | `overleaf/` (archivo:linea) | Estado cifra | Evidencia del recuento |
|---|---|---|---|---|---|
| 1 | `wang2025adaptiveweighting` leido completo: la ficha deja de ser "solo abstract" y sus cifras de cuerpo son citables | OK | `capitulo2.tex:82` | OK | `wang2025adaptiveweighting.md:13` retira "Profundidad: solo abstract"; filas 276-277 dan 26.76 dB/0.9501 y 32.67 dB/0.9803, las cuatro cifras que usa el texto |
| 12 | El rango "31-60%" queda retirado; el benchmark ordinal es solo S1 y S2 es descriptivo | OK | `capitulo2.tex:66`; `capitulo3.tex:164` | SIN CIFRA (es una prohibicion) | Busqueda de `31-60`, `31 a 60` en los 13 `.tex` de `overleaf/`: **0 coincidencias**. El S1-only esta escrito en las dos lineas |
| 14, 16 | BFC e ISC retirados; SAP es la unica metrica propia; las de Peters conservan su nombre publicado | OK | `introduccion.tex:43` ("la única métrica que introduce este trabajo"); `capitulo3.tex:261` | SIN CIFRA | Busqueda de `BFC` e `ISC` en `overleaf/secciones/`: **0 coincidencias**. Los tres nombres ingleses en cursiva aparecen en `introduccion.tex:43` y `capitulo2.tex:76` |
| 20 | La unidad de independencia es el paciente; duplicados por huella; se conserva el indice menor | OK | `capitulo3.tex:48` | OK | `capitulo3.tex:48` da 178 volumenes -> 168 pacientes y describe SHA256 de volumen y de corte; coincide con la decision |
| 27 | No se estratifica por fenotipo sacro | OK | `capitulo2.tex:70` ("en lugar de estratificar por fenotipo") | OK | Las dos areas de Gardner (222 frente a 346 mm²) estan en `capitulo2.tex:70`; `main.tex:52` da ademas las de S2 (109.3 y 220.1) |
| 35 | Reparto por objetivo: Obj 1 = grupos 1-3 (168), Obj 2 = grupos 2 y 3 (103), Obj 3 = grupo 3 (66) | OK | `capitulo3.tex:48`, `:50`, `:52` | OK | `capitulo3.tex:48`: 65 + 37 + 66 = 168; 37 + 66 = **103**, que es el numero que da `capitulo3.tex:52`. Grupo 3 = 66, el mismo que `capitulo3.tex:95` |
| 40 | Los 61 CT sin anotar de CLINIC-metal **no** son un banco de geometrias | OK | `capitulo3.tex:54` ("ninguna de ellas es la de aportar geometría de implante") | OK | `capitulo3.tex:54` enumera las cuatro funciones de los 65 con material y excluye la de geometria |
| 42 | Cinco correcciones a `CLAUDE.md` raiz | NO APLICABLE | — | SIN CIFRA | Ordena sobre `CLAUDE.md`, no sobre el documento |
| 47 | Nueva redaccion de C1 (geometria extraida por umbral es inservible) | OK | `capitulo3.tex:54`; `capitulo3.tex:46` | OK | `capitulo3.tex:54`: fragmentados, fuste bajo los calibres publicados, geometria cambiante entre adquisiciones. Es la frase de `main.tex:117` |
| 51 | Error de transcripcion corregido; recuentos 48 y 29 sobre 65 | OK | `capitulo3.tex:97` | OK | `capitulo3.tex:97` dice 48 y 29; `#51` da "marco computable con S1 correcto: 48 de 65; sin contaminacion: 29 de 65" y `main.tex:121` lo repite |
| 55 | El paper de TotalSegmentator no valida la version usada ni la clase S1 | OK (estado ambiguo, M-04) | `capitulo3.tex:85`; `introduccion.tex:84` | OK | `capitulo3.tex:85` nombra la version 2.18.0, la tarea `total` y declara que la publicacion no reporta exactitud para S1 |
| 62 | `zwingmann2013` y `zwingmann2009navigated` no son independientes; la cohorte 2009 entra con cero eventos | OK (estado ambiguo, M-04) | `capitulo2.tex:62` | OK | `capitulo2.tex:62` da 2.6 % (1832 tornillos) y 0.1 % (262 tornillos) y declara el cero de la cohorte 2009; identico a `main.tex:52` |
| 77 | El "2%-15%" no se usa; Templeman no publica porcentaje | OK | — (ausencia buscada) | SIN CIFRA | Busqueda de `Templeman` en `overleaf/secciones/`: **0 coincidencias**. `Routt` aparece solo en `capitulo1.tex:74`, `:76`, sin porcentaje |
| 78 | Vaccaro 1995 no contiene la escala de cuatro grados | OK | `capitulo2.tex:74`; `introduccion.tex:80` | OK | Busqueda de `Vaccaro`: **0 coincidencias**. La escala se atribuye a `gertzbein1990` y `mirza2003` via `smith2006iliosacral`, que es la cadena que #78 deja en pie |
| 80 | Dos trampas de cifra de Noojin y Matta; ninguna cierra #7 | NO APLICABLE | — | SIN CIFRA | Registro de procedencia; no ordena texto. Busqueda de `Noojin`/`Matta`: 0 coincidencias |
| 81 | La parafrasis de Xie en `zhu2023sinogram` no sostiene nada que use el documento | NO APLICABLE | — | SIN CIFRA | Registro; `main.tex` no depende de ella |
| 83 | `ziran2003` no propone el umbral de 10 mm; no hay prior ordinal para S2 | OK | `capitulo1.tex:78`; `capitulo3.tex:89`; `capitulo2.tex:66` | OK | El 10 mm se atribuye a Kaiser et al. como convencion elegida, "y lo atribuyen a trabajos previos". `ziran2007fluoroscopic` se cita solo por los coeficientes de variacion (`capitulo2.tex:70`, `capitulo3.tex:79`), no por el umbral |
| 84 | Tres atribuciones de `kaiser2014dysmorphism` no estan en sus fuentes primarias | OK | — (ausencia buscada) | SIN CIFRA | Las tres no aparecen en `overleaf/`; lo que si aparece (marco de referencia, regla de 5 mm, holgura 1-2 mm sobre 6.3-8 mm) es lo que Kaiser mide por si mismo |
| 86 | Punto de entrada y margenes neurales siguen sin fuente en mm, y el diseno no los necesita | OK | `capitulo1.tex:76` (cualitativo, sin mm) | SIN CIFRA | `capitulo1.tex:76` describe la zona segura y las estructuras vecinas **sin dar milimetros**, que es exactamente lo que #86 permite |
| 87 | La cadena del 2500 HU no tiene origen publicado; se usa como heuristica propia | OK | `capitulo3.tex:46` ("heurística de cribado, no un criterio validado") | OK | Los cinco usos de `2500~HU` en `overleaf/` (`capitulo1.tex:35`, `:46`; `capitulo2.tex:80`, `:84`, `:110`; `capitulo3.tex:46`, `:73`, `:87`, `:119`, `:178`) son todos criterio propio declarado; ninguno se atribuye a literatura MAR |
| 93 | MAISI descartado por diseno: su bundle recorta a [-1000, 1000] HU | NO APLICABLE | — (iria en `capitulo4.tex`, vacio) | SIN CIFRA en `overleaf/` | Busqueda de `MAISI`: **0 coincidencias**. Las cifras (42.24 HU en hueso, 11/34 sobre el umbral) solo estan en `main.tex` (Obj 1) |
| 94 | MedVAE tampoco resuelve la compuerta y excluye metal | NO APLICABLE | — | SIN CIFRA | Busqueda de `MedVAE`: **0 coincidencias** |
| (Radzi / `B_delta`, `:6969`) | El ancho de `B_delta` es construccion declarada, no medicion heredada | OK | `capitulo3.tex:176`; `introduccion.tex:80` | OK | `capitulo3.tex:176`: "Su ancho es un parámetro de diseño"; `introduccion.tex:80`: "Ninguna fuente revisada calibra el ancho de unos 12 mm" |
| 103 | La extraccion por componente murio por memoria a los 47 de 79 casos | NO APLICABLE | — | SIN CIFRA | Registro de ingenieria; no ordena texto |
| 108 | La Tabla III de `karageorgos2024ddpm` apoya la **direccion** de `B_delta`, no su anchura | OK | `capitulo3.tex:176` | OK | `capitulo3.tex:176` da 7.57 HU (mascara verdadera), 11.45 y 11.63 (dilatacion 1.4 y 1.8), 54.82 y 57.69 (contraccion 0.7 y 0.5) y cierra con la salvedad de dominio sinograma. Coincide con la salvedad de `:7822-7825` |
| 114 | `s_por_paso` es promedio acumulado; el regimen real es 0.0923 s/paso | NO APLICABLE | — | SIN CIFRA en `overleaf/` | La propia entrada se declara "Nivel: interno". La cifra no esta ni debe estar en el documento mientras `run02` no cierre (bloque B2) |
| 118 | SAP se mide con 7.0 mm; es la **tercera** geometria, con proposito propio | OK | `capitulo3.tex:114` (Tabla `tab:geometrias`), `:121` | OK | La tabla separa las tres: calibre nominal 6.5-8.0 mm, mascara 4.91 mm, calibre de medicion **7.0 mm** con la atribucion a `zwingmann2009navigated`. Es lo que ordeno la opcion (a) |
| 119 | El "7" de FOV cortado y el "4" de E9-TS son universos distintos y no se citan juntos | OK | `capitulo3.tex:97` | OK | `capitulo3.tex:97` usa el 7 **solo** dentro del universo de R1 ("De los 8 restantes, 7 tenían las crestas ilíacas truncadas"), con los 65 pacientes delante. El "4" de E9-TS no aparece: no se mezclan |
| 120 | El tramo de SAP es el propio implante, recortado 8 mm por extremo; ninguna pose queda sin grado | OK | `capitulo3.tex:87`, `:162` | OK | `capitulo3.tex:87`: "excluidos 8 mm en cada extremo"; `:162` declara el control "ninguna pose puede quedar sin calificar". El valor de 8 mm sigue con `\GAPDEC` propio en `MAPA.md:56`, que es correcto: #120 no lo justifica |
| 121 | El segundo corredor no es S2: se nombra "segundo corredor bajo S1" y se declara 13/4/1 | OK | `capitulo3.tex:164`; `introduccion.tex:68`; `capitulo2.tex:66` | OK | **Recuento propio sobre `r2_nivel_pico_revisor.csv`** (18 filas de datos, columna `nivel_del_punto`): S2 = 13 (`0025, 0030, 0044, 0045, 0050, 0067, 0073, 0077, 0079, 0086, 0088, 0093, 0103`), S3 = 4 (`0036, 0092, 0100, 0101`), S4 = 1 (`0060`). 13+4+1 = 18. "5 de 18 en S3 o mas caudal" = 4+1 ✓. La inversion (`0093` a -39 mm juzgado S2) consta en su comentario: *"al final de S2 casi en la unión"*. Procedencia del lector: ver M-06 |
| 122 | Reportar el W1 preinscrito y, junto a el, la estratificacion post hoc y la fraccion de corredores estrechos | OK en metodo / NO PROPAGADA en cifras | `capitulo3.tex:209` (metodo, pero con la atribucion causal retirada: A-05); cifras -> `capitulo4.tex`, vacio (M-08) | **CIFRA NO CUADRA** (A-07) | `e13b_estratificado.md:9`: "72; con `D_TS_max` >= 7.0 mm: **57**; mas estrechos: **15**". `main.tex:109`: "In **15** of the 72 volumes". El encabezado y el cuerpo de #122 dicen **16** y **22%**; el propio cuerpo explica por que el 16 era espurio (`sap.D_SAP_MM` en vez de `D_TS_max`; el decimosexto, `CLINIC_0018`, tiene `D_TS_max = 7.0`) |
| 123 | La condicion de reapertura del recorte de 6 mm esta **evaluada**: 0 de 16 `fallo_6mm`, el recorte se mantiene | NO PROPAGADA | `capitulo3.tex:91` y `introduccion.tex:84` lo siguen dando por no hecho (A-06) | OK | **Recuento propio sobre `e9ts_revision_laminas_autora.csv`** (16 filas de datos, columna `veredicto`): `ok` = 14, `fallo_ambos` = 2 (`CLINIC_0022`, `CLINIC_0024`), `fallo_6mm` = 0, `fallo_3mm` = 0, `dudoso` = 0. Las cifras agregadas que #123 cita de `e9ts_resumen.md` tambien cuadran con `capitulo3.tex:91`: 65.3 % y 62.5 % con d=6.5, eps=1; mediana 9.5 mm; 29 de 72 pasan los 10 mm (= 40.3 %) |
| 124 | Declarar el acuerdo **61 de 61** con los dos limites, opcion (b) | NO PROPAGADA | `capitulo3.tex:97` conserva el `\GAPDEC` ya resuelto (M-01) | OK | `r1_landmarks.md:45` da la distribucion del revisor clinico (ok 51, +1 7, otro 2, ? 1) y `r1_revision_laminas_revisor.csv` la reproduce: tabla cruzada en la diagonal, 61 de 61. `main.tex:121` ya lo declara con sus dos limites |
| 125 | La cohorte es "sin osteosintesis", no "sin fractura"; cerrada por el cribado de #132 | NO PROPAGADA | `capitulo3.tex:253` e `introduccion.tex:82` siguen en el estado pre-#132 (A-02, A-04) | OK | `r3_fractura_grupos.csv`: `CLINIC_0060` = estrecho, `D_TS_max = 6.2` mm ✓ (#125 dice 6.2); `CLINIC_0022` = estrecho, 4.7 mm ✓; `CLINIC_0043` = 11.7 mm y **no** esta en el estrato estrecho ✓ (`e9ts_revision_laminas_autora.csv` tambien da 11.7). `r3_fractura_revisor.csv` confirma `0060` con `fractura = si, sacro` |
| 131 | El recorte de 6 mm no se reabre; E14 no mueve ningun caso de la cohorte; quedan dos errores de segmentacion | NO PROPAGADA | `capitulo3.tex:91` lo da por pendiente (A-06); los dos errores de segmentacion no estan en ninguna parte de `overleaf/` | OK | Mismo recuento que #123 (14/2/0/0). Las notas: 12 de 16 filas llevan la nota identica sobre la cresta sacra media (`0012, 0023, 0030, 0043, 0045, 0058, 0064, 0076, 0092, 0096, 0100, 0101`), y `0024` la menciona en otra redaccion: coincide con el "12 de los 16" de #131 (ver B-03 por el cambio de termino). `CLINIC_0022` = "se reconoce S2 como S1..." ✓, `CLINIC_0024` = "parte de S1 no es reconocido en la vista coronal..." ✓. Las cifras de E14 (`outputs/e14_relleno.csv`, 152 casos, 0 de la cohorte cambian) **no estan en disco en este arbol**: `NO ENCONTRADO EN LA FUENTE`, solo constan en la propia #131 |
| 132 | 20 de 30 con fractura confirmada; 10 frente a 10; sacra desplazada 7/15 frente a 2/15, p = 0.109, sugerente no concluyente; lector sin especialidad | **NO PROPAGADA** (patron #135, en 4 sitios) | `capitulo3.tex:263` (A-01), `:253` (A-02), `:52` (A-03), `introduccion.tex:82` (A-04); ademas `capitulo3.tex:209` (A-05) | OK en el titular / **CIFRA NO CUADRA** en §4 (A-08) y en la tabla de `D_TS` (M-05) | Recuento propio detallado abajo |
| 130 | Nombrar el tornillo **transiliaco-transsacro**; `mclaren2021corridor` si aplica; Zwingmann y Herman son referencia de **distribucion**, no de equivalencia geometrica | NO PROPAGADA | `introduccion.tex:39`; `capitulo3.tex:101`, `:196`; `capitulo1.tex:72`; `capitulo2.tex:74` (M-02, M-03) | OK | `docs/SITUACION_ACTUAL.md:183` describe el corredor de E9 de cortical externa a cortical externa; `docs/03-glosario.md:74-75` asigna ese rasgo al transiliosacro; `mclaren2021corridor` aporta 1.53 ± 0.57° en S1 y 1.02 ± 0.33° en S2 (`main.tex:52`); `herman2016.md:167` acredita la mezcla de tipos. **Estado etiquetado ABIERTA pese a llevar decision y aplicacion** (M-04) |

### Recuento completo de #132 (el que nadie habia rehecho despues de #136)

**Criterio exacto.** Cruce de `experiments/objetivo2/r3_fractura_revisor.csv` (30 filas de datos,
columna `fractura` con dominio `si`/`no`/`dudoso`) con `experiments/objetivo2/r3_fractura_grupos.csv`
(30 filas, columna `grupo_oculto` con dominio `estrecho`/`control`), clave `Caso`. `dudoso` **no**
cuenta como fractura y se reporta aparte (decision de la autora, 2026-10-05). "Desplazada" = la
columna `comentario` contiene `con desplazamiento`. "Sacra" = `donde` == `sacro`. "Legible desde
lamina" = `legible` == `si`. Equivalente en `pandas`:
`rev.merge(gru, on='Caso').groupby(['grupo_oculto','fractura']).size()`.

| Magnitud | estrecho (n=15) | control (n=15) | total | Coincide con #132/#136? |
|---|---|---|---|---|
| `fractura = si` | **10** | **10** | **20** (67 %) | si, con la correccion de #136 |
| `fractura = no` | 5 | 4 | 9 | si |
| `fractura = dudoso` | 0 | 1 (`CLINIC_0088`) | 1 | si |
| `donde = sacro` | 9 | 5 | 14 | si |
| `donde = ilion` | 1 | 5 | **6** | **NO**: #132 §4 dice 7 (A-08) |
| Sacra **desplazada** | **7** | **2** | 9 | si |
| Desplazada (cualquiera) | 8 | 4 | 12 | si |
| `legible = si` | 8 | 10 | 18 | si |
| Sacra entre los legibles | 3 de 8 | 3 de 10 | — | si |
| Nivel de las 14 sacras | — | — | 9 en S1, 5 en S2 | si |

Casos `si` del estrato estrecho: `0001, 0016, 0027, 0044, 0047, 0060, 0067, 0072, 0078, 0096`.
Casos `si` del estrato control: `0023, 0039, 0049, 0079, 0081, 0083, 0090, 0093, 0100, 0101`.
Sacras desplazadas en estrechos: `0001, 0027, 0044, 0047, 0060, 0072, 0078` (7).
Sacras desplazadas en controles: `0083, 0090` (2).

**Fisher bilateral, recalculado a mano por la distribucion hipergeometrica** (`C(30,9) = 14 307 150`):
7/15 frente a 2/15 da `2 x (675 675 + 96 525 + 5 005) / 14 307 150 = 0.1086` -> **p = 0.109** ✓.
8/15 frente a 4/15 da **0.2636** -> **p = 0.264** ✓. 9/15 frente a 5/15 da **0.2723** -> **p = 0.272** ✓.
**Los tres valores p de #132 son correctos.** Lo que falla es el recuento de `ilion` (A-08) y el
tratamiento del `dudoso` en la tabla de `D_TS` (M-05).

Medianas de `D_TS_max_mm` por estado, recalculadas: desplazada (n=12) = **6.25 mm** (#132 dice 6.2,
B-01); no desplazada (n=8) = **10.4 mm** ✓; sin fractura **excluyendo** el dudoso (n=9) = **5.9 mm**,
**incluyendolo** (n=10) = 6.7 mm, que es el valor publicado (M-05).

---

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una implicancia CERRADA y aplicada a `main.tex` no llega a `overleaf/`, y el `\GAPDATO` que la precedia sigue ahi afirmando que el dato no existe | OC-2, OC-3 | `\GAPDATO{cribado ... preparado y no realizado}` con el CSV lleno en disco | nuevo (es #135 generalizado: ahora son 4 sitios y 4 implicancias) |
| El encabezado de una implicancia conserva una cifra que su propio cuerpo refuta; el redactor copia el encabezado | G-T4 | #122: "En 16 de 72 pelvis" frente a 15 verificadas en su cuerpo | nuevo (hermano de #136) |
| Una rectificacion numerica (#136) corrige las dos cifras que se miraron y deja sin marcar las de otras secciones de la misma entrada | G-T4 | #132 §4: "21 casos (14 sacro, 7 ilion)" sin aviso | nuevo |
| Una regla de analisis (`dudoso` aparte) se aplica a unas tablas de la entrada y no a otras, cambiando el signo del sesgo | G-T4 | #132: "Sin fractura \| 10 \| 6.7 mm" incluye el dudoso | nuevo |
| El estado de una implicancia discrepa entre su encabezado y una tabla resumen del mismo archivo | OC-3 | #55, #62, #130 | nuevo |
| Una segunda lectura se declara sin decir que el lector es la autora, no un clinico | G-T4, P-MM3 | "un segundo lector ciego a la profundidad medida" | nuevo (el estandar correcto lo fija #124) |
| El encargo de redaccion cita un numero de implicancia equivocado y arrastra la cita al texto | G-T4 | Bloque A3: "#124 — Herman et al." siendo #130 | nuevo |

---

## Prioridades: que corregir primero en `overleaf/` y en que seccion

1. **`capitulo3.tex:263` (§Validez externa) — A-01.** Es la unica **afirmacion falsa** del documento de
   entrega y sostiene un argumento de validez externa. Cifras autorizadas: 20 de 30 (67 %) con fractura
   confirmada mas un caso dudoso; 10 frente a 10; sacra desplazada 7/15 frente a 2/15, p = 0.109,
   **sugerente no concluyente**; cribado de medico recien egresado en SERUM, sin especialidad, sobre
   laminas fijas. Nunca 70 % ni 73 %.
2. **`capitulo3.tex:52` y `introduccion.tex:82` — A-03, A-04.** Dos `\GAPDATO` que **declaran no hecho
   algo que esta hecho**. Es peor que una omision: un lector que abra el repositorio ve el CSV lleno.
3. **`capitulo3.tex:253` y `capitulo3.tex:209` — A-02, A-05.** §Validez interna y §SAP: sustituir
   "al menos un paciente" por el cribado completo, y retirar la atribucion causal a la anatomia que
   #132 derogo.
4. **`capitulo3.tex:91` e `introduccion.tex:84` — A-06, M-07.** Cerrar el `\GAPDATO` del recorte de
   6 mm con 14 `ok` / 2 `fallo_ambos` / 0 `fallo_6mm` y con la procedencia correcta del revisor.
5. **`capitulo3.tex:97` — M-01.** Cerrar el `\GAPDEC` del 61 de 61 con la frase y los dos limites de
   `main.tex:121`. Es el punto A4 del encargo y ya no esta bloqueado (#138 nombra la cresta sacra media).
6. **`introduccion.tex:13`, `:15`, `:21` — A-09.** El alcance retirado (sintesis 2D, Dice, HD95) sigue
   afirmado en el bloque (a). Depende de #126, que es decision de la autora, pero mientras se decide
   esas frases deberian pasar a `\GAPDEC` y no quedarse como afirmaciones.
7. **`introduccion.tex:39`, `capitulo3.tex:101` y `:196`, `capitulo1.tex:72`, `capitulo2.tex:74` —
   M-02, M-03.** El tornillo transiliaco-transsacro y la clausula de "distribucion, no equivalencia".
   Citar **#130** como fuente, no #124, y respetar la lista de menciones que deben seguir diciendo
   "iliosacro".
8. **`capitulo3.tex:164` — M-06.** Una palabra: identificar a la autora como el segundo lector.

**Antes de redactar nada de los puntos 1 a 4, conviene que la autora corrija en
`docs/04-implicancias.md` el encabezado de #122 (16 -> 15) y la seccion 4 de #132 (21 y 7 ilion ->
20 y 6 ilion).** Si no, el redactor leera la fuente de autoridad y volvera a escribir las cifras
malas, que es exactamente como nacio #136.
