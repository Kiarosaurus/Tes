# Eleccion de la version 2 (regla aprobada el 2026-10-14)

Generado por `v2_eleccion.py` desde `d2_perfil.csv`. Validacion (`0101`, `0102`), 5 semillas, `mejor.pt` de cada corrida. Real: D1 tornillo.

| punto | 0-2 | 2-4 | 4-6 | 6-8 | 8-10 | E (2-10 mm) | dev 0-2 | salvaguarda 0-2 | reemplaza al anterior |
|---|---|---|---|---|---|---|---|---|---|
| real D1 tornillo | 1930 | 1199 | 765 | 473 | 174 | | | | |
| run04_mejor | 1697 | 488 | 97 | -65 | -40 | 532.8 | 233.0 | pasa | - |
| run05a_mejor | 1646 | 608 | 207 | 79 | 44 | 418.2 | 284.0 | DESCARTADO | no |
| run05b_mejor | 1390 | 625 | 257 | 144 | 117 | 367.0 | 540.0 | DESCARTADO | no |

Regla: E = media de |sintetico - real| en 2-4, 4-6, 6-8 y 8-10 mm. Salvaguarda: dev 0-2 <= 20 % mas que la de run04. Se reemplaza al elegido solo con E al menos 10 % menor (orden de simplicidad: run04_mejor -> run05a_mejor -> run05b_mejor).

**RESULTADO: ningun modelo de la version 2 mejora a run04 en al menos 10 %. La version 2 se reporta como "no mejora" y no hay corrida final con ella.**

Limitacion: 2 pacientes de validacion; el cotejo de `a17` se reporta pero no decide.

## Cotejo de a17 (no decide)

# A17 — cotejo de checkpoint contra los tornillos reales de `metal_0039`

Generado por `a17_cotejo.py`. Referencia: 2 tornillos aislados de `metal_0039` (validacion; 01-decisiones.md 2026-10-08 (2)). Regla: 01-decisiones.md 2026-10-07 (2). Cascaras de 1 mm. **No elige: informa.**

## Referencia real

| componente | mm3 | cortes | M p50 | M p75 | M p95 |
|---|---|---|---|---|---|
| 1 | 2639 | 70 | 3838 | 4341 | 5262 |
| 2 | 1548 | 26 | 3092 | 3552 | 5304 |

## Resultado de la regla

| checkpoint | pacientes | semillas | dentro p50 | dentro p95 | dentro total | comparables | M p50 | M p95 | dist. hist. | rango max. entre semillas (HU) |
|---|---|---|---|---|---|---|---|---|---|---|
| run04_mejor | 2 | 5/5 | 9 | 4 | 13 | 24 | 3245 | 4856 | 648 | 393 |
| run05a_mejor | 2 | 5/5 | 5 | 8 | 13 | 24 | 3255 | 4658 | 835 | 295 |
| run05b_mejor | 2 | 5/5 | 2 | 7 | 9 | 24 | 3258 | 4524 | 967 | 320 |

**Gana por la regla: `run04_mejor`.** La eleccion la confirma la autora.

Con 1 paciente de referencia el cotejo descarta, no prueba. Cascaras comparables = con valor en lo real y en lo sintetico (con cascaras mas finas que el pixel, de 0.7-1 mm, algunas quedan vacias). Perfiles por cascara: `a17_perfiles.csv`.

