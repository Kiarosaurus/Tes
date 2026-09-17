# selles2024marreview — Revision de tecnicas MAR tradicionales y novedosas en CT

- **DOI / URL:** https://doi.org/10.1016/j.ejrad.2023.111276 (European Journal of Radiology 170 (2024) 111276)
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/selles2024marreview.pdf

## Que hace (3 lineas maximo)
Revision narrativa (163 estudios de PubMed, 1981-2023) de reduccion de artefactos metalicos en CT: ajuste de adquisicion/reconstruccion, MAR en proyeccion (interpolacion, NMAR, FSMAR, algoritmos comerciales), monoE de DECT, DECT+MAR, CT de conteo de fotones y MAR con deep learning.
Clasifica tipos de implante por severidad de artefacto (Tabla 1) y da una recomendacion de tecnica por categoria.
Enfoque clinico-radiologico; no reporta medidas espaciales del artefacto ni umbrales de HU.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Supuestos relevantes para esta tesis:
- La falta de referencia limpia obliga a simular artefactos para entrenar MAR supervisado: "The ground truth image, with metal but without metal artifacts, is generally not available." (Sec. 4.2, p. 8). La simulacion se usa para **remover**, no para aumentar datos de segmentacion.
- La severidad se describe solo en forma cualitativa y dependiente del implante: "highly dependent on the size, shape and alloy of the metal implant" (Sec. 1, p. 1). No hay cuantificacion de extension espacial (mm, distancia al metal): NO ENCONTRADO EN EL PDF.
- Mecanismo de volumen parcial: NO ENCONTRADO EN EL PDF (el paper nombra beam hardening, photon starvation, scattering y edge effects).
- Umbral de HU para segmentar metal: NO ENCONTRADO EN EL PDF. Solo menciona que la imagen prior de FSNMAR depende de segmentar hueso y tejido blando, "which commonly results in segmentation errors" (Sec. 4.1, p. 8).
- Codificacion multi-ventana en HU (como entrada de red): NO ENCONTRADO EN EL PDF. Las ventanas que aparecen son solo de visualizacion de figuras.
- Dependencia de la extension del artefacto con kVp: NO ENCONTRADO EN EL PDF (el kVp se discute solo como estrategia de reduccion).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
Candidatos (ninguno citado aun; decision de la autora):

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Osteosintesis = artefactos "Medium" (categoria cualitativa) | "Osteosynthesis materials Medium artifacts" | Tabla 1, p. 6 |
| Artroplastia de cadera = implante grande/alta densidad, artefactos "Severe" | "Large and high-density implants Severe artifacts" | Tabla 1, p. 6 |
| 82 % de imagenes con artefactos secundarios (O-MAR, tornillos espinales) | "found secondary artifacts in 82 % of the images with O-MAR" | Sec. 3.2.2, p. 3 |
| Severidad depende de tamano, forma y aleacion | "highly dependent on the size, shape and alloy of the metal implant" | Sec. 1, p. 1 |
| Cuatro mecanismos principales | "Beam hardening, photon starvation, scattering and edge effects are the main contributors" | Sec. 1, p. 1 |

## Donde entra en mi tesis
- Related Work / Introduccion: mecanismos fisicos del artefacto y su manifestacion (streaks claros/oscuros alineados con bordes del metal, ruido aumentado) como justificacion cualitativa de la banda B_delta del Renderizador.
- Alcance: la Tabla 1 situa placas y tornillos ortopedicos en la categoria de artefactos "Medium", distinta de la artroplastia de cadera ("Severe"); util para delimitar que tipo de artefacto se sintetiza en pelvis.
- Datos (anatomia receptora): recuerda que la apariencia del artefacto en CT clinico depende de la reconstruccion (MAR del fabricante, monoE, kernel, grosor de corte, filtro de estano, kVp), y que MAR puede introducir artefactos secundarios.
- Implicancia #57: el survey no aporta ninguna medida de extension espacial; no la resuelve.
- Implicancia #22: no aporta umbral de HU para metal.
- Implicancia #61: describe dominios de MAR (proyeccion/sinograma, imagen, dual-domain) solo para remocion; no para sintesis.
- Implicancia #2 (opcion 3): el survey no menciona codificacion multi-ventana ni sintesis generativa de artefactos; menciona simulacion de artefactos solo para crear pares de entrenamiento de MAR supervisado (Sec. 4.2, p. 8).

