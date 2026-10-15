# gautier2001accuracy — Precision de la fijacion sacroiliaca con tornillos guiada por computadora (pelvis plasticas, S1 y S2)

- **DOI / URL:** NO ENCONTRADO EN EL PDF (el raw `refs/raw/gautier2001accuracy.nbib` trae `10.1097/00003086-200112000-00036`; el PDF no lo imprime)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/gautier2001accuracy.pdf

Profundidad: texto completo (8 paginas, pp. 310-317, incluye tablas 1-3 y referencias).

**Correspondencia PDF vs raw:** coincide. Titulo "Accuracy of Computer-Guided Screw Fixation of the Sacroiliac Joint"; autores Gautier, Bachler, Heini, Nolte; Clinical Orthopaedics and Related Research, Number 393, pp. 310-317, December 2001 (cabecera p. 310 y p. 311). El raw da `IP - 393`, `PG - 310-7`, `DP - 2001 Dec`. El abstract del raw es identico al del PDF.

## Que hace (3 lineas maximo)
Estudio de laboratorio en 6 pelvis plasticas (AO Synbone): navegacion optoelectronica con registro por surface matching para perforar 24 trayectos iliosacros a S1 y 12 a S2, planificados sobre CT.
Mide el error del registro (8 tornillos de referencia), el error de entrada/objetivo/angulo de cada perforacion contra la CT postoperatoria, y el "stock oseo" restante agrandando virtualmente cada orificio de 8 a 20 mm.
Concluye que no hubo perforaciones cortical/foraminales y que S2 tiene menos margen oseo que S1.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; la pregunta del template no aplica tal cual. Supuestos que limitan su uso en la tesis:
- Modelo **plastico**, no pacientes ni cadaveres: *"The technique was done on six plastic pelves"* (Materials and Methods, p. 311). Sin tejidos blandos, sin fractura desplazada real, sin dismorfismo documentado.
- Exito definido de forma **binaria** (perforacion si/no) y errores **continuos** en mm y grados, no grados ordinales de malposicion: *"was not observed in any of the 36 screw holes"* (Results, p. 314).
- El "stock oseo" es un calculo **virtual** sobre la CT postoperatoria (cilindros concentricos), no una medicion de tornillos reales: *"each hole was enlarged concentrically with an increment in diameter of 2 mm"* (Materials and Methods, p. 313). Nota: el pie de la Fig 6 dice "enlarged eccentrically" (p. 314), contradiccion interna del propio PDF.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Recomendacion 4.5 mm en S2 | "insertion of a 4.5-mm cortical screw is recommended, but only when necessary" | Discussion, p. 317 |
| Mayor riesgo en S2 | "increased risk for screw perforation when screw insertion was done into the S2 vertebra" | Discussion, p. 317 |
| Menos stock oseo en S2 | "the S2 area where less bone stock is present" | Results, p. 315 |
| 2 x 6.5 mm en S1, 1 x 4.5 mm en S2 | "allowing a double 6.5-mm screw insertion in the vertebral body of S1" | Discussion, p. 316 |
| 0 perforaciones / 36 orificios | "not observed in any of the 36 screw holes" | Results, p. 314 |
| Error entrada 2.7 mm, objetivo 3.5 mm, angulo 2.0 grados | "mean translational error of the entry points of 2.7 mm" | Results, p. 314; Table 2, p. 315 |

## Donde entra en mi tesis
- **Muestreador, restriccion de diametro por nivel sacro:** respalda que S2 tiene menos margen oseo que S1 y que el tornillo en S2 fue de 4.5 mm frente a 6.5 mm en S1. Relevante si el muestreador alguna vez se extiende a S2 (hoy muestrea malposicion solo en S1, `docs/00-tesis.md`).
- **No sirve como segunda fuente de distribucion de malposicion** junto a `zwingmann2009navigated`: no hay pacientes, no hay grados ordinales, y la tasa de perforacion observada es 0/36 en plastico. A lo sumo es contraste (precision de laboratorio de la navegacion, error continuo en mm/grados).
- **Banco de geometrias:** solo da diametros (6.5 mm S1, 4.5 mm S2; brocas de 4.5 y 3.5 mm). Largo de tornillo: NO ENCONTRADO EN EL PDF.
- **Cadena de la cifra 2%-15%:** el paper cita otro rango, *"Failure rates from 2% to 13% have been reported"* (introduccion, p. 310), atribuido a sus refs. 10, 19 y 22. Lo cita, no lo mide.

