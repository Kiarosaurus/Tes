# Respuesta del redactor — capitulo3 — r21 (ronda acotada GAPLIT)

Entradas: `docs/literatura/xcist2026main.md` y `docs/literatura/xcist2025example.md`. Ronda única para cerrar la
referencia versionada del código de XCIST en la Sección~`Brazos de comparación`; no es una revisión general.

## Hallazgos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| `GAPLIT` de los repositorios publicados del protocolo físico | encargo 2026-10-14 | APLICADO | Se retiró la marca y se citaron `xcist2026main` y `xcist2025example` después de los commits revisados y de la licencia BSD 3-Clause. |
| Alcance de las fuentes versionadas | encargo 2026-10-14 | APLICADO | El fallo de serialización y el parche de una línea se presentan explícitamente como observaciones de la ejecución local sobre esas revisiones, no como hechos declarados por XCIST. |
| `GAPDEC` de la implicancia 158 | encargo 2026-10-14 | sin cambio | Se conservó íntegro: la ronda solo cierra la referencia versionada de las revisiones y la licencia. |

## Balance de GAP

- `\GAPLIT`: 1 -> 0; se cerró únicamente la referencia bibliográfica de los repositorios versionados de XCIST.
- `\GAPDATO`: sin cambios.
- `\GAPDEC`: sin cambios; la implicancia 158 permanece abierta.

## Decisiones de redaccion

- Los repositorios versionados respaldan su identidad, revisión y licencia; los fallos y modificaciones observados
  al ejecutarlos se atribuyen a la ejecución local de la tesis.

## Verificación

`python scripts/lint_redaccion.py capitulo3 --compilar` -> **PASA**, alta=0, media=0, baja=22, todas E-P1
preexistentes y documentadas en rondas anteriores. Compila en 137 páginas, sin referencias indefinidas. GAP final:
lit=0, dato=15, dec=16. PDF de etapa: `redaccion/.build/etapas/capitulo3-r21.pdf`.
