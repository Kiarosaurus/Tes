# deman1999 — Artefactos de raya metalica en CT: estudio por simulacion

- **DOI / URL:** NO ENCONTRADO EN EL PDF (el PDF solo imprime `0018-9499/99$10.00 © 1999 IEEE`; datos de cabecera: IEEE Trans. Nucl. Sci., vol. 46, no. 3, June 1999, pp. 691-696)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/deman1999.pdf

## Que hace (3 lineas maximo)

Presenta un simulador 2D de CT de haz en abanico de alta resolucion, ajustado a un
Siemens Somatom Plus 4, y lo valida contra medidas de dos fantomas (varilla de hierro
en agua; placa de plexiglas con amalgamas). Aisla una a una las causas fisicas del
streaking metalico activando y desactivando cada efecto en la simulacion, y concluye
cualitativamente cuales son las mas importantes. No mide ni una sola vez la extension
espacial de las rayas.

## Restriccion o supuesto clave

No es un paper de sintesis generativa, pero su supuesto operativo es el que mas importa
aqui: **todos los mecanismos se definen y se manipulan en el dominio de proyeccion**, no
en la imagen. El streaking se produce alterando el sinograma (politcromatico vs
monocromatico, con/sin scatter, con/sin ruido de Poisson, modo 1 vs modo 2 de la integral
sobre foco y detector) y luego reconstruyendo. La propia motivacion del trabajo es un
esquema iterativo con *"model of the acquisition"* (Fig. 15, p. 695). Ademas se declara
que la tercera dimension no entra: *"The third dimension, perpendicular to the scanning
plane, is not taken into account"* (Sec. II-A, p. 691), y el volumen parcial axial queda
fuera de alcance. Consecuencia directa para la tesis: **este paper no autoriza ni prohibe
reproducir el artefacto en dominio-imagen; simplemente no trata el caso.**

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ancho del foco 0.6 mm, del detector 1.2 mm, muestreo 0.1 mm | *"sampling at high resolution (typically 0.1mm)"*; *"focal spot width (0.6mm) and detector element width (1.2mm)"* | Sec. II-A, p. 691 |
| Espectro modelado con 5 energias monocromaticas | *"modeled by summing 5 monochromatic simulations at well-chosen energies"* | Sec. II-A, p. 692 |
| Varilla de hierro de 11.6 mm de diametro (fantoma 1) | *"a cylindrical iron rod (ø 11.6mm) positioned eccentrically in the water"* | Sec. II-B-2, p. 692 |
| Alambre de hierro de 0.7 mm para la LSF | *"using an iron wire (ø 0.7mm) positioned at different positions"* | Sec. II-B-1, p. 692 |
| Razon scatter-primario 0.0001 | *"The scatter-to-primary ratio was arbitrarily chosen to be 0.0001"* | Sec. II-D, p. 693 |
| Flujo no atenuado de 1e5 o 2e5 fotones por detector | *"an unattenuated flux of 10^5 or 2 x 10^5 photons per detector"* | Sec. II-D, p. 693 |
| Exceso de tiempo de integracion ~500 us sobre 710 us esperados | *"this integration time is about 500us larger than the expected 710us"* | Sec. II-A, p. 692 |
| Tiempo teorico de coleccion de iones 600 us | *"theoretical ion collection time of 600us"* | Sec. II-A, p. 692 |
| Solapamiento de detectores 1/6 y desplazamiento de 1/4 de elemento | *"detector overlap of 1/6 at both sides"*; *"shifted over one fourth of the detector element width"* | Sec. II-A, p. 692 |
| Movimiento simulado de 1.4 mm tras 700 vistas | *"the iron rod was moved over about 1.4mm after 700 views"* | Sec. III-F, p. 694 |
| Ventana de visualizacion de las reconstrucciones (en mu, no en HU) | *"windowed in the interval mu = [0.1; 0.3] cm^-1"* | Sec. III-A, p. 693 |
| Ventana del mapa de error por ruido (en mu, no en HU) | *"windowing: mu = [-0.05; 0.05] cm^-1"* | Fig. 12, p. 694 |
| Reduccion de ruido por promediado de n sinogramas: factor sqrt(n) | *"Averaging of n intensity sinograms allows to reduce the noise by a factor"* | Sec. II-D, p. 693 |

