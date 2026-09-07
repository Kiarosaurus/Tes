# ren2022metalinsertion — Insercion de metal en dominio de proyeccion para CT intervencionista

- **DOI / URL:** 10.1117/1.JMI.9.3.035001
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/ren2022metalinsertion.pdf

Profundidad: texto completo (17 paginas, Journal of Medical Imaging 9(3) 035001, May/Jun 2022).

## Que hace (3 lineas maximo)

Extiende una herramienta de insercion de lesiones para insertar objetos metalicos altamente atenuantes (sondas de ablacion) en los datos de proyeccion de CT, incorporando modelos explicitos de ruido cuantico/electronico y de endurecimiento del haz. Valida con maniquies (varilla de titanio) y dos casos de pacientes de crioablacion, y construye una biblioteca de 18 sondas digitales con una GUI. Genera pares co-registrados con y sin artefacto como demostracion de datos de entrenamiento para MAR basada en CNN.

## Restriccion o supuesto clave

No es un metodo generativo: es simulacion analitica en el sinograma y exige acceso a los datos crudos del fabricante. La restriccion mas directa para esta tesis es de escala de metal: "The developed framework may need to be revisited if the amount of inserted metal increased (e.g., in the case of orthopedic implants)" (Sec. 4, p. 035001-15). Ademas supone que la dispersion inducida por el objeto insertado es despreciable ("it is believed that the contribution of perturbations from the inserted objects on the scatter distribution are negligible in our model", Sec. 4, p. 035001-15), asume fuente puntual, ignora efectos de borde K y usa titanio como material de referencia por falta de composicion real.

## Que toco de aqui
- [x] metodo que reimplemento
- [x] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Varilla de Ti de 12.7 mm | "A solid titanium rod (12.7-mm diameter) was inserted into the center hole" | Sec. 2.1.3, p. 035001-5 |
| Maniqui de cabeza 20 cm; cuerpo 30 x 40 cm | "Circular head (20-cm diameter) and elliptical body (30 cm x 40 cm) phantoms" | Sec. 2.1.3, p. 035001-5 |
| Ruido a 20 eff. mAs: 41.06+-1.48 (real) vs 39.78+-1.50 (sim con ruido) | "41.06 +- 1.48 (real rod), 35.37 +- 1.37 (simulated rod without noise model)" | Sec. 3.1, pp. 035001-9/10 |
| Ruido a 200 eff. mAs: 14.32+-0.68 (real) vs 13.21+-0.53 (sim con ruido) | "14.32 +- 0.68 (real rod), 11.53 +- 0.43 ... 13.21 +- 0.53" | Sec. 3.1, p. 035001-10 |
| Proyeccion: 17,678+-542 (real) vs 17,787+-639 (artificial) | "were 17,678 +- 542 and 17,787 +- 639 for the real and artificial rods" | Sec. 3.1, p. 035001-10 |
| Fondo de agua en proyeccion: 13,979+-427 vs 13,960+-402 | "the surrounding water region had measured values of 13,979 +- 427 and 13,960 +- 402" | Sec. 3.1, p. 035001-10 |
| Coef. atenuacion masica de Ti: 0.51, 0.30, 0.27 cm2/g | "for titanium, corresponding to the original and the two new spectra were calculated as 0.51, 0.30, and 0.27" | Sec. 2.1.2, p. 035001-4 |
| Umbrales de senal artefactual: -75 y 75 HU, tope 500 HU | "Thresholds of -75 and 75 HU were used to define the artifactual signal" | Sec. 2.4, p. 035001-7 |
| Umbral definido como +-3 desviaciones estandar del histograma solo-agua | "(+-3 standard deviations of the water-only histogram)" | Sec. 2.4, p. 035001-7 |
| 18 sondas metalicas en la biblioteca digital | "Digital models for 18 metallic probes that are routinely used in our clinical practice" | Sec. 2.3, p. 035001-7 |
| Integracion del espectro de 10 keV al kV maximo | "weighted by the new x-ray spectrum from 10 keV to maximum energy" | Sec. 2.1.2, p. 035001-4 |
| CT numbers del metal exceden miles de HU vs ~50 HU de lesiones | "yielding CT numbers in excess of thousands of HU as compared with ~50 HU" | Sec. 2.1, p. 035001-2 |
| Tanque de agua de 35 cm, sonda a ~26 grados oblicuos | "physically inserted into a 35-cm water tank with an oblique angle of ~26 deg" | Sec. 2.2, p. 035001-6 |
| Reconstruccion de validacion: 1.0/0.5 mm, 512x512, kernel Br40 | "1.0/0.5 mm slice-thickness/increment, 512 x 512 matrix size, medium sharp Br40 kernel" | Sec. 2.1.3, p. 035001-5 |
| Escaner de 128 filas de detectores | "All scans were performed with a 128-detector-rows CT scanner (Definition Flash" | Sec. 2.1.3, p. 035001-5 |

