# hyung2017ml — Machine-learning-based nonlinear decomposition of CT images for metal artifact reduction

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. arXiv:1708.00244v1 [physics.med-ph], 1 Aug 2017 (sello lateral, p. 1). Nota: el raw `refs/raw/hyung2017ml.bib` usa la clave `park2017machinelearningbasednonlineardecompositionct`, distinta del nombre de archivo.
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/hyung2017ml.pdf (8 paginas, preprint arXiv; "Manuscript received XXX; revised XXX", p. 1)

## Que hace (3 lineas maximo)
Aproxima f_CT ≈ tau chi_Dm + f^t + gamma f^m (Observacion 2.1, Ec. 6) y entrena una U-net que mapea la plantilla analitica g^m (Ec. 15, el corrector MAC-BC de [23] = park2016MAR) al artefacto "solo-metal" f^m simulado (perdida L2, Ec. 16). La imagen corregida es f_CT - gamma f~^m, con gamma escalar elegido minimizando la energia de gradiente fuera del metal (Ec. 18). Entrena con 690 imagenes simuladas de dos insertos de hierro en pelvis real, 2D haz paralelo.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; supuestos que limitan su traslado al canal T:
- Geometria 2D de haz paralelo: "Considering a two-dimensional parallel beam, we define X-ray data" (Sec. II, p. 1). Haz en abanico o conico: NO ENCONTRADO EN EL PDF.
- Un solo lambda y un solo c fijos para todo el dataset: "Hence, we used fixed λ and c for all input g^m" (Sec. III.A, p. 4). El valor numerico de lambda: NO ENCONTRADO EN EL PDF; solo "λ is determined as in [23]" (Sec. II.C, p. 4).
- La mascara D_m sale por umbral simple sobre f_CT: "the D_m is extracted with simple thresholding from f_CT" (Sec. II.C, p. 4). Mascara suavizada o parcial: NO ENCONTRADO EN EL PDF.
- Simulacion sin scatter ni volumen parcial no lineal: "scattering and nonlinear partial volume effects were not considered" (Sec. III.A, p. 4).
- Todo el entrenamiento usa exactamente dos objetos metalicos en posicion simetrica: "690 CT images for two metallic objects in a symmetric position" (Sec. III.A, p. 4). No hay casos de un unico objeto.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 690 imagenes de entrenamiento, dos objetos metalicos | "we generated 690 CT images for two metallic objects in a symmetric position" | Sec. III.A, p. 4 |
| Espectro: anodo de tungsteno, 100 kVp; ruido Poisson | "X-ray tube voltage of 100 kV with added Poisson noise" | Sec. III.A, p. 4 |
| NRMSD Pelvis 1: 54.67 / 21.10 / 14.67 (sin corregir / MAC-BC / propuesto) | Tabla I, fila "Pelvis 1": "54.67 21.10 14.67" | Tabla I, p. 6 |
| NRMSD Pelvis 3: 65.83 / 26.68 / 16.43 | Tabla I, fila "Pelvis 3": "65.83 26.68 16.43" | Tabla I, p. 6 |

## Donde entra en mi tesis
Componente renderizador, canal de condicion fisico T del ControlNet (opcion B de la version 2). Es el precedente directo de usar la formula g^m = -R^{-1}[ln(sinh(lambda R chi_Dm)/(lambda R chi_Dm))] + c chi_Dm como *entrada* de una red, no solo como corrector analitico.

Respuestas a lo pedido:

1. **Construccion de la plantilla.** Ec. 15 (p. 3): g^m(x) = -R^{-1}[ ln( sinh(lambda R chi_Dm) / (lambda R chi_Dm) ) ](x) + c chi_Dm(x). No linealidad h(u) = ln(sinh u / u), identica a la del canal T, mas un termino c chi_Dm dentro del metal. Dos parametros: lambda ("depending on μ_m and η", p. 3) y c ("some constant", p. 3). lambda se determina "as in [23]" (p. 4), es decir, por el procedimiento de park2016MAR, que usa f_CT; c se calcula como promedio sobre D_m con f^m (Ec. 17, p. 4). En entrenamiento ambos se fijan para todo el dataset (p. 4). Un solo valor de lambda, una sola imagen g^m como entrada; varios lambda como canales: NO ENCONTRADO EN EL PDF. 2D por imagen axial con haz paralelo (p. 1); mascara binaria (chi_Dm, funcion caracteristica, p. 2) obtenida por umbral (p. 4). Discrepancia de signo: el recuadro de la Fig. 4 (p. 5) escribe "-R^{-1}[-ln(...)]", que no coincide con la Ec. 15; se toma la Ec. 15 como referencia.
2. **Como entra a la red.** g^m es la *unica* entrada de la U-net y la salida es f~^m (no residual; f_CT no entra a la red): "the goal is to learn the map from the formula-based artifact g^m to the corresponding true artifact f^m" (p. 3). Perdida L2 (Ec. 16). U-net con conv 3x3 + ReLU, max pooling 2x2, average unpooling, concatenacion, conv 1x1 final, zero-padding; canales 64-128-256 (Fig. 4, p. 4-5). RMSProp, lr 0.001, "weight decay of 0.9", mini-batch 20, 200 epocas, ~1 h en GTX-1080 (p. 4-5). Datos: CT reales de pelvis con dos insertos de hierro simulados, 690 imagenes, 256x256 px, campo 50x50 cm; test: protesis de cadera simulada de geometria similar, 4 pelvis (Tabla I). Metrica: NRMSD (%) fuera de D_m frente a imagen de referencia (p. 5). Cifras en Tabla I y en la Evidencia textual.
3. **Rayas en la plantilla sola.** No hay una afirmacion textual sobre g^m aislado. Visualmente, la Fig. 4 (p. 5, panel "formula-based artifact") muestra g^m con banda oscura y rayas entre los dos objetos, y un panel "The difference between f^m and g^m" con diferencias residuales; esto es lectura de figura, no texto. Todas las geometrias son de varios objetos: dos cilindros de fluido (Fig. 1), dos de titanio (Fig. 2), tres de titanio + uno de hierro + hueso (Fig. 3), dos elipses de hierro (entrenamiento). Caso de un objeto convexo aislado, o advertencia sobre el: NO ENCONTRADO EN EL PDF. El texto atribuye el error g^m - f^m a la aproximacion lineal del modelo (p. 4) y menciona rayas residuales por photon starvation "along the X-ray line passing through both titanium inserts" (p. 3).
4. **Ablacion con/sin plantilla.** NO ENCONTRADO EN EL PDF. La unica comparacion es MAC-BC (la formula sola, usada como corrector) frente a la red alimentada con la formula (Tabla I, p. 6): por ejemplo Pelvis 2, 18.95 vs 13.60 NRMSD. No hay red entrenada sin g^m (por ejemplo, desde la mascara binaria o desde f_CT) para aislar el aporte de la plantilla.
5. **Limitaciones declaradas.** Ver tabla de Evidencia textual: photon starvation residual (p. 3), artefactos entre metal y hueso no tratados (p. 3), simulacion sin scatter (p. 4), datos de entrenamiento pequenos (p. 5), necesidad de mejorar el modelo directo (p. 6-8) y de estudios con pacientes (p. 8).

