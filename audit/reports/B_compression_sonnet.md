# B — Revisión de compresión científica (Scientific Compression Editor externo)

Alcance leído: `introduccion.tex`, `capitulo1.tex`, `capitulo2.tex`, `capitulo3.tex` líneas 1-201 y 339-366, más `docs/RUBRICA.md`, `anexos.tex` y `inventory.md`. Fuera de alcance, sin juicio: sintetizador v2, protocolo de apariencia, Amenazas a la validez, capitulo4.

## 0. Método y supuestos

- **Conteos.** Para cap1-3 uso las cifras de `inventory.md`. Para la introducción uso mi propio conteo, que excluye ecuaciones, captions y comentarios. El margen de error es de ±3 %. Total en alcance: ≈26 100 palabras (intro 5 543; cap1 6 482; cap2 6 575; cap3 7 475). Es el 45 % de las ≈58 000 de la tesis. El 75 % restante de cap3 (≈22 000 palabras) queda fuera de este alcance. Es probablemente la mayor palanca de compresión, y este informe no la evalúa.
- **Palabras/página.** Uso dos referencias. La primera es el ratio global 58 000/207 ≈ 280 w/p, que ya incluye tablas, ecuaciones, bibliografía y espacios. La segunda es ≈330 w/p de prosa pura (`a4paper,12pt`, `\setstretch{1.5}` en `main.tex`; no verifiqué márgenes ni fuente). Descuento ≈3 páginas por las figuras nuevas propuestas (≈8 × 0,4 pág.).
- **Restricciones de la RUBRICA que limitan la compresión.** G-A3 y G-B10: la brecha debe aparecer en la intro y coincidir con la de cap2. G-A10: la intro debe anticipar la contribución y los límites deliberados. G-A8: cada objetivo debe poder fallar. G-B3: el marco teórico debe ser autocontenido. P-EA2: se analizan los resultados de los autores. P-EA3: cap2 cierra con el aporte. P-MM3: la metodología es reproducible. Cada hallazgo respeta estas restricciones. Cuando dos copias duplicadas están obligadas por la rúbrica, se comprime una y se conserva la otra.
- **Límite de la revisión.** No leí Amenazas ni cap4. Donde propongo REUBICAR hacia ellos, la confianza baja un nivel hasta verificar que el dato ya existe allí. La propia intro afirma que Amenazas «las discute en detalle» (l.92).

## 1. Hallazgos

Formato: Sev = severidad (A/M/B). Conf = confianza. El ahorro es neto del cuerpo principal, en palabras.

### 1.1 Introducción

| ID | Ubicación | Evidencia | Descripción | Sev/Conf | Acción | Ahorro |
|---|---|---|---|---|---|---|
| B-001 | introduccion.tex:46-56 (≈710 w) | «0.00 HU en dos de las tres»; «diferencia media fue de −301.0 HU» | Los resultados, la cronología de decisiones y los caveats del margen Δ viven dentro de «Objetivos». Repiten cap1:155, cap2:112-120, cap3:38-40 y cap4. Dejar solo qué objetivos tienen regla de fallo y cuándo se fijó (G-A8), ≈220 w. | A/A | REUBICAR a cap4 y registro (B-031) + COMPRIMIR | −490 |
| B-002 | :37-43 (648 w) | «es decir, su nivel en una escala ordinal de cuatro niveles»; «suma las diferencias absolutas» | Cada objetivo carga definiciones operativas (brecha, W1, referencia clínica, banda 12 mm, calibre 7.0/1 mm) ya presentes en cap1:109,149 y cap3:97,341-354. Un objetivo debería ser verbo + variable + criterio (≈95 w). | A/A | COMPRIMIR | −270 |
| B-003 | :13-15, 32 | «Los implantes de osteosíntesis son dispositivos…» | El objetivo general define tres conceptos (cap1 los define). El pipeline se narra en l.13, l.15, l.32 y cap3:15. | B/M | COMPRIMIR | −50 |
| B-004 | :92-106 (≈1 080 w) | «las limitaciones se resumen aquí… la Sección discute en detalle» | Resumen de Amenazas (4 896 w) con cifras duplicadas: 20/30 fracturas (≡cap3:66), 16 casos, 14/2 (≡cap3:117) y 11/34, 7/57 (≡cap3:64). G-A10 pide solo los límites deliberados. Dejar 5-6 limitaciones con puntero (≈330 w). Las limitaciones de resultado van a Amenazas y a conclusiones (G-D3). | A/M | COMPRIMIR / TRASLADAR | −750 |
| B-005 | :76-90 | «222~mm² … 346» (≡cap2:74, cap3:200); «14 de los 75» (≡:7, :60, :82); «cerca del 95 %» (≡cap3:190) | Datos repetidos 3-4 veces en la misma intro y entre capítulos. Dejar la primera aparición con valor y referenciar el resto. Es obligatorio conservar supuestos y out-of-scope (G-A10). | M/A | FUSIONAR | −200 |
| B-006 | :58-72 (1 012 w) | «ninguno de los tres enfoques revisados» (≡cap2:116); «no puede ocupar el lugar del sintetizador» (≡cap2:118); tres elementos (≡cap2:122) | Casi verbatim entre intro y cap2. Mantener la brecha aquí (G-A3). La contribución solo se anticipa en ≈100 w (G-A10) y se desarrolla en cap2 (P-EA3). | A/A | FUSIONAR / COMPRIMIR | −330 |
| B-007 | :3-11 | l.5 y l.9: endurecimiento del haz, LDM y ControlNet explicados | Texto de contexto que cap1:37 y cap1:119-139 desarrollan. Mantener una frase por concepto con cita. | B/M | COMPRIMIR | −150 |

