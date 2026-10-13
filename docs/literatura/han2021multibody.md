# han2021multibody — Planificacion de reduccion de fractura pelvica via registro multicuerpo

- **DOI / URL:** 10.1016/j.media.2020.101917 (Med Image Anal. 2021;68:101917; de refs/raw/han2021multibody.nbib y confirmado en p. 1 del PDF)
- **Nivel de lectura:** 3 (contexto). Se pidio nivel 2; se ajusta a 3 porque el paper NO planifica tornillos ni trayectorias, solo reduccion de fragmentos.
- **Leido a fondo por la autora:** no
- **PDF:** papers/han2021multibody.pdf (manuscrito de autor HHS/PMC, 44 paginas; las paginas citadas abajo son la numeracion "Page N" del manuscrito)

## Que hace (3 lineas maximo)
Segmenta fragmentos oseos de pelvis fracturada en CT (continuous max-flow), planifica la reduccion registrando los fragmentos a una "plantilla adaptativa" (SSM de forma + SPM de pose de sacro e innominados) y luego registra 3D-2D los fragmentos a fluoroscopia para guiar la reduccion intraoperatoria. Evaluado en simulacion (40 CT, 120 casos), 1 cadaver y 3 casos clinicos retrospectivos.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Supuestos relevantes para esta tesis:
- Solo trata reduccion de fragmentos, no fijacion: la planificacion de fijacion se delega a trabajo previo, "previously reported methods for automatic pelvic fixation planning (Han et al., 2019)" (p. 26).
- No simula disrupciones del sacro: "Disruptions of the sacrum were not simulated in the current study" (p. 14, Sec. 4.1). Esto excluye justo la region S1 que usa el muestreador.
- Los fragmentos pequenos no reducidos se excluyen del analisis (p. 2-3, Introduccion).
- Implantes/instrumental solo aparecen como contenido extrano en fluoroscopia que la metrica GO intenta ignorar ("extraneous instrumentation", p. 13); no se modelan en CT.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna propuesta para la tesis | No aporta cifras de corredor, margen ni malposicion de tornillos | — |

## Donde entra en mi tesis
- **No compite con el muestreador.** No planifica tornillos iliosacros/transsacros, no define corredores oseos, margenes de seguridad, contencion cortical ni zonas seguras (ver tabla: todas NO ENCONTRADO EN EL PDF). No usa datos de malposicion.
- **Aporta contexto** en dos puntos posibles del Estado del arte / Objetivo 2: (a) ejemplo de modelado estadistico de forma y pose del sistema sacro + innominados (SSM + SPM en grupo de Lie) sobre un atlas pelvico de 40 CT, util si se discute como representar variabilidad anatomica receptora; (b) senala la existencia de planificacion automatica de fijacion pelvica en trabajo previo del mismo grupo (Han et al., 2019), que si podria relacionarse con el muestreador.
- Reduccion de fractura, navegacion 3D-2D y fluoroscopia quedan **fuera de alcance** de la tesis (CT pelvica, sin fractura simulada).

