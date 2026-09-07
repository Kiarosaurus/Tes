# 04 — Implicancias sobre la tesis

> Cola de hallazgos que PODRIAN cambiar algo del documento.
> La alimenta cualquier actividad: lecturas, tareas del asesor, experimentos.
> Claude escribe aqui. La autora decide: al resolver una entrada, la decision
> definitiva se copia a `01-decisiones.md` y aqui queda como APLICADA.

Estados: ABIERTA | APLICADA | DESCARTADA

| # | Fecha | Origen | Hallazgo | Que seccion toca | Tipo | Estado |
|---|---|---|---|---|---|---|
| 1 | 2026-09-06 | Inventario de `papers/` vs `refs.bib`; abstract aportado por la autora | `wang2025adaptiveweighting` es nivel 1 y sostiene la multi-ventana en HU (C3), pero solo hay abstract. Respaldo de C3 queda cualitativo | Metodo (C3, codificacion multi-ventana) | RIESGO | ABIERTA |
| 2 | 2026-09-06 | Abstract de `wang2025adaptiveweighting` | El multi-ventana en CT existe, pero siempre para REMOVER artefactos. Yo lo uso para GENERARLOS. Es desalineacion de tarea y a la vez posible gap | Related Work; justificacion de C3 | GAP | ABIERTA |
| 3 | 2026-09-06 | Abstract de `zhang2026pediclescrew` | Difusion + "CT sintetico" + planificacion de tornillos, publicado. La tarea es otra (traduce CBCT a CT, no inserta implantes), pero el encuadre colisiona con como presento mi novedad | Related Work; Problem Statement | RIESGO | ABIERTA |
| 4 | 2026-09-06 | Abstract de `zhang2026pediclescrew` | Usa una graduacion de brecha cortical con umbral explicito de 2 mm y un "Grade A". Mi BFC se apoya solo en `smith2006iliosacral` | Definicion de la metrica BFC; posiblemente SAP | RIESGO | ABIERTA |
| 5 | 2026-09-06, ACTUALIZADA con el PDF leido | `liu2025pipeline`, leido con `lector-papers` | La colision NO es de metodo: planifica un optimo determinista, sin distribucion de poses, sin tornillos iliosacrales, sin zonas seguras. Pero corre sobre CTPelvic1K y define CSV (distancia al borde oseo) y QID, vecinas de SAP y BFC | Related Work; definicion de SAP y BFC | RIESGO | ABIERTA |
| 6 | 2026-09-06, ACTUALIZADA con los PDFs leidos | `ren2022metalinsertion` y `yun2026simulationdriven`, leidos con `lector-papers` | `ren2022` aporta la frase que FUNDAMENTA el gap (su fisica se rompe con implantes ortopedicos), pero exige datos crudos de fabricante que CTPelvic1K no tiene. `yun2026` es MAR, no segmentacion, pero ya publica cifras sobre CLINIC-metal | Related Work; novedad del renderizador | GAP | ABIERTA |
| 7 | 2026-09-06 | `ramadanov2025safezone` leido con `lector-papers` | La unica fuente de "zona segura" de la bibliografia no da geometria 3D, ni umbral, ni margen: es un procedimiento cualitativo sobre proyeccion 2D con n=1. El muestreador se queda sin fuente operacional para su restriccion principal | Objetivo 2 (alcance MINIMO VIABLE); definicion de la restriccion del muestreador | RIESGO | ABIERTA |
| 8 | 2026-09-06, AGRAVADA con `wu2022xcist` leido | `deman2007catsim`, `yun2026simulationdriven`, `haneda2025aapm` y `wu2022xcist`, los cuatro leidos | La "reimplementacion validada de XCIST" NO es sostenible: el propio paper de XCIST no contiene ningun estudio ni validacion de artefacto metalico, declara su validacion como "first-order" y "in progress", y su pipeline agrega un ciclo de reconstruccion que el renderizador no sufre | Alcance COMPLETO, brazo de comparacion; Objetivo 3 | BASELINE | ABIERTA |
| 9 | 2026-09-06 | Patron transversal de cuatro lecturas: `wang2019cochlear`, `ren2022metalinsertion`, `karageorgos2024ddpm`, `haneda2025aapm` | Insertar metal sintetico en CT para fabricar datos de entrenamiento YA es practica establecida y publicada, en cuatro trabajos independientes. Ademas, difusion latente aplicada a artefactos metalicos ya compitio en el reto AAPM (5to lugar). El gap no puede enunciarse como "insertar metal sintetico" ni como "difusion latente en artefactos metalicos" | Problem Statement; reclamo de novedad completo | GAP | ABIERTA |
| 10 | 2026-09-06 | `chen2024tumorsynthesis` leido con `lector-papers` | Identidad DiffTumor confirmada. Declara que no modela nada fuera de la mascara y trunca HU a [-175, 250]: es respaldo citable directo de B_delta y de la multi-ventana C3 | Justificacion de B_delta (Obj 3) y de C3 (Obj 1) | REDACCION | ABIERTA |
| 11 | 2026-09-06 | `smith2006iliosacral` leido con `lector-papers` | El paper suma al score una SEGUNDA escala, angular (grados <5, 5-10, 11-15, >15), que la tesis no estaba considerando. Y sus tasas por brazo son cadavericas con n=4 y sin significancia: no sirven de prior clinico | Definicion de SAP; supuesto sobre de donde salen los priors del muestreador | RIESGO | ABIERTA |
| 12 | 2026-09-06 | `zwingmann2009navigated` leido con `lector-papers` | El rango "31-60%" NO existe en el PDF. Son dos complementos aritmeticos (100-69 y 100-40) de dos brazos tecnicamente distintos, navegado y convencional. Citarlo como rango del paper seria error de atribucion, y tratarlo como una sola distribucion es error de categoria | Benchmark del alcance MINIMO VIABLE; comparacion de distribuciones de SAP | RIESGO | ABIERTA |
| 13 | 2026-09-06 | `liu2021ctpelvic1k` leido con `lector-papers` | CLINIC-metal tiene solo 14 de 75 volumenes anotados: los autores lo excluyeron del entrenamiento supervisado por dificultad de etiquetado. Ademas el paper nunca dice que tipo de metal contiene, y no reporta ninguna cifra de degradacion por metal | Objetivo 5 (downstream); premisa central de la tesis; data card | RIESGO | ABIERTA |
| 14 | 2026-09-06 | `peters2025hybrid` leido con `lector-papers` | Da la definicion operacional de bone integrity (150 HU + SDC) y metal integrity (max HU en ROI + 250), base citable de BFC e ISC. Declara por escrito que la colocacion realista de metal es impracticable a mano, lo que sostiene la novedad del muestreador. Y su benchmark NO cubre osteosintesis pelvica | Definicion de BFC e ISC (Obj 4); brazo de comparacion (Obj 3); Related Work | GAP | ABIERTA |

Tipos: REDACCION (ajustar como lo digo) | ALCANCE (agranda o achica el trabajo)
| GAP (posible nueva contribucion) | RIESGO (amenaza un supuesto mio)
| BASELINE (afecta con que me comparo)

---

## Detalle de entradas abiertas

