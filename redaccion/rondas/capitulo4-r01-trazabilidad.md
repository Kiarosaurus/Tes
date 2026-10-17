# Auditoria de trazabilidad — capitulo4 — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2 | `capitulo4.tex`:172 | «sin un resumen registrado» | `experiments/registro/registro_2026-10-16.md`:144-170 | Patron PAT-19 reincide. El GAP es injustificado en el estado actual del repositorio: el registro ya resume, para 13 pacientes y cada brazo, las medianas y rangos del coeficiente de Sorensen-Dice y del cambio relativo de volumen de hueso y metal. Para el modelo evaluado registra 0.677, 0.098, 0.862 y -0.190; para el protocolo fisico con titanio, 0.800, 0.121, 0.856 y 0.283. | Retirar el `\GAPDATO` e incorporar las medianas de los brazos que se comparan, con `n=13`, condicion descriptiva y sin umbral. Remitir los demas brazos al registro o tabularlos si se decide reportarlos. |
| T02 | alta | G-T4, OC-3 | `capitulo4.tex`:244 | «el muestreo de poses en el [segundo corredor] no se preinscribio ni ejecuto» | `docs/01-decisiones.md`:2767-2770; `docs/00-tesis.md`:61-67 | El pasaje sigue la decision vigente, pero dos fuentes admitidas discrepan: la decision dice que solo se midio el eje en 69/72 y que no se muestrearon poses; `docs/00-tesis.md` aun afirma que S2 se evalua descriptivamente con «geometria y grados de brecha». Por la regla del auditor, una discrepancia entre fuentes propias es alta aunque el `.tex` copie una de ellas. Patron PAT-158 reincide. | Mantener en el capitulo la formulacion de la decision de 2026-10-16 (3) y alinear la fuente de alcance: solo geometria del segundo corredor, sin poses ni grados; muestreo a trabajo futuro. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| `:10` | Resultados ordenados por objetivos; Obj. 4 define metricas; SAP acompana Obj. 2 y Peters Obj. 3 | `docs/00-tesis.md`:47-70,176-212; `overleaf/secciones/capitulo3.tex`:301-371 | si |
| `:14` | Seis combinaciones; umbral 25 HU; 34 pacientes; minimo 61.72, IC95 55.12-68.99; 34/34 fallan | `experiments/objetivo1/p1_compuerta.md`:16-25 | si |
| `:19,24-33` | Tabla compuerta: medias, IC95, medianas, 34/34 y medias en banda; banda con `n=21` | `experiments/objetivo1/p1_compuerta.md`:18-25,51-60 | si |
| `:26` | Preentrenada/publicadas: 160.13, [142.42,180.62], 136.61, 114.73 | `p1_compuerta.md`:20,55 | si |
| `:27` | Preentrenada/20000 HU: 209.39, [191.91,228.62], 190.89, 147.77 | `p1_compuerta.md`:21,56 | si |
| `:28` | Preentrenada/asinh: 164.76, [148.81,182.87], 146.60, 118.27 | `p1_compuerta.md`:22,57 | si |
| `:29` | Adaptada/publicadas: 72.91, [59.37,89.02], 53.29, 64.62 | `p1_compuerta.md`:23,58 | si |
| `:30` | Adaptada/20000 HU: 77.03, [70.12,84.65], 70.41, 88.72 | `p1_compuerta.md`:24,59 | si |
| `:31` | Adaptada/asinh: 61.72, [55.12,68.99], 53.07, 69.70 | `p1_compuerta.md`:25,60 | si |
| `:37` | Reducciones entre variantes y subgrupos 53.72/46.99/76.03 HU con `n=14/6/14` | `p1_compuerta.md`:95-116 | si |
| `:39` | Ida y vuelta: hueso 0.00/0.00/21.80; banda 13.71/13.71/15.25; mejor VAE 64.62 | `p1_compuerta.md`:29-38,51-60; `experiments/objetivo1/EXPERIMENTOS.md`:14-19 | si |
| `:41` | Sensibilidades `n=33`: 60.95 [54.28,68.19]; `n=32`: 61.08 [54.23,68.57]; maximo 2.3 HU | `p1_sin_0053.md`:10-20; `p1_sin_0072.md`:10-21; `capitulo3.tex`:54-62 | si |
| `:43` | Guo: rango no publicado; bundle -1000 a 1000 HU; cota 42.24, mediana 18.24, rango 6.96-231.43, 11/34 | `guo2025maisi`, filas N4-N8 de Evidencia; `docs/04-implicancias.md`:6766-6789 (#93 CERRADA) | si; el texto distingue articulo y guiones |
| `:47` | 3600/72 y 2450/49, 50 poses por caso, cero sin grado; control con diametro propio; perturbacion 1.66/4.09/7.49 mm y 1.48/3.61/8.22 grados | `e13_sap.md`:3-14,35-38,52-54; `e13_sap_g3.md`:3-14,45-47; `tesis/main.tex`:107-109 | si |
| `:52-74` | Tabla SAP: series clinicas, cohortes, calibres, sensibilidad, estratos y W1 | `e13_sap.md`:40-50; `e13_sap_g3.md`:33-43; `e13b_estratificado.md`:7-25; `e15_w1_sensibilidad.md`:5-10 | si |
| `:60-61,78` | Zwingmann: 24/26 y 32/35; distribuciones 69/15/8/8 y 40/37/11.5/11.5 | `zwingmann2009navigated`, Evidencia textual filas «Resultado navegado», «Resultado convencional» y tamanos de muestra | si |
| `:60-61,74,78` | Distancia propia entre series = 0.395 grados | `e13_sap.md`:48-50; `capitulo3.tex`, `sec:sap` | si; indicada como calculo del trabajo |
| `:63-65,78,82` | Primaria: 51.5/31.4/11.1/6.0, W1 0.206/0.230; calibres 4.91 y 7.3 | `e13_sap.md`:42-46 | si |
| `:66,80` | Sin 0022/0024: 70, 3500, 51.8/31.4/11.1/5.7, W1 0.203/0.237 | `e15_w1_sensibilidad.md`:5-8 | si |
| `:67-72,84` | Estratos 57/15 y 41/8, poses, grados y distancias | `e13b_estratificado.md`:7-25 | si |
| `:70,78` | Sensibilidad: 49, 2450, 54.9/30.4/9.9/4.8, W1 0.186/0.299 | `e13_sap_g3.md`:33-39 | si |
| `:80` | IC95 con 2000 remuestreos: [0.152,0.313] y [0.089,0.364]; series tratadas como fijas | `e15_w1_sensibilidad.md`:10-12 | si |
| `:82` | Monotonia con calibre y comparabilidad del calibre 7.0 mm | `e13_sap.md`:42-50; `zwingmann2009navigated`, fila «Tornillo usado» | si |
| `:84` | Mezcla anatomica y estratificacion post hoc que no sustituye la cifra principal | `e13b_estratificado.md`:1-5,27-31 | si |
| `:86` | Viabilidad `D>=9 mm`: 59.7/65.3%; calibres 4.91/7.3: 79.2/54.2% | `e13_sap.md`:60-64; `e13_sap_g3.md`:53-57 | si |
| `:92,97,104` | Primario `n=13`: -301.0 HU, IC90 [-477.0,-124.9], Delta 196.3; medianas 1308/1574 | `resultados_prueba_v1.md`:10-17; `resultados_dec_2026-10-15.md`:71-81 | si |
| `:92` | IC95 [-516.2,-85.7] y clasificacion de Lakens | `resultados_dec_2026-10-15.md`:232-235; `lakens2017equivalence`, Evidencia fila «Resultado: diferente sin equivalencia» | si |
| `:104-120` | Tabla TOST: hierro, angostos, cortes, suelo, cabeza, anillos, pareado, estado final, v2 y parametrico | `resultados_prueba_v1.md`:12-20,28-39; `resultados_dec_2026-10-15.md`:29-57,83-100,207-223 | si |
| `:105,128` | Hierro -3814.2, IC90 [-4405.9,-3222.6], intervalo bajo `-Delta` | `resultados_prueba_v1.md`:14-16; DEC 2026-10-15, lectura de desenlaces | si |
| `:106,128` | Sin tres corredores angostos: `n=10`, -261.1, [-479.8,-42.4] | `resultados_prueba_v1.md`:16 | si |
| `:107-111,134-136` | Variantes v1: -295.3, -238.3, -329.3, +478.0 y +411.7 con sus IC90 | `resultados_dec_2026-10-15.md`:35-46 | si |
| `:112,140` | Pareado: -455.0 [-647.6,-262.5], mediana 1112 y Pearson 0.02 | `resultados_dec_2026-10-15.md`:207-230; `outputs/a29/a29_perfil.md`:24-31 | si |
| `:114,128` | Estado final: -384.0 [-566.5,-201.4], margenes 115.8/196.3, minimo 566.5 | `resultados_prueba_v1.md`:17-20,34-39 | si |
| `:116-117,202` | v2: -258.9/-264.3, IC90, Delta 157.1/107.1, minimos 456.7/456.8, anillos, CV y correlaciones | `resultados_dec_2026-10-15.md`:83-100 | si |
| `:119-120,168` | Parametrico: -98.9 [-287.3,89.4], -36.3 [-191.5,118.9], diferencia 202.0 | `resultados_dec_2026-10-15.md`:48-57,61-67 | si |
| `:126` | Lectura posterior: no concluyente, menor, sin afirmar equivalencia ni no equivalencia | `docs/01-decisiones.md`:2650-2662; `resultados_prueba_v1.md`:28-39 | si |
| `:128` | Permutacion [-477.2,-124.1], diferencia <2 HU y margen minimo 477.0 | `resultados_prueba_v1.md`:28-39 | si |
| `:130` | Wilcoxon una cola `p=0.000122=2^-13`, amplitud cero, ambos puntos de control | `resultados_prueba_v1.md`:23-26 | si |
| `:134` | Fraccion en suelo: sintetizador 0.000 y protocolo Ti 0.017, maximo por paciente | `resultados_prueba_v1.md`:23-26 | si |
| `:136` | Fuera de G el sintetizador vale cero; Peters 259.5/230.8 HU; piso 184 HU | `resultados_dec_2026-10-15.md`:43-46,68-79 | si |
| `:138` | Piso 893/184; con metal 1308/1574; razones 0.69/0.12; exceso 397/1388 | `resultados_dec_2026-10-15.md`:71-81 | si |
| `:140` | Anillos pareados 725/919 y 616/727; regla de la mitad | `resultados_dec_2026-10-15.md`:182-188,207-230 | si |
| `:145,150-162` | Tabla de anillos completa, razones, percentiles, `n=10`, `n=18` y condicion de comparacion | `outputs/a29/a29_perfil.md`:1-31; `resultados_dec_2026-10-15.md`:190-223 | si |
| `:166` | Perfil plano por regla: 1.92; comparadores 2.42/3.16/6.71/4.08; meseta 727-949 HU | `outputs/a29/a29_perfil.md`:5-22; `resultados_dec_2026-10-15.md`:190-205 | si |
| `:170` | CV 0.076/0.241; Pitman-Morgan en HU y log; Pearson; Bland-Altman en HU y razon | `resultados_prueba_v1.md`:41-43; `resultados_dec_2026-10-15.md`:128-162 | si |
| `:172` | Costura 4.3/1.2; Peters RMSE 31.4 [20.1,42.4], SSIM 0.9069 [0.8268,0.9653] | `resultados_prueba_v1.md`:45-48; `resultados_dec_2026-10-15.md`:17-27 | si |
| `:172` | Integridades por brazo sin resumen registrado; `\GAPDATO` | `registro_2026-10-16.md`:144-170 | no (T01) |
| `:176,181-195` | E-A1 v1: limite 0.030, `n=13=9+4`, tabla completa de discrepancias, SDC, dVol y costura | `resultados_prueba_v1.md`:50-59 | si |
| `:204` | E-A1 v2: limites 0.05/0.2/0.030; 259.5/242.1/271.8/246.4; 4/9/9/11 de 13; 43.9/72.8/9.0 | `resultados_dec_2026-10-15.md`:102-116 | si |
| `:212-214` | Discusion Obj. 1: criterio, IC, dos autoencoders, saturacion, rediseño en imagen y error 13.71 HU | fuentes del Obj. 1 inventariadas arriba; `docs/01-decisiones.md`; `capitulo3.tex`:89-93,202-210 | si |
| `:218` | W1 del muestreador menor que 0.395; estrato viable 64.2% frente a 69%; 15 estrechos y 3.3% | `e13_sap.md`:42-50; `e13b_estratificado.md`:7-15 | si |
| `:220` | 15/72 no admiten calibre; fractura 20/30; W1 0.186/0.299 y 0.203/0.237, todos <0.395 | `tesis/main.tex`:109; `e13_sap_g3.md`:37-43; `e15_w1_sensibilidad.md`:5-10 | si |
| `:222` | SAP definida, controles de identidad/monotonia/resolucion, todas las poses; no validacion clinica | `capitulo3.tex`:194,301-329,483-485; `docs/01-decisiones.md` | si |
| `:226` | Obj. 3 implementado/evaluado; hipotesis no se sostiene; estado final fuera; decisiones post hoc y sesgos hacia equivalencia | `docs/01-decisiones.md`:2650-2668; `resultados_prueba_v1.md`:28-39; `capitulo3.tex`, `sec:amenazas` | si |
| `:228-232` | Sintesis de perfil, comparador, acuerdo, v2 y E-A1 | resultados del Obj. 3 inventariados arriba | si |
| `:236` | Realismo visual no reclamado; decision de no rediseñar; perfil, piso 0.69, p95 y v2; H5/D3/E-A4 no ejecutados | `docs/01-decisiones.md`:2717-2734,2760-2773; `resultados_dec_2026-10-15.md`:118-126 | si |
| `:238` | D9 no ejecutado; E-A2 usa eje sin perturbar; pose del muestreador solo propiedad de diseño | `docs/01-decisiones.md`:2760-2766; `capitulo3.tex`:351-369 | si |
| `:240` | Envolvente: 71/72, hueco en 71, cierre en 14, maximos 6.4 mm z y 6.3 mm AP; limites y decision | `registro_2026-10-16.md`:40-69; `docs/01-decisiones.md`:2738-2752 | si |
| `:242` | Techo/platillo: 72/72, mediana 6.5 mm, RIC 5.7-7.2; supuesto global no medido | `registro_2026-10-16.md`:110-141; `docs/01-decisiones.md`:2781-2795 | si |
| `:244` | Segundo corredor: eje 69/72, poses no preinscritas ni ejecutadas, sin distribucion ordinal bajo S1 | `docs/01-decisiones.md`:2767-2770; `capitulo3.tex`:196 | fuentes en conflicto (T02) |
| `:244` | Revision en cortes solo para 56 CLINIC-metal; revision 3D y cribado HU para receptores | `docs/01-decisiones.md`:2774-2777; registros de `experiments/exploration-3d/` | si |
| citas `:43,60-61,78,92` | Claves existentes, apellidos correctos y ninguna cita como sujeto aislado | `overleaf/referencias.bib`:463-470,682-690,1681-1690; fichas respectivas | si |
| todo el capitulo | Sin downstream como objetivo, difusion latente/ControlNet vigente, rango 31-60%, BFC o ISC | `CLAUDE.md`; `docs/00-tesis.md`; busqueda en `capitulo4.tex` | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un GAP conserva como ausente un resumen que ya fue registrado | G-T4, OC-2 | «sin un resumen registrado» | PAT-19 |
| Una fuente de alcance queda atras de una decision y contradice el resultado redactado | G-T4, OC-3 | «muestreo ... no se preinscribio ni ejecuto» | PAT-158 |

TOTAL alta=1 media=1 baja=0
