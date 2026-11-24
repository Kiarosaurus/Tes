# Informe E — Calidad perceptual y prueba de Turing visual (auditoría prospectiva)

Rol: Perceptual Quality & Visual Turing Test Specialist. Material: `thesis/secciones/` (capitulo3, capitulo4, conclusiones, trabajosFuturos, introduccion), `results/objetivo3/` (c2b, borde/estática, textura_metricas, pipeline_textura y su reporte, C4), `code/src/renderizador/` (texturas.py, difusion.py, entrenar.py), `results/objetivo1/p1_particion.csv` y `results/exploration-3d/grupos.csv`.

Material NO disponible en `review/` (lo que dependa de él es NO VERIFICABLE): `docs/01-decisiones.md` (las reglas "2026-11-21 (18)" del pipeline de textura y la regla de c2b), la clave de c2b (`c2b_ciego.py` y la correspondencia id→brazo), el `REPORTE.md` del pipeline y el resultado en prueba de 100:0.3 (que el propio texto marca como pendiente, `capitulo3.tex:333`).

---

## 1. Diagnóstico en una página

1. **El objetivo perceptual no figura entre los objetivos de la tesis.** La introducción y las conclusiones dicen que el realismo visual "no se reclama" (`introduccion.tex:100`, `conclusiones.tex:30,38`). Los experimentos de textura, perceptual proxy y adversarial, el barrido de muestreo y el criterio visual (c) son exploratorios y posteriores a ver la prueba (`capitulo3.tex:602`). No pueden cambiar el reclamo del Objetivo 3, y el documento todavía tiene abierta la decisión que los acota (`capitulo3.tex:604`, `\GAPDEC`).
2. **Los dos pacientes de validación 0101/0102 ya se usaron demasiadas veces.** Con ellos se eligió el punto de control y el material y se fijó Δ. También se usaron en la regla de v2, el barrido η, el brazo B, c2b, borde/estática y ahora en los criterios del pipeline de textura (`textura_metricas.py:21`). Nada de lo que se elija sobre ellos generaliza. Tampoco hay un conjunto reservado para una evaluación visual independiente.
3. **El criterio visual (c) no es una prueba de Turing.** Es una puntuación de credibilidad de una sola lectora, que no está ciega y no tiene anclas de escala. Sus dos "controles" (lo real y Peters) se reconocen por cosas ajenas al artefacto: otra anatomía, y una reconstrucción completa con otro ruido.
4. **Dos de los criterios automáticos del pipeline de textura miden algo distinto de lo que se busca.** La "razón de textura" toma como meta la textura de la TC *sin metal*. La "estática" se calcula con la fracción de M bajo 2500 HU, que es otro defecto ("gris").
5. **Todavía se puede corregir mucho sin GPU:** fijar la lectura antes de abrir lo pendiente (100:0.3 y REPORTE), actualizar el inventario de lo visto y reservar ya un conjunto independiente.

---

## 2. Hallazgos

### E-01 — El objetivo perceptual no tiene sitio en la formulación y se arriesga scope creep
- **Ubicación:** `introduccion.tex:21`, `introduccion.tex:100`; `capitulo3.tex:604`, `capitulo3.tex:628`; `pipeline_textura.sbatch:2`.
- **Evidencia:** "la limitación principal del Objetivo 3 es el realismo visual del artefacto sintético, que este trabajo no reclama" (`introduccion.tex:100`). `\GAPDEC{confirmar que el brazo B y el criterio visual (c) se acotan así, como excepciones exploratorias declaradas, frente a la decisión del 16 de octubre [...] de no reentrenar ni rediseñar}` (`capitulo3.tex:604`). El pipeline se declara "EXPLORATORIO, POST-HOC" (`pipeline_textura.sbatch:2`) y entrena tres brazos nuevos: T, P y A.
- **Descripción:** La pregunta de investigación es de coherencia física y quirúrgica. Los brazos T/P/A y una futura prueba de Turing persiguen la credibilidad visual, que no tiene variable dependiente ni regla de decisión en el diseño (`capitulo3.tex:548-564`). Cada brazo nuevo multiplica las comparaciones sobre los mismos pacientes y alarga un documento que ya se quiere recortar.
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** Sin una frontera escrita, un resultado visual favorable podría leerse como respuesta al Objetivo 3, o como contradicción de la decisión del 16 de octubre.
- **Acción:** Cerrar el `\GAPDEC` de `capitulo3.tex:604` con una sola frase de estatus para todo el bloque perceptual: exploratorio, post hoc, sin papel en el desenlace del Objetivo 3 y sin reclamo de realismo. Decidir por escrito si la prueba de Turing es un entregable de la tesis o trabajo futuro (ver §5).
- **Dependencias:** ninguna (es una decisión de la autora).

