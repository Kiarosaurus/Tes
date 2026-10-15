# Inventario de lo visto — Objetivo 3 (D-extra 4, `01-decisiones.md` 2026-10-15 punto 20)

> Registro fechado de que resultados se vieron, para auditar que reglas son "previas". Se agrega una fila **cada vez**
> que la autora o Claude miran un resultado nuevo de v2 o de prueba. Reconstruido el 2026-10-15 desde `ESTADO.md`,
> `04-implicancias.md` y los logs versionados; las fechas anteriores al 2026-10-15 son las de esos registros.

| fecha | que se vio | particion | modelo(s) | fuente | decisiones posteriores afectadas |
|---|---|---|---|---|---|
| 2026-10-12 | salidas de prueba en HTML (`a25`) e inspeccion visual del artefacto | prueba | run04 | #176 | todo lo de v2; QC visual de run04 no ciego |
| 2026-10-13 | TOST, Wilcoxon y E-A1 de prueba | prueba | run04_mejor, run04_60k | `resultados_prueba_v1.md`, #177 | diseno de v2; D1-D16 |
| 2026-10-14 | regla de eleccion de v2 (perfil 2-10 mm, salvaguarda 0-2 mm, a17) | validacion | run04, run05a, run05b | `run05/v2_eleccion.md`, #182 | analisis exploratorio de v2 |
| 2026-10-14 | HTML de validacion de los tres modelos (`a25`) | validacion | run04, run05a, run05b | ESTADO 2026-10-14 (3) | D3 a ciegas (no ciega para validacion) |
| 2026-10-15 | E-A1 en prueba | prueba | run05a, run05b (frente a run04) | #184 | D-extra 3 |
| 2026-10-15 | `Delta` de run05a (157.1 HU) y amplitudes de validacion de run05b (a20 parcial, job 56847) | validacion | run05a, run05b | `outputs/obj3_v2/v2_prueba/` | D15-D16 (margen) |
| 2026-10-15 | CV, correlacion y Pitman-Morgan entre brazos; suelo por vanos; ruido de Peters; voxeles por brazo | prueba (v1) y entrenamiento/validacion | run04_mejor | #185, #186 | D1, D-extra 1-2 |

**No visto a la fecha de `01-decisiones.md` 2026-10-15:** ningun TOST, Wilcoxon ni amplitud de prueba de run05a o
run05b (E-A2); ninguna salida de las mediciones nuevas (D1, D2, D5, D7, D8, D9, D12, D-extra 1-3).
