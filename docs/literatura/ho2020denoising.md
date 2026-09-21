# ho2020denoising — Denoising Diffusion Probabilistic Models

- **DOI / URL:** DOI del artículo: NO ENCONTRADO EN EL PDF ni en `refs/raw/ho2020denoising.bib`; código indicado en el PDF: https://github.com/hojonathanho/diffusion
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/ho2020denoising.pdf (12 páginas; el PDF remite detalles arquitectónicos al Apéndice B, que no está incluido)

## Que hace (3 lineas maximo)
Formula y evalúa DDPM: una cadena de Markov aprende a invertir un proceso gaussiano de ruido. Introduce la predicción de ruido con objetivo simplificado y demuestra síntesis incondicional en CIFAR-10, CelebA-HQ y LSUN.

## Restriccion o supuesto clave
La evidencia arquitectónica se limita a imágenes naturales: usa una U-Net tipo PixelCNN++ con normalización por grupos y atención a 16 × 16. CT, pelvis, metal, implantes, inpainting, condicionamiento por máscara y preservación fuera de una región son **NO ENCONTRADO EN EL PDF**. Por ello respalda el origen de la familia U-Net de difusión, pero no demuestra que sus conexiones de salto eviten costuras ni que U-Net sea superior a DiT en el régimen de la tesis.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 1000 pasos de difusión | "We set T = 1000 for all experiments" | Sec. 4, p. 5 del PDF |
| Atención en 16 × 16 | "self-attention at the 16 × 16 feature map resolution" | Sec. 4, p. 5 del PDF |

## Donde entra en mi tesis
Fuente primaria de la formulación DDPM y del precedente arquitectónico de `src/renderizador/`: *"use a U-Net backbone similar to an unmasked PixelCNN++"* y *"with group normalization throughout"* (Sec. 4, p. 5). Autoriza a describir la implementación como perteneciente a la familia DDPM con backbone U-Net residual, normalización por grupos y atención de baja resolución; **no** autoriza a llamarla réplica exacta porque el Apéndice B no está en el PDF y la tesis cambia datos, canales, condicionamiento, tamaño y tarea. No compara U-Net contra DiT: esa afirmación es **NO ENCONTRADO EN EL PDF**.

## Dudas para el asesor
- ¿Citar este trabajo solo para DDPM y la adopción temprana de U-Net, dejando la defensa U-Net/DiT como elección no medida?
- El planificador de este paper es lineal; no respalda el planificador coseno implementado.
