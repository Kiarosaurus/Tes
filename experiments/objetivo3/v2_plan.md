# Version 2 del sintetizador: B + D (decidido por la autora el 2026-10-13) — plan de trabajo

> **Estado: PLANIFICADO, nada implementado.** Decision: `docs/01-decisiones.md` 2026-10-13. Implicancias: #176
> (diagnostico), #177 (resultado de la version 1). Este archivo fija QUE se hace y EN QUE ORDEN; los numeros concretos
> que todavia no estan fijados van marcados `[POR FIJAR]` y se fijan en este archivo **antes** de entrenar.

## 0. Por que existe una version 2, y lo que NO cambia

- **Motivo:** la version 1 genera bien junto al metal pero su artefacto se apaga hacia 6 mm, mientras que el de los
  tornillos reales sigue hasta ~10 mm (D1 con piezas tamano tornillo frente a D2; `d1_d2_resultado.md`). La banda de
  12 mm alcanza para tornillos: el defecto esta en lo que el modelo genera dentro de ella.
- **Declaracion obligatoria:** la version 2 se decide **despues** de ver salidas de prueba (HTML de `a25`, 2026-10-12)
  y el resultado de prueba de la version 1 (#177). Es **posterior y exploratoria**. La version 1 se reporta completa;
  la version 2 va al lado, nunca en su lugar.
- **No cambia:** la pose y el muestreador (Objetivo 2), la region `G = M U B_delta` con 12 mm, la copia exacta fuera de
  `G`, la representacion `pub+asinh`, la comparacion principal **frente a Peters Ti** con `streak amplitude` y TOST,
  la copia y pegado como piso, E-A1 y el realismo descriptivo. Peters no entra en el entrenamiento (sin circularidad).
  No se usan XCIST ni el conjunto AAPM para entrenar (autora, 2026-10-13).

## 1. Las dos intervenciones

### D — reentrenar con foco en tornillos (sin datos nuevos)

- **D-a, sobremuestreo:** los componentes tamano tornillo (500-4000 mm3, el mismo rango de D1) se muestrean con mas
  frecuencia en cada epoca. Motivo: el entrenamiento esta dominado por placas y componentes grandes (5 de 40
  componentes revisados eran tornillos, `a3_revision_componentes.md`). Factor: **`FRAC = 0.5` (fijado por la autora 2026-10-13)**: fraccion natural 0.2036 (2 888 de 14 182 parches, 45 componentes, 24 casos; `v2_d_componentes_run04.md`) -> factor 3.91.
- **D-b, peso de la perdida por distancia:** dentro de `G`, mas peso al anillo de 2-10 mm alrededor de `M`, donde D2
  mide el hueco (sintetico 488 / 97 / -65 / -40 HU frente a real 1199 / 765 / 473 / 174). Forma: escalon en 2-10 mm en el plano de `M`; **`PESO = 3` (fijado por la autora 2026-10-13)**.
- **Mismos datos que run04** (14 182 parches, 39 casos; validacion 896 / 3), mismos hiperparametros salvo lo anterior.
- Cambia el criterio R4 de `a5_criterio_inclusion.py` ("tamano y forma no filtran"): **no se filtra**, se sobremuestrea.
  Se declara como cambio de la version 2.

### B — plantilla analitica de endurecimiento del haz como canal de condicion

- **Que es:** un canal extra de entrada, calculado solo desde `M` en cada corte: proyeccion paralela de la mascara
  (longitudes en mm), no linealidad de endurecimiento del haz y retroproyeccion filtrada. Formula candidata segun la
  revision bibliografica de la autora (2026-10-13): `T = -FBP[ h(lambda * R(M)) ]`, `h(u) = log(sinh(u)/u)`.
  **Sin verificar contra los PDF:** la formula, su origen (Park, Choi y Seo 2017; Park et al. 2017 arXiv 1708.00244)
  y las condiciones en que produce rayas se confirman con `lector-papers` antes de implementar.
- **Nombre defendible:** "condicionamiento por un prior analitico aproximado de endurecimiento del haz". No es un
  simulador ni Peters; `lambda` no se calibra al escaner.
- **Compuerta previa (piloto, local, sin entrenar):** calcular `T` sobre los cortes reales de `M` (validacion) y sobre
  controles (disco, elipse, dos discos, rectangulo largo). Se sigue con B solo si `T` tiene senal fuera de `M` en
  2-10 mm y es estable al aumentar los angulos de proyeccion. Criterio numerico: ver "Compuerta de B" abajo
  (propuesto por Claude y APROBADO por la autora el 2026-10-13, antes de correr el piloto). Si falla, se sigue solo con D y se declara.
- **Implementacion:** `T` sobre el corte completo antes de recortar el parche, con espaciado fisico; misma definicion
  en entrenamiento (con la mascara del componente real) e inferencia (con el cilindro); normalizacion compartida.

### Compuerta de B (APROBADA por la autora 2026-10-13, ANTES de correr con datos reales; script `b_piloto_plantilla.py`)

Sin entrenar, local, sobre cortes de componentes tamano tornillo (500-4000 mm3) de entrenamiento de run04 y validacion,
con la seleccion de D1. `lambda0 = 1 / mediana(L_max)` (sin usar HU); mascara binaria; 360 angulos.
- **C0, validez numerica:** en controles sinteticos, `A_disco < 0.2 * A_dos_discos` (`A` = rms de la parte direccional
  de `T` en 2-10 mm / rms de `T` en `M`). La teoria predice ~0 fuera del disco (#178).
- **C1, estabilidad:** Spearman de la parte direccional de `T` entre 360 y 720 angulos, mediana por corte >= 0.9.
- **C2, coincidencia con lo real (decide):** parte direccional (menos la mediana por cascara de 1 mm) de `T` y del
  residuo real `D = HU(corte) - HU(referencia sin metal)` en 2-10 mm; `d = rho - rho_nulo` (nulo: `T` rotada 30-150 y
  210-330 grados); control anatomico `d0` = lo mismo con dos cortes sin metal (nulo de D1); `e = d - d0`. Medianas
  corte -> componente -> paciente. PASA si Wilcoxon de una cola `e > 0` entre pacientes da p < 0.05 y la mediana de
  `d` >= 0.05.
- B pasa si C0, C1 y C2 pasan. Sensibilidad que no decide: `lambda0 x 0.5`, `x 2`, mascara suavizada.
- Probado con datos sinteticos (no reales): controles C0 calculados (disco 0.0067, elipse 0.0642, dos discos 0.0902,
  estadio 0.1383: PASA; no usan datos); con anatomia alineada al tornillo y sin artefacto `e` < 0, con artefacto `e` > 0.

### Implementacion de D (2026-10-13, sesion cloud; probada solo con un cache de juguete)

- `src/renderizador/entrenar.py`: banderas `--componentes/--frac-tornillo` (D-a) y `--anillo-mm A B/--peso-anillo w`
  (D-b). Sin ellas el entrenamiento es el de run04 (curva identica bit a bit en el juguete).
- **D-a:** `WeightedRandomSampler` con reemplazo, `len(ds)` sorteos por epoca; peso `f = p (N - n) / ((1 - p) n)` a los
  parches de componentes tamano tornillo, de modo que salen con fraccion `p` por sorteo. La lista sale de
  `v2_d_componentes.py` (tabla versionada `v2_d_componentes_run04.csv`, aun por generar en local).
- **D-b:** mapa `w` = `peso` a `A`-`B` mm en el plano de `M` (EDT con el espaciado del corte, misma definicion de anillo
  que D1/D2), 1 en el resto; perdida = media ponderada dentro de `G` normalizada por la suma de pesos. Cortes sin metal
  del componente (banda mas alla de la punta): `w` = 1.
- **Validacion:** `perdida_val` sin ponderar (comparable con run04) elige `mejor.pt`; `perdida_val_pond` elige
  `mejor_pond.pt`. Cual se usa en la seleccion entre run05a, run05b y run04 es parte de la regla `[POR FIJAR]`.
- Controles nuevos al arrancar: peso uniforme = perdida de la version 1; fraccion sorteada a menos de 0.02 de `p`.
- `.sbatch`: `a7_run05a.sbatch`, aborta si no se pasan `FRAC` y `PESO` (los dos `[POR FIJAR]` de D).

## 2. Diseno de la comparacion (aisla cada efecto)

| Entrenamiento | D (sobremuestreo + peso) | B (canal `T`) | Para que |
|---|---|---|---|
| run04 (version 1, ya existe) | no | no | referencia |
| **run05a** | si | no | efecto de D |
| **run05b** | si | si | efecto de B sobre D (mismo todo lo demas) |

- Mismos datos, pasos y presupuesto. run05a y run05b pueden correr en paralelo en Khipu (QoS: 3 jobs).
- **Seleccion, solo en validacion:** perfil de D2 (2-10 mm frente a D1 tornillo) y cotejo de `a17`; regla de eleccion
  entre run05a, run05b y run04 `[POR FIJAR]` antes de generar. Prueba no se usa para elegir ni para ajustar `lambda`.
- **Corrida final de la version 2:** solo con el elegido; mismos 13 pacientes, mismo Peters (ya calculado: no se
  repite), mismo `a20` -> `a24`; `Delta` recalculado en validacion con la formula de siempre.

## 3. Orden de trabajo

1. **Lectura** (cuando la autora lo ordene): R3, R4 (y R9, R7, R8 si suben) con `lector-papers`; raw de cada uno en
   `refs/raw/`. Ver `docs/literatura/_candidatos.md`, ronda 2026-10-13.
2. **Scripts de D:** sobremuestreo y peso por distancia en `src/renderizador/` y el `.sbatch` de run05a; fijar los
   `[POR FIJAR]` de D en este archivo.
3. Piloto de B (despues de la lectura) -> compuerta -> canal `T` y `.sbatch` de run05b.
4. Fijar la regla de eleccion -> entrenar run05a / run05b -> validacion -> elegir -> corrida final -> `a20` / `a24`.
5. Redaccion (en pausa hasta aqui).
