# Asesor — introduccion r09

Archivo: `overleaf/secciones/introduccion.tex` (estado de r09, sin corregir). Encargo: `redaccion/ENCARGO_2026-10-16.md`.
Decisiones que mandan: `docs/01-decisiones.md` 2026-10-16 (#193 opcion a; ptos 2 y 3), 2026-10-15 (4) pto 4,
2026-10-15 pto 9 (D9), 2026-10-08 pto 22, 2026-09-08 (3)-(4) (S2 descriptivo). Encabezado (l. 3-17) y Formulacion
(l. 21) siguen bajo #126: no se tocan aqui.

Recuento: el `.tex` tiene **7** `\GAPDATO` (l. 54 x2, 66, 78, 94, 96, 100), no 6; 0 `\GAPDEC`, 0 `\GAPLIT`. Coincide
con el lint (dato=7).

| # | GAP (linea) | tipo | clase A/B/C/D | propuesta (1-2 lineas) | fuente |
|---|---|---|---|---|---|
| 1 | l. 54, contraste de realismo sin script (H5) | GAPDATO | **D** | Trabajo futuro declarado; retirar `\REVVISUAL` y reescribir como limitacion del Obj 3 | `01-decisiones.md` 2026-10-16 ptos 2-3; `00-tesis.md`:195, :212 |
| 2 | l. 54, comparacion visual a ciegas (D3) | GAPDATO | **D** | Igual: trabajo futuro, sin prueba de Turing | `01-decisiones.md` 2026-10-16 pto 2; `00-tesis.md`:212 |
| 3 | l. 66, analisis exploratorio con poses del muestreador (D9) | GAPDATO | **B** (calculo no barato: GPU, Khipu, particion de prueba del Obj 3) | Proponer: D9 preinscrito y **no ejecutado**, declarado como desviacion y trabajo futuro | `01-decisiones.md` 2026-10-15 pto 9; `objetivo3/EXPERIMENTOS.md`:111-112 ("falta D9", POR ESCRIBIR); ninguna decision lo excluye |
| 4 | l. 78, preinscripcion y corrida en el segundo corredor bajo S1 | GAPDATO | **B** | Proponer: no se preinscribe ni se corre; trabajo futuro (sin referencia ordinal clinica bajo S1; resultado solo descriptivo) | `preinscripcion_muestreador.md` §7; `01-decisiones.md` 2026-09-08 (3)-(4); MAPA fila 66; ninguna decision lo excluye |
| 5 | l. 94, sensibilidad del Obj 2 sin los dos casos | GAPDATO | **A** | Ya existe (E15): retirar la marca y alinear con la formula de capitulo3-r26 | `experiments/objetivo2/e15_w1_sensibilidad.md`:5-8; `01-decisiones.md` 2026-10-15 (4) pto 4; `capitulo3.tex`:115 |
| 6 | l. 96, envolvente osea y canal sacro / foramenes | GAPDATO | **C** (hecho en los 2 pilotos; la cohorte no es barata aqui) | Limitacion declarada con la evidencia piloto; opcion de correr la cohorte en Khipu (decision de la autora) | `experiments/registro/registro_2026-10-16.md` §1; `r_envolvente_canal.py` |
| 7 | l. 100, estructura direccional del artefacto sintetico | GAPDATO | **D** | Limitacion declarada (no medida); fuera de GAP por decision | `01-decisiones.md` 2026-10-16 pto 3 (nombra "estructura direccional") |

Hallazgo T01/T02 de `introduccion-r09-trazabilidad.md`: T01 es el GAP #5 (clase A, texto abajo). T02 ya esta resuelto
a medias: E15 **si** figura en `experiments/objetivo2/EXPERIMENTOS.md`:122, pero en la tabla de §7 ("Superados y
archivados"), que no le corresponde (deberia ir en §5, junto a `e13`). `docs/00-tesis.md` sigue sin la cifra 0.203 /
0.237. El asesor no edita ninguno de los dos: lo hace el orquestador o la autora. El texto propuesto para el GAP #5 no
usa cifras, asi que T02 no bloquea la correccion.

Afirmaciones sin marca que deberian cambiar (decision no tomada o ya revocada, escrita como hecho):
- **l. 41 (`\REVVISUAL`):** "Se compara también con observaciones reales de artefacto, mediante estadísticos [...]"
  afirma en presente un contraste (H5) que la decision 2026-10-16 pto 2 deja como trabajo futuro. No es un `\GAPDEC`
  nuevo: la decision existe, y lo que falta es reescribir la frase (texto abajo).
- **l. 98 y l. 88 (`\REVVISUAL`):** el contenido esta respaldado (#191, #193; DEC 2026-10-15 (3) pto 6). Solo hay que
  retirar la macro, sin cambiar las afirmaciones. No hay GAP.

## Textos para el redactor (clase A y D)

**GAP #5 (A), l. 94, ultima oracion.** Sustituir "y la variante se mantiene, con una sensibilidad sin los dos casos
fallidos \GAPDATO{...}" por:
> "[...] y la variante se mantiene. Los dos casos siguen en la cohorte preinscrita, y un análisis de sensibilidad sin
> ellos, con 70 pacientes, se presenta en el capítulo de resultados."

Es la misma formula que fijo capitulo3-r26 (`capitulo3.tex`:115). Sin cifras. Si se quieren cifras, deben ir las
primarias junto a las nuevas (T01, forma b): W1 0.206 -> 0.203 frente a la navegada y 0.230 -> 0.237 frente a la
convencional, con 72 y 70 pacientes (`e15_w1_sensibilidad.md`:7-8). No escribir "no cambia el resultado": ninguna
fuente lo dice.

**GAP #1 y #2 (D), l. 54.** Retirar las dos `\REVVISUAL` y los dos `\GAPDATO`. Propuesta:
> "La inserción por copia y pegado no produce rayas, y superarla es un control de cordura que alcanza cualquier brazo
> que genere artefacto; el sintetizador la supera en prueba, y ese resultado no cuenta a su favor. El contraste de
> realismo frente a observaciones reales de artefacto y la comparación visual a ciegas de los modelos no se
> ejecutaron: después de juzgar insuficiente el resultado visual, se decidió no rediseñar el sintetizador, y ambos
> quedan como trabajo futuro (Sección~\ref{sec:ap-realismo}). Después del resultado de la versión~1 se entrenó una
> versión~2 del sintetizador, posterior y exploratoria, que se reporta junto al modelo evaluado y no en su lugar
> (Sección~\ref{sec:v2}), y su evaluación exploratoria en prueba se ejecutó salvo esa comparación visual. [...]"

Respaldo: `01-decisiones.md` 2026-10-16 pto 2 ("La comparacion visual a ciegas (D3) y el contraste de realismo sin
script (H5) no se ejecutan: se declaran como trabajo futuro, con la razon"). No se menciona la prueba de Turing: no era
un compromiso y nombrarla sugiere que estuvo prevista.

**l. 41 (afirmacion sin marca, misma decision).** Sustituir la oracion `\REVVISUAL` por:
> "El contraste con observaciones reales de artefacto, mediante estadísticos de los HU alrededor del metal que no
> exigen una imagen sin metal del mismo paciente, quedó diseñado y no se ejecutó en prueba (Sección~\ref{sec:apariencia})."

**GAP #7 (D), l. 100.** Retirar `\REVVISUAL` y el `\GAPDATO`, y sustituir la segunda oracion por:
> "La \emph{streak amplitude} adaptada crece con cualquier desviación extrema del anillo, tenga o no estructura de
> raya, y la estructura direccional del artefacto sintético no se midió; queda como limitación del Objetivo~3."

El resto del parrafo (truncamiento de $B_{\delta}$; 12 mm frente a 10 mm para piezas del tamano de un tornillo; placas y
protesis sin acotar) se mantiene sin la macro: esta respaldado (C3 :262, :517; DEC 2026-10-15 (2)). No citar la
inspeccion visual de #176 (moteado y no rayas): #176 esta ABIERTA y no es una medicion.

**GAP #6 (C -> texto de limitacion, valido con cualquiera de las dos opciones de la decision B-3).** l. 96, sustituir
desde "La brecha se mide contra una envolvente ósea [...]" por:
> "La brecha se mide contra una envolvente ósea, una máscara de hueso cuyo cierre morfológico podría ocupar el canal
> sacro y los forámenes, y en ese caso una perforación hacia ellos daría brecha nula. Esa posibilidad no se comprobó
> en la cohorte. En dos casos piloto ajenos a ella, el canal quedó fuera de la envolvente en la línea media de S1,
> salvo en unos 6~mm de un extremo de S1 en uno de los dos, donde el cierre lo ocupó; los forámenes no se midieron
> (Sección~\ref{sec:amenazas})."

Cifras: 36 de 36 cortes con hueco medial conservado en `metal_0008`; 7 cortes contiguos de 0.8 mm (5.6 mm) ocupados por
el cierre en `CLINIC_0002`, donde la union dejaba un hueco de 3.1 a 8.6 mm (`registro_2026-10-16.md` §1). "Unos 6 mm" =
7 cortes x 0.8 mm. Calculo descriptivo y posterior. La misma frase, con las cifras, va a `capitulo3` §Amenazas (MAPA
fila 106), donde esta el original del GAP; la introduccion solo la resume. Que el hueco ocupado en `CLINIC_0002` sea
el canal no lo establece la medida: por eso la frase dice "lo ocupó" sobre el hueco medial que se describe como canal
en el resto de cortes, y la Seccion de amenazas debe decir que la medida es un sustituto en la linea media.

**GAP #3 y #4: textos condicionados a las decisiones B-1 y B-2 (abajo).** Si la autora las adopta:
- l. 66: "[...] Por eso la comparación no cubre las poses del muestreador. Un análisis exploratorio con esas poses,
  solo con el sintetizador, quedó fijado en el diseño y no se ejecutó; queda como trabajo futuro
  (Sección~\ref{sec:ap-sintesis})."
- l. 78: "Su eje está medido, pero el muestreo de poses en él no se preinscribió ni se ejecutó, y queda como trabajo
  futuro."

Los mismos cambios deben replicarse en `capitulo3` (l. 38, 194, 297, 349, 513, 519): el encargo los revisa ahi.

## Decisiones para la autora (clase B), con texto listo para 01-decisiones.md

**B-1. D9 (poses del muestreador en el Obj 3).** Recomendacion: **(a) no ejecutar; declararlo como analisis
preinscrito no ejecutado y trabajo futuro.** Argumento: exige generar con GPU en Khipu sobre la particion de prueba del
Obj 3 (13 pacientes x 5 poses x 5 semillas, DEC 2026-10-15 pto 9), justo lo que la decision del 2026-10-16 da por
cerrado ("el proyecto y sus resultados quedan como estan"; en Khipu no queda nada por correr). Era exploratorio, solo
con el sintetizador y sin umbral, y no podia mover el desenlace del contraste primario. Declararlo no ejecutado es
honesto: queda a la vista que se fijo antes y no se corrio.
- (b) Correrlo: cierra el GAP con un resultado, pero abre la particion de prueba para un analisis nuevo despues de
  #193 y pide GPU (no barato).
- (c) Borrarlo del diseno: no es admisible, porque quedo fijado el 2026-10-15 y borrarlo ocultaria una desviacion.

**B-2. Segundo corredor bajo S1.** Recomendacion: **(a) no preinscribir ni correr; trabajo futuro.** Argumento: ninguna
fuente revisada da una distribucion ordinal clinica bajo S1, asi que el resultado seria solo descriptivo (2026-09-08
(3)-(4)) y no responde la pregunta del Obj 2. La verificacion de nivel R2 esta "en pausa" (`objetivo2/EXPERIMENTOS.md`
§6), y el nivel del corredor varia entre volumenes (S2 a S4). La corrida pediria las mascaras de Khipu.
- (b) Preinscribir y correr en Khipu con los ejes ya medidos (69 de 72): es barato en CPU, pero exige una
  preinscripcion nueva (la decide la autora) y da una distribucion sin referencia.

Texto listo para `01-decisiones.md` (B-1 y B-2 juntas, si se adopta (a) en las dos):

```
## 2026-10-16 (2) — D9 y segundo corredor bajo S1: no se ejecutan; trabajo futuro (introduccion-r09)

Decidido por la autora a propuesta del asesor de tesis (ronda introduccion-r09).

1. **D9 (2026-10-15 pto 9) no se ejecuta.** El analisis exploratorio con 5 poses del muestreador por paciente de
   E-A2, solo con el sintetizador, queda como analisis fijado en el diseno y no ejecutado, y se declara como trabajo
   futuro. Razon: exige generar con GPU sobre la particion de prueba del Objetivo 3 despues de la decision del
   2026-10-16 (#193, el proyecto queda como esta), y su resultado, exploratorio y sin umbral, no podia cambiar el
   desenlace del contraste primario. Los capitulos lo escriben como no ejecutado, no como pendiente.
2. **Segundo corredor bajo S1: no se preinscribe ni se corre el muestreo de poses.** Trabajo futuro. Razon: sin
   distribucion ordinal clinica bajo S1 (2026-09-08 (3)-(4)), el resultado seria solo descriptivo; el nivel del
   corredor varia entre volumenes y su verificacion (R2) esta en pausa. El eje medido (69 de 72) se conserva y se
   reporta como dato de la geometria del corredor, no como resultado del muestreador.
```

**B-3 (asociada a C, GAP #6). Envolvente y canal sacro en la cohorte.** Recomendacion: **(b) declararlo limitacion con
la evidencia de los pilotos (el texto de arriba), y opcionalmente (a).** Argumento: incluso sobre los 72 casos, la
medida es un sustituto en la linea media del canal y no localiza los foramenes, asi que no "comprobaria" la frase del
GAP; daria un recuento de casos en que el cierre ocupa el hueco medial. El piloto ya muestra que el riesgo no es nulo
(`CLINIC_0002`), y eso justifica declararlo.
- (a) Correr `r_envolvente_canal.py --cohorte` en Khipu: es CPU y de minutos, pero el script usa rutas del
  repositorio y hay que adaptarlo a la disposicion plana de `~/metalsynth/qc/` (como `e14_relleno.sbatch`) y
  escribir su sbatch. No esta preparado.

Texto listo para `01-decisiones.md` (si se adopta (b)):

```
3. **Envolvente osea y canal sacro (GAP de introduccion l. 96 y capitulo3 §Amenazas):** no se comprueba en la
   cohorte; se declara como limitacion de validez de constructo del Objetivo 2, con la medicion descriptiva y
   posterior en los dos pilotos (`experiments/registro/registro_2026-10-16.md` §1): canal fuera de la envolvente en la
   linea media de S1 en `metal_0008`, y ocupado por el cierre en 7 cortes de un extremo de S1 en `CLINIC_0002`;
   foramenes no medidos.
```

Ninguna decision previa delega estos puntos en el asistente: son de la autora.

## Calculos hechos (clase C -> A) y calculos no baratos que quedan

**Hecho: `experiments/registro/r_envolvente_canal.py`** (local, unos 20 s; registro en
`experiments/registro/registro_2026-10-16.md` §1; fila en `experiments/objetivo2/EXPERIMENTOS.md` §5).
- Reconstruye `B` con el codigo de E12 (union TS, recorte de 6 mm, cierre de 2 mm, sin relleno) en los dos pilotos
  con mascaras en disco (`metal_0008`, `CLINIC_0002`; grupo 1, **fuera de la cohorte**).
- **Control de regresion:** la longitud anclada del implante sobre esa `B` reproduce `L_TS_mejor_mm` de E9-TS y E12
  (113.0 y 154.0 mm). **Reproduce.**
- Resultado: `metal_0008`, hueco medial en la union en 36 de 54 cortes de S1 y en `B` en los mismos 36 (mediana AP
  13.3 mm, HU mediana 2); el cierre recorta como maximo 3.0 mm. `CLINIC_0002`, 38 de 51 en la union y 31 de 51 en `B`
  (mediana 17.2 mm, HU 10); en **7** cortes contiguos de un extremo de S1 el cierre ocupa un hueco medial de 3.1-8.6
  mm. Relleno 2D maximo de 4.2 y 7.8 mm de espesor.
- Descriptivo y posterior; no toca la particion de prueba del Obj 3 ni ninguna cifra de E13.
- Se probo antes una version que anclaba la linea en el punto S1 de `r1_landmarks.csv`. En `CLINIC_0002` ese punto
  cae fuera del hueso de `B` en la linea media, y la medida daba 0 sin significado. Se sustituyo por la mediana lateral
  de la mascara `vertebrae_S1` en cada corte. La cifra de esa primera version no se reporta.

**No baratos que quedan (para la autora):**
1. **D9** (GAP #3): GPU en Khipu sobre la particion de prueba del Obj 3. Ver B-1.
2. **Envolvente en la cohorte** (GAP #6): CPU en Khipu, pocos minutos, pero falta adaptar el script y escribir el
   sbatch. Ver B-3 (a).
3. **Segundo corredor** (GAP #4): CPU en Khipu, pero exige antes una preinscripcion. Ver B-2 (b).

TOTAL A=1 B=2 C=1 D=3 | GAP que quedarian si se aplica todo: lit=0 dato=0 dec=0 (con B-1, B-2 y B-3 adoptadas como se proponen; sin ellas, dato=3: l. 66, 78, 96)