## Dudas para el asesor
1. Moed 2006 parafrasea como *"no larger than 4.5 mm"*. El PDF dice "insertion of a 4.5-mm cortical screw is recommended, but only when necessary from the mechanical point of view" (p. 317). El PDF **no** dice "no larger than": recomienda un tornillo cortical de 4.5 mm en S2 y ademas condiciona el tornillo en S2 a que haga falta mecanicamente. Si la tesis cita una cota maxima de diametro en S2, hay que decidir si se cita a Gautier con su redaccion o se atribuye la parafrasis a Moed.
2. La tabla 3 da, para S2 (n = 12), un volumen fuera de hueso de 6.6% con cilindro de 8 mm frente a 5.1% en S1 (n = 24). Hay que decidir si esa diferencia se usa como respaldo cuantitativo, porque el paper no hace ninguna prueba estadistica de S1 contra S2.
3. Con pelvis plasticas, ¿es aceptable extrapolar a CT clinicas de CTPelvic1K (anatomia con dismorfismo, osteoporosis)?
4. El paper no cita ningun resumen de 1999 de Gautier y Baechler (CAOS Davos). La unica referencia de Bachler en el PDF es Gong J, Bachler R, et al. 1997 (surface matching, ref. 8). No se puede afirmar desde el PDF que sea el mismo trabajo.

