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

**Paso 4: cohorte completa** (Khipu):

```bash
cd ~/metalsynth
B=$(sbatch --parsable e6b_vae_sd15.sbatch); echo "E6b=$B" | tee -a e6b_jobs.txt
B=$(grep '^E6b=' e6b_jobs.txt | tail -1 | cut -d= -f2); echo $B     # recupera el id si reconectaste
tail -f e6b_vae_$B.log                                     # una linea "ok" por volumen
sacct -j $B --format=JobID,State,ExitCode,Elapsed,MaxRSS
wc -l data/e6b/e6b_vae_sd15.csv                            # meta: 179 (178 + cabecera)
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
