# F6 lote 1, capitulo 4: informe del redactor

Archivo editado: `overleaf/secciones/capitulo4.tex` (solo prosa; tablas, captions, `\label`, `\ref`, `\cite` y marcas GAP intactos; finales de linea CRLF conservados). Copia previa en el scratchpad de la sesion.

Lint `python3 scripts/lint_redaccion.py capitulo4 --compilar`: PASA (alta 0, media 0, baja 0; GAP 0/0/0). PDF compilado de 207 paginas. Una primera version tuvo 5 oraciones de mas de 40 palabras (E-O1); se partieron o se revirtieron.

## (a) Hallazgos

| Hallazgo | Estado | Detalle |
|---|---|---|
| B2-026 (c4:37, 39, 41) | Parcial | Se quita el IC de la mejor media (en `tab:res-compuerta`), las medias de ventanas publicadas y techo de 20 000 HU (en la tabla) y la cifra 64.62 HU de la banda (apuntaba a "mejor caso" ambiguo; la tabla la da). No se agregan filas de ida y vuelta ni de sensibilidades a la tabla (prohibido tocar tablas): los valores de ida y vuelta (0.00, 21.80, 13.71, 15.25) y las sensibilidades (60.95, 61.08 y sus IC, 2.3 HU) quedan en prosa. |
| B2-029 (c4:49, 80, 82, 84, 86) | Aplicado | Se quitan recuentos de poses y pacientes, los porcentajes de grados de las dos cohortes y de las dos series de referencia, los porcentajes por calibre (70.3 y 48.6) con sus distancias, los de la estratificacion (1.122, 0.727, 64.6, 0.175, 5.2) y los de la distribucion sin los 2 casos. Se conservan las lecturas (control de monotonia, solo 7.0 mm hace comparables los grados, mezcla de poblaciones, falta de regla de decision) y las cifras clave (0.206/0.230, 0.186/0.299, 0.395, 64.2, 3.3, 0.183, 0.482). El c4:88 (viabilidad 59.7, 65.3, 79.2, 54.2) no se toca: solo esta en prosa. |
| B2-030 (c4:242, 244) | Aplicado | 242: "los 15 estrechos" pasa a "los estrechos" (el 15 de 72 se dice en 244). 244: las distancias de sensibilidad y de la cohorte sin los 2 casos (0.186, 0.299, 0.203, 0.237) pasan a una frase con `\ref` a `tab:res-sap`; se conserva "caso negativo anatomico", 15 de 72, 20 de 30 y la escala 0.395. |
| B2-031 (c4:94, 130, 136, 138) | Parcial | Aplicado en 130: se quita la diferencia de $-261.1$ (esta en `tab:res-tost`, fila n = 10). 94, 138 y 132 no se tocan: contienen cifras solo en prosa (IC 95 %, 1308/1574, 259.5, 230.8, 184, $p$ = 0.000122, margenes minimos 477.0 y 566.5, IC exacto, fraccion en el suelo). 136 queda sin cambios, ver "Para la autora". La columna de margenes minimos y el forest plot de B2-031 no se aplican: tocan tabla o crean figura. |
| B2-032 (c4:140, 142, 168, 170) | Parcial | 140: se quitan 1308 y 1574 (ya dichos en 94). 142: se quitan 725/919 y 616/727 (en `tab:res-anillos`), queda la regla "no baja de la mitad". 168: se quitan 2.42, 3.16, 6.71, 4.08 (en la tabla); se conserva 1.92 y el rango 727-949. 170: se quitan $-301.0$ y $-36.3$ (en `tab:res-tost`); se conserva $-98.9$ y 202.0. La nota de `tab:res-anillos` (c4:164) y la figura de perfil no se tocan. |
| B2-034 (c4:176) | Aplicado | Se quitan 0.098, 0.121, $-0.190$, $+0.283$, $+1.683$ (todos en `tab:res-integridad`). Quedan los Dice (0.677/0.800, 0.862/0.856), la lectura del signo del cambio de volumen y la advertencia final. No se fusionan las tablas: tocar tablas esta fuera del lote. |
| B2-035 (c4:198) | Aplicado | Se quitan 2312.5, 198.0, 0.717, 6.3 y 9.0 (en `tab:res-ea1`). Quedan 270.9, 0.928, 199.8, 0.753 (que usa la discusion c4:256), la ausencia de umbral y la advertencia sobre la discrepancia en $M$. |
| A-009 a A-012 | Solo prosa | Se uso su criterio de comprimir narracion que transcribe tabla. Sus figuras (barras apiladas, forest plot, lineas por anillo), el reordenamiento "datos primero" y los presupuestos de palabras no se aplican: no son recortes de prosa. |
| B2-027, 028, 033 y lo demas | No aplicados | Fuera de lote, por instruccion. |

