# yun2026simulationdriven — MLD-MAR: MAR guiado por simulacion para mejorar generalizabilidad

- **DOI / URL:** 10.1002/mp.70336 (Med Phys. 2026;53:e70336). Codigo: https://github.com/dbstjstod1/MLD-MAR
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/yun2026simulationdriven.pdf

## Que hace (3 lineas maximo)
Propone MLD-MAR, marco auto-supervisado de reduccion de artefactos metalicos que combina un MLP
que ajusta un polinomio de correccion de beam-hardening en el dominio de proyeccion con un modelo
de difusion latente condicional (LDM) que elimina el artefacto residual. Reusa los parametros del
MLP para simular imagenes contaminadas a partir de CT limpias y generar pares pseudo-emparejados,
evitando datos pareados reales. Evalua en SynDeepLesion y en datos clinicos (CLINIC-metal de
CTPelvic1K y Mayo Clinic).

## Restriccion o supuesto clave
El pipeline nunca genera el metal: lo asume dado como mascara binaria M, y en clinica esa mascara se
obtiene por umbral de intensidad. La simulacion solo produce el artefacto residual condicionado a esa
mascara. Frases: "the metal-only projection can be used to model the artifact correction map"
(Sec. 2.1, p.3); "F(M) itself contains no tissue or bone information" (Sec. 2.1, p.4);
"metal regions were segmented using intensity thresholding" (Sec. 2.4.2, p.8);
"The accuracy of the metal mask directly impacts the quality of artifact modeling" (Sec. 4, p.17).
Ademas declara un limite fisico explicito: "the proposed framework has an inherent limitation in
scenarios with severe photon starvation" (Sec. 4, p.17).

## Que toco de aqui
- [x] numero que cito
- [ ] metodo que reimplemento
- [x] baseline de comparacion (solo como referencia de uso de CLINIC-metal, no como MAR)
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| CTPelvic1K: 1,184 volumenes, >320,000 cortes | "consists of 1,184 pelvic CT volumes (over 320,000 slices)" | Sec. 2.4.2, p.8 |
| 75 estudios con artefacto metalico (CLINIC-metal) | "including 75 scans with metal artifacts (CLINIC-metal subset)" | Sec. 2.4.2, p.8 |
| Mascaras metalicas de CLINIC-metal obtenidas por umbral | "metal regions were segmented using intensity thresholding" | Sec. 2.4.2, p.8 |
| Ventana de despliegue clinica [-538, 702] HU | "The display window is [-538,702] HU." | Fig. 5, p.11 |
| Ventana de despliegue [-381, 659] HU | "The display window is [-381, 659] HU." | Fig. 4, p.9 |
| Ventana en CTPelvic1K [-803, 1061] HU | "CTPelvic1K WL:[-803, 1061] HU" | Fig. 13, p.18 |
| Sesgo HU medio en ROI libre de artefacto: 0.82 (propuesto) vs 3.18 (InDuDoNet+) | "HU Bias (Mean) ... 3.18 ... 0.82" | Tabla 4, p.11 |
| RMSE clinico en ROI libre de artefacto: 21.01 (propuesto) vs 23.47 | "RMSE 24.43 23.47 37.78 35.07 21.01" | Tabla 3, p.11 |
| Limitacion de CatSim/XCIST para benchmarking DL | "only compatible with its own CPU-based reconstruction module" | Sec. 4, p.18 |
| Dificultad de simular artefactos realistas | "challenging to generate synthetic metal artifacts that accurately reflect the complex physical behaviors" | Sec. 1, p.2 |

## Donde entra en mi tesis
- Justificacion del gap (Obj3/Obj5): confirma que sintetizar artefactos metalicos fisicamente
  realistas sigue siendo un problema abierto y que la falta de datos pareados motiva simulacion.
- Datos (docs/02-datos.md): evidencia externa de las cifras de CTPelvic1K/CLINIC-metal y de que
  CLINIC-metal no trae ni referencia libre de artefacto ni anotacion de metal.
- Baseline fisico (XCIST/CatSim): aporta una critica citable a CatSim como plataforma de simulacion
  para benchmarking con redes modernas.
- Renderizador: precedente directo de LDM condicional en dominio CT con condicionamiento por imagen,
  aunque en direccion inversa (quitar artefacto, no ponerlo).
