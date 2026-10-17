# Auditoria de trazabilidad — conclusiones — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-1 | `overleaf/secciones/conclusiones.tex:12,34` | “solo se examinaron dos autoencoders” | `docs/00-tesis.md:47-53`; `overleaf/secciones/capitulo4.tex:45,236-238`; `docs/literatura/guo2025maisi.md`, Evidencia textual, filas 15-16 | Patron PAT-201 reincide: el autoencoder de Guo no se ejecuto; solo se calculo una cota por saturacion del rango de salida inspeccionado en codigo. Por ello no consta que ese autoencoder fuera “examinado” ni que se comprobara que no conserva HU. | Sustituir ambas generalizaciones por: se evaluaron las dos variantes del autoencoder de Stable Diffusion y, para Guo, la cota por saturacion impidio ejecutar el autoencoder; no generalizar el resultado a “dos autoencoders examinados”. |
| T02 | alta | G-T4 | `overleaf/secciones/conclusiones.tex:14,26` | “Ningun parametro del muestreador se tomo de la referencia clinica” | `experiments/objetivo2/preinscripcion_muestreador.md:3-15,52-75`; `docs/00-tesis.md:61-78`; `CLAUDE.md:18-21` | Las fuentes vigentes se contradicen: la preinscripcion y `00-tesis.md` sostienen que Zwingmann solo se uso para comparar, pero `CLAUDE.md` ordena que el muestreador “muestrea de las distribuciones ordinales” de Zwingmann. Aunque el texto coincide con la implementacion documentada, una contradiccion entre fuentes es alta. | Escalar la contradiccion a la autora y alinear `CLAUDE.md` con la preinscripcion antes de conservar estas dos afirmaciones; no resolverla silenciosamente dentro de conclusiones. |
| T03 | alta | G-T4 | `overleaf/secciones/conclusiones.tex:34` | “separaron [...] donde la media no lo hacia” | `experiments/objetivo3/resultados_prueba_v1.md:14,36,41-42`; `overleaf/secciones/capitulo4.tex:94,128,172,252-254` | La diferencia media si separo los brazos en direccion: fue -301.0 HU y su IC95 excluyo cero. El perfil y la variabilidad agregan dimensiones que la comparacion de medias no recoge; no separan donde la media no lo hizo. | Escribir: “El perfil por anillos y la variabilidad entre pacientes mostraron diferencias adicionales que la comparacion de medias no recoge”. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| `conclusiones.tex:8` | Cadena de dos componentes: tornillo transiliaco-transsacro y artefacto local en TC pelvica sin implante | `docs/00-tesis.md:54-78,106-112` | si |
| `conclusiones.tex:8` | Se evalua coherencia quirurgica y fisica, no utilidad para segmentacion | `CLAUDE.md:5-15`; `docs/00-tesis.md:235-248` | si |
| `conclusiones.tex:8` | La compuerta de difusion latente fue negativa y llevo al dominio de imagen | `docs/00-tesis.md:47-53,106-114` | si |
| `conclusiones.tex:8` | Muestreador ejecutado sobre dos cohortes y comparado con referencia clinica | `experiments/objetivo2/preinscripcion_muestreador.md:18-23`; `e13_sap.md:44-46`; `e15_w1_sensibilidad.md:5-10` | si |
| `conclusiones.tex:8` | Sintetizador evaluado frente a Peters y copia y pegado | `experiments/objetivo3/diseno_A.md:319-332`; `resultados_prueba_v1.md:14-24` | si |
| `conclusiones.tex:8` | Peters et al. es el protocolo fisico adoptado | `docs/literatura/peters2025hybrid.md:8-14`; clave presente en `overleaf/referencias.bib` | si |
| `conclusiones.tex:8` | Compuerta no superada | `experiments/objetivo1/p1_compuerta.md:5,25` | si |
| `conclusiones.tex:8` | Hipotesis de equivalencia de apariencia no se sostiene | `docs/00-tesis.md:162-171,203-205`; `docs/01-decisiones.md:2615-2618` | si |
| `conclusiones.tex:8` | W1 del muestreador menor que la distancia entre series, sin regla de decision | `docs/00-tesis.md:66-78`; `e13_sap.md:45` | si |
| `conclusiones.tex:12` | Regla del Objetivo 1 fijada antes y resultado negativo | `experiments/objetivo1/p1_compuerta.md:5,25` | si |
| `conclusiones.tex:12` | Seis combinaciones, 25 HU, 34 pacientes | `experiments/objetivo1/p1_compuerta.md:5,20-25` | si |
| `conclusiones.tex:12` | Mejor MAE 61.72 HU; IC95 55.12-68.99 HU; 34/34 sobre umbral | `experiments/objetivo1/p1_compuerta.md:25`; `docs/00-tesis.md:47-53` | si |
| `conclusiones.tex:12` | Guo et al. publican un generador con autoencoder | `guo2025maisi`, Evidencia textual, filas 15-16; clave y primer autor coinciden en `referencias.bib` | si |
| `conclusiones.tex:12` | La saturacion del generador de Guo supera el criterio | `docs/00-tesis.md:52-53`; `overleaf/secciones/capitulo4.tex:45` | si |
| `conclusiones.tex:12` | Veredicto propio motivo el rediseño sin cambiar la regla | `docs/00-tesis.md:106-117`; `overleaf/secciones/capitulo4.tex:238` | si |
| `conclusiones.tex:12` | Se descarto difusion latente, no codificacion multiventana | `docs/00-tesis.md:106-114`; `overleaf/secciones/capitulo4.tex:238` | si |
| `conclusiones.tex:12` | Ida y vuelta asinh sin autoencoder: 0.00 HU en hueso | `experiments/objetivo1/p1_compuerta.md:34-38`; `overleaf/secciones/capitulo4.tex:41` | si |
| `conclusiones.tex:12` | Solo se examinaron dos autoencoders | `docs/00-tesis.md:52-53`; `overleaf/secciones/capitulo4.tex:45,236` | no; T01 |
| `conclusiones.tex:14` | Muestreo completo y controles de implementacion superados | `experiments/objetivo2/e12_sap_control.md:15-19,50,98`; `e13_sap.md:3,12,54` | si |
| `conclusiones.tex:14` | 3600 poses/72 pacientes y 2450 poses/49 pacientes | `preinscripcion_muestreador.md:18-23,61`; `e13_sap.md:44-46`; `e15_w1_sensibilidad.md:7` | si |
| `conclusiones.tex:14` | W1 0.206 navegada y 0.230 convencional | `experiments/objetivo2/e13_sap.md:45`; `e15_w1_sensibilidad.md:7` | si |
| `conclusiones.tex:14` | Distancia entre series: 0.395 grados | `docs/00-tesis.md:75-78`; `overleaf/secciones/capitulo4.tex:62-65,80` | si |
| `conclusiones.tex:14` | Ningun parametro procede de la referencia clinica | `preinscripcion_muestreador.md:52-75`; contradice `CLAUDE.md:18-21` | no; T02 |
| `conclusiones.tex:14` | Objetivo 2 sin regla de exito o fallo; escala posterior | `preinscripcion_muestreador.md:108-113`; `docs/00-tesis.md:75-78`; `capitulo4.tex:80` | si |
| `conclusiones.tex:14` | IC por remuestreo no ordenan las dos series | `experiments/objetivo2/e15_w1_sensibilidad.md:10-12`; `capitulo4.tex:82` | si |
| `conclusiones.tex:14` | 15 de 72 corredores no admiten calibre | `experiments/objetivo2/e13b_estratificado.md:13-15` | si |
| `conclusiones.tex:14` | Grado 0: 3.3 % en estrechos frente a 64.2 % en 57 restantes | `experiments/objetivo2/e13b_estratificado.md:13-15` | si |
| `conclusiones.tex:16` | Objetivo 3 implementado en imagen y evaluado con diseño congelado | `docs/00-tesis.md:106-123`; `experiments/objetivo3/diseno_A.md:81-124` | si |
| `conclusiones.tex:16` | Cumple como objetivo de diseño y evaluacion | `docs/01-decisiones.md:2615-2618`; `overleaf/secciones/capitulo4.tex:250` | si |
| `conclusiones.tex:16` | Contraste en 13 pacientes | `experiments/objetivo3/resultados_prueba_v1.md:14` | si |
| `conclusiones.tex:16` | Diferencia -301.0 HU; IC90 -477.0 a -124.9; Delta 196.3 HU | `experiments/objetivo3/resultados_prueba_v1.md:14,36` | si |
| `conclusiones.tex:16` | Desenlace no concluyente y amplitud menor | `resultados_prueba_v1.md:36`; `docs/00-tesis.md:162-170` | si |
| `conclusiones.tex:16` | Hipotesis no se sostiene, sin no equivalencia demostrada | `docs/00-tesis.md:203-205`; `docs/01-decisiones.md:2702-2706` | si |
| `conclusiones.tex:16` | Estado final: intervalo entero fuera del margen | `experiments/objetivo3/resultados_prueba_v1.md:20,37` | si |
| `conclusiones.tex:16` | Lectura en dos niveles fijada despues de ver ambas versiones | `docs/01-decisiones.md:2615-2618,2702-2706`; `capitulo4.tex:128` | si |
| `conclusiones.tex:18` | Wilcoxon p=0.000122, n=13, frente a copia y pegado | `experiments/objetivo3/resultados_prueba_v1.md:23-24` | si |
| `conclusiones.tex:18` | Copia y pegado es control de cordura sin evidencia favorable | `resultados_prueba_v1.md:23-24`; `docs/00-tesis.md:167-168,195-197` | si |
| `conclusiones.tex:18` | Amplitud menor en banda y mayor junto al borde de G | `experiments/objetivo3/resultados_dec_2026-10-15.md:39-42,65,192-204` | si |
| `conclusiones.tex:18` | Razones 1.92, 6.71 y 4.08 | `resultados_dec_2026-10-15.md:201-204`; `outputs/a29/a29_perfil.md:18-22` | si |
| `conclusiones.tex:18` | CV 0.076 frente a 0.241 | `resultados_prueba_v1.md:41-42`; `resultados_dec_2026-10-15.md:39` | si |
| `conclusiones.tex:18` | Version 2: -258.9 y -264.3 HU; mismo desenlace | `resultados_dec_2026-10-15.md:86-98`; implicancia 190 `docs/04-implicancias.md:12394-12403` | si |
| `conclusiones.tex:20` | SAP cumple Objetivo 4 como definicion y tiene dos componentes | `docs/00-tesis.md:75-78,231-232`; `capitulo4.tex:246` | si |
| `conclusiones.tex:20` | Controles de identidad, monotonia y resolucion | `experiments/objetivo2/e12_sap_control.md:15-19,41-50,75-84` | si |
| `conclusiones.tex:20` | SAP se aplico a todas las poses sin descartes | `experiments/objetivo2/e13_sap.md:3,12,54` | si |
| `conclusiones.tex:20` | SAP no validada clinicamente; mide protrusion respecto de envolvente segmentada | `docs/00-tesis.md:75-80`; `docs/01-decisiones.md:2743-2752`; `capitulo4.tex:246,264` | si |
| `conclusiones.tex:20` | Metricas de Peters aplicadas con inversion; protocolo no es verdad fisica | `docs/literatura/peters2025hybrid.md:382-400`; `overleaf/secciones/capitulo4.tex:246`; clave presente | si |
| `conclusiones.tex:22` | Pregunta compara colocaciones con distribuciones y artefactos con Peters/copia-pega | `docs/00-tesis.md:13-23`; `overleaf/secciones/introduccion.tex:27-33` | si |
| `conclusiones.tex:22` | Colocacion mas cerca de cada serie que las series entre si, descriptivo | `e13_sap.md:45`; `docs/00-tesis.md:75-78` | si |
| `conclusiones.tex:22` | Coherencia de apariencia no establecida; amplitud por debajo | `resultados_prueba_v1.md:14,36`; `docs/00-tesis.md:203-205` | si |
| `conclusiones.tex:22` | Copia y pegado no produce artefacto; cualquier brazo con artefacto la supera | `resultados_prueba_v1.md:23-24`; `capitulo4.tex:132` | si |
| `conclusiones.tex:26` | Regla de compuerta previa e inalterada | `experiments/objetivo1/p1_compuerta.md:5`; `docs/00-tesis.md:47-53,113-114` | si |
| `conclusiones.tex:26` | Distribucion del muestreador preinscrita antes de calcular W1 | `preinscripcion_muestreador.md:3-15,128-137`; `e13_sap.md:5` | si |
| `conclusiones.tex:26` | Preinscripcion independiente de referencia clinica | `preinscripcion_muestreador.md:52-75`; contradice `CLAUDE.md:18-21` | no; T02 |
| `conclusiones.tex:26` | SAP compara en escala de cuatro grados | `preinscripcion_muestreador.md:83-105`; `docs/00-tesis.md:61-78` | si |
| `conclusiones.tex:26` | Regla, margen y contrastes del sintetizador fijados en diseño congelado | `docs/00-tesis.md:115-123,160-171,187-202`; `diseno_A.md:81-124` | si |
| `conclusiones.tex:26` | Analisis añadidos: perfil, piso y variabilidad no recogida por prueba de medias | `resultados_dec_2026-10-15.md:71-78,192-204`; `resultados_prueba_v1.md:41-42`; `capitulo4.tex:254` | si |
| `conclusiones.tex:28` | Realismo visual no reclamado; juicio de autora; no rediseñar ni reentrenar | `docs/01-decisiones.md:2717-2734`; implicancia 193 `docs/04-implicancias.md:12443-12460` | si |
| `conclusiones.tex:28` | Perfil plano y piso/amplitud 0.69 | `resultados_dec_2026-10-15.md:76-78,201-204`; `capitulo4.tex:140,168` | si |
| `conclusiones.tex:28` | Reclamo acotado a sintesis local en G, geometria/pose y Peters | `docs/00-tesis.md:209-213`; `docs/01-decisiones.md:2723-2731` | si |
| `conclusiones.tex:28` | Pose del muestreador es propiedad del diseño, no resultado; E-A2 usa eje sin perturbar | `docs/01-decisiones.md:2760-2766`; implicancia 197 `docs/04-implicancias.md:12520-12529` | si |
| `conclusiones.tex:28` | Delta mide variabilidad propia, no diferencia aceptable para uso | `docs/01-decisiones.md:2709-2710`; implicancia 195 `docs/04-implicancias.md:12475-12497` | si |
| `conclusiones.tex:28` | En modelo evaluado, Delta lo fija variabilidad entre semillas | `docs/00-tesis.md:160-161`; `docs/01-decisiones.md:2298-2304` | si |
| `conclusiones.tex:30` | Cierre ocupa hueco medial en 14 de 71 | `experiments/registro/registro_2026-10-16.md:46-69`; `docs/01-decisiones.md:2743-2752` | si |
| `conclusiones.tex:30` | Pose hacia hueco ocupado recibiria brecha nula | `docs/04-implicancias.md:12499-12518`; `capitulo4.tex:264` | si |
| `conclusiones.tex:30` | Envolvente y cifras del Objetivo 2 se mantienen | `docs/01-decisiones.md:2743-2752` | si |
| `conclusiones.tex:30` | Causa de 15 corredores estrechos no establecida; fractura es confundidor | `docs/00-tesis.md:288-304`; implicancia 132 `docs/04-implicancias.md:9012-9187` | si |
| `conclusiones.tex:30` | Fractura confirmada en 20 de 30 casos | `docs/00-tesis.md:288-291`; `docs/04-implicancias.md:9012-9031,9055-9063` | si |
| `conclusiones.tex:30` | Voxel mas craneal de S1 no medido y afecta control de nivel | `experiments/registro/registro_2026-10-16.md:135-141`; `docs/01-decisiones.md:2781-2795` | si |
| `conclusiones.tex:30` | Comparacion limitada a S1 por falta de distribucion ordinal bajo ese nivel | `docs/00-tesis.md:61-65`; `docs/01-decisiones.md:2767-2770` | si |
| `conclusiones.tex:30` | Segundo corredor: eje en 69 de 72, solo geometria | `docs/00-tesis.md:61-65`; `docs/01-decisiones.md:2767-2770,2797-2803`; implicancia 198 `docs/04-implicancias.md:12531-12544` | si |
| `conclusiones.tex:34` | Ninguno de dos autoencoders examinados conserva HU a 25 HU | `docs/00-tesis.md:47-53`; `capitulo4.tex:45,236-238` | no; T01 |
| `conclusiones.tex:34` | Conservacion puede medirse antes de entrenar modelo generativo | `experiments/objetivo1/p1_compuerta.md:5`; `docs/00-tesis.md:47-53` | si |
| `conclusiones.tex:34` | Amplitud media no basta para evaluar sintetizador aprendido | `resultados_dec_2026-10-15.md:48-67,192-204`; `capitulo4.tex:252` | si |
| `conclusiones.tex:34` | Parametrico -98.9 HU frente a sintetizador -301.0 HU | `experiments/objetivo3/resultados_dec_2026-10-15.md:48-67`; `capitulo4.tex:121,170` | si |
| `conclusiones.tex:34` | Perfil y variabilidad separaron donde la media no lo hizo | `resultados_prueba_v1.md:14,36,41-42`; `capitulo4.tex:94,172,252-254` | no; T03 |
| `conclusiones.tex:36` | Aumento de datos para segmentacion no evaluado y downstream fuera de alcance | `docs/00-tesis.md:235-248`; `CLAUDE.md:5-15` | si |
| `conclusiones.tex:36` | Ningun resultado mide ayuda al entrenamiento de una red | `docs/00-tesis.md:239-243` | si |
| `conclusiones.tex:36` | CTPelvic1K: 14 de 75 volumenes con metal tienen anotacion osea | `liu2021ctpelvic1k`, Evidencia textual, filas “75 CTs”, “14 CTs”; clave y primer autor coinciden en `referencias.bib` | si |
| `conclusiones.tex:36` | La tesis aporta condicion previa separada en colocacion y apariencia | `docs/00-tesis.md:45-78,104-232` | si |
| `conclusiones.tex:36` | Muestreador y SAP evaluados sin depender del sintetizador | `CLAUDE.md:16-28`; `docs/00-tesis.md:45-78,104-112` | si |
| `conclusiones.tex:36` | Resultado de colocacion no cambia con desenlace del Objetivo 3 | Fuentes separadas: `experiments/objetivo2/e13_sap.md`; `experiments/objetivo3/resultados_prueba_v1.md` | si |
| `conclusiones.tex:36` | Uso del sintetizador como aumento carece de respaldo por realismo no reclamado | `docs/01-decisiones.md:2717-2734`; `docs/00-tesis.md:209-213,239-243` | si |
| `conclusiones.tex:1-36` | No hay marcas GAP ni `REVVISUAL` | Busqueda literal en la seccion; lint `conclusiones-r01-lint.md` | si |
| `conclusiones.tex:1-36` | No reaparecen 31-60 %, ControlNet vigente, BFC/ISC ni downstream como resultado | Busqueda literal; `CLAUDE.md:5-28`; `docs/00-tesis.md:235-257` | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Procedimiento no ejecutado resumido como evidencia obtenida | G-T4, OC-1 | “solo se examinaron dos autoencoders” | PAT-201 |
| Una dimension adicional se presenta como si corrigiera un resultado medio que ya separaba | G-T4 | “donde la media no lo hacia” | nuevo |

TOTAL alta=3 media=0 baja=0
