#!/bin/bash
# A2 / Diseno A: entrena el renderizador de difusion en espacio de imagen (Objetivo 3).
#
# USO NORMAL, Y EL UNICO AUTORIZADO HOY:
#   sbatch a2_entrenar.sbatch 200            # PRUEBA CORTA: mide s/paso y memoria (#89, #100)
# Corrida larga (SOLO despues de preinscribir diseno_A.md, regla del propio diseno):
#   sbatch a2_entrenar.sbatch 30000 --preinscrito
#
# Conjunto de entrenamiento CONGELADO el 2026-09-21 (01-decisiones): R1 dentro del cuerpo, R2 caso
# con material ortopedico, R3 metal + banda al 0.62 => 17 149 parches, 241 componentes, 47 casos.
# Falta solo el margen Delta de D4. Sin `--preinscrito` el script avisa que es piloto de medicion.
#
# Requiere en Khipu (disposicion de KHIPU.md: .py planos en ~/metalsynth/qc):
#   ~/metalsynth/src/{common,renderizador}/   copia de src/ de la PC
#   ~/metalsynth/qc/  p1_particion.csv, e6c_techo_lw.py, e6b_vae_sd15.py, p1_decodificador_sd15.py,
#                     a1_parches.py, a1b_parches_componente.py  (src/common los REEXPORTA: tienen que estar)
#   ~/metalsynth/qc/a5_manifiesto_train.csv   conjunto CONGELADO (R1-R3, decision 2026-09-21)
#   ~/metalsynth/data/a1b_cache/      .npz de A1b, uno por (componente, corte); se sube desde la PC
#   entorno conda e6b
# Salida: ~/metalsynth/data/a2/<etiqueta>/{curva.csv, entrenar_meta.json, ckpt.pt}
#
# OJO (KHIPU.md, lecciones): lanzar SIEMPRE desde el directorio del script, nunca desde ~;
# el tope de jobs ENVIADOS es 5, el sexto se rechaza.
#
# --- SLURM ---
#SBATCH --job-name=a2_entrenar
#SBATCH --partition=gpu
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=24:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

PASOS=${1:?ERROR: primer argumento = numero de pasos (200 para la prueba corta)}
shift

RAIZ=$HOME/metalsynth
DATA=$RAIZ/data
ETIQUETA="pasos${PASOS}_$(date +%Y%m%d_%H%M%S)"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate e6b || { echo "ERROR: no se activo el entorno e6b"; exit 1; }
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export PYTHONPATH="$RAIZ/src:$RAIZ/qc:$PYTHONPATH"
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch, nibabel, scipy; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())" \
    || { echo "ERROR: faltan dependencias en e6b (ver KHIPU.md)"; exit 1; }

[ -d "$DATA/a1b_cache" ] || { echo "ERROR: falta $DATA/a1b_cache (salida de a1b_parches_componente.py --cache)"; exit 1; }

cd "$RAIZ/src/renderizador" || { echo "ERROR: falta $RAIZ/src/renderizador"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)  pasos $PASOS  etiqueta $ETIQUETA"
python entrenar.py \
    --cache "$DATA/a1b_cache" \
    --particion "$RAIZ/qc/p1_particion.csv" \
    --manifiesto "$RAIZ/qc/a5_manifiesto_train.csv" \
    --out "$DATA/a2/$ETIQUETA" \
    --pasos "$PASOS" "$@"
rc=$?
echo "fin $(date -Is)  rc=$rc  etiqueta $ETIQUETA"
exit $rc
