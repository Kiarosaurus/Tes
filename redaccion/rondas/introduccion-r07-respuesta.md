# Respuesta del redactor — introduccion — r07

Modo `corregir`, ronda unica, mas el encargo `redaccion/ENCARGO_2026-10-15.md` §introduccion. Por instruccion del
orquestador, el encabezado (l. 3-17) y la Formulacion del problema (l. 19-21) **no se tocan**, porque siguen DESFASADOS
(#126). Todo hallazgo que cae ahi queda ESCALADO, sin marca nueva en el texto: el estado DESFASADO ya esta registrado
en la fila de `introduccion.tex` de `redaccion/MAPA.md` y en #126.

Fuentes de cifras nuevas: -301.0 HU, IC90 [-477.0, -124.9], n = 13, Peters Ti, `run04_mejor` ->
`experiments/objetivo3/resultados_prueba_v1.md` (tabla E-A2, fila PRIMARIO) y `docs/00-tesis.md` (bloque Obj 3);
Delta = 196.3 HU -> `capitulo3.tex` §Analisis estadistico, DEC 2026-10-15 pto 21; tres desenlaces y su clasificacion
para v1 -> DEC 2026-10-15 pto 15; "10 mm / 12 mm" -> `capitulo3.tex` §Amenazas (copiado de `sec:v2`). Ninguna cifra se
recalculo.

## Encargo

| Punto | Decision | Detalle |
|---|---|---|
| Retirar `\GAPDEC` de la contingencia (#90, DEC15 pto 13) | APLICADO | Se retira la marca y tambien la clausula "depende del plazo" (l. 90 antigua) y "segun el plazo" (l. 56 antigua) |
| Resultado del Obj 3 (DEC15 pto 15) | APLICADO | Parrafo propio en §Objetivos: regla previa, desenlaces fijados despues, -301.0 HU, IC90 [-477.0, -124.9], Delta 196.3; no concluyente con diferencia a la baja; cordura superada que no cuenta a favor |
| Actualizar `\GAPDATO` "modelo final no elegido" | APLICADO | Se retira. Prosa: "modelo evaluado, el punto de control de la version 1 elegido en validacion". Lo pendiente queda en dos marcas: contraste de realismo y prueba de la version 2 (posterior y exploratoria, DEC 2026-10-14 (2)) |

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Delta medido (196.3 HU); tres desenlaces con "no equivalencia, que haria fallar el objetivo" (pregunta cerrada por DEC15 pto 15, MAPA); se dice que la regla es anterior y la lectura posterior; resultado con su condicion (titanio, 13 pacientes, eje del corredor) en dos parrafos nuevos; :56 y :80 pasan a hecho |
| guia-2 | guia | APLICADO | Igual que el encargo; "modelo final" pasa a "modelo evaluado"; la version 2 en una frase |
| guia-3 | guia | APLICADO | §Justificacion: ejecutado sobre el eje sin perturbar, razon de DEC15 pto 9, la comparacion no cubre las poses del muestreador, exploratorio con `\GAPDATO`. :13 y :41 son encabezado/objetivo de diseno: :13 queda ESCALADO (encabezado); el cruce con `capitulo2.tex`:106 se avisa al orquestador |
| guia-4 | guia | APLICADO | Objetivo general: "Disenar e implementar ... y evaluar la coherencia fisica y quirurgica de lo generado" |
| guia-5 | guia | APLICADO | Limitaciones de apariencia partidas en dos parrafos: (a) metrica sin estructura de raya, con el mismo `\GAPDATO` del cap. 3; (b) el protocolo exagera y el p95 sintetico queda bajo lo real; (c) asimetrias con remision a `sec:amenazas`, sin cifras de #186. El resultado se enuncia en *streak amplitude* (PAT-61) |
| guia-6 | guia | APLICADO | El segundo desplazamiento: medido en la reconstruccion de implantes reales; en la sintesis sobre pelvis sin metal se anadio despues de la prueba, con `\GAPDATO` |
| T01 | trazabilidad | APLICADO | Delta = 196.3 HU medido en validacion |
| T02 | trazabilidad | APLICADO | Ver guia-3; condicional de la ultima oracion reescrito con el desenlace |
| T03 | trazabilidad | APLICADO | Ver encargo |
| T04 | trazabilidad | APLICADO | Ver encargo; MAPA actualizado (fila #90 y fila de la seccion) |
| T05 | trazabilidad | APLICADO | Se conserva la mitad sostenida (unico con distribucion clinica publicada de grados, DEC 2026-10-08 pto 27) y se dice, con las fichas, que otros tornillos pelvicos tienen corredores planificados por atlas sobre cada TC \cite{goerres2017planning,han2019atlasplanning}. No se abre `\GAPDEC`: la restriccion del implante sigue sostenida por la otra mitad de la razon. **Para la autora:** DEC pto 27 dice "placas y otros tornillos no tienen ninguna de las dos"; #180 (ABIERTA) lo contradice en el corredor |
| T06 | trazabilidad | APLICADO | Tres desenlaces y resultado, sin interpretar el porque (#177) |
| T07 | trazabilidad | APLICADO | "cilindro parametrico liso, con cabeza (Seccion geometria)" |
| T08 | trazabilidad | APLICADO | Acotamiento para tornillos con remision a `sec:v2`; placas y protesis no acotadas |
| T09 | trazabilidad | ESCALADO | l. 5, encabezado DESFASADO (#126); fuera del encargo por instruccion del orquestador |
| T10 | trazabilidad | ESCALADO | Idem (l. 5) |
| T11 | trazabilidad | ESCALADO | Idem (l. 9); el reviewer ya lo situa dentro de #126 |
| S01 | estilo | ESCALADO | l. 7, encabezado (#126). Nota: la propuesta es correcta segun la ficha `liu2021ctpelvic1k` ("taken off in our supervised training phase") |
| S02 | estilo | ESCALADO | l. 9, encabezado (#126) |
| S03, S04, S05, S06, S07, S08, S09 | estilo | ESCALADO | l. 3-5, encabezado (#126). S05-S08 son PAT-14 sobre terminos fijos; aplicar al reescribir |
| S10 | estilo | ESCALADO | Las cifras 14/75/61 se repiten entre l. 7 (encabezado DESFASADO) y l. 56 (§Justificacion). Quitarlas de la justificacion dejaria la unica copia en un texto que se va a reescribir; se resuelve al reescribir el encabezado, dejando una sola copia |
| S11, S12, S13, S14 | estilo | ESCALADO | l. 9-15, encabezado (#126). S13 (PAT-46) toca tambien l. 15 |
| S15 | estilo | APLICADO | "control de cordura que alcanza cualquier brazo que genere artefacto; ... no cuenta a su favor" |
| S16 | estilo | APLICADO | "protocolo fisico"; sin "justamente" |
| S17 | estilo | APLICADO | Aperturas de l. 64 ("Metodologicamente, ...") y l. 68 ("El alcance se acota por ...") cambiadas; l. 72 queda sola con recuento |
| S18 | estilo | APLICADO | El parrafo cajon se parte en dos: variante de la segmentacion; etiqueta de S1 y envolvente, con oracion tematica propia |
| lint E-O1 l. 7 | lint | ESCALADO | Oracion del encabezado (#126). Es lo unico que hace FALLAR el lint de la seccion |

Hallazgos bajos aplicados: guia-7 (reconstruccion de implantes reales en el Obj 3), guia-8 (Delta fijado por la
variabilidad del sintetizador y sentido de las tres elecciones), guia-9 (= T08), T14 ("diferencia media pareada"),
T15 ("minima media"), T16 ("objetos metalicos"; razon "medida antes de los ultimos retiros de volumenes"), T17
(`\GAPDATO` de la sensibilidad sin los dos casos, mismo texto que el cap. 3), T18, S20, S21. Escalados por encabezado:
guia-10, guia-11, T12, T13, S19, lint E-P4. T19: aviso a la autora, sin efecto en el texto (`tesis/main.tex`:98 y
`EXPERIMENTOS.md` filas `a23`, `a24`, `a20_v2` atrasadas, PAT-138/PAT-158).

## Para la autora y el orquestador

- `capitulo2.tex`:104 y :106 conservan el `\GAPDATO` "modelo final no elegido" y la oracion "ejecutar el protocolo
  fisico sobre las poses del muestreador ... segun el plazo". La bisagra G-B10 con la introduccion queda rota hasta
  corregirlos igual.
- #180: ver T05.
- Implicancias: sin implicancias nuevas sobre la tesis; todo lo aplicado sale de DEC 2026-10-15 y de fichas existentes.

## Decisiones de redaccion

- Resultado de un objetivo en la introduccion: parrafo propio con, en este orden, la regla (y cuando se fijo), el
  margen con su fuente, la lectura de desenlaces (y que es posterior), el resultado con su condicion y lo pendiente con
  `\GAPDATO`. La direccion se enuncia en la metrica ("la *streak amplitude* del sintetizador es menor"), no en el
  mecanismo ("rayas mas debiles").
- "No equivalencia, que haria fallar el objetivo" es la forma de decir el desenlace contrario del TOST (DEC15 pto 15).
- En la introduccion, la pose de la evaluacion de apariencia se dice siempre "el tornillo en el eje del corredor sin
  perturbar", con la remision a `sec:ap-sintesis`, igual que el cap. 3.
