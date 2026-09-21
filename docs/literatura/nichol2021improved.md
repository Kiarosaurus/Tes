# nichol2021improved — Improved Denoising Diffusion Probabilistic Models

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF ni en `refs/raw/nichol2021improved.bib`; URL: https://proceedings.mlr.press/v139/nichol21a.html
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/nichol2021improved.pdf (10 páginas; pp. 8162–8171 de PMLR; no contiene apéndices)

## Que hace (3 lineas maximo)
Mejora DDPM mediante varianzas reversas aprendidas, un objetivo híbrido y un schedule coseno. Evalúa además muestreo abreviado y contrasta sus samplers con DDIM en CIFAR-10 e ImageNet 64 × 64.

## Restriccion o supuesto clave
La evidencia procede de imágenes naturales: “ImageNet 64 × 64” y “CIFAR-10” (Sec. 3, p. 8164), no de CT. Pelvis, unidades Hounsfield, implantes metálicos, inpainting, máscara de defecto y preservación anatómica local son **NO ENCONTRADO EN EL PDF**. Las ablaciones del schedule coseno usan T = 4000; no prueban automáticamente una implementación con T distinto, DDIM a 50 pasos y η = 0.

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Offset del schedule coseno s = 0.008 | “which gives s = 0.008” | Sec. 3.2, p. 8165 |
| Límite superior β_t = 0.999 | “clip βt to be no larger than 0.999” | Sec. 3.2, p. 8165 |
| T = 4000 en la ablación relevante | “For the remainder of this section, we use T = 4000” | Sec. 3, p. 8164 |
| 50 evaluaciones de red para su muestreo acelerado | “good samples with as few as 50 forward passes” | Introducción, p. 8162 |

## Donde entra en mi tesis
Es la fuente primaria del **schedule coseno**: la Ec. 16 define `ᾱ_t = f(t)/f(0)` con `f(t) = cos²(((t/T+s)/(1+s))·π/2)`, y luego obtiene β_t de cocientes sucesivos (Sec. 3.2, p. 8165). Los autores explican que busca añadir ruido más gradualmente que el schedule lineal en imágenes pequeñas, pero reconocen que escoger `cos²` fue arbitrario. Por tanto, fundamenta la fórmula y su motivación, no una necesidad teórica ni su desempeño en CT.

La afirmación de 50 *forward passes* corresponde al muestreo acelerado de su Improved DDPM con varianza aprendida; no fundamenta por sí sola **DDIM con η = 0**. En su comparación, DDIM fue mejor con menos de 50 pasos y peor con 50 o más bajo ese protocolo (Sec. 4, pp. 8167–8168); además, el stride cuadrático de Song perjudicó la calidad al combinarse con su schedule coseno (nota 1, p. 8168). La combinación exacta de schedule coseno, DDIM, η = 0, 50 pasos, U-Net y datos CT de la tesis es **NO ENCONTRADO EN EL PDF**. Tampoco compara U-Net contra DiT.

## Dudas para el asesor
- ¿Describir schedule coseno y DDIM como decisiones respaldadas por fuentes distintas, dejando explícito que su combinación exacta se valida experimentalmente en la tesis?
- ¿Mantener `s = 0.008` y el recorte de β_t o verificarlos como hiperparámetros de implementación antes de citarlos?
