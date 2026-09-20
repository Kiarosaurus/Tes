# synthes_screw_reference_chart — Synthes Screw Reference Chart

**Profundidad: documentacion tecnica del fabricante, no revisada por pares**

- **DOI / URL:** NO ENCONTRADO EN EL PDF
- **Nivel de lectura:** 3 (contexto) — propuesto por el asistente; confirma la autora
- **Leido a fondo por la autora:** no
- **PDF:** papers/Synthes Screw Reference Chart.pdf

## Datos bibliograficos exactos (para armar la entrada)

| Campo | Texto impreso | Donde |
|---|---|---|
| Titulo de portada | *"Synthes Screw Reference Chart"* | portada, sin numero impreso (PDF p. 1) |
| Subtitulo de portada | *"Screws, Drill Bits, Taps and Guide Wires"* | portada (PDF p. 1) |
| Organizacion / fabricante | *"SYNTHES"* (logotipo) | portada (PDF p. 1) y pie del poster (PDF pp. 2-4) |
| Filiacion institucional | *"Original Instruments and Implants of the Association for the Study of Internal Fixation — AO ASIF"* | portada (PDF p. 1) y pie del poster (PDF pp. 2-4) |
| Copyright | *"©2002 SYNTHES (USA)"* | pie del poster, izquierda (PDF pp. 2-4) |
| Aviso de marcas | *"SYNTHES and ASIF are registered trademarks of SYNTHES (USA) and SYNTHES AG Chur"* | pie del poster (PDF pp. 2-4) |
| Codigo de documento | *"GP0644-C"* | pie del poster, esquina inferior derecha (PDF pp. 2-4) |
| Fecha impresa junto al codigo | *"4/04"* | pie del poster, esquina inferior derecha (PDF pp. 2-4) |
| Codigo adicional | *"J1364-C"* | pie del poster, esquina inferior derecha (PDF pp. 2-4) |
| Lugar de impresion | *"Printed in U.S.A."* | pie del poster (PDF pp. 2-4) |
| Direccion USA | *"SYNTHES (USA), 1690 Russell Road, Paoli, PA 19301-1262"* | pie del poster (PDF pp. 2-4) |
| Direccion Canada | *"SYNTHES (CANADA) LTD., 2566 Meadowpine Boulevard, Mississauga, Ontario L5N 6P9"* | pie del poster (PDF pp. 2-4) |
| Numero de version explicito | NO ENCONTRADO EN EL PDF (los sufijos *"-C"* de `GP0644-C` y `J1364-C` son lo unico parecido a una revision) | — |
| Autor personal | NO ENCONTRADO EN EL PDF | — |

**Aviso de transcripcion.** Los codigos `GP0644-C`, `4/04` y `J1364-C` estan impresos en
el cuerpo mas pequeno de la pagina, en la esquina inferior derecha del poster. Se
transcriben tal como se leen en la renderizacion; **la autora debe verificarlos** antes
de fijarlos en `refs/raw/`. El copyright `©2002 SYNTHES (USA)` y la fecha de impresion
`4/04` son inconsistentes entre si (ano de copyright 2002, tirada de abril de 2004): el
documento no aclara cual es la fecha de edicion.

**Paginacion.** 4 paginas de PDF. **Ninguna pagina lleva numero impreso.** La p. 1 es la
portada; las pp. 2, 3 y 4 del PDF reproducen la **misma** lamina de tres tablas
("Screws, Drill Bits and Taps", "Cannulated Screws, Guide Wires, Drill Bits and Taps",
"Locking Screws, Guide Wires, Drill Bits and Taps"). Toda cita a esta fuente debe decir
"lamina, PDF p. 2" y no un numero de pagina impresa, que no existe.

**Naturaleza de las tablas.** Es un poster de una sola lamina, con las tablas compuestas
tipograficamente y una fila de fotografias de tornillos a escala intercalada. El cuerpo
de letra es muy pequeno. Se transcribe unicamente lo que se lee con seguridad; las
fotografias de tornillos **no llevan cotas** y no se usan para extraer ninguna dimension.

## Que hace (3 lineas maximo)

Lamina de referencia que cruza, para cada diametro de tornillo Synthes, el tipo de
tornillo, la longitud de rosca, el diametro de aguja guia, las brocas de orificio
deslizante y roscado, el macho y el tipo de acoplamiento.

## Restriccion o supuesto clave

No es un articulo cientifico. Su valor para la tesis es una sola cosa, pero decisiva: el
encabezado de las tres tablas es *"SCREW DIAMETER (mm)"* y la fila que lleva los valores
6.5 y 7.3 se rotula **"Thread Diameter"**. Es decir, el fabricante llama "diametro del
tornillo" al **diametro de rosca**, exactamente la sospecha de la implicancia #97. La
lamina **no** publica diametro de fuste, de nucleo, de canulacion ni de cabeza, ni paso
de rosca, ni arandelas, ni material: para eso hace falta la tecnica quirurgica
(`synthes_cannulated_screws`).