- Metricas: usa PSNR/RMSE/SSIM y, en clinica sin ground truth, RMSE y sesgo HU en ROI libre de
  artefacto; ese protocolo sin referencia es directamente reusable para validar el renderizador.

## Dudas para el asesor
1. El protocolo clinico sin ground truth (RMSE y sesgo HU en ROI libre de artefacto) sirve como
   metrica auxiliar para validar el realismo del renderizador de MetalSynth, o confunde el mensaje
   por venir de la literatura MAR?
2. La critica a CatSim en Sec. 4 p.18 (solo reconstruccion CPU, no diferenciable) afecta la decision
   de reimplementar XCIST como brazo de comparacion?
3. Este paper deja el metal como mascara dada. Conviene citarlo como evidencia de que nadie sintetiza
   la geometria del implante, o es un uso demasiado forzado?

## Evidencia textual
| Dato / umbral / criterio | Frase original (max 15 palabras) | Seccion / pagina |
|---|---|---|
| lambda de perturbacion del ruido = 0.04 | "In this study, λ was heuristically determined to 0.04" | Sec. 2.2, p.4 |
| Error de reconstruccion acotado a ±4% | "to constrain the reconstruction error within ± 4% of the reference MLP parameters" | Sec. 2.2, p.4 |
| Nivel de confianza ~68% (±1σ) | "corresponding to a confidence level of ∼68% (± 1σ)" | Sec. 2.2, p.4 |
| lambda >= 0.08 excluido por respuestas exageradas | "For λ ≥ 0.08, the artifact simulation begins to produce exaggerated responses" | Sec. 3.2.2, p.14 |
| Latente x4 sub-muestreado (CVQ-VAE) | "using × 4 down-sampled latent representations" | Sec. 2.3.1, p.4 |
| Embedder: batch 16, lr 3e-4, codebook 4096, dim 4 | "batch size of 16, a learning rate of 3 × 10−4, a codebook size of 4096" | Sec. 2.3.1, p.6 |
| Programa de ruido de 1,000 pasos | "following a noise scheduling protocol of 1,000 steps" | Sec. 2.3.2, p.6 |
| Solo 5 pasos DDIM en inferencia | "only 5 DDIM steps were used to improve computational efficiency" | Sec. 2.3.2, p.6 |
| lr del LDM = 2e-4 | "trained using the Adam optimizer with a learning rate of 2 × 10−4" | Sec. 2.3.2, p.6 |
| Refinamiento con NMAR + capa CNN ligera | "performed using the Normalized Metal Artifact Reduction (NMAR) technique" | Sec. 2.3.3, p.6 |
| SDD = 793.8 mm | "source-to-detector distance (SDD) of 793.8 mm" | Sec. 2.4.1, p.7 |
| SOD = 396.9 mm | "source-to-rotation-center distance (SOD) of 396.9 mm" | Sec. 2.4.1, p.7 |
| Efectos fisicos simulados | "polychromatic X-rays, partial volume effect, beam hardening, and Poisson noise" | Sec. 2.4.1, p.7 |
| Entrenamiento: 1,000 CT x 90 mascaras = 90,000 pares | "A total of 1,000 CT images and 90 metal masks were used to generate 90,000 paired" | Sec. 2.4.1, p.7 |
| Test: 200 CT x 10 mascaras = 2,000 pares | "200 CT images combined with 10 metal masks were used to synthesize 2,000 paired" | Sec. 2.4.1, pp.7-8 |
| Resolucion 416 x 416 pixeles | "Each CT image has a resolution of 416 × 416 pixels" | Sec. 2.4.1, p.8 |
| 640 proyecciones en 360 grados | "640 projections were uniformly distributed over 360 degrees" | Sec. 2.4.1, p.8 |
| Sinogramas 641 x 640 | "sinograms have dimensions of 641 × 640" | Sec. 2.4.1, p.8 |
| CTPelvic1K: 1,184 volumenes, >320,000 cortes | "consists of 1,184 pelvic CT volumes (over 320,000 slices)" | Sec. 2.4.2, p.8 |
| 75 estudios con metal (CLINIC-metal) | "including 75 scans with metal artifacts (CLINIC-metal subset)" | Sec. 2.4.2, p.8 |
| CLINIC-metal sin referencia pareada ni anotacion de metal | "the dataset lacks both paired artifact-free references and metal mask annotations" | Sec. 2.4.2, p.8 |
| Redimensionado clinico a 416 x 416 | "CT images were resized to 416 × 416 pixels to match the training resolution" | Sec. 2.4.2, p.8 |
| Sin fine-tuning en datos clinicos | "MLD-MAR was applied directly to these clinical cases without any fine-tuning" | Sec. 2.4.2, p.8 |
| CLINIC-metal no provee sinogramas | "this dataset does not provide sinogram data" | Sec. 2.4.2, p.8 |
| Metricas cuantitativas usadas | "root-mean-squared error (RMSE), peak signal-to-noise ratio (PSNR), and structural similarity index (SSIM)" | Sec. 2.4.2, p.8 |
| Region de la mascara metalica excluida de la evaluacion | "The metal mask region is excluded from the quantitative evaluation" | Sec. 3.1.1, p.8 |
| MLD-MAR: PSNR 46.45 (σ=3.53) | "46.45 (σstd = 3.53)" | Tabla 1, p.10 |
| MLD-MAR: RMSE 12.74 (σ=5.36) | "12.74 (σstd = 5.36)" | Tabla 1, p.10 |
| MLD-MAR: SSIM 0.993 (σ=2.77E-3) | "0.993 (σstd = 2.77E−3)" | Tabla 1, p.10 |
| InDuDoNet+: PSNR 43.88 / RMSE 18.28 / SSIM 0.988 | "43.88 (σstd = 4.71) 18.28 (σstd = 10.53) 0.988" | Tabla 1, p.10 |
| CNNMAR: PSNR 37.30 / RMSE 34.85 / SSIM 0.968 | "37.30 (σstd = 2.52) 34.85 (σstd = 10.42) 0.968" | Tabla 1, p.10 |
| Score-MAR: PSNR 34.64 / RMSE 49.59 / SSIM 0.961 | "34.64 (σstd = 3.55) 49.59 (σstd = 24.95) 0.961" | Tabla 1, p.10 |
| DuDoDp-MAR: PSNR 37.05 / RMSE 35.49 / SSIM 0.968 | "37.05 (σstd = 2.19) 35.49 (σstd = 8.73) 0.968" | Tabla 1, p.10 |
| Costo: 2.16 s, 2094 MB, 5 pasos (propuesto) | "MLD-MAR (proposed) 2.16 2094 5" | Tabla 2, p.10 |
| Score-MAR y DuDoDp-MAR: 22 s, 2107 MB, 1000 pasos | "Score-MAR 22 2107 1000" | Tabla 2, p.10 |
| Definicion de PSNR | "PSNR is defined as PSNR = 20log10(MAX/RMSE)" | Sec. 3.1.1, p.10 |
| Razon de RMSE 1.435 -> 3.14 dB esperados | "20log10(1.435)≈3.14 dB, which is in close agreement" | Sec. 3.1.1, p.10 |
| MLP converge en <500 pasos, ~1.69 s, 24 MB | "completes within 500 steps, taking only ∼1.69 seconds and consuming 24 MB" | Sec. 3.1.1, p.10 |
| Inferencia del LDM: ~0.47 s, 2070 MB | "the conditional LDM takes ∼0.47 seconds and requires 2070 MB" | Sec. 3.1.1, p.10 |
| RMSE clinico ROI1 (5 metodos) | "RMSE 24.43 23.47 37.78 35.07 21.01" | Tabla 3, p.11 |
| Sesgo HU medio ROI2 (5 metodos) | "HU Bias (Mean) 4.20 3.18 6.30 5.89 0.82" | Tabla 4, p.11 |
| Criterio de evaluacion clinica sin ground truth | "we calculated the RMSE and HU bias within artifact-free ROIs" | Sec. 3.1.2, p.10 |
| Ablacion de condicionamiento: X_MA da PSNR 44.31 | "Using XMA 44.31(σstd = 4.34) 16.91(σstd = 11.06) 0.990" | Tabla 5, p.13 |
| Ablacion de condicionamiento: X_LI da RMSE 17.71 | "Using XLI 44.31(σstd = 4.34) 17.71(σstd = 8.43) 0.989" | Tabla 5, p.13 |
| Test agrupado: 10 metales, 200 imagenes por tipo | "consists of 2000 images, with 200 images per metal type" | Sec. 3.2.1, p.13 |
| Orden polinomial elegido: 6 | "we selected the 6th-order polynomial in this study" | Sec. 3.2.1, p.13 |
| Perdida de ajuste minima 3.29E-7 en orden 6 | "6 3.29E−7" | Tabla 6, p.14 |
| Perdida de ajuste en orden 1: 2.24E-6 | "1 2.24E−6" | Tabla 6, p.14 |
| Pasos de inferencia: 5 da PSNR 39.15 / RMSE 27.42 | "5 39.15(σstd = 1.48) 27.42(σstd = 4.07) 0.987" | Tabla 7, p.15 |
| Pasos de inferencia: 1 da PSNR 38.06 | "1 38.06(σstd = 1.65) 31.03(σstd = 4.10) 0.982" | Tabla 7, p.15 |
| Sin mejora significativa mas alla del paso 5 | "No significant improvement was observed beyond step 5" | Sec. 3.2.3, p.14 |
| Ganancia del refinamiento: +18% PSNR, -53% RMSE, +0.6% SSIM | "approximate 18% increase in PSNR, a 53% reduction in RMSE, and a 0.6% increase in SSIM" | Sec. 3.2.4, p.15 |
| Escaner Mayo: SOMATOM Definition AS+ | "acquired using a SOMATOM Definition AS + scanner (single-source mode, Siemens Healthcare)" | Sec. 4, p.17 |
| Tension y mAs de referencia Mayo: 120 kVp, QRM 200 | "tube potential of 120 kVp and a quality reference mAs (QRM) of 200" | Sec. 4, p.17 |
| Ranking en el AAPM CT MAR Challenge 2024 (top solutions) | "ranking among the top solutions using only the provided dataset" | Sec. 1, p.3 |
| Desempeno top-5 en el AAPM Challenge 2024 | "achieved top-5 performance without using any additional external datasets" | Sec. 4, p.17 |
| CBCT: 0.90 s por proyeccion, 150 iteraciones, 25 MB | "0.90 seconds per single projection image (904 × 724 resolution) for 150 iterations" | Sec. 4, p.18 |
| Hardware de benchmarking: RTX 3090, 24 GB | "performed on an NVIDIA RTX 3090 GPU with 24 GB of memory" | Sec. 4, p.18 |
| Limitacion de CatSim/XCIST (recon solo CPU) | "only compatible with its own CPU-based reconstruction module, limiting its use for benchmarking" | Sec. 4, p.18 |
| Dataset AAPM 2024 generado con CatSim | "the 2024 AAPM Challenge dataset was generated using CatSin,29 a simulation platform" | Sec. 4, p.18 |
| Gap: dificultad de simular artefactos fisicamente realistas | "challenging to generate synthetic metal artifacts that accurately reflect the complex physical behaviors" | Sec. 1, p.2 |
| Metodos supervisados requieren pares raros en clinica | "such data are rarely available in real-world clinical settings" | Sec. 1, p.2 |
| Ausencia de priors fisicos causa alucinacion | "prone to hallucination, anatomical distortion, and unstable artifact suppression" | Abstract, p.1 |
| Limitacion por photon starvation | "inherent limitation in scenarios with severe photon starvation" | Sec. 4, p.17 |
| La precision de la mascara metalica condiciona el modelado | "The accuracy of the metal mask directly impacts the quality of artifact modeling" | Sec. 4, p.17 |