### E-02 — Selección sobre validación reutilizada; no hay conjunto intacto para la evaluación visual
- **Ubicación:** `capitulo3.tex:596`, `capitulo3.tex:534`, `capitulo3.tex:309`, `capitulo3.tex:321`; `textura_metricas.py:21`; `borde_estatica_resultado.md:3`.
- **Evidencia:** "El punto de control, el material del protocolo físico y el margen Δ [...] se eligieron sobre los mismos dos receptores de validación" (`capitulo3.tex:596`). Por defecto, `CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']` (`textura_metricas.py:21`). c2b usa "los receptores de validación 0101 y 0102" (`capitulo3.tex:534`).
- **Descripción:** Los dos mismos receptores se han usado para elegir modelos, variantes de muestreo, brazos de ajuste fino, el juicio visual (c) y ahora los criterios (i)-(iv) del pipeline. Es selección iterativa sobre n = 2: cualquier ventaja que se observe ahí está sesgada a favor. Los 13 pacientes de prueba sin metal tampoco sirven para la evaluación visual. La autora vio sus salidas ("salidas de prueba en HTML (`a25`) e inspección visual", `visto.md:9`), y la métrica angular sobre ellos ya cambió el diseño del ajuste fino (`capitulo3.tex:602`).
- **Severidad:** alta. **Confianza:** alta.
- **Impacto:** Cualquier prueba de Turing hecha sobre 0101/0102 o sobre los 13 de prueba confundiría calidad con sobreajuste de selección.
- **Acción:** Reservar *ahora*, antes de mirar nada más, un conjunto de receptores que no haya intervenido en entrenar, seleccionar ni inspeccionar el sintetizador. Hay un candidato verificable. Según `p1_particion.csv` cruzado con `grupos.csv` (recuento propio), la partición `train` contiene 50 volúmenes del grupo 3 y 28 del grupo 2. El sintetizador solo se entrena con volúmenes con material ortopédico (`capitulo3.tex:52,226`), de modo que esos volúmenes nunca entraron en su entrenamiento ni en su selección. Falta verificar, sin mirar salidas sintéticas: un volumen por paciente, el eje del corredor medido y el control de pose (`capitulo3.tex:234`). Ese recuento por paciente es NO VERIFICABLE con el material.
- **Dependencias:** E-08 y protocolo de §5.

### E-03 — El criterio (i) del pipeline premia parecerse a la TC sin metal
- **Ubicación:** `textura_metricas.py:4-5`, `textura_metricas.py:57-66`; `pipeline_reporte.py:97-98`; `capitulo3.tex:276`.
- **Evidencia:** "`razon_textura` [...] 1 = textura igual a la de afuera. Referencia: el mismo cociente en la imagen original" (`textura_metricas.py:4-5`). El criterio es `i1 = abs(rt - ro) < abs(rc - ro)`, donde `ro` es la razón en la original (`pipeline_reporte.py:91,98`). La región "dentro" excluye M dilatada 6 px (`textura_metricas.py:58`), es decir, cubre más o menos de 5 a 12 mm. En esa zona el exceso real mediano todavía es de "765 y 473 HU" en 4–6 y 6–8 mm (`capitulo3.tex:276`).
- **Descripción:** La meta del criterio es la textura de alta frecuencia de la anatomía *sin metal*. Un artefacto real añade estructura en esa franja. El criterio puede, por tanto, preferir el brazo que *menos* artefacto texturizado genera. Sirve para detectar la "textura sobrepuesta" que marcó la autora, pero también castiga la textura física del artefacto. No hay referencia real (`metal_0039`) para este cociente.
- **Severidad:** alta. **Confianza:** alta, respecto del código; la regla escrita de (18) es NO VERIFICABLE.
- **Impacto:** Si se lee como "más realista", se elegiría o defendería un brazo por suavizar el artefacto.
- **Acción:** Antes de abrir el REPORTE, dejar escrito que (i) solo describe "textura parecida a la de la anatomía sin metal" y no realismo. Calcular el mismo cociente en los cortes reales de `metal_0039` (solo CPU) y reportarlo al lado, sin cambiar la regla.
- **Dependencias:** E-04.

