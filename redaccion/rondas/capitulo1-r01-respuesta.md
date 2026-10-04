# capitulo1 — r01 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo1.tex`. Reportes leidos: `capitulo1-r01-lint.md`
(PASA, 0/0/0), `-guia.md` (0 altos, 10 medios, 3 bajos), `-estilo.md` (0/17/10), `-trazabilidad.md` (1/9/5).
Lint final `python scripts/lint_redaccion.py capitulo1 --compilar`: **PASA**, alta 0 / media 0 / baja 0;
compila, 105 paginas. GAP del capitulo: lit 4 / dato 1 / dec 7 (antes 3/0/4).

Conteo (altos y medios, 37): **35 aplicados, 0 rechazados, 2 escalados** (guia-2/T05 comparten el
escalado del tipo de tornillo; guia-1 queda aplicado con `\GAPLIT`, y la figura anatomica, en el mismo GAP).
Sin cambio de titulos: S02 propone quitar "Marco" del titulo de §1.5; queda para la autora (ver al final).

## Altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 (alta) | trazabilidad | APLICADO | "solo para cribar" -> "umbral con que este trabajo criba la cohorte y delimita el metal real (Secciones datos y sintetizador)". Fuente: DEC 2026-09-20 (2) D1 (mascara `M` a 2500 HU); cap. 3 l.73, 87, 178 |
| guia-1 | guia | APLICADO (con GAP) | Ninguna ficha ni el glosario definen cortical, platillo, foramen, tabla externa ni articulacion sacroiliaca. Se glosa el ala sacra con `routt1997` ("slopes laterally and caudally from the upper sacral vertebral body", p. 206) y se abre `\GAPLIT` de fuente anatomica que defina e ilustre los seis terminos, en la primera aparicion de "cortical" (l.68). La figura anatomica queda dentro del mismo GAP: no hay imagen en el repositorio y no se inventa |
| guia-2 | guia | ESCALADO | No esta decidido que tipo de corredor mide el cap. 3 (glosario: no intercambiables; cap. 3 l.196: "entra y sale por la cortical del ilion"; TM: *transsacral*). Se enuncia la tension como hecho y se pone `\GAPDEC` (decision BITACORA introduccion-r03). Ver pregunta 1 |
| guia-3 | guia | APLICADO (con GAP) | Se da lo que consta: rango $[-1000, 20\,000]$ HU (cap. 3 l.69, TM:77) y que no es lineal a diferencia de la Ec. `eq:ventana`. Forma y parametros solo estan en `src/common/ventanas.py`, que no es fuente de contenido: `\GAPDATO` |
| guia-4 | guia | APLICADO | "MAE" -> "error absoluto medio" en l.44, l.104 y l.122 (decision BITACORA 2026-10-03: siglas definidas despues no se usan en el marco teorico) |
| guia-5 | guia | APLICADO | Equivalencia sobre "el intervalo de confianza del 90 % de la diferencia pareada", que "cae entero" en el margen (cap. 3 l.225). Mismo cambio que T09 |
| guia-6 | guia | APLICADO | Obj 1 y Obj 3 separados; en el Obj 3 se replica el `\GAPDEC` del cap. 3 l.223 con el mismo texto (decision BITACORA introduccion-r02). Mismo cambio que T08 |
| guia-7 | guia | APLICADO | "usa" -> "preve usar la simulacion fisica como comparacion" (decision BITACORA introduccion-r04). Mismo cambio que T04 |
| guia-8 | guia | APLICADO | La oracion de orden describe el orden real (fisica de la imagen, cirugia, modelo generativo, estadistica) y su razon: el artefacto se explica con los conceptos de la TC y el 2.5D con los del artefacto (l.108 usa Glover y Pelc). Ya no se atribuye al recorrido de la cadena. Mismo cambio que S01 |
| guia-9 | guia | APLICADO | Oracion nueva en l.44: el sintetizador usa la codificacion multiventana como canales de entrada y salida, sin autoencoder (cap. 3 l.172), con el `\GAPDEC` del cap. 2 l.86 ("que codificacion multiventana y que precision numerica adopta"), que ya esta cotejado con `experiments/` (BITACORA capitulo2-r03, PAT-19); no se copia el GAP del cap. 3, que aun da la ida y vuelta como no medida |
| guia-10 | guia | APLICADO | Se mantiene "brecha cortical" para la perforacion de Smith et al. y se agrega: "En este trabajo, el grado se calcula a partir de la protrusion del implante fuera de una envolvente osea segmentada, que aproxima esa perforacion" (cap. 3 l.194, l.257) |
| S01 | estilo | APLICADO | Ver guia-8 |
| S02 | estilo | APLICADO (parcial) | l.13 "marco estadistico" -> "analisis estadistico"; l.112 "pide un marco distinto" -> "se analiza de forma distinta". El titulo de §1.5 viene del esqueleto y no se cambia: lo decide la autora (ver al final) |
| S03 | estilo | APLICADO | "sus referencias anatomicas" -> "el platillo de S1, las crestas y las espinas iliacas" |
| S04 | estilo | APLICADO | "De ahi la distincion..." -> "Este documento distingue dos dominios: ..." |
| S06 | estilo | APLICADO | Se elimina la caracterizacion repetida de Park et al. en §1.2; la oracion abre "Park et al. separan dos efectos del endurecimiento" |
| S07 | estilo | APLICADO | Se elimina la ultima oracion de l.50; en l.54: "De Man et al. no nombran la inanicion de fotones; describen como artefacto de ruido ..." (ficha `deman1999`, Respuestas 1) |
| S09 | estilo | APLICADO | "Ninguna de las dos fuentes reune metal y volumen parcial axial: Glover y Pelc lo estudian sin metal, y De Man et al. lo dejan fuera al simular en dos dimensiones" |
| S11 | estilo | APLICADO (reformulado) | La propuesta del revisor ("este trabajo no traslada a un tipo las medidas del otro") afirmaria algo que el cap. 3 no cumple con seguridad. Se escribe la convencion del glosario como del trabajo ("trata como no intercambiables"), con las dos fuentes concretas (McLaren transiliosacro; Kaiser eligen 10 mm "for passage of an iliosacral screw", p. e120(2)), y la tension con el cap. 3 queda en `\GAPDEC` (guia-2) |
| S14 | estilo | APLICADO | "Smith et al. graduan esa perforacion, que en este documento se llama brecha cortical, en cuatro niveles" |
| S17 | estilo | APLICADO | El intervalo $(0,1)$ pasa a Zhang et al. con su `\cite{zhang2025diffboost}` (homonimo de ControlNet: decision BITACORA capitulo2-r00). Mismo cambio que T07 |
| S18 | estilo | APLICADO | La oracion de ControlNet sale de l.102 y cierra l.104, despues de presentar la difusion latente; "cayo" -> "quedo descartado con ella" |
| S19 | estilo | APLICADO | "Este trabajo lee como una aplicacion de ese tipo conservar los HU ... (Seccion obj1)"; "como condicion para adoptar la difusion latente, que el veredicto negativo descarto". Cubre T14 |
| S21 | estilo | APLICADO | "En las fuentes revisadas, el *inpainting* con un modelo de difusion sigue una de dos formas" |
| S22 | estilo | APLICADO | "No se ha fijado si su procedimiento de muestreo toma algo del de Lugmayr et al." + mismo `\GAPDEC` |
| S23 | estilo | APLICADO | Consecuencia explicita: "de modo que ninguna de las dos distribuciones tiene al paciente como unidad" |
| S25 | estilo | APLICADO | Parrafo partido: intervalo por remuestreo (2 oraciones) y proteccion contra el ajuste (multiplicidad + lo fijado + decisiones post hoc, T10) |
| S27 | estilo | APLICADO | "Dos errores por voxel aparecen en el documento y no son intercambiables: el error absoluto medio y la raiz del error cuadratico medio" |
| T02 | trazabilidad | APLICADO | Abadi et al. "en el simulador DukeSim" y Wang et al. "en su simulacion de implantes cocleares"; "energia por energia" -> "Wang et al. la discretizan en cinco energias" (ficha `wang2019cochlear`) |
| T03 | trazabilidad | APLICADO | "lo que este trabajo mide, y lo que genera el sintetizador, ocurre en el dominio de imagen. Solo el protocolo fisico de comparacion, previsto en la Seccion apariencia, pasa por proyecciones simuladas" |
| T04 | trazabilidad | APLICADO | Ver guia-7 |
| T05 | trazabilidad | APLICADO + ESCALADO | Definicion con `smith2006iliosacral` ("through the ileum into either the S1 or S2 vertebrae", M&M p. 235), redactada sin la sigla S2 (decision BITACORA capitulo2-r02); Kaiser deja de citarse para la definicion. Lo que queda abierto es guia-2 |
| T06 | trazabilidad | APLICADO | "esa guia" -> "la guia fluoroscopica, que llaman convencional" |
| T07 | trazabilidad | APLICADO | Ver S17 |
| T08 | trazabilidad | APLICADO | Ver guia-6 |
| T09 | trazabilidad | APLICADO | Ver guia-5 |
| T10 | trazabilidad | APLICADO | "En ambos casos hubo, sin embargo, decisiones posteriores a ver datos: esa regla se fijo conociendo un resultado exploratorio desfavorable que incluia a los pacientes de prueba, y tres decisiones del Objetivo 2 se tomaron despues de ver datos (Seccion amenazas)" (cap. 3 l.58, l.253) |

