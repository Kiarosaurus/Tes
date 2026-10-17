# Revisión guía CS — capitulo1 — r12

## Hallazgos
| ID | Sev | Criterio | Ubicación | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T2 | capitulo1.tex:37 | Patrón PAT-3 reincide. `recorte por defecto` aparece aquí por primera vez y condiciona la cifra de 0.42, pero su definición operacional como modelo de recorte de 6 mm recién se da en `capitulo3.tex:105`. | Definirlo brevemente en esta primera aparición (por ejemplo, como el recorte de 6 mm de TotalSegmentator) y conservar la remisión al método para el detalle. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | no cumple (guia-1) |
| G-T3 | cumple |
| G-T4 | cumple |
| G-T5 | cumple |
| G-T6 | cumple (lint PASA) |
| G-B1 | cumple |
| G-B2 | cumple |
| G-B3 | cumple |
| G-B4 | cumple |
| P-MT1 | cumple |
| P-MT2 | cumple (`fig:mt-conceptos` enlaza los fundamentos con las piezas de la propuesta) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patrón (una línea, generalizable a otras secciones) | Criterio | Ejemplo antes (máx. 15 palabras) | Ya en bitácora (PAT-n o "nuevo") |
|---|---|---|---|
| Término técnico usado antes de su definición formal | G-T2 | «con el recorte por defecto» | PAT-3 |

TOTAL alta=0 media=1 baja=0
