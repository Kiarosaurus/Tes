# selles2022mar — Metal Artifact Reduction in CT after Sacroiliac Joint Fusion

- **DOI / URL:** https://doi.org/10.1016/j.ejrad.2022.110159 (`refs/raw/selles2022mar.nbib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/selles2022mar.pdf (14 páginas; reimpresión como capítulo, artículo pp. 63–74 y dos páginas suplementarias)

## Que hace (3 lineas maximo)
Compara reconstrucciones pareadas con y sin O-MAR de 36 pacientes, adquiridas dentro de 24 h de una fusión sacroilíaca con implantes triangulares de titanio. Dos radiólogos puntúan calidad global, cinco criterios de seguimiento y delineación de cuatro estructuras con una escala ordinal 0–5.

## Restriccion o supuesto clave
Evalúa **reducción** de artefacto con el O-MAR comercial de Philips, no síntesis ni inserción de metal. Es una cohorte consecutiva de un centro, un escáner, un sistema de implante y solo dos lectores; no estudia tejido blando, y el acuerdo entre lectores es moderado. Los autores atribuyen el peor resultado a “secondary artifacts which caused a loss of contrast between cortical bone and surrounding structures” (Discusión, p. 68; PDF p. 8), pero no cuantifican su extensión o amplitud. Distancia al implante, perfiles radiales, HU, RMSE, SSIM, umbrales físicos, `B_delta` y una referencia limpia son **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Cohorte: 36 pacientes | “Thirty-six patients were included” | Métodos—Adquisición, p. 64 (PDF p. 4) |
| Escala ordinal de seis puntos, 0–5 | “A six-point ordinal scale was used” | Métodos—Scoring, p. 65 (PDF p. 5) |
| Calidad global, lector 1: 3 (IQR 3–4) sin O-MAR vs 2 (2–3) con O-MAR | “3 (3-4) 2 (2-3) <0.001” | Tabla 3, p. 68 (PDF p. 8) |
| Delineación del sacro: peor con O-MAR para ambos lectores, `p < 0.001` | “significantly higher for the images without O-MAR” | Resultados, p. 66 (PDF p. 6) |
| Acuerdo interlector: ICC 0.562 | “The ICC between the two radiologists was 0.562” | Resultados, p. 66 (PDF p. 6) |

## Donde entra en mi tesis
Es evidencia clínica en la anatomía más cercana de que reducir streaking no garantiza mejor utilidad visual: la Fig. 1 muestra menos streaks con O-MAR, pero pérdida de visibilidad de la articulación y de contraste cortical (p. 67; PDF p. 7). Esto es relevante para interpretar conjuntamente **streak amplitude** y **bone integrity** en E-A1/E-A2, y para que E-A4 compruebe por separado delineación cortical y daño/artefactos secundarios. No aporta una métrica cuantitativa nueva ni un umbral directamente aplicable; su escala 0–5 podría inspirar el QC ordinal, pero adoptar sus criterios o lectores requeriría una decisión de diseño.

No aporta nada operativo a E-A3: no mide preservación fuera de `G` ni RMSE/SSIM. Tampoco calibra `B_delta`: no define ROI por distancia, no publica milímetros y los artefactos secundarios provienen del algoritmo O-MAR, no de una medición espacial del artefacto metálico nativo. O-MAR no es baseline válido para la síntesis de la tesis, porque resuelve la tarea inversa. Al carecer de referencia limpia, tampoco resuelve #73. El ICC moderado y las discrepancias de significancia entre lectores advierten que una revisión por una sola autora es QC descriptivo, no validación clínica reproducible.

## Dudas para el asesor
- ¿Preespecificar en E-A4 dos ítems separados —streaking y delineación/contraste cortical— para que una mejora del primero no oculte daño secundario?
- ¿Mantener el QC por la autora como descriptivo o incorporar un segundo lector y reportar acuerdo si se adopta una escala ordinal?
- ¿Citar este estudio junto con `selles2023ai` solo para la anatomía y los riesgos, declarando que ninguno proporciona distancia para `B_delta`?