### 1.2 Capítulo 1 (marco teórico)

| ID | Ubicación | Evidencia | Descripción | Sev/Conf | Acción | Ahorro |
|---|---|---|---|---|---|---|
| B-008 | cap1:13 y fig. 15-27 | «Las secciones van de la física… al modelo generativo» | l.13 (144 w) parafrasea la columna derecha de `fig:mt-conceptos`. La figura es una tabla de `\fbox`, no un diagrama. Reducir l.13 a 2 frases. Redibujar la figura como TikZ con flechas (cumple P-MT2). | B/A | COMPRIMIR + figura | −90 |
| B-009 | cap1:47, 49 | «mediana de la fracción… fue 0.42» (≡cap3:103); «recorte por defecto… 6 mm» (≡cap3:105) | Dato de resultado y detalle de TotalSegmentator en el marco teórico, duplicado verbatim en cap3. Los umbrales 150/2500 HU aparecen además en cap3:48, 76, 91. | A/A | ELIMINAR en cap1 (queda en cap3) | −130 |
| B-010 | cap1:31-45 (≈640 w) | «Para cada medición podemos imaginar una línea…»; «no es un objeto adicional» | Explicación extensa de rayo, sinograma y modelo CatSim (l.41, 155 w). CatSim solo sustenta una comparación, no es concepto central. El endurecimiento se define en l.37 y de nuevo en l.79. **Figura F1** (SVG/TikZ): fuente–objeto–detector, un rayo con N_in/N_d, tabla de ángulos × detector con traza sinusoidal, y dos cajas «dominio de proyección → FBP → dominio de imagen». Reduce l.39, 41, 43, 45 a ≈60 % y fusiona l.37 con l.79. | M/M | COMPRIMIR + figura | −220 |
| B-011 | cap1:58-69 (≈450 w) | «tres codificaciones… 20 000 HU… arcoseno hiperbólico» (≡cap3:85 casi verbatim; ≡intro:48; ≡cap2:92) | Diseño de las codificaciones y la Ec. asinh en el marco teórico, replicado en cap3 §obj1. Dejar en cap1 solo el concepto de ventana y multiventana (G-B3). Mover la Ec. asinh y las 3 codificaciones a cap3 como **tabla única** (canal 1-3, techo, orden de prioridad) y quitar l.85. Cuidado con G-T3 (notación). | A/A | REUBICAR + FUSIONAR | −350 (+70 en cap3) |
| B-012 | cap1:71 (160 w) | «Una regla preinscrita debía… Esa regla no se aplicó»; «se añadió después de conocer el resultado» | Historia procedimental en un marco teórico. Dejar 2 frases. El detalle va al registro (B-031) o a Amenazas. | M/M | COMPRIMIR / REUBICAR | −120 |
| B-013 | cap1:77-85 (≈600 w) | «Selles et al. nombran… De Man et al. aíslan… Glover y Pelc derivan…» | Los mecanismos se comparan fuente por fuente en prosa, y l.79 repite el endurecimiento de l.37. **Tabla T1**: mecanismo × fuente × forma de raya × ¿exige dominio de proyección? Sustituye ≈350 w por ≈130 w más la tabla. | M/M | COMPRIMIR + tabla | −220 |
| B-014 | cap1:95-107 | «Estas definiciones… no describen la cuenta de corticales»; «equipo que rota 190°» | **Figura F2** (TikZ, cortes axial y coronal a nivel S1): ilion, ala sacra, cortical, foramen, canal, SI joint; tornillo iliosacro (a S1, 3 corticales) frente a transiliosacro (cruza ambas SI); zona segura (conos) y corredor óseo con el umbral 10 mm. Sustituye ≈200 w de descripción anatómica. Cortar detalles sin función: l.97 final, l.101 («190°»). | M/M | COMPRIMIR + figura | −250 |
| B-015 | cap1:99, 105, 107 ≡ cap3:101, 113, 131 | «justifican su corredor de 10 mm como holgura de 1 a 2 mm» (3×); «reformatean el volumen a lo largo del eje sacro» (2×); «va de la cortical lateral… ilion contralateral» (verbatim cap1:99 ≡ cap3:131) | Umbral 10 mm, marco de Kaiser y definición del transiliosacro están triplicados. Conservar el concepto en cap1. En cap3 dejar solo la operacionalización (h radial, ε por lado). | A/A | FUSIONAR | −310 (cap1 −60, cap3 −250) |
| B-016 | cap1:109-113 ≡ cap2:78 ≡ cap3:343, 348 | «pasa del grado angular 0 al 2 sin definir un grado 1» (cap1:111 y cap3:343); «equiespaciados» (cap1:113, cap1:149, cap3:354, intro:90) | La escala de Smith y sus límites se explican 3-4 veces. Definir una vez (cap1:109). **Figura F3** (TikZ): cilindro de calibre 7.0 mm, envolvente ósea, `dist(·)`, tramo T con 8 mm excluidos por extremo y bandas de grado 0/1/2/3 en mm. Sustituye el texto de límites de cap3:348. | M/A | FUSIONAR + figura | −190 (cap1 −70, cap2 −60, cap3 −60) |
| B-017 | cap1:115 ≡ cap2:80 ≡ cap3:198, 341 | «la densidad ósea no forma parte de él» (4×); Arand: «valores del ala sacra más bajos» (3×) | Mantener la decisión en cap3:198, una frase de literatura en cap2 y eliminar cap1. | A/A | ELIMINAR / FUSIONAR | −172 (cap1 −92, cap2 −80) |
| B-018 | cap1:119-143 | «Dorjsembe resumen…»; l.139 ≡ cap2:94 ≡ cap3:91; l.141 ≡ cap2:28 | Teoría DDPM con cadenas de atribución («Zhang et al. y Dorjsembe… escriben»). l.141 compara con Lugmayr/LeFusion, lo que viola el alcance declarado en l.11 y duplica cap2:28. El argumento «cuello de botella del autoencoder» está en 3 sitios. **Figura F4** (block diagram): tres cortes + máscara + región G borrada → U-Net con pasos de ruido → corte central → copia fuera de G. Sustituye ≈150 w de l.137, 141, 143. | M/M | COMPRIMIR + figura | −200 |
| B-019 | cap1:147-157 | «Los nombres de los tres desenlaces son de este trabajo… Walker… Lakens» | l.157 (75 w) discute taxonomías de terceros. l.155 repite lo que la intro cuenta en :52. **Figura F5** (forest-style): tres IC 90 % frente a [−Δ,+Δ] → equivalencia / no equivalencia / no concluyente. Sustituye ≈100 w. | B/M | COMPRIMIR + figura | −140 |
| B-020 | cap1:163 (171 w) | «El programa con que se calcularon originalmente los valores p no consta»; «scipy 1.15.3» | Procedencia de software y versiones, no concepto estadístico. Dejar la definición (≈50 w) y mover la procedencia a un anexo (conserva la reproducibilidad). | M/A | TRASLADAR A ANEXOS | −120 (+120 anexo) |
| B-021 | cap1:165-171 | «se fijó conociendo un resultado exploratorio desfavorable» (≡intro:50, cap3:74); MAISI (≡cap3:93); RMSE ≥ MAE (≡cap3:83, cap2:96) | Preinscripción, multiplicidad y MAISI repiten cap3. Dejar la lógica en ≈100 w. Mover la nota MAE/RMSE a cap3:83. | M/A | FUSIONAR / ELIMINAR | −220 |

