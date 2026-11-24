# F6 lote 7 — capitulo2.tex (modo corregir): B-026, B-028, B-030 y voz impersonal

Archivo editado: `overleaf/secciones/capitulo2.tex` (CRLF conservado: 126 líneas, 126 CR). Respaldo previo en el scratchpad de la sesión.
Lint: `python3 scripts/lint_redaccion.py capitulo2 --compilar` → PASA (alta 0, media 0, baja 0; GAP lit=1, dato=0, dec=0). PDF de 205 páginas.

## (a) Aplicado / parcial / no aplicado

| Hallazgo | Estado | Razón |
|---|---|---|
| B-026 | Parcial | La serie de Zwingmann 2009 (l.64) no se tocó. Se comprimió Zhang 2026 (solo resumen; conserva la declaración «solo se dispuso del resumen»), Zwingmann 2013 (l.66), Zwingmann 2010 (l.68) y Herman 2016 (l.70). Se quitó la frase final de l.70 («poses que no atraviesan hueso… SAP califica con grado 3»), que repite cap3:372. Las cifras de Zwingmann 2013/2010 y Herman no aparecen en ningún otro capítulo (grep en cap1, cap3, cap4, anexos, intro, conclusiones, trabajos futuros), por lo que se conservaron en prosa; el ahorro es menor que el estimado. |
| B-028 | Parcial | Sin tabla T2. Se quitó la última frase de l.104 (resultado de v2) tras comprobar que el resultado está en cap3 (l.303: anillo de 8 a 10 mm sobre el control nulo, componentes de 500 a 4000 mm³; l.647: «no se separa del control nulo más allá de 10 mm, y la banda de 12 mm lo contiene»). Se compactó l.88 (PSNR/SSIM) y l.106 (RMSE). No se quitaron SSIM ni los valores de Radzi (ver c). l.98 y l.94 sin cambios (una sola comparación por fuente, sin cifras redundantes). |
| B-030 | Aplicado | Se mantiene la contribución en cap2 (P-EA3). Se quitó el solape con la introducción: la cadena «Ningún objetivo aísla…» (3 oraciones → 1), la oración interpretativa de Xie (fusionada, conserva cifras y cita), el cierre de l.124 («se formula… como la combinación de esas piezas» → «es, por eso, su combinación») y el primer enunciado de l.126. La brecha de l.116 no se tocó: sigue idéntica a la de la introducción (G-B10). |
| Voz impersonal | Aplicado | Ver (e). |

## (b) Palabras (`texcount -brief -inc -q`)

Antes 6702; después 6575 (−127).

## (c) Cifras quitadas y dónde sí están

| Cifra quitada | Dónde está |
|---|---|
| Resultado de v2 de la última frase de l.104 (500–4000 mm³, exceso mediano medido por anillos, no se separa del control nulo pasados 10 mm) | cap3 l.303 y l.647 (Sección v2 y Amenazas) |
| Ninguna otra cifra se eliminó | — |

Cifras secundarias que NO se quitaron porque no aparecen en otro lugar, y por la regla del encargo se conservan en prosa:
- Wang et al.: SSIM 0.9501 y 0.9803 (el PSNR 26.76/32.67 dB sí está en la tabla de anexos).
- Radzi et al.: 2.0, 2.6, 1.6 y 2.0 mm; Cassanego: 3.1–4.2 mm.
- Zwingmann 2013: 2.6 % (1832) y 0.1 % (262). Zwingmann 2010: 81/11/3/5 %, 42/22/21/13 %, 2 % en grado 4, n 63/131. Herman: 36.5 %, 14.8 %, p = 0.035.
- Karageorgos RMSE 7.57, 11.45, 54.82: se conservan en cap2 l.106 como apoyo del argumento; también están en cap3 l.251, así que otro lote podría acortarlos allí o aquí sin pérdida.
Lin et al. (31.45/33.51 dB) y Li et al. (0.64 dB) quedan como están: son una cifra comparativa por fuente.

## (d) Cambios en \cite y marcas GAP

- `\cite`: ninguno añadido ni quitado (comparación del multiconjunto de `\cite{}` antes/después: idéntico). No se quitó la única oración que sostiene ninguna cita.
- `\GAPLIT`: conservado el único (l.88, fuente primaria del esquema multiventana). Sin `\GAPDATO`, `\GAPDEC` ni `\REVVISUAL` en el archivo.
- `\label`: ninguno cambiado. `\ref`: se perdieron únicamente dos apariciones repetidas (`sec:sap` en l.70 y `sec:v2` en l.104); ambas etiquetas siguen referenciadas en otras líneas del capítulo.

## (e) Oraciones con sujeto personal corregidas

| Línea | Antes | Después |
|---|---|---|
| 8 | «la brecha que este trabajo ocupa» | «la brecha que queda por ocupar» |
| 22 | «Este trabajo lee esa atribución como indicio…» | «Esa atribución se lee como indicio…» |
| 34 | «no es lo que aporta este trabajo» | «no constituye un aporte de este trabajo» |
| 66 | «este trabajo lee ese cero como efecto…» | «ese cero se lee como efecto…» |
| 70 | «este trabajo lee esa diferencia como señal…» | «esa diferencia se lee como señal…» |
| 72 | «que este trabajo toma de esa literatura» | «tomados de esa literatura» |
| 74 | «Este trabajo toma esa variación… como razón…» | «Esa variación… es razón para… y la inconsistencia, para medir…» |
| 80 | «este trabajo deja la densidad fuera de SAP» | «la densidad queda fuera de SAP» |
| 88 | «Este trabajo lee esa diferencia como indicio…» | «Esa diferencia se lee como indicio…» |
| 92 | «Este trabajo no reclama el esquema multiventana… emplea las ventanas…» | «El esquema multiventana de la MAR no se reclama aquí: las ventanas se emplean…» |
| 106 | «Este trabajo lee en esos valores una asimetría» | «En esos valores se lee una asimetría» |
| 122 | «Este trabajo lee esos valores como cobertura en exceso» | «Esos valores se leen como cobertura en exceso» |
| 126 | «La evaluación de este trabajo… este diseño lo evalúa… Este trabajo no reclama…» | «La evaluación difiere…, y aquí se evalúa… No se reclama…» |

La l.92 no figuraba entre las líneas indicadas pero tenía el mismo defecto. Las apariciones restantes de «este trabajo» son genitivos u objetos («de este trabajo», «incluye a este trabajo como una fila») y no se tocaron. Se verificó con grep que no hay «la autora», «esta tesis» ni primera persona en el archivo.

## Notas para otras rondas

- El lint marcó cuatro oraciones de más de 40 palabras que mi primera versión había creado; se dividieron antes de cerrar.
- Si la autora acepta quitar las cifras secundarias que hoy solo viven en cap2 (Zwingmann 2010/2013, Herman, SSIM de Wang, valores de Radzi), el ahorro adicional es de unas 40–60 palabras, pero eso exige una nota o un anexo donde conservarlas.
- No se tocaron MAPA, BITACORA ni ESTADO, según el encargo.
