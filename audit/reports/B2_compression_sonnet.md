# B2 — Scientific Compression Editor (externo) — capitulo3 367-525 y 546-565; capitulo4 1-223 y 234-247

Metodo: lectura de `capitulo3.tex`, `capitulo4.tex`, `docs/RUBRICA.md`, y contexto puntual de `capitulo1.tex` (§mt-estadistica) para detectar repeticion entre capitulos. Conteo de palabras con un script de regex (LaTeX limpiado; celdas de tabla incluidas; macros `\REVVISUAL/\GAP*` incluidas). Precision estimada +-5 %. Juzgo solo por el texto. No evalue 526-545 (realismo), v2, amenazas, limitaciones, conclusiones ni resumen.

Alcance medido: ~12 460 palabras (cap3 ~7 660; cap4 ~4 800), ~21 % del documento.

## 1. Diagnostico en cinco puntos

1. **Tres definiciones de la misma regla**: los tres desenlaces (equivalencia / no equivalencia / no concluyente) estan en cap1 §mt-estadistica, en cap3:496-498 y en cap4:128.
2. **La prosa del cap4 recita las tablas**. Casi cada parrafo de 80, 84, 86, 94, 130, 136, 138, 142, 168, 170, 176 y 198 repite cifras que ya estan en `tab:res-sap`, `tab:res-tost`, `tab:res-anillos`, `tab:res-integridad` o `tab:res-ea1`. Es el mayor ahorro con menor riesgo.
3. **Resultados en metodologia**: cap3:389-408 (comparacion principal de eta2_exc y `tab:c4-eta`, cuya etiqueta ya dice "c4"), cap3:484-488 (amplitudes y cascaras de validacion), cap3:524 (CV de la v1) y cap3:385 (valores de control).
4. **Historia de decisiones dispersa**: fechas (9, 11, 12, 15 de octubre; 20 de noviembre), "se anadio", "errata", "ya se corrio" aparecen en 377, 420, 424, 430, 446, 484-486, 496, 500, 508, 514, 548 y se repiten en cap3:38-40 y Amenazas (fuera de alcance). Una cronologia unica en tabla permitiria dejar solo una etiqueta en linea.
5. **Cada análisis añadido se describe dos veces** (definicion en cap3:508-516; redefinicion en cap4:138-142, 168) y los diseños no ejecutados se describen con detalle operativo que no aporta reproducibilidad.

## 2. Hallazgos (Sev = severidad; Conf = confianza; ahorro en palabras, estimado)

### Capitulo 3

**B2-001** | c3:371, 373, 432 | "mediante el cambio de volumen y el coeficiente de Sørensen-Dice… sobre 150 HU" / "no invierten su fórmula, sino su lectura… sobre 150~HU… 2500~HU" | `bone integrity` y `metal integrity` se definen en 371 y otra vez en 432; 373 es solo señalizacion ("se define… en la Sección…"). | Sev media | Conf alta | **FUSIONAR**: una tabla (metrica | definicion | region | umbral | lectura invertida) y un parrafo. | -130

**B2-002** | c3:375 | "Fuera de $G$, el sintetizador copia el volumen… preservación exacta por construcción… RMSE y SSIM" | Se dice tres veces que la preservacion es exacta (375, 412 de §sintetizador, cap4:174). La parte de RMSE/SSIM del protocolo fisico se repite en cap4:174. | Sev baja | Conf alta | **COMPRIMIR** a la definicion (rango -1000 a 2000 HU, region, "caracteriza al brazo, no es resultado"). | -40

**B2-003** | c3:383, 385 | "La primera versión… dio 0.49… un halo… dio 0.805… la segunda dio −0.01… 0.008… 0.556… 0.240" | Historia de la v1 de la metrica + valores de control en prosa. Los controles de validez son evidencia valida (G-T4) pero se leen mejor en tabla 4 controles x {v1, v2}. | Sev media | Conf media (la tabla solo puede usar los valores del texto: v1 solo da un rango "0.57-0.81"; no completar celdas) | **COMPRIMIR** con tabla pequeña; conservar el criterio de eleccion de la v2 ("por el fallo de la primera"). El `\GAPDATO` de 385 debe resolverse antes. | -90

