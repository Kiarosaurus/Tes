# trabajosFuturos — r00 (redactar) — respuesta del redactor

Encargo: `redaccion/ENCARGO_2026-10-16.md` pto 6. Modo redactar (plantilla). Sin reportes de revision en esta etapa,
por lo que no hay tabla de hallazgos; se deja la fuente de cada punto y de cada cifra.

## Estructura

Encabezado conservado (`\chapter*`, `\addcontentsline`, `\markboth`); texto de plantilla y comentario de M6 retirados.
Parrafo de apertura + cuatro bloques con `\introsection` en el orden de los objetivos (G-T5), cerrando con la
aplicacion que motivo el trabajo (G-D4): Representacion multiventana; Colocacion y admisibilidad quirurgica;
Apariencia del artefacto; Evaluacion de segmentacion posterior. Sin `\REVVISUAL`. 0 GAP abiertos.

## Fuente de cada punto

| Punto | Lugar | Fuente |
|---|---|---|
| Otros autoencoders en la compuerta; Guo et al. no corrido; codificacion no descartada | Representacion | cap. 4 `sec:res-obj1` y discusion "Compuerta de representacion"; conclusiones pfo. 3 y "Implicancias" ("puede medirse antes de entrenar") |
| Segundo corredor bajo S1: eje en 69 de 72; poses y grados no preinscritos ni ejecutados; razones | Colocacion pfo. 1 | DEC 2026-10-16 (3) pto 2; DEC 2026-10-16 (5) (#198); cap. 4 `sec:discusion` (Limitaciones, ult. pfo.); cap. 3 `sec:poses` l. ~196 (nivel variable) |
| Ablaciones del muestreador | Colocacion pfo. 1 | `introduccion.tex` Fuera de alcance (l. ~83); cap. 3 `sec:vision` l. ~36 |
| Envolvente y hueco medial de S1 (14 de 71); canal, foramenes y efecto sobre la brecha no medidos; cifras sin corregir | Colocacion pfo. 2 | DEC 2026-10-16 (2) (#196); cap. 4 Limitaciones; conclusiones "Logros y limitaciones" |
| Causa de los 15 corredores estrechos; fractura 20 de 30 como confusion | Colocacion pfo. 2 | cap. 4 discusion "Muestreador y admisibilidad"; conclusiones |
| Techo de S1: voxel mas craneal no medido; afecta al control de nivel | Colocacion pfo. 3 | DEC 2026-10-16 (4) (#138); cap. 4 Limitaciones |
| Revision en cortes solo en 56 de CLINIC-metal; receptores por revision 3D y cribado por HU | Colocacion pfo. 3 | DEC 2026-10-16 (3) pto 4; cap. 4 Limitaciones, ult. pfo. |
| Contraste de realismo (H5), comparacion visual a ciegas (D3), control de calidad visual (E-A4): fijados y no ejecutados; referencia no formada; control no ciego con el modelo evaluado | Apariencia pfo. 1 | DEC 2026-10-16 pto 2; DEC 2026-10-16 (3) pto 3; cap. 3 `sec:ap-realismo` (l. ~467-471), `sec:v2` (l. ~305), `sec:ap-contrastes` (l. ~377), `sec:amenazas` (l. ~549); cap. 4 Limitaciones |
| Version nueva: banda mayor, formulacion residual, refinamiento sobre simulacion fisica; requiere pares simulados, tiempo no estimado; ninguna disenada | Apariencia pfo. 2 | implicancia #193 opcion (c) (DECIDIDA con la opcion (a)); DEC 2026-10-16 pto 1 ("no hay version 3") |
| Lo que una version nueva tendria que corregir (perfil, piso, CV, v2) | Apariencia pfo. 2 | cap. 4 `sec:res-anadidos`, `tab:res-anillos`, `sec:res-v2`; conclusiones |
| La banda no es la causa del deficit medido | Apariencia pfo. 3 | cap. 3 `sec:v2` ("el deficit medido esta dentro de la banda y no en su ancho", piezas de 500 a 4000 mm^3, validacion); cap. 4 `sec:res-anadidos` (12-16 mm del orden del piso de ruido) |
| Varios volumenes de un paciente en una particion (oracion de M6 conservada literal) | Apariencia pfo. 4 | implicancia #171 pto 3; cap. 3 `sec:sintetizador` l. ~230 y `sec:datos` l. ~56 (secundarios retirados del entrenamiento) |
| Posterior y exploratoria si se evalua en la misma particion | Apariencia pfo. 4 | cap. 4 discusion "Sintetizador" ("posterior, exploratoria y reutiliza la particion de prueba") |
| D9: 5 poses, solo sintetizador, modelo evaluado, cinco semillas, resumen por grado, expectativa sin umbral; costo del protocolo fisico | Apariencia pfo. 5 | DEC 2026-10-16 (3) pto 1 (#197); cap. 3 `sec:ap-sintesis` l. ~359 |
| Segmentacion posterior fuera de alcance; 14 de 75, 178 de 1184; sin prometer resultado | Segmentacion | `introduccion.tex` Fuera de alcance (l. ~82); cap. 3 `sec:vision` l. ~36; conclusiones "Implicancias y aplicaciones" |

## Cifras (todas copiadas, ninguna nueva)

25 HU, 0.00 HU (cap. 4 `sec:res-obj1`); 69 de 72 (cap. 4, DEC (3)); 14 de 71, 15 corredores, 7.0 mm, 20 de 30
(cap. 4, conclusiones); 56 pacientes (cap. 4); 1.92 / 6.71 / 4.08 (`tab:res-anillos`); 0.69 / 0.12 y 0.076 / 0.241
(cap. 4 `sec:res-anadidos`); 12 mm (cap. 3 `sec:v2`); 5 poses, cinco semillas, uno de cada dos cortes (cap. 3
`sec:ap-sintesis`); 75, 14, 178, 1 184 (cap. 3 `sec:vision`, `\cite{liu2021ctpelvic1k}`).

## Para la autora (no es GAP)

- **Formulacion residual** aparece solo como nombre en #193 opcion (c); no se define en el texto porque el
  repositorio no da su contenido. Un revisor puede senalarlo por G-T2; si la autora quiere una glosa de una linea,
  hace falta que la fije.
- La "banda mayor" de #193 (c) se redacta junto al hecho medido de que el deficit de validacion quedo dentro de la
  banda (cap. 3 `sec:v2`), sin afirmar que ampliarla ayudaria.
- El encabezado conserva `TRABAJOSFUTUROS` (sin espacio) en `\addcontentsline` y `\markboth`, como pidio el encargo.

## Decisiones de redaccion

- Trabajo futuro desde un analisis fijado y no ejecutado: procedimiento en condicional ("compararia", "generaria",
  "juzgaria") y el estado en pasado ("no se ejecuto"); nunca presente que afirme evidencia (sigue la fila de
  capitulo3-r27).
- Opciones descartadas de una implicancia DECIDIDA (p. ej., #193 (c)) entran como trabajo futuro con "entre las
  opciones de esa decision figuraba ...", diciendo que no se disenaron y sin atribuirles un efecto.
- La aplicacion de segmentacion posterior se cierra como pregunta abierta "cuyo resultado no anticipa"; el
  sintetizador, con la formula de conclusiones ("queda sin respaldo ... porque el realismo visual ... no se reclama").