## Donde entra en mi tesis

Objetivo 3 (renderizador) y la justificacion del gap: es el ejemplo publicado y funcionando de insercion analitica de metal en dominio de proyeccion, con validacion fisica, y por tanto es el argumento a batir para justificar un enfoque generativo. Tambien sirve para el brazo de comparacion junto a XCIST/CatSim (ambos requieren simulacion fisica; este ademas requiere raw data de fabricante). Sus umbrales de -75/75/500 HU y el histograma de voxeles afectados son una plantilla directa para operacionalizar ISC / BFC y para definir la banda B_delta como region de evaluacion.

## Dudas para el asesor

- Si el paper mismo advierte que el marco "may need to be revisited" cuando aumenta la cantidad de metal (implantes ortopedicos), conviene citarlo como gap explicito o como limitacion de alcance de la comparacion?
- Se puede usar como brazo de comparacion sin acceso a proyecciones crudas de fabricante en CTPelvic1K? La reimplementacion tendria que hacerse con forward projection generica, exactamente lo que ellos critican de Zhang y Yu.
- Sus umbrales fijos de -75/75 HU vienen de un maniqui de agua; en pelvis con hueso denso habria que redefinir el umbral. Se recalibra con +-3 SD del tejido de referencia local?

## Evidencia textual

