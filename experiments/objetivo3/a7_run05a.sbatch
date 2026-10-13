#!/bin/bash
# A7 run05a: version 2, opcion D (`experiments/objetivo3/v2_plan.md`; decision de la autora 2026-10-13).
#
# QUE ES: run04 + D-a (sobremuestreo de parches de componentes tamano tornillo, 500-4000 mm3) + D-b (peso de la
# perdida en el anillo de 2-10 mm alrededor de `M`, dentro de `G`). Es POSTERIOR y EXPLORATORIA: se decide despues de
# ver la prueba de la version 1 (#177). La version 1 se reporta completa; esta va al lado.
#
# UNICAS DIFERENCIAS con run04 (a7_run04.sbatch): las banderas `--componentes/--frac-tornillo` y
# `--anillo-mm/--peso-anillo`, y la salida en $DATA/a7/run05a. Mismo manifiesto (14 182 parches, 39 casos), misma
# validacion (896 / 3), misma semilla, lote 16, base 64, lado 256, lr 1e-4, 60 000 pasos, validacion cada 500.
#
# LOS DOS NUMEROS DE D SON OBLIGATORIOS Y SIN VALOR POR DEFECTO (`[POR FIJAR]` en v2_plan.md, los fija la autora
# ANTES de entrenar). El job aborta si no se pasan:
#   FRAC  fraccion objetivo de parches tamano tornillo por sorteo (D-a)
#   PESO  peso del anillo 2-10 mm dentro de G (D-b)
#
# USO (desde ~/metalsynth, tras `git pull`; la tabla v2_d_componentes_run04.csv tiene que estar commiteada):
#   sbatch --test-only --export=ALL,FRAC=0.5,PESO=3 experiments/objetivo3/a7_run05a.sbatch
#   sbatch --export=ALL,FRAC=0.5,PESO=3 experiments/objetivo3/a7_run05a.sbatch
# Prueba corta de humo (200 pasos, otra carpeta):
#   sbatch --time=00:30:00 --export=ALL,FRAC=0.5,PESO=3,PASOS=200,SALIDA=$HOME/metalsynth/data/a7/run05a_humo \
#          experiments/objetivo3/a7_run05a.sbatch
#
# SI EL JOB SE CORTA, se relanza EXACTAMENTE igual: `--reanudar` continua desde `ckpt.pt`.
# EN TRAMOS (cola llena o reservas, 2026-10-13): jobs cortos encadenados con --dependency=afterany, cada uno con
# --time corto y CADA_CKPT=1000 para perder poco al cortarse. `mejor.pt`/`mejor_pond.pt` conservan su minimo al
# reanudar. Si la corrida ya llego a 60 000 pasos, un tramo extra termina enseguida sin entrenar.
# Salida: $DATA/a7/run05a/{ckpt.pt, mejor.pt, mejor_pond.pt, curva.csv, entrenar_meta.json}
#SBATCH --job-name=a7run05a
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
SALIDA=${SALIDA:-$DATA/a7/run05a}
PASOS=${PASOS:-60000}
MAN=$REPO/experiments/objetivo3/a5_manifiesto_train_run04.csv
COMP=$REPO/experiments/objetivo3/v2_d_componentes_run04.csv
ANILLO="2 10"

[ -n "${FRAC:-}" ] || { echo "ERROR: falta FRAC (fraccion objetivo de tornillos, [POR FIJAR] en v2_plan.md)"; exit 1; }
[ -n "${PESO:-}" ] || { echo "ERROR: falta PESO (peso del anillo 2-10 mm, [POR FIJAR] en v2_plan.md)"; exit 1; }

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch, scipy; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())" \
    || { echo "ERROR: falta torch o scipy"; exit 1; }
[ -f "$MAN" ] || { echo "ERROR: falta $MAN (git pull)"; exit 1; }
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
    --reanudar
rc=$?
echo "fin $(date -Is)  rc=$rc"
echo "ultimas filas de la curva:"
tail -5 "$SALIDA/curva.csv" 2>/dev/null
exit $rc