**B2-004** | c3:381, 387 | "Según qué se mida del corte, la métrica tiene dos modos… Hay dos referencias…" | Combinacion brazo x modo x referencia descrita en prosa; es una matriz 3x2. | Sev baja | Conf media | **COMPRIMIR** a tabla brazo | modo crudo | modo residuo (como se forma) | referencia. | -50

**B2-005** | c3:389, 391, 393-408 (`tab:c4-eta`) | "En el modo residuo, esa diferencia… mediana de +0.124 con IC… K=12… 0.039… −0.178" / "La Tabla~\ref{tab:c4-eta} da la mediana…" | Resultados (medianas, IC, tabla de variantes) en el capitulo de metodologia; viola el orden datos-en-resultados (G-C10) y la etiqueta delata el destino. Busque `eta^2` en cap4: no aparece en ningun lugar de cap4:1-268. | Sev alta | Conf alta (la relocalizacion); media (verificar que no exista un destino fuera de mi alcance) | **REUBICAR** a un nuevo §"Métrica angular" en cap4 (tras `res-anadidos`), con la tabla y 389/391 comprimidos; cap3 conserva definicion (379), controles y la advertencia de exploratorio. | cap3 -306; cap4 +230 (neto -76)

**B2-006** | c3:410 | `\REVVISUAL{La figura que desenrolla el anillo…}` `\GAPDATO{figura… pendiente}` | Marcador de figura pendiente. Una figura del anillo desenrollado (angulo x distancia; un corte sintetico y uno real) explica la definicion de 379 mejor que la prosa. | Sev baja | Conf alta | **CONSERVAR** como figura unica de 1 panel doble; si no se entrega, eliminar el marcador. No inventar contenido. | 0

**B2-007** | c3:414, 422, 428, 430 y c4:198 | "33 pacientes: 19 con metal, 9… 10… 14 sin metal… queda fuera uno… 13" / "los 6… dataset6 no aportan… 13 pacientes… 9… 4" / "3.1, 3.6 y 4.7 mm" / cap4:198 "los 9… los 4…" | El flujo de cohortes de la evaluacion (33 -> 19+14 -> 13 [9+4]; 14 -> 13 -> 10) se reconstruye en cuatro lugares. | Sev alta | Conf alta | **COMPRIMIR + figura**: diagrama de flujo (TikZ/SVG) con n en cada nodo y el motivo de cada exclusion (pixel 1.62 mm sin eje medido; umbral 500 mm3; corredor menor que 4.91 mm). Las cifras ya consistentes entre si (19=9+10; 13=9+4; 10=4+6 sin componente). | -200

**B2-008** | c3:416, 418 | "A diferencia del protocolo publicado…" / "La guarda se fija en el mínimo por la dirección del sesgo…" | Racional repetido (el sesgo de la guarda y del suelo se explican dos veces; el aparte sobre `Amenazas` se anticipa). | Sev baja | Conf media | **COMPRIMIR** conservando 12 mm, 8 mm de extremos, guarda de un voxel, estadistico de colas 5 %/5 %, fraccion en el suelo de -1000 HU. | -75

**B2-009** | c3:420 (parte), 438, 440 | "El 15 de octubre se fijó un análisis exploratorio con 5 poses…" / "control de calidad visual… tres cortes… cuatro defectos… no se ejecutó" | Detalle operativo (cortes a 1/4 y 3/4, lista de cuatro defectos, 5 semillas) de diseños **no ejecutados**: no sirve para reproducir nada. | Sev media | Conf media (puede interesar a la autora como honestidad de diseno) | **COMPRIMIR** a: que se fijo, cuando, por que no se ejecuto, consecuencia; el resto, a la cronologia (B2-024). | -145

**B2-010** | c3:424 | "En un paciente de validación, con la pose anterior a su corrección… 51 cortes… 25" | Historia de una correccion de pose dentro de la justificacion de metodo; el argumento (cero por construccion fuera de cortes generados -> sesgo a la baja) esta en dos frases. | Sev baja | Conf alta | **COMPRIMIR**; mantener "cada brazo se mide en los cortes que produce". | -60

