# A17 — resultado del cotejo de checkpoint (2026-10-09)

Copia versionada del resumen de `outputs/a17/a17_cotejo.md`; `outputs/` no esta versionado. Implicancia #157.

- **Insumo:** job Khipu 55130, `a15_cotejo.sbatch` (particion `all`, MIG `a100_3g.20gb`).
  - Receptores `dataset6_CLINIC_0101` (25 cortes con `M`) y `0102` (10 cortes).
  - 2 checkpoints x 5 semillas, todo en GPU.
  - Salida local: `outputs/a15_cotejo/`.
- **Referencia real:** 2 tornillos aislados de `metal_0039` (01-decisiones 2026-10-08 (2)).
  - Comp. 1: 2639 mm3, 70 cortes, `M` p50/p75/p95 = 3838/4341/5262 HU.
  - Comp. 2: 1548 mm3, 26 cortes, 3092/3552/5304 HU.
- **Regla:** 01-decisiones 2026-10-07 (2). Agregacion corte -> semilla -> paciente -> checkpoint por medianas,
  confirmada por la autora el 2026-10-09.

| checkpoint | dentro p50 | dentro p95 | dentro total | comparables | `M` p50 | `M` p95 | dist. hist. | rango entre semillas (HU) |
|---|---|---|---|---|---|---|---|---|
| run01_140k | 5 | 3 | 8 | 46 | 3280 | 4309 | 1159 | 238 |
| mejor_37k | 4 | 3 | 7 | 46 | 3194 | 4429 | 1125 | 643 |

**Gana por la regla `run01_140k`, por una cascara.** La eleccion la confirma la autora.

Cascaras respecto de la envolvente real (23 cascaras con valor por curva):

| checkpoint | curva | bajo | dentro | sobre |
|---|---|---|---|---|
| run01_140k | p50 | 10 | 5 | 8 |
| run01_140k | p95 | 20 | 3 | 0 |
| mejor_37k | p50 | 13 | 4 | 6 |
| mejor_37k | p95 | 20 | 3 | 0 |

Mas alla de 3 mm, la mediana de (p95 sintetico - borde inferior real) es -212 HU para `run01_140k` y -193 HU
para `mejor_37k`.

El p50 sintetico alterna entre cascaras vecinas. Explicacion probable, sin verificar: cascaras de 0.5 mm con
pixel de 0.896 mm.
