# Estado actual

> Lo actualiza Claude al cerrar cada sesion. Fuente de verdad de "por donde voy".

## 2026-10-08 — `overleaf/` al dia con el traspaso del 2026-10-07 (capitulo3-r08)

- **Hecho:** `ENCARGO_2026-10-07.md` bloque A aplicado como ronda acotada `capitulo3-r08` (sin revisores): lectura de HU del Obj 3 por mezcla de canales, criterio de seleccion del punto de control con `\GAPDEC` del tipo de implante, y GAP del Obj 3 reformulado en cap. 3, introduccion y cap. 2. Compila (116 pp.), etapa en `BITACORA.md`. Bloque B sin redactar.
- **Siguiente:** el paso 1 del bloque del 2026-10-07 sigue igual (clasificar `metal_0011/0039/0056`); en redaccion, una ronda con los tres revisores sobre `capitulo3` cuando la autora lo pida.
- **Tambien hecho:** `docs/SITUACION_ACTUAL.md` reescrito como guia pedagogica para la exposicion (decisiones en orden, su porque y alternativas; opinion del profesor marcada como tal). Sin cifras nuevas.
- **Tambien hecho (gaps-r01):** cerrados o estrechados los GAP de `overleaf/` cuya fuente ya existia (11 de 12; 54 `\GAPDEC` quedan, todos de decision real de la autora o de dato). Pendiente de la autora: si se mantiene la contingencia de plazo de #90 sobre el brazo fisico; 3 decisiones de redaccion nuevas en BITACORA §2; soporte del cribado de fractura (cap. 3 dice laminas, `00-tesis.md` dice 18 laminas + 12 volumen).
- **Tambien hecho (gaps-r02):** `00-tesis.md` puesto al dia (pregunta e hipotesis copiadas de `main.tex`, resultado del Obj 2, implante transiliaco-transsacro, envolvente, decisiones de octubre del Obj 3); cap. 3 corregido (soporte del cribado 18 laminas + 12 volumen; Overfull resuelto); visto bueno de la autora a las 3 decisiones de gaps-r01.
- **Pendientes nuevos:** (resueltos el 2026-10-08: visto bueno a las 5 decisiones de r08 y Overfull corregido en gaps-r02); tension 30 000 pasos frente a los candidatos 37 500 / 140 000 (`capitulo3-r08-respuesta.md`).

## 2026-10-07 — TRASPASO. Leer este bloque y nada mas para arrancar

