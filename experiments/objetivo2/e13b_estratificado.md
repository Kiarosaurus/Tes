# E13b — Wasserstein-1 estratificado por viabilidad del corredor

> **Analisis POST HOC declarado.** No estaba en `preinscripcion_muestreador.md`. Se decidio despues de ver la corrida 52175 y el hallazgo de #122. La cifra principal del Objetivo 2 sigue siendo la de `e13_sap.md`, calculada sobre toda la cohorte.

Calibre: **7.0 mm**, el del benchmark (D-O2.4). Un caso se considera de corredor viable cuando su `D_TS_max` alcanza ese calibre; por debajo, el eje ideal del corredor ya perfora y el grado 0 es inalcanzable por anatomia.

### Cohorte primaria (72 casos)

- Casos: **72**; con `D_TS_max` $\geq$ 7.0 mm: **57**; mas estrechos: **15**.

| estrato | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |
|---|---|---|---|---|---|---|---|
| **todos** (preinscrito) | 3600 | 51.5 | 31.4 | 11.1 | 6.0 | 0.206 | 0.230 |
| corredor $\geq$ 7.0 mm | 2850 | 64.2 | 27.5 | 6.1 | 2.2 | 0.183 | 0.482 |
| corredor $<$ 7.0 mm | 750 | 3.3 | 46.4 | 30.0 | 20.3 | 1.122 | 0.727 |

### Sensibilidad, grupo 3 (49 casos)

- Casos: **49**; con `D_TS_max` $\geq$ 7.0 mm: **41**; mas estrechos: **8**.

| estrato | n poses | % g0 | % g1 | % g2 | % g3 | W1 vs navegado | W1 vs convencional |
|---|---|---|---|---|---|---|---|
| **todos** (preinscrito) | 2450 | 54.9 | 30.4 | 9.9 | 4.8 | 0.186 | 0.299 |
| corredor $\geq$ 7.0 mm | 2050 | 64.6 | 26.6 | 6.6 | 2.1 | 0.175 | 0.483 |
| corredor $<$ 7.0 mm | 400 | 5.2 | 49.5 | 26.5 | 18.8 | 1.037 | 0.643 |

## Lectura

La cifra agregada es una **mezcla de dos poblaciones distintas**. En los corredores que admiten el calibre del benchmark, la distribucion del muestreador queda cerca del brazo navegado; en los corredores estrechos, practicamente ninguna pose alcanza el grado 0, y no porque el muestreador las desvie, sino porque el eje optimo de esos pacientes ya perfora. Por eso el W1 agregado frente al brazo navegado **no debe leerse como una medida limpia del muestreador**: parte de esa distancia es del emparejamiento entre la cohorte receptora y la cohorte clinica de referencia.

La estratificacion **no se usa para elegir cohorte**. Los dos estratos se reportan juntos, y la cifra que se defiende es la preinscrita sobre la cohorte completa.
