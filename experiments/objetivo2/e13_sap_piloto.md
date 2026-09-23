# E13 — muestreo de poses y SAP (generado por `e13_muestreo_sap.py`; no elige nada)

> Distribucion de poses y metrica **preinscritas** en `preinscripcion_muestreador.md` (2026-09-22), antes de calcular este archivo. Ningun parametro se ajusto despues.

## Integridad

- Casos procesados: **2** (esperados 152).
- Poses por caso y diametro: **50**.
- Filas totales: **300**.
- Poses sin grado: **0** (debe ser 0).

- Control de pose sin perturbar (debe dar brecha 0): **2 de 2** casos pasan.

## Perturbacion efectivamente aplicada

- desvio del centro (mm): mediana **1.82**, p90 **3.97**, max **7.44**
- inclinacion (grados): mediana **1.50**, p90 **3.83**, max **5.74**

## Distribucion de grados y Wasserstein-1

| d (mm) | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |
|---|---|---|---|---|---|---|---|
| 4.91 | 100 | 86.0 | 11.0 | 1.0 | 2.0 | 0.360 | 0.755 |
| 7.0 **(SAP)** | 100 | 66.0 | 28.0 | 3.0 | 3.0 | 0.180 | 0.515 |
| 7.3 | 100 | 60.0 | 33.0 | 4.0 | 3.0 | 0.230 | 0.445 |

Referencias de `zwingmann2009navigated`: navegado **69 / 15 / 8 / 8** (26 tornillos, 24 pacientes); convencional **40 / 37 / 11.5 / 11.5** (35 tornillos, 32 pacientes). `zwingmann2010percutaneous` no entra (#113).

El W1 esta en **grados**, no en milimetros, y trata los cuatro grados como equiespaciados (convencion declarada). Su maximo posible es 3.0.

## Estados de las poses

- `ok`: **100**

## Fraccion por zona de densidad (componente 2 de SAP, reportado)

- mediana **0.561**, p25 **0.467**, p75 **0.640** sobre 100 poses

## Viabilidad de corredor (componente 3 de SAP)

- d = 4.91 mm: **100.0%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.0 mm: **100.0%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.3 mm: **50.0%** de las poses en casos con `D_TS_max >= d + 2`
