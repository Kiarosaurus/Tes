# A21 — material del brazo fisico frente a los tornillos reales de `metal_0039`

Regla: `01-decisiones.md` 2026-10-09 (5), escrita antes de correr (commit f9d27cc). Cascaras de 1 mm. **El difusor no interviene.**

Real: `M` p50 3838/3092 HU, p95 5262/5304 HU (los 2 tornillos).

| material | dentro p50 | dentro p95 | dentro total | comparables | bajo | sobre | M p50 | M p75 | M p95 | dist. hist. |
|---|---|---|---|---|---|---|---|---|---|---|
| Ti | 2 | 5 | 7 | 24 | 4 | 13 | 4499 | 5881 | 8236 | 3986 |
| Fe | 0 | 0 | 0 | 24 | 0 | 24 | 7209 | 9724 | 15544 | 14005 |

**Gana por la regla: `Ti`** -> material primario del TOST; el otro, sensibilidad.

Con 1 paciente de referencia el cotejo descarta, no prueba. Perfiles: `a21_perfiles.csv`.

Copia versionada de `outputs/a21/a21_cotejo_material.md`.

Por paciente: `0101` usa 12 cortes simulados con `M` y `0102` 5. Mediana de `M`:

| caso | Fe p50 | Fe p95 | Ti p50 | Ti p95 |
|---|---|---|---|---|
| 0101 | 10 691 | 18 339 | 5864 | 10 374 |
| 0102 | 3726 | 12 750 | 3134 | 6097 |

Todas las cifras en HU.

- Los dos materiales quedan sobre lo real en la mayoria de las cascaras (Fe en todas).
- El brazo fisico exagera el artefacto respecto de CLINIC-metal con cualquiera de los dos; con Ti, menos.
