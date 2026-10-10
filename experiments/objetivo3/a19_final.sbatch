#!/bin/bash
# CORRIDA FINAL E-A2, brazo fisico de Peters: los 13 pacientes de test sin metal, en UN solo job (en serie).
# No es arreglo: cada tarea de un arreglo cuenta como job enviado y choca con QOSMaxSubmitJobPerUserLimit.
# Diseno CONGELADO (diseno_A.md seccion 0): Ti primario, Fe sensibilidad, replicas A/B, k = 2. Solo CPU.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only -p big-mem experiments/objetivo3/a19_final.sbatch
#   J=$(sbatch --parsable -p big-mem experiments/objetivo3/a19_final.sbatch); echo $J
# QoS a-tesis: 32 CPU y 98 GB por usuario EN TOTAL. Con a15_final y a23_final en GPU (4 CPU y 32 GB cada uno)
# quedan 24 CPU y ~34 GB: este job pide 24 y 30G. ~20-30 min por paciente -> ~5-6 h.
# Salida: $DATA/a19_final/
#SBATCH --job-name=a19fin
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=24
#SBATCH --mem=30G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
mapfile -t CASOS < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import gecatsim" || { echo "ERROR: falta gecatsim (pip install gecatsim==1.6.8)"; exit 1; }
grep -q "CONGELADO el 2026-10-09" "$REPO/experiments/objetivo3/diseno_A.md" \
    || { echo "ERROR: diseno_A.md no esta congelado (git pull)"; exit 1; }

export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
TMP=${SLURM_TMPDIR:-/tmp}/a19fin_${SLURM_JOB_ID}
echo "inicio $(date -Is)  nodo $(hostname)  casos ${#CASOS[@]}"
python -u "$REPO/experiments/objetivo3/a19_peters_completo.py" \
    --casos "${CASOS[@]}" --corrida-final --data "$DATA/extracted" --k 2 --trabajadores 12 \
    --out-dir "$DATA/a19_final" --tmp-dir "$TMP"
rc=$?
rm -rf "$TMP"
echo "fin $(date -Is)  rc=$rc"
exit $rc