### 1.3 Capítulo 2 (estado del arte)

| ID | Ubicación | Evidencia | Descripción | Sev/Conf | Acción | Ahorro |
|---|---|---|---|---|---|---|
| B-022 | cap2:8-12 | «Las secciones van de los trabajos que generan imagen…» | La hoja de ruta (121 w) y la metodología de revisión (117 w) son largas. Mantener la declaración de que la revisión es narrativa sin protocolo (G-B6). | B/M | COMPRIMIR | −110 |
| B-023 | cap2:18-24, 36-42, 56 ≡ anexos tabla | «sube en hígado de 62.5 a 66.5 %»; «58.89 a 63.53»; «78.46 a 84.56» | Cifras de Dice/SSIM/RMSE en la prosa y de nuevo en la columna «Resultado» de `tab:comparacion`. P-EA2 exige analizar resultados, no repetirlos. Dejar 1 resultado clave por fuente y el resto en la tabla. | M/A | COMPRIMIR | −240 |
| B-024 | cap2:46 ≡ cap2:76 ≡ intro:62 | «los colocan al azar, con una regla geométrica sobre la anatomía o a mano» (2× verbatim); «meaningful locations» (3×) | Misma síntesis dos veces en el mismo capítulo. | M/A | FUSIONAR | −110 |
| B-025 | cap2:44, 48, 114 | «validación… en dos dimensiones», 3× en cap2 más intro:68, 84, 102 | Los límites de validación de Peters/XCIST se repiten en 6 sitios. Canónico: cap2:44. | B/A | FUSIONAR | −70 |
| B-026 | cap2:54, 60, 64-70 | «solo se dispuso del resumen»; Zwingmann 2013 y 2010 «81, 11, 3 y 5 %» | Fuentes que el propio texto declara fuera de la referencia clínica o con solo resumen ocupan ≈450 w. Dejar 1-2 frases y los números secundarios en una nota o anexo. Las frases finales de l.70 («SAP califica con grado 3») son diseño y ya están en cap3:350. | M/M | COMPRIMIR | −300 |
| B-027 | cap2:96 ≡ cap3:83 | «RMSE de 12.3… 20.2… 12.74» | Mismos números y misma lógica en dos capítulos. Los números van en cap3 (diseño del criterio). Cap2 conserva el dato como brecha de la literatura. | A/A | FUSIONAR | −100 |
| B-028 | cap2:88, 94, 98, 104, 106 | «26.76 dB… 0.9501… 32.67 dB»; «2.0, 2.6, 1.6 y 2.0 mm»; «7.57… 11.45… 54.82» | Cifras puntuales en prosa densa. **Tabla T2** (fuente × método × punto de medida × material × valor × n) para Radzi/Cassanego. Quitar PSNR/SSIM secundarios. La última frase de l.104 cita un resultado de v2 (fuera de alcance): REUBICAR. | M/M | COMPRIMIR + tabla | −335 |
| B-029 | cap2:110-120 (≈595 w) | «La Tabla… compara diez de los trabajos…»; l.118-120 «el desenlace fue no concluyente» | l.110 describe columnas ya rotuladas. l.116 ≡ intro:62. l.118-120 reportan la ejecución y el resultado del Obj. 3 en un capítulo de revisión. Dejar una frase de brecha idéntica a la intro (G-B10) y los resultados en cap4. | A/A | ELIMINAR / REUBICAR | −325 |
| B-030 | cap2:122-128 | «combinación de tres elementos que las fuentes revisadas no reúnen»; Xie (≡intro:70) | P-EA3 exige conservar el aporte, pero cap2:122 ≡ intro:70-72 y l.128 ≡ intro:15, 100. Mantener cap2 como lugar del aporte y quitar el solape. | M/M | COMPRIMIR | −170 |

