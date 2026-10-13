# yang2022arcplanning — Canal de fijacion en arco (IAFC) y planificacion automatica para fractura pelvica

> **ALERTA DE CORRESPONDENCIA PDF/RAW.** El PDF en `papers/yang2022arcplanning.pdf` NO es el
> mismo documento que describe `refs/raw/yang2022arcplanning.nbib`.
> - Titulo del PDF: "An Internal Arc Fixation Channel and Automatic Planning Algorithm for
>   Pelvic Fracture" (p. 1). Autores del PDF: Yang, Song, Cheng, Shi, Liang, Wang.
> - Titulo del raw: "Computer-aided automatic planning and biomechanical analysis of a novel
>   arc screw for pelvic fracture internal fixation" (CMPB 220:106810). Autores del raw:
>   Yang, Feng, Song, Cheng, Liang, Wang.
> - El abstract del raw menciona "pelvises of ten adults" y analisis de elementos finitos en
>   tres posturas; el PDF usa cinco pelvis y no contiene analisis biomecanico.
> - El PDF no trae DOI, revista, volumen ni paginas.
> Parece una version previa/manuscrito distinto del articulo publicado. Toda cifra de esta
> ficha sale del PDF y NO debe citarse como si fuera del articulo de CMPB sin verificar.

- **DOI / URL:** NO ENCONTRADO EN EL PDF. (El raw trae 10.1016/j.cmpb.2022.106810, pero
  corresponde al articulo publicado, cuyo titulo y contenido difieren del PDF; ver alerta.)
- **Nivel de lectura:** 2 (metodo). Se mantiene el nivel pedido: lo util es el criterio de
  contencion por erosion 3D y el caso recto (curvatura cero) a traves de S1; las cifras
  (5 pelvis, canales en arco) no son reutilizables como parametros del muestreador.
- **Leido a fondo por la autora:** no
- **PDF:** papers/yang2022arcplanning.pdf

## Que hace (3 lineas maximo)
Planifica automaticamente un canal de fijacion en arco de curvatura constante (IAFC) que
cruza ilion-S1-ilion: genera candidatos por combinacion de puntos derivados de 3 semillas
(entrada, S1 medio, salida) y elige el mejor con un puntaje de distancia a superficie
obtenido por erosion 3D sobre voxeles de 1 mm; compara contra el caso recto (curvatura 0).

## Restriccion o supuesto clave
No es un paper de sintesis generativa; no aplica la pregunta sobre implantes metalicos.
Supuestos relevantes para el muestreador:
- La "seguridad" es solo distancia de la linea central a la superficie osea; no modela
  diametro de tornillo ni estructuras neurovasculares: "calculate the shortest distance from
  the centerline of the IAFC to the pelvis surface" (p. 3).
- Busca un optimo determinista, no una distribucion: "select the safest IAFC" (p. 4).
- Puntos de entrada/salida iniciales elegidos a mano: "requires manual selection of initial
  entry and exit points" (p. 6).
- Pelvis sanas, segmentadas en Mimics, no fracturadas ni con implantes (p. 2).

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
Ninguno por ahora (ver alerta de correspondencia PDF/raw). Candidatos si se resuelve la
alerta:

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| 1 de 5 pelvis sin canal recto viable | "a viable straight path cannot be found on one of the pelvis models" | III.A, p. 5 |
| voxel 1 mm para distancia a superficie | "voxel size of 1mm × 1mm × 1mm" | II.B(2), p. 3 |

## Donde entra en mi tesis
Objetivo 2 (muestreador), solo como **contexto**. No compite con el muestreador:
- Es planificacion de una trayectoria optima unica (y en arco, que no es un tornillo
  iliosacro/transsacro convencional); el muestreador de la tesis no optimiza, muestrea
  malposicion de `zwingmann2009navigated`.
- Aporta precedente de que la contencion cortical de un corredor transsacro por S1 puede
  puntuarse con un mapa de distancia a superficie por erosion morfologica 3D, tomando el
  minimo a lo largo de la trayectoria (CSV = minimo del VDVA, p. 4). Es conceptualmente un
  transformado de distancia; podria citarse como antecedente del chequeo de contencion,
  no como fuente de umbrales.
- Aporta contexto anatomico: en 1 de 5 pelvis no hubo canal recto viable por la posicion de
  S1 (p. 5), consistente con la variabilidad de corredores S1 (refs. [7], [8] del PDF).
- No da diametros de tornillo, margenes en mm, tasas de malposicion ni datos CT reutilizables.

## Dudas para el asesor
- El PDF local no es el articulo de CMPB del raw (titulo, autores, N=5 vs 10, sin FEA).
  Conseguir el PDF publicado o cambiar la clave/raw a la version que se tiene? (Decision de
  la autora; no se modifico `refs/`.)
- Vale la pena citar un trabajo de canales en arco (tecnica no clinica, sin perforacion
  estable segun el propio paper, p. 6) solo por el criterio de distancia por erosion?
- La "zona segura" se apoya en ref. [18] ("the front inner side is the safest", p. 3) sin
  definicion cuantitativa; no sirve como fuente de zonas seguras del muestreador.

