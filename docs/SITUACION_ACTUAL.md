# Situación actual de MetalSynth-Pelvis, explicada en simple

> **Corte del estado: 12 de octubre de 2026.** Lectura de unos 15 minutos, pensada para mostrar el avance al asesor.
> Explica **solo lo vigente**: lo que quedó superado está en `experiments/obsoletos/` y no se cita. La versión anterior
> de este documento (8 de octubre, más larga y con la historia de cada decisión) está en el historial de git
> (`git show e7417ad:docs/SITUACION_ACTUAL.md`).
>
> Convención: **HECHO** = ejecutado y registrado. **PENDIENTE** = todavía no existe. Las cifras salen de
> `docs/04-implicancias.md`, `docs/00-tesis.md`, `docs/02-datos.md` y de los resultados en `experiments/`.

---

## 1. La tesis en un minuto

**El problema.** Cuando un paciente tiene un tornillo metálico en la pelvis, la tomografía (TC) sale con **rayas**
claras y oscuras alrededor del metal (el "artefacto metálico"). Esas rayas confunden a los programas que segmentan
hueso. Para entrenarlos harían falta muchas TC con tornillos, y hay pocas.

**La idea.** Fabricar esos ejemplos: tomar una pelvis **sin** metal, decidir **dónde** iría un tornillo como lo
pondría un cirujano, y **pintar** el tornillo con sus rayas.

**Lo que se evalúa.** Si lo fabricado es **coherente**: si las posiciones se parecen a las de cirugías reales y si
las rayas se parecen a las de la física. **No** se evalúa si eso mejora un segmentador: está fuera de alcance.

**Analogía.** Es como un efecto especial de cine: primero el director decide dónde va el objeto (muestreador) y
después el equipo de efectos lo dibuja con su sombra y su reflejo (sintetizador). Se juzgan por separado.

---

## 2. El mapa

```
pelvis sin metal ─► [MUESTREADOR, Obj 2] ─► pose del tornillo ─► máscara M ─► [SINTETIZADOR, Obj 3] ─► TC con tornillo y rayas
                     ¿dónde va?                                                 ¿cómo se ve?
```

| Objetivo | Pregunta en simple | Estado | Dónde está |
|---|---|---|---|
| **1. Compuerta** | ¿Se puede comprimir la TC con un modelo de imágenes normales sin perder los números del hueso? | **HECHO: No** | `experiments/objetivo1/` |
| **2. Muestreador** | ¿Dónde pondría el tornillo un cirujano, con sus errores típicos? | **HECHO y cerrado** | `experiments/objetivo2/`, `src/muestreador/` |
| **3. Sintetizador** | ¿Se puede dibujar el tornillo y sus rayas de forma creíble? | **Generado todo; falta evaluar la prueba final** | `experiments/objetivo3/`, `src/renderizador/` |
| **4. Métricas** | ¿Con qué se mide? | SAP (propia) **HECHA**; rayas con métricas de Peters et al. | `src/muestreador/sap.py`, `experiments/objetivo3/a20_evaluador_ea2.py` |

**Por qué el Objetivo 1 importa todavía.** El plan original era usar Stable Diffusion, que trabaja sobre una versión
comprimida de la imagen. La compuerta midió el error al comprimir y descomprimir el hueso: el mejor caso dio
**61.72 HU** de error medio, frente a un máximo aceptable de 25 HU, y los 34 de 34 pacientes fallaron. Por eso el
sintetizador trabaja **directamente sobre la imagen**, sin comprimir, y se entrena desde cero.

**HU (unidades Hounsfield)** = el número de cada vóxel de la TC. Aire −1000, agua 0, hueso esponjoso ~100–300,
hueso cortical ~1000+, metal > 2500.

---

## 3. Objetivo 2: dónde va el tornillo (con sus ecuaciones)

El tornillo elegido es el **transilíaco-transsacro**: entra por un hueso de la cadera (ilion), cruza el sacro a la
altura de la vértebra **S1** y sale por el otro ilion. El cirujano debe pasarlo por un "túnel" de hueso, el
**corredor**.

