# capitulo2 — r03 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo2.tex`. Se leyeron los cuatro reportes de la ronda.
No se abrio ningun PDF. Fuentes consultadas: `experiments/objetivo1/p1_compuerta.md` (ll. 1-60),
`experiments/objetivo1/e6c_techo_lw.md` (ll. 1-40); fichas `arand2019pelvicring`, `herman2016`,
`karageorgos2024ddpm` (Tabla III y Apendice), `cassanego2026evolution`, `wang2025adaptiveweighting`,
`ramzan2026claim`, `peters2025hybrid`; `capitulo3.tex` (ll. 56-75, 164-176, 189, 200, 259) e
`introduccion.tex` (ll. 43, 46, 68, 75, 78).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 | traza | APLICADO | Verificado: `p1_compuerta.md`:31-38 da el MAE en hueso de la identidad sin autoencoder (`pub+asinh` y `LW20000` 0.00/0.00 HU, `pub` 21.80/0.14, n = 34) y `e6c_techo_lw.md`:21 lo da por precision (`pub+asinh` 0.00/0.01/0.13/2.07 HU). El texto ya no dice que ningun objetivo verifica el error: "La ida y vuelta ... se midio en los experimentos del Objetivo 1, fuera de la regla de su compuerta, y su resultado se presenta en el capitulo de resultados" (sin cifra, por la decision §2 capitulo3-r00: veredictos al cap. 4). GAP reformulado: `\GAPDEC{que codificacion multiventana y que precision numerica adopta el sintetizador, pendiente de su preinscripcion}`. Fila de MAPA anotada. `introduccion.tex`:46 y `capitulo3.tex`:172 no se tocan (fuera de alcance): ver pendientes |
| guia-1 | guia | APLICADO | Ultima columna = "Resultado reportado y su condicion", con la cifra principal que ya da el cuerpo y su condicion en las nueve filas (Chen: una de tres redes; Ramzan: mejor configuracion; Jacob: 300 imagenes; DiffBoost: por organo; Peters: fantoma; Karageorgos: simulados / cuatro TC con metal virtual; Liu: 14 casos; Zwingmann: por serie; Wang: ventana estrecha). Supuestos: la oracion de lectura de la tabla dice que las dos columnas centrales recogen lo que cada trabajo hace o supone sobre la colocacion y el exterior; la fila propia lleva en "Enfoque" el supuesto (generable en el dominio de imagen) y la convencion (ancho de $B_\delta$). No se anadio columna de supuestos ajenos: las fichas ("Restriccion o supuesto clave") dan como supuesto justo lo que ya esta en esas dos columnas, y otra columna obligaria a presentar en el cuerpo hechos nuevos (PAT-67). La tabla crece unas lineas; no pasa de pagina en la compilacion |
| guia-2 | guia | APLICADO | Herman en parrafo propio. Consecuencias: el dato es binario y ninguna fuente revisada da la distribucion ordinal para comparar las poses del segundo corredor bajo S1, que se reportan de forma descriptiva (`sec:poses`, `capitulo3.tex`:164); lectura propia marcada: la diferencia entre niveles es razon de que importe el nivel de la referencia clinica, asumido S1 en la serie navegada (`sec:amenazas`, `capitulo3.tex`:259). No se uso el resultado sobre dismorfismo: la propuesta lo dejaba opcional y el capitulo no trata el dismorfismo en otro lugar (evita PAT-80) |
| guia-3 | guia | APLICADO | Parrafo nuevo sobre densidad y apariencia del Obj 4. Arand et al. como motivacion del diseno (ficha: modelo medio de valores de gris por voxel, 50 TC post mortem de adultos sin lesion, valores bajos en el ala sacra; sin HU numericos ni calibracion, NO ENCONTRADO -> "el articulo no reporta"; no lo proponen como restriccion para colocar tornillos). Se replica el `\GAPDEC` de `introduccion.tex`:43 con el mismo texto; fila de MAPA existente anotada |
| guia-4 | guia | APLICADO | El parrafo de carencias del Obj 2 pasa antes de las medidas del Obj 4; la oracion de orden dice "Tras las carencias frente al Objetivo 2, cierra con las medidas de colocacion y de apariencia del Objetivo 4" |
| ES-01 | estilo | APLICADO | Dice de Jacob et al. tras la oracion del metodo; el parrafo cierra con la lectura propia |
| ES-02 | estilo | APLICADO | Parrafo partido; el del metaanalisis abre con su tesis ("La tasa agregada ... miden constructos distintos") |
| ES-03 | estilo | APLICADO | "Se asume que la sintesis, que no separa las contribuciones del paciente y del metal, no hereda esa dificultad de la reduccion; la comparacion prevista con el protocolo fisico es la que podria contradecir ese supuesto". Se fundio con la oracion de supuesto ya existente para no duplicarla y no pasar de 7 oraciones |

