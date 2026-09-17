# abadi2019 — DukeSim: simulador de CT realista, rapido y especifico de escaner

- **DOI / URL:** 10.1109/TMI.2018.2886530 (IEEE Trans. Med. Imag., vol. 38, no. 6, pp. 1457-1465, junio 2019)
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/abadi2019.pdf

## Que hace (3 lineas maximo)
Simulador de CT hibrido en dominio proyeccion para fantomas voxelizados: señal primaria por ray-tracing (Beer-Lambert polienergetico) y scatter por Monte Carlo (MC-GPU v1.3 modificado), con modelos de detector, ruido, crosstalk, bowtie y flying focal spot de un escaner Siemens concreto. Valida contra el fantoma fisico Mercury (sin metal) en contraste, ruido, NPS y MTF, y corre en minutos con 4 GPUs.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; es un simulador fisico. Lo que limita su uso como referencia para implantes metalicos:
- La validacion no incluye metal ni artefactos metalicos: "The validations were performed using a phantom with a simple geometry." (Sec. IV, p. 1464).
- El metal solo aparece como posibilidad de ajuste del scatter, no como caso simulado ni validado: "in case a highly-attenuative object is present in the field of view (e.g., a pacemaker)" (Sec. II-C, p. 1459).
- El beam hardening se simula (espectro polienergetico) pero la unica evaluacion es su supresion en un fantoma de agua con correccion polinomica de agua (Sec. II-E, p. 1460; Fig. 3, p. 1461); no hay correccion de hueso ni de metal.
- El modelado especifico del escaner depende de informacion propietaria del fabricante: "providing us proprietary information which enabled us to model a Siemens CT scanner" (Acknowledgment, p. 1464).
- Disponibilidad publica del codigo: NO ENCONTRADO EN EL PDF.
- Medicion de la extension espacial de artefactos (mm): NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Error relativo < 1.4% (contraste), 0.5% (ruido), 2.6% (textura), 3% (resolucion) | "less than 1.4%, 0.5%, 2.6%, and 3%, for image contrast, noise magnitude, noise texture" | Abstract, p. 1457 |
| ~2-3 min por rotacion con 4 GPUs | "approximately 2-3 minutes per rotation in our study using a computer with 4 GPUs" | Abstract, p. 1457 |
| Validacion en Mercury a 50/150/300 mAs, 120 kV, pitch 1.0 | "(50, 150, and 300 mAs) at 120 kV and a pitch of 1.0" | Sec. II-G, p. 1460 |
| Extension espacial de artefacto metalico | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |

## Donde entra en mi tesis
Related Work / encuadre del brazo fisico: DukeSim como ejemplo de simulador de CT en dominio proyeccion, especifico de escaner, validado solo en fantoma simple sin metal. Sirve para delimitar por que no se usa como baseline (protocolo adoptado: peters2025hybrid) y por que reimplementar un simulador validado esta fuera de alcance (requiere geometria/fisica propietaria del fabricante). Toca las implicancias #57 (no mide extension espacial de artefacto) y #61/#63 (dominio proyeccion frente a dominio imagen). No aporta cifras al muestreador ni al renderizador.

## Dudas para el asesor
- El texto dice "4th order polynomial water correction", pero la Ec. 5 suma p=0 a p=3 (Sec. II-E, p. 1460). ¿Se cita como polinomio de 4.o orden o de grado 3?
- El abstract reporta error de resolucion espacial "less than ... 3%", pero en resultados el f50 del inserto Air tiene "a relative error of 3.1%" (Sec. III-A, p. 1461). ¿Se cita el valor por inserto en vez del resumen del abstract?
- ¿Es correcto presentar DukeSim como "competidor" del protocolo adoptado si no simula ni valida metal en este paper, o conviene describirlo solo como simulador de CT específico de escáner?

