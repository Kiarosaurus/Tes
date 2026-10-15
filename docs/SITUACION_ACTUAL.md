# Situación actual de MetalSynth-Pelvis, explicada en simple

> **Corte del estado: 14 de octubre de 2026.** Lectura de unos 15 minutos, pensada para mostrar el avance al asesor.
> Explica **solo lo vigente**: lo que quedó superado está en `experiments/obsoletos/` y no se cita. La versión anterior
> al entrenamiento y evaluación de `run05a`/`run05b` está en el historial de git; la versión del 8 de octubre, más
> larga y con la historia de cada decisión, se recupera con `git show e7417ad:docs/SITUACION_ACTUAL.md`.
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
| **3. Sintetizador** | ¿Se puede dibujar el tornillo y sus rayas de forma creíble? | **Versión 1 evaluada; versión 2 no la mejora según la regla fijada; análisis exploratorio en curso** | `experiments/objetivo3/`, `src/renderizador/` |
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

| Variable | Valor elegido | Archivo fuente | Por qué |
|---|---|---|---|
| Red | **U-Net de difusión**, 4 niveles (64, 128, 256, 512 canales), atención en el nivel más bajo, float32 | `src/renderizador/modelo.py` (`UNetDifusion`) | Arquitectura estándar de difusión sobre imagen; nada exótico que defender |
| Dimensión | **2.5D**: 3 cortes axiales seguidos, genera el central | `src/renderizador/datos.py` (`ParchesMetal`); `src/renderizador/modelo.py` | Ve a sus vecinos (continuidad 3D) sin el costo en memoria y datos de un modelo 3D |
| Entrada principal | 3 cortes × 3 ventanas = 9 canales, + máscara `M` + región `G` = **11 canales** | `src/renderizador/datos.py` (`ParchesMetal.__getitem__`); `src/renderizador/modelo.py` (`CANALES_ENTRADA`) | Las máscaras le dicen dónde va el metal y qué zona puede tocar; `run05b` ensayó un duodécimo canal (§5.4) |
| Ventanas de HU (`pub+asinh`) | ancha LW **[−1000, 20000]** comprimida con asinh; media MW **[−320, 480]**; estrecha SW **[−160, 240]** | `src/common/ventanas.py` (`canales_diseno_a`) | Una sola escala no ve a la vez el metal (miles de HU) y el hueso (cientos); asinh deja caber el metal sin aplastar lo demás |
| Región que pinta | `G = M ∪ B_δ`: el tornillo más una **banda de 12 mm** alrededor | `experiments/objetivo3/a11_rasterizar_tornillo.py` (`BANDA_MM`, `rasteriza`); `src/common/region.py` | Las rayas se extienden fuera del metal; si solo pintara el tornillo, no habría rayas |
| Pérdida | error cuadrático **solo dentro de `G`** | `src/renderizador/difusion.py` (`perdida`) | Fuera de `G` no hay nada que aprender |
| Qué predice | **`v`** (en vez del ruido) | `src/renderizador/difusion.py` (`Difusion`, `perdida`) | Más estable con rangos muy grandes, como el metal |
| Ruido | programa **coseno**, 1000 pasos; muestreo **DDIM de 50 pasos** | `src/renderizador/difusion.py` (`betas_coseno`, `Difusion`, `muestrea_ddim`); `experiments/objetivo3/a15_cadena_completa.py` (`--pasos`) | Estándar; DDIM es rápido y, con semilla fija, repetible |
| Semillas | **5 por paciente** (0–4) | `experiments/objetivo3/a15_cadena_pose.sbatch` (`COMUN`); `experiments/objetivo3/a15_cadena_completa.py` (`--semillas`) | Mide cuánto varía el resultado de una muestra a otra (entra en `Δ`, §7) |
| Entrenamiento principal (**run04**) | **14 182 recortes de 39 pacientes**, 60 000 pasos; validación 896 recortes de 3 pacientes | `experiments/objetivo3/a7_run04.sbatch`; `experiments/objetivo3/a5_manifiesto_train_run04.csv`; `experiments/objetivo3/a5_manifiesto_val.csv` | Sigue siendo el modelo principal: se reentrenó tras hallar un paciente repetido entre entrenamiento y prueba (#166), y la versión 2 no cumplió la regla para reemplazarlo (#182) |
| Punto de control | **`run04_mejor`**, paso 16 500 (mínimo de la pérdida de validación); `run04_60k` (paso final) como sensibilidad | `src/renderizador/entrenar.py` (selección de `mejor.pt`); `experiments/objetivo3/outputs/a7/run04/curva.csv` (paso observado) | Lo eligió el cotejo contra tornillos reales (§8), no la pérdida |

La columna «Archivo fuente» indica dónde se implementa o, cuando es un resultado de la corrida, dónde queda
registrado cada valor. Código de la cadena completa: `a15_cadena_completa.py` (pelvis limpia → pose → máscara →
generación).

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

### 5.4 Versión 2: `run05a` y `run05b`

Después de evaluar la versión 1 se observó que sus rayas se apagaban hacia los 6 mm, mientras que en las piezas
reales de tamaño tornillo el exceso de amplitud llegaba aproximadamente a 10 mm. Por eso se probaron dos cambios
posteriores y exploratorios, con **los mismos datos, arquitectura base, 60 000 pasos y presupuesto** de `run04`:

| Corrida | Qué cambia frente a `run04` | Mejor punto de validación |
|---|---|---|
| **`run05a` (D)** | Los 2 888 recortes de componentes de 500–4000 mm³ se sobremuestrean de 20.36 % a 50 % (factor 3.91), y la pérdida pesa ×3 el anillo de 2–10 mm | paso 21 000; pérdida 0.0597 |
| **`run05b` (D + B)** | Todo lo anterior + un canal `T` con una plantilla analítica aproximada de endurecimiento del haz, calculada desde `M` | paso 21 000; pérdida 0.0596 |

La compuerta previa del canal `T` se superó (`e = 0.116`, `p = 0.0085`, 13 pacientes con control), pero eso solo
autorizaba entrenar `run05b`: no demostraba que el modelo completo fuera mejor. Los dos entrenamientos terminaron
correctamente el 14 de octubre; sus metadatos y curvas versionadas están en `experiments/objetivo3/run05/`.

La elección se hizo **solo en validación** (`0101` y `0102`, 5 semillas), con una regla aprobada antes de generar con
las corridas nuevas. Se comparó el error medio `E` frente al perfil real en 2–10 mm, se exigió una mejora mínima de
10 % y se descartó cualquier candidato cuya desviación en 0–2 mm superara en más de 20 % la de `run04`:

| Modelo | `E` en 2–10 mm (menor es mejor) | Desviación en 0–2 mm | Decisión |
|---|---:|---:|---|
| `run04_mejor` | 532.8 HU | 233 HU | referencia; pasa |
| `run05a_mejor` | 418.2 HU | 284 HU | descartado por la salvaguarda (tope 279.6 HU) |
| `run05b_mejor` | 367.0 HU | 540 HU | descartado por la salvaguarda |

**Resultado formal:** la versión 2 **no mejora** a `run04` según la regla fijada, aunque ambas corridas reducen el
error entre 2 y 10 mm. Por eso `run04_mejor` sigue siendo el modelo principal y no se hizo una corrida final
confirmatoria con la versión 2. Como la decisión depende de solo 2 pacientes y `run05a` excedió el tope por 4 HU,
`run05a` y `run05b` se están midiendo también en prueba, lado a lado y **solo como análisis exploratorio posterior**;
esa comparación no puede cambiar retrospectivamente el modelo principal. Detalle: `v2_plan.md` y
`run05/v2_eleccion.md`.

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

## 8. Lo último obtenido (14 de octubre)

### 8.1 Resultado principal de la versión 1 en prueba

| Qué | Resultado | Lectura simple |
|---|---|---|
| **E-A2 principal: `run04_mejor` frente a Peters Ti** | diferencia media **−301.0 HU**, IC90 **[−477.0, −124.9]**, `p_TOST = 0.845`, n = 13 | **No se concluye equivalencia**; el sintetizador produce rayas más débiles |
| **Cordura frente a copia y pegado** | Wilcoxon una cola `p = 0.000122`, n = 13 | El difusor sí supera el piso sin rayas, pero eso no demuestra equivalencia física |
| **Sensibilidad `run04_60k`** | −384.0 HU, IC90 [−566.5, −201.4]; no equivale con su margen (115.8 HU) ni con el principal (196.3 HU) | La conclusión no depende del checkpoint ni del margen elegido |
| **E-A1, grupo ortopédico** | n = 9; MAE en `G` 270.9 HU, en `M` 2312.5 HU y en la banda 198.0 HU | Reconstruir el metal sigue siendo mucho más difícil que reconstruir su entorno |
| **E-A1, objetos no ortopédicos** | n = 4; MAE en `G` 199.8 HU, en `M` 2747.9 HU y en la banda 165.8 HU | Resultado descriptivo y fuera de la distribución de entrenamiento |

El resultado principal estaba fijado antes de tocar prueba y queda en
`experiments/objetivo3/resultados_prueba_v1.md`. `run04_mejor` sigue siendo el modelo de tesis.

### 8.2 Resultado de selección de la versión 2

En validación, `run05a` y `run05b` acercaron las rayas al perfil real entre 2 y 10 mm, pero empeoraron la zona de
0–2 mm y fallaron la salvaguarda. El cotejo descriptivo contra los dos tornillos de `metal_0039` tampoco favoreció
a `run05b`: quedaron dentro de la envolvente real 13 de 24 cáscaras con `run04`, 13 con `run05a` y 9 con `run05b`.
Por la regla completa, **gana `run04_mejor`** (§5.4).

La evaluación exploratoria de `run05a` y `run05b` en los 13 pacientes de prueba está en curso. Se declararon antes
de iniciarla su carácter posterior, el uso del `Δ` propio de cada modelo y la obligación de mostrar los tres modelos
lado a lado sin escoger un ganador en prueba.

---

## 9. Lo que queda pendiente, en orden

1. **Terminar el análisis exploratorio de `run05a` y `run05b` en prueba:** E-A2 (13 pacientes, 5 semillas, `a20` →
   `a24`) y E-A1, siempre lado a lado con `run04` y sin reelegir el modelo principal.
2. **Completar la comparación visual a ciegas** D3 de los tres modelos y el **realismo** frente a los tornillos
   reales de prueba.
3. **Redacción:** incorporar por separado el resultado principal de `run04` y el análisis posterior de la versión 2;
   luego escribir el capítulo 4 con las cifras cerradas.
4. **Decisiones tuyas abiertas:** los `\GAPDEC` del capítulo 3 (16) y las implicancias abiertas (#162, #165,
   #167, #168, #175).
5. **Fuera de esta tesis (trabajo futuro):** medir el efecto del sintetizador sobre un segmentador.

---

## 10. Archivos para el asesor

| Para ver | Archivo |
|---|---|
| Pregunta, hipótesis y alcance | `docs/00-tesis.md` |
| Datos y conteos | `docs/02-datos.md` |
| Hallazgos que cambiaron el plan | `docs/04-implicancias.md` (#173–#182 cubren la pose corregida, la versión 1 y la versión 2) |
| Diseño congelado del Objetivo 3 | `experiments/objetivo3/diseno_A.md` (sección 0 + enmiendas) |
| Índices de experimentos | `experiments/objetivo2/EXPERIMENTOS.md`, `experiments/objetivo3/EXPERIMENTOS.md` |
| Muestreador y SAP | `src/muestreador/muestreo.py`, `src/muestreador/sap.py` |
| Corredor | `experiments/objetivo2/e9_corredor.py`, `outputs/e9ts_ejes_corredor.csv` |
| Censo de tornillos y grupos | `experiments/exploration-3d/tornillos_conteo.csv`, `grupos.csv` |
| Criterio de entrenamiento | `experiments/objetivo3/a5_criterio_inclusion.py` |
| Cadena del Objetivo 3 | `a11_rasterizar_tornillo.py`, `a15_cadena_completa.py`, `a20_evaluador_ea2.py`, `a24_contrastes.py` |
| Resultados vigentes | `experiments/objetivo3/resultados_prueba_v1.md`, `v2_plan.md`, `run05/v2_eleccion.md` |
| Documento de tesis | `overleaf/` (PDF en `redaccion/.build/main.pdf`) |
