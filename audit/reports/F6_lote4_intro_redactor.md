# F6 Lote 4: introduccion.tex (B-001, B-002, B-005, B-006)

Archivo editado: `overleaf/secciones/introduccion.tex` (solo ese; sigue en LF, 0 CR; 106 -> 94 lineas). Copia original en el scratchpad de la sesion: `.../scratchpad/introduccion_orig.tex`. Lint `--compilar`: compila (205 paginas), 0 altas; quedan 1 media (E-O1, l.7, oracion de 41 palabras) y 1 baja (E-P4 "robustos", l.7). Ambas estan en el parrafo 3 de la apertura, que no se toco en este lote (ya existian antes).

## (a) Estado por hallazgo

| Hallazgo | Estado | Detalle |
|---|---|---|
| B-001 (resultados y cronologia dentro de Objetivos, l.46-56) | Aplicado | Los 6 parrafos (l.46-56) pasan a 2: (1) quien tiene regla de fallo y cuando se fijo (Obj 1: regla despues de la exploracion con prueba, criterio de 25 HU anterior y sin moverse; Obj 2 sin regla; Obj 4 con controles de implementacion), (2) regla del Obj 3 (fijada antes de procesar prueba, comparacion que decide, IC 90 % dentro de [-D, +D], tres desenlaces, lectura en dos niveles fijada despues de ver la prueba de las dos versiones, control de cordura y version 2 no deciden). Fuera: veredicto y cifras de la compuerta, cronologia del rediseno, 0.00/21.80 HU, D = 196.3 HU y sus caveats, -301.0 HU con su IC, version 2. G-A8 intacto. |
| B-002 (objetivos especificos) | Aplicado | Cada objetivo queda como verbo + variable + criterio: 101->86, 155->83, 215->140, 160->138 palabras. Fuera: definicion de autoencoder-como-red-larga, corredor viable (calibre + holgura), escala ordinal de cuatro niveles, W1 como suma de diferencias, bandas pensadas para streaking, definicion de inpainting y de 2.5D, contraste de realismo "mediante estadisticos...". Se conservan numeracion, orden y estatus (compuerta Go/No-Go; contraste de realismo "diseñado y no ejecutado"; reconstruccion real "descriptiva"; "Ningun objetivo evalua esa adopcion"). |
| B-005 (datos repetidos, l.76-90) | Parcial | Hecho: "14 de los 75" queda solo en l.7 (se quitan la justificacion y la viñeta de segmentacion, que apunta "los 14 indicados al inicio"); 222/346 mm2 fuera (queda "menor en sacros dismorficos que en normales" + puntero al estado del arte); "unos 12 mm" queda solo en el Obj 3 (l.41), en l.78 (nuevo) "el ancho de B_delta"; "cerca del 95 %" fuera (queda "se cuantifica en la Seccion poses"); l.76 (nuevo) "(veanse los objetivos)" reapuntado a "capitulo de resultados". No aplicado: 178/1 184 se deja en l.64 (es el alcance de la cohorte; 1 184 aparece 2 veces, cambio sin ganancia). |
| B-006 (justificacion) | Aplicado | 999 -> 728 palabras (~-270; B-006 pedia -330). Se mantiene la BRECHA (G-A3) con su texto completo, el motivo de que el muestreador reproduzca una distribucion, y la contribucion en tres elementos. Fuera: detalle "meaningful locations", causas de las rayas de De Man, "el protocolo no puede ocupar el lugar del sintetizador" (cap2:118), "el sintetizador opera sobre TC reconstruida", desplazamiento de dominio de las mascaras umbralizadas, "no hay precedente de una banda con valor numerico", "esas ventanas se emplean como codificacion de entrada". |
| A-005, A-006, A-007 | Respaldo de lo anterior | A-007 solo en la parte B-005 (datos repetidos). El desglose de exclusiones en tabla y el traslado de limitaciones (l.92-106) es B-004, no se toco. |

