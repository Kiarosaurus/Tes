# goerres2017planning — Planificacion, guiado y QA de tornillos pelvicos con registro deformable

- **DOI / URL:** 10.1088/1361-6560/aa954f (Phys Med Biol 62(23): 9018-9038; segun portada del author manuscript PMC)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/goerres2017planning.pdf

> Nota de paginacion: el PDF es el author manuscript de HHS/PMC (31 paginas). Todas las
> paginas citadas abajo son las del manuscrito ("Page N" en el encabezado), NO las de la
> revista (9018-9038). La correspondencia entre ambas: NO ENCONTRADO EN EL PDF.

## Que hace (3 lineas maximo)
Planifica automaticamente trayectorias de K-wire/tornillo percutaneo en CT pelvica registrando un atlas (ASM, n=12 hemipelvis femeninas con trayectorias anotadas por experto) al CT del paciente, deformando las trayectorias con Mean Value Coordinates y optimizando un cilindro recto (6 DoF) sobre un mapa de acumulacion. Intraoperatoriamente localiza el K-wire deformado por registro 3D-2D deformable (dKC-Reg) desde 3 fluoroscopias, y compara plan vs. entregado para QA (brecha cortical, desviacion).

## Restriccion o supuesto clave
No es un paper de sintesis generativa; los supuestos que limitan su uso como muestreador son:
- **Determinista, un solo plan "ideal" por corredor**: optimiza la trayectoria que maximiza el solapamiento con el mapa de acumulacion ("The pose of a new trajectory ('plan') is optimized by maximizing the overlap volume", p. 5). No modela malposicion ni distribuciones.
- **Corredores no coinciden con los de la tesis**: solo rama pubica superior, AIIS a PSIS y cresta iliaca a columna posterior (p. 8). Los tornillos sacroiliacos quedan como trabajo futuro ("investigation of additional trajectories, such as sacroiliac screws", p. 15-16). No hay IS/TS ni S1.
- **Atlas sin sacro y unilateral**: "extension of the atlas to the whole pelvis and sacrum (c.f., left-side pelvis in the current work)" (p. 15).
- **Atlas pequeno y solo femenino**: "(n = 12) female pelves was manually segmented" (p. 7).
- **Solo fracturas no desplazadas**: "applicable to undisplaced fractures ... does not directly account for displaced fragments" (p. 14).
- **No define margen de seguridad numerico ni diametro de tornillo planificado**: la trayectoria es un cilindro; la suficiencia para "common screw sizes" se remite a Attias et al. 2005 sin cifra (p. 14).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| n = 12 hemipelvis en atlas | "A relatively small ensemble of (n = 12) female pelves" | 3.1.1, p. 7 |
| 3 trayectorias por forma | "three screw trajectories (Superior pubic ramus, AIIS to PSIS, and Iliac crest to posterior column)" | 3.1.1, p. 8 |
| Error RMS superficie 2.3 +/- 0.6 mm | "showed RMS surface error of 2.3 ± 0.6 mm" | 4.1, p. 12 |
| Conformancia +3-4 mm (rama superior) | "(i) +3–4 mm for the superior ramus" | 4.2, p. 12 |
| Conformancia +5 mm (AIIS-PSIS) | "(ii) +5 mm for AIIS to PSIS" | 4.2, p. 12 |
| Conformancia +4-5 mm (cresta-col. post.) | "(iii) +4–5 mm for the iliac crest to posterior column" | 4.2, p. 12 |
| Diferencia calc. vs experto ~2-3 mm | "mean difference ~2–3 mm in narrow bone corridors" | 4.2, p. 12 |
| dKC-Reg punta 1.1 mm y 1.4 grados | "localized the K-wire tip within 1.1 mm and 1.4°" | Abstract, p. 1 |
| Error rigido hasta 9.1 mm | "errors up to 9.1 mm at the tip" | 4.3, p. 13 |

## Donde entra en mi tesis
Objetivo 2 (muestreador), seccion de trabajo relacionado y de criterios de evaluacion.