**B2-011** | c3:428, 430 | "costo pasaría de 15 horas…" / "errata que daba ese umbral…" / "se había omitido al congelar el diseño y entró como enmienda" | Historia de la enmienda y logistica de computo; conservar umbral 2500 HU, 500 mm3 (vs 10 mm3 en entrenamiento), tope 24 cortes, orden de agregacion. | Sev baja | Conf alta | **COMPRIMIR**; la enmienda va a la cronologia. | -85

**B2-012** | c3:436, 440 (+548) | "La *streak amplitude* es el único criterio primario…" / "El diseño… ordena tres contrastes…" | Prioridad del contraste primario y rol del control de cordura se dicen en 436, 440, 492 y 548 (y cap4:132). | Sev media | Conf alta | **FUSIONAR** en un unico parrafo de 4 frases en 440; 436 conserva solo "solo metrica, sin lector". | -50

**B2-013** | c3:444-448 | "es la línea base ingenua… oráculo de nivel…" | Receta (5371 HU, mediana de 1 781 741 voxeles, 14 182 parches, 39 casos; formula con `signo(cos 2η)`) debe quedar. La retorica en torno ("un oráculo de nivel…", "no sustituye…") es baja densidad. | Sev baja | Conf alta | **COMPRIMIR** retorica; conservar receta. | -40

**B2-014** | c3:450-454 | "Reproducir ese protocolo no es validar el simulador…" / "Esos pasos se toman de los guiones…" | Tres parrafos de atribucion y cautela; los hechos tecnicos (900 columnas, 1 000 vistas, FBP, tres materiales, densidad (HU+1000)/1000) son reproducibles y deben quedar. La cautela se dice tres veces ("no hereda su validación" en 450 y 416). | Sev media | Conf media | **COMPRIMIR** la cautela a una frase; la `tab:desviaciones` absorbe los elementos de 454 (fantoma, realce). | -80

**B2-015** | c3:474 | "Ambos repositorios declaran la licencia de tres cláusulas… parche de una línea; ni el fallo ni el parche constan…" | La licencia no aporta; el parche si es un requisito de reproducibilidad (P-MM3) pero deberia estar como diff, no como relato. | Sev baja | Conf media | **COMPRIMIR** + **TRASLADAR A ANEXOS** el parche (texto del diff, solo si existe en el repositorio; no inventarlo). Conservar los hashes `4cf3544`, `4993e87`. | -30

**B2-016** | c3:476, 478, 480 | "El primer criterio exige… 72 horas… ±20 HU… 2 %… el triple…" / "Las salidas… se fijaron…" / "La primera corrida no cumplió…" | Es un protocolo a priori con salidas por criterio y dos corridas: ideal para una tabla: criterio | umbral | salida fijada si falla | corrida 1 | corrida 2. Hoy ocupa ~430 palabras de prosa. | Sev alta | Conf alta | **COMPRIMIR a tabla** + 120 palabras de contexto. **No perder** los umbrales ni las salidas (reglas de fallo). | -180

**B2-017** | c3:482-488 | "5243 y 2166 HU con hierro y de 1881 y 1287 HU con titanio… 2 de 24 cáscaras… 0 de 24… 7036 HU… 4462 HU" | Resultados de validacion y la historia del cambio de material (hierro -> titanio) en metodologia, ademas de la repeticion de "cercania" en Amenazas (598). Se explica mejor con una tabla Fe vs Ti: amplitud por receptor, cascaras dentro del intervalo real, cascaras sobre lo real, mediana en M frente a 3092-3838 HU reales. | Sev media | Conf alta | **COMPRIMIR a tabla**; conservar la regla escrita antes de aplicarla y la nota "es un cambio posterior a ver las amplitudes". | -150

**B2-018** | c3:375, 418, 446, 482, 498, 512, 516, 524 | "(capítulo de resultados)", "Ya se corrió con la pose corregida…" | Remisiones y partes de estado repetidas ("se midio en la particion de prueba (capítulo de resultados)"). Ya lo declara cap3:38. | Sev baja | Conf alta | **ELIMINAR** salvo una por subseccion. | -90