### 1.4 Capítulo 3 (líneas 1-201 y 339-366)

| ID | Ubicación | Evidencia | Descripción | Sev/Conf | Acción | Ahorro |
|---|---|---|---|---|---|---|
| B-031 | cap3:38-40 (327 w) | «se fijó el 9 de octubre… enmendó el 11… 12… 15» | Cronología narrada. Fechas y «se fijó después de ver» están dispersas (cap1:71,153,165,169; cap3:74,89,115,117,151; intro:50-56). **Figura F6** (timeline TikZ): 22 sep (preinscripción muestreador), 9 oct (diseño Obj.3 congelado), 11 oct (enmienda 1 + recuento), 12 oct (enmienda 2), 15 oct (lectura de desenlaces y análisis añadidos), v2 posterior. Más un **registro de decisiones** (fecha / decisión / antes-después de ver datos / sección) en anexo. Valida las fechas contra el diseño congelado. | M/M | REUBICAR + figura | −220 (+120 anexo) |
| B-032 | cap3:13, 15, 36 | «El Objetivo 3 diseña el sintetizador…»; l.36 «no está verificado que esas máscaras estén disponibles localmente» (≡intro:82) | Los 4 objetivos se reenuncian por tercera vez. Hay overlap entre l.15 y el texto de `fig:pipeline`. l.36 duplica el out-of-scope de la intro. | M/A | COMPRIMIR / FUSIONAR | −165 |
| B-033 | cap3:50-62 (≈730 w) | «178 volúmenes en 168 pacientes… 179 unidades… 166 volúmenes… 159 pacientes» | La cohorte se cuenta como historia de auditorías. **Figura F7** (flowchart): 178 vol → 168 pac → 159 pac (118 train/125 vol, 8 val, 33 test). Más una **tabla** grupo × partición (la suma 59+41+66=166 cuadra). Mover la mecánica de las auditorías a un anexo breve. Aclarar «179 unidades» frente a «178 volúmenes». | M/M | COMPRIMIR + figura + tabla | −330 |
| B-034 | cap3:64-70 | «fractura confirmada en 20 de los 30» (≡intro:92); «18 casos sobre láminas… 12 sobre el volumen» | El embudo 103→91→72→49 (la resta 91−72=19=11+7+1 cuadra) es un flowchart. El cribado de fractura se repite en la intro. Dejar el resultado una vez y mover el detalle de lector/láminas a anexo. | M/M | COMPRIMIR + figura | −170 (+80 anexo) |
| B-035 | cap3:74-93 | l.87: «AdamW… 10⁻⁴… 500 pasos… lotes de 4… 30 000 pasos»; l.93 ≡ cap1:167; l.74 ≡ intro:46, cap1:139 | Hiperparámetros: reproducibles pero mejor en tabla de anexo. Quitar duplicados de l.74 y l.93. l.83 absorbe los RMSE de B-027. | A/A | TRASLADAR A ANEXOS + FUSIONAR | −170 neto |
| B-036 | cap3:95-97 | «Ziran… 7 a 25 %… hasta 140 %» (≡cap2:74) | Párrafo introductorio que reexpone la motivación de cap2. | B/M | COMPRIMIR | −60 |
| B-037 | cap3:103-117 | l.107 «La decisión que la definía con ese relleno se corrigió»; l.115 «mediana de 9.5 mm… 65.3 %»; l.117 ≡ intro:94 | Resultados (diámetros, % viables) y historia de correcciones dentro de la metodología. La búsqueda de l.109 (rejilla 3 mm, 9×9 = 81 direcciones) es reproducible y se queda. Ahí cabe la **Figura F8** (TikZ): rejilla sagital con abanico de direcciones y criterios de salida. Los resultados van a cap4 (verificar) como tabla 2×2 recorte × (d, ε). | M/M | REUBICAR + COMPRIMIR | −250 |
| B-038 | cap3:121-127 | «percentil 99.9… percentil 0.1… 100 mm de ancho durante 10 mm» | Reglas de localización como **tabla** (referencia / regla / rango). l.123 gasta ≈40 w en reconciliar «66 vs 69» pacientes. l.125 y l.127 son resultados y acuerdos de lector que van a anexo. | M/M | COMPRIMIR + tabla | −170 |
| B-039 | cap3:131-155 | Tabla geom., fila 2: «Cilindro de 4.91 mm con una cabeza de 8.0…»; l.151 «La decisión anterior… fijaba un cilindro uniforme» | La fila 2 repite l.149-151. l.151 es historia de decisión (→ registro B-031). **Figura F9** (dibujo técnico): cuerpo 4.91 mm, cabeza 8.0 × 4.5 mm, calibre de medición 7.0 mm y nominal 6.5-8.0 mm, 8 mm excluidos por extremo. Resumen de fabricantes (l.155) a ≈70 w. | M/M | COMPRIMIR + figura | −164 |
| B-040 | cap3:159-200 | «se justifica por su consecuencia» (≡intro:90); l.196 ≡ intro:78 y cap2:70; l.200 ≡ intro:85, cap2:74 | l.159 ≡ cap1:165. l.200 (fenotipos) se repite 3×. l.194 (3 comprobaciones) solapa con los 6 controles de l.352. **Figura F10** (TikZ+plot): eje u, c, perturbación ρ y α, margen h, y densidad seminormal con 2σ=h (95 %). | M/A | COMPRIMIR + figura | −310 |
| B-041 | cap3:341-365 | l.341 ≡ intro:43; l.354 + l.361: «0.29, 0.07 y 0.035… 0.395» | SAP repetido desde la intro. **Tabla T3**: grado × (navegada, convencional, F_P, F_Q, |ΔF|); permite ver 0.29+0.07+0.035=0.395 de un vistazo (verificado con los porcentajes del texto). l.350 y l.363-365 pueden ceñirse. | M/M | COMPRIMIR + tabla | −233 |

