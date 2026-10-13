# wang2021streak — Streak artifacts from non-convex metal objects in X-ray tomography

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. El PDF local es el preprint arXiv:2002.12210v2 [math.AP], 29 Dec 2020 (margen de p. 1). Revista, volumen y paginas (Pure Appl. Anal. 3(2):295-318, segun `_candidatos.md`): NO ENCONTRADO EN EL PDF.
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wang2021streak.pdf (22 paginas, version arXiv v2; "Date: January 1, 2021", p. 1)

## Que hace (3 lineas maximo)
Analisis microlocal (distribuciones conormales) del termino no lineal de endurecimiento del haz f_MA = R* I^{-1} F(R f) para un dominio metalico 2D D simplemente conexo y con frontera suave, incluyendo dominios NO estrictamente convexos. Muestra que los puntos de inflexion de la frontera generan cuspides en el sinograma y que el soporte singular de f_MA esta contenido en la frontera mas las rectas bitangentes y las tangentes en inflexiones (Teo. 1.1 / 2.1).

## Restriccion o supuesto clave
- Es un resultado puramente teorico en 2D con transformada de Radon de haz paralelo en R^2 (Sec. 3.1, p. 5). Geometria fan-beam, cone-beam o 3D: NO ENCONTRADO EN EL PDF.
- Requiere D simplemente conexo, acotado y con frontera **suave** (Teo. 1.1, p. 2; Sec. 2, p. 3), mas (A1) curvatura que no se anula en abiertos y (A2) tangencias de orden finito, a lo sumo en dos puntos no inflexion o en un solo punto de inflexion (p. 4). Multiples dominios: solo "can be addressed similarly" (p. 3), sin demostracion en el paper.
- El resultado es una **inclusion** (cota superior) del soporte singular: dice donde PUEDEN estar las rayas, no prueba que cada recta de la familia lleve efectivamente una raya, salvo la generacion de nuevas singularidades en cuspides (Lema 5.2, p. 15). La fuerza se da como orden Sobolev -1/2 con perdida reconocida de 1/2 orden (p. 4) y no se busca el orden preciso (p. 5).
- Modelo de no linealidad: f_E = f_E0 + (E - E0) f con f = alpha chi_D en una ventana de energia [E0 - eps, E0 + eps] y P_MA = -ln(sinh(eps R f)/(eps R f)) (ec. 1.1, p. 1), tomado explicitamente de "the mathematical setup in [13]", donde [13] = Park, Choi, Seo 2017, CPAM 70(11) (refs., p. 22). Es decir, **coincide** con el modelo de Park-Choi-Seo 2017 en el punto de partida; luego el Teo. 2.1 lo generaliza a **cualquier** F suave R -> R (p. 4).
- Sin amplitudes en HU, sin distancias en mm, sin datos clinicos ni material concreto del metal: NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Orden Sobolev -1/2 de los artefactos lejos de la frontera | "away from γ, we have R*I^{-1}F(Rf) ∈ I_k H^{-1/2}(R^2; V(ℒ))" | Teo. 2.1, p. 4 |
| Perdida de 1/2 orden, probablemente mejorable | "the loss of 1/2 order is due to using the C∞-algebra properties" | Sec. 2, p. 4 |
| Experimento numerico: no linealidad cuadratica, constante sin valor | "FBP with the nonlinear function F(u) = au^2 for some constant a" | Fig. 1, p. 2 |
| Experimento numerico: 3 rectas predichas (2 por inflexiones, 1 bitangente) | "There are two lines corresponding to the two inflections points and one line" | Fig. 1, p. 2 |

## Donde entra en mi tesis
Fundamento teorico del canal de condicion T = -FBP[ h(lambda * R(M)) ]: el Teo. 2.1 (p. 4) cubre exactamente la forma R* I^{-1} F(R f) con f proporcional a la indicatriz del metal y F suave arbitraria, de modo que h (si es suave) entra en el teorema y la geometria de las rayas de T queda determinada solo por la frontera de M. Aporta el criterio geometrico para predecir que lineas puede contener T en un corte axial:
- Rectas tangentes a la frontera en dos puntos no inflexion (bitangentes).
- Rectas tangentes en un punto de inflexion (curvatura que cambia de signo), nuevo respecto de Park-Choi-Seo.
- La propia frontera dD.