| Item (cifra / umbral / definicion / criterio) | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| Dominio de insercion: proyeccion | "framework for metallic object insertion in the projection domain" | Sec. 1, p. 035001-2 |
| Insercion tambien en dominio imagen (sin artefacto) | "images from the image domain insertions are free of artifacts" | Sec. 2.3, p. 035001-7 |
| Objeto insertado: sondas de ablacion | "detailed modeling of ablation probes for image quality optimization" | Sec. 1, p. 035001-2 |
| Base metodologica previa: lesiones | "clinically validated tool to insert liver lesions, lung nodules, and renal stones" | Sec. 2.1, p. 035001-2 |
| Modelo de ruido cuantico y electronico | "increased quantum and electronic noise and beam hardening in the presence" | Sec. 2.1, p. 035001-3 |
| Ruido insertado por integral de linea que cruza el metal | "additional noise element is introduced for each line integral intersecting the metallic object" | Sec. 2.1.1, p. 035001-3 |
| N0 y Ne definidos | "incident photon number and the noise-equivalent quanta of the electronic noise floor" | Sec. 2.1.1, p. 035001-4 |
| x normal estandar | "normally distributed stochastic process with a zero mean and unit variance" | Sec. 2.1.1, p. 035001-4 |
| Modelo de beam hardening en tres pasos | "The model is comprised of three steps." | Sec. 2.1.2, p. 035001-4 |
| WEP = trayecto equivalente en agua | "water equivalent path computed for that specific line integral" | Sec. 2.1.2, p. 035001-4 |
| Titanio como material de referencia | "titanium is used as the reference material for mass attenuation coefficient calculation" | Sec. 2.1.2, p. 035001-4 |
| Escalado de proyecciones por razon de coeficientes | "scaling each projection intersecting the metal based on the ratio" | Sec. 2.1.2, p. 035001-4 |
| Coef. atenuacion masica Ti (original, 30-cm, 40-cm WEP) | "were calculated as 0.51, 0.30, and 0.27 cm2/g, respectively" | Sec. 2.1.2, p. 035001-4 |
| Espectros mostrados: 30 y 40 cm WEP | "two recorded spectra being attenuated by 30- and 40-cm water equivalent materials" | Sec. 2.1.2, p. 035001-4 |
| Diametro varilla Ti | "A solid titanium rod (12.7-mm diameter) was inserted into the center hole" | Sec. 2.1.3, p. 035001-5 |
| Maniquies: 20 cm y 30x40 cm | "Circular head (20-cm diameter) and elliptical body (30 cm x 40 cm) phantoms" | Sec. 2.1.3, p. 035001-5 |
| Escaner usado | "128-detector-rows CT scanner (Definition Flash, Siemens Healthcare, Forchheim, Germany)" | Sec. 2.1.3, p. 035001-5 |
| Protocolo de validacion de ruido: 120 kV, 20 y 200 eff. mAs | "scanned at 120 kV with 20 and 200 effective mAs, respectively" | Sec. 2.1.3, p. 035001-5 |
| Maniqui de cuerpo: 120 kV, 200 eff. mAs | "the body phantom was scanned at 120 kV with 200 effective mAs" | Sec. 2.1.3, p. 035001-5 |
| Herramienta usada para estimar atenuacion | "after estimating its CT number attenuation values using a CT-data simulation tool (DRASIM" | Sec. 2.1.3, p. 035001-5 |
| Parametros de reconstruccion de comparacion | "1.0/0.5 mm slice-thickness/increment, 512 x 512 matrix size, medium sharp Br40 kernel" | Sec. 2.1.3, p. 035001-5 |
| ROI de ruido sobre 100 cortes | "ROI was placed over 100 consecutive slices, and the final values" | Sec. 2.1.3, p. 035001-5 |
| Criterio de comparacion en proyeccion: mapa de diferencia | "difference map was derived as the subtraction between the projection data" | Sec. 2.1.3/2.2, pp. 035001-5/6 |
| Escaneo de sonda: tanque 35 cm, ~26 grados | "inserted into a 35-cm water tank with an oblique angle of ~26 deg" | Sec. 2.2, p. 035001-6 |
| Tabla 1: 120 kV, 200 eff. mAs, pitch 0.6, rot. 0.5 s | "Tube voltage (kV) 120 / Eff. mAs 200 / Pitch 0.6 / Rotation time (s) 0.5" | Tabla 1, p. 035001-6 |
| Tabla 1: colimacion 128 x 0.6 mm, CTDIvol 13.5 mGy | "Collimation (mm) 128 x 0.6 / CTDIvol (mGy) 13.5" | Tabla 1, p. 035001-6 |
| Tabla 1: FOV 200 mm, matrices 512x512 y 1024x1024 | "Recon FOV (mm) 200 200 200 / Matrix size 512 x 512 1024 x 1024" | Tabla 1, p. 035001-6 |
| Tabla 1: escala HU extendida de 16 bits vs 12 bits | "Extended HU scale No (12 bit) No (12 bit) Yes (16 bit)" | Tabla 1, p. 035001-6 |
| Tabla 1: voxel del VOI de la sonda | "Voxel size of VOI containing probe (mm) [0.5 0.5 0.5] [0.2 0.2 0.2]" | Tabla 1, p. 035001-6 |
| Tamano de la biblioteca de sondas | "Digital models for 18 metallic probes that are routinely used" | Sec. 2.3, p. 035001-7 |
| Umbrales de definicion de artefacto | "Thresholds of -75 and 75 HU were used to define the artifactual signal" | Sec. 2.4, p. 035001-7 |
| Justificacion estadistica del umbral | "(+-3 standard deviations of the water-only histogram)" | Sec. 2.4, p. 035001-7 |
| Tope superior para excluir el metal | "upper 500 HU limit was set to exclude voxels corresponding to the metallic probe" | Sec. 2.4, p. 035001-7 |
| Rango de HU analizado en histograma | "all of the voxels with HU values < -75 or [75, 500] were analyzed" | Sec. 2.4, p. 035001-7 |
| Caso ex-vivo: 2 sondas coplanares como peor caso | "coplanar with the imaging plane to provide a near-worst-case scenario" | Sec. 2.4, p. 035001-7 |
| Pacientes: 2 casos de crioablacion percutanea | "Two percutaneous cryoablation cases were used for demonstration." | Sec. 2.5, p. 035001-8 |
| Anatomia de los casos: rinon | "four cryoablation probes were employed to treat two small masses contained in a solitary kidney" | Sec. 2.5, p. 035001-8 |
| Segundo caso: masa renal derecha | "four cryoablation probes were placed to treat a right renal mass" | Sec. 2.5, p. 035001-8 |
| Tabla 2: 140 kV (probe scans), 100 kV (planning) | "Tube voltage (kV) 140 100" | Tabla 2, p. 035001-8 |
| Tabla 2: mAs de referencia 68 y 275; CTDIvol 11.4 / 24.37 / 15.0 mGy | "Quality reference mAs 68 275 ... CTDIvol (mGy) 11.4 24.37 15.0" | Tabla 2, p. 035001-8 |
| Tabla 2: corte 3.0/3.0 mm, 512x512, Br40, 12 bits | "Slice-thickness/increment (mm) 3.0/3.0 ... HU scale 12 bits" | Tabla 2, p. 035001-8 |
| Tercer caso: 4 sondas de dos tipos | "Four cryoablation probes of two different types ... were inserted" | Sec. 2.6, p. 035001-9 |
| Resultado de ruido a 20 eff. mAs | "41.06 +- 1.48 (real rod), 35.37 +- 1.37 (simulated rod without noise model)" | Sec. 3.1, pp. 035001-9/10 |
| Resultado de ruido a 20 eff. mAs (con modelo) | "39.78 +- 1.50 (simulated rod with noise model) for 20 eff. mAs" | Sec. 3.1, p. 035001-10 |
| Resultado de ruido a 200 eff. mAs | "14.32 +- 0.68 (real rod), 11.53 +- 0.43 ... and 13.21 +- 0.53" | Sec. 3.1, p. 035001-10 |
| Criterio cualitativo de validacion del ruido | "yielded a more similar appearance between the images of the real and simulated rods" | Sec. 3.1, p. 035001-9 |
| Valores de proyeccion real vs artificial | "17,678 +- 542 and 17,787 +- 639 for the real and artificial rods" | Sec. 3.1, p. 035001-10 |
| Valores de proyeccion en agua circundante | "13,979 +- 427 and 13,960 +- 402, respectively" | Sec. 3.1, p. 035001-10 |
| Fila de detector usada para comparar | "middle detector row (i.e., row number = 32) were selected and cropped" | Sec. 3.1, p. 035001-10 |
| Ventana del mapa de diferencia | "a much narrower window of 200 was selected compared with ... (W = 10,000)" | Sec. 3.1, p. 035001-11 |
| Criterio de validacion del beam hardening | "bright blooming artifacts ... were absent; however, they were well-replicated" | Sec. 3.1, p. 035001-10 |
| Causa del desalineamiento residual en proyeccion | "caused by imperfectly aligned insertion positions, as well as differences in x-ray tube starting angles" | Sec. 3.1, p. 035001-11 |
| Modelo optimo de sonda: alta resolucion + HU extendida | "higher fidelity ... from the high-resolution and extended HU scale reconstruction appears necessary" | Sec. 3.2, p. 035001-11 |
| Ventana usada en Fig. 8 | "window/level = 10,000/2000 HU" | Fig. 8, p. 035001-11 |
| Ventana usada en Fig. 9 | "(W/L = 1500/500 HU)" | Fig. 9, p. 035001-12 |
| Ventana usada en Figs. 11, 13, 14 | "(W/L = 400/40 HU)" | Figs. 11/13/14, pp. 035001-13/14 |
| Resultado ex-vivo: histogramas bajos bien igualados | "low value histograms (< -75 HU) ... were well matched" | Sec. 3.4, p. 035001-12 |
| Resultado ex-vivo: histogramas altos algo menores | "slightly lower for the artificially inserted probes compared with real probes" | Sec. 3.4, p. 035001-12 |
| Limitacion: no hubo comparacion cuantitativa en pacientes | "relative movement of the patient's organs and the inserted probes prevented quantitative comparison" | Sec. 3.5, p. 035001-13 |
| Criterio cualitativo en pacientes | "the simulated probes are indistinguishable from real ones contained in the same CT image" | Sec. 3.5, p. 035001-13 |
| Requisito de co-registro para CNN | "accurate coregistration is a requirement" | Sec. 3.6, p. 035001-13 |
| Sesgo del dominio imagen | "probes inserted in the image domain appear longer than the corresponding probes in the projection domain" | Sec. 3.6, p. 035001-14 |
| Necesidad del dominio de proyeccion | "insertion of the metallic object in the projection domain rather than in the image domain was vital" | Sec. 4, p. 035001-15 |
| Limitacion: efectos no modelados | "finite focal spot size (assumed a point source) and perturbations from the inserted objects on x-ray scatter" | Sec. 4, p. 035001-15 |
| Supuesto sobre dispersion | "the contribution of perturbations from the inserted objects on the scatter distribution are negligible" | Sec. 4, p. 035001-15 |
| Limitacion clave para implantes ortopedicos | "framework may need to be revisited if the amount of inserted metal increased (e.g., in the case of orthopedic implants)" | Sec. 4, p. 035001-15 |
| Limitacion: sin composicion material | "lack of material composition information for probes" | Sec. 4, p. 035001-15 |
| Limitacion: HU no calibrado a otro kV | "the difference in HU values was not calibrated" | Sec. 4, pp. 035001-15/16 |
| Limitacion: sin efectos de borde K | "k-edge effects were not included in the beam hardening model" | Sec. 4, p. 035001-16 |
| Limitacion: desregistro en datos de paciente | "slight misregistration between the real probes and the artificially inserted probes was noticed" | Sec. 4, p. 035001-16 |
| Criterio de tolerancia al desregistro | "not expected to require a perfect registration with a reference, metal-corrupted CT dataset" | Sec. 4, p. 035001-16 |
| Limitacion: un solo modelo de escaner | "this framework was developed on a single CT scanner model" | Sec. 4, p. 035001-16 |
| Requisito de acceso a datos del fabricante | "can be applied with proper access to vendor projection data" | Sec. 4, p. 035001-16 |
| Critica a proyeccion generica (vs Zhang y Yu) | "they used generic forward- and back-projection algorithms to obtain metal and metal-free images" | Sec. 4, p. 035001-15 |
| Aporte diferencial: estructuras internas del dispositivo | "digital models that possessed internal structures that significantly impact artifact generation" | Sec. 4, p. 035001-15 |
| Limitacion de MAR comercial O-MAR fuera de piel | "when the metal protrudes beyond the skin boundary, the O-MAR algorithm could erroneously cause the extension" | Sec. 1, p. 035001-2 |
| Estado del arte MAR en IO | "there is currently no universally applicable commercial tool available for IO procedures" | Sec. 1, p. 035001-2 |
| Contraste de magnitud metal vs lesion | "CT numbers in excess of thousands of HU as compared with ~50 HU or less" | Sec. 2.1, p. 035001-2 |
| Efecto ignorado en modelos previos de lesiones | "which were inconsequential for lesion insertion tasks and thus ignored in previous models" | Sec. 2.1, p. 035001-2 |
| Fecha de recepcion/aceptacion/publicacion | "received Jun. 24, 2021; accepted for publication May 12, 2022; published online Jun. 17, 2022" | Portada, p. 035001-1 |

