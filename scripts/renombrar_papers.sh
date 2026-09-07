#!/usr/bin/env bash
# renombrar_papers.sh
# papers/"Autor - Titulo.pdf"  ->  papers/<clave-bibtex>.pdf
#
# Generado por Claude a partir del listado real de papers/ y de refs.bib.
# NO se ejecuto nada. Revisar antes de correr.
# Emparejamiento por apellido + titulo. Sin acceso a internet, sin abrir los PDFs.
# Los nombres de archivo difieren un poco del titulo en refs.bib porque el sistema
# de archivos no admite ':'. Confirmado por la autora el 2026-09-06.
#
# Uso:      bash scripts/renombrar_papers.sh
# Dry-run:  DRY=1 bash scripts/renombrar_papers.sh
#
# mv -n = no sobrescribe si el destino ya existe.

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

MV=(mv -n --)
[ "${DRY:-0}" = "1" ] && MV=(echo mv -n --)

# ======================================================================
# EMPAREJADOS  (25 de 25 PDFs en papers/)
# ======================================================================

# original: Arand - 3D statistical model of the pelvic ring   a CT‐based statistical evaluation of.pdf
"${MV[@]}" 'papers/Arand - 3D statistical model of the pelvic ring   a CT‐based statistical evaluation of.pdf' 'papers/arand2019pelvicring.pdf'

# original: Chen - Towards Generalizable Tumor Synthesis.pdf
"${MV[@]}" 'papers/Chen - Towards Generalizable Tumor Synthesis.pdf' 'papers/chen2024tumorsynthesis.pdf'

# original: De Man - CATSIM. a new Computer Assisted Tomography SIMulation.pdf
"${MV[@]}" 'papers/De Man - CATSIM. a new Computer Assisted Tomography SIMulation.pdf' 'papers/deman2007catsim.pdf'

# original: Haneda - AAPM CT metal artifact reduction grand challenge-1.pdf
"${MV[@]}" 'papers/Haneda - AAPM CT metal artifact reduction grand challenge-1.pdf' 'papers/haneda2025aapm.pdf'

# original: Jacob - LGESynthNet. Controlled Scar Synthesis for Improved Scar Segmentation in Cardiac LGE-MRI Imaging.pdf
"${MV[@]}" 'papers/Jacob - LGESynthNet. Controlled Scar Synthesis for Improved Scar Segmentation in Cardiac LGE-MRI Imaging.pdf' 'papers/jacob2026lgesynthnet.pdf'

# original: Karageorgos - A denoising diffusion probabilistic model for metal artifact reduction in CT.pdf
"${MV[@]}" 'papers/Karageorgos - A denoising diffusion probabilistic model for metal artifact reduction in CT.pdf' 'papers/karageorgos2024ddpm.pdf'

# original: Kazerouni - Diffusion Models for Medical Image Analysis. A Comprehensive Survey.pdf
"${MV[@]}" 'papers/Kazerouni - Diffusion Models for Medical Image Analysis. A Comprehensive Survey.pdf' 'papers/kazerouni2023diffusionsurvey.pdf'

# original: Liu - An End-to-End Geometry-Based Pipeline for Automatic Preoperative Surgical Planning of Pelvic Fracture Reduction and Fixation.pdf
"${MV[@]}" 'papers/Liu - An End-to-End Geometry-Based Pipeline for Automatic Preoperative Surgical Planning of Pelvic Fracture Reduction and Fixation.pdf' 'papers/liu2025pipeline.pdf'

# original: Liu - Deep learning to segment pelvic bones. large-scale CT datasets and baseline models.pdf
"${MV[@]}" 'papers/Liu - Deep learning to segment pelvic bones. large-scale CT datasets and baseline models.pdf' 'papers/liu2021ctpelvic1k.pdf'

# original: Peters - A hybrid training database and evaluation benchmark for assessing metal artifact.pdf
"${MV[@]}" 'papers/Peters - A hybrid training database and evaluation benchmark for assessing metal artifact.pdf' 'papers/peters2025hybrid.pdf'

# original: Ramadanov - Ramadanov–Zabler Safe Zone for Sacroiliac Screw Placement A CT-Based Computational Pilot Study.pdf
"${MV[@]}" 'papers/Ramadanov - Ramadanov–Zabler Safe Zone for Sacroiliac Screw Placement A CT-Based Computational Pilot Study.pdf' 'papers/ramadanov2025safezone.pdf'

# original: Ramzan - CLAIM. Clinically-Guided LGE Augmentation for Realistic and Diverse Myocardial Scar Synthesis and Segmentation.pdf
"${MV[@]}" 'papers/Ramzan - CLAIM. Clinically-Guided LGE Augmentation for Realistic and Diverse Myocardial Scar Synthesis and Segmentation.pdf' 'papers/ramzan2026claim.pdf'

