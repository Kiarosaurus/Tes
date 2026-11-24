# F6 lote 5 - redactor (modo corregir, capitulo4.tex)

## (a) Que se aplico
Archivo editado: overleaf/secciones/capitulo4.tex (CRLF conservado). Unico cambio: en la subseccion
`sec:res-anadidos`, tras el parrafo "El perfil por anillos describe..." (que lee tab:res-anillos) y antes del
parrafo del artefacto parametrico, se agrego un parrafo de 5 oraciones y la tabla `tab:res-peters-real`
(6 columnas: anillo, protocolo fisico Ti, tornillo real, sintetizador, razon Ti/real, razon sintetizador/real;
anillos 0-2 a 8-10 mm; formato p{...}, \small, \hline, \tabcolsep 4pt, nota en \multicolumn{6}{p{0.9\linewidth}}).
Nota de tabla: n por columna (15 = 13 prueba + 2 validacion; 18 entrenamiento y validacion; 2 validacion),
estadistico (5 %/5 %, con metal menos sin metal en los mismos pixeles, anillos en el plano axial alrededor de M),
"descriptivo, sin regla de decision" y la ruta del script experiments/objetivo3/d3_peters_vs_real.py.
Parrafo (impersonal, sin sujeto personal, sin afirmar equivalencia ni superioridad): (1) compara los tres con el
estadistico del diagnostico de sec:v2; (2) Ti excede a lo real de 2.1 a 3.1 veces entre 0 y 8 mm; (3) el sintetizador
queda bajo lo real, su exceso se atenua desde unos 4 mm, y por tanto lo real queda entre el sintetizador y el protocolo
fisico; (4) el contraste primario mide la distancia al protocolo fisico, y el -301.0 HU no se lee como distancia a lo
real; (5) pacientes distintos entre columnas y referencia real = otro corte del paciente (en las otras dos, el mismo
corte sin metal); (6) oracion de comparabilidad (ver c). No se toco tab:res-anillos, otras tablas, ecuaciones, \cite,
\label existentes ni marcas \GAP*/\REVVISUAL. No se uso la sigla "E-A2" en el texto (no aparece en capitulo3 ni 4).
No se mencionaron en el parrafo las razones 6.55/-0.14/-0.23 (quedan solo en la tabla).
Lint: `python3 scripts/lint_redaccion.py capitulo4 --compilar` -> PASA (alta 0, media 0, baja 0; GAP 0/0/0).
Dos oraciones de >40 palabras de la primera version se partieron/acortaron. PDF compila (206 pag.); sin overfull;
la tabla (Tabla 4.5, p. 162 del PDF) cabe en el ancho. Nota: la numeracion automatica de tablas posteriores
(p. ej. tab:res-integridad) se corre en uno; todas las referencias son por \ref.

## (b) Palabras (`texcount -brief -inc -q`)
Antes: 4672+41+175 (13/6/60/0). Despues: 4854+41+207 (13/7/61/0). Delta texto: +182 palabras (parrafo + tabla + nota).

## (c) Comparabilidad con tab:res-anillos y lo visto en capitulo3
- capitulo3 l.438 (sec:ap-sintesis, "Las regiones de medicion se derivan de la pose"): "En planos perpendiculares al
  eje del implante se toman anillos completos de 360 grados... idéntica para los brazos que se comparan"; l.446 y l.470
  repiten "anillos en planos perpendiculares al eje". l.536 define el perfil por anillos (anillos de 2 mm de 0 a 12 mm en
  protocolo fisico Ti, sintetizador y parametrico) como el perfil de la streak amplitude. Por tanto las columnas Ti,
  sintetizador (y parametrico) de tab:res-anillos SI estan sustentadas como medidas en planos perpendiculares al eje.
- Lo que capitulo3 NO dice: el plano del "exceso real" (l.294-298 definen el exceso por anillo de 2 mm sin nombrar el
  plano; l.272 dice "en el plano de cada corte" pero para el perfil radial de HU, otro estadistico). El plano axial del
  exceso real y de las tres series de la tabla nueva sale de la docstring de experiments/objetivo3/d1_alcance_rayas.py
  ("en el plano axial", "distancia euclidea en el plano") y de d3_peters_vs_real.py (distancia en el plano a M), y de
  docs/01-decisiones.md 2026-11-24 (23).
- Resolucion: UNA oracion que afirma solo lo sustentado: "En la Tabla~\ref{tab:res-anillos}, el protocolo fisico y el
  sintetizador se miden en planos perpendiculares al eje del tornillo (Seccion~\ref{sec:ap-sintesis}), y aqui en el
  plano axial, por lo que sus valores no son intercambiables." No se afirma el plano de la columna "Exceso real" de
  tab:res-anillos (capitulo3 no lo sustenta); si la autora quiere que se diga, capitulo3 deberia explicitarlo.
- Observacion de la lectura: las cifras de ambas tablas difieren (p. ej. Ti 0-2 mm: 3864 en tab:res-anillos, mediana de
  13 pacientes y 10 validos, frente a 5004 aqui, 15 pacientes y exceso); no se comenta en el texto para no agregar
  cifras ni comparaciones no pedidas.

## (d) Cifra de la tabla -> d3_peters_vs_real_resultado.md (columnas "Peters Ti", "real tornillo", "modelo", "Ti/real", "modelo/real")
| Anillo | Ti | real | sintetizador | Ti/real | sint./real |
|---|---|---|---|---|---|
| 0-2 (fila 9) | 5004 | 1930 | 1697 | 2.59 | 0.88 |
| 2-4 (fila 10) | 2558 | 1199 | 488 | 2.13 | 0.41 |
| 4-6 (fila 11) | 2052 | 765 | 97 | 2.68 | 0.13 |
| 6-8 (fila 12) | 1487 | 473 | -65 | 3.14 | -0.14 |
| 8-10 (fila 13) | 1138 | 174 | -40 | 6.55 | -0.23 |
Coherencia con capitulo3 l.298 (real 1930, 1199, 765, 473, 174; modelo 1697, 488, 97, -65, -40) y con tab:res-anillos
(columna Exceso real). "2.1 a 3.1 veces entre 0 y 8 mm" = rango de Ti/real (2.13 a 3.14), igual que decisiones (23) punto 1.
n y estadistico de la nota: encabezado y docstring del mismo archivo (Peters 15 = 13 peters_final + 2 peters_val,
condicion A; real 18; modelo 0101/0102).
