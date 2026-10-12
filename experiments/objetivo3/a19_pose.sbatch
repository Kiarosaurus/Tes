#!/bin/bash
# BRAZO FISICO (Peters / XCIST) CON LA POSE CORREGIDA (#173), en dos etapas seguidas, CPU:
#   1. val    - 0101/0102: test-retest A/B -> `r` de Delta, y cotejo del material frente a lo real (a21, local)
#   2. final  - 13 de test de E-A2 (`casos_ea2_test.txt`): Ti (primario) y Fe (sensibilidad), replicas A/B
# El CONTROL pose de `a19.geometria` aborta si el tornillo no cae en el corredor.
#
# Recursos como `obsoletos/objetivo3/a19_final.sbatch` (big-mem, 24 CPU, 30G; ~20-30 min por paciente). QoS a-tesis: suma de CPU/RAM
# compartida con los jobs de GPU (KHIPU.md nota 11).
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only experiments/objetivo3/a19_pose.sbatch
#   J3=$(sbatch --parsable experiments/objetivo3/a19_pose.sbatch); echo $J3
#   Repetir solo una etapa:  sbatch --export=ALL,ETAPAS="final" experiments/objetivo3/a19_pose.sbatch
# Salida: $DATA/obj3_pose/peters_{val,final}/
#SBATCH --job-name=a19pose
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=24
#SBATCH --mem=30G
#SBATCH --time=10:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
ETAPAS=${ETAPAS:-"val final"}
BASE=${BASE:-$DATA/obj3_pose}
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import gecatsim" || { echo "ERROR: falta gecatsim (pip install gecatsim==1.6.8)"; exit 1; }
grep -q "def pose_a_marco_crudo" "$REPO/experiments/objetivo3/a11_rasterizar_tornillo.py" \
    || { echo "ERROR: a11 sin la correccion de pose de #173 (git pull)"; exit 1; }
grep -q "ENMIENDA 2026-10-11 (run04)" "$REPO/experiments/objetivo3/diseno_A.md" \
    || { echo "ERROR: diseno_A.md sin la enmienda de run04 (git pull)"; exit 1; }

export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
echo "inicio $(date -Is)  nodo $(hostname)  etapas: $ETAPAS"
rc=0
for etapa in $ETAPAS; do
    echo; echo "##### etapa $etapa  $(date -Is) #####"
    TMP=${SLURM_TMPDIR:-/tmp}/a19pose_${SLURM_JOB_ID}_$etapa
    case $etapa in
        val)   ARGS=(--casos dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data) ;;
        final) ARGS=(--casos "${TEST[@]}" --corrida-final) ;;
        *) echo "ERROR: etapa desconocida $etapa"; exit 1 ;;
    esac
    python -u "$REPO/experiments/objetivo3/a19_peters_completo.py" "${ARGS[@]}" \
        --data "$DATA/extracted" --k 2 --trabajadores 12 --out-dir "$BASE/peters_$etapa" --tmp-dir "$TMP" \
        || { echo "ERROR en etapa $etapa"; rc=1; }
    rm -rf "$TMP"
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
