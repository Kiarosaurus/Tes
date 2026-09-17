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

### 12 — ACTUALIZACION tras leer ebraheim1993 (2026-09-14)

- **Veredicto:** Ebraheim 1993 **no publica ninguna tasa de malposicion**. Es un reporte de un caso: 1 paciente,
  2 tornillos canulados de titanio y 0 malposiciones reales (encabezado "Case Reports", p. 617). La unica
  frecuencia es cualitativa: *"while a rare occurrence, can result in significant morbidity"* (Discussion, p. 617).
  No es fuente del 2%, del 15% ni de la banda.
- **Cadena:** de las cuatro refs. de Hinsche (5, 11, 20, 24) quedan leidas Keating 1999 (5/38 pacientes, 13%) y
  Ebraheim 1993 (sin tasa). Sin leer: Routt 1997 y Templeman 1996 (este sin PDF). Ninguna fuente leida escribe los
  extremos de la banda.
- **El "pitfall":** error de proyeccion en la radiografia AP. Por *"superimposition of the posterior S1 foramen over
  the sacral ala"* (p. 617), un tornillo en hueso parece entrar al foramen S1; la CT intraoperatoria lo mostraba en
  hueso. Conclusion: *"an intraoperative or postoperative AP radiograph alone is insufficient"* (p. 617). Criterio
  binario y cualitativo, sin mm.
- **Lectura interpretativa (no es cifra del paper):** las tasas historicas medidas solo con radiografia, como el 13%
  de Keating, podrian incluir falsos positivos foraminales. El paper no cuantifica ese sesgo.
- **Compatibilidad con la tesis:** SAP se mide sobre CT y el benchmark usa las distribuciones de
  `zwingmann2009navigated`, medidas por TC postoperatoria. El paper no discute grosor de corte, volumen parcial ni
  artefacto metalico (NO ENCONTRADO EN EL PDF). El rango ya esta retirado. No cambia `main.tex`, `00-tesis.md`,
  alcance, supuestos, baseline ni SAP.
- **Opcional, lo decide la autora:** si algun dia se relata la historia del 2%-15%, o se menciona el sesgo de la
  evaluacion solo radiografica como limitacion de las tasas historicas, Ebraheim 1993 sirve solo como fuente
  cualitativa. No esta en `refs.bib` (decision de la autora del 2026-09-14: solo ficha).
- **Ficha:** `docs/literatura/ebraheim1993.md`, nivel propuesto N3.

**Evaluacion de impacto:** sin implicancia nueva abierta; #12 no se reabre.

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

---

## Ronda 2026-09-09 (tarde) — #37 aplicada, grupos propuestos, R1 y E6c ejecutados

### 37 — APLICADA a `revision.csv`, y AMPLIADA con una tercera clase de procedencia

`experiments/exploration-3d/procedencia.py` anade seis columnas a `revision.csv` derivadas
**solo** de lo que ya estaba escrito en `Notas`, fila por fila. No revisa ningun volumen,
no modifica ninguna columna existente (verificado: 0 celdas alteradas contra
`revision.csv.bak`) y es idempotente.

**Hallazgo que #37 no habia nombrado: la procedencia no tiene dos clases, tiene tres.**
Ademas de `autora-3D` y `agente-laminas` existe **`autora-regla`**: valores que no salen de
mirar el volumen sino de aplicar una regla general que la autora enuncio. Son decisiones
validas, pero **no son observaciones**, y hasta hoy eran indistinguibles de las que si lo
son.

Reparto medido sobre las 178 filas:

| Columna | Valores |
|---|---|
| `Procedencia metal` | `autora-3D` 99, `autora-regla` **79** |
| `Procedencia observación` | `autora-3D` 108, `autora-regla` 3, `sin dato` 67 |
| `Procedencia artefacto` | `agente-laminas` 113, `sin dato` 65 |
| `Procedencia localización` | `agente-laminas` 113, `sin dato` 65 |
| `Procedencia instrumental` | `script` 178 |
| `Validado por autora (artefacto)` | `no` 178 |

Las dos lineas que importan:

1. **En los 75 volumenes de dataset7, `Metal = si` no es una observacion per-volumen.**
   Sale de la regla *"fila en blanco en dataset7 = hay material ortopedico"*. Los otros 4
   `autora-regla` son los `borde FOV` de dataset6 resueltos por la regla del 2026-09-07.
   No hay **ni una sola** fila de dataset7 donde la presencia de metal se haya verificado
   mirando ese volumen. Para la data card esto no invalida nada —el dataset se llama
   CLINIC-metal— pero **no puede escribirse como hallazgo propio**.
2. **El eje de artefacto sigue sin una sola celda de la autora.** 113 de agente, 65 vacias,
   cero validadas. Confirma el bloqueo declarado, ahora legible por columna y no por prosa.

**Riesgo residual detectado, NO resuelto:** tres filas de dataset7 (`metal_0036`,
`metal_0061`, `metal_0064`) llevan `Metal = si` mientras su propia `Notas` dice *"SIN
material ortopedico"* por la regla de duplicados. La columna y la nota se contradicen. No
se toco ninguna de las dos: corregirlo es decision de la autora, y afecta a que cohorte
entran esos tres.

- **Tipo:** RIESGO. **APLICADA** en su parte instrumental; la contradiccion de las 3 filas
  y el destino de `02-datos.md` siguen pendientes de la autora.

### 43 — La particion unica por objetivo contradice a #35, y se entrega marcada — ABIERTA

