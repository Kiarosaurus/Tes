#!/bin/bash
# Version 2: calibra el `delta` de `regla_suave` (lectura de HU, #152/#172) para el `mejor.pt` de run05a o run05b, en
# validacion, con `a16_calibrar_delta.py` (mismo criterio que con run04). Escribe $DATA/a16_v2/$RUN/a16_elegido.csv,
# que lee a15_cadena_v2.sbatch. Un job por corrida (run05b tiene 12 entradas y necesita el cache de T).
# `a16` corre en CPU (como con run04, en local): va a la particion de CPU, sin GPU.
#
# USO:  sbatch --export=ALL,RUN=run05a experiments/objetivo3/a16_v2.sbatch
#       sbatch --export=ALL,RUN=run05b experiments/objetivo3/a16_v2.sbatch
#SBATCH --job-name=a16v2
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=03:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
case "${RUN:-}" in
    run05a) EXTRA=() ;;
    run05b) EXTRA=(--cache-T "$DATA/a1b_cache_T") ;;
    *) echo "ERROR: falta RUN=run05a o RUN=run05b"; exit 1 ;;
esac
PT=$DATA/a7/$RUN/mejor.pt
OUT=$DATA/a16_v2/$RUN
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
[ -f "$PT" ] || { echo "ERROR: falta $PT"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)  $RUN  commit $(git -C "$REPO" rev-parse --short HEAD)"
python -u "$REPO/experiments/objetivo3/a16_calibrar_delta.py" --cache "$DATA/a1b_cache" \
    --ckpt "$PT" --etiquetas "${RUN}_mejor" --out-dir "$OUT" "${EXTRA[@]}"
rc=$?
echo "fin $(date -Is)  rc=$rc"
cat "$OUT/a16_elegido.csv" 2>/dev/null
exit $rc