## Evidencia textual
| Dato / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| DOI | "Digital Object Identifier 10.1109/TMI.2018.2886530" | p. 1457 (pag. 1 del PDF) |
| Error relativo global real vs simulado | "less than 1.4%, 0.5%, 2.6%, and 3%, for image contrast, noise magnitude, noise texture" | Abstract, p. 1457 |
| Tiempo de ejecucion resumido | "approximately 2-3 minutes per rotation in our study using a computer with 4 GPUs" | Abstract, p. 1457 |
| Resolucion tipica de fantomas en simuladores MC dosimetricos | "low-resolution phantoms (∼5 mm voxel sizes)" | Sec. I, p. 1458 |
| Arquitectura hibrida primario/scatter | "estimates the primary and scatter photons that hit the detector elements using ray-tracing and MC" | Sec. II, p. 1458 |
| Parametros de entrada: flying focal spot | "focal spot periodic wobbles (also known as “Z” and “in-plane” flying focal spots)" | Sec. II-A, p. 1458 |
| Señal primaria por Beer-Lambert | "computed using the Beer-Lambert Law" | Sec. II-B, p. 1458 |
| Muestreo de foco y detector finitos | "the area of the detector and focal spot were uniformly divided (sub-sampled)" | Sec. II-B, p. 1458 |
| Base del modulo de scatter | "the MC-GPU code v1.3 [17] was modified and extended" | Sec. II-C, p. 1459 |
| Geometria del detector | "curved energy-integrating detector model with energy response" | Sec. II-C, p. 1459 |
| Procesos de scatter incluidos | "incorporates scatter contribution from the Compton, Rayleigh, and multiple scatter processes" | Sec. II-C, p. 1459 |
| Suavizado del scatter | "the normalized scatter distribution was further smoothed using an optimized scatter kernel" | Sec. II-C, p. 1459 |
| Unica mencion de objeto altamente atenuante (metal) | "in case a highly-attenuative object is present in the field of view (e.g., a pacemaker)" | Sec. II-C, p. 1459 |
| Crosstalk del detector | "a percentage of the signal of the neighboring detector elements was added" | Sec. II-D, p. 1459 |
| Modelo de ruido | "a Gaussian random number generator [34] is used" | Sec. II-D, p. 1459 |
| Correccion de beam hardening | "a 4th order polynomial water correction was applied to the projection images" | Sec. II-E, p. 1460 |
| Ajuste de coeficientes BHC | "polynomial fit to a mono-energetic simulation of a detector signal attenuated by" | Sec. II-E, p. 1460 |
| Proyecciones por rotacion (rango general) | "number of projections per rotation (∼1000-2500)" | Sec. II-F, p. 1460 |
| Elementos de detector (rango general) | "number of detector elements (∼25,000-50,000)" | Sec. II-F, p. 1460 |
| Bins de energia (rango general) | "linear attenuation coefficients (∼100-200 bins)" | Sec. II-F, p. 1460 |
| Definicion de verificacion | "Verification answers the question of “did I build the thing, right?”" | Sec. II-G, p. 1460 |
| Definicion de validacion | "validation answers the question of “did I build the right thing?”" | Sec. II-G, p. 1460 |
| Escaner de referencia | "a commercial scanner (Somatom Definition Flash; Siemens Healthcare)" | Sec. II-G, p. 1460 |
| Fantoma de validacion | "a virtual model of the clinically-used Mercury phantom [37] was created" | Sec. II-G, p. 1460 |
| Protocolo de validacion | "(50, 150, and 300 mAs) at 120 kV and a pitch of 1.0" | Sec. II-G, p. 1460 |
| Fisica/geometria del escaner provista por fabricante | "the exact geometry and physics for the specific scanner (provided by the manufacturer) were used" | Sec. II-G, p. 1460 |
| Ruido electronico medido | "variance of the detector signal where the beam was blocked using a lead shield" | Sec. II-G, p. 1460 |
| Submuestreo foco/detector | "uniformly sampled 4 and 5 times, respectively (total of 20 sub-samples" | Sec. II-G, p. 1460 |
| Criterio de eleccion del submuestreo | "empirically found to give results close to clinical data, with limited gain beyond" | Sec. II-G, p. 1460 |
| Reconstruccion de validacion | "reconstructed using FreeCT medium kernel" | Sec. II-G, p. 1460 |
| Parametros de reconstruccion | "0.6 mm slice thickness, 512 ×512 in-plane pixels, and 370 mm reconstruction field" | Sec. II-G, p. 1460 |
| Metricas de comparacion real vs simulado | "CT number values, noise magnitude, noise power spectrum (NPS), and modulation transfer function (MTF)" | Sec. II-G, p. 1460 |
| Criterio de exactitud de numero CT | "selecting ROIs within the “Air” and “Water” inserts of the Mercury phantom" | Sec. II-G, p. 1460 |
| ROIs de NPS | "placing 8 squared ROIs (30 mm in radius) in 30 contiguous slices" | Sec. II-G, p. 1460 |
| Posicion de ROIs de NPS | "uniformly distributed in a 40 mm distance from the center of the image" | Sec. II-G, p. 1460 |
| Definicion de magnitud de ruido | "The noise magnitude was measured as the standard deviation in the same ROIs." | Sec. II-G, p. 1460 |
| ROIs de MTF | "circular ROIs (25.4 mm in radius) were placed in the center of the inserts" | Sec. II-G, p. 1460 |
| Calculo de MTF | "MTF was calculated by taking the Fourier transform of the LSF" | Sec. II-G, p. 1460 |
| VCT piloto: repeticiones | "A textured XCAT phantom [13], [14], [16] was imaged 50 times using DukeSim" | Sec. II-H, p. 1460 |
| VCT piloto: reconstrucciones | "(FBP, kernel of B31f) and iterative (SAFIRE, kernel of I31f)" | Sec. II-H, p. 1461 |
| Definicion de mapa de reduccion de ruido | "a relative noise reduction map was calculated as" (Ec. 6) | Sec. II-H, p. 1461 |
| Region de NPS en VCT piloto | "NPS was measured in the lung regions" | Sec. II-H, p. 1461 |
| Resultado BHC en fantoma de agua | "beam hardening artifact, which is a function of spectrum and bowtie filter, was suppressed" | Sec. III-A, p. 1461 |
| Filtro bowtie usado en Fig. 3 | "the images on the second row were acquired using a Siemens “body” filter" | Fig. 3, p. 1461 |
| Contraste Water-Air real vs simulado | "0.0188 ± 1.3e-05 mm2/g and 0.0191 ± 4.0e-05 mm2/g for the real and simulated" | Sec. III-A, p. 1461 |
| Error relativo de contraste | "showing a relative error of 1.4%" | Sec. III-A, p. 1461 |
| Error relativo de ruido por dosis | "relative error was +0.07%, −0.11%, and −0.48% for 50 mAs, 150 mAs, and 300 mAs" | Sec. III-A, p. 1461 |
| Normalizacion de NPS | "the NPS measurements were normalized to have an area of one" | Sec. III-A, p. 1461 |
| Error relativo de frecuencias NPS | "average and peak frequencies of the NPS curves were 2.49% and 2.57%" | Sec. III-A, p. 1461 |
| f_avg NPS: real 0.26/0.26/0.26; DukeSim 0.27/0.27/0.27 mm^-1 (50/150/300 mAs) | "Average and Peak Frequencies of the NPS Curves in the Real (First Row)" | Tabla I, p. 1461 |
| f_peak NPS: real 0.22/0.21/0.21; DukeSim 0.22/0.21/0.22 mm^-1 (50/150/300 mAs) | "Average and Peak Frequencies of the NPS Curves in the Real (First Row)" | Tabla I, p. 1461 |
| MTF f50 inserto Air | "f50) was 0.285 mm−1 and 0.294 mm−1 for the real and simulated images" | Sec. III-A, p. 1461 |
| Error MTF Air | "with a relative error of 3.1%" | Sec. III-A, p. 1461 |
| MTF f50 inserto Bone | "f50 was 0.302 mm−1and 0.303 mm−1for the real and simulated images" | Sec. III-A, p. 1461 |
| Error MTF Bone | "with a relative error of 0.4%" | Sec. III-A, p. 1461 |
| Hardware | "64 GB of memory and four Nvidia Titan Xp GPUs" | Sec. III-B, p. 1461 |
| Tamaño del fantoma del test de velocidad | "1900×1900×1000 voxels and a 0.25 mm isotropic voxel size" | Sec. III-B, p. 1461 |
| Rango de escaneo del test de velocidad | "a scan range of 115.2 mm (3 rotations with pitch of 1.0)" | Sec. III-B, p. 1461 |
| Tiempo de scatter | "2 minutes to obtain the scatter data (10^8 histories per projection and 10-degree" | Sec. III-B, p. 1462 |
| Tiempo de path lengths | "3 minutes to calculate the intersected path lengths" | Sec. III-B, p. 1462 |
| Tiempo de proyecciones finales y tamaño | "4 minutes to calculate the final projection images (47104 detectors × 6912 projection images)" | Sec. III-B, p. 1462 |
| VCT piloto: reduccion de ruido SAFIRE | "the noise was 29% lower in SAFIRE images" | Sec. III-C, p. 1462 |
| VCT piloto: ruido en bordes | "it was higher in the edge voxels" | Sec. III-C, p. 1462 |
| Velocidad (discusion) | "DukeSim simulated a typical CT scan in several minutes" | Sec. IV, p. 1463 |
| Modularidad de efectos fisicos | "noise modeling, polychromacity, scatter, and detector crosstalk can be included or excluded" | Sec. IV, p. 1464 |
| Limitacion de validacion | "The validations were performed using a phantom with a simple geometry." | Sec. IV, p. 1464 |
| Validacion futura con fantomas heterogeneos | "additional investigations are envisioned as future work using physical versions" | Sec. IV, p. 1464 |
| Trabajo futuro: modulacion de corriente | "extend DukeSim to account for tube current modulation" | Sec. IV, p. 1464 |
| Dependencia de informacion propietaria | "providing us proprietary information which enabled us to model a Siemens CT scanner" | Acknowledgment, p. 1464 |
| Simulacion de metal/implante validada contra escaner real | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Extension espacial de artefactos (metalicos o de otro tipo) en mm | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Metricas de streaking, photon starvation o artefacto metalico | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Disponibilidad publica o licencia del codigo | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Modelado explicito de volumen parcial (con ese termino) | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Distancias fuente-detector y fuente-isocentro (valores numericos) | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Numero de filas/canales del detector usados en validacion | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
| Numero de bins de energia usados en validacion | NO ENCONTRADO EN EL PDF | NO ENCONTRADO EN EL PDF |
