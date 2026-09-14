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