- **Compite con el muestreador?** Parcialmente, y solo en el concepto: es un planificador
  automatico de trayectorias pelvicas atlas-based que garantiza conformancia dentro del
  corredor oseo, que es la restriccion de contencion cortical del muestreador. Pero no
  compite como alternativa directa: (a) produce una trayectoria optima determinista, no
  muestrea poses ni malposicion; (b) no cubre IS/TS ni S1 (los sacroiliacos son trabajo
  futuro, p. 15-16); (c) su atlas no incluye sacro (p. 15). Por tanto NO reduce el gap
  declarado de muestrear malposicion condicionada por tecnica en S1.
- **Lo reutilizable**: (1) la metrica de "distancia trayectoria-cortex interna" muestreada
  a lo largo del eje, con signo positivo = dentro del hueso y negativo = brecha (Fig. 7,
  p. 26; definicion via d_min, Eq. 8, p. 9) es un candidato directo para la metrica de
  contencion cortical del muestreador; (2) el uso de un atlas con trayectorias de experto
  + mapa de acumulacion es una forma de definir el "corredor" o la trayectoria nominal
  sobre la cual luego se aplicaria la perturbacion de malposicion; (3) la variabilidad
  intra-observador del experto (~2-3 mm, p. 12) ofrece un orden de magnitud de la
  dispersion "aceptable" alrededor de la trayectoria nominal, aunque en corredores
  distintos de S1.
- **Advertencia**: las cifras de conformancia (+3 a +5 mm) son para corredores del
  ilion/rama pubica en un atlas femenino de 12 casos; no son transferibles a S1 sin
  otra fuente.

## Dudas para el asesor
1. El abstract dice ">5 mm for the widest corridor (tear drop)" pero los resultados
   (p. 12) reportan "+5 mm for AIIS to PSIS"; el termino "tear drop" no vuelve a aparecer
   en el cuerpo. Se cita la cifra del cuerpo; confirmar si conviene mencionar la
   discrepancia.
2. El abstract dice "1.1 mm and 1.4°" y el cuerpo "~1 mm and ~1°" (p. 13) para dKC-Reg.
   Cual usar si se cita? (la tesis probablemente no necesita esta cifra: es guiado
   intraoperatorio, no muestreo).
3. Sirve la metrica de distancia firmada al cortex a lo largo del eje (Fig. 7) como
   definicion operacional de "contencion cortical" del muestreador, o se prefiere la
   clasificacion ordinal de zwingmann2009navigated como unica metrica?
4. Vale la pena considerar un atlas de trayectorias de experto (estilo Goerres) para
   definir la trayectoria nominal IS/TS en S1, o eso ya esta resuelto por otra via?

