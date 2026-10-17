# conclusiones — r00 (modo redactar) — respuesta del redactor

Encargo: `redaccion/ENCARGO_2026-10-16.md` pto 6 y "En todos los capitulos". Texto de plantilla eliminado;
se conserva `\customchapter{CONCLUSIONES}`. `trabajosFuturos.tex` no se toco.

Estructura (subsecciones con `\introsection`, como la introduccion; sin numerar porque el capitulo es `\customchapter`):
parrafo de sintesis (G-D2) -> *Respuesta a los objetivos y a la pregunta de investigacion* (G-D1, P-CO2: un parrafo
por objetivo, uno de controles del Obj 3 y uno de la pregunta) -> *Logros y limitaciones* (P-CO2, G-D3) ->
*Implicancias y aplicaciones* (plantilla; con la evaluacion de segmentacion posterior como fuera de alcance).

GAP: ninguno abierto ni cerrado. Sin `\REVVISUAL`. Lint `conclusiones --compilar`: PASA (0/0/0; 189 paginas).

## Fuente de cada cifra

| Cifra en conclusiones | Fuente en el documento | Fuente primaria |
|---|---|---|
| 6 combinaciones, 25 HU, 34 pacientes; 61.72 HU, IC95 55.12-68.99; todos >= 25 HU | cap. 4 `tab:res-compuerta`, l. 37 | `experiments/objetivo1/p1_compuerta.md`; `00-tesis.md` l. 47-50 |
| Saturacion del autoencoder de Guo et al. supera el criterio (sin cifra) | cap. 4 l. 45; introduccion l. 46 | #93 |
| Ida y vuelta 0.00 HU en hueso con arcoseno hiperbolico | cap. 4 l. 41, l. 237 | `p1_compuerta.md` |
| 3 600 poses / 72 pacientes; 2 450 / 49 | cap. 4 l. 49 | `e13_sap.md` |
| W1 0.206 y 0.230; escala 0.395 | cap. 4 `tab:res-sap`, l. 80 | `e13_sap.md`; `00-tesis.md` l. 68, 76 |
| 15 de 72 corredores estrechos; grado 0 3.3 % frente a 64.2 % de 57 | cap. 4 l. 86, l. 241-243 | `e13b_estratificado.md` |
| 13 pacientes; -301.0 HU; IC90 -477.0 a -124.9; Delta 196.3 | cap. 4 `tab:res-tost`, l. 94 | `resultados_prueba_v1.md`; `00-tesis.md` l. 161-165 |
| Estado final: intervalo entero fuera del margen (sin cifra) | cap. 4 l. 130, l. 249 | idem |
| Wilcoxon p = 0.000122, 13 pacientes | cap. 4 l. 132 | idem |
| Razon 1.92 / 6.71 / 4.08 | cap. 4 `tab:res-anillos`, l. 168, l. 251 | `outputs/a29/a29_perfil.md`; DEC 2026-10-15 (3) pto 4 |
| CV 0.076 frente a 0.241 | cap. 4 l. 172, l. 253 | #185; DEC 2026-10-15 (3) pto 2 |
| v2: -258.9 y -264.3 HU | cap. 4 `tab:res-tost`, l. 225 | #190 |
| Piso / amplitud 0.69 | cap. 4 l. 140, l. 259 | #188 |
| Parametrico -98.9 frente a -301.0 HU | cap. 4 `tab:res-tost`, l. 170 | #187 |
| Hueco medial ocupado en 14 de 71 | cap. 4 l. 263 | `registro_2026-10-16.md` §2; DEC 2026-10-16 (2) |
| Fractura en 20 de 30 | cap. 4 l. 243; introduccion l. 92 | #125, #132 |
| Segundo corredor: eje en 69 de 72 | cap. 4 l. 267; introduccion l. 78 | DEC 2026-10-16 (3) pto 2 |
| 14 de 75 volumenes con metal anotados (CTPelvic1K) | introduccion l. 60, con `\cite{liu2021ctpelvic1k}` | ficha `liu2021ctpelvic1k` |

## Fuente de cada afirmacion de lectura (mismas palabras que el cap. 4)