### 3.1 Paso 1 — medir el corredor de cada paciente

**Qué hace.** Busca, en cada pelvis, la línea recta por la que cabe el cilindro más grueso sin salirse del hueso.

1. **Hueso** = la unión de sacro, S1 y los dos coxales que segmenta **TotalSegmentator** (red pública, no se
   entrena nada), con un cierre morfológico de 2 mm. *Por qué no un umbral de HU:* el hueso esponjoso del sacro
   tiene HU bajos y un umbral lo "ahueca" (en el eje del corredor, el 42 % de los vóxeles quedaba bajo 150 HU).
2. **Candidatos.** Centros en una rejilla de 3 mm en el plano de S1; en cada centro, 81 direcciones: inclinaciones
   de −20° a +20° en pasos de 5°, alrededor del eje izquierda–derecha.
3. **Diámetro de una línea.** Con la transformada de distancia euclídea `EDT(p)` (distancia de cada punto `p` al
   no-hueso más cercano), a lo largo del tramo de hueso de la línea, sin 8 mm en cada extremo:

   ```
   D = 2 · min_t EDT(c + t·u)
   ```

   donde `c` es el centro y `u` el vector unitario de dirección. Si todo el eje está a ≥ r del borde, un cilindro
   de radio r cabe entero. La línea debe salir a tejido blando por las dos cortezas del ilion.
4. **El corredor** del paciente es la línea con mayor `D` a la altura de S1: su eje `(c, u)`, su largo `L` y su
   diámetro `D_TS`.

Código: `experiments/objetivo2/e9_corredor.py` (lógica) y la versión con TotalSegmentator (E9-TS); resultados en
`experiments/objetivo2/outputs/e9ts_ejes_corredor.csv`.

### 3.2 Paso 2 — perturbar el eje como lo haría un cirujano

Un cirujano real no acierta el eje perfecto: se desvía un poco. El muestreador genera **50 poses por pelvis**
moviendo y girando el eje. Toda la escala sale de **una sola constante independiente**: la holgura cortical de
**5 mm** de Kaiser et al., con la convención declarada "5 mm = 2 desviaciones estándar".

- Desviación del centro: `σ_t = 5 / 2 = 2.5 mm`
- Desviación angular (la misma holgura de 5 mm vista desde la mitad del corredor): `σ_a = arctan( 5 / (L/2) ) / 2`
  (mediana 2.07°)

Para cada pose, con `e1, e2` dos vectores perpendiculares a `u`:

```
φ_t, φ_a ~ Uniforme(0, 2π)              (dirección del error, sin preferir ninguna)
m_t ~ |N(0, σ_t)|,  m_a ~ |N(0, σ_a)|    (tamaño del error, truncado a 3σ)
centro'    = c + m_t · (cos φ_t · e1 + sin φ_t · e2)
dirección' = cos m_a · u + sin m_a · (cos φ_a · e1 + sin φ_a · e2)
```

**Por qué así.** La decisión más importante del Objetivo 2: **el muestreador no se calibra contra la serie clínica**
con la que después se compara. Si se ajustaran los parámetros hasta imitar a los cirujanos, compararse con ellos no
probaría nada. Por eso todo sale de Kaiser y se escribió antes de mirar ningún resultado. La dirección es isótropa
porque no hay datos clínicos de hacia dónde se equivoca más un cirujano.

Código: `src/muestreador/muestreo.py` (función `muestrear_poses`, semilla fija 20260922, una por paciente).

### 3.3 Paso 3 — SAP: ¿cuánto se sale del hueso cada pose?

**SAP** (*Surgical Admissibility of Placement*) es la única métrica propia de la tesis. Para cada pose mide la
**brecha cortical**: cuánto sobresale el tornillo fuera del hueso. Con `sd(p)` la distancia con signo al borde del
hueso (negativa dentro, positiva fuera) y `r` el radio del tornillo (diámetro **7.0 mm**, el de la serie clínica):

