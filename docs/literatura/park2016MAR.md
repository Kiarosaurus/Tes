# park2016MAR — Metal Artifact Reduction for Polychromatic X-ray CT Based on a Beam-Hardening Corrector

- **DOI / URL:** 10.1109/TMI.2015.2478905 (impreso en p. 480 del PDF: "Digital Object Identifier 10.1109/TMI.2015.2478905")
- **Nivel de lectura:** 2 (metodo) — ajustado desde el 3 sugerido: la formula del corrector (Ec. 15/19) es practicamente el canal T que la tesis evalua, asi que se leyo como metodo y no como contexto.
- **Leido a fondo por la autora:** no
- **PDF:** papers/park2016MAR.pdf (8 paginas, IEEE TMI vol. 35, no. 2, pp. 480-487, feb. 2016)

## Que hace (3 lineas maximo)
Deriva un corrector analitico de beam hardening que depende solo de la geometria del metal: phi_{D,lambda} = -R^{-1}[ ln( sinh(lambda R chi_D) / (lambda R chi_D) ) ] (Ec. 15; multimaterial en Ec. 19). El unico parametro (lambda, uno por material) se estima por imagen minimizando un funcional ponderado sobre f_CT - phi fuera del metal (Ec. 17-18). Se resta de la imagen FBP sin usar el sinograma; se prueba en simulaciones 2D y fantomas fisicos en un CT industrial de haz conico.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; los supuestos que limitan su uso como prior son:
- Tejidos blandos independientes de la energia fuera del metal: "fE ≈ fE0 (energy independent) outside the metal region D" (Sec. II.A, p. 481). Ignora el beam hardening del hueso: "neglect of the polychromatic attenuation of bone" (Sec. III.A, p. 483), relevante en pelvis.
- lambda constante en energia: "Assuming that λ is approximately independent of E" (Sec. II.A, p. 482). Ademas, la aproximacion con sinh viene de reemplazar el espectro por una ventana uniforme de ancho 2h centrada en E0 (Ec. 10-12, p. 481-482).
- Geometria 2D de haz paralelo: "for a two-dimensional parallel beam system" (Sec. I, p. 480).
- Excluye otras fuentes de artefacto: "Other effects such as scattering and photon starvation are neglected" (Sec. III, p. 483); el residuo en fantomas se atribuye a "scattering, noise and our modeling error in (14)" (Sec. III.B, p. 484).
- lambda se estima con la imagen de CT: el funcional Phi(lambda) usa f_CT (Ec. 17, p. 482). No hay regla cerrada para fijar lambda sin imagen.

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Rango de energia de la simulacion: 20-80 keV | "projection data P in (1) is generated at energy range between 20–80 keV" | Sec. II.A, p. 481 (Fig. 1) |
| lambda optimo = 82.12 (Shepp-Logan, dos discos de oro) | "significantly reduced when λ = 82.12, which is the optimal value" | Sec. II.B, p. 483 |
| lambda fijos en fantoma: Al 0.3, Cu 4.1, Mo 5.5, Fe 3 | "λ1 = 0.3 for aluminum (D1), λ2 = 4.1 for copper (D2)" | Sec. III.B, p. 484 (Ec. 22) |
| NRMSD pelvis: sin corregir 12.19%, propuesto 5.50% | Tabla I, fila "Pelvis": "12.19 8.08 7.55 7.54 5.50" | Tabla I, p. 486 |
| MAD Phantom1 ROI2: 378.98 HU sin corregir, 115.27 HU propuesto | Tabla II, fila "Phantom1(ROI2)": "378.98 156.95 130.76 115.27" | Tabla II, p. 486 |

## Donde entra en mi tesis
Componente renderizador, canal de condicion fisico del ControlNet. La Ec. 15 tiene exactamente la forma T = -FBP[h(lambda R(M))] con h(x) = ln(sinh(x)/x), y depende solo de la mascara chi_D y de lambda; el paper la presenta como prior geometrico: "streaking artifacts ... can be characterized in term of the geometry of the metallic subject D" (Sec. II.B, p. 482). Las rayas viven fuera del metal: "streaking artifacts due to beam hardening are straight lines tangent to the boundaries" (Sec. II.B, p. 482), y Fig. 1 (p. 481) muestra phi para pelvis con dos objetos de titanio simulados. Esto respalda que el canal T aporte estructura espacial fuera de M (coherente con B_delta), sin fijar un ancho de banda: 12 mm / B_delta = NO ENCONTRADO EN EL PDF.

