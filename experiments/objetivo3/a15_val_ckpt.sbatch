#!/bin/bash
# EVALUACION EN VALIDACION de un checkpoint (B minima y su control), 0101/0102, con NIfTI para C4 y D2.
# Reglas: docs/01-decisiones.md 2026-11-20 (3), punto 8. POST-HOC, EXPLORATORIA. Muestreo 50 pasos, eta 0.
# Salida: $DATA/obj3_pose/b_min/<ETIQ>/  (_cotejo.csv, _perfil.csv, NIfTI: original, M, G, sintetica por semilla)
#
# USO (desde ~/metalsynth):
#   sbatch --export=ALL,ETIQ=b_min_l0.05,PT=$HOME/metalsynth/data/a7/b_min_l0.05/ckpt.pt experiments/objetivo3/a15_val_ckpt.sbatch
#   sbatch --export=ALL,ETIQ=b_min_l0,PT=$HOME/metalsynth/data/a7/b_min_l0/ckpt.pt       experiments/objetivo3/a15_val_ckpt.sbatch
#   CORTES=2 para una prueba de humo. DELTA=0.03 por omision (limite de run04_mejor; NO recalibrado para el ajuste fino).
#SBATCH --job-name=a15bmin
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=03:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
[ -n "${ETIQ:-}" ] && [ -n "${PT:-}" ] || { echo "ERROR: faltan ETIQ y PT"; exit 1; }
DELTA=${DELTA:-0.03}
CORTES=${CORTES:-0}
BASE=${BASE:-$DATA/obj3_pose/b_min}
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" || { echo "ERROR: sin cuda"; exit 1; }
for f in "$PT" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  etiqueta $ETIQ  ckpt $PT  delta $DELTA  cortes $CORTES"
A15="$REPO/experiments/objetivo3/a15_cadena_completa.py"
rc=0
for caso in "${VAL[@]}"; do
    echo "=== $ETIQ $caso  $(date -Is) ==="
    python -u "$A15" --caso "$caso" --cortes "$CORTES" --dispositivo cuda --semillas 0 1 2 3 4 \
        --pasos-cotejo-mm 1.0 --data "$DATA/extracted" --ckpt "$PT" --etiquetas "$ETIQ" --delta "$DELTA" \
        --pasos 50 --eta 0 --out-dir "$BASE/$ETIQ" \
        || { echo "ERROR en $ETIQ $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
