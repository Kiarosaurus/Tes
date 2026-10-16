# Respuesta del redactor — capitulo2 — r08 (ronda unica, encargo 2026-10-15b)

Archivos editados: `overleaf/secciones/capitulo2.tex`, `overleaf/secciones/anexos.tex` (Tabla A.1: fila nueva de Lyu
et al. y fila "Este trabajo"). Lint final: `python scripts/lint_redaccion.py capitulo2 --compilar` PASA (0/0/0),
GAP lit=1, dato=2, dec=0; PDF de 157 paginas, sin referencias indefinidas ni flotantes demasiado grandes.

Encargo: E1 (`\REVVISUAL`) aplicado; E2 aplicado (las dos `\GAPDEC` cerradas con DEC 2026-10-15 (3) ptos 8 y 9);
E3 sin `\GAPLIT` nuevos: ninguna afirmacion nueva necesita una fuente que el repositorio no tenga (el TOST y la prueba
de Pitman y Morgan no se tratan en este capitulo; la prueba visual con radiologos ya esta citada desde Chen et al.).

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | `\GAPDEC` #179 retirado. Parrafo nuevo en §Insercion y simulacion con U-DuDoNet y PND-Net desde sus fichas (componentes extraidos de otras imagenes con metal, sin geometria ni pose; imagen sintetizada sin evaluacion reportada; objecion de PND-Net a sumar el componente de imagen). §Brecha partida (PAT-58): parrafo de la brecha con la formula del pto 9 y parrafo de la comparacion. En l. de piezas publicadas, U-DuDoNet y PND-Net con `\cite`. La oracion "Ninguno de los tres enfoques..." se conserva igual que `introduccion` (G-B10); la acotacion se agrega despues. **Aviso:** `introduccion` §Justificacion debe recibir la misma acotacion en su r08 |
| guia-2 | guia | APLICADO | `\cite{yang2022computeraided}` en lugar del `\GAPDEC`; descripcion cotejada con la ficha (ver ES-01) |
| guia-3 | guia | APLICADO | `\REVVISUAL` en: supuesto del dominio de imagen (§Representacion y cierre del capitulo, y celda de la Tabla A.1, los tres por igual); contraste de realismo pendiente (con su `\GAPDATO` dentro) en la presentacion de la tabla y en la celda; oracion de la comparacion con observaciones reales |
| guia-4 | guia | APLICADO | §Representacion ya no usa el condicional: dice que la comparacion del Objetivo 3 contrasta el supuesto y remite al desenlace (§Brecha) y a Amenazas, todo dentro del `\REVVISUAL`, sin afirmar que lo contradice ni que lo sostiene. El desenlace con direccion y lectura posterior va una vez en §Brecha y en la celda |
| ES-01 | estilo | APLICADO | Oracion tematica: "con un atlas ... o con una busqueda sobre la pelvis del paciente". Goerres "registran sobre la TC del paciente un atlas de 12 pelvis femeninas"; Yang "no usan atlas: en cada una de 10 pelvis intactas eligen ... el canal en arco cuya linea central mas se aleja de la superficie osea" (ficha: "ten patients with an intact pelvis", 2.1; canal de curvatura constante, 2.2; puntaje por distancia de la linea central, solo se maximiza) |
| ES-02 | estilo | APLICADO | §Carencias: "entrega un plan por corredor y no una distribucion de poses" |
| ES-03 | estilo | APLICADO | Fusionado con T03 (ver abajo) |
| ES-04 | estilo | APLICADO | Con T05 y guia-4: §Representacion da la funcion del contraste sin desenlace; el desenlace queda en §Brecha y en la celda. La fila propia (presentacion de la tabla) ya no lo repite |
| ES-05 | estilo | APLICADO | Parrafo de densidad (5 oraciones) y parrafo de metricas de apariencia (3), con las aperturas propuestas |
| ES-06 | estilo | APLICADO | §Representacion partida tras la or. 5; segundo parrafo abierto por "Ningun trabajo revisado sintetiza ..." |
| ES-07 | estilo | APLICADO | Presentacion de la tabla partida; or. 3 = "La columna del enfoque añade, en la ultima fila, ..." |
| ES-08 | estilo | APLICADO | Eliminada l. 86 or. 2; l. 82 or. 3 acortada a "proviene de la MAR". El contraste queda en l. 88 y en la sintesis |
| T01 | trazabilidad | APLICADO | Igual que guia-2 |
| T02 | trazabilidad | APLICADO | Igual que guia-1. PAT-168: revisadas las menciones que repetian el hueco; en §Representacion se agrega que la sintesis aprendida de la MAR no pareada usa tambien el sinograma y no evalua la imagen sintetizada (el negativo "solo en el dominio de imagen y evalua su coherencia fisica" sigue cierto); "tres elementos que las fuentes revisadas no reunen" (§aporte) sigue cierto por la conjuncion. Sin cifras de PSNR |
| T03 | trazabilidad | APLICADO | `\REVVISUAL{En componentes de 500 a 4000 mm^3, del tamaño de un tornillo, el exceso mediano del artefacto real, medido por anillos en pacientes de entrenamiento y validacion, no se separa del de un control nulo pasados 10 mm (Seccion v2).}` Condicion de `capitulo3.tex` §v2 (18 pacientes de entrenamiento y validacion, 500-4000 mm^3, anillo mas lejano separado del control nulo = 8-10 mm). Ya no afirma que la banda "alcanza" |
| T04 | trazabilidad | APLICADO | Igual que guia-3, mas el inciso "la banda $B_\delta$ para los efectos de adquisicion" del aporte y la oracion de truncamiento de §Representacion (E1: "limitaciones de realismo") |
| T05 | trazabilidad | APLICADO | §Brecha: "el desenlace fue no concluyente: los datos no permiten afirmar la equivalencia, y la *streak amplitude* del sintetizador queda por debajo de la del protocolo fisico (capitulo de resultados). Esa lectura de los desenlaces se fijo despues de ver el resultado (Seccion ap-analisis)" (DEC15-3 pto 1; DEC15 pto 15). Celda: "no concluyente, con la *streak amplitude* del sintetizador por debajo de la del protocolo fisico" |

