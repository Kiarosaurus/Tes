#!/bin/bash
# Version 2, opcion B: precalcula el canal T (plantilla analitica) para todos los parches de $DATA/a1b_cache.
# CPU solamente (Radon + FBP, ~0.5-1 s por parche). Escribe $DATA/a1b_cache_T/{*_T.npy, escala.json}. Reanudable:
# si se corta, se relanza igual y solo calcula lo que falta. run05b espera a este job (--dependency=afterok).
#
# USO (desde ~/metalsynth, tras `git pull`):
#   JT=$(sbatch --parsable experiments/objetivo3/a7_cache_T.sbatch); echo $JT
# Ojo con el tope de a-tesis (32 CPU sumando todo lo que corre): run05a usa 8; este pide 24.
#SBATCH --job-name=a7cacheT
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=24
#SBATCH --mem=32G
#SBATCH --time=03:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import skimage, scipy; print('skimage', skimage.__version__)" || { echo "ERROR: falta scikit-image"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)  cpus $SLURM_CPUS_PER_TASK  commit $(git -C "$REPO" rev-parse --short HEAD)"
python -u "$REPO/experiments/objetivo3/v2_b_cache_T.py" --cache "$DATA/a1b_cache" --out "$DATA/a1b_cache_T" \
    --procesos "$SLURM_CPUS_PER_TASK"
rc=$?
echo "fin $(date -Is)  rc=$rc"
cat "$DATA/a1b_cache_T/escala.json" 2>/dev/null
exit $rc
