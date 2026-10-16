# Revision guia CS — capitulo3 — r24

Texto revisado: `overleaf/secciones/capitulo3.tex` tal como esta al abrir la ronda (lint r24: GAP dec=3, ningun
`\REVVISUAL`). El encargo `ENCARGO_2026-10-15b.md` todavia no esta aplicado. Por eso varios hallazgos senalan donde
la DEC 2026-10-15 (3) deja obsoleto el texto o una marca. Cruces leidos: `introduccion.tex` (:41-52) para G-A7, G-A8 y
G-C4, y `capitulo1.tex` (:101) para G-T3. Respuesta previa: `capitulo3-r23-respuesta.md`; sus cuatro escalados (T02,
guia-2, guia-4, T04) los resuelve ahora la DEC 2026-10-15 (3), ptos 1-3 y 10.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-A8, G-C4 | capitulo3.tex:417 | El `\GAPDEC` "que significa un desenlace no concluyente" ya lo resuelve DEC 2026-10-15 (3) pto 1 (PAT-122 y PAT-176 reinciden). El pto 1 tambien da el objetivo por "cumplido como objetivo de diseno y evaluacion". Si eso se redacta junto a "la no equivalencia haria fallar el objetivo" (:417, introduccion:50), ningun desenlace hace fallar el Objetivo 3, porque haberlo ejecutado ya lo cumple | Cerrar la marca con el pto 1 y separar dos niveles. El objetivo de diseno se cumple al implementar y evaluar. La hipotesis de equivalencia es lo que puede fallar: con "no concluyente, a la baja" los datos no permiten afirmar equivalencia y muestran una amplitud menor, y la no equivalencia la refutaria. Decir que esta lectura es posterior al resultado. Si la autora no quiere separar los niveles, `\GAPDEC` sobre que resultado haria fallar el objetivo |
| guia-2 | media | G-C7 | capitulo3.tex:519; :487 | El `\GAPDEC` sobre el sentido del piso de ruido (#188) ya lo cierra el pto 3: el piso favorece al sintetizador, con 893 frente a 184 HU. La prosa de fuera de la marca sigue repitiendo el hueco: "puede ser distinta de cero aun sin implante" (:519) y "de ese efecto solo se conoce el sentido" (:487) (PAT-168) | En la amenaza de :519, dar los dos pisos y su sentido (favorece al sintetizador) y quitar la marca. El contraste pareado entra como descriptivo y con su limite: cambiar el canal $M$ cambia toda la trayectoria de muestreo, asi que no aisla un artefacto puro. Su cifra (-455.0 HU, IC90) choca con BITACORA §2 2026-10-11 ("sensibilidad de un veredicto: en el cap. 3 sin cifra"), aunque el encargo la da: el orquestador debe decidir si va al cap. 3 o al cap. 4 |
| guia-3 | media | G-C8, G-C7 | capitulo3.tex:429; :513-515 | El `\GAPDEC` sobre la escala del acuerdo lo resuelve el pto 2. El pto 2 tambien contradice la oracion de :429 "la prueba compara varianzas y no coeficientes de variacion": decide aplicar Pitman y Morgan sobre ln como prueba aproximada de CV. Los cinco limites de #189 no aparecen en Validez de la conclusion | :429: escribir las dos escalas (HU para el TOST; razon en logaritmo para Bland y Altman) y las dos lecturas de Pitman y Morgan (sobre HU, varianzas; sobre ln, aproximacion al CV). Esa aproximacion lleva `\GAPLIT` si ninguna ficha la respalda (E3 del encargo; PAT-179). En :513-515, enumerar los cinco limites: pendiente que persiste en log, sin diferencia aceptable fijada, promedio de semillas, varianza frente a CV, normalidad con n = 13 |
| guia-4 | media | G-T4, OC-2 | capitulo3.tex:250, :289, :367, :427 | Siguen marcas "consta en una implicancia abierta" sobre implicancias que DEC (3) ya decidio: #191 (pto 6) en :250, #190 (pto 5) en :289, #187 (pto 4) en :367, y #187, #188 y #189 (ptos 2-4) en :427. En :289 la marca mezcla #184, aun ABIERTA, con #190, decidida (PAT-122 y PAT-133 reinciden) | Lecturas decididas: sin marca y con remision al capitulo de resultados (BITACORA §2 2026-10-15, medicion ejecutada sobre prueba que no depende de una lectura abierta). En :289 dejar la marca solo para lo que depende de #184 |
| guia-5 | media | G-C7 | capitulo3.tex:481; :483 | :481 dice que las decisiones del 15 de octubre son "previas solo a la prueba de equivalencia de la version 2". Las de DEC 2026-10-15 (3) son posteriores a la prueba de la v1 y tambien a la de la v2: fijan la lectura del Obj 3, el sentido del piso, la escala del acuerdo y la atribucion del p95. El inventario de lo visto queda corto (PAT-13 y PAT-140 reinciden) | Separar dos tandas: la del 15 de octubre, previa a la prueba de equivalencia de la v2, y la del 15 de octubre (3), posterior a las dos. En :483, anadir a la lista post hoc las lecturas de los ptos 1-6, el perfil por anillos y el contraste pareado |
| guia-6 | media | P-MM3, G-C5 | capitulo3.tex:367-369; :427 | DEC (3) pto 4 manda reportar en el cap. 4 el perfil por anillos de 0 a 12 mm (regla fijada antes: un brazo es "plano" si su razon 0-2/6-8 mm es menor que 2) y, con el pto 3, el contraste pareado. El metodo de ninguno de los dos esta en el capitulo: un resultado anunciado sin su medicion (PAT-88 reincide). El papel del comparador parametrico se da solo en negativo ("no sustituye", "no entra en ninguna decision") | En `sec:ap-analisis`, describir el perfil por anillos (estadistico, anillos y regla de "plano") y el contraste pareado (sintesis con metal menos sin metal con la misma semilla, regla fijada antes de correr), sin cifras y con remision al cap. 4. En :369, nombrar el papel que fija el pto 4: oraculo de nivel calibrado con datos reales, que reproduce la amplitud por construccion y no la textura |
| guia-7 | media | OC-2, OC-3 | capitulo3.tex:31, :36, :38, :40, :248, :250, :256, :287, :289, :323, :357-361, :431-435, :452, :471, :497, :505, :507, :511 | No hay ningun `\REVVISUAL` en el capitulo. Varios pasajes tratan del realismo del artefacto sintetico, o su afirmacion depende de el, mientras #193 sigue ABIERTA: el contraste de realismo, el control visual y la comparacion visual a ciegas, el juicio visual de la autora (:287), "una limitacion del realismo" (:248), la moteadura de #176 (:497) y el reclamo de coherencia de apariencia (:36, :323) | Envolver cada pasaje (no el titulo de seccion de :323) en `\REVVISUAL`, con los GAP que contenga dentro. :256 (atenuacion desde 4 mm) es una medicion y no un juicio visual: que lo decida la autora. Nada de #193 entra como hecho |
| guia-8 | media | G-T3 | capitulo3.tex:369 vs capitulo1.tex:101 | $\beta$ es el angulo del voxel en el plano del tornillo (:369). En el cap. 1, $\beta_n$ es la varianza de cada paso de difusion: el mismo simbolo con dos significados en dos capitulos (PAT-14 reincide; la fila del 2026-10-15 de BITACORA §2 que fija el angulo solo reservo $\theta$) | Cambiar el angulo de :369 por un simbolo libre en el documento, y actualizar la fila de BITACORA §2 |
| guia-9 | baja | G-T4 | capitulo3.tex:38 | Dice que la evaluacion en prueba de la v2 "esta incompleta", pero :289 da por ejecutadas la prueba de equivalencia y la reconstruccion de implantes reales. No se dice que falta | Nombrar lo pendiente (por ejemplo, la comparacion visual a ciegas, dentro de `\REVVISUAL`) o quitar "incompleta" |
| guia-10 | baja | G-T3 | capitulo3.tex:157 vs capitulo1.tex:98 | La normal se escribe $N(0, \sigma_t)$ en el cap. 3 y $\mathcal{N}$ en el cap. 1: dos notaciones para el mismo objeto | Unificar en $\mathcal{N}$ |

TOTAL alta=1 media=7 baja=2

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | cumple |
| G-T3 | no cumple (guia-8, guia-10) |
| G-T4 | no cumple (guia-4, guia-9) |
| G-T5 | cumple |
| G-T6 | cumple (compila sin citas indefinidas segun el lint) |
| G-A7 (cruce) | cumple con GAP (el contraste de realismo no tiene script) |
| G-A8 (cruce) | no cumple (guia-1) |
| G-C1 | cumple |
| G-C2 | cumple con GAP |
| G-C3 | cumple |
| G-C4 | no cumple (guia-1) |
| G-C5 | no cumple (guia-6) |
| G-C6 | cumple |
| G-C7 | no cumple (guia-2, guia-3, guia-5) |
| G-C8 | no cumple (guia-3) |
| G-C9 | cumple (protocolo fisico como contraste primario; copia y pegado declarado control de cordura) |
| P-MM1 | cumple |
| P-MM2 | cumple |
| P-MM3 | no cumple (guia-6); lo demas con GAP |
| OC-2 / OC-3 | no cumple (guia-4, guia-7) |

## Propuestas de criterio
- Criterio transversal sobre falsabilidad tras una lectura posterior: cuando una decision posterior da un objetivo por
  cumplido, el texto debe seguir nombrando que resultado lo habria hecho fallar (extiende G-A8 al momento en que se
  escriben los resultados).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Marca "consta en una implicancia abierta" que sigue en pie cuando una DEC posterior ya decidio la implicancia | G-T4, OC-2 | "desenlace del diagnostico ... consta en una implicancia abierta (implicancia 191)" | PAT-122 |
| GAP multiple con una parte decidida y otra abierta, que se conserva entero | OC-2 | "constan en implicancias abiertas (implicancias 184 y 190)" | PAT-133 |
| Decision que da un objetivo por cumplido al haberse ejecutado, sin que se diga que resultado lo haria fallar | G-A8 | "el Objetivo 3 se cumple como objetivo de diseno y evaluacion" | nuevo |
| Salvedad temporal ("previas a X") que una tanda posterior de decisiones del mismo dia deja falsa | G-C7 | "posteriores para la version 1 y previas solo a la prueba ... version 2" | PAT-13 |
| Resultado mandado al capitulo de resultados sin que el metodo describa la medicion | P-MM3, G-C5 | perfil por anillos 0-12 mm y contraste pareado ausentes del cap. 3 | PAT-88 |
| El mismo simbolo griego con dos significados en capitulos distintos | G-T3 | $\beta$ angulo (cap. 3) / $\beta_n$ varianza de difusion (cap. 1) | PAT-14 |
| Oracion que contradice una decision nueva queda junto a la marca que esa decision cierra | G-C8, OC-5 | "La prueba compara varianzas y no coeficientes de variacion" | PAT-176 |
