# Respuesta del redactor — capitulo4 — r01

Modo: corregir. Encargo: `redaccion/ENCARGO_2026-10-16.md` (una ronda). Reportes leidos: `-lint`, `-guia`,
`-estilo`, `-trazabilidad`, `-asesor`.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | §Obj 1: el primer parrafo da la poblacion (34), la medida, el criterio (25 HU) y la tabla; el veredicto negativo, la menor media y el 34/34 pasan a un parrafo nuevo despues de `tab:res-compuerta`. §Contraste primario: el primer parrafo da la comparacion, n = 13, la diferencia, IC90, IC95, margen y medianas; la categoria (no concluyente, con la razon en los limites del margen, PAT-171), la direccion y la lectura de Lakens pasan al parrafo posterior a `tab:res-tost`, fundidas con el que ya daba la lectura de DEC 2026-10-15 (3), sin repetir la oracion "no se lee como equivalencia ni como no equivalencia" |
| guia-2 | guia | APLICADO (parcial, limitacion declarada) | Ninguna fuente registra la dispersion por anillo (`outputs/a29/a29_perfil.md` y `a29_perfil.json` solo dan medianas por anillo y p25/p75 de la razon) ni el rango de E-A1 (`resultados_prueba_v1.md` solo da medianas por grupo). No se calculo nada. Pie de `tab:res-anillos`: el registro no resume la dispersion por anillo; la de la razon esta en la ultima fila y la de la diferencia en 8-12 mm, en `tab:res-tost` (IC90). Pie nuevo de `tab:res-ea1`: el diseno preve el rango entre pacientes (cap. 3 `sec:ap-reconstruccion`, l. 369), el registro solo resume medianas y el valor por paciente consta en la salida (`a23_pacientes.csv`). En l. 10, "su variabilidad" pasa a "su variabilidad cuando consta en el registro". Nota para la autora: el rango de E-A1 que el diseno promete es un calculo barato (clase C) sobre `a23_pacientes.csv`; no abro GAP por la meta del encargo |
| ES-01 | estilo | APLICADO | "es exacta en el hueso" -> "tuvo un error medio de 0.00~HU en el hueso"; la oracion siguiente ("Esa exactitud no se extiende") pasa a "En la banda $B_{\delta}$, ese error sube a 13.71~HU". Fuente: `p1_compuerta.md`:33-38 |
| ES-02 | estilo | APLICADO | Se retira "la del modelo con canal se sostiene en parte"; la oracion previa nombra cada modelo con su recuento: 4 y 9 de 13 con 0.030, 9 y 11 con su limite propio (`resultados_dec_2026-10-15.md`:102-116). La lectura ("la ventaja desaparece") queda en la discusion, l. de implantes reales |
| ES-04 | estilo | APLICADO | "Su caso negativo coincide con la condicion..." -> "La concordancia del metal fue menor en los objetos no ortopedicos, que estan fuera de la distribucion de entrenamiento: su coeficiente de Sorensen-Dice bajo de 0.928 a 0.753" |
| ES-05 | estilo | APLICADO | Se elimina "Lo medido sobre ese realismo es negativo o parcial"; la oracion siguiente abre con "En las mediciones de este capitulo, el perfil es plano, ..." y se parte en dos (lint E-O1) |
| ES-06 | estilo | APLICADO (variante) | Se elimina la oracion de cierre en lugar de sustituirla: repetia la apertura del parrafo ("La pose del muestreador no interviene en ningun resultado del Objetivo 3"), PAT-98. La propuesta del revisor invertia la relacion causal (el capitulo no evalua por separado *por* esa independencia) |
| T01 | trazabilidad | APLICADO | Mismo punto que asesor #1. Se retira el `\GAPDATO` de l. 172 y se escribe el texto del asesor en un parrafo propio (el original pasaba de 7 oraciones, PAT-58), con una tabla nueva `tab:res-integridad` (modelo evaluado, Ti, Fe; mediana [min, max], n = 13), que atiende tambien guia-2 para estas medidas. El estado final y la copia y pegado no se tabulan (asesor: no hacen falta en el texto). Fuente: `experiments/registro/registro_2026-10-16.md` §5 |
| T02 | trazabilidad | ESCALADO | El pasaje de l. 244 (segundo corredor: eje 69/72, poses no preinscritas ni ejecutadas) sigue DEC 2026-10-16 (3) y no se toca. La discrepancia esta en `docs/00-tesis.md`:61-67 ("geometria y grados de brecha" en S2), que el redactor no edita (regla 14 raiz). Para la autora: alinear `00-tesis.md` con DEC 2026-10-16 (3) |
| asesor #1 | asesor | APLICADO | Ver T01 |
| asesor #2 | asesor | APLICADO (opcional) | Celda "No equivalencia, menor" sin cambio (D15). Pie de `tab:res-tost`: "Solo la primera fila es confirmatoria; en las demas, la regla de desenlaces se aplica como descripcion" |
| asesor #3 | asesor | ESCALADO | Clase B. Atribucion del rango [-1000, 1000] HU a los guiones del bundle MONAI (l. 43) sin cita ni `\GAPLIT`. No se cambia la oracion ni se abre GAP. Decision de la autora entre (a) sin cita de software, (b) entrada nueva en `refs/raw/`, (c) `\GAPLIT`; texto listo en `capitulo4-r01-asesor.md`. Si elige (a), afecta tambien `capitulo3.tex`:93 |
| ES-03 (baja) | estilo | APLICADO | "Las direcciones que esos resultados abren se recogen..." -> "Las evaluaciones que no se ejecutaron se proponen en el capitulo de trabajos futuros" |

