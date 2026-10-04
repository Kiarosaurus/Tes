# capitulo2 — r06 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo2.tex`. Se leyeron los cuatro reportes de la ronda.
No se abrio ningun PDF. Fichas consultadas: `kaiser2014dysmorphism` (§C, reformateo segun el eje del sacro,
perpendicular al platillo de S1, p. e120(3); area sobre "contiguous slices perpendicular" al corredor, p. e120(2); §F,
tres fenotipos), `jacob2026lgesynthnet` (Tablas 1 a 3; Dudas, punto 2), `lin2019` ("Metal partial volume effect is also
considered", Sec. 4, p. 10508), `deman1999` (Sec. III-B, rayas oscuras en las direcciones de mayor atenuacion; Sec.
III-D, rayas que irradian desde los metales), `glover1980nonlinear`, `chen2026foundationvae` (unidades de PSNR, SSIM y
MSE no declaradas, l. 40 y 253); DEC 2026-09-08 (2); `capitulo3.tex`:164.
PAT-58: ningun parrafo crece. l. 128 pierde una oracion; l. 132 gana una por la particion de ES-08 (queda en seis);
l. 70 conserva seis (no se agrega la mencion de Kaiser, que era opcional).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 = ES-03 = T02 (traza) | guia, estilo, traza | APLICADO | l. 70 abre: "El corredor varia entre pelvis, y los estudios revisados no coinciden en el efecto del fenotipo sacro sobre su tamano." Sin "las mismas mediciones" (PAT-34) ni "muestran" (PAT-41). La inconsistencia queda entre Gardner et al. y el estudio previo que recogen (DEC 2026-09-08 (2)). No se nombra la agrupacion de Kaiser: era opcional y anadiria una oracion (PAT-58) |
| ES-01 | estilo | APLICADO | l. 34: "de modo que insertar metal virtual no es lo que aporta este trabajo"; l. 136: "Insertar metal virtual en TC y usar difusion ..." |
| ES-02 | estilo | APLICADO | "simulan tambien el efecto de volumen parcial del metal" (ficha `lin2019`, Sec. 4, p. 10508) |
| ES-04 | estilo | APLICADO | "los autores de redes de MAR de varios dominios reportan ..." (Li et al., de cuatro dominios, es ejemplo del mismo parrafo) |
| ES-05 (re-apertura) | estilo | APLICADO | Texto propuesto: "porque sintetizar no exige separar las contribuciones del paciente y del metal". El enunciado del supuesto no cambia (tabla y l. 138 iguales) |
| ES-06 | estilo | APLICADO | l. 98, oracion 6: se quita "y en ella se apoya la decision ..."; la oracion 3 ya dice en que se apoya el diseno |
| ES-07 | estilo | APLICADO con variante | Se elimina la oracion 2 de l. 128. La oracion 4 queda "La simulacion de Peters et al. se valido en un fantoma y en dos dimensiones", sin "ademas". No se usa "Esa simulacion fisica", porque la oracion anterior incluye tambien la fila de Karageorgos et al., cuya simulacion no se valido en fantoma |
| ES-08 | estilo | APLICADO | Texto propuesto: "... ningun objetivo aisla estos elementos. La geometria parametrica no se aisla porque ..., y la codificacion y la banda no se aislan porque ..." |
| Cifras de `jacob2026lgesynthnet` (nota de guia, escalado del orquestador) | guia / orquestador | ESCALADO | Se pone `\GAPDEC{si se citan las cifras de Jacob et al., cuya ficha registra mejoras de Dice distintas entre el resumen y los resultados del articulo}` en l. 22. Las cifras no se quitan: la ficha (Dudas, punto 2) dice "conviene no citarlas sin decidir cual vale", lo que es una recomendacion y no una prohibicion. Ademas, 0.72 -> 0.77 es el valor de la Tabla 2 (N = 300), coherente con los "5 points" de Resultados. Pregunta abajo |

## Hallazgos bajos

Aplicados:
- guia-2: "las poses del segundo corredor bajo S1 se reportaran de forma descriptiva cuando se preinscriba y ejecute
  su muestreo" (= `capitulo3.tex`:164). Va en texto y no como un `\GAPDATO` nuevo, para no duplicar el GAP del cap. 3.
- guia-3: l. 84, "como codificacion de entrada y de salida" (= l. 86 y `capitulo3.tex`:172). `introduccion.tex`:60
  queda como pendiente fuera de la seccion.
- T01: "De Man et al. describen, en una simulacion bidimensional ..., rayas oscuras en las direcciones de mayor
  atenuacion y rayas que irradian desde el metal" (ficha, Sec. III-B y III-D). Usa "describen" y no "muestran" (PAT-41).
- T04: "reformatean 104 TC ... segun el eje del sacro, perpendicular al platillo superior de S1, y sobre cortes
  perpendiculares al corredor miden su area transversal, su longitud y sus angulos axial y coronal".