## Verificacion de nivel

**1. Como simula el metal y sus artefactos? Que simulador o que fisica usa? Menciona XCIST, CatSim o similares?**

No usa XCIST ni CatSim para su propia simulacion. Dos mecanismos distintos:

(a) Datos sinteticos de entrenamiento/test (SynDeepLesion): simulacion analitica de haz en abanico
siguiendo un protocolo de terceros. Cita: "The simulation protocol applied to this dataset follows,21
incorporating metal masks from.10" (Sec. 2.4.1, p.7). Fisica declarada: "several physical effects were
taken into account, including polychromatic X-rays, partial volume effect, beam hardening, and Poisson
noise" (Sec. 2.4.1, p.7). Geometria: SDD 793.8 mm, SOD 396.9 mm, 640 proyecciones sobre 360 grados.

(b) Su aporte propio, la "residual artifact simulation": no es un simulador fisico completo sino un
modelo parametrico. Ajusta un MLP a un polinomio de beam-hardening sobre el mapa de longitud de
trayecto metalico y luego perturba esos parametros con ruido gaussiano para generar el artefacto
residual sobre CT limpias. Cita: "we introduce a physically motivated model of these residual
artifacts and simulate them to guide the training of our LDM" (Sec. 2.2, p.4); "the learned MLP
parameters are reused to simulate artifact-contaminated images from artifact-free scans" (Abstract,
p.1). El componente residual se compone de mismatch de no-linealidad mas artefacto de volumen
parcial: "X_res = F^-1(Δ) + X_pv" (Ec. 4, Sec. 2.2, p.4).

