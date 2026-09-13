#!/bin/bash
# Piloto TotalSegmentator (#29, #48, #49) sobre 2 casos: uno con metal y uno limpio.
# Corre cada caso con los dos modelos de recorte (#49): --robust_crop (3 mm) y por defecto (6 mm).
# Salida: ~/metalsynth/data/ts_piloto/<caso>/<modo>/*.nii.gz
#
# --- SLURM ---  GPU. VERIFICAR account/qos antes de lanzar:
#   sacctmgr show assoc user=$USER format=account,partition,qos%40
#   sinfo -p debug-gpu,gpu -o "%P %a %l %N %G"
#   Verificado 2026-09-12: debug-gpu lleva QoS de particion p-debug-gpu (MaxWall 1h) -> --time<=1h.
#   Particion gpu (QoS p-gpu, sin MaxWall) -> manda a-tesis: 24h, cpu=32, shard=40, mem=98G por usuario.
#SBATCH --job-name=ts_piloto
#   g001/g002/ds001 (GPU entera) ocupados el 2026-09-12; ag001 tiene 5 gres/gpu (A100 + MIG) -> 3g.20gb libre.
#SBATCH --partition=gpu
#SBATCH --gres=shard:a100_3g.20gb:1
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=%x_%j.log

set -eo pipefail

DEVICE=gpu            # cpu si se corre en big-mem
CASOS=(dataset7_CLINIC_metal_0008_data dataset6_CLINIC_0002_data)
ROI=(sacrum vertebrae_S1 hip_left hip_right)
IN_DIR=$HOME/metalsynth/data/ts_input
OUT_DIR=$HOME/metalsynth/data/ts_piloto
export TOTALSEG_HOME_DIR=$HOME/metalsynth/totalseg_home

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg

echo "== procedencia =="
date -Is
hostname
pip show TotalSegmentator | grep -E "^(Name|Version):"   # no usar head: con pipefail, SIGPIPE mata el job
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())"
if [ "$DEVICE" = gpu ]; then
    nvidia-smi --query-gpu=name,memory.total --format=csv
    python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)" \
        || { echo "ERROR: sin CUDA en el nodo; aborto para no caer a CPU en silencio"; exit 1; }
fi

mkdir -p "$OUT_DIR"
for caso in "${CASOS[@]}"; do
    f="$IN_DIR/${caso}.nii.gz"
    [ -e "$f" ] || { echo "ERROR: falta $f"; exit 1; }
    sha256sum "$(readlink -f "$f")"
    for modo in robust3mm default6mm; do
        extra=()
        [ "$modo" = robust3mm ] && extra=(--robust_crop)
        out="$OUT_DIR/$caso/$modo"
        mkdir -p "$out"
        echo "== $caso / $modo =="
        t0=$(date +%s)
        TotalSegmentator -i "$f" -o "$out" --task total \
            --roi_subset "${ROI[@]}" "${extra[@]}" \
            --device "$DEVICE" --nr_thr_resamp "$SLURM_CPUS_PER_TASK" --nr_thr_saving 2
        echo "segundos: $(( $(date +%s) - t0 ))"
        ls -la "$out"
    done
done
echo "== fin =="
date -Is
