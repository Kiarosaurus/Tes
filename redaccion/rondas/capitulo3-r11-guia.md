# Revision guia CS — capitulo3 — r11

Leidos: `RUBRICA.md`, `overleaf/CLAUDE.md`, `BITACORA.md` (§1 y §2), `capitulo3-r10-respuesta.md`, `capitulo3-r10-guia.md`,
`capitulo3-r11-lint.md` (PASA). Para cruces: `introduccion.tex` l. 36-65. Cotejo puntual: `a17_cotejo_resultado.md` l. 44-47,
`docs/ESTADO.md` l. 383-391. Los diecinueve hallazgos de r10 quedaron aplicados o escalados con `\GAPDEC`, y no se reportan de
nuevo. Lo de guia-15 (normalidad) se reabre abajo con un argumento nuevo.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C7, G-C6 | capitulo3.tex:350, :354 (frente a :246, :188, :328) | Patron PAT-54 reincide. La l. 328 promete que las decisiones tomadas despues de ver datos "se enumeran" en amenazas, pero la l. 350 cierra el recuento en "Tres decisiones" del Obj 2 y omite la escala de lectura de Wasserstein-1, "elegida despues de conocer la distancia" (l. 246). Para el Obj 3, la l. 354 omite el percentil 5 de la regla del suelo, "una eleccion hecha despues de ver su distribucion" (l. 188). | Quitar el recuento cerrado o completarlo. Anadir la escala de lectura post hoc (Obj 2) y el percentil 5 de la regla del suelo (Obj 3), cada uno con su efecto sobre la lectura |
| guia-2 | media | G-C6, G-C8 | capitulo3.tex:210, :318 frente a :262, :268 | El margen $\Delta$ se calibra solo en receptores "cuyo corredor admite el tornillo" (l. 210), y se excluye uno de 1.6 mm (l. 318). La prueba, en cambio, incluye tres corredores de 3.1 a 4.7 mm, mas angostos que el tornillo (l. 268), y solo excluye al paciente sin eje medido (l. 262). No se da regla de elegibilidad del receptor por ancho del corredor, y $\Delta$ se mide en una condicion distinta de la poblacion del contraste primario. | Enunciar la regla de elegibilidad de receptores en validacion y en prueba, o un `\GAPDEC` si no esta fijada. Declarar en validez de la conclusion que $\Delta$ se calibro solo sobre corredores que admiten el tornillo |
| guia-3 | media | G-T2 | capitulo3.tex:214 frente a :318 | Patron PAT-31 reincide. Para el mismo punto de control, la l. 214 da "324 HU ... de rango entre semillas" sin decir de que magnitud (en `a17_cotejo_resultado.md`:46 es del cotejo del perfil radial). La l. 318 da $s_{\mathrm{sem}} = 188.7$ HU, tambien "rango ... entre sus 5 semillas", pero de la *streak amplitude*. Un lector que coteje el margen ve dos rangos entre semillas distintos para el mismo modelo. | Nombrar en la l. 214 la magnitud y la agregacion del 324/162 (perfil radial del cotejo) para distinguirlo de $s_{\mathrm{sem}}$ |
| guia-4 | baja | G-T2 | capitulo3.tex:212, :276 | Patron PAT-14 reincide. "Como referencia se usan", "Con un solo paciente de referencia" y "el umbral de la referencia del cotejo" usan "referencia" para el paciente de validacion del cotejo. La decision §2 del 2026-09-30 reserva "referencia" para la referencia clinica, y "referencia de realismo" ya nombra otro conjunto, el de prueba. | "Los tornillos reales del cotejo" / "un solo paciente con tornillos reales" (como en la l. 310) |
| guia-5 | baja | G-T2 | capitulo3.tex:204 frente a :262 | Patron PAT-3 reincide. "La sintesis sobre pelvis sin metal" se usa en la l. 204 como evaluacion con nombre, sin `\ref`, y se define en negrita en la l. 262. | Anadir `(Seccion~\ref{sec:ap-sintesis})` en la l. 204 |
| guia-6 | baja | P-MM3, G-C2 | capitulo3.tex:206 | Uno de los dos candidatos es "el del paso 140 000 del primero" (entrenamiento), que el capitulo nunca describe. No se dice su duracion (144 500 pasos) ni que tiene la misma configuracion que el segundo y solo difiere en duracion (`docs/ESTADO.md`:383-388). | Una clausula que diga duracion y configuracion del primer entrenamiento |
| guia-7 | baja | P-MM3 | capitulo3.tex:137 frente a :133 | El espesor de arandela de 1.5 mm y la canulacion se presentan como parametros del modelo, pero la l. 133 dice que no entran en la corrida final. | Decir que esos dos parametros solo valen para las variantes no programadas |
| guia-8 | baja | G-C8 | capitulo3.tex:316 | Re-apertura: guia-15 de r10 no se aplico en su primer punto "porque ninguna fuente lo enuncia". OC-2 da la via para eso: marcar lo que falta, no callarlo. El IC con *t* sobre 13 diferencias pareadas descansa en un supuesto que el diseno congelado no registra, y la misma regla 1 que impide afirmarlo obliga a marcarlo. | `\GAPDEC` (o `\GAPLIT`) sobre el supuesto distribucional del IC con *t* de la comparacion de equivalencia |
| guia-9 | baja | G-C8 | capitulo3.tex:314 | "Se reportan el tamano de efecto y su IC" no dice que medida de tamano de efecto se usa para el Wilcoxon pareado. | Nombrar la medida o un `\GAPDEC` |
| guia-10 | baja | P-MM1 | capitulo3.tex:258 | "la de las otras dos metricas, despues de las dos evaluaciones en que se miden" puede leerse como inversion decidida despues de ver datos, cuando la l. 278 solo la describe mas abajo. | "y la de las otras dos, en la Seccion~\ref{sec:ap-reconstruccion}, tras describir las dos evaluaciones" |
| guia-11 | baja | G-C7 | capitulo3.tex:270 | En la prueba pareada, el sintetizador se resume sobre todos los cortes que toca $G$ y el protocolo fisico sobre uno de cada dos. La diferencia de soporte entre los valores pareados no figura en amenazas. | Una oracion en validez de la conclusion, o decir por que el submuestreo uniforme no sesga la mediana |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | no cumple (guia-3, guia-4, guia-5) |
| G-T3 | cumple ($s_{\mathrm{sem}}$, $r_{\mathrm{rep}}$ y *t* de texto resuelven el choque de r10) |
| G-T4 | cumple con GAP (las cifras son de `auditor-trazabilidad`) |
| G-T5 | cumple (§Apariencia partida en subsubsecciones por funcion; $\Delta$ remitido a `sec:ap-analisis`) |
| G-T6 | cumple (lint sin citas indefinidas) |
| G-A7 (cruce) | cumple con GAP del lado del cap. 3: la reconstruccion de implantes reales se declara analisis descriptivo y #90 tiene su `\GAPDEC`. Cruce para `introduccion`: la l. 41 no nombra la reconstruccion |
| G-A8 (cruce, lado del bloque c) | cumple con GAP (`\GAPDEC` de los desenlaces del TOST) |
| G-C1 | cumple con GAP (razon de $\Delta$ dada; regla del suelo con `\GAPDEC`) |
| G-C2 | no cumple (guia-6) |
| G-C3 | cumple |
| G-C4 | cumple con GAP (`\GAPDEC` de la pose sin perturbar). Cruce no evaluable aqui: `introduccion.tex`:48 ($\Delta$ "aun sin medir") y :56 ("sobre las poses del muestreador") contradicen el capitulo; se reportan en su seccion |
| G-C5 | cumple con GAP (cabeza y salto en el borde de $G$ con `\GAPDEC`; variantes no programadas declaradas) |
| G-C6 | no cumple (guia-1, guia-2) |
| G-C7 | no cumple (guia-1): los cuatro tipos son explicitos y no pro forma, y hay amenaza nueva por la pose sin perturbar, pero el recuento de decisiones posteriores a los datos esta incompleto |
| G-C8 | no cumple (guia-2, guia-8, guia-9) |
| G-C9 | cumple: el protocolo fisico es la linea base fuerte; copia y pegado es control de cordura declarado |
| P-MM1 | no cumple (guia-10, leve) |
| P-MM2 | cumple (la Figura 3.1 distingue la pose de la evaluacion) |
| P-MM3 | no cumple (guia-6, guia-7) |

## Propuestas de criterio
- Se repite la de r10: coherencia entre el diseno descrito y el registro congelado (`diseno_A.md` §0) como criterio propio del bloque (c).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Recuento cerrado de decisiones post hoc en amenazas que omite otras declaradas en el metodo | G-C7 | "Tres decisiones, en cambio, se tomaron despues de ver datos" (falta escala de lectura) | PAT-54 |
| Dos cifras con el mismo nombre ("rango entre semillas") para magnitudes distintas del mismo modelo | G-T2 | "324 HU frente a 162 HU de rango entre semillas" / $s_{\mathrm{sem}} = 188.7$ | PAT-31 |
| Parametro de calibracion medido en una subpoblacion que la poblacion de prueba no respeta, sin regla escrita | G-C6, G-C8 | $\Delta$ en "corredor que admite el tornillo"; la prueba incluye corredores de 3.1 mm | nuevo |
| Termino reservado reutilizado para un conjunto nuevo | G-T2 | "Con un solo paciente de referencia" (reservado a la referencia clinica) | PAT-14 |
| Evaluacion con nombre usada antes de su definicion, sin remision | G-T2 | "El segundo actua en la sintesis sobre pelvis sin metal" (l. 204) | PAT-3 |
