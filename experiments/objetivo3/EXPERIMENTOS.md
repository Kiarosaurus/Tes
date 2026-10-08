# Indice de experimentos del Objetivo 3

> **Para que existe.** Procedencia de artefactos: quien produjo cada cosa y si se puede usar. Mismo
> formato que `experiments/objetivo2/EXPERIMENTOS.md` (leyenda de `Origen` alli). No sustituye a
> `docs/ESTADO.md` (por donde voy) ni a `docs/04-implicancias.md`. El diseno del renderizador esta en
> `diseno_A.md`. Manual del cluster: `experiments/KHIPU.md`.
>
> **Regla de mantenimiento:** al anadir un experimento, anadir su fila. Si queda superado y nadie lo
> importa, `git mv` a `experiments/obsoletos/objetivo3/` y anadir su fila en `experiments/obsoletos/README.md`.
>
> **Ningun resultado de aqui es citable todavia como resultado del Objetivo 3**: falta `Delta`, y
> `diseno_A.md` sigue sin preinscribir. Las salidas (`outputs/`) no estan versionadas.

## 1. Diseno y datos de entrenamiento

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `diseno_A.md` | diseno del renderizador; D1-D4 resueltas el 2026-09-20 | autora + asistente | **BORRADOR, no preinscrito**: falta `Delta` |
| `a1_parches.py`, `a1_casos.csv` | parches 2.5D **por corte** | script | **SUPERADO por A1b** (#102), congelado como evidencia de #102. **NO MOVER:** lo importan `a1b` y `src/common/region.py` |
| `a1b_parches_componente.py` | parches 2.5D **por componente** (decision D2) | script | **VIGENTE**. Lo importan `a3`, `a4`, `a15` y `src/renderizador/datos.py` |
| `a3_laminas_componentes.py`, `a3_revision_componentes.csv` / `.md` | laminas de 40 componentes para fijar el criterio de implante (#104) | script + autora | **CERRADO**: 40 de 40 con veredicto |
| `a4_html_componentes.py` | vista 3D interactiva de componentes | script | **VIGENTE**. **NO MOVER:** `a5` importa `CUERPO_HU`, `mascara_cuerpo` |
| `a5_criterio_inclusion.py`, `a5_conjunto.csv`, `a5_manifiesto_train.csv` / `_val.csv` | criterio R1-R3 y conjunto de entrenamiento (17 149 parches train, 896 val) | script | **VIGENTE — CONGELADO** (`01-decisiones.md`, 2026-09-21) |

## 2. Entrenamiento

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a7_entrenar.sbatch` | entrenamiento con validacion y checkpoints reanudables | Khipu | **VIGENTE**. Corridas `run01` y `run02` en `outputs/a7/` (**no independientes**, #148) |
| `a14_curvas.py` | grafico de las curvas de `run01` y `run02` | script | **VIGENTE** -> `outputs/a7/a14_curvas_run01_run02.png` |
| `a13_comparar_ckpt.py` | dos checkpoints pareados sobre validacion | script | **CORRIDO, se conserva como evidencia**. Su lectura de #145 quedo revisada por #152 (decodificador v1) |

## 3. Mediciones sin modelo y muestras

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a8_muestra_serie.py` | serie completa de cortes, HTML, `.nii.gz`, montaje | script | **VIGENTE**, reanudable |
| `a9_suelo_representacion.py` | recorte del suelo de -1000 HU, sin modelo (#141) | script | **CORRIDO** sobre 23 058 parches |
| `a10_costura.py` | salto de HU en el borde de `G` (#139) | script | **CORRIDO** sobre las dos muestras de `a8` |
| `a12_roi_parametros.py` | perfil radial del artefacto real y parametros de las ROIs, sobre validacion | script | **VIGENTE**: referencia del cotejo. Pendiente ajustarlo a la decision 2026-10-07 (2) |
| `a16_calibrar_delta.py` | fija `delta` de `regla_suave` (v2, #152) | script | **CORRIDO**: `delta = 0.05` |

## 4. Cadena completa

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a11_rasterizar_tornillo.py` | pose -> `M`, `B_delta`, `G` | script | **VIGENTE**; lo importa `a15` |
| `a15_cadena_completa.py`, `a15_cadena.sbatch` | pelvis limpia -> pose -> `M` -> generacion; **no reanudable** | script / Khipu | **VIGENTE** |
| `outputs/a15_v2/` | 0101 y 0102, CPU, v2 `delta=0.05` | script | **VIGENTE — lo que vale hoy** |
| `outputs/a15/`, `a15_marcas/`, `a15_gpu/` | corridas con la lectura v1 (#150, #152, #151) | script / Khipu 54619 | **SUPERADAS por `a15_v2/`**, evidencia de esas implicancias. `a15/humo_2cortes/` no es resultado |

## 5. Brazo fisico (Peters / XCIST)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `peters/` | configuracion y parche del script publicado de XCIST, fuera del clon (#146) | script | **VIGENTE**: base de la sonda de viabilidad de Peters (pendiente) |

## 6. Archivados

| Artefacto | Donde | Motivo |
|---|---|---|
| `a2_entrenar.sbatch` | `../obsoletos/objetivo3/` | piloto de 200 pasos (job 52074, #89 medida); lo sustituye `a7_entrenar.sbatch` |
| `a6_muestra_minima.py` | `../obsoletos/objetivo3/` | primera muestra de un solo corte (#116); la sustituyen `a8` y `a15` |
