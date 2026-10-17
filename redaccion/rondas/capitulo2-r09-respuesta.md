# Respuesta del redactor — capitulo2 — r09

Modo: corregir (ronda unica de todos los capitulos, `redaccion/ENCARGO_2026-10-16.md`).
Archivos editados: `overleaf/secciones/capitulo2.tex`; `overleaf/secciones/anexos.tex`:30 (solo la fila "Este
trabajo" de la Tabla A.1, que resume el cap. 2; mismo precedente que capitulo2-r07 y r08); `redaccion/MAPA.md`.
Decisiones que mandan: DEC 2026-10-16 ptos 1-3 (#193 (a)); DEC 2026-10-15 (3) pto 1; DEC 2026-09-17 fila #71.
Reporte del asesor aplicado: GAP #1 (clase A) y #2 (clase D); R1-R9 con los ajustes que se indican.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 | trazabilidad | APLICADO | l. 98: `\GAPDATO` de la ablacion de Li et al. retirado (DEC 2026-09-17 #71, sin cifras). La oracion atribuye solo la frase de Sec. I, p. 1866 (ficha `li2024.md`:81) y la existencia de la ablacion (:137). Partida en dos por E-O1 (lint). "Los dos resultados" -> "Las dos fuentes" (asesor GAP #1) |
| T02 | trazabilidad | APLICADO | l. 112: `\REVVISUAL` y `\GAPDATO` retirados: "El contraste de realismo ... quedo disenado (`sec:ap-realismo`) y no se ejecuto, por la decision que se expone en `sec:amenazas`" (DEC 2026-10-16 pto 2; formula de BITACORA §2 2026-10-16). Tabla A.1: "contraste de realismo disenado y no ejecutado" |
| T03 | trazabilidad | APLICADO | l. 114: se elimina la oracion que presentaba H5 como comparacion existente (opcion de borrar, compatible con ES-02). No se nombra E-A1 como "la unica comparacion con lo real": el p95 en validacion (#191) tambien compara con lo real, y "unica" seria falso |
| T04 | trazabilidad | APLICADO | l. 100: la comparacion del Obj 3 "contrasta ese supuesto solo en la amplitud local del artefacto dentro de la banda, y su desenlace no permite afirmar la equivalencia" (DEC 2026-10-16 pto 1; DEC 2026-10-15 (3) pto 1). l. 124: "para los efectos de adquisicion" -> "alrededor de la mascara del implante" (la l. 120 ya dice que la banda extiende la generacion fuera de la mascara) |
| T05 | trazabilidad | APLICADO | 7 `\REVVISUAL` retirados del capitulo y 2 de `anexos.tex`:30. l. 102 y l. 104 sin cambio de texto (respaldo DEC 2026-09-17 #57; `capitulo3.tex` `sec:v2`). En el cierre (l. 126) se agrega la limitacion como hecho mas consecuencia: no se reclama el realismo visual, y el reclamo del Obj 3 se acota a la sintesis local en la banda frente al protocolo fisico (DEC 2026-10-16 pto 1) |
| guia-1 | guia | APLICADO | Cubierto por T02-T05: fila propia y cierre alineados con `introduccion.tex`:98; "pendiente" -> "disenado y no ejecutado"; banda descrita sin capacidad demostrada; desenlace "no concluyente" intacto |
| ES-01 | estilo | APLICADO (con ajuste) | Se conserva "Se asume que ..." (PAT-85 ERRADICADO: el supuesto debe decir "se asume"); lo que el hallazgo pedia, no afirmar realismo, se cumple acotando la oracion siguiente (T04) y declarando la no reclamacion en el cierre. La propuesta literal ("los resultados no permiten afirmar realismo visual") se descarta: el realismo no se evaluo, no es un resultado |
| ES-02 | estilo | APLICADO | El no ejecutado se dice una vez (l. 112); la oracion de l. 114 se elimina |
| ES-03 | estilo | APLICADO (con la formula de T04) | La propuesta "cuyo ancho limita la generacion al entorno local" se sustituye por la descripcion neutra que pide la trazabilidad (manda sobre estilo) |
| ES-04 | estilo | APLICADO | Re-apertura valida por DEC 2026-10-16: se eliminan las dos oraciones que repetian supuesto y convencion (ya en l. 100 y l. 104; la Tabla A.1 los conserva). El cierre abre con el contraste de evaluacion y suma la limitacion de T05 |
| ES-05 | estilo | APLICADO | Parrafo de l. 118 dividido; el segundo abre con "El desenlace de esa comparacion responde a una pregunta del Objetivo~3, ..." y mantiene la formula de r08 del desenlace |

Bajos aplicados: ES-06 (se elimina "La brecha es la misma tension que plantea la introduccion"), ES-07 ("Como
declara la justificacion de la introduccion," eliminado, PAT-5), ES-08 (l. 10: dos de las tres aperturas "La
Seccion" pasan a abrir por su funcion).

Correcciones colaterales (lint): la oracion de Li et al. (46 palabras) y la del aporte (41) partidas o acortadas
(E-O1); la primera oracion del parrafo de la brecha (que quedo abriendo parrafo tras ES-06) causaba un Overfull hbox
y se reordeno: "De los tres enfoques revisados, la simulacion fisica, ..., ninguno produce a la vez ...".

Lint final: `python scripts/lint_redaccion.py capitulo2 --compilar` -> TOTAL alta=0 media=0 baja=0 | GAP lit=1
dato=0 dec=0 | LINT: PASA | 165 paginas.

Dependencias con otros capitulos: el cap. 2 cita `sec:ap-realismo` (diseno del contraste) y `sec:amenazas` (razon de
no ejecutarlo y limitacion de realismo); capitulo3-r27 debe conservar ambas etiquetas y mantener en §Amenazas la
limitacion de realismo (ya presente en `capitulo3.tex`, parrafo "En la apariencia, la limitacion principal ...").

## Decisiones de redaccion

- Supuesto del dominio de imagen tras DEC 2026-10-16: se mantiene como supuesto ("se asume"), y el contraste que lo
  toca se acota a "la amplitud local del artefacto dentro de la banda"; nunca "contrasta ese supuesto" sin acotar.
- No reclamar realismo visual: una sola vez por capitulo, como hecho mas consecuencia ("no reclama el realismo
  visual ..., por lo que el reclamo del Objetivo~3 se acota a la sintesis local del artefacto en la banda, evaluada
  frente al protocolo fisico"), con remision a `sec:amenazas`; no "queda como limitacion" (PAT-5).
- La banda en enumeraciones de piezas o del aporte se describe por su posicion ("alrededor de la mascara del
  implante" / "que extiende la generacion fuera de la mascara"), no por lo que lograria ("para los efectos de
  adquisicion").
- En tablas que resumen el estado: "contraste de realismo disenado y no ejecutado".
