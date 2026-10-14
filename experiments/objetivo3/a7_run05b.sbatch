#!/bin/bash
# A7 run05b: version 2, D + B (`experiments/objetivo3/v2_plan.md`). Identico a run05a (mismo manifiesto, misma
# validacion, mismos hiperparametros, FRAC=0.5 y PESO=3, misma GPU `a100_3g`) MAS el canal T (plantilla analitica de
# endurecimiento del haz, `src/renderizador/plantilla.py`), que paso la compuerta del piloto el 2026-10-13
# (`experiments/objetivo3/b_piloto/b_resumen.md`). Modelo con 12 entradas en vez de 11.
#
# REQUIERE $DATA/a1b_cache_T completo (a7_cache_T.sbatch): el entrenamiento aborta si falta algun T.
#
# USO (desde ~/metalsynth, tras `git pull`), en tramos de 3 h como run05a:
#   JT=$(sbatch --parsable experiments/objetivo3/a7_cache_T.sbatch)
#   E="--export=ALL,FRAC=0.5,PESO=3,CADA_CKPT=1000"; F=experiments/objetivo3/a7_run05b.sbatch
#   G="-p all --gres=shard:a100_3g.20gb:8 --time=03:00:00"
#   J1=$(sbatch --parsable $G --dependency=afterok:$JT $E $F)
#   J2=$(sbatch --parsable $G --dependency=afterany:$J1 $E $F)   ... (J3, J4 igual)
# Salida: $DATA/a7/run05b/{ckpt.pt, mejor.pt, mejor_pond.pt, curva.csv, entrenar_meta.json}
#SBATCH --job-name=a7run05b
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=shard:a100_3g.20gb:8
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=${SALIDA:-$DATA/a7/run05b}
PASOS=${PASOS:-60000}
MAN=$REPO/experiments/objetivo3/a5_manifiesto_train_run04.csv
COMP=$REPO/experiments/objetivo3/v2_d_componentes_run04.csv
CACHE_T=${CACHE_T:-$DATA/a1b_cache_T}
ANILLO="2 10"

[ -n "${FRAC:-}" ] || { echo "ERROR: falta FRAC (fraccion objetivo de tornillos, [POR FIJAR] en v2_plan.md)"; exit 1; }
[ -n "${PESO:-}" ] || { echo "ERROR: falta PESO (peso del anillo 2-10 mm, [POR FIJAR] en v2_plan.md)"; exit 1; }

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch, scipy; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())" \
    || { echo "ERROR: falta torch o scipy"; exit 1; }
[ -f "$MAN" ] || { echo "ERROR: falta $MAN (git pull)"; exit 1; }
[ -f "$CACHE_T/escala.json" ] || { echo "ERROR: falta $CACHE_T/escala.json (correr a7_cache_T.sbatch)"; exit 1; }
[ -f "$COMP" ] || { echo "ERROR: falta $COMP (correr v2_d_componentes.py en local, commit y git pull)"; exit 1; }
n=$(($(wc -l < "$MAN") - 1))
[ "$n" -eq 14182 ] || { echo "ERROR: el manifiesto tiene $n parches, se esperaban 14182"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  parches $n  FRAC=$FRAC  PESO=$PESO  anillo $ANILLO mm"
echo "commit $(git -C "$REPO" rev-parse --short HEAD)"
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
    --lr 1e-4 \
    --cada 500 \
    --lotes-val 16 \
    --cada-ckpt "${CADA_CKPT:-5000}" \
    --trabajadores "$SLURM_CPUS_PER_TASK" \
    --componentes "$COMP" \
    --frac-tornillo "$FRAC" \
    --anillo-mm $ANILLO \
    --peso-anillo "$PESO" \
    --cache-T "$CACHE_T" \
    --reanudar
rc=$?
echo "fin $(date -Is)  rc=$rc"
echo "ultimas filas de la curva:"
tail -5 "$SALIDA/curva.csv" 2>/dev/null
exit $rc
