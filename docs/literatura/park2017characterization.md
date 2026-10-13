# park2017characterization — Caracterizacion microlocal de las rayas por metal en CT (endurecimiento del haz)

- **DOI / URL:** NO ENCONTRADO EN EL PDF. El PDF es un preprint; cabecera de p. 1: "Communications on Pure and Applied Mathematics, 0001–0027 (PREPRINT)", "© 2016 Wiley Periodicals, Inc."; p. 27: "Received February 2016". Volumen, numero y paginas finales: NO ENCONTRADO EN EL PDF.
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/park2017characterization.pdf

## Que hace (3 lineas maximo)

Analisis matematico (sin entrenamiento, sin datos) de las rayas por metal en CT 2D de haz paralelo: descompone la FBP del dato policromatico en imagen limpia mas un termino de artefacto que depende solo de la mascara del metal (Prop. 2.1, Ec. 2.10). Con el conjunto de frente de onda prueba que las rayas solo aparecen sobre rectas tangentes a dos puntos distintos de la frontera del metal (Teo. 3.3) y que un metal estrictamente convexo no produce rayas (Teo. 3.5). Ilustra con simulaciones sobre Shepp-Logan (titanio) y una CT dental clinica, sin cifras de error.

## Restriccion o supuesto clave

No es un paper generativo. Supuestos explicitos del modelo que fijan el alcance de la plantilla T:

- **Sin scatter ni ruido** en el modelo base: *"Assuming that there is no scattered radiation or noise"* (Sec. 1, p. 3, antes de Ec. 1.3).
- **Linealizacion en energia, solo dentro del metal:** f_E(x) ≈ f_E0(x) + α(E − E0)χ_D(x) (Ec. 1.5, p. 3; Ec. 2.7, p. 5). Fuera del metal ∂f_E/∂E = 0 (Ec. 2.5, p. 5). α = ∂f_E/∂E en D, constantes α_j < 0 (p. 5).
- **α constante e independiente de E; espectro rectangular:** *"we assume that α is constant, independent of E, and η = 1/2ε"* (p. 4); η = 1/2ε en [E0 − ε, E0 + ε] y 0 fuera (p. 5), con ε = (Ē − E̲)/2 (Ec. 2.1, p. 4).
- **Geometria 2D de haz paralelo:** transformada de Radon en (φ, s), φ ∈ (−π, π] (Ec. 1.1, p. 2). Fan beam, cone beam o 3D para el termino de artefacto: NO ENCONTRADO EN EL PDF.
- **Los teoremas de rayas asumen fronteras C∞ y la serie truncada:** Teo. 3.3 pide dominios *"strictly convex and disjoint bounded domains"* con frontera C∞ (p. 12) y f_MA como suma finita (Ec. 3.2); los autores declaran que este ultimo supuesto *"should be removed"* (Remark 3.4, p. 15).
- **"Raya" se define como singularidad (frente de onda), no por magnitud** (Def. 3.2, Ec. 3.4, p. 11). El paper es cualitativo: *"the quantitative analysis on the metal artifacts will be required"* (Sec. 5, p. 22).

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| ∂f_E/∂E ≈ −8.16 cm^-1/keV para oro en [40 keV, 60 keV] | *"∂f_E/∂E ≈ −8.16 cm^-1/keV on [40keV, 60keV] for gold [30]"* | Sec. 1, p. 3 |
| Simulacion entre 20 y 80 keV (titanio, Shepp-Logan) | *"generated at energy range between 20 and 80 keV"* | Fig. 3.1, p. 13 |
| Dos dominios convexos disjuntos: cuatro rectas tangentes comunes | *"there are four different tangent lines touching both the metal domains"* | Sec. 3, p. 17 |

## Donde entra en mi tesis

Fundamento analitico del canal de condicion "plantilla de endurecimiento del haz" T calculado solo desde la mascara M (renderizador, ControlNet). Respuestas a las preguntas del encargo:

1. **Formula del termino de artefacto.** CONFIRMADA en estructura, con matices.
   - Forma en la introduccion (Ec. 1.6, p. 4): −(1/4π) R* I^{-1} [ ln( sinh((α/2)(Ē − E̲) Rχ_D) / ((α/2)(Ē − E̲) Rχ_D) ) ].
   - Forma en la Prop. 2.1 (Ec. 2.10, p. 6): f_MA(x) = −(1/8π²) ∫∫ |ω| F[ ln( sinh(αε Rχ_D(φ,·)) / (αε Rχ_D(φ,·)) ) ](ω) e^{iωx·θ} dω dφ, con la convencion *"ln(sinh β / β) is understood to be 0 when β = 0"* (p. 6). La descomposicion es f_CT = f_E0 + f_MA (Ec. 2.9).
   - (1/4π) R* I^{-1} es la formula FBP (Ec. 1.2, p. 2), y χ_D es la funcion caracteristica del metal (p. 4). Por tanto T = −FBP[h(λ R(M))] coincide con Ec. 1.6 / 2.10 tomando M = χ_D, R = transformada de Radon paralela y λ = αε = (α/2)(Ē − E̲).
   - **h(u) = ln(sinh u / u) aparece literalmente** como integrando (Ec. 1.6, 2.10, 2.11, 2.12, y en el corrector φ_{D,λ} de p. 9). No es una derivacion de la ficha. El log es natural ("ln").
   - Supuestos que la producen: sin scatter ni ruido (Ec. 1.3), atenuacion lineal en E solo dentro del metal con α constante (Ec. 1.5 / 2.7), espectro uniforme/rectangular η = 1/2ε (p. 4-5). La derivacion es Ec. 2.11 (p. 6): integrar exp(−αE Rχ_D) sobre el espectro rectangular da el factor sinh(x)/x.
   - Matiz 1: en la teoria posterior (Sec. 3) el paper NO usa la forma cerrada sino una serie truncada reescalada con M = 1 (Ec. 2.26 y 3.2, p. 9-10); *"we assume f_MA = f_MA,N for technical convenience"* (p. 9).
   - Matiz 2 (observacion del extractor, no del paper): sinh(u)/u es par, asi que el signo de α (negativo, p. 5) no cambia h; el signo del termino lo fija el "−" delante de la FBP.
2. **λ.** En el corrector de [51] (p. 9-10) λ reemplaza a αε: φ_{D,λ} = −(1/4π) R* I^{-1}[ln(sinh(λRχ_D)/(λRχ_D))], y *"λ is an unknown parameter that depends on the energy-dependent attenuation"* ... *"and the spectrum of the X-ray source"* (p. 10). Valor numerico de λ o de αε para titanio, acero o cualquier metal: NO ENCONTRADO EN EL PDF. La unica cifra relacionada es ∂f_E/∂E ≈ −8.16 cm^-1/keV para oro en [40, 60] keV (p. 3); ε para un espectro clinico concreto: NO ENCONTRADO EN EL PDF. Unidades: α en cm^-1/keV, ε en keV y Rχ_D es una longitud, de modo que λRχ_D es adimensional (consistencia dimensional deducida por el extractor; el paper no lo enuncia).
3. **Condiciones geometricas de las rayas.**
   - Teo. 3.3 (p. 12-13): con D_j estrictamente convexos, disjuntos, frontera C∞, una recta de raya L_{φ,s} cumple dim(Span[Σ_(φ,s)(Rχ_D)]) = 2 (Ec. 3.8), lo que equivale a dos puntos distintos y, z ∈ ∂D con la misma direccion: *"L_φ,s is the straight line containing two points y and z"* (p. 13). Es condicion **necesaria**, no suficiente.
   - Resumen en la introduccion: rayas *"along the line tangent to boundaries of the metal region touching at least two different boundaries"* (p. 4).
   - Teo. 3.5 (p. 15): D con frontera C∞ conexa y estrictamente convexo => f_CT sin rayas (en el sentido del frente de onda). Texto: *"In the case of a single metallic object with a strictly convex boundary"* ... *"the reconstructed CT image has no streaking artifact"* (p. 16-17).
   - Dominios no suaves: un cuarto de disco produce rayas sobre las rectas que contienen sus lados rectos (Fig. 3.3, p. 16): *"Theorem 3.3 can be applied to a nonsmooth metal domain"* (pie Fig. 3.3). La Fig. 3.4 (p. 17) muestra elipse unica, dos elipses y un rectangulo de titanio. Que la elipse unica aparezca sin rayas y el rectangulo con rayas es lectura visual del extractor; el texto no comenta cada panel.
   - Un objeto convexo no queda libre de artefacto: para un disco D = {|x| < r0} la FBP *"is inhomogeneous in the homogeneous metal region"* (Sec. 5, p. 21, Ec. 5.1). Tal como esta escrita, Ec. 5.1 define g = 0 fuera de |x| < r0, es decir, el termino del disco quedaria confinado al metal. Se registra literal; la ficha no lo verifica.
   - En la figura 3.3 aparece ademas *"some shading artifacts near the boundary of D"* (p. 15).
