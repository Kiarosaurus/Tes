# Abstract r02 — traducción simultánea del resumen

Modo: corrección única y simultánea con `resumen.tex`. Se mantuvieron el título inglés ya decidido, las cinco palabras clave equivalentes y la correspondencia de 3/4/6/3 oraciones.

| Control | Resultado | Fuente |
|---|---|---|
| Problema, cadena y evaluación separada | Traducción de la introducción del resumen, sin ampliar el alcance. | `resumen.tex`:4; `introduccion.tex`:13-15. |
| Método y resultados | Misma secuencia, cifras, comparadores y cautelas; *streak amplitude* conserva su nombre publicado y su explicación funcional. | `resumen.tex`:6-8; `conclusiones.tex`:14-22. |
| Conclusión y límites | Conserva la insuficiencia del realismo visual, el perfil espacial y la segmentación no evaluada. | `resumen.tex`:10; `conclusiones.tex`:30, 36, 38. |

Verificación: `python scripts/lint_redaccion.py abstract --compilar` → PASA, documento completo de 194 páginas; `TOTAL alta=0 media=0 baja=0`. Sin GAP nuevos o cerrados.

## Patrones

Sin patrones adicionales a los documentados en `resumen-r02-respuesta.md`.

## Decisiones de redacción

Se tradujeron las ideas oración por oración, con sintaxis inglesa natural y las mismas condiciones de las comparaciones; no se añadieron resultados.
