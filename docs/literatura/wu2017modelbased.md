# wu2017modelbased — Reconstruccion de dosis basada en modelos para TC

- **DOI / URL:** 10.1002/mp.12409; https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.12409
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wu2017modelbased.pdf

Profundidad: PDF completo (9 paginas; pp. e255–e263 de la revista).

## Que hace (3 lineas maximo)

Mejora la reconstruccion rapida de dosis de De Man et al. mediante descomposicion agua/hueso y
modelos separados de absorcion fotoelectrica, dispersion Compton y Rayleigh. La valida contra
GEANT4 con fantomas analiticos y espectros policromaticos.

## Restriccion o supuesto clave

La descomposicion de una adquisicion de kVp unico es aproximada y restringe el cuerpo a agua y
hueso de densidad variable: "body is made of two materials with variable densities" (Sec. 2.D,
p. e257). Los kernels de scatter tampoco dependen del material; una identificacion erronea puede
producir errores cercanos a 50%. No estudia metal ni apariencia de artefactos.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| error voxel <6% | "less than 6% voxel-wise errors" | Abstract, p. e255 |
| error ROI <3.2% | "less than 3.2% ROI-based errors" | Abstract, p. e255 |
| 480 s en configuracion reportada | "the computation time is about 480 s" | Sec. 3, p. e262 |

## Donde entra en mi tesis

Antecedente del componente de dosis de XCIST y evidencia de que una aproximacion rapida puede
reproducir Monte Carlo para tejidos blandos y hueso bajo condiciones controladas. No debe usarse
como validacion de simulacion de metal, streaking ni intensidad CT peri-implante.

## Dudas para el asesor

1. La exactitud publicada depende de usar el mismo espectro en metodo y Monte Carlo; decidir si
   esta dependencia debe explicitarse al describir la validacion del simulador.
2. No extrapolar los resultados de agua/hueso a titanio o acero sin validacion adicional.

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Objetivo | "model-based approach for CT dose estimation" | Abstract, p. e255 |
| Diferencia con Monte Carlo | "we do not track each individual photon" | Abstract, p. e255 |
| Primer orden | "pencil-beam calculations for the first-order interactions" | Abstract, p. e255 |
| Orden superior | "kernels for the higher order interactions" | Abstract, p. e255 |
| Referencia | "comparing to Monte Carlo simulation (GEANT4) as the ground truth" | Abstract, p. e255 |
| Error voxel | "less than 6% voxel-wise errors" | Abstract, p. e255 |
| Error ROI | "less than 3.2% ROI-based errors" | Abstract, p. e255 |
| Error previo en tejido blando | "error < 10%" | Sec. 1, p. e255 |
| Error previo en hueso | "sometimes exceeding 50% in anthropomorphic phantoms" | Sec. 1, p. e255 |
| Tamano de voxel | "voxel size, we used (1.5625 mm)" | Sec. 2.C.1, p. e256 |
| Deposito fotoelectrico | "100% of the primary photon energy is absorbed" | Sec. 2.C.1, p. e256 |
| Materiales asumidos | "two materials with variable densities: water and bone" | Sec. 2.D, p. e257 |
| Rango energetico Compton | "energy range from 10 keV to 160 keV" | Sec. 2.E, p. e257 |
| Fuente de secciones eficaces | "obtained from ... GEANT4" | Sec. 2.D, p. e257 |
| Error voxel del fantoma | "remains below 6% for all voxels" | Sec. 3, p. e261 |
| Error ROI observado | "range between -1.5% and 3.2%" | Sec. 3, p. e261 |
| Limite de kernels | "does not distinguish the scatter kernel parameters for different materials" | Sec. 3, p. e262 |
| Caso extremo oseo | "approximately 150% ... overestimation" | Sec. 3, p. e262 |
| Error por clasificacion | "a large error, about 50%, will be expected" | Sec. 3, p. e262 |
| Dependencia del espectro | "accuracy directly relies on ... the incident spectrum" | Sec. 3, p. e262 |
| Costo de fisica | "Less than 1% of the computation time" | Sec. 3, p. e262 |
| Configuracion temporal | "256 x 256 x 256 voxelized phantom" | Sec. 3, p. e262 |
| Proyecciones del ejemplo | "880 columns x 64 rows x 984 views" | Sec. 3, p. e262 |
| Bins del ejemplo | "16 energy bins" | Sec. 3, p. e262 |
| Tiempo | "the computation time is about 480 s" | Sec. 3, p. e262 |
| Validacion requerida | "validated for a wide range of clinical datasets" | Sec. 3, p. e263 |
| Implantes metalicos | NO ENCONTRADO EN EL PDF | — |
| Artefactos metalicos | NO ENCONTRADO EN EL PDF | — |
