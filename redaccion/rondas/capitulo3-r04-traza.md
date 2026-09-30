# Auditoria de trazabilidad — capitulo3 — r04

Entrada: `overleaf/secciones/capitulo3.tex` (tras r03), respuesta `capitulo3-r03-respuesta.md`, lint
`capitulo3-r04-lint.md` (0/0/4, PASA). En r03 no hubo RECHAZADOS. guia-9 quedo NO APLICADO por falta de fuente,
y el texto no afirma el motivo, asi que no se re-reporta. Los `\GAPDEC` escalados en r01-r02 (#127) tampoco. T01 a T06
de r03 quedaron aplicados y se verificaron contra su fuente (l.83, l.95, l.97, l.183, l.196, l.221, l.249).
Se comprobaron los 24 patrones VIGENTES de BITACORA §1 y se respetaron las decisiones de §2. En particular: una cifra de
DEC entra como hecho, "esta proxima a" sin factor, y "reviso" para el revisor clinico.

Se reabren dos puntos que r03 dio por buenos en l.119: T01 (nucleo = fuste) y T03 ("unica medicion", "sin avellanado").
Hay argumento nuevo: las fichas de `synthes_cannulated_65_73_guide` y `sayres2014comparison`, y la tabla de #97 en IMP,
contradicen la lectura que hace el texto. Por eso van como "Re-apertura".

Siglas: TM = `tesis/main.tex`; PRE = `experiments/objetivo2/preinscripcion_muestreador.md`; DAT = `docs/02-datos.md`;
DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; RES = `experiments/objetivo2/e9ts_resumen.md`;
E12 = `experiments/objetivo2/e12_sap_control.md`; E13 = `experiments/objetivo2/e13_sap.md`;
R1 = `experiments/objetivo2/r1_landmarks.md`; GRP = `experiments/exploration-3d/grupos.csv`;
SYN = `docs/literatura/synthes_cannulated_65_73_guide.md` (ficha de `synthes2003guide`).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | E-R6, G-T4 | capitulo3.tex:119 | "la guía técnica del fabricante (...), que declara que núcleo y fuste tienen el mismo diámetro" | SYN:120 (Nucleo: "NO ENCONTRADO EN EL PDF (solo cualitativo)"); SYN:182 ("dice que nucleo y fuste son iguales entre 6.5 y 7.3"); SYN:240-241 (la frase *"The core and shaft diameters are the same."* va justo despues de *"the thread and head diameters of the 6.5 mm cannulated screw are smaller"*, p. impresa 5) | Re-apertura: r03 lo dio por bueno sin leer SYN §7. Segun la ficha, la guia compara los tornillos de 6.5 y 7.3 mm: la rosca y la cabeza del 6.5 son menores, y nucleo y fuste son iguales en los dos calibres. No dice que el nucleo mida lo mismo que el fuste, y la ficha registra el diametro del nucleo como NO ENCONTRADO. La Tabla `tab:geometrias` del propio capitulo da 4.9 mm de fuste y 4.7 mm de nucleo \cite{gardner2015screw}, justo lo contrario de lo que se atribuye a Synthes. El patron PAT-6 reincide | "(...) el fuste de 4.8~mm que imprime la guía técnica del fabricante \cite{synthes2003guide}, la misma para los tornillos de 6.5 y 7.3~mm". Otra opcion: quitar la oracion subordinada. Si la autora sostiene la otra lectura, hay que releer la p. impresa 5 con `lector-papers` antes de mantenerla |
| T02 | media | G-T4 | capitulo3.tex:194 | "Los 8 mm son el mismo recorte (...); su razón es clínica y no numérica" | DEC D-O2.3 pto 4 (:1457-1460); `experiments/objetivo2/e9_corredor.py`:49-51, :77 (`RECORTE_EXTREMO_MM = 8.0`); PRE:91 | Con esta frase, la razon clinica parece justificar el valor de 8 mm. En DEC, esa razon (el tornillo entra y sale por la cortical del ilion) justifica que se recorten los extremos, y el texto ya la da en la oracion anterior. El codigo del corredor recorta por otro motivo: en los extremos la distancia la limita la propia salida por la cortical. Ninguna fuente justifica el valor 8.0. Leido asi, el texto le da al parametro una fundamentacion que no tiene | "Los 8~mm son el mismo recorte con que se excluyen los extremos al medir el diámetro del corredor (Sección~\ref{sec:corredor}), y su valor no tiene fuente publicada." Si la autora prefiere marcarlo: `\GAPDEC{justificación del valor de 8 mm del recorte de extremos}` y una fila en MAPA |
| T03 | baja | G-T4, E-R6 | capitulo3.tex:119 | "la única medición de las fuentes revisadas, 8.0 mm (...) sin avellanado" | IMP #97 (:6696: "`doublemedical_trauma_catalogue` tambien imprime 8.0"; listados de distribuidor 8.2); `sayres2014comparison` fila "Sin avellanado" (*"No countersink was used in attempt to minimize the incision size"*, Operative Technique, p. 33) | Re-apertura por dos motivos. (1) "Única" no se sostiene para el diametro: otro documento revisado, el catalogo de Double Medical, imprime tambien 8.0 mm. Lo unico que solo da Sayres es la altura. (2) "Sin avellanado" es una decision quirurgica de Sayres et al. en osteotomia de calcaneo y no una propiedad de la cabeza del tornillo. Asi redactado, el texto la presenta como parte de la geometria medida | "(...) toma el diámetro de 8.0~mm y la altura de 4.5~mm que reportan Sayres et al.~\cite{sayres2014comparison}, la única fuente revisada que da la altura; se modela sin avellanado (...)". Si se quiere conservar el avellanado, hay que decirlo como supuesto propio |
| T04 | baja | E-R6 | capitulo3.tex:119 | "que usa 7.3 mm solo en la rosca distal" | `zhu2022optimalposition` filas "Diametro de rosca (modelo FEA)" (*"thread diameter, 7.3 mm"*) y "Longitud de rosca (modelo FEA)" (*"thread length, 16 mm"*), 2.3, p. 1548 | La ficha da el diametro y la longitud de la rosca, pero no dice que sea distal. "Distal" es una inferencia plausible que la ficha no registra | "(...) que usa 7.3~mm solo en una rosca de 16~mm." |
| T05 | baja | G-T4 | capitulo3.tex:123 | "Tres parámetros no tienen fuente en la documentación del propio fabricante" | SYN:73 y :230 (*"316L stainless steel or titanium alloy (Ti-6Al-7Nb)"*, p. impresa 12) | El tercer parametro, la aleacion, si tiene fuente del fabricante: la guia publica las dos aleaciones, y el mismo parrafo la cita. El problema de la aleacion es que no queda determinada, no que falte la fuente | "Dos parámetros no tienen fuente en la documentación del propio fabricante, y un tercero no queda determinado por ella." Tambien sirve: "Tres parámetros quedan sin fijar por la documentación del fabricante" |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9 | Dos componentes separados; compuerta previa | TM:74-80; CLAUDE.md raiz | si |
| :13 | Cuatro objetivos; SAP es la unica metrica propia; el Obj 4 adopta el protocolo con sus nombres publicados | TM:80; DEC 2026-09-08 (BFC/ISC retiradas) | si |
| :13 | GAPDEC alineacion con la introduccion | IMP #126 ABIERTA | si (justificado) |
| :15 | Corredor medido; eje perturbado; M, B_delta, G; copia fuera de G | TM:79, :107 | si |
| Fig. pipeline | TotalSegmentator; marco de Kaiser; SAP frente a dos distribuciones; *inpainting* en imagen; copia y pegado y protocolo fisico; la compuerta descarto la ruta latente | TM:77-79, :98; DEC 2026-09-19 | si |
| :36 | Dice/HD95 fuera de alcance, por dos condiciones | TM:83, :127 | si |
| :36 | La publicacion anota 14 de los 75 de CLINIC-metal | `liu2021ctpelvic1k` (Tabla 1, p. 3); DAT:157-161 | si |
| :36 | 178 de 1 184; ablaciones diferidas | DAT:55; DEC 2026-09-17 B.1 | si |
| :38 | Compuerta ejecutada y negativa; Obj 2 ejecutado; GAPDATO sin muestra sintetica; rediseno posterior | TM:77, :96; IMP #116 act. (:8750-8753); DEC 2026-09-19 pto 2 | si |
| :42 | 1 184; 178; dataset6 103 y dataset7 75; correspondencia inferida | DAT:27-30, :55-63 | si |
| :44 | El articulo no reporta adquisicion ni reconstruccion; Selles | `liu2021ctpelvic1k` (NO ENCONTRADO); `selles2024marreview` (Sec. 3.3, 3.5); DEC 2026-09-17 C | si |
| :46 | Cribado > 2500 HU, un voxel, sin filtro de tamano; revision 3D de los 178; GAPDATO de la revision multiplanar | DAT:67-69, :104, :139; DEC 2026-09-11 (3) | si |
| :48 | SHA256 y huella por corte, mas observacion visual; 178 -> 168; 65/37/66; 179; 10; 1 | DAT:117-122, :134-137; GRP | si |
| :50 | Aislamiento estricto; particion por paciente estratificada; 34 de prueba; Obj 3 reutiliza; Obj 2 grupos 2 y 3 | TM:77, :115; DEC 2026-09-17 (3); DEC 2026-09-14 (2) (:724) | si |
| :52 | 103 -> 91 -> 72; 11 de 34; 7 de 57; 1 en el borde; 49; criterio del control de nivel | DEC 2026-09-14 (3) (:747-749); DEC 2026-09-14 (:642, :668-671); PRE §1 | si |
| :52 | GAPDATO cribado de fractura, 30 (15 + 15) | IMP #125 (:8729-8730); `r3_fractura_revisor.csv` sin veredictos (0/30) | si (justificado) |
| :54 | Cuatro funciones de los 65; tornillos fragmentados, por debajo del calibre y cambiantes entre adquisiciones | TM:117; DEC D1; DEC 2026-09-11 (3) (:623) | si |
| :58 | Compuerta obligatoria; regla fijada antes de la prueba que decide; exploracion previa sobre los 178, por encima del criterio | DEC 2026-09-17 B.3, (3); DEC 2026-09-15 (2) (:841) | si |
| :60 | Tres canales; VAE de SD 1.5; lectura sin la imagen original; 150 HU | DEC 2026-09-17 (3) (:1048-1050); `peters2025hybrid` (2.5, p. 5); `haneda2025aapm` (Sec. 2.3, p. 7) | si |
| :61-65 (Ec. MAE) | MAE por paciente en hueso | DEC :1051 | si |
| :67 | Sin umbral publicado; 20.2 / 12.3 / 12.74 HU; RMSE >= MAE | DEC 2026-09-15 (2) (:818-829); `karageorgos2024ddpm` Tabla I; `yun2026simulationdriven` Tabla 1; `peters2025hybrid` fila "NMAR calibrado a score 2" | si |
| :69 | 2 x 3; decodificador adaptado con codificador congelado; GAPDATO de los parametros del ajuste; ventanas de Wang; 20 000; arcsinh | DEC 2026-09-17 (3), D.1; `wang2025adaptiveweighting` (V-A-1, p. 2412); TM:77 | si |
| :71 | Media sobre 34 < 25 HU; alguna de seis; IC 95 %; marginal; orden a priori; No-Go -> Obj 3 no se ejecuta | DEC :1051-1057, :1065, :976-979 | si |
| :73 | B_delta descriptivo; Rombach | DEC 2026-09-17 C; `rombach2022latentdiffusion` (§1, p. 2) | si |
| :75 | Extension a Guo; cota por recorte | DEC 2026-09-19 pto 3; `guo2025maisi` | si |
| :79 | Referencia clinica definida (dos series); Ziran: 7-25 % y 140 % | `zwingmann2009navigated` (Results, pp. 1836-1837); `ziran2007fluoroscopic` (pp. 351-352) | si |
| :83 | Marco de Kaiser; regla de 5 mm; "este trabajo lee" h como radial = radio de 10 mm | `kaiser2014dysmorphism` (p. e120(2)); DEC 2026-09-11 (2) (:603-605) | si (T05 de r03 aplicado) |
| :85 | 0.42; TS 2.18.0 `total`; nnU-Net; limpieza 0.1 %; 104 estructuras; sin exactitud para S1 | TM:123; DEC 2026-09-14 (3); `wasserthal2023` filas 1a, 2d, 3e | si |
| :85 | Recorte = modelo previo de menor resolucion; por defecto 6 mm y alternativo 3 mm con `--robust_crop`; el primero es el principal | DEC 2026-09-14 (4) (:763-765); IMP #49 hallazgo 3 (:3938-3941; solo describe la herramienta; la eleccion la fija DEC); `experiments/objetivo2/ts_cohorte.md`:13 (`--roi_subset` usado) | si |
| :87 | Envolvente; diametro = 2 x distancia libre; GAPDATO algoritmo; semimaximo y 2500 HU; contraste aparte | DEC D-O2.3 (:1450-1452, :1467-1469); DEC 2026-09-14 (2), (3); IMP #121 | si |
| :89 | D >= d + 2 epsilon; epsilon 1-2 mm; lectura por lado propia; Kaiser; McLaren; 10 mm como convencion | DEC 2026-09-11 (2) (:590-601); `kaiser2014dysmorphism` (p. e120(7)); `mclaren2021corridor` (p. 2) | si |
| :91 | 9.5 (7.4-11.7); 65.3 / 23.6; 62.5 / 20.8; 29 y 27 de 72; limpieza hasta 5 %; post hoc; GAPDATO 16 casos | RES:16, :20; DEC 2026-09-14 (3), (4) (:770-771), (5); IMP #123 ABIERTA | si |
| :95 | Union lumbosacra; ninguna fuente revisada; GAPDATO de la heuristica | TM:121; R1:7-15 | si (justificado) |
| :95 | 69 pacientes de dataset6 clasificados sin objeto por la revision 3D; no coincide con el grupo 3 (66) | R1:4; DAT:127; DAT:137 | si (T01 de r03 aplicado) |
| :95 | Revisor clinico (cirujano, ORL), ciego, reviso S1 en cada paciente | R1:45 (sin revisar 0); TM:121 | si (T04 de r03 aplicado) |
| :97 | 65; 57 con las cinco referencias; 7 de 8 con crestas truncadas; 48 con S1 correcto; 29 sin contaminacion | R1:42, :46, :57-88 | si |
| :97 | 17 con tornillo; S1 correcto en todos; 3 contaminados; GAPDEC 61 de 61; crestas sin revision clinica | TM:121; IMP #124 ABIERTA; DEC 2026-09-17 E | si (justificado) |
| :101 | Nominal = rosca; mas seccion que 4.91 mm; nominal solo para viabilidad | TM:117; IMP #97 (:6655-6668) | si |
| Tab. geom. | 6.5-8.0; 6.3-8; 4.91; 4.8; 4.9 y 4.7; 7.0; 4.91 y 7.3 de sensibilidad | `gardner2010safezones` (p. 624); `kaiser2014dysmorphism`; DEC D3; SYN:70; `gardner2015screw` (p. 42); `zwingmann2009navigated` (p. 1835); DEC D-O2.4 (:1481) | si |
| :119 | 79 componentes de 43 volumenes; filtro geometrico; no afirma que sean iliosacros | DEC D3 (:1243, :1252-1254) | si |
| :119 | Proximo al fuste de 4.8 mm de Synthes, "que declara que núcleo y fuste tienen el mismo diámetro" | SYN:70, :120, :182, :240-241 | no (T01) |
| :119 | Zhu y Liao: 4.8 mm de fuste en el modelo de elementos finitos; 7.3 "solo en la rosca distal" | `zhu2022optimalposition` filas FEA (2.3, p. 1548) | parcial (T04) |
| :119 | Cabeza 8.0 x 4.5 mm, "única medición", "sin avellanado"; variantes de sensibilidad | `sayres2014comparison` (Discusion, p. 34; Operative Technique, p. 33); IMP #97 (:6696); DEC D3 (:1249-1250) | parcial (T03) |
| :121 | Calibre fijado por la referencia; profundidad crece con el radio; longitud acotada por el corredor | DEC D-O2.4 (:1475-1479); TM:117 | si |
| :123 | "Tres parámetros sin fuente del fabricante" | SYN:73 | parcial (T05) |
| :123 | Arandela 1.5 mm de otro fabricante; canulacion libre (el valor de distribuidor aparece solo como instrumental); 316L y Ti-6Al-7Nb; nota P-EA1 | IMP #97 (:6686-6694); SYN:53-58, :73; `doublemedical2021trauma`; BITACORA §2 | si |
| :127 | Congelado el 22-09-2026; desviaciones con fecha | PRE:3-8, §9; DEC 2026-09-22 (:1413) | si |
| :129 | Anclaje al punto medio; motivo | PRE §2.1 | si |
| :131-136 (Ec. pose) | Seminormal truncada, isotropa, eje de giro uniforme | PRE §3 | si |
| Tab. preinsc. | 5.0; h = 2 sigma; 2.5 mm; sigma_a; 2.07 grados; L = 138; 3 sigma; 50; 20260922 | PRE §3.1 | si |
| :158 | Una sola constante; GAPDEC h = 2 sigma (sigma_t y sigma_a); 4 grados no usados; isotropia "a juicio" | PRE §3.1, §3.2; DEC D-O2.1 (:1428-1430) | si (justificado) |
| :160 | Semilla por caso; la sensibilidad es un subconjunto | PRE §3.1, §8 | si |
| :162 | Tres comprobaciones; dos entre los seis controles; la tercera en cada corrida | TM:107; E12 (C2, C3); E13:12 | si |
| :164 | 18 volumenes; 13 / 4 / 1; 39 frente a 36 y 33 mm; GAPDATO 69 de 72 | TM:78; IMP #121; PRE §7 | si |
| :166 | Densidad reportada; Arand; GAPDEC de la definicion; fenotipos; Gardner | DEC D-O2.6; `arand2019pelvicring` (p. 376); DEC 2026-09-14 (:647, :697); `gardner2010safezones` (pp. 624, 628) | si (justificado) |
| :170 | *Inpainting* 2.5D en imagen; copia fuera de G; GAPDEC con el numero de semillas | TM:79; `diseno_A.md`:9-11, :57; DEC :1288 | si (justificado) |
| :172 | Formulacion inicial SD 1.5 + ControlNet sustituida; ControlNet presupone la base | TM:79; `zhang2023controlnet` (§3.1-3.2) | si |
| :174 | ~12 mm; trunca las rayas lejanas; 7.57 / 11.45 / 11.63 / 54.82 / 57.69; sinograma | TM:79; DEC 2026-09-17 C; `karageorgos2024ddpm` Apendice Tabla III (p. 16) | si |
| :176 | Pares con metal; 2500 HU y semimaximo; unidad = componente | DEC D1, D2 | si |
| :178 | Tres reglas fijadas antes; 0.62 = todos los parches de solo banda; tamano y forma se reportan | DEC 2026-09-21 R1-R4 (:1316-1336, :1340-1345) | si |
| :178 | Supuesto mascara-artefacto no verificado; 5 de 40 componentes eran tornillos | DEC 2026-09-21 (:1305-1307); IMP #127 pto 7 | si |
| :180 | Tres desplazamientos; 0.62 frente a 1.40 | DEC R3 (:1331-1334); TM:79 | si |
| :183 | Obj 4 sin fila; seis controles (uno en fantasma, los demas en volumenes reales); GAPDEC evidencia del Obj 4 | E12:3-89 | si (justificado) |
| :187 | Tres componentes; GAPDEC del calibre de viabilidad; escala de Smith | TM:96; DEC D-O2.4 (:1487) frente a E13:60-64; `smith2006iliosacral` (p. 236) | si (justificado) |
| :188-192 (Ec. brecha) | max(0, r + s); limites de grado por convencion | PRE §4; DEC 2026-09-16 pto 4 | si |
| :194 | Tramo = implante, longitud del corredor, 8 mm por extremo; razon de recortar; sin hueso = grado 3 | PRE:91; DEC D-O2.3 pto 4 (:1457-1460); IMP #120 | si |
| :194 | 8 mm = mismo recorte de la medicion del corredor; "su razon es clinica y no numerica" | DEC :1457-1460; `e9_corredor.py`:49-51, :77 | parcial (T02) |
| :196 | Envolvente aproxima la cortical; seis controles (1 fantasma + 5 sobre dos volumenes reales); 0.083 mm en el fantasma; GAPDEC escala angular | DEC D-O2.3 (:1462-1465); E12:3-89, :96; IMP #11 ABIERTA | si (T03 de r03 aplicado) |
| :198 | 69/15/8/8 y 40/37/11.5/11.5; solo S1; por tecnica | `zwingmann2009navigated` (pp. 1836-1837); PRE §5 | si |
| :199-203 (Ec. W1) | Grados equiespaciados; unidad = grado | PRE §5 | si |
| :205 | Sin correccion por parametros; sin regla; GAPDEC; 26/24 y 35/32; nivel en la navegada supuesto; conteo por tornillo | PRE §6; DEC D-O2.1 (:1433-1434); `zwingmann2009navigated` (p. 1833) | si (justificado) |
| :207 | Estratificacion post hoc por 7.0 mm; restriccion rechazada por dos razones; Zwingmann no excluye | IMP #122 CERRADA; TM:109 | si |
| :211 | Nombres publicados; 150 HU fuera del metal; Dice; umbral adaptativo; 5 % alto y bajo | `peters2025hybrid` Metricas 4, 6, 7 (2.5, pp. 5-6) | si |
| :213 | Disenadas para MAR; GAPDEC de la inversion; escala 0-4; realismo contra observaciones reales | `peters2025hybrid`; IMP #16, #17 ABIERTAS; TM:98, :127 | si (justificado) |
| :215 | *Streak amplitude* como unico criterio primario, declarado antes; GAPDEC de la superioridad | DEC D4 ptos 1-2 (:1265-1268); IMP #127 pto 3 | si (justificado) |
| :217 | Tres brazos; GAPDEC de la copia y pegado; CatSim/XCIST; AAPM; en lugar de reimplementacion | TM:119; `deman2007catsim`; `wu2022xcist`; `haneda2025aapm` | si (justificado) |
| :219 | 2D y MAR; fantoma; proyeccion conjunta por verificar; control sin metal; GAPDEC n; GAPDATO protocolo fisico | TM:119; DEC 2026-09-17 B.2, C; IMP #17 ABIERTA | si (justificado) |
| :221 | Wilcoxon de una cola pareado, 0.05, efecto e IC; TOST con IC 90 %; nunca por no significacion; GAPDEC agregacion | DEC D4 ptos 2-4 (:1267-1277) | si (justificado) |
| :221 | Delta = semillas sobre un mismo caso + prueba y reprueba; 3 pacientes de validacion con implante real; semillas no fijadas; GAPDEC contingencia | DEC 2026-09-21 (2) (:1394-1400); DEC D4 (:1274-1276); IMP #90 | si |
| :223 | RMSE y SSIM fuera de B_delta; exacta por construccion; medicion en el protocolo fisico | TM:79, :102, :119 | si |
| :227 | Grado de cierre por objetivo | DEC 2026-09-17 (3); PRE; DEC D4 (:1272) | si |
| Tab. diseno | Filas 1-3 | TM:77, :96-98; DEC D4; PRE | si |
| :249 | Circularidad controlada; tres decisiones post hoc; 11 de 34 y 7 de 57; mas perdida en el grupo 2 | DEC D-O2.1; DEC 2026-09-14 (3), (5); IMP #122; DEC :748 | si |
| :249 | Fractura sin verificar; un paciente con corredor < 7.0 mm con fractura confirmada por un medico sin especialidad | IMP #125 (:8698-8704; D_TS_max = 6.2 mm; ABIERTA, solo se usa el dato confirmado) | si (T02 de r03 aplicado) |
| :251 | Regla y seis combinaciones posteriores a la exploracion; umbral anterior; rediseno posterior; cota de Guo | DEC 2026-09-15 (2) (:817, :832-833, :841); DEC 2026-09-19 | si |
| :253 | Protrusion; 0.083 mm; 2 mm de la literatura pedicular; sin frontera ni grosor de corte; Tejwani p = 0.3 | DEC D-O2.3; E12; TM:52; `smith2006iliosacral` (p. 236); `zwingmann2009navigated`; `tejwani2014` (p. 514) | si |
| :255 | Equiespaciado; h = 2 sigma; metricas para reducir; aleacion; supuesto mascara-artefacto; Lin y Li | PRE §3.1, §5; TM:117; DEC 2026-09-21 (:1305); `lin2019` (Sec. 2, p. 10506); `li2024` (Sec. I, p. 1866) | si |
| :257 | Tile B y C; Reilly 6 pelvis, 5-20 mm, 36-90 %; cohorte parcial; TS sin exactitud en S1; protocolo 2D; desplazamientos de dominio | `zwingmann2009navigated` (p. 1834); `reilly2003effect` (pp. 89, 91); `wasserthal2023` fila 3e; DAT:55-58; TM:119 | si |
| :259 | Series pequenas; W1 sin prueba; GAPDEC intervalo; multiplicidad; septimo candidato; Delta sobre 3; semillas que no multiplican pacientes; muestras pequenas | PRE §5-§6; DEC :1054; DEC 2026-09-21 (2) (:1398-1401); DEC D4 (:1279) | si (justificado) |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet vigente, "31-60%", BFC/ISC) | CLAUDE.md raiz; `docs/00-tesis.md` | ausente: solo aparece como excluido o sustituido (l.36, l.172) |
| global | Claves `\cite` en `overleaf/referencias.bib` (30, las mismas de r03) | revision de las llamadas | si |
| global | Apellidos = primer autor del .bib (Zhu y Liao verificado en :1223) | `overleaf/referencias.bib` | si |
| global | Ninguna cita como sujeto gramatical sola (E-F3) | revision de todas las llamadas | si |
| global | Fuentes de fabricante senaladas (P-EA1) | l.123 | si |
| global | Implicancias ABIERTAS afirmadas como hecho (#11, #16, #17, #49, #90, #116, #123, #124, #125, #126, #127) | revision del texto | ninguna afirmada como resuelta; de #49 solo se usa la descripcion de la herramienta, y de #125 solo el caso confirmado |
| global | PAT-1, 2, 4, 5, 7, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27 | revision del texto | sin reincidencia en este dominio |
| global | PAT-6 | l.119 | reincide (T01; T03 y T04 en forma leve) |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| La cita atribuye a la fuente una lectura que la ficha contradice o no registra | E-R6 | "la guía (...) declara que núcleo y fuste tienen el mismo diámetro" | PAT-6 |
| La razon de un procedimiento (por que se recorta) se presenta como justificacion del valor de su parametro (por que 8 mm) | G-T4 | "Los 8 mm son el mismo recorte (...); su razón es clínica" | nuevo |
| Exclusividad ("la única", "solo") afirmada sin cotejar las demas fichas del repositorio que dan el mismo dato | G-T4, E-P3 | "la única medición de las fuentes revisadas, 8.0 mm" | nuevo |
| Una decision de tecnica quirurgica de un estudio se traslada como propiedad geometrica del implante | E-R6 | "8.0 mm de diámetro y 4.5 mm de altura sin avellanado" | nuevo |
