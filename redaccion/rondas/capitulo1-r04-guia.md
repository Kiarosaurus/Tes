# Revision guia CS — capitulo1 — r04

Lecturas cruzadas: `capitulo3.tex` (l.11-95, l.125-266: cadena, compuerta, corredor, poses, SAP,
apariencia, amenazas), `capitulo2.tex` (l.1-50), `experiments/objetivo1/e6c_techo_lw.py`.
Respuesta previa: `capitulo1-r03-respuesta.md`. guia-1 r03 quedo NO APLICADO con motivo (conflicto con
T03 de trazabilidad r02) y no se reabre: no hay argumento nuevo. Bajas r03 verificadas: guia-2 (l.84,
Hinsche solo como definicion), guia-3 (l.80, regla de 5 mm y holgura de 1-2 mm con remision), guia-4
(l.106, muestreo y calendario pendientes), guia-5 (l.124, relacion IC 90 % dentro del `\GAPLIT`),
guia-6 (l.88, tercer componente de SAP con `\GAPDEC`). Lint r04: PASA, 0/0/0; GAP lit=4 dato=1 dec=8.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T4 | capitulo1.tex:35 | Patron PAT-31 reincide. La cifra 0.42 se copio de `capitulo3.tex`:85, pero la conclusion pierde su condicion: el cap. 3 dice que el umbral dejaria fuera "en la mediana, esa fraccion del corredor"; aqui, "un hueso definido por ese umbral dejaria fuera esa fraccion", que se lee como el 42 % de todo el hueso. | Restituir "en la mediana" y "del corredor" (o "de las mascaras sacras a lo largo del eje"), como en el cap. 3. |
| guia-2 | baja | G-T2 | capitulo1.tex:13, 19, 25 | Patron PAT-14 reincide. La figura y l.13 llaman "pieza de la cadena (Figura `fig:pipeline`)" a la compuerta del Obj 1 y a la "lectura de los resultados"; la Figura `fig:pipeline` (`capitulo3.tex`:20, :32) y la decision §2 (introduccion-r01) ponen la compuerta "previa a la cadena", no como pieza suya. | Caption y l.13: "pieza de la propuesta" (como en l.11), o separar la compuerta como "previa a la cadena". |
| guia-3 | baja | G-B3 | capitulo1.tex:46 | El `\GAPDATO` dice que forma y parametros del arcoseno hiperbolico "no constan en las fuentes de contenido", pero constan en `experiments/objetivo1/e6c_techo_lw.py`:17, :47, :61-69 (escala 500 HU, normalizacion entre arcsinh(-1000/500) y arcsinh(20000/500)), y OC-1 admite `experiments/` como fuente. MAPA:80 ya reconoce que la definicion "consta en el codigo". Argumento nuevo frente a la trazabilidad de r02/r03, que solo coteja `*.md`. | Dar la forma con su parametro citando el script (sin cifras de resultado), o reescribir el GAP como "solo constan en el codigo del experimento, no en un registro" para que no niegue lo que existe. Decision de la autora si el codigo cuenta como fuente. |
| guia-4 | baja | G-T2 | capitulo1.tex:88 | "La escala de brecha y el corredor son dos de los tres componentes de SAP": en `capitulo3.tex`:189 el componente es la "viabilidad del corredor" (criterio $D \geq d + 2\epsilon$), no el corredor. | "La escala de brecha y la viabilidad del corredor son dos de los tres componentes de SAP". |
| guia-5 | baja | G-T5 | capitulo1.tex:11 | La funcion del capitulo ("conceptos que el Capitulo 3 usa sin volver a definirlos") no se cumple en el cruce: el cap. 3 vuelve a definir en negrita la codificacion multiventana (`capitulo3.tex`:60) y repite la definicion de las tres metricas de Peters et al. (:213), contra la decision §2 de capitulo1-r02 (metricas presentadas una vez en el marco). | No tocar l.11; anotar para la proxima ronda de `capitulo3` que remita a `sec:mt-tc` y `sec:mt-artefactos` y deje solo lo operativo. Si no se hara, suavizar l.11 ("sin repetir su presentacion"). |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple; filas de la figura respaldadas en el cuerpo (PAT-67 no reincide) |
| G-T2 | cumple a medias (guia-2, guia-4); terminos de la introduccion usados igual (SAP, referencia clinica, $G$, $M$, $B_\delta$, holgura radial; PAT-3 no reincide) |
| G-T3 | cumple; $n$, $n_{\max}$, $\bar\gamma_n$, $\beta_n$, $\boldsymbol\xi$, $\theta$, $w_{\min}$, $x$, $\Delta$ sin choque con el cap. 3 ($\phi$, $\psi$, $\alpha$, $s$, $r$, $T$, $L$, $h$, $b$); $N$/$\mathcal{N}$ diferido (guia-12 r01) |
| G-T4 | cumple a medias (guia-1, PAT-31); protocolo fisico en futuro, decisiones post hoc segun `sec:amenazas`, agregacion del Obj 3 con `\GAPDEC` |
| G-T5 | cumple; orden real descrito (l.13, PAT-71 no reincide); baja guia-5 en el cruce con el cap. 3 |
| G-T6 | cumple (lint sin citas indefinidas) |
| G-B1 | cumple con GAP (fisica de TC y Beer-Lambert, `\GAPLIT` l.35; anatomia pelvica, `\GAPLIT` l.72; PAT-106 no reincide) |
| G-B2 | cumple; metricas de Peters et al. (l.66, PAT-107 no reincide), equivalencia sobre el IC (l.122), unidad de analisis por objetivo (l.118), tres componentes de SAP (l.88) |
| G-B3 | cumple con GAP (Wasserstein-1 `\GAPLIT` l.120; Wilcoxon, TOST, IC 90 % y remuestreo `\GAPLIT` l.124); baja guia-3 sobre el texto del `\GAPDATO` de l.46 |
| G-B4 | cumple (dominio de imagen l.62, limite del 2.5D l.114, equiespaciado como convencion l.86, umbrales HU como definiciones operativas l.35, lectura de Kaiser con remision l.80) |
| P-MT1 | cumple con GAP (codificacion, muestreo, calendario, cortes 2.5D y fraccion por zona de densidad con `\GAPDEC`; PAT-108 no reincide) |
| P-MT2 | cumple (Fig. `fig:mt-conceptos`; ver guia-2 por el termino "cadena") |
| G-A*, G-B5 a G-B10, G-C*, G-D*, G-R*, P-* de otros bloques | no aplican a esta seccion |