## Evidencia textual
| Elemento | Frase original (max. 15 palabras) | Seccion / pagina |
|---|---|---|
| Titulo del PDF | "An Internal Arc Fixation Channel and Automatic Planning Algorithm for Pelvic Fracture" | Titulo, p. 1 |
| Tasa de discapacidad (contexto, citado) | "Pelvis fracture is a serious trauma with disability rate as high as 60%." | I, p. 1 |
| Corredores oseos (definicion, citada) | "intracortical spaces known as osseous fixation paths (OFPs)" | I, p. 1 |
| Datos: numero de pelvis (intro) | "generate and evaluate IAFCs on five real pelvis models against straight channels" | I, p. 2 |
| Datos: origen | "five patients with the intact pelvis from Beijing Jishuitan Hospital" | II.A, p. 2 |
| Preprocesamiento | "threshold segmentation, region growth, open operation, and closed operation" | II.A, p. 2 |
| Software | "The Geomagic studio 12 is used to simplify and smoothen the pelvis model." | II.A, p. 2 |
| Tipo de trayectoria | "aims to generate constant curvature paths that are suitable for this drilling method" | II.B, p. 2 |
| Corredor buscado | "the screw must go through both sides of the pelvis along with the sacrum" | II.B, p. 2 |
| Geometria del arco | "Three points are needed to determine an arc of constant curvature." | II.B(1), p. 3 |
| Semilla media | "A point near S1 on the sagittal plane of the pelvis" | II.B(1), p. 3 |
| Zona segura (citada, cualitativa) | "There are two safe areas ... among which the front inner side is the safest" | II.B(1), p. 3 |
| Filtro de candidatos | "points that fall outside the pelvis model will be removed in the algorithm" | II.B(1), p. 3 |
| Reticula de puntos derivados | "the points derived from the hip bones of the two groups forms a 10 × 10 lattice" | Fig. 2, p. 3 |
| Definicion ingenua de CSV | "calculate the shortest distance from the centerline of the IAFC to the pelvis surface" | II.B(2), p. 3 |
| Resolucion voxel | "voxel size of 1mm × 1mm × 1mm" | II.B(2), p. 3 |
| Paso de erosion | "the pelvis' outermost layer of 1mm thickness is removed" | II.B(2), p. 3 |
| CSV por voxel | "These values are defined as the CSV for each voxel." | II.B(2), p. 3 |
| Definicion VDVA | "we define as voxel distance value array (VDVA)" | II.B(2), p. 4 |
| Ejemplo VDVA | "The VDVA of arc channel in the Fig. 3 is [0,1,1,2,2,2,2,2,1,1,0,0]" | II.B(2), p. 4 |
| CSV de trayectoria | "The CSV of a fixation path is the least value in the corresponding VDVA." | II.B(2), p. 4 |
| Limite de radio | "once it exceeds this radius, the channel will pass through the cortical bone" | II.B(3), p. 4 |
| Criterio 1 | "first find the path with the highest CSV in the set of planned paths" | II.B(3), p. 4 |
| Criterio 2 | "filter the curve with the least number of minimum values in VDVA" | II.B(3), p. 4 |
| Criterio 3 (desempate) | "identify the curve with the maximum average value of VDVA" | II.B(3), p. 4 |
| Canal recto (comparador) | "curvature is limited to zero in curve function of the straight channel generation algorithm" | II.C, p. 5 |
| Resultado: canal recto inviable | "a viable straight path cannot be found on one of the pelvis models" | III.A, p. 5 |
| Causa anatomica | "Because the S1 of the pelvis is higher than the position where the pelvis is easy to fix" | III.A, p. 5 |
| Resultado CSV | "the CSV of IAFC is higher than that of the straight channel" | III.B, p. 5 |
| CSV recto por pelvis (valores) | Solo en grafico Fig. 6 sin tabla; valores numericos: NO ENCONTRADO EN EL PDF | Fig. 6, p. 6 |
| Pelvis 1: largo / curvatura / CSV | Tabla I: "162.82 0.0089 10" | Tabla I, p. 6 |
| Pelvis 2: largo / curvatura / CSV | Tabla I: "146.81 0.0078 10" | Tabla I, p. 6 |
| Pelvis 3: largo / curvatura / CSV | Tabla I: "141.56 0.0053 10" | Tabla I, p. 6 |
| Pelvis 4: largo / curvatura / CSV | Tabla I: "154.86 0.0187 8" | Tabla I, p. 6 |
| Pelvis 5: largo / curvatura / CSV | Tabla I: "150.98 0.0126 11" | Tabla I, p. 6 |
| Unidades de largo | Encabezado "Length(mm)" | Tabla I, p. 6 |
| Unidades de curvatura | NO ENCONTRADO EN EL PDF | Tabla I, p. 6 |
| Unidades de CSV | NO ENCONTRADO EN EL PDF (implicitamente mm por voxel de 1 mm, no declarado en Tabla I) | Tabla I, p. 6 |
| "Statistical results" anunciados | "Table I shows the parameters of IAFC ... and the statistical results" (la tabla no trae estadisticos) | III.C, p. 6 |
| Limitacion: compromiso precision/velocidad | "This approach trades some accuracy of the final safety measure for fast evaluation." | IV, p. 6 |
| Limitacion: perforacion | "The most significant challenge of which is to stably drill curved paths" | IV, p. 6 |
| Limitacion: seleccion manual | "requires manual selection of initial entry and exit points on the pelvis" | IV, p. 6 |
| Diametro de tornillo | NO ENCONTRADO EN EL PDF | — |
| Margen de seguridad en mm / umbral de CSV minimo aceptable | NO ENCONTRADO EN EL PDF | — |
| Separacion de la reticula (mm) y paso de muestreo a lo largo del arco | NO ENCONTRADO EN EL PDF | — |
| Numero de candidatos generados | NO ENCONTRADO EN EL PDF | — |
| Largo/CSV del canal recto optimo por pelvis (tabla) | NO ENCONTRADO EN EL PDF | — |
| Resolucion/espesor de corte CT | NO ENCONTRADO EN EL PDF | — |
| Tasas de malposicion o validacion clinica | NO ENCONTRADO EN EL PDF | — |
| Analisis de elementos finitos / 10 pelvis (presentes en el abstract del raw) | NO ENCONTRADO EN EL PDF | — |
| DOI / revista / volumen | NO ENCONTRADO EN EL PDF | — |
