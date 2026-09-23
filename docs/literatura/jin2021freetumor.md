# jin2021freetumor — Free-form tumor synthesis in CT via FRGAN

- **DOI / URL:** https://doi.org/10.1016/j.knosys.2021.106753 (`refs/raw/jin2021freetumor.bib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/jin2021freetumor.pdf (texto completo; 25 paginas)

## Que hace (3 lineas maximo)
Formula la sintesis libre de tumores en CT como inpainting 3D condicionado por una mascara. FRGAN combina un generador encoder-decoder con convoluciones gated/dilatadas, una rama multiescala para el borde, discriminador 3D por parches y perdidas adversarial, de contenido, tumor, borde, perceptual y estilo.

## Restriccion o supuesto clave
El objeto se modela como tumor de tejido blando con frontera incierta: *"indistinct and blurry boundaries"* (Sec. 2, p. 5). Ademas, recorta las entradas a ventanas cuyo maximo es 300/200/600 HU (Sec. 4.2, p. 12), por lo que no conserva el rango de un implante metalico. Metal, implantes, pelvis, beam hardening y streaking son **NO ENCONTRADO EN EL PDF**.

La sintesis no tiene soporte duro igual a la mascara. El generador produce el parche 3D completo y la perdida de contenido usa todo `G(x)`; ademas, `M_sb` *"represents the surrounding boundary region of M_st"* (Sec. 3.4.1, p. 9). No se encuentra una ecuacion que recomponga `(1-M)` con el CT original: **NO ENCONTRADO EN EL PDF**. Por ello, una modificacion fuera de la mascara tumoral es posible —aunque penalizada— y el paper optimiza deliberadamente la interfaz exterior inmediata. Esto no equivale a modelar un artefacto fisico peri-implante ni cuantifica una banda de generacion.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ventanas KiTS/LiTS/LUNA: [-200,300], [-100,200], [-1000,600] HU | "perform a global cut-off using HU windows" | Sec. 4.2, p. 12 |
| Parches volumetricos de 64 x 64 x 64 | "resampled to a fixed size of 64 x 64 x 64" | Sec. 4.2, p. 13 |
| Muestras KiTS/LiTS/LUNA: 1,356/2,344/2,748 | "there are 1,356/2,344/2,748 tumor samples" | Sec. 4.2, p. 13 |
| KiTS, U-Net: Dice 0.840 a 0.858 con FRGAN | Tabla 2: "Real" 0.840; "Real+FRGAN" 0.858 | Tabla 2, p. 16 |

## Donde entra en mi tesis
Related Work de sintesis local en CT y control espacial. Es un precedente anterior de encoder-decoder/GAN 3D que concatena imagen y mascara y aprende sobre parches volumetricos, pero no es equivalente a LeFusion o CLAIM: estos recomponen el fondo en cada paso, mientras FRGAN predice el parche completo y solo lo aproxima al original mediante `L_cw`. Su mascara de borde `M_sb` demuestra que una sintesis de lesion puede supervisar una vecindad exterior; por eso, la novedad no debe formularse como “ningun metodo toca fuera de la mascara”, sino como ausencia de una banda exterior explicita para artefactos de adquisicion metalicos. No colisiona con `B_delta`: no hay metal, alcance en milimetros, HU de alta atenuacion ni senal de streaking, y su borde sirve para fusionar tumor y tejido, no para representar propagacion fisica.

## Dudas para el asesor
- ¿Conviene citarlo junto a LeFusion/CLAIM para separar restriccion blanda del generador y copia dura del fondo?
- ¿La frase vigente sobre ausencia de cambios fuera del objeto debe decir especificamente “artefactos inducidos por el objeto” para no abarcar `M_sb`?
- El paper infiere realismo principalmente por segmentacion downstream y observacion visual; ¿basta como contexto si esa evaluacion esta fuera del alcance de la tesis?
