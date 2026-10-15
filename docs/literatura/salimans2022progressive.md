# salimans2022progressive — Destilación progresiva y parametrización v

- **DOI / URL:** https://arxiv.org/abs/2202.00512
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/salimans2022progressive.pdf

## Que hace (3 lineas maximo)
Propone destilación progresiva para reducir a la mitad, iterativamente, los pasos de un muestreador de difusión determinista. Introduce parametrizaciones estables para pocos pasos, incluida la predicción de velocidad $v$, y las evalúa en CIFAR-10, ImageNet y LSUN.

## Restriccion o supuesto clave
La destilación empareja dos pasos DDIM del docente con uno del estudiante y mantiene igual arquitectura y número de parámetros. La evidencia procede de generación de imágenes naturales; implantes, CT, condicionamiento anatómico y preservación fuera de máscara son **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| $v=\alpha_t\epsilon-\sigma_t x$ | “Predicting $v \equiv \alpha_t\epsilon-\sigma_t x$” | Sec. 4, p. 5 |
| $\hat{x}=\alpha_t z_t-\sigma_t\hat v_\theta(z_t)$ | “which gives $\hat{x}=\alpha_tz_t-\sigma_t\hat v_\theta(z_t)$” | Sec. 4, p. 5 |
| CIFAR-10: FID 3.0 en 4 pasos | “achieving ... a FID of 3.0 on CIFAR-10 in 4 steps” | Resumen, p. 1 |

## Donde entra en mi tesis
Fuente primaria de la parametrización de predicción $v$. Con $z_t=\alpha_t x+\sigma_t\epsilon$, define $v=\alpha_t\epsilon-\sigma_t x$ y recupera la predicción limpia como $\hat{x}=\alpha_t z_t-\sigma_t\hat v_\theta(z_t)$. Esto justifica la fórmula, no una mejora automática en CT pélvica.

## Dudas para el asesor
- ¿La red predice $v$ con la misma convención de $\alpha_t,\sigma_t$ y proceso variance-preserving del artículo?

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Motivacion | Costo de muestreo | “many hundreds or thousands of model evaluations” | Resumen, p. 1 |
| Metodo | Reducción por iteración | “takes half as many sampling steps” | Resumen, p. 1 |
| Resultado | Pasos iniciales | “taking as many as 8192 steps” | Resumen, p. 1 |
| Resultado | Pasos destilados | “down to models taking as few as 4 steps” | Resumen, p. 1 |
| Resultado | FID CIFAR-10 | “a FID of 3.0 on CIFAR-10 in 4 steps” | Resumen, p. 1 |
| Metodo | Emparejamiento docente-estudiante | “single student DDIM step match 2 teacher DDIM steps” | Sec. 3, p. 3 |
| Algoritmo | Mitad de pasos | “$N \leftarrow N/2$ Halve number of sampling steps” | Algoritmo 2, p. 4 |
| Supuesto | Proceso variance-preserving | “assume a standard variance-preserving diffusion process” | Sec. 4, p. 4 |
| Definicion | Relación de varianzas | “$\sigma_t^2=1-\alpha_t^2$” | Sec. 4, p. 4 |
| Escala | Planificador coseno | “$\alpha_t=\cos(0.5\pi t)$” | Sec. 4, p. 4 |
| Definicion | Predicción de velocidad | “Predicting $v \equiv \alpha_t\epsilon-\sigma_t x$” | Sec. 4, p. 5 |
| Formula | Predicción de $x$ desde $v$ | “$\hat{x}=\alpha_tz_t-\sigma_t\hat v_\theta(z_t)$” | Sec. 4, p. 5 |
| Formula | Velocidad angular | “$v_\phi \equiv dz_\phi/d\phi$” | Appendix D, p. 14 |
| Formula | Forma angular de $v$ | “$v_\phi=\cos(\phi)\epsilon-\sin(\phi)x$” | Appendix D, p. 14 |
| Formula | Reconstrucción angular | “$x=\cos(\phi)z-\sin(\phi)v_\phi$” | Appendix D, p. 14 |
| Evaluacion | Semillas de Tabla 1 | “averages over 3 random seeds” | Tabla 1, p. 6 |
| Evaluacion | Variación residual | “results are still ±0.1” | Tabla 1, p. 6 |
| Restriccion | Arquitectura estudiante/docente | “same architecture and number of parameters as the teacher model” | Discussion, p. 9 |
| Dominio | CT o implantes | NO ENCONTRADO EN EL PDF | — |
