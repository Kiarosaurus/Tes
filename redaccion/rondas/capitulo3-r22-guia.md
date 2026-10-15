# Revision guia CS — capitulo3 — r22

Entradas: `overleaf/secciones/capitulo3.tex` (estado r21), lint `capitulo3-r22-lint.md` (PASA, 22 E-P1 bajas
preexistentes), respuesta `capitulo3-r21-respuesta.md` (sin RECHAZADOS) y encargo `ENCARGO_2026-10-15.md`. Contraste
con `docs/01-decisiones.md` 2026-10-15 (puntos 1-22) y con #185/#186 (ABIERTAS: solo hechos medidos). Cruce leido:
`introduccion.tex` (objetivos, :48, :90). El `.tex` todavia no aplica el encargo: las 16 `\GAPDEC` siguen abiertas, y
ademas hay prosa fuera de las marcas que contradice la entrada 2026-10-15.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-C7 | capitulo3.tex:451, 461-463 | Faltan en Amenazas las tres asimetrias medidas del contraste primario (#186): cortes `k = 2` solo en el protocolo fisico (62 341 frente a 124 679 voxeles por paciente), piso de ruido del protocolo fisico (mediana 184 HU) y suelo de -1000 HU solo en el sintetizador. :463 nombra los cortes sin cifra ni tratamiento, y :451 no dice que el suelo afecta a un solo brazo. | En validez de la conclusion: cada asimetria con su cifra medida, su sentido y la sensibilidad que la trata (DEC 2026-10-15 puntos 1, 17 y 18), todas posteriores. Resultados en `\GAPDATO`. Sin la lectura interpretativa de #186. |
| guia-2 | alta | G-C7 | capitulo3.tex:419, 391, 429 | Patron PAT-140 reincide. La lista post hoc no recoge el bloque del 2026-10-15, decidido despues de ver la prueba de v1 (#177), el `Delta` de run05a, E-A1 de v2 en prueba (#184) y los HTML de run04. Ademas, :419 ("ninguna uso pacientes de prueba") quedaria falso al anadirlo. Falta tambien la regla general: ninguna sensibilidad eleva la categoria del desenlace primario. | Un parrafo en validez interna: que se decidio el 2026-10-15, que se habia visto (inventario `experiments/objetivo3/visto.md`), "posterior para v1 y previo solo al TOST de prueba de v2", y la regla general. Acotar :419 a "las decisiones de validacion". En :391, que la lectura de desenlaces se fijo despues de v1. |
| guia-3 | alta | G-C8 | capitulo3.tex:377 (3.ª marca), 453, 463 | Patrones PAT-136 y PAT-116 reinciden. El `\GAPDEC` de :377 y la frase de :453 "la lectura de ese desenlace no esta fijada" contradicen DEC punto 15, que fija tres desenlaces (equivalencia, no equivalencia y no concluyente) mas la direccion. :463 ("puede no alcanzar a concluir equivalencia ni diferencia") sigue siendo un condicional sobre un resultado ya obtenido. | Enunciar en :377 los tres desenlaces, la regla de la direccion (IC90 que excluye 0), lo confirmatorio (solo el modelo evaluado con su `Delta`) y lo descriptivo, con multiplicidad declarada y sin correccion. Aclarar que se fijo despues de v1. Reescribir :453 y :463 con esas categorias. |
| guia-4 | media | G-C8 | capitulo3.tex:377 (2.ª marca) | El supuesto de *t* sigue en `\GAPDEC`, y DEC punto 14 lo decide: diferencias pareadas aproximadamente normales e independientes, con sensibilidad por IC90 exacto que invierte la permutacion pareada (2^13 cambios de signo). | Enunciar el supuesto y la sensibilidad como metodo posterior, sujeta a la regla general. Resultado en `\GAPDATO`. |
| guia-5 | media | G-T4 | capitulo3.tex:377 (1.ª marca) | Patron PAT-19 reincide. Pide el "cierre formal" de la contingencia #90, que esta CERRADA por ejecucion; DEC punto 13 manda retirar la marca. | Retirar la marca sin poner prosa en su lugar. |
| guia-6 | media | G-C8 | capitulo3.tex:375 | La marca del tamano de efecto la resuelve DEC punto 12: se declara la degeneracion (copia y pegado = 0 por construccion; p = 2^-13 es el minimo alcanzable) y no se reporta tamano de efecto. Tampoco se describe el comparador parametrico nuevo. | Decir la degeneracion con sus dos datos. Describir el artefacto parametrico (tornillo a HU constante mas el perfil radial medio del artefacto real de tornillos), posterior y descriptivo, y dejar claro que no sustituye la linea base. |
| guia-7 | media | G-C1 | capitulo3.tex:198, 325, 419, 451 | La regla del suelo sigue presentada como vigente y "sin conversion" (:198, :451), y :419 lista el percentil 5 como decision post hoc. DEC punto 1 la declara no aplicable y da los dos valores (225.0 HU con p95 por paciente y 1.2 HU con la mediana). :325 solo mide la fraccion en el suelo para el sintetizador. | Sustituir la marca por: regla no aplicable, sus tres razones (depende del percentil, era calculable antes de fijar una conversion y la rama de cambio esta bloqueada) y los dos valores. Anadir la fraccion de la region del protocolo fisico bajo -1000 HU y el TOST con suelo simetrico (posterior, en direccion hacia la equivalencia). Que auditor-trazabilidad coteje "percentil 5 de la fraccion" frente a "p95 de la perdida en HU" (#186). |
| guia-8 | media | G-C1 | capitulo3.tex:143 | La cabeza sigue en `\GAPDEC`, y DEC punto 2 la resuelve: la sintesis con cabeza es una desviacion declarada de D3 (2026-09-20), con una sensibilidad sin las regiones de medicion a menos de 20 mm del extremo con cabeza, en los dos brazos. | Declarar la desviacion en :143 y anadir esa sensibilidad (posterior) en la lista de :377. |
| guia-9 | media | G-T4 | capitulo3.tex:204 | Patron PAT-19 reincide. DEC punto 3 fija el lote en 16 y dice que "lote 4" fue un error de registro. | Retirar la marca y dejar "lotes de 16". |
| guia-10 | media | G-C5 | capitulo3.tex:214, 447 | El semimaximo sigue en `\GAPDEC`. DEC punto 4: no se entrena, por coste, y se reporta la diferencia de diametro entre las dos mascaras en componentes de 500-4000 mm3 como dato de la limitacion. Esa limitacion no aparece en Amenazas. | En :214, que la sensibilidad no se entrena y por que. En constructo (:447 o vecino), la limitacion, con la cifra en `\GAPDATO`. |
| guia-11 | media | G-C5 | capitulo3.tex:228 | La costura sigue en `\GAPDEC`. DEC punto 5 la mide en la sintesis sobre pelvis sin metal para los dos brazos y anade el perfil de *streak amplitude* en anillos de 2 mm entre 8 y 16 mm, descriptivo. | Describir las dos mediciones como metodo, con resultado en `\GAPDATO`, y anadirlas a la lista de descriptivos posteriores. |
| guia-12 | media | G-T4 | capitulo3.tex:232 | El paciente de 8.9 mm sigue en `\GAPDEC`. DEC punto 6 lo clasifica en el grupo 2 segun `grupos.csv`, y la clasificacion no cambia receptores ni resultados. | Retirar la marca y decir "grupo 2" en prosa. |
| guia-13 | media | G-C1 | capitulo3.tex:242 | La causa del p95 sigue en `\GAPDEC`. DEC punto 7 fija un diagnostico con regla de lectura: decodificacion con la mezcla frente a solo la ventana ancha, control sobre la ida y vuelta real y umbral de >= 4 de 7 cascaras y "menos de la mitad". | Describir el diagnostico y su regla. Lo que mida va en `\GAPDATO`; decir que no cambia el modelo ni la evaluacion. |
| guia-14 | media | G-C5 | capitulo3.tex:317 | La preservacion del protocolo fisico sigue en `\GAPDEC`. DEC punto 8: RMSE y SSIM (rango [-1000, 2000] HU) frente a la TC original, fuera de `G` y dentro del cuerpo, mas su amplitud de solo ruido, como caracterizacion de la comparacion. Para el sintetizador vale 0 por construccion. | Sustituir la marca por esa medicion (resultado en `\GAPDATO`) y decir que no es un resultado del sintetizador. |
| guia-15 | media | G-C7 | capitulo3.tex:327, 457 | La razon de la pose queda en `\GAPDEC`, y :457 afirma que el Objetivo 3 no cubre las poses del muestreador. DEC punto 9 da la razon (aislar la apariencia de la colocacion; coste de 108.9 h con `k = 1`) y anade un exploratorio con 5 poses por paciente, solo con el sintetizador, por grado de brecha y con una expectativa fijada antes. | Dar la razon en :327 y describir el exploratorio con su expectativa. En :457, acotar: las cubre solo el exploratorio del sintetizador, sin comparacion con el protocolo fisico. |
| guia-16 | media | P-MM3 | capitulo3.tex:341 | El control de calidad visual sigue en `\GAPDEC`. DEC punto 10 fija la muestra: 13 pacientes x semilla 0 x 3 cortes definidos, con una lista cerrada de defectos. Es un control y no una evaluacion, y no fue ciego para el modelo evaluado. | Dar la regla y la lista de defectos y decir que no fue ciego. Remitir a la comparacion a ciegas de :277, que es aparte. |
| guia-17 | media | G-C2 | capitulo3.tex:355, 353, 357 | El `\GAPDEC` de :355 pregunta si se cita el repositorio del desafio AAPM, pero :357 ya cita `xcist2025example` (guiones del desafio AAPM, commit fijo) y DEC punto 11 lo decide. Faltan la cita en :353 y la tabla de las cinco desviaciones. Esto sustituye la fila de la bitacora del 2026-10-10 ("sin cita ni URL mientras #158 este abierta"). | Retirar la marca, citar `xcist2025example` donde se toman los pasos (:353) y llevar las cinco desviaciones de :355 a una tabla. No hace falta un `\GAPLIT` nuevo. |
| guia-18 | media | G-C8 | capitulo3.tex:431-433 | La marca del margen la resuelve DEC punto 16: margen minimo de equivalencia de cada modelo y TOST de los tres con el margen comun de 196.3 HU, ademas del propio. :433 sigue diciendo que ninguna sensibilidad mide las tres elecciones juntas. | Describir el margen minimo (mayor valor absoluto de los limites del IC90) y el margen comun como metodo posterior, con resultado en `\GAPDATO`. Revisar la ultima oracion de :433. Vigilar PAT-14 en "margen" (cortical, `Delta`, minimo, comun). |
| guia-19 | media | G-C8 | capitulo3.tex:377-381 | Falta la lectura de acuerdo entre brazos (DEC punto 22: Bland-Altman y Pitman-Morgan, descriptivos, v1 y v2). Tampoco aparece su motivo medido, la menor dispersion entre pacientes del sintetizador (CV 0.076 frente a 0.241, #185). | Anadirla al analisis estadistico como descriptiva y posterior, con el CV como motivo y sin interpretarlo. Resultado en `\GAPDATO`. |
| guia-20 | media | G-C6 | capitulo3.tex:277, 38 | El metodo de la evaluacion de v2 no recoge el TOST con el margen comun (DEC punto 16) ni E-A1 repetida con el limite de lectura 0.03 (DEC punto 19). Patron PAT-122 reincide: el `\GAPDATO` de :277 y :38 dicen "en curso", y la DEC registra que `a20_v2` aborto en la validacion y espera relanzarse. | Anadir los dos analisis a :277 como metodo. Actualizar el estado a "por relanzar" en las dos marcas. |
| guia-21 | baja | G-T2 | capitulo3.tex:248 | "No se concluyo equivalencia" no usa la categoria que fija DEC punto 15: no concluyente, con diferencia significativa a la baja. | Usar la categoria nombrada en :248, sin cifras (bitacora 2026-10-14: las cifras van al cap. 4). |
| guia-22 | baja | G-C5 | capitulo3.tex:404 | La fila 3 de `tab:diseno` no recoge la lectura en tres desenlaces ni marca que las sensibilidades y lecturas del 2026-10-15 son descriptivas. | Anadir "tres desenlaces; sensibilidades descriptivas, posteriores" a la celda de Analisis, sin enumerarlas. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | cumple (salvo guia-21, baja) |
| G-T3 | cumple |
| G-T4 | no cumple (guia-5, guia-9 y guia-12: GAP que la DEC ya cierra) |
| G-T5 | cumple |
| G-T6 | cumple (lint PASA; `xcist2025example` existe) |
| G-C1 | no cumple (guia-7, guia-8, guia-13) |
| G-C2 | no cumple (guia-17) |
| G-C3 | cumple |
| G-C4 | cumple dentro del capitulo; el desfase con `introduccion.tex`:48 y :90 lo atiende `introduccion-r07` |
| G-C5 | no cumple (guia-10, guia-11, guia-14, guia-22) |
| G-C6 | no cumple (guia-20) |
| G-C7 | no cumple (guia-1, guia-2, guia-15) |
| G-C8 | no cumple (guia-3, guia-4, guia-6, guia-18, guia-19) |
| G-C9 | cumple (la linea base fuerte es el protocolo fisico; el comparador parametrico la complementa) |
| P-MM1 | cumple |
| P-MM2 | cumple (`fig:pipeline`) |
| P-MM3 | no cumple (guia-16) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que declara pendiente lo que una DEC posterior ya fija | G-T4, OC-2 | "\GAPDEC{... lotes de 4, pero el entrenamiento uso lotes de 16 ...}" | PAT-19 |
| Lista post hoc que omite un bloque entero de decisiones posteriores | G-C7 | "varias decisiones siguieron a resultados de validacion, y ninguna uso pacientes de prueba" | PAT-140 |
| Desenlaces de equivalencia sin lectura, aunque una DEC ya la fija | G-C8 | "la lectura de ese desenlace no esta fijada" | PAT-136 |
| Condicional sobre un resultado que ya se obtuvo | G-T4 | "puede no alcanzar a concluir equivalencia ni diferencia" | PAT-116 |
| GAP de corrida "en curso" cuando la corrida aborto | G-T4 | "cuyas generaciones estan en curso" | PAT-122 |
| Al cerrar una marca GAP, la prosa que repite el mismo hueco fuera de la marca queda sin revisar | G-T4, G-C7 | "pero no fija como expresar esa perdida en HU" (:451, fuera de la marca de :198) | nuevo |