### E-04 — El criterio (ii), llamado "estática", mide otro defecto y su dirección no está justificada
- **Ubicación:** `pipeline_reporte.py:99-100`; `borde_estatica_resultado.md:5-13`; `capitulo3.tex:70`, `capitulo3.tex:544`.
- **Evidencia:** El reporte llama "(ii) estatica no mayor" a `frac_M_bajo_2500` (`pipeline_reporte.py:100`). En `borde_estatica_resultado.md:5`, la "estática" es "M con |HU − mediana 3×3| > 1500 HU" y la fracción bajo 2500 HU es el "gris". Esa medida de estática no sigue a la marca visual: el control marcó estática en 5 de 6 paneles (`capitulo3.tex:542`) y su valor es 0.3 % (`borde_estatica_resultado.md:11`). Peters Ti tiene un 14.0 % de M bajo 2500 HU, y en los tornillos reales "dentro del hueso, el fuste [...] tiene HU bajos" (`capitulo3.tex:70`).
- **Descripción:** La relación entre estática y "gris" se observó después, en dos pacientes y sin ordenar bien los brazos (`capitulo3.tex:544`: "sin coincidir en el orden fino"). Además, minimizar la fracción gris no tiene un objetivo físico: la referencia física no está en cero.
- **Severidad:** media. **Confianza:** alta.
- **Acción:** Renombrar (ii) en el reporte y en el texto ("fracción de M bajo 2500 HU") y leerlo frente al valor de Peters Ti, no como "menor es mejor".
- **Dependencias:** ninguna.

### E-05 — El criterio visual (c) no permite inferir realismo ni discriminabilidad
- **Ubicación:** `capitulo3.tex:534-542`; `results/objetivo3/c2b_respuestas_2026-11-21.csv`.
- **Evidencia:**
  - "lo puntuó una sola lectora, la autora"; "El ciego es además nominal: la lectora conoce los modelos y sus defectos y vio el caso 0101 con 100:0.3" (`capitulo3.tex:536`).
  - La escala de 1 a 5 no tiene anclas (`\GAPDEC`, `capitulo3.tex:534`).
  - Lo real son "2 tornillos en 3 cortes" de otro paciente y otro escáner (`capitulo3.tex:534,542`).
  - El CSV tiene 48 respuestas. Recuento propio: 16 de puntaje 1, 5 de 2, 6 de 3, 7 de 4 y 14 de 5. La suma, 142, coincide con la suma de las medias publicadas por 6 (5.00 + 4.83 + 3.33 + 3.00 + 2.33 + 2.17 + 1.67 + 1.33 = 23.66; por 6 da unos 142).
  - La clave id→brazo no está en `review/`, de modo que las medias por brazo son NO VERIFICABLES.
- **Descripción:**
  - Las respuestas son bimodales (30 de 48 en los extremos), lo que es compatible con clasificar por señales categóricas (anatomía de otro paciente, reconstrucción completa de Peters, gris y estática en M) más que por la credibilidad del artefacto. Por eso el 5.00 de Peters y el 4.83 de lo real no son controles válidos.
  - Una sola semilla por brazo (rango entre semillas de hasta 393 HU, `capitulo3.tex:256`); seis paneles; siete comparaciones sin corrección; sin repetibilidad, sin tiempo y con una sola ventana.
- **Severidad:** alta, si se usa como evidencia; baja, si se mantiene como descripción. **Confianza:** alta.
- **Qué se puede concluir:** que en una sesión, para esta lectora, los paneles de 50:0.3 recibieron puntajes más altos que los del modelo evaluado en los 6 pares (cifra del texto, NO VERIFICABLE sin la clave), y que la estática y la textura sobrepuesta no aparecieron en lo real ni en Peters.
- **Qué NO se puede concluir:** que algún brazo sea realista o indistinguible de lo real; que la mejora generalice a otros pacientes o semillas; que lo real y Peters sean "comparables" como referencia; que el orden visual contradiga o valide las métricas.
- **Acción:**
  - Reescribir el pasaje como "puntuación exploratoria de credibilidad de una lectora" y evitar los términos "prueba", "Turing" y "cumple" sin calificativo.
  - Reportar la distribución de puntajes.
  - Declarar que los dos controles se reconocen por la anatomía y por la reconstrucción.
  - Quitar la frase "son comparables, 5.00 y 4.83" (`capitulo3.tex:542`) o calificarla.
  - No repetir c2b con la misma lectora sobre los mismos paneles para elegir entre T/P/A (ver E-11).
- **Dependencias:** E-02.