<!-- Una seccion por entrada ABIERTA, con el contexto completo.
     Formato:

### [#] Titulo corto — ABIERTA
- **Origen:** <paper / tarea del asesor / experimento>
- **Hallazgo:** <que se encontro, con evidencia textual si viene de un paper>
- **Por que importa:** <que supuesto o afirmacion mia queda tocada>
- **Seccion afectada:** <Problem Statement / Hipotesis / Objetivo N / Datasets>
- **Opciones:** <que podria hacer al respecto>
- **Pendiente de:** <decision mia / consultar al asesor / mas lectura>
-->

### 1 Solo hay abstract de wang2025adaptiveweighting: C3 queda con respaldo cualitativo — ABIERTA
- **Origen:** inventario de `papers/` contra `refs.bib` (2026-09-06), mas el abstract
  que aporto la autora ese mismo dia. Actualizada: el estado bajo de SIN ACCESO a
  ABSTRACT. La autora indica que el PDF llega pronto, pero aun no.
- **Hallazgo:** el abstract confirma la premisa que yo necesitaba, en sus palabras:
  *"The methods trained on a fixed single window would lead to insufficient removal
  of metal artifacts when being transferred to deal with other windows."* Eso
  respalda que fijar una sola ventana HU es una limitacion real. Pero es todo lo que
  hay: ninguna cifra del cuerpo esta disponible.
- **Por que importa:** `_index.md` marca esta fuente como **nivel 1** con el rol
  "multi-ventana (C3)". Por la regla dura de accesibilidad, mientras el estado sea
  ABSTRACT no puedo citarle ninguna cifra: ni umbrales de ventana, ni deltas de
  desempeno, ni el "five datasets" que menciona el propio abstract. La justificacion
  de C3 puede escribirse, pero solo en terminos cualitativos.
- **Seccion afectada:** Metodo, componente Renderizador (C3, codificacion
  multi-ventana en HU). Tambien Related Work.
- **Opciones:**
  1. Conseguir el PDF y releer con `lector-papers`. Resuelve de raiz; es nivel 1 y
     ya esta anunciado que llega. Es lo esperable.
  2. Mientras tanto, redactar C3 sin cifras de esta fuente. La frase del abstract
     alcanza para motivar, no para cuantificar.
  3. No escribir la justificacion de C3 en su version final hasta tener el PDF, para
     no tener que reescribirla dos veces.
- **Pendiente de:** llegada del PDF. Cuando llegue, regenerar la ficha
  `docs/literatura/wang2025adaptiveweighting.md` completa y quitar la marca
  "Profundidad: solo abstract".
- **Nota:** `zhang2026pediclescrew` sigue sin PDF y sin nivel asignado en
  `_index.md`. Definir su nivel antes de decidir si abre su propia implicancia.

### 2 El multi-ventana existe solo para remover artefactos, no para generarlos — ABIERTA
- **Origen:** abstract de `wang2025adaptiveweighting`, aportado por la autora el
  2026-09-06.
- **Hallazgo:** el abstract situa el estado del arte multi-ventana asi:
  *"few works have proposed to reconstruct the CT images under multiple-window
  configurations"*. Todo ese trabajo, incluido AdaW, es de **remocion** de artefactos:
  asume una imagen limpia de referencia y optimiza hacia ella.
- **Por que importa:** corta en dos direcciones y hay que decidir cual se escribe.
  - **Como riesgo:** C3 usa multi-ventana como condicionamiento de un renderizador
    **generativo**. Citar AdaW para justificar C3 empareja dos tareas distintas
    (remover vs generar). Un asesor o un revisor puede leerlo como analogia forzada.
    La premisa compartida es solida —una sola ventana HU pierde informacion—, pero el
    uso no es el mismo, y conviene decirlo explicitamente en vez de dejar que lo
    noten.
  - **Como gap:** si nadie aplico codificacion multi-ventana a la **sintesis** de
    artefacto metalico, eso es terreno libre y refuerza la contribucion del
    renderizador. Seria un argumento de novedad, no solo de motivacion.
- **Seccion afectada:** Related Work, y la justificacion de C3 en Metodo.
- **Opciones:**
  1. Redactar C3 reconociendo la diferencia de tarea de frente: "multi-ventana esta
     establecido en MAR de remocion; aqui se traslada a sintesis". Convierte la
     debilidad en el argumento de novedad.
  2. Buscar respaldo adicional en sintesis generativa medica que ya use
     multi-ventana o multi-contraste, para no depender de una analogia con MAR.
  3. Verificar el reclamo de novedad antes de escribirlo. El abstract dice "few
     works", no "ninguno en sintesis": es una inferencia mia, no una afirmacion del
     paper. Confirmar con el texto completo y con el survey `selles2024marreview`.
- **Pendiente de:** decision mia. La opcion 3 primero: no afirmar un gap que no
  verifique.
- **Nota (2026-09-06):** `zhang2026pediclescrew` refuerza el patron. Su modulo de
  artefactos tambien **mitiga** ("mitigate localized artifact distributions"). Van dos
  fuentes independientes donde el artefacto es lo que se quita. El patron se sostiene.

### 3 Un paper publicado ya combina difusion, CT sintetico y planificacion de tornillos — ABIERTA
- **Origen:** abstract de `zhang2026pediclescrew`, aportado por la autora el
  2026-09-06.
- **Hallazgo:** STADW-M genera CT sintetico desde CBCT intraoperatorio y despues
  corre planificacion automatica de tornillos sobre lo generado, reportando validacion
  clinica. Titulo y encuadre quedan muy cerca de los mios.
- **Por que importa:** la tarea tecnica **no** es la mia y conviene tenerlo claro
  antes de alarmarse:
  - El traduce CBCT a CT con datos pareados. La anatomia y el artefacto ya estan en
    su entrada; los limpia.
  - Yo inserto implantes que **no existen** en la imagen de entrada, y fabrico el
    artefacto que no esta.
  - El es columna (pedicular/vertebral). Yo soy pelvis.

  Mi gap sobrevive. El problema es de **framing**, no de metodo: alguien que lea
  "difusion + CT sintetico + tornillos" en los dos titulos va a asumir solapamiento y
  pedir comparacion. Si no me adelanto, gasto la defensa en aclarar en vez de en
  argumentar.
- **Seccion afectada:** Related Work y Problem Statement. Posiblemente la frase donde
  enuncio la contribucion.
- **Opciones:**
  1. Citarlo explicitamente en Related Work y marcar la diferencia en una frase:
     traduccion de dominio sobre anatomia existente vs sintesis de estructura ausente.
     Es lo mas barato y lo que mejor protege.
  2. Ajustar como enuncio mi contribucion para que la diferencia se lea desde el
     titulo y el abstract, sin depender de que el lector llegue a Related Work.
  3. Al llegar el PDF, revisar si en algun punto insertan o simulan estructura
     metalica. Si lo hicieran, esto deja de ser framing y pasa a ser competencia real,
     y esta entrada habria que reescribirla entera.
- **Pendiente de:** decision mia, pero la opcion 3 primero: es verificacion, no
  decision, y cambia el peso de todo lo demas.

