# Respuesta del redactor — capitulo3 — r18 (modo corregir, ronda unica; encargo 2026-10-12)

Entradas: `capitulo3-r18-{lint,guia,estilo,trazabilidad}.md`, `redaccion/ENCARGO_2026-10-12.md` (P1-P6), IMP #172-#175,
`experiments/objetivo3/resultados_validacion_pose.md` (RVP, versionado en `d5f256e`), `experiments/objetivo3/EXPERIMENTOS.md`
(EXP, filas :57, :67-69, :77 ya en CORRIDO), `experiments/objetivo3/diseno_A.md` (DAE) :41-48, `docs/ESTADO.md` 2026-10-12 (1)-(3),
`experiments/obsoletos/README.md` :112-133.

Lint final: `PASA`, alta=0 media=0 baja=14 (todas E-P1, cifras cuya fuente esta abajo). Compila: 137 paginas.
GAP capitulo3: 2 \GAPLIT / 14 -> 13 \GAPDATO / 16 \GAPDEC.

**Criterio sobre #175 (ABIERTA "solo redaccion").** Sus cifras (196.3 / 6.1 / 115.8 HU; 8 y 27 HU; amplitudes) entran como
**medidas en validacion**, sin GAP: (1) el encargo de la autora lo indica asi ("sus cifras entran como medidas en validacion");
(2) #175 no deja nada por decidir ("Pendiente de la autora: nada que decidir"; formula de DEC 2026-10-09 (4) y lectura (2) de
#169 ya fijadas); (3) `EXPERIMENTOS.md`:57 ya registra "`Delta` 196.3 / 115.8 HU (#175)", que satisface la regla 5 de
`overleaf/CLAUDE.md`; las amplitudes estan en RVP §3, enlazado desde esa misma fila. La lectura de #175 "la diferencia media a
Ti ya excede el margen" NO se escribio (encargo P5: descriptivo de validacion, n = 2).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 (:232 cotejo 12/10, 342/243, "la que se rehace") | trazabilidad | APLICADO | 13 de 24 frente a 7; 9/3 (mediana) y 4/4 (p95); 393 frente a 270 HU; "con cada punto de control leido con su limite calibrado". Fuente: RVP §1; A17p:16-17; IMP #174 (a) |
| T02 (:234 8/10 de 12; 3297/4641; 810/160) | trazabilidad | APLICADO | p95 bajo lo real en 7 de 12 con los dos; `M` p50/p95 3245/4856 (elegido) y 3402/4848 (estado final); distancia 648 frente a 497 HU. Con las cifras vigentes los dos quedan bajo la mediana real dentro de `M`, asi que "la diferencia depende del punto de control" se reescribio como "los dos generan HU mas bajos; el estado final queda mas cerca". Fuente: RVP §1 |
| T03 (:236 749/1076, 977/1238, Ti 2051/1279) | trazabilidad | APLICADO | 1164/1163 frente a 1248/1182; Ti 1881/1287. Ademas, por PAT-141: la sensibilidad se anadio con un cotejo de pose equivocada (ventaja del estado final en `M`, entonces mas amplia) y con la pose corregida se mantiene. Fuente: RVP §3; IMP #175; IMP #174 (a) ("Dentro de `M` se repite #169") |
| T04 (:206 "se rehacen", rama condicional, `\GAPDATO`) | trazabilidad | APLICADO | Parrafo reescrito: 0.05 fijado con modelos anteriores; recalibracion 0.030 / 0.05; cada punto de control con su limite, y asi se calcularon cotejo, margen, corrida final y reconstruccion de implantes reales. Rama "si cambia de ganador" y `\GAPDATO` retirados (-1 \GAPDATO). Fuente: IMP #172, #174 (a); EXP:57, :77 (`a23` con 0.030) |
| T05 (:202 porcion compartida, control bit a bit) | trazabilidad | APLICADO | Cotejo, margen y corrida final de los dos puntos de control: tarjetas del mismo tipo y de uso exclusivo (DAE:46-48 `gpu:rtxa6000:1`; ESTADO 2026-10-12 (2)/(3): 56243/56244 en g002). La reconstruccion de implantes reales, que no se compara con ellas, corrio por disponibilidad en una porcion compartida del mismo tipo (ESTADO 2026-10-12 (3): job 56355 "shard rtxa6000"; EXP:77). El control bit a bit (#170) se retiro: era sobre otra GPU (`a100_3g`) y no describe la corrida vigente |
| T06 (:317-321 sonda con pose espejada y cifras) | trazabilidad | APLICADO | Ver P4 |
| T07 (:325 amplitudes 5380/2205, 2051/1279; 901-1057, 1188-1360) | trazabilidad | APLICADO | Fe 5243/2166, Ti 1881/1287; sintetizador 1069-1361 y 1131-1232 HU. La observacion que motivo la regla queda atribuida al modelo afectado y a la pose equivocada (PAT-141). Fuente: RVP §3 |
| T08 (:327-329 Ti 7/24, 13 de 24, sonda 9895/5390) | trazabilidad | APLICADO | Ver P3 |
| T09 (:335, :337, :339, Tabla, :385: 163.8 / 23.2 / 0.4-5.2 / 100.3) | trazabilidad | APLICADO | 196.3; 6.1; 8 y 27; 115.8; "196.3 frente a 115.8 HU"; todas las menciones "con la lectura de 0.05" retiradas. Fuente: RVP §3; EXP:57; criterio sobre #175 arriba |
| T10 (:38 "la unica que procesa la particion de prueba") | trazabilidad | APLICADO | La corrida final se define como la que procesa prueba con el modelo evaluado y la pose corregida; las generaciones anteriores del modelo reentrenado con la pose equivocada "se archivaron sin evaluarse". Verificado: OBS:129 (`a15_final_run04` archivado), `obsoletos/.../pose_espejada/a20_run04/a20_ea2.csv` solo tiene filas de `0101`/`0102` (validacion), el unico `a24` existente es el de `mejor_37k` (#164), EXP:78 `a24` "LISTO, probado con datos de juguete", ESTADO 2026-10-12 "NO evaluar test con `run04_60k`" |
| T11 (correccion de la pose y control de pose ausentes) | trazabilidad | APLICADO | Ver P1. Dos parrafos nuevos en §Sintetizador y uno en §Amenazas; enmienda del 12 de octubre en §Vision general y en §Resumen del diseno |
| T12 (:38 `\GAPDATO` envejecido) | trazabilidad | APLICADO | Prosa: modelo elegido sobre validacion; generacion de los dos brazos sobre prueba y reconstruccion de implantes reales ejecutadas. Marca: "evaluacion de esas dos ejecuciones sobre la particion de prueba; los resultados del Objetivo 3 sobre esa particion no estan disponibles". Fuente: EXP:57, :68, :77; ESTADO 2026-10-12 (3) |
| T13 (:216 "todavia en curso") | trazabilidad | APLICADO | "se hizo solo con el, y su evaluacion esta pendiente" |
| T14 (fuentes desfasadas) | trazabilidad | ESCALADO (parcial) | Ya resuelto en la fuente antes de esta respuesta: EXP (:57, :68, :69, :77 en CORRIDO/REHECHO, job 56355 registrado), RVP versionado. Queda para la autora, sin `\GAPDEC` en el texto porque las cifras escritas tienen fuente versionada (EXP:57, RVP) y el encargo fija su uso: (a) `docs/00-tesis.md` bloque de `Delta` (aun 163.8 / 100.3 y amplitudes de pose espejada, marcado PENDIENTE) y :117 "corrida final ... en curso"; (b) `diseno_A.md` ENMIENDA run04 :29 y :32-34 (12 frente a 10; 163.8 / 100.3); (c) `tesis/main.tex` (Objectives: "12 of 24 ... against 10", "8 and 10 of 12", "810 HU against 160 HU") difiere de EXP:57 (13 frente a 7). La regla 5 de `overleaf/CLAUDE.md` pediria `\GAPDEC`, pero la discrepancia es un atraso de la fuente frente a #174 DECIDIDA y al encargo, no un conflicto abierto; (d) encabezado de #173 ("ABIERTA ... falta rehacer las corridas") y estado de #175. Ninguno lo puede editar el redactor (regla 14 raiz; lista de archivos permitidos) |
| guia-1 (:38 definicion de corrida final falsa) | guia | APLICADO | Junto con T10 |
| guia-2 (:38 `\GAPDATO` envejecido) | guia | APLICADO | Junto con T12 |
| guia-3 (:236 cifras de pose espejada) | guia | APLICADO | Junto con T03 |
| guia-4 (lista post hoc sin las decisiones de #173-#174) | guia | APLICADO | (1) Control de pose: parrafo propio en §Amenazas (criterio de cordura no preinscrito, decidido tras ver sinteticas de prueba). (2) Sonda no repetida: en el parrafo de :377, "ese veredicto se tomo con la pose equivocada, y lo confirmo despues el protocolo completo con la pose corregida, sin repetir la sonda con sus criterios escritos". (3) Material: en :379, la regla volvio a elegir Ti por 2 frente a 0 y la lectura "el menos alejado" se decidio al ver ese resultado. Parrafos de 7, 4 y 5 oraciones |
| guia-5 (:401 consecuencia en un solo sentido) | guia | APLICADO | "Un intervalo entero por debajo de $-\Delta$ tampoco mostraria por si solo que el sintetizador se aleja de lo real, y la lectura de ese desenlace no esta fijada (Seccion ap-analisis)". Sin la diferencia de validacion como conclusion |
| S1 (fuga repetida en l. 56 y l. 375) | estilo | APLICADO | l. 56 queda en una remision a §Amenazas; l. 375 lleva la consecuencia con "32 pacientes de prueba" y la remision al capitulo de resultados |
| S2 (inciso "la que se rehace") | estilo | APLICADO | Resuelto al reescribir :232 (T01) |
| S3 ("Es el mismo dominio de cortes") | estilo | APLICADO | "Con esos mismos dominios de cortes, uno por brazo, se fijo el margen $\Delta$" |
| S4 (:335 sensibilidades en dos tiempos) | estilo | APLICADO | Una oracion: "Los analisis de sensibilidad repiten la prueba frente al protocolo fisico con hierro, con el estado final como punto de control y sin los tres pacientes ...". La forma propuesta ("Son analisis de sensibilidad la misma prueba ...") daba 43 palabras (E-O1 del lint) |
| S5 (:337 8 oraciones) | estilo | APLICADO | "El margen lo fija, por tanto, ..." abre ahora el parrafo siguiente |
| S6 (:385 9 oraciones) | estilo | APLICADO | Partido en base comun (4 oraciones) y sentido de las tres elecciones con el `\GAPDEC` (4 oraciones) |
| S7 (:391 dos funciones) | estilo | APLICADO | Parrafo nuevo en "El nivel de la referencia ..." |
| S8 ("ademas" en tres aperturas) | estilo | APLICADO | Quitado en l. 395, 397 y 405; tambien en la apertura de :383 ("La particion de prueba ya se habia evaluado") |

## Hallazgos bajos

- T15 (medianas 3465 y 5283 derivadas): APLICADO sin cambio de cifra. Fuente: A17p:9-10 / RVP §1 "Real: `M` p50 3838 / 3092, p95 5262 / 5304 HU"; (3838 + 3092) / 2 = 3465 y (5262 + 5304) / 2 = 5283. Comprobacion de consistencia: |3245 - 3465| + |4856 - 5283| = 647 (RVP 648) y |3402 - 3465| + |4848 - 5283| = 498 (RVP 497), asi que la distancia de RVP se mide contra esas medianas. El texto dice "medianas ... en los dos tornillos reales".
- guia-6: APLICADO (en :377, junto con guia-4).
- guia-7: APLICADO. :321 conserva sin cifras que solo fallo el costo y que se aplico la salida fijada, un corte de cada dos.
- S9, S10 (l. 54): APLICADOS ("Por la regla de un volumen por paciente"; segundo "ademas" quitado).
- S11 (l. 109), S12 (l. 239, oracion eliminada), S14 (l. 383), S16 (l. 409), S17 (l. 66): APLICADOS.
- S13 (conteo / revision en cortes): APLICADO en l. 115 ("el conteo de tornillos que la autora hizo en su revision en cortes") y en la marca de l. 345 ("aplicada sobre esa revision en cortes de la autora"). l. 381 y l. 405 sin cambio.
- S15 ("de modo que" en cierres seguidos): APLICADO en l. 399 y l. 401; l. 405 sin cambio.

## Encargo de la autora (ENCARGO_2026-10-12.md)

| Punto | Decision | Detalle |
|---|---|---|
| P1 correccion de la pose (#173) | APLICADO, con un ajuste | §Sintetizador: el error (eje medido sobre el volumen reorientado; tornillo colocado sin convertir la pose, reflejado y fuera del sacro), la deteccion por la autora, la conversion al marco del volumen y el control de pose (> 5 % de `M` bajo -500 HU; mediana en `M` > 150 HU bajo la del eje del Obj 2; cordura, no preinscrito; 15 = 2 + 13 lo pasan). Segundo parrafo: que se rehizo y que no (E-A1, limite de lectura, 5371 HU, Obj 1 y 2). §Amenazas: parrafo tras el de la evaluacion previa. **Ajuste:** la frase "ninguna cifra del capitulo viene de la pose equivocada" seria falsa (PAT-39): el recuento de cortes de §Sintesis sobre pelvis sin metal (51 frente a 25, IMP #160, 2026-10-09) se midio con `a15` antes de la correccion. Se escribio "Las cifras del Objetivo 3 que este capitulo presenta y que dependen del tornillo sintetico se midieron con la pose corregida, salvo el recuento de cortes ...", y en :291 ese recuento lleva "con la pose anterior a su correccion". La corrida archivada sin evaluar esta verificada (ver T10), asi que no hizo falta `\GAPDATO`. Fuentes: IMP #173 (Origen, Medido, Aplicado); DAE:41-48; OBS:112-133 |
| P2 cotejo (#174 (a)) | APLICADO | Ver T01, T02, T04, T15 |
| P3 material (#174 (b)) | APLICADO | :327 "Con la pose corregida, la regla se aplico de nuevo tal como estaba escrita. Gano el titanio, con 2 de 24 ... frente a 0 de 24 con hierro"; :329 abre con "Ningun material reproduce los tornillos reales, y el titanio es el menos alejado"; Ti sobre lo real en 22 de 24; `M` 7036 (Fe) y 4462 (Ti) frente a 3092-3838 HU. Fuente: RVP §2; A21p:9-10; IMP #174 (b) |
| P4 sonda sin cifras (#174 (c)) | APLICADO | Criterios (:317) y salidas fijadas se conservan; :317 dice que se corrio "con el tornillo del sintetizador en la pose anterior a su correccion". Correcciones de implementacion (-2048 HU, camilla) conservadas sin cifras de sesgo. Retiradas: +237/+276, +3.9/+6.5, 72.8, 10 166/140, 114.7, 108.9 y ~54 h, y 9895/5390 de :329. Veredicto conservado; la pregunta la respondio de nuevo el protocolo completo con la pose corregida en validacion, "que produjo el artefacto en todos los cortes simulados" (IMP #174 (c); EXP:67-68) |
| P5 Delta y amplitudes (#175) | APLICADO | Ver T07, T09 y el criterio arriba |
| P6 estado de la corrida final | APLICADO | :216 (T13); :38 (T12); :323 "ya se corrio con la pose corregida" (EXP:68, job 56245) con su `\GAPDATO` sin cambio |

## Cambios no senalados, hechos para no dejar falsedades al lado

- :291 (51 frente a 25 cortes): "con la pose anterior a su correccion" (ver P1). Dos oraciones fundidas para no pasar de 7.
- §Resumen del diseno: "enmendado el 11 y el 12".
- :325: la medicion que motivo la regla del material, "hecha con un modelo afectado y con la pose equivocada".
- :38 partido en dos parrafos (estado de ejecucion / diseno congelado) para no pasar de 7 oraciones.

## Decisiones de redaccion

- Correccion de implementacion que archiva corridas: se declara una vez en la seccion del metodo que la sufre (error, correccion, control añadido, que se rehizo y que no), y una vez en §Amenazas con lo que se vio antes de corregir. Las cifras vigentes se escriben sin calificativo; las decisiones tomadas con la medicion archivada se dicen como observacion de esa medicion, sin cifras, y la vigente entra como comprobacion (extension de PAT-141 a mediciones, no solo a modelos).
- Nombres: "pose equivocada" / "pose corregida" / "pose anterior a su correccion" para #173; "control de pose" (negrita en §Sintetizador) para `a11.control_pose`, descrito como "criterio de cordura, no preinscrito".
- "Corrida final" = la que procesa la particion de prueba con el modelo evaluado y la pose corregida; las generaciones previas sobre prueba se nombran "generaciones ... archivadas sin evaluarse". Sustituye a la definicion de BITACORA §2 2026-10-10 ("la unica que procesa prueba").
- Una implicancia ABIERTA solo por redaccion, cuyas cifras estan en `EXPERIMENTOS.md` y que la autora manda usar en un encargo, entra como "medido en validacion" sin GAP; su lectura interpretativa (p. ej., "ya excede el margen") no entra.
- Una sonda o paso previo cuya corrida queda archivada se conserva como paso del metodo (criterios, salidas, veredicto) sin cifras, con la fuente que confirmo su pregunta despues.
