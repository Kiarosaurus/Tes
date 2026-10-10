#!/bin/bash
# CORRIDA FINAL E-A1: reconstruccion del implante real en los 19 de test con metal (diseno_A.md seccion 0).
# Componentes >= 500 mm3, hasta 24 cortes por componente, mejor_37k, 5 semillas. GPU: shard:rtxa6000:4, como a15_final.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   bash scripts/khipu_elegir_gpu.sh experiments/objetivo3/a23_final.sbatch 120 4
# Salida: $DATA/a23_final/ (a23_parches.csv, a23_pacientes.csv y el cache de parches de test)
#SBATCH --job-name=a23fin
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=shard:rtxa6000:4
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=08:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available()" || { echo "ERROR: sin cuda"; exit 1; }
[ -f "$DATA/a7/run02/mejor.pt" ] || { echo "ERROR: falta mejor.pt"; exit 1; }
grep -q "CONGELADO el 2026-10-09" "$REPO/experiments/objetivo3/diseno_A.md" || { echo "ERROR: diseno no congelado"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
python -u "$REPO/experiments/objetivo3/a23_ea1.py" --particiones test --corrida-final --dispositivo cuda \
    --data "$DATA/extracted" --ckpt "$DATA/a7/run02/mejor.pt" --out-dir "$DATA/a23_final"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
