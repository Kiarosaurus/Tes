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