```
brecha = max_t  max( 0,  r + sd(c' + t·u') )
```

y la brecha se convierte en **grado** (escala de Smith et al., la que usa Zwingmann et al.):
grado 0 = sin perforación; 1 = (0, 2) mm; 2 = [2, 4] mm; 3 = > 4 mm.

**Comparación con cirugías reales.** Las 3 600 poses (72 pelvis × 50) dan una distribución de grados `P`, que se
compara con las dos de **Zwingmann et al. (2009)**: cirugía **navegada** (69 % grado 0) y **convencional** (40 %).
Como los grados tienen orden, se usa la distancia de **Wasserstein-1** (cuánta "masa" hay que mover y cuán lejos):

```
W1(P, Q) = Σ_{k=0}^{2} | F_P(k) − F_Q(k) |      (F = distribución acumulada de grados)
```

**Resultado (HECHO):** grado 0 = 51.5 %, 1 = 31.4 %, 2 = 11.1 %, 3 = 6.0 %; **W1 = 0.206 a la navegada** y 0.230 a
la convencional. En 15 de las 72 pelvis el corredor es más estrecho que el tornillo, y allí ni el eje perfecto se
salva. En las 57 restantes (análisis posterior, declarado como tal), el grado 0 sube a 64.2 % y W1 baja a 0.183.

Código: `src/muestreador/sap.py`; preinscripción en `experiments/objetivo2/preinscripcion_muestreador.md`.

---

## 4. ¿Qué metal cuenta? Cómo se dejan fuera los metales que no son tornillos

Tú preguntaste por `tornillos_conteo.csv`. Hay **dos cosas distintas** que conviene separar ante el asesor:

### 4.1 `tornillos_conteo.csv` describe; no filtra