CatSim/XCIST si aparece, pero como comentario sobre datasets ajenos y con una critica explicita:
"the 2024 AAPM Challenge dataset was generated using CatSin,29 a simulation platform that accurately
models X-ray interactions with matter based on cross-section data and includes scatter modeling.
However, this dataset is only compatible with its own CPU-based reconstruction module, limiting its
use for benchmarking with modern deep learning models that require GPU-based differentiable forward
and backward projectors." (Sec. 4, p.18). La referencia 29 es el paper de XCIST (Wu M, Fitzgerald P,
Zhang J, et al. XCIST—An open access X-ray/CT simulation toolkit. Phys Med Biol. 2022;67(19)).

**2. La tarea aguas abajo es MAR o segmentacion?**

MAR, sin ambiguedad. No hay tarea de segmentacion aguas abajo. Citas:
"We address computed tomography (CT) metal artifacts reduction (MAR) using a generative deep-learning
model in the imaging physics framework" (Abstract, p.1); "We proposed MLD-MAR, a self-supervised metal
artifact reduction framework" (Conclusion, p.19). La segmentacion aparece solo como paso auxiliar para
obtener la mascara del metal, y el propio paper la declara fuera de alcance: "the development of an
accurate and robust metal segmentation algorithm is beyond the scope of this study" (Sec. 4, p.17).