## Verificacion de nivel

**1. Que inserta exactamente y en que dominio?**
Inserta modelos digitales voxelizados de sondas metalicas de ablacion (crioablacion y microondas) en el **dominio de proyeccion** (sinograma crudo del escaner), y opcionalmente tambien en el dominio imagen para obtener la version sin artefacto. Frases: "framework for metallic object insertion in the projection domain" (Sec. 1, p. 035001-2); "A voxelized high-attenuating metallic object model is forward projected to acquire the initial object projections" (Sec. 2.1, p. 035001-3); "the probe(s) can be artificially inserted into patient data in both the image domain and the projection domain at identical positions" (Sec. 2.3, p. 035001-7).

**2. Genera artefactos o solo la geometria?**
Genera artefactos. Modela explicitamente **beam hardening** y **ruido cuantico y electronico**; la severidad por baja estadistica de fotones se cubre implicitamente por el modelo de ruido, pero el termino "photon starvation" no aparece: NO ENCONTRADO EN EL PDF. Frases: "models accounting for increased quantum and electronic noise and beam hardening in the presence of the metallic object" (Sec. 2.1, p. 035001-3); "the images from the image domain insertions are free of artifacts, whereas those from the projection domain insertions contain metal artifacts" (Sec. 2.3, p. 035001-7); resultado: "they were well-replicated in images of the artificially inserted rod that included the beam hardening model" (Sec. 3.1, p. 035001-10). Streaking oscuro y blooming se cuantifican por histograma: "low value histograms (< -75 HU) corresponding to the dark streaking artifacts along the probe shaft were well matched" (Sec. 3.4, p. 035001-12).

