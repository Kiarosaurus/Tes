# Auditoria de trazabilidad — capitulo3 — r20

Archivo: `overleaf/secciones/capitulo3.tex` (463 lineas). Respuesta revisada: `capitulo3-r20-respuesta.md`; el rechazo de usar Salimans para XCIST/CatSim se respeta y no se reabre. Se auditó el inventario completo y se rastreó de nuevo el único pasaje modificado en r20. No se abrieron PDF.

La clave `salimans2022progressive` existe en `overleaf/referencias.bib`:982; Salimans es el primer autor y “Salimans y Ho” coincide con la entrada. La parametrización de (v), la relación de varianzas y el alcance exclusivamente matemático quedan respaldados. Falta, sin embargo, una fila de evidencia textual para la ecuación del estado ruidoso que el texto también atribuye a la fuente.

**Conteo: alta=1 media=0 baja=0**

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | E-R6, G-T4 | `capitulo3.tex:202` | “el estado ruidoso es z_t = alpha_t x + sigma_t epsilon” | `docs/literatura/salimans2022progressive.md`, tabla “Evidencia textual” | La tabla acredita el proceso con preservación de varianza, `sigma_t^2=1-alpha_t^2` y `v=alpha_t epsilon-sigma_t x`, pero no contiene una fila textual para la definición de `z_t`. La ecuación aparece solo en “Dónde entra en mi tesis”, que no satisface el rastro exigido a la fila de evidencia. | Relectura con `lector-papers` para añadir la frase y ubicación exactas de `z_t` a “Evidencia textual”; hasta entonces, retirar esa ecuación o presentarla como notación propia separada de lo atribuido. |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9-40, Fig. `fig:pipeline` | Dos componentes, cuatro objetivos, alcance y estado de ejecución | `docs/00-tesis.md`; `EXPERIMENTOS.md`:57-95; `resultados_prueba_v1.md`; DEC 2026-10-13/14 | si |
| :36 | Dice/HD95 y ablaciones fuera; 14/75 y 178/1184 | `docs/00-tesis.md`, “Fuera de alcance”; ficha `liu2021ctpelvic1k` | si |
| :38 | Obj. 1 negativo; Obj. 2 ejecutado; v1 ejecutada/evaluada; realismo pendiente; v2 en curso | `EXPERIMENTOS.md`:63, :83, :92; `resultados_prueba_v1.md`; `v2_plan.md` | si |
| :42-70 | Colecciones 103/75, 178 volúmenes, 168 pacientes, 179 unidades, aislamiento y grupos | `docs/02-datos.md`:120-162; DEC 2026-10-11 (4); implicancias #132, #136, #155, #163, #166 | si |
| :48 | Umbral 2500 HU y GAP de revisión multiplanar | fichas `wang2025adaptiveweighting`, `li2024`; `docs/02-datos.md` | si |
| :54-60 | Adquisiciones repetidas, 33 pacientes, 2.3 HU, fuga y cobertura de auditorías | implicancias #156, #163, #166; `p1_sin_0053.md`, `p1_sin_0072.md` | si |
| :62-70 | Recuentos por grupo, fractura 20/30, 10/15, lector y funciones del metal | `docs/02-datos.md`:149-160; implicancias #132, #155, #163 | si |
| :72-91 | Compuerta: datos, 150 HU, MAE, 25 HU, seis combinaciones, 20.2/12.3/12.74 HU, ventanas y GAP | `experiments/objetivo1/EXPERIMENTOS.md`; fichas `karageorgos2024ddpm`, `wang2025adaptiveweighting`, `rombach2022latentdiffusion`, `guo2025maisi` | si |
| :93-119 | Corredor: 72 casos, 6/3 mm, 2 mm, 8 mm, 9.5 mm, cohortes, revisión 16=14+2 | `experiments/objetivo2/EXPERIMENTOS.md`; `preinscripcion_muestreador.md`; implicancias #123, #125, #131, #132, #136 | si |
| :95-103 | Zwingmann, Ziran 7-25/140 %, Kaiser 5/10 mm, 0.42 y TotalSegmentator | fichas `zwingmann2009navigated`, `ziran2007fluoroscopic`, `kaiser2014dysmorphism`, `wasserthal2023` | si |
| :105-113 | Envolvente, cierre 2 mm, 72 sin cambio, controles y GAP de algoritmo | `EXPERIMENTOS.md`; implicancia #131; `docs/01-decisiones.md` | si |
| :115-147, Tabla `tab:geometrias` | Marco con metal, 61/61; geometrías 4.91/7.0/7.3 mm, cabeza y materiales | implicancias #124, #163; fichas `gardner2010safezones`, `sayres2014comparison`, `synthes2003guide`, `gardner2015screw`, `zhu2022optimalposition`, `doublemedical2021trauma` | si |
| :149-192, Tabla `tab:preinscripcion` | Preinscripción del muestreador, pose, h=5 mm, sigmas, semilla, controles y segundo corredor | `experiments/objetivo2/preinscripcion_muestreador.md`; `EXPERIMENTOS.md` | si |
| :194-200 | Inpainting 2.5D, asinh, regla del suelo y sustitución de ControlNet | `diseno_A.md`; DEC 2026-10-08; implicancia #141; ficha `zhang2023controlnet` | si |
| :202 | U-Net 64 (1,2,4,8) y atención mínima | `experiments/objetivo3/diseno_A.md`; código registrado en rondas previas | si |
| :202 | Proceso con preservación de varianza y `sigma_t^2=1-alpha_t^2` | `salimans2022progressive`, evidencia “Proceso variance-preserving” y “Relación de varianzas” | si |
| :202 | `v=alpha_t epsilon-sigma_t x` | `salimans2022progressive`, evidencia “Predicción de velocidad” | si |
| :202 | `z_t=alpha_t x+sigma_t epsilon` y significado de `x`, `epsilon` | `salimans2022progressive`, sin fila correspondiente en “Evidencia textual” | **no (T01)** |
| :202 | Fuente no aporta desempeño en TC, implantes ni condicionamiento anatómico | `salimans2022progressive`, evidencia “Dominio: CT o implantes — NO ENCONTRADO”; restricción de la ficha | si |
| :204 | Coseno 1000, AdamW 1e-4, lote 16, parche 256, tres cortes, DDIM 50 y GAP lote 4/16 | `diseno_A.md`; `EXPERIMENTOS.md`; implicancia #162; fichas `song2021ddim`, `lugmayr2022repaint`, `zhang2025lefusion` | si |
| :206-210 | Cinco semillas, GPU, mezcla de canales, 0.01/0.05, recalibración 0.030/0.05 | DEC 2026-10-07; implicancias #152, #172; `resultados_validacion_pose.md`:3-6 | si |
| :212 | Banda 12 mm y cifras 7.57/11.45/11.63/54.82/57.69 HU | ficha `karageorgos2024ddpm`; `d1_d2_resultado.md` | si |
| :214-218 | Componentes, máscara 2500 HU, reglas, 0.62, 5/40, 14182/39 y 896/3 | DEC 2026-09-21; `EXPERIMENTOS.md`:26-27; `v2_plan.md` | si |
| :220-228 | Reentrenamiento, pose corregida, control 5 %/-500/150 HU, 15=2+13 y tres desplazamientos | implicancias #167, #171, #173, #174; `resultados_validacion_pose.md` | si |
| :228 | Salto del borde y GAP de medición sobre pelvis sin metal | `resultados_prueba_v1.md`:35-38; `a23_ea1.py`; DEC de diseño | si |
| :230-244 | 60000/16500 pasos; cotejo 13/7; 393/270 HU; percentiles y sensibilidad del estado final | implicancias #168, #172, #174, #175; `resultados_validacion_pose.md`:19-54 | si |
| :248-252 | Motivo post hoc de v2; diagnóstico real/sintético, 18 pacientes y anillos 0-10 mm | `resultados_prueba_v1.md`; `d1_d2_resultado.md`; DEC 2026-10-13 | si |
| :252 | 1930/1199/765/473/174 y 1697/488/97/-65/-40 HU | `experiments/objetivo3/d1_d2_resultado.md`, D1-D2 | si |
| :254 | 2888/14182, 0.2036, 45/24, 0.5, 3.91, peso 3 y 896/3 | `v2_plan.md`; `run05/run05a_meta.json`; DEC 2026-10-14 | si |
| :256-263 | Canal Gamma, lambda 0.0847/mm, 11.80 mm, hipótesis y límites físicos | fichas `park2017characterization`, `park2016MAR`, `hyung2017ml`, `xia2024pndnet`, `wang2021streak`; `b_piloto/b_resumen.md` | si |
| :265 | GAP del tornillo estrictamente convexo | implicancias #178, #181 | si (GAP justificado) |
| :265-269 | Compuerta C0-C2, 228 cortes, p=0.0085, n=13, ganancias/correlaciones y sensibilidades | `b_piloto/b_resumen.md`; `v2_plan.md`; DEC 2026-10-14 | si |
| :271 | 60000/21000 pasos, pérdidas 0.0597/0.0596/0.0540 y GPU | `run05a_curva.csv`, `run05b_curva.csv`; implicancia #168; `docs/ESTADO.md` | si |
| :273-275 | Regla 20/10 %, E=532.8/418.2/367.0, 284/540/233/279.6 HU, cotejo 13/13/9 | `run05/v2_eleccion.md`; implicancia #182; DEC 2026-10-14 (2) | si |
| :277 | Evaluación exploratoria, 13 pacientes, cinco semillas y GAP de resultados | `v2_plan.md`; DEC 2026-10-14 (2); `EXPERIMENTOS.md`:95 | si (GAP justificado al corte) |
| :281-307 | Definición de SAP, 7+2=9 mm, escala de brecha, controles, W1=0.395 y n clínicos | `preinscripcion_muestreador.md`; fichas `smith2006iliosacral`, `zwingmann2009navigated` | si |
| :315-343 | Métricas de Peters, 33=19+14, exclusión 1.62 mm, n=13, regiones y tres contrastes | ficha `peters2025hybrid`; DEC 2026-10-11 (4); `resultados_prueba_v1.md` | si |
| :347-367 | Brazos, 5371 HU/1781741/14182/39; XCIST; sonda; Fe/Ti; 13 pacientes | `EXPERIMENTOS.md`; fichas `deman2007catsim`, `wu2022xcist`, `haneda2025aapm`, `peters2025hybrid`; implicancia #174 | si |
| :353-355 | Repositorios/revisiones/licencia y GAPLIT conservada | ausencia de ficha/entrada que respalde revisiones `4cf3544`, `4993e87` y licencia; MAPA | si (GAP justificado) |
| :369-387, Tabla `tab:diseno` | Wilcoxon, TOST, 13 pacientes, Delta 196.3 HU, sensibilidad 115.8 HU y realismo | `resultados_validacion_pose.md`:49-54; `resultados_prueba_v1.md`; DEC 2026-10-09/11 | si |
| :409-435 | Amenazas internas, cronología post hoc, fuga, pose, v2 y sentido de tres elecciones | implicancias #156-#182; DEC 2026-10-09 a 2026-10-14 | si |
| :437-453 | Amenazas de constructo: envolvente, S1, escala, dirección, banda, mezcla de implantes y suelo | implicancias #138, #141, #167, #176; fichas `smith2006iliosacral`, `tejwani2014`, `lin2019`, `li2024` | si |
| :455-457 | Validez externa: Tile, 6 pelvis, 5-20 mm, 36-90 %, 20/30 y límites de transferencia | ficha `reilly2003effect`; implicancias #155, #165, #167 | si |
| :459-463 | Validez de conclusión: 26/35 tornillos, bootstrap pendiente, multiplicidad, Delta en 2, n=13 | diseño vigente; `resultados_validacion_pose.md`; `resultados_prueba_v1.md` | si |
| global | Claves de citas, E-F3 y coincidencia de primeros autores | `overleaf/referencias.bib`; búsqueda de `\cite` | si |
| global | Fabricantes identificados como documentación técnica | `capitulo3.tex`:147; fichas `synthes2003guide`, `doublemedical2021trauma` | si |
| global | Contenido retirado | `docs/00-tesis.md`; búsqueda en el `.tex` | si (solo exclusión o método sustituido) |
| global | Implicancias ABIERTAS | revisión de #90, #138, #141, #157, #158, #162, #168, #176-#182 | si (hechos medidos separados de decisiones; pendientes marcados) |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una ficha explica una ecuación fuera de “Evidencia textual”, sin dejar la cita auditable | E-R6, G-T4 | “el estado ruidoso es z_t = ...” | nuevo |