## Evidencia textual
| Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Revista, numero, paginas | "Number 393, pp. 310–317" | Cabecera, p. 310 |
| Fecha | "Number 393 December, 2001" | Cabecera, p. 311 |
| DOI | NO ENCONTRADO EN EL PDF | — |
| Financiacion | "The study was supported by an AO/ASIF Research Grant." | Nota de afiliacion, p. 310 |
| Tasas de fallo citadas 2%-13% | "Failure rates from 2% to 13% have been reported." | Introduccion, p. 310 |
| Complicaciones raras | "neurologic or vascular complications are relatively rare" | Introduccion, p. 310 |
| Mayor fuerza en cuerpo vertebral | "highest fixation strength is achieved when the screws are positioned in the vertebral body" | Introduccion, p. 310 |
| Muestra: 6 pelvis plasticas | "The technique was done on six plastic pelves (AO Synbone" | Materials and Methods, p. 311 |
| Esquema por lado: 2 en S1, 1 en S2 | "two screw insertions into the S1 vertebral body and one screw insertion into S2" | Materials and Methods, p. 311 |
| 24 orificios S1 | "24 screw holes were made through the sacroiliac joint" | Abstract, p. 310 |
| 12 orificios S2 | "12 holes were made through the sacroiliac joint into S2" | Abstract, p. 310 |
| n pacientes | NO ENCONTRADO EN EL PDF (no hay pacientes; modelo plastico) | — |
| Tornillos de referencia: 8 x 3.5 mm Ti | "eight 3.5-mm Ti screws as reference points were inserted" | Materials and Methods, p. 311 |
| CT: gantry tilt | "with a gantry tilt of 0" | Materials and Methods, p. 311 |
| CT: FOV 300 mm | "a field of view of 300 mm" | Materials and Methods, p. 311 |
| CT: corte 2 mm, ~110 cortes | "slice thickness of 2 mm giving an average of 110 slices" | Materials and Methods, p. 311 |
| Segmentacion | "semiautomatic segmentation routine based on graylevel thresholding" | Materials and Methods, p. 311 |
| Camara: precision 0.1 mm en 1 m3 | "with an accuracy of 0.1 mm inside a volume of 1 m3" | Materials and Methods, p. 311 |
| Camara: hasta 256 LED | "able to track as much as 256 pulsed infrared light emitting diodes" | Materials and Methods, p. 311 |
| 4 LED por instrumento | "marker probes holding four infrared light emitting diodes each" | Materials and Methods, p. 311 |
| Registro: 4 landmarks | "four coarse anatomic landmarks were defined on the surface of the pelvis" | Materials and Methods, p. 311 |
| 15 puntos aleatorios | "the predefined coarse landmarks and of 15 random points" | Materials and Methods, p. 311 |
| 5 puntos ala ipsilateral | "Five random points were digitized on the ipsilateral sacral ala" | Materials and Methods, p. 311 |
| 10 puntos fosa iliaca contralateral | "and 10 on the inner surface of the contralateral iliac fossa" | Materials and Methods, p. 312 |
| Sin puntos en hemipelvis inestable | "No surface point is taken from the unstable left hemipelvis." | Pie Fig 1, p. 311 |
| Brocas: largo 25 cm, 4.5 mm (S1) y 3.5 mm (S2) | "shaft length of 25 cm and diameters of 4.5 mm and 3.5 mm, respectively" | Materials and Methods, p. 312 |
| Broca 4.5 mm en S1 (confirma asignacion) | "Drilling of a 4.5-mm hole along the trajectory into the S1 vertebral body" | Pie Fig 5, p. 314 |
| Profundidad mostrada 50 mm | "The position of the drill bit at a depth of 50 mm is shown." | Pie Fig 5, p. 314 |
| Grosor de trayectoria planificada 6 mm | "The thickness of the trajectory is 6 mm." | Pie Fig 3, p. 312 |
| Criterio de precision | "expressed as translational error of the entry and the target points" | Materials and Methods, p. 313 |
| Criterio angular | "and as angular deviation of the screw hole" | Materials and Methods, p. 313 |
| Evaluacion por CT postoperatoria | "the pelves underwent a second CT examination" | Materials and Methods, p. 313 |
| Criterio de seguridad: incremento 2 mm | "each hole was enlarged concentrically with an increment in diameter of 2 mm" | Materials and Methods, p. 313 |
| Rango de cilindros 8-20 mm | "screw holes were enlarged electronically from 8 to 20 mm" | Pie Fig 6, p. 314 |
| Inconsistencia: excentrico | "The holes are enlarged eccentrically to a diameter of 20 mm" | Pie Fig 6, p. 314 |
| Metrica de perforacion (% volumen) | "expressed as a percentage value of the complete volume of each cylinder" | Pie Fig 6, p. 314 |
| Planificacion < 5 min | "was not difficult and took less than 5 minutes to do" | Results, p. 313 |
| Registro posterior < 1.4 mm | "mean translational error less than 1.4 mm in the posterior part" | Results, p. 313 |
| Registro sinfisis < 3.1 mm | "less than 3.1 mm at the pubic symphysis" | Results, p. 313 |
| Error maximo 4.0 mm post., 9.0 mm ant. | "was 4.0 mm posteriorly and 9.0 mm anteriorly" | Results, p. 313 |
| Error rotacional ~3 grados | "which was estimated to be approximately 3" | Results, p. 313 |
| Registro ~10 min | "computer calculations of the registration took on average 10 minutes" | Results, p. 313 |
| Tabla 1, S1 | "Vertebral body S1 1.12 0.48 0.34 2.38" (media, DE, min, max, mm) | Table 1, p. 315 |
| Tabla 1, S2 | "Vertebral body S2 1.26 0.63 0.46 2.53" | Table 1, p. 315 |
| Tabla 1, ala anterior derecha | "Sacral ala anterior right 1.37 0.57 0.33 2.89" | Table 1, p. 315 |
| Tabla 1, ala anterior izquierda | "Sacral ala anterior left 1.40 0.71 0.66 3.66" | Table 1, p. 315 |
| Tabla 1, ala posterior derecha | "Sacral ala posterior right 1.34 0.53 0.42 2.92" | Table 1, p. 315 |
| Tabla 1, ala posterior izquierda | "Sacral ala posterior left 1.20 0.71 0.34 4.01" | Table 1, p. 315 |
| Tabla 1, sinfisis derecha | "Symphysis right 2.92 1.66 0.48 8.86" | Table 1, p. 315 |
| Tabla 1, sinfisis izquierda | "Symphysis left 3.08 1.72 0.44 9.02" | Table 1, p. 315 |
| Entrada 2.7 mm (DE 1.4; 0.4-6.3) | "entry points of 2.7 mm (standard deviation, 1.4; range, 0.4–6.3 mm)" | Results, p. 314; Table 2, p. 315 |
| Objetivo 3.5 mm (DE 2.0; 0.2-8.2) | "target points of 3.5 mm (standard deviation, 2.0; range, 0.2–8.2 mm)" | Results, p. 314; Table 2, p. 315 |
| Angulo 2.0 grados (DE 1.0; 0.4-3.9) | "was on average 2.0 (standard deviation, 1.0; range 0.4–3.9)" | Results, p. 314; Table 2, p. 315 |
| Errores de entrada/objetivo/angulo por nivel S1 vs S2 | NO ENCONTRADO EN EL PDF (Table 2 solo da valores agregados) | — |
| 0 perforaciones | "not observed in any of the 36 screw holes" | Results, p. 314 |
| Posicion intraosea completa | "confirmed the complete intraosseous position of each bore hole" | Results, p. 314 |
| Volumen fuera de hueso 5.6% (8 mm) | "on average 5.6% with the 8-mm diameter bore hole" | Results, p. 314 |
| Volumen fuera de hueso 17.4% (20 mm) | "as much as 17.4% with the 20-mm bore hole" | Results, p. 315 |
| Menos stock oseo en S2 | "increased substantially in the S2 area where less bone stock is present" | Results, p. 315 |
| Tabla 3, S1+S2 (n = 36), 8 mm | "8 5.6 2.1 2.1 10.4" (media, DE, min, max, %) | Table 3, p. 316 |
| Tabla 3, S1+S2, 10 mm | "10 7.7 2.8 3.2 14.4" | Table 3, p. 316 |
| Tabla 3, S1+S2, 12 mm | "12 10.0 3.6 4.1 17.9" | Table 3, p. 316 |
| Tabla 3, S1+S2, 14 mm | "14. 11.2 3.7 4.4 18.9" | Table 3, p. 316 |
| Tabla 3, S1+S2, 16 mm | "16 12.9 4.1 4.8 21.6" | Table 3, p. 316 |
| Tabla 3, S1+S2, 18 mm | "18 15.1 4.3 5.4 23.9" | Table 3, p. 316 |
| Tabla 3, S1+S2, 20 mm | "20 17.4 4.4 6.9 25.9" | Table 3, p. 316 |
| Tabla 3, S1 (n = 24), 8 mm | "8 5.1 2.1 2.1 10.4" | Table 3, p. 316 |
| Tabla 3, S1, 10 mm | "10 6.9 2.9 3.2 14.4" | Table 3, p. 316 |
| Tabla 3, S1, 12 mm | "12 9.0 3.5 4.1 17.9" | Table 3, p. 316 |
| Tabla 3, S1, 14 mm | "14 10.2 3.7 4.4 18.9" | Table 3, p. 316 |
| Tabla 3, S1, 16 mm | "16 11.7 4.1 4.8 21.6" | Table 3, p. 316 |
| Tabla 3, S1, 18 mm | "18 13.9 4.4 5.4 23.9" | Table 3, p. 316 |
| Tabla 3, S1, 20 mm | "20 16.2 4.5 6.9 25.9" | Table 3, p. 316 |
| Tabla 3, S2 (n = 12), 8 mm | "8 6.6 1.7 3.8 8.9" | Table 3, p. 316 |
| Tabla 3, S2, 10 mm | "10 9.2 2.3 5.8 12.7" | Table 3, p. 316 |
| Tabla 3, S2, 12 mm | "12 12.1 2.6 7.6 16.2" | Table 3, p. 316 |
| Tabla 3, S2, 14 mm | "14 13.4 2.7 8.2 17.8" | Table 3, p. 316 |
| Tabla 3, S2, 16 mm | "16 15.5 2.9 9.4 19.9" | Table 3, p. 316 |
| Tabla 3, S2, 18 mm | "18 17.7 3.0 10.6 21.7" | Table 3, p. 316 |
| Tabla 3, S2, 20 mm | "20 19.8 3.0 12.1 23.7" | Table 3, p. 316 |
| Prueba estadistica S1 vs S2 | NO ENCONTRADO EN EL PDF | — |
| Escala ordinal / grados de malposicion | NO ENCONTRADO EN EL PDF (solo perforacion si/no y errores continuos) | — |
| Diametro de tornillo: 2 x 6.5 mm en S1 | "allowing a double 6.5-mm screw insertion in the vertebral body of S1" | Discussion, p. 316 |
| Diametro de tornillo: 1 x 4.5 mm en S2 | "and one 4.5- mm screw insertion into S2" | Discussion, p. 316 |
| Largo de tornillo | NO ENCONTRADO EN EL PDF | — |
| Material/tipo del tornillo de fijacion (canulado, rosca) | NO ENCONTRADO EN EL PDF (solo "cortical screw" para S2, p. 317) | — |
| Riesgo de perforacion en S2 | "increased risk for screw perforation when screw insertion was done into the S2 vertebra" | Discussion, p. 317 |
| Recomendacion de 4.5 mm en S2 | "insertion of a 4.5-mm cortical screw is recommended" | Discussion, p. 317 |
| Condicion de la recomendacion | "but only when necessary from the mechanical point of view" | Discussion, p. 317 |
| Formulacion "no larger than 4.5 mm" | NO ENCONTRADO EN EL PDF (es parafrasis de Moed 2006) | — |
| Fuente del error | "a combination of the error of the surface-matching algorithm and of the surgical action" | Discussion, p. 317 |
| Fluoroscopia citada 2.3 min/tornillo | "a mean fluoroscopy time per screw of 2.3 minutes" | Discussion, p. 315 (atribuido a ref. 20) |
| Rango fluoroscopia citado | "(range, 1.4–4.4 minutes per screw)" | Discussion, p. 315 (atribuido a ref. 20) |
| Relacion con resumen CAOS 1999 de Gautier y Baechler | NO ENCONTRADO EN EL PDF | — |
