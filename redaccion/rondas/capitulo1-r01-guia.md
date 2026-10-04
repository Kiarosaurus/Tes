# Revision guia CS — capitulo1 — r01

Lecturas cruzadas: `introduccion.tex` (objetivos, alcance), `capitulo3.tex` completo (para G-B3, G-T2,
G-T3, G-T4, G-T5). Respuesta previa: `capitulo1-r00-respuesta.md` (redaccion inicial, sin rechazos que
respetar). Lint r01: PASA, 0/0/0.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-B1 | capitulo1.tex:68-78 | El capitulo se declara escrito para quien "no conoce la cirugia de la pelvis" (l.11), pero usa sin definir "cortical", "platillo (superior de S1)", "ala sacra", "foramen neural", "tabla externa del ilion" y "articulacion sacroiliaca". "Cortical" es la base de la brecha cortical, concepto central de SAP; ni el glosario la define. No hay figura anatomica. | Glosa corta en la primera aparicion de cada termino, con fuente de una ficha; si ninguna ficha lo sostiene, `\GAPLIT`. Valorar una figura anatomica del sacro con el corredor (o `\GAPDEC` si no hay imagen en el repositorio). |
| guia-2 | media | G-T2, G-B3 | capitulo1.tex:68 | Define el tornillo iliosacro como el que "termina dentro del sacro" y advierte que las cifras de un tipo no valen para el otro. El cap. 3 (l.196) dice que el tornillo iliosacro "entra y sale por la cortical del ilion por diseño", y el tramo medido usa la longitud del corredor (mediana 138 mm, Tabla 3.2). Con la definicion del cap. 1, el lector no puede decidir que tipo de corredor mide el cap. 3, ni si le aplican los 10 mm de Kaiser. | Decir en l.68, o con remision, a cual de los dos tipos corresponde el corredor que mide este trabajo. Si eso no esta decidido, `\GAPDEC` (el redactor ya lo levanto como observacion en r00). |
| guia-3 | media | G-B3 | capitulo1.tex:44 | La "compresion arcoseno hiperbolico" se nombra pero no se define en ningun capitulo, y es una de las tres codificaciones del Obj 1: la primera en el orden a priori y la que supone el borrador del sintetizador. El lector no puede verificar la compuerta sin conocer su forma. | Dar la transformacion (forma y parametros) desde `tesis/main.tex` o `docs/01-decisiones.md`, con su relacion con la Ec. `eq:ventana`. Si no consta, `\GAPDATO`. |
| guia-4 | media | G-T2 | capitulo1.tex:44, 122 | Usa la sigla "MAE" sin expandirla. En el orden del documento, la expansion recien llega en cap. 3 l.60 (la introduccion dice "error absoluto medio" sin sigla). Ademas contradice la decision de r00 (BITACORA §2, 2026-10-03): las siglas definidas despues no se usan en el marco teorico. Es el patron PAT-3 (termino usado antes de su definicion). | Escribir "error absoluto medio" en l.44 y l.122, o definir la sigla en l.44 y retirar la expansion duplicada del cap. 3 (decision BITACORA capitulo2-r04: la sigla se define en la primera aparicion). |
| guia-5 | media | G-B2 | capitulo1.tex:116 | El marco estadistico define que la equivalencia se concluye "cuando la diferencia pareada cae dentro de un margen". Tomado literalmente, una estimacion puntual dentro del margen bastaria. El cap. 3 (l.225) exige que el IC del 90 % de la diferencia caiga entero dentro del margen, y esa es la definicion que hace correcta la prueba. El marco no cubre el IC del 90 % ni su relacion con TOST. | Reformular: la equivalencia se concluye cuando el intervalo de confianza de la diferencia pareada cae entero dentro de $[-\Delta,+\Delta]$. La fuente del vinculo con las dos pruebas unilaterales queda bajo el `\GAPLIT` de l.118. |
| guia-6 | media | G-T4 | capitulo1.tex:112 | Afirma como hecho que en el Obj 3 "el error se promedia por paciente". El cap. 3 (l.223) marca con `\GAPDEC` como se agregan por paciente las poses y las regiones de rayas. Ademas, la magnitud primaria del Obj 3 es la *streak amplitude*, no un error. | Limitar la oracion al Obj 1, o replicar el `\GAPDEC` del cap. 3 para el Obj 3 (decision BITACORA introduccion-r02: el resumen de un tramo marcado con GAP lleva el mismo GAP). |
| guia-7 | media | G-T4 | capitulo1.tex:62 | "usa la simulacion fisica como comparacion" esta en presente de hecho. El cap. 3 marca el protocolo fisico como no realizado (`\GAPDATO`, l.221) y su permanencia como contingencia de plazo (`\GAPDEC`, l.225). El propio capitulo replica ese GAP en l.118. | Futuro de intencion ("preve usar ... como comparacion"), segun la decision BITACORA introduccion-r04, o remision al GAP de l.118. |
| guia-8 | media | G-T5 | capitulo1.tex:13 | Patron PAT-71 reincide. Dice que las secciones "siguen el recorrido de un volumen por la cadena propuesta", pero el orden real (TC, artefactos, fijacion, difusion, estadistica) pone el artefacto antes de la colocacion, al reves que la Fig. `fig:pipeline` (corredor y muestreador antes que el sintetizador). La compuerta y la estadistica tampoco son piezas de la cadena. | Describir el orden real y su razon (p. ej., de la medida fisica al artefacto, luego la colocacion, luego el generador y la lectura de resultados), sin atribuirlo al recorrido de la cadena. |
| guia-9 | media | G-T1 | capitulo1.tex:19 (vs l.44) | Patron PAT-67 reincide. La fila 1 de la Fig. `fig:mt-conceptos` asigna a la codificacion multiventana los "canales de entrada y salida del sintetizador (Objetivo 3)", pero el cuerpo de §1.1 solo la liga a la compuerta del Obj 1. La l.11 promete decir para cada concepto "en que pieza de la propuesta interviene". | Agregar en l.44 una oracion con remision a `sec:sintetizador` (el sintetizador usa la codificacion como canales, sin autoencoder; codificacion no fijada, con el `\GAPDEC` del cap. 3), o quitarla de la figura. |
| guia-10 | media | G-T2 | capitulo1.tex:78 | Patron PAT-14 reincide. Aqui la brecha cortical es "la perforacion de la cortical por el implante". La introduccion (l.39) la define como "cuanto sobresale el implante del hueso", y el cap. 3 (l.257) aclara que SAP mide protrusion fuera de una envolvente y no perforacion de una cortical segmentada. El lector recibe dos definiciones del mismo termino. Se respeta la decision §2 (capitulo2-r01) de llamar "brecha cortical" a la perforacion de Zwingmann et al. | Mantener el nombre y agregar una oracion: en este trabajo el grado se calcula como protrusion fuera de la envolvente osea (`sec:sap`, `sec:amenazas`), que aproxima esa perforacion. |
| guia-11 | baja | G-B2 | capitulo1.tex (ausente) | El marco no presenta los resultados previos que el cap. 3 usa como caja negra en el corredor y en SAP: la segmentacion anatomica (TotalSegmentator sobre nnU-Net) y el cierre morfologico de la envolvente. | Un parrafo breve en §1.3 o §1.4 que los nombre como caja negra, con cita y remision a `sec:corredor`. |
| guia-12 | baja | G-T3 | capitulo1.tex:88 | La distribucion normal se escribe $\mathcal{N}$ en el cap. 1 y $N$ en el cap. 3 (Ec. `eq:pose`). La razon que da r00, que en el cap. 3 "$N$ es la normal de las perturbaciones", trata como otro objeto lo que es el mismo concepto. | Unificar el simbolo en ambos capitulos. |
| guia-13 | baja | G-T2 | capitulo1.tex:104 | El cap. 3 (l.60, l.69) habla del "autoencoder variacional" y adapta por separado el codificador y el decodificador. El marco solo describe "un autoencoder" y nunca nombra el codificador. | Nombrar codificador y decodificador, y el caracter variacional si una ficha lo respalda. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | no cumple (guia-9) |
| G-T2 | no cumple (guia-2, guia-4, guia-10, guia-13) |
| G-T3 | no cumple, solo baja (guia-12); el resto de la notacion propia ($n$, $\bar\gamma_n$, $\boldsymbol{\xi}$, $w_{\min}$) no choca con el cap. 3 |
| G-T4 | no cumple (guia-6, guia-7) |
| G-T5 | no cumple (guia-8); la apertura si situa el capitulo entre la introduccion y el cap. 2 |
| G-T6 | cumple (lint y compilacion sin citas indefinidas) |
| G-B1 | no cumple (guia-1) |
| G-B2 | no cumple (guia-5, guia-11); definiciones, notacion y modelos de difusion presentes |
| G-B3 | no cumple (guia-2, guia-3); HU, Wasserstein-1, Wilcoxon, TOST y remuestreo, cumple con GAP (`\GAPLIT` l.35, l.114, l.118) |
| G-B4 | cumple (supuesto del dominio de imagen l.60, limite del 2.5D l.108, convencion de equiespaciado l.82) |
| P-MT1 | cumple con GAP (muestreo del sintetizador y numero de cortes 2.5D con `\GAPDEC`; fuentes estadisticas con `\GAPLIT`) |
| P-MT2 | cumple (Fig. `fig:mt-conceptos`; fila 1 en guia-9) |
| G-A*, G-B5 a G-B10, G-C*, G-D*, G-R*, P-* de otros bloques | no aplican a esta seccion |

