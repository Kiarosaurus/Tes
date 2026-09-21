# an2025generalization — On Inductive Biases That Enable Generalization in Diffusion Transformers

- **DOI / URL:** 10.52202/085713-1066; https://proceedings.neurips.cc/paper_files/paper/2025/file/2dc52e27a26afabb0bf2123bceaf9208-Paper-Conference.pdf (`refs/raw/an2025generalization.bib`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/an2025generalization.pdf (NeurIPS 2025; 20 páginas: artículo y checklist; los apéndices A–J citados no están incluidos)

## Que hace (3 lineas maximo)
Compara generalización de denoisers DiT y U-Net en espacio de píxeles, identifica localidad temprana de atención como sesgo de DiT y la fuerza con ventanas locales. Evalúa PSNR gap y calidad generativa en varios conjuntos naturales.

## Restriccion o supuesto clave
Los experimentos son sobre imágenes naturales 32 × 32, sin autoencoder, y miden generalización principalmente mediante brecha de PSNR de denoising. CT, pelvis, metal, implantes, condicionamiento, inpainting y preservación fuera de máscara son **NO ENCONTRADO EN EL PDF**. U-Net y DiT se igualan en FLOPs, pero no en parámetros (109.55 M frente a 14.27 M), y los apéndices con detalles/limitaciones no vienen en el archivo.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Regímenes escasos: 10³ y 10⁴ imágenes | "when trained with less data, e.g., N=10³ and N=10⁴" | Sec. 2.1, p. 4 |
| U-Net: 303.17 Gflops, 109.55 M parámetros | "UNet, FLOPs: 303.17G; Params: 109.55M" | Fig. 3, p. 5 |
| DiT: 300.49 Gflops, 14.27 M parámetros | "DiT, FLOPs: 300.49G; Params: 14.27M" | Fig. 3, p. 5 |
| 400 mil pasos | "the same 400k training steps" | Sec. 3.1, p. 8 |

## Donde entra en mi tesis
Es la única fuente de este bloque que compara directamente DiT y U-Net. Su hallazgo contradice el argumento simple de #106: *"a DiT has a remarkably smaller PSNR gap than a UNet"* con pocos datos (Sec. 2.1, p. 4), usando FLOPs equivalentes. Además muestra que ventanas locales tempranas reducen la brecha y suelen mejorar FID en el régimen de 10⁴ imágenes (Sec. 3.1, p. 8). Autoriza a afirmar que la localidad es un sesgo útil y que también puede incorporarse a DiT; **no** autoriza a trasladar la ventaja a CT pélvica 256 × 256, inpainting condicionado o síntesis de metal. En consecuencia, U-Net debe justificarse por alineación con la implementación y precedentes médicos, no por una supuesta superioridad en pocos datos.

## Dudas para el asesor
- ¿Registrar como limitación explícita que una comparación U-Net–DiT no se realizó y que evidencia reciente incluso favorece DiT bajo una métrica de generalización en imágenes naturales?
- La referencia de Peebles y Xie aparece como “CVPR 2023” en p. 12, pero el PDF/raw local de DiT dicen ICCV 2023; no reutilizar esa cita secundaria.
