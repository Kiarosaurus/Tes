# E13 — muestreo de poses y SAP (generado por `e13_muestreo_sap.py`; no elige nada)

> **CORRECCION POSTERIOR (2026-09-22, #122).** La seccion de control de este archivo esta **mal etiquetada** y su texto es falso en dos sentidos. (1) El control se calculo con un cilindro de **7.0 mm**, no con `D_TS_max`, que es la unica identidad garantizada por construccion; por eso "fallan" justo los casos cuyo corredor mide **menos de 7.0 mm**, donde el eje ideal **tiene** que perforar. Es anatomia, no un fallo de la metrica. (2) La frase "sus cifras no se usan" es incorrecta: `resumen()` calcula la distribucion sobre **todas** las poses y no excluye ningun caso; y **excluirlos habria estado mal**, porque la serie clinica de referencia tampoco excluyo a sus pacientes de corredor estrecho. **Las cifras de distribucion y de Wasserstein-1 de este archivo son validas y no cambian.** El codigo quedo corregido para la proxima corrida. Ver #122.

> Distribucion de poses y metrica **preinscritas** en `preinscripcion_muestreador.md` (2026-09-22), antes de calcular este archivo. Ningun parametro se ajusto despues.

## Integridad

- Casos procesados: **49** (esperados 49).
- Poses por caso y diametro: **50**.
- Filas totales: **7350**.
- Poses sin grado: **0** (debe ser 0).

- Control de pose sin perturbar (debe dar brecha 0): **40 de 49** casos pasan.

**Casos que NO pasan el control** (sus cifras no se usan):

  - `dataset6_CLINIC_0018_data`: brecha 0.31534790992736816 mm
  - `dataset6_CLINIC_0016_data`: brecha 2.1061558723449707 mm
  - `dataset6_CLINIC_0022_data`: brecha 1.0172913074493408 mm
  - `dataset6_CLINIC_0027_data`: brecha 1.1553318500518799 mm
  - `dataset6_CLINIC_0042_data`: brecha 0.25374436378479004 mm
  - `dataset6_CLINIC_0044_data`: brecha 0.2462005615234375 mm
  - `dataset6_CLINIC_0047_data`: brecha 1.4121406078338623 mm
  - `dataset6_CLINIC_0060_data`: brecha 0.36478757858276367 mm
  - `dataset6_CLINIC_0096_data`: brecha 0.26698923110961914 mm

## Perturbacion efectivamente aplicada

- desvio del centro (mm): mediana **1.66**, p90 **4.10**, max **7.45**
- inclinacion (grados): mediana **1.47**, p90 **3.66**, max **8.22**

## Distribucion de grados y Wasserstein-1

| d (mm) | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |
|---|---|---|---|---|---|---|---|
| 4.91 | 2450 | 72.7 | 19.7 | 5.9 | 1.8 | 0.182 | 0.577 |
| 7.0 **(SAP)** | 2450 | 54.9 | 30.4 | 9.9 | 4.8 | 0.186 | 0.299 |
| 7.3 | 2450 | 52.0 | 31.6 | 10.9 | 5.5 | 0.199 | 0.246 |

Referencias de `zwingmann2009navigated`: navegado **69 / 15 / 8 / 8** (26 tornillos, 24 pacientes); convencional **40 / 37 / 11.5 / 11.5** (35 tornillos, 32 pacientes). `zwingmann2010percutaneous` no entra (#113).

El W1 esta en **grados**, no en milimetros, y trata los cuatro grados como equiespaciados (convencion declarada). Su maximo posible es 3.0.

## Estados de las poses

- `ok`: **2450**

## Fraccion por zona de densidad (componente 2 de SAP, reportado)

- mediana **0.450**, p25 **0.359**, p75 **0.594** sobre 2450 poses

## Viabilidad de corredor (componente 3 de SAP)

- d = 4.91 mm: **83.7%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.0 mm: **65.3%** de las poses en casos con `D_TS_max >= d + 2`
- d = 7.3 mm: **57.1%** de las poses en casos con `D_TS_max >= d + 2`
