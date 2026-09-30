# Bitacora de redaccion

> Memoria compartida del ciclo de redaccion. La mantiene el **orquestador** de `/ciclo-redaccion`
> al cerrar cada etapa, consolidando lo que los revisores reportan en la seccion "Patrones" de
> sus informes. Los revisores y el redactor **la leen** al empezar; no la editan (corren en
> paralelo y se pisarian).
>
> **Etapa** = una serie de correcciones cerrada: la redaccion inicial de una seccion, o una ronda
> `rNN` despues de que el redactor responde a los revisores. Al cerrar cada etapa se compila.

## 1. Patrones recurrentes

Errores que aparecieron mas de una vez, o una vez pero con riesgo de repetirse en otras secciones.
El redactor los evita al escribir; cada revisor comprueba en su seccion **todos** los VIGENTES.

Estados: VIGENTE (hay que vigilarlo) | ERRADICADO (dos etapas seguidas sin aparecer en ninguna
seccion revisada) | DESCARTADO (la autora decidio que no es error).

| ID (PAT-n) | Patron | Criterio | Antes -> despues (max 15 palabras cada uno) | Visto en | Veces | Estado |
|---|---|---|---|---|---|---|
| PAT-1 | Frase de sintesis que atribuye a todos los objetivos una propiedad que solo tienen algunos | G-C6, E-P3 | "Las tres filas comparten ... la regla se fijo antes" -> decir cual objetivo la tiene | capitulo3-r01, capitulo3-r02, introduccion-r01 | 3 | ERRADICADO |
| PAT-2 | Cantidad de diseno calificada ("declarada", "reducida", "pocos") sin valor ni GAP | P-MM3 | "una proporcion declarada de parches" -> valor con fuente o \GAPDEC | capitulo3-r01, capitulo3-r03 | 2 | ERRADICADO |
| PAT-3 | Termino tecnico usado antes de su definicion formal | G-T2 | "grados de brecha" en l. 78 -> definir en primera aparicion o adelantar | capitulo3-r01, introduccion-r02, introduccion-r04, introduccion-r05 | 4 | VIGENTE |
| PAT-4 | Procedimiento nombrado ("heuristica", "control de calidad") sin descripcion ni GAP | P-MM3 | "se localizaron con una heuristica" -> describir o \GAPDATO | capitulo3-r01, capitulo3-r02 | 2 | ERRADICADO |
| PAT-5 | Metadeclaracion: la oracion anuncia que algo "se declara" o "es reportable" en vez de decirlo | E-R2 | "esa diferencia se declara y no se resuelve" -> decir el hecho | capitulo3-r01, capitulo3-r02, capitulo3-r04, capitulo3-r05, introduccion-r02 | 5 | ERRADICADO |
| PAT-6 | La cita atribuye a la fuente origen, razon o lectura que da la ficha, TM o un tercero | E-R6 | "Kaiser et al., de quienes proviene" -> Kaiser lo toma de trabajos previos | capitulo3-r01, capitulo3-r03, capitulo3-r04, capitulo3-r05, introduccion-r01, introduccion-r02, introduccion-r05 | 7 | VIGENTE |
| PAT-7 | Un mismo conjunto de datos externo recibe varios nombres | E-R5, E-T1 | "conjunto/serie de referencia" -> siempre "referencia clinica" | capitulo3-r01, capitulo3-r02, capitulo3-r03 | 3 | ERRADICADO |
| PAT-8 | Comparativo sin cifras al lado aunque el dato exista | E-P4 | "mas al truncamiento que a la contaminacion" -> dar los recuentos | capitulo3-r01, introduccion-r04, introduccion-r05 | 3 | VIGENTE |
| PAT-9 | Se copia `tesis/main.tex` cuando una decision o implicancia APLICADA posterior lo sustituyo | G-T4 | "convencion de 10 mm" -> criterio `D >= d + 2c` (#31) | capitulo3-r01 | 1 | ERRADICADO |
| PAT-10 | Se confunden unidades de recuento (volumenes, componentes) con pacientes | G-T4 | "otros 10 pacientes quedan excluidos" -> "unidades de volumen" | capitulo3-r01, capitulo3-r02 | 2 | ERRADICADO |
| PAT-11 | GAP redactado sobre el estado inicial de una implicancia, sin sus actualizaciones | G-T4 | "la corrida no se ha lanzado" -> estado vigente de la implicancia | capitulo3-r01, capitulo3-r02 | 2 | ERRADICADO |
| PAT-12 | Afirmacion sobre la literatura sin `\cite` aunque la fuente esta en el repositorio | G-T4 | "no es consistente entre estudios" -> con \cite de las fichas | capitulo3-r01, introduccion-r01 | 2 | ERRADICADO |
| PAT-13 | Integridad de la preinscripcion afirmada mas fuerte que el registro | G-T4 | "antes de cualquier corrida" -> "antes de correr la prueba que decide" | capitulo3-r01, capitulo3-r02, introduccion-r01 | 3 | ERRADICADO |
| PAT-14 | Un termino, nombre o simbolo designa dos cosas distintas en el capitulo (o reusa el sentido de otra fuente) | G-T2, G-T3, E-T1, G-T4 | "holgura" para $h$ y para $\epsilon$ -> "margen cortical" / "holgura radial" | capitulo3-r02, capitulo3-r03, capitulo3-r04, capitulo3-r05, introduccion-r01, introduccion-r02, introduccion-r03, introduccion-r04, introduccion-r05 | 9 | VIGENTE |
| PAT-15 | Comprobaciones de implementacion presentadas como falsabilidad del objetivo | G-A8, E-P3 | "se declaro falsable en tres puntos" -> "controles de consistencia de la implementacion" | capitulo3-r02, capitulo3-r04 | 2 | ERRADICADO |
| PAT-16 | Metrica primaria elegida porque la linea base no puede producirla por construccion | G-C9 | Wilcoxon de *streak amplitude* contra copia y pegado -> decir que resultado seria fallo | capitulo3-r02 | 1 | ERRADICADO |
| PAT-17 | Negativo universal sobre la literatura sin acotarlo a las fuentes revisadas | E-P3 | "Ninguna fuente publicada dice" -> "ninguna de las fuentes revisadas dice" | capitulo3-r02 | 1 | ERRADICADO |
| PAT-18 | Conector causal parentetico (", por tanto,") entre oraciones sin relacion causal | E-O3 | "no tiene, por tanto, una regla" -> "no tiene regla de decision: ..." | capitulo3-r02 | 1 | ERRADICADO |
| PAT-19 | GAP que declara ausente una cifra ya calculada o fijada en DEC o en un resumen de experimento VIGENTE | G-T4, OC-2 | \GAPDEC{proporcion de parches} -> 0.62 citando DEC 2026-09-21 | capitulo3-r02 | 1 | ERRADICADO |
| PAT-20 | El metodo se describe segun la decision y no segun lo implementado y corrido, que difiere | G-T4 | viabilidad con envolvente 6.5-8.0 mm (D-O2.4) vs corrida con 4.91/7.0/7.3 mm -> \GAPDEC | capitulo3-r02, capitulo3-r05 | 2 | ERRADICADO |
| PAT-21 | Opcion de herramienta nombrada sin decir que controla, aunque de ella dependen resultados | G-T2 | "recorte por defecto/alternativo" sin definir -> modelo de 6 mm / 3 mm (`--robust_crop`) | capitulo3-r03 | 1 | ERRADICADO |
| PAT-22 | Supuesto que sostiene el diseno, enunciado sin justificacion y ausente de amenazas a la validez | G-C1, G-C7 | mascara-artefacto independiente del implante -> supuesto no verificado en validez de constructo | capitulo3-r03, capitulo3-r04, capitulo3-r05, introduccion-r02 | 4 | ERRADICADO |
| PAT-23 | Parametro del diseno que aparece por primera vez en amenazas a la validez | P-MM1 | presentarlo en el metodo y remitir desde amenazas | capitulo3-r03 | 1 | ERRADICADO |
| PAT-24 | "Coincide" o factor ("mas del doble") entre cifras que difieren o cuyo factor no vale en todo el rango | E-P4 | "sobreestimaria mas del doble la seccion" -> ambas cifras visibles, sin factor | capitulo3-r03 | 1 | ERRADICADO |
| PAT-25 | Oracion-razon suelta al final del parrafo, separada del argumento que sostiene | E-M4 | "Zwingmann et al. no reportan..." -> "La segunda razon, que ..." | capitulo3-r03 | 1 | ERRADICADO |
| PAT-26 | El mismo argumento se repite en dos amenazas a la validez distintas | E-R4 | circularidad en validez interna y externa -> una sola, con remision | capitulo3-r03 | 1 | ERRADICADO |
| PAT-27 | Limitacion con evidencia confirmada en el registro redactada solo como hipotesis | G-T4, OC-3 | "fracturas no detectadas estrecharian" -> un paciente con fractura confirmada (#125) | capitulo3-r03 | 1 | ERRADICADO |
| PAT-28 | Subconjunto de la particion nombrado en el diseno sin haberse definido en la particion | G-T2, P-MM3, E-T1 | "pacientes de validacion" sin definir -> particion con entrenamiento, validacion (8) y prueba (34) | capitulo3-r04 | 1 | ERRADICADO |
| PAT-29 | Valor de un parametro dado en una seccion posterior a la que lo usa | P-MM3 | remision hacia atras -> dar el valor donde se usa por primera vez | capitulo3-r04 | 1 | ERRADICADO |
| PAT-30 | La misma cifra propia hace de caracterizacion de cohorte y de variable dependiente | P-MM1 | viabilidad en l.91 y en la tabla de diseno -> elegir un papel (\GAPDEC) | capitulo3-r04 | 1 | ERRADICADO |
| PAT-31 | Cifra medida en una condicion particular pierde la condicion al retomarse en otra seccion | E-P3 | "resolucion de 0.083 mm" -> "en el fantoma, 0.083 mm" | capitulo3-r04, introduccion-r01, introduccion-r02, introduccion-r03, introduccion-r04 | 5 | VIGENTE |
| PAT-32 | Un termino tecnico aparece con dos formas en el capitulo | E-T1 | "fantasma" / "fantoma" -> siempre "fantoma" | capitulo3-r04, capitulo3-r05 | 2 | ERRADICADO |
| PAT-33 | Parrafo cajon: varias ideas sin oracion tematica | E-M1 | envolvente + seis controles + escala de Smith -> separar por funcion | capitulo3-r04 | 1 | ERRADICADO |
| PAT-34 | Anafora a una razon u objeto que el parrafo no dice | E-M4 | "por la misma razon" -> nombrar la razon | capitulo3-r04, capitulo3-r05 | 2 | ERRADICADO |
| PAT-35 | La razon de un procedimiento se presenta como justificacion del valor de su parametro | G-T4 | "8 mm ... su razon es clinica" -> \GAPDEC sobre el valor | capitulo3-r04 | 1 | ERRADICADO |
| PAT-36 | Exclusividad ("la unica") afirmada sin cotejar las demas fichas del repositorio | G-T4, E-P3 | "la unica medicion, 8.0 mm" -> cotejar #97 y el catalogo que tambien da 8.0 | capitulo3-r04 | 1 | ERRADICADO |
| PAT-37 | Evaluacion nombrada en el texto sin metrica ni analisis, y ausente de la tabla de diseno | G-C5 | "se evalua por la continuidad de los valores de TC" -> metrica o \GAPDEC | capitulo3-r05 | 1 | ERRADICADO |
| PAT-38 | Amenaza o dato de sesgo en amenazas sin su efecto sobre el resultado | G-C7, E-M4 | "pierde mas pacientes del grupo 2" -> decir que sesgo introduce | capitulo3-r05, introduccion-r01, introduccion-r02, introduccion-r04 | 4 | VIGENTE |
| PAT-39 | Generalizacion ("todas", "todo") que el mismo parrafo contradice | E-P3 | "Todas las cifras dependen del recorte por defecto" -> "las cifras principales" | capitulo3-r05, introduccion-r02, introduccion-r03 | 3 | ERRADICADO |
| PAT-40 | Adjetivo que contradice una definicion dada en el propio capitulo | E-T1 | "el eje optimo" (el muestreador no busca optimo) -> "el eje del corredor" | capitulo3-r05 | 1 | ERRADICADO |
| PAT-41 | "Muestra" usado para resultados ajenos | E-P3 | "X muestra que" -> "X reporta que" | capitulo3-r05 | 1 | ERRADICADO |
| PAT-42 | Dato deducido de recuentos de una fuente que contradice lo que la fuente declara, sin decir la contradiccion | E-R6, G-T4 | dar los conteos de la fuente y la contradiccion | capitulo3-r05 | 1 | ERRADICADO |
| PAT-43 | Dos objetivos reclaman la misma evidencia, y no se sabe cual falla | G-A7, G-A8 | Wasserstein-1 como evidencia del Obj 2 y del Obj 4 -> comparacion en Obj 2, definicion en Obj 4 | introduccion-r01 | 1 | ERRADICADO |
| PAT-44 | Oracion tematica o lista que anuncia N elementos o "cada uno por una razon" y no los cubre | G-A10, E-M1 | "cuatro exclusiones, cada una por una razon" -> dar la razon de cada una | introduccion-r01 | 1 | ERRADICADO |
| PAT-45 | Titulo de objetivo con verbo que presupone el resultado, o que nombra lo que valida una ruta descartada | G-A7, G-T5, E-P3 | "Validar la representacion" -> "Evaluar una representacion multiventana" | introduccion-r01, introduccion-r02 | 2 | ERRADICADO |
| PAT-46 | La misma salvedad de alcance repetida en cada subseccion, como reflejo | E-R4 | decirla una vez en Alcance y remitir | introduccion-r01, introduccion-r02, introduccion-r03, introduccion-r04, introduccion-r05 | 5 | VIGENTE |
| PAT-47 | Convenciones declaradas listadas como supuestos | E-P3 | ancho de $B_\delta$ en "supuestos" -> "convenciones" | introduccion-r01 | 1 | ERRADICADO |
| PAT-48 | Afirmacion de cronologia del proyecto sin cotejar las fechas de DEC | G-T4 | "el orden de los objetivos es el orden en que se decidieron" -> retirar | introduccion-r01 | 1 | ERRADICADO |
| PAT-49 | Contribucion anunciada que ningun objetivo evalua, sin decirlo | G-A7, G-A10 | "el tercero es el uso de la codificacion multiventana" -> "ningun objetivo aisla ese aporte, porque ..." | introduccion-r02, introduccion-r03, introduccion-r04 | 3 | VIGENTE |
| PAT-50 | Exclusion de alcance nombrada con un termino que el documento no define | G-A10, G-T2 | "ablaciones restriccion por restriccion" sin enumerar restricciones -> \GAPDEC | introduccion-r02, introduccion-r03 | 2 | ERRADICADO |
| PAT-51 | El criterio que descarta una alternativa se aplica tambien, sin decirlo, a la opcion adoptada | E-M4 | "no tendria validacion en metal que heredar" -> decir si vale para la adoptada | introduccion-r02, introduccion-r03 | 2 | ERRADICADO |
| PAT-52 | Debilidad de una prueba nombrada sin su consecuencia (que resultado ya no puede ocurrir) | E-M4 | "una magnitud que la linea base no produce" -> decir que la prueba no puede fallar | introduccion-r02, introduccion-r03, introduccion-r05 | 3 | VIGENTE |
| PAT-53 | Un modal de la fuente ("may") se convierte en afirmacion de hecho al citarla | E-R6 | "cuyo error cambia de direccion" -> "cuyo error puede cambiar" | introduccion-r02 | 1 | ERRADICADO |
| PAT-54 | Recuento cerrado de limitaciones o supuestos que omite otros declarados en el metodo | G-A10 | "las limitaciones son tres" -> sin recuento, con remision a `sec:amenazas` | introduccion-r03 | 1 | ERRADICADO |
| PAT-55 | Tension de la justificacion que la propia comparacion de la tesis resuelve con la alternativa descartada | G-A3 | "ninguno produce a la vez" (el protocolo fisico corre sobre poses muestreadas) -> hecho + \GAPDEC | introduccion-r03 | 1 | ERRADICADO |
| PAT-56 | Un concepto recibe un nombre nuevo porque el termino fijo no encaja en la oracion | E-R5 | "marco multiventana" -> reescribir la oracion con "codificacion multiventana" | introduccion-r03 | 1 | ERRADICADO |
| PAT-57 | Dato o comparacion presentada en Alcance que ningun objetivo nombra como uso | G-A7 | comparacion con observaciones reales en Alcance -> nombrarla en el Obj 3 o quitarla | introduccion-r04, introduccion-r05 | 2 | VIGENTE |
| PAT-58 | Parrafo que crece por salvedades anadidas en rondas sucesivas hasta superar 7 oraciones con varias funciones | E-O2, E-M1 | dividir, remitir al cap. 3 y quitar repeticiones antes que agregar | introduccion-r04, introduccion-r05 | 2 | VIGENTE |
| PAT-59 | Sustantivo calcado del ingles que sustituye al termino fijo | E-R5, E-T1 | "un latente" (*a latent*) -> "el autoencoder" | introduccion-r04 | 1 | VIGENTE |
| PAT-60 | Definicion circular de un termino clinico ("difiere de lo normal") | E-R2 | "rasgos que difieren del sacro normal" -> nombrar 2-3 rasgos de la ficha | introduccion-r04 | 1 | VIGENTE |
| PAT-61 | Un resultado propio se enuncia en terminos (mecanismo) que el diseno del objetivo no mide | G-A7 | "se definen sobre rangos que excluyen el hueso denso" -> umbral superado o no | introduccion-r05 | 1 | VIGENTE |
| PAT-62 | Convencion propia redactada como igualdad o hallazgo ("equivale a") | E-P3 | "equivale a dos desviaciones estandar" -> "se fija en" | introduccion-r05 | 1 | VIGENTE |
| PAT-63 | Adjetivo que da a lo producido la calidad de aquello con que solo se compara | E-P3 | "distribucion clinica de poses" (del muestreador) -> "distribucion de poses" | introduccion-r05 | 1 | VIGENTE |
| PAT-64 | Negativo que abarca varias fuentes y solo vale para una parte | E-R6 | "en ninguno hay mecanismo" -> partir por subgrupo | introduccion-r05 | 1 | VIGENTE |
| PAT-65 | Se copia de la fuente la formulacion menos precisa cuando la misma fuente trae una mas precisa | G-T4 | "excluyo 7 de 57" -> 8 de 57 (7 son solo discordancia) | introduccion-r05 | 1 | VIGENTE |

## 2. Decisiones de redaccion tomadas en el ciclo

Soluciones que se adoptaron para un caso y deben aplicarse igual en todo el documento (como se
traduce un termino, como se presenta un resultado negativo, como se cita un fabricante). Si una
contradice `overleaf/CLAUDE.md` o `ESTILO.md`, manda el archivo y la fila se corrige.

| Fecha | Decision | Origen (seccion-rNN, hallazgo) | Quien decidio |
|---|---|---|---|
| 2026-09-29 | *gate* del Obj 1 = "compuerta (*Go/No-Go*)"; veredicto negativo = "veredicto negativo" o "No-Go" | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | *default/robust crop* de TotalSegmentator = "recorte por defecto" / "recorte alternativo" (no "robusto", E-IA) | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Segundo corredor: siempre "segundo corredor bajo S1", nunca "S2" (#121) | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | *bone envelope* = "envolvente osea"; `D_TS_max` = "diametro del corredor" | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | arcsinh = "compresion arcoseno hiperbolico" | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | *benchmark* de Zwingmann = "referencia clinica" / "conjunto clinico de referencia"; no "benchmark" en texto corrido | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | test-retest = "prueba y reprueba"; *downstream segmentation* = "evaluacion de segmentacion posterior" | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | TOST = "dos pruebas unilaterales de equivalencia (TOST, *two one-sided tests*)" | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | NMAR no se nombra como sigla mientras ninguna ficha de su expansion | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Fuentes de fabricante (`synthes2003guide`, `doublemedical2021trauma`) se senalan como "documentacion tecnica no revisada por pares" (P-EA1) | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Cap. 3 describe regla y diseno; veredictos (61.72 HU, Wasserstein-1, estratificacion) van al cap. 4; caracterizacion de cohorte si va en cap. 3 | capitulo3-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Datos de Zwingmann = "referencia clinica" (nunca "conjunto/serie de referencia"); grupos = "serie navegada / serie convencional" | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Brazo" solo para condiciones experimentales propias, no para tecnicas quirurgicas de Zwingmann | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Viabilidad del corredor: criterio `D >= d + 2c` (holgura = operacionalizacion propia de Kaiser); "10 mm" solo como "convencion de comparacion"; Kaiser no es origen del 10 mm | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Paciente" solo para pacientes (168); volumenes fuera de uso = "unidades de volumen" (179) | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Regla de la compuerta "fijada antes de correr la prueba que decide", nunca "antes de cualquier corrida"; consecuencia negativa como se registro | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Sin metadeclaraciones ("y se declara", "es un resultado reportable") | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Cifras ajenas se comparan dando valores, sin factores calculados | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Valor p = `$p$` minuscula; `$P$` para distribuciones | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Entrada con dos autores: "Zhu y Liao", no "et al." (E-F3) | capitulo3-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Kaiser: "margen cortical de longitud util" ($h$ = 5 mm) vs "holgura radial" ($\epsilon$ = 1-2 mm, criterio $D \geq d + 2\epsilon$); nunca "holgura" a secas para $h$ | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Indice de paciente $i$; $p$ solo para valor p | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | MAISI: no desplegar el nombre en ingles (contiene "AI"); "el generador de volumenes de TC de Guo et al." | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Metricas de Peters et al." = las tres metricas; "protocolo fisico (de Peters et al.)" = el brazo de simulacion | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Negativos sobre la literatura acotados a "las fuentes revisadas" | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Controles de consistencia de la implementacion no se llaman "falsables"; se distinguen de la regla de fallo | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Cifra congelada en `docs/01-decisiones.md` entra como hecho; \GAPDEC solo si dos decisiones se contradicen, si decision y corrida difieren o si ninguna da el dato | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Viabilidad: se reportan los dos extremos ($d$ = 6.5, $\epsilon$ = 1 y $d$ = 8.0, $\epsilon$ = 2) con ambos recortes, como "pacientes que cumplen el criterio" | capitulo3-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Referencia clinica" se define en su primera aparicion (series navegada y convencional de Zwingmann et al.) y es el unico nombre en el documento | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Envolvente" solo para la envolvente osea; 6.5-8.0 mm = "calibre nominal"; tres geometrias: calibre nominal, mascara $M$, calibre de medicion | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Protocolo fisico" (de Peters et al.) tambien para el brazo de comparacion; "brazo" solo en plural generico | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Recorte de TotalSegmentator: "por defecto" (6 mm) y "alternativo" (3 mm, `--robust_crop`), definidos en su primera aparicion | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | SAP: "seis controles, uno sobre un fantasma de geometria conocida y cinco sobre volumenes reales" | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Lectura operativa propia de una fuente: "este trabajo lee ... como ...", no como propiedad del marco citado | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Cercania entre cifras: "esta proxima a" con ambas cifras visibles, sin diferencia ni factor | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Revisor clinico de S1: "reviso", no "confirmo" (S1 correcto en 51 de 65) | capitulo3-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | *Phantom* = "fantoma" en todo el documento; nunca "fantasma" | capitulo3-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Recorte" solo para el modelo previo de TotalSegmentator; los 8 mm por extremo = "exclusion de extremos"; *clipping* de intensidades = "saturar / saturacion" | capitulo3-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Particion del Obj 1: "entrenamiento", "validacion" (8 casos) y "prueba" (34 pacientes); "pacientes" para los 3 con implante real que miden $\Delta$ | capitulo3-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Una decision de `docs/01-decisiones.md` que resuelve una implicancia aun ABIERTA en `04-implicancias.md` (p. ej., #69 en DEC 2026-09-17 C) se redacta como decidida | capitulo3-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | La razon de un procedimiento no se escribe junto a su parametro como si lo justificara; valor sin fuente = \GAPDEC | capitulo3-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "Dominio de imagen" es el unico nombre para operar sobre valores de TC por voxel (frente a latente y sinograma); no "espacio de imagen" ni "espacio de pixeles" | capitulo3-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | *CT numbers* = "valores de TC"; no "numeros de TC" | capitulo3-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Paciente adquirido dos veces = "par de reproducibilidad"; repeticion del protocolo fisico = "corridas repetidas del protocolo fisico"; no "prueba y reprueba" | capitulo3-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Si decision y codigo difieren, el metodo describe lo que se corrio y la decision no aplicada va en \GAPDEC (OC-5, PAT-20) | capitulo3-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | No se derivan porcentajes o conteos que no esten en la fuente (11 de 34 no pasa a 32 %) | capitulo3-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Evaluacion que solo consta en el borrador `diseno_A.md`: \GAPDEC que dice lo que propone el borrador y que no esta preinscrita; no entra en la tabla de diseno | capitulo3-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Objetivo especifico = titulo en negrita con verbo en infinitivo + 2-3 oraciones (E-O1, G-A6) | introduccion-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Los objetivos de la introduccion llevan un parrafo de falsabilidad objetivo por objetivo; los que no la fijan, con \GAPDEC (evita PAT-1, PAT-15) | introduccion-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | "HU" es masculino ("los HU") | introduccion-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | En la introduccion la TOST se nombra "comparacion de equivalencia frente al protocolo fisico"; la sigla se define en el cap. 3 | introduccion-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | En la introduccion el recorte de TotalSegmentator = "variante de la segmentacion anatomica"; en el cap. 3, "recorte por defecto / alternativo" (riesgo E-R5) | introduccion-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Primera definicion en la introduccion (Obj. especificos, en negrita): grado de brecha cortical, referencia clinica, region de generacion, mascara del implante, banda de generacion extendida, insercion por copia y pegado; ida y vuelta sin negrita | introduccion-r00 (redaccion inicial) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Objetivo con resultado desconocido o negativo: titulo con "Evaluar" o "Determinar si", nunca "Validar" | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | En la introduccion la compuerta del Obj 1 es "previa a la cadena", no una pieza de ella | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Wasserstein-1: comparacion en el Obj 2, definicion en el Obj 4 (SAP), nunca evidencia de ambos | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Junto a $B_\delta$ se dice "zonas oscuras", no "bandas oscuras" ("banda" reservada para $B_\delta$, PAT-14) | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Recuento de objetos metalicos por umbral = "objetos metalicos alargados", no "tornillos" | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Viabilidad en la introduccion: "calibre del tornillo mas una holgura radial tomada de Kaiser et al."; McLaren et al. no se citan como fuente del criterio | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Supuestos y convenciones por separado: convencion = valor fijado por este trabajo; supuesto = afirmacion sobre el mundo no verificada | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-29 | Glosas clinicas en la introduccion: aposicion corta en la primera aparicion con fuente; si la definicion solo esta en un borrador (2.5D), se remite al marco teorico | introduccion-r01 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Titulo de objetivo de tipo compuerta: nombra el objeto probado (el autoencoder) y lo que se conserva (los HU), no la representacion de la cadena | introduccion-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Supuestos y convenciones sin recuento cerrado, con remision a `sec:amenazas` y `tab:preinscripcion`; lo que TM y C3 llaman a la vez convencion y supuesto se nombra con las dos palabras | introduccion-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Contribucion que ningun objetivo evalua por separado: "ningun objetivo aisla ese aporte, porque ..." | introduccion-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | MAR se define en su primera aparicion en el orden del documento (hoy, Obj 4 de la introduccion) | introduccion-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | "Referencia" reservada para la referencia clinica; para observaciones reales y protocolo fisico, "para comparar la apariencia" / "como comparacion" | introduccion-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Recuento propio sin seccion ni `
ef` en el documento no se cita en la introduccion; se remite a la seccion del hallazgo | introduccion-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Si la introduccion resume un tramo que el cap. 3 marca con GAP, lleva el mismo GAP (PAT-31) | introduccion-r02 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Limitaciones como los supuestos: sin recuento cerrado, agrupadas por componente, con remision a `sec:amenazas`, cada una con su efecto (PAT-38) y su GAP del cap. 3 (PAT-31) | introduccion-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Tension de la justificacion debilitada por un hecho del propio diseno: se enuncia el hecho y se marca \GAPDEC con la pregunta; no se inventa la razon | introduccion-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Coincidencia verificable que podria explicar una restriccion de alcance: se dice como hecho, sin "por eso"; la razon declarada queda en \GAPDEC | introduccion-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Termino del cap. 3 no definido en la introduccion ("calibre de medicion", "control de nivel") se reemplaza por una descripcion corta | introduccion-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | "Tareas" = exclusiones de alcance; "componentes" = piezas de la cadena y objetos metalicos (PAT-14) | introduccion-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Limites de la escala de brecha = "limites de grado, de 2 mm de ancho", nunca "cortes" | introduccion-r03 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Si dividir un parrafo deja una oracion sola, esta pasa al parrafo cuya funcion comparte; nunca parrafo de una oracion | introduccion-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | En un resumen, un brazo o analisis del cap. 3 no implementado va en futuro de intencion ("preve ejecutar") y con sus condiciones | introduccion-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | En la introduccion *run* = "ejecutar"; "correr"/"corrida" solo dentro de textos de GAP con fila en MAPA | introduccion-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Termino clinico definido por diferencia con lo normal: nombrar 2-3 rasgos concretos de la ficha, sin recuentos que la ficha marca como inconsistentes | introduccion-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | La pieza que prueba el Obj 1 es "el autoencoder" / "los autoencoders", nunca "un latente"; "espacio latente" solo para el espacio | introduccion-r04 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Un resultado propio se enuncia en lo que el diseno mide (umbral, cota), no en el mecanismo; el mecanismo, si queda, marcado como interpretacion | introduccion-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Una salvedad de alcance vive en Alcance; en objetivos y justificacion, como mucho "(vease el alcance)" | introduccion-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Negacion que cubre varias fuentes se parte por subgrupo cuando no vale igual para todas | introduccion-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | Convencion propia = "se fija en", nunca "equivale a" | introduccion-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |
| 2026-09-30 | En listas de convenciones, cada oracion abre por el objeto que fija, no por un ordinal | introduccion-r05 (respuesta) | redactor-tesis (pendiente de visto bueno de la autora) |

## 3. Registro de etapas

Una fila por etapa, en orden. Paginas y GAP salen de la compilacion de cierre.

| Fecha | Seccion | Etapa | Que cambio (una linea) | Lint alta/media | Revisores alta/media (guia, estilo, traza) | GAP lit/dato/dec | Paginas | PDF |
|---|---|---|---|---|---|---|---|---|
| 2026-09-29 | capitulo3 | r00 | Redaccion inicial desde esqueleto: 7 secciones, 4 ecuaciones, 3 tablas, diagrama de cadena | 0/1 (seccion; media = "AI" en nombre de MAISI) | — (sin revision aun) | 0/7/8 | 52 | `redaccion/.build/etapas/capitulo3-r00.pdf` |
| 2026-09-29 | capitulo3 | r01 | 36 aplicados, 1 rechazado ("AI" de MAISI), 7 escalados; criterio `D >= d + 2c`, recuentos, metadeclaraciones | 0/1 | 2/7, 3/17, 3/11 | 0/9/16 | 54 | `redaccion/.build/etapas/capitulo3-r01.pdf` |
| 2026-09-29 | capitulo3 | r02 | 25 aplicados, 4 escalados; cifras de DEC como hecho (0.62, 3 pacientes), viabilidad `d + 2e`, MAISI sin sigla AI; lint PASA | 0/0 | 0/9, 0/14, 1/4 | 0/9/16 | 55 | `redaccion/.build/etapas/capitulo3-r02.pdf` |
| 2026-09-29 | capitulo3 | r03 | 12 medios aplicados, 0 escalados; terminos unicos (referencia clinica, envolvente, recortes), supuesto mascara-artefacto a amenazas, fractura #125 | 0/0 | 0/3, 0/7, 0/2 | 0/9/16 | 56 | `redaccion/.build/etapas/capitulo3-r03.pdf` |
| 2026-09-29 | capitulo3 | r04 | 9 aplicados, 1 escalado; reapertura Synthes aceptada, particion con validacion, "fantoma", exclusion de extremos | 0/0 | 0/3, 0/5, 1/1 | 0/10/17 | 57 | `redaccion/.build/etapas/capitulo3-r04.pdf` |
| 2026-09-29 | capitulo3 | r05 | 36 aplicados (5 con escalado), 1 rechazado; envolvente segun lo corrido + \GAPDEC, "dominio de imagen", "valores de TC"; TOPE | 0/0 | 0/3, 0/8, 1/0 | 0/10/22 | 57 | `redaccion/.build/etapas/capitulo3-r05.pdf` |
| 2026-09-29 | introduccion (Objetivos, Justificacion, Alcance) | r00 | Reescritura de las 3 subsecciones desde TM/00-tesis/cap. 3; objetivos alineados con cap. 3; Formulacion intacta | 0/0 en alcance (0/3 archivo, fuera de alcance) | — | 0/3/5 (subsecciones) | 62 | `redaccion/.build/etapas/introduccion-r00.pdf` |
| 2026-09-29 | introduccion (3 subsecciones) | r01 | 25 aplicados, 3 parciales, 2 escalados; titulos de Obj 1 y 4 cambiados, cronologia retirada, McLaren fuera | 0/0 en alcance | 0/7, 1/15, 1/5 | 0/3/6 (subsecciones) | 64 | `redaccion/.build/etapas/introduccion-r01.pdf` |
| 2026-09-30 | introduccion (3 subsecciones) | r02 | 18 aplicados, 1 escalado; titulo Obj 1 = compuerta del autoencoder, GAP del cap. 3 replicados, contribucion no evaluada declarada | 0/0 en alcance | 0/6, 0/10, 0/2 | 0/4/9 (subsecciones) | 65 | `redaccion/.build/etapas/introduccion-r02.pdf` |
| 2026-09-30 | introduccion (3 subsecciones) | r03 | 7 aplicados, 1 parcial, 2 escalados; limitaciones sin recuento cerrado, "tareas" para exclusiones, dismorfismo sacro | 0/0 en alcance | 0/5, 0/4, 0/0 | 0/5/14 (subsecciones) | 67 | `redaccion/.build/etapas/introduccion-r03.pdf` |
| 2026-09-30 | introduccion (3 subsecciones) | r04 | 13 aplicados, 0 escalados en alcance; parrafos divididos y repeticiones quitadas, protocolo fisico en futuro, conteos 11/34 y 7/57 | 0/0 en alcance | 0/0, 0/10, 0/2 | 0/5/16 (subsecciones) | 67 | `redaccion/.build/etapas/introduccion-r04.pdf` |
| 2026-09-30 | introduccion (3 subsecciones) | r05 | 11 aplicados, 1 rechazado; salvedades dichas una vez, parrafos <= 7 oraciones, resultado del Obj 1 sin mecanismo; TOPE | 0/0 en alcance | 0/1, 0/11, 0/0 | 0/5/16 (subsecciones) | 67 | `redaccion/.build/etapas/introduccion-r05.pdf` |
