# TS cohorte — TotalSegmentator sobre los 179 volumenes y su QC (entrega para el analisis)

Estado al 2026-09-13: **corrida completa, traida a la PC e integridad verificada. Analizada** (ver
seccion `Analisis` al final y `ts_analisis.md`); faltan la revision manual de laminas y las decisiones.
Este archivo es el punto de entrada del siguiente agente. **No decide nada**: las decisiones
son de la autora (#48, #49, #50 en `docs/04-implicancias.md`).

## Que se corrio

| | TS (`ts_cohorte.sbatch`) | QC (`ts_qc_cohorte.sbatch` -> `ts_qc.py`) |
|---|---|---|
| Job | 51315, ag001, `shard:a100_3g.20gb:1` (el mismo `--gres` que el piloto 51300) | 51316, n006 (`big-mem`) |
| Entorno | TS 2.18.0, torch 2.14.0+cu130, `--task total`, `--roi_subset sacrum vertebrae_S1 hip_left hip_right` | mismo entorno conda |
| Inicio / fin | 2026-09-12 23:23 -> 2026-09-13 05:50 (6 h 27 min) | 05:50 -> 06:18 (28 min), `rc=0` |
| Volumen | 179 x {robust3mm, default6mm} = 358 corridas | 179 casos |

## Donde esta (ignorado por git: `experiments/**/outputs/`)

- `outputs/ts_total_qc/`: `ts_qc.csv`, `ts_qc_esferas.csv`, `ts_qc_tornillos.csv`,
  `ts_qc_errores.csv`, `laminas/` (179 `_planos.png` + 18 `_tornillos.png`).
- `outputs/ts_total_procedencia/`: `ts_tiempos.csv`, `repetibilidad_piloto_51315.txt`,
  `entorno_51315.txt`, `pip_freeze_51315.txt`, `pesos_51315.txt`, `sha256_check.txt` y logs
  (`ts_cohorte_51315.log`, `ts_qc_51316.log`, `ts_piloto_51293/51298/51300.log`).
- **Mascaras NO traidas** (~650 MB estimados): siguen en Khipu, `~/metalsynth/data/ts_total/`.
  Solo hacen falta para rehacer E9 (`KHIPU.md`, paso 6).
- Definicion de cada columna: docstring de `ts_qc.py` y funciones de `ts_piloto_qc.py`.

## Integridad verificada (2026-09-13, contra los archivos locales)

| Control | Esperado | Obtenido |
|---|---|---|
| `sha256_check.txt` | 179 OK | 179 OK |
| `ts_tiempos.csv` | 358 `ok`, 4 mascaras | 358 `ok`, 179 casos x 2 modos unicos, todas con 4 mascaras; 45-96 s (media 64.8) |
| Log TS | `fallos=0` | `nuevas ok=358 fallos=0 ya hechas=0` |
| `ts_qc.csv` | 179 x 8 = 1432 filas | 1432; 8 filas por caso |
| `ts_qc_errores.csv` | vacio | solo cabecera |
| Laminas | 179 planos; tornillos = casos de E8 | 179; 18 = 18 casos en `ts_qc_tornillos.csv` |
| QC cohorte vs `ts_piloto_qc*.csv` (2 casos) | igual | esferas y tornillos identicos; en `ts_qc.csv` solo difieren `n_vox` y `solo_este_modo_vox` de `metal_0008` 6 mm (ver repetibilidad) |

## Hechos que el analisis debe conocer ANTES de contar

1. **Repetibilidad no exacta** (registrada en #49, 2026-09-13). Mismo nodo, `--gres`, version,
   clases y recorte que el piloto: 14 de 16 mascaras identicas. `metal_0008` default6mm:
   `sacrum` 16 voxeles distintos (Dice 0.99998) y `hip_left` 8 (0.99999).
2. **Filtrar por paciente.** `ts_qc*.csv` trae los 179 volumenes, incluidos los 11 de
   `experiments/exploration-3d/exclusiones.csv` (retirados, fusionados `0059`/`0071`,
   secundario `0065`). Sin ellos quedan 168 volumenes = 168 pacientes; `0059u0071_union` es el
   de ese paciente. Ojo: `metal_0065` (secundario) es uno de los 18 con tornillo.
3. **`metal_0053`: `vertebrae_S1` vacia con los dos recortes** (`n_vox = 0`; son las 2 filas
   sin geometria). R1 tampoco halla S1 ahi, y `sacrum` y las caderas tocan `z+`.
4. **16 casos sin esferas** = exactamente los 16 con `S1_hallado = no` en `r1_landmarks.csv`
   (12 de dataset6, 4 de dataset7: `0016`, `0022`, `0023`, `0053`). No es un fallo del QC.
5. **`control_marco_ok` vacio en 42 casos** (252 filas): no estan en `e9b_densidad_s1.csv`
   (121 filas), asi que no hay HU de E9b contra el que comparar. En los 121 restantes, 726 de
   726 esferas dan `True`.
6. **Tocan el borde del FOV 20 volumenes** (62 filas `z+`, 34 `z-`). Entre ellos esta
   `metal_0071` (fusionado, fuera de uso); la union `0059u0071` no toca el FOV. Hay que
   cruzarlos con "los 7 de FOV cortado" de #48.
7. **`techo_linea_media_dz_mm` no vacio:** `vertebrae_S1` 322 y `sacrum` 294 de 358 filas. Los
   16 sin S1 en R1 explican 32 por estructura, y `metal_0053` explica 2 mas en `vertebrae_S1`.
   **Las 32 restantes de `sacrum` no tienen explicacion verificada.** Revisar `techo_dz` en
   `ts_piloto_qc.py` antes de usar la columna.

## Analisis pendiente (orden de `docs/ESTADO.md`, PENDIENTE 1)

1. **Repetibilidad y fallos:** hecho arriba. Solo queda interpretarlo dentro de #49.
2. **Laminas `ts_total_qc/laminas/`:** separacion sacro/S1, ala dentro de la mascara, fallos
   bajo metal. Prioridad: `CLINIC_0002` (¿esfera en L5 o en S1?, #50), los 6 `+1` del clinico
   (#50, `r1_estados.csv`), los 18 con tornillo, los 20 que tocan el FOV y `metal_0053`.
3. **`ts_qc.csv`:** `techo_linea_media_dz_mm` de `vertebrae_S1` como segundo detector de nivel
   frente a R1 (#50 opcion b), por estado del clinico; `dice_3v6` y `solo_este_modo_vox` por
   estructura y grupo (con/sin metal) (#49). **`ts_qc_esferas.csv`:** cuantas esferas caen
   fuera de hueso (`frac_fuera_mascaras`), y la tabla de #50 rehecha con
   `frac_bajo150_recuperada_sacro_S1` (#50).
4. **Decisiones de la autora** (el analisis las alimenta, no las toma): adoptar TS (#48);
   recorte 3 mm, 6 mm o ambos (#49); `total` frente a `total_v3` (#49); auditar S1 de
   calibracion o retirar el brazo sin metal (#50).

Reglas: los scripts nuevos van en `experiments/objetivo2/`; las tablas que se vayan a citar se
copian a `experiments/objetivo2/` y se versionan (como E8 y E9b). Todo hallazgo pasa por la
regla 13 de `CLAUDE.md` (`04-implicancias.md`).

## Analisis (2026-09-13) — pasos 2 y 3 hechos en parte; paso 4 sin tocar

Script: `ts_analisis.py`, solo lectura de CSV. Genera `ts_analisis.md` (todas las tablas) y
`ts_nivel_s1.csv` (estado de nivel por caso), versionados. Cuenta 168 pacientes. Implicancias:
#48, #49 y #50 actualizadas, y #51 nueva.

| Pregunta | Resultado |
|---|---|
| ¿TS sirve como segundo detector de nivel? (#50 b) | Si. `dz` de `vertebrae_S1` concuerda con el clinico en 56 de 57 (`+1`: -34 a -32 mm; `ok`: +3.7 a +15.7 mm). Cualquier umbral de (-24.3, +3.7] mm da lo mismo, y el recorte no cambia ningun estado |
| ¿`CLINIC_0002` en L5 o S1? | TS y lamina: la esfera esta en la vertebra craneal a S1 (lectura del agente) |
| Error de nivel de R1 sin auditar | Calibracion 7 de 60; `otro` 11 de 31. `s1_discordante` no los captura todos |
| Discordancias con el clinico | `metal_0012` (`ok`, TS -24 mm; cuenta en 49/30 de `main.tex`) y `metal_0015` (`ok`, FOV cortado, agente "grosero"). Ver #51 |
| Esferas de E9b fuera de hueso (#50) | Las 75 de los 25 casos `R1 arriba`. Con nivel concordante, las alas < 150 HU caen sobre todo fuera de la mascara (sonda anterolateral al cuerpo). "Ala < 150 HU con esfera >= 90% en sacro/S1": con metal 4 de 53 (8%), calibracion 9 de 60 (15%) |
| Recorte (#49) | Dice mediano 0.94-0.97, ~5% de voxeles exclusivos, ~0.01 menos con osteosintesis. **Nuevo:** en 10 casos la caja se desplaza 14-98 mm (3 en el corredor) |
| FOV | 19 pacientes tocan el borde; los 7 de R1 estan todos. S1 cortada en `z+`: `metal_0015`, `metal_0022`, `CLINIC_0010`, `CLINIC_0011` |
| `metal_0053` | Sin S1 en TS y sin S1 en R1; la lamina muestra solo la pelvis baja (S1 fuera del FOV) |
| Tornillos (17 pacientes, 21 componentes) | Metal en mascaras: mediana 98%. Eje fuera: mediana 5-6%, maximo 35% (`metal_0024`, articulacion sacroiliaca con estriacion) |
| 32 filas de `sacrum` sin techo (pendiente) | Sobre 168: 28 filas y 16 casos. 12 casos son R1 un nivel arriba (columna anterior al sacro); quedan 4 casos sin explicar. El techo de `sacrum` **no** se usa |

**Correccion del 2026-09-14:** `metal_0012` era `+1` para el clinico (error de transcripcion) y
`metal_0015` es `?` (dudoso). Con eso, la concordancia TS/clinico es **57 de 57** y R1 queda en 48/29
(#51 CERRADA). Las filas de `metal_0012` y `metal_0015` de la tabla de arriba quedan obsoletas;
`ts_analisis.md` esta regenerado.

**Laminas revisadas (agentes, no la autora; 12 de 197):** `CLINIC_0002`, `0022`, `0043`;
`metal_0010`, `0012`, `0015`, `0017`, `0024` (tornillos), `0026`, `0030`, `0053`, `0058`.
Pendientes de la revision manual: los otros 4 `+1` y los otros 16 casos con tornillo, el resto de
los que tocan el FOV, y los 10 con caja desplazada.

**Paso 4 (decisiones de la autora), con lo que aporta el analisis:**
- **#48, adoptar TS:** a favor, nivel concordante y metal dentro de las mascaras; en contra, recorte
  y fragmentos, que obligan a declarar una limpieza.
- **#49, recorte:** ninguno domina, porque el nivel no cambia y la mascara cambia ~5%. Medir E9 con
  los dos sigue siendo la opcion que no elige a ciegas.
- **#50:** cifra de #48 y brazo sin metal.
- **#51:** cifra 49/30.
- **`total_v3`:** sigue sin evaluar.
