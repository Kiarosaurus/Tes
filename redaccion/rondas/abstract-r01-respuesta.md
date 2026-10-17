# abstract-r01 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/abstract.tex`. Tambien se toco `overleaf/secciones/resumen.tex`
(restriccion P-R4 del encargo: el abstract sigue siendo traduccion fiel del resumen).
Reportes leidos: `abstract-r01-lint.md` (PASA, 0 hallazgos), `-guia.md` (0), `-estilo.md` (ES-01..ES-04), `-trazabilidad.md` (0).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| ES-01 (media, E-M4, E-M8) | estilo | APLICADO | "rates each pose by corridor viability and by cortical breach grade, which records how far the screw protrudes from the bone". La relativa ata la protrusion al grado de brecha y no a la calificacion entera. Cambio de redaccion en ingles: el contenido coincide con "segun cuanto sobresale del hueso"; resumen sin tocar |
| ES-02 (media, E-R2, E-M4, E-M8; PAT-205) | estilo | APLICADO, tambien en el resumen | Abstract: "passed its identity, monotonicity and resolution checks; the grade distribution over 3\,600 poses in 72 patients lay at Wasserstein-1 distances of 0.206 and 0.230 grades from the clinical series with and without navigation". Fuente de los controles: `conclusiones.tex`:22 y `capitulo4.tex`:246 ("controles de identidad, monotonia y resolucion"). Resumen, misma oracion (3.2): "La admisibilidad quirurgica paso los controles de identidad, monotonia y resolucion; la distribucion de grados en 3\,600 poses de 72 pacientes disto 0.206 y 0.230 grados en Wasserstein-1 de las series clinicas con y sin navegacion". Para no superar 40 palabras (E-O1) se quito el inciso "en distancia de Wasserstein-1" y la forma "una serie ... y otra sin ella" paso a "las series clinicas con y sin navegacion"; el orden paralelo (0.206 con navegacion, 0.230 sin ella) conserva la asignacion. Ninguna cifra cambio |
| ES-04 (media, E-M8, E-P3) | estilo | APLICADO, tambien en el resumen | Abstract: "crosses the lower equivalence bound of $-196.3$ Hounsfield units; the outcome is inconclusive, and the synthesizer has a lower *streak amplitude* than the protocol". Resumen (3.5): "cruza el limite inferior de equivalencia de $-196.3$ unidades Hounsfield". Fuente: margen $\Delta = 196.3$ HU en `capitulo4.tex`:94 y `conclusiones.tex`:18; el limite inferior es $-\Delta$ (`capitulo4.tex`:130, "por debajo de $-\Delta$"). No se agregaron unidades al intervalo, como proponia el revisor, para no alargar la oracion del resumen; la oracion previa ya fija las unidades |

Baja:

- ES-03 (E-M8): APLICADO. "and the lowest mean absolute error was 61.72 Hounsfield units". Cambio de redaccion en ingles; el resumen ("la mejor dio 61.72") dice lo mismo y no se toco.

## Cambios en resumen.tex

Dos oraciones, sin cambiar el recuento 3/4/6/3 ni ninguna cifra:
- 3.2: nombra los controles de identidad, monotonia y resolucion, y reformula la distancia a las dos series (ver ES-02).
- 3.5: "limite inferior del margen de equivalencia de 196.3" pasa a "limite inferior de equivalencia de $-196.3$ unidades Hounsfield".

## Lint

- `python scripts/lint_redaccion.py abstract --compilar`: PASA, alta=0, media=0, baja=0. Compila (194 paginas).
- `python scripts/lint_redaccion.py resumen`: PASA, alta=0, media=0, baja=2 (E-P1, cifras sin `\ref`; inevitables por P-R2, igual que en resumen-r01).

## GAP

Abiertos: ninguno. Cerrados: ninguno. `redaccion/MAPA.md` sin cambios.

## Decisiones de redaccion

- Al nombrar los controles de la admisibilidad quirurgica en resumen y abstract: "los controles de identidad, monotonia y resolucion" / "its identity, monotonicity and resolution checks".
- El limite del margen de equivalencia se da con signo cuando se habla del limite inferior: "limite inferior de equivalencia de $-196.3$ unidades Hounsfield" / "lower equivalence bound of $-196.3$ Hounsfield units".
- Distancias a las dos series clinicas en una sola construccion paralela: "disto 0.206 y 0.230 grados en Wasserstein-1 de las series clinicas con y sin navegacion" / "lay at Wasserstein-1 distances of 0.206 and 0.230 grades from the clinical series with and without navigation".