**B2-019** | c3:496, 498, 500; c4:128; cap1:157 | "Esa lectura aplica los tres desenlaces que este trabajo fija en la Sección~\ref{sec:mt-estadistica}: equivalencia si el IC… cae entero dentro…" / "Los nombres… Su correspondencia con… Walker… Lakens… se da en la Sección" / cap4:128 "el desenlace es no concluyente, porque el IC del 90 % cruza…" | La regla y la correspondencia con Walker/Lakens estan en cap1; cap3 la reescribe y la "remite"; cap4 la vuelve a explicar. | Sev alta | Conf alta | **FUSIONAR**: la regla vive en cap1; cap3 conserva solo la fecha y la restriccion (solo la prueba del modelo evaluado con su margen es confirmatoria); cap4 pone el resultado ("no concluyente, direccion menor") y un remite. **No tocar** la regla. | cap3 -250; cap4 -60

**B2-020** | c3:502, 504, 506 | "Δ = max(s_sem, r_rep)… 196.3 HU… 6.1 HU… 115.8 HU… Un margen relativo… se descartó" | Formula y valores deben quedar. Sobra el segundo razonamiento ("un sintetizador más variable obtiene un margen más ancho…") dicho en 506 y en Amenazas; el margen relativo descartado puede ser una frase. | Sev baja | Conf media | **COMPRIMIR**. | -85

**B2-021** | c3:508, 510, 512, 514, 516 (y c4:138-142, 168) | "El primero es un IC del 90 % exacto… Otros tres repiten… piso de ruido… margen mínimo… costura… perfil por anillos… contraste pareado" | Nueve analisis añadidos descritos en 5 parrafos de prosa; cap4 los vuelve a definir (cap4:140 "el piso de ruido… la amplitud que da sin metal"; 142 "refiere el sintetizador a su propia síntesis…"; 168 "describe cómo cae la amplitud…"). Una tabla (analisis | definicion operativa | regla de lectura fijada | puede cambiar el desenlace) lo contiene entero. | Sev alta | Conf alta | **COMPRIMIR a tabla**; en cap4 solo datos. Mantener la asimetria ("solo pueden bajar la categoria") y la limitacion del contraste pareado (misma semilla, otro canal M -> otra trayectoria). | cap3 -240 (cap4 ver B2-032)

**B2-022** | c3:518, 520, 522, 524 | "Morgan la formula como la correlación entre la suma y la diferencia… Pitman…" / "Si $x$ es la amplitud… $e^{s}-1$ se aproxima a $s$…" | Derivacion propia ln -> CV (192 palabras) y descripciones de Bland-Altman/Pitman-Morgan que son marco estadistico (G-B2) y no estan en cap1. | Sev media | Conf media | **TRASLADAR A ANEXOS** la derivacion (dejar 2 frases + remite); **REUBICAR** la definicion de los tests a cap1 §mt-estadistica (ahorro neutro). Conservar que "ni la derivacion ni su uso están en sus fuentes" (honestidad, G-T4). | -180 cuerpo (+120 anexo)

**B2-023** | c3:548; 550-564 (`tab:diseno`) | "El diseño congelado el 9 de octubre y enmendado el 11 y el 12 (Sección~\ref{sec:vision})… La lectura… es posterior…" | El parrafo repite la cronologia de cap3:40 y de Amenazas; la fila 3 de la tabla (~125 palabras) mezcla primaria, descriptivas y no ejecutadas. | Sev media | Conf alta | **COMPRIMIR** el parrafo (grado de cierre por objetivo = 3 frases); partir la fila 3 en 3a/3b/3c. **Conservar la tabla** (G-C5). | -100

**B2-024** | c3:377, 420, 446, 496, 500, 508 | "el 20 de noviembre…", "El 15 de octubre se fijó…", "añadido el 15 de octubre" | Residuo de historia de decisiones en el capitulo de metodo. | Sev media | Conf media | **REUBICAR** a una tabla cronologica unica (fecha | decision | qué se había visto | efecto) en Amenazas/anexo (verificar con el revisor de ese alcance) y dejar en linea una etiqueta {preinscrito, enmienda, post hoc}. | -80

### Capitulo 4

**B2-025** | c4:10 | "Cada sección da primero los datos… El Objetivo~4 no tiene sección propia…" | Parrafo introductorio generico; repite cap3:36-38. | Sev baja | Conf alta | **COMPRIMIR** a 2 frases. | -50

