# singhrao2024fiducial — Validacion end-to-end del tracking de fiduciales con sCT derivada de MRI (CyberKnife)

- **DOI / URL:** 10.1002/mp.16857 (https://doi.org/10.1002/mp.16857; Med Phys. 2024;51:31-41)
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/singhrao2024fiducial.pdf

## Que hace (3 lineas maximo)
Inserta marcadores fiduciales metalicos artificiales en CT sinteticas (sCT) de densidad asignada ("bulk-density") derivadas de MRI, con cinco metodos (plantilla CT, voxel quemado a 10000 HU, plantilla compuesta, simulado sin y con orientacion), y evalua si el tracking de CyberKnife los detecta.
Evalua en un fantoma pelvico antropomorfico propio (correcciones de camilla, incertidumbre de deteccion) y en un fantoma de cabeza (error de targeting end-to-end con peliculas). No mide error en HU ni calidad de imagen.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Supuestos que impiden trasladarlo a implantes en CT clinica:
- El artefacto del fiducial se simula en un medio homogeneo, no en la anatomia: *"in a homogenous 10 cm3 digital water phantom"* (Sec. 2.2.4, p. 35).
- La insercion es un parche fijo pegado en la sCT: *"Fiducials were inserted using a 15 mm × 15 mm × 15 mm patch"* (Sec. 2.2.4, p. 35).
- La sCT receptora no es CT real sino segmentacion con HU constantes: *"Bone, air, and carrageenan/plastic equivalent soft tissue materials were assigned CT numbers"* (Sec. 2.2.2, p. 34).
- Escala del objeto: fiduciales de 1 mm x 3 mm, no tornillos ni placas. Posiciones definidas a mano sobre MRI, sin muestreo de pose.
- Validacion solo en fantomas: *"Human studies need to be conducted to validate the fiducial tracking accuracy"* (Sec. 4, p. 39).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
Ninguno obligatorio. Candidatos solo si la autora decide citarlo como contexto del renderizador:

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 10000 HU (valor de voxel quemado) | "replacing HU with a fixed value (10000HU) (voxel-burned)" | Abstract, p. 31 |
| Parche de insercion 15 mm x 15 mm x 15 mm | "Fiducials were inserted using a 15 mm × 15 mm × 15 mm patch" | Sec. 2.2.4, p. 35 |
| Voxel quemado: errores > 1 mm/1° | "The voxel burned fiducials produced setup errors >1 mm/1°" | Sec. 4, p. 39 |

## Donde entra en mi tesis
- **Related Work del renderizador (contexto):** precedente de insercion de objetos metalicos pequenos en CT (sCT) con su artefacto, mediante plantillas y proyeccion/retroproyeccion simulada, frente a insertar el metal "desnudo" como voxel de HU fijo. El paper reporta que la version sin artefacto (voxel quemado) da peor deteccion y la incertidumbre mas alta (68.39% frente a 40.05%-47.65%, Tabla 1, p. 37). Sirve como apoyo cualitativo a la idea de que la apariencia del artefacto alrededor del metal importa, pero para un algoritmo de tracking concreto y no para segmentacion.
- **Objetivo 1 (MAE < 25 HU en hueso):** NO sirve como precedente. No reporta MAE ni ningun error en HU por tejido (NO ENCONTRADO EN EL PDF); la sCT es de densidad asignada con HU constantes por clase.
- **Muestreador / SAP / BFC / ISC:** no aporta. Posiciones manuales en fantoma, sin anatomia real, sin corredores ni brecha cortical.
- **Pelvis/prostata:** fantoma pelvico con hueso fundido dentro de gel de carragenano; no es CT clinica ni CTPelvic1K.

## Dudas para el asesor
- La Discusion afirma *"setup errors >1 mm/1°"* para el voxel quemado (p. 39), pero en la Tabla 1 (p. 37) solo el pitch (1.22°) supera ese limite; las traslaciones del voxel quemado son como maximo 0.72 mm en valor absoluto. Inconsistencia interna menor.
- La tolerancia *"<0.95 mm"* del Abstract (p. 32) no tiene fuente ni definicion en el cuerpo; la Discusion usa *"<1 mm"* (p. 38). Origen de la tolerancia: NO ENCONTRADO EN EL PDF.
- Vale la pena citarlo como precedente de "metal pequeno + artefacto por plantilla" o basta con las fuentes de insercion de metal ya leidas (p. ej. `ren2022metalinsertion`)?

## Evidencia textual

| # | Cifra / umbral / definicion / criterio | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|---|
| 1 | DOI 10.1002/mp.16857 | "DOI: 10.1002/mp.16857" | Cabecera, p. 31 |
| 2 | Med Phys 2024;51:31-41 | "Med Phys. 2024;51:31–41." | Pie, p. 31 |
| 3 | Fechas: recibido 28/06/2023, revisado 13/10/2023, aceptado 05/11/2023 | "Received: 28 June 2023 Revised: 13 October 2023 Accepted: 5 November 2023" | Cabecera, p. 31 |
| 4 | 6 fiduciales por fantoma, separacion minima 2 cm | "Each phantom had six FMs implanted with a minimum spacing of 2 cm." | Abstract, p. 31; Sec. 2, p. 33 |
| 5 | Metodo voxel quemado: HU fijo 10000 | "replacing HU with a fixed value (10000HU) (voxel-burned)" | Abstract, p. 31 |
| 6 | Incertidumbre media de extraccion < 48% (compuesto y simulado) | "The mean FM-extraction uncertainty for the composite and simulated FMs was below 48%" | Abstract, p. 31 |
| 7 | Umbral de tratamiento 70% | "which is below the 70% treatment uncertainty threshold" | Abstract, pp. 31-32 |
| 8 | Tolerancia de error total de targeting < 0.95 mm | "The total targeting error was within tolerance (<0.95 mm)" | Abstract, p. 32 |
| 9 | Error de targeting 0.26 / 0.44 / 0.35 mm | "(0.26, 0.44, and 0.35 mm for the composite fiducial in sCT" | Abstract, p. 32 |
| 10 | Adquisicion CT 120 kVp, 80 mAs | "CT simulation images were acquired at 120kVp and 80 mAs tube current." | Sec. 2.1, p. 33 |
| 11 | Reconstruccion CT: kernel Bf37, 0.9 x 0.9 mm, corte 1 mm | "Bf37 kernel with 0.9 mm × 0.9 mm in plane resolution and 1 mm slice thickness" | Sec. 2.1, p. 33 |
| 12 | MRI 3.0T Siemens MAGNETOM Vida | "acquired on a 3.0T Siemens MAGNETOM Vida" | Sec. 2.1, p. 33 |
| 13 | Bobina de cuerpo de 18 canales | "A 3T compatible 18-channel body coil (Body 18, Siemens" | Sec. 2.1, p. 33 |
| 14 | T1 VIBE: flip 4°, TE 1.27 ms, TR 4.74 ms | "flip angle of 4°, echo time of 1.27 ms, and repetition time of 4.74 ms" | Sec. 2.1, p. 33 |
| 15 | T1 VIBE: corte 1.5 mm, 0.844-0.875 mm en plano | "slice thickness of 1.5 mm and in-plane resolution of 0.844–0.875 mm" | Sec. 2.1, p. 33 |
| 16 | T2 spin echo: flip 120°, TE 81 ms, TR 6000 ms | "flip angle of 120°, echo time of 81 ms and repetition time of 6000 ms" | Sec. 2.1, p. 33 |
| 17 | T2: corte 2.5 mm, 1.2 mm en plano | "slice thickness of 2.5 mm and in-plane resolution of 1.2 mm" | Sec. 2.1, p. 33 |
| 18 | Rayos X pretratamiento del estudio: 120 kV, 100 mA, 100 ms | "120 kV, 100 mA, 100 ms" | Sec. 2.1, p. 33 |
| 19 | Rayos X clinicos de prostata: 135 kV, 160 mA, 100 ms | "prostate patients typically have x-ray images acquired at 135 kV, 160 mA, 100 ms" | Sec. 2.1, p. 33 |
| 20 | End-to-end tipico: 100-120 kV, 100 mA, 100 ms | "For end-to-end tests, we typically use 100–120 kV, 100 mA, 100 ms." | Sec. 2.1, p. 33 |
| 21 | Version CyberKnife 11.1.3.2 | "In this study, CyberKnife version 11.1.3.2 was used." | Sec. 2.2.1, p. 33 |
| 22 | Criterio: 3 o mas fiduciales para traslaciones y rotaciones | "three or more fiducials are necessary" | Sec. 2.2.1, p. 33 |
| 23 | Definicion del algoritmo: marco probabilistico con modelo oculto de Markov | "a probabilistic framework based on hidden Markov model is used" | Sec. 2.2.1, p. 33 |
| 24 | Transformacion rigida 6D fiduciales DRR vs rayos X | "a 6D rigid transformation between the known fiducial positions" | Sec. 2.2.1, p. 33 |
| 25 | Precision planning system v3.3.1.2 | "Precision planning system (version v3.3.1.2, Accuray" | Sec. 2.2.2, p. 33 |
| 26 | 10 pares de imagenes de camara para incertidumbre intrinseca | "A total of 10 live camera image pairs were acquired" | Sec. 2.2.2, p. 34 |
| 27 | sCT pelvica: hueso 4000 HU, aire -1000 HU, tejido blando 30 HU | "assigned CT numbers of 4000HU, −1000HU, and 30HU in sCT images" | Sec. 2.2.2, p. 34 |
| 28 | Volumen de gel 2700 mL | "encased in 2700 mL of carrageenan gel" | Sec. 2.2.3, p. 34 |
| 29 | Dimensiones del fantoma pelvico 36 x 24 x 20 cm | "The dimensions of the pelvis model were 36 cm × 24 cm × 20 cm." | Sec. 2.2.3, p. 34 |
| 30 | Concentracion de carragenano 7% w/w | "The carrageenan gel concentration of 7% w/w" | Sec. 2.2.3, p. 34 |
| 31 | Seis fiduciales de oro 1 mm x 3 mm | "Six 1 mm (diameter) × 3 mm (length) gold fiducial markers" | Sec. 2.2.3, p. 34 |
| 32 | Agujas 18GA x 20 cm | "implanted using 18GA × 20 cm needles" | Sec. 2.2.3, p. 34 |
| 33 | Separacion >= 2 cm, configuracion no lineal > 15° | "in a non-linear configuration (>15° angle)" | Sec. 2.2.4 (cont. de 2.2.3), p. 35 |
| 34 | Cinco metodos de insercion artificial | "Five methods of artificial fiducial insertion were tested in sCT images" | Sec. 2.2.4, p. 35 |
| 35 | Parche de insercion 15 mm x 15 mm x 15 mm | "Fiducials were inserted using a 15 mm × 15 mm × 15 mm patch" | Sec. 2.2.4, p. 35 |
| 36 | Contorno MRI quemado a 10000 HU | "was voxel burned on sCT to 10000HU" | Sec. 2.2.4, p. 35 |
| 37 | Fantoma de cabeza: 4 esferas de tungsteno de 3 mm | "four 3 mm diameter spherical tungsten fiducials" | Sec. 2.2.4, p. 35 |
| 38 | Fantoma de cabeza: 2 barras 2 mm x 3 mm x 7 mm | "two 2 mm × 3 mm × 7 mm rod fiducials" | Sec. 2.2.4, p. 35 |
| 39 | Artefacto simulado: oro 1 mm x 3 mm en agua homogenea de 10 cm3 | "1 mm diameter × 3 mm length gold fiducial marker in a homogenous 10 cm3" | Sec. 2.2.4, p. 35 |
| 40 | Proyeccion fan beam 360° | "fan beam projections through a full 360 ° rotation" | Sec. 2.2.4, p. 35 |
| 41 | 200 elementos detectores de 0.5 mm | "two hundred 0.5 mm detector sensing elements" | Sec. 2.2.4, p. 35 |
| 42 | Retroproyeccion por transformada inversa fan beam | "back-projected using an inverse fan beam transform" | Sec. 2.2.4, p. 35 |
| 43 | Cinco orientaciones simuladas (4 paralelas al plano, 1 perpendicular) | "Five fiducial orientations were simulated, four assuming the fiducials long axis is parallel" | Sec. 2.2.4, p. 35 |
| 44 | Criterio de eleccion de orientacion: maxima correlacion cruzada normalizada | "based on the highest normalized cross correlation score" | Sec. 2.2.4, p. 35 |
| 45 | sCT de cabeza: aire -1024 HU, tejido blando 10 HU, hueso 1000 HU | "voxel burning air to −1024HU, soft tissue to 10HU and bone to 1000HU" | Sec. 2.3, p. 36 |
| 46 | Fiduciales simulados de cabeza: esfera 3 mm y barra 2 mm | "simulating a 3 mm spherical ball and 2 mm diameter rod in MATLAB" | Sec. 2.3, p. 36 |
| 47 | Esfera acrilica de 31.75 mm | "a 31.75 mm acrylic ball for targeting" | Sec. 2.3, p. 37 |
| 48 | Prescripcion a la isodosis de 70% | "to prescribe the dose (420 cGy to 70% isodose line)" | Sec. 2.3, p. 37 |
| 49 | Dosis puntual maxima 600 cGy | "The maximum point dose is 600 cGy." | Sec. 2.3, p. 37 |
| 50 | Escaner Epson 10000XL a 300 dpi | "flatbed scanner (Epson Expression 10000XL) and a resolution of 300 dpi" | Sec. 2.3, p. 37 |
| 51 | Definicion de error de targeting | "defined as the difference between the centers of the planned and delivered dose" | Sec. 2.3, p. 37 |
| 52 | Definicion de umbral de incertidumbre | "sets the maximum detection uncertainty value for the fiducial extraction algorithm" | Sec. 3.1, p. 37 |
| 53 | Umbral maximo 70% fijado por el fabricante | "The maximum uncertainty threshold of 70% is determined by the vendor" | Sec. 3.1, p. 37 |
| 54 | Criterio: por encima de 70% no se trata | "Above an uncertainty of 70% treatment cannot proceed." | Sec. 3.1, p. 37 |
| 55 | Incertidumbre intrinseca: 10 adquisiciones | "computed for 10 x-ray image acquisitions to quantify the intrinsic tracking system uncertainty" | Sec. 3.1, p. 37 |
| 56 | Correcciones medias < 1 mm/1° salvo voxel quemado | "the mean absolute translational and rotational corrections were less than 1 mm/1°" | Sec. 3.1, p. 37 |
| 57 | Todos los fiduciales en sCT bajo el limite de 70% | "produced a detection uncertainty below the no-treatment limit of 70%" | Sec. 3.1, p. 37 |
| 58 | Tabla 1, SI (mm), Planning CT / Real en sCT / Voxel 10000HU | "SI correction (mm) −0.03 ± 0.05 0.3 ± 0.05 −0.48 ± 0.09" | Tabla 1, p. 37 |
| 59 | Tabla 1, SI (mm), Compuesto / Head-on / Orientado | "0.19 ± 0.03 0.15 ± 0.05 0.15 ± 0.05" | Tabla 1, p. 37 |
| 60 | Tabla 1, LR (mm), Planning CT / Real en sCT / Voxel | "LR correction (mm) −0.03 ± 0.05 −0.01 ± 0.03 −0.72 ± 0.08" | Tabla 1, p. 37 |
| 61 | Tabla 1, LR (mm), Compuesto / Head-on / Orientado | "0.04 ± 0.05 0.06 ± 0.07 0 ± 0" | Tabla 1, p. 37 |
| 62 | Tabla 1, AP (mm), Planning CT / Real en sCT / Voxel | "AP correction (mm) 0.1 ± 0.01 −0.2 ± 0.05 0.67 ± 0.09" | Tabla 1, p. 37 |
| 63 | Tabla 1, AP (mm), Compuesto / Head-on / Orientado | "0.32 ± 0.04 0.25 ± 0.05 0.2 ± 0" | Tabla 1, p. 37 |
| 64 | Tabla 1, Roll (°), Planning CT / Real en sCT / Voxel | "Roll correction (°) 0.1 ± 0.01 −0.03 ± 0.11 0.17 ± 0.13" | Tabla 1, p. 37 |
| 65 | Tabla 1, Roll (°), Compuesto / Head-on / Orientado | "0.28 ± 0.06 0.18 ± 0.11 −0.04 ± 0.07" | Tabla 1, p. 37 |
| 66 | Tabla 1, Pitch (°), Planning CT / Real en sCT / Voxel | "Pitch correction (°) 0.13 ± 0.05 0.62 ± 0.1 1.22 ± 0.28" | Tabla 1, p. 37 |
| 67 | Tabla 1, Pitch (°), Compuesto / Head-on / Orientado | "−0.12 ± 0.04 −0.11 ± 0.06 −0.09 ± 0.03" | Tabla 1, p. 37 |
| 68 | Tabla 1, Yaw (°), Planning CT / Real en sCT / Voxel | "Yaw correction (°) −0.17 ± 0.05 −0.21 ± 0.11 −0.26 ± 0.19" | Tabla 1, p. 37 |
| 69 | Tabla 1, Yaw (°), Compuesto / Head-on / Orientado | "0.04 ± 0.05 0.25 ± 0.08 0.2 ± 0.12" | Tabla 1, p. 37 |
| 70 | Tabla 1, Incertidumbre (%), Planning CT / Real en sCT / Voxel | "Uncertainty (%) 16.19 ± 0.16 33.94 ± 0.46 68.39 ± 0.72" | Tabla 1, p. 37 |
| 71 | Tabla 1, Incertidumbre (%), Compuesto / Head-on / Orientado | "40.05 ± 0.61 44.57 ± 0.43 47.65 ± 0.33" | Tabla 1, p. 37 |
| 72 | Tabla 1, nota: 10 pares de rayos X | "Ten x-ray image pairs were acquired to calculate the intrinsic tracking system uncertainty." | Tabla 1 (nota), p. 37 |
| 73 | Tabla 2, SI (mm), Planning CT / Compuesto / Head-on | "SI correction (mm) 0.1 ± 0.01 −0.3 ± 0 0 ± 0" | Tabla 2, p. 37 |
| 74 | Tabla 2, LR (mm) | "LR correction (mm) 0.2 ± 0.01 0.2 ± 0 −0.1 ± 0.04" | Tabla 2, p. 37 |
| 75 | Tabla 2, AP (mm) | "AP correction (mm) 0.1 ± 0.01 0.17 ± 0.06 0.3 ± 0" | Tabla 2, p. 37 |
| 76 | Tabla 2, Roll (°) | "Roll correction (°) 0.1 ± 0.01 −0.3 ± 0 −0.4 ± 0.08" | Tabla 2, p. 37 |
| 77 | Tabla 2, Pitch (°) | "Pitch correction (°) −0.1 ± 0.01 0 ± 0 0.2 ± 0.04" | Tabla 2, p. 37 |
| 78 | Tabla 2, Yaw (°) | "Yaw correction (°) 0.1 ± 0.01 −0.07 ± 0.06 0.3 ± 0.08" | Tabla 2, p. 37 |
| 79 | Tabla 2, Incertidumbre (%) | "Uncertainty (%) 18.77 ± 0.1 40.37 ± 0.25 44.94 ± 1.29" | Tabla 2, p. 37 |
| 80 | Tabla 2, Error de targeting (mm) | "Targeting error (mm) 0.35 0.26 0.44" | Tabla 2, p. 37 |
| 81 | Correcciones dentro de 0.5 mm/0.5° del estandar CT | "translational and rotational couch corrections within 0.5 mm/0.5° of the CT-based standard" | Sec. 4, p. 38 |
| 82 | Error de targeting end-to-end < 1 mm | "targeting error for the composite and simulated fiducial markers were <1 mm" | Sec. 4, p. 38 |
| 83 | Correcciones de sustitutos simulados y compuestos < 0.5 mm/0.5° | "fiducial marker surrogates were both <0.5 mm/0.5°" | Sec. 4, pp. 38-39 |
| 84 | Voxel quemado: errores > 1 mm/1° | "The voxel burned fiducials produced setup errors >1 mm/1°" | Sec. 4, p. 39 |
| 85 | Distorsion geometrica MRI hasta 0.5 mm | "the effects of the errors contribute up to 0.5 mm depending on the readout bandwidth" | Sec. 4, p. 39 |
| 86 | Barrido de HU del voxel quemado: 750 a 15000 HU | "We adjusted the burned in HU value between 750HU and 15000HU." | Sec. 4, p. 39 |
| 87 | Meseta de incertidumbre por encima de 10000 HU | "detection uncertainty decreased with increasing HU values, and plateaued above 10000HU" | Sec. 4, p. 39 |
| 88 | Justificacion de 10000 HU: mayor que hueso cortical | "appreciably higher than cortical bone, and close to the mean centroid voxel HU" | Sec. 4, p. 39 |
| 89 | Fantoma preliminar con 4 fiduciales | "four fiducial markers were implanted in a homogenous carrageenan phantom" | Sec. 4, p. 39 |
| 90 | Afirmacion de independencia del algoritmo de sCT | "the fiducial marker insertion approaches investigated in this study are algorithm-agnostic" | Sec. 4, p. 39 |
| 91 | Conclusion: voxel quemado demasiado simple para CyberKnife | "voxel-burning fiducials into sCT images ... is too simple for CyberKnife fiducial tracking" | Sec. 5, p. 39 |
| 92 | MAE u otro error en HU por tejido (hueso) en la sCT | NO ENCONTRADO EN EL PDF | — |
| 93 | Metrica de calidad o realismo de imagen del artefacto insertado (SSIM, PSNR, lectura humana) | NO ENCONTRADO EN EL PDF | — |
| 94 | Origen o justificacion de la tolerancia de 0.95 mm | NO ENCONTRADO EN EL PDF | — |
| 95 | Pruebas estadisticas de significancia entre metodos | NO ENCONTRADO EN EL PDF | — |
| 96 | Pacientes o CT clinicas evaluadas | NO ENCONTRADO EN EL PDF | — |