4. **Experimentos.** Solo simulaciones numericas sobre el fantoma de Shepp-Logan con metal homogeneo de titanio (Fig. 2.1, 3.1, 3.4, 4.1), dato generado entre 20 y 80 keV con atenuacion de [30] y espectro de [8] (Fig. 3.1, p. 13), ventana de visualizacion [−0.2 0.6], truncaciones N = 2 y N = 10 (Fig. 2.1, p. 10), y una CT clinica dental de uno de los autores (Fig. 4.2, p. 20) evaluada solo de forma cualitativa. Fantomas fisicos en este paper: NO ENCONTRADO EN EL PDF (los *"Phantom experiments"* que menciona son de [51], p. 10, y la validez de Ec. 1.5 se apoya en [51], p. 4). Metricas cuantitativas (RMSE, HU, numero de vistas, tamano de imagen, numero de detectores): NO ENCONTRADO EN EL PDF.
5. **Limitaciones declaradas.**
   - Modelo base sin scatter ni ruido (p. 3). Scatter y ruido se tratan aparte en la Sec. 4 con modelos simplificados: scatter de Compton con fuente monocromatica y constante c (Ec. 4.2, siguiendo a Glover [23]), ruido como deltas discretas con constantes de Poisson (Ec. 4.5). Ambos tambien generan rayas tangentes; con scatter las rayas pueden aparecer *"between bones and metals, even when f_E = f_E0"* (Cor. 4.2, p. 19).
   - Inanicion de fotones: solo discusion cualitativa, citando [3, 43, 69] (p. 19-20).
   - Monoenergetico vs polienergetico: la condicion de ajuste perfecto exige rayos monocromaticos o ∂f_E/∂E = 0 (p. 3); el modelo es polienergetico solo via espectro rectangular y α constante.
   - 2D paralelo: todo se formula con la transformada de Radon paralela en el plano. Fan beam: NO ENCONTRADO EN EL PDF.
   - Supuesto de suma finita en el Teo. 3.3 (Remark 3.4, p. 15) y analisis solo cualitativo (Sec. 5, p. 22).

## Dudas para el asesor

- **Tornillo unico en un corte axial.** Segun el Teo. 3.5 (p. 15), si la seccion del tornillo es una region simplemente conexa, estrictamente convexa y de frontera C∞ (elipse ideal), el termino de endurecimiento del haz NO produce rayas en el sentido del frente de onda. Si produce inhomogeneidad (ejemplo del disco, Ec. 5.1) y sombreado cerca del borde (p. 15). Rayas con un solo tornillo solo aparecerian si la seccion no es estrictamente convexa o no es suave (rosca, cabeza hexagonal, corte oblicuo con lados casi rectos; cf. Fig. 3.3), o por scatter entre metal y hueso (Cor. 4.2), que T no modela. En la pelvis con placas y varios tornillos las rayas tangentes entre pares de objetos si se predicen (4 rectas por par de convexos, p. 17). Pregunta: aceptamos que T, con un tornillo aislado de seccion convexa, entregue un patron de sombreado sin rayas, o el canal debe complementarse (p. ej. con un termino de scatter tipo Ec. 4.2) para cubrir las rayas que se ven clinicamente con un solo implante?
- **λ libre.** El paper no da valor de λ (p. 10). Se fija λ por material y kVp desde tablas externas, se calibra sobre CLINIC-metal o se muestrea como parametro de aumentacion? Cualquier opcion es un supuesto que hoy no esta documentado.
- **Ec. 5.1 y la banda B_delta (~12 mm).** Si el termino de un disco aislado quedara confinado al metal (como sugiere Ec. 5.1 tal como esta escrita), T no aportaria senal fuera de la mascara para un tornillo convexo aislado. Conviene verificar numericamente esto antes de defender B_delta con este paper.
- **2D paralelo vs adquisicion helicoidal real.** El analisis no cubre fan beam ni 3D. Basta como plantilla aproximada por corte para un canal de condicion, o hay que declararlo como simplificacion en la tesis?
- **Snowballing (para que lo decida la autora; esta ficha no edita `_candidatos.md`):** [51] Park, Hwang, Seo, "Metal artifact reduction for polychromatic X-ray CT based on a beam hardening corrector", IEEE TMI 35(2):480-487, 2016, doi 10.1109/TMI.2015.2478905 (bibliografia, p. 25). Es la fuente del corrector φ_{D,λ} y de los experimentos con fantoma, y podria traer valores o un procedimiento de estimacion de λ.
- **Posible implicancia (no registrada por esta ficha):** confirma la forma de T y λ = αε, pero tambien limita lo que T puede afirmar: en un objeto convexo no hay rayas, λ no tiene valor y el modelo no incluye scatter. Esto podria tocar la redaccion del canal T y el argumento de B_delta. Lo decide la autora.

