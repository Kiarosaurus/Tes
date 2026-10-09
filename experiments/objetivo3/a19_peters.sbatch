#!/bin/bash
# A19 en Khipu: brazo fisico de Peters completo sobre los receptores de VALIDACION (para `Delta`).
# Un paciente por tarea del arreglo. XCIST corre en CPU (biblioteca C): este job NO pide GPU.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only experiments/objetivo3/a19_peters.sbatch             # estimar inicio
#   J=$(sbatch --parsable experiments/objetivo3/a19_peters.sbatch); echo $J  # 0101 y 0102
#   sbatch -p <particion> experiments/objetivo3/a19_peters.sbatch           # otra particion de CPU
#
# Requiere en el entorno `totalseg`: `pip install gecatsim==1.6.8` (la misma version que corrio la sonda).
# Salida: $DATA/a19/a19_<caso>.npz y .json; log por tarea: a19pet_<job>_<tarea>.log
#
# QoS a-tesis: 32 CPU y 98 GB por usuario en total. Dos tareas x 16 CPU = 32.
#SBATCH --job-name=a19pet
#SBATCH --partition=standard
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --array=0-1
#SBATCH --cpus-per-task=16
#SBATCH --mem=40G
#SBATCH --time=06:00:00
#SBATCH --output=%x_%A_%a.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
CASOS=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
CASO=${CASOS[$SLURM_ARRAY_TASK_ID]}

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import gecatsim, numpy; print('gecatsim', getattr(gecatsim, '__version__', '?'))" \
    || { echo "ERROR: falta gecatsim (pip install gecatsim==1.6.8)"; exit 1; }
for f in "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" \
         "$REPO/experiments/objetivo3/peters/AAPM_MAR_scanner.cfg"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done

# un hilo por proceso: el paralelismo lo da el Pool de a19 (8 procesos), no los hilos internos
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
TMP=${SLURM_TMPDIR:-/tmp}/a19_${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}

echo "inicio $(date -Is)  nodo $(hostname)  caso $CASO  cpus $SLURM_CPUS_PER_TASK"
python -u "$REPO/experiments/objetivo3/a19_peters_completo.py" \
    --casos "$CASO" --data "$DATA/extracted" --k 2 --trabajadores 8 \
    --out-dir "$DATA/a19" --tmp-dir "$TMP"
rc=$?
rm -rf "$TMP"
echo "fin $(date -Is)  rc=$rc"
exit $rc