Palabras de parrafos editados (antes -> despues): objetivos 101/155/215/160 -> 86/83/140/138; reglas y cronologia (l.46-56, 6 parrafos, 834 w) -> 2 parrafos, 355 w; justificacion (7 parrafos, 999 w) -> 5 parrafos, 728 w; viñeta segmentacion 81 -> 80; viñeta dismorfismo 108 -> 108; supuestos 150 -> 150; convenciones 148 -> 140. Ningun parrafo editado crece.

## (b) Palabras (texcount -brief -inc -q)

Antes: 5 600. Despues: 4 645. Ahorro: 955 palabras (el inventario B-001+002+005+006 suponia -1 290; la diferencia viene de conservar las reglas de fallo y la brecha completas y de no tocar B-003/004/007).

## (c) Cifras, resultados o decisiones quitadas y donde estan

| Quitado de la introduccion | Donde SI esta |
|---|---|
| Veredicto negativo; "ninguna de las seis combinaciones bajo de 25 HU" | capitulo4.tex:37, 236; conclusiones.tex:14 |
| Compuerta: 2 variantes x 3 codificaciones, 6 combinaciones | capitulo3.tex:107 |
| Extension al autoencoder de Guo et al. (entrenado con TC, saturacion al rango de salida) | capitulo3.tex:115; capitulo4.tex:45 |
| Ida y vuelta sin autoencoder: 0.00 HU en dos codificaciones, 21.80 HU en la tercera | capitulo4.tex:41 |
| El veredicto descarto la difusion latente y no la codificacion multiventana | capitulo4.tex:238 |
| Sintetizador adopta asinh en coma flotante de 32 bits | capitulo3.tex:226 |
| Rediseño del Obj 3 posterior al veredicto, sin tocar la regla (queda 1 oracion en intro) | capitulo3.tex:596; capitulo4.tex:238 |
| Regla del Obj 1 fijada tras exploracion con prueba; 25 HU anterior (se conserva en intro) | capitulo3.tex:596 |
| Obj 2 sin regla; escala = distancia entre series (0.395 grados) | capitulo3.tex:383 |
| Controles de implementacion de SAP (identidad, monotonia, resolucion) (se conservan en intro) | capitulo3.tex:359; capitulo4.tex:246; conclusiones.tex:22 |
| Delta = 196.3 HU; Delta = max(s_sem, r_rep); convencion; mide variabilidad propia; sintetizador mas variable da prueba mas facil | capitulo3.tex:524, 526, 528 |
| Las tres elecciones de validacion (punto de control, material, margen) acercan la prueba a equivalencia; piso de ruido | capitulo3.tex:620; capitulo4.tex:250 |
| Diferencia media -301.0 HU, IC -477.0 a -124.9 HU, desenlace no concluyente, amplitud menor | capitulo4.tex:94, 106, 128; capitulo3.tex:339 |
| Lectura en dos niveles, fijada tras ver la prueba de las dos versiones (se conserva en intro) | capitulo3.tex:522; capitulo4.tex:128, 250; conclusiones.tex:18 |
| Control de cordura no cuenta a favor; v2 posterior, exploratoria, tambien no concluyente | capitulo4.tex:132, 226; capitulo3.tex:38, 288; conclusiones.tex:20 |
| Obj 2: viabilidad del corredor = calibre + holgura (7.0 mm, 1 mm) | capitulo3.tex:135, 363 |
| Obj 2: escala ordinal de cuatro grados | capitulo3.tex:365; capitulo1.tex:109 |
| Obj 2: W1 como suma de diferencias entre acumuladas | capitulo1.tex:149 |
| Obj 3: contraste de realismo "mediante estadisticos..." | capitulo3.tex:462 |
| 222 vs 346 mm2 (Gardner et al.) | capitulo2.tex:74 |
| "Cerca del 95 %" de magnitudes seminormales dentro del margen | capitulo3.tex:212 |
| Protocolo: 14 000 casos, fractales, colocacion al azar, "meaningful locations" | capitulo2.tex:42, 46 |
| "El protocolo no puede ocupar el lugar del sintetizador" (proyecciones, 1 fila de detector) | capitulo2.tex:118 |
| Mascara umbralizada vs cilindro: desplazamiento de dominio | capitulo2.tex:124; capitulo3.tex:262 (sigue en la intro, l.94 del archivo nuevo) |
| Banda sin precedente con valor numerico; ventanas como codificacion de entrada | capitulo2.tex:106, 92 |
| Xie: en exceso (se conserva); fragmentacion local (se conserva) | capitulo2.tex:124; capitulo3.tex:92 |
| "14 de los 75", "1 109 / 14 / 61" (repeticion en justificacion) | se mantiene la primera aparicion, l.7 de la introduccion |

