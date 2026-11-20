#!/bin/bash
# B MINIMA (POST-HOC, EXPLORATORIA): ajuste fino de run04_mejor con termino de amplitud angular.
# Reglas: docs/01-decisiones.md 2026-11-20 (3), puntos 7-9. Termino: src/renderizador/angular.py.
#
# QUE ES: parte de `$DATA/a7/run04/mejor.pt` (paso 16 500), 3 000 pasos, lr 5e-5, lote 16, mismos datos, manifiesto,
# validacion y semilla que run04. LAMBDA=0.05 es el brazo B; LAMBDA=0 es el CONTROL DE AJUSTE FINO (seguir
# entrenando sin el termino, ruta identica a `perdida`). Se evalua el `ckpt.pt` FINAL (paso 3 000), no `mejor.pt`.
#
# USO (desde ~/metalsynth, rama exp/b-minima-angular):
#   sbatch --test-only --export=ALL,LAMBDA=0.05 experiments/objetivo3/a7_b_minima.sbatch
#   humo (200 pasos, 30 min):  sbatch --time=00:30:00 --export=ALL,LAMBDA=0.05,PASOS=200,SALIDA=$HOME/metalsynth/data/a7/b_min_humo experiments/objetivo3/a7_b_minima.sbatch
#   B:        sbatch --export=ALL,LAMBDA=0.05 experiments/objetivo3/a7_b_minima.sbatch
#   control:  sbatch --export=ALL,LAMBDA=0    experiments/objetivo3/a7_b_minima.sbatch
# ANGTMAX (por omision 300): tope de t del termino angular. Calibracion en 01-decisiones.md 2026-11-20 (6).
# Salida: $DATA/a7/b_min_l<LAMBDA>/{ckpt.pt, mejor.pt, curva.csv, entrenar_meta.json}
# SI EL JOB SE CORTA, se relanza con REANUDAR=1 (continua desde `ckpt.pt`). Sin REANUDAR=1 y con ckpt.pt previo, aborta (evita un humo que no entrena).
#SBATCH --job-name=a7bmin
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=03:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
[ -n "${LAMBDA:-}" ] || { echo "ERROR: falta LAMBDA (0.05 = B, 0 = control de ajuste fino)"; exit 1; }
SALIDA=${SALIDA:-$DATA/a7/b_min_l$LAMBDA}
PASOS=${PASOS:-3000}
if [ -f "$SALIDA/ckpt.pt" ] && [ -z "${REANUDAR:-}" ]; then
    echo "ERROR: $SALIDA ya tiene ckpt.pt; --reanudar no entrenaria nada. Usa otra SALIDA o REANUDAR=1 para continuar un job cortado."
    exit 1
fi
INIT=$DATA/a7/run04/mejor.pt
MAN=$REPO/experiments/objetivo3/a5_manifiesto_train_run04.csv

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch, scipy; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: falta torch/scipy/cuda"; exit 1; }
[ -f "$INIT" ] || { echo "ERROR: falta $INIT"; exit 1; }
[ -f "$MAN" ] || { echo "ERROR: falta $MAN (git pull)"; exit 1; }
n=$(($(wc -l < "$MAN") - 1))
[ "$n" -eq 14182 ] || { echo "ERROR: el manifiesto tiene $n parches, se esperaban 14182"; exit 1; }
grep -q "'--ang-lambda'" "$REPO/src/renderizador/entrenar.py" || { echo "ERROR: entrenar.py sin B minima (rama exp/b-minima-angular)"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  LAMBDA=$LAMBDA  pasos $PASOS  commit $(git -C "$REPO" rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

python -u "$REPO/src/renderizador/entrenar.py" \
    --cache "$DATA/a1b_cache" \
    --particion "$REPO/experiments/objetivo1/p1_particion.csv" \
    --manifiesto "$MAN" \
    --manifiesto-val "$REPO/experiments/objetivo3/a5_manifiesto_val.csv" \
    --out "$SALIDA" \
    --pasos "$PASOS" \
    --lote 16 \
    --base 64 \
    --lado 256 \
    --lr 5e-5 \
    --cada 250 \
    --lotes-val 16 \
    --cada-ckpt 1000 \
    --trabajadores "$SLURM_CPUS_PER_TASK" \
    --preinscrito \
    --init-modelo "$INIT" \
    --ang-lambda "$LAMBDA" \
    --ang-tmax "${ANGTMAX:-300}" \
    --ang-k 48 \
    --reanudar
rc=$?
echo "fin $(date -Is)  rc=$rc"
echo "ultimas filas de la curva:"
tail -5 "$SALIDA/curva.csv" 2>/dev/null
exit $rc
