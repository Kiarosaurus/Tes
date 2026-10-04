# capitulo2 — r02 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo2.tex`. Se leyeron los cuatro reportes de la ronda
(lint, guia, estilo, trazabilidad). No se abrio ningun PDF. Fichas consultadas: `liu2025pipeline`,
`karageorgos2024ddpm`, `herman2016`, `kaiser2014dysmorphism`, `haneda2025aapm`, `wang2025adaptiveweighting`,
`chen2026foundationvae`, `ren2022metalinsertion`, `yun2026simulationdriven`, `li2024`; ademas `capitulo3.tex`
(ll. 34-45, 168-227), `introduccion.tex` (ll. 36-62) y `docs/04-implicancias.md` #8.

Solapes resueltos una sola vez: guia-1 = ES-01; guia-2 = T02 = ES-05 (PAT-66); guia-3 = ES-04 = T01;
guia-8 = T05.

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| ES-01 (= guia-1) | estilo / guia | APLICADO | Una sola formulacion en cuerpo, carencias y tabla. l. 54: casos de fracturas de la cresta iliaca, del pubis y del acetabulo (ficha, p. 14); "el articulo no menciona tornillos iliosacros" (ficha, Verificacion pto 4, NO ENCONTRADO -> decision §2 "el articulo no menciona"); "los autores declaran que el metodo todavia no se aplica a fracturas de sacro" (Discussion p. 18, "not yet applicable"). l. 68 y celda de la tabla, lo mismo en corto. Desaparece "no cubre el sacro" |
| guia-2 (= T02, ES-05) | guia / traza / estilo | APLICADO | El parrafo abre con el resumen fijado y ajustado: "al azar, con una regla geometrica sobre la anatomia o a mano" (ES-05, PAT-33). El cierre ya no dice que falte "una restriccion anatomica": reconoce que Karageorgos y Wang 2019 ligan la posicion a la anatomia y enuncia la carencia con la formulacion de l. 68: generar poses cuya distribucion se compare con una distribucion clinica medida. l. 68 y l. 116 usan el mismo resumen ajustado; la tercera carencia suma "y ninguno compara las posiciones resultantes con una distribucion clinica". No se afirma "una sola posicion por volumen" de Wang 2019 (T02): la ficha no lo dice |
| guia-3 (= ES-04, T01) | guia / estilo / traza | APLICADO | Parrafo reescrito. Abre por concesion: la mascara tubular de Wang et al. 2019 es un precedente cercano, que tampoco proviene de segmentar metal (ficha: mascara tubular por umbral de un mapa de distancias). Lo que separa al tornillo: el objeto que modela (tornillo de osteosintesis con su calibre, `sec:geometria`) y que su pose la propone el muestreador. `karageorgos2024ddpm` sale de la lista del umbral (T01: su metal es siempre virtual); el umbral queda para "cuando el metal es clinico" (Yun, Wang 2025, Li; fichas Sec. 2.4.2, V-A-2, IV-E). Ultima oracion con relacion de concesion: "El sintetizador, sin embargo, se entrena como esas fuentes, con mascaras umbralizadas..." |
| guia-4 | guia | APLICADO | l. 38: "al que se infiere que corresponde una de las dos carpetas locales de este trabajo (Seccion `sec:datos`)"; l. 74: "que corresponde por inferencia a una carpeta local de este trabajo (Seccion `sec:datos`)" (`capitulo3.tex`:42) |
| guia-5 | guia | APLICADO | Retirada la lectura "cota del rango de colocaciones". Se deja el hecho de la ficha (Resultados p. 7) y su consecuencia compatible con `sec:sap` (`capitulo3.tex`:196): las poses del muestreador que no atraviesan hueso, que SAP califica con grado 3, no tienen equivalente en esa serie |
| guia-6 | guia | APLICADO (parcial) | Salvedad anadida tras el tercer elemento, con el mismo `\GAPDEC` que `introduccion.tex`:46 (BITACORA §2, GAP replicados). "Entrada y salida" se mantiene en l. 76: la respalda `capitulo3.tex`:172 ("Las entradas y salidas usan la codificacion multiventana"). La discrepancia esta en `introduccion.tex`:60 ("codificacion de la entrada"); queda PENDIENTE para la autora, fuera de lo editable |
| ES-02 | estilo | APLICADO | "Esa posibilidad queda como supuesto, y la comparacion con el protocolo fisico que el diseno preve es la que podria contradecirlo" (`capitulo3.tex`:261) |
| ES-03 | estilo | APLICADO | "Mide PSNR, SSIM y error cuadratico, y el articulo no menciona sus unidades ni una evaluacion por region de hueso o de metal" (ficha, filas NO ENCONTRADO; decision §2) |
| ES-06 | estilo | APLICADO | Oracion tematica por las dos mitades del Obj 4: "las de colocacion, para tornillos reales o para un plan unico; las de apariencia, para puntuar la MAR". "Otra cosa" paso a "otro fin" por la lista negra del lint (E-INF) |
| ES-07 | estilo | APLICADO | "Esos autores toman la escala ... de Smith et al. Smith et al. la aplican en cuatro cadaveres, ..." |
| ES-08 | estilo | APLICADO | Oracion quitada de l. 26; l. 72 cita ahora `chen2024tumorsynthesis,hu2023,jin2021freetumor,wu2025freetumor` para "no pasan de 600 HU" (inventario del auditor, l. 26) |
| ES-09 | estilo | APLICADO | Haneda pasa a l. 36 como segunda oracion, con "dedicado a la MAR" para situar el desafio antes de l. 40 |
| ES-10 | estilo | APLICADO | Eliminada la ultima oracion de l. 24. l. 30 abre con oracion tematica que cubre sus dos funciones ("Ni la evaluacion ni el mecanismo de estos modelos cubren el artefacto metalico") y cierra con la negacion partida por familia (decision §2 introduccion-r05) |
| ES-11 | estilo | APLICADO (con otra consecuencia) | No se uso "los tornillos quedan por debajo de ese diametro": si el limite de 3.0 cm alcanza a los implantes es la opcion 2 de la implicancia #8, sin resolver (regla 3 de `overleaf/CLAUDE.md`), y la seccion 2D de un tornillo iliosacro no es su calibre. Consecuencia dicha: ni la validacion de Wu ni el limite de Haneda se establecieron con implantes de osteosintesis, asi que el simulador no aporta validacion propia para el objeto de este trabajo |
| ES-12 | estilo | APLICADO | "la banda $B_{\delta}$ para los efectos de adquisicion" (termino fijo abreviado como en l. 10 y l. 120; la forma larga llevaba la oracion a 41 palabras). Texto de la fila del `\GAPDEC` en MAPA alineado |
| ES-13 | estilo | APLICADO | "Esta seccion revisa como se decide donde va un objeto: la planificacion automatica ...; las series clinicas ...; la colocacion de mascaras de lesion, y la geometria del corredor. Cierra con las medidas de colocacion y de apariencia del Objetivo 4." Las necesidades de Obj 2 y 4 se reescriben sin "la primera / la segunda" |
| T01 | traza | APLICADO | Ver guia-3 |
| T02 | traza | APLICADO | Ver guia-2 |

