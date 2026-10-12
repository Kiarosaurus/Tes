#!/bin/bash
# A15 COTEJO en Khipu: cadena completa sobre GPU, 2 checkpoints x 5 semillas, con salida `_cotejo.csv`
# (perfil 2D de 0.5 mm con elevacion e histograma en `M`; 01-decisiones.md 2026-10-07 (2) y 2026-10-08 (2)).
# La referencia real (2 tornillos de `metal_0039`) y la regla las aplica `a17_cotejo.py` en local.
#
# Derivado de `a15_cadena.sbatch`: TODOS los pacientes en `cuda`, porque con la misma semilla CPU y GPU no
# generan el mismo ruido (#151). Lectura de HU v2 (`delta = 0.05`), la de omision de `a15`.
#
# USO (desde ~/metalsynth):
#   sbatch experiments/objetivo3/a15_cotejo.sbatch                             # 0101 y 0102
#   sbatch experiments/objetivo3/a15_cotejo.sbatch dataset6_CLINIC_0102_data   # solo uno
#
# Requiere lo mismo que `a15_cadena.sbatch` mas `src/common/cotejo.py` y la `p1_particion.csv` nueva
# (sin `metal_0053`, #156). Checkpoints en $DATA/a7/run01/ckpt.pt y $DATA/a7/run02/mejor.pt.
# Salida: $DATA/a15_cotejo/, u otra con `SALIDA`:
#   sbatch --export=ALL,SALIDA=$HOME/metalsynth/data/a15_cotejo_1mm ...
# El mismo `_cotejo.csv` lleva cascaras de 0.5 y de 1 mm (columna `paso_mm`; sensibilidad #157).
#SBATCH --job-name=a15cot
#SBATCH --partition=gpu
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=${SALIDA:-$DATA/a15_cotejo}
CASOS=("$@")
[ ${#CASOS[@]} -eq 0 ] && CASOS=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$DATA/a7/run01/ckpt.pt" "$DATA/a7/run02/mejor.pt" \
         "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" \
         "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q "dataset7_CLINIC_metal_0053_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
    && { echo "ERROR: p1_particion.csv vieja (aun tiene metal_0053, #156)"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

rc=0
for caso in "${CASOS[@]}"; do
    echo; echo "=== $caso  $(date -Is) ==="
    python -u "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
        --caso "$caso" --cortes 0 --dispositivo cuda --semillas 0 1 2 3 4 --sin-nifti --pasos-cotejo-mm 0.5 1.0 \
        --data "$DATA/extracted" \
        --ckpt "$DATA/a7/run01/ckpt.pt" "$DATA/a7/run02/mejor.pt" \
        --etiquetas run01_140k mejor_37k \
        --out-dir "$SALIDA" \
        || { echo "ERROR en $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