## Propuestas de criterio
- El marco teorico se declara escrito para un lector ajeno a la cirugia. Podria existir un criterio
  derivado de G-B1: "todo termino anatomico que interviene en una metrica propia se glosa o se ilustra".
  Hoy se cubre con G-B1, pero a criterio del revisor.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Oracion que justifica el orden de las secciones y no describe el orden real | G-T5 | "Las secciones siguen el recorrido de un volumen por la cadena propuesta" | PAT-71 |
| Fila de figura o tabla que liga un concepto a una pieza que el cuerpo no menciona | G-T1 | "canales de entrada y salida del sintetizador (Objetivo 3)" | PAT-67 |
| Sigla usada antes de su expansion, contra una decision propia de no usarla | G-T2 | "mide ese error como MAE dentro del hueso" | PAT-3 |
| La definicion conceptual del marco no coincide con la operacionalizacion del metodo | G-T2, G-B3 | "termina dentro del sacro" vs "entra y sale por la cortical del ilion" | PAT-14 |
| Un resumen afirma como hecho lo que el metodo marca con GAP | G-T4 | "el error se promedia por paciente" (Obj 3, `\GAPDEC` en cap. 3) | nuevo |
| Una definicion estadistica resumida pierde el elemento que la hace correcta | G-B2 | "la diferencia pareada cae dentro de un margen" (falta el IC) | nuevo |