### 4 Aparece una segunda escala de brecha cortical, con umbral de 2 mm — ABIERTA
- **Origen:** abstract de `zhang2026pediclescrew`, aportado por la autora el
  2026-09-06.
- **Hallazgo:** reporta *"94.7% of screws placed without cortical breach and 5.3%
  exhibiting only minor (<2 mm) erosion"* y un *"100% Grade A standard"*. El abstract
  **no nombra** la escala de la que sale ese "Grade A": NO ENCONTRADO EN EL ABSTRACT.
- **Por que importa:** mi metrica BFC (brecha cortical) se apoya hoy en
  `smith2006iliosacral`, y `docs/ESTADO.md` ya registra como deuda que la definicion
  de grados de brecha cortical es de donde cuelga SAP. Que exista una segunda
  graduacion, con un umbral numerico explicito de 2 mm, es material directo para esa
  deuda. Puede convergir con mi definicion, y entonces la refuerza; o puede divergir,
  y entonces tengo que justificar por que elijo una.
- **Seccion afectada:** definicion de la metrica BFC. Por dependencia, posiblemente
  tambien SAP.
- **Opciones:**
  1. Al llegar los dos PDFs, comparar la escala de `smith2006iliosacral` contra la de
     este paper y decidir cual adopto, o si adopto una y reporto la otra.
  2. Si resultan ser escalas de anatomias distintas (pedicular vs iliosacral), no
     mezclarlas: usar la iliosacral y mencionar la otra como referencia de que el
     umbral de 2 mm circula en la literatura.
  3. Adoptar el umbral de 2 mm como corte de BFC solo si el texto completo lo
     sostiene. Hoy no puedo: fuente en ABSTRACT.
- **Pendiente de:** llegada de los PDFs. Esto engancha con la deuda ya asumida de
  leer a fondo `zwingmann2009navigated` y `smith2006iliosacral`.
- **Aviso aparte, para que no me agarre desprevenida:** su 5.3% de brecha menor y el
  31-60% de malposicion de `zwingmann2009navigated` **no son comparables** —
  planificacion automatica sobre imagen sintetica vs colocacion real en quirofano,
  columna vs pelvis, y probablemente escalas distintas. Pero son dos numeros de
  aspecto parecido y muy distinto valor. Conviene tener la respuesta preparada.

### 5 liu2025pipeline puede colisionar con la novedad del muestreador — ABIERTA
- **Origen:** recriterio de niveles de `docs/literatura/_index.md` el 2026-09-06,
  cuando la autora redefinio el nivel como riesgo sobre el argumento central.
  **Derivado unicamente del titulo y los metadatos de `refs.bib`. El PDF esta en
  `papers/` pero no se ha leido.** Nada de esta entrada es evidencia textual.
- **Hallazgo:** `refs.bib` registra *"An End-to-End Geometry-Based Pipeline for
  Automatic Preoperative Surgical Planning of Pelvic Fracture Reduction and
  Fixation"*, IEEE TMI 2025, 44(1), 79--91. Colocacion automatica de fijacion
  pelvica, basada en geometria, publicada. En `_index.md` estaba en nivel 3
  ("contexto, no tan relevante").
- **Por que importa:** el alcance MINIMO VIABLE de `00-tesis.md` es lo unico que la
  autora garantiza defender, y su unica contribucion propia ahi es el Obj 2: el
  muestreador de colocacion quirurgicamente restringido. Esto es la obra publicada
  mas cercana a ese objetivo que hay en toda la bibliografia, en la misma revista.
  Si un jurado la conoce, la primera pregunta es en que se diferencia el muestreador.
  Hay una respuesta plausible ya escrita en `CLAUDE.md` — el muestreador **no**
  optimiza una trayectoria buena, muestrea la distribucion clinica de malposiciones,
  que es lo contrario de planificar — pero esa respuesta hoy no esta verificada
  contra lo que el paper realmente hace.
- **Seccion afectada:** Problem Statement y Related Work. Potencialmente el reclamo
  de novedad del Obj 2.
- **Opciones:**
  1. Leer `liu2025pipeline` con `lector-papers` y ver si planifica una trayectoria
     optima (entonces la distincion optimizar/muestrear se sostiene y el paper pasa
     a ser apoyo, no amenaza) o si modela variabilidad de colocacion (entonces es
     competencia real y hay que reescribir la novedad del Obj 2).
  2. Si se sostiene la distincion, escribirla explicita en Related Work y no dejarla
     implicita. Es la defensa del minimo viable.
  3. Evaluar si sirve ademas como baseline geometrico del muestreador.
- **Pendiente de:** lectura. Es prioridad 1 del orden sugerido en `_index.md`.

### 6 La receta del renderizador ya tiene dos antecedentes publicados — ABIERTA
- **Origen:** recriterio de niveles de `docs/literatura/_index.md` el 2026-09-06.
  **Derivado unicamente de titulos y metadatos de `refs.bib`. Los dos PDFs estan en
  `papers/` y ninguno se ha leido.** Nada de esta entrada es evidencia textual.
- **Hallazgo:** dos entradas que estaban en niveles bajos hacen, por titulo, partes
  de lo que promete el renderizador:
  `ren2022metalinsertion` — *"Framework of Metal Insertion in the Projection Domain
  for Image Quality Optimization in Interventional Computed Tomography"*, J Med
  Imaging 2022 (estaba en nivel 2).
  `yun2026simulationdriven` — *"A Strategy for Simulation-Driven CT Metal Artifact
  Reduction Toward Improving Network Generalizability"*, Medical Physics 2026
  (estaba en nivel 3).
- **Por que importa:** el primero ya inserta metal sinteticamente en CT; el segundo
  ya usa artefactos metalicos simulados para que una red generalice mejor. Juntos
  cubren, en el papel, el argumento completo del Objetivo 3 y del Objetivo 5. La
  diferencia que la autora reclama es doble: el dominio (difusion latente vs
  proyeccion analitica) y la tarea aguas abajo (segmentacion osea peri-implante vs
  MAR). Ninguna de las dos diferencias esta verificada contra el texto.
- **Seccion afectada:** Related Work, justificacion del Objetivo 3, y la eleccion
  del brazo de comparacion. Hoy el unico baseline declarado es XCIST/CatSim, que es
  simulacion fisica; `ren2022metalinsertion` seria un baseline de insercion, que es
  una comparacion mas exigente y mas pertinente.
- **Opciones:**
  1. Leer los dos con `lector-papers` y precisar la diferencia en una frase que
     aguante una repregunta.
  2. Evaluar `ren2022metalinsertion` como segundo brazo de comparacion junto a XCIST.
     Sube el costo del alcance COMPLETO; decidir si vale.
  3. Si `yun2026simulationdriven` mide generalizacion de la red aguas abajo, mirar
     que metrica usa: puede servir de precedente metodologico para el Objetivo 5
     (Dice, HD95) en vez de ser solo una amenaza.
- **Pendiente de:** lectura. Prioridad 4 del orden sugerido en `_index.md`.

