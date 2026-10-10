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

## Difusor (`a15_delta`, `mejor_37k`, 5 semillas, `--incluir-banda`, shard RTX A6000, 2026-10-09)

| caso | s0 | s1 | s2 | s3 | s4 | rango | ROIs | fraccion en el suelo de -1000 |
|---|---|---|---|---|---|---|---|---|
| 0101 | 916 | 892 | 815 | 680 | 747 | 236.2 | 155 | 0.000 |
| 0102 | 1229 | 1273 | 1232 | 1132 | 1143 | 141.2 | 154 | 0.000 |

Todas las cifras en HU.

**`s` = 188.7 HU**: el rango entre semillas promediado sobre los dos pacientes.

## `Delta` (formula de 01-decisiones 2026-10-09 (4))

**`Delta = max(s, r) = max(188.7, 23.2) = 188.7 HU`.** Lo fija el difusor: su variabilidad entre semillas es unas 8
veces el test-retest de Peters. Salida en `outputs/a20/a20_delta.json`.

## Lectura en validacion (descriptiva, NO es el contraste primario, que se hace en test)

Mediana entre semillas del difusor frente a Peters, por paciente:

| caso | difusor | Peters Fe | diferencia Fe | Peters Ti | diferencia Ti |
|---|---|---|---|---|---|
| 0101 | 815 | 5380 | ~4570 | 2051 | ~1240 |
| 0102 | 1229 | 2205 | ~980 | 1279 | ~50 |

En los dos pacientes, la diferencia frente a Fe (el material preinscrito) es muchas veces `Delta`. Ver #161.
