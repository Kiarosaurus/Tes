# efron1992bootstrap — Bootstrap, remuestreo e intervalos percentiles

- **DOI / URL:** https://doi.org/10.1007/978-1-4612-4380-9_41 (RAW de la reimpresión de Efron); el segundo PDF es un extracto de *An Introduction to the Bootstrap*
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/efron1992bootstrap.pdf; papers/efron1993IC.pdf

## Que hace (3 lineas maximo)
Introduce el bootstrap no paramétrico: formar la distribución empírica, remuestrear $n$ observaciones con reemplazo y aproximar con las réplicas la distribución muestral de un estadístico. El extracto del libro ilustra remuestreo de sujetos por grupo y define el intervalo percentil mediante percentiles de la distribución bootstrap.

## Restriccion o supuesto clave
El bootstrap debe respetar la unidad independiente y la estructura de muestreo. El ejemplo clínico remuestrea sujetos dentro de cada brazo; no respalda remuestrear cortes 2D como si fueran pacientes independientes. El capítulo completo del método percentil no está incluido: solo aparecen su definición en el panorama y un ejemplo introductorio.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| $B=1000$ réplicas en ejemplo clínico | “We repeat this process ... say 1000 times” | Introducción, p. 5 (p. 22 de `efron1993IC.pdf`) |
| IC percentil aproximado de 95 % | “taking the 25th and 975th largest of the 1000 replicates” | Introducción, p. 5 (p. 22 de `efron1993IC.pdf`) |

## Donde entra en mi tesis
Base metodológica para IC bootstrap de métricas: remuestrear pacientes con reemplazo, conservar juntas todas sus observaciones, recalcular la métrica por réplica y tomar percentiles para los límites. Si hay dos grupos, el ejemplo clínico respalda remuestrearlos por separado dentro de cada grupo.

## Dudas para el asesor
- ¿Se preespecificarán $B$, semilla, percentiles y remuestreo estratificado por cohorte?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Problema | Muestra de tamaño $n$ | “a random sample $X=(X_1,X_2,...,X_n)$” | Resumen, p. 1 (p. 2 de `efron1992bootstrap.pdf`) |
| Definicion | Distribución empírica | “putting mass 1/n at each point” | Sec. 2, p. 3 (p. 4 de `efron1992bootstrap.pdf`) |
| Algoritmo | Tamaño de réplica | “draw a random sample of size n” | Sec. 2, p. 3 (p. 4 de `efron1992bootstrap.pdf`) |
| Algoritmo | Con reemplazo | “selected with replacement from the set” | Sec. 2, p. 3 (p. 4 de `efron1992bootstrap.pdf`) |
| Objetivo | Distribución bootstrap | “Approximate the sampling distribution ... by the bootstrap distribution” | Sec. 2, p. 3 (p. 4 de `efron1992bootstrap.pdf`) |
| Diseño clínico | Tamaños de grupos | “strokes subjects ... 119 11037 ... 98 11034” | Introducción, p. 4 (p. 21 de `efron1993IC.pdf`) |
| Remuestreo | Grupo 1 | “draw with replacement a sample of 11037 items” | Introducción, p. 5 (p. 22 de `efron1993IC.pdf`) |
| Remuestreo | Grupo 2 | “a sample of 11034 items from the second population” | Introducción, p. 5 (p. 22 de `efron1993IC.pdf`) |
| Replicas | Cantidad ilustrativa | “say 1000 times, and obtain 1000 bootstrap replicates” | Introducción, p. 5 (p. 22 de `efron1993IC.pdf`) |
| IC | Nivel | “A rough 95% confidence interval” | Introducción, p. 5 (p. 22 de `efron1993IC.pdf`) |
| IC percentil | Índices de orden | “taking the 25th and 975th largest” | Introducción, p. 5 (p. 22 de `efron1993IC.pdf`) |
| Definicion | Método percentil | “uses ... percentiles of the bootstrap distribution to define confidence limits” | Overview, p. 7 (p. 24 de `efron1993IC.pdf`) |
| Algoritmo | Cada réplica tiene $n$ elementos | “Each bootstrap sample has n elements” | Fig. 2.1, p. 13 (p. 30 de `efron1993IC.pdf`) |
| Algoritmo | $B$ para error estándar | “range from 50 to 200 for standard error estimation” | Sec. 2.1, p. 13 (p. 30 de `efron1993IC.pdf`) |
| Unidad | Remuestreo explícito por paciente | NO ENCONTRADO EN EL PDF; el ejemplo dice “subjects” y remuestrea sus resultados | — |
| Limitacion | Reglas completas del capítulo 13 | NO ENCONTRADO EN EL PDF (capítulo no incluido en el extracto) | — |