**Se puede usar el termino de forma directa, solo desde la mascara y sin la imagen de CT?** Parcialmente.
- *La forma si*: phi_{D,lambda} se calcula con proyeccion de chi_D, la no linealidad ln(sinh(x)/x) y FBP, sin sinograma, espectro ni f_CT (Ec. 15/19). El paper afirma ademas que "the structure of streaking artifacts in φD,λ does not change with λ" (Sec. II.B, p. 482), de modo que el patron espacial de rayas es una funcion de la mascara.
- *La amplitud no*: el paper estima lambda por imagen con f_CT (Ec. 17-18, metodo de Newton). Solo indica que el valor inicial lambda0 "can be determined by taking account of the energy range" del haz y del coeficiente del metal (Sec. II.B, p. 483), sin dar una formula ni valores para titanio o acero: NO ENCONTRADO EN EL PDF. Las unidades y la discretizacion de R chi_D, de las que depende la escala de lambda (82.12 en simulacion frente a 0.3-5.5 en fantomas), tampoco se reportan: NO ENCONTRADO EN EL PDF.
- *Conclusion operativa*: usar T solo desde M es una extrapolacion de la tesis, no un uso validado en el paper. Para condicionar, hay que fijar o muestrear lambda (o normalizar T) con un criterio propio y declararlo como supuesto.

Otros datos experimentales:
- Simulaciones con ruido Poisson, coeficientes de atenuacion de [17] y espectros de [8] (Sec. III, p. 483).
- Fantomas numericos: pelvis clinica con dos discos de titanio, mandibula con tres discos de oro, Shepp-Logan con oro y hierro, y Shepp-Logan con dos rectangulos de hierro (Fig. 5, p. 484).
- Fantomas fisicos en CT industrial de haz conico X-eye 7000 PCT (SEC Co., Korea): 150 kVp/650 µA y 100 kVp/400 µA (Fig. 7-8, p. 485-486).
- No incluye pacientes con implantes reales: "Further experimental work with patients is also needed" (Sec. IV, p. 486).

