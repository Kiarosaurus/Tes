# capitulo4 — r01-puntual — respuesta del redactor

Correccion puntual sin revisores. Manda `docs/01-decisiones.md` 2026-10-16 (6) (delegada por la autora).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| Atribucion del rango de salida de MAISI (l. 45; antes asesor #3 de r01, ESCALADO) | orquestador (DEC 2026-10-16 (6) pto 1) | APLICADO | La oracion pasa a: el articulo no publica el rango; la inspeccion del codigo hecha en este trabajo lo encontro en el paquete distribuido `maisi_ct_generative`, descargado con `monai.bundle`, cuyo guion `scripts/sample.py` fija la salida entre -1000 y 1000 HU. Fuente: `docs/04-implicancias.md` #93 (CERRADA 2026-09-20: `a_min = -1000`, `a_max = 1000`, lineas 211-212, y linea 309 de `scripts/sample.py`). Sin `\cite` nuevo, sin entrada bib, sin GAP. La utilidad se nombra `\texttt{monai.bundle}` y no "de MONAI": el lint marco MONAI como sigla sin definir (E-T3) y su expansion no consta en el repositorio |
| Rango entre pacientes de E-A1 (`tab:res-ea1`) | orquestador (DEC 2026-10-16 (6) pto 2) | APLICADO | Cada celda numerica pasa a "mediana [minimo, maximo]"; significado en el `\caption`; pie reemplazado por "rango entre pacientes que prevé el diseño, descriptivo, calculado después de conocer las medianas, sin prueba de hipótesis". Fila Pacientes 9 y 4 sin cambio. Columnas ensanchadas (0.36/0.27/0.27, `\tabcolsep` 3pt) para las celdas nuevas |

## Fuente de cada cifra

Todas de `experiments/registro/registro_2026-10-16.md` §6 (`r_rango_ea1.py` sobre `a23_pacientes.csv`, control de
regresion 16/16 contra `resultados_prueba_v1.md`), copiadas sin recalcular:

| Fila | Material ortopedico (n = 9) | Objetos no ortopedicos (n = 4) |
|---|---|---|
| Discrepancia en G | 270.9 [133.7, 480.3] | 199.8 [123.7, 397.8] |
| Discrepancia en M | 2312.5 [880.3, 2710.7] | 2747.9 [1842.3, 4071.7] |
| Discrepancia en B_delta | 198.0 [129.4, 340.7] | 165.8 [118.9, 270.3] |
| Hueso SDC | 0.717 [0.640, 0.786] | 0.534 [0.518, 0.728] |
| Hueso dVol | -0.041 [-0.142, 0.088] | 0.324 [-0.033, 0.526] |
| Metal SDC | 0.928 [0.846, 0.953] | 0.753 [0.580, 0.877] |
| Metal dVol | -0.078 [-0.151, -0.036] | -0.255 [-0.318, -0.204] |
| Salto en el borde de G | 6.3 [3.4, 24.1] | 9.0 [4.4, 18.9] |

Rango [-1000, 1000] HU: #93 CERRADA. Las cifras de la cota (42.24, 18.24, 6.96-231.43, 11 de 34) no se tocaron.

## Lo que no se cambio

- Texto de l. 198 (`sec:res-reconstruccion`): no remite a la falta de rango; sin cambio.
- Pie de `tab:res-anillos`: sigue declarando que el registro no resume la dispersion de cada anillo; sin cambio.

## Efecto lateral fuera de esta seccion (no editado)

`capitulo3.tex` `sec:obj1` ("Antes de correr ese modelo se comprobo su rango de salida") deberia llevar la misma
atribucion (lo senala el reporte `capitulo4-r01-asesor.md` y la DEC (6) no lo excluye). Queda para una correccion del
cap. 3.

## Decisiones de redaccion

1. Hecho leido en el codigo de un modelo distribuido que su articulo no publica: "la inspeccion del codigo hecha en
   este trabajo", con paquete y guion en `\texttt`, sin `\cite` de software ni `\GAPLIT`; excepcion acotada a la fila
   de BITACORA §2 del 2026-10-05 (DEC 2026-10-16 (6)).
2. `monai.bundle` va en `\texttt` y nunca como sigla MONAI: su expansion no consta en el repositorio.
3. La fila de BITACORA "tabla con medianas y sin dispersion registrada" deja de aplicar a `tab:res-ea1`; sigue para
   `tab:res-anillos`.

(Las tres ya se asentaron en BITACORA §2, mas la etapa en §3.)
