# A17 — cotejo de checkpoint de run04 (2026-10-11)

> **AVISO 2026-10-12 (#172, opcion (A)):** aqui `run04_mejor` esta leido con 0.05, no con su valor calibrado (0.030). Las filas de `run04_60k` siguen valiendo. El cotejo con cada punto de control en su valor sale del job 56176 (`a15_cotejo_run04_d003`) y va en un archivo aparte.

Reemplaza a `a17_cotejo_resultado.md` (run01/run02, modelo con fuga #166) para la eleccion de checkpoint.
Candidatos y regla fijados antes de generar: `01-decisiones.md` 2026-10-11 (2).

- **Generacion:** job 55820 (`a15_cotejo_run04.sbatch`, `-p all --gres=gpu:a100_3g.20gb:1`), receptores
  `dataset6_CLINIC_0101_data` y `0102`, 5 semillas, cascaras de 1 mm. Log: `fin ... rc=0`, CONTROL 1 PASA en
  los dos receptores.
- **Cotejo:** `python experiments/objetivo3/a17_cotejo.py --dir-sintetico experiments/objetivo3/outputs/a15_cotejo_run04 --paso-mm 1 --out-dir experiments/objetivo3/outputs/a17_run04_paso1mm`
  (local). Salida: `outputs/a17_run04_paso1mm/{a17_cotejo.md, a17_perfiles.csv}`.
- **Referencia:** 2 tornillos de `metal_0039` (2639 y 1548 mm3; `M` p50/p95 = 3838/5262 y 3092/5304 HU).

| checkpoint | dentro p50 | dentro p95 | dentro total | comparables | `M` p50 | `M` p95 | dist. hist. | rango entre semillas (HU) |
|---|---|---|---|---|---|---|---|---|
| run04_mejor (paso 16 500) | 9 | 3 | **12** | 24 | 3297 | 4641 | 810 | 342 |
| run04_60k | 9 | 1 | 10 | 24 | 3500 | 5157 | 160 | 243 |

**Gana por la regla: `run04_mejor`** (12 frente a 10 cascaras). No hay empate, asi que el desempate por
histograma no se aplica. La eleccion la confirma la autora.

Cascaras respecto de la envolvente real (calculado desde `a17_perfiles.csv`):

| checkpoint | curva | bajo | dentro | sobre |
|---|---|---|---|---|
| run04_mejor | p50 | 0 | 9 | 3 |
| run04_mejor | p95 | 8 | 3 | 1 |
| run04_60k | p50 | 3 | 9 | 0 |
| run04_60k | p95 | 10 | 1 | 1 |

- El p95 bajo lo real (#157) sigue con los dos candidatos, mas marcado en `run04_60k`.
- `run04_mejor` gana en el perfil pero queda mas lejos dentro de `M` (dist. hist. 810 frente a 160 HU; `M`
  p95 4641 frente a ~5283 de la referencia). La regla no usa el histograma salvo empate. Ver #169.
- Con 1 paciente de referencia el cotejo descarta, no prueba.
