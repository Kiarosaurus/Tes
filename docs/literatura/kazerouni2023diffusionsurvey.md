# kazerouni2023diffusionsurvey — Survey de modelos de difusion en imagen medica

- **DOI / URL:** DOI: NO ENCONTRADO EN EL PDF. El PDF local es el preprint arXiv:2211.07804v3 [eess.IV], 3 Jun 2023 (sello lateral, p. 1); repositorio del survey: https://github.com/amirhossein-kz/Awesome-Diffusion-Models-in-Medical-Imaging (nota al pie, p. 1). Datos de la version publicada en MedIA (volumen, paginas): NO ENCONTRADO EN EL PDF.
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/kazerouni2023diffusionsurvey.pdf

Profundidad: texto completo (33 paginas, arXiv v3), lectura con foco en CT, espacio latente, limitaciones y lista de referencias. Las paginas citadas son las del preprint, no las de MedIA.

## Que hace (3 lineas maximo)

Revisa la literatura de difusion en imagen medica hasta octubre de 2022 (con algunos trabajos hasta abril de 2023): teoria (DDPM, NCSN, SDE) y taxonomia por aplicacion, modalidad, organo y algoritmo.
Agrupa los trabajos en nueve categorias (traduccion imagen-imagen, reconstruccion, registro, clasificacion, segmentacion, denoising, generacion, anomalias, otras) y los resume en la Tabla 1.
Cierra con retos abiertos: velocidad, espacio de representacion, arquitectura, privacidad/memorizacion, aprendizaje federado.

## Restriccion o supuesto clave

El survey no trata implantes metalicos, artefactos metalicos, MAR, unidades Hounsfield ni ventanas de HU: NO ENCONTRADO EN EL PDF en ninguna de las 33 paginas, incluida la lista de 192 referencias. Tampoco aparece ControlNet (NO ENCONTRADO EN EL PDF).
El supuesto mas cercano que choca con implantes rigidos es la perdida de estructura en la difusion directa: "diffusion models inherently lack the ability to maintain the structural information accurately" (Sec. 4.1, p. 10), porque "structured details of the source domain images are lost during the forward diffusion process" (Sec. 4.1, p. 10). Es un argumento a favor de condicionar (el survey dice que el condicionamiento es "one of the most studied methods", Sec. 4.10, p. 20), pero no se prueba con metal.
Sobre espacio latente, lo unico explicito es que CoLa-Diff busca "address potential issues with compression and noise present in the latent space" (Sec. 4.7, p. 17), en MRI. Una frase sobre limitaciones de autoencoders preentrenados en imagen natural aplicados a imagen medica: NO ENCONTRADO EN EL PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 103 articulos revisados | "It is worth mentioning that the overall number of papers is 103." | Fig. 1, pie de figura, p. 2 |
| Corte de la revision: octubre 2022 (+ algunos hasta abril 2023) | "all available relevant papers (until October 2022)" / "some of the latest techniques through April 2023" | Sec. 1, p. 2 |
| Modalidades: 54% MRI, 38% rayos X (incluye CT), 6% optica, 2% nuclear | Etiquetas del grafico de torta; asignacion por color de la leyenda | Fig. 1b, p. 2 |
| Dominio de CT y MRI | "most of the published studies utilize CT and MRI as modalities" | Sec. 5, p. 22 |

## Donde entra en mi tesis

