# Respuesta del redactor — capitulo3 — r04

Insumos: `capitulo3-r04-lint.md` (PASA, 0/0/4), `-guia.md`, `-estilo.md`, `-traza.md`. Ningun hallazgo se saco por
oscilacion. Siglas de fuente: las de `capitulo3-r04-traza.md` (TM, PRE, DAT, DEC, IMP, RES, E12, R1, SYN).
Lint final: PASA, alta 0 / media 0 / baja 4 (las cuatro E-P1 de siempre, ver abajo). GAP: lit 0 / dato 10 / dec 17.

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 (Synthes "declara que nucleo y fuste tienen el mismo diametro", l.119) | traza | APLICADO | Re-apertura aceptada. SYN:120 registra el nucleo como NO ENCONTRADO (solo cualitativo) y SYN:182 lee la frase *"The core and shaft diameters are the same."* como comparacion entre los calibres 6.5 y 7.3, justo despues de *"the thread and head diameters of the 6.5 mm ... are smaller"* (p. impresa 5). Texto: "el fuste de 4.8 mm que imprime la guia tecnica del fabricante, el mismo para los tornillos de 6.5 y 7.3 mm". Fuente: SYN:70 ("Fuste 4.8 mm (ambos calibres)"). PAT-6 reincidia |
| T02 ("su razon es clinica y no numerica" justifica el valor de 8 mm, l.194) | traza | ESCALADO | Se retira la clausula (tambien S18). DEC D-O2.3 pto 4 (:1457-1460) justifica excluir los extremos, no el valor; `e9_corredor.py:77` solo fija `RECORTE_EXTREMO_MM = 8.0`. Se anade `\GAPDEC{justificacion del valor de 8 mm de la exclusion de extremos, que no consta en el repositorio}`. No se escribe "no tiene fuente publicada": seria un negativo sobre la literatura que nadie verifico |
| guia-1 ("pacientes de validacion" sin definir, l.221 vs l.50) | guia | APLICADO | l.50: la particion "separa tres conjuntos: entrenamiento, validacion, con 8 casos, y prueba, con 34 pacientes". Fuente: DEC 2026-09-21 (2) (:1384, `val` tiene 8 casos; misma particion `p1_particion.csv`, semilla 20260917, DEC :1052, :1378). l.221 remite a la Seccion de datos y dice que tras el criterio de inclusion quedan 3 pacientes con implante real (DEC :1394). Como `val` y `test` son conjuntos distintos de la misma particion por paciente, el margen no se mide sobre la prueba; no se anade mas porque ninguna fuente dice si el Obj 1 uso `val` |
| S04 (mismo punto) | estilo | APLICADO | Ver guia-1. Se usa "casos de validacion" para el conjunto (DEC dice "casos") y "pacientes" para los 3 con implante (DEC :1399 dice "3 pacientes") |
| guia-2 (canal sacro y foramenes dentro de la envolvente) | guia | APLICADO (con GAP) | Ninguna fuente verifica que el cierre de 2 mm y el relleno de cavidades dejen fuera canal y foramenes: `e9ts_revision_laminas.md:41` lo pone como algo a mirar, en una revision todavia pendiente (#123). Validez de constructo: "El cierre morfologico y el relleno de cavidades de la envolvente podrian ocupar el canal sacro o los foramenes, y en ese caso una perforacion hacia ellos daria brecha nula" + `\GAPDATO{comprobacion de que la envolvente osea deja fuera el canal sacro y los foramenes sacros}`. No se afirma que la referencia clinica cuente esas perforaciones: la ficha de Zwingmann (:286) registra la direccion de la perforacion como NO ENCONTRADO |
| guia-3 (S1 en la serie navegada, supuesto sin justificar ni en amenazas) | guia | APLICADO | No se escala: la decision existe. DEC 2026-09-17 C, fila #69: "(a)+(c): S1 explicito solo en el brazo convencional; en el navegado se declara supuesto". Rige DEC sobre el estado ABIERTA de #69 en IMP (regla 3 de `overleaf/CLAUDE.md`). l.198: "en S1, nivel que la serie convencional declara y que en la navegada se asume (Seccion de amenazas)". Validez de constructo: la serie convencional nombra S1 en la tecnica (*"into the S1 vertebra"*, p. 1835); la navegada no, y su criterio de evaluacion habla del *"respective sacral end plate and the S1 neuroforamina"* (ficha :301). "Este trabajo asume S1 tambien para la serie navegada, y la publicacion no permite verificarlo". Se quita la frase de l.205 para no repetir el argumento (PAT-26) |
| S01 ("convierte la comparacion en una validacion", l.127) | estilo | APLICADO | "impide que la comparacion sea un ajuste". DEC :1414 usa "validacion", pero el Obj 2 no tiene regla de decision (l.205), y la redaccion propuesta mantiene el argumento sin subir la certeza |
| S02 (0.083 mm generalizado a SAP, l.253) | estilo | APLICADO | "su resolucion, medida en el fantoma, es de 0.083 mm". Fuente: E12:96 |
| S03 ("fantasma" / "fantoma") | estilo | APLICADO | "Fantoma" en todo el capitulo (l.196; la mencion de l.183 desaparecio con S17). Va a decisiones de redaccion |
| S05 (parrafo cajon, l.196) | estilo | APLICADO | "La envolvente es una mascara de hueso..." pasa tras la definicion de $s$; la escala angular de Smith et al., con su `\GAPDEC`, pasa tras la escala de cuatro grados (l.187). El parrafo queda para los controles y abre con "Seis controles verificaron la implementacion..." |

## Hallazgos de severidad baja

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-4 | guia | APLICADO | l.87: "excluidos 8 mm en cada extremo (Seccion SAP)"; l.194 remite a l.87 |
| guia-5 | guia | NO APLICADO | Hay que elegir si la viabilidad es caracterizacion de cohorte o variable dependiente del Obj 2, y eso le toca a la autora (lo dice el propio revisor). Ya hay un `\GAPDEC` sobre el calibre de viabilidad de SAP (l.187). Pregunta abajo |
| guia-6 | guia | APLICADO | "Recorte" queda solo para TotalSegmentator. Extremos: "exclusion de extremos" (l.194). Intensidades: "saturar/saturacion" (l.71, l.75, l.251), el mismo sentido que "canal ... no saturado" de l.60 |
| guia-7 | guia | APLICADO | l.73: $B_{\delta}$ son los voxeles a 12 mm o menos, en distancia euclidea 3D, del metal real (umbral de 2500 HU), sin contar el metal. Fuente: `experiments/objetivo1/p1_decodificador_sd15.py`:34, :72 (`BDELTA_MM = 12.0`), :351 |
| T03 | traza | APLICADO | "mide 8.0 mm de diametro y 4.5 mm de altura. El diametro lo reportan Sayres et al. y lo imprime tambien el catalogo de otro fabricante; la altura, entre las fuentes revisadas, solo la dan Sayres et al. Que la cabeza quede sin avellanar es un supuesto propio". Fuente: `sayres2014comparison` filas 34-35; `doublemedical2021trauma` (ficha :72-80, *Head Diameter 8.0mm*); IMP #97 (:6696) |
| T04 | traza | APLICADO | "solo en una rosca de 16 mm". Fuente: `zhu2022optimalposition` fila "Longitud de rosca (modelo FEA)" |
| T05 | traza | APLICADO | "Tres parametros quedan sin fijar por la documentacion del propio fabricante" |
| S06 | estilo | APLICADO | "Quedan fuera de alcance las ablaciones ... y la evaluacion de segmentacion posterior (Dice, HD95); esta ultima, por dos condiciones auditables" |
| S07 | estilo | APLICADO | l.42 sin conector; l.253 con S26 |
| S08 | estilo | APLICADO | "los errores que reportan tres metodos de MAR en la misma escala" |
| S09 | estilo | APLICADO | "la fraccion de 0.1 % que se usa" |
| S10 | estilo | APLICADO | "cirujano otorrinolaringologo y ciego a la auditoria automatica" |
| S11 | estilo | APLICADO | l.101 nombra las tres preguntas; l.183: "porque cada una tiene su propia referencia" |
| S12 | estilo | APLICADO | "se entrena con la apariencia de una mezcla de materiales" |
| S13 | estilo | APLICADO | "Declarado; acota la magnitud de cada perturbacion" |
| S14 | estilo | APLICADO | "La profundidad no determina el nivel" |
| S15 | estilo | APLICADO | Parrafo nuevo en "Los fenotipos de morfologia sacra..." |
| S16 | estilo | APLICADO | "Las fuentes revisadas no dan un valor para el ancho, pero si el sentido del error" |
| S17 | estilo | APLICADO | l.183 remite a los controles de la Seccion SAP |
| S18 | estilo | APLICADO | Ver T02 |
| S19 | estilo | APLICADO | "por seleccion y no por colocacion, el mismo sesgo que introduciria ajustar el muestreador" |
| S20 | estilo | APLICADO | "se ancla en un algoritmo de MAR (Seccion compuerta) que no tiene analogo en sintesis" |
| S21 | estilo | APLICADO | Se quita "y no contra una verdad de referencia inexistente" |
| S22 | estilo | APLICADO | "una linea base sin rayas" |
| S23 | estilo | APLICADO | Tres oraciones en l.221; el `\GAPDEC` de la contingencia pasa tras "Nunca se infiere equivalencia...", la oracion sobre la prueba de equivalencia. No se escribe que la prueba "depende del plazo": solo el GAP lo dice |
| S24 | estilo | APLICADO | "exacta por construccion (Seccion sintetizador); en el protocolo fisico sí es una medicion" |
| S25 | estilo | APLICADO | "Como el control de nivel excluyo a 11 de 34 ... y a 7 de 57 (Seccion datos), la cohorte primaria pierde, en proporcion, mas pacientes del grupo 2 que el conjunto de partida" |
| S26 | estilo | APLICADO | "Cualquier acuerdo con la referencia clinica se lee como acuerdo..." |
| lint E-P1 x4 (l.180, 182, 198, 253) | lint | SIN CAMBIO | Son cifras de conteo del propio diseno (tres reglas, seis controles, seis combinaciones), con fuente en respuestas anteriores. Anadir un `\ref` por linea para callar el lint seria esquivarlo |

## Escalados y preguntas para la autora (van a #127)

1. **T02:** ¿de donde salen los 8 mm de la exclusion de extremos (medicion del corredor y tramo $T$ de SAP)? DEC D-O2.3
   solo justifica que se excluyan los extremos. Si el valor es una convencion propia, basta con decirlo.
2. **guia-5 (baja, no aplicado):** la viabilidad del corredor aparece como caracterizacion de cohorte (l.91, con porcentajes)
   y como variable dependiente descriptiva del Obj 2 (Tabla de diseno, SAP). ¿Cual de los dos papeles queda en el cap. 3?
3. **guia-3 (aplicado segun DEC):** la redaccion sigue #69 (a)+(c). Si la autora quiere dar un motivo para asumir S1 en la
   serie navegada, hace falta una frase de la publicacion; hoy la ficha solo tiene la del criterio de evaluacion.

## Decisiones de redaccion

- *Phantom* = "fantoma" en todo el documento, tanto para el fantoma de geometria conocida de SAP como para el fantoma
  fisico de Peters et al.; nunca "fantasma".
- "Recorte" solo para el modelo previo de TotalSegmentator (por defecto / alternativo). Los 8 mm por extremo = "exclusion
  de extremos". El *clipping* de intensidades a un rango = "saturar / saturacion", el mismo sentido que el canal "no
  saturado" de la codificacion multiventana.
- La particion del Obj 1 tiene tres conjuntos: "entrenamiento", "validacion" (8 casos) y "prueba" (34 pacientes). "Casos"
  para el conjunto de validacion y "pacientes" para los 3 con implante real que miden $\Delta$, como en DEC.
- Una decision de `docs/01-decisiones.md` que resuelve una implicancia todavia marcada ABIERTA en `04-implicancias.md`
  (p. ej., #69 en DEC 2026-09-17 C) se redacta como decidida; no se escala.
- La razon de un procedimiento no se escribe junto a su parametro como si lo justificara: si el valor no tiene fuente,
  va un `\GAPDEC` sobre el valor.
