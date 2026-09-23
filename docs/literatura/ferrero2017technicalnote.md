# ferrero2017technicalnote — Lesiones digitales en proyecciones de CT dual-energy

- **DOI / URL:** https://doi.org/10.1002/mp.12185 (`refs/raw/ferrero2017technicalnote.nbib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/ferrero2017technicalnote.pdf (14 paginas; manuscrito aceptado)

## Que hace (3 lineas maximo)

Extiende la insercion de Chen a CT dual-source y dual-energy con un modelo espectral que predice numeros CT desde composicion y densidad conocidas. Lo valida con yodo, calcio, fantoma ACR y calculos renales digitales insertados en proyecciones.

## Restriccion o supuesto clave

El metodo exige composicion quimica, densidad, espectros, respuesta energetica del detector, tamano del paciente y acceso a datos crudos. Declara que el modelo “assumes accurate beam hardening and scatter correction” (Discusion, PDF p. 13) en la reconstruccion del fabricante y que los datos comerciales son “proprietary and therefore difficult to access” (Discusion, PDF p. 13). Aunque admite objetos de composicion arbitraria, solo demuestra minerales de calculos renales; tornillos, placas, aleaciones de osteosintesis y artefactos metalicos pelvicos: **NO ENCONTRADO EN EL PDF**.

No sintetiza una textura local en imagen ni restringe el cambio a una banda. `B_delta`, 12 mm, difusion, U-Net, 2.5D y preservacion exacta fuera de `G`: **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Validacion espectral en fantomas de 24 a 45 cm WED | “phantoms from 24 to 45 cm WED” | Sec. III.A, PDF p. 8 |
| Error de numero CT a 80 kV: -2.2% a 0.1% | “ranged from -2.2 to 0.1%” | Sec. III.A, PDF p. 8 |
| Error de numero CT a 100 kV: -0.5% a 7.5% | “At 100 kV, the percent differences ranged from -0.5 to 7.5%” | Sec. III.A, PDF p. 8 |
| Error residual maximo de CTR: menor de 6% | “largest residual CTR error was well below 6%” | Sec. III.B, PDF p. 9 |
| Diferencia maxima media de numero CT del fantoma: 2 HU | “was 2 HU, as shown in Table 4” | Sec. III.C, PDF p. 9 |

## Donde entra en mi tesis

En antecedentes de fisica e insercion sintetica, demuestra que una apariencia dependiente del paciente y del protocolo puede construirse en proyecciones usando espectro atenuado, respuesta del detector y geometria del escaner. Es un contraste fuerte con la sintesis local en imagen: el renderizador actual no conoce esas variables y debe presentar la fisica como aprendida implicitamente de CT reconstruida, no calculada.

Para E-A2, aporta el principio de evaluar objetos con geometria y composicion conocidas despues de reconstruir, pero no sustituye el brazo fisico de Peters: trabaja con calculos renales, dual-energy, datos propietarios y correcciones del fabricante. Sus errores de CT/CTR miden fidelidad de una tuberia de proyeccion; no son umbrales transferibles para metal pélvico. Para E-A1 no compara implantes reales con reconstrucciones; para E-A4 no realiza lectura humana de realismo. E-A1, E-A3 y E-A4 como bloques del proyecto: **NO ENCONTRADO EN EL PDF**.

El trabajo tampoco respalda una `B_delta` finita. Al reconstruir proyecciones modificadas, no impone que el cambio permanezca cerca del objeto; por ello, la preservacion cero de E-A3 sigue siendo una propiedad de composicion del Diseno A y no evidencia de fidelidad fisica.

## Dudas para el asesor

- ¿Citarlo solo como antecedente de insercion fisicamente condicionada y como limite de la sintesis en imagen, sin convertirlo en baseline?
- ¿Conviene declarar en Metodos que composicion y espectro no son condiciones del renderizador y que esa variabilidad queda absorbida por la distribucion de entrenamiento?
