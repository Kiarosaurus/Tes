# Revision guia CS — capitulo1 — r03

Lecturas cruzadas: `introduccion.tex` (objetivos, alcance, terminos ya definidos: corredor oseo,
envolvente, holgura radial, SAP), `capitulo3.tex` completo (G-T2, G-T3, G-T4, G-T5, G-B3). Respuesta
previa: `capitulo1-r02-respuesta.md` (0 rechazados; S03 no aplicado, es de estilo y no se reabre).
No se reabren: guia-12 r01 ($N$ / $\mathcal{N}$, diferido al cap. 3), guia-11 r01 (aplicado minimo),
guia-13 r01 (aplicado parcial). Lint r03: PASA, 0/0/0; GAP lit=4 dato=1 dec=7.
Los dos medios de r02 se verificaron aplicados: Beer-Lambert dentro del `\GAPLIT` (l.35) y metricas de
Peters et al. en l.66 y en la fila 2 de la figura. Bajas de r02 aplicadas (l.13, l.46, l.70, l.76, l.110).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | baja | G-T5 | capitulo1.tex:124 | El cierre de §1.5 cuenta historia del diseno (extension de la compuerta a Guo et al. como septimo candidato, veredicto negativo que neutraliza la multiplicidad) que ya esta en `sec:amenazas` (cap. 3 l.255, l.265). l.11 dice que el capitulo no describe el diseno. Se respeta la decision §2 (capitulo1-r01): el resumen de lo fijado va seguido de las decisiones posteriores. | Dejar el concepto (fijar antes de ver datos, multiplicidad y en que direccion sesga) con la mencion de las decisiones posteriores y remision; sacar la oracion de Guo et al., que solo repite el cap. 3. |
| guia-2 | baja | G-T5 | capitulo1.tex:84 | La oracion de Hinsche et al. concluye que "sus resultados no se comparan con las distribuciones de grados de Zwingmann et al.": es comparacion entre trabajos, funcion que l.11 asigna al cap. 2. Hinsche et al. no aparece en el cap. 2 ni en el cap. 3, asi que la comparacion no la usa ninguna pieza. | Dejar en §1.3 solo el hecho de definicion (escala binaria frente a graduada) o llevar la comparacion a la seccion del cap. 2 que compara las fuentes del Obj 2/Obj 4. |
| guia-3 | baja | P-MT1 | capitulo1.tex:80 | El marco de Kaiser et al. se presenta sin la regla de longitud util (margen cortical $h$ de 5 mm) ni la holgura de 1 a 2 mm. El `\GAPDEC` de l.72 nombra "la holgura radial de Kaiser et al.", y el cap. 3 deriva de $h$ toda la escala de las poses (l.158, Tabla `tab:preinscripcion`). Es teoria usada directamente en el desarrollo. | Una oracion en l.80: el marco incluye una regla de longitud util de 5 mm y Kaiser et al. justifican el umbral como holgura de 1-2 mm; la lectura como $h$ radial y holgura por lado, con remision a `sec:corredor` y `sec:poses`. |
| guia-4 | baja | P-MT1 | capitulo1.tex:95, 104 | El calendario coseno de Nichol y Dhariwal y el muestreo determinista con menos pasos de Song et al. se definen, pero no se dice si el sintetizador los usa. l.11 promete decir en que pieza interviene cada concepto; l.110 cubre el muestreo solo frente a Lugmayr et al. y LeFusion. | Una clausula que remita al diseno no congelado del sintetizador (`sec:sintetizador`, `\GAPDEC` del cap. 3 l.172: entrenamiento y muestreo), o ampliar el `\GAPDEC` de l.110 para que cubra calendario y numero de pasos. |
| guia-5 | baja | G-B3 | capitulo1.tex:120, 122 | La equivalencia usa un IC del 90 % y la compuerta un IC del 95 %, sin decir por que difieren. Un lector de computacion no puede verificar por que 90 % es el nivel correcto de las dos pruebas unilaterales del cap. 3 (l.225). | Si una ficha lo respalda, una clausula que ligue el IC del 90 % con dos pruebas unilaterales; si no, nombrar esa relacion dentro del `\GAPLIT` de l.122. |
| guia-6 | baja | G-B2 | capitulo1.tex:21, 68-86 | La fila 3 de la figura liga §1.3 con SAP (Obj 4), pero el capitulo solo da concepto para dos de sus tres componentes (escala de brecha y corredor). La fraccion por zona de densidad no aparece, ni con remision a su `\GAPDEC` del cap. 3 (l.166). | Una oracion en §1.3 que nombre el tercer componente (densidad osea de Arand et al.) y remita a `sec:muestreador` y a su `\GAPDEC`; el criterio queda "cumple con GAP". |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple; filas de la figura respaldadas en el cuerpo (PAT-67 no reincide; ver guia-6 para SAP) |
| G-T2 | cumple; "corredor oseo", "envolvente", "holgura radial", "SAP" y "pacientes de prueba" se definen antes, en la introduccion (PAT-3 no reincide); "umbral de 10 mm" uniforme en el capitulo; "serie" solo para cada grupo (PAT-14 no reincide en este capitulo) |
| G-T3 | cumple; $n$, $n_{\max}$, $\bar\gamma_n$, $\boldsymbol\xi$, $\beta_n$, $w_{\min}$, $x$, $\Delta$, $G$, $M$, $B_\delta$ coherentes con el cap. 3; $N$ / $\mathcal{N}$ diferido (guia-12 r01) |
| G-T4 | cumple; protocolo fisico en futuro (l.64), equivalencia con su `\GAPDEC` de plazo (l.122), decisiones post hoc segun `sec:amenazas` (l.124), agregacion del Obj 3 con `\GAPDEC` (l.116); PAT-9, PAT-19, PAT-73, PAT-90 no reinciden |
| G-T5 | cumple; orden real descrito y justificado (l.13, PAT-71 no reincide); bajas guia-1, guia-2 |
| G-T6 | cumple (lint y compilacion sin citas indefinidas) |
| G-B1 | cumple con GAP (fisica de TC y Beer-Lambert, `\GAPLIT` l.35; anatomia pelvica, `\GAPLIT` l.72); PAT-106 corregido |
| G-B2 | cumple; metricas de Peters et al. presentes (l.66, PAT-107 corregido); equivalencia sobre el IC (l.120, PAT-100 no reincide); baja guia-6 |
| G-B3 | cumple con GAP (arcoseno hiperbolico `\GAPDATO` l.46; Wasserstein-1 `\GAPLIT` l.118; Wilcoxon, TOST y remuestreo `\GAPLIT` l.122); baja guia-5 |
| G-B4 | cumple (supuesto del dominio de imagen l.62, limite del 2.5D l.112, equiespaciado como convencion l.86, umbrales HU como definiciones operativas l.35) |
| P-MT1 | cumple con GAP (codificacion del sintetizador, muestreo y cortes 2.5D con `\GAPDEC`); bajas guia-3, guia-4 |
| P-MT2 | cumple (Fig. `fig:mt-conceptos`) |
| G-A*, G-B5 a G-B10, G-C*, G-D*, G-R*, P-* de otros bloques | no aplican a esta seccion |

## Propuestas de criterio
- Derivado de G-T5 para el bloque (b): "el marco teorico no concluye sobre la comparabilidad de
  resultados entre trabajos; eso es del estado del arte". Hoy se juzga con la frase de funcion del
  propio capitulo (guia-2).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| El marco teorico compara resultados entre trabajos, funcion que el propio capitulo asigna al estado del arte | G-T5 | "de modo que sus resultados no se comparan con las distribuciones de ... Zwingmann" | nuevo |
| Concepto de la teoria definido sin decir si la pieza propia lo usa, aunque el capitulo lo promete | P-MT1 | calendario coseno de Nichol y Dhariwal, sin decir si el sintetizador lo adopta | PAT-108 |