# original: Ren - Framework of metal insertion in the projection domain for image quality optimization in interventional computed tomography.pdf
"${MV[@]}" 'papers/Ren - Framework of metal insertion in the projection domain for image quality optimization in interventional computed tomography.pdf' 'papers/ren2022metalinsertion.pdf'

# original: Rombach - High-Resolution Image Synthesis with Latent Diffusion Models..pdf
"${MV[@]}" 'papers/Rombach - High-Resolution Image Synthesis with Latent Diffusion Models..pdf' 'papers/rombach2022latentdiffusion.pdf'

# original: Selles - Advances in metal artifact reduction in CT images. A review of traditional and novel metal artifact reduction techniques.pdf
"${MV[@]}" 'papers/Selles - Advances in metal artifact reduction in CT images. A review of traditional and novel metal artifact reduction techniques.pdf' 'papers/selles2024marreview.pdf'

# original: Singhrao - End‐to‐end validation of fiducial tracking accuracy in robotic radiosurgery using.pdf
"${MV[@]}" 'papers/Singhrao - End‐to‐end validation of fiducial tracking accuracy in robotic radiosurgery using.pdf' 'papers/singhrao2024fiducial.pdf'

# original: Smith - An evaluation of image-guided technologies in the placement of percutaneous iliosacral screws.pdf
"${MV[@]}" 'papers/Smith - An evaluation of image-guided technologies in the placement of percutaneous iliosacral screws.pdf' 'papers/smith2006iliosacral.pdf'

# original: van Bosse - Pelvic Positioning Creates Error in CT Acetabular Measurements.pdf
"${MV[@]}" 'papers/van Bosse - Pelvic Positioning Creates Error in CT Acetabular Measurements.pdf' 'papers/vanbosse2011pelvicpositioning.pdf'

# original: Wang - Deep Learning Based Metal Artifacts Reduction in Post-operative Cochlear Implant CT Imaging.pdf
"${MV[@]}" 'papers/Wang - Deep Learning Based Metal Artifacts Reduction in Post-operative Cochlear Implant CT Imaging.pdf' 'papers/wang2019cochlear.pdf'

# original: Wu - XCIST-an open access x-ray CT simulation toolkit.pdf
"${MV[@]}" 'papers/Wu - XCIST-an open access x-ray CT simulation toolkit.pdf' 'papers/wu2022xcist.pdf'

# original: Xie - Metal implant segmentation in CT images based on diffusion model.pdf
"${MV[@]}" 'papers/Xie - Metal implant segmentation in CT images based on diffusion model.pdf' 'papers/xie2024implantsegmentation.pdf'

# original: Yun - A strategy for simulation‐driven CT metal artifact reduction toward improving network.pdf
"${MV[@]}" 'papers/Yun - A strategy for simulation‐driven CT metal artifact reduction toward improving network.pdf' 'papers/yun2026simulationdriven.pdf'

# original: Zhang - Adding Conditional Control to Text-to-Image Diffusion Models.pdf
"${MV[@]}" 'papers/Zhang - Adding Conditional Control to Text-to-Image Diffusion Models.pdf' 'papers/zhang2023controlnet.pdf'

# original: Zhang - DiffBoost. Enhancing Medical Image Segmentation via Text-Guided Diffusion Model.pdf
"${MV[@]}" 'papers/Zhang - DiffBoost. Enhancing Medical Image Segmentation via Text-Guided Diffusion Model.pdf' 'papers/zhang2025diffboost.pdf'

# original: Zwingmann - Computer-navigated Iliosacral Screw Insertion Reduces Malposition Rate and Radiation Exposure.pdf
"${MV[@]}" 'papers/Zwingmann - Computer-navigated Iliosacral Screw Insertion Reduces Malposition Rate and Radiation Exposure.pdf' 'papers/zwingmann2009navigated.pdf'


# ======================================================================
# SIN EMPAREJAR
# ======================================================================
# Nada de aqui se renombra. Decide tu y descomenta si corresponde.

# (ninguno)

# ======================================================================
# ENTRADAS DE refs.bib SIN PDF EN papers/
# ======================================================================
#   wang2025adaptiveweighting
#     Adaptive Weighting Based Metal Artifact Reduction in CT Images
#   zhang2026pediclescrew
#     Enhancing Intraoperative Pedicle Screw Planning Accuracy via
#     Diffusion-Based Synthetic CT
#   No hay nada que renombrar para estas dos: faltan los PDFs.