### 1.5 Elementos a CONSERVAR (hallazgos de no intervención)

| ID | Ubicación | Descripción | Acción |
|---|---|---|---|
| B-042 | cap3:109, 111; Tabla `tab:preinscripcion`; Ec. `eq:pose`, `eq:brecha`, `eq:w1`, `eq:mae` | Parámetros de búsqueda, semilla, σ_t, σ_a, truncamiento, 50 poses y la definición de brecha son la receta reproducible (P-MM3). | CONSERVAR |
| B-043 | cap2:12 y tabla comparativa de `anexos.tex` | La declaración de revisión narrativa y la tabla con «este trabajo» como fila cumplen G-B6/G-B8. La tabla se mantiene. Solo se comprime el texto que la duplica. | CONSERVAR |
| B-044 | intro:50-52 (regla fijada antes de procesar la prueba), cap3:74, 159 | La declaración de qué se fijó antes de ver datos es lo que hace verificable el trabajo (G-A8, G-T4). Se reduce el volumen, no el contenido. | CONSERVAR |

## 2. Figuras y tablas propuestas

Ninguna requiere datos nuevos. Todas salen de lo ya escrito.

| Fig/Tab | Tipo | Contenido | Hallazgo |
|---|---|---|---|
| F1 | TikZ/SVG | Geometría de adquisición, sinograma sinusoidal y dominios proyección/imagen | B-010 |
| F2 | TikZ | Cortes axial/coronal en S1 con iliosacro vs transiliosacro, zona segura y corredor | B-014 |
| F3 | TikZ | Brecha b, envolvente, tramo T, 8 mm excluidos y bandas de grado | B-016 |
| F4 | Block diagram | Entradas del sintetizador 2.5D, U-Net y copia fuera de G | B-018 |
| F5 | Forest-style | Tres desenlaces de equivalencia frente a [−Δ,+Δ] | B-019 |
| F6 | Timeline | Congelamientos y enmiendas del 22 sep al 15 oct | B-031 |
| F7 | Flowchart | Flujo de pacientes 178→168→159 y embudo 103→91→72→49 | B-033, B-034 |
| F8 | TikZ | Búsqueda del corredor: rejilla sagital y 81 direcciones | B-037 |
| F9 | Dibujo técnico | Geometría del tornillo y calibres | B-039 |
| F10 | TikZ + plot | Perturbación de pose y densidad seminormal | B-040 |
| T1-T3, T4 | Tablas | T1 mecanismos de artefacto; T2 distancias de artefacto; T3 distribuciones de Zwingmann; T4 codificaciones (B-011/B-035) | B-013, B-028, B-041, B-011 |

