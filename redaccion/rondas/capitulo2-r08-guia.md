# Revision guia CS — capitulo2 — r08

Contexto: ronda unica del encargo `redaccion/ENCARGO_2026-10-15b.md` (E1 realismo visual en `\REVVISUAL`; E2 cerrar
GAPDEC con `01-decisiones.md` 2026-10-15 (3); E3 GAPLIT donde falte). El texto revisado es el de cierre de r07: aun no
aplica ninguno de los tres puntos del encargo. Lint r08: PASA, GAP lit=1 dato=2 dec=2.
Cruces leidos: `introduccion.tex` (tension l. 58, resultado del Obj 3 l. 50-52, supuestos l. 84), `capitulo3.tex`
(l. 262 y 499, banda de 12 mm), `anexos.tex` (Tabla A.1), DEC 2026-10-15 (3) ptos 1, 8 y 9, implicancias #179, #180, #193.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-B7, P-EA3, OC-2 | capitulo2.tex:108, 110, 114 | Patron PAT-19 reincide: el `\GAPDEC` de l. 114 (#179) sigue abierto aunque DEC 2026-10-15 (3) pto 9 ya lo decide. Mientras tanto la brecha (l. 108: "ninguno de los tres enfoques ... produce a la vez") y el aporte (l. 110-114) se formulan sin tener en cuenta el precedente mas cercano del sintetizador: la sintesis aprendida de componentes de artefacto como paso intermedio de la MAR no pareada (U-DuDoNet, PND-Net). Con eso se ataca un vacio generico y no la limitacion concreta de esas soluciones | Retirar el `\GAPDEC` de l. 114. En §Simulacion o en l. 114, presentar U-DuDoNet y PND-Net desde sus fichas (`lyu2021ududonet`, `xia2024pndnet`, ya en `referencias.bib`), con lo que hacen y que su sintesis no se evalua como producto. Despues, acotar la brecha de l. 108 con la formula del pto 9: sintesis del implante y de su artefacto local, condicionada por la geometria y la pose de un implante colocado por un muestreador quirurgicamente restringido, y evaluada como producto frente a un protocolo fisico. Para no romper G-B10, introduccion:58 debe recibir la misma formula en su r08. Antes de agregar oraciones a l. 108 (ya tiene 7), partir el parrafo (PAT-58) |
| guia-2 | media | G-T6, G-T4 | capitulo2.tex:56 | Patron PAT-19 reincide: Yang et al. aparece sin `\cite`, con un `\GAPDEC` de clave pendiente que DEC 2026-10-15 (3) pto 8 resuelve (`yang2022computeraided`, presente en `referencias.bib`; #180 CERRADA) | Sustituir la marca por `\cite{yang2022computeraided}` y cotejar con la ficha `yang2022computeraided` la descripcion "sobre 10 pelvis, un unico canal optimo ... a traves de S1" |
| guia-3 | media | OC-2 (`\REVVISUAL`) | capitulo2.tex:104, 106; anexos.tex:29; capitulo2.tex:94, 116 | Ningun pasaje esta envuelto en `\REVVISUAL`, aunque el capitulo trata el realismo del artefacto sintetico o depende de el (#193 ABIERTA). Los que lo tratan de forma directa: l. 104 ("Queda pendiente el contraste de realismo" + `\GAPDATO`), l. 106 (ultima frase: "esa comparacion con observaciones reales es la del contraste de realismo") y la celda propia de la Tabla A.1 ("contraste de realismo pendiente"). Los que dependen de el: el supuesto de generacion en el dominio de imagen en l. 94 (dos ultimas oraciones) y l. 116 (dos primeras), y la celda "Supuesto: ..." de anexos:29 | Envolver en `\REVVISUAL{...}` las tres menciones directas, con el `\GAPDATO` dentro. Decidir con el mismo criterio las del supuesto (l. 94, l. 116, celda de la tabla) y, si se envuelven, que sea en los tres lugares por igual (decision de bitacora 2026-09-30: el supuesto se enuncia igual en cuerpo, tabla y cierre). No escribir nada de #193 como hecho |
| guia-4 | media | G-T4 | capitulo2.tex:94 (tambien 104 y 108) | Patron PAT-116 reincide. La comparacion con el protocolo fisico "ya ejecutada y no concluyente ... es la que puede contradecir ese supuesto" sigue en condicional sobre una prueba ya cerrada, cuya lectura fija DEC 2026-10-15 (3) pto 1: la equivalencia no se sostiene, la amplitud es menor y la lectura se fijo despues de ver el resultado. Ademas, el capitulo da el desenlace sin "a la baja", que la introduccion (l. 52) si da (PAT-31). En la bisagra (l. 116), el lector no sabe en que estado queda el supuesto del que "descansa la brecha" | En l. 94, decir que la comparacion resulto no concluyente, con amplitud del sintetizador menor que la del protocolo fisico, sin cifras, y que esa lectura es posterior al resultado (pto 1), con remision al capitulo de resultados. Lo que ese resultado implica para el supuesto depende de #193: dejarlo dentro del `\REVVISUAL` de guia-3, sin afirmar que lo contradice ni que lo sostiene. Alinear la forma breve de l. 104 y l. 108 ("no concluyente, a la baja") |
| guia-5 | baja | G-B8 | anexos.tex:19-27 | Una vez aplicado guia-1, el precedente que acota la brecha (sintesis aprendida de artefacto en MAR no pareada) no tendria fila en la tabla comparativa, aunque es el mas proximo al sintetizador en la columna "Fuera del objeto" | Valorar una fila para U-DuDoNet o PND-Net, con enfoque, lo que hacen fuera del objeto y resultado con su condicion, desde la ficha. Si no se agrega, decir en l. 104 por que no esta |
| guia-6 | baja | G-T4 | capitulo2.tex:98 | Patron PAT-31 reincide: "el artefacto real medido en la cohorte queda dentro de esa banda" pierde la condicion con que capitulo3.tex:499 lo dice ("no se separa del control nulo mas alla de 10 mm"). La frase tambien choca en apariencia con l. 96 ("la banda trunca por diseno los efectos ... lejos del metal") | Dar la condicion: "en componentes del tamano de un tornillo, el artefacto real medido no se separa del control nulo mas alla de 10 mm (Seccion sec:v2)", y conservar la truncacion de l. 96 como limite de diseno. Si la autora considera que la suficiencia de la banda depende de #193, va dentro de `\REVVISUAL` |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | cumple |
| G-T3 | cumple |
| G-T4 | no cumple (guia-2, guia-4, guia-6) |
| G-T5 | cumple (l. 10 describe el orden real de las secciones) |
| G-T6 | no cumple (guia-2: Yang et al. sin `\cite`) |
| G-B5 | cumple (carencias por objetivo: l. 30, 74, 76-78, 90-92) |
| G-B6 | cumple (l. 12 declara una revision narrativa y dirigida, y su procedimiento) |
| G-B7 | no cumple (guia-1) |
| G-B8 | cumple (Tabla A.1 con fila propia; guia-5 es una mejora) |
| G-B9 | cumple |
| G-B10 | cumple por ahora: l. 108 = introduccion:58. Hay riesgo al aplicar el pto 9: tienen que cambiar los dos con la misma formula (guia-1) |
| P-EA1 | cumple (prepublicaciones senaladas; resumen de Zhang et al. 2026 declarado) |
| P-EA2 | cumple |
| P-EA3 | no cumple (guia-1: el aporte no se acota frente a la MAR no pareada) |
| OC-2 (`\REVVISUAL`, GAP vigentes) | no cumple (guia-1, guia-3) |

## Propuestas de criterio
- Hay un criterio transversal de "pasaje marcado para revision con el asesor" (`\REVVISUAL`) que hoy solo vive en
  `overleaf/CLAUDE.md` regla 2. Mientras exista, conviene darle un ID en la rubrica (p. ej., OC-2b) para que los
  revisores lo citen sin ambiguedad.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que declara pendiente una decision ya fijada en DEC | G-T4, OC-2 | "\GAPDEC{clave bibliográfica de Yang et al. 2022 pendiente de la autora}" | PAT-19 |
| Condicional sobre una prueba ya cerrada cuya lectura fija una DEC | G-T4 | "ya ejecutada y no concluyente ... es la que puede contradecir ese supuesto" | PAT-116 |
| El desenlace resumido pierde la direccion que la introduccion y la DEC dan | G-T4 | "no concluyente" (sin "a la baja") | PAT-31 |
| Una implicancia ABIERTA de alcance transversal (#193) sin marca de revision en los pasajes que dependen de ella | OC-2 | "Queda pendiente el contraste de realismo" sin `\REVVISUAL` | PAT-123 |
| Brecha formulada contra enfoques amplios, sin el precedente concreto que la propia DEC ordena nombrar | G-B7, P-EA3 | "Ninguno de los tres enfoques revisados ... produce a la vez" | nuevo |

TOTAL alta=1 media=3 baja=2
