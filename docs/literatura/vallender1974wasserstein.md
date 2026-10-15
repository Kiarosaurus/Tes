# vallender1974wasserstein — Distancia de Wasserstein en la recta

- **DOI / URL:** https://doi.org/10.1137/1118101 (metadato en `refs/raw/vallender1974wasserstein.bib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/vallender1974wasserstein.pdf

## Que hace (3 lineas maximo)
Define la distancia de Wasserstein como el ínfimo del costo esperado entre acoplamientos. Demuestra que, para distribuciones sobre la recta con distancia euclídea, ese costo es la integral de la diferencia absoluta entre sus funciones de distribución acumulada.

## Restriccion o supuesto clave
La forma cerrada demostrada es unidimensional: el espacio es la recta real con métrica euclídea. El artículo advierte que las fórmulas para espacios métricos finitos arbitrarios son complicadas y dependientes de la métrica; no demuestra que la expresión mediante CDF sea válida para imágenes o vectores multidimensionales.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Forma 1D de $W_1$ | “$R(P,Q)=\int |F(x)-G(x)|\,dx$” | Teorema, p. 784 (p. 1 del PDF) |

## Donde entra en mi tesis
Fundamento de la métrica Wasserstein-1 cuando se aplica a distribuciones escalares: $W_1(P,Q)=\int_{\mathbb R}|F(x)-G(x)|dx$. La cita no justifica aplicar esa forma de CDF directamente a distribuciones multivariadas de imágenes; en ese caso debe especificarse qué variable escalar se compara o emplearse la definición por acoplamientos.

## Dudas para el asesor
- ¿La tesis calculará $W_1$ sobre intensidades/HU escalares o sobre representaciones multivariadas?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Definicion | Distancia por acoplamientos | “inf is taken over all possible pairs of random variables” | Ec. (1), p. 784 (p. 1 del PDF) |
| Dominio | Caso unidimensional | “the case $X=R$ with the usual Euclidean metric” | Antes del teorema, p. 784 (p. 1 del PDF) |
| Formula | Wasserstein-1 en la recta | “$R(P,Q)=\int |F(x)-G(x)|\,dx$” | Teorema, ec. (2), p. 784 (p. 1 del PDF) |
| Definicion | $F$ y $G$ son CDF | “$F$ and $G$ are the distribution functions” | Teorema, p. 784 (p. 1 del PDF) |
| Alcance | Variables no acotadas | “independently of the boundedness or unboundedness of the variables” | Teorema, p. 784 (p. 1 del PDF) |
| Existencia | El ínfimo se alcanza | “we can replace inf by min” | Teorema, p. 784 (p. 1 del PDF) |
| Construccion | Acoplamiento por cuantiles | “We now put $\xi=F^{-1}(\zeta)$, $\eta=G^{-1}(\zeta)$” | Prueba, p. 785 (p. 2 del PDF) |
| Limitacion | Espacio finito arbitrario | “formulae are very clumsy and depend on the metric” | Remark 2, p. 786 (p. 3 del PDF) |
