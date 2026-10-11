# capitulo3 — r10 — respuesta del redactor

Modo `corregir`. Reportes leidos: `capitulo3-r10-lint.md`, `-guia.md`, `-estilo.md`, `-trazabilidad.md`.
Sin cifras de la corrida final en prueba (jobs 55453-55455). #158 sigue ABIERTA (su `\GAPDEC` se conserva).
Fuentes cotejadas: `experiments/objetivo3/diseno_A.md` §0; `a15_cadena_completa.py`:298-299; `a11_rasterizar_tornillo.py`:87-112;
`a23_ea1.py`:14, :79; `a20_resultados.md`; `sonda_peters.md`:88-152; DEC D3, D4, 2026-10-05, 2026-10-05 (3), 2026-10-08 A,
2026-10-09 (2)-(8); IMP #90 (act. 2026-09-21); `docs/ESTADO.md`:278-279; `tesis/main.tex`:98; ficha `peters2025hybrid`.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | ESCALADO | Ni `diseno_A.md` §0 (l. 127, solo "Lo que NO entra") ni DEC dan la razon del eje sin perturbar: `\GAPDEC` en §Apariencia, Sintesis sobre pelvis sin metal. Aplicado lo que tiene respaldo: l. 194 distingue la pose de la sintesis en general de la de la evaluacion; la ultima caja de la Figura 3.1 dice "con el tornillo sobre el eje del corredor sin perturbar"; amenaza nueva en validez externa ("los resultados del Objetivo 3 no cubren esas poses"), que es consecuencia directa del diseno congelado |
| guia-2 | guia | APLICADO + ESCALADO | `M` descrita como se corrio: cuerpo de 4.91 mm con cabeza de 8.0 x 4.5 mm en el extremo de entrada (Tabla 3.1, §Geometria l. 109 y 129, desplazamiento de dominio "cilindro ... con cabeza"). `\GAPDEC` con la diferencia D3 frente a corrida (BITACORA §2, 2026-09-29, capitulo3-r05) |
| guia-3 | guia | APLICADO | Retirado "la cabeza y la rosca entran como variantes de sensibilidad" y "se evalua el tornillo macizo frente al hueco". Ahora: rosca, arandela y canulacion no entran en la corrida final, sensibilidad no programada (`diseno_A.md` l. 126); lo corrido es "sin arandela y macizo" (`a15`:298-299, `rasteriza(..., True, False, 0.0, ...)`) |
| guia-4 | guia | APLICADO + ESCALADO | El segundo desplazamiento se declara sin medicion donde actua: el salto solo se mide en la reconstruccion de implantes reales (`diseno_A.md` l. 97; `a23_ea1.py`). `\GAPDEC` con DEC 2026-10-08 A.7 frente al diseno congelado. En la reconstruccion se precisa "descontado el de la TC real" (`a23_ea1.py`:14, `exceso_costura`) |
| guia-5 | guia | ESCALADO | DEC D4 y `diseno_A.md` §0 solo fijan "equivalencia si el IC90 cae entero" y que un no concluyente no pasa a "comparable"; no distinguen IC entero fuera de IC que cruza. `\GAPDEC` en §Analisis estadistico. La oracion de E9 se retiro aqui (queda una vez en validez de la conclusion) |
| guia-6 | guia | ESCALADO | `\GAPDEC` de #90 reformulado con el estado vigente: la contingencia sigue abierta aunque el diseno congelado fija el TOST como primario (DEC 2026-10-09 (6) pto 2, (8)). No se retira: #90 sigue ABIERTA y cerrarla es de la autora (regla 3 de `overleaf/CLAUDE.md`) |
| guia-7 | guia | APLICADO | Razon del margen al abrir su parrafo: "la variabilidad propia del metodo bajo condiciones que no deberian cambiar el resultado" (`tesis/main.tex`:98; DEC D4 pto 4). Desajuste de escala dicho como hecho en validez de la conclusion: `s_sem` es rango entre semillas sueltas y la prueba compara medianas de 5 semillas; "el diseno no ajusta el margen a esa diferencia". No se afirma cuanto menos varian las medianas (sin fuente) |
| guia-8 | guia | APLICADO + ESCALADO | (b) aplicado: la rama "se cambia la representacion" ya no puede aplicarse porque el diseno congelado fija la representacion (DEC 2026-10-09 (6); `diseno_A.md` §0 l. 25). (a) escalado: DEC 2026-10-05 pto 2-3 compara una fraccion sin unidad con `Delta` en HU sin conversion. El `\GAPDATO` del desenlace pasa a `\GAPDEC` (como expresar la perdida en HU y que consecuencia tiene una perdida mayor) |
| guia-9 | guia | APLICADO | Oracion nueva: la reconstruccion de implantes reales es un analisis descriptivo que no entra en ninguna decision del Obj 3; informa de la discrepancia con implante real, tambien fuera de la distribucion de entrenamiento, y es la unica evaluacion congelada que mide el salto en el borde de `G`. Cruce con `introduccion` (abajo) |
| guia-10 | guia | APLICADO | `s` y `r` de `Delta` pasan a $s_{\mathrm{sem}}$ y $r_{\mathrm{rep}}$ (en §Analisis y en validez de la conclusion). "*t* de Student" queda como nombre de la distribucion, en cursiva de texto (`\emph{t}`) y no como simbolo matematico, para no chocar con el $t$ de la Ec. 3.3 |
| guia-11 | guia | APLICADO | §Apariencia partida en siete `\subsubsection` con etiqueta: Metricas y su inversion (`sec:ap-metricas`), Sintesis sobre pelvis sin metal (`sec:ap-sintesis`), Reconstruccion de implantes reales (`sec:ap-reconstruccion`), Criterio primario y contrastes (`sec:ap-contrastes`), Brazos de comparacion (`sec:ap-brazos`), Analisis estadistico (`sec:ap-analisis`), Contraste de realismo (`sec:ap-realismo`). El parrafo de preservacion fuera de la banda paso a Metricas. Los usos previos de `Delta` (§Sintetizador y cortes de solo banda) remiten a `sec:ap-analisis` |
| guia-12 | guia | APLICADO | l. 194 describe el entrenamiento que produjo el modelo: segundo entrenamiento de 60 000 pasos, minimo de validacion en el paso 37 500 (`docs/ESTADO.md`:278). Retirados "el entrenamiento se fija en 30 000 pasos" y la meseta de "dos corridas" (#148 ABIERTA: no son independientes). En el parrafo del punto de control, los 30 000 pasos quedan como decision anterior que "deja de describir el modelo usado" (DEC 2026-10-09 (2) pto 2). "Unos 37 000" pasa a "37 500" en todo el capitulo |
| E1 | estilo | APLICADO | "brazo fisico" -> "protocolo fisico" en todo el capitulo; "brazo" solo en plural o "los tres brazos" |
| E2 | estilo | APLICADO | "el protocolo fisico sirve de comparacion y no es la verdad"; validez de constructo: "El protocolo fisico, contra el que se decide el contraste primario, tampoco es la verdad fisica" |
| E3 | estilo | APLICADO | "estadisticos sin referencia" -> "estadisticos que no exigen una imagen sin metal"; "referencia de realismo" como nombre propio, en negrita en su definicion; "Con un solo paciente de referencia" (regla del material) -> "Con un solo paciente con tornillos reales" |
| E4 | estilo | APLICADO | "un cambio posterior a ver las amplitudes de los dos materiales en validacion" |
| E5 | estilo | APLICADO | "El ancho se cambio despues de ver el resultado con 0.5 mm, y se reportan los dos" |
| E6 | estilo | APLICADO | Partidos por funcion: l. 204 (referencia y regla / ancho de cascara), l. 200 (por que no la perdida / criterio sobre sintesis), l. 50, l. 54, l. 238, l. 336; tambien los desplazamientos de dominio (enumeracion / medicion) y validez externa (fractura / resto), para no pasar de 7 al anadir |
| E7 | estilo | APLICADO | Cierre de `Delta` con su consecuencia (texto propuesto) |
| E8 | estilo | APLICADO | Validez de la conclusion: "Como el margen crece con la variabilidad del sintetizador, la prueba favorece a un sintetizador inestable", con remision a `sec:ap-analisis` |
| E9 | estilo | APLICADO | Oracion retirada de §Analisis; la declaracion de potencia queda una vez en validez de la conclusion |
| E10 | estilo | APLICADO | Razon dada y acotada a la sintesis: "el artefacto generado cambia los HU de `G` frente a la TC original: un valor alejado del ideal no indica un resultado peor, y se lee frente al valor del protocolo fisico". La lectura en la reconstruccion no se inventa: el diseno no la fija, y las metricas se declaran descriptivas en las dos |
| E11 | estilo | APLICADO | "A diferencia de la MAR, aqui la desviacion dentro de $B_\delta$ es la senal buscada y no un error" pasa al parrafo que define el campo de desviacion; retirada del parrafo de preservacion |
| E12 | estilo | APLICADO | "La referencia de realismo la define una regla de inclusion, escrita antes de ..." (fusiona las dos primeras oraciones) |
| E13 | estilo | RECHAZADO | BITACORA §2, 2026-10-05 (capitulo3-r07): "Un contraste que no puede fallar se declara con esas palabras —... 'una debilidad reconocida del diseno y no una victoria del metodo'— seguido de su consecuencia". Es una decision de redaccion vigente, no un remate |
| E14 | estilo | APLICADO | "es un cribado y no una lectura de especialista." |
| E15 | estilo | APLICADO | "Si esa fraccion no es nula, la cola inferior queda censurada y la amplitud medida es una cota inferior" |
| E16 | estilo | APLICADO | Primera mencion: "los dos repositorios publicados que lo implementan: el del simulador y uno de ejemplos que incluye los guiones del desafio AAPM"; despues "el repositorio de ejemplos" / "del simulador" |
| E17 | estilo | APLICADO | l. 200: "Tampoco se elige por la fidelidad con que regenera los implantes reales de validacion" |
| E18 | estilo | APLICADO | "... con que Peters et al. validan su simulacion en un fantoma fisico" (ficha, 3.1 p. 6) |
| T01 | traza | APLICADO + ESCALADO | Igual que guia-2 y guia-3 |
| T02 | traza | APLICADO + ESCALADO | Igual que guia-4 |
| T03 | traza | ESCALADO | Fuera de alcance del redactor: `docs/00-tesis.md` y `experiments/objetivo3/EXPERIMENTOS.md` no se tocan (regla 14 raiz; lista de archivos editables). Sin cambio ni GAP en el capitulo, que sigue a DEC. Para la autora (abajo) |
| T04 | traza | APLICADO | `\GAPDATO` acotado: "resultados del protocolo fisico sobre los 13 pacientes de prueba de la sintesis sobre pelvis sin metal; los de validacion ya fijaron el material y el margen $\Delta$" |
| T05 | traza | ESCALADO | Igual que guia-6 (reformulado, no retirado: #90 ABIERTA) |
| T06 | traza | APLICADO | "La primera corrida no cumplio el segundo criterio ni la parte de truncamiento del primero, por dos errores de implementacion ...; su costo, de 114.7 horas, tambien superaba el limite, sin ser un error" (`sonda_peters.md`:123-133, :140) |

Bajos aplicados: guia-13 ("intervalo real" sustituye a "envolvente real" en l. 204, 206, realismo, regla del material y Tabla 3.3); guia-14 ("en la prueba exacta de Fisher, bilateral"); guia-15 en parte (con titanio las replicas difieren en 0.4 y 5.2 HU, `a20_resultados.md`; el supuesto de normalidad del IC con *t* NO se escribio: ninguna fuente del repositorio lo enuncia, regla 1 de `overleaf/CLAUDE.md`); guia-16 (remision a `sec:amenazas` en §Resumen); guia-17 (`\GAPDEC` del tamano y la regla de la muestra del QC visual; `diseno_A.md` §7 solo dice "muestra fija"); guia-18 (= T04); E19 ("en la generacion de sus datos"); E20 ("horas de computo"); E21; E22 (= T06); E23; E24 (fundida: "sin prueba de hipotesis y sin intervencion del protocolo fisico"); E25 ("de los 47 pacientes de entrenamiento"); E26 ("vale 1 por construccion"); E27; T07 ("cinco puntos": el tope [0.5, 3] del cociente del realce, `sonda_peters.md`:94-96); T08 ("En la regla del material, aun con titanio, ..."); T09 ("los 13 pacientes de la sintesis sobre pelvis sin metal"); T10 ("rango entre semillas"); T11 ("con el mismo detalle" retirado; queda "Se reportan los resultados con los dos materiales", DEC 2026-10-09 (5) pto 6); T12 (la pertenencia del tornillo a la clase de 2.5-10 mm se dice "lectura de este trabajo").

Correcciones al lado, minimas: oraciones que el lint marco por pasar de 40 palabras tras las ediciones (l. 188, 202, 208, 274, 276, 296, 306, 316, 320) partidas o acortadas; "La sonda no calculo la amplitud del sintetizador" paso al cierre del parrafo de la segunda corrida para no dejar 8 oraciones; `\ref{sec:apariencia}` de validez interna, de constructo y de la conclusion apuntan ahora a la subseccion concreta.

## Escalados para la autora (preguntas)

1. **Cabeza del tornillo (T01, guia-2).** D3 fija cilindro uniforme con cabeza como sensibilidad; `diseno_A.md` §0 y `a15` sintetizan con cabeza de 8.0 x 4.5 mm. Se adopta la cabeza como parte de `M` (y se registra en DEC) o se declara como desviacion de D3?
2. **Salto en el borde de `G` (T02, guia-4).** DEC 2026-10-08 A.7 lo fijaba en E-A2 para los dos brazos; el diseno congelado solo lo mide en E-A1. Se mide tambien en E-A2 (enmienda) o se declara que el segundo desplazamiento de dominio queda sin medicion?
3. **Pose de E-A2 (guia-1).** Cual es la razon de evaluar sobre el eje del corredor sin perturbar y no sobre poses del muestreador? (Sin razon registrada en `diseno_A.md` ni DEC.)
4. **Lectura del TOST (guia-5).** Si el IC90 queda entero fuera de `[-Delta, +Delta]`, cuenta como evidencia en contra del sintetizador? Y si cruza el margen, se declara no concluyente?
5. **Implicancia #90 (guia-6, T05).** Se cierra la contingencia de plazo, dado que el diseno congelado fija el TOST como primario y la corrida final ya lo lanzo? Si se cierra, el `\GAPDEC` se retira aqui, en `introduccion` §Alcance y en `capitulo1` §Marco estadistico.
6. **Regla del suelo de -1000 HU (guia-8).** Como se expresa en HU la perdida (fraccion sin unidad, DEC 2026-10-05 pto 2) para compararla con `Delta`, y que se hace si es mayor, ahora que la representacion esta congelada?
7. **QC visual (guia-17).** Tamano y regla de seleccion de la "muestra fija" de casos sintetizados que revisa la autora.
8. **Fuentes desfasadas (T03).** Actualizar `docs/00-tesis.md` (Obj 3: n = 14 -> 13, `Delta` medido, regiones en todos los cortes que toca `G`, diseno congelado) y `experiments/objetivo3/EXPERIMENTOS.md` (estado de `diseno_A.md`, filas `a17`-`a24`, sonda). Ya figura como pendiente en `docs/ESTADO.md`.

## Contradicciones en otras secciones (no tocadas)

- `introduccion.tex`:48 dice que `Delta` esta "aun sin medir" (fijado en 188.7 HU, DEC 2026-10-09 (4)).
- `introduccion.tex`:56 y `capitulo2.tex`:106: el protocolo fisico "sobre las poses del muestreador"; el diseno congelado usa el eje sin perturbar.
- `capitulo1.tex`:122: "los 14 valores de los pacientes de prueba sin metal"; el diseno congelado usa 13 (DEC 2026-10-09 (8) pto 3).
- `introduccion.tex`:41 (Obj 3) no nombra la reconstruccion de implantes reales; el capitulo 3 la declara analisis descriptivo adicional (guia-9).
- `introduccion` §Alcance y `capitulo1` §Marco estadistico conservan el `\GAPDEC` de #90 con su redaccion anterior.
- `capitulo1` conserva el `\GAPDATO` del suelo de -1000 HU; en `capitulo3` paso a `\GAPDEC` (guia-8).
- `redaccion/MAPA.md`, fila del `\GAPDEC` "tipo de implante de los 3 pacientes de referencia": la marca ya no esta en el capitulo (tornillos-r01); la fila sigue abierta (aviso repetido de r09).

## GAP

- Nuevos `\GAPDEC` (5): cabeza en `M`; salto en el borde de `G` en E-A2; razon de la pose sin perturbar; desenlaces del TOST; muestra del QC visual.
- Convertido: `\GAPDATO` del desenlace del suelo -> `\GAPDEC` (unidades y consecuencia tras el congelamiento).
- Reformulados: `\GAPDEC` de #90 (estado vigente); `\GAPDATO` del protocolo fisico (acotado a los 13 de prueba).
- Sin `\GAPLIT` nuevo: `_candidatos.md` no cambia.
- Totales del capitulo (lint): 2/14/3 -> 2/13/9 (lit/dato/dec).

## Decisiones de redaccion

- "**Intervalo real**" = rango del minimo al maximo de los tornillos reales en el perfil radial (cotejo, regla del material, realismo); "envolvente" queda solo para la envolvente osea.
- Los estadisticos del cotejo se nombran "los estadisticos que no exigen una imagen sin metal", nunca "sin referencia"; "**referencia de realismo**" es nombre propio del conjunto de tornillos aislados reales de prueba.
- Terminos del margen: $\Delta = \max(s_{\mathrm{sem}}, r_{\mathrm{rep}})$; "*t* de Student" en cursiva de texto, no como simbolo.
- §Apariencia con `\subsubsection` numeradas y etiquetas `sec:ap-*`; los demas capitulos pueden remitir a ellas (`sec:ap-analisis` para `Delta` y el TOST, `sec:ap-sintesis` para la pose y la *streak amplitude*).
- Si el diseno congelado (o su codigo) difiere de una decision anterior de DEC: el texto describe lo congelado y corrido, y el `\GAPDEC` dice "la decision registrada ... fija X, pero las corridas ... hacen Y: falta decidir si ...".
- Una rama de una regla preinscrita que el congelamiento deja sin efecto se dice como hecho ("ya no puede aplicarse tal como se escribio, porque el diseno congelado fija ...") y la consecuencia pendiente va a `\GAPDEC` (PAT-116).
- Todo costo de calculo = "horas de computo" (CPU o tarjeta grafica); "tarjeta grafica" solo para el dispositivo.
- "Protocolo fisico" tambien para el brazo, incluidos "protocolo fisico con titanio/hierro" y "protocolo fisico completo"; de lo que no es la verdad se dice "sirve de comparacion".
- Punto de control elegido = "37 500 pasos" (`docs/ESTADO.md`:278), no "unos 37 000".
