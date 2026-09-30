# Revision guia CS — introduccion — r02

Alcance acotado por la autora: `introduccion.tex` l. 23-76 (Objetivos, Justificacion, Alcance y
limitaciones). Encabezado (l. 1-17) y Formulacion del problema (l. 19-21) fuera de alcance (#126);
los hallazgos del lint en l. 7, 13 y 21 tambien. Secciones cruzadas leidas: `capitulo3.tex`
(completo), `capitulo1.tex` y `capitulo2.tex` (esqueletos), `conclusiones.tex` (plantilla),
`docs/00-tesis.md` (Fuera de alcance). Respuesta r01 leida: no se reabre ningun RECHAZADO (no hubo)
ni los ESCALADOS (guia-4 y guia-5 quedan como `\GAPDEC` en l. 28 y l. 50).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-A7, G-T5 | introduccion.tex:37 | Patron PAT-45 reincide. En r01 cambio el verbo, pero el titulo sigue nombrando lo que la cadena conserva ("una representacion multiventana"), no lo que la compuerta puso a prueba: la ida y vuelta por el autoencoder latente. Como el veredicto fue negativo, el lector entiende que fallo la codificacion multiventana, y el objetivo general (l. 32) la sigue usando. La aclaracion de l. 28 llega antes del objetivo y no lo arregla. | Que el titulo nombre el objeto de la prueba, p. ej. "Evaluar si el autoencoder de un modelo de difusion latente conserva los HU de una codificacion multiventana (compuerta *Go/No-Go*)". |
| guia-2 | media | G-A10 | introduccion.tex:72 | "Dos supuestos y dos convenciones sostienen el diseno" presenta una lista cerrada, pero el cap. 3 declara otros supuestos y convenciones que tambien sostienen el diseno: la convencion $h = 2\sigma$, que "fija la escala de todas las perturbaciones y, con ella, la distancia" (cap3 l. 158, 261); los grados equiespaciados en $W_1$ (l. 200, 261), y el supuesto no verificado de que la relacion mascara-artefacto no depende del tipo de implante (l. 180, 261). Relacionado con PAT-22. | Agregar al menos $h = 2\sigma$ y el supuesto mascara-artefacto, o quitar el recuento cerrado y remitir a cap. 3 §Amenazas. |
| guia-3 | media | G-A7 | introduccion.tex:43 | El Obj. 4 "adopta" las metricas de Peters et al. como si pudieran usarse tal cual, pero cap3 l. 215 dice que usarlas para sintesis "exige invertirlas" y deja la definicion operativa en `\GAPDEC`. Ningun objetivo se hace cargo de esa inversion, aunque de ella depende la evidencia del Obj. 3. | Incluir en el Obj. 4 la definicion de la inversion de las metricas, con remision al `\GAPDEC` del cap. 3, o dejarla como limitacion en Alcance. |
| guia-4 | media | G-A7, G-A10 | introduccion.tex:56 | El tercer elemento de la contribucion es "el uso para la sintesis de la codificacion multiventana", pero l. 28 reconoce que ningun objetivo verifica su error de ida y vuelta sin autoencoder, y cap3 l. 172 no ha congelado que codificacion se usa. Es una contribucion anunciada sin evidencia prevista en el bloque (c). | En l. 56, acotar lo que se reclama (remitir a l. 28 y al `\GAPDEC` de cap. 3) o ligarlo a la evaluacion del Obj. 3. |
| guia-5 | media | G-A10, G-T2 | introduccion.tex:67 | Se excluyen las "ablaciones restriccion por restriccion", pero la introduccion nunca enumera las restricciones del muestreador. En cap. 3 el muestreador perturba un unico eje de corredor, y la densidad "no [es] condicionante del muestreo" (cap3 l. 166). El lector no puede saber que queda fuera. | Nombrar las restricciones que se ablacionarian, con fuente del repositorio, o marcar `\GAPDEC{que restricciones cubre la ablacion excluida}`. |
| guia-6 | media | G-A3 | introduccion.tex:52 | La tension de la colocacion dice que la simulacion fisica y la planificacion "no resuelven la colocacion", y dos oraciones despues el planificador de Liu et al. "optimiza una unica trayectoria", o sea, si coloca. Lo que falta es una distribucion de poses comparable con la observada clinicamente, que es lo que el texto concluye al final del parrafo. Tal como esta escrita, la brecha es imprecisa y se contradice. | Formular la tension en la oracion tematica como "no producen una distribucion de poses comparable con la clinica" (azar en Peters, pose unica en Liu). |
| guia-7 | baja | G-T5 | introduccion.tex:28 | El parrafo de apertura discute veredictos, reformulaciones y lo que ningun objetivo verifica antes de que se enuncie ningun objetivo. El lector lee "Objetivo 3 se reformulo" sin saber aun cual es. | Llevar ese contenido despues de la lista, junto al parrafo de l. 46, y dejar en la apertura solo la frase que conecta con el cap. 3 y el `\GAPDEC`. |
| guia-8 | baja | G-A9 | introduccion.tex:50 | Falta el eslabon que explica por que un implante sintetico aliviaria la escasez de volumenes con metal anotados; por ejemplo, que el volumen receptor conserva su anotacion osea y la mascara del implante se conoce. Hoy se pasa de "14 de 75 anotados" a "la motivacion de fondo es ... aumento de datos" sin ese paso. | Una oracion con fuente (TM, CLAUDE.md raiz), o `\GAPDEC` si no esta escrito. |
| guia-9 | baja | G-A10, G-A7 | introduccion.tex:62 | "El segundo corredor bajo S1 se reporta de forma descriptiva" lo presenta como algo que se entrega, pero cap3 l. 164 deja el muestreo de poses en ese corredor sin preinscribir ni correr (`\GAPDATO`). Solo esta medido su eje. | Decir que se reporta (eje medido) o llevar el `\GAPDATO` del cap. 3. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | no cumple, a medias (guia-5); los terminos de r01 guia-7 quedan glosados, y 2.5D se remite al marco teorico |
| G-T3 | cumple ($M$, $B_{\delta}$, $G$, $W_1$ iguales en cap. 3) |
| G-T4 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-T5 | no cumple, a medias (guia-1; baja guia-7); el orden Justificacion/Formulacion cumple con GAP (`\GAPDEC` l. 28) |
| G-T6 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-A1 | cumple con GAP (proposito presente; pregunta e hipotesis bajo el `\GAPDEC` de l. 28, #126) |
| G-A2 | no evaluable (encabezado fuera de alcance) |
| G-A3 | no cumple, a medias (guia-6); la tension esta en l. 52-54 |
| G-A4 | cumple |
| G-A5 | cumple en el alcance revisado |
| G-A6 | cumple |
| G-A7 | no cumple, a medias (guia-1, guia-3, guia-4; baja guia-9). r01 guia-1, 2 y 3 resueltos |
| G-A8 | cumple con GAP (Obj. 1 falsable; Obj. 2, 3 y 4 con `\GAPDEC` en l. 46) |
| G-A9 | cumple con GAP (eslabon necesidad-coherencia en `\GAPDEC` l. 50; orden en `\GAPDEC` l. 28); baja guia-8 |
| G-A10 | no cumple, a medias (guia-2, guia-4, guia-5; baja guia-9). XCIST/CatSim ya tiene razon |
| G-B10 | no evaluable (capitulo2 es esqueleto) |
| G-C4 | cumple (los cuatro objetivos coinciden con cap3 l. 13, fig. 1 y tab:diseno) |
| G-D1, G-D2 | no evaluable (conclusiones es plantilla) |

## Propuestas de criterio
- Un criterio (G §2.3) que pida que cada elemento que la introduccion anuncia como contribucion tenga un objetivo que lo evalue, o se declare no evaluado (ver guia-4).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Titulo de objetivo que nombra lo que la cadena conserva y no lo que la prueba evaluo | G-A7, G-T5 | "Evaluar una representacion multiventana" (se evaluo el autoencoder latente) | PAT-45 |
| Recuento cerrado de supuestos o convenciones que omite otros declarados en el metodo | G-A10 | "Dos supuestos y dos convenciones sostienen el diseno" (falta $h = 2\sigma$) | PAT-22 (variante) / nuevo |
| Contribucion anunciada que ningun objetivo evalua | G-A7, G-A10 | "El tercero es el uso para la sintesis de la codificacion multiventana" | nuevo |
| Exclusion de alcance nombrada con un termino que el documento no define | G-A10, G-T2 | "Ablaciones restriccion por restriccion" sin lista de restricciones | nuevo |
