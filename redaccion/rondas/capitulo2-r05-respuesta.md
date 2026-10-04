# capitulo2 — r05 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo2.tex`. Se leyeron los cuatro reportes de la ronda.
No se abrio ningun PDF. Fuentes consultadas: fichas `wang2025adaptiveweighting` (Sec. V-A-2, V-A-3, V-B: test
sintetico de 2000 pares; CLINIC-metal solo con evaluacion visual), `lin2019` (artefacto "siempre simulado" sobre
DeepLesion), `li2024` (simulado en sinograma sobre DeepLesion; +0.64 dB, Sec. IV-B.4), `kaiser2014dysmorphism`
(reformateo perpendicular al platillo superior de S1, Fig. 1; area, longitud, angulos coronal y axial,
p. e120(2)), `gardner2010safezones` (50 pacientes, lado no lesionado; S1 222 frente a 346 mm2, p. 624; Carlson sin
diferencia, p. 628), `arand2019pelvicring` (ala sacra baja frente a cuerpo S1 intermedio, p. 381);
`docs/01-decisiones.md` 2026-09-08 (2) "No se estratifica por fenotipo sacro" y 2026-09-08 (4); `introduccion.tex`:54
y :58; `capitulo3.tex`:168, :217, :223.
Criterio PAT-58: dos parrafos se partieron (corredor, l. 68; Li y reclamo, l. 82) y una oracion se movio (banda,
de l. 94 a l. 90); ningun parrafo pasa de siete oraciones.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 = ES-01 | guia, estilo | APLICADO | Cuerpo: "En su prueba simulada, una red no entrenada en la ventana estrecha obtiene en ella 26.76 dB de PSNR y 0.9501 de SSIM, frente a 32.67 dB y 0.9803 de su version multiventana" (oracion acortada por el lint E-O1). Celda: "En datos simulados y en la ventana estrecha, PSNR de ...". Ficha: test sintetico, Sec. V-A-2 y V-B |
| guia-2 | guia | APLICADO | El parrafo del corredor se parte en dos (PAT-58). El primero queda con los procedimientos computables (Kaiser, McLaren, Ramadanov y Zabler, remision a `sec:corredor`). El segundo abre con "Las mismas mediciones muestran que el corredor varia entre pelvis y que esa variacion no se agrupa de forma consistente por fenotipo"; luego vienen Gardner (S1: 222 frente a 346 mm2, lado sin lesion de 50 TC; estudio previo sin diferencia) y Ziran, y cierra con la consecuencia: "medir el corredor en cada volumen en lugar de estratificar por fenotipo" (DEC 2026-09-08 (2) y (4); = `capitulo3.tex`:168). No se escribe "inversion" ni "igual seguridad", que la DEC (4) descarta |
| ES-02 | estilo | APLICADO | "Sobre artefactos simulados, Lin et al. obtienen 31.45 dB ..." (ficha: "siempre simulado"). Se omitio "sobre TC reales" para que la oracion no pasara el limite de E-O1 |
| ES-03 (re-apertura) | estilo | APLICADO | Se parte tras "... queda saturado". El parrafo nuevo tiene tres oraciones: el reclamo, la medicion ("aunque no entra en su criterio de fallo", que sustituye a "fuera de la regla de su compuerta") y el `\GAPDEC` sin cambios. El argumento nuevo es correcto: la compuerta se presenta en la l. 84, despues |
| ES-04 | estilo | APLICADO con variante | Se quita de l. 94 y cierra l. 90: "La banda $B_\delta$ trunca por diseno los efectos que estas fuentes describen lejos del metal, y esa limitacion se discute en la Seccion amenazas". Dice "efectos" y no "rayas", porque Selles et al. (lado contralateral) y Li et al. (toda la imagen) no describen rayas |
| ES-05 | estilo | APLICADO | Texto propuesto, sin cambios |
| ES-06 = T01 | estilo, traza | APLICADO | "Sobre los mismos datos, Karageorgos et al. reportan un RMSE de 20.2 para el algoritmo de MAR con que Peters et al. calibran la escala de sus metricas" (ficha Tabla I p. 28, la misma que el 12.3) |
| ES-07 | estilo | APLICADO con variante | l. 88: "Se asume que la apariencia del artefacto puede generarse en el dominio de imagen, porque la sintesis no separa las contribuciones del paciente y del metal; la comparacion prevista con el protocolo fisico podria contradecir ese supuesto". El enunciado coincide con la tabla y con l. 134. Con la redaccion propuesta, la oracion llegaba a 51 palabras (E-O1), y partirla dejaba el parrafo en ocho oraciones |
| ES-08 | estilo | APLICADO | l. 98: "la fila propia anade su supuesto y su convencion"; la formulacion completa queda solo en l. 134 |
| ES-09 | estilo | APLICADO | "Kaiser et al. reformatean 104 TC de pelvis no lesionadas perpendicularmente al platillo superior de S1 y miden en ellas el area transversal, la longitud y los angulos axial y coronal del corredor" (ficha §C y §D). McLaren queda en una oracion aparte y sin "reproducible" (ES-14) |
| ES-10 | estilo | APLICADO | "Aunque su mascara de sintesis es el cilindro parametrico, el sintetizador se entrena como esas fuentes, ..., y la diferencia entre ambas mascaras es uno de los desplazamientos de dominio ..." |
| ES-11 | estilo | APLICADO | Texto propuesto; sin "Ademas" |
| T02 | traza | ESCALADO | Sin cambio en el texto: los RMSE de l. 86 y l. 94 siguen sin unidad (BITACORA §2, capitulo2-r03). Pregunta para la autora abajo |

