# 04 — Implicancias sobre la tesis

> Cola de hallazgos que PODRIAN cambiar algo del documento.
> La alimenta cualquier actividad: lecturas, tareas del asesor, experimentos.
> Claude escribe aqui. La autora decide: al resolver una entrada, la decision
> definitiva se copia a `01-decisiones.md` y aqui queda como APLICADA.

Estados: ABIERTA | APLICADA | DESCARTADA

> **Estado vigente S1/S2 (auditoria 2026-09-08):** Gardner esta LEIDO. Sus medidas
> anatomicas respaldan evaluar cada corredor; no aportan un prior ordinal S2.
> #27 CERRADA (sin fenotipos); #28 RESUELTA (van den Bosch leido); #12 CERRADA
> POR DELIMITACION (benchmark ordinal S1 por tecnica, S2 descriptivo). Los bloques
> de lecturas sucesivas conservan estados historicos; no son tareas vigentes.
> Ver la auditoria de Gardner al final para las correcciones de interpretacion.

| # | Fecha | Origen | Hallazgo | Que seccion toca | Tipo | Estado |
|---|---|---|---|---|---|---|
| 1 | 2026-09-06 | Inventario de `papers/` vs `refs.bib`; abstract aportado por la autora | `wang2025adaptiveweighting` es nivel 1 y sostiene la multi-ventana en HU (C3), pero solo hay abstract. Respaldo de C3 queda cualitativo | Metodo (C3, codificacion multi-ventana) | RIESGO | ABIERTA |
| 2 | 2026-09-06 | Abstract de `wang2025adaptiveweighting` | El multi-ventana en CT existe, pero siempre para REMOVER artefactos. Yo lo uso para GENERARLOS. Es desalineacion de tarea y a la vez posible gap | Related Work; justificacion de C3 | GAP | ABIERTA |
| 3 | 2026-09-06 | Abstract de `zhang2026pediclescrew` | Difusion + "CT sintetico" + planificacion de tornillos, publicado. La tarea es otra (traduce CBCT a CT, no inserta implantes), pero el encuadre colisiona con como presento mi novedad | Related Work; Problem Statement | RIESGO | ABIERTA |
| 4 | 2026-09-06 | Abstract de `zhang2026pediclescrew` | Usa una graduacion de brecha cortical con umbral explicito de 2 mm y un "Grade A". Mi BFC se apoya solo en `smith2006iliosacral` | Definicion de la metrica BFC; posiblemente SAP | RIESGO | ABIERTA |
| 5 | 2026-09-06, ACTUALIZADA con el PDF leido | `liu2025pipeline`, leido con `lector-papers` | La colision NO es de metodo: planifica un optimo determinista, sin distribucion de poses, sin tornillos iliosacrales, sin zonas seguras. Pero corre sobre CTPelvic1K y define CSV (distancia al borde oseo) y QID, vecinas de SAP y BFC | Related Work; definicion de SAP y BFC | RIESGO | ABIERTA |
| 6 | 2026-09-06, ACTUALIZADA con los PDFs leidos | `ren2022metalinsertion` y `yun2026simulationdriven`, leidos con `lector-papers` | `ren2022` aporta la frase que FUNDAMENTA el gap (su fisica se rompe con implantes ortopedicos), pero exige datos crudos de fabricante que CTPelvic1K no tiene. `yun2026` es MAR, no segmentacion, pero ya publica cifras sobre CLINIC-metal | Related Work; novedad del renderizador | GAP | ABIERTA |
| 7 | 2026-09-06 | `ramadanov2025safezone` leido con `lector-papers` | La unica fuente de "zona segura" de la bibliografia no da geometria 3D, ni umbral, ni margen: es un procedimiento cualitativo sobre proyeccion 2D con n=1. El muestreador se queda sin fuente operacional para su restriccion principal | Objetivo 2 (alcance MINIMO VIABLE); definicion de la restriccion del muestreador | RIESGO | ABIERTA |
| 8 | 2026-09-06, AGRAVADA con `wu2022xcist` leido | `deman2007catsim`, `yun2026simulationdriven`, `haneda2025aapm` y `wu2022xcist`, los cuatro leidos | La "reimplementacion validada de XCIST" NO es sostenible: el propio paper de XCIST no contiene ningun estudio ni validacion de artefacto metalico, declara su validacion como "first-order" y "in progress", y su pipeline agrega un ciclo de reconstruccion que el renderizador no sufre | Alcance COMPLETO, brazo de comparacion; Objetivo 3 | BASELINE | APLICADA (redacción; ver #17) |
| 9 | 2026-09-06 | Patron transversal de cuatro lecturas: `wang2019cochlear`, `ren2022metalinsertion`, `karageorgos2024ddpm`, `haneda2025aapm` | Insertar metal sintetico en CT para fabricar datos de entrenamiento YA es practica establecida y publicada, en cuatro trabajos independientes. Ademas, difusion latente aplicada a artefactos metalicos ya compitio en el reto AAPM (5to lugar). El gap no puede enunciarse como "insertar metal sintetico" ni como "difusion latente en artefactos metalicos" | Problem Statement; reclamo de novedad completo | GAP | ABIERTA |
| 10 | 2026-09-06 | `chen2024tumorsynthesis` leido con `lector-papers` | Identidad DiffTumor confirmada. Declara que no modela nada fuera de la mascara y trunca HU a [-175, 250]: es respaldo citable directo de B_delta y de la multi-ventana C3 | Justificacion de B_delta (Obj 3) y de C3 (Obj 1) | REDACCION | ABIERTA |
| 11 | 2026-09-06 | `smith2006iliosacral` leido con `lector-papers` | El paper suma al score una SEGUNDA escala, angular (grados <5, 5-10, 11-15, >15), que la tesis no estaba considerando. Y sus tasas por brazo son cadavericas con n=4 y sin significancia: no sirven de prior clinico | Definicion de SAP; supuesto sobre de donde salen los priors del muestreador | RIESGO | ABIERTA |
| 12 | 2026-09-06 | `zwingmann2009navigated` leido con `lector-papers` | El rango "31-60%" NO existe en el PDF. Son dos complementos aritmeticos (100-69 y 100-40) de dos brazos tecnicamente distintos, navegado y convencional. Citarlo como rango del paper seria error de atribucion, y tratarlo como una sola distribucion es error de categoria | Benchmark del alcance MINIMO VIABLE; comparacion de distribuciones de SAP | RIESGO | CERRADA POR DELIMITACION; ver cierre van den Bosch |
| 13 | 2026-09-06 | `liu2021ctpelvic1k` leido con `lector-papers` | CLINIC-metal tiene solo 14 de 75 volumenes anotados: los autores lo excluyeron del entrenamiento supervisado por dificultad de etiquetado. Ademas el paper nunca dice que tipo de metal contiene, y no reporta ninguna cifra de degradacion por metal | Objetivo 5 (downstream); premisa central de la tesis; data card | RIESGO | ABIERTA |
| 14 | 2026-09-06 | `peters2025hybrid` leido con `lector-papers` | Da la definicion operacional de bone integrity (150 HU + SDC) y metal integrity (max HU en ROI + 250), base citable de BFC e ISC. Declara por escrito que la colocacion realista de metal es impracticable a mano, lo que sostiene la novedad del muestreador. Y su benchmark NO cubre osteosintesis pelvica | Definicion de BFC e ISC (Obj 4); brazo de comparacion (Obj 3); Related Work | GAP | ABIERTA |

Tipos: REDACCION (ajustar como lo digo) | ALCANCE (agranda o achica el trabajo)
| GAP (posible nueva contribucion) | RIESGO (amenaza un supuesto mio)
| BASELINE (afecta con que me comparo)

## Actualización 2026-09-06 — encargo de Víctor y decisión de la autora

Evaluación explícita de regla 13: **sí**, el trabajo obliga a ajustar supuestos de
selección de datos y la redacción del baseline; también detecta una incompatibilidad
en la interpretación previa de las métricas. No cambia por sí solo el alcance mínimo.

| # | Fecha | Origen | Hallazgo | Qué sección toca | Tipo | Estado |
|---|---|---|---|---|---|---|
| 15 | 2026-09-06 | Exploración local y observación de la compañera | La revisión 2D anterior no certifica ausencia de objetos; dataset6 debe revisarse también. El registro previo contiene duplicados entre y dentro de datasets. HU solo prioriza | Datasets; separación entrenamiento/prueba; Objetivo 5 | RIESGO | ABIERTA |
| 16 | 2026-09-06 | Contraste de main.tex con la ficha Peters y #14 | ISC significa Inter-slice Consistency en la tesis, pero la ficha la equipara a metal integrity. BFC es Boundary Feature Coherence, no automáticamente Dice óseo ni grado de brecha cortical | Objetivo 4; definición de métricas | RIESGO | ABIERTA |
| 17 | 2026-09-06 | Adopción autorizada de Peters | Adoptar un protocolo MAR 2D no valida su extensión a síntesis 3D; falta materializar versión, configuración, controles y adaptación | Baseline; Objetivos 3–5 | BASELINE | ABIERTA |

### 8 — Decisión de la autora aplicada a la redacción (2026-09-06)

La autora indica explícitamente: «Adoptaremos el protocolo de peters2025hybrid»
y autoriza edición de `tesis/main.tex`. Se aplica la opción 3: el brazo físico se
describe como adopción del protocolo híbrido publicado, y se retiran los umbrales
RMSE ≤30 HU / SSIM ≥0.95 de aprobación de una reimplementación independiente.
Se distingue colocación aleatoria en entrenamiento de colocación experta en scoring.
**Estado de la decisión de baseline: APLICADA a main.tex.** La ejecución y validación
no están completas; se siguen en #17. Los detalles históricos de #8 se conservan.
`docs/00-tesis.md` aún contiene la formulación anterior y `docs/01-decisiones.md`
queda reservado a la autora; se propone registrar allí esta decisión.

### 15 — Revisión 3D y separación de cohortes — ABIERTA

**Cierre medido, 2026-09-07:** 103 CT dataset6 (38 candidatos HU), 75 CT dataset7
(75 candidatos HU), seis grupos de duplicados exactos confirmados (172 contenidos
únicos), cero errores y cero máscaras locales vinculadas por nombre. Tres casos
tienen revisión parcial; ninguno revisión completa. Las cifras se refieren a esta
carpeta local, no a disponibilidad remota ni a un conteo confirmado de metales.

- **Evidencia:** `experiments/exploration/duplicados.csv` registra seis pares de
  volúmenes con vóxeles iguales, tres cruzando dataset6/dataset7. La nueva ejecución
  verifica duplicados mediante SHA256 sobre forma y HU escalados; el resultado
  reproducible queda en `experiments/exploration-3d/resumen.md` y `revision.csv`.
- **Cambio necesario:** revisar 3D y todos los cortes, incluir objetos externos y
  otros cuerpos extraños, resolver duplicados y pacientes antes de separar cohortes.
  Ni un nombre CLINIC ni un resultado HU negativo garantizan una imagen limpia.
- **Implementado:** un único CSV, antecedentes separados de revisión nueva y
  elegibilidad conservadora. No se ha aprobado una cohorte final.
- **Pendiente:** revisión manual, tipo de implante, identidad por paciente y
  disponibilidad/alineación de anotaciones para evaluación supervisada. Ver data card.

### 16 — Integridad del metal no equivale a consistencia entre cortes — ABIERTA

- **Evidencia local:** Objetivo 4 y tabla Expected Results de `tesis/main.tex`
  expanden ISC como *Inter-slice Consistency* y BFC como *Boundary Feature Coherence*.
  La ficha `peters2025hybrid.md` y #14 las vinculan directamente a metal/bone integrity.
- **Implicación:** adoptar Peters no autoriza a cambiar el significado de estas siglas.
  Dice de metal frente a CAD puede complementar ISC, pero no mide por sí solo la
  consistencia entre cortes. Dice/volumen óseo tampoco demuestra continuidad cortical.
- **Otra cautela:** trasladar streak amplitude a CT clínicos sin referencia sin metal
  exige definir un estimador distinto o una referencia justificable. No hay pares
  clínicos sin/con metal garantizados por el inventario.
- **Pendiente:** especificar cada métrica, referencia y ROI; mantener separadas las
  métricas heredadas de Peters y las contribuciones propias. No se sustituyeron
  definiciones de BFC/ISC en main.tex.

### 17 — Adopción del protocolo y validación pendiente — ABIERTA

**Actualización 2026-09-07 — decisión registrada y niveles ajustados:** con permiso
explícito se escribió la adopción de Peters en `01-decisiones.md`. Peters queda N1
como protocolo adoptado y Wu baja a N2 como fundamento técnico y fuente de límites;
N4 se incorpora para descartes completos, sin entradas por ahora. Se resuelve así
el pendiente de registro de #8; `00-tesis.md` aún requiere armonización de su frase
sobre reimplementación independiente.

**Evaluación explícita de regla 13:** la decisión mantiene impacto sobre el baseline
y su justificación, ya cubierto por #8 y #17. La recategorización no es un hallazgo
experimental ni valida la adaptación; no abre un gap ni modifica el alcance mínimo.
Se actualiza esta entrada ABIERTA en lugar de duplicar la misma implicancia.

- **Base documental:** ficha Peters ya leída, secciones de limitaciones y reutilización.
  La validación publicada es para su diseño; su adopción no certifica el nuestro.
- **Aplicación autorizada:** main.tex declara la adaptación, mismas anatomías/poses
  entre brazos y un control de simulación/reconstrucción sin metal para separar su error.
- **Pendiente técnico:** fijar revisión del código y configuración, verificar acceso
  y licencia, reproducir ejemplos y definir tratamiento 2D/2.5D/3D y métricas de síntesis.
  La escala MAR 0–4 y su calibración no se trasladaron automáticamente.

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

### 12 El benchmark 31-60% no es una cita: es un calculo propio sobre dos poblaciones distintas — CERRADA POR DELIMITACION
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

---

## Actualización 2026-09-07 — auditoría del encargo de Víctor

Evaluación explícita de regla 13: **sí hay implicancia.** No por el resultado del
inventario, que ya estaba registrado en #15, sino por su cobertura: la descripción de
datos que se va a entregar y a citar en la tesis no cubre CTPelvic1K, cubre dos de sus
siete sub-datasets. Eso toca la sección Datasets y cualquier frase sobre generalización.

| # | Fecha | Origen | Hallazgo | Qué sección toca | Tipo | Estado |
|---|---|---|---|---|---|---|
| 18 | 2026-09-07 | Auditoría de `experiments/exploration-3d` contra el encargo de Víctor | Solo hay 178 de los 1184 volúmenes de CTPelvic1K en disco (CLINIC 103 y CLINIC-metal 75). Faltan ABDOMEN, COLONOG, MSD_T10, KITS19 y CERVIX: 1006 volúmenes. Además la correspondencia `dataset6`→CLINIC y `dataset7`→CLINIC-metal es una inferencia por conteo, spacing y dimensiones, no un dato declarado en los archivos | Datasets; alcance del entrenamiento; Objetivo 5 | DATOS | ABIERTA |

### 18 — La base local es CLINIC + CLINIC-metal, no CTPelvic1K — ABIERTA

- **Origen:** auditoría de `experiments/exploration-3d` del 2026-09-07, contrastada con
  la Tabla 1 de `liu2021ctpelvic1k` (p. 3) ya verificada en su ficha.
- **Hallazgo:** en `data/` hay 178 CT: 103 en `dataset6` y 75 en `dataset7`. El paper
  declara 1184 volúmenes en siete sub-datasets. Los cinco públicos (ABDOMEN 35,
  COLONOG 731, MSD_T10 155, KITS19 44, CERVIX 41 = 1006) no están descargados.
- **Por qué importa:** dos cosas distintas. Primera, el entregable a Víctor dice
  «datasets» y hoy solo puede describir dos; hay que decir que es inventario local o
  descargar el resto. Segunda, y más de fondo: si el entrenamiento del renderizador se
  alimenta solo de CLINIC, el modelo ve un único origen clínico, un único protocolo de
  adquisición y spacing en un rango estrecho (0.64–1.129 mm en plano). La robustez que
  la tesis promete aportar se mediría sobre la variabilidad que el propio dataset
  primario aporta para eso.
- **Segundo hallazgo, menor:** la correspondencia `dataset6`→CLINIC y
  `dataset7`→CLINIC-metal no está declarada en ningún header NIfTI. Se sostiene por
  coincidencia de conteo (103 y 75), spacing (0.85/0.83 en plano, 0.80 en z) y
  dimensiones (512, 512, ~345 y ~334) con la Tabla 1. Es consistente, pero en la tesis
  debe enunciarse como identificación inferida, no como metadato.
- **Cuantificación que refuerza #15:** 38 de los 103 volúmenes de `dataset6` superan
  2500 HU, y los 75 de `dataset7` también. `dataset6` no es un conjunto limpio por
  defecto; el nombre del sub-dataset no define la cohorte de entrenamiento.
- **Sección afectada:** Datasets; separación entrenamiento/prueba; cualquier afirmación
  de generalización del renderizador.
- **Opciones:**
  1. Descargar los cinco sub-datasets faltantes y rehacer el inventario (el script ya
     escala: `explorar.py inventario` conserva las anotaciones manuales por Caso).
  2. Declarar explícitamente que el alcance de datos es CLINIC + CLINIC-metal y ajustar
     las afirmaciones de generalización a ese límite.
  3. Preguntar a Víctor si el encargo pedía la descripción de las siete filas.
- **Pendiente de:** decisión de la autora y consulta al asesor. No requiere más lectura.

---

## Actualización 2026-09-07 — clasificación visual asistida de los 113 candidatos

Evaluación explícita de regla 13: **sí, y en cuatro frentes.** Corrieron 12 agentes
`clasificador-metal` sobre los 113 candidatos HU; 113 filas en
`experiments/exploration-3d/propuesta_clasificacion.csv`, todas `propuesta sin validar`.
Ninguna toca `revision.csv` y no hay cohortes nuevas. Lo que cambia no es el conteo:
es que el criterio de selección de datos resultó menos fiable de lo que suponía el
diseño del inventario.

| # | Fecha | Origen | Hallazgo | Qué sección toca | Tipo | Estado |
|---|---|---|---|---|---|---|
| 19 | 2026-09-07 | Clasificación visual asistida, lotes 03, 05, 09, 10 | El umbral HU no detecta ni certifica: `dataset6_CLINIC_0074_data` es candidato por 1 vóxel pero contiene un objeto tubular por DEBAJO de 1500 HU que ningún umbral de ese rango encuentra; el artefacto fabrica «componentes» que son cortical realzada; y la mesa del escáner entra como componente | Selección del conjunto limpio; data card; Objetivos 1 y 3 | RIESGO | ABIERTA |
| 20 | 2026-09-07 | Lotes 03, 07, 02. Criterio de duplicados cruzados APLICADO en `01-decisiones.md` 2026-09-07; sigue abierto el representante de los 3 grupos internos de dataset7 | Duplicados exactos CRUZADOS entre sub-datasets: `dataset7_CLINIC_metal_0064` = `dataset6_CLINIC_0070` y `dataset7_CLINIC_metal_0036` = `dataset6_CLINIC_0048`. Además `metal_0059` y `metal_0071` comparten geometría y HU mínimo sin compartir SHA256 | Separación entrenamiento/prueba; Objetivo 5 | RIESGO | ABIERTA |
| 21 | 2026-09-07 | Lotes 03, 05, 09, 10 | Estar en CLINIC-metal no implica osteosíntesis pélvica intracorpórea: en `metal_0036` el único material sobre umbral es extracorpóreo junto al antebrazo; `metal_0074`/`metal_0046` muestran objetos de superficie con HU 24 340 y morfología no de implante; `CLINIC_0089` tiene antecedente «metal» con lo denso fuera del contorno | Conjunto de prueba con metal; Objetivo 5; premisa de la tesis | RIESGO | ABIERTA |
| 22 | 2026-09-07 | Lotes 09 y 12, ambos trabados en lo mismo | `Objeto extraño` no está definido: ¿cualquier material no anatómico, incluida la mesa y la ropa, o solo cuerpo extraño distinto del implante? La regla actual de exclusión de entrenamiento depende de esa columna | Criterio de exclusión del entrenamiento; data card | DEFINICION | ABIERTA |

### 19 — El umbral HU no es un criterio de detección — ABIERTA

- **Origen:** revisión asistida de las láminas de los 113 candidatos, 2026-09-07.
- **Hallazgo, en tres formas distintas del mismo problema:**
  1. **Falso negativo.** `dataset6_CLINIC_0074_data` entra a la lista de candidatos por
     **un solo vóxel** sobre 2500 HU (HU máx 2540). Pero las proyecciones muestran una
     estructura tubular larga y curva con un lazo cerrado en pelvis media (axiales
     164-174) que **no está** entre los vóxeles sobre umbral. Reejecutado a 1500 HU
     aparecen 12 componentes y ninguno es esa estructura: son hueso denso. El objeto
     vive por debajo de 1500 HU.
  2. **Componentes fabricados.** En `dataset7_CLINIC_metal_0042_data` el componente 4
     (2485 vóxeles) es cortical ilíaca realzada por endurecimiento de haz y estrías que
     cruzan 2500 HU, no una pieza discreta.
  3. **Contaminación por el entorno.** En `metal_0002`, `metal_0026` y `metal_0038`
     aparecen componentes de 5-26 vóxeles a x cerca de -174 mm RAS, sobre el arco de la mesa.
- **Por qué importa:** el inventario usa «candidato HU» para priorizar, y eso sigue
  siendo válido. Lo que ya no se sostiene es la idea implícita de que **los 65 no
  candidatos de dataset6 son el lugar donde buscar volúmenes limpios**: si un objeto
  puede quedar bajo 1500 HU, la lista de candidatos no es un superconjunto de los
  volúmenes con objeto. El conjunto de entrenamiento «sin metal ni objetos extraños»
  no se puede construir descartando por umbral, hay que mirar los 178.
- **Sección afectada:** data card; definición del conjunto limpio de entrenamiento;
  cualquier frase que diga que el entrenamiento usa CT sin material.
- **Opciones:**
  1. Revisar los 178, no solo los 113. Cuesta 65 volúmenes más de láminas (~25 min).
  2. Aceptar el riesgo y declararlo como limitación en la tesis.
  3. Buscar un detector que no dependa de un umbral fijo (p. ej. gradiente local o
     detección de estrías), que es trabajo adicional no previsto en el alcance.
- **Pendiente de:** decisión de la autora. La opción 1 es barata y yo la recomiendo.

### 20 — Duplicados cruzados entre sub-datasets: fuga train/test — ABIERTA

- **Origen:** lotes 03, 07 y 02 de la clasificación asistida.
- **Hallazgo:** dos pares de duplicados exactos por vóxeles **cruzan la frontera de
  sub-dataset**: `dataset7_CLINIC_metal_0064_data` = `dataset6_CLINIC_0070_data`, y
  `dataset7_CLINIC_metal_0036_data` = `dataset6_CLINIC_0048_data`. Aparte,
  `metal_0059` y `metal_0071` tienen el mismo spacing, el mismo HU mínimo y una
  configuración casi idéntica pero SHA256 distintos: el hash no los agrupa y podrían
  ser dos estudios del mismo paciente.
- **Por qué importa:** el reparto más natural (dataset6 como entrenamiento limpio,
  dataset7 como prueba con metal) mete el mismo volumen a ambos lados. Es fuga directa,
  y el `Grupo duplicado` del inventario la detecta solo porque el hash coincide; el caso
  `0059`/`0071` muestra que hay repeticiones que el hash **no** detecta.
- **Sección afectada:** separación entrenamiento/prueba; validez del Objetivo 5.
- **Opciones:**
  1. Elegir representante por grupo y excluir el gemelo del otro lado del split.
  2. Establecer identidad por paciente con algo más que el hash (geometría, fecha de
     adquisición si el header la trae, correlación de contenido).
- **Pendiente de:** decisión de la autora. Bloquea cualquier split.

### 21 — Estar en CLINIC-metal no implica osteosíntesis pélvica — ABIERTA

- **Origen:** lotes 03, 05, 09 y 10.
- **Hallazgo:** en `dataset7_CLINIC_metal_0036_data` el único material sobre umbral es
  extracorpóreo, junto al antebrazo, sin material intrapélvico visible en las 16 axiales
  ni en los tres MIP. `metal_0074` y `metal_0046` (duplicados entre sí) muestran dos
  objetos de superficie con HU máximo 24 340 y morfología que no corresponde a un
  implante. `dataset6_CLINIC_0089_data` tiene antecedente «metal» de la revisión 2D
  previa, pero lo denso está fuera del contorno corporal.
- **Por qué importa:** conecta directamente con #13, donde quedó registrado que el
  paper **nunca dice qué metal contiene CLINIC-metal**. Ahora hay evidencia local de
  que al menos parte de ese subconjunto no es osteosíntesis pélvica. Si el conjunto de
  prueba del Objetivo 5 se define como «los 75 de CLINIC-metal», se está evaluando la
  síntesis de implantes contra volúmenes cuyo metal puede ser un objeto externo.
- **Sección afectada:** definición del conjunto de prueba; Objetivo 5; la premisa de que
  CLINIC-metal es el escenario clínico objetivo.
- **Opciones:**
  1. Definir un subconjunto «osteosíntesis pélvica confirmada» dentro de CLINIC-metal,
     y decir cuántos son. Es trabajo de revisión, no de lectura.
  2. Evaluar sobre todo CLINIC-metal y declarar la heterogeneidad como limitación.
- **Pendiente de:** revisión de la autora y, probablemente, consulta a Víctor.

### 22 — `Objeto extraño` no tiene definición operativa — ABIERTA

- **Origen:** dos agentes independientes (lotes 09 y 12) se trabaron en la misma duda.
- **Hallazgo:** la guía dice que la columna «incluye implantes, DIU, clips y objetos
  externos», lo que leído al pie marca `sí` por la mesa de exploración o por un botón
  de la ropa. Pero la regla de cohortes exige `Objeto extraño = no` para entrar a
  entrenamiento. Con la lectura amplia, casi ningún volumen entra.
- **Por qué importa:** esa columna es el filtro de entrada al entrenamiento. Su
  definición decide el tamaño del conjunto limpio, no es un detalle de anotación.
- **Opciones:**
  1. Restringir a material no anatómico **dentro del contorno cutáneo**, y tratar mesa,
     ropa y soportes como artefacto de adquisición, no como objeto extraño.
  2. Mantener la lectura amplia y añadir una columna aparte para lo extracorpóreo.
- **Pendiente de:** decisión de la autora. Es barata y desbloquea la columna entera.

---

## Actualización 2026-09-07 — revisión 3D de la autora fusionada con la de los agentes

Evaluación explícita de regla 13: **sí.** La revisión 3D completa de los 178 volúmenes
cierra en criterio dos entradas abiertas (#20, #21), deja una decidible en una línea
(#22) y deja #19 con un conflicto concreto sin resolver. No aplico nada a `main.tex`
ni a `00-tesis.md`; las reglas de clasificación son de la autora y deben pasar a
`01-decisiones.md` de su puño.

### Reglas de clasificación dictadas por la autora (2026-09-07)

1. `dataset6`: columna 2 vacía o `nada` = no encontró implante ni material metálico.
   Con texto = ese es el objeto metálico.
2. `dataset7`: columna 2 vacía = **sí hay material ortopédico**. Con texto = material
   ortopédico **y además** lo anotado.
3. Duplicados: si el grupo tiene un volumen en dataset7 y otro en dataset6, **prevalece
   el de dataset7** como representante. Y ese volumen de dataset7 **no** contiene
   material ortopédico, porque ningún volumen de dataset6 lo tiene.

Aplicadas sobre las 178 filas, con la investigación de los agentes añadida en
`Ubicación anatómica`, `Lateralidad`, `Artefactos`, `Severidad`, `Confianza` y `Notas`.
Copia previa a la fusión en `experiments/exploration-3d/revision.previo-merge.csv`.

### Números que salen de la fusión

| Magnitud | Valor |
|---|---:|
| dataset7 con material ortopédico | 72 de 75 |
| ...de contenido único (descontando 3 duplicados internos de dataset7) | 69 |
| dataset7 SIN material ortopédico (duplicados cruzados con dataset6) | 3 |
| dataset6 con objeto metálico | 33 de 103 |
| ...de ellos, solo material extracorpóreo (ropa, piel) | 27 |
| ...con DIU (intracorpóreo) | 6 |
| dataset6 sin objeto = candidatos a entrenamiento limpio | 70 |

### 20 — Duplicados cruzados: criterio RESUELTO por la autora, falta registrarlo

- **Decisión dictada:** dataset7 prevalece siempre como representante del grupo cruzado,
  y esos volúmenes quedan marcados sin material ortopédico. Afecta a tres grupos:
  `metal_0061` = `CLINIC_0037`, `metal_0036` = `CLINIC_0048`, `metal_0064` = `CLINIC_0070`.
- **Lo que sigue abierto:** los tres grupos internos de dataset7 (`0012`/`0021`,
  `0013`/`0043`, `0046`/`0074`) no tienen regla: los dos miembros son de dataset7 y
  ambos tienen material ortopédico. Hay que elegir representante igual, o el mismo
  volumen entra dos veces al conjunto de prueba.
- **`metal_0059` / `metal_0071`: DESCARTADO.** La autora confirma explícitamente el
  2026-09-07, tras revisarlos en 3D, que **no son el mismo paciente**. Comparten spacing
  y HU mínimo, nada más. No se toma ninguna acción sobre ese par y no se les asigna
  `Grupo paciente` común. Registrado en `01-decisiones.md`.
- **Pendiente de:** que la autora copie la regla 3 a `01-decisiones.md`, y que decida
  representante en los tres grupos internos.

### 21 — CONFIRMADA con cifra: 3 de 75 de CLINIC-metal no tienen osteosíntesis

- La revisión 3D confirma lo que los agentes habían señalado: `metal_0036`,
  `metal_0061` y `metal_0064` no contienen material ortopédico. Son duplicados exactos
  de volúmenes de CLINIC, y su contenido denso es zipper, electrodos o DIU.
- **Consecuencia para el Objetivo 5:** el conjunto de prueba con metal no son 75
  volúmenes, son **72**, y de contenido único **69**. Definir el test como «los 75 de
  CLINIC-metal» sobrestima el conjunto y mete tres volúmenes sin implante.
- **Sección afectada:** definición del conjunto de prueba; cualquier cifra de tamaño
  del test en la tesis.

### 22 — La definición de `Objeto extraño` ahora tiene precio en volúmenes

- De los 33 volúmenes de dataset6 con objeto, **27 son solo material extracorpóreo**
  (cierres de cremallera, botones, electrodos de superficie, accesorios de ropa) y 6
  contienen DIU, que sí es intracorpóreo.
- **Por eso importa la definición:** con la lectura amplia actual, el conjunto limpio de
  entrenamiento es de **70** volúmenes. Si `Objeto extraño` se restringe a material no
  anatómico **dentro del contorno cutáneo**, pasa a **97**. Son 27 volúmenes, un 38 %
  más de datos de entrenamiento, decididos por una línea de definición.
- **Advertencia:** los objetos extracorpóreos igual producen estrías que atraviesan la
  pelvis. «Limpio de objeto» y «limpio de artefacto» no son lo mismo, y la decisión
  debería decir cuál de los dos exige el entrenamiento del renderizador.
- **Pendiente de:** decisión de la autora.

### 19 — Conflictos RESUELTOS por la autora; la entrada se estrecha

Resolución del 2026-09-07, dictada por la autora:

- **`CLINIC_0074`: no es metal.** Confirma que hay una estructura en lazo evidente, pero
  no es material ortopédico ni metálico, así que no se anota como objeto. El volumen
  sigue siendo candidato a entrenamiento limpio.
- **Regla general:** si la autora anotó «sin objeto» y el agente quedó `incierto`, manda
  «sin objeto». Cierra los cinco desacuerdos menores.

**Qué queda vivo de #19 tras esto.** La pata del falso negativo pierde fuerza *para
metal*: el objeto sub-1500 HU de `CLINIC_0074` existe, pero no es metálico, así que el
umbral no dejó escapar ningún implante. Siguen en pie las otras dos patas, que no
dependen de ese caso: el artefacto fabrica componentes que no son piezas
(`metal_0042` comp4, cortical realzada) y la mesa del escáner entra como componente
(`metal_0002`, `metal_0026`, `metal_0038`). Y sigue en pie la advertencia de fondo para
#22: si «objeto extraño» llegara a incluir material no metálico, un umbral en HU no es
el instrumento para encontrarlo.

### 19 — Texto original del conflicto (histórico)

- `dataset6_CLINIC_0074_data`: la autora no anotó objeto tras revisar el 3D; el agente
  reportó una estructura tubular larga con lazo cerrado en pelvis media, axiales
  164-174, **por debajo de 1500 HU**. Las superficies 3D se calculan a 300, 1500, 2500 y
  3500 HU, así que un objeto sub-1500 se confunde con la superficie de 300 HU (piel y
  partes blandas): es esperable que la revisión 3D no lo vea.
- Otros cinco desacuerdos, todos con el agente en `incierto` y la autora en «sin objeto»:
  `CLINIC_0039`, `CLINIC_0058`, `CLINIC_0066`, `CLINIC_0077` (los tres primeros y el
  último, borde del FOV) y `CLINIC_0068` (aquí el agente propuso `no` y la autora sí
  anotó objeto).
- **Por qué no lo cierro solo:** si `CLINIC_0074` tiene un objeto, está hoy dentro de los
  70 candidatos a entrenamiento limpio. Es exactamente el modo de fallo que #19 describe.
- **Pendiente de:** que la autora mire `CLINIC_0074` en cortes, no en 3D.

### Nota de método, sin implicancia

`Revisión 3D y cortes` quedó en `3D completa`, no en `completa`, porque la revisión fue
del 3D y no del recorrido de cortes. Por eso ninguna cohorte se asigna todavía; el otro
bloqueo es `Grupo paciente`, vacío en las 178 filas.

---

## Actualizacion 2026-09-07 — consulta de alcance a 3 meses de la entrega

### 23 — Recortar por el Objetivo 4 no acorta el camino critico — ABIERTA

- **Origen:** consulta de la autora del 2026-09-07. Quedan 3 meses y percibe el alcance
  como demasiado grande; propone adoptar las metricas de Peters en vez de formalizar BFC
  e ISC. Analisis sobre entradas ya abiertas (#7, #8, #12, #13, #14, #16, #17, #18).
  **No hay lectura nueva ni cifra nueva**: es una sintesis de lo ya registrado.
- **Hallazgo:** el recorte propuesto actua sobre el **Objetivo 4**, que en `00-tesis.md`
  ya esta en el alcance COMPLETO, no en el MINIMO VIABLE. Recorta el camino opcional,
  no el critico. El camino critico es el MINIMO (Obj 1 + Obj 2 + SAP) y hoy tiene **dos
  cimientos abiertos**:
  - **#7**: el Objetivo 2, unica contribucion propia del minimo, se queda sin fuente
    operacional de zona segura (`ramadanov2025safezone` es piloto sobre una sola CT, en
    proyeccion 2D, sin umbral numerico).
  - **#12**: SAP dice compararse contra un 31-60% que **no aparece** en
    `zwingmann2009navigated`. Es derivacion propia sobre dos poblaciones distintas.
  Mientras esos dos sigan abiertos, ningun recorte en los objetivos 3-5 cambia el riesgo
  de la sustentacion.
- **Tres consecuencias no registradas antes:**
  1. **Orden de recorte invertido.** El Objetivo 5 (downstream Dice/HD95) es mas caro y
     esta mas bloqueado que el 4: #13 (14 de 75 de CLINIC-metal anotados) y #18 (178 de
     1184 volumenes en disco). Si algo sale primero, es el 5, no el 4.
  2. **`Fuera de alcance` esta vacio** en `00-tesis.md`. Mientras nada este declarado
     fuera, todo sigue dentro; la sensacion de exceso no se arregla recortando por
     dentro sino escribiendo esa seccion.
  3. **El titulo promete el renderizador.** `main.tex` titula *"using Multi-Window Latent
     Diffusion"* y la Research Question y la Hypothesis giran sobre el LDM. Si el alcance
     efectivo se reduce al muestreador — el MINIMO que la propia autora declaro
     defendible por si solo — el titulo, la pregunta y la hipotesis dejan de coincidir
     con lo entregado. Ademas el **Objetivo 1 se queda sin consumidor**: valida una
     representacion multi-ventana que ningun modelo llegaria a usar.
- **Sobre adoptar las metricas de Peters, en si:** es legitimo y defendible (heredar de
  un benchmark publicado es mas solido que inventar), pero **no es gratis**: la #16 exige
  renombrar o redefinir. Reportar *bone integrity* y *metal integrity* bajo las siglas
  BFC e ISC deja el Objetivo 4 diciendo "Formalization" sobre algo que no se formalizo.
- **Por que importa:** determina que se entrega en 3 meses y como se enuncia. Recortar
  por el 4 da alivio percibido sin mover la fecha de entrega real.
- **Seccion afectada:** `00-tesis.md` (alcance minimo, alcance completo, fuera de
  alcance, fechas). En `main.tex`: titulo, Research Question, Hypothesis, Objetivos 4 y 5.
- **Opciones:**
  1. **Recomendada.** Congelar el alcance en Obj 1 + Obj 2 + SAP + un renderizador
     demostrativo sin evaluacion downstream. Declarar Obj 5 fuera de alcance por #13 y
     #18. Adoptar las metricas de Peters con **sus propios nombres**, y dejar SAP como
     unica metrica propia. Antes que nada, cerrar #7 y #12.
  2. Mantener Obj 3 completo y sacar Obj 4 y Obj 5. Exige igualmente cerrar #7 y #12.
  3. Reducir al muestreador puro (Obj 1 + Obj 2 + SAP). Es el MINIMO tal como esta
     escrito, pero obliga a retitular la tesis y a reescribir pregunta e hipotesis.
- **Pendiente de:** decision de la autora. Ninguna opcion exige lectura adicional, salvo
  la opcion 1 de #7 (McLaren 2021), que pide un PDF nuevo.

---

### 12 — ACTUALIZACION tras leer hinsche2002fluoroscopy (2026-09-08)

**El 2%-15% tampoco se mide en Hinsche. Es una cita heredada, y la cadena sigue rio
arriba.** Ficha: `docs/literatura/hinsche2002fluoroscopy.md`, PDF completo.

- **Hallazgo 1 — Hinsche no mide ninguna tasa clinica de malposicion.** El rango aparece
  una sola vez, en su Introduccion (p. 135), y esta atribuido a sus propias referencias
  5, 11, 20 y 24: *"has been reported to range between 2% and 15%, even by experienced
  surgeons"*. Esas cuatro son Ebraheim 1993, Keating 1999, Routt 1997 y Templeman 1996.
  Es decir: `zwingmann2009navigated` cita a Hinsche, y Hinsche cita a otros cuatro.
  **Ninguna fuente leida hasta hoy mide ese rango.**
- **Hallazgo 2 — Hinsche es un banco sobre plastico, no un estudio clinico.**
  *"28 plastic pelvic models (Synthes, Oberdorf, Switzerland) were used"* (Materials,
  p. 136), mas 7 modelos adicionales. Sin fractura ni desplazamiento: *"No attempt to
  create a fracture or displacement was made"* (p. 136). La evaluacion fue fisica, no
  radiologica: cortaron el sacro con sierra de banda e inspeccion visual (Measurements,
  p. 138). Sus tasas propias (93% seguro en S1; 71% y 64% en S2, Discussion pp. 141-142)
  **no son prior clinico** y no deben citarse como tal. Los autores mismos avisan que el
  modelo se desvia de la anatomia real (*"The alar slope of the plastic model seemed to
  be steeper"*, p. 141) y cierran declarandose preclinicos: *"have led to initiation of a
  clinical trial"* (p. 143).
- **Hallazgo 3 — dos definiciones de malposicion que NO son intercambiables.** Hinsche usa
  un criterio **binario**: *"unsafe when the screw path perforated one of the cortices
  while jeopardizing neurovascular structures"* (Measurements, p. 138). `smith2006iliosacral`
  y `zwingmann2009navigated` usan una escala **ordinal de cuatro grados** con umbrales en
  milimetros (0 / <2 / 2-4 / >4 mm). Mezclar tasas de las dos familias en un mismo
  benchmark seria un error de categoria. Toca la definicion de SAP y la de BFC.
- **Hallazgo 4, util para el muestreador — la malposicion se concentra en S2.**
  *"18 of the 22 (82%) misplaced screws were at the S2 level"* (Discussion, p. 142), con
  tasas de 93% en S1 frente a 71% y 64% en S2. Aunque las cifras sean de banco, el patron
  sugiere que **el muestreador deberia condicionar la distribucion de malposicion por
  nivel vertebral (S1 vs S2), no aplicar una tasa unica**. Eso es diseno del Objetivo 2.
- **Cautela aritmetica registrada por el agente lector:** el texto habla de 22 tornillos
  mal colocados (p. 142) pero la Tabla 1 (p. 140) suma 28 colocaciones inseguras, y el PDF
  no reconcilia ambos. Por eso **no se derivo ninguna tasa global**. No la derives despues.
- **Efecto neto sobre #12:** la tesis se queda **sin ningun prior clinico de malposicion
  respaldado por una fuente leida**. Las dos cifras que estaban en juego caen:
  - 31-60%: derivacion propia (100-69, 100-40) sobre dos poblaciones separadas por tecnica.
  - 2-15%: cita de tercera mano, sin fuente primaria leida.
- **Opciones, revisadas:**
  1. **Recomendada, y ahora con mas fuerza que antes.** Abandonar el rango unico y comparar
     la distribucion generada contra **las dos distribuciones de cuatro grados** de
     `zwingmann2009navigated`, que si son medidas, clinicas, por TC postoperatoria y
     separadas por tecnica. Es lo unico que hoy resiste una pregunta del jurado.
  2. Subir en la cadena y conseguir la fuente primaria: Routt 1997, Templeman 1996,
     Ebraheim 1993 o Keating 1999. Exige PDFs nuevos. `templeman1996proximity` ya tiene
     entrada en `refs.bib` desde su raw, pero **no tiene PDF**.
  3. Sustituir la afirmacion cuantitativa por una cualitativa hasta tener fuente primaria.
- **Pendiente de:** decision de la autora. La opcion 1 no exige ninguna lectura nueva.
- **Candidatas de snowballing anadidas por el agente:** Routt 1997, Ebraheim 1993,
  Keating 1999 (Templeman ya estaba), y Noojin 2000 para #7. Todas en `_candidatos.md`
  como PENDIENTE; no se buscaron ni se descargaron.

---

## Actualizacion 2026-09-08 — lectura completa de wang2025adaptiveweighting

Ficha regenerada desde el PDF (16 paginas, pp. 2408-2423):
`docs/literatura/wang2025adaptiveweighting.md`. Sustituye por entero la version que se
habia hecho solo desde el abstract.

### 1 — CERRADA (2026-09-08)

El PDF llego y se leyo completo. La ficha ya no lleva "Profundidad: solo abstract" y la
regla 16 deja de aplicarle. El unico nivel 1 sin texto completo pasa a estar verificado.
**Lo que la lectura encontro no es tranquilizador**, pero eso es #2, #24 y #9, no #1.
`_index.md` actualizado a PDF `si`, acceso `COMPLETO`. El lector mantiene **N1**: el
riesgo no bajo, cambio de sitio.

### 2 — CONFIRMADA contra el cuerpo (2026-09-08)

El multi-ventana publicado **es de remocion**, ahora con evidencia textual y no
cualitativa: *"The image-domain-based technique aims to directly recover artifact-removed
images from the corresponding corrupted ones"* (Sec. II-A, p. 2409). No hay una sola
linea que proponga generar artefacto como objetivo.

**Matiz que obliga a corregir la redaccion:** el paper **si** sintetiza metal, pero solo
como fabrica de datos de entrenamiento, no como contribucion. Inserta hierro en cortes
clinicos limpios — *"we select Fe as the metal material, manually segment the metal masks
from clinical data"* (Sec. V-A-2, p. 2413), *"then insert them into the collected clinical
slices by carefully adjusting the size, angle, and position"* (p. 2414) — con simulacion
de haz en abanico, 120 kVp, endurecimiento de haz y volumen parcial. **Es otra instancia
del patron de #9**, y sube a cinco los trabajos que ya insertan metal sintetico.

### 24 — El respaldo de C3 es fuente SECUNDARIA, y ademas el mecanismo no es el mismo — ABIERTA

- **Origen:** `wang2025adaptiveweighting` leido completo el 2026-09-08. Es el hallazgo
  mas incomodo de la lectura y no estaba previsto en ninguna entrada.
- **Hallazgo 1 — el marco multi-ventana NO es de este paper.** Viene de su referencia
  [24], Niu & Wang, *Multiple window learning for metal artifact reduction*, SPIE 2021
  (MWLNet). El propio texto: *"Motivated by the existing work [24], we construct the
  general multiple-window MAR framework"* (Sec. III, p. 2410) y *"Following [24], we set
  the number of windows B to three"* (Sec. V-A-1, p. 2412). Lo propio de AdaW es el
  **peso de la perdida por ventana** en una optimizacion bi-nivel, no la codificacion.
  Es decir: la fuente N1 que sostiene C3 es **secundaria** para justo lo que C3 reclama.
  Mismo defecto que ya tiene `smith2006iliosacral` respecto de la escala 0-3.
- **Hallazgo 2 — el mecanismo publicado no es el que plantea C3.** AdaW combina las
  ventanas en **cascada secuencial** de ancha a estrecha, con una *window transfer layer*
  que reclipa y renormaliza, y concatenacion por canal entre etapas (Eq. 1 y Fig. 1,
  p. 2410). La tesis plantea una **codificacion multi-ventana de entrada**. Refinamiento
  progresivo y codificacion multicanal simultanea no son lo mismo. Escribir "multi-ventana
  (Wang et al., 2025)" sin esa salvedad atribuye al paper un diseno que no tiene.
- **Hallazgo 3 — lo que si es citable y es bueno.** Las tres ventanas concretas, en rango
  [L, H] y no en centro/ancho: LW [-1000HU, 2000HU], MW [-320HU, 480HU], SW
  [-160HU, 240HU] (Sec. V-A-1, p. 2412). Y la normalizacion `Ynorm = (Yclamp - L)/(H - L)`
  (Eq. 2, p. 2410). Eso alimenta directo el Objetivo 1 (round-trip MAE < 25 HU).
- **Hallazgo 4 — B_delta sigue SIN precedente.** Ninguna banda, margen ni region
  peri-implante con valor numerico: **NO ENCONTRADO EN EL PDF**. Solo menciones
  cualitativas (*"especially around the metal implants"*, Sec. V-E, p. 2421). Esto juega
  **a favor** de la tesis y refuerza #10: B_delta es lo que queda intacto como novedad.
- **Por que importa:** toca el reclamo de novedad de C3 en el Problem Statement y la
  redaccion del Objetivo 3. Si C3 se sostiene sobre una fuente secundaria y ademas
  describe otro mecanismo, el reclamo hay que reescribirlo o hay que conseguir el
  primario.
- **Seccion afectada:** Problem Statement (C3), Objetivo 1, Objetivo 3, Related Work.
- **Opciones:**
  1. Conseguir Niu & Wang, SPIE 2021, y citarlo como origen del marco multi-ventana,
     dejando a `wang2025adaptiveweighting` como la fuente de las ventanas concretas y del
     argumento de que una ventana fija no transfiere. Exige PDF nuevo; el lector ya lo
     dejo como candidato N1 en `_candidatos.md`.
  2. Reescribir C3 para que la novedad NO sea "multi-ventana" sino la combinacion
     multi-ventana **para sintesis** mas B_delta, que es lo unico sin precedente hallado.
     No exige lectura nueva y es coherente con #2 y con #9.
  3. Migrar el N1 a Niu & Wang cuando llegue, y bajar `wang2025adaptiveweighting` a N2.
     El lector dejo esa alternativa registrada en `_index.md`.
- **Pendiente de:** decision de la autora. La opcion 2 no exige ninguna lectura nueva.

### 13 — DATO CRUZADO desde wang2025adaptiveweighting (2026-09-08)

No cambia el estado de #13, pero aporta tres cosas verificadas contra un paper publicado:

1. **Las 14 series se confirman desde fuera.** *"it contains 14 metal-corrupted volumes"*
   (Sec. V-A-2, p. 2413), sobre CLINIC-metal, citando a `liu2021ctpelvic1k` como su
   referencia [54]. Coincide exactamente con la cifra de #13.
2. **El problema de la falta de referencia limpia ya lo enfrento otro grupo, y su salida
   es reutilizable.** *"we can only provide visual evaluations on these two testing sets"*
   (Sec. V-A-3, p. 2414); resuelven con 30 imagenes y puntuacion de 5 medicos en escala de
   5 niveles (Sec. V-C-3, p. 2415). Si la validacion de realismo de la tesis necesita
   lectura humana, hay precedente citable de como se hace sobre este mismo subconjunto.
3. **Umbral de segmentacion de metal, util para #19 y #22:** *"clinical metals for
   CLINIC-metal and SpineWeb are segmented with the thresholding of 2,500HU"*
   (Sec. V-A-2, p. 2413). La exploracion local uso superficies a 300/1500/2500/3500 HU.
   Que un paper publicado fije 2500 HU para mascara metalica sobre este mismo dataset es
   respaldo directo para la definicion operativa que #22 pide.

**Efecto colateral util:** CLINIC-metal aparece como set de generalizacion clinica en un
TMI de 2025. Sostiene por escrito que ese subconjunto es el estandar de facto para MAR
pelvico, lo que ayuda a justificar la eleccion de datos sin depender solo de #18.

---

## Actualizacion 2026-09-08 — lectura completa de mclaren2021corridor

Ficha: `docs/literatura/mclaren2021corridor.md`. **22 entradas NO ENCONTRADO EN EL PDF.**

### 7 — PARCIALMENTE CUBIERTA, NO CERRADA (2026-09-08)

McLaren es mejor fuente que `ramadanov2025safezone` por dos ordenes de magnitud (433
pelves con cortical mapeada frente a una sola CT en proyeccion 2D), y da lo que
Ramadanov no daba: un umbral con numero y un procedimiento reproducible. Pero **no
entrega la geometria parametrizada** que el muestreador necesita.

**Lo que SI resuelve:**
- **Umbral de zona segura con valor:** *"Dmax of >= 10 mm was defned as the target amount
  of available space"* (Material and methods, PDF p. 2). Mismo umbral para S1 y S2.
- **Procedimiento de Dmax, reimplementable:** malla 3D de densidad por voxel de los
  contornos corticales, recta de tabla externa iliaca a tabla externa contralateral
  cruzando ambas articulaciones SI, y diametro creciente *"until it contacted and breached
  the thickness of the cortex... in at least three locations"*.
- **Tolerancia angular transiliosacra:** S1 `1.53 +/- 0.57` grados y S2 `1.02 +/- 0.33`
  grados (Results, PDF p. 4).
- **Distribucion poblacional verificada:** 68.9% S1, 81.1% S2, 48.3% ambos, 5.1% ninguno.
- **Sexo si predice, edad y BMI no:** S1 52% vs 67% (p = 0.001), S2 64% vs 86% (p < 0.001).
- **Los cinco pasos del calculo estan en prosa:** `(Dmax - 7 mm)/2` como cateto corto,
  150 mm de piel a cuerpo sacro como cateto largo, arcotangente, por dos.

**Lo que NO resuelve, y por que #7 no cierra:**
1. **El umbral de 10 mm es heredado y el propio paper lo declara no establecido:**
   *"Reported between 8 and 12 mm, the minimal corridor for safely placing a
   transiliosacral screw has not yet been established"*, y lo adopta de Kaiser
   (Introduccion, PDF p. 2). No es un valor asentado: es un rango 8-12 mm con una
   recomendacion elegida.
2. **La zona segura es un ESCALAR, no una region.** Toda la geometria colapsa en un
   numero por segmento. El paper dice que la posicion y la alineacion quedan
   determinadas, pero **sus valores no se reportan**: coordenadas, angulos de entrada,
   margen al foramen o a la cortical, longitud del corredor y Dmax medio en mm son
   **NO ENCONTRADO EN EL PDF**.
3. **Es una recta unica y maximal, no una distribucion.** Busca el camino mas grande;
   no muestrea el espacio de poses viables ni las malposiciones. **Mide capacidad
   anatomica, no comportamiento clinico.** El muestreador de la tesis necesita
   exactamente lo contrario.
4. **La tolerancia angular mezcla anatomia con tecnica percutanea.** El cateto largo es
   la distancia piel-sacro *"estimated to be 150 mm"*, tomada de Templeman, y el ancho
   util resta un tornillo de 7 mm. Si el origen fuera la cortical iliaca contralateral
   en vez de la piel, la tolerancia **subiria**; los autores lo admiten (Discusion,
   PDF p. 5). No es una restriccion intrinseca del volumen CT.
5. **Sin periostio:** *"The technique does not account for periosteal thickness"*.
6. **Todo lo medido es TRANSILIOSACRO** (cruza ambas articulaciones SI). El 4 grados
   iliosacro es cita de Templeman, no medicion de McLaren. No son intercambiables.
7. **Ecuacion en notacion matematica: NO ENCONTRADO EN EL PDF.** Solo prosa.
8. **Procedencia de los datos opaca:** 433 CTs de una institucion sin nombrar;
   resolucion, escaner y protocolo **NO ENCONTRADO EN EL PDF**.

**Dos inconsistencias internas del PDF, registradas para no tropezar con ellas:**
- S2 aparece como `1.02 +/- 0.33` en Resultados y `1.03 +/- 0.33` en Discusion, en
  abstract y en cuerpo. El paper no lo explica.
- El 31.1% *"sin corredor viable"* aparece **solo en el abstract**; el cuerpo dice 31% y
  lo declara especifico de S1. El "sin ningun corredor" es 5.1%.
- En el mismo parrafo conviven 48.3% (n=209) y *"352 (81.3%) pelves had both S1 and S2
  corridors Dmax >= 10 mm"*. No se derivo nada de ahi.

**Efecto neto sobre #7:** la restriccion de zona segura pasa de "sin respaldo" a
"respaldo parcial, con umbral heredado". El muestreador **ya puede** justificar por
escrito una regla de contencion cortical y un criterio de corredor viable. Lo que sigue
sin heredarse es la parametrizacion de la pose: eso queda como construccion propia y
hay que **declararlo como tal**, que era la opcion 2 original de #7.

**Discrepancia de nivel que la autora debe resolver:** la ficha encabeza
`Nivel de lectura: 2 (metodo)` y el lector propuso **N1** en `_index.md`. Los dos
criterios son defendibles y no los concilio yo.

**Candidatas nuevas en `_candidatos.md`:** Gottschling 2009 (el algoritmo de mapeo
cortical, que McLaren no describe), Kaiser 2014 (el origen del umbral de 10 mm) y
Lee 2015, mas otras seis. `templeman1996proximity` sube de urgencia.

### 25 — Patron sistemico: tres anclas cuantitativas son citas heredadas — ABIERTA

- **Origen:** sintesis de las tres lecturas del 2026-09-08. No es un hallazgo de un
  paper: es un patron que solo se ve poniendolas juntas, y por eso se registra.
- **Hallazgo:** tres de los numeros que sostienen la tesis **no se miden en la fuente que
  la tesis cita**. En los tres casos la fuente los hereda de un tercero:
  1. **Tasa de malposicion 2%-15%** -> `hinsche2002fluoroscopy` la cita de Ebraheim 1993,
     Keating 1999, Routt 1997 y Templeman 1996 (Introduccion, p. 135).
  2. **Umbral de zona segura Dmax >= 10 mm** -> `mclaren2021corridor` lo adopta de Kaiser
     y declara que el corredor minimo *"has not yet been established"*, con rango previo
     de 8 a 12 mm (Introduccion, PDF p. 2).
  3. **Marco multi-ventana en HU** -> `wang2025adaptiveweighting` lo toma de Niu & Wang,
     SPIE 2021: *"Motivated by the existing work [24]"* (Sec. III, p. 2410).
  Se suma un cuarto, mas fino: el **cateto de 150 mm** con el que McLaren deriva su
  tolerancia angular esta *"estimated"* y tomado de Templeman.
- **Por que importa:** no son tres coincidencias. Es que **las anclas cuantitativas de la
  tesis estan sistematicamente a un salto de cita de donde se cree que estan.** Cada vez
  que la tesis escriba "X segun Fuente", hay que verificar si Fuente lo mide o lo hereda.
  Por la regla 2 de `CLAUDE.md`, citar a quien hereda es atribuir un dato que la fuente
  no produjo.
- **Consecuencia practica:** `templeman1996proximity` pasa a ser **la fuente sin PDF mas
  cara del proyecto**. Sostiene dos cosas a la vez: es uno de los cuatro origenes del
  2%-15% y es el origen del 150 mm de McLaren. Es el unico PDF cuya ausencia bloquea dos
  entradas distintas.
- **Seccion afectada:** toda cita cuantitativa. En concreto: Problem Statement (C3 y el
  rango de malposicion), Objetivo 2 (zona segura), Objetivo 4 (SAP).
- **Opciones:**
  1. **Recomendada.** Auditar las cifras que ya estan escritas en `main.tex` marcando
     cuales son medidas por su fuente y cuales heredadas, y reescribir las heredadas como
     "reportado en la literatura y recogido por Fuente" en vez de "segun Fuente". No
     exige ninguna lectura nueva.
  2. Subir un eslabon en las tres cadenas: Kaiser, Niu & Wang y Routt/Templeman. Tres
     PDFs nuevos; ninguno esta en `papers/`.
  3. Reenunciar las afirmaciones para que no dependan de heredar un numero: usar
     distribuciones medidas en vez de rangos citados, y reclamar novedad sobre la
     combinacion en vez de sobre el componente.
- **Pendiente de:** decision de la autora. La opcion 1 no exige lectura nueva y es la que
  mas riesgo quita por hora invertida.

---

## Nota provisional 2026-09-08 — CUMPLIDA Y CERRADA

Las tres lecturas terminaron el 2026-09-08 y sus hallazgos estan arriba, con evidencia
textual y pagina: Hinsche en la actualizacion de #12, Wang en el cierre de #1 y en #24,
McLaren en la actualizacion de #7 y en #25. Nada de la nota provisional sigue vigente;
ninguna de sus cifras de abstract debe usarse: usar las de las fichas.

## Actualizacion 2026-09-08 (tarde) — DECISIONES APLICADAS por orden de la autora

La autora adopto las opciones recomendadas y autorizo aplicarlas en el mismo turno.
Lo que sigue **ya esta escrito** en `tesis/main.tex`, `docs/00-tesis.md` y
`docs/03-glosario.md`. Falta que la autora lo recoja en `docs/01-decisiones.md`, que
Claude no toca (regla 3).

### 12 — APLICADA (redaccion)
El rango unico desaparece de `main.tex`. El Problem Statement, el Objetivo 2 y la fila
SAP de Expected Results citan ahora las **dos distribuciones ordinales de cuatro grados**
de `zwingmann2009navigated` (navegado 69/15/8/8; convencional 40/37/11.5/11.5), declaradas
como dos poblaciones por tecnica y no como un rango. Se anade el condicionamiento por
**nivel sacro** con el 82% en S2 de `hinsche2002fluoroscopy`, citado explicitamente como
banco sobre plastico. **Lo que sigue vivo:** conseguir una fuente primaria del 2-15%
(Routt, Ebraheim, Keating o Templeman) si alguna vez se quiere una tasa agregada.

### 7 — APLICADA (redaccion), sigue ABIERTA en lo tecnico
`main.tex` sustituye la zona segura cualitativa por la viabilidad de corredor de
`mclaren2021corridor`, con las dos tolerancias angulares, y **declara por escrito** que
el umbral de 10 mm es heredado y reportado como no establecido (8-12 mm), y que la
parametrizacion de la pose es construccion propia. `ramadanov2025safezone` se conserva
citado, pero como descripcion cualitativa, que es lo que es. **Lo que sigue vivo:** la
geometria parametrizada (coordenadas, angulos de referencia, margenes) no existe en
ninguna fuente leida. `kaiser2014dysmorphism` esta en lectura y puede cambiarlo.

### 24 — APLICADA (redaccion)
C3 reescrita. Ya no reclama el multi-ventana como novedad: dice que es de trabajo previo
de MAR y que `wang2025adaptiveweighting` lo atribuye a su vez a trabajo anterior. La
novedad reclamada es **el uso para sintesis mas B_delta**, y se afirma que no se hallo
precedente publicado que cuantifique una banda peri-implante.

### 14 y 16 — CERRADAS por la decision de retirar BFC e ISC
No hay siglas propias que rellenar con medidas heredadas, asi que el conflicto
desaparece. La apariencia se evalua con **bone integrity, metal integrity y streak
amplitude** bajo sus nombres publicados. La escala 0-4 no se traslada. **SAP queda como
unica metrica introducida por la tesis.** Registrado tambien en `03-glosario.md` con un
aviso de no reintroducir BFC ni ISC.

### 13 y 18 — DEGRADADAS de bloqueo a limitacion declarada
Al salir el Objetivo 5 del alcance, dejan de bloquear. `main.tex` incorpora un parrafo
**Why downstream evaluation is excluded** que da las dos condiciones auditables (anotacion
parcial y coleccion incompleta en disco) en vez de alegar falta de tiempo, y usa
`wang2025adaptiveweighting` para sostener que ese subconjunto es el estandar de facto.
`00-tesis.md` las recoge en `Fuera de alcance`.

### 22 — DEFINICION OPERATIVA ESCRITA, recuento pendiente
`03-glosario.md` fija el umbral de mascara metalica en **2500 HU**, con la frase literal
de `wang2025adaptiveweighting` sobre este mismo subconjunto. Queda el aviso de que un
umbral en HU no encuentra material no metalico (#19). **Lo que sigue vivo y es de la
autora:** rehacer el recuento de volumenes limpios con esa definicion. Es la diferencia
entre 70 y 97 volumenes de entrenamiento.

### 25 — APLICADA en `main.tex`, pendiente el barrido completo
Las tres anclas heredadas quedan marcadas como tales en el texto: el umbral de 10 mm, el
marco multi-ventana y el rango de malposicion. `03-glosario.md` repite el aviso en cada
termino afectado. **Lo que sigue vivo:** el barrido del resto de cifras del documento y
de las fichas, que no se ha hecho entero.

### 23 — RESUELTA en su parte de alcance
`00-tesis.md` ya tiene `Fuera de alcance` escrito con seis puntos, que era el vacio que
la entrada senalaba. El Objetivo 5 sale; el Objetivo 4 se modifica. **Lo que sigue vivo:**
la tabla de `Fechas` de `00-tesis.md` sigue vacia.

### Cambios estructurales en `tesis/main.tex` (2026-09-08)
- Research Question: se elimina el impacto downstream y se remite al alcance.
- Hypothesis: se retira la frase de segmentacion downstream; SAP pasa a ser la unica
  metrica propia; el brazo fisico se nombra como el protocolo adoptado.
- Objetivo general: la robustez downstream pasa a "in future work".
- Objetivos: el 5 desaparece de la lista y se anade el parrafo
  **Explicitly out of scope**.
- Expected Results: la fila de downstream se sustituye por **Preservation outside
  $B_{\delta}$** (RMSE y SSIM en el complemento de la banda), que era lo que
  `peters2025hybrid` ya sostenia.
- Compila limpio: 0 citas indefinidas, 31 entradas en el `.bbl`.

## Actualizacion 2026-09-08 (noche) — lectura completa de kaiser2014dysmorphism

Ficha: `docs/literatura/kaiser2014dysmorphism.md`. **41 entradas NO ENCONTRADO EN EL PDF.**
El Appendix (tabla de scores por quintil, figura de clusters) esta fuera del PDF.
**Nada de esto se ha aplicado a `main.tex`: la autora pidio discutirlo antes.**

### 25 — CONFIRMADA y PROFUNDIZADA: la cadena del 10 mm tiene tres saltos

Kaiser **tampoco** establece el umbral. Lo elige y lo hereda:
- Metodos, p. e120(2): *"A 10-mm-diameter corridor perpendicular to the axis of the safe
  zone was chosen as a conservative size for passage of an iliosacral screw"* (refs. 29 y 37).
- Discusion, p. e120(7): *"has been previously established as a reasonably 'safe'-diameter
  corridor by experienced surgeons"* (refs. 4, 29 y 37).
- Los autores lo llaman *"our conservative 10-mm threshold"*.

Cadena completa: `mclaren2021corridor` -> `kaiser2014dysmorphism` -> Gardner 2010 (ref. 29),
Ziran 2007 (ref. 37) y Moed 2006 (ref. 4). **Tres saltos y tres PDFs que no estan en
`papers/`.** Las tres quedaron en `_candidatos.md` con nivel sugerido 1.

**Hallazgo que cambia la recomendacion:** el paper **si** da su justificacion interna, y no
es empirica sino **dimensional**: *"Ten millimeters was chosen to allow 1 to 2 mm of
circumference around a 6.3 to 8-mm-diameter screw"* (Discusion, p. e120(7)). Es decir, el
10 mm **no es un umbral de seguridad clinica validado: es una regla de holgura geometrica
derivada del diametro del tornillo**. Eso se puede citar de Kaiser directamente, con su
frase, sin subir la cadena. Perseguir Gardner, Ziran y Moed compraria muy poco.

**Recomendacion (pendiente de la autora):** NO subir la cadena. Reenunciar el 10 mm como
criterio de holgura geometrica, citando a Kaiser como quien lo adopta y su razon
dimensional. Cierra la rama mas cara de #25 sin ningun PDF nuevo.

### 7 — CUBIERTA OPERACIONALMENTE (propuesta de cierre, pendiente de la autora)

Kaiser aporta lo unico que faltaba y que `mclaren2021corridor` no daba: **un marco de
referencia calculable sobre un volumen CT.**

- **Plano de reformateo:** *"Each CT scan was reformatted along the axis of the sacrum"*
  (p. e120(2)), con el eje *"perpendicular to the superior end plate of the first sacral
  segment"* (Fig. 1, pie, p. e120(3)).
- **Angulo coronal:** *"angle subtended by a line drawn perpendicular to the axis of the
  osseous corridor"* **y** *"a line connecting the top of the iliac crests"* (p. e120(2)).
- **Angulo axial:** la misma perpendicular **y** *"a line connecting the posterior iliac
  spines"* (p. e120(2)).
- **Score:** *"sacral dysmorphism score = (first sacral coronal angle) + 2(first sacral
  axial angle)"* (Resultados, p. e120(4)).
- **Margen cortical operativo, que nadie mas daba:** *"no less than 5 mm of distance to the
  cortex on either side"* (p. e120(2)). Es un numero para la contencion cortical.
- **Valores poblacionales:** coronal S1 `22.6 +/- 11.1` grados, axial S1 `11 +/- 10.5`
  grados, area minima S1 `417.4 +/- 81.1` mm2 (Tabla II, p. e120(5)).
- **Estratificacion:** tres fenotipos por longitud de corredor (>120 mm en S1; <120 mm en
  S1 y >110 mm en S2; corto en ambos), con medias y DE por cluster (Tabla III). El
  fenotipo dismorfico es el **41%** de la cohorte.

Los landmarks son **oseos y segmentables**: platillo superior de S1, crestas iliacas,
espinas iliacas posteriores. Es la primera cosa de toda la bibliografia que se puede
implementar directamente sobre un volumen.

**Propuesta:** bajar #7 de RIESGO a cubierta operacionalmente. Lo que queda como
construccion propia es la **distribucion de poses**, que es justamente la contribucion.

**Cautelas que hay que escribir si se adopta:**
1. El `>70` es **descriptivo, no umbral validado**: *"There were no safe transsacral
   corridors in any subject with a dysmorphic score >70"* (Resultados, p. e120(4)), sobre
   104 pelves. Presentarlo como corte validado seria repetir el error de #12.
2. Los propios autores declaran que falta validacion: *"Future clinical research is
   recommended to validate and test the ability to use reformatted CT"* (p. e120(7)).
3. Cuatro discrepancias internas del PDF documentadas por el lector (tres rangos de
   acuerdo entre revisores, dos de kappa, una fila de longitud que contradice al texto, y
   las refs. 17 y 22 duplicadas).

### 26 — Los landmarks de Kaiser se midieron en pelvis SIN implante — ABIERTA

- **Origen:** `kaiser2014dysmorphism` leido el 2026-09-08. Riesgo tecnico nuevo, no
  bibliografico.
- **Hallazgo:** la cohorte es de **pelvis no lesionadas** (*"a consecutive series of 104
  uninjured pelves"*, p. e120(2)) y el criterio de exclusion es explicito: se excluyen los
  CT con *"any pelvic ring injury, radiographic contrast medium or implants obscuring the
  lumbosacral junction"* (Materials and Methods, p. e120(2)). **Excluye justamente los
  volumenes con implante, que son el caso de uso de esta tesis.**
- **Por que importa:** el muestreador tiene que calcular el marco de referencia sobre
  volumenes de CLINIC-metal, donde hay metal y artefacto. Los tres landmarks (platillo
  superior de S1, crestas iliacas, espinas iliacas posteriores) pueden quedar oscurecidos
  por streaking justo en la union lumbosacra. Si no sobreviven, el marco de referencia no
  se puede calcular donde mas se necesita.
- **Seccion afectada:** Objetivo 2, implementacion del muestreador. No toca la redaccion
  del Problem Statement.
- **Opciones:**
  1. **Recomendada, y es barata.** Verificarlo localmente: medir en cuantos de los
     volumenes con metal se pueden ubicar los tres landmarks. Es un experimento sobre datos
     que ya estan en disco, no una lectura. Da una cifra propia y citable.
  2. Calcular el marco de referencia solo sobre los volumenes limpios (que son la fuente de
     anatomia del muestreador de todos modos) y declarar la limitacion para los de test.
  3. Definir un marco de referencia alternativo con landmarks mas lejanos al metal.
- **Pendiente de:** decision de la autora. La opcion 1 no exige lectura y responde con un
  numero medido en casa.

## Actualizacion 2026-09-08 (noche, 2) — Kaiser APLICADO y respuesta sobre el 2500 HU

### 22 — El 2500 HU SI es arbitrario. Peters NO lo respalda, y respalda lo contrario

La autora pregunto si hay alguna fuente que sostenga el umbral. Respuesta corta: **una
sola, y para otra cosa.** Lo verificado:

| Fuente | Umbral | Para que | Sirve para #22? |
|---|---|---|---|
| `wang2025adaptiveweighting` | **2500 HU fijo** | segmentar mascara metalica en CLINIC-metal y SpineWeb | Si, pero como **cribado**, no como definicion |
| `peters2025hybrid` (metal integrity) | **adaptativo por ROI**: mayor HU del ROI + 250 | medir integridad del metal | **No.** Y contradice el enfoque de umbral fijo |
| `peters2025hybrid` (bone integrity) | 150 HU | separar hueso | No, es para hueso |

**Peters no respalda el 2500 HU: hace lo contrario.** Su umbral es **relativo al ROI**,
precisamente porque un umbral absoluto no transfiere entre adquisiciones. Citar a Peters
como respaldo de un 2500 fijo seria un error, y ademas del mismo tipo que #25.

**Lo unico que respalda el 2500 es Wang**, y ahi es una conveniencia de segmentacion para
fabricar mascaras, no una definicion fisica de metal. Su valor esta en que es **sobre el
mismo subconjunto** (CLINIC-metal), asi que es un precedente citable y no una invencion.

**Opinion, para decision de la autora: separar los dos trabajos, que hoy estan mezclados.**

1. **Cribado y definicion de cohorte (#22).** Umbral **fijo de 2500 HU**, citando a Wang
   sobre este mismo dataset, y **declarado como convencion de cribado**, no como
   definicion fisica. Es defendible: reproducible, con precedente publicado, y la
   pregunta que responde ("este volumen entra a entrenamiento limpio o no") tolera un
   criterio conservador.
2. **Medicion de metal integrity.** Umbral **adaptativo por ROI** de Peters, que es el que
   la metrica exige. Es la metrica adoptada; usar su propia regla es lo coherente.

Asi el 2500 deja de ser "la definicion de metal" y pasa a ser "el filtro con el que se
armo la cohorte", que es todo lo que #22 necesitaba.

**Dos limites que hay que escribir igualmente:**
- Un umbral en HU **no encuentra material no metalico**. Si `objeto extrano` llega a
  incluirlo, el instrumento es otro (#19). La revision 3D local ya encontro un objeto por
  debajo de 1500 HU que resulto no ser metal.
- La exploracion local uso superficies a 300/1500/2500/3500 HU. El 2500 coincide con una
  de ellas, lo que facilita rehacer el recuento sin recalcular nada.

**Pendiente de la autora:** aceptar la separacion en dos umbrales y rehacer el recuento de
volumenes limpios. Es la diferencia entre 70 y 97 volumenes de entrenamiento.
**No se ha tocado `03-glosario.md`**, que sigue con la redaccion de umbral unico.

### 7 — APLICADA a `main.tex`, baja a cubierta operacionalmente

El marco de referencia de Kaiser esta escrito en el Problem Statement y en el Objetivo 2:
reformateo por el eje sacro perpendicular al platillo superior de S1, angulo coronal contra
la linea de crestas iliacas, angulo axial contra la linea de espinas iliacas posteriores, y
holgura cortical de 5 mm. Los fenotipos entran como estratificador descriptivo (41%
dismorfico). El `>70` **no** se usa como corte.

### 25 — APLICADA en su parte del 10 mm

`main.tex` dice ahora que el criterio de 10 mm **no es un umbral de seguridad validado** y
lo cita con la razon dimensional de Kaiser (holgura de 1-2 mm alrededor de un tornillo de
6.3-8 mm). **Sigue vivo:** la autora subio `moed2006s2screw`, `gardner2010safezones` y
`ziran2007fluoroscopic` en una primera ronda; estan en lectura. Si ninguno mide el umbral,
la cadena se declara agotada y la redaccion actual queda firme.

### 26 — ESCRITA COMO RIESGO DECLARADO en `main.tex`

Por decision de la autora, el riesgo no se esconde: la seccion Datasets lleva un parrafo
**Declared risk: landmark visibility under metal artifact** que dice que la cohorte de
Kaiser excluyo los CT con implantes en la union lumbosacra, que la visibilidad de los
landmarks bajo artefacto no esta establecida por la fuente, y que se cuantificara en la
cohorte local antes de comprometerse, con contingencia explicita.
**Sigue ABIERTA hasta que exista la cifra medida en casa.**

### 27 — Riesgo historico sobre Kaiser — CERRADA: sin fenotipos ni score

- **Origen:** decision de la autora del 2026-09-08. Se adopta lo operacional de Kaiser y se
  deja explicitamente sin decidir el resto.
- **Lo adoptado:** marco de referencia, definiciones angulares, margen de 5 mm, fenotipos
  como estratificador descriptivo.
- **Lo que queda pendiente:** usar el score de dismorfismo como **predictor**, adoptar el
  corte `>70`, o convertir los cortes de longitud de los tres fenotipos en **reglas duras**
  del muestreador.
- **Por que no se cierra:** el `>70` es descriptivo en su fuente, no un umbral propuesto;
  los autores declaran que falta validacion externa (*"Future clinical research is
  recommended to validate and test the ability to use reformatted CT"*); el Appendix con la
  tabla de scores por quintil y la figura de clusters **esta fuera del PDF**; y la ficha
  documenta cuatro discrepancias internas.
- **Que decide la continuacion:** (a) el resultado de #26, porque si el marco no sobrevive
  al metal comprometerse mas con Kaiser no tiene sentido; y (b) lo que aporten
  `moed2006s2screw`, `gardner2010safezones` y `ziran2007fluoroscopic`.
- **Pendiente de:** decision de la autora, despues de esas dos cosas.

## Actualizacion 2026-09-08 (noche, 3) — lectura de ziran2007fluoroscopic

Ficha: `docs/literatura/ziran2007fluoroscopic.md`. **24 entradas NO ENCONTRADO EN EL PDF.**
Es el primero de los tres eslabones de la cadena del 10 mm que la autora subio.

### 25 — PRIMER ESLABON DESCARTADO: la ref. 37 de Kaiser NO contiene el umbral

**El umbral de 10 mm NO ESTA en `ziran2007fluoroscopic`.** El lector reviso texto completo,
abstract, Tabla 1, pies de las figuras 1-10, Apendice y conclusiones. **El paper no mide
ninguna distancia**: todas sus mediciones son angulares, en grados, con goniometro de
1 grado. Los unicos milimetros del texto son el **diametro del tornillo**, no del corredor.

Kaiser cita a esta fuente como una de las tres que habrian "establecido" el 10 mm. **No lo
hace.** Queda documentado que la cadena no termina aqui, y que al menos una de las tres
atribuciones de Kaiser no se sostiene.

**Efecto sobre la decision ya tomada:** ninguno en contra. Refuerza la decision del
2026-09-08 de usar el 10 mm como **convencion de holgura geometrica** con la razon
dimensional de Kaiser, en vez de perseguir un origen empirico que, por ahora, no aparece.
Quedan `gardner2010safezones` y `moed2006s2screw`, en lectura.

### C2 — APORTE INESPERADO: evidencia de que el corredor NO es fijo

Es lo mas util del paper para esta tesis, y no estaba previsto. Los coeficientes de
variacion de la orientacion de las superficies oseas van de **7%-25%** en general hasta
**43%**, **47%-52%** y, en el peor caso, *"the orientation of the superior S1 ala in the
sacral frontal plane (97% to 140%)"* (Resultados, p. 352).

**Por que importa:** la contribucion C2 afirma que no existe una pose canonica y que hay
que muestrear una distribucion. Hasta hoy ese argumento se apoyaba en las tasas de
malposicion. Ahora tiene un respaldo **anatomico y directo**: la geometria del corredor
varia tanto entre individuos que una trayectoria fija no puede ser correcta para todos.
Rol compartido con `arand2019pelvicring`. Material de Problem Statement y Related Work.

### 26 — REFORZADA: toda esta literatura mide pelvis intactas

Tercer paper consecutivo con el mismo sesgo de poblacion. `kaiser2014dysmorphism` excluye
CT con implantes en la union lumbosacra; `mclaren2021corridor` usa CTs "naive";
`ziran2007fluoroscopic` es cadaverico y avisa: *"the presence of fracture and displacement
would significantly affect fluoroscopic visualization"*, ademas de *"presence of
soft-tissue injury and variations of body habitus would affect the ability to visualize"*
(Discusion, p. 354).

**No es coincidencia: es el estado del campo.** Toda la geometria de corredor disponible se
midio en pelvis intactas, sin fractura y sin implante. La tesis la necesita en pelvis con
metal y, en el caso clinico, fracturadas. Esto **sube el peso del riesgo R1**: no es solo
que los landmarks puedan no verse, es que ninguna fuente ha caracterizado el corredor en la
poblacion de interes. Conviene escribirlo como limitacion del campo, no como debilidad
propia.

### Nivel propuesto
El lector propone **N2, acceso COMPLETO**, y **descarta explicitamente N4**: cubre dos roles
vigentes (eslabon auditado de la cadena, y evidencia de variabilidad angular). No entra al
muestreador como restriccion ejecutable, porque no da longitudes ni trabaja en volumen:
todo vive en el marco de referencia del haz de fluoroscopia, que un CT no tiene.

## Actualizacion 2026-09-08 (noche, 4) — lectura de moed2006s2screw

Ficha: `docs/literatura/moed2006s2screw.md`. **31 entradas NO ENCONTRADO EN EL PDF.**
Segundo eslabon de la cadena del 10 mm.

### 25 — EL HALLAZGO MAS GRAVE DE LA CADENA: el 10 mm CAMBIA DE MAGNITUD

En `moed2006s2screw` **si aparece un 1 cm, y es nodo terminal**: no lleva llamada de
referencia, o sea que no lo hereda de nadie. Pero **no mide lo que Kaiser dice que mide**.

| Fuente | Que dice el numero | Que magnitud es |
|---|---|---|
| `moed2006s2screw` | *"a minimum of 1 cm between the S1 and S2 neural foramina on 3 sequential preoperative CT 3-mm sections"* (Metodos, p. 379) | **separacion interforaminal** medida en cortes axiales 2D, usada como **criterio de inclusion** de pacientes |
| `kaiser2014dysmorphism` | *"A 10-mm-diameter corridor perpendicular to the axis of the safe zone"* | **diametro de corredor** en 3D |

**No son la misma cantidad.** Una es la distancia entre dos forámenes en cortes axiales; la
otra es el diámetro de un cilindro perpendicular al eje del corredor. Kaiser atribuye a
Moed un umbral que Moed no formula.

**Esto es peor que una cita heredada: es una cita heredada y transformada.** El numero
sobrevive el salto pero cambia de significado. Es el caso mas fuerte de la implicancia #25
encontrado hasta ahora, y es exactamente lo que la regla 2 de `CLAUDE.md` existe para
evitar.

**Estado de la cadena tras dos de tres lecturas:**
- `ziran2007fluoroscopic` (ref. 37 de Kaiser): **no contiene el umbral**. No mide ninguna
  distancia.
- `moed2006s2screw` (ref. 4 de Kaiser): contiene un 1 cm terminal, pero **de otra magnitud**.
- `gardner2010safezones` (ref. 29 de Kaiser): **en lectura. Unica candidata viva** a
  contener un umbral que sea de verdad un diametro de corredor.

**Efecto sobre la decision ya tomada:** la refuerza y le da un argumento que antes no
tenia. El 10 mm se usa como **convencion de holgura geometrica** con la justificacion
dimensional de Kaiser (1-2 mm alrededor de un tornillo de 6.3-8 mm) porque esa
justificacion es **autocontenida**: no depende de una cadena que, auditada, pierde el
origen y ademas cambia de magnitud. La tesis puede afirmar esto por escrito y con
evidencia, que es mas de lo que la mayoria de trabajos del area puede.

### 12 — NO SE CIERRA. Moed no aporta prior clinico

Se leyo con la esperanza de que 49 casos dieran una tasa medida. **No la dan:**
- **0 de 53 tornillos** mal colocados. El paper **nunca escribe un porcentaje**.
- Criterio **binario** (*"satisfactory screw position"*, p. 380), **sin definicion
  operacional**, sin observador cegado.
- Cohorte **auto-seleccionada por el propio umbral de 1 cm**: solo entraron pacientes con
  separacion interforaminal suficiente, o sea los anatomicamente faciles.
- El unico compromiso foraminal fue por **perdida de reduccion postoperatoria**, no por
  error de insercion.

Como prior de malposicion es inservible, y ademas su criterio binario pertenece a la otra
familia, no a la escala ordinal de `smith2006iliosacral`. **#12 sigue abierta.**

### 12 — TRAMPA DE CRITERIO REGISTRADA, para no tropezar despues

La unica escala en milimetros de `moed2006s2screw` (4 / 5-10 / 11-20 / >20 mm) es de
**calidad de reduccion de la fractura**, tomada de Matta y Tornetta 1996. **No es posicion
del tornillo.** Se parece peligrosamente a la escala 0/<2/2-4/>4 mm de
`smith2006iliosacral` y mide algo distinto. **No mezclar.** Matta 1996 queda como candidato
para deslindarla si hace falta.

### 12 — LA PISTA QUE SI VALE: van den Bosch, S1 vs S2 en pacientes

`moed2006s2screw` cita a van den Bosch con **6/31 frente a 1/49 por nivel vertebral**.
**Es la unica cifra comparativa S1 vs S2 medida en pacientes que ha aparecido en todo el
proyecto**, y llega justo despues de que la tesis decidiera condicionar el muestreador por
nivel sacro.

**Aviso de procedencia:** esa cifra es **de segunda mano**, leida dentro de Moed. Por la
regla 2 no puede ir a la tesis sin el PDF de van den Bosch. Subido a nivel 1 en
`_candidatos.md`.

**Por que importa ahora:** el eje S1/S2 que se acaba de escribir en `main.tex` se apoya hoy
**solo en `hinsche2002fluoroscopy`, que es banco sobre plastico**. Si van den Bosch se
consigue, ese eje pasa a tener respaldo clinico. Es la fuente pendiente mas rentable del
proyecto ahora mismo, por delante de `templeman1996proximity`.

### Nivel propuesto
El lector propone **N1**, con N2 como alternativa defendible: es el primer eslabon de la
cadena que no reenvia a nadie y el que demuestra que el numero heredado mide otra magnitud.
Citarlo mal deja mal definida la restriccion del Objetivo 2. Decision de la autora.

## Actualizacion 2026-09-08 (noche, 5) — lectura de gardner2010safezones. CADENA CERRADA

Ficha: `docs/literatura/gardner2010safezones.md`. **25 entradas NO ENCONTRADO EN EL PDF.**
Tercer y ultimo eslabon de la ronda que subio la autora.

### 25 — CUATRO ESLABONES AUDITADOS. NINGUNO MIDE EL UMBRAL

**El 10 mm SI aparece en Gardner, pero se DECLARA, no se mide.** Materials and Methods,
"Computed Tomography Measurements", p. 624:

> *"A safe zone dimension of 10 mm was considered the critical threshold"* ... *"below
> which placement of a large (6.5-mm to 8.0-mm) cannulated iliosacral screw would be
> considered difficult by most orthopaedic surgeons."*

Con llamada a las refs. **17 y 20 de Gardner**, que son **Ziran 2003 (JBJS Br 85:411-418)**
y **Moed 2006**.

**Cadena completa auditada:**

| Salto | Fuente | Que hace con el 10 mm |
|---|---|---|
| 1 | `mclaren2021corridor` | Lo atribuye a Kaiser |
| 2 | `kaiser2014dysmorphism` | *"was chosen as a conservative size"*. Lo atribuye a Moed, Gardner y Ziran 2007 |
| 3a | `ziran2007fluoroscopic` | **No lo contiene.** No mide ninguna distancia |
| 3b | `moed2006s2screw` | Contiene "1 cm" terminal, pero es **separacion interforaminal**, otra magnitud |
| 3c | `gardner2010safezones` | Lo **declara** como criterio. Lo atribuye a Ziran **2003** y Moed 2006 |

**CONCLUSION, y es la respuesta definitiva a la pregunta de la autora: el 10 mm nunca fue
una medicion. Es una convencion profesional derivada del diametro del tornillo, y las dos
fuentes que la enuncian lo dicen en su propio texto.** Kaiser la justifica como holgura de
1-2 mm alrededor de un tornillo de 6.3-8 mm; Gardner la justifica como el punto *"below
which placement of a large (6.5-mm to 8.0-mm) cannulated iliosacral screw would be
considered difficult by most orthopaedic surgeons"* --- es decir, **consenso de expertos
sobre un calibre de tornillo, explicitamente**.

Que la cadena no tenga origen empirico **no es un fallo de la busqueda: es el hallazgo
correcto.** No hay origen porque no es una medicion.

**Efecto sobre la decision del 2026-09-08:** queda **plenamente vindicada y ahora es
demostrable**. La tesis puede escribir, con cuatro fuentes auditadas y frases literales,
que usa el 10 mm como convencion de holgura geometrica porque eso es exactamente lo que
es. Muy pocos trabajos del area pueden sostener esa afirmacion con evidencia.

**Recomendacion sobre seguir subiendo:** **parar.** Queda un eslabon sin auditar
(**Ziran 2003**, eslabon NUEVO, no registrado hasta hoy), pero auditarlo **para el umbral**
ya no cambia la redaccion: cuatro fuentes coinciden en que es una convencion por calibre.
Ver mas abajo el motivo, distinto, por el que si podria valer la pena conseguirlo.

**Aviso critico de desambiguacion:** el Ziran del umbral es el de **2003, JBJS Br**, y
**NO** `ziran2007fluoroscopic`, que ya se leyo. Son dos trabajos del mismo primer autor.
El de 2007 es la ref. 21 de Gardner y **nunca** se usa para el umbral. Registrado en
`_candidatos.md` con la advertencia, y con una **discrepancia de ano sin resolver**: Moed
lo imprime como `2002` y Gardner como `2003`, con el mismo volumen y las mismas paginas.

### 12 — Ziran 2003 es ahora la segunda pista, por un motivo distinto del umbral

Independientemente del umbral, `moed2006s2screw` cita a esa misma fuente asi: *"Ziran et al
inserted 31 screws into S2 without an adverse event using a CT-guided technique"*
(Discusion, p. 382). Es **serie clinica, con n por nivel sacro, y guiada por CT** --- el
escenario mas cercano al que la tesis simula. Con #12 todavia sin ningun prior clinico,
ese es el motivo por el que podria valer la pena, no el umbral.

**Prioridad de fuentes pendientes, actualizada:**
1. **van den Bosch** (via `moed2006s2screw`): unica cifra comparativa S1 vs S2 **medida en
   pacientes** vista en todo el proyecto. Respaldaria el eje S1/S2 que hoy se apoya solo en
   banco de plastico.
2. **Ziran 2003**: serie clinica guiada por CT; posible tasa por nivel.
3. `templeman1996proximity`: baja de prioridad; su rol en el 2-15% ya no es decisivo.

### Objetivo 2 y #27 — Gardner: geometria S1/S2 por morfologia (interpretacion corregida)

Publica geometria **separada por segmento y morfologia**. Las areas medias iliosacras
son S1/S2 = **346/109.3 mm2** en normales y **222/220.1 mm2** en dismorficos
(Results, p. 624 y Tabla 1, p. 627; evidencia en la ficha). Las dos ultimas son
aproximadamente iguales: no se invierte el orden de las medias ni se demuestra
equivalencia estadistica. La mayor viabilidad transversa de S2 en dismorficos es
otro resultado, con otra geometria; no debe confundirse con area ni riesgo clinico.

**Por que importa:** no justifica afirmar que S2 siempre sea mas estrecho o dificil.
Tampoco obliga a introducir `nivel x fenotipo`: esa fue una propuesta de interpretacion,
no una exigencia del paper, y #27 la descarto. La decision vigente mide la geometria
de cada corredor sobre cada volumen, manteniendo S1/S2 sin fenotipos ni score.
Las trayectorias centrales ideales de Gardner no son poses quirurgicas observadas
ni distribuciones ordinales de malposicion; no completan el benchmark SAP en S2.

**Riesgos de citarlo mal, registrados por el lector:**
- Atribuirle el umbral de 10 mm.
- Confundir sus cifras **iliosacras** (area, longitud, angulos) con las **transsacras**
  (anchos y *"transverse screw possible"*). No son intercambiables.
- Citar el abstract: imprime *"15% versus 4%"* donde el cuerpo dice **grados**, y mezcla
  inlet con outlet en S2.
- Ignorar que clasifica dismorfismo **por radiografia simple y sin score**, a diferencia de
  Kaiser, y que mide el lado **no lesionado**.

### 27 — OBJECION PUBLICADA a la estratificacion por fenotipo

Gardner recoge que Carlson 2000 *"found no difference in the safe zone size between normal
and dysmorphic sacra"* (Discusion, p. 628). **Es la objecion publicada mas directa a
estratificar por fenotipo**, que es justo lo que la tesis adopto de Kaiser.

**No rompe la decision, porque el fenotipo se adopto como estratificador DESCRIPTIVO y no
como regla dura** --- que fue la razon de dejar #27 pendiente. Pero **hay que citarla**: si
la tesis estratifica por fenotipo sin mencionar que existe evidencia en contra, un jurado
que conozca Carlson lo nota. Aviso de paginacion: Ziran imprime `14:4` y Gardner
`14:264-269` para esa misma fuente.

Se anade un tercer aviso: `Noojin 2000` da dimensiones que Gardner describe como
*"larger than in the present study"*. **Dos fuentes de CT discrepan sobre el mismo corredor
segun el plano de medida.** Refuerza que las cifras absolutas de corredor no son
transferibles entre protocolos, y por tanto que el muestreador debe medir sobre su propio
volumen en vez de importar valores.

### 12 — Gardner NO usa el 2%-15%: hay una cadena paralela

Hereda otras dos cifras distintas: *"screw misplacements as high as 24%"* y *"neurologic
complication rates as high as 18%"*. **No confundirlas con el 2-15%**: es otra cadena de
citas, con otras fuentes. Registrado para que no se mezclen al redactar.

### Nivel propuesto
El lector propone **N1, acceso COMPLETO**: es a la vez el tercer eslabon auditado de la
cadena y la unica fuente leida que publica geometria S1/S2 por fenotipo, asi que un error
de cita golpea la restriccion del Objetivo 2 por dos rutas independientes. Alternativa
defendible N2 si el 10 mm no se adopta como restriccion dura; en ese caso el N1 migraria a
Ziran 2003 y Moed 2006.

### Nota de proceso
El agente de Gardner **no pudo escribir** en `_index.md` ni en `_candidatos.md`: cuatro
intentos, todos rechazados por conflicto con los otros dos agentes que escribian a la vez,
y `_candidatos.md` ya supera el limite de una lectura. **El merge lo hizo la sesion
principal**, y al hacerlo detecto que el agente de Moed ya habia registrado Ziran 2003 por
su cuenta: las dos filas se consolidaron en una, con la discrepancia de ano anotada.
Lanzar tres lectores en paralelo sobre los mismos ficheros indice fue un error de
planificacion; con mas de dos, conviene serializar o darles ficheros distintos.

## Actualizacion 2026-09-08 (cierre) — decisiones de la autora aplicadas

Todo lo de abajo esta **ya escrito** en `tesis/main.tex`, `docs/00-tesis.md`,
`docs/01-decisiones.md` y `docs/literatura/_index.md`.

### 27 — CERRADA: no se estratifica por fenotipo

**Decision de la autora del 2026-09-08.** La estratificacion por fenotipo sacro sale del
Objetivo 2. `main.tex` dice ahora que los fenotipos **no** se usan como variable
estratificadora, porque su efecto sobre el tamano de la zona segura **no es consistente
entre estudios**, y que el muestreador mide la geometria del corredor **directamente sobre
cada volumen**.

**Efecto util no previsto: la objecion de Carlson 2000 deja de aplicar.** Gardner recoge
que ese trabajo *"found no difference in the safe zone size between normal and dysmorphic
sacra"* (Discusion, p. 628). Era la objecion publicada mas directa a estratificar por
fenotipo. Al no estratificar, la tesis **no queda expuesta a ella**, y ademas la
inconsistencia entre estudios pasa a ser el **argumento** de la decision en vez de una
amenaza. Tambien desaparece el problema de que Kaiser clasifique dismorfismo por score y
Gardner por radiografia simple: dos criterios distintos que habria habido que conciliar.

**Lo que queda de #27:** nada del fenotipo. El score de dismorfismo y el corte `>70` no se
usan. #27 se cierra por completo.

### 26 — REESCRITA COMO LIMITACION DEL CAMPO

Por decision de la autora, el parrafo de `main.tex` deja de ser "riesgo que asumo" y pasa a
ser **limitacion del campo**, que es lo que los datos sostienen:

> *"This is not a limitation of the present cohort but of the available literature. Every
> source that publishes sacral corridor geometry measured it in pelves without implants and
> without fracture."*

Con las tres fuentes nombradas y su exclusion respectiva: `kaiser2014dysmorphism` excluye
CT con implantes en la union lumbosacra, `mclaren2021corridor` usa CTs no lesionados, y
`ziran2007fluoroscopic` es cadaverico y avisa que fractura, desplazamiento y lesion de
partes blandas alterarian lo visible.

**Sigue ABIERTA en lo tecnico:** falta la cifra medida en casa (en cuantos volumenes locales
con metal se ubican los tres landmarks). Lo que cambia es que ahora se reportara **como
hallazgo**, no como confesion: nadie ha caracterizado el corredor en la poblacion de
interes, asi que medirlo es aportacion, no remiendo.

### C2 — APLICADO: la premisa del muestreador ahora tiene respaldo anatomico

`main.tex` incorpora en el Problem Statement los coeficientes de variacion de
`ziran2007fluoroscopic` (7-25% en la mayoria de superficies; 43%; 47-52%; y 97-140% para la
orientacion del ala superior de S1 en el plano frontal sacro, sobre 17 pelvis cadavericas).

**Por que importa:** hasta hoy la premisa "no existe pose canonica" se apoyaba **solo en
que los cirujanos fallan**. Ahora se apoya tambien en que **la anatomia varia tanto que una
trayectoria fija no puede servir a todos**. Es un argumento independiente del error humano
y mas dificil de discutir.

### 22 — ADOPTADA la tabla de sensibilidad

La autora adopta el cribado con **varios umbrales fijos** en vez de comprometerse con uno
solo. Se recontara la cohorte a **1500, 2500 y 3500 HU** --- valores que ya existen como
superficies en la exploracion local, asi que no hay que recalcular nada --- y se reportara
cuantos volumenes cambian de clase.

- Si el recuento es **estable** en ese rango, la arbitrariedad del 2500 queda neutralizada
  con una cifra propia.
- Si es **inestable**, eso es un hallazgo, y ademas senala exactamente que volumenes
  necesitan revision visual.

**Pendiente:** correr el recuento. Es trabajo sobre datos ya en disco.
**No decidido todavia:** si se adopta ademas el reparto en dos reglas (2500 fijo para
cribado, adaptativo por ROI de `peters2025hybrid` para medir metal integrity sobre
geometria CAD propia). `03-glosario.md` sigue con la redaccion de umbral unico.

### 28 — Encargo historico de van den Bosch — RESUELTA: lectura e integracion completadas

> El bloque siguiente conserva el encargo previo a la llegada del PDF. Sus menciones
> a falta de PDF y lectura no ejecutada quedaron superadas por el cierre posterior.

- **Origen:** `moed2006s2screw` lo cita como fuente de la unica comparativa S1 vs S2 medida
  en pacientes que ha aparecido en el proyecto. Decision de la autora del 2026-09-08:
  preparar la lectura sin ejecutarla.
- **Estado:** **PDF NO DISPONIBLE.** No esta en `papers/` ni en `refs/raw/`. Por la regla 9,
  darlo de alta empieza por pegar el archivo del editor en `refs/raw/`.
- **La cifra que se persigue, y su procedencia:** Moed reporta **6/31 frente a 1/49 por
  nivel vertebral**. Es **cita de segunda mano leida dentro de Moed**; por la regla 2 no
  puede entrar a la tesis sin el PDF original.
- **Que decide esta lectura, en concreto:**
  1. **El eje S1/S2 del muestreador.** Hoy `main.tex` lo justifica **solo** con
     `hinsche2002fluoroscopy`, que es banco sobre plastico (82% de los tornillos mal
     colocados en S2). Si van den Bosch confirma una diferencia por nivel **en pacientes**,
     ese eje pasa de respaldo de banco a respaldo clinico. Es la mejora mas grande
     disponible por una sola lectura.
  2. **La implicancia #12.** Sigue sin ningun prior clinico de malposicion respaldado por
     fuente leida. Si van den Bosch publica una tasa medida con criterio explicito, #12
     podria cerrarse por fin.
  3. **El nivel de `moed2006s2screw`**, hoy N2 provisional por decision de la autora.
- **Que se espera encontrar, y que seria decepcionante:** lo esperado es una serie clinica
  con conteos por nivel sacro. Lo decepcionante, y hay precedente en esta misma ronda,
  seria (a) que la cifra sea un conteo sin porcentaje ni criterio operacional, como en
  `moed2006s2screw`; (b) que use criterio **binario** en vez de la escala ordinal de cuatro
  grados de `smith2006iliosacral`, en cuyo caso **no se puede mezclar** con el benchmark de
  SAP; o (c) que la cohorte este auto-seleccionada por un criterio anatomico de inclusion,
  otra vez como Moed.
- **Seccion afectada:** Problem Statement (justificacion del eje S1/S2), Objetivo 2,
  benchmark de SAP.
- **Pendiente de:** que la autora consiga el PDF. **No se ha lanzado ninguna lectura.**

#### Encargo listo para el subagente `lector-papers` (no ejecutado)

> Cuando el PDF este en `papers/`, este es el encargo. No hay que redactarlo de nuevo.

```
Lee `papers/<clave>.pdf` y escribe su ficha en `docs/literatura/<clave>.md` siguiendo
`docs/literatura/_plantilla.md` sin excepciones. `Leido a fondo por la autora: no`.
Usa los metadatos de `refs/raw/<clave>.nbib`; no los re-derives.

CONTEXTO: esta tesis tiene ABIERTA la implicancia #12: no tiene NINGUN prior clinico de
malposicion de tornillo iliosacro respaldado por una fuente leida. Cayeron el 31-60%
(derivacion propia sobre dos poblaciones distintas de `zwingmann2009navigated`) y el
2-15% (cita de tercera mano; `hinsche2002fluoroscopy` no lo mide y es banco sobre
plastico). Ademas la tesis acaba de decidir condicionar su muestreador por NIVEL SACRO
(S1 vs S2), y hoy ese eje se apoya solo en un estudio sobre modelos de plastico.
`moed2006s2screw` cita a este trabajo como fuente de una comparativa por nivel.

EXTRAE CON PRIORIDAD, cada cifra con su frase literal (menos de 15 palabras) y su
seccion o pagina:
1. LA PREGUNTA CENTRAL: hay una TASA DE MALPOSICION medida, expresada como porcentaje?
   Frase exacta. Si el paper NO escribe un porcentaje, dilo destacado y reporta los
   conteos crudos SIN derivar la tasa tu.
2. CONTEOS POR NIVEL SACRO (S1 vs S2): cuantos tornillos por nivel y cuantos mal
   colocados en cada uno. Moed cita "6/31 frente a 1/49": verifica esos dos pares
   contra el cuerpo y di si coinciden.
3. CRITERIO de colocacion incorrecta: binario o escala graduada con umbrales en mm?
   Quien evalua, con que modalidad, cegado o no. CRITICO: si es binario NO se puede
   mezclar con la escala ordinal 0/<2/2-4/>4 mm de `smith2006iliosacral`.
4. POBLACION: cuantos pacientes, cuantos tornillos, tipo de lesion, si hay criterio de
   inclusion anatomico que auto-seleccione la cohorte (como el "1 cm" de Moed).
5. TECNICA de colocacion: fluoroscopia, navegacion, guiada por CT. Importa para
   condicionar por tecnica, como se hace con `zwingmann2009navigated`.
6. Complicaciones neurologicas o vasculares con cifras.
7. Cualquier geometria del corredor en mm o grados.
8. Limitaciones declaradas.

REGLAS DURAS: no inventes ninguna cifra, DOI, pagina ni dato. Si algo no esta, escribe
literalmente NO ENCONTRADO EN EL PDF. No estimes ni infieras. Si haces cualquier
aritmetica, marcala como derivacion propia y nunca como cita.

Al final, agrega la fila en `docs/literatura/_index.md`, marca el paper como LEIDO en
`_candidatos.md`, y propon nivel con justificacion en una linea. Di explicitamente si la
implicancia #12 se puede cerrar con lo leido o no, y si el eje S1/S2 queda respaldado
clinicamente.
```

### Nota de proceso adoptada
No lanzar mas de dos `lector-papers` en paralelo mientras compartan `_index.md` y
`_candidatos.md`. En la ronda de tres, el agente de Gardner perdio cuatro intentos de
escritura y el merge lo tuvo que hacer la sesion principal, que ademas encontro una fila
duplicada de Ziran 2003 creada por otro agente.


## 2026-09-08 ? Resolucion tras leer van den Bosch con `lector-papers`

Encargo de la autora: analizar el PDF nuevo y resolver sus implicancias. Fuente:
`docs/literatura/vandenbosch2002.md`, texto completo, pp. 44-48; metadatos del raw.
Esta actualizacion prevalece sobre los pendientes historicos de #12 y #28.

### 28 - RESUELTA: respaldo clinico del eje S1/S2, con otro desenlace

**Hallazgo:** los pares citados por Moed se confirman, pero son **pacientes con quejas
neurologicas**, agrupados por configuracion, no tornillos malposicionados por nivel:
6 de 31 con tornillo inferior en S2 y 1 de 49 con ambos en S1, p=0.01
(Results, p. 46). Ocho pacientes con un solo tornillo se excluyeron de esa comparacion.
No se deben convertir estos pares en probabilidades de brecha cortical por tornillo.

**Limite:** la serie es retrospectiva y el cambio de colocacion hacia S1 ocurre durante
el periodo estudiado. El paper reconoce sesgo por curva de aprendizaje. La CT se solicitaba inicialmente por sospecha y solo despues se hizo rutinaria;
la cohorte mezcla trauma, no union y dolor posparto. No se transporta su porcentaje
binario a la cohorte de la tesis. La asociacion
clinica respalda distinguir el nivel, pero no aisla un efecto causal de S2 ni demuestra
que toda tecnica tenga el mismo riesgo. Hinsche conserva valor de banco, deja de ser
el unico apoyo del eje.

**Aplicacion:** Problem Statement de `main.tex` cita directamente a van den Bosch y
explicita desenlace, unidad y sesgo. S1/S2 sigue como variable geometrica del muestreador;
no se introducen fenotipos ni una tasa neurologica como objetivo de SAP.

### 12 - CERRADA POR DELIMITACION: benchmark ordinal en S1; S2 descriptivo

**Correccion del diagnostico previo:** era incorrecto decir que no habia *ningun*
prior clinico leido. Zwingmann ya aporta las dos distribuciones ordinales por tecnica,
pero su ficha documenta **S1**, no distribuciones medidas para S1 y S2.

**Lo nuevo:** van den Bosch si publica 2.1%-6.8% de malposicion dependiendo de la
modalidad (abstract, p. 44). No es un intervalo de incertidumbre ni un rango por nivel.
La evaluacion de posicion es **binaria**, sin grados de penetracion en milimetros.
La Tabla 2 registra 11 tornillos malposicionados asintomaticos y 4 sintomaticos en CT;
son sobre **220 tornillos evaluados por CT** (suma propia de las cuatro celdas
de la tabla, corroborada por 218 + 2 en el texto), no sobre los 285 de toda la serie
(Results y Tabla 2, p. 46). No reconstruimos de ahi un prior ordinal ni porcentajes S1/S2.

**Resolucion aplicada al alcance:** se mantienen las dos distribuciones de Zwingmann
como referencias de SAP/Wasserstein-1 **en S1, separadas por tecnica**. S2 conserva
medicion de geometria y reporte descriptivo de grados; no se reclama ajuste a una
distribucion clinica ordinal S2. Corregidos Objetivo 2, Expected Results,
`00-tesis.md` y `03-glosario.md` para no prometer una tabla tecnica x nivel inexistente.

**Sentido del cierre:** se retira el compromiso sin fuente. Van den Bosch **no cierra
la carencia empirica de un prior ordinal S2**; esta queda declarada como limite de la
validacion, sin bloquear el alcance delimitado. Si se decide exigir calibracion clinica
S2, hay que reabrir #12 y obtener datos ordinales compatibles por nivel y tecnica.
No se mezclan posicion binaria, sintomas neurologicos y grados de brecha.

### Nivel de lectura y efecto sobre otras implicancias

- `vandenbosch2002`: **N1**, porque una lectura incorrecta de sus denominadores o
  desenlaces invalidaria el fundamento del eje S1/S2 y contaminaria SAP.
- `moed2006s2screw`: **N2 confirmado**. Ser via de acceso a una fuente primaria no
  convierte al intermediario en soporte del benchmark; la tesis cita el original.
- #25: se resuelve la procedencia de esta comparativa consultando el original, sin
  reabrir la cadena agotada del umbral de 10 mm.
- #26: sigue pendiente la medicion local de landmarks. Que van den Bosch eval?e
  tornillos por CT no constituye una caracterizacion del corredor bajo artefacto.

**Evaluacion de impacto:** si obliga a ajustar redaccion, supuesto y alcance de
validacion. Los cambios anteriores quedan aplicados por el encargo actual de resolver
las implicancias; no abre un nuevo baseline ni aporta una escala nueva de SAP.

## Auditoria de consistencia de Gardner y S1/S2 (2026-09-08)

**Verificacion:** contra la ficha completa `gardner2010safezones.md`, sus tablas y
localizadores; no se hizo una nueva lectura del PDF. La lectura previa si estaba
integrada parcialmente: existian fila LEIDO y bloque de resultados, pero convivian
con una fila duplicada PENDIENTE, rutas de lectura agotadas y propuestas descartadas.

**Correcciones aplicadas:** una sola fila de Gardner en candidatos, LEIDO; referencias
al estado final de la cadena de 10 mm y de Moed; estado vigente visible al inicio de
este archivo y encabezados #12/#27/#28 sincronizados. Corregidas ficha e indice:
222 frente a 220.1 mm2 no es inversion de medias, y la variacion anatomica no obliga
a estratificar por fenotipo ni permite heredar una distribucion clinica de poses.
La atribucion previa a #24 era incorrecta: esta cuestion corresponde al Objetivo 2
con #27; #24 trata de multi-ventana.

**Impacto en S1/S2:** Gardner ya aporta respaldo anatomico en CT para considerar los
dos niveles y medir su geometria individual. Decir que solo habia respaldo de plastico
confundia el texto entonces escrito en main.tex con toda la literatura ya leida.
Van den Bosch agrega un desenlace clinico por configuracion; no inaugura la evidencia
anatomica S1/S2 ni sustituye a Gardner. La similitud de areas no prueba igual seguridad.

**Impacto en SAP:** ninguno sobre la delimitacion vigente. Gardner mide corredores
y trayectorias ideales, no frecuencias de grados de brecha en colocaciones clinicas.
S1 mantiene el benchmark ordinal por tecnica; S2 sigue descriptivo. #27 no se reabre:
la medicion individual preserva la variabilidad anatomica sin introducir fenotipos.
No se adopta una regla universal de que S2 sea peor o mejor que S1.

**Estado:** correccion documental APLICADA a #7/#12/#25/#27/#28; no se adopta un metodo
nuevo ni se cambia el alcance. El texto actual de main.tex ya distingue resultados
clinicos y geometria individual y no afirma superioridad universal de S1 o S2.


### Gardner S1/S2 - respaldo anatomico APLICADO a la tesis (2026-09-08)

Por encargo explicito de la autora, incorporado a `00-tesis.md`, registrado en
`01-decisiones.md` y citado en Problem Statement y Objetivo 2 de `main.tex`.
Se explicitan las areas por nivel y morfologia con evidencia en la ficha, y su
limite: anatomia del lado no lesionado y trayectorias ideales, no prior clinico SAP.
Impacto: se completa el respaldo anatomico de la redaccion; no cambia el alcance
ni reabre #27, ni la delimitacion de #12. La medicion individual sigue vigente.

---

## Keating 1999 — lectura cerrada: SI aporta 13%, no el rango 2%-15%

- **Origen:** la autora subio `papers/keating1999iliosacral.docx`. No hay PDF.
- **Restriccion, y toca la regla 2:** la copia `.docx` disponible no conserva una
  paginacion impresa estable. El texto se extrajo completo al scratchpad, fuera del repo
  por la regla 6, y la ficha se genera desde ahi. **Todas sus citas llevan seccion, no pagina**,
  marcadas `(sin paginacion: fuente .docx)`. Inventar una pagina seria violar la regla 2.
- **Consecuencia practica:** si alguna cifra de Keating llega a la tesis y el formato de
  cita exige pagina, **hace falta el PDF real**. Hasta entonces la fuente es citable por
  seccion.
- **Nivel de acceso para `_index.md`:** `COMPLETO (.docx, sin paginacion)`. No es acceso
  limitado por contenido: el texto esta entero.
- **Aviso de trampa confirmado por la lectura:** el abstract de Keating contiene cuatro
  porcentajes que **NO son de malposicion** y que
  caen dentro o cerca de la banda 2-15%: `13%` (embolia pulmonar), `2.6%` (mortalidad
  hospitalaria), `15%` (pacientes **sin dolor**) y `11%` (fusion sacroiliaca por dolor).
  Ademas `44%`/`36%` son de **malunion**, no de posicion del tornillo. Cualquiera de las
  tres primeras podria citarse por error como tasa de malposicion y encajaria en la banda.
- **Ubicacion en la cadena, para no confundirla:** Keating **no** es fuente directa de
  `zwingmann2009navigated`. Zwingmann cita a Hinsche y Templeman; `hinsche2002fluoroscopy`
  no mide el rango y lo cita de Ebraheim 1993, **Keating 1999**, Routt 1997 y
  Templeman 1996. Keating es una fuente indirecta dentro de la cadena.
- **Veredicto contra el cuerpo:** **SI**, Keating escribe una tasa propia de malposicion:
  *"Screw misplacement occurred in five patients (13 percent)"* (Results; sin
  paginacion: fuente DOCX). El resumen solo escribe cinco pacientes y omite 13%, que
  explica por que una lectura limitada al abstract llega al veredicto PARCIAL.
- **Unidad y denominadores:** el resultado es **5 de 38 pacientes**, aunque se usaron
  85 tornillos. No corresponde calcular 5/85 como tasa por tornillo ni atribuirla al
  paper. La evaluacion es radiografica y binaria, sin umbrales de brecha en milimetros.
- **Que sostiene realmente:** un punto clinico interior de **13%**, compatible con la
  amplitud narrada por Hinsche. No publica el rango 2%-15%, no identifica sus extremos
  y no demuestra que el 2% o el 15% provengan de una fuente concreta.
- **Compatibilidad con la tesis:** no entra al benchmark SAP, porque no aporta la escala
  ordinal 0/<2/2-4/>4 mm, una distribucion por tornillo ni resultados S1/S2. La decision
  vigente de retirar el rango unico se mantiene.
- **Estado de #12:** no se reabre. La auditoria de procedencia queda mejor documentada,
  pero Keating no reemplaza las distribuciones ordinales de Zwingmann. Para reconstruir
  historicamente los extremos faltaria leer Ebraheim 1993, Routt 1997 y Templeman 1996;
  ya no es necesario para el alcance vigente.
- **Ficha:** `docs/literatura/keating1999iliosacral.md`.

**Evaluacion de impacto:** corrige la afirmacion documental de que ninguna fuente real
de la banda habia sido leida. No obliga a cambiar `main.tex`, `00-tesis.md`, alcance,
supuestos, baseline ni SAP: el rango 2%-15% ya esta retirado y el nuevo dato es binario
por paciente. Sin nueva implicancia abierta.

---

## 29 — TotalSegmentator como inicializacion anatomica, no como corredor — ABIERTA

- **Origen:** evaluacion solicitada por la autora el 2026-09-08 contra la documentacion
  oficial vigente de TotalSegmentator y las necesidades del Objetivo 2.
- **Aporte util:** la tarea CT `total` produce mascaras separadas de `sacrum`,
  `vertebrae_S1`, `hip_left` y `hip_right`; tambien incluye arterias y venas iliacas.
  Puede localizar la pelvis, proponer una ROI y dar una mascara osea inicial para el
  procesamiento geometrico. El proyecto oficial admite NIfTI y permite limitar clases.
- **Lo que no entrega:** S2 como clase independiente, cortical frente a trabecular,
  platillo superior de S1, crestas iliacas, espinas iliacas posteriores, punto de entrada,
  eje del corredor, diametro libre ni margen cortical. Esas variables siguen requiriendo
  geometria propia y las definiciones de Kaiser/McLaren/Gardner.
- **Limite critico:** el paper principal encontrado no documenta validacion especifica
  sobre osteosintesis pelvica con artefacto metalico. La clase opcional `hip_implant`
  identifica implantes de cadera, no tornillos o placas del anillo pelvico, y la propia
  documentacion advierte que las tareas entrenadas en datasets pequenos son menos robustas.
- **Uso recomendado:** herramienta de preprocesamiento no autoritativa sobre anatomia
  sin metal, con correccion/QC y version fijada. Para preservar bordes no usar `--fast`
  (3 mm); evaluar el modelo de 1.5 mm. Sus mascaras no son ground truth, restriccion
  quirurgica ni contribucion de la tesis.
- **Validacion minima antes de adoptarlo:** piloto local con casos limpios y con metal;
  comprobar superficie cerca de S1/S2, separacion correcta de sacro/S1, localizacion de
  los tres landmarks de Kaiser y fallos bajo streaking. Medir error de superficie en la
  region del corredor, no solo Dice global. Esto puede ejecutar parte de #26, pero no
  sustituye la revision de visibilidad de landmarks.
- **Efecto sobre alcance:** no reabre la evaluacion downstream ni cambia SAP. Puede reducir
  trabajo de implementacion del muestreador y hacer reproducible su inicializacion.
- **Pendiente de decision:** adoptar TotalSegmentator como generador de ROI/mascara inicial
  y correr el piloto; si se adopta, dar de alta y leer su paper antes de citarlo en la tesis.

---

## Ronda "la geometria que McLaren NO publica" — 7 lecturas (2026-09-08)

Fichas nuevas: `gottschling2009`, `grass2016`, `lee2014`, `wagner2017`, `mendel2011`,
`zhao2012`, `hasenboehler2011`. Kaiser ya estaba leido. Con esto **la seccion queda
agotada**: no queda ninguna fila PENDIENTE en ella.

La pregunta de la seccion era si alguna de estas fuentes entrega la geometria que
`mclaren2021corridor` declara haber determinado ("position, alignment and maximum
diameter") y solo reporta a medias. **Respuesta: si, repartida entre varias, pero
nunca en un mismo marco de referencia y nunca en la poblacion de interes.**

### 30 — La geometria existe, pero en marcos que no componen — ABIERTA

- **Origen:** las 7 lecturas de esta ronda.
- **Lo que cada fuente cubre del hueco:**

| Pieza que falta en McLaren | Quien la publica | Valor | Magnitud real que mide |
|---|---|---|---|
| Diametro S1/S2 | `grass2016` | S1 12.8 mm (IC95 12.1-13.5); S2 11.6 mm (IC95 11.3-11.9) | cilindro inscrito maximo |
| Diametro S1/S2 | `wagner2017` | S1cc 11.6 mm (DE 5.4); S2cc 14.0 mm (DE 2.4) | diametro limitante craneo-caudal |
| Diametro S1/S2 | `lee2014` | S1 14.4 (DE 3.8); S2 10.9 (DE 3.3); n=526 | seccion axial, estratificada por LSTV |
| Diametro por sexo | `grass2016` | S1 M 11.7 vs H 13.5; S2 M 10.6 vs H 12.2 | idem cilindro inscrito |
| Punto de entrada | `zhao2012` | S1: 42.21-63.69 mm por delante de la EIPS y 32.77-53.75 mm sobre la escotadura ciatica mayor. S2: 22.68-54.28 y 14.06-33.70 mm | par de distancias proyectadas en vista lateral estandarizada |
| Longitud | `zhao2012` | S1 136.90-174.34 mm; S2 120.50-149.90 mm | longitud de tornillo |
| Angulo axial | `hasenboehler2011` | S1 19.27 grados; S2 13.10 grados (medias) | angulo axial sobre CT de 3 mm |
| Forma del corredor | `wagner2017` | ovalada consistente; modelo PCA sobre 92 superficies homologas | modelo estadistico 3D |
| Regla de decision | `mendel2011` | boundary ratio 1.5 (BW/BH); VPP 97%, sensibilidad 94% | triangulo sacro lateral en vista lateral estricta |

- **El problema no es falta de numeros: es que no componen.** `grass2016` da un cilindro
  inscrito, `wagner2017` un diametro limitante en un solo eje y `lee2014` una seccion
  axial: **tres magnitudes distintas bajo el mismo nombre**. `zhao2012` da punto de
  entrada como distancias a dos landmarks proyectados, no como coordenadas en el marco
  del voxel. `hasenboehler2011` da angulos axiales en su propia convencion, no en la de
  `kaiser2014dysmorphism`. Ninguna terna (posicion, orientacion, diametro) es coherente
  consigo misma.
- **Consecuencia para el Objetivo 2:** estas cifras **no se pueden encadenar** para armar
  una pose. Sirven como **contraste de orden de magnitud** de lo que el muestreador mida
  en cada volumen; no sustituyen la medicion. Refuerzan la decision vigente en vez de
  ofrecer una alternativa a ella.
- **Efecto sobre #7:** no se reabre ni se agrava. Queda **cubierta operacionalmente y
  ahora ademas calibrada**: hay rangos publicados contra los que contrastar la salida.
- **Pendiente de decision:** si estos rangos entran en `main.tex` como tabla de contraste
  anatomico del muestreador, o se quedan como respaldo en las fichas.

### 30b — Wagner invierte el orden S1/S2 respecto a Gras — corrobora #12 y #27

`grass2016` mide S1 (12.8) mas ancho que S2 (11.6). `wagner2017` mide S2 (14.0) mas
ancho que S1 (11.6). `lee2014` mide S1 mas ancho que S2 y ademas halla que la fraccion
de pelvis sobre el umbral en S2 pasa de 26% a 73% segun haya o no vertebra transicional
lumbosacra. **No es discrepancia de datos: es discrepancia de definicion de diametro.**
Tres cohortes grandes (280, 156 y 526 pelvis) no coinciden en que segmento es mas amplio.

Es **respaldo cuantitativo publicado** para dos decisiones que hasta ahora se sostenian
solo por argumento: no imponer jerarquia universal S1/S2 (#12, delimitacion del
benchmark) y no estratificar por fenotipo sino medir volumen a volumen (#27). Se puede
escribir en la tesis como hallazgo de la revision, no como limitacion propia.

### 31 — El umbral de corredor es SIEMPRE calibre de tornillo mas holgura — ABIERTA

Septima confirmacion del patron de #25, y esta vez con salida constructiva. Ninguna
fuente mide un umbral de seguridad; cada una lo **deriva del implante**:

| Fuente | Umbral | De donde sale |
|---|---|---|
| `gardner2010safezones` | 10 mm | consenso por calibre de tornillo (ya auditado) |
| `kaiser2014dysmorphism` | 10 mm | elegido, atribuido a terceros |
| `mclaren2021corridor` | 10 mm | heredado; declara que "has not yet been established" |
| `lee2014` | 10 mm | citado de Gardner; lo llama "an arbitrary safety threshold", para tornillo de 6.5-8.0 mm |
| `grass2016` | **9 mm** | propio: "cutoff for placing a 7.3-mm cortical screw" |
| `wagner2017` | **12 / 8 mm** | 12 mm tomado de Carlson; el rango se deriva de implantes de 6.0-7.3 mm |
| `mendel2011` | ratio 1.5 | calibrado contra un tornillo canulado de 7.3 mm |

- **Que significa:** el umbral no es una propiedad de la anatomia, es una **funcion del
  implante**. Siete fuentes lo confirman por convergencia independiente y dos lo dicen en
  su propio texto.
- **Salida constructiva:** el muestreador **no tiene por que adoptar un escalar fijo de
  10 mm**. Puede expresar la restriccion como `Dmax >= d_implante + holgura`, con
  `d_implante` tomado del banco propio de 61 geometrias y la holgura declarada como
  parametro. Convierte una convencion heredada y debil en una restriccion **derivada e
  interna al metodo**, coherente con el insumo propio del proyecto, y hace de la
  sensibilidad al umbral una ablacion natural en vez de un supuesto oculto.
- **Efecto sobre #25:** no la reabre, la completa: la cadena era una convencion, y ahora
  se sabe **de que es funcion** esa convencion.
- **Pendiente de decision de la autora:** adoptar o no la formulacion parametrica. Toca
  `main.tex` (Objetivo 2) y `03-glosario.md`. **No aplicado.**

### 26 — CUARTA, QUINTA Y SEXTA CONFIRMACION: nadie ha medido corredores con metal

`grass2016` excluye explicitamente: *"Pelves with fractures, pelvic ring deformity, hip
dysplasia, or hardware in situ were excluded"* (Materials and Methods, p. 2306).
`wagner2017` excluye 6 fracturas y 13 patologias oseas, y admite en Limitaciones que una
fractura desplazada reduciria los corredores **sin cuantificarlo**. `zhao2012` usa 66
pelvis sanas. Con Kaiser, McLaren y Ziran ya contados, son **seis cohortes consecutivas
de pelvis intactas**.

El parrafo `Field limitation` de `main.tex` ya afirma esto y ahora tiene tres fuentes mas.
**No requiere cambio de redaccion**; a lo sumo ampliar la lista de ejemplos. R1 se sigue
cerrando midiendo en casa, no leyendo.

### 32 — `gottschling2009` no documenta ninguna medicion sacra — ABIERTA

- **Hallazgo:** el paper que `mclaren2021corridor` cita como su metodologia de extraccion
  automatica de contorno oseo trata **exclusivamente femur y tibia** (1265 femures, 805
  tibias; mide diametro de cabeza femoral y longitud femoral). Las palabras pelvis, sacro,
  corredor, cilindro, tornillo e implante **no aparecen en su texto**.
- **Tampoco es reimplementable tal cual:** da la formulacion (mapeo por deformacion no
  rigida y funcion de energia sobre transformadas de distancia con signo) pero no los
  parametros de implementacion ni el nombre del software, y remite a tres referencias
  externas para las piezas clave.
- **Consecuencia:** la unica parte de McLaren que la tesis pensaba heredar como ejecutable
  —el procedimiento de Dmax— **no tiene ancestro publicado que lo describa sobre el
  sacro**. McLaren queda como fuente del **criterio** (Dmax como escalar de viabilidad),
  no de una **implementacion** heredada.
- **Efecto:** no rompe nada, porque la decision vigente ya es medir el corredor con
  geometria propia sobre cada volumen. Pero cambia **como se cita a McLaren**. Si
  `main.tex` insinua herencia de implementacion, hay una frase que ajustar.
- **Pendiente:** que la autora revise con esto en mano la redaccion del Objetivo 2.

### 33 — La cifra de dismorfismo "hasta 50%" no la sostiene la fuente titulada asi — ABIERTA

- **Verificado literalmente en el PDF de McLaren (Discusion, p. 6):** *"Several studies
  reported a prevalence of sacral dysmorphism as high as 50% [9, 19, 39]."* Es una **cita
  colectiva a tres fuentes**, sin atribuir el 50% a ninguna en particular. Las tres son
  `gardner2010safezones` [9], `kaiser2014dysmorphism` [19] y `hasenboehler2011` [39].
- **Lo que dicen esas fuentes, ya leidas las tres:**
  - `hasenboehler2011`, el unico estudio de los tres **titulado** "Prevalence of sacral
    dysmorphia" y el unico prospectivo de prevalencia: **14.2%-14.5%** (49 de 344; el PDF
    tiene esa inconsistencia interna entre abstract y cuerpo). Maximo por subgrupo 19.2%
    en mujeres.
  - `kaiser2014dysmorphism`: *"The dysmorphic phenotype was identified in 41% of the
    cohort"* (Resultados, p. e120(4)).
  - `gardner2010safezones`: su muestra es de 28 sacros normales y 22 dismorficos, es decir
    una composicion **elegida por diseno**, no una prevalencia poblacional.
- **Conclusion defendible:** ninguna de las tres publica un 50%. La cifra mas alta
  disponible es el 41% de Kaiser, y **la unica medicion de prevalencia real de las tres es
  14.2%-14.5%**. HIPOTESIS NO VERIFICADA, no citable: el 50% podria venir de leer la
  composicion muestral de Gardner (22/50 = 44%) como si fuera prevalencia. No hay frase
  que lo respalde y no debe escribirse como afirmacion.
- **Que se puede afirmar en la tesis, y que no.** SI: que la prevalencia publicada de
  dismorfismo sacro varia entre 14.2% y 41% segun definicion y cohorte, con las tres
  fuentes citadas. NO: repetir "hasta 50%", ni siquiera citando a McLaren.
- **Efecto:** no toca el muestreador (los fenotipos ya estan fuera de alcance por #27).
  Toca la **justificacion epidemiologica** si en algun momento se escribe una cifra de
  dismorfismo, y suma un caso mas al patron de #25, esta vez de cifra **alterada al alza**
  y no solo de umbral heredado.
- **Pendiente de decision:** que la autora confirme que ninguna version de "hasta 50%"
  entra a `main.tex`.

### Niveles propuestos para las 7 fichas nuevas

`grass2016` N1 (geometria en mm que sustituye el hueco de McLaren, con cohorte de 280),
`wagner2017` N1 (geometria y modelo de forma, y es quien invierte el orden S1/S2),
`lee2014` N2 (eslabon auditado del 10 mm, mas geometria y efecto LSTV),
`hasenboehler2011` N2 (angulos axiales y prevalencia; origen de #33),
`zhao2012` N2 (punto de entrada y longitudes),
`mendel2011` N2 (regla de decision alternativa a Dmax),
`gottschling2009` N3 (contexto metodologico; no aplica al sacro).
Decision de nivel: de la autora.

### 30 — AMPLIADA con `ebraheim1997`: septimo marco, misma incompatibilidad

Lectura del 2026-09-08 por decision de la autora (una de las dos finales de la linea).
**Es la fuente con geometria mas fina del pediculo de S1 vista hasta ahora**, y confirma
#30 en vez de resolverla.

| Pieza | Valor | Frase original | Seccion / pagina |
|---|---|---|---|
| Altura pedicular anterior S1 | 30.2 ± 3.4 mm (24-38) | *"anterior pedicular height (30.2 ± 3.4 mm, range 24-38 mm)"* | Results, p. 843 |
| Altura pedicular posterior S1 | 26.1 ± 3.4 mm (21-35) | *"posterior pedicular height (26.1 ± 3.4 mm, range 21-35 mm)"* | Results, p. 843 |
| Profundidad del pediculo | 27.8 ± 2.7 mm (24-32) | *"pedicular depth (27.8 ± 2.7 mm, range 24-32 mm)"* | Results, p. 843 |
| Altura posterior del ala | 28.7 ± 5.1 mm (20-37) | *"posterior alar height (28.7 ± 5.1 mm, range 20-37 mm)"* | Results, p. 844 |
| Profundidad del ala | 45.8 ± 1.9 mm (43-48) | *"alar depth (45.8 ± 1.9 mm, range 43-48 mm)"* | Results, p. 844 |
| Punto de entrada | 3-3.5 cm por delante del borde posterior del ilion, plano sagital | *"3 to 3.5 cm anterior to the posterior border of the iliac bone"* | Abstract, p. 841 |
| Longitud segura | hasta 80 mm | *"The safe length of the iliosacral pedicular screw is up to 80 mm"* | Abstract/Discusion, p. 841/845 |
| Margen entre dos tornillos | 4-6 mm | *"The safety margin for two closely inserted pedicular screws was only 4 to 6 mm"* | Abstract, p. 841 |

**Dos avisos que hay que respetar al citarla, o se cometen errores de magnitud:**

1. **El punto de entrada NO es comparable con el de `zhao2012`.** Ebraheim mide 3-3.5 cm
   por delante del **borde posterior del ilion**; Zhao mide 42.21-63.69 mm por delante de
   la **espina iliaca posterosuperior**. Landmarks distintos: los numeros no se promedian
   ni se contrastan entre si. Septimo marco de referencia incompatible de la linea.
2. **Las longitudes tampoco son comparables.** Los 80 mm de Ebraheim son de un tornillo
   **pedicular unilateral en S1**; los 136.90-174.34 mm de `zhao2012` son de un tornillo
   **alargado / transsacro**. Son construcciones quirurgicas distintas. Mezclarlas
   produciria un rango absurdo de 80-174 mm.

**Lo que si aporta y no tenia ninguna otra fuente:** el **margen de 4-6 mm entre dos
tornillos** en S1. Es la contraparte fina del dato grueso de `mclaren2021corridor` (17 mm
de corredor para dos tornillos, alcanzado solo por el 19.2%). Si el muestreador llega a
generar configuraciones de dos tornillos, esta es la unica cifra publicada de separacion
disponible.

**Lo que no aporta:** ningun angulo en grados contra planos anatomicos (solo
"perpendicular a la tabla iliaca"), ninguna separacion por sexo, ninguna area, y **nada
de S2**. El hueco angular de McLaren sigue abierto tras siete fuentes.

**Efecto:** ninguno sobre el alcance. Refuerza #30 y da cifras de contraste mas finas
para el Objetivo 2. **No aplicado a `main.tex`.**

### Nivel propuesto para `ebraheim1997`
**N2.** Aporta geometria de contraste util y una cifra unica (4-6 mm), pero no entra al
muestreador como restriccion ejecutable: sin angulos y sin S2, no cierra una pose.
Decision de nivel: de la autora.

---

## Ronda 2026-09-09 — primer experimento del giro a benchmarks (E1)

Ejecutado `experiments/exploration-3d/sensibilidad_hu.py` sobre los 178 volumenes
locales. Solo lectura de `data/`; `revision.csv` intacto. Salidas:
`sensibilidad_hu.csv`, `sensibilidad_hu.md`, `sensibilidad_hu.log`.

### 22 — EJECUTADA. El recuento existe y el 2500 queda respaldado por medicion

**Lo que pedia la decision del 2026-09-08:** recontar la cohorte a 1500, 2500 y 3500 HU
y reportar cuantos volumenes cambian de clase. **Hecho.**

| Umbral | candidatos | limpios (no candidatos) | Metal=si y NO candidato |
|---:|---:|---:|---:|
| 1500 | 177 de 178 | 1 | 0 |
| 2500 | 113 de 178 | 65 | 0 |
| 3500 | 104 de 178 | 74 | **5** |

- **Cambios de clase:** 64 volumenes dejan de ser candidatos al pasar de 1500 a 2500;
  9 mas al pasar de 2500 a 3500.
- **Reproducibilidad:** las 178 clasificaciones a 2500 HU coinciden exactamente con la
  columna `Candidato HU` de `revision.csv`. Cero desacuerdos. El cribado es determinista.
- **1500 HU no criba:** deja 177 de 178 como candidatos y solo 1 volumen limpio en toda
  la cohorte. Confirma con medicion que a 1500 HU entra hueso cortical, no solo metal.
  **Queda descartado como umbral de cribado.**
- **2500 HU tiene cero falsos negativos** contra la revision 3D completa de la autora:
  ningun volumen que ella marco `Metal=si` u `Objeto extraño=si` cae del lado limpio.
  Es la primera validacion medida del umbral que ya se usaba.
- **3500 HU gana 9 volumenes de entrenamiento y pierde 5 metales reales.**

### 34 — El umbral de cribado y la definicion de `Objeto extraño` son LA MISMA decision — ABIERTA

- **Origen:** E1, 2026-09-09. Hallazgo no previsto por la decision del 2026-09-08.
- **Hallazgo:** los 5 volumenes que 3500 HU pierde son los cinco `accesorio` de dataset6
  (`CLINIC_0036`, `0068`, `0078`, `0084`, `0097`; HU maximo entre 2701 y 3395), material
  **extracorporeo**, no osteosintesis. Ninguno es implante.
- **Consecuencia:** subir a 3500 no es "perder metal" en general, es **perder exactamente
  la clase de objeto cuya inclusion #22 dejaba sin definir**. Las dos preguntas abiertas
  colapsan en una:
  - Si `Objeto extraño` incluye lo extracorporeo -> el umbral es **2500** y el
    entrenamiento limpio por HU son **65** volumenes.
  - Si `Objeto extraño` se restringe a lo intracorporeo -> **3500** no pierde ningun
    implante y el entrenamiento limpio por HU sube a **74**.
  Son 9 volumenes de diferencia, todos de dataset6.
- **Cautela de interpretacion:** estos 65 y 74 son cohortes **por criterio HU puro**, no
  las cifras de 70 y 97 que salieron de la revision 3D. Las tres definiciones son
  distintas y no se deben mezclar en la data card.
- **CORRECCION 2026-09-09 de una afirmacion sin respaldo.** La primera version de esta
  entrada decia que "un accesorio extracorporeo a 3000 HU produce estrias que atraviesan
  el campo". **Eso no esta medido ni citado, y como enunciado general es falso.** La
  amplitud del streaking no es funcion del HU maximo: depende de la seccion que el objeto
  presenta a los rayos, de su composicion y del recorrido de atenuacion, no de su pico
  reconstruido. Un piercing de 1 mm y un tornillo de 7.3 mm pueden reconstruirse al mismo
  HU y producir artefactos de ordenes de magnitud distintos. Ademas el HU pico de un
  objeto metalico ya viene corrompido por su propio artefacto: es un efecto, no una
  medida de atenuacion.
- **Lo que si se puede afirmar:** la clase de objeto que 3500 HU descarta es
  extracorporea. **Si produce o no artefacto dentro del ROI oseo esta SIN MEDIR.**
  La pregunta que la autora ya lleva al asesor ("el entrenamiento exige limpio de objeto
  o limpio de artefacto?") sigue siendo la que decide, pero decidirla por HU es decidirla
  por la variable equivocada. Requiere un estimador de artefacto sin referencia (ver la
  cautela de #16 sobre streak amplitude sin par sin metal). Propuesto como E7, no corrido.
- **Que seccion toca:** criterio de exclusion del entrenamiento; `02-datos.md`;
  `03-glosario.md` (redaccion de umbral unico).
- **Tipo:** DEFINICION. **Pendiente de decision de la autora. No aplicado.**

### Nota sobre #19

`CLINIC_0074`, el caso que motivo #19, aparece a 2500 HU con **0.632 mm3** (un solo
voxel) y desaparece a 3500. Su objeto tubular sigue sin ser detectable por umbral, tal
como registraba #19. La autora ya lo resolvio como "no es metal"; E1 no lo reabre, solo
mide por que ningun umbral de este rango lo encuentra.

### 34 — AMPLIADA con la evidencia de la propia revision 3D (2026-09-09)

Cruzada la columna `Artefactos` de `revision.csv` con `sensibilidad_hu.csv` para los 33
volumenes de dataset6 con objeto. **5 producen artefacto, 20 no, 8 inciertos.**

| Categoria | n | artef=si | no | incierto | mm3>2500 mediana | max |
|---|---:|---:|---:|---:|---:|---:|
| DIU (intracorporeo) | 6 | 2 | 3 | 0 | 269 | 368 |
| accesorio | 10 | 1 | 7 | 2 | 131 | 7801 |
| electrodo (cutaneo) | 7 | 0 | 3 | 4 | 121 | 456 |
| ropa (zipper/boton) | 10 | 2 | 6 | 2 | 1181 | 5361 |

Los cinco con artefacto: `CLINIC_0069` (accesorio **extracorporeo**, moderada, 7801 mm3),
`CLINIC_0007` y `CLINIC_0091` (zipper de ropa, leve, ~3700-4000 mm3), `CLINIC_0067` y
`CLINIC_0080` (**DIU**, leve, 204-272 mm3).

- **Rompe las dos intuiciones categoricas.** El artefacto **moderado** de toda la cohorte
  lo produce un objeto **fuera del cuerpo**: extracorporeo no es sinonimo de inocuo. Y un
  DIU de 204 mm3 produce artefacto mientras un accesorio de tamano parecido no: no es solo
  el volumen, es el camino de atenuacion acumulado, y el DIU esta profundo.
- **El umbral HU es ortogonal a la taxonomia.** Los 6 DIU son candidatos a 2500 **y** a
  3500; los zipper de ropa llegan a 5361 mm3. **Ninguna definicion categorica de
  `Objeto extraño` se puede implementar con un umbral HU.** Esto cierra la parte
  instrumental de #22: el umbral sirve para priorizar revision, no para definir cohortes.
- **Consecuencia practica:** la decision 2500 vs 3500 **no debe tomarse por el umbral**.
  Los 5 volumenes que 3500 pierde tienen `Artefactos = no` en cuatro casos e `incierto` en
  uno (`CLINIC_0097`), asi que por criterio de artefacto los cinco serian admisibles. La
  cohorte se define por la columna `Artefactos`, ya poblada por la autora, no por HU.
- **Argumento de asimetria, sin medicion adicional:** son 65 vs 74 volumenes, ~12% mas
  datos sobre una base pequena. Un volumen contaminado ensena al generativo a producir
  estrias **no pedidas por el condicionamiento**, lo que ataca la afirmacion central
  (streaking atribuible a la mascara y a B_delta). El costo de incluir supera al de excluir.
- **Pendiente de decision de la autora. No aplicado.**

### 35 — Una sola cohorte "limpia" para tres consumidores distintos — ABIERTA

- **Origen:** analisis del 2026-09-09 a raiz de las preguntas de la autora sobre DIU,
  piercing y objetos de ropa.
- **Hallazgo:** `Objeto extraño` hace hoy dos trabajos incompatibles: **describir** lo que
  hay y **decidir** que se excluye. Por eso lleva desde el 2026-09-07 sin cerrarse (#22).
  Y la regla de exclusion no puede ser unica, porque los tres objetivos no necesitan lo
  mismo:

| Consumidor | Que necesita limpio | Los 6 DIU |
|---|---|---|
| Obj 1 (multi-ventana) | nada; es per-voxel, y los volumenes con metal son mas informativos | incluir |
| Obj 2 (muestreador) | geometria osea sacroiliaca intacta y corredor libre | incluir (sin contacto oseo) |
| Obj 3 (renderizador) | ninguna fuente de artefacto sin enmascarar | excluir los 2 con artefacto |

- **Propuesta operativa:** separar la columna descriptiva de la regla. Descripcion en tres
  ejes independientes — **ubicacion** (intracorporeo / superficial / extracorporeo),
  **naturaleza** (osteosintesis pelvica / otro implante medico / no medico) y **efecto**
  (artefacto si / no / sin medir). `Objeto extraño` pasa a significar "cualquier material
  no anatomico presente, sea cual sea su ubicacion", sin juicio. La exclusion se construye
  sobre el eje **efecto** y se declara **por objetivo**.
- **Ventaja:** los tres ejes ya se pueden poblar con lo que la autora anoto; no exige
  revisar nada de nuevo. Y hace auditable en la data card por que un volumen entra en una
  cohorte y no en otra.
- **Que seccion toca:** `02-datos.md`, `03-glosario.md`, criterio de split.
- **Tipo:** DEFINICION. **Pendiente de decision de la autora. No aplicado.**

### 36 — El Objetivo 1 no es ejecutable como esta escrito: falta el VAE — ABIERTA

- **Origen:** montaje de E6 el 2026-09-09.
- **Hallazgo:** `tesis/main.tex` (Obj 1) define el Go/No-Go como el viaje
  `HU -> multi-ventana -> VAE -> HU` con MAE < 25 HU en hueso. Las ventanas estan
  documentadas en `03-glosario.md`. **El VAE no aparece en ningun documento del
  repositorio**: ni arquitectura, ni factor de compresion, ni pesos, ni si se entrena o se
  toma preentrenado. Tampoco `00-tesis.md` ni `01-decisiones.md` lo fijan.
- **Consecuencia:** el Objetivo 1, que es **obligatorio** y esta en el alcance minimo
  viable, no se puede ejecutar ni reproducir tal como esta enunciado. Es el unico objetivo
  del minimo con una dependencia tecnica sin declarar.
- **Mitigacion ya aplicada:** E6a mide solo `HU -> ventana -> HU`, que si esta
  especificado, y reporta una **cota inferior** valida para cualquier decodificador. Sirve
  de Go/No-Go parcial sin asumir nada sobre el VAE.
- **Pendiente:** que la autora fije el VAE. Hasta entonces E6b no corre.
- **Tipo:** ALCANCE. **No aplicado a `main.tex`.**

### 34 y 35 — CORRECCION DE PROCEDENCIA (2026-09-09). La columna `Artefactos` NO la lleno la autora

La autora advierte que no llenó `Artefactos` y que no tenía claro qué designaba.
**Verificado contra `revision.csv` y le asiste la razón.** En los tres casos revisados,
la parte de la autora en `Notas` dice únicamente `Autora: objeto observado en 3D = <tipo>`;
la descripción de estriación viene siempre del bloque `Agente:`, derivada de las láminas
PNG. Concuerda con `ESTADO.md`, que registra que la autora anotó **tipo y cantidad**.

**Qué queda invalidado de lo que escribí antes:**

- La frase "tus propias anotaciones lo demuestran" y "columna ya poblada por la autora"
  en #34 y #35 es **falsa**. La columna es **propuesta de agente sin validar**, del mismo
  estatus que `propuesta_clasificacion.csv`.
- La recomendación de #35 de **construir la regla de exclusión sobre el eje `efecto`
  usando la columna actual queda RETIRADA.** Construir cohortes sobre salida de agente no
  validada es exactamente lo que `01-decisiones.md` prohíbe para la clasificación de metal.
- Los 20 `Artefactos = no` son **afirmaciones de ausencia derivadas de unas pocas láminas
  axiales**, el mismo defecto ya registrado en #19 y #21 ("16 axiales no demuestran
  ausencia"). Son los menos confiables de toda la columna, y son justo los que sostenían
  que los 5 casos perdidos por el 3500 HU eran admisibles.

**Qué sobrevive:**

- La tabla de #34 sigue siendo útil, pero **como hipótesis a verificar**, no como
  evidencia. Reetiquetada: los 5 con artefacto son 5 **propuestas**.
- El hallazgo instrumental **no depende de esa columna y se mantiene**: los 6 DIU son
  candidatos a 2500 y a 3500, y los zipper de ropa llegan a 5361 mm3. Eso sale de
  `sensibilidad_hu.csv`, medido. El umbral HU sigue siendo ortogonal a la taxonomía.
- El **argumento de asimetría tampoco depende de la columna**, y con esta corrección se
  refuerza: si no se sabe cuáles de los 9 volúmenes en disputa están contaminados, la
  incertidumbre empuja a excluir, no a incluir.
- Los tres ejes propuestos en #35 (ubicación / naturaleza / efecto) siguen en pie como
  **estructura**. Lo que cambia es que el eje `efecto` **está vacío de evidencia válida**:
  hoy solo tiene propuestas de agente.

**Consecuencia:** el eje `efecto` necesita una fuente real antes de decidir cohortes. Dos
vías, no excluyentes: (a) revisión visual de la autora enfocada solo en estriación, o
(b) un estimador medido sin referencia (E7, no corrido; ver la cautela de #16 sobre
streak amplitude sin par sin metal). **Ninguna decisión de cohorte debería tomarse antes.**

### 37 — `revision.csv` no distingue por campo quien lo escribio — ABIERTA

- **Origen:** el error de procedencia del 2026-09-09 (ver la correccion de #34 y #35).
- **Hallazgo estructural:** las 178 filas llevan el mismo valor en `Revisor`
  (`Kiara (autora, 3D) + agentes clasificador-metal (laminas)`). **Ningun campo declara su
  autor.** La unica forma de saber si un dato lo puso la autora o un agente es leer el
  texto libre de `Notas` y buscar el separador `Autora: ... || Agente: ...`. Ese reparto
  no es uniforme: la autora aporto **tipo y cantidad**; `Artefactos`, `Severidad`,
  `Ubicación anatómica`, `Lateralidad` y `Confianza` vienen de las laminas.
- **Por que importa:** ya provoco un error real. Un analisis leyo `Artefactos` como dato
  verificado por la autora y construyo sobre el una recomendacion de cohorte. Volvera a
  pasar con cualquier otra columna mientras la procedencia siga solo en prosa.
- **Riesgo especifico:** las afirmaciones de **ausencia** (`no`) generadas por agente desde
  laminas axiales son las mas fragiles y las mas faciles de tomar por verificadas. Son
  tambien las que sostienen cualquier cohorte "limpia".
- **Salida barata:** una columna por eje con sufijo de procedencia, o un unico campo
  `Procedencia` con el reparto explicito. No exige revisar ningun volumen de nuevo.
- **Que seccion toca:** `02-datos.md` (data card, trazabilidad de la cohorte); criterio de
  split. No toca la tesis directamente, pero si la defendibilidad de las cifras de datos.
- **Tipo:** RIESGO. **Pendiente de decision de la autora. No aplicado.**

---

## BLOQUEO DECLARADO (2026-09-09) — entradas detenidas hasta que la autora marque artefactos

> Pedido explicito de la autora. Estas entradas **no avanzan** con analisis, lectura ni
> computo: su siguiente paso exige una observacion visual que solo ella puede firmar.
> Ver la correccion de procedencia de #34/#35: la columna `Artefactos` de `revision.csv`
> es propuesta de agente sin validar, y sus 20 `no` son afirmaciones de ausencia sacadas
> de pocas laminas axiales.

| # | Entrada | Que espera exactamente |
|---|---|---|
| 15 | Revision 3D y separacion de cohortes | eje `efecto` poblado antes de aprobar cualquier cohorte |
| 22 | Umbral de cribado y definicion de exclusion | la parte instrumental quedo cerrada por E1; la parte de cohorte espera artefactos |
| 34 | Umbral vs definicion de `Objeto extraño` | si los 5 casos que pierde el 3500 HU producen artefacto o no |
| 35 | Una cohorte para tres consumidores | el eje `efecto`, hoy vacio de evidencia valida |

**Alcance del bloqueo:** afecta la cohorte de entrenamiento del **Objetivo 3**
(renderizador). **No** bloquea el Objetivo 1 ni el Objetivo 2: el Obj 1 es per-voxel y el
Obj 2 trabaja sobre geometria osea, y ninguno depende de esta columna.

**Requisito previo, no posterior:** decidir #37 (procedencia por campo) **antes** de que la
autora empiece la revision. Si anota sobre la estructura actual, su observacion vuelve a
quedar indistinguible de la del agente y el bloqueo se reproduce.

**Que desbloquea:** la revision (a) de 33 volumenes de dataset6, mirando solo estriacion
alrededor del objeto ya localizado. No exige revisar los 178 ni recorrer todos los cortes.

## Ronda 2026-09-09 — E6a ejecutado (Objetivo 1, tramo sin VAE)

`experiments/objetivo1/e6a_codificacion.py` sobre los 178 volumenes. Mide solo
`HU -> ventana -> HU` con LW [-1000, 2000], MW [-320, 480], SW [-160, 240], a float, 16 y
8 bits, en ROI oseo (HU > 150) y de metal (HU > 2500). Sin VAE: es **cota inferior** de
cualquier decodificador. Salidas `e6a_codificacion.csv` / `.md` / `.log`.

### 38 — Las tres ventanas publicadas son REDUNDANTES en reconstruccion HU — ABIERTA

- **Medido:** `max |MAE LW - MAE oraculo|` en hueso a float = **0.0 HU exacto** sobre los
  178 volumenes. MW y SW estan **estrictamente anidadas** dentro de LW, asi que un
  decodificador que elija el mejor canal por voxel **nunca** prefiere MW ni SW. A 8 bits el
  oraculo si mejora a LW, pero solo **1.679 HU de mediana**: la unica aportacion medible de
  la multi-ventana en este eje es **resolucion de cuantizacion**, no rango.
- **MW y SW por si solas son inservibles en hueso**: MAE mediana 107.63 y 218.19 HU,
  ambas muy por encima del umbral de 25 HU, porque recortan todo lo que pasa de 480 y 240 HU.
- **CAUTELA, y es la parte que no se debe sobreinterpretar:** esto mide **fidelidad de
  reconstruccion HU**, nada mas. El beneficio que la literatura de MAR atribuye a la
  multi-ventana es de **aprendizaje** (dar al modelo contraste normalizado en varios rangos
  de tejido para que los gradientes esten bien escalados), y ese beneficio **no se puede
  observar en una prueba de ida y vuelta**. E6a **no refuta C3**. Lo que refuta es una
  justificacion concreta de C3: que la multi-ventana **preserve mejor los HU**. No lo hace.
- **Consecuencia para la redaccion:** si `main.tex` justifica la multi-ventana por
  preservacion de HU, esa frase no tiene respaldo medido y ahora hay evidencia propia en
  contra. Si la justifica por condicionamiento del aprendizaje, hace falta la ablacion del
  Objetivo 4, no el Go/No-Go del Objetivo 1.
- **Tipo:** RIESGO. **Pendiente de decision de la autora. No aplicado.**

### 39 — El Go/No-Go del Objetivo 1 no puede fallar en su cohorte y no dice nada del metal — ABIERTA

- **Medido, ROI oseo, cota del oraculo a float:**

| Cohorte | mediana | maximo | supera 25 HU |
|---|---:|---:|---:|
| dataset6 (sin metal) | **0.00 HU** | 30.81 | 2 de 103 |
| dataset7 (con metal) | **46.36 HU** | 274.49 | **48 de 75** |

- **En pelvis limpia el criterio pasa por construccion.** El hueso vive en [150, 2000] HU y
  LW lo cubre entero sin recortar: el error es **cero exacto** en la mediana. Un Go/No-Go
  que no puede fallar en la cohorte donde se va a evaluar no es una prueba.
- **En pelvis con metal el mismo criterio falla en 48 de 75**, y falla **antes del VAE**,
  solo por el techo de 2000 HU de LW. `main.tex` no declara sobre que cohorte se evalua el
  Objetivo 1, asi que el veredicto depende de una eleccion no escrita.
- **ROI de metal: MAE mediana 3588.80 HU** (rango 540 a 6844), identica a float, 16 y 8
  bits porque el error es **recorte puro**, no cuantizacion. El HU maximo mediano de
  dataset7 es **18 822** y llega a **24 970**, contra un techo de ventana de **2000**.
- **Colision de diseno:** la tesis debe **generar** metal. Una representacion que trunca a
  2000 HU no puede representar el objeto que se sintetiza, ni su beam hardening. Si el
  renderizador genera en espacio multi-ventana y decodifica, el implante sale recortado.
- **Salidas posibles, ninguna adoptada:** (a) una cuarta ventana de metal con techo
  suficiente, (b) mover el techo de LW, (c) compresion no lineal del rango alto, (d)
  declarar que el metal se compone fuera del espacio multi-ventana. **Decision de la autora.**
- **Que seccion toca:** Objetivo 1 (criterio y cohorte de evaluacion), C3, `03-glosario.md`
  (las tres ventanas), y el diseno del renderizador.
- **Tipo:** RIESGO. **Pendiente de decision de la autora. No aplicado.**

### 39 — AMPLIADA: el techo de 2000 HU tambien golpea el BASELINE (2026-09-09)

Consecuencia no registrada al abrir #39. El protocolo adoptado (`peters2025hybrid`, #14)
define **metal integrity** como el maximo HU dentro del ROI mas 250. Si el renderizador
genera en espacio multi-ventana y decodifica con el techo de LW en 2000 HU, el maximo HU
del implante sintetico queda **fijado en 2000 por construccion**, mientras el implante real
de dataset7 tiene mediana 18 822.

- **Efecto:** la metrica heredada no mediria calidad de sintesis, mediria el recorte de la
  representacion. Daria el mismo valor para cualquier implante generado, y una separacion
  artificialmente enorme contra el brazo fisico, que no pasa por esa representacion.
- **Alcance:** invalida la comparabilidad de **metal integrity** entre el brazo propio y el
  de `peters2025hybrid` mientras el techo siga en 2000 HU. **No** afecta bone integrity
  (el hueso limpio cabe en LW) ni SAP (es geometrica, no de intensidad).
- **Depende enteramente de como se resuelva #39.** Si se adopta una cuarta ventana de metal
  o se mueve el techo, esta ampliacion se cierra sola.
- **Tipo:** BASELINE. **Pendiente. No aplicado.**

### 40 — El banco de 61 geometrias: una linea, sin origen, sin formato, sin archivo — CERRADA (2026-09-09; ver cierre definitivo al final del bloque)

- **Origen:** la autora pregunta el 2026-09-09 a que se refiere el banco de 61 y donde
  descargarlo. La pregunta en si es el hallazgo.
- **Rastreo completo del repositorio.** La cifra aparece en **un unico lugar original**:

  `CLAUDE.md:23` — *"Insumo propio: un banco de 61 geometrias de implantes."*

  Todas las demas apariciones (`docs/ESTADO.md` lineas 27, 43 y 55) son **derivadas**:
  las escribio Claude en sesiones anteriores citando esa linea. No hay ninguna mencion en
  `00-tesis.md`, `01-decisiones.md`, `02-datos.md`, `03-glosario.md`, `05-asesor.md`,
  ninguna ficha de literatura ni ningun script.
- **Lo que NO existe en ninguna parte:** origen o proveedor, formato (STL, mallas,
  voxelizado, tabla de diametros), licencia, fecha de obtencion, ruta en disco, y que
  tipos de implante contiene. `data/` solo tiene dataset6 y dataset7.
- **`tesis/main.tex` ya compromete cosas sobre ese banco sin que exista.** La linea 111
  impone una **regla de aislamiento estricto**: *"Test implant geometries must not enter
  the bank consumed by the proposed sampler or the physical simulation arm."* Y C1 declara
  *"Non-biological rigid implant geometries"* como la primera contribucion.
- **Por que es critico:** sin el banco no hay **C1**, el muestreador (Obj 2) no tiene que
  colocar, **#31** no se puede formular (`d_implante` no existe), y el ROI de metal del
  protocolo de Peters no tiene geometria CAD de referencia. Toca el **alcance minimo
  viable**, no el completo.
- **Pregunta abierta, no resuelta y no asumida:** si el banco ya existe fuera del
  repositorio, hace falta su ruta y su procedencia. **Si no existe todavia**, la cifra 61
  es un plan, no un insumo, y `CLAUDE.md` la enuncia como algo ya disponible. La
  distincion cambia el cronograma.
- **Nota de proceso.** Una linea de `CLAUDE.md` se leyo durante varias sesiones como hecho
  verificado sin que nadie comprobara el archivo. Es el mismo patron de la columna
  `Artefactos` (#37) y del patron #25 en bibliografia: **un enunciado se propaga por
  citarse a si mismo.** Aqui el enunciado esta en las instrucciones permanentes, que es el
  lugar de mayor autoridad y menor verificacion del repositorio.
- **Que seccion toca:** C1, Objetivo 2, #31, ROI de metal, cronograma.
- **Tipo:** RIESGO. **Pendiente de la autora. No aplicado.**

### 40 — HIPOTESIS DE LA AUTORA REFUTADA: el 61 no sale de `exploration-3d` (2026-09-09)

La autora propone que el 61 pudiera ser un recuento de la exploracion local (volumenes
tras quitar duplicados y objetos no ortopedicos). **Refutado por cronologia, que es
prueba decisiva y no requiere interpretacion:**

| Evento | Commit | Fecha |
|---|---|---|
| Linea `banco de 61 geometrias` escrita en `CLAUDE.md` | `6ee6ad5` "scaffold inicial" | **2026-09-06** |
| Aparece `experiments/exploration-3d` | `3543bdc` "exploration" | 2026-09-07 |
| Revision 3D de los 178 volumenes | — | 2026-09-07 |

La linea esta en el **primer commit del repositorio**, un dia antes de que existiera
cualquier recuento local. **No puede derivar de el.** Ademas el banco son geometrias de
**implante** (insumo a colocar), no volumenes de **CT** (anatomia receptora): son
poblaciones distintas y contarlas juntas seria error de categoria.

**Aviso metodologico, deliberado.** Al probar la hipotesis se buscaron ~15 recuentos
plausibles y **uno dio 61** (`dataset7` con `Metal=si`, excluidos los de ubicacion
extracorporea, deduplicados por SHA256). **Ese 61 es coincidencia de busqueda, no
evidencia.** Probando suficientes combinaciones, cualquier cifra aparece. Ademas se
apoyaria en `Ubicación anatómica`, que es columna de agente sin validar (#37). Queda
anotado aqui precisamente para que nadie lo reencuentre dentro de un mes y lo tome por
confirmacion. Es el mismo mecanismo de #25.

**#40 sigue ABIERTA sin cambios:** el banco no tiene origen, formato, licencia ni ruta.

### 20 — VERIFICADO: el criterio de duplicados SI es de igualdad exacta

Consulta de la autora sobre si volumenes solo *parecidos* se contaron como copias.
**Verificado en `revision.csv`: no.** `Grupo duplicado` se llena con SHA256 sobre forma
mas vóxeles HU escalados; agrupa solo contenido **identico**. Seis grupos vigentes:

- **Cruzados:** `CLINIC_0037`=`metal_0061`, `CLINIC_0048`=`metal_0036`, `CLINIC_0070`=`metal_0064`
- **Internos de dataset7:** `metal_0012`=`metal_0021`, `metal_0013`=`metal_0043`, `metal_0046`=`metal_0074`

**El error que la autora recuerda existio y ya se corrigio.** El par
`metal_0059`/`metal_0071` se habia agrupado por **similitud** (mismo spacing y mismo HU
minimo), no por identidad. Tras su revision 3D se descarto el 2026-09-07 y quedo en
`01-decisiones.md`. Hoy sus hashes difieren (`c0564a2b6d4e` vs `a6ad7cbae19e`): confirmado
que no son el mismo contenido.

**Lo que sigue pendiente de #20 no cambia:** elegir representante en los 3 grupos internos
de dataset7. Eso bloquea el split.

### 40 — RESUELTA (2026-09-09). El 61 es de Liu 2021 y NO es un banco de geometrias

La autora identifica el origen. **Confirmado contra `docs/literatura/liu2021ctpelvic1k.md`**,
ficha ya verificada contra el PDF el 2026-09-06. Evidencia textual, Data annotation, p. 3:

> *"In total, we have annotations for 1109 metal-free CTs and 14 metal-affected CTs.
> The remaining 61 metal-affected CTs of image are left unannotated and planned for use
> in unsupervised learning"*

Corroborado por la Tabla 1, p. 3: `CLINIC-metal | 75 | ... | 0(61)/0/14`. Y por los datos
en disco: **61 + 14 = 75 = dataset7**, exacto.

**`CLAUDE.md:23` contiene dos errores de categoria encadenados:**

1. **Volumenes de CT leidos como geometrias de implante.** Los 61 son **CT de pacientes**
   sin anotar, la anatomia receptora. No son modelos de implante.
2. **Dataset publico de terceros leido como "insumo propio".** Son de `liu2021ctpelvic1k`,
   y **ya estan en disco**: son la mayor parte de dataset7.

**Efecto colateral util:** confirma #13 por segunda via y explica la composicion local
(103 CLINIC + 75 CLINIC-metal = 178).

**Correccion propuesta para `CLAUDE.md:23`** (la autora decide; no se edita por cuenta propia):

    Insumo de implantes: PENDIENTE DE DEFINIR. No existe banco de geometrias en el
    repositorio. (Los 61 CT sin anotar de CLINIC-metal son anatomia receptora de
    liu2021ctpelvic1k, no geometrias de implante.)

### 41 — C1 se queda SIN INSUMO: no existe ninguna fuente de geometrias de implante — ABIERTA

- **Origen:** resolucion de #40 el 2026-09-09.
- **Hallazgo:** la primera contribucion declarada de la tesis, **C1** en `main.tex:54`
  (*"Non-biological rigid implant geometries"*), **no tiene ninguna fuente**. El unico
  insumo que el repositorio nombraba resulto ser un recuento de CT ajenos. No hay STL, ni
  mallas, ni CAD, ni tabla de diametros, ni proveedor, ni paper de la bibliografia leida
  registrado como fuente de geometrias.
- **Lo que cae con esto, en cadena:**
  - **C1** no tiene insumo. Es la primera de las tres contribuciones del gap.
  - **Objetivo 2** (muestreador) es el **unico aporte propio del alcance minimo viable** y
    no tiene **que** colocar. Su salida es una pose; una pose sin objeto no es nada.
  - **#31 colapsa.** La formulacion `Dmax >= d_implante + holgura` tomaba `d_implante`
    "del banco de 61". Sin banco no hay `d_implante`, y la restriccion vuelve a depender
    del escalar heredado de 10 mm que #25 dejo desacreditado.
  - **`main.tex:111`** impone una regla de aislamiento estricto sobre "the bank": hoy
    regula un conjunto que no existe.
  - **`00-tesis.md:114`** habla de medir metal integrity "sobre geometria CAD propia".
    No hay CAD propio.
  - **Objetivo 3** (renderizador) se condiciona sobre la mascara del implante. Sin
    geometrias no hay mascara de condicionamiento ni B_delta que la rodee.
- **Gravedad:** es el **unico hallazgo de la sesion que toca el alcance minimo viable en su
  parte propia**. #38 y #39 tocan el Objetivo 1 y son corregibles moviendo un techo de
  ventana; esto no se corrige escribiendo, hay que conseguir o construir el insumo.
- **Opciones, ninguna adoptada y ninguna verificada por mi:** (a) banco propio construido a
  partir de los implantes segmentados en los 75 CLINIC-metal en disco — es la unica fuente
  que se sabe disponible, y tiene la ventaja de dar geometrias reales del dominio; (b)
  modelos CAD de fabricante o de repositorio publico, cuya existencia y licencia **no
  verifique y no debo afirmar**; (c) geometrias parametricas sinteticas (cilindros
  roscados, placas) con dimensiones tomadas de los rangos publicados que ya estan en #30 y
  #31. **La (a) y la (c) son ejecutables con lo que hay en disco hoy.**
- **Nota:** la opcion (a) tiene una tension que hay que declarar: extraer geometrias de los
  mismos volumenes que luego sirven de prueba viola la regla de aislamiento de
  `main.tex:111`. Si se adopta, el reparto entre banco y test debe fijarse antes.
- **Que seccion toca:** C1, `main.tex:54` y `:111`, Objetivo 2, Objetivo 3, #31,
  `00-tesis.md`, cronograma.
- **Tipo:** RIESGO. **Pendiente de decision de la autora. No aplicado.**

### 40 — PRECISION tras la observacion de la autora (2026-09-09)

La autora señala que el dataset se actualizo y que hoy son 1184 volumenes, de los cuales
75 son CLINIC-metal. **Hay que separar dos afirmaciones, porque solo una esta abierta:**

1. **1184 y 75 NO son una actualizacion: son cifras del propio paper de 2021.** Evidencia
   textual ya verificada en la ficha: *"including 1, 184 CT volumes of diverse appearance
   variations"* (Introduction, contribuciones, p. 2) y Tabla 1, p. 3:
   `CLINIC-metal | 75 | (0.83, 0.83, 0.80) | (512, 512, 334) | 0(61)/0/14 | Collected 2020`.
   El 61 y el 14 son el reparto **de anotacion dentro de esos mismos 75**, no un conteo
   anterior que 75 haya sustituido. Los tres numeros conviven en la misma tabla.
2. **Lo que si puede haber cambiado desde 2021 es el estado de ANOTACION de esos 61.**
   Eso no se puede verificar sin consultar el repositorio publico
   (`github.com/ICT-MIRACLE-lab/CTPelvic1K`) y **no esta verificado aqui**. Ya figuraba
   como pendiente en `ESTADO.md` ("ver si CLINIC-metal amplio su anotacion desde 2021").
   Si se amplio, **afecta a #13** (hoy 14 de 75 anotados) y podria reabrir la evaluacion
   downstream que se declaro fuera de alcance por esa misma razon.

**Lo que NO cambia en ningun escenario: #41.** Esten anotados o no, los 61 son **volumenes
CT de pacientes**, anatomia receptora. No son geometrias de implante. El error de categoria
de `CLAUDE.md:23` y la falta de insumo para C1 son independientes del estado de anotacion.

### 40 — CERRADA en su parte de versionado (2026-09-09)

La autora confirma que la exploracion local se hizo sobre la **version mas reciente** de
CTPelvic1K, asi que no hay anotacion nueva que perseguir. **La duda sobre el estado de
anotacion queda cerrada por declaracion de la autora, no por verificacion tecnica.**

- **Efecto sobre #13: ninguno.** Los 14 de 75 anotados siguen siendo la cifra vigente, y
  la evaluacion downstream sigue **fuera de alcance** por el punto 1 de `Fuera de alcance`
  en `00-tesis.md`. No se reabre el Objetivo 5.
- **Cautela unica, para el registro:** `revision.csv` reporta **0 mascaras locales
  vinculadas por nombre** en los 178 volumenes, asi que la disponibilidad de anotacion no
  se pudo comprobar contra el disco. Se toma la declaracion de la autora como fuente.
- **`CLAUDE.md:23` CORREGIDA** el 2026-09-09 con autorizacion explicita de la autora, con
  el texto propuesto en esta implicancia. **#40 CERRADA.** #41 sigue ABIERTA y no se ve
  afectada.

### 40 — CIERRE DEFINITIVO (2026-09-09). La autora retira su observacion

La autora declara que **se equivoco en su observacion** sobre el dataset: no hubo
actualizacion posterior a 2021 y **el estado de anotacion de los 61 volumenes no ha
cambiado**. Confirma ademas que **la lectura de la evidencia textual era correcta**.

- **Que queda en firme (sin cambios respecto a la ficha de `liu2021ctpelvic1k`):**
  1184 CT en total; `CLINIC-metal` = 75 volumenes; reparto de anotacion `0(61)/0/14`
  dentro de esos mismos 75. Los tres numeros son del paper de 2021 y conviven en su
  Tabla 1. No son cifras sucesivas ni sustituidas.
- **Efecto sobre #13: ninguno.** Los 14 de 75 anotados siguen vigentes. La evaluacion
  downstream sigue FUERA DE ALCANCE por el punto 1 de `Fuera de alcance` en
  `00-tesis.md`. El Objetivo 5 **no se reabre**.
- **Pendiente eliminado:** "ver si CLINIC-metal amplio su anotacion desde 2021" queda
  **cerrado**; ya no hay que consultar el repositorio publico por esta via.
- **Base del cierre:** declaracion de la autora, no verificacion tecnica contra el
  repositorio publico. Se deja constancia igual que en el bloque anterior.
- **#41 sigue ABIERTA y no se ve afectada.** Anotados o no, los 61 son volumenes CT de
  pacientes (anatomia receptora), no geometrias de implante. El insumo de implantes
  sigue PENDIENTE DE DEFINIR.

**#40 CERRADA en todas sus partes.**

### 42 — `CLAUDE.md` conserva dos afirmaciones que contradicen decisiones ya tomadas — ABIERTA

Detectadas al corregir la linea 23. Mismo patron de #40: el archivo de **mayor autoridad y
menor verificacion** del repositorio conserva enunciados que el proyecto ya descarto.

| Linea | Dice | Estado real |
|---|---|---|
| 17 | *"muestrea de la distribucion clinica real de malposiciones (31-60% segun Zwingmann et al. 2009)"* | **RETIRADO.** Punto 5 de `Fuera de alcance` en `00-tesis.md`: el rango no existe en el PDF, son dos complementos de brazos distintos (#12, #25). Se usan las dos distribuciones ordinales, solo en S1 |
| 27 | *"Baseline fisico de comparacion: XCIST/CatSim"* | **SUSTITUIDO.** #8 APLICADA: el brazo es el protocolo de `peters2025hybrid`. El punto 3 de `Fuera de alcance` declara la reimplementacion de XCIST FUERA |

- **Por que importa:** toda sesion nueva lee `CLAUDE.md` como contexto permanente y
  reintroduce lo que diga. Las dos afirmaciones estan **explicitamente descartadas** en
  `00-tesis.md`, asi que hoy el repositorio se contradice consigo mismo.
- **Correccion propuesta** (la autora decide; solo autorizo la linea 23 el 2026-09-09):
  en la linea 17, sustituir el rango por "muestrea de las distribuciones ordinales medidas
  por tecnica quirurgica, solo en S1 (ver `00-tesis.md`)"; en la linea 27, sustituir por
  "Baseline de comparacion: protocolo hibrido de `peters2025hybrid` (XCIST/CatSim queda
  como fundamento tecnico, no como brazo)".
- **Tipo:** REDACCION. **Pendiente de la autora. No aplicado.**

### 42 — APLICADA en las lineas 17 y 27 (2026-09-09), y AMPLIADA con dos hallazgos mas

**Aplicado con autorizacion explicita de la autora**, con el texto propuesto en esta
implicancia:

- **Linea 17:** el rango "31-60%" sustituido por "las distribuciones ordinales de
  malposicion medidas por `zwingmann2009navigated`, condicionadas por tecnica quirurgica y
  **solo en S1**", con la nota de que el rango unico quedo RETIRADO por no aparecer en el
  PDF (#12, #25).
- **Linea 27:** "Baseline fisico de comparacion: XCIST/CatSim" sustituido por el protocolo
  hibrido de `peters2025hybrid` (#8 APLICADA), dejando XCIST como fundamento tecnico y
  fuente de limites, **no** como brazo.

Con la linea 23 del turno anterior, son **tres** correcciones a `CLAUDE.md` el 2026-09-09.

**Barrido del resto del archivo. Dos hallazgos mas, NO aplicados:**

1. **`CLAUDE.md` se contradice a si mismo entre sus propias reglas 16 y 18.** La regla 16
   ordena registrar toda fuente procesada en `docs/literatura/_acceso.md` (linea 109); la
   regla 18 dice que `_index.md` absorbio ese registro y **prohibe crear `_acceso.md`**
   (linea 118). Una sesion que lea de arriba abajo obedece la 16 antes de llegar a la 18 y
   crea el archivo prohibido. **Correccion propuesta:** reescribir la regla 16 para que
   apunte a la columna de acceso de `_index.md`, y eliminar la mencion a `_acceso.md`.
2. **La linea 9 promete lo que el alcance excluye.** Dice que los implantes sinteticos son
   *"para usarlos como aumentacion de datos y mejorar la robustez de redes de segmentacion
   osea en la zona peri-implante"*. La **evaluacion downstream de segmentacion esta FUERA
   DE ALCANCE** (punto 1 de `Fuera de alcance` en `00-tesis.md`; `main.tex` dice
   *"Downstream segmentation impact is deliberately excluded"*). Como **motivacion** la
   frase es legitima; como esta escrita se lee como **entregable**. **Correccion
   propuesta:** anadir "La evaluacion downstream de segmentacion esta fuera de alcance
   (ver `docs/00-tesis.md`); la mejora de robustez es la motivacion, no un resultado que
   esta tesis mida." **Decision de la autora.**

**Nota de proceso:** cuatro afirmaciones obsoletas o contradictorias en un archivo de 120
lineas que toda sesion lee como verdad permanente. Conviene una revision periodica de
`CLAUDE.md` contra `00-tesis.md` cada vez que se cierre una implicancia con efecto de
alcance.

### 42 — CERRADA. Las cinco correcciones de `CLAUDE.md` aplicadas (2026-09-09)

Con autorizacion explicita de la autora, en tres turnos del mismo dia:

| Ubicacion | Antes | Ahora |
|---|---|---|
| Linea 23 | "Insumo propio: un banco de 61 geometrias de implantes" | "PENDIENTE DE DEFINIR. No existe banco... Ver #40 y #41" |
| Linea 17 | "malposiciones (31-60% segun Zwingmann et al. 2009)" | distribuciones ordinales por tecnica, **solo en S1**; rango RETIRADO (#12, #25) |
| Linea 27 | "Baseline fisico de comparacion: XCIST/CatSim" | protocolo hibrido de `peters2025hybrid` (#8); XCIST como fundamento tecnico, no brazo |
| Linea 9 | "para usarlos como aumentacion de datos y mejorar la robustez..." | la mejora se declara **motivacion, no resultado medido**; downstream FUERA DE ALCANCE |
| Reglas 16 y 18 | la 16 ordenaba crear `_acceso.md`, la 18 lo prohibia | ambas apuntan a la columna de acceso de `_index.md`; la contradiccion se nombra en la 18 |

**Verificado tras aplicar:** `docs/literatura/_acceso.md` **no existe** en disco, asi que
la regla 16 nunca llego a ejecutarse; la contradiccion se corrigio antes de causar dano.

**Barrido final del resto de `CLAUDE.md`:** revisadas las menciones restantes de B_delta
(~12 mm), difusion latente 2.5D con ControlNet, `_plantilla.md` y el pipeline de `refs/`.
**Todas siguen vigentes** contra `00-tesis.md` y `01-decisiones.md`. No quedan
contradicciones detectadas. **#42 CERRADA.**

**Recomendacion de proceso, no aplicada:** revisar `CLAUDE.md` contra `00-tesis.md` cada
vez que se cierre una implicancia con efecto de alcance. Cinco defectos en 120 lineas de un
archivo que toda sesion lee como verdad permanente no es una anomalia puntual.
