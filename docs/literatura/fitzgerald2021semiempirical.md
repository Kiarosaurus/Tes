# fitzgerald2021semiempirical — Estimacion parametrizada del espectro de rayos X

- **DOI / URL:** 10.1002/mp.14715; https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.14715
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/fitzgerald2021semiempirical.pdf

Profundidad: PDF completo del manuscrito de autor (29 paginas, incluidas tablas y figuras).

## Que hace (3 lineas maximo)

Construye espectros de tubo de tungsteno para TC mediante inicializacion fisica y ajuste a 6144
mediciones de transmision. Parametriza bremsstrahlung y lineas caracteristicas, y entrega espectros
interpolables para XCIST entre 80–140 kVp y angulos de salida de 5–9 grados.

## Restriccion o supuesto clave

Solo estima la forma espectral relativa: "does not include a calibration of the total number of
photons" (Discussion, PDF p. 14). Los autores desaconsejan extrapolar fuera de 80–140 kVp o
5–9 grados. El titanio se usa como atenuador de calibracion, no como implante simulado ni para
validar artefactos metalicos.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 80–140 kVp | "tube voltages in the range of 80 kVp through 140 kVp" | Abstract, PDF p. 1 |
| 5–9 grados | "takeoff angles in the range of 5 degrees to 9 degrees" | Abstract, PDF p. 1 |
| 6144 mediciones | "a total of 6,144 unique measurements were made" | Abstract, PDF p. 1 |
| error post-log 0.005–0.032 | "post-log RMS errors ranging from 0.005 to 0.032" | Discussion, PDF p. 13 |

## Donde entra en mi tesis

Marco del baseline fisico XCIST/CatSim: respalda el origen y el rango validado de sus espectros de
rayos X. Puede justificar policromaticidad realista y limites de interpolacion, pero no respalda por
si solo la reproduccion de beam hardening o streaking causados por implantes.

## Dudas para el asesor

1. Si se usa el espectro en un protocolo fisico, registrar que falta calibrar el numero absoluto de
   fotones; la forma espectral no determina por si sola el nivel de ruido.
2. Confirmar si los rangos 80–140 kVp y 5–9 grados se citaran como dominio del modelo, no como
   protocolo especifico de la tesis.

## Evidencia textual

| Item | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Proposito | "produce accurate, well-validated x-ray spectra" | Abstract, PDF p. 1 |
| Parametrizacion | "13 spline knots to represent the bremsstrahlung component" | Abstract, PDF p. 1 |
| Lineas caracteristicas | "4 values to represent characteristic lines" | Abstract, PDF p. 1 |
| Tensiones iniciales | "Initial spectra at 80, 100, 120, and 140 kVp" | Abstract, PDF p. 1 |
| Angulos | "takeoff angles from 5 degrees to 9 degrees" | Abstract, PDF p. 1 |
| Scatter residual | "reducing measurement contamination from scatter to <1%" | Abstract, PDF p. 1 |
| Detector | "covering the entire 64-row detector" | Abstract, PDF p. 1 |
| Mediciones | "a total of 6,144 unique measurements were made" | Abstract, PDF p. 1 |
| Ajuste parametrico | "R2 values of 0.995 and 0.997" | Abstract, PDF p. 1 |
| Rango de transmision | "up to 3.5 orders of magnitude" | Abstract, PDF p. 1 |
| Mejora de ajuste | "improved agreement with measurements by twofold through tenfold" | Abstract, PDF p. 1 |
| Titanio como atenuador | "titanium ... is commonly used for medical implants" | Methods, PDF p. 9 |
| Motivo del titanio | "near the upper limit ... materials found in clinical scans" | Methods, PDF p. 9 |
| Error optimizado | "post-log RMS errors ranging from 0.005 to 0.032" | Discussion, PDF p. 13 |
| Traduccion ilustrativa a HU | "error reduction from 20 HU to 2 HU" | Discussion, PDF p. 13 |
| No extrapolar angulo | "do not recommend extrapolating spectra outside ... 5 degrees to 9 degrees" | Discussion, PDF p. 13 |
| No extrapolar kVp | "do not recommend extrapolating outside ... 80 kVp to 140 kVp" | Discussion, PDF p. 13 |
| Limite de interpolacion kVp | "post-log RMS error was 0.07" | Discussion, PDF p. 13 |
| Limitacion de amplitud | "does not include a calibration of the total number of photons" | Discussion, PDF p. 14 |
| Uso previsto | "appropriate for use in ... XCIST" | Abstract (Conclusion), PDF p. 1 |
| Implante simulado | NO ENCONTRADO EN EL PDF | — |
| Metrica de artefacto metalico | NO ENCONTRADO EN EL PDF | — |