## Bajos

| Hallazgo | Decision | Detalle |
|---|---|---|
| guia-11 | APLICADO (minimo) | La remision al cap. 3 nombra las mascaras de TotalSegmentator con `\cite{wasserthal2023}`; no se agrega parrafo nuevo |
| guia-12 | NO APLICADO | Unificar $N$/$\mathcal{N}$ exige editar `capitulo3.tex` (fuera de la lista editable). Para la ronda del cap. 3 |
| guia-13 | APLICADO (parcial) | Se nombran codificador y decodificador; "variacional" no se agrega porque la ficha `rombach2022latentdiffusion` solo lo sugiere en el resumen del lector (KL), sin evidencia textual |
| S05, S08, S10, S12, S13, S15, S16, S20, S24, S26 | APLICADOS | S10 tambien en la fila 2 de la Figura 1.1 |
| T11, T12, T13, T14, T15 | APLICADOS | T12 con la condicion "a lo largo del eje del corredor" y "a 150 HU o menos" |

## GAP por tipo

- `\GAPLIT` (4; 1 nuevo): fuente de anatomia de la pelvis (guia-1). Candidato PENDIENTE en `docs/literatura/_candidatos.md` (ronda 2026-10-03).
- `\GAPDATO` (1; nuevo): forma y parametros de la compresion arcoseno hiperbolico (guia-3).
- `\GAPDEC` (7; 3 nuevos en el capitulo): tipo de tornillo del corredor medido (nuevo en el documento, guia-2/T05); codificacion y precision del sintetizador (replicado del cap. 2, guia-9); agregacion por paciente en el Obj 3 (replicado del cap. 3, guia-6/T08).
- Cerrados: ninguno. Todo anotado en `redaccion/MAPA.md`.