## Dudas para el asesor
- La referencia citada en p. 26 / p. 27 "Han R, Uneri A, De Silva T, ... 2019. Atlas-based automatic planning and 3D-2D fluoroscopic guidance in pelvic trauma surgery. Phys. Med. Biol 64, 95022" es descrita por este PDF como "automatic pelvic fixation planning". Es posiblemente mas pertinente para el Objetivo 2 que este paper (candidata de snowballing; no verificada).
- El atlas de 40 CT con segmentaciones de innominados y sacro ("open-source pelvis atlas (Han et al., 2019)", p. 9) podria ser relevante como insumo anatomico; el PDF no da su URL ni licencia.
- Los umbrales de aceptacion clinica (5 mm anillo pelvico, 2 mm acetabulo) son de reduccion, no de posicion de tornillo; no deben confundirse con margenes de corredor.

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Dataset simulacion: 40 CT | "a simulation study of 40 CT images simulating three fracture categories" | Abstract, p. 1 |
| Atlas: 40 CT con segmentaciones | "An open-source pelvis atlas (Han et al., 2019) comprised of 40 CT images" | 3.2.1, p. 9 |
| Validacion leave-one-out N = 40 | "leave-one-out cross validation of the atlas (N = 40)" | 4.1, p. 14 |
| 120 casos simulados | "In total, 120 cases were simulated (3 fracture categories for each of the 40" | 4.1, p. 14 |
| 3 categorias de fractura | "unilateral two-body, unilateral three-body, and bilateral two-body" | Abstract, p. 1 |
| Dislocaciones simuladas 0-20 mm, 0-15 grados | "magnitude uniformly distributed from 0-20 mm and 0°-15°" | 4.1, p. 14 |
| Sacro no simulado | "Disruptions of the sacrum were not simulated in the current study" | 4.1, p. 14 |
| Fractura simulada por cuboide | "the innominate bone was dissected by a cuboid (B) with an arbitrary size" | 4.1, p. 14 |
| Seed points en simulacion | "one 'seed point' for smaller fragments and up to three 'seed points'" | 4.1, p. 14 |
| Criterio exito segmentacion DC > 0.70 | "success rate defined by the ratio of trials with DC > 0.70" | 4.1, p. 15 |
| Metricas de segmentacion | "quantified in terms of the Dice coefficient (DC) ... as well as Hausdorff distance" | 4.1, p. 15 |
| Metrica de reduccion | "analyzed in terms of constituent translational and rotational magnitudes" | 4.1, p. 15 |
| Baseline "mirror" | "A symmetry plane defined by the sacral midline was determined" | 4.1, p. 15 |
| Geometria C-arm simulado | "source-axis distance=600 mm, source-detector distance=1100 mm" | 4.2, p. 15 |
| 80 registros 3D-2D | "a total of 80 registrations were performed (two fracture categories" | 4.2, p. 15 |
| Errores 3D-2D en/fuera de plano | "decomposed into in-plane (parallel to the detector plane) and out-of-plane" | 4.2, p. 16 |
| Cadaver: 1 especimen, fractura Tile C1 | "to mimic a common Tile C1 fracture, resulting in three bone fragments" | 4.3, p. 16 |
| Voxel CT cadaver | "reconstructed at 0.39x0.39x0.5 mm3 voxel size" | 4.3, p. 16 |
| Cadaver: 3 etapas, 6 vistas | "manipulated to 3 different stages ... and 6 fluoroscopic images" | 4.3, p. 16 |
| Clinico: 3 pacientes retrospectivos | "IRB-approved retrospective study of three patients undergoing pelvic fracture reduction" | 4.4, p. 17 |
| Voxel CT clinico | "reconstructed at 0.74×0.74×3 mm3 voxel size and 512×512×260 voxels" | 4.4, p. 17 |
| Umbral clinico anillo pelvico 5-10 mm | "up to 5-10 mm residual displacement may be acceptable" | 4.4, p. 17 |
| Umbral clinico acetabulo 2 mm | "acetabulum reduction requires residual displacement within 2 mm" | 4.4, p. 17 |
| Umbral mal-reduccion (intro) | ">5 mm residual displacement in pelvic ring fractures and >2 mm in acetabulum" | 1, p. 2 |
| Malalineacion 30% del error | "geometric misalignments comprise 30% of surgical reduction error" | 1, p. 2 |
| Metrica clinica PDE | "accuracy was quantified by 2D projection distance error (PDE)" | 4.4, p. 18 |
| Landmarks PDE | "Eight to thirteen anatomical landmarks were manually annotated" | 4.4, p. 18 |
| Rango aceptacion en figuras | "Clinical acceptance range (5 mm and 5°) are plotted in red dashed lines" | Fig. 5, p. 34 |
| Epidemiologia: 20% trauma contuso | "comprises up to 20% of blunt trauma (and 3% of all bone fractures)" | 1, p. 2 |
| Epidemiologia: 537 pacientes, 74.5%, 18.3% | "unstable fractures requiring surgical intervention consisted of 74.5% of total cases" | 1, p. 2 |
| Conminutas 2% | "consisted of 2% of total cases (Switzer et al., 2000)" | 1, p. 2 |
| Fluoroscopia >2 min | "extended fluoroscopy time (often >2 min)" | 1, p. 3 |
| Planificacion manual 174.8 min | "an average time of 174.8 min was reported for manual planning" | 1, p. 3 |
| Parametros CMF beta, gamma | "β and γ were chosen to be 0.5 and 3.0, respectively" | 3.1, p. 8 |
| GMM dos componentes | "A gaussian mixture model with two components was chosen" | 3.1, p. 8 |
| Variabilidad SSM ~3.3 mm | "quantifying the variability of the SSM, is around 3.3 mm" | 3.2.1, p. 9 |
| Pose similaridad 7 parametros | "can be modeled linearly in the Lie group space ... by seven parameters" | 3.2.1, p. 10 |
| Restriccion SPM 3 desviaciones | "within three standard deviations of the SPM eigenvalue" | 3.2.1, p. 11 |
| SD traslacion innominados 1.5-2.6 mm, sacro 5 mm | "ranges from 1.5 mm to 2.6 mm for the innominate bones and up to 5 mm" | 3.2.1, p. 11 |
| SD rotacion 1-3 grados, sacro 5 grados | "ranges from 1° to 3° for the innominate bones ... up to 5°" | 3.2.1, p. 11 |
| Registro rigido 6 DoF | "solves the 6 degree-of-freedom (DoF) rigid transformations" | 3.2.2, p. 11 |
| Optimizador CMA-ES | "solved simultaneously using the covariance matrix adaption evolution strategy (CMA-ES)" | 3.2.2, p. 12 |
| Proyeccion 9 DoF | "parametrized by a 9 DoF projection matrix H" | 3.3, p. 13 |
| Metrica similaridad GO | "based on pixel-wise correspondence of gradient orientation (GO)" | 3.3, p. 13 |
| Parametros multiresolucion | "downsampling factors of [4x, 2x], CMA-ES population size of [100, 100]" | 3.3, p. 13 |
| SD CMA-ES | "CMA-ES standard deviation of [4, 1] mm and [4, 1]°" | 3.3, p. 13 |
| Exito segmentacion 91% vs 96% | "achieved success rates ... of 91% and 96%, respectively" | 5.1, p. 18 |
| DC simulacion 0.90 vs 0.92 | "DC was comparable between the two methods (0.90 ± 0.07 and 0.92 ± 0.06" | 5.1, p. 18 |
| HD 4.1 vs 2.7 mm | "higher HD (4.1 ± 2.0 mm) compared to the CMF method (2.7 ± 1.7 mm" | 5.1, p. 18 |
| Mirror 2-cuerpos 5.3 mm / 7.4 grados | "mirror method exhibited translational errors of 5.3 ± 3.7 mm and rotational errors of 7.4 ± 4.3°" | 5.1, p. 18 |
| Adaptativo 2-cuerpos 2.2 mm / 2.2 grados | "achieved translational error of 2.2 ± 1.5 mm and rotational error of 2.2 ± 1.5°" | 5.1, p. 18 (Tabla 2, p. 43, reporta 2.2 ± 1.6 mm) |
| Error por direccion | "3 translational directions (1.3 ± 1.2 mm, 1.4 ± 1.2 mm, 1.3 ± 1.2mm" | 5.1, p. 18 |
| Mirror 3-cuerpos 6.2 mm / 9.5 grados | "the mirror method yielded 6.2 ± 4.4 mm and 9.5 ± 5.7°" | 5.1, p. 19 |
| Adaptativo 3-cuerpos 2.6 mm / 3.7 grados | "achieving 2.6 ± 1.6 mm and 3.7 ± 1.8°, respectively" | 5.1, p. 19 |
| Diferencia 2 vs 3 cuerpos | "average difference 0.4 mm (not statistically significant) and 1.5°" | 5.1, p. 19 |
| Fraccion dentro de 5 mm / 5 grados | "majority of both two-body (88%) and three-body (77.5%) fracture simulations" | 5.1, p. 19 |
| Bilateral 2.8 mm / 3.3 grados | "translational error of 2.8 ± 1.5 mm and rotational error of 3.3 ± 2.1°" | 5.1, p. 19 |
| Bilateral vs unilateral p = 0.05 | "rotation (p = 0.05, computed via unpaired t-test)" | 5.1, p. 19 |
| 3D-2D en plano 1.4 mm | "1.4 ± 0.8 mm and 1.4 ± 0.8 mm in-plane translational error" | 5.2, p. 20 |
| 3D-2D fuera de plano | "achieving 1.3 ± 0.8 mm and 1.6 ± 1.1 mm out-of-plane error" | 5.2, p. 20 |
| 3D-2D total traslacion | "2.1 ± 0.9 mm and 2.4 ± 1.0 mm for two-body and three-body" | 5.2, p. 20 |
| Exito 2 mm acetabulo | "the proposed method succeeded in 80% of cases" | 5.2, p. 20 |
| 3D-2D rotacion en plano | "0.1 ± 0.1° in-plane rotational error for the two-body fractures" | 5.2, p. 20 |
| 3D-2D rotacion total | "overall rotational error ... was 0.3 ± 0.1° and 0.4 ± 0.2°" | 5.2, p. 20 |
| Error combinado 0.5-4.7 mm | "would range between ... 0.5 mm~4.7 mm" | 5.2, p. 20 |
| Cadaver segmentacion | "overall Dice Coefficient of 0.92 ± 0.04 and HD of 5.2 ± 2.0 mm" | 5.3, p. 20 |
| Cadaver planificacion | "difference between the automatic plan and ground truth was 2.68 mm and 4.10°" | 5.3, p. 21 |
| Cadaver 3D-2D | "1.5 ± 0.6 mm in-plane, 1.8 ± 0.5 mm out-of-plane translational error" | 5.3, p. 21 |
| Cadaver 3D-2D rotacion, 16 ensayos | "0.6 ± 0.2° in-plane, 0.7 ± 0.4° out-of-plane ... 16 registration trials" | 5.3, p. 21 |
| Runtime segmentacion ~4.5 min | "seed points input and continuous max-flow was ~4.5 min" | 5.3, p. 22 |
| Runtime planificacion ~42 min | "runtime for fracture reduction planning was ~42 min" | 5.3, p. 22 |
| Runtime intraoperatorio ~2 min | "overall runtime ~2 min for the first fluoroscopic image" | 5.3, p. 22 |
| Tabla 3 tiempos | "3.3 ± 0.7 ... 1.4 ± 0.2 ... 42.3 ± 10.9" (min) | Tabla 3, p. 44 |
| Caso 1 segmentacion | "DC of 0.87 ± 0.05 and HD of 2.8±0.9" | 5.4.1, p. 22 |
| Caso 1 auto vs manual | "difference between the automatic and manual planning was 3.3 ± 0.3 mm and 2.5 ± 2.1°" | 5.4.1, p. 22 |
| Caso 1 PDE | "The registration achieved PDE of 3.0 ± 1.4 mm" | 5.4.1, p. 23 |
| Caso 2 segmentacion | "DC of 0.89 ± 0.04 and HD of 3.8 ± 1.2 mm" | 5.4.2, p. 23 |
| Caso 2 auto vs manual | "difference between the two plans was 2.6 ± 0.3 mm, 3.4 ± 1.8°" | 5.4.2, p. 23 |
| Caso 2 PDE | "The registration achieved 2.5 ± 1.2 mm PDE" | 5.4.2, p. 23 |
| Caso 3 dislocacion >90 grados | "fractured and severely dislocated (over 90°)" | 5.4.3, p. 23 |
| Caso 3 segmentacion | "DC of 0.95 ± 0.02 and HD of 1.6 ± 0.5 mm" | 5.4.3, p. 23 |
| Caso 3 auto vs manual | "quantified to be 1.0 mm and 5.8°" | 5.4.3, p. 23 |
| Caso 3 PDE | "with PDE 2.2 ± 1.1 mm" | 5.4.3, p. 24 |
| Comparacion literatura (Borg) | "exceeding 5 mm in 17% ... 29% ... and 52%" | 6, p. 24 |
| Propuesto >5 mm | "only 12% - 25% of cases presenting greater than 5 mm error" | 6, p. 24 |
| Runtime preoperatorio ~45 min | "exhibited a runtime of ~45 min" | 6, p. 25 |
| Planificacion de tornillos / trayectorias | NO ENCONTRADO EN EL PDF | — |
| Corredores oseos (iliosacro / transsacro) | NO ENCONTRADO EN EL PDF | — |
| Margenes de seguridad / contencion cortical | NO ENCONTRADO EN EL PDF | — |
| Zonas seguras / estructuras neurovasculares | NO ENCONTRADO EN EL PDF | — |
| Datos de malposicion de implantes | NO ENCONTRADO EN EL PDF | — |
| Modelado de implantes o artefacto metalico en CT | NO ENCONTRADO EN EL PDF | — |
| URL / licencia del atlas de 40 CT | NO ENCONTRADO EN EL PDF | — |
