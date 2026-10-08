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
| `exploration-2d/` (carpeta entera) | `experiments/exploration/` | exploracion 2D inicial (cribado por PNG, resumen del dataset, duplicados): superada por `exploration-3d/` | `exploration-3d/`. `explorar.py` aun lee de aqui `excluded_clinic_ids.csv` y `caracterizacion_metal_d7.csv` para la columna `Antecedente 2D` (ruta ya actualizada) |

Las salidas pesadas de cada experimento (`*/outputs/`) **no se movieron**: no estan versionadas y los
`.sbatch` las buscan en su sitio.