`experiments/exploration-3d/tornillos_conteo.csv` (con su guía `tornillos_conteo.md`) es un **censo descriptivo**:
una fila por paciente y pregunta (¿hay tornillo?, cuántos iliosacros (IS), cuántos transilíacos-transsacros (TS),
cuántos otros aislados, qué clases de objeto: (a) tornillo aislado, (b) placa con tornillos, (c) fijador externo,
(d) prótesis, (e) otro). Tiene tres columnas de respuesta: `agente` (4 agentes de IA sobre láminas, solo
propuesta), `autora` (tu revisión en cortes, la que manda) y `evaluador_externo` (vacía). La clase (e) lleva
etiquetas: `e-noorto` (cremallera, catéter…), `e-dudoso`, `e-borde` (cortado en el borde de la imagen). Los
volúmenes repetidos de un mismo paciente van con `cuenta = no` y no suman: quedan **56 pacientes**. Resultado:
tornillos IS en 25 pacientes (38 tornillos) y **ningún TS** en el conjunto (#165). **No lo pide ningún objetivo:**
sirve para describir los datos en la tesis y para saber qué tornillos reales sirven de referencia.

### 4.2 Lo que sí filtra: tres capas

**Capa 1 — por paciente (`experiments/exploration-3d/grupos.csv`).** Cada paciente cae en un grupo:
grupo 1 = material ortopédico; grupo 2 = solo objetos no ortopédicos (catéteres, cremalleras…); grupo 3 = sin
ningún objeto; más los excluidos y los volúmenes repetidos. Hoy: 59 / 41 / 66. El sintetizador **solo aprende de
grupo 1**, y el muestreador y la prueba de rayas usan pelvis **sin osteosíntesis**.

**Capa 2 — por pieza de metal (criterio R1–R3, `experiments/objetivo3/a5_criterio_inclusion.py`).** La unidad es
el **componente**: cada pieza de metal conectada (> 2500 HU). La pregunta de cada regla no es "¿esto es un tornillo?"
sino **"¿este ejemplo enseña algo que en la síntesis será falso?"**:

- **R1 — dentro del cuerpo.** Se calcula la máscara del cuerpo (> −400 HU, el trozo conectado más grande, con huecos
  rellenos; descarta mesa y tubos) y se quita todo metal fuera de ella: un electrodo o una cremallera sobre la piel
  tienen aire alrededor, y el tornillo sintético siempre va dentro del hueso.
- **R2 — el paciente tiene material ortopédico** (grupo 1). Si no tiene, ninguna de sus piezas puede ser un implante.
- **R3 — el recorte contiene metal de esa pieza** (más una parte declarada de recortes "solo banda").
- **Tamaño y forma no filtran.** El modelo aprende "metal → rayas", que es física: filtrar por forma de tornillo
  habría tirado la mayoría de los datos (en 40 piezas revisadas, solo 5 eran tornillos). Sobre esas 40, el
  criterio coincidió con tu revisión en 36 de 39 decisiones.

**Capa 3 — limpieza manual.** Se quitaron 3 piezas no ortopédicas que tu revisión ya había identificado (dos trozos
de una pulsera y un DIU, #167), y los volúmenes repetidos de un mismo paciente (#163, #166). Límite declarado: en
19 de los 39 pacientes de entrenamiento hay además algún objeto no ortopédico; la regla es por paciente y solo una
muestra de piezas se revisó una a una.

**Y para comparar con lo real** no se usan todos los implantes: solo los **tornillos intraóseos aislados** (sin placa)
que tú confirmaste en cortes. En validación son los 2 tornillos de `metal_0039`.

---

## 5. Objetivo 3: el modelo que dibuja el tornillo

### 5.1 Qué modelo es

Un **modelo de difusión** (aprende a quitar ruido de una imagen paso a paso; al revés, "inventa" imagen a partir de
ruido) que **rellena un hueco**: borra la zona alrededor del tornillo y la vuelve a pintar con metal y rayas.
Lo de fuera del hueco se copia tal cual, así que el resto de la anatomía queda intacto **por construcción**.

| Variable | Valor elegido | Por qué |
|---|---|---|
| Red | **U-Net de difusión**, 4 niveles (64, 128, 256, 512 canales), atención en el nivel más bajo, float32 | Arquitectura estándar de difusión sobre imagen; nada exótico que defender |
| Dimensión | **2.5D**: 3 cortes axiales seguidos, genera el central | Ve a sus vecinos (continuidad 3D) sin el costo en memoria y datos de un modelo 3D |
| Entrada | 3 cortes × 3 ventanas = 9 canales, + máscara `M` + región `G` = **11 canales** | Las máscaras le dicen dónde va el metal y qué zona puede tocar |
| Ventanas de HU (`pub+asinh`) | ancha LW **[−1000, 20000]** comprimida con asinh; media MW **[−320, 480]**; estrecha SW **[−160, 240]** | Una sola escala no ve a la vez el metal (miles de HU) y el hueso (cientos); asinh deja caber el metal sin aplastar lo demás |
| Región que pinta | `G = M ∪ B_δ`: el tornillo más una **banda de 12 mm** alrededor | Las rayas se extienden fuera del metal; si solo pintara el tornillo, no habría rayas |
| Pérdida | error cuadrático **solo dentro de `G`** | Fuera de `G` no hay nada que aprender |
| Qué predice | **`v`** (en vez del ruido) | Más estable con rangos muy grandes, como el metal |
| Ruido | programa **coseno**, 1000 pasos; muestreo **DDIM de 50 pasos** | Estándar; DDIM es rápido y, con semilla fija, repetible |
| Semillas | **5 por paciente** (0–4) | Mide cuánto varía el resultado de una muestra a otra (entra en `Δ`, §7) |
| Entrenamiento (**run04**) | **14 182 recortes de 39 pacientes**, 60 000 pasos; validación 896 recortes de 3 pacientes | run04 es el único modelo vigente: se reentrenó tras hallar un paciente repetido entre entrenamiento y prueba (#166) |
| Punto de control | **`run04_mejor`**, paso 16 500 (mínimo de la pérdida de validación); `run04_60k` (paso final) como sensibilidad | Lo eligió el cotejo contra tornillos reales (§8), no la pérdida |

Código: `src/renderizador/` (modelo y datos), `experiments/objetivo3/a7_run04.sbatch` (entrenamiento),
`a15_cadena_completa.py` (pelvis limpia → pose → máscara → generación).

### 5.2 Cómo se leen los HU de la salida

El modelo devuelve las tres ventanas; hay que volver a un solo número en HU. La regla (`regla_suave`, en
`src/common/ventanas.py`) parte de la ventana ancha y la corrige con cada ventana estrecha, que pesa menos cuanto más
cerca está de su techo o su suelo (allí ya no informa). Con `u` el valor normalizado de un canal estrecho:

```
d = min(u, 1 − u)                                    (distancia al borde de la ventana)
w = clip( (d − 0.01) / (δ − 0.01), 0, 1 )            (peso del canal estrecho)
HU = w · HU_estrecho + (1 − w) · HU_anterior          (primero MW, después SW)
```

`δ` se calibró en validación: **0.030** para `run04_mejor` y **0.050** para `run04_60k` (`a16_calibrar_delta.py`).

### 5.3 Cómo se coloca el tornillo sintético (y la corrección del 12 de octubre)

El tornillo sintético es un **cilindro de 4.91 mm** (el cuerpo de los tornillos reales del conjunto, sin la rosca)
puesto **en el eje del corredor sin perturbar** (para la prueba de rayas). Su máscara es `M`.

**Corrección importante (#173).** El 12 de octubre viste en los HTML que el tornillo no caía en el sacro. La causa:
el Objetivo 2 mide el eje sobre la TC girada a una orientación estándar (RAS+), y el Objetivo 3 lo dibujaba sobre la
TC en su orientación original (LPS), sin convertir. El tornillo quedaba **reflejado**, fuera del hueso. Se corrigió
(`pose_a_marco_crudo` en `a11_rasterizar_tornillo.py`) y se agregó un **control de pose** que detiene el caso si más
del 5 % de `M` cae en aire o si la mediana de HU dentro de `M` queda más de 150 HU bajo lo medido en el eje por el
Objetivo 2. Los 15 pacientes lo pasan (ej. `0101`: 84 HU frente a 68). **Todo lo que usaba el tornillo sintético se
rehízo**; lo anterior está archivado en `experiments/obsoletos/objetivo3/outputs/pose_espejada/`.

---

## 6. ¿Qué es Peters?

**Peters et al. (2025)** (`docs/literatura/peters2025hybrid.md`) es un trabajo de física médica que hizo dos cosas:

1. **Validó un simulador físico de rayos X** (CatSim/XCIST): mete un metal virtual en una TC real, simula cómo
   atravesarían los rayos X ese cuerpo con metal (haz de varias energías, ruido, detector) y reconstruye la imagen.
   Comprobaron contra un maniquí físico que el simulador se desvía **menos del 2 %** del escáner real.
2. **Definió métricas** para medir artefactos metálicos, entre ellas la ***streak amplitude*** (amplitud de las
   rayas), que es la métrica principal de esta tesis.

**Para qué lo usamos.** Como **referencia física**: es la forma "por física" de hacer lo mismo que el sintetizador
hace "por aprendizaje". Si el sintetizador produce rayas de amplitud parecida a las de Peters sobre el mismo
paciente y el mismo tornillo, es coherente con la física. **Analogía:** el sintetizador es un dibujante rápido; Peters
es la simulación lenta pero con leyes físicas; se compara el dibujo con la simulación.

**Límites que se declaran:** su protocolo es **2D** (un corte, una fila de detector), es lento (por eso se simula uno
de cada dos cortes) y sus metales eran formas aleatorias, no implantes. Y lo medido hoy dice que **exagera** las
rayas frente a los tornillos reales (§8): sirve de comparación, **no es la verdad**.

**Material.** El tornillo real puede ser de acero o titanio, y la colección no lo registra. Se simulan los dos (Fe y
Ti). Una regla escrita antes eligió el que más se parece a los tornillos reales: ganó **titanio**, pero por poco.
Tu lectura, ya registrada: *ningún material reproduce lo real; el titanio es el menos alejado* (#174).

Código: `experiments/objetivo3/a19_peters_completo.py` (y `peters/`), `a21_cotejo_material.py`.

---

## 7. Las comparaciones que se hacen

### 7.1 E-A2 — rayas sobre pelvis sin metal (el experimento principal)

Sobre **13 pacientes de prueba sin metal**, el mismo tornillo en la misma pose se produce de **tres formas**:

| Brazo | Qué es | Papel |
|---|---|---|
| **Sintetizador** | el modelo de difusión (5 semillas) | lo que se evalúa |
| **Peters** | la simulación física (Ti principal, Fe sensibilidad; 2 réplicas A y B) | referencia física |
| **Copia y pegado** | pintar `M` con un HU fijo (**5371 HU**, la mediana del metal real de entrenamiento), sin rayas | piso: lo mínimo que hay que superar |

**La métrica: *streak amplitude*.** Con `Δ_img = imagen con tornillo − imagen original` (en Peters: reconstrucción
con metal menos sin metal), en anillos alrededor del tornillo (de 1 vóxel a 12 mm, perpendiculares a su eje, sin
8 mm en cada punta):

```
amplitud(anillo) = media del 5 % más alto de Δ_img  −  media del 5 % más bajo
valor del paciente = mediana sobre anillos   (sintetizador: mediana de 5 semillas; Peters: de A y B)
```

**Las dos pruebas:**

- **Cordura frente a copia y pegado:** Wilcoxon de rangos con signo, una cola, α = 0.05. Que el sintetizador haga
  más rayas que "pegar metal" es lo mínimo; no prueba calidad.
- **Principal frente a Peters Ti: TOST (equivalencia).** Con `d_i` = amplitud del sintetizador − la de Peters en el
  paciente i (n = 13):

  ```
  IC90 = d̄ ± t(0.95, 12) · s_d / √13
  equivalentes  ⇔  IC90 ⊂ [−Δ, +Δ]
  ```

  **El margen `Δ`** dice qué diferencia se considera "despreciable". Se fijó con una fórmula escrita antes de ver
  datos: `Δ = max(s, r)`, donde `s` es cuánto varía el sintetizador entre sus 5 semillas y `r` cuánto varía Peters
  entre sus 2 réplicas, medidos en los 2 pacientes de validación. Idea: no se le puede pedir al sintetizador
  parecerse a Peters más de lo que se parece a sí mismo.

**Declarado desde el inicio:** con 13 pacientes, el resultado honesto puede ser "no se pudo concluir equivalencia".

### 7.2 E-A1 — reconstruir implantes reales

En los **13 pacientes de prueba con metal**: se borra el implante real y su banda, se le pide al modelo que los
repinte con la máscara real y se compara con la TC real (error medio absoluto en HU dentro de `G`, en `M` y en la
banda; integridad de hueso y de metal adaptadas de Peters). Es descriptivo. Código: `a23_ea1.py`.

### 7.3 Realismo

El perfil de HU por anillos de 1 mm alrededor del tornillo (mediana y percentil 95) y el histograma dentro de `M`
del sintetizador se comparan con los de los **tornillos aislados reales** de prueba. Descriptivo, sin prueba de
hipótesis.

---

## 8. Lo último obtenido (12 de octubre, con la pose corregida)

Todo en **validación** (2 pacientes sin metal, `0101` y `0102`, frente a los 2 tornillos reales de `metal_0039`).
Resumen versionado: `experiments/objetivo3/resultados_validacion_pose.md`.

| Qué | Resultado | Lectura simple |
|---|---|---|
| **Cotejo del punto de control** (`a17`) | `run04_mejor` **13** de 24 anillos dentro de lo real; `run04_60k` 7 | El paso 16 500 se parece más a los tornillos reales. Confirmado por ti |
| **Material de Peters** (`a21`) | Ti 2 de 24, Fe 0 de 24; Ti queda **sobre** lo real en 22 | Peters exagera las rayas con los dos; Ti es el menos alejado |
| **`Δ`** (`a20`) | **196.3 HU** (principal); 115.8 HU (`run04_60k`); `r` de Peters = 6.1 HU | El margen lo fija la variabilidad del propio sintetizador |
| **Amplitudes** | sintetizador 1248 / 1182 HU; Peters Ti 1881 / 1287 HU | El sintetizador hace rayas **más débiles** que Peters: −633 HU en `0101`, −104 en `0102` |
| **Corrida final** | sintetizador (2 puntos de control), Peters y E-A1: **generadas**, sin errores | Falta medirlas |
| **HTML** | 60 vistas (3D y cortes) en `outputs/obj3_pose/{final,delta}/<punto>/html/` | Para revisar a ojo que el tornillo cae en S1 |

**Lo que eso anticipa (sin ser resultado):** en validación la diferencia media con Peters (≈ −369 HU) ya es mayor que
el margen (196 HU). Es probable que la prueba final **no** concluya equivalencia; la tesis ya lo aceptó por escrito
como resultado válido. Además, el sintetizador queda **bajo** Peters, y Peters **sobre** lo real: el sintetizador
podría estar más cerca de los tornillos reales que la física simulada. Eso lo dirá el realismo (§7.3).

---

## 9. Lo que queda pendiente, en orden

1. **Evaluar la prueba final de rayas (E-A2):** `a20` sobre los 13 pacientes de prueba (los dos brazos) → `a24`
   (Wilcoxon y TOST, con el principal y la sensibilidad `run04_60k` con sus dos márgenes).
2. **Resumir E-A1** (`a23`, ya generado) y el **realismo** frente a los tornillos reales de prueba.
3. **Redacción:** pasar al capítulo 3 las cifras nuevas (en curso, ronda r18) y escribir el capítulo 4 (resultados)
   cuando existan.
4. **Decisiones tuyas abiertas:** los `\GAPDEC` del capítulo 3 (16) y las implicancias abiertas (#162, #165,
   #167, #168, #175).
5. **Fuera de esta tesis (trabajo futuro):** el efecto sobre un segmentador, y un posible run05.

---

## 10. Archivos para el asesor

| Para ver | Archivo |
|---|---|
| Pregunta, hipótesis y alcance | `docs/00-tesis.md` |
| Datos y conteos | `docs/02-datos.md` |
| Hallazgos que cambiaron el plan | `docs/04-implicancias.md` (#173–#175 son los de hoy) |
| Diseño congelado del Objetivo 3 | `experiments/objetivo3/diseno_A.md` (sección 0 + enmiendas) |
| Índices de experimentos | `experiments/objetivo2/EXPERIMENTOS.md`, `experiments/objetivo3/EXPERIMENTOS.md` |
| Muestreador y SAP | `src/muestreador/muestreo.py`, `src/muestreador/sap.py` |
| Corredor | `experiments/objetivo2/e9_corredor.py`, `outputs/e9ts_ejes_corredor.csv` |
| Censo de tornillos y grupos | `experiments/exploration-3d/tornillos_conteo.csv`, `grupos.csv` |
| Criterio de entrenamiento | `experiments/objetivo3/a5_criterio_inclusion.py` |
| Cadena del Objetivo 3 | `a11_rasterizar_tornillo.py`, `a15_cadena_completa.py`, `a20_evaluador_ea2.py`, `a24_contrastes.py` |
| Resultados de hoy | `experiments/objetivo3/resultados_validacion_pose.md` |
| Documento de tesis | `overleaf/` (PDF en `redaccion/.build/main.pdf`) |