## Hallazgos bajos

Aplicados: guia-7 ("en un subconjunto de pacientes y segun el plazo", como `introduccion.tex`:54), guia-8 = T05
(celda de Karageorgos: "SSIM frente a la imagen sin metal; metricas en cuatro TC clinicas con metal virtual";
SSIM de Wang 2025, 0.9501 y 0.9803, llevado al cuerpo, ficha V-B p. 2414), guia-9 en parte ("el segundo segmento
sacro" en lugar de "S2", que BITACORA §2 reserva), guia-10 (Kaiser "sobre 104 TC de pelvis no lesionadas"), T03
(metal disenado a mano e insertado de forma virtual en las cuatro TC clinicas), T04 (sin "no validado en metal";
"fundamento tecnico, y no un metodo que aqui se reimplemente y valide", `CLAUDE.md` raiz), ES-14, ES-15, ES-16,
ES-17 (modal "podria tener que revisarse", PAT-53), ES-18, ES-19, ES-20 (parentesis, igual que la introduccion),
ES-21, ES-22 (Radzi: referencia de la medida antes de las cifras; parrafo reordenado para no pasar de 7
oraciones), ES-23, ES-24, ES-25, ES-26 ("efectos del artefacto fuera del objeto que lo produce", que abarca a
Glover y Pelc), ES-27, ES-28 (con lectura propia marcada: "este trabajo lee esa diferencia como indicio de ...").

No aplicados: guia-9 en la sigla AAPM (la ficha `haneda2025aapm` no trae su expansion; "AAPM CT-MAR" es el
nombre publicado del desafio y expandirlo seria completar con conocimiento propio); T06 (acotar la sintesis de
Ramzan exige saber si la distribucion por segmento de la Sec. 3.5 es cuantitativa; sigue sugerida la relectura
con `lector-papers`, como en r01).

## GAP tras la ronda

Lint: lit = 1, dato = 2, dec = 8 (antes 1/2/7). Abierto: un `\GAPDEC` replicado de la introduccion y del
cap. 3 (error de ida y vuelta de la codificacion multiventana sin autoencoder), anotado en la fila existente de
`redaccion/MAPA.md`. Ninguno cerrado. Sin `\GAPLIT` nuevos: `_candidatos.md` no cambia.

## Pendientes fuera de mi alcance

1. `introduccion.tex`:60 dice "codificacion de la entrada"; cap. 2 (l. 76) y cap. 3 (l. 172) dicen entradas y
   salidas. Alinear la introduccion (guia-6).
2. Relecturas con `lector-papers`: `ramzan2026claim` Sec. 3.5 (T06), `herman2016` p. 8 (46/129 frente a 36.5 %)
   y `hu2023` Fig. 3, que siguen de r01.
3. Si el limite de 3.0 cm de Haneda alcanza a los implantes que colocara el protocolo fisico adaptado sigue
   abierto en la implicancia #8 (opcion 2); el capitulo no lo afirma en ningun sentido.

## Lint

`python scripts/lint_redaccion.py capitulo2 --compilar`: PASA, alta = 0, media = 0, baja = 0; compila, 88 paginas.

## Decisiones de redaccion

1. El resumen de como colocan el metal la simulacion y la MAR pasa a "al azar, con una regla geometrica sobre la
   anatomia o a mano" (sustituye a la decision de capitulo2-r01); la carencia que queda es siempre "generar poses
   cuya distribucion se compare con una distribucion clinica medida", con la misma formula en cuerpo y sintesis.
2. Limitacion de una solucion concreta: se da la de su ficha mas pertinente al objetivo (Liu et al.: "el articulo
   no menciona tornillos iliosacros" y "no se aplica a fracturas de sacro"), no una derivada ("no cubre el sacro").
3. Una lectura propia de un dato ajeno no puede asignar al metodo un uso que el cap. 3 no tiene; si no hay uso, se
   dice la consecuencia comparando con lo que el cap. 3 si hace (Herman frente al grado 3 de las poses fuera del
   hueso).
4. CLINIC-metal se nombra siempre con la salvedad de que la carpeta local le corresponde por inferencia
   (Seccion `sec:datos`), nunca como "el mismo que usa este trabajo".
5. S2 como nivel sacro (Herman) se escribe "segundo segmento sacro", sin la sigla, para no chocar con la reserva
   del segundo corredor.
6. Siglas de organizaciones sin expansion en la ficha (AAPM) se dejan dentro del nombre publicado, sin expandir.