## Hallazgos bajos

Aplicados: guia-3 = T08 (dos razones partidas, con la de la geometria copiada de `introduccion.tex`:58), guia-4
(l. 44 y l. 70: "que describen donde va el metal lo colocan al azar, ..."; se mantiene la formula fija de §2),
guia-5 = T06 (l. 126: "El diseno de este trabajo preve comparar por *streak amplitude* la apariencia sintetizada con
la insercion por copia y pegado", segun `capitulo3.tex`:217 y :223; el protocolo fisico queda como "segunda
comparacion"), guia-6 = T05 ("orden de magnitud" para los errores; "escala" queda solo para la de Peters y la de
brecha), ES-12, ES-13 (ficha Arand: "ala sacra baja, cuerpo S1 intermedio"), ES-14, ES-15, ES-16 (unida con ES-08),
ES-17, ES-19, ES-20, T04 ("para su metodo completo").

No aplicados:
- ES-18 RECHAZADO: `introduccion.tex`:54 usa "planificacion quirurgica determinista", y BITACORA §2 (capitulo2-r00)
  fija que la brecha se enuncia con las mismas palabras que la introduccion (G-B10). Si se cambia, debe cambiarse
  primero en la introduccion.
- guia-7 = T07: sin cambio, pendiente fuera de la seccion (1).
- T03: depende de la relectura de T02; no se afirma ninguna region.

## Escalado para la autora

**T02 — Unidad de los RMSE de Karageorgos et al. (12.3, 20.2; 7.57, 11.45, 54.82) y de Yun et al. (12.74).**
DEC 2026-09-15 (2) y `capitulo3.tex`:67 los dan en HU. Las fichas `karageorgos2024ddpm` y `yun2026simulationdriven`
no registran unidad, y la decision de redaccion de capitulo2-r03 manda escribirlos sin unidad. Pregunta: ¿se
encarga a `lector-papers` la relectura de Karageorgos (Tablas I y III, Sec. II-G; tambien la region sobre la que se
calcula el RMSE, que pide T03) y de Yun (Tabla 1, Sec. 2.4.2) para fijar la unidad, o la autora confirma HU
directamente desde los PDF? Si se confirma HU, se agrega en l. 86 y l. 94. Si no se confirma, hay que corregir la
DEC y `capitulo3.tex`:67, porque hoy el cap. 2 y el cap. 3 no coinciden.

## GAP tras la ronda

Lint: lit = 1, dato = 2, dec = 9, sin cambios. No se abrio ni se cerro ningun GAP. En MAPA, la fila del `\GAPDEC`
de codificacion y precision anota que pasa a un parrafo propio (ES-03). `_candidatos.md` no cambia.

## Pendientes fuera de mi alcance

1. Siguen: `introduccion.tex`:46 y `capitulo3.tex`:172 dan como no verificada la ida y vuelta sin autoencoder
   que el cap. 2 da por medida, y `capitulo3.tex` `sec:obj1` no describe esa medicion (PAT-88, guia-7, T07).
2. `capitulo4.tex` sin `\label{cap:resultados}`: cuando exista, cambiar "en el capitulo de resultados" por `\ref`.
3. T02 (arriba), y con el T03.
4. "Zona segura" sin definicion en su primera aparicion (`introduccion.tex`:75). Ahora tambien aparece en el
   parrafo de Gardner.
5. Relecturas previas: `ramzan2026claim` Sec. 3.5, `herman2016` p. 8, `hu2023` Fig. 3.

## Lint

`python scripts/lint_redaccion.py capitulo2 --compilar`: PASA, alta = 0, media = 0, baja = 0; compila, 90 paginas.
Un primer paso marco cinco oraciones de mas de 40 palabras (E-O1), todas de esta ronda; se partieron o acortaron.

## Decisiones de redaccion

1. Un supuesto se enuncia con las mismas palabras en el cuerpo, en la tabla y en el cierre ("la apariencia del
   artefacto puede generarse en el dominio de imagen").
2. Para el tamano de un error se escribe "orden de magnitud"; "escala" se reserva a las escalas de medida (grados de
   brecha, puntuacion de Peters et al.).
3. Una cifra de una fuente en una oracion que cita otra fuente lleva como sujeto a los autores que la reportan.
4. Cuando una correccion haria crecer un parrafo por encima de siete oraciones, se parte por funcion antes de
   anadir (aplicacion de PAT-58).
