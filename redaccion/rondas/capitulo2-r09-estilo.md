# Revision de estilo — capitulo2 — r09

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-01 | media | E-P3 | `overleaf/secciones/capitulo2.tex`:100, oracion 3 | "Se asume que la apariencia del artefacto puede generarse en el dominio de imagen" | La decision del 2026-10-16 exige redactar este punto como limitacion y no afirmar realismo visual. Propuesta: "El sintetizador genera en el dominio de imagen, pero los resultados no permiten afirmar realismo visual." |
| ES-02 | media | E-R2, E-P3, E-M4 | `overleaf/secciones/capitulo2.tex`:112, oracion 2, y :114, oracion 4 | "Queda pendiente el contraste" / "la comparacion con observaciones reales es la del contraste" | El mismo procedimiento aparece primero como pendiente y luego como una comparacion existente. El encargo confirma que se diseno y no se ejecuto. Decirlo una vez en :112: "El contraste de realismo quedo disenado y no se ejecuto; se reserva como trabajo futuro." Eliminar la oracion de :114. |
| ES-03 | media | E-P3, E-M4 | `overleaf/secciones/capitulo2.tex`:124, oracion 5 | "la banda $B_{\delta}$ para los efectos de adquisicion" | La formula presenta la banda como capacidad cumplida y oculta el limite que ahora debe declararse. Propuesta: "la banda $B_{\delta}$, cuyo ancho limita la generacion al entorno local del implante". |
| ES-04 | media | E-R4 | `overleaf/secciones/capitulo2.tex`:126, oraciones 1 y 2 | "El supuesto es que la apariencia del artefacto puede generarse en el dominio de imagen" | Re-apertura: la decision del 2026-10-16 sustituye la repeticion deliberada acordada en r08. El supuesto ya aparece en :100 y la convencion en :104; eliminar estas dos oraciones y conservar el contraste sobre la forma de evaluacion. Patron PAT-46 reincide bajo la decision nueva. |
| ES-05 | media | E-M1, E-O2 | `overleaf/secciones/capitulo2.tex`:118 | "La apariencia sintetizada se comparo" ... "Esa lectura de los desenlaces se fijo despues" | El parrafo mezcla el diseno del contraste, su alcance, el desenlace y su cronologia. Dividir antes de la quinta oracion y abrir el segundo parrafo con: "El desenlace de esa comparacion responde a la pregunta del Objetivo~3." |
| ES-06 | baja | E-R2 | `overleaf/secciones/capitulo2.tex`:116, oracion 1 | "La brecha es la misma tension que plantea la introduccion" | Eliminar: anuncia correspondencia con otra seccion, pero las tres oraciones siguientes ya formulan la brecha. |
| ES-07 | baja | E-R2 | `overleaf/secciones/capitulo2.tex`:120, oracion 5 | "Como declara la justificacion de la introduccion, ningun objetivo aisla estos elementos" | Patron PAT-5 reincide: la apertura anuncia donde se declara el hecho. Propuesta: "Ningun objetivo aisla estos elementos." |
| ES-08 | baja | E-R1 | `overleaf/secciones/capitulo2.tex`:10, oraciones 2 a 4 | "La Seccion" / "La Seccion" / "La Seccion" | Tres oraciones consecutivas repiten la misma apertura. Conservar la primera y abrir las siguientes por su funcion: "La colocacion se revisa en..." y "La representacion de los valores de TC se reune en...". |

TOTAL alta=0 media=5 baja=3

## Impresion general
La seccion conserva una voz sobria, precisa y sin informalidad; las citas suelen llevar verbo, condicion y alcance.
El desajuste dominante esta en los pasajes de realismo: alternan supuesto, capacidad, comparacion pendiente y comparacion existente despues de la decision del 2026-10-16.
Fuera de ese bloque, quedan una metadeclaracion, un parrafo con varias funciones y una repeticion sintactica menor.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un ensayo no ejecutado alterna entre futuro pendiente y comparacion existente | E-P3, E-M4 | "Queda pendiente" / "la comparacion ... es" | nuevo |
| Una decision nueva convierte un supuesto repetido en limitacion, pero el cierre conserva la formula anterior | E-R4 | "El supuesto es que la apariencia ... puede generarse" | PAT-46 |
| La oracion remite a donde se declara un hecho en vez de decirlo directamente | E-R2 | "Como declara la justificacion de la introduccion" | PAT-5 |
