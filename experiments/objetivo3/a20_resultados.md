# A20 — `streak amplitude` de E-A2 en validacion (componentes de `Delta`)

Copia versionada; `outputs/` no esta versionado. Evaluador: `a20_evaluador_ea2.py`. Formula de `Delta`:
`01-decisiones.md` 2026-10-09 (4).

## Brazo fisico de Peters (`a19`, job Khipu 55240, `big-mem`, 2026-10-09)

- **Corrida:** cortes alternos (`k = 2`): 28 de 55 cortes con `G` en `0101` y 19 de 38 en `0102`.
- **Correlacion de calibracion** (simulacion sin metal frente al original): 0.997 en `0101` y 0.987-0.989 en
  `0102`.
- **Sesgo sin metal en tejido blando:** +8 HU en `0101` y +24 HU en `0102`. Es un control, no un criterio, y se
  cancela en `con metal - sin metal`.
- **XCIST:** `gecatsim` 1.6.8 segun `pip`; el atributo `__version__` del paquete dice 0.1.8, que es un dato
  desactualizado del propio paquete.

| caso | Fe_A | Fe_B | \|A-B\| Fe | Ti_A | Ti_B | \|A-B\| Ti | ruido A-B | ROIs |
|---|---|---|---|---|---|---|---|---|
| 0101 | 5363 | 5397 | 34.1 | 2051 | 2051 | 0.4 | 139 | 155 |
| 0102 | 2211 | 2199 | 12.3 | 1277 | 1282 | 5.2 | 193 | 154 |

Todas las cifras en HU.

**`r` = 23.2 HU**: |Fe_A - Fe_B| promediado sobre `0101` y `0102`.

## Difusor (`a15_delta`)

Pendiente: el job esta en curso en Khipu. Con su `s`, `Delta = max(s, r)` sale de `a20_evaluador_ea2.py delta`.