### 5 — ACTUALIZACION tras leer el PDF (2026-09-06)
La sospecha derivada del titulo era **parcialmente falsa**. `liu2025pipeline` no
compite en metodo: produce un plan optimo determinista, no una distribucion.
- *"The computation of implanted directions of the screws is formulated as an
  optimization problem subject to safety, fixation ability, and clinical executability
  constraints"* (Sec. III-D.3, p. 11).
- Modelado de distribucion o muestreo estocastico de poses: **NO ENCONTRADO EN EL PDF**.
- No son tornillos iliosacrales, y el sacro queda fuera: *"not yet applicable to
  bilateral fractures and to sacral fractures"* (Discussion, p. 18).
- No genera imagen ni artefacto. Tasa de malposicion: **NO ENCONTRADO EN EL PDF**.

Pero la colision se movio de sitio, y ahora es de **metrica**: corre sobre el mismo
dataset, *"Our method is tested in data set CTPelvic1K [48]"* (Sec. VI, p. 14), con 14
casos clinicos, y define CSV como distancia al borde oseo mas QID. Si SAP se define
como margen a la cortical, CSV es antecedente directo y la comparacion pasa a ser
obligatoria. Nivel corregido de 1 a 2, con la salvedad de que sube a 1 por la via de
la metrica si SAP se define asi.

### 6 — ACTUALIZACION tras leer los PDFs (2026-09-06)
Las dos lecturas mueven esta entrada de BASELINE a GAP, y en direcciones opuestas.

`ren2022metalinsertion` **confirma nivel 1**, por una sola frase que es el activo mas
valioso encontrado en toda la ronda: *"The developed framework may need to be revisited
if the amount of inserted metal increased (e.g., in the case of orthopedic implants)"*
(Sec. 4, p. 035001-15). El supuesto que se rompe es la dispersion despreciable. Es la
literatura analitica declarando por escrito su propio limite justo donde empieza esta
tesis. Aporta ademas umbrales de artefacto reutilizables: -75 / 75 / 500 HU.
Pero **debilita** su propio uso como brazo de comparacion: exige proyecciones crudas de
fabricante y espectro/DQE provistos por el, y CTPelvic1K son imagenes reconstruidas.
Anatomia: rinon, no pelvis. Metal: sondas de ablacion, no osteosintesis.

`yun2026simulationdriven` **baja a nivel 2**: la tarea es MAR, no segmentacion, y no
reporta Dice ni HD95. Pero es la lectura que mas cifras citables deja, porque ya publica
sobre el subconjunto exacto de la tesis: *"we additionally tested on a publicly
available clinical CT dataset, referred to as CLINIC_METAL, based on the CTPelvic1K
dataset"* (Sec. 2.4.2, p. 8), y describe CTPelvic1K con *"1,184 pelvic CT volumes [...]
including 75 scans with metal artifacts (CLINIC-metal subset)"*. Trae la frase que
sostiene el gap de realismo: *"in the absence of highly realistic simulation pipelines,
it is challenging to generate synthetic metal artifacts that accurately reflect the
complex physical behaviors observed in clinical CT scans"* (Sec. 1, p. 2). Y un
protocolo de evaluacion clinica **sin ground truth** (RMSE y sesgo HU en ROI libre de
artefacto) que es directamente reutilizable, porque CLINIC-metal tampoco tiene GT.

### 7 El muestreador se queda sin fuente operacional de zona segura — ABIERTA
- **Origen:** `ramadanov2025safezone` leido con `lector-papers` el 2026-09-06. Es la
  unica fuente de toda la bibliografia que define una zona segura sacroiliaca.
- **Hallazgo:** no define una geometria, define un procedimiento cualitativo. Estudio
  piloto sobre **una sola CT**: *"This study is based on a single CT scan of a
  75-year-old male patient"* (Sec. 4.1, p. 10). La zona sale de una proyeccion **2D**:
  *"a 2D lateral view of the sacrum was generated by summing the Y-axis slices"*
  (Metodos, paso 4, p. 4). El umbral no tiene valor numerico: *"choosing a threshold
  high enough to only outline the high density of S1"* (Fig. 5, p. 8). Umbral propio,
  coordenadas, angulos, diametros, margen al cortical o al foramen, y tasa de
  malposicion propia: **NO ENCONTRADO EN EL PDF**. Los autores lo admiten: *"A formula
  or algorithm that allows for the application of the Ramadanov-Zabler Safe Zone [...]
  could significantly enhance clinical applicability"* (Sec. 4.2, p. 11). Ademas la
  segmentacion automatica les fallo: *"Standard thresholding methods for segmentation
  proved ineffective due to low bone density"* (Abstract, p. 1).
- **Por que importa:** `CLAUDE.md` describe el muestreador como "restringido por mapas
  de densidad osea, contencion cortical y **zonas seguras**". El Objetivo 2 es la unica
  contribucion propia del alcance MINIMO VIABLE. Con esta fuente, la tercera restriccion
  no tiene respaldo numerico en la literatura: seria una construccion propia presentada
  como si fuera heredada. Es la clase de cosa que un jurado pide sustentar.
- **Seccion afectada:** Objetivo 2, definicion de la restriccion del muestreador.
  Posiblemente SAP, si SAP se apoya en la zona segura.
- **Opciones:**
  1. Buscar una fuente con geometria parametrizada. Candidata concreta que este mismo
     paper cita: McLaren et al. 2021, *Corridor-diameter-dependent angular tolerance for
     safe transiliosacral screw placement: An anatomic study of 433 pelves*, con
     tolerancias de 1.53 grados (S1) y 1.02 grados (S2). Registrada en `_candidatos.md`.
  2. Reformular la restriccion como "mapa de densidad osea + contencion cortical" y
     declarar que la zona segura es construccion propia, no heredada.
  3. Mantener "zona segura" solo como motivacion cualitativa, citando esta fuente para
     eso y nada mas.
- **Pendiente de:** decision de la autora. La opcion 1 exige conseguir un PDF nuevo.

### 8 El brazo de comparacion XCIST/CatSim se debilita por tres frentes — ABIERTA
- **Origen:** `deman2007catsim`, `yun2026simulationdriven` y `haneda2025aapm`, los tres
  leidos con `lector-papers` el 2026-09-06.
- **Hallazgo:** el alcance COMPLETO promete una "reimplementacion validada de XCIST como
  brazo de comparacion". Tres lecturas independientes la complican:
  1. `deman2007catsim` **no modela metal**. No hay seccion, figura ni parrafo sobre
     artefactos metalicos, y el termino *beam hardening* no aparece. Tampoco trae los
     parametros para reimplementar (distancias fuente-detector, celdas, vistas, bowtie,
     DQE): **NO ENCONTRADO EN EL PDF**, 20 entradas.
  2. `yun2026simulationdriven` lo descarta como banco de pruebas moderno: *"this dataset
     is only compatible with its own CPU-based reconstruction module, limiting its use
     for benchmarking with modern deep learning models that require GPU-based
     differentiable forward and backward projectors"* (Sec. 4, p. 18).
  3. `haneda2025aapm`, que si usa CatSim dentro de XCIST, documenta que falla justo en
     el regimen de implantes grandes: *"the metal trace in the training sinogram
     generated by the XCIST simulator may look distorted [...] for large metal objects
     with diameters larger than 3.0 cm"* (Sec. 4, p. 16), con 274 casos afectados de
     14 000.
  La alternativa `ren2022metalinsertion` tampoco es reimplementable aqui: exige
  proyecciones crudas de fabricante, y CTPelvic1K son imagenes ya reconstruidas.
