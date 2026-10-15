# zhang2024catsim — Validacion de resolucion espacial de CatSim

- **DOI / URL:** 10.1088/1361-6560/ad2122; https://doi.org/10.1088/1361-6560/ad2122
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/zhang2024catsim.pdf

Profundidad: PDF completo del manuscrito de autor (30 paginas, incluidas tablas y figuras).

## Que hace (3 lineas maximo)

Evalua la resolucion espacial simulada por CatSim frente a un escaner clinico real de 64 filas en
los dominios de proyeccion e imagen. Introduce un modelo realista del foco y ajusta empiricamente
la respuesta temporal del detector; compara PSF y MTF.

## Restriccion o supuesto clave

La respuesta temporal del detector fue ajustada para concordar con los datos y varios modelos no
dependen de kV ni mA. Los autores reconocen que "CatSim could benefit from more complex,
kV- and mA-dependent models" (Limitations, PDF p. 11). Valida resolucion espacial con alambres,
no artefactos de implantes ni fidelidad de intensidades metalicas.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [x] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| mayoria de errores medios <5% | "most of the average errors substantially less than 5%" | Abstract, PDF p. 1 |
| error PSF de imagen <5% | "Agreement for PSF50_img ... is good (within 5%)" | Results, PDF p. 8 |
| discrepancia MTF local hasta 12% | "disagreement of up to about 12%" | Results, PDF p. 8 |

## Donde entra en mi tesis

Estado de validacion del baseline fisico CatSim/XCIST. Sustenta que la resolucion espacial del
simulador concuerda con un escaner real dentro de limites cuantificados para la configuracion
estudiada. No permite afirmar validacion de artefacto metalico, ruido peri-implante, beam hardening
por metal ni anatomia pelvica.

## Dudas para el asesor

1. Si se cita el error <5%, precisar que corresponde a metricas de resolucion (PSF/MTF), no a una
   metrica global de fidelidad de imagen.
2. La respuesta temporal se ajusto al 90% del valor publicado; decidir si el baseline propio debe
   recalibrarse o declarar que adopta los parametros de XCIST.

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Escaner | "typical 64-detector-row clinical CT scanner" | Abstract, PDF p. 1 |
| Fantomas | "we scanned two phantoms designed to evaluate spatial resolution" | Abstract, PDF p. 1 |
| Modelo de foco | "new, realistic model for the x-ray source focal spot" | Abstract, PDF p. 1 |
| Respuesta temporal | "empirically tuned ... detector temporal response" | Abstract, PDF p. 1 |
| Metricas | "point-spread functions ... modulation transfer functions" | Abstract, PDF p. 1 |
| Error general | "most of the average errors substantially less than 5%" | Abstract, PDF p. 1 |
| Tendencia | "errors tended to increase with decreasing kV" | Abstract, PDF p. 1 |
| Definicion PSF50 | "full width at half maximum ... of the point spread function" | Methods, PDF p. 3 |
| Definicion MTF | "modulation transfer function ... at 50% and 10% modulation" | Methods, PDF p. 3 |
| Umbral del modelo de foco | "pixels ... at 2% of the maximum intensity" | Methods, PDF p. 4 |
| Discretizacion energetica | "we used kV/5 ... energy bins" | Methods, PDF p. 5 |
| Lineas, caso simple | "3x10^13 line integrals" | Methods, PDF p. 5 |
| Tiempo, caso simple | "ran in about 15 minutes" | Methods, PDF p. 5 |
| Lineas, caso complejo | "calculation of 2x10^16 line integrals" | Methods, PDF p. 5 |
| Amplitud PSF de proyeccion | "20% to 30% higher amplitude PSFs" | Results, PDF p. 7 |
| Perturbacion temporal | "primary time constant ... varied by 50%" | Results, PDF p. 7 |
| Efecto temporal | "varied by about 28% at positions S and D" | Results, PDF p. 7 |
| Error medio de proyeccion | "average errors are all within 5%" | Results, PDF p. 8 |
| PSF de imagen | "Agreement for PSF50_img ... is good (within 5%)" | Results, PDF p. 8 |
| Amplitud PSF de imagen | "about 10% higher for the simulated" | Results, PDF p. 8 |
| Desacuerdo MTF local | "disagreement of up to about 12%" | Results, PDF p. 8 |
| Frecuencia del desacuerdo | "at low frequencies (< 5 lp/cm)" | Results, PDF p. 8 |
| Centro del campo | "errors are within +/-5% in the center 25-cm diameter" | Results, PDF p. 9 |
| Ajuste temporal | "adjusted the value of tau1 to 90%" | Discussion, PDF p. 9 |
| Limitacion computacional | "We did not explore sampling strategies" | Discussion, PDF p. 9 |
| Amplitud no explicada | "simulations consistently produce about 20% to 30% higher amplitude" | Discussion, PDF p. 9 |
| Limites de modelos | "kV- and mA-dependent models" | Limitations, PDF p. 11 |
| Alambres excluidos | "exclusion of five of the nineteen wires" | Limitations, PDF p. 11 |
| Alcance validado | "ability to simulate a real scanner's spatial resolution" | Conclusion, PDF p. 11 |
| Implantes metalicos | NO ENCONTRADO EN EL PDF | — |
| Metrica de artefacto metalico | NO ENCONTRADO EN EL PDF | — |
| Validacion en pelvis | NO ENCONTRADO EN EL PDF | — |