## Hallazgos bajos

Aplicados: guia-5 (Cassanego: tornillos de 3.0 a 3.5 mm, condilo humeral de seis miembros toracicos caninos
cadavericos; ficha pto 3 y M&M p. 2), guia-6 (Karageorgos en l. 92: RMSE 7.57 con la traza verdadera, 11.45 con
mascara de 1.4 veces el area y 54.82 con 0.7; caso de pelvis con dos marcadores de oro virtuales; ficha Tabla III
p. 16 y Apendice p. 15; sin unidad porque la ficha no la da; RMSE definida aqui, primera aparicion en el orden
del documento), guia-7 = ES-12 ("esquema multiventana" para la MAR; "marco" queda para Kaiser; "desde que punto
miden"), guia-8 ("y, segun el plazo, al protocolo fisico"), T02 ("la coleccion de la que proceden los datos de
este trabajo"), T03 (14 volumenes, 30 imagenes; ficha V-A-2 y V-C-3), ES-05, ES-06 (ficha Abstract p. 1),
ES-07, ES-08, ES-09, ES-10, ES-11, ES-13 (cada elemento abre por su objeto, BITACORA §2 introduccion-r05),
ES-14, ES-15.

No aplicado: ES-04. La ficha `ramzan2026claim` (filas 50 y 52, Tabla 2 p. 11) da 58.89 y 63.53 sin unidad;
anadir "%" seria completar la fuente (regla 1 de `overleaf/CLAUDE.md`).

## GAP tras la ronda

Lint: lit = 1, dato = 2, dec = 9 (antes 1/2/8). Abierto: un `\GAPDEC` replicado (fraccion por zona de densidad,
fila existente de MAPA). Reformulado: el `\GAPDEC` de ida y vuelta pasa a "que codificacion multiventana y que
precision numerica adopta el sintetizador". Ninguno cerrado. Sin `\GAPLIT` nuevos; el existente cambia "marco"
por "esquema" en su texto (MAPA anotado). `_candidatos.md` no cambia.

## Pendientes fuera de mi alcance

1. `introduccion.tex`:46 ("no lo verifica ningun objetivo" + `\GAPDEC{error de ida y vuelta ... sin autoencoder}`)
   y `capitulo3.tex`:172 (el `\GAPDEC` incluye "y su error de ida y vuelta sin autoencoder") deben alinearse con
   el cap. 2: el error esta medido (`p1_compuerta.md`:31-38, `e6c_techo_lw.md`:21); lo pendiente es la
   codificacion y la precision que adopta el sintetizador (T01, PAT-19).
2. Siguen de rondas anteriores: `introduccion.tex`:60 ("codificacion de la entrada" frente a entrada y salida);
   relecturas con `lector-papers` de `ramzan2026claim` Sec. 3.5, `herman2016` p. 8 (46/129 frente a 36.5 %) y
   `hu2023` Fig. 3.
3. `capitulo3.tex`:176 da el RMSE de Karageorgos en HU; la ficha no trae la unidad. Conviene verificarlo.

## Lint

`python scripts/lint_redaccion.py capitulo2 --compilar`: PASA, alta = 0, media = 0, baja = 0; compila, 89 paginas.

## Decisiones de redaccion

1. Un GAP replicado de otra seccion se coteja con `experiments/` antes de copiarlo; si el dato ya esta medido, se
   dice que se midio (sin cifra, si es veredicto del cap. 4) y el GAP nombra solo la decision pendiente.
2. El esquema de ventanas de la MAR = "esquema multiventana"; "marco" solo para el marco de referencia de Kaiser
   et al.; "codificacion multiventana" solo para la de este trabajo.
3. Tabla comparativa: la ultima columna es "Resultado reportado y su condicion", con cifras que ya da el cuerpo;
   la fila propia declara en "Enfoque" su supuesto y su convencion.
4. Cifra de una ficha sin unidad (RMSE de Karageorgos, Dice de Ramzan) se da sin unidad; no se completa.