- **Por que importa:** el renderizador necesita contra que compararse. Hoy el unico
  soporte nivel 1 del brazo fisico es `wu2022xcist`, que no esta leido. Si la
  reimplementacion no es fiel, la comparacion pierde valor y con ella parte del Obj 3.
- **Seccion afectada:** alcance COMPLETO, brazo de comparacion. Objetivo 3.
- **Opciones:**
  1. Leer `wu2022xcist` a fondo antes de comprometer el brazo de comparacion. Es nivel 1
     y esta sin leer; puede que si traiga los parametros que faltan.
  2. Verificar el limite de 3.0 cm contra el banco propio de 61 geometrias. Si los
     tornillos caen debajo, no aplica; si hay placas por encima, aplica.
  3. Cambiar el brazo de comparacion al protocolo ya parametrizado de `peters2025hybrid`
     y `haneda2025aapm`, en vez de reimplementar.
  4. Declarar el brazo de comparacion como alcance COMPLETO opcional.
- **Pendiente de:** lectura de `wu2022xcist` (opcion 1) antes de cualquier decision.

### 9 Insertar metal sintetico ya es practica establecida: el gap hay que reenunciarlo — ABIERTA
- **Origen:** patron transversal de cuatro lecturas del 2026-09-06. No sale de un paper,
  sale de leerlos juntos. Es la implicancia mas cara de esta ronda.
- **Hallazgo:** cuatro trabajos independientes ya insertan metal sintetico en CT para
  fabricar datos de entrenamiento:
  1. `wang2019cochlear`: *"the virtual insertion of electrode arrays and the simulation
     of beam hardening based on the Beer-Lambert law"* (Abstract, p. 1), sobre 1090
     volumenes. *"Instead of training the GANs on pairs of pre and postoperative images,
     our approach relies on the physical simulation of artifacts"* (Intro, p. 2).
  2. `ren2022metalinsertion`: *"framework for metallic object insertion in the projection
     domain"* (Sec. 1).
  3. `karageorgos2024ddpm`: *"Training data are generated by performing highly realistic
     CT simulations of real patient images with and without metal objects"* (Sec. II-A,
     p. 3), con CatSim.
  4. `haneda2025aapm`: *"a hybrid data simulation framework that combined real patient
     images [...] with virtual metal objects"* (Abstract, p. 1), y lo declara comun:
     *"Many deep learning-based MAR studies rely on numerical simulations, where metal
     artifacts are synthetically introduced into randomly selected clinical CT images"*
     (Sec. 1, p. 2).
  Y ademas, difusion latente ya compitio en artefactos metalicos: el 5to lugar del reto
  AAPM usa *"Latent Diffusion model, Attention UNet"* (Tabla 1, p. 13).
- **Por que importa:** el reclamo de novedad no puede ser "insertar metal sintetico en
  CT", ni "usar difusion latente en artefactos metalicos". Las dos cosas estan
  publicadas. Lo que NO aparecio en ninguna lectura, y por eso sigue siendo defendible,
  es la **conjuncion**:
  (a) sintesis **generativa condicionada** de implante y artefacto, no simulacion
      analitica;
  (b) para **aumentacion de datos de segmentacion osea** peri-implante — la ficha de
      `haneda2025aapm` lo confirma por ausencia: ningun uso de metal sintetico como
      aumentacion para segmentacion, **NO ENCONTRADO EN EL PDF**;
  (c) con la **pose muestreada de la distribucion clinica de malposiciones** en vez de
      colocada al azar o a mano — `haneda2025aapm` coloca el metal *"in random soft
      tissue or bone locations"* (Sec. 2.2, p. 5) en entrenamiento y *"manually designed
      and positioned"* (Sec. 2.3, p. 6) en scoring.
- **Seccion afectada:** Problem Statement, reclamo de novedad completo, Related Work.
  Toca los dos componentes a la vez.
- **Opciones:**
  1. Reenunciar el gap alrededor de la conjuncion (a)+(b)+(c), que es lo que ninguna
     lectura contradijo, con esas tres patas explicitas.
  2. Escribir un parrafo de Related Work que reconozca las cuatro instancias de
     insercion sintetica. Reconocerlas de frente es mas fuerte que omitirlas.
  3. Convertir el punto (c) en la contribucion principal si el renderizador queda fuera
     del alcance por tiempo: el muestreo de la distribucion de malposiciones es lo unico
     que ningun trabajo leido hace.
- **Pendiente de:** decision de la autora. Es reenunciado, no cambio de diseno: el
  pipeline no se toca.

### 10 chen2024tumorsynthesis pasa de precedente favorable a respaldo directo de B_delta — ABIERTA
- **Origen:** `chen2024tumorsynthesis` leido con `lector-papers` el 2026-09-06.
- **Hallazgo:** se resolvio primero la identidad: el metodo **si se llama DiffTumor**,
  *"we introduce a novel framework, termed DiffTumor"* (Sec. 1, p. 2), aunque el titulo
  publicado es *Towards Generalizable Tumor Synthesis*. Queda confirmado el mapeo con la
  clave de `refs.bib`.
  Lo importante es otra cosa: el paper **declara que no modela nada fuera de la
  mascara**, *"we do not intend to model organ textures outside of the tumors"*
  (Sec. 3.2, p. 4), y **trunca HU a [-175, 250]** (Apendice E.2, p. 21).
- **Por que importa:** deja de ser "un precedente que me favorece" y pasa a ser respaldo
  citable de dos decisiones de diseno propias:
  1. La banda extendida **B_delta**: el estado del arte en sintesis de lesiones contiene
     todo dentro de la mascara. Un implante metalico produce streaking lejos del metal.
     Esa es la justificacion de B_delta dicha por la literatura misma, no por la autora.
  2. La codificacion **multi-ventana en HU (C3)**: truncar a [-175, 250] descarta
     precisamente el rango donde vive el metal. Refuerza el mismo argumento que
     `wang2025adaptiveweighting` sostiene hoy solo desde el abstract, y esta vez con
     PDF completo y cifra exacta.
- **Seccion afectada:** justificacion de B_delta y de C3, dentro del Objetivo 3 y del
  Objetivo 1.
- **Opciones:**
  1. Citar ambas frases en la justificacion de B_delta y de C3. Es la opcion barata y
     solida.
  2. Revisar si esto amerita subirlo a nivel 1: hoy esta en 2, pero sostiene dos
     decisiones de diseno, no solo redaccion.
- **Pendiente de:** decision de la autora sobre el nivel. La cita se puede usar ya.

### 4 — ACTUALIZACION tras leer smith2006iliosacral (2026-09-06)
La colision entre las dos escalas de brecha cortical **probablemente no es colision, es
ascendencia comun**. `smith2006iliosacral` declara que su escala no es propia:
*"Perforations were graded according to prior established classification methods used to
evaluate optimal pedicle screw placement"* (Screw Position, p. 236), con referencias a
Vaccaro 1995, Gertzbein & Robbins 1990 y Mirza 2003 — **literatura de tornillos
pediculares**, que es exactamente el dominio de `zhang2026pediclescrew`.

