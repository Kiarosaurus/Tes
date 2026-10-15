# Auditoria de trazabilidad — capitulo3 — r22

Archivo: `overleaf/secciones/capitulo3.tex` (463 lineas), sin cambios de texto desde r21. Lint r22: PASA (22 bajas E-P1).
Respuesta previa: `capitulo3-r21-respuesta.md` (sin rechazos; nada que respetar como RECHAZADO). Fuentes nuevas
cotejadas: `docs/01-decisiones.md` 2026-10-15 (puntos D1-D16, D-extra 1-4, 21 y 22) e implicancias #183, #184, #185 y
#186 (ABIERTAS). Por la decision de BITACORA §2 del 2026-09-29, una DEC que resuelve una implicancia aun ABIERTA se
redacta como decidida; las cifras que solo constan en #185/#186 (CV 0.076/0.241, r = 0.40, piso de ruido de 184 HU)
no entran como hecho. No se abrieron PDF.

Lo que el encargo pedia comprobar:
- **Delta 163.8 / r 23.2:** el capitulo ya usa los vigentes (196.3 / 6.1 / 115.8; :377, :379, :381, :404, :433). La
  discrepancia sobrevive en `experiments/objetivo3/diseno_A.md`:29-33 (T05).
- **Lote 4:** el `\GAPDEC` de :204 queda cerrado por D3 (lote 16; "lote 4" fue error de registro) (T08).
- **Desenlace del TOST de v1:** :248 lo atribuye a la causa equivocada y :377/:453 niegan una lectura que D15 ya fija
  (T01, T02).

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-3 | `capitulo3.tex:248` | "No se concluyó equivalencia ..., porque el intervalo de la diferencia quedó entero por debajo de cero" | DEC 2026-10-15 D15; `resultados_prueba_v1.md`:14, :27-29; #177 | La causa que se da es errónea. Un IC90 entero bajo 0 puede caer dentro de ±Δ. Con IC90 [-477.0, -124.9] y Δ = 196.3, el intervalo **cruza** -Δ. D15 clasifica ese resultado como "no concluyente con diferencia significativa a la baja". Que el IC90 excluya 0 da la **dirección**, no el desenlace. | "El intervalo del 90 % de la diferencia cruzó el límite inferior del margen. El desenlace fue no concluyente, con una diferencia significativa a la baja: el sintetizador da rayas más débiles (capítulo de resultados)". Decir en la misma oración que esa categoría se fijó después de ver el resultado (ver T04). |
| T02 | alta | G-T4, OC-3; PAT-116 reincide | `:377` (`\GAPDEC` "qué desenlace ... cuenta como evidencia en contra"), `:453` ("la lectura de ese desenlace no está fijada") | "la lectura de ese desenlace no está fijada" | DEC 2026-10-15 D15 | D15 fija tres desenlaces: equivalencia (IC90 entero dentro de ±Δ), no equivalencia (IC90 entero fuera) y no concluyente (IC90 cruza un límite). La dirección se reporta siempre que el IC90 excluya 0. El confirmatorio es solo `run04_mejor` con su Δ. El resto es descriptivo, con la multiplicidad declarada y sin corrección. La incertidumbre de Δ (n = 2) se declara aparte. El texto afirma que nada de esto está fijado. | Retirar el `\GAPDEC` y escribir en `sec:ap-analisis` los tres desenlaces, el carácter confirmatorio y la declaración de la incertidumbre de Δ. En :453, en lugar de "no está fijada", poner que un IC90 entero bajo -Δ contaría como no equivalencia, y que eso tampoco mostraría por sí solo un alejamiento de lo real. Declarar que la regla es posterior para la versión 1 (T04). |
| T03 | alta | G-T4, OC-3; PAT-11 reincide | `:198` (regla del suelo y su `\GAPDEC`), `:419` (percentil 5), `:451` ("La regla que trata el suelo se evalúa contra el contraste primario ... no fija cómo expresar esa pérdida en HU") | "La regla que trata el suelo se evalúa contra el contraste primario" | DEC 2026-10-15 D1; #186; DEC 2026-10-05:1593-1619 | D1 declara la regla **no aplicable**, por tres razones. Su desenlace depende del percentil: 225.0 HU con el p95 de la pérdida por paciente, que coincide con el percentil 5 de la fracción superviviente, y 1.2 HU con la mediana. Ese desenlace ya era calculable antes de fijar una conversión. Y su rama de cambio de representación está bloqueada por el congelamiento. La pérdida ya está expresada en HU, y se reportan los dos valores. En su lugar entran la fracción de la ROI de Peters bajo -1000 HU y un TOST con las imágenes de Peters (con metal y limpia) recortadas a -1000 HU, con el mismo suelo en los dos brazos. Es un análisis posterior y su dirección (hacia la equivalencia) está declarada. El texto sigue presentando la regla como vigente y la conversión a HU como pendiente. | En :198, sustituir la regla por el hecho decidido: la regla no es aplicable, con los dos valores (225.0 y 1.2 HU) y sus tres razones. Quitar el `\GAPDEC`. Añadir la sensibilidad con Peters recortado a -1000 HU como posterior, con su dirección. En :451 retirar "se evalúa contra el contraste primario ... no fija". En :419 conservar la elección del percentil 5 como post hoc y añadir que la regla quedó declarada no aplicable. |
| T04 | alta | G-T4, G-C7; PAT-13 y PAT-140 reinciden | `:38` ("se evaluaron con el diseño preinscrito"), `:248` ("se evaluó tal como estaba preinscrita"), `:391`, `:419-433` (lista post hoc del Obj. 3) | "La corrida final de la versión 1 se evaluó tal como estaba preinscrita" | DEC 2026-10-15 encabezado ("previo al TOST de prueba de v2 y posterior para v1"), "Regla general", D1, D2, D5, D9, D12, D14-D16, D-extra 1-4, punto 22; `experiments/objetivo3/visto.md` | La generación y la regla de equivalencia sí estaban preinscritas. Lo que falta es todo lo que la DEC fijó el 2026-10-15, después de ver la prueba de la v1: la lectura de los desenlaces (D15) y el sustituto del suelo (D1). También las sensibilidades sin cabeza (D2) y con intersección de cortes (D-extra 1), la costura en los dos brazos (D5) y las 5 poses (D9). Y además el comparador paramético (D12), el IC por permutación (D14), los márgenes mínimo y común (D16), el piso de ruido (D-extra 2) y la lectura de acuerdo (22). Ni la lista de decisiones post hoc ni la oración de :391 los recogen. Tampoco se enuncia la regla general: ninguna sensibilidad añadida puede **elevar** la categoría del desenlace primario, solo bajarla. | En :248 y :38, "la generación y la regla de equivalencia se fijaron antes; la lectura de sus desenlaces y las sensibilidades del 15 de octubre, después de ver el resultado". Añadir a `sec:amenazas` un párrafo con la lista completa de lo fijado el 15 de octubre, la regla general y el inventario de lo visto (`visto.md`). En :391, añadir que las reglas de lectura del TOST son posteriores para la versión 1 y previas para la versión 2. |
| T05 | alta | G-T4, OC-5; PAT-138 y PAT-158 reinciden | fuente: `experiments/objetivo3/diseno_A.md`:29, :32-33 (texto en `capitulo3.tex`:240, :379, :381) | "`Delta`: principal 163.8 HU (`s` de `run04_mejor`; `r` = 23.2)" | DEC 2026-10-15 punto 21; #175; `resultados_validacion_pose.md`:19-20, :49-52; `docs/00-tesis.md`:157-158 | El capítulo copia los vigentes: 196.3 / 6.1 / 115.8 HU y un cotejo de 13 frente a 7. La ENMIENDA del diseño congelado sigue diciendo 163.8 / 23.2 / 100.3 HU y 12 frente a 10. La viñeta de corrección de #173 solo dice que se rehacen, sin dar las cifras nuevas. Las dos fuentes de la misma magnitud discrepan entre sí. | Que la autora actualice la ENMIENDA de `diseno_A.md` con las cifras de la pose corregida (o con una nota que las retire y remita a `resultados_validacion_pose.md` §3). En el `.tex`, sin cambio. |
| T06 | alta | G-T4, OC-5; PAT-138 y PAT-158 reinciden | fuentes: `docs/00-tesis.md`:91, :174, :186-188, :319-321; `experiments/objetivo3/EXPERIMENTOS.md`:39-40; `resultados_prueba_v1.md`:27 | "con cabeza y rosca de 7.3 mm como sensibilidad"; "semimaximo local queda como variante de sensibilidad" | DEC 2026-10-15 D1, D2, D4, D15; #172 (A); #184 | Las fuentes de contenido van detrás de la DEC y discrepan con ella. En `00-tesis.md`: :91 da la cabeza como sensibilidad (D2: la cabeza es parte de la síntesis); :319-321 da el semimáximo como sensibilidad (D4: no se entrena); :186-188 da la regla del suelo como vigente (D1: no aplicable); y :174 da `delta = 0.05` sin la recalibración 0.030 de #172. En `EXPERIMENTOS.md`:39-40, `a23_v2` figura CORRIENDO y `a20_v2` POR CORRER, cuando #184 da E-A1 v2 terminado y `a20_v2` (56847) abortado. En `resultados_prueba_v1.md`:27, la lectura figura como "no fijada en el diseño". | Que la autora actualice esas líneas (regla 14 raíz). Mientras tanto, el `.tex` sigue a la DEC, como corresponde. |
| T07 | media | OC-2; PAT-19 y PAT-133 reinciden | `:143` (`\GAPDEC` de la cabeza) | "falta decidir si la cabeza se adopta como parte de $M$" | DEC 2026-10-15 D2 | Decidido: la síntesis usa el tornillo con cabeza congelado el 2026-10-09, y se declara como desviación de D3 (2026-09-20). La sensibilidad posterior es E-A2 sin las ROIs a menos de 20 mm del extremo con cabeza, en los dos brazos. | Sustituir el `\GAPDEC` por el hecho: desviación declarada y sensibilidad posterior. El resultado de esa sensibilidad va en `\GAPDATO` si no se ha corrido. |
| T08 | media | OC-2; PAT-19 reincide | `:204` (`\GAPDEC` del lote) | "la decisión registrada ... da lotes de 4, pero el entrenamiento usó lotes de 16" | DEC 2026-10-15 D3 | D3 corrige el registro de 2026-10-08 punto 3: el lote corrido en run02, run04, run05a y run05b es 16, y "lote 4" fue un error de registro que no cambia ningún resultado. | "lotes de 16" sin GAP. Si se quiere, una cláusula de que el registro anterior decía 4 por error. |
| T09 | media | OC-2; PAT-19 reincide | `:214` (`\GAPDEC` del semimáximo) | "si la máscara ... por semimáximo local se entrena y reporta como sensibilidad o se retira" | DEC 2026-10-15 D4 | Decidido: no se entrena, por coste. Se reporta la diferencia de diámetro entre las dos máscaras en componentes de 500-4000 mm³ de entrenamiento, como dato de la limitación. | Hecho decidido, más un `\GAPDATO` para la diferencia de diámetro si no está medida. |
| T10 | media | OC-2; PAT-19 reincide | `:228` (`\GAPDEC` del salto en el borde de $G$) | "si el salto en el borde de $G$ se mide también en la síntesis" | DEC 2026-10-15 D5 | Decidido: la costura se mide en E-A2 para los dos brazos, como fijaba la DEC de 2026-10-08 punto 7 que el congelamiento omitió. Se agrega el perfil de *streak amplitude* en anillos de 2 mm entre 8 y 16 mm, descriptivo. | Hecho decidido, con `\GAPDATO` para el resultado. Retirar o ajustar "el diseño congelado solo la toma en la reconstrucción" a "el congelamiento la omitió y se añadió el 15 de octubre". |
| T11 | media | OC-2; PAT-19 reincide | `:232` (`\GAPDEC` del paciente de 8.9 mm) | "si el paciente ... cuenta como paciente sin metal ... o en el grupo~2" | DEC 2026-10-15 D6 | Decidido: `CLINIC_0066` va en el grupo 2 según `grupos.csv`, que prevalece sobre 2026-09-21 (2). No cambia receptores ni resultados. | Retirar el `\GAPDEC` y escribir que pertenece al grupo 2 (objeto no ortopédico). |
| T12 | media | OC-2; decisión de BITACORA §2 2026-10-08 | `:242` (`\GAPDEC` del mecanismo del p95) | "mecanismo del sesgo del percentil~95: hipótesis sin verificar" | DEC 2026-10-15 D7 | La decisión del diagnóstico ya está tomada. Se usan validación, `0101` y `0102`, 5 semillas y `run04_mejor`, y `regla_suave` se compara con solo LW, con control sobre la ida y vuelta de parches reales. La lectura está fijada de antemano: el mecanismo es el decodificador si con LW el p95 entra en la envolvente en al menos 4 de 7 cáscaras y el control se mueve menos de la mitad; si no, el modelo o indeterminado. Lo único que falta es el dato. | Pasar a `\GAPDATO` ("desenlace del diagnóstico preinscrito del percentil 95, aún no medido") y dejar la regla en prosa. |
| T13 | media | OC-2; PAT-19 reincide | `:317` (`\GAPDEC` de la preservación del protocolo físico) | "si la preservación del protocolo físico se mide con RMSE y SSIM" | DEC 2026-10-15 D8 | Decidido: se reporta como caracterización de la referencia. Se dan el RMSE y el SSIM (rango [-1000, 2000] HU) de la simulación sin metal frente a la TC original, fuera de $G$ y dentro del cuerpo, más la amplitud de solo ruido. Para el sintetizador vale 0 por construcción y no se presenta como resultado. | Hecho decidido, con `\GAPDATO` para el valor. |
| T14 | media | OC-2; PAT-19 reincide | `:327` (`\GAPDEC` de la pose), `:457` ("los resultados del Objetivo~3 no cubren esas poses") | "razón para evaluar el sintetizador sobre el eje ...: el diseño congelado solo registra la exclusión" | DEC 2026-10-15 D9; `sonda_peters.md`:145 | La razón ya está registrada: aislar la apariencia de la colocación (que evalúa el Objetivo 2) y el coste del protocolo físico (sonda: 108.9 h con k = 1). Se añade un análisis exploratorio de 5 poses del muestreador por paciente de E-A2, solo con el sintetizador (`run04_mejor`, 5 semillas), con *streak amplitude* y *metal integrity* por grado de brecha. La expectativa se fijó antes: poca variación entre grados. | Dar las dos razones en prosa y quitar el `\GAPDEC`. En :457, matizar: las poses perturbadas solo se examinan en un análisis exploratorio, sin protocolo físico (`\GAPDATO` para el resultado). |
| T15 | media | OC-2; PAT-19 reincide | `:341` (`\GAPDEC` de la muestra de control visual) | "tamaño y regla de selección de la muestra de casos sintetizados" | DEC 2026-10-15 D10 | Decidido: la muestra son 13 pacientes, semilla 0 y 3 cortes (el de mayor área de $M$, más 1/4 y 3/4 del tramo evaluado), con una lista cerrada de cuatro defectos. Es control, no evaluación, y no es ciego para run04. | Escribir la muestra, la lista de defectos y que no es ciego. Quitar el `\GAPDEC`. |
| T16 | media | OC-2; PAT-19 reincide | `:355` (`\GAPDEC` de la implicancia 158) | "si el repositorio del desafío AAPM se cita como fuente de la implementación" | DEC 2026-10-15 D11 | Decidido: el protocolo se atribuye a Peters et al. y la implementación al repositorio del reto AAPM en versión fija, con una tabla de las cinco desviaciones. :357 ya cita `xcist2025example` en `4993e87`. La DEC del 2026-10-10 en BITACORA §2 ("sin cita ni URL mientras #158 esté abierta") queda sin objeto. | Quitar el `\GAPDEC`. Atribuir la implementación al repositorio de ejemplos citado (`xcist2025example`, `4993e87`) y convertir los cinco puntos de :355 en tabla. |
| T17 | media | OC-2; PAT-19 reincide | `:375` (`\GAPDEC` del tamaño de efecto del Wilcoxon) | "si la prueba de cordura reporta un tamaño de efecto con su IC" | DEC 2026-10-15 D12; `resultados_prueba_v1.md`:23-24 | Decidido: se declara la degeneración del contraste (la copia y pegado vale 0 por construcción; $p = 2^{-13}$, el mínimo alcanzable con 13 pares) y no se reporta tamaño de efecto. | "No se reporta tamaño de efecto: la prueba es degenerada ..., y su $p$ es el mínimo alcanzable con 13 pacientes". Quitar el `\GAPDEC`. |
| T18 | media | OC-2, OC-3; PAT-19 reincide | `:377` (`\GAPDEC` de la implicancia 90) | "cierre formal de la contingencia de plazo ... (implicancia 90)" | DEC 2026-10-15 D13; `04-implicancias.md`:6464 (#90 CERRADA 2026-10-14) | D13 manda retirar las marcas. #90 está CERRADA por ejecución desde el 2026-10-14. | Eliminar el `\GAPDEC` sin sustituto. |
| T19 | media | OC-2; PAT-19 reincide | `:377` (`\GAPDEC` del supuesto de *t*) | "supuesto distribucional del IC con \emph{t} ...: el diseño congelado no lo enuncia" | DEC 2026-10-15 D14 | Decidido: el IC90 con *t* supone diferencias pareadas aproximadamente normales e independientes. La sensibilidad es el IC90 exacto por inversión de la prueba de permutación pareada (2^13 cambios de signo), sujeta a la regla general. | Enunciar el supuesto y la sensibilidad (posterior para la v1) y quitar el `\GAPDEC`. |
| T20 | media | OC-2; PAT-19 y PAT-133 reinciden | `:433` (`\GAPDEC` de la implicancia 162) | "si ... se reporta la prueba de equivalencia con un margen no fijado por el sintetizador" | DEC 2026-10-15 D16 | Decidido: se reporta el margen mínimo de equivalencia (el mayor \|límite\| del IC90) de cada modelo y el TOST de los tres modelos con el margen común de run04 (196.3 HU), además del propio. Se declara el sentido conjunto de las tres elecciones. El margen 0.80-1.25 se descarta porque se eligió tras ver la razón de la v1. | Sustituir el `\GAPDEC` por lo decidido, con la exclusión del 0.80-1.25 y su motivo. |
| T21 | media | G-T4, P-MM3 | `:343`, `:347` (contrastes y brazos) | "La superioridad frente a la inserción por copia y pegado se declara control de cordura" | DEC 2026-10-15 D12 | D12 añade un comparador nuevo, posterior y descriptivo: un **artefacto paramétrico** (tornillo a HU constante más el perfil radial medio del artefacto real de tornillos de `d1_d2`, sin difusión). El capítulo no lo nombra ni en los contrastes ni en los brazos. | Añadirlo en `sec:ap-brazos` como comparador posterior y descriptivo, con su construcción y fuera de la tabla de diseño preinscrito. Resultado en `\GAPDATO`. |
| T22 | media | G-T4, G-C7; PAT-11 reincide | `:329` ("Cada brazo se mide en los cortes que produce"), `:451` (suelo), `:463` ("El diseño no evalúa si esa diferencia desplaza la mediana") | "El diseño no evalúa si esa diferencia desplaza la mediana de cada paciente" | DEC 2026-10-15 D-extra 1, D-extra 2, D1; #186 | #186 registra tres asimetrías entre brazos: cortes k = 2 solo en Peters, piso de ruido de Peters y suelo de -1000 HU solo en el difusor. La DEC decide una sensibilidad para cada una: `a20 --interseccion`, la amplitud nula de cada brazo (Peters `limpia_A - limpia_B`, y el difusor generando $G$ sin $M$ en 13 × 5) y Peters recortado a -1000 HU. :463 afirma que ninguna se evalúa, y el capítulo calla el piso de ruido. La cifra de 184 HU solo consta en #186 (ABIERTA) y no debe entrar. | En :463, nombrar la sensibilidad con intersección de cortes (posterior). En `sec:ap-analisis`, añadir la amplitud nula de los dos brazos "junto a la amplitud de cada brazo", sin cifra. En amenazas, presentar las tres asimetrías juntas, con su dirección, y remitir a T03 para el suelo. |
| T23 | media | G-T4 | `:375-381` (`sec:ap-analisis`) | (ausencia) | DEC 2026-10-15 punto 22; #185 | La DEC fija una lectura de acuerdo entre brazos (Bland-Altman y Pitman-Morgan), descriptiva, para v1 y v2. #185 da la razón: el TOST de medias no ve la diferencia de dispersión entre pacientes. El análisis estadístico no la menciona. | Una oración en `sec:ap-analisis`: análisis descriptivo de acuerdo, añadido el 15 de octubre (posterior para la v1). Las cifras de #185 (ABIERTA) van al cap. 4, no aquí. |
| T24 | media | OC-2, G-T4; PAT-122 y PAT-11 reinciden | `:38` ("cuya evaluación en prueba sigue en curso"), `:277` (procedimiento de la v2 y `\GAPDATO` "cuyas generaciones están en curso") | "resultados de la evaluación exploratoria ..., cuyas generaciones están en curso" | #184; DEC 2026-10-15 encabezado, D16, D-extra 3, D-extra 4; `EXPERIMENTOS.md`:39-40 | Las generaciones terminaron. E-A1 de la v2 en prueba está calculado (#184). `a20_v2` (56847) abortó en la etapa de validación, y el TOST de la v2 no ha corrido. Al procedimiento de :277 le faltan tres cosas: el TOST con el margen común de 196.3 HU, además del propio (D16); la repetición de E-A1 de run05a y run05b con `--delta` 0.03 para separar modelo y lectura (D-extra 3); y el inventario de lo visto (D-extra 4). | Redactar el GAP con el estado vigente: "la prueba de equivalencia de la versión 2 sobre la partición de prueba no se ha ejecutado; la reconstrucción de implantes reales sí, y su resultado está en una implicancia abierta". Añadir D16 y D-extra 3 al procedimiento de :277. |
| T25 | baja | G-T4; decisión de BITACORA §2 2026-09-29 (no derivar cifras) | `:242` | "frente a medianas de 3465 y 5283~HU en los dos tornillos reales" | `resultados_validacion_pose.md`:23 (real: `M` p50 3838 / 3092, p95 5262 / 5304 HU) | 3465 y 5283 son las medianas (es decir, las medias) de dos valores por tornillo, calculadas a partir de la fuente versionada. La fuente no las da, y los valores por tornillo no aparecen en el texto. | Dar los valores por tornillo (3838 y 3092 HU; 5262 y 5304 HU), o citar la salida que trae la mediana real si se versiona. |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9-15, Fig. `fig:pipeline` | Dos componentes, cuatro objetivos, $G = M \cup B_\delta$, tornillo transilíaco-transsacro | `docs/00-tesis.md`; DEC 2026-10-08 C; #130 | si |
| :31 (figura) | Evaluación sobre el eje sin perturbar | DEC 2026-10-15 D9 (razón ahora registrada) | si (ver T14) |
| :36 | Dice/HD95 y ablaciones fuera; 14 de 75 anotados; 178 de 1184 | `docs/00-tesis.md`, "Fuera de alcance"; ficha `liu2021ctpelvic1k` | si |
| :38 | Obj. 1 negativo; Obj. 2 ejecutado; v1 evaluada "con el diseño preinscrito" | `resultados_prueba_v1.md`; DEC 2026-10-15 encabezado | **no (T04)** |
| :38 | GAPDATO del realismo sin script | `resultados_prueba_v1.md`:44-45 | si (GAP justificado) |
| :38 | v2 "sigue en curso" | #184; `EXPERIMENTOS.md`:39-40 | **no (T24)** |
| :40 | Congelado el 9-oct; enmiendas 11 y 12-oct; corrida final; generaciones archivadas | DEC 2026-10-09 (6), 2026-10-11 (2)-(3); `diseno_A.md`:14-48; #171, #173 | si |
| :44 | 1184; 103 + 75 = 178; correspondencia inferida | ficha `liu2021ctpelvic1k`; `docs/02-datos.md` | si |
| :46 | Parámetros de reconstrucción no reportados; Selles et al. | fichas `liu2021ctpelvic1k`, `selles2024marreview` | si |
| :48 | 2500 HU de cribado; revisión 3D de 178; GAPDATO multiplanar | DEC 2026-09-11 (3); `docs/02-datos.md` | si |
| :50 | SHA256; 168 pacientes; 65/37/66; 179 unidades; 10 fuera; 1 par | DEC 2026-09-10; `docs/02-datos.md` | si |
| :52 | Partición del Obj. 1: validación 8, prueba 34 | `experiments/objetivo1/EXPERIMENTOS.md`; BITACORA §2 2026-09-29 | si |
| :54 | 34 → 33; Δ máx. 2.3 HU; veredicto igual | #156; `p1_sin_0053.md` | si |
| :56-60 | 7 secundarios; paciente pre/post cirugía; cobertura de las auditorías | DEC 2026-10-11, 2026-10-11 (4); #163, #166 | si |
| :62 | 166 vol. = 159 pac.; 118/125, 8, 33; 20 + 13; 9/10/14; 59/41/66 | DEC 2026-10-11 (4); `docs/02-datos.md` | si |
| :64 | 103 → 91 → 72; 11 de 34; 7 de 57; +1 borde; 49 | `experiments/objetivo2/EXPERIMENTOS.md`; D-O2.2 | si |
| :66-68 | 30 casos 15 + 15; 20 de 30 (67 %); 10/15 y 10/15; 18 láminas/12 volumen; 7/5 | #132 (CERRADA) y su CSV | si |
| :70 | Cuatro funciones del metal; 3 pacientes con fuste de HU bajos | DEC 2026-09-11; #155 | si |
| :74 | Exploración previa del VAE sobre 178, por encima del criterio | #36/#39 (E6b) | si |
| :76-81 | VAE SD 1.5; 150 HU; MAE | `experiments/objetivo1/EXPERIMENTOS.md`; fichas `peters2025hybrid`, `haneda2025aapm` | si |
| :83 | 25 HU; 20.2; 12.3; 12.74 HU | DEC 2026-09-15 (2); fichas `karageorgos2024ddpm`, `yun2026simulationdriven` | si |
| :85 | 2 × 3 combinaciones; ventanas [-1000, 2000], [-320, 480], [-160, 240]; 20 000 HU; GAPDATO del ajuste | ficha `wang2025adaptiveweighting`; código del experimento | si |
| :87 | Media sobre 34 < 25 HU; IC 95 % por remuestreo; orden a priori | DEC 2026-09-17 (3) | si |
| :89 | $B_\delta$ de 12 mm desde el metal de 2500 HU; Rombach | ficha `rombach2022latentdiffusion` | si |
| :91 | Extensión a Guo et al.; cota por saturación | DEC 2026-09-19; ficha `guo2025maisi` | si |
| :95 | Zwingmann (dos series); Ziran 7-25 % y hasta 140 % | fichas `zwingmann2009navigated`, `ziran2007fluoroscopic` | si |
| :99 | Kaiser: 5 mm; lectura radial; 10 mm | ficha `kaiser2014dysmorphism`; DEC 2026-09-08 | si |
| :101 | Mediana 0.42 con 150 HU | `experiments/objetivo2/EXPERIMENTOS.md`; #48 | si |
| :103 | TotalSegmentator 2.18.0; 6/3 mm; 0.1 %; 104 estructuras | DEC 2026-09-14; fichas `wasserthal2023`, `isensee2021` | si |
| :105 | Cierre de 2 mm; relleno sin cambio en 72; 8 mm; GAPDATO del algoritmo | DEC 2026-09-14 (3)-(5); #131 | si |
| :107 | $D \geq d + 2\epsilon$; 1-2 mm; 6.3-8 mm; McLaren | DEC 2026-09-11 (2); fichas `kaiser2014dysmorphism`, `mclaren2021corridor` | si |
| :109 | 9.5 mm (7.4-11.7); 65.3 / 23.6 %; 62.5 / 20.8 %; 29 y 27 de 72; 5 % | `experiments/objetivo2/EXPERIMENTOS.md` | si |
| :111 | 16 revisados: 14 / 2 / 0; GAPDATO de la sensibilidad | #123, #131 | si |
| :115-119 | 69 de calibración frente a 66; 64 → 57 / 7 / 6; 48; 29; 17; 3; 61 de 61; 12 de 16 | #124, #136, #163 | si |
| :123, Tabla `tab:geometrias` | 6.5-8.0; 6.3-8; 4.91 + cabeza 8.0 × 4.5; 4.8; 4.9/4.7; 7.0; 7.3 | fichas `gardner2010safezones`, `kaiser2014dysmorphism`, `sayres2014comparison`, `synthes2003guide`, `gardner2015screw`, `zwingmann2009navigated` | si |
| :141 | 79 componentes de 43 volúmenes; ≥ 30 mm; ≤ 12 mm; 4.8 mm; 7.3/16 mm | E11; fichas `synthes2003guide`, `zhu2022optimalposition` | si |
| :143 | Cabeza 8.0/4.5 mm; supuesto sin avellanar; `\GAPDEC` de la cabeza | fichas `sayres2014comparison`, `doublemedical2021trauma`; DEC 2026-10-15 D2 | **no (T07)** |
| :147 | Arandela 1.5 mm; 316L y Ti-6Al-7Nb; fabricantes como documentación técnica | fichas `doublemedical2021trauma`, `synthes2003guide`; BITACORA §2 (P-EA1) | si |
| :151-160 | Preinscripción del 22-sep; ecuación de la pose | `experiments/objetivo2/preinscripcion_muestreador.md`; D-O2.7 | si |
| Tabla `tab:preinscripcion` | h 5.0; σ_t 2.5; σ_a 2.07° con L = 138 mm; 3σ; 50 poses; semilla 20260922 | `preinscripcion_muestreador.md` | si |
| :182 | ~95 % bajo 2σ; 4° de Zwingmann | `preinscripcion_muestreador.md`; ficha `zwingmann2009navigated` | si |
| :188 | 18 volúmenes: 13/4/1; 39/36/33 mm; GAPDATO; 69 de 72 | #121; `experiments/objetivo2/EXPERIMENTOS.md` | si |
| :190-192 | Densidad retirada; Arand; Gardner y el fenotipo | DEC 2026-10-08 B; fichas `arand2019pelvicring`, `gardner2010safezones` | si |
| :196 | Inpainting 2.5D; asinh FP32 | `diseno_A.md` §0; DEC 2026-09-19 | si |
| :198 | Regla del suelo vigente; percentil 5; `\GAPDEC` de conversión a HU | DEC 2026-10-05:1593-1619; DEC 2026-10-15 D1 | **no (T03)** |
| :200 | Sustitución de ControlNet | ficha `zhang2023controlnet`; DEC 2026-09-19 | si |
| :202 | Predicción $v$; $\sigma_t^2 = 1 - \alpha_t^2$; dominio de imágenes naturales | ficha `salimans2022progressive` (filas de evidencia; z_t retirada en r20) | si |
| :204 | U-Net 64 (1, 2, 4, 8); coseno 1000; AdamW 1e-4; 256; 50 pasos DDIM | `diseno_A.md`; fichas `song2021ddim`, `lugmayr2022repaint`, `zhang2025lefusion` | si |
| :204 | Lote 16 con `\GAPDEC` (registro de lote 4) | DEC 2026-10-15 D3 | **no (T08)** |
| :206 | 5 semillas; GPU del mismo tipo; E-A1 en porción compartida | DEC 2026-10-08 (3); #151, #170, #174 | si |
| :208-210 | Rampa 0.01/0.05; recalibración 0.030 / 0.05 | DEC 2026-10-07; #152, #172 (A) | si |
| :212 | 12 mm; 7.57 / 11.45 / 11.63 / 54.82 / 57.69 HU; factores 1.4 / 1.8 / 0.7 / 0.5 | ficha `karageorgos2024ddpm`; `d1_d2_resultado.md` | si |
| :214 | Máscara de 2500 HU; `\GAPDEC` del semimáximo | DEC 2026-09-20 (2) D1; DEC 2026-10-15 D4 | **no (T09)** |
| :216 | Tres reglas; razón 0.62 (GAPDATO); 5 de 40 | DEC 2026-09-21; #109 | si |
| :218 | 14 182 / 39; 896 / 3; tres componentes retirados | DEC 2026-10-11; `docs/00-tesis.md`:121-123 | si |
| :220 | Modelos afectados; lo heredado; ninguna cifra afectada | #171; BITACORA §2 2026-10-11 | si |
| :222 | Control de pose: 5 %, -500 HU, 150 HU; 15 = 2 + 13 | #173 | si |
| :224 | Lo que se rehízo con la pose corregida; sonda no repetida | #173, #174 (c) | si |
| :226-228 | Desplazamientos de dominio; 0.62 frente a 1.40; 9 de 57; 4.91 mm | DEC 2026-09-21 (`01-decisiones.md`:1331-1333); #112 | si |
| :228 | `\GAPDEC` de la costura | DEC 2026-10-15 D5 | **no (T10)** |
| :230 | 60 000 pasos; mínimo en 16 500; dos candidatos | DEC 2026-10-11 (2)-(3); #168 | si |
| :232 | $D \geq 9$ mm; cremallera; 1.6 / 7.0 / 8.9 mm; `\GAPDEC` de 0066 | DEC 2026-10-09 (4); DEC 2026-10-15 D6 | **no (T11)** |
| :234-238 | 1 mm; 0-12 mm; 0.896 mm; anillo de 12-15 mm; agregación; dos tornillos de 0039 | DEC 2026-10-09; 2026-10-08 (2); #154 | si |
| :240 | 13 frente a 7 de 24; 9/3 y 4/4; 393 frente a 270 HU | `resultados_validacion_pose.md`:19-20 | si |
| :242 | 7 de 12 cáscaras; 3245/4856 y 3402/4848; 497/648 HU | `resultados_validacion_pose.md`:19-23 | si |
| :242 | 3465 y 5283 HU (medianas reales) | derivadas de `resultados_validacion_pose.md`:23 | **no (T25)** |
| :242 | `\GAPDEC` del mecanismo del p95 | DEC 2026-10-15 D7 | **no (T12)** |
| :244 | 1164/1163 frente a 1248/1182; Ti 1881/1287 | `resultados_validacion_pose.md`:42-44; #175 | si |
| :248 | Desenlace de la v1 y su causa | `resultados_prueba_v1.md`:14; DEC 2026-10-15 D15 | **no (T01)** |
| :248 | "Tal como estaba preinscrita"; v2 posterior | DEC 2026-10-13; DEC 2026-10-15 encabezado | **no (T04)** |
| :250-252 | 18 pacientes; 500-4000 mm³; 15-40 mm; 8-10 mm; 1930…174; 1697…-40 | `d1_d2_resultado.md`; #177 adenda | si |
| :254 | 2888 / 14 182; 0.2036; 45 comp. / 24 casos; 0.5; 3.91; peso 3 | `v2_d_componentes_run04.md`:8; DEC 2026-10-14 | si |
| :258-261 | Canal Γ; λ = 0.0847/mm; 11.80 mm; Park, Choi y Seo; Park, Hwang y Seo; Park et al. (`hyung2017ml`) | `b_piloto/b_resumen.md`:24; fichas; `referencias.bib`:503-504, 847-859 | si |
| :263 | Haz paralelo 2D; Xia et al.; convexidad estricta; Wang y Zou | fichas `park2017characterization`, `xia2024pndnet`, `wang2021streak`; #178 | si |
| :265 | GAPDATO del caso estrictamente convexo | #178, #181 | si (GAP justificado) |
| :265-269 | C0 0.0067/0.0902; C1 0.9 / 1.000 en 228 cortes; C2 0.116, p = 0.0085, n = 13; 0.133; 0.166; 0.114-0.119 | #181; `b_piloto/b_resumen.md`; DEC 2026-10-14 | si |
| :271 | 60 000; mínimo en 21 000; 0.0597 / 0.0596 / 0.0540; GPU | `EXPERIMENTOS.md`:41; curvas de run05 | si |
| :273-275 | Regla 20 % / 10 %; E 532.8 / 418.2 / 367.0; 284 / 540 / 233.0 / 279.6; 13 / 13 / 9; 4 HU | `run05/v2_eleccion.md`:8; #182; DEC 2026-10-14 (2) | si |
| :277 | Procedimiento exploratorio de la v2 y GAPDATO "en curso" | DEC 2026-10-14 (2); DEC 2026-10-15 D16, D-extra 3; #184 | **no (T24)** |
| :281 | El Obj. 4 sin fila; controles de SAP | `docs/00-tesis.md`; D-O2.3 | si |
| :285 | Dos componentes de SAP; $d$ = 7.0, $\epsilon$ = 1 → 9 mm | DEC 2026-10-08 B; D-O2.4 | si |
| :287-294 | Escala de Smith; ec. de la brecha; grados 0/2/4 mm; 8 mm; grado 3 sin descarte | ficha `smith2006iliosacral`; D-O2.3 | si |
| :296 | Seis controles (1 fantoma + 5); 0.083 mm | `preinscripcion_muestreador.md`; BITACORA §2 | si |
| :298 | 69/15/8/8 %; 40/37/11.5/11.5 % | ficha `zwingmann2009navigated` | si |
| :305 | 0.29 / 0.07 / 0.035 → W1 = 0.395; 26/24 y 35/32 | DEC 2026-10-08 (escala post hoc); ficha `zwingmann2009navigated` | si |
| :307-309 | 15 de 72; estratificación post hoc; restricción rechazada | `experiments/objetivo2/EXPERIMENTOS.md`; #125 | si |
| :315 | Métricas de Peters, 150 HU, 5 %, selección de ROIs y su limitación | ficha `peters2025hybrid` | si |
| :317 | Escala 0-4 no trasladada; `\GAPDEC` de la preservación del protocolo físico | DEC 2026-10-09 (8) punto 2; DEC 2026-10-15 D8 | **no (T13)** |
| :321 | 33 = 19 (9 + 10) + 14; 1.62 mm; 13 | DEC 2026-10-09 (8) punto 3; DEC 2026-10-11 (4) | si |
| :323-325 | Anillos de 360°; guarda de un vóxel; 12 mm; 8 mm; fracción en el suelo | DEC 2026-10-05 (3)-(4); `diseno_A.md`:69-77 | si |
| :327 | `\GAPDEC` de la pose; 3.1 / 3.6 / 4.7 mm; sensibilidad con n = 10 | DEC 2026-10-09 (8) punto 4; DEC 2026-10-15 D9 | **no (T14)** |
| :329 | 51 frente a 25 cortes (pose anterior); dominios por brazo | DEC 2026-10-09 (4) punto 1; `diseno_A.md`:72-73 | si (ver T22) |
| :333-335 | 19 → 13 (9 + 4); 500 / 10 mm³; 6 de `dataset6` sin componentes; 24 cortes; 15 h; errata | DEC 2026-10-09 (8) puntos 1 y 6; DEC 2026-10-11 (4) punto 3 | si |
| :337 | SDC y cambio de volumen; 150 / 2500 HU | DEC 2026-10-09 (8) punto 2 | si |
| :341 | Primario único; sin lector clínico; `\GAPDEC` del control visual | DEC 2026-10-05 (3); DEC 2026-10-15 D10 | **no (T15)** |
| :343 | Tres contrastes; cordura degenerada | DEC 2026-10-05 (3) punto 5; DEC 2026-10-15 D12 (comparador paramético ausente) | **no (T21)** |
| :347 | 5371 HU; 1 781 741 vóxeles; 14 182 / 39 | DEC 2026-10-11 (3) punto 5; `04-implicancias.md` (fila de a22 de run04) | si |
| :347-351 | CatSim/XCIST; AAPM; 900 columnas, 1000 vistas, 64; 138 mm; fractales; fantoma | fichas `deman2007catsim`, `wu2022xcist`, `haneda2025aapm`, `peters2025hybrid`; DEC 2026-10-05 (5) | si |
| :353 | Conversión (HU + 1000)/1000; pasos ausentes del artículo | #158; ficha `peters2025hybrid` | si |
| :355 | Cinco desviaciones; 459 mm; [0.5, 3]; `\GAPDEC` de la implicancia 158 | DEC 2026-10-05 (5); DEC 2026-10-15 D11 | **no (T16)** |
| :357 | Commits `4cf3544` / `4993e87`; BSD 3-Clause; parche local | `xcist2026main`, `xcist2025example` (r21) | si |
| :359-363 | Sonda: 72 h; ±20 HU; 2 %; triple; -2048 → -1000 HU; k = 2 | `sonda_peters.md`; DEC 2026-10-09 (2); #174 (c) | si |
| :365 | Fe/Ti; réplicas A/B; 2.5-10 mm; 4.91 mm; 13 pacientes | DEC 2026-10-09 (3), (5); ficha `peters2025hybrid` | si |
| :367 | Fe 5243 / 2166; Ti 1881 / 1287; difusor 1069-1361 y 1131-1232 HU | `resultados_validacion_pose.md`:42-45; #175 | si |
| :369-371 | Ti 2 de 24 frente a Fe 0 de 24; 22 de 24 por encima; 7036 / 4462 frente a 3092-3838 HU | `resultados_validacion_pose.md`:29-34; #174 | si |
| :375 | Wilcoxon de una cola, 0.05, n = 13; `\GAPDEC` del tamaño de efecto | DEC 2026-10-05 (3); DEC 2026-10-15 D12 | **no (T17)** |
| :377 | TOST frente a Ti; IC90; Δ = 196.3; n = 13; sensibilidades Fe / 60k / n = 10 | `diseno_A.md` §0; `resultados_validacion_pose.md`:51 | si |
| :377 | `\GAPDEC` de la implicancia 90 | #90 CERRADA; DEC 2026-10-15 D13 | **no (T18)** |
| :377 | `\GAPDEC` del supuesto de *t* | DEC 2026-10-15 D14 | **no (T19)** |
| :377 | `\GAPDEC` de los desenlaces | DEC 2026-10-15 D15 | **no (T02)** |
| :379 | Δ = max(s, r); s = 196.3; r = 6.1; Ti 8 y 27 HU | DEC 2026-10-09 (4); `resultados_validacion_pose.md`:51-54; DEC 2026-10-15 punto 21 | si |
| :381 | Estado final: s = 115.8; dos márgenes | `resultados_validacion_pose.md`:52; DEC 2026-10-11 (3) punto 4 | si |
| :375-381 | Lectura de acuerdo (Bland-Altman, Pitman-Morgan) | DEC 2026-10-15 punto 22 | **no (T23)** |
| :385-387 | Realismo: 1 mm, mediana y p95, histograma en $M$; regla de inclusión; GAPDATO de la lista | DEC 2026-10-09 (6)-(7) | si |
| :391 | Qué se fijó de antemano en el Obj. 3 | DEC 2026-10-15 (reglas de lectura posteriores para la v1) | **no (T04)** |
| Tabla `tab:diseno` | 2 × 3; 34; 72/49; 13 y 13 de 19; Δ = 196.3 | filas anteriores | si |
| :413 | Decisiones post hoc del Obj. 2; 11/34, 7/57, 91 | `experiments/objetivo2/EXPERIMENTOS.md`; DEC 2026-10-08 | si |
| :415 | 10/15 y 10/15; 7/15 frente a 2/15; p = 0.109 (Fisher, bilateral) | #132 | si |
| :417 | Fuga del Obj. 1; 32 pacientes; veredicto igual; extensión a Guo | `p1_sin_0072.md`; #166 | si |
| :419-433 | Lista post hoc del Obj. 3 | DEC 2026-10-15 (encabezado, regla general, D1-D16, D-extra 1-4, 22) | **no (T04; :419 también T03)** |
| :423 | 3 de 11; 9 tras el recuento; tornillo de 0006 | DEC 2026-10-09 (7); DEC 2026-10-11 (4) | si |
| :433 | Sentido conjunto; 196.3 frente a 115.8; `\GAPDEC` de la implicancia 162 | #162 (3); DEC 2026-10-15 D16 | **no (T20)** |
| :435 | Cobertura de las auditorías y efecto por objetivo | BITACORA §2 2026-10-11 (r17); #166 | si |
| :437 | GAPDATO de la envolvente y del techo de S1; 2 mm de Smith | ficha `smith2006iliosacral`; #136 | si (GAP justificado) |
| :439 | Tejwani: 2.5 / 5.0 mm, p = 0.3 | ficha `tejwani2014` | si |
| :441 | S1 nombrado solo en la serie convencional | ficha `zwingmann2009navigated` | si |
| :443 | GAPDATO de la estructura direccional (implicancia 176) | #176 (ABIERTA) | si (GAP justificado) |
| :445 | Más allá de 10 mm no se separa del nulo; placas no acotadas | `d1_d2_resultado.md`; #177 adenda | si |
| :447 | 19 de 39 casos con objeto no ortopédico | #167 | si |
| :449 | Lin et al.; Li et al.; problema mal planteado | fichas `lin2019`, `li2024` | si |
| :451 | El suelo pesa menos frente al protocolo físico (una ejecución local) | `04-implicancias.md`:10429-10452 (ampliación a #141 y #146) | si (dato) |
| :451 | Regla del suelo evaluada contra el primario, sin conversión a HU | DEC 2026-10-15 D1 | **no (T03)** |
| :453 | Brazos desplazados en sentidos opuestos; "lectura no fijada" | #174; `resultados_validacion_pose.md`; DEC 2026-10-15 D15 | **no (T02)** |
| :455 | Tile B/C; Reilly: 6 pelvis, 5-20 mm, 36-90 %; 20 de 30 | ficha `reilly2003effect`; #132 | si |
| :457 | 56 de CLINIC-metal sin tornillo transilíaco-transsacro; poses no cubiertas | #155, #165; DEC 2026-10-15 D9 | **no (T14, en lo de las poses)** |
| :459 | 26 y 35 tornillos; GAPDATO del remuestreo; séptimo candidato | ficha `zwingmann2009navigated`; DEC 2026-10-08 punto 18 | si |
| :461 | Δ en 2 pacientes; escala semilla frente a mediana; receptor con cremallera | DEC 2026-10-09 (4); #162 | si |
| :463 | Cortes distintos por brazo; "el diseño no evalúa" | DEC 2026-10-15 D-extra 1 | **no (T22)** |
| global | Delta 163.8 / 23.2 / 100.3, 188.7, 5373, "12 de 24" en el `.tex` | grep sobre `overleaf/secciones/` | si (ausentes) |
| global | Fuentes de contenido frente a la DEC 2026-10-15 | `diseno_A.md`:29-33; `00-tesis.md`:91, :174, :186-188, :319-321; `EXPERIMENTOS.md`:39-40; `resultados_prueba_v1.md`:27 | **no (T05, T06)** |
| global | Claves `\cite`, E-F3 y primeros autores (Park et al. = `hyung2017ml`; Wang y Zou; Salimans y Ho) | `overleaf/referencias.bib`:503-504, 847-859, 995, 1249-1250 | si |
| global | Fabricantes como documentación técnica (P-EA1) | `:147` | si |
| global | Contenido retirado (Dice/HD95, latente/ControlNet, 31-60 %, BFC/ISC) | `docs/00-tesis.md`; búsqueda en el `.tex` | si (solo como exclusión o método sustituido) |
| global | Cifras de implicancias ABIERTAS #185/#186 (CV, r, 184 HU, ~1 %) fuera del texto | búsqueda en el `.tex` | si |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una DEC nueva cierra en bloque varios `\GAPDEC` y ninguno se retira | OC-2, G-T4 | `\GAPDEC{... lotes de 4, pero el entrenamiento usó lotes de 16}` | PAT-19 |
| La lista post hoc y las fórmulas de integridad no recogen las reglas fijadas tras ver la prueba | G-C7, G-T4 | "La corrida final de la versión 1 se evaluó tal como estaba preinscrita" | PAT-13, PAT-140 |
| Desenlace de una prueba de equivalencia atribuido a la exclusión del cero en vez de a los límites del margen | G-T4, E-P3 | "no se concluyó equivalencia ..., porque el intervalo ... entero por debajo de cero" | nuevo |
| Una frase de amenazas niega una lectura o sensibilidad que una DEC posterior ya fija | G-T4, OC-3 | "la lectura de ese desenlace no está fijada" | PAT-116 |
| Fuentes de contenido (diseño congelado, `00-tesis.md`, `EXPERIMENTOS.md`) quedan detrás de la DEC | G-T4, OC-5 | `diseno_A.md`: "`Delta`: principal 163.8 HU (... `r` = 23.2)" | PAT-138, PAT-158 |
| Cifra resumen calculada por el redactor (mediana de dos valores) sin estar en la fuente | G-T4 | "medianas de 3465 y 5283 HU en los dos tornillos reales" | nuevo |

**Conteo: alta=6 media=18 baja=1**
