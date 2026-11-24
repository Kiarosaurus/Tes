# E13 — muestreo de poses y SAP (generado por `e13_muestreo_sap.py`; no elige nada)

> Distribucion de poses y metrica **preinscritas** en `preinscripcion_muestreador.md` (2026-09-22), antes de calcular este archivo. Ningun parametro se ajusto despues.

## Integridad

- Casos procesados: **72** (esperados 72).
- Poses por caso y diametro: **50**.
- Filas totales: **10800**.
- Poses sin grado: **0** (debe ser 0).

- Control de pose sin perturbar, al diametro del propio corredor (debe dar brecha 0): **49 de 72** casos pasan.

**Casos que NO pasan el control.** Esto si es un fallo de implementacion y sus cifras no deben usarse:

  - `dataset6_CLINIC_0018_data`: brecha 0.31534790992736816 mm con d = D_TS_max = 7.0 mm
  - `dataset6_CLINIC_0008_data`: brecha 0.22653436660766602 mm con d = D_TS_max = 4.8 mm
  - `dataset6_CLINIC_0016_data`: brecha 0.15615570545196533 mm con d = D_TS_max = 3.1 mm
  - `dataset6_CLINIC_0027_data`: brecha 0.05533194541931152 mm con d = D_TS_max = 4.8 mm
  - `dataset6_CLINIC_0035_data`: brecha 0.2832341194152832 mm con d = D_TS_max = 9.0 mm
  - `dataset6_CLINIC_0033_data`: brecha 0.14154577255249023 mm con d = D_TS_max = 9.8 mm
  - `dataset6_CLINIC_0049_data`: brecha 0.06573486328125 mm con d = D_TS_max = 10.9 mm
  - `dataset6_CLINIC_0041_data`: brecha 0.07381010055541992 mm con d = D_TS_max = 7.7 mm
  - `dataset6_CLINIC_0055_data`: brecha 0.06625986099243164 mm con d = D_TS_max = 13.9 mm
  - `dataset6_CLINIC_0052_data`: brecha 0.3938107490539551 mm con d = D_TS_max = 9.5 mm
  - `dataset6_CLINIC_0059_data`: brecha 0.06587362289428711 mm con d = D_TS_max = 11.8 mm
  - `dataset6_CLINIC_0081_data`: brecha 0.20437860488891602 mm con d = D_TS_max = 9.9 mm
  - `dataset6_CLINIC_0067_data`: brecha 0.1814117431640625 mm con d = D_TS_max = 5.0 mm
  - `dataset6_CLINIC_0083_data`: brecha 0.3047909736633301 mm con d = D_TS_max = 9.0 mm
  - `dataset6_CLINIC_0086_data`: brecha 0.3741583824157715 mm con d = D_TS_max = 14.0 mm
  - `dataset6_CLINIC_0090_data`: brecha 0.10674142837524414 mm con d = D_TS_max = 10.2 mm
  - `dataset6_CLINIC_0089_data`: brecha 0.1011509895324707 mm con d = D_TS_max = 9.5 mm
  - `dataset6_CLINIC_0074_data`: brecha 0.14659833908081055 mm con d = D_TS_max = 9.8 mm
  - `dataset6_CLINIC_0092_data`: brecha 0.21370506286621094 mm con d = D_TS_max = 13.7 mm
  - `dataset6_CLINIC_0093_data`: brecha 0.08599328994750977 mm con d = D_TS_max = 8.6 mm
  - `dataset6_CLINIC_0101_data`: brecha 0.06559991836547852 mm con d = D_TS_max = 10.6 mm
  - `dataset6_CLINIC_0102_data`: brecha 0.27983570098876953 mm con d = D_TS_max = 12.4 mm
  - `dataset6_CLINIC_0103_data`: brecha 0.23331952095031738 mm con d = D_TS_max = 7.5 mm

- **Corredores mas estrechos que el calibre del benchmark** (`D_TS_max` < 7.0 mm): **15 de 72** casos. **No es un fallo:** en esos pacientes el eje ideal del corredor ya perfora al calibre de 7.0 mm, asi que el grado 0 es inalcanzable por anatomia y no por el muestreador. Sus poses **si entran** en la distribucion, porque la serie clinica tampoco excluyo a sus pacientes estrechos (#122).
  Brecha del eje ideal a 7.0 mm en esos casos: mediana **1.02 mm**, maxima **2.48 mm**.

## Perturbacion efectivamente aplicada

- desvio del centro (mm): mediana **3.32**, p90 **8.19**, max **14.97**
- inclinacion (grados): mediana **2.96**, p90 **7.21**, max **16.43**

## Distribucion de grados y Wasserstein-1

| d (mm) | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |
|---|---|---|---|---|---|---|---|
| 4.91 | 3600 | 41.8 | 25.1 | 15.1 | 17.9 | 0.542 | 0.183 |
| 7.0 **(SAP)** | 3600 | 27.9 | 26.8 | 17.4 | 27.8 | 0.901 | 0.506 |
| 7.3 | 3600 | 26.0 | 26.9 | 18.7 | 28.5 | 0.947 | 0.552 |

Referencias de `zwingmann2009navigated`: navegado **69 / 15 / 8 / 8** (26 tornillos, 24 pacientes); convencional **40 / 37 / 11.5 / 11.5** (35 tornillos, 32 pacientes). `zwingmann2010percutaneous` no entra (#113).

El W1 esta en **grados**, no en milimetros, y trata los cuatro grados como equiespaciados (convencion declarada). Su maximo posible es 3.0.

## Estados de las poses

- `ok`: **3600**

## Fraccion por zona de densidad (componente 2 de SAP, reportado)

- mediana **0.397**, p25 **0.269**, p75 **0.547** sobre 3600 poses

## Viabilidad de corredor (componente 3 de SAP)

- d = 4.91 mm: **79.2%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.0 mm: **59.7%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.3 mm: **54.2%** de las poses en casos con `D_TS_max >= d + 2`
