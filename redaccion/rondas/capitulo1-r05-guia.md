# Revision guia CS — capitulo1 — r05

Lecturas cruzadas: `capitulo3.tex` (l.17-75 cadena y compuerta; l.81-89 corredor; l.170-180 sintetizador;
l.187-205 SAP y W1; l.223-247 apariencia y diseno; l.249-265 amenazas), `introduccion.tex` (l.36-48,
objetivos y falsabilidad), `docs/01-decisiones.md` 2026-09-19, `docs/04-implicancias.md` #93.
Respuesta previa: `capitulo1-r04-respuesta.md`. Verificadas las correcciones r04: guia-1 (l.35, 0.42 con
cohorte, recorte, "en la mediana" y "del corredor", igual que `capitulo3.tex`:85), guia-2 (l.11, 13, 25,
"pieza de la propuesta"), guia-3 (l.46, `\GAPDATO` ya no niega el codigo), guia-4 (l.88, "viabilidad del
corredor"). guia-5 quedo NO APLICADO con motivo (corresponde a `capitulo3`); no se reabre: no hay
argumento nuevo, aunque PAT-113 sigue presente en el cruce (`capitulo3.tex`:60, :83, :89, :213 repiten
definiciones del marco). Lint r05: PASA, 0/0/0; GAP lit=4 dato=1 dec=8.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T4 | capitulo1.tex:126 (con :110) | La condicional anadida en r04 ("si fuera aprobatorio, la multiplicidad de siete combinaciones si podria haberlo favorecido") deja abierto que la extension a Guo et al. cambie algo, mientras l.110 y `introduccion.tex`:46 dan la ruta latente por descartada. El registro cierra esa puerta: DEC 2026-09-19 punto 3, "Su resultado no cambia el diseno del Objetivo 3". El lector no puede conciliar l.110 con l.126. | Conservar la oracion de S05/T03 (sin adelantar el veredicto), pero anadir el hecho de DEC 2026-09-19: el resultado de la extension no cambia el diseno del Objetivo 3. Asi la multiplicidad queda acotada a la lectura del veredicto y no a la cadena. |
| guia-2 | baja | P-MT2 | capitulo1.tex:20, 23 (y :66) | La figura liga las metricas de Peters et al. solo al Objetivo 3 y la distancia de Wasserstein-1 a "los Objetivos 1 a 3". La introduccion (l.43) asigna al Objetivo 4 adoptar esas metricas y definir la distancia dentro de SAP (decision §2 2026-09-29: W1 se define en el Obj 4), y `capitulo3.tex`:200 la ubica en `sec:sap`. El mapa concepto-pieza omite el objetivo que los formaliza. | Fila 2: "metricas de apariencia (Objetivos 3 y 4)"; fila 5: anadir "definicion de la distancia en SAP (Objetivo 4)". |
| guia-3 | baja | G-B2 | capitulo1.tex:124 | "la incertidumbre de una media por paciente" se lee como la media de cada paciente ($\mathrm{MAE}_i$), cuando el IC es de la media sobre los 34 pacientes del error de cada uno (`capitulo3.tex`:71, :242). La oracion siguiente lo aclara a medias. | "la incertidumbre de la media, sobre los pacientes, del error de cada paciente". |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple; filas de la figura respaldadas en el cuerpo (PAT-67 no reincide) |
| G-T2 | cumple; "pieza de la propuesta" vs "cadena" ya separados; "holgura radial", "margen cortical", "umbral de 10 mm", "brecha cortical", "dominio de imagen" como en §2 (PAT-14 no reincide). Titulo "Marco estadistico" frente a la decision "marco solo para Kaiser" ya escalado en r01, no se reporta |
| G-T3 | cumple; $n$, $\bar\gamma_n$, $\beta_n$, $\boldsymbol\xi$, $\theta$, $w_{\min}$, $x$, $\Delta$ sin choque con $\phi$, $\psi$, $\alpha$, $s$, $r$, $T$, $L$, $h$, $b$, $P$, $Q$ del cap. 3; $x$ coherente con $x_v$ de `eq:mae` |
| G-T4 | cumple a medias (guia-1); 0.42, seis/siete combinaciones, tres decisiones post hoc del Obj 2, Wilcoxon de una cola y *streak amplitude* primaria coinciden con el cap. 3 (PAT-31, PAT-19 no reinciden) |
| G-T5 | cumple; orden real descrito en l.13 (PAT-71 no reincide). PAT-113 persiste en el cruce con el cap. 3 (guia-5 r04, NO APLICADO con motivo, no se reabre) |
| G-T6 | cumple (lint sin citas indefinidas) |
| G-B1 | cumple con GAP (fisica de TC, Beer-Lambert y retroproyeccion, `\GAPLIT` l.35; anatomia pelvica, `\GAPLIT` l.72) |
| G-B2 | cumple; unidad de analisis por objetivo (l.118), equivalencia sobre el IC del 90 % (l.122), MAE frente a RMSE (l.128); baja guia-3 |
| G-B3 | cumple con GAP (W1 `\GAPLIT` l.120; Wilcoxon, TOST, remuestreo `\GAPLIT` l.124; arcoseno hiperbolico `\GAPDATO` l.46) |
| G-B4 | cumple (dominio de imagen con remision a amenazas l.62; limite del 2.5D l.114, cubierto por el supuesto del dominio de imagen en `capitulo3.tex`:261; equiespaciado como convencion l.86; umbrales HU como definiciones operativas l.35) |
| P-MT1 | cumple con GAP (codificacion, U-Net, muestreo, calendario, cortes 2.5D, fraccion por zona de densidad e inversion de metricas como pendientes; PAT-108 no reincide) |
| P-MT2 | cumple a medias (guia-2) |
| G-A*, G-B5 a G-B10, G-C*, G-D*, G-R*, P-* de otros bloques | no aplican a esta seccion |

Patrones vigentes comprobados sin reincidencia en el dominio de guia: PAT-14, PAT-19, PAT-31, PAT-39,
PAT-52, PAT-101, PAT-108, PAT-110, PAT-112, PAT-113 (solo en el cruce, no reabierto), PAT-115.
PAT-8, PAT-58, PAT-72, PAT-102, PAT-111, PAT-114 son de estilo/trazabilidad.

## Propuestas de criterio
(sin propuestas nuevas; sigue pendiente la de r04 sobre si el codigo de `experiments/` cuenta como fuente)

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Condicional sobre un resultado pendiente sin decir que la decision registrada ya lo deja sin efecto | G-T4 | "si fuera aprobatorio, la multiplicidad de siete combinaciones si podria haberlo favorecido" | nuevo |
| Mapa concepto-pieza (figura o tabla) que asigna un concepto a otro objetivo que el de la introduccion | P-MT2, G-T5 | metricas de Peters solo "(Objetivo 3)"; la introduccion las pone en el Obj 4 | nuevo |