## Fuente de cada cifra nueva

| Cifra (capitulo4.tex) | Fuente |
|---|---|
| Hueso SDC 0.677 [0.586, 0.775], 0.800 [0.736, 0.876], 0.707 [0.599, 0.865] | `experiments/registro/registro_2026-10-16.md` §5, tabla de resultado |
| Hueso dVol 0.098 [-0.094, 0.340], 0.121 [-0.002, 0.319], 0.043 [-0.124, 0.349] | idem |
| Metal SDC 0.862 [0.769, 0.903], 0.856 [0.820, 0.892], 0.518 [0.503, 0.668] | idem |
| Metal dVol -0.190 [-0.367, -0.084], +0.283 [-0.117, 0.334], +1.683 [0.989, 1.785] | idem |
| n = 13, mediana de 5 semillas / 2 replicas por paciente; umbrales 150 y 2500 HU | idem, lineas "Script" y "Fuente"; cap. 3 l. 371 |

Las demas cifras movidas (61.72, 55.12-68.99, 34/34, -301.0, IC90, IC95, 1308/1574, 4/9/9/11, 0.00, 13.71) son
las de r00, solo reubicadas; su fuente sigue en `capitulo4-r00-respuesta.md`.

## Lint

`python scripts/lint_redaccion.py capitulo4 --compilar`: PASA, alta=0 media=0 baja=0; GAP lit=0 dato=0 dec=0. Tras
la primera pasada marco tres oraciones de mas de 40 palabras (l. 176, 227, 259, todas mias); se partieron.

## Para la autora

1. T02: `docs/00-tesis.md`:61-67 atrasado frente a DEC 2026-10-16 (3) (S2 solo con geometria del eje; sin poses ni
   grados).
2. asesor #3: decision sobre la atribucion del rango del bundle MONAI (texto listo en el reporte del asesor).
3. guia-2: el rango entre pacientes de E-A1, que el diseno promete (cap. 3 l. 369), no esta registrado; calculo
   barato sobre `a23_pacientes.csv` si se quiere cerrar en una ronda siguiente.
4. Pendiente del asesor fuera de mi permiso: fila en `experiments/objetivo3/visto.md` por el resumen de §5.

## Decisiones de redaccion

- Cuando una tabla de resultados resume pacientes con medianas y el registro no trae dispersion, el pie de la tabla
  lo declara ("el registro no resume la dispersion ...; el valor de cada paciente consta en la salida de la corrida")
  y remite a la dispersion que si exista en otra tabla. No se abre GAP ni se calcula.
- Rango entre pacientes en tablas: formato "mediana [minimo, maximo]" en la celda, con el significado en el
  `\caption`.
- Secciones de resultados: el primer parrafo da poblacion, medida, criterio y tabla; la categoria o el veredicto va
  en el parrafo posterior a la tabla (G-C10).
