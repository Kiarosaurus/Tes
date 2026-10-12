#!/bin/bash
# A15 en Khipu: cadena completa (pelvis limpia -> pose -> `M` -> generacion) sobre GPU.
#
# POR QUE EN KHIPU: en la laptop `0102` murio por memoria baja del sistema (2026-10-05), y `0101`
# tardo ~70 min en CPU.
#
# POR QUE SE REPITE `0101`: con la misma semilla, CPU y GPU NO generan el mismo ruido. Para que el
# cotejo entre pacientes use un solo dispositivo, aqui se corren TODOS los pacientes en `cuda`. La
# corrida CPU de la laptop (`outputs/a15/`) queda como control: no se mezcla con esta.
#
# USO (desde ~/metalsynth):
#   sbatch experiments/objetivo3/a15_cadena.sbatch                       # 0101 y 0102
#   sbatch experiments/objetivo3/a15_cadena.sbatch dataset6_CLINIC_0102_data   # solo uno
#
# Requiere en ~/metalsynth/ la misma estructura que el repo: `src/{common,renderizador,muestreador}`,
# `experiments/objetivo1/{p1_decodificador_sd15,e6b_vae_sd15,e6c_techo_lw}.py` y `p1_particion.csv`,
# `experiments/objetivo2/outputs/e9ts_ejes_corredor.csv`, y en `experiments/objetivo3/` los scripts
# `a15`, `a11`, `a1b`, `a1_parches`. Checkpoints en $DATA/a7/run01/ckpt.pt y $DATA/a7/run02/mejor.pt.
# Salida: $DATA/a15_gpu/
#SBATCH --job-name=a15cad
#SBATCH --partition=gpu
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=$DATA/a15_gpu
CASOS=("$@")
[ ${#CASOS[@]} -eq 0 ] && CASOS=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$DATA/a7/run01/ckpt.pt" "$DATA/a7/run02/mejor.pt" \
         "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

rc=0
for caso in "${CASOS[@]}"; do
    echo; echo "=== $caso  $(date -Is) ==="
    python -u "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
        --caso "$caso" --cortes 0 --dispositivo cuda \
        --data "$DATA/extracted" \
        --ckpt "$DATA/a7/run01/ckpt.pt" "$DATA/a7/run02/mejor.pt" \
        --out-dir "$SALIDA" \
        || { echo "ERROR en $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
