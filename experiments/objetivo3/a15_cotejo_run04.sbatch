#!/bin/bash
# A15 COTEJO run04 en Khipu: eleccion de checkpoint del difusor reentrenado sin fuga (#166).
# Candidatos fijados ANTES de mirar resultados (autora, 2026-10-11; propuesta de #166, ultima vineta):
#   run04/mejor.pt (minimo de validacion) y run04/ckpt.pt (final, 60 000 pasos).
# Misma regla que 2026-10-05 (6) / 2026-10-09: 5 semillas, receptores 0101/0102, cascaras de 1 mm,
# referencia `metal_0039` (la aplica `a17_cotejo.py --paso-mm 1` en local).
#
# Derivado de `a15_cotejo.sbatch` (que queda como el de run01/run02, archivado). Solo cambian los
# checkpoints, las etiquetas, el ancho de cascara (solo 1 mm, el decidido) y la salida.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch experiments/objetivo3/a15_cotejo_run04.sbatch                             # 0101 y 0102
#   sbatch experiments/objetivo3/a15_cotejo_run04.sbatch dataset6_CLINIC_0102_data   # solo uno
# Salida: $DATA/a15_cotejo_run04/, u otra con `SALIDA`.
#SBATCH --job-name=a15cot04
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
SALIDA=${SALIDA:-$DATA/a15_cotejo_run04}
CASOS=("$@")
[ ${#CASOS[@]} -eq 0 ] && CASOS=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$DATA/a7/run04/mejor.pt" "$DATA/a7/run04/ckpt.pt" \
         "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" \
         "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
for viejo in metal_0053 metal_0003; do
    grep -q "dataset7_CLINIC_${viejo}_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
        && { echo "ERROR: p1_particion.csv vieja (aun tiene $viejo; #156/#166)"; exit 1; }
done

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

rc=0
for caso in "${CASOS[@]}"; do
    echo; echo "=== $caso  $(date -Is) ==="
    python -u "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
        --caso "$caso" --cortes 0 --dispositivo cuda --semillas 0 1 2 3 4 --sin-nifti --pasos-cotejo-mm 1.0 \
        --data "$DATA/extracted" \
        --ckpt "$DATA/a7/run04/mejor.pt" "$DATA/a7/run04/ckpt.pt" \
        --etiquetas run04_mejor run04_60k \
        --out-dir "$SALIDA" \
        || { echo "ERROR en $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
