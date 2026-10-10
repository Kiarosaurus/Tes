#!/bin/bash
# CORRIDA FINAL E-A2, brazo fisico de Peters: los 13 pacientes de test sin metal, una tarea por paciente.
# Diseno CONGELADO (diseno_A.md seccion 0): Ti primario, Fe sensibilidad, replicas A/B, k = 2. Solo CPU.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only -p big-mem experiments/objetivo3/a19_final.sbatch
#   J=$(sbatch --parsable -p big-mem experiments/objetivo3/a19_final.sbatch); echo $J
# QoS a-tesis: 32 CPU por usuario -> %2 (dos tareas de 16 CPU a la vez). ~0.5-0.7 h por paciente.
# Salida: $DATA/a19_final/
#SBATCH --job-name=a19fin
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --array=0-12%2
#SBATCH --cpus-per-task=16
#SBATCH --mem=40G
#SBATCH --time=03:00:00
#SBATCH --output=%x_%A_%a.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
mapfile -t CASOS < "$REPO/experiments/objetivo3/casos_ea2_test.txt"
CASO=${CASOS[$SLURM_ARRAY_TASK_ID]}

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import gecatsim" || { echo "ERROR: falta gecatsim (pip install gecatsim==1.6.8)"; exit 1; }
grep -q "CONGELADO el 2026-10-09" "$REPO/experiments/objetivo3/diseno_A.md" \
    || { echo "ERROR: diseno_A.md no esta congelado (git pull)"; exit 1; }

export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
TMP=${SLURM_TMPDIR:-/tmp}/a19fin_${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}
echo "inicio $(date -Is)  nodo $(hostname)  caso $CASO"
python -u "$REPO/experiments/objetivo3/a19_peters_completo.py" \
    --casos "$CASO" --corrida-final --data "$DATA/extracted" --k 2 --trabajadores 8 \
    --out-dir "$DATA/a19_final" --tmp-dir "$TMP"
rc=$?
rm -rf "$TMP"
echo "fin $(date -Is)  rc=$rc"
exit $rc
