# Propuesta del asesor sobre las 18 marcas `\GAPDEC` — 2026-10-14

> Lo escribe Claude en rol de asesor senior, a pedido de la autora. **No es una decision**: las decisiones son de la
> autora (regla 3 y 14 de `CLAUDE.md`). No se edito ningun `.tex`, ni `docs/01-decisiones.md`, ni `docs/00-tesis.md`,
> ni `tesis/main.tex`. Los textos "para el .tex" son propuestas para pegar con `/ciclo-redaccion` o a mano; los textos
> "para DEC" son propuestas para que la autora los pegue en `docs/01-decisiones.md`.
>
> Fuentes leidas: `CLAUDE.md`, `overleaf/CLAUDE.md`, `docs/ESTADO.md` (bloques 2026-10-13 a 2026-10-14 (3)),
> `docs/00-tesis.md`, `docs/01-decisiones.md` (2026-10-05 a 2026-10-14 (2)), `docs/04-implicancias.md` (#90 y su
> actualizacion, #157, #158, #162), `redaccion/MAPA.md` (tabla de GAP), `experiments/objetivo3/diseno_A.md`,
> `v2_plan.md`, `resultados_prueba_v1.md`, `d1_d2_resultado.md`, `a10_costura.py`, `a25_html_sintesis.py`.

## Criterio general que aplico

1. **Lo que se ejecuto manda sobre lo que se previo.** Si el diseno congelado (`diseno_A.md` §0) y su codigo hicieron
   algo distinto de una decision anterior, no se rehace nada: se declara la diferencia y, si era un error de registro,
   se corrige el registro.
2. **Nada que se decida hoy sobre el TOST de la version 1 es preinscrito**: el resultado ya se conoce (#177:
   diferencia media -301.0 HU, IC90 [-477.0, -124.9], `Delta` 196.3 HU, no se concluye equivalencia). Toda regla de
   lectura nueva se declara posterior. **Pero la version 2 aun no tiene `a20`/`a24` en prueba** (ESTADO 2026-10-14
   (3): `a20_v2.sbatch` espera a 56791/56792). Si las reglas de lectura se escriben en DEC **antes** de lanzar
   `a20_v2`, son previas para el analisis exploratorio. Esto es lo que vuelve urgente el bloque del TOST.
3. **No anadir analisis nuevos sobre prueba salvo que sean baratos, descriptivos y no puedan rescatar el resultado.**
   Con plazo corto y sin medico, cada analisis anadido despues del congelamiento es una pregunta mas del jurado.
4. **Ninguna cifra fuera del repositorio.** Las que aparecen abajo estan en las fuentes citadas al lado.

## Inventario (18 marcas, 16 decisiones distintas)

| ID | Archivo:linea | Texto de la marca (abreviado) | Decision |
|---|---|---|---|
| G01 | `introduccion.tex:90` | si la comparacion de equivalencia frente al protocolo fisico se mantiene o pasa a trabajo futuro, contingencia de plazo registrada por la autora | D-A (#90) |
| G02 | `capitulo1.tex:128` | (mismo texto que G01) | D-A (#90) |
| G03 | `capitulo3.tex:143` | la decision registrada sobre la geometria de sintesis fija un cilindro uniforme y deja la cabeza como variante de sensibilidad, pero las generaciones del Objetivo 3 rasterizan el tornillo con cabeza: falta decidir si la cabeza se adopta como parte de $M$ o se declara como desviacion | D-B |
| G04 | `capitulo3.tex:198` | como se expresa en HU la perdida de la regla del suelo para compararla con $\Delta$, y que consecuencia tiene una perdida mayor ahora que el diseno congelado fija la representacion | D-C |
| G05 | `capitulo3.tex:202` | la decision registrada que fija la arquitectura da lotes de 4, pero el entrenamiento uso lotes de 16: falta corregir ese registro o declarar la diferencia como desviacion | D-D |
| G06 | `capitulo3.tex:212` | si la mascara de entrenamiento por semimaximo local se entrena y reporta como sensibilidad o se retira | D-E |
| G07 | `capitulo3.tex:226` | si el salto en el borde de $G$ se mide tambien en la sintesis sobre pelvis sin metal y para los dos brazos que generan artefacto | D-F |
| G08 | `capitulo3.tex:230` | si el paciente de validacion con un objeto en el borde del campo de vision (corredor 8.9 mm) cuenta como paciente sin metal o en el grupo 2 | D-G |
| G09 | `capitulo3.tex:240` | mecanismo del sesgo del percentil 95: hipotesis sin verificar sobre los techos de los canales estrechos (implicancia 157) | D-H |
| G10 | `capitulo3.tex:315` | si la preservacion del protocolo fisico se mide con RMSE y SSIM contra la TC original y sobre que region | D-I |
| G11 | `capitulo3.tex:325` | razon para evaluar el sintetizador sobre el eje del corredor sin perturbar y no sobre las poses del muestreador | D-J |
| G12 | `capitulo3.tex:339` | tamano y regla de seleccion de la muestra de casos sintetizados que revisa la autora | D-K |
| G13 | `capitulo3.tex:353` | si el repositorio del desafio AAPM se cita como fuente de la implementacion del protocolo fisico, y en que forma (implicancia 158) | D-L |
| G14 | `capitulo3.tex:373` | si la prueba de cordura reporta un tamano de efecto con su IC, y con que medida | D-M |
| G15 | `capitulo3.tex:375` (1.a) | cierre formal de la contingencia de plazo (implicancia 90): la comparacion ya se ejecuto como contraste primario | D-A (#90) |
| G16 | `capitulo3.tex:375` (2.a) | supuesto distribucional del IC con *t* sobre 13 diferencias pareadas | D-N |
| G17 | `capitulo3.tex:375` (3.a) | que desenlace del TOST cuenta como evidencia en contra del sintetizador y cual como no concluyente | D-O |
| G18 | `capitulo3.tex:431` | si se reporta la prueba de equivalencia con un margen no fijado por el sintetizador como sensibilidad descriptiva (implicancia 162) | D-P |

---

## D-A — Contingencia de plazo del TOST frente a Peters (G01, G02, G15)

- **(a) Que falta decidir:** cerrar formalmente la contingencia de #90 y declarar que la equivalencia frente a Peters
  se mantiene como contraste primario (no pasa a trabajo futuro).
- **(b) Contexto:** #90 ACTUALIZACION 2026-09-21: "no se corta nada por ahora [...] El recorte de arriba queda como
  contingencia declarada, a aplicar solo si el plazo lo obliga". DEC 2026-10-08 (i) lo dejo fuera de la delegacion
  porque "depende del plazo real". Desde entonces el TOST se congelo como primario (DEC 2026-10-09 (6) pto 2) y **ya
  se ejecuto en prueba** (`resultados_prueba_v1.md`, #177). DEC 2026-10-13 pto 3: "la comparacion principal frente a
  Peters" se mantiene en la version 2. ESTADO 2026-10-14 (3): la redaccion escalo esto como T05.
- **(c) Opciones:** (1) cerrar #90: el TOST queda como primario y se borra "segun el plazo"; (2) mantener la
  contingencia abierta; (3) aplicar el recorte y pasar el TOST a trabajo futuro.
- **(d) Recomendacion: (1).** La contingencia era para el caso de no llegar; se llego. Mantenerla abierta deja en el
  documento la posibilidad de retirar un contraste primario **despues de conocer que no concluyo equivalencia**, que
  es exactamente lo que un jurado lee como seleccion del resultado. La opcion (3) seria hoy indefendible por el mismo
  motivo. Costo: cero.
- **(e) Se resuelve YA** (solo decision y redaccion).
- **(f) Texto propuesto.**
  - `introduccion.tex:90`, en lugar de "y su comparacion [...] depende del plazo \GAPDEC{...}":
    > y su comparación de equivalencia frente al protocolo físico, prevista desde el diseño como contraste primario, se ejecutó como tal.

    Nota: el `\GAPDATO` contiguo de esa misma linea ("no existe aun resultado del Objetivo 3 porque el modelo final no
    esta elegido") esta desfasado (PAT-122): `capitulo3` §Vision general ya dice que la corrida final se ejecuto.
    Alinearlo en la misma pasada.
  - `capitulo1.tex:128`, sustituir "y aun sin preinscribir (Seccion~\ref{sec:apariencia}) \GAPDEC{...}" por:
    > fijado sobre validación (Sección~\ref{sec:apariencia}).

    ("aun sin preinscribir" tambien esta desfasado: `Delta` = 196.3 HU, `resultados_validacion_pose.md` §3.)
  - `capitulo3.tex:375`, quitar la marca y dejar:
    > [...] entre el sintetizador y el protocolo físico con titanio. Es el contraste primario del Objetivo~3 y se ejecutó como tal.
  - Fuera de las marcas, misma decision: `introduccion.tex:56` y `capitulo2.tex:106` dicen "segun el plazo" (y "sobre
    las poses del muestreador", ver D-J). Alinear en la misma ronda.
  - **Para DEC:**
    > **2026-10-1X — Cierre de la contingencia de plazo de #90.** La comparación de equivalencia (TOST) frente al
    > protocolo físico de Peters se mantiene como contraste primario del Objetivo 3. Se ejecutó con la versión 1
    > (#177) y sigue siendo la comparación principal en la versión 2 (2026-10-13 pto 3). La contingencia del
    > 2026-09-21 (pasarla a trabajo futuro si el plazo lo obligaba) queda retirada. #90 pasa a CERRADA.

## D-B — Cabeza del tornillo en $M$ (G03)

- **(a)** Decidir si la cabeza (8.0 x 4.5 mm) es parte de la geometria de sintesis o una desviacion de D3.
- **(b)** D3 (DEC 2026-09-20 (2); `diseno_A.md` §8 bis D3): "Cabeza y rosca: como sensibilidad, no en el piloto". Pero
  el diseno congelado (`diseno_A.md` §0, "Tornillo: cilindro de 4.91 mm con cabeza, como en `a11`/`a15` (D3)") y el
  codigo (MAPA, fila de la cabeza: `a15_cadena_completa.py`:298-299, `a11_rasterizar_tornillo.py`:87-88) generan con
  cabeza. `00-tesis.md`:91 repite la version de D3 ("con cabeza y rosca de 7.3 mm como sensibilidad").
- **(c)** (1) adoptar la cabeza como parte de $M$ por el congelamiento, declarando que sustituye a D3; (2) declararla
  desviacion de D3 sin adoptarla; (3) regenerar sin cabeza.
- **(d) Recomendacion: (1).** El congelamiento es posterior a D3, se hizo antes de tocar prueba y su §0 "manda sobre
  todo lo que sigue". La geometria con cabeza esta respaldada por fuente (Sayres et al.) y es mas fiel a un tornillo
  real; la "desviacion" es solo un error de atribucion ("como en ... (D3)"). Regenerar (3) rehace cotejo, `Delta` y
  corrida final: inaceptable en plazo y sin motivo. La variante sin cabeza queda como sensibilidad no programada, en
  la misma frase que ya lista rosca, arandela y canulacion.
- **(e) YA.**
- **(f)** `capitulo3.tex:143`:
  > Todas las generaciones del Objetivo~3 sintetizan el tornillo con esa cabeza, sin arandela y macizo. Así lo fija el diseño congelado, que en este punto sustituye a la decisión anterior que dejaba la cabeza como variante de sensibilidad; el cambio es anterior a cualquier generación sobre la partición de prueba.

  Y en la oracion siguiente: "La rosca, la arandela, la canulacion **y la variante sin cabeza** no entran en la
  corrida final [...]".
  - **Para DEC:** "2026-10-1X — Geometria de sintesis: la cabeza (8.0 x 4.5 mm, sin avellanar) es parte de $M$, como
    fija `diseno_A.md` §0 (2026-10-09). Sustituye a D3 (2026-09-20 (2)) en ese punto; la variante sin cabeza queda
    como sensibilidad no programada. Alinear `00-tesis.md`:91."

## D-C — Regla del suelo de -1000 HU (G04)

- **(a)** Decidir que se hace con una regla preinscrita que, tal como se escribio, no puede evaluarse.
- **(b)** DEC 2026-10-05 ptos 2-4: la perdida es una fraccion del vano (sin unidad) y se compara con `Delta` (HU); si
  es mayor, "se cambia la representacion". DEC 2026-10-08 pto 12 fija que se evalua contra el contraste primario. Pero
  `diseno_A.md` §0 congela `pub+asinh`, y la version 2 la mantiene (`v2_plan.md` §0 "No cambia"). MAPA, fila del suelo:
  escalado desde capitulo3-r10. Ademas existe un indicador preinscrito de censura: la fraccion de la ROI en el suelo
  (DEC 2026-10-05 (3) pto 3), que ya se reporto en prueba (`resultados_prueba_v1.md`:24-25).
- **(c)** (1) convertir la fraccion a HU (multiplicarla por el vano de cada paciente) y evaluar la regla; (2) declarar
  la regla no evaluable tal como se escribio, constatar que sus dos ramas llevan hoy al mismo desenlace (limitacion de
  alcance) y remitir el efecto real al indicador de censura preinscrito; (3) cambiar la representacion.
- **(d) Recomendacion: (2).** (1) exige inventar ahora una conversion que no se preinscribio, despues de conocer
  `Delta` y el resultado: cualquier eleccion seria post hoc y el jurado puede preguntar por que esa y no otra. (3) es
  imposible en plazo. (2) es lo honesto y lo mas facil de defender: la rama "cambiar" ya no existe, asi que la regla
  solo puede terminar en "limitacion"; y lo que el jurado quiere saber (si el suelo afecta al endpoint primario) lo
  responde una cifra preinscrita que ya existe. Se reconoce el defecto de diseno como tal.
- **(e) YA.** La cifra del indicador va al cap. 4, no al cap. 3.
- **(f)** `capitulo3.tex:198`, en lugar de la marca:
  > Tal como se escribió, la regla no es evaluable, y se declara así. Como su segunda rama ya no puede aplicarse, cualquiera de sus desenlaces deja el suelo como limitación de alcance, y así se trata. Su efecto sobre el criterio primario se lee en el indicador de censura preinscrito, la fracción de vóxeles de la región de medición que cae en el suelo, que se reporta por paciente (Sección~\ref{sec:ap-sintesis}).
  - **Para DEC:** "2026-10-1X — Regla del suelo (2026-10-05 ptos 2-4): no evaluable tal como se escribio (compara
    una fraccion con un margen en HU sin conversion preinscrita, y su rama 'cambiar la representacion' quedo anulada por
    el congelamiento). No se fija una conversion despues de ver `Delta`. El suelo se declara limitacion de alcance; su
    efecto sobre E-A2 se lee en la fraccion de la ROI en el suelo (2026-10-05 (3) pto 3)."

## D-D — Lote de entrenamiento 4 frente a 16 (G05)

- **(a)** Corregir el registro (errata) o declarar desviacion.
- **(b)** DEC 2026-10-08 A.3 congela la arquitectura "tal como corrio" con lote 4; `a7_entrenar.sbatch`:60 y los
  metadatos de los checkpoints dan 16 (#148, #162 (1); el 4 era del piloto, #134). `v2_plan.md` §1: run05a/b con
  "mismos hiperparametros".
- **(c)** (1) errata fechada en DEC: el valor es 16; (2) declarar desviacion.
- **(d) Recomendacion: (1).** A.3 quiso registrar lo que corrio; lo que corrio esta en los metadatos. Llamarlo
  "desviacion" sugiere que algo se cambio respecto de un plan, y no fue asi: fue un error al copiar el valor.
- **(e) YA.**
- **(f)** `capitulo3.tex:202`: quitar la marca y dejar "lotes de 16". Sin mas texto.
  - **Para DEC:** "2026-10-1X — Errata de 2026-10-08 A.3: el tamano de lote del entrenamiento es 16, no 4 (4 era el
    del piloto, #134). Fuente: `a7_entrenar.sbatch`:60 y `meta` de los checkpoints (#148). Vale para run04, run05a y
    run05b."

## D-E — Sensibilidad con mascara por semimaximo local (G06)

- **(a)** Entrenar y reportar la sensibilidad, o retirarla.
- **(b)** D1 (DEC 2026-09-20 (2); `00-tesis.md` "Pendiente de decision", DECIDIDO 2026-09-20): semimaximo como
  sensibilidad. `diseno_A.md` §0 no la programa.
- **(c)** (1) retirarla y declararla trabajo futuro; (2) entrenarla (reextraer parches, reentrenar, regenerar,
  reevaluar).
- **(d) Recomendacion: (1).** (2) es otra corrida completa de 60 000 pasos mas toda la cadena, en plazo corto y
  despues de ver prueba. El desplazamiento de dominio que la sensibilidad iba a medir ya se cuantifica con lo medido
  (E8: 9 de 57 fragmentados; E11: 4.91 mm; DEC 2026-10-08 A.6), y eso esta escrito en el parrafo siguiente.
- **(e) YA.**
- **(f)** `capitulo3.tex:212`:
  > La decisión que fijó esa máscara preveía el semimáximo local por objeto como sensibilidad. Esa sensibilidad se retira y queda como trabajo futuro: exigiría extraer de nuevo los parches y reentrenar, y el diseño congelado no la programa. La diferencia entre la máscara umbralizada y el cilindro de síntesis se cuantifica con lo ya medido (párrafo siguiente).
  - **Para DEC:** "2026-10-1X — Se retira la sensibilidad de mascara por semimaximo local (D1, 2026-09-20 (2)); no
    la programa `diseno_A.md` §0. Trabajo futuro."

## D-F — Salto en el borde de $G$ en la sintesis sobre pelvis sin metal (G07)

- **(a)** Medir la costura tambien en E-A2 (como fijaba DEC 2026-10-08 A.7) o declarar que no se mide donde actua.
- **(b)** DEC 2026-10-08 A.7: "se mide con `a10_costura.py` [...] en E-A2, para los dos brazos, descriptiva y sin
  umbral". `diseno_A.md` §0 solo la mide en E-A1 (`resultados_prueba_v1.md`: "exceso costura" 6.3 y 9.0 HU por
  grupo). Es justo el segundo desplazamiento de dominio (contexto con rayas frente a pelvis limpia), que actua en
  E-A2. `a10_costura.py` ya existe y su lectura es "exceso = salto compuesta - salto original"; en E-A2 la TC original
  limpia es la referencia exacta.
- **(c)** (1) correr `a10` sobre las salidas de E-A2 ya generadas, para el sintetizador (y para el protocolo fisico
  como referencia, si sus cortes reconstruidos estan en disco), descriptivo; (2) declarar que no se mide.
- **(d) Recomendacion: (1).** Es la unica marca donde recomiendo medir: es barato (CPU local, script existente, sin
  GPU ni prueba nueva), estaba decidido antes del congelamiento, y deja sin respuesta una pregunta obvia del jurado
  ("¿se ve el borde de la region generada en la tarea real?"). Es descriptivo y sin umbral, asi que no puede cambiar
  el resultado primario. Se declara como restitucion de A.7 posterior al congelamiento. Para el protocolo fisico el
  borde de $G$ no es una costura (simula la imagen entera): su salto sirve solo de referencia de cuanto salto "fisico"
  hay a 12 mm. Si sus cortes no estan guardados, medir solo el sintetizador y decirlo.
- **(e) Depende de una corrida** (barata, local). Para los tres modelos de la version 2, correrlo junto con `a20_v2`.
- **(f)** `capitulo3.tex:226`, en lugar de la marca:
  > Ese salto se mide también en la síntesis sobre pelvis sin metal, con la misma definición y para el sintetizador, y en el protocolo físico como referencia, como fijaba una decisión anterior al congelamiento que este no recogió. Se añade después de conocer los resultados de prueba, es descriptivo y no tiene umbral.

  Hasta tener la cifra, cambiar la marca por `\GAPDATO{salto en el borde de $G$ en la síntesis sobre pelvis sin metal}`.
  La frase siguiente ("Fuera de ella solo hay una medicion, sobre un caso [...]") se retira cuando exista la medicion.
  - **Para DEC:** "2026-10-1X — Se restituye 2026-10-08 A.7: la costura (`a10_costura.py`) se mide en E-A2 sobre
    las salidas ya generadas (sintetizador; protocolo fisico como referencia si hay cortes), descriptiva y sin umbral.
    Posterior al congelamiento y a la evaluacion de prueba; se declara."

## D-G — `CLINIC_0066`: sin metal o grupo 2 (G08)

- **(a)** Que fuente manda para clasificar el paciente de validacion de corredor 8.9 mm.
- **(b)** DEC 2026-09-21 (2) e #105: "no lleva metal"; `grupos.csv`:67 y `ts_nivel_s1.csv`:64: grupo 2, objeto no
  ortopedico en el borde del FOV, `incierto` (#162 (2)). No cambia los receptores de `Delta` (queda fuera por
  corredor < 9 mm).
- **(c)** (1) manda `grupos.csv` (auditoria posterior y mas especifica); (2) manda DEC; (3) redaccion neutra.
- **(d) Recomendacion: (1) con redaccion que no dependa de la eleccion.** El parrafo habla de pelvis **sin
  osteosintesis**, categoria que `0066` cumple en las dos fuentes (y `0102`, receptor, ya lleva una cremallera). Usar
  `grupos.csv` es la opcion conservadora (no afirma ausencia de un objeto que la auditoria vio) y coincide con el resto
  del cap. 3, que ya usa `grupos.csv`. DEC se alinea con una nota.
- **(e) YA.**
- **(f)** `capitulo3.tex:230`, tras "1.6, 7.0 y 8.9~mm":
  > La de 8.9~mm lleva, según la auditoría por grupos, un objeto no ortopédico de clasificación incierta en el borde del campo de visión, de modo que se cuenta en el grupo~2; como no tiene osteosíntesis, pertenece igualmente a las pelvis de validación sin osteosíntesis.
  - **Para DEC:** "2026-10-1X — `CLINIC_0066` (validacion) se clasifica por `grupos.csv` (grupo 2, objeto no
    ortopedico en el borde del FOV, incierto). Corrige 2026-09-21 (2) en ese punto. No cambia los receptores de
    `Delta`."

## D-H — Mecanismo del sesgo del p95 (G09)

- **(a)** Verificar la hipotesis o declararla como no verificada.
- **(b)** #157 y DEC 2026-10-09 (2) pto 4: "Hipotesis de mecanismo, sin verificar [...] los techos de los canales
  estrechos"; "Diagnostico posible, no programado". El sesgo se declara y no bloquea.
- **(c)** (1) declararla en prosa como hipotesis no verificada; (2) correr el diagnostico (fraccion de voxeles junto
  a los techos).
- **(d) Recomendacion: (1).** No es una decision pendiente sino una incognita declarada; el `\GAPDEC` sobra. El
  diagnostico no esta programado y no cambia ninguna conclusion. Ademas D1/D2 (#176) ya documentan un defecto mas
  grande del mismo signo (el artefacto sintetico se apaga hacia 6 mm), que es lo que importa en la discusion.
- **(e) YA.**
- **(f)** `capitulo3.tex:240`:
  > Su causa no está establecida. Una hipótesis, que este trabajo no verifica, es que el modelo aprenda mal la cola alta cerca de los techos de los canales estrechos de la codificación multiventana.
  - DEC: no hace falta (ya esta en 2026-10-09 (2) pto 4).

## D-I — Preservacion fuera de $G$ del protocolo fisico (G10)

- **(a)** Medir RMSE/SSIM del protocolo fisico frente a la TC original, y sobre que region, o declarar que no se mide.
- **(b)** `tesis/main.tex`:102 la preve sobre el complemento de $B_\delta$ (que incluye $M$); `diseno_A.md` §7 E-A3
  (historico) "fuera de $G$"; §0 y los scripts de la corrida final no la incluyen. El sesgo sin metal del brazo
  fisico ya tiene control (sonda, criterio V2: +/-20 HU, DEC 2026-10-09 (2); simulacion sin metal, §Brazos).
- **(c)** (1) declarar no medida y corregir la region; (2) medirla ahora fuera de $G$, descriptiva.
- **(d) Recomendacion: (1).** La preservacion no es un endpoint: para el sintetizador vale por construccion y para el
  protocolo fisico el control sin metal ya responde la pregunta relevante (si la simulacion altera la anatomia). Medir
  ahora anade un analisis post hoc sin valor de decision. Lo que si hay que arreglar es la region: el complemento de
  $B_\delta$ incluye $M$ y no tiene sentido.
- **(e) YA.**
- **(f)** `capitulo3.tex:315`, en lugar de la marca:
  > La preservación del protocolo físico no se mide con RMSE ni SSIM: no es un criterio del diseño congelado, y los cambios fuera de $G$ quedan acotados por la simulación sin metal. Si se midiera, la región sería el exterior de $G$, y no el complemento de $B_{\delta}$, que incluye $M$.
  - **Para DEC:** "2026-10-1X — E-A3 para el protocolo fisico: no se mide; el control es la simulacion sin metal. La
    region 'complemento de $B_\delta$' de `tesis/main.tex`:102 es incorrecta (incluye $M$): la region correcta seria
    fuera de $G$."

## D-J — Por que el eje sin perturbar y no las poses del muestreador (G11)

- **(a)** Registrar la razon de una exclusion que el diseno congelado solo enumera.
- **(b)** `diseno_A.md` §0, "Lo que NO entra": "poses perturbadas del muestreador", sin razon. Elementos con respaldo
  en el repositorio: el protocolo fisico "necesita simular proyecciones por pose" (DEC 2026-10-08 pto 25) y su coste
  ya obligo a submuestrear cortes (k = 2, DEC 2026-10-09 (3) pto 2); `Delta` se midio sobre esa pose en `0101`/`0102`
  (DEC 2026-10-09 (4)); la validez de la colocacion es objeto del Obj 2 (cap. 3, misma linea).
- **(c)** (1) declarar la razon ahora como articulacion posterior de una eleccion previa a prueba; (2) dejar la
  exclusion sin razon y solo la consecuencia en amenazas; (3) correr la sintesis sobre poses del muestreador.
- **(d) Recomendacion: (1).** La eleccion se hizo antes de tocar prueba, asi que no es seleccion por resultado; lo que
  falta es escribir el por que, y las tres razones estan en el registro. (3) duplica el coste de Peters y exige otro
  `Delta`. Hay que declarar que la razon se escribe despues.
- **(e) YA.**
- **(f)** `capitulo3.tex:325`:
  > La razón es aislar la apariencia de la variabilidad de la colocación, que evalúa el Objetivo~2: con una pose común, la diferencia entre brazos no mezcla el artefacto con la pose. Además, el protocolo físico exige simular proyecciones para cada pose, y el margen $\Delta$ se midió con esa misma pose en validación. El diseño congelado registró la exclusión sin su razón; la razón se declara aquí, y su consecuencia, que los resultados del Objetivo~3 no cubren las poses del muestreador, en la Sección de amenazas.

  Alinear `introduccion.tex`:56 y `capitulo2.tex`:106, que dicen "sobre las poses del muestreador": debe decir "sobre
  el eje del corredor medido".
  - **Para DEC:** "2026-10-1X — Razon (declarada despues del congelamiento, eleccion previa a prueba) de evaluar el Obj
    3 en el eje del corredor sin perturbar: aislar apariencia de colocacion; coste del protocolo fisico por pose;
    `Delta` medido en esa pose."

## D-K — Muestra del QC visual de la autora (G12)

- **(a)** Fijar tamano y regla de la muestra de E-A4.
- **(b)** `diseno_A.md` §7 E-A4: "muestra fija", "Laminas con el mismo formato de las de E9-TS". DEC 2026-10-08 pto
  9: QC como control, no evaluacion. En la practica la autora reviso los HTML de `a25` (ESTADO 2026-10-12;
  `v2_plan.md` §0), que generan por paciente cortes sagital, coronal y axial por el centro de $M$, con semilla 0 por
  omision (`a25_html_sintesis.py`:107).
- **(c)** (1) declarar como muestra lo que efectivamente se reviso (todos los pacientes de E-A2, semilla 0, cortes
  de `a25`), con la regla fijada despues; (2) definir otra muestra y repetir la revision; (3) retirar E-A4.
- **(d) Recomendacion: (1),** con la confirmacion de la autora de que reviso esos casos y semilla. Es honesto,
  no cuesta tiempo y es una muestra exhaustiva (todos los pacientes), que es mas solida que un submuestreo. La
  comparacion visual a ciegas de la version 2 (D3, `v2_plan.md` §1 pto 5) es otra cosa y se describe aparte.
- **(e) YA** (solo confirmar que casos y semillas reviso).
- **(f)** `capitulo3.tex:339`:
  > La muestra son los 13 pacientes de la síntesis sobre pelvis sin metal, con la semilla~0, en cortes sagital, coronal y axial por el centro de $M$, generados por la herramienta de inspección del sintetizador. La regla se fijó después de la revisión y se declara así.
  - **Para DEC:** "2026-10-1X — E-A4: la muestra del QC visual son los 13 pacientes de E-A2, semilla 0, cortes de
    `a25` por el centro de $M$; regla escrita despues de la revision; control, no evaluacion."

## D-L — Cita del repositorio AAPM (G13)

- **(a)** Citar el repositorio del desafio AAPM como fuente de la implementacion, junto a Peters como fuente del
  protocolo.
- **(b)** #158 (ABIERTA): el PDF de Peters no da la conversion HU -> fantoma ni como entra el metal; lo fija el
  repositorio (`(HU+1000)/1000`, realce de frecuencias). Opcion (1) de #158. MAPA ya tiene un `\GAPLIT` para la
  referencia del repositorio (revisiones `4cf3544` y `4993e87`); la regla 9 impide crear la entrada sin raw.
- **(c)** (1) citarlo, con entrada nueva desde `refs/raw/`; (2) mencionarlo en prosa sin cita; (3) no mencionarlo.
- **(d) Recomendacion: (1).** El jurado debe poder reproducir el brazo fisico; atribuir al articulo lo que no esta en
  el articulo seria inexacto. Citar el codigo junto al articulo es practica normal. La unica tarea es de la autora:
  pegar el raw de la cita del repositorio en `refs/raw/` (la regla 9 lo exige; Claude no puede crearla).
- **(e) YA como decision;** la cita queda como `\GAPLIT` hasta que exista el raw.
- **(f)** `capitulo3.tex:353`, en lugar de la marca:
  > Lo que el artículo no especifica, la conversión de la TC en fantoma y el realce de frecuencias, se toma del repositorio público del desafío AAPM, que se cita como fuente de la implementación, junto a Peters et al. como fuente del protocolo \GAPLIT{entrada bibliográfica del repositorio del desafío AAPM, con las revisiones usadas}.
  - **Para DEC:** "2026-10-1X — #158 opcion (1): el repositorio del desafio AAPM se cita como fuente de la
    implementacion del protocolo fisico, junto a Peters et al. como fuente del protocolo; las desviaciones se
    declaran. La autora aporta el raw en `refs/raw/`."

## D-M — Tamano de efecto de la prueba de cordura (G14)

- **(a)** Reportar o no un tamano de efecto con IC para el Wilcoxon frente a copia y pegado.
- **(b)** `diseno_A.md` §8 bis D4 (ii): "Se reporta ademas el tamano de efecto y su IC". §0 y `a24_contrastes.py`
  solo calculan $p$. La amplitud de copia y pegado vale 0 por construccion (`resultados_prueba_v1.md`:24, "las ROIs
  excluyen $M$"); el resultado fue p = 0.000122 con n = 13 en los dos puntos de control.
- **(c)** (1) retirar el tamano de efecto y reportar descriptivamente la mediana de las diferencias; (2) calcular
  una correlacion biserial de rangos con IC por remuestreo; (3) diferencia de medianas de Hodges-Lehmann con IC.
- **(d) Recomendacion: (1).** Con un brazo que vale 0 por construccion, la diferencia pareada es la amplitud del
  sintetizador y cualquier tamano de efecto basado en rangos es maximo y trivial (calculo propio: 0.000122 coincide con
  1/2^13, el minimo posible con 13 pares, es decir, todas las diferencias positivas). Un IC sobre eso no informa nada
  sobre calidad, y DEC 2026-10-05 (3) pto 5 ya dice que esta prueba no es evidencia. Retirarlo con esa razon es mas
  defendible que reportar un numero vacio.
- **(e) YA.** Fijarlo antes de correr `a24` de la version 2.
- **(f)** `capitulo3.tex:373`:
  > La decisión que fijó esta prueba preveía reportar además el tamaño de efecto y su IC; esa previsión se retira. Como la amplitud de la inserción por copia y pegado vale cero por construcción, la diferencia pareada coincide con la amplitud del sintetizador, y un tamaño de efecto basado en rangos no informaría sobre su calidad. Se reportan el valor $p$ y, de forma descriptiva, la mediana de las diferencias pareadas.
  - **Para DEC:** "2026-10-1X — Cordura (Wilcoxon frente a copia y pegado): se retira el tamano de efecto previsto en
    D4 (ii); se reporta $p$ y la mediana de las diferencias pareadas. Vale tambien para run05a/run05b."

## D-N — Supuesto del IC con *t* (G16)

- **(a)** Declarar el supuesto de normalidad aproximada de las 13 diferencias y decidir si se comprueba.
- **(b)** `diseno_A.md` §0: "IC90 de la diferencia media pareada con *t* de Student, n = 13"; nada sobre el supuesto
  (MAPA, fila del supuesto distribucional).
- **(c)** (1) declarar el supuesto y mostrar las 13 diferencias en el cap. 4; (2) anadir un IC por remuestreo como
  sensibilidad descriptiva; (3) no decir nada.
- **(d) Recomendacion: (1).** Es el estandar del TOST pareado y esta congelado. Mostrar las 13 diferencias
  individuales (tabla o grafico de puntos) deja al jurado juzgar la forma sin anadir pruebas. (2) es defendible solo
  como descriptivo, pero no lo recomiendo: abre "¿y si el remuestreo dice otra cosa?" sin que pueda cambiar el
  primario. (3) es un hueco que un jurado de estadistica senala.
- **(e) YA** (la tabla de 13 diferencias sale de `a20_ea2_test.csv`, ya calculado; va al cap. 4).
- **(f)** `capitulo3.tex:375`:
  > Ese IC se calcula con la distribución \emph{t} de Student sobre los 13 pacientes, lo que supone que las diferencias pareadas siguen aproximadamente una distribución normal. El diseño congelado no prevé comprobarlo; el supuesto se declara, y las 13 diferencias se muestran una a una en el capítulo de resultados.
  - **Para DEC:** "2026-10-1X — TOST: el IC90 con *t* supone normalidad aproximada de las diferencias pareadas; no se
    comprueba con una prueba; se declara y se muestran las 13 diferencias."

## D-O — Lectura de los desenlaces del TOST (G17)

- **(a)** Fijar que desenlace del TOST se lee como no equivalencia y cual como no concluyente.
- **(b)** D4 (`diseno_A.md` §8 bis (iii)) y §0: solo "equivalencia si el IC90 cae entero en el margen" y que un no
  concluyente no se convierte en "comparable". `resultados_prueba_v1.md`:27-29 ya hace una lectura descriptiva y la
  marca como no fijada en el diseno: con el principal, IC90 entero bajo 0 y con su extremo superior (-124.9) dentro de
  [-196.3, 196.3]; con `run04_60k`, entero fuera de los dos margenes.
- **(c)** (1) fijar ahora tres desenlaces (equivalencia: IC90 entero dentro; no equivalencia: IC90 entero fuera;
  no concluyente: cruza un limite), mas si el IC excluye 0, declarando que es posterior para la version 1 y previo para
  la version 2; (2) no fijar nada y reportar solo "no se concluye equivalencia"; (3) leer el resultado de la version 1
  como "evidencia en contra".
- **(d) Recomendacion: (1).** Es la lectura estandar de un TOST, no favorece al sintetizador (con ella el resultado
  principal de la version 1 queda **no concluyente, con rayas significativamente mas debiles**, y la sensibilidad con
  `run04_60k` queda **no equivalente**) y evita las dos trampas: (2) esconde informacion que el jurado vera en la tabla;
  (3) seria una sobrelectura. Lo decisivo es **escribirla en DEC antes de lanzar `a20_v2`/`a24` de la version 2**: asi
  es preinscrita para el exploratorio y solo posterior para la version 1, y se declara asi.
- **(e) YA, y con urgencia** (antes de `a20_v2`).
- **(f)** `capitulo3.tex:375`, tras "Nunca se infiere equivalencia de una diferencia no significativa":
  > El diseño congelado solo define cuándo se concluye equivalencia. La lectura de los demás desenlaces se fijó después de conocer el resultado de la versión~1 y antes de evaluar la versión~2 en prueba, y se declara así: si el IC del 90\,\% queda entero fuera de $[-\Delta, +\Delta]$, se concluye que no hay equivalencia; si cruza uno de sus límites, el resultado es no concluyente. En los dos casos se informa además si el IC excluye el cero.
  - **Para DEC:** "2026-10-1X — Lectura del TOST (posterior para la version 1, #177; previa para run05a/run05b, antes
    de `a20_v2`): equivalencia si el IC90 cae entero en [-Delta, +Delta]; no equivalencia si cae entero fuera; no
    concluyente si cruza un limite. Se informa ademas si el IC90 excluye 0. Nunca se lee 'no concluyente' como
    'comparable' ni como 'evidencia en contra'."

## D-P — Margen no fijado por el sintetizador (G18)

- **(a)** Anadir o no un TOST con un margen ajeno al sintetizador como sensibilidad post congelamiento (#162 (3)(b)).
- **(b)** #162 (3): punto de control, material y `Delta` se fijaron sobre los mismos dos receptores y los tres
  empujan hacia concluir equivalencia; (a) declararlo (ya hecho en la prosa), (b) ademas un `Delta` alternativo. El
  unico otro margen calculable del registro es el test-retest del protocolo fisico, `r` = 6.1 HU
  (`resultados_validacion_pose.md` §3), mucho mas estrecho que 196.3.
- **(c)** (1) solo declarar el sentido conjunto (opcion (a)); (2) anadir el TOST con `r`; (3) anadir un margen nuevo.
- **(d) Recomendacion: (1).** El sesgo declarado favorece la equivalencia; un margen mas estrecho solo puede hacer mas
  dificil concluirla, asi que una sensibilidad con `r` no puede cambiar la lectura de un resultado que no concluyo
  equivalencia y solo anade un analisis post hoc. (3) seria inventar un margen despues de ver el resultado. La frase
  correcta para el cap. 3 es condicional: el sesgo importa si se concluye equivalencia, no si no se concluye.
- **(e) YA.**
- **(f)** `capitulo3.tex:431`, en lugar de la marca:
  > Como las tres elecciones empujan hacia concluir equivalencia, un desenlace de equivalencia tendría que leerse con esa salvedad, mientras que uno de no equivalencia o no concluyente no puede atribuirse a ellas. Por eso no se añade una prueba con un margen ajeno al sintetizador: sería un análisis posterior al congelamiento, y el único margen alternativo calculable con lo registrado, el de las corridas repetidas del protocolo físico, es más estrecho y solo podría dificultar la equivalencia.
  - **Para DEC:** "2026-10-1X — #162 (3): opcion (a) sola. Se declara el sentido conjunto de las tres elecciones; no se
    anade TOST con margen alternativo."

---

## Agrupacion final

### Tomar YA, en un solo bloque (15 decisiones, 17 marcas)

D-A (G01, G02, G15), D-B, D-C, D-D, D-E, D-G, D-H, D-I, D-J, D-K, D-L, D-M, D-N, D-O, D-P.
**Por que en bloque:** ninguna depende de datos nuevos ni de la version 2; todas son correcciones de registro,
declaraciones o retiros de lo no programado, y el criterio es el mismo en todas (lo ejecutado manda, se declara lo
posterior, no se anaden analisis que no puedan cambiar la conclusion). Se pueden pegar en una sola entrada de DEC y
cerrar con una sola ronda de `/ciclo-redaccion capitulo3` (mas `introduccion` y `capitulo1` para D-A).
**Dentro del bloque, D-O, D-M y D-N deben escribirse en DEC antes de lanzar `a20_v2.sbatch`/`a24`**, para que valgan
como previas en el analisis exploratorio de la version 2.

### Dependen de datos o corridas (1 decision, 1 marca)

- D-F (G07): costura en E-A2 con `a10_costura.py` sobre salidas ya generadas (CPU local; sumarla a `a20_v2` para los
  tres modelos). Mientras tanto, `\GAPDATO`.
- Ninguna marca depende de los resultados de prueba de la version 2: esos resultados van al cap. 4 y no cambian el
  diseno del cap. 3.

### Conviene consultar con el asesor humano

- **D-O** (lectura del TOST): define como se presenta el resultado principal ante el jurado; es la mas sensible.
- **D-C** (regla del suelo no evaluable): reconocer un defecto en una regla preinscrita; conviene que el asesor este de
  acuerdo con la formulacion.
- **D-A** (cierre de #90): toca alcance y la pregunta de investigacion; el asesor debe saber que el contraste primario
  se mantiene con un resultado no favorable.
- Opcional: **D-J** (razon escrita despues) y **D-P**, si el asesor prefiere una sensibilidad adicional.

### Desfases detectados fuera de las marcas (para la misma ronda)

- `introduccion.tex:56` y `capitulo2.tex:106`: "sobre las poses del muestreador" y "segun el plazo" (D-A, D-J).
- `introduccion.tex:90`: el `\GAPDATO` contiguo dice que el modelo final no esta elegido (PAT-122).
- `capitulo1.tex:128`: "aun sin preinscribir" del margen.
- `docs/00-tesis.md`:91 (cabeza como sensibilidad) y la region de E-A3 en `tesis/main.tex`:102: los alinea la autora.
