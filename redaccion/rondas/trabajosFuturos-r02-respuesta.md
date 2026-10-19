# Trabajos futuros r02 — corrección puntual del índice

| Hallazgo | Decisión | Detalle |
|---|---|---|
| `trabajosFuturos.tex`:2 — «TRABAJOSFUTUROS» en el índice | APLICADO | Se restituyó el espacio en `\addcontentsline`; también en `\markboth` (línea 3), para que el encabezado use el mismo título. El título visible del capítulo (línea 1) ya estaba correcto. |

`TOTAL alta=0 media=0 baja=0` tras la corrección. Sin GAP abiertos ni cerrados.

Verificación: `python scripts/lint_redaccion.py trabajosFuturos` → PASA. Compilación directa con `pdflatex` en dos pasadas → PDF de 194 páginas; `main.toc`:66 y el índice extraído del PDF muestran «TRABAJOS FUTUROS». Se usó `pdflatex` porque `latexmk` no puede ejecutarse en este equipo sin Perl. Copia de etapa: `redaccion/.build/etapas/trabajosFuturos-r02-puntual.pdf`.

## Patrones

| Patrón | Criterio | Ejemplo antes | Ya en bitácora |
|---|---|---|---|
| El título escrito manualmente en el índice diverge del título del capítulo | E-T1 | «TRABAJOSFUTUROS» frente a «TRABAJOS FUTUROS» | nuevo |

## Decisiones de redacción

Mantener idéntico el texto del capítulo, del índice y del encabezado.