### E-06 — El inventario de lo visto no cubre las decisiones de noviembre
- **Ubicación:** `capitulo3.tex:590`; `results/objetivo3/visto.md:7-25`; `capitulo3.tex:602`.
- **Evidencia:** El texto dice "Lo visto antes de cada decisión consta en un inventario fechado, que se lleva desde las primeras" (`capitulo3.tex:590`). La última fila de `visto.md` es del 2026-10-15 (`visto.md:25`). Pero el 20 de noviembre se miró η²_exc en los 13 pacientes de prueba (`c4_resultado.md`, "Parte 1 — 13 pacientes de prueba"), y eso "cambió además el diseño del ajuste fino" (`capitulo3.tex:602`).
- **Severidad:** alta, para la auditabilidad de lo post hoc. **Confianza:** alta.
- **Impacto:** Sin inventario no puede demostrarse qué reglas de noviembre (barrido, B, c2b, pipeline de textura, prueba de 100:0.3) son anteriores a cada resultado.
- **Acción:** Añadir a `visto.md` las filas del 20 al 22 de noviembre, con fecha, partición y modelo, *antes* de leer el REPORTE y la prueba de 100:0.3.
- **Dependencias:** ninguna. Coste: minutos.

### E-07 — La prueba de 100:0.3 solo tiene margen propio, y η > 0 lo ensancha por construcción
- **Ubicación:** `capitulo3.tex:333`, `capitulo3.tex:506`; `a20_eta_test.sbatch:48-58`; `evalua_todo_local.sh:28`.
- **Evidencia:** "el margen Δ propio de la variante, medido en validación con dos pacientes" (`capitulo3.tex:333`). El script solo calcula `a20_delta_<etiqueta>.json` (`a20_eta_test.sbatch:58`), y `a24` se llama con ese `--delta-json` (`evalua_todo_local.sh:28`). El propio texto dice: "un sintetizador más variable obtiene un margen más ancho y, con él, una prueba de equivalencia más fácil de aprobar" (`capitulo3.tex:506`). Para v2 se fijó un margen común "para que sus desenlaces sean comparables" (`capitulo3.tex:305`).
- **Descripción:** η_DDIM > 0 inyecta ruido estocástico en cada paso, lo que previsiblemente aumenta la variabilidad entre semillas (s_sem) y con ella Δ. Esto es una inferencia, no un dato. También puede subir la amplitud por ruido y no por rayas; el piso de ruido del modelo evaluado ya es 0.69 veces su amplitud (`capitulo4.tex:140`). Es la vía perceptual con más probabilidad de dar un "equivalente" espurio.
- **Severidad:** alta. **Confianza:** media (la dirección del efecto sobre Δ es una inferencia).
- **Acción:** Antes de leer el resultado, escribir que 100:0.3 se juzga también con el margen común de 196.3 HU y con su margen mínimo de equivalencia, como v2, y que la equivalencia con margen propio no se reporta sola.
- **Dependencias:** E-06.

### E-08 — Ninguna métrica disponible mide la calidad perceptual buscada
- **Ubicación:** `capitulo3.tex:614-616`; `c4_resultado.md:31-32`; `c4_eta_resultado.md:26,29`; `capitulo4.tex:168`.
- **Evidencia:**
  - La *streak amplitude* "crece con cualquier desviación extrema [...] tenga o no estructura de raya" (`capitulo3.tex:614`).
  - En modo crudo, η²_exc no separa a Peters de la anatomía en prueba: "peters_Ti_test − control_anatomia_test | crudo | 0.007 | [-0.075, 0.081]" (`c4_resultado.md:32`). En validación, el modelo evaluado en crudo da 0.320 y el control sin metal 0.319 (`c4_eta_resultado.md:26,29`).
  - En modo residuo entra el piso de ruido de 893 HU (`capitulo3.tex:616`).
- **Descripción:** Esto es lo que mide cada métrica disponible:

  | Métrica | Qué representa | Qué no representa |
  |---|---|---|
  | *streak amplitude* | nivel de las colas | rayas ni textura |
  | perfil radial, E y cáscaras p95 | caída con la distancia | dirección ni textura |
  | η²_exc residuo | anisotropía relativa, solo para ordenar brazos | realismo (depende de K y del ruido) |
  | razón de textura (E-03) | similitud con la anatomía sin metal | realismo del artefacto |
  | fracción gris y salto en borde de G | defectos locales concretos | calidad global |

  Ninguna está validada contra juicios humanos, y casi todas descansan en dos pacientes y una referencia real de dos tornillos.
- **Severidad:** media. **Confianza:** alta.
- **Acción:** No presentar ninguna como sustituto de la calidad perceptual, ni usarlas para predecir una prueba de Turing. No adoptar métricas de imágenes naturales (FID, LPIPS con redes de ImageNet): no tienen validación en TC ni tamaño de muestra suficiente aquí.
- **Dependencias:** E-03, E-04.

