# lyu2021ududonet — U-DuDoNet: red dual-dominio no pareada para MAR en CT

- **DOI / URL:** https://doi.org/10.1007/978-3-030-87231-1_29 (MICCAI 2021, LNCS 12906, pp. 296–306; p. 296)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/lyu2021ududonet.pdf

## Que hace (3 lineas maximo)
Red de reduccion de artefactos metalicos (MAR) entrenada con datos no pareados: estima componentes aditivos del artefacto en sinograma (S-Net, guiada por una red de inpainting P-Net) y en imagen (I-Net).
Para entrenar sin pares, suma esos componentes a una CT limpia (I^ca = I^c + a_S + a_I) y exige poder volver a quitarlos (ciclo + consistencia de artefacto).
Justifica la suma con una derivacion de que el artefacto es aditivo y depende solo de la imagen de metal X^m(E) (Sec. 2, Ec. 3).

## Restriccion o supuesto clave
Si genera artefactos en la direccion limpio -> con metal, pero solo como paso auxiliar del entrenamiento ciclico de MAR, no como producto que se evalue. El artefacto que se suma a la CT limpia es el que se estimo de otra imagen real con metal (a_S, a_I salen de I^a), no se genera a partir de una geometria ni una pose de implante que uno elija: "we can create a plausible artifact-affected CT I^ca by adding the artifact term" (Sec. 2, p. 298); "I^ca = I^c + a_S + a_I" (Sec. 3, p. 298). Ademas:
- La aditividad vale solo bajo "mild assumptions" (p. 297): se supone que la atenuacion del tejido normal es "almost constant with respect to E" (p. 298). Esto no cubre explicitamente hueso denso alrededor del tornillo.
- El trabajo es 2D, por cortes (los conjuntos se cuentan en "images", p. 301). Volumetria 3D: NO ENCONTRADO EN EL PDF.
- El dato clinico es de columna (SpineWeb; "two rods on each side of the spinous process", p. 302). CT pelvica / tornillos de osteosintesis: NO ENCONTRADO EN EL PDF.
- En datos clinicos la evaluacion es solo visual (Fig. 3). Metricas cuantitativas clinicas: NO ENCONTRADO EN EL PDF.
- Nunca se evalua el realismo de las imagenes sinteticas I^ca. Solo se reportan PSNR/SSIM de la imagen corregida.

Por todo lo anterior no sirve tal cual para implantes en CT pelvica real: no controla donde ni como va el implante, el artefacto se toma de otro paciente sin coherencia anatomica, es 2D y no se valida en pelvis.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

(Posible uso conceptual: la derivacion aditiva de la Ec. 3 como respaldo teorico del canal analitico T. Lo decide la autora.)

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| PSNR/SSIM 34.54/0.934 (U-DuDoNet, simulacion) | "U-DuDoNet (ours) 34.54/0.934" | Tabla 1, Sec. 4.1, p. 301 |
| +0.73 dB frente a ADN | "an improvement of 0.73 dB in PSNR compared with ADN" | Sec. 4.2, p. 302 |

## Donde entra en mi tesis
- Cap. 2 (estado del arte / brecha): ejemplo de sintesis aprendida de artefactos (limpio -> con metal) usada como medio para MAR no pareado, no como fin.
- Justificacion del canal T: la Ec. 3 (I^a = I^ac + F(X^m(E))) separa un termino de artefacto que depende solo del metal. Es la misma premisa que calcular T desde la mascara de metal (proyeccion + no linealidad + FBP).
- Uso de la proyeccion de la mascara: aqui la traza del metal M_t = δ(P(M)) solo delimita la region del sinograma que se inpinta o se corrige. No se usa como prior fisico para generar el artefacto.

