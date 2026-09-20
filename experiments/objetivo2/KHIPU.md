# Khipu: manual operativo de MetalSynth-Pelvis

Todo lo verificado al correr TotalSegmentator (TS) en el clúster, para no repetir errores. Las
decisiones de método no se toman aquí: están en `docs/04-implicancias.md` (#29, #48, #49, #50).
El estado del proyecto está en `docs/ESTADO.md`.

## Acceso y estructura en el clúster

- `ssh kiara.balcazar@khipu.utec.edu.pe`. Tienen internet el nodo de acceso y `ds001`; **los nodos
  GPU no**, así que pesos y paquetes se instalan desde el nodo de acceso.
- Carpetas en `~/metalsynth/`:

| Ruta | Contenido |
|---|---|
| `data/extracted/CTPelvic1K_dataset{6,7}_data/` | los 178 CT originales |
| `data/derivados/` | `dataset7_CLINIC_metal_0059u0071_union.nii.gz` |
| `data/ts_input/` | 179 enlaces simbólicos planos (178 + unión) |
| `data/sha256_local.txt`, `data/sha256_check.txt` | SHA256 de la PC y verificación en Khipu: **179/179 OK** (2026-09-12) |
| `totalseg_home/` | pesos de TS (`total` + `total_fast`) |
| `data/ts_piloto/` | piloto, job 51300 |
| `data/ts_total/` | cohorte (`ts_cohorte.sbatch`) |
| `data/ts_total_qc/` | QC de la cohorte (`ts_qc_cohorte.sbatch`) |
| `qc/` | copia de los scripts y CSV que usa el QC |
| `*.sbatch`, `*_<jobid>.log` | scripts de job y sus logs |

## Entorno (creado el 2026-09-12)

```bash
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda create -y -n totalseg python=3.11
conda activate totalseg
pip install TotalSegmentator==2.18.0          # torch 2.14.0+cu130 quedó instalado
export TOTALSEG_HOME_DIR=$HOME/metalsynth/totalseg_home
totalseg_download_weights -t total            # modelos 1.5 mm + recorte 6 mm
totalseg_download_weights -t total_fast       # trae el recorte 3 mm que usa --robust_crop
```

Si al QC le falta alguna dependencia, instálala en el nodo de acceso con el entorno activo:
`pip install pandas scipy matplotlib`.

## Colas y límites (verificado con `sinfo` y `sacctmgr`, 2026-09-12)

| Partición | Nodos / GPU | QoS de partición | Límite efectivo con `--qos=a-tesis` |
|---|---|---|---|
| `debug-gpu` | g001 (`tesla`, `shard:16`) | `p-debug-gpu` **MaxWall 1 h** | 1 h |
| `gpu` | g001 (tesla); g002 y ds001 (`rtxa6000`, `shard:48`); ag001 (A100 + MIG: `a100_3g.20gb`, `a100_2g.10gb`, `a100_1g.5gb`) | `p-gpu` sin MaxWall | 24 h |
| `big-mem` | n006 (CPU) | `p-big-mem` | 24 h |

`a-tesis` pone topes **por usuario**, sumando todos sus jobs: 32 CPU, 98G, 40 shards y 3 jobs.
Cuenta: `--account=tesis`.

**Actualizacion 2026-09-14 (`sinfo`, `scontrol show node`, `sacctmgr`):**
- ag001 declara ademas una **A100 entera** (`gpu:a100:1`, `shard:a100:16`) junto a las MIG (`3g.20gb`,
  `2g.10gb`, `1g.5gb` x2); `gres/gpu=5`, `gres/shard=80`.
- g001 `tesla` = 1 GPU, `shard:16`; modelo y memoria sin verificar (`nvidia-smi` dentro de un job).
- `a-tesis` muestra `MaxTRESPU=cpu=32,gres/shard=40,mem=98G`, `MaxJobsPU=3`, `MaxWall=1-00:00:00`: **no pone
  tope a `gres/gpu`**. Pedir `--gres=gpu:rtxa6000:1` no descuenta shards; confirmar con `sbatch --test-only`
  antes del primer uso.
- Foto de ocupacion ese dia: g002 (A6000) y g001 (tesla) `IDLE`; ds001 con su A6000 tomada por 24 h;
  la A100 entera de ag001 tomada por 2 dias y un shard de ag001 por 4 h.

## Lecciones (cada una ya costó un job)

1. **`--time` mayor que el MaxWall de la partición** deja el job en `PD` con
   `QOSMaxWallDurationPerJobLimit` para siempre. **`sbatch --test-only` no lo detecta.** Si el job
   aún no arrancó, se arregla con `scontrol update JobId=<id> TimeLimit=...`.
2. **`PD (Resources)`**: todo el nodo está ocupado. Para ver quién y hasta cuándo: `squeue -j <id> --start`,
   `squeue -p gpu -o "%.8i %.10u %.8N %.10M %.10l %b"` y `scontrol show node <nodo> | grep AllocTRES`.
   El 2026-09-12 las tres GPU enteras estaban tomadas por días; **la MIG `a100_3g.20gb` de ag001
   estaba libre**. No pidas `shard:1` sin tipo en `gpu`: puede tocarte una MIG de 5 GB.
3. **`set -o pipefail` + `cmd | head`**: `head` cierra la tubería, `pip` muere por SIGPIPE
   (`ERROR: Pipe to stdout was broken`, exit 120) y el job falla en 3 s. Filtra con `grep`.
4. **Número de job:** captúralo con `J=$(sbatch --parsable x.sbatch)`. Buscarlo después con
   `squeue` falla si el job ya terminó.
5. **CRLF:** un `.sbatch` subido desde Windows puede traer `\r`. Tras cada `scp`, corre
   `sed -i 's/\r$//' ~/metalsynth/*.sbatch`.
6. En una MIG, `nvidia-smi` muestra la tarjeta física (A100 40 GB), no la porción asignada.
7. El log de `tail -f` puede quedar vacío un rato: `module` y `conda` tardan antes del primer `echo`.
8. **Límite de envíos (2026-09-17):** con 5 jobs propios en cola o corriendo (P1: 51667-51671), el sexto `sbatch`
   fue rechazado con `QOSMaxSubmitJobPerUserLimit`, y `$E` quedó vacío sin error aparente. Aparte de `MaxJobsPU=3`
   (corriendo), hay un tope de jobs **enviados**. Un job con `--dependency` también ocupa cupo mientras espera.

## Correr la cohorte completa

**Paso 1: subir scripts y referencias** (PowerShell local):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo2
ssh kiara.balcazar@khipu.utec.edu.pe "mkdir -p ~/metalsynth/qc"
scp ts_cohorte.sbatch ts_qc_cohorte.sbatch kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp ts_qc.py ts_piloto_qc.py r1_landmarks.py e9b_densidad_s1.py r1_landmarks.csv e9b_densidad_s1.csv e8_componentes.csv kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

**Paso 2: comprobar y lanzar** (Khipu):

```bash
cd ~/metalsynth
sed -i 's/\r$//' *.sbatch
module load miniconda/3.0                               # en cada terminal nueva: conda no esta en el PATH
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg && python -c "import pandas, scipy, matplotlib; print('ok')"
ls ~/metalsynth/data/ts_input/*.nii.gz | wc -l      # 179
sbatch --test-only ts_cohorte.sbatch
J=$(sbatch --parsable ts_cohorte.sbatch); echo "TS=$J"
Q=$(sbatch --parsable --dependency=afterany:$J ts_qc_cohorte.sbatch); echo "QC=$Q"
```

Si `--test-only` da una hora de inicio lejana, mira la lección 2 y cambia `--gres`/`--partition` en
`ts_cohorte.sbatch`. Si terminas usando otro tipo de GPU, anótalo: la comparación con el piloto
mezclaría GPU y repetibilidad.

**Paso 3: seguimiento:**

```bash
squeue -u $USER -o "%.8i %.12j %.9P %.2t %.10M %.8N %R"
tail -3 ~/metalsynth/data/ts_total/_procedencia/ts_tiempos.csv
grep -c ",ok," ~/metalsynth/data/ts_total/_procedencia/ts_tiempos.csv     # meta: 358
grep -v ",ok," ~/metalsynth/data/ts_total/_procedencia/ts_tiempos.csv     # fallos (más la cabecera)
tail -f ts_cohorte_$J.log
```

**Paso 4: si se corta** (por tiempo o por fallos): relanza el mismo `sbatch`; salta lo que ya tiene
`.ok`. El QC también se relanza y continúa donde quedó.

**Paso 5: cierre:**

```bash
sacct -j $J,$Q --format=JobID,JobName,State,ExitCode,Elapsed,MaxRSS
find ~/metalsynth/data/ts_total -name .ok | wc -l                          # 358
cat ~/metalsynth/data/ts_total/_procedencia/repetibilidad_piloto_*.txt     # ¿0 vóxeles distintos?
wc -l ~/metalsynth/data/ts_total_qc/ts_qc*.csv                             # ts_qc.csv: 1 + 179*8 = 1433
cat ~/metalsynth/data/ts_total_qc/ts_qc_errores.csv
```

**Paso 6: traer a la PC** (PowerShell). Las tablas y láminas pesan poco; las máscaras, unos 650 MB
estimados, así que tráelas solo cuando se vayan a usar:

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/ts_total_qc experiments\objetivo2\outputs\
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/ts_total/_procedencia experiments\objetivo2\outputs\ts_total_procedencia
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/ts_*_*.log" experiments\objetivo2\outputs\ts_total_procedencia\
# opcional, pesado:
# scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/ts_total data\derivados\
```

**Corrida real (2026-09-13):** TS 51315, 358/358 ok, 45-96 s por corrida, 6 h 27 min en total.
QC 51316, 28 min, 0 errores. Resultados y controles en `ts_cohorte.md`.

## E10: componentes conexas de las máscaras (regla de limpieza, decisión del 2026-09-14)

Solo CPU (`big-mem`) y sin GPU. Lee las 358 máscaras de `data/ts_total/`, que no hace falta traer
a la PC. Tiempo sin medir.

**Paso 1: subir** (PowerShell local):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo2
scp ts_componentes.sbatch kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp ts_componentes.py kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

**Paso 2: comprobar y lanzar** (Khipu):

```bash
cd ~/metalsynth
sed -i 's/\r$//' *.sbatch
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg && python -c "import nibabel, numpy, scipy; print('ok')"
find data/ts_total -name .ok | wc -l                  # 358
sbatch --test-only ts_componentes.sbatch
E=$(sbatch --parsable ts_componentes.sbatch); echo "E10=$E"
```

**Paso 3: seguimiento y cierre:**

```bash
squeue -u $USER -o "%.8i %.14j %.9P %.2t %.10M %.8N %R"
tail -f ts_componentes_$E.log                          # una linea "ok" por caso
wc -l data/ts_componentes/ts_componentes_resumen.csv   # meta: 1 + 179*2*5 = 1791
cat data/ts_componentes/ts_componentes_errores.csv     # solo cabecera
sacct -j $E --format=JobID,JobName,State,ExitCode,Elapsed,MaxRSS
```

Si se corta, relanza el mismo `sbatch`: salta los casos ya escritos.

**Paso 4: traer** (PowerShell):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/ts_componentes experiments\objetivo2\outputs\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/ts_componentes_*.log" experiments\objetivo2\outputs\ts_componentes\
```

## Noche automatica: E10 + E9-TS + resumen, con una sola orden (2026-09-14)

`noche_e9ts.sh` comprueba los archivos y lanza tres jobs: E10 y E9-TS en paralelo, y el resumen cuando
terminan los dos (`afterany`). Sumando los tres, 21 CPU y 96G, dentro de `a-tesis` (32 CPU, 98G,
3 jobs). **No elige nada:** E9-TS calcula recorte (6 y 3 mm) x limpieza (F = 0, 0.001, 0.01, 0.05)
x politica de metal (`hueso`; y, si hay metal en el recorte, `ocupado_2500` y `ocupado_semimax`, #52 c)
para los 152 casos con S1 en R1, y la fraccion y #52 se deciden despues filtrando filas.
Si E10 se lanzo antes por separado, no uses este script: lanza solo `e9ts_corredor.sbatch` y el
resumen a mano (paso 4).

Prueba local (2026-09-14, `metal_0008` del piloto, 1 proceso): 35 s por caso con las 8 variantes. En
Khipu no esta medido; con 16 procesos se espera bastante menos de una hora.

**Paso 1: subir** (PowerShell local):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo2
scp ts_componentes.sbatch e9ts_corredor.sbatch noche_e9ts.sh kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp ts_componentes.py e9ts_corredor.py e9_corredor.py e9ts_resumen.py r1_landmarks.py ts_piloto_qc.py e9b_densidad_s1.py r1_landmarks.csv r1_estados.csv ts_nivel_s1.csv kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

`r1_estados.csv` y `ts_nivel_s1.csv` **deben** ser los del 2026-09-14 (transcripcion corregida).

**Paso 2: lanzar** (Khipu):

```bash
cd ~/metalsynth
sed -i 's/\r$//' noche_e9ts.sh
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg && python -c "import nibabel, numpy, pandas, scipy, matplotlib; print('ok')"
bash noche_e9ts.sh            # imprime E10=... E9TS=... RESUMEN=... y los guarda en noche_e9ts_jobs.txt
```

**Paso 3: por la manana:**

```bash
cd ~/metalsynth
cat noche_e9ts_jobs.txt
sacct -j <E10>,<E9TS>,<RESUMEN> --format=JobID,JobName,State,ExitCode,Elapsed,MaxRSS
wc -l data/e9ts/e9ts_corredor.csv                  # 8 filas por caso sin metal en el recorte, 24 con metal
grep -c "," data/e9ts/e9ts_corredor.csv            # el recuento exacto por caso lo da e9ts_resumen.md, seccion 1
wc -l data/ts_componentes/ts_componentes_resumen.csv   # meta: 1791
cat data/e9ts/e9ts_resumen.md
```

**Paso 4: si algo se corto:** relanza el `sbatch` que fallo (los dos son reanudables) y despues el
resumen:

```bash
cd ~/metalsynth/qc && python e9ts_resumen.py --e9-dir ~/metalsynth/data/e9ts --e10-dir ~/metalsynth/data/ts_componentes
```

**Paso 5: traer** (PowerShell):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/e9ts experiments\objetivo2\outputs\
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/ts_componentes experiments\objetivo2\outputs\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/*e9ts*_*.log" "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/ts_componentes_*.log" experiments\objetivo2\outputs\e9ts\
```

`experiments/**/outputs/` está ignorado por git. Si alguna tabla se va a citar, se copia aparte a
`experiments/objetivo2/` y se versiona, igual que las de E8 y E9b.

**Corrida real (2026-09-14):** E9-TS 51505 completo (152 casos, 0 errores). E10 51504 murio por SIGKILL
externo (`ExitCode 0:9`, 6:47, MaxRSS 908 MB) mientras E9-TS corria en el mismo n006; relanzado solo como
51522: 179 casos, 0 errores, 16 min. Resumen 51523. Antes de relanzar hubo que reponer a mano la cabecera
del CSV de errores (el proceso muerto no la vuelca).

## E9-TS con 3 mm: laminas, repetibilidad y resumen (preferencia de la autora, 2026-09-14)

**Las cifras con `robust3mm` ya existen** en `data/e9ts/e9ts_corredor.csv` (51505 calculo los dos recortes para
los 152 casos), igual que E10 y E10b. Pasar el principal a 3 mm no exige recalcular nada. Esta corrida hace lo
que falta: laminas de QC con 3 mm (51505 solo las hizo con 6 mm), resumen con la seccion 5 en 3 mm y un
**control de repetibilidad** (el CSV nuevo debe ser identico al de 51505; si difiere, el log dice `DIFIERE`).
51505 tardo 6 min 39 s con 16 CPU. No lances esto a la vez que E10b en n006 (el primer E10 murio con E9-TS al lado).

**Paso 1: subir** (PowerShell local):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo2
scp e9ts_3mm.sbatch kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp e9ts_corredor.py e9ts_resumen.py e9ts_repetibilidad.py kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

**Paso 2: comprobar y lanzar** (Khipu):

```bash
cd ~/metalsynth
sed -i 's/\r$//' e9ts_3mm.sbatch
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg
cd qc && python e9ts_corredor.py --help | grep -A1 modo-laminas && cd ..   # debe listar la opcion nueva
ls qc/e9_corredor.py qc/r1_landmarks.py qc/ts_piloto_qc.py qc/e9b_densidad_s1.py qc/r1_landmarks.csv qc/r1_estados.csv qc/ts_nivel_s1.csv
ls -l data/e9ts/e9ts_corredor.csv                        # la corrida 51505, contra la que se compara
squeue -u $USER -o "%.8i %.14j %.9P %.2t %.10M %.8N %R"   # nada corriendo en n006
sbatch --test-only e9ts_3mm.sbatch
T=$(sbatch --parsable e9ts_3mm.sbatch); echo "E9TS_3mm=$T" | tee -a noche_e9ts_jobs.txt
```

**Paso 3: seguimiento y cierre:**

```bash
tail -f e9ts_3mm_$T.log                                  # Ctrl+C para salir
sacct -j $T --format=JobID,State,ExitCode,Elapsed,MaxRSS
grep -A12 "== REPETIBILIDAD" e9ts_3mm_$T.log             # debe decir IDENTICO
ls data/e9ts_3mm/laminas | wc -l                         # 152
grep -A6 "^## 5" data/e9ts_3mm/e9ts_resumen.md
```

**Paso 4: traer** (PowerShell):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/e9ts_3mm experiments\objetivo2\outputs\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/e9ts_3mm_*.log" experiments\objetivo2\outputs\e9ts_3mm\
```

**Corrida real (2026-09-14):** job 51529, n006, 16 CPU, 6 min 41 s (18:03:34-18:10:15), rc=0. 152 casos, 152 laminas
con 3 mm. **Repetibilidad frente a 51505: IDENTICO, 2352 filas x 43 columnas, tolerancia 0.** Resumen con la seccion 5
en `robust3mm`. Traido a `experiments/objetivo2/outputs/e9ts_3mm/`.

## E10b: cajas tras la limpieza (verifica la decision 2026-09-14 (3))

Solo CPU (`big-mem`). Recalcula las cajas de las 358 mascaras con F = 0, 0.001, 0.01 y 0.05 y la
diferencia de caja entre recortes. **Control:** con F = 0 debe reproducir `dif_caja_3v6_max_mm` de
`ts_qc.csv`; si no, el resto no vale. Si no encuentra filas en comun imprime `CONTROL NO EJECUTADO`.
Prueba local (2026-09-14, piloto `CLINIC_0002` + `metal_0008`): 10.8 s los 2 casos; control 8 de 8 contra
`ts_piloto_qc.csv`. En Khipu se espera del orden de E10 (16 min).

**Paso 1: subir** (PowerShell local):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo2
scp ts_cajas_limpias.sbatch kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp ts_cajas_limpias.py kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

**Paso 2: comprobar y lanzar** (Khipu):

```bash
cd ~/metalsynth
sed -i 's/\r$//' ts_cajas_limpias.sbatch
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg && python -c "import nibabel, numpy, scipy, pandas; print('ok')"
find data/ts_total -name .ok | wc -l                   # 358
ls -l data/ts_total_qc/ts_qc.csv                       # debe existir
squeue -u $USER -o "%.8i %.14j %.9P %.2t %.10M %.8N %R"   # que no quede nada corriendo en n006
sbatch --test-only ts_cajas_limpias.sbatch
B=$(sbatch --parsable ts_cajas_limpias.sbatch); echo "E10b=$B" | tee -a noche_e9ts_jobs.txt
```

**Paso 3: seguimiento y cierre:**

```bash
tail -f ts_cajas_limpias_$B.log                        # una linea "ok" por caso; Ctrl+C para salir
sacct -j $B --format=JobID,State,ExitCode,Elapsed,MaxRSS
wc -l data/ts_cajas_limpias/ts_cajas_limpias.csv       # meta: 1 + 179*4*4 = 2865
cat data/ts_cajas_limpias/ts_cajas_limpias_errores.csv # solo cabecera
tail -40 ts_cajas_limpias_$B.log                       # CONTROL y desplazamientos > 10 mm por F
```

Si se corta, relanza el mismo `sbatch`: salta los casos ya escritos y repite el control al final.

**Paso 4: traer** (PowerShell):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/ts_cajas_limpias experiments\objetivo2\outputs\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/ts_cajas_limpias_*.log" experiments\objetivo2\outputs\ts_cajas_limpias\
```

**Corrida real (2026-09-14):** job 51527, n006, 8 min, rc = 0; control 715 de 716 (la S1 vacia de `metal_0053`).
Lectura en `docs/04-implicancias.md` (#49, E10b LEIDO).

## E6b: VAE de SD 1.5 sobre los 178 CT (#36, #39; orden de la autora, 2026-09-15)

GPU (RTX A6000, particion `gpu`). Mide `HU -> ventanas -> VAE -> HU` con el VAE de Stable Diffusion 1.5
preentrenado y **sin reentrenar**, para `pub`, `LW20000` y `pub+asinh` (3 canales). `pub+MTW` no entra (4 canales).
Diseno y controles en el docstring de `experiments/objetivo1/e6b_vae_sd15.py`.

**Version del 2026-09-15 (RMSE):** el script reporta ahora MAE **y** RMSE sobre el mismo vector de errores
(decision 2026-09-15 (2)). La columna de MAE mantiene su nombre sin sufijo, asi que **el control contra E6c y
los comandos de abajo no cambian**; lo que cambia es que el CSV pasa de 32 a **56 columnas** y el `.md` trae
tablas de las dos metricas. La corrida de la cohorte hay que **rehacerla entera** (~8.8 h): el CSV anterior no
tiene las columnas `rmse` y el script no las puede reconstruir sin volver a pasar los volumenes por el VAE.
Con `--solo-resumen` sobre un CSV viejo el informe sale solo con MAE y lo avisa en una linea.

**Prueba local (2026-09-15, sin modelo: la PC no tiene `diffusers` ni GPU):**
- `--vae identidad` sobre `CLINIC_0001` y `metal_0000`: control **12 de 12** frente a `e6c_techo_lw.csv`.
- Con un valor de E6c alterado en 0.5 HU: **11 de 12**, y senala el valor cambiado. El control puede fallar.
- `--vae eco` (tuberia de torch sin modelo): **12 de 12** frente a identidad.
- Relleno de lados no multiplos de 8: el encoder recibe 512 y la salida vuelve a 510 x 507.
- **El VAE real no se probo en local.** Su primer uso es la prueba corta del paso 3.

**Paso 1: subir** (PowerShell local):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo1
ssh kiara.balcazar@khipu.utec.edu.pe "mkdir -p ~/metalsynth/qc ~/metalsynth/modelos ~/metalsynth/data/e6b"
scp e6b_vae_sd15.sbatch kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp e6b_vae_sd15.py e6c_techo_lw.py e6c_techo_lw.csv kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

**Paso 2: entorno y pesos** (Khipu, **nodo de acceso**, que tiene internet; una sola vez):

```bash
cd ~/metalsynth
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda create -y -n e6b --clone totalseg          # no se toca el entorno de TS
conda activate e6b
pip install diffusers
python -c "import torch, diffusers; print('torch', torch.__version__, 'diffusers', diffusers.__version__)"
python -c "import os; from huggingface_hub import snapshot_download; print(snapshot_download('stable-diffusion-v1-5/stable-diffusion-v1-5', allow_patterns=['vae/config.json', 'vae/diffusion_pytorch_model.safetensors'], local_dir=os.path.expanduser('~/metalsynth/modelos/sd15')))"
ls -l modelos/sd15/vae                          # config.json y diffusion_pytorch_model.safetensors
HF_HUB_OFFLINE=1 python -c "from diffusers import AutoencoderKL; v = AutoencoderKL.from_pretrained('$HOME/metalsynth/modelos/sd15', subfolder='vae'); print('parametros', sum(p.numel() for p in v.parameters()))"
```

**Hecho (2026-09-15):** el VAE carga sin internet con **83 653 863 parametros**. El aviso
`Cannot initialize model with low cpu memory usage because accelerate was not found` no cambia los pesos ni
los resultados: solo carga el modelo con mas RAM, y en un job de 48G sobra. `accelerate` no se instalo.

El repositorio `stable-diffusion-v1-5/stable-diffusion-v1-5` es publico y no restringido (API de Hugging Face,
consultada el 2026-09-14), con licencia `creativeml-openrail-m`.

**Paso 3: comprobar y prueba corta de 1 caso** (Khipu):

```bash
cd ~/metalsynth
sed -i 's/\r$//' e6b_vae_sd15.sbatch
find data/extracted -name '*_data.nii*' | wc -l          # 178
squeue -u $USER -o "%.8i %.14j %.9P %.2t %.10M %.8N %R"
sbatch --test-only e6b_vae_sd15.sbatch
P=$(sbatch --parsable --time=02:00:00 e6b_vae_sd15.sbatch --casos dataset7_CLINIC_metal_0000_data --out $HOME/metalsynth/data/e6b_prueba); echo "E6b_prueba=$P" | tee -a e6b_jobs.txt
tail -f e6b_vae_$P.log                                    # Ctrl+C para salir
```

Si `--test-only` rechaza `--gres=gpu:rtxa6000:1` o da un inicio lejano, no cambies nada a ciegas: copia el
mensaje (lecciones 1 y 2). En el log de la prueba, lee:
- `nvidia-smi` y la linea de `torch`: que diga RTX A6000 y `cuda True`;
- `...metal_0000_data: ok N s`: **segundos por volumen**. Con N x 178 por encima de ~20 h, lanza la cohorte con
  `--lote 8` o en dos tandas (el script es reanudable);
- `CONTROL identidad frente a E6c float: 6 de 6`. Si no es 6 de 6, **no lances la cohorte**;
- `pub hueso ... vae oraculo X regla Y`: primera cifra real del VAE.

**Prueba corta hecha (2026-09-15):** job 51539, nodo **ds001** (RTX A6000, 49 140 MiB), torch 2.14.0+cu130, diffusers
0.40.0, rc = 0. `metal_0000` (350 cortes): 182.8 s; control **6 de 6**. Con 60 595 cortes axiales en los 178 volumenes
(mediana 350, rango 187-388), la cohorte se estima en **~8.8 h** con `--lote 4`, sin cambiar nada. `--gres=gpu:rtxa6000:1`
funciona y puede caer en g002 o en ds001 (las dos son RTX A6000).

### Relanzar la cohorte con la version de RMSE (2026-09-15)

**El paso 0 no es opcional.** El script es **reanudable**: lee los `Caso` ya escritos en
`data/e6b/e6b_vae_sd15.csv` y los salta. Si se relanza con el CSV viejo en su sitio, **salta los 178
volumenes, no mide nada y rehace el informe solo con MAE**, con rc = 0 y sin ningun error visible. Hay que
apartar la salida vieja antes de lanzar. No se borra: se mueve.

El entorno y los pesos (paso 2) ya estan hechos y no se repiten. El `.sbatch` y los archivos de E6c
**no cambiaron**: solo se vuelve a subir `e6b_vae_sd15.py`.

```powershell
# Local (PowerShell): subir solo el script nuevo
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo1
scp e6b_vae_sd15.py kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

```bash
# Khipu: comprobar que llego la version nueva y APARTAR la salida vieja
cd ~/metalsynth
grep -c SUF_RMSE qc/e6b_vae_sd15.py            # meta: > 0 (si da 0, no se subio la version nueva)
mv data/e6b data/e6b_mae_20260915              # se guarda, no se borra
mkdir -p data/e6b
```

Prueba corta antes de las 8.8 h (recomendada; `--out` nuevo para no chocar con `e6b_prueba` viejo):

```bash
P=$(sbatch --parsable --time=02:00:00 e6b_vae_sd15.sbatch --casos dataset7_CLINIC_metal_0000_data --out $HOME/metalsynth/data/e6b_prueba_rmse); echo "E6b_prueba_rmse=$P" | tee -a e6b_jobs.txt
squeue -j $P -o "%.8i %.2t %.10M %.8N %R"       # PD = en cola (mira la ultima columna); R = corriendo
until [ -f e6b_vae_$P.log ]; do sleep 20; done  # SLURM crea el log al ARRANCAR, no al encolar
tail -f e6b_vae_$P.log
```

**`tail: cannot open 'e6b_vae_<id>.log'` no es un fallo.** SLURM escribe el log (`--output=%x_%j.log`, en el
directorio desde el que se lanzo) **cuando el job arranca**, no cuando se encola. Si el `tail -f` se lanza con el
job todavia en `PD`, el archivo no existe. Se comprueba con `squeue -j $P`: si aparece con estado `PD`, solo hay
que esperar, y la ultima columna dice por que (`Resources`, `Priority`, limite de QOS...). Si **no** aparece en
`squeue` y tampoco hay log, el job ya termino o murio al arrancar: entonces `sacct -j $P
--format=JobID,State,ExitCode,Elapsed,Start,NodeList` lo dice.

En el log de la prueba, lee: `CONTROL identidad frente a E6c float: 6 de 6` y que la linea del volumen
termine en `| RMSE regla <cifra>`. Si no aparece el tramo de RMSE, esta corriendo el script viejo.

**Paso 4: cohorte completa** (Khipu):

```bash
cd ~/metalsynth
B=$(sbatch --parsable e6b_vae_sd15.sbatch); echo "E6b=$B" | tee -a e6b_jobs.txt
B=$(grep '^E6b=' e6b_jobs.txt | tail -1 | cut -d= -f2); echo $B     # recupera el id si reconectaste
tail -f e6b_vae_$B.log                                     # una linea "ok" por volumen
sacct -j $B --format=JobID,State,ExitCode,Elapsed,MaxRSS
wc -l data/e6b/e6b_vae_sd15.csv                            # meta: 179 (178 + cabecera)
head -1 data/e6b/e6b_vae_sd15.csv | tr ',' '
' | wc -l    # meta: 56 columnas (version con RMSE)
cat data/e6b/e6b_vae_sd15_errores.csv                      # solo cabecera
tail -30 e6b_vae_$B.log                                    # CONTROL (N de N) y ruta del .md
```

Si se corta (tiempo, nodo), relanza el mismo `sbatch`: salta los volumenes ya escritos y rehace control e informe.

**Paso 5: traer** (PowerShell):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/e6b experiments\objetivo1\outputs\
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/e6b_prueba experiments\objetivo1\outputs\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/e6b_vae_*.log" experiments\objetivo1\outputs\e6b\
```

**Al traer la corrida de RMSE (2026-09-15):** apartar antes la salida MAE que ya esta en la PC, para no
pisarla y poder comparar las dos. Las cifras de MAE tienen que salir **identicas**; si cambia alguna, algo
se movio y hay que pararse a mirar.

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo1\outputs
mkdir e6b_mae_20260915
move e6b_vae_sd15*.csv e6b_mae_20260915\
move e6b_vae_sd15.md  e6b_mae_20260915\
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/e6b experiments\objetivo1\outputs\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/e6b_vae_*.log" experiments\objetivo1\outputs\e6b\
```

Comprobaciones en la PC, antes de analizar nada:

```powershell
python -c "import csv; r=list(csv.DictReader(open(r'experiments\objetivo1\outputs\e6b\e6b_vae_sd15.csv'))); print(len(r),'filas |',len(r[0]),'columnas')"
```

Meta: **178 filas y 56 columnas**. Y que las medianas de MAE del `.md` nuevo coincidan con las de
`e6b_mae_20260915\e6b_vae_sd15.md` (hueso: 152.05 / 212.00 / 162.95 en `vae regla`).

## P1: compuerta del Objetivo 1 con decodificador afinado (decision 2026-09-17, D.1)

GPU (RTX A6000, particion `gpu`). Script `experiments/objetivo1/p1_decodificador_sd15.py` (no toca E6b): afina
`post_quant_conv` + `decoder` del VAE de SD 1.5 con el encoder congelado, **una vez por configuracion** (`pub`,
`LW20000`, `pub+asinh`), y evalua en los **34 pacientes de test** el VAE preentrenado (`sd15`) y el afinado con MAE y
RMSE en hueso, metal y `B_delta`. Particion versionada en `experiments/objetivo1/p1_particion.csv` (168 pacientes:
126 train, 8 val, 34 test; semilla 20260917). Regla del Go/No-Go y diseno en el docstring del script.

**Regla preinscrita (autora, 2026-09-17, antes de correr):** Go si ALGUNA combinacion {sd15, afinado} x configuracion
tiene media por paciente del MAE en hueso con `vae regla` < 25 HU sobre los 34 de test. Lo escribe `p1_compuerta.md`,
con IC95 (pase MARGINAL si el limite superior >= 25 HU) y, si pasan varias, la elegida por orden a priori (#76).

**Prueba local (2026-09-17, PC sin GPU, diffusers aislado en el scratchpad):**
- `identidad` + `eco` sobre `CLINIC_0012` (sin metal) y `metal_0006`: identidad frente a E6c **9 de 9**; eco frente a
  identidad **24 de 24** (incluye `bdelta`). Con un valor de E6c alterado en 0.5 HU: **8 de 9** y senala el valor.
- `B_delta` frente a fuerza bruta en un volumen sintetico anisotropo: 648 = 648 voxeles.
- VAE diminuto con pesos aleatorios (misma clase `AutoencoderKL`): entrenamiento cortado por `--horas-max`, reanudado
  desde el paso guardado y completado; relanzar con `decoder_<cfg>.pt` ya escrito no hace nada. Encoder congelado (hash
  identico) 1 de 1; decodificador afinado distinto del preentrenado 1 de 1. Control `sd15 frente a E6b` **0 de 4**
  con ese modelo aleatorio: el control puede fallar.
- **El VAE real no se probo en local** (ni velocidad ni memoria de entrenamiento). Su primer uso es la prueba corta.

**Prueba corta (2026-09-17, job 51667, ds001, RTX A6000):** 126 volumenes train y 8 val; **49 490 199 parametros
entrenables**; paso 0 (VAE preentrenado, cortes de val): **val hueso regla MAE 156.02 HU, RMSE 401.18 HU**, del orden de E6b
(`pub+asinh vae regla` mediana 162.95); memoria 4.1 GB antes del primer paso de entrenamiento. Paso 200: **1.32 s/paso,
24.6 GB** de GPU, val hueso regla MAE 130.92 HU; COMPLETO en 5 min 40 s con hash del encoder identico. Estimacion:
30 000 pasos x 1.32 s = **~11 h por configuracion** (sin contar val ni lectura de volumenes).
Evaluacion 51668: **~65 s por volumen y modelo con 1 configuracion**; `sd15 pub+asinh vae regla hueso` en `metal_0006` =
242.9751, la misma cifra que E6b. Controles de hash OK. **Fallo rc=1 al final** (`FileNotFoundError:
e6b_vae_sd15_mae_20260915.csv`): el `scp` de la cohorte E6b no se habia hecho. Desde entonces el script comprueba
`--e6c`, `--e6b` y `--particion` antes de cargar modelos. 51668 y 51669 no compartieron GPU (51669 arranco 22 s despues).
Tras subir el CSV, `resumen` en el **nodo de acceso** (segundos, sin GPU) cerro los controles de la prueba:
**sd15 frente a E6b 4 de 4** (tolerancia 0.05 HU), identidad frente a E6c 2 de 2, encoder congelado 1 de 1 y
decodificador afinado distinto 1 de 1. La tuberia reproduce E6b: la cohorte queda validada.

**Cohorte de entrenamiento (2026-09-17/18):** `pub+asinh` 51669 COMPLETED 10:36:07 (ds001); `LW20000` 51670 COMPLETED
10:33:24 (g002); `pub` 51671 **CANCELLED** (`ExitCode 0:15`, SIGTERM) a las 5:56:43 en ds001, atribuido por la autora a
mantenimiento. Quedo `ckpt_pub.pt` (checkpoint cada 1000 pasos) y se relanza la misma configuracion, que reanuda desde
ahi. **Declarar:** el decodificador de `pub` se entreno con una interrupcion; el orden de cortes tras reanudar no
reproduce el de una corrida continua (pesos y optimizador si se restauran). 51670 y 51671 estuvieron ~10 h en
`JobHeldUser` antes de arrancar (`scontrol hold` sin liberar).
Log de 51671: `CANCELLED AT 2026-09-18T11:29:23 DUE to SIGNAL Terminated`, sin mencion de tiempo ni de preempcion.
Ultimo checkpoint en el paso **16 000** (11:11:15): se pierden ~18 min. Relanzado como **51878**, con la evaluacion
**51879** encolada con `afterok:51878`.

**Corrida real (2026-09-19):** 51878 reanudo `pub` desde el paso 16 000 (g002) y termino en el paso 30 000. Evaluacion
51879: 68 filas (34 x 2), 0 errores, mediana 177 s por fila, 3.22 h. Controles: identidad frente a E6c 165/165, sd15
frente a E6b 330/330, encoder congelado 3/3, decodificador distinto 3/3. **Resultado: NO-GO** (#91).

**Paso 1: subir** (PowerShell local). `e6b_vae_sd15.py`, `e6c_techo_lw.py` y `e6c_techo_lw.csv` ya estan en `qc/`
desde E6b; se vuelven a subir para asegurar la version. La cohorte MAE de E6b va con fecha en el nombre (control):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo1
ssh kiara.balcazar@khipu.utec.edu.pe "mkdir -p ~/metalsynth/qc ~/metalsynth/data/p1"
scp p1_entrenar.sbatch p1_evaluar.sbatch kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp p1_decodificador_sd15.py p1_particion.csv e6b_vae_sd15.py e6c_techo_lw.py e6c_techo_lw.csv kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
scp outputs\e6b_vae_sd15.csv kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/e6b_vae_sd15_mae_20260915.csv
```

**Paso 2: comprobar** (Khipu). El entorno `e6b` y los pesos de SD 1.5 ya existen (E6b, paso 2):

```bash
cd ~/metalsynth
sed -i 's/\r$//' p1_*.sbatch
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate e6b && python -c "import torch, diffusers, nibabel, pandas, scipy; print('ok')"
ls -l data/derivados/dataset7_CLINIC_metal_0059u0071_union.nii.gz      # la union de P158
find data/extracted -name '*_data.nii*' | wc -l                         # 178
wc -l qc/p1_particion.csv                                               # 169 (168 + cabecera)
ls -l qc/e6b_vae_sd15_mae_20260915.csv qc/e6c_techo_lw.csv               # los dos deben existir (51668 fallo por esto)
squeue -u $USER -o "%.8i %.14j %.9P %.2t %.10M %.8N %R"
sbatch --test-only p1_entrenar.sbatch pub+asinh
```

**Paso 3: prueba corta** (Khipu): 200 pasos de `pub+asinh` y evaluacion de 1 caso de test con ese decodificador.
Salida aparte en `data/p1_prueba/` para no mezclarla con la cohorte.

```bash
cd ~/metalsynth
P=$(sbatch --parsable --time=01:00:00 p1_entrenar.sbatch pub+asinh --pasos 200 --cada-val 100 --cada-ckpt 100 --out $HOME/metalsynth/data/p1_prueba/pesos); echo "P1_prueba_entrenar=$P" | tee -a p1_jobs.txt
Q=$(sbatch --parsable --time=01:00:00 --dependency=afterok:$P p1_evaluar.sbatch --pesos $HOME/metalsynth/data/p1_prueba/pesos --configs pub+asinh --casos dataset7_CLINIC_metal_0006_data --out $HOME/metalsynth/data/p1_prueba/eval); echo "P1_prueba_evaluar=$Q" | tee -a p1_jobs.txt
squeue -j $P,$Q -o "%.8i %.12j %.2t %.10M %.8N %R"
until [ -f p1_entrenar_$P.log ]; do sleep 20; done; tail -f p1_entrenar_$P.log     # Ctrl+C para salir
```

En `p1_entrenar_$P.log`, lee:
- `nvidia-smi` y `cuda True`;
- `paso 0 ... val hueso regla MAE X`: el VAE preentrenado sobre los cortes de val. Debe ser del orden de E6b
  (cientos de HU); si da cerca de 0 o NaN, algo esta mal y **no lances la cohorte**;
- `paso 200 ... | S s/paso | mem M GB`: **S x 30000 / 3600 = horas por configuracion**. Si pasa de 23 h, el job sale
  con `INCOMPLETO` y se relanza igual (reanudable); anotalo, no cambies `--pasos` por eso. Si da `CUDA out of memory`,
  copia el mensaje y para: bajar `--lote-entreno` es un cambio de diseno;
- `COMPLETO ... CONTROL encoder congelado: hash identico`.

En `p1_evaluar_$Q.log` (`tail -40`), lee:
- `CONTROL encoder congelado ... [pub+asinh, paso 200]: OK` y `decodificador afinado distinto del preentrenado ... OK`;
- `CONTROL identidad frente a E6c float: 2 de 2`;
- `CONTROL sd15 frente a E6b: 4 de 4` (tolerancia 0.05 HU). **Si no es 4 de 4, no lances la cohorte**: la tuberia
  no reproduce E6b;
- `ok N s` por fila (aqui 1 configuracion; la cohorte evalua 3 por modelo).

**Paso 4: entrenar las tres configuraciones** (Khipu), **solo despues de leer la prueba corta** (lección 8: con la
prueba en cola, los tres entrenamientos llenan el cupo de envíos). Tres jobs de 8 CPU y 32G suman 24 CPU y 96G (tope `a-tesis`:
32 CPU, 98G, 3 jobs): **no puede haber nada mas corriendo**. Solo hay dos RTX A6000 (g002, ds001): el tercero queda
en `PD (Resources)` hasta que se libere una; es normal.

```bash
cd ~/metalsynth
squeue -u $USER                                          # vacio
for C in pub+asinh LW20000 pub; do J=$(sbatch --parsable p1_entrenar.sbatch $C); echo "P1_entrenar_$C=$J" | tee -a p1_jobs.txt; done
```

Seguimiento:

```bash
cat p1_jobs.txt
squeue -u $USER -o "%.8i %.12j %.2t %.10M %.8N %R"
tail -3 data/p1/pesos/curva_*.csv                         # una fila cada 1000 pasos
grep -H "COMPLETO\|INCOMPLETO\|ERROR" p1_entrenar_*.log
ls data/p1/pesos/decoder_*.pt                              # meta: 3
sacct -j <ids> --format=JobID,JobName,State,ExitCode,Elapsed,MaxRSS
```

Si un log dice `INCOMPLETO` o el job se corto, relanza **la misma configuracion**: `sbatch p1_entrenar.sbatch <cfg>`
(sigue desde `ckpt_<cfg>.pt`; el orden de los cortes tras reanudar no se reproduce, declarado en el script).

**Paso 5: evaluar** (Khipu), cuando esten los tres `decoder_*.pt` (si falta uno, el script aborta al arrancar):

```bash
cd ~/metalsynth
E=$(sbatch --parsable p1_evaluar.sbatch); echo "P1_evaluar=$E" | tee -a p1_jobs.txt
tail -f p1_evaluar_$E.log                                  # 68 lineas "ok": 34 casos x (sd15, afinado)
wc -l data/p1/eval/p1_eval.csv                             # meta: 69
cat data/p1/eval/p1_eval_errores.csv                       # solo cabecera
grep "CONTROL\|Resultado\|Sin veredicto" p1_evaluar_$E.log
sacct -j $E --format=JobID,State,ExitCode,Elapsed,MaxRSS
```

Controles esperados: identidad frente a E6c con 6 valores por caso con metal y 3 sin metal (la union de P158 no esta en
E6c); `sd15 frente a E6b` con 12 por caso con metal y 6 sin metal; encoder congelado y decodificador distinto **3 de 3**
cada uno. Tiempo sin medir: por E6b, ~180 s por volumen y modelo con tres configuraciones, mas `B_delta`.
Si se corta, relanza el mismo `sbatch`: salta los pares (Caso, modelo) ya escritos.

**Paso 6: traer** (PowerShell). Los pesos (~3 x 200 MB) no hacen falta en la PC para leer el resultado:

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
mkdir experiments\objetivo1\outputs\p1
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/p1/eval experiments\objetivo1\outputs\p1\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/p1/pesos/curva_*.csv" experiments\objetivo1\outputs\p1\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/p1_*.log" experiments\objetivo1\outputs\p1\
```

## P1-MAISI: ida y vuelta con el VAE 3D de MAISI (extension del Objetivo 1, decision 2026-09-19)

Subordinado a la opcion A: **si compite con el renderizador por GPU o por tiempo, va primero A**. Su resultado
**no cambia** el diseno del Objetivo 3. Script: `experiments/objetivo1/p1_maisi.py` (subcomandos `inspeccionar` y
`evaluar`) y `p1_maisi.sbatch`. Regla: la misma de P1 (#76), media por paciente del MAE en hueso < 25 HU en los 34 de
test. **El paso 0 no es opcional:** `guo2025maisi` no publica como normaliza los HU (#93), y el script **aborta** si no
se le pasan `--hu-min/--hu-max`.

**Paso 1: subir** (PowerShell local). El resto de archivos (`p1_decodificador_sd15.py`, `e6b_vae_sd15.py`,
`e6c_techo_lw.py`, `p1_particion.csv`) ya estan en `~/metalsynth/qc/` desde P1:

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis\experiments\objetivo1
scp p1_maisi.sbatch kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/
scp p1_maisi.py p1_decodificador_sd15.py kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/qc/
```

**Paso 2: entorno y pesos** (Khipu, **nodo de acceso**, que es el que tiene internet; una sola vez):

```bash
cd ~/metalsynth
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda create -y -n maisi --clone e6b          # no se toca el entorno de P1
conda activate maisi
pip install "monai-weekly[nibabel,tqdm]" fire   # `fire` lo necesita la linea de comandos de MONAI
python -c "import monai, torch; print('monai', monai.__version__, 'torch', torch.__version__)"
# Nombre exacto del bundle, por la API de Python (no hace falta la CLI ni `fire`):
python -c "from monai.bundle import get_all_bundles_list; L=get_all_bundles_list(); print([n for n in L if 'maisi' in str(n).lower()]); print('total bundles:', len(L))"
# Descarga con el nombre que imprima la linea anterior (NO pegar marcadores tipo <...>: bash lee '<' como redireccion):
python -c "from monai.bundle import download; download(name='maisi_ct_generative', bundle_dir='$HOME/metalsynth/modelos')"
ls -R $HOME/metalsynth/modelos | head -40
```

Si la lista sale vacia (con `total bundles` > 0), el bundle no esta en el indice de esa version de MONAI: hay que
bajarlo a mano desde el nodo de acceso y descomprimirlo en `~/metalsynth/modelos/maisi/`. **Anota que version bajaste**:
el paper no basta para reproducir (#93).

**Errores ya vistos (2026-09-20):** `OptionalImportError: import fire` al usar `python -m monai.bundle ...` (falta
`fire`, o se usa la API de Python); y `-bash: nombre_exacto: No such file or directory` por pegar el marcador
`<nombre_exacto>` tal cual.

**Paso 3: PASO 0, sin GPU** (nodo de acceso, segundos):

```bash
cd ~/metalsynth
sed -i 's/\r$//' p1_maisi.sbatch
cd qc
python p1_maisi.py inspeccionar --bundle $HOME/metalsynth/modelos/maisi
```

Lee la salida:
- si el recorte de intensidad **deja fuera el hueso denso** (algo como `a_max` = 1000 HU), **MAISI se descarta por
  diseno**: se anota en #93 y no se corre nada mas. Es el resultado barato, y tambien sirve al Objetivo 1;
- si el rango cubre hueso y metal, apunta `a_min` y `a_max`: son los `--hu-min/--hu-max` del paso 4.

**Paso 4: prueba corta de 1 caso** (Khipu, GPU), sustituyendo A y B por lo que dijo el paso 0:

```bash
cd ~/metalsynth
P=$(sbatch --parsable --time=02:00:00 p1_maisi.sbatch --hu-min A --hu-max B --casos dataset7_CLINIC_metal_0006_data --out $HOME/metalsynth/data/p1_maisi_prueba); echo "MAISI_prueba=$P" | tee -a p1_jobs.txt
squeue -j $P -o "%.8i %.2t %.10M %.8N %R"
until [ -f p1_maisi_$P.log ]; do sleep 20; done; tail -f p1_maisi_$P.log
```

En el log, lee: que aparezcan `monai` y `cuda True`; que `claves no cargadas` sea cercano a 0 (si son cientos, el
bundle y el codigo no casan y hay que parar); y la linea `ok N s | hueso ...`. Si da `CUDA out of memory`, baja
`--bloque` (por defecto 128 cortes) y anotalo: eso cambia el solape, no la regla.

**Paso 5: los 34 de test** (Khipu):

```bash
cd ~/metalsynth
M=$(sbatch --parsable p1_maisi.sbatch --hu-min A --hu-max B); echo "MAISI=$M" | tee -a p1_jobs.txt
tail -f p1_maisi_$M.log
wc -l data/p1_maisi/p1_maisi.csv          # meta: 35 (34 + cabecera)
cat data/p1_maisi/p1_maisi_errores.csv    # solo cabecera
grep "Media por paciente\|Sin veredicto" p1_maisi_$M.log
sacct -j $M --format=JobID,State,ExitCode,Elapsed,MaxRSS
```

Si se corta, relanza el mismo `sbatch`: salta los casos ya escritos.

**Paso 6: traer** (PowerShell):

```powershell
cd D:\UTEC\CICLOX\PFCII\metalsynth-pelvis
scp -r kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/p1_maisi experiments\objetivo1\outputs\
scp "kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/p1_maisi_*.log" experiments\objetivo1\outputs\p1_maisi\
```

**Al leer el resultado:** MAISI es 3D y de un canal, asi que **no hay `oraculo` ni `regla`** y la comparacion con P1 es
solo contra la columna de HU reconstruidos. El veredicto se escribe en `p1_maisi.md` con el mismo umbral de 25 HU.