- **Estado del arte / trabajo relacionado (renderizador, Objetivo del renderizador LDM 2.5D):** solo contexto general de difusion en imagen medica. No reduce el gap: ninguna entrada del survey sintetiza metal, implantes ni artefactos metalicos en CT con difusion, y no lista trabajos de MAR con difusion (NO ENCONTRADO EN EL PDF).
- **Codificacion multi-ventana en HU / rango dinamico de HU / VAE para CT:** NO ENCONTRADO EN EL PDF. No hay precedente citable aqui.
- **Difusion en CT que si aparece (todas sin metal):** MRI->CT con DDPM/SDE en el dataset Gold Atlas pelvis masculina (Lyu y Wang [49], Sec. 4.1, p. 10); DOLCE para CT de angulo limitado en C4KC-KiTS [103] (Sec. 4.2, p. 11-12); MCG, CT multiorgano, SDE [58] (Fig. 5, p. 9); SIM-SGM CT/MRI [52]; MT-Diffusion CT/MRI [49]; SynDiff MRI/CT [51]; BAnoDDPM listado como CT/MRI [73] (Fig. 5, p. 9); CT de baja dosis con DDPM [133] y CoreDiff [134] (citados en Sec. 4.6, p. 14; titulos en referencias, p. 30); desplazamiento de linea media en CT de cabeza [168] y fracturas vertebrales con Diffusion Autoencoder [169] (Sec. 4.9, p. 19).
- **Espacio latente en medicina:** brainSPADE con LDM [61] (p. 13), Packhauser et al. con LDM para radiografia de torax [145] (p. 17), CoLa-Diff [151] (p. 17), BAnoDDPM con VQ-VAE [73] (p. 17-18), CDPM con normalizacion dinamica "to avoid saturation in latent space pixels" [71] (p. 17). Ninguno discute HU ni autoencoders de imagen natural.
- **Motivacion de datos sinteticos (fuera de alcance medirla):** frases de contexto sobre escasez de datos y combinacion sintetico+real (Sec. 3, p. 7-8). Utiles solo para la introduccion; la tesis no mide impacto downstream.
- **Riesgo de memorizacion:** "diffusion models tend to memorize individual images from their training data" (Sec. 5, p. 23), citando a Carlini et al. [191]. Posible frase de contexto para la discusion de limitaciones del renderizador.

## Dudas para el asesor

- El PDF local es arXiv v3 (3 Jun 2023), no la version de MedIA. Se cita la version publicada (necesitaria su raw en refs/raw/ y paginas propias) o el preprint?
- La Sec. 4 dice "seven application categories" (p. 8) pero la taxonomia y la Sec. 1 hablan de nueve. Es una inconsistencia interna del preprint; si se cita el numero de categorias hay que elegir una fuente.
- Basta un survey de 2023 (corte octubre 2022) para sostener que no hay sintesis de metal con difusion, o hace falta una busqueda propia posterior a esa fecha?

## Evidencia textual