**3. Que mide como "generalizability" y contra que conjuntos? Metricas y cifras?**

Generalizabilidad = aplicar el modelo entrenado solo con datos sinteticos auto-supervisados a datos
clinicos reales de otros dominios, sin fine-tuning. Cita: "MLD-MAR was applied directly to these
clinical cases without any fine-tuning, demonstrating its robustness and generalizability across
real-world scenarios" (Sec. 2.4.2, p.8) y "we intentionally refrained from such finetuning to
demonstrate the native generalizability of the proposed framework" (Sec. 3.1.2, p.10).

Conjuntos: (i) SynDeepLesion (sintetico, 2,000 cortes de test); (ii) CLINIC-metal de CTPelvic1K
(clinico, sin ground truth); (iii) Mayo Clinic LDCT (clinico, solo cualitativo, Fig. 13);
(iv) un dataset dental de CBCT como estudio de factibilidad (Fig. 14).

Metricas y cifras:
- Sintetico (Tabla 1, p.10): PSNR / RMSE / SSIM. MLD-MAR 46.45 / 12.74 / 0.993;
  InDuDoNet+ 43.88 / 18.28 / 0.988; CNNMAR 37.30 / 34.85 / 0.968;
  DuDoDp-MAR 37.05 / 35.49 / 0.968; Score-MAR 34.64 / 49.59 / 0.961.
- Clinico sin ground truth: RMSE en ROI libre de artefacto 1 (Tabla 3, p.11): MLD-MAR 21.01,
  InDuDoNet+ 23.47, CNN-MAR 24.43, DuDoDp-MAR 35.07, Score-MAR 37.78. Sesgo HU medio en ROI libre
  de artefacto 2 (Tabla 4, p.11): MLD-MAR 0.82, InDuDoNet+ 3.18, CNN-MAR 4.20, DuDoDp-MAR 5.89,
  Score-MAR 6.30.
- Costo (Tabla 2, p.10): 2.16 s y 2094 MB en 5 pasos, frente a 22 s y 1000 pasos de los difusivos.
- No reporta Dice, HD95 ni ninguna metrica de segmentacion: NO ENCONTRADO EN EL PDF.

**4. Usa CT pelvica o alguna anatomia con osteosintesis? Que dataset?**