### E-09 — Brazo adversarial sin regla de peso y con otro t_max
- **Ubicación:** `pipeline_textura.sbatch:113,148`; `pipeline_lambda.py:3`; `entrenar.py:176`; `texturas.py:6,61-97`; `capitulo3.tex:319`.
- **Evidencia:**
  - T y P calibran λ con "lambda = 0.1 x L_v / L_termino" (`pipeline_lambda.py:3`). A usa un `--aux-adv 0.01` fijo (`pipeline_textura.sbatch:113,148`).
  - `--aux-tmax` vale 500 por defecto (`entrenar.py:176`) y el pipeline no lo pasa, frente a t_max 1000 y 300 en B (`capitulo3.tex:319`).
  - El humo de A solo comprueba que `L_D` sea finito y esté en [0.1, 3] (`pipeline_textura.sbatch:133`).
  - El proxy perceptual "NO es la pérdida perceptual de la literatura" (`texturas.py:6`).
- **Descripción:** Un discriminador PatchGAN entrenado desde cero en 3000 pasos puede introducir textura que convence al ojo sin respaldo físico. Es justo el riesgo de "superar el Turing sin coherencia física". Con dos pacientes no se puede distinguir una mejora de una alucinación.
- **Severidad:** media. **Confianza:** alta (código).
- **Acción:**
  - Si A llega a evaluarse, exigir como condición necesaria los criterios físicos (iii) y (iv) del reporte (cáscaras críticas y desviación en 0–2 mm, `pipeline_reporte.py:71`), además de los perceptuales.
  - Declarar el t_max de 500 y el peso sin regla.
  - No llevar A a ninguna prueba visual sin una decisión escrita previa.
- **Dependencias:** E-01.

### E-10 — Comparador de respaldo con hardware distinto
- **Ubicación:** `pipeline_reporte.py:90`; `capitulo3.tex:321,325`.
- **Evidencia:** `c = leer_json(... 'aux_C.json') or leer_json(... 'b_min_l0.json')` (`pipeline_reporte.py:90`). "No hay contraste válido entre B y el modelo evaluado [...] no se separa el efecto de la tarjeta del de seguir entrenando" (`capitulo3.tex:325`).
- **Descripción:** Si falla `aux_C`, los criterios (i) y (ii) se calculan contra un control de otra corrida y quizá de otra tarjeta, lo que repite el problema que el texto ya reconoce para B.
- **Severidad:** media. **Confianza:** alta.
- **Acción:** Escribir que, sin `aux_C`, los criterios de T/P/A no se interpretan.
- **Dependencias:** ninguna.

### E-11 — Una nueva sesión ciega con los mismos paneles y la misma lectora no sería independiente
- **Ubicación:** `evalua_todo_local.sh:24-25`; `capitulo3.tex:534`.
- **Evidencia:** `c2b_ciego.py --sufijo _aux ... "Sesion a ciegas nueva"` (`evalua_todo_local.sh:24-25`), sobre los brazos del pipeline. Los paneles de c2b son 0101/0102 en los cortes 1/6, 3/6 y 5/6 con la semilla 0 (`capitulo3.tex:534`).
- **Descripción:** Si la sesión nueva repite los receptores y los cortes, la lectora reconoce la anatomía y puede recordar los defectos que vio antes. Usarla para elegir entre T, P y A sería otra selección visual sobre n = 2. Que repita receptores y cortes es NO VERIFICABLE sin `c2b_ciego.py`.
- **Severidad:** media. **Confianza:** media.
- **Acción:** Si se hace, que sea solo descriptiva, que no elija ningún brazo y que se declare la memoria de la lectora.
- **Dependencias:** E-02, E-05.

### E-12 — Hay señales visuales ajenas al artefacto que contaminan cualquier juicio de realismo
- **Ubicación:** `capitulo3.tex:143`, `capitulo3.tex:151`, `capitulo3.tex:70`, `capitulo3.tex:544`; `capitulo4.tex:174`.
- **Evidencia:** La máscara sintetizada es un "Cilindro de 4.91 mm con una cabeza" liso, "sin arandela y macizo" (`capitulo3.tex:143,151`). Los tornillos reales están "fragmentados" a 2500 HU (`capitulo3.tex:70`). El "gris" de M sintético va del 15.6 al 40.2 % (`capitulo3.tex:544`). Según el conteo de la autora, ningún paciente de CLINIC-metal lleva un tornillo transilíaco-transsacro (`capitulo3.tex:632`).
- **Descripción:** Un lector puede distinguir sintético de real por la geometría del tornillo, la trayectoria (transsacra frente a iliosacra u otras), la anatomía o el gris interior, sin mirar el artefacto. Una prueba de Turing mal emparejada mediría esas señales.
- **Severidad:** media. **Confianza:** alta.
- **Acción:** Fijar en el protocolo qué se pregunta: el realismo del artefacto local o del implante con su artefacto. Emparejar recorte, ventana, espaciado y selección de cortes, y declarar las señales que no se pueden emparejar.
- **Dependencias:** §5.

