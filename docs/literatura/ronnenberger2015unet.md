# ronnenberger2015unet — U-Net: Convolutional Networks for Biomedical Image Segmentation

- **DOI / URL:** 10.1007/978-3-319-24574-4_28 (impreso en el PDF, p. 234)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/ronnenberger2015unet.pdf (LNCS 9351, pp. 234–241; 8 páginas)

## Que hace (3 lineas maximo)
Introduce una red completamente convolucional con ruta contractiva y ruta expansiva simétrica para segmentación biomédica. Combina características de alta resolución del encoder con el decoder y usa aumentación intensa para entrenar con pocas imágenes anotadas.

## Restriccion o supuesto clave
Es segmentación supervisada de microscopía, no síntesis, difusión, CT ni inpainting. Sus skip connections concatenan mapas recortados para localizar píxeles; el paper no estudia continuidad de intensidad, costuras en una máscara generativa, HU, metal o implantes. Por tanto, no demuestra que las conexiones de salto preserven exactamente el exterior de `G` ni que U-Net supere a DiT.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 30 imágenes de entrenamiento (EM) | "The training data is a set of 30 images" | Sec. 4, p. 239 |
| 23 capas convolucionales | "the network has 23 convolutional layers" | Sec. 2, p. 237 |

## Donde entra en mi tesis
Fuente arquitectónica original para la ruta contractiva/expansiva: *"contracting path to capture context and a symmetric expanding path"* (Abstract, p. 234) y para la concatenación de alta resolución: *"a concatenation with the correspondingly cropped feature map"* (Sec. 2, p. 237). También documenta entrenamiento *"end-to-end from very few images"* (Abstract, p. 234), pero ese resultado depende de aumentación elástica y tareas de microscopía. Autoriza a explicar el origen del sesgo local y multiescala de U-Net; no autoriza una conclusión sobre difusión médica ni sobre U-Net frente a DiT.

## Dudas para el asesor
- ¿Mantener esta cita solo como origen de U-Net, detrás de DDPM/ADM y de los precedentes médicos directos?
