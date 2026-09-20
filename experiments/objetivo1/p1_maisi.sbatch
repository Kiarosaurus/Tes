#!/bin/bash
# P1-MAISI: ida y vuelta con el VAE 3D de MAISI sobre los pacientes de test (extension del Objetivo 1).
# Uso: sbatch p1_maisi.sbatch --hu-min <A> --hu-max <B> [mas argumentos de `evaluar`]
# **--hu-min y --hu-max son obligatorios y salen del PASO 0** (`p1_maisi.py inspeccionar`, sin GPU,
# en el nodo de acceso). El script aborta si no se pasan: no asume ninguna normalizacion (#93).
# GPU RTX A6000 (particion gpu). Reanudable por caso.
# Requiere: entorno conda `maisi` (clon de e6b + monai), bundle en ~/metalsynth/modelos/maisi/ y
#           ~/metalsynth/qc/{p1_maisi.py, p1_decodificador_sd15.py, e6b_vae_sd15.py, e6c_techo_lw.py,
#           p1_particion.csv}.
# Salida por defecto: ~/metalsynth/data/p1_maisi/{p1_maisi.csv, _errores.csv, .md}
#
# --- SLURM ---
#SBATCH --job-name=p1_maisi
#SBATCH --partition=gpu
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate maisi || { echo "ERROR: no se activo el entorno maisi (ver KHIPU.md, P1-MAISI)"; exit 1; }
export HF_HUB_OFFLINE=1
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch, monai, nibabel, pandas, scipy; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), 'monai', monai.__version__)" \
    || { echo "ERROR: faltan dependencias en el entorno maisi"; exit 1; }

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)"
python p1_maisi.py evaluar --bundle "$HOME/metalsynth/modelos/maisi" --particion p1_particion.csv \
    --data "$DATA/extracted" "$DATA/derivados" --out "$DATA/p1_maisi" "$@"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
