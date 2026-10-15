# Auditoria de trazabilidad — introduccion — r07

Alcance: `overleaf/secciones/introduccion.tex` completo (l. 1-90). Encargo: `redaccion/ENCARGO_2026-10-15.md`
§introduccion (retirar el `\GAPDEC` de la contingencia, dar el resultado de prueba de v1, actualizar el `\GAPDATO`
del modelo; no reescribir el encabezado, DESFASADO por #126). Los hallazgos del encabezado (l. 3-11) se reportan para
la autora; el redactor decide si caen dentro del encargo.

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; 00T = `docs/00-tesis.md`;
DEC = `docs/01-decisiones.md`; DEC15 = entrada DEC 2026-10-15 (l. 2559-2634); IMP = `docs/04-implicancias.md`;
EXP3 = `experiments/objetivo3/EXPERIMENTOS.md`; RP1 = `experiments/objetivo3/resultados_prueba_v1.md`;
P1C = `experiments/objetivo1/p1_compuerta.md`.

No existe respuesta a r06. El texto de l. 46-90 es el mismo que audito r06, asi que sus hallazgos siguen vigentes
y se re-reportan (no hay RECHAZADO que respetar). Lo nuevo de esta ronda es DEC15: el punto 13 retira la marca de la
contingencia (#90), el punto 15 clasifica el desenlace de v1, el punto 9 fija la pose de E-A2, el punto 2 fija la
cabeza y el punto 5 resuelve donde se mide la costura. Varios hallazgos de r06 cambian de base o de correccion por eso
(T06, T07; el T07 de r06 queda resuelto por DEC15 punto 5 y no se re-reporta).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-2 | l. 48, oracion 5 | "un margen $[-\Delta, +\Delta]$, aún sin medir" | C3 l. 377, 379 ("$\Delta = 196.3$~HU", medido en validacion); 00T l. 157; RP1 l. 7, 14; IMP #175; DEC15 punto 21 (196.3 / 6.1 vigentes) | Patron PAT-19 reincide (y PAT-122). La prosa niega una cifra medida, fijada y corregida en DEC. Persiste de r06 (T01), sin respuesta | "... cae entero en el margen $[-\Delta, +\Delta]$, con $\Delta = 196.3$~HU medido en pacientes de validación (Sección~\ref{sec:ap-analisis})" |
| T02 | alta | G-T4, OC-3 | l. 56, oraciones 1 y 4 | "prevé ejecutar ... el protocolo de Peters et al. sobre las poses del muestreador ... según el plazo" | DEC15 punto 9 ("E-A2 usa el eje del corredor para aislar la apariencia de la colocacion ... y por el coste del protocolo fisico"); DEC15 punto 13 (#90 CERRADA por ejecucion); IMP #90 (cabecera l. 6464, CERRADA 2026-10-14); C3 l. 377; RP1 l. 10-14 (n = 13, ya corrido) | Patron PAT-11 reincide; PAT-116 en la oracion 4 ("Si alcanza la equivalencia ... es lo que pone a prueba"), condicional sobre un resultado ya obtenido. Tres errores: (a) se ejecuto, no "se prevé"; (b) sobre el eje del corredor sin perturbar, no sobre las poses del muestreador, y ahora una decision de la autora lo dice expresamente; (c) "según el plazo" invoca la contingencia que DEC15 punto 13 retira. Las poses del muestreador solo entran en un exploratorio con el sintetizador, sin el protocolo fisico (DEC15 punto 9) | "El protocolo de Peters et al. se ejecutó como contraste primario de la apariencia sobre el eje del corredor, sin perturbar, en los 13 pacientes de prueba sin metal, para aislar la apariencia de la colocación, que evalúa el Objetivo~2 (Sección~\ref{sec:ap-brazos})." La oracion 4 queda como pregunta del diseno y remite al resultado (T06) |
| T03 | alta | OC-2, G-T4 | l. 90, `\GAPDATO` final | "no existe aún resultado del Objetivo~3 porque el modelo final no está elegido" | DEC 2026-10-11 (3) punto 1 (`run04_mejor`, paso 16 500); DEC 2026-10-14 (2) punto 1 ("la comparacion principal frente a Peters sigue siendo run04"), punto 2 (v2 exploratoria, sin ganador en prueba); RP1 l. 14, 23; DEC15 punto 15; 00T l. 160 | Patron PAT-122 reincide. El GAP niega dos hechos decididos: el modelo esta elegido y la prueba de v1 esta evaluada (TOST frente a Peters Ti, n = 13: -301.0 HU, IC90 [-477.0, -124.9], $\Delta$ = 196.3; Wilcoxon de cordura p = 0.000122). Lo que falta de verdad es el contraste de realismo (RP1 l. 42-45: "no hay script") y la prueba de la version 2 (EXP3 l. 40, `a20_v2` sin correr) | Prosa con el resultado (T06) y, como marcas: `\GAPDATO{evaluación del contraste de realismo sobre la partición de prueba, que no tiene script}` y, si se nombra la version 2, `\GAPDATO{evaluación en prueba de la versión 2, exploratoria y posterior}` |
| T04 | alta | G-T4, OC-3 | l. 90, ultima clausula y `\GAPDEC` | "su comparación de equivalencia frente al protocolo físico depende del plazo \GAPDEC{...}" | DEC15 punto 13 ("se retiran las marcas; #90 CERRADA por ejecucion"); IMP #90 l. 6464; ENCARGO l. 70 | Patron PAT-11 reincide. La marca pregunta por una decision que la autora ya tomo y retiro; la prosa afirma una dependencia que ya no existe. Persiste de r06 (T04) | Retirar la clausula y el `\GAPDEC`. Actualizar MAPA l. 24 ("1 \GAPDEC (#90)" pasa a 0) y la fila de la marca en la tabla de GAP |
| T05 | alta | G-T4, E-P3 | l. 68, oracion 4 | "en las fuentes revisadas las placas y los demás tornillos no tienen ninguna de las dos" | DEC 2026-10-08 punto 27 (lo afirma); fichas `han2019atlasplanning` (corredores AIIS-PSIS, rama pubica superior e iliosacro S1/S2 planificados por volumen) y `goerres2017planning` ("three screw trajectories (Superior pubic ramus, AIIS to PSIS, ...)"); IMP #180 (ABIERTA) | Dos fuentes del repositorio discrepan: la exclusividad del corredor medible por volumen la contradicen dos fichas leidas despues de la decision. La mitad "distribucion clinica de grados" se sostiene. Afin a PAT-148. Persiste de r06 (T05) | Acotar: "Es el único implante con una distribución clínica publicada de grados de brecha en las fuentes revisadas; otros tornillos pélvicos tienen corredores planificados sobre cada volumen \cite{goerres2017planning,han2019atlasplanning}, pero sin esa distribución." Escalar a la autora (#180 ABIERTA, DEC pto 27 suyo) |
| T06 | media | G-T4, OC-2 | l. 48, oracion 5 | "solo se concluye equivalencia si el intervalo ... cae entero en un margen" | DEC15 punto 15 (tres desenlaces: equivalencia, no equivalencia, no concluyente; direccion si el IC90 excluye 0; "Para v1: `run04_mejor` = no concluyente con diferencia significativa a la baja"); RP1 l. 14, 27-29 | Patron PAT-136 reincide. La regla esta incompleta frente a la decision vigente: da solo la condicion de equivalencia y calla los otros dos desenlaces, que DEC15 ya fija. Al anadir el resultado (encargo), el lector necesita la categoria. El `\GAPDEC` que r06 (T06) proponia ya no corresponde: la decision existe. #177 sigue ABIERTA, pero DEC15 decide la clasificacion (BITACORA §2, 2026-09-29: DEC que resuelve una implicancia abierta se redacta como decidida) | "... cae entero en el margen; si cae entero fuera, no hay equivalencia, y si cruza un límite, el resultado no es concluyente." Y el resultado: "En prueba, la diferencia media fue de $-301.0$~HU (IC del 90\,\% de $-477.0$ a $-124.9$~HU): el intervalo cruza el límite inferior, de modo que el resultado no es concluyente, con el sintetizador significativamente por debajo del protocolo físico con titanio." Sin interpretar el porque (#177) |
| T07 | media | G-T4, OC-2 | l. 90, oracion 2; l. 39 | "la de síntesis es el cilindro paramétrico liso" | DEC15 punto 2 ("la sintesis usa el tornillo con cabeza congelado el 2026-10-09; se declara desviacion de D3"); C3 l. 226 ("cilindro paramétrico liso con cabeza") | Patron PAT-20 reincide. Lo que se sintetiza lleva cabeza, y ahora una decision lo declara como desviacion; la introduccion describe la mascara sin cabeza en el unico lugar donde la caracteriza. Sube de baja (r06 T15) a media porque la fuente es ya una decision | "la de síntesis es el cilindro paramétrico liso, con cabeza (Sección~\ref{sec:geometria})" |
| T08 | media | G-T4, OC-3 | l. 88, oracion 4 | "la comparación ... no puede mostrar si el sintetizador reproduciría las rayas más allá de la banda" | DEC 2026-10-13 punto 1 ("Diagnostico D1/D2: en tornillos la banda de 12 mm alcanza") y punto 3 ("D1 con piezas tamano tornillo muestra que la banda de 12 mm alcanza"); C3 l. 210, 250 | La limitacion es cierta, pero calla una medicion que una decision de la autora ya registra y que la acota para tornillos. Sube de baja (r06 T18) a media: la fuente es DEC. Afin a PAT-27 (ERRADICADO) | "... más allá de la banda, aunque en piezas del tamaño de un tornillo el artefacto real medido no sobrepasa los 12~mm (Sección~\ref{sec:v2})" |
| T09 | media | E-R6 | l. 5, oracion 2 | "reducir la calidad de las imágenes utilizadas por los modelos de segmentación \cite{selles...,xie...}" | `selles2024marreview`, "bright and dark streaking artifacts that disguise anatomical structures" (Sec. 1, p. 1); `xie2024implantsegmentation`, "the common threshold method often fails to accurately segment metals" (Abstract) | Xie et al. tratan de segmentar el metal, no de la calidad de imagen para segmentar anatomia. Persiste de r06 (T08); encabezado fuera del encargo (#126) | "... ocultar los límites de las estructuras anatómicas \cite{selles2024marreview}"; Xie et al. solo si se dice lo que reportan |
| T10 | media | G-T4, E-R6 | l. 5, oraciones 3-4 | "endurecimiento del haz, la escasez de fotones y las inconsistencias ... durante la reconstrucción" | `selles2024marreview`, "Beam hardening, photon starvation, scattering and edge effects are the main contributors" (Sec. 1, p. 1); TM l. 56 (`deman1999`) | Sin `\cite` aunque hay ficha; la lista no coincide con la fuente; "escasez de fotones" no es el termino fijo ("inanición de fotones", E-T1). Persiste de r06 (T09) | "Su formación se atribuye al endurecimiento del haz, la inanición de fotones, la dispersión y los efectos de borde \cite{selles2024marreview}, y De Man et al.~\cite{deman1999} aíslan esos mecanismos modificando el sinograma." |
| T11 | media | G-T4 | l. 9, oraciones 4-5 | "Los modelos de difusión latente reducen el costo ... mientras que ControlNet permite" | 00T l. 103-105; DEC 2026-09-19 pto 2; `CLAUDE.md` raiz; IMP #126 (ABIERTA) | Contenido retirado como contexto habilitante del metodo (el parrafo siguiente abre "A partir de esta necesidad"). Las citas sostienen lo que dicen. Persiste de r06 (T10) | Presentarlas como formulacion inicial descartada por el Objetivo 1 (remision a l. 46) o retirarlas; decision dentro de #126 |
| T12 | baja | G-T4 | l. 3, oracion 1; l. 7, oracion 4 | "relevante para el análisis de lesiones, la reconstrucción tridimensional y la planificación" | ficha `liu2021ctpelvic1k`; TM l. 46 | Sin fuente para los tres usos; "limita el desarrollo de modelos robustos" es inferencia sin marca. Persiste de r06 (T11) | Acotar a TM l. 46 y redactar l. 7 como lectura propia |
| T13 | baja | E-R6 | l. 9, oracion 5 | "condiciones espaciales, como mapas de segmentación o máscaras" | ficha `zhang2023controlnet` ("Canny edges, Hough lines, user scribbles, human key points, segmentation maps") | "Máscaras" no figura en la ficha. Persiste de r06 (T12) | "como bordes, mapas de segmentación o poses" |
| T14 | baja | G-T4 | l. 48, oracion 5 | "el intervalo de confianza del 90 % de la diferencia pareada" | C3 l. 377 ("del IC del 90\,\% de la diferencia media pareada"); RP1 l. 12 | Falta "media". Persiste de r06 (T13) | "de la diferencia media pareada" |
| T15 | baja | G-T4 | l. 77, oracion 3 | "área transversal mínima de la zona segura de 222 mm² ... frente a 346" | `gardner2010safezones`, "222 mm2 [SD, 67] versus 346 mm2 [SD, 71]" (p. 624) | Son medias de grupo. Persiste de r06 (T14) | "un área transversal mínima media de ..." |
| T16 | baja | G-T4, OC-2 | l. 90, oraciones 2 y 5 | "el diámetro de los tornillos medidos"; "el tercero, con la razón entre tipos de parche" | C3 l. 228 ("9 de 57 objetos metálicos"); C3 l. 226 ("0.62 frente a 1.40 ... la primera razón se midió en el conjunto anterior a los retiros"); BITACORA §2 (2026-09-29, "objetos metálicos alargados") | El recuento de la auditoria es de objetos metalicos, no de tornillos; la razon del tercero lleva en C3 una condicion que aqui se pierde (PAT-31). La medida del segundo ya tiene base (DEC15 punto 5, E-A2 en los dos brazos), sin resultado aun | "la fragmentación y el diámetro de los objetos metálicos medidos en la auditoría"; "... con la razón entre tipos de parche, medida antes de los últimos retiros" |
| T17 | baja | OC-2 | l. 86, oracion 2 | "14 salieron conformes y 2 fallaron con las dos variantes" | C3 l. 111 (`\GAPDATO` de la sensibilidad sin los dos casos); DEC 2026-10-08 pto 22 | El tramo resumido lleva un GAP en C3 que aqui no aparece (BITACORA §2, 2026-09-30). Persiste de r06 (T16) | "... 2 fallaron con las dos variantes y su sensibilidad está pendiente (Sección~\ref{sec:corredor})" |
| T18 | baja | G-T4 | l. 80, oracion 3 | "La comparación con el protocolo físico es la que puede contradecirlo" | RP1 l. 14; DEC15 punto 15; IMP #177 (ABIERTA en su lectura) | Patron PAT-116 reincide: el modal se refiere a una comparacion ya ejecutada y clasificada, sin decirlo, y la remision lleva a limitaciones que hoy dicen "depende del plazo" (T04). No debe pasar a "lo contradijo": la lectura del porque sigue abierta (#177) | "La comparación con el protocolo físico, ya ejecutada y no concluyente (véanse las limitaciones), es la que puede contradecirlo." |
| T19 | baja | OC-5 | fuentes, no el texto | TM y EXP3 sin el resultado de prueba de v1 | TM l. 98 (aun "a non-conclusive equivalence result is a possible and reportable outcome"; grep sin "301" ni "196.3"); EXP3 l. 84 (`a24` "LISTO, probado con datos de juguete"), l. 83 (`a23` "resumen PENDIENTE", ya hecho en RP1), l. 40 (`a20_v2` "POR CORRER", abortado segun DEC15); 00T l. 153-163 si lo trae | Patrones PAT-138 y PAT-158 reinciden. OC-5 pide las cifras propias de TM o `EXPERIMENTOS.md`; las del encargo solo estan en 00T, C3, RP1 y DEC. El texto puede usarlas con esa fuente, pero las dos fuentes nominales quedan atras | Avisar a la autora: actualizar TM (regla 4 raiz, solo por pedido) y EXP3 (estado CORRIDO de `a24`, resumen de `a23` en RP1, estado de `a20_v2`). Sin efecto sobre el texto de esta ronda |

Conteo: alta = 5 (T01-T05), media = 6 (T06-T11), baja = 8 (T12-T19).

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l. 3 | Segmentacion osea pelvica relevante para lesiones, reconstruccion 3D, planificacion | sin fuente; TM l. 46 mas acotado | no (T12) |
| l. 3 | El desempeno depende de que el entrenamiento represente las variaciones | TM l. 46 | si |
| l. 3 | Fracturas, protocolos y metal; metal una de las mas dificiles \cite{liu2021ctpelvic1k} | `liu2021ctpelvic1k`, "bone fractures, low dose, metal artifacts" (Abstract); "the challenge of the metal artifacts is the most difficult to handle" (Introduction, p. 2) | si |
| l. 5 | Tornillos, placas, protesis; alta atenuacion; bandas oscuras, regiones brillantes, rayas | `selles2024marreview`, "observed as dark or bright streaks in line with the edge of the metal" (Sec. 1, p. 1) | si |
| l. 5 | Ocultan limites anatomicos \cite{selles...} | `selles2024marreview`, "disguise anatomical structures" (Sec. 1, p. 1) | si |
| l. 5 | Reducen la calidad para modelos de segmentacion \cite{xie...} | `xie2024implantsegmentation` (segmentacion del metal) | no (T09) |
| l. 5 | Mecanismos: endurecimiento, escasez de fotones, inconsistencias de reconstruccion | `selles2024marreview` (lista distinta), sin `\cite` | no (T10) |
| l. 5 | Reproducir el artefacto exige dominio de proyeccion | TM l. 56 (`deman1999`), sin cita en el texto | no (T10) |
| l. 7 | 1 184 volumenes; 75 con artefacto metalico | `liu2021ctpelvic1k`, "including 1, 184 CT volumes", "including 75 CTs with metal artifacts" (Introduction, p. 2) | si |
| l. 7 | 1 109 sin metal y 14 con metal anotados; 61 sin anotar | `liu2021ctpelvic1k`, "annotations for 1109 metal-free CTs and 14 metal-affected CTs"; "remaining 61 ... left unannotated" (p. 3) | si |
| l. 7 | Los 61 no se usan en el entrenamiento supervisado original | `liu2021ctpelvic1k`, "CLINIC-metal is taken off in our supervised training phase" (Tabla 1, p. 3) | si |
| l. 7 | Representacion reducida limita modelos robustos | inferencia sin marca | no (T12) |
| l. 9 | El aumento convencional no modela el implante | razonamiento propio | parcial |
| l. 9 | Difusion aprende distribuciones y sintetiza imagenes medicas \cite{kazerouni...} | `kazerouni2023diffusionsurvey` (Sec. 3, p. 7) | si |
| l. 9 | Difusion latente reduce el costo \cite{rombach...} | `rombach2022latentdiffusion` (Abstract, p. 1) | si (contexto retirado: T11) |
| l. 9 | ControlNet incorpora condiciones espaciales, mapas o mascaras \cite{zhang2023controlnet} | `zhang2023controlnet` (§1, p. 2); "mascaras" sin fila | parcial (T11, T13) |
| l. 11 | Sintesis de tumores evaluada en tarea posterior \cite{chen2024tumorsynthesis} | `chen2024tumorsynthesis`, "develop an AI model to detect and segment real tumors" | si |
| l. 11 | Este trabajo examina plausibilidad antes que utilidad | DEC 2026-10-08 pto 26 | si |
| l. 13 | Cadena de dos componentes; tornillo y artefacto local en TC sin implante | C3 l. 9, 15; 00T l. 71-73 | si |
| l. 13 | Muestreador propone pose 3D en el corredor medido | TM l. 78; C3 l. 15 | si |
| l. 13 | Sintetizador en dominio de imagen, sin latente ni proyeccion | TM l. 79; DEC 2026-09-19 pto 2 | si |
| l. 13 | Generacion restringida a $M$ y banda; resto copiado | TM l. 79; C3 l. 196 | si |
| l. 15 | Coherencia fisica y quirurgica, no utilidad | 00T §Fuera de alcance 1 | si |
| l. 15 | Grados de brecha frente a distribuciones clinicas publicadas | TM l. 78; C3 `sec:sap` | si |
| l. 15 | Metricas del protocolo publicado, frente a ese protocolo y a copia y pegado | TM l. 62, 80; C3 l. 377 | si |
| l. 15 | Compuerta previa sobre la representacion de los HU | TM l. 77; C3 l. 87 | si |
| l. 17 | Orden del documento | `overleaf/CLAUDE.md` §Estructura | si |
| l. 21 | Pregunta de investigacion | TM l. 62; DEC 2026-10-08 pto 24 | si |
| l. 28 | Cuatro objetivos; 2 y 3 componentes; 1 previo; 4 sin variable dependiente | C3 l. 13; BITACORA §2 (introduccion-r01) | si |
| l. 32 | Objetivo general; osteosintesis; corredor; multiventana | TM l. 74, 77, 78; `CLAUDE.md` raiz | si |
| l. 32 | Unico implante: tornillo transiliaco-transsacro | IMP #130 (decision 2026-10-04); TM l. 117 | si |
| l. 37 | Compuerta; MAE < 25 HU en hueso | TM l. 77; DEC 2026-09-15 (2); C3 l. 87 | si |
| l. 37 | Autoencoder comprime a un latente \cite{rombach...} | `rombach2022latentdiffusion` (Abstract) | si |
| l. 37 | Seis combinaciones; 34 pacientes de prueba; aprueba si alguna cumple | C3 l. 87; P1C l. 18-25; IMP #156 ("La compuerta preinscrita se ejecuto con 34 y no se reescribe"; sensibilidad sin `0053` NO-GO igual) | si |
| l. 39 | Tornillo que cruza las dos sacroiliacas; cilindro parametrico rigido | TM l. 117; C3 l. 123 | si (cabeza: T07) |
| l. 39 | Marco de Kaiser et al.; viabilidad = calibre + holgura radial | C3 l. 107 | si |
| l. 39 | Grado de brecha: escala ordinal de cuatro niveles | TM l. 52; C3 `sec:sap` | si |
| l. 39 | Referencia clinica: series navegada y convencional de Zwingmann et al. en S1 | TM l. 52, 78 | si |
| l. 39 | W1 = suma de diferencias absolutas de las acumuladas | C3 ec. `eq:w1` | si |
| l. 41 | *Inpainting* 2.5D en dominio de imagen | TM l. 79; C3 l. 196 | si |
| l. 41 | $G = M \cup B_\delta$; banda de ~12 mm; rayas y zonas oscuras fuera del metal | TM l. 79; C3 l. 210 | si |
| l. 41 | Comparacion con copia y pegado, protocolo fisico y observaciones reales | C3 l. 404 (tabla); DEC 2026-10-08 pto 11 | si |
| l. 43 | SAP unica metrica propia; 7.0 mm y 1 mm; solo grados comparados | DEC 2026-10-08 ptos 14, 16 | si |
| l. 43 | Metricas de Peters et al.; disenadas para MAR; inversion | DEC 2026-10-08 ptos 10, 23; TM l. 80 | si |
| l. 46 | Compuerta para latente + ControlNet; veredicto negativo; Obj 3 reformulado; regla intacta | TM l. 77, 79; C3 l. 87 | si |
| l. 46 | Autoencoder de TC examinado despues con la misma regla | TM l. 77; C3 l. 91 | si |
| l. 46 | Ida y vuelta sin autoencoder: 0.00 HU en dos codificaciones, 21.80 HU en la tercera, n = 34 | P1C l. 33-38 | si |
| l. 46 | Arcoseno hiperbolico en coma flotante de 32 bits | DEC 2026-10-08 pto 1; C3 l. 196 | si |
| l. 48 | Regla del Obj 1 escrita tras exploracion, antes de la prueba que decide; 25 HU anterior | DEC 2026-09-15 (2); C3 l. 74 | si (PAT-13 sin reincidencia) |
| l. 48 | Obj 2 sin regla de decision; lectura contra la distancia entre series | DEC 2026-10-08 pto 17 | si |
| l. 48 | Obj 3: equivalencia si el IC 90 % cae en $[-\Delta, +\Delta]$ | C3 l. 377; DEC15 punto 15 | parcial (T06, T14) |
| l. 48 | $\Delta$ "aún sin medir" | C3 l. 379 (196.3 HU); DEC15 punto 21 | no (T01) |
| l. 48 | Copia y pegado sin rayas por construccion; control de cordura; no cuenta a favor | C3 l. 377; DEC15 punto 12 (degeneracion declarada) | si |
| l. 48 | Obj 4 de definicion; controles de identidad, monotonia y resolucion | DEC 2026-10-08 pto 23 | si |
| l. 52 | 14 de 75 anotados, 61 sin anotar | `liu2021ctpelvic1k` (p. 3) | si |
| l. 52 | Motivacion de aumento de datos; utilidad no medida; razon de la coherencia antes | `CLAUDE.md` raiz; 00T §Fuera de alcance 1; DEC 2026-10-08 pto 26 | si |
| l. 54 | Ninguno de los tres enfoques produce poses y apariencia a la vez | TM l. 54 | si |
| l. 54 | Peters et al.: colocacion aleatoria; manual impracticable; "meaningful locations" sin regla | `peters2025hybrid` (Discussion, p. 9) | si |
| l. 54 | Liu et al. optimizan una unica trayectoria | `liu2025pipeline` (Sec. III-D.3, p. 11) | si |
| l. 54 | Zwingmann et al.: distribuciones distintas por tecnica; lectura propia | C3 `sec:sap`; BITACORA §2 | si |
| l. 56 | Se preve ejecutar Peters sobre poses del muestreador, segun el plazo | DEC15 puntos 9 y 13; IMP #90 CERRADA; RP1 | no (T02) |
| l. 56 | Peters necesita proyecciones por pose, 2D de una fila, metal fractal | DEC 2026-10-08 pto 25; `peters2025hybrid` | si |
| l. 56 | La equivalencia es pregunta del Obj 3, no premisa | DEC 2026-10-08 pto 25 | si (PAT-116: T02) |
| l. 58 | De Man et al.: endurecimiento, dispersion, ruido, EEGE; rayas que irradian | `deman1999` (Conclusiones, p. 695; Sec. III-D, p. 694) | si |
| l. 58 | CLAIM, DiffTumor, LGESynthNet acotados a mascara; DiffBoost desde ruido | TM l. 48; fichas `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`, `zhang2025diffboost` | si |
| l. 60 | Xie et al.: el umbral cubrio el implante en exceso, en cortes simulados | `xie2024implantsegmentation`, "The mask shape obtained by threshold segmentation covered the ground truth" (Abstract) | si |
| l. 60 | Objetos alargados por umbral fragmentados en la cohorte | C3 l. 228 (9 de 57) | si |
| l. 60 | Entrenamiento con mascaras umbralizadas = desplazamiento; ningun brazo coloca geometria por umbral | C3 l. 226; C3 `sec:ap-brazos` | si |
| l. 62 | Sin precedente que fije con valor una banda fuera de la mascara | TM l. 54, 79; C3 l. 210 | si |
| l. 62 | Varias ventanas de HU vienen de MAR \cite{wang2025...,li2024} | fichas `wang2025adaptiveweighting`, `li2024` | si |
| l. 62 | Se reclama la combinacion, no cada pieza | DEC 2026-10-08 pto 30 | si |
| l. 64 | Distribucion de poses fijada antes de cualquier distancia; sin parametros de la referencia | TM l. 107; C3 l. 151 | si |
| l. 64 | Ninguna de las seis combinaciones bajo de 25 HU; saturacion del AE de TC ya superaba | P1C l. 20-25 (minimo 61.72); TM l. 77 (42.24 HU); IMP #156 (sin `0053`: NO-GO igual) | si |
| l. 68 | 178 de los 1 184 volumenes | `docs/02-datos.md` l. 136 (178 + union); `liu2021ctpelvic1k` | si |
| l. 68 | Tornillo parametrico rigido; implantes reales sin geometria | IMP #130; C3 l. 123 | si |
| l. 68 | Unico implante con corredor medible y distribucion clinica; placas y otros tornillos sin ninguna | DEC 2026-10-08 pto 27 frente a `han2019atlasplanning`, `goerres2017planning`; IMP #180 | no (T05) |
| l. 68 | Distribucion y marco de Kaiser de tornillos iliosacros; referencia externa | IMP #130 pto 3; `zwingmann2009navigated`; `kaiser2014dysmorphism` | si |
| l. 70 | Comparacion solo en S1; segundo corredor sin distribucion; eje medido | C3 l. 188; 00T l. 62-64 | si |
| l. 70 | \GAPDATO: preinscripcion y corrida en el segundo corredor | MAPA l. 65; `experiments/objetivo2/EXPERIMENTOS.md` (R2 en pausa) | si (GAP justificado) |
| l. 70 | Sintesis por parches; solo genera $G$ | C3 l. 196, 202 | si |
| l. 74 | Dice/HD95 fuera; 14 casos; disponibilidad local no verificada | 00T §Fuera de alcance 1; `liu2021ctpelvic1k` | si |
| l. 75 | Ablaciones a trabajo futuro, por tiempo | DEC 2026-10-08 pto 28 | si |
| l. 76 | XCIST preliminar sin estudio de metal \cite{wu2022xcist}; Peters valida contra fantoma | `wu2022xcist` (Validation, p. 9); `peters2025hybrid` (Abstract) | si |
| l. 77 | Gardner et al.: dismorfismo por radiografia, rasgos; 222 frente a 346 mm²; estudio previo sin diferencia | `gardner2010safezones` (p. 624, p. 628) | si (T15: medias) |
| l. 80 | Supuesto 1 y De Man (no lineal, aislado en sinograma) | TM l. 56; `deman1999` (Sec. III-E) | si |
| l. 80 | La comparacion con el protocolo fisico puede contradecirlo | RP1; DEC15 punto 15 | parcial (T18) |
| l. 80 | Supuestos 2 (serie navegada = S1) y 3 (relacion mascara-artefacto) | C3 `sec:sap`; C3 l. 214 | si |
| l. 82 | 12 mm sin calibrar; limites de 2 mm via Smith et al.; equiespaciados | TM l. 52; `gertzbein1990`, `mirza2003`, `smith2006iliosacral`; C3 `eq:w1` | si |
| l. 82 | $\sigma$ = mitad de 5 mm; ~95 % dentro | DEC 2026-10-08 pto 19; `kaiser2014dysmorphism` (p. e120) | si |
| l. 84 | Referencia de pelvis fracturadas; receptoras no verificadas libres de fractura | TM l. 109, 121; C3 l. 66 | si |
| l. 84 | Corredor mas estrecho: grado 0 inalcanzable | C3 `sec:sap`; TM l. 109 | si |
| l. 84 | Cribado: 30 casos, 15+15, fractura en 20 de 30, 10 por grupo; medico sin especialidad | C3 l. 66; IMP #132, #136 | si |
| l. 86 | Revision de 16 casos: 14 conformes, 2 fallan con ambas; variante se mantiene | C3 l. 111; MAPA l. 55 | si (T17) |
| l. 86 | TotalSegmentator sin exactitud para S1 \cite{wasserthal2023}; control de nivel | `wasserthal2023` (NO ENCONTRADO EN EL PDF el Dice de S1); C3 l. 64 | si |
| l. 86 | Discordancia excluyo 11 de 34 y 7 de 57 | C3 l. 64; TM l. 123 | si |
| l. 86 | \GAPDATO: envolvente y canal sacro/foramenes | MAPA l. 105; C3 `sec:amenazas` | si (GAP justificado) |
| l. 88 | Reconstruccion no reportada; MAR del fabricante \cite{selles...} | `selles2024marreview` (Sec. 3.5, p. 6); C3 l. 46 | si |
| l. 88 | Protocolo validado en 2D y para MAR; adaptacion no hereda | C3 `sec:ap-brazos`; TM l. 50, 119 | si |
| l. 88 | $B_\delta$ trunca rayas lejanas; la comparacion no lo muestra | C3 l. 210; DEC 2026-10-13 ptos 1, 3 | parcial (T08) |
| l. 90 | Tres desplazamientos de dominio | C3 l. 226 | parcial (T07) |
| l. 90 | Medida de cada desplazamiento | C3 l. 226, 228; DEC15 puntos 4, 5 | parcial (T16) |
| l. 90 | \GAPDATO: modelo final no elegido; sin resultado del Obj 3 | DEC 2026-10-11 (3); DEC 2026-10-14 (2); RP1; DEC15 punto 15 | no (T03) |
| l. 90 | Equivalencia depende del plazo; \GAPDEC de la contingencia | DEC15 punto 13; IMP #90 CERRADA | no (T04) |
| l. 1-90 | Claves citadas existen en `overleaf/referencias.bib`; apellidos = primer autor (Liu, Peters, Kaiser, Zwingmann, De Man, Xie, Gardner, Smith) | `overleaf/referencias.bib` (verificado en r06; sin claves nuevas en r07) | si |
| l. 1-90 | Ninguna cita como sujeto gramatical sola (E-F3) | revision del texto | si |
| l. 1-90 | Sin fuentes de fabricante (P-EA1) | revision del texto | si (no aplica) |
| l. 1-90 | Contenido retirado: Dice/HD95 solo como exclusion; latente/ControlNet como historia (l. 37, 46) y contexto (l. 9); sin "31-60 %", BFC ni ISC | 00T §Fuera de alcance; `CLAUDE.md` raiz | parcial (T11) |
| l. 1-90 | Implicancias ABIERTAS: #177 no se afirma (no aparece); #180 contradice l. 68; #185, #186 no aparecen | IMP | parcial (T05) |
| l. 1-90 | GAP: 0 \GAPLIT, 3 \GAPDATO (l. 70, 86, 90), 1 \GAPDEC (l. 90) | `introduccion-r07-lint.md` (dato=3, dec=1) | si (conteo); T03, T04 sobre su vigencia |
| l. 1-90 | Patrones VIGENTES del dominio | PAT-11 (T02, T04), PAT-19 (T01), PAT-122 (T01, T03), PAT-136 (T06), PAT-20 (T07), PAT-31 (T16), PAT-116 (T02, T18), PAT-138 y PAT-158 (T19), PAT-148 afin (T05); PAT-13 (l. 48, 64), PAT-133, PAT-140, PAT-145, PAT-155, PAT-156, PAT-157 sin reincidencia en esta seccion | — |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una decision nueva que retira una contingencia no llega a la seccion que la enuncia, ni en prosa ni en GAP | G-T4, OC-3 | "su comparación de equivalencia ... depende del plazo \GAPDEC{...}" | PAT-11 |
| GAP de resultado propio que niega un modelo elegido y una evaluacion ya hechos | OC-2, G-T4 | "no existe aún resultado del Objetivo~3 porque el modelo final no está elegido" | PAT-122 |
| La seccion promete ejecutar sobre las poses del muestreador lo que una decision fija sobre el eje sin perturbar | G-T4 | "el protocolo de Peters et al. sobre las poses del muestreador" | nuevo (visto en introduccion-r06 y r07) |
| Regla de decision enunciada solo por su desenlace favorable cuando una decision ya fija los tres desenlaces | G-T4, G-C4 | "solo se concluye equivalencia si el intervalo ... cae entero" | PAT-136 |
| Limitacion redactada como abierta cuando una decision registrada ya la acota con una medicion propia | G-T4, OC-3 | "no puede mostrar si ... reproduciría las rayas más allá de la banda" | PAT-27 (reincide tras ERRADICADO) |
| Una seccion sin respuesta del redactor arrastra entera la ronda anterior, y las decisiones nuevas cambian la correccion de hallazgos viejos | G-T4 | T06 de r06 proponia un `\GAPDEC` que DEC15 punto 15 ya resuelve | nuevo |