Entra en el marco/fundamento del renderizador (por que el artefacto excede la mascara y donde), no en el muestreador. No entrega cifras de amplitud ni de extension espacial, por lo que no respalda el ancho de B_delta (~12 mm): NO ENCONTRADO EN EL PDF.

Sobre un unico objeto estrictamente convexo: el paper NO lo dice como enunciado explicito ("un objeto convexo no produce rayas": NO ENCONTRADO EN EL PDF). Lo que si dice: (i) para D estrictamente convexo es imposible una recta tangente en dos puntos distintos (p. 8), (ii) sin inflexiones no hay cuspides (p. 7), y (iii) la familia ℒ solo contiene bitangentes y tangentes en inflexiones (Teo. 1.1, p. 2). La consecuencia logica (inferencia de esta ficha, no frase del paper) es que para un unico D estrictamente convexo ℒ es vacio y el Teo. 1.1 da sing supp(f_MA) ⊂ dD: sin rayas singulares fuera de la frontera bajo este modelo. La frase de p. 2 "for strictly convex objects, the artifacts are straight lines tangent to two boundary curves", atribuida a [13], habla de dos curvas de frontera, es decir, de mas de un objeto o pieza convexa.

## Dudas para el asesor
- **Un unico tornillo (corte axial ~ disco/elipse estrictamente convexo):** por la inferencia anterior, el T analitico no tendria rayas singulares fuera del borde de M; solo la frontera y componentes suaves. Si los artefactos clinicos de un tornillo aislado muestran streaking, este paper no lo explica con su modelo (ruido, scatter o photon starvation no se tratan en el PDF: NO ENCONTRADO EN EL PDF). Conviene aclarar si T se presenta como "prior de beam hardening" sabiendo que para un tornillo aislado ese prior seria casi solo un halo en el borde. Tambien cabria verificar si una elipse muy excentrica o la seccion con rosca cumplen "estrictamente convexo".
- **Dos tornillos en el mismo corte:** el paper solo dice que multiples dominios "can be addressed similarly" (p. 3) y cita a [13] para rayas tangentes a dos curvas de frontera (p. 2). Este es el caso en que T si deberia mostrar rayas rectas (bitangentes comunes). ¿Basta citar [13] y este trabajo, o hace falta leer Park-Choi-Seo 2017 / Palacios-Uhlmann-Wang 2018 ([12], que trata fronteras convexas a trozos, p. 2) para el caso multi-objeto?
- **Tornillo + placa, o cabeza + fuste en un mismo corte:** si la union es conexa y no convexa, aparecen inflexiones (rayas tangentes en la inflexion) y bitangentes (Teo. 1.1). Si son componentes separadas, se aplica el caso multi-dominio (no demostrado aqui). Una placa curvada puede tener tramos concavos. Las esquinas de cabeza o placa violan la frontera suave exigida (p. 3), y el caso de esquinas no esta cubierto: NO ENCONTRADO EN EL PDF.
- **Mascara voxelizada:** M binaria en una grilla tiene frontera en escalera, no suave. El teorema supone frontera suave (p. 3). ¿Se suaviza M antes de R(M), o se acepta la discrepancia y se declara?
- **Alcance del resultado:** el teorema es una inclusion (donde pueden estar las rayas), no una prediccion de intensidad. ¿Se usa solo para justificar la geometria de T y no su amplitud?
- **Snowballing (para la autora, no agregado aqui):** [12] Palacios, Uhlmann, Wang, SIAM J. Math. Anal. 50(5):4914-4936, 2018 y [13] Park, Choi, Seo, CPAM 70(11):2191-2217, 2017 (refs., p. 22) parecen candidatos segun `_candidatos.md`.

