#!/bin/bash
# P1: evalua en los pacientes de test el VAE de SD 1.5 preentrenado (sd15) y el de decodificador afinado (afinado),
# con MAE y RMSE en hueso, metal y B_delta, controles (E6c, E6b, hashes) e informe p1_compuerta.md con el veredicto.
# Uso: sbatch p1_evaluar.sbatch [argumentos extra de `evaluar`; el ultimo gana]
# GPU RTX A6000 (particion gpu). Reanudable por (Caso, modelo).
# Requiere: los tres ~/metalsynth/data/p1/pesos/decoder_<cfg>.pt terminados, y en ~/metalsynth/qc/
#           {p1_decodificador_sd15.py, p1_particion.csv, e6b_vae_sd15.py, e6c_techo_lw.py, e6c_techo_lw.csv,
#            e6b_vae_sd15_mae_20260915.csv}.
# Salida por defecto: ~/metalsynth/data/p1/eval/{p1_eval.csv, p1_eval_errores.csv, p1_control.csv,
#                     p1_control_pesos.csv, p1_compuerta.md}
#
# --- SLURM ---
#SBATCH --job-name=p1_evaluar
#SBATCH --partition=gpu
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate e6b || { echo "ERROR: no se activo el entorno e6b"; exit 1; }
export HF_HUB_OFFLINE=1
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch, diffusers, nibabel, pandas, scipy; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), 'diffusers', diffusers.__version__)" \
    || { echo "ERROR: faltan dependencias en e6b (ver KHIPU.md, P1)"; exit 1; }

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)"
python p1_decodificador_sd15.py evaluar --particion p1_particion.csv \
    --data "$DATA/extracted" "$DATA/derivados" --modelo "$HOME/metalsynth/modelos/sd15" \
    --vaes sd15 afinado --pesos "$DATA/p1/pesos" --out "$DATA/p1/eval" \
    --e6c e6c_techo_lw.csv --e6b e6b_vae_sd15_mae_20260915.csv "$@"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
