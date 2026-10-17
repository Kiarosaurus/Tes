# Auditoria de trazabilidad — trabajosFuturos — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4 | `overleaf/secciones/trabajosFuturos.tex:35` | "la amplitud variara poco entre grados" | `overleaf/secciones/capitulo3.tex:359`; `docs/01-decisiones.md:2760-2763`; `redaccion/BITACORA.md` PAT-178 | Patron PAT-178 reincide. El registro solo conserva una expectativa cualitativa y reconoce que carece de umbral; por ello no es contrastable ni puede verificarse qué contaría como "poco". | Eliminar la expectativa o presentarla expresamente como intuicion no evaluable, sin llamarla expectativa fijada susceptible de contraste. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| `trabajosFuturos.tex:11` | Las direcciones proceden de ensayos fijados no ejecutados y mediciones declaradas no hechas. | `overleaf/secciones/capitulo3.tex:38,519,529-553`; `overleaf/secciones/capitulo4.tex:232` | si |
| `trabajosFuturos.tex:11` | Se ordenan por objetivo y terminan en la segmentacion posterior. | Estructura visible en `trabajosFuturos.tex:13-39`; encargo `redaccion/ENCARGO_2026-10-16.md`, punto 6 | si |
| `trabajosFuturos.tex:11` | La aplicacion motivadora es el aumento para segmentacion osea periimplante. | `docs/00-tesis.md:239-243`; `overleaf/secciones/conclusiones.tex:38` | si |
| `trabajosFuturos.tex:15` | La compuerta descarto la difusion latente con dos variantes de SD 1.5. | `experiments/objetivo1/p1_compuerta.md:5,19-24`; `overleaf/secciones/capitulo4.tex:236-238` | si |
| `trabajosFuturos.tex:15` | El resultado no descarta todo espacio latente. | `overleaf/secciones/capitulo4.tex:238`; solo se evaluaron dos variantes y una cota | si |
| `trabajosFuturos.tex:15` | El criterio de la compuerta fue 25 HU de MAE en hueso. | `experiments/objetivo1/p1_compuerta.md:5`; `overleaf/secciones/capitulo4.tex:37` | si |
| `trabajosFuturos.tex:15` | La regla puede aplicarse antes de entrenar un modelo generativo. | `overleaf/secciones/conclusiones.tex:36`; consecuencia metodologica del procedimiento de compuerta | si |
| `trabajosFuturos.tex:15` | El autoencoder de Guo et al. no se corrio. | `overleaf/secciones/capitulo4.tex:45,236`; `docs/01-decisiones.md:2812-2818` | si |
| `trabajosFuturos.tex:15` | Su cota por saturacion supera 25 HU. | `overleaf/secciones/capitulo4.tex:45` (42.24 HU); inspeccion de codigo registrada en `docs/01-decisiones.md:2812-2818` | si |
| `trabajosFuturos.tex:15` | La compuerta no descarto la codificacion multiventana. | `overleaf/secciones/capitulo4.tex:238`; `overleaf/secciones/conclusiones.tex:14` | si |
| `trabajosFuturos.tex:15` | Su ida y vuelta sin autoencoder dio 0.00 HU con asinh. | `experiments/objetivo1/p1_compuerta.md:35,38`; `overleaf/secciones/capitulo4.tex:41` | si |
| `trabajosFuturos.tex:19` | El muestreador se ejecuto en un corredor y con todos sus componentes. | `overleaf/secciones/capitulo4.tex:49`; `docs/01-decisiones.md:2767-2770` | si |
| `trabajosFuturos.tex:19` | Del segundo corredor solo se midio el eje en 69 de 72 pacientes. | `docs/00-tesis.md:63-65`; `docs/01-decisiones.md:2767-2770` | si |
| `trabajosFuturos.tex:19` | Sus poses y grados no se preinscribieron ni ejecutaron. | `docs/01-decisiones.md:2767-2770`; `overleaf/secciones/capitulo3.tex:196` | si |
| `trabajosFuturos.tex:19` | El nivel vertebral del segundo corredor varia entre volumenes. | `overleaf/secciones/capitulo3.tex:196`; `docs/01-decisiones.md:2767-2769` | si |
| `trabajosFuturos.tex:19` | No hay distribucion ordinal clinica revisada por debajo de S1. | `docs/00-tesis.md:62-65`; `docs/01-decisiones.md:2767-2769`; `overleaf/secciones/capitulo3.tex:196` | si |
| `trabajosFuturos.tex:19` | Un muestreo futuro seria descriptivo y sin referencia clinica. | `docs/01-decisiones.md:2767-2770`; `overleaf/secciones/capitulo3.tex:196` | si |
| `trabajosFuturos.tex:19` | Las ablaciones retirarian anclaje al eje y escala de perturbacion. | `overleaf/secciones/introduccion.tex:83`; `docs/01-decisiones.md:2163-2164` | si |
| `trabajosFuturos.tex:21` | El cierre ocupa el hueco medial de S1 en 14 de 71. | `experiments/registro/registro_2026-10-16.md:53`; `docs/01-decisiones.md:2743-2748` | si |
| `trabajosFuturos.tex:21` | No se establecio que el hueco sea el canal ni se midieron foramenes. | `docs/01-decisiones.md:2749-2751`; `overleaf/secciones/capitulo3.tex:529` | si |
| `trabajosFuturos.tex:21` | No se midio el efecto de esa ocupacion sobre la brecha. | `docs/01-decisiones.md:2749-2751`; `overleaf/secciones/capitulo3.tex:529` | si |
| `trabajosFuturos.tex:21` | Las cifras del Objetivo 2 no se corrigieron por ese efecto. | `docs/01-decisiones.md:2743-2744`; `overleaf/secciones/conclusiones.tex:32` | si |
| `trabajosFuturos.tex:21` | No se establecio la causa de los 15 corredores estrechos. | `overleaf/secciones/capitulo4.tex:242-244`; `overleaf/secciones/conclusiones.tex:32` | si |
| `trabajosFuturos.tex:21` | El calibre es 7.0 mm. | `overleaf/secciones/capitulo3.tex:315`; `overleaf/secciones/capitulo4.tex:54` | si |
| `trabajosFuturos.tex:21` | Hubo fractura confirmada en 20 de 30 casos cribados. | `overleaf/secciones/capitulo3.tex:551`; `overleaf/secciones/capitulo4.tex:244` | si |
| `trabajosFuturos.tex:21` | La fractura confunde la causa de los corredores estrechos. | `overleaf/secciones/capitulo3.tex:551`; `overleaf/secciones/capitulo4.tex:244` | si |
| `trabajosFuturos.tex:23` | No se midio donde cae el voxel mas craneal de toda S1. | `docs/01-decisiones.md:2793-2795`; `overleaf/secciones/capitulo3.tex:531` | si |
| `trabajosFuturos.tex:23` | Ese supuesto afecta el control de nivel de la cohorte. | `docs/01-decisiones.md:2793-2795`; `overleaf/secciones/capitulo3.tex:531` | si |
| `trabajosFuturos.tex:23` | La revision en cortes consta solo para 56 pacientes de CLINIC-metal. | `docs/01-decisiones.md:2774-2777`; `overleaf/secciones/capitulo3.tex:48` | si |
| `trabajosFuturos.tex:23` | En receptores, la ausencia de metal descansa en revision 3D y cribado HU. | `docs/01-decisiones.md:2774-2777`; `overleaf/secciones/capitulo3.tex:48` | si |
| `trabajosFuturos.tex:27` | Contraste de realismo, comparacion ciega y control visual no se ejecutaron. | `docs/01-decisiones.md:2729-2734,2771-2773`; `overleaf/secciones/capitulo3.tex:549` | si |
| `trabajosFuturos.tex:27` | El contraste usaria perfil radial e histograma dentro de M. | `overleaf/secciones/capitulo3.tex:467-469` | si |
| `trabajosFuturos.tex:27` | La referencia serian tornillos aislados reales de prueba. | `overleaf/secciones/capitulo3.tex:469-471` | si |
| `trabajosFuturos.tex:27` | La lista de pacientes de la referencia no se formo. | `overleaf/secciones/capitulo3.tex:471` | si |
| `trabajosFuturos.tex:27` | La comparacion ciega ordenaria tres modelos con etiquetas ocultas y orden aleatorio. | `overleaf/secciones/capitulo3.tex:305` | si |
| `trabajosFuturos.tex:27` | El control visual usaria laminas regladas y cuatro defectos cerrados. | `overleaf/secciones/capitulo3.tex:377` | si |
| `trabajosFuturos.tex:27` | Con el modelo evaluado, el control ya no seria ciego. | `overleaf/secciones/capitulo3.tex:377` | si |
| `trabajosFuturos.tex:27` | Los ensayos visuales no intervenian en ningun desenlace. | `overleaf/secciones/capitulo3.tex:305,377`; `docs/01-decisiones.md:2729-2731` | si |
| `trabajosFuturos.tex:27` | La tesis no reclama realismo visual. | `docs/01-decisiones.md:2723-2734`; `overleaf/secciones/capitulo3.tex:549` | si |
| `trabajosFuturos.tex:29` | Se decidio no crear una tercera version del sintetizador. | `docs/01-decisiones.md:2723-2724` | si |
| `trabajosFuturos.tex:29` | La opcion descartada incluia banda mayor, residual o refinamiento sim-a-real. | `docs/04-implicancias.md:12456-12460` (#193, opcion c); `docs/01-decisiones.md:2723-2728` (opcion a elegida) | si |
| `trabajosFuturos.tex:29` | Esa opcion requeria pares simulados y tiempo no estimado. | `docs/04-implicancias.md:12456-12460` (#193) | si |
| `trabajosFuturos.tex:29` | Perfil: 1.92 sintetizador, 6.71 fisico y 4.08 exceso real. | `experiments/objetivo3/resultados_dec_2026-10-15.md:201-203`; `overleaf/secciones/capitulo4.tex:161-168` | si |
| `trabajosFuturos.tex:29` | Piso de ruido: 0.69 sintetizador y 0.12 protocolo fisico. | `experiments/objetivo3/resultados_dec_2026-10-15.md:78-79` | si |
| `trabajosFuturos.tex:29` | CV: 0.076 sintetizador y 0.241 protocolo fisico. | `experiments/objetivo3/resultados_prueba_v1.md:41`; `experiments/objetivo3/resultados_dec_2026-10-15.md:39` | si |
| `trabajosFuturos.tex:29` | La version 2 no cambio ningun desenlace. | `overleaf/secciones/capitulo4.tex:224-228`; `docs/01-decisiones.md:2726-2728` | si |
| `trabajosFuturos.tex:31` | El deficit medido en validacion quedo dentro de la banda de 12 mm. | `overleaf/secciones/capitulo3.tex:299-301,539,549`; medicion acotada a componentes de 500--4000 mm3 | si |
| `trabajosFuturos.tex:31` | Mas alla, la amplitud fisica es del orden de su piso de ruido. | `overleaf/secciones/capitulo4.tex:136-142`; `overleaf/secciones/capitulo3.tex:539` | si |
| `trabajosFuturos.tex:33` | El entrenamiento excluyo volumenes secundarios por la regla de uno por paciente. | `overleaf/secciones/capitulo3.tex:56,230,509` | si |
| `trabajosFuturos.tex:33` | Incluir varios volumenes del mismo paciente es una variante por medir. | `docs/04-implicancias.md` #171, punto 3; `overleaf/secciones/capitulo3.tex:230` | si |
| `trabajosFuturos.tex:33` | Evaluarla en la misma prueba seria posterior y exploratorio, como v2. | `overleaf/secciones/capitulo3.tex:303-307,509`; `overleaf/secciones/capitulo4.tex:254` | si |
| `trabajosFuturos.tex:35` | Ningun resultado del Objetivo 3 usa poses perturbadas del muestreador. | `docs/01-decisiones.md:2760-2766`; `docs/04-implicancias.md:12520-12529` (#197) | si |
| `trabajosFuturos.tex:35` | La sintesis evaluada uso el eje del corredor sin perturbar. | `overleaf/secciones/capitulo3.tex:359,553`; `docs/01-decisiones.md:2764-2766` | si |
| `trabajosFuturos.tex:35` | D9 fijo 5 poses por paciente y no se ejecuto. | `docs/01-decisiones.md:2760-2763`; `overleaf/secciones/capitulo3.tex:359` | si |
| `trabajosFuturos.tex:35` | D9 usaria solo sintetizador, modelo evaluado y cinco semillas. | `overleaf/secciones/capitulo3.tex:359` | si |
| `trabajosFuturos.tex:35` | D9 resumiria streak amplitude y metal integrity por grado. | `overleaf/secciones/capitulo3.tex:359` | si |
| `trabajosFuturos.tex:35` | La expectativa de variacion pequena carece de umbral. | `overleaf/secciones/capitulo3.tex:359`; `docs/01-decisiones.md:2760-2763` | no: T01 |
| `trabajosFuturos.tex:35` | El protocolo fisico simulo uno de cada dos cortes por costo. | `overleaf/secciones/capitulo3.tex:359,363` | si |
| `trabajosFuturos.tex:39` | La evaluacion posterior con Dice y HD95 quedo fuera de alcance. | `docs/00-tesis.md:239-243`; `overleaf/secciones/introduccion.tex:82` | si |
| `trabajosFuturos.tex:39` | CTPelvic1K tiene 75 volumenes con metal y 14 anotados. | `liu2021ctpelvic1k`, Evidencia textual, filas "Volumenes con metal", "CLINIC-metal" y "Anotaciones existentes" | si |
| `trabajosFuturos.tex:39` | No esta verificado que las mascaras anotadas esten disponibles localmente. | `docs/02-datos.md:180-184`; `overleaf/secciones/capitulo3.tex:36` | si |
| `trabajosFuturos.tex:39` | Hay 178 volumenes locales de los 1184 publicados. | `docs/02-datos.md:53-57`; `liu2021ctpelvic1k`, Evidencia textual, fila "Total del dataset" | si |
| `trabajosFuturos.tex:39` | El uso como aumento carece de respaldo porque no se reclama realismo visual. | `docs/01-decisiones.md:2723-2734`; `overleaf/secciones/conclusiones.tex:38` | si |
| `trabajosFuturos.tex:39` | La utilidad posterior queda como pregunta abierta sin resultado anticipado. | `docs/00-tesis.md:239-243`; `overleaf/secciones/conclusiones.tex:38` | si |
| `trabajosFuturos.tex:15,39` | Claves `guo2025maisi` y `liu2021ctpelvic1k` existen; apellidos coinciden. | `overleaf/referencias.bib:463-469,724-732` | si |

TOTAL alta=0 media=1 baja=0

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una expectativa cualitativa se presenta sin umbral que permita contrastarla. | G-T4 | "la amplitud variara poco entre grados" | PAT-178 |
