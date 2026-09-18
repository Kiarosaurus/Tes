# yazdi2011opposite — Reemplazo por vista opuesta para MAR dental (OVR)

- **DOI / URL:** 10.1118/1.3566016
- **Nivel de lectura:** 2 (metodo) — PROPUESTO por Claude
- **Leido a fondo por la autora:** no
- **PDF:** papers/yazdi2011opposite.pdf

## Que hace (3 lineas maximo)
MAR en sinograma para objetos dentales pequenos y multiples: segmenta metal en la imagen FBP inicial con un umbral T = alpha*Imax (alpha = 0.9), lo reproyecta para marcar
proyecciones afectadas y las reemplaza por su vista opuesta (interpolacion bilineal, con desvanecimiento en los bordes, p = 12). Compara con interpolacion lineal tipo Kalender
en un craneo fantoma (PSNR en la ROI de la lengua) y en un caso clinico de cabeza y cuello (solo evaluacion visual).

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Supuestos relevantes para la tesis:
- El umbral es GLOBAL por imagen (corte): fraccion fija del maximo de toda la imagen inicial, no local por objeto: "a fixed fraction of the maximum value found in each initial image" (p. 2276, Sec. II.A).
- Asume que hay metal en el corte: "Imax should be high enough to ensure the presence of a metal object" (p. 2277). El valor minimo de Imax: NO ENCONTRADO EN EL PDF.
- El metodo tolera una segmentacion imprecisa: "the perfect determination of such boundaries is not crucial" (p. 2276, Sec. I).
- Solo para CT helicoidal de un corte y objetos pequenos en z: "only valid for single-slice helical CT scanning" (p. 2277, Sec. II.B).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito (alpha = 0.9, solo como precedente de umbral relativo al maximo)
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| alpha = 0.9 | "the value of alpha is selected as being equal to 0.9" | Sec. II.A, p. 2277 |
| T = alpha*Imax | "where Imax is the maximum value found in the given image I" | Sec. II.A, Ec. 1, p. 2277 |

