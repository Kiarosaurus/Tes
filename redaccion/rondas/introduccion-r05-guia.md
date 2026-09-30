# Revision guia CS — introduccion — r05

La autora acoto el alcance a `introduccion.tex` l. 23-84: Objetivos, Justificacion y Alcance y
limitaciones. El encabezado (l. 1-17) y la Formulacion del problema (l. 19-21) quedan fuera (#126),
igual que los hallazgos del lint en l. 7, 13 y 21. Secciones cruzadas leidas: `capitulo3.tex`
(l. 56-265), `capitulo2.tex` (sigue siendo esqueleto: solo titulos), `docs/00-tesis.md` (Fuera de
alcance) y `tesis/main.tex` l. 77. Tambien lei la respuesta r04. Resueltos: guia-1, 2, 3, 5 y 7. guia-6
se aplico en parte; la razon de trabajar por parches no tiene fuente y no se inventa, asi que no se
reabre. guia-4 ("componentes" de SAP) quedo NO APLICADO y escalado a la autora, y no se reabre.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-A7, G-A9 | introduccion.tex:62 | La "justificacion metodologica" presenta como "hallazgo del Objetivo 1" que los autoencoders "se definen sobre rangos de intensidad que excluyen el hueso denso y el metal". El diseno del Obj. 1 (cap3 l. 60-75, `tab:diseno`) no produce esa evidencia: mide MAE en hueso contra 25 HU. Solo la extension a Guo et al. usa una cota por saturacion al rango del modelo. Para el autoencoder de Stable Diffusion, el rango es una explicacion y no lo que el objetivo mide. Ademas, cap3 l. 75 deja ambos veredictos para resultados. Asi, la justificacion descansa en una afirmacion que ningun objetivo verifica. | Enunciar el hallazgo en los terminos que el Obj. 1 mide: ninguna combinacion baja de 25 HU, y el autoencoder de TC ya lo supera por saturacion a su rango. Para el mecanismo, remitir a resultados. Si se conserva, marcarlo como interpretacion. |
| guia-2 | baja | G-A7 | introduccion.tex:66 | Patron PAT-57 reincide. El alcance dice que el eje del segundo corredor bajo S1 esta medido y deja pendiente, con `\GAPDATO`, la preinscripcion y la corrida de su muestreo. Ningun objetivo nombra ese muestreo como uso: el Obj. 2 (l. 39) solo compara en S1. El lector no sabe si esos resultados descriptivos (cap3 l. 164) pertenecen al Obj. 2 o quedan fuera. | En el Obj. 2, una clausula que diga que el segundo corredor se reporta de forma descriptiva, o bien declararlo fuera del objetivo. |
| guia-3 | baja | G-T2 | introduccion.tex:46, 48 | Patron PAT-3 reincide. "Regla de la compuerta" (l. 46) y "regla operativa" (l. 48) se usan como algo distinto del "criterio de 25 HU", pero la introduccion no dice que es la regla: aprueba si alguna de las seis combinaciones baja del criterio, y hay un orden a priori (cap3 l. 71). Sin eso, la distincion de l. 48 entre la regla, escrita despues de la exploracion, y el criterio, anterior a ella, no se puede verificar. | Una aposicion corta en l. 37 o l. 48 que diga en que consiste la regla (seis combinaciones, aprueba si alguna cumple el criterio) y que remita a `sec:obj1`. |
| guia-4 | baja | G-T2 | introduccion.tex:37, 82 | En la seccion aparecen dos grupos de 34 pacientes: los "34 pacientes de prueba" del Obj. 1 (l. 37) y los "11 de 34 pacientes con objetos no ortopedicos" del Obj. 2 (l. 82). El texto no dice si son el mismo conjunto, y un lector los identificara. | En l. 82 precisar el universo ("de los 34 pacientes de la cohorte del Objetivo 2 con objetos no ortopedicos"). |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | cumple a medias (bajas guia-3 y guia-4). "Componentes" de SAP esta escalado a la autora (r04 guia-4) y no se reabre. "Cortical" sigue sin glosa por falta de fuente (r03), y tampoco se reabre |
| G-T3 | cumple: $M$, $B_{\delta}$, $G$ y $W_1$ se usan igual que en el cap. 3 |
| G-T4 | no evaluable (lo revisa `auditor-trazabilidad`). Aviso para estilo y traza, sin contarlo como hallazgo: l. 84 dice "menos frecuentes ... solo este ultimo desplazamiento esta cuantificado" sin dar 0.62 frente a 1.40 (cap3 l. 182). Seria PAT-8, criterio E-P4 |
| G-T5 | cumple con GAP: el orden Justificacion/Formulacion queda en el `\GAPDEC` de l. 28 |
| G-T6 | no evaluable (lo revisa `auditor-trazabilidad`) |
| G-A1 | cumple con GAP: el proposito esta; la pregunta queda bajo el `\GAPDEC` de l. 28 (#126) |
| G-A2 | no evaluable (encabezado fuera de alcance) |
| G-A3 | cumple con GAP: tension en l. 54-56 con el `\GAPDEC` del sintetizador aprendido. PAT-55 no reincide |
| G-A4 | cumple con GAP: el desafio fisico esta en l. 56 |
| G-A5 | cumple en el alcance revisado: el problema (escasez de datos y enfoques que no producen poses y apariencia a la vez) no es el metodo |
| G-A6 | cumple: objetivo general y cuatro especificos, resaltados |
| G-A7 | cumple a medias (media guia-1, baja guia-2). PAT-49 no reincide, porque los tres elementos de la contribucion dicen que objetivo los evalua o que ninguno los aisla. El Obj. 3 nombra ya las observaciones reales, con GAP. El Obj. 4 cumple con GAP |
| G-A8 | cumple con GAP: el Obj. 1 es falsable, y los Obj. 2, 3 y 4 tienen su `\GAPDEC` en l. 48. PAT-52 no reincide |
| G-A9 | cumple con GAP (el eslabon necesidad-coherencia esta en el `\GAPDEC` de l. 52), salvo guia-1 |
| G-A10 | cumple. Se nombran las cuatro tareas excluidas, cada una con su razon (PAT-44, 50 y 51 no reinciden). Supuestos y convenciones van sin recuento cerrado y con remision a `sec:amenazas` (PAT-54 no reincide). Cada limitacion lleva su efecto (PAT-38 no reincide) |
| G-B10 | no evaluable: capitulo2 es esqueleto |
| G-C4 | cumple: los objetivos coinciden con cap3 `tab:diseno`. La comparacion con observaciones reales falta en la tabla, pero tiene `\GAPDEC` en los dos capitulos |
| G-D1, G-D2 | no evaluable: conclusiones sigue siendo plantilla |

## Propuestas de criterio
- Sin propuestas nuevas. Sigue vigente la de r03: que la tension justifique cada componente de la
  contribucion frente a la alternativa que la propia tesis usa como comparacion.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un resultado propio se enuncia en terminos (mecanismo) que el diseno del objetivo no mide | G-A7 | "El hallazgo del Objetivo 1 es que ... se definen sobre rangos de intensidad" | nuevo |
| Dato o comparacion presentada en Alcance que ningun objetivo nombra como uso | G-A7 | "Su eje esta medido, pero el muestreo de poses en el no se ha ejecutado" | PAT-57 |
| Termino tecnico usado sin definir en la seccion | G-T2 | "Su regla operativa se escribio despues de una exploracion" | PAT-3 |
