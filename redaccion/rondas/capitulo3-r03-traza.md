# Auditoria de trazabilidad — capitulo3 — r03

Entrada: `overleaf/secciones/capitulo3.tex` (tras r02), respuesta `capitulo3-r02-respuesta.md`, lint
`capitulo3-r03-lint.md` (0/0/5, PASA). En r02 no hubo RECHAZADOS. Los 4 ESCALADOS de r02 (guia-1, guia-2, T01, T03)
estan ya como `\GAPDEC` con la contradiccion concreta y no se re-reportan. Tampoco se re-reportan los avisos sobre
`tesis/main.tex` escalados en r01 y r02. Se comprobaron los 20 patrones VIGENTES de BITACORA §1 y se respetaron las
decisiones de §2 (en particular: cifra de DEC entra como hecho; viabilidad con los dos extremos; "metricas de Peters
et al." / "protocolo fisico").

Se verificaron contra su fuente todas las cifras y afirmaciones reescritas en r02: l.58, l.60, l.69, l.83, l.91,
l.95, l.97, l.119, l.162, l.180, l.182, l.189, l.251 y l.259.

Siglas: TM = `tesis/main.tex`; PRE = `experiments/objetivo2/preinscripcion_muestreador.md`; DAT = `docs/02-datos.md`;
DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; RES = `experiments/objetivo2/e9ts_resumen.md`;
E12 = `experiments/objetivo2/e12_sap_control.md`; E13 = `experiments/objetivo2/e13_sap.md`;
R1 = `experiments/objetivo2/r1_landmarks.md`; GRP = `experiments/exploration-3d/grupos.csv`.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4 | capitulo3.tex:95 (y :48) | "el máximo observado en 69 pacientes sin objeto metálico de la carpeta `dataset6`" | R1:4 ("dataset6 sin objeto, una unidad por paciente: 69"); DAT:115, :127 (revision 3D del 2026-09-07); DAT:137 y GRP (grupo 3 = 66, todos de dataset6; reparto #35 del 2026-09-14) | La cifra coincide con R1, pero no con la clasificacion vigente que el mismo capitulo usa en l.48 ("66 sin objeto metálico (grupo 3)"). La cohorte de calibracion de R1 salio de la revision 3D inicial. El reparto posterior paso al menos 3 de esos pacientes a grupo 2 (objetos no ortopedicos, p. ej. electrodos). El lector ve 69 "sin objeto metálico" en una sola carpeta frente a 66 en toda la cohorte, sin explicacion. Ademas, "sin objeto metálico" es falso para esos 3 segun GRP. | "(...) el máximo observado en 69 pacientes de `dataset6` que la revisión tridimensional inicial clasificó sin objeto, antes del reparto por grupos (Sección~\ref{sec:datos})". Otra opcion: indicar que la calibracion es anterior al reparto y que incluye pacientes hoy asignados al grupo 2. No se recalcula nada. |
| T02 | media | G-T4, OC-3 | capitulo3.tex:52, :251 | "fracturas no detectadas estrecharían corredores por una causa distinta de la variabilidad anatómica" | IMP #125 (:8693-8705, ABIERTA): `CLINIC_0060` tiene fractura CONFIRMADA el 2026-09-23, corredor de 6.2 mm, dentro de los 15 estrechos; `CLINIC_0022` sospechosa (4.7 mm) | La fuente existe y el texto no la hace visible. El capitulo presenta la fractura solo como hipotesis ("no se verificó", "fracturas no detectadas"). El registro, en cambio, tiene un caso confirmado dentro de la cohorte primaria, y justo en el estrato que motiva la estratificacion post hoc (l.209). Como #125 esta ABIERTA, entra como GAP y no como conclusion, pero el dato de un caso confirmado no depende de la decision pendiente. | En l.251, despues de "no se verificó": "y al menos un paciente de la cohorte primaria, uno de los de corredor más estrecho que el calibre de 7.0~mm, tiene una fractura confirmada por un médico sin especialidad". Mantener el `\GAPDATO` del cribado de l.52. La salvedad sobre quien confirmo es obligatoria (IMP :8699-8700). |
| T03 | baja | G-T4 | capitulo3.tex:185, :198 | "seis controles sobre geometría conocida verificaron la implementación" | E12:3-19 (C1, fantasma de geometria conocida) y E12:21-89 (C2-C6 sobre dos casos reales, `metal_0008` y `CLINIC_0002`) | Solo C1 usa geometria conocida. C2 a C6 se corrieron sobre el eje de dos volumenes reales, cuya geometria no es conocida sino medida. La resolucion de 0.083 mm si sale de C1. | "Seis controles, uno sobre un fantasma de geometría conocida y cinco sobre dos volúmenes reales, verificaron la implementación (...); la resolución de la métrica en el fantasma es de 0.083~mm". Ajustar igual l.185. |
| T04 | baja | G-T4 | capitulo3.tex:95 | "confirmó el nivel S1 en cada paciente" | R1:45-46 (revisor clinico: ok 51, +1 7, no hallado 4, otro 2, ? 1; "Marco computable con S1 correcto segun revisor clinico: 48 de 65"); TM:121; IMP #124 (:8677-8679) | La frase viene de TM:121, e IMP #124 la da por exacta en el sentido de "reviso". Leida en espanol, "confirmó" indica que el nivel era correcto en todos. Segun R1 lo era en 51 de 65, y eso explica el paso de 57 a 48 en l.97, que hoy no tiene causa visible. | "(...) revisó el nivel S1 en cada paciente." En l.97: "(...) el marco fue computable con el nivel S1 correcto según el revisor en 48 (...)". |
| T05 | baja | E-R6 | capitulo3.tex:83 | "es el radio del corredor de 10 mm de Kaiser et al." | `kaiser2014dysmorphism` fila "Margen de 5 mm al cortical para longitud util" ("no less than 5 mm of distance to the cortex on either side", p. e120(2)); DEC 2026-09-11 (2) (:603-605, alternativa descartada) | Que el margen sea radial y equivalga al radio del corredor es la lectura del proyecto (DEC), no algo que la ficha registre de Kaiser. Es aritmetica plausible (5 = 10/2), pero la frase la presenta como propiedad del marco citado. El patron PAT-6 reincide en forma leve. | "Ese margen, $h$, se lee en este trabajo como una distancia radial medida en el plano perpendicular al eje, equivalente al radio del corredor de 10~mm de Kaiser et al., y no como una holgura añadida al tornillo." |
| T06 | baja | P-MM3, G-T4 | capitulo3.tex:259 | "con varias semillas por caso" | DEC 2026-09-21 (2) (:1398-1400: "3 casos por k semillas"); DEC D4 pto 4 | Ninguna fuente fija el numero de semillas. Hoy queda como cuantificador vago sin valor ni GAP, que es el patron PAT-2 (reincide). El `\GAPDEC` de l.170 cubre el "margen de equivalencia", pero no se ve desde aqui. | "(...) con un número de semillas por caso aún no fijado (Sección~\ref{sec:sintetizador})". Tambien sirve anadir "número de semillas por caso" al `\GAPDEC` de l.170. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9 | Dos componentes separados; compuerta previa | TM:74-80; CLAUDE.md raiz | si |
| :13 | Cuatro objetivos; SAP unica metrica propia; Obj 4 adopta protocolo con nombres publicados | TM:80; DEC 2026-09-08 (BFC/ISC retiradas) | si |
| :13 | GAPDEC alineacion con la introduccion | IMP #126 ABIERTA | si (justificado) |
| :15 | Corredor medido, eje perturbado, M, B_delta, G, copia fuera de G | TM:79, :107 | si |
| Fig. pipeline | TotalSegmentator; marco de Kaiser; SAP frente a dos distribuciones; *inpainting* en imagen; copia y pegado y protocolo fisico; la compuerta descarto la ruta latente | TM:77-79, :98; DEC 2026-09-19 | si |
| :36 | Dice/HD95 fuera de alcance; dos condiciones | TM:83, :127 | si |
| :36 | 14 de 75 de CLINIC-metal anotados en la publicacion | `liu2021ctpelvic1k` (Tabla 1, p. 3); DAT:157-161 | si |
| :36 | 178 de 1 184 | DAT:55; `liu2021ctpelvic1k` | si |
| :36 | Ablaciones diferidas | DEC 2026-09-17 B.1 | si |
| :38 | Compuerta ejecutada y negativa; Obj 2 ejecutado sobre las dos cohortes | TM:77, :96 | si |
| :38 | GAPDATO sin muestra sintetica | IMP #116 act. 2026-09-24 (:8750-8753) | si (justificado) |
| :38 | Rediseno posterior; regla fijada antes de la prueba que decide | DEC 2026-09-17 B.3; 2026-09-19 pto 2 | si |
| :42 | 1 184; 178; dataset6 103 y dataset7 75; correspondencia inferida | DAT:27-30, :55-63 | si |
| :44 | El articulo no reporta adquisicion ni reconstruccion; Selles | `liu2021ctpelvic1k` (NO ENCONTRADO); `selles2024marreview` (Sec. 3.3, 3.5); DEC 2026-09-17 C (#73) | si |
| :46 | Cribado > 2500 HU, un voxel, sin filtro de tamano; heuristica; no es metrica de Peters | DAT:67-69; DEC 2026-09-11 (3) | si |
| :46 | La autora reviso en 3D los 178; GAPDATO de revision multiplanar | DAT:104, :139 | si (justificado) |
| :48 | SHA256 y huella por corte, mas observacion visual; 178 -> 168 | DAT:117-122 | si |
| :48 | 65 / 37 / 66; 179 unidades; 10 fuera de uso; 1 de reproducibilidad | DAT:134-137; GRP (66 y 37 verificados) | si |
| :50 | Aislamiento estricto; particion por paciente estratificada; 34 de prueba; Obj 3 reutiliza; Obj 2 grupos 2 y 3 | TM:77, :115; DEC 2026-09-17 (3) (:1051-1052); DEC 2026-09-14 (2) | si |
| :52 | 103 -> 91 -> 72; 11 de 34; 7 de 57; 1 en el borde del FOV; 49 de sensibilidad | DEC 2026-09-14 (3) (:747-749); PRE §1; RES:12, :25 | si |
| :52 | Criterio del control de nivel | DEC 2026-09-14 (:642, :668-671) | si |
| :52 | GAPDATO cribado de fractura 30 (15 + 15) | IMP #125 (:8729-8730) | si (justificado; ver T02) |
| :54 | Cuatro funciones de los 65; tornillos fragmentados y por debajo de calibre; cambian entre adquisiciones | TM:117; DEC D1 | si |
| :58 | Compuerta obligatoria previa; regla fijada antes de la prueba que decide | DEC 2026-09-17 B.3, (3) | si |
| :58 | Exploracion previa del preentrenado sobre los 178, por encima del criterio en todos | DEC 2026-09-15 (2) (:841: "178 de 178") | si |
| :60 | Tres canales; VAE de SD 1.5; lectura sin imagen original, canal mas estrecho no saturado | DEC 2026-09-17 (3) (:1048-1050) | si |
| :60 | 150 HU del protocolo adoptado | `peters2025hybrid` (2.5, p. 5); `haneda2025aapm` (Sec. 2.3, p. 7); DEC :825-826 | si |
| :61-65 (Ec. MAE) | MAE por paciente en hueso | DEC :1051 | si |
| :67 | Sin umbral publicado; 20.2 / 12.3 / 12.74 HU; NMAR como ancla de la escala; RMSE >= MAE | DEC 2026-09-15 (2) (:818-829); `karageorgos2024ddpm` Tabla I (p. 28); `yun2026simulationdriven` Tabla 1 (p. 10); `peters2025hybrid` fila "NMAR calibrado a score 2" | si |
| :69 | 2 x 3; decodificador adaptado por codificacion con el codificador congelado; cortes de pacientes de entrenamiento | DEC 2026-09-17 (3) (:1048-1049); DEC 2026-09-17 D.1 (:996-998) | si |
| :69 | GAPDATO parametros del ajuste | sin fuente en `experiments/objetivo1/*.md` ni en `docs/` (busqueda de optimizador, perdida y pasos sin resultados) | si (justificado) |
| :69 | Ventanas de Wang; techo de 20 000; arcsinh sobre [-1000, 20 000] | `wang2025adaptiveweighting` (V-A-1, p. 2412); TM:77 | si |
| :71 | Media sobre 34 < 25 HU; Go si alguna de seis; IC 95 %; marginal; orden a priori; 2000 HU recorta metal | DEC :1051-1057, :1065 | si |
| :71 | Si ninguna aprueba, el Obj 3 no se ejecuta; rediseno posterior | DEC :976-979; DEC 2026-09-19 pto 2 | si |
| :73 | B_delta descriptivo; Rombach, alta frecuencia | DEC 2026-09-17 C (#66/75); `rombach2022latentdiffusion` (§1, p. 2) | si |
| :75 | Extension al latente de Guo (entrenado con TC); misma regla y pacientes; cota por recorte; no se corre si supera | DEC 2026-09-19 pto 3; TM:77; `guo2025maisi` (resumen: VAE sobre 39 206 CT y 18 827 RM) | si |
| :79 | Perturba, no optimiza; malposicion dependiente de la tecnica | PRE §2; `zwingmann2009navigated` (Results, pp. 1836-1837) | si |
| :79 | Ziran: CV 7-25 %; hasta 140 % en el ala superior de S1 | `ziran2007fluoroscopic` (pp. 351-352) | si |
| :83 | Marco de Kaiser: reformateo, angulos, regla de 5 mm | `kaiser2014dysmorphism` filas de reformateo y "no less than 5 mm" (p. e120(2)) | si |
| :83 | h radial = radio del corredor de 10 mm, no holgura | DEC 2026-09-11 (2) (:603-605) | parcial (T05) |
| :85 | Mediana 0.42 de voxeles <= 150 HU | TM:123 | si |
| :85 | TS 2.18.0, `total`, recortes; nnU-Net; limpieza 0.1 %; 104 estructuras; sin exactitud para S1 | TM:78; DEC 2026-09-14, (3), (4); `wasserthal2023` filas 1a, 2d, 3e | si |
| :87 | Envolvente: sacro, S1, coxales, cierre 2 mm, relleno; diametro = 2 x distancia libre | DEC D-O2.3 (:1450-1452, :1467-1469) | si |
| :87 | GAPDATO algoritmo de busqueda del eje | IMP #121 | si (justificado) |
| :87 | Semimaximo por objeto; 2500 HU como cota superior; contraste aparte | DEC 2026-09-14 (3) (:745-746); TM:123 | si |
| :89 | D >= d + 2 epsilon; epsilon 1-2 mm; lectura por lado propia; Kaiser: 1-2 mm alrededor de 6.3-8 mm; conservador; trabajos previos | DEC 2026-09-11 (2) (:590-601); `kaiser2014dysmorphism` filas "Justificacion dimensional", "umbral propio y conservador", "Atribucion explicita del 10 mm a terceros" (p. e120(7)) | si |
| :89 | McLaren lo toma de Kaiser; no validado | `mclaren2021corridor` (p. 2) | si |
| :91 | 9.5 mm (RIC 7.4-11.7) | RES:16 | si |
| :91 | 65.3 % y 23.6 % (recorte por defecto); 62.5 y 20.8 % (alternativo) | RES:16, :20 (`%_d6.5_c1`, `%_d8.0_c2`) | si |
| :91 | 29 y 27 de 72 a 10 mm | DEC 2026-09-14 (4) (:770-771); RES:16, :20 (40.3 y 37.5 %) | si |
| :91 | Limpieza sin efecto hasta 5 %; fijada post hoc, igual que la ocupacion | DEC 2026-09-14 (3), (5); RES:16-23; TM:123 | si |
| :91 | GAPDATO 16 casos; recorte condicionado | IMP #123 ABIERTA | si (justificado) |
| :95 | Referencias en la union lumbosacra; ninguna de las fuentes revisadas | TM:121 | si |
| :95 | GAPDATO heuristica (codigo y notas) | R1:7-15 | si (justificado) |
| :95 | Contaminacion > maximo en 69 pacientes "sin objeto metalico" de dataset6 | R1:4, :9-15; DAT:127 frente a DAT:137 / GRP | parcial (T01) |
| :95 | Revisor clinico (cirujano, ORL), ciego; "confirmo" S1 en cada paciente | TM:121; R1:45-46; IMP #124 | parcial (T04) |
| :97 | 65 / 57 / 48 / 29 | R1:42, :46 | si |
| :97 | 7 pacientes fuera en el primer paso por crestas truncadas | R1:57-88 (7 casos con cresta fuera de FOV; el octavo, `metal_0016`, por S1 no hallado; 65 - 8 = 57) | si |
| :97 | 17 con tornillo; S1 correcto en todos; 3 contaminados | TM:121 | si |
| :97 | GAPDEC segunda lectura 61 de 61 | IMP #124 ABIERTA | si (justificado) |
| :97 | Crestas y espinas sin revision clinica | DEC 2026-09-17 E | si |
| :101 | Tres geometrias; nominal = rosca; mas del doble | TM:117; DEC 2026-09-20 | si |
| Tab. geom. | 6.5-8.0; 6.3-8; 4.91; 4.8; 4.9 y 4.7; 7.0; 4.91 y 7.3 de sensibilidad | `gardner2010safezones` (p. 624); `kaiser2014dysmorphism` (p. e120(7)); DEC D3; `synthes2003guide`; `gardner2015screw` (p. 42); `zwingmann2009navigated` (p. 1835); DEC D-O2.4 | si |
| :119 | 79 componentes de 43 volumenes; filtro > 2500 HU, >= 30 mm, <= 12 mm; no clinico | DEC D3 (:1243, :1252-1254) | si |
| :119 | Nucleo = fuste; Zhu y Liao 7.3 y 4.8; cabeza 8.0 x 4.5; sensibilidad | `synthes2003guide`; `zhu2022optimalposition` (2.3, p. 1548); `sayres2014comparison` (p. 34); DEC D3 (:1249-1250) | si |
| :121 | Calibre fijado por la referencia; profundidad escala con el radio; longitud por la regla de Kaiser | DEC D-O2.4 (:1475-1481); TM:117 | si |
| :123 | Arandela 1.5 mm de otro fabricante; canulacion libre; 316L y Ti-6Al-7Nb; fabricantes senalados como no revisados por pares | DEC 2026-09-20 ptos 1-2; TM:117; `doublemedical2021trauma`; BITACORA §2 | si |
| :127 | Congelado el 22-09-2026 antes de cualquier distancia; desviaciones con fecha y motivo | PRE:3-8, §9 | si |
| :129 | Anclaje al punto medio; longitud del tramo; motivo | PRE §2.1 | si |
| :131-136 (Ec. pose) | Perturbacion isotropa, seminormal truncada, eje de giro uniforme | PRE §3 | si |
| Tab. preinsc. | h 5.0; h = 2 sigma; 2.5 mm; sigma_a; 2.07 grados; L = 138 mm; 3 sigma; 50; semilla 20260922 | PRE §3.1 (atan(5/69)/2 = 2.07 grados, comprobado) | si |
| :158 | Una sola constante; GAPDEC h = 2 sigma; 4 grados no usados; isotropia | PRE §3.1, §3.2 | si (justificado) |
| :160 | Semilla por caso; sensibilidad como subconjunto | PRE §3.1, §8 | si |
| :162 | Tres comprobaciones fijadas antes; dos entre los seis controles; la tercera en cada corrida | TM:107; E12 (C2, C3); E13:12 ("Poses sin grado: 0") | si |
| :164 | 18 volumenes; 13 / 4 / 1; 39 frente a 36 y 33 mm; lector ciego | TM:78; IMP #121 | si |
| :164 | GAPDATO segundo corredor; eje en 69 de 72 | PRE §7; IMP #121 act. (7) | si (justificado) |
| :166 | Densidad reportada, no condicionante; Arand | DEC D-O2.6; `arand2019pelvicring` (Abstract, p. 376) | si |
| :166 | GAPDEC fuente y definicion de la densidad | DEC D-O2.6 (:1504) frente a DEC 2026-09-14 (:647, :697) | si (justificado) |
| :166 | Gardner: S1 menor en dismorficos; estudio previo sin diferencia | `gardner2010safezones` (pp. 624, 628) | si |
| :170 | *Inpainting* 2.5D en imagen; entradas; copia fuera de G; multiventana sin compresion | TM:79 | si |
| :170 | GAPDEC congelar el diseno (codificacion supuesta arcsinh) | `diseno_A.md`:9-11, :57 (BORRADOR, `[SUPUESTO]` pub+asinh); DEC :1288 | si (justificado) |
| :172 | SD 1.5 + ControlNet inicial; ControlNet presupone base congelada y latente | TM:79; `zhang2023controlnet` (§3.1, §3.2) | si |
| :174 | ~12 mm; parametro de diseno que trunca las rayas lejanas; sin medicion en las fuentes revisadas | TM:79; DEC 2026-09-17 C (#57) | si |
| :174 | 7.57; 11.45 y 11.63 (1.4, 1.8); 54.82 y 57.69 (0.7, 0.5) | `karageorgos2024ddpm` Apendice Tabla III (p. 16); TM:79 | si |
| :176 | Sinograma, no banda; no fija los 12 mm | TM:79 | si |
| :178 | Pares con metal; 2500 HU; semimaximo como sensibilidad; unidad = componente | DEC D1, D2 | si |
| :180 | R1-R3 fijados antes; 0.62 = todos los parches de solo banda; tamano y forma se reportan | DEC 2026-09-21 R1-R4 (:1316-1336); tabla :1340-1345 (6 584 / 10 586 = 0.62, comprobado) | si |
| :182 | Tres desplazamientos; 0.62 frente a 1.40; primero y tercero cuantificados; segundo por continuidad en el borde | TM:79; DEC R3 (:1331-1334); `diseno_A.md`:116 (costura en el borde de B_delta) | si |
| :185 | Obj 4 sin fila; seis controles "sobre geometria conocida" | E12 | parcial (T03) |
| :185 | GAPDEC evidencia del Obj 4 | sin fuente | si (justificado) |
| :189 | Tres componentes de SAP; solo los grados se comparan; densidad y viabilidad descriptivas, viabilidad por caso | TM:96; DEC D-O2.6; PRE §2 (`D_TS_max` "usada solo para la viabilidad"); E13:56-64 | si |
| :189 | GAPDEC calibre de viabilidad en SAP | DEC D-O2.4 (:1487) frente a E13:60-64 | si (justificado) |
| :189 | Escala de Smith | `smith2006iliosacral` (Screw Position, p. 236) | si |
| :190-194 (Ec. brecha) | max(0, r + s); limites de grado por convencion | PRE §4; DEC 2026-09-16 pto 4 | si |
| :196 | Tramo = implante, longitud del corredor, 8 mm por extremo; razon; sin hueso = grado 3 | PRE §4; DEC D-O2.3 pto 4; IMP #120 | si |
| :198 | Envolvente aproxima la cortical; 0.083 mm | DEC D-O2.3; E12:15, :95-97 | si |
| :198 | Seis controles "sobre geometria conocida" antes de la corrida | E12:3-89; PRE §8 | parcial (T03) |
| :198 | GAPDEC escala angular de Smith | IMP #11 ABIERTA | si (justificado) |
| :200 | 69/15/8/8 y 40/37/11.5/11.5; solo S1; por tecnica | `zwingmann2009navigated` (Results, pp. 1836-1837); PRE §5 | si |
| :201-205 (Ec. W1) | Grados equiespaciados; unidad = grado | PRE §5 | si |
| :207 | Sin correccion por parametros; sin regla de decision; GAPDEC escala | PRE §6; DEC D-O2.1 (:1433-1434) | si (justificado) |
| :207 | 26/24 y 35/32; no es equivalencia; S1 supuesto en la navegada; grados por tornillo | `zwingmann2009navigated` (Abstract, p. 1833); PRE §6; DEC 2026-09-17 C (#69) | si |
| :209 | Estratificacion post hoc por 7.0 mm; grado 0 inalcanzable; restriccion rechazada; sin exclusion en Zwingmann | IMP #122 CERRADA (:8524-8533); TM:109 | si |
| :213 | *Bone* / *metal integrity*; *streak amplitude* (5 % alto y bajo) | `peters2025hybrid` Metricas 4, 6, 7 (2.5, pp. 5-6) | si |
| :215 | Disenadas para MAR; GAPDEC inversion; escala 0-4 sin analogo; realismo contra observaciones reales | `peters2025hybrid` filas "Escala de score 0 a 4.0", "NMAR calibrado a score 2"; IMP #16, #17 ABIERTAS; TM:98, :127 | si (justificado) |
| :217 | *Streak amplitude* unico primario, declarado antes; GAPDEC fallo de la superioridad | DEC D4 ptos 1-2 | si (justificado) |
| :219 | Tres brazos, misma anatomia y poses; GAPDEC copia y pegado; CatSim/XCIST; AAPM; en lugar de reimplementacion | TM:119; `diseno_A.md`:116; `deman2007catsim`; `wu2022xcist`; `haneda2025aapm` | si (justificado) |
| :221 | 2D y MAR; fantoma; sin paso hibrido; proyeccion conjunta por verificar; control sin metal; GAPDEC n; GAPDATO brazo fisico | TM:119; DEC 2026-09-17 B.2, C (#70); IMP #17 ABIERTA | si (justificado) |
| :223 | Wilcoxon de una cola pareado, 0.05, efecto e IC; TOST con IC 90 %; nunca por no significacion; Delta en validacion | DEC D4 ptos 2-4 | si |
| :223 | GAPDEC agregacion por paciente; GAPDEC contingencia TOST | DEC D4 (sin agregacion); IMP #90 | si (justificado) |
| :225 | RMSE y SSIM fuera de B_delta; exacta por construccion; medicion en el brazo fisico | TM:79, :102, :119 | si |
| :229 | Grado de cierre por objetivo | DEC 2026-09-17 (3); PRE; DEC D4 | si |
| Tab. diseno | Filas 1-3 | TM:77, :96-98; DEC D4; PRE | si |
| :251 | Circularidad controlada; tres decisiones post hoc | DEC D-O2.1; DEC 2026-09-14 (3), (5); IMP #122 | si |
| :251 | Regla y seis combinaciones fijadas despues de E6b, que incluia pacientes de prueba y fallo 25 HU; umbral anterior y no movido | DEC 2026-09-15 (2) (:817, :832-833, :841); DEC 2026-09-17 (3) | si |
| :251 | Rediseno posterior; cota de Guo sobre los mismos pacientes | DEC 2026-09-19; TM:77 | si |
| :251 | 11 de 34 y 7 de 57; mas perdida en el grupo 2 | DEC :748 | si |
| :251 | Fractura no verificada (hipotetica) | IMP #125 (caso confirmado) | parcial (T02) |
| :253 | Protrusion, no cortical; 0.083 mm; 2 mm de la literatura pedicular; Smith declara la escala | DEC D-O2.3; E12; TM:52; `smith2006iliosacral` (p. 236) | si |
| :253 | Sin frontera en 2 o 4 mm ni grosor de corte; Tejwani 2.5 frente a 5.0 mm, p = 0.3 | `zwingmann2009navigated` (verificacion 2026-09-16); `tejwani2014` (M&M, p. 514) | si |
| :255 | Grados equiespaciados; h = 2 sigma; metricas para reducir; mascara sin aleacion | PRE §3.1, §5; TM:117 | si |
| :255 | Lin y Li: penalizacion solo en imagen, en reduccion; Lin: mal planteado | `lin2019` (Sec. 2, p. 10506); `li2024` (Sec. I, p. 1866); DEC 2026-09-17 C (#71) | si |
| :257 | Tile B y C; Reilly: 6 pelvis, osteotomia, 5-20 mm, 36-90 % en S1 | `zwingmann2009navigated` (M&M, p. 1834); `reilly2003effect` (pp. 89, 91); TM:121 | si |
| :257 | Cohorte parcial; reconstruccion desconocida; TS no reporta exactitud para S1; protocolo 2D y MAR | DAT:55-58; `wasserthal2023` fila 3e; TM:119 | si |
| :259 | Series pequenas que cuentan tornillos; W1 sin prueba inferencial; GAPDEC intervalo | PRE §5-§6 | si (justificado) |
| :259 | Multiplicidad solo favorece el aprobado; septimo candidato examinado | DEC :1054; TM:77 | si |
| :259 | Delta sobre 3 pacientes de validacion con implante real | DEC 2026-09-21 (2) (:1394, :1398) | si |
| :259 | "varias semillas por caso" | DEC 2026-09-21 (2) (:1400, "k semillas") | parcial (T06) |
| :259 | Muestras pequenas acotadas por el subconjunto fisico | DEC D4 (:1279); remision a §Apariencia | si |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet vigente, "31-60%", BFC/ISC) | CLAUDE.md raiz; `docs/00-tesis.md` | ausente: solo aparece como excluido o sustituido (l.36, l.172) |
| global | 30 claves `\cite`, las mismas de r02; todas en `overleaf/referencias.bib` | revision de las llamadas; r02 (30 de 30) | si |
| global | Apellidos = primer autor del .bib (Gardner, Ziran, Zhu y Liao, Guo, etc.) | `overleaf/referencias.bib` | si |
| global | Ninguna cita como sujeto gramatical sola (E-F3) | revision de todas las llamadas | si |
| global | Fuentes de fabricante senaladas (P-EA1) | l.123 | si |
| global | Implicancias ABIERTAS afirmadas como hecho (#11, #16, #17, #90, #116, #117, #123, #124, #125, #126) | revision del texto | ninguna afirmada como resuelta; #125 con dato omitido (T02) |
| global | PAT-1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 | revision del texto | sin reincidencia en este dominio |
| global | PAT-2 | l.259 | reincide (T06) |
| global | PAT-6 | l.83 | reincide leve (T05) |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una subcohorte se describe con la etiqueta de una clasificacion anterior que el reparto vigente corrigio | G-T4 | "69 pacientes sin objeto metálico de la carpeta `dataset6`" (grupo 3 = 66) | nuevo |
| Una limitacion con evidencia confirmada en el registro se redacta solo como hipotesis | G-T4, OC-3 | "fracturas no detectadas estrecharían corredores" (hay una confirmada, #125) | nuevo |
| Cuantificador vago sin valor ni GAP para un parametro que ninguna fuente fija | P-MM3 | "con varias semillas por caso" | PAT-2 |
| La lectura operativa del proyecto (DEC) se enuncia como propiedad de la fuente citada | E-R6 | "es el radio del corredor de 10 mm de Kaiser et al." | PAT-6 |
