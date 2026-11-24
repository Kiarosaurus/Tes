# F6 lote 6 — cap2 (capitulo2.tex), modo corregir

Archivo editado: overleaf/secciones/capitulo2.tex (CRLF conservado; 128 a 126 lineas). Respaldo previo en el scratchpad de la sesion.

## (a) Aplicado / parcial / no aplicado

| ID | Estado | Detalle |
|---|---|---|
| B-022 | Aplicado | Hoja de ruta (l.10) reducida a una enumeracion Seccion-Objetivo. Metodologia (l.12) reescrita en voz impersonal y mas corta. Se conserva la declaracion de revision narrativa, dirigida y sin protocolo (G-B6) y la de que no se declaran bases ni criterios. Se quito "La autora definio la lista / la autora decidio" (sujeto persona). |
| B-023 | Parcial | Se dejo 1 resultado clave por fuente cuando el resto esta en tab:comparacion. Chen: se quito la prueba visual con radiologos (en tabla; sigue mencionada en l.30). DiffBoost: queda proximo 78.46 a 84.56 %; bazo y mama pasan a la tabla. Karageorgos: se quito SSIM 0.964 (en tabla); queda "13 de 28". Peters: ruido fusionado en una sola oracion (el 13.3 % esta en tabla, el < 10 % solo en prosa, por eso se conserva). Liu: se quitan 2.56 mm / 3.31 grados y 86.7 % (en tabla); queda la distancia al borde oseo, que no esta en tabla y se usa en la Seccion de medidas. NO tocado: Ramzan (58.89 a 63.53, su unico resultado), Zwingmann 2009 (69/40 %, remite a sec:sap), y las cifras de Wang (PSNR/SSIM), que son B-028 (otro lote). |
| B-024 | Aplicado | l.76: se quito la repeticion verbatim "al azar, con una regla geometrica o a mano"; ahora dice que los trabajos de insercion no ligan la colocacion a una distribucion clinica medida. La forma completa (y "meaningful locations") queda solo en l.46, canonica. |
| B-025 | Aplicado | l.114: se quito "se valido en un fantoma y en dos dimensiones"; queda solo que la validacion tampoco fue frente a artefacto en pacientes, con remision a sec:ea-simulacion. Canonico: l.44 (intacto). El "dos dimensiones" de l.118 es el motivo de costo del protocolo, no un limite de validacion, y se conserva. |
| B-027 | Aplicado | l.96: se quitan 12.3 / 20.2 / 12.74. Se conserva la logica de brecha (no hay umbral de aprobacion; el orden de magnitud lo dan los RMSE de MAR en datos simulados), las tres citas y la definicion de RMSE, y se remite a Seccion sec:obj1. |
| B-029 | Aplicado | l.110: se quito la descripcion columna por columna. l.112: compactada. l.114: ver B-025. l.116: ultima oracion igualada a la de la intro ("La brecha que queda es la sintesis del implante y de su artefacto local, condicionada por ..."), identica palabra por palabra desde ese punto (G-B10). l.118: tres oraciones de la comparacion reducidas a una con las dos remisiones y se conserva la razon de por que el protocolo fisico no sustituye al sintetizador. l.120 (desenlace no concluyente): eliminada. |
| B-026, B-028, B-030 | No aplicados | Segun instruccion (otro lote). |

Efecto colateral corregido: l.100 remitia el desenlace a la Seccion ea-brecha, que ya no lo contiene; ahora remite al Capitulo~\ref{cap:resultados} (mismo texto, solo cambia el \ref).

## (b) Palabras (texcount -brief -inc -q)

Antes 7005; despues 6702 (-303).

## (c) Cifras o resultados quitados y donde SI estan

| Quitado de cap2 | Donde sigue |
|---|---|
| Prueba visual Chen (cerca de la mitad tomada por real, cuatro radiologos) | anexos.tex tab:comparacion (fila Chen) |
| Dice bazo 94.42 a 94.78 % y mama 62.92 a 71.65 % (DiffBoost) | tab:comparacion (fila Zhang) |
| SSIM 0.964 (Karageorgos) | tab:comparacion (fila Karageorgos) |
| Peters: "hasta 13.3 %" como oracion aparte | sigue en la misma prosa (fusionada) y en tab:comparacion |
| Liu: 2.56 mm, 3.31 grados, 12 casos, 86.7 %, tres cirujanos | tab:comparacion (fila Liu) |
| RMSE 12.3, 20.2, 12.74 | capitulo3.tex l.105 (Seccion sec:obj1), con las tres citas |
| Desenlace Obj. 3 (no concluyente; IC 90 %; streak amplitude del sintetizador menor; lectura fijada tras ver el resultado) | capitulo4.tex l.128-130 (lectura y desenlace), conclusiones.tex l.18 (13 pacientes, -301.0 HU, IC 90 % de -477.0 a -124.9, margen 196.3 HU) y la fila "Este trabajo" de tab:comparacion. Comprobado con grep. Tambien "la equivalencia no se toma como premisa": introduccion.tex l.58 |
| Descripcion de los 13 pacientes / eje sin perturbar / contraste primario | tab:comparacion (fila propia) y introduccion.tex l.58; el limite de poses se mantiene en l.118 |

Referencia de seccion quitada junto con l.120: \ref{sec:ap-analisis} (la lectura posterior al resultado sigue en capitulo4 l.128 con ese mismo \ref).

## (d) Cambios en \cite y marcas GAP

- \cite: ninguno (diff de conteos por clave identico, 60 claves). Ninguna cita estaba sostenida por una oracion unica quitada.
- \ref: se pierde \ref{sec:ap-analisis} (l.120) y un \ref{sec:ea-brecha} (l.100, reemplazado por \ref{cap:resultados}); se agregan 2 \ref{tab:comparacion} (remisiones a la tabla) y 1 \ref{sec:ea-simulacion} (l.114). Ningun \label tocado.
- Marcas: unica marca real = 1 \GAPLIT (l.88, ficha de la fuente primaria del esquema multiventana), intacta. No hay GAPDATO/GAPDEC/REVVISUAL en este archivo; el "6" de texcount no corresponde a marcas GAP (el grep cuenta 1). No cambia ninguna.

## (e) tab:comparacion y la tesis

Si. anexos.tex tab:comparacion tiene diez filas de trabajos y una fila final "Este trabajo" (enfoque con supuesto y convencion, colocacion, fuera del objeto, resultado con el desenlace no concluyente y lo no ejecutado). No se agrego nada.

## Lint

python3 scripts/lint_redaccion.py capitulo2 --compilar: PASA (alta=0, media=0, baja=0; GAP lit=1). Compila (205 paginas). Primera pasada marco 6 oraciones largas (E-O1); se partieron.

## Observaciones

- l.46 sigue siendo la unica formulacion completa de "al azar / regla geometrica / a mano"; si B-030 o una revision posterior acorta intro:62, mantener ahi la remision.
- La voz impersonal se aplico solo en los parrafos editados (l.10, 12, 76 no tenia sujeto persona, 96, 110-118). Quedan fuera por alcance oraciones tipo "Este trabajo lee esa atribucion..." (l.22, 88, 106, 124 y similares) en parrafos no editados; conviene un lote aparte.
