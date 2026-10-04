# Respuesta del redactor — capitulo1 — r02

Modo: corregir. Archivo: `overleaf/secciones/capitulo1.tex`. Reportes: `capitulo1-r02-lint.md`
(PASA, 0/0/0), `-guia.md` (2 medias, 6 bajas), `-estilo.md` (14 medias, 11 bajas),
`-trazabilidad.md` (1 media, 2 bajas). Hallazgos sacados por oscilacion: ninguno.

Lint final (`python scripts/lint_redaccion.py capitulo1 --compilar`): **PASA**, alta=0 media=0 baja=0;
compila (106 paginas). GAP: lit=4, dato=1, dec=7 (sin cambio de conteo).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Ninguna ficha enuncia la forma de la ley (`deman2007catsim` solo define `mu_ok` y `l_iso`; `abadi2019`:51 y `wang2019cochlear`:52,56 solo la nombran). Se amplio el `\GAPLIT` de §1.1 (l.35) para que pida tambien el enunciado de la ley de Beer-Lambert con el coeficiente de atenuacion lineal. MAPA y `_candidatos.md` actualizados (misma fila, no es GAP nuevo) |
| guia-2 | guia | APLICADO | Parrafo nuevo al final de §1.2 con las tres metricas de Peters et al. y sus nombres publicados (terminos fijos), definidas desde la ficha `peters2025hybrid` (Sec. 2.5, pp. 5-6: streak "highest and lowest 5%", bone "above 150 HU ... SDC", metal "highest CT number within a ROI ... plus 250 HU"), con remision a `sec:apariencia` y la *streak amplitude* como unico criterio primario (`capitulo3.tex`:217). Fila 2 de la Fig. `fig:mt-conceptos` ampliada con las metricas |
| S01 | estilo | APLICADO | Junto con guia-6 (baja, mismo problema). Se quito "en el orden en que se necesitan sus conceptos" y se anadio la razon de que la cirugia vaya antes del modelo generativo: el muestreador precede al sintetizador en la cadena (`capitulo3.tex` Fig. `fig:pipeline`) |
| S02 | estilo | APLICADO | La oracion de la cohorte local ahora dice su consecuencia (un hueso definido por 150 HU dejaria fuera esos voxeles), segun `capitulo3.tex`:85 ("dejaria fuera, en la mediana, esa fraccion del corredor") |
| S04 | estilo | APLICADO | "delimita el metal clinico de sus volumenes" (PAT-97) |
| S07 | estilo | APLICADO | La dispersion pasa al parrafo del endurecimiento, que abre con "Dos de esos mecanismos producen rayas parecidas entre si", con la semejanza de `deman1999` Sec. III-C ("very similar to the polychromatic artifacts"). Para que el parrafo de la inanicion no quede en dos oraciones (E-O2) se anadio la no linealidad del ruido (`deman1999` Sec. III-E: "Noise artifacts are non-linear artifacts, just like beam hardening and scatter") |
| S11 | estilo | APLICADO | Eliminada la reconstruccion por FBP de CatSim en §1.2 (ya en l.33, PAT-102) |
| S14 | estilo | APLICADO | "umbral de 10 mm" en la oracion de Kaiser et al. y dentro del `\GAPDEC` (PAT-14), igual que l.78 |
| S15 | estilo | APLICADO | "Zwingmann et al. aplican la escala de perforacion (Seccion sap)." |
| S17 | estilo | APLICADO | "En la formulacion de Ho et al., la red no predice la imagen limpia, sino el ruido anadido, ..." (PAT-101) |
| S18 | estilo | APLICADO | La U-Net se liga al sintetizador: "El borrador del diseno del sintetizador propone tambien una U-Net, arquitectura que aun no se ha fijado (Seccion sintetizador)". Fuente: `experiments/objetivo3/diseno_A.md` §5 (`[SUPUESTO]`); la arquitectura ya esta en el `\GAPDEC` de `capitulo3.tex`:172, por eso no se abre GAP nuevo |
| S19 | estilo | APLICADO | "... mas rapida, en tiempo de reloj, que la del muestreo de Ho et al." La ficha `song2021ddim`:9 define DDIM frente a DDPM (Ho et al.); la frase copiada de la Evidencia (l.26) no trae el referente, que el auditor da por confirmado (inventario l.214) |
| S20 | estilo | APLICADO | Las dos etapas se nombran antes de enumerar: autoencoder y modelo de difusion en el latente (ficha `rombach2022latentdiffusion`:13); el decodificador pasa a oracion propia |
| S21 | estilo | APLICADO | Eliminada "Ese contexto no convierte al modelo en un simulador fisico"; queda la oracion verificable con "este trabajo lee" |
| S23 | estilo | APLICADO | Eliminada la ultima oracion de §1.5 parrafo de superioridad y equivalencia (PAT-98) |
| S25 | estilo | APLICADO | Junto con T03 (baja). "La regla de la compuerta aprueba si lo hace cualquiera de sus seis combinaciones de autoencoder y codificacion; esa multiplicidad ... no lo compromete", y oracion aparte con la extension a Guo et al. como septimo candidato sobre los mismos pacientes de prueba (`capitulo3.tex`:75, 265) |
| T01 | trazabilidad | APLICADO | El `\GAPDEC` se mantiene (regla 3; #130 ABIERTA) con el hecho del registro visible: "que tornillo representa el corredor que mide este trabajo, que el registro describe de la cortical externa de un ilion a la del ilion opuesto, y con ello si le aplican el umbral de 10 mm y la holgura radial de Kaiser et al., definidos para el tornillo iliosacro". No se usa "transsacro" en el texto (calco sin forma establecida en espanol). MAPA actualizado con #130 |

## Hallazgos bajos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-3 | guia | APLICADO | LeFusion se introduce en el cuerpo con su cita: "o del metodo LeFusion de Zhang et al.~\cite{zhang2025lefusion}" (no se pone `\cite` dentro de la marca: ninguna seccion lo hace) |
| guia-4 | guia | APLICADO | "su estudio" / "En ese estudio" (PAT-14) |
| guia-5 | guia | APLICADO | Al final del parrafo de la zona segura: no se usa como variable, es antecedente del corredor que mide el muestreador (`capitulo3.tex`:168) |
| guia-6 | guia | APLICADO | Con S01 |
| guia-7 | guia | APLICADO | Con S05: "El Objetivo 1 examina tres codificaciones", la primera con las ventanas de Wang et al. como canales (`capitulo3.tex`:69) |
| guia-8 | guia | APLICADO en parte | El parrafo de la definicion queda solo con la definicion y el ejemplo de Wang et al.; la clausula "en una cascada ... y no como canales" se conserva porque sin ella el ejemplo atribuiria a Wang et al. el uso por canal (E-R6). El techo de 2000 HU pasa al parrafo del uso propio, como motivo de las otras dos codificaciones |
| S03 | estilo | NO APLICADO | Partir el parrafo de HU antes de "Dos umbrales" deja un primer parrafo de dos oraciones (E-O2) |
| S05 | estilo | APLICADO | Parrafo partido; el segundo abre con "Este trabajo usa la codificacion multiventana en dos piezas" |
| S06 | estilo | APLICADO | "sus listas comparten el endurecimiento del haz, la dispersion y los efectos de borde, y difieren en el resto" |
| S08 | estilo | APLICADO | |
| S09 | estilo | APLICADO | |
| S10 | estilo | APLICADO | "Como la cohorte solo contiene volumenes reconstruidos (Seccion mt-tc), este trabajo asume ..." |
| S12 | estilo | APLICADO | Quitado "guiados por imagen durante la operacion" |
| S13 | estilo | APLICADO | "En Smith et al., el tornillo iliosacro entra por el ilion y llega a ...". Se mantiene el subjuntivo "de modo que atraviese" porque la ficha dice "intended to cross 3 cortices" |
| S16 | estilo | APLICADO | "de modo que sus resultados no se comparan con las distribuciones de grados de Zwingmann et al." |
| S22 | estilo | APLICADO | Orden 1, 2, 3 |
| S24 | estilo | APLICADO | El parrafo del intervalo por remuestreo se unio al de las pruebas, que abre con "Tres procedimientos de inferencia completan el marco" (Wilcoxon, TOST, remuestreo); el `\GAPLIT` de las tres fuentes queda al cierre |
| T02 | trazabilidad | APLICADO | "la primera o la segunda vertebra sacra" (sin "cuerpo"), `smith2006iliosacral`:69 |
| T03 | trazabilidad | APLICADO | Con S25 |

Correcciones laterales: cuatro oraciones nuevas superaban las 40 palabras (lint E-O1) y se partieron;
el parrafo de orden (l.13) quedaba en ocho oraciones y se fundieron las dos primeras.

Conteo: altos+medios 17 (APLICADO 17, RECHAZADO 0, ESCALADO 0). Bajos: 18 aplicados (uno en parte), 1 no aplicado.

## GAP

| Tipo | Abiertos | Cerrados | Modificados |
|---|---|---|---|
| `\GAPLIT` | 0 | 0 | 1 (fisica de TC: ahora incluye la ley de Beer-Lambert; `_candidatos.md` y MAPA actualizados) |
| `\GAPDATO` | 0 | 0 | 0 |
| `\GAPDEC` | 0 | 0 | 1 (tipo de tornillo del corredor: texto segun T01 y "umbral de 10 mm"; #130 en MAPA) |

Totales en la seccion: lit=4, dato=1, dec=7.

## Decisiones de redaccion

- **"Umbral de 10 mm", no "corredor de 10 mm".** La cifra de Kaiser et al., Gardner et al. y McLaren et al. se nombra siempre "umbral de 10 mm" (sobre el tamano del corredor); "corredor" queda para la region osea. Vale tambien para `capitulo2` y `capitulo3` si usan "corredor de 10 mm".
- **No usar "transsacro".** El corredor de `tesis/main.tex` (*transsacral*) se describe por su recorrido (de la cortical externa de un ilion a la del opuesto) mientras #130 este ABIERTA; "transiliosacro" queda para la definicion de McLaren et al.
- **Metricas de Peters et al. en el marco teorico.** Se presentan una vez en §1.2 con sus nombres publicados y remision a `sec:apariencia`; la definicion operativa y su inversion quedan en el cap. 3.
- **Un `\cite` nunca va dentro de una marca GAP**: si la marca nombra una fuente que el lector no conoce, se presenta antes en el cuerpo con su cita.
