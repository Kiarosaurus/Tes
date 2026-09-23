# konz2024anatomicallycontrollable — SegGuidedDiff

- **DOI / URL:** DOI o URL de publicacion **NO ENCONTRADO EN EL PDF ni en `refs/raw/konz2024anatomicallycontrollable.bib`**; codigo: https://github.com/mazurowski-lab/segmentation-guided-diffusion
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/konz2024anatomicallycontrollable.pdf (MICCAI 2024, LNCS 15007:88-98; 11 paginas)

## Que hace (3 lineas maximo)
SegGuidedDiff es un DDPM 2D en espacio de imagen, entrenado desde cero, que concatena una mascara anatomica multiclase al U-Net en cada paso. Introduce mask-ablated training para generar con clases omitidas y evalua fidelidad anatomica en MRI mamaria y CT cuello-pelvis frente a SPADE y ControlNet.

## Restriccion o supuesto clave
No es inpainting local: parte de ruido gaussiano y sintetiza la imagen completa; la mascara es condicion, no soporte de edicion. Por tanto, fuera de una clase concreta no copia ningun fondo y puede cambiar cualquier pixel; una garantia de preservacion exterior es **NO ENCONTRADO EN EL PDF**. Esto lo diferencia de LeFusion/CLAIM y del renderizador de la tesis, que recompone el CT fuente fuera de su region de generacion.

Para implantes, la mascara solo codifica clases anatomicas y el estudio *"did not consider full 3D generation"* (Conclusion, p. 96; PDF p. 9). CT se normaliza a [0,255], no a HU (Sec. 3, p. 93; PDF p. 6). Metal, implantes, pelvis o sacro como tarea, HU, beam hardening y streaking son **NO ENCONTRADO EN EL PDF**; tampoco hay una perdida que atribuya cambios exteriores a un objeto rigido.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| T = 1000 pasos | "we use T = 1000" | Sec. 1.1, p. 90 (PDF p. 3) |
| CT: 40 pacientes; split 24/8 | "Our second dataset is a 40-patient subset" | Sec. 2, p. 92 (PDF p. 5) |
| CT: aproximadamente 1,100/2,100 cortes 2D train/test | "results in a train/test split of ~1100/2100 2D slice images" | Sec. 2, p. 92 (PDF p. 5) |
| Fidelidad CT, Dice generado-mascara: 0.8980 | Tabla 1, CT Organ, Ours: "0.8980" | Tabla 1, p. 94 (PDF p. 7) |
| Entrada/salida a 256 x 256 y rango [0,255] | "resized to 256 x 256 and normalized to [0, 255]" | Sec. 3, p. 93 (PDF p. 6) |

## Donde entra en mi tesis
Related Work de condicionamiento espacial y arquitectura. Es el precedente mas cercano de una U-Net de difusion en espacio de imagen que recibe la mascara por concatenacion en cada paso y usa DDIM; por ello, la tesis no debe reclamar como novedosos esos componentes aislados. La diferencia defendible es funcional: SegGuidedDiff genera un corte completo desde ruido, sin CT fuente, mascara de region de generacion, copia exterior, HU ni 2.5D; el proyecto genera solo `G = M union B_delta`, conserva el exterior y condiciona por vecinos, mascara metalica y banda. Frente a LeFusion/CLAIM ocupa la familia global: puede alterar fuera de la mascara, pero no modela un efecto fisico causado por el objeto. No es baseline comparable por tarea, datos ni salida.

## Dudas para el asesor
- ¿Citarlo para dejar explicito que concatenar una mascara condiciona anatomia, pero no garantiza soporte espacial?
- ¿La cercania arquitectonica obliga a describir la novedad solo como la combinacion metal + multi-ventana + `B_delta` + copia exterior, nunca como U-Net de difusion condicionada?
- El PDF remite a un Apendice A con detalles de arquitectura que no esta incluido: ¿registrar el acceso como completo para el articulo, pero incompleto para los hiperparametros?
