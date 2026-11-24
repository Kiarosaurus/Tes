# Veredicto etapa 0 de v3 (exploratorio, post-hoc)

Regla: 01-decisiones.md 2026-11-20. Criterio (a) desde los CSV; (b) 0-2 mm requiere NIfTI (no calculado).

## Control de validez

Control NO evaluado (falta --control o la variante p50_e0). **El barrido no es interpretable sin el.**

## Cascaras criticas con p95 dentro de la envolvente real

| variante | pacientes | dentro (de 7) | cascaras (mm) | criterio (a) >= 4 | criterio (b) 0-2 mm |
|---|---|---|---|---|---|
| b_min_l0 | 2 | 0 | - | no | n/a |
| b_min_l0.8_t1000 | 2 | 3 | 6,8,9 | no | n/a |
| b_min_l3_t300 | 2 | 2 | 8,9 | no | n/a |

## p95 sintetico frente a la envolvente real (HU), cascaras criticas

| r (mm) | real lo | real hi | b_min_l0 | b_min_l0.8_t1000 | b_min_l3_t300 |
|---|---|---|---|---|---|
| 4-5 | 759 | 832 | 603 | 832 | 977 |
| 5-6 | 692 | 759 | 571 | 769 | 909 |
| 6-7 | 596 | 775 | 530 | 720 | 850 |
| 8-9 | 516 | 714 | 445 | 573 | 644 |
| 9-10 | 496 | 632 | 422 | 514 | 551 |
| 10-11 | 533 | 659 | 414 | 462 | 509 |
| 11-12 | 487 | 629 | 396 | 393 | 431 |

Limites: 2 pacientes de validacion; un checkpoint; el criterio (b) no esta evaluado; resultado exploratorio.
