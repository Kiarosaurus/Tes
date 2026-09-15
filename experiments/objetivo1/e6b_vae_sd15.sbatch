#!/bin/bash
# E6b: ida y vuelta HU -> ventanas -> VAE de SD 1.5 -> HU sobre los 178 CT (e6b_vae_sd15.py; #36, #39).
# GPU RTX A6000 (particion gpu). Reanudable: relanzar continua donde quedo.
# Requiere: ~/metalsynth/qc/{e6b_vae_sd15.py, e6c_techo_lw.py, e6c_techo_lw.csv},
#           entorno conda e6b (clon de totalseg + diffusers) y ~/metalsynth/modelos/sd15/vae/.
# Salida por defecto: ~/metalsynth/data/e6b/{e6b_vae_sd15.csv, _errores.csv, _control.csv, .md}
# Argumentos extra se pasan al script (el ultimo --out gana), p. ej.:
#   sbatch --time=02:00:00 e6b_vae_sd15.sbatch --casos dataset7_CLINIC_metal_0000_data --out ~/metalsynth/data/e6b_prueba
#
# --- SLURM ---
#SBATCH --job-name=e6b_vae
#SBATCH --partition=gpu
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=24:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate e6b || { echo "ERROR: no se activo el entorno e6b"; exit 1; }
export HF_HUB_OFFLINE=1
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch, diffusers, nibabel, pandas; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), 'diffusers', diffusers.__version__)" \
    || { echo "ERROR: faltan dependencias en e6b (ver KHIPU.md, E6b)"; exit 1; }

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)"
python e6b_vae_sd15.py --data "$DATA/extracted" --out "$DATA/e6b" --modelo "$HOME/metalsynth/modelos/sd15" \
    --e6c e6c_techo_lw.csv "$@"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