## Escalados a la autora

1. **Tipo de tornillo del corredor (guia-2, T05).** El marco define iliosacro (termina en el sacro) y
   transiliosacro (cruza ambas articulaciones) como no intercambiables, segun el glosario. El cap. 3 (l.196)
   dice que "un tornillo iliosacro entra y sale por la cortical del ilion por diseño", usa la longitud del
   corredor del caso, y `tesis/main.tex` llama *transsacral* al diametro. ¿A que tipo corresponde el
   corredor que mide este trabajo, y le aplican el corredor de 10 mm y la holgura radial de Kaiser et al.
   (definidos para el iliosacro)? La respuesta probablemente obliga a corregir tambien el cap. 3 y merece
   entrada en `docs/04-implicancias.md` (no la registro: fuera de mi lista editable).
2. **Titulo de §1.5 (S02, sin GAP en el texto).** "Marco estadistico de la evaluacion" usa "marco",
   reservado para el de Kaiser et al. (BITACORA capitulo2-r03). Propuesta: "Analisis estadistico de la
   evaluacion". El titulo viene del esqueleto; no lo cambio sin su visto bueno.

## Decisiones de redaccion

| Decision | Motivo |
|---|---|
| Termino anatomico sin definicion en ninguna ficha: se glosa lo que una ficha describe (ala sacra con `routt1997`) y un solo `\GAPLIT` agrupa los demas en su primera aparicion | G-B1; evita definir con conocimiento propio |
| Brecha cortical en el marco teorico: nombre para la perforacion de Smith et al. + una oracion que dice que este trabajo la calcula como protrusion fuera de la envolvente osea (misma formula en todo capitulo que la defina) | PAT-14; une la definicion de la introduccion con la del cap. 3 |
| Cuando un GAP del cap. 3 contradice uno posterior del cap. 2 ya cotejado con `experiments/`, se replica el del cap. 2 | PAT-19; caso de la ida y vuelta sin autoencoder |
| Equivalencia (TOST) siempre enunciada sobre el intervalo de confianza del 90 % que "cae entero" en el margen, nunca sobre la diferencia | T09, guia-5 |
| Resumen de lo fijado antes de ver datos: siempre seguido de las decisiones posteriores que enumera `sec:amenazas` | T10, PAT-31 |
| La difusion latente y ControlNet se presentan como teoria y se cierran con "que el veredicto negativo descarto" / "quedo descartado con ella", con `\ref`; sin "cayo" ni "ruta latente" | S18, PAT-34, PAT-89 |
