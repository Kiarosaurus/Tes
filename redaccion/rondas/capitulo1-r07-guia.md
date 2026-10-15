# Revision guia CS — capitulo1 — r07

Entrada: `overleaf/secciones/capitulo1.tex`, lint `capitulo1-r07-lint.md` (PASA) y respuesta
`capitulo1-r06-respuesta.md` (sin hallazgos RECHAZADOS). Se leyeron `redaccion/RUBRICA.md`,
`overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§§1--2) y, para coherencia entre bloques,
`introduccion.tex` y `capitulo3.tex`. El foco fue el cierre de los GAPLIT de física de TC,
anatomía, Wasserstein-1, Wilcoxon, TOST, remuestreo y Fisher.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T2, G-B2 | capitulo1.tex:74 | Patron PAT-3 reincide. La fuente nueva describe una capa de hueso compacto, pero el texto no establece que la cortical es esa capa externa; «cortical» sostiene después corredor, brecha y SAP. | Añadir en la primera explicación anatómica una definición explícita y breve que identifique cortical con la capa compacta externa, sin ampliar lo que acredita `standring2020grays`. |
| guia-2 | media | G-T4, G-B3 | capitulo1.tex:48, :128 | El estado del diseño quedó antiguo: el margen ya vale 196.3 HU y el contraste TOST ya se ejecutó sobre 13 pacientes (`capitulo3.tex`:377), pero aquí sigue «aún no medido», «aún sin preinscribir» y permanece la contingencia de plazo. Patrones PAT-11 y PAT-19 reinciden. | Actualizar el estado y remitir al diseño vigente: margen medido, contraste ejecutado y contingencia pendiente solo de cierre formal si la implicancia sigue abierta; retirar o estrechar las marcas envejecidas. |
| guia-3 | media | G-T4, G-B3 | capitulo1.tex:122 | El marco estadístico afirma que las pruebas pareadas usan 14 pacientes, mientras el método vigente usa 13 tras la exclusión documentada (`capitulo3.tex`:327, :375, :377). | Cambiar a 13 y, si hace falta explicar la diferencia, remitir a la exclusión y sensibilidad de `sec:ap-sintesis`. |
| guia-4 | media | G-B2, P-MT1 | capitulo1.tex:106-114 | La predicción de ruido se explica como aparato teórico, pero la predicción $v$, objetivo que usa el sintetizador, solo se define recién en el método (`capitulo3.tex`:202). El bloque de fundamentos no contiene todo el concepto central que el desarrollo usa directamente. | Incorporar en §1.4 la definición mínima de predicción $v$ y su relación con el estado ruidoso, citando `salimans2022progressive`; en el cap. 3 dejar la especificación de que ese es el objetivo usado. |

## Cobertura

| Criterio | Estado |
|---|---|
| G-T1 | no cumple (guia-2, guia-3) |
| G-T2 | no cumple (guia-1) |
| G-T3 | cumple |
| G-T4 | no cumple (guia-2, guia-3) |
| G-T5 | cumple |
| G-T6 | cumple (lint PASA) |
| G-B1 | no cumple (guia-1) |
| G-B2 | no cumple (guia-1, guia-4); la convención bilateral de Fisher cumple con GAP |
| G-B3 | no cumple (guia-2, guia-3) |
| G-B4 | cumple con GAP (suelo de $-1000$ HU y compresión arcoseno hiperbólico) |
| P-MT1 | no cumple (guia-4); los demás elementos usados directamente están descritos |
| P-MT2 | cumple (Figura `fig:mt-conceptos` y remisión al pipeline) |

## Propuestas de criterio

Ninguna.

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Término anatómico central se usa sin identificarlo con la estructura que la fuente sí describe | G-T2, G-B2 | «capa de hueso compacto» y luego «cortical» sin equivalencia explícita | PAT-3 |
| GAP conserva el estado anterior aunque el parámetro ya fue medido y el contraste ejecutado | G-T4 | «margen ... aún sin medir» después de obtener 196.3 HU | PAT-11, PAT-19 |
| Resumen estadístico conserva el tamaño muestral anterior tras cambiar la cohorte del método | G-T4, G-B3 | «14 valores» frente a 13 pacientes vigentes | nuevo |
| Concepto teórico central se define por primera vez dentro del método y no en fundamentos | G-B2, P-MT1 | predicción $v$ definida solo en el capítulo de propuesta | nuevo |
