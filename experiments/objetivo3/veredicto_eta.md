# Veredicto etapa 0 de v3 (exploratorio, post-hoc)

Regla: 01-decisiones.md 2026-11-20. Criterio (a) desde los CSV; (b) 0-2 mm requiere NIfTI (no calculado).

## Control de validez

Max |p95 variante run04_mejor_p50_e0 - p95 octubre| en las 7 cascaras: **48.63 HU** (tol 1.00) -> NO REPRODUCE: el barrido no se interpreta

## Cascaras criticas con p95 dentro de la envolvente real

| variante | pacientes | dentro (de 7) | cascaras (mm) | criterio (a) >= 4 | criterio (b) 0-2 mm |
|---|---|---|---|---|---|
| run04_mejor_p100_e0.3 | 2 | 5 | 4,5,6,8,9 | PASA | PENDIENTE (b): rerun con NIfTI + d2 |
| run04_mejor_p200_e0 | 2 | 1 | 8 | no | n/a |
| run04_mejor_p50_e0 | 2 | 1 | 8 | no | n/a |
| run04_mejor_p50_e0.3 | 2 | 4 | 4,6,8,9 | PASA | PENDIENTE (b): rerun con NIfTI + d2 |
| run04_mejor_p50_e0.6 | 2 | 3 | 6,8,9 | no | n/a |

## p95 sintetico frente a la envolvente real (HU), cascaras criticas

| r (mm) | real lo | real hi | run04_mejor_p100_e0.3 | run04_mejor_p200_e0 | run04_mejor_p50_e0 | run04_mejor_p50_e0.3 | run04_mejor_p50_e0.6 |
|---|---|---|---|---|---|---|---|
| 4-5 | 759 | 832 | 794 | 701 | 690 | 762 | 755 |
| 5-6 | 692 | 759 | 719 | 635 | 625 | 646 | 670 |
| 6-7 | 596 | 775 | 694 | 584 | 579 | 614 | 632 |
| 8-9 | 516 | 714 | 578 | 548 | 543 | 546 | 581 |
| 9-10 | 496 | 632 | 512 | 478 | 472 | 509 | 537 |
| 10-11 | 533 | 659 | 496 | 434 | 432 | 495 | 515 |
| 11-12 | 487 | 629 | 453 | 403 | 403 | 433 | 463 |

Limites: 2 pacientes de validacion; un checkpoint; el criterio (b) no esta evaluado; resultado exploratorio.