**B2-026** | c4:14, 37, 39, 41, 43 | "Con la compresión arcoseno hiperbólico, la media bajó de 164.76 a 61.72…" | Todos esos valores estan en `tab:res-compuerta`. Los de 41 (ida y vuelta) y 43 (sensibilidades) solo existen en prosa y se leen mejor como 3-5 filas adicionales de la tabla. | Sev media | Conf alta | **COMPRIMIR**; añadir las filas; no borrar los IC (G-C11). | -130

**B2-027** | c4:45 | "…descargado con la utilidad monai.bundle: su guion scripts/sample.py fija…" | Detalle de inspeccion de codigo (metodo) en resultados; cap3:93 ya anuncia la comprobacion sin dar el paquete. | Sev baja | Conf alta | **REUBICAR** el nombre del paquete/script a cap3:93 (reproducibilidad); cap4 conserva 42.24 HU, mediana, rango, 11/34. | -35 (cap4)

**B2-028** | c4:236, 238, 246 | "el IC del 95 % de la mejor combinación empieza en 55.12… todos los pacientes incumplen" / "0.00 HU… 13.71 HU" | La discusion repite cifras de cap4:37-45 y la decision de rediseño de cap3:93. P-RE3 exige discusion por objetivo, no recitar. | Sev media | Conf alta | **COMPRIMIR**; conservar el alcance negativo ("no establece que ningún espacio latente…") y "pasa la compuerta si lo hace alguna" (sesgo de multiplicidad). | -108

**B2-029** | c4:49, 80, 82, 84, 86, 88 | "Sus poses se repartieron en el 51.5, 31.4, 11.1 y 6.0 %… La serie navegada reúne el 69, 15, 8 y 8 %… Con el cuerpo de 4.91 mm, el grado~0 reúne el 70.3 %… 0.138 y 0.533" | Practicamente todas las cifras de 80, 84, 86 estan en `tab:res-sap`; 69/15/8/8 y 40/37/11.5/11.5 aparecen ademas en cap3 §sap y en las filas de referencia de la tabla. | Sev alta | Conf alta | **COMPRIMIR**: dejar interpretacion (control de monotonia cumplido; solo 7.0 mm hace comparables los grados; mezcla de poblaciones) y la cifra clave. La viabilidad (88) podria ser una columna. | -230

**B2-030** | c4:242, 244 | "64.2 % frente al 69 %… 3.3 %… 15 de los 72… 0.186 y 0.299… 0.203 y 0.237… 0.395" | Tercera aparicion de las mismas cifras (tabla, 82-86, discusion). | Sev media | Conf alta | **COMPRIMIR**; mantener "el caso negativo es anatomico" (P-RE2) y la confusion con fractura (20 de 30). | -75

**B2-031** | c4:94, 128-132, 136, 138; `tab:res-tost` | "−295.3… −238.3… −329.3… +478.0… +411.7…" | La prosa enumera filas de la tabla. Las cifras no tabuladas (IC del 95 %, margen minimo 477.0 y 566.5, 1308 vs 1574 HU, p=0.000122, fraccion en el suelo) deben conservarse; mover los margenes minimos a una columna. Una **forest plot** (SVG/TikZ pgfplots: diferencia con IC del 90 % por analisis, banda sombreada ±196.3 HU, etiqueta del desenlace) comunica "cruza el limite / queda fuera" mejor que 17 filas; la tabla completa puede ir a anexo (neutro en paginas, alto beneficio). | Sev alta | Conf alta | **COMPRIMIR + figura** | -185

**B2-032** | c4:140, 142, 164 (nota), 168, 170; `tab:res-anillos` | "725 HU frente a 919… 616 frente a 727" / "1.92… 2.42… 3.16… 6.71… 4.08" / "−98.9 HU frente a −301.0" | Cifras presentes en la tabla (columnas "pareado" y razones). La nota de la tabla (≈100 palabras) incluye historia ("El registro no resume…"). Un **line plot** (amplitud vs. anillo, 5 curvas, con el sintetizador plano) muestra el "perfil plano" que hoy requiere 120 palabras; la tabla de datos se mantiene o va a anexo. Piso de ruido (140): dos filas de tabla. | Sev alta | Conf alta | **COMPRIMIR + figura** | -213