Si. Usa CT pelvica clinica con implantes: el subconjunto CLINIC_METAL de CTPelvic1K. Cita:
"we additionally tested on a publicly available clinical CT dataset, referred to as CLINIC_METAL,
based on the CTPelvic1K dataset.28" (Sec. 2.4.2, p.8). Las Figuras 5, 6 y 13 muestran cortes pelvicos
con material metalico lineal compatible con osteosintesis, y el origen se describe como
"primarily from a collaborating orthopedic hospital" (Sec. 2.4.2, p.8). El dataset sintetico
SynDeepLesion tambien incluye pelvis entre sus regiones: "diverse anatomical regions such as the
lungs, abdomen, liver, and pelvis" (Sec. 2.4.1, p.7). El termino "osteosintesis" o el tipo de implante
(tornillo, placa) no se nombra: NO ENCONTRADO EN EL PDF.

**5. Menciona CTPelvic1K o CLINIC-metal?**

Si, ambos, explicitamente y con cifras. "based on the CTPelvic1K dataset.28 The CTPelvic1K dataset
consists of 1,184 pelvic CT volumes (over 320,000 slices) collected from multiple domains and
manufacturers, including 75 scans with metal artifacts (CLINIC-metal subset), covering diverse
appearance variations." (Sec. 2.4.2, p.8). Tambien lo etiqueta en Fig. 13 (p.18) y lo cita en la
discusion (Sec. 4, p.17). La referencia 28 es Liu et al., CTPelvic1K, Int J Comput Assist Radiol Surg.
2021;16(5):749-756.

**6. Dice explicitamente que los datos simulados son insuficientes o poco realistas?**

Si, en tres lugares. Citas literales:
- "in the absence of highly realistic simulation pipelines, it is challenging to generate synthetic
  metal artifacts that accurately reflect the complex physical behaviors observed in clinical CT
  scans." (Sec. 1, p.2). Esta es la frase que sostiene el gap.
- "These synthetic sinograms are then directly used to produce final corrected images despite their
  physical inaccuracy due to the nonlinearity of metal-induced artifacts." (Sec. 2.4.2, p.8), critica
  a estudios previos que forward-proyectan imagenes ya contaminadas.
- "this dataset is only compatible with its own CPU-based reconstruction module, limiting its use for
  benchmarking with modern deep learning models" (Sec. 4, p.18), sobre el dataset AAPM/CatSim, y
  "We acknowledge the importance of well-designed, publicly shareable, and extensible datasets"
  (Sec. 4, p.19).

Matiz importante para la tesis: el paper afirma el gap pero tambien lo estrecha en parte, porque su
propia simulacion residual la califica de suficiente y bien caracterizada: "The behavior of the
artifact simulation process is well characterized in the ablation study." (Sec. 4, p.15). Y limita el
realismo por diseno: "For λ ≥ 0.08, the artifact simulation begins to produce exaggerated responses
relative to the observed mismatch patterns, and thus these cases were excluded" (Sec. 3.2.2, p.14),
es decir, calibra la severidad del artefacto a mano en vez de derivarla de fisica completa.

**7. Compara contra algun metodo generativo (GAN, difusion) para generar los artefactos?**

No para generar artefactos. Los metodos generativos con los que compara (Score-MAR, DuDoDp-MAR;
y CycleGAN/ADN/β-CycleGAN mencionados en la introduccion) son metodos de eliminacion de artefactos,
no de sintesis. Cita: "we compare MLD-MAR with several existing MAR approaches, including CNN-MAR,
InDuDoNet +, a score-based diffusion model (Score-MAR), and the DuDoDp-MAR diffusion model."
(Sec. 3, p.8). Para generar el artefacto usa exclusivamente su simulacion parametrica basada en el
MLP; no hay ablacion que enfrente "artefacto simulado por fisica" contra "artefacto generado por
GAN/difusion": NO ENCONTRADO EN EL PDF.

Lo mas cercano a una ablacion de generacion es la Tabla 5 (p.13), que compara entradas de
condicionamiento del LDM (X_MA, X_LI, imagen corregida por beam-hardening), no fuentes de artefacto.

**8. Nivel que sostiene la evidencia**

