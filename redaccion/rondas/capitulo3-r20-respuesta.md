# Respuesta del redactor — capitulo3 — r20 (ronda acotada GAPLIT)

Entradas: `docs/literatura/salimans2022progressive.md` y reportes `capitulo3-r20-lint.md`, `-guia.md`, `-estilo.md`
y `-trazabilidad.md`. Ronda única para cerrar la fuente de la parametrización de predicción $v$ en la
Sección~`Sintetizador`; no es una revisión general. La GAPLIT del repositorio XCIST/CatSim no se modificó, porque las
fuentes nuevas no respaldan las revisiones ni la licencia declaradas en ese pasaje.

## Hallazgos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| `GAPLIT` de la parametrización de predicción $v$ | encargo 2026-10-14 | APLICADO | Se retiró la marca y se definieron $v = \alpha_t\epsilon - \sigma_t x$ y $\sigma_t^2 = 1 - \alpha_t^2$ para el proceso con preservación de varianza, con cita a Salimans y Ho~(`salimans2022progressive`). El texto limita el dominio evaluado por la fuente a imágenes naturales. |
| `GAPLIT` del repositorio publicado del protocolo físico | encargo 2026-10-14 | RECHAZADO | Se conserva sin cambios: la ficha de Salimans y Ho no documenta XCIST/CatSim, sus revisiones ni su licencia, y el encargo prohíbe atribuirle ese respaldo. |
| T01 (alta) | trazabilidad | APLICADO | Se retiró $z_t = \alpha_t x + \sigma_t\epsilon$, porque la tabla de evidencia textual de la ficha no acredita esa ecuación. La definición conserva solo $v = \alpha_t\epsilon - \sigma_t x$ y $\sigma_t^2 = 1 - \alpha_t^2$, ambas respaldadas por filas de evidencia. |
| S1 (media) | estilo | APLICADO | El párrafo abre por su función, la definición de $v$; la oración sobre la U-Net pasó al párrafo del entrenamiento. |
| S2 (media) | estilo | APLICADO | Se añadió el término inglés en la primera aparición: proceso con preservación de varianza (\emph{variance-preserving}). |
| S3 (media) | estilo | APLICADO | Se retiró la metadeclaración sobre lo que respalda la fuente. El texto dice directamente que Salimans y Ho evalúan la parametrización en imágenes naturales, no en TC, implantes ni condicionamiento anatómico. |

## Balance de GAP

- `\GAPLIT`: 2 -> 1; se cerró únicamente la parametrización de predicción $v$.
- `\GAPDATO`: sin cambios.
- `\GAPDEC`: sin cambios.

## Decisiones de redaccion

- La parametrización $v$ se presenta con la convención del proceso con preservación de varianza
  (\emph{variance-preserving}); el dominio evaluado por la fuente se nombra directamente, sin una metadeclaración.

## Verificación

`python scripts/lint_redaccion.py capitulo3 --compilar` -> **PASA**, alta=0, media=0, baja=22, todas E-P1
preexistentes y documentadas en rondas anteriores. Compila en 137 páginas, sin referencias indefinidas. GAP final:
lit=1, dato=15, dec=16.
