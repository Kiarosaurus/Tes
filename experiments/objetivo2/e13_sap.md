# E13 — muestreo de poses y SAP (generado por `e13_muestreo_sap.py`; no elige nada)

> **CORRECCION POSTERIOR (2026-09-22, #122).** La seccion de control de este archivo esta **mal etiquetada** y su texto es falso en dos sentidos. (1) El control se calculo con un cilindro de **7.0 mm**, no con `D_TS_max`, que es la unica identidad garantizada por construccion; por eso "fallan" justo los casos cuyo corredor mide **menos de 7.0 mm**, donde el eje ideal **tiene** que perforar. Es anatomia, no un fallo de la metrica. (2) La frase "sus cifras no se usan" es incorrecta: `resumen()` calcula la distribucion sobre **todas** las poses y no excluye ningun caso; y **excluirlos habria estado mal**, porque la serie clinica de referencia tampoco excluyo a sus pacientes de corredor estrecho. **Las cifras de distribucion y de Wasserstein-1 de este archivo son validas y no cambian.** El codigo quedo corregido para la proxima corrida. Ver #122.

> Distribucion de poses y metrica **preinscritas** en `preinscripcion_muestreador.md` (2026-09-22), antes de calcular este archivo. Ningun parametro se ajusto despues.

## Integridad

- Casos procesados: **72** (esperados 72).
- Poses por caso y diametro: **50**.
- Filas totales: **10800**.
- Poses sin grado: **0** (debe ser 0).

- Control de pose sin perturbar (debe dar brecha 0): **56 de 72** casos pasan.

**Casos que NO pasan el control** (sus cifras no se usan):

  - `dataset6_CLINIC_0018_data`: brecha 0.31534790992736816 mm
  - `dataset6_CLINIC_0008_data`: brecha 1.3265342712402344 mm
  - `dataset6_CLINIC_0001_data`: brecha 0.35600805282592773 mm
  - `dataset6_CLINIC_0016_data`: brecha 2.1061558723449707 mm
  - `dataset6_CLINIC_0022_data`: brecha 1.0172913074493408 mm
  - `dataset6_CLINIC_0027_data`: brecha 1.1553318500518799 mm
  - `dataset6_CLINIC_0042_data`: brecha 0.25374436378479004 mm
  - `dataset6_CLINIC_0044_data`: brecha 0.2462005615234375 mm
  - `dataset6_CLINIC_0047_data`: brecha 1.4121406078338623 mm
  - `dataset6_CLINIC_0060_data`: brecha 0.36478757858276367 mm
  - `dataset6_CLINIC_0078_data`: brecha 2.086200714111328 mm
  - `dataset6_CLINIC_0067_data`: brecha 1.1814117431640625 mm
  - `dataset6_CLINIC_0091_data`: brecha 2.4783778190612793 mm
  - `dataset6_CLINIC_0097_data`: brecha 0.2798764705657959 mm
  - `dataset6_CLINIC_0072_data`: brecha 0.7898426055908203 mm
  - `dataset6_CLINIC_0096_data`: brecha 0.26698923110961914 mm

## Perturbacion efectivamente aplicada

- desvio del centro (mm): mediana **1.66**, p90 **4.09**, max **7.49**
- inclinacion (grados): mediana **1.48**, p90 **3.61**, max **8.22**

## Distribucion de grados y Wasserstein-1

| d (mm) | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |
|---|---|---|---|---|---|---|---|
| 4.91 | 3600 | 70.3 | 20.4 | 6.9 | 2.3 | 0.138 | 0.533 |
| 7.0 **(SAP)** | 3600 | 51.5 | 31.4 | 11.1 | 6.0 | 0.206 | 0.230 |
| 7.3 | 3600 | 48.6 | 32.5 | 12.3 | 6.7 | 0.247 | 0.174 |

Referencias de `zwingmann2009navigated`: navegado **69 / 15 / 8 / 8** (26 tornillos, 24 pacientes); convencional **40 / 37 / 11.5 / 11.5** (35 tornillos, 32 pacientes). `zwingmann2010percutaneous` no entra (#113).

El W1 esta en **grados**, no en milimetros, y trata los cuatro grados como equiespaciados (convencion declarada). Su maximo posible es 3.0.

## Estados de las poses

- `ok`: **3600**

## Fraccion por zona de densidad (componente 2 de SAP, reportado)

- mediana **0.420**, p25 **0.311**, p75 **0.578** sobre 3600 poses

## Viabilidad de corredor (componente 3 de SAP)

- d = 4.91 mm: **79.2%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.0 mm: **59.7%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.3 mm: **54.2%** de las poses en casos con `D_TS_max >= d + 2`
