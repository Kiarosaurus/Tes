# Auditoria de trazabilidad — capitulo1 — r09

Archivo: `overleaf/secciones/capitulo1.tex` (137 lineas). Respuesta previa: `capitulo1-r08-respuesta.md` (sin hallazgos rechazados). Lint r09: PASA, 1 `\GAPDATO`, 1 `\GAPDEC`. Contexto nuevo: DEC 2026-10-15 (puntos 1, 13, 15, 16, 21) e implicancias #185 y #186 (ABIERTAS). No se abrieron PDF.

Todas las claves citadas existen en `overleaf/referencias.bib`. Los apellidos nombrados coinciden con el primer autor (Fay, Standring, Vallender, Schuirmann, Wilcoxon: un solo autor; Nichol y Dhariwal, Glover y Pelc: dos). Ninguna cita funciona sola como sujeto gramatical. No aparecen como vigentes Dice ni HD95, BFC ni ISC, el rango 31-60 %, la difusion latente ni ControlNet (las dos ultimas, solo como rutas descartadas, :116). #185 no toca este capitulo. De #186 solo afecta la regla del suelo, que DEC 2026-10-15 pto 1 ya decidio.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-2, OC-3 | `capitulo1.tex:48` | "Una regla preinscrita compara la perdida ... \GAPDEC{como expresar en HU la perdida ...}" | `docs/01-decisiones.md`:2571-2575 (DEC 2026-10-15 pto 1); `docs/04-implicancias.md`:12308-12311 (#186) | Reinciden PAT-19 y PAT-116. DEC 2026-10-15 pto 1 declara la regla del suelo **no aplicable**. Da tres razones: su desenlace depende del percentil (225.0 HU con p95 por paciente, 1.2 HU con mediana), ya era calculable antes de fijar una conversion y su rama de cambio de representacion esta bloqueada por el congelamiento. El texto la presenta como regla vigente y abre una `\GAPDEC` sobre una conversion que la decision ya no pide. Ademas, la premisa "fraccion sin unidad" que no se convierte a HU queda contradicha: la decision reporta la perdida en HU. | Retirar la `\GAPDEC`. Escribir el hecho decidido: la regla preinscrita del suelo se declaro no aplicable, porque su desenlace cambia segun el percentil (225.0 HU con el percentil 95 por paciente, frente a 1.2 HU con la mediana; margen de 196.3 HU) y su rama de cambio de representacion quedo bloqueada por el congelamiento. Remitir a `sec:amenazas` y a `sec:sintetizador`, que reportan la fraccion de las regiones de medicion bajo -1000 HU y la sensibilidad del TOST con las imagenes del protocolo fisico recortadas a -1000 HU (posterior y dirigida hacia la equivalencia). Si el marco teorico no debe llevar las cifras, basta la oracion sin ellas y la remision. Aviso para el orquestador: `capitulo3.tex`:198 tiene la misma `\GAPDEC` obsoleta, y la fila del suelo en `redaccion/MAPA.md`:61 debe pasar a CERRADO. |
| T02 | alta | G-T4, OC-2 | `capitulo1.tex:58` | "depende de una regla preinscrita cuyo desenlace aun no se conoce" | DEC 2026-10-15 pto 1 (`01-decisiones.md`:2571-2575) | Reinciden PAT-116 y PAT-122. El desenlace ya se conoce y depende del percentil, y la regla se declaro no aplicable. La oracion sostiene lo contrario. | Sustituir por: "La regla preinscrita para ese limite se declaro no aplicable (Seccion~\ref{sec:sintetizador})". Que concuerde con la nueva redaccion de :48, sin repetir las cifras. |
| T03 | media | G-T4 | `capitulo1.tex:132` | "La convencion bilateral adoptada es \emph{minlike}" | `docs/01-decisiones.md`; `docs/04-implicancias.md`:9037-9040 (#132, "Fisher bilateral"); `experiments/` (sin script ni registro de software); `fay2010two` | Se afirma una eleccion propia, que la tesis adopto minlike, y ningun registro la sostiene. DEC no la fija, #132 solo dice "Fisher bilateral", y en el repositorio no hay script ni nota que indique con que software o convencion se calcularon p = 1.000, 0.272 y 0.109. Fay sostiene la definicion y la conducta de `fisher.test` en `stats` 2.11.0, no que esta tesis la usara. Observacion del auditor: con 15 casos por grupo (n = N/2), la distribucion hipergeometrica condicional es simetrica, y las convenciones central y minlike dan el mismo valor p. El fondo no cambia, pero la eleccion queda sin rastro. | Opcion (a): la autora registra el software y la convencion con que se calcularon los valores p de #132, y el texto lo cita. Opcion (b): redactar "Para la version bilateral, este documento usa la convencion \emph{minlike} ..." como definicion de lectura, sin "adoptada", y anadir que con dos grupos de igual tamano las convenciones central y minlike coinciden. Esa observacion es una derivacion: si entra, se marca como lectura propia. |
| T04 | baja | G-T4 | `capitulo1.tex:130` | "puede no concluir ni equivalencia ni diferencia" | DEC 2026-10-15 pto 15 (`01-decisiones.md`:2615-2619) | DEC fija ahora tres desenlaces con nombre: equivalencia, no equivalencia y no concluyente. El IC90 que cruza un limite se llama "no concluyente" y puede llevar diferencia significativa, que es el caso de v1. "Ni ... ni diferencia" no coincide con esa taxonomia: un no concluyente puede tener diferencia. | "... esa comparacion puede quedar no concluyente, con el intervalo cruzando un limite del margen", con los terminos de DEC pto 15. La lectura de cada desenlace queda en el cap. 3. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :11-13, Fig. `fig:mt-conceptos` | Funcion del capitulo, orden y relacion de conceptos con objetivos | `capitulo3.tex` §Vision general, §Obj1, §Sintetizador, §SAP | si |
| :31 | Coeficiente de atenuacion, Beer-Lambert, supuesto monoenergetico | `kak2001book`, evidencia "Atenuacion exponencial", "Logaritmo medido", "Condicion monoenergetica" | si |
| :31 | Fuentes policromaticas y endurecimiento del haz | `kak2001book`, "Fuente medica real", "Definicion de beam hardening" | si |
| :31 | Sinograma y modelo espectral de CatSim | `deman2007catsim`, Sec. 2.1 | si |
| :31 | DukeSim aplica Beer-Lambert; Wang et al., cinco energias | fichas `abadi2019`, `wang2019cochlear` | si |
| :33 | Dos pasos de retroproyeccion filtrada | `kak2001book`, "Dos pasos de FBP" | si |
| :33 | De Man, CatSim y Karageorgos usan FBP; modelo de Radon monocromatico | fichas `deman1999`, `deman2007catsim`, `karageorgos2024ddpm`, `park2015ct` | si |
| :33 | Dominios; cohorte ya reconstruida; protocolo fisico por proyecciones | `docs/02-datos.md`; `capitulo3.tex` §Datos, §Apariencia | si |
| :35 | Formula HU; agua 0 HU, aire -1000 HU | `kak2001book`, "Formula HU", "Agua", "Aire"; `wu2022xcist` | si |
| :35 | Conversion con mu del agua dependiente de la energia | `wang2019cochlear`, Sec. 2.1 | si |
| :35 | Hueso >150 HU (Peters); metal 2500 HU (Wang, Li); cribado por HU | fichas `peters2025hybrid`, `wang2025adaptiveweighting`, `li2024`; `capitulo3.tex` §Datos | si |
| :35 | Mediana 0.42 de voxeles <=150 HU en mascaras sacras | `tesis/main.tex`:123; `experiments/objetivo2/maintex_cifras.md`:4, :17 | si |
| :37-42 | Ventana, saturacion, Ec. `eq:ventana` y canje rango/contraste | `wang2025adaptiveweighting`, Ec. 2; derivacion | si |
| :44 | Tres ventanas de Wang et al. en cascada | `wang2025adaptiveweighting` | si |
| :46 | Tres codificaciones; techos 2000 y 20 000 HU; asinh sobre [-1000, 20 000] | `tesis/main.tex`:77; `experiments/objetivo3/diseno_A.md`:209; `p1_compuerta.md` | si |
| :46 | `\GAPDATO` forma y parametros de asinh | `e6c_techo_lw.py`; `diseno_A.md`:209 da solo el rango, no la forma | si (GAP justificado) |
| :46 | Sintetizador: tercera codificacion, coma flotante de 32 bits, sin autoencoder | DEC 2026-10-08 pto 1 | si |
| :48 | Suelo comun de -1000 HU; error en hueso no ve la cola baja | DEC 2026-10-05 (suelo) pto 5; `capitulo3.tex`:198 | si |
| :48 | Margen 196.3 HU, modelo principal | DEC 2026-10-15 pto 21; `resultados_validacion_pose.md`:51 | si |
| :48 | Regla del suelo vigente y `\GAPDEC` de conversion a HU | DEC 2026-10-15 pto 1 (regla no aplicable; 225.0 / 1.2 HU) | **no (T01)** |
| :52 | Definicion de artefacto; categoria intermedia sin criterio numerico | `selles2024marreview` | si |
| :54-60 | Mecanismos segun Selles y De Man; rayas de todas las causas; borde | `selles2024marreview`, `deman1999` | si |
| :56 | Cupping y rayas (Park); razon 0.0001 arbitraria | `park2015ct`; `deman1999`, Sec. III-C | si |
| :58 | Inanicion de fotones; artefacto de ruido no lineal | `selles2024marreview`; `deman1999` | si |
| :58 | "Regla preinscrita cuyo desenlace aun no se conoce" | DEC 2026-10-15 pto 1 | **no (T02)** |
| :62 | Volumen parcial no lineal; una o varias discontinuidades; hueso, monocromatico | `glover1980nonlinear`; `deman1999` | si |
| :64 | Rayas fuera del implante; ancho de $B_\delta$ como convencion; supuesto del dominio de imagen | `deman1999`, `park2015ct`; `capitulo2` §Representacion; `capitulo3` §Amenazas | si |
| :66 | CatSim/XCIST y mecanismos modelados; protocolo fisico como comparacion | `wu2022xcist`, `deman2007catsim`; `capitulo3` §Apariencia | si |
| :68 | Tres metricas de Peters, umbral 150 HU, 5 % extremos, inversion definida | `peters2025hybrid`; DEC 2026-10-05 (3); DEC 2026-10-08 pto 10 | si |
| :68 | Streak amplitude como unico criterio primario del Obj. 3 | `capitulo3` §Apariencia; `diseno_A.md` §0 | si |
| :72 | Tile B/C, via percutanea, referencia clinica externa; dos nombres de tornillo | `zwingmann2009navigated`; #130 | si |
| :74 | Tornillo iliosacro, tres corticales; ala sacra caudal | `smith2006iliosacral`, `routt1997` | si |
| :74 | Cortical, ala, forámenes, platillos, articulacion SI | `standring2020grays` | si |
| :76 | Transiliaco-transsacro, superficie glutea; tolerancias de McLaren; umbral de Kaiser como convencion | `mclaren2021corridor`, `standring2020grays`, `kaiser2014dysmorphism`; #130; bitacora §2 2026-10-05 | si |
| :78 | Decubito supino y tres planos; navegacion 190 grados; TC posoperatoria | `routt1997`, `zwingmann2009navigated` | si |
| :80 | Zona segura y estructuras vecinas; dos conos de Gardner | `routt1997`, `gardner2010safezones` | si |
| :82 | Diametro maximo de McLaren; 10 mm heredado; holgura 1-2 mm sobre 6.3-8 mm | `mclaren2021corridor`, `kaiser2014dysmorphism`, `gardner2010safezones` | si |
| :82 | Medicion sobre mascaras de TotalSegmentator | `wasserthal2023`; `capitulo3` §Corredor | si |
| :84 | Marco de Kaiser; margen de 5 mm; techo de S1 vs platillo, no medido | `kaiser2014dysmorphism`; #138; `capitulo3` §Amenazas | si |
| :86 | Posicion ideal y grados 0-3 (<2, 2-4, >4 mm); protrusion fuera de envolvente | `smith2006iliosacral`; `capitulo3` §SAP | si |
| :88 | Escala angular sin grado 1; Zwingmann y SAP solo perforacion; Hinsche binaria | `smith2006iliosacral`; DEC 2026-10-08 pto 15; `hinsche2002fluoroscopy` | si |
| :90 | Escala ordinal; equiespaciado como convencion | derivacion de :86; `capitulo3` §SAP | si |
| :92 | SAP sin densidad; Arand, ala vs S1; trabajo futuro | DEC 2026-10-08 pto 14; `arand2019pelvicring` | si |
| :96-101 | Cadena de Markov, 1000 pasos, Ec. directa, calendario coseno, betas en (0,1) | `ho2020denoising`, `dorjsembe2024`, `zhang2025diffboost`, `nichol2021improved` | si |
| :103-108 | Perdida simplificada; U-Net (Ronneberger); arquitectura fijada | `rombach2022latentdiffusion`, `song2021ddim`, `ronnenberger2015unet`; DEC 2026-10-08 pto 2 | si |
| :110 | Prediccion $v$, reconstruccion de $x$, dominio de imagenes naturales | `salimans2022progressive`, "Prediccion de velocidad", "Prediccion de x desde v", "Dominio: NO ENCONTRADO" | si |
| :112 | Muestreo no markoviano determinista; 10-50 veces; 50 pasos | `song2021ddim`; DEC 2026-10-08 pto 4 | si |
| :114 | Dos vias de condicionamiento; ControlNet | `rombach2022latentdiffusion`, `dorjsembe2024`, `zhang2023controlnet` | si |
| :116 | Autoencoder; cuello de botella; MAE < 25 HU; veredicto negativo; ControlNet descartado | `rombach2022latentdiffusion`; `p1_compuerta.md`; `capitulo3` §Obj1 | si |
| :118 | RePaint, inpainting condicionado, LeFusion; el sintetizador no remuestrea | `lugmayr2022repaint`, `zhang2025lefusion`; DEC 2026-10-08 pto 4 | si |
| :120 | 2.5D, tres cortes, razon de computo; lectura propia sobre volumen parcial | DEC 2026-10-08 pto 3; `capitulo3` §Sintetizador | si |
| :124 | Tres tipos de resultados; unidades de analisis | `capitulo3` §Obj1, §Poses, §Apariencia | si |
| :124 | 13 valores pareados; uno de 14 sin eje | `capitulo3` §ap-sintesis; `EXPERIMENTOS.md`:63, :81 | si |
| :126 | W1 1D como integral de CDF; suma discreta; unidad grado; 1 y 3 | `vallender1974wasserstein`; derivacion | si |
| :128 | TOST de Schuirmann; IC 90 % con alpha 0.05 | `schuirmann1987comparison` | si |
| :130 | Wilcoxon pareada de una cola; algoritmo | `wilcoxon1945rankingmethods`; `capitulo3` §ap-analisis | si |
| :130 | TOST preinscrita y ejecutada como contraste primario | DEC 2026-10-15 pto 13 (#90 CERRADA); `capitulo3` §ap-analisis | si |
| :130 | Margen por semillas y replicas; 196.3 HU | DEC 2026-10-15 pto 21; DEC 2026-10-09 (4) | si |
| :130 | "Ni equivalencia ni diferencia" | DEC 2026-10-15 pto 15 | **parcial (T04)** |
| :132 | Remuestreo con reemplazo, percentiles, paciente como unidad | `efron1992bootstrap`; `capitulo3` §Obj1 | si |
| :132 | Fisher: margenes fijos y tablas compatibles | `fisher1935logic`, "Margenes fijos", "13 tablas posibles" | si |
| :132 | Minlike: suma de probabilidades <= observada | `fay2010two`, "Minlike suma resultados no mas probables" | si |
| :132 | `fisher.test` en `stats` 2.11.0 | `fay2010two`, "Version de stats evaluada", "fisher.test bilateral usa minlike" | si |
| :132 | Convencion minlike "adoptada" por esta tesis | sin registro en DEC, #132 ni `experiments/` | **no (T03)** |
| :132 | 15 casos por grupo; lectura sugerente | #132 (`04-implicancias.md`:9037) | si |
| :134 | Regla fijada antes de la prueba que decide; resultado exploratorio previo; tres decisiones post hoc del Obj. 2 | `capitulo3` §Amenazas; bitacora §2 2026-09-29 | si |
| :134 | Seis combinaciones, luego siete con el VAE de Guo et al.; veredicto negativo; no cambia el Obj. 3 | #91, #93; `guo2025maisi`; `capitulo3` §Obj1 | si |
| :136 | MAE vs RMSE; RMSE >= MAE; RMSE de MAR como orden de magnitud | derivacion; `capitulo2` §Representacion | si |
| global | Claves y primer autor de todas las citas | `overleaf/referencias.bib` | si |
| global | Contenido retirado (Dice/HD95, BFC/ISC, 31-60 %, difusion latente o ControlNet vigentes) | `docs/00-tesis.md`; busqueda en el `.tex` | si (ausente o descartado) |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una DEC nueva declara no aplicable una regla, y el texto y su GAP la siguen presentando como pendiente | G-T4, OC-2 | "regla preinscrita cuyo desenlace aun no se conoce" | PAT-116 / PAT-19 |
| Una eleccion metodologica propia ("adoptada") se toma de la ficha de una fuente sin registro de que la tesis la aplico | G-T4, E-R6 | "La convencion bilateral adoptada es minlike" | nuevo |
