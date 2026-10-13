# gottschalk2022DL — Inpainting DL para MAR en CBCT con longitud de trayectoria en metal

- **DOI / URL:** 10.1002/mp.15909 (impreso en p. 1: "DOI: 10.1002/mp.15909"; p. 14: https://doi.org/10.1002/mp.15909)
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/gottschalk2022DL.pdf

Ano segun el PDF: 2022 ("Med Phys. 2022;1–14.", pie de p. 1; "Accepted: 18 July 2022", p. 1). Coincide con la clave del archivo. Volumen/numero: NO ENCONTRADO EN EL PDF (la cita de la p. 14 trae solo "Med Phys. 2022;1-14").

## Que hace (3 lineas maximo)
Propone PaintNet, una U-Net que hace inpainting en el dominio de proyecciones de CBCT (C-arm movil) como paso de MAR, metiendo como canales extra la mascara binaria de metal y un mapa estimado de longitud de trayectoria en metal. Ese mapa sale del filtro de consistencia (CF) aplicado a segmentaciones 2D. Se entrena y evalua solo con pares reales con y sin metal de cadaveres (rodillas y columnas) y se compara con LI (fsMAR) y PConv-Net.

## Restriccion o supuesto clave
No es un paper de sintesis generativa: reduce artefactos, no los genera. Hay tres supuestos relevantes para el canal de condicion de la tesis:
- La longitud de trayectoria en metal NO se calcula desde un modelo CAD ni desde una mascara 3D precisa. Es un producto intermedio del CF: retroproyeccion de las mascaras 2D segmentadas, umbral y reproyeccion ("the estimated metal path length map is an intermediate result", Fig. 3, p. 4).
- El mapa es una estimacion binaria y reproyectada, por lo que puede quedarse corto o pasarse ("can consequently vary between an under- or overestimation", Sec. 4, p. 13). Los autores atribuyen a la sobreestimacion zonas inpintadas "too dark" (Sec. 4, p. 13).
- Los autores dicen que con simulacion sobre mallas 3D la longitud seria exacta: "using for example 3D meshes as a basis, the accurate metal path length is available" (Sec. 4, p. 12-13). El paper no lo implementa.

No hay ablacion con y sin el mapa de longitud. El beneficio se argumenta de forma cualitativa: "the network relies heavily on the given metal path length information" (Sec. 4, p. 13).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 13 canales de entrada | "network's input has a size of 976 pixels × 976 pixels × 13 channels" | Sec. 2.3.1, p. 5 |
| SSIM medio 0.9974 | "reach a mean structural similarity index measure (SSIM) score of 0.9974" | Abstract, p. 1 |

## Donde entra en mi tesis
Sirve de antecedente para el canal de condicion basado en la longitud de trayectoria en metal por proyeccion: es un precedente de usar ese mapa como canal extra de entrada a una red. Hay que marcar las diferencias:
- (a) aqui el mapa se estima desde segmentaciones 2D con CF, no desde una mascara o un modelo del implante;
- (b) se usa para MAR en CBCT, no para sintetizar artefactos en CT pelvica;
- (c) no aporta evidencia ablativa cuantitativa del aporte del canal.

Region anatomica: rodilla y columna (cadaver), no pelvis.

## Dudas para el asesor
- El paper no aisla el aporte del mapa de longitud (no hay ablacion). Basta como precedente de "canal extra de longitud de trayectoria" o hace falta buscar una fuente con ablacion?
- Los autores sostienen que una longitud exacta (desde mallas 3D) podria mejorar el resultado (Sec. 4, p. 13), pero no lo prueban. Conviene citarlo solo como motivacion y no como evidencia?

## Evidencia textual

| Item | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Fechas | "Received: 7 March 2022 Revised: 29 June 2022 Accepted: 18 July 2022" | p. 1 (cabecera) |
| Revista / ano | "Med Phys. 2022;1–14." | p. 1 (pie) |
| DOI | "DOI: 10.1002/mp.15909" | p. 1 |
| Volumen / numero | NO ENCONTRADO EN EL PDF | — |
| Tipo de implantes | "fixated with metal implants like plates and screws" | Sec. 1, p. 1 |
| Equipo | "an isocentric mobile C-arm system" | Sec. 2.1, p. 2 |
| Datos: pares | "contain 55 matching 3D scan pairs comprising 36 knees and 19 spines" | Sec. 2.1, p. 2-3 |
| Datos: origen | "three cadaver studies of human knees and spines" | Sec. 2.1, p. 2 |
| Datos: par con/sin metal | "the first scan with metal implants and the second scan without metal implants" | Sec. 2.1, p. 3 |
| Rango angular / proyecciones | "covers an angular range of 200°, acquiring 400 2D projection images" | Sec. 2.1, p. 3 |
| Incremento angular | "using an equiangular increment of 0.5°" | Sec. 2.1, p. 3 |
| Tamano de proyeccion | "image size of each acquired 2D projection is 976² pixels" | Sec. 2.1, p. 3 |
| Pixel | "with a pixel size of 0.310 mm" | Sec. 2.1, p. 3 |
| Volumen reconstruido | "a size of 512³ voxels with a voxel size of 0.313 mm" | Sec. 2.1, p. 4 |
| Estudio 1: implantes en superficie | "metal implants were solely placed on the surface (the skin)" | Sec. 2.1, p. 3 |
| Estudios 2 y 3: implantes en hueso | "lie directly on and even inside the specimen's bone" | Sec. 2.1, p. 3 |
| Particion | "randomly split into 33 3D scans for training, 11 for testing" | Sec. 2.1, p. 4 |
| Validacion | "and 11 for validation" | Sec. 2.1, p. 4 |
| GT de entrenamiento | "metal-free projection is used as a ground truth (GT) label" | Sec. 2.1, p. 4 |
| Origen de la longitud de trayectoria | "the CF also provides an estimation of the metal path lengths" | Sec. 2.2, p. 4 |
| Longitud desde segmentacion (no CAD) | "the estimated metal path length map is an intermediate result" | Fig. 3, p. 4 |
| Contador de aciertos | "expressing the amount of 2D segmentation masks contributing to that specific voxel" | Sec. 2.2, p. 4 |
| N mascaras | "total number of segmentation masks ... (in our case 400)" | Sec. 2.2, p. 4 |
| Normalizacion V_Norm | "normalized voxel values of V_Norm range between 0 and 1" | Sec. 2.2, p. 5 |
| Umbral de binarizacion | "described in detail in our previous work" | Sec. 2.2, p. 5 |
| Valor numerico del umbral CF | NO ENCONTRADO EN EL PDF | — |
| Reproyeccion = mapa de longitud | "can be interpreted as an estimated metal path length map" | Sec. 2.2, p. 5 |
| Entrada como canal extra | "add an estimated metal path length map ... to the network's input" | Sec. 2.3, p. 5 |
| Motivacion | "shrinks the problem to a nearly subtraction-like task" | Sec. 2.3, p. 5 |
| No borra info bajo el metal | "uses the complete unprocessed projection images" | Sec. 2.3, p. 5 |
| Arquitectura | "eight contraction blocks and eight corresponding expansion blocks with skip connections" | Sec. 2.3.1, p. 5 |
| Cuello de botella | "bottleneck has a size of 7 pixels × 7 pixels" | Sec. 2.3.1, p. 5 |
| Mapas de caracteristicas | "with an amount of 1024 feature maps" | Sec. 2.3.1, p. 5 |
| Ventana de vecinas | "sliding window has a window size of 11 and an angular increment of 1°" | Sec. 2.3.1, p. 5 |
| Vecinas | "10 additional projections are provided to the network" | Sec. 2.3.1, p. 5 |
| Total de canales | "976 pixels × 976 pixels × 13 channels" | Sec. 2.3.1, p. 5 |
| Fusion de imagen | Ec. (6): I_fusion = I_pred∘M + I_in∘(1 − M) | Sec. 2.3.2, p. 5 |
| Preprocesado | "transformed from pixel intensity data to line integral data" | Sec. 2.3.3, p. 6 |
| Optimizador | "exponentially decaying learning rate, the Adam optimizer" | Sec. 2.3.3, p. 6 |
| Peso region metal | "λ is empirically chosen to 10" | Sec. 2.3.3, p. 6 |
| Pesos de perdida | "chosen to α = 2 and β = γ = δ = 1" | Sec. 2.3.3, p. 6 |
| Perdidas | "f ∈ {MAE, MSE, Sobel, SSIM}" | Sec. 2.3.3, p. 6 |
| Aumentacion | "random brightness- and contrast-scaling as well as ... Poisson noise" | Sec. 2.3.3, p. 6 |
| Metricas | "structural similarity index measure (SSIM) as well as the peak signal-to-noise ratio (PSNR)" | Sec. 2.5, p. 7 |
| Comparadores | "compared against the LI-based inpainting method, used by ... fsMAR" | Sec. 2.5, p. 7 |
| Segmentacion comun | "the same consistent 2D segmentation maps ... are used for all methods" | Sec. 2.5, p. 7 |
| GT con metal reinsertado | "metal injection ... is also performed on the metal-free GT reconstruction" | Sec. 2.5, p. 7 |
| ROI | "region of interest (ROI) evaluation comprising those anatomical relevant regions" | Sec. 2.5, p. 7-8 |
| Clinico solo cualitativo | "this evaluation can only be done qualitatively" | Sec. 2.5, p. 8 |
| NoMAR macromedia | "macromeans of 0.9923 and 56.19 dB, respectively" | Sec. 3.1, p. 8 |
| LI+fs macromedia | "LI+fs reaches macromean SSIM and PSNR scores of 0.9971 and 60.42 dB" | Sec. 3.1, p. 8 |
| PConv+fs macromedia | "PConv+fs achieves ... SSIM and PSNR scores of 0.9967 and 60.32 dB" | Sec. 3.1, p. 8 |
| Propuesto macromedia | "proposed DL-inpainting yields slightly higher macromean SSIM scores of 0.9974 and 60.99 dB" | Sec. 3.1, p. 8 |
| Max. diferencia por corte | "SSIM scores increased by up to 0.0094 and PSNR ... up to 6.7 dB" | Sec. 3.1, p. 8 |
| Abstract: hasta 6 dB | "outperform the other methods by up to 6 dB on single slices" | Abstract, p. 1 |
| Tabla 1: max. diferencia media | Fila "Ø": Max Diff. SSIM 0.0006, PSNR 1.3193 | Tabla 1, p. 8 |
| Excepciones | "TS 2 and 3 being the only exceptions for which both scores ... are lower" | Sec. 3.1, p. 8 |
| SSIM = 1 imposible | "makes it impossible to reach an SSIM score of 1" | Sec. 3.1, p. 8 |
| ROI: mejora PSNR | "Increases of up to 3.5 dB in terms of PSNR" | Sec. 3.1, p. 10 |
| Clinico: tipo de implante | "comprising Pedicle screws with their associated towers for minimally invasive spine surgery" | Sec. 3.2, p. 11 |
| Clinico: sin fs | "the fs-step is omitted in these cases" | Sec. 3.2, p. 11 |
| Ablacion con/sin mapa de longitud | NO ENCONTRADO EN EL PDF | — |
| Mejora atribuida al mapa en cifras | NO ENCONTRADO EN EL PDF | — |
| Dependencia del mapa (cualitativa) | "the network relies heavily on the given metal path length information" | Sec. 4, p. 13 |
| Error de estimacion | "can consequently vary between an under- or overestimation" | Sec. 4, p. 13 |
| Efecto de sobreestimar | "the inpainting regions appear too dark or comprise a dark outline" | Sec. 4, p. 13 |
| Alternativa CAD/malla (no implementada) | "using for example 3D meshes as a basis, the accurate metal path length is available" | Sec. 4, p. 12-13 |
| Tamanos manejables | "projection image sizes of around 1000² pixels, and reconstruction volume sizes of 512³" | Sec. 4, p. 11 |
| Trabajo futuro | "possible improvements to the estimated metal path length information" | Sec. 5, p. 13 |
| Financiacion | "ERC grant no. 810316" | Agradecimientos, p. 13 |
