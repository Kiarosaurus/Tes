# capitulo4 — r00 (modo redactar) — respuesta del redactor

Encargo: `redaccion/ENCARGO_2026-10-16.md` item 5. Esqueleto de 11 lineas -> capitulo completo. Sin reportes de
revision (r00): no hay hallazgos que decidir; este archivo deja la fuente de cada cifra (regla 5 de
`overleaf/CLAUDE.md`), los GAP y las notas para la autora y para r01.

## Estructura

Titulos del esqueleto conservados (4 `\section`). Anadidos: `\label{cap:resultados}`; en §Coherencia de apariencia,
cuatro `\subsection` (Contraste primario, Analisis anadidos, Reconstruccion de implantes reales, Version 2); en
§Discusion, cuatro `\subsection` (Compuerta, Muestreador y SAP, Sintetizador, Limitaciones). El Obj 4 no tiene
seccion propia (sus controles van con el Obj 2 y su lectura en la discusion), como en `tab:diseno` del cap. 3.
Tablas nuevas: `tab:res-compuerta`, `tab:res-sap`, `tab:res-tost`, `tab:res-anillos`, `tab:res-ea1`. Sin figuras.

## Fuente de cada cifra

| Cifra(s) en `capitulo4.tex` | Fuente |
|---|---|
| Obj 1: seis medias, IC95, medianas, 34/34, Bdelta (n = 21); 164.76 -> 61.72, 160.13 -> 72.91, 209.39 -> 77.03; subgrupos 53.72 / 46.99 / 76.03 (14, 6, 14) | `experiments/objetivo1/p1_compuerta.md` (veredicto; MAE ROI bdelta, `vae regla`; subgrupo `afinado pub+asinh`) |
| Ida y vuelta sin autoencoder: hueso 0.00 / 0.00 / 21.80; Bdelta 13.71 / 13.71 / 15.25; "cota inferior" | `p1_compuerta.md` (columna identidad regla); `objetivo1/EXPERIMENTOS.md` §1 ("sin VAE; cota inferior") |
| Sensibilidades 60.95 [54.28, 68.19] (n = 33), 61.08 [54.23, 68.57] (n = 32); "a lo sumo 2.3 HU" con 33 | `p1_sin_0053.md`, `p1_sin_0072.md`; 2.3 = formula de `capitulo3.tex`:54 (fuente: 2.25) |
| Guo et al.: rango -1000 a 1000 HU, 42.24 / 18.24 / 6.96-231.43 HU, 11 de 34 | implicancia #93 (CERRADA); `experiments/obsoletos/README.md`:34; ficha `guo2025maisi` (rango NO ENCONTRADO EN EL PDF) |
| Obj 2: 3 600 / 2 450 poses, 0 sin grado; pose sin perturbar con brecha nula a su diametro | `e13_sap.md`, `e13_sap_g3.md`; `tesis/main.tex` *Placement result* ("integrity checks pass") |
| Perturbacion aplicada 1.66 / 4.09 / 7.49 mm; 1.48 / 3.61 / 8.22 grados | `e13_sap.md` §Perturbacion |
| Distribuciones y W1 (7.0, 4.91, 7.3 mm; 72 y 49); estratos 57/15 y 41/8 | `e13_sap.md`, `e13_sap_g3.md`, `e13b_estratificado.md`; `tesis/main.tex` *Placement result* |
| Series de Zwingmann 69/15/8/8 (26 tornillos, 24 pac.), 40/37/11.5/11.5 (35, 32); 0.395 | `e13_sap.md` (referencias); `capitulo3.tex` §SAP (0.395, calculo propio) |
| IC95 [0.152, 0.313], [0.089, 0.364]; sin 0022/0024: 51.8/31.4/11.1/5.7, 0.203 / 0.237 | `e15_w1_sensibilidad.md` |
| Viabilidad 59.7 / 65.3 % de poses; 79.2 / 54.2 % (4.91 / 7.3 mm) | `e13_sap.md`, `e13_sap_g3.md` §Viabilidad (D >= d + 2) |
| TOST v1: -301.0 [-477.0, -124.9]; Fe -3814.2 [-4405.9, -3222.6]; sin angostos -261.1 [-479.8, -42.4]; estado final -384.0 [-566.5, -201.4]; Wilcoxon p = 0.000122 (los dos puntos de control) | `resultados_prueba_v1.md` (tabla E-A2 y Cordura); `outputs/obj3_pose/a24/run04_mejor/a24_contrastes.md` |
| IC permutacion [-477.2, -124.1]; margen minimo 477.0 / 566.5; "a menos de 2 HU" | `resultados_prueba_v1.md` §Lecturas fijadas |
| IC95 [-516.2, -85.7]; caso de Lakens | `resultados_dec_2026-10-15.md` §IC95; DEC 2026-10-15 (4) pto 1 |
| Medianas 1308 (sintetizador) y 1574 (Ti); piso 893 / 184; 0.69 / 0.12; 397 / 1388 | `resultados_dec_2026-10-15.md` §D-extra 2 |
| Variantes: inter -295.3 [-473.6, -117.1]; suelo -238.3 [-384.1, -92.4]; sin cabeza -329.3 [-510.4, -148.3]; anillos +478.0 [+393.9, +562.2], +411.7 [+350.9, +472.5]; Peters 12-14 / 14-16 mm 259.5 / 230.8 (medias: la diferencia de medias con 0.0 del difusor) | `resultados_dec_2026-10-15.md` §Variantes |
| Fraccion en el suelo: 0.000 (sintetizador), 0.017 (Ti, maximo por paciente) | `resultados_prueba_v1.md` (Cordura); `a24_contrastes.md` |
| Parametrico -98.9 [-287.3, +89.4]; suelo -36.3 [-191.5, +118.9]; difusor - parametrico -202.0 | `resultados_dec_2026-10-15.md` §Comparador parametrico |
| Pareado: 1112, -455.0 [-647.6, -262.5]; 725/919, 616/727; Pearson 0.02 | `resultados_dec_2026-10-15.md` §Resultados (i) y (iii); `outputs/a29/a29_perfil.md` |
| Tabla de anillos y razones (6.71 [5.89, 7.54] n = 10, 3.16 [3.08, 3.17], 1.92 [1.82, 2.21], 2.42 [2.09, 2.59], 4.08) | `experiments/objetivo3/outputs/a29/a29_perfil.md` |
| Acuerdo: CV 0.076 / 0.241; Pitman-Morgan r -0.89, p 3.8e-5; log r -0.83, p 4.7e-4; Pearson 0.40; BA -301.0 [-999.0, +397.1]; razon 0.831 [0.533, 1.296] | `resultados_prueba_v1.md` §Acuerdo; `resultados_dec_2026-10-15.md` §#189 |
| Costura E-A2 4.3 / 1.2 HU; preservacion de Peters RMSE 31.4 (20.1-42.4), SSIM 0.9069 (0.8268-0.9653) | `resultados_prueba_v1.md` §Asimetrias; `resultados_dec_2026-10-15.md` §D8 |
| E-A1 v1 (tabla completa, 9 y 4 pacientes) | `resultados_prueba_v1.md` §E-A1 |
| v2: -258.9 [-456.7, -61.1], -264.3 [-456.8, -71.7]; Delta propio 157.1 / 107.1; margen minimo 456.7 / 456.8; anillos +415.2 a +489.8; CV 0.093 / 0.081; Pearson 0.03 / 0.09 | `resultados_dec_2026-10-15.md` §Version 2 en prueba |
| E-A1 v2: 259.5 / 242.1 (propio 0.05 / 0.2), 271.8 / 246.4 (0.03); 4 y 9 de 13 (0.03), 9 y 11 de 13 (propio); costura grupo 2: 43.9 / 72.8 frente a 9.0 | `resultados_dec_2026-10-15.md` §D-extra 3 |
| #196: 71 de 72, 14 casos, 6.4 mm, 6.3 mm | `experiments/registro/registro_2026-10-16.md` §2; DEC 2026-10-16 (2) |
| #138: 72 de 72, mediana 6.5 mm, RIC 5.7-7.2 | `registro_2026-10-16.md` §4; DEC 2026-10-16 (4) |
| Segundo corredor 69 de 72; revision en cortes 56 de CLINIC-metal; fractura 20 de 30 | DEC 2026-10-16 (3) ptos 2 y 4; `capitulo3.tex` §Datos |