## 3. Presupuesto de palabras por sección

El presupuesto está justificado por la función de cada unidad, no por un porcentaje. Los números salen de restar los ahorros de los hallazgos asignados a cada sección. Las columnas son actual → propuesto.

| Unidad | Función que debe cumplir | Actual | Propuesto | Hallazgos |
|---|---|---|---|---|
| Intro: apertura (l.3-17) | Dominio, problema y hoja de ruta | 795 | 645 | B-007 |
| Intro: formulación y objetivo general | Pregunta y propósito | 236 | 186 | B-003 |
| Intro: objetivos específicos y reglas | Objetivos falsables, sin resultados | 1 362 | 602 | B-001, B-002 |
| Intro: justificación | Brecha (G-A3) y contribución anticipada | 1 012 | 682 | B-006 |
| Intro: alcance y limitaciones | Supuestos, out-of-scope y límites deliberados | 2 138 | 1 188 | B-004, B-005 |
| **Introducción** | | **5 543** | **3 303** | −2 240 |
| Cap1: apertura y figura | Mapa conceptos → objetivos | 352 | 262 | B-008 |
| Cap1: TC y HU | Autocontención física mínima | 1 478 | 658 | B-009 a B-012 |
| Cap1: artefactos | Mecanismos y por qué exceden la máscara | 988 | 768 | B-013 |
| Cap1: fijación iliosacra | Vocabulario quirúrgico y escala | 1 314 | 842 | B-014 a B-017 |
| Cap1: difusión | DDPM, condicionamiento, inpainting, 2.5D | 1 004 | 804 | B-018 |
| Cap1: estadística | W1, equivalencia, bootstrap | 1 346 | 866 | B-019 a B-021 |
| **Capítulo 1** | | **6 482** | **4 200** | −2 282 |
| Cap2: apertura | Criterio de revisión | 280 | 170 | B-022 |
| Cap2: lesiones | Qué pasa fuera de la máscara | 962 | 852 | B-023 |
| Cap2: simulación | Inserción y protocolo físico | 1 150 | 1 000 | B-023, B-024, B-025 |
| Cap2: colocación | Dónde va el tornillo y qué se mide | 1 648 | 1 088 | B-016, B-017, B-023, B-024, B-026 |
| Cap2: representación | Ventanas, autoencoder, extensión del artefacto | 1 480 | 1 045 | B-027, B-028 |
| Cap2: comparación y brecha | Brecha idéntica a la intro y aporte (P-EA3) | 1 055 | 520 | B-025, B-029, B-030 |
| **Capítulo 2** | | **6 575** | **4 675** | −1 900 |
| Cap3: apertura y visión general | Pipeline y estado de ejecución | 845 | 460 | B-031, B-032 |
| Cap3: datos | Cohorte, partición y aislamiento | 1 435 | 935 | B-033, B-034 |
| Cap3: compuerta (Obj.1) | Regla, criterio y ajuste reproducibles | 924 | 754 | B-035, B-011 |
| Cap3: muestreador (apertura) | Motivación | 137 | 77 | B-036 |
| Cap3: corredor | Medición reproducible | 1 032 | 602 | B-015, B-037 |
| Cap3: marco en volúmenes con metal | Aplicabilidad del marco | 551 | 381 | B-038 |
| Cap3: geometría | Geometrías y su respaldo | 752 | 518 | B-015, B-039 |
| Cap3: poses preinscritas | Receta del muestreo | 935 | 625 | B-040 |
| Cap3: SAP | Métrica y comparación con la referencia | 864 | 571 | B-016, B-041 |
| **Capítulo 3 (en alcance)** | | **7 475** | **4 923** | −2 552 |
| **TOTAL en alcance** | | **26 075** | **17 101** | **−8 974** |

