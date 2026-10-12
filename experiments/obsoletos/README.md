# Experimentos obsoletos

> **Que hay aqui.** Pruebas, pilotos y versiones superadas que **no alimentan la ruta principal** de
> ningun objetivo: ningun script vigente los importa ni los lee, y ninguna cifra de `tesis/main.tex` ni de
> `overleaf/` sale de ellos. Se movieron aqui el 2026-10-08 con `git mv` (la historia de cada archivo se
> conserva: `git log --follow <ruta>`).
>
> **Que NO hay aqui.** Lo superado que todavia **se importa** sigue en su carpeta, marcado como SUPERADO en
> su `EXPERIMENTOS.md`: `objetivo2/e9_corredor.py`, `objetivo2/ts_piloto_qc.py`, `objetivo3/a1_parches.py`,
> `objetivo2/e13_poses_piloto.csv` (lo lee `verificar_coherencia.py`). Moverlos romperia imports.
>
> **Regla del proyecto:** no se borra evidencia. Archivar no es borrar.

## Citas con la ruta vieja

`docs/01-decisiones.md` (solo lo edita la autora), `docs/04-implicancias.md`, `docs/ESTADO.md` y
`redaccion/rondas/` citan estos archivos **con la ruta anterior**. No se reescribieron: son registros
fechados. Para resolver una cita vieja, buscar el nombre del archivo en la tabla de abajo.

## Los scripts no corren desde aqui

Calculan rutas relativas a su carpeta original (`Path(__file__).parents[...]`, imports de modulos
hermanos). Para reproducir uno, copiarlo de vuelta a su carpeta original o ajustar `sys.path`.

## Inventario