Su escala completa, textual: grado 0 *"no perforation"*; grado 1 *"perforation less than
2 mm"*; grado 2 *"perforation between 2 and 4 mm"*; grado 3 *"perforation more than
4 mm"*. El corte de 2 mm **coincide** con el de `zhang2026pediclescrew`. Lo que no
aparece aqui es la etiqueta "Grade A": la nomenclatura es numerica 0-3.

Consecuencia: es probable que ambas escalas desciendan de Gertzbein & Robbins 1990. Si se
confirma, la implicancia #4 deja de ser un riesgo de divergencia y pasa a ser una
oportunidad: se cita la fuente comun y se cierra la discusion. **Pendiente de** conseguir
el PDF de `zhang2026pediclescrew` y de leer Gertzbein & Robbins, ya registrado como
candidato.

Salvedad nueva: `smith2006iliosacral` es **fuente secundaria** del umbral. Citarlo como
origen de la escala seria un error de atribucion.

### 11 SAP ignora la segunda dimension de smith2006, y sus tasas no son priors clinicos — ABIERTA
- **Origen:** `smith2006iliosacral` leido con `lector-papers` el 2026-09-06.
- **Hallazgo:** dos cosas que el registro no tenia.
  1. El paper no puntua solo perforacion. Suma una **segunda escala angular**: grado 0
     (<5 grados), grado 2 (5-10), grado 3 (11-15), grado 4 (>15). El score final por
     tornillo es *perforacion + angulo*. La tesis le atribuia solo la escala de
     perforacion. Si SAP quiere replicar el criterio de admisibilidad completo de su
     propia fuente, le falta la mitad.
     Aviso de implementacion: el texto **no define un grado angular 1**, pero las Tablas
     1, 3 y 4 se lo asignan a varios tornillos. Es inconsistencia interna del paper y
     bloquea reimplementar el score compuesto sin una decision explicita.
  2. Las tasas por brazo son **cadavericas, n = 4 tornillos por brazo, 16 en total**, y
     los propios autores avisan: *"The difference between methods was not statistically
     significant"* (Results, p. 237) y *"The design of this study aliases the comparison
     of methods with the comparison of cadavers"* (Discussion, p. 237). Ademas los
     especimenes eran osteopenicos, *"making this population a worst-case study
     population"* (p. 237).
- **Por que importa:** el muestreador dice muestrear de la distribucion clinica real de
  malposiciones. Si alguna vez se pensaron estas tasas como prior, no sirven: n=4,
  cadaverico, sin significancia y sesgado a peor caso. El prior tiene que salir de
  `zwingmann2009navigated` o de otra fuente clinica. Esta entrada es un candado para que
  no se cuele una cifra de aqui a la tesis por parecer disponible.
- **Seccion afectada:** definicion de SAP (dimension angular) y supuesto sobre el origen
  de los priors del muestreador.
- **Opciones:**
  1. Incorporar la dimension angular a SAP y resolver por escrito el hueco del grado 1.
  2. Declarar explicitamente que SAP usa solo la dimension de perforacion, y justificar
     por que se descarta la angular.
  3. Usar `smith2006iliosacral` solo como fuente de la escala, nunca de tasas.
- **Pendiente de:** decision de la autora sobre 1 o 2. La opcion 3 no es opcional.

### 12 El benchmark 31-60% no es una cita: es un calculo propio sobre dos poblaciones distintas — ABIERTA
- **Origen:** `zwingmann2009navigated` leido con `lector-papers` el 2026-09-06. Es la
  entrada mas grave de todas las rondas de verificacion, porque toca el unico numero
  contra el que se compara el alcance MINIMO VIABLE.
- **Hallazgo:** el rango **31-60% no aparece en el PDF**. Ni como texto, ni como rango,
  ni en ninguna forma. Lo que el paper mide y escribe son dos distribuciones completas de
  cuatro grados, una por tecnica:

  | Brazo | Grado 0 | Grado 1 (<2 mm) | Grado 2 (2-4 mm) | Grado 3 (>4 mm) | n |
  |---|---|---|---|---|---|
  | Navegado 3D | 69% | 15% | 8% | 8% | 26 tornillos / 24 pacientes |
  | Convencional | 40% | 37% | 11.5% | 11.5% | 35 tornillos / 32 pacientes |

  Literal: *"Grade 0 in 69% (Grade 1, 15%; Grade 2, 8%; Grade 3, 8%)"* (Results, p. 1836)
  y *"Grade 0 in 40% (Grade 1, 37%; Grade 2, 11.5%; Grade 3, 11.5%)"* (Results, p. 1837).
  El 31 y el 60 salen de 100-69 y 100-40. Los grados suman exactamente 100 en cada brazo,
  asi que **la derivacion es aritmeticamente correcta**. El problema no es el numero: es
  como esta registrado y como se pensaba usar.
- **Por que importa:** tres problemas distintos, en orden de gravedad.
  1. **Atribucion.** Escribir "31-60% (Zwingmann et al. 2009)" en la tesis atribuye al
     paper un texto que no contiene. Por la regla 2 de `CLAUDE.md`, toda cifra necesita
     evidencia textual, y esta no la tiene. Hay que presentarlo como calculo propio a
     partir de las tasas de Grado 0, nunca entrecomillado.
  2. **Categoria.** Un "rango 31-60%" sugiere una sola distribucion con incertidumbre.
     No lo es: son dos poblaciones separadas por tecnica quirurgica, con diferencia
     estadisticamente significativa, *"We observed a greater percentage of correct screw
     positions (p = 0.02) in the navigated group"* (Results, p. 1836). Colapsarlas en un
     rango borra justamente la variable que las explica.
  3. **Confusion con otra cifra.** El unico rango de malposicion que el paper si escribe
     literal es **2% a 15%**: *"Screw malposition rates with fluoroscopic guidance have
     been reported to range from 2% to 15%"* (Introduction, p. 1834), y es **citado** de
     Hinsche 2002 y Templeman 1996, no medido aqui. Conviene tener claro cual es cual
     antes de la sustentacion.
- **Lo que si sostiene el paper, y es mejor de lo que estaba registrado:** una escala
  ordinal de brecha cortical con umbrales metricos (0 / <2 / 2-4 / >4 mm), medida por TC
  postoperatoria por un radiologo independiente, y **dos distribuciones completas de
  cuatro grados**, no dos numeros sueltos. Eso es mas rico que un rango.
- **Seccion afectada:** benchmark del alcance MINIMO VIABLE. Definicion de la
  comparacion de distribuciones de SAP. Redaccion de toda cita a esta fuente.
