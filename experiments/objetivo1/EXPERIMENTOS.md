# Indice de experimentos del Objetivo 1

> **Para que existe.** Procedencia de artefactos: quien produjo cada cosa y si se puede usar. Mismo
> formato que `experiments/objetivo2/EXPERIMENTOS.md` (leyenda de `Origen` alli). No sustituye a
> `docs/ESTADO.md` ni a `docs/04-implicancias.md`. Manual del cluster: `experiments/KHIPU.md`.
>
> **Regla de mantenimiento:** al anadir un experimento, anadir su fila. Si queda superado y nadie lo
> importa, `git mv` a `experiments/obsoletos/objetivo1/` y anadir su fila en `experiments/obsoletos/README.md`.

**Resultado del Objetivo 1:** `p1_compuerta.md` — **NO-GO**, ninguna combinacion modelo x configuracion
baja de 25 HU de MAE en hueso en test. La continuacion del Objetivo 3 es una decision posterior y
declarada (`docs/00-tesis.md`).

## 1. E6a, E6c — representacion sin VAE

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `e6a_codificacion.py` / `.csv` / `.md` / `.log` | ida y vuelta HU -> multi-ventana -> HU, sin VAE; cota inferior | script | **VIGENTE** |
| `e6c_techo_lw.py` / `.csv` / `.md` | barrido del techo de la ventana ancha (#39) | script | **VIGENTE**. **NO MOVER:** lo importan `e6b`, `p1_*`, `objetivo3/a1*`, `a3`-`a5` y `src/common/ventanas.py` |

## 2. E6b — VAE de SD 1.5 sin reentrenar

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `e6b_vae_sd15.py` / `.sbatch` | ida y vuelta con el VAE de SD 1.5, 178 CT | Khipu 51540 | **VIGENTE** como evidencia: falla en 178/178 (#36/#39). **NO MOVER:** define `regla`, `eje_axial` y otros que importan P1, el Obj 3 y `src/common/ventanas.py` |
| `outputs/e6b_vae_sd15*.csv`, `.md` | resultados de la cohorte | Khipu 51540 | **VIGENTE** |
| `outputs/e6b_prueba/` | prueba corta de 1 caso antes de la cohorte (`KHIPU.md`, E6b paso 3) | Khipu | **NO ES RESULTADO** |

## 3. P1 — compuerta con decodificador afinado

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `p1_decodificador_sd15.py` | entrenamiento y evaluacion del decodificador afinado (encoder congelado) | script | **VIGENTE**. **NO MOVER:** de aqui salen `leer_particion`, `rutas`, `BDELTA_MM`, `ROIS` |
| `p1_entrenar.sbatch`, `p1_evaluar.sbatch` | jobs de P1 | Khipu | **VIGENTES** |
| `p1_particion.csv` | particion por paciente train/val/test | script | **VIGENTE**: la usan tambien el Objetivo 3 y `src/renderizador/` |
| `p1_control.csv`, `p1_eval.csv`, `p1_curvas/` | controles, evaluacion y curvas | Khipu | **VIGENTES** |
| `p1_compuerta.md` | veredicto del Go/No-Go en test | script | **VIGENTE — resultado del Objetivo 1** |

## 4. Archivados

| Artefacto | Donde | Motivo |
|---|---|---|
| `p1_maisi.py`, `p1_maisi.sbatch`, `p1_maisi_cota.csv` | `../obsoletos/objetivo1/` | MAISI descartado por diseno el 2026-09-20 (#93 CERRADA) |