**3. Que anatomia y que tipo de metal?**
Anatomia: abdomen, especificamente **rinon** en los dos casos de paciente ("four cryoablation probes were employed to treat two small masses contained in a solitary kidney", Sec. 2.5, p. 035001-8; "a right renal mass", misma seccion); mas maniquies de cabeza y cuerpo. El objetivo declarado es CT de "different body regions" (Abstract), pero no se muestra pelvis: NO ENCONTRADO EN EL PDF. Metal: **instrumental de intervencion**, no osteosintesis — sondas de crioablacion y microondas (IceForce 2.1 CX, NeuWave XT, Endocare V-Probe) y una varilla solida de titanio como fantoma. Los implantes ortopedicos aparecen solo como escenario *no* cubierto: "may need to be revisited if the amount of inserted metal increased (e.g., in the case of orthopedic implants)" (Sec. 4, p. 035001-15).

**4. Como valida que la insercion es realista?**
Validacion fisica contra adquisiciones reales del mismo objeto, no contra un dataset clinico. Metricas: (a) **nivel de ruido en ROI** (media +- SD sobre 100 cortes) real vs simulado con/sin modelo de ruido: "41.06 +- 1.48 (real rod)" vs "39.78 +- 1.50 (simulated rod with noise model)" a 20 eff. mAs y "14.32 +- 0.68" vs "13.21 +- 0.53" a 200 eff. mAs (Sec. 3.1, pp. 035001-9/10); (b) **valores de proyeccion en ROI y mapa de diferencia**: "17,678 +- 542 and 17,787 +- 639 for the real and artificial rods" (Sec. 3.1, p. 035001-10); (c) **histograma de voxeles afectados por el artefacto** con umbrales -75/75/500 HU (Sec. 2.4, p. 035001-7 y Fig. 12); (d) **comparacion cualitativa** en pacientes: "the simulated probes are indistinguishable from real ones contained in the same CT image" (Sec. 3.5, p. 035001-13). No reporta MAE en HU, SSIM, PSNR ni prueba estadistica: NO ENCONTRADO EN EL PDF.

