# Auditoria de trazabilidad — capitulo3 — r27

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-3 | `capitulo3.tex:31,38,369,455,457,474,493,519` | «realismo frente a tornillos reales» | `docs/01-decisiones.md:2717-2736`; `docs/04-implicancias.md:12438-12455`; `redaccion/ENCARGO_2026-10-16.md:33-36` | El contraste H5 y la comparacion D3 se presentan como partes pendientes de la evaluacion, y la tabla conserva resultados de realismo por producir. La decision vigente establece que no se ejecutan ni se prometen, que pasan a trabajo futuro y que los `\GAPDATO` de realismo dejan de ser GAP. Es contenido retirado presentado como vigente; el patron PAT-200 reincide. | Dar un estado unico: «disenados y no ejecutados; trabajo futuro». Retirar sus `\GAPDATO`, la referencia de realismo como cohorte existente y toda lectura que afirme realismo visual. Conservar solo las limitaciones cuantificadas por perfil, piso, percentil 95, contraste pareado y version 2. |
| T02 | alta | G-T4, OC-1 | `capitulo3.tex:365-367` | «La autora revisa ademas laminas de una muestra fija» | `docs/01-decisiones.md:2600-2605`; `experiments/objetivo3/EXPERIMENTOS.md:111-112`; `capitulo3-r27-asesor.md`, B-4 | La decision fija el protocolo E-A4, pero no acredita su ejecucion. El indice experimental solo registra D9, D3 y H5 como no hechos y no contiene el control de 13 pacientes por tres laminas y cuatro defectos. La inspeccion de #176 no siguio esa regla. La afirmacion propia carece de fuente. | Escribir que el control se fijo y que no consta ejecutado. Si la autora confirma que no se hizo, declararlo «no ejecutado»; si se hizo, registrar laminas y defectos antes de afirmarlo. |
| T03 | alta | G-T4, OC-2 | `capitulo3.tex:533` | «Las poses perturbadas ... se examinan en un analisis exploratorio» | `capitulo3.tex:349`; `experiments/objetivo3/EXPERIMENTOS.md:111-112`; `redaccion/ENCARGO_2026-10-16.md:28,43-44` | La misma seccion marca el resultado D9 como faltante y el indice experimental dice «falta D9»/«POR ESCRIBIR». «Se examinan» afirma una ejecucion inexistente. El patron PAT-122 reincide. | Cambiar por «se fijo un analisis exploratorio, que no consta ejecutado» y mantener el mismo estado en `:349` y `:533`; la decision de convertirlo en trabajo futuro sigue reservada a la autora. |
| T04 | alta | G-T4 | `capitulo3.tex:345,519` | «los extremos ... encuentran las rayas claras y las oscuras» | `capitulo3.tex:519`; `docs/01-decisiones.md:2723-2734`; #193 (`docs/04-implicancias.md:12438-12455`) | La justificacion de los anillos atribuye estructura de raya a un estadistico de colas. El propio capitulo reconoce en `:519` que la amplitud crece con cualquier desviacion extrema y no distingue una raya de textura sin direccion. No hay fuente que sostenga la identificacion. | Decir que el estadistico toma los extremos de HU sin orientar el anillo ni atribuirles estructura de raya. Mantener la ausencia de medicion direccional como limitacion, no como `\GAPDATO`. |
| T05 | media | G-T4, OC-2 | `capitulo3.tex:287` | «la prueba ... no separa [las secciones] estrictamente convexas» | `experiments/registro/registro_2026-10-16.md:69-99`; `experiments/objetivo3/EXPERIMENTOS.md:113`; `capitulo3-r27-asesor.md`, GAP 4 | El patron PAT-19 reincide parcialmente. La estratificacion posterior ya separa secciones compactas de alargadas o multiples y registra, para el corte 1.5, ganancias 0.079/0.111 y neta 0.012 frente a 0.201/0.148 y neta 0.148. Lo que sigue sin medirse es el efecto del canal sobre la salida del modelo. | Sustituir la negacion y el GAP amplio por el resultado descriptivo, con sus limites (sustituto geometrico, 11 cortes compactos con control, sin prueba). Declarar aparte que no se midio el efecto del canal sobre la salida del modelo. |
| T06 | media | G-T4, OC-2, OC-3 | `capitulo3.tex:513` (primer GAP) | «comprobacion de que la envolvente ... deja fuera el canal» | `docs/01-decisiones.md:2738-2752`; `experiments/registro/registro_2026-10-16.md:27-57`; #196 (`docs/04-implicancias.md:12494-12513`) | El patron PAT-19 reincide. La decision #196 ordena cerrar el GAP y declarar la limitacion con la medicion de cohorte: reproduce 71 de 72 casos; el cierre ocupa el hueco medial en 14, hasta 6.4 mm en z y 6.3 mm AP. La medicion no identifica el canal, no mide foramenes ni brecha, por lo que tampoco permite afirmar que la envolvente los deje fuera. | Retirar el GAP y escribir la evidencia descriptiva y sus limites exactamente como fija la decision; no convertir el hueco medial en canal anatomico. |
| T07 | media | G-T4, OC-2 | `capitulo3.tex:513` (segundo GAP) | «esa diferencia no esta medida» | `experiments/registro/registro_2026-10-16.md:101-126`; `experiments/objetivo2/EXPERIMENTOS.md:93`; #138 (`docs/04-implicancias.md:9707-9730`) | PAT-19 y PAT-133 reinciden. Ya esta medida la diferencia usada por el control de nivel en la columna media: 72 casos, mediana 6.5 mm, RIC 5.7-7.2, rango 3.7-15.4. No esta medida la distancia desde el voxel mas craneal de toda la etiqueta, que podria caer en la cresta sacra media. El GAP actual mezcla ambas. | Dar la medicion de la columna media y declarar sus limites: cohorte truncada por seleccion, platillo heuristico y voxel mas craneal global sin medir. Si se conserva una marca, reducirla solo a esa ultima distancia; el encargo busca declararla como limitacion. |