| Afirmacion | Fuente |
|---|---|
| Obj 1 responde negativo con el criterio fijado de antemano; hallazgo propio y razon del rediseno, que no modifico la regla | cap. 4 l. 235, 237; introduccion l. 46 |
| El veredicto descarto la difusion latente, no la codificacion multiventana; no establece que ningun latente pueda | cap. 4 l. 237 |
| Obj 2 sin regla de decision; escala elegida despues; los IC no ordenan las series; caso negativo anatomico | cap. 4 l. 80-82, 241-243 |
| Ningun parametro del muestreador tomado de la referencia clinica; distribucion fijada en la preinscripcion antes de calcular distancias | introduccion l. 72 |
| Obj 3 "se cumple como objetivo de diseno y evaluacion"; "la hipotesis de equivalencia ... no se sostiene"; "tampoco se lee como no equivalencia demostrada"; lectura en dos niveles fijada despues | cap. 4 l. 249; introduccion l. 54; cap. 3 `sec:ap-analisis`; DEC 2026-10-15 (3) pto 1 |
| Control de cordura que no cuenta a favor | cap. 4 l. 132; introduccion l. 56 |
| Obj 4 "se cumple como objetivo de definicion"; no validada como medida clinica; metricas de Peters con su inversion, protocolo no es verdad fisica | cap. 4 l. 245 |
| Realismo visual no reclamado; decision de la autora con su asesor; reclamo acotado (texto literal del cap. 4 l. 259) | DEC 2026-10-16 pto 1; #193 (DECIDIDA) |
| Pose del muestreador como propiedad del diseno, no resultado evaluado | DEC 2026-10-16 (3) pto 1; #197 (DECIDIDA); cap. 4 l. 261 |
| Delta mide variabilidad propia y lo fija la variabilidad entre semillas | introduccion l. 52; cap. 3 `sec:ap-analisis`; #195 (DECIDIDA) |
| Envolvente y cifras del Obj 2 se mantienen | DEC 2026-10-16 (2); cap. 4 l. 263 |
| Voxel mas craneal de S1 no medido; afecta al control de nivel | DEC 2026-10-16 (4); cap. 4 l. 265 |
| Segundo corredor solo como geometria (sin poses ni grados) | DEC 2026-10-16 (3) pto 2. #198 (ABIERTA) solo toca `docs/00-tesis.md`; no se afirma nada que dependa de ella |
| Evaluacion de segmentacion posterior fuera de alcance; no se presenta como resultado | `00-tesis.md` Fuera de alcance pto 1; introduccion l. 82 |
| La amplitud media no distingue un modelo aprendido de uno analitico | cap. 4 l. 251 |
| Muestreador y SAP evaluados sin depender del sintetizador | `CLAUDE.md` raiz (dos componentes que se disenan y evaluan por separado); cap. 4 `sec:res-obj2` no usa el sintetizador |

## Decisiones de redaccion

- **Respuesta por objetivo sin endurecer ni suavizar:** cada objetivo usa la formula de cumplimiento que ya fija el cap. 4
  ("responde con el criterio fijado de antemano" para el Obj 1; "sin regla que la convierta en exito o fallo" para el
  Obj 2; "se cumple como objetivo de diseno y evaluacion" + "la hipotesis de equivalencia no se sostiene" + "tampoco
  se lee como no equivalencia demostrada" para el Obj 3; "se cumple como objetivo de definicion" para el Obj 4). El
  Obj 2 no recibe "se cumple", porque ninguna fuente del documento se lo da.
- **Hipotesis:** el documento de entrega solo nombra la "hipotesis de equivalencia con el protocolo fisico"; la
  hipotesis larga de `tesis/main.tex` (mas coherente que bases generativas sin restriccion) no aparece en la
  introduccion y no se introduce aqui (G-D2, sin informacion nueva).
- **Aperturas de parrafo variadas** en la respuesta por objetivo (compuerta / colocacion / sintetizador / SAP) para
  evitar E-R1 y PAT-119.
- **Aplicaciones:** la motivacion (aumento de datos) se presenta como no evaluada y fuera de alcance; el unico uso que
  se afirma es metodologico y acotado a lo examinado (PAT-174).
