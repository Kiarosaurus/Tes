# Respuesta del redactor — capitulo3 — r12

Modo `corregir`. Archivo editado: `overleaf/secciones/capitulo3.tex` (CRLF conservado). Lint final:
`PASA` (alta 0, media 0, baja 14, todas E-P1 de cifras propias con fuente en el inventario de trazabilidad).
GAP del capitulo: lit 2 / dato 13 / dec 16 (antes 2/13/12). E13 de r10 sigue RECHAZADO (BITACORA §2) y no se reabre.
Ninguna cifra de la corrida final en prueba; #158 sigue ABIERTA y conserva su `\GAPDEC`.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 | trazabilidad | APLICADO + ESCALADO | l. 192: "lotes de 16" (`a7_entrenar.sbatch`:60 `--lote 16`; `meta` de los `ckpt` de `run01` y `run02` en IMP #148) con `\GAPDEC`: DEC 2026-10-08 A.3 da lote 4 (el del piloto, IMP #134). BITACORA §2 2026-10-10 (describir lo corrido + `\GAPDEC`). DEC no se toca |
| T02 | trazabilidad | APLICADO + ESCALADO | DEC 2026-09-21 (2) e IMP #105: `0102` (cremallera) y `0019` (accesorio) llevan metal no ortopedico. l. 208: "dos pelvis de validacion sin osteosintesis cuyo corredor admite el tornillo, una de ellas con un objeto metalico no ortopedico, una cremallera" + `\GAPDEC` sobre por que no son receptores `0046`/`0066` (sin metal): ninguna DEC lo dice (DEC 2026-10-09 (4) pto 4 solo excluye `0019`). l. 322: "un tercer paciente de validacion sin osteosintesis, que lleva un accesorio metalico". Amenaza en validez de la conclusion: uno de los dos receptores del margen lleva un objeto que la sintesis en prueba excluye |
| T03 | trazabilidad | APLICADO | Validez interna, Obj 2: se anaden la sensibilidad sin los dos casos con error de segmentacion (DEC 2026-10-08 pto 22; l. 101) y el intervalo por remuestreo de W1 (pto 18, decidido con la distancia conocida, pto 17). La lista quedo en dos oraciones (E-O1) |
| guia-1 | guia | APLICADO + ESCALADO | Parrafo nuevo en validez interna: punto de control, material y $\Delta$ sobre los mismos dos receptores; los dos primeros con los mismos dos tornillos de `metal_0039`. Solo se afirman los sentidos registrados: Ti acerco el protocolo fisico al sintetizador en validacion (l. 310; #161; DEC 2026-10-09 (5)) y el margen fijado por el sintetizador facilita concluir equivalencia (DEC 2026-10-09 (4) pto 3). El efecto conjunto no consta en ninguna fuente: `\GAPDEC` |
| guia-2 | guia | APLICADO + ESCALADO | l. 198: la decision de la mascara (DEC D1) preveia el semimaximo como sensibilidad, el diseno congelado no la programa (`diseno_A.md` §0 no la nombra) + `\GAPDEC`. Mismo tratamiento que la promesa RMSE/SSIM de r11 (BITACORA §2 2026-10-10) |
| guia-3 | guia | APLICADO | (a) Obj 3: la regla de la referencia de realismo se escribio con 3 de 11 pacientes de prueba revisados y un tornillo aislado hallado que la lista previa no tenia (DEC 2026-10-09 (7)); usa informacion de inclusion de prueba y ningun resultado de sintesis. El cierre pasa a "Ni el percentil 5, ni el ancho de cascara, ni el material usaron pacientes de prueba". (b) como T03 |
| E1 | estilo | APLICADO | l. 294: se borra "y eso es lo que hace hibrido al protocolo" (primera propuesta; no se redefine el termino de la fuente) |
| E2 | estilo | APLICADO | l. 180: la causa ya no es circular ni usa "sonda": "su unica fuente era una medicion de densidad previa que quedo invalidada por un error de nivel vertebral y por la geometria de la region en que media" (DEC 2026-09-13 #50: "refutado por dos mecanismos: el error de nivel y la geometria de la sonda"; DEC 2026-10-08 pto 14) |
| E3 | estilo | APLICADO | l. 366: "Este trabajo asume que la sintesis no necesita separar esas dos contribuciones." |
| E4 | estilo | APLICADO | "La cohorte receptora no es una coleccion de pelvis sanas." pasa, sin "por tanto", al final de l. 56 |
| E5 | estilo | APLICADO | Apertura que nombra los tres parametros; la salvedad de las fuentes de fabricante pasa al final del parrafo |
| E6 | estilo | APLICADO | l. 186: "la preservacion fuera de $G$" |
| E7 | estilo | APLICADO | l. 206: "en los dos entrenamientos" |
| E8 | estilo | APLICADO (en sentido inverso) | Manda la trazabilidad (T02): "sin metal" era falso para `0102`. Se unifica en "sin osteosintesis" en l. 208 y en la oracion de los receptores, no en "sin metal" |
| E9 | estilo | APLICADO | Parrafo del perfil (5 oraciones) y parrafo del histograma, que absorbe la comparacion con los tornillos de `metal_0039` y la confirmacion en cortes; la oracion de los receptores pasa al final de l. 208. El parrafo del cotejo abre con "La referencia del cotejo se limita a ese paciente." |
| E10 | estilo | APLICADO | El costo de 114.7 h pasa al parrafo de la segunda corrida: "El costo, que en la primera corrida era de 114.7 horas de computo, siguio fuera del limite, con 108.9 horas proyectadas." |
| E11 | estilo | APLICADO | l. 376 partido en dos parrafos (margen; cortes distintos y tamano de muestra), sin "ademas" en cadena, "por otra parte" ni "por ultimo". Absorbe E16 y la amenaza de T02 |

## Bajos

Aplicados: guia-4 (caja final de la Figura 3.1 con realismo frente a tornillos reales y reconstruccion de implantes
reales), guia-5 y E19 ("corrida" fuera de entrenamientos y muestreador: l. 133 "generaciones", l. 174 "cohortes",
l. 176 y l. 237 "antes de muestrear las poses", l. 186 "los dos entrenamientos", l. 178 `\GAPDATO` "ejecucion"),
T04 (la marca de l. 258 pregunta tambien la region y dice que el complemento de $B_{\delta}$ incluye $M$), E12
("140 000 pasos en lugar de 37 500"; el parrafo de 2 oraciones no se movio: su contenido no encaja en l. 206, que va
antes de definir el cotejo), E13, E14, E15, E16 (con E11), E17 (sujeto antepuesto en l. 354), E18, E20.
No aplicados: las 14 E-P1 del lint (cifras propias, todas con fuente en el inventario de `-trazabilidad.md`).

Cambio colateral: el lint marco cuatro oraciones de mas de 40 palabras creadas por mis correcciones (l. 214, 237,
354, 358); se partieron. La confirmacion en cortes de los tornillos de `metal_0039` paso del parrafo del cotejo al
del histograma para que el primero no creciera a 8 oraciones.

## Escalados para la autora (con pregunta)

1. **T01, lote.** DEC 2026-10-08 A.3 dice "tal como corrio ... lote 4"; el script y los puntos de control dicen 16.
   Pregunta: ¿corriges DEC A.3 a lote 16 (errata) o lo declaramos como desviacion?
2. **T02, receptores.** `0046` y `0066` son las pelvis de validacion sin ningun metal (DEC 2026-09-21 (2)), pero los
   receptores del cotejo, del material y de $\Delta$ son `0101` y `0102` (este con cremallera). Pregunta: ¿por que
   quedaron fuera `0046` y `0066` (corredor, control de nivel, otra razon)? Si hay registro, se cita; si no, hace falta
   una entrada en DEC.
3. **guia-1, ajuste conjunto.** Pregunta: ¿se declara que fijar punto de control, material y $\Delta$ sobre los
   mismos dos receptores sesga la prueba de equivalencia hacia concluir equivalencia, o solo que el efecto conjunto
   no esta establecido (como dice hoy el texto)?
4. **guia-2, semimaximo.** DEC D1 lo preve como sensibilidad y el diseno congelado no. Pregunta: ¿se entrena y
   reporta (seria un tercer entrenamiento) o se retira la promesa?

## GAP

- Nuevos `\GAPDEC` (4): lote (T01), receptores `0046`/`0066` (T02), sesgo conjunto (guia-1), semimaximo (guia-2).
  Anotados en `redaccion/MAPA.md`; la fila de RMSE/SSIM (r11 T01) se precisa con T04.
- Sin `\GAPLIT` nuevo: `_candidatos.md` no cambia. Sin GAP cerrados.
- Totales (lint): 2/13/12 -> 2/13/16 (lit/dato/dec).

## Decisiones de redaccion

- Los pacientes de validacion `0102` y `0019` se nombran "sin osteosintesis" con su objeto metalico no ortopedico
  ("una cremallera", "un accesorio metalico"), nunca "sin metal". "Sin metal" queda solo para el grupo 3 (ningun
  objeto metalico), como en la clasificacion 19 = 11 + 8 de la particion de prueba.
- "Corrida" se reserva para la sonda y la corrida final; para el entrenamiento se dice "entrenamiento", para el
  sintetizador "generacion" y para el muestreador "muestrear las poses" o "cohorte".
- Una amenaza cuyo sentido solo esta registrado en parte se escribe con los sentidos registrados como hecho y el
  efecto conjunto en `\GAPDEC`; no se infiere la direccion.
- En la lista de decisiones post hoc de amenazas se incluyen tambien los analisis anadidos despues de ver datos
  (sensibilidades, intervalos no preinscritos) y las reglas escritas con informacion parcial de la particion de prueba,
  con el alcance exacto de lo que usaron.
