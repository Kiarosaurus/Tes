# wu2025freetumor — FreeTumor a gran escala para CT

- **DOI / URL:** https://arxiv.org/abs/2502.18519 (`refs/raw/wu2025freetumor.bib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wu2025freetumor.pdf (arXiv:2502.18519v1; texto completo y Extended Data; 53 paginas)

## Que hace (3 lineas maximo)
Entrena un generador U-Net 3D adversarial con datos CT etiquetados y no etiquetados; un segmentador y un clasificador actuan como discriminadores. Inserta tumores en linea dentro de mascaras sinteticas y descarta resultados que el segmentador no reconoce, para ampliar el entrenamiento downstream a gran escala.

## Restriccion o supuesto clave
La Ec. 1 impone soporte exactamente dentro de la mascara tumoral: *"other positions are reserved as the original values"* (Sec. 4.2, p. 20). Por construccion no puede generar streaking ni beam hardening fuera de `M`, salvo que esos efectos se incluyeran dentro de una mascara ampliada, posibilidad que el paper no define. Esta es la misma limitacion espacial de LeFusion/CLAIM, aunque aqui el generador es GAN/U-Net y aplica una transformacion residual sustractiva, no difusion.

Tambien presupone tumor de tejido blando y recorta abdomen a (-175,250) HU y torax a (-1000,500) HU (Tabla A19, p. 53), rangos incompatibles con metal. Metal, implantes, pelvis, unidades HU conservadas en la salida y artefactos metalicos son **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 161,310 CT de 33 fuentes; 2.3% con tumor anotado | "161,310 publicly available CT volumes from 33 different sources" | Sec. 2, p. 6 |
| Test visual: 13 radiologos, 90 casos | "provided 18 cases each" de cinco tipos | Sec. 2.1, p. 7 |
| Sensibilidad/exactitud media del lector: 51.1%/60.8% | Figura 2: "51.1" y "60.8" | Fig. 2d-e, p. 8 |
| Mejora media de Dice: +6.7 puntos | "average +6.7% Dice score improvements" | Sec. 2.2, p. 10 |
| Ventanas HU y crops 3D | "(-175, 250)" / "(96, 96, 96)" | Tabla A19, p. 53 |

## Donde entra en mi tesis
Related Work como el comparador conceptual mas reciente y mas grande para sintesis local volumetrica en CT. La Ec. 1 formaliza exactamente la separacion relevante: `M` transforma y `(1-M)` copia el CT. Refuerza la motivacion de `G = M union B_delta`: frente a LeFusion/CLAIM cambia GAN por U-Net residual adversarial y escala los datos, pero conserva la imposibilidad matematica de producir efectos fuera de `M`. Tambien muestra que una U-Net volumetrica y la mascara no son por si solas novedad. No colisiona con la contribucion especifica: no sintetiza objetos rigidos, no preserva metal/HU altos, no define una banda periobjeto ni evalua coherencia fisica; sus resultados principales son downstream.

## Dudas para el asesor
- ¿Subirlo de la prioridad N3 candidata a N2 y usar su Ec. 1 como contraste directo de `B_delta`?
- El texto atribuye “mass effect” al tumor, pero la Ec. 1 copia todo voxel fuera de `M`; ¿conviene señalar esta tension o evitar ese reclamo?
- Hay una inconsistencia interna: resumen/resultados/Tabla A17 dicen 161,310 CT, pero Metodos y Data availability dicen 161,130. Si se cita, ¿usar 161,310 por ser el total tabulado?
