# chen2015lesion — Insercion de lesiones en el dominio de proyeccion

- **DOI / URL:** https://doi.org/10.1118/1.4935530 (`refs/raw/chen2015lesion.nbib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/chen2015lesion.pdf (9 paginas)

## Que hace (3 lineas maximo)

Segmenta lesiones reales, las proyecta hacia datos crudos de pacientes y reconstruye las proyecciones modificadas en un escaner comercial. Valida la geometria con un fantoma ACR y ensaya el realismo de seis lesiones hepaticas reinsertadas con lectores cegados.

## Restriccion o supuesto clave

No es sintesis de metal ni un generador aprendido. La proyeccion de la lesion supone que “Only primary beam was considered during the forward projection” (Sec. 2.A, p. 7035 / PDF p. 2), justificado por su tamano limitado; ese supuesto no se transfiere a implantes rigidos de alta atenuacion y sus efectos de scatter, photon starvation o streaking. Ademas necesita proyecciones comerciales decodificadas con asistencia del fabricante y una energia de correccion de beam hardening propietaria, estimada por calibracion. La lesion segmentada ya fue reconstruida una vez, por lo que se vuelve a proyectar con ruido y borde heredados: “the segmented lesion has already been imaged once” (Sec. 4, p. 7039 / PDF p. 6).

Implantes, aleacion metalica, artefacto metalico, mascara `M`, banda `B_delta`, ancho de 12 mm y una region local de generacion: **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Validacion de realismo principal: 6 lesiones hepaticas | “Six liver lesions covering a range of size, boundary type, homogeneity, and contrast” | Sec. 2.C, p. 7036 / PDF p. 3 |
| Lectura cegada: 2 radiologos con mas de 10 anos de experiencia | “both with more than ten years of experience” | Sec. 2.C, p. 7037 / PDF p. 4 |
| La demostracion de 6 lesiones no tiene potencia estadistica suficiente | “small number of lesions does not provide adequate statistical power” | Sec. 2.C, p. 7037 / PDF p. 4 |
| Error de numeros CT del fantoma: dentro de 2 HU | “excellent agreement (within 2 HU) was observed” | Sec. 3.B, p. 7037 / PDF p. 4 |
| Estudio posterior resumido: 49% (25/51) de pares clasificados al reves | “49% (25/51) of lesion pairs were incorrectly classified” | Sec. 4, p. 7040 / PDF p. 7 |

## Donde entra en mi tesis

En antecedentes metodologicos, delimita con precision la diferencia entre insercion en imagen y en proyeccion: al insertar despues de reconstruir, reproducir el efecto de dosis, espesor de corte, kernel e iteracion sobre la apariencia es muy dificil (Introduccion, pp. 7034-7035). Por tanto, no valida el supuesto actual de sintesis local en imagen; sirve para declararlo como una aproximacion empirica que E-A1..E-A4 debe validar, no como equivalente fisico.

Su protocolo de insertar una estructura en otro lugar del mismo paciente y compararla con la original es antecedente directo de E-A1. La lectura cegada en contexto volumetrico y a traves de cortes es reutilizable en E-A4, pero el propio paper advierte que seis pares no permiten inferencia estadistica. Para E-A2, la dependencia de la apariencia con los parametros de reconstruccion favorece comparar el tornillo sintetico contra el brazo fisico adoptado, aunque este trabajo no genera tornillos ni artefactos metalicos. Para E-A3, no autoriza a interpretar la copia exacta fuera de `G` como realismo fisico: su reconstruccion desde proyecciones no impone soporte espacial local.

No fija metricas de bone integrity, metal integrity, streak amplitude, costura en el borde ni SSIM fuera de `G`: E-A1..E-A4 son **NO ENCONTRADO EN EL PDF**. Tampoco justifica `B_delta`; en particular, no mide extension del artefacto fuera del objeto.

## Dudas para el asesor

- ¿Usarlo para presentar E-A1/E-A4 como adaptacion de un protocolo de insercion y lectura cegada, sin trasladar sus resultados de lesion hepatica a metal?
- ¿Declarar que el renderizador en imagen busca realismo condicionado a la reconstruccion observada, no invariancia ni equivalencia con una insercion en proyecciones?
