# Respuesta de redacción — capitulo1-r08

| Hallazgo | Revisor | Decisión | Detalle |
|---|---|---|---|
| Convención bilateral de la prueba exacta de Fisher sin respaldo | Encargo GAPLIT 2026-10-14 | APLICADO | Se integró `fay2010two`: la convención bilateral adoptada es \emph{minlike} y suma las probabilidades de tablas con probabilidad menor o igual que la observada. La atribución a `fisher.test` se acotó a la versión 2.11.0 de `stats` examinada por Fay; se conservó `fisher1935logic` para el fundamento condicional. Se cerró la marca. |

## Decisiones de redacción

- La convención bilateral \emph{minlike} se define por la suma de probabilidades de tablas no más probables que la observada.
- Una conducta de `fisher.test` documentada para una versión concreta de `stats` no se generaliza a versiones no verificadas.
