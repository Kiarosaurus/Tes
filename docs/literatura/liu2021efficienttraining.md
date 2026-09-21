# liu2021efficienttraining — Efficient Training of Visual Transformers with Small Datasets

- **DOI / URL:** https://proceedings.neurips.cc/paper_files/paper/2021/file/c81e155d85dae5430a8cee6f2242e82c-Paper.pdf (`refs/raw/liu2021efficienttraining.bib`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/liu2021efficienttraining.pdf (13 páginas; el suplementario mencionado no está incluido)

## Que hace (3 lineas maximo)
Estudia transformers visuales en clasificación con conjuntos pequeños/medianos y propone una tarea autosupervisada de localización relativa densa. Compara CvT, Swin y T2T con ResNet-50, desde cero y por fine-tuning.

## Restriccion o supuesto clave
Es clasificación de imágenes naturales; no evalúa denoisers, difusión, U-Net, DiT, CT, metal ni inpainting. Además, sus mejores transformers incorporan localidad o convoluciones y pueden igualar a ResNet en varios conjuntos pequeños. Por ello solo sustenta que quitar sesgos convolucionales puede elevar la demanda de datos, no que una U-Net de difusión sea superior a un DiT.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 2,040 imágenes de entrenamiento (Flowers102) | "Oxford Flowers102 ... 2,040" | Tabla 1, p. 6 del PDF |
| 100 épocas desde cero | "trained from scratch on different datasets (100 epochs)" | Tabla 4, p. 8 del PDF |

## Donde entra en mi tesis
Evidencia indirecta y cuidadosamente acotada para el argumento de datos: *"lack of the typical convolutional inductive bias makes these models more data hungry"* (Abstract, p. 1). Sin embargo, el propio paper informa que *"VTs can match the ResNet accuracy when trained with small datasets"* (Sec. 1, p. 2) y que CvT resulta comparable a ResNet-50 (Sec. 5.2, p. 8). No compara U-Net con DiT ni generación con difusión. Autoriza a describir un **riesgo general** al entrenar transformers visuales sin sesgos locales desde cero; no autoriza a usarlo como prueba de superioridad de U-Net en la tesis.

## Dudas para el asesor
- ¿Omitir esta cita si la defensa arquitectónica cabe en una frase, para no trasladar evidencia de clasificación natural a difusión médica?
