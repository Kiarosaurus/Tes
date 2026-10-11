# A20 run04 — `streak amplitude` de E-A2 en validacion y `Delta` (2026-10-11)

Reemplaza la parte del difusor y el `Delta` de `a20_resultados.md` (que eran de `mejor_37k`, modelo con fuga
#166). Peters no cambia: mismas filas, recalculadas desde `outputs/a19/` (|A-B| Fe = 34.1 y 12.3 HU, `r` = 23.2 HU).
Decisiones: `01-decisiones.md` 2026-10-11 (2) punto 2; #169 opcion (b).

- **Generacion:** job 55825 (`a15_delta_run04.sbatch`, `-p all --gres=gpu:a100_3g.20gb:1`), `--incluir-banda`,
  5 semillas, NIfTI, receptores `0101`/`0102`.
- **Evaluacion (local):** `a20_evaluador_ea2.py difusor --dir outputs/a15_delta_run04 --etiqueta <et> --out
  outputs/a20_run04/a20_ea2.csv` por caso y etiqueta; `a20_evaluador_ea2.py delta --csv outputs/a20_run04/a20_ea2.csv
  --etiqueta <et>` -> `outputs/a20_run04/a20_delta_<et>.json`.

## Difusor, amplitud por semilla (HU)

| checkpoint | caso | s0 | s1 | s2 | s3 | s4 | rango | ROIs | fraccion en el suelo de -1000 |
|---|---|---|---|---|---|---|---|---|---|
| run04_mejor | 0101 | 1014 | 1057 | 977 | 901 | 915 | 156.0 | 155 | 0.000 |
| run04_mejor | 0102 | 1238 | 1360 | 1291 | 1188 | 1214 | 171.7 | 154 | 0.000 |
| run04_60k | 0101 | 773 | 832 | 746 | 749 | 740 | 91.4 | 155 | 0.000 |
| run04_60k | 0102 | 1076 | 1106 | 1129 | 1020 | 1052 | 109.2 | 154 | 0.000 |

## `Delta = max(s, r)`

| checkpoint | `s` (HU) | `r` (HU) | **`Delta` (HU)** | lo fija |
|---|---|---|---|---|
| **run04_mejor** (principal) | 163.8 | 23.2 | **163.8** | el difusor |
| run04_60k (sensibilidad) | 100.3 | 23.2 | **100.3** | el difusor |
| *mejor_37k (archivado, con fuga)* | *188.7* | *23.2* | *188.7* | *el difusor* |

- `run04_mejor` genera rayas mas intensas que `run04_60k` (~+200 HU en `0101`, ~+180 HU en `0102`, medianas
  de semillas) y varia mas entre semillas.
- Cada checkpoint lleva su propio `Delta`: la sensibilidad de E-A2 con `run04_60k` se juzga con 100.3 HU, un
  margen mas estrecho. Ver #169.