## (b) Palabras del capitulo (`texcount -brief -inc -q`)

- Antes: 5004+41+175 (13/6/69/0), total 5220.
- Despues: 4709+41+175 (13/6/60/0), total 4925.
- Diferencia: -295 palabras de texto (-5.9 %); 9 formulas inline menos.

Cada parrafo editado quedo mas corto o igual. Se agregaron 7 `\ref` a tablas existentes (`tab:res-sap` x5, `tab:res-anillos` x1, `tab:res-tost` x1, ya definidas en el capitulo) y ningun `\cite` ni cifra nuevos. El `\cite{zwingmann2009navigated}` de c4:80 se mantuvo, ahora unido a la primera mencion de las dos series.

## (c) Cifras que quedaron solo en prosa (no estan en tabla del capitulo)

- Objetivo 1: subgrupos 53.72, 46.99, 76.03 HU; ida y vuelta 0.00, 21.80, 13.71, 15.25 HU; sensibilidades 60.95 [54.28, 68.19] (33 pacientes) y 61.08 [54.23, 68.57] (32), cambio maximo 2.3 HU; saturacion de MAISI (42.24, 18.24, 6.96-231.43, 11 de 34).
- Objetivo 2: perturbacion (1.66, 4.09, 7.49 mm; $1.48^{\circ}$, $3.61^{\circ}$, $8.22^{\circ}$); IC del 95 % (0.152-0.313, 0.089-0.364, 2 000 remuestreos); series de 26 y 35 tornillos; viabilidad 59.7, 65.3, 79.2, 54.2 %.
- Contraste primario: IC del 95 % (-516.2 a -85.7), 1308 y 1574 HU, IC exacto (-477.2 a -124.1), margen minimo 477.0 y 566.5, $p$ = 0.000122 ($2^{-13}$), fraccion en el suelo (0.000 y 0.017), 259.5 y 230.8 HU de 12 a 16 mm, piso de ruido 893 y 184, cocientes 0.69 y 0.12, 397 y 1388, mediana pareada 1112, correlacion 0.02, 202.0 HU, coeficiente de variacion 0.076 y 0.241, Pitman-Morgan, correlacion 0.40, Bland-Altman, costura y preservacion (4.3, 1.2, 31.4, 0.9069 y sus rangos).
- Reconstruccion real y version 2: todo lo de c4:226 y 228 queda como estaba (fuera de lote).

## Para la autora (no resuelto aqui)

- c4:136 dice que los analisis de asimetrias "acercan la diferencia a cero", pero uno de los tres, el de $-329.3$ HU, queda mas lejos que $-301.0$. Se dejo el texto y las tres cifras tal cual, sin cambiar el sentido cientifico. Decision de redaccion o de alcance de la frase pendiente.
- c4:252 (discusion) sigue citando 1.92, 6.71 y 4.08; tras el recorte de c4:168 esas cifras ya no se dicen en los resultados, solo en `tab:res-anillos`. No se toco por no estar en la lista.

## Decisiones de redaccion

- Una cifra que aparece en prosa y en tabla se deja en prosa solo si sostiene la lectura inmediata; el resto se remite con `\ref` a la tabla.
- Al comprimir una enumeracion de la que solo se conserva una conclusion ("la serie mas cercana es la navegada / la convencional"), la conclusion se dice con palabras y se remite a la tabla, sin repetir las distancias.