**B2-033** | c4:172, 174 | "r = −0.89 y p = 3.8×10⁻⁵… sesgo de −301.0 HU…" / "mediana de 4.3 HU… 1.2 HU… RMSE… 31.4… SSIM" | Cifras sueltas en prosa; el sesgo −301.0 duplica la tabla. Bland-Altman es un grafico (13 puntos, sesgo y limites). | Sev baja | Conf media | **COMPRIMIR** a minitabla; el grafico es opcional (no ahorra palabras). | -44

**B2-034** | c4:176, `tab:res-integridad`, `tab:res-ea1` | "mediana… 0.677… 0.800… 0.098… 0.121… 0.862… 0.856… −0.190… +0.283… +1.683" | La prosa transcribe la tabla completa (4 metricas x 3 brazos). Ademas, las dos tablas miden las mismas 4 magnitudes (Dice y cambio de volumen de hueso y metal) en dos cohortes. | Sev media | Conf alta | **FUSIONAR** las dos tablas (grupos de filas: sintesis / reconstruccion) y dejar 3 frases de lectura. | -124

**B2-035** | c4:198 | "270.9 HU… 2312.5… 198.0… 0.717… 0.928… 6.3… 199.8… 0.753… 9.0" | Idem: prosa = tabla. Dejar solo la lectura (sin umbral de comparacion; M se mide contra una TC real cuya reconstruccion se desconoce). | Sev media | Conf alta | **COMPRIMIR** | -85

## 3. Presupuesto de palabras por seccion (actual -> propuesto)

| Unidad | Actual | Propuesto | Funcion que justifica el tamaño |
|---|---|---|---|
| c3:367-411 Metricas y su inversion | 1 292 | 730 | Definir lo medido; eta2_exc exploratorio con controles; resultados se mudan |
| c3:412-425 Sintesis sobre pelvis sin metal | 928 | 575 | Definir cohorte, regiones, guarda, pose |
| c3:426-433 Reconstruccion real | 563 | 350 | Cohorte y umbrales; inversion de lectura |
| c3:434-441 Criterio primario y contrastes | 360 | 220 | Declarar primario y orden de contrastes |
| c3:442-489 Brazos de comparacion | 2 063 | 1 535 | Receta reproducible de baselines y protocolo fisico |
| c3:490-525 Analisis estadistico | 2 059 | 1 220 | Tests, margen, reglas de lectura (+120 a anexo) |
| c3:546-565 Resumen del diseno | 394 | 295 | Sintesis G-C5 (tabla) |
| **Subtotal cap3** | **7 659** | **4 925** | |
| c4:1-11 Introduccion | 105 | 55 | Orientacion |
| c4:12-46 Objetivo 1 | 740 | 575 | Datos primero (tabla) + 3 parrafos de lectura |
| c4:47-89 Objetivo 2 | 915 | 685 | Tabla de grados + estratificacion |
| c4:90-133 Contraste primario | 694 | 520 | Resultado confirmatorio y sensibilidades |
| c4:134-195 Analisis añadidos | 1 451 | 1 000 (+230 de B2-005) | Datos descriptivos; 3 tablas/figs |
| c4:196-223 Reconstruccion real | 326 | 240 | Descriptivo, sin umbral |
| c4:234-247 Discusion compuerta/muestreador/Obj4 | 569 | 385 | P-RE3: lectura por objetivo |
| **Subtotal cap4** | **4 800** | **3 690** (incluye +230 reubicados) | |
| **Total en alcance** | **12 459** | **8 615** (+120 a anexo) | |

## 4. Estimacion de reduccion

- **Palabras**: bruto en alcance ≈ -4 080 (cap3 -2 734; cap4 -1 340). Neto del documento, descontando 230 palabras reubicadas al cap4 y 120 enviadas a anexos: **≈ -3 700 (6.4 % de ~58 000; 30 % del alcance)**. Banda: conservador ≈ -2 400 (solo hallazgos de Conf alta y Sev alta/media); agresivo ≈ -4 500 (si ademas se aceptan los recortes de B2-009, 013, 014, 020 mas fuertes).
- **Paginas** (estimacion, no compilada): supuesto 58 000/207 ≈ 280 palabras/pagina como promedio global (incluye tablas, ecuaciones, figuras, portadas) y ~350 en prosa densa. 3 700 palabras equivalen a ≈ 10.5-13 paginas; hay que restar ≈ 1.2-1.6 paginas de las figuras nuevas (flujo de cohorte, forest plot, perfil por anillos, anillo desenrollado) y las tablas nuevas compactas. **Neto ≈ -8 a -11 paginas (≈ 4-5 % de 207)**; conservador ≈ -5 a -7. Las tablas ocupan mas por palabra que la prosa, por lo que la perdida de tablas tiene mas efecto en paginas que en palabras.

