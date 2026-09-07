# Estado actual

> Lo actualiza Claude al cerrar cada sesion. Fuente de verdad de "por donde voy".

## Ultimo paso completado
P1: `refs.bib` generado desde la seccion References de `tesis/main.tex`. 27 entradas,
claves `apellidoANIOpalabraclave`. Las 27 quedaron marcadas `% VERIFICAR`.

Ademas: `scripts/renombrar_papers.sh` generado (NO ejecutado). Los 25 PDFs
emparejados, ninguno pendiente. Conflicto de claves resuelto: manda `refs.bib`,
se corrigio `_index.md`. Ficha de `wang2025adaptiveweighting` creada desde abstract.

## Siguiente paso
Correr `bash scripts/renombrar_papers.sh` (revisar antes). Luego completar los DOIs
de `refs.bib` desde los PDFs ya renombrados.

## Pendientes abiertos
- Las 27 entradas de `refs.bib` siguen marcadas `% VERIFICAR` (falta DOI en todas;
  numero o paginas en 10).
- Implicancia #1 ABIERTA: `wang2025adaptiveweighting` es nivel 1 y solo hay abstract.
  Al llegar el PDF, releer con `lector-papers` y regenerar la ficha completa.
- Implicancia #2 ABIERTA (GAP): el multi-ventana publicado es todo de remocion, no
  de sintesis. Verificar el reclamo de novedad antes de escribirlo.
- Implicancias #3 y #4 ABIERTAS, ambas de `zhang2026pediclescrew`: colision de
  encuadre con mi novedad, y una segunda escala de brecha cortical con umbral de
  2 mm que toca la definicion de BFC.
- `zhang2026pediclescrew`: ficha creada desde abstract. Nivel 1 PROPUESTO por Claude,
  falta que la autora lo confirme en `_index.md`.
- Las 24 filas restantes de `_index.md` no existen todavia: solo hay 7 de 27.
- `main.tex` no trae ningun DOI, asi que ninguna entrada lo tiene.
- Faltan tambien: volumen (deman2007catsim), paginas (jacob2026lgesynthnet,
  ramzan2026claim, wang2019cochlear), numero (liu2021ctpelvic1k, singhrao2024fiducial,
  smith2006iliosacral, vanbosse2011pelvicpositioning, xie2024implantsegmentation,
  yun2026simulationdriven).
- `tesis/main.tex` sigue con la bibliografia en texto plano dentro de `multicols`;
  migrar a `\bibliography{refs}` es decision de la autora (no se toco).

## Deudas asumidas
- Leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion:
  la metrica SAP depende de la definicion de grados de brecha cortical.
