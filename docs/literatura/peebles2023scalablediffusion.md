# peebles2023scalablediffusion — Scalable Diffusion Models with Transformers

- **DOI / URL:** 10.1109/ICCV51070.2023.00387 (`refs/raw/peebles2023scalablediffusion.bib`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/peebles2023scalablediffusion.pdf (ICCV 2023, pp. 4195–4205 en el PDF; 11 páginas)

## Que hace (3 lineas maximo)
Introduce DiT: reemplaza la U-Net de un modelo de difusión latente por un Vision Transformer sobre parches latentes. Estudia escalado por profundidad, anchura y número de tokens, y evalúa síntesis condicionada por clase en ImageNet.

## Restriccion o supuesto clave
El experimento usa el VAE preentrenado de Stable Diffusion, imágenes RGB de ImageNet, millones de pasos y TPU v3-256. No evalúa CT en píxeles, pocos pacientes, inpainting local, máscaras, HU, metal ni preservación anatómica. Aunque afirma que DiT puede aplicarse a píxeles, esa variante no se experimenta aquí.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Latente 32 × 32 × 4 para imagen 256 × 256 | "z has shape 32 × 32 × 4" | Sec. 3.2, p. 4198 |
| Backbone máximo de 118.6 Gflops | "high-capacity backbone (118.6 Gflops)" | Sec. 1, p. 4196 |
| 7 millones de pasos para DiT-XL/2 | "DiT-XL/2, for 7M steps" | Sec. 5.1, p. 4202 |

## Donde entra en mi tesis
Control adversarial obligatorio de #106. El paper reemplaza la U-Net *"with a transformer that operates on latent patches"* (Abstract, p. 4195) y sostiene que *"the U-Net inductive bias is not crucial"* (Sec. 1, p. 4196) en su benchmark. Corrige el argumento de complejidad: para 256 × 256, DiT atiende tokens derivados de un latente 32 × 32, no 65,536 píxeles. Sí compara DiT con resultados publicados de U-Nets (ADM/LDM) y los supera en ImageNet, pero no controla simultáneamente dominio, autoencoder, datos y cómputo para la tarea de la tesis. No autoriza a afirmar que DiT sería mejor en CT pélvica ni que U-Net sea obsoleta; sí obliga a presentar U-Net como elección pragmática no comparada.

## Dudas para el asesor
- ¿Eliminar de la defensa el descarte de DiT por atención cuadrática sobre píxeles y conservar solo las restricciones verificadas de dominio, preentrenamiento y alcance experimental?
- `refs/raw` registra pp. 4172–4182, mientras el PDF local imprime pp. 4195–4205; requiere verificación bibliográfica sin corregir el raw.