| Item | Frase original (<= 15 palabras) | Seccion / pagina |
|---|---|---|
| Version del PDF | "arXiv:2211.07804v3 [eess.IV] 3 Jun 2023" | Sello lateral, p. 1 |
| DOI de MedIA | NO ENCONTRADO EN EL PDF | - |
| Tres marcos de difusion | "diffusion probabilistic models, noise-conditioned score networks, and stochastic differential equations" | Abstract, p. 1 |
| Total de articulos | "It is worth mentioning that the overall number of papers is 103." | Fig. 1, p. 2 |
| Modalidades (grafico) | Etiquetas "54%" (MRI), "38%" (X-ray based), "6%" (Optical), "2%" (Nuclear) | Fig. 1b, p. 2 |
| Porcentajes por aplicacion (grafico) | Etiquetas visibles 24%, 21%, 19%, 13%, 8%, 7%; asignacion a categorias no legible sin ambiguedad | Fig. 1a, p. 2 |
| Corte temporal | "a comprehensive overview of all available relevant papers (until October 2022)" | Sec. 1, p. 2 |
| Extension temporal | "showcase some of the latest techniques through April 2023" | Sec. 1, p. 2 |
| Dos categorias de modelos | "We divide the existing diffusion models into two categories" | Sec. 1, p. 2 |
| Nueve categorias de aplicacion | "we group the applications of diffusion models into nine categories" | Sec. 1, p. 2 |
| Siete categorias (inconsistencia) | "diffusion-based methods, which are proposed ... in seven application categories" | Sec. 4, p. 8 |
| Fuentes de busqueda | "We searched DBLP, Google Scholar, and Arxiv Sanity Preserver" | Search Strategy, p. 3 |
| Criterio de seleccion | "novelty, contribution, significance, and if being the first introduced paper in medical imaging" | Search Strategy, p. 3 |
| Profundidad por tema | "we selected two or three of the highest-ranked papers to examine in more detail" | Search Strategy, p. 3 |
| Requisitos de modelos generativos | "(i) high-quality sampling, (ii) mode coverage and sample diversity, and (iii) fast execution" | Sec. 2.1, p. 3 |
| Definicion schedule DDPM | "T and β1,...,βT ∈ [0,1) represent the number of diffusion steps and the variance schedule" | Sec. 2.2.1, p. 5 |
| Tres muestreadores SDE | "Three commonly used techniques are discussed in detail below." | Sec. 2.3.2, p. 7 |
| Limitacion del solver ODE | "while ODE is a quick solver, it lacks a stochastic term to correct errors" | Sec. 2.3.2, p. 7 |
| Escasez de datos | "diffusion models to generate synthetic samples can alleviate the problem of medical data scarcity" | Sec. 3, p. 7 |
| Sintetico + real (Akrout) | "trained using a combination of synthetic and real data perform better" | Sec. 3, p. 7-8 |
| Evaluacion por patologos | "administering a survey to two pathologists with different levels of expertise" | Sec. 3, p. 8 |
| Resultado de la evaluacion | "the pathologists could not distinguish real from synthetic images generated by the diffusion model" | Sec. 3, p. 8 |
| MCG en CT | "Modality: CT", "Organ: Multi-organ", "Algorithm: SDE" (entrada 11. MCG) | Fig. 5, p. 9 |
| BAnoDDPM listado como CT/MRI | "Modality: CT / MRI", "Organ: Brain" (entrada 28. BAnoDDPM) | Fig. 5, p. 9 |
| MRI->CT condicionado | "their reverse process is conditioned on T2w MRI images" | Sec. 4.1, p. 10 |
| Dataset pelvico MRI->CT | "Their extensive experiments on the Gold Atlas male pelvis dataset" | Sec. 4.1, p. 10 |
| Criterio de evaluacion MRI->CT | "outperform both CNN and GAN-based methods in terms of Structural Similarity Index Measure" | Sec. 4.1, p. 10 |
| Monte Carlo en MRI->CT | "the model outputs ten times, and the average yields the final result" | Sec. 4.1, p. 10 |
| Valores SSIM/PSNR de Fig. 6 | Rotulos numericos dentro de la figura no legibles en la lectura realizada; no transcritos | Fig. 6, p. 10 |
| BraTS19 | "which contains four MRI modalities for each subject" | Sec. 4.1, p. 10 |
| Perdida de estructura | "diffusion models inherently lack the ability to maintain the structural information accurately" | Sec. 4.1, p. 10 |
| Causa de la perdida | "structured details of the source domain images are lost during the forward diffusion process" | Sec. 4.1, p. 10 |
| DOLCE, CT angulo limitado | "addressed the limited-angle CT reconstruction with a model-based DDPM paradigm called DOLCE" | Sec. 4.2, p. 11 |
| DOLCE, condicionamiento FBP | "incorporates the output of FBP on the limited sinograms as prior information" | Sec. 4.2, p. 12 |
| DOLCE, evaluacion | "The results of the Kidney CT (C4KC-KiTS) dataset [105] regarding SSIM and PSNR" | Sec. 4.2, p. 12 |
| brainSPADE en latente | "The compressed latent code is then diffused and denoised via LDMs" | Sec. 4.5, p. 13 |
| brainSPADE, sintetico vs real | "comparable results when trained on synthetic data compared to that trained on factual data" | Sec. 4.5, p. 13 |
| brainSPADE, evaluador | "nnU-Net [122] was leveraged to examine the performance" | Sec. 4.5, p. 13 |
| CIMD, datasets | "three datasets (one private and two publicly available ones) with different modalities" | Sec. 4.5, p. 14 |
| PatchDDM 3D | "generate meaningful three-dimensional segmentation while requiring less computational resources" | Sec. 4.5, p. 14 |
| CT baja dosis con difusion (refs) | "diffusion models are convenient for diverse denoising problems [133, 134]" | Sec. 4.6, p. 14 |
| Ref [133] | "Low-dose CT using denoising diffusion probabilistic model for 20× speedup" | Referencias, p. 30 |
| Ref [134] | "CoreDiff: Contextual error-modulated generalized diffusion model for low-dose CT denoising" | Referencias, p. 30 |
| SNR en OCT | Rotulos "SNR=92dB", "SNR=96dB", "SNR=101dB" | Fig. 10, p. 15 |
| Ground truth OCT | "the average of 5 successive b-scans as the ground truth" | Fig. 10, p. 15 |
| Test PET | "left hemisphere from 20 18F-MK-6240 test dataset" | Fig. 11, p. 15 |
| PET-DDPM, metrica | "compared with U-Net [79] based denoising network in terms of PSNR and SSIM" | Sec. 4.6, p. 15 |
| DDM, factor latente | "scaling the latent code with a factor, which is an element of [0, 1]" | Sec. 4.7, p. 16 |
| LDM en radiografia | "utilize a latent diffusion model [120] to produce high-quality class-conditional chest X-ray images" | Sec. 4.7, p. 17 |
| Evaluacion LDM radiografia | "the images are evaluated on a thoracic abnormality classification task" | Sec. 4.7, p. 17 |
| Costo en espacio de pixel | "these models often suffer from high memory demands" | Sec. 4.7, p. 17 |
| Problemas del latente (CoLa-Diff) | "In order to address potential issues with compression and noise present in the latent space" | Sec. 4.7, p. 17 |
| Mascaras como prior (CoLa-Diff) | "brain region masks as priors for density distributions to guide the diffusion process" | Sec. 4.7, p. 17 |
| Ruido Simplex | "leveraging Simplex noise over Gaussian noise significantly enhances the performance" | Sec. 4.8, p. 17 |
| Saturacion en latente (CDPM) | "a dynamic normalization technique is applied during inference to avoid saturation" | Sec. 4.8, p. 17 |
| VQ-VAE en BAnoDDPM | "VQ-VAE [164] is first adopted following [120]" | Sec. 4.8, p. 17 |
| Umbral de anomalia | "applying a pre-calculated threshold on the average of intermediate samples" | Sec. 4.8, p. 18 |
| pDDPM, datasets | "Experiments on the public BraTS21 [166] and MSLUB [167] datasets" | Sec. 4.8, p. 18 |
| CT de cabeza | "accurately quantify the brain midline shift observed in head CT images" | Sec. 4.9, p. 19 |
| Fracturas vertebrales | "grading vertebral fractures using a Diffusion Autoencoder (DAE)" | Sec. 4.9, p. 19 |
| R2D2+, datasets | "single coiled fastMRI [98] knee dataset and private liver MRI dataset" | Sec. 4.9, p. 19 |
| R2D2+, metricas | "in terms of SNR and Contrast-to-Noise Ratio (CNR) metrics" | Sec. 4.9, p. 19 |
| ISIC | "Experimental results on the ISIC 2019 dataset [173]" | Sec. 4.9, p. 19 |
| Dataset dental | "a new public dataset with three distinct data types" | Sec. 4.9, p. 20 |
| Condicionamiento como via principal | "conditioning the reverse diffusion process is one of the most studied methods" | Sec. 4.10, p. 20 |
| Metadatos en BrainGen | "age, gender, ventricular volume, and brain volume relative to intracranial volume" | Sec. 4.10, p. 20 |
| DDIM | "resulting in a faster sampling procedure with negligible quality degradation" | Sec. 4.10, p. 20 |
| Aceleracion adversarial | "adversarial learning can boost reverse diffusion speed by two orders of magnitude" | Sec. 4.10, p. 20 |
| Alta frecuencia | "operating the diffusion process only in the high-frequency part of the image improves the stability" | Sec. 4.10, p. 20 |
| Limitacion: velocidad | "a slower generation process compared to some other generative models" | Sec. 5, p. 22 |
| Limitacion: tipos de dato | "limited applicability to certain data types (e.g., audio, text, or structured data)" | Sec. 5, p. 22 |
| Limitacion: verosimilitud y dimension | "lower likelihood compared to other models, and an inability to perform dimensionality reduction" | Sec. 5, p. 22 |
| Modalidades dominantes | "most of the published studies utilize CT and MRI as modalities" | Sec. 5, p. 22 |
| Representacion latente | "less successful in creating semantically meaningful data representations in their latent space" | Sec. 5, p. 22 |
| Arquitectura dominante | "Most diffusion models currently utilize CNN-based architectures with a global attention layer" | Sec. 5, p. 23 |
| Falta de arquitectura medica | "a lack of research focused on improving the architecture of diffusion models for medical imaging" | Sec. 5, p. 23 |
| Memorizacion | "diffusion models tend to memorize individual images from their training data" | Sec. 5, p. 23 |
| Privacidad vs GAN | "diffusion models are much less private compared to other generative models like GANs" | Sec. 5, p. 23 |
| Preprints incluidos | "some of the papers cited in this survey are pre-prints" | Sec. 6, p. 24 |
| Sintesis de metal/implantes/artefactos metalicos con difusion | NO ENCONTRADO EN EL PDF | - |
| Trabajos de MAR con difusion | NO ENCONTRADO EN EL PDF | - |
| Ventanas de HU multiples / rango dinamico de HU / VAE para CT | NO ENCONTRADO EN EL PDF | - |
| Limitaciones de autoencoders/LDM preentrenados en imagen natural aplicados a imagen medica | NO ENCONTRADO EN EL PDF | - |
| ControlNet | NO ENCONTRADO EN EL PDF | - |
