# zhang2025lefusion — LeFusion: Controllable Pathology Synthesis via Lesion-Focused Diffusion Models

- **DOI / URL:** https://proceedings.iclr.cc/paper_files/paper/2025/file/233d16f17f809981763db2f01b7f9603-Paper-Conference.pdf (`refs/raw/zhang2025lefusion.bib`)
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/zhang2025lefusion.pdf (ICLR 2025; 22 páginas, incluidos apéndices)

## Que hace (3 lineas maximo)
Propone difusión 3D focalizada en lesiones: calcula la pérdida solo en la lesión y combina foreground generado con background real difundido. Evalúa nódulos pulmonares en CT y lesiones cardíacas en RM, con control de textura y difusión de máscaras.

## Restriccion o supuesto clave
Asume que el contenido a generar es una lesión blanda localizada cuya máscara y contexto sano están disponibles. Metal, implantes, pelvis, HU extremos, beam hardening y streaking fuera de la máscara son **NO ENCONTRADO EN EL PDF**. Para esta tesis, el soporte debe extenderse a `G = M ∪ B_delta`; usar solo la máscara rígida del implante impediría modelar precisamente el artefacto exterior.

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| ROI de pulmón 64 × 64 × 32 | "fixed size of 64 × 64 × 32" | Apéndice F, p. 22 |
| 808 casos de entrenamiento LIDC | "an 808-case training set" | Sec. 4.1, p. 6 |
| 300 pasos de difusión | "all diffusion models were set to 300 timesteps" | Apéndice F, p. 22 |

## Donde entra en mi tesis
Precedente funcional directo para inpainting local con U-Net: la lesión se predice *"using a 3D U-Net"* (Sec. 3.1, p. 4), la pérdida se calcula *"exclusively within the lesion region"* (Sec. 3.1, p. 5), y fuera de la máscara el resultado es *"replaced by the real noised background"* (Sec. 3.1, p. 5). La Ec. 3 recompone foreground y background en cada paso; a `t=0`, el exterior procede del original. Esto respalda focalizar capacidad y copiar el exterior, pero no prueba continuidad en el borde de `G`, fidelidad de HU ni física del artefacto metálico. Compara variantes U-shaped/latentes, no U-Net contra DiT; SwinUNETR aparece únicamente como segmentador downstream.

## Dudas para el asesor
- ¿Citar LeFusion para el mecanismo de pérdida enmascarada y copia exterior, declarando que la banda `B_delta` es una adaptación necesaria al artefacto fuera del metal?
- Los resultados downstream de segmentación están fuera del alcance de la tesis; ¿omitirlos por completo del texto principal?