## Dudas para el asesor
- Ec. 15 describe un artefacto residual de beam hardening bajo supuestos de espectro uniforme y lambda constante; ¿basta como prior *aproximado* para condicionar al difusor, aunque ignore el hueso y el scatter, que en pelvis no son despreciables?
- Sin f_CT no hay como estimar lambda. ¿Fijar un lambda por material (titanio/acero) a partir del espectro, muestrearlo en un rango, o normalizar T a amplitud unitaria y dejar que la red aprenda la escala?
- El paper es 2D de haz paralelo; la tesis trabaja en 2.5D con CT clinico de haz conico/helicoidal. ¿Aceptable calcular T corte a corte con proyeccion paralela, declarandolo como aproximacion?
- ¿Usar Tabla I (pelvis 12.19% -> 5.50% NRMSD) solo como evidencia de que el corrector captura buena parte del artefacto simulado, sin presentarla como validacion clinica?

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Objetivo | "correct beam hardening artifacts caused by the presence of metal in polychromatic" | Abstract, p. 480 |
| Sin espectro conocido | "Without prior knowledge of the spectrum parameters or energy-dependent attenuation coefficients" | Abstract, p. 480 |
| Modelo polienergetico de proyeccion | "P(φ, s) = −ln( ∫ η(E) exp{−Rf_E(φ, s)} dE )" | Ec. 1, p. 480 |
| Geometria | "for a two-dimensional parallel beam system" | Sec. I, p. 480 |
| Descomposicion del artefacto | "R^{-1}[P − Rf_target] indicates the artifacts" | Ec. 3, p. 480 |
| Corrector propuesto (multimaterial) | "we propose a beam hardening corrector φD,λ expressed by" | Sec. I, p. 480 (Ec. 4) |
| Definicion de lambda_i | "λi is an unknown parameter that depends on the energy-dependent attenuation value" | Sec. I, p. 480 |
| Mascara del metal | "χDj denotes the characteristic function of Dj; χD = 1 in Dj" | Sec. I, p. 480 |
| Espectro normalizado | "η(E) = I0(E)/ ∫ I0(E′)dE′ indicates the normalized energy spectrum" | Sec. II, p. 481 |
| Supuesto tejidos blandos | "fE ≈ fE0 (energy independent) outside the metal region D" | Sec. II.A, p. 481 |
| Definicion de alpha | "α = (1/(E−E0)) ∫ (df^metal/dE′)dE′ depends on the spectral attenuation coefficient" | Ec. 9, p. 481 |
| Ventana uniforme del espectro | "η̃h(E) = 1/2h if |E − E0| < h, 0 otherwise" | Ec. 11, p. 481 |
| Relacion lambda-alpha | "where λ = −αh" | Sec. II.A, p. 482 |
| Supuesto lambda constante | "Assuming that λ is approximately independent of E" | Sec. II.A, p. 482 |
| No linealidad | "≈ −ln( sinh(λRχD(φ, s)) / λRχD(φ, s) )" | Ec. 13, p. 482 |
| Corrector monomaterial | "φD,λ(x) = −R^{-1}[ ln( sinh(λRχD) / λRχD ) ](x)" | Ec. 15, p. 482 |
| Espectro de Fig. 2: 80 kVp, W; E0 = 45 keV, h = 35 | "tungsten anode generated at a tube voltage of 80 kVp" | Fig. 2, p. 482 |
| Fig. 2: parametros de ventana | "η̃h(E) in (11) is generated at E0 = 45 keV and h = 35" | Fig. 2, p. 482 |
| Fig. 3: E0 = 50 keV, h = 25 | "E0 = 50 keV and h = 25" | Sec. II.A, p. 482 |
| Modelo de proyeccion ajustado | "P̃ closely match with P" | Sec. II.A, p. 482 |
| Rango de energia simulado | "generated at energy range between 20–80 keV" | Sec. II.A, p. 481 |
| Fig. 1: pelvis con titanio simulado | "clinical CT image of pelvis containing two simulated metallic objects (titanium)" | Fig. 1, p. 481 |
| Ventana de visualizacion | "same window center and width (C = 2000 HU/W = 8000 HU)" | Fig. 1, p. 481 |
| Algoritmo paso 1 | "Segment the metal region D in fCT" | Sec. II.B, p. 482 |
| Algoritmo paso 2 | "Determine the best λ in such a way that φD,λ alleviates the streaking" | Sec. II.B, p. 482 |
| Funcional de ajuste (fuera del metal) | "Φ(λ) = ∫_{R²\D} |W(x)∇(fCT(x) − φD,λ(x))|² dx" | Ec. 17, p. 482 |
| Peso laplaciano | "W(x) = ∇²φD,λ0(x) for some fixed λ0" | Sec. II.B, p. 482 |
| Estructura independiente de lambda | "the structure of streaking artifacts in φD,λ does not change with λ" | Sec. II.B, p. 482 |
| Rayas tangentes | "streaking artifacts due to beam hardening are straight lines tangent to the boundaries" | Sec. II.B, p. 482 |
| Dos discos: cuatro tangentes | "there are four tangent lines touching two different points on the boundary" | Sec. II.B, p. 482 |
| Segmentacion | "the simple thresholding method suffices to extract the metal region D" | Sec. II.B, p. 483 |
| Optimizacion | "solved using the standard Newton's method with the initial value λ0" | Sec. II.B, p. 483 |
| Eleccion de lambda0 | "can be determined by taking account of the energy range of incident X-ray" | Sec. II.B, p. 483 |
| lambda optimo en simulacion | "significantly reduced when λ = 82.12, which is the optimal value" | Sec. II.B, p. 483 |
| Multimaterial: N parametros | "λ := (λ1, . . . , λN) is a sequence of parameters" | Ec. 19, p. 483 |
| Reduccion a k materiales | "can be simplified into k unknown parameters" | Remark 2.1, p. 483 |
| Ruido en simulaciones | "projection data P in (1) containing Poisson noise" | Sec. III, p. 483 |
| Fuentes de atenuacion/espectro | "attenuation coefficients given in [17] and source spectra described in [8]" | Sec. III, p. 483 |
| Efectos ignorados | "Other effects such as scattering and photon starvation are neglected" | Sec. III, p. 483 |
| Reconstruccion | "The fCT is computed by the standard FBP" | Sec. III, p. 483 |
| Escaner de fantomas | "industrial cone-beam CT system (X-eye 7000 PCT, SEC CO., Korea)" | Sec. III, p. 483 |
| Sin sinograma | "corrected CT images are obtained without using the projection data" | Sec. III, p. 483 |
| Numero de fantomas numericos | "Four different numerical phantoms containing metallic materials" | Sec. III.A, p. 483 |
| Referencia sin artefactos | "reference images (artifact-free images) were generated by polychromatic simulation" | Sec. III.A, p. 483 |
| Limitacion: hueso | "neglect of the polychromatic attenuation of bone" | Sec. III.A, p. 483 |
| Hueso corregible si se segmenta | "can be removed by applying the proposed method using segmented bone" | Sec. III.A, p. 483 |
| Comparadores | "comparison among LI, NMAR, EBHC and the proposed method" | Sec. III.A, p. 483 |
| NMAR: imagen prior | "obtained by simple thresholding after fCT is smoothed with the Gaussian filter" | Sec. III.A, p. 483 |
| EBHC: parametros | "compute the parameter c = (c1, c2, c3) ∈ R³ minimizing" | Ec. 21, p. 483 |
| Costo computacional | "requires backprojection at each iteration to compute the optimal parameter λ" | Sec. III.A, p. 484 |
| Costo EBHC | "EBHC requires one additional projection of the metallic objects and two additional backprojections" | Sec. III.A, p. 484 |
| Fantomas de Fig. 5 | "clinical CT image of pelvis with the two disk-shaped numerical metallic objects (titanium)" | Fig. 5, p. 484 |
| Fantoma de mandibula | "jaw phantom [37] with three disk-shaped metallic objects (gold)" | Fig. 5, p. 484 |
| Energias Fig. 5 | "simulated at energy range between 20–80 keV" | Fig. 5, p. 484 |
| Fantoma fisico superior | "four different metallic rods (aluminum (Al), copper (Cu), molybdenum (Mo) and iron" | Sec. III.B, p. 484 |
| Fantoma fisico inferior | "bottom phantom consists of aluminum only" | Sec. III.B, p. 484 |
| lambda por material | "λ1 = 0.3 for aluminum (D1), λ2 = 4.1 for copper (D2)" | Ec. 22, p. 484 |
| lambda por material | "λ3 = 5.5 for molybdenum (D3) and λ4 = 3 for iron (D4)" | Ec. 22, p. 484 |
| Residuo en fantomas | "remaining streaking artifacts are mainly due to scattering, noise and our modeling error" | Sec. III.B, p. 484 |
| Adquisicion fantomas Fig. 7 | "respectively acquired using 150 kVp at 650 µA" | Fig. 7, p. 485 |
| Adquisicion fantoma inferior | "100 kVp at 400 µA" | Fig. 7, p. 485 |
| Ventanas Fig. 7 | "C = 2000 HU/W = 8000 HU for CT images" | Fig. 7, p. 485 |
| Phantom1 | "made up of two materials-iron and aluminum based alloy" | Fig. 8, p. 486 |
| Adquisicion Phantom1 | "The uncorrected images is acquired using 100 kVp at 400 µA" | Fig. 8, p. 486 |
| Metrica simulacion: NRMSD fuera del metal | "normalized root mean square difference (NRMSD) [24] between the corrected and reference" | Sec. III.B, p. 485 |
| Region de NRMSD | "computed on the outside of the metal region D (See Table I)" | Sec. III.B, p. 485 |
| Metrica experimental: referencia rROI | "referencing the uncorrected image on the region (marked rROI in Fig. 8)" | Sec. III.B, p. 485 |
| Metrica experimental: MAD | "mean absolute deviation (MAD) between the corrected and reference images" | Sec. III.B, p. 485 |
| Tabla I, Jaw (sin corr./LI/NMAR/EBHC/prop., %) | "28.58 32.61 26.77 21.30 20.42" | Tabla I, p. 486 |
| Tabla I, Pelvis (%) | "12.19 8.08 7.55 7.54 5.50" | Tabla I, p. 486 |
| Tabla II, ROI1 (sin corr./NMAR/EBHC/prop., HU) | "135.76 114.72 101.56 95.18" | Tabla II, p. 486 |
| Tabla II, ROI2 (HU) | "378.98 156.95 130.76 115.27" | Tabla II, p. 486 |
| Conclusion: sin sinograma ni espectro | "removes beam-hardening artifacts without the use of sinogram data" | Sec. IV, p. 486 |
| Dependencia de la segmentacion | "The performance of our method depends on segmenting the metallic objects" | Sec. IV, p. 486 |
| Geometria conocida: pose rigida | "a rigid body in three-dimensional space has six degrees of freedom" | Sec. IV, p. 486 |
| Otras fuentes no tratadas | "scattering, photon noise, and nonlinear partial volume effects" | Sec. IV, p. 486 |
| Falta validacion en pacientes | "Further experimental work with patients is also needed" | Sec. IV, p. 486 |
| Tamano de pixel / matriz / numero de vistas | NO ENCONTRADO EN EL PDF | — |
| Unidades de lambda y discretizacion de R chi_D | NO ENCONTRADO EN EL PDF | — |
| Formula o valores de lambda0 (o lambda para titanio/acero en datos reales) | NO ENCONTRADO EN EL PDF | — |
| Tiempo de computo en segundos | NO ENCONTRADO EN EL PDF | — |
| Ancho de banda peri-metal (B_delta, 12 mm) | NO ENCONTRADO EN EL PDF | — |
| Datos de pacientes con implantes reales | NO ENCONTRADO EN EL PDF | — |