> Escrito para una sesion **sin historial** (la autora hace `/clear`). Sesion del 2026-10-06/07:
> cadena completa en CPU y GPU, descubrimiento del fallo del decodificador (#152), decodificador v2
> fijado y registrado, criterio de seleccion de checkpoint registrado.

### En una frase

La cadena del Objetivo 3 corre sobre dos pacientes de validacion y, con el **decodificador v2**, los
dos checkpoints generan metal de forma parecida; **lo siguiente es el cotejo contra implantes reales**
para elegir checkpoint, y antes hay que **clasificar el tipo de implante** de los 3 pacientes de
referencia.

### Lo que se decidio (`01-decisiones.md`, ambas escritas por el asistente con autorizacion explicita)

| Entrada | Que fija |
|---|---|
| **2026-10-07** | El Obj 3 lee los HU con `regla_suave` (v2), `delta = 0.05`. La `regla` v1 sigue siendo la del Obj 1, **cuyo texto y cifras no cambian** |
| **2026-10-07 (2)** | Definicion comun del cotejo (#150): perfil 2D, cascaras de 0.5 mm, **mediana y p95 como elevacion** sobre el anillo de 12-15 mm; histograma en `M` sobre voxeles > 2500; referencia = `metal_0011`, `metal_0039`, `metal_0056`; regla por envolvente real |

### Lo que se descubrio (todo en `04-implicancias.md`, ABIERTAS)

- **#152 (la mas importante):** la `regla` v1 convertia en techo de SW (~236 HU) o MW (~472 HU) el
  metal que el canal ancho si marcaba. La idea de que `mejor.pt` "genera la mitad del metal" (#145) era
  **casi toda del decodificador**. Peor: la v1 **recortaba la cola clara del streaking en `B_delta`**,
  asi que toda amplitud de rayas medida con ella saldria subestimada (adenda 6). Lista de resultados
  anteriores afectados al final de #152.
- **#150:** el perfil de `a12` y el de `a15` no eran comparables; resuelto con la decision (2). Ademas:
  la fraccion > 2500 HU **no se compara con lo real** (su mascara se define con ese umbral).
- **#151:** con la misma semilla, CPU y GPU no dan el mismo ruido: **un solo dispositivo por cotejo**.

### Donde estan los resultados

| Carpeta (`experiments/objetivo3/outputs/`) | Que es | Lectura |
|---|---|---|
| `a15_v2/` | **0101 y 0102, CPU, v2 `delta=0.05`** — los que valen hoy | v2 |
| `a15_marcas/` | 0101 CPU con `u` crudo dentro de `M` (prueba de #152) | v1 |
| `a15/` | 0101 CPU (#150); `humo_2cortes/` no son resultados | v1 |
| `a15_gpu/` | 0101 y 0102 GPU, Khipu job 54619 (#151) | v1 |
| `a16/` | calibracion de `delta` sobre validacion | v1 y v2 |

### Siguiente paso, en orden

1. **Clasificar el tipo de implante de `metal_0011`, `metal_0039`, `metal_0056`** con el agente
   `clasificador-metal` (propuesta preliminar; ordenado por la autora como PENDIENTE). Si no son
   tornillos, el cotejo se revisa.
2. **Ajustar `a12` (real) y el perfil de `a15` (sintetico) a la decision 2026-10-07 (2)** y correr el
   cotejo con lo de `a15_v2/`. Para el perfil sintetico en 2D con elevacion **no hace falta regenerar**
   si se escriben los volumenes: hoy `a15_v2` se corrio con `--sin-nifti`, asi que o se recalcula
   dentro de `a15` o se regenera con `--nifti` (en Khipu, ~4 min).
3. Despues: sonda de viabilidad de Peters (orden de la decision 2026-10-05 (6)).

### Redaccion: encargo listo

**`redaccion/ENCARGO_2026-10-07.md`** para `/ciclo-redaccion`: A1 declarar el decodificador v2 en el
cap. 3 (sin tocar el Obj 1), A2 escribir el criterio de seleccion de checkpoint, A3 el GAP del Obj 3
quedo desfasado (la cadena SI se ejecuto; sigue sin resultado citable). Bloque B = ABIERTAS, no se
redactan como hecho. `MAPA.md` actualizado.

### Lo tecnico que conviene saber

- **`a15`** gano: `--dispositivo {cpu,cuda}`, `--delta`, `--sin-nifti`, y escribe `_marcas.npz`.
  **No es reanudable.** `a15_cadena.sbatch` lo corre en Khipu (GPU; ~4 min dos pacientes).
- **`src/common/ventanas.py`**: `regla_suave`, `peso_borde`; `decodifica_bloque(u, delta=None)` sigue en
  v1 por omision (reproduce lo ya corrido). **Para el Obj 3, pasar siempre `delta=0.05`.**
- **`a16_calibrar_delta.py`**: nuevo; eligio el `delta`.
- **Memoria de la laptop (12 GB):** `a15` con `--sin-nifti` llega a ~3.8 GB de python; una vez quedaron
  solo 327 MB libres por otro proceso. `0102` con `.nii.gz` murio por memoria el 2026-10-05.
  Para corridas largas: Khipu, o laptop con `--sin-nifti` y registro de memoria.
- **Khipu:** la autora corre los comandos ella misma; el asistente se los da. `KHIPU.md` tiene todo.

### Pendientes de la autora

- Commit: hay mucho sin commitear (`01-decisiones.md`, `04-implicancias.md`, `ESTADO.md`, `ventanas.py`,
  `a15`, `a16`, `a15_cadena.sbatch`, `redaccion/`).
- Si las corridas GPU de #151 se rehacen con la v2 (hoy son v1).
- Lo que ya estaba: #55, #62, #130, #126; las 15 decisiones de redaccion de `BITACORA.md` §2; titulo de
  la seccion 1.5; el 91 % del entrenamiento sin tipo de implante clasificado.

### Advertencia de metodo, otra vez

Esta sesion repitio el patron: el "~471 HU = hueso" de #149 era **el techo de MW** y se habia
presentado como senal fisica. Lo destapo ver el mismo valor repetirse en pacientes y semillas
distintos. **Un valor que se repite exacto en condiciones distintas es un artefacto de medicion hasta
que se demuestre lo contrario.**

## 2026-10-05 (3) — traspaso anterior (superado por el del 2026-10-07)

> Escrito para una sesion **sin historial**. La sesion del 2026-10-05 fue larga: siete entradas nuevas
> en `04-implicancias.md` (#141 a #149), seis en `01-decisiones.md`, cinco scripts nuevos y dos
> capitulos corregidos. Esto es lo que hace falta para seguir.

### En una frase

El Objetivo 3 **ya entrena, ya genera y ya ejecuto su cadena completa**, pero **ningun checkpoint esta
elegido** porque el criterio con que se elegia resulto no medir lo que importa; lo siguiente es correr
`a15` en serio y cotejar contra implantes reales.

### LO PRIMERO AL ARRANCAR: relanzar la corrida que quedo a medias

La autora pidio **pausar** la corrida de la cadena completa para cerrar el chat. Se mato el proceso.

```
cd /d/UTEC/CICLOX/PFCII/metalsynth-pelvis
python -u experiments/objetivo3/a15_cadena_completa.py --caso dataset6_CLINIC_0101_data --cortes 0
```

**25 cortes x 2 checkpoints, ~43 min de CPU.** Dos avisos:

1. **`a15` NO es reanudable.** No guarda por corte, asi que la corrida interrumpida **no dejo nada**:
   empieza de cero. (`a8` si es reanudable; `a15` deberia serlo y es deuda tecnica anotada en #149.)
2. **Lo que hay hoy en `outputs/a15/` es la prueba de humo de 2 cortes**, con `n_M = 19` voxeles. **No
   son resultados.** Ver la correccion a #149.

### LO SEGUNDO: un error de lectura que quedo corregido y hay que no repetir

El asistente reporto que "el orden de los checkpoints se invierte" entre reconstruir y sintetizar, con
10.5 % frente a 31.6 %. **Esas fracciones salen de 19 voxeles**: son 2 voxeles frente a 6. La
afirmacion **se retiro** (correccion a #149) y **tambien se le dijo a la autora en el chat**, asi que
si ella la menciona, esta retirada.

Lo que **si** se sostiene: la cadena corre y los tres controles pasan. **El "~471 HU dentro de `M`"
tambien quedo RETIRADO** (segunda correccion a #149): con los 25 cortes, `run01_140k` da p50 = 3409 HU.

### Las seis decisiones que la autora tomo el 2026-10-05 (`01-decisiones.md`)

| Entrada | Que fija |
|---|---|
| **(2)** | **30 000 pasos** de entrenamiento, declarado como eleccion sobre validacion. **Aplazada su revision**, ver (6) |
| **(3)** | Definicion operativa de `streak amplitude`: verdad de terreno = la TC limpia del mismo paciente, lo que ancla el endpoint en **E-A2**; ROIs derivadas de la pose; censura del suelo reportada como cifra; agregacion por paciente; jerarquia TOST / realismo / cordura |
| **(4)** | Los cuatro parametros de las ROIs, fijados sobre validacion. **La preinscripcion del endpoint primario quedo completa** |
| **(5)** | El brazo fisico **se reproduce, NO se valida**; y lo verificado en su codigo entra al documento |
| **(6)** | **El modelo final NO se elige por la perdida de validacion.** Se elige comparando el perfil radial de HU y el histograma dentro de `M` de lo sintetico contra implantes reales. Validacion = **3 pacientes** de CLINIC-metal. **B1 y B2 aplazados.** #142 y #143 se **declaran**, no se rehacen. **Cadena completa ANTES que Peters** |

**La (6) es la que manda sobre el trabajo tecnico.** Y contiene una correccion que la autora acepto:
la primera version proponia elegir con metricas de **reconstruccion**, y se descarto porque esa tarea
**premia memorizar** y no se traslada al uso real.

### El orden de trabajo acordado

1. **Correr `a15` completo** sobre `dataset6_CLINIC_0101_data` (comando arriba).
2. **Repetir sobre los otros pacientes limpios de validacion.** Candidatos verificados: `0101`
   (corredor 10.6 mm) y `0102` (12.4 mm). **`0019` NO sirve**: su corredor mide 1.6 mm y el tornillo
   lo perforaria por construccion.
3. **Cotejar** el perfil radial y el histograma de lo sintetico contra los de implantes **reales**, que
   calcula `a12_roi_parametros.py`. **Ese cotejo es el criterio de seleccion de checkpoint.**
4. **Sonda de viabilidad de Peters**, no la implementacion completa: un corte, con el tornillo y la
   anatomia de esta tesis. Su protocolo es **2D de una sola fila de detector** y el tornillo mide
   138 mm en el eje: si esa extension es inviable, **el contraste primario se queda sin brazo**.
5. Peters completo -> `Delta` -> congelar `diseno_A.md` -> corrida final.

### Los cinco scripts nuevos del 2026-10-05

| Script | Que hace | Estado |
|---|---|---|
| `a8_muestra_serie.py` | genera una **serie completa** de cortes y escribe HTML navegables, `.nii.gz`, montaje y controles | usado; **reanudable** |
| `a9_suelo_representacion.py` | mide cuanto recorta el suelo de -1000 HU, **sin modelo** | corrido sobre 23 058 parches |
| `a10_costura.py` | salto de HU al cruzar el borde de `G`, en 3D y por corte | corrido sobre las dos muestras |
| `a11_rasterizar_tornillo.py` | **pose -> `M`, `B_delta`, `G`**. Era el eslabon que faltaba | verificado en 3 casos |
| `a12_roi_parametros.py` | perfil radial del artefacto **real**, y los parametros de las ROIs | **su salida es la referencia del paso 3** |
| `a13_comparar_ckpt.py` | compara dos checkpoints pareado sobre validacion | corrido, 5 pacientes |
| `a14_curvas.py` | grafico de las curvas de entrenamiento | `outputs/a7/a14_curvas_run01_run02.png` |
| `a15_cadena_completa.py` | **la cadena entera**: pelvis limpia -> pose -> `M` -> generacion | **a medio correr; relanzar** |

### Lo que hay que saber de los dos entrenamientos

- `run02` termino: **60 000 pasos en 6 h 20**, minimo de validacion en el paso **37 500**.
- **`run01` y `run02` NO son corridas independientes** (#148): misma semilla 20260920, mismos datos,
  tasa de aprendizaje constante. Son **la misma trayectoria medida dos veces**. **No se puede afirmar
  reproducibilidad**; eso exigiria otra semilla y no se ha corrido.
- Los dos `curva.csv` estan en local, y el grafico en `outputs/a7/a14_curvas_run01_run02.png`.

### Pendientes de la autora, por urgencia

1. **Nada bloquea el paso 1.** Se puede correr `a15` ya.
2. **El hueco del contraste de realismo:** la decision (3) lo especifico contra "la amplitud de rayas
   medida en CLINIC-metal real", y **esa magnitud no es calculable** en pacientes con implante real
   porque exige una imagen sin metal del mismo paciente. La decision (6) lo resolvio **para la
   seleccion de checkpoint**, pero **sigue vivo en el criterio de exito D4**.
3. **#142 y #143 estan decididas pero sin redactar**, y #143 necesita antes medirse sobre poses
   **perturbadas**, que son oblicuas casi siempre.
4. **El 91 % del conjunto de entrenamiento no tiene clasificado su tipo de implante** (15 558 parches
   de 216 componentes sin revisar; de los 25 revisados, solo 6 son tornillos). Sin registrar como
   implicancia: la autora no lo pidio.
5. **La validacion esta dominada por un paciente:** `0011` aporta el 60 % de los parches y el 65 % del
   metal de los tres.
6. Sigue pendiente: etiquetas de estado de #55, #62 y #130; **#126**; las **15 decisiones de
   redaccion** de `BITACORA.md` §2; el **titulo de la seccion 1.5**; y la **segunda muestra de `a8`**
   (`dataset7_CLINIC_metal_0056_data_c001`), que el sistema mato por memoria y nunca se relanzo.

### Estado del repositorio

Hay un commit nuevo del 2026-10-05, `c786b9a` ("obj 3 exps"). **Sin commit quedan**:
`docs/01-decisiones.md`, `docs/04-implicancias.md` y `experiments/objetivo3/a15_cadena_completa.py`.

### Advertencia de metodo, que esta sesion volvio a confirmar

**Tres veces** en el dia se reporto como hallazgo una cifra que venia de una muestra de la cola o
demasiado chica: el 23.4 % del suelo (un componente de un paciente), el +196 HU de costura (un corte),
y el 10.5 % frente a 31.6 % de la cadena (**19 voxeles**). Las tres se corrigieron, pero **ninguna la
detecto el asistente por su cuenta**: dos las destapo una pregunta de la autora y la tercera aparecio
al leer el CSV para cerrar. **Ante una cifra nueva, mirar primero cuantos datos la sostienen.**

## 2026-10-05 (2) — PRIMERA SERIE SINTETICA COMPLETA y #141: el suelo de la representacion borra la inanicion de fotones. Cap. 3 y cap. 1 corregidos en r06

**Ultimo paso completado.** Tres cosas, en este orden.

1. **BLOQUE 0 del encargo, hecho.** `auditor-trazabilidad` audito las 36 implicancias CERRADA con
   paridad **y** recuento: `redaccion/rondas/paridad-r01-trazabilidad.md`, **9 altas / 8 medias / 3
   bajas**. Las dos pruebas de control se detectaron y se **ampliaron**: #135 no era un caso aislado
   (cuatro sitios de `overleaf/`, cinco implicancias sin propagar) y #136 habia dejado sin marcar una
   **tercera** cifra falsa de #132. Dos cifras nuevas no cuadran dentro de entradas CERRADA: el
   encabezado de **#122** (16 de 72, deberia ser **15 de 72 = 20.8%**) y **#132 seccion 4** (21 casos y
   "7 ilion", deberian ser **20** y **6 ilion**). Todo en **#140**.
2. **`a8_muestra_serie.py`, nuevo: primera serie COMPLETA de cortes sinteticos.** 66 cortes
   consecutivos (235 a 300) de `dataset7_CLINIC_metal_0011_data_c011`, paciente de **validacion**, con
   el `ckpt` de `run01` (paso 140 000, pasado de su optimo). Los dos controles duros **PASAN en los 66
   cortes**. Salidas en `experiments/objetivo3/outputs/a8/`: dos `.html` navegables (3D con metal real
   en magenta y generado en verde; recorrido corte a corte con deslizador), tres `.nii.gz`, montaje y
   `controles.csv`. **De ahi salio #141** (abajo). La **segunda muestra**
   (`dataset7_CLINIC_metal_0056_data_c001`, 86 cortes) **no corrio**: el sistema mato el proceso por
   memoria. Es reanudable y no repite nada.
3. **`/ciclo-redaccion capitulo3` r06 y `capitulo1` r06, las dos cerradas.** Cap. 3: 25 altos/medios
   aplicados, 0 rechazados, 0 escalados. Cap. 1: 5 altos y 15 medios, 0 rechazados, **2 escalados**.
   El documento compila: **111 paginas**, 0 errores, 0 citas indefinidas, 0 Overfull. PDF por etapa en
   `redaccion/.build/etapas/capitulo3-r06.pdf` y `capitulo1-r06.pdf`.

**#141, EL HALLAZGO DE LA SESION.** El suelo de la codificacion multiventana esta en **-1000 HU**
(`CONFIG_DISENO_A = 'pub+asinh'` es `asinh_canal(-1000.0, 20000.0)`; su `ida` aplica `np.clip`), y el
**23.4% de los voxeles de `G`** de un caso real con metal cae por debajo. Eso es **inanicion de
fotones**, y el Diseno A **no puede representarla**. Control de ida y vuelta **sin modelo**: minimo
real **-6048 HU**, tras ida y vuelta **-1000 HU exacto**; el techo en cambio sobrevive intacto
(12 472 HU). **Las nueve configuraciones candidatas de E6c comparten `low = -1000.0`**: el suelo nunca
fue una variable del experimento, solo se estudio el techo. La ida y vuelta del Objetivo 1 no podia
detectarlo porque se mide sobre **HU de hueso**.

**#141 MEDIDA Y ACOTADA el mismo dia.** `a9_suelo_representacion.py` (nuevo) la midio sin modelo sobre
**23 058 parches de 77 pacientes** de entrenamiento y validacion, nunca test. La lectura es **de cola,
no de centro**: en el paciente tipico el recorte toca el **1.0 %** de la banda y el vano entre los
extremos del 5 % sobrevive al **99.9 %**, pero **19 de 77 pacientes pasan del 10 %**, 9 del 20 %, uno
llega al **44.9 %**, y en el peor el parche mediano pierde **la mitad del vano**. El 23.4 % que
origino la entrada era de la cola alta. **La correlacion entre el minimo del volumen y lo recortado es
-0.12: saber hasta donde baja un volumen no predice cuanto pierde.** Ademas quedo verificado que la
metrica afectada es **`streak amplitude`**, que Peters et al. definen como el vano entre el 5 %
superior y el 5 % inferior: el suelo recorta uno de los dos extremos, el sesgo es siempre a la baja y
**solo afecta al brazo del sintetizador**, no al fisico. Eso toca **D4**, no solo la redaccion. El
titular de #141 quedo corregido: sobreafirmaba.

**`run02` TERMINADO el 2026-10-05 (#134 ampliada). LA U SE REPRODUCE CON EL ESTIMADOR CORREGIDO.**
Job **54498**, `ag001`, 06:38:18 a ~12:55, **60 000 pasos en ~6 h 20** a **0.377 s/paso**
(9 549 pasos/h) en la MIG `a100_3g.20gb`, 12.3 GB de 20; no toco la pared de 12 h. Arranco ~21 h antes
de lo predicho.

| Bloque | 0 | 10 k | 20 k | **30 k** | 40 k | 50 k | 60 k |
|---|---|---|---|---|---|---|---|
| val | 0.08098 | 0.06271 | 0.05927 | **0.05891** | 0.06132 | 0.06364 | 0.06590 (1 fila) |

`MEJOR VALIDACION: 0.05519 en el paso 37500 (mejor.pt). Ultimo paso: 60000.`

**Lo que esto establece:** el sobreajuste **es del modelo, no del instrumento**. `run01` ya mostraba la
U pero con el `mide_val()` defectuoso; con `SEMILLA_VAL` fija se vuelve a ver. **OJO (#148): `run01` y
`run02` NO son corridas independientes** —misma semilla 20260920, mismos datos, tasa de aprendizaje
constante— asi que son **la misma trayectoria medida dos veces**. No se puede concluir
reproducibilidad: eso exigiria otra semilla, que no se ha corrido. Y `mejor.pt` justifico
su existencia: el minimo esta **22 500 pasos** antes del final, el 37.5 % de la corrida se gasto despues
del optimo, y con el `guarda()` anterior esas pesas **se habrian perdido otra vez**.

**DOS COMPARACIONES PROHIBIDAS, escritas para que nadie las repita:** `0.05519` de `run02` **no es
"mejor"** que `0.05809` de `run01` —instrumentos distintos— y la subida mas chica de `run02` **no es
menos sobreajuste**, es menos corrida (2 bloques frente a 12). Detalle en #134.

**`run01/curva.csv` YA ESTA EN LOCAL y las DOS curvas son la misma.** 289 filas, ultimo paso 144 500.
Reproduce lo registrado: minimo 0.05809 en el bloque 20-30 k, subida durante **doce** bloques hasta
0.10807. Comparadas bloque a bloque sobre los 60 000 pasos compartidos, `run01` y `run02` coinciden
dentro de **1.5e-3 en todos los bloques**, con instrumentos distintos. De ahi salen dos cosas:

- **El entrenamiento es reproducible**, no fue una corrida afortunada.
- **El minimo es una MESETA de ~20 000 a ~40 000 pasos**, no un punto: `run01` lo pone en 20-30 k y
  `run02` en 30-40 k, y esos dos bloques difieren menos que las dos corridas entre si. Despues del
  bloque 40-50 k la subida es monotona en las dos.

**Eso cambia la forma de B2:** la pregunta no es el paso optimo sino **donde termina la meseta**, y la
respuesta medida es **~40 000**. 40 000 queda en el extremo alto; **30 000** cae en el centro y cuesta
un 25 % menos. Las dos son defendibles; la eleccion es de la autora.

**Correccion de metodo, afinada con `run01` en la mano:** la justificacion escrita aqui
("promediar cancela el ruido del estimador") **era cierta para `run01` y ahora esta demostrada** —el
promedio recupero una curva que coincide con la determinista dentro de 1.5e-3 pese al +-15 % por
fila— y es **obsoleta para `run02`**, donde con semilla fija no hay ruido de estimador y las filas
sueltas si se comparan entre si. Asimetria que no hay que perder: `run01` promediaba sobre `t` y el
ruido, asi que estima la perdida esperada; `run02` usa **un solo sorteo fijo**, asi que es comparable
entre pasos pero es una **muestra sesgada** de esa perdida. **Sigue prohibido comparar filas sueltas
entre corridas; comparar bloques queda habilitado.**

**Siguiente paso. `Delta` (D4) ESTA DESBLOQUEADO: `mejor.pt` existe.** El orden es: traer
`mejor.pt` y las dos `curva.csv` -> medir `Delta` como lo define D4 (dispersion entre semillas DDIM del
mismo caso y test-retest del brazo fisico, **solo en los 5 pacientes de validacion**) -> **compararlo
contra 0.914**, el percentil 5 preinscrito en `01-decisiones.md` el 2026-10-05, que resuelve #141 ->
recien ahi congelar `diseno_A.md` y correr la corrida preinscrita. Redaccion: `/ciclo-redaccion
introduccion` (A2 y los tres altos de A-09), `capitulo2` (A3) y el glosario; `capitulo3` r07 y
`capitulo1` r07 quedan como rondas de verificacion **no corridas**.

**DECIDIDO el 2026-10-05: la definicion operativa de `streak amplitude` para sintesis** (`01-decisiones.md`,
entrada 2026-10-05 (3)). Cuatro piezas: verdad de terreno = el CT limpio del mismo paciente, lo que
ancla el endpoint en **E-A2** y no en E-A1; **ROIs derivadas de la pose** (arcos anulares en planos
perpendiculares a `u` dentro de `B_delta`), identicas para los dos brazos; **la censura por el suelo de
-1000 HU se reporta como cifra** (fraccion de voxeles de la ROI en el suelo), lo que convierte #141 en
medicion; y **la unidad de agregacion es el paciente**, lo que cierra un `\GAPDEC` abierto. Jerarquia:
TOST contra el brazo fisico como **primario**, distancia entre distribuciones frente a CLINIC-metal real
como **realismo**, y Wilcoxon contra copia y pegado declarado **control de cordura y no evidencia**,
porque su amplitud vale ~0 por construccion. **Corrigio un defecto de la tabla de evaluacion:**
`streak amplitude` estaba listada como medible en E-A1, donde no hay verdad de terreno; esa fila ahora
mide discrepancia. **Faltan cuatro parametros de las ROIs**, que se fijan sobre validacion al congelar
`diseno_A.md`.

**TARDE DEL 2026-10-05: BRAZO FISICO ARRANCADO, ENDPOINT PREINSCRITO, Y UN HALLAZGO QUE CUESTIONA B2.**

- **`streak amplitude` preinscrita por completo.** `01-decisiones.md` entradas **2026-10-05 (3)** (verdad
  de terreno = la TC limpia del mismo paciente, lo que ancla el endpoint en **E-A2** y no en E-A1; ROIs
  derivadas de la pose; censura del suelo reportada como cifra; agregacion por paciente; jerarquia
  TOST / realismo / cordura) y **(4)** (los cuatro parametros de las ROIs, fijados sobre validacion con
  `a12_roi_parametros.py`). **Ya no queda ningun parametro del endpoint por decidir cuando lleguen los
  resultados.** La guarda se fijo **al minimo por argumento** porque dos criterios de medicion fallaron
  por razones opuestas, y porque una guarda mayor sesga el endpoint a la baja igual que el suelo.
- **Brazo fisico: corre en local.** `pip install -e repos/xcist-main` (commits `4cf3544` y `4993e87`,
  licencia BSD 3-Clause). Simulacion mas reconstruccion en **~70 s por corte**. **Paciente y metal se
  proyectan JUNTOS**, por desplazamiento de agua antes de la proyeccion: eso **cierra un pendiente
  escrito en `main.tex`**. Su script publicado **no corre tal como viene** y el parche vive en
  `experiments/objetivo3/peters/`, nunca en el clon. Todo en **#146**, y la decision de **no validar
  XCIST** en `01-decisiones.md` **2026-10-05 (5)**.
- **#145, EL HALLAZGO MAS INCOMODO DEL DIA.** Comparando los dos checkpoints sobre la misma serie, los
  mismos cortes y la misma semilla, **`mejor.pt` (el minimo de la perdida) pierde en las ocho
  magnitudes de apariencia**: genera el **54.8 %** del metal real frente al **94.9 %** de `run01`,
  duplica la costura y pierde en MAE dentro del metal y en la banda. La hipotesis facil —que la perdida
  esta dominada por la banda— se midio y es **falsa**. **Si la perdida no ordena los modelos por
  fidelidad en HU, B2 se eligio con el instrumento equivocado**, y la evidencia de B1 (la curva de la
  perdida) tampoco demuestra saturacion.
- **`a13_comparar_ckpt.py` corriendo**: repite esa comparacion en los **5 pacientes de validacion**,
  12 cortes por paciente, pareado. **De el dependen B1, B2 y el mecanismo de `mejor.pt`.** Limite
  declarado de antemano: con n = 5 solo el resultado unanime alcanza significacion (p = 0.031).
- **#147: el conjunto de validacion no es lo que el diseno dice.** Los "5 pacientes con metal" son
  **3 con implante y 2 con objeto incidental de `dataset6`**, con un factor **23** entre su contenido
  metalico (1 226 frente a 28 075 voxeles). `Delta` se calibraria en parte sobre metal que no es el
  objeto de la tesis, y **A13 hereda el defecto**: su analisis se hara dos veces, con los 5 y con los 3.
  Ademas **el `n` del contraste primario no es 14**: el brazo fisico corre sobre un subconjunto
  reducido cuyo numero sigue en `\GAPDEC`.
- **`/ciclo-redaccion capitulo3` r07 cerrado** (encargo acotado, sin revisores): 11 de 11 puntos
  aplicados, **114 paginas**, lint de seccion PASA. Cerro 3 `\GAPDEC`, estrecho 2 y abrio 1 mas 1
  `\GAPLIT` por la referencia del software. PDF en `redaccion/.build/etapas/capitulo3-r07.pdf`.
- **Implicancias nuevas de la tarde:** #144 (el codigo del benchmark confirma la definicion de la
  metrica y da su licencia), #145, #146, #147, mas ampliaciones a #134 y a #141.

**Pendientes que surgieron.**
- **Corregir en `docs/04-implicancias.md`** el encabezado de **#122** (16 -> 15, 22% -> 20.8%) y la
  **seccion 4 de #132** (21 -> 20, 7 ilion -> 6 ilion), y extender el aviso de #136 a la tabla de
  `D_TS` (cuenta el `dudoso` al reves que la fila ya corregida: n = 9 y 5.9 mm, no 10 y 6.7 mm). Solo
  lo escribe la autora (regla 3). **Mientras no se corrija, cada ronda de redaccion necesita las
  cifras buenas a mano en el encargo del agente.**
- **Unificar la etiqueta de estado de #55, #62 y #130**: dicen ABIERTA en su encabezado y CERRADA en
  una tabla resumen del mismo archivo.
- **Visto bueno a 15 decisiones de redaccion** en `redaccion/BITACORA.md` §2 (4 del cap. 3, 11 del
  cap. 1). La unica que puede necesitar fuente: **no escribir "SERUM"**, porque su expansion no consta
  en ningun archivo del repositorio.
- **Dos escalados vivos del cap. 1:** el **titulo de la seccion 1.5** (desde r01) y nombrar la prueba
  exacta de Fisher en `capitulo3.tex:265`.
- **Tres contradicciones entre capitulos** aparecieron en una sola ronda (cap. 1 contra cap. 2 y contra
  cap. 3). El ciclo no tiene hoy ningun paso que compare capitulos: cada revisor ve una seccion. La
  pasada **`/ciclo-redaccion documento`** existe para eso y **no se ha corrido nunca**.
- **HECHO el 2026-10-05: la regla de decision de #141 ya esta en `docs/01-decisiones.md`**, dictada por
  la autora y registrada por el asistente con instruccion explicita, como la entrada del 2026-09-07.
  Preinscribe las cifras **antes** de conocer `Delta` (0.999 mediana, 0.914 p5, 0.498 peor paciente) y
  fija el **percentil 5 del paciente** como estadistico de decision, declarado como eleccion post hoc.
  **Lo que sigue abierto es el desenlace**, que se resuelve al medir `Delta` tras el piloto de `run02`.
- **Los pasos 4 y 5 de la recomendacion de #141 NO se aplicaron** (regla 14): declarar el suelo en
  alcance, en amenazas a la validez de constructo y en el criterio de la compuerta del Objetivo 1, y
  nombrar el arreglo en trabajos futuros. Entran en `/ciclo-redaccion introduccion` y en la proxima
  ronda del cap. 3, y su redaccion depende de lo que decida la regla. Hoy el cap. 3 y el cap. 1 ya
  llevan su `\GAPDEC` del suelo, sin cifras.
- **Relanzar la muestra 2** cuando la memoria lo permita:
  `python experiments/objetivo3/a8_muestra_serie.py --serie dataset7_CLINIC_metal_0056_data_c001`
- **Todo el trabajo sigue sin commit**, incluido el de la sesion anterior.

## 2026-10-04 — OBJETIVO 3: PRIMER ENTRENAMIENTO REAL. Sobreajuste medido; `run02` en cola hasta el lunes 6

**Ultimo paso completado.** Se entreno el renderizador del Diseno A por primera vez con el bucle de
validacion conectado (job 54367, A100 de ag001, 144 500 pasos, 8 h). Resultado: **sobreajuste
confirmado**. La validacion toca su minimo en el bloque 20-30 k (**0.05809**, ~paso 25 000) y de ahi
sube durante **doce bloques consecutivos** hasta 0.10807. Los ~119 500 pasos posteriores al minimo
(6 h 34 min de A100) **empeoraron el modelo**. Todo en #134.

**Dos defectos encontrados y corregidos en `src/renderizador/entrenar.py`:**
1. `mide_val()` llamaba a `perdida` **sin `generador`**, asi que sorteaba `t` y el ruido en cada
   medicion: la columna oscilaba +-15% por COMO se media. Ahora usa `SEMILLA_VAL = 20261004`.
2. **No habia modelo mejor.** `guarda()` sobrescribia un unico `ckpt.pt`, asi que **las pesas del
   minimo de `run01` se perdieron**. Ahora se escribe `mejor.pt` con el minimo de validacion.

**Siguiente paso.** `run02` esta en cola con `--gres=gpu:a100_3g.20gb:1` (particion MIG de 20 GB; solo
se usan 12.31), `--time=12:00:00` y **`--pasos 60000`**. El cluster esta saturado: **arranque predicho
2026-10-06T04:02**, y todas las alternativas probadas (A6000, tesla, shards, A100 entera) arrancan mas
tarde. Al terminar: `mejor.pt` -> medir `Delta` (D4) -> congelar `diseno_A.md` -> corrida preinscrita.

**Pendientes que surgieron.**
- ~~Confirmar 60 000 como `--pasos`~~ **DECIDIDO el 2026-10-05: 30 000 pasos** (B2), centro de la
  meseta de ~20 000 a ~40 000 que trazan las dos corridas. En `docs/01-decisiones.md`, declarado como
  eleccion sobre **validacion** y no fijada de antemano. **Falta llevarlo a `diseno_A.md`**, que se
  congela despues de `Delta`.
- **Decidir si la saturacion con 47 pacientes entra como limitacion declarada.** El renderizador no
  mejora con mas computo; si `Delta` no alcanza, la palanca son mas pacientes. Hoy eso no esta escrito
  en ninguna parte del documento.
- **#115 pasa de prediccion a observacion** y hay que decidir como se declara.
- **NO borrar `data/a7/run01/`**: `curva.csv` es la evidencia de la U y `ckpt.pt` la del sobreajuste.
- **RESUELTO el 2026-10-05:** el medico confirmo que la "parte de atras" aceptada como S1 es la
  **cresta sacra media** (#138). Desbloquea el `\GAPDEC` de `capitulo3.tex:97` (bloque A4). **Queda
  abierto** si se mide la diferencia entre el techo de la etiqueta `vertebrae_S1` y el platillo
  superior de S1, que es a lo que se ancla el marco de Kaiser.
- **PRIMERA MUESTRA CON MODELO ENTRENADO, 2026-10-05.** Con el `ckpt.pt` de `run01` (**paso 140 000**,
  el ultimo checkpoint antes del corte; **pasado de su optimo**, ver #134):
  `experiments/objetivo3/outputs/a6/a6_dataset7_CLINIC_metal_0011_data_c011_k0263.png` y los dos
  `.nii.gz` (`_original`, `_compuesta`) para ITK-SNAP. Los dos controles de preservacion **pasan
  exactos** (0.000e+00 fuera de `G`), y el modelo **genera HU de rango metalico, hasta 10 570 HU**
  frente a 12 472 del real. `a6_muestra_minima.py` gano `--mas-metal` y `--nifti`.
- **Todo el trabajo del dia sigue sin commit.**

**PARA EL SIGUIENTE AGENTE — leer antes de hacer nada.**

0. **DECISION DE LA AUTORA, 2026-10-05: el `dudoso` del cribado de fractura NO cuenta como fractura
   y se reporta aparte.** Cifra unica para el documento: **20 de 30 (67%) con fractura confirmada,
   mas un caso dudoso**; por grupo, **10 frente a 10**. Dos cifras de #132 estaban mal (contaban el
   dudoso) y quedan rectificadas en **#136**, con un aviso dentro de la propia #132. **No escribir
   70% ni 73%.** Falta que la autora registre esta decision en `docs/01-decisiones.md`, que solo
   escribe ella (regla 3); el texto propuesto se le entrego en el chat del 2026-10-05.

0b. **ETAPA DE REDACCION: ESTE ES EL ORDEN. No improvisar otro.**

   | # | Que correr | Que lleva | Por que ahi |
   |---|---|---|---|
   | **1** | **BLOQUE 0 del encargo**, `auditor-trazabilidad` sobre TODAS las implicancias CERRADA | paridad `main.tex` vs `overleaf/` **y** recomputo de cifras | #135 mostro que una CERRADA puede no haber llegado a `overleaf/`; #136, que puede traer una cifra falsa. **Redactar antes es arreglar frases sin saber cuantas hay** |
   | **2** | `/ciclo-redaccion capitulo3` | **A1** (afirmacion FALSA), **A4** (cresta sacra media), **A2** en lineas 101 y 196 | A1 es lo unico que corrige algo falso ya impreso |
   | **3** | `/ciclo-redaccion capitulo1` | **A2**, resuelve el `\GAPDEC` de la linea 72 | el `\GAPDEC` ya esta escrito y pregunta justo lo que #130 contesta |
   | **4** | `/ciclo-redaccion introduccion` | **A2**, lineas 32, 39 y 66 | — |
   | **5** | `/ciclo-redaccion capitulo2` | **A3**, linea 74 | — |
   | **6** | `docs/03-glosario.md`, lineas 74-75, edicion directa | **A2** | no pasa por `/ciclo-redaccion` |

   **Al cerrar todas las rondas: recompilar y abrir el PDF** (preferencia registrada de la autora).

   **Dos trampas del bloque A2**, que estan detalladas en el encargo: hay menciones que **deben seguir
   diciendo "iliosacro"** porque describen lo que hicieron Smith, Kaiser, Reilly y Liu; cambiarlas
   seria atribuirles algo que no dijeron. Y en A1 **no escribir 70% ni 73%**: la cifra es **20 de 30
   (67%)** mas un caso dudoso aparte.

1. **Redaccion: el encargo ya esta escrito en `redaccion/ENCARGO_2026-10-04.md`.** Tiene un bloque A
   con cuatro cambios listos para aplicar (cada uno con su fuente, los archivos y lineas exactos, y
   que menciones NO hay que tocar) y un bloque B con cinco puntos **bloqueados** esperando decision
   de la autora. No mezclar los dos bloques. El mas urgente es **A1**: `capitulo3.tex:263` afirma
   que las pelvis receptoras estan "sin fractura conocida", y **#132 lo desmiente** (20 de 30).
2. **Khipu: no hay nada que hacer hasta el 2026-10-06 ~04:02.** `run02` es el **job 54498**,
   enviado el 2026-10-04 y en cola con razon `(Priority)`, que es espera normal por turno. Las
   cuatro lineas del sbatch y la copia de `entrenar.py` en Khipu (con `SEMILLA_VAL` y `mejor.pt`)
   quedaron verificadas antes de enviar. No reenviar,
   no cancelar, no bajar la pared: ya se probaron A6000, tesla, shards y A100 entera, y la particion
   MIG `a100_3g.20gb` es la que arranca antes. Pedir 12 h en vez de 8 no retrasa el arranque.
3. **ANTES DE ENVIAR CUALQUIER JOB, verificar las CUATRO lineas del sbatch.** El 2026-10-04 se
   envio el job 54490 con el GRES y la hora corregidos pero con `SALIDA=$DATA/a7/run01` y
   `--pasos 200000` sin corregir: con `--reanudar` habria **cargado el `ckpt.pt` sobreajustado de
   `run01`** y entrenado 200 000 pasos mas desde ahi, gastando el turno y sobrescribiendo la
   evidencia de la U. Se cancelo a tiempo. Un `sed` de varios `-e` puede aplicar unos y otros no, y
   `squeue` no avisa de nada: lo unico que lo detecta es mirar el archivo.

```
cd ~/metalsynth && grep -nE "^#SBATCH --(gres|time)|^SALIDA=|--pasos" a7_a100.sbatch
```

   Las cuatro que tienen que salir: `--gres=gpu:a100_3g.20gb:1`, `--time=12:00:00`,
   `SALIDA=$DATA/a7/run02`, `--pasos 60000`.

4. **Comandos de seguimiento y de traida de resultados:**

```
squeue -j <JOBID>
squeue --start -j <JOBID>
cd ~/metalsynth && tail -f a7entr_<JOBID>.log
```

   Tabla de validacion por bloques de 10 000 pasos, que es como se lee la curva (promediar cancela
   el ruido del estimador; las filas sueltas no se citan):

```
cd ~/metalsynth && awk -F, 'NR>1 {b=int($1/10000); s[b]+=$3; c[b]++} END {for (i in s) printf "%d\t%.5f\t%d\n", i*10000, s[i]/c[i], c[i]}' data/a7/run02/curva.csv | sort -n
```

   Traer a local (desde la raiz del repositorio; **la autora no acepta llaves `{}` en los comandos**):

```
mkdir -p experiments/objetivo3/outputs/a7/run01 experiments/objetivo3/outputs/a7/run02
scp kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/a7/run01/curva.csv experiments/objetivo3/outputs/a7/run01/
scp kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/a7/run02/curva.csv experiments/objetivo3/outputs/a7/run02/
scp kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/a7/run02/mejor.pt experiments/objetivo3/outputs/a7/run02/
scp kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/a7entr_54367.log experiments/objetivo3/outputs/a7/run01/
```

   **`run01/curva.csv` hay que traerlo ya**: es la evidencia de la U y hoy solo existe en Khipu.
   `mejor.pt` son ~112 MB y `ckpt.pt` ~340 MB; `ckpt.pt` de `run01` se deja en Khipu, no hace falta
   en local salvo para reproducir el sobreajuste.
5. **Cuando `run02` termine**, el orden es: leer la tabla por bloques -> confirmar el paso del minimo
   que imprime el log (`MEJOR VALIDACION: ... en el paso N`) -> medir `Delta` (D4) con `mejor.pt`
   -> recien ahi congelar `diseno_A.md` -> corrida preinscrita.

**Advertencia de metodo, repetida.** Dos veces hoy interprete el instrumento como si fuera la senal:
reporte una "inversion de la brecha" que era ruido de medicion y hubo que retirarla. Ante una cifra que
se mueve, revisar primero **como se mide**.

## 2026-10-03 — `/ciclo-redaccion capitulo1` (marco teorico, todas las secciones): TOPE en r05, con decisiones pendientes

- **Hecho:** cap. 1 redactado desde el esqueleto (r00) y corregido en r01 a r05. El lint de la seccion da 0/0/0 y el documento compila (107 pag., 0 Overfull). PDF de cada etapa en `redaccion/.build/etapas/capitulo1-r0*.pdf`. Hallazgos medios de los revisores: 36 en r01, 6 en r05, todos de estilo salvo uno. GAP: 4 lit, 1 dato, 8 dec. Se abrio la #130 (que tornillo representa el corredor medido; Zwingmann et al. lo llaman iliosacro y transiliosacro).
- **Siguiente:** la autora decide la #130, el titulo de 1.5 ("Marco estadistico" frente a "marco" reservado para Kaiser et al.) y si el codigo de `experiments/` cuenta como fuente. Luego `capitulo4` o una ronda mas de `capitulo1`.
- **Pendientes:** 3 `\GAPLIT` nuevos de fuentes de referencia (fisica de TC, anatomia pelvica, W1, Wilcoxon, TOST y remuestreo) en `_candidatos.md`; en el cap. 3 falta unificar el simbolo de la normal (guia-12 de r01) y usar "transsacro" segun lo que decida la #130.

## 2026-09-30 (2) — `/ciclo-redaccion capitulo2` (estado del arte): TOPE en r06, con decisiones pendientes

- **Hecho:** cap. 2 redactado desde esqueleto (r00; pausa tras r01 a pedido de la autora) y corregido en r01 a r06. Lint de seccion 0/0/0, compila (90 pag.). PDF por etapa en `redaccion/.build/etapas/capitulo2-r0*.pdf`. Medios de revisores: r01 2/32 -> r06 0/9. GAP 1 lit / 2 dato / 10 dec. Se abrio la #129 (ida y vuelta ya medida contradice #128.3, intro:46 y cap3:172; unidad y dominio de los RMSE que anclan los 25 HU; cifras de Jacob et al.).
- **Siguiente:** la autora decide #129 (sobre todo encargar a `lector-papers` Karageorgos y Yun) y los dos escalados; luego una ronda mas de `capitulo2` o alinear introduccion y cap. 3 con la ida y vuelta medida.
- **Tablas (inspeccion visual):** la Tabla 2.1 desbordaba la pagina; ahora es la Tabla A.1, apaisada en `anexos.tex`. Las tablas 3.1-3.3 caben. Compila con 0 Overfull.
- **Pendientes:** relecturas `hu2023` Fig. 3, `herman2016` p. 8, `ramzan2026claim` Sec. 3.5, `selles2023ai` (sin evidencia textual); `\label` del cap. 4; "zona segura" sin definir (intro:75); intro:60 "codificacion de la entrada"; Xie "cobertura en exceso" en la intro mas fuerte que la ficha.

## 2026-09-30 — `/ciclo-redaccion introduccion` (solo Objetivos, Justificacion y Alcance): TOPE en r05

- **Hecho:** tres subsecciones reescritas (r00) y corregidas en r01 a r05. Dentro del alcance el lint da 0/0 y compila (67 pag.). Revisores alta/media: r01 2/27 -> r05 0/12 (solo estilo no baja). Los PDF estan en `redaccion/.build/etapas/introduccion-r0*.pdf`. Se abrio la #128: eslabones del argumento sin fuente, en especial para que el sintetizador si el protocolo fisico corre sobre las mismas poses.
- **Siguiente:** la autora decide #128, #127 y #126. Luego se reescriben el encabezado y la Formulacion del problema (pregunta, hipotesis) y se alinean con los nuevos objetivos.
- **Pendientes para el cap. 3:** alinear el titulo de `sec:obj1` y la l. 13 ("valida") con el nuevo titulo del Obj 1; la l. 253 atribuye al "control de nivel" los 7 de 57 que la l. 52 atribuye a la discordancia de nivel; el control tambien excluyo a un paciente por borde del campo de vision, de grupo no dicho: revisar; decidir "componentes" o "medidas" para SAP en todo el documento.

## 2026-09-29 (2) — `/ciclo-redaccion capitulo3`: TOPE en r05, con decisiones pendientes

- **Hecho:** cap. 3 redactado (r00) y corregido en r01 a r05. El lint PASA y compila (57 pag.). Los PDF por etapa estan en `redaccion/.build/etapas/`. Revisores alta/media: r01 8/35 -> r05 1/11. La bitacora tiene 42 patrones (21 VIGENTES, 21 ERRADICADOS).
- **Siguiente:** que la autora decida los 16 puntos de #127 (22 `\GAPDEC` en el cap. 3). Despues, `/ciclo-redaccion capitulo3` para una ronda mas, o seguir con `capitulo4` / `capitulo1`.
- **Pendientes nuevos:** #127, sobre todo el punto 13 (envolvente implementada distinta de D-O2.3; puede obligar a volver a correr E9-TS, E12 y E13) y el 14 (regiones de rayas contra $B_\delta$). Validar las decisiones de redaccion de `BITACORA.md` §2.

## 2026-09-29 — Arranque del documento de entrega (`overleaf/`)

- **Hecho:** ciclo de redaccion montado: `overleaf/CLAUDE.md`, `redaccion/` (RUBRICA, ESTILO, MAPA, muestras), 4 agentes, skill `/ciclo-redaccion`, `scripts/lint_redaccion.py` (+8 tests) y macros `\GAPLIT/\GAPDATO/\GAPDEC`. Capitulos reordenados segun la guia; `overleaf/referencias.bib` ahora sale de `build_refs.py`. Compila (25 pag.).
- **Ajuste (misma fecha):** modelo de prosa = la guia del departamento (`ESTILO.md` §1.1); compilacion obligatoria al cerrar cada etapa, con PDF en `redaccion/.build/etapas/` y registro en `redaccion/BITACORA.md`.
- **Siguiente:** `/ciclo-redaccion capitulo3` (las muestras de la autora ya son opcionales) (el bloque con mas fuente en `tesis/main.tex`); la introduccion va despues.
- **Pendientes nuevos:** #126 (titulo, introduccion desfasada, ORCID/asesor en portada). Siguen #123, #124, #125 del Obj 2.

## PUNTO DE RETOMA 2026-09-23 (2) — TRASPASO. Leer esto y nada mas para arrancar

> Escrito para una sesion nueva **sin historial**. Sustituye a los bloques del 2026-09-22 y al primero
> del 2026-09-23, que quedan abajo como historico.

### En una frase

El **Objetivo 2 esta terminado y escrito en `main.tex`**; lo que queda son **dos revisiones humanas**
(#123 y #125), **una decision de redaccion** (#124), y despues el **Objetivo 3**, que es el riesgo real
porque **nunca ha generado una muestra** (#116).

### Orden de lectura al arrancar

1. Este bloque.
2. `experiments/objetivo2/EXPERIMENTOS.md` — que artefacto esta vigente, quien lo produjo, que lo
   consume. **Un CSV vacio no significa que nadie respondio**; puede ser una planilla superada.
3. `docs/04-implicancias.md`, solo **#123, #124 y #125**, que son las abiertas del Objetivo 2.
4. Correr `python experiments/objetivo2/verificar_coherencia.py` (**94 comprobaciones**). Si falla
   alguna, el codigo y `main.tex` han dejado de decir lo mismo y eso se arregla **antes** de tocar nada.

### El resultado del Objetivo 2, ya en `main.tex`

Corrida **52175** (Khipu), preinscrita en `preinscripcion_muestreador.md`, sin errores. Fila
*Surgical Admissibility* marcada **executed**:

| Cohorte | n poses | g0 / g1 / g2 / g3 (%) | W1 navegado | W1 convencional |
|---|---|---|---|---|
| Primaria, 72 casos | 3600 | 51.5 / 31.4 / 11.1 / 6.0 | **0.206** | 0.230 |
| Sensibilidad, 49 casos | 2450 | 54.9 / 30.4 / 9.9 / 4.8 | **0.186** | 0.299 |

`main.tex`: 0 errores, 0 citas indefinidas, 8 paginas.

**Cerradas esta semana:** #118 (SAP se mide con 7.0 mm, el calibre del benchmark) · #119 (los FOV
cortados no estan en la cohorte) · #120 (el tramo que SAP califica es el implante, de longitud fija) ·
#121 (el segundo corredor **no es S2**: 13 S2 / 4 S3 / 1 S4 en 18 casos) · #122 (en 15 de 72 el corredor
no admite el calibre; W1 estratificado, **post hoc declarado**).

### Lo que queda, con su estado exacto

| # | Que | Estado | Donde |
|---|---|---|---|
| **#123** | 16 casos del **recorte de 6 mm**. Condicion de reapertura escrita por la autora y nunca evaluada; **todas** las cifras del Obj 2 salen de ese recorte | autora **0/16**, agente **16/16** | `e9ts_revision_laminas_autora.csv`, `_agente.csv`, instrucciones en `e9ts_revision_laminas.md` |
| **#125** | **Cribado de fractura**, 30 casos **ciegos** (15 estrechos + 15 control) | **0/30** | `r3_fractura_revisor.csv` + `.md`. El reparto esta en `r3_fractura_grupos.csv` y **NO se entrega al revisor** |
| **#124** | Decidir si la frase del acuerdo **61 de 61** entra en `main.tex` | decision | recomendacion: si, en una frase, con los dos limites declarados |

**Revisiones ya completas:** S1 sobre laminas (**61/61**, acuerdo total con el revisor clinico ORL) y
nivel del segundo corredor (**18/18**).

### El subagente ya corrio, y su resultado tiene un pero

`.claude/agents/revisor-laminas-corredor.md` reviso los 16 casos de #123: **14 `ok`, 2 `fallo_3mm`,
0 `fallo_6mm`, 0 `dudoso`**. Los dos fallos son `CLINIC_0076` y `CLINIC_0022`, y en los dos **la region
perdida lo es en el recorte de 3 mm**, no en el de 6 mm.

**Cero `fallo_6mm` apunta a que la decision de 2026-09-14 (4) no se reabre. Pero NO la cierra:**

- Es una **propuesta**, no la referencia. La revision de la autora sigue en 0/16 y es la que vale.
- **Cero `dudoso` en 16 casos visuales es sospechoso.** Las instrucciones invitaban explicitamente a
  usarlo y el agente no lo uso ni una vez. Un revisor que nunca duda sobre cortes sueltos esta siendo
  optimista, no preciso.
- `ok` significa *"no veo error en estos cortes"*, no *"no hay error"*: las laminas **no demuestran
  ausencia** (#19, #21).

### Por que #125 es la mas seria de las tres

`CLINIC_0060` tiene **fractura confirmada** —por un medico recien licenciado, **sin especialidad**, y
asi debe citarse— y un corredor de **6.2 mm**: **esta dentro de los 15 estrechos de #122**, que
`main.tex` presenta hoy como variabilidad anatomica. `CLINIC_0022` tiene 4.7 mm y tambien esta.
`reilly2003effect`, ya citado en la tesis, midio que una fractura desplazada reduce el area para
tornillos en S1 **entre 36% y 90%**. Si la fractura se concentra en los estrechos, parte de lo que la
tesis llama anatomia es patologia no detectada. Por eso el cribado es **ciego y con grupo de control**:
sin el, no se distingue concentracion de tasa de fondo.

### Estado del repositorio

**Hay trabajo sin commitear**, incluido el resultado del Objetivo 2, cuatro ediciones de `main.tex`,
ocho implicancias, cuatro planillas de revision, `EXPERIMENTOS.md` y el subagente. **Commitear es lo
primero.** Comprobar con `git status --short`.

### Siguiente, en orden

1. **Commitear.**
2. Las dos revisiones humanas: **#123** (la autora, para contrastar con el agente) y **#125** (mejor si
   la contesta alguien con especialidad; con un lector general sigue valiendo, pero hay que escribirlo asi).
3. Decidir **#124**.
4. **Objetivo 3.** Es lo que queda del alcance completo: nunca se ha generado una muestra sintetica
   (#116) y sigue en pie el compromiso del brazo TOST (#90), que la autora decidio mantener como meta.

### Aviso de metodo, ganado a golpes esta semana

El asistente afirmo **cinco veces** algo por delante de la evidencia: dio por aplicado un cambio que no
ejecuto (dos veces), infirio de un CSV vacio que un revisor no habia respondido, generalizo desde una
sola imagen y cito un documento que solo habia leido a medias. Las cinco las detecto la autora o una
verificacion posterior. **Pedir la cifra medida, no la impresion.** Los hallazgos reales de la semana
—el calibre de 7.0 mm, el tramo del implante, que el segundo corredor no es S2— salieron todos de un
control que podia fallar, no de razonar sobre el codigo.

## PUNTO DE RETOMA 2026-09-22 (4) — EL OBJETIVO 2 TIENE SU PRIMER RESULTADO (job 52175)

> Sustituye a los tres bloques anteriores de este mismo dia, que quedan abajo como historico.

**El alcance minimo viable ya no esta sin ejecutar.** Corrida 52175 en Khipu, las dos cohortes, sin
errores. Salidas en `experiments/objetivo2/`: `e13_sap.md`, `e13_poses.csv`, `e13_sap_g3.md`,
`e13_poses_g3.csv`.

### Resultado preinscrito (SAP, calibre 7.0 mm)

| Cohorte | n poses | g0 / g1 / g2 / g3 (%) | W1 navegado | W1 convencional |
|---|---|---|---|---|
| Primaria, 72 casos | 3600 | 51.5 / 31.4 / 11.1 / 6.0 | **0.206** | 0.230 |
| Sensibilidad, 49 casos | 2450 | 54.9 / 30.4 / 9.9 / 4.8 | **0.186** | 0.299 |

Integridad: **72 y 49** casos, **0** poses sin grado, todos los estados `ok`. Referencias de Zwingmann:
navegado 69/15/8/8, convencional 40/37/11.5/11.5. W1 en grados, maximo 3.0.

### #122 NUEVA, y es lo importante de la corrida

El control de pose sin perturbar reporto **16 de 72 casos "fallando"**. **No era un fallo de la
metrica: el control estaba mal especificado** —usaba 7.0 mm en vez de `D_TS_max`, que es la unica
identidad garantizada por construccion—. Los 16 coinciden con los que tienen **`D_TS_max < 7.0 mm`**:
en esas pelvis el corredor no admite el tornillo del benchmark y **el eje ideal ya perfora**. Es
anatomia, no error.

**Las cifras de la tabla de arriba son validas y no cambian**: nada se excluyo. La frase del `.md` que
decia "sus cifras no se usan" era falsa —`resumen()` calculaba sobre todas las poses— y excluirlos
habria estado mal, porque Zwingmann tampoco excluyo a sus pacientes estrechos.

**Estratificado (post hoc declarado, `e13b_estratificado.md`):**

| estrato | g0 (%) | W1 navegado | W1 convencional |
|---|---|---|---|
| `D_TS >= 7.0` (57 de 72) | **64.2** | **0.183** | 0.482 |
| `D_TS < 7.0` (15 de 72) | 3.3 | 1.122 | 0.727 |

En corredores viables el muestreador da **64.2%** de grado 0 frente al **69%** del brazo navegado, y la
cohorte de sensibilidad lo reproduce (**64.6%**, W1 0.175). **La cifra agregada es una mezcla de dos
poblaciones**, y su parecido con el brazo convencional es en parte efecto de esa mezcla.

### Aplicado en este turno

Control de `procesar()` corregido a `D_TS_max`; `corredor_estrecho` y brecha del eje a 7.0 mm anadidos
como dato reportado; `resumen()` ya no afirma que excluye casos; nota de correccion al inicio de los dos
`.md` de la corrida; `python -u` en el `.sbatch`; `verificar_coherencia.py` en **41/41**.

### #122 CERRADA y ESCRITA en `main.tex` (2026-09-22, por peticion explicita)

La autora adopto **(a)+(b)**. La fila *Surgical Admissibility* pasa a **executed** con la cifra
preinscrita de las dos cohortes, y un parrafo nuevo trae la estratificacion **declarada post hoc**, la
fraccion de corredores estrechos y el motivo por el que **no** se restringe la cohorte. Compila: 0
errores, 0 citas indefinidas, 8 paginas.

`verificar_coherencia.py` **recomputa desde los CSV todas las cifras que `main.tex` afirma** —las dos
distribuciones, los seis Wasserstein-1, y los recuentos de casos viables y estrechos— y comprueba que
el texto las declare. **78/78 comprobaciones pasan.**

### Siguiente

1. **#121 (S2).** Lo que falta es concreto y pequeno: `buscar()` (`e9ts_corredor.py:195-201`) guarda
   `mejor_por_z[iz] = mejor_z.get('D_TS', 0.0)`, es decir **solo el diametro**, y tira el `c` y el `u`
   de cada altura; la fila de perfil (linea 305) escribe solo `z_rel_S1_mm` y `D_TS_mejor_mm`. Hay que
   conservar el eje por altura y anadir seis columnas a `CAMPOS_PERFIL`. Coste de la corrida:
   **E9-TS entero fueron 1.34 h de CPU** sobre 152 casos y todas las variantes; los 72 con una sola
   variante son minutos.
   **Pero antes hay que resolver una cosa:** el pico inferior se identifica por la **forma del perfil
   de diametro**, no por una etiqueta. TotalSegmentator `total` etiqueta `vertebrae_S1` y el sacro
   entero, **no S2**. En la cohorte el pico inferior esta entre **-45.6 y -24.0 mm** de S1 (p10-p90) y
   existe en **69 de 72** casos. Llamarlo "S2" sin verificarlo seria un supuesto silencioso.
2. Objetivo 3, con el minimo viable ya defendible.

## PUNTO DE RETOMA 2026-09-22 (3) — TODO LISTO PARA KHIPU; LA CORRIDA NO SE PUEDE HACER EN LOCAL

> Sustituye a los dos bloques anteriores de este mismo dia, que quedan abajo como historico.

### Lo que BLOQUEA, y no es una decision

**E13 sobre la cohorte no se puede correr en esta maquina.** Verificado: los **72/72** CT de la cohorte
estan en disco, pero **0/72** tienen mascaras de TotalSegmentator; en local solo existen las de los dos
casos piloto (`data/derivados/ts_piloto/`). `totalsegmentator` no esta instalado y `torch` es **2.9.1+cpu**
sin CUDA. Las mascaras de la cohorte viven en Khipu (`~/metalsynth/data/ts_total`, 358 casos).

**Para lanzarlo** (todo lo demas ya esta hecho):

```
scp experiments/objetivo2/{e13_muestreo_sap.py,e13_muestreo_sap.sbatch,e12_sap_control.py}     kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
scp src/muestreador/{sap.py,muestreo.py} kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
# en Khipu:  sed -i 's/
$//' ~/metalsynth/qc/*.sbatch  &&  sbatch e13_muestreo_sap.sbatch
```

El `.sbatch` corre **las dos cohortes en un solo job**: primaria (72, grupos 2 y 3) y sensibilidad
(49, grupo 3). Coste medido: **15.7 s/caso**, unos **32 min** de reloj para las dos. Solo CPU.
Salidas: `e13_poses.csv` / `e13_sap.md` y `e13_poses_g3.csv` / `e13_sap_g3.md`.

### Lo que SI se hizo en este turno

- **Semilla por caso** (`muestreo.rng_de_caso`, blake2b del nombre + semilla global). Antes era un
  generador global que avanzaba caso a caso: el mismo paciente habria recibido poses distintas en la
  corrida de 72 y en la de 49, y la diferencia entre ambas cifras habria mezclado efecto de cohorte con
  ruido de muestreo. Corregido **antes** de cualquier corrida y declarado en la preinscripcion.
- **`main.tex`, cuatro cambios** (regla 4: pedidos en el turno). Tres eran **contradicciones con D-O2.1**
  que quedaban en el texto: el Problem Statement decia *"sample from the measured ordinal distribution
  of clinical malpositions"*, los Objetivos *"emulating the two measured ordinal distributions"* y la
  tabla *"Wasserstein-1 shows generated placements approaching..."*. Las tres describian el muestreador
  **calibrado contra el benchmark**, que es justo la opcion (b) rechazada. Reescritas. El cuarto cambio
  es un parrafo nuevo, **Pre-registration of the placement sampler**, tras la tabla de Expected Results.
  Compila: **0 errores, 0 citas indefinidas, 8 paginas**.
- **`verificar_coherencia.py`: 39 comprobaciones, 39 pasan.**

### #121 (S2): la salida es mas barata de lo que decia la entrada original

Verificado en `e9ts_corredor.py:167-200`: **`buscar()` ya calcula el eje a cada altura** (`mejor_z` con
`c` y `u`) y **lo tira**; a `e9ts_perfiles.csv` solo se escribe el diametro. El barrido ya cubre S2 —en
la cohorte el pico inferior esta a **-30 mm** de S1, diametro mediano **7.3 mm**, presente en **69 de
72** casos— y **no hace falta ningun landmark nuevo**. Cerrar #121 = anadir seis columnas a la salida de
perfiles, relanzar E9-TS sobre los 72, preinscribir S2 aparte y correrlo sin W1. Recomendacion: hacerlo,
pero **despues** de la corrida principal.

### Siguiente

1. Lanzar `e13_muestreo_sap.sbatch` en Khipu. Produce el primer resultado propio del Objetivo 2.
2. Con las cifras en mano, escribir Resultados. **No hay nada escrito con numeros inventados.**
3. Decidir #121.

## PUNTO DE RETOMA 2026-09-22 (2) — EL OBJETIVO 2 CORRE DE PUNTA A PUNTA. Leer esto primero

> Sustituye al bloque "SAP EXISTE Y ESTA CONTROLADA" de este mismo dia, que queda abajo como historico.

- **Ultimo paso completado:** #120 resuelta por la opcion **(b)** y aplicada; **preinscripcion escrita y
  congelada** (`experiments/objetivo2/preinscripcion_muestreador.md`); **muestreador implementado**
  (`src/muestreador/muestreo.py`); **camino completo verificado de punta a punta** sobre los dos casos
  piloto (E13). `main.tex` **actualizado por orden explicita de la autora** (regla 4).
- **Lo que existe ahora:** `sap.py` (metrica), `muestreo.py` (poses), `e12_sap_control.py` (seis
  controles), `e13_muestreo_sap.py` (cohorte + W1) y `verificar_coherencia.py` (**34 comprobaciones,
  34 pasan**), que falla si codigo, preinscripcion, controles y `main.tex` dejan de decir lo mismo.
- **Definicion final de la brecha, y lo que costo llegar:** el tramo que SAP califica es el **propio
  implante**, de longitud fija igual a la del corredor del caso, centrado en la pose **anclada al punto
  medio del corredor** y recortado 8 mm por extremo. Dos definiciones anteriores cayeron: "del primer al
  ultimo cruce con el hueso" (la tumbo C6: 10.38 mm sobre el eje del corredor, que debe dar 0) y la
  misma cortando en huecos de 40 mm (la tumbo C5: brecha 0.0 a 20 grados de inclinacion, porque el tramo
  se encoge con la pose). **Los controles hicieron todo el trabajo.**
- **`main.tex`:** tres geometrias en vez de dos, con la frase de los tornillos de 7.0 mm de Zwingmann;
  definicion operativa de SAP en la fila *Surgical Admissibility* (protrusion radial, recorte de 8 mm,
  grado 3 en vez de descarte, resolucion 0.083 mm, envolvente de hueso y no de cortical); y los casos de
  FOV truncado declarados fuera de la cohorte del muestreador. **Compila: 0 errores, 0 citas
  indefinidas, 8 paginas.**
- **#121 NUEVA y ABIERTA:** **S2 no tiene eje de corredor medido.** `e9ts_corredor.csv` guarda un solo
  eje por caso y es el de S1; de S2 solo hay posicion y diametro del pico inferior, sin direccion. La
  mitad de D-O2.5 no es ejecutable. **No bloquea el resultado principal** (el benchmark ordinal ya era
  solo S1). Recomendacion: (b), dejar S2 fuera del muestreo y reportarlo con lo ya medido.
- **Siguiente, y es una sola cosa:** correr **E13 sobre los 72 casos en Khipu**
  (`python e13_muestreo_sap.py --ts-dir ~/metalsynth/data/ts_total --ct-dir ~/metalsynth/data/ts_input`).
  Eso produce el primer resultado propio del Objetivo 2. Nada mas hay que decidir para lanzarlo.
- **Lo unico que la autora tiene que decidir antes o despues:** #121 (S2).

## PUNTO DE RETOMA 2026-09-22 — SAP EXISTE Y ESTA CONTROLADA. Leer esto primero

> Sustituye como punto de entrada al bloque del 2026-09-21 (cierre 3), que queda mas abajo como historico.
> Lo que ese bloque llama "agenda de decisiones del Objetivo 2" **ya esta resuelto**: las siete decisiones
> D-O2.1 a D-O2.7 estan tomadas y escritas en `docs/01-decisiones.md` (entrada del 2026-09-22).

- **Ultimo paso completado:** las siete decisiones del Objetivo 2, aplicadas a `00-tesis.md` (tres
  geometrias en vez de dos; pendiente de FOV cerrado), y **la primera implementacion de SAP**.
  `src/muestreador/` deja de estar vacio: `sap.py` calcula los tres componentes (grado de brecha de
  cuatro niveles, fraccion por zona de densidad, viabilidad de corredor) y el Wasserstein-1 ordinal
  contra las dos distribuciones de `zwingmann2009navigated`. #118 y #119 quedan CERRADAS.
- **Controles, en `experiments/objetivo2/e12_sap_control.md`:** C1 fantasma de geometria conocida, error
  maximo **0.083 mm** (esa es la resolucion de SAP y va declarada junto a cualquier cifra de brecha);
  C2 identidad con el corredor, **0.0 exacto** en el fantasma y en los dos casos piloto reales;
  C3 monotonia en diametro; C4 la envolvente reconstruida reproduce el `D_TS_max` de E9-TS
  (diferencias 0.012 y 0.042 mm, dentro del redondeo del CSV); C5 discriminacion por inclinacion.
  **Los controles atraparon tres errores reales** durante la implementacion, dos de convencion de
  distancia y uno de diseno (#120).
- **#120 NUEVA y es lo siguiente que hay que decidir:** `e9_corredor.tramo` exige salida a tejido blando
  y lateralidad de EIPS, porque se escribio para **buscar corredores**. SAP **califica poses**, y a 5-8
  grados de inclinacion devuelve "no evaluable" en vez de un grado. Descartar esas poses sesgaria el W1
  a la baja, que es justo lo que D-O2.1 existe para evitar. Mitigado a medias:
  `distribucion_grados` **lanza por defecto** si hay poses sin grado, asi que el descarte silencioso es
  imposible. La eleccion de fondo (contarlas grado 3, separar el calificador del buscador, o categoria
  aparte) es **de la autora**.
- **Siguiente:** decidir #120; luego el muestreador en `src/muestreador/`, perturbando el eje de
  `e9ts_corredor.csv` con una distribucion **preinscrita** (D-O2.1, D-O2.7); luego correr SAP sobre la
  cohorte de 72 y calcular el W1.
- **`tesis/main.tex` NO se toco** (regla 4). La tercera geometria y las cifras de SAP estan en `docs/`,
  pendientes de que la autora decida llevarlas al documento.

## PUNTO DE RETOMA 2026-09-21 (cierre 3) — ARRANCA EL OBJETIVO 2. Leer esto primero

> Escrito para una sesion nueva sin historial. Sustituye como punto de entrada al bloque del 2026-09-20.
> **Ojo:** la *Actualizacion (6)* (ronda de 8 papers: Jin, Wu, Konz, Glover, Selles 2022, Kadkhodaie,
> Chen, Ferrero) la escribio otra sesion en paralelo el mismo dia. Es posterior y **sigue vigente**: no
> abre implicancia numerada nueva, actualiza #56, #57/#60, #73 y #106, y deja dicho que **esas ocho fuentes
> aun no estan en `refs.bib`** (sigue en 110 entradas). De ella importa para el Objetivo 3, no para el 2.
>
> Lo del Objetivo 3 esta al dia y **no bloquea**: el piloto se analizo, #89 esta medida y el modelo entrenado
> existe. **El trabajo ahora es el Objetivo 2.**

### Decision de plazo, tomada el 2026-09-21 por la autora

**Se apunta a llegar al Objetivo 3 en ~5 semanas. NO se corta nada todavia.** `main.tex` **no se toca**:
el brazo de equivalencia (TOST frente al protocolo fisico de `peters2025hybrid`) **se mantiene como meta**.
El recorte propuesto por el asistente queda como **contingencia declarada**, registrada en la
**ACTUALIZACION de #90**, y solo se aplica si el plazo lo obliga. **No lo apliques por tu cuenta.**

### Lo que el Objetivo 2 YA tiene medido (no rehacer nada de esto)

| Insumo | Donde | Que trae |
|---|---|---|
| Corredor por caso | `experiments/objetivo2/e9ts_corredor.csv` | **2 352 filas, 152 casos, 0 errores**. Eje del corredor por caso: centro `c_x,c_y,c_z`, direccion `u_x,u_y,u_z`, `ang_coronal_crestas_deg`, `ang_axial_eips_deg`, `D_TS_max_mm`, `L_TS_mejor_mm`, y banderas `viable_TS_*` por combinacion `(d, c)` |
| Resumen | `experiments/objetivo2/e9ts_resumen.md` | Cohorte Obj 2 (72 casos): `D` mediana **9.5 mm**, **40.3%** pasa 10 mm, **65.3%** con `d=6.5, c=1`, **54.2%** con `d=7.3, c=1`, **23.6%** con `d=8.0, c=2` |
| Landmarks | `r1_landmarks.csv`, `r1_auditoria_s1_clinico.csv` | Marco de Kaiser computable con S1 confirmado por revisor clinico en **49 de 65**; **30** sin contaminacion |
| Densidad S1 | `e9b_densidad_s1.csv` | Insumo de la fraccion por zona de densidad de SAP |
| Geometria del tornillo | E8 + E11 (`e11_perfil_axial.md`) | Cuerpo **~4.91 mm** (`d_centro` mediana), tres vias coincidentes dentro de un cuarto de voxel |

**El muestreador NO se construye desde cero: se construye perturbando un eje ya medido.**

### Lo que NO existe (es todo el trabajo)

- **`src/muestreador/` esta VACIO.** 0 archivos.
- **SAP no tiene una sola linea** en el repositorio. Es, segun `00-tesis.md`, la **unica metrica que esta
  tesis introduce**. Ver **#116**.

### SAP, tal como ya esta comprometida en `main.tex` (no reinventarla)

`main.tex`, tabla de Expected Results, fila *Surgical Admissibility*:

- **Grado de brecha cortical de cuatro niveles** (`smith2006iliosacral`), con **limites fijados por
  convencion**: grado **0** sin perforacion, **1** en `(0,2)`, **2** en `[2,4]`, **3** en `(4,inf)` mm.
- Mas **fraccion por zona de densidad** y **viabilidad de corredor** (`mclaren2021corridor`) en el marco de
  `kaiser2014dysmorphism`.
- **Comparacion: distancia de Wasserstein-1** contra las **dos** distribuciones ordinales de
  `zwingmann2009navigated`, condicionadas por tecnica y **solo en S1**. S2 se reporta descriptivamente.

**Las dos distribuciones de referencia** (de la ficha, con frase original verificada):
- **Navegado: 69 / 15 / 8 / 8** (grados 0/1/2/3), 26 tornillos en 24 pacientes.
- **Convencional: 40 / 37 / 11.5 / 11.5**, 35 tornillos en 32 pacientes.
- Umbrales del paper: *"Grade 0, no perforation; Grade 1, perforation less than 2 mm"*, *"Grade 2,
  perforation between 2 and 4 mm; and Grade 3, perforation greater than 4 mm"* (Materials and Methods,
  p. 1835). Los limites exactos de `main.tex` son **convencion propia** porque el paper no cierra los bordes.
- **`zwingmann2010percutaneous` NO entra al benchmark** (#113): publica un grado 4 sin definir y puede
  solaparse con la cohorte de 2009.

### Agenda de decisiones del Objetivo 2 — esto es lo que hay que resolver con la autora

Ninguna esta decidida. Van en este orden porque cada una condiciona la siguiente.

1. **D-O2.1 — Que se muestrea, y como se evita la circularidad. ES LA DECISION CENTRAL.**
   El prior de `zwingmann2009navigated` es **ordinal** (cuatro grados), no una distribucion de poses. El
   muestreador produce **poses 3D continuas**. Hay que decidir el sentido de la flecha:
   - (a) muestrear poses desde una distribucion geometrica declarada, **medir** la distribucion de grados
     que resulta, y **compararla** con Zwingmann via Wasserstein-1; o
   - (b) calibrar el muestreador para **reproducir** las proporciones de Zwingmann.
   **(b) hace la comparacion circular** —se compara contra lo que se uso para ajustar— y destruiria el
   unico resultado propio de la tesis. **Recomendacion del asistente: (a), y preinscribir la distribucion
   geometrica antes de medir nada.** Si se elige (b), la metrica deja de ser validacion y pasa a ser
   verificacion de ajuste, y hay que decirlo asi.
2. **D-O2.2 — Cohorte.** 72 casos (grupos 2 y 3 con QC de nivel) o 49 (grupo 3). Y que se hace con los
   **7 con FOV cortado** de R1, que `00-tesis.md` declara **sin decidir** desde el 2026-09-11.
3. **D-O2.3 — Como se mide la brecha cortical en milimetros.** Es lo que convierte SAP en algo calculable.
   Necesita una definicion operativa de superficie cortical sobre la segmentacion de TotalSegmentator, y
   una regla para medir cuanto sobresale el cilindro. **Sin esto no hay grado y no hay SAP.**
4. **D-O2.4 — Que diametro entra en la brecha.** `00-tesis.md` ya separa **dos geometrias**: envolvente
   **6.5-8.0 mm** para viabilidad de corredor (#31) y cilindro **~4.9 mm** para sintesis (D3). Para SAP hay
   que elegir explicitamente cual, y no mezclarlas.
5. **D-O2.5 — S1 y S2.** El benchmark ordinal es **solo S1** (#12, #28). Decidir si el muestreador propone
   pose en S2 y se reporta descriptivamente, o si S2 queda fuera del muestreo.
6. **D-O2.6 — Fraccion por zona de densidad.** Existe `e9b_densidad_s1.csv`; falta definir como entra en SAP
   (componente de la metrica, o covariable que condiciona el muestreo).
7. **D-O2.7 — Preinscripcion.** SAP y la distribucion de poses se congelan **antes** de comparar contra
   Zwingmann, igual que se hizo con `diseno_A.md` y con el criterio de inclusion R1-R3.

### Trampas conocidas, ganadas a golpes en este proyecto

- **No reintroducir fenotipos sacros ni el score de dismorfismo.** FUERA POR COMPLETO desde el 2026-09-08
  (punto 8 de `Fuera de alcance`, #27). El muestreador **mide el corredor en cada volumen**.
- **No usar el "31-60%" ni el "2-15%"** como rango de malposicion: los dos estan RETIRADOS (#12, #25).
- **No citar `zwingmann2010`** en el benchmark (#113).
- **Toda capa o metrica derivada necesita una comprobacion que pueda fallar.** En las superficies 3D la util
  resulto ser **contar vertices**, no mirar la figura. Cuatro fallos silenciosos de este proyecto se
  detectaron **mirando la salida**, no con controles.
- **`d_max` de E11 (8.10 mm) es un maximo sobre tramos, sesgado al alza, y NO es un diametro de cabeza medido.**

### Estado del Objetivo 3, para no volver a abrirlo sin motivo

Piloto **52074** analizado y valido. **#89 medida** (0.0923 s/paso, 0.77 h por 30 000 pasos, 3.35 GB) y lista
para cerrar, no aplicada. Abiertas: **#114** (instrumentacion de `s_por_paso`), **#115** (7% de GPU),
**#117** (el muestreador **no** es RePaint ni LeFusion; corrige la atribucion de Metodos y guarda el
remuestreo como mitigacion de #112), **#106**, **#112**. Sin conectar: bucle de validacion y E-A1..E-A4.
**Nunca se ha generado una muestra sintetica** (#116).

### Actualizacion 2026-09-21 (7) — las 8 fuentes de la ronda (6), dadas de alta: `refs.bib` pasa a 118

- **Ultimo paso completado:** normalizacion bibliografica de las ocho fuentes que la ronda (6) dejo leidas
  pero sin alta. Se escribieron los ocho `refs/clean/*.bib` desde su raw, se anadieron las ocho filas a
  `refs/MAPEO.md` y se regenero `refs.bib` con `python scripts/build_refs.py`: **110 -> 118 entradas**.
  Compilacion verificada: **0 errores, 0 citas indefinidas, 7 paginas**.
- **Ninguna esta citada en `main.tex`** (regla 4): entran como **disponibles**, no como usadas.
- **Fichas releidas y contrastadas con la ronda (6):** coinciden. **No se abrio implicancia numerada nueva**
  y no se duplico nada; la ronda (6) ya habia ajustado #56, #57/#60, #73 y #106. Se le hicieron dos
  correcciones de hecho: (i) la linea que decia que no hubo alta en `refs.bib` quedo tachada y corregida;
  (ii) se anadio que **`konz2024anatomicallycontrollable` apoya la #106**, por ser el precedente publicado
  mas cercano a lo implementado (difusion en espacio de imagen, U-Net, mascara concatenada por paso,
  `T = 1000`, DDIM), con sus limites en la misma frase: normaliza a `[0, 255]` y no a HU, y genera el corte
  completo desde ruido.
- **Pendientes que arrastra la ronda (6):** el reclamo de novedad de `main.tex` hay que estrecharlo (#56) —
  no son novedad ni la insercion sintetica, ni la U-Net de difusion con mascara concatenada, ni tocar fuera
  de la mascara; lo que sobrevive es **metal rigido + multi-ventana + banda exterior explicita + copia exacta
  fuera de `G`**. Y E-A4 debe separar **streaking** de **delineacion cortical** (#73, Selles 2022).
  **Nada de esto se aplico a `main.tex`** (reglas 4 y 14).
- **Siguiente:** sin cambios — arranca el **Objetivo 2** por **D-O2.1** (ver el punto de retoma del tope).

### Actualizacion 2026-09-21 (6) — ocho papers pendientes leidos; novedad y evaluacion mejor delimitadas

- **Ultimo paso completado:** `lector-papers` leyo a fondo `chen2015lesion`,
  `ferrero2017technicalnote`, `glover1980nonlinear`, `jin2021freetumor`,
  `kadkhodaie2024generalization`, `konz2024anatomicallycontrollable`, `selles2022mar` y
  `wu2025freetumor`. Las ocho fichas, `_index.md` y los estados de `_candidatos.md` quedaron actualizados;
  todas se proponen N2. `refs/clean/`, `refs/MAPEO.md` y `refs.bib` **no se tocaron**: el encargo no incluyo
  normalizacion bibliografica y `refs.bib` conserva 110 entradas.
- **Impacto:** Jin/Wu/Konz obligan a centrar la diferencia en metal + multi-ventana + `B_delta` + copia
  exterior, no en insercion, U-Net o mascara concatenada. Glover refuerza que el artefacto excede `M` pero
  no calibra 12 mm. Selles muestra que menos streaking puede coexistir con peor delineacion cortical, por
  lo que E-A4 debe separar ambos items. Kadkhodaie no demuestra superioridad U-Net/DiT y #106 no cambia.
- **Implicancias:** la ronda actualiza #56, #57/#60, #73 y #106; **no abre una implicancia numerada nueva**,
  no cambia baseline, arquitectura, alcance ni preinscripcion. E-A3 debe presentarse como preservacion por
  construccion, no como fidelidad fisica global. No surgio snowballing que superara el filtro vigente.
- **Siguiente:** la autora debe resolver la priorizacion abierta por #116. Mientras no la cambie, el paso
  operativo previamente vigente sigue siendo conectar `a5_manifiesto_val.csv` en `entrenar.py`, seguido de
  E-A1..E-A4 y Metodos. Si estas ocho fuentes se van a citar, falta su alta en `refs/clean/`/`refs.bib`.

### Actualizacion 2026-09-21 (5) — PILOTO A2 ANALIZADO: corrida valida, #89 medida, dos implicancias nuevas

- **Ultimo paso completado:** se bajo y analizo el job **52074**, el primer entrenamiento del proyecto.
  Salidas en `experiments/objetivo3/outputs/a2/`. **La corrida es VALIDA:** `parches: 17149`, `casos: 47`
  (el conjunto preinscrito, no el 21 754 / 72), los tres controles pasan y aparece el aviso
  `corrida NO preinscrita`. `rc=0`, 49 s de reloj.
- **#89 queda MEDIDA y lista para cerrar** (no aplicada a `main.tex`, reglas 4 y 14): **0.0923 s/paso** en
  regimen, **0.77 h por 30 000 pasos**, **`gb_max` 3.35 GB** de 48. Los umbrales de relanzamiento
  (~40 GB, ~20 h) no se acercan: **no hay que bajar `--base` ni `--lote`**.
- **#114 NUEVA:** la columna `s_por_paso` de `curva.csv` es un **promedio acumulado**, no el ritmo de un
  tramo (`entrenar.py:144`, `t0` nunca se reinicia), y el titular `LISTO` incluye la escritura de
  `ckpt.pt`. **La instruccion de `KHIPU.md` —"tomar el ultimo tramo"— no es ejecutable leyendo la ultima
  fila.** La cifra buena (0.0923) sale de diferenciar la columna. El sesgo es conservador, asi que la
  decision no cambia; la cifra publicable, si.
- **#115 NUEVA:** el renderizador usa el **7% de la GPU** y ~1 h de las 24 h de cola. Abre que hacer con la
  holgura (lote, base, pasos, banda). **Recomendacion: no agrandar nada todavia** — el piloto midio coste,
  no calidad, y E-A1..E-A4 sigue sin una linea de codigo.
- **Siguiente:** Tarea 3.1 del encargo, **conectar el bucle de validacion en `entrenar.py`**
  (`a5_manifiesto_val.csv` existe y nada lo consume); despues E-A1..E-A4 y Metodos. Tarea 2 (15 fichas sin
  procesar, prioridad `lugmayr2022repaint`) sigue pendiente.
- **Pendiente que surgio:** hay **5 raw nuevos sin procesar** en `refs/raw/` subidos por la autora
  (`chen2015lesion`, `ferrero2017technicalnote`, `kadkhodaie2024generalization`,
  `konz2024anatomicallycontrollable`, `selles2022mar`). No se tocaron: el alta empieza por decision de la
  autora (regla 9).

### Actualizacion 2026-09-21 (4) — cinco candidatos prioritarios leidos y normalizados

- **Ultimo paso completado:** `lector-papers` leyo `selles2023ai`, `lugmayr2022repaint`,
  `zwingmann2010percutaneous`, `choi2025mar` y `park2015ct`. Las cinco fichas, sus entradas `refs/clean/`,
  el mapeo y el indice quedaron actualizados; `refs.bib` pasa de 105 a **110 entradas**.
- **Impacto:** Selles y Park refuerzan que el artefacto excede `M`, pero ninguno calibra los 12 mm de
  `B_delta` (#57). Zwingmann 2010 publica un grado 4 sin definir y puede solaparse con la cohorte de 2009;
  por eso no entra al benchmark y abre #113. RePaint y Choi quedan como antecedentes mecanisticos/Related Work.
- **Snowballing:** se registro Selles et al. 2022 sobre O-MAR en fusion sacroiliaca como N3 pendiente, sin
  buscarlo ni descargarlo. `main.tex` y `01-decisiones.md` no se modificaron.
- **Pendiente:** Niu 2021 sigue sin PDF/raw y `song2024bmar` sigue sin texto completo. El ancho de `B_delta`
  conserva justificacion empirica local y requiere la sensibilidad prevista.

## PUNTO DE RETOMA del 2026-09-20 — SUPERADO por el bloque de arriba (historico)

> Escrito para una sesion nueva, sin historial. Verificado contra disco el 2026-09-20; el arbol esta limpio
> (ultimo commit `420d51c`). El bloque del 2026-09-17 queda mas abajo como historico: **su plan (renderizador
> latente + compuerta) ya se ejecuto y cambio de rumbo**; lo unico vigente de el son P2 (#70) y P3.

### Actualizacion 2026-09-21 (3) — DDIM y planificador coseno leidos; bloque metodologico de #106 completo

- **Ultimo paso completado:** `lector-papers` leyo `song2021ddim` y `nichol2021improved`; ambas fuentes tienen
  ficha, raw, clean, alta en `refs/MAPEO.md` e `_index.md`. `refs.bib` pasa de 103 a **105 entradas**. Con ellas
  quedan disponibles DDPM, ADM, DDIM y el planificador coseno.
- **Que respalda cada una:** Song define DDIM determinista con eta = 0 y evalua 50 pasos sobre modelos T = 1000;
  Nichol--Dhariwal define el schedule coseno con `s = 0.008` y beta <= 0.999.
- **Limite que debe conservarse en Metodos:** ningun paper evalua la combinacion exacta de la tesis —coseno con
  T = 1000, DDIM lineal con eta = 0 y 50 pasos, U-Net y CT pelvica con metal—. Nichol usa T = 4000 en las
  ablaciones relevantes y sus 50 evaluaciones corresponden a Improved DDPM, no a DDIM. #106 sigue ABIERTA solo
  hasta atribuir correctamente cada componente en `main.tex` y declarar que la integracion se valida localmente.
- **Snowballing:** las dos lecturas no abrieron candidatos nuevos que cumplan las reglas.

### Actualizacion 2026-09-21 (2) — ocho fuentes de #106 leidas, normalizadas y auditadas

- **Ultimo paso completado:** `lector-papers` leyo a fondo los ocho PDF entregados y genero sus fichas en
  `docs/literatura/`: DDPM, ADM, U-Net original, Liu 2021, DiT, Yeap 2025, LeFusion y An 2025. Todos tienen
  `refs/clean/`, alta en `refs/MAPEO.md` y fila en `_index.md`; `refs.bib` pasa de 95 a **103 entradas**.
- **Conclusion para #106:** U-Net se puede justificar por alineacion con DDPM/ADM, por Yeap (CT, pocos pacientes
  y concatenacion) y por LeFusion (sintesis local y copia del fondo). **No** se puede justificar como superior a
  DiT por pocos datos: An 2025 favorece a DiT en brecha de PSNR con 10^3--10^4 imagenes naturales 32 x 32 y
  FLOPs equivalentes. Peebles tambien invalida el descarte por atencion sobre 65 536 pixeles, porque usa parches
  latentes. #106 queda corregida como eleccion pragmatica y no comparada.
- **Pendiente:** de las cuatro fuentes metodologicas originales aun faltan raw y PDF de **DDIM** y de
  **Nichol--Dhariwal (planificador coseno)**. Nuevo snowballing N2 condicional: Kadkhodaie et al., ICLR 2024.
- **Verificacion:** `scripts/build_refs.py` genero las 103 entradas; BibTeX y dos pasadas de pdfLaTeX terminaron
  sin citas indefinidas (7 paginas). `latexmk` no se uso porque la instalacion local de MiKTeX no tiene Perl.
  `main.tex` y `01-decisiones.md` no se modificaron. La discrepancia de paginas de DiT (raw 4172--4182; PDF
  4195--4205) queda marcada `% VERIFICAR` y documentada en `refs/MAPEO.md`.

### Actualizacion 2026-09-21 — busqueda dirigida de fuentes para justificar U-Net (#106)

- **Ultimo paso completado:** se buscaron fuentes primarias publicadas y se añadieron a la prioridad de
  `docs/literatura/_candidatos.md`. Las mas directas son **LeFusion (ICLR 2025)**, U-Net 3D para sintesis medica
  local en CT con fondo preservado, y **Yeap et al. (Medical Physics 2025)**, U-Net de difusion entrenada desde
  cero con 25 pacientes y reentrenada con 27 casos pelvicos. Se registraron tambien U-Net original, evidencia
  de regimen escaso y los controles adversariales DiT/An.
- **Siguiente:** la autora decide cuales fuentes incorporar; cada alta empieza por su raw en `refs/raw/`. La cadena
  N1 propuesta es DDPM/ADM + LeFusion + Yeap; no se toca `refs.bib` ni `main.tex` antes de esos raw.
- **Pendiente/impacto:** #106 sigue ABIERTA, pero mejor delimitada. No aparece una implicancia nueva: ninguna fuente
  compara U-Net contra DiT en esta tarea, asi que solo se puede defender una eleccion razonada, no superioridad.

### Actualizacion 2026-09-20 (4) — tabla de prioridad de `_candidatos.md` reordenada tras el giro a dominio de imagen

- **Ultimo paso completado:** auditoria y reordenamiento de "PRIORIDAD VIGENTE" en `docs/literatura/_candidatos.md`,
  que seguia congelada en el 2026-09-18, es decir en la bibliografia del renderizador **latente + ControlNet**.
  Ahora entra primero el bloque de **#106** (DDPM, DDIM, coseno, ADM: implementados en `src/renderizador/`, con
  **0 entradas** en `refs.bib`), suben LeFusion (N1), `B_delta`/Selles y RePaint (N2), y las metricas AAPM pasan a
  insumo de E-A1..E-A4; **baja** Choi (es latente y es *removal*). La fila del **VAE alternativo queda DESCARTADA**
  (MAISI/MedVAE/CVQ-VAE): su condicion "solo si P1 da No-Go" se evaporo al elegirse la opcion A sin autoencoder.
- **Siguiente:** la autora decide la reordenacion (la tabla dice que la prioridad la propone el asistente) y, si la
  acepta, **#106 empieza por pegar los cuatro raw en `refs/raw/`** (regla 9); sin eso no se escribe Metodos.
- **Pendiente que surgio:** ninguno nuevo. Sin implicancias sobre la tesis: el fondo ya esta en **#106**; lo de hoy
  es mantenimiento bibliografico. Sin tocar `refs.bib`, `main.tex`, `00-tesis.md` ni `01-decisiones.md`.

### PUNTO DE RETOMA 2026-09-21 — leer esto primero

**El proyecto esta esperando el resultado del primer entrenamiento de su historia.** Job **52074** en Khipu,
piloto de 200 pasos del renderizador. Encolado al cierre de la sesion.

**Lo primero que hay que hacer:** bajar sus salidas y analizarlas. El **encargo detallado esta al final de
`docs/04-implicancias.md`**, seccion *"Ronda 2026-09-21 (cierre 2) — ENCARGO ACTUALIZADO PARA EL SIGUIENTE
AGENTE"* — **la segunda, que sustituye a la primera**. Trae las tres tareas, los controles que pueden fallar y
las implicancias abiertas por gravedad. **Leerlo antes de tocar nada.**

**Control que decide si la corrida vale:** el log debe decir **`parches: 17149`** y **`casos: 47`**. Si dice
21 754 / 72, el manifiesto no se aplico y hay que relanzar, no reinterpretar.

#### Lo que se cerro el 2026-09-21

- **Criterio de inclusion PREINSCRITO** (`01-decisiones.md`, entrada 2026-09-21). R1 dentro del cuerpo, R2 caso
  con material ortopedico, R3 metal del componente mas banda al 0.62. **Tamano y forma se reportan, no filtran.**
  Conjunto congelado: **17 149 parches, 241 componentes, 47 casos**, en el manifiesto versionado
  `experiments/objetivo3/a5_manifiesto_train.csv`, que el entrenador lee y **sin el cual aborta**.
- **Validado contra las 40 laminas revisadas por la autora: 36/39 = 92%**, recall 100%, frente al 40% del
  criterio anterior. Los 3 falsos positivos (dos piezas de fijador dentro del cuerpo y un DIU) **no los separa
  ninguna regla geometrica**: limitacion declarada.
- **Dos recomendaciones del asistente quedaron descartadas por los datos**, y consta: el umbral de volumen de
  200 mm3 (quita el 4% de parches pero el 29% de componentes) y el filtro por forma tipo tornillo.
- **`--dentro-min` no necesita justificacion: es invariante.** `frac_dentro` es 0.000 o 1.000, nunca
  intermedio; el barrido de 0.05 a 0.95 da resultados identicos. Mismo argumento que `F = 0.001`.
- **`main.tex` editado** (orden explicita): #107 aplicada, Objetivo 3 al dia, de dos desplazamientos de dominio
  declarados se pasa a **tres**, y el **criterio de exito de `main.tex:98`** deja de ser *"statistically
  comparable"* a secas: ahora declara endpoint primario unico (streak amplitude), **Wilcoxon** de una cola para
  superioridad, **TOST** para equivalencia con margen fijado de antemano y medido solo en validacion, y que un
  resultado **no concluyente es reportable**. Compila **0 errores, 0 indefinidas, 7 paginas, 110 referencias**.
- **Contradiccion de #106 resuelta:** la entrada duplicada del asistente se retiro y quedo una nota de
  trazabilidad. **La #106 vigente es la de la autora**, y sigue ABIERTA: la combinacion coseno T=1000 + DDIM
  lineal eta=0 con 50 pasos **no esta evaluada en ninguna fuente**.
- **#106 cerrada en su parte bibliografica:** las cuatro fuentes del metodo (DDPM, ADM, coseno, DDIM) ya estan
  en `refs.bib`, subidas por la autora, mas cuatro que sostienen la discusion U-Net frente a DiT.

#### Lo que queda, por gravedad

1. **#105 RESUELTA el 2026-09-21** (`01-decisiones.md`, entrada 2026-09-21 (2)). **Ya no bloquea.** No hizo
   falta rehacer la particion: basto aplicar **R2 tambien a `val`**, que es el criterio ya preinscrito, sin
   tocar semilla ni `test` y **sin seleccion post hoc**. `val` queda en **896 parches / 3 casos con implante
   real**, manifiesto en `a5_manifiesto_val.csv`. **Limitacion declarada: `Delta` se medira sobre n = 3
   pacientes**; el informe debe decir la n y no presentarlo como robusto.
   - **PENDIENTE DE CODIGO:** `entrenar.py` **todavia no usa** el manifiesto de validacion; hoy solo carga
     `train`. Hay que conectar el bucle de validacion antes de que `val` sirva para algo.
2. **14 fichas nuevas sin procesar** en `docs/literatura/` (regla 13). La mas urgente es **`lugmayr2022repaint`**:
   RePaint es inpainting con difusion, o sea el metodo de esta tesis.
3. **Dos entradas #106 contradictorias** en el archivo critico (regla 17). Debe prevalecer la de la autora.
4. **La evaluacion E-A1..E-A4 sigue sin una sola linea de codigo.**
5. **Metodos sin escribir:** la arquitectura no esta en `main.tex` y ya no hay excusa bibliografica.

#### AVISO para quien escriba Metodos — leer antes de redactar la arquitectura

La justificacion de la **U-Net** que va al documento es la de la **#106 vigente**: **eleccion pragmatica y no
comparada**, alineada con DDPM y ADM y con dos precedentes medicos cercanos (Yeap, LeFusion), entrenable en el
pipeline ya implementado y sin depender del VAE que fracaso; la integracion concreta se declara **propia y
pendiente de evaluacion**.

**NO usar el argumento del sesgo inductivo con pocos datos.** Lo escribio este asistente y **esta refutado** por
la bibliografia del propio proyecto:
- **`an2025generalization`** compara DiT y U-Net en espacio de pixeles a FLOPs equivalentes y, con 10^3-10^4
  imagenes, reporta **brecha de PSNR menor para DiT**.
- El argumento de que un DiT exigiria atencion sobre 65 536 pixeles es **falso**: `peebles2023scalablediffusion`
  tokeniza **parches latentes**.

Es la trampa mas facil de pisar, porque el razonamiento suena convincente y esta mal. Detalle en la **#106
vigente** y en la nota de la **#106 (duplicada) RETIRADA**.

**Limite adicional a declarar (#106):** la combinacion **coseno T = 1000 + DDIM lineal eta = 0 con 50 pasos**
que implementa `src/renderizador/difusion.py` **no aparece evaluada en ninguna fuente**; Nichol--Dhariwal
advierte ademas que el stride cuadratico de Song empeoro al combinarse con coseno.

#### Advertencia de metodo, ganada a golpes en esta sesion

Tres fallos silenciosos se detectaron **mirando la salida**, no con controles: el eje sagital de las laminas,
el `level=None` de `marching_cubes` que dibujaba metal donde decia piel, y una cita mal caracterizada (#107).
**Toda capa o metrica derivada necesita una comprobacion que pueda fallar.** En el caso de las superficies, la
comprobacion util resulto ser **contar vertices**, no mirar la figura.

### Actualizacion 2026-09-20 (3) — las cuatro decisiones del Diseno A, RESUELTAS y escritas

- **`01-decisiones.md` tiene la entrada 2026-09-20 (2)** con D1-D4, escrita por el asistente **por orden explicita
  de la autora**. Resumen: D1 umbral 2500 (semimaximo como sensibilidad); **D2 unidad = COMPONENTE**; D3 cilindro
  uniforme de ~4.9 mm con cabeza como sensibilidad; D4 forma del contraste fijada (endpoint primario unico,
  Wilcoxon de una cola, **TOST** para equivalencia) y margen `Delta` medido despues sobre validacion.
- **Para preinscribir `diseno_A.md` solo falta el margen `Delta`**, que por construccion se mide despues del
  piloto. Todo lo demas esta decidido.
- **D2 cambio por medicion, no por opinion (#102).** A1 dio 2714/13496 cortes (20.1%) con `G` fuera del encuadre.
  Se descartaron con datos la mezcla de implantes (20.0% vs 20.2%) y el spacing (sin tendencia); la causa real es
  que `G` se definia por corte y en pacientes bilaterales abarca 380 mm. **`a1b_parches_componente.py`** (nuevo)
  extrae por componente; en el peor caso de #102 da **0 de 1217** parches fuera del encuadre y control 1217/1217.
  `a1_parches.py` queda **CONGELADO** como evidencia.
- **A1b: la primera corrida MURIO por memoria en 47/79 sin escribir un solo CSV (#103).** Causa: materializaba dos
  mascaras del tamano del volumen por componente. **Corregido**: ahora trabaja dentro de la caja del componente
  (`find_objects`) y **anexa los CSV caso a caso con `flush`**, saltando los que ya tienen fila (reanudable).
  Control: los tres casos de prueba dan cifras **identicas** a la version muerta, asi que la reescritura es
  equivalente y solo mas liviana. **Relanzado sobre la cohorte; al cierre seguia corriendo.**
- **A1b TERMINADO (79/79, 0 errores).** Cifras de cohorte, que son las citables: 363 componentes, **23 058
  parches**; no contenidos **336/23058 (1.5%)** frente al 20.1% por corte, **0/1304** en validacion; control de
  composicion **23 058 de 23 058**. Caché ~**2.25 GB**. **D2 cerrada con medicion.**
- **PERO A1b abrio #104, que es mas grave que lo que cerro.** La composicion del conjunto no coincide con la
  tarea: **42.5% de parches sin ningun voxel del implante objetivo** (`B_delta` se extiende mas alla de las
  puntas), **40.3% con metal de otro componente** (19.3% sin metal propio y con ajeno), y componentes con volumen
  mediano **458 mm3** frente a ~1450 de un tornillo (52% por debajo de 500 mm3). Falta una **politica declarada de
  muestreo** y hay que preinscribirla. **Toca D4**: validacion tiene 51.6% de parches sin metal, asi que medir
  `Delta` ahi sin estratificar lo haria artificialmente pequeno.
- **NO subir el cache a Khipu todavia:** si cambia la politica de muestreo, cambia lo que se sube.
- **Numero que NO se debe citar:** el cruce "14 componentes tipo tornillo" es un artefacto de usar caja alineada
  a los ejes en vez del eje principal por PCA (detalle en #104).
- **`datos.py` agrupa el 2.5D por SERIE (caso + componente)**, asi los vecinos de un corte son del mismo implante
  y no del contralateral. Reporta `casos` (pacientes) y `series` (implantes) por separado.
- **`KHIPU.md` seccion A2 y `a2_entrenar.sbatch` apuntan ya a `a1b_cache`**, con la orden de borrar `a1_cache` en
  el cluster si se subio antes: entrenar con el produciria `G` multi-implante.
- **`main.tex`: #98 APLICADA** (2026-09-20, orden explicita de la autora, opciones a + b). El reclamo de ausencia
  se acota a *"generation band outside the implant mask"* y se citan los precedentes de medicion
  (`radzi2014metalartifacts` 2.0/2.6/1.6/2.0 mm; `cassanego2026evolution` 3.1-4.2 mm) con sus cuatro diferencias
  declaradas: desde el **eje** y no la superficie, umbral no publicado, tornillos de 3.5-4.0 mm en cadaver/dental,
  sin HU. Compila **0 errores, 0 citas indefinidas, 7 paginas, 95 referencias**; `refs.bib` **sin tocar** (las dos
  claves ya estaban). `B_delta` = 12 mm sigue sin calibracion publicada: queda como construccion declarada.

**Siguiente:** (1) A1b termina -> anotar parches y empaquetar `a1b_cache.tgz`; (2) subir y correr el piloto de 200
pasos en Khipu; (3) cerrar #89 con la cifra medida; (4) medir `Delta` sobre validacion y **preinscribir**;
(5) escribir la evaluacion E-A1..E-A4, que sigue sin existir.

### Actualizacion 2026-09-20 (2) — E11 corrido, A1 corriendo, y el Diseno A ya tiene codigo

- **E11 TERMINADO sobre los 178 volumenes.** 79 componentes esbeltos. `d_centro` mediana **4.91 mm**, que
  coincide con el fuste de catalogo (4.8 mm) y con E8 (5.00 mm): **tres vias independientes dentro de un cuarto
  de voxel**. Ensanchamiento de extremo: mediana **0.96 mm** (~1 voxel), pero **12/59 superan 2 mm**. Lectura:
  cilindro uniforme como piloto, cabeza como sensibilidad. Salidas en `experiments/objetivo2/outputs/e11/`
  (fuera de git). **Implicancia #101.** Con esto, **D3 de `diseno_A.md` ya se puede decidir**.
- **A1 CORRIENDO** (`experiments/objetivo3/outputs/a1/`, cache en `outputs/a1_cache/`). Al cierre iba en 9/79.
  Señal temprana: la contencion en 256 falla **solo en implantes grandes** (`CLINIC_0005`: 60 de 267 cortes no
  caben; el resto de los casos vistos, 0). Hay que leer `a1_casos.csv` al terminar: es el control de D2.
- **Codigo del Diseno A escrito y probado en CPU** (no existia; **implicancia #100**):
  `src/common/{ventanas,region}.py` y `src/renderizador/{modelo,difusion,datos,entrenar}.py`, mas
  `experiments/objetivo3/a2_entrenar.sbatch`. `src/common/` **reexporta** lo validado en `experiments/`, no lo
  reimplementa. Controles que pasan: identidad multi-ventana **1.27e-11 HU**, perdida exactamente 0.0 con `G`
  vacia, salida exactamente 0.0 fuera de `G`, reproducibilidad por semilla, y **aislamiento: 0 de 34 casos de
  test en el cargador**. Prueba end-to-end sobre 736 parches reales: 1.8 M parametros a `base=16`, 0.77 s/paso
  en CPU. **Esa cifra de CPU no sirve de presupuesto**: la prueba corta de 200 pasos en Khipu sigue pendiente.
- **`diseno_A.md` ampliado con la seccion 8 bis**: recomendaciones del asesor sobre las cuatro `[DECIDIR]`, con
  la columna de **cuando** se puede fijar cada una (D1 y D2 ya; D3 tras E11, ya disponible; D4 mixto: la forma
  del contraste ya, el margen `Delta` solo tras el piloto sobre validacion). Sigue en **BORRADOR, no preinscrito**.
- **`repos/` nuevo:** `xcist-main` y `xcist-example` clonados (este ultimo trae `AAPM_datachallenge`, filas 132-133
  de `_candidatos.md`, ligadas a #8 y P2/#70). Son los dos unicos repos de codigo que `_candidatos.md` menciona.

**Siguiente, en orden:** (1) leer `a1_casos.csv` cuando A1 termine y cerrar D2; (2) la autora decide las cuatro
`[DECIDIR]` — D3 ya tiene su medicion; (3) preinscribir `diseno_A.md`; (4) prueba corta de 200 pasos en Khipu con
`a2_entrenar.sbatch` y actualizar #89 con la cifra medida; (5) escribir la evaluacion E-A1..E-A4, que no existe.
**Pendientes que surgieron:** #100 y #101 ABIERTAS; el ensanchamiento de 12/59 no esta decidido; la evaluacion del
Objetivo 3 sigue sin una sola linea de codigo.

### Donde esta el proyecto

- **El Objetivo 1 esta CERRADO y dio NO-GO.** P1 (jobs 51669-51671, 51878, 51879) evaluo seis combinaciones
  {preentrenado, decodificador afinado} x {`pub`, `LW20000`, `pub+asinh`} en 34 pacientes de test. La mejor,
  afinado `pub+asinh`, dio **61.72 HU** de media por paciente en hueso (IC95 [55.12, 68.99]) contra un umbral de
  25 HU, con **34/34 pacientes fallando en las seis**. Controles todos en verde: identidad frente a E6c 165/165,
  preentrenado frente a E6b 330/330, encoder congelado 3/3, decodificador distinto 3/3. Curvas en plateau desde
  ~5 000 pasos. Resultados versionados en `experiments/objetivo1/p1_compuerta.md`, `p1_eval.csv`, `p1_control.csv`
  y `p1_curvas/`. Implicancia **#91**.
- **MAISI tambien esta cerrado, sin gastar GPU (#93 CERRADA).** Su bundle (`maisi_ct_generative`, descargado en
  Khipu) mapea la salida a **[-1000, 1000] HU** en `scripts/sample.py`, rango que el paper no publica. Medido con
  `p1_maisi.py cota` sobre los 34 de test: **solo el recorte** ya da 42.24 HU de media en hueso (11/34 por encima
  del umbral). Es cota inferior, asi que no pasa ni con pesos perfectos. Tabla: `experiments/objetivo1/p1_maisi_cota.csv`.
  MedVAE quedo descartado antes (#94: excluye metal en su entrenamiento).
- **El Objetivo 3 se redisenó: opcion A, difusion en el ESPACIO DE IMAGEN, sin autoencoder** (decision de la autora,
  `01-decisiones.md` 2026-09-19). Inpainting de `G = M ∪ B_delta`; fuera de `G` se copia el CT, asi que la
  preservacion es exacta por construccion. Ya **aplicado a `main.tex`**: titulo (*Multi-Window Image-Domain
  Diffusion*), pregunta, objetivo general, resultado No-Go escrito en el Obj 1 (con la frase de MAISI), Obj 3
  reescrito y fila de la tabla. Compila **0 errores, 7 paginas, 95 referencias**.
- **La geometria del tornillo quedo cerrada con fuentes citables** (decision 2026-09-20, #97 y #99): el "7.3 mm"
  es el **diametro de rosca**; el cuerpo es de **4.8 mm** (`synthes2003guide`, guia del fabricante del sistema),
  nucleo bajo la rosca 4.7 mm, paso 2.5 mm, rosca de 16/32 mm o completa, **cabeza 8.0 x 4.5 mm sin avellanar**
  (`sayres2014comparison`), arandela 13.0 mm de diametro. Sin fuente y declarados: **espesor de arandela**
  (1.5 mm, `doublemedical2021trauma`, OTRO fabricante) y **canulacion** (parametro libre; el 2.9 mm de los
  distribuidores resulto ser canulacion de brocas). Material: 316L o Ti-6Al-7Nb, y la mascara binaria no lo codifica.

### Lo siguiente: experimentos del Diseno A

Diseno en `experiments/objetivo3/diseno_A.md`, **en BORRADOR: no preinscrito**. Se preinscribe (se congela y se
registra en `01-decisiones.md`) **antes de entrenar**. Orden:

1. **E11 — perfil axial (CPU local, ~30 s por caso).** `experiments/objetivo2/e11_perfil_axial.py`, probado en 3
   casos. Mide el diametro a lo largo del eje de los tornillos reales para decidir si la mascara necesita el tramo
   de rosca de 7.3 mm o basta un cilindro de 5.0 mm. Es el paso 4 de la decision 2026-09-20.
   `python e11_perfil_axial.py --out <dir>` (sin `--casos` recorre los 178; filtra a componentes esbeltos:
   largo >= 30 mm y anchos <= 12 mm, que deja fuera placas y protesis).
2. **A1 — extraccion de parches (CPU local).** `experiments/objetivo3/a1_parches.py`, probado en 2 casos: 216
   cortes, **todos caben en 256 x 256** y el control de composicion fuera de `G` dio 216/216.
   `python a1_parches.py --out <dir> [--cache <dir>] --verificar`. Usa la particion de P1
   (`experiments/objetivo1/p1_particion.csv`: 126 train / 8 val / 34 test por paciente).
3. **Las 4 decisiones que faltan** (marcadas `[DECIDIR]` en `diseno_A.md`): mascara de entrenamiento (umbral 2500
   frente a semimaximo), tamano de parche (recomendado 256), diametro del cilindro y **criterio de exito**
   (`main.tex:98` promete "mejor que copia-pega" y "comparable al brazo fisico": falta fijar la prueba estadistica
   ANTES de ver resultados, patron #76).
4. **Prueba corta en Khipu** (200 pasos, como en P1) para medir s/paso y memoria antes de lanzar nada largo (#89).
5. **En paralelo, sin GPU:** P2 (verificar en el codigo de XCIST si paciente y metal se proyectan juntos, #70) y
   P3 (muestreador + SAP en `src/muestreador/`, que sigue vacio).

### Pendiente de decision de la autora (nada de esto lo aplica el asistente, reglas 4 y 14)

- **#98:** `main.tex:54` afirma que no hay precedente que cuantifique una banda peri-implante, y
  `radzi2014metalartifacts` publica milimetros en CT (2.0/2.6/1.6/2.0). Hay que acotar la frase.
- **#89:** plan de falsos positivos de extraccion y presupuesto de computo, pedidos por el asesor.
- **#90:** el plazo real (la autora hablo de 5 semanas y luego de ~10; los documentos planifican con ~11).
- **7 paginas:** el `nocite` global de `main.tex:139` mete las 95 entradas en la bibliografia. Si hay limite, se quita.
- **#95, #96, #99** y las 4 de `diseno_A.md`.

### Reglas que esta sesion aprendio por las malas

- **Khipu:** hay tope de jobs **enviados** (con 5 en cola, el sexto se rechaza); `scontrol hold` sin liberar costo
  ~10 h de cola; un `.sbatch` lanzado desde `~` no encuentra el script; y los marcadores tipo `<nombre>` pegados
  tal cual hacen que bash los lea como redireccion. Todo en `KHIPU.md`, con sus secciones P1, P1-MAISI y lecciones.
- **Documentacion de fabricante sin `raw`:** entra a `refs/clean/` como `@manual` con la procedencia en comentarios
  y `% VERIFICAR` en lo dudoso; la excepcion esta escrita en `refs/MAPEO.md`. Ya hay cinco entradas asi.

## PUNTO DE RETOMA anterior (2026-09-17, historico)

> Sustituye como entrada al bloque del 2026-09-15 que sigue abajo (queda como historico; sus pendientes sobre
> #36/#39 y la lectura de Chen ya estan resueltos). Verificado contra disco el 2026-09-17.

**Sesion 2026-09-18 (2) — entrega de 2 pp.** `entrega/main.tex` + `main.pdf` (2 pp., 21 refs, 0 indefinidas) responden la retroalimentacion del asesor: plan de falsos positivos de extraccion y presupuesto de computo con cifras medidas en Khipu; sin las ~140 GPU-h del borrador (no medidas). Implicancia **#89 ABIERTA**. Siguiente: piloto cronometrado del ControlNet cuando P1 cierre; decidir si #89 pasa a `main.tex`.

**Sesion 2026-09-18 — 13 fuentes mas + duplicados.** 13 altas (`refs.bib` = 83; compila 6 pp., 0 indefinidas); ningun PDF queda sin ficha; duplicados borrados con autorizacion (Miller, Gertzbein, raw de Templeman; PDF de Templeman renombrado). Implicancias **#83-#88** (ninguna abierta); `main.tex:117` decia falsamente que ningun corredor se midio con fractura (Reilly 2003 lo hace) -> **APLICADA (a) en `main.tex:117`** por orden de la autora (compila 6 pp., 83 refs, 0 indefinidas). Pendiente: `
ocite{*}` (#82/#88); PDF + raw de MWLNet y Choi (prioridades 1-2 de `_candidatos.md`); entrada 2026-09-18 para `01-decisiones.md`. Siguiente: evaluacion de P1 en Khipu.

**Sesion 2026-09-17 (2) — literatura nueva.** 8 raw nuevos: 6 altas en `refs/clean/` (`refs.bib` = 70; compila 6 pp., 0 indefinidas) y 2 duplicados exactos (`gertzbein1990`, `templeman1996proximity`, que ya tiene PDF). Fichas escritas. Implicancias **#77-#82**: ninguna cambia alcance, Obj 1/P1 ni renderizador; 2-15% y escala de 4 grados cerradas. Pendiente de la autora: quitar `
ocite{*}` (#82, recomendado), linea obsoleta de Templeman en `00-tesis.md` y entrada propuesta para `01-decisiones.md`. Siguiente: sigue P1 en Khipu (evaluacion tras 51670/51671).

**Donde esta el proyecto.**
- `main.tex` compila: **6 paginas**, 64 referencias, 0 errores, 0 citas indefinidas. `src/` sigue **vacio**.
- Literatura: **toda entrada de `refs/raw/` tiene ficha** (ronda 2026-09-16). Implicancias hasta **#76**.
- **Decisiones del 2026-09-17, delegadas al asistente como asesor** (`01-decisiones.md`, entrada 2026-09-17):
  - se mantiene el renderizador (la autora rechazo recortarlo);
  - ablaciones FUERA; brazo fisico de Peters sobre un subconjunto reducido;
  - Chen citado como preprint.
- **Regla preinscrita en `main.tex`:** el Go/No-Go del Objetivo 1 (MAE en hueso < 25 HU, pacientes separados) se
  prueba con el VAE de SD 1.5 preentrenado y con una variante de **decodificador adaptado y encoder congelado**. Si
  ninguno pasa, **no hay Objetivo 3** y el No-Go es el resultado.

**E6b con RMSE — NO SE CORRIO (confirmado en Khipu por la autora, 2026-09-17).** `sacct` desde 2026-09-15 solo
muestra 51539 (prueba), 51540 (cohorte MAE, 08:44:58) y 51591 (prueba RMSE de 1 volumen); `~/metalsynth/data/e6b/` esta
vacio. En la PC: `outputs/e6b_vae_sd15.csv` = cohorte MAE vieja (178 filas, 32 columnas, sin `rmse`), logs en
`outputs/e6b/`. **Decision 2026-09-17 (2):** no se relanza la cohorte RMSE sola; MAE y RMSE se reportan dentro de P1.

**Siguiente, en orden:**
1. **P1 — PREPARADO Y PROBADO EN LOCAL (2026-09-17), falta correr en Khipu.** `experiments/objetivo1/p1_decodificador_sd15.py`
   + `p1_entrenar.sbatch` / `p1_evaluar.sbatch` + `p1_particion.csv` (168 pacientes: 126/8/34, semilla 20260917). Regla
   fijada por la autora antes de correr: Go si **alguna** de {sd15, afinado} x {pub, LW20000, pub+asinh} tiene **media por
   paciente** del MAE en hueso con **`vae regla`** < 25 HU en los 34 de test. Comandos: `KHIPU.md`, seccion P1 (prueba
   corta -> 3 entrenamientos -> evaluacion). Local: controles identidad/eco/hash/`B_delta` OK; VAE real sin probar.
   **#76 DECIDIDA Y APLICADA** (regla completa en `main.tex:77`; desempate a priori pub+asinh > LW20000 > pub, sd15 antes
   que afinado; pase MARGINAL si IC95 superior >= 25 HU). Registrada en `01-decisiones.md` 2026-09-17 (3).
   **Lanzado en Khipu (2026-09-17):** prueba 51667 (entrenar) + 51668 (evaluar, afterok) y cohorte 51669/51670/51671
   (pub+asinh/LW20000/pub) **a la vez, sin esperar la prueba**. Evaluacion rechazada (`QOSMaxSubmitJobPerUserLimit`).
   Estado 00:56: 51667 corre bien en ds001 (paso 0: val hueso regla MAE 156.02 HU, 4.1 GB); 51668 espera dependencia;
   51669-71 en PD (Priority). ~01:05: 51667 COMPLETED (5:40); **51668 FAILED rc=1 (2:38), causa sin leer**; 51669 corre
   en ds001 (arranco antes del hold); 51670-71 retenidos. Causa de 51668: faltaba `qc/e6b_vae_sd15_mae_20260915.csv` (evaluacion
   completa, fallo en el control). Prueba: 1.32 s/paso, 24.6 GB, ~11 h/config. Pendiente: subir CSV + `.py`, `resumen` en
   nodo de acceso (meta sd15 frente a E6b 4 de 4) y `scontrol release 51670 51671`.
   **51669 (`pub+asinh`) COMPLETED en 10:36:07** (estimacion 11 h, acertada). **51670 y 51671 siguen PENDING 20 h
   despues por `scontrol hold`; liberados y 51670 corre en g002, 51671 detras.** Controles de la prueba CERRADOS:
   **sd15 frente a E6b 4 de 4**, identidad 2 de 2, hashes OK. Falta: evaluacion (~3.5-4 h tras el ultimo entrenamiento).
   2026-09-18: la evaluacion NO se encolo (`cd` mal tecleado; `sbatch` corrio en `~`). 51670/51671 ya no estan en cola:
   Verificado: **51670 (`LW20000`) COMPLETED 10:33:24 en g002**, hash identico. **51671 (`pub`) CANCELLED 0:15 a las
   5:56:43 en ds001** (probable mantenimiento del cluster); queda `ckpt_pub.pt` de las 11:11. Siguiente: relanzar
   `p1_entrenar.sbatch pub` (reanuda del checkpoint) y encolar la evaluacion con `afterok`.
   Relanzado: **51878** (`pub`, desde el paso 16000; PD Resources, las dos A6000 en `mix`) y **51879** (evaluacion,
   afterok:51878). Faltan 14 000 pasos x 1.26 s = ~4.9 h + ~3.5-4 h de evaluacion, contadas desde que arranque.
   `squeue --start`: 51878 entra en ds001 a mas tardar ~01:09 del 19 (cota por TIME_LIMIT ajenos); veredicto ~10:00 del 19.
   No se cambia de GPU: MIG 3g.20gb < 24.6 GB y la tesla de g001 no tiene memoria verificada (decision 2026-09-18).
   **2026-09-19: P1 TERMINADO — NO-GO** (51879; controles 165/165, 330/330, 3/3, 3/3). Mejor: afinado `pub+asinh`
   61.72 HU [55.12, 68.99]; 34/34 pacientes >= 25 HU en las seis. **#91 ABIERTA: decidir (a) aceptar No-Go, sin
   Objetivo 3 (recomendada) o (b) MAISI como compuerta nueva preinscrita.** Salidas traidas a la PC y versionadas en
   `experiments/objetivo1/` (`p1_compuerta.md`, `p1_eval.csv`, `p1_control.csv`, `p1_curvas/`). Curvas en plateau
   desde ~5 000 pasos: "faltaron pasos" no explica el No-Go (#91).
   Fichas 2026-09-19: `guo2025maisi` (#93), `varma2025medvae` (#94), `tonetti2001results` (#92). Ninguno de los dos VAE
   documenta su rango de HU ni error en HU: solo se deciden midiendo. Paper del sacro ("3D statistical modeling...") NO
   esta en `papers/` ni `refs/raw/`. Pendiente: refs/clean + build_refs para las tres entradas nuevas.
   **Decision 2026-09-19 (01-decisiones): opcion A + MAISI como extension del Obj 1.** Borrador de diseno en
   `experiments/objetivo3/diseno_A.md` (NO preinscrito; 4 `[DECIDIR]` de la autora). #95/#96 ABIERTAS.
   Siguiente: respuestas de la autora -> extraccion de parches (CPU) -> prueba corta Khipu -> preinscripcion.
   **`main.tex` adaptado (2026-09-19, orden de la autora):** titulo, RQ, objetivo general, resultado No-Go escrito en
   el Obj 1, Obj 3 reescrito como inpainting en espacio de imagen y fila de la tabla. Compila 6 paginas, 0 errores.
   `docs/00-tesis.md` sigue describiendo el Obj 3 como LDM + ControlNet: pendiente de orden de la autora.
   **`refs/deep-research/` revisado (2026-09-19):** candidatos de geometria del tornillo en `_candidatos.md`
   (ronda 2026-09-19; prioridad G1 Berk 2023, G2 Gardner 2015, T1 ficha Synthes) e implicancia **#97** (el nominal de
   7.3 mm seria rosca, no fuste; cabeza y arandela ausentes del modelo).
   **2026-09-19, 9 lecturas mas (6 papers + 3 fichas de fabricante): #97 VERIFICADA.** Rosca 7.3 / fuste 4.8-4.9 /
   nucleo 4.7 / paso 2.5 / cabeza 8.0 x 4.5 / arandela 13.0 mm. Sin fuente: espesor de arandela y canulacion.
   Nueva **#98** (`main.tex:54` afirma que no hay precedente que cuantifique la banda; Radzi publica mm en CT).
   `refs.bib` pasa a **92 entradas**; las tres fichas de fabricante entran como `@manual` sin raw (excepcion en
   `refs/MAPEO.md`). Compila 6 paginas, 0 errores.
   2026-09-20, 5 documentos mas: **espesor de arandela 1.5 mm** (catalogo Double Medical, otro fabricante) y
   **canulacion sin fuente citable** (2.9 mm solo en listados de distribuidor).
   2026-09-20 (2): leida la **guia del fabricante del sistema 6.5/7.3** (`synthes2003guide`): confirma fuste 4.8 mm y
   material 316L o Ti-6Al-7Nb, **no publica** arandela ni canulacion, y su 2.9 mm es de instrumental. Nueva **#99**
   (la indicacion sacroiliaca impresa es del calibre 6.5, no del 7.3). `refs.bib` = 94 entradas.
   **`main.tex` con la geometria nueva (2026-09-20, orden de la autora):** envolvente del corredor frente a mascara de
   metal, cuerpo 4.8 mm (`synthes2003guide`), cabeza 8.0 x 4.5, arandela 1.5 mm (otro fabricante), canulacion libre y
   aleacion no codificada. Compila 0 errores, **7 paginas** (por `nocite{*}` con 94 entradas: si hay limite, se quita).
   Scripts nuevos probados en local: `objetivo2/e11_perfil_axial.py`, `objetivo3/a1_parches.py`, `objetivo1/p1_maisi.py`
   + `.sbatch` (comandos en `KHIPU.md`, seccion P1-MAISI).
   **MAISI CERRADO (2026-09-20, paso 0): descartado por diseno.** `scripts/sample.py` del bundle fija el rango en
   [-1000, 1000] HU; medido con `p1_maisi.py cota`, ese recorte solo ya da **42.24 HU de media en hueso** (11/34
   pacientes > 25 HU). No se corre la evaluacion en GPU. #93 CERRADA; tabla en `experiments/objetivo1/p1_maisi_cota.csv`.
2. **P2:** verificar en el codigo de XCIST si paciente y metal se proyectan juntos (#70).
3. **P3:** muestreador + SAP en `src/muestreador/` (en paralelo a P1).
Autora: laminas `e9ts_revision_laminas_autora.csv` 0/16; plazo de 2 semanas al revisor de #53.

## PUNTO DE RETOMA anterior (2026-09-15, historico)

> Escrito para que una sesion nueva, sin historial, retome sin releer nada mas. Todo lo de
> abajo esta verificado contra archivos en disco. Las decisiones son de la autora: Claude no
> las aplica sin orden explicita (reglas 3, 4 y 14 de `CLAUDE.md`).

### Donde esta el proyecto

- **Literatura cerrada por saturacion; el proyecto esta en fase experimental.** `src/` sigue
  **vacio**: todo lo ejecutable esta en `experiments/`. Segun #23, la entrega queda a unas 12
  semanas.
- **Cohorte por paciente (decision del 2026-09-10):**
  - 178 volumenes = 168 pacientes (`Grupo paciente` en `revision.csv`).
  - Volumenes fuera de uso: `experiments/exploration-3d/exclusiones.csv` (11; ningun archivo
    borrado).
  - Particion por objetivo: `grupos.csv` (grupo 1 con material ortopedico = 65, grupo 2 = 37,
    grupo 3 limpio = 66).
  - `metal_0059` y `metal_0071` estan unidos sin perdida en `data/derivados/`.
- **`tesis/main.tex` compila** (4 paginas, **43** referencias, 0 citas indefinidas). Cambios
  recientes:
  - R1 en 48/29 (`Field limitation`);
  - TS en el Objetivo 2, holgura #31 (1-2 mm) y parrafo `Corridor measurement on the local cohort`;
  - limpieza: "changed neither the transsacral corridor diameter nor its 10~mm viability";
  - `maintex_cifras.py` recalcula ese parrafo desde tablas versionadas: **12 de 12**.

### Lo que se midio (reproducible, en disco)

| Exp | Donde | Resultado vigente |
|---|---|---|
| E1 | `exploration-3d/sensibilidad_hu.py` | 2500 HU criba con 0 falsos negativos (113 candidatos) |
| Dup. | `exploration-3d/duplicados_parciales.py` | 6 grupos por SHA256 + 3 por cortes compartidos; todos resueltos por paciente |
| E6a / E6c | `objetivo1/` | Techo de 2000 HU de LW: 48 de 75 con metal fallan el Go/No-Go. `pub+MTW` (4a ventana) domina (#39) |
| R1 | `objetivo2/r1_*.py` | 65 pacientes: marco computable con S1 confirmado por revisor clinico **48**, sin contaminacion **29** (transcripcion corregida el 2026-09-14; ya en `main.tex`). Revisor: medico ORL, ciego; acuerdo con el agente kappa 0.81. Segundo juicio en ITK-SNAP (#53): planilla de 61 casos lista, **0 de 61 llenos** |
| E8 | `objetivo2/e8_*.py` | >= 17 de 65 con tornillo iliosacro; a 2500 HU los tornillos salen fragmentados (9/57) y con fuste de 5.1 mm (#46). Test-retest `0065`/`0066` |
| E9b | `objetivo2/e9b_*.py` | Alguna esfera de S1 con mediana < 150 HU en **38% con metal y 43% sin metal** (#48). **El brazo sin metal queda cuestionado por #50** |
| E9 | `objetivo2/e9_corredor.py` | **NO VALIDO**, no correr: el umbral HU no captura el esponjoso sacro (#48) |
| TS piloto | `objetivo2/ts_piloto.sbatch`, `ts_piloto_qc.py` | Job 51300, 2 casos x 2 recortes. Sin truncamiento; entre recortes Dice 0.93-0.97 con diferencias en SI/ala (#49). En `CLINIC_0002` las esferas de E9b caen un nivel arriba de la S1 de TS y las alas en tejido blando (#50) |
| TS cohorte | `objetivo2/ts_cohorte.sbatch` -> `ts_qc_cohorte.sbatch` (`ts_qc.py`) | **Completa y traida a la PC** (2026-09-13): jobs 51315 (358/358 ok) y 51316 (179 casos, 0 errores). Integridad verificada. Repetibilidad contra el piloto no exacta: 16 y 8 voxeles en `metal_0008` 6 mm (#49). Entrada: **`objetivo2/ts_cohorte.md`** |
| TS analisis | `objetivo2/ts_analisis.py` -> `ts_analisis.md`, `ts_nivel_s1.csv` | Nivel S1 de TS concuerda con el clinico en 57/57 (tras corregir la transcripcion de `metal_0012`); R1 falla el nivel en 7/60 de calibracion (#50). "Ala < 150 HU dentro de sacro/S1": 8% con metal, 15% sin metal (#48 decia 38/43%). Recorte ~5% de voxeles; 10 casos con cajas desplazadas 14-98 mm (#49). #51 cerrada: era transcripcion. Laminas: 12/197, revisadas por agentes |
| E9-TS | `objetivo2/e9ts_corredor.py` (51505; 3 mm: 51529) | 152 casos, 0 errores. Objetivo 2 (72 tras QC de nivel, #54): `D_TS` mediana 9.5 mm (IQR 7.4-11.7); viables a 10 mm 29/72 (6 mm) y 27/72 (3 mm). Grupo 1 con `ocupado_semimax`: 53.8% -> 40.4% en 52. Tablas versionadas en `objetivo2/` |
| E10 / E10b | `ts_componentes.py` (51522), `ts_cajas_limpias.py` (51527) | F = 0.001: `D_TS` y viabilidad invariantes para F hasta 0.05; quedan 4 cajas desplazadas > 10 mm (1 original, 3 creadas por la limpieza), declaradas (#49) |
| E6b | `objetivo1/e6b_vae_sd15.py` + `.sbatch` | **Cohorte completa y en la PC** (job 51540): 178 volumenes, 0 errores, control de identidad 873/873, 8.74 h. **Las tres configuraciones fallan el Go/No-Go de hueso en 178/178**, tambien con el decodificador oraculo (cota). El VAE de SD 1.5 sin reentrenar agrega 163-212 HU sobre codificaciones cuya identidad es 0.00 HU (#36/#39, ronda (7)) |

### Decisiones tomadas en esta ronda (todas en `01-decisiones.md`)

1. **Unidad = paciente:** duplicados parciales, union, `metal_0068` sin material ortopedico,
   ningun `.nii.gz` se borra.
2. **#20:** indice menor en las copias exactas.
3. **#41 via (c):** geometria parametrica, calibre de 6.5-8.0 mm, cilindro liso. **Contingencia
   abierta:** via (a), extraer de CLINIC-metal, **solo** si a futuro falta por completo
   bibliografia de calibres y longitudes. La falta de rosca o cabeza no la dispara.
4. **#31:** `Dmax >= d_implante + 2c`, `c` = 1-2 mm radiales (operacionalizacion declarada de
   Kaiser).
5. **#22:** 2500 HU solo para cribado; metal integrity con la regla adaptativa de Peters.
6. **#48/#49/#50 (2026-09-14):** TS `total` 2.18.0; recorte de 6 mm principal y 3 mm como sensibilidad (se
   reabre solo si las laminas muestran un fallo de 6 mm); E9b retirado.
7. **#52 (a + c), #35 cerrada, #54 opcion (a):** `ocupado_semimax` principal; F = 0.001 justificada por la
   invarianza de `D_TS` (decision 2026-09-14 (5)).
8. **#53 (2026-09-15):** el revisor clinico juzga los 61 casos con S1 en ITK-SNAP, ciego y en planilla aparte.

### PENDIENTES PARA LA PROXIMA SESION, por urgencia

1. **#36 + #39: VAE y ventanas, juntas. Bloquean el Objetivo 1**, que es obligatorio.
   - **E6b ya corrio y ya se analizo** con el criterio preinscrito: **SD 1.5 sin reentrenar no pasa**. La opcion 1
     de #36/#39 queda descartada por evidencia propia. Ver la ronda (7) de `04-implicancias.md`.
   - **Decision de la autora, pendiente:** opciones 2-5 de #36/#39. La 3 (otro VAE, con requisito de MAE de hueso
     < 25 HU) es la via principal; la 5 (revisar el umbral de 25 HU, solo con fuente) es nueva. Ninguna aplicada.
2. **Objetivo 2, cierre (sin decisiones de metodo pendientes):**
   - mandar al revisor `r1_revision_itksnap_revisor.csv` + `.md` + 61 CT (#53). Al volver: comparar con el
     mosaico y con TS; si cambia algun `ok`/`+1`, cambian 48/29 y 57/57 en `main.tex`;
   - revision de laminas de la autora: `e9ts_revision_laminas_autora.csv`, **0 de 16**. Un `fallo_6mm` reabre
     la decision 2026-09-14 (4).
3. **ABIERTAS de referencia:** #55 (cifras por clase de TS; regla F sin precedente, LiTS/KiTS19 en
   `_candidatos.md`) y #54 (discordancia de nivel sin juicio clinico en grupos 2 y 3; ya decidida la opcion a).
4. **Decisiones pequenas de la autora:** tercera regla de umbral para implantes reales (#22).
5. **Opcional, para blindar R1:** revision clinica de crestas y EIPS (heuristica sin revisar, declarado en
   `main.tex`).
6. **No urgente:**
   - revision de artefactos por la autora (#34, #35, #37; solo Objetivo 3);
   - candidatos PENDIENTE de `_candidatos.md`;
   - deuda: leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion.

### Avisos para quien retome

- **Memoria.** La PC tiene 11.8 GB y suele quedar con ~1.5-2 GB libres. Los scripts pesados
  corren por lotes reanudables (`--max`), en primer plano o con procesos nuevos por lote: dos
  corridas de fondo murieron por RAM. Lo que necesite GPU o modelos grandes va a **Khipu**.
  Host, carpetas, entorno, colas, limites, errores ya vistos y comandos estan en
  `experiments/objetivo2/KHIPU.md`: leerlo antes de escribir cualquier `.sbatch`.
- **Procedencia.**
  - `objetivo2/r1_auditoria_s1_clinico.csv`: medico ORL, **no la autora**.
  - `r1_auditoria_s1_agente.csv`: agente.
  - `revision.csv` solo se toca con scripts que verifican y respaldan (`procedencia.py`,
    `grupo_paciente.py`, `correcciones_autora.py`).
- **Historicos que no se usan:** `r1_landmarks.v1-parcial.csv`, `r1_landmarks.v2a.*`,
  `revision.pre-*.csv`.
- **Bibliografia:** `refs/raw` -> `refs/clean` -> `python scripts/build_refs.py` (regla 9). No
  editar `refs.bib` a mano.
- **Patron a vigilar (visto 6 veces):** un enunciado se vuelve verdad por citarse a si mismo, o
  un control que no puede fallar se toma por verificacion (#25, #37, #40, #45, #47, #50). En #50,
  el control de marco de E9b validaba el CT, no el nivel de S1. Verificar contra el archivo o el
  dato antes de construir encima.
- **TS:** `ts_piloto_qc.py` y sus CSV estan congelados como evidencia de #49/#50; para la cohorte
  se usa `ts_qc.py`, que reutiliza sus funciones. No cambiar `--task` ni `--roi_subset` en
  `ts_cohorte.sbatch` sin decision: el recorte depende de las clases pedidas (#49).
- `04-implicancias.md` es el archivo critico irreemplazable (regla 17). Llega hasta la #75 (ultima ronda:
  2026-09-16 (14), recomendaciones aplicadas y 11 fichas faltantes).

## Ultimo paso completado
2026-09-17 (ronda 15) — **la autora delega las decisiones al asistente en rol de asesor**; rechaza recortar el renderizador.
- Chen citado como preprint (Obj 1). Aplicadas en `main.tex` #57, #69-#75; ablaciones FUERA (`00-tesis.md` punto 10);
  brazo fisico sobre subconjunto reducido; **regla preinscrita**: si el VAE (preentrenado o con decodificador adaptado y
  encoder congelado) no pasa el Obj 1, no hay Obj 3. Compila: **6 paginas** (antes 5), 64 refs, 0 errores.
- Decision completa en `01-decisiones.md` (2026-09-17), incluidos los pendientes previos de este archivo.

**Siguiente (en orden):** P1 = afinar solo el decodificador del VAE de SD 1.5 en Khipu y evaluar con E6b (hueso, metal y
`B_delta`) en pacientes separados; P2 = verificar proyeccion conjunta en el codigo de XCIST; P3 = implementar el
muestreador + SAP en `src/muestreador/` (en paralelo a P1). Autora: laminas 0/16 (~1 h) y plazo de 2 semanas a #53.
**Pendientes que surgieron:** limite de paginas (6 pp.); `src/` sigue vacio.

## Paso anterior
2026-09-16 (ronda 14), **orden de la autora** — recomendaciones adoptadas y 11 fichas faltantes generadas.
- **`main.tex` APLICADAS #64 (a), #66 (a), #67 (limitacion) y #68 (a) + regla de borde SAP** `0 / (0,2) / [2,4] / (4,inf)`.
  Compila: 5 pp., 64 refs, 0 errores, 0 citas indefinidas. Decision 2026-09-16 escrita en `01-decisiones.md`.
- **#65 NO aplicada:** la autora espera el raw de las ACTAS de Chen (el de `refs/raw/` es el preprint arXiv); frase
  preparada en `01-decisiones.md`.
- **Re-verificaciones:** `zwingmann2009navigated` (grosor de corte NO ENCONTRADO; un radiologo; nivel del brazo navegado
  NO ENCONTRADO -> **#69**) y `peters2025hybrid` (proyeccion conjunta NO ENCONTRADO; fantoma no cubre el paso hibrido ->
  **#70**). Secciones "Verificacion 2026-09-16" al final de ambas fichas.
- **11 fichas nuevas** (todo raw sin ficha): abadi2019, dorjsembe2024, hu2023, kazerouni2023diffusionsurvey, li2024,
  rombach2022latentdiffusion, selles2024marreview, singhrao2024fiducial, yu2021, zhang2023controlnet y
  templeman1996proximity (solo abstract). **Ya no queda raw sin ficha.** `ziran2003` tiene PDF pero no raw (cadena del
  10 mm cerrada; no se leyo).
- **ABIERTAS nuevas #69-#75**, ninguna aplicada.

**Siguiente:** decision de la autora sobre #69 (S1 en brazo navegado; toca `main.tex:52` y `:78`), #70 (`main.tex:50`),
#71 (`main.tex:56`), #72 (`main.tex:48`, pocas palabras), #73, #74 (junto con #36/#39) y #75 (citar Rombach en la frase de
#66). Ejecucion pendiente: ROI `B_delta` en `e6b_vae_sd15.py` + Khipu.
**Pendientes que surgieron:** candidatos Szalkowski 2021 y Selles 2023 [140] (posible extension espacial, #57); verificar
cifras de Tabla I de `li2024` (imagen poco nitida); `kazerouni2023` y `zhang2023controlnet` leidos sobre preprint.

## Paso anterior
2026-09-16 (ronda 13) — **4 lecturas mas con `lector-papers`**: `mirza2003`, `fan2022`, `routt1997`, `macháček2023`
(fichas, filas en `_index.md`, `_candidatos.md` actualizado). **#68 NUEVA** (escala de 4 grados literal en Mirza, que la
declara heredada; `main.tex:52` dice "lettered" y omite ese eslabon; SAP sin regla de borde para 4.0 mm). #67
actualizada. `fan2022`, `routt1997` y `macháček2023` sin implicancia ABIERTA (registrado).

**Siguiente:** decision de la autora sobre #64-#68. Vaccaro 1995 Part II sube a N1 en `_candidatos.md` (unico nodo sin
leer de la escala). Verificacion menor: proyeccion conjunta paciente+metal en `peters2025hybrid`.
**Pendientes que surgieron:** quedan 11 PDF sin ficha, ninguno con riesgo alto (surveys, arquitecturas, MAR puros,
DukeSim, Polyp-DDPM, hu2023, singhrao2024).

## Paso anterior
2026-09-16 (ronda 12) — **4 lecturas con `lector-papers`**: `arand2019pelvicring`, `chen2026foundationvae`, `tejwani2014`,
`zhang2018` (fichas, filas en `_index.md`, candidatos en `_candidatos.md`). **#64-#67 NUEVAS** y #63 actualizada.
`main.tex`, `00-tesis.md` y `01-decisiones.md` sin tocar. #64: Arand citado como "bone density maps" sin mapa utilizable.
#65: Chen no refuta E6b. #66: E6b no mide la banda B_delta. #67: grosor de corte del CT vs benchmark Zwingmann.

**Siguiente:** decision de la autora sobre #64 (redaccion `main.tex:78`), #65 (frase en Related Work), #66 (ROI de banda
en E6b) y #67 (verificar protocolo CT de Zwingmann 2009). Mas urgente sigue siendo #36/#39 (VAE); MAISI entra como
candidata N1 para la opcion 3.
**Pendientes que surgieron:** protocolo de CT de `zwingmann2009navigated` no esta en su ficha (releer ese punto);
Wagner 2014 queda condicionada a #64.

## Paso anterior
2026-09-15 (ronda 11) — **2 lecturas mas, correcciones APLICADAS a `main.tex` y bibliografia regenerada**,
todo por orden explicita de la autora en el mismo turno.
- **`zwingmann2013.md` (N2 propuesto) y `lin2019.md` (N1 propuesto).** Fichas y filas en `_index.md`.
- **#62 NUEVA:** `zwingmann2009navigated` **no es independiente** de `zwingmann2013` — es su ref. 10 **y** su
  estudio primario n.o 19, y **entra con cero eventos en ambos brazos**, porque ahi "malposicion" significa
  revision. Prueba limpia de que tasa agregada y grado ordinal son constructos distintos. **Cierra la cadena
  del 2%-15%**, que el propio paper imprime como "2 to 15 %" y "0 to 15 %" con las mismas dos referencias.
- **#63 NUEVA:** `lin2019` (DuDoNet) **no prohibe** el renderizador en dominio imagen — es rendimiento, no
  imposibilidad, y ademas es REMOCION, que el paper llama *ill-posed*. #61 queda como falta de precedente.
- **`main.tex`: #56, #58, #59, #60 y #61 APLICADAS.** Compila: **5 paginas** (antes 4), **64 referencias**,
  0 citas indefinidas, 0 errores.
- **`refs.bib` 43 -> 64.** Se generaron los **21 `refs/clean/` que faltaban** desde su raw; `refs/raw/` intacto.
  Procedencia y decisiones, una por una, en `refs/MAPEO.md`. Ya no queda raw sin clean ni clean sin raw.
- **Correccion:** el reporte previo dijo que `deman1999` no tenia raw. Era falso (filtro `^title` que falla en
  los `.bib` de IEEE). Si es citable, y ya se cito.

**Siguiente:** decision de la autora sobre #62 y #63, y copiar a `01-decisiones.md` las cinco aplicadas si las
da por definitivas. **Lectura siguiente mas rentable: `zhang2018`** — es la fuente del protocolo de simulacion
de metal que `lin2019` reutiliza y omite, y **ya tiene PDF, raw y entrada en `refs.bib`**.
**Pendientes que surgieron:** (1) con `\nocite{*}` en `main.tex:139` las 21 altas entran a la bibliografia sin
citarse — solo 5 de las 21 se citan hoy; si debe listar solo lo citado, hay que quitar `\nocite{*}` (regla 14).
(2) `herman2016` apunta a dos versiones: `refs.bib` a la de revista (2017, 35(7):1478-1484), la ficha al
*Accepted Article*. (3) `tejwani2014` y `gottschling2009` van sin DOI: su raw no lo trae. (4) `macháček2023`
tiene clave no ASCII; compila, pero renombrarla es decision de la autora.

## Paso anterior
2026-09-15 (ronda 10) — **4 lecturas nuevas con `lector-papers`**, elegidas entre los 24 PDF de `papers/`
sin ficha. Fichas: `gertzbein1990.md`, `ramzan2026claim.md`, `herman2016.md`, `deman1999.md`.
Filas anadidas a `_index.md` (N1 Gertzbein; N2 los otros tres) y candidatos de snowballing a `_candidatos.md`.
- **#56 CERRADA EN EVIDENCIA** (sigue ABIERTA en decision): CLAIM era la cuarta fuente sin leer.
  Recuento final de la frase de `main.tex:48`: *"bounded inpainting"* 3/4, *"strictly inside the mask"* 2/4,
  **"implicitly assume non-rigidity" 0/4** — no lo enuncia ninguno de los cuatro PDF.
- **#58 NUEVA:** `gertzbein1990` publica **SEIS** tramos de 2 mm, no cuatro grados; los cortes de 6 y 8 mm no
  tienen justificacion declarada y su referencia anatomica es el pediculo, no el corredor iliosacro.
  Toca la atribucion de la escala del benchmark SAP/BFC en `main.tex:48` y amplia #4.
- **#59 NUEVA:** `herman2016` da 32% de malposicion por tornillo y **S1 36.5% frente a S2 14.8%**; tensiona el
  parrafo S1/S2. **No resuelve #32** (es 2D fluoroscopico, scale-invariant, sin Dmax).
- **#60 y #61 NUEVAS:** `deman1999` **no mide extension espacial del streak**, asi que el reclamo de novedad de
  B_delta sobrevive y **#57 sigue sin fuente externa**; abre el hueco del dominio imagen frente a proyeccion.

**Siguiente:** decision de la autora sobre #56 (opcion a), #58 (b+c), #59 (c), #60 (b o c) y #61 (b).
`main.tex`, `00-tesis.md` y `01-decisiones.md` sin tocar (reglas 4 y 14).
**Pendientes que surgieron:** `gertzbein1990` y `herman2016` tienen `.nbib` en `refs/raw/` pero **no estan en
`refs.bib`**; `deman1999` **no tiene raw** y hoy no es citable (regla 9). `herman2016` es version
"Accepted Article" sin paginacion de revista: elegir version antes de citar paginas (patron `isensee2021`).
Candidata mas fuerte de la ronda para leer: **Zwingmann 2013**, metaanalisis de malposicion por modalidad.

## Paso anterior
2026-09-14 (3):
- **#52 decidida (a + c)** y **#35 cerrada** por la autora. `grupos.py` regenerado: solo cambian `Regla` y
  `Estado regla`. Registradas en `01-decisiones.md` (2026-09-14 (2)) con orden de la autora.
- **E9-TS ahora calcula #52 (c):** politicas `hueso`, `ocupado_2500` (cota) y `ocupado_semimax` (propuesta #22).
  `metal_0008`, 6 mm: 11.3 -> 10.0 mm ocupado; 3 mm: 9.5 sin cambio. El resumen pone primero la cohorte del
  Objetivo 2 (grupos 2 y 3).
- **#53:** `r1_cortes_itksnap.py` -> `r1_cortes_itksnap.csv`, corte exacto del punto de S1 en el archivo original,
  para que el revisor lo abra en ITK-SNAP. Ciego, con comprobacion por HU.

**Lanzados en Khipu (2026-09-14, n006):** E10 = job 51504, E9-TS = 51505 (los dos en `R`), resumen = 51506
(espera a los dos). Cierre: `KHIPU.md`, "Noche automatica", pasos 3-5.
**Revision del cierre (2026-09-14, tarde):** E9-TS integro (152 casos, 0 errores, 2352 filas). **E10 INCOMPLETO:**
42/179 casos (`CLINIC_0001`-`0042`, solo dataset6), `ts_componentes_errores.csv` vacio (0 bytes: proceso matado sin
`finally`). Seccion 6 de `e9ts_resumen.md` NO sirve para fijar F. `sacct`: FAILED, ExitCode `0:9` (SIGKILL externo)
a los 6:47, MaxRSS 908 MB de 32G; no es tiempo ni memoria del job, y `CLINIC_0043` tiene tamano normal. Causa sin
confirmar (sospecha: E9-TS con 16 procesos en el mismo n006). Siguiente: `sacct`/`seff` de 51504 y 51505, cabecera
`Caso,Error` a mano en el CSV de errores, relanzar E10 solo (~10 s/caso) y regenerar el resumen.
**Relanzado:** E10 = 51522 (`R` en n006, sin E9-TS al lado), resumen = 51523 (`afterok`). GPUs revisadas: g002
(RTX A6000 48 GB) libre; `a-tesis` no limita `gres/gpu` (detalle en `KHIPU.md`, Colas y limites).
**2026-09-14 (4): E10 completo** (179 casos, 0 errores, rc=0, 16 min) y **E9-TS + E10 analizados**, traidos a
`outputs/e9ts/` y `outputs/ts_componentes/`. Implicancias: #49, #52 y #48 actualizadas; **#54 nueva** (la QC de nivel
excluye 18/91 del Objetivo 2, desigual entre grupos). Textos de decision y de `main.tex` propuestos en el chat, NO
aplicados. Siguiente: la autora decide F, politica de ocupacion principal y #54; luego, aplicar con orden explicita.
**2026-09-14 (5), con orden explicita de la autora:** decision 2026-09-14 (3) escrita en `01-decisiones.md` (F = 0.001,
`ocupado_semimax` principal, #54 opcion a). `main.tex`: TS en el Objetivo 2 y parrafo `Corridor measurement on the local
cohort`; compila, 4 paginas, 41 referencias, 0 indefinidas. `wasserthal2023` dado de alta (raw -> clean -> refs.bib,
MAPEO, `_index.md` N2 propuesto, ficha por `lector-papers`). **#55 nueva:** el paper no valida S1 ni metal. E10b listo
(`ts_cajas_limpias.py` + `.sbatch`, probado en local: control 8/8); comandos en `KHIPU.md`, seccion E10b.
Siguiente: correr E10b en Khipu y confirmar que F = 0.001 elimina los 10 desplazamientos; revisar laminas (36
componentes >= 1%, `CLINIC_0091`/`0078`); despues, Objetivo 1 (#36/#39, E6b en g002).
**2026-09-14 (6):** #55 actualizada con el README del repositorio TS que pego la autora: el paper es de la v1 (literal de
los autores); `vertebrae_S1` existe en `total`; Apache-2.0; piden citar nnU-Net; el recorte robusto es "better" segun
ellos (toca #49) y reconocen confusion de vertebras vecinas (toca #54). Opciones (a)-(d) en #55, sin aplicar.
**2026-09-14 (7), orden de la autora:** `main.tex` con los cuatro pendientes (post hoc, cota 2500 HU, desfase de la
publicacion de TS, cita nnU-Net `isensee2021`); compila, 4 paginas, 42 referencias. **La autora prefiere 3 mm como
recorte principal: PENDIENTE** (#49, ronda (6)); las cifras con 3 mm ya existen. Preparado y probado en local
`e9ts_3mm.sbatch` (laminas 3 mm + repetibilidad + resumen); comandos en `KHIPU.md`, "E9-TS con 3 mm". Falta: fila de
`isensee2021` en `_index.md` (ficha en curso), fuentes de la autora sobre 3 mm, correr E10b y E9-TS 3 mm en Khipu.
**Ficha de `isensee2021` hecha:** el PDF local es el **preprint arXiv 2020**, no el Nature Methods 2021 del raw (#55,
actualizacion). La cita de `main.tex` no depende de su contenido; falta el PDF publicado o decidir (#55 opciones a-c).
nnU-Net usa "componente mayor", no fraccion: la regla F no tiene respaldo bibliografico (se declara como propia).
**Detenido (2026-09-14):** la autora subio `falk2019` como el nnU-Net de Nature Methods 2021, pero el raw es Falk et al.
2019, "U-Net: deep learning for cell counting..." (otro articulo). No se proceso ni se corrigio nada; esperando el PDF
correcto como `papers/isensee2021.pdf` (#55, seguimiento).
**Resuelto:** la autora subio el PDF de Nature Methods y retiro `falk2019`. Ficha de `isensee2021` rehecha y verificada;
se mantiene que nnU-Net solo usa "componente mayor" (sin fraccion) y no tiene CT oseo ni metal. `main.tex` sin cambios.
LiTS y KiTS19 en `_candidatos.md` como posibles precedentes de F.
**E9-TS 3 mm corrido (51529):** repetibilidad IDENTICO frente a 51505 (2352 x 43); 152 laminas con 3 mm en
`outputs/e9ts_3mm/`. Objetivo 2 con 3 mm y F = 0.001: 9.35 mm (IQR 7.75-11.7), 27/72 viables. **E10b no llego a la PC**
(sin `outputs/ts_cajas_limpias/`). Siguiente: traer o correr E10b; la autora revisa laminas 3 mm y aporta la fuente
citable del recorte; luego, con orden, decision y `main.tex` a 3 mm.
**2026-09-14 (8): `ebraheim1993` leido** con `lector-papers`. Por decision de la autora, solo ficha: el raw queda sin
`clean/` y `refs.bib` sigue con 42 entradas. Es un reporte de un caso sin tasa, asi que no es fuente del 2%-15%; su
pitfall es la superposicion en la AP y no afecta SAP. Registrado en `_index.md` (N3 propuesto), `_candidatos.md` y #12,
sin implicancia nueva. De las 4 refs. de Hinsche faltan Routt 1997 y Templeman 1996, que no hacen falta para el alcance.
**2026-09-14 (9):** comandos de E10b entregados a la autora (sin cambios en `KHIPU.md`; meta de filas 2865 verificada
contra el script). La autora confirma que eligio 3 mm solo por el README: #49 actualizada, porque cambiar el principal
ahora seria post hoc. Recomendacion: mantener 6 mm y reabrir solo si E10b o las laminas muestran un fallo del recorte de 6 mm. Siguiente: correr
E10b, la autora decide #49 y despues el Objetivo 1.
**2026-09-14 (10):** decision 2026-09-14 (4) escrita en `01-decisiones.md` por orden de la autora: 6 mm principal y
3 mm como sensibilidad; `main.tex` sin cambios. **E10b analizado** (job 51527, rc=0, control 715/716 por la S1 vacia de
`metal_0053`). Con F = 0.001 quedan 4 desplazamientos: 1 original y 3 nuevos creados por la limpieza. Ningun cambio en
`D_TS`. Cae la justificacion escrita de F en la decision (3); #49 actualizada con opciones y recomendacion (a). Siguiente:
la autora decide la justificacion de F; revision de laminas; Objetivo 1.
**2026-09-14 (11):** decision 2026-09-14 (5) escrita por orden de la autora: se mantiene F = 0.001 y su justificacion
queda en la invarianza de `D_TS`; la seccion E10b de #49 queda CERRADA. Objetivo 2 sin decisiones pendientes de metodo.
Siguiente propuesto: cierre corto del Objetivo 2 (versionar tablas citadas, revision dirigida de laminas, #53) y despues
el Objetivo 1: E6b sin reentrenar (VAE de SD 1.5 sobre configuraciones de 3 canales) para decidir #36 + #39 juntas.
**2026-09-15:** por orden de la autora:
- **Tablas versionadas** en `experiments/objetivo2/` (e9ts_corredor, e9ts_resumen, ts_cajas_limpias y su control; hash
  identico). `maintex_cifras.py` las recalcula: **11 de 12** cifras de `main.tex` coinciden. La que no es "changed no
  measurement": en `CLINIC_0012` el corredor iliosacro izquierdo cambia 0.2 mm; texto propuesto en #49, sin aplicar.
- **Plantilla de revision de laminas** (16 casos) y su guia, `e9ts_revision_laminas.md`.
- **E6b preparado y probado en local sin modelo** (identidad 12/12 frente a E6c; con E6c alterado da 11/12; eco 12/12).
  Comandos en `KHIPU.md`, seccion E6b.

Siguiente: prueba corta y cohorte de E6b en Khipu; revision de laminas (autora); tabla de ITK-SNAP al revisor (#53);
decidir el texto de #49.
**2026-09-15 (2), orden de la autora:**
- **`main.tex`**: la limpieza "changed neither the transsacral corridor diameter nor its 10~mm viability"; compila, 4
  paginas, 42 referencias, 0 indefinidas. `maintex_cifras.py` da **12 de 12**.
- **#53**: el revisor mira los 61 casos; planilla ciega `r1_revision_itksnap_revisor.csv` (61 filas) e instrucciones
  en `.md`. La decision falta escribirla en `01-decisiones.md` (texto propuesto en el chat).

Siguiente: mandar la planilla, los .md y los 61 CT al revisor; E6b en Khipu; revision de laminas.
**2026-09-15 (3):**
- **Decision de #53 (61 casos)** escrita en `01-decisiones.md` por orden de la autora.
- **Prueba corta de E6b OK:** job 51539, ds001 (A6000), control 6/6, 182.8 s por volumen; cohorte estimada en ~8.8 h.
  Unica cifra vista, sin interpretar (n = 1): `pub`, hueso, `metal_0000`: identidad 156.6, VAE oraculo 222.7, regla 291.2 HU.

Siguiente: lanzar la cohorte de E6b (`KHIPU.md`, E6b, paso 4) y traerla; despues, analizar #36/#39.
**2026-09-15 (4):** `ESTADO.md` consolidado. PUNTO DE RETOMA puesto al dia (tabla con E9-TS, E10/E10b y E6b;
decisiones 6-8; pendientes rehechos) y borrado un "Siguiente" obsoleto de 51504-51506. Verificado en disco: sin
salidas de E6b en la PC, laminas 0/16 y planilla del revisor 0/61. Sin trabajo experimental nuevo.
`01-decisiones.md` sin cambios (no hubo decision nueva). **La autora decide esperar ITK-SNAP** para la frase
"confirmed the S1 level on every patient" de `Field limitation` (#53): se reescribe una sola vez, con el juicio
nuevo. `main.tex` sin cambios. Commit bloqueado por `ESTADO.md` sin stage: `git add docs/ESTADO.md`.

Siguiente: cohorte de E6b (lanzar o traer) y analisis de #36/#39; enviar la planilla al revisor; laminas. Al volver
la planilla: 48/29, 57/57 y la frase "confirmed" de `main.tex`.
**2026-09-15 (5):**
- **Fichas nuevas** (`lector-papers`) de `zhang2025diffboost` y `jacob2026lgesynthnet`. DiffBoost se **releyo sobre
  la version IEEE TMI** que subio la autora (raw `.nbib` -> `.bib` de IEEE; `clean/` y `refs.bib` sin cambios;
  `MAPEO.md` actualizado). Las otras 5 pedidas ya tenian ficha y no se releyeron. `_index.md` al dia (N2 propuesto);
  2 candidatos N3 en `_candidatos.md`.
- **#56 nueva:** la frase de `main.tex:48` ("bounded inpainting... non-rigidity... strictly inside the mask") no es fiel
  para DiffBoost y solo en parte para LGESynthNet; `ramzan2026claim`, citado en la misma frase, no tiene ficha.
  `main.tex` sin cambios.

**2026-09-15 (6):** candidatos de DiffBoost: Med-DDPM [35] agregado (N3); DiffuseExpand [36] a descartados. #56 con
recomendacion de asesor (leer CLAIM, afirmacion causal y no espacial, conservar DiffBoost, bajar "structurally fail") y
correccion: `main.tex:54` no reclama ControlNet. **#57 nueva:** "globally far beyond" frente a B_delta ~12 mm y titulo
"local". Pendiente de la autora: verificar las citas de DiffBoost y LGESynthNet contra el PDF (#56).

Siguiente: la autora decide #56 y #57 (recomendado: leer `ramzan2026claim`, luego una sola reescritura de `main.tex:48/54`);
prioridad por debajo de E6b.

**2026-09-15 (7): cohorte de E6b traida y analizada.** Job 51540: 178 volumenes, 0 errores, rc = 0, control de identidad
frente a E6c **873 de 873**, mediana 180 s/volumen, 8.74 h. Integridad completa. Contra el criterio fijado antes de ver
resultados, el VAE de SD 1.5 sin reentrenar **falla el Go/No-Go de hueso (25 HU) en 178/178 con las tres
configuraciones**, y tambien con el decodificador `oraculo`, que es cota inferior: el mejor volumen de la mejor
combinacion da 52.85 HU. Hallazgo de fondo: `LW20000` y `pub+asinh` tienen identidad **0.00 HU** y el VAE les agrega
**212.00** y **162.95** HU de mediana, dos ordenes de magnitud por encima del error de ventana de E6c (1-6 HU a 8 bits).
Elegir ventana no arregla el Objetivo 1 mientras el VAE sea este. **#36/#39 actualizada** (ronda (7)) con el efecto sobre
las cuatro opciones y una quinta nueva (revisar el umbral de 25 HU, solo si se justifica con bibliografia).
`main.tex`, `00-tesis.md` y `01-decisiones.md` sin cambios (reglas 3 y 14).

**Busqueda de respaldo para #36/#39, solo sobre fichas ya escritas (sin PDFs nuevos, sin buscar fuera):** el umbral de
25 HU **si tiene con que anclarse**. `peters2025hybrid` (2.5, p.5) y `haneda2025aapm` (Sec. 2.3, p.6) definen *CT number
accuracy* como RMSE contra ground truth, con el mismo umbral de hueso de 150 HU; NMAR, el ancla de la escala AAPM, da
RMSE 20.2 (karageorgos, Tabla I, p.28) y el mejor latente publicado 12.74 (yun, Tabla 1, p.10). 25 HU queda justo encima
de NMAR: se justifica, no hace falta bajarlo (desactiva en gran parte la opcion 5). **Problema nuevo: E6b reporta MAE y el
campo publica RMSE**; no son comparables de frente, y el CSV solo guarda MAE. Candidato de VAE con cifra de HU: uno,
indirecto, el **CVQ-VAE x4 de MLD-MAR** (`yun2026simulationdriven`, ref. 23 = Zheng y Vedaldi 2023). Registrado en
`04-implicancias.md` (#36/#39, hallazgos 1-6) y en `_candidatos.md`, seccion "Candidatos de AUTOENCODER" (3 filas; Esser
VQGAN rehabilitado tras estar descartado).

**2026-09-15 (8), orden explicita de la autora:**
- **Umbral de 25 HU anclado y citado.** Decision escrita en `01-decisiones.md` (2026-09-15 (2)): se **mantiene** 25 HU y
  se cita. `main.tex` editado en los dos sitios donde vivia la cifra (Objetivo 1 y fila `Representation Viability`):
  ROI de hueso sobre el umbral de 150 HU del protocolo adoptado, declaracion de que **no existe umbral publicado de
  pasa/no-pasa**, y ancla en NMAR 20.2 HU / imagen 12.3 HU (`karageorgos2024ddpm`) / latente 12.74 HU
  (`yun2026simulationdriven`). **La discrepancia RMSE vs MAE se declara en el texto.** Compila: 4 paginas, 42
  referencias, 0 citas indefinidas. `refs.bib` SIN CAMBIOS (las 4 claves ya estaban; regla 9 respetada).
- **Busqueda web autorizada** (excepcion declarada al flujo de bibliografia; nada entro a `refs.bib`). Resultado:
  el hueco se **confirma** desde fuera (DM4CT no separa la primera etapa y no usa HU), y aparece
  **`Foundation VAEs for 3D CT` (ICML 2026, arXiv:2605.30893)**, que hace la pregunta de E6b y da la respuesta
  contraria con siete VAE de video congelados. Diferencia probable: recortan a **[-1000, 1000] HU**, fuera del rango
  de hueso denso y metal. **Sin verificar.** Es la lectura de prioridad 1. Tres filas en `_candidatos.md`.
- **Opcion 5 de #36/#39 cerrada en la practica**: el umbral no se baja, se justifica.

**2026-09-15 (9), orden de la autora:**
- **`papers/chen2023foundation.pdf` VERIFICADO: es el correcto.** Es *Foundation VAEs for 3D CT...* (arXiv:2605.30893v1,
  ICML 2026), **no** *Towards Generalizable Tumor Synthesis* (que es `chen2024tumorsynthesis`, CVPR 2024). Comparten
  autores (Qi Chen, Yuille, Zhou), de ahi la confusion. **Lo que si esta mal es la clave: dice 2023 y el paper es 2026**,
  y no hay `refs/raw/` para el. Pendiente de la autora: renombrar y pegar el raw (sugerencia `chen2026foundationvae`).
- **E6b reporta ahora MAE y RMSE** (`e6b_vae_sd15.py`). Columna de MAE sin sufijo (no rompe el control ni las corridas
  viejas); RMSE con sufijo ` rmse`; CSV de 32 a **56 columnas**; informe con tablas de las dos metricas y Go/No-Go por
  metrica. Probado en local con `--vae identidad`: control **12/12**, RMSE >= MAE en 24 de 24 pares, y el informe de la
  cohorte vieja se regenera con control **873/873** y MAE identico. Sin regresion. `KHIPU.md` actualizado; comandos sin
  cambio.
- **Hallazgo:** para `pub`, MAE y RMSE no dan lo mismo (2 volumenes de prueba: MAE 2.02 frente a RMSE 53.30 en hueso).
  El techo de 2000 HU satura pocos voxeles con error enorme y MAE lo diluye. `LW20000` y `pub+asinh` dan 0.00 en las
  dos. La metrica **no es neutral: penaliza a la configuracion con techo**, que es el tema de #39. Solo 2 volumenes,
  sin VAE: no se interpreta mas.

**2026-09-15 (10), orden de la autora:** `chen2026foundationvae` **dado de alta y cerrado**. `refs/clean/` +
`build_refs.py` -> **43 entradas**; `MAPEO.md` con fila de procedencia y nota. Decision 2026-09-15 (3) escrita en
`01-decisiones.md`: se cita **el preprint de arXiv** con dos excepciones declaradas (se conservan `eprint`,
`archivePrefix` y `primaryClass` contra la regla 7 de MAPEO, porque son el unico localizador; y se cita como
preprint un trabajo aceptado en ICML 2026). Se reabre solo si el paper llega a citarse en `main.tex`. **`PMLR 306`
no se usa en ninguna parte:** sale solo del pie del PDF y no se confirmo contra el editor. `main.tex` **sin editar**
(no lo cita); el PDF pasa de 42 a 43 referencias por `
ocite{*}`. **E6b RMSE corriendo en Khipu** (prueba corta
51591; el `tail` fallaba solo porque el job estaba en cola, ya documentado en `KHIPU.md`).

Siguiente: **rehacer la cohorte de E6b en Khipu** (~8.8 h; el CSV viejo no tiene las columnas `rmse` y no se pueden
reconstruir). Leer `Foundation VAEs` con `lector-papers` para confirmar el recorte a [-1000, 1000] HU: si se confirma,
es el mejor argumento a favor del encuadre de la tesis; si no, contradice a E6b y hay que responderlo. Despues, probar
el CVQ-VAE reusando E6b. En paralelo, sin bloqueo: planilla de ITK-SNAP al revisor (#53), revision de laminas (0/16),
y #56/#57.

## Paso anterior
2026-09-14 (2):
- **`main.tex` pasa a 48/29** por orden de la autora; compila, 4 paginas.
- **E9-TS listo para la noche:** `e9ts_corredor.py` + `.sbatch`, `e9ts_resumen.py` y `noche_e9ts.sh`, que lanza
  E10, E9-TS y el resumen con dependencias. Calcula recorte x limpieza para los 152 casos con S1 y no decide nada.
  Probado en `metal_0008`: 35 s; D_TS 11.3 (6 mm) / 9.5 (3 mm).
- Recomendaciones registradas en #52 (opcion a, con #35) y #53 (texto de "confirmed").

Siguiente: la autora sube y lanza (`KHIPU.md`, "Noche automatica"). Por la manana, `data/e9ts/e9ts_resumen.md`; luego
decidir F, #52/#35 y el texto de #53.

## Paso anterior
2026-09-14: **#48, #49 y #50 decididas y registradas** en `01-decisiones.md` (asesoria del 2026-09-13, literal, por
orden de la autora). **Transcripcion de R1 corregida:** `metal_0012` = `+1` (lo corrigio la autora) y `metal_0015` = `?`.
Con eso R1 queda en **48/29** (`main.tex` sigue diciendo 49/30, sin aplicar), TS/clinico 57/57 y **#51 cerrada**. La
lista del segundo revisor tiene 15 casos (#53). **E10 preparado y probado en local** (`ts_componentes.py` + `.sbatch`,
manual en `KHIPU.md`).
Siguiente: lanzar E10 en Khipu; la autora decide #52 y la orden para 48/29 en `main.tex`; despues, E9 sobre TS.

## Paso anterior
2026-09-13 (2): **cohorte TS analizada** con `experiments/objetivo2/ts_analisis.py`, que genera `ts_analisis.md` y
`ts_nivel_s1.csv`. TS como detector de nivel: concuerda con el clinico en 56 de 57; R1 falla el nivel en 7 de 60 de
calibracion. Tabla de #50 rehecha: "ala < 150 HU dentro de sacro/S1" da 8% con metal y 15% sin metal (antes 38/43%).
Recorte: ~5% de voxeles y 10 casos con fragmentos desplazados. #48, #49 y #50 actualizadas; **#51 nueva**
(`metal_0012` contradice la cifra 49/30 de `main.tex`). Laminas: 12 de 197, revisadas por agentes.
Siguiente: decisiones de la autora (#48, #49, #50, #51), luego rehacer E9 sobre las mascaras de TS con limpieza de componentes.

## Paso anterior
2026-09-13: **cohorte de TotalSegmentator completa, en la PC y verificada; sin analizar.** 358/358 corridas TS y
QC de 179 casos sin errores; la QC reproduce el piloto. Repetibilidad no exacta (#49, actualizada).
Entrega para el analisis en `experiments/objetivo2/ts_cohorte.md`.
Pendiente que surgio: 32 filas de `sacrum` sin techo (resuelto en parte el 2026-09-13 (2): 12 de 16 casos explicados).

## Paso anterior
2026-09-12 (cierre): **piloto de TotalSegmentator ejecutado y analizado; scripts de la cohorte listos.**
- Piloto: job 51300 (ag001, MIG A100 `3g.20gb`; TS 2.18.0; torch 2.14.0+cu130), 2 casos x {3 mm, 6 mm},
  59-76 s por corrida. Antes fallaron 3 jobs, por la cola y por un bug del script; los dos
  problemas estan documentados en `KHIPU.md`.
- QC (`ts_piloto_qc.py`, `ts_piloto_qc*.csv`, laminas en `outputs/ts_piloto_qc/`): #49 ampliada con
  evidencia; **#50 nueva** (error de nivel de S1 -> "ala < 150 HU" en tejido blando; 6 de 6 casos +1).
- Cohorte: `ts_cohorte.sbatch` (179 volumenes x 2 recortes, reanudable, control de repetibilidad
  contra el piloto) y `ts_qc_cohorte.sbatch` + `ts_qc.py`. Manual en `experiments/objetivo2/KHIPU.md`.
  **Lanzados el 2026-09-12:** TS = job 51315 (ag001, `R`); QC = job 51316 (`big-mem`, espera a 51315).
Siguiente: cierre de 51315/51316 (KHIPU.md, pasos 5-6). Luego, sesion manual de QC y decisiones #48/#49/#50
(PENDIENTE 1).

## Paso anterior
2026-09-12: preparados (no ejecutados) los comandos para correr TotalSegmentator 2.18.0 en Khipu
(`khipu.utec.edu.pe`, particiones `debug-gpu`/`gpu`, `--gres=shard:1`; pesos en el nodo de acceso,
porque los nodos GPU no tienen internet). Solo falta subir `data/derivados/...union.nii.gz`: los 178
originales ya estan en Khipu. #49 nueva (version, `total_v3`, modelo de recorte).
Siguiente: la autora corre el piloto (`metal_0008` + `CLINIC_0002`), valida y decide #48/#49.

## Paso anterior
2026-09-11 (cierre): #31 y #22 decididas y registradas; cifra de R1 escrita en `main.tex`; E9
(corredor) pilotado y **declarado no valido** por segmentacion (#48); E9b mide esponjoso de S1 bajo
150 HU en ~40% de los pacientes, con o sin metal; con y sin los 7 de FOV da lo mismo en densidad.
Siguiente: decidir la via de segmentacion (#48/#29, Khipu) y #36+#39. Detalle en PUNTO DE RETOMA.

## Paso anterior (2026-09-10 / 11, detalle)
2026-09-10: **R1 y E8 ejecutados enteros, y barrido de duplicados parciales.** #26 con cifra
provisional (52/69 marco computable con S1 correcto, 33 sin contaminacion; FOV y heuristica
pesan mas que el metal). #45 nueva: `metal_0059`/`0071` son el mismo estudio (contradice la
decision del 2026-09-07), mas `0011`/`0034` y `CLINIC_0038`/`0090`. #46 nueva: la via (a) de
#41 no produce geometria por umbral. #21: `metal_0068` sin osteosintesis densa.
Cierre del 2026-09-10: la autora **confirma** mismo paciente en los tres pares de #45, que
`0065`/`0066` son la misma persona y que `metal_0068` no tiene material ortopedico. Queda en
#45 una propuesta por par: contenedor, union sin perdida o par de reproducibilidad. Con
ella, dataset7 con osteosintesis pasa a 71 volumenes y 65 pacientes. Tambien hay texto
propuesto para `01-decisiones.md`, sin aplicar.
**Aplicado por orden de la autora:** union sin perdida de `0059`/`0071` en `data/derivados/`
y `Grupo paciente` lleno: 178 volumenes, 168 pacientes; dataset7 con osteosintesis 71/65,
dataset6 sin objeto 70/69.
**Cierre final del 2026-09-10 (orden de la autora):** decision por paciente escrita en
`01-decisiones.md`; `exclusiones.csv` creado (11 volumenes, ningun archivo borrado);
`metal_0068` corregido; `grupos.csv` regenerado (65/37/66); R1 y E8 recontados por paciente:
marco computable con S1 correcto 51/65, sin contaminacion 32/65; >= 17 con tornillo
iliosacro; fuste 5.08 mm.
#20 CERRADA por la autora (indice menor). Mosaicos regenerados sobre 65 pacientes y
plantilla ciega `experiments/objetivo2/r1_auditoria_s1_clinico.csv`.
2026-09-11: la plantilla de S1 la lleno un **medico cirujano ORL** (revisor clinico externo,
no la autora). Con el como referencia: **49/65** marco computable con S1 correcto, **30/65**
ademas sin contaminacion; acuerdo con el agente kappa 0.80. #20 escrita en `01-decisiones.md`.
2026-09-11 (2): **#41 via (c) APLICADA** en `01-decisiones.md` y `main.tex` (Objetivo 2,
regla de aislamiento, parrafo `Implant geometry source`; compila). **Contingencia (a)
ABIERTA:** extraer geometrias de CLINIC-metal si a futuro falta por completo bibliografia
con calibres y longitudes (no la disparan rosca, canulacion ni cabeza). Plantilla renombrada
por la autora a `r1_auditoria_s1_clinico.csv`. Lectura de `xie2024` (#47) lanzada.
Xie leido (#47): cita de C1 PARCIALMENTE respaldada (sobrecobertura solo en cortes simulados;
direccion dependiente del umbral); redaccion alternativa de C1 propuesta, sin aplicar.
Por orden de la autora: `grass2016`, `lee2014`, `wagner2017` y `zhao2012` anadidas a `refs.bib`
(36 -> 40, MAPEO actualizado; tesis compila: 4 paginas, 0 citas indefinidas, 2 avisos ya
conocidos) y `00-tesis.md:114` pasa de 'CAD propia' a geometria parametrica.
C1 reescrita en `main.tex:54` por orden de la autora; **#47 CERRADA**.
Siguiente: FOV del Obj 2 (7 pacientes sin crestas); cifra de R1 (49/65, revisor clinico) en
`main.tex:115`.

## Paso anterior
2026-09-09 (cierre real): **#40 RESUELTA y #41 abierta, y es lo mas grave de la sesion.**
La autora identifico el origen del "banco de 61": es la cita de `liu2021ctpelvic1k`,
Data annotation p. 3, *"The remaining 61 metal-affected CTs ... left unannotated"*.
Confirmado contra la ficha ya verificada y contra la Tabla 1 (`0(61)/0/14`), y contra el
disco: **61 + 14 = 75 = dataset7**. `CLAUDE.md:23` encadena dos errores de categoria:
CT de pacientes leidos como geometrias de implante, y dataset publico de terceros leido
como "insumo propio". **#41: C1 se queda sin insumo.** No existe ninguna fuente de
geometrias de implante en el repositorio, y con eso el Objetivo 2 (unico aporte propio del
minimo viable) no tiene que colocar, **#31 colapsa** (`d_implante` no existe), `main.tex:111`
regula un banco inexistente y `00-tesis.md:114` habla de un CAD propio que no hay.
Opciones ejecutables con lo que hay en disco: (a) extraer geometrias de los implantes de
los 75 CLINIC-metal, con la tension de aislamiento que eso implica, o (c) geometrias
parametricas con los rangos publicados de #30 y #31. Propuesta de correccion de
`CLAUDE.md:23` redactada en #40, sin aplicar.
Precision: 1184 y 75 son cifras del propio paper de 2021 (Introduction p. 2 y Tabla 1
p. 3), no una actualizacion posterior. **#40 CERRADA el 2026-09-09**: la autora retira su
observacion sobre el dataset y confirma que el estado de ANOTACION de los 61 no ha
cambiado y que la lectura de la evidencia textual era correcta. Sin efecto sobre #13
(siguen 14 de 75 anotados) ni sobre #41, que sigue ABIERTA.
Siguiente: la autora decide #41 (de donde salen las geometrias) — es ahora el bloqueo
numero uno del alcance minimo, por delante de #37, #39 y #36.

## Paso anterior
2026-09-09 (cierre): **E6a ejecutado** y **bloqueo declarado por pedido de la autora**.
E6a mide el tramo `HU -> ventana -> HU` del Objetivo 1 (sin VAE, cota inferior de
cualquier decodificador). Dos hallazgos: **#38**, las tres ventanas publicadas son
**redundantes en reconstruccion** (`max |LW - oraculo|` en hueso a float = **0.0 exacto**;
la unica ganancia es 1.679 HU a 8 bits, o sea cuantizacion, no rango) — no refuta C3, pero
si refuta que la multi-ventana **preserve mejor los HU**; y **#39**, el Go/No-Go
**no puede fallar** en pelvis limpia (mediana **0.00 HU**) y **falla en 48 de 75** con
metal (mediana 46.36, max 274.49), antes del VAE, solo por el techo de 2000 HU de LW.
En ROI de metal el MAE es **3588.80 HU** de mediana, con HU maximo mediano de 18 822 y
pico 24 970 contra un techo de 2000: **la representacion no puede codificar lo que la
tesis debe generar.** `main.tex` no declara sobre que cohorte se evalua el Objetivo 1.
**Bloqueo declarado:** #15, #22, #34 y #35 detenidas hasta que la autora marque artefactos.
Afecta solo la cohorte del Objetivo 3; Obj 1 y Obj 2 siguen libres.
Antes tambien: **#34 corregida por procedencia** (la columna `Artefactos` la llenaron los
agentes desde laminas, no la autora; sus 20 `no` son afirmaciones de ausencia fragiles),
**#35** (una cohorte para tres consumidores), **#36** (el VAE del Obj 1 no esta
especificado en ningun documento) y **#37** (`revision.csv` no declara procedencia por
campo).
Siguiente: la autora decide **#37 primero** (procedencia por campo) y luego hace la
revision visual de estriacion sobre los 33 volumenes de dataset6 con objeto. En paralelo,
decidir #38/#39 (que hacer con el techo de 2000 HU) y #36 (que VAE). Sigue sin ubicarse el
banco de 61 geometrias.

## Paso anterior
2026-09-09: **primer experimento del giro a benchmarks (E1)**. Corrido
`experiments/exploration-3d/sensibilidad_hu.py` sobre los 178 volumenes locales (solo
lectura; `revision.csv` intacto). **#22 EJECUTADA**: 1500 HU deja 177 de 178 como
candidatos y **queda descartado** (entra hueso cortical); 2500 HU da 113 candidatos, 65
limpios y **cero falsos negativos** contra la revision 3D de la autora; 3500 HU da 104
candidatos y 74 limpios pero **pierde 5 metales reales**. Cambios de clase: 64 de 1500 a
2500, 9 de 2500 a 3500. Las 178 clasificaciones a 2500 reproducen exactamente
`revision.csv`. **#34 nueva**: los 5 que pierde el 3500 son los cinco `accesorio`
extracorporeos de dataset6, asi que el umbral y la definicion de `Objeto extraño` son la
misma decision (2500 -> 65 limpios; 3500 -> 74 limpios). Ademas, analisis de prioridad de
las 34 implicancias y cola de experimentos E1-E6 propuesta.
Siguiente: **E6, el Go/No-Go del Objetivo 1** (MAE < 25 HU en hueso del round-trip
multi-ventana), que no tiene ningun bloqueo. Antes de E2 y E3 hacen falta tres decisiones
de la autora: adoptar o no TotalSegmentator (#29), donde esta el banco de 61 geometrias
(NO esta en `data/`, que solo tiene dataset6 y dataset7), y si se adopta la formulacion
parametrica `Dmax >= d_implante + holgura` (#31).
Aviso de estado del repo: `docs/04-implicancias.md`, `refs.bib` y `tesis/main.pdf` siguen
modificados sin commitear desde el 2026-09-08, mas 15 `refs/raw/*` sin trackear.

## Paso anterior
2026-09-08: cerrada la seccion "la geometria que McLaren NO publica" con 7 lecturas
(`grass2016`, `wagner2017`, `lee2014`, `hasenboehler2011`, `zhao2012`, `mendel2011`,
`gottschling2009`). La geometria SI existe pero en marcos que no componen (#30); Gras y
Wagner se invierten el orden S1/S2 por definicion distinta de diametro (#30b, corrobora
#12 y #27); el umbral es siempre calibre de tornillo mas holgura en 7 fuentes, lo que
habilita expresarlo como `Dmax >= d_implante + holgura` sobre el banco de 61 (#31);
Gottschling es de femur y tibia (#32); el "hasta 50%" de dismorfismo no lo sostiene
ninguna de las tres fuentes citadas (#33). Busqueda de corredor: **cerrada por saturacion**.
Decision de la autora: cerrar **tras** dos lecturas finales (`carlson2000`, `ebraheim1997`),
y cierre **reversible** si los experimentos revelan que falta geometria. **Ebraheim leido**
(pediculo S1 en mm, entrada a 3-3.5 cm del borde posterior del ilion, margen 4-6 mm entre
dos tornillos; sin angulos, sin S2; septimo marco incompatible, #30 ampliada).
**Carlson BLOQUEADO: falta el PDF y el raw.** Unica candidata de reapertura anotada:
Morse 1994, angulos para tornillo sacro sobre TC preoperatoria.
Siguiente (decidido por la autora): cerrar los tres pendientes de datos — cifra de R1 (#26),
tabla de sensibilidad HU 1500/2500/3500 (#22) y representante de los 3 grupos duplicados
(#20, que bloquea el split). Todo sobre datos ya en disco.

## Paso anterior
2026-09-08: evaluado TotalSegmentator para el Objetivo 2 (#29 ABIERTA). Es util como
ROI/mascara anatomica inicial (`sacrum`, S1, caderas), no entrega S2, cortical, landmarks
ni corredor y no esta validado aqui bajo metal. Recomendado piloto 1.5 mm + QC local;
pendiente decision de adopcion. No cambia SAP ni downstream.

## Paso anterior
2026-09-08: Keating 1999 leido con `lector-papers` desde DOCX completo sin paginacion.
SI publica malposicion en 5/38 pacientes (13%): fuente indirecta via Hinsche y punto
interior, no origen del rango 2%-15% ni de sus extremos. Binario, radiografico, sin
S1/S2 ni escala SAP; #12 no se reabre. `refs.bib` = 36; tesis recompilada sin citas
indefinidas. Siguiente: sensibilidad HU y #26.

## Paso anterior
2026-09-08: Gardner incorporado como respaldo anatomico S1/S2 en `00-tesis.md`,
`01-decisiones.md` y `main.tex` (Problem Statement y Objetivo 2), por encargo de la autora.
Se mantiene geometria individual sin fenotipos y benchmark ordinal SAP solo en S1.
PDF recompilado: 4 paginas, sin citas indefinidas. Siguiente: sensibilidad HU y landmarks (#26).

## Paso anterior
2026-09-08: auditada consistencia de Gardner contra su ficha ya leida. Corregidos
candidatos, indice, ficha e implicancias: LEIDO; areas S1/S2 similares en dismorficos,
no inversion ni prior ordinal. Sin cambio de alcance: geometria individual sin fenotipos;
SAP clinico solo S1. Siguiente: sensibilidad HU y landmarks (#26).

## Paso anterior
2026-09-08: van den Bosch leido con `lector-papers`; 6/31 vs 1/49 son pacientes con
quejas neurologicas, no malposicion por nivel. #28 resuelta; #12 cerrada delimitando
SAP ordinal a S1 por tecnica, S2 descriptivo. Aplicado en tesis y alcance; 35 referencias.
Siguiente: sensibilidad HU y landmarks (#26). Prior ordinal clinico S2 sigue no disponible.
Validacion: PDF recompilado, 35 entradas y ninguna cita indefinida; dos avisos BibTeX
ya documentados por revistas sin volumen (Hinsche y Templeman).

## Paso anterior
2026-09-08 (cierre): auditada entera la cadena de citas del umbral de 10 mm con tres
lecturas mas (`ziran2007fluoroscopic`, `moed2006s2screw`, `gardner2010safezones`).
**Cuatro eslabones, ninguno lo mide**: Ziran no contiene el umbral, el "1 cm" de Moed es
separacion interforaminal (otra magnitud), Kaiser lo elige y Gardner lo declara como
consenso por calibre de tornillo. Conclusion: **nunca fue una medicion, es una convencion
profesional**, y la tesis lo afirma con frases literales. Cadena declarada agotada.
Decisiones de la autora aplicadas: **no estratificar por fenotipo** (#27 CERRADA, y con eso
la objecion de Carlson 2000 deja de aplicar); la geometria en pelvis intactas se reescribe
como **limitacion del campo** en `main.tex`; se anade el respaldo **anatomico** de C2 con
los coeficientes de variacion de Ziran (hasta 97-140%); se adopta la **tabla de
sensibilidad** de cribado a 1500/2500/3500 HU; Ziran queda N2 y Moed baja a **N2
provisional**. `refs.bib` = 34. 16 decisiones fechadas en `01-decisiones.md`.
**#28 nueva**: van den Bosch preparado con el encargo completo redactado y SIN ejecutar.
Siguiente: conseguir el PDF de van den Bosch (decide el eje S1/S2 y puede cerrar #12),
correr la tabla de sensibilidad y la cifra de R1 (#26). Ambas sobre datos ya en disco.

## Paso anterior
2026-09-08 (tarde/noche): la autora adopto las opciones recomendadas y autorizo
aplicarlas. **APLICADO** en `tesis/main.tex` (RQ e hipotesis sin downstream, Obj 5
eliminado con parrafo `Explicitly out of scope`, Obj 4 con SAP como unica metrica propia
y metricas de Peters con sus nombres, C3 reescrita, el rango 31-60% sustituido por las dos
distribuciones ordinales de Zwingmann condicionadas por tecnica y nivel sacro, zona segura
via McLaren con el umbral declarado heredado), en `docs/00-tesis.md` (`Fuera de alcance`
escrito con seis puntos) y en `docs/03-glosario.md` (escrito entero). Compila limpio, 31
entradas. **#14 y #16 CERRADAS**; #13 y #18 degradadas a limitacion declarada.
Alta y lectura de `kaiser2014dysmorphism`: **no** establece el 10 mm (tercer salto de
cita, hacia Gardner 2010 / Ziran 2007 / Moed 2006), pero aporta el marco de referencia
calculable (reformateo perpendicular al platillo de S1, angulo coronal vs crestas iliacas,
angulo axial vs espinas iliacas posteriores, margen cortical de 5 mm, tres fenotipos).
**#26 nueva**: Kaiser midio en pelvis SIN implante y excluye los CT con metal.
Siguiente: la autora decide sobre las cinco propuestas de Kaiser (a-e), y falta que
recoja en `01-decisiones.md` las seis decisiones ya aplicadas.

## Paso anterior
2026-09-08: alta de 3 fuentes (`mclaren2021corridor`, `hinsche2002fluoroscopy`,
`templeman1996proximity`) y llegada del PDF de `wang2025adaptiveweighting`. `refs.bib`
regenerado a 30 entradas. Tres lecturas con `lector-papers`. Resultado: **#1 CERRADA**;
**#2 confirmada** contra el cuerpo; **#7 pasa a PARCIALMENTE CUBIERTA** (McLaren da
umbral y procedimiento, no geometria parametrizada); **#12 agravada** (el 2-15% es cita
de tercera mano y Hinsche es banco sobre plastico); **#13** con tres datos cruzados;
**#24 nueva** (el respaldo de C3 es fuente secundaria y el mecanismo es cascada, no
codificacion de entrada); **#25 nueva** (patron sistemico: tres anclas cuantitativas son
citas heredadas). Decision de la autora tomada: adoptar metricas de Peters, Obj 5 fuera
de alcance, Obj 4 modificado; falta registrarla en `01-decisiones.md` y aplicarla.
Siguiente: que la autora elija opciones en #7, #12, #24 y #25, y decida el nivel de
McLaren (ficha dice N2, `_index.md` dice N1).

## Paso anterior
2026-09-07: cerrados tres pendientes abiertos por orden de la autora.
(1) **LNCS: se ignoran.** La tabla con los volumenes retirados salio de `refs/MAPEO.md`;
en su lugar queda la decision de no perseguirlos, sin los valores, para que nadie los
reintroduzca sin respaldo en `refs/raw/`. (2) **`.gitignore` limpio**: se quitaron el
`@'` inicial y la linea `'@ | Set-Content ...` final; las reglas se verificaron con
`git check-ignore` (`papers/`, `data/`, `*.nii.gz`, `*.bbl`). (3) **`main.tex` migrado a
BibTeX**: `natbib` con `abbrvnat`, `\bibliography{../refs}` y las 19 citas del cuerpo
convertidas a `\citep`/`\citet`/`\citealp`. La lista en texto plano (27 entradas a mano)
desaparecio; ahora sale de `refs.bib`. Compila limpio, 0 citas indefinidas, 27 entradas
en el `.bbl`, y las citas del cuerpo se imprimen igual que antes.
Siguiente: cerrar el representante de los 3 grupos internos de dataset7.

## Paso anterior
2026-09-07: montado el pipeline bibliografico `refs/raw` -> `refs/clean` -> `refs.bib`
por encargo de la autora. 27 fuentes del editor (16 nbib de PubMed, 10 bib, 1 txt),
27 entradas normalizadas en `refs/clean/`, procedencia y reglas en `refs/MAPEO.md`,
regeneracion con `scripts/build_refs.py`. Los 27 DOIs y las 27 claves quedaron
identicos; se corrigio `issue`->`number` en tres entradas (fasciculo que BibTeX
descartaba), se desambiguo `CORR`, se completaron autores y el volumen de SPIE.
`main.tex`: 15 correcciones en la lista de referencias, sin migrar a BibTeX.
Cerrado con los 5 .bib oficiales que pego la autora: `wu2022xcist` confirmado por IOP,
`ramadanov2025safezone` por MDPI, y los tres volumenes LNCS retirados porque el
exportador de Springer no los trae. `refs.bib` sin ningun `% VERIFICAR`. Decision de
precedencia registrada en `01-decisiones.md` con orden explicita.
Regla 9 de `CLAUDE.md` reescrita y marcas eliminadas de `refs.bib`.
Siguiente: cerrar el representante de los 3 grupos internos de dataset7.

## Paso anterior
2026-09-07: la autora reviso en 3D los 178 volumenes; fusionadas sus tres reglas de
clasificacion con la investigacion de los agentes en `revision.csv` (178 filas,
`3D completa`). Cifras: dataset7 con material ortopedico 72 de 75 (69 de contenido
unico); dataset6 con objeto 33, de ellos 27 solo extracorporeo; 70 candidatos a
entrenamiento limpio. #20 y #21 resueltas en criterio, #22 cuantificada (27 volumenes
en juego). #19 estrechada: `CLINIC_0074` resuelto (hay lazo, no es metal) y regla nueva
"autora sin objeto + agente incierto = sin objeto". `metal_0059`/`metal_0071` descartado
como par. Textos "preliminar" borrados de metal_0002 y metal_0003.
Siguiente: que la autora copie sus reglas a `01-decisiones.md` y elija representante en
los 3 grupos duplicados internos de dataset7.

## Paso anterior
2026-09-07: corridos 12 agentes `clasificador-metal` sobre los 113 candidatos HU.
113 filas en `propuesta_clasificacion.csv`, todas `propuesta sin validar`; `revision.csv`
intacto (sigue con 3 filas parciales). Metal: 65 `si (propuesto)`, 42 `incierto`, 1 `no`,
5 mixtos. Cuatro implicancias nuevas #19-22: el umbral HU no detecta (objeto bajo 1500 HU
en CLINIC_0074), duplicados CRUZADOS entre sub-datasets (fuga train/test), CLINIC-metal
con material extracorpóreo, y `Objeto extraño` sin definicion operativa.
Siguiente: decidir #19 (revisar los 178) y #22 (definicion), resolver duplicados.

## Paso anterior
2026-09-07: auditado `experiments/exploration-3d` contra el encargo de Victor.
Descripcion de datos cubierta para lo local; metal y split instrumentados pero SIN
ejecutar (0 de 178 confirmadas, 166 pendiente + 12 duplicado). Nuevo: solo 178 de los
1184 volumenes de CTPelvic1K estan en disco -> implicancia #18. Construido (no corrido)
el subagente `clasificador-metal` con `laminas.py` y `propuesta_clasificacion.csv`.
Siguiente: correr el agente sobre los 113 candidatos y los 65 no candidatos de dataset6.

## Paso anterior
2026-09-07: adopción de Peters registrada en `01-decisiones.md` con autorización.
Índice y fichas armonizados: Peters N1, Wu/XCIST N2; N4 de descartes creado y vacío.
Siguiente: concretar adaptación/validación del protocolo (#16–17) y armonizar `00-tesis.md`.
Continúan pendientes revisión 3D completa, pacientes/duplicados y máscaras.

## Paso anterior — exploración 3D
2026-09-07 (cierre del encargo del 06): flujo 3D con un script y un CSV listo;
178 CT, 113 candidatos HU, 6 grupos duplicados, 3 revisiones parciales. Peters en main.tex.
Siguiente: completar revisión 3D+cortes, resolver duplicados/pacientes y máscaras.
Nuevas implicancias #15–17; #8 aplicada a redacción, validación técnica pendiente.

## Paso anterior — verificación bibliográfica
P4: verificacion de niveles con 10 subagentes `lector-papers`, uno por PDF. **6 de mis
7 movimientos verificados estaban mal.** Reparto corregido a 8/12/7, con 10 fichas
nuevas. Salieron 4 implicancias (#7 a #10) y se actualizaron #5 y #6 con evidencia
textual. `_candidatos.md` poblado con 21 candidatos de snowballing.

## Paso anterior
P3: niveles de `_index.md` reasignados por el criterio nuevo de la autora (riesgo
sobre el argumento central o el benchmark).

## Paso anterior
P2: `docs/literatura/_index.md` completado. Las 27 entradas de `refs.bib` tienen fila,
con estado del PDF y acceso. Inventario: 25 de 27 PDFs presentes; faltan
`wang2025adaptiveweighting` y `zhang2026pediclescrew`.

## Paso anterior
P1: `refs.bib` generado desde la seccion References de `tesis/main.tex`. 27 entradas,
claves `apellidoANIOpalabraclave`. Las 27 quedaron marcadas `% VERIFICAR`.

Ademas: `scripts/renombrar_papers.sh` generado (NO ejecutado). Los 25 PDFs
emparejados, ninguno pendiente. Conflicto de claves resuelto: manda `refs.bib`,
se corrigio `_index.md`. Ficha de `wang2025adaptiveweighting` creada desde abstract.

## Pendientes bibliográficos anteriores
Decidir sobre la implicancia #9 (reenunciar el gap) y la #7 (el muestreador sin fuente
operacional de zona segura). Las dos tocan el alcance minimo viable y ninguna se puede
resolver leyendo mas: son decision de la autora. En paralelo, conseguir McLaren 2021,
que es la posible solucion de #7.

## Pendientes abiertos
- La bibliografia crecio de 2 a 3 paginas al migrar a BibTeX. No es un error: la lista
  a mano llevaba `et al.` y omitia DOI, editores e ISBN; la generada los imprime todos.
  Se probo `plainnat`, `abbrvnat` y `biblatex` con `maxbibnames=1`: las tres dan
  3 paginas. Si hay limite de dos, la decision es de la autora y las palancas son
  quitar los DOI del impreso o bajar el cuerpo de letra de la lista.
- 11 de las 27 entradas no se citan en el cuerpo (`karageorgos2024ddpm`,
  `kazerouni2023diffusionsurvey`, `ren2022metalinsertion`, `rombach2022latentdiffusion`,
  `selles2024marreview`, `singhrao2024fiducial`, `vanbosse2011pelvicpositioning`,
  `wang2019cochlear`, `yun2026simulationdriven`, `zhang2023controlnet`,
  `zhang2026pediclescrew`). Las sostiene `\nocite{*}`, puesto para que la lista siga
  siendo exactamente la que definio la autora. Citarlas en el cuerpo o retirarlas es
  decision suya; sin `\nocite{*}` la lista bajaria a 16 entradas.
- Implicancia #1 ABIERTA: `wang2025adaptiveweighting` es nivel 1 y solo hay abstract.
  Al llegar el PDF, releer con `lector-papers` y regenerar la ficha completa.
- Implicancia #2 ABIERTA (GAP): el multi-ventana publicado es todo de remocion, no
  de sintesis. Verificar el reclamo de novedad antes de escribirlo.
- Implicancias #3 y #4 ABIERTAS, ambas de `zhang2026pediclescrew`: colision de
  encuadre con mi novedad, y una segunda escala de brecha cortical con umbral de
  2 mm que toca la definicion de BFC.
- Implicancia #5 ABIERTA, ACTUALIZADA: `liu2025pipeline` no compite en metodo (plan
  optimo determinista), pero define CSV y QID sobre CTPelvic1K, vecinas de SAP y BFC.
- Implicancia #6 ABIERTA (GAP), ACTUALIZADA: `ren2022` aporta la frase que fundamenta
  el gap pero no sirve de brazo de comparacion (exige raw data de fabricante).
- Implicancia #7 ABIERTA (RIESGO): el muestreador se queda SIN fuente operacional de
  zona segura. Toca el alcance minimo viable. La mas urgente.
- Implicancia #9 ABIERTA (GAP): insertar metal sintetico ya es practica establecida en
  4 trabajos, y la difusion latente ya compitio en MAR. Hay que reenunciar la novedad.
- Implicancia #10 ABIERTA (REDACCION): `chen2024tumorsynthesis` no modela nada fuera de
  la mascara y trunca HU a [-175,250]: respaldo citable de B_delta y de C3.
- `karageorgos2024ddpm`: el subagente propuso N1, se mantuvo en N2 por consistencia.
  Disenso registrado en `_index.md`; decision de la autora.
- `chen2024tumorsynthesis`: candidato a subir a N1, sin decidir.
- Implicancia #11 ABIERTA: SAP ignora la segunda escala (angular) de `smith2006iliosacral`,
  y las tasas de ese paper son cadavericas n=4: no sirven de prior clinico.
- Implicancia #12 ABIERTA (RIESGO, la mas grave): el rango 31-60% NO aparece en
  `zwingmann2009navigated`. Son dos complementos derivados de dos brazos distintos.
- Implicancia #13 ABIERTA (RIESGO): CLINIC-metal tiene solo 14 de 75 volumenes anotados,
  el paper no dice que metal contiene, y no da cifra de degradacion.
- Implicancias #19-22 ABIERTAS, todas de la clasificacion asistida, pero
  estrechadas por la revision 3D del 2026-09-07:
  - #19 estrechada: `CLINIC_0074` resuelto (no es metal). Siguen vivas dos patas,
    el artefacto que fabrica componentes y la mesa del escaner como componente.
    Opcion 1 (correr laminas sobre los 65 no candidatos, ~25 min) sigue abierta.
  - #20: criterio cruzado ya dictado por la autora; falta elegir representante en
    los 3 grupos internos de dataset7 (`0012`/`0021`, `0013`/`0043`, `0046`/`0074`).
    Hasta eso, sigue bloqueando el split.
  - #21 CONFIRMADA con cifra: 3 de 75 de CLINIC-metal no tienen osteosintesis.
    El test es 72, de contenido unico 69. Falta fijar esa cifra.
  - #22 sin decidir, y es la mas barata: define 70 vs 97 volumenes de entrenamiento.
- Implicancia #18 ABIERTA (DATOS): en disco hay 178 de los 1184 volumenes de
  CTPelvic1K; faltan ABDOMEN, COLONOG, MSD_T10, KITS19 y CERVIX. Decidir si se
  descargan o si el alcance de datos se declara como CLINIC + CLINIC-metal.
- Encargo de Victor a medias: `experiments/exploration-3d/cumplimiento-encargo.md`
  detalla que sub-tarea esta cubierta. `clasificador-metal` ya corrio y la revision
  3D esta completa; falta representante en los 3 grupos internos de dataset7 y
  `Grupo paciente`, vacio en las 178 filas, antes de cualquier split.
- Implicancia #14 ABIERTA (GAP): `peters2025hybrid` da la base operacional de BFC e ISC y
  sostiene por escrito la novedad del muestreador. La lectura mas productiva de todas.
- Falta armonizar el alcance completo de `00-tesis.md` con la adopcion de Peters
  (su frase sobre reimplementacion independiente de XCIST).
- Verificacion de #13 pendiente y no bibliografica: mirar los volumenes para saber que
  metal contienen. (La otra —si CLINIC-metal amplio su anotacion desde 2021— quedo
  CERRADA el 2026-09-09 con el cierre de #40: no se amplio.)
- `wang2025adaptiveweighting`: unico N1 SIN VERIFICAR, tercera ronda bloqueado por el PDF.
- Faltan por verificar tambien:
  `arand2019pelvicring` y `xie2024implantsegmentation`.
- `SAP`, `BFC` e `ISC` siguen sin definir en `docs/03-glosario.md`. El nivel de
  `xie2024implantsegmentation` y el de `liu2025pipeline` dependen de esas definiciones.

## Pendientes cerrados
> Lo que ya no requiere accion. Se conserva para no reabrirlo por olvido.

- **Implicancia #8 — APLICADA (redaccion).** La autora adopto el protocolo de
  `peters2025hybrid` como brazo de comparacion en lugar de la reimplementacion de
  XCIST; `wu2022xcist` no valida metal. Decision registrada en `01-decisiones.md`
  con autorizacion el 2026-09-07 y escrita en `main.tex`. Lo que sigue vivo es #17
  (ejecucion, configuracion y validacion) y armonizar `00-tesis.md`.
- **`zhang2026pediclescrew`: nivel resuelto.** Queda en nivel 1 por el criterio de
  riesgo, al ser origen de las implicancias #3 y #4.
- **Mapeo difftumor = `chen2024tumorsynthesis`: RESUELTO** contra el PDF.
- **Par `metal_0059` / `metal_0071`: DESCARTADO.** La autora confirmo el 2026-09-07,
  tras revision 3D, que no son el mismo paciente: comparten spacing y HU minimo, nada
  mas. Sin `Grupo paciente` comun. Registrado en `01-decisiones.md`.
- **#20, criterio cruzado: DICTADO.** En un grupo duplicado que cruza sub-datasets
  prevalece el volumen de dataset7 como representante, y ese volumen queda marcado
  sin material ortopedico. Afecta a `metal_0061`=`CLINIC_0037`,
  `metal_0036`=`CLINIC_0048`, `metal_0064`=`CLINIC_0070`.
- **#19, conflictos autora/agente: RESUELTOS.** `CLINIC_0074` tiene una estructura en
  lazo pero no es metal, asi que sigue siendo candidato limpio. Regla general dictada:
  autora «sin objeto» + agente `incierto` = sin objeto. Cierra los cinco desacuerdos
  menores.
- **Revision 3D de los 178 volumenes: COMPLETA** (`3D completa`, no recorrido de
  cortes). Fusionada con la investigacion de los agentes en `revision.csv`.
- **Textos «preliminar»** borrados de `metal_0002` y `metal_0003`.
- **`refs.bib`: los 27 DOIs, PUESTOS y VERIFICADOS contra el raw del editor.**
  Ninguno cambio al reconstruir el archivo, ni se anadio ni se quito ninguna entrada.
- **Pipeline bibliografico `raw` -> `clean` -> `refs.bib`: MONTADO** el 2026-09-07 por
  encargo de la autora. `refs/raw/` (27 fuentes del editor, intactas), `refs/clean/`
  (27 entradas normalizadas a mano), `refs/MAPEO.md` (procedencia y reglas) y
  `scripts/build_refs.py`, que regenera `refs.bib`. Los `% VERIFICAR` obsoletos
  desaparecieron; quedan 4 nuevos, reales.
- **Bug de compilacion corregido: `issue` -> `number`** en `liu2021ctpelvic1k` (16(5)),
  `xie2024implantsegmentation` (24(1)) y `zhang2026pediclescrew` (34(4)). BibTeX
  clasico descarta `issue` sin avisar: esos tres fasciculos no se habrian impreso.
- **`CORR` desambiguado** a *Clinical Orthopaedics and Related Research* en
  `vanbosse2011pelvicpositioning` y `zwingmann2009navigated`. Se confundia con el
  repositorio de preprints *CoRR* de arXiv. Igual `IEEE TMI` e `Int J CARS`.
- **`deman2007catsim` volume 6510**, que faltaba, confirmado por el raw de SPIE.
- **Autores completos en las 27.** Antes 25 decian `and others`.
- **Precedencia dictada por la autora (2026-09-07): manda `refs/raw/`,** y en su
  defecto `refs/clean/`. Un campo que el raw no confirme no se conserva por costumbre.
  Pendiente que la autora lo copie a `01-decisiones.md`.
- **`ramadanov2025safezone`: raw RESUELTO** el 2026-09-07. La autora sustituyo el .txt
  degradado por el .bib real de MDPI y borro el .txt. Confirma 14(10):3567, el DOI que
  ya estaba, y que el titulo si lleva los dos puntos. Es la fuente de la implicancia #7.
- **Los 4 campos sin respaldo: CERRADOS** el 2026-09-07 con los .bib oficiales.
  `wu2022xcist` CONFIRMADO por IOP (`pages = {194002}`, 67(19)). Los tres volumenes
  LNCS RETIRADOS de `refs.bib` y de `main.tex`: el exportador de Springer no los da.
  `refs.bib` ya no tiene ningun `% VERIFICAR`.
- **Decision de precedencia REGISTRADA** en `01-decisiones.md` el 2026-09-07 con orden
  explicita de la autora.
- **Regla 9 de `CLAUDE.md` REESCRITA** el 2026-09-07 con orden explicita: describe el
  flujo `raw` -> `clean` -> `refs.bib` generado, prohibe cualquier campo sin respaldo
  en el raw y mantiene que la lista de entradas la define la autora.
- **Marcas eliminadas de `refs.bib`.** Ni `% VERIFICAR` ni `% NOTA`: lo que esta en el
  archivo tiene respaldo en el raw. Lo retirado queda solo en `refs/MAPEO.md`.
- **`main.tex`, MIGRADO A BIBTEX** el 2026-09-07 con orden explicita de la autora.
  `\usepackage[round,authoryear]{natbib}`, `\bibliographystyle{abbrvnat}` y
  `\bibliography{../refs}` dentro del `multicols`, con `\renewcommand{\bibsection}{}`
  para no duplicar el encabezado `\section{References}`. Las 17 citas del cuerpo pasaron
  de texto a `\citep` (parentesis), `\citet` (autor + anio en linea) y `\citealp`
  (dentro del parentesis de C1). La lista a mano se borro entera. Compila con
  `pdflatex; bibtex; pdflatex; pdflatex` desde `tesis/`: 0 citas indefinidas, 27
  `\bibitem` en el `.bbl` y las citas del cuerpo impresas igual que antes. Lo que
  cambia de aspecto es la lista: 3 paginas en vez de 2, y 11 entradas la sostiene
  `\nocite{*}`. Las dos cosas estan en Pendientes abiertos.
- **`.gitignore`: LIMPIADO** el 2026-09-07. Se quitaron el `@'` de la primera linea y
  el `'@ | Set-Content -Encoding utf8 .gitignore` de la ultima, restos de un here-string
  de PowerShell que se escribio en vez de ejecutarse. Reglas verificadas con
  `git check-ignore -v`: `papers/`, `data/`, `*.nii.gz` y `*.bbl` se ignoran;
  `refs/raw/*.bib` no.
- **LNCS: IGNORADOS por decision de la autora** el 2026-09-07. Los tres volumenes
  (`jacob2026lgesynthnet`, `ramzan2026claim`, `wang2019cochlear`) no se persiguen en
  otra fuente. Sus valores salieron de `refs/MAPEO.md` para que nadie los reintroduzca
  sin respaldo en `refs/raw/`; ahi queda solo la decision y el motivo (el exportador de
  Springer no trae `series` ni `volume`).
- **`main.tex`, lista de referencias actualizada** el 2026-09-07 con autorizacion
  explicita: 15 correcciones (revistas completas, fasciculos, paginas de las tres
  actas, volumen de SPIE). Sigue en texto plano; no se migro a BibTeX.


## Deudas asumidas
- Leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion:
  la metrica SAP depende de la definicion de grados de brecha cortical.