## Donde entra en mi tesis
Metodos / extraccion de mascaras de implantes reales (E8, #46/#47): precedente publicado de un umbral de metal RELATIVO al maximo en lugar de un HU fijo. NO respalda el
semimaximo LOCAL: el umbral de Yazdi es global por corte y conservador (90 %, no 50 %), y su exactitud no se mide. Tambien confirma lo que atribuye xie2024implantsegmentation
("90% of the maximum gray value"): la cifra coincide, y el maximo es el de cada imagen reconstruida inicial, no del sinograma ni de una ROI.

## Dudas para el asesor
- Alcanza con citar a Yazdi como precedente de umbral "relativo al maximo" si el principio (global al 90 %) es distinto del semimaximo local (50 % por objeto)?
- Un umbral del 90 % del maximo tiende a subsegmentar, que es justo el problema que el semimaximo busca resolver con el fuste. Conviene mencionar ese contraste de forma explicita?
- Justificacion empirica de alpha = 0.9: NO ENCONTRADO EN EL PDF (solo "is close to 1 and does not change with imaging parameters").

## Evidencia textual
| Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Umbral: definicion | "We consider a fixed fraction of the maximum value found in each initial image" | Sec. II.A, p. 2276 |
| Umbral: formula | "T = alpha Imax" | Sec. II.A, Ec. 1, p. 2277 |
| Imax: de que imagen | "where Imax is the maximum value found in the given image I" | Sec. II.A, p. 2277 |
| Imagen inicial | "initial image is reconstructed from the 360 deg raw helical projections" | Sec. II.A, p. 2276 |
| Imagen inicial: algoritmo | "using a conventional fan-beam FBP algorithm" | Sec. II.A, p. 2276 |
| alpha: propiedades | "is fixed for all images, is close to 1 and does not change" | Sec. II.A, p. 2277 |
| alpha = 0.9 | "the value of alpha is selected as being equal to 0.9" | Sec. II.A, p. 2277 |
| Aplicacion de alpha | "For phantom and patient studies, the value of alpha is selected" | Sec. II.A, p. 2277 |
| Condicion sobre Imax | "Imax should be high enough to ensure the presence of a metal object" | Sec. II.A, p. 2277 |
| Valor minimo de Imax | NO ENCONTRADO EN EL PDF | — |
| Automatizacion | "the threshold is quasiautomatically determined in each initial image" | Sec. II.A, p. 2277 |
| Justificacion: dependencia de Z | "the threshold does depend on Z (object atomic number)" | Sec. IV, p. 2280 |
| Justificacion: ajuste automatico | "the detection step is automatically adjusted for different Z objects" | Sec. IV, p. 2280 |
| Justificacion empirica de 0.9 | NO ENCONTRADO EN EL PDF | — |
| Tolerancia a bordes | "the perfect determination of such boundaries is not crucial" | Sec. I, p. 2276 |
| Sensibilidad de interpolacion | "These methods are highly sensitive to the correct detection of the missing projections" | Sec. I, p. 2276 |
| Reproyeccion | "reprojected using forward projection to obtain approximate affected projections" | Sec. II.A, p. 2277 |
| Deteccion futura | "integration of a more sophisticated metal detection approach" | Sec. V, p. 2281 |
| Exactitud de la segmentacion de metal | NO ENCONTRADO EN EL PDF | — |
| Alcance geometrico | "only valid for single-slice helical CT scanning" | Sec. II.B, p. 2277 |
| Desplazamiento de vistas opuestas | "ranging from a fraction of millimeters up to a few millimeters" | Sec. II.B, p. 2277 |
| Interpolacion bilineal | "we use the bilinear interpolation using four nearest projections" | Sec. II.B, p. 2278 |
| Profundidad de desvanecimiento p = 12 | "we chose p to be 12 empirically" | Sec. II.B, p. 2278 |
| Bloques de datos de 180 deg | "corresponding to a data block of 180 deg" | Sec. II.B, p. 2278 |
| Limitacion del metodo | "limited to metallic objects with small size" | Sec. II.B, p. 2278 |
| Fantoma: materiales metalicos | "amalgam fillings, gold crown, and titanium implants" | Sec. II.D, p. 2278 |
| Fantoma: tejidos | "made out of Surgident periphery wax" | Sec. II.D, p. 2278 |
| Fantoma: lengua | "the tongue was made of Polyflex" | Sec. II.D, p. 2278 |
| ROI de evaluacion | "This region of interest was chosen manually" | Sec. II.D, p. 2278 |
| Metrica PSNR | "peak signal to noise ratio (PSNR), which assesses the image restoration quality" | Sec. II.E, p. 2278 |
| Bits b (valor usado) | NO ENCONTRADO EN EL PDF | — |
| Baseline | "an interpolation-based algorithm originally proposed by Kalender et al." | Sec. II.F, p. 2279 |
| Escaner | "Siemens Somatom Emotion used in helical mode at 130 kVp" | Sec. III, p. 2279 |
| Carga y pitch | "140 mA s) with a pitch of 2" | Sec. III, p. 2279 |
| Espesor de corte | "The reconstructed image thickness is 2 mm" | Sec. III, p. 2279 |
| Mismo protocolo | "In both phantom and patient cases, the same parameters of scanning were used" | Sec. III, p. 2279 |
| n fantoma (cortes evaluados) | "we compare the six consecutive images of the phantom" | Sec. III.A, p. 2279 |
| Ventana de visualizacion | "Window width W=400 and window level L=40" | Fig. 4, p. 2279 |
| PSNR imagen 1 (raw/interp/OVR) | "1 28.54 30.92 31.17" | Tabla I, p. 2279 |
| PSNR imagen 2 | "2 27.86 28.7 29.12" | Tabla I, p. 2279 |
| PSNR imagen 3 | "3 24.12 26.32 27.90" | Tabla I, p. 2279 |
| PSNR imagen 4 | "4 21.95 23.61 25.67" | Tabla I, p. 2279 |
| PSNR imagen 5 | "5 19.65 22.13 24.44" | Tabla I, p. 2279 |
| PSNR imagen 6 | "6 23.2 25.72 27.21" | Tabla I, p. 2279 |
| Criterio PSNR | "Larger PSNR values are better." | Tabla I, p. 2279 |
| n pacientes | "Figure 5 shows the comparative results for a typical clinical case" | Sec. III.B, p. 2280 |
| n pacientes (cifra explicita) | NO ENCONTRADO EN EL PDF | — |
| Evaluacion clinica cuantitativa | NO ENCONTRADO EN EL PDF | — |
| Software | "implemented in MATLAB (Version 6.5)" | Sec. IV, p. 2280 |
| Hardware | "3 GHz Pentium IV desktop computer with 1024 MB RAM" | Sec. IV, p. 2280 |
| Tiempo | "on the entire sinogram of the clinical case is about 30 min" | Sec. IV, p. 2280 |
| Financiamiento | "NSERC under Grant No. 262105" | Agradecimientos, p. 2281 |

## Candidatos de snowballing
| Cita tal como aparece | n. ref | Por que |
|---|---|---|
| M. Yazdi, L. Gingras, and L. Beaulieu, "An adaptive approach of metal artifact reduction in helical CT for radiation therapy treatment planning: Experimental and clinical studies," Int. J. Radiat. Oncol., Biol., Phys. 62, 1224-1231 (2005). | 14 | Mismo grupo, protesis de cadera; el titulo dice "adaptive" y en p. 2280 se cita como trabajo previo con paso de segmentacion automatica. Puede traer el origen del umbral relativo al maximo en un contexto ortopedico. El criterio de umbral que usa: NO ENCONTRADO EN EL PDF (solo esta en la ref.). |
