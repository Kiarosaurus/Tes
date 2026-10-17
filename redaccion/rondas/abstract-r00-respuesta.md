# abstract-r00 — respuesta del redactor

Modo: redactar (desde plantilla lorem ipsum). Pedido de la autora: DEC 2026-10-16 (7).
Fuente unica: `overleaf/secciones/resumen.tex` (r01). Criterio: P-R4 (traduccion fiel), P-R2 (sin citas ni siglas).
No se agrego ni quito contenido; las cifras se copian del resumen, con punto decimal.

## Correspondencia oracion a oracion

| # | Resumen (r01) | Abstract (r00) |
|---|---|---|
| 1.1 | Los artefactos de los implantes metalicos pueden ocultar los limites del hueso en la tomografia computarizada pelvica, y la escasez ... motiva sintetizar el implante y su artefacto como aumento de datos. | Artifacts from metallic implants can obscure bone boundaries in pelvic computed tomography, and the scarcity ... motivates synthesizing the implant and its artifact as data augmentation. |
| 1.2 | Medir la utilidad de ese aumento presupone que lo sintetizado sea plausible, y ninguno de los enfoques revisados produce a la vez una distribucion de poses ... y la apariencia de su artefacto. | Measuring the usefulness of that augmentation presupposes that what is synthesized is plausible, and none of the reviewed approaches produces both a distribution of implant poses and the appearance of its artifact. |
| 1.3 | Este trabajo propuso una cadena de sintesis que inserta un tornillo transiliaco-transsacro ... en tomografias pelvicas sin implante del conjunto publico CTPelvic1K, y evaluo la coherencia quirurgica y fisica ... | This work proposed a synthesis pipeline that inserts a transiliac-transsacral screw ... into implant-free pelvic computed tomography scans from the public CTPelvic1K dataset, and evaluated the surgical and physical coherence ... |
| 2.1 | Una compuerta previa, con criterio fijado de antemano, examino si el autoencoder ... conserva los valores oseos con error absoluto medio menor que 25 unidades Hounsfield. | A preliminary gate, with a criterion fixed in advance, examined whether the autoencoder ... preserves bone values with a mean absolute error below 25 Hounsfield units. |
| 2.2 | Un muestreador de colocacion propone poses tridimensionales ... y la admisibilidad quirurgica de la colocacion, propuesta aqui, califica cada pose por viabilidad del corredor y grado de brecha cortical, segun cuanto sobresale del hueso. | A placement sampler proposes three-dimensional screw poses ..., and surgical admissibility of placement, proposed here, rates each pose by corridor viability and cortical breach grade, according to how far the screw protrudes from the bone. |
| 2.3 | El sintetizador usa un modelo de difusion en el dominio de imagen con codificacion multiventana ..., y regenera solo el implante y una banda de unos 12 mm a su alrededor. | The synthesizer uses an image-domain diffusion model with multi-window encoding ..., and regenerates only the implant and a band of about 12 mm around it. |
| 2.4 | La *streak amplitude* ... se comparo por equivalencia con un protocolo publicado de simulacion fisica y, como control, con la insercion por copia y pegado, sin artefacto. | The *streak amplitude* ... was compared for equivalence with a published physics-based simulation protocol and, as a control, with copy-paste insertion, which produces no artifact. |
| 3.1 | La compuerta dio un veredicto negativo ...: ninguna de las seis combinaciones ... bajo de 25 HU en los 34 pacientes de prueba, y la mejor dio 61.72 HU. | The gate returned a negative verdict ...: none of the six configurations evaluated fell below 25 Hounsfield units in the 34 test patients, and the best one gave 61.72 Hounsfield units. |
| 3.2 | La admisibilidad quirurgica paso sus controles, y la distribucion de grados de 3 600 poses en 72 pacientes disto 0.206 grados, en distancia de Wasserstein-1, de una serie clinica con navegacion y 0.230 de otra sin ella. | Surgical admissibility of placement passed its checks, and the grade distribution of 3 600 poses in 72 patients lay 0.206 grades, in Wasserstein-1 distance, from a clinical series with navigation and 0.230 from another without it. |
| 3.3 | Las dos distancias son menores que los 0.395 grados ...; el objetivo no tiene regla de decision, y los intervalos por remuestreo de pacientes no ordenan las series por cercania. | Both distances are smaller than the 0.395 grades ...; the objective has no decision rule, and the patient-level bootstrap intervals do not rank the series by closeness. |
| 3.4 | En 13 pacientes de prueba sin metal, la diferencia media pareada ... con titanio fue de -301.0 HU. | In 13 metal-free test patients, the mean paired difference ... with titanium was -301.0 Hounsfield units. |
| 3.5 | Su intervalo de confianza del 90 %, de -477.0 a -124.9, cruza el limite inferior del margen de equivalencia de 196.3, y el desenlace es no concluyente, con una amplitud del sintetizador menor que la del protocolo. | Its 90 % confidence interval, from -477.0 to -124.9, crosses the lower limit of the equivalence margin of 196.3, and the outcome is inconclusive, with a lower amplitude for the synthesizer than for the protocol. |
| 3.6 | Superar la insercion por copia y pegado, con p = 0.000122 en la prueba de Wilcoxon, es un control de cordura que no cuenta a favor ..., porque esa insercion no produce rayas. | Outperforming copy-paste insertion, with p = 0.000122 in the Wilcoxon test, is a sanity check that does not count in favor ..., because that insertion produces no streaks. |
| 4.1 | Los resultados son acotados: la distribucion de grados queda mas cerca de cada serie clinica que esas series entre si, en una lectura descriptiva, y la equivalencia ... no se establecio. | The results are limited: the grade distribution lies closer to each clinical series than those series lie to each other, in a descriptive reading, and the equivalence ... was not established. |
| 4.2 | El realismo visual del artefacto sintetico no se reclama, porque la autora lo juzgo insuficiente; ella y su asesor decidieron no redisenar el sintetizador, y su salida no reproduce la caida de la amplitud con la distancia al metal. | The visual realism of the synthetic artifact is not claimed, because the author judged it insufficient; she and her advisor decided not to redesign the synthesizer, and its output does not reproduce the decay of the amplitude with distance from the metal. |
| 4.3 | La evaluacion de segmentacion osea quedo fuera de alcance, y ningun resultado ... mide si los implantes sinteticos ayudan a entrenar una red. | Bone segmentation evaluation was left out of scope, and no result of this work measures whether synthetic implants help train a network. |