- **Opciones:**
  1. **Recomendada.** Reformular el objetivo: en vez de comparar SAP contra un rango
     31-60%, comparar la distribucion generada contra **las dos distribuciones de cuatro
     grados**, condicionando por tecnica. Es mas fuerte, no mas debil: el muestreador
     pasa de reproducir un rango a reproducir una distribucion ordinal medida, y puede
     ofrecer dos modos (navegado / convencional). Ademas la escala de grados es la misma
     que la de BFC, asi que las dos metricas quedan sobre un eje comun.
  2. Mantener el uso de 31% y 60% como cotas, pero escritas explicitamente como calculo
     propio y como dos poblaciones, nunca como rango citado.
  3. Buscar una fuente clinica con tasa agregada real si se quiere un rango unico. Exige
     PDF nuevo y no esta claro que exista con esta granularidad.
- **Pendiente de:** decision de la autora. La opcion 1 cambia una linea de
  `00-tesis.md`, que Claude no toca.
- **Efecto colateral util:** el paper toma su escala de `smith2006iliosacral`
  (*"graded according to an established classification method used for correct pedicle
  screw placement [23]"*, Materials and Methods, p. 1835, donde [23] es Smith et al.,
  Spine 2006;31:234-238). Queda confirmada la cadena de la escala de BFC:
  literatura de tornillos pediculares -> `smith2006iliosacral` -> `zwingmann2009navigated`.
  Las dos fuentes N1 de la tesis usan la MISMA escala. Eso refuerza la actualizacion de
  la implicancia #4.

### 13 CLINIC-metal esta casi sin anotar, y el dataset no cuantifica la degradacion por metal — ABIERTA
- **Origen:** `liu2021ctpelvic1k` leido con `lector-papers` el 2026-09-06. El rol de
  "dataset primario" se confirma y el nivel 1 se sostiene, pero aparecen tres reservas
  que no estaban en el registro y que tocan cosas distintas.
- **Hallazgo 1 — anotacion.** De los 75 volumenes de CLINIC-metal, **solo 14 tienen
  ground truth**. Los 61 restantes quedaron sin etiquetar por decision explicita de los
  autores: *"Due to the difficulty of labeling the CLINIC-metal, CLINIC-metal is taken
  off in our supervised training phase"*.
- **Hallazgo 2 — que metal es.** El paper **nunca dice** que tipo de material contienen
  esos volumenes. Ni tornillos, ni placas, ni protesis: **NO ENCONTRADO EN EL PDF**. La
  tesis sintetiza implantes de **osteosintesis**; que el subconjunto que le da nombre a
  su dominio contenga osteosintesis y no artroplastia es un supuesto sin respaldo textual.
- **Hallazgo 3 — la premisa.** El paper **no reporta ninguna cifra de degradacion de
  desempeno en presencia de metal**. Solo la afirmacion cualitativa de que es la
  variacion mas dificil de manejar. La premisa central de la tesis —que la segmentacion
  osea se degrada cerca del metal— no tiene numero de partida en su propio dataset.
- **Hallazgo 4 — metrica.** El paper reporta **HD, no HD95**, y **en voxeles, no en mm**.
  El Objetivo 5 promete HD95. Comparar contra las cifras publicadas exige recalcular o
  declarar que no son comparables.
- **Por que importa:** el Objetivo 5 (alcance COMPLETO) evalua aguas abajo con Dice y
  HD95 sobre este subconjunto. Con 14 volumenes anotados, ese conjunto de evaluacion es
  muy chico para sostener una conclusion, y la comparacion contra el baseline publicado
  no es directa. Y si nadie ha cuantificado la degradacion, la tesis tiene que producir
  esa cifra ella misma antes de poder decir que la mejora.
- **Seccion afectada:** Objetivo 5, diseno de la evaluacion downstream. Premisa del
  Problem Statement. `docs/02-datos.md`, que deberia registrar el 14 de 75.
- **Opciones:**
  1. Convertir la cuantificacion de la degradacion en un resultado propio previo al
     Objetivo 5: medir Dice sobre los 14 anotados con y sin zona peri-implante. Es
     trabajo extra, pero convierte una premisa prestada en un resultado.
  2. Verificar en el portal del dataset si la anotacion de CLINIC-metal se amplio desde
     2021. El paper es de 2021 y el repositorio pudo actualizarse; esto no se puede
     resolver leyendo el PDF.
  3. Confirmar el tipo de metal inspeccionando los volumenes directamente. Es dato
     observable, no bibliografico.
  4. Si 14 volumenes resultan insuficientes, evaluar aumentar el conjunto anotando, o
     mover la evaluacion downstream a un conjunto sintetico con ground truth conocido.
- **Pendiente de:** las opciones 2 y 3 no dependen de nadie mas y deberian hacerse antes
  de comprometer el diseno del Objetivo 5.

### 8 — AGRAVADA tras leer wu2022xcist (2026-09-06)
La lectura que iba a cerrar esta implicancia la empeoro. `wu2022xcist` **si** entrega
parametros reimplementables, y en eso atenua lo que dejo `deman2007catsim`: distancia
fuente-isocentro 540 mm, SDD 950 mm, 900 columnas y 16 filas de detector, 1000 vistas por
rotacion, espectro 120 kVp, filtro de aluminio 3.0 mm, 20 bins de energia, ruido
electronico 3500 e-, mas las ecuaciones explicitas de deteccion y de scatter.

Pero falla justo donde la tesis lo necesita:

1. **No contiene ningun estudio de artefacto metalico.** El metal aparece solo como dos
   varillas (titanio 20 mm, hierro 10 mm) dentro de un fantoma cuyo objetivo declarado es
   otro. No usa la expresion *metal artifact*, no reporta ninguna metrica de artefacto
   metalico, no compara contra adquisiciones reales con implantes. La unica correccion de
   endurecimiento listada es *"Water beam-hardening correction"*: basada en agua, no en
   metal.
2. **Su propia validacion esta declarada incompleta.** *"The results presented in this
   report represent a qualitative and semi-quantitative first-order evaluation"*
   (Validation, p. 9), *"More thorough and rigorous evaluation is planned"* (p. 9),
   *"Validation of the noise and resolution modeling capability is in progress"* (p. 16).
   La comparacion contra un escaner real se declara en curso, sin metricas.
3. **Faltan piezas para una reimplementacion fiel**: los valores de C, H y w del modelo de
   scatter, la curva DQE en funcion de la energia, el perfil del bowtie y los espectros
   numericos remiten a archivos externos o a otra publicacion. **NO ENCONTRADO EN EL PDF**.
4. **Confound metodologico nuevo, no registrado antes.** XCIST no opera sobre imagenes
   reconstruidas: hay que convertirlas en fantoma voxelizado, *"Voxelized phantoms can be
   produced from patient images by assigning a material or a mixture of materials to each
   voxel based on its CT number"* (Phantoms, p. 5), re-simular y **re-reconstruir**. Eso
   mete un ciclo extra de reconstruccion que el renderizador LDM no sufre. El PDF no
   cuantifica el error de ese ciclo. Comparar los dos brazos sin aislar ese efecto seria
   una comparacion sesgada en contra de XCIST.
5. **La acusacion de `yun2026simulationdriven` queda corroborada.** El PDF no declara en
   ningun momento proyectores en GPU ni diferenciables; la unica referencia a hardware
   propio es *"take a few minutes on a PC with 12 CPU-cores"* (p. 7).

