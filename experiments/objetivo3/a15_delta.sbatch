#!/bin/bash
# A15 DELTA en Khipu: difusor con el checkpoint ELEGIDO (`mejor_37k`, 01-decisiones 2026-10-09), 5 semillas,
# volumenes .nii.gz y TODOS los cortes que toca `G` (`--incluir-banda`, #160), sobre los receptores de
# validacion. Es el componente "dispersion entre semillas DDIM" de `Delta` (D4); el otro es el test-retest de
# Peters (`a19`). Los dos los mide `a20_evaluador_ea2.py`.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   bash scripts/khipu_elegir_gpu.sh experiments/objetivo3/a15_delta.sbatch 11 4
#   (y enviar con el comando que imprime)
# Salida: $DATA/a15_delta/ (un .nii.gz por semilla y paciente, mas original, M y G)
#SBATCH --job-name=a15del
#SBATCH --partition=gpu
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:a100_3g.20gb:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=01:30:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=${SALIDA:-$DATA/a15_delta}
CASOS=("$@")
[ ${#CASOS[@]} -eq 0 ] && CASOS=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$DATA/a7/run02/mejor.pt" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" \
         "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q -- "--incluir-banda" "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
    || { echo "ERROR: a15 sin --incluir-banda (git pull)"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

rc=0
for caso in "${CASOS[@]}"; do
    echo; echo "=== $caso  $(date -Is) ==="
    python -u "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
        --caso "$caso" --cortes 0 --incluir-banda --dispositivo cuda --semillas 0 1 2 3 4 \
        --pasos-cotejo-mm 1.0 \
        --data "$DATA/extracted" \
        --ckpt "$DATA/a7/run02/mejor.pt" --etiquetas mejor_37k \
        --out-dir "$SALIDA" \
        || { echo "ERROR en $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
