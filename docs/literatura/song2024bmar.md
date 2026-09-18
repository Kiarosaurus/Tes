**Profundidad: solo abstract.**

# song2024bmar — b-MAR: representaciones bidireccionales de artefacto para MAR en CBCT dental

- **DOI / URL:** 10.1088/1361-6560/ad3c0a (https://doi.org/10.1088/1361-6560/ad3c0a), segun refs/raw/song2024bmar.bib
- **Nivel de lectura:** 3 (contexto) — PROPUESTO por Claude
- **Leido a fondo por la autora:** no
- **PDF:** NO DISPONIBLE (no existe papers/song2024bmar.pdf)

## Que hace (3 lineas maximo)
Propone b-MAR: un codificador extrae representaciones multiescala del artefacto metalico y las inyecta en un eliminador (supervisado) y un generador de artefactos (adversarial), con una "artifact consistency loss" entre ambos. Se valida en CBCT dental con datos simulados y clinicos.

## Restriccion o supuesto clave
No es sintesis generativa de implantes, pero incluye un generador de artefactos. Supuestos visibles solo desde el abstract:
- Dominio restringido a CBCT dental: "metal artifacts caused by various dental implants" (abstract). La transferencia a CT pelvica con tornillos/placas es NO ENCONTRADO EN EL ABSTRACT.
- El generador aprende artefactos "in an adversarial manner" (abstract) a partir de imagenes ya afectadas; no se declara modelo fisico. Detalle del condicionamiento geometrico del metal: NO ENCONTRADO EN EL ABSTRACT.
- Metricas cuantitativas solo en simulacion: "Quantitative metrics are calculated to evaluate the results of the simulation tests" (abstract). Como se evaluo lo clinico: NO ENCONTRADO EN EL ABSTRACT.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Ninguna cifra citada por ahora | — | — |

## Donde entra en mi tesis
Contexto de MAR con generacion de artefactos aprendida (Estado del arte). wang2025adaptiveweighting lo cita (ref. 55) como origen de una escala de calificacion humana de 5 niveles; el abstract NO la menciona (ni observadores ni lectores). Esa escala es NO ENCONTRADO EN EL ABSTRACT: para usarla como validacion ordinal del realismo del artefacto sintetico hace falta el PDF.

## Dudas para el asesor
- Conviene conseguir el PDF para verificar si la escala de 5 niveles que atribuye wang2025adaptiveweighting esta realmente en este paper, y con que definicion de niveles, numero de lectores y cegamiento?
- Una escala de calidad de reduccion de artefacto (MAR) sirve para evaluar el realismo de un artefacto sintetizado, o mide otra cosa?

## Evidencia textual
Fuente unica: campo abstract de refs/raw/song2024bmar.bib. Ninguna cifra del cuerpo.

| Elemento | Frase original (max. 15 palabras) | Ubicacion |
|---|---|---|
| Dominio / modalidad | "dental cone-beam computed tomography (Dental CBCT) images are seriously contaminated by metal artifacts" | abstract |
| Causa declarada del artefacto | "widespread use of low tube voltages and the presence of various high-attenuation materials" | abstract |
| Critica a metodos previos | "while ignoring the modeling of the metal artifact generation process" | abstract |
| Codificador | "efficient artifact encoder to extract multi-scale representations of metal artifacts" | abstract |
| Eliminador (criterio de entrenamiento) | "The artifact eliminator learns artifact removal in a supervised manner" | abstract |
| Generador (criterio de entrenamiento) | "the artifact generator learns artifact generation in an adversarial manner" | abstract |
| Perdida propia | "we propose artifact consistency loss to align the consistency of images" | abstract |
| Datos | "experiments are conducted on simulated and clinical datasets containing various dental metal morphologies" | abstract |
| Criterio de evaluacion (alcance) | "Quantitative metrics are calculated to evaluate the results of the simulation tests" | abstract |
| PSNR | "b-MAR improvements of >1.4131 dB in PSNR" | abstract |
| RMSE | ">0.3473 HU decrements in RMSE" | abstract |
| SSIM | ">0.0025 promotion in structural similarity index measurement" | abstract |
| Referencia de comparacion | "over the current state-of-the-art MAR methods" | abstract |
| Evaluacion por observadores / escala de 5 niveles | NO ENCONTRADO EN EL ABSTRACT | — |
| Numero de volumenes, pacientes o cortes | NO ENCONTRADO EN EL ABSTRACT | — |
| Metodo de simulacion de artefactos | NO ENCONTRADO EN EL ABSTRACT | — |
| Metodos comparados (nombres) | NO ENCONTRADO EN EL ABSTRACT | — |
| Evaluacion del subconjunto clinico | NO ENCONTRADO EN EL ABSTRACT | — |
