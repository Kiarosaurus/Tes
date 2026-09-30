# Auditoria de trazabilidad — capitulo3 — r02

Entrada: `overleaf/secciones/capitulo3.tex` (tras r01), respuesta `capitulo3-r01-respuesta.md`, lint
`capitulo3-r02-lint.md`. RECHAZADO en r01: solo el lint "AI" de MAISI (no es de este dominio; no se reabre).
ESCALADOS de r01 que dependen de alinear `tesis/main.tex` (T03/T04 aviso TM:77, T14 TM:78/:117, S07 TM:121,
T02 aviso TM:52/:123) no se re-reportan: el texto sigue la fuente de mayor autoridad y la discrepancia ya
esta en manos de la autora. Se revisaron los 13 patrones VIGENTES de BITACORA §1 y se respetan las
decisiones de §2.

Siglas: TM = `tesis/main.tex`; PRE = `experiments/objetivo2/preinscripcion_muestreador.md`;
EXP = `experiments/objetivo2/EXPERIMENTOS.md`; DAT = `docs/02-datos.md`; DEC = `docs/01-decisiones.md`;
IMP = `docs/04-implicancias.md`; RES = `experiments/objetivo2/e9ts_resumen.md`;
E13 = `experiments/objetivo2/e13_sap.md`.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-5 | capitulo3.tex:89, :192; Tabla `tab:geometrias` fila 1 | "$d$ es el calibre nominal del tornillo paramétrico" / SAP incluye "la viabilidad del corredor" | DEC D-O2.4 (:1485-1489: envolvente 6.5-8.0 mm para `Dmax >= d + 2c`); E13:60-64; RES:14-16 | Las fuentes discrepan. DEC asigna la viabilidad a la envolvente nominal 6.5-8.0 mm, y RES la calcula asi (d = 6.5, 7.3, 8.0). Pero el componente 3 de SAP tal como se implemento y reporto (E13, "Viabilidad de corredor (componente 3 de SAP)") usa d = 4.91, 7.0 y 7.3 mm con `D_TS_max >= d + 2`. El texto afirma para SAP el criterio de DEC, que no es el que se corrio. | `\GAPDEC{calibre con que SAP evalúa la viabilidad del corredor: la decisión fija la envolvente de 6.5 a 8.0 mm; la corrida del Objetivo 2 usa 4.91, 7.0 y 7.3 mm}` en §SAP, y avisar a la autora. |
| T02 | media | G-T4, OC-2 | capitulo3.tex:91 | `\GAPDATO{número de corredores viables con el criterio $D \geq d + 2c$; las cifras disponibles usan la convención de 10 mm}` | RES:16, :20 (columnas `%_d6.5_c1`, `%_d7.3_c1`, `%_d8.0_c2`); EXP:72 (`e9ts_resumen.md` VIGENTE); IMP #123 (:8584-8585, cita el 65.3 %) | GAP injustificado: RES da el criterio vigente sobre los 72 pacientes. Con el recorte por defecto: 65.3 % (d = 6.5, c = 1), 54.2 % (7.3, 1), 23.6 % (8.0, 2); con el alternativo: 62.5 / 51.4 / 20.8 %. DEC #31 pide reportar "ambos extremos". Ademas, "La elección de recorte cambia, así, el número de corredores viables" llama "viables" a los recuentos de 10 mm. Patron PAT-9 reincide. | Si la autora acepta RES como fuente (esta en el indice EXP), reportar los extremos: "el criterio $D \geq d + 2c$ se cumplió en el 65.3 % de los 72 pacientes con $d = 6.5$ y $c = 1$, y en el 23.6 % con $d = 8.0$ y $c = 2$ (62.5 y 20.8 % con el recorte alternativo)". Si no, cambiar el GAP a `\GAPDEC{llevar a la fuente de contenido los recuentos del criterio $D \geq d + 2c$, ya calculados}`. En los dos casos, "el número de pacientes que cumplen la convención" en lugar de "corredores viables". |
| T03 | media | G-T4, OC-2 | capitulo3.tex:166 | `\GAPDEC{definición operativa, por pose, de la fracción por zona de densidad que SAP reporta}` | E13:56-58 (mediana 0.420 sobre 3 600 poses); DEC D-O2.6 (:1504: "calculado sobre `e9b_densidad_s1.csv`"); DEC 2026-09-14 #50 (:647, :697: E9b "se retira como evidencia de densidad"); EXP:61 (E9b VIGENTE, "componente 2 de SAP") | El GAP describe mal lo que falta. El componente esta implementado y ya se calculo en la cohorte primaria. Lo que esta sin resolver es una discrepancia entre fuentes: D-O2.6 y EXP lo calculan sobre E9b, que la decision del 2026-09-14 retiro como evidencia de densidad. | `\GAPDEC{fuente de la fracción por zona de densidad: SAP la calcula sobre la sonda E9b, que una decisión anterior retiró como evidencia de densidad}`, y describir la definicion implementada o marcarla `\GAPDATO` (hoy solo consta en `src/muestreador/sap.py`). |
| T04 | media | OC-2, OC-3 | capitulo3.tex:180 | `\GAPDEC{cifra de la proporción de parches de solo banda, registrada en las decisiones (...)}` | DEC 2026-09-21 R3 (:1328-1334: "`ratio-banda` = 0.62", todos los disponibles; sintesis 1.40); tabla :1340-1345 | GAP injustificado. 0.62 es un parametro de diseno congelado en DEC, no un resultado propio, y OC-3 admite como hecho lo decidido en DEC. La regla 5 (cifras propias desde TM o EXPERIMENTOS) no lo cubre. Escalado en r01 (guia-8) sin rechazo. Nuevo argumento: es una decision, no una cifra medida. | "junto con parches de solo banda en razón de 0.62 respecto de los parches con metal, que son todos los disponibles". En el tercer desplazamiento de dominio (:182) se puede anadir "frente a 1.40 que predice la geometría del corredor" (misma entrada DEC). Si la autora prefiere que DEC no aporte cifras, mantener el GAP. |
| T05 | media | G-T4, OC-2 | capitulo3.tex:262 | `\GAPDEC{(...) las decisiones registran primero 5 y después 3, y la cifra no consta (...)}` | DEC 2026-09-21 (2) (:1384-1401: "`val` tiene 8 casos, no 5"; "el margen `Delta` de D4 se medirá sobre 3 pacientes"); IMP #90 act. 2026-09-21 (:8128, "n = 3 (#105)") | Las dos cifras no son una ambiguedad: la entrada posterior corrige el dato de D4 y fija 3 de forma explicita, y ademas pide declarar esa n ("El informe debe declarar esta n"). El GAP presenta como abierto algo que ya esta sustituido. Patron PAT-11 reincide. | "el margen $\Delta$ se medirá sobre 3 pacientes de validación con implante real, con varias semillas por caso". Quitar el `\GAPDEC`. |
| T06 | baja | G-T4 | capitulo3.tex:212 | "Restringir la cohorte a los corredores viables se consideró y se rechazó." | IMP #122 opcion (c) (:8529-8530), donde "viables" = `D_TS >= 7.0` mm | El capitulo define "viable" como `D >= d + 2c` (:89). Aqui la opcion rechazada era restringir por el calibre de 7.0 mm, no por ese criterio. | "Restringir la cohorte a los corredores que admiten el calibre de 7.0 mm se consideró y se rechazó." |
| T07 | baja | G-T4 | capitulo3.tex:95 | `\GAPDATO{descripción de la heurística (...), que hoy solo consta en el código}` | `experiments/objetivo2/r1_landmarks.md`:7-15, :29, :44 | GAP justificado, pero no es cierto que solo conste en el codigo: `r1_landmarks.md` documenta la envolvente de contaminacion (HU < -200 oscuro, > 2500 brillante, maximo en calibracion) y los dos metodos de S1 (sagital y del ala). | "(...) que hoy consta en el código y, en parte, en las notas del experimento". |
| T08 | baja | E-R6 | capitulo3.tex:260 | "la versión de TotalSegmentator usada no tiene exactitud publicada para S1" | `wasserthal2023` filas 2d, 3e (NO ENCONTRADO); capitulo3.tex:85 | La ficha solo dice que la publicacion citada no reporta exactitud para S1. "No tiene exactitud publicada" es una afirmacion de ausencia general que la ficha no sostiene. La l. 85 lo dice bien. | "(...) la publicación de TotalSegmentator no reporta exactitud para la etiqueta de S1 (...)". |
| T09 | baja | G-T4 | capitulo3.tex:254, :262 | "extensión (...) a MAISI, evaluada con los mismos pacientes de prueba" / "séptimo candidato, evaluado" | TM:77 ("the evaluation was not run"); capitulo3.tex:75 | El modelo MAISI no se corrio. Sobre los pacientes de prueba solo se calculo la cota por recorte, sin modelo. "Evaluada" o "evaluado" sugiere una corrida del modelo. | "(...) cuya cota por recorte se calculó sobre los mismos pacientes de prueba" y "añade un séptimo candidato, examinado sobre los mismos pacientes de prueba". |
| T10 | baja | G-T4 | capitulo3.tex:67 | "un error cuadrático medio (RMSE, \emph{root mean square error}) de 20.2 HU" | `karageorgos2024ddpm` Tabla I (RMSE); DEC 2026-09-15 (2) | RMSE es la raiz del error cuadratico medio. El nombre en espanol corresponde al MSE, que se mide en HU² y no en HU como la cifra citada. | "la raíz del error cuadrático medio (RMSE, \emph{root mean square error})". |
| T11 | baja | G-T4 | capitulo3.tex:262 | "la prueba de equivalencia tiene muestras pequeñas" | DEC D4 (:1279: "n = 14 sin metal y n = 20 con metal son muestras chicas para un TOST") | Hay fuente para el n y el texto no lo da. Ademas el TOST corre sobre el subconjunto del brazo fisico, cuyo n es un `\GAPDEC` (:224). Patron PAT-2 reincide. | Dar el n de D4 o remitir: "(...) tiene muestras pequeñas, acotadas por el subconjunto del brazo físico (Sección~\ref{sec:apariencia})". |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9 | Dos componentes separados; compuerta previa | TM:74-80; CLAUDE.md raiz | si |
| :13 | Cuatro objetivos; SAP unica metrica propia; Obj 4 adopta protocolo con nombres publicados | TM:68, :76-80 | si |
| :13 | GAPDEC alineacion con la introduccion | IMP #126 ABIERTA | si (justificado) |
| :15 | Corredor medido, eje perturbado, M, B_delta, G, copia fuera de G | TM:79, :107 | si |
| Fig. pipeline | TotalSegmentator; marco Kaiser; SAP vs dos distribuciones; inpainting en imagen; copia-pega y protocolo fisico; compuerta descarto la ruta latente | TM:77-79, :98; DEC 2026-09-19 | si |
| :36 | Dice/HD95 fuera de alcance; dos condiciones | TM:83, :127 | si |
| :36 | 14 de 75 de CLINIC-metal anotados en la publicacion | `liu2021ctpelvic1k` filas "14 CTs con metal anotados" y Tabla 1 "0(61)/0/14" (p. 3); DAT:157-161 | si |
| :36 | Mascaras no verificadas localmente | DAT:50, :158-160 | si |
| :36 | 178 de 1 184 | DAT:55; `liu2021ctpelvic1k` (Tabla 1, p. 3) | si |
| :36 | Ablaciones diferidas | TM:83; DEC 2026-09-17 B.1 | si |
| :38 | Compuerta ejecutada y negativa; Obj 2 ejecutado sobre la cohorte completa | TM:77, :96; EXP:85-86 | si |
| :38 | GAPDATO sin muestra sintetica | IMP #116 act. 2026-09-24 (:8750-8753) | si (justificado) |
| :38 | Rediseno posterior; regla fijada antes de la prueba que decide | DEC 2026-09-17 B.3, 2026-09-19 pto 2 | si |
| :42 | 1 184; 178 locales; dataset6 103 y dataset7 75; correspondencia inferida | DAT:27-30, :55-63 | si |
| :44 | El articulo no reporta adquisicion ni reconstruccion | `liu2021ctpelvic1k` fila escaner NO ENCONTRADO; DEC 2026-09-17 C (#73) | si |
| :44 | Selles: MAR del fabricante y monoE cambian la apariencia | `selles2024marreview` (Sec. 3.3 y 3.5) | si |
| :46 | Cribado > 2500 HU, un voxel, sin filtro de tamano; heuristica; no es de Peters | DAT:67-69 | si |
| :46 | La autora reviso en 3D los 178 | DAT:104-105 | si |
| :46 | GAPDATO revision multiplanar | DAT:139 | si (justificado) |
| :48 | Huella de volumen y de corte, mas observacion visual; 178 -> 168 | DAT:117-122 | si |
| :48 | 65 / 37 / 66; 179 unidades; 10 fuera de uso; 1 de reproducibilidad | DAT:134-137 | si |
| :48 | Union sin interpolar de dos campos solapados | DAT:130-131 (`union_0059_0071.md`, "union sin perdida") | si |
| :50 | Aislamiento estricto; particion por paciente estratificada; 34 de prueba | TM:77, :115; DEC 2026-09-17 (3) | si |
| :50 | Obj 3 reutiliza la particion con pacientes de entrenamiento con metal; Obj 2 sin particion, grupos 2 y 3 | DEC 2026-09-21; DEC 2026-09-14 (2) | si |
| :52 | 103 -> 91 -> 72; 11 de 34; 7 de 57; 1 en el borde del FOV | TM:123; DEC 2026-09-14 (3) | si |
| :52 | Control de nivel: TS/R1 discordante, S1 en el borde del FOV o vacia | DEC 2026-09-14 (:642, :668-671) | si |
| :52 | 49 de sensibilidad | PRE §1; DEC D-O2.2 | si |
| :52 | GAPDATO cribado de fractura 30 (15 + 15) | IMP #125 (:8729-8730); `r3_fractura_revisor.csv` sin juicios | si (justificado) |
| :54 | Cuatro funciones de los 65; geometria parametrica; tornillos fragmentados que cambian entre adquisiciones | TM:117; DEC D1 (E8) | si |
| :58 | Compuerta Go/No-Go obligatoria previa al Obj 3; regla fijada antes de la prueba que decide | DEC 2026-09-17 B.3, (3) | si |
| :58 | Exploracion previa del preentrenado sobre la cohorte completa, por encima del criterio | DEC 2026-09-15 (2) (:841, 178 de 178) | si |
| :60 | Tres canales; VAE; lectura sin imagen original, canal mas estrecho no saturado | DEC 2026-09-17 (3) (:1050); TM:77 | si |
| :60 | 150 HU del protocolo adoptado | `peters2025hybrid` (2.5, p. 5); `haneda2025aapm` (Sec. 2.3, p. 7) | si |
| :61-65 (Ec. MAE) | MAE por paciente en hueso | DEC:1051 | si |
| :67 | Sin umbral publicado de aprobacion | DEC 2026-09-15 (2); TM:77 | si |
| :67 | 20.2 / 12.3 / 12.74 HU; RMSE >= MAE; orden de magnitud | `karageorgos2024ddpm` Tabla I (p. 28); `yun2026simulationdriven` Tabla 1 (p. 10); DEC:821-829 | si (T10, nombre de la metrica) |
| :69 | 2 x 3 = 6; ventanas de Wang; techo de 20 000; arcsinh | DEC:1048-1049; `wang2025adaptiveweighting` (V-A-1, p. 2412); TM:77 | si |
| :71 | Media sobre 34 < 25 HU; Go si alguna de seis; IC 95 % bootstrap; marginal | DEC:1051-1055 | si |
| :71 | Orden a priori; preentrenado antes que adaptado; techo de 2000 recorta metal | DEC:1056-1057, :1065 | si |
| :71 | Si ninguna aprueba, el Obj 3 no se ejecuta; rediseno posterior | DEC:976-979; DEC 2026-09-19 | si |
| :73 | B_delta descriptivo, fuera de la regla; Rombach, alta frecuencia | DEC 2026-09-16 pto 2; `rombach2022latentdiffusion` (§1, p. 2) | si |
| :75 | Extension a MAISI con la misma regla y pacientes; cota por recorte; no se corre si supera | DEC 2026-09-19 pto 3; TM:77 | si |
| :79 | Perturba, no optimiza; distribuciones dependientes de la tecnica | PRE §2; `zwingmann2009navigated` (Results, pp. 1836-1837) | si |
| :79 | Ziran: CV 7-25 % en la mayoria; hasta 140 % en el ala superior de S1 | `ziran2007fluoroscopic` filas "7%-25%" (p. 351) y "97%-140%" (p. 352) | si |
| :79 | Grado de brecha = protrusion fuera del hueso | PRE §4; DEC D-O2.3 | si |
| :83 | Marco de Kaiser: reformateo, angulos, 5 mm | `kaiser2014dysmorphism` filas reformateo y "no less than 5 mm" (p. e120(2)) | si |
| :85 | Mediana 0.42 de voxeles <= 150 HU | TM:123; `maintex_cifras.md`:17 (COINCIDE) | si |
| :85 | TS 2.18.0, `total`, recorte por defecto y alternativo; nnU-Net; limpieza 0.1 %; control de nivel | TM:78; DEC 2026-09-14, (3), (4); `wasserthal2023` fila 1a | si |
| :85 | 104 estructuras; sin exactitud para S1 | `wasserthal2023` filas 2d, 3e | si |
| :87 | Envolvente: sacro, S1, coxales, cierre 2 mm, relleno; diametro = 2 x distancia libre | DEC D-O2.3 (:1450-1452, :1467-1469) | si |
| :87 | GAPDATO algoritmo de busqueda del eje | IMP #121 (:8315-8318) | si (justificado) |
| :87 | Semimaximo por objeto (principal); 2500 HU como cota superior; contraste aparte | DEC 2026-09-14 (3) (:745-746); TM:123 | si |
| :89 | `D >= d + 2c`; c = 1-2 mm; lectura radial propia | DEC 2026-09-11 (2) (:590-598); IMP #31 APLICADA | si |
| :89 | d = calibre nominal para la viabilidad | DEC D-O2.4 frente a E13:60-64 | no (T01) |
| :89 | Kaiser: 1-2 mm alrededor de 6.3-8 mm; conservador; atribuido a trabajos previos | `kaiser2014dysmorphism` filas "Justificacion dimensional", "umbral propio y conservador", "Atribucion explicita del 10 mm a terceros" (p. e120(7)) | si |
| :89 | McLaren lo toma de Kaiser; procedimiento reproducible; no validado | `mclaren2021corridor` filas "El umbral es heredado" y "not yet been established" (p. 2) | si |
| :91 | 9.5 mm (RIC 7.4-11.7); 29 y 27 de 72 a 10 mm | TM:123; RES:16, :20 (40.3 % y 37.5 %) | si |
| :91 | GAPDATO recuento con `d + 2c` | RES:16, :20 | no (T02) |
| :91 | Limpieza sin efecto hasta 5 %; fijada post hoc, igual que la ocupacion | DEC 2026-09-14 (3), (5); TM:123; RES:16-19 | si |
| :91 | GAPDATO 16 casos; recorte condicionado | IMP #123 ABIERTA; `e9ts_revision_laminas_autora.csv` (veredicto vacio) | si (justificado) |
| :95 | Referencias en la union lumbosacra; ninguna fuente publicada | TM:121 | si |
| :95 | GAPDATO heuristica | `r1_landmarks.md`:7-15 | parcial (T07) |
| :95 | Contaminacion > maximo en 69 sin metal | TM:121; `r1_landmarks.md`:4, :9-15 | si |
| :95 | Revisor clinico (cirujano, ORL), ciego, confirmo S1 | TM:121; IMP #124 (:8677-8679) | si |
| :97 | 65 / 57 / 48 / 29; 7 por truncamiento de crestas; 17 con tornillo; S1 correcto; 3 contaminados | TM:121; `r1_landmarks.md`:42-46, :57-88 | si |
| :97 | GAPDEC segunda lectura 61 de 61 | IMP #124 ABIERTA | si (justificado) |
| :97 | Crestas y espinas sin revision clinica | TM:121; DEC 2026-09-17 E | si |
| :101 | Tres geometrias; nominal = rosca; mas del doble | TM:117; DEC 2026-09-20 | si |
| Tab. geom. | 6.5-8.0; 6.3-8; 4.91; 4.8; 4.9 y 4.7; 7.0; 4.91 y 7.3 como sensibilidad | `gardner2010safezones` (p. 624); `kaiser2014dysmorphism` (p. e120(7)); DEC D3; `synthes2003guide`; `gardner2015screw` (p. 42); `zwingmann2009navigated` (p. 1835); DEC D-O2.4 | si |
| :119 | 79 componentes de 43 casos; filtro geometrico, no clinico | DEC D3 (:1243, :1252-1254) | si |
| :119 | Nucleo = fuste en la guia; Zhu y Liao 7.3 en la rosca distal y 4.8 en el fuste; cabeza 8.0 x 4.5 | `synthes2003guide`; `zhu2022optimalposition` (2.3, p. 1548); `sayres2014comparison` (p. 34) | si |
| :119 | Cabeza y rosca como sensibilidad | DEC D3 (:1249-1250) | si (TM:117 discrepa; escalado r01) |
| :121 | Calibre fijado por la referencia; la perforacion escala con el radio; longitud por la regla de Kaiser | DEC D-O2.4; TM:117 | si |
| :123 | Arandela 1.5 mm de otro fabricante; canulacion libre; 316L y Ti-6Al-7Nb; fabricantes senalados | DEC 2026-09-20 ptos 1-2; TM:117; `doublemedical2021trauma`; BITACORA §2 | si |
| :127 | Congelado el 22-09-2026 antes de cualquier distancia; sin desviaciones | PRE encabezado, §9; E13:5 | si |
| :129 | Anclaje al punto medio; longitud del tramo; motivo | PRE §2.1 | si |
| :131-136 (Ec. pose) | Perturbacion isotropa, seminormal truncada, eje de giro uniforme | PRE §3 | si |
| Tab. preinsc. | h 5.0; h = 2 sigma; 2.5 mm; sigma_a; 2.07 grados; L = 138 mm; 3 sigma; 50; semilla 20260922 | PRE §3.1 | si |
| :158 | Una sola constante; GAPDEC h = 2 sigma | PRE §3.1 ("propia, declarada") | si (justificado) |
| :158 | 4 grados no usados, citados de un tercero; isotropia | PRE §3.1, §3.2; `zwingmann2009navigated` (Introduction, p. 1834) | si |
| :160 | Semilla por caso; sensibilidad como subconjunto | PRE §3.1, §8 | si |
| :162 | Tres puntos de falsabilidad | TM:107; DEC D-O2.3 | si |
| :164 | 18 volumenes; 13 / 4 / 1; 39 frente a 36 y 33 mm; lector ciego | TM:78; IMP #121 (:8439-8451) | si |
| :164 | GAPDATO preinscripcion y corrida del segundo corredor; eje en 69 de 72 | IMP #121 act. (7) (:8426-8427); PRE §7 | si (justificado) |
| :166 | Densidad reportada, no condicionante | DEC D-O2.6 | si (TM:78 discrepa; escalado r01) |
| :166 | Arand: valores de gris bajos en el ala | `arand2019pelvicring` (Abstract, p. 376); DEC 2026-09-16 pto 1 | si |
| :166 | GAPDEC definicion operativa de densidad | E13:56-58; DEC D-O2.6 frente a DEC #50 | no (T03) |
| :166 | Gardner: S1 menor en dismorficos; un estudio previo sin diferencia | `gardner2010safezones` filas "36% smaller" (p. 624) y "no difference" (p. 628) | si |
| :170 | Inpainting 2.5D en imagen; entradas; copia fuera de G; multiventana sin compresion | TM:79 | si |
| :172 | SD 1.5 + ControlNet inicial; ControlNet presupone base congelada y latente | TM:79; `zhang2023controlnet` (§3.1, §3.2) | si |
| :174 | ~12 mm; parametro de diseno; trunca las rayas lejanas; sin medicion en la literatura | TM:79; DEC 2026-09-17 C (#57) | si |
| :174 | 7.57; 11.45 y 11.63 (1.4, 1.8); 54.82 y 57.69 (0.7, 0.5) | `karageorgos2024ddpm` Apendice Tabla III (p. 16) | si |
| :176 | Sinograma, no banda en imagen; 12 mm construccion | TM:79 | si |
| :178 | Pares con metal; 2500 HU; semimaximo como sensibilidad; unidad = componente | DEC D1, D2 | si |
| :180 | R1-R3 fijados antes; tamano y forma se reportan; la relacion no depende del tipo | DEC 2026-09-21 R1-R4 (:1305-1306, :1335) | si |
| :180 | GAPDEC proporcion de solo banda | DEC 2026-09-21 R3 (:1330) | no (T04) |
| :182 | Tres desplazamientos; primero y tercero cuantificados | TM:79; DEC D1, R3 | si |
| :184 | GAPDEC congelar el diseno del sintetizador | DEC:1288; `diseno_A.md`:7 | si (justificado) |
| :188 | Obj 4 sin fila; seis controles de SAP | EXP:83 (`e12_sap_control`, C1-C6) | si |
| :188 | GAPDEC evidencia del Obj 4 | sin fuente | si (justificado) |
| :192 | Tres componentes de SAP; escala de Smith | TM:96; `smith2006iliosacral` (Screw Position, p. 236) | si (T01 sobre el componente de viabilidad) |
| :193-197 (Ec. brecha) | max(0, r + s); limites de grado por convencion | PRE §4; DEC 2026-09-16 pto 4 | si |
| :199 | Tramo = implante, longitud del corredor, 8 mm por extremo; razon; sin hueso = grado 3 | PRE §4; DEC D-O2.3 pto 4; IMP #120 | si |
| :201 | Envolvente aproxima la cortical; seis controles; 0.083 mm | DEC D-O2.3; PRE §4 | si |
| :201 | GAPDEC escala angular de Smith | IMP #11 ABIERTA; `smith2006iliosacral` filas angulares | si (justificado) |
| :203 | 69/15/8/8 y 40/37/11.5/11.5; solo S1; por tecnica | `zwingmann2009navigated` (Results, pp. 1836-1837); PRE §5 | si |
| :204-208 (Ec. W1) | Grados equiespaciados; unidad = grado | PRE §5 | si |
| :210 | No se corrige moviendo parametros; sin regla de decision; GAPDEC escala | PRE §6; DEC D-O2.1 | si (justificado) |
| :210 | 26/24 y 35/32; no es equivalencia; S1 asumido en la serie navegada; grados por tornillo | `zwingmann2009navigated` (Abstract, p. 1833); PRE §6; DEC 2026-09-17 C (#69) | si |
| :212 | Estratificacion post hoc por 7.0 mm; grado 0 inalcanzable | IMP #122 CERRADA; TM:109 | si |
| :212 | "corredores viables" en la opcion rechazada | IMP #122 (c): `D_TS >= 7.0` | parcial (T06) |
| :212 | La serie no reporta exclusion por corredor estrecho | `zwingmann2009navigated` (sin frase); IMP #122 | si |
| :216 | Bone / metal integrity; streak amplitude (5 % alto y bajo) | `peters2025hybrid` Metricas 4, 6, 7 (2.5, pp. 5-6) | si |
| :218 | Disenadas para MAR; GAPDEC inversion; escala 0-4 no se traslada; realismo contra observaciones reales | IMP #16, #17 ABIERTAS; TM:98, :127 | si (justificado) |
| :220 | Streak amplitude unico primario, declarado antes; razon | DEC D4 pto 1; TM:98 | si |
| :222 | Tres brazos, misma anatomia y poses; GAPDEC copia-pega | TM:119; `diseno_A.md`:116 (sin valor de HU) | si (justificado) |
| :222 | CatSim/XCIST; AAPM CT-MAR; unico brazo con fisica; en lugar de una reimplementacion | TM:50, :56, :119 | si |
| :224 | 2D y MAR; fantoma; sin paso hibrido; proyeccion conjunta por verificar | TM:50, :119; IMP:6112 (P2 pendiente) | si |
| :224 | GAPDEC n del brazo fisico; control sin metal; documentacion | DEC 2026-09-17 B.2 (sin n); TM:119 | si (justificado) |
| :224 | GAPDATO brazo fisico no realizado | IMP #17 ABIERTA | si (justificado) |
| :226 | Wilcoxon de una cola pareado por paciente, 0.05, efecto e IC | DEC D4 pto 2 | si |
| :226 | GAPDEC agregacion por paciente | sin fuente | si (justificado) |
| :226 | TOST; IC 90 %; nunca por no significacion; Delta = variabilidad propia en validacion | DEC D4 ptos 3-4 | si |
| :226 | GAPDEC brazo TOST, contingencia | IMP #90 act. 2026-09-21 (:8138-8143) | si (justificado) |
| :228 | RMSE y SSIM fuera de B_delta; exacta por construccion; medicion en el brazo fisico | TM:79, :102, :119; `diseno_A.md`:117 | si |
| :232 | Grado de cierre por objetivo | DEC 2026-09-17 (3); PRE; DEC D4 | si |
| Tab. diseno | Filas 1-3 | TM:77, :96-98; DEC D4; PRE | si |
| :254 | Circularidad controlada; tres decisiones post hoc; rediseno posterior | DEC D-O2.1, 2026-09-14 (3), 2026-09-19; IMP #122 | si |
| :254 | MAISI "evaluada" con los mismos pacientes | TM:77 (no se corrio) | parcial (T09) |
| :254 | 11 de 34 y 7 de 57; fractura no verificada | DEC:748; IMP #125 ABIERTA | si |
| :256 | Protrusion, no cortical; 0.083 mm | DEC D-O2.3; PRE §4 | si |
| :256 | 2 mm de la literatura pedicular; Smith declara tomar la escala | TM:52; `smith2006iliosacral` fila "Origen de la escala de perforacion" (p. 236) | si |
| :256 | Sin frontera de 2 o 4 mm ni grosor de corte; Tejwani 2.5 frente a 5.0 mm, p = 0.3 | `zwingmann2009navigated` verificacion 2026-09-16; `tejwani2014` (M&M, p. 514) | si |
| :258 | Grados equiespaciados; h = 2 sigma; metricas para reducir; mascara sin aleacion | PRE §3.1, §5; TM:117 | si |
| :258 | Lin y Li: penalizacion solo en imagen, en reduccion; Lin: mal planteado porque ambos contribuyen a la traza | `lin2019` fila "MAR perfecta es mal planteada" (Sec. 2, p. 10506); `li2024` (Sec. I, p. 1866) | si |
| :260 | Tile B y C; Reilly: 6 pelvis, osteotomia, 5-20 mm, 36-90 % en S1 | `zwingmann2009navigated` (M&M, p. 1834); `reilly2003effect` filas (pp. 89, 91) | si |
| :260 | Cohorte parcial; reconstruccion desconocida; TS sin exactitud publicada para S1 | DAT:55-58; `wasserthal2023` fila 3e | parcial (T08) |
| :262 | Series pequenas que cuentan tornillos; W1 sin prueba inferencial | `zwingmann2009navigated`; PRE §5-§6 | si |
| :262 | GAPDEC intervalo por remuestreo | sin fuente | si (justificado) |
| :262 | Multiplicidad solo favorece el aprobado; septimo candidato | DEC:1054; TM:77 | parcial (T09) |
| :262 | GAPDEC n de validacion para Delta | DEC 2026-09-21 (2) (3 pacientes) | no (T05) |
| :262 | "muestras pequenas" sin n | DEC D4 (:1279) | parcial (T11) |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet vigente, "31-60%", BFC/ISC) | CLAUDE.md raiz; `docs/00-tesis.md` | ausente: solo aparece como excluido o sustituido |
| global | 30 claves `\cite` existen en `overleaf/referencias.bib` | `overleaf/referencias.bib` (30 de 30) | si |
| global | Apellidos = primer autor del .bib (incluidos Gardner, Ziran, Zhu y Liao) | `overleaf/referencias.bib`:229-230, :1254-1255 | si |
| global | Ninguna cita como sujeto gramatical sola (E-F3) | revision de las 45 llamadas | si |
| global | Fuentes de fabricante senaladas (P-EA1) | :113, :119, :123 | si |
| global | PAT-1, 3, 4, 5, 6, 7, 8, 10, 12, 13 | revision del texto | sin reincidencia en este dominio |
| global | PAT-2 | :262 | reincide (T11) |
| global | PAT-9 | :91 | reincide (T02) |
| global | PAT-11 | :262 | reincide (T05) |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que declara ausente una cifra ya calculada en un resumen de experimento VIGENTE del indice | G-T4, OC-2 | "número de corredores viables con el criterio $D \geq d + 2c$; las cifras disponibles usan (...)" | nuevo |
| GAP que presenta como ambiguas dos cifras de DEC cuando la entrada posterior sustituye a la anterior | G-T4 | "las decisiones registran primero 5 y después 3" | PAT-11 |
| El metodo se describe segun la decision y no segun lo que se implemento y corrio, que difiere | G-T4 | "$d$ es el calibre nominal" (SAP corrio con 4.91, 7.0 y 7.3 mm) | nuevo |
| Un termino definido en el capitulo ("viable") se reusa con el sentido de otra fuente | G-T4 | "Restringir la cohorte a los corredores viables" (= admiten 7.0 mm) | nuevo |
