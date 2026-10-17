# Revisión guía CS — capitulo1 — r11

## Hallazgos
| ID | Sev | Criterio | Ubicación | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T3 | capitulo1.tex:31 | Patrón PAT-14 reincide. En la ley de Beer--Lambert, $L$ designa la trayectoria del rayo, pero `capitulo3.tex:180` usa $L$ para la longitud del corredor; la bitácora del 2026-10-03 reserva expresamente $L$ para esta segunda magnitud. | Cambiar solo el símbolo de la trayectoria de integración en la ecuación de Beer--Lambert y reservar $L$ para la longitud del corredor en todo el documento. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | cumple |
| G-T3 | no cumple (guia-1) |
| G-T4 | cumple |
| G-T5 | cumple (el orden interno se justifica en `capitulo1.tex:13` y la transición hacia el estado del arte y la propuesta se delimita en `capitulo1.tex:11`) |
| G-T6 | cumple (lint PASA) |
| G-B1 | cumple |
| G-B2 | cumple |
| G-B3 | cumple |
| G-B4 | cumple |
| P-MT1 | cumple |
| P-MT2 | cumple (`fig:mt-conceptos` enlaza los fundamentos con los objetivos y remite al diagrama del pipeline) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patrón (una línea, generalizable a otras secciones) | Criterio | Ejemplo antes (máx. 15 palabras) | Ya en bitácora (PAT-n o "nuevo") |
|---|---|---|---|
| Un símbolo del marco se reutiliza para otra magnitud en el método | G-T3 | «integral de $\mu$ sobre la trayectoria $L$» | PAT-14 |

TOTAL alta=0 media=1 baja=0
