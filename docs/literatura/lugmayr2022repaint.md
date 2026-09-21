# lugmayr2022repaint — RePaint: Inpainting Using Denoising Diffusion Probabilistic Models

- **DOI / URL:** DOI / URL del artículo: NO ENCONTRADO EN EL PDF ni en `refs/raw/lugmayr2022repaint.bib`; repositorio indicado en el PDF: http://git.io/RePaint
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/lugmayr2002repaint.pdf (11 páginas, pp. 11461–11471; el suplemento referido en el texto no está incluido; el nombre local dice 2002, pero PDF y raw dicen 2022)

## Que hace (3 lineas maximo)
Convierte un DDPM incondicional preentrenado en método de inpainting sin reentrenarlo para máscaras. En cada paso combina píxeles conocidos muestreados desde la entrada con la región desconocida generada, y usa saltos de remuestreo para armonizar ambas regiones.

## Restriccion o supuesto clave
Se evalúa en imágenes naturales 2D de CelebA-HQ e ImageNet, a 256 × 256. CT, HU, metal, implantes rígidos, pelvis, coherencia 3D y física de adquisición son **NO ENCONTRADO EN EL PDF**. En máscaras extremas puede producir completaciones realistas “very different from the Ground Truth image” (Sec. 6, p. 11468); realismo semántico no equivale a fidelidad anatómica o cuantitativa.

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Imágenes de 256 × 256 | “We use 256 × 256 crops” | Sec. 5.1, p. 11466 |
| 250 pasos de difusión en su configuración final | “we use T = 250 timesteps” | Sec. 5.1, p. 11466 |
| 10 remuestreos y salto de longitud 10 | “r = 10 times resampling with jumpy size j = 10” | Sec. 5.1, p. 11466 |
| Saturación aproximada en 10 remuestreos | “benefit saturates at about n = 10 resamplings” | Fig. 3, p. 11465 |

## Donde entra en mi tesis
Es el antecedente metodológico del inpainting por difusión. La Fig. 2 y la Ec. 8 separan la región conocida, muestreada desde la entrada, de la región desconocida, muestreada desde el DDPM, y las recomponen con una máscara en cada iteración. Además, RePaint “goes forward and backward in diffusion time” (Introducción, p. 11462) para dar al modelo más oportunidades de armonizar el borde. Esto respalda el principio de condicionar por contexto y estudiar costuras en el borde de `G = M ∪ B_delta`.

No autoriza a afirmar que la implementación de la tesis sea RePaint: esta entrena un denoiser condicionado y copia el CT fuera de `G`, mientras RePaint reutiliza un DDPM incondicional y altera solo el muestreo. Tampoco prueba conservación de HU, continuidad clínica del borde, generación de streaking exterior al metal ni suficiencia de `B_delta`. Sus hiperparámetros `T=250`, `r=10`, `j=10` no se transfieren automáticamente al sampler de la tesis.

## Dudas para el asesor
- ¿Citar RePaint como ancestro del mecanismo de inpainting y LeFusion como precedente médico más cercano?
- ¿La implementación incorpora remuestreo tipo RePaint o solo composición enmascarada? No deben presentarse como equivalentes.

