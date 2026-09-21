# selles2023ai — Is AI the way forward for reducing metal artifacts in CT?

- **DOI / URL:** https://doi.org/10.1016/j.ejrad.2023.110844 (`refs/raw/selles2023ai.bib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/selles2023ai.pdf (9 páginas: portada institucional y artículo de 8 páginas; los materiales suplementarios 1–3 remitidos por el texto no están incluidos)

## Que hace (3 lineas maximo)
Entrena una ResUNet de reducción de artefacto con CT y metal simulados, y la evalúa retrospectivamente contra O-MAR y CT sin corregir. La evaluación usa CT preoperatoria y postoperatoria registrada de pacientes con implantes de fusión sacroilíaca.

## Restriccion o supuesto clave
Es **remoción** de artefacto, no síntesis. El entrenamiento es 2D y los autores reconocen que “not all relevant physical effects are included” (Introducción, p. 2 del artículo; p. 3 del PDF). La evaluación clínica incluye solo 25 pacientes, implantes sacroilíacos y equipos Philips; además, las adquisiciones preoperatorias y postoperatorias difieren en kVp. No mide distancia al implante ni un perfil radial del streaking, por lo que no calibra `B_delta` ni autoriza 12 mm.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Entrenamiento: 461 pacientes y 105 163 cortes axiales | “461 patients and 105,163 axial CT-images” | Sec. 2.1, p. 2 del artículo (p. 3 del PDF) |
| Banco de 35 máscaras de implante | “manual segmentations of 35 implants” | Sec. 2.1, p. 2 del artículo (p. 3 del PDF) |
| Evaluación clínica: 25 pacientes | “twenty-five consecutive patients” | Sec. 2.3, p. 2 del artículo (p. 3 del PDF) |
| Seis ROI por paciente | “six regions of interest (ROI)” | Sec. 2.3, p. 3 del artículo (p. 4 del PDF) |

## Donde entra en mi tesis
Es evidencia anatómicamente cercana para motivar generación fuera de la máscara metálica: describe “dark and bright streaks throughout the images” (Introducción, p. 2 del artículo) y cuantifica diferencias de HU en hueso trabecular, glúteo medio e ilíaco tanto cerca del implante como en el lado contralateral. Esto respalda que `M` sola es insuficiente como soporte del artefacto y que debe evaluarse preservación lejos del implante.

La inferencia para la tesis debe limitarse: los ROI no tienen distancias publicadas y no forman un muestreo espacial continuo. El paper, por tanto, **no** demuestra que `B_delta ≈ 12 mm` contenga el artefacto ni que el artefacto sea exclusivamente periimplante. Su simulación polienergética con agua, hueso, hierro y ruido es un precedente de pares sintéticos para MAR; no valida el problema inverso de insertar metal y artefacto en CT limpia. La ResUNet y la codificación de tres canales por ventanas son contexto, no la arquitectura ni el objetivo generativo de esta tesis.

## Dudas para el asesor
- ¿Citarlo solo para demostrar alteraciones de HU fuera del metal, declarando que no proporciona una distancia para elegir `B_delta`?
- ¿Conviene mencionar que el efecto contralateral obliga a tratar el streaking lejano como limitación del renderizador local?

