# Respuesta del redactor — capitulo1 — r13

Reportes leidos: `capitulo1-r13-lint.md` (PASA; 1 baja), `-guia.md` (0), `-estilo.md` (media=3), `-trazabilidad.md` (0).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| ES-1 (E-O2, E-M1; PAT-58), §TC, parrafo de la retroproyeccion | estilo | APLICADO | Parrafo partido tras "...como artefacto (Seccion mt-artefactos)". El nuevo abre con oracion tematica que enlaza con el anterior: "De ese proceso de medida y reconstruccion se derivan los dos dominios que distingue este documento: ...". Se evito abrir con "Este documento ...", que habria repetido la apertura "Este trabajo usa ..." del mismo apartado (PAT-119). Contenido y referencias sin cambios. |
| ES-2 (E-O2, E-M1; PAT-58), §TC, codificaciones del Objetivo 1 | estilo | APLICADO | Parrafo partido antes de la tercera codificacion. Para que la apertura se sostenga sola, "La tercera conserva" pasa a "La tercera codificacion conserva". El bloque nuevo reune la Ecuacion asinh, su lectura y la pendiente (5 oraciones); el anterior queda en 4. |
| ES-3 (E-O2, E-M1; PAT-58), §Marco estadistico, Wasserstein-1 | estilo | APLICADO | Parrafo partido tras la reduccion a suma (Ecuacion w1). "Su unidad es el grado" no servia como oracion tematica de un parrafo nuevo; se reescribe como "La distancia se expresa en grados de la escala de brecha." Siguen los dos ejemplos (1 y 3) y la ventaja frente a la fraccion de grado 0. Sin cifras nuevas. |
| Lint E-P1 baja (linea 57, constantes de la Ecuacion asinh) | lint | RECHAZADO (baja, ya respondido) | Falso positivo ya registrado: -1000, 20 000, 500, -2 y 40 son las constantes de la definicion de la Ecuacion eq:asinh, cuya fuente se dio en rondas previas; no son resultados. |

Control PAT-119: revisadas todas las aperturas de §TC tras las divisiones ("Una TC...", "La imagen se obtiene...", "De ese proceso...", "Los valores de TC...", "Las mascaras oseas...", "Varias de las redes...", "La codificacion multiventana...", "Este trabajo usa...", "La tercera codificacion...", "El paso de ida y vuelta...", "Las tres codificaciones...") y de §Marco estadistico ("Cada objetivo...", "Para comparar distribuciones...", "La distancia se expresa...", "El Objetivo 3 plantea..."): no hay dos aperturas contiguas con el mismo arranque.

Lint final: PASA (alta=0, media=0, baja=1; GAP lit=0 dato=0 dec=0), compila (165 paginas). Sin GAP abiertos ni cerrados; `MAPA.md` sin cambios en la tabla de GAP.

## Decisiones de redaccion

- Al partir un parrafo, si la oracion donde se corta es breve o depende del contexto previo ("Su unidad es el grado", "La tercera ..."), se reescribe como oracion tematica autosuficiente (sujeto explicito, sin pronombre ni ordinal huerfano) en vez de dejarla como apertura.