**5. Usa los datos sinteticos para entrenar alguna red aguas abajo?**
No los usa: solo demuestra la *generacion* de pares de entrenamiento co-registrados y la optimizacion de calidad de imagen. "demonstration of a proof-of-concept application—generation of training data for convolutional neural network (CNN) based MAR algorithms" (Sec. 1, p. 035001-2); "This framework has potential to generate robust training libraries for deep learning algorithms" (Abstract, Conclusions). En futuro condicional: "one could use our framework to generate registered projection data ... and train a CNN model" (Sec. 4, p. 035001-15). Ningun entrenamiento, ninguna metrica downstream (Dice, HD95, etc.): NO ENCONTRADO EN EL PDF.

**6. Limitacion explicita que un metodo generativo podria resolver?**
Si, y es la frase mas util para la tesis. Literal (Sec. 4, p. 035001-15):
> "This assertion appears to be validated by the results ... The developed framework may need to be revisited if the amount of inserted metal increased (e.g., in the case of orthopedic implants)."

Contexto inmediato: el supuesto que se rompe es la dispersion despreciable — "due to the relatively small cross-section and the high atomic number of the metallic probes, it is believed that the contribution of perturbations from the inserted objects on the scatter distribution are negligible in our model" (Sec. 4, p. 035001-15). Limitaciones complementarias citables: fuente puntual asumida; sin efectos de borde K ("k-edge effects were not included in the beam hardening model", Sec. 4, p. 035001-16); sin composicion material real de los dispositivos ("there was a lack of material composition information for probes", Sec. 4, p. 035001-15); HU no calibrado al cambiar de kV ("the difference in HU values was not calibrated", Sec. 4, pp. 035001-15/16); un solo modelo de escaner ("this framework was developed on a single CT scanner model", Sec. 4, p. 035001-16); y dependencia de datos crudos propietarios ("can be applied with proper access to vendor projection data", Sec. 4, p. 035001-16).

