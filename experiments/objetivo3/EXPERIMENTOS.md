# Indice de experimentos del Objetivo 3

> **Para que existe.** Procedencia de artefactos: quien produjo cada cosa y si se puede usar. Mismo
> formato que `experiments/objetivo2/EXPERIMENTOS.md` (leyenda de `Origen` alli). No sustituye a
> `docs/ESTADO.md` (por donde voy) ni a `docs/04-implicancias.md`. El diseno del renderizador esta en
> `diseno_A.md`. Manual del cluster: `experiments/KHIPU.md`.
>
> **Regla de mantenimiento:** al anadir un experimento, anadir su fila. Si queda superado y nadie lo
> importa, `git mv` a `experiments/obsoletos/objetivo3/` y anadir su fila en `experiments/obsoletos/README.md`.
>
> **Modelo vigente: run04** (sin fuga, #166). Todo lo generado o medido con run01/run02 (`mejor_37k`) o run03 esta
> archivado en `experiments/obsoletos/objetivo3/outputs/` y **no es citable** (#166, #171). Resultados citables del
> Objetivo 3: solo los de la corrida final con run04 (`a15_final_run04`, `a23_final_run04`, `a24`), cuando existan.
> Las salidas (`outputs/`) no estan versionadas. Actualizado el 2026-10-11.

## 1. Diseno y datos de entrenamiento

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `diseno_A.md` | diseno del renderizador y de la evaluacion | autora + asistente | **CONGELADO** el 2026-10-09 (seccion 0) + **ENMIENDA 2026-10-11 (run04)**, antes de tocar test con run04 |
| `a1_parches.py`, `a1_casos.csv` | parches 2.5D **por corte** | script | **SUPERADO por A1b** (#102), congelado como evidencia de #102. **NO MOVER:** lo importan `a1b` y `src/common/region.py` |
| `a1b_parches_componente.py` | parches 2.5D **por componente** (decision D2) | script | **VIGENTE**. Lo importan `a3`, `a4`, `a15`, `a23` y `src/renderizador/datos.py` |
| `a3_laminas_componentes.py`, `a3_revision_componentes.csv` / `.md` | laminas de 40 componentes para fijar el criterio de implante (#104) | script + autora | **CERRADO**: 40 de 40 con veredicto; 3 no ortopedicos quitados del manifiesto de run04 (#167) |
| `a4_html_componentes.py` | vista 3D interactiva de componentes | script | **VIGENTE**. **NO MOVER:** `a5` importa `CUERPO_HU`, `mascara_cuerpo` |
| `a5_criterio_inclusion.py`, `a5_conjunto.csv` | criterio R1-R3 | script | **VIGENTE** (`01-decisiones.md`, 2026-09-21) |
| `a5_manifiesto_train_run04.csv` | entrenamiento de run04: **14 182 parches, 39 casos** | script + autora | **VIGENTE** (`01-decisiones.md` 2026-10-11) |
| `a5_manifiesto_val.csv` | validacion: 896 parches, 3 casos | script | **VIGENTE** |
| `a5_manifiesto_train.csv`, `_sin163.csv`, `_sin166.csv` | manifiestos de run01/run02, run03 y paso intermedio | script | **SUPERADOS** por `_run04` (#163, #166, #167). Se conservan por procedencia |

## 2. Entrenamiento

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a7_run04.sbatch` | entrenamiento de run04 (60 000 pasos, mismos hiperparametros que run02) | Khipu 55706 | **VIGENTE**. Salida en `outputs/a7/run04/`; minimo de validacion en el paso 16 500 (#168) |
| `a7_entrenar.sbatch`, `a7_run03.sbatch` | run01/run02 y run03 | Khipu | **SUPERADOS** (fuga, #166). Salidas archivadas |
| `a14_curvas.py` | grafico de curvas de entrenamiento | script | **VIGENTE** (herramienta) |
| `a13_comparar_ckpt.py` | dos checkpoints pareados sobre validacion | script | herramienta; sus salidas con run01/run02 estan archivadas |

## 3. Mediciones sin modelo y muestras

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a8_muestra_serie.py` | serie completa de cortes, HTML, `.nii.gz`, montaje | script | **VIGENTE** (herramienta); muestras con run01/run02 archivadas |
| `a9_suelo_representacion.py` | recorte del suelo de -1000 HU, sin modelo (#141) | script | **CORRIDO** sobre 23 058 parches; no usa el difusor |
| `a10_costura.py` | salto de HU en el borde de `G` (#139) | script | **VIGENTE** (herramienta) |
| `a12_roi_parametros.py` | perfil radial del artefacto real y parametros de las ROIs, sobre validacion | script | **CORRIDO**; no usa el difusor |
| `a16_calibrar_delta.py` | fija `delta` de `regla_suave` (v2, #152) | script | **CORRIDO**: `delta = 0.05` |
| `a22_hu_copiapega.py` | HU de la copia y pegado (mediana del metal de entrenamiento) | script | **CORRIDO con run04: 5371 HU** (`outputs/a22_run04/`) |

## 4. Cadena completa, cotejo y `Delta`

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a11_rasterizar_tornillo.py` | pose -> `M`, `B_delta`, `G` | script | **VIGENTE**; lo importa `a15` |
| `a15_cadena_completa.py` | pelvis limpia -> pose -> `M` -> generacion; **no reanudable** | script | **VIGENTE** |
| `a15_cotejo_run04.sbatch` + `a17_cotejo.py` | cotejo de checkpoint (1 mm, 5 semillas, `0101`/`0102`, ref. `metal_0039`) | Khipu 55820 + local | **CORRIDO**: gana `run04_mejor` 12 a 10 -> `a17_cotejo_resultado_run04.md` (#169) |
| `a15_delta_run04.sbatch` + `a20_evaluador_ea2.py` | `s` de `Delta` para los 2 checkpoints | Khipu 55825 + local | **CORRIDO**: `Delta` 163.8 / 100.3 HU -> `a20_resultados_run04.md` |
| `outputs/a15_delta_run04_shard/` | control shard frente a exclusiva sobre `0101` | Khipu 55858 | **CORRIDO**: identico bit a bit (#170) |
| `a15_cadena.sbatch`, `a15_cotejo.sbatch`, `a15_delta.sbatch` | versiones con `mejor_37k`/`run01` | Khipu | **SUPERADOS** por los `_run04` |
| `a17_cotejo_resultado.md`, `a20_resultados.md` | resultados con `mejor_37k` | local | **SUPERADOS** (salvo las filas de Peters de `a20_resultados.md`, que no usan el difusor) |

## 5. Brazo fisico (Peters / XCIST)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `peters/` | configuracion y parche del script publicado de XCIST, fuera del clon (#146) | script | **VIGENTE** |
| `sonda_peters.md`, `a18_sonda_peters.py` | sonda de viabilidad preinscrita (2026-10-09 (2)) | script | **CORRIDO** |
| `a19_peters_completo.py`, `a19_peters.sbatch`, `a19_final.sbatch` | brazo fisico en validacion y en los 13 de test | Khipu 55240, 55453 | **CORRIDO**, no usa el difusor: **vale con run04** (`r` = 23.2 HU) |
| `a21_cotejo_material.py`, `a21_resultado.md` | material primario frente a tornillos reales | script | **CORRIDO**: Ti primario, Fe sensibilidad |

## 6. Corrida final (test, diseno congelado + enmienda)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `casos_ea2_test.txt` | los 13 pacientes de test sin metal de E-A2 | script | **VIGENTE** |
| `a15_final_run04.sbatch` | difusor en los 13 de E-A2, un job por checkpoint (`CKPT=mejor` / `60k`) | Khipu 55859, 55911 | **EN CURSO** (2026-10-11), en `shard:a100_3g.20gb` (#170) |
| `a23_ea1.py`, `a23_final_run04.sbatch` | E-A1: reconstruccion del implante real en test con metal, `run04_mejor` | Khipu | **LISTO, sin lanzar** |
| `a24_contrastes.py` | TOST primario y sensibilidades; dos lecturas de `Delta` para `run04_60k` | script | **LISTO**, probado con datos de juguete |
| `a15_final.sbatch`, `a23_final.sbatch` | corrida final con `mejor_37k` | Khipu 55454, 55455 | **SUPERADOS** (fuga); resultados archivados, no citables (#164, #171) |

## 7. Archivados

Inventario completo en `experiments/obsoletos/README.md`.

| Artefacto | Donde | Motivo |
|---|---|---|
| `a2_entrenar.sbatch` | `../obsoletos/objetivo3/` | piloto de 200 pasos (job 52074, #89 medida); lo sustituye `a7_entrenar.sbatch` |
| `a6_muestra_minima.py` | `../obsoletos/objetivo3/` | primera muestra de un solo corte (#116); la sustituyen `a8` y `a15` |
| salidas de run01/run02/run03 y todo lo medido con ellas | `../obsoletos/objetivo3/outputs/` | modelo con fuga (#166) |