## Dudas para el asesor
1. La brecha del cap. 2 ("sintesis aprendida de artefactos locales poco explorada") debe reformularse? U-DuDoNet (y ADN [14] y RCN [26], segun su Sec. 1, p. 297) ya sintetizan artefactos de forma aprendida sobre CT limpias. Propuesta de matiz: lo que falta es una sintesis condicionada por la geometria y la pose del implante, en 3D/2.5D, anatomicamente coherente y evaluada como producto. En estos trabajos la sintesis es un paso intermedio del MAR que nunca se evalua.
2. La derivacion aditiva (Sec. 2) puede citarse como respaldo teorico del canal T, aunque su supuesto ("almost constant with respect to E", p. 298) excluye en la practica al hueso cortical denso?
3. Candidatos de snowballing, sin registrar (este extractor solo escribe la ficha): ADN (Liao et al., ref. [14], TMI 2019), RCN (Zhao et al., ref. [26], 2020), Zhang & Yu (ref. [25], TMI 2018, metodo de simulacion de artefactos usado aqui), Lyu et al. 2020 (ref. [18], codificacion de la proyeccion de la mascara de metal).

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Aditividad (supuesto) | "we prove metal artifacts are inherently additive up to mild assumptions" | Sec. 2, p. 297 |
| Supuesto sobre el tejido normal | "attenuation coefficient of normal body tissue is almost constant with respect to E" | Sec. 2, p. 298 |
| Causa del artefacto | "Metal artifacts appear mainly because of beam hardening." | Sec. 2, p. 298 |
| Descomposicion | "X^a(E) = X^ac + X^m(E). Often X^m(E) is locally constrained." | Sec. 2, Ec. 2, p. 298 |
| Termino de artefacto | "the second term introduces streaky and band artifacts, which is a function of X^m(E)" | Sec. 2, Ec. 3, p. 298 |
| Sintesis limpio -> metal | "create a plausible artifact-affected CT I^ca by adding the artifact term" | Sec. 2, p. 298 |
| Sintesis en el metodo (Fase II) | "I^ac = I^a − a_S − a_I, I^ca = I^c + a_S + a_I" | Sec. 3, p. 298 |
| Dominio sinograma por proyeccion | "acquire metal corrupted sinograms (S^a and S^ca) by forward projecting" | Sec. 3.1, p. 299 |
| Traza de metal (proyeccion de mascara) | "M_t denotes a binary metal trace, M_t = δ(P(M))" | Sec. 3.1, p. 299 |
| P-Net (prior) | "P-Net is an inpainting net ... treats the metal-affected area in sinogram as missing" | Sec. 3.1, p. 299 |
| Entrenamiento de P-Net | "we artificially inject masks into clean sinograms S_c" | Sec. 3.1, p. 299 |
| S-Net | "φ_S represents a U-Net [20] of depth 2" | Sec. 3.1, Ec. 4, p. 299 |
| Prediccion limitada a la traza | "sinogram prediction is limited to the M_t region" | Sec. 3.1, p. 299 |
| I-Net | "Let φ_I denote I-Net, which is a 5-depth U-Net." | Sec. 3.1, p. 299 |
| Perdida de ciclo | "We use L1 loss to minimize the distance" | Sec. 3.2, Ec. 7, p. 300 |
| Consistencia de artefacto | "artifact components estimated from I^a and I^ca should be the same" | Sec. 3.2, Ec. 8, p. 300 |
| Adversarial | "we adopt PatchGAN [9] as discriminators D^a and D^c" | Sec. 3.2, p. 300 |
| Canal Sobel | "add gradient image generated by Sobel operator" | Sec. 3.2, p. 300 |
| Peso L_adv | "empirically set the weight of L_adv to 1" | Sec. 3.2, p. 300 |
| Pesos L_prior, L_art y resto | "weights of L_prior, L_art to 10, and the weights of the other losses to 100" | Sec. 3.2, p. 300 |
| σ_s = 1, σ_i = 3 | "We set σ_s to 1 and σ_i to 3 in L_prior." | Sec. 3.2, p. 300 |
| Simulacion de artefactos | "we generate images with metal artifacts using the method in [25]" | Sec. 4.1, p. 301 |
| DeepLesion entrenamiento: 3,984 imagenes, 90 mascaras | "we randomly choose 3,984 clean images combining with 90 metal masks for training" | Sec. 4.1, p. 301 |
| DeepLesion prueba: 200 imagenes, 10 mascaras | "additional 200 clean images combining with 10 metal masks for testing" | Sec. 4.1, p. 301 |
| Particion no pareada | "split 3,984 images into two groups" | Sec. 4.1, p. 301 |
| Clinico entrenamiento: 6,146 / 21,002 | "6,146 images with artifacts and 21,002 clean images for training from SpineWeb" | Sec. 4.1, p. 301 |
| Clinico prueba: 124 | "Additional 124 images with metal are used for testing." | Sec. 4.1, p. 301 |
| FP/FBP diferenciables | "differential FP and FBP operators with ODL library [1]" | Sec. 4.1, p. 301 |
| 50 epocas, Adam, lr 1e-4, batch 2 | "train the model for 50 epochs using an Adam optimizer ... 1 × 10^-4" | Sec. 4.1, p. 301 |
| Clinico: 20 epocas | "we train another model using unpaired images for 20 epochs" | Sec. 4.1, p. 301 |
| Umbral de mascara de metal: 2,500 HU | "metal mask is segmented with a threshold of 2,500 HU" | Sec. 4.1, p. 301 |
| Metricas | "We use peak signal-to-noise ratio (PSNR) and structural similarity index (SSIM)" | Sec. 4.1, p. 301 |
| Prueba estadistica (p < 0.001; d de Cohen) | "paired t-test (*** indicates p<0.001) and the effect size are measured by Cohen's d" | Tabla 1, p. 301 |
| Metal (sin corregir) 27.23/0.692 | "Metal - 27.23/0.692" | Tabla 1, p. 301 |
| DuDoNet 36.95/0.927; d 1.33/0.31 | "DuDoNet [17] 36.95/0.927 ***/*** 1.33/0.31" | Tabla 1, p. 301 |
| DuDoNet++ 37.65/0.953; d 2.93/1.51 | "DuDoNet++ [18] 37.65/0.953 ***/*** 2.93/1.51" | Tabla 1, p. 301 |
| DSCIP 29.22/0.624; d 4.65/5.32 | "DSCIP [24] 29.22/0.624 ***/*** 4.65/5.32" | Tabla 1, p. 301 |
| DAN-Net 39.73/0.944; d 3.83/1.58 | "DAN-Net [22] 39.73/0.944 ***/*** 3.83/1.58" | Tabla 1, p. 301 |
| RCN 32.98/0.918; d 1.26/1.19 | "RCN [26] 32.98/0.918 ***/*** 1.26/1.19" | Tabla 1, p. 301 |
| ADN 33.81/0.926; d 0.54/0.51 | "ADN [14] 33.81/0.926 ***/*** 0.54/0.51" | Tabla 1, p. 301 |
| U-DuDoNet 34.54/0.934 | "U-DuDoNet (ours) 34.54/0.934" | Tabla 1, p. 301 |
| +0.73 dB frente a ADN | "an improvement of 0.73 dB in PSNR compared with ADN" | Sec. 4.2, p. 302 |
| Ventanas de visualizacion | "display window are [-200, 600] and [-300, 300] HU" | Fig. 2, p. 302 |
| Caso de Fig. 2 (PSNR/SSIM) | "Corrupted CT 23.36/0.442 ... Ours 33.46/0.925" | Fig. 2, p. 302 |
| Caso de Fig. 2, otros metodos | "DuDoNet 35.48/0.921, DuDoNet++ 34.98/0.934, DSCIP 27.73/0.533, DAN-Net 37.14/0.893" | Fig. 2, p. 302 |
| Caso de Fig. 2, no supervisados | "RCN 30.24/0.868 ADN 30.47/0.869" | Fig. 2, p. 302 |
| Datos clinicos: anatomia | "clinical CT image with two rods on each side of the spinous process" | Sec. 4.2, p. 302 |
| Supervisados no generalizan | "DuDoNet++, DSCIP, and DAN-Net do not generalize to clinical data" | Sec. 4.2, p. 303 |
| Ablacion M1 32.97/0.927; d 1.45/0.76 | "M1 (Image Domain) 32.97/0.927 ***/*** 1.45/0.76" | Tabla 2, p. 303 |
| Ablacion M2 33.30/0.930; d 1.70/0.71 | "M2 (Dual-domain) 33.30/0.930 ***/*** 1.70/0.71" | Tabla 2, p. 303 |
| Ablacion M3 34.54/0.934 | "M3 (Dual-domain + prior) 34.54/0.934" | Tabla 2, p. 303 |
| Ganancia dual-dominio: 0.33 dB | "Dual-domain learning increases the PSNR by 0.33 dB" | Sec. 4.3, pp. 303–304 |
| Caso de Fig. 4 | "Corrupted CT 26.62/0.691 M1 32.85/0.928 M2 34.32/0.932 M3(full) 35.11/0.935" | Fig. 4, p. 304 |
| Evaluacion cuantitativa en datos clinicos | NO ENCONTRADO EN EL PDF | — |
| Evaluacion del realismo de las imagenes sinteticas I^ca | NO ENCONTRADO EN EL PDF | — |
| CT pelvica / tornillos | NO ENCONTRADO EN EL PDF | — |
| Procesamiento 3D volumetrico | NO ENCONTRADO EN EL PDF | — |
| Geometria del haz y parametros de proyeccion (n.º de vistas, detectores) | NO ENCONTRADO EN EL PDF | — |