## Dudas para el asesor
- **Sentido inverso.** El paper usa g^m como entrada para *predecir* f^m (el artefacto) desde la mascara: es, de hecho, un generador de artefacto condicionado por geometria, la misma direccion que la sintesis. Esto apoya el canal T como condicion, pero la red de ellos produce f^m aislado (sin anatomia) y luego se escala con gamma; en la tesis el difusor debe componer artefacto y anatomia. Conviene presentar este paper como evidencia de que g^m es un buen *predictor* de f^m, no como validacion de condicionamiento de un difusor.
- **Fijar lambda sin la imagen.** El paper fija un unico lambda y un unico c para todo el dataset (p. 4) y deja que la red absorba la discrepancia; ademas la amplitud final la ajusta gamma por imagen (Ec. 18, que usa f_CT). Esto sugiere que un lambda fijo por material es aceptable *si* la red posterior aprende la escala. Pero el valor de lambda y como se obtuvo en concreto no aparecen (NO ENCONTRADO EN EL PDF), y solo hay un metal (hierro) en entrenamiento. ¿Basta con fijar lambda por material y normalizar T, declarandolo supuesto?
- **Unico tornillo.** Todos los ejemplos tienen dos o mas objetos; nada se dice de un objeto convexo aislado. Combinado con park2017characterization (Teo. 3.5: metal estrictamente convexo sin rayas), para un tornillo unico T podria aportar poco o nada de raya fuera del metal (solo efecto de forma y, si el corte axial del tornillo no es estrictamente convexo, algo de estructura). ¿Se acota la opcion B a cortes con varios tornillos, o se acepta que T sea casi radial en el caso de un tornillo y se reporta como limitacion?
- **Signo.** La Ec. 15 y el recuadro de la Fig. 4 difieren en un signo dentro del corchete. ¿Se adopta la Ec. 15 (coincide con park2016MAR) y se anota la errata?
- **Tipo de fuente.** Preprint arXiv v1 sin DOI ni revision por pares evidente en el PDF. ¿Se cita solo como precedente metodologico?

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Objetivo | "we propose an implant-specific method that extracts beam-hardening artifacts from CT images" | Abstract, p. 1 |
| Idea central | "can be approximately extracted by subtracting artifacts generated exclusively by metals" | Abstract, p. 1 |
| No requiere imagen sin artefacto | "The proposed method is not designed to identify ground-truth CT images" | Abstract, p. 1 |
| Datos (resumen) | "real CT scans of pelvises containing simulated hip prostheses" | Abstract, p. 1 |
| Arquitectura | "we adopt a multi-scale convolutional network, called U-net [28]" | Sec. I, p. 1 |
| Geometria | "Considering a two-dimensional parallel beam, we define X-ray data" | Sec. II, p. 1 |
| Modelo polienergetico | "P_f(φ,s) = −ln( ∫ η(E) e^{−R f_E(φ,s)} dE )" | Ec. 1, p. 2 |
| Reconstruccion | "f_CT(x) := R^{-1} P_f(x)" (FBP) | Ec. 2, p. 2 |
| Modelo de dos materiales | "f_E(x) = μ_t(E) χ_{D_t}(x) + μ_m(E) χ_{D_m}(x)" | Ec. 3, p. 2 |
| Observacion 2.1 | "f_CT(x) ≈ τ χ_{D_m}(x) + f^t(x) + γ f^m(x)" | Ec. 6, p. 2 |
| Sin tejido | "In the absence of tissue ... τ = 0 and γ = 1" | Obs. 2.1, p. 2 |
| Fig. 1, gamma | "f_CT − γ f^m with γ = 0.4" | Fig. 1, p. 2 |
| Fig. 1, ventana | "(C=-1000 HU/W=4000 HU for CT images.)" | Fig. 1, p. 2 |
| Equipo Fig. 1 | "industrial CT scanner (DUKIN, Korea) with an X-ray tube voltage of 100 kV" | Sec. II.A, p. 2 |
| Corriente Fig. 1 | "a tube current of 12 mA" | Sec. II.A, p. 2 |
| Fantoma Fig. 1 | "two cylinders filled with highly attenuating fluid" | Sec. II.A, p. 2 |
| Relacion lineal | "μ_m(E^c) ≈ γ μ_m(E^m) + τ, for (φ,s) ∈ supp(Rχ_{D_m})" | Ec. 12, p. 3 |
| Fig. 2, parametros | "approximated by the line γμ_m(E^m)+τ with γ = 0.65 and τ = 0.051" | Sec. II.A, p. 3 |
| Photon starvation residual | "there remain streaking artifacts along the X-ray line passing through both titanium inserts" | Sec. II.A, p. 3 |
| Fig. 3, objetos | "three titanium inserts, one iron insert, and one bone insert" | Sec. II.A, p. 3 |
| Limitacion metal-hueso | "f^m cannot deal with artifacts between metallic inserts and bone" | Sec. II.A, p. 3 |
| Fig. 3, gamma | "f_CT − γf^m with γ = 0.74 at different window levels" | Fig. 3, p. 4 |
| Fig. 3, ventanas | "C=-500 HU/W=3000 HU for (a), (b) and (c), and C=2500 HU/W=6000 HU" | Fig. 3, p. 4 |
| Necesidad de prior | "the number of variations is too great to allow the features to be learned" | Sec. II.B, p. 3 |
| Plantilla g^m | "g^m(x) = −R^{-1}[ ln( sinh(λRχ_{D_m}) / (λRχ_{D_m}) ) ](x) + c χ_{D_m}(x)" | Ec. 15, p. 3 |
| Parametros lambda, c | "λ is the parameter depending on μ_m and η, and c is some constant" | Sec. II.B, p. 3 |
| Sin conocimiento previo | "approximated without the use of any prior knowledge of μ_m and η" | Sec. II.B, p. 3 |
| Mapeo aprendido | "learn the map from the formula-based artifact g^m to the corresponding true artifact f^m" | Sec. II.B, p. 3 |
| Perdida | "Err(Υ) = ‖f^m − Υ(g^m)‖²_{L²(R²)}" | Ec. 16, p. 3 |
| Capas | "two convolutions with a 3×3 window, each followed by a rectified linear unit" | Sec. II.B, p. 3-4 |
| Pooling | "2×2 max pooling with strides of two in each direction" | Sec. II.B, p. 4 |
| Unpooling | "the average unpooling is used instead of max pooling" | Sec. II.B, p. 4 |
| Padding | "every convolution in our network is performed with zero-padding" | Sec. II.B, p. 4 |
| Canales | Bloques "64", "128", "256" y "Conv 1 × 1" | Fig. 4, p. 5 |
| Mascara | "D_m is extracted with simple thresholding from f_CT" | Sec. II.C, p. 4 |
| lambda | "λ is determined as in [23]" | Sec. II.C, p. 4 |
| c | "c is computed as the average value over D_m" | Ec. 17, p. 4 |
| Criterio para gamma | "find the γ minimizing the function Φ" (gradiente de f_CT − γf~^m fuera de D_m) | Ec. 18, p. 4 |
| Origen del error g^m − f^m | "linear approximation for nonlinear variation in the attenuation coefficient" | Sec. II.C, p. 4 |
| Datos de test | "tested on real CT images of pelvises containing two simulated metallic (iron) inserts" | Sec. III.A, p. 4 |
| Espectro | "η for the tungsten anode generated at a tube voltage of 100 kVp" | Sec. III.A, p. 4 |
| Exclusiones de simulacion | "scattering and nonlinear partial volume effects were not considered" | Sec. III.A, p. 4 |
| Etiqueta | "We took f^m as the label" | Sec. III.A, p. 4 |
| lambda y c fijos | "Hence, we used fixed λ and c for all input g^m" | Sec. III.A, p. 4 |
| Tamano del entrenamiento | "we generated 690 CT images for two metallic objects in a symmetric position" | Sec. III.A, p. 4 |
| Rotacion | "θ = (−43°, −39°, ···, 45°)" | Sec. III.A, p. 4 |
| Distancia al origen | "r = (7cm, 9cm, ···, 15cm)" | Sec. III.A, p. 4 |
| Semiejes de elipses | "(a1,b1,a2,b2) = (2,2,2,2), (3,3,3,3), (4,4,4,4), (1,2,2,1), (2,3,3,2), (3,4,4,3)" | Sec. III.A, p. 4 |
| Campo de vision | "with an image size of 50×50 cm" | Sec. III.A, p. 4 |
| Test | "CT images for a simulated hip prosthesis, with geometry similar to the training set" | Sec. III.A, p. 4 |
| Optimizador | "minimized using the RMSPropOptimizer [29] with a learning rate of 0.001" | Sec. III.B, p. 4 |
| Regularizacion y batch | "weight decay of 0.9, and mini-batch size of 20" | Sec. III.B, p. 4 |
| Epocas | "We used 200 epochs to train the network" | Sec. III.B, p. 4-5 |
| Hardware | "a GPU (NVIDIA GTX-1080, 8GB) system" | Sec. III.B, p. 5 |
| Tiempo | "It required approximately one hour to train our network" | Sec. III.B, p. 5 |
| Resolucion | "256 × 256 pixel CT images" | Sec. III.C, p. 5 |
| Datos pequenos | "Although we use a relatively small training data" | Sec. III.C, p. 5 |
| Convergencia | "L² error converged and that beam-hardening artifacts in test image were reduced" | Sec. III.C, p. 5 |
| Limitacion de MAC-BC | "MAC-BC still retained some streaking artifacts, owing to model's assumption" | Sec. III.C, p. 5 |
| Metrica | "normalized root mean square difference (NRMSD) [17] on the outside of D_m" | Sec. III.C, p. 5 |
| Resultado | "The proposed method obtained the lowest NRMSD in all cases" | Sec. III.C, p. 5 |
| NRMSD Pelvis 1 | "54.67 21.10 14.67" (sin corregir / MAC-BC / propuesto) | Tabla I, p. 6 |
| NRMSD Pelvis 2 | "46.68 18.95 13.60" | Tabla I, p. 6 |
| NRMSD Pelvis 3 | "65.83 26.68 16.43" | Tabla I, p. 6 |
| NRMSD Pelvis 4 | "46.87 24.96 16.87" | Tabla I, p. 6 |
| Ventana Fig. 7 | "(C=1000 HU/W=3000 HU.)" | Fig. 7, p. 7 |
| Variedad baja dimensional | "can be assumed to lie on a low-dimensional submanifold M" | Sec. IV, p. 6 |
| Sin ground truth clinico | "there are no available ground-truth CT images for deep learning" | Sec. IV, p. 6 |
| Mejora pendiente | "could be modified by enhancing the forward model" | Sec. IV, p. 6-8 |
| Estudios con pacientes | "Various experimental studies with patients will be required" | Sec. IV, p. 8 |
| Haz en abanico / conico | NO ENCONTRADO EN EL PDF | — |
| Valor numerico de lambda | NO ENCONTRADO EN EL PDF | — |
| Valor numerico de c | NO ENCONTRADO EN EL PDF | — |
| Varios lambda como canales | NO ENCONTRADO EN EL PDF | — |
| Mascara suavizada | NO ENCONTRADO EN EL PDF | — |
| Caso de un unico objeto / objeto convexo aislado | NO ENCONTRADO EN EL PDF | — |
| Ablacion con/sin plantilla | NO ENCONTRADO EN EL PDF | — |
| Numero de imagenes de test | NO ENCONTRADO EN EL PDF (solo 4 filas "Pelvis 1-4" en Tabla I) | — |
| DOI | NO ENCONTRADO EN EL PDF | — |