## (d) Lo que solo esta en la introduccion y se dejo

- Sin cambio y sin duplicado verificado: "14 de los 75" (l.7, primera aparicion); "unos 12 mm" (Obj 3); 178/1 184 y "69 de los 72" (alcance, l.64-66 del archivo nuevo); la distincion confirmatorio / descriptivo de la lectura de resultados; las viñetas de fuera de alcance (la de XCIST/CatSim con la cita de `wu2022xcist`).
- Detalle de las limitaciones, l.80-94 del archivo nuevo (limitaciones, supuestos, cribado de 30 casos, 16 casos, 11/34, 7/57, envolvente osea, desplazamientos de dominio): no se tocan, son del lote B-004.
- "Sin regla de decision del Obj 2" y el hecho de que la escala de lectura se eligio despues de conocer la distancia: esta en capitulo3.tex:383; lo agregue una vez en la introduccion (ver abajo, nota 1).

## (e) \cite y \ref que cambian

- \cite: `liu2021ctpelvic1k` 4 -> 3 (se quito la oracion de la justificacion que repetia 14/75/61); `peters2025hybrid` 5 -> 4 (oracion "el protocolo no puede ocupar el lugar del sintetizador"). Ninguna otra cita se pierde ni se agrega; las demas claves conservan su conteo.
- \ref (por clave): `sec:amenazas` 6 -> 5; `sec:obj1` 4 -> 2; `sec:sap` 3 -> 4 (se agrega 1 en el Obj 2 para su comparacion; se cuenta el que ya existia en l.43 y l.50); `sec:sintetizador` 7 -> 4. Las demas (cap:propuesta, ap-analisis 2, ap-realismo, ap-reconstruccion, ap-sintesis 2, apariencia, corredor, datos 2, ea-brecha, ea-simulacion, geometria 2, mt-iliosacra, poses, v2 3, tab:preinscripcion) no cambian. No quedan referencias huerfanas.

## Notas para la autora

1. Oracion agregada: "escala elegida despues de conocer la distancia del muestreador" (Obj 2). No es contenido nuevo: copia capitulo3.tex:383 y consigna que la escala de lectura es posterior al resultado. La cobertura original de l.50 solo decia "la lee contra la distancia entre las dos series". Si se prefiere no agregar, basta quitar esas ocho palabras.
2. Cabe señalar que la introduccion ya no anuncia el resultado del Obj 1 ni el del Obj 3; el unico rastro es en los supuestos: "su desenlace no concluyente no lo confirma ni lo refuta (capitulo de resultados)". Eso es parte de B-004 y se deja.
3. B-006 pedia ~-330 palabras; se logro ~-270. Mas recorte exigiria quitar la cadena MAR no pareada o las citas de difusion de lesiones, que sostienen la brecha (G-A3), y no se hizo.
4. Voz impersonal: en los parrafos editados no queda sujeto personal ("la autora", "este trabajo" como sujeto de un verbo de accion); "este trabajo" aparece solo como complemento ("motiva este trabajo", "una premisa de este trabajo", "convencion de este trabajo"). Fuera de los parrafos editados no se reescribio nada (en las secciones de limitaciones, l.80-94 nuevas, siguen oraciones con "La autora juzgo insuficiente..." y similares; son del lote B-004).
