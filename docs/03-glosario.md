# 03 — Glosario

> Actualizado el 2026-09-08. Cada termino con cifra lleva su fuente. Si una cifra no
> tiene fuente verificada, se dice. Las siglas retiradas se conservan aqui a proposito,
> para que nadie las reintroduzca por inercia.

## Imagen y artefacto

- **HU (Hounsfield Unit):** escala de atenuacion normalizada de la CT, con agua en 0 HU
  y aire en -1000 HU. Es la unidad en la que se define todo lo demas de este glosario.
- **MAR (Metal Artifact Reduction):** familia de metodos que **remueven** artefacto
  metalico de una CT ya adquirida. Importa la direccion: esta tesis **sintetiza**, no
  remueve. Toda la literatura multi-ventana leida es de MAR (implicancia #2).
- **Beam hardening:** endurecimiento del haz. El espectro policromatico pierde
  preferentemente fotones de baja energia al cruzar metal, lo que sesga la atenuacion
  reconstruida y produce bandas oscuras entre objetos densos.
- **Photon starvation:** inanicion de fotones. Trayectorias que cruzan mucho metal
  llegan al detector con muy pocos fotones; el ruido domina y aparecen rayas.
- **Streaking:** rayas de alta amplitud que se propagan **fuera** de la mascara del
  implante. Es justo lo que los modelos de sintesis de lesiones no pueden generar,
  porque restringen la alteracion al interior de la mascara.
- **Ventana (HU window):** intervalo `[L, H]` de HU que se mapea al rango visible.
  Normalizacion usada por la literatura leida: `Ynorm = (Yclamp - L)/(H - L)`
  (`wang2025adaptiveweighting`, Eq. 2, p. 2410).
- **Multi-ventana:** uso de varias ventanas HU a la vez en un mismo modelo. Las tres
  ventanas concretas de la literatura leida son
  LW `[-1000, 2000]`, MW `[-320, 480]`, SW `[-160, 240]` HU
  (`wang2025adaptiveweighting`, Sec. V-A-1, p. 2412).
  **Aviso de atribucion (implicancia #24):** el marco multi-ventana **no** es de ese
  paper; el lo adopta de trabajo previo de MAR. Ademas ahi las ventanas se combinan en
  **cascada** de ancha a estrecha, no como codificacion multicanal de entrada. Citarlo
  sin esta salvedad atribuye un diseno que la fuente no tiene.
- **Zona peri-implante:** region de tejido adyacente al implante donde el artefacto
  degrada la senal. En la literatura leida solo aparece de forma cualitativa; ninguna
  fuente la cuantifica en milimetros.
- **B_delta (banda de generacion extendida):** banda espacial de ~12 mm anadida alrededor
  de la mascara del implante, dentro de la cual el modelo tiene permitido generar.
  Existe para que streaking y beam hardening puedan manifestarse **fuera** del metal.
  **Sin precedente publicado hallado:** ninguna de las fuentes leidas define una banda
  peri-implante con valor numerico (implicancia #24, hallazgo 4). El valor de 12 mm es
  eleccion de esta tesis, no heredado.

## Anatomia y colocacion

- **Brecha cortical (cortical breach):** perforacion de la cortical osea por el implante.
  Esta tesis usa la **escala ordinal de cuatro grados** con umbrales en milimetros:
  grado 0 (sin brecha), grado 1 (<2 mm), grado 2 (2-4 mm), grado 3 (>4 mm). Origen:
  `smith2006iliosacral`, adoptada por `zwingmann2009navigated`.
  **No confundir con el criterio binario** seguro/inseguro de `hinsche2002fluoroscopy`
  (*"unsafe when the screw path perforated one of the cortices"*, Measurements, p. 138):
  son dos definiciones **no intercambiables** y sus tasas no se mezclan (implicancia #12).
- **Corredor oseo (osseous corridor):** volumen de hueso por el que puede pasar un
  tornillo sin romper cortical.
- **Dmax:** diametro maximo de una trayectoria recta dentro del corredor antes de romper
  cortical. Procedimiento: contornos corticales mapeados, recta de tabla externa iliaca a
  la contralateral, diametro creciente *"until it contacted and breached the thickness of
  the cortex... in at least three locations"* (`mclaren2021corridor`).
- **Zona segura (safe zone):** corredor con `Dmax >= 10 mm`. **Umbral heredado y no
  establecido:** `mclaren2021corridor` lo adopta de trabajo previo y declara que el
  corredor minimo *"has not yet been established"*, con valores previos entre 8 y 12 mm
  (implicancias #7 y #25).
- **Tolerancia angular:** margen angular disponible para la insercion.
  Transiliosacra: `1.53 +/- 0.57` grados en S1 y `1.02 +/- 0.33` grados en S2
  (`mclaren2021corridor`, Results). **Mezcla anatomia con tecnica percutanea**: se deriva
  con una distancia piel-sacro estimada en 150 mm y restando un tornillo de 7 mm.
- **Transiliosacro vs iliosacro:** transiliosacro cruza **ambas** articulaciones
  sacroiliacas; iliosacro no. Las cifras de `mclaren2021corridor` son transiliosacras.
  **No son intercambiables.**

## Metricas

- **SAP (Surgical Admissibility of Placement):** **unica metrica introducida por esta
  tesis.** Evalua el muestreador, no el renderizador. Se compara con distancia de
  Wasserstein-1 contra las **dos distribuciones ordinales de cuatro grados** de
  `zwingmann2009navigated` (navegado: 69/15/8/8; convencional: 40/37/11.5/11.5),
  condicionadas por tecnica quirurgica **en S1**. El nivel S1/S2 condiciona la
  geometria del muestreador; S2 se reporta descriptivamente, sin referencia ordinal
  clinica para Wasserstein-1. `vandenbosch2002` aporta quejas neurologicas por
  paciente/configuracion y posicion binaria por tornillo; ninguna equivale a
  los cuatro grados de SAP. Ver cierre de #12 y #28 (2026-09-08).
- **BFC (Boundary Feature Coherence) e ISC (Inter-slice Consistency): RETIRADAS**
  el 2026-09-08. Se proponian como metricas propias, pero se iban a rellenar con medidas
  heredadas de `peters2025hybrid`, lo que vaciaba el objetivo de "formalizacion"
  (implicancias #14 y #16). La apariencia se evalua ahora con los nombres publicados del
  protocolo adoptado. **No reintroducir estas siglas.**
- **Bone integrity:** Dice sobre voxeles por encima de 150 HU excluyendo la geometria
  metalica de referencia (`peters2025hybrid`, Sec. 2.5).
- **Metal integrity:** Dice de la mascara metalica contra la geometria de referencia, con
  umbral **adaptativo por ROI**: el mayor HU dentro de un ROI que cubre el metal y el
  tejido adyacente, mas 250 HU (`peters2025hybrid`, Sec. 2.5).
  **No es un umbral fijo de 250 HU.** Citarlo como tal seria un error.
- **Streak amplitude:** amplitud de las rayas. En sintesis se compara de forma
  distribucional contra observaciones reales, porque no hay imagen limpia de referencia.
- **Escala 0-4 del benchmark de Peters:** **no se traslada.** Su ancla (NMAR = 2) no
  tiene analogo en sintesis, y el mapeo exacto de cada metrica a la escala no esta en el
  PDF (implicancia #14).

## Datos

- **Umbral de mascara metalica en CLINIC-metal:** 2500 HU. *"clinical metals for
  CLINIC-metal and SpineWeb are segmented with the thresholding of 2,500HU"*
  (`wang2025adaptiveweighting`, Sec. V-A-2, p. 2413). Es el unico umbral publicado sobre
  este mismo subconjunto y sirve de definicion operativa para separar metal de otros
  objetos densos (implicancia #22). **Nota:** un umbral en HU no encuentra material no
  metalico; si `objeto extrano` llega a incluirlo, hace falta otro instrumento
  (implicancia #19).