**7. Serviria como brazo de comparacion del renderizador?**
Conceptualmente si (es el analogo analitico exacto del renderizador: metal + artefactos, con par co-registrado limpio/corrupto), pero la reimplementacion fiel es dudosa con CTPelvic1K. Lo que haria falta, segun lo que el propio paper exige:
- **Proyecciones crudas del fabricante** y decodificacion de las mismas — el pipeline arranca en "Original CT raw data / Decode raw data" (Fig. 1, p. 035001-3) y ellos reconstruyen "at the CT scanner console using the same algorithms as those used for clinical patient data" (Sec. 4, p. 035001-15). CTPelvic1K son imagenes reconstruidas: esto es el bloqueo principal.
- **Espectro policromatico y DQE del escaner**, que ellos obtuvieron del fabricante: "polychromatic x-ray spectrum and detector quantum efficiency were provided by the CT manufacturer" (Sec. 2.1.2, p. 035001-4).
- **Calibraciones de mA por proyeccion, bowtie y AEC**: "calibrations were performed to estimate photon flux on each detector at a given mA" (Sec. 4, p. 035001-15).
- **Modelo digital del implante con estructura interna**, reconstruido en alta resolucion con escala HU extendida (Sec. 3.2, p. 035001-11) — aqui el banco de 61 geometrias propias cubre la parte geometrica pero no la composicion material ni la escala HU extendida.
- Implementar Ecs. (1)-(3): ruido insertado por integral de linea, espectro esperado via WEP, y escalado por razon de coeficientes de atenuacion masica.
Conclusion practica: sin raw data, la reimplementacion cae en "generic forward- and back-projection", justo lo que ellos critican (Sec. 4, p. 035001-15), lo que la aproximaria a XCIST/CatSim y debilitaria la comparacion. NO ENCONTRADO EN EL PDF: codigo publico, repositorio o disponibilidad de la GUI.

**8. Nivel que sostiene la evidencia: NIVEL 1.**
Sostiene nivel 1 porque contiene la advertencia explicita del propio metodo analitico sobre implantes ortopedicos —la frase que fundamenta el gap de la tesis— y ademas fija umbrales y criterios de validacion de artefacto (-75/75/500 HU, ruido en ROI, histograma de voxeles afectados) directamente reutilizables para ISC/BFC y para definir el brazo de comparacion.

