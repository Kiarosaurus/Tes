# Auditoria de trazabilidad — capitulo3 — r01

Entrada: `overleaf/secciones/capitulo3.tex` (redaccion inicial r00), respuesta del redactor
`capitulo3-r00-respuesta.md`, lint `capitulo3-r01-lint.md`. No hay ronda anterior con RECHAZADOS.
Bitacora §1 sin patrones VIGENTES; se respetan las decisiones de §2 (terminos, NMAR sin sigla,
fabricantes senalados, veredictos al cap. 4).

Siglas de fuente: TM = `tesis/main.tex`; PRE = `experiments/objetivo2/preinscripcion_muestreador.md`;
EXP = `experiments/objetivo2/EXPERIMENTOS.md`; DAT = `docs/02-datos.md`; DEC = `docs/01-decisiones.md`;
IMP = `docs/04-implicancias.md`.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4 | capitulo3.tex:47 | "Otros 10 pacientes quedan excluidos y uno se reserva como par de reproducibilidad" | DAT:136-137; DEC:496-539 | Los 10 excluidos y el 1 de reproducibilidad son **unidades/volumenes**, no pacientes: DAT dice "179 unidades (178 + union) y 168 pacientes con una unidad en uso: grupo 1 = 65, grupo 2 = 37, grupo 3 = 66, excluido = 10, reproducibilidad = 1". 65+37+66 = 168 ya son todos los pacientes; el texto sugiere 179 pacientes. | "Los 168 pacientes se reparten en tres grupos (...). De las 179 unidades de volumen, 10 quedan fuera de uso por duplicado y una se reserva como par de reproducibilidad del mismo paciente." |
| T02 | alta | G-T4, OC-3 | capitulo3.tex:88 (y tab. 111, :191) | "La viabilidad del corredor se juzga con la convención de un diámetro de al menos 10 mm" | DEC:588-610 (#31); IMP:3844-3855 (#31 APLICADA); DEC:1483-1489 (D-O2.4) | El criterio vigente de viabilidad es `Dmax >= d_implante + 2c` (#31 APLICADA; tabla de D-O2.4 lo liga a la envolvente 6.5-8.0 mm); el 10 mm "queda como convencion heredada de comparacion". TM no se actualizo (IMP:3850 lo dice). Las fuentes discrepan y el texto copia la de menor autoridad; ademas se contradice con su propia Tabla `tab:geometrias`, que asigna la viabilidad a la envolvente de 6.5-8.0 mm. | Enunciar la viabilidad como `D >= d + 2c` (d = 6.5-8.0 mm, c = 1-2 mm radiales, operacionalizacion propia de la frase de Kaiser) y el 10 mm como convencion de comparacion, o `\GAPDEC{criterio de viabilidad: TM usa 10 mm, #31 aplicada usa d + 2c}`. Reportar a la autora para alinear TM. |
| T03 | alta | G-T4 | capitulo3.tex:57 | "Su regla se fijó por escrito antes de cualquier corrida." | DEC:814-845 (2026-09-15 (2)); DEC:1044-1071 (2026-09-17 (3)); TM:77 ("reproduced an earlier full-cohort run (330/330)") | La regla operativa (seis combinaciones, lectura, desempate, marginal) se fijo el 2026-09-17, **despues** de E6b, que ya habia corrido el VAE preentrenado con las tres configuraciones sobre los 178 volumenes (DEC:841). "Antes de cualquier corrida" es falso; lo cierto es "antes de correr P1, la prueba que decide". TM trae la misma frase, asi que las dos fuentes se contradicen. | "La regla se fijó por escrito antes de correr la prueba que decide la compuerta (P1); una exploración previa del autoencoder preentrenado (E6b) ya había fallado el criterio, y se declara." |
| T04 | media | G-T4 | capitulo3.tex:70 | "Si ninguna aprueba, la ruta latente se abandona y el veredicto negativo se reporta" | DEC:976-979 (2026-09-17 B.3); DEC:1136-1149 | La regla registrada decia "si ninguna pasa, **el Objetivo 3 no se ejecuta** y el No-Go se reporta como resultado". El rediseno al dominio de imagen es posterior (2026-09-19). El texto (y TM) reformula la regla preinscrita a la medida del desenlace, aunque :37 y :171 si declaran el rediseno como posterior. | Citar la consecuencia tal como se registro ("el Objetivo 3, en su forma latente, no se ejecuta") y dejar el rediseno en :37/:171 como decision posterior declarada. |
| T05 | media | G-T4 | capitulo3.tex:163 | `\GAPDATO{eje medido del segundo corredor (...) la corrida que lo mide no se ha lanzado}` | IMP:8422-8427 (#121, act. 2026-09-22 (7)); `experiments/objetivo2/outputs/e9ts_ejes_corredor.csv`, `e9ts_ejes_perfiles.csv` | GAP injustificado: la corrida se lanzo y se bajo; hay eje a la altura del pico inferior en 69 de 72 casos. Lo que falta es la preinscripcion de poses en ese corredor y la corrida de muestreo/SAP. (MAPA:38 arrastra el mismo error, "`e9ts_ejes.sbatch` sin lanzar".) | `\GAPDATO{preinscripción y corrida del muestreo de poses en el segundo corredor; su eje ya está medido en 69 de 72 casos}`. Corregir la fila de MAPA. |
| T06 | media | OC-3 | capitulo3.tex:96 | "Existe además una segunda lectura del nivel S1" | IMP:8639-8691 (#124 ABIERTA) | #124 esta ABIERTA precisamente sobre si esa lectura se declara y con que limites. La frase fuera de la marca ya la afirma como hecho; la marca solo cubre el detalle. | Dejar solo la marca: `\GAPDEC{si se declara una segunda lectura del nivel S1 hecha por la autora sobre láminas (61 de 61), y con qué límites}`, sin la frase previa. |
| T07 | media | G-T4 | capitulo3.tex:47 | "Con esa regla, los 178 volúmenes corresponden a 168 pacientes." | DAT:117-122; DEC:508-535 | De los 10 grupos, 6 salen por SHA256 y 3 por cortes compartidos **confirmados por la autora**; el par `metal_0065`/`0066` se agrupo **por observacion visual**, no por huella. "Con esa regla" atribuye el recuento entero a las dos huellas. | "Las huellas de volumen y de corte, más una observación visual (un par de adquisiciones del mismo implante), agrupan los 178 volúmenes en 168 pacientes." |
| T08 | media | E-R6 | capitulo3.tex:257 | "Lin et al. describen esa tarea como un problema mal planteado porque hay información destruida" | `lin2019`, Evidencia fila "MAR perfecta es mal planteada" (Sec. 2, p. 10506) | La ficha da la razon del autor: "ill-posed problem since both terms contribute to the region of metal trace". "Porque hay informacion destruida" es la lectura del lector (ficha:351-356), no del paper. La cita afirma mas que la ficha. | "Lin et al. describen esa tarea como un problema mal planteado, porque en la traza del metal se superponen la contribución del metal y la del tejido; la síntesis no tiene que recuperar esa información." |
| T09 | media | E-R6 | capitulo3.tex:173 | "Dilatarla deja el error casi igual, con 11.45 y 11.63 HU" | `karageorgos2024ddpm`, Tabla III (p. 16): 7.57 / 11.45 / 11.63 / 54.82 / 57.69 | Frente a la mascara verdadera (7.57 HU) la dilatacion sube el RMSE ~50 %; "casi igual" solo vale entre los dos factores de dilatacion. La redaccion sugiere que dilatar no cuesta nada. | "Dilatarla lo sube moderadamente, a 11.45 y 11.63 HU para factores de 1.4 y 1.8; contraerla lo multiplica por siete, a 54.82 y 57.69 HU." |
| T10 | media | E-R6 | capitulo3.tex:88 | "Kaiser et al., de quienes proviene, lo describen como un valor conservador elegido" | `kaiser2014dysmorphism` filas "10 mm heredado de refs. 4, 29, 37" y "Atribucion explicita del 10 mm a terceros" (p. e120(7)); `mclaren2021corridor` fila "Kaiser et al. recommended 10 mm" | Kaiser no es el origen: lo atribuye a trabajos previos ("previously established ... by experienced surgeons"). Solo McLaren lo toma de Kaiser. DEC 2026-09-08 (2) declara la cadena agotada. | "Kaiser et al., de quienes lo toman McLaren et al., lo describen como un valor conservador elegido y lo atribuyen a trabajos previos (...)". |
| T11 | media | G-T4 | capitulo3.tex:165 | "su efecto reportado sobre el tamaño de la zona segura no es consistente entre estudios" | DEC:319-335 (2026-09-08 (2)); `gardner2010safezones` (cita a Carlson 2000: "no difference in the safe zone size") | Afirmacion sobre la literatura sin `\cite`; la fuente esta en el repositorio. | Citar `\cite{gardner2010safezones,kaiser2014dysmorphism}` con la frase que lo sostiene (Gardner et al. recogen un estudio sin diferencia; Kaiser y Gardner clasifican el dismorfismo con criterios distintos). |
| T12 | media | G-T4 | capitulo3.tex:255 | "el ancho de 2 mm procede de la literatura de tornillos pediculares" | TM:52 (`gertzbein1990`, `mirza2003`); `zwingmann2009navigated` fila "Origen de la escala" (p. 1835); `smith2006iliosacral` fila "Origen de la escala de perforacion" (p. 236) | Afirmacion de procedencia sin cita; las cuatro claves existen en `referencias.bib`. | Anadir `\cite{smith2006iliosacral,gertzbein1990,mirza2003}` o "Smith et al. y Zwingmann et al. declaran tomarla de la clasificación de tornillos pediculares". |
| T13 | media | G-T4 | capitulo3.tex:221 | "es la referencia fiel al mecanismo y el competidor más fuerte disponible" | TM:56, :119; `docs/00-tesis.md`; DEC | "Referencia fiel al mecanismo" sale de TM:56. "El competidor mas fuerte disponible" no aparece en ninguna fuente del repositorio; es una valoracion sin respaldo. | Quitar "y el competidor más fuerte disponible", o marcarlo `\GAPDEC`. |
| T14 | media | G-T4 | capitulo3.tex:118, :165 | "La cabeza, cuando se modela" / "La densidad ósea entra como componente reportado" | TM:78 ("constrained by bone density"), TM:117 ("The head is modelled"); DEC D3 (:1241-1250), D-O2.6 (:1502-1506) | El texto sigue DEC (correcto por autoridad), pero TM dice otra cosa en ambos casos y la discrepancia no queda visible para la autora en el documento. El redactor la reporto (respuesta r00 §4.1-4.2). No es error del texto; es discrepancia de fuentes abierta. | Mantener la redaccion y pedir a la autora que alinee TM (no lo hace el ciclo). Si la autora prefiere, `\GAPDEC` en :165. |
| T15 | baja | G-T4 | capitulo3.tex:90 | `\GAPDATO{revisión (...) de los 16 casos en que los dos recortes difieren}` | `e9ts_revision_laminas_autora.csv` (16 filas, veredicto vacio); IMP:8583-8588 | GAP justificado (0 de 16), pero 14 casos difieren por `|D6 - D3| >= 1 mm` y 2 (`CLINIC_0022`, `CLINIC_0043`) tienen el mismo D con caja desplazada tras la limpieza. | "(...) de los 16 casos marcados por diferencia entre recortes o por desplazamiento de caja (...)". |
| T16 | baja | G-T4 | capitulo3.tex:86 | `\GAPDATO{descripción del algoritmo de búsqueda del eje del corredor, que hoy solo consta en el código}` | IMP:8315-8318 (#121, CERRADA): "recorre zs = S1 - 3..75 mm en pasos de 3 mm" | Falta una descripcion completa, pero no "solo consta en el codigo": #121 documenta el barrido por alturas. | "(...) que hoy solo consta en el código y, en parte, en la implicancia #121". |
| T17 | baja | G-T4 | capitulo3.tex:118 | "El cuerpo de 4.91 mm es la mediana medida en la cohorte local" | DEC:1243-1245 (D3: 79 componentes esbeltos en 43 casos, 178 volumenes) | Falta el n. | "(...) mediana sobre 79 componentes en 43 casos (...)". |
| T18 | baja | G-T4 | capitulo3.tex:70 | "Ese orden es arcoseno hiperbólico, luego el techo de 20 000 HU y por último las ventanas publicadas" | DEC:1056-1057; TM:77 | Omite la segunda regla del desempate preinscrito: dentro de una codificacion, el decodificador preentrenado va antes que el adaptado. | Anadir "; dentro de cada codificación, el decodificador preentrenado precede al adaptado". |
| T19 | baja | E-R6 | capitulo3.tex:259 | "un desplazamiento craneal de 5 a 20 mm de una fractura sacra de zona II" | `reilly2003effect` (resumen: osteotomia transforaminal zona II en 6 pelvis cadavericas) | La fractura es una osteotomia simulada; TM dice "osteotomised". | "(...) de una fractura sacra de zona II creada por osteotomía (...)". |
| T20 | baja | E-F3 | capitulo3.tex:118 | "el estudio de elementos finitos de Zhu et al." | `referencias.bib`:1222-1223 (Zhu, Zongdong and Liao, Feng) | Entrada de dos autores: "et al." no corresponde. | "Zhu y Liao \cite{zhu2022optimalposition}". |
| T21 | baja | G-T4 | capitulo3.tex:261 | "se reporta sin prueba inferencial, como fija la preinscripción" | PRE §5-§6 | PRE fija la distancia "tal como se mide" y dice que no es prueba de equivalencia; no fija explicitamente la ausencia de prueba inferencial. | "(...) sin prueba inferencial, porque la preinscripción no prevé ninguna". |
| T22 | baja | E-R6 | capitulo3.tex:211 | "la serie clínica tampoco excluyó a sus pacientes de corredor estrecho" | `zwingmann2009navigated` (criterio de inclusion: Tile B y C, p. 1834); IMP #122 | Es una ausencia: la ficha solo registra la inclusion Tile B/C; no hay frase sobre exclusion por anatomia. | "(...) y la serie clínica no reporta haber excluido pacientes por corredor estrecho". |
| T23 | baja | G-T4 | capitulo3.tex:43 | "La publicación del conjunto no reporta los parámetros de adquisición ni de reconstrucción" | `liu2021ctpelvic1k` fila "Marca/modelo de escaner y kVp/mAs: NO ENCONTRADO EN EL PDF (remitido a Online Resource 1)" | La ficha remite al suplemento, no leido. "No reporta" puede ser falso para el material suplementario. Ficha insuficiente. | "El artículo del conjunto no reporta (...)"; si se quiere afirmar sobre el suplemento, relectura con `lector-papers`. |
| T24 | baja | G-T4 | capitulo3.tex:78 | "Las series clínicas muestran distribuciones de malposición que dependen de la técnica quirúrgica" | `zwingmann2009navigated` filas de resultados (p. 1836-1837) | La cita al final de la frase siguiente es `ziran2007fluoroscopic`; esta afirmacion queda sin cita. | Anadir `\cite{zwingmann2009navigated}`. |
| T25 | baja | G-T4 | capitulo3.tex:152 | "Fija; la corrida no se repite" | PRE §3.1 ("fija; la corrida no se re-tira") | PRE dice que las poses no se vuelven a sortear; "no se repite" sugiere que la corrida no es reproducible. | "Fija; las poses no se vuelven a sortear". |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :8 | Dos componentes separados + compuerta previa | TM:74-80; CLAUDE.md raiz | si |
| :12 | Obj 1 valida HU del hueso con tolerancia fijada | TM:77 | si |
| :12 | SAP, unica metrica introducida | TM:68, :80; DEC 2026-09-08 | si |
| :12 | Obj 4 adopta protocolo publicado con nombres originales | TM:80 | si |
| :14 | M, B_delta, G = M u B_delta; copia fuera de G | TM:79 | si |
| Fig. pipeline | TotalSegmentator; marco Kaiser; SAP vs dos distribuciones; inpainting en imagen; comparacion copia-pega y protocolo fisico; compuerta descarto ruta latente | TM:77-79, :98; DEC 2026-09-19 | si |
| :35 | Dice/HD95 fuera de alcance por dos condiciones auditables | TM:83, :127 | si |
| :35 | Ablaciones diferidas | TM:83; DEC 2026-09-17 B.1 | si |
| :37 | Compuerta ejecutada, veredicto negativo | TM:77, :100 | si |
| :37 | Obj 2 ejecutado sobre cohorte completa | TM:96, :109; EXP:85-86 | si |
| :37 | Obj 3 con formulacion y conjunto definidos | DEC 2026-09-21 (R1-R3) | si |
| :37 | GAPDATO sin muestra sintetica | IMP #116 (ABIERTA; act. 2026-09-24, :8751-8753) | si |
| :37 | Rediseno posterior; regla fijada antes y no modificada | DEC 2026-09-19 pto 2; TM:77 | si |
| :41 | 1 184 volumenes | `liu2021ctpelvic1k` fila "1184 volumenes CT totales" (p. 2) | si |
| :41 | 178 locales; dataset6 103, dataset7 75 | DAT:27-30, :55 | si |
| :41 | Correspondencia inferida por conteo, espaciado, dimensiones | DAT:60-63 | si |
| :43 | Publicacion no reporta adquisicion/reconstruccion | `liu2021ctpelvic1k` fila escaner NO ENCONTRADO (remitido a suplemento); DEC 2026-09-17 C (#73) | T23 |
| :43 | MAR del fabricante y monoE cambian apariencia | `selles2024marreview` filas monoE (Sec. 3.3, pp. 3-4) y "varies by vendor" (Sec. 3.5, p. 6) | si |
| :45 | Cribado >2500 HU, un voxel, sin filtro de tamano, heuristica, no Peters | DAT:67-69; DEC 2026-09-11 (3) | si |
| :45 | Autora reviso en 3D los 178 y anoto tipo y cantidad | DAT:104-105 | si |
| :45 | GAPDATO revision multiplanar | DAT:139 ("3D completa, falta el recorrido de cortes") | si (justificado) |
| :47 | Unidad de independencia = paciente | DEC 2026-09-10 | si |
| :47 | Huella de volumen y de corte | DEC:524-530 | parcial (T07) |
| :47 | 178 volumenes = 168 pacientes | DAT:120; DEC:533 | si (T07 sobre el metodo) |
| :47 | Grupos 65 / 37 / 66 | DAT:137 | si |
| :47 | Ejemplos de objetos no ortopedicos | DAT:112-114 | si |
| :47 | 10 excluidos y 1 de reproducibilidad | DAT:136-137 (son unidades) | no (T01) |
| :49 | Aislamiento estricto | TM:115 | si |
| :49 | Particion Obj 1 por paciente, estratificada, 34 de prueba | TM:77; DEC 2026-09-17 (3) | si |
| :49 | Obj 3 reutiliza particion; pares de train con metal | DEC 2026-09-21, 2026-09-21 (2); TM:79 | si |
| :49 | Obj 2 sin particion; grupos 2 y 3 | DEC 2026-09-14 (2) (#52 a) | si |
| :51 | 103 -> 91 -> 72 | TM:123; DEC 2026-09-14 (3) | si |
| :51 | 11 de 34; 7 de 57; 1 por borde de FOV | TM:123; DEC:747-749 | si |
| :51 | 49 de sensibilidad (grupo 3) | PRE §1; DEC D-O2.2 | si |
| :51 | Seleccion por ausencia de osteosintesis, no de fractura | TM:109; IMP #125 | si |
| :51 | GAPDATO cribado de fractura 30 (15+15) | `r3_fractura_revisor.csv` (30 filas, columnas vacias); IMP:8729-8731 | si (justificado) |
| :53 | Cuatro funciones de los 65 con metal; control de prueba y reprueba | TM:117; DEC 2026-09-11 | si |
| :53 | Tornillos por umbral fragmentados, fuste bajo calibre, cambian entre adquisiciones | TM:117; DEC:1210 (E8, #46) | si |
| :57 | Compuerta obligatoria Go/No-Go previa al Obj 3 | TM:77; DEC 2026-09-17 B.3 | si |
| :57 | Regla fijada antes de cualquier corrida | DEC 2026-09-15 (2), 2026-09-17 (3) | no (T03) |
| :59 | Tres canales con ventanas distintas; VAE; lectura sin imagen original; canal mas estrecho no saturado | TM:77; DEC:1050 | si |
| :59 | 150 HU del protocolo adoptado | `peters2025hybrid` fila "Umbral de hueso 150 HU" (2.5, p. 5); `haneda2025aapm` fila "Umbral de hueso" (Sec. 2.3, p. 7) | si |
| :61 (Ec. MAE) | MAE por paciente en hueso | DEC:1051 | si |
| :66 | Sin umbral publicado de aprobacion | DEC 2026-09-15 (2); TM:77 | si |
| :66 | RMSE 20.2 HU (algoritmo que ancla la escala de Peters) | `karageorgos2024ddpm` fila NMAR (Tabla I, p. 28); `peters2025hybrid` fila "NMAR calibrado a score 2" (2.5, p. 5) | si |
| :66 | 12.3 HU, difusion en sinograma evaluada en imagen | `karageorgos2024ddpm` fila DDPM (Tabla I, p. 28) y "DDPM in the sinogram domain" (Sec. I, p. 3) | si |
| :66 | 12.74 HU, difusion latente | `yun2026simulationdriven` fila MLD-MAR (Tabla 1, p. 10) | si |
| :66 | RMSE >= MAE; orden de magnitud declarado | DEC 2026-09-15 (2); TM:77 | si |
| :68 | 2 variantes x 3 codificaciones = 6 | DEC:1048-1049 | si |
| :68 | Ventanas [-1000,2000], [-320,480], [-160,240] | `wang2025adaptiveweighting` filas LW/MW/SW (Sec. V-A-1, p. 2412) | si |
| :68 | Techo 20 000 HU; arcsinh sobre [-1000, 20 000] | TM:77 | si |
| :70 | Media sobre 34 < 25 HU; Go si alguna de seis | DEC:1051-1052; TM:77 | si |
| :70 | Multiplicidad sin corregir; IC 95 % bootstrap; marginal | DEC:1054-1055 | si |
| :70 | Orden a priori; techo de 2000 recorta metal | DEC:1056-1057, :1065 | parcial (T18) |
| :70 | Si ninguna aprueba, se abandona ruta latente | DEC 2026-09-17 B.3 | no (T04) |
| :72 | Error en B_delta descriptivo, fuera de la regla | DEC 2026-09-16 pto 2; TM:77 | si |
| :72 | Rombach: primera etapa elimina alta frecuencia | `rombach2022latentdiffusion` fila "La compresion perceptual quita alta frecuencia" (§1, p. 2) | si |
| :74 | Extension a MAISI, misma regla y pacientes | DEC 2026-09-19 pto 3; TM:77 | si |
| :74 | Expansion "Medical AI for Synthetic Imaging" | `guo2025maisi` titulo de ficha | si |
| :74 | Cota inferior por recorte; no se corre si supera | TM:77 | si |
| :78 | Muestreador perturba, no optimiza | PRE §2; TM:107 | si |
| :78 | Distribuciones dependientes de tecnica | `zwingmann2009navigated` (Results, pp. 1836-1837) | si, sin cita (T24) |
| :78 | Orientacion de superficies varia entre individuos | `ziran2007fluoroscopic` fila coeficientes de variacion; TM:52 | si |
| :82 | Marco de Kaiser: reformateo, angulos coronal/axial, 5 mm | `kaiser2014dysmorphism` filas reformateo (Fig. 1, p. e120(3)), crestas/espinas (p. e120(2)), "5 mm of distance to the cortex" (p. e120(2)) | si |
| :84 | Mediana 0.42 de voxeles <= 150 HU | TM:123 | si |
| :84 | TotalSegmentator 2.18.0, tarea total, recorte por defecto, alternativo como sensibilidad | TM:78; DEC 2026-09-14, 2026-09-14 (4) | si |
| :84 | Construido sobre nnU-Net | `wasserthal2023` fila 1a (p. 2) | si |
| :84 | Limpieza < 0.1 % | TM:78; DEC 2026-09-14 (3), (5) | si |
| :84 | 104 estructuras; sin exactitud para S1 | `wasserthal2023` filas 2d, 3e (NO ENCONTRADO) | si |
| :86 | Envolvente: sacro, S1, coxales; cierre 2 mm; relleno | DEC D-O2.3 (:1450-1452) | si |
| :86 | Diametro = 2 x distancia libre minima, sin extremos | DEC:1468-1469 | si |
| :86 | GAPDATO algoritmo de busqueda | IMP:8315-8318 (descripcion parcial) | parcial (T16) |
| :86 | Semimaximo por objeto; 2500 HU cota superior; contraste aparte | DEC 2026-09-14 (2), (3); TM:123 | si |
| :88 | Viabilidad = diametro >= 10 mm | DEC #31 (2026-09-11 (2)); IMP #31 APLICADA; D-O2.4 | no (T02) |
| :88 | McLaren: procedimiento reproducible, no validado como umbral | `mclaren2021corridor` filas "El umbral es heredado" (p. 2) y "Regla de expansion" (p. 2) | si |
| :88 | Kaiser: conservador, 1-2 mm alrededor de 6.3-8 mm | `kaiser2014dysmorphism` filas "Justificacion dimensional" y "umbral propio y conservador" (p. e120(7)) | si |
| :88 | Kaiser como origen del 10 mm | `kaiser2014dysmorphism` fila "10 mm heredado de refs. 4, 29, 37" | no (T10) |
| :90 | Mediana 9.5 mm (RIC 7.4-11.7) | TM:123 | si |
| :90 | 29 de 72 (defecto) y 27 (alternativo) | TM:123; DEC:770-771 | si |
| :90 | Limpieza sin efecto hasta 5 %; fijada post hoc | TM:123; DEC 2026-09-14 (3) | si |
| :90 | GAPDATO 16 casos | `e9ts_revision_laminas_autora.csv` (vacio); IMP #123 ABIERTA | si (T15 precision) |
| :94 | Referencias en la union lumbosacra donde se concentran rayas; sin fuente publicada | TM:121 | si |
| :94 | Contaminacion > maximo de 69 sin metal | TM:121 | si |
| :94 | Revisor clinico (cirujano, ORL), ciego, confirmo S1 | TM:121; IMP:8677-8679 | si |
| :96 | 65 / 57 / 48 / 29 | TM:121 | si |
| :96 | 7 por truncamiento; 17 con tornillo; S1 correcto en todos; 3 contaminados | TM:121 | si |
| :96 | "Existe además una segunda lectura" + GAPDEC 61 de 61 | IMP #124 ABIERTA | no (T06) |
| :96 | Localizacion de crestas y espinas sin revision clinica | TM:121; DEC 2026-09-17 E | si |
| :100 | Tornillos rigidos parametricos; tres geometrias | TM:117; DEC D-O2.4 | si |
| :100 | Cifra nominal = rosca; cilindro 6.5-8.0 sobreestima mas del doble | TM:117; DEC 2026-09-20 (alternativas) | si |
| Tab. geom. | 6.5-8.0 mm | `gardner2010safezones` fila "Diametro de tornillo asumido" (M&M, p. 624) | si |
| Tab. geom. | 6.3-8 mm | `kaiser2014dysmorphism` fila "Justificacion dimensional" (p. e120(7)) | si |
| Tab. geom. | 4.91 mm, mediana medida | DEC D3 (:1245); EXP:62 | si |
| Tab. geom. | Fuste 4.8 mm | `synthes2003guide` (ficha `synthes_cannulated_65_73_guide.md`) fila "Fuste 4.8 mm" (impresa 2) | si |
| Tab. geom. | 4.9 fuste, 4.7 nucleo | `gardner2015screw` filas Tabla 1 (p. 42) | si |
| Tab. geom. | 7.0 mm canulados | `zwingmann2009navigated` fila "Tornillo usado" (M&M, p. 1835) | si |
| Tab. geom. | 4.91 y 7.3 como sensibilidad | DEC:1481; PRE §4 | si |
| :118 | Filtro geometrico, no clinico | DEC:1252-1254 | si (T17 falta n) |
| :118 | Nucleo = fuste en la guia | `synthes2003guide` fila "Nucleo y fuste iguales" (impresa 5) | si |
| :118 | Zhu: 7.3 solo en rosca distal, 4.8 en fuste | `zhu2022optimalposition` filas fuste/rosca (2.3, p. 1548) | si (T20 E-F3) |
| :118 | Cabeza 8.0 x 4.5 mm sin avellanado; unica medicion | `sayres2014comparison` filas cabeza/altura (Discusion, p. 34); TM:117 | si |
| :118 | Cabeza y rosca como sensibilidad | DEC D3 (:1249-1250) | si (T14: TM discrepa) |
| :120 | Calibre fijado por la referencia; perforacion escala con radio | DEC D-O2.4; TM:117 | si |
| :120 | Longitud acotada por el corredor con regla de Kaiser | DEC 2026-09-11; TM:117 | si |
| :122 | Arandela 1.5 mm, otro fabricante | `doublemedical2021trauma` (ficha `doublemedical_trauma_catalogue.md`) fila Washer 6.5/7.3 (5/7); DEC 2026-09-20 pto 1 | si |
| :122 | Canulacion libre; valor circulante solo como instrumental | DEC 2026-09-20 pto 2; TM:117 | si |
| :122 | 316L y Ti-6Al-7Nb | `synthes2003guide` fila "Material del tornillo" (impresa 12) | si |
| :122 | Fabricantes identificados como no revisados por pares | Bitacora §2; P-EA1 | si |
| :126 | Congelado el 22 sept 2026, antes de cualquier distancia | PRE encabezado; DEC D-O2.7 | si |
| :126 | Sin desviaciones a la fecha | PRE §9 | si |
| :128 | Anclaje al punto medio; longitud del implante del tramo; motivo | PRE §2.1 | si |
| :130-135 (Ec. pose) | Perturbacion isotropa, seminormal truncada 3 sigma, eje de giro uniforme | PRE §3 | si |
| Tab. preinsc. | h = 5.0 mm; h = 2 sigma; sigma_t = 2.5; sigma_a por caso; 2.07 grados; L = 138 mm; 3 sigma; 50 poses; semilla 20260922 | PRE §3.1 | si (T25 redaccion) |
| :157 | Una constante independiente | PRE §3.1; TM:107 | si |
| :157 | 4 grados no usados; citados de tercera fuente | PRE §3.1; `zwingmann2009navigated` fila "Umbral angular de dano" (Introduction, p. 1834) | si |
| :157 | Isotropia por falta de dato de direccionalidad | PRE §3.2 | si |
| :159 | Semilla por caso; sensibilidad subconjunto de la primaria | PRE §3.1, §8 | si |
| :161 | Tres puntos de falsabilidad | TM:107; DEC D-O2.3 | si |
| :163 | 18 volumenes; 13 / 4 / 1; 39, 36 y 33 mm | TM:78; IMP:8439-8451 | si |
| :163 | Sin distribucion ordinal para niveles bajo S1; preinscripcion solo S1 | TM:78; PRE §7 | si |
| :163 | GAPDATO eje del segundo corredor | IMP:8422-8427; `outputs/e9ts_ejes_*.csv` | no (T05) |
| :165 | Densidad como componente reportado, no condicionante | DEC D-O2.6 | si (T14: TM discrepa) |
| :165 | Arand: heterogeneidad, valores de gris bajos en el ala | `arand2019pelvicring` filas modelo de gris (Abstract, p. 376); DEC 2026-09-16 pto 1 | si |
| :165 | GAPDEC fraccion por zona de densidad | DEC D-O2.6 (depende de `e9b_densidad_s1.csv`, retirada por DEC 2026-09-14 #50) | si (justificado) |
| :165 | Fenotipos no consistentes entre estudios | DEC 2026-09-08 (2); `gardner2010safezones` | si, sin cita (T11) |
| :169 | Inpainting 2.5D en imagen; entradas; copia fuera de G; multiventana sin compresion | TM:79 | si |
| :171 | Formulacion inicial SD 1.5 + ControlNet; ControlNet presupone base congelada y latente | `zhang2023controlnet` filas "Justificacion del congelamiento" (§3.1, p. 4) y "Espacio latente como dominio" (§3.2, p. 5) | si |
| :171 | Sin base de TC preentrenada en pixeles; rediseno posterior declarado | TM:79; DEC 2026-09-19 | si |
| :173 | B_delta ~12 mm; parametro de diseno; trunca rayas lejanas | TM:79; DEC 2026-09-17 C (#57) | si |
| :173 | 7.57; 11.45 y 11.63 (1.4, 1.8); 54.82 y 57.69 (0.7, 0.5) | `karageorgos2024ddpm` filas Apendice Tabla III (p. 16) | si (T09 interpretacion) |
| :175 | Experimento en sinograma, no banda en imagen; 12 mm construccion declarada | TM:79 | si |
| :177 | Pares de train con metal; mascara 2500 HU; semimaximo sensibilidad | DEC D1 (:1205-1208) | si |
| :177 | Unidad = componente conexo | DEC D2 (:1214-1226) | si |
| :179 | Criterio R1-R3 fijado antes; tamano y forma se reportan | DEC 2026-09-21 (R1-R4) | si |
| :181 | Tres desplazamientos de dominio; primero y tercero cuantificados | TM:79; DEC:1331-1334 | si |
| :183 | GAPDEC congelar diseno del sintetizador | DEC:1288 (se congela al medir Delta) | si (justificado) |
| :191 | Tres componentes de SAP | TM:96 | si |
| :191 | Escala de cuatro grados de Smith en fijacion iliosacra | `smith2006iliosacral` filas grados 0-3 (Screw Position, p. 236) | si |
| :193 (Ec. brecha) | max(0, r + s(c + t u)) | PRE §4 | si |
| :196 | Limites 0, (0,2), [2,4], (4, inf) por convencion | PRE §4; DEC 2026-09-16 pto 4 | si |
| :198 | Tramo = implante, longitud del corredor, recorte 8 mm; razon | PRE §4; DEC D-O2.3 pto 4 | si |
| :198 | Poses sin hueso = grado 3; denominador como las series | PRE §4; TM:96; IMP #120 | si |
| :200 | Envolvente aproxima cortical externa | DEC:1462-1465; TM:96 | si |
| :200 | Seis controles antes de la corrida; resolucion 0.083 mm | EXP:83; PRE §4, §8 | si |
| :200 | Smith suma escala angular; GAPDEC | `smith2006iliosacral` filas grado angular (p. 236); IMP #11 ABIERTA | si (justificado) |
| :202 | Dos distribuciones de Zwingmann, por tecnica, solo S1 | DEC D-O2.1, D-O2.5; PRE §5 | si |
| :202 | 69/15/8/8 y 40/37/11.5/11.5 | `zwingmann2009navigated` filas "Resultado navegado/convencional" (Results, pp. 1836-1837) | si |
| :202-207 (Ec. W1) | Grados equiespaciados por convencion; unidad = grado | PRE §5 | si |
| :209 | Reporte tal cual; distancia grande reportable; no es equivalencia | PRE §6; DEC D-O2.1 | si |
| :209 | 26 tornillos / 24 pacientes; 35 / 32 | `zwingmann2009navigated` filas "Muestra navegada/convencional" (Abstract, p. 1833) | si |
| :209 | S1 explicito en convencional, asumido en navegado; grados por tornillo | `zwingmann2009navigated` verificacion 2026-09-16 filas 6; DEC 2026-09-17 C (#69) | si |
| :211 | Estratificacion post hoc por calibre 7.0 mm; grado 0 inalcanzable | IMP #122 CERRADA; TM:109 | si |
| :211 | Restringir cohorte considerado y rechazado | IMP:8529-8533; TM:109 | si |
| :211 | Serie clinica no excluyo corredores estrechos | IMP:8516-8517 (inferencia); ficha sin frase | parcial (T22) |
| :215 | Bone integrity: >150 HU fuera del metal; volumen y SDC | `peters2025hybrid` filas Metrica 6 (2.5, pp. 5-6) | si |
| :215 | Metal integrity analoga, umbral adaptativo por ROI | `peters2025hybrid` filas Metrica 7 y umbral (2.5, p. 6) | si |
| :215 | Streak amplitude: ROIs perpendiculares, 5 % alto y bajo | `peters2025hybrid` filas Metrica 4 (2.5, p. 5) | si |
| :217 | Metricas disenadas para MAR; GAPDEC inversion | IMP #16, #17 ABIERTAS | si (justificado) |
| :217 | Escala 0-4 no se traslada; ancla sin analogo | `peters2025hybrid` ficha:368; TM:98 | si |
| :217 | Realismo contra observaciones reales | TM:127 | si |
| :219 | Streak amplitude unico primario, declarado antes | DEC D4 pto 1; TM:98 | si |
| :221 | Tres brazos, misma anatomia y poses | TM:119 | si |
| :221 | GAPDEC copia-pega | `experiments/objetivo3/diseno_A.md` §7 (borrador, segun respuesta r00) | si (justificado) |
| :221 | CatSim en XCIST; asociado a AAPM CT-MAR | TM:50, :119 | si |
| :221 | "competidor mas fuerte disponible" | sin fuente | no (T13) |
| :221 | Adoptado en lugar de reimplementacion validada | TM:119; CLAUDE.md raiz | si |
| :223 | Protocolo 2D y para MAR; adaptacion no hereda validacion | `peters2025hybrid` filas "Todo en 2D" (Abstract, p. 1); IMP #17 | si |
| :223 | Validan contra fantoma; no cubren paso hibrido ni geometria generica; proyeccion conjunta no dicha | `peters2025hybrid` filas 4a, 4b, 1d (pp. 2-3); DEC 2026-09-17 C (#70) | si |
| :223 | Subconjunto reducido; control sin metal; documentacion de reproduccion | TM:119; DEC 2026-09-17 B.2 | si |
| :223 | GAPDATO brazo fisico | IMP #17 ABIERTA | si (justificado) |
| :225 | Wilcoxon pareado una cola, alfa 0.05, efecto e IC | DEC D4 pto 2 | si |
| :225 | TOST; IC 90 % dentro de [-Delta, +Delta]; nunca desde no significativo | DEC D4 pto 3; TM:98 | si |
| :225 | Delta = variabilidad propia en validacion | DEC D4 pto 4; DEC 2026-09-21 (2) | si |
| :225 | GAPDEC brazo TOST | IMP #90 (act. 2026-09-21, contingencia) | si (justificado) |
| :227 | RMSE y SSIM fuera de B_delta; exacta por construccion en el sintetizador | TM:79, :102, :119 | si |
| Tab. diseno | Filas Obj 1-3 | TM:77, :96-98; DEC D4 | si |
| :253 | Circularidad controlada por preinscripcion | DEC D-O2.1; PRE | si |
| :253 | Tres decisiones post hoc | DEC 2026-09-14 (3); IMP #122 | si |
| :253 | Control de nivel excluyo mas con objetos no ortopedicos | DEC:748 | si |
| :253 | Fractura no verificada | IMP #125 ABIERTA; TM:109 | si |
| :255 | Protrusion, no cortical; 0.083 mm | DEC D-O2.3; PRE §4 | si |
| :255 | 2 mm de la literatura pedicular | TM:52; fichas Zwingmann/Smith | si, sin cita (T12) |
| :255 | Serie no define 2 o 4 mm exactos ni grosor de corte | `zwingmann2009navigated` verificacion 2026-09-16 filas 4 (NO ENCONTRADO); DEC 2026-09-16 pto 3 | si |
| :255 | Tejwani 2.5 vs 5.0 mm, P = 0.3 | `tejwani2014` fila "Grosor de corte" (M&M, p. 514) y ficha pto 7 (P = .3) | si |
| :257 | Grados equiespaciados convencion; metricas de Peters para reducir; mascara no codifica aleacion | PRE §5; TM:117 | si |
| :257 | Lin y Li: penalizacion por solo imagen, en remocion | `lin2019` filas IE-Net vs G (Tabla 1, p. 10509); `li2024` fila "Insuficiencia de un solo dominio" (Sec. I, p. 1866) | si |
| :257 | Lin: mal planteado "porque hay informacion destruida" | `lin2019` fila "MAR perfecta es mal planteada" (Sec. 2, p. 10506) | no (T08) |
| :259 | Pelvis fracturadas Tile B y C | `zwingmann2009navigated` fila "Criterio de inclusion" (M&M, p. 1834) | si |
| :259 | Reilly: 6 pelvis, 5-20 mm, zona II, 36-90 % en S1 | `reilly2003effect` filas desplazamientos (p. 89) y reduccion de area (Results, p. 91) | si (T19) |
| :259 | Cohorte local parcial, reconstruccion desconocida, TS sin exactitud para S1, protocolo 2D | DAT:55-58; TM:115; `wasserthal2023` fila 3e | si |
| :261 | Series pequenas; cuentan tornillos | `zwingmann2009navigated` filas muestra; ficha fila 6 | si |
| :261 | W1 sin prueba inferencial "como fija la preinscripcion" | PRE §5-§6 | parcial (T21) |
| :261 | GAPDEC intervalo por remuestreo | ninguna fuente lo decide | si (justificado) |
| :261 | Multiplicidad solo favorece el aprobado | DEC:1053-1055 | si |
| :261 | Delta sobre pocos pacientes de validacion | DEC 2026-09-21 (2) (3 pacientes) | si |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente/ControlNet vigente, "31-60%", BFC/ISC) | CLAUDE.md raiz; `docs/00-tesis.md` | ausente; solo aparece como excluido o sustituido |
| global | 30 claves `\cite` existen en `overleaf/referencias.bib` | `overleaf/referencias.bib` | si |
| global | Apellidos nombrados = primer autor del .bib (Karageorgos, Yun, Wang, Rombach, Kaiser, McLaren, Zwingmann, Smith, Peters, Tejwani, Reilly, Lin, Li, Selles, Arand) | `overleaf/referencias.bib` | si (Zhu: T20) |
| global | Ninguna cita como sujeto gramatical sola (E-F3) | revision de las 30 llamadas | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Se copia la formulacion de `tesis/main.tex` cuando una decision o implicancia APLICADA posterior la sustituyo y TM no se actualizo | G-T4, OC-3 | "La viabilidad del corredor se juzga con la convención de (...) 10 mm" | nuevo |
| Se confunden unidades de recuento (volumenes, unidades, componentes) con pacientes | G-T4 | "Otros 10 pacientes quedan excluidos y uno se reserva" | nuevo |
| El GAP se redacta sobre el estado inicial de una implicancia y omite sus actualizaciones posteriores | G-T4 | "la corrida que lo mide no se ha lanzado" | nuevo |
| Se atribuye al paper la lectura interpretativa del lector o de TM, no la frase de la ficha | E-R6 | "Lin et al. describen (...) mal planteado porque hay información destruida" | nuevo |
| Afirmacion sobre la literatura sin `\cite` aunque la fuente esta en el repositorio | G-T4 | "su efecto reportado (...) no es consistente entre estudios" | nuevo |
| Afirmaciones de integridad del preregistro mas fuertes que el registro ("antes de cualquier corrida") | G-T4 | "Su regla se fijó por escrito antes de cualquier corrida." | nuevo |