## 4. Potencial de reducción

El ahorro bruto del cuerpo principal es ≈8 970 palabras (34 % del alcance, 15 % de la tesis). Hay que descontar ≈380 palabras que aterrizan en anexos (Fisher, registro, cribado, hiperparámetros) y ≈300 de captions de las figuras nuevas.

| Escenario | Criterio | Palabras (neto) | Páginas (neto) |
|---|---|---|---|
| Conservador | Solo hallazgos con confianza alta (B-001, 002, 005, 006, 008, 009, 011, 015-017, 020, 021, 023-025, 027, 029, 032, 035, 040) | ≈4 400 | 10-13 |
| Esperado | Alta + mitad de confianza media | ≈6 200 | 16-19 |
| Máximo | Todo lo propuesto | ≈8 300 | 22-27 |

**Supuesto de páginas.** Páginas = palabras ÷ (330 prosa pura o 280 ratio global) − ≈3 páginas de figuras añadidas. Es una estimación: sin compilar el PDF no se conoce el efecto real de los flotantes. El escenario esperado equivale a ≈8-9 % de las 207 páginas. Casi todo el ahorro es duplicación (verbatim entre intro, cap1, cap2 y cap3), no contenido único.

## 5. NO TOCAR

- Ecuaciones y definiciones `eq:ventana`, `eq:asinh` (solo se mueve), `eq:mae`, `eq:pose`, `eq:brecha`, `eq:w1`, y la Tabla `tab:preinscripcion` (parámetros, semilla, 50 poses).
- Parámetros de búsqueda del corredor (cap3:109, 111), regla de longitud útil, 8 mm de exclusión, calibres 7.0 mm, ε = 1 mm y d.
- Reglas de fallo y qué se fijó antes de ver los datos (intro:50-52; cap3:74, 89, 159). Solo cambia su ubicación o volumen, no su contenido (G-A8).
- Definición de las 3 codificaciones y el orden fijado a priori para elegir (cap3:85, 89), y los criterios de selección de la cohorte y la regla de aislamiento (cap3:44-52).
- La brecha de la intro (G-A3) y la tabla comparativa con «este trabajo» como fila (G-B8); la declaración de revisión narrativa (G-B6).
- Los supuestos y convenciones declarados, y la distinción confirmatorio vs descriptivo (G-A10, G-C8).
- Las citas con cifra de fuente. Antes de borrar una cifra secundaria hay que confirmar que sigue en la tabla del anexo.

