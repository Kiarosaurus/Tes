# Respuesta del redactor — capitulo1 — r05

Archivo: `overleaf/secciones/capitulo1.tex`. Reportes leidos: `capitulo1-r05-guia.md`, `-estilo.md`,
`-trazabilidad.md`, `-lint.md` (PASA, 0/0/0). Respuesta previa: `capitulo1-r04-respuesta.md`.
Hallazgos sacados por oscilacion: ninguno. Ronda final por tope.

## Altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 (media) | guia | APLICADO | Resuelto junto con S05 en l.126. Se anade el hecho de DEC 2026-09-19, punto 3 ("Su resultado no cambia el diseno del Objetivo 3"): "El veredicto de esa extension se presenta en el capitulo de resultados y, segun la decision que la autorizo, no cambia el diseno del Objetivo~3". Asi la multiplicidad queda acotada a la lectura del veredicto y l.126 concilia con l.110. No se adelanta el veredicto (BITACORA §2 2026-09-29) |
| S05 (media) | estilo | APLICADO | Misma oracion que guia-1. Se quita el contrafactico ("si fuera ... podria haberlo") y el "si" enfatico; queda, como en `capitulo3.tex`:265: "La multiplicidad de siete combinaciones solo podria comprometer ese veredicto si fuera aprobatorio (Seccion amenazas)". PAT-116 |
| S01 (media) | estilo | APLICADO | l.35: la ultima oracion deja de reformular la cifra y da su consecuencia, como `capitulo3.tex`:85: "Por eso el corredor se mide sobre mascaras anatomicas y no con el umbral de 150~HU, que dejaria fuera esa fraccion (Seccion corredor)". El "en la mediana" sigue en la oracion de la cifra. PAT-118 |
| S02 (media) | estilo | APLICADO | l.64: "La MAR reduce el artefacto ..." (termino fijo de `overleaf/CLAUDE.md`: reduccion de artefactos metalicos) y "el sintetizador de este trabajo no hace ni lo uno ni lo otro", que ya no choca con la comparacion prevista con la simulacion fisica al final del parrafo (PAT-39) |
| S03 (media) | estilo | APLICADO | Aperturas de §1.5 ahora: l.120 "Para comparar distribuciones..." (se conserva), l.122 "El Objetivo~3 plantea dos preguntas sobre sus brazos pareados." (se quita "distintas"), l.124 "La prueba de superioridad del Objetivo~3 es la de rangos con signo de Wilcoxon...", parrafo nuevo "La compuerta del Objetivo~1 acompana su error...", l.126 "La proteccion contra ajustar...", l.128 "El error absoluto medio...". Ninguna serie de tres aperturas con la misma formula (PAT-119). La oracion que perdio sujeto pasa a "Para la comparabilidad con el protocolo fisico, el diseno preve dos pruebas..." |
| S04 (media) | estilo | APLICADO | Con guia-3 (baja). El remuestreo del Objetivo 1 sale del parrafo del Objetivo 3 a uno propio de 4 oraciones: "La compuerta del Objetivo~1 acompana su error con un intervalo de confianza por remuestreo de pacientes. El error que decide es la media, sobre los pacientes, del error de cada paciente. [...] Se remuestrean pacientes porque el paciente es la unidad de analisis del Objetivo~1". El `\GAPLIT` de Wilcoxon, TOST y remuestreo queda al final y cubre los dos parrafos (MAPA actualizado) |

## Bajos

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-2 | guia | APLICADO | Figura `fig:mt-conceptos`: fila 2 "metricas de apariencia (Objetivos~3 y~4)"; fila 5 "...; definicion de la distancia en SAP (Objetivo~4)" (`introduccion.tex`:43; BITACORA §2 2026-09-29, W1 se define en el Obj 4). PAT-117 |
| guia-3 | guia | APLICADO | Ver S04: "la media, sobre los pacientes, del error de cada paciente" |
| S06 | estilo | APLICADO | "pregunta si una condicion supera a la otra"; "entre ambas" (BITACORA §2 2026-09-29, "brazo" solo en plural generico) |
| S07 | estilo | APLICADO | l.44: "usa varias ventanas a la vez, una por canal, y evita asi elegir entre conservar el rango y separar los contrastes" |
| S08 | estilo | APLICADO | l.46: "de modo que el metal satura tambien en la ventana ancha" |
| S09 | estilo | APLICADO | l.78: "Esa seccion describe tambien como este trabajo mide el corredor..." |
| S10 | estilo | APLICADO | l.88: "La motivacion de esa fraccion es la heterogeneidad..." |
| T01 | trazabilidad | APLICADO | l.54 abre con la condicion: "En la simulacion bidimensional de De Man et al., el endurecimiento del haz y la dispersion producen rayas muy parecidas entre si \cite{deman1999}" (`deman1999`:201). Para no repetir la semejanza, la ultima oracion queda "Para producir rayas apreciables, en la misma simulacion basta una razon ... de 0.0001, elegida de forma arbitraria", y la del endurecimiento pasa a "En esa simulacion, ..." |

## GAP

Sin GAP nuevos ni cerrados. Totales del lint: lit=4, dato=1, dec=8. Cambia solo la posicion del
`\GAPLIT` de Wilcoxon, TOST y remuestreo (fila de MAPA actualizada). `\GAPDEC` vigentes, sin cambio de
texto en esta ronda: codificacion multiventana y precision del sintetizador; tipo de tornillo del
corredor y de la referencia clinica; dimension angular de la escala de Smith et al. en SAP; fuente y
definicion de la fraccion por zona de densidad; procedimiento de muestreo frente a Lugmayr et al. y
LeFusion; numero de cortes de la entrada 2.5D; agregacion por paciente de poses y regiones de rayas;
equivalencia frente al protocolo fisico o trabajo futuro.

Lint final (`--compilar`): PASA, alta=0 media=0 baja=0; PDF de 107 paginas.

## Escalados

Ninguno.

## Decisiones de redaccion

- Cuando el marco teorico menciona un resultado pendiente (veredicto en el cap. 4) cuya consecuencia
  ya fijo una decision registrada, dice esa consecuencia ("no cambia el diseno del Objetivo 3") en
  lugar de un condicional sobre el resultado.
- Al separar un parrafo con dos funciones o reescribir aperturas, se revisan juntas todas las
  aperturas de la seccion para no crear una serie nueva ("Para ...", "En el Objetivo ...").
- Una semejanza observada solo en una simulacion (De Man et al.) lleva la condicion en la primera
  oracion que la enuncia, y no se repite al final del parrafo.
