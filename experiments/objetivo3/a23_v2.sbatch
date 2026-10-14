#!/bin/bash
# E-A1 de la version 2 (EXPLORATORIO, #182; declarado en v2_plan.md): reconstruccion del implante real en los pacientes
# de prueba con metal, igual que `a23_final_run04.sbatch` (componentes >= 500 mm3, hasta 24 cortes, 5 semillas), con el
# `mejor.pt` de run05a o run05b y su `delta` de `a16_v2`. `a23` lee del checkpoint si lleva el canal T (run05b) y calcula
# T al vuelo para los parches de prueba (en <out>/cache_T).
#
# USO:  sbatch --export=ALL,RUN=run05a experiments/objetivo3/a23_v2.sbatch
# Salida: $DATA/a23_v2/<RUN>/ (a23_parches.csv, a23_pacientes.csv, cache de parches de prueba)
#SBATCH --job-name=a23v2
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=shard:a100_3g.20gb:5
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=08:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
case "${RUN:-}" in
    run05a|run05b) ;;
    *) echo "ERROR: falta RUN=run05a o RUN=run05b"; exit 1 ;;
esac
PT=$DATA/a7/$RUN/mejor.pt
if [ -z "${DELTA:-}" ]; then
    F16=$DATA/a16_v2/$RUN/a16_elegido.csv
    [ -f "$F16" ] || { echo "ERROR: falta $F16"; exit 1; }
    DELTA=$(awk -F, -v e="${RUN}_mejor" '$1==e {print $2}' "$F16")
    [ -n "$DELTA" ] || { echo "ERROR: $F16 sin delta para ${RUN}_mejor"; exit 1; }
fi
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available()" || { echo "ERROR: sin cuda"; exit 1; }
[ -f "$PT" ] || { echo "ERROR: falta $PT"; exit 1; }
grep -q "Analisis exploratorio en prueba (DECLARADO" "$REPO/experiments/objetivo3/v2_plan.md" \
    || { echo "ERROR: v2_plan.md sin la declaracion del analisis exploratorio (git pull)"; exit 1; }
for viejo in metal_0053 metal_0003; do
    grep -q "dataset7_CLINIC_${viejo}_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
        && { echo "ERROR: p1_particion.csv vieja (aun tiene $viejo)"; exit 1; }
done
echo "inicio $(date -Is)  nodo $(hostname)  $RUN  delta $DELTA  commit $(git -C "$REPO" rev-parse --short HEAD)"
echo "AVISO: E-A1 EXPLORATORIO y POSTERIOR (v2_plan.md, #182): no reemplaza a run04"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
python -u "$REPO/experiments/objetivo3/a23_ea1.py" --particiones test --corrida-final --dispositivo cuda \
    --data "$DATA/extracted" --ckpt "$PT" --delta "$DELTA" --out-dir "$DATA/a23_v2/$RUN"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
