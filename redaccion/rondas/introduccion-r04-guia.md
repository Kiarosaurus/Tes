# Revision guia CS — introduccion — r04

Alcance acotado por la autora: `introduccion.tex` l. 23-82 (Objetivos, Justificacion, Alcance y
limitaciones). Encabezado (l. 1-17) y Formulacion del problema (l. 19-21) quedan fuera de alcance (#126),
igual que los hallazgos del lint en l. 7, 13 y 21. Secciones cruzadas leidas: `capitulo3.tex` (l. 56-265),
`capitulo2.tex` (sigue siendo esqueleto) y `docs/00-tesis.md` (Fuera de alcance). Respuesta r03 leida:
guia-1 (sintetizador aprendido frente a simulacion fisica) y guia-5 (razon del tornillo iliosacro) quedaron
ESCALADOS con `\GAPDEC`. No se reabren. Los demas hallazgos de r03 (guia-2, 3, 4, 6, 7, 8, 9) estan
resueltos. Esta ronda no tiene hallazgos altos ni medios. Los que quedan son bajos y casi todos son
reincidencias parciales de patrones de la bitacora.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | baja | G-A10, G-A7 | introduccion.tex:60 | Patron PAT-49 reincide (parcial). El tercer elemento es "la codificacion multiventana ... junto con la banda $B_{\delta}$", pero la clausula final dice que el trabajo "solo aporta su uso como codificacion para generar". No queda claro si la banda es parte del aporte. Si lo es, ningun objetivo la aisla, y l. 78 la trata como convencion sin calibrar. | Decir si la banda forma parte del aporte. Si lo es, extender "ningun objetivo aisla ese aporte" a la banda, con la misma razon (el Obj. 3 evalua el sintetizador completo). |
| guia-2 | baja | G-A10 | introduccion.tex:82 | Patron PAT-38 reincide. Se enumeran los tres desplazamientos de dominio, pero no su efecto sobre el resultado. El cap. 3 (l. 263) si lo dice: "limitan ... la transferencia de lo aprendido sobre metal real a los tornillos parametricos". La decision de r03 pide que cada limitacion resumida lleve su efecto. | Media oracion con ese efecto, tomada de cap3 l. 263. |
| guia-3 | baja | G-T2 | introduccion.tex:58, 66, 78 | Patron PAT-3 reincide. Hay tres terminos que aparecen sin definirse en la introduccion. "Desplazamientos de dominio" se usa en l. 58 y solo se detalla en l. 82. "Segundo corredor bajo S1" (l. 66): el lector no sabe que existe un segundo corredor. "Preinscripcion del muestreador" (l. 78; antes solo aparece dentro del GAP de l. 46): l. 62 describe el concepto sin nombrarlo. | Nombrar la preinscripcion en l. 62 ("esa fijacion previa, la preinscripcion, ..."). Poner una aposicion corta para el segundo corredor. En l. 58, remitir a l. 82 o adelantar una glosa. |
| guia-4 | baja | G-T2 | introduccion.tex:28, 43, 76 | Patron PAT-14 reincide. "Componentes" tiene tres sentidos en la seccion: piezas de la cadena (l. 28), partes de SAP (l. 43) y objetos metalicos (l. 76). La decision de r03 reserva la palabra para los dos primeros sentidos de esa lista (piezas de la cadena y objetos metalicos), no para SAP. | Para SAP, usar otra palabra ("SAP reune tres medidas" o "tres partes") o ampliar la decision. Ojo: cap3 l. 189 usa el mismo termino. |
| guia-5 | baja | G-A7 | introduccion.tex:66, 82 (frente a l. 41) | El alcance presenta las observaciones reales de artefacto como fuente de datos y dice que "sirven para comparar la apariencia". Pero el Obj. 3 solo nombra dos comparaciones (copia y pegado, protocolo fisico). El cap. 3 (l. 215) tiene una tercera comparacion con observaciones reales, marcada con `\GAPDEC`. El lector no sabe que objetivo usa esas observaciones. | En el Obj. 3, una clausula que diga que la apariencia tambien se contrasta con observaciones reales, con el mismo `\GAPDEC` de cap3 l. 215 (PAT-31). |
| guia-6 | baja | G-A10 | introduccion.tex:66 | El cuarto punto del alcance ("la sintesis opera por parches alrededor del implante y en el dominio de imagen") no da razon. La del dominio de imagen esta en l. 46 (veredicto del Obj. 1). La de operar por parches no aparece en ninguna parte de la seccion. | Remitir a l. 46 para el dominio de imagen. Dar la razon de los parches con fuente (p. ej., la region de generacion $G$ y la preservacion fuera de ella, cap3 l. 172) o `\GAPDEC`. |
| guia-7 | baja | G-A10, G-A9 | introduccion.tex:62 | La "justificacion metodologica" se apoya en un resultado propio (el veredicto del Obj. 1) y lo generaliza: "el veredicto no se limita a una sola arquitectura". Pero el segundo latente se examino despues del veredicto y sobre los mismos pacientes de prueba (cap3 l. 255, 265), y su resultado aun no esta en el documento (cap3 l. 75). La salvedad de l. 46 no llega a esta oracion. | Acotar a "los dos latentes examinados", con la condicion de que el segundo se examino despues del veredicto. O remitir la generalizacion a resultados. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | cumple a medias (bajas guia-3, guia-4). "Cortical" sigue sin glosa: no hay fuente (r03 guia-7, no se reabre) |
| G-T3 | cumple ($M$, $B_{\delta}$, $G$ y $W_1$ se usan igual que en el cap. 3; $h$ y $\sigma$ solo aparecen dentro de un GAP) |
| G-T4 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-T5 | cumple con GAP (orden Justificacion/Formulacion en el `\GAPDEC` de l. 28) |
| G-T6 | no evaluable (dominio de `auditor-trazabilidad`) |
| G-A1 | cumple con GAP (el proposito esta; la pregunta queda bajo el `\GAPDEC` de l. 28, #126) |
| G-A2 | no evaluable (encabezado fuera de alcance) |
| G-A3 | cumple con GAP. La tension de l. 54-56 queda con el `\GAPDEC` del sintetizador aprendido (r03 guia-1, escalado). PAT-55 no reincide: el hecho se enuncia y la razon no se inventa |
| G-A4 | cumple con GAP (mismo GAP; el desafio fisico de l. 56 esta) |
| G-A5 | cumple en el alcance revisado |
| G-A6 | cumple (objetivo general y cuatro especificos resaltados) |
| G-A7 | cumple a medias (bajas guia-1, guia-5). El Obj. 4 y la codificacion sin autoencoder cumplen con GAP |
| G-A8 | cumple con GAP (el Obj. 1 es falsable; los Obj. 2, 3 y 4 tienen `\GAPDEC` en l. 48; la dependencia del plazo esta en l. 82) |
| G-A9 | cumple con GAP (eslabon necesidad-coherencia en el `\GAPDEC` de l. 52; orden en l. 28; baja guia-7) |
| G-A10 | cumple a medias (bajas guia-1, guia-2, guia-6, guia-7). Las cuatro tareas excluidas tienen su razon. Ya no hay recuentos cerrados (PAT-54 no reincide). La razon del implante esta en `\GAPDEC`. La ablacion tiene su GAP (PAT-50 cumple con GAP). XCIST distingue la opcion adoptada (PAT-51 no reincide) |
| G-B10 | no evaluable (capitulo2 es esqueleto) |
| G-C4 | cumple (los objetivos coinciden con cap3 `tab:diseno`; el titulo de `sec:obj1` ya lo escalo el redactor) |
| G-D1, G-D2 | no evaluable (conclusiones es plantilla) |

## Propuestas de criterio
- Sin propuestas nuevas. Sigue vigente la de r03: que la tension justifique cada componente de la
  contribucion frente a la alternativa que la propia tesis usa como comparacion.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Contribucion anunciada que ningun objetivo evalua, sin decirlo (aqui, la banda del tercer elemento) | G-A7, G-A10 | "la codificacion multiventana usada para generar, junto con la banda" | PAT-49 |
| Amenaza o limitacion resumida sin su efecto sobre el resultado | G-A10 | "Entre el entrenamiento del sintetizador y la sintesis hay tres desplazamientos de dominio" | PAT-38 |
| Termino tecnico usado antes de su definicion | G-T2 | "uno de los desplazamientos de dominio del sintetizador" (l. 58) | PAT-3 |
| Un termino designa varias cosas en la misma seccion | G-T2 | "SAP reune tres componentes" junto a "componentes de la cadena" | PAT-14 |
| Dato o comparacion presentada en Alcance que ningun objetivo nombra como uso | G-A7 | "Por eso sirven para comparar la apariencia" (Obj. 3 no las nombra) | nuevo |
