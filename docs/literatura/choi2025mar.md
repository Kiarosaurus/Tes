# choi2025mar — Conditional Latent Diffusion for Dental CBCT Metal Artifact Reduction

- **DOI / URL:** https://doi.org/10.1002/acm2.70317 (`refs/raw/choi2025mar.nbib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/choi2025mar.pdf (18 páginas)

## Que hace (3 lineas maximo)
Propone LDM-NMAR para reducir artefactos en CBCT dental: un LDM condicionado produce el prior de NMAR, una U-Net segmenta metal y el mismo LDM corrige artefactos secundarios. Evalúa pares de fantoma y una aplicación clínica sin ground truth.

## Restriccion o supuesto clave
Es **remoción** de artefacto dental, no síntesis de implantes. El LDM opera corte por corte y el resultado final depende también de proyecciones, NMAR, segmentación de metal y una segunda corrección; no es el rendimiento del LDM aislado. La validación cuantitativa procede del fantoma, mientras los cinco casos clínicos carecen de referencia. Pelvis exige estudios adicionales: “further studies are required to establish its generality” (Sec. 5.2, p. 13).

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Schedule de entrenamiento de 1000 pasos | “following a noise scheduling protocol of 1000 steps” | Sec. 2.1, p. 6 |
| Muestreo DDIM de 5 pasos | “DDIM step 5 was used” | Sec. 2.1, p. 6 |
| Fantomas: 8 pares train, 2 validación y 2 test | “8 were used for training, 2 for validation and 2 for tests” | Sec. 3.2, p. 8 |
| Evaluación clínica: 5 pacientes sin ground truth | “5 patient data without ground truth were used” | Sec. 3.3, p. 9 |
| RMSE de fantoma: 34.78×10⁻⁴ a 19.30×10⁻⁴ frente a CNNMAR | “from 34.78 × 10−4 to 19.30 × 10−4” | Resumen, p. 1; Tabla 1, p. 10 |

## Donde entra en mi tesis
Es un precedente directo de **difusión latente condicional aplicada a metal en CT**: usa una U-Net como estimador de ruido y “condition image was concatenated to the input” en cada paso (Sec. 2.1, p. 6). También documenta un riesgo central: el LDM aislado suaviza estructura y produce deformaciones por alucinación; NMAR reutiliza la proyección original para mitigarlas (Sec. 5.2, p. 12). Esto justifica evaluar preservación anatómica, no asumirla por arquitectura.

La transferencia es limitada y adversarial para el diseño vigente. Choi transforma CBCT con artefacto en una estimación limpia; la tesis transforma CT limpia más condición geométrica en metal con artefacto. Usa CVQ-VAE, cinco pasos DDIM y un pipeline híbrido analítico; no ControlNet ni dominio de píxeles. Los valores se expresan como coeficientes de atenuación y HU es **NO ENCONTRADO EN EL PDF**. `B_delta`, fusión sacroilíaca y comparación U-Net–DiT también son **NO ENCONTRADO EN EL PDF**. No autoriza a atribuir a un LDM solo los resultados de LDM-NMAR.

## Dudas para el asesor
- ¿Mantenerlo en Related Work como el precedente más próximo por modalidad y condicionamiento, subrayando que resuelve la tarea inversa?
- ¿Usar su ablación de alucinación para motivar controles de preservación, sin importar sus métricas de fantoma como umbrales?