Patrones vigentes comprobados sin reincidencia en el dominio de guia: PAT-19 (salvo la variante de
guia-3), PAT-39, PAT-52, PAT-67, PAT-71, PAT-101, PAT-106, PAT-107, PAT-108, PAT-109, PAT-110,
PAT-112. PAT-8, PAT-72, PAT-97, PAT-98, PAT-102, PAT-111 son de estilo/trazabilidad.

## Propuestas de criterio
- Derivado de G-B3 / OC-1: precisar si el codigo bajo `experiments/` (no solo `*.md`) cuenta como
  fuente de contenido para definiciones y parametros de diseno; hoy guia y trazabilidad lo leen distinto.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Cifra copiada de otro capitulo cuya conclusion pierde "en la mediana" y el ambito | G-T4 | "Un hueso definido por ese umbral dejaria fuera esa fraccion" | PAT-31 |
| Un termino del documento ("cadena") cubre aqui una pieza que otra seccion deja fuera | G-T2 | "Conceptos del capitulo y pieza de la cadena ... que los usa" (incluye la compuerta) | PAT-14 |
| GAP que niega que un dato conste en las fuentes cuando esta en el codigo de `experiments/` | G-B3, G-T4 | "forma y parametros ... que no constan en las fuentes de contenido" | PAT-19 (variante) |
| La funcion declarada del capitulo la contradice otro capitulo que redefine lo mismo | G-T5 | "conceptos que el Capitulo 3 usa sin volver a definirlos" | nuevo |