## Donde entra en mi tesis

- **Related Work / fundamento fisico del renderizador.** Es la fuente clasica que enumera
  y separa las causas del streaking metalico. Sirve para justificar *por que* el artefacto
  aparece **fuera** del metal (rayas que conectan objetos metalicos, rayas que irradian
  desde el metal, rayas en las direcciones de maxima atenuacion), sin comprometerse con
  ninguna cifra de extension.
- **Justificacion cualitativa de B_delta.** Respalda el enunciado de `main.tex` de que el
  artefacto no queda confinado a la mascara del implante, pero **solo en terminos
  cualitativos**.
- **NO sirve como fuente de umbrales en HU** (no hay HU en todo el PDF) ni como precedente
  cuantitativo de banda peri-implante.

## Respuestas a las preguntas dirigidas

**1. Causas fisicas separadas y cuantificadas.** Separa siete: beam hardening, scatter,
ruido (Poisson), exponential edge-gradient effect (EEGE), movimiento del objeto, submuestreo
de detectores y submuestreo de vistas. El **photon starvation no se nombra con ese termino**;
el ruido se trata como artefacto no lineal dependiente de la atenuacion integrada. El
**non-linear partial volume effect se declara explicitamente fuera de alcance** (*"axial
partial volume effects [16] are beyond the scope of this article"*, Sec. II-A, p. 691).
Contribucion relativa: **solo un ranking cualitativo, sin ninguna cifra**: *"Beam hardening,
scatter, noise and EEGE are the most important causes of metal streak artifacts"*
(Conclusiones, p. 695) y *"Under extreme circumstances, also object motion and aliasing
effects produce streak artifacts"* (misma seccion). **Porcentaje, fraccion de varianza o
peso numerico por causa: NO ENCONTRADO EN EL PDF.**

**2. Extension espacial del streak alrededor del metal — PREGUNTA CRITICA.**
**NO ENCONTRADO EN EL PDF, de forma inequivoca.** Revisado el texto completo de las seis
paginas (691-696), abstract, metodos, resultados, conclusiones y los pies de las figuras
1-15: **no hay ninguna medida de la extension del artefacto en mm, cm, pixeles, ni perfil
radial, ni ley de decaimiento, ni distancia de "alcance" del streak, ni region de interes
definida alrededor del metal.** Todas las descripciones de localizacion son cualitativas y
direccionales: *"dark streaks in the directions of highest attenuation"* (Sec. III-B,
p. 693), *"additional dark streaks connecting the metal objects"* (Sec. III-B, p. 693),
*"a number of streaks can be seen radiating from the metals"* (Sec. III-D, p. 694),
*"streaks tangent to long straight edges"* (Sec. III-D, p. 694). La unica frase que menciona
una distancia es descriptiva y **sin valor numerico**: *"streaks starting at a certain
distance from the center"* (Sec. III-G, p. 694), y ademas se refiere al centro de rotacion
en submuestreo de vistas, no al borde del implante. Los unicos milimetros del paper son
tamanos de hardware y de fantoma (0.1 / 0.6 / 1.2 / 0.7 / 11.6 mm) y el desplazamiento de
1.4 mm del experimento de movimiento. **Conclusion para la tesis: este paper NO constituye
precedente publicado que cuantifique una banda peri-implante, y por tanto NO pone en riesgo
la frase de novedad de B_delta en `main.tex`.**

**3. Umbrales de error en HU.** **NO ENCONTRADO EN EL PDF.** La palabra "Hounsfield" y la
sigla HU no aparecen. Todas las ventanas de visualizacion estan en coeficiente de
atenuacion: `mu = [0.1; 0.3] cm^-1` (p. 693) y `mu = [-0.05; 0.05] cm^-1` (Fig. 12, p. 694).
No hay +/-75 HU, ni 500 HU, ni ningun criterio cuantitativo de severidad del artefacto.

**4. Material, geometria y tamano del implante simulado.** Dos materiales metalicos:
**hierro** (varilla cilindrica de 11.6 mm de diametro en cuenco de agua, mas un alambre de
0.7 mm solo para la LSF) y **amalgama** (una, dos o tres rellenos cilindricos en una placa
de plexiglas). Los coeficientes se calculan para *"water, iron and amalgam"* desde datos del
NIST (Sec. II-A, p. 692). **Es dental/fantoma, NO ortopedico**: la motivacion declarada son
los rellenos dentales (*"such as dental fillings"*, Introduccion, p. 691). **Titanio, acero
quirurgico, tornillos, placas o cualquier implante ortopedico: NO ENCONTRADO EN EL PDF.**
**Diametro de los rellenos de amalgama: NO ENCONTRADO EN EL PDF.** Nota: la Fig. 1 muestra
un caso clinico con artefactos, sin identificar el metal ni la region anatomica.

**5. Modelo de adquisicion y reimplementabilidad hoy.** Geometria de haz en abanico 2D
(*"based on a typical fan-beam geometry"*, Sec. II-A, p. 691), parametros ajustados al
*"Siemens Somatom Plus 4 CT-scanner"* (misma seccion), adquisicion de 360 grados, fuente
modelada como linea recta de radiacion uniforme, foco 0.6 mm, detector 1.2 mm, muestreo
0.1 mm, solapamiento de detector 1/6, desplazamiento de cuarto de detector, detectores de
xenon con after-glow modelado, scatter constante, ruido de Poisson, reconstruccion FBP de
haz en abanico de Herman [21] y, para validacion, rebinning + reconstruccion paralela.
Espectro: 5 simulaciones monocromaticas sobre el espectro real de la Fig. 4 (eje de 0 a
140 keV). **kVp, mAs, filtracion, distancia foco-isocentro, distancia foco-detector, numero
de detectores, tamano de pixel de la reconstruccion, matriz y kernel: NO ENCONTRADO EN EL
PDF.** **Numero total de proyecciones: NO ENCONTRADO EN EL PDF de forma explicita**; el
unico indicio es *"between view 1056 and view 1"* (Sec. III-F, p. 694) y el eje de la Fig. 7,
que llega a ~1000 vistas. Reimplementabilidad hoy: **parcial**. La estructura del simulador
es reproducible en concepto, pero faltan la mayoria de los parametros de escaner, el
espectro esta solo como figura, y el codigo (IDL + C) no se publica ni se enlaza. Los
propios autores acotan la generalidad: *"we focussed on one specific scanner type. Results
must be generalized for other scanner types"* (Future Work, p. 695).

**6. Reproducibilidad del artefacto por metodos puramente de dominio-imagen.**
**NO ENCONTRADO EN EL PDF.** El paper no discute en ningun momento si el streaking podria
generarse o corregirse sin pasar por el sinograma. Lo que si aporta, y es lo mas cercano:
(a) caracteriza los cuatro mecanismos principales como **no lineales** (*"Noise artifacts
are non-linear artifacts, just like beam hardening and scatter artifacts"*, Sec. III-E,
p. 694), lo que implica dependencia de la atenuacion integrada a lo largo del rayo, es
decir del sinograma; (b) todos sus experimentos de aislamiento se ejecutan modificando
proyecciones; (c) critica el supuesto de la MAR de la epoca de que los datos afectados por
metal son inservibles (*"all based on the assumption that measured data affected by metal
objects are useless"*, Introduccion, p. 691). **Ninguna frase dice que el artefacto sea
irreproducible en el dominio imagen, y ninguna dice que lo sea.**

## Dudas para el asesor

- El renderizador de la tesis trabaja en imagen y este paper define toda la fisica en
  proyeccion. Se cita De Man como *fundamento del mecanismo* (por que hay senal fuera del
  metal) aceptando que no respalda la implementacion, o se busca una fuente mas cercana al
  dominio imagen?
- Los materiales aqui son hierro y amalgama dental. Vale como respaldo fisico generico
  para acero/titanio pelvico, o hay que marcarlo como caveat explicito de transferencia de
  material y escala?
- El ranking de causas es cualitativo. Si la tesis quiere ponderar que efectos incluye el
  renderizador (beam hardening vs scatter vs ruido), este paper no da pesos: hace falta
  otra fuente o se deja como decision de diseno?

## Evidencia textual

| Item | Frase original (<15 palabras) | Seccion / pagina |
|---|---|---|
| Causas identificadas como mas importantes | *"Beam hardening, scatter, noise and EEGE are the most important causes of metal streak artifacts"* | Conclusiones, p. 695 |
| Causas secundarias | *"Under extreme circumstances, also object motion and aliasing effects produce streak artifacts"* | Conclusiones, p. 695 |
| Lista completa de causas revisadas en literatura | *"beam hardening, scatter, noise, exponential edge-gradient effect, detector under-sampling, view under-sampling, object motion"* | Introduccion, p. 691 |
| Todas las causas producen rayas | *"We have proven that all investigated causes of streaks are effectively able to produce streaks"* | Conclusiones, p. 695 |
| Volumen parcial axial fuera de alcance | *"axial partial volume effects [16] are beyond the scope of this article"* | Sec. II-A, p. 691 |
| Simulacion 2D, sin tercera dimension | *"The third dimension, perpendicular to the scanning plane, is not taken into account"* | Sec. II-A, p. 691 |
| Geometria de adquisicion | *"based on a typical fan-beam geometry"* | Sec. II-A, p. 691 |
| Escaner de referencia | *"All parameters were adjusted for the Siemens Somatom Plus 4 CT-scanner"* | Sec. II-A, p. 691 |
| Modelo de fuente | *"the X-ray source is modeled as a uniformly radiating straight line"* | Sec. II-A, p. 691 |
| Muestreo de alta resolucion | *"sampling at high resolution (typically 0.1mm)"* | Sec. II-A, p. 691 |
| Ancho de foco y de detector | *"focal spot width (0.6mm) and detector element width (1.2mm)"* | Sec. II-A, p. 691 |
| Espectro por 5 monocromaticas | *"modeled by summing 5 monochromatic simulations at well-chosen energies"* | Sec. II-A, p. 692 |
| Materiales con coeficientes calculados | *"Absorption coefficients of water, iron and amalgam are calculated from data available on-line"* | Sec. II-A, p. 692 |
| Exceso de tiempo de integracion | *"this integration time is about 500us larger than the expected 710us"* | Sec. II-A, p. 692 |
| Tiempo teorico de coleccion de iones | *"in good agreement with the theoretical ion collection time of 600us"* | Sec. II-A, p. 692 |
| Movilidad ionica usada | *"k = 0.015 cm2/V.s the ionic mobility taken from [20]"* | Sec. II-A, p. 692 |
| Cross-talk de detectores | *"Detector cross-talk is modeled by including a detector overlap of 1/6 at both sides"* | Sec. II-A, p. 692 |
| Desplazamiento de cuarto de detector, adquisicion 360 grados | *"shifted over one fourth of the detector element width to remove the redundancy"* | Sec. II-A, p. 692 |
| Scatter de nivel constante | *"a constant scatter level was chosen"* | Sec. II-A, p. 692 |
| Justificacion del scatter constante | *"Real scatter profiles usually contain very little high frequencies"* | Sec. II-A, p. 692 |
| Ruido anadido | *"Poisson noise was added to the simulated intensities"* | Sec. II-A, p. 692 |
| Calibracion del nivel de ruido | *"tuned so that the simulated intensities had the same standard deviation as in the measurements"* | Sec. II-A, p. 692 |
| Alambre de hierro para la LSF | *"using an iron wire (ø 0.7mm) positioned at different positions"* | Sec. II-B-1, p. 692 |
| Ajuste de la LSF | *"The full width at half maximum (FWHM) of the LSF was calculated by fitting a Gaussian"* | Sec. II-B-1, p. 692 |
| Fantoma 1: varilla de hierro 11.6 mm | *"a cylindrical iron rod (ø 11.6mm) positioned eccentrically in the water"* | Sec. II-B-2, p. 692 |
| Fantoma 2: placa de plexiglas con 1-3 amalgamas | *"a Plexiglas plate, with one, two or three cylindrical amalgam fillings"* | Sec. II-B-2, p. 692 |
| Algoritmo de reconstruccion | *"the direct fan-beam filtered backprojection algorithm from Herman [21]"* | Sec. II-C, p. 692 |
| Segundo algoritmo, solo validacion | *"a rebinner followed by a parallel beam reconstruction"* | Sec. II-C, p. 692 |
| Razon scatter-primario | *"The scatter-to-primary ratio was arbitrarily chosen to be 0.0001"* | Sec. II-D, p. 693 |
| Flujo de fotones por detector | *"an unattenuated flux of 10^5 or 2 x 10^5 photons per detector"* | Sec. II-D, p. 693 |
| Reduccion de ruido por promediado | *"Averaging of n intensity sinograms allows to reduce the noise by a factor"* (sqrt(n)) | Sec. II-D, p. 693 |
| Metodo de aislamiento de causas | *"comparing scatter-, noise- and EEGE-free simulations and simulations with scatter, noise or EEGE"* | Sec. II-D, p. 693 |
| Metodo para beam hardening | *"comparing polychromatic and monochromatic simulations"* | Sec. II-D, p. 693 |
| Ventana de las reconstrucciones | *"All reconstructions are windowed in the interval mu = [0.1; 0.3] cm-1"* | Sec. III-A, p. 693 |
| Ventana del mapa de error por ruido | *"windowing: mu = [-0.05; 0.05] cm-1"* | Fig. 12, p. 694 |
| Beam hardening: direccion de las rayas | *"we observe dark streaks in the directions of highest attenuation"* | Sec. III-B, p. 693 |
| Beam hardening con dos o mas metales | *"additional dark streaks connecting the metal objects can be seen"* | Sec. III-B, p. 693 |
| Cupping presente pero invisible con esa ventana | *"the more general cupping artifact is present, but this can not be seen"* | Sec. III-B, p. 693 |
| Scatter minimo basta | *"Even a very small scatter-to-primary ratio causes significant streaks"* | Sec. III-C, p. 694 |
| Rayas brillantes por el kernel | *"probably due to the negative values in the reconstruction kernel"* | Sec. III-C, p. 694 |
| Semejanza scatter / policromatico | *"these artifacts are very similar to the polychromatic artifacts in figure 9"* | Sec. III-C, p. 694 |
| EEGE: nada en fantoma de un solo metal | *"For phantom 1, no streaks are observed"* | Sec. III-D, p. 694 |
| EEGE: signo segun gradientes | *"dark streaks... connecting edges with equally-signed gradients, while white streaks... opposite gradients"* | Sec. III-D, p. 694 |
| EEGE: rayas tangentes a bordes rectos | *"the EEGE is known to cause streaks tangent to long straight edges"* | Sec. III-D, p. 694 |
| EEGE: rayas que salen del metal | *"a number of streaks can be seen radiating from the metals"* | Sec. III-D, p. 694 |
| Ruido: patron de lineas alternas | *"consists of thin lines alternately dark and bright"* | Sec. III-E, p. 694 |
| Ruido: no linealidad | *"Noise artifacts are non-linear artifacts, just like beam hardening and scatter artifacts"* | Sec. III-E, p. 694 |
| Ruido: dependencia de la atenuacion integrada | *"strongly depends on the magnitude of the measured intensities and thus of the total integrated attenuation"* | Sec. III-E, p. 694 |
| Acoplamiento entre causas | *"even the amount of scatter and beam hardening have a strong influence on the severity"* | Sec. III-E, p. 694 |
| Movimiento simulado | *"the iron rod was moved over about 1.4mm after 700 views"* | Sec. III-F, p. 694 |
| Vistas de inconsistencia (unico indicio del total de vistas) | *"between view 700 and view 701 and between view 1056 and view 1"* | Sec. III-F, p. 694 |
| Submuestreo de detectores | *"circular patterns tangent to strong edges"* | Sec. III-G, p. 694 |
| Submuestreo de vistas (unica mencion de "distancia", sin cifra) | *"streaks starting at a certain distance from the center"* | Sec. III-G, p. 694 |
| Aliasing residual en las simulaciones "libres de artefacto" | *"aliasing errors (such as Moire patterns) are present, although not visible"* | Sec. III-G, p. 694 |
| Aliasing corregible con kernel | *"appropriate reconstruction kernels should be able to reduce aliasing artifacts as much as wanted"* | Sec. III-G, pp. 694-695 |
| Aliasing y movimiento no son exclusivos del metal | *"neither the aliasing artifacts, nor the artifacts due to object motion are limited to metal"* | p. 695 |
| El metal agrava artefactos genericos | *"because of their high attenuation values, the presence of metal objects makes the artifacts more prominent"* | p. 695 |
| Motivacion clinica: rellenos dentales | *"strongly attenuating objects - such as dental fillings - causes typical streak artifacts"* | Introduccion, p. 691 |
| Critica al supuesto de la MAR previa | *"all based on the assumption that measured data affected by metal objects are useless"* | Introduccion, p. 691 |
| Objetivo declarado: entender antes de corregir | *"a complete understanding of the streak generation processes is indispensable for a well-founded solution"* | Introduccion, p. 691 |
| Limite de generalizacion a otros escaneres | *"we focussed on one specific scanner type. Results must be generalized for other scanner types"* | Future Work, p. 695 |
| Necesidad de extension a 3D | *"Extension to 3D, and in particular analysis of the axial partial volume effect is needed"* | Future Work, p. 695 |
| Prevencion en adquisicion | *"Noise can be reduced by using high mAs-settings. Beam hardening can be minimized by using pre-filtering"* | Future Work, p. 695 |
| Conflicto con dosis | *"all these measures are in direct conflict with other clinical concerns such as low patient dose"* | Future Work, p. 695 |
| Ruta propuesta por los autores | *"Our aim is to apply iterative reconstruction [19] to reduce metal streak artifacts"* | Future Work, p. 695 |
| Ventaja del enfoque iterativo | *"the possibility to use a model of the acquisition, taking into account polychromaticity, scatter, noise, EEGE"* | Future Work, p. 695 |
| Financiamiento | *"supported by the Flemish Fund for Scientific Research (FWO), grant number G.0106.98"* | Agradecimientos, p. 695 |
| **Extension espacial del streak en mm/cm/pixeles** | **NO ENCONTRADO EN EL PDF** | — |
| **Perfil radial o ley de decaimiento del artefacto** | **NO ENCONTRADO EN EL PDF** | — |
| **Banda o region de interes peri-metal definida** | **NO ENCONTRADO EN EL PDF** | — |
| **Cualquier umbral o cifra en HU** | **NO ENCONTRADO EN EL PDF** | — |
| **Metrica cuantitativa de severidad del artefacto (RMSE, error medio, etc.)** | **NO ENCONTRADO EN EL PDF** | — |
| **Contribucion relativa numerica entre causas** | **NO ENCONTRADO EN EL PDF** | — |
| **Titanio, acero quirurgico o implante ortopedico** | **NO ENCONTRADO EN EL PDF** | — |
| **Diametro o tamano de los rellenos de amalgama** | **NO ENCONTRADO EN EL PDF** | — |
| **kVp del tubo** | **NO ENCONTRADO EN EL PDF** | — |
| **mAs** | **NO ENCONTRADO EN EL PDF** | — |
| **Filtracion / pre-filtro del haz (valor)** | **NO ENCONTRADO EN EL PDF** | — |
| **Numero total de proyecciones declarado explicitamente** | **NO ENCONTRADO EN EL PDF** (solo *"view 1056 and view 1"*) | — |
| **Numero de elementos del detector** | **NO ENCONTRADO EN EL PDF** | — |
| **Distancia foco-isocentro y foco-detector** | **NO ENCONTRADO EN EL PDF** | — |
| **Angulo de abanico en grados** | **NO ENCONTRADO EN EL PDF** | — |
| **Tamano de matriz y de pixel de la reconstruccion** | **NO ENCONTRADO EN EL PDF** | — |
| **Kernel de reconstruccion usado** | **NO ENCONTRADO EN EL PDF** | — |
| **Valores numericos de FWHM de la LSF** | **NO ENCONTRADO EN EL PDF** (solo la curva de la Fig. 7) | — |
| **Energias exactas de las 5 monocromaticas** | **NO ENCONTRADO EN EL PDF** (solo flechas en la Fig. 4) | — |
| **Espesor de corte** | **NO ENCONTRADO EN EL PDF** | — |
| **Coeficientes de atenuacion numericos de hierro y amalgama** | **NO ENCONTRADO EN EL PDF** | — |
| **Afirmacion sobre reproducir el artefacto en dominio imagen** | **NO ENCONTRADO EN EL PDF** | — |
| **Mencion de anatomia pelvica, sacro o tornillos** | **NO ENCONTRADO EN EL PDF** | — |
| **Datos de pacientes o dataset clinico** | **NO ENCONTRADO EN EL PDF** (Fig. 1 es un ejemplo sin describir) | — |
| **Seccion de limitaciones formal** | **NO ENCONTRADO EN EL PDF** (solo Future Work) | — |
| **DOI impreso** | **NO ENCONTRADO EN EL PDF** | — |
| **Disponibilidad del codigo del simulador** | **NO ENCONTRADO EN EL PDF** | — |

## Impacto sobre la tesis (propuesta del lector)

**(a) Que obliga a ajustar**

- **Redaccion: si, en un punto concreto y a favor.** La frase de `main.tex` *"for which no
  published precedent quantifying a peri-implant band was found"* **no queda en riesgo**:
  este paper, que es la referencia canonica del mecanismo del streaking metalico, no
  cuantifica ninguna extension espacial. Se puede citar De Man como la fuente que establece
  el mecanismo y, a la vez, como evidencia de que el mecanismo se describe sin metrica de
  alcance.
- **Redaccion: matiz sobre "propagate globally".** El respaldo que da este paper a
  *"propagate globally far beyond the implant's boundaries"* es **cualitativo y direccional**
  (rayas en direcciones de maxima atenuacion, rayas que conectan metales, rayas que irradian
  desde el metal). Si `main.tex` cita a De Man para esa frase, conviene que la frase no
  sugiera una cuantificacion que la fuente no tiene.
- **Supuesto: si, hay un caveat nuevo de transferencia.** Las causas se establecen sobre
  **hierro y amalgama dental**, en **2D**, con volumen parcial axial excluido. Trasladarlas
  a tornillos pelvicos de acero o titanio en CT helicoidal 3D es una extrapolacion que hay
  que declarar, sobre todo porque los propios autores piden generalizar a otros escaneres y
  extender a 3D.
- **Gap nuevo: si, uno.** El renderizador de la tesis trabaja en imagen y **todas** las
  causas principales aqui son no lineales y definidas sobre el sinograma. El paper **no dice**
  que sean irreproducibles en dominio imagen, pero tampoco lo respalda: queda un hueco
  argumental que la tesis debe cubrir con otra fuente o declarar como supuesto de diseno.
- **Alcance y baseline: no.** No es candidato a baseline (no sintetiza nada, no hay codigo,
  parametros incompletos) y no toca el alcance declarado.

**(b) Nivel sugerido: 2.** Afecta la redaccion de Related Work y del fundamento fisico del
renderizador, y sostiene indirectamente la novedad de B_delta, pero no aporta ninguna cifra
que entre al benchmark ni ningun metodo reimplementable: un error al citarlo no tumba el
argumento central ni la evaluacion.

**(c) Acceso: COMPLETO. 6 paginas (691-696), incluidas las 21 referencias.** Sin material
suplementario, sin codigo, sin apendices.