- ES-09, ES-10, ES-11, ES-12, ES-14, ES-16 ("Glover y Pelc reportan que"), ES-17, ES-19 (nueve filas, contadas),
  ES-20.
- ES-13 con variante: "Sobre datos simulados miden ...", y luego "En esa prueba, ...". La oracion de CLINIC-metal pasa
  al cierre del parrafo ("solo evaluan con una lectura visual", segun la ficha, Sec. V-B) para que "esa prueba" no
  remita a la lectura visual.
- ES-18 con variante (PAT-99): la formula queda en l. 72. En l. 88: "Ninguna de las fuentes revisadas responde si ...";
  en l. 90: "Las fuentes revisadas tampoco dan un umbral ..."; en l. 92: "Ningun trabajo revisado sintetiza ..." (se
  mantiene, porque es la carencia que convierte la oracion siguiente en supuesto, G-B7); en l. 98: "En las fuentes
  revisadas tampoco hay un precedente ...".

No aplicados:
- ES-15 RECHAZADO: la premisa ("la PSNR esta en dB") no esta en la ficha. `chen2026foundationvae.md`:40 y :253 dicen
  que el articulo no declara las unidades de PSNR, SSIM ni MSE. "Sus unidades", referido a las tres metricas, es
  correcto.
- guia-4: sin cambio, pendiente fuera de la seccion (1).
- T03: depende de una relectura de `selles2023ai` con `lector-papers`; no cambia el texto.

## Escalado para la autora

**Cifras de Jacob et al. (`jacob2026lgesynthnet`).** El capitulo cita el Dice de 0.72 a 0.77 con 300 imagenes
sinteticas (Tabla 2) y el SSIM de imagen completa de 0.587 (Tabla 1), en l. 22 y en la tabla. `_index.md` l. 107 dice
que hoy no se cita ninguna cifra, y la ficha pide decidir antes cual vale (mejora de Dice "up-to 6" en resumen frente a
"5 points" en resultados). Pregunta: ¿se mantienen estas dos cifras de tabla (0.72 -> 0.77 y 0.587), que no dependen de
la discrepancia del resumen, y se actualiza `_index.md`? ¿O se quitan, y el parrafo y la fila de la tabla describen a
Jacob et al. sin cifras? Si se mantienen, se quita el `\GAPDEC` de l. 22.

**T02 de r05 (unidad de los RMSE).** Sigue escalado, sin cambios.

## GAP tras la ronda

Lint: lit = 1, dato = 2, dec = 10. Se abre un `\GAPDEC` (cifras de Jacob et al., l. 22), anotado en MAPA. No se cierra
ninguno. `_candidatos.md` no cambia.

## Pendientes fuera de mi alcance

1. Siguen: `introduccion.tex`:46 y `capitulo3.tex`:172 dan como no verificada la ida y vuelta sin autoencoder, que el
   cap. 2 da por medida, y `sec:obj1` no describe esa medicion (PAT-88, guia-4).
2. `introduccion.tex`:60 limita el aporte a la "codificacion de la entrada"; el cap. 2 y el cap. 3 dicen "de entrada y
   de salida" (guia-3).
3. `_index.md` l. 107 (`jacob2026lgesynthnet`) contradice el texto hasta que la autora decida (escalado arriba).
4. T03: relectura de `selles2023ai` para completar su Evidencia textual (regiones, lado contralateral, "streaks
   throughout the images" con pagina).
5. Discrepancia interna de DEC 2026-09-15 (2): llama "difusion en imagen" al 12.3 de Karageorgos, y la ficha dice que
   opera en el sinograma (nota del auditor). El texto no repite el error.
6. La respuesta r05 justifico ES-04 con "Selles et al. no describen rayas", pero la ficha (`selles2023ai.md`:29) copia
   "dark and bright streaks throughout the images". El texto no cambia; esa razon no debe reutilizarse.
7. Siguen: `capitulo4.tex` sin `\label{cap:resultados}`; "zona segura" sin definir en `introduccion.tex`:75;
   relecturas de `ramzan2026claim`, `herman2016` y `hu2023`.

## Lint

`python scripts/lint_redaccion.py capitulo2 --compilar`: PASA, alta = 0, media = 0, baja = 0; compila, 90 paginas.

## Decisiones de redaccion

1. "Metal virtual" es el termino para el metal insertado por simulacion en TC reales. No se alterna con "sintetico"
   dentro de un mismo argumento (PAT-97). "Sintetico" queda para lo que genera el sintetizador de este trabajo.
2. Un negativo acotado a las fuentes revisadas varia de forma cuando se repite en parrafos vecinos ("ninguna de las
   fuentes revisadas ...", "las fuentes revisadas tampoco ...", "ningun trabajo revisado ..."), sin perder el
   acotamiento (PAT-99).
3. Para la inconsistencia del efecto del fenotipo se escribe "los estudios revisados no coinciden en el efecto del
   fenotipo sacro sobre su tamano". No se atribuye a "las mediciones" de una sola fuente.