## 5. NO TOCAR (rubrica y rigor)

- **Ecuaciones/definiciones**: `eq:w1`, `eq:brecha`, `eq:mae` (fuera de mi rango pero referenciadas), Δ = max(s_sem, r_rep) (c3:502), definicion de eta2_exc (K, anillos 1 mm de 2 a 10 mm, recorte [-500, 1300], 2 000 remuestreos, "no se calculan p", c3:379-381), limites de acuerdo ±1.96 DE, regla de equivalencia (IC 90 % dentro de [-Δ, +Δ]), el valor 2^-13.
- **Receta reproducible**: 5371 HU (1 781 741 voxeles, 14 182 parches, 39 casos); `4cf3544` y `4993e87`; `tab:desviaciones`; 900 columnas, 1 000 vistas, tres materiales, densidad (HU+1000)/1000; 2500 HU, 500 mm3, tope de 24 cortes, banda de 12 mm, guarda de 1 voxel, extremos de 8 mm; 5 semillas, replicas A/B, un corte de cada dos.
- **Reglas de fallo/decision escritas antes**: criterios de la sonda (±20 HU, 2 %, 3x ruido, 72 h) y sus salidas; regla del material (24 cascaras, desempate); Objetivo 2 sin regla de decision; "ningun analisis añadido puede elevar la categoria"; el control de cordura no cuenta a favor del sintetizador.
- **Rubrica**: `tab:diseno` (G-C5, G-C6), baselines y comparador mejor disponible (G-C9), analisis estadistico (G-C8); cap4: datos antes que interpretacion (G-C10), toda cifra con variabilidad o rango (G-C11: IC, minimos/maximos de `res-integridad` y `res-ea1`), casos negativos (P-RE2: compuerta negativa, 15 corredores estrechos, no concluyente), discusion por objetivo (P-RE3), trazabilidad (G-T4: no borrar de la prosa una cifra que no este en tabla sin moverla antes).
- **Tablas de datos de cap4**: `res-compuerta`, `res-sap`, `res-tost`, `res-anillos`, `res-integridad`, `res-ea1`. Se pueden fusionar o pasar a anexo, no perder valores.

## 6. Orden recomendado de ejecucion

1. Cap4: B2-026, 029, 030, 031, 032, 034, 035 (solo recortan prosa que repite tablas; riesgo bajo).
2. Fusionar la regla de desenlaces (B2-019) y la descripcion de analisis añadidos (B2-021).
3. Tablas de sonda y material (B2-016, 017) y flujo de cohortes (B2-007).
4. Reubicar eta2_exc (B2-005) y cronologia (B2-024); coordinar con quien revise Amenazas.
5. B2-022 (anexo de derivacion) y resto de COMPRIMIR.

Observacion fuera de alcance (no evaluada): c3:526-545 contiene ≈1 275 palabras con resultados cuantitativos (puntajes, fracciones) en el capitulo de metodologia; merece el mismo tratamiento de B2-005 en otra revision.

## Resumen

1. Alcance ≈12 460 palabras: ahorro neto estimado ≈3 700 (rango 2 400-4 500), ≈8-11 paginas netas (supuesto 280-350 palabras/pagina, tras sumar ≈1.2-1.6 paginas de figuras nuevas).
2. Mayor ahorro con menor riesgo: la prosa de cap4 que recita las tablas, y la triple definicion de los desenlaces y de los analisis añadidos entre cap1, cap3 y cap4; resultados de eta2_exc y de seleccion de material estan en el capitulo equivocado (cap3).
3. Conservar ecuaciones, receta reproducible, reglas de fallo y las tablas/ICs que exige la rubrica (G-C5, G-C10, G-C11, P-RE2, P-RE3); convertir sonda, material y analisis añadidos a tablas, y flujo de cohortes, forest plot y perfil por anillos a figuras.
