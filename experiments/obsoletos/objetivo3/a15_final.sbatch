#!/bin/bash
# CORRIDA FINAL E-A2, difusor: los 13 pacientes de test sin metal (casos_ea2_test.txt), diseno CONGELADO
# (diseno_A.md seccion 0; 01-decisiones 2026-10-09 (6) y (8)). mejor_37k, 5 semillas, --incluir-banda, NIfTI.
# GPU: shard:rtxa6000:4 en particion all, la MISMA en que se midio `s` de Delta (a15_delta). No mezclar (#151).
#
# USO (desde ~/metalsynth, tras `git pull`):
#   bash scripts/khipu_elegir_gpu.sh experiments/objetivo3/a15_final.sbatch 70 4    # ~13 x 5 min en A100
#   (enviar con el comando que imprima; anotar el tipo de GPU elegido)
#   Relanzar solo algunos:  sbatch ... experiments/objetivo3/a15_final.sbatch dataset6_CLINIC_0012_data ...
# Salida: $DATA/a15_final/
#SBATCH --job-name=a15fin
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=shard:rtxa6000:4
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=06:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=${SALIDA:-$DATA/a15_final}
CASOS=("$@")
[ ${#CASOS[@]} -eq 0 ] && mapfile -t CASOS < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$DATA/a7/run02/mejor.pt" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q "CONGELADO el 2026-10-09" "$REPO/experiments/objetivo3/diseno_A.md" \
    || { echo "ERROR: diseno_A.md no esta congelado (git pull)"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  casos ${#CASOS[@]}"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
rc=0
for caso in "${CASOS[@]}"; do
    echo; echo "=== $caso  $(date -Is) ==="
    python -u "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
        --caso "$caso" --particiones test --corrida-final \
        --cortes 0 --incluir-banda --dispositivo cuda --semillas 0 1 2 3 4 --pasos-cotejo-mm 1.0 \
        --data "$DATA/extracted" --ckpt "$DATA/a7/run02/mejor.pt" --etiquetas mejor_37k \
        --out-dir "$SALIDA" \
        || { echo "ERROR en $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
