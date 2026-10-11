#!/bin/bash
# A7 run03: reentrenamiento del difusor SIN los volumenes repetidos de #163 (autora, 2026-10-10).
#
# QUE ES: version posterior declarada. La corrida final congelada (E-A1/E-A2) sigue siendo la de
# `mejor_37k` (run02); este modelo no la reemplaza sin una decision nueva de la autora (#163, #164).
#
# UNICA DIFERENCIA con run02 (job 54498): el manifiesto. `a5_manifiesto_train_sin163.csv` es
# `a5_manifiesto_train.csv` sin los 7 volumenes secundarios de #163 (metal_0020, 0026, 0027, 0038,
# 0005, 0052, 0041): 17 149 -> 15 166 parches, 47 -> 40 casos. El resto de filas es identico.
# Mismos hiperparametros que run02 (#148): semilla 20260920 (por omision), lote 16, base 64, lado 256,
# lr 1e-4 constante, 60 000 pasos, validacion cada 500 sobre 16 lotes fijos (SEMILLA_VAL),
# `mejor.pt` por minimo de validacion. Validacion = el mismo `a5_manifiesto_val.csv`. Test no se toca.
#
# Ritmo de referencia: run02 hizo 60 000 pasos en ~6 h 20 (0.38 s/paso, MIG de A100). Con ~12 % menos
# parches el paso cuesta lo mismo; cambia solo cuantas epocas son 60 000 pasos.
#
# SI EL JOB SE CORTA, se relanza EXACTAMENTE igual: `--reanudar` continua desde `ckpt.pt`.
#
# Requiere en ~/metalsynth/ (clon git: `git pull`): `src/renderizador/`, `src/common/`,
# `experiments/objetivo1/{p1_particion.csv,e6c_techo_lw.py,e6b_vae_sd15.py}`, los manifiestos, y la
# cache de A1b en $DATA/a1b_cache.
# Salida: $DATA/a7/run03/{ckpt.pt, mejor.pt, curva.csv}
#SBATCH --job-name=a7run03
#SBATCH --partition=gpu
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=$DATA/a7/run03
MAN=$REPO/experiments/objetivo3/a5_manifiesto_train_sin163.csv

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())" \
    || { echo "ERROR: falta torch"; exit 1; }
[ -f "$MAN" ] || { echo "ERROR: falta $MAN (git pull)"; exit 1; }
n=$(($(wc -l < "$MAN") - 1))
[ "$n" -eq 15166 ] || { echo "ERROR: el manifiesto tiene $n parches, se esperaban 15166"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  parches $n"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

python -u "$REPO/src/renderizador/entrenar.py" \
    --cache "$DATA/a1b_cache" \
    --particion "$REPO/experiments/objetivo1/p1_particion.csv" \
    --manifiesto "$MAN" \
    --manifiesto-val "$REPO/experiments/objetivo3/a5_manifiesto_val.csv" \
    --out "$SALIDA" \
    --pasos 60000 \
    --lote 16 \
    --base 64 \
    --lado 256 \
    --lr 1e-4 \
    --cada 500 \
    --lotes-val 16 \
    --cada-ckpt 5000 \
    --trabajadores "$SLURM_CPUS_PER_TASK" \
    --reanudar
rc=$?
echo "fin $(date -Is)  rc=$rc"
echo "ultimas filas de la curva:"
tail -5 "$SALIDA/curva.csv" 2>/dev/null
exit $rc
