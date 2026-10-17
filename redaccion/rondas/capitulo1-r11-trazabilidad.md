# Auditoria de trazabilidad — capitulo1 — r11

Archivo: `overleaf/secciones/capitulo1.tex` (153 lineas). Respuesta previa: `capitulo1-r10-respuesta.md`; no contiene hallazgos rechazados. Lint r11: PASA, 0 `\GAPLIT`, 0 `\GAPDATO`, 0 `\GAPDEC` y una baja E-P1 en :51 que no constituye hallazgo de trazabilidad: los valores de la compresion estan documentados en `experiments/registro/registro_metodos_2026-10-15.md`:7-16. Encargo: `redaccion/ENCARGO_2026-10-16.md`. No se abrio ningun PDF.

Las 44 claves citadas existen en `overleaf/referencias.bib`; los apellidos nombrados coinciden con el primer autor y ninguna cita funciona sola como sujeto gramatical. No aparecen el rango 31--60 %, BFC ni ISC, ni Dice/HD95 como evaluacion downstream. La difusion latente y ControlNet aparecen solo como antecedentes descartados (:121-123), de acuerdo con el alcance vigente. El capitulo no contiene `\REVVISUAL` ni afirma realismo visual. Las implicancias abiertas que toca quedan presentadas como supuestos o limitaciones, no como hechos resueltos.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | Sin hallazgos. | — |

