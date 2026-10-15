# kak2001book — Principles of Computerized Tomographic Imaging

- **DOI / URL:** 10.1137/1.9780898719277; https://epubs.siam.org/doi/abs/10.1137/1.9780898719277
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/kak2001book1.pdf; papers/kak2001book2.pdf; papers/kak2001book3.pdf; papers/kak2001book4.pdf; papers/kak2001book5.pdf; papers/kak2001book6.pdf; papers/kak2001book7.pdf; papers/kak2001book8.pdf

Profundidad: ocho capitulos separados que, en conjunto, constituyen el libro completo disponible.

## Que hace (3 lineas maximo)

Tratado de los fundamentos fisicos y matematicos de la tomografia computarizada: formacion de
proyecciones, reconstruccion por fuentes no difractantes, medicion con rayos X, artefactos, ruido y
metodos algebraicos. Deriva la relacion atenuacion–proyeccion, la escala HU y la FBP.

## Restriccion o supuesto clave

La igualdad entre la integral de linea y el logaritmo de intensidades es estricta para fotones
monoenergeticos: "strictly true only under the assumption that the x-ray beam consists of
monoenergetic photons" (Sec. 4.1.1, p. 117). Tambien supone detectores insensibles al scatter, haz
muy estrecho y apertura pequena. El propio libro explica que las fuentes medicas reales son
policromaticas y que esto produce endurecimiento del haz (Sec. 4.1.2, pp. 117–118).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| agua = 0 HU | "The value H = 0 corresponds to water" | Sec. 4.1.2, p. 119 |
| aire = -1000 HU | "H = -1000 corresponds to p = 0" | Sec. 4.1.2, p. 119 |
| factor 1000 de la escala HU | "H = ... x1000" | Ec. (12), Sec. 4.1.2, p. 119 |

## Donde entra en mi tesis

Capitulo 1, fundamento fisico de TC y cierre de la marca `capitulo1.tex:35`. Respalda
explicitamente las tres afirmaciones solicitadas por ese GAPLIT:

1. **Beer–Lambert / proyeccion:** deriva `N(x)=N0 exp(-mu x)` y, para un objeto no homogeneo,
   que la integral de `mu(x,y)` sobre el rayo es `ln(Nin/Nd)` (Sec. 4.1.1, pp. 115–117).
2. **Escala Hounsfield:** define `H = (mu-mu_water)/mu_water x 1000`, con agua en 0 HU y
   aire ideal en -1000 HU (Sec. 4.1.2, p. 119).
3. **Retroproyeccion filtrada:** identifica filtrado en frecuencia y retroproyeccion como sus dos
   pasos y enumera el algoritmo completo (Sec. 3.3, pp. 61–62).

Ademas, permite advertir que el modelo lineal monocromatico es una aproximacion y documenta
streaks y flares debidos a policromaticidad cerca y entre huesos gruesos (Sec. 4.1.3, p. 120).

## Dudas para el asesor

1. Confirmar si la formulacion del capitulo debe decir "modelo de Beer–Lambert monocromatico"
   para no ocultar las condiciones que el propio libro enumera.
2. La ecuacion usa conteos de fotones `N`, no intensidad continua `I`; decidir si se conserva la
   notacion del libro o se presenta la forma equivalente usada en el documento.

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Parametro reconstruido en TC de rayos X | "forming images of tissues based on their x-ray attenuation coefficient" | Cap. 1, p. 1 |
| Definicion de proyeccion | "a projection at a given angle is the integral of the image" | Cap. 1, p. 1 |
| Proyeccion como integral de linea | "projections are a set of measurements of the integrated values" | Cap. 3, p. 49 |
| Atenuacion exponencial | "N(x) = Noe-@" | Ec. (6), Sec. 4.1.1, p. 115 |
| Nombre de mu | "The constant p is called the attenuation coefficient" | Sec. 4.1.1, p. 115 |
| Logaritmo medido | "measurements like ln (Nin/Nd) ... generate projection data" | Sec. 4.1.1, p. 116 |
| Condicion monoenergetica | "strictly true only under the assumption ... monoenergetic photons" | Sec. 4.1.1, p. 117 |
| Condiciones adicionales | "detectors that are insensitive to scatter" | Sec. 4.1.1, p. 117 |
| Rango diagnostico citado | "from 20 to 150 keV" | Sec. 4.1, p. 114 |
| Fuente medica real | "x-ray sources used for medical imaging do not produce monoenergetic photons" | Sec. 4.1.2, p. 117 |
| Definicion de beam hardening | "This phenomenon is called beam hardening" | Sec. 4.1.2, p. 118 |
| Definicion de energia efectiva | "monochromatic energy at which a given material ... same attenuation coefficient" | Sec. 4.1.2, p. 118 |
| Salida tipica del escaner | "integers that usually range in values from -1000 to 3000" | Sec. 4.1.2, p. 119 |
| Nombre de la escala | "given the name Hounsfield units and are denoted by HU" | Sec. 4.1.2, p. 119 |
| Formula HU | "The relationship between the linear attenuation coefficient and ... Hounsfield unit" | Sec. 4.1.2, p. 119 |
| Agua | "The value H = 0 corresponds to water" | Sec. 4.1.2, p. 119 |
| Aire | "H = -1000 corresponds to p = 0" | Sec. 4.1.2, p. 119 |
| Teorema de corte de Fourier | "Fourier transform of a parallel projection ... gives a slice" | Sec. 3.2, p. 57 |
| Dos pasos de FBP | "there are two steps to the filtered backprojection algorithm" | Sec. 3.3, p. 61 |
| Paso de filtrado | "simple weighting of each projection in the frequency domain" | Sec. 3.3, p. 61 |
| Paso de retroproyeccion | "smearing of each filtered projection over the image plane" | Sec. 3.3, p. 62 |
| Dominio angular de FBP | "K angles ... between 0 and 180" | Sec. 3.3, p. 62 |
| Artefacto por policromaticidad | "appearance of streaks and flares ... between bones" | Sec. 4.1.3, p. 120 |