## Evidencia textual
| Dato | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Referencia de publicacion | "Phys Med Biol. ; 62(23): 9018–9038. doi:10.1088/1361-6560/aa954f." | Portada, p. 1 |
| Corredor mas estrecho 3-4 mm | "conformed within the bone cortex by 3–4 mm for the narrowest corridor" | Abstract, p. 1 |
| Corredor mas ancho >5 mm | ">5 mm for the widest corridor (tear drop)" | Abstract, p. 1 |
| dKC-Reg 1.1 mm / 1.4 grados | "localized the K-wire tip within 1.1 mm and 1.4°" | Abstract, p. 1 |
| Error rigido hasta 9 mm (abstract) | "more accurate than rigid-body tracking (errors up to 9 mm)" | Abstract, p. 1 |
| Longitud K-wire 20-30 cm | "Such K-wires are commonly ~20–30 cm in length" | 1, p. 2 |
| Trayectorias estandar (anterior column) | "anterior column through the superior pubic ramus (Routt et al., 1995)" | 1, p. 2 |
| Trayectoria AIIS-PSIS | "the anterior inferior iliac spine (AIIS) to posterior superior iliac spine (PSIS)" | 1, p. 2 |
| Iliosacros mencionados como comunes | "Other common trajectories include iliosacral fusion at S1 or S2" | 1, p. 2 |
| Longitud de trayectorias hasta 15 cm | "the trajectories are up to 15 cm long (Puchwein et al., 2012)" | 1, p. 2 |
| Fluoroscopia hasta 123 s por tornillo | "upwards of 123 sec per screw (Gras et al., 2010)" | 1, p. 2 |
| Supuesto de rigidez / fracturas no desplazadas | "reasonable assumption for simple undisplaced fractures" | 1, p. 3 |
| SSM: jerarquia de modos d | "following a coarse-to-fine hierarchy of d = 1 to 2 to 4 to 8" | 2.1, p. 4 |
| Trayectorias modeladas como cilindros | "Trajectory annotations are modeled as cylinder surfaces C_i" | 2.3, p. 5 |
| Voxel del mapa de acumulacion 0.5 mm | "Binary images of the surfaces (0.5 mm voxels) are then aggregated" | 2.3, p. 5 |
| Optimizacion del plan, 6 DoF | "Transformation parameters z with 6 degrees of freedom (DoF) are optimized" | 2.3, p. 5 |
| Criterio de plan: max. solapamiento | "optimized by maximizing the overlap volume of the deformed cylinders" | 2.3, p. 5 |
| CMA-ES poblacion 400, sigma 10 | "with a population size of 400 and an initial standard deviation of σ = 10" | 2.4, p. 6 |
| Vistas separadas al menos 20 grados | "three views with separating angles of at least 20° were used" | 2.4, p. 6 |
| Atlas desde TCIA (CT de ganglios) | "atlas was created from data in The Cancer Imaging Archive" | 3.1.1, p. 7 |
| n = 12 pelvis femeninas | "A relatively small ensemble of (n = 12) female pelves was manually segmented" | 3.1.1, p. 7 |
| k ~ 5000 vertices | "to obtain approximately k ≈ 5000 equidistant vertices on each" | 3.1.1, p. 7 |
| Tres trayectorias anotadas | "three screw trajectories (Superior pubic ramus, AIIS to PSIS, and Iliac crest...)" | 3.1.1, p. 8 |
| Anotacion doble + cirujano | "annotations were performed twice for each case" | 3.1.1, p. 8 |
| Criterio del experto | "compromise between maximum trajectory length and maximum distance to cortical boundaries" | 3.1.1, p. 8 |
| Punta distal en el cortex | "The distal tip was also positioned at the cortex" | 3.1.1, p. 8 |
| RANSAC n_pts = 20 | "a fixed number of points n_pts = 20 was randomly selected" | 3.1.2, p. 8 |
| RANSAC n_it = 50 | "After a fixed number of iterations n_it = 50" | 3.1.2, p. 8 |
| Evaluacion leave-one-out | "A leave-one-out cross-validation of the atlas members was performed." | 3.1.4, p. 9 |
| Metrica d_min (Eq. 8) | "computed the minimum distance between a vertex q on Q to the closest vertex" | 3.1.4, p. 9 |
| Metrica RMS de superficie (Eq. 9) | "summarized in the root mean square (RMS) surface error" | 3.1.4, p. 9 |
| Subconjuntos de atlas n_min > 3 | "For each atlas size n_min > 3, the subsets" | 3.1.4, p. 9 |
| Muestreo a lo largo de trayectoria -7.5 a 7.5 cm | "ranging from −7.5 to 7.5 cm with respect to the center" | 3.1.4, p. 9 |
| Criterio proximidad al cortex | "d_min ... was evaluated at each sample point ... to analyze proximity to bone cortex" | 3.1.4, p. 9 |
| K-wire modelo: knots h=3,4,5, orden 3 | "cubic spline with h = 3,4,5 knots of order n = 3" | 3.2.1, p. 10 |
| Radio inicial 1.6 mm | "initialized with 1.6 mm radius" | 3.2.1, p. 10 |
| Multi-start 10 reinicios | "the KC is reinitialized 10 times" | 3.2.1, p. 10 |
| Binning 2x2 a 1x1 mm2 | "reduced in three steps from 2×2 mm2 to 1.5×1.5 mm2 and then to 1×1 mm2" | 3.2.1, p. 10 |
| 1 cadaver | "a study involving a human cadaver" | 3.2.2, p. 10 |
| Cadaver: mujer anciana | "an elderly female, moderately obese, dissected at the upper humerus and mid-femur" | 3.2.2, p. 10 |
| Lado: cadera izquierda | "K-wires were inserted into the left hip through the superior pubic ramus" | 3.2.2, p. 10 |
| 3-4 posiciones por trayectoria | "At three or four positions along each trajectory, images were acquired" | 3.2.2, p. 10 |
| K-wire 3.2 mm de diametro | "Stryker K-wires of 3.2 mm diameter with threaded tip" | 3.2.2, p. 10 |
| MDCT 120 kVp, 500 mAs | "(120 kVp, 500 mAs, 0.35×0.35×0.80 mm3 voxels; Philips Brilliance 64-slice MDCT)" | 3.2.2, p. 10 |
| Angulos de vistas | "θ = {−37.6°, −10.2°, 15.9°}" | 3.2.2, p. 10 |
| Fluoroscopia 125 kVp, ~0.9 mAs | "(125 kVp, ~0.9 mAs at 15 fps)" | 3.2.2, p. 10 |
| Orbita CBCT 300 grados | "A complete orbit of the C-arm covering 300° was acquired for CBCT" | 3.2.2, p. 10 |
| 75 proyecciones orbitales | "3D-2D registration of the CBCT volume to 75 orbital projections" | 3.2.2, p. 10 |
| Rango -37.6 a 15.9 grados | "ranging from –37.6° to 15.9° about the LR axis" | 3.2.2, p. 10 |
| Init. paciente 40.5 +/- 31.8 mm / 25.3 +/- 22.6 grados | "dislocated from the solution by 40.5 ± 31.8 mm/25.3 ± 22.6°" | 3.2.2, p. 10 |
| Init. componente 78.1 +/- 44.3 mm / 6.4 +/- 3.3 grados | "differing from CBCT tip annotation by 78.1 ± 44.3 mm/6.4 ± 3.3°" | 3.2.2, p. 10-11 |
| Verdad: 2 puntos a 1.5 cm | "c_l^(e) (1.5 cm away from the tip)" | 3.2.3, p. 11 |
| Metricas TRE_x (mm) y TRE_phi (grados) | "The deviation in positional (mm) and angular (°) measurements was computed" | 3.2.3, p. 11 |
| RMS superficie 2.3 +/- 0.6 mm | "showed RMS surface error of 2.3 ± 0.6 mm" | 4.1, p. 12 |
| <4 mm tras 40 iteraciones; ~2 mm tras 130 | "reduced to less than 4 mm after 40 iterations and to ~2 mm" | 4.1, p. 12 |
| -0.03 mm por miembro del atlas | "slow improvement in accuracy with additional members (−0.03 mm/atlas member)" | 4.1, p. 12 |
| Error en cadaver 1.8 mm | "The error in atlas registration for the cadaver image was 1.8 mm" | 4.1, p. 12 |
| Zonas suaves dentro de 1 mm | "the registration is typically within 1 mm" | 4.1, p. 12 |
| Definicion conformancia (seguridad) | "distance between the planned trajectory and the bone cortex characterizes the suitability" | 4.2, p. 12 |
| Calculado vs referencia difiere ~1-2 mm | "with mean distance deviating by ~1–2 mm" | 4.2, p. 12 |
| Convencion de signo | "A positive distance indicates conformance within the bone" | 4.2, p. 12 |
| Conformancia rama superior +3-4 mm | "(i) +3–4 mm for the superior ramus" | 4.2, p. 12 |
| Conformancia AIIS-PSIS +5 mm | "(ii) +5 mm for AIIS to PSIS" | 4.2, p. 12 |
| Conformancia cresta-col. post. +4-5 mm | "(iii) +4–5 mm for the iliac crest to posterior column" | 4.2, p. 12 |
| Outliers 1-2 | "A small number (1–2) of outliers was observed" | 4.2, p. 12 |
| Calculado vs experto ~2-3 mm | "mean difference ~2–3 mm in narrow bone corridors" | 4.2, p. 12 |
| Rama superior estrechez ~1-2 mm | "at the narrowest section of the superior ramus (~1–2 mm)" | 4.2, p. 12 |
| Criterio estadistico: t-test pareado, p 0.05 | "P-values (paired t-test) along the trajectory" | Fig. 8, p. 27 |
| Signo negativo = brecha | "negative values indicate a breach of the bone cortex" | Fig. 7, p. 26 |
| Rigido: error hasta 9.1 mm | "errors up to 9.1 mm at the tip" | 4.3, p. 13 |
| Rigido: 28.9% outliers | "a rigid model showing up to 28.9% rate of outliers in TRE_x" | 4.3, p. 13 |
| dKC-Reg ~1 mm y ~1 grado | "yielding TRE_x and TRE_phi ~1 mm and ~1°, respectively" | 4.3, p. 13 |
| Errores rigidos ilustrados 1.4/8.2/9.1 mm | Etiquetas de figura "1.4 mm", "8.2 mm", "9.1 mm" | Fig. 10(a), p. 29 |
| KC rigido ejemplo 1.8 +/- 32.7 mm | Etiqueta de figura "1.8 ± 32.7 mm" | Fig. 10(b), p. 29 |
| Outliers dKC por etapa 10/8/7/5% | Etiquetas de figura "10%", "8%", "7%", "5%" | Fig. 10(c), p. 29 |
| Escala QA desviacion 0-3 mm | Leyenda "Deviation from plan (mm)" con marcas 0, 1, 2, 3 | Fig. 12(d), p. 31 |
| Fluctuacion RANSAC <0.3 mm | "minor fluctuations (smaller than 0.3 mm)" | 5, p. 14 |
| Atlas N = 12 | "relatively small number of atlas members (N = 12)" | 5, p. 14 |
| Margen suficiente (sin cifra) | "safely traverse bone corridors with margin sufficient for common screw sizes" | 5, p. 14 |
| Acuerdo ~1-2 mm en corredores estrechos | "close agreement (mean ~ 1–2 mm) with expert reference trajectories" | 5, p. 14 |
| Discrepancia extremos ~3-6 mm | "Larger discrepancy (mean ~ 3–6 mm) was observed at trajectory endpoints" | 5, p. 14 |
| Outliers sin espacio para tornillo | "1–2 outliers ... did not provide sufficient space for common screw sizes" | 5, p. 15 |
| dKC-Reg 1-2 mm | "accurate (1–2 mm) localization of the deformed K-wire tip" | 5, p. 15 |
| Trayectoria larga >10 cm | "a long (>10 cm) wire trajectory" | 5, p. 15 |
| Tiempo registro paciente 30 s | "requiring 30 s for patient registration" | 5, p. 15 |
| Tiempo dKC-Reg ~1-3 min | "~1–3 min for dKC-Reg in its current, rudimentary implementation" | 5, p. 15 |
| ASM ~3 min; trayectoria ~30 s | "The ASM registration was computed in ~3 min, and each trajectory required ~30 s" | 5, p. 15 |
| Atlas solo lado izquierdo, sin sacro | "extension of the atlas to the whole pelvis and sacrum (c.f., left-side pelvis" | 5, p. 15 |
| Sacroiliacos = trabajo futuro | "investigation of additional trajectories, such as sacroiliac screws" | 5, p. 15-16 |
| Diametro de tornillo planificado | NO ENCONTRADO EN EL PDF | — |
| Longitud de tornillo planificado | NO ENCONTRADO EN EL PDF | — |
| Margen de seguridad numerico (umbral mm) | NO ENCONTRADO EN EL PDF | — |
| Escala/graduacion de brecha cortical (grados tipo Gertzbein o similar) | NO ENCONTRADO EN EL PDF | — |
| Trayectorias IS/TS en S1 evaluadas | NO ENCONTRADO EN EL PDF | — |
| Correspondencia paginas manuscrito vs revista | NO ENCONTRADO EN EL PDF | — |
