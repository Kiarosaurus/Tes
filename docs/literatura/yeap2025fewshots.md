# yeap2025fewshots — Few-shot CBCT-based Synthetic CT Generation with DDPM

- **DOI / URL:** https://doi.org/10.1002/mp.70126 (`refs/raw/yeap2025fewshots.bibtex`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/yeap2025fewshots.pdf (Medical Physics 52(11), e70126; 15 páginas)

## Que hace (3 lineas maximo)
Genera CT sintético 2D desde CBCT con un DDPM condicionado por concatenación de canales y por una versión ruidosa del CBCT. Entrena con pocos pacientes, valida externamente en cabeza-cuello y pelvis y estudia sensibilidad al tamaño del conjunto.

## Restriccion o supuesto clave
Traduce CBCT a CT y busca **reducir** artefactos; no inserta implantes ni sintetiza artefacto metálico. El entrenamiento primario seleccionó casos con *"minimal metal artifacts in the pCTs"* (Sec. 2.1, p. 3). En pelvis externa sí aparecen implantes femorales, pero la supresión produjo una falla anatómica: *"over-correction, resulting in the absence of the left femoral head"* (Sec. 3.5, p. 11). No garantiza identidad fuera de máscara y no compara U-Net con DiT.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 25 pacientes de entrenamiento primario | "trained on 25 patients" | Abstract, p. 1 |
| Pelvis a 512 × 512 | "512 × 512 pixels for pelvis" | Sec. 2.1, p. 3 |
| 27 pacientes para entrenamiento SynthRAD | "27 patients (nine from each center)" | Sec. 2.1, p. 3 |
| Pelvis: MAE 44 ± 9 HU | "masked MAE 44 ± 9 HU" | Abstract, p. 1 |

## Donde entra en mi tesis
Es la evidencia médica más próxima para viabilidad de U-Net + CT + pocos pacientes. Usa *"a 2D U-Net architecture"* con seis bloques de bajada y subida, dos capas ResNet por bloque y atención espacial en una escala (Sec. 2.2, p. 4). El condicionamiento se implementa porque *"The guiding CBCT image y was concatenated with the noisy CT sample"* (Sec. 2.3, p. 5). El reentrenamiento desde cero con 27 pacientes externos y la pelvis a 512 × 512 respaldan factibilidad, no superioridad arquitectónica. La eliminación de una cabeza femoral demuestra que similitud global/MAE y reducción de artefacto no bastan para seguridad anatómica, y limita fuertemente su transferencia a síntesis peri-implante.

## Dudas para el asesor
- ¿Citarlo como precedente de concatenación por canales y viabilidad con pocos pacientes, incluyendo en la misma oración la falla de sobrecorrección?
- ¿Evitar la cifra de MAE pélvico en la defensa de síntesis de metal, dado que el objetivo del paper es retirar artefacto y no generarlo?
