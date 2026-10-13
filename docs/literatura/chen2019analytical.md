# chen2019analytical — Metodo analitico de MAR por caracterizacion geometrica del endurecimiento del haz

- **DOI / URL:** https://doi.org/10.1155/2019/2351878 (impreso en la cabecera de la p. 1: "Volume 2019, Article ID 2351878, 7 pages")
- **Nivel de lectura:** 4 (propuesto por Claude; fuera de la escala 1-3 de la plantilla. Se mantiene el nivel sugerido: el paper es una variante del corrector geometrico de Park et al. 2016 con un espectro sustituto sinusoidal, validada solo con un fantoma 2D y sin metricas cuantitativas. Sirve para rastrear alternativas al nucleo h(u), no como fuente de cifras)
- **Leido a fondo por la autora:** no
- **PDF:** papers/chen2019analytical.pdf

## Que hace (3 lineas maximo)
Modela el artefacto de endurecimiento del haz como R^{-1}[p - R f_{E'}], calculado solo a partir de la funcion caracteristica del metal segmentado, sustituyendo el espectro desconocido por una funcion sinusoidal truncada de semiancho h (ec. 9). Obtiene una expresion cerrada del sinograma del artefacto (ec. 12), lo reconstruye por FBP y lo resta de la imagen original (ec. 13). Validado en un fantoma mandibular digital 2D fan-beam con incrustaciones de mercurio.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; los supuestos relevantes son fisicos:
- Solo endurecimiento del haz por metal: "we only consider beam-hardening effects of metallic objects" (p. 3, Sec. 3). Fotones escasos, dispersion y volumen parcial no se modelan.
- Metal homogeneo: "metallic objects have the same attenuation coefficient in a reconstruction image" (p. 3, Sec. 3).
- Atenuacion lineal en energia: f_E - f_{E'} ≈ w(E)(E - E') (ec. 7, p. 3), y w(E) "approximately independent of E" para llegar a la ec. 12 (pp. 3-4).
- Espectro sustituto: eta'(E) = A sin(omega(E - E' + theta)) si |E - E'| <= h, 0 en otro caso (ec. 9, p. 3). No es un espectro uniforme/rectangular.
- Parametros fijados a mano (A = pi/4h, omega = pi/2h, E' = 65 keV, h = 55 keV, theta = h) y un "optimized parameter w = 0.042" cuyo procedimiento de optimizacion no se describe: NO ENCONTRADO EN EL PDF.

Relacion con el canal T = -FBP[h(lambda R(M))], h(u) = log(sinh u / u) de la tesis:
- Coincide en la estructura: artefacto = FBP de una funcion no lineal de la proyeccion de la mascara de metal (R_{lambda(Omega)}), sin datos crudos ni espectro medido.
- Difiere en el espectro sustituto (sinusoide truncada, ec. 9) y por eso en la no linealidad: la ec. 12 combina exp{-w h R'} / sqrt((wR')^2 + omega^2) con terminos sin(gamma - ...), y no contiene un termino sinh(u)/u.
- Comparacion explicita con Park, Choi y Seo 2017: NO ENCONTRADO EN EL PDF. El paper solo cita a Park, Hwang y Seo 2016 (ref. [25], IEEE TMI 35(2)) y dice de el que "choosing the approximate alternative of energy spectrum is very critical" (p. 2, Sec. 1).
- La ec. 12 incluye el angulo de proyeccion phi dentro del seno (sin(gamma - (omega h + omega phi))); el PDF no explica por que el artefacto dependeria de phi. Se registra tal cual, sin interpretar.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna propuesta para la tesis | Los parametros son ad hoc para un fantoma 2D y no hay metricas cuantitativas | — |

## Donde entra en mi tesis
Contexto en la justificacion del canal de condicion analitico (renderizador): ejemplo adicional de que el artefacto de endurecimiento puede aproximarse como FBP de una funcion no lineal de R(M) sin conocer el espectro, y de que la forma de esa no linealidad depende del espectro sustituto elegido (aqui sinusoidal, no uniforme). Util para una frase de trabajo relacionado o para justificar que h(u) = log(sinh u/u) es una eleccion entre varias, no la unica. No aporta cifras ni baseline.