Bajas aplicadas: guia-5 (fila de Lyu et al. en la Tabla A.1, sin cifras, con respaldo en el parrafo nuevo; "nueve"
pasa a "diez"), guia-6 (con T03), ES-09 (con T05), ES-10 ("la combinacion de esas piezas"), ES-11, T06 (con ES-01),
T07 (filas 148-149 de MAPA cerradas; fila del capitulo actualizada).

Correccion al lado, no senalada: la oracion "esa comparacion con observaciones reales es la del contraste de realismo"
atribuia al contraste de realismo una comparacion de Peters et al. con lo real; ahora dice "En este trabajo, la
comparacion con observaciones reales es la del contraste de realismo del Objetivo 3, que no incluye al protocolo
fisico" (`capitulo3.tex` §ap-realismo: "sin intervencion del protocolo fisico").

Nada RECHAZADO ni ESCALADO. `\GAPLIT` nuevos: ninguno (no hay candidatos que agregar a `_candidatos.md`).

## Decisiones de redaccion

- `\REVVISUAL` envuelve una o varias oraciones completas dentro de un mismo parrafo (o un inciso), nunca un salto de
  parrafo (`\textcolor` no admite `\par`). El supuesto del dominio de imagen va envuelto en todos los lugares donde se
  enuncia (cuerpo, cierre y tabla), igual que exige la decision de 2026-09-30 de enunciarlo igual en los tres.
- Entra en `\REVVISUAL`: supuesto del dominio de imagen, contraste de realismo, truncamiento y suficiencia de
  $B_\delta$, la banda "para los efectos de adquisicion" en el aporte. No entra: el desenlace del TOST (medida de
  *streak amplitude* frente al protocolo fisico), las metricas de Peters et al. y el realismo de lesiones sinteticas
  ajenas.
- Desenlace del Objetivo 3 fuera de la introduccion y del cap. 3 (sustituye a la fila 2026-10-15 de capitulo2-r07):
  "no concluyente: los datos no permiten afirmar la equivalencia, y la *streak amplitude* del sintetizador queda por
  debajo de la del protocolo fisico", con remision al capitulo de resultados y la salvedad de que la lectura se fijo
  despues de ver el resultado; una sola vez por capitulo mas la celda de tabla; los demas pasajes remiten sin repetirlo.
- MAR no pareada = "la MAR que se entrena sin pares de una misma imagen con metal y sin el"; U-DuDoNet y PND-Net se
  nombran una vez junto al autor (regla de nombres en caja mixta).
- Brecha acotada (DEC 2026-10-15 (3) pto 9), texto fijo para G-B10: "la sintesis del implante y de su artefacto
  local, condicionada por la geometria y la pose de un implante colocado por un muestreador quirurgicamente
  restringido, y evaluada como producto frente a un protocolo fisico".
- Yang et al. se describen siempre como "no usan atlas" y con canal en arco por pelvis; los planificadores se agrupan
  como "con un atlas ... o con una busqueda sobre la pelvis del paciente".
