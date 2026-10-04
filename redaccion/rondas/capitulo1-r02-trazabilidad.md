# Auditoria de trazabilidad — capitulo1 — r02

Archivo: `overleaf/secciones/capitulo1.tex` (125 lineas). Lint r02: PASA (0/0/0; GAP lit 4 / dato 1 / dec 7).
Respuesta previa: `capitulo1-r01-respuesta.md` (35 aplicados, 0 rechazados, 2 escalados). No hay RECHAZADOS que respetar.
Las 15 correcciones de trazabilidad de r01 (T01-T15) se verificaron en el texto: todas aplicadas y con fuente.
Claves: todas existen en `overleaf/referencias.bib`; el apellido nombrado coincide con el primer autor (incluida `ronnenberger2015unet`, cuyo primer autor en el `.bib` es Ronneberger; la clave mal escrita no afecta al PDF). Ninguna cita es sujeto gramatical sola.
Ninguna ficha citada tiene "Profundidad: solo abstract" vigente (`wang2025adaptiveweighting.md`:13 la retira). Sin contenido retirado: Dice/HD95, "31-60 %", BFC/ISC no aparecen; difusion latente y ControlNet solo como teoria y como descartadas (l.104).

**Conteo: alta=0 media=1 baja=2**

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2, OC-3 | l.68, `\GAPDEC` | "a cual de los dos tipos de tornillo corresponde el corredor que mide este trabajo" | `tesis/main.tex`:123 ("maximum transsacral corridor diameter"); `docs/SITUACION_ACTUAL.md`:183 ("empieza en la cortical externa de un ilion, atraviesa el sacro y termina en la cortical externa del ilion opuesto"); `docs/04-implicancias.md` #130 (ABIERTA) | El GAP pregunta por la geometria del corredor medido como si no constara, pero el registro la describe: de la cortical externa de un ilion a la del opuesto (cruza ambas articulaciones, rasgo que `docs/03-glosario.md`:74 asigna al transiliosacro). Lo que #130 deja abierto es que tornillo representa ese corredor y si le valen las convenciones de Kaiser et al., no que corredor se mide. Mantener el GAP (regla 3, #130 abierta) pero con el hecho registrado visible. Patron PAT-19 reincide (GAP que declara ausente un dato ya registrado) | `\GAPDEC{qué tornillo representa el corredor que mide este trabajo, que el registro describe como transsacro, de la cortical externa de un ilion a la del ilion opuesto, y con ello si le aplican el corredor de 10~mm y la holgura radial de Kaiser et al., definidos para el tornillo iliosacro}` |
| T02 | baja | E-R6 | l.68 | "hasta el cuerpo de la primera o de la segunda vertebra sacra" | ficha `smith2006iliosacral`:69 ("through the ileum into either the S1 or S2 vertebrae", M&M, p. 235) | La evidencia dice "vertebrae", no "vertebral body"; la ficha no registra "cuerpo" para el destino del tornillo (solo `routt1997` usa "upper sacral vertebral body" para describir el ala). Precision anadida sin fuente | "hasta la primera o la segunda vertebra sacra" |
| T03 | baja | G-T4 | l.122 | "En ambos casos hubo, sin embargo, decisiones posteriores a ver datos: esa regla ..." | `capitulo3.tex`:75, 255 ("extension de la compuerta al latente de Guo et al., cuya cota ... sobre los mismos pacientes de prueba"), 265 ("añade un septimo candidato") | Para el Obj 1 el recuento de decisiones posteriores a ver datos omite la extension de la compuerta al latente de Guo et al., evaluada sobre los mismos pacientes de prueba; justo despues el parrafo habla de la multiplicidad, que esa extension aumenta. Perdida menor de condicion (PAT-31) | "...esa regla se fijo conociendo un resultado exploratorio desfavorable que incluia a los pacientes de prueba, la compuerta se extendio despues a un septimo candidato sobre esos mismos pacientes, y tres decisiones del Objetivo~2 ..." |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.11 | Funcion del capitulo; reparto con caps. 2 y 3 | estructura propia; `\ref` existentes (lint PASA) | si |
| l.13 | Orden de secciones y su razon; que pieza usa cada seccion | estructura; `capitulo3.tex`:9-31 | si |
| fig. 1.1 | Conceptos -> Obj 1 (compuerta, canales), Obj 2 (muestreador), Obj 3 (sintetizador, $B_\delta$), Obj 4 (SAP), protocolo fisico | `capitulo3.tex`:13, 20-31, 172, 189, 219 | si |
| l.31 | Lectura del detector = indice del sinograma | `deman2007catsim` ("y_i is the detector signal at sinogram index i", Sec. 2.1, p. 1) | si |
| l.31 | Senal = suma sobre energias, atenuada por longitud en cada material | `deman2007catsim` defs. A_ik, l_iso, mu_ok (Sec. 2.1, p. 1) | si |
| l.31 | Coef. de atenuacion lineal por material y energia | `deman2007catsim` ("mu_ok is the linear attenuation coefficient ...") | si |
| l.31 | Abadi et al., en DukeSim, usan Beer-Lambert | `abadi2019`:51 ("computed using the Beer-Lambert Law", Sec. II-B, p. 1458); titulo de la ficha | si |
| l.31 | Wang et al., implantes cocleares, Beer-Lambert en cinco energias | `wang2019cochlear`:52, 56 ("Beer-Lambert law discretized on 5 different energies", Intro, p. 2) | si |
| l.33 | FBP en De Man 1999, CatSim y Karageorgos | `deman1999` Sec. II-C; `deman2007catsim` Sec. 3.1; `karageorgos2024ddpm` Sec. II-F | si |
| l.33 | Park: FBP supone modelo monocromatico de Radon; desvio no lineal | `park2015ct`:9 | si |
| l.33 | Cohorte solo con volumenes reconstruidos | `capitulo3.tex`:42-46; `docs/02-datos.md` | si |
| l.33 | Lo medido y lo generado por el sintetizador, en dominio de imagen; solo el protocolo fisico (previsto) pasa por proyecciones | `capitulo3.tex`:172, 219-221, 261 | si |
| l.35 | Agua 0 HU, aire -1000 HU por definicion | `wu2022xcist` (Discussion Exp. 1, p. 13) | si |
| l.35 | Conversion HU-mu con coef. del agua por energia | `wang2019cochlear` (Sec. 2.1, p. 4) | si |
| l.35 | `\GAPLIT` fisica de TC (HU como transformacion; FBP) | ninguna ficha la define; MAPA:75 | si (GAP justificado) |
| l.35 | Hueso > 150 HU fuera de la geometria metalica (Peters) | `peters2025hybrid`:177; `capitulo3.tex`:213 | si |
| l.35 | Metal clinico segmentado con 2500 HU (Wang, Li) | `wang2025adaptiveweighting`:110, 186 (Sec. V-A-2, p. 2413); `li2024` Sec. IV-E, p. 1878 | si |
| l.35 | 2500 HU: cribado de cohorte y delimitacion del metal real | `capitulo3.tex`:46, 73, 178; DEC 2026-09-20 (2) D1 | si |
| l.35 | Fraccion de voxeles sacros a 150 HU o menos a lo largo del eje del corredor | `capitulo3.tex`:85 (mediana 0.42) | si |
| l.37-41 | Ventana: saturar a $[w_{\min}, w_{\max}]$ y escalar a [0,1] (Ec. ventana) | `wang2025adaptiveweighting`:112, 184 (Eq. 2, p. 2410) | si |
| l.42 | Saturacion; fraccion inversamente proporcional al ancho | demostracion desde Ec. ventana | si |
| l.44 | Tres ventanas [-1000,2000], [-320,480], [-160,240] HU; cascada, no canales | `wang2025adaptiveweighting`:108 (Sec. V-A-1, p. 2412); Sec. III, p. 2410 | si |
| l.44 | Techo 2000 < 2500: el metal satura | derivacion de las dos cifras; `capitulo3.tex`:71 | si |
| l.44 | Variantes del Obj 1: techo 20 000 HU; arcoseno hiperbolico sobre [-1000, 20 000] HU, no lineal | `capitulo3.tex`:69; `tesis/main.tex`:77; DEC 2026-09-17 (l.1049) | si |
| l.44 | `\GAPDATO` forma y parametros del arcoseno hiperbolico | sin formula en TM, DEC ni `experiments/objetivo1/*.md` (solo la etiqueta `pub+asinh`); solo en `src/common/ventanas.py`; MAPA:80 | si (GAP justificado) |
| l.44 | Compuerta mide la ida y vuelta como MAE en hueso (Ec. mae) | `capitulo3.tex`:58-65 | si |
| l.44 | Sintetizador usa la codificacion multiventana como canales, sin autoencoder | `capitulo3.tex`:172 | si |
| l.44 | `\GAPDEC` codificacion y precision del sintetizador | replica `capitulo2` (cotejado con `experiments/objetivo1/p1_compuerta.md`:31-38, #129.1); `diseno_A.md`:57 `[SUPUESTO]` | si (GAP justificado) |
| l.48 | Rayas claras y oscuras que ocultan anatomia; severidad por tamano, forma, aleacion | `selles2024marreview` Sec. 1, p. 1 | si |
| l.48 | Osteosintesis en categoria intermedia, cualitativa, sin criterio numerico | `selles2024marreview` Tabla 1, p. 6; criterio numerico NO ENCONTRADO | si |
| l.50 | Selles: BH, inanicion, dispersion, bordes como principales | `selles2024marreview` ("... are the main contributors") | si |
| l.50 | De Man: simulacion 2D; mas importantes BH, dispersion, ruido, EEGE; todas producen rayas; sin peso numerico | `deman1999`:69-75 (Respuestas 1); Conclusiones, p. 695 | si |
| l.52 | BH: absorcion preferente de baja energia | `selles2024marreview` Sec. 1, p. 1 | si |
| l.52 | Park: cupping dentro; rayas fuera de la region | `park2015ct`:9; Intro, p. 2 | si |
| l.52 | De Man: rayas oscuras en direcciones de mayor atenuacion; rayas que conectan metales | `deman1999` Sec. III-B, p. 693 | si |
| l.54 | Inanicion: muy pocos fotones; faltan datos | `selles2024marreview` Sec. 1, p. 1 | si |
| l.54 | De Man no nombra la inanicion; ruido como lineas finas alternas dependientes de la atenuacion integrada | `deman1999`:71-72; Sec. III-E, p. 694 | si |
| l.54 | Dispersion por densidad electronica; razon muy pequena produce rayas | `selles2024marreview` Sec. 1; `deman1999` Sec. III-C | si |
| l.56 | EEGE: rayas tangentes a bordes rectos; rayas que irradian; Selles: alineadas con el borde | `deman1999` Sec. III-D, p. 694; `selles2024marreview` | si |
| l.56 | Ninguna da distancia; De Man no mide extension | `deman1999` Respuestas 2 (NO ENCONTRADO); `selles2024marreview` (NO ENCONTRADO) | si |
| l.58 | Volumen parcial no lineal; una discontinuidad local, dos o mas de largo alcance; hueso, monocromatica | `glover1980nonlinear` Que hace; Sec. II, pp. 240-243; Restriccion | si |
| l.58 | De Man en 2D, volumen parcial axial fuera de alcance | `deman1999`:73-74 (Sec. II-A, p. 691) | si |
| l.60 | Rayas fuera del metal | `deman1999` Sec. III-B/D; `park2015ct` Intro, p. 2 | si |
| l.60 | Ancho de $B_\delta$ como convencion | `capitulo2.tex` §Representacion; #57/#98 ABIERTAS, no afirmado como resuelto | si |
| l.60 | De Man aisla causas modificando el sinograma | `deman1999` Sec. II-D, p. 693 | si |
| l.60 | Supuesto del dominio de imagen, con remision a amenazas | `capitulo3.tex`:261 | si |
| l.62 | CatSim dentro de XCIST; protocolo de Peters sobre CatSim | `wu2022xcist` (Simulation, p. 6); `peters2025hybrid` Abstract | si |
| l.62 | CatSim modela espectro, ruido cuantico y electronico, VP no lineal, dispersion; FBP | `deman2007catsim` Abstract, p. 1; Sec. 3.1, p. 5 | si |
| l.62 | Este trabajo preve usar la simulacion fisica como comparacion | `capitulo3.tex`:219-225 (GAPDATO, GAPDEC #90); BITACORA §2 2026-09-30 | si |
| l.66 | Solo fracturas Tile y Pennal B y C; B rotacional, C rotacional y vertical | `zwingmann2009navigated` M&M, p. 1834; Discussion, p. 1837 | si |
| l.66 | Percutanea, guiada por imagen; grados = referencia clinica del Obj 2 | `zwingmann2009navigated` Que hace; `capitulo3.tex`:79 | si |
| l.68 | Smith: tornillo por el ilion hasta S1 o S2 | `smith2006iliosacral`:69 (M&M, p. 235) | parcial (T02) |
| l.68 | Tres corticales: dos del ilion, una del ala | `smith2006iliosacral` ("intended to cross 3 cortices (2 ileum, 1 sacral ala)", M&M, p. 235) | si |
| l.68 | Ala sacra desciende lateral y caudal desde el cuerpo vertebral superior | `routt1997`:122 (Sacral Dysmorphism, p. 206) | si |
| l.68 | `\GAPLIT` anatomia pelvica | ninguna ficha ni `docs/03-glosario.md` define los seis terminos; MAPA:79 | si (GAP justificado) |
| l.68 | Transiliosacro cruza ambas SI y sale por la tabla externa opuesta | `mclaren2021corridor` M&M, PDF p. 2 | si |
| l.68 | Este trabajo trata como no intercambiables los dos tipos; McLaren transiliosacro | `docs/03-glosario.md`:74-76; `docs/04-implicancias.md`:1307-1308 | si |
| l.68 | Kaiser eligen 10 mm para el paso de un tornillo iliosacro | `kaiser2014dysmorphism`:72 ("chosen as a conservative size for passage of an iliosacral screw", p. e120(2)) | si |
| l.68 | Sec. SAP trata el tornillo como uno que entra y sale por la cortical del ilion | `capitulo3.tex`:196 | si |
| l.68 | `\GAPDEC` tipo de tornillo del corredor medido | #130 ABIERTA (GAP obligatorio, regla 3); pero la geometria medida consta en `tesis/main.tex`:123 y `docs/SITUACION_ACTUAL.md`:183 | parcial (T01) |
| l.70 | Routt: supino, fluoroscopia en tres planos | `routt1997` (Intro, p. 206) | si |
| l.70 | Zwingmann: guia fluoroscopica "convencional" frente a navegacion; equipo que rota 190 grados | `zwingmann2009navigated` (Abstract; M&M, p. 1834) | si |
| l.70 | Posicion final evaluada en TC posoperatoria | `zwingmann2009navigated` M&M, p. 1835 | si |
| l.72 | Zona segura: limites alares y foraminales; L5, canal, vasos iliacos | `routt1997` Fig. 2, p. 207; pp. 212-213 | si |
| l.72 | Gardner: dos conos punta a punta; seccion minima en plano ortogonal | `gardner2010safezones` M&M, p. 623 | si |
| l.74 | McLaren: recta dentro de contornos; diametro hasta romper la cortical en tres puntos | `mclaren2021corridor` M&M, PDF p. 2 | si |
| l.74 | 10 mm en Gardner, Kaiser y McLaren; los tres lo toman de trabajos anteriores; McLaren: minimo no establecido | `gardner2010safezones`:71, 303-304; `kaiser2014dysmorphism` p. e120(2); `mclaren2021corridor` (implicancias:1289) | si |
| l.74 | Corredor medido sobre mascaras de TotalSegmentator; criterio de viabilidad propio | `capitulo3.tex`:85, 89; `wasserthal2023` | si |
| l.76 | Kaiser: reformateo perpendicular a S1; angulacion contra crestas y espinas posteriores | `kaiser2014dysmorphism` Fig. 1, p. e120(3); p. e120(2) | si |
| l.76 | Poses en el marco de Kaiser; aplicabilidad con metal | `capitulo3.tex`:83, 93-97 | si |
| l.78 | Posicion ideal de Smith; tres tipos de perforacion; grados 0-3 con 2 y 4 mm | `smith2006iliosacral` Screw Position, p. 236 | si |
| l.78 | Grado calculado como protrusion fuera de envolvente osea segmentada | `capitulo3.tex`:189-194, 257 | si |
| l.80 | Escala tomada de tornillos pediculares; escala angular | `smith2006iliosacral` Screw Position, p. 236 | si |
| l.80 | `\GAPDEC` dimension angular en SAP | #11 ABIERTA; MAPA:41 | si (GAP justificado) |
| l.80 | Zwingmann aplica la escala en TC posoperatoria, por tecnica | `zwingmann2009navigated` M&M, p. 1835; Results, pp. 1836-1837 | si |
| l.80 | Hinsche: definicion binaria (insegura si perfora comprometiendo estructuras) | `hinsche2002fluoroscopy` Measurements, p. 138 | si |
| l.82 | Grados 1 y 2 de 2 mm; grado 3 abierto; equiespaciado es convencion | demostracion desde Smith; `capitulo3.tex`:200, 261 | si |
| l.86 | Difusion en imagen medica (revision) | `kazerouni2023diffusionsurvey` | si |
| l.86 | Ho: cadena de Markov; ruido gaussiano; $n_{\max} = 1000$ | `ho2020denoising` ("We set T = 1000 for all experiments", Sec. 4, p. 5) | si |
| l.86 | Dorjsembe: proceso directo borra la estructura | `dorjsembe2024` (§II, p. 2) | si |
| l.86-91 | Forma cerrada (Ec. difusion-directa) en DiffBoost y Dorjsembe; fuentes escriben $\bar\alpha_t$ | `zhang2025diffboost` Ec. 3, p. 3672; `dorjsembe2024` Ec. (1), p. 2 | si |
| l.91 | Nichol y Dhariwal: calendario coseno; varianzas de cocientes sucesivos | `nichol2021improved` Sec. 3.2, p. 8165 | si |
| l.91 | Zhang et al.: varianzas en (0,1) | `zhang2025diffboost` ("β_t ∈ (0, 1) represents the variance schedule", Sec. III-A, p. 3672) | si |
| l.93-98 | Prediccion del ruido; objetivo (Ec. perdida) en Rombach; $n$ uniforme | `ho2020denoising`; `rombach2022latentdiffusion` Ec. 1, §3.2, p. 4 | si |
| l.98 | U-Net en Ho y Song; definicion de Ronneberger | `ho2020denoising`, `song2021ddim` Ap. D.1, p. 16; `ronnenberger2015unet` Que hace | si |
| l.100 | Song: no markoviano, mismo objetivo, determinista, sin reentrenar; 10 a 50 veces | `song2021ddim` ("10× to 50× faster in terms of wall-clock time", Resumen, p. 1) | si |
| l.100 | Las tres en imagenes naturales, sin TC ni metal | `ho2020denoising`, `song2021ddim`, `nichol2021improved`: Restriccion | si |
| l.102 | Rombach: concatenacion o atencion cruzada; Dorjsembe concatena la mascara | `rombach2022latentdiffusion` Fig. 3, p. 4; §4.3.2; `dorjsembe2024` §II, p. 2 | si |
| l.102 | ControlNet: base congelada, copia del codificador, convoluciones en cero | `zhang2023controlnet` §3.1-3.2, pp. 3-4 | si |
| l.104 | LDM: dos etapas, decodificacion en una pasada; perdida perceptual y adversarial; elimina alta frecuencia; cuello de botella por pixel | `rombach2022latentdiffusion` §3.1-3.2, §1, §5 | si |
| l.104 | 25 HU; Obj 1 como condicion; veredicto negativo descarto la ruta latente; ControlNet descartado con ella | `capitulo3.tex`:20, 67-71, 174 | si |
| l.106 | RePaint: modelo incondicional; combina regiones; avanza y retrocede | `lugmayr2022repaint` Que hace (p. 11462) | si |
| l.106 | Inpainting de Rombach por concatenacion | `rombach2022latentdiffusion` Tabla 15, p. 25 | si |
| l.106 | Sintetizador: parche con G borrada, mascaras, copia fuera de G | `capitulo3.tex`:172 | si |
| l.106 | `\GAPDEC` muestreo frente a RePaint y LeFusion | #106, #117 ABIERTAS; MAPA:69 | si (GAP justificado) |
| l.108 | 2.5D: cortes axiales con contexto contiguo | `capitulo3.tex`:172; `diseno_A.md` §4 | si |
| l.108 | `\GAPDEC` numero de cortes (borrador: 3, central) | `diseno_A.md` §4 `[SUPUESTO]`; MAPA:78 | si (GAP justificado) |
| l.108 | Lectura de Glover: cortes vecinos no reproducen la integracion | `glover1980nonlinear`; marcada "este trabajo lee" | si |
| l.112 | Tres tipos de resultado; Obj 1 promedia por paciente; Obj 3 pareado por paciente | `capitulo3.tex`:71, 223, tabla :242-244 | si |
| l.112 | `\GAPDEC` agregacion por paciente en el Obj 3 | `capitulo3.tex`:223; MAPA:52 | si (GAP justificado) |
| l.112 | Obj 2 reune poses; referencia cuenta tornillos | `capitulo3.tex`:207, 265 | si |
| l.114 | W1 = suma de diferencias de FDA; unidad grado; valores 1 y 3 | `capitulo3.tex`:200-205 (Ec. w1); demostracion | si |
| l.114 | `\GAPLIT` referencia de W1 | ninguna ficha la define; MAPA:76 | si (GAP justificado) |
| l.116 | Superioridad vs equivalencia; IC 90 % de la diferencia pareada entero en $[-\Delta, +\Delta]$ | `capitulo3.tex`:225 | si |
| l.118 | Wilcoxon pareada de una cola; TOST con margen por variabilidad del metodo | `capitulo3.tex`:223, 225 | si |
| l.118 | `\GAPDEC` #90; `\GAPLIT` Wilcoxon, TOST, remuestreo | `capitulo3.tex`:225; MAPA:44, 77 | si (GAP justificado) |
| l.118 | Muestras pequenas: puede no concluir | `capitulo3.tex`:265 | si |
| l.120 | IC 95 % por remuestreo de pacientes en la compuerta | `capitulo3.tex`:71 | si |
| l.122 | Regla de la compuerta antes de la prueba que decide; poses y metrica antes de cualquier distancia | `capitulo3.tex`:58, 127 | si |
| l.122 | Regla fijada tras exploracion desfavorable con pacientes de prueba; tres decisiones post hoc del Obj 2 | `capitulo3.tex`:58, 253, 255 | parcial (T03) |
| l.122 | Multiplicidad no corregida solo favorece el aprobado | `capitulo3.tex`:265 | si |
| l.124 | MAE en HU (Ec. mae); RMSE nunca menor que MAE; RMSE de MAR como orden de magnitud | `capitulo3.tex`:60-67 | si |

## Comprobacion de patrones VIGENTES (dominio G-T4 / E-R6)
PAT-9: no reincide (2500 HU con la decision D1). PAT-19: reincide (T01). PAT-31: reincide en forma leve (T03). PAT-73: no (De Man et al. como autores de CatSim, coherente con `deman2007catsim`). PAT-85: no (lecturas propias marcadas "este trabajo lee"). PAT-87: no. PAT-88: no. PAT-90: no (Zhang et al. con su `\cite`). PAT-94: no. PAT-95: no (lo que la respuesta r01 dice de las fichas coincide: `deman1999`:71, `kaiser2014dysmorphism`:72, `routt1997`:122, `smith2006iliosacral`:69). PAT-100, PAT-101, PAT-104, PAT-105: corregidos, no reinciden. PAT-39: no. PAT-103: no.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP de decision redactado como si faltara el dato, cuando el registro ya da el hecho y solo falta la decision | G-T4, OC-2 | "a cual de los dos tipos corresponde el corredor que mide este trabajo" | PAT-19 |
| Recuento de decisiones posteriores a ver datos que omite una de las que enumera `sec:amenazas` | G-T4 | "esa regla se fijo conociendo un resultado exploratorio..." (sin la extension a Guo et al.) | PAT-31 |
