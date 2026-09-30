# Revision guia CS — introduccion — r01

Alcance acotado por la autora: `introduccion.tex` l. 23-76 (Objetivos, Justificacion, Alcance y
limitaciones). Encabezado (l. 1-17) y Formulacion del problema (l. 19-21) fuera de alcance. Secciones
cruzadas leidas: `capitulo3.tex` (completo), `capitulo2.tex` y `capitulo1.tex` (esqueletos),
`conclusiones.tex` (plantilla), `docs/00-tesis.md` (Fuera de alcance).

**Nota de contexto (no es hallazgo, ya es `\GAPDEC` l. 28, #126):** la pregunta de l. 21 promete
sintesis 2D, SSIM/MAE, DSC/HD95 y comparacion con aumento convencional; ninguno de los cuatro
objetivos lo cubre. Ademas la introduccion no tiene hipotesis (G-A1 pide preguntas **o** hipotesis;
`docs/00-tesis.md` §Hipotesis sigue vacia, "<pegar del main.tex>"): conviene reescribirlas juntas.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-A7 | introduccion.tex:46 | "Cada objetivo tiene en el Capitulo 3 una variable dependiente que lo verifica" es falso para el Obj. 4: cap. 3 l. 185 dice que no tiene fila propia en la tabla de diseno, y el mismo parrafo lo admite con `\GAPDEC`. Reaparece el patron de PAT-1 (erradicado). | Acotar: "Los Objetivos 1 a 3 tienen ... una variable dependiente; el 4 no" y dejar el `\GAPDEC` donde esta. |
| guia-2 | media | G-A7, G-T5 | introduccion.tex:28, 37 | l. 28 dice que los objetivos "corresponden a las piezas de la cadena", y el titulo del Obj. 1 promete "validar una representacion multiventana". Pero la compuerta evalua la ida y vuelta por el autoencoder, que la cadena ya no usa (cap. 3 fig. 1: "previa a la cadena"), y el objetivo general y el Obj. 3 usan la codificacion multiventana sin autoencoder, cuyo error de ida y vuelta ningun objetivo verifica (cap. 3 l. 172, `\GAPDEC`). | Decir que el Obj. 1 evalua la ruta latente y que su veredicto fijo el dominio de imagen; no presentarlo como pieza de la cadena, y anotar que la codificacion sin autoencoder no la valida ningun objetivo (remitir al `\GAPDEC` del cap. 3). |
| guia-3 | media | G-A7, G-A8 | introduccion.tex:39, 43 | Los Obj. 2 y 4 reclaman la misma evidencia: comparar la distribucion de grados con la referencia clinica mediante Wasserstein-1. Si la distancia es grande, no se sabe cual de los dos falla. La segunda mitad del Obj. 4 ("adoptar un protocolo de apariencia heredado") es una decision de diseno y no puede fallar. El `\GAPDEC` de l. 46 solo cubre "mas alla de los controles". | Atribuir la comparacion con Wasserstein-1 a un solo objetivo (el cap. 3 la pone en la fila del Obj. 2), y ampliar el `\GAPDEC` del Obj. 4 para que diga si la adopcion del protocolo cuenta como objetivo evaluable. |
| guia-4 | media | G-A9 | introduccion.tex:52 | Se rompe el embudo entre necesidad y problema. La necesidad es la escasez de TC con metal anotados; lo evaluado es la coherencia fisica y quirurgica. Falta la oracion que diga por que esa coherencia es lo que hay que establecer antes de medir la utilidad, o que la justifique por si misma. Hoy la justificacion descansa en una necesidad que el trabajo declara no atender. | Agregar el eslabon con fuente del repositorio (TM, `docs/00-tesis.md`), o `\GAPDEC` si no esta escrito. |
| guia-5 | media | G-A9, G-A3 | introduccion.tex:50-58 | La brecha ("ninguno de los tres enfoques revisados resuelve a la vez donde ... y como se ve", l. 54) aparece en Justificacion, despues de la Formulacion y de los Objetivos. El embudo de G-A9 pone la justificativa antes del problema y de los objetivos, y los objetivos quedan presentados antes de la tension que los motiva. | Proponer a la autora mover Justificacion antes de Formulacion del problema (overleaf/CLAUDE.md permite cambiar titulos y orden de secciones), o llevar la tension de l. 54-56 al encabezado cuando se reescriba. |
| guia-6 | media | G-A10 | introduccion.tex:70 | l. 66 anuncia "cada uno por una razon distinta", pero la exclusion de XCIST/CatSim solo dice que se sustituye, no por que queda fuera. `docs/00-tesis.md` punto 3 tampoco da la razon. | Dar la razon, con fuente del repositorio, o marcar `\GAPDEC{razon para excluir la reimplementacion validada de XCIST/CatSim}`. |
| guia-7 | media | G-T2 | introduccion.tex:32, 37, 39, 41, 43, 64 | Se usan sin definir terminos que el lector de computacion no conoce, y cap. 1 es todavia un esqueleto: osteosintesis (l. 32), autoencoder (l. 37), S1 y corredor oseo (l. 39), difusion 2.5D e *inpainting* (l. 41), distancia de Wasserstein-1 (l. 43), tornillo iliosacro (l. 64). | Dar una glosa de pocas palabras en la primera aparicion, o remitir a la seccion del cap. 1 que los definira. |
| guia-8 | baja | G-T2 | introduccion.tex:39 | "criterio de viabilidad del corredor de McLaren et al." no coincide con el cap. 3 (l. 89): alli el criterio es $D \geq d + 2\epsilon$, a partir de Kaiser, y McLaren aporta el procedimiento de medicion del diametro (tambien `docs/00-tesis.md` punto 6). | Cambiar por "el procedimiento de medicion del corredor de McLaren et al.". |
| guia-9 | baja | G-A10 | introduccion.tex:60 | El hallazgo del No-Go (latentes sin hueso denso ni metal) es un resultado anticipado, pero va dentro de la "justificacion metodologica", que el parrafo abre diciendo que trata "como se evaluan dos de los objetivos". | Moverlo al parrafo de la contribucion (l. 58) como resultado anticipado, o reescribir la oracion tematica. |
| guia-10 | baja | G-A10 | introduccion.tex:76 | Las limitaciones enumeran hechos sin su efecto sobre el resultado: una fractura en la cohorte, una reconstruccion no reportada, un protocolo validado en 2D. Patron PAT-38 reincide, en version de introduccion. | Media clausula por limitacion con el sentido del sesgo (p. ej., una fractura estrecha el corredor y sube los grados de brecha), igual que en cap. 3 §Amenazas. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | no cumple (guia-7, guia-8) |
| G-T3 | cumple ($M$, $B_{\delta}$, $G$ iguales en cap. 3) |
| G-T4 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-T5 | no cumple (guia-2, guia-5) |
| G-T6 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-A1 | cumple con GAP (proposito presente; pregunta/hipotesis bajo `\GAPDEC` l. 28, #126) |
| G-A2 | no evaluable (encabezado fuera de alcance) |
| G-A3 | cumple (tension en l. 54-56); ubicacion en guia-5 |
| G-A4 | cumple (no hay pose canonica; rayas fuera de la mascara; latentes sin hueso denso) |
| G-A5 | cumple en el alcance revisado |
| G-A6 | cumple |
| G-A7 | no cumple (guia-1, guia-2, guia-3) |
| G-A8 | cumple con GAP (Obj. 2, 3 y 4 con `\GAPDEC` l. 46; Obj. 1 falsable) |
| G-A9 | no cumple (guia-4, guia-5) |
| G-A10 | no cumple, a medias (guia-6; bajas guia-9, guia-10) |
| G-B10 | no evaluable (capitulo2 es esqueleto) |
| G-C4 | cumple (los cuatro objetivos coinciden con cap. 3 l. 13 y la tabla de diseno) |
| G-D1, G-D2 | no evaluable (conclusiones es plantilla) |

## Propuestas de criterio
- Un criterio de la guia (G §2.2) que diga que cada objetivo especifico tiene **evidencia propia**, no compartida con otro objetivo (hoy solo se infiere de G-A7; ver guia-3).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Frase de sintesis atribuye a todos los objetivos una propiedad que uno no tiene | G-A7 | "Cada objetivo tiene en el Capitulo 3 una variable dependiente que lo verifica" | PAT-1 (erradicado, reaparece) |
| Dos objetivos reclaman la misma evidencia, asi que no se sabe cual falla | G-A7, G-A8 | Obj. 2 y Obj. 4, ambos "frente a la referencia clinica" con Wasserstein-1 | nuevo |
| Lista que anuncia "cada uno por una razon" y un elemento solo dice su sustituto | G-A10 | "Reimplementacion validada de XCIST/CatSim. En su lugar se adopta ..." | nuevo |
| Objetivo titulado por lo que valida la cadena actual cuando valida una ruta descartada | G-A7, G-T5 | "Validar una representacion multiventana" (se valido el autoencoder latente) | nuevo |
| Limitacion enunciada sin su efecto sobre el resultado | G-C7, G-A10 | "al menos un paciente ... tiene una fractura confirmada" | PAT-38 |