- **Origen:** encargo de la autora del 2026-09-09 (un CSV con un grupo por imagen).
- **Producto:** `experiments/exploration-3d/grupos.csv`, generado por `grupos.py`.
- **Conflicto declarado:** #35 concluye que **una cohorte sirve a tres consumidores** y que
  la exclusion se declara *por objetivo*. Un volumen con metal es a la vez el mejor insumo
  del Obj 1 (per-voxel) y no apto para el Obj 3. Forzar un grupo unico por imagen
  **contradice esa conclusion**. Por eso el CSV trae las dos lecturas: `Elegible Obj1/2/3`
  (no excluyentes, que es lo correcto segun #35) y `Grupo` (la particion pedida).
- **Recuento de la particion propuesta:** `grupo 1` = 69, `grupo 2` = 36, `grupo 3` = 67,
  `excluido` = 6. Elegibles: Obj1 172, Obj2 103, Obj3 67.
- **Control aritmetico que sale exacto:** los 69 del `grupo 1` coinciden con los *"69 de
  contenido unico"* que la decision del 2026-09-07 ya habia calculado por otra via
  (75 - 3 cruzados - 3 internos). Es una verificacion independiente, no una coincidencia.
- **Lo que va marcado PROVISIONAL y por que:**
  - Los 3 duplicados internos de dataset7 se resuelven por indice menor. **#20 sigue
    ABIERTA**: es una regla determinista y reversible, no una decision.
  - El reparto por objetivo aplica la logica de **#35, que sigue ABIERTA**, y su eje de
    artefacto viene de agente bajo bloqueo (#34/#37). `Elegible Obj3` es el mas fragil.
- **Dos filas que la autora debe adjudicar a mano:** `dataset6_CLINIC_0058_data` y
  `dataset6_CLINIC_0074_data` caen en `grupo 3` (anatomia limpia para el renderizador)
  aunque en `0074` la autora **si vio** una estructura en lazo, registrada como no metal y
  por eso con `Tipo` vacio. La regla las deja limpias; su observacion dice que hay algo.
- **Tipo:** DEFINICION. **PROPUESTA. No aplicada, no adoptada.**

### 39 — EJECUTADA con E6c. Hay salida, y no es mover el techo — sigue ABIERTA la decision

`experiments/objetivo1/e6c_techo_lw.py` sobre los 178 volumenes, 0 errores. Ocho
configuraciones x cuatro profundidades. Mide **solo** recorte y cuantizacion, sin VAE
(#36 sigue abierta): es cota inferior de cualquier decodificador.

**Control de reproduccion:** con `pub` (las tres ventanas publicadas), dataset7 da mediana
**46.35 HU** y **48 de 75** fallando el umbral de 25 HU. E6a habia dado 46.36 y 48 de 75
por otro camino. Reproduccion independiente; la cifra de E6a queda confirmada.

MAE oraculo en hueso, mediana sobre los 178 (HU):

| Config | float | 16b | 12b | 8b | fallan 25 HU (float) |
|---|---|---|---|---|---|
| `pub` (techo 2000) | 0.94 | 0.95 | 1.02 | 2.18 | **50/178** |
| `LW4000` | 0.20 | 0.21 | 0.31 | 2.17 | 40/178 |
| `LW10000` | 0.00 | 0.02 | 0.25 | 3.72 | 3/178 |
| `LW20000` | 0.00 | 0.03 | 0.40 | 6.24 | **0/178** |
| `pub+MTW` (4a ventana) | 0.00 | 0.01 | **0.08** | **1.31** | **0/178** |
| `pub+asinh` | 0.00 | 0.01 | 0.13 | 2.07 | **0/178** |

En ROI de metal, mediana: `pub` 3588.80 HU; `LW20000` 0.00 / 20.62 (float / 8b);
`pub+MTW` 0.00 / 17.72; `pub+asinh` 0.00 / 32.02.

**Lo que decide esto y lo que no.** Tres configuraciones llevan el Go/No-Go a 0 de 178, asi
que el problema **tiene salida**. Pero no son equivalentes, y la diferencia esta donde #39
no la habia buscado:

- **Mover el techo de LW es la peor de las tres salidas.** `LW20000` resuelve el metal
  estirando la misma ventana sobre 21 000 HU, y paga esa cobertura en el rango
  diagnostico: **6.24 HU a 8 bits contra 2.18 de `pub`**. Empeora el hueso para arreglar
  el metal.
- **Anadir una CUARTA ventana de metal no tiene ese intercambio: es dominante.**
  `pub+MTW` gana a `pub` en **todas** las profundidades y en los dos ROI a la vez
  (hueso 8b: 1.31 contra 2.18). No es un compromiso mejor, es estrictamente mejor, porque
  anade un canal en vez de estirar uno existente.
- **La profundidad de bits no es un detalle de implementacion.** A float las tres salidas
  empatan en 0.00; solo se separan con precision finita. La columna de bits es el
  **sustituto medible de la precision efectiva del VAE**, que sigue sin especificar.
  Corolario de proceso: **decidir #39 antes que #36 es decidir en el orden equivocado.**
  Si el VAE tiene precision efectiva alta, las tres salidas empatan y la decision da igual.

**Precision sobre lo que E6a habia afirmado:** E6a dijo que el Go/No-Go *"no puede fallar
en pelvis limpia"*. Con la cohorte entera eso es cierto para la mediana pero **no para
todos**: `pub` falla tambien en **2 de 103** de dataset6.

- **Tipo:** RIESGO / DISENO. **EJECUTADA.** La eleccion entre `pub+MTW`, `pub+asinh` y
  `LW20000` sigue **pendiente de la autora**. No aplicada a `main.tex`.

### 44 — Los objetos "no ortopedicos" tambien rompen la codificacion — ABIERTA

- **Origen:** desglose de E6c por volumen, 2026-09-09.
- **Hallazgo:** los 2 volumenes de dataset6 que fallan el umbral de 25 HU con `pub` son
  `CLINIC_0005` (*"electrodos y zipper (cursor)"*, HU max **22 185**) y `CLINIC_0069`
  (*"accesorio"*, HU max **21 457**). Ambos estan en `grupo 2` de `grupos.csv`, es decir
  clasificados como objeto **no ortopedico** y por tanto tolerables para el Obj 2.
- **Por que importa:** un cursor de cremallera alcanza HU comparables a los de un implante.
  Radiologicamente **es metal**. La distincion "ortopedico / no ortopedico" es
  **quirurgicamente** valida y **radiologicamente** irrelevante: para la codificacion en
  HU, el eje que manda es la densidad, no la naturaleza del objeto.
- **A que afecta:** conecta #34 y #35 (la definicion de `Objeto extraño` y el reparto por
  objetivo) con #39 (la codificacion). Hasta ahora se trataban como decisiones separadas.
  Un volumen puede ser apto para el Obj 2 y a la vez romper la representacion del Obj 1.
- **Consecuencia para #43:** `Elegible Obj2 = si` no implica que el volumen sea inocuo para
  el resto del pipeline. La elegibilidad debe declararse **por eje** (densidad maxima
  presente), no solo por naturaleza del objeto.
- **Tipo:** DEFINICION. **Pendiente de decision de la autora. No aplicado.**

---

## Ronda 2026-09-10 — R1 corrido entero, duplicados parciales, E8 montado

### 45 — Hay DUPLICADOS PARCIALES que el SHA256 no ve, y uno contradice una decision ya registrada — ABIERTA

- **Origen:** R1 (2026-09-10). `metal_0011` y `metal_0034` dieron cresta, S1 por sagital y
  S1 por ala **identicos al 0.1 mm**. Tres medidas independientes no coinciden por azar.
- **Instrumento:** `experiments/exploration-3d/duplicados_parciales.py` hashea (blake2b)
  cada corte axial no constante de los 178 volumenes y lista los pares que comparten cortes.
  Salida `duplicados_parciales.csv`. **Control:** recupera los 6 grupos ya conocidos con
  todos sus cortes compartidos. Verificacion adicional voxel a voxel y contra el affine.
- **Hallazgo — tres pares nuevos, los tres del mismo estudio:**

| Par | Cortes | Compartidos | Relacion verificada |
|---|---|---|---|
| `metal_0011` / `metal_0034` | 351 / 350 | 350 | `0034` = `0011` sin su ultimo corte; mismo origen en el affine |
| `CLINIC_0038` / `CLINIC_0090` | 331 / 350 | 331 | `0038` = primeros 331 cortes de `0090`; mismo origen |
| `metal_0059` / `metal_0071` | 288 / 350 | **216** | cortes 0-215 de `0059` = cortes 134-349 de `0071`; desfase constante de 134 cortes = 107.2 mm, exactamente la diferencia de origen z del affine (1358.207 vs 1251.0) |

  Los cortes compartidos de `0059`/`0071` **no son triviales**: ~32% de voxeles de cuerpo
  (HU > -500) y metal de hasta 8218 HU. Son dos ventanas de FOV solapadas de **una misma
  adquisicion**: `0059` sigue 72 cortes mas arriba y `0071` 134 mas abajo.
- **CONTRADICE UNA DECISION REGISTRADA.** `01-decisiones.md` (2026-09-07) dice que
  `metal_0059` y `metal_0071` **"no son el mismo paciente"**, y `ESTADO.md` lo lista en
  Pendientes cerrados como DESCARTADO. La medicion dice lo contrario: comparten 216 cortes
  identicos bit a bit con geometria coherente. **No se edita `01-decisiones.md`** (regla 3).
- **Error propio que tambien queda corregido.** La entrada "#20 — VERIFICADO" de esta
  misma ronda del 2026-09-09 afirmaba: *"Hoy sus hashes difieren: confirmado que no son el
  mismo contenido."* **Esa inferencia era invalida**: un SHA256 sobre forma + voxeles
  distingue *forma*, no contenido; dos volumenes de distinta longitud nunca comparten hash
  aunque uno contenga al otro. Es de nuevo el patron de #25/#37/#40: un control que no
  podia fallar se tomo por verificacion.
- **Por que importa:**
  - **Fuga train/test y doble conteo** en el mismo sentido que #20. Ningun split puede
    tratar estos pares como independientes.
  - **Cifras que cambian** (si la autora adopta el criterio por estudio): dataset7 de
    "contenido unico" pasa de **69 a 67** (se pierden `0034` por copia y `0071` o `0059` por
    mismo estudio); dataset6 sin objeto pasa de **70 a 69** (`0038` ⊂ `0090`). `grupos.csv`
    (#43) tiene los 4 de dataset7 en `grupo 1` y los 2 de dataset6 en `grupo 3`.
  - **Medianas ya reportadas sobre 178** (E1, E6a, E6c, R1) cuentan dos veces estos
    volumenes. El efecto sobre medianas de 178 es pequeno, pero las cifras "de 75" y "de 103"
    no son de volumenes independientes.
  - **Limite del instrumento:** detecta solo cortes **bit a bit identicos**. Dos
    reconstrucciones distintas del mismo paciente (otro kernel, otro espesor) no comparten
    ningun corte y seguirian invisibles. `Grupo paciente` sigue vacio en las 178 filas.
- **Pendiente de la autora:** (1) revisar su decision sobre `0059`/`0071` con esta
  evidencia; (2) si el criterio de duplicado pasa de "contenido identico" a "mismo estudio";
  (3) representante en los grupos nuevos. **No aplicado a `revision.csv` ni a `grupos.csv`.**
- **Que seccion toca:** #20 (reabre su parte de criterio), #43, `02-datos.md`, split, y la
  cifra de test con metal (hoy "72 / 69").
- **Tipo:** DATOS / RIESGO.
- **Sospecha adicional, NO verificada (agente, mosaico de R1):** `metal_0065` y `metal_0066`
  se ven anatomicamente identicos (mismo tornillo, misma forma sacra) con distinto spacing
  (0.835 vs 0.770 mm), numero de cortes (332 vs 344) y HU maximo (18 816 vs 19 684). Encaja
  con dos reconstrucciones del mismo estudio: justo el caso que el hash por corte no puede
  detectar. Verificarlo exige registro rigido entre ambos, no hash.

### 45 — RESPUESTA DE LA AUTORA (2026-09-10) y propuesta de tratamiento por par

**Confirmado por la autora:** `metal_0059`/`0071`, `metal_0011`/`0034` y
`CLINIC_0038`/`0090` son el mismo paciente. En `0011`/`0034` y `0038`/`0090` los cortes de
diferencia no aportan informacion significativa. `metal_0059` aporta cortes superiores y
`metal_0071` inferiores, y los dos muestran el implante. `metal_0065`/`0066` le parecen la
misma persona escaneada dos veces: misma anatomia y artefactos, un hueso ligeramente rotado,
y distinta cantidad de segmentos del tornillo sobre 2500 HU.

**Mediciones de apoyo (2026-09-10):**

- `0059`/`0071`: el solape es bit a bit identico (216 cortes, desfase exacto de 134) y el
  affine en x/y coincide. **Se pueden unir sin interpolar**: `0071[:, :, 0:350]` seguido de
  `0059[:, :, 216:288]`, 422 cortes, origen z el de `0071`. Ademas son complementarios en
  R1: `0071` tiene **las dos crestas fuera del FOV** (marco no computable) y `0059` las
  tiene dentro.
- `0065`/`0066`: **no comparten ningun voxel** (spacing 0.835 vs 0.770 mm, 332 vs 344
  cortes) y sus origenes de coordenadas no tienen relacion: z = -1709.8 frente a +1322.1,
  y x/y distintos. Dos reconstrucciones del mismo dato crudo suelen conservar el marco de
  la mesa; con eso y la rotacion osea que ve la autora, **lo mas probable son dos
  adquisiciones**. No es demostrable sin DICOM (el NIfTI no trae serie ni hora).
- **E8 da en ese par una prueba test-retest del mismo implante.** El tornillo que cruza el
  sacro sale sobre 2500 HU como tres objetos (209 + 110 con 3 fragmentos + 272 mm3; tramos
  de 22-33 mm) en `0065`, y como dos piezas de 149 y 155 mm3 de **7.4 mm** en `0066`. Los
  pines del fijador salen estables (~15 000 mm3 en ambos). **Mismo tornillo, misma
  persona: el volumen segmentado cambia ~2x y la longitud visible de 33 a 7 mm segun la
  adquisicion.** Es evidencia directa para #46: la geometria por umbral depende del
  escaneo, no solo del implante. R1 es estable en el par (S1 bajo cresta 32.5 vs 34.5 mm;
  ancho de crestas 175.0 vs 172.3 mm; ambos marcos legibles).

**Propuesta (decide la autora):**

| Par | Relacion | Tratamiento propuesto | Unidad de conteo |
|---|---|---|---|
| `0011` ⊃ `0034` | subconjunto exacto | conservar `0011`, retirar `0034` | 1 paciente, 1 volumen |
| `0090` ⊃ `0038` | subconjunto exacto | conservar `0090`, retirar `0038` | 1 paciente, 1 volumen |
| `0059` ∪ `0071` | mismo escaneo, FOV solapados | **unir sin perdida** en un volumen derivado (script, no se toca `data/` original) | 1 paciente, 1 volumen |
| `0065` ~ `0066` | mismo paciente, casi seguro dos adquisiciones | **conservar ambos con el mismo `Grupo paciente`**; uno primario por regla fijada a priori; el otro solo como par de reproducibilidad | 1 paciente |

Regla general propuesta: **la unidad de independencia es el paciente, no el volumen.**
Mismo paciente, mismo lado del split, siempre. Las estadisticas de cohorte cuentan pacientes.
Si hay copia exacta o subconjunto, se conserva el contenedor; si hay FOV solapados del mismo
escaneo, se unen; si hay adquisiciones distintas, se conservan agrupadas y se declaran.

**Cifras si se adopta todo (con `metal_0068` sin osteosintesis, confirmado):** dataset7 con
osteosintesis **71 volumenes -> 65 pacientes** (75 - 3 cruzados - `0068` = 71; - 3 copias
SHA - `0034` - union `0059`/`0071` - par `0065`/`0066` = 65). dataset6 sin objeto
**70 -> 69**. **No aplicado** a `revision.csv`, `grupos.csv` ni `02-datos.md`.

### 45 — APLICADA en dos partes por orden de la autora (2026-09-10)

1. **Union `metal_0059` + `metal_0071`:** `experiments/exploration-3d/union_0059_0071.py`.
   Comprueba dtype, affine, desfase, los 216 cortes del solape, la ida y vuelta a ambos
   originales y la relectura desde disco, y aborta si algo falla. Resultado: 422 cortes en
   `data/derivados/dataset7_CLINIC_metal_0059u0071_union.nii.gz`, no versionado y con un
   nombre que no encaja con `*_data.nii*`, asi que los scripts siguen viendo 178. Hashes en
   `union_0059_0071.md`. Originales intactos.
2. **`Grupo paciente` lleno:** `experiments/exploration-3d/grupo_paciente.py`, con respaldo
   `revision.pre-paciente.csv` y la columna nueva `Procedencia paciente`. **178 volumenes =
   168 pacientes**; 10 grupos: 6 `hash-volumen`, 3 `hash-corte + autora`, 1
   `autora-visual + agente`. Verificado: 0 celdas ajenas alteradas, idempotente. El script
   **aborta** si aparece un par con cortes compartidos no confirmado por la autora.
   dataset7 con osteosintesis: **71 volumenes / 65 pacientes**; dataset6 sin objeto:
   **70 / 69**. `02-datos.md` actualizado.

**Sigue pendiente:** la regla a priori del volumen primario de `0065`/`0066`, la
correccion de la fila de `metal_0068` y el registro en `01-decisiones.md`. `grupos.csv`
(#43) no se regenero: sigue contando volumenes.

### 21 — `metal_0068` CONFIRMADO sin material ortopedico por la autora (2026-09-10)

Confirmado por la autora. CLINIC-metal sin osteosintesis: **4 de 75** (`0036`, `0061`,
`0064` por duplicado cruzado; `0068` por observacion). La regla "fila vacia en dataset7 =
material ortopedico" tiene al menos una excepcion observada: es un argumento mas para que
#37 distinga regla de observacion. **Falta que la autora corrija la fila en `revision.csv`
y lo registre en `01-decisiones.md`.**

### 26 — R1 EJECUTADO sobre los 178. El marco sobrevive al metal mas de lo temido; la heuristica, menos — sigue ABIERTA

`experiments/objetivo2/r1_landmarks.py` (v2b), `r1_resumen.py`, `r1_mosaico.py`. Salidas
`r1_landmarks.csv`/`.md`, `r1_estados.csv`, `r1_auditoria_s1.md`. 178 volumenes, 0 errores.
La v1 habia muerto por memoria en 17/178 sin registrarse; la v2 inicial, en 51/178.

**Diseno.** Cinco puntos del marco de Kaiser (S1, dos crestas, dos EIPS) localizados por
heuristica; en una esfera de 12 mm se mide fraccion de HU < -200 (estria oscura) y de
HU > 2500. El criterio de "contaminado" **no se invento**: es el maximo observado en 70
volumenes de dataset6 sin objeto (envolvente nula). Cohorte de evaluacion: 69 de dataset7
(regla provisional de #20; **antes de #45**, asi que incluye dos pares del mismo estudio).

**Resultado (evaluacion, n = 69):**

| | n |
|---|---|
| Marco computable (5 puntos hallados y dentro del FOV) | 60 |
| ... y con S1 en el nivel correcto segun auditoria visual (agente) | **52** |
| ... y ademas sin ningun punto contaminado | **33** |
| Crestas fuera del FOV (algun lado) | 8 |
| S1 no hallado | 4 |
| S1 en nivel equivocado (5 un nivel arriba, 3 grosero) o ambiguo (2) | 10 |

Contaminados por punto: S1 10, cresta der 5, cresta izq 3, EIPS 3 y 3. En calibracion, el
marco es computable en 57 de 70 **sin metal**: el FOV y la heuristica pierden casi tantos
volumenes como el artefacto.

**Tres lecturas, en orden de importancia:**

1. **El artefacto no es la causa principal de perdida del marco.** De 69, el FOV (crestas
   cortadas) y la localizacion fallida o erronea de S1 explican 17 perdidas (69 - 52); la
   contaminacion, 19 de las 52 restantes. En los 18 volumenes con candidato a tornillo
   iliosacro (E8, #46) S1 esta en el nivel correcto en los 18 y contaminado solo en **3**:
   el tornillo pasa entre 5 y 36 mm por debajo del platillo, fuera de la esfera. **La
   contingencia de `main.tex:115` ("computed on metal-free anatomy only") no parece
   necesaria para la mayoria**, pero la cifra aun no es citable (punto 3).
2. **El FOV es un limite no declarado.** 8 de 69 (y 4 de 70 en calibracion) no incluyen
   las crestas enteras. El marco de Kaiser **no se puede calcular** en esos volumenes con o
   sin metal. `main.tex` no lo contempla.
3. **La heuristica no es un instrumento validado.** Dos detectores independientes de S1
   fallan por un nivel vertebral (~30 mm, mas que la esfera) en casos distintos. La
   auditoria visual (agente, no autora) da 55 correctos, 8 errores, 2 ambiguos y 4 no
   hallados. Los 8 errores salen todos "limpios", o sea que **el error sesga la
   contaminacion hacia abajo**. Tambien se corrigio en la corrida un fallo de crestas
   (costillas en CT que llegan al torax, `metal_0063`).

- **Sensibilidad no medida:** "oscuro" (HU < -200) solo capta estria oscura severa; las
  estrias moderadas en hueso (de 150 a -200 HU) no cuentan. Es una cota **optimista** de
  legibilidad. Contaminado tampoco significa irrecuperable.
- **Lo que falta para cerrar #26:** (a) que la autora revise los 4 mosaicos
  (`outputs/r1_mosaico/`, 69 tejas, ~15 min) y firme el nivel de S1; (b) recontar con #45
  aplicado; (c) decidir si el FOV se declara criterio de exclusion del Objetivo 2.
- **Que seccion toca:** `main.tex:115` (Field limitation, contingencia), Objetivo 2, #29
  (TotalSegmentator da `vertebrae_S1` y resolveria el error de nivel, pero no es ejecutable
  en esta maquina: ~2 GB de RAM libres).
- **Tipo:** RIESGO (en proceso de cierre). **No aplicado a `main.tex`.**

### 46 — E8: los implantes de CLINIC-metal NO dan geometria utilizable por umbral — ABIERTA

`experiments/objetivo2/e8_censo_implantes.py` y `e8_resumen.py`; salidas
`e8_componentes.csv`/`.md`, laminas en `outputs/e8_qc/`. 75 volumenes, 0 errores. Objetos =
componentes de HU > 2500 con fragmentos colineales fusionados. **Clases morfologicas
propuestas por script, no tipos de implante.**

**Que contiene dataset7 (responde a la opcion 3 de #13, pendiente desde el 2026-09-06).**
Cohorte de evaluacion (69): objetos dentro del cuerpo alargados en 38 volumenes, masivos
(>= 15 cm3) en 19, laminares en 1, "otro" en 61. **Al menos 18 de 69** tienen un candidato
a tornillo iliosacro o transsacro (alargado, eje izquierda-derecha, 5-36 mm bajo el
platillo de S1). Las laminas revisadas (agente) muestran mezcla de tornillos iliosacros y
transsacros, fijadores externos con pines en las crestas, clavos y placas femorales, y
placas del anillo anterior. **CLINIC-metal es osteosintesis heterogenea, no una cohorte de
tornillos sacros.** 18 es cota inferior: la fusion no recupera tornillos con huecos > 20 mm
bajo 2500 HU (`metal_0000`, `metal_0024` en S2).

**Lo que decide sobre la via (a) de #41.** Sobre 62 objetos alargados:

- **10 de 62 salen partidos** a HU > 2500, y la fusion no alcanza a todos. Un tornillo
  transsacro de `metal_0065` queda en tres piezas y el candidato es solo su tramo central
  de 33 mm.
- **Diametro exterior del fuste: mediana 5.00 mm a HU > 2500 y 5.14 mm a semimaximo
  local** (p10 3.05, p90 7.19). Con 51 de 62 por debajo de 6.0 mm, **quedan bajo la
  envolvente de calibres de tornillo iliosacro recogida en #31 (6.0-8.0 mm)**. No se sabe
  el calibre real de estos implantes; lo que si se sabe es que la geometria extraida no
  coincide con la publicada.
- **El umbral de semimaximo local tiene mediana 2770 HU (p10 1736, p90 6548)** y el HU p50
  de estos objetos es 3266. Para la mayoria de los alargados, **2500 HU no infla por
  blooming: esta cerca del semimaximo y recorta la periferia**. La hipotesis de partida de
  E8 (blooming que engorda el implante) **no se sostiene** como efecto dominante.
- **Consecuencia:** la via (a) no se puede ejecutar como "segmentar por umbral y guardar la
  malla". Exigiria ajustar un modelo parametrico (cilindro + cabeza) a cada implante, y
  entonces sigue necesitando calibres publicados. Eso **acerca la via (a) a la (c)**: la
  geometria parametrica con rangos de #30/#31 es el insumo y los implantes reales sirven para
  **poses y contraste**, no para mallas.
- **Efecto sobre #39/E6c:** el HU tipico de estos tornillos (p50 ~3300) queda muy por debajo
  del pico de 18 822 que motivo la ventana de metal; el rango que el renderizador tiene que
  representar en tornillos sacros es mas bajo de lo que sugiere el maximo por volumen.
  Descriptivo, sin cambiar la tabla de E6c.
- **Que seccion toca:** #41 (vias a/c), #31 (`d_implante`), C1, #13, `02-datos.md`.
- **Tipo:** RIESGO / DATOS. **Pendiente de la autora. No aplicado.**

### 21 — `metal_0068` NO tiene material ortopedico denso (medido)

E8 no encuentra en `metal_0068` ningun objeto de HU > 2500 dentro del cuerpo. Su unico metal
es un componente de 2309 mm3 con fraccion dentro del cuerpo 0.0 (cremallera/accesorio en el
flanco; la MIP muestra una pelvis sin implantes; lamina en `outputs/e8_qc/`). En
`revision.csv` la fila dice *"Material ortopedico presente (regla de la autora para
dataset7)"* con `Procedencia metal = autora-regla`, y el `Tipo` anotado es solo
*"zipper (cursor) y accesorios"*. **Es la regla por defecto, no una observacion, la que le
asigna osteosintesis** (#37). Si se confirma, CLINIC-metal sin osteosintesis pasa de **3 a 4
de 75**. Material ortopedico de baja densidad (< 2500 HU) no queda descartado por esta
medicion. **Pendiente de la autora. No aplicado.**

---

## Cierre 2026-09-10 — decision por paciente APLICADA y recuentos rehechos

Orden explicita de la autora: registrar la decision, regenerar `grupos.csv`, recontar R1
por paciente y aplicar las correcciones pendientes. **Decision registrada en
`01-decisiones.md` (2026-09-10).**

### 45 y 21 — APLICADAS

- **`exclusiones.csv`** (`exclusiones.py`, nuevo): manifiesto de volumenes fuera de uso,
  **sin borrar ningun archivo**. 11 volumenes de 10 pacientes: 8 `retirado` (3 duplicados
  cruzados, 3 copias internas #20, `metal_0034`, `CLINIC_0038`), 2 `fusionado` (`0059`,
  `0071`) y 1 `secundario` (`metal_0065`, primario `0066` por spacing). Cada fila lleva
  motivo, evidencia, decision y estado de la decision.
- **`metal_0068` corregido en `revision.csv`** (`correcciones_autora.py`: comprueba el valor
  previo, idempotente, respaldo `revision.pre-correcciones.csv`). Cambia el bloque de la
  autora en `Notas` y `Procedencia metal` pasa de `autora-regla` a `autora-3D`. `Metal`
  sigue en `sí`: tiene metal (cremallera), lo que no tiene es material ortopedico.

### 37 — La "contradiccion" de tres filas no era tal

#37 registraba como riesgo que `metal_0036`/`0061`/`0064` llevan `Metal = sí` con una nota
de "SIN material ortopedico". **No hay contradiccion.** `Metal` significa presencia de
metal, sea cual sea: en dataset6 una cremallera o un electrodo tambien valen `sí` (las 33
filas con objeto), y los tres tienen cremallera, electrodos o DIU. El material ortopedico
no tiene columna propia: vive en `Tipo` y `Notas`, y en `grupos.py` como regla. Queda
cerrado el riesgo residual de #37. **El hueco de fondo sigue:** no hay columna explicita
de "material ortopedico".

### 43 — `grupos.csv` REGENERADO por paciente

`grupos.py` reescrito: lee `exclusiones.csv`, trata `metal_0068` como sin material
ortopedico, anade la union como unidad y **aborta si un paciente tiene mas de una unidad en
uso**. Resultado: **179 unidades** (178 + union) y **168 pacientes con exactamente una
unidad en uso**.

| Grupo | unidades = pacientes | antes (por volumen) |
|---|---|---|
| grupo 1 (material ortopedico) | **65** | 69 |
| grupo 2 (objeto no ortopedico) | **37** | 36 |
| grupo 3 (sin metal ni objeto) | **66** | 67 |
| excluido | 10 | 6 |
| reproducibilidad | 1 | — |

Solo cambian 7 filas: `CLINIC_0038`, `metal_0034`, `0059`, `0071` a excluido; `0065` a
reproducibilidad; `metal_0068` de grupo 1 a grupo 2; y la union nueva en grupo 1. **#35
sigue ABIERTA** (el reparto por objetivo es propuesta).

### 26 — R1 RECONTADO POR PACIENTE (sustituye las cifras sobre 69 volumenes)

R1 y E8 se corrieron tambien sobre la union; su lamina de QC muestra la costura continua,
las crestas dentro del FOV y S1 en su nivel (auditoria agente: `ok`). Cohorte de
evaluacion = `grupo 1` (65 pacientes); calibracion = 69 pacientes.

| Evaluacion (n = 65 pacientes) | n |
|---|---|
| Marco computable (5 puntos, en FOV) | 57 |
| ... con S1 auditado en el nivel correcto | **51** |
| ... y sin ningun punto contaminado | **32** |
| Crestas fuera del FOV | 7 |
| Auditoria de S1: ok / +1 nivel / grosero / ambiguo / no hallado | 53 / 4 / 2 / 2 / 4 |

Contaminados por punto: S1 10, cresta der 5, izq 3, EIPS 3 y 3. Calibracion: marco
computable en 56 de 69. Pacientes con candidato iliosacro: **17**, todos con S1 correcto y
**3** con S1 contaminado. **Las tres lecturas de la entrada anterior se mantienen** (el FOV
y la heuristica pesan mas que el metal; el FOV es un limite no declarado; la heuristica no
esta validada). Siguen faltando la firma de la autora sobre los mosaicos y la decision
sobre el FOV.

### 46 — E8 RECONTADO POR PACIENTE

Sobre 65 pacientes: objetos alargados en 36, masivos en 17, laminar en 1; **al menos 17**
con candidato iliosacro o transsacro (21 objetos). Alargados: 57, de ellos **9
fragmentados**. `d_ext_semimax` con mediana **5.08 mm** (p10 2.99, p90 6.11), y **49 de
57 por debajo de 6.0 mm**. Umbral de semimaximo con mediana 2818 HU; HU p50 3296. **Las
conclusiones de #46 no cambian.**

### 20 — CERRADA (2026-09-10)

La autora decide conservar el **indice menor** en las tres copias exactas internas de
dataset7 (`0012`, `0013`, `0046`; se retiran `0021`, `0043`, `0074`). Como el contenido es
identico voxel a voxel, la eleccion no cambia ninguna cifra. `exclusiones.csv` y
`grupos.csv` pasan esas filas de `PROVISIONAL #20` a `decidida`. Con #45 aplicada, **#20
queda cerrada en todas sus partes**: criterio (paciente), representantes y `Grupo paciente`.
**Falta que figure en `01-decisiones.md`** (la entrada del 2026-09-10 aun dice "queda
pendiente"; texto propuesto en el chat).

**Material de revision para la autora (sin implicancia nueva):** mosaicos de S1
regenerados sobre los 65 pacientes vigentes (`outputs/r1_mosaico/`) y plantilla en blanco
`experiments/objetivo2/r1_auditoria_s1_clinico.csv`. Esta **deliberadamente sin los juicios
del agente**, para que la revision no se ancle en ellos; al terminar se compara con
`r1_auditoria_s1_agente.csv` (acuerdo entre revisores).

---

## Ronda 2026-09-11 — revision clinica del nivel de S1 (R1)

### 26 — R1 con REVISOR CLINICO como referencia: 49 de 65 con marco y S1 correctos — sigue ABIERTA solo en lo que no depende de medir

**Procedencia (declararla asi siempre):** `experiments/objetivo2/r1_auditoria_s1_clinico.csv`
lo lleno **un medico cirujano otorrinolaringologo**, revisor clinico externo, segun informo la
autora el 2026-09-11. **No es juicio de la autora**, aunque el nombre del archivo diga
"autora" (mismo riesgo de #37: el nombre no es la procedencia). Revision **ciega** a los
juicios del agente sobre los 4 mosaicos de 65 pacientes. Integrado en `r1_resumen.py`
(`auditoria_S1_clinico`). Normalizacion unica: `otro` con comentario "no hay circulo rojo"
se cuenta como `no hallado` (4 casos); el CSV original no se toco.

**Juicio clinico:** ok 53, un nivel arriba (L5) 6 (`0010`, `0011`, `0014`, `0026`, `0038`,
`0067`), otro sitio 2 (`0046` y `0058`, cruz sobre los ligamentos sacroiliacos
posteriores), no hallado 4.

| Evaluacion, 65 pacientes | referencia clinica | agente |
|---|---|---|
| Marco computable con S1 correcto | **49** | 51 |
| ... y sin ningun punto contaminado | **30** | 32 |
| Con tornillo iliosacro (E8) y S1 correcto | 17 de 17 | 17 de 17 |
| ... con S1 contaminado | 3 | 3 |

**Acuerdo agente frente a clinico:** categoria exacta 92.3%; ok / no-ok 93.8%, **kappa de
Cohen 0.80**. Discrepancias (5): `0003` y `0015` (agente dudoso o error, clinico ok),
`0026` y `0038` (clinico +1), `0046` (clinico otro). **El agente se equivoco en las dos
direcciones.** La cifra citable es la de la referencia clinica.

**Lo que aporta la revision clinica, mas alla de la cifra:**

- **Errores que ningun control automatico detecta:** en `0026` y `0038` los dos detectores
  coinciden (discrepancia 5.8 y -2.3 mm) y los dos estan en L5. La concordancia entre metodos
  **no garantiza** el nivel; la regla candidata de "tomar el z menor" no los habria arreglado.
- **La regla candidata arreglaria 4 de los 6 "+1"** (`0010`, `0011`, `0014`, `0067`: el ala
  da un z entre 18 y 32 mm menor). Sigue siendo hipotesis: se evaluo sobre los mismos casos.
- **El metodo del ala sirve de respaldo:** en `0016` y `0023`, donde el sagital no halla S1,
  el clinico anota que la linea amarilla (ala) **esta bien posicionada**.
- **`0035`:** la cruz esta en S1 pero en su parte **lateral** mas que superior. Apunta a que el
  corte sagital en `x_mid` no siempre es el medio del sacro. Lo marca ok.

**Limites de la referencia (declararlos en la tesis):**

1. **Un solo revisor**, y su especialidad es otorrinolaringologia, no columna ni
   radiologia musculoesqueletica. La identificacion del nivel vertebral es anatomia basica
   de su formacion, pero un tribunal puede preguntarlo. **Mitigacion barata:** que un segundo
   revisor (radiologo o traumatologo) mire solo los 12 no-ok y las 5 discrepancias.
2. **Se reviso el nivel de S1, no las crestas ni las EIPS.** Esos puntos siguen con
   auditoria solo del agente (sin errores vistos en los mosaicos de QC, pero sin revision
   clinica).
3. **"Contaminado"** sigue midiendo estria oscura severa (HU < -200) y metal en la esfera:
   cota optimista de legibilidad.

**Que cambia para `main.tex:115`:** la cifra prometida ya existe con respaldo clinico. **49
de 65 pacientes con metal tienen el marco de Kaiser computable con S1 bien localizado, y 30
lo tienen ademas sin contaminacion**. La perdida se explica mas por el FOV (7) y la
localizacion (12 no-ok) que por el artefacto (19 de 49). La contingencia "computed on
metal-free anatomy only" no parece necesaria para la mayoria. **No aplicado a `main.tex`.**

**Pendiente de la autora:** (1) si la cifra entra en `main.tex` y con que redaccion del
revisor; (2) si el FOV incompleto es criterio de exclusion del Obj 2; (3) si se renombra el
archivo a `r1_auditoria_s1_clinico.csv` para que el nombre no mienta sobre la procedencia;
(4) segundo revisor opcional para los 17 casos senalados.

### 41 — DECISION DE LA AUTORA (2026-09-11): via (c), con (a) como contingencia — ABIERTA hasta registrarla y aplicarla

La autora decide avanzar por la **via (c)**: geometrias parametricas con dimensiones
publicadas. No descarta la **via (a)** (extraer implantes de CLINIC-metal) si la busqueda de
papers no da las dimensiones necesarias. **No aplicado** a `main.tex`, `00-tesis.md` ni
`01-decisiones.md`; texto propuesto en el chat.

**Contrastado contra el texto actual de `main.tex` (2026-09-11), la via (c) cambia poco:**

- **RQ (l. 60), hipotesis (l. 66), Objetivos 1-4, SAP, C2, C3 y el protocolo de Peters: sin
  cambios.** Hablan de "rigid implant geometries" sin fijar su origen.
- **C1 (l. 54)** dice *"Non-biological rigid implant geometries (compensating for
  thresholding over-coverage bias)"*. Una geometria parametrica **es** una geometria rigida
  no derivada de umbral: (c) encaja con C1 **tal como esta escrita**, mejor que (a).
- **Regla de aislamiento (l. 111):** con un banco sintetico se cumple por construccion;
  basta una frase que diga de donde sale el banco.
- **Lo que falta de verdad:** `main.tex` **no dice en ningun sitio de donde salen las
  geometrias**. Hay que anadir un parrafo de metodo (fuente de dimensiones, nivel de detalle
  del modelo, simplificaciones) y una limitacion.
- **`00-tesis.md:114`** ("geometria CAD propia") pasa a "geometria parametrica propia".
- **#31** queda utilizable: `d_implante` pasa a ser un parametro conocido.

**La contingencia (a) cambiaria MUCHO mas que (c):**

- La regla de l. 111 pasa a ser **vinculante**: hay que repartir pacientes entre banco y
  evaluacion (65 con osteosintesis, >= 17 con tornillo iliosacro), y la cohorte de prueba
  se reduce.
- **C1 se contradiria:** reclama compensar el sesgo del umbral mientras extrae geometria por
  umbral. Habria que reescribirla.
- Hay que declarar lo que E8 midio: fragmentacion (9 de 57), fuste bajo el calibre publicado
  (49 de 57 < 6.0 mm) y dependencia de la adquisicion (`0065`/`0066`).

**Criterio de disparo de la contingencia, a precisar por la autora.** Las dimensiones
basicas **ya tienen evidencia textual**: calibres 6.0-8.0 mm (#31) y longitudes S1/S2
(`zhao2012`, #30). Lo que puede no aparecer son los detalles (paso de rosca, canulacion,
cabeza o arandela). **Para eso (a) no sirve de rescate:** E8 no recupero ni el diametro
exterior de forma consistente, asi que es improbable que resuelva detalles mas finos. La
contingencia natural ante esa falta es **cilindro liso declarado como simplificacion**, no
(a). (a) solo tendria sentido si faltaran incluso calibres y longitudes, que no es el caso.

### 47 — La justificacion de C1 cita una fuente NO leida, y E8 no confirma su direccion — ABIERTA

- **Hallazgo:** C1 (`main.tex:54`) se justifica con *"compensating for thresholding
  over-coverage bias, \citealp{xie2024implantsegmentation}"*. **`xie2024implantsegmentation`
  no tiene ficha en `docs/literatura/`**: en `_index.md` figura sin verificar, y `ESTADO.md`
  la lista entre las que faltan. La afirmacion de que el umbral **sobrecubre** el implante no
  tiene evidencia textual extraida (reglas 1 y 2).
- **Tension con E8:** en los tornillos de CLINIC-metal, el umbral de 2500 HU esta cerca del
  semimaximo local (mediana 2818 HU) y el efecto dominante es **fragmentacion y fuste bajo el
  calibre publicado**, no sobrecobertura (`d_ext_2500 - d_ext_semimax` con mediana +0.24 mm).
  La direccion del sesgo **depende del implante y del umbral**. No refuta a Xie, que puede
  medir otro material, otro umbral u otra anatomia, pero impide escribir "over-coverage"
  como hecho general sin leerlo.
- **Que seccion toca:** C1 (redaccion de su justificacion). Con la via (c) la contribucion se
  sostiene igual; lo que cambia es **por que** se prefiere geometria rigida: porque el umbral
  deforma (hacia arriba o hacia abajo segun el caso), no porque siempre sobrecubra.
- **Salida:** leer `xie2024implantsegmentation` con `lector-papers` (el PDF figura en
  `_index.md`) antes de fijar la redaccion de C1.
- **Tipo:** REDACCION / RIESGO. **Pendiente de la autora. No aplicado.**

### 41 — APLICADA a `01-decisiones.md` y `main.tex` (2026-09-11). CONTINGENCIA (a) ABIERTA

Orden explicita de la autora. **Decision registrada** en `01-decisiones.md`: geometrias
parametricas.

**Cambios en `main.tex` (compila: 4 paginas, 0 citas indefinidas):**

1. **Objetivo 2:** "3D pose **of a parametric rigid screw model** constrained by...".
2. **Regla de aislamiento (Datasets):** la frase sobre el banco pasa a *"The implant
   geometries consumed by the proposed sampler and by the physical simulation arm are
   parametric and are not derived from any evaluation volume."*
3. **Parrafo nuevo `Implant geometry source`:**
   - calibre de 6.5-8.0 mm (`gardner2010safezones`) y de 6.3-8 mm (`kaiser2014dysmorphism`),
     las dos ya en `refs.bib`;
   - longitud acotada en cada volumen por el corredor medido con la regla de longitud util de
     Kaiser (sin rango publicado fijo);
   - rosca, canulacion, cabeza y arandela simplificadas a cilindro liso, declarado como
     limitacion;
   - implantes reales de CLINIC-metal fuera del banco, usados como contraste de poses,
     referencia de apariencia y control test-retest;
   - motivacion por la auditoria local (fragmentacion, fuste bajo el calibre publicado,
     cambio entre adquisiciones), **sin cifras**.

**No se toco:** C1 (su justificacion depende de #47, lectura de `xie2024` en curso) ni
`00-tesis.md:114` ("geometria CAD propia"), que pide orden aparte (regla 14).

**Bibliografia disponible y no citable hoy:** `grass2016`, `lee2014`, `wagner2017` y
`zhao2012` tienen archivo en `refs/raw/` y ficha leida, pero **no estan en `refs.bib`**. Por
eso la longitud no se cita de `zhao2012` y el calibre de 7.3 mm de `grass2016` no aparece.
Anadirlas a `refs.bib` es decision de la autora (regla 9).

**CONTINGENCIA ABIERTA (decision de la autora, 2026-09-11):** si a futuro faltara **por
completo** bibliografia con calibres y longitudes utilizables, se reconsidera la **via (a)**:
extraer geometrias de los implantes reales de CLINIC-metal. Si se activa:

- la regla de aislamiento pasa a ser vinculante a nivel de paciente (`Grupo paciente` ya
  existe);
- C1 debe reescribirse;
- hay que declarar las limitaciones de E8 (#46);
- el parrafo `Implant geometry source` de `main.tex` se sustituye.

**La falta de detalles finos (rosca, canulacion, cabeza) NO la dispara.** Hoy la
contingencia **no aplica**: hay calibres en dos fuentes citadas y la longitud sale del
corredor.

### 47 — LECTURA HECHA (2026-09-11): la cita de C1 esta PARCIALMENTE respaldada — sigue ABIERTA solo la redaccion

`xie2024implantsegmentation` leido entero con `lector-papers`; ficha en
`docs/literatura/xie2024implantsegmentation.md` (31 `NO ENCONTRADO EN EL PDF`). Queda en
**N2, con el rol corregido**: no es insumo de ISC, sino fuente del fallo del umbral fijo.
Filas de `_index.md` y `_candidatos.md` integradas por la sesion principal.

- **Lo que SI respalda:** el umbral fijo sobrecubrio el metal **en cortes 2D simulados**.
  *"the segmentation outcomes completely contain the ground truth"* (Resultados, p. 6). A
  2500 y 3000 HU, SE 100% con DSC 82.92% y 84.19% (Tabla 2, p. 11). La palabra
  "over-coverage" no aparece en el texto.
- **Lo que NO respalda:**
  - **Generalidad:** la propia Discusion dice que la direccion depende del umbral
    (*"larger thresholds may misidentify metal implants as tissue"*, p. 10).
  - **Contexto:** no mide tornillos pelvicos ni tamanos en mm; en titanio la comparacion es
    solo visual y en CT clinica no hay referencia.
  - **Relacion con C1:** su remedio es una red de segmentacion, no geometria rigida. Que la
    geometria rigida "compense" el sesgo es inferencia de la tesis.
- **Coherencia con E8:** Xie documenta sobrecobertura en su simulador; E8 documenta
  fragmentacion y fuste fino en tornillos reales a 2500 HU. **Las dos cosas son compatibles**
  con "el umbral deforma el tamano en una direccion que depende del umbral y del caso". Xie
  atribuye la fragmentacion del caso de CLINIC-metal a las CNN, no al umbral (p. 6).
- **Discrepancia interna de Xie:** 95.81% y 85.33% en contribuciones (p. 2) frente a 97.89% y
  95.45% en abstract, Tabla 1 y conclusiones. **No citar esas cifras.**
- **Redaccion propuesta para C1 (NO aplicada; `main.tex:54`):** sustituir *"(compensating
  for thresholding over-coverage bias, \citealp{xie2024implantsegmentation})"* por *"which
  avoid the threshold-dependent size distortion of fixed-HU metal segmentation (over-coverage
  in simulated slices, \citealp{xie2024implantsegmentation}; fragmentation of pelvic screws in
  the local audit)"*. Cada tramo tiene respaldo: p. 6 y Tabla 2 (sobrecobertura simulada),
  p. 10 (dependencia del umbral), E8 (#46).
- **Snowballing con prioridad:** `Yu 2020, Deep sinogram completion` es el simulador con el
  que Xie fabrica su ground truth. Si la sobrecobertura depende de ese simulador, no se
  traslada a CT clinica. Anotado PENDIENTE en `_candidatos.md`.
- **Pendiente de la autora:** aprobar o ajustar la redaccion de C1.

### 41 — Complemento (2026-09-11): bibliografia y alcance alineados

Por orden de la autora:

- **`refs.bib` 36 -> 40:** `grass2016`, `lee2014`, `wagner2017` y `zhao2012` entran por el
  flujo raw -> clean -> build (MAPEO actualizado). Dos avisos de clave:
  - `grass2016`: el primer autor es **Gras**, con una s.
  - `lee2014`: el ano del fasciculo es **2015**; 2014 es la fecha electronica.

  Se mantienen las claves (regla 1). Entran por `\nocite{*}`: `main.tex` todavia no las
  cita en el cuerpo. Quedan disponibles para el calibre de 7.3 mm (`grass2016`) y las
  longitudes de `zhao2012` si la autora quiere reforzar el parrafo `Implant geometry source`.
- **`00-tesis.md:114`:** "geometria CAD propia" pasa a "geometria parametrica propia de
  implante".
- **Tesis:** compila con 40 referencias, 4 paginas, 0 citas indefinidas y los 2 avisos de
  BibTeX ya documentados (Hinsche, Templeman).

### 47 — CERRADA (2026-09-11): nueva redaccion de C1 APLICADA

Por orden explicita de la autora, `main.tex:54` pasa de *"(compensating for thresholding
over-coverage bias, \citealp{xie2024implantsegmentation})"* a *"which avoid the
threshold-dependent size distortion of fixed-HU metal segmentation (over-coverage in simulated
slices, \citealp{xie2024implantsegmentation}; fragmentation of pelvic screws in the local
audit)"*. Respaldo de cada tramo:

- Xie, p. 6 y Tabla 2 (sobrecobertura en cortes simulados);
- Xie, p. 10 (la direccion del error depende del umbral);
- E8, #46 (fragmentacion en tornillos pelvicos).

Compila: 4 paginas, 0 citas indefinidas. **#47 CERRADA.** Queda PENDIENTE en
`_candidatos.md` el simulador de Xie (Yu 2020): solo haria falta si se quisiera trasladar la
sobrecobertura simulada a CT clinica, cosa que la nueva redaccion ya no afirma.

### 36 y 39 — Deben decidirse JUNTAS: la cuarta ventana no cabe en el VAE que sugiere `main.tex` (2026-09-11) — ABIERTA

- **Hallazgo:** el Objetivo 3 de `main.tex` dice *"Stable Diffusion 1.5 backbone"*. Eso
  apunta al autoencoder de SD 1.5 como el VAE que #36 da por no especificado. Es una
  inferencia, **no una decision escrita**. Ese autoencoder recibe imagenes de **3 canales**.
- **Choque con E6c (#39):** la unica salida que domina en las dos ROI es `pub+MTW`, las tres
  ventanas publicadas **mas una cuarta ventana de metal**. Cuatro canales no entran en un VAE
  de tres sin modificarlo. `pub+asinh` (tres canales, con compresion no lineal en la ventana
  ancha) si cabe, pero E6c la deja por detras de `pub+MTW` a 8 bits en hueso (2.07 frente a
  1.31 HU) y en metal (32.02 frente a 17.72 HU).
- **Consecuencia:** decidir #39 sin #36 es decidir a ciegas. Las combinaciones posibles son
  cuatro, ninguna adoptada:
  1. SD 1.5 con tres ventanas y `asinh`;
  2. SD 1.5 con primera capa del encoder adaptada a cuatro canales (reentrenamiento parcial);
  3. otro VAE de cuatro canales;
  4. metal compuesto fuera del espacio latente.
- **Ejecucion:** E6b (`HU -> ventanas -> VAE -> HU`) no corre en la maquina local (torch solo
  CPU, sin `diffusers`, RAM justa). Es candidato natural para Khipu cuando se fije la
  combinacion.
- **Que seccion toca:** Objetivo 1 (Go/No-Go), Objetivo 3 (backbone), C3, `03-glosario.md`.
- **Tipo:** DISENO / RIESGO. **Pendiente de la autora. No aplicado.**

---

## Ronda 2026-09-11 (tarde) — #31 y #22 decididas, R1 en `main.tex`, E9 bloqueado por segmentacion

### 31 — APLICADA (decision de la autora, 2026-09-11)

`Dmax >= d_implante + 2c`, con `c` = 1-2 mm radiales por lado, la "holgura de Kaiser"
**operacionalizada** a partir de su frase (que no publica la cuenta). Registrada en
`01-decisiones.md`; aplicada a `00-tesis.md` y `03-glosario.md`.

- **No aplicada a `main.tex`**: el Objetivo 2 y `Problem Statement` siguen hablando del
  criterio de 10 mm como convencion.
- **Texto propuesto para el Objetivo 2**, a continuacion de "osseous-corridor viability":
  *"expressed as $D_{\max} \ge d_{\text{implant}} + 2c$, with $d_{\text{implant}}$ the
  calibre of the parametric screw and a radial clearance $c$ of 1--2~mm derived from the
  clearance \citet{kaiser2014dysmorphism} describe around a 6.3--8~mm screw"*.

### 22 — DECIDIDA (2026-09-11)

- **2500 HU:** solo cribado.
- **Metal integrity:** con la regla adaptativa por ROI de Peters.
- **Propuesta abierta:** semimaximo local para mascaras de implantes reales (E8).

Registrada en `01-decisiones.md`, `00-tesis.md` y `03-glosario.md`.

### 26 — Cifra de R1 ESCRITA en `main.tex` (2026-09-11)

Por orden de la autora, el parrafo `Field limitation` sustituye la promesa ("will be
quantified...") por el resultado: 57/65 con los cinco landmarks en FOV; 49 con marco
computable y S1 confirmado por el revisor clinico (una sola persona, otorrinolaringologia,
ciega a la auditoria automatica); 30 sin contaminacion. Declara que la perdida la explican
mas el FOV (7) y la localizacion que el artefacto, que los 17 con tornillo iliosacro tienen
S1 correcto y 3 contaminados, que el tratamiento de los FOV cortados se evalua aparte, y que
crestas y EIPS no tienen revision clinica. Compila: 4 paginas, 0 citas indefinidas.

### 48 — El corredor oseo NO se puede medir con un umbral HU: el esponjoso sacro cae bajo 150 HU en ~40% de los pacientes — ABIERTA

- **Origen:** piloto de E9 (`experiments/objetivo2/e9_corredor.py`), 2026-09-11.
- **Hallazgo 1, el piloto:** en 6 volumenes el cilindro transsacro maximo salio de **1.6 a
  7.8 mm**, incluido `metal_0008`, que **tiene tornillos transsacros reales de ~7 mm en S1**.
  Imposible. A lo largo del tornillo S1 de `metal_0008`, el ala sacra mide **HU 0-100**, bajo
  el umbral de 150, en tramos de 13 a 33 mm. Ni el cierre morfologico de 2 mm ni el relleno 3D
  de cavidades lo arreglan: la cortical a 150 HU no forma una envolvente cerrada. Antes se
  corrigieron dos fallos del propio metodo (un foramen sacro tomado como salida; tramos que no
  llegaban al ilion). **E9 queda marcado NO VALIDO en su codigo y no se corrio sobre la
  cohorte.**
- **Hallazgo 2, E9b** (`e9b_densidad_s1.py`, `e9b_densidad_s1.md`; mediana HU en esferas de
  6 mm en el cuerpo de S1 y en las alas a 25 mm del plano medio, 12 mm bajo el platillo):

| Cohorte | n | alguna esfera con mediana < 150 HU |
|---|---|---|
| Con metal, S1 confirmado por el clinico (**con** los 7) | 53 | 20 (38%) |
| Con metal, **sin** los 7 de FOV cortado | 49 | 18 (37%) |
| Sin metal (calibracion; S1 no auditado) | 60 | **26 (43%)** |

  El cuerpo de S1 queda sobre 150 HU casi siempre (0 de 53; 5 de 60). **Las alas no:** 12-24
  esferas bajo 150 por lado y cohorte.
- **Lectura:** es una propiedad del **hueso de estos pacientes**, no del artefacto. La cohorte
  sin metal esta igual o peor. Cualquier medida basada en "HU > 150" subestima el hueso en el
  ala sacra de cerca de 4 de cada 10 pacientes. Eso afecta a E9 y tambien a **bone integrity**
  de Peters (Dice sobre voxeles > 150 HU): en un ala de HU 0-100, el hueso no entra en la
  metrica.
- **Limitacion de la sonda:** las esferas del ala estan a una distancia fija del plano medio y
  pueden incluir parte del foramen de S1. El piloto de `metal_0008` (HU 0-100 a lo largo de un
  tornillo real) confirma el fenomeno sin esa ambiguedad.
- **Consecuencias:**
  1. **E9 necesita una segmentacion osea rellena** (interior de la envolvente cortical). Es
     exactamente lo que #29 recomendaba evaluar con TotalSegmentator (`sacrum`,
     `vertebrae_S1`, `hip_left/right`). No es ejecutable en la maquina local (CPU, poca RAM):
     es candidato a **Khipu**. Alternativas: segmentacion cortical propia (contornos, estilo
     McLaren) o semi-manual en un subconjunto.
  2. **#29 sube de prioridad:** pasa de "inicializacion util" a **bloqueo del Objetivo 2**.
  3. **Bone integrity (Peters, #14)** usa un umbral que no representa el esponjoso sacro de
     esta cohorte. Hay que declararlo o adaptarlo al trasladar el protocolo (#17).
- **Los 7 de FOV cortado (pedido de la autora: con y sin):**
  - **Densidad:** con y sin ellos sale casi lo mismo (38% frente a 37%), asi que excluirlos no
    cambia este resultado.
  - **Los 7 en si:** 3 no tienen S1 localizable. Los otros 4 tienen S1 correcto, pero sin
    crestas no se puede expresar el angulo coronal en el marco de Kaiser.
  - **Cambio neto:** 53 frente a 49 pacientes con S1 confirmado.
  - **El experimento que realmente decide** (corredor y angulos con y sin ellos) queda
    **bloqueado por el punto 1**. `e9_corredor.py` ya trae la comparacion prevista: angulos en
    el marco de Kaiser solo con crestas, y diametros en el marco nativo para todos.
- **Que seccion toca:** Objetivo 2 (medicion del corredor), #29, #31 (la restriccion necesita
  un `Dmax` valido), #14 y #17 (bone integrity), `main.tex` (metodo del muestreador).
- **Tipo:** RIESGO / BLOQUEO. **Pendiente de la autora:** via de segmentacion (TotalSegmentator
  en Khipu, segmentacion cortical propia o semi-manual) y como declarar bone integrity.

### 49 — TotalSegmentator: la version y el modelo de recorte son parte del metodo, y existe `total_v3` sin evaluar — ABIERTA

- **Origen:** preparacion de los comandos para correr TotalSegmentator en Khipu (#48 punto 1),
  2026-09-12, contra PyPI y el codigo fuente de la rama `master` del repositorio oficial. No es
  una lectura del paper.
- **Hallazgo 1, version:** PyPI da `2.18.0` (subida el 2026-08-12). #29 pide "version fijada";
  hasta hoy no habia numero. Sin fijarla, un `pip install` posterior cambia el modelo sin aviso.
- **Hallazgo 2, `total_v3`:** `totalseg_download_weights.py` lista una tarea `total_v3`
  (ids `831-835, 837`) ademas de `total` (`291-295, 298`). #29 se escribio sobre `total`. No se
  verifico si `total_v3` trae `sacrum`, `vertebrae_S1`, `hip_left`, `hip_right`, ni que cambia.
- **Hallazgo 3, recorte:** con `--roi_subset`, el codigo corre primero un modelo de recorte de
  **6 mm** (`crop_model_task = 298`), o de 3 mm (`297`) con `--robust_crop`. Frase del codigo:
  "use the more robust 3mm model instead of the default and faster 6mm model". En volumenes con
  streaking, un recorte grueso que falle deja fuera parte de la pelvis antes del modelo de 1.5 mm.
  `-t total` descarga el 298, pero no el 297 (este viene en `total_fast`).
- **Operativo (no toca la tesis, se anota para no repetirlo):** segun la documentacion de Khipu,
  solo el nodo `ds001` (particion `data-science`) tiene internet. Los pesos se bajan en el nodo de
  acceso antes de lanzar el job.
- **Que seccion toca:** #29 (validacion minima y version fijada), #48 (via de segmentacion), y el
  metodo del muestreador en `main.tex` si se adopta (version, tarea y modelo de recorte declarados).
- **Tipo:** SUPUESTO / REPRODUCIBILIDAD. **Pendiente de la autora:** `total` o `total_v3`, y recorte
  por defecto (6 mm) o `--robust_crop` (3 mm). Recomendacion: `total` 2.18.0 con `--robust_crop`
  en el piloto, y guardar la version en el log del job. **No aplicado.**
- **Actualizacion 2026-09-12, piloto ejecutado** (job 51300, Khipu ag001, MIG A100 `3g.20gb`,
  torch 2.14.0+cu130; `metal_0008` y `CLINIC_0002`, cada uno con 3 mm y 6 mm; QC con
  `experiments/objetivo2/ts_piloto_qc.py`, tablas `ts_piloto_qc*.csv`):
  - **Sin truncamiento visible:** ninguna de las 16 mascaras toca el borde del FOV, y las cajas
    de cada estructura difieren <= 1.6 mm entre recortes. 59-76 s por corrida.
  - **Pero el recorte cambia la mascara final:** Dice 3 mm vs 6 mm de **0.930** (`sacrum`,
    `metal_0008`) a 0.972 (`hip_right`, `CLINIC_0002`); 2.6-7.4% de voxeles exclusivos por
    estructura. En las laminas se concentran en bordes, **articulacion sacroiliaca y ala**, justo
    la region del corredor (un corte coronal de `metal_0008`: 1200 voxeles solo en 3 mm, 627 solo
    en 6 mm). A lo largo del tornillo `comp 1` de `metal_0008`, el eje queda fuera de toda
    mascara en **17.5% (3 mm) frente a 5.8% (6 mm)**.
  - **Lectura:** el modelo de recorte no es solo un riesgo de truncamiento: cambia el encuadre de
    entrada del modelo de 1.5 mm y, con eso, la etiqueta en la zona que mide E9. Esa diferencia
    es una cota de reproducibilidad de cualquier `Dmax` medido sobre TS. Causa no verificada.
    Con 2 casos no hay base para preferir 3 mm por robustez.
  - **Metal:** 95-98% de los voxeles > 2500 HU del cilindro de 4 mm de cada tornillo quedan
    dentro de alguna mascara (TS etiqueta el tornillo existente como hueso).
  - **Pendiente de la autora (ampliado):** elegir recorte y declararlo, o medir `Dmax` con ambos y
    reportar la diferencia como incertidumbre del metodo.
- **Actualizacion 2026-09-13: cohorte ejecutada; la repetibilidad NO es exacta.** Job 51315,
  ag001, el mismo `--gres=shard:a100_3g.20gb:1` que el piloto, TS 2.18.0, torch 2.14.0+cu130.
  179 volumenes x 2 recortes, 358/358 `ok`. Resumen en `experiments/objetivo2/ts_cohorte.md`.
  - **Hallazgo:** se re-segmentaron los 2 casos del piloto con el mismo nodo, tipo de GPU,
    version, clases y recorte (`repetibilidad_piloto_51315.txt`). Resultado: 14 de 16 mascaras
    identicas. Las otras 2 son de `metal_0008`, default6mm: `sacrum` con **16 voxeles** distintos
    (Dice 0.99998) y `hip_left` con **8** (Dice 0.99999). El resto del QC del piloto se
    reproduce exacto, incluidas esferas y tornillos.
  - **Lectura:** en esta configuracion TS no es determinista bit a bit, asi que "misma
    configuracion = misma mascara" no se puede declarar. La magnitud es varios ordenes menor que
    el efecto del recorte (Dice 0.930-0.972) y no compite con el. Solo aparecio con 6 mm y en el
    caso con metal, pero con n = 2 eso no es un patron. **Causa no verificada.**
  - **Que seccion toca:** la declaracion de reproducibilidad del metodo del muestreador en
    `main.tex`, si se adopta TS (#48).
  - **Opciones:** (a) declarar la cota observada (<= 16 voxeles por mascara en 2 casos);
    (b) medir la repetibilidad en mas casos antes de declararla; (c) comprobar si TS/torch
    admiten un modo determinista (no verificado). **Pendiente de la autora. No aplicado.**

### 50 — E9b: un error de nivel de S1 produce "ala < 150 HU" midiendo tejido blando; el brazo sin metal de #48 (43%) no respalda que sea "propiedad del hueso" — ABIERTA

- **Origen:** QC del piloto de TotalSegmentator (`experiments/objetivo2/ts_piloto_qc.py`,
  `ts_piloto_qc_esferas.csv`, laminas en `outputs/ts_piloto_qc/`), 2026-09-12.
- **Hallazgo 1, `CLINIC_0002`** (calibracion, S1 de R1 **sin auditar**, `s1_discordante = True`):
  - las tres esferas de E9b quedan **100% fuera** de `sacrum`, `vertebrae_S1` y caderas, con
    ambos recortes;
  - alas con mediana **17 y 34 HU**, identicas a `e9b_densidad_s1.csv` (control de marco ok):
    rango de tejido blando, no de esponjoso;
  - el techo de `vertebrae_S1` de TS en la linea media queda **24.6 mm** (3 mm) / 23.8 mm (6 mm)
    **bajo** el platillo de R1, cerca de un nivel vertebral. En la lamina sagital la esfera del
    cuerpo cae en la vertebra inmediatamente craneal a la S1 de TS.
  - R1 o TS se equivoca de nivel; sin auditoria no se decide cual. En cualquier caso, las alas
    medidas no son hueso.
- **Contraste, `metal_0008`** (S1 `ok` por el revisor clinico): esferas dentro de sacro/S1 en
  100%, 92-93% y 70-71%; HU 319/270/442; techo de S1 de TS 6.2 mm sobre el platillo de R1.
- **Hallazgo 2, cohorte** (cruce de `e9b_densidad_s1.csv` con `r1_estados.csv`):

| Grupo | n | alguna ala < 150 HU |
|---|---|---|
| Evaluacion, S1 `+1` segun el clinico | 6 | **6** |
| Evaluacion, S1 `ok` segun el clinico | 53 | 20 |
| Calibracion (sin auditar), `s1_discordante` | 24 | 8 |
| Calibracion (sin auditar), no discordante | 36 | 18 |

- **Lectura:** un S1 un nivel arriba pone las esferas del ala junto al cuerpo lumbar, en tejido
  blando, y produce "ala < 150 HU" de forma mecanica (6 de 6 en los `+1` auditados). El 43%
  del brazo sin metal de #48 incluye un numero **desconocido** de esferas fuera de hueso, asi
  que la frase de #48 "es una propiedad del hueso de estos pacientes ... La cohorte sin metal
  esta igual o peor" pierde su control. Los 20 de 53 con S1 `ok` tampoco estan verificados como
  hueso (foramen o fuera del ala; limitacion ya declarada en #48).
- **Lo que NO cambia:** el Hallazgo 1 de #48 (HU 0-100 a lo largo del tornillo de `metal_0008`)
  se midio sobre el eje del tornillo, no con esferas; E9 sigue NO VALIDO y la necesidad de una
  segmentacion rellena se mantiene.
- **Que seccion toca:** #48 (tabla y lectura de E9b), #14/#17 (bone integrity, si se cita el
  43%), #26 (S1 de calibracion no auditado), `e9b_densidad_s1.md`.
- **Opciones:** (a) auditar S1 de la calibracion (`r1_mosaico.py --cohorte calibracion`);
  (b) tras correr TS en la cohorte, usar `vertebrae_S1` de TS como segundo detector de nivel y
  medir densidad solo dentro de la mascara del ala; (c) retirar el brazo sin metal de la lectura
  de #48 hasta auditar.
- **Tipo:** RIESGO / SUPUESTO. **Pendiente de la autora. No aplicado.**

## Ronda 2026-09-13 — analisis de la cohorte de TotalSegmentator (PENDIENTE 1, pasos 2 y 3)

- **Origen:** `experiments/objetivo2/ts_analisis.py`, que genera `ts_analisis.md` y `ts_nivel_s1.csv`
  (versionados) a partir de la QC del job 51316. Cuenta 168 volumenes = 168 pacientes, sin los 11
  de `exclusiones.csv`.
- **Procedencia de las laminas:** las revisaron agentes, no la autora ni el clinico, a 80 dpi. Casos
  revisados: `CLINIC_0002`, `0022`, `0043`; `metal_0010`, `0012`, `0015`, `0017`, `0024` (tornillos),
  `0026`, `0030`, `0053`, `0058`. **No** es la revision completa de las 197 laminas.

### 50 — Opcion (b) EJECUTADA: TS como segundo detector de nivel. La tabla rehecha deja el "~40%" de #48 en 8-17% — sigue ABIERTA

- **Detector:** `dz` = techo de `vertebrae_S1` de TS en la columna media del platillo de R1, menos el
  platillo. Estado `R1 arriba de TS` si `dz < -10 mm` con los dos recortes.
- **Hallazgo 1, concordancia con el clinico: 56 de 57** casos `ok`/`+1` con techo.
  - Los 5 `+1` dan `dz` de -34.3 a -32.0 mm.
  - De los `ok`, 51 dan +3.7 a +15.7 mm y 1 da -24.3 mm (`metal_0012`, ver #51).
  - El estado no cambia con el recorte en ningun caso: `dz` difiere <= 1.6 mm entre recortes.
  - **Circularidad declarada:** el umbral de -10 mm se fijo mirando esta misma distribucion. La
    concordancia sale igual con cualquier umbral mayor que -24.3 mm y de hasta +3.7 mm. La
    referencia es un solo revisor.
- **Hallazgo 2, casos sin auditar:**
  - Calibracion: `R1 arriba de TS` en **7 de 60** (6 de 24 con `s1_discordante`, 1 de 36 sin el).
  - `otro` (grupo 2): 11 de 31.
  - `CLINIC_0002`: `dz` = -24.6 / -23.8 mm. En la lamina sagital, la esfera del cuerpo esta en la
    vertebra craneal a la S1 de TS, con un disco entre ambas. Lectura del agente: R1 en L5, salvo
    transicion lumbosacra, que la lamina no permite evaluar. Responde la pregunta de #50.
- **Hallazgo 3, tabla de #50 rehecha** (recorte 3 mm; con 6 mm cambia poco):

| Grupo | n | alguna esfera < 150 HU (E9b) | ala < 150 con esfera >= 90% en `sacrum`/S1 | ala < 150 con esfera > 50% fuera de mascaras |
|---|---|---|---|---|
| Evaluacion, clinico `ok` | 53 | 20 (38%) | 4 (8%) | 16 (30%) |
| ... con TS concordante | 51 | 18 (35%) | 4 (8%) | 14 (27%) |
| Evaluacion, clinico `+1` | 6 | 6 | 0 | 6 |
| Calibracion (sin auditar) | 60 | 26 (43%) | 9 (15%) | 16 (27%) |
| ... con TS concordante | 53 | 19 (36%) | 9 (17%) | 9 (17%) |
| ... con `R1 arriba de TS` | 7 | 7 | 0 | 7 |

  En los 25 casos `R1 arriba de TS` (todas las cohortes), las 75 esferas quedan 100% fuera de las
  cuatro mascaras.
- **Hallazgo 4, geometria de la sonda.** Casos concordantes con ala < 150 HU y esfera mayormente fuera
  (`metal_0017`, `metal_0030`, `CLINIC_0043`): en las laminas, la esfera del ala queda anterolateral
  al cuerpo de S1, sobre el borde del contorno y en tejido blando presacro. El ala osea esta detras.
  Cae ahi porque la esfera se pone a 25 mm lateral **a la altura del centro del platillo**, no porque
  TS deje hueso fuera. Algunas medianas son negativas (`metal_0003` -161 HU, `CLINIC_0033` -54 HU).
  **No se descarta** que TS excluya esponjoso muy hipodenso: con 3 laminas a 80 dpi no se puede
  afirmar.
- **Lectura:**
  - El "38% / 43% con alguna esfera < 150 HU" de #48 lo dominan esferas fuera del hueso, por error de
    nivel o por la geometria de la sonda.
  - Con esfera >= 90% dentro de `sacrum`/S1 quedan **4 de 53 (8%) con metal** y **9 de 60 (15%;
    17% entre concordantes) sin metal**. Ejemplo: `CLINIC_0012`, ala izquierda, mediana 0 HU con
    99.8% de la esfera dentro.
  - El fenomeno existe, pero en un orden de magnitud menor. Que el brazo sin metal quede por encima
    ya no se explica por error de nivel; con n pequenos y cohortes no emparejadas no es un contraste.
- **Aparte:** `techo_linea_media_dz_mm` de `sacrum` **no** sirve como detector de nivel.
  - De los 16 casos con S1 en R1 y sin techo de sacro, 12 son casos con R1 un nivel arriba: la columna
    cae sobre L5, anterior al sacro.
  - Quedan 4 sin explicar (`CLINIC_0045`, `CLINIC_0066`, `metal_0007`, `metal_0054`; 5 filas). No
    se usa.
- **Que seccion toca:** #48 (tabla y lectura), `e9b_densidad_s1.md`, #14/#17 (bone integrity), y el
  texto propuesto de ESTADO sobre bone integrity (pendiente 3, no aplicado).
- **Opciones:**
  - (a) sustituir la cifra de #48 por la del criterio en mascara (8% / 15%), con la sonda declarada;
  - (b) retirar E9b como evidencia de densidad y medir HU directamente dentro de `sacrum` +
    `vertebrae_S1` en el E9 rehecho (hacen falta las mascaras de Khipu);
  - (c) auditar igualmente la S1 de calibracion, porque TS no es referencia clinica.
- **Pendiente de la autora. No aplicado.**

### 48 — ACTUALIZACION 2026-09-13: la cifra "~40%" no sobrevive al control de mascara; el fenomeno y la necesidad de TS, si

- **Sigue en pie:**
  - el Hallazgo 1 de #48 (HU 0-100 a lo largo del tornillo real de `metal_0008`);
  - 4 pacientes con metal y 9 sin metal con esfera de ala dentro de TS y mediana < 150 HU (#50).
- **Dentro de las mascaras** (`ts_analisis.md`, seccion 5), mediana de la fraccion <= 150 HU:

  | Mascara | grupo 1 | grupo 2 | grupo 3 |
  |---|---|---|---|
  | `sacrum` | 0.32 | 0.38 | 0.43 |
  | `vertebrae_S1` | 0.10 | 0.11 | 0.13 |

  - Incluye el borde (volumen parcial) y los segmentos sacros distales: no es especifico del ala.
  - Lo que si dice: una mascara "HU > 150" perderia un tercio o mas del `sacrum` en cualquier grupo,
    y la de TS lo contiene por construccion.
  - Grupos no emparejados; en grupo 1 entran voxeles de metal y estriacion.
- **Para la adopcion de TS:**
  - En las laminas revisadas no aparecio ningun fallo de segmentacion osea bajo metal.
  - Metal de E8 dentro de alguna mascara: mediana 98% (recorte 6 mm) / 98% (3 mm), minimo 68-70%.
  - Eje del tornillo fuera de toda mascara: mediana 5-6%, maximo **35%** en `metal_0024` comp 3. En
    su lamina, el tramo sin mascara es la articulacion sacroiliaca con estriacion, donde `hip_right`
    no sigue al ilion junto al tornillo. Es exactamente el tramo de salida del corredor de E9.
- **Pendiente de la autora:** adoptar TS, y que cifra queda en #48 (ver opciones de #50).

### 49 — ACTUALIZACION 2026-09-13 (analisis): el recorte cambia ~5% de cada mascara en toda la cohorte, y en 10 casos la caja se desplaza 14-98 mm

- **Dice 3 mm frente a 6 mm** (168 pacientes; mediana, con osteosintesis / sin osteosintesis):

  | Estructura | con osteosintesis | sin osteosintesis |
  |---|---|---|
  | `sacrum` | 0.940 | 0.950 |
  | `vertebrae_S1` | 0.946 | 0.952 |
  | caderas | 0.956-0.957 | 0.963-0.966 |

  - Percentil 5: 0.918-0.949. Minimo: **0.848** (`CLINIC_0022`, `vertebrae_S1`).
  - Voxeles exclusivos de un recorte: 3.4-5.9% de mediana.
  - Con osteosintesis el Dice baja ~0.01 en las cuatro estructuras.
  - Confirma el piloto a escala de cohorte.
- **Nuevo:** en 10 casos la caja de alguna estructura cambia **13.6-98.3 mm** entre recortes (11
  estructuras). La afirmacion del piloto (<= 1.6 mm) no generaliza.
  - Tres son del corredor: `CLINIC_0022` `sacrum` 78 mm, `CLINIC_0029` S1 16 mm y `CLINIC_0032` S1
    14 mm.
  - En la lamina de `CLINIC_0022` hay un fragmento `sacrum` suelto junto a la articulacion
    sacroiliaca derecha, y una region posterior de S1 que solo aparece con 6 mm.
  - Causa no verificada: islas de voxeles o extension distinta.
- **Lo que el recorte NO cambia:** el estado de nivel de #50 (0 casos).
- **Consecuencia para E9:** antes de medir `Dmax` hace falta una regla de limpieza (p. ej. componente
  conexa principal), y hay que declararla como parte del metodo junto a la version y el recorte.
- **Opciones anadidas a las de la autora:**
  - (d) medir E9 con los dos recortes y reportar la diferencia de `Dmax` como incertidumbre (ya
    propuesto el 2026-09-12);
  - (e) regla de limpieza de componentes, declarada.
- **Pendiente de la autora. No aplicado.**

### 51 — TS contradice al revisor clinico en el nivel de S1 de `metal_0012`, que cuenta en la cifra de R1 ya escrita en `main.tex` (49 y 30) — ABIERTA

- **Origen:** `ts_analisis.md`, seccion 1, y laminas de `ts_total_qc/laminas/`, 2026-09-13.
- **Hallazgo 1, `metal_0012`:**
  - El clinico y el agente dicen `ok`.
  - TS da `dz = -24.3 mm` con los dos recortes. Es el unico `ok` con `dz` menor que +3.7 mm.
  - En la lamina (coronal y sagital), las esferas estan en un cuerpo vertebral craneal a la S1 de TS,
    con un disco entre ambos.
  - Tiene marco computable y legible, y S1 `limpio`: **cuenta en los 49 y en los 30** del parrafo
    `Field limitation` de `main.tex`.
- **Hallazgo 2, `metal_0015`** (uno de los 7 de FOV cortado; no entra en los 49):
  - Clinico `ok`; agente `error grosero` ("teja sin cuerpo vertebral").
  - En TS, S1 esta cortada por el FOV (`z+`, 15 726 voxeles, ~20% de la mediana de la cohorte). La
    caja de S1 de TS (z 188.8-200.0; y 153.3-201.8) queda entera **craneal (19 mm) y anterior
    (16 mm)** al punto de R1 (z 169.8; y 137.2).
  - En la lamina, las esferas caen dentro de `sacrum`, hacia la cara dorsal.
  - Dos de tres fuentes dicen que ese punto no es el platillo de S1. Si fuera asi, "los otros 4 [de
    los 7] tienen S1 correcto" (#48) pasaria a 3.
- **Casos que TS apoya:**
  - `metal_0026`: clinico `+1`, agente `ok`. TS no tiene techo porque la columna cae 20 mm anterior
    a la caja de S1. En la lamina, la esfera esta en el cuerpo craneal a la S1 de TS: apoya al
    clinico.
  - `metal_0058`: clinico `otro`, agente "arco posterior". TS da -14.3 / -12.7 mm. En la lamina, la
    esfera esta sobre el arco posterior, craneal y dorsal al cuerpo de S1 de TS.
- **Lectura:**
  - TS no es referencia: no esta validado para el nivel, y una transicion lumbosacra puede cambiar
    que se llama S1.
  - Pero la cifra escrita descansa en un solo revisor, y en `metal_0012` la contradicen TS y la
    imagen. Si `metal_0012` fuera `+1`, quedaria **48 de 65** con marco computable y S1 correcto, y
    **29** sin contaminacion.
  - La frase de los 17 con tornillo iliosacro no cambia: ni `metal_0012` ni `metal_0015` estan en
    `ts_qc_tornillos.csv`.
- **Que seccion toca:** `main.tex`, `Field limitation` (49, 30); #26; `r1_landmarks.md`; #48 (53 con S1
  `ok` y "los otros 4" de los 7).
- **Opciones:**
  - (a) llevar `metal_0012` y `metal_0015` al segundo revisor opcional (pendiente 5 de ESTADO).
    Verificado el 2026-09-13 contra `r1_estados.csv`:
    - `metal_0015` es discrepancia clinico/agente (`ok` frente a `error grosero`), asi que entra en
      cualquier lista de discrepancias.
    - `metal_0012` **no** entra: clinico y agente dicen `ok`, y solo lo senala TS.
    - Los "17" de #26 (12 no-ok + 5 discrepancias) no se reconstruyen desde el CSV: salen 12 no-ok
      y 4 discrepancias ok/no-ok (`0003`, `0015`, `0026`, `0046`), de las cuales `0026` y `0046` ya
      estan entre los 12. Union: 14.
  - (b) mantener 49/30 declarando que la referencia es un revisor unico (ya lo dice) y reportar la
    discordancia con TS.
  - (c) adoptar TS como segundo lector y recontar.
- **Tipo:** RIESGO (cifra escrita). **Pendiente de la autora. No aplicado.**

### 52 — TS etiqueta el implante existente como hueso: `Dmax` en volumenes con tornillo mediria a traves del metal — ABIERTA

- **Origen:** `ts_analisis.md`, seccion 7 (y piloto de #49). Surgio en la asesoria del 2026-09-13.
- **Hallazgo:** la mediana del metal de E8 (> 2500 HU, cilindro de 4 mm) que queda dentro de alguna
  mascara de TS es 98% con los dos recortes. Si E9 se rehace sobre esas mascaras, en los pacientes
  con tornillo iliosacro el corredor incluye el implante como hueso.
- **Que seccion toca:** Objetivo 2 (medicion del corredor), la restriccion #31 (`Dmax`), la cohorte
  sobre la que se mide (grupo 1 frente a grupo 3), y #26/`Field limitation` si el corredor se mide en
  volumenes con metal.
- **Opciones:**
  - (a) medir el corredor solo en pelvis sin osteosintesis;
  - (b) tratar los voxeles > 2500 HU (o la mascara de E8) como ocupados al calcular `Dmax`;
  - (c) medir con y sin (b) y reportar la diferencia.
- **Tipo:** SUPUESTO / METODO. **Pendiente de la autora. No aplicado.**

### 53 — La referencia de nivel de R1 no puede ver vertebras de transicion, y la lista de los "17" de #26 no se reconstruye — ABIERTA

- **Origen:** preparacion del segundo revisor (#51), 2026-09-13, contra `r1_mosaico.py` y
  `r1_estados.csv`.
- **Hallazgo 1:** el mosaico que vio el revisor clinico es un sagital medio de +-60 mm alrededor de la
  cruz. No muestra la columna lumbar entera, asi que no permite contar niveles ni detectar una
  vertebra de transicion lumbosacra. `metal_0012` (#51) es candidato a ese caso. El juicio `ok`/`+1`
  es "la cruz esta en el platillo del primer segmento sacro visible", no un nivel contado.
- **Hallazgo 2:** #26 habla de "12 no-ok + 5 discrepancias = 17". Desde `r1_estados.csv` salen 12
  no-ok y 4 discrepancias ok/no-ok (`0003`, `0015`, `0026`, `0046`), con union de 14. La lista de 17
  no esta en ningun archivo.
- **Que seccion toca:** `main.tex`, `Field limitation` ("confirmed the S1 level"), #26, #51 y el
  diseno del segundo revisor.
- **Opciones:**
  - (a) mosaico ciego nuevo con L1-L5 visibles y coronal, casos dudosos mezclados con controles `ok`
    (requiere anadir seleccion de casos y campo ampliado a `r1_mosaico.py`);
  - (b) declarar en la tesis que la revision no evalua anomalias de transicion;
  - (c) fijar la lista del segundo revisor en un archivo (14 + `metal_0012`).
- **Tipo:** SUPUESTO / RIESGO. **Pendiente de la autora. No aplicado.**

## Ronda 2026-09-14 — transcripcion de R1 corregida, #48-#50 decididas, E10 preparado

### 51 — CERRADA (2026-09-14): era un error de transcripcion, y TS lo detecto

- **Lo que informa la autora:**
  - `metal_0012`: el revisor dijo `+1`; se transcribio `ok` por error. Lo corrigio ella en
    `r1_auditoria_s1_clinico.csv`.
  - `metal_0015`: el propio revisor dudo, "`?` tirando a otro". El asistente lo registro como `?`,
    con ese comentario, a partir de lo que informo la autora.
- **Recuento** (`r1_resumen.py` regenerado; `r1_landmarks.md`, `r1_estados.csv`):
  - Clinico: `ok` 51, `+1` 7, no hallado 4, `otro` 2, `?` 1.
  - **Marco computable con S1 correcto: 48 de 65. Ademas sin contaminacion: 29 de 65.**
  - Acuerdo con el agente: categoria exacta 0.908; ok/no-ok 0.938, kappa 0.81.
- **TS** (`ts_analisis.md` regenerado): **concordancia 57 de 57**.
  - `+1` con techo (6): `dz` de -34.3 a -24.3 mm.
  - `ok` (51): +3.7 a +14.9 mm. Los rangos no se solapan.
  - Sin techo: `metal_0026` (`+1`) y `metal_0015` (`?`).
- **Lectura:** la contradiccion de #51 venia de la transcripcion, no del revisor. TS la detecto sin
  conocer la correccion, lo que respalda usar TS como control de nivel (decision del 2026-09-14).
- **Lo que queda abierto (redaccion):**
  - `main.tex`, `Field limitation`, dice **49** y **30**. Con la transcripcion corregida son
    **48** y **29**.
  - En #48, "los otros 4 [de los 7] tienen S1 correcto" pasa a **3** (`0002`, `0003`, `0054`).
  - La frase de los 17 con tornillo no cambia.
  - `e9b_densidad_s1.md` regenerado: clinico `ok` con los 7 = 51, con alguna esfera < 150 HU 18
    (35%); sin los 7 = 48, 17 (35%). E9b ya esta retirado como evidencia por la decision del
    2026-09-14.
  - **No aplicado a `main.tex`** (regla 4): requiere orden explicita de la autora.

### 53 — ACTUALIZACION 2026-09-14: la lista de los "17" SI se reconstruye (era una suma con solapamiento)

- **Que eran los 17:** 12 no-ok del clinico mas 5 discrepancias de categoria exacta con el agente
  (`0003`, `0015`, `0026`, `0038`, `0046`). `0026`, `0038` y `0046` estaban en los dos grupos: son
  **14 casos distintos**.
- El Hallazgo 2 de #53 ("no se reconstruye") queda corregido: el cruce anterior usaba ok/no-ok y
  dejaba fuera `0038` (`+1` frente a `ambiguo`).
- **Con la transcripcion corregida:** no-ok del clinico 14; discrepancias exactas 6 (`0003`, `0012`,
  `0015`, `0026`, `0038`, `0046`). Union, **15**: `0003`, `0010`, `0011`, `0012`, `0014`, `0015`,
  `0016`, `0022`, `0023`, `0026`, `0038`, `0046`, `0053`, `0058`, `0067`.
- El Hallazgo 1 (el mosaico de +-60 mm no permite contar niveles) sigue **ABIERTO**.

### 48, 49, 50 — DECIDIDAS (2026-09-14): registradas en `01-decisiones.md`

- La autora adopto literal la asesoria del 2026-09-13: TS 2.18.0 `total`; recorte de 6 mm principal
  y 3 mm como sensibilidad; limpieza por fraccion de componente; `total_v3` como trabajo futuro;
  repetibilidad con la cota observada; E9b retirado; sin contraste con/sin metal.
- **Siguen abiertos:**
  - la fraccion de la regla de limpieza: se mide con **E10** (`ts_componentes.py` +
    `ts_componentes.sbatch`, manual en `KHIPU.md`). Probado en local sobre `metal_0008` del piloto:
    `sacrum` tiene 6-8 componentes, el mayor con 99.9% de los voxeles; la union `sacrum+vertebrae_S1`
    tiene **1** componente.
  - #52 (implante existente al medir `Dmax`);
  - bone integrity (#17).
- **No aplicado** a `main.tex` ni a `00-tesis.md` (reglas 4 y 14).

## Ronda 2026-09-14 (2) — 48/29 en `main.tex`, recomendaciones de redaccion, E9-TS preparado

### 51 — Redaccion APLICADA (2026-09-14)

- Por orden explicita de la autora, `main.tex` (`Field limitation`) pasa de "computable in 49 ...
  in 30" a **"computable in 48 ... in 29"**.
- Compila: 4 paginas, 0 citas indefinidas.

### 53 — ACTUALIZACION: "confirmed the S1 level on every patient" ya no es literal

- **Hallazgo:** con `metal_0015` = `?`, el revisor **no** confirmo el nivel en todos los pacientes: en
  uno no pudo decidir. Ademas, el Hallazgo 1 de #53 sigue en pie: juzgo sobre un sagital de +-60 mm.
- **Texto propuesto (no aplicado; requiere orden):** *"After a clinician reviewer (one surgeon,
  otorhinolaryngology), blinded to the automatic audit, judged the S1 level on a mid-sagittal view in
  every patient (undecidable in one), the frame was computable in 48 patients ..."*.
- **Frase opcional:** *"The S1 level implied by TotalSegmentator vertebral labels agreed with the
  reviewer in all 57 patients with a definite judgment and a computable check."*
  - Esta frase se apoya en 57/57 con los rangos de `dz` separados (-34.3 a -24.3 frente a +3.7 a
    +14.9 mm).
  - El detector se definio sobre estos mismos datos, y hay que declararlo si se cita.
- **Que seccion toca:** `main.tex`, `Field limitation`.
- **Pendiente de la autora.**

### 52 — Recomendacion registrada (asistente, 2026-09-14), no decidida: opcion (a), atada a #35

- **Por que (a):**
  - `grupos.csv` ya propone `Elegible Obj2 = si` solo para los grupos 2 y 3 (#35, PROPUESTA): el
    muestreador necesita "geometria osea sacroiliaca intacta y corredor libre".
  - Medir el corredor solo en pelvis sin osteosintesis lo hace comparable con la literatura, toda
    medida en pelvis intactas (`Field limitation`).
  - Evita definir la ocupacion del implante con 2500 HU, que la decision #22 reserva al cribado.
  - Los volumenes con metal quedan para la computabilidad del marco, ya medida y escrita (48/29).
- **Recomendacion de proceso:** decidir antes de leer los resultados de E9-TS. E9-TS calcula todos
  los grupos, asi que la opcion elegida no obliga a volver a correr.
- **Pendiente de la autora:** decidir #52 y #35 juntas.

### E9-TS — preparado y probado en un caso; un hallazgo a vigilar en la cohorte

- **Scripts:** `e9ts_corredor.py` (`.sbatch`), `e9ts_resumen.py` y `noche_e9ts.sh`. Manual en
  `KHIPU.md`.
- **Diseno:** calcula todas las variantes que las decisiones pendientes pueden elegir (recorte x
  fraccion de limpieza, todos los grupos); no decide nada.
- **Prueba** (`metal_0008` del piloto, local, 35 s; tabla en `outputs/e9ts_prueba/`, ignorada por git):
  - `D_TS` = **11.3 mm con 6 mm** y **9.5 mm con 3 mm**. El recorte cambia 1.8 mm y **cruza la
    convencion de 10 mm** (viable si/no).
  - La limpieza no cambia `D` (quita 144 / 212 voxeles lejos del corredor).
  - El eje del mejor corredor (6 mm) va casi paralelo (4.5 grados) al tornillo real `comp 1`, a
    5.9-13.6 mm de su eje, y a >= 2.2 mm del voxel de metal mas cercano. **El cilindro de 11.3 mm
    (radio 5.65 mm) si alcanza el tornillo**, que TS cuenta como hueso: en este caso `Dmax` incluye el
    implante existente. Es #52 en concreto. La lamina coronal lo hacia parecer "sobre el tornillo"
    porque proyecta el eje e ignora su inclinacion en y.
  - `frac_metal_eje` (metal exactamente en el voxel del eje) dio 0 otra vez: no sirve, como en el
    piloto. Se anadieron `frac_eje_metal_r2mm`, `dist_eje_metal_min_mm` y `cilindro_toca_metal`.
  - Densidad: el eje cae 71% (6 mm) / 56% (3 mm) en voxeles <= 150 HU dentro de la mascara, con
    mediana 111 / 118 HU.
- **Lectura:**
  - Con n = 1 no hay resultado.
  - Si en la cohorte el recorte cambia la viabilidad binaria en una fraccion apreciable, la
    incertidumbre de #49 deja de ser un matiz y pasa a la conclusion del Objetivo 2.
  - La densidad del eje dentro de la mascara es la medida que decidio el 2026-09-14 en lugar de E9b.
- **Que seccion toca:** #49 (el recorte como incertidumbre de la viabilidad), #31 y el Objetivo 2.
- **Pendiente:** correr la cohorte y leer `e9ts_resumen.md`, seccion 3.

## Ronda 2026-09-14 (3) — #52 decidida (a + c), #35 cerrada, ITK-SNAP para el revisor

### 52 — DECIDIDA por la autora (2026-09-14): opciones (a) y (c)

- **(a):** el corredor del Objetivo 2 se mide en pelvis **sin osteosintesis** (grupos 2 y 3).
- **(c):** en los volumenes con implante se mide **con y sin el implante como espacio ocupado**, y se
  reporta la diferencia.
- **Como se implemento (c) sin decidir la forma del implante:** la decision #22 no deja definirla con
  2500 HU. `e9ts_corredor.py` calcula dos politicas de ocupacion, ademas de `hueso` (TS tal cual):
  - `ocupado_2500`: 2500 HU adelgaza el implante (#46), asi que da una **cota superior** del corredor
    ocupado;
  - `ocupado_semimax`: semimaximo local por objeto, con el casquete de E8. Es la propuesta abierta de
    #22; difiere de E8 en que no fusiona fragmentos.
- **Pendiente de la autora:** cual de las dos es la principal. No hace falta volver a correr.
- **Prueba** (`metal_0008`, F = 0): con 6 mm, `D_TS` da **11.3 mm como hueso y 10.0 mm con cualquiera
  de las dos ocupaciones**. Con 3 mm, 9.5 mm en las tres politicas.
- **Lectura (n = 1):** en este caso el implante existente agranda el corredor medido 1.3 mm y lo pone
  sobre la convencion de 10 mm. Con 3 mm el mejor corredor no toca el tornillo y no cambia.
- **Registrada en `01-decisiones.md`** (2026-09-14 (2)) por el asistente, con orden explicita de la
  autora.

### 35 — CERRADA por la autora (2026-09-14)

- **Se adopta el reparto por objetivo** de `grupos.csv`: Obj 1 = grupos 1-3 (168); **Obj 2 = grupos 2
  y 3 (103), coherente con #52 (a)**; Obj 3 = grupo 3 (66).
- `grupos.py` regenerado: solo cambian `Regla` y `Estado regla` (168 filas, de `PROPUESTA #35` a
  `decidida #35`). Grupos y elegibilidades, identicos.
- **Lo que no cierra:** la **evidencia** de `Elegible Obj3` (eje de artefacto de agente, #34/#37,
  bloqueo declarado), la definicion en tres ejes de `Objeto extraño` que proponia #35 (no aplicada a
  `02-datos.md` ni a `03-glosario.md`), y #43 (particion unica frente a elegibilidad), que sigue
  ABIERTA.
- **Registrada en `01-decisiones.md`** (2026-09-14 (2)) por el asistente, con orden explicita de la
  autora.

### 53 — ACTUALIZACION 2026-09-14: el revisor pide ver cada punto en ITK-SNAP; tabla generada

- **Pedido:** el revisor clinico quiere el corte exacto de cada punto de S1 para mirarlo en el volumen
  completo. Eso responde al Hallazgo 1: en el volumen completo si se pueden contar niveles.
- **Hecho:** `experiments/objetivo2/r1_cortes_itksnap.py` genera `r1_cortes_itksnap.csv`
  (versionable), con los 65 casos de evaluacion:
  - 61 con punto: corte sagital, coronal y axial en el **archivo original**, contados desde 0 y
    desde 1; voxel (i, j, k); mundo RAS y LPS; HU del voxel y mediana 3x3x3; corte axial de la linea
    del ala.
  - 4 sin punto: `0016`, `0022`, `0023`, `0053`.
  - Ciega: sin juicios de clinico, agente ni TS.
- **Comprobacion interna superada:** en los 61 casos, el HU en el indice calculado sobre el archivo
  original coincide con el HU del punto en el marco RAS de R1. En los 61, los ejes del archivo ya
  estan en orden sagital/coronal/axial (0/1/2).
- **No verificado:** si ITK-SNAP numera los cortes desde 0 o desde 1, y si muestra coordenadas RAS o
  LPS. Por eso la tabla trae ambas y el HU. El revisor debe comprobar que el cursor marca ese HU.
- **Pendiente de la autora:**
  - si el revisor mira los 15 casos de la lista o los 61. Si solo los 15, conviene mezclarlos con
    controles `ok` para no revelarle cuales son dudosos;
  - que el nuevo juicio se guarde en un archivo aparte, sin sobrescribir
    `r1_auditoria_s1_clinico.csv`.

## Ronda 2026-09-14 (4) — E9-TS y E10 completos en la cohorte

Fuente: `experiments/objetivo2/outputs/e9ts/e9ts_resumen.md` (jobs 51505, 51522, 51523) y consultas del
asistente sobre `e9ts_corredor.csv`, `ts_componentes*.csv` (outputs ignorados por git). E10: 179 casos,
1790 estructuras, 0 errores (el primer intento, 51504, murio por SIGKILL externo a los 42 casos).
E9-TS: 152 casos, 0 errores, 2352 filas.

### 49 — ACTUALIZACION 2026-09-14 (4): la limpieza no mueve el corredor; el recorte si cruza los 10 mm

- **E10, tamanos:** 1239 componentes no principales con >= 10 voxeles; fraccion de su estructura con
  mediana 0.00009 y p90 0.00095. Solo 36 filas (caso x recorte x estructura) tienen un componente no
  principal >= 1%; casi todos contiguos al mayor (`dist_caja_mayor_mm = 0`), p. ej. `CLINIC_0022`
  S1 44%, `CLINIC_0032` sacro 30%, `CLINIC_0061` cadera 8.8%: candidatos a fractura o a particion de
  etiqueta, **sin revisar en lamina**.
- **Que quita cada F:** 0.001 -> componentes de hasta 0.38 mL; 0.01 -> 2.08 mL; 0.05 -> 12.41 mL (este
  ultimo podria borrar fragmentos de fractura).
- **Los 10 desplazamientos de caja (11 estructuras):** en 8 los explica una isla de 1-8 voxeles
  presente en un solo recorte (`vox_fuera_mayor` 2-8, `n_comp` > `n_comp_min10`); en `CLINIC_0022`
  sacro, un componente de 68 voxeles a 80 mm; en `CLINIC_0029` S1, uno de 24 voxeles a 14 mm; en
  `CLINIC_0032` S1, componentes de fraccion 0.0005 contiguos. **Todos tienen fraccion < 0.001**, asi
  que F = 0.001 los quitaria. **No verificado:** las cajas no se recalcularon tras limpiar (hacen falta
  las mascaras, en Khipu); es inferencia desde los componentes.
- **E9-TS, efecto de F sobre `D_TS`** (QC de nivel, 124 casos): cambia en **1 caso por recorte**, ambos del
  grupo 1 (`metal_0002` 6 mm 13.8 -> 13.4; `metal_0041` 3 mm 12.0 -> 11.1), identico para F = 0.001,
  0.01 y 0.05. **En la cohorte del Objetivo 2 (72), cero cambios** y ninguna viabilidad cambia.
- **Recorte:** en la cohorte del Objetivo 2, `D(6) - D(3)` tiene mediana 0.0 mm, p10/p90 -0.89/+0.89,
  |dif| >= 1 mm en 14 de 72; viable a 10 mm con los dos recortes 27, con alguno 29 (37.5-40.3%). Cruzan
  10 mm 2 casos del Objetivo 2 (`CLINIC_0090`, `CLINIC_0101`) y 10 del grupo 1.
- **Lectura:** la eleccion de F es de higiene de mascara, no de resultado; el recorte es la
  incertidumbre que si llega a la conclusion binaria, y ya esta decidido reportarla (decision
  2026-09-14). Cualquier F se eligio despues de mirar los datos: declararlo y reportar la invarianza.
- **Tipo:** METODO. **Pendiente de la autora:** fijar F. No aplicado.

### 52 — ACTUALIZACION 2026-09-14 (4): la ocupacion importa en el grupo 1; 2500 y semimaximo no se distinguen en viabilidad

- Grupo 1, QC de nivel, 52 casos, F = 0: la ocupacion cambia `D_TS` en 21-23; viable a 10 mm pasa de
  53.8% a 40.4% (6 mm) y de 57.7% a 40.4% (3 mm): se pierden 7 (6 mm) y 9 (3 mm). Diferencia mediana en
  los casos con cambio: 2.0 mm; maxima 6.0 mm.
- **`ocupado_2500` y `ocupado_semimax` difieren en 6 de 118** filas caso x recorte (maximo 1.0 mm,
  `metal_0062`) y **en ninguna cambia la viabilidad a 10 mm**. Elegir la politica principal no cambia
  ningun resultado binario.
- Grupos 2 y 3: 7 casos con voxeles > 2500 HU en el recorte (5 y 2; en grupo 3 son `CLINIC_0058`, HU max
  2641, y `CLINIC_0074`, 2540, el lazo de #19); cero cambios.
- **No se interpreta** que grupo 1 ocupado (40.4%) y Objetivo 2 (40.3%) coincidan: grupos no
  emparejados (decision 2026-09-14).
- **Pendiente de la autora:** politica principal. No aplicado.

### 48 — ACTUALIZACION 2026-09-14 (4): la densidad medida dentro de la mascara, la que se decidio en lugar de E9b

- Cohorte del Objetivo 2, QC de nivel, 72 casos, eje del mejor corredor dentro de `sacrum` +
  `vertebrae_S1`: mediana de `hu_p50_eje` **171.5 HU** (IQR 119.6-216.5) con 6 mm y 160.3 con 3 mm;
  fraccion del eje <= 150 HU con mediana **0.42** (6 mm) / 0.46 (3 mm); **28 de 72** con mas de la mitad
  del eje <= 150 HU.
- Confirma, ahora con la medida decidida, que una regla de hueso > 150 HU dejaria fuera buena parte del
  trayecto del corredor en pelvis sin osteosintesis. Toca bone integrity (#17) y el texto propuesto de
  #48 aun no aplicado a `main.tex`.
- **Pendiente de la autora:** si se cita la cifra y como se resuelve bone integrity (#17). No aplicado.

### 54 — La QC de nivel excluye 18 de 91 casos del Objetivo 2, y excluye mas en el grupo 2 (32%) que en el grupo 3 (12%) — ABIERTA

- **Hallazgo:** la cohorte del Objetivo 2 son 103 pacientes; 91 tienen punto de S1 en R1; la QC deja 72
  (72 pacientes unicos). Motivos: `R1 arriba de TS` en **18** y S1 tocando el FOV en 1. Los 12 sin fila no
  tienen S1 en R1 (criterio de `e9ts_corredor.py`).
  - Por cohorte de R1: `calibracion` (60; 3 del grupo 2 y 57 del grupo 3) **7 discordantes**, que son los
    7/60 ya conocidos de `ts_analisis.md`; `otro` (31, todos del grupo 2) **11 discordantes (35%)**.
  - Por grupo: grupo 2, 11 de 34 (32%); grupo 3, 7 de 57 (12%).
  - Contraste: en el grupo 1 (`evaluacion`) los 7 `R1 arriba de TS` coinciden en numero con los 7 `+1`
    del revisor clinico.
- **Por que importa:**
  - En el grupo 1, TS concordo con el revisor clinico (#51, `ts_analisis.md`) y la discordancia es error
    de R1. **En los grupos 2 y 3 no hay juicio clinico**: atribuirla a R1 es inferencia por analogia.
  - El conjunto `otro` nunca se uso para calibrar ni evaluar R1, y ahi se concentra la discordancia.
  - La exclusion es desigual entre grupos, y el grupo 2 ya tiene el corredor mas estrecho (mediana 8.9
    frente a 9.8 mm). La cifra del Objetivo 2 podria sesgarse hacia el grupo 3.
- **Que seccion toca:** cohorte y tamano del Objetivo 2; criterio de QC de la decision 2026-09-14
  ("nivel TS/R1 discordante: se excluye o se revisa").
- **Opciones:**
  - (a) mantener la exclusion (72) y declarar el embudo y el desbalance;
  - (b) en los 18, usar el nivel de TS para centrar el recorte y relanzar E9-TS solo en ellos (hay que
    modificar la entrada de S1; no esta implementado);
  - (c) revisar los 18 a mano (la decision ya permitia "se revisa").
- **Tipo:** COHORTE / SESGO. **Pendiente de la autora. No aplicado.**

### 49, 52, 54, 48 — DECIDIDAS Y APLICADAS (2026-09-14): la autora acepta las recomendaciones

- **Decision** registrada en `01-decisiones.md` (2026-09-14 (3)) por el asistente con orden explicita:
  F = 0.001; `ocupado_semimax` principal y `ocupado_2500` como cota; #54 opcion (a), exclusion mantenida
  con embudo declarado.
- **Aplicado a `tesis/main.tex`** con orden explicita:
  - Objetivo 2: mascaras de TotalSegmentator 2.18.0 (`\citep{wasserthal2023}`), recorte por defecto con el
    robusto como sensibilidad, QC por caso y limpieza < 0.1%.
  - Parrafo nuevo `Corridor measurement on the local cohort`: embudo 103 -> 91 -> 72 (con la exclusion por
    FOV, corregida respecto del borrador del chat), 9.5 mm (IQR 7.4-11.7), 29 y 27 de 72, fraccion 0.42
    <= 150 HU (#48), y 53.8% -> 40.4% en 52 pacientes con metal.
  - Compila: 4 paginas, 41 referencias, 0 citas indefinidas.
- **Alta bibliografica:** `wasserthal2023` (raw pegado por la autora; `MAPEO.md` actualizado). Ficha en
  curso con `lector-papers`.
- **Sigue abierto:**
  - #49: la afirmacion "F = 0.001 elimina los 10 desplazamientos" es inferencia hasta correr E10b
    (`ts_cajas_limpias.py`, `KHIPU.md`); `main.tex` no la afirma.
  - #48/#17: bone integrity sigue sin resolverse; `main.tex` solo dice que una definicion por HU excluiria
    buena parte del corredor.
  - #54 (b) queda como sensibilidad no implementada.
  - Los 36 componentes >= 1% y los minimos (`CLINIC_0091`, `CLINIC_0078`) siguen sin revisar en lamina.

### 55 — El paper citado de TotalSegmentator no valida la version usada: sin clase S1, sin Dice por clase y sin metal — ABIERTA

- **Origen:** ficha `docs/literatura/wasserthal2023.md` (`lector-papers`, 2026-09-14); PDF de 9 paginas sin
  suplemento.
- **Hallazgo:**
  - Describe un nnU-Net de 104 estructuras con modelos de 1.5 y 3 mm; Dice global 0.943 (p. 4). No da numero
    de version, tarea `total`, modelo "fast" ni recorte de 6 mm.
  - La Figura 2 (p. 4) nombra `sacrum`, `hip` y vertebras C1-L5: **S1 no aparece** y tampoco la lateralidad
    de cadera. Los Dice por clase estan en el suplemento, que no esta en el PDF.
  - **Ninguna mencion de implantes, metal ni artefactos**; excluyeron del entrenamiento estructuras "highly
    distorted" (n = 40, p. 2).
  - Inconsistencia interna: 0.932 vs 0.871 figura como "separate dataset" en el abstract y como "our test set"
    en resultados (p. 5).
- **Que toca:** `main.tex` cita `\citep{wasserthal2023}` solo como fuente de las mascaras: **eso si lo
  respalda**. No podria respaldar ninguna frase sobre la calidad de `vertebrae_S1` o de la segmentacion junto
  a metal. Refuerza la condicion ya decidida "TS es herramienta, no referencia" y la QC por caso
  (decision 2026-09-14): la unica validacion local de nivel es la concordancia con el revisor en el grupo 1.
- **Opciones:** (a) dejar la cita como esta y no afirmar calidad (estado actual); (b) conseguir el suplemento
  o una fuente de la version con `vertebrae_S1` si alguna frase de la tesis llegara a necesitarlo.
- **Tipo:** REDACCION / SUPUESTO. **Pendiente de la autora. No aplicado.**

### Valores extremos del Objetivo 2 — sin implicancia, anotado para QC

- `CLINIC_0091` (`D_TS` 2.0 mm) y `CLINIC_0078` (2.2 mm): en lamina coronal no se ve un fallo grosero de
  mascara; el perfil es 0 en casi todos los niveles con IS izq/der 8.5/9.6 y 8.9/3.5 mm. Compatible con
  corredor transsacro ausente, **sin verificar**. Revisar antes de citar minimos.

## Ronda 2026-09-14 (5) — cierre de la sesion: verificaciones, E10b preparado y pendientes de redaccion

### Cifras de pacientes de `main.tex` — VERIFICADAS (sin implicancia)

- `grupos.csv` (179 filas, 168 pacientes): grupos 2 y 3 = **103 filas = 103 pacientes** (37 + 66).
- E9-TS, `default6mm`, F = 0, `hueso`: Objetivo 2 con S1 = **91 filas = 91 pacientes**; tras la QC =
  **72 = 72**; grupo 1 tras la QC = **52 = 52**. Ninguna fila sin `Grupo paciente`.
- La exclusion por FOV del Objetivo 2 es `CLINIC_0010` (grupo 3). Cuadra: grupo 3, 57 - 7 - 1 = 49;
  grupo 2, 34 - 11 = 23. (El otro caso con S1 en el FOV es `metal_0015`, del grupo 1.)
- Las frases "103 patients", "91", "72 passed" y "52 patients" del parrafo `Corridor measurement on the
  local cohort` quedan respaldadas en unidad paciente.

### 49 — E10b PREPARADO y probado en local; falta la corrida en Khipu

- **Scripts:** `experiments/objetivo2/ts_cajas_limpias.py` + `.sbatch`. Manual en `KHIPU.md`, seccion E10b.
- **Que hace:** recalcula la caja de las 4 estructuras en los dos recortes con F = 0, 0.001, 0.01 y 0.05,
  con la misma formula que `ts_qc.py` (`dif_caja_3v6_max_mm`, RAS+).
- **Control que puede fallar:** con F = 0 debe reproducir `ts_qc.csv`.
- **Prueba local** (piloto `CLINIC_0002` + `metal_0008`, copia en el scratchpad con `.ok` creados a mano):
  10.8 s los 2 casos; control **8 de 8** contra `ts_piloto_qc.csv`; 0 desplazamientos > 10 mm con toda F
  (esperado: el piloto no tenia desplazamientos). Prueba sintetica: una isla de 1 voxel se quita con F > 0.
- **Criterio de lectura en Khipu:** F = 0 debe dar los 10 casos / 11 estructuras de `ts_analisis.md`; F = 0.001
  deberia dar 0. Si quedan desplazamientos, la frase "cleaned of connected components below 0.1%" de
  `main.tex` sigue siendo cierta como regla, pero la justificacion de la decision 2026-09-14 (3) ("quita las
  islas de los 10 desplazamientos") cae y hay que revisarla.
- **Estado:** ABIERTA hasta leer la corrida.

### Patron vigilado (#25, #37, #40, #45, #47, #50) — un caso evitado en E10b

- La primera version de `control()` imprimia "0 de 0 estructuras coinciden" cuando no habia filas en comun:
  **un control que no puede fallar**, justo el patron que `ESTADO.md` pide vigilar. Salio en la prueba local
  (las mascaras del piloto no tenian `.ok`). Corregido: ahora imprime `CONTROL NO EJECUTADO` y no valida.
- Tambien en E10 (`ts_componentes.py`): la cabecera del CSV de errores no se volcaba al abrir y un SIGKILL la
  dejo en 0 bytes. `ts_cajas_limpias.py` ya la vuelca; `ts_componentes.py` no se modifico (corrida cerrada).

### Pendientes de redaccion derivados de lo aplicado — ABIERTOS

- **Post hoc no declarado en `main.tex`:** F = 0.001 y `ocupado_semimax` se eligieron tras ver E9-TS/E10. Lo
  dice `01-decisiones.md`, no `main.tex`. Hoy el parrafo solo afirma que la limpieza no cambio ninguna medida,
  lo que hace la eleccion inocua para la cifra; declararlo o no es decision de la autora.
- **`ocupado_2500` como cota no aparece en `main.tex`:** el parrafo reporta solo semimaximo. La decision dice
  "se reporta como cota"; hoy el reporte vive solo en `e9ts_resumen.md` (ignorado por git).
- **Tablas citadas sin version:** `e9ts_resumen.md`, `e9ts_corredor.csv` y `ts_componentes*.csv` estan en
  `outputs/` (ignorado). `KHIPU.md` pide copiar a `experiments/objetivo2/` lo que se cite; aun no se hizo.
- **Nivel N2 de `wasserthal2023`** en `_index.md`: propuesto por el asistente, sin confirmar.

### 55 — ACTUALIZACION 2026-09-14: el README del repositorio confirma el desfase de version y toca #49 y #54

- **Fuente:** README de `https://github.com/wasserth/totalsegmentator`, rama principal, pegado por la autora en el
  chat el 2026-09-14. No es un PDF de `papers/` ni tiene raw en `refs/raw/`: sirve como evidencia interna, **no
  es citable en `main.tex`** sin alta bibliografica (regla 9). No fija version: describe la rama actual, no
  necesariamente la 2.18.0 usada.
- **Lo que resuelve de #55:**
  - **El paper es de la v1, dicho por los autores:** *"Our Radiology AI publication refers to TotalSegmentator v1."*
    (seccion "Running v1"). La cohorte uso 2.18.0 (v2). El desfase deja de ser inferencia de la ficha.
  - **La clase existe en la tarea usada:** *"total: default task containing 117 main classes"*; la tabla de clases
    lista `sacrum` (25), `vertebrae_S1` (26), `hip_left` (77) y `hip_right` (78). Coincide con las mascaras que
    produjo la cohorte. **Existencia no es validacion**: el README no da cifras por clase.
  - **Citar el paper es la practica que piden los autores**, tambien para v2: *"If you use it please cite our
    Radiology AI paper"*. La cita actual de `main.tex` es correcta como fuente del software.
  - **Licencia:** *"Openly available for any usage (Apache-2.0 license)"*, con `total` en esa lista. Cierra el punto
    6 de la ficha (en el PDF: `NO ENCONTRADO`).
  - **Datos de entrenamiento distintos del paper:** el README ofrece *"CT dataset (1228 subjects)"*; el paper
    describe 1204 examenes (ficha). Otro indicio de que el modelo en uso no es el validado.
- **Lo que abre o precisa:**
  - **nnU-Net:** *"Please also cite nnUNet since TotalSegmentator is heavily based on it."* No hay entrada de nnU-Net
    en `refs.bib`. Anadirla es decision de la autora y empieza por pegar su raw (regla 9).
  - **Resultados por clase:** el README remite a un archivo con las cifras del modelo de 1.5 mm y dice *"The paper shows
    these numbers in the supplementary materials Figure 11."* La ficha registro el suplemento como "Figure S1"
    (desde el PDF). **Discrepancia de nombre sin verificar**; el enlace no vino en el texto pegado, y no consta a
    que version corresponden esas cifras.
  - **#49, recorte:** el README describe `--robust_crop`: el recorte de 6 mm *"Sometimes this model is incorrect,
    which leads to artifacts like segmentations being cut off."* y el de 3 mm es *"a better but slower 3mm model"*.
    La decision 2026-09-14 eligio 6 mm como principal por ser el defecto (reproducibilidad) y por ir algo mejor en
    tornillos locales; los desarrolladores llaman "better" al de 3 mm. En la cohorte local no hubo truncamiento
    (#49) y `D(6) - D(3)` tiene mediana 0.0 mm, pero **un tribunal puede preguntar por que el principal no es el
    recomendado**: la justificacion hay que poder decirla, y hoy `main.tex` no la dice.
  - **#54, atribucion de la discordancia de nivel:** el README anuncia `vertebrae_pp` con *"less mixup of neighboring
    vertebrae"*, es decir, los desarrolladores reconocen confusiones de vertebras vecinas en `total`. En los grupos 2
    y 3 (sin juicio clinico) eso debilita aun mas atribuir los 18 casos a R1. `vertebrae_pp` cubre *"vertebral bodies
    C1-L5"*: **no incluye S1**, asi que no sustituye a `vertebrae_S1`; podria servir, sin implementar, para
    comprobar que L5 esta bien etiquetada justo encima.
  - **#52, implante:** existe la tarea `hip_implant`, marcada con asterisco (*"not trained on the full totalsegmentator
    dataset"*). Es de protesis de cadera, no de tornillos iliosacros: no resuelve la ocupacion de #52.
  - **Reproducibilidad:** `--report` escribe *"a machine-readable JSON run manifest"* con versiones de software y
    modelo. La cohorte no lo uso; su version quedo registrada por otra via (`ts_total_procedencia`). No consta
    desde que version existe la opcion.
- **Opciones (no aplicadas):**
  - (a) en `main.tex`, junto a la cita: declarar que la publicacion describe la v1 y que la version usada es 2.18.0
    (la afirmacion literal de los autores lo respalda, pero el README no es citable sin alta);
  - (b) alta de nnU-Net (la autora pega el raw);
  - (c) conseguir las cifras por clase (`sacrum`, `vertebrae_S1`, `hip_*`) del archivo que enlaza el README y la
    version a la que corresponden; solo si alguna frase de la tesis necesita calidad de mascara;
  - (d) justificar en `main.tex` el recorte por defecto como principal frente al robusto que recomiendan los
    desarrolladores, apoyado en la invarianza medida (mediana 0.0 mm; 2 de 72 cruzan 10 mm).
- **Estado:** #55 sigue **ABIERTA**; ahora con evidencia de los propios autores. Toca tambien #49 (recorte) y #54
  (atribucion). **Pendiente de la autora.**

## Ronda 2026-09-14 (6) — cuatro pendientes de redaccion aplicados; la autora prefiere el recorte de 3 mm

### 55 y pendientes de la ronda (5) — APLICADOS a `main.tex` (orden explicita de la autora)

- **Interpretacion de la orden** ("los cuatro pendientes de redaccion"): los cuatro que tocan `main.tex`. (1) declarar
  que la fraccion y la regla de ocupacion son post hoc; (2) reportar la cota de 2500 HU; (3) #55 (a), el desfase
  entre la publicacion citada y la version usada; (4) #55 (b), citar nnU-Net. Los otros dos de la ronda (5), tablas
  sin versionar y nivel N2 de `wasserthal2023`, no son de `main.tex` y siguen ABIERTOS.
- **Textos aplicados:**
  - Objetivo 2: "TotalSegmentator 2.18.0 \citep{wasserthal2023}, which is built on nnU-Net \citep{isensee2021}" y "The
    cited publication evaluates a 104-structure model and reports no accuracy for the S1 label used here, so its
    reported accuracy is not assumed for the version and classes used in this work."
  - `Corridor measurement`: la limpieza no cambio ninguna medida "at any tested fraction up to 5%; the fraction, like the
    occupancy rule below, was fixed after inspecting these results"; y la cota: "a fixed 2500 HU threshold, which thins
    the screws and therefore bounds the occupied corridor from above, gave the same proportion".
- **Respaldo de cada frase:**
  - "104-structure model" y "reports no accuracy for the S1 label": ficha de `wasserthal2023` (titulo; sin Dice por
    clase en el PDF). **No** se escribio "v1" ni "without an S1 label": lo primero esta solo en el README (no
    citable) y lo segundo no se puede afirmar sin el Appendix S1 (la lista completa de clases no esta en el PDF).
    Una primera version decia "without a separate S1 label" y se corrigio antes de compilar.
  - "built on nnU-Net": lo dice la propia publicacion citada, *"The authors trained an nnU-Net segmentation algorithm"*
    (abstract en `refs/raw/wasserthal2023.bib`; la ficha tambien lo registra, Model, p. 2). El README lo repite
    ("heavily based on it"), pero no hace falta. La ficha de `isensee2021` esta en curso (`lector-papers`).
  - "same proportion": grupo 1, 6 mm, se pierden 7 de 52 con las dos politicas (53.8% -> 40.4%).
  - "thins the screws": E8 (#46), ya dicho en `Implant geometry source`.
- **Alta bibliografica:** `isensee2021` (raw PubMed pegado por la autora; `MAPEO.md`). `refs.bib` 41 -> 42.
- **Compila:** 4 paginas, 42 referencias, 0 citas indefinidas, los 2 avisos conocidos.
- **#55:** (a) y (b) APLICADAS. (c), cifras por clase, sigue ABIERTA. (d), justificar el recorte de 6 mm, queda
  **superada** por la preferencia de la autora (abajo).

### 55 — ACTUALIZACION 2026-09-14 (ficha de `isensee2021`): el PDF no es el articulo citado, y nnU-Net no respalda la limpieza F — ABIERTA

- **Desfase PDF / raw:** `papers/isensee2021.pdf` es el preprint arXiv:1904.08128v2 (2020), *"Automated Design of Deep
  Learning Methods for Biomedical Image Segmentation"*, 19 datasets. `refs/raw/isensee2021.nbib` y `refs.bib` describen
  Nature Methods 18(2):203-211 (2021), *"nnU-Net: a self-configuring method..."*, "23 public datasets". La ficha se hizo
  sobre el preprint.
- **Efecto sobre `main.tex`, hoy acotado:** la cita solo identifica el metodo en "built on nnU-Net", y esa afirmacion
  la respalda `wasserthal2023` (abstract: "trained an nnU-Net"). No se toma ninguna cifra ni frase del articulo. La
  referencia impresa coincide con su raw (regla 9). Lo que falta es tener en `papers/` el PDF que se cita.
- **nnU-Net no es precedente de la limpieza por fraccion:** su postprocesado es *"non-largest component suppression"*
  (p. 3), aplicado solo si no baja el Dice de ninguna clase en validacion cruzada (p. 20), con una instancia por
  estructura como supuesto (B.3, p. 26). No usa fraccion ni tamano. La decision 2026-09-14 descarto "componente mayor"
  por las fracturas: **coherente**, pero **sin respaldo bibliografico** para F. Hay que decirlo como regla propia si
  alguien pregunta.
- **Sin CT oseo ni metal:** los 10 datasets CT del preprint son de abdomen, pulmon y torax (Table A.1, p. 23). No aporta
  nada sobre robustez con metal; coincide con lo que #55 ya registra para TotalSegmentator.
- **Snowballing:** la fila de nnU-Net (arXiv:1904.08128) de `_candidatos.md`, que salio de `liu2021ctpelvic1k`, es este
  preprint: se marca LEIDO.
- **Opciones:** (a) conseguir el PDF de Nature Methods y releerlo con `lector-papers`; (b) dejarlo como esta y declarar
  en `_index.md` que el PDF local es el preprint (hecho); (c) retirar la cita de nnU-Net si la autora prefiere no citar
  sin el PDF publicado (el README pide citarla, pero no es obligatorio).
- **Tipo:** REFERENCIA / SUPUESTO. **Pendiente de la autora. No aplicado.**
- **Seguimiento 2026-09-14 — el archivo subido como "Nature Methods 2021" es otro articulo:** la autora pego
  `refs/raw/falk2019.nbib` y `papers/falk2019.pdf` como el nnU-Net publicado. El raw describe **Falk T et al., "U-Net:
  deep learning for cell counting, detection, and morphometry", Nat Methods 16(1):67-70, 2019** (PMID 30559429): plugin
  de ImageJ para celulas, no nnU-Net (Isensee et al., Nat Methods 18(2):203-211, 2021, PMID 33288961).
  - **No se hizo nada con el:** ni `refs/clean/`, ni `refs.bib`, ni ficha. No se abrio el PDF (regla 10), asi que no
    consta si `falk2019.pdf` es el Falk 2019 del raw o el nnU-Net mal nombrado.
  - **`papers/isensee2021.pdf` sigue siendo el preprint** (mismo tamano, 9.3 MB).
  - **Redaccion a revisar cuando llegue el articulo correcto** (hoy descrita como del preprint, no como del articulo
    publicado): "nnU-Net no respalda la regla F" (postprocesado, pp. 3 y 20 del preprint), "sin CT oseo ni metal"
    (Table A.1 del preprint: 10 CT; el publicado declara 23 datasets) y "self-configuring NO ENCONTRADO" (ficha 1m).
    `main.tex` no depende de ninguna: su unica frase ("built on nnU-Net") la respalda `wasserthal2023`.
  - **Pendiente de la autora:** confirmar que se queria el nnU-Net de 2021 y reemplazar `papers/isensee2021.pdf` por el
    PDF publicado; decidir que hacer con `refs/raw/falk2019.nbib` y `papers/falk2019.pdf` (no se borran sin orden).
- **RESUELTO 2026-09-14:** la autora reemplazo `papers/isensee2021.pdf` por el articulo de Nature Methods (6.9 MB) y
  retiro `falk2019` de `papers/` y `refs/raw/`. Ficha rehecha con `lector-papers`; identidad verificada contra el raw
  (titulo, cinco autores, DOI). El PDF trae 12 pp. de articulo + Reporting Summary, **sin** Extended Data ni
  Supplementary Notes; volumen y paginas no estan impresos.
  - **(a) Se mantiene:** unico postprocesado *"non-largest component suppression"* (p. 4), aplicado si mejora el Dice
    medio y no baja ninguna clase (Methods, p. 11); **sin umbral de tamano ni fraccion**. nnU-Net sigue sin ser
    precedente de la regla F. El supuesto "una instancia por estructura" era del suplemento del preprint: no verificable.
  - **(b) Se mantiene:** 23 datasets, 53 tareas; los CT son higado, pulmon, pancreas, vasos hepaticos, bazo, colon,
    organos abdominales, rinon y torax; los 4 nuevos (D20-D23) son microscopia. **Sin CT oseo, pelvis, vertebras ni
    metal.**
  - **(c) Cambia:** "self-configuring" esta en el titulo, no en el cuerpo.
  - **(d) Se mantiene:** tres configuraciones por defecto (p. 4) frente a cuatro seleccionables (Methods, p. 11).
  - **Cifras del preprint superadas** (19 datasets / 49 tareas -> 23 / 53); ninguna estaba en `main.tex`.
  - **Posible precedente de F:** el articulo cita LiTS (ref. 18) y KiTS19 (ref. 25) junto al postprocesado por
    componentes. Anadidos a `_candidatos.md` como PENDIENTE (prioridad 3), sin cita completa copiada.
- **Estado del subpunto "PDF / raw":** CERRADO. **#55 sigue ABIERTA** por (c), las cifras por clase de TotalSegmentator,
  y la regla F queda declarada como propia (sin precedente bibliografico hasta revisar LiTS/KiTS19).
  `main.tex` no cambia.

### 49 — La autora prefiere el recorte de 3 mm como principal — PENDIENTE (no aplicado)

- **Que dijo la autora (2026-09-14):** esta de acuerdo con las decisiones de la ronda, pero prefiere `robust3mm` como
  principal porque tiene fuentes que lo respaldan. Pide dejarlo pendiente y preparar los experimentos.
- **Estado de los documentos, hoy inconsistente con esa preferencia:**
  - `01-decisiones.md` (2026-09-14) dice "Recorte principal: default 6 mm; robust 3 mm como analisis de
    sensibilidad". No se edito: falta orden explicita (regla 3).
  - `main.tex` dice "default crop; robust crop as sensitivity analysis", y el parrafo `Corridor measurement` usa
    las cifras de 6 mm.
- **Las fuentes de la autora no estan en el repositorio.** Para citarlas hace falta su raw en `refs/raw/` y su PDF en
  `papers/` (reglas 9 y 10). El README de TotalSegmentator llama "better" al modelo de 3 mm (#55), pero no es citable.
- **No hay que recalcular cifras:** E9-TS (51505), E10 y E10b ya calculan los dos recortes. Con `robust3mm`
  como principal, desde `e9ts_resumen.md` y las consultas del 2026-09-14 (4):
  - Objetivo 2 (72): mediana 9.4 mm (IQR 7.8-11.7); viable a 10 mm **27 de 72 (37.5%)**; 6 mm como sensibilidad 29 de
    72. Cruzan 10 mm los mismos 2 casos.
  - Densidad en el eje: fraccion <= 150 HU mediana **0.46** (6 mm: 0.42); `hu_p50` mediana 160.3 HU.
  - Grupo 1 (52): viable 57.7% -> **40.4%** con semimaximo; 2500 HU, la misma proporcion (se pierden 9 con las dos).
- **Lo que si falta, preparado:** laminas de QC con 3 mm (51505 solo las hizo con 6 mm) y resumen con la seccion 5
  en 3 mm. `e9ts_corredor.py --modo-laminas`, `e9ts_resumen.py --modo-principal`, `e9ts_repetibilidad.py` y
  `e9ts_3mm.sbatch`; manual en `KHIPU.md`, "E9-TS con 3 mm".
  - **Prueba local** (`metal_0008` del piloto): lamina con 3 mm generada; seccion 5 del resumen en `robust3mm`;
    repetibilidad **IDENTICO** (24 x 43) frente a `outputs/e9ts_prueba` y **DIFIERE** (rc = 1) frente a una copia con
    un valor numerico y uno booleano alterados. El control puede fallar.
  - Se corrigio un fallo del control con columnas booleanas antes de darlo por bueno.
- **Riesgo de cita equivocada (aclarado a la autora, 2026-09-14):** la unica fuente que llama "better" al recorte de
  3 mm es el README (no citable sin alta). `wasserthal2023` **no** menciona un recorte de 6 mm (ficha, 1g) y su "modelo
  de 3 mm" es otro: segmenta a 3 mm isotropicos y da **peor** Dice, *"The 3-mm model showed a lower Dice score of 0.840"*
  (Segmentation Evaluation, p. 4), frente a 0.943. `isensee2021` tampoco trata el recorte. **Citar cualquiera de los dos
  papers para "3 mm es mejor" seria un error de atribucion**, y con `wasserthal2023` diria lo contrario. Via posible:
  dar de alta la documentacion o cita del software (raw aportado por la autora) con version o fecha de consulta.
- **ACTUALIZACION 2026-09-14 — E9-TS con 3 mm CORRIDO (job 51529):** 152 casos, rc=0, 6 min 41 s.
  - **Repetibilidad frente a 51505: IDENTICO, 2352 filas x 43 columnas, tolerancia 0.** Las cifras con `robust3mm`
    de la ronda (4) quedan confirmadas por una segunda ejecucion completa.
  - **Cifras con 3 mm y F = 0.001** (la F decidida; en el Objetivo 2 identicas a F = 0), QC de nivel, 72 casos: mediana
    **9.35 mm** (IQR 7.75-11.7); el resumen redondea a 9.4. Viable a 10 mm **27 de 72**. `main.tex` debe usar la misma
    regla de redondeo en todas las cifras cuando se aplique el cambio.
  - **Densidad, seccion 5 del resumen** (3 mm, F = 0, todos los casos, sin QC): fraccion del eje <= 150 HU, mediana
    0.354 / 0.37 / 0.488 (grupos 1 / 2 / 3). Con QC en el Objetivo 2: 0.46 (ronda 4). Cilindro que toca metal en el
    grupo 1: 30 casos con 3 mm frente a 27 con 6 mm.
  - **Diferencias entre recortes en los corredores iliosacros** (Objetivo 2, F = 0.001): mediana 0.00 mm; |dif| >= 2 mm
    en 3 casos (izquierdo) y 1 (derecho); maximos `CLINIC_0001` derecho 4.7 mm y `CLINIC_0091` izquierdo 3.5 mm
    (8.5 -> 5.0 mm). En `D_TS` el maximo es 1.8 mm. `main.tex` no reporta corredores iliosacros; si llegara a hacerlo,
    esa incertidumbre es mayor que la de `D_TS`.
  - **Laminas revisadas por el asistente (3 de 152):** `CLINIC_0090` (9.6 mm) y `CLINIC_0101` (9.5 mm), los dos que
    cruzan 10 mm, y `CLINIC_0091` (2.5 mm; con 6 mm, 2.0). Sin fallo grosero visible en el corte coronal, que proyecta el
    eje y no permite juzgar la mascara. **149 laminas sin revisar.**
  - **Perfil con huecos:** en 20 de 72 casos, algun nivel da `D = 0` entre dos niveles con corredor (p. ej.
    `CLINIC_0090`, a -24 y -42 mm). Compatible con forámenes sacros que interrumpen el corredor; **sin verificar**. No
    cambia `D_TS` (maximo del perfil).
  - **E10b NO esta en la PC:** no hay `outputs/ts_cajas_limpias/`. Sigue sin verificarse que F = 0.001 elimine los 10
    desplazamientos de caja.
- **Para aplicar el cambio hace falta:** (1) ~~la corrida en Khipu con `IDENTICO`~~ (hecho, 51529) y revisar las laminas de 3 mm;
  (2) las fuentes de la autora en `refs/raw/` y `papers/`; (3) orden explicita para escribir la decision en
  `01-decisiones.md` y cambiar `main.tex` (Objetivo 2 y cifras del parrafo).
- **Tipo:** METODO / REDACCION. **Pendiente de la autora.**

### 49 — ACTUALIZACION 2026-09-14 (9): la preferencia por 3 mm se apoya solo en el README, y cambiar el principal ahora seria post hoc

- **Dato de la autora (2026-09-14):** eligio `robust3mm` basandose solo en el README de TotalSegmentator, que no es
  citable sin alta (#55).
- **Orden temporal:** "Recorte principal: default 6 mm" se decidio (`01-decisiones.md`, 2026-09-14) **antes** de correr
  E9-TS (51505) y de ver `D_TS`. Pasar a 3 mm despues de ver las cifras cambia el analisis principal post hoc: habria que
  declararlo, como ya se hizo con F y `ocupado_semimax`.
- **Los datos no piden el cambio:** mediana de `D(6) - D(3)` 0.0 mm; viables 27 (3 mm) frente a 29 (6 mm) de 72; 2 casos
  cruzan 10 mm. La propia decision dice que el de 3 mm "protege contra truncamientos que no aparecieron".
- **Buscar papers no se recomienda.** El modelo de recorte es un detalle de implementacion de una version del software.
  La unica fuente leida con un "modelo de 3 mm" (`wasserthal2023`) habla de otro modelo y le da peor Dice (0.840), y la
  literatura esta cerrada por saturacion.
- **Opciones:**
  - (a) mantener 6 mm como principal (pre-especificado, ya escrito en `main.tex`) y 3 mm como sensibilidad; se cierra la
    preferencia;
  - (b) pasar a 3 mm y declarar el cambio como post hoc, con su motivo;
  - (c) pasar a 3 mm solo si E10b o la revision de laminas muestran un fallo del recorte de 6 mm; el cambio lo motiva
    entonces un fallo observado.
- **Recomendacion del asistente:** (a), con (c) como condicion de reapertura. **Pendiente de la autora. No aplicado.**
- **DECIDIDA 2026-09-14 (4):** la autora elige (a). Registrada en `01-decisiones.md` por el asistente con orden
  explicita. `main.tex` ya decia "default crop; robust crop as sensitivity analysis": sin cambios.

### 49 — E10b LEIDO (2026-09-14, job 51527): F = 0.001 no elimina todos los desplazamientos de caja; cae la justificacion escrita de F, no el resultado del corredor — ABIERTA

- **Corrida:** n006, 8 min 5 s, rc = 0; 179 casos; 2864 filas + cabecera (meta 2865); el CSV de errores solo
  trae la cabecera. En `experiments/objetivo2/outputs/ts_cajas_limpias/`.
- **Control F = 0 frente a `ts_qc.csv`: 715 de 716.** La unica diferencia es `metal_0053` `vertebrae_S1`,
  vacia con los dos recortes (NaN en las dos columnas; ya documentada en `ts_cohorte.md`). El control vale.
  F = 0 reproduce exactamente los 10 casos / 11 estructuras de `ts_analisis.md`.
- **Estructuras con caja desplazada entre recortes, por F** (0 / 0.001 / 0.01 / 0.05):
  - > 10 mm: **11 / 4 / 1 / 1**;
  - > 5 mm: 17 / 10 / 9 / 9;
  - > 2 mm: 79 / 63 / 59 / 59;
  - mediana: 1.0 mm con toda F.
- **Con F = 0.001:**
  - 10 de las 11 originales bajan a <= 2.1 mm.
  - Queda `CLINIC_0022` sacro en 20.8 mm (78.2 con F = 0). Sus componentes de 596, 764 y 486 voxeles (fraccion
    0.00195-0.00307) solo se quitan con F = 0.01, que lo deja en 0.0.
  - **Aparecen 3 desplazamientos nuevos, creados por la propia limpieza:**
    - `metal_0015` S1: 0.8 -> 18.8 mm;
    - `metal_0025` S1: 1.6 -> 36.4 mm;
    - `CLINIC_0043` sacro: 1.6 -> 11.7 mm.
  - **Mecanismo de los nuevos:** un fragmento con fraccion cercana a F se quita en un recorte y no en el otro.
    - En `metal_0025`, con 3 mm se quitan 94 voxeles (componente de 70, fraccion 0.00095); con 6 mm, 148 voxeles,
      pero solo con F = 0.01.
    - En `metal_0015`, con 6 mm se quitan 8 voxeles; con 3 mm, un componente de 49 voxeles (fraccion 0.00312),
      pero solo con F = 0.01.
    - `CLINIC_0043` sigue en 11.7 mm con F = 0.05. Con 6 mm se quitan 248 voxeles y la caja pierde 10.7 mm en y;
      con 3 mm se quitan 150 y la caja no cambia. **Inferido, sin verificar en mascara:** esa region, que con 6 mm
      es un componente aparte, con 3 mm esta dentro del componente principal.
- **Que recorte origina las 11 originales** (el recorte cuya caja cambia al limpiar): 3 mm en 5, 6 mm en 4 y los dos
  en 2. No hay patron de fallo de un recorte ni de truncamiento.
- **Efecto sobre el corredor: ninguno.** En los 4 residuales, `D_TS` es identico para F en {0, 0.001, 0.01, 0.05},
  con los dos recortes y todas las politicas:
  - `CLINIC_0022`: 4.7 mm;
  - `CLINIC_0043`: 11.7 mm;
  - `metal_0015`: 7.4 / 8.3 mm (6 / 3 mm); `sin techo`, S1 en el borde del FOV;
  - `metal_0025`: 9.3 / 10.0 mm con `hueso`.
  `CLINIC_0022` y `CLINIC_0043` son del grupo 3 y concordantes de nivel. Coincide con lo que ya habia medido E9-TS.
- **Que cae:** la justificacion de la decision 2026-09-14 (3): *"0.001 es la menor probada que quita las islas de los
  10 desplazamientos de caja"*. Verificado: quita 10 de 11 estructuras, deja 1 y crea 3; ninguna F probada deja 0.
- **Que no cae:** la frase de `main.tex` *"Component cleaning changed no measurement in this cohort at any tested
  fraction up to 5%"* sigue siendo cierta y no afirma nada sobre cajas.
- **Opciones:**
  - (a) mantener F = 0.001 y reescribir la justificacion. La limpieza es higiene de mascara; `D_TS` y la viabilidad
    no dependen de F; los desplazamientos de caja entre recortes no desaparecen con ninguna F probada y se declaran.
  - (b) pasar a F = 0.01, que deja 1 residual. Seria la segunda eleccion post hoc del mismo parametro, y sin efecto
    sobre el resultado.
- **Recomendacion del asistente:** (a).
- **DECIDIDA 2026-09-14 (5):** la autora elige (a). Correccion escrita en `01-decisiones.md` por el asistente con
  orden explicita. `main.tex` sin cambios. Seccion CERRADA.
- **Relacion con el recorte:** E10b no muestra un fallo del recorte de 6 mm. La condicion de reapertura de la decision
  2026-09-14 (4) queda solo en la revision de laminas.

### 49 — Tablas versionadas y recalculo de `main.tex` (2026-09-15): 11 de 12 cifras coinciden; "changed no measurement" dice mas de lo medido — ABIERTA

- **Tablas copiadas** a `experiments/objetivo2/` por orden de la autora, con SHA256 identico al de `outputs/`:
  `e9ts_corredor.csv`, `e9ts_resumen.md`, `ts_cajas_limpias.csv` y `ts_cajas_limpias_control.csv`. Cierra el pendiente
  "Tablas citadas sin version" (ronda (5)) para el parrafo `Corridor measurement on the local cohort`.
- **`maintex_cifras.py`** rehace las 12 cifras de ese parrafo solo desde tablas versionadas (`e9ts_corredor.csv` y
  `grupos.csv`) y busca cada frase literal en `main.tex`. Escribe `maintex_cifras.md`. **11 de 12 coinciden**:
  103, 91, 72, 11 de 34, 7 de 57, 1 por FOV, 9.5 (7.4-11.7), 29 y 27 de 72, 0.42, 53.8 -> 40.4% en 52 y la misma
  proporcion con 2500 HU.
- **DIFIERE:** *"Component cleaning changed no measurement in this cohort at any tested fraction up to 5%"*.
  - En `CLINIC_0012` (grupo 3, 6 mm), `D_IS_izq_max_mm` pasa de 11.4 mm (F = 0) a 11.2 mm (F >= 0.001; 165 voxeles
    quitados).
  - `D_TS` (9.6 mm) y la viabilidad no cambian.
  - `main.tex` no reporta los corredores iliosacros.
- **Origen:** la frase se escribio en la ronda (6) desde la seccion 3 de `e9ts_resumen.md`, que solo compara `D_TS`. Es el
  patron vigilado: un enunciado mas amplio que el control que lo respalda. La decision 2026-09-14 (5) dice "`D_TS` y la
  viabilidad", y eso si es cierto.
- **Texto propuesto** (no aplicado, regla 4): *"Component cleaning changed neither the transsacral corridor diameter nor
  its 10~mm viability in this cohort at any tested fraction up to 5\%;"*. Si se aplica, hay que cambiar la frase 9 de
  `maintex_cifras.py` para que compruebe solo `D_TS` y la viabilidad.
- **Tipo:** REDACCION. **Pendiente de la autora.**

### 49 — Revision dirigida de laminas: plantilla lista (2026-09-15)

- `experiments/objetivo2/e9ts_revision_laminas_autora.csv` (16 casos: 14 con |D(6) - D(3)| >= 1 mm, mas `CLINIC_0022` y
  `CLINIC_0043` por E10b) y la guia `e9ts_revision_laminas.md`. Las columnas `veredicto` y `nota` las llena solo la autora.
- Un `fallo_6mm` activa la condicion de reapertura de la decision 2026-09-14 (4).

### 36 y 39 — E6b PREPARADO (2026-09-15): VAE de SD 1.5 sin reentrenar sobre los 178 CT; probado en local sin modelo — ABIERTA

- **Orden de la autora:** preparar E6b con los 178 volumenes (diseno minimo: solo 3 canales, sin reentrenar).
- **Scripts:** `experiments/objetivo1/e6b_vae_sd15.py` + `.sbatch`; comandos en `KHIPU.md`, seccion E6b.
- **Mide** `pub`, `LW20000` y `pub+asinh`. `pub+MTW` no se mide, porque sus 4 canales no entran en el VAE sin modificarlo.
- **Elecciones de medicion, declaradas en el script** (no son decisiones de la tesis):
  - pesos `stable-diffusion-v1-5/stable-diffusion-v1-5`, subcarpeta `vae` (repositorio publico, no restringido; API de
    Hugging Face consultada el 2026-09-14);
  - cortes axiales 2D a tamano nativo, latente = media de la posterior;
  - ROI y submuestreo de E6c;
  - dos decodificadores: `oraculo` (mejor canal con el HU verdadero, comparable con E6c) y `regla` (sin verdad: el canal
    mas estrecho no saturado, EPS = 0.01).
- **Supuesto a vigilar:** que "Stable Diffusion 1.5 backbone" implique este VAE es una inferencia (#36/#39). E6b mide ese
  candidato; no lo adopta.
- **Pruebas locales:**
  - identidad 12 de 12 frente a E6c; con un valor alterado da 11 de 12 (el control puede fallar);
  - `eco` 12 de 12 (tuberia de torch sin modelo);
  - relleno de lados no multiplos de 8 correcto.
  - **El VAE real no se probo en local** (sin `diffusers`): su primer uso es la prueba corta de 1 caso en Khipu.
- **Criterio de lectura, fijado antes de ver resultados:**
  - Si `vae regla` en hueso falla el umbral de 25 HU en una parte sustancial de los volumenes con las tres
    configuraciones, el VAE de SD 1.5 sin ajustar no pasa el Go/No-Go con ninguna ventana. La decision pasa a las
    opciones 2-4 de #36/#39.
  - Si pasa con `pub+asinh`, esa configuracion es viable con SD 1.5 tal cual, y queda por decidir si la ventaja de
    `pub+MTW` en E6c justifica adaptar el encoder.
- **Pendiente:** correr en Khipu. **Sin decision de la autora sobre #36/#39.**

### 49 — Texto de la limpieza APLICADO a `main.tex` (2026-09-15, orden explicita de la autora)

- `Corridor measurement on the local cohort`: "changed no measurement" pasa a *"changed neither the transsacral corridor
  diameter nor its 10~mm viability in this cohort at any tested fraction up to 5\%"*.
- `maintex_cifras.py`: la frase 9 ahora comprueba solo `D_TS` y la viabilidad, y el informe lista aparte las medidas que si
  cambian (`D_IS_izq_max_mm` en `CLINIC_0012`). Resultado: **12 de 12 cifras coinciden**.
- Compila: 4 paginas, 42 referencias, 0 citas indefinidas, los 2 avisos de BibTeX ya conocidos.
- La seccion "Tablas versionadas y recalculo" de #49 queda **CERRADA**.

### 53 — La autora decide: el revisor mira los 61 casos en ITK-SNAP (2026-09-15)

- **Decision (en el chat):** revision de los **61** casos con punto de S1, no solo de los 15. Asi no hace falta mezclar
  controles para no revelar los dudosos. Falta escribirla en `01-decisiones.md` (regla 3; texto propuesto en el chat).
- **Preparado:**
  - `experiments/objetivo2/r1_revision_itksnap_revisor.csv`: 61 filas desde `r1_cortes_itksnap.csv`; solo cortes desde 0
    y desde 1, mundo RAS/LPS y HU; columnas vacias `convencion_indices`, `HU_cursor`, `juicio_nivel`,
    `vertebra_transicion` y `comentario`;
  - `r1_revision_itksnap_revisor.md`: instrucciones. Las categorias son las del juicio sobre el mosaico (`ok`, `+1`,
    `otro`, `?`), para poder compararlas, y hay un campo nuevo de vertebra de transicion que responde al Hallazgo 1.
- **Ciega:** sin juicios del clinico, del agente ni de TS. El juicio nuevo va a una planilla aparte y no sobrescribe
  `r1_auditoria_s1_clinico.csv`.
- **Al volver:** comparar con el juicio sobre el mosaico y con TS, por categoria. Si cambia algun `ok`/`+1` de los 65,
  cambian las cifras 48/29 de `Field limitation` y el 57/57 de TS: revisar `main.tex` entonces.
- **Estado:** #53 sigue **ABIERTA** hasta recibir la planilla.
- **Decision escrita** en `01-decisiones.md` (2026-09-15) por el asistente, con orden explicita de la autora.
- **Frase "confirmed the S1 level on every patient" (2026-09-15):** la autora elige esperar el juicio en ITK-SNAP
  antes de aplicar el texto propuesto ("judged ... (undecidable in one)"). La frase sigue sin ser literal en
  `main.tex` hasta entonces. Se reescribe una sola vez junto con 48/29 y 57/57. **Pendiente.**

### 36 y 39 — E6b: prueba corta en Khipu (2026-09-15, job 51539) — primer uso del VAE real

- **Corrida:** ds001, RTX A6000; `metal_0000`; 182.8 s; control identidad frente a E6c **6 de 6**; rc = 0.
- **Unica cifra vista** (log; `pub`, hueso): identidad **156.57** HU, `vae oraculo` **222.67**, `vae regla` **291.16**.
  - Es un solo volumen, con metal, y con `pub`, que ya falla por el techo de LW. **No se interpreta** y no cambia el
    criterio de lectura fijado antes.
  - Solo confirma que el VAE agrega error medible sobre la cota de la ventana. Las configuraciones que importan
    (`LW20000`, `pub+asinh`) estan en el `.md` de la prueba, que no se ha leido.
- **Tiempo:** la cohorte se estima en ~8.8 h (60 595 cortes). Siguiente: lanzar la cohorte.

### Infraestructura — sin implicancia sobre la tesis

- Khipu (2026-09-14): g002 con RTX A6000 48 GB libre; `a-tesis` no limita `gres/gpu` (sin probar con
  `--test-only`); ag001 tiene ademas una A100 entera. E10 no usa GPU. Detalle en `KHIPU.md`. Relevante solo para
  E6b (#36/#39).

## Ronda 2026-09-15 (5) — lecturas de `zhang2025diffboost` y `jacob2026lgesynthnet`

### 56 — La frase de `main.tex:48` sobre los modelos de sintesis de lesiones no es fiel para DiffBoost, y para LGESynthNet solo en parte — ABIERTA

- **Origen:** fichas `zhang2025diffboost.md` y `jacob2026lgesynthnet.md`, hechas por `lector-papers` el 2026-09-15,
  ambas con PDF completo. **DiffBoost se releyo el mismo dia sobre la version publicada** (IEEE TMI
  44(9):3670-3682), porque la primera lectura se hizo sobre el preprint arXiv:2310.12868v2. Las citas se
  sostienen igual; abajo van las paginas de la revista.
- **Frase en riesgo** (`main.tex:48`): DiffTumor, DiffBoost, CLAIM y LGESynthNet *"are designed around bounded
  inpainting for deformable biological tissues. They implicitly assume non-rigidity and strictly restrict intensity
  alterations to the inside of the object's mask."*
- **Contraste por fuente** (evidencia textual en cada ficha):

  | Fuente | Inpainting acotado | No-rigidez | Cambios solo dentro de la mascara |
  |---|---|---|---|
  | `chen2024tumorsynthesis` | si (ficha previa) | no verificada en esta ronda | si: no modela nada fuera de la mascara (`_index.md`) |
  | `zhang2025diffboost` | **no**: genera la imagen entera desde ruido (Alg. 1, p. 3676); la mascara solo entra como borde (§III-C, p. 3674) | NO ENCONTRADO EN EL PDF; los bordes fijan la geometria y lo declara limitacion (§VI, p. 3680) | **no**: *"m · x_0 + (1 − m) · x_i"* (Alg. 1, p. 3676) |
  | `jacob2026lgesynthnet` | si: *"Formulated as inpainting using a ControlNet-based architecture"* (Abstract, p. 1) | NO ENCONTRADO EN EL PDF | sin respaldo: la imagen completa pasa por el latente, *"resulting in lower SSIM"* (Sec. 5, p. 8); no se describe reinsercion de pixeles |
  | `ramzan2026claim` | **sin ficha: no verificado** | — | — |

- **Por que importa:** esa frase es el argumento de que los modelos de lesiones *"structurally fail"* con metal, y es
  la motivacion de B_delta. Dos de las cuatro citas no dicen lo que se les atribuye, y una esta sin leer. Es una
  repregunta directa en la sustentacion y repite el patron de #25: un enunciado atribuido sin abrir el PDF.
- **Segundo hallazgo, sobre novedad (toca #6 y #9):** DiffBoost ya publica ControlNet sobre Stable Diffusion en imagen
  medica, y LGESynthNet combina LDM, ControlNet y mascara. "LDM + ControlNet sobre CT" no se sostiene como novedad
  si alguna frase lo presenta asi. La novedad queda en B_delta, en la codificacion multi-ventana en HU y en el metal.
- **Refuerzo, sin entrada nueva:** LGESynthNet atribuye a la compresion latente la perdida de SSIM en la imagen
  completa. Eso respalda medir la no-degradacion fuera de B_delta.
- **Opciones:**
  - **(a) Reescribir por familias.** Inpainting acotado (DiffTumor, LGESynthNet) frente a sintesis global condicionada
    (DiffBoost). Quitar "implicitly assume non-rigidity" y "strictly ... inside the mask" donde no haya cita.
    Borrador en ingles: *"condition generation on a bounded lesion mask and neither model nor supervise
    intensity changes beyond it, or synthesize the whole image under edge conditioning with no notion of
    object-induced artifacts"*.
  - **(b) Quitar DiffBoost de la lista** y leer CLAIM antes de mantenerlo en ella.
  - **(c) Pasar a una afirmacion cualitativa comun:** ninguno modela efectos inducidos por el objeto fuera de el.
    Las tres fichas leidas lo sostienen, pero hay que confirmarlo para CLAIM.
- **Recomendacion del asistente:** (a), leyendo antes `ramzan2026claim` con `lector-papers`, porque se cita en la
  misma frase.
- **Pendiente de:** decision de la autora. `main.tex` sin cambios (reglas 4 y 14).

**Pendiente de la autora (2026-09-15): verificar las citas contra el PDF.** De DiffBoost: Alg. 1 p. 3676, §III-C p. 3674
y §VI p. 3680. De LGESynthNet: Abstract p. 1 y Sec. 5 p. 8. Solo las verifico un agente, y son las que desmienten la frase.

**Correccion del segundo hallazgo (2026-09-15).** `main.tex:54` ya pone la novedad solo en C3 (multi-ventana para
*generacion* + B_delta) y dice *"The multi-window framework is not claimed as novel here"*. **No reclama ControlNet.** La
novedad no esta en riesgo y no hace falta cambiar texto por ese motivo. Mejora opcional: citar DiffBoost y LGESynthNet
como precedentes de ControlNet en imagen medica, para adelantarse a la pregunta.

**Recomendacion del asistente como asesor (2026-09-15), sustituye a la de arriba:**

1. **Leer `ramzan2026claim` antes de tocar el texto.** Cuesta una corrida de `lector-papers`, y evita reescribir dos
   veces una frase con cuatro citas. Reescribirla con una cita sin abrir repetiria el patron de #25.
2. **Elegir un hibrido: (c) como afirmacion central y una clausula de (a). Descartar (b).**
   - **La afirmacion tiene que ser causal, no espacial.** "Todo cambio queda dentro de la mascara" cae con un
     contraejemplo (DiffBoost ya lo es). "Ninguno condiciona sobre un objeto ajeno ni modela los efectos que ese objeto
     induce fuera de si" se sostiene en las tres fichas leidas. Ese es el gap real que motiva B_delta.
   - **Quitar "non-rigidity" del renderizador.** Ninguna fuente lo respalda, y la rigidez ya es argumento de C1, no del
     renderizador. Mezclarlos da una superficie de ataque sin ganar nada.
   - **No quitar DiffBoost (b).** Sacar el contraejemplo es seleccion a conveniencia, y es IEEE TMI 2025: el tribunal
     puede conocerlo. Citado bien, fortalece el argumento: aunque genera la imagen entera, no produce artefactos
     inducidos por un objeto, porque nada en su condicionamiento los describe.
   - **Una clausula de (a)** ("either by inpainting a bounded region ... or by synthesizing the whole image") basta para
     mostrar que se leyeron. No hace falta una taxonomia completa.
3. **Bajar los verbos que nada mide.** "structurally fail" (`main.tex:48`) y "cannot generate rigid global streaks"
   (`main.tex:54`) afirman un fracaso que ningun experimento de la tesis prueba: no se corrio ninguno de estos modelos
   sobre metal. Pasar a "are not designed to" / "do not model".
4. **Presentar B_delta como punto intermedio.** El inpainting acotado no llega fuera de la mascara, y la generacion
   global altera anatomia lejana (LGESynthNet atribuye al latente la perdida de SSIM en la imagen completa). B_delta
   extiende la region de forma acotada. **Este encuadre depende de #57.**
5. **Borrador en ingles, condicionado a CLAIM y a #57:** *"Diffusion-based lesion synthesis models such as DiffTumor,
   DiffBoost, CLAIM and LGESynthNet generate biological findings under mask, edge or text conditioning, either by
   inpainting a bounded region or by synthesizing the whole image. None of them conditions generation on a foreign
   object or models the effects such an object induces beyond its own boundary."*
6. **Prioridad:** por debajo de E6b (#36/#39 bloquea el Objetivo 1, que es obligatorio). Es texto, de una sola pasada
   una vez leido CLAIM.

### 57 — `main.tex` dice que los artefactos se propagan "globally far beyond" el implante, pero B_delta (~12 mm) y el titulo son locales — ABIERTA

- **Origen:** revision de `main.tex:48` y `main.tex:54` al asesorar #56 (2026-09-15). Sin lectura nueva.
- **Tension, con texto literal:**
  - `main.tex:48`: artefactos *"that propagate globally far beyond the implant's boundaries, destroying the signal of the
    surrounding soft tissue"*.
  - `main.tex:54`, C3: B_delta *"so that global streaking and beam hardening are modelled outside the metal itself"*.
  - `main.tex:77`: B_delta es una banda de *"$\sim$12mm"*.
  - `00-tesis.md:7`: el titulo habla de *"local metal artifacts"*. `CLAUDE.md` tambien dice "artefactos metalicos locales".
- **Por que importa:** si las estrias son globales, una banda de 12 mm no las contiene, y C3 promete modelar algo que su
  propio mecanismo recorta. Es contradiccion interna del documento, detectable sin leer ningun paper. Ademas, el valor de
  ~12 mm no tiene fuente: `01-decisiones.md` registra que B_delta no tiene precedente publicado. Este caso es mas grave
  que "sin precedente", porque tampoco hay una medicion propia que lo justifique.
- **Opciones:**
  - **(a) Declarar el alcance local.** Las estrias pueden extenderse lejos. La tesis modela solo la parte peri-implante,
    dentro de B_delta, y declara el campo lejano como limitacion. Cambia "global" en C3 por "peri-implant".
  - **(b) Justificar delta con una medicion.** Perfil de desviacion de HU frente a distancia al metal en CLINIC-metal. Ya
    hay heuristicas en disco sobre esferas de 12 mm (ver la revision de artefactos de #34). Solo seria util si el
    Objetivo 3 se ejecuta.
  - **(c) Tratar delta como parametro** con sensibilidad (p. ej. 6/12/24 mm) en el Objetivo 3.
  - **(d) Generar el corte entero.** Contradice el titulo local, se acerca a DiffBoost y arriesga degradar anatomia lejana.
- **Recomendacion del asistente:** (a) ya, porque es solo texto y cierra la contradiccion. Anadir (b) o (c) solo si el
  Objetivo 3 pasa de demostrativo a evaluado. No (d).
- **Pendiente de:** decision de la autora. `main.tex` y `00-tesis.md` sin cambios (regla 14).

## Ronda 2026-09-15 (7) — cohorte de E6b: el VAE de SD 1.5 sin reentrenar NO pasa el Go/No-Go

### 36 y 39 — E6b EJECUTADO en cohorte (job 51540): las tres configuraciones fallan en 178 de 178 volumenes — ABIERTA

- **Corrida:** job 51540, 178 volumenes, **0 errores** (`e6b_vae_sd15_errores.csv` solo cabecera), `rc = 0`,
  **control de identidad frente a E6c 873 de 873** (tolerancia 0.01 HU), mediana 180 s/volumen, 8.74 h.
  `e6b_vae_sd15.csv` tiene 179 filas (178 + cabecera). La integridad pedida en `ESTADO.md` se cumple entera.
  Salidas en `experiments/objetivo1/outputs/` y logs en `outputs/e6b/`.
- **Criterio de lectura fijado ANTES de ver resultados** (bloque "E6b PREPARADO", 2026-09-15): si `vae regla` en
  hueso falla el umbral de 25 HU en una parte sustancial de los volumenes con las tres configuraciones, el VAE de
  SD 1.5 sin ajustar no pasa el Go/No-Go con ninguna ventana, y la decision pasa a las opciones 2-4.
- **Resultado, contra ese criterio:** no es "una parte sustancial", es **todo**. Go/No-Go en hueso (MAE >= 25 HU):

  | Configuracion | identidad oraculo | identidad regla | vae oraculo | vae regla |
  |---|---|---|---|---|
  | `pub` | 50/178 | 50/178 | **178/178** | **178/178** |
  | `LW20000` | 0/178 | 0/178 | **178/178** | **178/178** |
  | `pub+asinh` | 0/178 | 0/178 | **178/178** | **178/178** |

- **Margen:** el mejor volumen de la mejor combinacion (`pub`, `vae oraculo`) da **52.85 HU**, mas del doble del
  umbral. `pub+asinh` con `vae regla`, que es la tuberia real, va de **99.10** (min) a **368.85** (max), mediana
  **162.95** HU. No hay ningun volumen que pase con ninguna ventana y ningun decodificador.
- **Medianas en hueso (HU), sobre los 178:**

  | Configuracion | identidad regla | vae oraculo | vae regla | E6c 8b (referencia) |
  |---|---|---|---|---|
  | `pub` | 0.94 | 84.86 | 152.05 | 2.18 |
  | `LW20000` | 0.00 | 122.22 | 212.00 | 6.24 |
  | `pub+asinh` | 0.00 | 100.20 | 162.95 | 2.07 |

- **Lo que esto separa, y es el hallazgo de fondo:** la **codificacion en ventanas** (#39) y el **autoencoder** (#36)
  son dos perdidas de escala distinta. `LW20000` y `pub+asinh` tienen identidad **0.00 HU**: como codificacion son
  exactas. El VAE de SD 1.5 les agrega **162-212 HU** de mediana. El error de la ventana, que era el tema de E6c
  (1-6 HU a 8 bits), es **dos ordenes de magnitud menor** que el del autoencoder. **Elegir ventana no arregla el
  Objetivo 1 mientras el VAE sea este.**
- **Inversion respecto de E6c, a vigilar:** en E6c `LW20000` era la peor a 8 bits (6.24 HU) y `pub` la mejor tras
  `pub+MTW`; con el VAE el orden se mantiene pero las distancias cambian de signo practico: `pub` tiene el **menor**
  error de VAE (84.86 oraculo) pese a ser la unica que falla la identidad (50/178, techo de 2000 HU, #39). Lectura
  plausible, **no verificada**: las ventanas que preservan HU exactos estiran un rango dinamico mucho mayor sobre el
  mismo soporte normalizado, asi que cada unidad de error del latente cuesta mas HU. No hay medicion que lo pruebe:
  si la decision se apoya en esto, hay que medirlo.
- **Metal:** ninguna configuracion se acerca. `LW20000` es la menos mala (2695 HU con oraculo, 4145 con regla) frente
  a identidad 0.00. `pub` parte ya de 3588.80 HU por el techo. El metal no es el criterio del Go/No-Go, pero confirma
  que el latente de SD 1.5 no transporta el rango del implante.
- **`oraculo` frente a `regla`:** el oraculo usa el HU verdadero para elegir canal y es una **cota inferior**, no una
  tuberia. Aun asi falla 178/178. Que la cota falle cierra la discusion: no es un problema de la regla de seleccion.
- **`pub+MTW` sigue sin medirse:** sus 4 canales no entran en el VAE de SD 1.5 sin modificarlo. E6b no dice nada
  sobre la opcion 2 (encoder adaptado a 4 canales) mas alla de que el VAE base, con 3 canales, ya falla.
- **Consecuencia para las opciones de #36/#39:**
  - **Opcion 1 (SD 1.5 con tres ventanas y `asinh`): queda descartada por evidencia propia**, con el criterio
    preinscrito. Es el resultado mas fuerte de la sesion.
  - **Opcion 2 (primera capa a 4 canales, reentrenamiento parcial):** no la rescata por si sola. El error medido no
    viene del numero de canales sino del latente; adaptar la entrada sin tocar el resto tiene poca razon para bajar
    de 160 HU a menos de 25.
  - **Opcion 3 (otro VAE):** pasa a ser la via principal, y ahora con un requisito numerico: reconstruccion de hueso
    por debajo de 25 HU de MAE. Candidatos tipicos son VAE de CT entrenados en HU o autoencoders con factor de
    compresion menor. **Ninguno leido ni verificado.**
  - **Opcion 4 (metal fuera del espacio latente):** no la toca este experimento, porque el fallo esta en el **hueso**,
    fuera de la mascara de metal. Componer el metal aparte deja el problema intacto.
  - **Opcion 5, nueva:** revisar el propio umbral de 25 HU del Go/No-Go. Ningun modelo latente publicado reporta
    fidelidad de HU a ese nivel, y el umbral lo fijo la tesis sin fuente. **No es una salida por resultado adverso
    si se justifica con bibliografia**; si se baja solo para aprobar, repite el patron #25/#37/#45/#47/#50 que
    `ESTADO.md` manda vigilar.
- **Lo que este experimento NO dice:** no mide calidad perceptual ni utilidad para difusion. Un VAE puede fallar una
  MAE de HU y aun servir para generar imagenes plausibles. El Go/No-Go de la tesis, tal como esta escrito, es de
  fidelidad en HU; si esa es la pregunta correcta es una decision, no un dato.
- **Que seccion toca:** Objetivo 1 (Go/No-Go y su umbral), Objetivo 3 (`Stable Diffusion 1.5 backbone` en
  `main.tex`), C3 (codificacion multi-ventana), `03-glosario.md`.
- **Tipo:** DISENO / RIESGO. **Pendiente de la autora. `main.tex` y `00-tesis.md` sin cambios (regla 14).**

### 36 y 39 — El umbral de 25 HU SI tiene con que anclarse, pero la metrica de E6b no es la que publica el campo (MAE frente a RMSE) — ABIERTA

- **Origen:** busqueda de respaldo bibliografico para la opcion 5 (revisar el umbral) y para la opcion 3 (otro VAE),
  hecha el 2026-09-15 **solo sobre fichas ya escritas**. No se leyo ningun PDF nuevo ni se busco fuera del corpus.

**Hallazgo 1 — la metrica tiene precedente directo, incluido el baseline de la tesis.**

| Fuente | Definicion literal | Donde |
|---|---|---|
| `peters2025hybrid` (baseline, #8) | *"assessed as the voxel-wise root-mean square error (RMSE) between the ground truth and the MAR image"* | 2.5, p. 5 |
| `haneda2025aapm` | *"defined as the root-mean-square error (RMSE) between the ground truth and the MAR image"* | Sec. 2.3, p. 6 |

  Las dos llaman a eso *CT number accuracy* y las dos umbralizan hueso en 150 HU (*"all voxels with a CT number
  above 150 HU ... were considered bone"*, Peters 2.5 p. 5; Haneda Sec. 2.3 p. 7), que es el mismo umbral de hueso
  que ya usa E6b/E6c. **La familia de metrica y el ROI de hueso estan respaldados.**

- **Pero E6b reporta MAE, no RMSE.** Son metricas distintas y RMSE >= MAE siempre. Citar 12.74 o 20.2 HU de la
  literatura al lado de los 162.95 HU de E6b **no es comparacion valida de frente**. En este caso no cambia la
  conclusion (el margen es de un orden de magnitud), pero **si la autora quiere citar esas cifras, E6b tiene que
  reportar RMSE**. El CSV actual solo guarda MAE: hace falta rehacer la corrida (~8.7 h) o guardar las dos.

**Hallazgo 2 — no existe en el corpus un umbral absoluto publicado de "pasa/no pasa" en HU.** Lo que hay es una
  escala normalizada 0-4 *"calibrated by assigning a score of 2 to the popular NMAR algorithm"* (`haneda2025aapm`,
  Sec. 2.3, p. 6). El campo ancla en un metodo de referencia, no en un numero de HU. **El 25 HU de la tesis sigue
  sin fuente directa**, como dice la opcion 5.

**Hallazgo 3 — hay magnitudes publicadas que encuadran el 25 HU, y lo dejan en un lugar razonable.**

| Metodo | Cifra en HU | Fuente |
|---|---|---|
| NMAR (ancla de la escala AAPM) | RMSE 20.2 (σ=19.7) | `karageorgos2024ddpm`, Tabla I, p. 28 |
| DDPM en imagen | RMSE 12.3 (σ=10.4) | `karageorgos2024ddpm`, Tabla I, p. 28 |
| DDPM, pelvis (Paciente 1) | RMSE_INT 11, RMSE_ROI 20 | `karageorgos2024ddpm`, Tabla II, p. 29 |
| DDPM, protesis total de cadera (Paciente 4) | RMSE_INT 147 | `karageorgos2024ddpm`, Tabla II, p. 29 |
| MLD-MAR (**latente**, CVQ-VAE x4) | RMSE 12.74 (σ=5.36) sintetico | `yun2026simulationdriven`, Tabla 1, p. 10 |
| MLD-MAR, ROI clinico libre de artefacto | RMSE 21.01; sesgo HU medio 0.82 | `yun2026simulationdriven`, Tablas 3 y 4, p. 11 |

  **Lectura:** 25 HU cae justo por encima de donde aterriza NMAR (20.2), el metodo que el campo usa como ancla, y a
  unas dos veces el mejor latente publicado (12.74). **No es un umbral arbitrario ni inalcanzable**, y se puede
  defender por comparacion con fuentes que la autora ya tiene leidas. Esto **desactiva en gran parte la opcion 5**:
  el umbral no necesita bajarse, necesita justificarse.
  - **Aviso de honestidad:** todas esas cifras son de **MAR** (quitar artefacto), no de ida y vuelta de un
    autoencoder, y son RMSE sobre tuberia completa. Sirven como **orden de magnitud citable**, no como equivalencia.
    Presentarlas como si midieran lo mismo que E6b repetiria el patron #25/#47/#50.

**Hallazgo 4 — alternativa de formulacion, tambien del baseline.** `peters2025hybrid` valida con un criterio
  **relativo**: *"the mean CT number deviation between simulation and real data was less than 2%"* (Abstract, p. 1).
  Un umbral relativo en vez de absoluto es una opcion de diseno abierta para el Go/No-Go, y viene del mismo paper
  que la tesis ya adopto como baseline.

**Hallazgo 5 — candidato de VAE con cifra de HU medida: uno solo, y es indirecto.** `yun2026simulationdriven`
  (MLD-MAR) es LDM sobre CT con metal y usa *"× 4 down-sampled latent representations"* (Sec. 2.3.1, p. 4) de un
  **CVQ-VAE** (Zheng y Vedaldi 2023, ref. 23). Factor de compresion 4 frente al 8 de SD 1.5: razon mecanica para
  esperar menos perdida, coherente con lo que midio E6b.
  - **No es fidelidad de autoencoder verificada:** 12.74 HU es la tuberia entera contra ground truth. Que el error
    de ida y vuelta del CVQ-VAE sea menor que eso es **inferencia del asistente, no una medicion publicada**. La
    unica forma de saberlo es correr E6b con ese autoencoder.
  - `chen2024tumorsynthesis` (VQGAN 3D, 9.262 CT, latente 1/4 en las tres dimensiones) es el otro candidato de
    arquitectura, pero **no publica cifra de fidelidad en HU** y su ficha ya advierte que el autoencoder nunca vio
    el rango del metal.
  - Los tres candidatos estan en `_candidatos.md`, seccion "Candidatos de AUTOENCODER" (2026-09-15).

**Hallazgo 6 — el hueco real.** Ninguna fuente del corpus mide el error de ida y vuelta de un autoencoder solo, en
  HU, sobre CT oseo. E6b si lo hace. Eso es a la vez el motivo de que no haya con que compararlo **y** una
  contribucion metodologica menor que la tesis puede reclamar, si la autora quiere.

- **Que seccion toca:** Objetivo 1 (definicion y umbral del Go/No-Go), Related Work, `03-glosario.md`.
- **Tipo:** RIESGO / GAP. **Pendiente de la autora. Nada aplicado (reglas 3 y 14).**
- **Recomendacion del asistente:** (i) mantener 25 HU y justificarlo contra NMAR = 20.2 y MLD-MAR = 12.74, no
  bajarlo; (ii) antes de citar esas cifras, hacer que E6b reporte **RMSE ademas de MAE**; (iii) para la opcion 3,
  el candidato a probar primero es el CVQ-VAE de MLD-MAR, reusando E6b tal cual.

### 36 y 39 — Busqueda web autorizada: el hueco se confirma, y aparece un paper que responde lo contrario que E6b — ABIERTA

- **Origen:** busqueda web del 2026-09-15, **con orden explicita de la autora**. Es una excepcion declarada al flujo
  `refs/raw` -> `clean` -> `refs.bib`. Nada entro a `refs.bib`; las tres filas estan en `_candidatos.md`, seccion
  "Busqueda WEB", marcadas SIN VERIFICAR. Ninguna cifra de esta busqueda se uso en `main.tex`.

- **Hallazgo 1 — el hueco es real, y ahora esta comprobado por fuera.** No aparecio ningun trabajo que publique el
  error de ida y vuelta de un autoencoder **solo**, en HU, sobre CT oseo con rango de metal. Lo confirma por la
  negativa el benchmark del campo, DM4CT (arXiv:2602.18589): no separa la primera etapa de la tuberia y declara
  *"we do not use Hounsfield Unit for display, as the benchmark is not intended for clinical analysis"*. **El
  benchmark de referencia no mide lo que mide E6b.** Refuerza que E6b es contribucion metodologica menor propia.

- **Hallazgo 2, el importante — hay un paper que hace la pregunta de E6b y le da la respuesta CONTRARIA.**
  *Foundation VAEs for 3D CT Reconstruction, Augmentation, and Generation* (ICML 2026, arXiv:2605.30893) transfiere
  **siete VAE de video genericos y congelados** a CT *"without medical fine-tuning"*, y lo presenta como resultado
  positivo. E6b concluye que un VAE generico sin reentrenar no sirve. **Las dos cosas pueden ser ciertas a la vez**,
  y la razon esta en el rango: ellos recortan a **[-1000, 1000] HU**, que **deja fuera el hueso denso y todo el
  metal**; el Objetivo 1 vive justo en el rango que ellos descartan. Si esa lectura se confirma al leer el PDF, deja
  de ser una contradiccion y pasa a ser **el mejor argumento disponible a favor del encuadre de la tesis**: el
  problema no es el CT, es el rango extendido que exige el metal.
  - **Riesgo simetrico:** si NO se confirma, es un paper de ICML 2026 que contradice de frente la conclusion de E6b,
    y la tesis tiene que responderlo. Es repregunta segura en la sustentacion.
  - **Sin verificar.** Las cifras vistas (PSNR 30.93 pulmon / 39.18 pancreas; MSE 77.97 / 8.58, unidad sin
    confirmar; compresion 8x8x4 y 16x16x4) vienen del HTML, no de una lectura con `lector-papers`.
  - **Accion recomendada:** es la lectura de prioridad 1. Lo que hay que verificar es solo el rango de recorte y si
    alguna cifra esta en HU.

- **Hallazgo 3 — donde si se publica MAE en HU por tejido.** El subcampo de sCT en radioterapia MR-only reporta MAE
  en HU con ROI de hueso separado, que es exactamente la metrica de E6b. **No se uso como ancla y no debe usarse:**
  la tarea es sintesis MR -> CT, mucho mas dificil que una ida y vuelta, y las magnitudes que se ven en los
  resumenes son de cientos de HU en hueso. Usarlas para decir que "25 HU es exigente" seria inflar el argumento con
  una tarea ajena. Valor legitimo: la **convencion de reporte** (MAE en HU, desglosado por tejido).

- **Que seccion toca:** Objetivo 1, Related Work (el paper de ICML obliga a posicionarse), `_candidatos.md`.
- **Tipo:** GAP / RIESGO. **Pendiente de la autora. Nada aplicado a `main.tex` por esta busqueda.**

### 36 y 39 — El umbral de 25 HU queda ANCLADO Y CITADO en `main.tex` (2026-09-15, orden explicita de la autora)

- **Decision de la autora:** mantener 25 HU y hacer que el texto cite las fuentes que lo sostienen. Escrita en
  `01-decisiones.md` (2026-09-15 (2)) por el asistente, con orden explicita.
- **Aplicado a `main.tex`**, en los dos sitios donde vivia la cifra:
  - **Objetivo 1 (l. 75):** el ROI de hueso queda declarado sobre el mismo umbral de 150 HU del protocolo adoptado
    (`peters2025hybrid`, `haneda2025aapm`); se declara que **no existe umbral publicado de pasa/no-pasa**; y el 25 HU
    se ancla en NMAR 20.2 HU, difusion en imagen 12.3 HU (`karageorgos2024ddpm`) y difusion latente 12.74 HU
    (`yun2026simulationdriven`).
  - **Tabla de metricas, fila `Representation Viability` (l. 98):** misma ancla en version corta.
- **La discrepancia de metrica se declara en el propio texto**, no se esconde: las cifras citadas son RMSE, el
  criterio es MAE, y RMSE nunca queda por debajo de MAE para los mismos residuos, asi que la comparacion fija el
  orden de magnitud y no una equivalencia. Esto era el riesgo principal de la edicion y queda visible en el PDF.
- **Compila:** 4 paginas, 42 referencias, 0 citas indefinidas. **`refs.bib` sin cambios**: las cuatro claves ya
  estaban (regla 9 respetada, no se anadio ninguna entrada).
- **Pendiente tecnico que queda abierto:** hacer que E6b reporte **RMSE ademas de MAE** para que la comparacion deje
  de ser de orden de magnitud. Exige rehacer la corrida (~8.7 h); el CSV actual solo guarda MAE.
- **Efecto sobre la opcion 5 de #36/#39:** queda **cerrada en la practica**. El umbral no se baja; se justifica.

## Ronda 2026-09-15 (9) — verificacion de `chen2023foundation` y E6b con RMSE

### Bibliografia — `papers/chen2023foundation.pdf` ES el paper correcto; lo que esta mal es la clave — sin implicancia sobre el argumento

- **Duda de la autora:** que el PDF subido como `chen2023foundation` fuera en realidad el mismo que
  `chen2024tumorsynthesis` ("Towards Generalizable Tumor Synthesis").
- **Verificado el 2026-09-15** por metadatos y primera pagina (`pdfinfo` y `pdftotext`, sin lectura de contenido;
  la lectura de literatura sigue pendiente y va por `lector-papers`, regla 10):

  | Archivo | Titulo real | Identificador | Venue |
  |---|---|---|---|
  | `papers/chen2023foundation.pdf` | *Foundation VAEs for 3D CT Reconstruction, Augmentation, and Generation* | arXiv:2605.30893v1, 29 May 2026 | ICML 2026, PMLR 306, Seul |
  | `papers/chen2024tumorsynthesis.pdf` | *Towards Generalizable Tumor Synthesis* | arXiv:2402.19470v2, 28 Mar 2024 | CVPR 2024, pp. 11147-11158 |

- **Conclusion: son dos papers distintos y el subido es el correcto.** La confusion es razonable porque comparten
  autores (Qi Chen, Alan Yuille, Zongwei Zhou en los dos) y porque los dos abren con la formula *"makes a
  progressive stride toward ..."*.
- **Lo que si esta mal es la clave:** `chen2023foundation` dice **2023** y el paper es de **2026**. Ademas no hay
  `refs/raw/chen2023foundation.*`, asi que la entrada no existe en `refs.bib` (regla 9: empieza por pegar el archivo
  en `refs/raw/`). **Pendiente de la autora:** renombrar el PDF a la clave definitiva y pegar el raw. Sugerencia de
  clave, no aplicada: `chen2026foundationvae`.
- **Sin implicancia sobre el argumento de la tesis.** La relevancia del paper ya esta registrada en la ronda (8).
  Lo que hay que verificar al leerlo sigue siendo el recorte de intensidad a [-1000, 1000] HU.

### 36 y 39 — E6b reporta ahora RMSE ademas de MAE, y la diferencia NO es cosmetica — ABIERTA

- **Orden de la autora (2026-09-15):** cerrar el pendiente tecnico de la decision 2026-09-15 (2).
- **Implementado** en `experiments/objetivo1/e6b_vae_sd15.py`:
  - las dos metricas se calculan sobre **el mismo vector de errores absolutos por voxel**;
  - la columna de MAE **conserva su nombre sin sufijo** y la de RMSE anade ` rmse`. Asi el control contra
    `e6c_techo_lw.csv` y las corridas anteriores siguen leyendose;
  - el oraculo sigue eligiendo canal por **menor error absoluto**; no se re-optimiza para RMSE. Si se
    re-optimizara, su RMSE seria menor. Declarado en el docstring, no corregido;
  - el `.md` trae tablas de las dos metricas y una fila de Go/No-Go por metrica, con aviso de que **el criterio de
    la tesis sigue siendo MAE**;
  - `--solo-resumen` sobre un CSV viejo sale solo con MAE y lo avisa.
- **Verificacion local** (`--vae identidad`, sin torch, 2 volumenes): control frente a E6c **12 de 12**; RMSE >= MAE
  en los **24** pares comparados, 0 violaciones; el CSV pasa de 32 a **56** columnas. Regenerado el informe de la
  cohorte vieja: control **873 de 873** y tablas de MAE **identicas** a las publicadas. No hay regresion.
- **Hallazgo que aparece solo: para `pub`, cambiar de MAE a RMSE cambia el resultado.** En los 2 volumenes de
  prueba, `pub` identidad en hueso da **MAE 2.02 frente a RMSE 53.30** de mediana (en `metal_0008`, 3.88 frente a
  90.34). El techo de 2000 HU satura unos pocos voxeles con error enorme: **MAE lo diluye y RMSE lo expone.**
  - `LW20000` y `pub+asinh` dan **0.00 en las dos metricas**, porque su identidad es exacta. Ahi no cambia nada.
  - **Consecuencia:** si la tesis pasara el Go/No-Go a RMSE, `pub` empeoraria mucho (hoy falla 50/178 por MAE) y las
    otras dos configuraciones no se moverian. Es decir, **la eleccion de metrica no es neutral: penaliza justo a la
    configuracion con techo**, que es el tema de #39.
  - **Cautela:** son **2 volumenes**, no la cohorte, y solo identidad (sin VAE). No se interpreta mas alla de esto.
    La cifra buena sale de la corrida completa.
- **Lo que NO cambia:** el criterio del Go/No-Go sigue siendo MAE < 25 HU, como quedo escrito en `main.tex` y en la
  decision 2026-09-15 (2). Este cambio solo **anade** la metrica que permite comparar con la literatura.
- **Falta correr la cohorte de nuevo** (~8.8 h en Khipu): el CSV anterior no tiene las columnas `rmse` y no se
  pueden reconstruir sin volver a pasar los volumenes por el VAE. Comandos sin cambio en `KHIPU.md`, seccion E6b,
  donde ya esta anotada la version nueva.
- **Que seccion toca:** Objetivo 1. **Tipo:** DISENO. **Pendiente:** correr la cohorte; despues, la autora decide si
  la comparacion con la literatura se hace en RMSE.

### Proceso — relanzar E6b con el CSV viejo en su sitio produce un falso exito (2026-09-15)

- **Riesgo detectado al preparar la relanzada**, no en una corrida real. `e6b_vae_sd15.py` es reanudable: lee los
  `Caso` ya escritos y los salta. Con el CSV de la corrida MAE en `data/e6b/`, un `sbatch` nuevo **salta los 178
  volumenes, no mide nada, rehace el informe solo con MAE y termina con `rc = 0`**. El control de identidad contra
  E6c seguiria dando **873 de 873**, porque valida el CSV viejo.
- **Es el patron que `ESTADO.md` manda vigilar** (#25, #37, #40, #45, #47, #50): un control que no puede fallar
  tomado por verificacion. Aqui el control pasa justamente porque no se midio nada nuevo.
- **Mitigacion escrita en `KHIPU.md`** (seccion "Relanzar la cohorte con la version de RMSE"): apartar
  `data/e6b` antes de lanzar, comprobar `grep -c SUF_RMSE` en el script subido, exigir **56 columnas** en el CSV y
  que la linea de log traiga el tramo `| RMSE regla`. El numero de columnas es el unico control que distingue las
  dos versiones: el de identidad no.
- **Sin implicancia sobre el argumento de la tesis.** Se registra por la regla 17 y porque el mismo patron ya costo
  caro cinco veces.

### Bibliografia — `chen2026foundationvae`: el raw tiene tres defectos, ninguno bloqueante (2026-09-15)

- La autora renombro el PDF y pego el raw. Verificado contra el archivo:
  1. **URL rota:** `url={httpsarxiv.orgabs2605.30893}`, sin `://` ni `/`. Artefacto de copiar de arXiv. **No se
     toca el raw** (regla 9); se resuelve en `refs/clean/`, omitiendo el campo o marcando `% VERIFICAR`.
  2. **Clave distinta del nombre de archivo:** el raw declara `chen2026foundationvaes3dct`, el archivo es
     `chen2026foundationvae.bib`. Hay que elegir una.
  3. **`@misc` de arXiv, pero el paper esta publicado** en ICML 2026 (PMLR 306), segun su primera pagina. El raw
     solo respalda el preprint. **Mismo caso que `isensee2021`.**
- **No bloquea nada:** la entrada no esta en `refs.bib` (0 ocurrencias) y `main.tex` no la cita.
- **Pendiente de la autora:** elegir clave y decidir si se cita el preprint (con lo que hay) o se consigue el raw
  de PMLR para citar la version publicada.

### Bibliografia — `chen2026foundationvae` DADA DE ALTA, y `\nocite{*}` la mete en la bibliografia sin citarla (2026-09-15)

- **Orden de la autora:** dar de alta el `clean/` y regenerar `refs.bib`. Hecho:
  `refs/clean/chen2026foundationvae.bib` -> `python scripts/build_refs.py` -> **43 entradas**. `MAPEO.md` con
  su fila de procedencia y una nota propia.
- **Normalizacion aplicada:** clave de la autora (la del editor, `chen2026foundationvaes3dct`, se descarta por la
  regla 1); autores en `Apellido, Nombre`; titulo en `{{...}}`; `url` descartado por la regla 7 **y ademas venia
  roto** en el raw. `eprint`, `archivePrefix` y `primaryClass` **se conservan como excepcion declarada** a la regla
  7: en las demas entradas sobraban porque habia DOI o revista, aqui son el unico localizador del raw.
- **Es la primera entrada `@misc` del repositorio.** Las 42 anteriores son 35 `@article` y 7 `@inproceedings`. Es
  tambien la primera que cita un preprint teniendo version publicada (ICML 2026, PMLR 306), igual que paso con
  `isensee2021`. Se cita el preprint porque es lo unico que respalda el raw. **Pendiente de la autora:** si quiere
  la version publicada, hay que pegar el raw de PMLR.
- **Efecto no obvio, y por eso se registra:** `main.tex:139` tiene **`\nocite{*}`**, asi que **toda** entrada de
  `refs.bib` entra en la bibliografia del PDF aunque no se cite en el texto. Dar de alta esta entrada subio el
  documento de **42 a 43 referencias** sin que ninguna frase la cite. Compila: 4 paginas, 0 citas indefinidas.
  - Es el comportamiento buscado (el comentario de `main.tex:137` lo declara), pero conviene tenerlo presente:
    **cada alta en `refs.bib` cambia el conteo de referencias del PDF**, y ese conteo se usa como control de
    compilacion en `ESTADO.md`. `ESTADO.md` actualizado a 43.
  - Si en la revision final se prefiere que la bibliografia liste solo lo citado, hay que quitar `\nocite{*}`.
    **No se toca sin orden** (regla 14).
- **Sin implicancia sobre el argumento.** El paper sigue sin leerse; su relevancia esta en la ronda (8).

### Correccion — `chen2026foundationvae` frente a `isensee2021`: es el caso ESPEJO, no el mismo (2026-09-15)

- **Corrige** dos entradas de hoy (ronda (9) y el alta de la referencia), donde el asistente escribio "mismo caso
  que `isensee2021`". Es inexacto y se corrige aqui y en `MAPEO.md`.

  | | `isensee2021` | `chen2026foundationvae` |
  |---|---|---|
  | `refs/raw/` | Nature Methods 2021, PMID 33288961 → **publicada** | arXiv 2605.30893 → **preprint** |
  | `papers/*.pdf` | era el **preprint** arXiv 2020 | lleva el pie de ICML 2026 |
  | Estado | resuelto (la autora subio el PDF de Nature Methods) | **sin resolver** |

- En nnU-Net el riesgo era **citar paginas de una version leyendo otra**, que es lo que rompe las fichas. Aqui el
  riesgo es **citar como preprint algo revisado por pares**. Lo comun es la leccion: `raw/`, `papers/` y `refs.bib`
  tienen que apuntar a la misma version.
- **Aviso de evidencia:** el numero de volumen **`PMLR 306` sale unicamente del pie de la primera pagina del PDF**
  (*"Proceedings of the 43 rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026."*).
  La pagina de PMLR no se encontro al buscar el 2026-09-15. La aceptacion en ICML 2026 si tiene dos respaldos
  independientes (pagina de poster de `icml.cc` y el repositorio de los autores), **el volumen no**. Si esa cifra se
  usa alguna vez, hay que confirmarla contra el editor: es justo el patron #25/#37/#45/#47/#50, un dato que se
  vuelve verdad por repetirse.
- **Sin implicancia sobre el argumento de la tesis.** `main.tex` no cita esta entrada.
- **Pendiente de la autora:** elegir version de referencia **antes** de mandar el paper a `lector-papers`, para que
  la ficha cite paginas de la version que se va a citar.

## Ronda 2026-09-15 (10) — 4 lecturas nuevas: `gertzbein1990`, `ramzan2026claim`, `herman2016`, `deman1999`

> Seleccion del asistente sobre los 24 PDF de `papers/` sin ficha, por probabilidad de mover el
> argumento. Las cuatro fichas las hizo `lector-papers` (regla 10), cada una con PDF completo.
> `main.tex`, `00-tesis.md` y `01-decisiones.md` sin tocar (reglas 4 y 14).

### 56 — CERRADA EN EVIDENCIA por la lectura de CLAIM: la fila que faltaba ya esta, y el veredicto cambia de "dos de cuatro" a "el atributo del medio no lo dice NADIE" — sigue ABIERTA en decision

- **Origen:** ficha `ramzan2026claim.md`, `lector-papers`, 2026-09-15, PDF completo. Completa la tabla de #56,
  cuya ultima fila decia *"sin ficha: no verificado"*.
- **CLAIM, por atributo:**

  | Atributo | Veredicto | Evidencia textual |
  |---|---|---|
  | Inpainting acotado | **RESPALDA**, y es el caso mas fuerte de los cuatro | perdida enmascarada, Ec. 1, p. 4: *"to ensure that the diffusion model operates only on manipulating the specified scar regions"* |
  | Cambios solo dentro de la mascara | **RESPALDA, con formula literal** | Sec. 2.1, p. 5: `x^_{N_{t-1}} = o_{N_{t-1}} (.) M_f + x_{N_{t-1}} (.) (1-M_f)`, mas *"The background mask (1-Mf) is applied ... to preserve the non-lesion regions."* Es exactamente `m*generado + (1-m)*original` |
  | No-rigidez | **NO RESPALDA. NO ENCONTRADO EN EL PDF** | *"non-rigid"* aparece solo como metodo de REGISTRO dentro de SMILE (p. 6: *"non-rigid registration (i.e. fast symmetric forces demons method)"*), para warpear mascaras plantilla<->sujeto. Es el muestreador, no el renderizador |

- **Tabla consolidada de #56, ya con las cuatro fuentes leidas:**

  | Atributo de la frase | Lo respalda | No lo respalda |
  |---|---|---|
  | *"bounded inpainting"* | DiffTumor, LGESynthNet, CLAIM (**3 de 4**) | DiffBoost |
  | *"strictly ... inside the mask"* | DiffTumor, CLAIM (**2 de 4**) | DiffBoost (mezcla parches de fuera), LGESynthNet (la imagen entera pasa por el latente) |
  | *"implicitly assume non-rigidity"* | **NINGUNO (0 de 4)** | los cuatro: NO ENCONTRADO EN EL PDF |

- **Hallazgo que obliga a cambiar la recomendacion anterior:** la palabra *"implicitly"* no salva la frase. Atribuir
  un supuesto que **ningun** PDF enuncia es exactamente el patron de #25, #37, #40, #45, #47 y #50: un enunciado que
  se vuelve verdad por repetirse. La opcion (a) de #56 ya proponia quitar "implicitly assume non-rigidity"; la lectura
  de CLAIM la convierte de preferencia en **correccion obligada**, porque ahora el recuento es 0 de 4, no 2 de 4.
- **Lo que la lectura REFUERZA:** CLAIM recompone el fondo con pixeles originales. Con esa construccion el streaking
  peri-implante es **imposible por construccion**, no solo no modelado. Es el respaldo mas limpio que tiene B_delta
  en toda la bibliografia leida, y conviene que la frase reescrita lo diga asi, con la formula.
- **Aviso de arquitectura, corrige un supuesto implicito de la ronda:** CLAIM es **DDPM en espacio de imagen**, no
  latente, **sin ControlNet y sin Stable Diffusion** (UNet denoiser, adaptado de LeFusion). Agruparlo con DiffBoost y
  LGESynthNet como "LDM + ControlNet" seria inexacto. Dimensionalidad del generador (2D/2.5D/3D): NO ENCONTRADO EN EL PDF.
- **Alcance de CLAIM frente a la tesis:** metal, implantes, Hounsfield, MAR, streaking y beam hardening son **todos**
  NO ENCONTRADO EN EL PDF. CT solo aparece en trabajo relacionado. Su rol es analogo metodologico, nada mas.
- **Discrepancia interna del PDF, para no citarla mal:** las contribuciones (p. 3) afirman *"showing its improved
  robustness against domain shift"*, pero Sec. 3.5 (p. 9-10) dice que el rendimiento fuera de dominio *"increased
  initially and then dropped"* y que el entrenamiento conjunto *"did not always produce better results on
  out-of-domain-data"*. Ese experimento **solo existe como grafico de barras, sin tabla**. Mismo tipo de hallazgo que
  en `xie2024implantsegmentation` y `zhang2025diffboost`.
- **Cifras citables:** EMIDEC 100 casos (67 patologicos / 33 normales), privado 80; Dice baseline 58.89 frente a
  CLAIM(J) 63.53 (maximo, Tabla 2, p. 11). **Sin FID, SSIM ni PSNR**, y **sin ninguna medida cuantitativa de
  degradacion fuera de la mascara**: solo la afirmacion cualitativa *"the background regions remain preserved in all
  methods"* (p. 8).
- **Gap nuevo, pequeno pero util para el Objetivo 3:** los cuatro analogos validan la sintesis **por Dice downstream**.
  Ninguno publica una metrica directa de coherencia fisica de lo generado. Como esta tesis excluye el downstream por
  alcance, esa ausencia es a la vez su hueco y su justificacion.
- **Pendiente de:** decision de la autora sobre la opcion (a) de #56, ahora con las cuatro fuentes verificadas.

### 58 — La escala ordinal del benchmark SAP/BFC se atribuye a una fuente que NO la contiene: `gertzbein1990` publica SEIS tramos, no cuatro grados — ABIERTA

- **Origen:** ficha `gertzbein1990.md`, `lector-papers`, 2026-09-15, PDF completo. La lectura se pidio porque
  `_index.md` ya registraba que `smith2006iliosacral` es **fuente SECUNDARIA** (*"la escala viene de la literatura de
  tornillos pediculares"*). Este es el nodo primario de esa cadena.
- **Frase en riesgo** (`main.tex:48`): *"Grading iliosacral screws on the four-level cortical-breach scale of
  \citet{smith2006iliosacral}"*.
- **Lo que el PDF publica** (Tabla 1, p. 13): **seis** categorias, en tramos de 2 mm —
  `In pedicle` / `0-2 mm` / `2.1-4.0 mm` / `4.1-6.0 mm` / `6.1-8.0 mm` / `Lateral to Pedicle`,
  con 71.9 / 9.6 / 9.0 / 4.8 / 1.8 / 3.6 %.
- **Grados A/B/C/D: NO ENCONTRADO EN EL PDF.** La "escala de Gertzbein-Robbins" con grados con letra es codificacion
  **posterior de la comunidad**, no de este articulo. Es decir: ninguno de los dos eslabones de la cadena respalda la
  formula "four-level ... scale of Smith".
- **Auditoria de la cadena, igual que se hizo con el umbral de 10 mm:**
  - **TERMINAL para el esquema de tramos:** no cita a nadie por los cortes de 4, 6 ni 8 mm.
  - **NO terminal para el ancla de 2 mm:** *"anatomical dissections have shown that there is 2 mm of epidural space"*,
    con llamada a su ref. 4 (Roy-Camille, Saillant, Mazel, Clin Orthop 203:7-17, 1988).
  - **El corte de 4 mm es extrapolacion propia desde UN SOLO mielo-TC:** *"we would extrapolate that 4 mm of canal
    encroachment could be tolerated"*.
  - **Los cortes de 6 y 8 mm no tienen ninguna justificacion declarada.**
- **Cambio de estructura de referencia, y es el problema de fondo:** los umbrales de Gertzbein estan anclados al
  **canal espinal y al borde medial del pediculo**. El benchmark de esta tesis mide brecha sobre el **corredor
  iliosacro**. Cohorte: 40 pacientes, 167 tornillos, T8-S1, TC postoperatoria en todos los casos. Incluye S1, pero con
  **2 tornillos**, y son **pediculares sacros, no iliosacros**. Iliosacro, ala sacra y pelvis: **cero menciones**.
- **Sin fiabilidad:** observador unico que ademas es coautor — *"All measurements were recorded by one author (SR) to
  reduce the interobserver error."* Sin cegamiento, sin kappa ni ICC. Grosor de corte: NO ENCONTRADO EN EL PDF.
- **Toca directamente la medicion con metal:** *"The CT 'window' was adjusted to reduce metal artifact"* y
  *"measurements corrected to reflect actual size"*, sin validar esa correccion. Volumen parcial: NO ENCONTRADO EN EL
  PDF. Esta tesis mide brecha justo sobre imagenes con metal, asi que hereda el problema sin heredar la solucion.
- **Por que importa:** SAP/BFC es la metrica central. Que su escala se atribuya mal, que los tramos de 6 y 8 mm no
  tengan justificacion y que la fuente primaria no mida el corredor iliosacro son tres repreguntas distintas en la
  sustentacion. Toca ademas #4, que ya senalaba que BFC se apoya solo en `smith2006iliosacral`.
- **Opciones:**
  - **(a) Corregir solo la atribucion.** Mantener la escala de 4 niveles citando a `smith2006iliosacral` como quien la
    **usa en tornillos iliosacros**, sin llamarla "de Smith" ni "de Gertzbein". Es el cambio minimo y es solo texto.
  - **(b) Citar la cadena completa.** Declarar que la escala de tramos de 2 mm viene de la literatura de tornillos
    pediculares (`gertzbein1990`), que los cortes superiores no estan validados, y que `smith2006iliosacral` la
    traslada al corredor iliosacro. Mas honesto y mas largo.
  - **(c) Declarar los tramos como convencion geometrica**, igual que se hizo con el umbral de 10 mm tras la auditoria
    de Kaiser/Gardner/Moed/Ziran. Es el precedente mas coherente con lo ya decidido en este repositorio.
  - **(d) No cambiar nada** y asumir la repregunta.
- **Recomendacion del asistente:** **(b) + (c)**, porque reproducen la decision ya tomada para el 10 mm y porque el
  hallazgo de los cortes de 6/8 mm sin justificacion no aparece en ninguna otra fuente del repositorio.
- **Pendiente de:** decision de la autora. **Sin entrada en `refs.bib`**: hay `refs/raw/gertzbein1990.nbib`, pero el
  alta la decide la autora (regla 9).

### 59 — `herman2016` publica prevalencias de malposicion por nivel y le da MAS brechas a S1 que a S2, lo que tensiona el encuadre S1/S2 de `main.tex` — ABIERTA

- **Origen:** ficha `herman2016.md`, `lector-papers`, 2026-09-15, PDF completo (version **"Accepted Article"**).
- **Cifras propias, con definicion estricta de malposicion** (cualquier porcion del tornillo cruza la cortical),
  medidas con **TC postoperatoria**:
  - **32 %** por tornillo; **45.7 %** por paciente.
  - **S1 36.5 % frente a S2 14.8 % (p=0.035).**
  - Trans-sacro 38.2 % frente a iliosacro 30.3 % (p=0.038).
  - **Ningun tornillo quedo integramente fuera del hueso.**
  - Dismorfismo (37.2 % de pacientes) **NO** se asocio a brecha.
  - Validacion del modelo: sens 97.1 %, esp 84.0 %, VPP 92.7 %, VPN 93.3 %, exactitud 92.9 % frente a lateral 70.0 %
    (p=0.004).
- **La tension, con texto literal.** `main.tex:48` usa `vandenbosch2002` (6/31 con el tornillo bajo en S2 frente a 1/49
  con ambos en S1, p=0.01) para sostener *"This clinical association supports retaining S1/S2 as a sampler variable"*.
  Herman mide **lo contrario en la variable que la tesis modela**: mas brecha cortical en **S1**. No es contradiccion
  real — van den Bosch mide **quejas neurologicas por paciente y por configuracion**, Herman mide **brecha por
  tornillo y por nivel** — pero el parrafo actual no distingue esas dos magnitudes para el lector, y una repregunta
  del tipo "entonces que nivel es mas riesgoso" no tiene hoy respuesta escrita.
- **Toca #12, que esta CERRADA POR DELIMITACION** (benchmark ordinal solo en S1, S2 descriptivo). Herman **no la
  reabre**: su criterio es **binario**, sin escala en mm y sin distribucion ordinal, asi que no sirve como prior SAP.
  Pero si es la **primera fuente del repositorio con tasa de malposicion por nivel medida sobre TC**, y el "ningun
  tornillo integramente fuera del hueso" **acota el rango de malposiciones plausibles que el muestreador debe generar**.
  Eso es directamente utilizable como control de cordura del Objetivo 2.
- **Lo que NO resuelve: la implicancia #32 sigue abierta.** El titulo promete un modelo *"easy to implement"*, pero:
  - Es un **clasificador binario 2D de una pose ya existente**, no un generador: no define punto de entrada, eje,
    angulo ni longitud.
  - **Marco = proyeccion fluoroscopica inlet/outlet**, no voxel ni reformateo segun el eje sacro. Mismo defecto de
    transferencia que ya se documento en `ziran2007fluoroscopic`.
  - **Renuncia a los milimetros:** *"it is a ratio of anatomic landmarks and therefore scale invariant"*. No mide Dmax
    ni publica ninguna dimension propia en mm, ni define contorno oseo sobre el sacro.
  - Faltan piezas **en el PDF**: el **Appendix A** con la derivacion (*"as described in Apppendix A"*, solo remite a
    Supporting Information online) y la **Figure 3** de la definicion de brecha. El **+/-20 %** aparece como dato dado,
    sin origen ni analisis de sensibilidad.
- **El modelo, para el registro:** zona segura = banda de **+/-20 %** alrededor de la recta `Y = (b/a)*X` en coordenadas
  normalizadas por dos landmarks oseos, uno por vista. `a` = ancho antero-posterior del ala sacra en su porcion mas
  estrecha (inlet); `b` = altura del borde superior del foramen neural a la cortical superior del ala (outlet). Regla:
  `APPP = SIPP +/- 20 %`. Primitiva unica: una recta.
- **Desplaza la cadena del 10 mm sin reabrirla:** aqui el umbral se atribuye a **Gardner 2010 y Lee 2015**; Ziran y
  Moed **no estan** en su bibliografia. Coherente con la cadena ya auditada, y sin efecto sobre el cierre por decision.
- **Caveats de cohorte, importantes:** **TC postoperatoria con metal y con fracturas** como criterio de inclusion, no
  anatomia virgen, y **sin mencion de MAR**. Inconsistencias internas del PDF: 97.1 % frente a 97.2 %, especificidad
  lateral 61.5 % frente a 64.2 %, e IC95 % impreso como *"85.1 %-1.01 %"*. Es version "Accepted Article", 25 pp. sin
  paginacion de revista: **citar paginas de aqui repite el patron de `isensee2021`**.
- **Opciones:**
  - **(a) Solo cohorte.** Usar el "ningun tornillo integramente fuera del hueso" y el 32 % por tornillo como control de
    cordura del muestreador, sin tocar `main.tex`.
  - **(b) Anadir una frase al parrafo S1/S2** que separe explicitamente "quejas neurologicas por configuracion"
    (van den Bosch) de "brecha cortical por nivel" (Herman), y que registre que la segunda favorece a S2.
  - **(c) (a) + (b).**
- **Recomendacion del asistente:** **(c)**. (b) es barato y desactiva una repregunta; (a) da un control de cordura que
  hoy no existe.
- **Pendiente de:** decision de la autora. **Sin entrada en `refs.bib`**: hay `refs/raw/herman2016.nbib`; el alta la
  decide la autora (regla 9). Si se da de alta, decidir antes si se cita el "Accepted Article" o la version de revista.

### 60 — `deman1999` NO mide la extension espacial del streak: el reclamo de novedad de B_delta sobrevive, y #57 sigue sin evidencia externa — ABIERTA

- **Origen:** ficha `deman1999.md`, `lector-papers`, 2026-09-15, PDF completo (6 pp., 691-696). Se leyo expresamente
  para intentar **refutar** la frase de `main.tex:54`: *"for which no published precedent quantifying a peri-implant
  band was found"*. Es el estudio de simulacion clasico del streak metalico.
- **Resultado, inequivoco: NO mide extension.** Ni mm, ni cm, ni pixeles, ni perfil radial, ni ley de decaimiento, ni
  region de interes peri-metal. Revisadas las 6 paginas, abstract, metodos, resultados, conclusiones y pies de las
  figuras 1-15. Toda localizacion es **cualitativa y direccional**: *"dark streaks in the directions of highest
  attenuation"* (III-B, p. 693), *"a number of streaks can be seen radiating from the metals"* (III-D, p. 694). La
  unica frase con "distance" — *"streaks starting at a certain distance from the center"* (III-G, p. 694) — **no trae
  cifra** y se refiere al centro de rotacion en submuestreo de vistas, no al borde del metal.
- **Efecto sobre el argumento: refuerza, no amenaza.** El reclamo de novedad de B_delta queda en pie, y ahora con un
  intento de refutacion documentado sobre la fuente mas probable. Ademas respalda **cualitativamente** el
  *"propagate globally"* de `main.tex:48`.
- **Pero NO resuelve #57.** La contradiccion interna sigue igual: `main.tex:48` dice *"globally far beyond"*, B_delta
  es de ~12 mm y el titulo dice *"local"*. Este paper confirma que las estrias se propagan, y **confirma tambien que
  nadie publico cuanto**. O sea: la opcion (b) de #57 (medicion propia de perfil de HU frente a distancia al metal
  sobre CLINIC-metal) pasa de "deseable" a **la unica via que puede justificar el ~12 mm con una cifra**. No hay
  fuente que citar.
- **No aporta umbrales en HU: cero HU en todo el PDF.** Las ventanas van en mu ([0.1;0.3] cm^-1 y [-0.05;0.05] cm^-1).
  Para umbrales de artefacto sigue mandando `ren2022metalinsertion` (-75/75/500 HU).
- **Causas que separa:** beam hardening, scatter, ruido, EEGE, movimiento y aliasing de detector/vistas. **Sin pesos
  numericos**; el ranking es una sola frase: *"Beam hardening, scatter, noise and EEGE are the most important causes of
  metal streak artifacts"* (Conclusiones, p. 695). El **volumen parcial no lineal queda explicitamente fuera de
  alcance** — justo el mecanismo que mas pesa en el borde metal/hueso que esta tesis sintetiza.
- **Caveats de transferencia, y son fuertes:** fantoma de **hierro** (*"a cylindrical iron rod (diam. 11.6mm) positioned
  eccentrically in the water"*, II-B-2, p. 692) y amalgama dental. **Ni titanio, ni acero quirurgico, ni implante
  ortopedico.** Fan-beam **2D**. Reimplementable solo en parte: faltan kVp, mAs, filtracion, distancias, numero de
  detectores, matriz, kernel y el numero de vistas explicito; sin codigo. Lo que si publica: *"focal spot width (0.6mm)
  and detector element width (1.2mm)"*, muestreo 0.1 mm, sobre *"Siemens Somatom Plus 4"* (II-A, p. 691); scatter
  *"The scatter-to-primary ratio was arbitrarily chosen to be 0.0001"* (II-D, p. 693) con *"Even a very small
  scatter-to-primary ratio causes significant streaks"* (III-C, p. 694); ruido *"an unattenuated flux of 10^5 or
  2 x 10^5 photons per detector"* (II-D, p. 693).
- **Opciones:**
  - **(a) Citarlo como respaldo cualitativo** del *"propagate globally"* y como evidencia de que la cuantificacion
    peri-implante no esta publicada. Refuerza C3 sin prometer nada.
  - **(b) (a) + declarar el caveat de material** (hierro/amalgama dental, 2D, sin volumen parcial) al citarlo.
  - **(c) No citarlo.** No hay raw en `refs/raw/`, asi que hoy no es citable de todos modos.
- **Recomendacion del asistente:** **(b)** si la autora decide dar de alta la entrada; **(c)** mientras no haya raw.
- **Pendiente de:** decision de la autora. **Sin `refs/raw/deman1999.*`**: por regla 9 no se puede dar de alta hasta
  que la autora pegue el archivo del editor.

### 61 — El renderizador trabaja en el dominio imagen, pero TODOS los mecanismos del streak que describe `deman1999` son no lineales y se manipulan en proyeccion — ABIERTA

- **Origen:** ficha `deman1999.md`, 2026-09-15. Es un hallazgo lateral de esa lectura, separado de #60 porque no toca
  la redaccion sino el **supuesto de viabilidad del Objetivo 3**.
- **El hueco:** el renderizador de esta tesis es un LDM 2.5D con ControlNet que genera **en imagen**, sin sinograma.
  De Man separa beam hardening, scatter, ruido/photon starvation, EEGE y aliasing, y los manipula **todos en el
  dominio de proyeccion**, con no linealidades explicitas (el ruido *"strongly depends on ... the total integrated
  attenuation"*, III-E, p. 694).
- **Lo que el PDF dice sobre reproducir eso sin sinograma: NO ENCONTRADO EN EL PDF.** No lo afirma ni lo niega. Es
  decir, **no hay en la bibliografia leida ninguna frase que autorice ni que prohiba** el atajo en imagen.
- **Por que importa:** el argumento actual de `main.tex` contra los simuladores fisicos es que **no escalan la
  colocacion anatomica** (*"physical simulators do not supply scalable anatomically constrained placement"*), no que
  el dominio imagen sea equivalente. La equivalencia nunca se afirma, pero tampoco se discute, y es la pregunta
  natural de un jurado con formacion en fisica de la imagen: *por que un modelo generativo en imagen puede producir un
  efecto cuyo mecanismo es de proyeccion y no lineal*.
- **Relacion con lo ya decidido:** es el mismo eje de #6 (`ren2022metalinsertion` exige datos crudos de fabricante que
  CTPelvic1K no tiene) y de la eleccion de `peters2025hybrid` como brazo fisico. La respuesta defendible probablemente
  ya existe — el brazo fisico cubre el mecanismo, el brazo generativo cubre la escala — pero **no esta escrita**.
- **Opciones:**
  - **(a) Una frase en Limitations:** el renderizador aprende la **apariencia** del artefacto, no su mecanismo de
    formacion; el mecanismo lo cubre el brazo fisico de `peters2025hybrid`.
  - **(b) Ademas, convertirlo en hipotesis evaluable:** es justamente lo que mide la coherencia fisica distribucional
    del Objetivo 3, asi que puede enunciarse como lo que la tesis pone a prueba en vez de como limitacion.
  - **(c) No escribir nada** y responderlo solo si lo preguntan.
- **Recomendacion del asistente:** **(b)**, con (a) como respaldo. Convierte una debilidad silenciosa en el enunciado
  de lo que la tesis efectivamente mide, y no cuesta ningun experimento nuevo.
- **Pendiente de:** decision de la autora. `main.tex` y `00-tesis.md` sin cambios (regla 14).

## Ronda 2026-09-15 (11) — `zwingmann2013` y `lin2019` leidos, correcciones APLICADAS a `main.tex` por orden de la autora, `refs.bib` 43 -> 64

> **Orden explicita de la autora en este turno:** leer Zwingmann 2013 y otro paper sin ficha,
> **aplicar en `main.tex` las correcciones recomendadas**, y generar los `refs/clean/` que faltaban
> a partir de `refs/raw/`. Las ediciones de `main.tex` de abajo se hicieron bajo esa orden, no por
> iniciativa del asistente (reglas 4 y 14). `docs/01-decisiones.md` **sigue sin tocarse** (regla 3):
> copiar alli la decision definitiva le corresponde a la autora.

### 56, 58, 59, 60, 61 — APLICADAS en `main.tex` el 2026-09-15

`tesis/main.tex` compila: **5 paginas** (antes 4), **64 referencias**, **0 citas indefinidas**, 0 errores.

| # | Que se escribio | Estado |
|---|---|---|
| 56 | La frase de las cuatro fuentes se reescribio **por familias**. Se **retiro** *"implicitly assume non-rigidity"* (0 de 4 lo enuncian) y *"strictly restrict ... to the inside of the object's mask"*. Ahora CLAIM aparece como el que recompone el fondo, DiffTumor como el que no modela nada fuera, LGESynthNet como inpainting cuyo latente perturba el corte *"incidentally rather than by design"*, y DiffBoost como sintesis global con la mascara solo de borde. El enunciado comun quedo en lo unico que las cuatro fichas sostienen: ninguna tiene mecanismo ni senal de entrenamiento para cambios de intensidad fuera de la mascara | **APLICADA** |
| 58 | Se retiro *"the four-level cortical-breach scale of \citet{smith2006iliosacral}"*. Ahora Smith aparece como quien **aplica** la escala en tornillos iliosacros, y `gertzbein1990` como el origen pedicular con **seis tramos de 2 mm**, ancla de 2 mm en el espacio epidural, corte de 4 mm extrapolado de un solo mielo-TC y **sin justificacion para 6 y 8 mm**. El ancho de 2 mm queda declarado **convencion geometrica**, igual que el criterio de 10 mm, y el traslado del canal espinal al corredor iliosacro queda escrito como **supuesto explicito de este trabajo** | **APLICADA** |
| 59 | Frase nueva en el parrafo S1/S2 con las cifras de `herman2016` (36.5% en S1 frente a 14.8% en S2, p=0.035; 32% global; ningun tornillo integramente fuera del hueso) y la aclaracion de que **no contradice** a van den Bosch porque miden magnitudes distintas. El "ningun tornillo fuera del hueso" queda escrito como cota del rango que el muestreador debe producir | **APLICADA** |
| 60 | `deman1999` citado como respaldo cualitativo del streak, **con su caveat de transferencia escrito en el texto**: varilla de hierro y amalgama dental, geometria fan-beam 2D, volumen parcial no lineal excluido, y **sin extension espacial**, de donde la banda peri-implante *"remains unmeasured in the literature"* | **APLICADA** |
| 61 | Parrafo nuevo tras el Recognized Gap. La generabilidad en dominio imagen queda **declarada como supuesto y como objeto de la evaluacion**, no como premisa, con `peters2025hybrid` de referencia fiel al mecanismo. Ver #63 para la evidencia que lo sostiene | **APLICADA** |

**Pendiente de la autora:** copiar estas cinco a `docs/01-decisiones.md` si las da por definitivas, y **verificar contra los PDF** las citas que ahora estan impresas en el documento. Las verifico un agente.

### 62 — `zwingmann2013` y `zwingmann2009navigated` NO son independientes, y la cohorte del prior ordinal entra al metaanalisis con CERO eventos — ABIERTA

- **Origen:** ficha `zwingmann2013.md`, `lector-papers`, 2026-09-15, PDF completo (9 pp., 1257-1265). Se leyo porque era la candidata mas fuerte de la ronda anterior para tocar el prior ordinal del benchmark.
- **Hallazgo decisivo, y es el que hay que entender bien.** `zwingmann2009navigated` es la **ref. 10** de este metaanalisis **y ademas entra como estudio primario numero 19**, con los tamanos exactos de esa cohorte: *"19 Zwingmann J (convent.) 2009 0 35"* y *"19 Zwingmann J (3d nav.) 2009 0 26"* (Fig. 2, p. 1261). La cohorte de 2010 en *J Trauma* es el estudio numero 9.
  - **La misma cohorte que aporta el prior ordinal del benchmark SAP (grado 0 en 69% y en 40%, es decir 31% y 60% de brecha no nula) figura aqui con CERO malposiciones en los dos brazos.**
  - No es un error: es que *"malposicion"* agregada designa **otro constructo, mucho mas estricto**. El propio paper lo dice dos veces: *"no clear definition about screw malposition and no comparable grading systems are given"* (Discusion, p. 1263) y *"Most authors use the term 'malposition' only when a screw revision was performed."* (Discusion, p. 1264).
  - **El paper no declara el solapamiento ni hace analisis de sensibilidad sin los autoestudios.**
- **Efecto sobre la tesis: refuerza la decision ya tomada.** Es la prueba mas limpia de por que el muestreador apunta a **distribuciones ordinales** y no a una tasa agregada. Ya esta escrito en `main.tex` (ver #58 arriba). **Pero obliga a no citar las dos fuentes Zwingmann como si fueran independientes**, y eso tambien quedo escrito.
- **Cifras citables** (todas **por tornillo**; tasa por paciente: NO ENCONTRADO EN EL PDF): malposicion convencional **2.6%** (1832 tornillos, IC95 `[0.014; 0.043]`), navegacion 2D/3D **1.3%** (445, `[0.002; 0.033]`), navegacion TC **0.1%** (262, `[0.001; 0.008]`), global `0.018 [0.010; 0.029]` (Fig. 2, p. 1261). Revision: 2.7% / 1.3% / 0.8% (Fig. 3, p. 1262). TC frente a convencional *"significantly lower (p < 0.0001)"*; convencional frente a 2D/3D no significativo. Heterogeneidad con I2 y tau2: 70.8% / 52.2% / 0% / 65.7% global.
- **Es BINARIO, de forma inequivoca.** Datos agregados como `Events / Total`, sin ningun umbral en mm para el tornillo. **No aporta prior ordinal y no reabre #12**, que sigue cerrada por delimitacion: **no desagrega por nivel sacro** (S1, S2, transacro y dismorfismo con cifra: todos NO ENCONTRADO EN EL PDF).
- **TRAMPA que hay que dejar anotada:** su unica escala en mm (Tabla 2, p. 1263: <5 / 5-10 / 10-15 / >15 mm) es **desplazamiento rotacional secundario del anillo pelvico en radiografia de seguimiento**, no brecha cortical. No mezclarla con la escala 0/<2/2-4/>4 mm. Es el mismo tipo de confusion que ya ocurrio con la escala de REDUCCION de `moed2006s2screw`.
- **CIERRA la cadena del 2%-15%, y la cierra mal para quien la cite.** El rango aparece **dos veces en el mismo articulo y con valores distintos**: *"reported to range from 2 to 15 % [19, 25]"* (Introduccion, p. 1258) frente a *"range from 0 to 15 % [19, 25]"* (Discusion, p. 1263), **con las mismas dos referencias** (19 = Hinsche 2002, 25 = Templeman 1996). Ya se sabia que Hinsche lo hereda y no lo mide. Con esto la banda queda como **cita circular e internamente inestable**: no debe usarse en la tesis bajo ninguna forma. *"31%"*, *"60%"* y *"31-60%"* como tasa de malposicion: **NO ENCONTRADO EN EL PDF** (el 60.6% de la Tabla 2 es desplazamiento <5 mm). Confirma por tercera via el retiro del rango unico (#12, #25).
- **Discrepancias internas, para no citarlo mal:** la Discusion (p. 1264) escribe *"compared to 2.3 %"* para el brazo convencional, contra **2.6%** en abstract y resultados; y el bosque totaliza **2539** tornillos frente a los *"2,353"* del texto. Modalidad de verificacion de los estudios incluidos, cegamiento, PROSPERO/PRISMA, sesgo de publicacion y escala de calidad: todos NO ENCONTRADO EN EL PDF.
- **Nivel propuesto: 2.** Acceso COMPLETO, 9 pp.
- **Pendiente de la autora:** decidir si quiere ademas una frase explicita que declare la no-independencia de las dos fuentes Zwingmann. Hoy `main.tex` la deja implicita al escribir *"by the same first author"* y *"the 2009 cohort enters that pool with zero events"*.

### 63 — `lin2019` NO prohibe el renderizador en dominio imagen, pero deja el supuesto sin precedente: la asimetria remocion/generacion es lo unico que lo sostiene — ABIERTA

- **Origen:** ficha `lin2019.md` (DuDoNet, CVPR 2019), `lector-papers`, 2026-09-15, PDF completo. Se leyo expresamente contra #61, por ser el paper cuya tesis central es que un solo dominio no basta.
- **Veredicto sobre #61: la debilita sin prohibirla, y por dos razones distintas.**
  1. **Es rendimiento, no imposibilidad.** *"image domain enhancement is not sufficient for mitigating intense metal shadows"* (Sec. 2.3, p. 10506), pero justo antes concede *"The metal artifacts considered in these works are mild and thus can be effectively reduced by a CNN"*, y en la Fig. 7b admite *"image domain methods reduce most of the artifacts"*. **No hay ninguna frase con "cannot" ni "impossible" sobre el dominio imagen.** La unica palabra fuerte del paper, *"inevitably"*, se aplica al **sinograma solo**.
  2. **Asimetria de tarea.** DuDoNet hace **remocion** y enuncia su problema como mal planteado (*"ill-posed problem since both terms contribute to the region of metal trace"*, p. 10506). En generacion no hay informacion destruida que recuperar. **Trasladar "no se puede quitar desde imagen" a "no se puede poner desde imagen" es una inferencia que el paper no autoriza**, y asi quedo escrito en `main.tex`.
- **La ablacion, que es lo mas valioso de la lectura** (Tabla 1, p. 10509): variante de solo imagen (IE-Net) **31.45 dB / 0.9269** frente a dual-domain completo **33.51 dB / 0.9379**. Solo sinograma queda mucho peor: 26.71 / 0.8337. Una red de imagen muy profunda (RDN-CT, ~80 capas) llega a 31.74 / 0.9156 (Tabla 2). **Aviso: el delta en dB NO lo enuncia el paper**; en `main.tex` se imprimieron los dos valores absolutos, no la resta.
- **Caveat que cambia la lectura y tambien quedo escrito:** la variante de solo imagen **no es ciega al sinograma**, porque recibe `X_LI`, reconstruida de un sinograma **ya interpolado**. Esos 2 dB miden el valor de **refinar el sinograma con una red**, no el de **tener acceso a la proyeccion**.
- **Supuesto nuevo, ahora explicito en el documento:** que la **apariencia** del artefacto es generable en imagen sin operador de proyeccion. **No esta respaldado por ninguna fuente leida**, y tampoco refutado. #61 queda como **falta de precedente**, no como prohibicion demostrada. Contrapeso honesto: el propio DuDoNet **fabrica sus artefactos en el sinograma** y no discute alternativa.
- **Gap nuevo:** no se encontro trabajo que **sintetice** artefacto metalico trabajando solo en imagen y valide su coherencia fisica. Es exactamente el hueco que el Objetivo 3 ocupa.
- **No sirve para C3 ni para B_delta.** Ventanas en HU: **NO ENCONTRADO EN EL PDF** (ni *"HU"* ni *"Hounsfield"*), asi que no es precedente del multi-ventana. Extension espacial del artefacto: **NO ENCONTRADO EN EL PDF** — la unica mascara formal es la traza de metal **en coordenadas de sinograma**. Refuerza el "sin precedente" que ya dejo `deman1999` (#60).
- **Como simula el metal, que es un precedente directo de insercion sintetica:** DeepLesion, 4000 imagenes / 320 pacientes (train), 200 / 12 (test), 416x416; **100 mascaras de metal** (90 train + 10 test) y 360 000 combinaciones; tamanos 16-4967 px (train) y 32-2054 px (test); *"polychromatic X-ray, partial volume effect, and Poisson noise"* con 2x10^7 fotones incidentes; D = 39.7 cm, 320 vistas de 0 a 360 grados, sinograma 321x320. **Materiales, geometrias, tipo de implante y scatter: NO ENCONTRADO EN EL PDF**; *"beam hardening"* no aparece como termino, solo *"polychromatic"*.
- **Pista accionable:** ese protocolo se hereda de su ref. [33], **Zhang & Yu, IEEE TMI 2018**, que es `zhang2018` y **acaba de entrar a `refs.bib` en esta misma sesion**. Ahi estarian los materiales, coeficientes y geometrias que DuDoNet omite. Es la lectura siguiente mas rentable para el brazo fisico.
- **Anatomia:** no declarada en el texto (las figuras muestran torax y abdomen). **CTPelvic1K, CLINIC-metal, pelvis y tornillo: NO ENCONTRADO EN EL PDF.**
- **Nivel propuesto: 1.** Es la objecion central al diseno del renderizador y la unica ablacion leida que cuantifica el costo de trabajar en un solo dominio.
- **Pendiente de la autora:** validar el nivel 1 y decidir si `zhang2018` entra a la cola de lectura.

### Bibliografia — 21 altas de una vez: `refs.bib` pasa de 43 a 64 y el PDF de 4 a 5 paginas (2026-09-15)

- **Orden de la autora:** *"Sobre los archivos que tienen refs/raw pero no refs/clean, es natural porque necesitan ser regenerados a partir del raw (hazlo)"*. Hecho: 21 `refs/clean/*.bib` generados desde su raw, `python scripts/build_refs.py` -> **64 entradas**. `refs/raw/` intacto. Procedencia y decisiones de normalizacion, una por una, en `refs/MAPEO.md`. **Ya no queda ningun raw sin clean ni ningun clean sin raw.**
- **Correccion de un error del asistente:** en la ronda anterior se reporto que `deman1999` no tenia raw. **Es falso**, `refs/raw/deman1999.bib` existia. El fallo fue un filtro que buscaba `^title` y no acierta en los `.bib` de IEEE, donde el campo va con sangria. Lo detecto la autora. Afecta a lo que se dijo en #60: `deman1999` **si es citable**, y de hecho ya se cito.
- **Efecto medido, y conviene tenerlo presente:** con `\nocite{*}` en `main.tex:139`, las 21 altas entran a la bibliografia **sin que ninguna frase las cite**. El documento paso de **4 a 5 paginas** y de 43 a **64 referencias**. De las 21, solo tres se citan hoy en el texto: `deman1999`, `gertzbein1990`, `herman2016`, `lin2019` y `zwingmann2013` (cinco). Las otras dieciseis se imprimen sin uso.
  - **Decision pendiente de la autora:** si la bibliografia debe listar solo lo citado, hay que quitar `\nocite{*}`. **No se toca sin orden** (regla 14).
- **Dos avisos que quedaron registrados en `MAPEO.md` y merecen su ojo:**
  - **`macháček2023` tiene una clave con caracteres no ASCII** (`á`, `č`). Se conservo por la regla 1. **Verificado: BibTeX y pdfLaTeX compilan sin error con ella**, pero si alguna vez falla, renombrarla es decision suya.
  - **`tejwani2014` es la unica de las 21 sin DOI**: su raw no trae `AID` ni `LID`, y no se busco en otra fuente (regla 9). `gottschling2009` tampoco lleva `doi`, porque el de Springer solo aparece dentro de la clave del editor y una clave no es un campo.
  - **`herman2016` apunta hoy a dos versiones distintas:** el raw confirma la version de revista (J Orthop Res 35(7):1478-1484, 2017) y es la que entro a `refs.bib`, pero el PDF de `papers/` es el *Accepted Article* sin paginacion, que es sobre el que se hizo la ficha. Mismo patron que `isensee2021`.
- Las dos unicas advertencias de BibTeX siguen siendo las de siempre y son correctas: `hinsche2002fluoroscopy` y `templeman1996proximity` tienen numero de fasciculo y no volumen, porque *CORR* de esa epoca numeraba asi.

## Ronda 2026-09-16 — 4 lecturas: `arand2019pelvicring`, `chen2026foundationvae`, `tejwani2014`, `zhang2018`

Elegidas entre los 19 PDF de `papers/` sin ficha por riesgo sobre el argumento: una cita impresa sin leer
(`arand2019pelvicring`), la objecion externa a E6b (`chen2026foundationvae`, prioridad 1 desde el 2026-09-15), la
fuente de simulacion que `lin2019` omite (`zhang2018`) y la unica "safe zone" iliosacra sobre CT postoperatorio sin
leer (`tejwani2014`). Fichas de `lector-papers`; las afirmaciones de los lectores se contrastaron contra `main.tex`,
`peters2025hybrid.md`, `e6b_vae_sd15.py` y `_candidatos.md`, y **tres se corrigieron** (ver #64, #67 y la
actualizacion de #63). `main.tex`, `00-tesis.md` y `01-decisiones.md` sin tocar (reglas 3, 4 y 14).

### 64 — `arand2019pelvicring` esta citado en `main.tex` como fuente de "bone density maps" y NO publica un mapa utilizable — ABIERTA

- **Origen:** ficha `arand2019pelvicring.md`, 2026-09-16, PDF completo. **Estaba citado dos veces en `main.tex` sin
  haberse leido nunca** (patron vigilado: una cita que se vuelve verdad por estar impresa).
- **Frases afectadas:**
  - `main.tex:78` (Objetivo 2): *"constrained by bone density maps \citep{arand2019pelvicring}"*.
  - `main.tex:52`: *"bounded by pelvic density representations \citep{arand2019pelvicring}"*.
- **Lo que SI hay:** *"A separate statistical model of the grey value distribution"* (Abstract, p. 376);
  *"The mean HU value for each voxel was calculated"* (Methods, p. 377). Es un **promedio poblacional de HU**,
  mostrado como figura y descrito por regiones (ala sacra baja, *"so-called alar void"*; cuerpo de S1 intermedio).
  Dice que sirve para *"preoperative planning and screw positioning"* (Discussion, p. 382).
- **Lo que NO hay:** valores numericos de HU, calibracion a densidad mineral, dispersion, disponibilidad publica del
  modelo, ni ningun uso del mapa para restringir un tornillo. Cohorte: 50 CT **post mortem**, japoneses, edad media
  74.9, sin lesion; implantes: NO ENCONTRADO EN EL PDF.
- **Veredicto:** `main.tex:52` ("representations") es defendible como motivacion cualitativa. `main.tex:78` ("maps")
  **sugiere que la tesis toma los mapas de Arand**, y el muestreador en realidad lee el HU de cada volumen.
- **Correccion al lector:** su informe dice que la regla de 5 mm y la viabilidad de corredor "no salen de este paper".
  Es cierto pero **no es un problema de `main.tex`**: en `main.tex:78` la regla de 5 mm cae bajo Kaiser y la
  viabilidad bajo `mclaren2021corridor`. No hay mala atribucion ahi.
- **Lo que si respalda:** el rol de `_index.md` ("el corredor no es fijo"). Componentes 3 y 4 cambian *"the size and
  availability"* del corredor transsacro S1 (Results, p. 379), sin cifra en mm. Varianza de las 5 primeras componentes
  61.7% (Results) frente a 61.64% (Conclusion): inconsistencia menor del paper.
- **Supuesto nuevo sin documentar:** transferir un patron de densidad de pelvis ancianas post mortem sin lesion a
  CLINIC-metal (fractura + implante) no esta justificado. Solo importa si la tesis usa el patron, no si usa HU propio.
- **Opciones para la autora:**
  - (a) Reescribir `main.tex:78` como *"constrained by per-volume HU (bone density), motivated by the heterogeneous
    sacral bone mass reported by \citet{arand2019pelvicring}"*, sin afirmar que se usan sus mapas.
  - (b) (a) + usar Arand tambien en la frase de `main.tex:52` sobre variacion anatomica (*no canonical pose*), que es
    el uso mejor respaldado.
  - (c) Retirar la cita de densidad y leer Wagner 2014 (*bone mass distribution and trans-sacral corridors*, ya en
    `_candidatos.md`) como fuente alternativa.
- **Tipo:** REDACCION / SUPUESTO. **Nivel propuesto: N2.**

### 65 — `chen2026foundationvae` NO contradice E6b: no mide error en HU, no evalua hueso ni metal, y su unico recorte declarado es [-1000, 1000] HU — ABIERTA

- **Origen:** ficha `chen2026foundationvae.md`, 2026-09-16, PDF completo. Cierra en evidencia la accion de la entrada
  "36 y 39 — Busqueda web autorizada" (2026-09-15), que lo marco como prioridad 1.
- **Hipotesis del recorte: confirmada solo en parte.**
  - Generacion (CT-RATE / ReXGroundingCT): *"intensities are clipped to [−1000, 1000] HU"* (§4.1, p. 5).
  - **Reconstruccion y aumentacion** (MSD Task06/07, LiTS, KiTS19; Tablas 1-2, p. 3), que es donde se apoya
    *"without medical fine-tuning"*: rango y normalizacion **NO ENCONTRADO EN EL PDF**. No se puede afirmar que ahi
    tambien recorten.
- **Por que igual no refuta E6b (evidencia, no inferencia):** metricas PSNR/SSIM/MSE **sin unidad declarada**; **ningun
  error en HU** ni MAE; **ningun ROI por tejido** (hueso, metal); anatomia torax y abdomen, **sin pelvis ni metal**;
  **ningun VAE 2D tipo Stable Diffusion** (solo 7 VAE de video congelados, con MedVAE y MAISI como referencia). E6b mide
  MAE en HU dentro de hueso > 150 HU con SD 1.5: otra pregunta.
- **Lo que NO se puede escribir:** que Chen "recorta todo a [-1000, 1000]" (solo esta declarado para generacion), ni que
  un VAE de video congelado fallaria en hueso (no se probo).
- **Riesgo de sustentacion:** sigue siendo repregunta probable (ICML 2026, titulo contrario a la conclusion de E6b). Hoy
  `main.tex` no lo cita.
- **Inconsistencias internas del paper** (para no citarlo mal): MedVAE PSNR 20.34 / MSE ">600" en Introduccion frente a
  30.06 / 88.36 en Tabla 1; WAN2.1 y WAN2.2 identicos en Lung; 124 frente a 126 clases de mascara.
- **Opciones para la autora:**
  - (a) Frase en Related Work / Objetivo 1 que lo cite y lo acote con las diferencias de arriba. Recomendada.
  - (b) (a) + anadir un VAE de video congelado (WAN2.x o IVVAE) como configuracion extra de E6b, para responder con dato
    propio. Coste: otra corrida de cohorte en Khipu (E6b completo tardo 8.74 h).
  - (c) No citarlo y preparar solo la respuesta oral.
- **Tipo:** REDACCION / RIESGO. **Nivel propuesto: N2.** Snowballing: MAISI y MedVAE a `_candidatos.md` (utiles para la
  opcion 3 de #36/#39).

### 66 — El Go/No-Go del Objetivo 1 solo mide hueso y metal: nada comprueba que el autoencoder conserve el streaking de B_delta — ABIERTA (GAP)

- **Origen:** `chen2026foundationvae`, Fig. 2, p. 2: *"Errors are dominated by high-frequency noise and mild streak
  artifacts"*. Contrastado contra `experiments/objetivo1/e6b_vae_sd15.py`: `ROIS = ('hueso', 'metal')` (linea 79),
  hueso > 150 HU, metal > 2500 HU. **No hay ROI de banda peri-implante ni de estrias.**
- **Por que importa:** el streaking de baja amplitud y alta frecuencia **es la senal que el Objetivo 3 debe sintetizar**
  dentro de B_delta. Un VAE que suprima (o introduzca) estrias leves puede pasar el Go/No-Go en hueso y aun asi
  **limitar lo que el renderizador puede expresar**, o contaminar la evaluacion con estrias propias.
- **Cautela:** la frase de Chen es sobre su error de reconstruccion en datos sin metal y posiblemente recortados; **no
  distingue si el VAE quita o pone estrias** y no da cifra. Es una senal para medir, no evidencia de fallo.
- **Opciones para la autora:**
  - (a) Anadir a E6b (o al VAE que se elija por la opcion 3 de #36/#39) un tercer ROI: la banda B_delta alrededor del
    metal (> 2500 HU dilatado ~12 mm, menos metal), con MAE/RMSE y, si se quiere, error en alta frecuencia. No cambia
    el Go/No-Go; se reporta como descriptivo. Barato: la mascara de metal ya se calcula.
  - (b) Declarar la limitacion en el Objetivo 3 sin medir.
  - (c) Nada (solo aceptable si el Objetivo 3 se cae del alcance).
- **Tipo:** GAP metodologico, afecta Objetivo 1 (diseno del control) y Objetivo 3.

### 67 — `tejwani2014`: la brecha detectada podria depender del grosor de corte del CT, y el benchmark compara contra CT de protocolo no registrado — ABIERTA

- **Origen:** ficha `tejwani2014.md`, 2026-09-16, PDF completo (Am J Orthop 43(11):513-516).
- **Hallazgo 1 (SUPUESTO del benchmark):** CT de *"either a 5.0-mm or a 2.5-mm sequential axial image"* (Materials and
  Methods, p. 514); la penetracion detectada es mayor con 2.5 mm (20 de 32 pacientes), **con P = .3, no
  significativo**. Es solo una tendencia, pero plantea un supuesto que la tesis no declara: los grados de
  `zwingmann2009navigated` salen de CT postoperatorios cuyo grosor de corte **no esta registrado en su ficha**, y SAP se
  medira sobre volumenes con espaciado z submilimetrico (`02-datos.md`). `herman2016` usa cortes de 2 mm. Si la
  sensibilidad a brechas de 2 mm depende del grosor de corte, **comparar la distribucion del muestreador (voxel
  submilimetrico) con la clinica (corte posiblemente mas grueso) no es neutral**.
  - Accion posible: verificar en el PDF de Zwingmann 2009 el protocolo de CT (via `lector-papers`); si es >= 2.5 mm,
    declarar la asimetria como limitacion o evaluar SAP tambien re-muestreando a ese grosor como sensibilidad.
- **Hallazgo 2 (#7, sin cambio de decision):** la "safe zone" es foraminal y cualitativa (penetracion pequena en el
  tercio superior del foramen S1 en axial), con limite en mm **inconsistente en el propio paper** (2, 2.1, 2.7, 3 mm
  segun seccion). No compite con Kaiser/McLaren ni sirve de fuente operacional.
- **Hallazgo 3 (amplia #58):** escala propia de 3 categorias (intraoseo / *"skived"* < 2 mm en foramen S1 / extruido),
  **sin fuente y sin conteos por categoria**. Otro uso del corte de 2 mm en iliosacro sin justificacion. No aporta prior
  ordinal y no reabre #12/#28: solo mide S1 y llama "S1 screws" a los 51 tornillos aunque 3 casos llevaron S2.
- **Hallazgo 4 (cadena 2%-15%, cerrada):** repite *"reported in 2% to 15% of patients"* (p. 514) sin numero de
  referencia. **Correccion al lector:** no puede ser el origen del rango (2014, posterior a Hinsche 2002 y a Zwingmann
  2009/2013, #62); es un repetidor mas. Sin efecto: el rango ya esta RETIRADO.
- **Cifras que NO se deben citar** sin aclarar discrepancia: pacientes sin cambio neurologico (4 frente a 2), deficit
  nuevo (6 frente a 8), iatrogenico (1 frente a 2), penetracion 45% frente a 43%, suma de tornillos que no da 51. Solo la
  tabla (46 pacientes, 51 tornillos, 23 con penetracion) es consistente.
- **Tipo:** SUPUESTO (hallazgo 1) / REDACCION (2-3). **Nivel propuesto: N2.**

### 63 — ACTUALIZACION tras leer `zhang2018` (2026-09-16): protocolo recuperado, y `lin2019` le atribuye algo que no tiene

- **Origen:** ficha `zhang2018.md`, 2026-09-16, PDF completo (12 pp., version aceptada).
- **Lo que `lin2019` omitia, ahora con fuente:** metales Ti, Fe, Cu y Au; coeficientes de XCOM (valores NO ENCONTRADO
  EN EL PDF); fuente policromatica 120 kVp, 2x10^7 fotones, ruido de Poisson; fan-beam 2D, 984 vistas, 920 detectores,
  59.5 cm fuente-isocentro; 512x512; 74 CT, 15 formas de metal segmentadas a mano, 100 casos. Metrica: RMSE en HU
  excluyendo pixeles de metal, y SSIM.
- **Discrepancia:** `lin2019` dice simular volumen parcial igual que su ref. [33]; **este PDF no menciona volumen
  parcial ni dispersion**. Lo que `main.tex:56` dice de `lin2019` no depende de ese detalle: sin cambio de texto.
- **Sobre #61:** el artefacto se fabrica en proyeccion **reproyectando CT ya reconstruidos** (HU -> atenuacion,
  separacion agua/hueso), sin datos crudos. **Correccion al lector:** propuso que esto obliga a repensar el brazo
  fisico. No: `main.tex:56` no argumenta falta de datos crudos, y `peters2025hybrid` (protocolo adoptado) ya hace
  proyeccion y reconstruccion sobre CT. Sin implicancia nueva sobre baseline.
- **Sobre #57 / B_delta:** extension espacial del artefacto **NO ENCONTRADO EN EL PDF** (solo cualitativo: hueso borroso
  *"near the metals"*). Tercera fuente de simulacion leida sin cifra de alcance (tras `deman1999` y `lin2019`): el
  *"remains unmeasured in the literature"* de `main.tex` sigue en pie.
- **Dato util para el Objetivo 3:** caso 1 es un corte pelvico con **protesis bilaterales de cadera** (visto en figura;
  el texto solo dice *"hip prostheses"*). Precedente de metal simulado en pelvis, no de tornillo iliosacro.
- **#63 sigue ABIERTA** en decision; la evidencia nueva no cambia su veredicto. **Nivel propuesto: N2.**

## Ronda 2026-09-16 (2) — 4 lecturas: `mirza2003`, `fan2022`, `routt1997`, `macháček2023`

Elegidas entre los 15 PDF sin ficha: la tercera fuente de la escala del benchmark (`mirza2003`), la validacion que
`karageorgos2024ddpm` y `haneda2025aapm` atribuyen a `fan2022`, la fuente de Moed para "S2 es menor" (`routt1997`) y el
LDM condicionado por mascara mas cercano al renderizador (`macháček2023`). Informes de `lector-papers` contrastados
contra `main.tex:48`, `main.tex:50`, `main.tex:52`, `peters2025hybrid.md`, `smith2006iliosacral.md` y
`zwingmann2009navigated.md`. `main.tex`, `00-tesis.md` y `01-decisiones.md` sin tocar.
**Resultado: una implicancia nueva (#68), una actualizacion (#67) y tres lecturas sin implicancia ABIERTA.**

### 68 — La escala de cuatro grados del benchmark aparece literal en `mirza2003`, que la declara heredada; `main.tex:52` salta de los seis tramos de Gertzbein a los cuatro grados sin ese eslabon, y los llama "lettered" — ABIERTA

- **Origen:** ficha `mirza2003.md`, 2026-09-16, PDF completo (Spine 28(4):402-413). Es la ref. 8 de
  `smith2006iliosacral`, que cita tres fuentes para su escala: Vaccaro 1995 (ref. 6), Gertzbein 1990 (ref. 7) y Mirza
  2003 (ref. 8).
- **Hallazgo 1 — primera fuente leida con la forma exacta del benchmark.** Grado 0 = 0 mm, 1 = >0 y <2 mm, 2 = >2 y
  <4 mm, 3 = >4 mm (p. 405); leyenda de la Fig. 5: *"0: no perforation, 1: <2mm, 2: 2-4mm, 3: >4mm"* (p. 407).
  Grados **numerados**, no letras (las letras A/B/C de su Tabla 3 son grupos de Tukey).
- **Hallazgo 2 — tampoco es el origen.** *"The thresholds reported in prior studies were used"* (p. 405), con las
  refs. Gertzbein & Robbins 1990 y **Vaccaro 1995 Part II**. Como Gertzbein publica seis tramos, **Vaccaro 1995 es el
  unico nodo sin leer** que podria contener los cuatro grados antes de 2003.
- **Hallazgo 3 — los propios autores niegan validez a los cortes, y eso REFUERZA la decision vigente.** Dicen que esos
  umbrales *"do not apply to the thoracic spine"* y *"are likely different for different directions"*, y que en
  cadaver no se pueden definir umbrales de lesion (p. 411). Es la frase mas fuerte leida a favor de tratar el ancho de
  2 mm como convencion geometrica, y es de una fuente de la propia cadena.
- **Que toca en `main.tex:52`** (hoy: *"\citet{gertzbein1990} tabulate canal encroachment ... in six 2~mm bins rather
  than four lettered grades"*):
  - La frase **no es falsa** sobre Gertzbein, pero deja sin nombrar donde aparecen los cuatro grados.
  - **"lettered" es inexacto** para la escala del benchmark: Zwingmann (*"Grade 0 ... Grade 1 ..."*, p. 1835) y Mirza
    usan numeros. La escala con letras es la de `zhang2026pediclescrew` (Grade A), que no esta en esta cadena.
- **Hallazgo 4 — regla de borde no definida.** Mirza no dice a que grado van exactamente 2 y 4 mm (usa >2 y <4).
  Zwingmann escribe *"less than 2 mm"*, *"between 2 and 4 mm"*, *"greater than 4 mm"*: 2.0 cae en grado 2, pero 4.0
  queda ambiguo. **SAP necesita una regla explicita** (p. ej. `[0,2) / [2,4] / (4,inf)`), declarada como convencion.
- **No usar como prior:** sus distribuciones (fluoroscopia estandar 80/9/5/6%, StealthStation 95/0/1/4%; Tabla 3,
  p. 410) son de tornillos **toracicos en cadaver**, medidos con calibrador en diseccion. No compiten con Zwingmann.
- **Inconsistencias internas** (no citar sin aclarar): cirujano A *"31 (91%)"* sobre 35; rango inferolateral 1-5.1 mm en
  texto frente a 1.7-5.1 mm en Tabla 4; perforacion inferolateral 15% en Discusion frente a 14% en Tabla 3.
- **Opciones para la autora:**
  - (a) Corregir `main.tex:52`: "four lettered grades" -> "four numbered grades", y anadir que la version de cuatro
    grados aparece en \citet{mirza2003}, que declara los cortes heredados y *"likely different for different
    directions"*. Recomendada: refuerza la frase de convencion geometrica con la fuente de la propia cadena.
  - (b) (a) + leer Vaccaro 1995 Part II para cerrar la cadena. **Aviso:** el punto 9 de Fuera de alcance cierra la
    cadena del **10 mm**, no la de la escala; pero la escala ya esta declarada como convencion, asi que leer Vaccaro solo
    mejora la atribucion, no cambia el metodo.
  - (c) Solo corregir "lettered" y no nombrar a Mirza.
  - En todos los casos: fijar la regla de borde de SAP (hallazgo 4) y escribirla en la definicion de la metrica.
- **Tipo:** REDACCION (benchmark) + decision de implementacion menor. Amplia #58. **Nivel propuesto: N1** (es el
  eslabon donde aparece la forma exacta del benchmark ordinal).

### 67 — ACTUALIZACION tras leer `mirza2003` (2026-09-16): las fuentes de la escala miden a resoluciones distintas

- `mirza2003` mide la perforacion **con calibrador en diseccion**, con minimo medible de 0.2 mm; la unica CT con
  parametros es la preoperatoria de navegacion (cortes de 2 mm cada 1.3 mm). `herman2016` mide en CT de 2 mm y
  `tejwani2014` en CT de 2.5 o 5.0 mm. Protocolo de CT de `zwingmann2009navigated`: sigue sin registrar en su ficha.
- **Precision del hallazgo, para no inflarlo:** Mirza **no calibra** los cortes (los hereda), asi que esto no dice que
  los cortes se derivaron por diseccion. Lo que muestra es que **una misma escala se aplica con instrumentos de
  resolucion muy distinta** entre estudios, lo que sostiene la cautela de #67 sobre comparar SAP en voxel submilimetrico
  con grados clinicos. #67 sigue ABIERTA; su accion (verificar el protocolo de CT de Zwingmann 2009) no cambia.

### Sin implicancia ABIERTA — `fan2022`, `routt1997`, `macháček2023` (registro por regla 13)

- **`fan2022`:** sin cambio sobre `main.tex` ni sobre el baseline.
  - `karageorgos2024ddpm` le atribuye validar que CatSim produce artefactos realistas; **el PDF no compara con datos
    reales** (solo re-simulacion sin calcio frente a la original, Fig. 2). `main.tex:50` no usa esa atribucion: se apoya
    en la validacion con fantoma de `peters2025hybrid`. Anotado en la fila de `_index.md`.
  - "Freq. Boost" sin parametros en `fan2022`, pero `peters2025hybrid` describe su construccion (filtro 1D asignado
    radialmente en Fourier, 2.3, p. 3). No bloquea la adopcion del protocolo.
  - **#57:** mide blooming de calcio como aumento del volumen umbralizado (36% a 140 kVp, 68% a 80 kVp, p. 1230415-4),
    **no extension en mm**, y los autores advierten dependencia del umbral. Cuarta fuente de simulacion sin cifra de
    alcance espacial; el *"remains unmeasured in the literature"* de `main.tex` sigue en pie.
  - **Verificacion pendiente, baja prioridad:** `fan2022` suma sinogramas de paciente y calcio de forma lineal,
    justificado por *"minimal beam hardening impact"* del calcio, lo que no vale para metal. Conviene confirmar en el PDF
    de `peters2025hybrid` que paciente y metal se proyectan juntos con el espectro de 12 energias (su ficha registra el
    espectro, no si la proyeccion es conjunta).
- **`routt1997`:** opinion experta sin datos. *"The second sacral 'safe zone' is smaller"* (leyenda Fig. 2, p. 207) es
  compatible con `main.tex`, que ya evita una jerarquia universal S1/S2 y mide el corredor por volumen. No da `c`, ni
  escala, ni tasas, ni protocolo de CT. Nota de fidelidad: `moed2006s2screw` lo cita bien para S2 y para las vistas, y
  solo en parte para "el dismorfismo limita el espacio en S1".
- **`macháček2023`:** encaja en la familia "Globally conditioned" de `main.tex:48` (genera la imagen completa desde
  ruido), confirma la delimitacion y no reduce la novedad de B_delta. Si se cita junto a DiffBoost, *"using the mask
  only as an edge constraint"* debe quedar solo para DiffBoost (Machacek condiciona por region).

## Ronda 2026-09-16 (3) — adopcion de recomendaciones por orden de la autora y re-verificaciones

### 69 — `zwingmann2009navigated`: el brazo NAVEGADO no nombra S1, y "one screw in all patients" contradice los conteos 26/24 y 35/32 — ABIERTA

- **Origen:** re-verificacion dirigida con `lector-papers` (2026-09-16), seccion "Verificacion 2026-09-16" al final de
  `zwingmann2009navigated.md`. Se pidio para #67 (protocolo de CT) y trajo esto ademas.
- **Hallazgo 1 — nivel sacro por brazo.** Convencional: S1 explicito, *"a guide wire was placed across the ileum into the
  S1 vertebra"* (p. 1835). Navegado: **nivel NO ENCONTRADO EN EL PDF**; el criterio habla de *"respective sacral end
  plate"*. S2: NO ENCONTRADO.
  - **Toca la delimitacion vigente** (00-tesis.md, #12/#28): *"comparacion contra las DOS distribuciones ... solo en
    S1"*, y `main.tex:52` y `:78` (*"applies to S1"*, *"conditioned on surgical technique within S1"*). Para el brazo
    convencional esta respaldado; para el navegado es una **inferencia** (de la ficha original: *"un tornillo por
    paciente, en S1"*), no una frase del PDF.
- **Hallazgo 2 — contradiccion interna.** *"we used only one screw in all patients"* (Discussion, p. 1837) frente a 26
  tornillos en 24 pacientes y 35 en 32 (Abstract, p. 1833). Algunos pacientes recibieron mas de un tornillo y el paper no
  lo explica. Las distribuciones son **por tornillo**; no son independientes por paciente.
- **Opciones para la autora:**
  - (a) Mantener "S1" para ambos brazos declarando en `main.tex` que el nivel del brazo navegado no se reporta y se asume
    S1 por el algoritmo de tratamiento descrito.
  - (b) Restringir la afirmacion textual de S1 al brazo convencional y describir el navegado como "sacral level not
    reported".
  - (c) (a) o (b) + declarar que los grados son por tornillo con pacientes con mas de un tornillo.
- **No aplicado** a `main.tex` (regla 14): es hallazgo nuevo, no parte de las recomendaciones adoptadas.
- **Tipo:** SUPUESTO del benchmark. **Nivel:** toca fuente N1.

### 67 — APLICADA en `main.tex` (2026-09-16) — y el grosor de corte de Zwingmann es NO ENCONTRADO

- Re-verificacion: escaner, grosor de corte, intervalo, kernel, plano y herramienta de medida: **NO ENCONTRADO EN EL PDF**.
  Un solo radiologo coautor (*"one independent radiologist (EK) not involved in the treatment"*, p. 1835), sin acuerdo
  interobservador. La opcion de re-muestrear a su grosor queda **imposible**; se aplica la de declarar la limitacion.
- **Escrito en `main.tex:52`:** radiologo unico, protocolo no reportado, bordes 2/4 mm no definidos, tendencia de
  `tejwani2014` con *P* = .3 declarada como tal, y lectura del benchmark como acuerdo entre distribuciones a resolucion de
  referencia desconocida.

### 68 — APLICADA en `main.tex` (2026-09-16), opcion (a) + regla de borde

- `main.tex:52`: "lettered" -> "numbered"; frase nueva con `mirza2003` (forma de 4 grados literal, cortes heredados,
  medido en cadaver toracico, umbrales *"do not apply to the thoracic spine"* y *"likely different for different
  directions"*).
- Fila SAP de la tabla: grado 0 sin perforacion, 1 `(0,2)`, 2 `[2,4]`, 3 `(4,inf)` mm, **declarado como convencion**.
  La re-verificacion confirma que Zwingmann no define los bordes (NO ENCONTRADO EN EL PDF).
- Vaccaro 1995 Part II sigue PENDIENTE en `_candidatos.md`.

### 64 y 66 — APLICADAS en `main.tex` (2026-09-16), opcion (a) en ambas

- **#64:** Objetivo 2 dice ahora densidad leida del HU de cada volumen, motivada por la heterogeneidad de masa osea del
  modelo poblacional de `arand2019pelvicring` (parafrasis del *"so-called alar void"*; no es cita textual). `main.tex:52` sin cambio.
- **#66:** Objetivo 1 y fila `Representation Viability`: error de ida y vuelta tambien dentro de `B_delta` en volumenes con
  metal, descriptivo y fuera del Go/No-Go. **Pendiente de ejecucion:** anadir el ROI a `e6b_vae_sd15.py` y correr en Khipu.

### 65 — NO aplicada, por decision de la autora (2026-09-16): se espera el raw de las actas

- La decision 2026-09-15 (3) exige el raw de PMLR antes de citar `chen2026foundationvae` en `main.tex`. La autora eligio
  esperarlo. Frase preparada en `01-decisiones.md`.

### 70 — `peters2025hybrid` no dice si paciente y metal se proyectan juntos, y su validacion con fantoma no cubre el paso hibrido ni la geometria usada para generar datos — ABIERTA

- **Origen:** re-verificacion dirigida con `lector-papers` por orden de la autora (2026-09-16), seccion "Verificacion
  2026-09-16" de `peters2025hybrid.md`. Motivo: `fan2022` (origen del filtro de Peters, ref. 45) suma sinogramas de
  paciente y calcio de forma lineal, justificado solo para calcio.
- **Proyeccion conjunta: NO ENCONTRADO EN EL PDF**, en ningun sentido. Lo que hay: el metal se inserta en la imagen
  clinica (*"virtual metal objects were then inserted in random soft tissue or bone positions"*, 2.3, p. 4), esas imagenes
  son la entrada de la simulacion, espectro de 12 energias (2.1, p. 3), y cada caso trae *"a sinogram with and without
  metal"*. Insertar en imagen **sugiere** proyeccion conjunta; es inferencia. Conversion HU -> materiales: NO ENCONTRADO
  (solo *"water beam hardening correction"*). Volumen parcial: NO ENCONTRADO.
- **Filtro:** cociente empirico original/simulado en Fourier promediado en polar sobre 64 cortes, citando `fan2022`;
  curva, frecuencias y ganancias no publicadas.
- **Validacion:** fantoma fisico CIRS de torax con varillas, escaneado en Lightspeed VCT contra su simulacion, 4
  configuraciones; numero CT medio < 2%, ruido < 10% sin artefacto y hasta 13.3% con artefacto; *"Strong streak artifacts
  ... well-replicated"* (3.1, p. 6). **No cubre** el paso hibrido (imagen clinica + filtro) ni la geometria generica
  (vendor-neutral) de los datos de entrenamiento; el paper limita: *"for the specific CT scanner setup used here"*
  (Discussion, p. 9). Geometria 2D, *"1 detector row with 900 columns"*.
- **Que toca en `main.tex`:**
  - `main.tex:50`: *"Their phantom validation supports the evaluated simulation settings"* es **generoso**: soporta la
    simulacion del escaner del fantoma, no el protocolo hibrido tal como se usa.
  - `main.tex:117` ya es prudente (*"two-dimensional"*, *"does not inherit its validation automatically"*, *"artifact
    realism ... requires separate evaluation"*): sin cambio necesario.
- **Opciones para la autora:**
  - (a) Reescribir `main.tex:50`: *"Their phantom validation covers the simulated scanner geometry against a physical
    scan; it does not cover the hybrid step (clinical image input with frequency compensation), does not report whether
    patient and metal are projected jointly, and does not establish ... "*. Recomendada.
  - (b) (a) + verificar la proyeccion conjunta en el codigo de XCIST o en los Supplements de Peters antes de reproducir.
    Es condicion practica de la reproduccion que ya promete `main.tex:117`.
  - (c) Sin cambio.
- **Resuelve** la "verificacion pendiente, baja prioridad" registrada con `fan2022` (ronda 2026-09-16 (2)): no se puede
  confirmar con el PDF.
- **Tipo:** REDACCION / SUPUESTO del baseline fisico. Fuente N1.

### 71 — `li2024` (Quad-Net) debilita la primera salvedad de `main.tex:56`, describe el artefacto como "global" y usa multi-ventana solo en la perdida — ABIERTA (actualiza #61/#63, #57, #24)

- **Origen:** ficha `li2024.md`, 2026-09-16, PDF completo. **Aviso del lector:** cifras de tablas leidas de imagen poco
  nitida; varias cuadran con diferencias que el texto si enuncia (0.31, 0.49, 0.64 dB). Verificar antes de citar.
- **#61/#63 — la salvedad 1 de `main.tex:56` pierde fuerza.** `main.tex:56` relativiza `lin2019` porque su variante de
  imagen *"is fed a reconstruction of an already-interpolated sinogram"*. En Quad-Net el brazo solo-imagen (LU-Net) parte
  de la reconstruccion del sinograma **corrupto**: *"The second group works only in the image domain with metal-corrupted
  images as input"* (Sec. IV-B, p. 1871). Tabla I (media): LU-Net 38.59 dB frente a Quad-Net 41.78 dB; metal grande 33.87
  frente a 39.42 dB (diferencias calculadas por el lector, no enunciadas). Frase mas fuerte que la de `lin2019`: *"Working
  in a single domain cannot effectively recover the true tissues from corrupted data."* (Sec. I, p. 1866). **Sigue siendo
  REMOCION** y "cannot effectively" es rendimiento: la salvedad 2 (asimetria remocion/generacion) queda intacta y pasa a
  ser el unico sosten.
- **#57 — tension cualitativa con B_delta.** *"the metal artifacts on the reconstructed images are present globally"*
  (Sec. I, p. 1866). Sin cifra. Refuerza que una banda de ~12 mm **trunca** el streaking lejano por diseno; hay que
  declararlo como eleccion o justificar el radio. (`main.tex:48` ya dice *"propagate globally far beyond"*, que es la
  tension original de #57.)
- **#24 — precision sobre el precedente multi-ventana.** Quad-Net usa 3 ventanas (WL/WW 500/3000, -600/800, 50/500) **solo
  en la perdida y la evaluacion**; entrada normalizada a un rango unico [-1000, 2000] HU; ablacion +0.64 dB. Coincide con
  `wang2025adaptiveweighting` (lo propio de AdaW es el peso de la perdida por ventana). Umbral de 2500 HU sin fuente.
  **Efecto:** los precedentes leidos usan multi-ventana en supervision/reconstruccion por ventana, no como codificacion de
  entrada para un autoencoder. Puede afinar la formulacion de la novedad (punto 4 de Fuera de alcance), sin reclamarla de
  nuevo.
- **Snowballing:** cita Niu, Li y Wang, SPIE 11840, 2021, que ya esta PENDIENTE en `_candidatos.md`; discrepancia de cita
  (titulo "Multi-window" vs "Multiple window", autores, mes) frente a `wang2025adaptiveweighting`.
- **Opciones para la autora:**
  - (a) Anadir `li2024` a `main.tex:56` como evidencia sin el sesgo de interpolacion y dejar la asimetria
    remocion/generacion como unica salvedad. Recomendada (fidelidad).
  - (b) Declarar en Objetivo 3 que `B_delta` trunca por diseno el streaking lejano.
  - (c) Precisar en la formulacion de novedad que el multi-ventana previo es de supervision, no de codificacion de entrada.
- **No aplicado** (regla 14). **Tipo:** REDACCION / GAP (#61). **Nivel propuesto: N2** (N1 defendible por #61).

### Sin implicancia ABIERTA (ronda 2026-09-16 (3)) — registro por regla 13

- `templeman1996proximity` (solo abstract): sin % de malposicion en el abstract; confirma que el 2%-15% no es citable desde
  ahi. Rango ya RETIRADO.
- `abadi2019` (DukeSim): no simula ni valida metal; `main.tex` no lo cita.
- `singhrao2024fiducial`: fiduciales en CT sintetica de densidad asignada, sin HU de error; N3. Candidato Szalkowski 2021.
- `yu2021`: sin brazo solo-imagen aislado; umbral de 2000 HU (ya decidido #22); preservacion fuera de `B_delta` ya medida.
- `kazerouni2023diffusionsurvey`: ningun trabajo de metal o MAR con difusion; corte oct 2022; PDF es preprint v3.
- `dorjsembe2024`: familia "Globally conditioned", condiciona por region; confirma `main.tex:48`.

### 72 — `hu2023` es una tercera familia (analitica) que SI modifica voxeles fuera de la lesion: la frase de "dos familias" de `main.tex:48` debe acotarse a difusion — ABIERTA

- **Origen:** ficha `hu2023.md` (Label-Free Liver Tumor Segmentation, CVPR 2023), 2026-09-16, PDF completo.
- **Hallazgo:** sintesis **analitica**, sin aprendizaje (textura gaussiana, mezcla con fondo, recorte a [-21, 189] HU).
  Fuera del tumor modela **efecto de masa**: desplazamiento de tejido hasta 1.3r (Tabla 1), aunque segun la Fig. 3 algunos
  pasos *"are only used for Visual Turing Test (not for training)"*. Es un cambio geometrico, no un artefacto de
  adquisicion, pero **si cambia intensidades fuera del objeto por diseno**.
- **Que toca:** `main.tex:48`: *"State-of-the-art lesion synthesis models fall into two families, and neither represents
  the intensity changes that the synthesized object induces outside itself."* El parrafo abre hablando de difusion, pero
  la frase es general. Con `hu2023` como contraejemplo la afirmacion universal no se sostiene literalmente.
- **Opciones para la autora:**
  - (a) Acotar: *"State-of-the-art diffusion-based lesion synthesis models fall into two families ..."* y, si se quiere,
    precisar *"acquisition-induced intensity changes"*. Recomendada: cambio de pocas palabras.
  - (b) (a) + mencionar el polo analitico con `hu2023` y su efecto de masa como cambio geometrico, no fisico.
- **Precedente de evaluacion sin downstream:** Visual Turing Test debil (2 lectores, 50 CT, "unsure" excluido, sin
  criterio preinscrito, inconsistencias en Tabla 2). Si la tesis usa lectores, preinscribir trato de "unsure" y umbral.
- **Muestreador:** colocacion por propuesta uniforme + rechazo por vasos; analogia util, sin datos clinicos de ubicacion.
- **No aplicado** (regla 14). **Tipo:** REDACCION. **Nivel propuesto: N2.**

### 73 — La apariencia del artefacto real depende de la reconstruccion (MAR del fabricante, monoE, kernel), y el protocolo de CLINIC-metal no esta documentado — ABIERTA

- **Origen:** ficha `selles2024marreview.md` (Eur J Radiol 2024), 2026-09-16, PDF completo.
- **Hallazgo:** los MAR de fabricante y las imagenes monoenergeticas cambian el artefacto y anaden artefactos secundarios:
  *"found secondary artifacts in 82 % of the images with O-MAR"* (Sec. 3.2.2, p. 3); el efecto *"varies by vendor"*
  (Sec. 3.5, p. 6). Tabla 1: osteosintesis como *"Medium artifacts"*, protesis grandes de alta densidad como *"Severe"*
  (clasificacion cualitativa).
- **Cruce con el repo:** `liu2021ctpelvic1k.md`: kVp, mAs, algoritmo de reconstruccion y fabricante concreto **NO
  ENCONTRADO EN EL PDF**; `02-datos.md` no registra reconstruccion ni MAR.
- **Por que importa:** el renderizador aprende la apariencia del artefacto de CT reales de CLINIC-metal, y la evaluacion
  de coherencia fisica la compara contra el brazo de Peters (FBP/FDK sin MAR de fabricante). Si parte de los CT reales
  vienen con MAR o monoE, **el objetivo de apariencia mezcla artefacto fisico con artefacto de post-proceso**, y la
  comparacion con el brazo fisico no es homogenea.
- **Opciones para la autora:**
  - (a) Revisar si los volumenes o la documentacion del dataset conservan metadatos (DICOM originales, pagina del
    dataset) y anotar en `02-datos.md` lo que haya o "no documentado". Recomendada: barata.
  - (b) (a) + declarar en `main.tex` (Datasets) que la reconstruccion de los CT con metal no esta documentada y puede
    incluir MAR de fabricante.
  - (c) Sin accion.
- **#57 y #2:** el survey no resuelve ninguna (sin extension espacial en mm, sin multi-ventana ni sintesis).
- **Tipo:** SUPUESTO (datos del Objetivo 3). **Nivel propuesto:** N3 para el paper; la implicancia toca fuente N1
  (`liu2021ctpelvic1k`).

### 74 — ControlNet presupone el modelo base y su VAE congelados: si #36/#39 obliga a cambiar el VAE, la justificacion de ControlNet con "Stable Diffusion 1.5 backbone" pierde su fuente — ABIERTA (liga con #36/#39)

- **Origen:** ficha `zhang2023controlnet.md`, 2026-09-16, PDF arXiv v3 (sin suplementario; version ICCV no verificada).
- **Hallazgo:** el valor de ControlNet es reutilizar un base congelado preentrenado a gran escala; las zero convolutions
  hacen que el modelo parta sin cambios (*"evaluate to zero"*, §3.1, p. 4), y todo opera sobre el latente 64x64 del VAE de
  SD (§3.2, p. 5). **Cambio de VAE o reentrenamiento del U-Net base: NO ENCONTRADO EN EL PDF.** Datos limitados: *"small
  (<50k)"* (Abstract) y *"limited 1k images"* (§4.5, p. 8), esta ultima con una sola figura cualitativa en imagen natural
  con el base intacto. *"All models are trained with general-domain data"* (Fig. 7, p. 6). Coste: *"200k training samples,
  one single NVIDIA RTX 3090Ti, and 5 days"* (§4.3, p. 7).
- **Cruce con el repo:** `main.tex:79` fija *"2.5D ControlNet-guided Latent Diffusion Model (Stable Diffusion 1.5
  backbone)"*. E6b mostro que el VAE de SD 1.5 congelado falla el Go/No-Go en 178/178 (#36/#39) y la via principal pendiente
  es la opcion 3 (otro VAE). **Inferencia, no frase del paper:** con otro latente, el U-Net de SD 1.5 ya no es reutilizable
  sin reentrenar, y la premisa de ControlNet (base preentrenado congelado) deja de sostenerse con esta fuente; las cifras de
  "<50k / 1k" tampoco respaldan 65 pacientes con cortes 2.5D correlacionados.
- **Localidad:** *"spatially localized"* (§1, p. 2) no se define ni se mide; la senal de control se suma en toda la imagen.
  Ya cubierto por la fila *Preservation outside B_delta* de `main.tex` (sin accion nueva).
- **Opciones para la autora (decidir junto con #36/#39):**
  - (a) Si se elige un VAE distinto: decidir entre reentrenar base + ControlNet o condicionar directamente (concatenacion
    de mascara en un LDM entrenado desde el nuevo latente), y actualizar `main.tex:79` quitando *"Stable Diffusion 1.5
    backbone"*.
  - (b) Si se elige un base preentrenado cuyo VAE pase el Go/No-Go: ControlNet se conserva tal cual.
  - (c) No citar las cifras de "<50k / 1k" como respaldo de viabilidad con la cohorte local.
- **No aplicado** (regla 14). **Tipo:** SUPUESTO / arquitectura del Objetivo 3. **Nivel propuesto: N2** (sube desde N3).

### 75 — `rombach2022latentdiffusion` respalda E6b y #66 con frase propia, apoya la opcion 3 de #36/#39 solo en tendencia, y NO nombra Stable Diffusion ni el rango [-1,1] — ABIERTA (actualiza #36/#39/#66)

- **Origen:** ficha `rombach2022latentdiffusion.md`, 2026-09-16, PDF completo (45 pp., arXiv v2).
- **Respaldo de E6b:** el autoencoder *"can become a bottleneck for tasks that require fine-grained accuracy in pixel
  space"* (§5, p. 9); entrenado con perdida perceptual + adversarial sobre RGB natural (OpenImages, Tabla 8). Sin HU ni
  error absoluto de intensidad: coherente con 178/178, sin medirlo.
- **Respaldo de #66 (ya aplicada):** la primera etapa *"removes high-frequency details"* (§1, p. 2), y PSNR/SSIM *"favor
  blurriness over imperfectly aligned high frequency details"* (§4.4, p. 8). **Es la cita que le falta a la frase de #66**
  en `main.tex:77`, hoy sin fuente.
- **Opcion 3 de #36/#39, solo tendencia:** Tabla 8 (KL): f=8/4 canales 24.19, f=4/3c 27.53, f=2/2c 32.47 dB PSNR; con f
  fijo, mas canales ayudan. RGB natural, sin HU; f=1-2 difunde lento (§4.1). No dice si algun f alcanza 25 HU.
- **Riesgo de cita:** **Stable Diffusion 1.5: NO ENCONTRADO EN EL PDF**; la fila f=8/KL/4c coincide con su VAE, pero la
  identidad no se verifica aqui. **Rango [-1,1]: NO ENCONTRADO.** `main.tex:79` nombra *"Stable Diffusion 1.5 backbone"*
  sin cita; si se cita, no puede ser a `rombach2022` para el nombre del modelo.
- **Opciones para la autora:**
  - (a) Citar `rombach2022latentdiffusion` en la frase de #66 (`main.tex:77`) con §1/§5. Recomendada: una cita, cero riesgo.
  - (b) Usar la Tabla 8 como motivacion cualitativa de la opcion 3 (menor f / mas canales), sin cifras en HU.
  - (c) No atribuir a este paper ni SD 1.5 ni el rango de entrada.
- **No aplicado** (regla 14). **Tipo:** REDACCION / respaldo de metodo. **Nivel propuesto: N2** (sube desde N3).

## Ronda 2026-09-17 — decisiones delegadas al asistente (rol de asesor)

Detalle completo en `01-decisiones.md`, entrada 2026-09-17. La autora rechazo recortar el renderizador; todo se decidio
dentro de esa restriccion. Estado resultante:

| # | Estado |
|---|---|
| 36, 39, 74 | DECIDIDA via: decodificador adaptado con encoder congelado; **pendiente de P1** (compuerta del Objetivo 1, regla preinscrita: si no pasa, no hay Objetivo 3) |
| 57, 61, 63, 65, 66, 69, 70, 71, 72, 73, 75 | **APLICADAS** en `main.tex` (2026-09-16/17) |
| 62 | CERRADA sin cambio |
| 55 | CERRADA como declarada |
| 70 | Aplicada en redaccion; **pendiente P2** (proyeccion conjunta en el codigo de XCIST) |
| 53 | Plazo de 2 semanas; si no vuelve el revisor, se declara |

**Efecto medido:** `main.tex` compila con 0 errores, 0 citas indefinidas y 64 referencias, pero **pasa de 5 a 6 paginas**.
Si hay limite de paginas, el recorte natural es el parrafo del supuesto de dominio imagen (`main.tex:56`) y la frase de
Mirza. Sin implicancia nueva sobre el argumento.

