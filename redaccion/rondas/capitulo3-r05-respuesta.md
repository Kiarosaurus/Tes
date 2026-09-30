# Respuesta del redactor — capitulo3 — r05 (ultima ronda)

Insumos: `capitulo3-r05-lint.md` (PASA, 0/0/4), `-guia.md`, `-estilo.md`, `-traza.md`. Ningun hallazgo se saco por
oscilacion. Siglas de fuente: las de `capitulo3-r05-traza.md` (TM, PRE, DAT, DEC, IMP, RES, E12, E13, ZW), mas
DSA = `experiments/objetivo3/diseno_A.md` (borrador, NO preinscrito).
Lint final: PASA, alta 0 / media 0 / baja 4 (E-P1 en l.71, 180, 198, 255; ver abajo). GAP: lit 0 / dato 10 / dec 22
(+5 dec, todos de esta ronda).

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 (envolvente "con relleno de cavidades cerradas", l.87 y l.255) | traza | APLICADO + ESCALADO | Verificado: DEC D-O2.3 pto 1 (:1450-1451) fija cierre de 2 mm y relleno 3D; `e9ts_corredor.py`:41-45 y :307 y `e12_sap_control.py`:94, :112 (importado por E13) solo hacen `binary_closing`; `binary_fill_holes` solo esta en `e9_corredor.py`:99 (version por HU). l.87 describe lo corrido: "con un cierre morfologico de 2 mm `\GAPDEC{la decision que define la envolvente fija ademas un relleno de cavidades cerradas que el codigo del corredor y de SAP no aplica}`". l.255: "El cierre morfologico de la envolvente ... podria ocupar el canal sacro o los foramenes". Fila de MAPA ajustada y fila nueva. Va a #127 |
| guia-1 ("prueba y reprueba" con dos sentidos, l.54 vs l.223) | guia | APLICADO + ESCALADO | l.54 pasa a "par de reproducibilidad", el nombre de l.48; "prueba y reprueba" desaparece del capitulo. l.223: "la de corridas repetidas del protocolo fisico sobre ese caso `\GAPDEC{que cambia entre dos corridas repetidas del protocolo fisico}`". DEC D4 pto 4 (:1274-1276) solo dice "test-retest del brazo fisico", sin decir que varia. "Ambas se miden solo en los casos de validacion ..., de modo que el protocolo fisico tambien se corre sobre ellos": DEC :1275-1276 y :1400 miden las dos componentes de `Delta` solo en validacion, lo que exige correr el brazo fisico ahi |
| guia-2 (regiones de *streak amplitude* respecto de $B_{\delta}$; truncamiento ausente de constructo) | guia | APLICADO + ESCALADO | l.213: "Si esas regiones caen fuera de $B_{\delta}$, el sintetizador da alli amplitud nula por construccion, de modo que su ubicacion condiciona la comparacion `\GAPDEC{ubicacion de las regiones de medicion de rayas respecto de B_delta; el borrador del diseno mide las metricas dentro de G, sin preinscribirlo}`". Fuente: DSA:115 (E-A1, "dentro de `G`"); la copia fuera de $G$, l.172. Constructo (l.257): "La banda trunca a proposito las rayas lejanas ..., y el protocolo fisico, que simula y reconstruye el volumen entero, no las trunca. La comparacion entre ambos no puede mostrar ... si el sintetizador reproduciria las rayas mas alla de la banda". Fuente: DSA:19 ("truncado por diseno, #57"); TM:119 (control sin metal por cambios del brazo fisico). No se escribe que el protocolo fisico "genera rayas en todo el volumen": ninguna fuente lo dice asi |
| guia-3 (dos evaluaciones sin metrica, l.182 y l.215) | guia | APLICADO + ESCALADO | l.182: se retira "El primero y el tercero se cuantifican": solo el tercero tiene cifra (DEC R3, 0.62 frente a 1.40); DEC R3 declara el primero (#95) como limitacion, sin metrica. Texto: "El tercero queda asi cuantificado; para el primero y el segundo falta la metrica `\GAPDEC{...; el borrador del diseno propone medir el salto de HU en ese borde, sin preinscribirlo}`" (DSA:116, "costura en el borde de `B_delta`"). l.215: la frase se conserva (TM:127) con `\GAPDEC{metrica y analisis de la comparacion con observaciones reales de artefacto; el borrador ... propone sintetizar de nuevo implantes reales de la particion de prueba y compararlos con su TC, sin preinscribirlo}` (DSA:115, E-A1). No se anaden filas a la Tabla `tab:diseno`: seria dar por decidido un borrador |
| S01 (tres nombres para el dominio de imagen) | estilo | APLICADO | Solo "dominio de imagen" (l.67, l.174). Sentido fijado en l.172: "es decir, sobre valores de TC por voxel, sin espacio latente ni datos de proyeccion". Cubre las dos oposiciones (latente en l.20/l.174; sinograma en l.176/l.257) |
| S02 ("Todas las cifras del Objetivo 2", l.91) | estilo | APLICADO | "Las cifras principales del Objetivo 2 usan el recorte por defecto, y la decision que lo fijo quedo condicionada a una revision pendiente `\GAPDATO{...}`"; el GAP pierde la clausula que ahora dice el texto. Fuente: DEC 2026-09-14 (4) |
| S03 ("el eje optimo", l.209) | estilo | APLICADO | "el propio eje del corredor ya perfora" |
| S04 ("el mismo defecto que tendria tomarlo de la referencia clinica", l.158) | estilo | APLICADO | Decidido con PRE §3.2: *"ponerlo a ojo seria el mismo defecto que calibrar contra el benchmark"*. La fuente si equipara las dos cosas, pero no dice cual es el defecto comun; la version de r03 lo nombraba ("un parametro sin dato"), y ese defecto no es el de calibrar contra la referencia (circularidad). Restituir la equiparacion obligaria a interpretar el defecto comun, que PRE no da. Se elimina la clausula; queda "Fijarla a juicio anadiria un parametro sin dato que lo sostenga" |
| S05 (termino de comparacion y efecto, l.251) | estilo | APLICADO (parcial) | Se corrige el termino de comparacion: "pierde asi, en proporcion, mas pacientes del grupo 2 que del grupo 3, y su composicion por grupos deja de ser la de los 91 pacientes con S1 localizado". No se escriben 32 % y 12 %: serian cifras recalculadas (regla dura 5 de `overleaf/CLAUDE.md`); DEC 2026-09-14 (3) solo da 11 de 34 y 7 de 57. Efecto: ver guia-4 |
| S06 (tautologia "por esa misma razon", l.217) | estilo | APLICADO | "Por eso, la prueba de superioridad ... compara el sintetizador con una linea base sin rayas y, por si sola, no dice si las rayas generadas se parecen a las reales `\GAPDEC{...}`" |
| S07 (PAT-5, l.91) | estilo | APLICADO (parcial) | "La diferencia entre recortes es incertidumbre de la medicion, no variabilidad anatomica." No se escribe "difiere en 2": 47/45 y 17/15 serian conteos recalculados desde porcentajes; solo 29/27 esta en DEC (:770-771) |
| S08 (PAT-6, "Respalda", l.176) | estilo | APLICADO | "Este trabajo lo lee como apoyo a generar mas alla de la mascara del implante, pero no como valor para el ancho de 12 mm" (decision de BITACORA §2) |

## Hallazgos de severidad baja

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-4 (perdida del grupo 2 sin efecto) | guia | APLICADO | "Si el corredor difiriera entre grupos, la distribucion de grados heredaria esa composicion; la cohorte de sensibilidad, que solo reune pacientes sin objeto, no esta expuesta a ese desequilibrio." Condicional; cohorte de sensibilidad = 49 del grupo 3 (l.52) |
| T02 ("cuyo criterio de evaluacion", l.255) | traza | APLICADO | "... pero no en la de la navegada. La definicion de posicion ideal del estudio se refiere al platillo sacro correspondiente y a los foramenes de S1." (ZW:72, :177-178) |
| T03 (mas de un tornillo por paciente, l.207) | traza | APLICADO | "Los grados se cuentan por tornillo. Los recuentos implican que algunos pacientes recibieron mas de uno, aunque el articulo declara un solo tornillo por paciente." (ZW:85, :303-304; DEC :986) |
| S09 | estilo | APLICADO | "que describen Arand et al. en su modelo estadistico poblacional"; se quita "sistematica" |
| S10 | estilo | APLICADO | "valores de TC" en todo el capitulo (l.67, l.174, l.182) |
| S11 | estilo | APLICADO | Se elimina de l.71; queda en l.38 y l.253 |
| S12 ("unos 12 mm", l.176) | estilo | RECHAZADO | Para el sintetizador la fuente da un valor aproximado: TM:79 "~12mm" y DSA:25 "banda de ~12 mm". Los 12 mm exactos de l.73 son el parametro del codigo de la compuerta (`p1_decodificador_sd15.py`:72), otra medicion |
| S13 | estilo | APLICADO | "uno de entrenamiento, uno de validacion con 8 casos y uno de prueba con 34 pacientes" |
| S14 | estilo | APLICADO | "que la mascara de S1 toque el borde ..." (ademas se parte la oracion por E-O1) |
| S15 | estilo | APLICADO | "fue 0.42. Una definicion de hueso por HU dejaria fuera, en la mediana, esa fraccion del corredor." (dos oraciones: con los dos puntos el lint marcaba E-O1) |
| S16 | estilo | APLICADO | "Las dos fuentes de fabricante [synthes, doublemedical] son documentacion tecnica no revisada por pares", tras la primera cita de fabricante del parrafo |
| S17 | estilo | APLICADO | "Entre entrenamiento y sintesis hay tres desplazamientos de dominio." |
| S18 | estilo | APLICADO | "sin la etapa de compresion del autoencoder. La codificacion elegida entre las tres de la compuerta, ... constan en un diseno que todavia no se congelo" |
| S19 | estilo | APLICADO | "no reportan haber excluido pacientes de corredor estrecho, de modo que una cohorte restringida dejaria de ser comparable con la suya" |
| S20 | estilo | APLICADO | Parrafo nuevo en "La comparabilidad con el protocolo fisico..." |
| S21 | estilo | APLICADO | Parrafo nuevo en "La referencia clinica no dice..."; se quita "ademas" |
| S22 | estilo | APLICADO | "; como el veredicto fue negativo, esa multiplicidad no lo compromete" (l.38) |
| S23 | estilo | APLICADO | "Esta ultima se excluye por dos condiciones de los datos." |
| lint E-P1 x4 (l.71, 180, 198, 255) | lint | SIN CAMBIO | Cifras de conteo y criterio del propio diseno (34 pacientes, 25 HU, tres reglas, seis controles, seis combinaciones), con fuente en respuestas anteriores. La de l.71 aparece porque S11 quito el `\ref` de esa linea; la de l.182 desaparece porque ahora lleva GAP |

Arreglos minimos no pedidos: cinco oraciones que al aplicar S05, S15, guia-1 y guia-2 pasaron de 40 palabras (E-O1)
se partieron en dos, sin cambiar contenido. Comentario de cabecera del .tex actualizado a r05.

## Escalados y preguntas para la autora (van a #127)

1. **T01 (envolvente):** la decision D-O2.3 fija cierre de 2 mm **y relleno de cavidades cerradas en 3D**, pero el codigo
   que midio el corredor (E9-TS) y el que corrio SAP (E12/E13) solo aplica el cierre. ¿Se corrige la decision para que
   diga lo que se corrio, o se vuelve a correr con relleno (y cambian el diametro del corredor y los grados)?
2. **guia-1:** en el margen `Delta`, ¿que cambia entre dos corridas del "test-retest del brazo fisico" (semilla de ruido,
   corrida completa, otra cosa)?
3. **guia-2:** ¿donde se ubican las regiones de medicion de *streak amplitude*: dentro de $B_{\delta}$ (como supone el
   borrador de `diseno_A.md`) o donde las fije el protocolo de Peters? Fuera de la banda el sintetizador da amplitud nula.
4. **guia-3:** ¿con que metrica y analisis se evaluan (a) la diferencia mascara umbralizada / cilindro liso, (b) la
   continuidad en el borde de $B_{\delta}$ (el borrador propone el salto de HU) y (c) el realismo contra observaciones
   reales (el borrador propone E-A1)? ¿Entran como filas descriptivas de la Tabla de diseno?
5. Siguen abiertos de r04: valor de 8 mm de la exclusion de extremos; doble papel de la viabilidad (guia-5 r04).

## Decisiones de redaccion

- "Dominio de imagen" es el unico nombre para operar sobre valores de TC por voxel, sin espacio latente ni datos de
  proyeccion; se opone tanto al latente como al sinograma. No se usan "espacio de imagen" ni "espacio de pixeles".
- *CT numbers* = "valores de TC" en todo el documento; no "numeros de TC".
- El paciente adquirido dos veces con el mismo implante es el "par de reproducibilidad". La repeticion de corridas del
  protocolo fisico se llama "corridas repetidas del protocolo fisico"; "prueba y reprueba" no se usa.
- Cuando decision y codigo difieren, el metodo describe lo que se corrio y la decision no aplicada va en `\GAPDEC`
  (OC-5, PAT-20).
- Un porcentaje o conteo que no esta escrito en la fuente no se deriva de otros (p. ej., 11 de 34 no se convierte en
  32 %); se dan los conteos de la fuente.
- Una evaluacion que solo consta en el borrador `diseno_A.md` se nombra con `\GAPDEC` que dice lo que propone el
  borrador y que no esta preinscrito; no entra en la Tabla de diseno.
