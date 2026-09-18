#!/bin/bash
# P1: afina post_quant_conv + decoder del VAE de SD 1.5 (encoder congelado) para UNA configuracion.
# Uso: sbatch p1_entrenar.sbatch <pub|LW20000|pub+asinh> [argumentos extra de `entrenar`; el ultimo gana]
# GPU RTX A6000 (particion gpu). Reanudable: si sale por --horas-max o se corta, relanzar el mismo comando.
# Requiere: ~/metalsynth/qc/{p1_decodificador_sd15.py, p1_particion.csv, e6b_vae_sd15.py, e6c_techo_lw.py},
#           entorno conda e6b (clon de totalseg + diffusers) y ~/metalsynth/modelos/sd15/vae/.
# Salida por defecto: ~/metalsynth/data/p1/pesos/{decoder_<cfg>.pt, ckpt_<cfg>.pt, curva_<cfg>.csv}
# Memoria 32G: tres entrenamientos a la vez suman 96G, dentro del tope de a-tesis (98G).
#
# --- SLURM ---
#SBATCH --job-name=p1_entrenar
#SBATCH --partition=gpu
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=24:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

CFG=$1
case "$CFG" in
    pub|LW20000|pub+asinh) shift ;;
    *) echo "ERROR: primer argumento = configuracion (pub, LW20000 o pub+asinh); recibido '$CFG'"; exit 1 ;;
esac

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
echo "inicio $(date -Is)  nodo $(hostname)  config $CFG"
python p1_decodificador_sd15.py entrenar --config "$CFG" --particion p1_particion.csv \
    --data "$DATA/extracted" "$DATA/derivados" --modelo "$HOME/metalsynth/modelos/sd15" \
    --out "$DATA/p1/pesos" --horas-max 23 "$@"
rc=$?
echo "fin $(date -Is)  rc=$rc  config $CFG"
exit $rc