## 6. Riesgos y observaciones

1. Varias reubicaciones (B-001, B-004, B-029, B-037) suponen que cap4 o Amenazas ya contienen el dato. Verificarlo antes de borrar.
2. Posibles inconsistencias de lectura: «179 unidades» frente a 178 volúmenes (cap3:50); «64 pacientes» (cap3:125) frente a los conteos finales; 66 vs 69 pacientes de calibración (cap3:123). Un flowchart y una tabla las harían visibles o las resolverían.
3. Los comentarios de `.tex` con rutas internas (`redaccion/rondas/...`) no se renderizan. No ahorran palabras, pero conviene limpiarlos antes de entregar.

## Resumen

1. La mayor parte del ahorro es duplicación real (intro ↔ cap2 ↔ cap3, p. ej. brecha, contribución, 10 mm, escala de Smith, codificaciones), y el resto es historia procedimental y resultados colocados en capítulos conceptuales.
2. Potencial: ≈4 400 (conservador), ≈6 200 (esperado) o ≈8 300 palabras (máximo), equivalentes a 10-13, 16-19 o 22-27 páginas (330/280 w/p, −3 pp de figuras).
3. Palancas principales: intro (−2 240, sobre todo objetivos y limitaciones), cap1 TC y estadística, cap2 comparación y colocación, y cap3 datos/poses con 10 figuras y 4 tablas. No tocar ecuaciones, la receta de búsqueda y preinscripción, ni las reglas de fallo.
