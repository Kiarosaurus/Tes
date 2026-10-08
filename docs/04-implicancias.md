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

### 76 — La regla operativa del Go/No-Go de P1 (fijada el 2026-09-17) no esta escrita en `main.tex` e introduce comparacion multiple: seis combinaciones, basta con que pase una — DECIDIDA Y APLICADA (2026-09-17)

- **Origen:** preparacion de P1 (`experiments/objetivo1/p1_decodificador_sd15.py`), 2026-09-17. Antes de escribir codigo
  la autora fijo, **sin haber visto resultados**: (i) las tres configuraciones (`pub`, `LW20000`, `pub+asinh`) con un
  decodificador afinado por cada una, **Go si alguna pasa**; (ii) lectura de HU `vae regla`; (iii) estadistico = media
  por paciente del MAE en hueso < 25 HU; (iv) poblacion = los 34 pacientes de test, estratificados.
- **Hallazgo 1 (redaccion):** `main.tex:77` dice *"evaluated on held-out patients for the pretrained autoencoder and for a
  decoder-adapted variant"*, pero no nombra la configuracion de ventanas, la lectura de HU (oraculo o regla), el
  estadistico (media, mediana, todos) ni la poblacion. Esas cuatro elecciones cambian el veredicto y hoy solo estan en
  el docstring del script y en el chat. Una regla preinscrita que no esta en el documento no se puede auditar.
- **Hallazgo 2 (supuesto / validez):** con 2 modelos x 3 configuraciones hay **seis oportunidades** de pasar. No se
  corrige por multiplicidad. Con 34 pacientes y una media de puntos, una combinacion puede quedar bajo 25 HU por azar de
  muestreo aunque su IC95 cruce el umbral. El script reporta IC95 bootstrap por paciente pero, por la regla elegida, **no
  decide** con el.
- **Hueco nuevo:** si pasan dos o mas combinaciones, **no hay regla para elegir cual usa el Objetivo 3**. Elegirla despues
  de ver las cifras repite el patron #25/#37/#45/#47/#50.
- **Opciones para la autora:**
  - (a) Escribir en `main.tex:77`, antes de lanzar la cohorte, las cuatro elecciones y la frase de multiplicidad. Recomendada.
  - (b) Fijar ya la regla de desempate (p. ej., menor media de MAE en hueso con `vae regla`; o preferencia a priori por
    `pub+asinh`, codificacion exacta) y registrarla en `01-decisiones.md`.
  - (c) Reportar el IC95 junto al veredicto y declarar en limitaciones que la compuerta no corrige por multiplicidad.
- **No aplicado** (regla 14). **Tipo:** REDACCION + SUPUESTO / criterio del Objetivo 1. **Nivel propuesto: N1** (toca la
  compuerta que decide si existe el Objetivo 3).
- **Decision (asistente como asesor, orden explicita de la autora, 2026-09-17):** (a) + (b) + (c), sin tocar el
  estadistico que eligio la autora (media puntual).
  - (a) La regla completa queda en `main.tex:77` (34 pacientes de test estratificados; dos variantes x tres codificaciones
    nombradas, ventanas de `wang2025adaptiveweighting`; lectura sin verdad; media por paciente < 25 HU; basta una de seis).
    Fila *Representation Viability* de la tabla ajustada a lo mismo.
  - (b) Desempate **a priori, no por error**: `pub+asinh`, `LW20000`, `pub` (techo de 2000 HU recorta el metal); dentro de
    cada una, preentrenado antes que afinado. Elegir por menor MAE seria seleccionar sobre el test.
  - (c) Multiplicidad declarada sin corregir; IC95 bootstrap por paciente junto a cada veredicto; un pase con limite
    superior >= 25 HU se etiqueta **MARGINAL** y no cambia el veredicto.
- **Aplicado:** `main.tex` compila 0 errores, 6 paginas, 64 referencias, 0 citas indefinidas. `p1_decodificador_sd15.py`
  implementa (b) y (c) (`ORDEN_OBJ3`); probado con CSV sinteticos de 34 pacientes: NO-GO, GO con eleccion por orden (elige
  `pub+asinh` aunque `pub` tenga menor error) y GO MARGINAL (media 24.56, IC95 [20.00, 33.68]).


---

## Ronda 2026-09-17 (2) — lectura de las 8 fuentes nuevas de `refs/raw/` (asistente en rol de asesor, delegacion explicita)

**Encargo de la autora (2026-09-17):** leer la literatura nueva, pasar los raw a `clean`, evaluar si cambia la tesis y,
si hay que tomar decisiones cruciales, tomarlas registrando aqui las alternativas. Objetivo declarado: terminar la tesis
lo antes posible, conservando el renderizado.

**Fuentes:** `routt1997early`, `templeman1996proximity` (PDF nuevo, antes solo abstract), `noojin2000cross`,
`matta1996internal`, `vaccaro1995part1`, `vaccaro1995part2`, `zhu2023sinogram`, y una segunda copia de `gertzbein1990`.
Ocho lectores `lector-papers` en paralelo, cada uno escribio solo su ficha; `_index.md` y `_candidatos.md` los integro la
sesion principal.

**Veredicto global: ninguna de las ocho lecturas cambia el alcance, la hipotesis, los objetivos, el baseline, la compuerta
del Objetivo 1 ni el renderizador.** Todas caen en el Objetivo 2 (cadenas de citas del benchmark) o en el Related Work, y
confirman decisiones ya tomadas. `00-tesis.md`, `01-decisiones.md` y `02-datos.md` no necesitan cambios de fondo (ver el
final de esta ronda).

### 77 — Origen del "2%-15%" RESUELTO: el 2% es Routt 1997 y el 15% es la cita de Routt a una presentacion de Keating; Templeman no publica ningun porcentaje — CERRADA (sin cambio en `main.tex`)

- **Routt 1997** (`routt1997early.md`): 5 de 244 tornillos mal colocados, *"2.05 percent"* (p. 587). Criterio binario,
  sin mm ni grados; 240 tornillos en S1 y 4 en S2; fluoroscopia convencional.
- **El 15% es del mismo parrafo de Routt, pero no es de Routt:** lo atribuye a Keating (ref. 5, presentacion en la OTA
  de 1994, 6 errores en 40 pacientes). El articulo publicado de Keating (`keating1999iliosacral`) da **13% (5 de 38
  pacientes)**. El extremo superior de la banda sale de una cifra de congreso que no coincide con la version publicada.
- **Templeman 1996:** no trae ningun porcentaje de malposicion (ni 2, ni 15, ni 0-15). Da conteos: 5 de 57 tornillos
  entraban al foramen S1 **o tenian demasiado scatter para decidirlo**, y 1 perforacion anterior (p. 196). **La
  atribucion de `zwingmann2013` (*"2 to 15 %"*, *"0 to 15 %"*) no se sostiene en su fuente primaria.**
- **Que dice esto:** la banda junta una tasa binaria por tornillo (2.05%) con una cifra de congreso por paciente (15%).
  Son dos unidades y dos criterios distintos. Esto confirma el retiro del punto 5 de `Fuera de alcance` y cierra la
  auditoria historica que #12 y #25 habian dejado abierta.
- **Decision (asistente, delegada):** (c) sin cambios en `main.tex`.
  - (a) *Descartada:* una frase en `main.tex` con el origen de la banda. Documenta un rango que la tesis ya no usa y
    ocupa espacio en una propuesta de 6 paginas.
  - (b) *Descartada por ahora:* usar el 2.05% de Routt como contraste en *"Aggregate malposition rates and ordinal
    cortical-breach grades therefore measure different constructs"* (`main.tex:52`). Seria un buen ejemplo: la misma
    tecnica, fluoroscopia convencional casi toda en S1, da 2.05% "misplaced" contra 60% con algun grado >= 1 en el brazo
    convencional de Zwingmann. Pero `zwingmann2013` (2.6% contra 0.1%) ya sostiene el argumento. **Reabrir solo si un
    revisor lo discute.**
  - (d) *Descartada:* usar Routt como prior del brazo convencional. Es binario y mezcla S1 con S2, asi que no da los
    cuatro grados de SAP.
- **Tipo:** auditoria de procedencia. **Nivel:** N3.

### 78 — Vaccaro 1995 (Partes I y II) NO contiene la escala de cuatro grados: la cadena de #68 queda cerrada — CERRADA (sin cambio en `main.tex`)

- **Part II** (`vaccaro1995part2.md`): 90 tornillos toracicos en cadaver, 37 perforaron (21 medial, 16 lateral), CT de 5 mm
  y una sola lectora. Cada tornillo va a una de tres clases: medial, lateral o correcto (Tabla I, p. 1201). No hay cortes
  en mm. El unico umbral es el >4 mm de Gertzbein, citado (p. 1203). Su postura es *"any breach ... is unacceptable"*
  (p. 1205).
- **Part I** (`vaccaro1995part1.md`): morfometria de pediculos toracicos, sin escala. N4, fuera de alcance.
- **Consecuencia:** de las dos fuentes que `mirza2003` cita para *"The thresholds reported in prior studies were used"*,
  una (Gertzbein) tiene los cortes de 2 y 4 mm entre seis tramos, y la otra (Vaccaro II) no tiene ningun corte. **La forma
  de cuatro grados aparece por primera vez, entre lo leido, en Mirza 2003.** Que Mirza la construyera a partir de
  Gertzbein es una inferencia: el PDF no lo dice.
- **`main.tex:52` ya es correcto.** Atribuye la forma literal a Mirza, dice que declara los cortes heredados y adopta el
  ancho de 2 mm como convencion geometrica. Nada que corregir.
- **Decision (asistente, delegada):** sin cambios. #68 cerrada del todo.
  - (a) *Descartada:* anadir *"neither of the two sources Mirza cites publishes four grades"*. Refuerza la frase de
    convencion, pero no cambia el metodo y la frase ya esta blindada.
  - (b) *Descartada:* citar Vaccaro en `main.tex`. No aporta a ningun objetivo.
- **Segunda copia de Gertzbein** (`papers/gertzbein1990pedicularscrew.pdf`): mismo articulo; **todas las cifras de la
  ficha CONFIRMADAS**, dos citas del abstract corregidas a literal y el grosor de corte sigue NO ENCONTRADO.

### 79 — Templeman: el +-4 grados es trigonometria 2D idealizada, el 21.7 mm no es un diametro de corredor, y el artefacto impidio graduar 5 de 57 tornillos en CT postoperatoria — DECIDIDA (limitacion a declarar, sin cambio ahora)

- **+-4 grados** (p. 197): sale de suponer piel-ilion de unos 10 cm, ilion-cuerpo de 5 cm y un pediculo de 21 mm, con
  insercion y alineacion perfectas. Los propios autores advierten que la tolerancia es menor fuera del eje central. **Es
  un modelo, no un umbral medido.** `main.tex` no usa los 4 grados (usa las tolerancias de McLaren, 1.53 y 1.02 grados).
  Sin cambio.
- **21.7 mm (16.2-28.9):** es la dimension AP entre el foramen S1 y la cortical anterior, en corte axial. Los autores dicen
  que *"the 3-dimensional zone ... could not be determined"*. **No se compara con `D_TS`** (diametro inscrito perpendicular
  al eje, mediana 9.5 mm).
- **Hallazgo que si toca un supuesto:** con CT de 4 mm y ventana osea, en 5 de 57 tornillos no se pudo decidir la relacion
  con el foramen por *"too much scatter"* (p. 196), y cuando el artefacto tocaba una estructura se anotaba 0 mm. **Los
  grados clinicos de brecha se leen sobre CT con artefacto metalico.** Eso vale tambien para el benchmark de Zwingmann,
  cuyo protocolo de CT sigue NO ENCONTRADO (#67): las distribuciones objetivo pueden llevar un error de lectura que la tesis
  no controla.
- **Decision (asistente, delegada):** (b).
  - (a) *Descartada:* reabrir #67 como bloqueo. No cambia el metodo, porque SAP se mide sobre la pose conocida del
    tornillo sintetico, sin leer la imagen.
  - (b) **Elegida:** declararlo como limitacion del benchmark cuando se escriba la seccion de resultados del Objetivo 2
    (*"clinical grades are read on post-operative CT under metal artefact; Templeman et al. could not grade 5 of 57
    screws for scatter"*). Ademas es un argumento de motivacion para el renderizador: el artefacto oculta justo la relacion
    tornillo-cortical que se grada. No se toca `main.tex` ahora (regla 4).
  - (c) *Descartada:* usar Templeman como segundo benchmark. Es binario, solo S1 y parcial.
- **Tipo:** SUPUESTO (benchmark) + redaccion futura. **Nivel:** N2.

### 80 — Noojin y Matta: dos trampas de cifra registradas; ninguna cierra #7 — CERRADA (registro)

- **Noojin 2000:** 27.76 mm de alto y 28.05 mm de ancho son la **extension del contorno** del pediculo sacro en UN corte
  sagital oblicuo paralelo a la SI, de un solo lado, en 13 pacientes con CT de 5 mm. **No es un diametro inscrito
  perpendicular al eje del tornillo.** `D_TS` exige un cilindro continuo por ambas alas y el cuerpo, asi que por
  construccion es menor o igual. **28 mm no contradice 9.5 mm; no citar uno contra el otro.** Tampoco cuantifica la caida
  fuera del centro, asi que no da zona segura operacional y **#7 sigue como estaba** (cubierta operacionalmente por
  McLaren y Kaiser).
- **Matta 1996:** escala de REDUCCION, no de posicion de tornillo, con limites que no coinciden entre abstract y Metodos
  (4/5 mm; 10 mm cae en dos categorias). No evalua malposicion. Confirma la trampa de #12 (2026-09-08): **no citar Matta
  para SAP.**
- **Decision:** ninguna cita nueva en `main.tex`. **Sin cambio.**

### 81 — `zhu2023sinogram`: la parafrasis de Xie cambia el objeto de la critica al umbral, pero `main.tex` no depende de ella; #47 sigue CERRADA — CERRADA (registro)

- Zhu dice que el umbral simple sobre CT sin corregir *"can make the metal projection data inaccurate or cause difficulties
  in clinical applications"* (Sec. 2.2.1, p. 4). No habla de segmentacion, no cita a nadie y no compara contra ningun
  umbral. Xie lo cita como *"inaccurate metal segmentation"*.
- **`main.tex:54` (C1) no usa esa parafrasis.** Cita a Xie por su propia sobrecobertura en cortes simulados (p. 6, Tabla 2)
  y a la auditoria local E8. Asi que #47 no se reabre.
- **Aporte lateral:** Zhu es otro ejemplo de metal simulado sobre CT limpio (DeepLesion; titanio; Spektr 120 kVp, XCOM,
  beam hardening y photon starvation; sin scatter) **para entrenar MAR, no como aumentacion para segmentacion**, y sin
  datos clinicos con metal. Entra en la familia de simuladores fisicos que `main.tex:48`/`:54` ya describe. No da el
  alcance espacial del artefacto en mm: el *"remains unmeasured"* de #57 sigue en pie.
- **Decision (asistente, delegada):** no citar.
  - (a) *Descartada:* citarlo en Related Work como simulador de insercion. Hay fuentes mas directas ya leidas
    (`peters2025hybrid`, `ren2022metalinsertion`) y no aporta al renderizador.
- **Snowballing:** Park 2015 (caracterizacion matematica del beam hardening) queda PENDIENTE N2 en `_candidatos.md`. Es la
  unica pista nueva hacia la estructura espacial del artefacto (#57). **No se lee salvo que sobre tiempo.**

### 82 — Duplicados en `refs/raw/` y `\nocite{*}`: la bibliografia sube a 70 entradas, seis de ellas sin citar — DECIDIDA en parte (aplicacion en `main.tex` pendiente de orden)

- **Duplicados:** `gertzbein1990pedicularscrew.nbib` y `templeman1996iliosacralscrews.nbib` son copias identicas (`diff`
  vacio) de raws que ya existian. **Decision (asistente): no se crean claves nuevas.** Los PDF nuevos se asocian a
  `gertzbein1990` y `templeman1996proximity` (`refs/MAPEO.md`).
  - *Descartadas:* crear las dos entradas (la referencia saldria duplicada en la bibliografia); borrar los raw (la regla 9
    dice que el raw no se toca y que la lista la define la autora).
  - **Pendiente de la autora (opcional):** borrar esos dos raw o renombrar los PDF a la clave. No cambia `refs.bib`.
- **`\nocite{*}` (`main.tex:139`):** las seis altas entran a la bibliografia **sin que `main.tex` cite ninguna**. Entre
  ellas va `vaccaro1995part1`, que esta en N4 (fuera de alcance). Compilado en copia: 6 paginas, **70 referencias**, 0
  citas indefinidas, y los tres avisos esperados de BibTeX (numero sin volumen: `hinsche2002fluoroscopy`,
  `templeman1996proximity` y ahora `matta1996internal`).
  - (a) Mantener `\nocite{*}`. La bibliografia refleja todo lo leido, pero un jurado vera obras que el texto no cita.
  - (b) **Recomendada:** quitar `\nocite{*}` antes de la entrega, para que la bibliografia liste solo lo citado. Es una
    linea. **No se aplica: la regla 4 exige orden explicita sobre `main.tex` en el turno.**
  - (c) Citar las nuevas en `main.tex`. *Descartada*: ninguna aporta a un objetivo (#77-#81).
- **Tipo:** REDACCION / forma. **Nivel:** N3.

### Evaluacion de impacto sobre los documentos rectores (regla 13)

- **`00-tesis.md`:** sin cambio de alcance, hipotesis ni objetivos. Solo queda **obsoleta una linea** de `Pendiente de
  decision de la autora`: *"`templeman1996proximity` sigue en `refs.bib` sin PDF"*. Ya tiene PDF y ficha completa, y su
  papel en el 2-15% queda resuelto (#77). Texto propuesto en el chat; lo aplica la autora.
- **`01-decisiones.md`:** no hace falta ninguna decision de alcance. Se propone en el chat una entrada breve que deje
  constancia de #77-#82. Este archivo lo escribe la autora (regla 3).
- **`02-datos.md`:** **sin implicancias.** Ninguna fuente toca CTPelvic1K, la cohorte ni las particiones.
- **Renderizador / Objetivo 1 / P1:** **sin implicancias.** Nada de lo leido afecta el VAE, la compuerta de 25 HU,
  ControlNet ni `B_delta`. El camino critico sigue siendo P1 en Khipu.

---

## Ronda 2026-09-18 — 13 fuentes nuevas, limpieza de duplicados (asistente en rol de asesor, delegacion explicita)

**Encargo de la autora (2026-09-18):** leer los papers nuevos con subagentes, revisar si queda algun PDF sin ficha y
borrar los duplicados verificados. Lecturas: `ziran2003` (PDF previo sin ficha, ahora con raw), `gardner2011transiliac-transsacral`,
`reilly2003effect`, `miller2012variations`, `wu2009variable`, `xu1996projection`, `ebraheim2000lumbosacral`,
`griffin2003vertically`, `mostafavi1996radiologic`, `lyu2020dudonet`, `wang2022adaptativeconv`, `yazdi2011opposite`
y `song2024bmar` (solo abstract, no hay PDF). **Despues de esta ronda no queda ningun PDF de `papers/` sin ficha.**

**Duplicados borrados** (autorizacion de la autora; detalle en `refs/MAPEO.md`): `miller2012sacralmorphology` (raw y PDF
identicos byte a byte a `miller2012variations`), `gertzbein1990pedicularscrew` (raw y PDF) y el raw
`templeman1996iliosacralscrews`. El PDF de Templeman se renombro a `papers/templeman1996proximity.pdf`.

**Veredicto global:** una sola lectura toca `main.tex` (#85, redaccion de la limitacion de campo mas un supuesto del
benchmark). El resto cierra cadenas de citas o confirma decisiones vigentes. **Alcance, compuerta del Objetivo 1, P1 y
renderizador: sin cambios.**

### 83 — `ziran2003` no propone el umbral de 10 mm y no da prior ordinal en S2: se cierra el ultimo nodo de la cadena — CERRADA (sin cambio)

- La unica mencion es descriptiva: *"very narrow (10 to 14 mm) corridors"* en sacros dismorficos (Discussion, p. 417).
  No se mide sistematicamente, no se cita de nadie y no se propone como criterio. `gardner2010safezones` simplifica
  esa frase al atribuirle el 10 mm.
- 113 tornillos de 7.3 mm (80 S1, 31 S2, 2 S3), 66 pacientes, **0 malposicion con criterio binario** (pp. 413-416).
  No hay mm, grados ni resultados por nivel: **no hay prior ordinal para S2**, lo que confirma que S2 se evalua solo
  descriptivamente (#12).
- El ano es 2003 (J Bone Joint Surg Br 85-B:411-8). El "2002" de Moed corresponde a las fechas de recepcion.
- `main.tex:52` atribuye el 10 mm a Kaiser como convencion elegida. Es correcto. **Sin cambio.** La ref. 22 de Ziran
  (resumen de congreso de 1996) queda en `_candidatos.md` como "no perseguir".

### 84 — Tres atribuciones de `kaiser2014dysmorphism` no aparecen en sus fuentes primarias — CERRADA (registro; `main.tex` no las usa)

- **Gardner 2011:** la frase *"sufficient size and complementary orientation to allow screw placement without a cortical
  breach"* **no esta en el PDF**. El criterio de viabilidad transsacra es cualitativo, sin umbral en mm.
- **Miller 2012:** la definicion de displasia (*"a sacral phenotype in which the size and orientation ... does not allow
  safe passage"*) **no esta en el PDF**. Solo aparecen frases cercanas (*"may preclude transiliac, transsacral screw
  placement"*, p. 12). Los siete signos de dismorfismo son cualitativos.
- **Wu 2009** (Kaiser lo cita como "Lu LP" y con otro titulo): no mide dismorfismo ni corredor, no usa CT (203 sacros
  secos). **No sostiene la diferencia etnica** que Kaiser le atribuye para explicar su prevalencia de 41%.
- **Que usa `main.tex` de Kaiser:** el marco de referencia, la holgura de 5 mm, la convencion de 10 mm, el calibre de
  6.3-8 mm y la regla de longitud util. **Nada de lo anterior**, y los fenotipos ya estan fuera de alcance (punto 8).
- **Decision (asistente):** sin cambio. Regla para la redaccion futura: **no citar via Kaiser** la definicion de
  dismorfismo, el requisito transsacro de Gardner ni argumentos etnicos. Si hacen falta, citar la fuente primaria con
  su frase real.
  - *Descartado:* reabrir el punto 8 de `Fuera de alcance`. Estas lecturas refuerzan la decision de no estratificar.
- **Nota de Miller (p. 13):** con transicion lumbosacra, la raiz en riesgo puede ser de otro nivel. El etiquetado de S1
  en la cohorte local ya tiene control de nivel (TotalSegmentator + revisor clinico, #50/#53/#54). Sin accion nueva.

### 85 — `main.tex:117` dice que ninguna fuente midio el corredor con fractura, pero `reilly2003effect` lo mide; y abre un supuesto sobre la poblacion del benchmark — ABIERTA (decidida; aplicacion en `main.tex` pendiente de orden)

- **Hallazgo 1 (redaccion):** `main.tex:117` afirma *"Every source that publishes sacral corridor geometry measured it
  in pelves without implants and without fracture"*. **Es falso.**
  - `reilly2003effect` mide la zona segura de S1 en 6 cadaveres con fractura sacra zona II por osteotomia y desplazamiento
    craneal de 0, 5, 10, 15 y 20 mm, con CT de 1 mm.
  - El area de la seccion limitante cae 36/50/79/90% (tablas, pp. 90-91). Con mas de 10 mm, el tornillo de 7 mm *"may not
    be technically possible"* (p. 93).
  - El abstract da otros porcentajes (30/56/81/90%) y el texto mezcla cm2 con mm2: **citar las tablas, no el abstract.**
- **Hallazgo 2 (supuesto, no registrado antes):** el benchmark de Zwingmann viene de pacientes **fracturados y reducidos**,
  mientras que los corredores de la tesis (`D_TS`) y los huespedes de la sintesis son pelvis **sin osteosintesis**. Reilly
  muestra que la malreduccion estrecha el corredor, asi que parte de la malposicion clinica puede deberse a corredores mas
  estrechos que los del huesped. Comparar las poses sinteticas con esas distribuciones supone que la geometria del
  corredor no difiere entre ambas poblaciones.
- **Opciones:**
  - (a) **Elegida:** reescribir la frase para que Reilly refuerce la limitacion en vez de contradecirla, y anadir el
    supuesto. Texto propuesto para `main.tex:117`:
    > *"With one exception, every source that publishes sacral corridor geometry measured it in pelves without implants
    > and without fracture: [...]. The exception, \citet{reilly2003effect}, osteotomised a zone~II sacral fracture in six
    > cadaveric pelves and found that 5--20~mm of cranial displacement reduced the limiting S1 cross-section by 36--90\%,
    > so corridor limits from intact pelves do not transfer to fractured or malreduced ones. The clinical ordinal
    > distributions targeted here come from fractured, reduced pelves, whereas corridors are measured on pelves without
    > osteosynthesis; residual malreduction is therefore an uncontrolled difference between benchmark and host."*
  - (b) Acotar la frase a *"clinical CT cohorts"*. Es minimo y cierto, porque Reilly es cadaverico, pero pierde el mejor
    argumento a favor de medir el corredor en cada volumen y deja el supuesto sin declarar.
  - (c) Borrar la frase. Pierde la justificacion de R1.
- **Por que (a):** corrige una afirmacion falsa verificable por cualquier revisor y convierte la fuente en respaldo del
  diseno (medir `D_TS` por volumen). No cambia ningun metodo ni corrida.
- **No aplicado:** la regla 4 exige orden explicita sobre `main.tex` en el turno. **Tipo:** REDACCION + SUPUESTO
  (benchmark). **Nivel:** N1 (frase falsa en el documento).

### 86 — Punto de entrada y margenes neurales: siguen sin fuente en mm, y el diseno no los necesita — CERRADA (sin cambio)

- `xu1996projection` da la region de entrada como triangulo (EIPS 30 mm y EIPI 27.4 mm al eje), sin S1/S2, sin angulos
  y sin CT. `ebraheim2000lumbosacral` trata un tornillo **dorsal** S1 (no iliosacro) y no da margenes en mm.
- El muestreador obtiene la trayectoria del corredor medido en cada volumen, y la entrada sale como interseccion con la
  cortical iliaca lateral. **No depende de un prior publicado de entrada.** La holgura `c` de 1-2 mm y la escala de brecha
  siguen declaradas como convenciones (Kaiser; #68/#78).
- **Decision:** sin cambio. *Descartado:* perseguir Kellam 1992 (capitulo de libro) o Mirkovic 1991.

### 87 — Umbrales de metal en la literatura MAR: la cadena del 2500 HU no tiene origen, y el 3000 HU tampoco — CERRADA (sin cambio; refuerza C1)

- `wang2022adaptativeconv` segmenta las mascaras clinicas de CLINIC-metal a 2500 HU *"Following [Yu et al., 2020]"*
  (p. 5), pero `yu2021` (esa misma obra) usa **2000 HU**. `wang2025adaptiveweighting` atribuye el 2500 HU a DICDNet y
  DuDoNet. **El 2500 HU sobre CLINIC-metal es una convencion del grupo sin fuente primaria.**
- `lyu2020dudonet`: 3000 HU sin justificar ni citar (p. 4). Es la unica fuente que Xie da para ese umbral.
- `yazdi2011opposite`: umbral **global** `0.9*Imax` por corte, sin validar la segmentacion. Es precedente de umbral
  relativo, **no** del semimaximo local de E8.
- ACDNet admite que *"An unsatisfactory threshold possibly makes tissues be wrongly regarded as metals"* (p. 6).
- **Que toca:** `main.tex` ya usa 2500 HU solo como cribado heuristico (`02-datos.md`) y como cota en `main.tex:119`, y
  C1 se apoya en la sobrecobertura propia de Xie y en E8. **Nada que corregir.**
- **Decision:** sin cambio.
  - *Descartado:* citar ACDNet en C1. Refuerza, pero C1 ya esta respaldada.
  - *Descartado:* presentar Yazdi como precedente del semimaximo. No es el mismo principio.

### 88 — Versiones y metadatos: reimpresion de Griffin, preprints de Lyu y ACDNet, `song2024bmar` sin PDF; la bibliografia sube a 83 — DECIDIDA (registro; refuerza #82)

- `griffin2003vertically`: el raw y el PDF son la **reimpresion** (JOT 2006;20(1 Suppl):S30-S36); `refs.bib` imprime 2006
  con la clave 2003 (precedente `herman2016`). El original (2003;17(6):399-405) solo aparece en la portada del PDF.
- `lyu2020dudonet` (preprint arXiv, **sin Liao** entre los autores) y `wang2022adaptativeconv` (arXiv v2): las paginas
  de las fichas no coinciden con la version publicada que cita `refs.bib`.
- `song2024bmar`: solo abstract. **No confirma** ser el origen de la escala humana de 5 niveles de `wang2025adaptiveweighting`.
  `main.tex` no la usa.
- **Ninguna de las 13 se cita en `main.tex`.** Con `\nocite{*}` la bibliografia pasa a **83 referencias**, 19 sin citar.
  Compila en copia: 6 paginas, 0 citas indefinidas, 4 avisos esperados (CORR sin volumen, ahora tambien
  `mostafavi1996radiologic`). **Refuerza la recomendacion (b) de #82: quitar `\nocite{*}` antes de la entrega.**
- **Decision:** ninguna de estas versiones se cita con numero de pagina mientras no haya PDF de la version publicada.
  *Descartado:* cambiar la clave de Griffin (la define la autora).

### Evaluacion de impacto sobre los documentos rectores (regla 13)

- **`00-tesis.md`:** sin cambio de alcance. #85 anade un supuesto al benchmark (poblacion fracturada frente a huesped
  sin osteosintesis), que va a `main.tex` si la autora aprueba (a). No se toca `00-tesis.md` (regla 14).
- **`01-decisiones.md`:** texto propuesto en el chat (duplicados borrados + #85).
- **`02-datos.md`:** sin implicancias. El 2500 HU ya estaba declarado como heuristica de cribado (#87 lo confirma).
- **Renderizador / Objetivo 1 / P1:** sin implicancias.

### 85 — APLICADA en `main.tex:117` (2026-09-18), opcion (a), por orden explicita de la autora

- Titulo del parrafo: *"corridor geometry has almost only been characterized in intact pelves"*.
- *"With one exception, every source ..."*, seguido de Reilly: seis cadaveres, fractura zona II osteotomizada, 5-20 mm de
  desplazamiento craneal y area para tornillos de S1 reducida un 36-90% (Results, p. 91). Se cierra con *"this supports
  measuring the corridor on each volume"*.
- Supuesto declarado: las distribuciones de Zwingmann vienen de pelvis fracturadas (Tile B y C; Materials and Methods,
  p. 1834), y los corredores se miden en pelvis sin osteosintesis.
- **Diferencia con el texto propuesto:** donde el borrador decia *"fractured, reduced pelves"* quedo *"fractured pelves
  (Tile types B and C)"*. La ficha de Zwingmann respalda el tipo de fractura, pero no la calidad de la reduccion, asi que
  "reduced" se quito para no afirmar algo sin fuente.
- Compila: 6 paginas, 83 referencias, 0 citas indefinidas. **#85 APLICADA.**

---

## Ronda 2026-09-18 (2) — entrega recortada de 2 paginas (`entrega/main.tex`)

### 89 — Retroalimentacion del asesor sobre la primera version: `main.tex` no tiene plan de falsos positivos de extraccion ni presupuesto de computo — ABIERTA

- **Origen:** retroalimentacion sobre `entrega/PFCII___ENG___Kiara.pdf`, transmitida por la autora el 2026-09-18:
  (1) plan para falsos positivos/artefactos en la extraccion; (2) recursos de computo para estimar si caben las pruebas
  de difusion y simulador; (3) estilo: spanglish, exceso de adverbios y adjetivos.
- **Hallazgo:** `tesis/main.tex` (6 pp.) no trae ninguno de los dos contenidos. La entrega de 2 pp. los arma solo con
  cifras ya medidas: cribado 2500 HU (113/178, 0 falsos negativos, #22), E8 (9 de 57 fragmentados, 49 de 57 < 6.0 mm,
  #46), corredor ocupado 53.8% -> 40.4% en 52 pacientes, R1 48/29 de 65; computo de `KHIPU.md` (2 x RTX A6000 48 GB,
  QoS a-tesis 3 jobs/32 CPU/98G/24 h; P1 1.32 s/paso, 24.6 GB, 10 h 36 min por codificacion; TS 6 h 27 min).
- **Cifra retenida:** el borrador de la autora (~140 GPU-h; 50 h ControlNet, 40 h segmentacion downstream, 15 h
  generacion) **no entra**: ninguna cifra esta medida, el asesor pidio no ponerla, y las 40 h de segmentacion downstream
  contradicen el punto 1 de `Fuera de alcance`. Su atribucion del limite de tamano a los "kernels de scatter Monte Carlo"
  tampoco tiene respaldo: `haneda2025aapm` (Sec. 4, p. 16) dice "may look distorted for large metal objects with
  diameters larger than 3.0 cm", sobre la traza de metal del sinograma.
- **Gap abierto:** el tiempo de entrenamiento del ControlNet y el de XCIST por volumen no estan medidos. La entrega
  declara el procedimiento (piloto de 200 pasos, como en P1) y no da cifra.
- **Que toca:** `tesis/main.tex` (dos parrafos nuevos + pasada de estilo), `docs/00-tesis.md` (presupuesto de computo
  como supuesto), plan de P3/O3.
- **Tipo:** REDACCION + SUPUESTO. **Pendiente de decision de la autora. No aplicado a `main.tex` (reglas 4 y 14).**

### 90 — Plazo: la autora habla de 5 semanas, los documentos dicen ~11 — ABIERTA

- **Origen:** pregunta de la autora, 2026-09-18: "es posible llegar hasta el 4 en 5 semanas?".
- **Hallazgo:** `01-decisiones.md` (2026-09-17, "Por que") planifica con **~11 semanas**; `ESTADO.md` cita ~12 semanas
  desde el 2026-09-15 (#23). Ningun documento registra 5 semanas ni una decision de "llegar solo hasta el Objetivo 3".
  Lo registrado: minimo = Obj 1 + Obj 2 + SAP; completo = Obj 3 (condicionado a la compuerta del Obj 1, renderizador
  mantenido por la autora) + Obj 4.
- **Que toca:** si 5 semanas es el plazo real, el alcance COMPLETO de `00-tesis.md`, la pregunta y la hipotesis
  (comparacion contra Peters) y la entrega de 2 pp. dejan de ser alcanzables tal como estan escritos.
- **Tipo:** ALCANCE + SUPUESTO. **Pendiente de la autora: confirmar plazo y a que corresponde. No aplicado.**

---

## Ronda 2026-09-19 — resultado de P1 (compuerta del Objetivo 1)

### 91 — P1 da NO-GO con la regla preinscrita: ninguna de las seis combinaciones baja de 25 HU; la mejor (decodificador afinado, `pub+asinh`) queda en 61.72 HU — ABIERTA

- **Origen:** jobs 51669/51670/51671+51878 (entrenamiento) y 51879 (evaluacion), Khipu, 2026-09-17 a 2026-09-19.
  `data/p1/eval/p1_compuerta.md` (copia local pendiente). Regla fijada el 2026-09-17 (`01-decisiones.md` (3), #76,
  `main.tex:77`) **antes** de correr.
- **Controles, todos OK:** identidad frente a E6c 165 de 165; `sd15` frente a E6b 330 de 330 (0.05 HU); encoder
  congelado 3 de 3; decodificador afinado distinto del preentrenado 3 de 3. 68 filas (34 pacientes x 2 modelos), 0 errores.
- **Veredicto (media por paciente del MAE en hueso, `vae regla`, 34 de test):**

  | Modelo | Codificacion | media | IC95 bootstrap | pacientes >= 25 HU |
  |---|---|---|---|---|
  | sd15 | `pub` | 160.13 | [142.42, 180.62] | 34/34 |
  | sd15 | `LW20000` | 209.39 | [191.91, 228.62] | 34/34 |
  | sd15 | `pub+asinh` | 164.76 | [148.81, 182.87] | 34/34 |
  | afinado | `pub` | 72.91 | [59.37, 89.02] | 34/34 |
  | afinado | `LW20000` | 77.03 | [70.12, 84.65] | 34/34 |
  | afinado | `pub+asinh` | **61.72** | [55.12, 68.99] | 34/34 |

  **NO-GO.** Ningun paciente de test, en ninguna combinacion, baja de 25 HU. El mejor IC95 empieza en 55.12 HU.
- **Lo que el resultado separa:**
  - El afinado del decodificador **reduce el error a menos de la mitad** (164.76 -> 61.72 en `pub+asinh`), pero queda
    ~2.5 veces por encima del umbral.
  - **No es un problema del metal.** Sin metal (dataset6, n = 14), el mejor afinado da 53.72 HU de media. Con el
    oraculo (que elige canal con el HU verdadero) el afinado sigue en 49.65-63.56 HU: la regla de lectura no explica la
    brecha.
  - **Lectura plausible, no verificada:** con el encoder congelado, el latente f=8 de SD 1.5 es el cuello de botella;
    un decodificador mejor no recupera lo que el encoder ya descarto. P1 no mide el encoder, asi que esto no esta probado.
  - Metal (descriptivo): el afinado baja de ~4200 a ~2065-2154 HU en `LW20000`/`pub+asinh`. `B_delta` (descriptivo):
    64.62-88.72 HU con afinado. Ninguno decide.
- **Objecion previsible: entrenamiento insuficiente.** Las curvas de validacion terminan en 61.84 / 79.99 / 70.31 HU
  (`pub+asinh` / `LW20000` / `pub`) tras 30 000 pasos; `pub` estuvo entre 69.85 y 73.64 HU desde el paso 15 000
  (plateau). Falta revisar la pendiente de las otras dos en `curva_*.csv` antes de afirmarlo. Aun asi, pasar de 61.72
  a < 25 HU exige reducir el error 2.5 veces.
- **Curvas revisadas (2026-09-19, `experiments/objetivo1/p1_curvas/`):** casi toda la mejora ocurre en los primeros
  ~5 000 pasos (`pub+asinh` 156.02 -> 71.61; `pub` 151.64 -> 76.57; `LW20000` 208.48 -> 81.80). Media de val MAE en
  hueso, pasos 10-19k frente a 20-30k: `pub+asinh` 66.54 -> 64.47; `pub` 71.63 -> 71.42; `LW20000` 76.93 -> 70.77.
  Pendiente lineal 20-30k: -0.60, -0.59 y **+0.18** HU por 1000 pasos. Aun extrapolando esa pendiente en linea recta
  (optimista para una curva que se aplana), `pub+asinh` necesitaria ~66 000 pasos mas (~23 h) para llegar a 25 HU, y
  `LW20000` no bajaria. El minimo de val de toda la corrida es 60.78 HU (`pub+asinh`, paso 27 000). El val final
  (61.84) coincide con la media de test (61.72): los 8 pacientes de val representan bien al test. **Conclusion: el
  entrenamiento esta en plateau; "faltaron pasos" no explica el No-Go.** Ademas, entrenar mas despues de ver el test
  seria elegir tras el resultado (opcion c).
- **Versionado:** `experiments/objetivo1/p1_compuerta.md`, `p1_eval.csv`, `p1_control.csv` y `p1_curvas/`.
- **Analisis del asesor (2026-09-19, a pedido de la autora; lectura, no medicion nueva salvo donde se indica):**
  - *Orden de magnitud esperable:* `rombach2022latentdiffusion` da para KL f=8, c=4 (la configuracion del VAE de SD)
    PSNR 24.19 dB en imagen natural (Tabla 8, p. 21). 24 dB equivale a un error RMS de ~6% del rango; sobre la LW de
    `pub` (3000 HU) son ~185 HU. Es el mismo orden que lo medido con `sd15` (RMSE en hueso 397-511 HU de media).
    25 HU de MAE sobre 3000 HU exige errores de ~0.8% del rango. **Inferencia, no medicion:** el objetivo pide una
    fidelidad que la arquitectura no declara ni en su dominio de origen.
  - *Componer el original fuera de `B_delta` no rescata el Objetivo 3.* Medido en `p1_eval.csv`: con el mejor afinado
    (`pub+asinh`), en los 20 pacientes de test con metal, el MAE dentro de `B_delta` es 69.89 HU, frente a 67.32 en
    hueso. El error del autoencoder esta tambien dentro de la banda que el renderizador tiene que generar.
  - *Anclaje del 25 HU:* las cifras que lo sostienen en `main.tex:77` (NMAR 20.2, DDPM 12.3, MLD-MAR 12.74) son RMSE de
    imagen completa fuera de la mascara de metal, en tareas de MAR. `karageorgos2024ddpm` define hueso como
    150 <= CTN < 1000 HU (Sec. II-G, p. 11) y da RMSE_ROI de 36 (NMAR) y 52 (DDPM) en su caso de cadera (Tabla II,
    p. 29); el ROI de esta tesis es hueso > 150 HU sin tope. El umbral es exigente para un ROI de hueso denso. **Sirve
    para la discusion, NO para mover el umbral ahora** (ya esta declarado que no hay umbral publicado).
  - *MAISI:* sin ficha y sin leer (`01-decisiones.md` 2026-09-17 E). Antes de decidir (b) hay que verificar, via
    `lector-papers`: dominio de entrenamiento (CT en HU), normalizacion de intensidad (si recorta a un rango tipo
    [-1000, 1000] HU, como declara `chen2026foundationvae` en sus experimentos de generacion, el hueso denso y el metal
    quedan fuera), factor de compresion, 2D/3D y memoria, y si trae modelo de difusion con ControlNet propio (#74).
- **Consecuencia segun la regla ya escrita** (`main.tex:77`): *"If none passes, Objective 3 is not pursued and the
  No-Go result is reported as the outcome."* El criterio **no se mueve** (patron #25/#37/#45/#47/#50).
- **Tension con la contingencia registrada:** `01-decisiones.md` 2026-09-17 C dice *"Otro VAE (MAISI) queda como
  contingencia solo si el decodificador adaptado no pasa y queda tiempo"*. `main.tex` no la menciona. Probar otro VAE
  seria una **compuerta nueva**, no un reintento de esta, y solo es legitima si se preinscribe antes de correrla. Choca
  ademas con #74 (otro latente invalida ControlNet sobre SD 1.5) y con #90 (plazo).
- **Opciones para la autora:**
  - (a) **Aceptar el No-Go como resultado** (lo que dice `main.tex`): el Objetivo 3 sale del alcance ejecutado y la
    tesis entrega Obj 1 (resultado negativo con controles) + Obj 2 + SAP. Es el alcance minimo de `00-tesis.md`.
    **Recomendada por el asistente**, sobre todo con #90 (5 semanas).
  - (b) Contingencia MAISI como compuerta nueva y preinscrita (misma regla, mismo test, un solo VAE), con plazo cerrado.
    Si pasa, el Objetivo 3 se rehace sin ControlNet sobre SD 1.5 (#74 a).
  - (c) No recomendada: subir el umbral, cambiar la lectura a oraculo o entrenar mas pasos despues de ver el test.
- **Que toca:** `main.tex` (Obj 1 resultado, Obj 3, tabla, resumen), `00-tesis.md` (alcance), #74, #90.
- **No aplicado** (regla 14). **Tipo:** RESULTADO + ALCANCE. **Nivel propuesto: N1.**

### 92 — El "24%" de malposicion que heredan `tejwani2014` y la cadena de Gardner (#12) viene de `tonetti2001results`, que publica 23%, binario y sin denominador declarado — ABIERTA

- **Origen:** ficha `tonetti2001results.md` (lector-papers, 2026-09-19).
- **Hallazgo:** *"Outside bone trajectories 12 (23%) 0 (0%)"* (Table 1, p. 209); criterio binario dentro/fuera de hueso,
  sin mm ni grados ni nivel S1/S2; *"No statistical comparison tests were done"* (p. 208). 12/51 = 23.5% es calculo del
  lector, el paper no declara el denominador.
- **Consecuencia:** no es prior ordinal ni distribucion S2 para SAP (Obj 2 sin cambio). Si se cita la cifra, citar
  12 (23%) desde Tonetti, no "24%" via Tejwani.
- **No aplicado** (regla 14). **Tipo:** REDACCION / trazabilidad. **Nivel propuesto: N3.**

### 93 — MAISI no permite preinscribir la contingencia de #91 (b) desde el paper: el rango de HU esta en un suplementario no incluido, y su latente 3D obliga a cambiar el renderizador entero — ABIERTA (liga con #91, #74)

- **Origen:** ficha `guo2025maisi.md` (lector-papers, 2026-09-19; articulo sin suplementario).
- **Hallazgo:** normalizacion de HU del CT: NO ENCONTRADO EN EL PDF (remite a *"Supplementary Sec. A/B"*). Metricas de
  reconstruccion solo PSNR/SSIM/LPIPS (Tabla 1, p. 4435), sin error en HU ni en hueso. Datos de CT: torax, abdomen y
  cabeza-cuello; pelvis y metal NO ENCONTRADO. VAE-GAN **3D**, con difusor y ControlNet 3D propios condicionados por
  mascaras de 127 estructuras; entrenado en A100 80G.
- **Consecuencias:** (1) la compuerta de MAISI solo se puede decidir midiendo; su rango de recorte hay que sacarlo del
  suplementario o del codigo (no citables hoy). (2) Adoptarlo no es "cambiar un VAE": cambia el renderizador 2.5D sobre
  SD 1.5 por uno 3D (resuelve #74 por reemplazo, no por compatibilidad). (3) MAISI es precedente de ControlNet con
  mascaras en CT: la novedad del renderizador debe apoyarse en metal + artefacto fuera de la mascara (`B_delta`).
- **No aplicado** (regla 14). **Tipo:** SUPUESTO / arquitectura Obj 3. **Nivel propuesto: N1.**

### 94 — MedVAE tampoco resuelve la compuerta desde el paper, y excluye explicitamente los estudios con metal — ABIERTA (liga con #91, #74, #93)

- **Origen:** ficha `varma2025medvae.md` (lector-papers, 2026-09-19).
- **Hallazgo:** parte del KL-VAE de `rombach2022` con LoRA en todas las convoluciones y entrada de 1 canal. Los modelos
  2D se entrenan solo con radiografia de torax y mamografia; CT solo en 3D (1,434 CT de cuerpo entero, pelvis NO
  ENCONTRADO). *"remove all samples with metal hardware and casts"* (p. 15). Normalizacion de HU, error en HU y
  compatibilidad con el latente de SD: NO ENCONTRADO. Solo PSNR/MS-SSIM, con posible solape entre entrenamiento y
  evaluacion. No reporta uso del latente para difusion.
- **Consecuencias:** (1) como MAISI (#93), solo se decide midiendo. (2) La forma del latente 64/4 coincide con la de SD
  (H/8 x W/8 x 4), pero LoRA y la entrada de 1 canal impiden dar por compatible el espacio: ControlNet sobre SD 1.5 no
  queda respaldado (#74). (3) Excluir metal en el entrenamiento hace improbable que transporte el rango del implante.
- **No aplicado** (regla 14). **Tipo:** SUPUESTO / arquitectura Obj 3. **Nivel propuesto: N2.**

### 95 — Opcion A: el renderizador se entrenaria con mascaras de metal real por umbral y se usaria con mascaras de tornillo parametrico; la diferencia entre las dos es un gap de dominio sin medir — ABIERTA (liga con #41, E8, #31)

- **Origen:** pronostico de la opcion A (chat, 2026-09-19). **Correccion del asistente:** en el chat se dijo que las
  mascaras por umbral salen "mas gruesas por blooming". **E8 midio lo contrario:** *"2500 HU no infla por blooming: esta
  cerca del semimaximo y recorta la periferia"* (#41, E8), con fuste mediano de 5.00 mm a > 2500 HU frente a 5.14 mm a
  semimaximo, y 10 de 62 objetos alargados partidos a > 2500 HU.
- **Gap:** las mascaras de entrenamiento (umbral sobre metal real) son algo mas finas que la periferia real y a veces
  estan fragmentadas; la mascara parametrica (cilindro de calibre publicado, 6.0-8.0 mm segun #31) es continua y mas
  gruesa que el 5.00 mm medido. El renderizador veria en inferencia mascaras distintas de las de entrenamiento.
- **Opciones:** (a) entrenar con la misma regla de mascara que se usara en inferencia (umbral aplicado tambien al
  implante sintetizado, o mascara parametrica ajustada a los implantes reales); (b) medir la sensibilidad del generador
  al calibre de la mascara como analisis declarado; (c) calibre del cilindro tomado de E8 (5.00 mm) en vez de #31, con la
  salvedad de E8 de que no coincide con la geometria publicada.
- **No aplicado** (regla 14). **Tipo:** SUPUESTO / diseno del Obj 3. **Nivel propuesto: N2.** Se resuelve en el
  documento de diseno de A, antes de entrenar.

### 96 — Opcion A: el contexto de entrenamiento trae el streaking del implante real y el de uso (paciente sin metal) no — ABIERTA (liga con #57, #95)

- **Origen:** borrador `experiments/objetivo3/diseno_A.md` (2026-09-19), seccion 8.
- **Hallazgo (razonamiento de diseno, sin medir):** en inpainting sobre pacientes con metal, lo que queda fuera de
  `G = M ∪ B_delta` incluye el streaking lejano del implante real (el que `B_delta` trunca por diseno, #57). En la
  sintesis sobre pacientes sin metal ese contexto es limpio. El modelo puede aprender a apoyarse en rayas que en uso no
  existen: artefacto debil o costura en el borde de la banda.
- **Como se vera:** E-A2 del diseno (costura a traves del borde de `B_delta`, streak amplitude frente a copia-pega y
  al brazo fisico).
- **Opciones:** (a) contexto recortado o suavizado fuera de `G` en entrenamiento; (b) banda de contexto intermedia
  excluida de la entrada; (c) aceptar y medir. Se decide tras la prueba corta, antes de preinscribir.
- **No aplicado** (regla 14). **Tipo:** SUPUESTO / diseno del Obj 3. **Nivel propuesto: N2.**

### 97 — El deep-research sugiere que el tornillo canulado de 7.3 mm es, en su mayor parte, un fuste de ~4.8 mm con cabeza y arandela mucho mas grandes: si se confirma, el cilindro liso de 6.5-8.0 mm de `main.tex` sobreestima el metal — ABIERTA (liga con #95, #41, #31)

- **Origen:** `refs/deep-research/fuentes_geometria_tornillo_iliosacro.md` y `gemini_research.md`, aportados por la autora
  (2026-09-19). **Ninguna de sus cifras esta verificada**: no hay PDF en `papers/` ni entrada en `refs/raw/`, asi que nada
  de esto puede escribirse en la tesis todavia (reglas 1, 2 y 9). Los dos documentos se contradicen entre si (tabla en
  `docs/literatura/_candidatos.md`, ronda 2026-09-19).
- **Afirmacion central por verificar:** el nominal de 7.3 mm describe la **rosca distal**, no el cuerpo. El fuste seria de
  ~4.8-4.9 mm y el nucleo de ~4.5-4.7 mm a lo largo de casi toda la trayectoria, con una cabeza de ~8.0-8.2 mm y, en
  iliosacros, una arandela de ~13-14 mm apoyada en la cortical iliaca.
- **Por que toca al metodo, si se confirma:**
  1. **`main.tex:113` modela un cilindro liso de 6.5-8.0 mm en todo el trayecto.** Eso pondria ~7.3 mm de metal donde el
     implante real tiene ~4.8 mm, es decir mas del doble de area transversal, y ademas **sobre hueso trabecular sano**.
     Agrava #95 en la direccion contraria a la que el diseno suponia.
  2. **Coherencia con E8:** el fuste medido en CLINIC-metal fue 5.00 mm (mediana, HU > 2500), muy cerca del 4.8 mm que
     afirma el deep-research y lejos de los calibres publicados de 6.5-8.0 mm. E8 lo habia leido como "geometria extraida
     que no coincide con la publicada" (#41); esta lectura ofrece una explicacion alternativa: **el calibre publicado y el
     fuste no son la misma magnitud**. No esta verificado, pero reordena la interpretacion de E8.
  3. **Cabeza y arandela no estan en el modelo.** Estan en la cortical iliaca, en un gradiente alto, y por volumen serian
     el mayor emisor de artefacto del conjunto. Su ausencia en la mascara de sintesis es un candidato mas fuerte que el
     fuste para explicar diferencias con los pacientes reales.
  4. **#31 no cambia:** para la viabilidad del corredor manda la envolvente (rosca, 6.5-8.0 mm). Lo que cambia es la
     mascara de metal para sintetizar. **Son dos geometrias distintas y hoy el texto usa una sola.**
- **Lo que NO se puede hacer:** cambiar `main.tex:113` con estas cifras. Requiere los PDF (G1, G2 y la ficha tecnica T1 de
  `_candidatos.md`) y su lectura con `lector-papers`.
- **Opciones para la autora:** (a) conseguir G1 + G2 + T1 y modelar fuste, cabeza y arandela por piezas; (b) mantener el
  cilindro liso declarado como simplificacion y calibrar su diametro con E8 (5.00 mm) en vez de con el nominal, declarando
  que es la magnitud que el modelo vio en entrenamiento; (c) mantener 6.5-8.0 mm, que es lo que dice hoy el texto, y
  declarar la sobreestimacion como limitacion.
- **Recomendacion del asistente:** (b) para el piloto, porque no depende de ninguna lectura nueva y alinea la mascara con
  los datos de entrenamiento; (a) para la version final si llegan los PDF.
- **VERIFICADO el 2026-09-19 con seis lecturas y tres fichas tecnicas** (todas ya en `refs.bib`):

  | Pieza | Valor | Fuente |
  |---|---|---|
  | Diametro de rosca (el "nominal") | 7.3 mm | `synthes2002chart` (*"Thread Diameter"* sobre *"SCREW DIAMETER (mm)"*); `gardner2015screw` Tabla 1, p. 42; `zhu2022optimalposition` p. 1548 |
  | **Fuste** | **4.8 mm** (`synthes2006cannulated`, columna *"Shaft diameter"*, p. impresa 4; `zhu2022optimalposition`, p. 1548) y **4.9 mm** (`gardner2015screw`, p. 42) | tres fuentes independientes |
  | Nucleo | 4.7 mm | `gardner2015screw`, p. 42 |
  | Longitud de rosca | 16 / 32 mm o completa | `synthes2002chart`; `acumed2020cannulated`; `gardner2015screw`; `zhu2022optimalposition` |
  | Paso de rosca | **2.5 mm** | `zhu2022optimalposition`, p. 1548 (descarta el 2.75 mm del deep-research) |
  | Cabeza | **8.0 mm de diametro, 4.5 mm de altura**, hex de 4.0 mm, sin avellanado | `sayres2014comparison`, p. 34; `synthes2006cannulated` (*"4.0 mm Hex"*) |
  | Arandela plana 6.5/7.3 | **13.0 mm exterior, 6.6 mm interior** (X19.990, `synthes2006cannulated`, p. 5); 13.0 x 6.7 mm en Acumed; 13.0 mm en `berk2023washer`, p. 2 | tres fuentes coincidentes en el exterior |
  | Espesor de la arandela | **SIN FUENTE.** Synthes no lo publica; el *"thickness 6.6 mm"* de Berk (p. 2) coincide con el **diametro interior** del catalogo y el PDF no define la magnitud | ninguna |
  | Diametro de canulacion | **SIN FUENTE.** Los 2.8 mm son la aguja guia y los 5.0 mm la broca: instrumental, no el implante | ninguna |
  | Material | `berk2023washer` usa **acero 316LVM**; Acumed declara **titanio ASTM F136**; Synthes dice *"stainless steel and titanium"* sin aleacion | coexisten los dos |

- **Conclusion: la afirmacion central de #97 queda PROBADA.** El nominal es el diametro de rosca; el cuerpo del
  tornillo mide ~4.8 mm en casi todo el trayecto. El cilindro liso de 6.5-8.0 mm de `main.tex:113` **sobreestima el
  area transversal del metal en mas del doble** a lo largo del corredor, y por casualidad acierta el tamano de la
  cabeza (8.0 mm), que es la unica parte del implante con ese calibre.
- **Precedente en la literatura para separarlas:** `zhu2022optimalposition` usa las **dos** geometrias del mismo
  tornillo sin comentarlo: cilindro de 7.3 mm para planificar sobre imagen (*"7.3 mm diameter splines"*, p. 1547) y
  fuste de 4.8 mm para simular (p. 1548). Es exactamente la separacion **envolvente del corredor (#31) frente a
  mascara de metal (#95)** que el texto de la tesis hoy no hace.
- **Lo que queda abierto:** espesor de arandela, diametro de canulacion, y el hecho de que ninguna de las fuentes de
  dimensiones sea iliosacra (Gardner y Zhu son femorales, Sayres calcaneo). `berk2023washer` si es iliosacro pero no
  publica el cuerpo del tornillo. **Ninguna fuente de dimensiones cita a su vez una fuente**: son nodos terminales.
- **Consecuencia para el material (nueva):** el implante iliosacro puede ser acero o titanio segun el fabricante, y
  `radzi2014metalartifacts` y `cassanego2026evolution` muestran que el artefacto cambia con el material y entre
  fabricantes. La mascara binaria del Objetivo 3 no codifica aleacion: queda como limitacion declarada (#98).
- **Recomendacion revisada del asistente:** modelar **por piezas** (cabeza de 8.0 x 4.5 mm + fuste de 4.8 mm +
  envolvente de rosca de 7.3 mm en los 16 o 32 mm distales + arandela de 13.0 mm como opcion declarada), con la
  envolvente de 6.5-8.0 mm reservada a la viabilidad del corredor (#31). Ya no hace falta buscar mas papers para esto:
  lo esencial esta citable. Solo el espesor de la arandela y la canulacion siguen sin fuente, y para ambos la salida
  honesta es declarar la simplificacion.
- **Cierre parcial con 5 documentos mas (2026-09-20):**
  - **Espesor de arandela: hay cifra, pero de OTRO fabricante.** `doublemedical_trauma_catalogue` publica
    *"Thickness: 1.5mm"* con *"Width: 13.0mm"* para su arandela de 6.5/7.3 mm (impresa 5/7, PDF 98), y 5.5 mm para la
    variante con puas. Coincide con el ancho de 13.0 mm de Synthes y Acumed, pero **es un catalogo de Double Medical**:
    sirve para decir *"un fabricante publica 1.5 mm"*, no para atribuirselo al implante de Synthes.
  - **Canulacion: NO se cierra.** El valor de 2.9 mm aparece **solo en listados de distribuidor**
    (`primis_synthes_listings`), atribuido al tornillo pero sin respaldo del fabricante: el `Inventory Control Form` de
    Synthes **no publica canulacion**, y sus 2.8 mm son aguja guia y sus 5.0/7.3 mm brocas. Uno de esos listados trae
    ademas texto residual de otro producto (*"SYNTHES TI SOLID TIBIAL NAIL"* en una ficha de acero), lo que degrada toda
    su columna de cifras.
  - **Tres contradicciones que resuelve lo ya verificado:** nucleo 4.5 (listados) frente a **4.7** (`gardner2015screw`);
    cabeza 8.2 frente a **8.0** (`sayres2014comparison`, y `doublemedical_trauma_catalogue` tambien imprime 8.0);
    paso 2.75 frente a **2.5** (`zhu2022optimalposition`). Prevalecen las fuentes citables.
  - **Dato nuevo de catalogo:** existe una variante de 7.3 mm **totalmente roscada** (209.620-209.780) y el rango de
    longitudes llega a 30-180 mm. La mascara parametrica debe poder representar rosca parcial y total.
  - **Conclusion operativa:** de los dos huecos, **uno se cubre con fuente de otro fabricante (1.5 mm) y el otro no
    tiene fuente citable**. No recomiendo seguir buscando: el camino que faltaria es el *Technique Guide* especifico del
    sistema 7.3 mm de Synthes, y su ausencia no bloquea el piloto. **Propuesta: declarar la canulacion como parametro
    libre del modelo (y evaluar el caso macizo frente al hueco como sensibilidad), y el espesor de arandela como
    1.5 mm citando a Double Medical con la salvedad de fabricante.**
- **No aplicado** (regla 14). **Tipo:** SUPUESTO / geometria del implante. **Nivel propuesto: N1.**

### 98 — Existe un precedente publicado que cuantifica en milimetros la extension peri-implante del artefacto en CT: la frase de `main.tex:54` hay que acotarla — ABIERTA (liga con #57, #96)

- **Origen:** ficha `radzi2014metalartifacts.md` (lector-papers, 2026-09-19).
- **Lo que dice `main.tex:54`:** *"for which no published precedent quantifying a peri-implant band was found"*.
- **Hallazgo:** `radzi2014metalartifacts` publica distancias en milimetros del artefacto en CT: *"from CT were 2.0, 2.6,
  1.6 and 2.0 mm"* (Resultados, p. 167) para titanio, acero, canulado de titanio y canulado de acero. Es una cifra
  peri-implante publicada, aunque no sea una banda de generacion.
- **Por que la frase no cae del todo:** Radzi mide la *"perpendicular distance from the central screw axis"* (p. 163),
  es decir **desde el eje**, no desde la superficie del implante, hasta el borde de una superficie **umbralizada** cuyo
  umbral no publica y sin mencionar HU en todo el PDF. No mide el alcance del streaking (en MRI lo excluye
  explicitamente, p. 169, y en CT no lo aclara), es un tobillo de un solo cadaver y usa tornillos de 3.5-4.0 mm.
- **Riesgo concreto:** la frase, tal como esta, es un reclamo de ausencia de precedente. Un jurado que conozca a Radzi
  la puede refutar con una sola cita.
- **Opciones:** (a) precisar a *"no published precedent quantifying a generation band outside the implant mask"*;
  (b) citar a Radzi como precedente de medicion y declarar en que se diferencia (desde el eje, umbral no publicado,
  tobillo, sin HU); (c) dejarla y aceptar la objecion.
- **Recomendacion del asistente:** (a) + (b). Cuesta dos frases y convierte una afirmacion fragil en una acotacion.
- **Lo que NO cambia:** `B_delta` = 12 mm sigue sin calibracion publicada. Radzi no la respalda ni la refuta, y
  `cassanego2026evolution` mide 3.1-4.2 mm con el mismo metodo declarado, sin punto de referencia: los dos numeros no
  son comparables entre si.
- **Dato adicional para el renderizador:** entre titanios de distinto fabricante el artefacto varia (3.1 a 3.9 mm,
  Cassanego Tabla 3, p. 7), y Radzi separa titanio de acero (2.0 vs 2.6 mm) aunque con O-MAR solo en el titanio. La
  **mascara binaria no codifica aleacion**: queda como limitacion declarada del Objetivo 3, no como equivalencia.
- **No aplicado** (regla 14). **Tipo:** REDACCION / reclamo de novedad. **Nivel propuesto: N1.**

### 99 — La guia del fabricante confirma el fuste pero deja sin cerrar arandela y canulacion, y atribuye la indicacion sacroiliaca al calibre de 6.5 mm, no al de 7.3 — ABIERTA (liga con #97, #41, #31)

- **Origen:** ficha `synthes_cannulated_65_73_guide.md` (lector-papers, 2026-09-20). Es la guia **especifica del
  sistema** que la tesis modela, del propio fabricante (doc. J4552-E).
- **Lo que confirma, y ahora con la fuente mas directa posible:** *"4.8 mm diameter shaft"* (impresa 2), roscas de
  16 mm, 32 mm y completa, hex de 4.0 mm, longitudes de 20 a 180 mm y material *"316L stainless steel or titanium alloy
  (Ti-6Al-7Nb)"* (impresa 12), sin norma ASTM/ISO. Ademas: *"The core and shaft diameters are the same."* (impresa 5),
  es decir el nucleo del fuste **es** el fuste; los 4.7 mm de `gardner2015screw` son del nucleo **bajo la rosca**, que
  es otra magnitud. **El cuerpo del tornillo queda cerrado en 4.8 mm con fuente del fabricante.**
- **Lo que NO cierra:** espesor y diametro interior de la arandela son **NO ENCONTRADO** (solo *"Washer, 13.0 mm"*,
  impresa 12, refs. 219.99 acero y 419.99 titanio), y el **diametro de canulacion del tornillo tampoco aparece**.
- **Hallazgo que corrige la pista de los distribuidores:** en esta guia **el 2.9 mm es siempre canulacion de
  INSTRUMENTAL** (brocas 310.495 y 310.63, destornilladores 314.05 y 314.23, impresa 18). Lo unico que el documento
  dice del tornillo es funcional: *"Cannulated shaft accepts 2.8 mm diameter guide wires"* (impresa 2). El 2.9 mm de
  los listados de distribuidor **no solo carece de respaldo: hay evidencia de que su origen es el instrumental**. La
  decision del 2026-09-20 (canulacion como parametro libre) queda **reforzada**, no revisada.
- **Riesgo nuevo, y es de redaccion:** la unica mencion sacroiliaca impresa, *"Sacroiliac joint disruptions"*
  (impresa 4), esta bajo el encabezado *"6.5 mm Cannulated Screws are also indicated for:"*, o sea **atribuida al
  calibre de 6.5 mm, no al de 7.3**; "iliosacral", "sacrum", "S1" y "S2" no aparecen en todo el documento. La tesis
  ancla su envolvente de 6.5-8.0 mm en literatura clinica (`gardner2010safezones`, `kaiser2014dysmorphism`), no en el
  fabricante, asi que **nada obliga a cambiar el rango**; lo que no se puede escribir es que el fabricante indique el
  7.3 mm para fijacion iliosacra. `synthes2006cannulated` si lista *"iliosacral dislocations"*, pero bajo el grupo
  *"CSS 6.5, 7.0 und 7.3"*, sin separar calibres.
- **Efecto sobre el material:** el mismo sistema existe en **acero 316L y en titanio Ti-6Al-7Nb**, y `berk2023washer`
  uso acero 316LVM mientras Acumed declara titanio. Refuerza la limitacion ya declarada en #98: la mascara binaria no
  codifica aleacion y la cohorte real mezcla materiales.
- **Opciones para la autora:** (a) mantener la envolvente de 6.5-8.0 mm citando la literatura clinica y **no** atribuir
  la indicacion al fabricante; (b) declarar en `main.tex` que el cuerpo del tornillo es de 4.8 mm citando
  `synthes2003guide`, que es ahora la fuente mas directa; (c) dejar espesor de arandela (1.5 mm,
  `doublemedical2021trauma`, otro fabricante) y canulacion (libre) como estan, con su salvedad.
- **Recomendacion del asistente:** (a) + (b) + (c). No queda nada que buscar: es la guia del sistema y no publica esos
  dos parametros.
- **No aplicado** (regla 14). **Tipo:** REDACCION + SUPUESTO / geometria del implante. **Nivel propuesto: N2.**

### 93 — CERRADA (2026-09-20): MAISI recorta su salida a [-1000, 1000] HU, y ese recorte por si solo ya falla la compuerta

- **Paso 0 ejecutado** (regla fijada en `01-decisiones.md`, 2026-09-19: si la normalizacion deja fuera el hueso denso,
  MAISI se descarta por diseno y no se corre). Bundle `maisi_ct_generative` descargado con `monai.bundle` en Khipu
  (autoencoder 80 MB, difusor 2066 MB, ControlNet 275 MB, generador de mascaras).
- **Lo que el paper no publicaba y el bundle si:** `scripts/sample.py` fija `a_min = -1000` y `a_max = 1000` (lineas
  211-212) y devuelve la imagen con `synthetic_images * (a_max - a_min) + a_min` (linea 309). **La salida del modelo
  vive en [-1000, 1000] HU.**
- **Medicion propia, sin modelo y sin GPU** (`p1_maisi.py cota`, 34 pacientes de test, ROI de P1): recortar a ese
  rango y comparar con el CT original da, **solo por el recorte**, MAE en hueso de **media 42.24 HU** (mediana 18.24,
  min 6.96, max 231.43), con **11 de 34 pacientes por encima del umbral de 25 HU**; en metal, miles de HU.
  `experiments/objetivo1/p1_maisi_cota.csv`.
- **Consecuencia:** es una **cota inferior**. Con la regla preinscrita (media por paciente < 25 HU), MAISI **no puede
  pasar la compuerta ni con un autoencoder perfecto**, porque 42.24 > 25 antes de que el modelo haga nada. La
  evaluacion en GPU **no se corre**: no aportaria informacion y gastaria una cola que necesita la opcion A.
- **Lo que esto NO dice:** no evalua a MAISI como generador. Dentro de su rango declarado puede ser excelente; lo que
  queda probado es que **su representacion no cubre el hueso denso ni el metal**, que es justo lo que esta tesis
  necesita. Tambien confirma la lectura de `chen2026foundationvae`, que declara el mismo recorte para generacion.
- **Efecto sobre #91 y la opcion A:** ninguno. La decision del 2026-09-19 ya decia que el resultado de MAISI no cambia
  el diseno del Objetivo 3. Lo que aporta es un argumento mas fuerte para el Objetivo 1: **no es que el VAE de SD 1.5
  sea malo; es que los latentes preentrenados disponibles, incluido uno entrenado en CT, se definen sobre un rango de
  HU que excluye el hueso denso y el metal.**
- **Queda para la redaccion (pendiente de la autora):** una frase en el Objetivo 1 con este resultado, y la cita del
  bundle (no del paper) para el rango. **Tipo:** RESULTADO. **#93 CERRADA.**

---

## Ronda 2026-09-19/20 — estado consolidado (leer esto al retomar)

Escrito para una sesion nueva. Detalle de cada una en su entrada; las decisiones, en `01-decisiones.md`
(2026-09-19 y 2026-09-20).

| # | Tema | Estado |
|---|---|---|
| 91 | **P1 da NO-GO**: mejor combinacion 61.72 HU en hueso, 34/34 pacientes fallan, controles en verde y curvas en plateau | **RESUELTA en redaccion** (`main.tex`, Obj 1) y en alcance (opcion A). Queda como resultado de la tesis |
| 92 | El "24%" de malposicion de la cadena Tejwani/Gardner viene de `tonetti2001results`, que publica 23% binario y sin denominador | ABIERTA (N3). Solo importa si se cita esa cifra |
| 93 | **MAISI descartado por diseno**: su bundle mapea la salida a [-1000, 1000] HU; el recorte solo ya da 42.24 HU en hueso (11/34 sobre el umbral) | **CERRADA**, aplicada a `main.tex` (Obj 1) |
| 94 | MedVAE tampoco resuelve la compuerta y **excluye metal** en su entrenamiento | CERRADA de hecho por la decision 2026-09-19 (no se evalua) |
| 95 | Brecha entre la mascara de entrenamiento (umbral sobre metal real) y la de sintesis (parametrica) | **ABIERTA, bloqueante del Diseno A.** Se resuelve con E11 y con la eleccion de mascara de `diseno_A.md` |
| 96 | El contexto de entrenamiento trae streaking del implante real; el paciente limpio de sintesis no | **ABIERTA, riesgo principal del Diseno A.** Se ve en la evaluacion E-A2 (costura en el borde de la banda) |
| 97 | El nominal de 7.3 mm es la ROSCA; el cuerpo mide 4.8 mm, con cabeza de 8.0 x 4.5 y arandela de 13.0 mm | **VERIFICADA y aplicada** a `main.tex` (geometria) y a `diseno_A.md`. Sin fuente: espesor de arandela y canulacion |
| 98 | `main.tex:54` afirma que no hay precedente que cuantifique una banda peri-implante, y `radzi2014metalartifacts` publica mm en CT | **ABIERTA. Pendiente de la autora**; es la frase mas facil de refutar del documento |
| 99 | La guia del fabricante confirma el fuste pero no publica arandela ni canulacion, y su indicacion sacroiliaca es del calibre 6.5 | ABIERTA (N2). Aplicado lo verificable; no atribuir al fabricante la indicacion del 7.3 |

**Lo que un agente nuevo debe saber antes de tocar nada:**

1. **El Objetivo 1 ya se ejecuto y dio No-Go. El criterio NO se mueve** (`main.tex:77`, regla preinscrita el
   2026-09-17). Cualquier propuesta de bajar el umbral, cambiar la lectura de HU a `oraculo` o entrenar mas pasos
   despues de ver el test repite el patron que `ESTADO.md` manda vigilar (#25, #37, #45, #47, #50, #76).
2. **El Objetivo 3 ya no es latente.** No reintroducir VAE, ControlNet ni Stable Diffusion sin una decision nueva
   de la autora: la opcion A se eligio **despues** del No-Go y asi esta declarado en el documento.
3. **Lo que bloquea el Diseno A no es codigo, son las 4 decisiones de `diseno_A.md`** y las implicancias #95 y #96.
   Los scripts (`e11_perfil_axial.py`, `a1_parches.py`) estan escritos y probados en local.
4. **Nada se cita sin `refs/raw/` o, para documentacion de fabricante, sin la excepcion de `refs/MAPEO.md`.**


## Ronda 2026-09-20 (2) — E11 corrido, y el hueco de implementacion del Diseno A

### 100 — El Diseno A no tiene codigo de entrenamiento ni de evaluacion: el "paso 3, prueba corta en Khipu" no era lanzable, y el presupuesto de #89 no lo contempla — ABIERTA (liga con #89, #90, #91)

- **Origen:** revision de estado pedida por la autora (2026-09-20), verificada contra disco.
- **Hallazgo:** `experiments/objetivo3/` contenia **dos** archivos, los dos de CPU (`a1_parches.py`,
  `diseno_A.md`), y `src/` (`common/`, `muestreador/`, `renderizador/`) estaba **vacio**. La seccion 9 de
  `diseno_A.md` lista como paso 3 de la semana 1 una "prueba corta en Khipu (200 pasos)", pero **no existia red
  que entrenar**: ni U-Net, ni proceso de difusion, ni cargador de parches, ni `.sbatch`.
- **Por que importa, y no es solo trabajo pendiente:** (a) el presupuesto de computo que la entrega de 2 paginas
  le dio al asesor (#89) se construyo con cifras de P1, que era un autoencoder afinado, no una difusion en pixeles
  entrenada desde cero; (b) el plazo (#90) se planifico sin contar este desarrollo; (c) mientras no exista y se
  mida, **cualquier cifra de GPU-h para el Objetivo 3 es una estimacion sin base**, que es exactamente lo que #89
  pedia evitar.
- **Estado tras esta sesion:** escrito y probado en local, en CPU, por orden de la autora del 2026-09-20:
  `src/common/ventanas.py`, `src/common/region.py`, `src/renderizador/{modelo,difusion,datos,entrenar}.py`.
  Los modulos de `src/common/` **reexportan** la implementacion ya validada en `experiments/` en vez de
  reimplementarla, para no crear una segunda version numerica sin control (control de identidad: peor error
  **1.27e-11 HU**). Controles del muestreador verificados en CPU: perdida exactamente 0.0 con `G` vacia, salida
  exactamente 0.0 fuera de `G`, reproducibilidad por semilla.
- **Lo que sigue sin existir:** la evaluacion E-A1..E-A4 (metricas de Peters, baseline de copia-pega, costura en
  el borde de `B_delta`) y el `.sbatch` de Khipu. Y el codigo **no sustituye a la preinscripcion**: `diseno_A.md`
  sigue en BORRADOR con cuatro `[DECIDIR]`.
- **Opciones:** (a) medir la prueba corta de 200 pasos y **actualizar #89 con la cifra medida** antes de
  comprometer plazo; (b) dejar el presupuesto como esta y aceptar que el numero del Objetivo 3 no esta medido.
- **Recomendacion del asistente:** (a). Es una corrida de minutos y convierte la unica cifra no medida de la
  respuesta al asesor en una medida.
- **No aplicado** (regla 14). **Tipo:** ALCANCE / presupuesto y plazo. **Nivel propuesto: N1.**

### 101 — E11 mide el perfil axial en la cohorte: el cuerpo de ~4.9 mm queda confirmado por tercera via independiente, y el ensanchamiento de extremo es de ~1 voxel en la mediana — ABIERTA (resuelve la parte medible de #97; liga con #95, #41)

- **Origen:** E11 corrido sobre los **178 volumenes** el 2026-09-20 (`experiments/objetivo2/e11_perfil_axial.py`;
  salidas en `outputs/e11/`, fuera de git por `.gitignore`). 79 componentes esbeltos (largo >= 30 mm, anchos
  <= 12 mm), tramos de 2 mm, diametro = 2 x p95 del radio, el mismo estimador de E8.
- **Resultado principal:** `d_centro` mediana **4.91 mm** (p10 3.39, p90 7.37). Coincide con el fuste de catalogo
  **4.8 mm** (`synthes2003guide`, impresa 2) y con los **5.00 mm** medidos por E8 con otro metodo. Tres vias
  independientes — catalogo del fabricante, censo E8 y perfil axial — dentro de un cuarto de voxel.
- **Ensanchamiento de extremo (extremo mas ancho menos centro), n = 59 componentes con los tres valores:**
  mediana **0.96 mm**, p90 3.41 mm, maximo 4.07 mm. Por encima de un voxel (~0.78 mm): **33/59**. Por encima de
  2.0 mm: **12/59**. Por encima de 3.0 mm: **7/59**.
- **Como se lee (la decision es de la autora, D3 de `diseno_A.md` seccion 8 bis):** la mediana de 0.96 mm es
  **del orden de un voxel**, asi que en el caso tipico el volumen parcial **si** promedia cabeza y rosca, y el
  cilindro uniforme de ~5 mm queda justificado con medicion propia. Pero **no es despreciable en una minoria**:
  12 de 59 superan 2 mm, que es lo que se esperaria si el CT estuviera resolviendo una cabeza de 8.0 mm sobre un
  cuerpo de ~5 mm. La lectura conservadora es **cilindro uniforme como piloto, cabeza como sensibilidad**, que es
  justamente el par que `diseno_A.md` seccion 6 ya tenia propuesto — ahora con cifra propia detras.
- **Salvedades que hay que declarar si esto va al documento:** (a) el filtro es **geometrico**, no por tipo de
  implante: entre los 79 esbeltos hay material que no es tornillo iliosacro; (b) 5 de los componentes esbeltos
  estan en casos `dataset6`, el grupo nominalmente sin metal; (c) `d_max` (mediana 8.10 mm) es un **maximo sobre
  tramos** y por tanto sesgado al alza, no debe citarse como "diametro de cabeza medido"; (d) 2 componentes no
  dieron `d_centro` y 20 no dieron los dos extremos (tramos con menos voxeles que el minimo).
- **Lo que NO resuelve:** #95 sigue abierta. E11 dice como es el metal real; no dice cuanto se parece la mascara
  por umbral a la mascara parametrica, que es la brecha que el Diseno A tiene que declarar.
- **No aplicado** (regla 14). **Tipo:** GEOMETRIA / medicion propia. **Nivel propuesto: N1.**

### 102 — A1 sobre la cohorte: `G` se define por CORTE y no por IMPLANTE, asi que en pacientes con material bilateral la region de generacion abarca toda la pelvis y el parche no la contiene (20.1% de los cortes) — ABIERTA (liga con #95, #96, y decide D2)

- **Origen:** A1 corrido sobre la particion completa el 2026-09-20 (`experiments/objetivo3/a1_parches.py`;
  resumen versionado en `experiments/objetivo3/a1_casos.csv`).
- **Lo que salio bien, y cierra un bloque de la evaluacion:** el **control de composicion dio 13496 de 13496**
  cortes identicos bit a bit fuera de `G`. La fila E-A3 ("preservacion fuera de la banda, cero por construccion")
  queda respaldada por el control, no solo por el argumento.
- **Hallazgo:** **2714 de 13496 cortes (20.1%)** tienen `G` que no cabe en el parche de 256. La prueba piloto en
  2 casos habia dado 216 de 216, es decir **0%**: dos casos no eran la cohorte.
- **Dos explicaciones descartadas con datos:**
  - *No* es la mezcla de implantes: casos **con** componente esbelto 20.0%, **sin** componente esbelto 20.2%.
  - *No* es el spacing: por tramos de spacing en plano da 13.3%, 21.7%, 23.7% y 11.9%, sin tendencia.
- **Causa verificada:** en los tres casos peores el metal tiene **9, 12 y 7 componentes** de mas de 50 voxeles,
  con extension en plano de **380, 358 y 321 mm**, es decir toda la anchura pelvica. `G` es la union de **todo**
  el metal del corte, asi que un paciente con implantes bilaterales produce una `G` que ningun parche centrado
  puede contener. El parche de 256 mide 211.7 mm de mediana: el problema no es que sea pequeno.
- **Por que importa mas alla del encuadre:** en **sintesis** se coloca **un** tornillo, cuya `G` (cilindro de
  ~4.9 mm mas banda de 12 mm) cabe de sobra. Entrenar con `G` multi-implante y usar con `G` de un implante es una
  **segunda brecha de dominio**, distinta de #95 (que es sobre el borde de la mascara) y que hoy no esta declarada.
- **Opciones:**
  - (a) **Extraer por COMPONENTE en vez de por corte**: cada componente conexo de `M` con su propia `B_delta` y su
    propio parche. La `G` de entrenamiento pasa a tener la misma estructura que la de sintesis (un implante),
    la contencion deja de ser un problema de encuadre y de paso se puede reportar y equilibrar la mezcla por
    tamano de componente, que es el riesgo 3 de este documento.
  - (b) Agrandar el parche. El computo crece con el cuadrado del lado y aun asi no cubre los 380 mm.
  - (c) Dejar 256 y declarar que el 20% de los cortes entrena con `G` truncada.
- **Recomendacion del asistente:** **(a)**. Es la unica que alinea entrenamiento con uso; (b) no alcanza y (c)
  ensena al modelo a completar mascaras cortadas por el borde, que en sintesis nunca ocurre. Cuesta una
  modificacion de `a1_parches.py` y volver a correrlo (~2 h de CPU).
- **No aplicado** (regla 14). **Tipo:** DISENO / definicion de la unidad de entrenamiento. **Nivel propuesto: N1.**

### 102 — ACTUALIZACION (2026-09-20): DECIDIDA opcion (a), extraccion por componente; verificada en el peor caso

- **Decision de la autora** (*"ahora trataremos D2 como COMPONENTE"*), escrita en `01-decisiones.md`,
  entrada 2026-09-20 (2), seccion D2.
- **Verificacion antes de adoptarla, en dos casos de prueba** (uno de ellos `CLINIC_metal_0044`, el peor de esta
  implicancia, con 215 de 298 cortes sin contener): la extraccion por componente da **0 de 1217 parches** con `G`
  fuera del encuadre, frente al **20.1%** por corte. **Control de composicion 1217 de 1217.** El diagnostico
  (la union multi-implante, no el tamano del parche) queda confirmado por el arreglo.
- **Efecto secundario medido y declarado:** **548 de 1217** parches contienen metal de **otro** componente. No se
  enmascara —es anatomia real del paciente— pero se cuenta en `n_metal_otros`. Es insumo cuantitativo para #96,
  no su solucion.
- **Codigo:** `experiments/objetivo3/a1b_parches_componente.py` (nuevo). `a1_parches.py` queda **CONGELADO** como
  evidencia de esta implicancia, igual que `ts_piloto_qc.py` para #49/#50. `src/renderizador/datos.py` agrupa el
  2.5D por **serie** (caso + componente), de modo que los vecinos de un corte son del **mismo implante** y no del
  contralateral; reporta `casos` (pacientes, unidad de la particion) y `series` (implantes, unidad de
  entrenamiento) por separado.
- **Coste aceptado:** el numero de parches sube (un corte con varios implantes produce un parche por implante), y
  con el crece el cache y el tiempo de subida a Khipu. `a2_entrenar.sbatch` y la seccion A2 de `KHIPU.md` ya
  apuntan a `a1b_cache`, con la advertencia de borrar `a1_cache` si se subio antes.
- **Sigue ABIERTA la parte de #96** que esta decision no toca: el contexto de entrenamiento trae streaking del
  implante real y el paciente limpio de sintesis no.

### 103 — La extraccion por componente murio por memoria a los 47 de 79 casos y perdio todo lo calculado: dos defectos de diseno corregidos, y un dato para #89 — CERRADA (registro; liga con #102, #89)

- **Que paso:** la primera version de `a1b_parches_componente.py` se detuvo en el caso 47 de 79 **sin traceback y
  sin escribir un solo CSV**. El proceso ya no existia. Es el patron que `ESTADO.md` avisa ("dos corridas de fondo
  murieron por RAM") y el mismo de E10 el 2026-09-14 (SIGKILL externo, `Caso,Error` vacio por falta de `finally`).
- **Causa:** por cada componente se materializaban **dos mascaras del tamano del volumen completo**
  (`etiquetas == lab` y su banda). Con 9-12 componentes por caso y ~1.4 GB de RAM libre, la PC no aguanta.
- **Corregido, y por que asi:**
  1. **Memoria:** se trabaja dentro de la **caja del componente** ensanchada por la banda (`find_objects`), sin
     materializar nunca una mascara del volumen entero. Fuera de esa caja la `G` del componente es vacia **por
     definicion**, asi que no se pierde nada.
  2. **Reanudable:** los CSV se anexan **caso a caso con `flush`**, y al arrancar se saltan los casos que ya tienen
     fila en `a1b_casos.csv`. Un corte deja de costar la corrida entera.
- **Control de que la correccion no cambia el resultado:** los tres casos de prueba dan cifras **identicas** a la
  version que murio (`0016`: 4 comp / 461 parches / 0 no caben; `0044`: 12 comp / 756 / 0; `0022`: 1 comp / 75 /
  **31 no caben**). La reescritura es equivalente, solo mas liviana.
- **Dato que hay que llevarse a #89:** `0022` tiene **31 de 75** parches sin contener **con un solo componente**.
  La extraccion por componente **no lleva la no-contencion a cero en todos los casos**: hay implantes que por si
  solos exceden los 256 px. El titular "0 de 1217" salia de dos casos elegidos; la cifra de cohorte saldra del
  `a1b_parches.md` final y **hay que citar esa, no la de los casos de prueba**.
- **Tipo:** INFRAESTRUCTURA / honestidad de cifras. **Nivel propuesto: N2.** No toca `main.tex`.

### 98 — APLICADA en `main.tex` (2026-09-20), opciones (a) + (b), por orden explicita de la autora

- **Orden:** *"Sobre #98, aplica (a) + (b) y redacta main.tex"* (2026-09-20).
- **Antes:** *"together with $B_{\delta}$, for which no published precedent quantifying a peri-implant band was
  found"*. Era un reclamo de ausencia refutable con una sola cita.
- **Despues:** el reclamo se acota a *"no published precedent quantifying a **generation band outside the implant
  mask**"* (opcion a) y se **cita el precedente de medicion** (opcion b): `radzi2014metalartifacts` con
  *"2.0, 2.6, 1.6 and 2.0 mm"* y `cassanego2026evolution` con 3.1-4.2 mm.
- **Diferencias declaradas en el texto, todas con respaldo en ficha:** la medida es *"the perpendicular distance
  from the central screw axis to the boundary of the artifact"* (Radzi, Abstract p. 163), es decir desde el **eje**
  y no desde la superficie; el umbral de la superficie umbralizada **no se publica**; son tornillos de 3.5-4.0 mm
  en tobillo de un solo cadaver y en contexto dental; **no reportan HU**; y los dos rangos **no son comparables
  entre si** por falta de punto de referencia comun. Se cierra diciendo que el ancho de banda usado aqui es una
  **construccion declarada, no una medicion heredada**.
- **Lo que NO cambia:** `B_delta` = 12 mm sigue sin calibracion publicada. Radzi no la respalda ni la refuta.
- **Compilacion verificada:** 0 errores, **0 citas indefinidas**, 7 paginas, 95 referencias. Las dos claves ya
  estaban en `refs.bib` (lineas 55 y 552), asi que **`refs.bib` no se toco** (regla 9 respetada).
- **Estado: CERRADA** en redaccion. **Tipo:** REDACCION / reclamo de novedad.

### 104 — La composicion del conjunto de entrenamiento no coincide con la tarea de sintesis: 42.5% de parches sin metal, 40.3% con metal ajeno y componentes que son fragmentos — ABIERTA (liga con #95, #96, #102; toca D4)

- **Origen:** A1b corrido sobre la particion completa el 2026-09-20 (79 casos, 363 componentes, **23 058 parches**,
  0 errores). Salidas en `experiments/objetivo3/outputs/a1b/`.
- **Lo que cierra:** D2 queda verificada en cohorte. La no-contencion baja de **2714/13496 (20.1%)** por corte a
  **336/23058 (1.5%)** por componente, con **0/1304** en validacion, y el control de composicion da
  **23 058 de 23 058**. La decision de extraer por componente **funciona y no se revierte**.
- **Lo que abre, en tres cifras medidas:**
  1. **42.5% de los parches (9 811) no contienen NINGUN voxel del implante objetivo.** `n_metal` mediana 20
     voxeles, p10 = 0. Es estructural: `B_delta` se extiende 12 mm en 3D, asi que los cortes mas alla de las
     puntas tienen `G` sin `M`. Casi la mitad del entrenamiento seria "rellena una banda donde no hay metal",
     que **no es la tarea de sintesis**.
  2. **40.3% de los parches (9 298) contienen metal de OTRO componente**, y en **6 886** el metal ajeno supera al
     propio. En **4 452 (19.3%) no hay metal propio y si ajeno**: el modelo ve metal que no debe explicar y no ve
     el que si. Es #96 medido, y mas severo que como estaba descrito.
  3. **Los componentes son mayoritariamente fragmentos.** Volumen mediano **458 mm3**, frente a ~1450 mm3 de un
     tornillo de 4.8 x 80 mm. El **52%** esta por debajo de 500 mm3 y el **18%** por debajo de 50 mm3. El umbral
     usado (`MIN_COMP_MM3` = 10, heredado de `e8_censo_implantes`) sirve para **censar** metal, no para definir
     una **unidad de entrenamiento**.
- **Causa de fondo:** el diseno nunca declaro una politica de **que componente y que corte entran como ejemplo**.
  Hoy la decide por omision un umbral heredado de otro experimento. El `[SUPUESTO]` de la seccion 3 de
  `diseno_A.md` ("entra todo el metal de los pacientes de entrenamiento") se escribio antes de tener estas cifras.
- **Toca D4, y esto es lo mas facil de pasar por alto:** el margen `Delta` se mide sobre validacion, y
  **validacion tiene 673 de 1304 parches (51.6%) sin metal**. Medir ahi la variabilidad del metodo sin
  estratificar daria un `Delta` dominado por parches donde no hay nada que generar, y por tanto
  **artificialmente pequeno**, lo que haria mas facil declarar "equivalencia". Es el mismo patron que D4 trataba
  de evitar, entrando por otra puerta.
- **Opciones (politica de muestreo, a PREINSCRIBIR antes de entrenar):**
  - (a) Volumen minimo de componente. A 200 mm3 se excluye el 35% de componentes y solo el **18.7%** de los
    parches; a 500 mm3, el 52% de componentes.
  - (b) Proporcion declarada de parches sin metal. No eliminarlos (la banda mas alla de la punta es real), pero
    fijar un objetivo a priori en vez de heredar el 42.5%.
  - (c) Metal ajeno: como minimo estratificar y reportar; para el piloto, considerar excluir los parches donde el
    ajeno supera al propio.
  - (d) Estratificar la medicion de `Delta` por presencia de metal.
- **Recomendacion del asistente:** (a) 200 mm3 en el piloto + (b) ratio declarado ~1 sin metal por cada 2 con
  metal + (c) estratificar y reportar + (d) obligatoria. Se aplican al construir el `Dataset`, **sin volver a
  recorrer la cohorte**.
- **Advertencia metodologica sobre un numero que NO debe usarse:** al cruzar los 363 componentes con el filtro
  geometrico de E11 salieron "14 tipo tornillo". **Es un artefacto:** se calculo con las extensiones de la caja
  alineada a los ejes, mientras E11 usa el eje principal por PCA; un tornillo oblicuo tiene caja grande en los
  tres ejes y el filtro lo rechaza por construccion. El cruce correcto exige emparejar indices de componente
  entre los dos scripts, que no coinciden. **No citar ese 14.**
- **No aplicado** (regla 14). **Tipo:** DISENO / composicion del conjunto de entrenamiento. **Nivel propuesto: N1.**

### 104 — ACTUALIZACION (2026-09-20): el subconjunto limpio esta cuantificado, y la opcion (c) es viable

- **Pregunta de la autora** (2026-09-20): si conviene revisar `revision.csv` a mano, aislar casos con metal
  limpio, o quedarse solo con criterios automaticos.
- **Precision sobre `revision.csv`, para que no se pierda:** de ese archivo **solo esta en uso la columna
  `Metal`** (si/no), que ya esta **178/178 completa**, y llega a los experimentos **indirectamente**, via
  `p1_particion.csv`. `e11_perfil_axial.py` y `a1b_parches_componente.py` **no lo leen**. Las columnas
  incompletas (`Tipo de estructura observada`, `Artefactos`, `Severidad`) **no las usa ningun experimento del
  Diseno A**. Completarlas **no resolveria #104**: `revision.csv` tiene una fila **por volumen** (178) y el
  problema es **por componente** (363). Es la granularidad equivocada.
- **Subconjunto limpio, medido:** parches con metal propio, **sin metal ajeno** y de componentes >= 200 mm3:
  **7 974 parches**, **197 componentes**, **68 casos** (train 7 631 en 63 casos; val 343 en 5 casos). Es un
  tercio del total crudo, pero cada ejemplo contiene el implante que el modelo debe explicar y nada mas.
- **Casos con pocos implantes**, por si se prefiere filtrar por caso y no por parche: <= 1 componente 18 casos
  (1 273 parches), <= 2 componentes 28 casos (3 066), <= 3 componentes 42 casos (6 171), <= 5 componentes 57
  casos (10 500).
- **Recomendacion del asistente, afinada con estas cifras:** piloto sobre el **subconjunto limpio** (7 974) y
  conjunto completo como sensibilidad; criterios **automaticos** (volumen, elongacion por eje principal, metal
  ajeno) como filtro primario, **validados** contra laminas de contacto de una muestra de 30-40 componentes
  revisada por la autora, con el formato de las laminas de E9-TS. La revision por forma **no requiere criterio
  medico** —distinguir objeto alargado y fino de placa o fragmento es geometria, no diagnostico—, a diferencia
  de #53, que si lo requeria.
- **Dos condiciones que no se pueden saltar:** (1) el filtro se **declara antes** de entrenar, o es seleccion
  post hoc; (2) `val` baja a **343 parches en 5 casos**, asi que la medicion de `Delta` de D4 hay que
  **estratificarla** igualmente.
- **Sigue ABIERTA.** La politica de muestreo es decision de la autora y falta preinscribirla.

### 104 — ACTUALIZACION (2026-09-20): laminas generadas, planilla lista, revision pendiente de la autora

- **Generadas 40 laminas** con `experiments/objetivo3/a3_laminas_componentes.py` (semilla 20260920,
  reproducible). Muestra estratificada por volumen en escala logaritmica, con **sobremuestreo deliberado de la
  franja 100-500 mm3**, que es donde cae el umbral propuesto (200 mm3). Cubre de **11 a 15 530 mm3**.
- **Planilla:** `experiments/objetivo3/a3_revision_componentes.csv` (40 filas, ordenadas por volumen, columnas
  `veredicto` y `nota` vacias). Guia: `a3_revision_componentes.md`. Laminas en `outputs/a3/laminas/`, fuera de git.
- **Hipotesis a contrastar, escrita ANTES de mirar:** la columna `propuesta_auto` trae lo que dice hoy el filtro
  (< 200 mm3 = `fragmento`; si no, `tornillo` cuando largo >= 30 mm y ancho <= 12 mm por **PCA**, si no
  `otro implante`). Reparto: **17 `fragmento`, 17 `otro implante`, 6 `tornillo`**. Que este escrito de antemano
  es lo que permite medir acuerdo en vez de racionalizar despues.
- **Medida de forma corregida respecto al error ya registrado:** las laminas y la planilla usan **eje principal
  por PCA**, como E11, y no la caja alineada a los ejes que produjo el "14 tipo tornillo" que esta implicancia
  manda no citar.
- **Que decide esta revision:** no 40 componentes, sino **si el umbral de 200 mm3 es defendible**. Los dos tipos
  de error tienen consecuencias distintas y se reportaran por separado: `fragmento` automatico que resulta
  tornillo (umbral alto, quita datos buenos) frente a `tornillo`/`otro implante` que resulta fragmento o no es
  metal (umbral bajo, mete ruido, que es lo que #104 sospecha).
- **Regla fijada de antemano:** si aparece un patron de error, se recalibra el criterio y se vuelve a mirar **la
  misma muestra**. No se genera una muestra nueva despues de ver el resultado.
- **Sigue ABIERTA.** Bloquea el entrenamiento: nada se entrena antes de que la politica de muestreo este escrita
  en `01-decisiones.md`.

### 105 — 29 de los 79 casos de entrenamiento NO tienen material ortopedico: su metal son electrodos, cremalleras, DIU y accesorios de ropa, y aportan el 20.5% de los parches y 2 de los 5 casos de validacion — ABIERTA (liga con #104, #102; toca D4 y la particion)

- **Origen:** observacion de la autora al revisar las primeras laminas de A3 (2026-09-20): *"aparecen artefactos
  que no estan siquiera dentro del cuerpo (accesorios exteriores o incluso electrodos)"*. Cuantificado despues
  contra `revision.csv`.
- **Hallazgo, con la columna que la propia autora creia sin terminar:** `Tipo de estructura observada` de
  `revision.csv` esta **completa para todos los casos con metal**, y sobre los 79 casos de A1b declara
  **29 casos SIN material ortopedico**. Su metal es `electrodo`, `zipper (cursor)`, `diu`, `accesorio de la
  ropa`, `botones`. Aportan **100 componentes y 4 719 parches = 20.5% del conjunto**.
- **Lo mas grave: contamina la validacion.** **2 de los 5 casos de validacion** (`dataset6_CLINIC_0019_data`,
  `dataset6_CLINIC_0102_data`) no contienen ningun implante. Validacion es donde D4 manda medir el margen
  `Delta`. Medirlo ahi significa estimar la variabilidad del metodo sobre pacientes donde **no hay implante que
  generar**, lo que lo hace artificialmente pequeno y facilita declarar "equivalencia". Es el tercer camino por
  el que D4 puede viciarse (los otros dos: #104, parches sin metal; y la falta de estratificacion).
- **Por que entraron:** la particion se filtra por la columna **`Metal` = si**, que dice si hay metal, **no si
  hay implante**. Un electrodo de ECG es metal. El filtro nunca pretendio distinguirlos.
- **Correccion a lo que este asistente afirmo antes (registro del error):** en la actualizacion anterior de #104
  se dijo que completar `revision.csv` **no** resolveria el problema, por ser granularidad de volumen y no de
  componente. Eso **sigue siendo cierto para elegir el umbral por componente**, pero era una respuesta
  incompleta: la anotacion **ya existente** resuelve un eje distinto y mayor —excluir casos enteros sin
  implante— sin trabajo manual nuevo. La columna que parecia no aportar es la que ataja el 20.5%.
- **Opciones:**
  - (a) Excluir del entrenamiento los 29 casos sin material ortopedico declarado, **y rehacer la particion de
    validacion** para que los 5 casos tengan implante.
  - (b) Excluir solo los componentes externos, conservando los casos (requiere juicio por componente: es #104).
  - (c) Conservarlos como contexto negativo, declarado.
- **Recomendacion del asistente:** **(a) para validacion, obligatorio** —un conjunto de validacion sin implantes
  no puede calibrar nada— y **(a) tambien para entrenamiento en el piloto**, con (c) como sensibilidad si se
  quiere medir si el metal no osteosintetico aporta o estorba. **Ojo:** rehacer la particion toca la *Strict
  Isolation Rule* (`main.tex:111`) y la semilla 20260917 de P1; hay que declarar el cambio y **no tocar test**.
- **Categorias `externo` y `diu` anadidas** a la planilla de A3 (`a3_revision_componentes.md`): el esquema
  original las habria forzado a `otro implante`, que es exactamente el error que contamina el entrenamiento.
- **No aplicado** (regla 14). **Tipo:** DATOS / composicion de la cohorte y particion. **Nivel propuesto: N1.**

### 106 — Las cuatro fuentes del metodo ya son citables, pero su combinacion exacta no fue validada y no hay evidencia de superioridad frente a DiT — ABIERTA (liga con #74, #100)

- **Origen:** pregunta de la autora (2026-09-20) sobre por que U-Net y no una arquitectura mas nueva. Al verificar
  la bibliografia aparecio el hueco inverso al que se buscaba.
- **Actualizacion tras lectura profunda (2026-09-21):** ya estan en `refs.bib`, con raw, clean, PDF y ficha,
  **Ho et al. 2020** (DDPM) y **Dhariwal y Nichol 2021** (ADM). Tambien entraron seis fuentes para justificar
  o tensionar la arquitectura: Ronneberger 2015, Liu 2021, Peebles y Xie 2023, Yeap et al. 2025, Zhang et al.
  2025 (LeFusion) y An et al. 2025.
- **Cierre bibliografico 2026-09-21:** ya estan tambien en `refs.bib`, con raw, clean, PDF y ficha:
  - **Nichol y Dhariwal 2021**, fuente primaria del planificador **coseno**: `s = 0.008`, beta recortada a 0.999.
  - **Song et al. 2021**, fuente primaria de **DDIM**: define el caso determinista eta = 0 y evalua 50 pasos.
  Con estas dos altas, las cuatro fuentes metodologicas quedan disponibles para citar.
- **Lo que hoy se cita en `main.tex` para el renderizador** (`rombach2022latentdiffusion`, `zhang2023controlnet`,
  `karageorgos2024ddpm`) **no es fuente de ninguna de las cuatro**: Rombach es latente (y el latente se
  descarto), ControlNet se cayo con el (#74) y Karageorgos es una aplicacion a MAR, no el metodo base.
- **Que si respalda U-Net:** Ho documenta el backbone U-Net residual con normalizacion por grupos y atencion;
  ADM conserva esa familia y publica ablaciones arquitectonicas; Yeap prueba viabilidad de una U-Net 2D de
  difusion para CT con pocos pacientes y condicion concatenada; LeFusion aporta una U-Net 3D para sintesis local
  en CT, perdida enmascarada y recomposicion con fondo real. Ronneberger solo sustenta el origen del sesgo local y
  multiescala. Ninguna de estas fuentes estudia sintesis peri-implante pelvica ni compara U-Net contra DiT.
- **Dos correcciones obligatorias al razonamiento anterior:**
  1. Peebles y Xie no aplican atencion sobre 65 536 pixeles: DiT tokeniza **parches latentes**. Por tanto, el
     argumento O(N^2) sobre cada pixel no describe esa alternativa y debe retirarse.
  2. An et al. compara DiT y U-Net en espacio de pixeles y a FLOPs equivalentes; con 10^3--10^4 imagenes naturales
     32 x 32 reporta una brecha de PSNR menor para DiT. La localidad ayuda, pero tambien puede incorporarse a DiT.
     No se transfiere directamente a CT, metal o inpainting, pero invalida afirmar que pocos datos demuestran una
     ventaja de U-Net.
- **Razonamiento que queda defendible:** la U-Net es una eleccion **pragmatica y no comparada**, alineada con DDPM,
  ADM y dos precedentes medicos cercanos, entrenable en el pipeline ya implementado y sin depender del VAE que
  fracaso en #74. Las conexiones de salto y la localidad son motivaciones arquitectonicas, no garantia de ausencia
  de costuras; esa propiedad depende de la composicion explicita fuera de `G` y debe evaluarse.
- **Limite metodologico descubierto al cerrar las fuentes:** los componentes estan respaldados **por separado**,
  pero la configuracion conjunta de `src/renderizador/difusion.py` no aparece evaluada en ninguno: schedule coseno
  con T = 1000 + DDIM con subsecuencia lineal, eta = 0 y 50 pasos + U-Net + CT. Song usa T = 1000 y evalua 50
  pasos, pero no el schedule coseno. Nichol--Dhariwal usa T = 4000 en las ablaciones relevantes; sus 50 *forward
  passes* corresponden a Improved DDPM con varianza aprendida, no a DDIM eta = 0. Ademas reporta que el stride
  cuadratico de Song perjudico al combinarse con coseno. La implementacion local usa `torch.linspace`, es decir,
  una subsecuencia lineal.
- **Opciones:** (a) citar las cuatro fuentes por cada componente y declarar que la integracion se valida localmente;
  (b) atribuir la combinacion completa a una sola fuente, lo que seria incorrecto.
- **Recomendacion del asistente:** (a). Al redactar Metodos, citar Ho/ADM por la familia arquitectonica, Song por
  DDIM eta = 0 y 50 pasos, Nichol--Dhariwal por la formula coseno, Yeap por CT + pocos pacientes + concatenacion y
  LeFusion por inpainting local; declarar que no hubo comparacion U-Net--DiT y que la configuracion conjunta es una
  integracion propia que requiere evaluacion.
- **No aplicado** (regla 14). **Tipo:** BIBLIOGRAFIA / atribucion de metodo. **Nivel propuesto: N1.**

### 107 — `main.tex` llama a `karageorgos2024ddpm` "an image-domain diffusion model", pero su DDPM opera en el dominio de SINOGRAMA: la cita que ancla el umbral de 25 HU esta mal caracterizada, y ademas debilita el argumento del Objetivo 3 — ABIERTA (liga con #91, #61, #63)

- **Origen:** pregunta de la autora (2026-09-20) sobre que arquitectura usa cada paper de referencia. Al verificar
  contra la ficha aparecio la discrepancia.
- **Lo que dice `main.tex`:** *"The NMAR algorithm ... reports an RMSE of 20.2~HU, **an image-domain diffusion
  model 12.3~HU** \citep{karageorgos2024ddpm}"*. Es parte del anclaje del umbral de 25 HU (decision
  2026-09-15 (2)).
- **Lo que dice la ficha `karageorgos2024ddpm.md`, con frase textual:** entrena un DDPM **incondicional en el
  dominio de sinograma**: *"a DDPM-based approach is proposed for inpainting of missing sinogram data for
  improved MAR"* (Abstract) y *"The DDPM was unconditionally trained with the ground truth sinograms, S_GT"*
  (Sec. II-A). El implante se reinyecta por umbralizacion, no se modela: *"an estimate of the metal object was
  added, by thresholding the uncorrected image"* (Sec. II-F).
- **Que parte es y que parte no es error:** el **12.3 HU si** se mide sobre la imagen reconstruida (Tabla I,
  p. 28), asi que la cifra y su uso como ancla **se sostienen**. Lo que esta mal es llamar al **modelo**
  "image-domain": es un DDPM de sinograma cuyo error se reporta en HU tras reconstruir.
- **Por que no es un detalle menor:** el Objetivo 3 se sostiene sobre que la apariencia se puede generar **en el
  dominio imagen sin acceso a proyecciones** (`main.tex`, parrafo del supuesto). Citar un metodo de **sinograma**
  como si fuera la evidencia de rendimiento del dominio imagen **resta fuerza justo al argumento que hay que
  defender**, y un jurado que conozca el paper lo detecta.
- **Error del asistente en el mismo hilo, registrado:** en la conversacion del 2026-09-20 este asistente le dijo
  a la autora que `karageorgos2024ddpm` era "difusion en espacio de imagen, en CT, con metal" y que era "la
  prueba de que el dominio imagen funciona aca", para un mensaje a su asesor. **Es falso** por lo mismo de
  arriba. Es el patron que `ESTADO.md` manda vigilar (#25, #37, #45, #47, #50): un enunciado se vuelve verdad
  por repetirse. Queda corregido aqui.
- **Opciones para `main.tex`:** (a) cambiar *"an image-domain diffusion model"* por *"a sinogram-domain
  diffusion model, evaluated in image space"*, que es exacto y conserva el ancla; (b) sustituir el ejemplo por
  uno que si sea de dominio imagen, **si existe con cifra en HU** (hoy no consta ninguno en `refs.bib`);
  (c) dejarlo.
- **Recomendacion del asistente:** **(a)**. Cuesta cinco palabras, mantiene el anclaje del umbral y elimina una
  objecion facil. **NO aplicado** (regla 14): toca `main.tex` y espera orden explicita.
- **Cual es de verdad el referente arquitectonico mas cercano:** **no** Karageorgos, sino `ramzan2026claim`
  (CLAIM), que segun su ficha usa *"a conditional diffusion model based on Denoising Diffusion Probabilistic
  Model (DDPM)"* (Sec. 2, p. 3) con *"The diffusion model (often implemented as a UNet parameterized by theta)"*
  (Sec. 2.1, p. 4), **no latente y no Stable Diffusion** (item 16 de su ficha: NO ENCONTRADO EN EL PDF).
- **Tipo:** REDACCION / caracterizacion de una cita. **Nivel propuesto: N1.**

### 108 — La Tabla III de `karageorgos2024ddpm` cuantifica el colapso de calidad al subestimar la mascara metalica, y hoy NO se usa para justificar `B_delta` — ABIERTA (liga con #98, #57, #104)

- **Origen:** pregunta de la autora (2026-09-20) sobre por que Karageorgos es relevante por sus cifras en HU.
  Al revisar su ficha aparecieron dos tablas cuyo contenido no esta en el argumento de la tesis.
- **Hallazgo 1 — respaldo cuantitativo para `B_delta`, sin usar.** Tabla III (p. 16): con mascara **ensanchada**
  el RMSE se mantiene (R = 1.4 -> 11.45; R = 1.8 -> 11.63), y con mascara **reducida** se desploma
  (R = 0.7 -> **54.82**; R = 0.5 -> **57.69**). La referencia con traza real da 7.57. La propia ficha ya lo
  marcaba: *"dato util para justificar la banda extendida B_delta"*. **Hoy `main.tex` no lo cita.**
  - **Por que importa:** `B_delta` = 12 mm es la decision con menos respaldo externo del diseno. #98 se cerro
    acotando el reclamo de novedad, pero **la anchura sigue sin justificacion publicada**. Esta tabla no la
    calibra —es sensibilidad de mascara en MAR de sinograma, no anchura de banda de generacion— pero **si
    respalda la direccion**: subestimar la extension del metal degrada, ensancharla no penaliza. Es el argumento
    mas fuerte disponible hoy para generar mas alla de la mascara.
- **Hallazgo 2 — el tamano del implante domina el error, y refuerza #104.** Tabla II (p. 29), mismo DDPM:
  pelvis (Paciente 1) **RMSE_INT 11**, protesis total de cadera (Paciente 4) **RMSE_INT 147**, trece veces peor.
  Es evidencia externa de que **tornillos y protesis no son intercambiables** ni para entrenar ni para evaluar,
  que es justo lo que #104 sospecha desde los datos propios.
- **Lo que NO autoriza:** ninguna de las dos cifras calibra los 12 mm. Citarlas como si fijaran la anchura seria
  el patron de #25/#45. Sirven como **respaldo de direccion**, declarado como tal.
- **Opciones:** (a) citar la Tabla III en el parrafo de `B_delta` como respaldo de direccion, con la salvedad de
  que es sensibilidad de mascara en MAR y no anchura de banda; (b) citar ademas la Tabla II en el argumento de
  #104 sobre mezcla de implantes; (c) no usarlas.
- **Recomendacion del asistente:** **(a) + (b)**. Las dos son cifras publicadas, verificadas contra ficha con
  pagina, y cubren los dos puntos mas debiles del diseno actual.
- **No aplicado** (regla 14). **Tipo:** REDACCION / respaldo de una decision de diseno. **Nivel propuesto: N1.**

### 104 — ACTUALIZACION (2026-09-20): las laminas de A3 cortaban por el eje equivocado; corregidas y regeneradas

- **Origen:** la autora, revisando las laminas, pregunto que significaba "corte 344" porque no le cuadraba al
  abrir ITK-SNAP.
- **Fallo:** `a3_laminas_componentes.py` tomaba el corte con `arr[k]` sobre el **eje 0 del archivo**, sin el
  `moveaxis` que si hace `a1b_parches_componente.py`. En esta cohorte la orientacion es **('L','P','S')** y el
  **eje axial es el 2**, asi que el panel rotulado "CT, corte N" mostraba un plano **sagital** y su numero no
  correspondia a ningun corte axial del visor. El panel "proyeccion axial" tampoco lo era.
- **Alcance:** afecta solo a la **herramienta de revision**, no a ningun resultado. `a1b_parches_componente.py`
  y `e11_perfil_axial.py` siempre trabajaron en el marco correcto, asi que **ninguna cifra publicada cambia**.
  Las tres proyecciones de la mascara seguian siendo utiles para juzgar forma (son ortogonales en cualquier
  orden); lo inservible era el numero de corte y el rotulo.
- **Corregido:** se mueve el eje axial al 0 antes de dibujar, y ademas cada lamina y cada fila de la planilla
  traen ahora el **centroide del componente en indices del archivo** (`voxel_itksnap`, formato `x, y, z`), que
  es lo que se teclea en el cursor de ITK-SNAP y no depende de convenciones de rotulado. Se declara que el
  indice es **base 0**. Laminas regeneradas (40, misma semilla 20260920).
- **Por que se registra:** esta revision es la evidencia que sostendra el umbral de #104. Una herramienta que
  muestra un plano distinto del que dice es exactamente el tipo de error que `ESTADO.md` manda vigilar
  (#25, #37, #45, #47, #50): el revisor habria juzgado sobre un plano equivocado creyendo que era otro.
- **Nota operativa:** si la regeneracion falla con `OSError [Errno 22]`, hay un visor de PNG con el archivo
  abierto; basta cerrarlo.

### 104 — RESULTADO DE LA REVISION (2026-09-21): el filtro automatico acierta 15 de 40, y el umbral de volumen esta mal planteado, no mal calibrado

- **La autora lleno las 40 filas** de `a3_revision_componentes.csv`. Acuerdo exacto con `propuesta_auto`:
  **15/40 = 38%**.

| Propuesta \ Veredicto | tornillo | otro implante | fragmento | externo | diu | dudoso |
|---|---|---|---|---|---|---|
| **tornillo** (6) | **4** | 0 | 2 | 0 | 0 | 0 |
| **otro implante** (17) | 1 | **8** | 2 | 5 | 1 | 0 |
| **fragmento** (17) | 0 | 1 | **3** | 11 | 0 | 2 |

- **Hallazgo 1 — el umbral de volumen no separa implante de no-implante.** El cubo `fragmento` resulto ser
  **11 externos de 17**. Un electrodo o un cursor de cremallera es **pequeno**, asi que cae bajo 200 mm3 igual
  que un fragmento de tornillo. **Volumen y "es implante" son ejes distintos**: la propuesta de 200 mm3 estaba
  mal planteada, no mal calibrada. Queda descartada como criterio primario.
- **Hallazgo 2 — el criterio de FORMA si discrimina.** De 6 propuestos `tornillo`, **4** lo eran; de los 5
  tornillos que marco la autora, el filtro cazo **4**. Precision 4/6, recall 4/5, sobre numeros chicos. El
  `largo >= 30 mm` y `ancho <= 12 mm` por **PCA** se conserva.
- **Hallazgo 3 — confirma #105 por via independiente.** **16 de 40 (40%) son `externo`** y 1 es `diu`. #105 lo
  dedujo de `revision.csv` a nivel de caso; esta revision lo confirma **componente a componente**.
- **SALVEDAD que hay que citar siempre con estas cifras:** la muestra esta **estratificada por volumen**, con
  sobremuestreo deliberado de 100-500 mm3. **NO es aleatoria**, asi que **no se puede extrapolar** el 40% de
  externos ni ninguna otra proporcion a los 363 componentes. Para una tasa poblacional haria falta una muestra
  aleatoria aparte.
- **Criterio nuevo que sugieren los datos:** un test **espacial** (¿el componente esta dentro del cuerpo?),
  calculable con la misma superficie de 300 HU que ya dibujan los HTML de A4. Habria atrapado los 16 externos
  de golpe, es geometrico, auditable y no depende de nada externo.
- **Regla ya fijada que aqui aplica:** si se recalibra el criterio, se vuelve a medir **sobre esta misma
  muestra**, no sobre una nueva.
- **Sigue ABIERTA:** falta implementar el criterio revisado, remedir el acuerdo y preinscribir la politica.

### 109 — Usar un segmentador de implantes ya publicado en vez de un criterio propio: evaluado y NO recomendado — ABIERTA (decidida en recomendacion; liga con #104, #105, C1)

- **Pregunta de la autora (2026-09-21):** si convendria apoyarse en un repositorio que ya haga la
  identificacion de implantes, en vez de proponer criterios propios, y si el problema seria que no sean
  especificos de pelvis.
- **Razon 1 — no ahorra el trabajo, lo mueve.** Cualquier segmentador externo habria que **validarlo en esta
  cohorte**, es decir revisar laminas exactamente como se acaba de hacer. La planilla seguiria siendo necesaria.
- **Razon 2 — el unico candidato disponible no resuelve el problema.** `xie2024implantsegmentation` (DiffSeg)
  segmenta metal **2D por corte**, su unico ground truth es **sintetico** (*"Metal implants were inserted into
  clean CT images"*, Method, p. 3) y en CT clinica *"Due to the lack of a corresponding ground truth"*
  (Results, p. 6) la comparacion es solo visual. Ademas separa **metal de no-metal**, no **implante de
  electrodo**, que es el problema real segun la revision de #104. Detectar metal ya esta resuelto: el umbral de
  2500 HU da 0 falsos negativos (E1).
- **Razon 3 — tension con C1.** `main.tex` reclama *"non-biological rigid implant geometries, which avoid the
  threshold-dependent size distortion of fixed-HU metal segmentation"* y **cita a Xie** para sostenerlo. Adoptar
  un segmentador aprendido como pieza central obliga a explicar por que se depende de aquello de lo que se dice
  escapar. No es contradiccion fatal (son usos distintos), pero es una objecion previsible.
- **Sobre la sospecha de la autora (que no sean de pelvis):** es real pero **no es el problema principal**. Pesa
  mas que la referencia de DiffSeg sea sintetica y que no distinga tipos de objeto, que el que no sea pelvico.
- **Marco conceptual que conviene fijar:** un **criterio de inclusion** para armar el conjunto de entrenamiento
  **no es una contribucion** que haya que defender como novedad. Se le exige ser **preinscrito y reproducible**,
  no original. Esto responde la preocupacion de fondo de la autora ("proponer metricas nosotros").
- **Recomendacion del asistente:** criterio propio, geometrico y declarado, con cuatro reglas: (1) test
  espacial dentro/fuera del cuerpo; (2) forma por PCA (validada en #104); (3) volumen como criterio
  **secundario**; (4) exclusion de los 29 casos sin material ortopedico via `revision.csv` (#105). Se mide el
  acuerdo sobre las **mismas** 40 laminas ya revisadas.
- **No aplicado** (regla 14). **Tipo:** METODO / dependencias externas. **Nivel propuesto: N1.**

### 104/109 — CORRECCION (2026-09-21): el umbral de 300 HU NO delimita el cuerpo, y el criterio espacial propuesto estaba roto de origen

- **Origen:** la autora, mirando los HTML de A4: *"el criterio de los 300 HU para detectar piel no funciono, no
  esta saliendo la piel... solo los metales en realidad"*.
- **El error:** `a4_html_componentes.py` dibujaba una isosuperficie a **300 HU** y la rotulaba "silueta del
  paciente". **300 HU es hueso**, no piel: el tejido blando esta entre -100 y +60 HU y el borde aire/tejido
  ronda los **-400 HU**. El umbral se copio de `exploration-3d/explorar.py`, donde estaba puesto para
  superficies densas, sin comprobar que representaba.
- **Medido en `dataset7_CLINIC_metal_0004_data`:** HU > **-400** da el **29.7%** del volumen (el paciente);
  HU > 300 da el **1.3%** (hueso y metal); HU > 1500, el 0.1% (metal). Entre -600 y -200 la fraccion apenas
  cambia: **-400 cae en una meseta**, asi que no es un valor delicado.
- **Por que no es solo cosmetico:** ese mismo umbral es el que se propuso en #104 y #109 como **criterio
  espacial** (dentro/fuera del cuerpo) para sustituir al de volumen, que es el que habria atrapado los 16
  componentes `externo`. Implementado con 300 HU, **el criterio habria estado roto desde el principio** y el
  fallo habria sido invisible en una tabla, a diferencia de en un HTML. La deteccion la hizo la autora mirando.
- **Corregido:** `mascara_cuerpo()` construye el cuerpo como tejido > **-400 HU**, **componente conexo mayor**
  (descarta mesa, tubos y ruido) y **huecos rellenos** (el aire intestinal no abre agujeros). Verificado en el
  caso de prueba: **28.5%** del volumen y **99.9%** del metal del paciente queda dentro.
- **Ademas:** el hueso de referencia baja de 1500 a **150 HU**, el mismo umbral que usa el resto de la tesis
  (`BONE_HU` de `e6c_techo_lw`), para que se vea el hueso completo y no solo cortical muy densa.
- **Las etiquetas de la leyenda traen ahora el veredicto de la autora**, asi que el HTML sirve tambien para
  revisar lo ya decidido.
- **Lo que NO cambia:** ninguna cifra publicada. `a1b`, `e11` y la planilla no usan este umbral. El criterio
  espacial **todavia no esta implementado** como filtro: cuando se implemente, usara `mascara_cuerpo()`.

### 104/109 — CORRECCION DE LA CORRECCION (2026-09-21): la causa NO era el valor del umbral, era que el umbral nunca se pasaba

- **Rectifica la entrada anterior de este mismo dia.** Ahi se atribuyo el fallo a que 300 HU delimita hueso y no
  piel. **Eso es cierto como hecho pero NO era la causa**, y dejarlo escrito asi habria mandado a cualquiera a
  buscar en el sitio equivocado.
- **Causa real:** `superficie()` llamaba a `marching_cubes(dato, level=None, ...)` para los arrays de HU.
  Sin `level`, `marching_cubes` usa **`(max + min) / 2`**. En estos CT: `(18283 + (-3820)) / 2 =` **7 231 HU**.
  Las capas rotuladas "piel" y "hueso" dibujaban en realidad **metal**. Por eso la autora describio ver
  *"solo los metales... y algunas partes internas a esos mismos metales"*: era una descripcion exacta.
- **Prueba medida, no visual:** decodificando los arrays binarios del HTML, la capa de hueso tenia **367**
  vertices; con el nivel pasado correctamente tiene **89 513**. La capa de cuerpo siempre funciono (40 316)
  porque es una mascara **booleana** y para booleanas si se pasaba `level=0.5`.
- **Corregido:** `nivel` es **obligatorio** para arrays de HU y el script **lanza** si falta, en vez de dibujar
  algo silenciosamente equivocado. Se anade ademas una comprobacion de rango. Hueso fijado en **300 HU**, el
  mismo de `exploration-3d/explorar.py`, por peticion de la autora, para que las dos vistas sean comparables.
- **Patron, tercera vez en esta sesion:** fallo en silencio + explicacion dada sin medir. Las otras dos: #107
  (caracterizar una cita sin verificarla contra la ficha) y el eje sagital de las laminas. En los tres casos lo
  detecto la autora mirando la salida, no un control. **Leccion operativa: toda capa o metrica derivada necesita
  una comprobacion que pueda fallar**; aqui la comprobacion util resulto ser contar vertices, no mirar la figura.
- **Lo que NO cambia:** ninguna cifra publicada. Afecta solo a la herramienta de visualizacion A4. El criterio
  espacial de #104/#109 sigue sin implementarse; cuando se implemente usara `mascara_cuerpo()`, que es booleana
  y nunca estuvo afectada por este fallo.

### 110 — La categoria `externo` mezcla dos cosas distintas: accesorios (13) y componentes de FIJADOR EXTERNO (3), y su exclusion necesita justificaciones separadas — ABIERTA (liga con #104, #105, #109)

- **Origen:** la autora pregunto si `CLINIC_metal_0044` y `CLINIC_metal_0013` eran el mismo CT, por lo parecidos
  que se ven (2026-09-21).
- **Respuesta a la pregunta, verificada:** **no son el mismo volumen ni el mismo paciente.** `metal_0044` es
  `Grupo paciente` **P143**, SHA256 `c623c237...`, spacing 0.866 mm; `metal_0013` es **P116**, SHA256
  `3b82dc1a...`, spacing 0.746 mm. El sistema de duplicados **si funciono**: `metal_0013` esta agrupado con
  `metal_0043` (mismo SHA256, mismo P116). **La regla de aislamiento no esta comprometida.**
- **Por que se parecen:** los dos llevan **fijador externo pelvico**. Las notas de `revision.csv` describen en
  ambos "bloques externos", "vastagos rectilineos entrando en las crestas iliacas" y "montaje bilateral". Es el
  mismo tipo de dispositivo en pacientes distintos. Detalle consistente con herraje de catalogo: los dos
  componentes muestreados de esos casos miden **largo 46.7 mm** por PCA.
- **Hallazgo que abre esta entrada:** de los **16** componentes que la autora marco `externo`, **13** vienen de
  casos **sin** material ortopedico (accesorios, electrodos, cremalleras, botones) y **3** vienen de casos
  **con** material ortopedico: son piezas de **fijador externo**. No son lo mismo:
  - un accesorio o electrodo **no es material quirurgico**: es ruido y se descarta sin mas;
  - un fijador externo **si es material quirurgico deliberado**, produce artefacto real y su apariencia es
    senal legitima; se descarta porque su **geometria no se parece a un tornillo** y esta **fuera del hueso**,
    no porque sea espurio.
- **Consecuencia para el criterio de #109:** la regla "dentro del cuerpo" excluye a los dos, lo cual es correcto
  para sintetizar tornillos iliosacros, pero **la justificacion escrita debe separarlos**. Si no, el documento
  dira que se descarto material quirurgico real por "no estar dentro del cuerpo" sin explicar que ademas su
  geometria es ajena al objeto de sintesis.
- **Consecuencia para la planilla:** conviene una columna de **procedencia** (el `Tipo de estructura observada`
  de `revision.csv`) que permita separar `externo`-accesorio de `externo`-fijador **sin** que nadie tenga que
  reinterpretar los veredictos ya escritos. Es dato, no juicio.
- **Estado de la revision al 2026-09-21:** 40/40 veredictos llenos; acuerdo exacto con `propuesta_auto`
  **16/40 = 40%**; distribucion: externo 16, otro implante 9, fragmento 8, tornillo 5, diu 1, dudoso 1.
- **No aplicado** (regla 14). **Tipo:** DATOS / taxonomia de exclusion. **Nivel propuesto: N2.**

### 106 (duplicada) — RETIRADA el 2026-09-21 por orden de la autora

- **Que habia aqui:** una segunda entrada #106, escrita por el asistente, que declaraba la implicancia
  **CERRADA** al comprobar que las cuatro fuentes del metodo ya estaban en `refs.bib`.
- **Por que se retira y no se renumera:** sus afirmaciones centrales **ya estaban refutadas** por la #106
  vigente (mas arriba en este archivo), que la autora actualizo tras lectura profunda. En concreto:
  (a) el argumento de que un DiT exigiria atencion sobre 65 536 pixeles es **falso** —Peebles y Xie
  tokenizan **parches latentes**—; y (b) la afirmacion de que con pocos datos la U-Net gana por sesgo
  inductivo la **contradice An et al. 2025**, que a FLOPs equivalentes reporta brecha de PSNR menor para
  DiT. Renumerarla habria dejado en el archivo critico un texto con afirmaciones falsas, citable por error.
- **Causa del duplicado, que es lo que vale la pena conservar:** el asistente **no releyo la entrada #106
  existente antes de escribir**. Verifico `refs.bib`, vio las claves y apendo una entrada nueva con el mismo
  numero. Es el mismo modo de fallo de #107 y del `level=None` de `marching_cubes`: **afirmar sin verificar
  el estado actual del artefacto que se esta modificando**. Antes de escribir sobre una implicancia
  existente, hay que leerla.
- **Lo unico sustantivo que aportaba, y que ya consta en la #106 vigente:** el cierre bibliografico del
  2026-09-21 (DDPM, ADM, coseno y DDIM disponibles para citar).
- **Consecuencia para la redaccion:** la justificacion de la U-Net que vaya a Metodos es la de la #106
  vigente —**eleccion pragmatica y no comparada**, con la integracion declarada como propia y pendiente de
  evaluacion—, **no** el argumento del sesgo inductivo con pocos datos.

### 110 — ACTUALIZACION (2026-09-21): la anotacion de `revision.csv` es de CASO y solo vale en una direccion; verificado contra los 40 veredictos

- **Objecion de la autora:** al distinguir por componente, `tipo_caso_revision` "no es del todo cierta". **Es
  correcta**, y la asimetria quedo medida.
- **Verificacion contra los 40 veredictos de la autora:**

| | Veredictos observados |
|---|---|
| `CASO_tiene_ortopedico = no` (13 comp.) | **externo 13, y nada mas** |
| `CASO_tiene_ortopedico = si` (27 comp.) | otro implante 9, fragmento 8, tornillo 5, **externo 3**, diu 1, dudoso 1 |

- **Contradicciones en la direccion fuerte: 0.** Ningun componente de un caso sin material ortopedico fue
  juzgado implante.
- **Regla de uso, asimetrica y por logica (no por correlacion):**
  - **`no` CONCLUYE a nivel de componente:** si el caso no tiene material ortopedico, **ningun** componente suyo
    puede ser un implante. La implicacion baja de caso a componente sin perdida. Sirve para **excluir el caso
    entero** y ya cubre 13 de los 16 `externo`.
  - **`si` NO CONCLUYE nada del componente:** que el paciente lleve osteosintesis no implica que *este* objeto
    lo sea. Prueba: 4 componentes en casos con ortopedico resultaron `externo` (3 piezas de fijador, en
    `metal_0027` y `metal_0045`) o `diu` (`metal_0062`). Ahi decide la **geometria**.
- **Encaje con el criterio de #109:** la regla 4 (excluir casos sin ortopedico) usa **solo** la direccion
  valida; las reglas 1 (dentro del cuerpo) y 2 (forma por PCA) hacen el trabajo dentro de los casos que si
  tienen material.
- **Salvedad a declarar:** en `dataset7` el valor "material ortopedico" proviene de una **regla de la autora**
  ("fila en blanco en dataset7 = hay material ortopedico"), no de inspeccion objeto por objeto. No afecta a la
  direccion `no`, porque esos 13 componentes estan en casos `dataset6` con tipo explicito (electrodo, zipper,
  DIU), pero si limita cualquier uso de la direccion `si`.
- **Columnas renombradas** a `CASO_tipo_revision` y `CASO_tiene_ortopedico`: el prefijo avisa de que el ambito es
  el caso y no el componente. Verificado que ningun veredicto cambio.

### 109 — REEVALUACION (2026-09-21): el criterio de FORMA y el umbral de VOLUMEN quedan descartados como filtros de entrenamiento; el criterio correcto es "¿este ejemplo ensena algo que en sintesis sera falso?"

- **Origen:** la autora pidio reevaluar si las cuatro reglas propuestas eran la direccion correcta. Al hacerlo,
  el asistente **descarta dos de sus propias recomendaciones**.
- **Error de planteamiento:** las reglas de forma (PCA tipo tornillo) y de volumen (>= 200 mm3) optimizaban para
  *"se parece a un tornillo"*. Pero el renderizador no aprende tornillos: aprende **la relacion entre una
  mascara de metal y el artefacto que produce**, que es fisica (atenuacion y geometria) y **no depende de si el
  objeto es tornillo, placa o fragmento**. Filtrar por forma tira datos que ensenan justo lo que se quiere
  aprender: en la muestra revisada solo **5 de 40** componentes son tornillos.
- **Ademas, la forma no arregla #95.** La brecha entre mascara real umbralizada y mascara parametrica no se
  cierra descartando componentes: el modelo condiciona en la mascara que se le da. Corresponde **declarar y
  reportar** la distribucion de formas y tamanos, no tirar datos.
- **Criterio correcto, que sustituye al anterior:** no *"¿esto es un tornillo?"* sino **"¿este ejemplo ensena
  algo que en sintesis sera falso?"**. Aplicado:

| Exclusion candidata | ¿Ensena algo falso? | Decision |
|---|---|---|
| Metal **fuera del cuerpo** | Si: contexto aire/piel, cuando en sintesis el tornillo va en hueso | **Excluir** |
| Parches **sin metal** (42.5%, #104) | Si: ensena "rellenar banda vacia"; en sintesis toda `G` tiene metal | **Excluir o acotar** |
| Casos **sin material ortopedico** (#105) | Si: no hay nada que aprender | **Excluir** |
| **Fragmentos** | No: metal real en hueso con artefacto real | **Conservar y reportar** |
| **Placas y protesis** | No: artefacto real; amplian el rango mascara -> artefacto | **Conservar y reportar** |

- **Reglas revisadas:** **R1** dentro del cuerpo; **R2** excluir casos sin material ortopedico (direccion `no`,
  validada en #110); **R3** el parche debe contener metal del componente objetivo, con proporcion declarada de
  parches de solo banda (no cero: la banda mas alla de la punta es real); **R4** tamano y forma como variables
  de **ESTRATIFICACION Y REPORTE**, no de exclusion.
- **Medido sobre los 21 754 parches de entrenamiento de A1b:**

| Criterio | Parches | Componentes | Casos |
|---|---|---|---|
| R2 sola | 17 170 | 241 | 47 |
| **R2 + R3** | **10 586** | **241** | **47** |
| R2 + R3 + volumen >= 200 mm3 | 10 160 | 172 | 47 |
| R2 + R3 + sin metal ajeno | 6 478 | 162 | 47 |

- **El dato que cierra el caso del umbral de volumen:** quita solo el **4%** de los parches pero elimina
  **69 componentes (29%)**. Descarta variedad de formas sin ganar tamano de conjunto. **Queda descartado.**
- **La forma por PCA vuelve a su proposito legitimo:** fue el filtro de **E11** para *medir* el diametro del
  tornillo, y ahi sigue siendo valido. No es un filtro de entrenamiento.
- **Direcciones alternativas evaluadas y descartadas, declaradas:** (a) **condicionar el modelo con descriptores
  del componente** (volumen, elongacion) en vez de filtrar — mas elegante, pero anade maquinaria y una via de
  fallo nueva a un modelo aun no entrenado, con el computo sin medir (#89); (b) **entrenar con todo y afinar
  luego sobre el subconjunto tipo tornillo** — duplica el gasto de GPU; queda como extension natural **si** el
  piloto sale barato.
- **Recomendacion final del asistente:** **R2 + R3** como exclusiones (10 586 parches, 241 componentes, 47
  casos), **R1** como refinamiento dentro de eso, **R4** solo como reporte.
- **No aplicado** (regla 14). **Tipo:** METODO / composicion del conjunto. **Nivel propuesto: N1.**

### 111 — La fragmentacion del umbral (E8: 9 de 57) se agrava con D2: un implante fisico puede dar VARIAS unidades de entrenamiento con mascara parcial — ABIERTA (agrava #95; liga con #46, #101, #102)

- **Origen:** observacion de la autora al terminar la revision (2026-09-21): *"hay metal que es ortopedico que no
  estamos considerando (tal vez por la forma)"*, y que reconoce piezas de tornillo etiquetadas como otro metal.
- **Evidencia previa del proyecto:** E8 midio que **a 2500 HU los tornillos salen fragmentados en 9 de 57**
  (#46), con `d_ext_semimax` de mediana 5.08 mm. Ya esta citado en `main.tex` dentro de C1.
- **Lo que cambia con D2, y no estaba declarado:** cuando la unidad era el **corte**, un tornillo partido seguia
  dentro de la misma `G` y el modelo veia la mascara completa aunque tuviera huecos. Con extraccion **por
  componente** (#102), **un tornillo fragmentado se vuelve varias unidades de entrenamiento**, cada una con
  mascara parcial. El modelo aprende "esta astilla produce este artefacto" cuando el artefacto lo produce el
  tornillo entero; en sintesis se coloca **un cilindro solido**. Es #95 **agravada por D2**.
- **Donde NO cuesta:** en el conjunto de entrenamiento. R1-R4 (#109 reevaluada) **no filtran por tipo ni forma**,
  asi que un fragmento entra igual. El error de etiqueta es la parte barata; la cara es la fragmentacion fisica
  de la mascara, que **no se arregla etiquetando mejor**.
- **Donde SI cuesta, y hay que declararlo:**
  1. **E11 esta sesgado.** Su filtro exige **largo >= 30 mm**; un tornillo partido en tres da piezas de ~20 mm
     que **quedan fuera de la medicion**. El `d_centro` de **4.91 mm** se midio sobre los tornillos que
     sobrevivieron **enteros** al umbral: esta sesgado hacia los mejor segmentados. **No invalida la cifra**
     (coincide con catalogo 4.8 mm y E8 5.00 mm por vias independientes), pero **la salvedad falta** en
     `e11_perfil_axial.md` y en #101.
  2. **Reportar la mezcla (R4).** Sin tipo anotado no se puede decir "N tornillos y M placas"; se reporta por
     **volumen y elongacion**, y se declara que el tipo no esta anotado, como ya hace `main.tex:111`.
- **Lo que NO se recomienda:** perseguir la clasificacion perfecta. Llevaria a segmentacion manual de los 363
  componentes, que es justo el trabajo que #109 concluyo que no corresponde.
- **Medicion propia pendiente, opcional y barata:** cuantos componentes se unirian con **semimaximo local**
  (propuesta abierta de #22/#46), para tener una cifra de fragmentacion **sobre esta cohorte** en vez de heredar
  el 9/57 de E8. **Aviso metodologico:** el asistente intento estimarlo con **cierre morfologico** y el metodo
  **NO sirve** — unia componentes en unos casos y los separaba en otros (hasta -67%). No usar esa via.
- **No aplicado** (regla 14). **Tipo:** DATOS / mascara de entrenamiento. **Nivel propuesto: N1.**

### 112 — La proporcion de parches "solo banda" NO se elige: se calcula del corredor medido, y da 1.40, no el 0.5 que propuso el asistente — ABIERTA (fija un parametro de R3, #109; liga con #104, #57)

- **Pregunta de la autora (2026-09-21):** si hay fuente para `--dentro-min 0.5` y `--ratio-banda 0.5`, o si son
  razonables con los datos propios.
- **Para `ratio-banda` no hace falta fuente ni eleccion: es geometria ya medida.** La proporcion correcta es la
  que tendra el **caso de sintesis**, y el eje del corredor esta en `experiments/objetivo2/e9ts_corredor.csv`
  (E9-TS). Para un cilindro de diametro `d` y largo `L` sobre el eje unitario `u`, su extension axial es
  `L*|u_z| + d*sqrt(1-u_z^2)`, y la banda anade `2*delta` con `delta = 12 mm`:

  `ratio = 2*delta / (L*|u_z| + d*sqrt(1-u_z^2))`

- **Medido sobre 908 corredores viables (`D_TS >= 10 mm`), con `d = 4.9 mm` (E11):**

| Magnitud | mediana | p10 | p90 |
|---|---|---|---|
| `|u_z|` (inclinacion fuera del plano axial) | **0.087** | 0.000 | 0.174 |
| Extension axial del cilindro (mm) | **17.1** | 4.9 | 30.0 |
| **Ratio banda-sola / con-metal** | **1.40** | 0.80 | 4.90 |

- **Robusto al diametro supuesto**, que es la magnitud con mas discusion en el proyecto (#97, #99, #101):
  ratio mediana **1.40** con 4.9 mm, 1.40 con 5.0, **1.23** con 7.3 y **1.19** con 8.0. La eleccion de geometria
  no lo mueve.
- **Interpretacion:** el tornillo transacro corre **casi en el plano axial** (`|u_z|` ~ 0.09), asi que aparece en
  pocos cortes axiales mientras `B_delta` anade 12 mm por cada extremo. Es el caso extremo de "poco metal por
  corte, mucha banda".
- **Dos correcciones que salen de aqui:**
  1. **El 0.5 propuesto por el asistente era casi tres veces demasiado bajo.** Queda **descartado**.
  2. **El conjunto de entrenamiento tambien se queda corto**: en A1b los parches sin metal dan ratio **0.74**,
     frente al **1.40** que producira la sintesis. Tiene sentido —placas y protesis tienen extension axial
     grande y diluyen—, pero es una **diferencia de distribucion entre entrenamiento y uso** que hay que
     declarar, y que R3 puede corregir deliberadamente al fijar el ratio.
- **Valor recomendado: `--ratio-banda 1.4`**, justificado con medicion propia sobre 908 corredores y con la
  sensibilidad al diametro declarada. **No requiere fuente externa.**
- **Para `--dentro-min` el argumento es OTRO y sigue pendiente:** no existe ni cabe esperar una fuente sobre
  "que fraccion de un implante debe estar dentro del cuerpo". El precedente correcto del proyecto es
  **justificar por invariancia**, como se hizo con `F = 0.001` (decision 2026-09-14 (5), justificada por la
  invarianza de `D_TS`). Si `frac_dentro` resulta **bimodal** (tornillo ~1.0, electrodo ~0.0), cualquier umbral
  entre 0.2 y 0.8 da el mismo resultado y el valor deja de ser una eleccion. **Si NO es bimodal, hay una
  decision real que tomar y se declarara como tal.** Se mide con `a5_acuerdo.csv`, en curso.
- **No aplicado** (regla 14). **Tipo:** METODO / parametro con justificacion propia. **Nivel propuesto: N1.**

### 112 — ACTUALIZACION (2026-09-21): el ratio 1.40 NO es alcanzable con los parches existentes; el maximo es 0.62

- **Medido tras R2 (casos con material ortopedico), particion train:** **10 586** parches con metal del
  componente y **6 584** de solo banda. **Ratio maximo alcanzable = 0.62.** Para 1.40 harian falta 14 820 de
  banda: **faltan 8 236**.
- **Es decir: el parametro justificado con medicion propia no se puede cumplir con los datos extraidos.** Queda
  registrado asi, sin maquillarlo.
- **Opciones:**
  - **(a)** Usar **todos** los parches de banda disponibles (ratio **0.62**) y **declarar la brecha** frente al
    1.40 que producira la sintesis. Coste cero.
  - **(b)** **Extraer mas parches de banda** bajando `MIN_VOX_G` (hoy 50 voxeles de `G` para que un corte
    cuente), lo que admitiria cortes de banda fina en los extremos del implante. **Exige recorrer A1b otra vez**
    (~2 h de CPU, reanudable).
  - **(c)** Recortar parches con metal hasta alcanzar 1.40. **Descartada:** tirar ~6 000 parches buenos para
    igualar una proporcion repite el error del umbral de 200 mm3 (#109).
- **Recomendacion del asistente:** **(a) ahora**, y **(b) solo si el piloto muestra problema de costura en el
  borde de `B_delta`** (bloque E-A2 de `diseno_A.md`). La brecha 0.62 frente a 1.40 se declara como limitacion
  del conjunto, junto a la diferencia 0.74 (A1b crudo) ya registrada.
- **Nota de infraestructura, relevante para el plan:** cambiar `ratio-banda` o `dentro-min` **no exige reextraer
  nada**. El cache de A1b guarda todos los parches y el criterio se aplica al construir el `Dataset`, por
  diseno. Solo la opcion (b) obligaria a recorrer A1b.

### 109 — RESULTADO DE R1-R3 (2026-09-21): el criterio de inclusion acierta 36 de 39, con recall 100%, y `dentro-min` queda justificado por INVARIANCIA

- **Medido con `a5_criterio_inclusion.py` sobre las mismas 40 laminas ya revisadas** (regla fijada de antemano
  en #104: no se genera muestra nueva). 1 `dudoso` excluido del calculo, no forzado.

| | Criterio anterior (#104) | **R1 + R2** |
|---|---|---|
| Que mide | acierto de **tipo** | **incluir / excluir** |
| Acuerdo | 16/40 = **40%** | **36/39 = 92%** |
| Precision / recall | — | **88% / 100%** |

- **Recall 100%:** ningun componente que la autora juzgo implante fue excluido. Los 3 errores son falsos
  positivos, la direccion barata.
- **Las dos reglas se reparten el trabajo:** de los 14 aciertos de exclusion, **7 los caza R1** (fuera del
  cuerpo) y **7 los caza R2** (caso sin ortopedico). Ninguna es redundante.
- **`--dentro-min` NO necesita fuente ni eleccion: es invariante.** `frac_dentro` resulta **perfectamente
  bimodal** — vale **0.000 o 1.000, nunca un valor intermedio** (n=22 "debe entrar", todos 1.000; n=17 "debe
  salir", mediana 1.000 por los falsos positivos pero minimo 0.000). Barrido de **0.05 a 0.95**: exactitud
  **92% en todos los umbrales**, con TP/FP/TN/FN identicos. Es el mismo argumento con que el proyecto justifico
  **`F = 0.001`** (decision 2026-09-14 (5), invarianza de `D_TS`). **Queda cerrado sin fuente externa.**
- **Los 3 falsos positivos, identificados y explicables:** `metal_0045` comp 0 (162.2 mm3) y comp 1 (21.8 mm3),
  marcados `externo` por la autora pero **dentro del cuerpo** (previsiblemente los tornillos del fijador, que
  atraviesan piel y entran en hueso); y `metal_0062` comp 2 (267.6 mm3), **DIU**: interno y deliberado, pero no
  osteosintesis. **Ninguna regla geometrica los separa**: requieren criterio humano. Se declara.

### 112 — ACTUALIZACION (2026-09-21): la opcion (b) interactua con la normalizacion de la perdida, y hoy seria PERJUDICIAL

- **Pregunta de la autora:** si (b) —bajar `MIN_VOX_G` para extraer mas parches de solo banda— no seria mejor
  opcion.
- **Hallazgo no registrado hasta ahora.** `difusion.perdida()` normaliza **por imagen**:
  `err.sum(dim=(1,2,3)) / (n * canales)` con `n = |G|`, y luego promedia el lote. Es decir **cada parche pesa
  igual, sin importar el tamano de `G`** — puesto a proposito para que las protesis grandes no dominen (riesgo 3
  de `diseno_A.md`).
- **Consecuencia:** (b) admitiria miles de parches con `G` **menor de 50 voxeles** (< 0.08% de un parche de
  256x256), y **cada uno pesaria lo mismo que uno con un tornillo entero**. El gradiente lo dominarian parches
  casi sin informacion. **(b) no es solo mas lenta: hoy seria perjudicial.**
- **Recomendacion revisada:** **(a) ahora**. Si tras el piloto la **costura** en el borde de `B_delta` (salto de
  HU al cruzar el borde de `G`, metrica del bloque E-A2) resulta un problema, entonces **(b) junto con cambiar
  la normalizacion a peso proporcional a `|G|`** — una linea. Hacer (b) sin ese cambio es arreglar un
  desbalance creando otro.
- **Lo que esto anade al registro:** la composicion del conjunto y la funcion de perdida **no son decisiones
  independientes**. Cualquier cambio futuro en el ratio de banda debe revisar la normalizacion, y viceversa.

### 57 — ACTUALIZACION (2026-09-21): Selles 2023 y Park 2015 confirman artefacto fuera de `M`, pero ninguno calibra `B_delta`

- **Selles 2023** es evidencia clinica en la anatomia mas cercana disponible: compara HU en hueso y musculo
  ipsilateral y contralateral alrededor de implantes de fusion sacroiliaca. Esto refuerza que el efecto relevante
  no se limita a la mascara del metal. Sin embargo, sus ROI no se definen por distancia al implante y el paper no
  publica perfiles radiales, una distancia maxima ni un ancho de banda.
- **Park 2015** aporta el fundamento fisico-matematico: el beam hardening produce cupping dentro del objeto y
  streaking fuera de el, con dependencia de la geometria y disposicion de los objetos. Su modelo 2D tampoco
  define un radio finito ni una distancia en milimetros.
- **Consecuencia:** ambas fuentes respaldan la **direccion** de `G = M u B_delta`, pero **no justifican
  `delta = 12 mm`**. Ese valor conserva su estatus de construccion metodologica/hiperparametro local y debe
  validarse mediante la sensibilidad ya prevista. La medicion contralateral de Selles tampoco implica que una
  banda local capture todo el campo: `B_delta` es una delimitacion deliberada del objetivo, no la extension
  fisica total del artefacto.
- **Estado:** ABIERTA en cuanto al ancho; evidencia externa reforzada para la necesidad de salir de `M`.

### 113 — Zwingmann 2010 no puede entrar todavia al benchmark SAP: publica un grado 4 sin definir y puede solaparse con la cohorte 2009 — ABIERTA

- **Hallazgo primario:** Metodos define cuatro grados, `0`, `1`, `2` y `3`, pero la Tabla 1 publica cinco
  categorias. La distribucion navegada es **81/11/3/5%** para grados 0-3; la convencional es
  **42/22/21/13/2%** para grados 0-4. El paper no define el grado 4.
- **Segundo riesgo:** es una cohorte secuencial/historica del mismo grupo y no hay informacion suficiente para
  demostrar o descartar solapamiento con `zwingmann2009navigated`. Tratar ambas distribuciones como observaciones
  independientes podria duplicar pacientes.
- **Opciones:** (a) excluir Zwingmann 2010 del benchmark principal; (b) obtener de los autores la definicion del
  grado 4 y la relacion entre cohortes; (c) hacer una sensibilidad que agrupe el grado 4 con `>4 mm`, dejando
  claro que esa agrupacion es una suposicion externa y no una definicion del paper.
- **Recomendacion:** **(a)**. Conservar la fuente como evidencia descriptiva y no modificar el prior SAP hasta
  resolver ambas ambiguedades. **Tipo:** BENCHMARK / validez de la distribucion ordinal. **Nivel: N1.**

## Ronda 2026-09-21 (cierre) — ENCARGO PARA EL SIGUIENTE AGENTE

Escrito para una sesion nueva sin historial. Leer tambien `docs/ESTADO.md` (regla 11) y la entrada
**2026-09-21** de `01-decisiones.md`, que congela el conjunto de entrenamiento.

### Tarea 1 — Analizar el piloto de Khipu (job 52074)

Es lo primero. Salidas en `~/metalsynth/data/a2/<etiqueta>/`: `curva.csv`, `entrenar_meta.json`, `ckpt.pt`.
Comandos de bajada en `KHIPU.md`, seccion **A2**.

- **CONTROL QUE PUEDE FALLAR, mirarlo antes que nada:** el log debe decir **`parches: 17149`** y
  **`casos: 47`**. Si dice 21 754 / 72, **el manifiesto no se aplico** y esa corrida **no** es la
  preinscrita: hay que relanzarla, no reinterpretarla.
- Los tres controles deben aparecer antes del paso 1: identidad de ventanas (1.27e-11 HU), aislamiento
  (0 de 34 casos de test) y perdida solo en `G` (G vacia -> 0.0).
- Debe aparecer el aviso **`corrida NO preinscrita`**: es piloto de medicion, no resultado de tesis.
- **Que se extrae:** `s_por_paso` del **ultimo** tramo de `curva.csv` (los primeros pasos incluyen carga)
  y `gb_max`. Presupuesto = `s_por_paso x pasos / 3600`. **La perdida de 200 pasos no significa nada.**
- **Con eso se cierra #89**, que es el encargo pendiente del asesor. Si `gb_max` pasa de ~40 GB o la
  extrapolacion da mas de ~20 h por corrida, la respuesta correcta **no** es lanzarla igual: es bajar
  `--base` o `--lote` y dejar escrito por que.

### Tarea 2 — Leer las fichas nuevas y medir su impacto (regla 13)

Hay **14 fichas nuevas sin procesar** en `docs/literatura/`, subidas por la autora. **No releer los PDF**
(regla 10: toda lectura va por `lector-papers`); aqui basta con leer las fichas y evaluar impacto:

| Ficha | Por que importa |
|---|---|
| `lugmayr2022repaint` | **Prioridad 1.** RePaint es inpainting con difusion: es el metodo del Diseno A. Puede ser mejor referente que CLAIM o LeFusion, y puede aportar tecnica de muestreo (resampling) que hoy no se usa |
| `zhang2025lefusion` | Sintesis controlada por mascara enfocada en lesion; candidata a referente principal |
| `ho2020denoising`, `dhariwal2021diffusion`, `nichol2021improved`, `song2021ddim` | Las cuatro piezas que `src/renderizador/` implementa. Hay que **citarlas en Metodos** |
| `peebles2023scalablediffusion`, `an2025generalization`, `liu2021efficienttraining` | Sostienen el argumento U-Net frente a DiT (#106, #109), que hasta ahora era razonamiento sin fuente |
| `ronnenberger2015unet` | U-Net original |
| `yeap2025fewshots` | DDPM para CT sintetica con pocos datos: pertinente al regimen de esta tesis |
| `choi2025mar`, `selles2023ai`, `park2015ct`, `zwingmann2010percutaneous` | Sin evaluar por este asistente |

**Para cada una:** ¿obliga a ajustar redaccion, alcance, un supuesto, un baseline, o abre un gap? Si si,
entrada nueva aqui; si no, decirlo explicitamente en el chat (regla 13).

### Tarea 3 — Resolver la contradiccion de #106

**Hay DOS entradas #106 incompatibles**: una ABIERTA escrita por la autora (*"las cuatro fuentes ya son
citables, pero su combinacion exacta no fue validada y no hay evidencia de superioridad frente a DiT"*) y
una CERRADA escrita por el asistente. **La de la autora plantea un estandar mas alto y deberia prevalecer.**
Decidir cual queda, renumerar la otra, y dejar el archivo sin contradiccion. Es el archivo critico
irreemplazable (regla 17).

### Estado de `main.tex` al cierre

**Editado el 2026-09-21 por orden explicita de la autora.** Compila **0 errores, 0 citas indefinidas,
7 paginas, 110 referencias**. Cambios:
- **#107 APLICADA:** *"an image-domain diffusion model"* -> *"a sinogram-domain diffusion model evaluated
  in image space"* para `karageorgos2024ddpm`. Era un error factual: su DDPM opera en sinograma.
- **Objetivo 3 puesto al dia** con lo decidido el 2026-09-21: unidad de entrenamiento = **componente**, no
  corte; criterio de inclusion fijado antes de entrenar; tamano y forma **se reportan, no filtran**.
- **De dos desplazamientos de dominio declarados se pasa a TRES**: se anade el de la proporcion de parches
  de solo banda (0.62 extraido frente a 1.40 que predice la geometria del corredor, #112).

**Lo que `main.tex` todavia NO dice, y alguien tiene que escribir:**
- La **arquitectura** (U-Net tipo DDPM/ADM, planificador coseno, muestreo DDIM, ~28 M parametros) y su
  atribucion a las cuatro fuentes nuevas. Es la seccion de Metodos, y ya no hay excusa bibliografica.
- Que la eleccion de U-Net **no se comparo** con alternativas: limitacion a declarar (#106, #109).
- **#108 sin aplicar:** la Tabla III de `karageorgos2024ddpm` respalda la direccion de `B_delta`
  (mascara ensanchada RMSE ~11.5; reducida 54.8 y 57.7). Es el apoyo mas fuerte disponible para la
  decision con menos respaldo externo del diseno.

### Implicancias ABIERTAS que bloquean, por gravedad

1. **#105** — **2 de los 5 casos de validacion no tienen ningun implante**. Validacion es donde D4 manda
   medir el margen `Delta`. **Bloquea la evaluacion**, y rehacer la particion toca la *Strict Isolation
   Rule* (`main.tex:111`) y la semilla 20260917 de P1.
2. **#111** — la fragmentacion del umbral se agrava con la unidad por componente; el sesgo de E11 ya esta
   declarado en `e11_perfil_axial.md`, falta decidir si se mide.
3. **#112** — si el piloto muestra problema de **costura** en el borde de `B_delta`, la opcion de extraer
   mas parches de banda **exige ademas** cambiar la normalizacion de la perdida a peso proporcional a
   `|G|`. Las dos cosas juntas o ninguna.
4. **#108**, **#106** (contradiccion), y la evaluacion **E-A1..E-A4**, que **sigue sin una sola linea de
   codigo**.

### 105 — REEVALUACION Y APLICACION (2026-09-21): no hacia falta rehacer la particion; bastaba aplicar R2 tambien a validacion

- **La recomendacion anterior del asistente era desproporcionada y partia de un dato incompleto.** Decia
  "rehacer la particion de validacion", lo que tocaba la *Strict Isolation Rule* (`main.tex:111`) y la semilla
  20260917 de P1 —la misma sobre la que descansa el resultado No-Go del Objetivo 1 (#91)—. **Nada de eso era
  necesario.**
- **Dato que faltaba:** la particion `val` tiene **8 casos**, no 5. Los 5 eran los que tienen metal, que es lo
  unico que A1b procesa. Desglose real:

| Casos | Cuales | Para que sirven |
|---|---|---|
| **3 con material ortopedico** | `metal_0011`, `metal_0039`, `metal_0056` | validacion de reconstruccion |
| **2 con metal NO ortopedico** | `CLINIC_0019` (accesorio), `CLINIC_0102` (cremallera) | **nada**: no hay implante que generar |
| **3 sin metal** | `CLINIC_0046`, `CLINIC_0066`, `CLINIC_0101` | analogo de sintesis (E-A2): paciente limpio |

- **Los 3 sin metal NO son un problema**, al contrario: son exactamente el caso de uso de sintesis. El problema
  se reduce a **2 casos**.
- **Solucion aplicada: aplicar R2 tambien a `val`.** No es una decision nueva —es aplicar con consistencia el
  criterio ya preinscrito el 2026-09-21—, y **no toca la particion, ni la semilla, ni test**. Ventaja decisiva
  frente a re-particionar: **cero seleccion post hoc**, porque no se elige que casos entran, solo se aplica una
  regla escrita de antemano.
- **Resultado medido:** `val` pasa de 1 304 a **896 parches** (553 con metal, 343 banda) en **3 casos con
  implante real**, de los 5 con metal. Manifiesto versionado: `experiments/objetivo3/a5_manifiesto_val.csv`.
  `a5_criterio_inclusion.py` genera ahora los dos manifiestos con el mismo codigo.
- **Limitacion que hay que declarar, y es real:** el margen `Delta` de D4 se medira sobre **3 pacientes**. Es
  poco. Mitiga en parte que `Delta` mide variabilidad **intra-metodo** (semillas DDIM sobre el mismo caso, mas
  test-retest del brazo fisico), asi que el n efectivo es 3 casos x k semillas y no 3 observaciones. **Aun asi
  es fino, y el informe debe decirlo**, no presentar un `Delta` de 3 pacientes como si fuera robusto.
- **Alternativa descartada y por que:** mover casos de `train` a `val` para volver a 5 mantendria la isolation
  rule (no repite paciente entre particiones) pero **obliga a elegir cuales**, y elegir despues de ver los
  datos es seleccion post hoc. No compensa por dos pacientes.
- **Estado: RESUELTA en lo que bloqueaba.** Queda abierta la declaracion de la limitacion de n = 3 en el
  documento, que es de redaccion y no de metodo.

## Ronda 2026-09-21 (cierre 2) — ENCARGO ACTUALIZADO PARA EL SIGUIENTE AGENTE

**Sustituye al encargo anterior de esta misma fecha.** Leer antes `docs/ESTADO.md` (regla 11) y las dos
entradas **2026-09-21** de `01-decisiones.md`.

### Cambios desde el encargo anterior

- **#105 RESUELTA.** No hizo falta rehacer la particion: basto aplicar **R2 tambien a `val`**. `val` queda en
  **896 parches / 3 casos con implante real**; manifiesto `a5_manifiesto_val.csv`. **`Delta` se medira sobre
  n = 3 pacientes**, limitacion a declarar. Ya **no bloquea** la evaluacion.
- **La contradiccion de #106 esta resuelta:** la entrada duplicada del asistente fue retirada y sustituida por
  una nota de trazabilidad. **La #106 vigente es la de la autora** y sigue ABIERTA.
- **`main.tex:98` actualizado:** el criterio de exito deja de ser *"statistically comparable"* a secas y pasa a
  declarar endpoint primario unico (streak amplitude), **Wilcoxon** de una cola para superioridad, **TOST**
  para equivalencia con margen fijado de antemano y medido solo en validacion, y que **un resultado
  no concluyente es reportable**. Es D4 llevado al documento.

### Tarea 1 — Analizar el piloto (job 52074). Sigue siendo lo primero

Sin cambios respecto al encargo anterior: control **`parches: 17149`, `casos: 47`** antes que nada; si sale
21 754 / 72 el manifiesto no se aplico y hay que relanzar. De `curva.csv`, `s_por_paso` del **ultimo** tramo y
`gb_max`. **Con eso se cierra #89.**

### Tarea 2 — Las 15 fichas nuevas, sin procesar (regla 13)

`an2025generalization`, `choi2025mar`, `dhariwal2021diffusion`, `ho2020denoising`, `liu2021efficienttraining`,
**`lugmayr2022repaint`**, `nichol2021improved`, `park2015ct`, `peebles2023scalablediffusion`,
`ronnenberger2015unet`, `selles2023ai`, `song2021ddim`, `yeap2025fewshots`, `zhang2025lefusion`,
`zwingmann2010percutaneous`.

**No releer los PDF** (regla 10). Prioridad 1: **`lugmayr2022repaint`** — RePaint es inpainting con difusion,
es decir el metodo de esta tesis, y puede aportar tecnica de muestreo (resampling) que hoy no se usa.
`zwingmann2010percutaneous` ya genero **#113**. Las demas: evaluar impacto y registrar o declarar "sin
implicancias" en el chat.

### Tarea 3 — Codigo que falta, por orden

1. **Bucle de validacion en `entrenar.py`.** `a5_manifiesto_val.csv` existe pero **nada lo consume**: hoy el
   script solo carga `train`. Sin esto, `val` no sirve para nada.
2. **Evaluacion E-A1..E-A4**, que sigue **sin una sola linea**.
3. **Metodos en `main.tex`:** la arquitectura (U-Net tipo DDPM/ADM, coseno, DDIM, ~28 M parametros) y su
   atribucion. **Usar la justificacion de la #106 vigente** —eleccion pragmatica y no comparada, integracion
   declarada como propia y pendiente de evaluacion— y **NO** el argumento del sesgo inductivo con pocos datos,
   que An et al. contradice.

### ABIERTAS que quedan, por gravedad

1. **#106** — la combinacion coseno T=1000 + DDIM lineal eta=0 con 50 pasos **no esta evaluada en ninguna
   fuente**, y Nichol--Dhariwal advierte que el stride de Song empeora combinado con coseno. Toca
   `src/renderizador/difusion.py`: declarar como integracion propia o ajustar a una combinacion con respaldo.
2. **#112** — si el piloto muestra **costura** en el borde de `B_delta`, extraer mas parches de banda **exige
   ademas** cambiar la normalizacion de la perdida a peso proporcional a `|G|`. Las dos cosas juntas o ninguna.
3. **#111** — sesgo de fragmentacion de E11, ya declarado en `e11_perfil_axial.md`; falta decidir si se mide
   con semimaximo local.
4. **#108** — la Tabla III de `karageorgos2024ddpm` respalda la direccion de `B_delta` y **sigue sin aplicarse**
   a `main.tex`. Es el apoyo mas fuerte disponible para la decision con menos respaldo externo del diseno.
5. **#113** — Zwingmann 2010 y el grado 4 sin definir.

### Advertencia de metodo, ganada en esta sesion

Cuatro fallos silenciosos se detectaron **mirando la salida**, no con controles: el eje sagital de las laminas,
el `level=None` de `marching_cubes`, la caracterizacion erronea de una cita (#107) y una entrada duplicada por
no releer el archivo antes de escribir (#106). **Antes de afirmar algo sobre un artefacto, leer su estado
actual.** Y toda capa o metrica derivada necesita una comprobacion que pueda fallar: para las superficies 3D,
la util resulto ser **contar vertices**, no mirar la figura.

### 108 — APLICADA en `main.tex` (2026-09-21), por orden explicita de la autora

- **Donde:** parrafo del Objetivo 3, justo despues de declarar que el ancho de banda es un parametro de diseno
  sin extension publicada.
- **Que se anadio:** la Tabla III de `karageorgos2024ddpm` como **respaldo de direccion**, con sus cifras:
  dilatar la traza metalica deja el error practicamente igual (**RMSE 11.45 y 11.63 HU** con factores 1.4 y
  1.8), mientras que encogerla lo hace **colapsar** (**54.82 y 57.69 HU** con 0.7 y 0.5), frente a **7.57 HU**
  con la traza verdadera. El argumento que habilita: **quedarse corto cubriendo el metal es mucho mas danino
  que pasarse**, que es exactamente la razon para generar mas alla de la mascara del implante.
- **Salvedad escrita en el mismo texto, para que nadie la lea de mas:** ese experimento varia una **mascara**
  en reduccion de artefacto **en dominio sinograma**, no una **banda de generacion** en dominio imagen. Por
  eso **motiva la direccion de `B_delta` sin fijar su anchura**, y el valor de **12 mm sigue siendo una
  construccion declarada**.
- **Por que importaba:** `B_delta` era la decision de diseno con menos respaldo externo de toda la tesis. Con
  esto pasa de no tener ningun apoyo publicado a tener uno **direccional y honestamente acotado**.
- **Compilacion verificada:** 0 errores, **0 citas indefinidas**, 7 paginas, 110 referencias. `refs.bib` **sin
  tocar**: la clave ya estaba (regla 9).
- **Estado: CERRADA.**

### Correccion al encargo del siguiente agente (2026-09-21)

Dos puntos del encargo anterior **ya no aplican**:
- **#108 ya NO esta pendiente**: fue aplicada (arriba). Retirarla de la lista de ABIERTAS.
- **El aviso para quien escriba Metodos** (usar la justificacion de la #106 vigente y **no** el argumento del
  sesgo inductivo) **se movio a `docs/ESTADO.md`**, por orden de la autora, en la seccion *"AVISO para quien
  escriba Metodos"*. Es el sitio correcto: `ESTADO.md` es lo primero que se lee al arrancar (regla 11).

---

## Ronda 2026-09-21 (cierre 3) — resultado del piloto A2 (job 52074)

Primer entrenamiento del proyecto. Salidas en `experiments/objetivo3/outputs/a2/`:
`a2_entrenar_52074.log` y `pasos200_20260921_074236/{curva.csv, entrenar_meta.json, ckpt.pt}`.
Corrida **VALIDA**: los cuatro controles pasan y el conjunto es el preinscrito.

### 89 — ACTUALIZACION (2026-09-21): el presupuesto de computo ya esta MEDIDO; queda listo para cerrar

- **Control de identidad de la corrida, superado:** `datos: {'parches': 17149.0, 'casos': 47.0,
  'series': 339.0, 'borde': 480.0, 'frac_borde': 0.028}`. Es exactamente el conjunto congelado por la
  decision del 2026-09-21 (R1-R3). **No** salio 21 754 / 72, asi que el manifiesto si se aplico.
- **Los tres controles internos pasan:** `identidad_ventanas: peor 9.09e-12 HU`, `aislamiento: 0 de 34
  casos de test en el cargador`, `perdida_solo_en_G: G vacia -> 0.0`. Aparece el aviso `corrida NO
  preinscrita`, como debia. `entrenar_meta.json` confirma `"preinscrito": false`. `rc=0`.
  - **Nota para no leer mal un control:** el encargo anterior citaba `1.27e-11 HU` para identidad de
    ventanas y esta corrida dio `9.09e-12 HU`. **No es una discrepancia:** el control comprueba que el
    ida-y-vuelta de ventanas es identidad a precision de maquina, y ambos valores son del orden de
    1e-11 HU. La cifra del encargo venia de la prueba local; no es un valor esperado fijo.
- **Cifra medida para el presupuesto: `0.0923 s/paso` en regimen.** Ver #114 para por que **no** es la
  cifra que imprime el script. Configuracion: `lote 4`, `lado 256`, `base 64`, objetivo `v`,
  **27 979 587 parametros (28.0 M)**, RTX A6000 de 49 140 MiB, nodo `ds001`, `torch 2.14.0+cu130`.
- **Presupuesto resultante:** **0.77 h por 30 000 pasos**; 1.28 h por 50 000; 2.56 h por 100 000.
  Los 200 pasos tomaron 49 s de reloj (07:43:29 a 07:44:18).
- **Memoria: `gb_max = 3.35 GB`** de los 48 GB de la A6000. Ver #115.
- **Contra los umbrales preinscritos en `KHIPU.md`:** el criterio era relanzar con `--base`/`--lote`
  menores si `gb_max` pasaba de ~40 GB o la extrapolacion daba mas de ~20 h. **Ninguno se acerca:** la
  memoria usa el 7% del techo y el tiempo, el 4% del tope. **No hay que bajar nada.**
- **Consecuencia para la entrega al asesor:** el gap que declaraba #89 —"el tiempo de entrenamiento no
  esta medido", entregado como procedimiento sin cifra— **queda cubierto**. Y confirma que descartar el
  borrador de ~140 GPU-h fue correcto: el orden real del entrenamiento del renderizador es **~1 h**, no
  decenas. La diferencia son **mas de dos ordenes de magnitud**.
- **Alcance de la cifra, para no sobrevenderla:** mide **el renderizador del Diseno A a esta
  configuracion**. No cubre el muestreo/inferencia, ni la evaluacion E-A1..E-A4, ni XCIST, ninguno de los
  cuales tiene medicion. El presupuesto total de la tesis **sigue sin estar cerrado**.
- **Tipo:** REDACCION + SUPUESTO. **Lista para pasar a CERRADA, pero no aplicada a `main.tex` ni a
  `00-tesis.md` (reglas 4 y 14): espera decision de la autora.**

### 114 — La columna `s_por_paso` es un promedio ACUMULADO, no el ritmo de un tramo — **CERRADA el 2026-10-04**: `curva.csv` anade `s_tramo`, que es el ritmo real

- **Hallazgo:** `src/renderizador/entrenar.py:144` calcula `sp = (time.time() - t0) / paso`, con `t0`
  fijado antes del bucle y **nunca reiniciado**. Toda fila de `curva.csv` es el promedio desde el paso 1,
  no el ritmo de su tramo. Por eso la columna decrece de forma monotona y suave (0.1500, 0.1211, 0.1113,
  0.1065, 0.1036, 0.1018, 0.1005, 0.0995): es la firma de una media acumulada que arrastra un arranque
  lento, no de una medicion por tramo, que seria ruidosa alrededor del valor estable.
- **Por que importa:** `KHIPU.md` (seccion A2) y el encargo anterior mandan tomar "`s_por_paso` del
  **ultimo** tramo, no del primero, porque los primeros pasos incluyen la carga". **Esa instruccion no es
  ejecutable leyendo la ultima fila:** la ultima fila (0.0995) sigue contaminada por el arranque. Quien la
  siga al pie de la letra cree estar corrigiendo el sesgo y no lo corrige.
- **Segundo defecto, independiente:** `entrenar.py:151-152` guarda `ckpt.pt` (112 MB) **antes** de calcular
  el `sp` del mensaje `LISTO`. Por eso el titular dice `0.106 s/paso` y extrapola 0.9 h: mete un coste
  **de una sola vez** (1.30 s de escritura de checkpoint) dentro de un ritmo **por paso**, y la
  extrapolacion a 30 000 pasos lo multiplica por 150.
- **Cifra correcta, por diferenciacion de la columna acumulada** (el tiempo acumulado en el paso `n` es
  `n * s_n`; el ritmo del tramo es la diferencia dividida entre 25):

  | tramo | s/paso acumulado | s/paso del tramo |
  |---|---|---|
  | 1-25 | 0.1500 | 0.1500 |
  | 26-50 | 0.1211 | 0.0922 |
  | 51-75 | 0.1113 | 0.0917 |
  | 76-100 | 0.1065 | 0.0921 |
  | 101-125 | 0.1036 | 0.0920 |
  | 126-150 | 0.1018 | 0.0928 |
  | 151-175 | 0.1005 | 0.0927 |
  | 176-200 | 0.0995 | 0.0925 |

- **Comprobacion que podia fallar y no fallo:** si la columna fuera por tramo, la diferenciacion daria
  ruido sin estructura. Da **0.0917-0.0928, plano**, que es justo lo que predice la hipotesis de media
  acumulada. El regimen es **0.0923 s/paso** (pasos 26-200). El arranque cuesta **1.44 s una sola vez**.
- **Direccion del sesgo:** las dos cifras publicadas **sobreestiman** (0.106 y 0.0995 frente a 0.0923),
  o sea el error es conservador y **la decision no cambia**: 0.77 h frente a 0.88 h, ambas lejisimos del
  umbral de 20 h. **Lo que cambia es la cifra que puede ir a la tesis.**
- **Opciones:** (a) dejar el codigo y corregir `KHIPU.md` para que mande diferenciar la columna;
  (b) reiniciar `t0` tras el primer tramo y escribir el ritmo por tramo, mas guardar `ckpt.pt` **despues**
  de calcular el `sp` final; (c) las dos.
- **Recomendacion: (b) + (c)** — una columna que hay que posprocesar a mano para leerla bien es una
  trampa; el arreglo son tres lineas. Mientras no se arregle, **la cifra que vale es 0.0923 s/paso**.
- **Por que encaja con la advertencia de metodo de este proyecto:** es el quinto fallo silencioso
  detectado **mirando la salida**, no por un control. Los controles de la corrida (identidad, aislamiento,
  perdida en `G`) pasaron todos y **ninguno vigila la unica cifra que el piloto existe para producir.**
- **Contagio: NINGUNO, y el patron correcto ya existe en el repositorio.** Se verifico
  `experiments/objetivo1/p1_decodificador_sd15.py`: en la linea 330 calcula
  `(time.time() - t_bloque) / n_acum` y en la 331 **reinicia `t_bloque`**. Es decir, **P1 si mide por
  bloque**, asi que su cifra de **1.32 s/paso**, que `KHIPU.md` y #89 citan, **no esta afectada**.
  `entrenar.py` es una regresion respecto de P1, no un criterio distinto. El arreglo (b) es copiar el
  patron que ya funciona dos directorios mas alla.
- **Tipo:** VALIDEZ DE MEDICION / INSTRUMENTACION. Toca `src/renderizador/entrenar.py` y
  `experiments/objetivo2/KHIPU.md`. **Nivel: interno.**

### 115 — El renderizador usa el 7% de la GPU (3.35 de 48 GB) y ~1 h de las 24 h de la cola: la configuracion del Diseno A esta muy por debajo del hardware disponible — ABIERTA (liga con #89, #106, #112)

- **Hallazgo:** `gb_max = 3.35 GB` constante en los ocho puntos de `curva.csv`, sobre una RTX A6000 de
  **49 140 MiB**. Con `lote 4`, `lado 256`, `base 64` y 28.0 M de parametros, el entrenamiento completo de
  30 000 pasos cabe en **0.77 h**, frente al limite de **24 h** de la QoS `a-tesis`.
- **Consecuencia inmediata sobre el plan de trabajo:** los dos barridos que `KHIPU.md` proponia
  (`--base 96 --lote 2` y `--base 64 --lote 8`) estaban pensados como **pruebas de que algo cabe**. Ya no
  hacen falta para eso: nada esta cerca del techo. Si se corren, es para otra pregunta.
- **La pregunta que esto abre, y que no es mia:** con dos ordenes de magnitud de holgura en memoria y uno
  en tiempo, la configuracion actual es una eleccion, no una restriccion. Las salidas posibles no son
  equivalentes:
  - (a) **Dejarla igual** y declarar la holgura. Defendible: el conjunto son **17 149 parches de 47 casos**,
    y mas capacidad sobre pocos datos no es gratis.
  - (b) **Subir `lote`**, que estabiliza el gradiente. Es lo mas barato y lo menos comprometido.
  - (c) **Subir `base`** (mas capacidad). Interactua con #106: la arquitectura ya esta declarada como
    eleccion pragmatica **no comparada**, y tocarla sin evaluacion solo mueve el problema.
  - (d) **Mas pasos.** A 0.0923 s/paso, 100 000 pasos son 2.56 h.
  - (e) **Ampliar la banda `B_delta` o el contexto**, que es lo unico que tocaria una pregunta de tesis y
    **arrastra #112**: mas parches de banda **exigen ademas** cambiar la normalizacion de la perdida a
    peso proporcional a `|G|`. Las dos cosas juntas o ninguna.
- **Recomendacion:** **(a) o (b), y declarar la holgura**; **no** (c) ni (e) por ahora. Nada de esto se
  decide con un piloto de 200 pasos: **el piloto midio coste, no calidad**, y hoy no existe ninguna metrica
  de calidad implementada (E-A1..E-A4 sigue sin una linea). Subir capacidad antes de poder medir si sirve
  es exactamente el movimiento que no se puede justificar despues.
- **Riesgo a evitar, explicito:** que la holgura de computo se lea como invitacion a agrandar el modelo.
  El cuello de botella de esta tesis **no es la GPU**: son 47 casos, 3 pacientes de validacion (#105) y
  cero metricas de evaluacion escritas.
- **Tipo:** DISENO + PRESUPUESTO. **Pendiente de decision de la autora. No aplicado.**

### Lo que este piloto NO dice, escrito para que nadie lo cite de mas

- **La perdida no significa nada, y ahora se sabe por que.** `entrenar.py:145` registra
  `float(l.detach())`, es decir **el valor de UN lote de 4 parches con pasos de tiempo `t` aleatorios**,
  no una media movil. La subida de 0.4933 (paso 100) a 0.7837 (paso 200) es **varianza del muestreo de
  `t`**, no divergencia ni sobreajuste. Con `lote 4` no se puede distinguir una cosa de la otra.
- **No hay ninguna evidencia sobre calidad de imagen.** No se genero una sola muestra: `ckpt.pt` existe
  pero no se corrio muestreo.
- **#112 sigue sin poder evaluarse.** La costura en el borde de `B_delta` solo se ve en muestras generadas.
  El piloto no aporta nada a esa decision.
- **El bucle de validacion sigue sin conectar.** `entrenar_meta.json` solo registra el manifiesto de
  `train`; `a5_manifiesto_val.csv` existe y **nada lo consume**. Sigue siendo la Tarea 3.1 del encargo.

### 116 — El alcance MINIMO VIABLE es lo unico sin codigo: `src/muestreador/` esta vacio y SAP tiene 0 lineas, mientras el alcance COMPLETO (Obj 3) ya tiene modelo entrenado — ABIERTA (liga con #90, #91, #95)

- **Origen:** revision del estado experimental pedida por la autora, 2026-09-21, despues de analizar el
  piloto A2. No sale de ningun paper: sale de inventariar el arbol.
- **Hallazgo, verificado contra disco:**
  - `src/muestreador/` **existe y esta vacio** (0 archivos).
  - **SAP no tiene una sola linea en el repositorio:** `grep -rl "SAP" --include=*.py src/ experiments/`
    no devuelve nada. `00-tesis.md` la declara **"unica metrica introducida por esta tesis"**.
  - `muestrea_ddim` esta definida en `src/renderizador/difusion.py:93` y **ningun archivo la llama**:
    `ckpt.pt` no puede producir una imagen. **Nunca se genero una muestra sintetica en el proyecto.**
  - El banco de geometrias de implante sigue **PENDIENTE DE DEFINIR** (CLAUDE.md), con #97 y #99 abiertas
    sobre si el cilindro liso de 6.5-8.0 mm sobreestima el metal.
- **Por que toca el ALCANCE y no es solo gestion:** `00-tesis.md` define el minimo viable como
  **Obj 1 + Obj 2 + SAP**, "lo que garantizo defender". El Obj 1 esta cerrado (#91, NO-GO, ya redactado).
  De lo que queda del minimo viable, **las dos piezas que faltan son justo las que tienen directorio vacio**.
  El Obj 3, que `00-tesis.md` marca como COMPLETO y condicional, es lo unico con modelo entrenado, cache de
  17 149 parches, criterio preinscrito y presupuesto medido (#89).
- **Consecuencia si no se corrige:** hoy el proyecto **no puede defender su propio alcance minimo**, y la
  unica contribucion metrica propia que declara no existe. Es independiente del plazo: con 5 o con 11
  semanas, el orden de trabajo actual deja el camino critico para el final.
- **Segundo hallazgo, sobre por que hay tantas implicancias estancadas:** la cadena del Obj 3 es
  geometria -> colocacion -> mascara -> render -> metrica, y **solo existe el cuarto eslabon**. Por eso
  **#95, #96, #112 y #57 son todas predicciones sobre imagenes que nadie ha visto**. Un muestreo minimo
  (cargar `ckpt.pt`, llamar `muestrea_ddim`, una mascara, una lamina) cuesta **segundos** a 0.0923 s/paso
  y 3.35 GB —cabe en la laptop, no necesita Khipu— y convertiria las cuatro en observacion.
- **Recomendacion del asistente:** (1) muestreador y SAP primero, por ser el minimo viable y lo
  irreemplazable; (2) end-to-end minimo del Obj 3, aunque la salida sea mala; (3) despues bucle de
  validacion, E-A1..E-A4 y Metodos. **Aplazar** los barridos de `--base`/`--lote`, #115 y las fichas
  pendientes salvo RePaint.
- **Depende de #90:** si el plazo real son 5 semanas, el Obj 3 deberia declararse demostrativo con el
  modelo ya entrenado y cortarse ahi. Con ~11 cabe ademas el punto (2).
- **Nota de trazabilidad:** en el chat del 2026-09-21 este asistente dijo primero "sin implicancias
  nuevas" sobre esta misma revision, por considerarla priorizacion y no hallazgo. **Es incorrecto bajo la
  regla 17:** toca el alcance declarado y no se reconstruye despues. Queda registrada.
- **Tipo:** ALCANCE + PLAN DE TRABAJO. **La priorizacion la decide la autora. No aplicado a `main.tex` ni
  a `00-tesis.md` (reglas 4 y 14).**

---

## Ronda 2026-09-21 (lectura de 8 papers) — ajustes a #56, #57/#60, #73 y #106; sin implicancia numerada nueva

Se leyeron a fondo `chen2015lesion`, `ferrero2017technicalnote`, `glover1980nonlinear`,
`jin2021freetumor`, `kadkhodaie2024generalization`, `konz2024anatomicallycontrollable`,
`selles2022mar` y `wu2025freetumor`. Las ocho fichas y sus filas de `_index.md` quedaron registradas;
~~ninguna fuente se dio de alta en `refs.bib` porque el encargo no incluyo normalizacion bibliografica.~~
**CORREGIDO el 2026-09-21, por orden de la autora:** las ocho ya estan normalizadas en `refs/clean/`,
dadas de alta en `refs/MAPEO.md` y en `refs.bib`, que pasa de 110 a **118 entradas**. Compilacion
verificada: **0 errores, 0 citas indefinidas, 7 paginas**. Ninguna esta citada todavia en `main.tex`
(regla 4), asi que entran como disponibles, no como usadas.

- **#56 — el reclamo de novedad debe ser mas preciso.** `jin2021freetumor` predice el parche completo y
  supervisa una region alrededor del borde de la lesion, sin copia dura del exterior;
  `wu2025freetumor` hace lo contrario y recompone exactamente el CT original fuera de la mascara;
  `konz2024anatomicallycontrollable` concatena una mascara a una U-Net de difusion, pero genera el corte
  completo desde ruido. Por tanto, no es defendible reclamar como novedad la insercion sintetica, la U-Net
  de difusion condicionada por mascara ni cualquier cambio fuera de una mascara. La diferencia que sobrevive
  es la combinacion **objeto metalico rigido + codificacion multi-ventana + banda exterior explicita para
  efectos de adquisicion + copia exacta fuera de `G`**. Ninguno de los tres modela metal, HU altos o streaking.
- **#57/#60 — Glover refuerza la direccion de `B_delta`, no su ancho.** El volumen parcial axial puede
  producir streaks que conectan estructuras incluso bajo un modelo monocromatico. Esto confirma que el
  efecto no queda contenido en `M`, pero distancia radial, decaimiento en mm y un ancho de 12 mm son
  **NO ENCONTRADO EN EL PDF**. E-A3 debe describirse como preservacion por construccion, no como fidelidad
  fisica del campo completo de artefacto; el modelo 2.5D tampoco equivale a integrar continuamente el
  espesor del detector.
- **#73 y evaluacion E-A1--E-A4 — menos streaking no implica mejor imagen.** `selles2022mar` muestra, en
  fusion sacroiliaca, que O-MAR puede reducir rayas y a la vez empeorar contraste y delineacion cortical
  por artefactos secundarios. E-A1/E-A2 deben interpretarse junto con integridad osea y E-A4 debe separar
  explicitamente streaking de delineacion/contraste cortical. Una unica lectora solo permite QC descriptivo,
  no validacion clinica reproducible. El paper no aporta una metrica transferible ni distancia para `B_delta`.
- **#106 — Kadkhodaie no rehabilita el argumento de superioridad U-Net.** La red estudiada es bias-free,
  ReLU, ciega al nivel de ruido y localmente lineal por construccion; no equivale a la U-Net real del
  proyecto y no se compara con DiT. Su regimen de datos tampoco se puede trasladar a parches correlacionados
  de pocos pacientes. La eleccion vigente sigue siendo pragmatica y no comparada.
- **#106 — Konz si suma, y en la direccion contraria a la del reclamo de novedad.** Donde para #56 es un
  problema (concatenar mascara a una U-Net de difusion no es novedoso), para #106 es **apoyo**:
  `konz2024anatomicallycontrollable` es el precedente publicado **mas cercano a lo implementado** —difusion
  en **espacio de imagen**, 2D a 256 x 256, U-Net que recibe la mascara **por concatenacion en cada paso**,
  `T = 1000` y muestreo **DDIM**— en imagen medica y con 40 pacientes. Suma un cuarto precedente a los tres
  que ya sostienen la #106 vigente (DDPM/ADM, Yeap, LeFusion) y es el mas proximo en dominio y sampler.
  **Limites que van en la misma frase:** normaliza a `[0, 255]`, **no a HU**; genera el corte completo desde
  ruido, sin CT fuente ni copia exterior; y *"did not consider full 3D generation"*. Por eso refuerza que la
  eleccion es **razonable y con precedente**, y **no** que sea superior ni que transporte HU. La combinacion
  coseno + DDIM eta = 0 con 50 pasos sigue sin aparecer evaluada en ninguna fuente.
- **Chen/Ferrero — antecedente de validacion, no baseline nuevo.** La insercion en proyecciones puede
  conservar dependencias de protocolo que el renderizador en imagen solo aprende implicitamente. Chen aporta
  reinsercion en el mismo paciente y lectura cegada como precedentes para E-A1/E-A4; Ferrero condiciona por
  composicion, espectro, detector y tamano corporal. Ninguno valida implantes metalicos ni sustituye el brazo
  fisico de Peters.
- **Veredicto global:** no cambia el alcance, el baseline, la arquitectura ni la preinscripcion. Si ajusta
  la redaccion de novedad y la interpretacion de E-A3/E-A4 dentro de implicancias ya abiertas. No aparecio
  una referencia de snowballing que superara el filtro vigente: los nodos propuestos son contexto generico,
  estudios de MAR comercial ya cubiertos o sintesis tumoral redundante.

**No aplicado** a `main.tex`, `00-tesis.md`, `01-decisiones.md` ni al diseno de evaluacion (reglas 3, 4 y 14).

### 117 — El muestreador de la tesis no es RePaint ni LeFusion: pone el exterior de `G` a CERO en cada paso, no reinyecta el fondo real ruidoso, y no usa remuestreo — ABIERTA (toca la atribucion de Metodos y ofrece una mitigacion publicada para #112)

- **Origen:** revision de las 15 fichas pendientes (regla 13), 2026-09-21, cruzada con
  `src/renderizador/difusion.py`. La ficha de `lugmayr2022repaint` pregunta literalmente: *"La
  implementacion incorpora remuestreo tipo RePaint o solo composicion enmascarada? No deben presentarse
  como equivalentes."* Esta entrada contesta esa pregunta leyendo el codigo.
- **Lo que hace el codigo, verificado:** `muestrea_ddim` (`difusion.py:93-125`) aplica `x = x * g`
  **en cada paso** y devuelve `x * g`. Es decir, fuera de `G` el tensor queda en **cero**, no en
  contenido real. El contexto entra **solo por los canales de `cond`**
  (`modelo(torch.cat([x * g, cond], dim=1), tb)`). **No hay remuestreo**: un solo recorrido de 50 pasos
  DDIM con `eta = 0`.
- **Como difiere de los dos precedentes que la tesis quiere citar:**
  - **RePaint** reinyecta en cada iteracion la region conocida **muestreada desde la imagen de entrada**
    al nivel de ruido `t`, y ademas *"goes forward and backward in diffusion time"* (Intro, p. 11462)
    para armonizar el borde. Config final: `T = 250`, `r = 10` remuestreos, salto `j = 10`, con el
    beneficio que *"saturates at about n = 10 resamplings"* (Fig. 3, p. 11465).
  - **LeFusion** recompone en cada paso y fuera de la mascara el resultado es *"replaced by the real
    noised background"* (Sec. 3.1, p. 5).
  - **La tesis** no hace ninguna de las dos: es un **denoiser condicionado por concatenacion de canales**
    (mas cercano a Yeap, *"The guiding CBCT image y was concatenated with the noisy CT sample"*) con
    **perdida enmascarada** (esto si coincide con LeFusion, *"exclusively within the lesion region"*) y
    copia del exterior **al final**, no en cada paso.
- **Consecuencia 1, de atribucion (va a Metodos):** **no se puede presentar el muestreador como RePaint
  ni heredar sus hiperparametros.** `T = 250`, `r = 10`, `j = 10` no se transfieren. La descripcion
  correcta es: familia DDPM con backbone U-Net (Ho, Dhariwal), schedule coseno (Nichol-Dhariwal), sampler
  DDIM `eta = 0` (Song), condicionamiento por concatenacion (precedente: Yeap), perdida enmascarada y
  copia exterior (precedente: LeFusion), **sin remuestreo**. RePaint queda como **ancestro del mecanismo
  de inpainting por difusion**, no como el metodo implementado.
- **Consecuencia 2, y es la util: #112 tiene una mitigacion publicada que la tesis no esta usando.** El
  riesgo declarado de #112 es **costura en el borde de `B_delta`**, y armonizar exactamente ese borde es
  **la razon de ser del remuestreo de RePaint**. Hoy el diseno afronta la costura solo con el
  condicionamiento y con la proporcion de parches de banda (limitada a 0.62, #112).
  - **Ventaja practica:** el remuestreo **no toca el entrenamiento**. Es un cambio de muestreo sobre el
    `ckpt.pt` que ya existe, y a 3.35 GB y 0.0923 s/paso el coste es despreciable (#89, #115). Se puede
    probar **con el modelo ya entrenado**, sin relanzar nada.
  - **Cautela:** RePaint lo valida en imagenes naturales 2D (CelebA-HQ, ImageNet, 256 x 256). CT, HU,
    metal, implantes y coherencia 3D son **NO ENCONTRADO EN EL PDF**. Y advierte que con mascaras
    extremas produce completaciones realistas *"very different from the Ground Truth image"* (Sec. 6,
    p. 11468): realismo no es fidelidad cuantitativa. Si se adopta, entra **declarado y preinscrito**,
    no como arreglo posterior si la costura sale fea —la misma regla que ya fija la mitigacion de #96.
- **Opciones:** (a) dejar el muestreo como esta y declarar la diferencia con RePaint en Metodos;
  (b) (a) mas evaluar el remuestreo como **brazo de sensibilidad preinscrito** sobre el `ckpt.pt`
  existente, solo si la costura aparece; (c) adoptarlo por defecto (no recomendado: nada lo valida en CT
  con metal).
- **Recomendacion: (a) ya, y (b) solo si la costura aparece al mirar las primeras muestras.** La
  atribucion hay que arreglarla igual; el remuestreo es una carta guardada, no una tarea.
- **Nota sobre por que esto no se vio antes:** #112 lleva semanas abierta discutiendo la costura sin que
  existiera **ninguna muestra generada** (#116). La mitigacion estaba en la bibliografia del propio
  proyecto desde que se leyo RePaint.
- **Tipo:** METODO + ATRIBUCION. Toca `tesis/main.tex` (Metodos, cuando se escriba) y, opcionalmente,
  `src/renderizador/difusion.py`. **No aplicado (reglas 4 y 14).**

### 90 — ACTUALIZACION (2026-09-21): la autora fija ~5 semanas; el brazo de equivalencia contra Peters deja de ser entregable y `main.tex:98` queda comprometido

- **Origen:** instruccion de la autora, 2026-09-21: *"considera que quedan como 5 semanas y endurece tu
  recomendacion, la voy a adaptar"*. Es adopcion del plazo corto, **todavia no formalizada** como decision
  en `01-decisiones.md`.
- **Consecuencia concreta, que no puede quedarse en el chat:** `main.tex:98` promete hoy **Wilcoxon de una
  cola** (superioridad frente a copia-pega) **y TOST** (equivalencia frente al protocolo fisico de
  `peters2025hybrid`), con margen `Delta` medido en validacion. **El brazo TOST no es entregable en 5
  semanas:** exige implementar el brazo fisico entero, medir `Delta` sobre n = 3 (#105), conectar el bucle
  de validacion (hoy inexistente) y correr la evaluacion. Ademas `diseno_A.md` **no se puede preinscribir**
  sin `Delta` (D4), asi que el Objetivo 3 seguiria sin congelar.
- **Recomendacion del asistente:** conservar el endpoint primario unico (streak amplitude) con **Wilcoxon
  frente a copia-pega**, y declarar la **equivalencia frente a Peters como trabajo futuro** —no como
  resultado "no concluyente"—. El Objetivo 3 se entrega **demostrativo**, que es lo que `00-tesis.md` ya
  dice. Es el mismo movimiento ya hecho con el downstream (punto 1 de `Fuera de alcance`) y con las
  ablaciones (punto 10).
- **Lo que NO se toca:** el Objetivo 1 y su No-Go ya estan redactados; el minimo viable (Obj 2 + SAP)
  **no se recorta**, es justo lo que absorbe el tiempo liberado (#116).
- **DECISION DE LA AUTORA (2026-09-21, en chat):** **no se corta nada por ahora.** Se apunta a llegar al
  Objetivo 3 dentro de las ~5 semanas y **`main.tex` no se toca**: el brazo TOST **se mantiene como meta**.
  El recorte de arriba queda como **contingencia declarada**, a aplicar solo si el plazo lo obliga.
  Literal: *"Por ahora no voy a tocar lo de main.tex a pesar del endurecimiento porque se intentara llegar
  en 5 semanas al objetivo 3. En caso de no llegar, se cortara pero por ahora solo se dejara como una
  posibilidad."* **El asistente no debe aplicar el recorte por su cuenta.**
- **Que toca si se confirma:** `main.tex:98` y la tabla de Expected Results (fila *Appearance Coherence*),
  el alcance COMPLETO de `00-tesis.md`, D4 de `01-decisiones.md` y #112. **No aplicado a `main.tex`
  (regla 4) ni a `01-decisiones.md` (regla 3): la decision formal es de la autora.**

---

## Ronda 2026-09-22 — revision de estado para arrancar el Objetivo 2 (asistente en rol de asesor)

### 118 — El benchmark de Zwingmann se midio sobre tornillos de **7.0 mm**, y esa es una TERCERA geometria que la tesis no tiene declarada — **CERRADA el 2026-09-22** (opcion (a) adoptada y aplicada)

- **Origen:** revision de la agenda del Objetivo 2 (D-O2.4: "que diametro entra en la brecha"), 2026-09-22.
  No sale de una lectura nueva: sale de releer la ficha ya existente de `zwingmann2009navigated`.
- **Evidencia textual, de la ficha:** *"the screws using a 7.0-mm cannulated screw"* (Materials and Methods,
  p. 1835). Complementarias en la misma seccion: broca guia de 3.2 mm y broca canulada previa de 5 mm.
- **Por que importa:** SAP compara la distribucion de grados de brecha del muestreador contra la distribucion
  **medida sobre tornillos de 7.0 mm**. La profundidad de perforacion escala con el radio del cilindro, asi
  que medir la brecha con un diametro distinto **sesga el grado de forma sistematica** —hacia abajo si se usa
  menos de 7.0, hacia arriba si se usa mas— y el Wasserstein-1 resultante mezcla ese sesgo geometrico con la
  diferencia real de poses. No es una eleccion libre de convenios: es una condicion de comparabilidad.
- **El problema concreto:** `00-tesis.md` declara hoy **dos** geometrias (envolvente **6.5-8.0 mm** para
  viabilidad de corredor, #31; cilindro de **~4.91 mm** para sintesis, D3 del 2026-09-20) y **ninguna de las
  dos es 7.0 mm**. La de sintesis queda 2.1 mm por debajo del tornillo del benchmark. Si SAP se midiera con
  4.91 mm, los grados saldrian artificialmente buenos frente a Zwingmann.
- **Opciones:**
  - (a) **SAP se mide con 7.0 mm**, por comparabilidad con el benchmark, y se declara como **tercera
    geometria con proposito propio** (metrica), separada de la de viabilidad (#31) y la de sintesis (D3).
    4.91 mm y 7.3 mm entran como sensibilidad.
  - (b) SAP se mide con 4.91 mm (coherencia interna con lo que se sintetiza) y se declara el sesgo a la baja
    frente a Zwingmann, sin corregirlo.
  - (c) Se cambia la geometria de sintesis a 7.0 mm, reabriendo D3 y #101.
- **Recomendacion del asistente: (a).** Es la unica que no rompe nada ya decidido y la unica que hace
  interpretable el Wasserstein-1. D3 se tomo para responder *"que se sintetiza"*, no *"con que se mide la
  brecha"*: son preguntas distintas y `zhu2022optimalposition` ya usa dos diametros sin declararlo
  (precedente citado en `00-tesis.md`). (c) es la peor: obligaria a rehacer E11 y la cache de parches.
- **Nota:** `main.tex` cita hoy el rango **6.3-8 mm** de Kaiser para justificar la holgura de 10 mm; 7.0 cae
  dentro de ese rango, asi que (a) no contradice lo escrito.
- **Tipo:** METODO + METRICA.
- **DECISION DE LA AUTORA (2026-09-22, en chat):** se adopta **(a)**. SAP se mide con **7.0 mm**; 4.91 y
  7.3 mm quedan como sensibilidad declarada. D3 **no se reabre**.
- **APLICADO el 2026-09-22, por orden explicita de la autora:** el bloque de `00-tesis.md` pasa de
  *"Dos geometrias para dos preguntas distintas"* a **tres**, con tabla y con la frase original de
  Zwingmann. La decision se redacto como **D-O2.4** en `01-decisiones.md`. **`tesis/main.tex` NO se toco**
  (regla 4): no se pidio en ese turno. **Queda pendiente de la autora** llevar la tercera geometria al
  documento cuando lo decida.
- **Estado: CERRADA.**

### 119 — La etiqueta "los 7 de FOV cortado" no corresponde a lo que el codigo descuenta, y los casos de FOV cortado **no estan** en la cohorte del Objetivo 2 — **CERRADA el 2026-09-22**

- **Origen:** verificacion directa de `e9ts_corredor.csv` al revisar D-O2.2, 2026-09-22.
- **Hallazgo, contado sobre el CSV (152 casos unicos):**
  - `fov7 = True` en **4 casos**, y los cuatro son de **grupo 1**. Ninguno cae en grupos 2 o 3.
  - La tabla de `e9ts_resumen.md` titulada *"grupo 1 sin los 7 de FOV cortado"* baja de **52 a 49**, es decir
    descuenta **3**, no 7 ni 4: uno de los cuatro ya lo elimina el QC de nivel. El titulo lo escribe
    `e9ts_resumen.py:96` con el literal "7" hardcodeado.
  - El "7" original viene de R1 (65 pacientes); solo 4 de esos sobreviven al conjunto de 152.
- **Consecuencia para el Objetivo 2, y es la util:** la cohorte primaria son **grupos 2 y 3 (72 casos)**, y
  **ningun caso de FOV cortado esta dentro**. El pendiente que `00-tesis.md` arrastra desde el 2026-09-11
  —*"El tratamiento de los 7 con FOV cortado sigue sin decidir"*— **no bloquea el muestreador**: solo afecta
  al grupo 1, que es contraste y no cohorte.
- **Consecuencia de redaccion:** la cifra "7" no debe reaparecer en `main.tex` asociada a este CSV sin decir
  sobre que conjunto se cuenta. Son universos distintos (65 de R1 frente a 152 de E9-TS).
- **Recomendacion:** (1) declarar en `00-tesis.md` que el pendiente de FOV queda **cerrado por irrelevancia
  para la cohorte del Objetivo 2**, y (2) corregir el titulo hardcodeado de `e9ts_resumen.py:96` para que
  imprima el descuento real.
- **Tipo:** DATO + REDACCION.
- **DECISION DE LA AUTORA (2026-09-22, en chat):** se adoptan los dos puntos.
- **APLICADO el 2026-09-22:** (1) en `00-tesis.md`, R1 deja de decir *"sigue sin decidir"* y declara el
  pendiente **cerrado por irrelevancia para la cohorte del Objetivo 2**, con la advertencia de que el "7"
  de R1 (65 pacientes) y el "4" de E9-TS (152 casos) son universos distintos y no deben citarse juntos;
  (2) `e9ts_resumen.py` ya no imprime el "7" hardcodeado, sino el descuento real, calculado.
  Consta ademas como **D-O2.2** en `01-decisiones.md`. **`tesis/main.tex` NO se toco** (regla 4).
- **Estado: CERRADA.**

### 120 — `tramo` es un buscador de CORREDORES, no un calificador de POSES: a 5-8 grados de inclinacion devuelve "no evaluable" en vez de un grado, y eso sesga la distribucion que compara con Zwingmann — **CERRADA el 2026-09-22** (opcion (b) adoptada y aplicada)

- **Origen:** control **C5** de `experiments/objetivo2/e12_sap_control.py`, 2026-09-22, al implementar SAP.
  No sale de un paper: sale de mirar la salida del control que se escribio para que pudiera fallar.
- **Que se ve, medido:** inclinando el eje del corredor alrededor de su centro, con cilindro de 7.0 mm:
  - `dataset7_CLINIC_metal_0008_data`: 0 grados -> grado 0; 1 -> 1; 2 -> 0; 3 -> 1; **5 -> None**;
    **8 -> None**; 12 -> 2.
  - `dataset6_CLINIC_0002_data`: 0 a 5 grados -> grado 0; 8 -> 2; **12 -> None**.
  El `None` **no es un grado alto**: es "esta pose no es evaluable", y aparece **en medio** del barrido,
  con poses peores a un lado y mejores al otro.
- **Causa, verificada en el codigo:** `e9_corredor.tramo` exige que la trayectoria **salga a tejido
  blando** —ningun hueso en los 40 mm siguientes (`SALIDA_BLANDO_MM`)— y ademas que cada salida sea al
  menos tan lateral como la EIPS. Esos requisitos existen porque `tramo` se escribio para **encontrar
  corredores transsacros validos**, donde son correctos. Pero SAP no busca un corredor: **califica una
  pose que ya esta puesta**, y un tornillo malposicionado no tiene por que cumplirlos. Se esta usando un
  filtro de admisibilidad como si fuera un medidor.
- **Por que toca el argumento de la tesis y no es solo un detalle de implementacion:** D-O2.1 compara la
  distribucion de grados del muestreador contra las de `zwingmann2009navigated` por Wasserstein-1.
  Zwingmann califico **todos** sus tornillos (26 y 35), porque todos estaban implantados: su denominador
  no descarta nada. Si el muestreador produce poses que salen `None` y se descartan en silencio, el
  denominador de esta tesis **si** descarta, y descarta justamente las poses mas desviadas. El W1
  saldria artificialmente bajo. **Y el barrido muestra que no es un caso raro:** ocurre a 5-8 grados, un
  rango que la propia introduccion de Zwingmann considera clinicamente relevante (*"Malposition of the
  screw by as little as 4 degrees can cause damage"*, Introduction, p. 1834, cita de terceros).
- **Mitigacion ya implementada, que no decide nada:** `sap.distribucion_grados` tiene el parametro
  `no_evaluables` con **defecto `'error'`**: lanza si hay alguna. Descartar en silencio es hoy
  imposible. Las otras dos opciones son `'grado3'` (contarlas como grado 3) y `'excluir'` (descartarlas
  con el recuento declarado).
- **Opciones de fondo:**
  - (a) **Contar los `None` como grado 3.** Barato y conservador: perforar mas de 4 mm y no tener
    corredor valido no se distinguen en una escala de cuatro grados. Pero mete en el grado 3 poses que
    fallan por razones distintas (sin salida a blando, salida poco lateral) y no por perforar.
  - (b) **Separar el calificador del buscador.** Definir el tramo de SAP por el **primer y ultimo cruce
    del eje con la envolvente osea**, recortando 8 mm por extremo, **sin** exigir salida a blando ni
    lateralidad de EIPS. Es mas trabajo y hay que reescribirlo sin tocar `e9_corredor` (que esta bien
    para lo suyo), pero da un grado a toda pose que atraviese hueso, que es lo que hace un radiologo.
  - (c) Declarar las poses sin corredor como categoria propia fuera de la escala y reportar su
    frecuencia aparte del W1.
- **Recomendacion del asistente: (b), y (a) como respaldo.** (b) es lo unico que hace que SAP califique
  lo mismo que califico Zwingmann. (a) sirve si el plazo aprieta, **declarado**. (c) no cierra el
  problema: deja el W1 calculado sobre un subconjunto elegido por el propio criterio que se evalua.
- **Nota de metodo:** esto lo encontro el control C5, que se escribio precisamente porque los controles
  C1-C4 solo producian ceros y **un control que solo da ceros no distingue una metrica correcta de una
  que devuelve 0 siempre**. Es el quinto fallo silencioso del proyecto detectado mirando la salida.
- **Tipo:** METODO.
- **DECISION DE LA AUTORA (2026-09-22, en chat):** se adopta **(b)**, separar el calificador del buscador.
- **APLICADO el 2026-09-22 en `src/muestreador/sap.py`.** El camino hasta la version correcta lo
  marcaron los controles, y queda escrito porque es lo que justifica la definicion final:
  1. *Del primer al ultimo cruce del eje con la envolvente.* La tumbo **C6**: en
     `dataset7_CLINIC_metal_0008_data` el eje vuelve a tocar hueso a ~90 mm del centro, el tramo pasaba
     de 97 a 167 mm incluyendo tejido blando, y la brecha salia **10.38 mm sobre el propio eje del
     corredor**, que debe dar 0.
  2. *Igual, cortando en el primer hueco de 40 mm* (`SALIDA_BLANDO_MM`, sin constante nueva). Arreglo C6
     pero la tumbo **C5**: a 20 grados de inclinacion la brecha volvia a **0.0**, porque el tramo se
     encoge con la pose y **"quedarse dentro del hueso que uno mismo elige atravesar" es trivialmente
     satisfacible**.
  3. **Version final:** el tramo es el **propio implante**, de longitud fija igual a la del corredor de
     ese caso, centrado en la pose y recortado 8 mm por extremo. La extension del implante **no depende
     de donde este el hueso**. Requirio ademas anclar la pose base al punto medio del corredor
     (`sap.pose_base`), porque `c_*_mm` del CSV es el origen de busqueda y no el punto medio.
- **Resultado de los controles tras aplicar (b)**, en `e12_sap_control.md`: C2 y C6 dan **0.0 exacto**
  en los dos casos piloto, C3 pasa, y C5 es ahora monotona y sin ningun `None`:
  0-3 grados -> grado 0; 5 -> 1; 8 -> 2; 12 y 20 -> 3. **Ninguna pose se queda sin grado.**
- **Estado: CERRADA.**

### 121 — El segundo corredor NO es S2: en 5 de 18 casos cae en S3 o mas caudal. Medido, no supuesto — **CERRADA el 2026-09-23** (medido, decidido y escrito en `main.tex`)

- **Origen:** al escribir `experiments/objetivo2/preinscripcion_muestreador.md`, 2026-09-22. Salio de
  buscar en el CSV los campos que hacian falta para muestrear en S2 y no encontrarlos.
- **Hallazgo, verificado contra las columnas del CSV:** hay **un solo** `(c_x_mm, c_y_mm, c_z_mm)` y un
  solo `(u_x, u_y, u_z)` por fila, y `e9_corredor` los calcula con **los centros en el sagital del S1**
  de R1. De S2 existen unicamente `pico_inf_z_rel_mm` y `pico_inf_D_mm`: **posicion y diametro del pico
  inferior del perfil, sin direccion**. Un diametro no es una pose: sin `u` no se puede perturbar nada.
- **Consecuencia:** la parte de D-O2.5 que dice *"el muestreador propone pose en S1 y en S2"* **no es
  ejecutable hoy**. La parte del benchmark no se toca: el prior ordinal ya era solo S1 (#12, #28), asi
  que el **resultado principal del Objetivo 2 no depende de esto**. Lo que queda sin poder hacerse es el
  reporte **descriptivo** de S2.
- **Por que no se vio antes:** D-O2.5 se decidio sobre lo que dice `00-tesis.md` —que S1/S2 se conserva
  como variable geometrica del muestreador— sin comprobar que el insumo tuviera eje para los dos
  niveles. Es el mismo patron que la advertencia de metodo del proyecto: **antes de afirmar algo sobre
  un artefacto, leer su estado actual**.
- **Opciones:**
  - (a) **Medir un eje de corredor en S2** reutilizando `e9ts_corredor.py` con los centros en el sagital
    de S2. Es una corrida de Khipu sobre la cohorte, no codigo nuevo de fondo, pero hay que ubicar el
    nivel S2 en cada caso y eso no esta en R1.
  - (b) **Dejar S2 fuera del muestreo** y conservarlo solo como lo que ya esta medido: perfil de
    diametro por altura (`pico_inf_*`), reportado descriptivamente sin poses.
  - (c) Aplazar S2 a trabajo futuro, declarado.
- **Recomendacion del asistente: (b) ahora, (a) solo si sobra tiempo al final.** El resultado principal
  no depende de S2, y (a) mete una medicion nueva en el camino critico del alcance minimo viable
  justo cuando #116 dice que ese camino es lo unico sin terminar. (b) no pierde nada de lo ya medido y
  mantiene la promesa de `00-tesis.md` de evaluar S2 "descriptivamente (geometria y grados de brecha)"
  — con el matiz de que serian grados **del corredor**, no de poses muestreadas, y hay que escribirlo asi.
- **Afecta a:** D-O2.5 de `01-decisiones.md` y la frase de S2 del alcance minimo de `00-tesis.md`, que
  hoy promete mas de lo que el insumo permite. La preinscripcion ya lo declara en su seccion 7.
- **ACTUALIZACION 2026-09-22 (2), tras implementar el muestreador: la opcion (a) es MUCHO mas barata
  de lo que decia arriba, y pasa a ser la recomendada.** Verificado leyendo `e9ts_corredor.py:167-200`
  y el CSV de perfiles:
  - `buscar()` **ya calcula el eje a cada altura**: recorre `zs = S1 - 3..75 mm` en pasos de 3 mm y en
    cada una guarda `mejor_z = {**r, 'c': c, 'u': u}`. **El eje de S2 se calcula y se tira**: a
    `e9ts_perfiles.csv` solo se escribe `D_TS_mejor_mm`, y de todo el barrido solo sobrevive el eje del
    mejor global, que es el de S1.
  - El barrido **ya cubre S2**: en la cohorte del Objetivo 2 el pico inferior esta a **-30 mm** de S1
    (mediana; IQR -36 a -27) con diametro mediano **7.3 mm**, y existe en **69 de 72** casos.
  - **No hace falta ningun landmark nuevo.** Mi objecion original —"hay que ubicar el nivel S2 en cada
    caso y eso no esta en R1"— **era incorrecta**: el barrido no usa un landmark de S2, usa alturas
    relativas a S1, y el pico inferior ya esta identificado y medido.
  - **El muestreador y SAP son agnosticos al nivel**: `muestrear_poses` y `evaluar_pose` toman
    `(c, u, L)` y no preguntan de que vertebra salen. No hay codigo nuevo aguas abajo.
  - **Coste real:** anadir `c_x,c_y,c_z,u_x,u_y,u_z` a las filas de `e9ts_perfiles.csv` y **relanzar
    E9-TS sobre los 72 casos de la cohorte**, no sobre los 358. Es una edicion corta y una corrida de
    Khipu; `e9ts_corredor.py` es reanudable.
- **Recomendacion revisada: (a) por la via del perfil**, es decir volcar el eje por altura y tomar el
  del pico inferior como eje de S2. Con eso D-O2.5 se cumple entera —muestreo en S1 y S2, benchmark
  ordinal solo en S1— sin tocar el resultado principal ni la preinscripcion de S1, que se queda como
  esta. (b) pasa a ser el plan de contingencia si el plazo aprieta, y (c) se descarta: no hay motivo
  para aplazar algo que ya esta calculado y solo falta guardar.
- **Como se cierra, en concreto:** (1) se anaden las seis columnas del eje a la salida de perfiles;
  (2) se relanza E9-TS sobre la cohorte; (3) se escribe una **preinscripcion de S2 aparte**, identica a
  la de S1 salvo el eje base y con el descriptivo declarado como tal; (4) se corre E13 con el eje de S2
  y se reporta **sin Wasserstein-1**, porque no hay prior ordinal para S2 (#12, #28). Mientras (1) y (2)
  no esten, `main.tex` promete mas de lo que el insumo permite, y esa es la unica deuda que esto deja.
- **ACTUALIZACION 2026-09-22 (3): falta un paso previo que las dos actualizaciones anteriores no vieron.
  El pico inferior NO esta etiquetado como S2; se infiere de la forma del perfil de diametro.**
  - TotalSegmentator `total` etiqueta **`vertebrae_S1`** y el **sacro entero**. **No hay etiqueta de
    S2.** Las cuatro estructuras que usa el corredor son `sacrum`, `vertebrae_S1`, `hip_left` y
    `hip_right` (`e9ts_corredor.py:91`).
  - Por tanto "el pico inferior del perfil es S2" es una **inferencia geometrica**, no un dato. La
    dispersion no permite darla por buena sin mas: en la cohorte del Objetivo 2 el pico inferior cae
    entre **-45.6 y -24.0 mm** de S1 (p10-p90, mediana -30.0) y existe en **69 de 72** casos.
  - Llamarlo "S2" sin verificarlo seria un **supuesto silencioso**, del mismo tipo que los que ya
    costaron tres reescrituras en esta misma sesion (el `tramo` de #120, el calibre del control de #122).
- **Detalle exacto de lo que falta en el codigo**, verificado: `buscar()` guarda
  `mejor_por_z[iz] = mejor_z.get('D_TS', 0.0)` (`e9ts_corredor.py:195-201`), es decir **solo el
  diametro**, y descarta el `c` y el `u` de cada altura; la fila de perfil (linea 305) escribe solo
  `z_rel_S1_mm` y `D_TS_mejor_mm`, y `CAMPOS_PERFIL` (linea 106) tiene seis campos. Hay que conservar
  una lista de ejes paralela a `mejor_por_z` y anadir seis columnas. **Coste de la corrida:** E9-TS
  entero fueron **1.34 h de CPU** sobre 152 casos y todas las variantes; los 72 con una sola variante
  son minutos.
- **Plan de cierre revisado, en ese orden:**
  1. **Verificacion clinica del nivel del pico inferior**, sobre un subconjunto (15-20 casos), con el
     mismo procedimiento que ya se uso para confirmar S1 en los 65 pacientes de R1.
  2. Si confirma: el cambio de codigo, la corrida sobre los 72, una **preinscripcion de S2 aparte**, y
     E13 **sin Wasserstein-1** (no hay prior ordinal para S2; #12, #28).
  3. Si **no** confirma o no hay revisor: se implementa igual, pero se reporta como **"el segundo
     corredor por debajo de S1"** y no como S2. Cumple la parte descriptiva de D-O2.5 sin afirmar un
     nivel que no se midio.
- **ACTUALIZACION 2026-09-22 (4), CORREGIDA: sobre el formato de la revision, no sobre el revisor.**
  - **Hechos verificados:** `r1_auditoria_s1_clinico.csv` (revision de S1 **sobre laminas**, 2026-09-11)
    esta **completa: 65 de 65**. `r1_revision_itksnap_revisor.csv` (segunda vuelta de S1 **en
    ITK-SNAP**, preparada el 2026-09-15) sigue en **0 de 61**.
  - **RECTIFICACION.** En el chat del 2026-09-22 este asistente presento ese 0 de 61 como que "el
    revisor no devolvio la planilla", y de ahi dedujo un riesgo de no-respuesta. **Es incorrecto y no
    estaba sostenido por ninguna evidencia del repositorio:** la revision de S1 se completo, en su
    formato de lamina, y la segunda vuelta en ITK-SNAP es un encargo posterior distinto que
    simplemente no se persiguio. La autora lo corrigio en el chat. Queda registrado por la regla 17.
  - **Lo que si se sostiene, y es lo unico que hay que retener:** el formato que se completa es la
    **lamina**; ITK-SNAP quedo sin usar. Por eso la revision de #121 se entrega como lamina
    (`r2_nivel_pico_laminas.py`) y no como planilla de ITK-SNAP, resolviendo ademas la objecion
    original del revisor: el mosaico de +-60 mm no deja contar vertebras, y la lamina nueva si.
  - **Dato que condiciona el plan:** los 18 casos de la revision de S2 y los 65 de la revision de S1
    **no comparten ningun paciente**. Los de S1 son todos `dataset7` (con metal); la cohorte del
    Objetivo 2 es `dataset6` (sin osteosintesis, decision #52 a). No se puede revalidar S1 sobre las
    laminas de S2.
- **ACTUALIZACION 2026-09-22 (5), a raiz de una pregunta de la autora: la lamina de verificacion
  hereda el mismo hueco de datos, y eso obliga a reordenar los pasos.**
  - **Pregunta de la autora:** *"¿y si la linea pasa por dos S? porque a veces estan muy como
    acostados"*.
  - **Es un problema real, y medido.** La linea de la lamina es un **plano axial**, horizontal; los
    segmentos sacros no lo son. Ademas los dos corredores que mide E9-TS estan separados **18 mm**
    (mediana; IQR 15-21, min 12, max 42) sobre 69 casos de la cohorte, menos que la altura de un cuerpo
    sacro. Un plano axial puede cortar dos segmentos.
  - **La causa de fondo no es la lamina: es que solo se guardo la altura.** El corredor no es un plano,
    es un tubo de **7.3 mm** de diametro (mediana en el pico inferior) que pasa por un punto concreto
    `c = (x_mid, y, z)` (`e9ts_corredor.buscar`). De ese punto **solo se conserva `z`**; la `y` se
    descarta junto con `c` y `u`. Por eso la lamina solo puede marcar una linea horizontal a lo ancho de
    toda la imagen, cuando lo correcto seria marcar **un punto**.
  - **Consecuencia para el orden de trabajo:** hacer primero el cambio de codigo de #121 y **despues**
    la revision. Con `c` y `u` por altura, la lamina marca el punto por donde pasa el corredor y la
    pregunta pasa a tener la **misma forma que la de S1** —un punto juzgado contra la anatomia—, que es
    la que ya se ha contestado 65 de 65 veces. Mandar la revision antes arriesga una segunda pasada.
  - **Medida provisional, por si se manda igual:** la planilla acepta `S1-S2` y `S2-S3`, con el nivel
    dominante en `comentario`. Esa respuesta tambien es informativa: dice que la altura sola no
    identifica un nivel.
  - **No afecta al lote de revalidacion de S1** (61 casos), que marca un punto y no una linea.
- **RECOMENDACION FINAL DEL ASISTENTE, revisada con lo anterior: desacoplar.**
  1. Implementar el volcado del eje por altura y la corrida, y reportar el segundo corredor como
     **"el segundo corredor por debajo de S1"**. Eso **ya cierra** la promesa de `main.tex`, no depende
     de nadie y es defendible hoy.
  2. Mandar la revision de las 18 laminas como **mejora opcional**: si vuelve y confirma, se reetiqueta
     a **S2** y se gana precision anatomica; si no vuelve, **nada queda bloqueado**.
  3. No poner S2 en el camino critico. El minimo viable ya esta cerrado y el riesgo que queda es el
     Objetivo 3, que **nunca ha generado una muestra** (#116) y arrastra el compromiso del brazo TOST
     (#90).
- **ACTUALIZACION 2026-09-22 (6): el cambio de codigo esta HECHO y verificado en local; falta la
  corrida.** Por orden de la autora. En `e9ts_corredor.py`: `buscar()` conserva el eje de cada altura
  (`ejes_por_z`) y lo devuelve; `CAMPOS_PERFIL` pasa de 6 a 12 columnas (+ `c_x_mm, c_y_mm, c_z_mm,
  u_x, u_y, u_z`); `procesar()` los escribe por fila de perfil. Se anade `e9ts_ejes.sbatch`, con
  `--out-dir` propio para **no sobrescribir** el `e9ts_corredor.csv` que respalda cifras de `main.tex`.
  - **Controles pasados sobre el caso piloto:** `|u| = 1` en todas las filas con eje; y el
    `e9ts_corredor.csv` nuevo es **identico por valor** al existente en las **46** columnas comparadas.
    La primera comparacion marco cuatro columnas como distintas y eran **solo dtype** (el CSV viejo
    tiene 152 casos y mezcla tipos); por valor no difiere ninguna. El cambio solo anade.
  - **Pendiente:** lanzar `e9ts_ejes.sbatch` en Khipu, bajar `e9ts_perfiles.csv` y regenerar las 18
    laminas de S2 marcando el **punto** del corredor en vez de la linea.
- **ACTUALIZACION 2026-09-22 (7): el hueco de datos esta CERRADO. Queda solo la decision de etiqueta.**
  La corrida de Khipu se hizo y se bajo (`outputs/e9ts_ejes_corredor.csv`, `e9ts_ejes_perfiles.csv`).
  - **Control de identidad: PASA.** 2 352 filas, 152 casos, **0 errores**, y las **46** columnas del
    `e9ts_corredor.csv` nuevo son identicas por valor a las del existente. El cambio solo anadio.
  - **Eje por altura disponible:** `|u| = 1` en todas las filas con eje, y **69 de 72** casos de la
    cohorte tienen eje a la altura del pico inferior, que son exactamente los que tenian pico.
  - **Dato que explica la ambiguedad de la lamina anterior:** el corredor inferior pasa **30 mm por
    detras** del punto de S1 (mediana; rango -45 a -15), y su eje esta a **8.5 grados** de la horizontal
    izquierda-derecha (mediana; maximo 27). Una linea horizontal no localizaba nada en el plano.
  - **Laminas regeneradas:** las 18 marcan ahora el **punto** del corredor y su seccion, con los indices
    de ITK-SNAP del mismo punto al pie. Planilla nueva `r2_nivel_pico_revisor.csv` con `nivel_del_punto`;
    las instrucciones viejas quedan en `r2_nivel_pico_revisor.ANTERIOR.md`.
  - **Pendiente:** solo la revision y, con ella, decidir si el segundo corredor se reporta como **S2** o
    como **"el segundo corredor por debajo de S1"**.
- **RESULTADO DE LA REVISION (2026-09-22), y contesta la pregunta de raiz.** La autora juzgo los 18
  casos sobre las laminas con el punto del corredor marcado (`r2_nivel_pico_revisor.csv`):

  | Nivel juzgado | n | Profundidad bajo S1 (mm): min / mediana / max | Diametro mediano |
  |---|---|---|---|
  | **S2** | **13** | -39 / -30 / -24 | 8.8 mm |
  | **S3** | **4** | -54 / -40.5 / -33 | 7.4 mm |
  | **S4** | **1** | -51 | 3.8 mm |

  - **El pico inferior NO es S2.** Lo es en **13 de 18 (72%)**; en **5 de 18 (28%)** cae en S3 o mas
    caudal. **Llamarlo "corredor de S2" habria sido incorrecto en mas de uno de cada cuatro casos**, y
    era exactamente lo que este asistente propuso hacer en dos actualizaciones anteriores de esta misma
    implicancia. El supuesto no sobrevivio a la medicion.
  - **La profundidad predice pero no determina.** Un umbral en -32 mm acertaria en 17 de 18, pero hay
    una inversion real: `CLINIC_0093` a **-39 mm** es **S2** —*"al final de S2 casi en la union"*—
    mientras que casos a **-36** y **-33 mm** son **S3**. La altura sola no identifica el nivel, que es
    justo lo que la autora anticipo al preguntar por el sacro inclinado.
  - **El diametro acompana al nivel:** 8.8 mm en S2, 7.4 en S3, 3.8 en el S4. Cuanto mas caudal, mas
    estrecho. Es coherente con la anatomia y no se uso para juzgar.
  - **Un caso ilegible, y con motivo:** `CLINIC_0060`, juzgado S4, `legible = no`, comentario *"los
    huesos en esa parte parecen (en mi opinion estan) rotos"*. Diametro 3.8 mm, el menor de la muestra.
    Es un volumen de `dataset6`, sin osteosintesis, pero **no necesariamente sin fractura**.
- **DECISION QUE QUEDA, ahora con evidencia:** el segundo corredor se reporta como **"el segundo
  corredor por debajo de S1"**, sin atribuirle nivel vertebral, y se declara que en una muestra de 18
  casos cayo en S2 en 13, en S3 en 4 y en S4 en 1. **La opcion de etiquetarlo S2 queda descartada por
  medicion propia**, no por prudencia.
- **Consecuencia para D-O2.5 y para `main.tex`:** el documento promete hoy evaluar S2
  descriptivamente. Con esto, lo que se puede evaluar es **el segundo corredor**, que no es un nivel
  vertebral fijo. Hay que reescribir esa promesa. **No aplicado (reglas 4 y 14).**
- **Higiene de datos, aplicada:** la planilla venia en cp1252; reescrita en UTF-8, original en
  `r2_nivel_pico_revisor.raw.csv`. Las columnas de juicio quedaron intactas.
- **APLICADO a `tesis/main.tex` el 2026-09-23, por peticion explicita** (regla 4). Cuatro ediciones:
  1. *Problem Statement*: *"S2 placements are evaluated descriptively"* -> *"placements in the second
     osseous corridor below S1"*.
  2. *Objetivos*: parrafo nuevo con el hallazgo medido —13 / 4 / 1 en S2 / S3 / S4, profundidades
     medianas de 30, 40.5 y 51 mm, diametros medianos de 8.8, 7.4 y 3.8 mm, y la inversion del caso a
     39 mm— y la frase que lo ata al argumento que el texto ya hacia: **medir cada corredor sobre la
     anatomia individual en vez de asumir una jerarquia universal de nivel**.
  3. *Tabla de Expected Results*: la fila deja de hablar de S2 y declara que el nivel vertebral del
     segundo corredor **no es constante**.
  4. **Correccion de una frase propia del 2026-09-22**: el parrafo de resultados decia que la anatomia
     receptora *"is unfractured"*. No esta verificado: la cohorte se selecciono **sin osteosintesis**,
     que no es lo mismo. Reescrito como *"selected as free of osteosynthesis rather than verified as
     free of fracture"*. Lo motivo `CLINIC_0060` (ver #125).
- **Verificacion:** `verificar_coherencia.py` recomputa desde `r2_nivel_pico_revisor.csv` los recuentos,
  las tres profundidades medianas, los tres diametros medianos y la inversion, y comprueba que
  `main.tex` los declare. **94/94 comprobaciones pasan.** Compila: 0 errores, 0 citas indefinidas,
  8 paginas.
- **Estado: CERRADA.**
- **En los tres casos el resultado principal del Objetivo 2 no se toca.**
- **Tipo:** ALCANCE + DATO. **No aplicado (reglas 3, 4 y 14): la eleccion es de la autora.**

## Ronda 2026-09-22 (2) — primera corrida del Objetivo 2 (job 52175)

### 122 — En **15 de 72** pelvis de la cohorte el corredor medido es mas estrecho que el tornillo del benchmark, asi que el eje ideal YA perfora: parte de la distancia a Zwingmann es anatomica, no del muestreador — **CERRADA el 2026-09-22** (opcion (a)+(b) adoptada y aplicada)

- **Origen:** primera corrida de E13 sobre la cohorte (job 52175, Khipu, 2026-09-22). Lo destapo el
  control de pose sin perturbar, que reporto **15 de 72** casos "fallando".
  *[corregido 2026-10-05, ver #140]*
- **Los 16 no son un fallo de la metrica. El control estaba mal especificado.** Verificado:
  - `procesar()` calculaba el control con un cilindro de **7.0 mm** (`sap.D_SAP_MM`) en vez de con
    `D_TS_max`. La identidad garantizada por construccion es *"cilindro de diametro `D_TS_max` sobre el
    eje del corredor => brecha 0"*, porque `D_TS_max` es `2 x min` del EDT **sobre ese mismo eje**.
    A 7.0 mm no hay ninguna identidad que exigir.
  - Los 16 casos coinciden casi exactamente con los **15** que tienen `D_TS_max < 7.0 mm`; el
    decimosexto (`dataset6_CLINIC_0018_data`) tiene `D_TS_max = 7.0` redondeado a un decimal.
  - La brecha medida sigue el orden de magnitud geometrico esperado `(7.0 - D_TS) / 2`: por ejemplo
    `D_TS = 2.0` -> brecha 2.48 (predicho 2.50); `D_TS = 4.8` -> 1.33 (1.10); `D_TS = 6.4` -> 0.25 (0.30).
- **El hallazgo real, y va al argumento de la tesis:** en **20.8% de la cohorte (15/72)** el corredor no
  admite un tornillo de 7.0 mm **ni siquiera sobre su eje optimo**. Para esos pacientes el **grado 0 es
  anatomicamente inalcanzable al calibre del benchmark**. Por tanto **una parte de la distancia de
  Wasserstein-1 frente al brazo navegado (69% de grado 0) no la produce el muestreador: la produce la
  anatomia de la cohorte receptora.** Reportar el W1 sin decir esto atribuiria al muestreador un
  desajuste que es del emparejamiento cohorte-benchmark.
- **Conecta con una limitacion ya escrita en `main.tex`:** las distribuciones clinicas vienen de pelvis
  **fracturadas** (Tile B y C) operadas, mientras que los corredores de aqui se miden en pelvis **sin
  osteosintesis**. La #122 anade la direccion que faltaba: la cohorte receptora local tiene, ademas,
  corredores estrechos en una fraccion no despreciable.
- **Lo que NO cambia:** las cifras de distribucion y de Wasserstein-1 de la corrida 52175 **son validas**.
  Nada se excluyo: `resumen()` calculaba la distribucion sobre **todas** las poses, pese a que su texto
  decia "sus cifras no se usan". Esa frase era falsa y esta corregida.
- **Y excluirlos habria sido un error**, no un descuido afortunado: `zwingmann2009navigated` graduo
  **todos** sus tornillos y no excluyo pacientes por anatomia estrecha. Quitar aqui los corredores
  estrechos habria subido artificialmente el porcentaje de grado 0 y bajado el W1 frente al brazo
  navegado, que es exactamente el sesgo que D-O2.1 y #120 existen para impedir.
- **Aplicado el 2026-09-22:** (i) el control de `procesar()` pasa a usar `D_TS_max`; (ii) se anade
  `corredor_estrecho` y la brecha del eje ideal a 7.0 mm como **dato anatomico reportado**, no como
  fallo; (iii) `resumen()` deja de afirmar que excluye casos; (iv) los dos `.md` de la corrida llevan
  una nota de correccion al inicio; (v) `verificar_coherencia.py` comprueba ambas cosas (41/41).
- **Opciones para el informe:**
  - (a) **Reportar el W1 tal cual y declarar la fraccion de corredores estrechos junto a el**, como
    limitacion del emparejamiento cohorte-benchmark.
  - (b) Reportar ademas el W1 **estratificado** por `D_TS_max >= 7.0` frente a `< 7.0`, para separar lo
    que aporta la anatomia de lo que aporta el muestreador.
  - (c) Restringir la cohorte a los corredores viables. **No recomendada:** seleccionar pacientes por
    una variable correlacionada con el resultado es justo lo que el parrafo anterior dice que no se hace.
- **Recomendacion del asistente: (a) + (b).** (b) es barato —una particion del CSV ya existente, sin
  volver a Khipu— y es lo unico que permite decir cuanto del desajuste es del muestreador. (c) queda
  descartada por la misma razon que se descarto calibrar contra el benchmark.
- **(b) YA CALCULADA** (`e13b_estratificado.py` / `.md`, analisis **post hoc declarado**, calibre
  7.0 mm). La separacion es nitida y se reproduce en las dos cohortes:

  | Cohorte | estrato | n poses | g0/g1/g2/g3 (%) | W1 navegado | W1 convencional |
  |---|---|---|---|---|---|
  | 72 | todos (preinscrito) | 3600 | 51.5 / 31.4 / 11.1 / 6.0 | **0.206** | 0.230 |
  | 72 | `D_TS >= 7.0` (57 casos) | 2850 | 64.2 / 27.5 / 6.1 / 2.2 | **0.183** | 0.482 |
  | 72 | `D_TS < 7.0` (15 casos) | 750 | 3.3 / 46.4 / 30.0 / 20.3 | **1.122** | 0.727 |
  | 49 | todos (preinscrito) | 2450 | 54.9 / 30.4 / 9.9 / 4.8 | **0.186** | 0.299 |
  | 49 | `D_TS >= 7.0` (41 casos) | 2050 | 64.6 / 26.6 / 6.6 / 2.1 | **0.175** | 0.483 |
  | 49 | `D_TS < 7.0` (8 casos) | 400 | 5.2 / 49.5 / 26.5 / 18.8 | **1.037** | 0.643 |

- **Lo que dice esa tabla.** En corredores que admiten el calibre del benchmark, el muestreador produce
  **64.2%** de grado 0 frente al **69%** del brazo navegado de Zwingmann, con `W1 = 0.183`; la cifra se
  reproduce casi identica en la cohorte de sensibilidad (**64.6%**, `W1 = 0.175`), lo que indica que no
  es un artefacto de composicion. En los corredores estrechos el grado 0 practicamente desaparece
  (**3.3%**) y el W1 frente al navegado se dispara a **1.122**. **La cifra agregada es una mezcla de dos
  poblaciones distintas**, y su parecido con el brazo **convencional** (`W1 = 0.230`) es en buena parte
  un efecto de esa mezcla: dentro del estrato viable, la distancia al brazo convencional es **0.482**.
- **Consecuencia para la redaccion:** el W1 agregado **no se puede presentar como medida limpia del
  muestreador**, y tampoco se puede sustituir por el del estrato viable, que seria seleccion por una
  variable correlacionada con el resultado. Se reportan **los dos**, con la cifra preinscrita como
  principal y la estratificacion declarada como post hoc.
- **Tipo:** RESULTADO + INTERPRETACION.
- **DECISION DE LA AUTORA (2026-09-22, en chat):** se adopta **(a)+(b)**.
- **APLICADO a `tesis/main.tex` el 2026-09-22, por peticion explicita** (regla 4): la fila
  *Surgical Admissibility* pasa a **executed** con la cifra preinscrita de las dos cohortes, y se anade
  el parrafo *Placement result, and what the aggregate distance does and does not measure*, que trae la
  estratificacion **declarada como post hoc**, la fraccion de corredores estrechos, el motivo por el que
  **no** se restringe la cohorte, y el enlace con la limitacion ya escrita sobre pelvis fracturadas
  frente a intactas. Compila: 0 errores, 0 citas indefinidas, 8 paginas.
- **Verificacion:** `verificar_coherencia.py` recomputa desde `e13_poses.csv` y `e13_poses_g3.csv`
  **todas** las cifras que `main.tex` afirma —distribuciones, los seis Wasserstein-1, recuentos de casos
  viables y estrechos— y comprueba que el texto las declara. **78/78 comprobaciones pasan.**
- **Estado: CERRADA.**

### 123 — La decision del recorte de 6 mm tenia una condicion de reapertura sin evaluar — **CERRADA el 2026-10-04**: evaluada en #131, 0 de 16 `fallo_6mm`, el recorte se mantiene

- **Origen:** inventario del directorio `experiments/objetivo2/` para escribir `EXPERIMENTOS.md`,
  2026-09-22. No sale de un paper ni de un experimento: sale de contar columnas vacias.
- **Hallazgo, verificado:** `e9ts_revision_laminas_autora.csv` tiene **16 filas y las columnas
  `veredicto` y `nota` completamente vacias**. Su documento, `e9ts_revision_laminas.md`, dice literal:
  *"Condicion de reapertura de la decision 2026-09-14 (4): el recorte de 6 mm se mantiene como
  principal salvo que esta revision muestre un fallo suyo."*
- **Por que importa y no es gestion:** **todo** el Objetivo 2 se calcula sobre `default6mm`. La cohorte
  de 72, el `D_TS_max` de cada caso, la longitud del implante, la pose base, los 3 600 grados de brecha
  y los dos Wasserstein-1 que ya estan escritos en `main.tex` salen de ese recorte. La decision que lo
  fijo se tomo **condicionada** a una revision que no se hizo, asi que la condicion sigue **sin
  verificar**.
- **Que tan grande es el efecto, con lo ya medido:** `e9ts_resumen.md` da las dos variantes sobre la
  cohorte de 72. `default6mm`: D mediana **9.5 mm**, **40.3%** pasa 10 mm, **65.3%** con `d=6.5, c=1`.
  `robust3mm`: **9.4 mm**, **37.5%**, **62.5%**. Las diferencias agregadas son pequenas. **Pero la
  revision no se preparo sobre agregados:** los 16 casos son justamente aquellos donde
  `|D_TS(6 mm) - D_TS(3 mm)| >= 1 mm`, mas dos con cajas desplazadas mas de 10 mm (#49). El efecto por
  caso puede ser grande aunque la mediana no se mueva, y por caso es como entra en SAP.
- **Lo que NO se puede concluir:** que las cifras esten mal. No hay evidencia de eso. Lo que hay es una
  **condicion declarada y no comprobada**, que es distinto.
- **Opciones:**
  - (a) **Llenar la revision de los 16 casos.** Las laminas ya existen (`outputs/e9ts/laminas/` y
    `outputs/e9ts_3mm/laminas/`) y la planilla tambien. Es mirar 16 pares de imagenes.
  - (b) **Correr SAP con `robust3mm`** sobre la cohorte y reportar la diferencia como sensibilidad del
    recorte. No necesita revisor, pero si una corrida de Khipu y una preinscripcion de la sensibilidad.
  - (c) Declarar la condicion como no evaluada y decirlo en la limitacion del documento.
- **Recomendacion del asistente: (a), y es barata.** Son 16 casos con las laminas ya generadas; cierra
  una condicion que la propia autora escribio. (b) es el respaldo cuantitativo si (a) levanta dudas.
  (c) sola no basta: una condicion de reapertura que se declara incumplida sin mirarla, teniendo las
  imagenes en disco, es dificil de defender.
- **Por que no se vio antes:** nada en el repositorio distinguia una planilla llena de una vacia, ni una
  pendiente de una superada. `EXPERIMENTOS.md` existe para que esto no vuelva a pasar.
- **ACTUALIZACION 2026-09-23: la revision tenia un criterio que habria producido fallos falsos.**
  Al actualizar `e9ts_revision_laminas.md` se encontro que pedia comprobar que *"el corredor esta a la
  altura de S1, no en S2 ni en L5"*. **Ese criterio contradice lo medido despues** y se retiro:
  - El **mejor corredor global** de la cohorte de 72 esta a una mediana de **-20 mm** del punto de S1
    (p10 -33, p90 -9), y **36 de 72 casos** lo tienen a mas de 20 mm por debajo.
  - La revision de #121 mostro que corredores a **-24 mm** ya se juzgan **S2**, y que la profundidad no
    determina el nivel (un S2 a -39 mm frente a S3 a -36 y -33 mm).
  Con el criterio antiguo, **la mitad de la cohorte tendria un "fallo" de nivel que no es tal**. Si la
  revision se hubiera hecho en su momento, habria producido falsos positivos justo en la variable que
  #121 acaba de demostrar que es variable. El nivel pasa a anotarse en `nota`, no a puntuarse.
- **Otros dos cambios, de forma, aplicados el 2026-09-23:** las rutas del CSV estaban referidas a la
  raiz del repositorio mientras las otras dos revisiones las refieren a `experiments/objetivo2/`;
  unificadas, 48 de 48 resuelven. Y se anadio la columna `revisor`, que no existia; el original quedo
  en `e9ts_revision_laminas_autora.sin_revisor.csv`.
- **Lo demas de la especificacion de 2026-09-14 sigue siendo correcto:** los 16 casos, los tres paneles,
  las cinco categorias de `veredicto` y la advertencia de #19/#21.
- **PROPUESTA DEL AGENTE (2026-09-23), que NO cierra la condicion.** El subagente
  `revisor-laminas-corredor` reviso los 16 casos y escribio `e9ts_revision_laminas_agente.csv`:
  **14 `ok`, 2 `fallo_3mm`, 0 `fallo_6mm`, 0 `dudoso`**. Los dos fallos son `CLINIC_0076` y
  `CLINIC_0022`, y en ambos la region perdida lo es en el recorte de **3 mm**, no en el de 6 mm; la
  evidencia que cita es la fila 3 de la lamina de mascaras, donde esa region aparece solo en azul.
  - **Apunta a que la decision 2026-09-14 (4) no se reabre**, porque el unico veredicto que la reabriria
    es `fallo_6mm` y no hay ninguno.
  - **Pero no la cierra, por tres razones.** (i) Es una **propuesta**: la revision de la autora sigue en
    **0 de 16** y es la que vale. (ii) **Cero `dudoso` en 16 casos visuales es sospechoso**: las
    instrucciones lo invitaban explicitamente y el agente no lo uso ni una vez; un revisor que nunca
    duda sobre cortes sueltos esta siendo optimista, no preciso. (iii) `ok` significa *"no veo error en
    estos cortes"*, y las laminas **no demuestran ausencia** (#19, #21).
  - **La condicion se cierra cuando la autora revise y se comparen las dos**, como se hizo en R1 entre
    el agente y el revisor clinico (0.908 exacto, kappa 0.81). Los desacuerdos son los casos a mirar dos
    veces.
  - Higiene: el CSV venia en cp1252, reescrito en UTF-8; original en
    `e9ts_revision_laminas_agente.raw.csv`. `e9ts_revision_laminas_autora.csv` **intacto**, verificado.
- **Tipo:** METODO + VERIFICACION PENDIENTE. Toca la decision del 2026-09-14 (4) y, si (a) o (b) mueven
  algo, las cifras del Objetivo 2. **No aplicado (reglas 3, 4 y 14).**

### 124 — Segunda lectura independiente del nivel de S1 sobre laminas: 61 de 61 de acuerdo con la revision del ORL — **CERRADA el 2026-10-04** (opcion (b) aplicada a `main.tex`)

- **Origen:** revision de `r1_revision_laminas_revisor.csv`, llenada por la autora el 2026-09-22 sobre
  las 61 laminas alargadas.
- **Resultado bruto:** 61 de 61 llenas. Distribucion **ok 51, +1 7, otro 2, ? 1**, que reproduce
  **exactamente** la del revisor clinico ORL de 2026-09-11 (`r1_landmarks.md:45`: ok 51, +1 7, otro 2,
  ? 1, mas 4 "no hallado" que no estan en este subconjunto). Tabla cruzada: **todo en la diagonal, 61
  de 61, acuerdo exacto 100%**.
- **RECTIFICACION (2026-09-22).** Este asistente concluyo primero que la lectura **no** era
  independiente, porque tres comentarios son identicos palabra por palabra a los de 2026-09-11. **Era
  una inferencia equivocada.** La autora lo aclaro en el chat: *"primero llene los juicio_nivel,
  verifique por mi cuenta si concordaban con el pasado (y si), y como eran iguales anadi exactamente
  los mismos comentarios adrede"*. Es decir, el **orden fue juicio -> comparacion -> copia deliberada
  del comentario**, no al reves. Los juicios **si** son una segunda lectura independiente. Queda
  registrado por la regla 17: es la segunda vez en la sesion que el asistente infiere procedencia de un
  artefacto en vez de preguntarla.
- **Lo que por tanto SI se puede afirmar:** una **segunda lectura independiente** del nivel de S1 sobre
  las 61 laminas coincide con la del revisor clinico en **61 de 61 casos**, categoria por categoria.
  Como contraste, el agente automatico sobre los mismos casos daba 0.908 exacto y kappa 0.81
  (`r1_landmarks.md:47`).
- **Los dos limites que conviene conservar al redactarlo:**
  1. **Los comentarios no son evidencia independiente**: se copiaron a proposito una vez comprobada la
     coincidencia, y la propia autora lo declara. Solo los **juicios** lo son.
  2. **El segundo lector es la autora, no un segundo clinico.** Es una segunda lectura, no una segunda
     opinion clinica, y asi debe describirse si llega al documento.
- **Lo que la relectura SI aporta, y no es poco:**
  - **El formato funciona:** 60 de 61 casos legibles sobre lamina, sin abrir ITK-SNAP. Cierra la
    objecion del revisor de 2026-09-14 al mosaico de +-60 mm.
  - **Dos observaciones nuevas** que no estaban en 2026-09-11: `metal_0019`, marcado `ok`, lleva ahora
    *"aunque ligeramente cae en el pediculo"*; y `metal_0015` aporta un **candidato concreto de
    correccion** hallado en ITK-SNAP, S1 en **(277-350-114)**, con `legible = no`.
  - **Un modo de fallo del detector, ahora con texto:** en `metal_0035` el punto cae *"mas en la parte
    lateral que en la parte superior"*, y en `metal_0046` y `metal_0058` la cruz esta sobre los
    **ligamentos sacroiliacos posteriores**. Son tres casos del mismo tipo de error, no tres errores
    distintos.
- **Impacto en las cifras de `main.tex`: NINGUNO, verificado.** `metal_0015` ya tiene
  `marco_computable = False` en `r1_estados.csv`, asi que el candidato de correccion afecta a un caso
  que ya estaba fuera del recuento de 48. Las cifras de 48 y 29 no se mueven.
- **Lo que `main.tex` dice hoy sigue siendo exacto:** *"a clinician reviewer (one surgeon,
  otorhinolaryngology), blinded to the automatic audit, confirmed the S1 level on every patient"*. Esa
  frase describe la revision de 2026-09-11 y no se toca. El riesgo es solo anadir un segundo lector que
  no existe.
- **Opciones:** (a) dejar `main.tex` como esta y guardar la segunda lectura como respaldo interno;
  (b) anadir una frase declarando el acuerdo de 61 de 61 entre el revisor clinico y una segunda lectura
  de la autora, con los dos limites de arriba explicitos.
- **Recomendacion: (b), en una sola frase.** El acuerdo es real y refuerza el unico punto del marco de
  referencia que depende de juicio humano; ocultarlo seria desaprovechar trabajo hecho. Pero tiene que
  decir **quien** es el segundo lector y que los comentarios no son independientes, o pasa a afirmar de
  mas.
- **DECISION DE LA AUTORA (2026-10-04):** se adopta **(b)**.
- **APLICADO a `tesis/main.tex`**, por peticion explicita (regla 4), en el parrafo de la limitacion de
  campo: una frase que declara el acuerdo **61 de 61** y, en la misma oracion, los dos limites —que el
  segundo lector es **la autora y no un segundo clinico**, y que **solo los juicios de nivel son
  independientes**, porque las notas se copiaron una vez vista la coincidencia—. Compila: 0 errores,
  0 citas indefinidas, 8 paginas.
- **Estado: CERRADA.**
- **Nota de higiene de datos, ya aplicada:** la planilla venia en **cp1252** y con cinco textos libres
  escritos en la columna `vertebra_transicion`, que solo admite `si`/`no`/`?`. Se movieron a
  `comentario`, se guardo en UTF-8 y el original quedo en `r1_revision_laminas_revisor.raw.csv`.
- **Tipo:** REDACCION + PROCEDENCIA. **No aplicado a `tesis/main.tex` (regla 14).**

### 125 — `CLINIC_0060` tiene fractura CONFIRMADA y esta entre los 15 corredores estrechos de #122; la cohorte nunca se verifico libre de fractura, solo libre de osteosintesis — **CERRADA el 2026-10-04** por el cribado de #132

- **Origen:** revision del segundo corredor, 2026-09-22. La revisora juzgo `dataset6_CLINIC_0060_data`
  como S4 con `legible = no` y comento: *"los huesos en esa parte parecen (en mi opinion estan) rotos"*.
  Es el corredor mas estrecho de la muestra, **3.8 mm**.
- **CONFIRMADO el 2026-09-23.** Un medico **recien licenciado y sin especialidad** confirmo que
  `CLINIC_0060` tiene fractura. Es una confirmacion real y se cuenta como tal, pero **no es lectura de
  radiologo ni de traumatologo**, y esa salvedad debe acompanar a cualquier cifra que se derive.
- **Y el caso confirmado cae DENTRO del grupo que hace dudar de #122.** `CLINIC_0060` tiene
  `D_TS_max = 6.2 mm`, asi que **es uno de los 15 corredores estrechos** que #122 atribuye hoy a
  variabilidad anatomica. La otra sospecha abierta, `CLINIC_0022` (fragmentos separados de sacro o S1,
  E10b/#49), tiene **4.7 mm** y **tambien** esta en ese grupo. `CLINIC_0043`, la tercera candidata,
  tiene 11.7 mm y no lo esta.
- **Eso convierte la duda en una hipotesis comprobable:** si la fractura se concentra en los corredores
  estrechos, parte de lo que `main.tex` presenta como anatomia es patologia no detectada.
- **El hallazgo de fondo no depende de ese caso.** El criterio con el que se construyo la cohorte del
  Objetivo 2 es **ausencia de osteosintesis** (#52 a), no ausencia de fractura. Nadie verifico lo
  segundo, ni caso por caso ni por muestreo. `dataset6` es la particion sin metal de CTPelvic1K, y eso
  no garantiza pelvis intacta.
- **Aplicado a `main.tex` el 2026-09-23:** la frase del parrafo de resultados que decia que la anatomia
  receptora *"is unfractured"* —escrita por este asistente el 2026-09-22— pasa a *"selected as free of
  osteosynthesis rather than verified as free of fracture"*. Era una afirmacion mas fuerte que la
  evidencia, del mismo tipo que las otras de esta sesion.
- **Por que puede importar mas que un caso:** `reilly2003effect`, ya citado en `main.tex`, midio que
  5-20 mm de desplazamiento craneal de una fractura de zona II reducen el area disponible para tornillos
  iliosacros en S1 **entre 36% y 90%**. Si hubiera fracturas no detectadas en la cohorte receptora,
  sus corredores estarian estrechados por la misma razon, y eso **confunde parcialmente** el hallazgo de
  #122 —los 15 de 72 corredores mas estrechos que el calibre del benchmark— con una causa distinta de
  la variabilidad anatomica normal.
- **Opciones:** (a) esperar la confirmacion de `CLINIC_0060` y, si es fractura, revisar los corredores
  mas estrechos de la cohorte en busca de mas casos; (b) revisar de entrada los 15 casos estrechos de
  #122, que son donde la hipotesis se juega; (c) declarar la limitacion sin mirar.
- **Recomendacion del asistente: (b), y ya esta preparada.** Con una correccion de diseno respecto de
  lo que propuse ayer: **mirar solo los 15 estrechos no contesta la pregunta**. Si aparecieran tres
  fracturas no se sabria si es mucho o poco, porque falta la tasa de fondo de la coleccion. Por eso el
  cribado lleva **grupo de comparacion y es ciego**:
  - `r3_fractura_revisor.csv`: **30 casos barajados**, 15 estrechos (todos los que hay) y 15 de control
    tomados al azar de los 57 viables, **sin decir a que grupo pertenece ninguno**. Semilla 20260923.
  - El reparto esta en `r3_fractura_grupos.csv`, que **no se entrega** y solo se abre al analizar.
  - Instrucciones en `r3_fractura_revisor.md`. Las **60 laminas** ya existen en disco.
  - Columnas: `revisor` (pide especialidad a proposito), `fractura` (`si`/`no`/`dudoso`), `donde`,
    `legible`, `comentario`.
- **Las tres salidas posibles son reportables:** sin fractura en ninguno de los dos grupos, #122 se
  reporta como esta; concentrada en los estrechos, cambia la interpretacion de #122 y es un resultado;
  repartida por igual, es tasa de fondo de CTPelvic1K y se declara como limitacion.
- **Tipo:** DATO + LIMITACION. **No aplicado a `00-tesis.md` ni al criterio de cohorte (reglas 3 y 14).**

---

### 116 — ACTUALIZACION (2026-09-24): la mitad del minimo viable ya tiene codigo; la otra mitad del diagnostico sigue en pie, literal

- **Origen:** revision de estado pedida por la autora, 2026-09-24 (asistente en rol de asesor). Verificado
  contra disco, no inferido.
- **Lo que ya NO se sostiene de la #116 original:**
  - `src/muestreador/` **no esta vacio**: `sap.py` (469 lineas, 17 funciones) y `muestreo.py` (125 lineas).
  - **SAP existe, corre y produjo resultado**: corrida 52175, dos cohortes, escrita en `main.tex`.
  - El minimo viable **Obj 1 + Obj 2 + SAP** esta, por tanto, ejecutado y redactado.
- **Lo que sigue exactamente igual, comprobado hoy:**
  - `muestrea_ddim` (`src/renderizador/difusion.py:93`) **sigue sin un solo llamador** en todo el arbol
    (`grep -rn "muestrea_ddim" --include=*.py --include=*.sbatch`, un unico acierto: la propia definicion).
    **El proyecto no ha generado ninguna muestra sintetica.**
  - El unico `ckpt.pt` es el del piloto de 200 pasos (`outputs/a2/pasos200_20260921_074236`), declarado
    en su propio log: *"corrida NO preinscrita. Es piloto de medicion (#89), no resultado de tesis."*
  - El banco de geometrias de implante sigue **PENDIENTE DE DEFINIR** (CLAUDE.md; #97, #99).
- **Consecuencia sobre la priorizacion, que es lo que cambia:** el argumento de la #116 original era
  *"el camino critico es el minimo viable"*. Ese argumento **ya se consumio**. El camino critico hoy es
  el **pegamento del Obj 3** —geometria -> pose -> mascara -> render -> metrica—, del que solo existe el
  cuarto eslabon. El entrenamiento **no es el cuello de botella**: el piloto midio 0.106 s/paso y 3.4 GB
  en A6000, y extrapola a **0.9 h para 30 000 pasos**.
- **Sigue ABIERTA.** No se cierra porque su afirmacion central —cero muestras sinteticas, contribucion de
  apariencia sin observar— es verdadera hoy. Lo que caduco es el inventario de `src/muestreador/`.
- **Tipo:** ALCANCE + PLAN DE TRABAJO. **No aplicado a `main.tex` ni a `00-tesis.md` (reglas 4 y 14).**

---

## Ronda 2026-09-29 — arranque del documento de entrega (`overleaf/`)

### 126 — El documento que se entrega a la universidad (`overleaf/`) contradice el alcance vigente: titulo, introduccion y datos de portada — ABIERTA

- **Origen:** lectura de `overleaf/` para montar el ciclo de redaccion, 2026-09-29. Verificado contra
  disco.
- **Lo que dice hoy `overleaf/`, y por que choca:**
  - **Titulo** (`overleaf/main.tex:49`): *"...mediante difusion condicionada para aumento de datos en
    segmentacion osea"*. La mejora downstream esta **fuera de alcance** (punto 1 de `Fuera de alcance`,
    `docs/00-tesis.md`; `tesis/main.tex`, *"Downstream segmentation impact is deliberately excluded"*).
    El titulo vigente en `docs/00-tesis.md` es otro (*Multi-Window Image-Domain Diffusion*).
  - **Introduccion** (`overleaf/secciones/introduccion.tex`): la pregunta, el objetivo general y el
    objetivo especifico 4 prometen **DSC y HD95** sobre casos reales con metal; el metodo es **2D** y
    **difusion latente con ControlNet**. Las tres cosas quedaron retiradas: #1 fuera de alcance, No-Go del
    Objetivo 1 (#91) y rediseno del Objetivo 3 al dominio de imagen (decision 2026-09-19 pto 4).
  - **Portada:** el asesor figura como *"Victor"* sin apellido y los dos ORCID son `0000-0000-0000-0000`;
    la plantilla declara el ORCID **obligatorio**.
- **Consecuencia para la redaccion:** la introduccion se reescribe desde `tesis/main.tex` y su texto
  actual **no** se usa como fuente (marcada DESFASADO en `redaccion/MAPA.md`). El titulo y la portada no
  los decide el asistente.
- **Que falta decidir (autora):** (a) titulo en espanol del documento de entrega; (b) si el titulo menciona
  la motivacion (aumento de datos) o solo lo que se evalua (coherencia fisica y quirurgica); (c) nombre
  completo y ORCID del asesor, y ORCID propio.
- **Tipo:** REDACCION + ALCANCE. **No aplicado: `overleaf/main.tex` conserva titulo y portada (regla 14).**

### 127 — La redaccion del capitulo 3 (`overleaf/`) destapo contradicciones entre decisiones, corridas y `tesis/main.tex` — ABIERTA

Origen: `/ciclo-redaccion capitulo3`, rondas r01-r02 (2026-09-29). Detalle en
`redaccion/rondas/capitulo3-r01-respuesta.md` y `capitulo3-r02-respuesta.md`. Hoy todo entra al capitulo como `\GAPDEC`.

1. **SAP, componente de viabilidad (T01):** D-O2.4 fija la envolvente en 6.5-8.0 mm para `D >= d + 2c`, pero `e13_sap.md` se corrio con 4.91 / 7.0 / 7.3 mm y 1 mm de holgura. Hay que decidir cual se reporta.
2. **SAP, fraccion por zona de densidad (T03):** D-O2.6 la calcula sobre E9b, pero la decision del 2026-09-14 (#50) retiro E9b como evidencia de densidad. Falta definir la fraccion por pose.
3. **Obj 3, prueba primaria (guia-1, r02):** el Wilcoxon de *streak amplitude* contra copia y pegado no puede fallar, porque la copia no produce rayas por construccion. Hay que decir que resultado cuenta como fallo, o si la prueba decisiva es la TOST contra el protocolo fisico.
4. **Obj 1, preinscripcion (guia-3, r02):** la regla de la compuerta se escribio despues de una exploracion sobre la cohorte completa, incluidos los 34 de prueba. Toca la validez que se afirma para la preinscripcion.
5. **`tesis/main.tex` desfasado:**
   - :78 y :117 contradicen D-O2.6 y D3 (densidad y cabeza del tornillo);
   - :52 y :123 usan el criterio de 10 mm, sustituido por #31;
   - :77 dice "fixed before any run" y "latent route is abandoned";
   - la frase de :121 sobre el truncamiento no cuadra con su propio embudo (7 frente a 19).
6. **Obj 2 sin regla de decision y Obj 4 sin evidencia experimental** (guia-2 y guia-3, r01). Tambien siguen abiertos h = 2 sigma, la agregacion por paciente y el tamano del brazo fisico.
7. **Supuesto no verificado (guia-3, r03):** el sintetizador se entrena con todo el material ortopedico (placas, protesis) y sintetiza solo tornillos. Eso supone que la relacion entre mascara y artefacto no depende del tipo de implante. El capitulo lo declara como amenaza a la validez de constructo (dato: 5 de 40 componentes revisados eran tornillos, DEC 2026-09-21).
8. **`tesis/main.tex:117`:** dice "more than a factor of two", pero en el extremo de 6.5 mm la razon de secciones frente a 4.91 mm es de aproximadamente 1.75 (S01, r03).
9. **Cohorte de sensibilidad del Obj 2:** ninguna fuente dice por que son solo los pacientes del grupo 3 (guia-9, r03).
10. **Exclusion de extremos de 8 mm (T02, r04):** D-O2.3 justifica excluir los extremos al medir el corredor y el tramo $T$ de SAP, pero no justifica el valor de 8 mm. Si es una convencion propia, hay que declararlo.
11. **Viabilidad con dos papeles (guia-5, r04):** en el capitulo 3 aparece como caracterizacion de la cohorte (l.91) y como variable dependiente descriptiva del Obj 2. Hay que decidir cual queda.
12. **S1 en la serie navegada (guia-3, r04):** esta decidido (#69, DEC 2026-09-17 C) y ahora figura como supuesto en validez de constructo. Para justificarlo hace falta una frase de `zwingmann2009navigated` que la ficha no trae; la ficha solo tiene la del criterio de evaluacion. Revisar el PDF via `lector-papers`.
13. **La envolvente osea implementada no es la decidida (T01, r05):** D-O2.3 (pto 1) fija un cierre de 2 mm mas el relleno de cavidades cerradas en 3D. El codigo que midio el corredor (`e9ts_corredor.py`:307-308) y el que corrio SAP (`e12_sap_control.py`:111-112, importado por `e13_muestreo_sap.py`) solo aplican el cierre. El relleno solo existe en `e9_corredor.py`:99, la version por umbral de HU que ya se reemplazo. Hay que decidir si se corrige el texto de la decision o se vuelve a correr E9-TS, E12 y E13 con relleno. Mientras tanto, las cifras del corredor y de SAP corresponden a la envolvente sin relleno.

    **MEDICION (2026-10-03), sobre los dos casos piloto con mascaras en disco.** El relleno es
    practicamente un no-op sobre mascaras de TotalSegmentator:

    | Caso | voxeles del hueso cerrado | anade el relleno | D_TS sin relleno -> con relleno |
    |---|---|---|---|
    | `CLINIC_0002` | 1 186 638 | **0** (0.000 %) | 9.158 -> **9.158** mm |
    | `metal_0008` | 1 565 517 | **394** (0.025 %, 0.17 cm3) | 11.288 -> **11.288** mm |

    **Y hay una razon de construccion, no una casualidad.** El comentario de `e9_corredor.py`:95-98 dice
    por que existe el relleno ahi: *"El esponjoso del sacro y del ilion puede quedar bajo 150 HU: sin
    rellenar, la mascara es un cascaron cortical y el corredor sale de 1-3 mm"*. Es decir, el relleno
    corrige el **hueco trabecular de una mascara por umbral de HU**. Las etiquetas de TotalSegmentator
    son volumenes solidos: no hay cascaron que rellenar. El mismo comentario anade que *"el conducto
    sacro y los foramenes se comunican con el exterior y no se rellenan"*, asi que el escenario de que
    el relleno tape el canal o un foramen **no puede darse** con `binary_fill_holes`, que solo rellena
    cavidades cerradas.

    **Lectura:** D-O2.3 describe la envolvente de `e9_corredor.recortar` (la via por umbral de HU,
    reemplazada por #48) y nunca describio la de E9-TS. Es un **defecto de documentacion**, no de
    implementacion, y la opcion "corregir el texto de la decision" tiene respaldo empirico.

    **Limite de esta medicion, y es importante:** son **2 casos de 152**. No se puede generalizar desde
    ahi —el proyecto ya tiene registrado ese error de metodo—. Lo que falta es barato: un trabajo de
    Khipu que, por caso, cuente los voxeles que anade el relleno y recalcule `D_TS` **sobre el eje ya
    guardado**, sin rehacer la busqueda de corredor. Si el maximo sobre los 152 sigue siendo
    despreciable, se corrige el texto; si algun caso se mueve, ese caso —y solo ese— justifica la
    corrida de sensibilidad completa.

    **Coste real, medido en el log del job 51505:** E9-TS entero (152 casos, todas las variantes,
    16 CPU) tardo **6 min 39 s de reloj**, no 1.34 h; esa cifra es la **suma de CPU**, no el tiempo de
    pared. E13 sobre las dos cohortes son ~32 min. El diagnostico de arriba es mas barato que ambos.
14. **Regiones de medicion de rayas (guia-2, r05):** la banda $B_\delta$ trunca a proposito las rayas lejanas, y fuera de la banda el sintetizador da amplitud nula por construccion. El protocolo fisico, en cambio, genera rayas en todo el volumen. Si las regiones de *streak amplitude* se miden fuera de $B_\delta$, la comparacion con el protocolo fisico (TOST) queda sesgada en contra del sintetizador. El borrador `diseno_A.md` supone medir dentro de la banda, pero no esta preinscrito.
15. **Margen $\Delta$ (guia-1, r05):** no esta definido que cambia entre dos corridas repetidas del protocolo fisico (semilla de ruido o corrida completa).
16. **Evaluaciones sin metrica (guia-3, r05):** la diferencia entre mascara umbralizada y cilindro liso, la continuidad de los valores de TC en el borde de $B_\delta$ y el realismo frente a observaciones reales solo constan en el borrador `diseno_A.md`, sin preinscripcion.

### 128 — Al reescribir la introduccion (`overleaf/`) aparecieron eslabones del argumento que ninguna fuente del repositorio escribe — ABIERTA

Origen: `/ciclo-redaccion introduccion` (Objetivos, Justificacion y Alcance), rondas r01-r03, 2026-09-29/30. Detalle en `redaccion/rondas/introduccion-r0*-respuesta.md`. En el texto van como `\GAPDEC`; no se invento ninguna razon.

1. **Para que un sintetizador por difusion, si el protocolo fisico ya corre sobre las poses muestreadas (guia-1, r03):** el diseno del Obj 3 ejecuta el protocolo fisico de Peters et al. sobre las poses del muestreador. Entonces la tension "ningun enfoque produce a la vez poses clinicas y apariencia del artefacto" queda debilitada por el propio diseno. Falta la razon declarada (costo, validacion del simulador, otra). **Toca el argumento central de la tesis.** Salvedad (T01, introduccion r04): la implementacion y los resultados del protocolo fisico siguen como `\GAPDATO` en el cap. 3; lo que existe hoy es el diseno, no la corrida.
2. **Orden coherencia -> utilidad (guia-4, r01):** ni `tesis/main.tex` ni `docs/00-tesis.md` dicen por que la coherencia fisica y quirurgica debe establecerse antes de medir la utilidad para segmentacion. Tampoco dicen por que un implante sintetico aliviaria la escasez de volumenes con metal anotados.
3. **Contribucion no evaluada (guia-4, r02):** "el uso para la sintesis de la codificacion multiventana" figura como contribucion, pero ningun objetivo verifica su error de ida y vuelta sin autoencoder (ver #127.6).
4. **Contribucion en tension con el diseno (guia-2, r03):** la geometria parametrica "evita segmentar el metal con un umbral fijo de HU", pero el sintetizador se entrena con mascaras umbralizadas.
5. **Alcance: solo el tornillo iliosacro (guia-5, r03):** no hay razon declarada para excluir placas y otros tornillos. La coincidencia verificable es que la referencia clinica y el marco de Kaiser et al. solo cubren ese tornillo.
6. **Ablacion excluida sin objeto (r02):** "restriccion por restriccion" no enumera restricciones; el muestreador actual solo perturba el eje.
7. **Hipotesis ausente (r00):** la introduccion no enuncia hipotesis (G-A1). Su lugar es la Formulacion del problema, desfasada (#126).
8. **Como se enuncia el resultado del Obj 1 (guia-1, r05):** la introduccion lo presentaba como mecanismo ("los autoencoders se definen sobre rangos de intensidad que excluyen el hueso denso y el metal"), pero el diseno del Obj 1 solo mide si se supera el umbral de 25 HU. El texto ya se corrigio. Queda por decidir si esa explicacion del mecanismo se afirma en algun lugar de la tesis (cap. 4) y con que evidencia.

### 129 — La redaccion del capitulo 2 (`overleaf/`) encontro supuestos del Obj 1 y de la introduccion que el registro contradice — ABIERTA

Origen: `/ciclo-redaccion capitulo2`, rondas r01-r06 (2026-09-30). Detalle en `redaccion/rondas/capitulo2-r0*-respuesta.md` y `capitulo2-r0*-trazabilidad.md`. En el cap. 2 van como `\GAPDEC` o escalados; no se aplico nada fuera de esa seccion (regla 14).

1. **La ida y vuelta sin autoencoder SI esta medida (T01, r03):** `experiments/objetivo1/p1_compuerta.md`:31-38 (control de identidad, `pub+asinh`, 0.00 HU en hueso) y `e6c_techo_lw.md`:21 la miden. Eso contradice #128.3 ("ningun objetivo verifica su error de ida y vuelta"), `introduccion.tex`:46 y `capitulo3.tex`:172, que la dan por no verificada; ademas `sec:obj1` no describe esa medicion (PAT-88). Lo que de verdad falta es decidir que codificacion y que precision adopta el sintetizador. El cap. 2 ya lo dice asi.
2. **Escala del umbral de 25 HU del Obj 1 (T02 r05; nota del auditor r06):** DEC 2026-09-15 (2) y `capitulo3.tex`:67 anclan los 25 HU en RMSE publicados de MAR (Karageorgos 12.3 y 20.2; Yun 12.74) y los dan en HU, pero las fichas no traen la unidad. Ademas, DEC 2026-09-15 (2) llama "difusion en imagen" al 12.3 de Karageorgos, cuya ficha dice que opera en el sinograma. Si la unidad o el dominio no son los registrados, se debilita la justificacion del umbral. Propuesta: relectura con `lector-papers` de Karageorgos (Tablas I y III, Sec. II-G, region del RMSE) y Yun (Tabla 1, Sec. 2.4.2).
3. **Cifras de `jacob2026lgesynthnet` (r06):** la ficha pide no citarlas sin decidir cual vale (Dice +6 puntos en el resumen frente a +5 en resultados) y `_index.md`:107 dice "hoy no se cita ninguna cifra"; el cap. 2 cita Dice 0.72 -> 0.77 (Tabla 2, N = 300) y SSIM 0.587 con un `\GAPDEC`. Decidir si se mantienen.

- **Tipo:** SUPUESTO + REDACCION. **No aplicado.**

### 130 — El marco teorico (`overleaf/` cap. 1) no puede decir que tipo de tornillo representa el corredor que mide la tesis — ABIERTA

Origen: `/ciclo-redaccion capitulo1`, r00 (nota del redactor) y r01 (guia-2, T05 escalados), 2026-10-03. Detalle en `redaccion/rondas/capitulo1-r01-respuesta.md`. En el cap. 1 va como `\GAPDEC`; no se toco el cap. 3 (regla 14).

1. **Tres nombres para un corredor:** `docs/03-glosario.md`:74-75 separa transiliosacro (cruza ambas articulaciones sacroiliacas) de iliosacro y dice que las cifras de `mclaren2021corridor` son transiliosacras. `tesis/main.tex`:123 mide un "transsacral corridor diameter"; `tesis/main.tex`:52 y `capitulo3.tex`:196 hablan de tornillo iliosacro, y el cap. 3 justifica la exclusion de 8 mm por extremo con que el tornillo "entra y sale por la cortical del ilion", rasgo que el glosario asocia al transiliosacro.
2. **Que convenciones aplican:** el criterio de 10 mm y la holgura de 1-2 mm vienen de `kaiser2014dysmorphism` y las tolerancias angulares de `mclaren2021corridor` (transiliosacras). Si el corredor medido es de un tipo, no esta dicho si las convenciones tomadas del otro valen.
3. **Referencia clinica:** `zwingmann2009navigated` gradua tornillos iliosacros; si el corredor muestreado es transiliosacro, la comparacion de distribuciones de brecha une poblaciones de tornillos distintas.

4. **Lo que si consta (T01, capitulo1-r02):** `docs/SITUACION_ACTUAL.md`:183 describe el corredor de E9 como transsacro, "de la cortical externa de un ilion ... a la cortical externa del ilion opuesto": cruza ambas articulaciones, rasgo que el glosario asigna al transiliosacro. Lo abierto no es que corredor se mide, sino que tornillo representa y si le valen las convenciones de Kaiser et al. y la referencia de Zwingmann et al.

5. **La propia referencia clinica mezcla los nombres (T01, capitulo1-r03):** la ficha `zwingmann2009navigated` dice "navigated iliosacral screw placement" (:79, p. 1834) y "localization of the transiliosacral screw" (:83, :197, p. 1835). El punto 3 no se resuelve sin aclarar que tornillo graduo Zwingmann et al.; posible relectura con `lector-papers`.

- **DECISION DE LA AUTORA (2026-10-04, en chat): se adopta la recomendacion del asistente.**
  1. La geometria implementada se nombra **tornillo transiliaco-transsacro (transiliosacro)**: el
     corredor medido va de la cortical externa de un ilion a la del otro y cruza **ambas**
     articulaciones sacroiliacas, que es el rasgo que `docs/03-glosario.md`:74-75 asigna a ese tipo.
  2. Las convenciones de **`mclaren2021corridor`** (tolerancias angulares transiliosacras) **si
     aplican**, porque son del mismo tipo de corredor.
  3. **`zwingmann2009navigated` se conserva como referencia clinica externa de distribuciones de grado
     de brecha, NO como validacion del mismo diseno de implante.** Su propio texto usa los dos nombres
     —*"navigated iliosacral screw placement"* (p. 1834) y *"localization of the transiliosacral
     screw"* (p. 1835)— y no documenta longitud ni extremo de todos sus tornillos. La comparacion es de
     **distribuciones**, no de equivalencia geometrica, y asi debe escribirse.
  4. **No se acorta el modelo** a un tornillo iliosacro unilateral: obligaria a rehacer corredor,
     longitud, mascaras, poses y parte de SAP, sin ganancia.
- **APLICADO a `tesis/main.tex` el 2026-10-04**, por peticion explicita (regla 4). Dos frases: en el
  parrafo de geometria del implante, que la trayectoria medida va de cortical externa de un ilion a la
  contralateral cruzando **ambas** articulaciones y por tanto representa un **tornillo
  transiliaco-transsacro (transiliosacro)**, con las tolerancias de `mclaren2021corridor` aplicables por
  ser del mismo corredor; y antes del benchmark, que esa serie es **referencia clinica externa de la
  distribucion de grados y no evidencia de equivalencia geometrica**, porque su propio texto usa los dos
  nombres y no reporta longitud ni extremo de cada tornillo. Compila: 0 errores, 0 citas indefinidas,
  8 paginas. **Las menciones de "iliosacral screws" que describen trabajos ajenos —Zwingmann, Reilly—
  se dejan como estan: son de esos autores, no del implante de esta tesis.**
- **Pendiente de aplicar:** `overleaf/` cap. 1 y cap. 3, y `docs/03-glosario.md`. **Y antes de citar a Gardner para
  el nombre, comprobar que su raw este** en `refs/raw/` (regla 9); existe la ficha
  `gardner2011transiliac-transsacral.md`.
- **Tipo:** SUPUESTO + REDACCION. **Decidida, no aplicada.**

### 131 — La revision del recorte NO reabre la decision de 6 mm (0 de 16 `fallo_6mm`), y E14 cierra la desviacion de la envolvente: 0 casos de la cohorte cambian — **CERRADA el 2026-10-04**; quedan dos errores de segmentacion anotados (`CLINIC_0022`, `CLINIC_0024`)

- **Origen:** revision de los 16 casos por la autora con apoyo de un medico con SERUM, y corrida E14 en
  Khipu, 2026-10-03/04.

#### 1. La condicion de reapertura no se cumple

`e9ts_revision_laminas_autora.csv`, 16 de 16: **14 `ok`, 2 `fallo_ambos`, 0 `fallo_6mm`, 0 `fallo_3mm`**.
El unico veredicto que reabre la decision **2026-09-14 (4)** es `fallo_6mm`, y no hay ninguno. **El
recorte de 6 mm se mantiene como principal, ahora con la condicion evaluada y no solo declarada.**

- Normalizacion aplicada: la autora escribio `bien`, que no es categoria del protocolo; se mapeo a `ok`.
  Codificacion a UTF-8. Original en `e9ts_revision_laminas_autora.raw.csv`.
- **Procedencia corregida el 2026-10-04:** la columna `revisor` decia `autora`; la revision se hizo
  **con apoyo de un medico egresado (SERUM, sin especialidad)** y ahora lo declara. El nombre del
  archivo conserva el sufijo `_autora` por compatibilidad con las referencias ya escritas, pero
  **el juicio no es solo suyo**, y asi debe citarse.
- **Acuerdo con el agente: 13 de 16.** Los tres desacuerdos van en la direccion esperada: el agente
  llamo `fallo_3mm` a dos casos que la autora juzgo `fallo_ambos` u `ok`, y `ok` a uno que ella juzgo
  `fallo_ambos`. El agente nunca uso `dudoso`, lo que ya se habia senalado como optimista.
- **Los 2 `fallo_ambos` son errores de segmentacion, no de recorte**, y por eso no reabren nada:
  `CLINIC_0022` *"se reconoce S2 como S1 y el S1 no esta totalmente reconocido en plano sagital"*;
  `CLINIC_0024` *"parte de S1 no es reconocido en la vista coronal"*.

#### 2. E14: la desviacion de la envolvente no mueve nada en la cohorte (cierra #127, pto 13)

`outputs/e14_relleno.csv`, **152 casos, 0 errores**:

| Magnitud | Valor |
|---|---|
| Voxeles que anade el relleno | mediana **139**, max **9 833** (0.51 %) |
| `|dif D_TS|` | mediana **0.000 mm**, max **2.330 mm** |
| Casos con `|dif D_TS|` > 0.05 mm | **4 de 152** |
| Casos que cruzan el umbral de 7 mm | **0** |
| **Casos de la cohorte de 72 que cambian** | **0**; maxima diferencia dentro de la cohorte: **0.000 mm** |

Los 4 que se mueven son `metal_0025`, `metal_0066`, `metal_0068` y `metal_0072`, **todos fuera de la
cohorte del Objetivo 2**. **Ninguna cifra publicada depende del relleno.** Procede corregir el texto de
D-O2.3 para que describa la envolvente que E9-TS construye, en vez de volver a correr E9-TS, E12 y E13.

#### 3. Hallazgo nuevo: `vertebrae_S1` incluye el arco posterior, y eso NO es un error

**12 de los 16 casos** llevan la misma nota: *"se reconoce parte de la medula a la misma altura como
parte de S1"*. Dos aclaraciones:

- **`vertebrae_S1` de TotalSegmentator es una etiqueta de vertebra completa**, no de cuerpo vertebral.
  Incluir laminas, cresta sacra media y apofisis articulares superiores es su comportamiento esperado.
  Confirmado mirando las laminas de `CLINIC_0030` y `CLINIC_0076`: el contorno rojo rodea el cuerpo de
  S1 y se extiende por detras.
- **"Medula" es un nombre equivocado para lo que se vio**, y la propia autora lo declara: es hueso. Lo
  que hay por detras del cuerpo de S1 a esa altura es el **arco posterior**, cuyos componentes a ese
  nivel son la **cresta sacra media** (las apofisis espinosas fusionadas, en la linea media), las
  **laminas** y las **apofisis articulares superiores**, laterales a la cresta.
- **Nomenclatura, corregida por la autora el 2026-10-04:** en el chat dijo primero "astas del sacro" y
  acto seguido lo rectifico a **cresta sacra**, que es lo correcto. Las **astas** estan en el extremo
  **caudal**, flanqueando el hiato sacro, y no aparecen a la altura de S1. Queda anotado para que el
  termino que entre al documento sea el bueno.
- **Aun asi, esto necesita confirmacion del medico antes de entrar al documento.** El asistente lo
  dedujo mirando laminas, no es radiologo, y la distincion entre cresta media y apofisis articulares
  superiores depende de que se vio exactamente en cada caso. Se registra como **nomenclatura pendiente
  de confirmar**, no como dato.

#### 4. No hay contradiccion con la revision de R1, y conviene dejarlo escrito

La autora pregunta si aceptar la parte posterior como S1 contradice que en R1 un punto posterior se
marcara `otro`. **No se contradicen: son dos preguntas sobre dos objetos distintos.**

- **R1 juzga un PUNTO** y pregunta si esta *"en el platillo superior de S1"*. El platillo es la cara
  superior del **cuerpo** vertebral. Un punto sobre el arco posterior o sobre los ligamentos
  sacroiliacos **no** esta en el platillo: `otro` es correcto.
- **Esta revision juzga una MASCARA** y pregunta si cubre la vertebra S1. El arco posterior **si** es
  parte de S1: no es error.

Ademas, **R1 no usa mascaras de TotalSegmentator** (verificado: 0 referencias en `r1_landmarks.py`), asi
que el comportamiento de `vertebrae_S1` no puede haber causado los puntos posteriores de R1. Y el modo
de fallo ya estaba previsto en el codigo: `r1_landmarks.py`:225 dice que *"el tope en z a secas cae a
veces en el arco posterior"*, y por eso `s1_sagital` busca el promontorio en el bloque sagital.

- **Tipo:** RESULTADO + NOMENCLATURA. Cierra la condicion de reapertura y el punto 13 de #127.
  **Pendiente de la autora:** confirmar con el medico el nombre del arco posterior, y decidir si los dos
  `fallo_ambos` ameritan revisar la segmentacion de esos dos casos. **No aplicado (reglas 3, 4 y 14).**

### 132 — Cribado ciego de fractura: **20 de 30** pelvis de la cohorte la tienen, y la fractura **sacra desplazada** se concentra en los corredores estrechos (**7/15 frente a 2/15**, p = 0.109, sugerente no concluyente) — **CERRADA el 2026-10-04**, aplicada a `main.tex` y `00-tesis.md`

> **AVISO (2026-10-05): las cifras de esta entrada YA ESTAN CORREGIDAS en su sitio.** Por
> instruccion de la autora se aplicaron las cuatro correcciones que #136 y #140 habian detectado, y
> el recuento se rehizo de forma independiente desde `r3_fractura_revisor.csv` cruzado con
> `r3_fractura_grupos.csv`. Lo que decia antes y lo que dice ahora:
>
> | Donde | Decia | Dice |
> |---|---|---|
> | tabla, *Fractura (cualquiera)*, control | `11 (73%)` | **`10 (67%)`** |
> | seccion 2 | `21 de 30 (70%)` | **`20 de 30 (67%)` mas un dudoso aparte** |
> | seccion 4, columna `donde` | `21 casos (14 sacro, 7 ilion)` | **`20 casos (14 sacro, 6 ilion)`** |
> | tabla de `D_TS`, *Sin fractura* | `10 \| 6.7 mm` | **`9 \| 5.9 mm`**, con la fila del dudoso aparte |
> | tabla de `D_TS`, *desplazada* | `6.2 mm` | **`6.25 mm`** |
>
> Las cuatro venian del mismo origen: contar el unico caso `dudoso` como fractura, contra la regla
> que la autora decidio el 2026-10-05. Verificadas y sin cambios: el titular, las cifras de fractura
> sacra (9 y 5), las de sacra desplazada (7 y 2), las de legibles (8 y 10) y los tres valores p.

- **Origen:** `r3_fractura_revisor.csv`, 30 de 30, cribado ciego con grupo de comparacion. Revisor:
  **medico licenciado sin especialidad**. 2026-10-04.

#### 1. La hipotesis que motivo el cribado NO se sostiene

El cribado existia para comprobar si los 15 corredores estrechos de **#122** se explican por fractura no
detectada. **No se explican.**

| | estrecho (n=15) | control (n=15) | Fisher bilateral |
|---|---|---|---|
| Fractura (cualquiera) | **10 (67%)** | **10 (67%)** | **p = 1.000** |  <!-- corregido 2026-10-05: el control decia 11 (73%) contando el unico `dudoso` -->
| Fractura **sacra** | 9 (60%) | 5 (33%) | p = 0.272 |

- Sin concentracion global: la tasa es practicamente igual en los dos grupos.
- La fractura **sacra** —la unica con mecanismo, por `reilly2003effect`— va en la direccion predicha
  pero **no se distingue del azar** con n = 15 por grupo.
- **Y el subconjunto legible la borra:** entre los 18 casos que el revisor juzgo legibles, la fractura
  sacra es **3 de 8** en estrechos y **3 de 10** en controles. Sin diferencia.

**Consecuencia: #122 se mantiene como esta.** Los 15 corredores estrechos siguen reportandose como
variabilidad anatomica, y ahora con un cribado que lo respalda en vez de con una limitacion declarada.

#### 2. El hallazgo inesperado, y es mas grande que la pregunta original

**20 de 30 pelvis (67%) tienen fractura confirmada**, mas **un caso dudoso que se reporta aparte**, repartidas por igual entre los dos grupos. *[corregido 2026-10-05, ver #140]* La cohorte del
Objetivo 2 se construyo con el criterio **"sin osteosintesis"** (#52 a); nadie verifico "sin fractura", y
resulta que la mayoria **si** la tiene. `dataset6` es la particion sin metal de CTPelvic1K, no una
coleccion de pelvis sanas.

Esto **no invalida ninguna cifra** —el corredor se mide sobre cada volumen tal como esta—, pero cambia
como hay que **describir la anatomia receptora** en el documento. La frase actual de `main.tex`,
*"selected as free of osteosynthesis rather than verified as free of fracture"*, es exacta pero suave:
el dato dice que la mayoria esta fracturada.

#### 3. Los limites reales, tras una correccion importante

**RECTIFICACION (2026-10-04).** La primera version de esta entrada decia que *"buena parte de los
diagnosticos se emitieron sobre imagenes que el propio revisor declaro insuficientes"*. **Es falso**, y
el error es del asistente por interpretar la columna sin preguntar. La autora lo aclaro: `legible = no`
**no** significa que el caso quedara sin juzgar, sino que **la lamina no basto y el revisor abrio el
volumen completo en ITK-SNAP**, donde si distinguio la fractura. Los `si`/`no` directos son los que eran
evidentes desde la lamina.

Es decir, **la evidencia de esos 12 casos es mejor, no peor**: se juzgaron sobre el volumen entero y no
sobre tres cortes. El **67%** queda **mas respaldado** de lo que decia la version anterior. *[corregido 2026-10-05, ver #140]*

Los limites que si quedan en pie:

- **El revisor es medico licenciado sin especialidad**, no radiologo ni traumatologo. Sigue siendo un
  cribado y asi debe citarse siempre.
- **La evidencia es heterogenea por diseno accidental:** 18 casos se juzgaron solo con laminas y 12 con
  el volumen completo. Como el salto a ITK-SNAP lo motivo una **sospecha**, la deteccion pudo ser mas
  sensible justo donde ya se sospechaba algo. El reparto entre grupos es parejo —7 estrechos y 5
  controles fueron a ITK-SNAP—, asi que no sesga la comparacion del punto 1, pero si conviene declararlo.
- **La columna `legible` quedo mal definida en las instrucciones.** El documento la planteaba como
  "¿se puede juzgar con lo que se ve?" y el revisor la uso como "¿basto la lamina?". **Hay que renombrar
  esa columna** antes de reutilizar este material: por ejemplo `basto_la_lamina`, con el volumen completo
  como recurso previsto y no como excepcion.

**Las dos conclusiones anteriores se mantienen, y la segunda se refuerza.**

#### 4. Sobre pedir mas especificidad, que es lo que pregunto la autora

- **`donde` esta lleno en los 20 casos con `fractura = si` (14 sacro, 6 ilion).** *[corregido 2026-10-05, ver #140]* La version
  anterior decia "21 casos (14 sacro, 7 ilion)". Son **20**, y el reparto es **14 sacro y 6 ilion**.
  Y el `dudoso` **no** se puede sumar para llegar a 21: su columna `donde` esta **vacia**, asi que la
  frase "no tiene huecos" se caia por los dos lados.
  No hay nada que reclamar ahi.
- Lo que falta es el **nivel y la zona** de la fractura sacra y su **desplazamiento**, que es lo que
  `reilly2003effect` liga al estrechamiento del corredor. Solo 5 comentarios lo traen (`S1` en tres,
  *"a la altura del S2"* en dos).
- **RECOMENDACION CORREGIDA (2026-10-04).** La version anterior decia que pedir mas detalle seria un
  error porque el cuello de botella eran las imagenes. **Con la aclaracion del punto 3 eso ya no aplica:**
  el revisor **ya esta abriendo el volumen completo** cuando hace falta, y en 5 casos anoto el nivel por
  iniciativa propia (`S1` en tres, *"a la altura del S2"* en dos).
- **Si vale la pena pedir el nivel, y es un encargo pequeno:** solo los **14 casos con fractura sacra**,
  de los cuales **9 no tienen nivel anotado**. No hay que volver a mirar los 30 ni los de ilion.
- Lo que conviene pedir, en este orden: **nivel** (S1, S2, S3 o mas caudal) y **si esta desplazada**.
  El desplazamiento es lo que `reilly2003effect` liga al estrechamiento del corredor; el nivel solo no
  completa el mecanismo.
- **Si se va a citar una clasificacion por zonas** (tipo Denis), su fuente tiene que entrar por
  `refs/raw/` antes de usarse (regla 9). Mientras no exista, pedir el nivel y el desplazamiento en
  lenguaje llano, sin nombre de clasificacion.

- **Opciones:** (a) cerrar el cribado como esta, con sus limites declarados, y mantener #122;
  (b) si se quiere probar el mecanismo, montar una revision **distinta**: solo los casos con fractura
  sacra, **sobre el volumen completo en un visor**, preguntando zona y desplazamiento, idealmente con
  especialista; (c) volver a pedirle al mismo revisor mas detalle sobre las mismas imagenes.
- **Recomendacion corregida: (a) mas el encargo pequeno de nivel y desplazamiento sobre los 9 casos de
  fractura sacra sin nivel.** (b), la revision formal con especialista, solo si el 70% va a entrar al
  documento como cifra central. (c) deja de estar descartada: ahora es justamente lo barato y util,
  porque el revisor ya trabaja sobre el volumen.
#### 5. AMPLIACION (2026-10-04) con desplazamiento y nivel: **el resultado se INVIERTE**

**RECTIFICACION.** La primera version de este bloque, escrita el mismo dia, concluyo que el
desplazamiento tampoco se concentraba (4/15 frente a 4/15, p = 1.000). **Esa lectura era sobre datos
incompletos**: la planilla no se habia guardado bien y faltaba el desplazamiento de 7 fracturas. Con los
**20 de 20** datos, la conclusion es la contraria. Queda registrado por la regla 17.

Ademas se corrigio un caso: `CLINIC_0056` (control) pasa de `fractura = si, ilion` a `no`; el revisor lo
habia confundido con un volumen de `dataset7`. Total: **20 de 30 (67%)** con fractura.

**El desplazamiento SI se concentra en los corredores estrechos**, y el efecto va en la direccion que
predice `reilly2003effect`:

| | estrecho (n=15) | control (n=15) | Fisher bilateral |
|---|---|---|---|
| Fractura **desplazada** (cualquiera) | **8 (53%)** | **4 (27%)** | p = 0.264 |
| Fractura **sacra y desplazada** | **7 (47%)** | **2 (13%)** | **p = 0.109** |

Y el contraste por estado es grande:

| Estado | n | `D_TS` mediana |
|---|---|---|
| **Fractura desplazada** | 12 | **6.25 mm** |
| Fractura **no** desplazada | 8 | **10.4 mm** |
| Sin fractura, **sin** el dudoso | **9** | **5.9 mm** |
| *(Sin fractura, contando el dudoso)* | *10* | *6.7 mm* |

*Corregido el 2026-10-05 (ver #140).* La version anterior publicaba una sola fila, `Sin fractura | 10 |
6.7 mm`, que **contaba el `dudoso` dentro de "sin fractura"** — justo al reves de la regla decidida por
la autora, que lo reporta aparte. Con la regla aplicada son **n = 9 y 5.9 mm**; la fila con el dudoso se
conserva en cursiva solo para que la diferencia quede visible. Y la mediana de las desplazadas es
**6.25 mm** (media de 6.2 y 6.3 entre 12 valores), no 6.2: antes se publicaba redondeada sin declararlo.

**Como leerlo, sin pasarse.**

- **La direccion es la predicha y el tamano del efecto es grande:** 47% frente a 13% en el estrato
  estrecho, y 4.2 mm de diferencia de mediana entre fractura desplazada y no desplazada.
- **No alcanza significacion** con n = 15 por grupo: p = 0.109 en la comparacion con mecanismo. Es
  **sugerente, no establecido**. Decir que esta demostrado seria sobreinterpretar 9 casos.
- **La tabla de `D_TS` por estado NO es una comparacion limpia:** el muestreo fue estratificado por
  `D_TS` (15 por debajo de 7 mm y 15 por encima), asi que su distribucion esta fijada por diseno. La
  comparacion valida es la de **proporciones entre estratos**, que es la primera tabla.
- **Nivel:** de las 14 fracturas sacras, **9 en S1 y 5 en S2**. Reilly solo estudio S1 y solo
  desplazamiento craneal; para las de S2 su resultado **no transfiere**.

**Consecuencia para #122, y es la que importa.** Hasta hoy los 15 corredores estrechos se reportaban como
**variabilidad anatomica**. Con esto, **casi la mitad de ellos (7 de 15) tienen una fractura sacra
desplazada**, que es un mecanismo conocido de estrechamiento. **Esa redaccion ya no se sostiene tal
cual**: hay que declarar que una parte del estrechamiento puede ser patologia, no anatomia normal, y que
la muestra no permite cuantificar cuanta.

**Lo que no cambia:** el resultado principal del Objetivo 2 —las distribuciones de grado y los
Wasserstein-1— se mide sobre cada volumen tal como esta y no depende de esta discusion.

- **APLICADO a `tesis/main.tex` el 2026-10-04, por peticion explicita** (regla 4). Dos ediciones en el
  parrafo *Placement result*:
  1. Los 15 corredores estrechos dejan de atribuirse a anatomia. El texto dice ahora que **no esta
     establecido** que los estrecha, reporta el cribado ciego —**7 de 15 frente a 2 de 15** con fractura
     sacra desplazada, **p = 0.109**, lector sin especialidad—, declara que **5 de las 14 sacras estan
     en S2**, donde `reilly2003effect` no transfiere, y concluye que *"an unquantifiable fraction of
     them may be displaced fracture rather than anatomy"*.
  2. La limitacion sobre la anatomia receptora se concreta: el cribado **hallo fractura en 20 de los 30
     volumenes** que examino.
- **Verificacion:** `verificar_coherencia.py` recomputa desde `r3_fractura_revisor.csv` y
  `r3_fractura_grupos.csv` los recuentos por estrato, las 20 fracturas, los 7 frente a 2, las 14 sacras
  y las 5 en S2, y comprueba que `main.tex` los declare. **104/104 comprobaciones pasan.** Compila:
  0 errores, 0 citas indefinidas, 8 paginas.
- **APLICADO tambien a `docs/00-tesis.md` el 2026-10-04**, por orden explicita de la autora: seccion
  nueva *Criterio de cohorte del Objetivo 2: lo que significa y lo que NO*. Declara que la cohorte **no
  es anatomia sana**, que el documento debe decir **"sin osteosintesis"** y nunca "intacta", que ninguna
  cifra depende de esto porque el corredor se mide sobre cada volumen tal como esta, y que una fraccion
  **no cuantificable** del estrechamiento puede ser patologia.
- **Tipo:** RESULTADO + LIMITACION. Cierra **#125**. Debilito la redaccion de #122, **ya corregida en
  `main.tex`**, y el criterio de cohorte de **#52 (a)**, **ya declarado en `00-tesis.md`**.

### 133 — PRIMERA MUESTRA SINTETICA del proyecto: la cadena funciona de punta a punta y los dos controles pasan, pero el `ckpt` del piloto genera RUIDO — ABIERTA (cierra la parte ejecutable de #116)

- **Origen:** `experiments/objetivo3/a6_muestra_minima.py`, 2026-10-04. Es la primera vez que se llama a
  `muestrea_ddim` desde que se escribio el Diseno A.
- **Corrio en local, sin GPU.** `torch 2.9.1+cpu`. **No hacia falta Khipu**: el `ckpt.pt` (112 MB) y los
  **23 058 parches** de `outputs/a1b_cache/` ya estaban en disco. Lo que bloqueaba #116 durante dos
  semanas **no era el computo**: era que nadie llamaba a la funcion.
- **Coste medido:** **~1.0 s/paso en CPU**, 50 pasos DDIM, **~50 s por muestra**. En GPU eran 0.0923
  s/paso (#89).

#### Lo que funciona, con control

Dos parches de **validacion** (los que el modelo no vio), uno de banda y uno con metal:

| Parche | `G` del parche | MAE dentro de `G` |
|---|---|---|
| `metal_0011_c000 k0240` (**sin metal**, solo banda) | 0.2 % | 1 131 HU |
| `metal_0011_c011 k0263` (**n_metal = 1 256**) | 18.9 % | 1 519 HU |

- **Control 1:** maximo `|valor generado|` **fuera de `G`** = **0.000e+00** en los dos. `muestrea_ddim`
  multiplica por `g` en cada paso, como dice #117.
- **Control 2:** `verificar_composicion` **pasa**: fuera de `G` la salida es identica **bit a bit** al
  original. **La promesa central del Diseno A —preservacion por construccion, bloque E-A3— se cumple y
  ahora esta comprobada sobre una imagen real, no supuesta.**

#### Lo que NO funciona, y era de esperar

**Lo generado es ruido de sal y pimienta, no un implante.** Es el `ckpt` del **piloto de 200 pasos**
(job 52074), corrido para medir coste (#89), **no para converger**. **Nada de esto es un resultado y no
debe citarse como tal.**

**El techo de 20 000 HU: RESUELTO el 2026-10-04, y NO es un fallo.** El maximo decodificado es
exactamente **20 000 HU** en los dos parches. Verificado en el codigo: `CONFIG_DISENO_A` es
**`pub+asinh`** (`ventanas.py`:44), cuyo canal LW es `asinh_canal(-1000.0, **20000.0**)`
(`e6c_techo_lw.py`:81). **20 000 HU es el techo declarado de la representacion**, elegido en E6c
precisamente porque un techo de 2 000 no podia codificar el metal que la tesis debe generar (#39).

Un modelo sin converger emite valores repartidos por todo `[-1, 1]`; los que caen cerca de `u = 1` en LW
decodifican a 20 000 HU **por diseno**. Lo observado **confirma que el decodificador funciona**, no que
algo este roto.

**Lo que si queda, y es barato:** un control declarado para cuando el modelo si este entrenado. Si un
modelo convergido sigue emitiendo 20 000 HU **fuera de la mascara de metal**, eso si seria un fallo. Se
anade como comprobacion de E-A1, no como bloqueo previo.

#### Lo que esto convierte de prediccion en observacion

- **#95, #96, #112, #57** dejan de ser discusiones sobre imagenes que nadie vio. En particular, **#112**
  (costura en el borde de `B_delta`) ya **se puede mirar**: el panel 4 de la lamina muestra `G` aislada.
- **La composicion de `val` queda medida:** **553 parches con metal y 343 solo de banda**, de 896. El
  primer parche del conjunto es **solo banda**, cosa que conviene saber antes de sacar conclusiones de
  una muestra suelta.

- **Siguiente, en orden:** (1) decidir el techo de 20 000 HU; (2) entrenar de verdad en Khipu, que ahora
  si necesita GPU; (3) recien entonces E-A1..E-A4.
- **Tipo:** RESULTADO DE DIAGNOSTICO. Cierra la parte ejecutable de **#116**. **No aplicado a
  `tesis/main.tex` (regla 14).**

### 134 — Bucle de validacion conectado y checkpoints reanudables: el entrenamiento del Objetivo 3 deja de ser ciego y deja de perderse al cortar la cola — ABIERTA (decision de preinscripcion pendiente)

- **Origen:** peticion de la autora, 2026-10-04. Cierra el pendiente que arrastraba desde el cierre del
  2026-09-21: *"`a5_manifiesto_val.csv` existe pero nada lo consume"*.
- **Tres cambios en `src/renderizador/entrenar.py`:**
  1. **Validacion.** `--manifiesto-val` carga los **896 parches / 3 casos** (#105) y mide la perdida
     cada `--cada` pasos sobre `--lotes-val` lotes **fijos y sin barajar**: la cifra tiene que ser
     comparable entre pasos, y con lotes distintos cada vez la curva mezclaria convergencia con que
     parches tocaron. Sin esto no se ve si converge **ni se puede medir el margen `Delta` de D4**.
  2. **Checkpoint reanudable** cada `--cada-ckpt` pasos, con **modelo, optimizador y paso**. El estado
     del optimizador es necesario: sin el, reanudar reinicia los momentos de AdamW y la curva da un
     salto artificial. `--reanudar` es seguro siempre; si no hay ckpt, arranca de cero.
  3. **`s_tramo`** en `curva.csv`, el ritmo del ultimo tramo. **Cierra #114.** `s_por_paso` se conserva
     por comparabilidad con el piloto, pero es el promedio acumulado y **no es la cifra publicable**.
- **Probado en local** (CPU, modelo de 1.8 M): 4 pasos, corte, reanudacion declarada en el paso 4 y
  continuacion hasta 8. `curva.csv` se anade **sin duplicar cabecera**; la validacion reporta los 896
  parches y 3 casos esperados.
- **Parametros propuestos para la corrida (`a7_entrenar.sbatch`), con su razon:**
  - **200 000 pasos** (~187 epocas con lote 16; ~5-6 h al ritmo de #89, holgado en las 24 h de cola).
    La regla de parada real es la **curva de validacion**, y con el ckpt reanudable extender es gratis.
  - **lote 4 -> 16, `base` intacto en 64.** Responde a #115 (7% de GPU) **sin tocar la arquitectura**:
    con 17 149 parches de **47 pacientes**, un modelo mas grande memoriza, y en sintesis eso es peor que
    subajustar. Ademas `base = 64` es lo que midio el piloto y lo que supone la preinscripcion.
    Memoria estimada: ~13 GB de 48.
  - **`lr` en 1e-4**, sin escalar con el lote. Es lo conservador; si la perdida baja muy lento en las
    primeras ~20 000 iteraciones, ahi se revisa, y ahora **se puede ver** en `perdida_val`.
- **RESUELTO el 2026-10-04: la corrida va SIN `--preinscrito`, y la razon no es de comodidad.**
  `00-tesis.md`:71-72 dice que `diseno_A.md` sigue en BORRADOR y que **lo unico que falta para
  congelarlo es medir el margen `Delta` (D4)**. Ese margen **sale de esta corrida**, porque necesita el
  bucle de validacion que acaba de conectarse. **Preinscribir usando la corrida de la que depende la
  preinscripcion seria circular.** Esta corrida es la que **habilita** a congelar el diseno, no una que
  lo suponga congelado.
  - Consecuencia: la corrida es de **ajuste**, no resultado de tesis, y el script lo imprime
    (`AVISO: corrida NO preinscrita`). La corrida preinscrita viene **despues**, con `diseno_A.md`
    congelado y `Delta` ya medido.
- **Donde corre, y por que importa:** no habia ninguna A6000 libre —g002 y ds001 ocupadas por jobs de
  24 h y 3 dias—, asi que la corrida pasa a la **A100 entera de ag001** (40 GB), que `--test-only` dio
  disponible el mismo dia en vez de al siguiente. **#89 y #115 estan medidas sobre A6000**, asi que sus
  cifras de `s/paso` y de ocupacion **no son comparables** con las de esta corrida; el log registra la
  tarjeta via `nvidia-smi`. Bajar la pared de 24 h a 8 h **no fue lo que adelanto el arranque**: el
  cuello era que no habia A6000 libre, no el *backfill*.
- **Tipo:** METODO + INFRAESTRUCTURA. Cierra **#114** y el pendiente del bucle de validacion.
  **No aplicado a `tesis/main.tex` (regla 14).**

- **MEDIDO el 2026-10-04 (job 54367, A100-PCIE-40GB de ag001, arranque 13:22:51).** Primera corrida
  real del Objetivo 3 con el bucle conectado. Cifras tomadas de `data/a7/run01/curva.csv`, no estimadas:
  - **`s_tramo` = 0.197 s/paso**, estable entre los pasos 500 y 9 000 (0.1934 -> 0.1971).
  - **`gb_max` = 12.31 GB de 40.** La estimacion de ~13 GB del punto anterior se confirma, pero estaba
    hecha contra una A6000 de 48 GB; en la A100 **sobra 3x de memoria** con `--lote 16`.
  - `perdida_val` 0.165986 (paso 500) -> 0.060020 (paso 9 000). La perdida de entrenamiento oscila
    (0.119, 0.051, 0.105, 0.082) porque cada lote muestrea un `t` distinto; la cifra comparable es
    `perdida_val`, medida siempre sobre los mismos 16 lotes fijos.
- **CONSECUENCIA DE PLANIFICACION, que corrige el supuesto del punto anterior.** Se habia escrito
  "~5-6 h al ritmo de #89, holgado en las 24 h de cola". Con la cifra medida eso **no se sostiene**:
  200 000 x 0.197 s = **10 h 56 min de computo**, y la pared pedida es de **8 h**. Entran
  **~145 000 pasos** por turno; el checkpoint que sobrevive es el de **145 000** y se pierden menos de
  600 pasos. Faltarian **55 000 pasos (~3 h)** en un segundo envio. **La corrida de 200 000 pasos no
  cabe en un turno de cola.** El ckpt reanudable deja de ser una precaucion y pasa a ser la condicion
  para que la corrida termine.
- **DOS DECISIONES QUE QUEDAN ABIERTAS PARA LA AUTORA** (no se aplican aqui, regla 14):
  1. **Si 200 000 pasos son necesarios.** `perdida_val` ya esta en 0.060 al paso 9 000. Si se aplana
     antes de los 145 000, el segundo turno de cola es innecesario. El numero de pasos debe pasar de
     supuesto a **decision medida sobre la curva** antes de congelar `diseno_A.md`.
  2. **Si la corrida preinscrita entra con un lote mayor.** 12.31 de 40 GB es GPU ociosa. Cambiar
     `--lote` **a mitad de esta corrida romperia la comparabilidad de la curva** y no debe hacerse;
     pero la corrida preinscrita, que es la que va al documento, podria dimensionarse a la tarjeta
     desde el paso 0. Es decision de diseno, no de operacion, y afecta a lo que diga `diseno_A.md`.
- **SEGUNDA LECTURA, paso 44 000 del job 54367 (2026-10-04, ~15:50).** Ritmo sin cambio
  (`s_tramo` 0.1971, `gb_max` 12.31). Dos observaciones sobre la curva, ambas con cifra:
  1. **La validacion esta en arrastre, no en convergencia.** 0.165986 (500) -> 0.060020 (9 000) ->
     0.054720 (44 000). La segunda caida es de **8.8% en 35 000 pasos**, es decir ~2.5% por cada
     10 000, contra el 64% de la primera. Sigue bajando, pero poco.
  2. **La brecha entrenamiento/validacion se invirtio.** Paso 9 000: entrenamiento 0.081805 **por
     encima** de validacion 0.060020. Paso 44 000: entrenamiento **0.021370** muy **por debajo** de
     validacion **0.054720**. **Salvedad:** la perdida de entrenamiento es un lote suelto con `t`
     aleatorio y la de validacion son 16 lotes fijos, asi que **las magnitudes no son estrictamente
     comparables y el valor puntual no debe citarse como medida de sobreajuste**. Lo que si es
     interpretable es la **tendencia divergente**.
  - **Por que importa:** es exactamente el riesgo que **#115** declaro al subir el lote sin tocar
     `base = 64` —17 149 parches de solo **47 pacientes**, donde un modelo con margen memoriza—. Esta
     es la primera evidencia medida de ese riesgo en el proyecto, y **confirma la decision de #115 de
     NO agrandar la arquitectura**: el problema observado es de datos, no de capacidad.
  - **No se concluye sobreajuste aqui.** Se registra la senal y se deja la lectura para la decada
     completa al llegar a la pared, que es lo que cierra la decision 1 de esta implicancia.
- **CORRECCION AL PUNTO ANTERIOR, 2026-10-04 (~16:10). La lectura del paso 44 000 estaba mal hecha y
  se retira.** Al ver la validacion SUBIR en los pasos 47 000-48 000 (0.071788, 0.064280, 0.067137)
  despues del 0.054720 del paso 44 000, se reviso **como se mide** la columna en vez de interpretar el
  salto. Hallazgo: `mide_val()` llamaba a `perdida(...)` **sin pasar `generador`**. Los parches eran
  fijos, pero `perdida` sortea el nivel de ruido `t` y el ruido mismo del RNG global **en cada
  medicion**, y la MSE de difusion depende fuertemente de `t`.
  - **Consecuencia:** `perdida_val` oscilaba **+-15%** por como se midio, no por lo que aprendio el
    modelo. La perdida de entrenamiento rebota igual (0.021370 -> 0.041864 -> 0.047569 -> 0.068550),
    por la misma razon y porque ademas es un lote suelto.
  - **SE RETIRA la "inversion de la brecha"** reportada en el punto anterior. Comparaba dos sorteos de
    ruido, no dos estados del modelo: el 0.021370 del paso 44 000 fue un sorteo favorable. **No hay
    evidencia de sobreajuste en este job**, ni a favor ni en contra. Lo que #115 advirtio sigue siendo
    una prediccion sin medir, no una observacion.
  - **Arreglado en `src/renderizador/entrenar.py`:** `mide_val()` crea un `torch.Generator` con
    `SEMILLA_VAL = 20261004` (fija, y distinta de `--semilla` para que la medicion no quede
    correlacionada con el estado del entrenamiento) y se lo pasa a `perdida`, que **ya aceptaba el
    parametro y no se estaba usando**. Dos pasos distintos pasan a compararse sobre el MISMO conjunto
    de (parche, `t`, ruido).
  - **No se cancela el job 54367.** El defecto es del instrumento de lectura, no del entrenamiento:
    las pesas nunca vieron esos sorteos, solo los vio el medidor. El arreglo entra en la **reanudacion
    natural tras el corte de pared de las 21:22**, asi que `curva.csv` tendra una **discontinuidad
    documentada**: antes del paso de reanudacion la columna es ruidosa, despues es comparable. Al
    analizar, **los dos tramos no se grafican como una sola curva**.
  - **Lo ya medido no se pierde:** promediada en bloques de 10 000 pasos (~20 mediciones por bloque) la
    tendencia se recupera, porque el ruido es de medicion y se promedia. Las filas sueltas de
    `curva.csv` del tramo previo **no deben citarse individualmente**.
  - **Metodo, y es la leccion que se repite en este proyecto:** ante una cifra que se mueve, revisar
    primero como se mide. La version anterior de esta implicancia interpreto el instrumento como si
    fuera la senal.
- **CIERRE DEL JOB 54367, 2026-10-04 (~21:22). SOBREAJUSTE CONFIRMADO, y esta vez si supera el ruido
  de medicion.** El job llego al paso **144 500** y murio en la pared de 8 h, como estaba previsto
  (144 500 x 0.1988 s = 7 h 58 min; la prediccion fue ~145 000).

  | paso | entrenamiento | validacion |
  |---|---|---|
  | 44 000 | 0.021370 | **0.054720** |
  | 143 500 | 0.022791 | **0.106057** |
  | 144 000 | 0.056342 | **0.111781** |
  | 144 500 | 0.017097 | **0.110858** |

  - **Por que esto SI es senal y la lectura retirada NO lo era.** El estimador ruidoso oscila **+-15%**;
    aqui la validacion esta al **doble**, en **tres mediciones consecutivas y mutuamente consistentes**,
    mientras el entrenamiento sigue en ~0.02. Un estimador ruidoso pero insesgado no produce un
    desplazamiento sostenido de 2x. La retractacion del punto anterior sigue siendo correcta para
    aquellos datos; este es un hallazgo distinto y de otra magnitud.
  - **#115 PASA DE PREDICCION A OBSERVACION.** Advirtio que 17 149 parches de solo **47 pacientes** son
    poca gente y que un modelo con margen memoriza. Esta es la medicion. **Refuerza su decision de NO
    agrandar `base = 64`**: el limite es de pacientes, no de capacidad.
  - **PERDIDA REAL: las pesas del minimo ya no existen.** `guarda()` escribia siempre al mismo
    `ckpt.pt`, sobrescrito cada 5 000 pasos, y **no habia logica de mejor modelo**. Lo unico que
    sobrevive es el paso ~145 000, que es el sobreajustado. El modelo util de esta corrida se perdio.
  - **Arreglado en `src/renderizador/entrenar.py`:** se anade **`mejor.pt`**, que guarda las pesas del
    minimo de validacion (sin estado del optimizador: es para inferencia), y al terminar el log imprime
    el paso del minimo frente al paso final, para que pasarse de largo sea visible.
  - **NO se lanza el segundo turno de 55 000 pasos.** Ya no es "completar la corrida": seria alejarse
    mas del minimo. La corrida de 200 000 pasos queda **descartada por medicion**, no por falta de
    cuota.
  - **Lo que esta corrida SI deja, y es lo que #134 pedia:** un **criterio de parada medido sobre el
    propio dato** en lugar del numero escrito a priori. La corrida buena se relanza en `run02` (con
    `run01` y `--reanudar` continuaria desde las pesas sobreajustadas), con `--pasos` fijado desde la
    tabla de validacion por bloques de 10 000, el generador de validacion ya sembrado y `mejor.pt`
    activo. Al ritmo medido, si el minimo esta cerca de los 45 000, son **menos de 4 h: un solo turno**.
  - **PENDIENTE DE LA AUTORA:** localizar el minimo en la tabla por bloques y fijar `--pasos`. Esa
    cifra, y no la de 200 000, es la que debe entrar en `diseno_A.md` al congelarlo.
- **MINIMO LOCALIZADO, 2026-10-04. Es la cifra que cierra la decision 1 de esta implicancia.**
  Validacion de `run01` promediada en bloques de 10 000 pasos (20 mediciones por bloque, lo que cancela
  el +-15% del estimador sin sembrar):

  | bloque | val media | | bloque | val media |
  |---|---|---|---|---|
  | 0-10 k | 0.08241 | | 70-80 k | 0.07731 |
  | 10-20 k | 0.06121 | | 80-90 k | 0.08459 |
  | **20-30 k** | **0.05809** | | 90-100 k | 0.09178 |
  | 30-40 k | 0.06008 | | 100-110 k | 0.09376 |
  | 40-50 k | 0.06058 | | 110-120 k | 0.10082 |
  | 50-60 k | 0.06310 | | 120-130 k | 0.10652 |
  | 60-70 k | 0.06857 | | 130-140 k | 0.10807 |

  - **Minimo en el bloque 20-30 k (~paso 25 000), val 0.05809**, y de ahi **doce bloques consecutivos
    subiendo** hasta 0.10807. La forma en U es inequivoca.
  - **Coste del error:** el minimo esta a **1 h 23 min** de computo. Se corrieron 144 500 pasos, de los
    cuales ~**119 500 (6 h 34 min de A100) empeoraron el modelo**.
  - **`--pasos` de la corrida buena: 60 000** (3 h 18 min, un solo turno). No 30 000: el minimo hay que
    **verlo pasar**, no suponerlo. 60 000 deja 35 000 pasos de subida posterior, da la U completa como
    figura y justifica el numero en `diseno_A.md`. `mejor.pt` retiene las pesas del minimo aunque la
    corrida siga.
  - **HALLAZGO DE FONDO, mas alla de la operacion:** el renderizador **satura a ~25 000 pasos** con 47
    pacientes y no mejora con mas computo. **La capacidad del renderizador no se decide con la perdida
    sino con `Delta` (D4), medido sobre las muestras.** Si `Delta` no alcanza, la palanca no son mas
    pasos ni un modelo mayor (#115): son mas pacientes, y eso se declara como limitacion con esta
    medicion como respaldo.

#### AMPLIACION 2026-10-05: `run02` TERMINADO. La U se reproduce con el estimador corregido, y el sobreajuste NO era un artefacto de medicion

Job **54498**, nodo `ag001`, 06:38:18 a ~12:55 del 2026-10-05, **60 000 pasos en ~6 h 20** a
**0.377 s/paso** (9 549 pasos/h) en la particion MIG `a100_3g.20gb`, 12.3 GB de 20. No toco la pared
de 12 h.

**Tabla por bloques de 10 000 (`data/a7/run02/curva.csv`):**

| Bloque | val media | filas |
|---|---|---|
| 0 | 0.08098 | 19 |
| 10 000 | 0.06271 | 20 |
| 20 000 | 0.05927 | 20 |
| **30 000** | **0.05891** | 20 |
| 40 000 | 0.06132 | 20 |
| 50 000 | 0.06364 | 20 |
| 60 000 | 0.06590 | 1 (no se cita) |

`MEJOR VALIDACION: 0.05519 en el paso 37500 (mejor.pt). Ultimo paso: 60000.`

##### Lo que queda establecido

1. **La forma de U es real.** Baja hasta el bloque 30-40 k y sube en los **dos** bloques siguientes.
   `run01` ya la mostraba, pero con el `mide_val()` defectuoso, asi que cabia la duda de que la subida
   fuera ruido del estimador. **Con `SEMILLA_VAL` fija la U se reproduce.** El sobreajuste de #134 es
   un hecho del modelo, no del instrumento.
2. **`mejor.pt` justifica su existencia.** El minimo esta en 37 500 y la corrida acabo en 60 000:
   **22 500 pasos de distancia**, el 37.5 % de la corrida gastado despues del optimo. Con el
   `guarda()` anterior, que sobrescribia un unico `ckpt.pt`, **esas pesas se habrian perdido otra vez**.
3. **El minimo se corrio mas tarde que en `run01`** (bloque 30-40 k frente a 20-30 k; paso 37 500
   frente a ~25 000). No se puede decir cuanto de ese corrimiento es real: la posicion del minimo de
   `run01` tambien la midio el estimador roto.

##### DOS COMPARACIONES QUE NO SE PUEDEN HACER, y conviene dejarlas escritas

- **`0.05519` de `run02` NO es "mejor" que `0.05809` de `run01`.** Salen de instrumentos distintos:
  `run01` con un estimador que sorteaba `t` y el ruido en cada medicion (oscilacion +-15 %), `run02`
  con semilla fija. **Enfrentar los dos numeros es exactamente el error de leer el instrumento como
  si fuera la senal.** Si se quiere comparar corridas, hay que remedir `run01` con `SEMILLA_VAL`, y
  para eso su `ckpt.pt` final no sirve: haria falta reentrenar.
- **La magnitud de la subida tampoco se compara.** `run01` subio de 0.05809 a 0.10807 a lo largo de
  **doce** bloques porque corrio 144 500 pasos; `run02` sube de 0.05891 a 0.06364 en **dos** bloques
  porque paro en 60 000. La subida mas chica no significa menos sobreajuste: significa menos corrida.

##### CORRECCION a la justificacion documentada de la tabla por bloques

`ESTADO.md` justifica promediar por bloques diciendo que "promediar cancela el ruido del estimador".
**Para `run02` eso ya no es cierto.** Con `SEMILLA_VAL` fija la medicion es determinista dado el
modelo: no hay ruido de estimador que cancelar, y **las filas sueltas de `run02` si son comparables
entre si**. Lo que el promedio por bloques suaviza ahora es la **fluctuacion de las pesas a lo largo
del descenso**, que es otra cosa. La practica sigue siendo correcta; el motivo escrito, no.

##### Pendiente de la autora (reglas 3 y 14). Esto NO se aplico

1. ~~**B2, el numero de pasos de `diseno_A.md`.**~~ **DECIDIDO el 2026-10-05: 30 000 pasos**, el centro
   de la meseta, registrado en `docs/01-decisiones.md`. Queda **declarado como eleccion de
   hiperparametro hecha sobre validacion**, no fijada de antemano: sale del minimo observado en
   `run01` y `run02`, ninguna de las dos medida sobre test. Esa salvedad tiene que viajar con la cifra
   a `diseno_A.md` y a la tesis. **Falta aplicarla a `diseno_A.md`**, que sigue en borrador y se
   congela despues de medir `Delta`.
2. **B1, la saturacion como limitacion declarada.** Este resultado la **sostiene**: con el estimador
   bueno, mas computo no mejora nada despues del paso ~37 500. La palanca que queda son mas pacientes,
   no mas pasos. Sigue sin estar escrito en ninguna parte del documento.
3. **#115 pasa definitivamente de prediccion a observacion**, y como se declara sigue siendo decision
   de la autora.
- **Tipo:** SUPUESTO + RIESGO. **No aplicado.**

#### AMPLIACION 2026-10-05 (2): `run01/curva.csv` ya esta en local, y las DOS curvas son la misma

`run01/curva.csv` bajado de Khipu: **289 filas, ultimo paso 144 500**, columnas
`paso, perdida, perdida_val, s_por_paso, s_tramo, gb_max`. Reproduce **exactamente** lo que esta
entrada describia: minimo **0.05809** en el bloque 20-30 k y subida sostenida durante **doce** bloques
hasta **0.10807**.

| Bloque | `run01` (estimador que sorteaba) | `run02` (`SEMILLA_VAL` fija) | diferencia |
|---|---|---|---|
| 0 | 0.08241 | 0.08098 | -0.00143 |
| 10 000 | 0.06121 | 0.06271 | +0.00150 |
| 20 000 | **0.05809** | 0.05927 | +0.00117 |
| 30 000 | 0.06008 | **0.05891** | -0.00118 |
| 40 000 | 0.06058 | 0.06132 | +0.00074 |
| 50 000 | 0.06310 | 0.06364 | +0.00054 |
| 60 000 | 0.06857 | 0.06590 (1 fila) | — |
| 70 000 a 140 000 | 0.07373 -> **0.10807** | no corrio | — |

**Maxima diferencia entre bloques comparables: 0.00150.**

##### 1. Dos corridas independientes trazan la misma curva de validacion

Sobre los 60 000 pasos compartidos, `run01` y `run02` coinciden dentro de **1.5e-3** en **todos** los
bloques, **medidas con instrumentos distintos**. Eso establece dos cosas que antes eran supuesto:

- **El entrenamiento es reproducible.** No es una corrida con suerte ni una con mala suerte.
- **El estimador defectuoso NO distorsionaba la curva promediada por bloques.** Su oscilacion de
  +-15 % era ruido por fila, y el promedio de 20 filas lo cancelaba, que es exactamente para lo que
  se adopto la tabla por bloques.

##### 2. EL MINIMO NO ES UN PUNTO, ES UNA MESETA de ~20 000 a ~40 000 pasos

`run01` lo pone en el bloque 20-30 k (0.05809) y `run02` en el 30-40 k (0.05891): **los dos bloques
difieren menos que la diferencia entre las dos corridas**. Juntando ambas, los bloques 20 k, 30 k y
40 k caen entre **0.05809 y 0.06132**. No hay un optimo agudo que haya que acertar; hay un tramo
plano, y despues del bloque 40-50 k la subida es monotona en las dos corridas.

**Esto cambia la forma de la respuesta a B2.** La pregunta no es "cual es el paso optimo" sino
"donde termina la meseta", y la respuesta medida es **alrededor de 40 000**. Fijar 40 000 estaria en
el extremo alto de la meseta; 30 000 caeria en su centro y costaria un 25 % menos de computo. Las dos
cifras son defendibles con esta evidencia; **la eleccion es de la autora** (regla 14).

##### 3. REFINAMIENTO de la correccion de metodo de la ampliacion anterior

La ampliacion previa decia que la justificacion escrita del promedio por bloques ("cancela el ruido
del estimador") estaba **mal**. Con `run01` en la mano, lo correcto es mas fino:

- Para **`run01` era cierta, y ahora esta demostrada**: el promedio por bloques recupero una curva que
  coincide con la determinista dentro de 1.5e-3 pese al +-15 % por fila.
- Para **`run02` es obsoleta**: con semilla fija no hay ruido de estimador que cancelar, y sus filas
  sueltas si son comparables entre si.

Y una asimetria que conviene no perder: el estimador de `run01` **promediaba sobre `t` y sobre el
ruido**, asi que su media por bloque estima la perdida esperada; el de `run02` usa **un solo sorteo
fijo** de `t` y de ruido, asi que es comparable entre pasos pero es **una muestra sesgada** de esa
perdida esperada. Que coincidan dentro de 1.5e-3 es una **observacion empirica sobre este par de
corridas**, no una prueba de que los dos instrumentos sean intercambiables. La prohibicion de
comparar **filas sueltas entre corridas** sigue en pie; lo que queda habilitado es comparar **bloques**.

#### AMPLIACION 2026-10-05 (3): el papel de la validacion cambio y `diseno_A.md` dice lo contrario

Al aplicar B2 a `experiments/objetivo3/diseno_A.md` aparecio una contradiccion que la correccion de
esta misma entrada introdujo sin que nadie la declarara. La seccion 5 del diseno decia:

> Validacion: 5 pacientes con metal; registra curva, **no elige checkpoint** (igual que P1).

**Hoy la validacion hace las dos cosas que esa frase niega:**

1. **Elige el checkpoint.** `guarda()` escribe `mejor.pt` en cada minimo de validacion desde la
   correccion del 2026-10-04. Eso es seleccion de modelo por validacion.
2. **Fija un hiperparametro.** Los 30 000 pasos de B2 salen del minimo de validacion de `run01` y
   `run02`.

**El cambio es correcto y resolvio una perdida real** —en `run01` las pesas del optimo se perdieron
porque `guarda()` sobrescribia un unico `ckpt.pt`—, y **seleccion de modelo por validacion con test
intacto es practica estandar**. El problema no es el metodo: es que **aparta al Objetivo 3 del
precedente del Objetivo 1 (P1, que deliberadamente no elegia checkpoint) y eso no esta declarado en
ninguna parte**. Un jurado que compare los dos objetivos vera dos protocolos distintos sin
justificacion escrita.

**Lo que NO cambia:** el aislamiento por paciente. Las dos cosas se deciden sobre los **5 pacientes de
validacion** y **ninguna toca los 20/14 de test** (`main.tex`:111).

**Pendiente de la autora (regla 14):** decidir como se declara el cambio de papel de la validacion en
el Objetivo 3, y si el precedente de P1 se menciona como contraste deliberado o se deja sin comentar.
Marcado como `[DECIDIR]` en `diseno_A.md` seccion 5, al lado de la cifra de B2. **No se resolvio.**

### 135 — #132 se aplico a `tesis/main.tex` pero NO a `overleaf/`, que todavia afirma lo contrario — ABIERTA

- **Origen:** mapeo de pendientes de redaccion, 2026-10-04, al preparar `redaccion/ENCARGO_2026-10-04.md`.
- **El defecto:** `overleaf/secciones/capitulo3.tex:263`, parrafo de *Validez externa*, dice que la
  referencia clinica proviene de pelvis fracturadas **"mientras que los corredores de este trabajo se
  miden en pelvis sin osteosintesis"**, y cierra con **"las pelvis receptoras, sin fractura conocida,
  no reproducen"**. **#132 (CERRADA) lo desmiente:** el cribado ciego hallo fractura en **20 de 30**
  pelvis de la cohorte. El criterio de construccion fue "sin osteosintesis" (#52 a), que **no es lo
  mismo** que "sin fractura", y eso nunca se verifico.
- **Por que importa mas que una errata:** es una **afirmacion falsa en el documento de entrega**, y
  sostiene un argumento de validez externa. Un lector que compruebe #132 encuentra la contradiccion.
- **Lo que no es:** no es un problema de #132, que esta correctamente cerrada y aplicada donde se
  ordeno. Es un **fallo de propagacion** entre `tesis/main.tex` (boceto, ingles) y `overleaf/`
  (entrega, espanol), que son dos documentos y no uno.
- **GAP DE PROCESO QUE ESTO ABRE:** cerrar una implicancia y aplicarla a `main.tex` **no garantiza**
  que llegue a `overleaf/`. **#124 y #130 estan en la misma situacion**, aplicadas solo en
  `main.tex`. Convendria que el cierre de una implicancia exija declarar los dos destinos, o que
  `auditor-trazabilidad` verifique la paridad entre ambos documentos.
- **Redaccion preparada, NO aplicada** (regla 14): bloque A1 de `redaccion/ENCARGO_2026-10-04.md`.
  Al corregirlo el argumento **se fortalece**: ya no es solo que las receptoras no reproduzcan la
  malreduccion, es que **tampoco estan libres de fractura**, y parte de lo atribuido a variabilidad
  anatomica podria ser patologia no detectada.
- **Limite que debe acompanar a la cifra:** el cribado lo hizo un **medico recien egresado en SERUM,
  sin especialidad**, sobre laminas fijas. Cribado valido, **no** lectura de especialista.

### 136 — RECTIFICACION NUMERICA DE #132: la tabla y la seccion 2 contaban el `dudoso` como fractura; los grupos son 10 y 10, no 10 y 11 — **CERRADA el 2026-10-05**: regla decidida por la autora y las cuatro cifras corregidas en #132 (ver tambien #140) — (decision de la autora sobre la regla del `dudoso`)

- **Origen:** verificacion directa contra las fuentes el 2026-10-05, al preparar la redaccion de #135.
- **Recuento desde `r3_fractura_revisor.csv` cruzado con `r3_fractura_grupos.csv`:**

  | | estrecho (n=15) | control (n=15) | total |
  |---|---|---|---|
  | `fractura = si` | **10** | **10** | **20** |
  | `fractura = no` | 5 | 4 | 9 |
  | `fractura = dudoso` | 0 | **1** | 1 |

- **Lo que #132 dice mal, en dos sitios:**
  1. La tabla de la seccion 1: *"Fractura (cualquiera) | 10 (67%) | **11 (73%)**"*. El 11 solo sale
     contando como fractura el unico `dudoso`, que esta en el grupo control.
  2. La seccion 2: *"**21 de 30** pelvis (70%) tienen fractura"*. Mismo origen.
- **El titular de #132 SI es correcto** (*"20 de 30"*), igual que `tesis/main.tex`:109
  (*"fracture in 20 of the 30 volumes"*). **El error no se propago al documento**; vive solo dentro de
  la entrada de implicancias, que es lo que leen los agentes de redaccion.
- **Por que no es defendible contar el `dudoso` como `si`:** el diseno declaro `dudoso` como respuesta
  valida y distinta (`r3_fractura_revisor.md`, *"`dudoso` es una respuesta valida y util"*), y
  contarlo como fractura en **un solo brazo** inclina la comparacion justo en la direccion que el
  cribado queria poner a prueba. Es una decision de analisis tomada despues de ver el dato.
- **Efecto sobre la conclusion: ninguno, y la refuerza.** Con el criterio correcto los dos grupos son
  **10 y 10, identicos**. #122 se mantiene, y ahora con una comparacion que no depende de como se
  clasifique un caso ambiguo.
- **DECISION PENDIENTE DE LA AUTORA (regla 14):** fijar la regla del `dudoso` antes de que cualquier
  cifra entre a `overleaf/`. **Recomendacion del asistente:** `dudoso` **no** cuenta como fractura y se
  reporta aparte -> *"20 de 30 (67%) con fractura confirmada, mas un caso dudoso"*. Es lo que dice el
  CSV, es la lectura conservadora, y evita tener que justificar en la sustentacion por que un caso
  ambiguo se resolvio hacia el lado que convenia.
- **Bloquea el bloque A1 de `redaccion/ENCARGO_2026-10-04.md`:** si los agentes redactan antes de esta
  decision, escribiran 70% o 73% en el documento de entrega.
- **RESUELTA el 2026-10-05 por decision de la autora: se adopta la regla recomendada.** `dudoso`
  **no** cuenta como fractura y se reporta aparte. La cifra unica para el documento es
  **20 de 30 (67%) con fractura confirmada, mas un caso dudoso**, y la comparacion entre grupos es
  **10 frente a 10**. El bloque A1 queda desbloqueado.
- **Verificacion completa contra `r3_fractura_revisor.csv` el 2026-10-05**, para que ninguna otra
  cifra de #132 se arrastre sin comprobar:

  | | estrecho (n=15) | control (n=15) |
  |---|---|---|
  | Fractura confirmada (`si`) | 10 | 10 |
  | Fractura sacra | 9 | 5 |
  | Fractura sacra **desplazada** | **7** | **2** |
  | Casos legibles desde lamina | 8 | 10 |

  Las tres ultimas filas coinciden con lo que #132 ya decia: **solo la fila de fractura
  *cualquiera* y el total de la seccion 2 estaban mal.**
- **ESTIMACION PARA LA COHORTE COMPLETA, calculada el 2026-10-05. No requiere leer un caso mas.**
  Los 30 cribados **no** fueron una muestra al azar: fueron **los 15 estrechos que existen** (censo de
  ese estrato) mas **15 de los 57 controles**. Es un muestreo estratificado con pesos conocidos, asi
  que la prevalencia en los 72 se estima por diseno:
  - estrato estrecho: **10** (censado, 15 de 15);
  - estrato control: 10/15 -> 57 x 0.667 = **38**;
  - total: **48 de 72, 67%**. Intervalo ancho, del orden de **47% a 81%** (Wilson sobre 10/15 del
    estrato control, escalado; sin correccion por poblacion finita, que lo estrecharia algo).
  - **Consecuencia practica:** para la frase que el documento necesita —que la anatomia receptora
    **no** es una coleccion de pelvis sanas— el intervalo sobra, y **no hace falta ampliar el
    cribado**. La cifra puntual citable sigue siendo la medida, **20 de 30**; esta estimacion se usa
    solo si se quiere hablar de los 72, y entonces va con su intervalo y la palabra "estimada".
- **DESCARTADO, con motivo, el 2026-10-05: no se cribara todo `dataset6` (99 casos).** El limite de lo
  que puede afirmarse lo pone **quien lee** —medico recien egresado sin especialidad, sobre laminas
  fijas—, no el tamano de muestra; 69 lecturas mas darian una estimacion mas precisa **de lo que ve un
  no especialista**, sin mover el techo. Ademas los 27 casos de `dataset6` fuera de la cohorte del
  Objetivo 2 **no alimentan nada**: el Objetivo 3 entrena sobre los 47 pacientes con metal.
- **OPCION QUE QUEDA ABIERTA, no ejecutada:** completar los **42 controles** restantes de la cohorte de
  72, con **un unico objetivo declarado**: resolver la fractura **sacra desplazada** (7/15 frente a
  2/15, p = 0.109), que es lo unico que quedo sin potencia y que `reilly2003effect` predice. **Si se
  hace, no es una segunda ronda ciega:** los 42 restantes son **todos controles**, y el revisor ya
  conoce la estructura del estudio, asi que seria una **completacion de censo** y todo analisis sobre
  los 72 es **post-hoc y debe declararse**. La comparacion ciega primaria sigue siendo la de los 30.
  **No se hace ahora:** el camino critico es `run02` -> `Delta` -> congelar `diseno_A.md`, la auditoria
  de paridad y la redaccion.

### 137 — El Objetivo 3 no tiene NINGUNA lectura humana prevista: E-A1..E-A4 son todos bloques metricos — ABIERTA

- **Origen:** revision de los bloques de evaluacion del Diseno A el 2026-10-05, al decidir si se podia
  ensenar una muestra al medico colaborador sin contaminar una evaluacion futura.
- **El hallazgo:** los cuatro bloques (metricas de Peters, baseline de copia-pega, costura en el borde
  de `B_delta`, preservacion fuera de la banda) **son todos cuantitativos**. No hay ni una linea de
  evaluacion por observador humano para la apariencia del implante sintetizado ni de su artefacto.
- **El contraste con el Objetivo 2 es llamativo:** alli se montaron **tres** revisiones humanas
  (laminas del corredor, nivel del pico, cribado de fractura, #131 y #132), con protocolo ciego y
  grupo de comparacion. El Objetivo 3, cuyo producto **es una imagen**, no tiene ninguna.
- **Por que importa:** la tesis afirma evaluar **coherencia fisica y quirurgica**. Las metricas de
  Peters miden parecido de artefacto frente a un protocolo de referencia; **ninguna** contesta si un
  clinico reconoce el resultado como un tornillo en una TC. Un comite puede preguntarlo.
- **Lo que NO se afirma aqui:** que haga falta un estudio formal de lectura. Puede ser deliberado y
  defendible —el alcance declara que la evaluacion downstream esta fuera—, pero **hoy no esta
  declarado como eleccion**, solo esta ausente.
- **Riesgo operativo, con fecha:** el 2026-10-05 se recomendo a la autora ensenar la primera lamina al
  medico colaborador y pedirle una opinion de plausibilidad. Es barato y aporta lo que las metricas no
  dan, **pero quema la ingenuidad de ese lector** para cualquier estudio formal posterior. Si se hace,
  **declararlo como lectura exploratoria**, no como evaluacion.
- **DECISION PENDIENTE DE LA AUTORA (regla 14):** o se declara explicitamente que el Objetivo 3 se
  evalua solo con metricas y por que, o se anade un bloque de lectura. Lo primero es legitimo; el
  silencio no.

### 138 — El medico confirma que la "parte de atras" aceptada como S1 es la CRESTA SACRA MEDIA; el techo de la etiqueta `vertebrae_S1` no es el platillo superior — ABIERTA

- **Origen:** respuesta del medico colaborador el 2026-10-05, a la pregunta pendiente que bloqueaba el
  `\GAPDEC` de `overleaf/secciones/capitulo3.tex:97`. **Desambigua** lo que se habia anotado como
  "tambien se considero la parte de atras": no son las apofisis articulares superiores, es la
  **cresta sacra media**.
- **Es coherente con la etiqueta, no un error de lectura.** `vertebrae_S1` de TotalSegmentator es una
  etiqueta de **vertebra completa**, que incluye el arco posterior. El revisor acepto como S1 una
  estructura que la mascara efectivamente contiene.
- **LO QUE ESTO IMPLICA, y es lo que hay que mirar:** el marco de referencia de
  `kaiser2014dysmorphism` se define **perpendicular al platillo superior de S1**. Si la extension
  superior de la mascara `vertebrae_S1` la marca la **cresta sacra media** —una estructura
  **posterior y, segun el caso, mas craneal que el platillo**— entonces "el techo de S1 segun la
  mascara" y "el platillo superior de S1" **no son la misma superficie**, y cualquier medida anclada
  al techo de la etiqueta hereda esa diferencia.
- **NO se afirma aqui que el marco este mal.** Hace falta comprobar, caso por caso, si el voxel mas
  craneal de `vertebrae_S1` cae en el cuerpo vertebral o en el arco posterior, y con que diferencia en
  milimetros. **Eso no esta medido.** Mientras no lo este, es una amenaza identificada, no un defecto
  demostrado.
- **DESBLOQUEA la redaccion** del `\GAPDEC` de `capitulo3.tex:97`: ya se puede nombrar la estructura.
  **Lo que NO desbloquea** es afirmar que el nivel S1 este bien o mal determinado: eso depende de la
  comprobacion anterior.
- **PENDIENTE DE LA AUTORA (regla 14):** decidir si esa comprobacion se hace antes de la sustentacion
  o si la diferencia entre el techo de la etiqueta y el platillo se declara como supuesto no medido.

### 139 — LA CADENA COMPLETA NUNCA SE HA EJECUTADO, y la costura de E-A2 queda medida por primera vez (203 frente a 30 HU) — ABIERTA

- **Origen:** la autora miro la lamina de A6 el 2026-10-05 y objeto que el tornillo "no parece estar en
  S1" y que la imagen "parece un PNG sobrepuesto". Las dos objeciones se verificaron con medicion.

#### 1. EL HALLAZGO PRINCIPAL: muestreador y renderizador nunca se han encadenado

`a6_muestra_minima.py` **no coloca ningun tornillo**. Toma un paciente que **ya tenia** un implante real
(`CLINIC_metal_0011`, componente 11: `alargado`, 94.3 mm, 8.2 x 3.6 mm), borra `G` y pide al modelo que
**reconstruya** lo que habia. La pose la decidio el cirujano que opero a ese paciente, **no el
muestreador del Objetivo 2**.

**Consecuencia:** el Objetivo 2 esta validado por separado (SAP, #131, #132) y el Objetivo 3 esta
validado por separado (reconstruccion de metal real), pero **la secuencia pelvis limpia de `dataset6`
-> muestrear pose en S1 -> rasterizar `M` -> generar apariencia NO SE HA EJECUTADO NUNCA**. El producto
de la tesis **no existe como imagen**, y por eso la lamina no parece presentable: **no es el producto,
es una prueba de componente**.

- **No esta claro que exista el eslabon de rasterizado** (de pose muestreada a mascara `M` voxelizada).
  Hay que comprobarlo antes de prometer la demostracion.
- **Expondra el riesgo #96:** el renderizador aprendio apariencia sobre pacientes que **ya tenian**
  streaking de implante real; se le pedira generar sobre una pelvis **limpia**. El resultado puede ser
  malo, y eso tambien es informacion.

#### 2. PRIMERA MEDICION DE LA COSTURA (bloque E-A2), que no tenia ninguna

Salto de HU al cruzar el borde de `G` (mediana del anillo interior frente al exterior, un voxel):

| | HU |
|---|---|
| imagen **real** | **30** |
| imagen **compuesta** | **203** |

Escalon de ~170 HU que no existe en el original. Es el **riesgo #96** y lo que **E-A2** existe para
medir. **Un solo caso, un solo corte, con un `ckpt` pasado de su optimo**: es una primera medicion, no
el bloque E-A2.

#### 3. LO QUE LA MEDICION DESMIENTE: el modelo SI respeta la mascara `M`

| | real | generado |
|---|---|---|
| HU mediano en `M` | 5 129 | **5 375** |
| HU mediano en la banda `G\M` | -164 | 13 |
| **contraste metal menos banda** | **5 293** | **5 362** |

El contraste se reproduce con ~1% de diferencia: el metal se genera **donde `M` dice**. La "cuna
luminosa de bordes rectos" del cuarto panel es el **recorte por `G`** —ese panel se titula *"solo lo
generado en G"*—, no la forma del implante. **El asistente tambien leyo mal ese panel antes de medir.**

#### 4. Limitaciones de presentacion, menores pero reales

- El `.nii.gz` es **256 x 256 x 1**: un corte suelto, no navegable. El modelo es 2.5D y puede generar
  **cortes consecutivos**; apilarlos daria un volumen que un clinico si puede recorrer.
- **BUG CORREGIDO:** el titulo de la lamina decia *"ckpt del piloto de 200 pasos"*, falso desde que se
  uso el `ckpt` de `run01`. Se corrigio en `a6_muestra_minima.py`; **cualquier lamina generada antes
  del 2026-10-05 lleva ese pie falso y no debe mostrarse.**

#### Pendiente de la autora (regla 14)

Decidir si se construye la demostracion de cadena completa y **cuando**. Recomendacion del asistente:
**si, pero con `mejor.pt` de `run02`**, no con el `ckpt` pasado de `run01`.

### 140 — La auditoria de paridad del BLOQUE 0 encuentra que el fallo de #135 no es un caso aislado (4 sitios, 5 implicancias) y que la rectificacion de #136 quedo incompleta: dos cifras mas no cuadran dentro de entradas CERRADA — ABIERTA

- **Origen:** `auditor-trazabilidad`, BLOQUE 0 del `redaccion/ENCARGO_2026-10-04.md`, ejecutado el
  2026-10-05. Reporte completo en `redaccion/rondas/paridad-r01-trazabilidad.md`. Alcance: las 36
  entradas CERRADA de este archivo, mas #130. Dos comprobaciones por entrada: paridad con
  `overleaf/secciones/` y recuento de cada cifra contra `experiments/`.
- **Saldo:** 9 hallazgos altos, 8 medios, 3 bajos. Las dos pruebas de control (#135 y #136) se
  detectaron, y las dos quedaron **ampliadas**.

#### 1. #135 no es un caso aislado: son cuatro sitios y cinco implicancias sin propagar

`overleaf/` sigue en estado pre-#132 en `capitulo3.tex` lineas **263**, **253**, **52** y **209**, y en
`introduccion.tex:82`. Dos de esos sitios son `\GAPDATO` que **declaran no hecho algo que esta hecho y
cerrado**: el cribado de fractura (`capitulo3.tex:52`, `introduccion.tex:82`) y la revision del recorte
de 6 mm (`capitulo3.tex:91`, `introduccion.tex:84`, que son #123 y #131). Lo mismo con #124
(`capitulo3.tex:97`, `\GAPDEC` ya resuelto) y #130 (`introduccion.tex:39`, `capitulo3.tex:101` y `:196`,
`capitulo1.tex:72`, `capitulo2.tex:74`).

**Por que importa mas que una omision:** un lector que abra el repositorio ve el CSV lleno mientras el
documento afirma que el dato no existe.

#### 2. DOS CIFRAS NUEVAS QUE NO CUADRAN, las dos dentro de entradas CERRADA

| Donde | Dice | El recuento da | Criterio del recuento |
|---|---|---|---|
| **#122**, encabezado (`:8490`) y cuerpo (`:8503`) | "16 de 72", "22% de la cohorte" | **15 de 72 (20.8%)** | `e13b_estratificado.md:9` dice 72 / 57 / **15**; `tesis/main.tex:109` dice "15 of the 72". El propio cuerpo de #122 explica que el 16 salia de usar `sap.D_SAP_MM` en vez de `D_TS_max`, y que el decimosexto (`CLINIC_0018`) tiene `D_TS_max = 7.0` |
| **#132 seccion 4** (`:9075`) | "21 casos con `fractura = si` (14 sacro, **7 ilion**)" | **20** (14 sacro, **6** ilion) | cruce de `r3_fractura_revisor.csv` con `r3_fractura_grupos.csv` por `Caso`, con `dudoso` aparte. Y si se contara el `dudoso` para llegar a 21, su columna `donde` esta **vacia**: la frase "no tiene huecos" se cae por los dos lados |

Ademas, en **#132** la tabla de `D_TS` por estado (`:9121-9125`) aplica la regla del `dudoso` **al
reves** que la fila que #136 corrigio: cuenta el dudoso **dentro** de "sin fractura", con lo que publica
n = 10 y mediana 6.7 mm donde la regla autorizada da **n = 9 y 5.9 mm**. Y la mediana de "desplazada"
es **6.25 mm**, no 6.2, sin declarar el redondeo.

**Lo que SI quedo verificado de #132:** el titular (20 de 30, 67%), los grupos (10 y 10), las sacras
(9 y 5), las desplazadas (7 y 2), las legibles (8 y 10), y **los tres valores p**, recalculados a mano
por la distribucion hipergeometrica: 0.109, 0.264 y 0.272.

#### 3. Un hallazgo alto que no venia de ninguna implicancia: alcance retirado afirmado como vigente

`overleaf/secciones/introduccion.tex` lineas **13**, **15** y **21** siguen afirmando **sintesis
condicionada bidimensional** y que **"se evaluara con Dice (DSC) y HD95"**. Las dos cosas estan
**FUERA DE ALCANCE** por `docs/00-tesis.md` y por el `CLAUDE.md` raiz, y `capitulo3.tex:36` ya lo dice
bien. El `\GAPDEC` de la linea 28 avisa, pero las tres frases siguen afirmandolo. Es #126, que es
decision de la autora; mientras se decide, afirmarlo es peor que marcarlo.

#### 4. Dos defectos de procedencia de lector

- `capitulo3.tex:164` dice "un segundo lector ciego a la profundidad medida" sin decir que el lector es
  **la autora** (`r2_nivel_pico_revisor.csv`, columna `revisor` = `autora` en las 18 filas). El estandar
  correcto lo fija #124 y esta aplicado en `main.tex:121`.
- `capitulo3.tex:91` e `introduccion.tex:84` atribuyen la revision del recorte **solo a la autora**;
  #131 la corrigio el 2026-10-04: fue la autora **con apoyo de un medico egresado (SERUM, sin
  especialidad)**. El sufijo `_autora` del archivo se conserva por compatibilidad y no acredita autoria
  unica.

#### 5. Tres problemas de etiqueta, no de contenido

- **#55, #62 y #130** aparecen ABIERTAS en su encabezado y CERRADA en una tabla resumen del mismo
  archivo. Un redactor que lea el encabezado las trata como GAP; uno que lea la tabla, como hecho.
  (El contenido de #55 y #62 ya esta propagado y bien matizado; no hay que tocar `overleaf/` por eso.)
- **El encargo cita la implicancia equivocada en su bloque A3:** atribuye a **#124** lo de "Herman es
  referencia de distribucion, no de equivalencia de implante". #124 es el 61 de 61 del nivel S1. El
  contenido de A3 es **#130 punto 3**. El contenido si tiene respaldo (`main.tex:52` lo trae aplicado;
  `docs/literatura/herman2016.md:167` acredita la mezcla de tipos), pero la cita es falsa.
- **#131 cita una frase literal que ya no existe en su fuente:** "se reconoce parte de la **medula**
  como parte de S1" (12 de 16). El CSV dice hoy "cresta sacra media", porque la autora corrigio la
  nomenclatura el 2026-10-04; el original esta en `e9ts_revision_laminas_autora.raw.csv`. El recuento
  de 12 si se sostiene.

#### 6. Un dato que no se pudo verificar

Las cifras de E14 que cita #131 (`outputs/e14_relleno.csv`, 152 casos, 0 casos de la cohorte cambian)
**no estan en disco en este arbol**: `NO ENCONTRADO EN LA FUENTE`. Solo constan en la propia #131.

#### 7. Ningun resultado del Objetivo 2 esta en el documento de entrega

`overleaf/secciones/capitulo4.tex` tiene cuatro secciones vacias. Los seis Wasserstein-1, las cuatro
distribuciones de grado y el 15/57 viven **solo** en `tesis/main.tex:109` y en `experiments/`. No es
fallo de #121 ni de #122: el capitulo no se ha redactado. Cuando se redacte, la fuente deben ser
`e13_sap.md` y `e13b_estratificado.md`, **no** el encabezado de #122 (ver seccion 2).

#### Pendiente de la autora (reglas 3 y 14). Esto NO se aplico

1. ~~**Corregir en este archivo** el encabezado de #122 y la seccion 4 de #132~~ **HECHO el
   2026-10-05 por instruccion de la autora.** #122 dice ahora **15 de 72 (20.8%)** en su encabezado y
   en su cuerpo; #132 tiene sus cuatro cifras corregidas en sitio y su aviso reescrito como tabla de
   "decia / dice". El recuento se rehizo de forma **independiente** desde los CSV antes de tocar nada,
   y coincide con el de esta auditoria en todo. Con esto **desaparece el riesgo que motivaba este
   punto**: un redactor que lea ahora la fuente de autoridad encuentra las cifras buenas. El aviso de
   #132 se conservo, reescrito como tabla de "decia / dice", porque explica de donde salieron las
   cifras que ya estan impresas en versiones anteriores del documento.
2. **Unificar la etiqueta de estado** de #55, #62 y #130.
3. **Decidir #126** (el alcance afirmado en `introduccion.tex:13`, `:15`, `:21`).
4. **Decidir si la cadena de custodia de las cifras necesita un control permanente**: dos de las tres
   cifras falsas halladas hasta hoy (#136, y las dos de esta entrada) estaban dentro de entradas
   **CERRADA**. `CERRADA` no equivale a verificado, y hoy nada lo comprueba salvo una pasada manual.
- **Tipo:** REDACCION + RIESGO DE TRAZABILIDAD. **No aplicado.**

### 141 — EL SUELO DE LA REPRESENTACION ESTA EN -1000 HU Y RECORTA LA PARTE DEL *UNDERSHOOT* QUE CAE POR DEBAJO: mediana del **1.0%** de los voxeles de la banda por paciente, pero **19 de 77 pasan del 10%** y uno llega al **44.9%**; y la metrica recortada es **`streak amplitude`** — ABIERTA (toca E-A1, E-A2, D4 y la codificacion congelada del Objetivo 1)

- **Origen:** `experiments/objetivo3/a8_muestra_serie.py`, 2026-10-05. Primera muestra de una **serie
  completa** de cortes (66 cortes consecutivos, 235 a 300, de `dataset7_CLINIC_metal_0011_data_c011`,
  paciente de **validacion**). El hallazgo salio de comparar los percentiles de HU, no de mirar la imagen.
- **No lo causa el modelo. Lo causa la representacion.** Control de ida y vuelta **sin modelo**, sobre
  el corte `k0263`:

| | real | ida y vuelta de la representacion |
|---|---|---|
| minimo de HU en `G` | **-6048** | **-1000** |
| voxeles por debajo de -1000 HU en `G` | **3148** de 12 408 | **0** |
| maximo de HU en `G` | 12 472 | **12 472** (exacto) |

  El techo sobrevive intacto; **el suelo destruye todo lo que hay debajo de -1000 HU**. La causa esta en
  una linea: `CONFIG_DISENO_A = 'pub+asinh'` (`src/common/ventanas.py`:44) es
  `asinh_canal(-1000.0, 20000.0)` (`experiments/objetivo1/e6c_techo_lw.py`:81), y su `ida` aplica
  `np.clip(h, low, high)` (`e6c_techo_lw.py`:66). **El recorte inferior es por construccion.**

#### Cuanto se pierde, medido sobre la serie entera

461 380 voxeles en `G` en los 66 cortes:

| Umbral | real | generado |
|---|---|---|
| < -1000 HU | **107 851 (23.4%)** | **0** |
| < -2000 HU | **63 540** | 0 |
| < -3000 HU | 2 821 | 0 |

Percentil 1 de HU en `G`: **-2605 real frente a -995 generado**. El minimo real de la serie es
**-7159 HU**.

#### Por que importa, y por que no se habia visto

Los HU muy negativos dentro de `G` **no son ruido ni aire**: son la **inanicion de fotones**, una de las
tres manifestaciones del artefacto metalico que el `CLAUDE.md` raiz y el glosario nombran explicitamente,
junto con el endurecimiento del haz y las rayas. **El Diseno A no puede generarla.** Las bandas oscuras
del artefacto quedan aplanadas al suelo del aire.

**No se habia visto porque E6c nunca lo puso a prueba:** las **nueve** configuraciones candidatas de
`configuraciones()` (`e6c_techo_lw.py`:73-80) comparten `low = -1000.0`. El suelo **no fue una variable**
del experimento; solo se estudio el techo, y por eso #39 lo subio de 2 000 a 20 000 HU y nadie miro hacia
abajo. Y la cifra de ida y vuelta del Objetivo 1 **no podia detectarlo**: se mide sobre **HU de hueso**
(`p1_compuerta.md`, `e6c_techo_lw.md`), donde el suelo no interviene.

#### Lo que esto NO dice

- **No invalida el Objetivo 1.** Su compuerta pregunta si la representacion conserva los HU **del hueso**,
  y eso sigue siendo cierto. Lo que queda en evidencia es que el criterio de la compuerta **no cubre** el
  rango negativo del artefacto.
- **No es un fallo de implementacion.** El recorte esta donde la decision lo puso. Es un **limite de
  alcance que hoy no esta declarado en ninguna parte del documento**.
- **No se midio con `mejor.pt`.** Es el `ckpt` de `run01` (paso 140 000, pasado de su optimo, #134). Pero
  **eso es irrelevante para este hallazgo**: el control de ida y vuelta no usa el modelo.

#### Lo que la serie completa SI muestra, y es la buena noticia

| | real | generado |
|---|---|---|
| voxeles > 2 500 HU en `G` | 28 377 | **26 923** (94.9%) |
| maximo de HU en `G` | 15 122 | 17 138 |
| HU mediano en `G` | -375 | -153 |

Los dos controles duros **pasan en los 66 cortes**: el parche del cache coincide voxel a voxel con la
ventana del volumen original, y la composicion es identica fuera de `G`. El modelo genera metal de rango
metalico a lo largo de toda la serie, no en un corte aislado.

#### Pendiente de la autora (reglas 3 y 14). Esto NO se aplico

1. **Decidir si el suelo de -1000 HU se declara como limitacion de alcance o se cambia la
   representacion.** Cambiarlo no es gratis: reabre la codificacion congelada del Objetivo 1, obliga a
   recachear los 23 058 parches y a reentrenar. Declararlo cuesta un parrafo en amenazas a la validez de
   constructo y una frase en el alcance.
2. **Decidir si E-A1 o E-A2 incorporan una comprobacion del rango negativo.** Hoy ningun bloque mide si
   la inanicion de fotones se reproduce, asi que el Diseno A puede "pasar" sus cuatro bloques sin generar
   una de las tres manifestaciones del artefacto.
3. **Si se decide medir el suelo:** la cifra barata es el percentil 1 de HU dentro de `G`, real frente a
   generado, que es como se detecto aqui.
- **Tipo:** SUPUESTO + ALCANCE + RIESGO. **No aplicado.**

#### AMPLIACION 2026-10-05: medido sobre los 77 pacientes, y el titular anterior sobreafirmaba

Las tres correcciones de abajo salen de revisar la recomendacion antes de ejecutarla, por pedido de
la autora, y de `experiments/objetivo3/a9_suelo_representacion.py` (nuevo). **El titular de esta
entrada quedo corregido**: decia que el suelo "borra la inanicion de fotones", y eso sobreafirma.
Recorta **la parte del *undershoot* que cae por debajo de -1000 HU**; las bandas oscuras por encima
de ese suelo si se representan.

##### 1. La prevalencia, medida sin modelo sobre entrenamiento y validacion

`a9_suelo_representacion.py`: **23 058 parches, 77 pacientes con metal** de los 134 de `train` y
`val`. **Ningun paciente de test**: el script aborta si se le pide, porque medir ahi para decidir
diseno violaria la *Strict Isolation Rule* (`main.tex`:111). La medicion es **ida y vuelta por la
representacion, sin modelo**, asi que no depende de ningun `ckpt`.

| Magnitud, por paciente | p50 | IQR | rango |
|---|---|---|---|
| voxeles de `G` bajo el suelo | **1.0 %** | 0.4 a 8.7 % | 0.0 a 43.4 % |
| voxeles de la **banda `G \ M`** bajo el suelo | **1.0 %** | 0.4 a 9.0 % | 0.0 a **44.9 %** |
| minimo de HU del parche | -3376 | -5385 a -2048 | -14 319 a **-1020** |
| fraccion del **vano** que sobrevive (mediana del paciente) | **0.999** | 0.989 a 1.000 | **0.498** a 1.000 |
| fraccion del vano que sobrevive (p5 del paciente) | 0.914 | 0.851 a 0.983 | **0.084** a 1.000 |

**La lectura es de cola, no de centro.** En el paciente tipico el recorte toca el **1 %** de la banda
y el vano sobrevive al **99.9 %**: eso solo no justifica tocar la representacion. Pero
**19 de 77 pacientes pasan del 10 %** de banda recortada, **9 pasan del 20 %**, **11 tienen un vano
mediano por debajo de 0.95** y **8 por debajo de 0.90**; en el peor (`dataset6_CLINIC_0054_data`) el
parche mediano pierde **la mitad del vano**. **El 23.4 % que origino esta entrada era un caso de la
cola alta, no el caso tipico.**

**Dato que impide un atajo:** la correlacion entre el minimo de HU del volumen y la fraccion
recortada es **-0.12**, practicamente nula. **Saber hasta donde baja un volumen no predice cuanto
pierde.** Hay 8 pacientes cuyo volumen ya viene recortado en origen (minimo por encima de -1100 HU,
recorte de 12 bits del propio CT) y para ellos la representacion no cuesta casi nada; y 22 que bajan
de -5000 HU. La heterogeneidad hay que medirla por paciente, no inferirla.

##### 2. LA METRICA RECORTADA ES `streak amplitude`, y eso es lo que eleva la gravedad

`docs/literatura/peters2025hybrid.md`:56, :173 y :174 la definen literalmente: *"the average over
the highest and lowest 5% CT number deviation to ground truth in each ROI is calculated"* y *"The
remaining streak amplitude is then defined as the difference between the two"* (§2.5, p. 5). Es
**el vano entre el lobulo claro y el lobulo oscuro**. No es una metrica que incidentalmente toque
los valores bajos: **esta definida como la distancia entre los dos extremos, y el suelo recorta uno
de los dos**. Peters et al. ademas eligen RMSE en otra metrica *"to avoid errors from light and dark
streaks canceling each other out"* (:163): el lobulo oscuro es objeto de primera clase en ese
protocolo.

**Consecuencia que no estaba declarada:** el sesgo es **de direccion conocida y siempre a la baja**,
y **afecta al brazo del sintetizador y no al brazo fisico**, que reconstruye y no pasa por esta
codificacion. Un TOST de equivalencia con un lado sesgado por construccion no mide lo que dice
medir. Eso toca **D4**, no solo la redaccion.

##### 3. SUSTITUCION DECLARADA: lo medido NO es `streak amplitude`

La definicion de Peters se calcula sobre la **desviacion respecto a la verdad de terreno**, que para
un paciente real con metal **no existe** (es lo que E-A2 resuelve usando casos de test sin metal), y
la inversion de sus metricas para sintesis sigue siendo `\GAPDEC` abierto (#16, #17). Asi que `a9`
mide la **forma** del estadistico sobre HU en la banda:

    S = promedio(5 % superior de HU) - promedio(5 % inferior de HU),  dentro de `G \ M`

y compara `S` del parche real contra `S` tras la ida y vuelta. **No es streak amplitude y no debe
citarse como tal.**

**Y el proxy probablemente SUBESTIMA el problema.** La banda contiene hueso y tejido blando, de modo
que su vano de HU lo domina el contraste hueso-aire y no el streak; las ROIs de Peters se trazan
**perpendiculares a los streaks fuertes** y miden desviacion, no HU crudo. Es decir: el 99.9 % de
supervivencia del paciente tipico es un **limite superior optimista**, no una cota tranquilizadora.
Medirlo como Peters lo define exige primero cerrar el `\GAPDEC` de la inversion.

##### 4. Lo que esto cambia en la recomendacion que estaba escrita

La version anterior de esta entrada proponia comparar la perdida contra el margen **`Delta`**.
**Eso era inaplicable:** `diseno_A.md` D4 define `Delta` como la variabilidad propia del metodo
—dispersion entre semillas DDIM y test-retest del brazo fisico— medida **solo en los 5 pacientes de
validacion** y escrita **antes** de evaluar, asi que necesita `mejor.pt` de `run02` y hoy no existe.
La regla correcta es de dos etapas, y su texto se entrego a la autora para `01-decisiones.md`
(regla 3): `run02` corre sin cambios, **las cifras de arriba se preinscriben hoy, antes de conocer
`Delta`**, y la comparacion se hace cuando `Delta` exista.

##### 5. DECIDIDA EN PARTE el 2026-10-05: la regla ya esta preinscrita en `01-decisiones.md`

La autora tomo la decision el mismo dia y pidio que se registrara; esta en
`docs/01-decisiones.md`, entrada **2026-10-05 — Suelo de -1000 HU de la representacion
multiventana**. Resumen de lo que queda cerrado y lo que sigue abierto:

| | Estado |
|---|---|
| `run02` corre con la representacion actual | **CERRADO** |
| cantidad que decidira, preinscrita antes de conocer `Delta` | **CERRADO** (0.999 mediana; 0.914 p5; 0.498 peor paciente; 19 de 77 sobre el 10 %) |
| estadistico de decision: percentil 5 del paciente, no la mediana | **CERRADO**, y declarado como eleccion post hoc |
| declarar o cambiar la representacion | **ABIERTO**: se resuelve al medir `Delta` tras el piloto de `run02` |
| redaccion en los tres sitios (alcance, amenazas, compuerta del Obj 1) | **ABIERTO**: su texto depende de la regla; hoy hay `\GAPDEC` en el cap. 3 y el cap. 1 |
| medir el vano como Peters lo define | **ABIERTO**: exige cerrar antes el `\GAPDEC` de la inversion de sus metricas (#16, #17) |

Esta entrada sigue **ABIERTA** porque la decision de fondo —declarar o cambiar— no esta tomada:
esta *condicionada por una regla escrita*, que es cosa distinta.

### 142 — EL EJE DEL CORREDOR SE BUSCA EN UNA REJILLA DE 5°, y la tolerancia angular que la tesis cita es de 1.53° ± 0.57°: la cuantizacion del eje es mayor que el margen que declara admisible — ABIERTA (toca D_TS_max, SAP y el W1 del Objetivo 2)

- **Origen:** al escribir `a11_rasterizar_tornillo.py` (2026-10-05) aparecieron ejes con componentes
  exactamente iguales entre casos (`u = [0.9924, 0.0868, 0.0868]` en dos pacientes distintos, y
  `u = [1, 0, 0]` exacto en un tercero). No era casualidad: `0.0868 = sin(5°)`.
- **Verificado en el codigo:** `experiments/objetivo2/e9_corredor.py`:80 define
  `ANGULOS = np.deg2rad(np.arange(-20, 20.01, 5))`, y `e9ts_corredor.py`:179-181 recorre
  `for a in ANGULOS: for b in ANGULOS: u = [1, tan(a), tan(b)]`. **El eje del corredor se busca en una
  rejilla de 5° en dos angulos, entre -20° y +20°.**

#### Por que importa

`main.tex` adopta de **`mclaren2021corridor`** las tolerancias angulares transiliosacras como el
elemento operativo que una descripcion cualitativa de zona segura no da: **1.53° ± 0.57° en S1** y
1.02° ± 0.33° en S2. Pero el eje sobre el que se construye todo esta determinado con un paso de 5°,
o sea **±2.5° de error de cuantizacion en el mejor caso**. Ese error es **mayor que la tolerancia
completa** que la tesis cita como margen angular admisible.

#### Lo que esto NO invalida

- **SAP sigue midiendo bien.** `sap.py` califica la brecha geometricamente sobre el eje que se le da,
  con un campo signado y un calibre. La medicion es exacta **para esa pose**; lo que es grueso es la
  afirmacion de que esa pose sea el eje optimo del corredor.
- **El W1 preinscrito no se recalcula por esto.** La corrida 52175 esta cerrada y su resultado es el
  que es.

#### Lo que si queda tocado

1. **`D_TS_max` es una COTA INFERIOR del diametro del corredor.** Una rejilla mas fina solo puede
   encontrar un corredor igual o mas ancho. Eso afecta a **#122** (15 de 72 no admiten el calibre de
   7.0 mm): parte de esos 15 podrian admitirlo con un eje mejor orientado. **No se toca la cifra**,
   pero su lectura cambia: es "no admite el calibre **con el eje hallado en la rejilla de 5°**".
2. **El muestreador perturba alrededor de un eje que ya esta desviado.** Si el eje base esta hasta
   2.5° fuera del optimo, las poses perturbadas acumulan ese sesgo y sus grados de brecha salen
   **sistematicamente peores** de lo que serian alrededor del optimo real. La direccion del sesgo es
   conservadora —el muestreador parece peor, no mejor— pero es un sesgo y no esta declarado.
3. **La redaccion.** `capitulo3` describe la busqueda del eje del corredor con un `\GAPDATO` por el
   algoritmo completo; el paso de la rejilla no aparece en ninguna parte del documento.

#### Pendiente de la autora (reglas 3 y 14). Esto NO se aplico

1. **Decidir si se declara o se refina.** Declararlo cuesta una frase en metodo y otra en amenazas a
   la validez. Refinarlo exige volver a correr E9-TS con un paso menor (p. ej. 1°), que son
   **64 veces** mas direcciones si se mantiene el rango de ±20° con paso 0.5°, o 25 veces con 1°.
   Antes de refinar conviene medir **cuanto cambia `D_TS_max`** en una muestra chica de casos: si no
   se mueve, la rejilla gruesa esta justificada por los datos y se declara con evidencia.
2. **Si se refina, afecta al Objetivo 2 entero** (corredor, poses, SAP, W1) y eso reabre una corrida
   preinscrita y cerrada. Es una decision de alcance, no de implementacion.
- **Tipo:** SUPUESTO + RIESGO. **No aplicado.**

### 143 — LA MASCARA `M` BINARIA TIENE UN SESGO DE VOLUMEN QUE DEPENDE DE LA ORIENTACION DE LA POSE: +0.15 % con eje oblicuo y +7.27 % con eje alineado a la rejilla, y el submuestreo no lo corrige — ABIERTA (toca E-A1, E-A2 y el reclamo C1)

- **Origen:** `experiments/objetivo3/a11_rasterizar_tornillo.py`, nuevo el 2026-10-05, el eslabon que
  faltaba para que la cadena del Objetivo 3 se pueda ejecutar (#139).
- **El codigo de la geometria esta bien.** Control separado: el volumen **fraccionario** (ocupacion
  media con rejilla de 4³ por voxel) coincide con el volumen analitico del solido dentro del
  **0.05 %** en los dos casos probados. El sesgo no viene de la formula.

#### La medicion

`diseno_A.md` seccion 6 define `M = voxeles cuyo centro cae dentro` y lo marca `[SUPUESTO]`, **sin
cuantificar su error**. Cuantificado:

| Caso | eje `u` | voxel | volumen binario frente al analitico |
|---|---|---|---|
| `dataset6_CLINIC_0101_data` | [0.9924, -0.0868, 0.0868] (oblicuo) | 0.90 mm | **+0.15 %** |
| `dataset6_CLINIC_0102_data` | [1, 0, 0] (alineado) | 0.98 mm | **+7.27 %** |

**Cincuenta veces mas sesgo, y la unica diferencia es la orientacion de la pose frente a la rejilla
de voxeles.**

#### Por que el submuestreo NO lo arregla

Se probo ocupacion por mayoria con 1, 2 y 3 subpuntos por lado: **+7.3 %, -2.2 %, +7.1 %**. Oscila,
no converge. La razon es estructural: el cuerpo tiene **~5 voxeles de ancho** (4.91 mm sobre ~0.98 mm)
y **ninguna mascara binaria a esa resolucion puede representar una seccion circular de 5 voxeles sin
un error de area de varios por ciento**. Con el eje oblicuo los errores de cada corte se cancelan en
parte; con el eje alineado el mismo error se repite en todos y no se cancela. El submuestreo elige
mejor los voxeles del borde, pero sigue eligiendo voxeles enteros.

#### Con que conecta

- **Es el espejo sintetico de C1.** El reclamo C1 dice que la geometria extraida por umbral de HU
  esta distorsionada —sobrecobertura en Xie et al., fragmentacion en la auditoria local— y por eso la
  geometria se modela parametricamente. Pero **la geometria parametrica tambien se discretiza**, y su
  error no esta medido en ninguna parte del documento. No es del mismo tamano (7 % frente a factores
  de 2), pero existe y es sistematico.
- **`main.tex` ya se preocupa por la seccion de metal:** advierte que un cilindro uniforme de
  6.5-8.0 mm *"would overstate the metal cross-section along the corridor by more than a factor of
  two"*. Con esa sensibilidad declarada, un sesgo del 7 % correlacionado con la orientacion merece
  una frase.
- **Afecta a `metal integrity`** de las metricas de Peters, que es la que mide si el metal esta donde
  debe: un sesgo de volumen que depende de la pose entra directo en esa metrica.

#### Pendiente de la autora (reglas 3 y 14). Esto NO se aplico

1. **Decidir si `M` se declara con su error de cuantizacion o si se cambia a una mascara fraccionaria.**
   Una `M` fraccionaria representaria el volumen con error < 0.1 %, pero **el Diseno A la necesita
   binaria**: `M` y `G` son canales binarios de la entrada del renderizador y `muestrea_ddim`
   multiplica por `g`. Cambiarlo no es un parametro, es rediseno.
2. **Si se declara, hay que decir que el sesgo depende de la orientacion**, no dar un numero unico.
   La cifra honesta es un rango medido sobre varias poses, no el 7.27 % de un caso.
3. **Medir el sesgo sobre la distribucion de poses del muestreador**, no sobre el eje central: las
   poses perturbadas son oblicuas casi siempre, asi que el caso malo (eje alineado) **puede ser raro
   en la practica**. Eso es barato de medir y cambiaria la gravedad.
- **Tipo:** SUPUESTO + RIESGO. **No aplicado.**

### AMPLIACION a #141, #16 y #17 — 2026-10-05: la definicion operativa de `streak amplitude` esta DECIDIDA, y el suelo pasa a ser una cifra reportada

`docs/01-decisiones.md`, entrada **2026-10-05 (3)**. Lo que cambia para estas tres entradas:

**#141.** El punto 2 de sus pendientes —si E-A1 o E-A2 incorporan una comprobacion del rango
negativo— queda **CERRADO**: se reporta, junto al endpoint, la **fraccion de voxeles de la ROI de la
imagen sintetica que quedan exactamente en el suelo de -1000 HU**. Si es apreciable, `streak
amplitude` se declara **cota inferior**, con numero y no con adjetivo. Ademas, **el brazo fisico
reconstruye y si puede bajar de -1000 HU**, asi que esa cifra **separa el limite de la representacion
del limite del modelo**, que es lo que convierte #141 de salvedad en medicion. Sigue ABIERTO su
punto 1: declarar el suelo como limitacion de alcance o cambiar la representacion, atado a la regla
contra `Delta`.

**#16 y #17.** El `\GAPDEC` de la **definicion operativa de la inversion de las metricas de Peters
para sintesis** queda cerrado **para `streak amplitude`**, que era la que bloqueaba a las demas: la
verdad de terreno es el CT limpio del mismo paciente, las ROIs se derivan de la pose y la unidad de
agregacion es el paciente. **Sigue abierto para `bone integrity` y `metal integrity`**, que no se
tocaron.

**Un defecto de diseno corregido por el camino.** `diseno_A.md` §7 listaba `streak amplitude` como
medible en **E-A1** (20 pacientes con metal). **No lo es**: su definicion exige desviacion respecto a
una verdad de terreno sin metal, que en un paciente con implante real no existe. La fila de E-A1 ya
quedo corregida —pasa a medir **discrepancia** frente al CT real— y la de E-A2 ampliada con la
definicion completa. Ese error llevaba en el documento desde que se escribio la tabla.

**Lo que esta decision NO fija, y por que importa:** faltan cuatro parametros de las ROIs (radios,
numero y separacion de planos, apertura del arco, guarda alrededor de `M`). **Se fijan sobre
validacion, nunca sobre test**, al congelar `diseno_A.md`. Hasta entonces la preinscripcion cubre el
**que** y el **contra que**, no el **con que parametros**, y asi esta escrito en la propia entrada.

**Dependencia nueva y declarada:** el contraste primario y el segundo componente de `Delta`
necesitan el **brazo fisico de Peters implementado**. La autora decidio implementarlo el 2026-10-05.
**Implementarlo no es validar XCIST**: la reimplementacion validada sigue fuera de alcance (#8), y lo
que se hace es reproducir un protocolo publicado documentando revision de codigo, configuracion y
ajustes de reconstruccion.

### 144 — EL CODIGO DEL BENCHMARK DE PETERS ESTA EN DISCO Y CONTIENE LA DEFINICION EXACTA DE `streak amplitude`: confirma la decision del 2026-10-05 (3) y cierra dos "NO ENCONTRADO EN EL PDF" de su ficha — ABIERTA (decision de la autora sobre como se cita)

- **Origen:** al preparar la implementacion del brazo fisico (2026-10-05) se reviso `repos/`, que la
  autora ya habia clonado: **`repos/xcist-main`** (commit `4cf3544`, 2026-03-27) y
  **`repos/xcist-example`** (commit `4993e87`, 2025-10-08), este ultimo con
  `AAPM_datachallenge/scoring/`.
- La ficha `docs/literatura/peters2025hybrid.md` dice en dos sitios que el detalle de la metrica
  *"habria que leerlo del codigo en GitHub"* y marca la licencia como `NO ENCONTRADO EN EL PDF`.
  **Las dos cosas estan en disco.**

#### 1. La licencia: BSD 3-Clause

`repos/xcist-main/LICENSE` y `repos/xcist-example/LICENSE`: **BSD 3-Clause, Copyright 2024, GE
Precision HealthCare**. Permite reutilizacion con atribucion y conservando el aviso. Eso **cierra** el
`NO ENCONTRADO EN EL PDF` de la fila de licencia, y con ello desaparece el riesgo de citar
reutilizacion sin base.

#### 2. La implementacion de referencia de `streak amplitude`, y CONFIRMA lo decidido hoy

`repos/xcist-example/AAPM_datachallenge/scoring/utils.py`:399, `metric_streak(img_mar, img_ref,
roi_amplitude)`:

```
diff_image = img_mar - img_ref
streak_values = diff_image[roi_amplitude == True]
streak_values.sort()
cutoff = int((len(streak_values)/(100/perc)))        # perc = 5
streak_distance = np.abs(np.mean(streak_values[:cutoff]) - np.mean(streak_values[-cutoff:]))
```

Cuatro precisiones que el PDF no da y que el codigo si:

| | Lo que dice el codigo | Frente a la decision 2026-10-05 (3) |
|---|---|---|
| campo | `img_mar - img_ref`: imagen bajo prueba menos referencia | **coincide**: `Delta = I_sintetica - I_original` |
| estadistico | `abs(media del 5 % inferior - media del 5 % superior)` sobre **todos** los voxeles de la ROI agrupados | coincide en forma; el codigo toma **valor absoluto**, asi que la metrica es **no negativa por construccion** |
| dimension | la ROI es **2D**: la funcion documenta *"2D MAR image"* | **precisa** la decision: el estadistico se calcula **por corte** y luego se agrega por paciente, que es justo la regla de agregacion ya fijada |
| voxeles minimos | `cutoff = int(n/20)`; con `n < 20` el corte vale 0 y la media de una lista vacia es `nan` | coincide con la guarda de `n >= 20` que ya usan `a10` y `a12` |

**Lo que esto cambia en el estatus de la metrica:** deja de ser una parafrasis del texto del paper y
pasa a ser **la definicion del codigo publicado**, con su commit anotado. La tesis puede decir que
calcula `streak amplitude` con la definicion de la implementacion de referencia, y eso es mas fuerte
que citar la frase del articulo.

**Y refuerza #141 con el signo del sesgo demostrado, no argumentado:** el campo es
`sintetica - referencia`, y el suelo de -1000 HU censura los valores bajos de la sintetica, de modo
que `media del 5 % inferior` queda **menos negativa** de lo que seria y `streak_distance` sale
**mas chica**. El sesgo a la baja que #141 declara se sigue de la formula, no de un razonamiento.

#### 3. Lo que el codigo NO resuelve

- **La ROI.** `metric_streak` **recibe** `roi_amplitude` como entrada: el codigo no la construye. Como
  se traza sigue siendo decision propia, y es lo que la entrada `2026-10-05 (4)` fijo sobre validacion.
- **La inversion de `bone integrity` y `metal integrity`** para sintesis sigue abierta. Nota de
  `scoring_metric.md`:15: `metal integrity` umbraliza con *"the highest non-metal value near the metal
  plus a margin 250 HU"* y mide cambio de volumen mas Dice contra la verdad sin artefacto. Ese umbral
  **depende del caso** y hay que decidir como se fija en sintesis.

#### Pendiente de la autora (reglas 3, 5, 10 y 14). Esto NO se aplico

1. **Actualizar la ficha `peters2025hybrid.md`** con la licencia BSD-3 y con la definicion del codigo,
   indicando que no salen del PDF sino del repositorio y con que commit. Por la **regla 10** las fichas
   se escriben con `lector-papers`, asi que no la toque.
2. **Decidir como se cita.** Citar codigo no es citar el articulo: hay que fijar si la tesis cita el
   repositorio con su commit, y si ese commit entra en `refs/raw/` (**regla 9**: ningun campo sin
   respaldo en el raw).
3. **Anotar los dos commits en la preinscripcion del brazo fisico**, porque `main.tex` ya promete
   documentar *"the code revision, configuration, reconstruction settings and access conditions"*.
- **Tipo:** REDACCION + SUPUESTO. **No aplicado.**

### 145 — LA PERDIDA DE VALIDACION NO ESTA ALINEADA CON LA FIDELIDAD EN HU: el checkpoint "mejor" (`mejor.pt`, paso 37 500) genera la MITAD del metal y DUPLICA la costura frente al sobreajustado (paso 140 000) — ABIERTA (cuestiona el criterio de seleccion de checkpoint y, con el, la decision B2)

- **Origen:** `a8_muestra_serie.py` corrido dos veces sobre **la misma serie, los mismos 66 cortes y la
  misma semilla**, cambiando **solo** el `ckpt`: `run01/ckpt.pt` (paso 140 000, pasado de su optimo) y
  `run02/mejor.pt` (paso 37 500, minimo de validacion). Comparacion pareada sobre el mismo ruido.
  Costura medida con `a10_costura.py`.

#### La medicion

| | `run01` paso 140 000 | `mejor.pt` paso 37 500 | real |
|---|---|---|---|
| voxeles > 2500 HU en `G` | **26 923** (94.9 % del real) | **15 540** (54.8 %) | 28 377 |
| HU mediano dentro del metal real | **4849** | 2922 | 4831 |
| HU mediano en la banda `G \ M` | -212 | -154 | -491 |
| MAE en HU dentro del metal real | **1688.1** | 3545.7 | — |
| MAE en HU en la banda `G \ M` | **534.3** | 571.3 | — |
| MAE en HU en `G` completa | **605.3** | 754.3 | — |
| exceso de costura, 3D | **+196.2 HU** | +435.4 HU | — |
| exceso de costura, mediana por corte | **+50.8 HU** | +62.6 HU | — |
| cortes con exceso > 100 HU | **16 de 66** | 22 de 66 | — |

**El checkpoint con MEJOR perdida de validacion es PEOR en las ocho filas.**

#### La hipotesis facil es falsa, y conviene dejarla descartada

La primera explicacion que se me ocurrio fue que la perdida esta dominada por la banda: `G` tiene
461 380 voxeles y solo **28 377 son metal (6.2 %)**, asi que minimizarla optimizaria el 94 % que no es
metal. **Medido, es falso:** `run01` gana tambien en la banda (534.3 frente a 571.3 HU). No es un
problema de ponderacion entre regiones.

#### Lo que queda como explicacion

La perdida de validacion mide **error de prediccion de ruido en un paso**, promediado sobre `t` con
semilla fija. La imagen sale de **50 pasos de DDIM**. Son dos cosas distintas, y que una baje no
implica que la otra mejore. Es un desacople conocido en difusion —la perdida y la calidad de las
muestras no ordenan igual los modelos— y aqui aparece medido en el proyecto, no citado.

#### La explicacion alternativa que NO se puede descartar con un paciente

`run01` entreno 107 000 pasos mas y **puede haber memorizado la apariencia de los implantes de
entrenamiento**. Si el implante de este paciente de validacion se parece a los de entrenamiento, su
ventaja seria memorizacion y **no generalizaria al test**. Con **una serie de un paciente** no se
puede separar "la perdida no mide lo que importa" de "el sobreajuste ayuda en este caso concreto".
**Esa es la pregunta del experimento que falta**, y es barata: repetir esta comparacion pareada sobre
los **5 pacientes de validacion** y mirar si el orden se mantiene.

#### CONSECUENCIA DIRECTA SOBRE B2, decidida hoy

**B2 (30 000 pasos) se eligio por el minimo de la perdida de validacion.** Si ese criterio no ordena
los modelos por fidelidad en HU, **la cifra se eligio con el instrumento equivocado**. Esto **no
invalida** la decision —sigue siendo una eleccion declarada sobre validacion, y 30 000 cae en una
meseta reproducida en dos corridas— pero **cambia el criterio con el que deberia haberse tomado**.
Lo honesto es que B2 quede **condicionada**: si la comparacion sobre los 5 pacientes confirma el
orden, el numero de pasos y la seleccion de checkpoint se deciden con una **metrica de apariencia
sobre validacion**, no con la perdida.

**Lo mismo vale para `mejor.pt`:** `guarda()` lo escribe en el minimo de la **perdida**. Si el criterio
cambia, el mecanismo de seleccion de checkpoint cambia con el.

#### Pendiente de la autora (reglas 3 y 14). Esto NO se aplico

1. **Correr la comparacion pareada en los 5 pacientes de validacion** antes de congelar
   `diseno_A.md`. Es local, sin GPU, y no toca test. **Es el experimento que decide esto y tambien B1.**
2. **Decidir el criterio de seleccion de checkpoint.** Seleccionar por una metrica de apariencia medida
   sobre validacion es legitimo y no toca test; seguir seleccionando por la perdida, sabiendo esto,
   habria que justificarlo.
3. **Si el criterio cambia, B2 se revisa**, y la entrada `2026-10-05 (2)` de `01-decisiones.md` necesita
   una nota que remita aqui.
- **Tipo:** SUPUESTO + RIESGO. **No aplicado.**

### 146 — BRAZO FISICO ARRANCADO: XCIST corre en local, el metal se proyecta JUNTO al paciente por desplazamiento de agua (cierra un pendiente de `main.tex`), y el script publicado NO corre tal como viene — ABIERTA (preinscripcion del brazo fisico)

- **Origen:** 2026-10-05, los cuatro pasos de arranque del brazo fisico, con los repos que la autora
  ya tenia clonados.
- **Revision de codigo, para la promesa de `main.tex`** (*"document the code revision, configuration,
  reconstruction settings and access conditions"*):

| | valor |
|---|---|
| `repos/xcist-main` | commit **`4cf3544`**, 2026-03-27 |
| `repos/xcist-example` | commit **`4993e87`**, 2025-10-08 |
| paquete | `gecatsim`, `setup.py` declara **1.6.8**, `xc.__version__` dice **0.1.8** |
| licencia | **BSD 3-Clause**, GE Precision HealthCare 2024, en los dos repos |
| instalacion | `pip install -e repos/xcist-main`, modo editable; dependencias: matplotlib, numpy, scipy, tqdm, coverage |
| binario | `libcatsim64.dll` presente; corre en Windows sin compilar |
| configuracion | `AAPM_MAR_{phantom,protocol,physics,scanner,recon}.cfg` |

**La discrepancia de version es un dato, no una curiosidad:** `1.6.8` frente a `0.1.8` significa que
**la cadena de citas no puede apoyarse en el numero de version**; el identificador reproducible es el
commit.

#### 1. PACIENTE Y METAL SE PROYECTAN JUNTOS. Cierra un pendiente declarado de `main.tex`

`main.tex` dice que *"the paper does not state whether patient and metal are projected jointly, which
this work verifies in the simulator code before reproduction"*. **Verificado** en
`simulation_scripts/run.py`: el fantoma se arma como **un solo volumen multimaterial de tres
componentes** y se simula en **una sola pasada** (`CatSim(...)` + `run_all()`):

| | material | mapa | `density_scale` |
|---|---|---|---|
| 1 | water | `phantom.vf` (paciente) | **+1.0** |
| 2 | water | `metal.vf` | **-1.0** (resta el agua donde va el metal) |
| 3 | `Ti` u otro | `metal.vf` | **+1.0** |

Es **desplazamiento de material antes de la proyeccion**, no pegado en el dominio de imagen. Eso es
lo que hace "hibrido" al protocolo, y es la receta que nuestro brazo fisico debe reproducir con el
tornillo parametrico: `M` como mapa de fraccion de volumen, restar agua, anadir la aleacion.

#### 2. El script publicado NO corre tal como viene

`run.py` aborta con `TypeError: Object of type float32 is not JSON serializable` al escribir
`sim.json`: `metaldiam = 2.*np.sqrt(metal.sum()/np.pi)` es `np.float32` y `mt_pixsize` lo hereda.
**El clon de `repos/` se deja INTACTO** —misma regla que `refs/raw/`— y el parche de una linea vive en
`experiments/objetivo3/peters/run.py`, anotado en el sitio exacto y con cabecera que declara de que
commit sale la copia. Reproducir el protocolo **exige ese parche**, y eso es parte de las "access
conditions" que `main.tex` promete documentar.

**Coste medido:** 1000 vistas a ~14 it/s, del orden de **70 s por corte** en CPU local.

#### 3. Dos cosas de `data_generation.md` que REFUERZAN el gap de la tesis

- **El metal del entrenamiento son formas fractales aleatorias, no implantes.** *"Metal masks were
  defined as random shapes synthesized by generating vertices of a random fractal shape"*: hexagono
  con puntos medios perturbados, mascara binaria de 256x256, diametro efectivo escalado, y
  *"inserted in random soft tissue or bone locations"*. Materiales: amalgama, acero inoxidable, cobre,
  cobalto, titanio. **Confirma con detalle lo que `main.tex` ya afirma** sobre colocacion aleatoria, y
  anade que **la geometria tampoco es realista**: ni colocacion restringida por anatomia (C2) ni
  geometria de implante (C1).
- **La geometria es 2D de UNA fila de detector.** *"1 detector row, 900 detector columns, 1000 views"*,
  con dispersion *"consistent with 64 detector rows"* y reconstruccion FDK con correccion de agua.
  Eso **cuantifica** por que extenderlo a un tornillo pelvico que abarca ~150 mm axiales es una
  adaptacion explicita y no una herencia de su validacion.
- El *"moderate frequency boosting filter"* que `main.tex` menciona como no cubierto por su validacion
  **esta confirmado** en ese documento.

#### Pendiente de la autora (reglas 3, 9, 10 y 14). Esto NO se aplico

1. **Decidir que se versiona.** `repos/` esta en el arbol sin commit. Un entorno XCIST completo es
   grande; si entra, con una regla explicita de que si y que no.
2. **Actualizar la ficha de Peters** con la licencia, la proyeccion conjunta y la discrepancia de
   version. Por la **regla 10** eso va con `lector-papers`.
3. **Como se cita el codigo** y si su commit entra en `refs/raw/` (**regla 9**).
4. **El umbral de `metal integrity`** depende del caso (*"the highest non-metal value near the metal
   plus a margin 250 HU"*, `scoring_metric.md`:15) y como se fija en sintesis sigue sin decidir.
- **Tipo:** BASELINE + REDACCION. **No aplicado.**

#### AMPLIACION a #141 y #146 — 2026-10-05: el suelo de -1000 HU afecta al contraste de REALISMO, casi no al TOST. Y corrige una afirmacion del asistente

Primera corrida del brazo fisico en local (#146), reconstruccion de 512x512 con un objeto de titanio,
comparada con la etiqueta sin metal que el propio repositorio trae. Cuerpo definido como `HU > -500`
sobre la etiqueta sin metal (93 963 voxeles):

| | con metal | sin metal (etiqueta) |
|---|---|---|
| minimo **dentro del cuerpo** | **-1083.8 HU** | -499.6 HU |
| voxeles < -1000 HU dentro del cuerpo | **9 373** | — |
| voxeles < -1200 HU en toda la imagen | **0** | 0 |
| maximo | 9 827.5 HU | 1 443.0 HU |

**El brazo fisico si produce *undershoot* por debajo de -1000 HU** —9 373 voxeles dentro del cuerpo,
frente a un minimo de -500 en la imagen sin metal: eso es inanicion de fotones, no ruido de aire—
**pero no baja de -1200 HU**. El CLINIC-metal **real** llega a **-7159 HU** (#141).

##### Lo que esto corrige

El asistente afirmo, al registrar #141 y al proponer la decision `2026-10-05 (3)`, que como el brazo
fisico reconstruye y puede bajar de -1000 HU, la fraccion censurada **separaria** el limite de la
representacion del limite del modelo. **Medido, el argumento se sostiene pero es mucho mas chico de lo
que se dijo:** en esta configuracion el brazo fisico solo usa ~84 HU por debajo de nuestro suelo. El
suelo **casi no sesga la comparacion contra el brazo fisico**.

##### La consecuencia operativa, que es mas util que la correccion

El sesgo del suelo **no afecta por igual a los dos contrastes** de la jerarquia fijada el 2026-10-05 (3):

| Contraste | Referencia | Cuanto le cuesta el suelo |
|---|---|---|
| **Primario, TOST** | brazo fisico, minimo ~-1084 HU | **~84 HU: despreciable** |
| **Realismo** | distribucion de CLINIC-metal real, minimo -7159 HU | **miles de HU: sustancial** |

Es decir: **el suelo de -1000 HU no pone en riesgo el endpoint primario; pone en riesgo el contraste
de realismo.** Eso reordena la gravedad de #141 y, de paso, debilita el argumento para cambiar la
representacion: el contraste que decide el exito del Objetivo 3 apenas lo nota.

##### Lo que NO se puede concluir con esto

**Una sola imagen, un solo objeto, un solo material.** El objeto es una forma fractal de titanio con
el diametro que fija `tgt_mtdiam` en su script. Acero inoxidable, cobalto o un objeto mas grande
producen mas inanicion de fotones y podrian bajar mas. **Esto no es una cota**, es una medicion de una
configuracion. Antes de apoyarse en ella hay que repetirla con los materiales densos de su lista
(amalgama, acero, cobre, cobalto) y con el diametro del tornillo de la tesis.

**Pendiente de la autora (regla 14):** si la regla de decision de #141 —comparar la perdida de vano
contra `Delta`— se evalua **contra el brazo fisico** (donde el suelo casi no pesa) o **contra la
distribucion real** (donde pesa mucho). La entrada `2026-10-05` de `01-decisiones.md` no lo distingue,
y ahora se sabe que la respuesta cambia segun cual se elija. **No se aplico.**

### 147 — LOS "5 PACIENTES DE VALIDACION CON METAL" SON 3 CON IMPLANTE Y 2 CON OBJETO INCIDENTAL, con un factor 23 entre su contenido metalico; y el `n` del contraste primario no es 14 — ABIERTA (toca `Delta`, D4 y mi propio experimento A13)

- **Origen:** doble, el 2026-10-05. `redactor-tesis` levanto en r07 una discrepancia de recuentos
  (5 / 8 / 3) al no poder escribir la cifra junto a los 30 000 pasos; y la salida de
  `a13_comparar_ckpt.py` la confirmo con los numeros.

#### 1. Composicion real del conjunto de validacion

La particion tiene **8 pacientes de validacion**. De ellos, **5 tienen metal cacheado** y solo **3 son
de `dataset7` CLINIC-metal**:

| Paciente | Cohorte | Metal en la serie elegida |
|---|---|---|
| `dataset6_CLINIC_0019_data` | dataset6 | **1 226 vox** |
| `dataset6_CLINIC_0102_data` | dataset6 | **1 870 vox** |
| `dataset7_CLINIC_metal_0011_data` | CLINIC-metal | **28 075 vox** |
| `dataset7_CLINIC_metal_0039_data` | CLINIC-metal | 3 463 vox |
| `dataset7_CLINIC_metal_0056_data` | CLINIC-metal | 13 011 vox |

`diseno_A.md` seccion 5 dice *"Validacion: 5 pacientes con metal"*. Es literalmente cierto y
**engañoso**: `dataset6` es la cohorte **sin osteosintesis** de este proyecto, asi que esos dos casos
aportan **objeto metalico incidental o cuerpo extrano, no un implante de osteosintesis**. Y el
contenido metalico va de **1 226 a 28 075 voxeles, un factor 23**.

#### 2. Por que importa, y no es cosmetico

- **`Delta` se mide sobre "los 5 pacientes de validacion"** (D4, y la regla preinscrita de #141 lo
  repite). Si dos de los cinco no tienen implante, **el margen de equivalencia del endpoint primario
  se calibra en parte sobre metal que no es el objeto de la tesis.**
- **Mi propio experimento A13 hereda el defecto.** Esta corriendo con los cinco y su recuento de
  ganadores pesa igual un objeto extrano de 1 226 voxeles que un implante de 28 075. **Es un fallo de
  diseno mio.** No hace falta relanzarlo: el CSV es por paciente, asi que el analisis se hara **dos
  veces**, con los 5 y restringido a los 3 de CLINIC-metal, y se reportaran los dos recuentos. Con 3
  pacientes ninguna prueba de signos dice nada, y eso tambien hay que decirlo.
- **La seleccion de serie por "mas metal" agrava el desequilibrio**, porque en los dos de `dataset6`
  el maximo disponible sigue siendo un objeto chico.

#### 3. El `n` del contraste primario NO es 14

Segundo hallazgo del redactor, independiente y del mismo tipo. **D4 fija el TOST sobre n = 14**, los
pacientes de test sin metal. Pero `main.tex` declara que **el brazo fisico corre sobre un subconjunto
reducido** de pacientes, y el numero de ese subconjunto sigue en `\GAPDEC` desde capitulo3-r01. El
contraste es **pareado contra el brazo fisico**, asi que su `n` **no puede ser mayor que el subconjunto
reducido**. Hoy el documento dice 14 en un sitio y "subconjunto reducido sin numero" en otro.

**Consecuencia:** la declaracion de potencia de D4 —*"n = 14 ... es muy posible que el resultado honesto
sea no se pudo concluir equivalencia con esta n"*— **esta calculada sobre una n que el diseno no
garantiza**. Si el subconjunto fisico es, por ejemplo, 6, la conclusion de no equivalencia pasa de
"posible" a casi segura, y eso cambia como se presenta el objetivo.

#### Pendiente de la autora (reglas 3 y 14). Esto NO se aplico

1. **Decidir si los dos pacientes de `dataset6` cuentan como validacion del renderizador**, o si
   `Delta` y la seleccion de checkpoint se miden solo sobre los **3** de CLINIC-metal. Las dos
   opciones son defendibles; lo que no es defendible es decir "5 pacientes con metal" sin decir que
   dos no llevan implante.
2. **Fijar el `n` del subconjunto del brazo fisico**, porque de el depende el `n` real del contraste
   primario y la declaracion de potencia.
3. **Corregir la frase de `diseno_A.md` seccion 5**, que hoy induce a error.
- **Tipo:** SUPUESTO + RIESGO. **No aplicado.**

#### CORRECCION a #147 — 2026-10-05: el conjunto de validacion del ENTRENAMIENTO son 3 pacientes, todos de CLINIC-metal. La version anterior de esta entrada estaba mal planteada

Recuento directo sobre los manifiestos, que son los artefactos que el entrenamiento **si** consume:

| | parches | pacientes | dataset6 | dataset7 |
|---|---|---|---|---|
| `a5_manifiesto_train.csv` | 17 149 | **47** | **0** | **47** |
| `a5_manifiesto_val.csv` | 896 | **3** | **0** | **3** |

**El entrenamiento y su validacion usan exclusivamente pacientes de `dataset7` CLINIC-metal.** Los
dos pacientes de `dataset6` con objeto metalico incidental **estan en el cache pero el criterio de
inclusion R1-R3 los dejo fuera**, y por eso no entran al entrenamiento ni a su validacion.

##### Lo que esto corrige de la version anterior de #147

Se dijo que "los 5 pacientes de validacion son 3 con implante y 2 con objeto incidental". **Mal
planteado.** Lo correcto:

- **La validacion del entrenamiento son 3 pacientes**, los tres con implante real: `0011`, `0039` y
  `0056`. No hay contaminacion por objeto incidental.
- **Los 5 salieron de MIS scripts, no del diseno.** `a9`, `a12` y `a13` cargan `ParchesMetal` **sin
  manifiesto**, con el argumento —escrito en `a8`— de que "el manifiesto decide que entrena, no que se
  puede generar". Para generar una muestra eso es correcto; **para medir sobre "el conjunto de
  validacion" no lo es**, porque el conjunto de validacion del diseno es el del manifiesto.
- **`diseno_A.md` seccion 5 sigue siendo incorrecta, pero por otra razon:** dice "Validacion: 5
  pacientes con metal" y el manifiesto da **3**. El 5 corresponde al cache, no al conjunto que se usa.

##### Consecuencias, y una toca a `Delta`

1. **`Delta` (D4) se mediria sobre 3 pacientes, no 5.** La regla preinscrita de #141 dice "los 5
   pacientes de validacion". Con el manifiesto son **3**, y eso reduce la base sobre la que se calibra
   el margen de equivalencia del endpoint primario. **Es una decision de la autora**, y es mas estrecha
   de lo que parecia.
2. **A13, que esta corriendo, mide sobre los 5.** Dos de esos pacientes **nunca estuvieron en la
   validacion del entrenamiento**. No hay fuga de test —los cinco son de la particion `val`— pero su
   recuento de ganadores no es "sobre el conjunto de validacion" en el sentido que D4 usa. **El
   analisis se hara igualmente dos veces**, y ahora se sabe que la lectura que corresponde al diseno es
   la de los **3** de CLINIC-metal, no la de los 5.
3. **El 47 de la saturacion queda confirmado**: son los 47 pacientes del manifiesto de entrenamiento,
   todos de CLINIC-metal.

**Pendiente de la autora (regla 14):** decidir si `Delta` y la seleccion de checkpoint se miden sobre
los **3** del manifiesto, o si se amplia la validacion a los 5 del cache declarando que dos aportan
objeto incidental. Y **corregir `diseno_A.md` seccion 5**, que dice 5 donde el manifiesto dice 3.
**No se aplico.**

#### CONFIRMACION de #145 — 2026-10-05: el orden se mantiene en los 5 pacientes de validacion. NO era un caso aislado

`a13_comparar_ckpt.py`, 120 generaciones: 12 cortes por paciente, los **mismos** cortes y la **misma
semilla** en los dos brazos, cambiando solo el `ckpt`.

| Magnitud | Gana | Recuento |
|---|---|---|
| MAE en HU dentro del metal | **`run01` (paso 140 000)** | **5 de 5** |
| MAE en HU en la banda | **`run01`** | **5 de 5** |
| fraccion del metal real reproducida | **`run01`** | 4 de 5 |
| exceso de costura | `mejor.pt` | 3 de 5 (mezclado) |

Por paciente, la fraccion del metal real reproducida:

| Paciente | `run01` 140 k | `mejor.pt` 37.5 k |
|---|---|---|
| `metal_0011` | **0.950** | 0.550 |
| `metal_0039` | **0.916** | 0.672 |
| `metal_0056` | **0.929** | 0.615 |
| `dataset6_0102` | **0.576** | 0.351 |
| `dataset6_0019` | 0.535 | **0.592** |

**Restringido a los 3 pacientes con implante real** —que es la lectura que corresponde al diseno, por
la correccion a #147— `run01` gana **3 de 3** en las tres magnitudes de HU, y por un margen grande:
reproduce entre el 92 % y el 95 % del metal frente al 55-67 % de `mejor.pt`.

##### Que queda establecido y que no

**Establecido:** lo de #145 **no era un caso aislado**. El checkpoint que la perdida de validacion
llama "mejor" produce sistematicamente menos metal y mas error en HU. Con 5 de 5 en las dos
magnitudes de MAE, la prueba de signos de una cola da **p = 0.031**, el limite que este diseno puede
alcanzar y que estaba declarado **antes** de ver el resultado.

**NO establecido, y sigue sin poder separarse:** si la causa es que **la perdida no mide lo que
importa** o que **`run01` memorizo** la apariencia de los implantes de entrenamiento y los de
validacion se le parecen. Los cinco son implantes pelvicos de la misma cohorte, asi que el parecido es
esperable. Separarlo exigiria un tercer modelo entrenado hasta un punto intermedio, o evaluar sobre
implantes de otra morfologia.

**La costura va al reves y es el unico contraste mezclado:** `mejor.pt` gana 3 de 5. Es coherente con
generar menos metal —menos metal, menos salto en el borde— y por eso no contradice lo anterior.

##### Consecuencias

1. **El criterio de seleccion de checkpoint no se puede dejar como esta.** Elegir por la perdida de
   validacion entrega, en los cinco pacientes, el modelo con mas error en HU.
2. **B2 (30 000 pasos) se eligio con ese mismo criterio.** La cifra sigue cayendo en una meseta
   reproducida en dos corridas, pero **el argumento que la sostiene es ahora mas debil**.
3. **B1 (la saturacion como limitacion declarada) no se puede afirmar con la curva de la perdida.**
   Esa curva no ordena los modelos por lo que la tesis mide. **Decidir B1 hoy seria declararlo con el
   instrumento equivocado.**

**Pendiente de la autora (regla 14):** decidir el criterio de seleccion —una metrica de apariencia
sobre validacion es legitima y no toca test— y si B2 se revisa. **No se aplico.**

### 148 — CORRECCION GRAVE a #134: `run01` y `run02` NO son corridas independientes. Usan la MISMA semilla, los mismos datos y tasa de aprendizaje constante: son la misma trayectoria calculada dos veces — ABIERTA (retira una afirmacion que ya se difundio)

- **Origen:** la autora pregunto por que, si `run02` es "mejor", sus imagenes se ven peor. Al
  verificarlo aparecio que la premisa de la pregunta —y la mia— estaba mal.
- **Verificado en los propios `ckpt`:**

| | `run01` | `run02` |
|---|---|---|
| `meta['semilla']` | **20260920** | **20260920** |
| lote | 16 | 16 |
| tasa de aprendizaje | `AdamW(lr=1e-4)`, **constante, sin planificador** (`entrenar.py`:150) | igual |
| `--pasos` | 200 000 (cortada en 144 500) | 60 000 |

`torch.manual_seed(args.semilla)` fija la inicializacion y el orden de los datos. **Sin planificador
de tasa de aprendizaje, `--pasos` solo decide donde se para.** Por lo tanto `run01` y `run02`
recorren **la misma trayectoria**; lo unico que las separa es la particion de GPU (no determinismo de
coma flotante), las dos correcciones de codigo —que tocan **como se mide y que se guarda**, no las
actualizaciones del modelo— y donde se detuvieron.

#### LO QUE HAY QUE RETIRAR

La ampliacion de #134 del 2026-10-05 afirma:

> "Dos corridas independientes trazan la misma curva de validacion" y "**El entrenamiento es
> reproducible.** No es una corrida con suerte ni una con mala suerte."

**Las dos frases son falsas.** Con la misma semilla no se puede concluir reproducibilidad ni
descartar que el resultado dependa de la inicializacion. Para eso harian falta **semillas distintas**,
y eso no se ha corrido.

**Donde se difundio y hay que corregir:** la ampliacion de #134, `docs/ESTADO.md`,
`docs/SITUACION_ACTUAL.md` (frente 1 y seccion 4) y el material que el asistente preparo para la
reunion con el asesor del 2026-10-05.

#### LO QUE SIGUE EN PIE, y es mas limpio de lo que se creia

**El estimador defectuoso no distorsionaba la curva promediada por bloques.** Y ahora el argumento es
**mejor**, no peor: como las dos corridas son la **misma trayectoria**, cualquier diferencia entre sus
curvas es **puramente de medicion**. Dos instrumentos distintos —el que sorteaba y el de semilla
fija— midiendo **el mismo modelo en los mismos pasos** coinciden dentro de **1.5e-3** por bloque. Eso
valida la practica de promediar por bloques de forma mas directa de lo que se habia argumentado.

Tambien sigue en pie que la **forma de U es real**: el estimador corregido la muestra. Lo que **no**
se puede decir es que se haya observado "dos veces" de forma independiente. **Se observo una vez, con
un instrumento bueno.**

#### Lo que esto NO cambia

Nada de #145 ni de su confirmacion: esa comparacion es entre **dos checkpoints** —paso 140 000 y paso
37 500— generando con la misma semilla sobre los mismos cortes. Que vengan de la misma trayectoria
**no afecta** a ese resultado; al contrario, lo hace mas interpretable, porque los dos puntos estan
sobre la misma curva y la unica variable es **cuanto se entreno**.

#### Pendiente de la autora (regla 14). Esto NO se aplico

1. **Decidir si se corre una tercera vez con otra semilla.** Es lo unico que sostendria una
   afirmacion de reproducibilidad. Coste: ~3 h 10 de GPU con los 30 000 pasos decididos.
2. **Corregir los tres documentos** donde la frase ya esta escrita.
- **Tipo:** SUPUESTO + RIESGO DE AFIRMACION. **No aplicado.**

### 149 — LA CADENA COMPLETA SE EJECUTO POR PRIMERA VEZ (cierra la parte ejecutable de #139), y el orden de los checkpoints SE INVIERTE respecto de la reconstruccion — ABIERTA (resultado preliminar, 2 cortes)

- **Origen:** `experiments/objetivo3/a15_cadena_completa.py`, nuevo el 2026-10-05. Encadena por primera
  vez **pelvis limpia -> pose del muestreador -> rasterizado de `M` -> `B_delta` -> generacion ->
  composicion**. Ninguna pieza es nueva: se importan `a11.rasteriza`, `a1b.ventana_coords`,
  `common.ventanas`, `common.region` y `difusion.muestrea_ddim`, de modo que la cadena usa **las
  mismas convenciones que el entrenamiento**.
- **Caso:** `dataset6_CLINIC_0101_data`, paciente de **validacion sin metal**, corredor de 10.6 mm,
  tornillo parametrico de 4.91 mm sobre el eje del corredor medido.

#### 1. La cadena FUNCIONA. Los tres controles pasan

| Control | Resultado |
|---|---|
| receptor limpio: voxeles del original en `G` sobre 2500 HU | **0** |
| lo generado es cero exacto fuera de `G` | **0.000e+00** |
| composicion identica fuera de `G` | **PASA** |

`M` = 4 788 voxeles, `G` = 173 182, diametro medido sobre la mascara 5.12 mm frente a 4.91 nominal.
El tornillo abarca **25 cortes axiales**, coherente con un tornillo transiliaco-transsacro: corre casi
en el plano, asi que su extension axial es la del diametro mas la inclinacion (~20 mm), no su longitud.

#### 2. EL DESPLAZAMIENTO DE DOMINIO ES SEVERO, y era lo que habia que medir

HU **dentro de la mascara del tornillo**, que es donde deberia haber metal (miles de HU):

| | `run01` paso 140 000 | `mejor.pt` paso 37 500 |
|---|---|---|
| HU mediano dentro de `M` | **471** | **472** |
| HU p95 dentro de `M` | 2 739 | 3 678 |
| **fraccion de `M` sobre 2500 HU** | **0.105** | **0.316** |

**Un HU mediano de ~471 dentro del tornillo no es metal: es densidad de hueso.** En la tarea de
reconstruccion, sobre implantes reales, `run01` reproducia el **95 %** del metal. Aqui, sobre una
pelvis limpia y con una mascara de cilindro liso, produce el **10.5 %**.

Las dos causas estaban registradas y **ninguna estaba medida**: el modelo aprendio apariencia en
pacientes que **ya tenian** streaking, y con mascaras de implantes **reales**, irregulares y recortadas
por umbral; aqui recibe una pelvis **limpia** y una mascara **parametrica lisa**.

#### 3. EL ORDEN DE LOS CHECKPOINTS SE INVIERTE

| Tarea | Gana |
|---|---|
| **reconstruir** un implante real (#145, 5 de 5 pacientes) | **`run01` paso 140 000** |
| **sintetizar** sobre pelvis limpia (esta entrada) | **`mejor.pt` paso 37 500**, 0.316 frente a 0.105 |

**Es exactamente la hipotesis que motivo la correccion del criterio de seleccion** en
`01-decisiones.md` 2026-10-05 (6): la ventaja de `run01` venia de **memorizar** la apariencia de
implantes parecidos a los de entrenamiento, y **no se traslada** al caso de uso de la tesis.

**Si se hubiera adoptado la primera version de esa recomendacion** —elegir por la fraccion de metal
reproducida en reconstruccion— **se habria elegido el checkpoint peor para sintetizar**. La correccion
evito ese error, y ahora hay medicion que lo respalda.

#### 4. Lo que NO se puede concluir todavia

**Son 2 cortes de 1 paciente.** La corrida completa de los 25 cortes esta en marcha. Y aunque
confirme el orden, sigue siendo **un paciente y una pose**. Antes de decidir el checkpoint hace falta
repetirlo sobre mas pacientes limpios de validacion y, segun la decision (6), **cotejar el perfil
radial y el histograma contra implantes reales**, no solo mirar la fraccion sobre 2500 HU.

**Y hay una lectura alternativa que no se puede descartar:** que **ningun** checkpoint sirva para
sintesis, y que la diferencia entre 10 % y 32 % sea la diferencia entre dos resultados igualmente
malos. Un 31.6 % de la mascara con HU de metal sigue estando lejos de un implante.

#### Pendiente de la autora (regla 14). Esto NO se aplico

1. **Decidir si el desplazamiento de dominio se ataca o se declara.** Opciones conocidas, ninguna
   gratis: entrenar con mascaras suavizadas o parametricas (reabre el conjunto de entrenamiento),
   anadir un brazo de sensibilidad con contexto recortado (#96 ya lo contempla), o declararlo como
   limitacion y reportar la cifra.
2. **Repetir sobre los otros pacientes limpios de validacion** antes de cualquier conclusion.
3. **Esta entrada cierra la parte ejecutable de #139**: la cadena ya no es un hueco. Lo que queda
   abierto es su **calidad**, que es otra cosa.
- **Tipo:** SUPUESTO + RIESGO. **No aplicado.**

#### CORRECCION a #149 — 2026-10-05: las fracciones 10.5 % y 31.6 % salen de **19 voxeles**. No sostienen la comparacion que el asistente hizo con ellas

Al parar la corrida se leyo el CSV de la prueba de humo y aparecio la columna `n_M`:

| etiqueta | `n_M` | frac sobre 2500 HU |
|---|---|---|
| `run01_140k` | **19** | 0.1053 |
| `mejor_37k` | **19** | 0.3158 |

**`n_M = 19`**: la prueba genero **2 cortes**, y en esos dos cortes la mascara del tornillo tiene
**19 voxeles**. Asi que el 10.5 % son **2 voxeles** y el 31.6 % son **6**. La diferencia entre los dos
checkpoints es **de cuatro voxeles**.

##### Lo que hay que retirar de #149

- **La tabla de la seccion 3 y la afirmacion de que "el orden de los checkpoints se invierte".** Con
  19 voxeles no se sostiene ninguna comparacion. El asistente la presento como un hallazgo y
  **la escribio tambien en el chat con la autora**.
- **La frase de que la correccion del criterio de seleccion "evito ese error" con medicion que lo
  respalda.** La hipotesis sigue siendo razonable y la correccion sigue siendo correcta por su
  argumento, pero **la medicion que se invoco no la respalda**.

##### Lo que SI se sostiene de #149

- **La cadena se ejecuto y los tres controles pasan.** Eso no depende del tamano de la muestra: el
  receptor esta limpio, lo generado es cero exacto fuera de `G` y la composicion es identica fuera de
  `G`. **La parte ejecutable de #139 sigue cerrada.**
- **El HU mediano dentro de `M` es ~471 en los dos checkpoints**, que es densidad de hueso y no de
  metal. La mediana sobre 19 voxeles es debil, pero **los dos coinciden** y el valor esta a un orden de
  magnitud del metal real: como senal de que hay un problema, vale; como cifra citable, no.
- La geometria: 25 cortes con `M`, 4 788 voxeles en el volumen completo, diametro medido 5.12 mm.

##### Por que paso, y como se evita

La fraccion se calcula **solo sobre los cortes generados** (`sel` restringe `M` a `ks`). Con
`--cortes 2` eso deja 19 voxeles, y el script **no avisa** de que la muestra es insuficiente. Dos
arreglos, ninguno hecho:

1. **`a15` deberia negarse a emitir estadisticos con `n_M` por debajo de un minimo declarado**, igual
   que `a10` y `a12` exigen 20 voxeles por anillo.
2. **La corrida completa de 25 cortes no llego a escribir nada**: el script no guarda por corte, asi
   que al pararlo se perdio lo avanzado. **No es reanudable**, a diferencia de `a8`.

**Pendiente de la autora (regla 14):** nada que decidir aqui; es deuda tecnica del script y una
correccion de registro. **No se aplico.**

#### Segunda correccion a #149 (2026-10-05, corrida completa de `a15`, PARCIAL: solo `run01_140k`)

**Retira el bullet "el HU mediano dentro de `M` es ~471 en los dos checkpoints" de "Lo que SI se
sostiene".** La corrida completa sobre `dataset6_CLINIC_0101_data` (25 de 25 cortes con `M`, 4 788
voxeles en el volumen; el `n_M` exacto lo confirmara `..._resumen.csv` al terminar) da, para
`run01_140k`:

| | prueba de humo (2 cortes, `n_M = 19`) | corrida completa (25 cortes) |
|---|---|---|
| HU p05 dentro de `M` | 468 | **2384** |
| HU p50 dentro de `M` | 471 | **3409** |
| HU p95 dentro de `M` | 2739 | **4853** |
| fraccion sobre 2500 HU | 0.105 | **0.938** |

Fuente: `experiments/objetivo3/outputs/a15/a15_0101.log`, linea `HU dentro de M: p05 2384 | p50 3409
| p95 4853 | fraccion sobre 2500 HU: 0.938`. La prueba de humo se archivo en `outputs/a15/humo_2cortes/`.

**Lectura:** el ~471 no era una propiedad del checkpoint sino de los 2 cortes que tocaron (probablemente
los extremos del tornillo, donde `M` es una seccion parcial: hipotesis NO verificada). Con la muestra
completa, `run01_140k` **si** genera densidad de metal dentro de `M`. Es el mismo error de muestra chica
que ya registro la primera correccion, ahora en la cifra que esa correccion habia dejado en pie.

**Lo que NO se puede decir todavia:** nada sobre `mejor_37k` ni sobre el orden entre checkpoints; su
generacion esta en curso. Tampoco que 3409 HU sea "correcto": el criterio de la decision (6) es el
cotejo contra el perfil radial y el histograma de implantes reales (`a12`), que no se ha hecho.

**Afecta:** `docs/ESTADO.md` (bloque de traspaso, "Lo que si se sostiene") repite el ~471; se corrige
ahi. No se ha propagado a `overleaf/` ni a `tesis/main.tex` (verificado con grep).

**Pendiente de la autora (regla 14):** nada que decidir; correccion de registro. Estado de #149 sigue
ABIERTA.

### 150 — CADENA COMPLETA SOBRE `0101` (25 cortes, los dos checkpoints) y EL COTEJO DE LA DECISION (6) NO ES CALCULABLE CON LO QUE HAY: el perfil de `a15` y el de `a12` miden cosas distintas — ABIERTA (toca el criterio de seleccion de checkpoint; supuesto sin documentar)

- **Origen:** `a15_cadena_completa.py --caso dataset6_CLINIC_0101_data --cortes 0`, 2026-10-05,
  ~70 min de CPU (el estimado del script, 43 min, se quedo corto). Salidas en
  `experiments/objetivo3/outputs/a15/`. Codigo de salida 0: **los controles 1, 2 y 3 pasan** en los
  50 cortes generados (2 y 3 abortan si fallan).

#### La medicion (un paciente, un tornillo, `n_M = 4 788` voxeles en los dos checkpoints)

Fuente: `a15_dataset6_CLINIC_0101_data_resumen.csv`.

| HU dentro de `M` | `run01_140k` | `mejor_37k` |
|---|---|---|
| p05 | 2384 | **235** |
| p25 | 2978 | **472** |
| p50 | 3409 | 3014 |
| p95 | 4853 | 4602 |
| fraccion > 2500 HU | 0.938 | **0.676** |

Perfil radial (cascaras de 1 mm desde `M`, dentro de `G`), mediana de HU, fuente `..._perfil.csv`:
0-1 mm: `run01_140k` 1644, `mejor_37k` 873. A partir de 2 mm los dos perfiles difieren en menos de
~25 HU en la mediana (p.ej. 3-4 mm: 62.5 frente a 62.7).

**Lo que se sostiene:** con el mismo tornillo y la misma semilla, `mejor_37k` deja **al menos un cuarto
de `M` en densidad de hueso** (p25 = 472 HU), y `run01_140k` no (p05 = 2384). Es la misma direccion que
#145 midio con `a8` sobre otro paciente (`0011`), ahora en la cadena completa con pose sintetica.

**Lo que NO se sostiene todavia:**
- Nada generalizable: **un paciente**, y los 4 788 voxeles **no son independientes** (un solo solido,
  una sola semilla). La unidad es el paciente (decision (3)); `n = 1`. `0102` en curso.
- **Que `run01_140k` sea "mejor"**: el criterio de (6) es el parecido con implantes reales, no tener
  mas HU. Ese cotejo no se ha hecho, y por lo de abajo no se puede hacer tal como esta.

#### El problema: los dos perfiles no son comparables

`a12_perfil_radial_val.csv` (la referencia real) y el perfil de `a15` difieren en definicion:

| | `a12` (real) | `a15` (sintetico) |
|---|---|---|
| distancia a `M` | **2D**, en el plano del corte | **3D** (`distance_transform_edt` sobre el volumen) |
| region del anillo | anillo completo, sin restringir | interseccion con `G` (por su tamano, 173 182 voxeles, parece ser casi toda la banda de 12 mm: NO verificado) |
| ancho de cascara | 0.5 mm (`--paso-mm 0.5`) | 1.0 mm |
| agregacion | mediana por parche -> por paciente -> entre pacientes | todos los voxeles juntos, un paciente |
| pacientes | 5 de validacion, **incluidos los 2 con objeto incidental** (#147) | 1 |
| histograma dentro de `M` | **no lo calcula** | si |

Consecuencia visible: lejos del metal, `a12` baja a ~ -500 HU y `a15` se queda en ~13 HU. **La causa
no esta verificada**: puede ser la anatomia distinta alrededor de implantes reales (placas, objetos
incidentales cerca de piel) frente a un tornillo dentro del corredor, o la diferencia 2D/3D. Mientras
no se separe, comparar esas curvas mezcla diferencia de ROI con diferencia de artefacto. Y para el histograma dentro de `M` **no existe hoy referencia real** en `a12`
(el 4 831 HU de #145 es otra medida: dentro del metal real de un paciente, con `a8`).

**Supuesto que falta (regla 8):** la decision (6) dice "perfil radial e histograma dentro de `M`
contra implantes reales" pero no fija **una definicion comun** de los dos estadisticos (2D/3D, region,
ancho, agregacion, que pacientes cuentan como "implante real"). Sin eso, cualquier eleccion la hace el
script por defecto.

**Pendiente de la autora (regla 14):** decidir la definicion comun; texto propuesto en el chat. **No se
aplico nada:** no se modifico `a12` ni `a15`.

### 151 — `a15` PASA A GPU EN KHIPU: con la misma semilla CPU y GPU generan ruido distinto, asi que `0101` se REPITE en GPU y la corrida CPU queda solo como control — ABIERTA (comparabilidad entre pacientes del cotejo de la decision (6))

- **Origen:** `0102` murio en la laptop por memoria baja (2026-10-05); la autora pidio correr en Khipu
  (2026-10-06). `a15` era solo CPU; se le anadio `--dispositivo` (por omision `cpu`, el comportamiento
  previo no cambia) y `experiments/objetivo3/a15_cadena.sbatch`, que corre `0101` y `0102` en `cuda`.
- **Por que importa:** `muestrea_ddim` crea `torch.Generator(device=...)`; el generador de CUDA no
  reproduce la secuencia del de CPU. **Mismas semillas, distintas muestras.** Si un cotejo mezclara
  `0101` en CPU con `0102` en GPU, parte de la diferencia entre pacientes seria del dispositivo.
- **Regla operativa:** un solo dispositivo por cotejo. Salidas GPU en `$DATA/a15_gpu/` ->
  `outputs/a15_gpu/`; las CPU siguen en `outputs/a15/`. **Las cifras de #150 son CPU.**
- **Lo que se gana:** `0101` CPU frente a `0101` GPU es una comparacion de **dos semillas efectivas**
  sobre el mismo tornillo; dice algo de la variabilidad entre muestras (insumo de `Delta`, D4), aunque
  con `n = 1` paciente no la estima.
- **Pendiente de la autora (regla 14):** confirmar que el cotejo se hace con las corridas GPU. **No se
  aplico nada** a `00-tesis.md` ni a `main.tex`.

#### Adenda a #150 (2026-10-06): corrida GPU en Khipu, job 54619 — PRELIMINAR, fuente: log

Fuente: `~/metalsynth/a15cad_54619.log` (Khipu), pegado por la autora; **los CSV aun no estan en
local y el `n_M` no esta verificado** (el log no lo imprime). Job `COMPLETED`, rc=0, **3 min 58 s**
para los dos pacientes en A6000 (frente a ~70 min de CPU para `0101` solo). CONTROL 1 PASA en ambos.

| HU dentro de `M` | `0101` CPU (#150) | `0101` GPU | `0102` GPU |
|---|---|---|---|
| `run01_140k` p05 / p50 / frac>2500 | 2384 / 3409 / 0.938 | 472 / 3360 / 0.911 | 2629 / 3179 / 0.973 |
| `mejor_37k` p05 / p50 / frac>2500 | 235 / 3014 / 0.676 | 234 / 2642 / 0.526 | 234 / 2858 / 0.642 |

**Lo que sugiere (sin cerrar):**
- En las tres corridas `mejor_37k` deja menos de `M` sobre 2500 HU que `run01_140k`, y su p05 cae a
  ~234 HU en las tres. La direccion de #145 se repite en un segundo paciente.
- **La variabilidad entre semillas efectivas no es despreciable.** `0101` CPU frente a GPU es el mismo
  tornillo con otro ruido (#151): la fraccion de `mejor_37k` pasa de 0.676 a 0.526 y el p05 de
  `run01_140k` de 2384 a 472. Cualquier diferencia entre checkpoints hay que leerla contra ese
  margen, que es el insumo de `Delta` (D4) y **no esta estimado** con dos muestras.
- **Coste:** con ~2 min por paciente en GPU, repetir con varias semillas por paciente es barato. Eso
  cambia lo que es factible para estimar `Delta`; la decision de hacerlo es de la autora.

**Lo que NO se sostiene:** ninguna eleccion de checkpoint (el cotejo de la decision (6) sigue
bloqueado por la definicion comun, arriba), ni cifra citable hasta leer los CSV con su `n_M`.

### 152 — EL "HUESO DENTRO DE `M`" ES UN EFECTO DE LA DECODIFICACION MULTI-VENTANA: los voxeles bajos de `M` se apilan exactamente en los techos de SW (236 HU) y MW (472 HU) — ABIERTA (toca #145, #149, #150, la metrica `frac_sobre_2500` y la `regla` del Objetivo 1)

- **Origen:** lectura de los CSV del job 54619 (GPU, `outputs/a15_gpu/`). Valores casi identicos
  (~234 y ~471 HU) se repetian como percentiles en pacientes, semillas y dispositivos distintos.
- **Mecanismo (verificado en el codigo):** `regla` (`e6b_vae_sd15.py:111`) decodifica con el canal
  mas estrecho cuyo `u` este en `[EPS, 1-EPS]`, `EPS = 0.01`. Con SW = (-160, 240) y MW = (-320, 480)
  (`e6c_techo_lw.py:42-43`), un `u` justo por debajo de 0.99 da **236 HU** (SW) o **472 HU** (MW),
  aunque LW diga metal. Un canal "casi saturado" gana sobre LW.
- **Medicion (histograma de HU dentro de `M` en los `.nii.gz` sinteticos GPU):**

| | `n_M` | en [200, 236.5] (techo SW) | en [440, 472.5] (techo MW) | > 2500 | resto |
|---|---|---|---|---|---|
| `0101` `run01_140k` | 4788 | 0.000 | 0.069 | 0.911 | 0.020 |
| `0101` `mejor_37k` | 4788 | **0.359** | 0.078 | 0.526 | 0.037 |
| `0102` `run01_140k` | 4657 | 0.000 | 0.018 | 0.973 | 0.008 |
| `0102` `mejor_37k` | 4657 | **0.222** | 0.083 | 0.642 | 0.052 |

  En `mejor_37k` el bin de 8 HU mas poblado por debajo de 600 es **232-240** (1669 y 1001 voxeles);
  entre los techos y el metal casi no hay nada (`resto` <= 5 %). La distribucion es trimodal por
  construccion del decodificador, no un continuo de densidades.

#### Lo que hay que retirar o requalificar

- **"Densidad de hueso, no de metal"** (#149, ESTADO): esos valores son techos de ventana. Tambien el
  ~471 de la prueba de humo era el techo de MW.
- **#145 "`mejor.pt` genera la mitad del metal"** y la fraccion > 2500 de #150: miden **modelo +
  `regla`**, no solo el modelo. La diferencia entre checkpoints puede estar en cuantos voxeles dejan
  SW/MW *casi* saturados, no en si generan metal en LW.

#### Lo que NO se sabe todavia

- **Que dice LW en esos voxeles.** Los `.nii.gz` guardan HU ya decodificado; los `u` crudos no se
  guardaron. Si LW marca metal, el modelo genero metal y la `regla` lo borro; si LW tambien es bajo, el
  modelo no lo genero. **Es la verificacion que decide** y requiere regenerar guardando `u` (en GPU,
  ~2 min por paciente).
- Si pasa igual en datos reales: en el Objetivo 1 la `regla` se valido en ida y vuelta por el VAE,
  donde un canal saturado suele quedar en 1.0 y no en 0.98. La difusion puede dejar mas valores en esa
  franja.

**Pendiente de la autora (regla 14):** autorizar la verificacion de LW (cambio en `a15` para guardar
`u`, regenerar). Cualquier cambio de `EPS` o de la `regla` toca un componente congelado del Objetivo 1
y es decision suya. **No se aplico nada.**

#### Adenda a #152 (2026-10-07): QUE MARCA LW en los voxeles de techo — respondido para `0101` (CPU)

- **Origen:** `a15` con las marcas crudas (`--sin-nifti`, CPU, laptop), `0101`, 25 cortes, los dos
  checkpoints. Salidas: `outputs/a15_marcas/` (`_marcas.npz`, `_resumen.csv`), log
  `outputs/a15_marcas_0101.log`. **Reproduce bit a bit el resumen CPU de #150** (0.9382 y 0.6761):
  la corrida CPU es determinista y las marcas corresponden a las mismas muestras.

| `0101`, CPU, `n_M = 4788` | `run01_140k` | `mejor_37k` |
|---|---|---|
| voxeles en techo SW | 0 | 773 (0.161) |
| ... de ellos con LW > 2500 HU | — | **0.957** (LW p50 3219 HU) |
| voxeles en techo MW | 169 (0.035) | 617 (0.129) |
| ... de ellos con LW > 2500 HU | **0.959** (LW p50 3091 HU) | **0.951** (LW p50 3108 HU) |
| `frac_sobre_2500` con la `regla` | 0.938 | 0.676 |
| `frac_sobre_2500` con **LW sola** | **0.972** | **0.953** |

Fuente: lineas `techo SW: ...`, `techo MW: ...` y `LW sola en toda M: ...` del log. En los voxeles de
techo, el canal estrecho elegido queda justo bajo el umbral (`u_MW` p50 0.989, `u_SW` p50 0.989).

**Lectura:** en ~95 % de los voxeles de techo **LW marca metal**: el modelo genero metal y la `regla`
lo sustituyo por el techo de un canal casi saturado. La diferencia entre checkpoints en
`frac_sobre_2500` pasa de **26 puntos con la `regla`** a **2 puntos con LW sola**. La mayor parte de
"`mejor.pt` genera la mitad del metal" (#145) es **del decodificador, no del modelo**.

**Lo que NO se sostiene todavia:** un paciente, una semilla, CPU; los voxeles no son independientes.
`0102` y las corridas GPU no tienen marcas. "LW sola" es un diagnostico, **no una propuesta de
decodificador**: cambiar `regla` o `EPS` toca el Objetivo 1 congelado y es decision de la autora.
Tampoco se sabe si el mismo efecto ocurre en los voxeles **fuera** de `M` (en `B_delta`, donde el
artefacto real vive en el rango de MW y SW).

**Memoria (laptop, 12 GB):** pico de python 3.77 GB al cerrar el primer checkpoint; **minimo de RAM
libre 327 MB** a las 00:04, con python en 1.2 GB (otro proceso del sistema). Paso cerca del corte.

#### Adenda 2 a #152 (2026-10-07): propuesta de `regla` v2 — SIN DECIDIR

La autora quiere cambiar la `regla`. Propuesta del asistente (texto completo en el chat): **LW como
ancla**; MW/SW solo si no saturan **y** `|hu_canal - hu_lw| <= tau_canal`. Se descarta bajar `EPS`
(traslada el problema y sacrifica SW en 220-240 HU). Lo que abre:
- **`tau_canal` NO esta medido**: depende de la imprecision de LW por rango, a sacar de datos del
  Objetivo 1. Hasta medirlo, cualquier valor seria inventado.
- **Toca la redaccion del Objetivo 1** si P1 se reevalua con la v2 (propuesta: conservar v1 como
  resultado de O1 y reportar ambas).
- **Riesgo de circularidad:** la v2 no puede elegirse por el resultado de `a15`; solo por identidad
  exacta e ida y vuelta sobre CT reales.
**Pendiente de la autora (regla 14):** aprobar o no; texto de decision propuesto en el chat. No se
aplico nada.

#### Adenda 3 a #152 (2026-10-07): `regla_suave` (v2) IMPLEMENTADA, `delta` SIN FIJAR

- La autora eligio la **mezcla suave** (no la de tolerancia `tau`). Implementada en
  `src/common/ventanas.py` (`peso_borde`, `regla_suave`); `decodifica_bloque(..., delta=None)` sigue
  aplicando la v1 por omision. `a15` gano `--delta`. **`e6b_vae_sd15.py` (Objetivo 1) no se toco.**
- **No modifica lo publicado del Objetivo 1:** sus cifras salen de `e6b_vae_sd15.regla` via
  `p1_decodificador_sd15.py:217`, y su descripcion ("canal mas estrecho no saturado",
  `capitulo3.tex:62`, `main.tex:77`) sigue siendo exacta para O1. **Si cambia:** el Objetivo 3 debera
  declarar que lee con la v2 (redaccion pendiente, decision de la autora).
- **Controles:** identidad exacta pasa para `delta` en {0.01, 0.02, 0.05, 0.10, 0.20}, peor error
  1.27e-11 HU, igual que la v1; con `delta = EPS` la v2 es identica a la v1 (max |dif| = 0.0 sobre
  200 000 `u` aleatorios). La v1 es un caso particular de la v2.
- **Abierto:** el valor de `delta`. Fija la zona de confianza plena de cada canal estrecho:
  SW en HU `[-160 + 400*delta, 240 - 400*delta]`, MW en `[-320 + 800*delta, 480 - 800*delta]`. No debe
  elegirse por el resultado de `a15` (circular).

#### Adenda 4 a #152 (2026-10-07): criterio para fijar `delta`, REGISTRADO ANTES DEL RESULTADO

La autora delego la eleccion de `delta` "tras una eleccion minuciosa". `a16_calibrar_delta.py`:
- **Datos:** reconstruccion sobre los 5 pacientes de validacion con metal real (serie de mas metal,
  6 cortes repartidos, como `a13`), los dos checkpoints, semilla 0, 50 pasos. Verdad = `x0`.
  **`a15` no interviene** (seria circular).
- **Grilla:** `delta` en {0.01 (= v1), 0.02, 0.03, 0.05, 0.075, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50}.
- **Criterio:** (1) argmin de la mediana entre pacientes del MAE de HU en `G`; (2) parsimonia: el menor
  `delta` a <= 1 HU de ese minimo; (3) salvaguarda: MAE fuera del metal real no peor que la v1.
- **Cota reportada:** `1 - u` del modelo donde la verdad satura (p50/p95/p99).
- **Ajuste declarado:** la grilla hasta 0.5 y la regla de parsimonia se anadieron tras una prueba de
  humo con 2 pasos de DDIM (cifras sin valor: no se leyeron), porque el argmin caia en el borde de la
  grilla original. Ninguna cifra valida se habia visto.
- **Limite:** reconstruccion puede premiar memoria (decision (6)); `n = 5`; criterio por checkpoint, y
  si los dos difieren decide la autora.

#### Adenda 5 a #152 (2026-10-07): RESULTADO de `a16` — `delta = 0.05` por el criterio, en los dos checkpoints

Fuente: `experiments/objetivo3/outputs/a16.log`, `a16/a16_delta_val.csv`. 60 generaciones (5 pacientes
de validacion x 6 cortes x 2 ckpt), CPU, rc=0. Memoria: pico python 860 MB, minimo libre 3.1 GB.

| mediana entre pacientes | `run01_140k` v1 -> v2(0.05) | `mejor_37k` v1 -> v2(0.05) |
|---|---|---|
| MAE de HU en `G` | 326.6 -> **295.5** | 376.9 -> **344.1** |
| MAE fuera del metal real | 247.2 -> **241.8** | 277.2 -> **261.6** |
| MAE en metal real | 1584.9 -> 1223.0 | 2692.9 -> 1781.0 |
| metal real recuperado (> 2500 HU) | 0.864 -> **0.956** | 0.534 -> **0.883** |

- **Criterio aplicado tal como se registro (adenda 4):** argmin 0.075 (`run01`) y 0.050 (`mejor`);
  parsimonia -> **0.050 en los dos**; salvaguarda cumplida (el MAE fuera del metal **mejora**, no
  empeora). A partir de 0.03-0.05 la curva es plana: ningun `delta` mayor gana mas de 1 HU.
- **Por paciente:** la v2 con 0.05 mejora el MAE en `G`, el MAE fuera del metal y el metal recuperado en
  **10 de 10** pares paciente x checkpoint (prueba de signos por checkpoint: 5 de 5, p = 0.031, una
  cola; `n = 5`).
- **Por que 0.05 tiene sentido fisico, no solo estadistico:** donde la verdad satura, la distancia al
  tope `1 - u` que deja el modelo se reparte asi (MW / SW): **[0, 0.01) 0.596 / 0.618** (la v1 ya lee
  bien), **[0.01, 0.05) 0.118 / 0.128** (la franja que la v1 lee como techo: el caso de `a15`,
  `u ~ 0.989`), **[0.05, 0.10) 0.019 / 0.015** (valle), y **>= 0.10: 0.267 / 0.239** (errores del modelo
  en el canal estrecho, que ninguna lectura corrige). **0.05 cae justo en el valle** entre "casi
  saturado" y "de verdad no saturado".
- **La brecha entre checkpoints en metal recuperado** baja de 33 a 7 puntos con la v2, en linea con lo
  medido sobre `a15` (adenda a #152).
- **Lo que NO dice:** nada sobre que checkpoint elegir (decision (6), bloqueada por #150), y nada sobre
  el streaking en `B_delta` (el MAE fuera del metal incluye la banda, pero no mide amplitud de rayas).
  El ~25 % de voxeles saturados con `1 - u >= 0.10` es error del modelo y queda como esta.

**Pendiente de la autora (regla 3):** registrar en `01-decisiones.md` la v2 con `delta = 0.05`; texto
propuesto en el chat. **No se aplico como omision en ningun script**: `a15 --delta 0.05` lo usa solo
si se pide.

**Actualizacion (2026-10-07):** la v2 con `delta = 0.05` quedo registrada en `01-decisiones.md` (entrada 2026-10-07), escrita por el asistente con autorizacion explicita de la autora. #152 sigue ABIERTA por el streaking en `B_delta`.

#### Adenda 6 a #152 (2026-10-07): `a15` con la v2 (`delta = 0.05`) sobre `0101` y `0102` — y la v1 RECORTABA las rayas claras en la banda

Fuente: `outputs/a15_v2.log`, `outputs/a15_v2/*_resumen.csv` y `*_perfil.csv`. CPU, laptop, semilla 0,
`--sin-nifti`, rc=0 en los dos. Memoria: pico python 3.2 GB, minimo libre 2.7 GB.

**Dentro de `M`** (`n_M` 4788 y 4657; techos SW/MW: **0 voxeles** en las 4 corridas):

| frac > 2500 HU | `0101` v1 CPU | `0101` v2 | `0102` v2 |
|---|---|---|---|
| `run01_140k` | 0.938 | **0.972** | **0.992** |
| `mejor_37k` | 0.676 | **0.932** | **0.928** |

Brecha entre checkpoints con la v2: 4.0 puntos (`0101`) y 6.4 (`0102`). (No hay v1 CPU de `0102`.)

**Hallazgo nuevo — la v1 tambien afectaba `B_delta`.** Mismo `0101`, mismas muestras (CPU
determinista), solo cambia la lectura. Perfil radial:
- **Medianas: identicas desde 2 mm** en los dos checkpoints. Cambian solo a 0-2 mm (`mejor_37k` 0-1 mm:
  873 -> 1572 HU).
- **p95: sube hasta 9 mm.** `mejor_37k`: 4-5 mm 555 -> 624; 5-6 mm **470 -> 547**; 7-8 mm **237 -> 339**;
  8-9 mm **235 -> 270**. `run01_140k`: 4-5 mm **471 -> 511**.
- **Varios p95 de la v1 coinciden con los techos** (471.2, 470.4 ~ MW 472; 237.4, 234.7 ~ SW 236): la v1
  **aplastaba la cola clara del streaking** contra los techos de ventana. Mecanismo coherente con #152;
  **no verificado voxel a voxel** (las marcas se guardan solo dentro de `M`).

**Por que importa mas que lo de `M`:** el endpoint primario (`streak amplitude`, decision (3), estilo
Peters) es un estadistico **de colas**: media del 5 % superior menos la del 5 % inferior. Con la v1 la
cola superior quedaba recortada, asi que **cualquier amplitud de rayas medida con la v1 esta
subestimada**. Antes de medir el endpoint, la version del decodificador tiene que estar fijada (ya lo
esta: v2, `01-decisiones.md` 2026-10-07) y declarada.

**Lo que NO se sostiene:** dos pacientes, una semilla; `0102` sin pareja v1 en CPU. Ninguna eleccion
de checkpoint (sigue bloqueada por #150). Las cifras GPU de #150/#151 son v1 y no se comparan con estas.

**Alcance hacia atras (adenda 6):** todo lo medido sobre salidas del modelo con `decodifica_bloque` antes del 2026-10-07 uso la v1: `a6`, `a8` (#141, #145), `a10` (costura), `a13`, `a15` (#149, #150, #151). Sus cifras de colas y de metal deben leerse como v1. **No afecta** a `a12` (perfil de implantes reales: HU del CT, sin decodificador) ni al Objetivo 1. `a9` decodifica codificacion exacta (identidad): tampoco cambia.

#### Adenda 2 a #150 (2026-10-07): dos problemas nuevos del cotejo, y propuesta revisada — SIN DECIDIR

- **La fraccion > 2500 HU no se puede comparar contra lo real.** En los implantes reales la mascara de
  metal SE DEFINE como `arr > METAL_HU` (`a1b_parches_componente.py:100`): lo real da 1.0 por
  construccion. El histograma dentro de `M` tiene que compararse sobre los voxeles > 2500 en ambos
  lados (p50/p75/p95), y la fraccion sintetica solo como control.
- **El tipo de implante de los 3 pacientes de referencia no esta verificado.** Si son placas o
  protesis y no tornillos, su perfil puede no ser comparable con un tornillo. Hay que mirarlo antes del
  cotejo.
- **La mediana sola es ciega al streaking** (adenda 6 a #152: lo que cambia en `B_delta` es el p95). El
  perfil debe incluir el p95. Y el HU crudo esta dominado por la anatomia: comparar **elevacion**
  respecto al anillo de 12-15 mm del mismo paciente.
- Texto de decision propuesto en el chat (2026-10-07). **Pendiente de la autora (regla 14).**

**Actualizacion a #150 (2026-10-07):** la definicion comun quedo registrada en `01-decisiones.md`
2026-10-07 (2), escrita por el asistente con autorizacion explicita de la autora. **Pendiente por
orden de la autora:** clasificar con `clasificador-metal` el tipo de implante de los 3 pacientes de
referencia, antes del cotejo. #150 sigue ABIERTA hasta que el cotejo corra.

## Ronda 2026-10-08 — decisiones delegadas al asistente

### 153 — `tesis/main.tex` queda desalineado con las decisiones delegadas del 2026-10-08: la hipotesis y el Objetivo 2 siguen hablando de densidad — APLICADA el 2026-10-08

- **Origen:** `01-decisiones.md`, entrada 2026-10-08 (decisiones delegadas), aplicada a `overleaf/` y a
  `docs/00-tesis.md` en la ronda `gaps-r03`. `tesis/main.tex` no se toco (regla 4: solo con orden explicita).
- **Que queda desalineado en `main.tex`:** (1) la Hipotesis (*"density-based placement sampler"*) y el
  Objetivo 2 (*"constrained by bone density read from the CT numbers"*), cuando el muestreador preinscrito no
  condiciona por densidad y la fraccion por zona de densidad salio de SAP (punto 14); (2) la fila *Surgical
  Admissibility* de la tabla de resultados, que lista *"density-zone fraction"* como componente; (3) la
  Pregunta de investigacion conserva *"bone density"* entre parentesis.
- **Tipo:** REDACCION / coherencia entre `main.tex` (fuente de contenido) y `overleaf/` (entrega). No cambia
  ninguna cifra ni ningun experimento.
- **Pendiente de la autora:** orden explicita para editar `main.tex`, o confirmar que `main.tex` queda como
  boceto historico y la fuente vigente es `overleaf/`.
- **APLICADA el 2026-10-08 por orden explicita de la autora** ("edita main.tex tambien para alinearlo"):
  Problem Statement (el muestreo queda acotado por la viabilidad del corredor), Research Question
  (*"osseous corridor and cortical containment"*), Hypothesis (*"corridor-constrained placement sampler"*),
  Objetivo 2 (restringido por la holgura cortical de 5 mm y la viabilidad del corredor), fila *Surgical
  Admissibility* (solo perforacion; viabilidad a 7.0 mm con 1 mm de holgura, descriptiva; sin fraccion de
  densidad) y *Explicitly out of scope* (condicionar por densidad, motivado por `arand2019pelvicring`, pasa a
  trabajo futuro). Compila: 8 paginas, 0 errores, 0 citas indefinidas. Copias literales de `00-tesis.md`
  alineadas.

### 154 — LOS 3 PACIENTES DE REFERENCIA DEL COTEJO NO SON TORNILLOS AISLADOS: `0011` fijador externo, `0056` placas con tornillos, `0039` dos tornillos (uno iliosacro, no transsacro completo) — APLICADA el 2026-10-08 (opcion 1 con solo `0039`, `01-decisiones.md` 2026-10-08 (2); toca #150)

- **Origen:** agente `clasificador-metal`, 2026-10-08, lote `experiments/exploration-3d/propuesta_lote-tipo-ref.csv`
  (propuesta sin validar; morfologia, no modelo ni material). Laminas a 2500 HU del 2026-09-07; `0056` tambien a
  1500 HU (`experiments/exploration-3d/outputs/hu1500/`).
- **Hallazgo propuesto:**
  - `metal_0039`: (a) dos tornillos intraoseos aislados, confianza alta. comp1 3463 vox / 2639 mm3, cortes 87-156,
    oblicuo pubis -> acetabulo; comp2 2031 vox / 1548 mm3, cortes 180-205, transverso en sacro, ~82 mm y ~5 mm de
    diametro equivalente (estimacion grosera). comp2 solo cruza ~14 mm la linea media: forma de tornillo
    iliosacro, no transiliaco-transsacro. HU max 6778, el mas bajo de los tres.
  - `metal_0056`: (b) tres placas con tornillos (sinfisis, cresta iliaca, borde pelvico; 13011/12816/10033 vox) +
    (e) hilera externa de focos pequenos. Ningun tornillo aislado ni a 2500 ni a 1500 HU.
  - `metal_0011`: (c) fijador externo (barras y bloques extracorporeos, 2 clavos por lado a las alas iliacas;
    comp1 28075 vox / 15530 mm3). Coincide con el veredicto de la autora en `a3_revision_componentes.csv`
    ("otro implante").
- **Por que importa:** la envolvente real del cotejo (min-max de 3 pacientes, perfil radial mediana/p95 e
  histograma en `M`) mezcla un fijador cuyos clavos cruzan aire y tejido blando, placas con mas metal por
  componente y solo un tornillo aislado. El perfil de artefacto de una placa o un fijador no es el de un tornillo
  transiliaco-transsacro: la envolvente puede quedar ensanchada (deja pasar checkpoints malos) o desplazada.
  Refuerza el supuesto no verificado ya declarado (sintetizador entrenado con todo material, sintetiza solo
  tornillos; implicancia de guia-3 r03).
- **Opciones (no decididas, regla 14):** (1) restringir la referencia a componentes tornillo: comp1/comp2 de
  `0039` y, si existen, tornillos aislados de pacientes de entrenamiento (`a3_revision_componentes.csv`, 5 de 40
  eran tornillos) — rompe la separacion validacion/entrenamiento si se usan los de entrenamiento; (2) mantener los
  3 pacientes y cotejar por componente, declarando el tipo; (3) mantener el cotejo como esta y declarar la
  heterogeneidad como amenaza a la validez (el cotejo ya "descarta, no prueba").
- **Afecta:** `overleaf/secciones/capitulo3.tex` (cotejo, l.~204; el `\GAPDEC` del tipo de implante),
  `experiments/objetivo3/a13_comparar_ckpt.py`, #150.
- **Pendiente de la autora:** validar la propuesta (abrir `explorar.py cortes` en `0039` primero, luego `0056`) y
  elegir opcion. El cotejo no corre hasta entonces.
- **Resolucion (2026-10-08):** la autora eligio la opcion 1 usando solo `0039`, previa revision de los 65 pacientes
  (`experiments/exploration-3d/tornillos_candidatos.md`). Aplicada en `00-tesis.md` y `capitulo3.tex` (cotejo).

### 155 — EL CENSO `e8` SUBCUENTA LOS TORNILLOS CANDIDATOS (26 de 65 pacientes a ojo frente a 17) y LA REFERENCIA DE REALISMO DEL OBJETIVO 3 MEZCLA TIPOS DE IMPLANTE; posible paciente repetido entre test y train (`0053`/`0054`) — ABIERTA

- **Origen:** revision visual de los 65 pacientes con material ortopedico, 4 agentes `clasificador-metal`,
  2026-10-08 (`experiments/exploration-3d/propuesta_lote-tornillos-{A,B,C,D}.csv`, resumen en
  `tornillos_candidatos.md`). Propuesta sin validar.
- **(1) Censo `e8` (#41, #13):** 26 pacientes con tornillo aislado candidato IS/TS a ojo frente a 17 del censo.
  No detecta 9 (vastago bajo 2500 HU o fragmentado) y subestima L en los fragmentados (`0040` 33 frente a
  ~145 mm). Toda cifra de `e8` (17 de 65, medianas de L y d de alargados) es un minimo o esta sesgada a
  tornillos densos y enteros. **Afecta:** el cuerpo de 4.91 mm (mediana de 79 alargados del censo morfologico,
  `capitulo3.tex` l.~127) si sale de este mismo filtro; revisar si el sesgo cambia la mediana.
- **(2) Realismo del Objetivo 3 (`capitulo3.tex` l.~248):** las muestras sinteticas se comparan con "los
  implantes reales de los 20 pacientes de prueba con implante", que incluyen placas, fijadores y protesis;
  solo 5 de ellos tienen tornillo aislado candidato (`0009`, `0024`, `0048`, `0049`, `0066`). Mismo problema
  que #154 para el cotejo. Opciones: restringir a componentes tornillo aislado de test, estratificar por tipo,
  o declarar la heterogeneidad.
- **(3) Particion:** `0053` (test) y `0054` (train) tienen una placa del anillo anterior casi identica y grupos de
  paciente distintos. Si son el mismo paciente, hay **fuga train/test** (`p1_particion.csv`). Otros posibles
  repetidos sin registrar, solo en train: `0025`/`0026`, `0027`/`0028`, `0037`/`0038`, `0019`/`0020`.
- **(4) Datos previos:** `0066` estaba como "ortopedico = no" en la revision 2D y las laminas muestran clavos y
  barra transversa.
- **Pendiente de la autora:** validar en cortes (`0053`/`0054` primero por la fuga), decidir (2) y si se rehace
  `e8` con umbral menor o union de fragmentos colineales.
- **Actualizacion (2026-10-08):** la autora reviso en cortes (`tornillos_revision_autora.csv`). (3) **Confirmado:**
  `0053` y `0054` son el mismo paciente -> se resuelve en #156. (4) `0066`: barra de ilion a ilion. `0040`: barra
  de ilion a ilion dentro del hueso. `0055`: 3 tornillos transversos sueltos. En los tres, dentro del hueso el fuste
  tiene HU bajo y se confunde con el hueso (confirma (1)). (2) queda como `\GAPDEC` en `capitulo3.tex` (realismo:
  19 pacientes de prueba con implante, 5 con tornillo aislado).

### 156 — `metal_0053` (test) y `metal_0054` (train) SON EL MISMO PACIENTE: fuga train/test; `0053` sale de las cohortes por la regla del 2026-09-10 — APLICADA en datos y `overleaf/` el 2026-10-08; PENDIENTE en `00-tesis.md` y `tesis/main.tex`

- **Origen:** revision en cortes de la autora, 2026-10-08 (misma placa y anatomia; `0053` tiene ademas un implante
  femoral y un FOV mas alto). Tenian grupos de paciente distintos (P152/P153).
- **Regla aplicada (sin decision nueva):** `01-decisiones.md` 2026-09-10, adquisiciones distintas del mismo
  paciente: primaria la de menor spacing en plano -> `0054` (0.785 frente a 0.820 mm), que sigue en train; `0053`
  secundaria, fuera de cohortes. Cambios: `p1_particion.csv` (fila de `0053` retirada, como `0065`: el
  control de `leer_particion` aborta si un paciente aparece en dos particiones), `grupos.csv`
  (reproducibilidad), `exclusiones.csv` (fila nueva). `revision.csv` (archivo de la autora) sigue con P152.
- **Objetivo 1:** el decodificador `afinado` se entreno con train (incluye `0054`) y se evaluo en `0053`: fuga. La
  compuerta preinscrita se ejecuto con 34 y no se reescribe. Sensibilidad sin `0053`
  (`experiments/objetivo1/p1_sin_0053.md`): mejor combinacion 61.72 -> 60.95 HU (IC95 [54.28, 68.19]); maxima
  diferencia 2.25 HU; **NO-GO igual**. La cota de MAISI (42.24 HU) no entrena nada: sin fuga, solo cambia n.
- **Objetivo 2:** el marco de Kaiser sobre metal pasa a 64 pacientes; `0053` no tenia marco computable (S1 no
  hallado, crestas fuera de FOV): 57 sigue, 8 -> 7, 7 -> 6; 48, 29 y 17 no cambian. La cohorte primaria (sin
  osteosintesis) no se toca.
- **Objetivo 3:** el sintetizador se entreno con `0054` (train): correcto. Prueba 34 -> **33** (con implante 20 ->
  **19**; sin metal 14). Nada de test se ha medido aun.
- **Aplicado en `overleaf/secciones/capitulo3.tex`** (ronda `tornillos-r01`).
- **Alineados el 2026-10-08** por orden de la autora: `00-tesis.md` y `tesis/main.tex` (sensibilidad del Obj 1,
  64 pacientes, 19 de prueba con implante). Queda: si `revision.csv` se corrige a P153.
