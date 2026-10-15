# fisher1935logic — Inferencia exacta condicional en tablas 2×2

- **DOI / URL:** http://www.jstor.org/stable/2342435
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/fisher1935logic.pdf

## Que hace (3 lineas maximo)
Expone la lógica de la inferencia inductiva e ilustra, para una tabla 2×2, una prueba exacta condicional. Condiciona en los márgenes, enumera las tablas compatibles mediante una distribución hipergeométrica y suma resultados al menos tan discrepantes como el observado.

## Restriccion o supuesto clave
El ejemplo fija los márgenes como información ancilar y calcula una cola en la dirección observada. Una regla explícita para una prueba exacta bilateral 2×2 —incluida la definición de “tan extrema” en ambas colas— es **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Tabla 2×2 del ejemplo: 10/3 y 2/15 | “Monozygotic 10 3 ... Dizygotic 2 15” | Example 1, p. 48 (p. 11 del PDF) |
| $p=3095/6653325$ | “3,095 trials out of 6,653,325” | Example 1, p. 50 (p. 13 del PDF) |

## Donde entra en mi tesis
Respalda una prueba exacta para comparar proporciones en una tabla 2×2 cuando los conteos son pequeños, condicionando en los márgenes. Para reportarla como bilateral debe citarse o declararse además la convención bilateral usada por el software; este artículo no la especifica.

## Dudas para el asesor
- ¿Se documentará la definición bilateral del paquete estadístico y su tratamiento de tablas con probabilidad igual?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Dominio | Tabla 2×2 | “the well-worn topic of the 2 X 2 table” | Example 1, p. 48 (p. 11 del PDF) |
| Datos | Monozygotic | “Out of 13 cases ... in 10 cases also a criminal” | Example 1, p. 48 (p. 11 del PDF) |
| Datos | Dizygotic | “only 2 convicts out of 17” | Example 1, p. 48 (p. 11 del PDF) |
| Condicionamiento | Márgenes | “leaving only the marginal frequencies” | Example 1, p. 48 (p. 11 del PDF) |
| Espacio muestral | Márgenes fijos | “subject to these marginal frequencies” | Example 1, p. 49 (p. 12 del PDF) |
| Distribucion | 13 tablas posibles | “13 possible values from 0 to 12” | Example 1, p. 49 (p. 12 del PDF) |
| Criterio | Al menos tan discrepante | “a discrepancy ... as great or greater than that observed” | Example 1, p. 50 (p. 13 del PDF) |
| Resultado | Conteo exacto | “exactly 3,095 trials out of 6,653,325” | Example 1, p. 50 (p. 13 del PDF) |
| Resultado | Aproximación verbal | “approximately once in 2,150 trials” | Example 1, p. 50 (p. 13 del PDF) |
| Definicion | Exactitud en muestras pequeñas | “direct, and exact for small samples” | Example 1, p. 50 (p. 13 del PDF) |
| Umbral | Nivel 1 % | “reaches 1 per cent” | Example 1, p. 50 (p. 13 del PDF) |
| Umbral | Nivel 5 % | “rises to 5 per cent” | Example 1, p. 50 (p. 13 del PDF) |
| Alcance | Prueba bilateral 2×2 explícita | NO ENCONTRADO EN EL PDF | — |