## Inventario
| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| `:9-15` | Cadena de dos componentes; compuerta; cuatro objetivos; $G=M\cup B_\delta$ | `docs/00-tesis.md`; `docs/01-decisiones.md`; `tesis/main.tex` | si |
| `:20-32` | Figura: compuerta negativa, muestreador, sintetizador y evaluaciones | `docs/00-tesis.md`; `experiments/objetivo1/EXPERIMENTOS.md`; `experiments/objetivo2/EXPERIMENTOS.md`; `experiments/objetivo3/EXPERIMENTOS.md` | no en la parte de realismo (T01) |
| `:36` | Segmentacion posterior fuera de alcance; 75/14; inventario local 178/1184 | `CLAUDE.md`; `docs/00-tesis.md`; `liu2021ctpelvic1k`, tabla Evidencia; `docs/02-datos.md` | si |
| `:38-40` | Estado de ejecucion, dos receptores, fechas 9/11/12 de octubre y pose corregida | `docs/01-decisiones.md`; `experiments/objetivo3/EXPERIMENTOS.md`; `resultados_validacion_pose.md` | si, salvo H5/D3 (T01) |
| `:44` | CTPelvic1K 1184; local 178 = 103+75; correspondencia inferida | `docs/02-datos.md`; `liu2021ctpelvic1k`, tabla Evidencia | si |
| `:46` | Adquisicion/reconstruccion no reportadas; MAR cambia apariencia | `liu2021ctpelvic1k` y `selles2024marreview`, tablas Evidencia | si |
| `:48` | Cribado >2500 HU; revision 3D de 178; multiplanar sin constancia | `experiments/exploration-3d/revision.csv`; `README.md:58-60`; `tornillos_conteo.csv` | si (GAP justificado; decision B-3 pendiente) |
| `:50` | 178 volumenes, 168 pacientes, grupos 65/37/66; 179 unidades; 10 fuera | `docs/02-datos.md`; registros de identidad y grupos de `experiments/exploration-3d/` | si |
| `:52` | Particion: validacion 8, prueba 34; Obj. 2 sin division | `docs/02-datos.md`; `experiments/objetivo1/EXPERIMENTOS.md`; `docs/01-decisiones.md` | si |
| `:54-62` | Duplicados; prueba 33; cambio maximo 2.3 HU; 166 volumenes/159 pacientes; 118/8/33 | `docs/02-datos.md`; `p1_sin_0053.md`; auditorias de identidad registradas | si |
| `:64` | Embudo Obj. 2: 103, 91, 72; exclusiones 11/34 y 7/57; sensibilidad 49 | `experiments/objetivo2/EXPERIMENTOS.md`; `ts_analisis.md`; preinscripcion | si |
| `:66-68` | Cribado 30=15+15; fractura 20/30; 10/15 por estrato; laminas 18 y volumen 12 | registro del cribado; #132; DEC 2026-10-08 | si |
| `:70` | Cuatro usos de casos con metal; tres pacientes confirman fragmentacion | auditoria local y revisiones de tornillos; decisiones de geometria | si |
| `:74-81` | Regla Go/No-Go; exploracion previa 178; MAE en hueso | `docs/01-decisiones.md`; `experiments/objetivo1/EXPERIMENTOS.md` | si |
| `:76` | Umbral oseo 150 HU atribuido al protocolo | `peters2025hybrid` y `haneda2025aapm`, tablas Evidencia | si |
| `:83` | RMSE 20.2/12.3/12.74 HU; RMSE no menor que MAE | `karageorgos2024ddpm`, `peters2025hybrid`, `yun2026simulationdriven`, tablas Evidencia | si |
| `:85-89` | Seis combinaciones; ventanas; ajuste L1/AdamW; 30000 pasos; regla 25 HU/34 pacientes/IC95 | `registro_metodos_2026-10-15.md` §§1-2; `experiments/objetivo1/EXPERIMENTOS.md` | si |
| `:91-93` | Banda real de 12 mm; extension al autoencoder de Guo y cota de saturacion | `docs/01-decisiones.md`; `rombach2022latentdiffusion` y `guo2025maisi`, tablas Evidencia | si |
| `:97` | Dos series de malposicion; CV 7-25% y hasta 140% | `zwingmann2009navigated` y `ziran2007fluoroscopic`, tablas Evidencia | si |
| `:101-109` | Marco, 5 mm, mascara, 0.42, TotalSegmentator 2.18, recortes 6/3 mm, cierre 2 mm, rejilla y 81 direcciones | `kaiser2014dysmorphism`; `registro_metodos_2026-10-15.md` §§3-4; `experiments/objetivo2/EXPERIMENTOS.md` | si |
| `:111-115` | Viabilidad; mediana 9.5, RIC 7.4-11.7; porcentajes y 29/27; revision 16=14+2; sensibilidad 70 | `experiments/objetivo2/EXPERIMENTOS.md`; `e15_w1_sensibilidad.md` | si |
| `:119-125` | Heuristica de referencias, umbrales, 69/66, cohorte metal 64/57/48/29/17/3, acuerdo 61/61 | `registro_metodos_2026-10-15.md` §4; registros de aplicabilidad y laminas | si |
| `:129-153` | Tipo y tres geometrias; 4.91/8.0/4.5/7.0 mm; 79 componentes/43 volumenes; aleaciones | fichas `mclaren2021corridor`, `gardner2010safezones`, `kaiser2014dysmorphism`, `sayres2014comparison`, `synthes2003guide`, `gardner2015screw`, `zwingmann2009navigated`, `doublemedical2021trauma`; auditoria local | si; fabricantes identificados como documentacion tecnica (P-EA1) |
| `:157-190` | Preinscripcion 22-09; ecuacion de pose; $h=5$, 50 poses, semilla; 95%; segundo corredor 18 casos y eje 69/72 | `preinscripcion_muestreador.md`; `kaiser2014dysmorphism`; registros del segundo corredor | si; ejecucion del segundo corredor sigue como GAP B-2 |
| `:196-198` | Densidad fuera de SAP; fenotipo no estratificado | decisiones vigentes; `arand2019pelvicring`, `gardner2010safezones`, tablas Evidencia | si |
| `:202-218` | Difusion 2.5D en imagen; suelo; 225.0/1.2/196.3 HU; $v$; U-Net; lote 16; 5 semillas; limites 0.05/0.030 | `docs/01-decisiones.md`; `experiments/objetivo3/EXPERIMENTOS.md`; `salimans2022progressive`, `song2021ddim`, `lugmayr2022repaint`, `zhang2025lefusion`, tablas Evidencia | si |
| `:208` | Stable Diffusion/ControlNet descritos como formulacion sustituida | `docs/00-tesis.md`; `zhang2023controlnet`, tabla Evidencia | si; no se presentan como metodo vigente |
| `:220` | Banda 12 mm y cifras de sensibilidad de mascara 7.57/11.45/11.63/54.82/57.69 | `karageorgos2024ddpm`, tabla Evidencia; decisiones de diseno | si como apoyo de sentido, no del ancho |
| `:222-240` | Mascaras; -0.24 mm; razon 0.638=5526/8656; 14182/39 y 896/3; pose y controles; 60000/16500 | `registro_metodos_2026-10-15.md` §7; `experiments/objetivo3/EXPERIMENTOS.md`; `resultados_validacion_pose.md` | si |
| `:242-260` | Cotejo: dos receptores/tornillos; cáscaras; 13/24 frente a 7; HU y amplitudes; diagnostico D7 | `resultados_validacion_pose.md`; `resultados_dec_2026-10-15.md`; `EXPERIMENTOS.md:108-111` | si; la lectura de realismo debe reformularse por T01 |
| `:264-270` | v2 posterior; IC90 por anillo; excesos reales y sinteticos; alcance 10/12 mm | `d1_d2_resultado.md`; `registro_metodos_2026-10-15.md` §5; #193 | si en cifras; solo como limitacion cuantificada |
| `:272-285` | 2888/14182, 0.2036, 45/24, fraccion 0.5, factor 3.91; canal y prueba 0.0067/0.0902/1.000/0.116/$p=0.0085$ | `v2_plan.md`; `b_piloto`; fichas `park2017characterization`, `park2016MAR`, `hyung2017ml`, `xia2024pndnet`, `wang2021streak` | si |
| `:287` | Secciones convexas no separadas y GAP #178 | `registro_2026-10-16.md` §3; `EXPERIMENTOS.md:113` | parcial/no (T05) |
| `:289-297` | v2: 60000/21000; regla $E$; 532.8/418.2/367.0; salvaguarda; evaluacion exploratoria | `run05/v2_eleccion.md`; `resultados_dec_2026-10-15.md`; decisiones 15-10 | si, salvo D3/H5 (T01) |
| `:301-329` | SAP; formula y grados; tramo sin 8 mm; seis controles y 0.083 mm; distribuciones 69/15/8/8 y 40/37/11.5/11.5; W1 0.395; 26/24 y 35/32; 15/72 | preinscripcion; `experiments/objetivo2/EXPERIMENTOS.md`; `zwingmann2009navigated`, `smith2006iliosacral`, tablas Evidencia | si |
| `:335-339` | Metricas de Peters; 150 HU; colas 5%; RMSE/SSIM fuera de $G$ | `peters2025hybrid`, tabla Evidencia; `resultados_dec_2026-10-15.md` | si |
| `:343-351` | Prueba 33; 19/9/10/14; exclusion 1.62 mm; n=13; 3.1/3.6/4.7 y sensibilidad n=10 | `docs/02-datos.md`; `resultados_prueba_v1.md`; EXP3 | si |
| `:345` | Colas identifican rayas sin orientar el anillo | ninguna fuente; contradice `:519` | no (T04) |
| `:349,533` | D9: 5 poses, 5 semillas, sin comparador; ejecucion | DEC 15-10 pto 9; `EXPERIMENTOS.md:111-112` | diseno si; ejecucion no (T03) |
| `:353` | Todos los cortes de $G$; ejemplo 51/25; dominios distintos por brazo | decisiones del diseno; registro de validacion | si |
| `:357-361` | Reconstruccion: 19 de diseno, 13 efectivos=9+4; 500 mm3; 24 cortes; 5 semillas; integridades | `experiments/objetivo3/EXPERIMENTOS.md`; diseno congelado/enmienda | si |
| `:365-367` | Criterio primario y control visual 13x3 con cuatro defectos | DEC 15-10 pto 10; sin registro de ejecucion | no en ejecucion (T02) |
| `:369` | Tres contrastes, incluido realismo | DEC 16-10 ptos 1-3 | no (T01) |
| `:373-377` | Copia-pega 5371 HU de 1781741 voxeles/14182 parches/39 casos; artefacto parametrico | `a20_resultados_run04.md`; `resultados_dec_2026-10-15.md`; EXP3 | si |
| `:379-383` | Protocolo Peters: 900 columnas/1000 vistas/64 filas; implementacion de repositorios | fichas `peters2025hybrid`, `xcist2026main`, `xcist2025example` | si |
| `:394-403` | Cinco desviaciones; 459 mm; commits y BSD; parche local | decisiones y registro de reproduccion; repositorios citados | si |
| `:405-417` | Sonda: 72 h, ±20 HU, 2%, triple; segundo intento; 1/2 cortes; Fe/Ti; amplitudes y 2/24 frente a 0/24 | diseno y resultados de validacion; `peters2025hybrid`, tabla Evidencia | si |
| `:421-433` | Wilcoxon 0.05 y $2^{-13}$; TOST, IC90, n=13, $\Delta=196.3$; IC95 excluye 0; $s=196.3$, $r=6.1$, Ti 8/27, estado final 115.8 | `resultados_prueba_v1.md`; `resultados_dec_2026-10-15.md`; DEC 15-10; fichas `walker2011understanding`, `lakens2017equivalence`, `haber2008general` | si |
| `:435-451` | Permutacion $2^{13}$; suelo; piso; perfiles; pareado; Bland-Altman/Pitman-Morgan; CV 0.076/0.241 | `resultados_dec_2026-10-15.md`; fichas `bland1986statisticalmeasurement`, `bland1996statisticsmeasurement`, `pitman1939note`, `morgan1939test` | si |
| `:455-457` | Contraste H5 y referencia real pendientes | DEC 16-10 pto 2-3 | no como GAP o evaluacion vigente (T01) |
| `:472-474` | Tabla: 2x3, n=34; n=72/49; n=13/19; IC95; $\Delta$ | fuentes experimentales de los tres objetivos | si, salvo celdas de realismo (T01) |
| `:483-485` | Post hoc Obj. 2; 10/15 y 10/15; sacra desplazada 7/15 frente a 2/15, $p=0.109$ | `registro_metodos_2026-10-15.md` §6; cribado | si |
| `:487-499` | Fuga Obj. 1; n=32; cronologia de decisiones, pose y modelo afectado | `p1_sin_0072.md`; decisiones; EXP3 | si |
| `:501-505` | v2 posterior y dos tandas del 15-10 | `docs/01-decisiones.md` 15-10 y 15-10 (3) | si, salvo procedimientos visuales ya retirados (T01/T02) |
| `:507-511` | Tres elecciones sobre dos receptores; 196.3/115.8; aislamiento no exhaustivo | resultados de validacion; auditorias de identidad | si |
| `:513` | Canal/foramen y techo/platillo como GAP | DEC 16-10 (2); `registro_2026-10-16.md` §§2,4 | no (T06, T07) |
| `:515-517` | Resolucion desconocida; 2.5 frente a 5.0 mm, $p=0.3$; S1 supuesto | `tejwani2014`, `zwingmann2009navigated`, tablas Evidencia | si |
| `:519-529` | Metrica no distingue direccion; truncamiento; 19/39; supuestos de imagen; suelo; brazos frente a real | DEC 16-10; #193; EXP3; fichas `lin2019`, `li2024` | si como limitaciones; no como GAP de realismo (T01/T04) |
| `:531` | Seis pelvis; 5-20 mm; reduccion 36-90%; fractura 20/30 | `reilly2003effect`, tabla Evidencia; cribado propio | si |
| `:533` | No transferencia; D9; 56 sin tornillo transiliaco-transsacro | auditoria local; EXP3 | no para «se examinan» (T03); resto si |
| `:535-541` | IC95 W1 2000 remuestreos; 26/35; n=13; limites de acuerdo; margen en dos pacientes | `e15_w1_sensibilidad.md`; `EXPERIMENTOS.md`; fichas estadisticas; #195 | si |
| `:543-547` | 62341/124679 voxeles; pisos 893/184 HU; pareado -455.0, IC90 [-647.6,-262.5]; suelo -1000 | `resultados_prueba_v1.md`; `resultados_dec_2026-10-15.md`; DEC 15-10 (3) | si |
| todas las citas | 48 claves existen; apellidos nombrados coinciden; ninguna cita es sujeto gramatical aislado | `overleaf/referencias.bib`; fichas respectivas | si |
| todo el capitulo | No presenta Dice/HD95 como objetivo, ni latente/ControlNet como metodo vigente, ni 31-60%, BFC o ISC | `CLAUDE.md`; `docs/00-tesis.md` | si |

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un analisis decidido como no ejecutado sigue figurando como evaluacion pendiente con GAP | G-T4, OC-3 | «realismo frente a tornillos reales» | PAT-200 / PAT-122 |
| Un procedimiento fijado se redacta como ejecutado sin registro de su ejecucion | G-T4 | «La autora revisa ademas laminas» | nuevo |
| Un calculo posterior cierra parte de un GAP, pero el GAP conserva su formulacion completa | G-T4, OC-2 | «esa diferencia no esta medida» | PAT-19 / PAT-133 |
| Una metrica de extremos recibe el nombre del mecanismo que no distingue | G-T4 | «encuentran las rayas claras y las oscuras» | nuevo |

TOTAL alta=4 media=3 baja=0