Dato util a favor: las varillas demostradas son de 2.0 cm y 1.0 cm de diametro, **ambas
por debajo** del umbral de 3.0 cm donde `haneda2025aapm` reporta distorsion del trazo
metalico. El limite no esta anticipado ni contradicho por este PDF.

**Consecuencia:** la formulacion honesta del alcance COMPLETO no es "reimplementacion
validada de XCIST como brazo de comparacion", sino "referencia fisica cualitativa,
parcialmente reimplementable". La opcion 1 de esta implicancia (leer `wu2022xcist` antes
de decidir) queda ejecutada y **descartada como salida**. Quedan vivas la opcion 3
(adoptar el protocolo ya parametrizado de `peters2025hybrid` y `haneda2025aapm`) y la
opcion 4 (declararlo opcional). La opcion 3 gana peso: ese protocolo usa CatSim dentro de
XCIST pero ya calibrado y con scoring publicado, lo que evita reimplementar y valida.


### 9 — ACTUALIZACION tras leer peters2025hybrid (2026-09-06)
La pata (c) del reclamo de novedad —la pose muestreada de la distribucion clinica en vez
de colocada al azar— **ya no es una conjetura: tiene admision escrita del estado del
arte**. `peters2025hybrid`, Discussion, p. 9:

> *"the location of the metal objects in the training dataset was randomized to enable
> the creation of a large dataset. Ideally, virtual metals would be placed only in
> realistic locations, but this was not done since manual metal placement was
> impractical."*

Es el trabajo mas completo y reciente del area diciendo que la colocacion anatomicamente
plausible a escala es impracticable a mano, y por eso la abandona. El muestreador es
exactamente el componente que falta. Confirmado en Metodos: *"Up to five virtual metal
objects were then inserted in random soft tissue or bone positions"* (2.3, p. 4).

Matiz de rigor, para no sobrevender: la aleatoriedad aplica al **dataset de entrenamiento
(14 000 casos)**. El **benchmark de scoring (29 escenarios)** si usa colocacion manual
experta, en *"meaningful locations"*, pero el PDF **no da ninguna regla anatomica ni
criterio cuantitativo** para esa palabra: **NO ENCONTRADO EN EL PDF**. O sea: lo manual
no escala y lo que escala es aleatorio. Ese es el hueco, dicho con precision.

Refuerzo adicional: tampoco modelan los cambios anatomicos de la cirugia, *"Concomitant
anatomical changes due to surgery, such as swelling, bone ablation or drilled holes
within the patient cannot be covered"* (Discussion, p. 9), y avisan del riesgo:
*"special attention must be paid regarding feature hallucination of such regions"*. Eso
abre espacio a BFC y a la contencion cortical.

Con esto, la opcion 1 de esta implicancia (reenunciar el gap como conjuncion de a+b+c)
pasa de recomendable a claramente sostenible, y la pata (c) es la que tiene la cita mas
fuerte de las tres.

### 14 peters2025hybrid da la base operacional de BFC e ISC, y el benchmark no cubre osteosintesis pelvica — ABIERTA
- **Origen:** `peters2025hybrid` leido con `lector-papers` el 2026-09-06. Es la lectura
  mas productiva de todas las rondas. Tipo GAP, no RIESGO: casi todo lo que trae juega a
  favor.
- **Hallazgo 1 — definiciones operacionales que la tesis no tenia.** El paper es la fuente
  primaria y unica de las dos metricas sobre las que se pueden construir BFC e ISC:
  - **bone integrity** (Sec. 2.5, pp. 5-6): *"All voxels with a CT number above 150 HU,
    excluding those in the metal ground truth geometry, are considered bone. Bone
    integrity is assessed via the change of volume as well as with the Sorensen-Dice
    coefficient (SDC)... SDC = 2(X∩Y)/(X+Y)"*.
  - **metal integrity** (Sec. 2.5, p. 6): umbral **adaptativo por ROI**, *"all voxels
    above the highest CT number within a ROI covering the metal ground truth and adjacent
    tissue plus an empirically determined margin of 250 HU"*.
  Aviso: el umbral de metal integrity **no es 250 HU absoluto**, es max-HU-del-ROI + 250.
  Citarlo como umbral fijo seria un error.
- **Hallazgo 2 — la inversion de las metricas funciona, pero no para todas.** El benchmark
  compara (ground truth sin metal, imagen corregida) y penaliza la desviacion. La tesis
  compara (original sin metal, sintetizada con metal), donde la desviacion dentro de
  B_delta **es la senal buscada, no el error**. Analisis metrica por metrica en la ficha.
  Resumen: **metal integrity** sobrevive casi directa y con MEJOR ground truth que el
  paper, porque la mascara CAD del banco de 61 geometrias es geometria exacta;
  **bone integrity** sobrevive excluyendo el volumen del implante, y es BFC medido como
  perdida de continuidad cortical; **streak amplitude** sobrevive como comparacion
  distribucional contra CLINIC-metal real; **sharpness** y **noise** como restricciones de
  no-degradacion fuera de B_delta; **RMSE y SSIM** solo en el complemento de B_delta;
  **proton beam range** no aplica. Ninguna conserva su escala 0-4, porque el ancla NMAR=2
  no tiene analogo en sintesis.
- **Hallazgo 3 — el benchmark no cubre osteosintesis pelvica.** Cubre protesis de cadera
  en pelvis (Tabla 2: *"Hip implant (40%) / Titanium or cobalt / 10-50 mm"*) y
  osteosintesis **espinal** (*"Spinal screws (Ti, n=2, cat III)"*, *"Spinal rods"*), pero
  tornillos iliosacros, placas acetabulares o cualquier osteosintesis del anillo pelvico:
  **NO ENCONTRADO EN EL PDF**. Es el hueco exacto que ocupa la tesis, y ahora esta
  documentado por ausencia en el benchmark de referencia del area.
- **Por que importa:** resuelve tres cosas a la vez. Da definicion citable a BFC e ISC,
  que hasta hoy no tenian formula; refuerza la pata (c) de la implicancia #9; y abre la
  salida de la implicancia #8, porque este protocolo ya esta calibrado y publicado, asi
  que adoptarlo evita la reimplementacion de XCIST que resulto no sostenible.
- **Seccion afectada:** definicion de BFC e ISC (Objetivo 4); brazo de comparacion
  (Objetivo 3); Related Work.
- **Opciones:**
  1. Definir BFC sobre bone integrity e ISC sobre metal integrity, con la inversion
     documentada en la ficha. Es la via mas solida: metricas heredadas de un benchmark
     publicado, no inventadas.
  2. Adoptar el protocolo completo como brazo de comparacion en vez de reimplementar
     XCIST (cierra la #8 por la opcion 3).
  3. Citar la ausencia de osteosintesis pelvica en el benchmark como evidencia del gap.
- **Pendiente de:** decision de la autora. Ninguna opcion exige lectura adicional.
- **Advertencia de nivel 1:** el mapeo exacto de cada metrica a la escala 0-4 **no esta
  en el PDF**; solo se recupera del codigo en GitHub. Si la tesis cita la escala, hay que
  leer ese codigo o citar solo el ancla NMAR = 2. Registrado en `_candidatos.md`.
