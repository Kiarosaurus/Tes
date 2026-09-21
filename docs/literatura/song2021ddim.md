# song2021ddim — Denoising Diffusion Implicit Models

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF ni en `refs/raw/song2021ddim.bib`; URL: https://openreview.net/forum?id=St1giarCHLP
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/song2021ddim.pdf (20 páginas; incluye los Apéndices A–D)

## Que hace (3 lineas maximo)
Introduce DDIM como una familia de procesos generativos no markovianos que conserva el objetivo de entrenamiento de DDPM. Permite muestreo determinista con η = 0 y trayectorias abreviadas sin reentrenar el modelo.

## Restriccion o supuesto clave
Los experimentos son generación de imágenes naturales: “CIFAR10 (32 × 32, unconditional), CelebA (64 × 64)” y LSUN (Apéndice D.1, p. 16); la arquitectura heredada “is a U-Net” basada en Wide ResNet (misma sección y página). CT, pelvis, unidades Hounsfield, implantes metálicos, inpainting local, condicionamiento por máscara y preservación fuera de la ROI son **NO ENCONTRADO EN EL PDF**. Los resultados con 50 pasos no demuestran eficacia clínica ni validan la configuración completa de la tesis.

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| η = 0 define el caso DDIM | “DDIM when η = 0” | Sec. 5, p. 6 del PDF |
| T = 1000 en los modelos evaluados | “same trained model with T = 1000” | Sec. 5, p. 6 del PDF |
| 50 pasos figura entre las trayectorias evaluadas, incluida η = 0 | “S 10 20 50 100 1000” | Tabla 1, p. 7 del PDF |
| Aceleración reportada de 10× a 50× | “10× to 50× faster in terms of wall-clock time” | Resumen, p. 1 del PDF |

## Donde entra en mi tesis
Es la fuente primaria para justificar el **muestreador DDIM** y la elección explícita de η = 0. La Tabla 1 evalúa 50 pasos con η = 0 en CIFAR-10 y CelebA, y la Tabla 3 hace lo propio en LSUN; esto autoriza a presentar 50 pasos como una configuración estudiada en imágenes naturales, no como óptima ni validada para CT pélvica con metal. El paper mantiene el mismo entrenamiento DDPM y cambia la trayectoria de muestreo, por lo que respalda separar entrenamiento y sampler.

La transferencia a la implicancia #106 es parcial: el Apéndice D.1 confirma que el denoiser usado es una U-Net, pero no compara U-Net contra DiT. Además, la selección de la subsecuencia no es única: usa espaciado cuadrático en CIFAR-10 y lineal en los demás conjuntos (Apéndice D.2, p. 17). Combinar DDIM a 50 pasos y η = 0 con el schedule coseno de Nichol–Dhariwal es una decisión de implementación entre trabajos; esa combinación exacta es **NO ENCONTRADO EN EL PDF**.

## Dudas para el asesor
- ¿Documentar explícitamente si la implementación usa subsecuencia lineal, cuadrática u otra regla para los 50 pasos?
- ¿Presentar η = 0 y 50 pasos como hiperparámetros adoptados, evitando atribuirles validación en CT o superioridad arquitectónica?
