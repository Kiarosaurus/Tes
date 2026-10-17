# Revisión guía CS — capitulo2 — r09

## Hallazgos
| ID | Sev | Criterio | Ubicación | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T1, G-B5, G-B8, P-EA3 | capitulo2.tex:112, 114, 124, 126; anexos.tex:30 | Patrón PAT-183 reincide. El cierre y la fila propia todavía presentan el contraste de realismo como «pendiente» y mantienen en `\REVVISUAL` el supuesto, la banda y el aporte. Esto ya no coincide con la formulación vigente del Objetivo~3: `introduccion.tex:98` declara que no se reclama realismo visual, que el contraste no se ejecutó y que queda como trabajo futuro. Así, la comparación contra el objetivo y el resumen de la contribución conservan un alcance anterior. | Retirar las marcas `\REVVISUAL`; en la fila propia y en el cierre, sustituir «pendiente» por «diseñado y no ejecutado» y declarar una sola vez que el realismo visual no se reclama y queda como trabajo futuro. Reformular «la banda para los efectos de adquisición» como propósito de diseño, no como capacidad demostrada, sin alterar el desenlace no concluyente frente al protocolo físico. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | no cumple (guia-1) |
| G-T2 | cumple |
| G-T3 | cumple |
| G-T4 | cumple |
| G-T5 | cumple |
| G-T6 | cumple |
| G-B5 | no cumple (guia-1) |
| G-B6 | cumple (la revisión narrativa y dirigida y su procedimiento se declaran en l. 12) |
| G-B7 | cumple |
| G-B8 | no cumple (guia-1: la fila propia conserva el estado anterior del contraste de realismo) |
| G-B9 | cumple |
| G-B10 | cumple (la brecha de capitulo2.tex:116 coincide con introduccion.tex:66) |
| P-EA1 | cumple |
| P-EA2 | cumple con GAP (capitulo2.tex:98 declara las cifras de ablación pendientes de verificación) |
| P-EA3 | no cumple (guia-1) |

## Propuestas de criterio

Ninguna.

## Patrones
| Patrón (una línea, generalizable a otras secciones) | Criterio | Ejemplo antes (máx. 15 palabras) | Ya en bitácora (PAT-n o "nuevo") |
|---|---|---|---|
| Una tabla que resume la sección conserva el estado anterior tras una decisión | G-B8, G-T1 | «contraste de realismo pendiente» | PAT-183 |

TOTAL alta=0 media=1 baja=0
