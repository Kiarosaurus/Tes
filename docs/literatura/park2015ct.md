# park2015ct — Computed Tomographic Beam-Hardening Artefacts

- **DOI / URL:** https://doi.org/10.1098/rsta.2014.0388 (`refs/raw/park2015ct.nbib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/park2015ct.pdf (11 páginas)

## Que hace (3 lineas maximo)
Caracteriza matemáticamente el beam hardening como discrepancia no lineal entre proyecciones polienergéticas y el modelo monocromático de Radon usado por FBP. Separa cupping dentro del objeto de streaking exterior y relaciona los streaks con geometría y tangencias del metal.

## Restriccion o supuesto clave
El análisis parte de un sistema paralelo 2D y supuestos simplificadores sobre espectro, diferenciabilidad y geometría de materiales de alta atenuación. Aísla beam hardening, aunque reconoce scatter, volumen parcial no lineal, ruido, movimiento y photon starvation como causas adicionales (Sec. 4, p. 9). No mide extensión espacial, amplitud en HU ni una banda periimplante; `B_delta` y 12 mm son **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Condición geométrica: al menos dos puntos de tangencia | “touching at least two different points in the boundaries” | Sec. 2(b), p. 7 |
| Atenuación varía poco después de 100 keV bajo su argumento | “do not vary much with E after 100 keV electron energy” | Sec. 2(a), p. 4 |

## Donde entra en mi tesis
Es fundamento físico para que el soporte de generación exceda la máscara: “streaking artefacts corrupt the tomographic image outside the problematic region”, mientras el cupping queda dentro (Introducción, p. 2). También establece que el factor no lineal depende de la geometría individual de los objetos y de su disposición en el campo de visión (Introducción, p. 2). Esto respalda condicionar el artefacto por geometría y pose, y descarta modelarlo como una textura exclusiva del metal.

No respalda que una banda local finita capture todos los streaks: sus líneas pueden prolongarse fuera del objeto y el trabajo no proporciona una distancia de decaimiento. Por tanto, justifica la **dirección** de `B_delta` —más allá de `M`— pero no su ancho de 12 mm. Tampoco valida síntesis generativa, U-Net, difusión, ControlNet ni una simulación física completa. La condición de tangencia se deriva bajo supuestos matemáticos particulares y no debe convertirse en regla universal para todos los artefactos clínicos.

## Dudas para el asesor
- ¿Citarlo para separar cupping interior y streaking exterior, declarando que la extensión de `B_delta` sigue siendo un parámetro empírico?
- ¿Usar la dependencia geométrica solo como motivación física, sin exigir al modelo reproducir literalmente las tangencias del análisis 2D?

