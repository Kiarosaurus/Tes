# kadkhodaie2024generalization — Generalization in Diffusion Models Arises from Geometry-Adaptive Harmonic Representations

- **DOI / URL:** DOI: **NO ENCONTRADO EN EL PDF** ni en `refs/raw/kadkhodaie2024generalization.bib`; https://proceedings.iclr.cc/paper_files/paper/2024/file/cbaf319a4712385b5ba8a414808b5713-Paper-Conference.pdf
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/kadkhodaie2024generalization.pdf (25 páginas; artículo ICLR 2024 y apéndices A–E)

## Que hace (3 lineas maximo)
Relaciona el error de denoising con el error de densidad y estudia cuándo denoisers entrenados en subconjuntos disjuntos convergen a funciones similares. Interpreta su Jacobiano como shrinkage en bases armónicas adaptadas a la geometría (GAHB) y prueba ese sesgo en imágenes naturales y clases sintéticas.

## Restriccion o supuesto clave
La evidencia usa denoisers **bias-free**, ciegos al nivel de ruido, entrenados con ruido gaussiano i.i.d. y MSE sobre CelebA/LSUN reducidos o imágenes sintéticas. La U-Net analizada tiene tres escalas, ReLU, batch normalization sin sesgo y 7.6 M de parámetros; su mapeo es localmente lineal porque no contiene constantes aditivas. La U-Net real del proyecto es otra arquitectura: cuatro escalas, bloques residuales GroupNorm–SiLU, condicionamiento temporal, atención, 11 canales de entrada, tres de salida y sesgos entrenables. Por ello, la descomposición local del paper no se transfiere automáticamente. CT, HU, pelvis, metal, implantes, inpainting en `G`, `B_delta` y comparación con DiT son **NO ENCONTRADO EN EL PDF**. Los autores además reconocen: “do not provide a formal mathematical definition of the class of GAHBs” (Discusión, p. 9).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Régimen principal de generalización: `N = 10^5` imágenes | “At N = 10^5, test and train PSNR are essentially identical” | Fig. 1, p. 4 |
| U-Net experimental de 7.6 M de parámetros | “The total number of parameters is 7.6m” | Apéndice A.1, p. 12 |
| Imágenes naturales principales de 80 × 80 | “downsampled to 80 × 80 resolution” | Apéndice A.1, p. 12 |
| Entrenamiento durante 1000 épocas | “Training is carried out on batches of size 512, for 1000 epochs” | Apéndice A.1, p. 12 |
| BF-CNN: 20 000 imágenes de 32 × 32 | “N = 20,000 images down-sampled to size 32 × 32” | Fig. 13, p. 16 |

## Donde entra en mi tesis
Entra, si se conserva, como contexto teórico muy acotado para #106: aporta una explicación posible de cómo denoisers convolucionales pueden explotar contornos y regiones regulares. El hallazgo central es empírico y dependiente de arquitectura/datos: dos modelos sobre subconjuntos disjuntos se aproximan cuando hay suficientes imágenes, y la cantidad necesaria depende de resolución, complejidad y capacidad (Discusión, p. 9; Fig. 15, p. 17).

No permite presentar los 17 149 parches correlacionados de 47 pacientes como equivalentes a 17 149 imágenes independientes, ni inferir que el renderizador ya generaliza. Tampoco permite llamar localmente lineal a la U-Net del proyecto: SiLU, normalizaciones afines, sesgos, atención y condicionamiento temporal rompen la construcción exacta analizada. Finalmente, el paper no compara U-Net con DiT y, por tanto, **no respalda superioridad U-Net–DiT**; la elección vigente sigue siendo pragmática y no comparada. A lo sumo motiva un control local de memorización o estabilidad entre particiones, no una modificación de arquitectura ni una métrica para E-A1–E-A4.

## Dudas para el asesor
- ¿Vale la pena citar esta explicación teórica en una sola frase, con la salvedad de que la red analizada no es la U-Net implementada?
- ¿Añadir un control de vecino más cercano o de estabilidad entre semillas para detectar memorización, sin tratar `N = 10^5` como umbral transferible?
- Si se discute U-Net frente a DiT, ¿mantener esta fuente solo como mecanismo convolucional y usar la comparación directa de `an2025generalization` como control adversarial?

