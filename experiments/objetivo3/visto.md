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
| 2026-10-15 | `a26` sobre el CSV congelado de v1: desenlaces D15 con *t* y permutacion, margen minimo (477.0 HU), Bland-Altman | prueba (v1) | run04_mejor, run04_60k | `a26` (scratchpad; se rehace sobre la variante `base`) | ninguna (lecturas ya fijadas) |
| 2026-10-15 | D8: preservacion de Peters fuera de `G` (RMSE mediana 31.4 HU, SSIM 0.907) | prueba | Peters (sin metal) | `outputs/obj3_pose/a27/` | ninguna |
| 2026-10-15 | D4: diametro semimaximo - 2500 HU en componentes 500-4000 mm3 de entrenamiento (E8) | entrenamiento | — | `resultados_dec_2026-10-15.md` | ninguna |
| 2026-10-15 | `a20` de prueba en 8 variantes (base, inter, suelo, sincabeza, anillos 8-16 mm) con brazo parametrico; `a26` sobre cada una | prueba (v1) | run04_mejor, parametrico | `resultados_dec_2026-10-15.md`, #187 | ninguna (lecturas ya fijadas; v2 sigue sin ver) |
| 2026-10-15 | D-extra 2: piso de ruido del difusor (`G` sin `M`, 893 HU mediana) | prueba | run04_mejor | `resultados_dec_2026-10-15.md`, #188 | ninguna (pto 18 ya fijado) |
| 2026-10-15 | TOST, permutacion, margen y acuerdo de v2 en prueba, 8 variantes (`a26` de Khipu) | prueba | run05a, run05b | `resultados_dec_2026-10-15.md`, #190 | ninguna previa; todo lo que se decida despues es posterior para v2 |
| 2026-10-15 | E-A1 de v2 con `--delta` 0.03 (D-extra 3) | prueba | run05a, run05b | idem, #190 | ninguna |
| 2026-10-15 | D7: p95 con solo LW frente a regla_suave | validacion | run04_mejor | `outputs/obj3_pose/a28/`, #191 | ninguna (regla fijada antes) |

**No visto a la fecha de `01-decisiones.md` 2026-10-15:** ningun TOST, Wilcoxon ni amplitud de prueba de run05a o
run05b (E-A2); ninguna salida de las mediciones nuevas (D1, D2, D5, D7, D8, D9, D12, D-extra 1-3).
