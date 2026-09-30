# capitulo3 — r01 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo3.tex`. Reportes leidos: `capitulo3-r01-lint.md`,
`-guia.md`, `-estilo.md`, `-traza.md`. Fuentes releidas para cada cifra o cita tocada: `docs/02-datos.md`
(:117-137), `docs/01-decisiones.md` (2026-09-10; 2026-09-11 (2) #31; 2026-09-13; 2026-09-14 (3);
2026-09-15 (2); 2026-09-17 B.3 y (3); 2026-09-20 (2) D3-D4; 2026-09-21 (2); D-O2.4),
`docs/04-implicancias.md` (#31, #121, #124), `experiments/objetivo2/preinscripcion_muestreador.md` §3-§7,
`tesis/main.tex` :52, :74-84, :107, :117, :121, :123, y las fichas `kaiser2014dysmorphism`, `lin2019`,
`ziran2007fluoroscopic`, `gardner2010safezones`, `smith2006iliosacral`, `liu2021ctpelvic1k`,
`zhu2022optimalposition`.

Conteo (alta + media): **36 APLICADOS, 1 RECHAZADO, 7 ESCALADOS** (44 hallazgos).

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| S01 (alta) | estilo | APLICADO | Junto con T10 y T02. Kaiser ya no figura como origen: "eligen ese corredor de 10 mm como un valor conservador y lo atribuyen a trabajos previos" (ficha, p. e120(2) y (7)); McLaren "lo toma de Kaiser" (ficha `mclaren2021corridor`) |
| S02 (alta) | estilo | APLICADO | Cierre de §Resumen reescrito por objetivo: Obj 1 criterio y regla previos; Obj 2 distribucion y metrica preinscritas sin regla de decision; Obj 3 criterio primario fijado y Delta pendiente. Resuelve tambien la parte de l.231 de guia-2 |
| S03 (alta) | estilo | APLICADO | Se elimino "La lista no es un tramite...". No se adopto la lista de "tres amenazas que condicionan la lectura": seria una valoracion propia sin fuente |
| S04 (media) | estilo | APLICADO | Junto con T08: "porque paciente y metal contribuyen a la misma traza en el sinograma" (`lin2019`, Sec. 2, p. 10506) |
| S05 (media) | estilo | APLICADO | "Ese supuesto no se toma como premisa" sustituido por "La comparacion con el protocolo fisico es la que puede contradecir ese supuesto" |
| S06 (media) | estilo | APLICADO | Junto con T13: se quito "el competidor mas fuerte disponible"; queda "es el unico de los tres brazos que simula la fisica de formacion del artefacto" (TM:98, "physics-based protocol") |
| S07 (media) | estilo | APLICADO | Se quito el comparativo y queda solo "En 7 pacientes, el campo de vision truncaba las crestas iliacas" (TM:121). No se reconstruyo N por resta. **Aviso a la autora:** la frase de TM:121 ("Losses were driven more by ... truncation (7) and landmark localisation than by artifact contamination") no se ve compatible con su propio embudo (48 -> 29); conviene revisarla en `main.tex` |
| S08 (media) | estilo | APLICADO | "coeficientes de variacion de 7 a 25 % en la mayoria de las superficies y de hasta 140 % en el ala superior de S1" (`ziran2007fluoroscopic`, p. 351-352; TM:52) |
| S09 (media) | estilo | APLICADO | Cifras de las dos condiciones: 14 de 75 volumenes de CLINIC-metal anotados en la publicacion (`liu2021ctpelvic1k`, Data annotation, p. 3), sin verificacion local (DAT:157-161), y 178 de 1 184. Se quito "demasiado" |
| S10 (media) | estilo | APLICADO | "porque se asume que la relacion entre mascara y artefacto no depende del tipo de implante" |
| S11 (media) | estilo | APLICADO | Datos de Zwingmann = "referencia clinica" en todo el capitulo (tabla de geometrias, §Geometria, §Poses, §SAP, Amenazas). "Series clinicas" solo para los dos estudios como series |
| S12 (media) | estilo | APLICADO | "Serie navegada / convencional" para Zwingmann (texto y fila 2 de `tab:diseno`); "brazo" queda para las tres condiciones del Obj 3 |
| S13 (media) | estilo | APLICADO | "el diametro del corredor tuvo una mediana de 9.5 mm" |
| S14 (media) | estilo | APLICADO | Coletillas quitadas en l.37, l.51, l.66 y l.171 (la frase de l.171 se elimino entera; el caracter posterior del rediseno queda dicho en l.37, §Compuerta y Amenazas). En l.122 y l.181 se conserva "se declaran en lugar de suponerse": ahi contrasta con suponer, no anuncia |
| S15 (media) | estilo | APLICADO | l.209: "una distancia grande no se corrige moviendo parametros del muestreador" (PRE §6). l.225: se quito la oracion "es posible y reportable"; la mencion queda solo en Amenazas. l.231: frase quitada (S02) |
| S16 (media) | estilo | APLICADO | "excluyo a 11 de 34 ... y a 7 de 57 ..., de modo que la cohorte primaria pierde, en proporcion, mas pacientes del grupo 2". Se evito "subrepresenta", que requiere una referencia de proporcion no fijada |
| S17 (media) | estilo | APLICADO | "se agrupan en cuatro tipos: interna, de constructo, externa y de la conclusion" |
| S18 (media) | estilo | APLICADO | "los HU del hueso quedan sesgados en el volumen sintetizado aunque el generador no tenga error" |
| S19 (media) | estilo | APLICADO | "fijarla sin dato reproduciria el defecto de calibrar contra la referencia clinica" |
| S20 (media) | estilo | APLICADO | Se siguio TM:117 en vez de la propuesta: "el valor que circula en listados de distribuidores solo aparece en la guia del fabricante como canulacion de brocas y destornilladores" |
| guia-1 (alta) | guia | ESCALADO | `\GAPDEC{alinear la pregunta de investigacion y los objetivos de la introduccion con los cuatro objetivos de este capitulo, que hoy no coinciden}` en §Vision general. La correccion es de `introduccion.tex` (DESFASADO, #126 ABIERTA), fuera de esta seccion |
| guia-2 (alta) | guia | ESCALADO | l.231 corregida (S02). En §SAP se dice que el Obj 2 no tiene regla de decision y se abre `\GAPDEC{si se fija una escala de lectura de la distancia de Wasserstein-1, o que resultado contaria como fallo del muestreador}`; la fila 2 de `tab:diseno` dice "sin regla de decision". Fijar la escala es decision de la autora (PRE §6 no la da) |
| guia-3 (media) | guia | ESCALADO | l.12: se quito "cada uno produce una pieza verificable". §Protocolo explica que el Obj 4 no tiene fila porque su producto son las metricas de las filas 2 y 3, y cita los seis controles de SAP; `\GAPDEC{que evidencia verifica el Objetivo 4 mas alla de esos controles, o si se declara que no se evalua experimentalmente}` |
| guia-4 (media) | guia | ESCALADO | Ninguna fuente justifica `h = 2 sigma` (PRE §3.1 solo dice "propia, declarada"; sin rastro en DEC, IMP ni TM). `\GAPDEC` en §Poses y mencion en validez de constructo |
| guia-5 (media) | guia | ESCALADO | Aplicado: la prueba se parea por paciente (D4 pto 2: "mismos pacientes en los dos brazos"). Escalado: la agregacion de poses y regiones por paciente no consta; `\GAPDEC{como se agregan por paciente las poses y las regiones de medicion de rayas antes de las pruebas}` |
| guia-6 (media) | guia | APLICADO | La extension a MAISI se presenta como posterior al veredicto (§Compuerta), se anade a validez interna y a la multiplicidad de validez de la conclusion ("un septimo candidato") |
| guia-7 (media) | guia | APLICADO | El control de nivel se describe (DEC 2026-09-13: TS/R1 discordante, S1 en borde del FOV o vacia) y §Corredor remite a el. La heuristica de referencias no esta descrita en ninguna fuente: `\GAPDATO{descripcion de la heuristica de localizacion de las referencias anatomicas, que hoy solo consta en el codigo}` |
| guia-8 (media) | guia | ESCALADO | Tres `\GAPDEC`: proporcion de parches de solo banda (DEC 2026-09-21: 0.62 frente a 1.40), numero de pacientes del brazo fisico (sin cifra en ninguna fuente) y numero de pacientes de validacion para Delta (DEC registra 5 en D4 y 3 en 2026-09-21 (2)). Las cifras existentes no se copiaron: la regla 5 de `overleaf/CLAUDE.md` limita las cifras propias a TM y `EXPERIMENTOS.md`, y la de validacion ademas cambio entre decisiones |
| guia-9 (media) | guia | APLICADO | Definicion de una linea del grado de brecha en la apertura del muestreador, con `\ref{sec:sap}` |
| T01 (alta) | traza | APLICADO | "Los 168 pacientes se reparten en tres grupos (...). La particion trabaja sobre 179 unidades de volumen (...). De esas unidades, 10 quedan fuera de uso y una se reserva como par de reproducibilidad del mismo paciente" (DAT:136-137). No se dio el motivo "por duplicado": las 10 no comparten un solo motivo en DAT |
| T02 (alta) | traza | APLICADO | Viabilidad = `D >= d + 2c`, con `c` = 1-2 mm y la lectura radial declarada como operacionalizacion propia (DEC 2026-09-11 (2), #31 APLICADA; D-O2.4). El 10 mm queda como convencion de comparacion y sus cifras 29/27 de 72 se conservan como tales. `\GAPDATO{numero de corredores viables con el criterio D >= d + 2c; las cifras disponibles usan la convencion de 10 mm}`: ninguna fuente da ese recuento. **Aviso a la autora:** TM:52 y :123 siguen con 10 mm (IMP #31 lo registra) |
| T03 (alta) | traza | APLICADO | "Su regla operativa se fijo por escrito antes de correr la prueba que decide la compuerta. Una exploracion previa, con el autoencoder preentrenado sobre la cohorte completa, ya habia quedado por encima del criterio" (DEC 2026-09-15 (2) y 2026-09-17 (3)). l.37 dice "antes de correr la prueba que decide". **Aviso:** TM:77 ("The gate rule is fixed before any run") contradice DEC |
| T04 (media) | traza | APLICADO | "Si ninguna aprueba, la regla registrada establece que el Objetivo 3 no se ejecuta y que el veredicto negativo se reporta como resultado", seguida de "El rediseno ... es posterior a esa regla" (DEC 2026-09-17 B.3). **Aviso:** TM:77 dice "the latent route is abandoned" |
| T05 (media) | traza | APLICADO | `\GAPDATO{preinscripcion y corrida del muestreo de poses en el segundo corredor bajo S1; su eje ya esta medido en 69 de 72 casos}` (IMP #121, act. 2026-09-22 (7), CERRADA). Fila de MAPA corregida |
| T06 (media) | traza | APLICADO | Se quito "Existe ademas una segunda lectura del nivel S1"; queda solo la `\GAPDEC` de #124 (ABIERTA) |
| T07 (media) | traza | APLICADO | "Esas dos huellas, mas una observacion visual que unio dos adquisiciones del mismo implante, agrupan los 178 volumenes en 168 pacientes" (DAT:117-122) |
| T08 (media) | traza | APLICADO | Ver S04 |
| T09 (media) | traza | APLICADO | "Dilatarla eleva el error a 11.45 y 11.63 HU (...); contraerla lo eleva a 54.82 y 57.69 HU" frente a 7.57 HU. No se adopto "multiplica por siete" (S22 y T09): seria una cifra calculada, no copiada |
| T10 (media) | traza | APLICADO | Ver S01 |
| T11 (media) | traza | APLICADO | "Gardner et al. \cite{gardner2010safezones} encuentran una zona segura de S1 menor en sacros dismorficos, pero recogen un estudio previo que no hallo diferencia" (ficha, Discusion, p. 628). No se cito `kaiser2014dysmorphism`: la diferencia de criterios de clasificacion consta en DEC, no en la ficha de Kaiser como contraste |
| T12 (media) | traza | APLICADO | "de la que Smith et al. \cite{smith2006iliosacral} declaran tomar la escala" (ficha, Screw Position, p. 236). No se anadieron `gertzbein1990` ni `mirza2003`: sus fichas no se releyeron en esta ronda |
| T13 (media) | traza | APLICADO | Ver S06 |
| T14 (media) | traza | ESCALADO | Sin marca en el texto: la redaccion sigue DEC (D3 y D-O2.6), que tiene mas autoridad que TM (orden de `MAPA.md`). Pedido a la autora: alinear TM:78 ("constrained by bone density") y TM:117 ("The head is modelled") |
| lint AI (media) | lint | RECHAZADO | Falso positivo, ya documentado en r00: "AI" aparece dentro de la expansion del nombre propio `MAISI (\emph{Medical AI for Synthetic Imaging})`, copiada de la ficha `guo2025maisi`. E-T3 rige para las siglas del documento, y reescribir el nombre para evitar el lint iria contra la instruccion de no esquivarlo |

## Bajas

Aplicadas: S21 (se quitaron cinco "Por eso"; queda uno en §Compuerta, donde la causa es la oracion inmediatamente anterior), S22 (con la version de T09), S23, S24, S25, S26, S27, S28,
S29, S30 (se quito la sigla VAE, que no se reusa), guia-11 (`$p = 0.3$`), guia-13 (la compuerta pasa arriba
de la figura y se cambio el pie), T15 a T25. No aplicadas: S31 (DEC 2026-09-17 B.1 no da el motivo de las
ablaciones; darlo seria completar), guia-10 (ninguna fuente del repositorio define "2.5D"; se deja al cap. 1),
guia-12 (la tabla cambiaria de forma; se puede hacer cuando se cierren los GAP de sensibilidad).

Cambio minimo fuera de lo senalado: en la oracion de T20 se escribio "modelo de elementos finitos" en lugar de
"estudio de elementos finitos". La ficha `zhu2022optimalposition` describe un estudio radiologico que usa
elementos finitos como validacion.

## GAP (tras r01)

- `\GAPDATO` (9): 7 de r00, dos con el texto corregido (eje del segundo corredor; 16 casos), mas 2 nuevos
  (recuento con `d + 2c`; heuristica de referencias).
- `\GAPDEC` (16): 8 de r00 mas 8 nuevos (alineacion con la introduccion; `h = 2 sigma`; evidencia del
  Obj 4; regla o escala de W1; proporcion de solo banda; n del brazo fisico; agregacion por paciente;
  n de validacion para Delta).
- `\GAPLIT` (0). `docs/literatura/_candidatos.md` no se toco.

## Lint

`python scripts/lint_redaccion.py capitulo3 --compilar`: compila (54 paginas el documento entero).
Alta 0, media 1 (el falso positivo "AI"), baja 3 (E-P1 en lineas con 2.5D, 12 mm y 8 mm, que son
parametros de diseno ya trazados en r00). `LINT: FALLA` solo por el falso positivo.

## Decisiones de redaccion

- **Datos de Zwingmann:** "referencia clinica" para el conjunto de comparacion (nunca "conjunto de
  referencia", "serie de referencia" ni "la referencia" a secas). "Serie navegada / serie convencional"
  para sus dos grupos. "Series clinicas" solo cuando se habla de los dos estudios como series.
- **"Brazo"** se reserva para las condiciones experimentales propias (sintetizador, copia y pegado,
  protocolo fisico); no se usa para las tecnicas quirurgicas de Zwingmann.
- **Viabilidad del corredor:** el criterio es `D >= d + 2c`, con la holgura radial por lado declarada
  como operacionalizacion propia de la frase de Kaiser. "10 mm" solo como "convencion de comparacion".
  Kaiser no se presenta como origen del 10 mm (lo atribuye a trabajos previos); McLaren lo toma de Kaiser.
- **Recuentos de cohorte:** "paciente" solo para pacientes (168); los volumenes fuera de uso y el par de
  reproducibilidad se cuentan como "unidades de volumen" (179).
- **Regla de la compuerta:** se dice "fijada antes de correr la prueba que decide", nunca "antes de
  cualquier corrida", y su consecuencia negativa se cita como se registro ("el Objetivo 3 no se ejecuta").
- **Sin metadeclaraciones:** no cerrar oraciones con "y se declara", "y asi se enuncia" ni "es un
  resultado reportable". Se dice el hecho o la regla ("no se corrige moviendo parametros").
- **Comparaciones de cifras ajenas:** se dan los valores, sin factores calculados ("multiplica por
  siete"), para no introducir cifras que no estan en la ficha.
- **Valor p:** `$p$` minuscula en todo el documento; `$P$` queda para distribuciones.
- **Autores de una entrada con dos autores:** "Zhu y Liao", no "et al." (E-F3).
