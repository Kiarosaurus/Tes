#!/bin/bash
# A7: entrenamiento del renderizador del Diseno A, con validacion y checkpoints reanudables.
#
# QUE CAMBIA respecto del piloto A2 (job 52074, 200 pasos para medir coste, #89):
#   - **Bucle de validacion conectado**: `a5_manifiesto_val.csv` (896 parches, 3 casos, #105) se mide
#     cada `--cada` pasos sobre `--lotes-val` lotes FIJOS. Sin esto no se ve si converge ni se puede
#     medir el margen `Delta` de D4.
#   - **Checkpoint reanudable cada `--cada-ckpt` pasos**, con modelo, optimizador y paso. La cola de
#     Khipu corta a las 24 h: sin esto, un corte pierde la corrida entera.
#   - `curva.csv` anade `perdida_val` y `s_tramo`. `s_por_paso` se conserva por comparabilidad con el
#     piloto, pero es el promedio ACUMULADO; el ritmo real del ultimo tramo es `s_tramo` (#114).
#
# SI EL JOB SE CORTA, se relanza EXACTAMENTE igual anadiendo `--reanudar`: continua desde `ckpt.pt`
# en el mismo `--out`, sin reiniciar el optimizador y sin duplicar la cabecera de `curva.csv`.
#
# SIN `--preinscrito` A PROPOSITO: `docs/00-tesis.md:72` dice que lo unico que falta para congelar
# `diseno_A.md` es medir `Delta`, y `Delta` sale de ESTA corrida. Exigir la preinscripcion aqui seria
# circular. La corrida preinscrita viene despues, con el diseno ya congelado.
#
# Requiere en ~/metalsynth/: `src/renderizador/`, `src/common/`, la cache de A1b, los dos manifiestos
# y `experiments/objetivo1/p1_particion.csv`. ADEMAS, porque `src/common/ventanas.py` REEXPORTA en vez
# de duplicar la implementacion congelada del Objetivo 1, hacen falta en
# `~/metalsynth/experiments/objetivo1/`: `e6c_techo_lw.py` y `e6b_vae_sd15.py`. Sin ellos el job muere
# en el import con `ModuleNotFoundError: No module named 'e6c_techo_lw'` (job 54366, 2026-10-04).
# Salida: $DATA/a7/<nombre>/{ckpt.pt, curva.csv, entrenar_meta.json}
#SBATCH --job-name=a7entr
#SBATCH --partition=gpu
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=08:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=$DATA/a7/run01

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())" \
    || { echo "ERROR: falta torch"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

# `--reanudar` es seguro siempre: si no hay ckpt previo, arranca de cero. Asi el mismo script sirve
# para la primera corrida y para las continuaciones tras un corte de 24 h.
python -u "$REPO/src/renderizador/entrenar.py" \
    --cache "$DATA/a1b_cache" \
    --particion "$REPO/experiments/objetivo1/p1_particion.csv" \
    --manifiesto "$REPO/experiments/objetivo3/a5_manifiesto_train.csv" \
    --manifiesto-val "$REPO/experiments/objetivo3/a5_manifiesto_val.csv" \
    --out "$SALIDA" \
    --pasos 200000 \
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