## Dudas para el asesor
1. Vale la pena mencionar este espectro sustituto sinusoidal como alternativa al nucleo log(sinh u/u), o basta con citar Park et al. 2016/2017? El paper no muestra que su eleccion mejore sobre la de Park (no hay comparacion con [25]; solo con interpolacion lineal y solo visual).
2. La ec. 12 contiene el angulo phi en el argumento del seno; sin derivacion intermedia en el PDF no se puede verificar. Conviene no apoyarse en esta formula.
3. El "optimized parameter w = 0.042" no tiene procedimiento de ajuste descrito: no es reproducible tal como esta publicado.

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| DOI / identificador | "https://doi.org/10.1155/2019/2351878" | Cabecera, p. 1 |
| Fechas | "Received 7 November 2018; Accepted 20 December 2018; Published 13 January 2019" | p. 1 |
| Claim: sin conocimiento previo del espectro | "It does not require prior knowledge of x-ray energy spectrum" | Abstract, p. 1 |
| Claim: sin datos de proyeccion originales | "and original projection data, avoiding iterative calculation and saving reconstruction time" | Abstract, p. 1 |
| Critica a Park et al. [25] | "choosing the approximate alternative of energy spectrum is very critical" | Sec. 1, p. 2 |
| Rango del espectro a 120 kV | "the range of the output x-ray photon energy is [20 keV, 120 keV]" | Sec. 2, p. 2 |
| Corte inferior del espectro | "energy photons less than 20 keV are absorbed by some materials" | Sec. 2, p. 2 |
| Modelo de proyeccion polienergetica (ec. 4) | "eta(E) = I_{0,E} / ∫ I_{0,E} dE represents a normalized x-ray beam energy spectrum" | Sec. 2, p. 3 |
| Definicion del artefacto (ec. 5) | "R^{-1}[p - Rf_{E'}](X) seen as metal artifacts" | Sec. 3, p. 3 |
| Supuesto: metal homogeneo | "metallic objects have the same attenuation coefficient in a reconstruction image" | Sec. 3, p. 3 |
| Supuesto: solo endurecimiento por metal | "we only consider beam-hardening effects of metallic objects" | Sec. 3, p. 3 |
| Correccion agua/hueso asumida existente | "water and bone beam-hardening corrections can usually be used in current medical CT" | Sec. 3, p. 3 |
| Fuera del metal | "f_E - f_E' = 0 outside of Omega" | Sec. 3, p. 3 |
| Justificacion fisica de ec. 7 | "photoelectric interactions is roughly inversely proportional to the cubic of excess photon energy" | Sec. 3, p. 3 |
| Aproximacion lineal (ec. 7) | "f_E - f_E' ≈ w(E)(E - E')" | Ec. 7, p. 3 |
| Dependencia de w(E) | "w(E) depends on E and attenuation coefficients of metal regions" | Sec. 3, p. 3 |
| Mascara de metal | "lambda(Omega) is a characteristic function for the metal domain Omega" | Sec. 3, p. 3 |
| Espectro sustituto (ec. 9) | "eta'(E) = A sin(omega(E - E' + theta)) if |E - E'| <= h; 0 otherwise" | Ec. 9, p. 3 |
| Parametros del sustituto | "selections of an amplitude A, a frequency omega, and a phase theta are generally related to h" | Sec. 3, p. 3 |
| Criterio de validez del sustituto (ec. 10) | "ln(∫[eta(E) - eta'(E)] exp{-w(E)(E-E')R_lambda(Omega)} dE) ≈ 1" | Ec. 10, p. 3 |
| Supuesto para ec. 12 | "supposing that w(E) is approximately independent of E" | Sec. 3, pp. 3-4 |
| Forma cerrada (ec. 12) | "exp{-whR'} / sqrt((wR')^2 + omega^2) sin(gamma - (omega h + omega phi))" | Ec. 12, p. 4 |
| Definiciones en ec. 12 | "R' = R_lambda(Omega)(r, phi), cos gamma = wR' / sqrt((wR')^2 + omega^2)" | p. 4 |
| Correccion (ec. 13) | "f_E'(X) = R^{-1}p(X) - R^{-1}[p - Rf_E'](X)" | Ec. 13, p. 4 |
| Plataforma | "numerical simulations are performed on VC++ 6.0 platform" | Sec. 4, p. 4 |
| Distancia fuente-isocentro | "distance between x-ray source and a center of rotation is 1100mm" | Sec. 4, p. 4 |
| Distancia fuente-detector | "distance between x-ray source and a linear-array detector is 1600mm" | Sec. 4, p. 4 |
| Tamano de celda del detector | "the length of a detector cell is 0.87mm" | Sec. 4, p. 4 |
| Numero de celdas | "the number of detector cells is 512" | Sec. 4, p. 4 |
| Angulos de proyeccion | "the number of 360 degree full-scan projection angles is 660" | Sec. 4, p. 4 |
| Matriz de imagen | "The size of image matrix is 512 x 512" | Sec. 4, p. 4 |
| Fantoma | "We select a modified digital mandibular phantom" | Sec. 4, p. 4 |
| Origen del fantoma | "which are firstly given by Lemmens et al. [32]" | Sec. 4, p. 4 |
| Objetos metalicos | "Three circles with maximum gray values mean the implanted mercury objects" | Sec. 4, p. 4 |
| Tejidos del fantoma | "set according to the parameters reported by ICRU44 [33]" | Sec. 4, p. 4 |
| Coeficientes de atenuacion | "Their attenuation coefficients are obtained by XCOM software [34]" | Sec. 4, pp. 4-5 |
| Espectro de simulacion | "where x-ray tube operates at 120 kVp" | Sec. 4, p. 5 |
| Densidad mercurio (estructura 1) | "Mercury 13.6" | Tabla 1, p. 5 |
| Densidad hueso (estructuras 2, 3) | "Bone 2.9" / "Bone 2.7" | Tabla 1, p. 5 |
| Densidad tejido blando (estructuras 4-6) | "Soft tissue 0.8" / "0.6" / "0.2" | Tabla 1, p. 5 |
| Ventana de visualizacion del fantoma | "the display window is [0.0, 4.5]" | Fig. 4, p. 5 |
| Umbral de segmentacion del metal | "we select the threshold value 3000HU [35, 36]" | Sec. 4, p. 5 |
| Valores de A y omega | "A = pi/4h, omega = pi/2h" | Sec. 4, p. 5 |
| Valores de E' y h | "E' = 65Kev, h = 55Kev" | Sec. 4, p. 5 |
| Valor de theta y w | "theta = h and the optimized parameter w = 0.042" | Sec. 4, p. 5 |
| Procedimiento de optimizacion de w | NO ENCONTRADO EN EL PDF | — |
| Tiempo de reconstruccion | "CT image reconstruction takes about 85 seconds" | Sec. 4, p. 5 |
| Hardware | "on a computer with CPU 3.40GHz" | Sec. 4, p. 5 |
| Comparador | "a reconstruction result using the linear interpolation MAR in Figure 7(b)" | Sec. 4, p. 5 |
| Criterio de evaluacion (solo visual) | "the developed methods can reduce most artifacts, and preserve more original details" | Sec. 4, p. 5 |
| Ventana de visualizacion de resultados | "the display window is [0.0, 0.6]" | Fig. 7, p. 6 |
| Metricas cuantitativas (RMSE, PSNR, SSIM u otras) | NO ENCONTRADO EN EL PDF | — |
| Comparacion con Park et al. [25] | NO ENCONTRADO EN EL PDF | — |
| Comparacion con Park, Choi y Seo 2017 | NO ENCONTRADO EN EL PDF | — |
| Datos clinicos reales | NO ENCONTRADO EN EL PDF | — |
| Material de densidad menor | "if the materials with lower density than the mercury are implanted" | Sec. 4, p. 5 |
| Limitacion declarada | "photoelectric interactions are very difficult" (por ruido de generacion y deteccion) | Sec. 5, p. 6 |
| Disponibilidad de datos | "available from the corresponding author upon request" | Data Availability, p. 6 |