### E-13 — "No hay un lector clínico disponible", pero el proyecto ya contó con lectores externos
- **Ubicación y evidencia:** "no hay un lector clínico disponible para juzgar la apariencia" (`capitulo3.tex:436`), frente a "un médico recién egresado y sin especialidad" (`:66`) y "un revisor clínico, cirujano otorrinolaringólogo" (`:123`) en el Objetivo 2.
- **Severidad:** baja. **Confianza:** alta.
- **Acción:** Valorar si 2–3 lectores externos, aunque no sean radiólogos, hacen viable el piloto de §5.

---

## 3. Alineación de los métodos post hoc con el objetivo perceptual

| Método | ¿Mejora visual? | ¿Coherencia física? | Riesgo principal |
|---|---|---|---|
| Barrido η (50:0.3, 100:0.3) | Parcial: sube el p95 en 4–12 mm (`eta_veredicto_resultado.md:23-29`) | Incierta: ruido o rayas (E-07) | Margen propio inflado; n = 2 |
| B (L_ang) | Sí, anisotropía | Sí | No cumple (i); B1000 puntuó 1.67 en c2b |
| T (textura) | Sí: referencia = `x0` real de entrenamiento | Neutral | Criterio de lectura (i) mal orientado (E-03) |
| P (pirámide laplaciana) | Débil: L1 multiescala, no perceptual | Neutral | Nombre engañoso; puede suavizar |
| A (PatchGAN) | Sí, por diseño | El de más riesgo | Peso sin regla (E-09) |

T y A comparan contra el `x0` real (`difusion.py:152-164`), que es la referencia correcta. El fallo está en la *lectura* (criterios i y ii), no en la pérdida.

---

## 4. Qué permite y qué no permite concluir el material actual sobre la calidad visual

**Permite:** que la autora juzgó insuficiente el resultado visual (`capitulo3.tex:628`); que η > 0 sube el p95 en cáscaras críticas en dos receptores (`capitulo3.tex:315`); y la lectura descriptiva de c2b de E-05.

**NO permite:** realismo, indistinguibilidad, que un brazo sea perceptualmente mejor en general, ni que la calidad visual implique utilidad diagnóstica, coherencia física o valor como aumento de datos (`conclusiones.tex:38`).

---

## 5. Prueba de Turing visual: protocolo mínimo viable

**Estatus recomendado:** piloto descriptivo y preinscrito. Solo es RECOMENDABLE si hay al menos 2 lectores externos y unos días; si no, es TRABAJO FUTURO. Su resultado no entra en el desenlace del Objetivo 3.

**5.1 Pregunta (fijarla antes).** Con unas condiciones de visualización fijas, ¿distinguen lectores con formación en imagen médica parches axiales locales de TC con un tornillo sintético y su artefacto de parches con un tornillo real?

**5.2 Modelo congelado.** Uno, a lo sumo dos brazos, elegidos *antes* de generar el conjunto de la prueba: el modelo evaluado (50:0) y, si se quiere, una variante declarada. No se elige el brazo según los resultados de la prueba.

**5.3 Independencia de datos.**
- Receptores sintéticos: el conjunto intacto de E-02 (grupo 3, y grupo 2 si hace falta, de la partición `train`, que no entró en el sintetizador), sorteado con una semilla guardada *antes* de generar.
- Excluidos: 0101/0102 y los 13 de prueba.
- Clase real: tornillos intraóseos aislados de pacientes de prueba con material ortopédico, aplicando la regla de inclusión ya escrita (`capitulo3.tex:532`). Si no alcanzan, se pueden añadir pacientes de entrenamiento, declarando el sesgo: el modelo vio su apariencia, lo que acerca lo sintético a ellos y facilita "pasar".
- El número disponible de tornillos reales aislados es NO VERIFICABLE (la lista "no se formó", `capitulo3.tex:532`). Es la restricción que manda.

**5.4 Estímulos y visualización.**
- Selección de cortes por una regla idéntica en las dos clases (por ejemplo, 1/6, 3/6 y 5/6 del tramo con M).
- Recorte fijo alrededor del implante, por ejemplo de 60 × 60 mm (valor que se fija de antemano), remuestreado a un espaciado común.
- Dos ventanas fijas mostradas juntas: [−500, 1300] HU, la de c2b, y una ventana de tejido blando.
- Sin zoom ni desplazamiento libre en la condición principal. ITK-SNAP, con navegación 3D, solo como condición secundaria declarada.
- Tiempo libre, pero registrado.
- Si el sintetizador elegido tiene salto en el borde de G (`capitulo3.tex:544`), hay que declararlo como señal posible.