| Archivo | Ruta anterior | Por que quedo obsoleto | Lo sustituye |
|---|---|---|---|
| `objetivo1/p1_maisi.py`, `p1_maisi.sbatch` | `experiments/objetivo1/` | MAISI **descartado por diseno** (2026-09-20, paso 0): el bundle recorta a [-1000, 1000] HU y ese recorte solo ya da 42.24 HU de MAE en hueso. #93 CERRADA | nada: la via MAISI se cerro |
| `objetivo1/p1_maisi_cota.csv` | `experiments/objetivo1/` | tabla del paso 0 que cerro #93; evidencia del descarte | — |
| `objetivo2/r1_mosaico.py` | `experiments/objetivo2/` | mosaico de +-60 mm: el revisor objeto que no deja contar vertebras | `r2_nivel_pico_laminas.py` (lamina alargada). Su producto, `r1_auditoria_s1_clinico.csv`, **sigue vigente** en `objetivo2/` |
| `objetivo2/r1_revision_itksnap_revisor.csv` / `.md` | `experiments/objetivo2/` | 2da vuelta de S1 en ITK-SNAP que no se persiguio (0 de 61); se resolvio por lamina | `r1_revision_laminas_revisor.csv` |
| `objetivo2/r1_landmarks.v1-parcial.csv` | `experiments/objetivo2/` | v1 murio por memoria (17 de 178 filas) | `r1_landmarks.csv` |
| `objetivo2/r1_landmarks.v2a.csv` / `.md`, `r1_estados.v2a.csv` | `experiments/objetivo2/` | version previa de la deteccion | `r1_landmarks.csv`, `r1_estados.csv` |
| `objetivo2/r2_nivel_pico_revisor.ANTERIOR.md` | `experiments/objetivo2/` | instrucciones previas de R2 | `r2_nivel_pico_revisor.md` |
| `objetivo3/a2_entrenar.sbatch` | `experiments/objetivo3/` | piloto de 200 pasos para medir coste (job 52074, #89 medida) | `a7_entrenar.sbatch` |
| `objetivo3/a6_muestra_minima.py` | `experiments/objetivo3/` | primera muestra sintetica, UN corte (#116) | `a8_muestra_serie.py` (serie) y `a15_cadena_completa.py` (cadena) |
| `objetivo3/a7_entrenar.sbatch`, `a7_run03.sbatch` | `experiments/objetivo3/` | entrenamientos run01/run02 y run03: modelos con fuga (#166). Movidos 2026-10-12 | `a7_run04.sbatch` |
| `objetivo3/a15_cadena.sbatch`, `a15_cotejo.sbatch`, `a15_delta.sbatch`, `a15_final.sbatch` | `experiments/objetivo3/` | cadena, cotejo, `Delta` y corrida final con `run01_140k` / `mejor_37k` (#164, #166). Movidos 2026-10-12 | los `_run04.sbatch` |
| `objetivo3/a23_final.sbatch` | `experiments/objetivo3/` | E-A1 con `mejor_37k` (#164). Movido 2026-10-12 | `a23_final_run04.sbatch` |
| `objetivo3/a17_cotejo_resultado.md` | `experiments/objetivo3/` | cotejo que eligio `mejor_37k` (#157). Movido 2026-10-12 | `a17_cotejo_resultado_run04.md` |
| `objetivo3/a20_resultados.md` | `experiments/objetivo3/` | `Delta` = 188.7 con `mejor_37k`; sus filas de Peters siguen valiendo y estan repetidas en el sustituto. Movido 2026-10-12 | `a20_resultados_run04.md` |
| `exploration-2d/` (carpeta entera) | `experiments/exploration/` | exploracion 2D inicial (cribado por PNG, resumen del dataset, duplicados): superada por `exploration-3d/` | `exploration-3d/`. `explorar.py` aun lee de aqui `excluded_clinic_ids.csv` y `caracterizacion_metal_d7.csv` para la columna `Antecedente 2D` (ruta ya actualizada) |

### Scripts de `exploration-2d/` recuperados (2026-10-09)

Los 6 `.py` de `exploration-2d/` no estaban versionados. Vivian solo en Khipu, en `~/metalsynth/scripts/`,
desde el repo anterior (ya borrado). Se trajeron al convertir `~/metalsynth` en clon de este repo. Son
los que produjeron los CSV de esta carpeta. Leen de `~/metalsynth/data/extracted` y escriben en
`~/metalsynth/outputs` (rutas fijas de Khipu).

| Script | Produce |
|---|---|
| `describe_data.py` | `per_volume_stats.csv`, `dataset_summary.csv` |
| `screen_metal.py` | `metal_screening.csv`, `metal_png/` |
| `finalize_screening.py` | `duplicados.csv`, `excluded_clinic_ids.csv`, `ejemplos_seleccion.csv` |
| `check_dups.py` | verifica 3 pares de duplicados dataset6/dataset7; solo imprime |
| `gen_caracterizacion.py` | `caracterizacion_metal_d7.csv` |
| `reporte_semana.py` | `reporte_semana.md`, `cohorte_A_ids.txt`, `cohorte_B_ids.txt`, `macros_datos.tex` (reporte del 3 de septiembre). Lee `test_ids.txt` y `excluded_metal_ids.csv`, que no estan versionados |

Las salidas pesadas de cada experimento (`*/outputs/`) **no se movieron**: no estan versionadas y los
`.sbatch` las buscan en su sitio.

### Salidas del difusor con fuga (archivadas 2026-10-11, #166)

`metal_0003` (train) y `metal_0072` (test) son el mismo paciente (autora, 2026-10-11; regla (a): `0003`
sale de train). Todo modelo entrenado con `0003` y todo lo generado o medido con el queda superado. Por orden
de la autora se **movio** (no se borro; no versionado) de `experiments/objetivo3/outputs/` a
`experiments/obsoletos/objetivo3/outputs/`:

| Carpeta o archivo | Que es |
|---|---|
| `a2/` | piloto de entrenamiento de 200 pasos (job 52074) |
| `a7/` (`run01`, `run02` con `mejor.pt` = `mejor_37k`, `a14_curvas_run01_run02.png`) | entrenamientos del difusor |
| `a7_prueba/` | entrenamiento de prueba |
| `a6/`, `a8/`, `a8_mejor/` | muestras generadas con esos modelos |
| `a13/` | comparacion de checkpoints sobre validacion |
| `a15*` (`a15`, `a15_cotejo`, `a15_cotejo_1mm`, `a15_delta`, `a15_final`, `a15_gpu`, `a15_marcas`, `a15_v2`) y sus `.log`/`_memoria.csv`, `a15fin_55454.log` | cadena completa del difusor: cotejo, `Delta`, corrida final de E-A2 (#164) |
| `a16/`, `a16.log`, `a16_memoria.csv` | calibracion de `Delta` con el difusor |
| `a17/`, `a17_paso1mm/`, `a17_rep05/` | cotejo de checkpoint que eligio `mejor_37k` |
| `a20/`, `a24/` | E-A2 y contrastes (#164). E-A2 usa solo dataset6: la fuga no lo toca, pero el modelo se reemplaza |
| `a23_final/`, `a23fin_55455.log` | E-A1 (#164), incluye `0072` |

**Siguen en su sitio** porque no usan el difusor: `a1`, `a1b` (y caches), `a3`, `a5`, `a9` (mide sin modelo),
`a11`, `a12`, `a18*` y `a19*` incluido `a19_final` (Peters), `a21`, `a22`, `peters_run*.log`.

Los `.md` versionados que citan esas cifras (`objetivo3/a17_cotejo_resultado.md`, `a20_resultados.md`, #157,
#164) quedan como registro fechado. Las copias en Khipu (`$DATA/...`) no se tocaron.

### Salidas de `run04_mejor` leidas con 0.05 (archivadas 2026-10-12, #172 (A))

La recalibracion de `a16` con run04 dio 0.030 para `run04_mejor` (0.050 para `run04_60k`); la autora eligio que
cada punto de control se lea con su valor (#172, opcion (A)). Lo de `run04_mejor` leido con 0.05 queda superado y se
**movio** (no versionado) a `experiments/obsoletos/objetivo3/outputs/`:

| Carpeta o archivo | Que es |
|---|---|
| `a15_final_run04/run04_mejor_d005_cortado/`, `a15fin04_55859.log` | corrida final de test, cortada por tiempo en `0100` |
| `a15_delta_run04_mejor_d005/` | `s` de `Delta` (163.8 HU) en validacion |
| `a20_run04/a20_delta_run04_mejor.json` | `Delta` = 163.8 HU |
| `a17_run04_paso1mm_mejor_d005/` | cotejo `run04_mejor` (0.05) frente a `run04_60k` (12 frente a 10) |
| `a22_run02/` | HU de copia y pegado del conjunto de run02 (5373 HU); el vigente es `outputs/a22_run04/` |

**Siguen en su sitio** porque mezclan filas validas de `run04_60k` y los scripts filtran por etiqueta:
`a15_cotejo_run04/` y `a20_run04/a20_ea2.csv`. Las filas `run04_mejor` de esos dos no se usan.

### Todo lo generado con la pose espejada (archivado 2026-10-12, #173)

La pose del corredor del Objetivo 2 esta en el array reorientado a RAS+; `a11`, `a15`, `a18` y `a19` la rasterizaban
sobre el array crudo (LPS) sin convertir, y el tornillo quedaba reflejado en x e y, fuera del sacro. Corregido en
`a11.pose_a_marco_crudo` + `control_pose`. Todo lo que puso un tornillo sintetico queda superado.

**Versionados (`git mv`):**

| Archivo | Que era | Lo sustituye |
|---|---|---|
| `objetivo3/a17_cotejo_resultado_run04.md` | cotejo de run04 (12 frente a 10) | cotejo de `a15_cadena_pose.sbatch` |
| `objetivo3/a20_resultados_run04.md` | `Delta` (163.8 / 100.3 HU) | `Delta` con la pose corregida |
| `objetivo3/a21_resultado.md` | eleccion del material (Ti primario) | `a21` sobre `peters_val` de `a19_pose.sbatch` |
| `objetivo3/a15_cotejo_run04.sbatch`, `a15_delta_run04.sbatch`, `a15_final_run04.sbatch` | cotejo, `Delta` y corrida final de run04 | `a15_cadena_pose.sbatch` (las tres etapas en un job) |

**No versionados, en `objetivo3/outputs/pose_espejada/`:** `a11`, `a15_cotejo_run04`, `a15_delta_run04` (con sus
`html/`), `a15_delta_run04_shard`, `a15_final_run04` (con `html/`), `a18`, `a18_corrida1`, `a19`, `a19_final`,
`a19fin_55453.log`, `a20_run04`, `a21`, `peters_run1.log`, `peters_run2.log`.

**Siguen valiendo** (no ponen tornillo sintetico): `a16_run04` (0.030 / 0.050), `a22_run04` (5371 HU), `a7/run04`,
`a1b`, `a12`, `a9`, y E-A1 (`a23`, implantes reales).

