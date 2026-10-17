# Respuesta del redactor — capitulo1 — r14

Reportes leidos: `capitulo1-r14-lint.md` (PASA; 1 baja), `-guia.md` (0), `-estilo.md` (media=1), `-trazabilidad.md` (0).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| ES-1 (E-M8), §Marco estadistico, cierre del parrafo de Fisher (l.153) | estilo | APLICADO (parcial) | Se deshace la ambiguedad sintactica: "un valor $p$ alto no permite distinguir entre la ausencia de asociacion y la falta de deteccion por el tamano de la muestra. Por ello, esas comparaciones se leen como sugerentes y no como concluyentes (Seccion sec:amenazas)." Dos cambios respecto de la propuesta: (1) se parte en dos oraciones, porque la version con punto y coma daba 41 palabras y el lint la marco E-O1 (media); (2) se conserva "no como concluyentes" en lugar de "no concluyentes", para que no se lea como el desenlace "no concluyente" de las dos pruebas unilaterales, cuyo nombre y mapeo (Walker y Nowacki, Lakens) quedaron fijados por #194 en el parrafo anterior. No contradice r11-r13: esta oracion no fue tocada en esas rondas (r11 ES-6 cambio solo la oracion previa sobre SciPy). Coherente con capitulo3:485 ("sugerente y no concluyente", mismo sentido descriptivo). Sin cifras nuevas. |
| Lint E-P1 baja (linea 57, constantes de la Ecuacion asinh) | lint | RECHAZADO (baja, ya respondido) | Falso positivo ya registrado en r13: son constantes de la definicion de la Ecuacion eq:asinh, no resultados. |

Lint final: `python scripts/lint_redaccion.py capitulo1 --compilar` -> PASA (alta=0 media=0 baja=1; GAP 0/0/0).

## Decisiones de redaccion

- Para calificar una prueba de hipotesis que no sea la de equivalencia como debil, se escribe "sugerente y no como concluyente" (con "como"), no el adjetivo suelto "no concluyente", que en el documento es el nombre de un desenlace de las dos pruebas unilaterales (#194).