Matiz para la autora: la promocion se hizo asumiendo por el titulo que era candidato a brazo de comparacion; la lectura confirma el valor argumental (punto 6) pero **debilita** la viabilidad del brazo de comparacion, porque el metodo exige datos crudos de fabricante que CTPelvic1K no provee. Es osteosintesis: no. Es imagen reconstruida: no.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| A. Ferrero et al., "Technical note: insertion of digital lesions in the projection domain for dual-source, dual-energy CT," Med. Phys. 44(5), 1655-1660 (2017). [ref. 10] | Fuente original del marco de insercion en dominio de proyeccion que este paper extiende; compite directamente con el renderizador como metodo analitico previo. |
| B. Chen et al., "Lesion insertion in the projection domain: methods and initial results," Med. Phys. 42(12), 7034-7042 (2015). [ref. 11] | Segunda fuente base del pipeline de insercion; define el estandar de validacion "insertar y comparar contra el real". |
| L. Yu et al., "Development and validation of a practical lower-dose-simulation tool for optimizing computed tomography scan protocols," J. Comput. Assist. Tomogr. 36(4), 477-487 (2012). [ref. 12] | Fuente original del modelo de insercion de ruido (Ec. 1) y de la incorporacion de AEC y bowtie; cifra/metodo citable si se reimplementa el brazo analitico. |
| P. Wu et al., "Cone-beam CT for neurosurgical guidance: high-fidelity artifacts correction for soft-tissue contrast resolution," Proc. SPIE 11595, 115950X (2021). [ref. 13] | Es la referencia que respalda la afirmacion clave "insertion in the projection domain rather than in the image domain was vital"; sostiene o refuta un supuesto central del renderizador. |
| Y. Zhang and H. Yu, "Convolutional neural network based metal artifact reduction in x-ray computed tomography," IEEE Trans. Med. Imaging 37(6), 1370-1381 (2018). [ref. 16] | Metodo que tambien inserta metal sinteticamente en proyecciones para entrenar CNN, con forward projection generica: reduce el gap declarado y es candidato a brazo de comparacion mas accesible. |
| W.-A. Lin et al., "DuDoNet: dual domain network for ct metal artifact reduction," CVPR (2019). [ref. 14] | Consumidor tipico de datos sinteticos de metal; util para definir la tarea downstream y su protocolo de datos. |
| L. Yu et al., "Deep sinogram completion with image prior for metal artifact reduction in CT images," IEEE Trans. Med. Imaging 40(1), 228-238 (2021). [ref. 15] | Idem: baseline downstream y potencial fuente de metricas alternativas a ISC/BFC. |
| B. D. Man et al., "Metal streak artifacts in X-ray computed tomography: a simulation study," IEEE Trans. Nucl. Sci. 46(3), 691-696 (1999). [ref. 17] | Fuente clasica sobre la contribucion de la dispersion Compton a los artefactos metalicos; cuestiona el supuesto de dispersion despreciable con mas metal. |
| J. F. Williamson et al., "Prospects for quantitative computed tomography imaging in the presence of foreign metal bodies using statistical image reconstruction," Med. Phys. 29(10), 2404-2418 (2002). [ref. 18] | Segunda fuente sobre dispersion/cuerpos metalicos; relevante para justificar por que un implante grande rompe el modelo analitico. |
| P. Healthcare, "Metal artifact reduction for orthopedic implants (O-MAR)," White Paper, Philips CT Clinical Science (2012). [ref. 6] | Fuente original del criterio de fallo de O-MAR cuando el metal sobresale de la piel; unico item del paper que menciona explicitamente implantes ortopedicos. |
| J. Y. Huang et al., "An evaluation of three commercially available metal artifact reduction methods for CT imaging," Phys. Med. Biol. 60(3), 1047-1067 (2015). [ref. 8] | Comparativa de MAR comerciales; posible fuente de metricas de evaluacion de artefacto que podrian validar o reemplazar ISC. |
| Y. Zhang et al., "A hybrid metal artifact reduction algorithm for x-ray CT," Med. Phys. 40(4), 041910 (2013). [ref. 7] | Baseline clasico de MAR; contexto para el argumento de generalizabilidad limitada. |