**Trampa de lectura:** en la primera tabla existen columnas rotuladas *"Shaft"* bajo los
diametros 4.0 y 4.5. Ahi *"Shaft"* es un **tipo de tornillo** (shaft screw), no una
dimension de fuste. No confundirlo con la columna *"Shaft diameter"* de la tecnica
quirurgica.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| El nominal 7.3 es diametro de rosca | *"SCREW DIAMETER (mm)"* / *"Thread Diameter"* ... *"7.3"* | Cannulated Screws, lamina, PDF p. 2 |
| Longitudes de rosca del 7.3 canulado | *"Thread Length ... 16 mm | 32 mm | Full"* | Cannulated Screws, lamina, PDF p. 2 |
| Longitudes de rosca del 6.5 canulado | *"Thread Length ... 16 mm | 32 mm | Full"* | Cannulated Screws, lamina, PDF p. 2 |
| Aguja guia 2.8 mm (instrumental) | *"Guide Wire ... 2.8"* | Cannulated Screws, lamina, PDF p. 2 |
| Broca de orificio roscado 5.0 mm (instrumental) | *"Drill Bit for Threaded Hole ... 5.0"* | Cannulated Screws, lamina, PDF p. 2 |

## Donde entra en mi tesis

Objetivo 1 / geometria del implante: es la cita mas limpia para afirmar que "7.3 mm" es
diametro de rosca y no del cuerpo, y la unica de las tres fuentes que da las **longitudes
de rosca en mm (16 / 32 / completa)** para el canulado de 7.3 y de 6.5.

## Dudas para el asesor

1. Se cita esta lamina como fuente del "16/32 mm", o se prefiere el catalogo Acumed, que
   publica los mismos 16/32/full con numeros de parte?
2. Copyright 2002 y tirada 4/04: que ano se pone en la entrada bibliografica?

## Evidencia textual

Toda la lamina carece de numeracion impresa; se indica la pagina del PDF. Las tres
tablas son identicas en las PDF pp. 2, 3 y 4.

### Datos bibliograficos

| Dato | Frase o celda original (max. 15 palabras) | Pagina impresa / PDF |
|---|---|---|
| Titulo | *"Synthes Screw Reference Chart"* | sin numero impreso / PDF p. 1 |
| Subtitulo | *"Screws, Drill Bits, Taps and Guide Wires"* | sin numero impreso / PDF p. 1 |
| Copyright | *"©2002 SYNTHES (USA)"* | sin numero impreso / PDF p. 2 |
| Marcas registradas | *"SYNTHES and ASIF are registered trademarks of SYNTHES (USA) and SYNTHES AG Chur"* | sin numero impreso / PDF p. 2 |
| Codigo, fecha y codigo adicional | *"Printed in U.S.A.  GP0644-C  4/04  J1364-C"* | sin numero impreso / PDF p. 2 |
| Filiacion AO | *"Original Instruments and Implants of the Association for the Study of Internal Fixation — AO ASIF"* | sin numero impreso / PDF p. 2 |

### Sistema 7.3 mm canulado

| Magnitud | Frase o celda original (max. 15 palabras) | Pagina impresa / PDF |
|---|---|---|
| Encabezado de la tabla | *"SCREW DIAMETER (mm)"* | sin numero impreso / PDF p. 2 |
| Rotulo de la fila del nominal | *"Thread Diameter"* | sin numero impreso / PDF p. 2 |
| Valor del nominal | *"7.3"* | sin numero impreso / PDF p. 2 |
| Tipo de tornillo | *"Cancellous / Self-drilling / Self-tapping"* | sin numero impreso / PDF p. 2 |
| Longitudes de rosca | *"16 mm | 32 mm | Full"* | sin numero impreso / PDF p. 2 |
| Acoplamiento | *"4.0 mm Hex"* (fila *Drive Type*) | sin numero impreso / PDF p. 2 |
| Diametro de FUSTE | NO ENCONTRADO EN EL PDF | — |
| Diametro de NUCLEO | NO ENCONTRADO EN EL PDF | — |
| Paso de rosca | NO ENCONTRADO EN EL PDF | — |
| Diametro de canulacion | NO ENCONTRADO EN EL PDF | — |
| Diametro y perfil de cabeza | NO ENCONTRADO EN EL PDF (solo fotografias sin cotas) | — |
| Longitudes de tornillo disponibles | NO ENCONTRADO EN EL PDF | — |

### Sistema 6.5 mm