**5.5 Tarea.**
- Cada imagen se presenta sola y se juzga como real o sintética, más una confianza de 1 a 5 (sirve para la AUC).
- Prevalencia del 50 %, comunicada a los lectores. Orden aleatorio por lector, con semilla guardada.
- Clave cerrada hasta terminar.
- 5 a 10 imágenes de práctica sacadas de otro conjunto y sin retroalimentación.

**5.6 Lectores.**
- Al menos 2, mejor 3, externos y sin acceso a las salidas previas.
- La autora queda excluida como lectora.
- Se registra la formación de cada lector (radiólogo, residente, médico general). Con no radiólogos, el resultado solo vale para ese nivel de pericia.

**5.7 Controles.**
- *Positivo:* parches de copia y pegado (metal sin artefacto) o del control `b_min_l0` (estática en 5 de 6). Si su detección queda por debajo de un umbral fijado antes (por ejemplo, el 80 %), la prueba es poco sensible y el 50 % del brazo principal no se interpreta.
- *Real contra real:* un subconjunto de imágenes reales de otro paciente o escáner da la tasa basal de "sintético" en imágenes reales (especificidad).
- *Protocolo físico:* opcional. Su reconstrucción completa delata el brazo; si entra, se recorta igual y se analiza aparte.

**5.8 Tamaño de muestra.** Los cálculos siguientes son propios y suponen juicios independientes, binomiales con p = 0.5.
- Para concluir que la exactitud está dentro de ±10 puntos de 50 % por TOST (α = 0.05 por lado, potencia del 80 %) hacen falta n ≈ (1.645 + 1.282)² · 0.25 / 0.10² ≈ 214 juicios. Con ±15 puntos, unos 96.
- Los juicios se agrupan por caso y por lector, así que n se multiplica por el efecto de diseño 1 + (m − 1)·ICC. Por ejemplo, con m = 6 juicios por caso y un ICC supuesto de 0.2, el factor es 2. El ICC real es NO VERIFICABLE.
- Con pocos pacientes reales (posiblemente menos de 10), la incertidumbre la dominan los casos, y el piloto **no podrá demostrar indistinguibilidad**. Solo podrá describir la exactitud con su IC.

**5.9 Análisis y criterio de éxito (fijados antes).**
- Exactitud por lector y global, y AUC a partir de la confianza.
- IC por bootstrap por conglomerados (casos y lectores), o GLMM logístico con interceptos aleatorios de lector y de caso, si converge.
- Criterio fijado de antemano, por ejemplo: "IC 95 % de la exactitud contenido en [35 %, 65 %] *y* control positivo detectado al 80 % o más".
- Se reportan también las exactitudes por encima del 50 % (detectable) sin reetiquetarlas.

**5.10 Riesgos que se cierran.** Prohibido ajustar el modelo, el muestreo, la ventana o el recorte después de ver respuestas. Prohibido reutilizar los parches del piloto para elegir modelos. Prohibido añadir lectores o casos hasta "pasar".

**Afirmaciones que permitiría:** "Con estas condiciones (parches 2D locales, ventanas X, lectores de formación Y), la exactitud de los lectores para separar lo sintético de lo real fue Z % [IC]". Y, si se cumple el criterio, "no se distinguieron de forma fiable en esta tarea".

**Afirmaciones que NO permitiría:** utilidad diagnóstica; coherencia física del artefacto (eso lo responden la *streak amplitude*, el perfil y Peters); validez en volumen 3D o con navegación libre; generalización a otros implantes, escáneres o lectores expertos; idoneidad como aumento de datos para segmentación.

---

## 6. Recomendaciones clasificadas

### INDISPENSABLE antes del cierre experimental (sin GPU o casi)

**R1 — Fijar el estatus del bloque perceptual y cerrar el `\GAPDEC` de `capitulo3.tex:604`** (E-01)
- Pregunta: qué puede y qué no puede decir el bloque perceptual.
- Evidencia nueva: ninguna; es una decisión.
- Riesgo que resuelve: contradicción con la decisión del 16 de octubre y scope creep.
- Coste: muy bajo.
- Si no se hace: un tribunal puede leer los brazos T/P/A/B y c2b como un rediseño encubierto.

**R2 — Actualizar `visto.md` con lo visto entre el 20 y el 22 de noviembre** (E-06)
- Resuelve la auditabilidad de lo previo y lo posterior.
- Coste: minutos.
- Si no se hace: la afirmación de `capitulo3.tex:590` queda sin respaldo.

