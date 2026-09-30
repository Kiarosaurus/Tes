# Auditoria de trazabilidad — capitulo3 — r05

Entrada: `overleaf/secciones/capitulo3.tex` (tras r04), respuesta `capitulo3-r04-respuesta.md`, lint
`capitulo3-r05-lint.md` (0/0/4, PASA; las cuatro E-P1 de siempre, con fuente en respuestas anteriores). En r04 no
hubo RECHAZADOS. T02 quedo ESCALADO con `\GAPDEC` sobre el valor de 8 mm, y guia-5 como NO APLICADO a la espera
de la autora; ninguno de los dos se re-reporta. T01, T03, T04 y T05 de r04 quedaron aplicados y se verificaron
contra su fuente (l.119, l.123). Tambien se verificaron los cambios de r04 que traen cifras o hechos nuevos: l.50
(validacion con 8 casos), l.73 (definicion de $B_{\delta}$), l.196 (GAPDEC de 8 mm), l.200 y l.255 (S1 en la serie
navegada), l.223 y l.261 (3 pacientes de validacion) y l.255 (GAPDATO de canal y forámenes).
Se comprobaron los patrones VIGENTES de BITACORA §1 y se respetaron las decisiones de §2, en particular la de r04:
una decision de DEC que resuelve una implicancia todavia ABIERTA (#69) se redacta como decidida.

Siglas: TM = `tesis/main.tex`; PRE = `experiments/objetivo2/preinscripcion_muestreador.md`; DAT = `docs/02-datos.md`;
DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; RES = `experiments/objetivo2/e9ts_resumen.md`;
E12 = `experiments/objetivo2/e12_sap_control.md`; E13 = `experiments/objetivo2/e13_sap.md`;
R1 = `experiments/objetivo2/r1_landmarks.md`; GRP = `experiments/exploration-3d/grupos.csv`;
SYN = `docs/literatura/synthes_cannulated_65_73_guide.md` (ficha de `synthes2003guide`);
ZW = `docs/literatura/zwingmann2009navigated.md`.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-5 | capitulo3.tex:87 (y l.255) | "con un cierre morfológico de 2 mm y relleno de cavidades cerradas" | DEC D-O2.3 pto 1 (:1450-1451: "cierre morfologico de 2 mm, relleno de cavidades cerradas en 3D"); `experiments/objetivo2/e9ts_corredor.py`:41-45 (docstring: "Hueso = union de las cuatro, con cierre morfologico de 2 mm") y :307-308 (solo `binary_closing`, sin `binary_fill_holes`); `experiments/objetivo2/e12_sap_control.py`:94 ("union de TS, cierre de 2 mm") y :111-112 (solo cierre), funcion que importa `e13_muestreo_sap.py`:50 | Hay dos fuentes y no coinciden. La decision fija cierre mas relleno de cavidades; el codigo que midio el corredor (E9-TS) y el que corrio SAP (E12/E13) aplica solo el cierre. El relleno 3D existe unicamente en `e9_corredor.py`:99, la version por umbral de HU que la envolvente de TotalSegmentator reemplazo. El texto copia la decision. La amenaza de validez de constructo de l.255 ("el cierre morfológico y el relleno de cavidades ... podrían ocupar el canal sacro") se apoya en un paso que no se corrio. Patron PAT-20 (hoy ERRADICADO) reincide | Describir lo que se corrio y marcar la discrepancia (OC-5): "la unión de las máscaras de sacro, vértebra S1 y ambos coxales, con un cierre morfológico de 2~mm \GAPDEC{la decisión que define la envolvente fija además un relleno de cavidades cerradas que el código del corredor y de SAP no aplica}". En l.255, "El cierre morfológico de la envolvente (...) podría ocupar (...) los forámenes". Anotar el GAP en MAPA y escalar a la autora (#127) |
| T02 | baja | E-R6 | capitulo3.tex:255 | "no en la de la navegada, cuyo criterio de evaluación se refiere al platillo sacro" | ZW:72 y :177-178 ("Definicion de posicion ideal (orientacion)", comun, Materials and Methods, p. 1835); ZW:301 | La frase *"parallel to the respective sacral end plate and the S1 neuroforamina"* es, segun la ficha, la definicion general de posicion ideal del estudio y no un criterio propio de la serie navegada. ZW:301 la usa para el brazo navegado porque es lo unico que se acerca a nombrar un nivel, no porque sea exclusiva de el. Con "cuyo", el texto la atribuye solo a la navegada | "(...) pero no en la de la navegada. La definición de posición ideal del estudio se refiere al platillo sacro correspondiente y a los forámenes de S1." |
| T03 | baja | E-R6, G-T4 | capitulo3.tex:207 | "Los grados se cuentan por tornillo, aunque algunos pacientes recibieron más de uno." | DEC 2026-09-17 C, fila #69 (:986: "grados por tornillo con pacientes con mas de uno"); ZW:85 y :303 (*"In our treatment algorithm, we used only one screw in all patients"*, Discussion, p. 1837); ZW:304 (inconsistencia; explicacion NO ENCONTRADO EN EL PDF) | La decision respalda la frase, y por eso no se reporta como error (BITACORA §2, r04). Pero la frase viene justo despues de una cita a Zwingmann et al. y afirma como hecho algo que el articulo niega de forma explicita. "Mas de uno" se deduce de los recuentos 26/24 y 35/32, y la ficha registra esa deduccion como inconsistencia interna del articulo, sin explicacion. El lector no ve la contradiccion | "Los grados se cuentan por tornillo. Los recuentos implican que algunos pacientes recibieron más de uno, aunque el artículo declara un solo tornillo por paciente." |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9 | Dos componentes separados; compuerta previa | TM:74-80; CLAUDE.md raiz | si |
| :13 | Cuatro objetivos; SAP es la unica metrica propia; el Obj 4 adopta el protocolo con sus nombres publicados | TM:80; DEC 2026-09-08 (BFC/ISC retiradas) | si |
| :13 | GAPDEC alineacion con la introduccion | IMP #126 ABIERTA | si (justificado) |
| :15 | Corredor medido; eje perturbado; M, B_delta, G; copia fuera de G | TM:79, :107 | si |
| Fig. pipeline | TotalSegmentator; marco de Kaiser; SAP frente a dos distribuciones; *inpainting* en imagen; copia y pegado y protocolo fisico; la compuerta descarto la ruta latente | TM:77-79, :98; DEC 2026-09-19 | si |
| :36 | Dice/HD95 y ablaciones fuera de alcance, por dos condiciones | TM:83, :127; DEC 2026-09-08; DEC 2026-09-17 B.1 | si |
| :36 | La publicacion anota 14 de los 75 de CLINIC-metal | `liu2021ctpelvic1k` (Tabla 1, p. 3); DAT:157-161 | si |
| :36 | 178 de 1 184 | DAT:55 | si |
| :38 | Compuerta ejecutada y negativa; Obj 2 ejecutado; GAPDATO sin muestra sintetica; rediseno posterior | TM:77, :96; IMP #116 act. (:8750-8753); DEC 2026-09-19 pto 2 | si |
| :42 | 1 184; 178; dataset6 103 y dataset7 75; correspondencia inferida | DAT:27-30, :55-63 | si |
| :44 | El articulo no reporta adquisicion ni reconstruccion; Selles | `liu2021ctpelvic1k` (NO ENCONTRADO); `selles2024marreview` (Sec. 3.3, 3.5); DEC 2026-09-17 C fila #73 | si |
| :46 | Cribado > 2500 HU, un voxel, sin filtro de tamano; revision 3D de los 178; GAPDATO multiplanar | DAT:67-69, :104, :139; DEC 2026-09-11 (3) | si |
| :48 | SHA256 y huella por corte, mas observacion visual; 178 -> 168; 65/37/66; 179; 10; 1 | DAT:117-122, :134-137; GRP | si |
| :50 | Aislamiento estricto; particion por paciente estratificada; entrenamiento, validacion con 8 casos, prueba con 34; Obj 3 reutiliza; Obj 2 grupos 2 y 3 | TM:77, :115; DEC 2026-09-21 (2) (:1378, :1384); DEC 2026-09-17 (3); DEC 2026-09-14 (2) (:724) | si |
| :52 | 103 -> 91 -> 72; 11 de 34; 7 de 57; 1 en el borde; 49; criterio del control de nivel | DEC 2026-09-14 (3) (:747-749); DEC 2026-09-14 (:642, :668-671); PRE §1 | si |
| :52 | GAPDATO cribado de fractura, 30 (15 + 15) | IMP #125 (:8729-8730); `r3_fractura_revisor.csv` sin veredictos | si (justificado) |
| :54 | Cuatro funciones de los 65; tornillos fragmentados, bajo el calibre y cambiantes entre adquisiciones | TM:117; DEC D1; DEC 2026-09-11 (3) (:623) | si |
| :58 | Compuerta obligatoria; regla fijada antes de la prueba que decide; exploracion previa sobre los 178 | DEC 2026-09-17 B.3 (:976-979); DEC 2026-09-15 (2) (:841) | si |
| :60 | Tres canales; VAE de SD 1.5; lectura sin la imagen original; 150 HU | DEC 2026-09-17 (3) (:1048-1050); `peters2025hybrid` (2.5, p. 5); `haneda2025aapm` (Sec. 2.3, p. 7) | si |
| :61-65 (Ec. MAE) | MAE por paciente en hueso | DEC :1051 | si |
| :67 | Sin umbral publicado; 20.2 / 12.3 / 12.74 HU; RMSE >= MAE | DEC 2026-09-15 (2) (:818-829); `karageorgos2024ddpm` Tabla I; `yun2026simulationdriven` Tabla 1; `peters2025hybrid` | si |
| :69 | 2 x 3; decodificador adaptado con codificador congelado; GAPDATO parametros del ajuste; ventanas de Wang; 20 000; arcsinh | DEC 2026-09-17 C (:984), D.1 (:996-997); `wang2025adaptiveweighting` (V-A-1, p. 2412); TM:77 | si |
| :71 | Media sobre 34 < 25 HU; alguna de seis; IC 95 %; marginal; orden a priori; No-Go -> Obj 3 no se ejecuta | DEC :1051-1057, :1065, :976-979 | si |
| :73 | B_delta descriptivo; 12 mm, distancia euclidea 3D, metal > 2500 HU, sin el metal; Rombach | `experiments/objetivo1/p1_decodificador_sd15.py`:34, :72 (`BDELTA_MM = 12.0`), :351-364; DEC 2026-09-17 C fila 66/75 (:985); `rombach2022latentdiffusion` (§1, p. 2) | si (guia-7 de r04 aplicado) |
| :75 | Extension a Guo; cota por saturacion | DEC 2026-09-19 pto 3; DEC :1145; `guo2025maisi` | si |
| :79 | Referencia clinica definida (dos series); Ziran: 7-25 % y 140 % | `zwingmann2009navigated` (Results, pp. 1836-1837); `ziran2007fluoroscopic` (pp. 351-352) | si |
| :83 | Marco de Kaiser; regla de 5 mm; "este trabajo lee" h como radial = radio de 10 mm | `kaiser2014dysmorphism` (p. e120(2)); DEC 2026-09-11 (2) (:603-605) | si |
| :85 | 0.42; TS 2.18.0 `total`; nnU-Net; recorte 6 mm / 3 mm (`--robust_crop`); limpieza 0.1 %; 104 estructuras; sin exactitud para S1 | TM:123; DEC 2026-09-14 (3), (4) (:763-765); IMP #49 hallazgo 3; `wasserthal2023` filas 1a, 2d, 3e | si |
| :87 | Envolvente = union de sacro, S1 y coxales, cierre de 2 mm "y relleno de cavidades cerradas" | DEC D-O2.3 (:1450-1451) frente a `e9ts_corredor.py`:41-45, :307-308 y `e12_sap_control.py`:94, :111-112 | no (T01) |
| :87 | Diametro = 2 x distancia libre, sin 8 mm por extremo; GAPDATO del algoritmo; semimaximo y 2500 HU; contraste aparte | DEC D-O2.3 (:1457), :1467-1469; `e9ts_corredor.py`:37-39; DEC 2026-09-14 (2), (3); IMP #121 | si |
| :89 | D >= d + 2 epsilon; epsilon 1-2 mm; lectura por lado propia; Kaiser; McLaren; 10 mm como convencion | DEC 2026-09-11 (2) (:590-601); `e9_corredor.py`:25-28; `kaiser2014dysmorphism` (p. e120(7)); `mclaren2021corridor` (p. 2) | si |
| :91 | 9.5 (7.4-11.7); 65.3 / 23.6; 62.5 / 20.8; 29 y 27 de 72; limpieza hasta 5 %; post hoc; GAPDATO 16 casos | RES:16, :20; DEC 2026-09-14 (3), (4) (:770-771), (5); IMP #123 ABIERTA | si |
| :95 | Union lumbosacra; ninguna fuente revisada; GAPDATO heuristica; 69 de dataset6 sin objeto frente a 66 del grupo 3; revisor clinico ciego | TM:121; R1:4, :7-15, :45; DAT:127, :137 | si (justificado) |
| :97 | 65; 57; 7 de 8 truncados; 48; 29; 17 con tornillo, S1 correcto en todos, 3 contaminados; GAPDEC 61 de 61; crestas sin revision clinica | R1:42, :46, :57-88; TM:121; IMP #124 ABIERTA; DEC 2026-09-17 E | si (justificado) |
| :101 | Nominal = rosca; mas seccion que 4.91 mm; nominal solo para viabilidad | TM:117; IMP #97 (:6655-6668) | si |
| Tab. geom. | 6.5-8.0; 6.3-8; 4.91; 4.8; 4.9 y 4.7; 7.0; 4.91 y 7.3 de sensibilidad | `gardner2010safezones` (p. 624); `kaiser2014dysmorphism`; DEC D3; SYN:70, :119; `gardner2015screw` (p. 42); `zwingmann2009navigated` (p. 1835); DEC D-O2.4 (:1481) | si |
| :119 | 79 componentes de 43 volumenes; filtro geometrico; no afirma que sean iliosacros | DEC D3 (:1243, :1252-1254) | si |
| :119 | Proximo al fuste de 4.8 mm de Synthes, "el mismo para los tornillos de 6.5 y 7.3 mm" | SYN:70 ("Fuste 4.8 mm (ambos calibres)"), :119 (rotulo compartido) | si (T01 de r04 aplicado) |
| :119 | Zhu y Liao: fuste de 4.8 mm; 7.3 mm "solo en una rosca de 16 mm" | `zhu2022optimalposition` filas FEA (2.3, p. 1548) | si (T04 de r04 aplicado) |
| :119 | Cabeza 8.0 x 4.5 mm; diametro en Sayres y en el catalogo; altura solo en Sayres; sin avellanar = supuesto propio; variantes de sensibilidad | `sayres2014comparison` filas 34-35 (Discusion, p. 34); `doublemedical_trauma_catalogue.md`:155, :187-196 (*"Head Diameter: 8.0mm"*); DEC D3 (:1249-1250) | si (T03 de r04 aplicado) |
| :121 | Calibre fijado por la referencia; profundidad crece con el radio; longitud acotada por el corredor | DEC D-O2.4 (:1475-1479); TM:117 | si |
| :123 | "Tres parámetros quedan sin fijar por la documentación del propio fabricante"; arandela 1.5 mm; canulacion libre; 316L y Ti-6Al-7Nb; P-EA1 | IMP #97 (:6686-6694); DEC :1174-1175; SYN:53-58, :73; `doublemedical_trauma_catalogue.md`:160; BITACORA §2 | si (T05 de r04 aplicado) |
| :127 | Congelado el 22-09-2026; "impide que la comparación sea un ajuste"; desviaciones con fecha | PRE:3-8, §9; DEC 2026-09-22 (:1413-1414) | si |
| :129 | Anclaje al punto medio; motivo | PRE §2.1 | si |
| :131-136 (Ec. pose) | Seminormal truncada, isotropa, eje de giro uniforme | PRE §3 | si |
| Tab. preinsc. | 5.0; h = 2 sigma; 2.5 mm; sigma_a; 2.07 grados; L = 138; 3 sigma; 50; 20260922 | PRE §3.1 | si |
| :158 | Una sola constante; GAPDEC h = 2 sigma; 4 grados no usados; isotropia | PRE §3.1, §3.2; DEC D-O2.1 (:1428-1430); ZW:39 | si (justificado) |
| :160 | Semilla por caso; la sensibilidad es un subconjunto | PRE §3.1, §8 | si |
| :162 | Tres comprobaciones; dos entre los seis controles; la tercera en cada corrida | TM:107; E12 (C2, C3); E13:12; DEC :1467-1471 | si |
| :164 | 18 volumenes; 13 / 4 / 1; 39 frente a 36 y 33 mm; GAPDATO 69 de 72 | TM:78; IMP #121; PRE §7 | si |
| :166 | Densidad reportada; Arand; GAPDEC de la definicion | DEC D-O2.6; `arand2019pelvicring` (p. 376) | si (justificado) |
| :168 | Fenotipos no estratifican; Gardner: zona menor en dismorficos y estudio previo sin diferencia | DEC 2026-09-14 (:647, :697); `gardner2010safezones` (pp. 624, 628) | si |
| :172 | *Inpainting* 2.5D en imagen; copia fuera de G; GAPDEC de la preinscripcion (con semillas) | TM:79; `diseno_A.md`:9-11, :57; DEC :1288 | si (justificado) |
| :174 | Formulacion inicial SD 1.5 + ControlNet sustituida; ControlNet presupone la base | TM:79; DEC 2026-09-19; `zhang2023controlnet` (§3.1-3.2) | si |
| :176 | ~12 mm; trunca las rayas lejanas; 7.57 / 11.45 / 11.63 / 54.82 / 57.69; sinograma | TM:79; DEC 2026-09-17 C fila 57 (:990); `karageorgos2024ddpm` Apendice Tabla III (p. 16) | si |
| :178 | Pares con metal; 2500 HU y semimaximo; unidad = componente | DEC D1, D2 | si |
| :180 | Tres reglas fijadas antes; 0.62 = todos los parches de solo banda; tamano y forma se reportan; supuesto no verificado; 5 de 40 | DEC 2026-09-21 R1-R4 (:1305-1307, :1316-1336) | si |
| :182 | Tres desplazamientos; fuste por debajo de los calibres; 0.62 frente a 1.40 | DEC R3 (:1330-1334); DEC 2026-09-11 (3) (:623); TM:79 | si |
| :185 | Obj 4 sin fila; controles de SAP; GAPDEC evidencia del Obj 4 | E12:3-89 | si (justificado) |
| :189 | Tres componentes; GAPDEC calibre de viabilidad; escala de Smith aplicada a iliosacros; escala angular con GAPDEC | TM:96; DEC D-O2.4 (:1487) frente a E13:60-64; `smith2006iliosacral` (p. 236; ficha :14, :84-87) | si (justificado) |
| :190-194 (Ec. brecha) | max(0, r + s); envolvente aproxima la cortical; limites de grado por convencion | PRE §4; DEC D-O2.3 (:1448-1465); DEC 2026-09-16 pto 4 | si |
| :196 | Tramo = implante, longitud del corredor, 8 mm por extremo; razon de excluir; GAPDEC del valor de 8 mm; sin hueso = grado 3 | PRE:91; DEC D-O2.3 pto 4 (:1457-1460); `e9_corredor.py`:49-51, :77; IMP #120 | si (justificado; T02 de r04 escalado) |
| :198 | Seis controles; uno en el fantoma y cinco sobre dos volumenes reales; 0.083 mm en el fantoma | E12:3-89, :96 | si |
| :200 | 69/15/8/8 y 40/37/11.5/11.5; S1 declarado en la convencional y asumido en la navegada | ZW:34-35, :300-301; DEC 2026-09-17 C fila #69 (:986); PRE §5 | si |
| :201-205 (Ec. W1) | Grados equiespaciados; unidad = grado | PRE §5 | si |
| :207 | Sin ajuste; sin regla; GAPDEC; 26/24 y 35/32; no es prueba de equivalencia | PRE §6; DEC D-O2.1 (:1433-1434); ZW:41-42 | si (justificado) |
| :207 | "algunos pacientes recibieron más de uno" | DEC :986 frente a ZW:85, :303-304 | parcial (T03) |
| :209 | Estratificacion post hoc por 7.0 mm; restriccion rechazada por dos razones; Zwingmann no excluye | IMP #122 CERRADA; TM:109 | si |
| :213 | Nombres publicados; 150 HU fuera del metal; Dice; umbral adaptativo; 5 % alto y bajo | `peters2025hybrid` Metricas 4, 6, 7 (2.5, pp. 5-6) | si |
| :215 | Disenadas para MAR; GAPDEC de la inversion; escala 0-4; realismo contra observaciones reales | `peters2025hybrid`; IMP #16, #17 ABIERTAS; TM:98, :127 | si (justificado) |
| :217 | *Streak amplitude* como unico criterio primario, declarado antes; GAPDEC de la superioridad | DEC D4 ptos 1-2 (:1265-1268); IMP #127 pto 3 | si (justificado) |
| :219 | Tres brazos; GAPDEC de la copia y pegado; CatSim/XCIST; AAPM; en lugar de reimplementacion | TM:119; DEC :69-71; `deman2007catsim`; `wu2022xcist`; `haneda2025aapm` | si (justificado) |
| :221 | 2D y MAR; fantoma; proyeccion conjunta por verificar; control sin metal; GAPDEC n; GAPDATO protocolo fisico | TM:119; DEC 2026-09-17 B.2, C fila 70 (:987); IMP #17 ABIERTA | si (justificado) |
| :223 | Wilcoxon de una cola pareado, 0.05, efecto e IC; TOST con IC 90 %; nunca por no significacion; GAPDEC agregacion y contingencia | DEC D4 ptos 2-4 (:1267-1277) | si (justificado) |
| :223 | Delta = semillas + prueba y reprueba; casos de validacion; 3 pacientes con implante real; semillas no fijadas | DEC 2026-09-21 (2) (:1384, :1394, :1398-1400); DEC D4 (:1274-1276) | si |
| :225 | RMSE y SSIM fuera de B_delta; exacta por construccion; medicion en el protocolo fisico | TM:79, :102, :119 | si |
| :229 | Grado de cierre por objetivo | DEC 2026-09-17 (3); PRE; DEC D4 (:1272), :1288 | si |
| Tab. diseno | Filas 1-3 (34; 72 y 49; S1; Delta de validacion) | TM:77, :96-98; DEC D4; PRE; DEC 2026-09-21 (2) | si |
| :251 | Circularidad controlada; tres decisiones post hoc; 11 de 34 y 7 de 57; fractura sin verificar; un paciente con fractura confirmada | DEC D-O2.1; DEC 2026-09-14 (3), (5); IMP #122; IMP #125 (:8698-8704) | si |
| :253 | Regla y seis combinaciones posteriores a la exploracion; umbral anterior; rediseno posterior; cota de Guo | DEC 2026-09-15 (2) (:817, :832-833, :841); DEC 2026-09-19 | si |
| :255 | Protrusion; 0.083 mm en el fantoma; 2 mm de la literatura pedicular; sin frontera ni grosor de corte; Tejwani p = 0.3 | DEC D-O2.3; E12:96; `smith2006iliosacral` (ficha :79); ZW:292-293, :272; `tejwani2014` (p. 514) | si |
| :255 | "El cierre morfológico y el relleno de cavidades"; GAPDATO canal y forámenes | `e9ts_revision_laminas.md`:41 (pendiente); IMP #123; codigo sin relleno (ver T01) | GAP si justificado; "relleno" no (T01) |
| :255 | S1 nombrado en la convencional y no en la navegada; "cuyo criterio de evaluación" | ZW:72, :177-178, :300-301; DEC :986 | parcial (T02) |
| :257 | Equiespaciado; h = 2 sigma; metricas para reducir; aleacion; supuesto mascara-artefacto; Lin (mal planteado, misma traza) y Li | PRE §3.1, §5; TM:117; DEC 2026-09-21 (:1305); `lin2019` (Sec. 2, p. 10506; ficha :264); `li2024` (Sec. I, p. 1866); DEC :988 | si |
| :259 | Tile B y C; Reilly 6 pelvis, 5-20 mm, 36-90 %; cohorte parcial; TS sin exactitud en S1; protocolo 2D; desplazamientos | ZW:88; `reilly2003effect` (pp. 89, 91); `wasserthal2023` fila 3e; DAT:55-58; TM:119 | si |
| :261 | Series pequenas por tornillo; W1 sin prueba; GAPDEC intervalo; multiplicidad; septimo candidato; Delta sobre 3; muestras pequenas | PRE §5-§6; DEC :1054; DEC 2026-09-21 (2) (:1398-1401); DEC D4 (:1279) | si (justificado) |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet vigente, "31-60%", BFC/ISC) | CLAUDE.md raiz; `docs/00-tesis.md` | ausente: solo aparece como excluido o sustituido (l.36, l.174) |
| global | Claves `\cite` en `overleaf/referencias.bib` | revision de las llamadas (las mismas de r04, sin claves nuevas) | si |
| global | Apellidos = primer autor del .bib | `overleaf/referencias.bib` | si |
| global | Ninguna cita como sujeto gramatical sola (E-F3) | revision de todas las llamadas | si |
| global | Fuentes de fabricante senaladas (P-EA1) | l.123 | si |
| global | Implicancias ABIERTAS afirmadas como hecho (#11, #16, #17, #49, #69, #90, #116, #123, #124, #125, #126, #127) | revision del texto | ninguna; #69 entra por DEC 2026-09-17 C (BITACORA §2) |
| global | PAT-2, 5, 7, 14, 15, 21 a 36 (VIGENTES) | revision del texto | sin reincidencia en el dominio de trazabilidad |
| global | PAT-6 | l.119, l.255 | sin reincidencia en l.119; forma leve en l.255 (T02) |
| global | PAT-20 (ERRADICADO) | l.87, l.255 | reincide (T01) |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| El metodo se describe segun la decision y no segun lo implementado y corrido, que difiere | G-T4, OC-5 | "cierre morfológico de 2 mm y relleno de cavidades cerradas" | PAT-20 |
| Frase general de una fuente (definicion comun a todo el estudio) atribuida a uno solo de sus brazos | E-R6 | "la navegada, cuyo criterio de evaluación se refiere al platillo sacro" | nuevo |
| Dato deducido de recuentos de una fuente que contradice lo que la fuente declara, presentado sin la contradiccion | E-R6, G-T4 | "aunque algunos pacientes recibieron más de uno" | nuevo |