TOTAL alta=0 media=0 baja=0

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :11-13, :15-27 | Funcion del capitulo y relacion de conceptos con los cuatro objetivos | `overleaf/secciones/capitulo3.tex`:13-38, :301-307 | si |
| :31 | Coeficiente de atenuacion, Beer--Lambert y supuesto monoenergetico | `kak2001book`, filas "Atenuacion exponencial", "Logaritmo medido" y "Condicion monoenergetica" | si |
| :31 | Haces policromaticos y endurecimiento del haz | `kak2001book`, filas "Fuente medica real" y "Definicion de beam hardening" | si |
| :31 | Sinograma y modelo espectral de CatSim | `deman2007catsim`, evidencia de la Sec. 2.1 | si |
| :31 | DukeSim aplica Beer--Lambert; Wang et al. discretizan cinco energias | fichas `abadi2019` y `wang2019cochlear` | si |
| :33 | Retroproyeccion filtrada; uso por De Man, CatSim y Karageorgos; Radon monocromatico | fichas `kak2001book`, `deman1999`, `deman2007catsim`, `karageorgos2024ddpm`, `park2015ct` | si |
| :33 | Dominios; cohorte reconstruida; protocolo fisico pasa por proyecciones | `docs/02-datos.md`; `overleaf/secciones/capitulo3.tex` §§Datos y Apariencia | si |
| :35 | Formula HU; agua 0 HU; aire ideal -1000 HU; dependencia de energia | fichas `kak2001book`, `wu2022xcist`, `wang2019cochlear` | si |
| :35 | Hueso sobre 150 HU; metal a 2500 HU; cribado de la cohorte | fichas `peters2025hybrid`, `wang2025adaptiveweighting`, `li2024`; DEC 2026-09-11 (3) | si |
| :35 | Mediana 0.42 de voxeles a 150 HU o menos en mascaras sacras | `tesis/main.tex`:123; `experiments/objetivo2/maintex_cifras.md`:4, :17 | si |
| :37-42 | Ventana, saturacion, ecuacion y compromiso entre rango y contraste | `wang2025adaptiveweighting`, fila de evidencia de la Ec. 2; derivacion declarada | si |
| :44 | Tres ventanas de Wang et al. y uso en cascada | ficha `wang2025adaptiveweighting` | si |
| :46 | Tres codificaciones y techos de 2000 y 20 000 HU | `overleaf/secciones/capitulo3.tex`:85; `experiments/objetivo1/e6c_techo_lw.py`:73-81 | si |
| :48-51 | Formula `asinh`, saturacion [-1000, 20 000], escala 500, extremos -2 y 40, rango [0,1] e inversa | `experiments/registro/registro_metodos_2026-10-15.md`:7-16; `experiments/objetivo1/e6c_techo_lw.py`:47, :61-69, :81 | si |
| :51 | Resolucion fina cerca de 0 HU y gruesa en el rango alto | `experiments/registro/registro_metodos_2026-10-15.md`:13; `e6c_techo_lw.py`:61-62 | si |
| :53 | Error de ida y vuelta; sintetizador con tercera codificacion, float32 y sin autoencoder | DEC 2026-10-08 pto 1; `src/common/ventanas.py`:53-64 | si |
| :55 | Suelo comun de -1000 HU y error en hueso que no observa la cola baja | DEC 2026-10-05 (suelo); `e6c_techo_lw.py`:76-81 | si |
| :55 | Regla del suelo no aplicable; bloqueo por congelamiento; sensibilidad posterior | DEC 2026-10-15 pto 1, `docs/01-decisiones.md`:2571-2575 | si |
| :59 | Definicion de artefacto; categoria intermedia cualitativa | ficha `selles2024marreview` | si |
| :61 | Listas de mecanismos de Selles y De Man; todas las causas simuladas producen rayas | fichas `selles2024marreview` y `deman1999` | si |
| :63 | Endurecimiento, *cupping*, rayas y razon dispersa/primaria 0.0001 arbitraria | fichas `selles2024marreview`, `park2015ct`, `deman1999` | si |
| :65 | Inanicion de fotones; artefacto de ruido no lineal; saturacion bajo -1000 HU | fichas `selles2024marreview`, `deman1999`; `e6c_techo_lw.py`:81 | si |
| :67 | Efecto exponencial de gradiente de borde y ausencia de distancia publicada | ficha `deman1999`, incluida fila "distancia: NO ENCONTRADO EN EL PDF" | si |
| :69 | Volumen parcial no lineal, discontinuidades, hueso y modelo monocromatico | fichas `glover1980nonlinear` y `deman1999` | si |
| :71 | Rayas fuera del implante; ancho de $B_\delta$ como convencion; supuesto del dominio de imagen | fichas `deman1999`, `park2015ct`; `capitulo3.tex` §Amenazas | si |
| :73 | CatSim/XCIST y mecanismos; protocolo fisico como comparacion | fichas `wu2022xcist`, `deman2007catsim`; DEC 2026-10-13 | si |
| :75 | Metricas de Peters, 5 % de extremos, inversion y criterio primario | ficha `peters2025hybrid`; DEC 2026-10-05 (3); DEC 2026-10-08 pto 10 | si |
| :79 | Tile B/C, via percutanea y referencia clinica externa con dos nombres de tornillo | ficha `zwingmann2009navigated`; #130 aplicada | si |
| :81 | Tornillo iliosacro, tres corticales, ala sacra, cortical, foramenes y platillos | fichas `smith2006iliosacral`, `routt1997`, `standring2020grays` | si |
| :83 | Definicion transiliaco-transsacra; traslado del umbral; corredor e implante propios | fichas `mclaren2021corridor`, `standring2020grays`, `kaiser2014dysmorphism`; #130 aplicada; `capitulo3.tex`:129 | si |
| :85 | Decubito supino, tres planos, rotacion de 190 grados y TC posoperatoria | fichas `routt1997` y `zwingmann2009navigated` | si |
| :87 | Zona segura, estructuras vecinas y dos conos de Gardner | fichas `routt1997` y `gardner2010safezones` | si |
| :89 | Diametro maximo; umbral 10 mm heredado; holgura 1--2 mm sobre 6.3--8 mm | fichas `mclaren2021corridor`, `kaiser2014dysmorphism`, `gardner2010safezones` | si |
| :89 | Medicion propia sobre mascaras de TotalSegmentator | ficha `wasserthal2023`; `capitulo3.tex` §Corredor | si |
| :91 | Marco de Kaiser, margen de 5 mm y diferencia no medida entre techo de S1 y platillo | ficha `kaiser2014dysmorphism`; #138; `capitulo3.tex` §Amenazas | si |
| :93 | Posicion ideal, grados 0--3 y protrusion propia fuera de envolvente | ficha `smith2006iliosacral`; `capitulo3.tex` §SAP | si |
| :95 | Escala angular incompleta; Zwingmann y SAP solo perforacion; Hinsche binaria | fichas `smith2006iliosacral`, `zwingmann2009navigated`, `hinsche2002fluoroscopy`; DEC 2026-10-08 pto 15 | si |
| :97 | Escala ordinal y equiespaciado como convencion | derivacion de :93; `capitulo3.tex` §SAP | si |
| :99 | SAP sin densidad; Arand, ala frente a S1; trabajo futuro | DEC 2026-10-08 pto 14; ficha `arand2019pelvicring` | si |
| :103-108 | Cadena de Markov, 1000 pasos, ecuacion directa, calendario coseno y betas en (0,1) | fichas `ho2020denoising`, `dorjsembe2024`, `zhang2025diffboost`, `nichol2021improved` | si |
| :110-115 | Perdida simplificada, proceso inverso y U-Net | fichas `rombach2022latentdiffusion`, `ho2020denoising`, `song2021ddim`, `ronnenberger2015unet` | si |
| :117 | Prediccion $v$, recuperacion de imagen limpia y dominio natural de la fuente | ficha `salimans2022progressive`; DEC 2026-10-08 pto 2 | si |
| :119 | DDIM no markoviano, determinista, 10--50 veces mas rapido y 50 pasos propios | ficha `song2021ddim`; DEC 2026-10-08 pto 4 | si |
| :121 | Dos vias de condicionamiento y arquitectura de ControlNet | fichas `rombach2022latentdiffusion`, `dorjsembe2024`, `zhang2023controlnet` | si |
| :123 | Difusion latente, cuello de botella, criterio de 25 HU y descarte propio | ficha `rombach2022latentdiffusion`; `experiments/objetivo1/p1_compuerta.md`:5, :25; DEC 2026-09-19 | si |
| :125 | RePaint, *inpainting* condicionado, LeFusion y muestreo propio | fichas `lugmayr2022repaint`, `rombach2022latentdiffusion`, `zhang2025lefusion`; DEC 2026-10-08 pto 4 | si |
| :127 | Modelo 2.5D, tres cortes, limite de computo y lectura del volumen parcial | DEC 2026-10-08 pto 3; `capitulo3.tex` §Sintetizador; ficha `glover1980nonlinear` | si |
| :131 | Unidades de analisis; 13 valores y exclusion de uno de 14 pacientes | `capitulo3.tex`:421, :537; DEC 2026-10-09 (8) | si |
| :133 | Wasserstein-1 unidimensional, suma discreta, unidad grado y ejemplos 1/3 | ficha `vallender1974wasserstein`; derivacion explicita | si |
| :135 | TOST, alfa 0.05, IC90, *t* y sensibilidad exacta posterior | fichas `schuirmann1987comparison`, `walker2011understanding`; DEC 2026-10-15 pto 14 | si |
| :137 | TOST primario preinscrito y ejecutado; margen 196.3 HU; tres desenlaces y direccion | DEC 2026-10-15 ptos 13, 15 y 21; DEC 2026-10-15 (4) pto 1 | si |
| :139 | Nombre propio "no concluyente" y mapeo condicionado a Walker y Lakens | DEC 2026-10-15 (4) pto 1, `docs/01-decisiones.md`:2702-2706; fichas `walker2011understanding` filas :84, :107, :146-147 y `lakens2017equivalence` filas :65-75 | si |
| :141 | Wilcoxon de una cola, pareada por paciente y procedimiento de rangos | ficha `wilcoxon1945rankingmethods`; `capitulo3.tex`:421 | si |
| :143 | Remuestreo con reemplazo, percentiles y pacientes como bloques en Objetivo 2 | ficha `efron1992bootstrap`; `experiments/objetivo2/e15_w1_sensibilidad.md`; `capitulo3.tex`:535 | si |
| :145 | Fisher bilateral: margenes fijos, tres convenciones, minlike y `stats` 2.11.0 | fichas `fisher1935logic` y `fay2010two`, filas :39-50 | si |
| :145 | Programa original ausente; SciPy 1.15.3 reproduce cuatro valores con minlike | `experiments/registro/registro_metodos_2026-10-15.md`:69-74; `r_fisher_amenazas.py`:1-20 | si |
| :145 | Quince casos por grupo y lectura sugerente | `docs/04-implicancias.md` #132; `capitulo3.tex` §Amenazas | si |
| :147 | Cronologia de reglas, tres decisiones posteriores, seis combinaciones y veredicto negativo | `capitulo3.tex`:85-89, :487, :535; #91; preinscripcion del Objetivo 2 | si |
| :149 | Extension a Guo et al., septima combinacion, mismos pacientes y diseño inalterado | ficha `guo2025maisi`; #93; DEC 2026-09-19; `capitulo3.tex`:93, :535 | si |
| :151 | Solo prueba principal confirmatoria; analisis posteriores descriptivos y no ascendentes | DEC 2026-10-15 regla general y pto 15; `capitulo3.tex`:537 | si |
| :153 | Diferencia MAE/RMSE, desigualdad y uso como orden de magnitud | derivacion; `capitulo3.tex`:83; `capitulo2.tex` §Representacion | si |
| global | Claves, autores y uso gramatical de las citas | `overleaf/referencias.bib`; 44 claves cotejadas | si |
| global | Contenido retirado y decision de realismo del 2026-10-16 | `docs/00-tesis.md`; `docs/01-decisiones.md`:2717-2736; busqueda en el `.tex` | si |

## Patrones
sin patrones
