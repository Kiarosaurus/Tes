# dhariwal2021diffusion — Diffusion Models Beat GANs on Image Synthesis

- **DOI / URL:** DOI / URL del artículo: NO ENCONTRADO EN EL PDF ni en `refs/raw/dhariwal2021diffusion.bib`
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/dhariwal2021diffusion.pdf (15 páginas; los apéndices citados en el cuerpo no están incluidos)

## Que hace (3 lineas maximo)
Realiza ablaciones de la U-Net de DDPM y propone ADM, con mejoras de profundidad/anchura, atención, remuestreo residual y normalización adaptativa. Añade guía por clasificador y evalúa síntesis natural incondicional y condicionada por clase.

## Restriccion o supuesto clave
Toda la evidencia procede de LSUN e ImageNet, no de CT ni de datos médicos. El condicionamiento principal es por clase y guía de un clasificador; la concatenación por canales solo se describe para un modelo de superresolución ajeno al renderizador. Metal, implantes, inpainting local, preservación anatómica fuera de máscara y comparación con DiT son **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 2 bloques residuales por resolución | "2 residual blocks per resolution" | Sec. 3, p. 4 del PDF |
| Atención en 32, 16 y 8 | "attention at 32, 16 and 8 resolutions" | Sec. 3, p. 4 del PDF |
| 64 canales por cabeza | "64 channels per head" | Sec. 3, p. 4 del PDF |

## Donde entra en mi tesis
Fuente primaria para justificar que ADM conserva una U-Net: *"Ho et al. adopted the UNet architecture for diffusion models"* (Sec. 3, p. 3), formada por capas residuales, convoluciones de down/up-sampling y conexiones de salto. Las ablaciones muestran que, en ImageNet 128 × 128, múltiples cabezas, atención multirresolución y bloques BigGAN mejoran acumulativamente el FID (Sec. 3, pp. 3–4). Esto respalda la **familia** U-Net residual con atención, no la configuración exacta de la tesis ni una ventaja en CT pélvica. No compara U-Net con DiT, y no autoriza a atribuir a ADM el condicionamiento por concatenación del renderizador.

## Dudas para el asesor
- ¿Presentar ADM como antecedente de diseño y no como arquitectura replicada?
- La guía por clasificador no está implementada en la tesis; conviene evitar que la cita sugiera lo contrario.