## Dudas para el asesor
- Un survey clinico de 163 estudios no reporta extension espacial del artefacto: basta como apoyo (no prueba) a "remains unmeasured in the literature", o hace falta una busqueda en literatura de fisica medica?
- La Tabla 1 es una categorizacion cualitativa de los autores (severe/medium/small) sin criterio numerico explicito en el PDF: es citable como respaldo de que la osteosintesis produce artefactos de severidad intermedia?
- Se debe registrar en la data card si los CT de CLINIC-metal fueron reconstruidos con MAR del fabricante o monoE, dado que el survey reporta artefactos secundarios por MAR?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Bibliografico | Revista, volumen, articulo | "European Journal of Radiology 170 (2024) 111276" | Encabezado, p. 1 |
| Bibliografico | Fechas | "Received 2 November 2023; Received in revised form 14 December 2023" | p. 1 |
| Bibliografico | Aceptacion | "Accepted 18 December 2023" | p. 1 |
| Metodo del survey | Busqueda PubMed, 899 estudios | "yielded 899 studies between November 1981 and August 2023" | Sec. 2, p. 2 |
| Metodo del survey | Herramienta de cribado | "loaded into ASReview (v1.3) [12] for initial screening" | Sec. 2, p. 2 |
| Metodo del survey | 163 estudios incluidos | "163 studies were included and categorized on metal artifact reduction techniques" | Sec. 2, p. 2 |
| Metodo del survey | Criterio de exclusion | "cone beam CT, megavoltage CT and micro CT were excluded" | Sec. 2, p. 2 |
| Mecanismo | Dependencia de severidad | "highly dependent on the size, shape and alloy of the metal implant" | Sec. 1, p. 1 |
| Mecanismo | Contribuyentes principales | "Beam hardening, photon starvation, scattering and edge effects are the main contributors" | Sec. 1, p. 1 |
| Mecanismo | Beam hardening | "low energy photons are predominantly absorbed while higher energy photons penetrate" | Sec. 1, p. 1 |
| Mecanismo | Beam hardening, efecto espectral | "shift in the polychromatic X-ray spectrum towards a higher energy level" | Sec. 1, p. 1 |
| Mecanismo | Photon starvation | "This leads to a very low photon count on the detector" | Sec. 1, p. 1 |
| Mecanismo | Photon starvation, datos | "therefore missing essential projection data" | Sec. 1, p. 1 |
| Mecanismo | Scatter | "the high electron density of the metals also causes more scattering" | Sec. 1, p. 1 |
| Mecanismo | Edge effects, manifestacion | "observed as dark or bright streaks in line with the edge of the metal" | Sec. 1, p. 1 |
| Mecanismo | Ruido | "Noise is typically not considered as metal artifact" | Sec. 1, p. 1 |
| Mecanismo | Manifestacion general | "often visible as bright and dark streaking artifacts that disguise anatomical structures" | Sec. 1, p. 1 |
| Mecanismo | Volumen parcial | NO ENCONTRADO EN EL PDF | — |
| Extension espacial | Distancia/mm/region afectada del artefacto | NO ENCONTRADO EN EL PDF | — |
| Extension espacial | Dependencia de extension con kVp | NO ENCONTRADO EN EL PDF | — |
| Extension espacial | Mencion cualitativa de vecindad | "small anatomical structures such as vessels in the vicinity of the implant" | Sec. 3.2.1, p. 2 |
| Umbral HU | Umbral de segmentacion de metal | NO ENCONTRADO EN EL PDF | — |
| Multi-ventana | Codificacion multi-ventana en HU | NO ENCONTRADO EN EL PDF | — |
| Visualizacion | Ventana Fig. 1 (cadera bilateral) | "Window: L:40 W:400." | Fig. 1, p. 3 |
| Visualizacion | Ventana Fig. 2 (tornillos espinales) | "Window: L:400 W:1600." | Fig. 2, p. 3 |
| Visualizacion | Ventana Fig. 3 (clavo intramedular) | "Window: L:400 W:1600." | Fig. 3, p. 4 |
| Visualizacion | Ventana Fig. 4 (THA unilateral) | "Window: L: 40, W: 400." | Fig. 4, p. 5 |
| Visualizacion | Ventana Fig. 6 (PCCT, THA) | "Window: L: 650, W:2000." | Fig. 6, p. 7 |
| Visualizacion | Ventana Fig. 7 (THA, DL MAR) | "Window: L: 400, W: 1600." | Fig. 7, p. 8 |
| Adquisicion | Corriente del tubo | "increasing tube current results in more photons that reach the detector" | Sec. 3.1, p. 2 |
| Adquisicion | Costo de subir kV | "increased tube voltage results in a decrease in overall image contrast" | Sec. 3.1, p. 2 |
| Adquisicion | Filtro de estano + 150 kVp | "often combined using a higher tube voltage of 150 kilovoltage peak (kVp)" | Sec. 3.1, p. 2 |
| Reconstruccion | Kernel suave | "soft reconstruction kernel may be helpful ... but this reduces spatial resolution" | Sec. 3.1, p. 2 |
| Reconstruccion | Grosor de corte | "increasing the slice thickness is another method to reduce metal artifact" | Sec. 3.1, p. 2 |
| MAR proyeccion | Kalender, interpolacion lineal | "subsequent linear interpolation to replace missing data" | Sec. 3.2, p. 2 |
| MAR proyeccion | Limitacion interpolacion | "blurring of anatomical structures and introduction of new streaking artifacts" | Sec. 3.2, p. 2 |
| MAR proyeccion | NMAR | "decreased blurring of anatomical structures, particularly in the vicinity of metal implants" | Sec. 3.2, p. 2 |
| MAR, THA/TKA | Beneficio en pelvis | "assessment of pelvic organs when compared to polychromatic images without MAR" | Sec. 3.2.1, p. 2 |
| MAR, THA/TKA | Artefacto residual | "some artifacts may still remain in the corrected image" | Sec. 3.2.1, p. 2 |
| MAR, THA/TKA | Artefactos secundarios | "degradation of bone cortex, pseudo-loosening artifacts and image distortion" | Sec. 3.2.1, p. 2 |
| MAR, TSA | Artefactos secundarios O-MAR | "pseudo-cemented appearance, and pseudo-notching of the scapula" | Sec. 3.2.1, p. 2 |
| MAR, columna | 82 % artefactos secundarios | "found secondary artifacts in 82 % of the images with O-MAR" | Sec. 3.2.2, p. 3 |
| MAR, columna | Efecto de artefactos secundarios | "may result in overcorrection of the original artifact, mimic implant loosening" | Sec. 3.2.2, p. 3 |
| monoE, THA | Rango 130-200 keV | "MonoE of 130–200 kiloelectron volt (keV) are able to reduce metal artifacts" | Sec. 3.3.1, p. 3 |
| monoE, THA bilateral | Inferior a MAR | "reduction by high energy monoE can be inferior to MAR algorithms" | Sec. 3.3.1, p. 3 |
| monoE, TSA | 130 keV | "MonoE of 130 keV reduce metal artifacts caused by TSA implants" | Sec. 3.3.1, p. 3 |
| monoE, TAA | 150 y 190 keV | "monoE of 150 and 190 keV can be used to reduce metal artifacts" | Sec. 3.3.1, p. 3 |
| monoE, TKA | No reduce severos | "Severe metal artifacts caused by TKA implants were not reduced by high energy monoE" | Sec. 3.3.1, p. 3 |
| monoE, dental | 130-200 keV | "assessment of soft tissue on 130–200 keV monoE" | Sec. 3.3.1, p. 3 |
| monoE, osteosintesis | Filograna, 109-144 keV | "found an optimal keV in the range of 109–144 keV" | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Bamberg, energias comparadas | "compared monoE of 64, 69, 88, 105 and a manually adjusted optimal keV" | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Bamberg, 105 keV | "suggested 105 keV monoE as a robust standard" | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Horat, 130 optimo | "An optimal keV of 130 was found by Horat et al." | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Horat, rango comparado | "when comparing monoE of 64–130 keV and polychromatic images" | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Mangold, 130 keV | "intramedullary fixation devices on 130 keV monoE compared to polychromatic images" | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Wellenberg, rango e incremento | "compared mono of 70–190 keV with an increment of 10 keV" | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Wellenberg, optimo por material | "130, 180 and 190 keV for titanium plates, stainless steel plates" | Sec. 3.3.2, p. 4 |
| monoE, osteosintesis | Hakvoort, 130-150 segun material | "optimal fracture visibility on 130–150, which depends on the implant material" | Sec. 3.3.2, p. 4 |
| monoE, columna | Wang y Dong | "optimal keV ranges of respectively 110–140 keV and 100–140 keV" | Sec. 3.3.2, p. 4 |
| monoE, columna | Ceccarelli, 100-140 keV | "found best diagnostic quality on 140 keV monoE" | Sec. 3.3.2, p. 4 |
| monoE, columna | Lee, 70 y 150 keV | "compared monoE of 70 and 150 keV to polychromatic images" | Sec. 3.3.2, p. 4 |
| monoE, columna | Lee, resultado | "increased signal-to-noise ratio (SNR) and improved image quality on 150 keV monoE" | Sec. 3.3.2, p. 4 |
| monoE, columna | Van Hedent, 80-200 keV | "found 140 keV as optimal energy level for general image quality" | Sec. 3.3.2, p. 4 |
| monoE, columna | Grosse Hokamp, 140/200 keV | "bone-metal interface was best assessable on 200 keV monoE" | Sec. 3.3.2, p. 4 |
| monoE, columna | Grosse Hokamp, canal espinal | "highest image quality for the spinal canal was observed on the 140 keV monoE" | Sec. 3.3.2, p. 4 |
| monoE, columna | Dangelmaier, 160/180/200 keV | "optimal assessment of bone and the spinal canal at 200 keV" | Sec. 3.3.2, p. 4 |
| monoE, columna | Dangelmaier, musculo y aorta | "adjacent muscle at 160 keV and optimal assessment of the aorta at 180 keV" | Sec. 3.3.2, p. 4 |
| monoE, columna | Zeng, 40-190 keV | "found an optimal keV of 130 for assessment of metal-bone interface" | Sec. 3.3.2, p. 4 |
| monoE, columna | Zeng, canal espinal | "120 keV monoE were optimal to assess the spinal canal" | Sec. 3.3.2, p. 4 |
| monoE, CIED | 100/140/200 keV | "MonoE of 100, 140 and 200 keV can be used to reduce metal artifact" | Sec. 3.3.3, p. 4 |
| monoE, cardiovascular | 100 y 120 keV | "The application of 100 and 120 keV monoE reduces metal artifacts" | Sec. 3.3.4, p. 4 |
| monoE, cardiovascular | Comparacion 40-80 keV | "compared to monoE of 40–80 keV, yielding improved image quality" | Sec. 3.3.4, p. 4 |
| monoE, cardiovascular | Laukamp, 100-200 | "reduction of artifacts ... soft tissue, organs and sternal bone on monoE of 100–200" | Sec. 3.3.4, p. 4 |
| monoE, cardiovascular | Schwartz, 60/100 keV | "improved leaflet visualization on the 100 keV monoE" | Sec. 3.3.4, p. 4 |
| monoE, intracraneal | Zopfs, sin reduccion cuantitativa | "no significant reduction of metal artifacts by monoE of 100, 140 and 200" | Sec. 3.3.5, p. 5 |
| monoE, intracraneal | Jia, 60 keV | "optimal contrast to noise ratio of the cerebral arteries at 60 keV" | Sec. 3.3.5, p. 5 |
| DECT+MAR, THA | Neuhaus, 140-200 keV + O-MAR | "superior reduction of hypodense metal artifact on monoE of 140–200 keV with O-MAR" | Sec. 3.4.1, p. 5 |
| DECT+MAR, THA | Neuhaus, musculo | "no significant difference was observed ... for the assessment of adjacent muscles" | Sec. 3.4.1, p. 5 |
| DECT+MAR, THA | Yue, 120 y 140 keV | "periprosthetic soft tissue and prosthesis-related problems on monoE of 120 and 140 keV" | Sec. 3.4.1, p. 5 |
| DECT+MAR, THA | Chandrasekar, fantoma | "due to the loss of overall image contrast in 130 keV monoE" | Sec. 3.4.1, p. 5 |
| DECT+MAR, TKA | Kim, energias | "comparing monoE of 70, 95, 115, 140 and without MARS" | Sec. 3.4.1, p. 5 |
| DECT+MAR, TKA | Kim, 14.7 % secundarios | "secondary artifacts were introduced by MARS in 14.7 % of the images" | Sec. 3.4.1, p. 5 |
| DECT+MAR | Chea, 120 keV + O-MAR | "better depicted on 120 keV with O-MAR and polychromatic images with O-MAR" | Sec. 3.4.1, p. 5 |
| DECT+MAR | Choo, 130-190 keV | "compared to monoE of 130–190 keV with iMAR by Choo et al." | Sec. 3.4.1, p. 5 |
| DECT+MAR, TSA | Mohammadinejad, 130 keV | "best images quality on 130 keV with iMAR" | Sec. 3.4.1, p. 5 |
| DECT+MAR, dental | Laukamp, O-MAR | "The combination of O-MAR with 100, 140 and 200 keV showed reduction" | Sec. 3.4.1, p. 5 |
| DECT+MAR, dental | Schmidt, energias | "monoE of 40, 70, 100, 120, 150 and 190 keV with iMAR" | Sec. 3.4.1, p. 5 |
| DECT+MAR, dental | Schmidt, 100 keV | "MonoE of 100 keV with iMAR showed improved reduction of hypo-attenuating artifacts" | Sec. 3.4.1, p. 5 |
| DECT+MAR, THA | Bongers, sin diferencias | "130 keV with iMAR to polychromatic images with iMAR, no significant differences" | Sec. 3.4.1, p. 5 |
| DECT+MAR, columna | Ceccarelli, 140 keV + MARS | "severe secondary artifacts on 140 keV monoE with MARS" | Sec. 3.4.2, p. 5 |
| DECT+MAR, columna | Long, 130 keV + iMAR | "stronger metal artifact reduction on 130 keV monoE with iMAR" | Sec. 3.4.2, p. 5 |
| DECT+MAR, CIED | Pennig | "monoE of 100, 140 and 200 with O-MAR provided strongest reduction" | Sec. 3.4.3, p. 5 |
| DECT+MAR, CIED | Pennig, cables | "monoE of 100 keV with O-MAR did provide improved assessment" | Sec. 3.4.3, p. 5 |
| DECT+MAR, intracraneal | Zopfs, 140-200 | "recommending monoE of 140–200 with O-MAR" | Sec. 3.4.4, p. 5 |
| DECT+MAR, intracraneal | 24 % secundarios | "Secondary artifacts were observed in 24 % of polychromatic images with O-MAR" | Sec. 3.4.4, p. 5 |
| DECT+MAR, intracraneal | 6-8 % secundarios | "and on 6–8 % of the monoE with O-MAR" | Sec. 3.4.4, p. 5 |
| DECT+MAR, CTA | Zhang/Shinohara | "40–70 monoE with MARS and 40–75 monoE with MARS" | Sec. 3.4.4, p. 5 |
| DECT+MAR, CTA | Comparacion | "when compared to monoE of 80–140 with MARS" | Sec. 3.4.4, p. 5 |
| DECT+MAR, CTA | Jia, 60 keV + MARS | "highest contrast-to-noise ratios (CNRs) in the cerebral arteries on 60 keV monoE" | Sec. 3.4.4, p. 5 |
| DECT+MAR, CTA | Dunet, 65 y 70 keV | "monoE of 65 and 70 keV with MARS as the best compromise" | Sec. 3.4.4, p. 5 |
| Escala Tabla 1 | Definicion + / ++ / +++ | "+Small reduction of metal artifacts, ++medium reduction of metal artifacts, +++large reduction" | Tabla 1, p. 6 |
| Escala Tabla 1 | Definicion +/- | "+/-added value is questionable" | Tabla 1, p. 6 |
| Escala Tabla 1 | Definicion daga | "severe secondary artifacts may be introduced" | Tabla 1, p. 6 |
| Escala Tabla 1 | Criterio numerico de severe/medium/small | NO ENCONTRADO EN EL PDF | — |
| Tabla 1 | Categoria implantes grandes | "Large and high-density implants Severe artifacts" | Tabla 1, p. 6 |
| Tabla 1 | Categoria osteosintesis | "Osteosynthesis materials Medium artifacts" | Tabla 1, p. 6 |
| Tabla 1 | Categoria dispositivos cardiacos | "Electronic cardiac device Medium artifacts" | Tabla 1, p. 6 |
| Tabla 1 | Categoria metal cardiovascular | "Cardiovascular metal Medium-small artifacts" | Tabla 1, p. 6 |
| Tabla 1 | Categoria metal intracraneal | "Intercranial metal Small artifacts" | Tabla 1, p. 6 |
| Tabla 1 | Artroplastia cadera: monoE / MAR | "Hip arthroplasty ... 120–200 keV++ +++" | Tabla 1, p. 6 |
| Tabla 1 | Artroplastia rodilla | "Knee arthroplasty ... 120–140 keV+ +++" | Tabla 1, p. 6 |
| Tabla 1 | Artroplastia hombro | "Shoulder arthroplasty ... 130 keV++ +++" | Tabla 1, p. 6 |
| Tabla 1 | Artroplastia tobillo | "Ankle arthroplasty ... 105–150 keV++ +++" | Tabla 1, p. 6 |
| Tabla 1 | Dental | "Dental ... 130–200 keV+ +++" | Tabla 1, p. 6 |
| Tabla 1 | Recomendacion implantes grandes | "140 keV + MAR" | Tabla 1, p. 6 |
| Tabla 1 | Placas ortopedicas | "Orthopedic plates ... 110–180 keV++ +/-" | Tabla 1, p. 6 |
| Tabla 1 | Clavos intramedulares | "Intramedullary nails ... 130–190 keV++ +/-" | Tabla 1, p. 6 |
| Tabla 1 | Tornillos ortopedicos | "Orthopedic screws ... 109–144 keV++ +/-" | Tabla 1, p. 6 |
| Tabla 1 | Tornillos espinales | "Spine screws ... 105–200 keV++ +†" | Tabla 1, p. 6 |
| Tabla 1 | Recomendacion osteosintesis | "130 keV MonoE" | Tabla 1, p. 6 |
| Tabla 1 | CIED dispositivo / cables | "Device ... 140–200 keV+ ++"; "Leads ... 100 keV++ ++" | Tabla 1, p. 6 |
| Tabla 1 | Recomendacion CIED | "100 keV + MAR" | Tabla 1, p. 6 |
| Tabla 1 | Valvula aortica / alambres esternales | "Aortic valve replacement ... 100 keV++ +/-"; "Sternal wires ... 100–200 keV++ +/-" | Tabla 1, p. 6 |
| Tabla 1 | Stent coronario / clips bypass | "Coronary artery stent ... 100–120 keV++ +/-"; "Bypass clips ... 100–120 keV++ +/-" | Tabla 1, p. 6 |
| Tabla 1 | Recomendacion cardiovascular | "100 keV monoE" | Tabla 1, p. 6 |
| Tabla 1 | Intracraneal sin contraste / CTA | "(unenhanced) ... 100–200 keV++ ++"; "(CTA) ... 40–75 keV+ ++" | Tabla 1, p. 6 |
| Tabla 1 | Recomendaciones intracraneal | "140 keV + MAR"; "65 keV + MAR" | Tabla 1, p. 6 |
| Resumen | Efectividad dependiente del metal | "greatly depends on metal size, shape and alloy" | Sec. 3.5, p. 6 |
| Resumen | Alcance de recomendaciones | "may not be the optimal strategy for each individual patient" | Sec. 3.5, p. 6 |
| Resumen | Costo de monoE alta energia | "monoE of high energy decrease contrast between tissues" | Sec. 3.5, p. 6 |
| Resumen | Variabilidad por fabricante | "effectiveness of metal artifact reduction and the introduction of secondary artifacts varies by vendor" | Sec. 3.5, p. 6 |
| PCCT | Grosor de septa | "These septa are approximately 0.1 mm thick" | Sec. 4.1, p. 6 |
| PCCT | Zhou, bins > 75 keV | "improved anatomical reconstruction on > 75 keV bin images" | Sec. 4.1, p. 7 |
| PCCT | Costo de bins de alta energia | "comes at a cost of increased noise and reduction of overall image contrast" | Sec. 4.1, p. 7 |
| PCCT, THA | Layer, energias | "polychromatic images and monoE of 100, 130, 160 and 190 keV" | Sec. 4.1, p. 7 |
| PCCT, THA | Layer, mejor resultado | "best result on 100 keV monoE with iMAR" | Sec. 4.1, p. 7 |
| PCCT, dental | Risch | "No significant difference was observed when comparing monoE of > 70 keV to 70 keV" | Sec. 4.1, p. 7 |
| PCCT, dental | Patzer | "stronger reduction ... was observed on monoE of 110–190 with iMAR" | Sec. 4.1, p. 7 |
| PCCT vs DECT | Bjorkman, objetivo | "the objective analysis showed no significant differences" | Sec. 4.1, p. 7 |
| PCCT, columna | Popp, rango e incremento | "monoE of 60–190 keV with a 10 keV increment on a clinical PCCT" | Sec. 4.1, p. 7 |
| PCCT, columna | Popp, metrica artifact index | "lowest artifact index values on monoE of 110 keV" | Sec. 4.1, p. 7 |
| PCCT, fantomas | Anhaus, 40-190 keV | "compared monoE of 40–190 keV (10 keV increment) with and without iMAR" | Sec. 4.1, p. 7 |
| PCCT, fantomas | Anhaus, cabeza de cadera | "unsatisfactory reduction of metal artifacts in metals with high atomic numbers" | Sec. 4.1, p. 7 |
| PCCT, columna | Anhaus, kVp y keV | "optimal keV of 100 and 120 keV was found when scanning with 120 kVp" | Sec. 4.1, p. 7 |
| PCCT, THA | Material: Ti vs CoCr (Fig. 6) | "cobalt-chromium femur component causing severe metal artifacts" | Fig. 6, p. 7 |
| PCCT, THA | Energias de Fig. 6 | "monoE of 70, 90, 110 and 140 keV" | Fig. 6, p. 7 |
| MAR proyeccion | Dependencia de prior en FSNMAR | "it strongly relies on the generation of a prior image" | Sec. 4.1, p. 8 |
| MAR proyeccion | Errores de segmentacion del prior | "segmentation of bone and soft tissue, which commonly results in segmentation errors" | Sec. 4.1, p. 8 |
| MAR proyeccion | PCNMAR limite | "PCNMAR was unable to outperform FSNMAR in case of severe metal artifacts" | Sec. 4.1, p. 8 |
| DL MAR | Falta de referencia | "The ground truth image, with metal but without metal artifacts, is generally not available." | Sec. 4.2, p. 8 |
| DL MAR | Simulacion de artefactos (Zhang) | "used CT images without metal to simulate images with metal and metal artifacts" | Sec. 4.2, p. 8 |
| DL MAR | Variedad de implantes simulados | "wide variety of metal implants, from small clips to bilateral hip prostheses" | Sec. 4.2, p. 8 |
| DL MAR | Dominios | "image-to-image deep learning models ... sinogram-to-sinogram deep learning models" | Sec. 4.2, p. 8 |
| DL MAR | Dual-domain | "dual-domain deep learning models using both image and sinogram data" | Sec. 4.2, p. 8 |
| DL MAR | No supervisado | "no need for paired data and therefore simulation is not required" | Sec. 4.2, p. 8 |
| DL MAR | Comparadores cuantitativos | "stronger reduction of metal artifacts in comparison to NMAR and linear interpolation techniques" | Sec. 4.2, p. 8 |
| Criterio de evaluacion | Limitacion de evaluacion DL | "limited to visual inspection without structured assessment by radiologists and without statistical testing" | Sec. 4.2, p. 8 |
| Criterio de evaluacion | Koike, artifact index | "significant reduction of artifact index" | Sec. 4.2, p. 8 |
| Criterio de evaluacion | Koike, dosis | "dose distributions with smaller dose errors were found" | Sec. 4.2, p. 8 |
| Criterio de evaluacion | Arabi, PET | "most accurate PET attenuation maps were observed when applying the deep learning based MAR" | Sec. 4.2, p. 9 |
| Pelvis | Selles, fusion sacroiliaca pre/post | "patients who underwent sacroiliac joint fusion were included" | Sec. 4.2, p. 9 |
| Criterio de evaluacion | Selles, referencia pre-cirugia | "metal artifacts in muscle and bone were quantified using the pre-surgery scan" | Sec. 4.2, p. 9 |
| Criterio de evaluacion | Metrica usada por Selles (definicion) | NO ENCONTRADO EN EL PDF | — |
| Criterio de evaluacion | Definicion de "artifact index" | NO ENCONTRADO EN EL PDF | — |
| Criterio de evaluacion | Metricas generales citadas | "reduction of noise, better image quality and decreased artifacts" | Sec. 3.2.1, p. 2 |
| Criterio de evaluacion | CNR, confianza diagnostica | "increased contrast-to-noise ratio, image quality, increased diagnostic confidence" | Sec. 3.2.4, p. 3 |
| Criterio de evaluacion | Exactitud de valores CT | "improved accuracy of CT values, image quality, diagnostic confidence" | Sec. 3.2.1, p. 2 |
| Conclusion | Sin solucion general | "there is still not one general solution to reduce metal artifacts" | Sec. 5, p. 9 |
| Conclusion | monoE y artefactos leves | "High energy monoE effectively reduce mild metal artifacts" | Sec. 5, p. 9 |
| Conclusion | monoE y artefactos severos | "unable to achieve satisfactory reduction of severe metal artifacts caused by large implants" | Sec. 5, p. 9 |
| Conclusion | Evaluacion recomendada | "paired pre-surgery and post-surgery CT-scans, enabling a comparison with true non-metal reference images" | Sec. 5, p. 9 |
| Conclusion | Riesgo DL | "alter the CT-image in a way that clinically relevant information is lost" | Sec. 5, p. 9 |
| Conflicto de interes | Colaboracion con fabricante | "has established a research collaboration with Philips Healthcare regarding metal artefact reduction" | Acknowledgements, p. 9 |
