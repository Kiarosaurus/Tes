# Revision guia CS — capitulo3 — r20

Entrada: `overleaf/secciones/capitulo3.tex`, lint `capitulo3-r20-lint.md` (PASA) y respuesta
`capitulo3-r19-respuesta.md` (sin hallazgos RECHAZADOS). Se leyeron `redaccion/RUBRICA.md`,
`overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§§1--2) y, para coherencia entre bloques,
`introduccion.tex`, `capitulo1.tex` y `capitulo4.tex`. El foco fue el cierre del GAPLIT de la
parametrización de predicción $v$.

## Hallazgos

Sin hallazgos nuevos. La definición de $v$ en `capitulo3.tex`:202 identifica el estado ruidoso,
la imagen limpia, el ruido y la relación entre los coeficientes; además separa correctamente la
definición matemática respaldada por la fuente de cualquier afirmación de desempeño en TC.

## Cobertura

| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | cumple |
| G-T3 | cumple ($z_t$, $x$, $\epsilon$, $\alpha_t$ y $\sigma_t$ tienen un único sentido local) |
| G-T4 | cumple con GAP |
| G-T5 | cumple |
| G-T6 | cumple (lint PASA) |
| G-C1 | cumple con GAP |
| G-C2 | cumple con GAP; la predicción $v$ ya está definida y citada |
| G-C3 | cumple |
| G-C4 | no cumple en el cruce con la introducción; desfase ya escalado como `capitulo3-r19-guia.md` guia-4, sin hallazgo nuevo en r20 |
| G-C5 | cumple con GAP |
| G-C6 | cumple |
| G-C7 | cumple con GAP |
| G-C8 | cumple con GAP |
| G-C9 | cumple |
| P-MM1 | cumple |
| P-MM2 | cumple (Figura `fig:pipeline`) |
| P-MM3 | cumple con GAP |

## Propuestas de criterio

Ninguna.

## Patrones

sin patrones
