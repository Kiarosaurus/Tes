# E12 — controles de SAP (generado por `e12_sap_control.py`; no elige nada)

## C1 — fantasma de geometria conocida

Cilindro oseo de radio **6.0 mm**, voxel isotropo de 1 mm. La brecha esperada de un cilindro de diametro `d` es `max(0, d/2 - R)`.

| d (mm) | brecha (mm) | esperado (mm) | error (mm) | grado |
|---|---|---|---|---|
| 4.91 | 0.0 | 0.0 | 0.0 | 0 |
| 7.0 | 0.0 | 0.0 | 0.0 | 0 |
| 12.0 | 0.0 | 0.0 | 0.0 | 0 |
| 14.0 | 0.917 | 1.0 | 0.083 | 1 |
| 20.0 | 3.917 | 4.0 | 0.083 | 2 |

**Error maximo frente a la geometria continua: 0.083 mm.** Es la resolucion de SAP y debe declararse junto a cualquier cifra de brecha: por debajo de ese valor la metrica no distingue.

**C2 en el fantasma:** brecha con `d = D_TS` = **0.000000 mm** (debe ser 0).

**C3 monotonia:** pasa.

## C2 y C3 — casos reales, sobre el eje del corredor de E9-TS

### `dataset7_CLINIC_metal_0008_data`

- longitud del implante (tramo del corredor) = **113.0 mm**; `L_TS_mejor_mm` del CSV = **113.0 mm**
- `D_TS_max` guardado en E9-TS = **11.3 mm**; recalculado aqui = **11.644 mm**; voxel (0.741, 0.741, 0.8) mm
- **C4** (misma envolvente que E9-TS): diferencia **0.344 mm**, dentro del redondeo a 1 decimal del CSV
- **C2:** brecha con el `D_TS_max` guardado = **0.0 mm** (tolerancia 0.05 mm, que es ese mismo redondeo); con el valor exacto = **0.0 mm** (debe ser 0)
- **C3:** brechas por diametro creciente = [0.0, 0.0, 0.0, 0.0] (no decrece)

| d (mm) | brecha (mm) | grado | frac. baja densidad | viable corredor |
|---|---|---|---|---|
| 7.0 | 0.0 | 0 | 0.711 | True |
| 4.91 | 0.0 | 0 | 0.711 | True |
| 7.3 | 0.0 | 0 | 0.711 | True |

**C5 — la metrica discrimina.** Eje inclinado alrededor del centro del corredor, cilindro de 7.0 mm:

| inclinacion (deg) | brecha (mm) | grado | estado |
|---|---|---|---|
| 0.0 | 0.0 | 0 | `ok` |
| 1.0 | 0.0 | 0 | `ok` |
| 2.0 | 0.0 | 0 | `ok` |
| 3.0 | 0.0 | 0 | `ok` |
| 5.0 | 0.156 | 1 | `ok` |
| 8.0 | 2.341 | 2 | `ok` |
| 12.0 | 5.599 | 3 | `ok` |
| 20.0 | 11.42 | 3 | `ok` |

Poses sin grado en el barrido: **0** (con la opcion (b) de #120 debe ser 0).

**C6 — los dos tramos coinciden donde ambos son validos.** Sobre el eje del corredor, que cumple las dos definiciones:

- brecha con tramo de corredor = **0.0 mm**; con tramo de pose = **0.0 mm**; diferencia **0.0 mm**
- largo del tramo: corredor 97.0 mm, pose 96.0 mm

### `dataset6_CLINIC_0002_data`

- longitud del implante (tramo del corredor) = **154.0 mm**; `L_TS_mejor_mm` del CSV = **154.0 mm**
- `D_TS_max` guardado en E9-TS = **9.2 mm**; recalculado aqui = **9.158 mm**; voxel (0.781, 0.781, 0.8) mm
- **C4** (misma envolvente que E9-TS): diferencia **0.042 mm**, dentro del redondeo a 1 decimal del CSV
- **C2:** brecha con el `D_TS_max` guardado = **0.021059 mm** (tolerancia 0.05 mm, que es ese mismo redondeo); con el valor exacto = **0.0 mm** (debe ser 0)
- **C3:** brechas por diametro creciente = [0.0, 0.0, 0.0, 0.0] (no decrece)

| d (mm) | brecha (mm) | grado | frac. baja densidad | viable corredor |
|---|---|---|---|---|
| 7.0 | 0.0 | 0 | 0.554 | True |
| 4.91 | 0.0 | 0 | 0.554 | True |
| 7.3 | 0.0 | 0 | 0.554 | False |

**C5 — la metrica discrimina.** Eje inclinado alrededor del centro del corredor, cilindro de 7.0 mm:

| inclinacion (deg) | brecha (mm) | grado | estado |
|---|---|---|---|
| 0.0 | 0.0 | 0 | `ok` |
| 1.0 | 0.0 | 0 | `ok` |
| 2.0 | 0.0 | 0 | `ok` |
| 3.0 | 0.0 | 0 | `ok` |
| 5.0 | 0.0 | 0 | `ok` |
| 8.0 | 2.604 | 2 | `ok` |
| 12.0 | 6.87 | 3 | `ok` |
| 20.0 | 16.037 | 3 | `ok` |

Poses sin grado en el barrido: **0** (con la opcion (b) de #120 debe ser 0).

**C6 — los dos tramos coinciden donde ambos son validos.** Sobre el eje del corredor, que cumple las dos definiciones:

- brecha con tramo de corredor = **0.0 mm**; con tramo de pose = **0.0 mm**; diferencia **0.0 mm**
- largo del tramo: corredor 138.0 mm, pose 138.0 mm

> El eje de E9-TS es el **mejor** corredor del caso, no una pose muestreada. Sus grados son 0 por construccion y **no son un resultado de SAP**: son el control de que la metrica no inventa brechas donde no las hay.

## Limites declarados

- La envolvente viene de TotalSegmentator, que segmenta **hueso**, no cortical. Su borde **aproxima** la superficie cortical externa.
- La brecha se mide **radialmente**, en el plano perpendicular al eje. Coincide con la protrusion para una cortical localmente plana.
- Resolucion de la metrica: **0.083 mm** sobre geometria conocida con voxel de 1 mm.
- Las poses sin travesia osea suficiente se califican **grado 3** y su estado se reporta (#120, opcion (b), decidida el 2026-09-22). Ninguna pose se queda sin grado.