**R3 — Preescribir la lectura de 100:0.3 en prueba con el margen común de 196.3 HU y el margen mínimo** (E-07)
- Pregunta: ¿la variante se acerca a Peters, o solo se ensancha su margen?
- Coste: nulo, porque `a24` ya calcula el IC.
- Si no se hace: una "equivalencia" con margen propio sería indistinguible de un artefacto del margen.

**R4 — Reescribir la lectura de los criterios (i) y (ii) del pipeline antes de abrir el REPORTE** (E-03, E-04, E-10)
- Resuelve la invalidez de constructo y el sesgo hacia suavizar el artefacto.
- Coste: muy bajo.
- Si no se hace: se elegiría un brazo por parecerse a la TC sin metal.

**R5 — Reservar ahora el conjunto intacto para la evaluación visual y dejar de seleccionar visualmente sobre 0101/0102 y sobre los 13 de prueba** (E-02, E-11)
- Resuelve el sobreajuste de selección y garantiza la independencia de cualquier prueba de Turing.
- Coste: bajo (verificación de identidad y de pose, sin generar nada).
- Si no se hace: la prueba de Turing futura estaría contaminada de origen.

**R6 — Corregir la redacción de c2b** (E-05)
- No llamarlo prueba ni "cumple" sin calificativo.
- Reportar la distribución de puntajes 1–5.
- Declarar que los controles se reconocen por la anatomía y la reconstrucción.
- Calificar "comparables".
- Coste: texto. Si no se hace: sobrelectura de n = 1 lectora.

### RECOMENDABLE si hay capacidad

**R7 — Piloto de prueba de Turing de §5** (2–3 lectores externos, conjunto intacto, 1–2 brazos)
- Pregunta: ¿son discriminables los parches locales?
- Evidencia nueva: la primera medida de discriminabilidad independiente de la autora.
- Riesgo que resuelve: el juicio no ciego de una sola lectora.
- Coste: GPU moderada (una semilla por receptor nuevo; tiempo NO VERIFICABLE, aunque el pipeline estima 340 min para GEN_TEST de 13 pacientes con 5 semillas, `pipeline_textura.sbatch:189`) y unas horas de lectores.
- Si no se hace: la tesis no dice nada sobre la percepción, lo cual es coherente con no reclamar realismo. Por eso no es indispensable.

**R8 — Piso de ruido de 100:0.3 (G sin M) en los dos receptores de validación** (E-07)
- Pregunta: ¿el aumento de p95 y de η² con η > 0 es ruido o artefacto?
- Coste: GPU baja. Si no se hace: la mejora del barrido es ambigua.

**R9 — Razón de textura real con `metal_0039` en modo crudo, junto al criterio (i)** (E-03)
- Solo CPU.
- Da una referencia real, aunque débil, para (i).

### OPCIONAL

**R10 — Repetir c2b con la misma lectora tras un periodo de espera y orden nuevo**
- Pregunta: ¿qué repetibilidad intra-lectora tiene la puntuación (kappa ponderado)?
- Coste: 1 hora. Solo describe la fiabilidad y no corrige el ciego.

**R11 — Descriptor espectral (tipo espectro de potencia del ruido) del residuo, angular y radial, frente a los tornillos reales**
- Daría una medida de textura más estándar que η².
- Riesgo: otra métrica post hoc con n = 2. Solo si se declara antes.

### TRABAJO FUTURO
- **R12:** prueba de Turing con potencia suficiente, multi-lector y multi-caso, con radiólogos, análisis MRMC y varios tipos de implante y escáneres.
- **R13:** evaluación basada en una tarea (detección de malposición o segmentación con aumento de datos). Es la única vía para hablar de utilidad.
- **R14:** contraste de realismo y comparación visual a ciegas de los tres modelos ya diseñados (`trabajosFuturos.tex:65`), sobre un conjunto independiente.
- **R15:** estudiar si las pérdidas adversariales degradan la coherencia física (*streak amplitude*, perfil) en pacientes no usados.

### No recomendado (scope creep)
- Más brazos de pérdida o más barridos sobre 0101/0102.
- FID o LPIPS con redes de imágenes naturales.
- Sesiones c2b adicionales para elegir brazos.
- Llevar el brazo adversarial a la prueba de Turing sin la condición física de E-09.

**Dependencias:** R2 va antes de R3 y R4. R5 va antes de R7. R1 condiciona todo: si la prueba de Turing se declara trabajo futuro, R7 pasa a R12 y bastan R1–R6.