## Evidencia textual

| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Tesis central: rayas tangentes a dos fronteras | "produced along the line tangent to boundaries of the metal region touching at least two" | Abstract, p. 1 |
| Condicion suficiente de no existencia | "a sufficient condition for the nonexistence of the metal streaking artifacts" | Abstract, p. 1 |
| Causa: desajuste del modelo directo de la FBP | "caused mainly from the mismatch of the forward model of the filtered back-projection" | Abstract, p. 1 |
| Modelo de datos lineal (Ec. 1.1) | "P(φ, s) = Rf(φ, s) for (φ, s) ∈ (−π, π] × R" | Ec. 1.1, p. 2 |
| Formula FBP (Ec. 1.2) | "f = (1/4π) R* I^{-1} Rf" | Ec. 1.2, p. 2 |
| Sin scatter ni ruido (Ley de Beer, Ec. 1.3) | "Assuming that there is no scattered radiation or noise" | Sec. 1, p. 3 |
| η(E) = fraccion espectral | "η(E) denotes the fractional energy at photon energy E in the spectrum" | Sec. 1, p. 3 |
| Ajuste perfecto exige monocromatico o derivada nula | "we have either E̲ − Ē = 0 (monochromatic X-rays ...) or ∂f_E/∂E = 0" | Sec. 1, p. 3 |
| Cifra: oro, −8.16 cm^-1/keV en [40, 60] keV | "∂f_E/∂E ≈ −8.16 cm^-1/keV on [40keV, 60keV] for gold" | Sec. 1, p. 3 |
| Monocromatico dificil en clinica | "difficult to generate monochromatic X-rays for routine clinical use" | Sec. 1, p. 3 |
| Linealizacion en el metal (Ec. 1.5) | "f_E(x) ≈ f_E0(x) + α(E − E0)χ_D(x)" | Ec. 1.5, p. 3 |
| Definicion de α y χ_D | "χ_D is the characteristic function of D and α = ∂f_E/∂E in the metal" | Sec. 1, p. 4 |
| Validez de Ec. 1.5 remitida a [51] | "Phantom and numerical experiments show that (1.5) is a good approximation [51]" | Sec. 1, p. 4 |
| α constante y espectro rectangular | "we assume that α is constant, independent of E, and η = 1/2ε" | Sec. 1, p. 4 |
| Termino de artefacto (Ec. 1.6) | "−(1/4π) R* I^{-1}[ln( sinh((α/2)(Ē−E̲)Rχ_D) / ((α/2)(Ē−E̲)Rχ_D) )]" | Ec. 1.6, p. 4 |
| Rayas solo si D no es estrictamente convexo | "the reconstructed image contains streaking artifacts only if D is not strictly convex" | Sec. 1, p. 4 |
| Definicion de ε | "where ε = (Ē − E̲)/2" | Ec. 2.1, p. 4 |
| Derivada nula fuera del metal, α_j ≠ 0 dentro | "∂f_E/∂E = 0 if x ∉ D_j; α_j ≠ 0 if x ∈ D_j" | Ec. 2.5, p. 5 |
| Signo de α_j | "α_1, ..., α_J < 0 are constants depending on the metallic materials" | Sec. 2, p. 5 |
| Espectro uniforme | "let η in (2.1) be η = 1/2ε on [E0 − ε, E0 + ε] and 0 otherwise" | Sec. 2, p. 5 |
| Supuesto A1: soporte compacto | "f_E ∈ E'(R²) for all E ∈ [E0 − ε, E0 + ε]" | Sec. 2, p. 5 |
| Supuesto A2: contraste del metal, C > 1 | "f_E0(x) ≥ C sup f_E0(y) for some C > 1" | Sec. 2, p. 6 |
| Descomposicion (Ec. 2.9) | "f_CT(x) = f_E0(x) + f_MA(x)" | Prop. 2.1, p. 6 |
| f_MA = termino de artefacto metalico (Ec. 2.10) | "where f_MA represents the metal artifact term given by" | Prop. 2.1, p. 6 |
| Convencion en β = 0 | "ln(sinh β / β) is understood to be 0 when β = 0" | Prop. 2.1, p. 6 |
| Dato con factor sinh (Ec. 2.11) | "= Rf_E0(φ, s) − ln( sinh(αε Rχ_D(φ, s)) / (αε Rχ_D(φ, s)) )" | Ec. 2.11, p. 6 |
| No linealidad respecto de la geometria del metal | "f_CT in (2.9) is nonlinear with respect to the geometry of the metal region D" | Sec. 2, p. 6 |
| Dato desajustado P_MA (Ec. 2.12), conjunto G | "G := {(φ, s) ∈ (−π, π] × R : Rχ_D(φ, s) ≠ 0}" | Sec. 2, p. 7 |
| M ≥ 1 (Ec. 2.14) | "Note that M ≥ 1." | Sec. 2, p. 7 |
| Rango de t en el espacio de Sobolev | "For 0 < t < 1/2, let H^t((−π, π] × R) be the Hilbert space" | Sec. 2, p. 7 |
| Cota L2 (Ec. 2.21) | "≤ √|G| ln M ≤ √(2π diam(D)) ln M" | Ec. 2.21, p. 8 |
| Reescalado M = 1 | "From now on, for notational simplicity, we rescale M = 1." | Sec. 2, p. 9 |
| Truncaciones N = 2 y N = 10 | "f_MA,N for N = 2, 10 for the Shepp-Logan phantom containing two metallic objects" | Sec. 2, p. 9 |
| Supuesto de serie truncada | "we assume f_MA = f_MA,N for technical convenience" | Sec. 2, p. 9 |
| Corrector φ_{D,λ} de [51] | "φ_D,λ = −(1/4π) R* I^{-1}[ln( sinh(λRχ_D) / (λRχ_D) )]" | Sec. 2, p. 9 |
| Significado de λ | "λ is an unknown parameter that depends on the energy-dependent attenuation" | Sec. 2, p. 10 |
| λ depende tambien del espectro | "value of the object in D and the spectrum of the X-ray source" | Sec. 2, p. 10 |
| Experimentos con fantoma son de [51] | "Phantom experiments showed that the beam hardening corrector effectively reduced the streaking" | Sec. 2, p. 10 |
| Ventana de visualizacion comun (Fig. 2.1) | "f_MA and f_MA,N for N = 2, 10 are displayed with the same window" | Fig. 2.1, p. 10 |
| Definicion de raya (Def. 3.2, Ec. 3.4) | "is called a streaking artifact of f_CT in the sense of wavefront set" | Def. 3.2, p. 11 |
| Hipotesis del Teo. 3.3 | "Let D_1, ..., D_J be strictly convex and disjoint bounded domains" | Teo. 3.3, p. 12 |
| Condicion de raya (Ec. 3.8) | "dim(Span[Σ_(φ,s)(Rχ_D)]) = 2" | Teo. 3.3, p. 12 |
| Simulacion: titanio, Shepp-Logan | "Illustration of streaking artifacts in the presence of metallic objects (titanium)." | Fig. 3.1, p. 13 |
| Ventana de visualizacion [−0.2 0.6] | "reconstructed f_CT (right figure) with the display window [−0.2 0.6]" | Fig. 3.1, p. 13 |
| Rango de energia 20-80 keV | "the projection data P in (1.3) is generated at energy range between 20 and 80 keV" | Fig. 3.1, p. 13 |
| Fuente de atenuacion y espectro | "based on the experimental findings of the attenuation coefficient in [30] and source spectra" | Fig. 3.1, p. 13 |
| Interpretacion geometrica: dos puntos tangentes | "L_φ,s is the straight line containing two points y and z" | Sec. 3, p. 13 |
| Tangencia en un solo punto (vecindad) | "the line L_φ,s is tangent to at most one point on ∂D" | Fig. 3.2, p. 15 |
| Ejemplo no suave: cuarto de disco | "D = {x ∈ R² : |x| ≤ 1 and x_1, x_2 ≥ 0}" | Sec. 3, p. 15 |
| Rayas y sombreado en el cuarto de disco | "shows streaking artifacts along the lines L_0,0 and L_π/2,0 and some shading artifacts" | Sec. 3, p. 15 |
| Limitacion: suma finita | "Theorem 3.3 is proved under the assumption that f_MA is the finite sum" | Remark 3.4, p. 15 |
| Limitacion: supuesto a remover | "This assumption should be removed." | Remark 3.4, p. 15 |
| Teo. 3.5: estrictamente convexo sin rayas | "If D is strictly convex, then the CT image f_CT does not have the streaking" | Teo. 3.5, p. 15 |
| Teorema aplicable a dominio no suave | "This example shows that Theorem 3.3 can be applied to a nonsmooth metal domain." | Fig. 3.3, p. 16 |
| Rayas ligadas a la geometria de D | "the streaking artifacts in f_CT are related with the geometry of D" | Sec. 3, p. 16 |
| Objeto unico estrictamente convexo | "In the case of a single metallic object with a strictly convex boundary" | Sec. 3, p. 16 |
| ... sin rayas | "the reconstructed CT image has no streaking artifact." | Sec. 3, p. 17 |
| Dos dominios: cuatro tangentes | "there are four different tangent lines touching both the metal domains ∂D_1 and ∂D_2" | Sec. 3, p. 17 |
| Fig. 3.4: titanio, ventana [−0.2 0.6] | "with the display window [−0.2 0.6], respectively" | Fig. 3.4, p. 17 |
| Scatter de Compton tambien produce rayas | "Compton scattering can also cause streaking artifacts by altering the direction and energy" | Sec. 4, p. 17 |
| Modelo de scatter monocromatico | "simple model of Compton scattering using a monochromatic X-ray source" | Sec. 4, p. 18 |
| Constante de scatter c | "c is a positive constant representing the scattered intensities approximately" | Sec. 4, p. 18 |
| Justificacion (Glover 1982) | "the scattered radiations are relatively uniform for the round metallic materials" | Remark 4.1, p. 18 |
| Rango 0 ≤ s < 1/2 | "for all 0 ≤ s < 1/2 as N → ∞" | Sec. 4, p. 18 |
| Rayas por scatter entre hueso y metal | "can occur between bones and metals, even when f_E = f_E0" | Cor. 4.2, p. 19 |
| Modelo de ruido Poisson | "c_1, ..., c_K are positive constants that follow the Poisson probability distribution" | Sec. 4, p. 19 |
| Inanicion de fotones | "occurs when insufficient (possibly zero) photons reach the detector" | Sec. 4, p. 19-20 |
| Fig. 4.1: scatter y ruido, ventana [−0.2 0.6] | "due to (b) scattering and (c) noise with the display window [−0.2 0.6]" | Fig. 4.1, p. 20 |
| Validacion clinica cualitativa | "The presence of the streaking artifacts in the clinical CT image mostly agrees" | Fig. 4.2, p. 20 |
| Imagen clinica dental de un autor | "a CT image of the teeth and mandible of one of the authors" | Sec. 4, p. 20 |
| Valores singulares del Radon O(n^-1/2) | "the singular value {σ_n : n ∈ N} of R satisfies an estimate O(n^-1/2)" | Sec. 5, p. 21 |
| Disco: metal homogeneo reconstruido inhomogeneo | "is inhomogeneous in the homogeneous metal region" | Sec. 5, p. 21 |
| Disco de radio r0 (Ec. 5.1) | "the metal region is occupied in the disk D = {x : |x| < r0}" | Sec. 5, p. 21 |
| Ec. 5.1: g = 0 fuera del disco | "(x) if |x| < r0, 0 otherwise." | Ec. 5.1, p. 21 |
| Categorias de MAR | "inpainting methods, iterative reconstruction methods, and their variations and/or combinations" | Sec. 5, p. 21 |
| Limitacion: solo cualitativo | "the quantitative analysis on the metal artifacts will be required" | Sec. 5, p. 22 |
| Pendiente: geometria de mandibula | "it remains a future work to obtain the exact geometry of the mandible" | Sec. 5, p. 22 |
| Financiamiento | "Samsung Science & Technology Foundation (no. SSTF-BA1402-01)" | Acknowledgments, p. 23 |
| Fecha de recepcion | "Received February 2016." | p. 27 |
| Valor numerico de λ o αε | NO ENCONTRADO EN EL PDF | — |
| Fan beam / cone beam / 3D | NO ENCONTRADO EN EL PDF | — |
| Metricas cuantitativas de error (RMSE, HU, SSIM) | NO ENCONTRADO EN EL PDF | — |
| Parametros de muestreo (vistas, detectores, tamano de imagen) | NO ENCONTRADO EN EL PDF | — |
| Experimentos con fantoma fisico propios | NO ENCONTRADO EN EL PDF | — |
| DOI del articulo | NO ENCONTRADO EN EL PDF | — |