**Nivel 2.** La promocion a Nivel 1 hecha solo con el titulo no se sostiene: la tarea aguas abajo es
MAR y no segmentacion osea, la simulacion es un modelo parametrico 2D de beam-hardening y no un
simulador fisico tipo XCIST, y no reporta ninguna metrica de segmentacion. Pero es mas que apoyo:
aporta cifras citables de CTPelvic1K/CLINIC-metal, la frase que sostiene el gap de realismo de
simulacion, una critica directa a CatSim/XCIST como brazo de comparacion, y un protocolo de
evaluacion clinica sin ground truth (RMSE y sesgo HU en ROI libre de artefacto) reutilizable.

Nota para la autora: la clasificacion final es decision suya; aqui solo se reporta lo que sostiene la
evidencia textual.

## Candidatos de snowballing detectados

| Cita como aparece | Por que podria importar |
|---|---|
| 21. Yu L, Zhang Z, Li X, Xing L. Deep sinogram completion with image prior for metal artifact reduction in CT images, 2020. | Fuente original del protocolo de simulacion de artefactos metalicos de SynDeepLesion, incluido el set de efectos fisicos y la geometria. Compite directamente con la fisica del renderizador. |
| 10. Zhang Y, Yu H. Convolutional neural network based metal artifact reduction in X-Ray computed tomography. IEEE Trans Med Imaging. 2018;37(6):1370-1381. | Fuente de las mascaras metalicas usadas para simular (90 entrenamiento, 10 test, "realistic implant shapes"); es la referencia canonica del banco de formas de implante, comparable a mi banco de 61 geometrias. |
| 3. Meyer E, Raupach R, Lell M, Schmidt B, Kachelriess M. Normalized metal artifact reduction (NMAR) in computed tomography. Med Phys. 2010;37(10):5482-93. | Metodo de refinamiento usado aqui; baseline clasico y posible componente del brazo de comparacion no aprendido. |
| 29. Wu M, Fitzgerald P, Zhang J, et al. XCIST—An open access X-ray/CT simulation toolkit. Phys Med Biol. 2022;67(19). | Ya esta en refs.bib como wu2022xcist, pero aqui aparece con una limitacion citable (reconstruccion solo CPU, no diferenciable) que afecta la decision de usarlo como brazo de comparacion. |
| 22. Haneda E, Peters N, Zhang J, et al. AAPM CT metal artifact reduction grand challenge. Med Phys. 2025;52:e70050. | Ya en refs.bib como haneda2025aapm; aqui se usa como benchmark externo y como origen del dataset generado con CatSim. |
| 28. Liu P, Han H, Du Y, et al. Deep learning to segment pelvic bones: large-scale CT datasets and baseline models. Int J Comput Assist Radiol Surg. 2021;16(5):749-756. | Ya en refs.bib como liu2021ctpelvic1k; confirma la fuente de las cifras de CTPelvic1K y CLINIC-metal. |
| 23. Zheng C, Vedaldi A. Online clustered codebook. IEEE Int. Conf. Comput. Vis. pp. 22741-22750, 2023. | CVQ-VAE, el embedder latente usado; alternativa concreta al autoencoder del LDM del renderizador. |
| 25. Song J, Meng C, Ermon S. Denoising Diffusion Implicit Models. ICLR 2021. | Muestreador DDIM que permite el costo de 5 pasos; relevante para el presupuesto computacional del renderizador. |
| 30. McCollough C, Chen B, Holmes D, et al. Low dose CT image and projection data (LDCT-and-Projection-data) (Version 7), The Cancer Imaging Archive, 2020. | Segundo dataset clinico externo con parametros de adquisicion explicitos (120 kVp, QRM 200); util como dominio adicional de validacion. |
| 31. Choi D, Yun S, Hyun S, Cho S. Metal artifact reduction algorithm with conditional latent diffusion model for dental cone-beam CT. J Appl Clin Med Phys. 2025;26:e70317. | Version previa del LDM condicional del mismo grupo; precedente metodologico directo del renderizador latente condicionado. |
| 13. Wang H, Li Y, Zhang H, Meng D, Zheng Y. InDuDoNet+: a deep unfolding dual domain network for metal artifact reduction in CT images. Med Image Anal. 2023;85:102729. | Estado del arte supervisado con el que se compara todo; referencia de las cifras de PSNR/RMSE/SSIM del segundo mejor metodo. |