## Evidencia textual
| Cifra / umbral / definicion / criterio | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Ventana de energia E en [E0 - eps, E0 + eps], eps > 0 | "We assume that for E ∈ [E0 − ε, E0 + ε], ε > 0," | Sec. 1, p. 1 |
| Modelo lineal en energia, f = alpha chi_D | "f_E(x) = f_E0(x) + (E − E0)f where f = αχ_D" | Sec. 1, p. 1 |
| alpha > 0 aproxima la derivada respecto de la energia | "α > 0 a constant which approximates ∂f_E/∂E over D" | Sec. 1, p. 1 |
| Modelo de sinograma (ec. 1.1) | "P = Rf_E0 + P_MA, P_MA = −ln( sinh(εRf) / εRf )" | Ec. (1.1), p. 1 |
| Origen del modelo: Park-Choi-Seo [13] | "We begin with the mathematical setup in [13] for beam hardening effects." | Sec. 1, p. 1 |
| P_MA viene de Beer-Lambert bajo supuestos | "The term P_MA is derived from the Beer-Lambert law under some assumptions" | Sec. 1, p. 1 |
| Sin dependencia energetica no hay termino no lineal | "If α = 0 so that f = 0, it is clear that P_MA = 0" | Sec. 1, p. 1 |
| F de beam hardening es suave | "F(x) = −ln( sinh(εx) / εx ) is smooth." | Sec. 1, p. 1 |
| f_MA causa las rayas | "The term f_MA often causes streak artifacts in the reconstruction" | Sec. 1, p. 1 |
| Teo. 1.1: contencion del soporte singular | "sing supp(f_MA) ⊂ ( ∪_{L∈ℒ} L ) ∪ ∂D." | Teo. 1.1, p. 2 |
| Teo. 1.1: definicion de la familia ℒ | "either tangent at two non-inflection points, or tangent at only one inflection point" | Teo. 1.1, p. 2 |
| Definicion de punto de inflexion | "if the curvature κ = 0 at p and changes sign across p" | Sec. 1, p. 2 |
| Caso estrictamente convexo (resultado de [13]) | "for strictly convex objects, the artifacts are straight lines tangent to two boundary curves" | Sec. 1, p. 2 |
| Mecanismo: interaccion no lineal ligada a la geometria | "due to nonlinear interactions of the singularities in Rχ_D" | Sec. 1, p. 2 |
| Fronteras convexas a trozos tratadas en [12] | "metal regions with piecewise strictly convex boundaries are addressed" | Sec. 1, p. 2 |
| Inflexiones generan cuspides en el sinograma | "When ∂D contains inflection points, we show that the sinogram contains cusp points" | Sec. 1, pp. 2-3 |
| Cuspides generan nuevas singularidades | "the nonlinear interaction of cusp singularities generates new ones that lead to the artifacts" | Sec. 1, p. 3 |
| Experimento numerico: objeto | "Numerical simulation of steak artifacts for a non-strictly convex metal object." | Fig. 1, p. 2 |
| Experimento numerico: rectas predichas | "There are two lines corresponding to the two inflections points and one line" | Fig. 1, p. 2 |
| Experimento numerico: no linealidad usada | "FBP with the nonlinear function F(u) = au^2 for some constant a" | Fig. 1, p. 2 |
| Experimento numerico: interseccion transversal en sinograma | "We circled the transversal intersection point in the oval" | Fig. 1, p. 2 |
| Experimento numerico: cuspide en sinograma | "We circled the cusp point in the square" | Fig. 1, p. 2 |
| Valor de a, tamano de grilla, numero de angulos, metricas cuantitativas | NO ENCONTRADO EN EL PDF | — |
| Supuesto de dominio | "a simply connected bounded domain D ⊂ R^2 with smooth boundary" | Sec. 2, p. 3 |
| Multiples dominios (sin demostracion) | "The case of multiple domains can be addressed similarly." | Sec. 2, p. 3 |
| Supuesto (A1) | "The curvature κ on γ does not vanish on open sets of γ." | Sec. 2, p. 4 |
| Supuesto (A2), orden finito | "L is tangent to γ at a finite order" | Sec. 2, p. 4 |
| Supuesto (A2), maximo de tangencias | "tangent at at most two non-inflection points, or tangent at only one inflection point" | Sec. 2, p. 4 |
| Generalidad de los supuestos (afirmacion de los autores) | "There is essentially no loss of generality." | Sec. 2, p. 4 |
| Teo. 2.1: vale para toda F suave | "Then for any smooth function F : R → R, we have" | Teo. 2.1, p. 4 |
| Teo. 2.1: orden -1/2 lejos de la frontera | "away from γ, we have R*I^{-1}F(Rf) ∈ I_k H^{-1/2}" | Teo. 2.1, p. 4 |
| Perdida de 1/2 orden | "the loss of 1/2 order is due to using the C∞-algebra properties" | Sec. 2, p. 4 |
| Orden preciso no estudiado | "find the precise order of the artifacts which we do not pursue here" | Sec. 2, p. 5 |
| Radon de haz paralelo en R^2 | "Rf(s,θ) = ∫_{x·θ=s} f(x) dH^1(x)" | Sec. 3, p. 5 |
| Continuidad de Radon con ganancia de 1/2 | "R : H^s(R^2) → H^{s+1/2}(ℒ) is bounded." | Sec. 3.1, p. 7 |
| Criterio de convexidad | "γ is convex if and only if κ(t) ≥ 0 or κ(t) ≤ 0 on [a,b]" | Sec. 3.1, p. 7 |
| Criterio de convexidad estricta | "γ is strictly convex if κ(t) ≠ 0." | Sec. 3.1, p. 7 |
| Sin inflexiones, curva del sinograma suave | "if there are no inflection points, then S is a smoothly embedded curve" | Sec. 3.1, p. 7 |
| Convexo estricto: no hay bitangente | "tangent to γ at two different points, which would be impossible for D strictly convex" | Sec. 3.1, p. 8 |
| Inflexion simple (orden 1) | "The simplest case is when x2(t) = t^3 h(t), h(0) ≠ 0" | Sec. 3.2, p. 8 |
| Lema 3.3: cuspide en el sinograma | "S+ ∪ S− form a cusp at (s, φ) = (0, π/2)" | Lema 3.3, p. 8 |
| Inflexiones de orden superior | "where k ≥ 3 is odd." | Sec. 3.2, p. 9 |
| kappa = 0 sin cambio de signo: no tratado | "the union of the curves forms a curve which is C^1 but not C^2" | Sec. 3.2, p. 10 |
| Ese caso queda fuera | "Although we do not pursue this case here" | Sec. 3.2, p. 10 |
| Corolario 4.6 (caso estrictamente convexo) | "If γ = ∂D is the boundary of a strictly convex domain" | Cor. 4.6, p. 13 |
| Supuesto sobre tangentes multiples | "either tangent to (at most) two strictly convex pieces γi, γj" | Sec. 5, p. 14 |
| Intersecciones transversales en sinograma | "If Si, Sj intersect, they must intersect transversally" | Sec. 5.1, p. 14 |
| Orden Sobolev optimo ignorado | "we will ignore the optimal Sobolev order in this paper." | Obs. 5.1, p. 14 |
| Lema 5.2: k >= 3, nuevas singularidades | "For k ≥ 3, there exist u ... such that u^2 ∉ I_kL^2" | Lema 5.2, p. 15 |
| Cuspides producen nuevas singularidades | "the nonlinear interaction of cusp type singularities could produce new singularities" | Sec. 5.2, p. 15 |
| No hay dos cuspides en un mismo punto | "we cannot have two different cusps sharing a common cusp point" | Sec. 5.2, p. 15 |
| Lema 7.1 (de [17]): umbral rho > 2 | "f ∈ C_c^∞(R), and ρ > 2." | Lema 7.1, p. 18 |
| DOI, revista y paginas de la version publicada | NO ENCONTRADO EN EL PDF | — |
| Geometria fan-beam / cone-beam / 3D | NO ENCONTRADO EN EL PDF | — |
| Amplitud en HU, extension en mm, material del metal | NO ENCONTRADO EN EL PDF | — |
| Enunciado explicito "un objeto estrictamente convexo no produce rayas" | NO ENCONTRADO EN EL PDF | — |
| Tratamiento de fronteras con esquinas (no suaves) | NO ENCONTRADO EN EL PDF | — |
| Ruido, scatter o photon starvation como causa de rayas | NO ENCONTRADO EN EL PDF | — |