| Magnitud | Frase o celda original (max. 15 palabras) | Pagina impresa / PDF |
|---|---|---|
| Nominal canulado | *"Thread Diameter ... 6.5"* (tabla de canulados) | sin numero impreso / PDF p. 2 |
| Tipo de tornillo canulado | *"Cancellous / Self-drilling / Self-tapping"* | sin numero impreso / PDF p. 2 |
| Longitudes de rosca (canulado) | *"16 mm | 32 mm | Full"* | sin numero impreso / PDF p. 2 |
| Acoplamiento (canulado) | *"4.0 mm Hex"* | sin numero impreso / PDF p. 2 |
| Nominal NO canulado | *"Thread Diameter ... 6.5"* (tabla de auto/no autorroscantes) | sin numero impreso / PDF p. 2 |
| Longitudes de rosca (no canulado) | *"16 mm Thread | 24 mm Thread | 32 mm Thread | Full Thread"* | sin numero impreso / PDF p. 2 |
| Acoplamiento (no canulado) | *"3.5 mm Hex"* | sin numero impreso / PDF p. 2 |
| Fuste, nucleo, paso, canulacion, cabeza del 6.5 | NO ENCONTRADO EN EL PDF | — |

### Tornillos bloqueados de 7.3 (aparecen en la tercera tabla)

| Magnitud | Frase o celda original (max. 15 palabras) | Pagina impresa / PDF |
|---|---|---|
| Nominal | *"Thread Diameter ... 7.3"* (Locking Screws) | sin numero impreso / PDF p. 2 |
| Tipos de cabeza | *"Locking Head"* y *"Conical Head"* | sin numero impreso / PDF p. 2 |
| Tipo de tornillo | *"Cannulated / Self-drilling, Self-tapping"* | sin numero impreso / PDF p. 2 |
| Longitudes de rosca | *"Full"* y *"Partial"* | sin numero impreso / PDF p. 2 |
| Aguja guia | *"Guide Wire and Threaded Wire Guide ... 2.5"* | sin numero impreso / PDF p. 2 |
| Broca | *"5.0 (optional)"* | sin numero impreso / PDF p. 2 |
| Macho | *"7.3 [311.682]"* | sin numero impreso / PDF p. 2 |
| Acoplamiento | *"4.0 mm Hex"* | sin numero impreso / PDF p. 2 |

### Arandelas, material e iliosacro

| Dato | Frase o celda original (max. 15 palabras) | Pagina impresa / PDF |
|---|---|---|
| Arandelas (referencia, DE, DI, espesor, material) | NO ENCONTRADO EN EL PDF — la lamina no incluye arandelas | — |
| Material declarado | NO ENCONTRADO EN EL PDF (no se nombra acero, 316L, titanio ni ASTM) | — |
| Asociacion con fijacion iliosacra o sacroiliaca | NO ENCONTRADO EN EL PDF — la lamina no menciona ninguna indicacion anatomica | — |

### Instrumental (NO es el implante)

| Instrumento | Frase o celda original (max. 15 palabras) | Pagina impresa / PDF |
|---|---|---|
| Aguja guia del canulado 7.3 | *"Guide Wire ... 2.8"* | sin numero impreso / PDF p. 2 |
| Aguja guia del canulado 6.5 | *"Guide Wire ... 2.8"* | sin numero impreso / PDF p. 2 |
| Broca de orificio deslizante 7.3 | *"Drill Bit for Gliding Hole (in hard bone) ... 7.3 [310.495]"* | sin numero impreso / PDF p. 2 |
| Broca de orificio roscado 7.3 | *"Drill Bit for Threaded Hole ... 5.0"* | sin numero impreso / PDF p. 2 |
| Macho 7.3 | *"Tap (in hard bone) ... 7.3 [311.689]"* | sin numero impreso / PDF p. 2 |
| Broca de orificio deslizante 6.5 canulado | *"7.3 [310.495]"* | sin numero impreso / PDF p. 2 |
| Broca de orificio roscado 6.5 canulado | *"5.0"* | sin numero impreso / PDF p. 2 |
| Macho 6.5 canulado | *"7.3 [311.689]"* | sin numero impreso / PDF p. 2 |
| Broca de orificio deslizante 6.5 NO canulado | *"4.5 in hard bone"* | sin numero impreso / PDF p. 2 |
| Broca de orificio roscado 6.5 NO canulado | *"3.2"* | sin numero impreso / PDF p. 2 |
| Macho 6.5 NO canulado | *"6.5 [311.66]"* | sin numero impreso / PDF p. 2 |
| Aguja guia del 7.0 canulado (contraste) | *"Guide Wire ... 2.0"* | sin numero impreso / PDF p. 2 |