IMRyC conservado: 3/4/6/3 oraciones, como el resumen.

Palabras clave: Sintesis de imagenes medicas -> Medical image synthesis; Artefacto metalico -> Metal artifact;
Tomografia computarizada pelvica -> Pelvic computed tomography; Modelos de difusion -> Diffusion models;
Fijacion iliosacra -> Iliosacral fixation.

Titulo: el decidido en DEC 2026-10-16 (7) ptos 3 y 6, sin el prefijo MetalSynth-Pelvis; conserva "CT" porque es el titulo decidido tal cual.

## Notas para el orquestador

- **copy-paste vs cut-and-paste.** El encargo listaba "cut-and-paste", pero `tesis/main.tex` no usa ese termino
  (0 apariciones) y si "copy-paste insertion" (2). Se aplico la regla del propio encargo ("toma la de tesis/main.tex
  cuando exista"): *copy-paste insertion*. Si la autora prefiere "cut-and-paste", es un reemplazo en dos lugares.
- "sin artefacto" (2.4) se tradujo "which produces no artifact" para que el atributo quede en la insercion y no en el control.
- "remuestreo de pacientes" (3.3) -> "patient-level bootstrap", termino de `tesis/main.tex` ("patient-level bootstrap 95% CI").
- "3\,600" y "90\,\%" conservan el espacio fino del resumen.
- El resumen no tiene `\REVVISUAL`; el abstract tampoco.
- No se copio el PDF a `redaccion/.build/etapas/` ni se registro en `BITACORA.md` (fuera de los archivos editables del redactor).

## Decisiones de redaccion

- Terminos fijos en ingles para el abstract: placement sampler, surgical admissibility of placement (sin sigla),
  corridor viability, cortical breach grade, osseous corridor, multi-window encoding, image-domain diffusion model,
  physics-based simulation protocol, copy-paste insertion, patient-level bootstrap, sanity check, equivalence margin.