## GAP

| Tipo | Texto | Estado |
|---|---|---|
| `\GAPDATO` (nuevo) | "medianas por brazo del coeficiente de Sorensen-Dice y del cambio relativo de volumen del hueso y del metal en la sintesis sobre pelvis sin metal" | ABIERTO. Los valores existen por paciente en `outputs/obj3_pose/a20_test/a20_ea2_test.csv` (`hueso_sdc`, `hueso_dvol`, `metal_sdc`, `metal_dvol`), pero ningun `.md` registrado los resume; no se recalcularon (regla 5). Clase C para el `asesor-tesis`: mediana por paciente y brazo (Peters Ti A/B, difusor 5 semillas) y mediana entre los 13. |

Sin `\GAPLIT` ni `\GAPDEC` nuevos; sin `\REVVISUAL`. Ningun candidato nuevo a `_candidatos.md`.

## Notas para la autora y para r01 (no son GAP)

1. **Categoria "no equivalencia" de la sensibilidad con hierro** (`tab:res-tost`, fila 2; texto: "el intervalo queda
   entero por debajo de -Delta"). `resultados_prueba_v1.md` la rotula con el texto viejo de `a24` ("no se concluye
   equivalencia"); la categoria es la aplicacion directa de la regla de DEC 2026-10-15 pto 15 al IC90
   [-4405.9, -3222.6] frente a +-196.3. Si un revisor la objeta, la alternativa es dejar en la celda "IC entero bajo
   -Delta".
2. **Rango de salida del autoencoder de Guo et al.** Consta en los guiones del modelo distribuido (#93), no en el
   articulo (ficha: NO ENCONTRADO). El texto lo dice asi y no cita el software: #93 deja "la cita del bundle"
   pendiente de la autora y no hay raw en `refs/raw/`. No se abrio `\GAPLIT` para no contradecir la meta de la ronda;
   si la autora quiere la cita, hace falta su raw.
3. **Fuentes atrasadas (PAT-158):** #177 sigue ABIERTA en `04-implicancias.md` aunque DEC 2026-10-15 pto 15 y (3)
   pto 1 fijan su desenlace y lectura; #181 y #182 tambien ABIERTAS con resultados ya en cap. 3. El capitulo usa las
   cifras como medidas (decision de bitacora 2026-10-15, cifras de implicancias que el encargo manda usar).
4. **Contradicciones con otros capitulos:** ninguna encontrada. Cotejadas con `introduccion` (desenlace, -301.0,
   IC90, Delta, mismos cortes y suelo sin cambio de desenlace, piso a favor del sintetizador, 70 pacientes),
   `capitulo1` §Marco estadistico (tres desenlaces, Lakens, siete candidatos), `capitulo2` (desenlace con la formula
   de la bitacora, ida y vuelta medida) y `capitulo3` (2.3 HU, 0.395, 893/184, -455.0, 15 de 72, 13 y 19 pacientes,
   limites de lectura 0.030/0.05/0.2). Las cifras que el cap. 3 ya da en §Amenazas (piso, pareado, CV) se repiten en
   la seccion de datos del cap. 4 como resultado, y la discusion remite a `sec:amenazas` sin repetir sus argumentos.
5. **Ronda: sin implicancias nuevas.** El capitulo no abre ninguna decision de alcance ni cambia cifras escritas en
   otro capitulo.

## Decisiones de redaccion

- En el capitulo de resultados, el desenlace del Obj 3 se da con cifras una vez (§Contraste primario) y la formula
  fija ("no concluyente: los datos no permiten afirmar la equivalencia, y la *streak amplitude* del sintetizador queda
  por debajo de la del protocolo fisico") una sola vez, con la salvedad de cuando se fijo la lectura; la discusion
  remite a `sec:res-primario`.
- Etiquetas del cap. 4 para remitir desde conclusiones: `cap:resultados`, `sec:res-obj1`, `sec:res-obj2`,
  `sec:res-obj3`, `sec:res-primario`, `sec:res-anadidos`, `sec:res-reconstruccion`, `sec:res-v2`, `sec:discusion`.
  Los demas capitulos dicen hoy "capitulo de resultados" en texto; pueden pasar a `\ref` en su proxima ronda.
- En tablas de desenlaces del TOST: "No concluyente, menor", "No equivalencia, menor/mayor" y "Descriptivo" para lo
  que no tiene margen propio (pareado, parametrico).
- El exceso real por anillo (D1) se compara por su forma (razon 0-2 / 6-8 mm) y no por su nivel, con esa salvedad en
  el pie de tabla, porque es otra metrica.
