# deman2015dose — Reconstruccion de dosis especifica del paciente en TC

- **DOI / URL:** 10.1118/1.4921066; https://aapm.onlinelibrary.wiley.com/doi/10.1118/1.4921066
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/deman2015dose.pdf

Profundidad: PDF completo (12 paginas; pp. 2740–2751 de la revista).

## Que hace (3 lineas maximo)

Propone reconstruir dosis absorbida por voxel desde una imagen CT: usa pencil beams
distance-driven para interacciones de primer orden y una suma de kernels gaussianos para las de
orden superior. Compara ocho experimentos 3D contra GEANT4.

## Restriccion o supuesto clave

El kernel avanzado es material-independiente, isotropico e invariante a traslacion: "we use a
material-independent shift-invariant blur kernel" (Sec. 2.D, p. 2747). Los parametros se ajustan
empiricamente a Monte Carlo y el modelo muestra desajuste en hueso; no modela ni valida implantes
metalicos ni artefactos de metal.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| error maximo <10% en experimento 6 | "largest deviation between the curves is less than 10%" | Sec. 3, p. 2749 |
| 541/949 mm, distancias de geometria | "541 mm source-to-isocenter distance, 949 mm source-to-detector distance" | Sec. 2.E, p. 2747 |
| 888 columnas y 64 filas | "888 detector columns, and 64 detector rows" | Sec. 2.E, p. 2747 |

## Donde entra en mi tesis

Marco del simulador fisico CatSim/XCIST y antecedentes de modelos rapidos de interaccion de rayos
X. Sirve para documentar el origen de la reconstruccion de dosis incorporada en esa familia, pero
no para afirmar fidelidad de artefactos metalicos ni como baseline de apariencia peri-implante.

## Dudas para el asesor

1. El articulo es de dosimetria, no de sintesis de imagen: confirmar que permanezca como contexto
   tecnico y no como evidencia de validacion visual de CatSim/XCIST.
2. La comparacion es solo contra simulacion Monte Carlo y los autores anuncian validacion posterior
   en cadaveres; no atribuirle validacion clinica.

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Salida del metodo | "volumetrically reconstructing absorbed dose on a per-voxel basis" | Abstract, p. 2740 |
| Entrada del metodo | "directly from the actual CT images" | Abstract, p. 2740 |
| Primer orden | "distance-driven pencil-beam approach to model the first-order x-ray interactions" | Abstract, p. 2740 |
| Orden superior | "Gaussian convolution kernels to model the higher-order x-ray interactions" | Abstract, p. 2740 |
| Referencia | "comparing the proposed method to a Monte Carlo based ground truth" | Abstract, p. 2740 |
| Error preliminar | "errors below 10%, except in bone regions" | Abstract, p. 2740 |
| Complejidad | "similar to that of a low-resolution filtered-backprojection algorithm" | Abstract, p. 2740 |
| Gold standard | "Monte Carlo simulation is generally considered ... gold standard" | Sec. 1, p. 2741 |
| Absorcion por Beer–Lambert | "Eabs(1) = Einc(0)*(1 - exp(-mu*d/cos theta))" | Ec. (1), Sec. 2.C, p. 2744 |
| Coeficiente desde reconstruccion | "linear attenuation coefficient mu is obtained from a CT reconstruction" | Sec. 2.C, p. 2745 |
| Aproximacion inicial de material | "fixed to (mu/rho)WATER" | Sec. 2.C, p. 2746 |
| Refinamiento de material | "refined by segmenting the reconstruction" | Sec. 2.C, p. 2746 |
| Modelo policromatico | "spectrum is divided in a number of energy bins" | Sec. 2.C, p. 2746 |
| Limitacion del kernel | "material-independent shift-invariant blur kernel" | Sec. 2.D, p. 2747 |
| Gaussianas isotropicas | "weighted sum of (isotropic) Gaussian kernels" | Sec. 2.D, p. 2747 |
| Geometria | "541 mm source-to-isocenter distance, 949 mm source-to-detector distance" | Sec. 2.E, p. 2747 |
| Detector | "888 detector columns, and 64 detector rows" | Sec. 2.E, p. 2747 |
| Energia experimental | "a beam energy of 70 keV" | Sec. 2.E, p. 2747 |
| Atenuacion tejido blando | "0.193 cm-1 for soft tissue" | Sec. 2.E, p. 2748 |
| Atenuacion pulmon | "0.052 cm-1 for lung tissue" | Sec. 2.E, p. 2748 |
| Atenuacion hueso | "0.493 cm-1 for bone tissue" | Sec. 2.E, p. 2748 |
| Kernels ajustados | "sigmas and weight factors were determined empirically" | Sec. 3, p. 2749 |
| Desajuste oseo | "model is not well tuned for bone tissue" | Sec. 3, p. 2749 |
| Error experimento 6 | "largest deviation between the curves is less than 10%" | Sec. 3, p. 2749 |
| Velocidad potencial | "compute time can become an order of magnitude lower" | Sec. 3, p. 2749 |
| Validacion futura | "more extensive validation study ... point dose measurements in cadavers" | Sec. 4, p. 2750 |
| Implantes metalicos | NO ENCONTRADO EN EL PDF | — |
| Artefactos metalicos | NO ENCONTRADO EN EL PDF | — |
| Validacion contra mediciones clinicas | NO ENCONTRADO EN EL PDF | — |
