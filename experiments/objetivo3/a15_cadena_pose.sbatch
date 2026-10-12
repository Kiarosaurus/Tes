#!/bin/bash
# OBJETIVO 3 CON LA POSE CORREGIDA (#173): difusor, un punto de control por job, en tres etapas seguidas.
#   1. cotejo  - 0101/0102 (validacion), cortes con `M`, 5 semillas, cascaras de 1 mm, sin NIfTI  (eleccion, #169)
#   2. delta   - 0101/0102 (validacion), `--incluir-banda`, 5 semillas, NIfTI                     (`s` de Delta)
#   3. final   - 13 de test de E-A2 (`casos_ea2_test.txt`), `--incluir-banda`, 5 semillas, NIfTI  (E-A2)
# Cada punto de control se lee con su limite calibrado (#172 (A)): CKPT=mejor -> DELTA=0.03, CKPT=60k -> DELTA=0.05.
# La pose del Obj 2 se convierte al marco del array (`a11.pose_a_marco_crudo`) y el CONTROL pose aborta si el tornillo
# no cae en el corredor.
#
# GPU: los DOS jobs (mejor y 60k) deben pedir el MISMO --gres (#151): el cotejo compara los dos, y `s` describe la
# corrida final del mismo job. Lo que se pase con -p/--gres/--time al enviar manda sobre los #SBATCH de abajo.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only -p all --gres=shard:a100_3g.20gb:5 --export=ALL,CKPT=mejor experiments/objetivo3/a15_cadena_pose.sbatch
#   J1=$(sbatch --parsable -p all --gres=shard:a100_3g.20gb:5 --export=ALL,CKPT=mejor experiments/objetivo3/a15_cadena_pose.sbatch)
#   J2=$(sbatch --parsable -p all --gres=shard:a100_3g.20gb:5 --export=ALL,CKPT=60k   experiments/objetivo3/a15_cadena_pose.sbatch)
#   Repetir solo una etapa:  --export=ALL,CKPT=mejor,ETAPAS="final"
# Salida: $DATA/obj3_pose/{cotejo,delta,final}/run04_<CKPT>/
#SBATCH --job-name=a15pose
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=shard:a100_3g.20gb:5
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=07:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
case "${CKPT:-}" in
    mejor) PT="$DATA/a7/run04/mejor.pt"; DEF_DELTA=0.03 ;;
    60k)   PT="$DATA/a7/run04/ckpt.pt";  DEF_DELTA=0.05 ;;
    *) echo "ERROR: falta CKPT=mejor o CKPT=60k (sbatch --export=ALL,CKPT=...)"; exit 1 ;;
esac
DELTA=${DELTA:-$DEF_DELTA}
ETIQ=run04_$CKPT
ETAPAS=${ETAPAS:-"cotejo delta final"}
BASE=${BASE:-$DATA/obj3_pose}
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$PT" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q "def pose_a_marco_crudo" "$REPO/experiments/objetivo3/a11_rasterizar_tornillo.py" \
    || { echo "ERROR: a11 sin la correccion de pose de #173 (git pull)"; exit 1; }
grep -q "ENMIENDA 2026-10-11 (run04)" "$REPO/experiments/objetivo3/diseno_A.md" \
    || { echo "ERROR: diseno_A.md sin la enmienda de run04 (git pull)"; exit 1; }
for viejo in metal_0053 metal_0003; do
    grep -q "dataset7_CLINIC_${viejo}_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
        && { echo "ERROR: p1_particion.csv vieja (aun tiene $viejo; #156/#166)"; exit 1; }
done

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  ckpt $ETIQ  delta $DELTA  etapas: $ETAPAS"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
A15="$REPO/experiments/objetivo3/a15_cadena_completa.py"
COMUN=(--cortes 0 --dispositivo cuda --semillas 0 1 2 3 4 --pasos-cotejo-mm 1.0 --data "$DATA/extracted"
       --ckpt "$PT" --etiquetas "$ETIQ" --delta "$DELTA")
rc=0
for etapa in $ETAPAS; do
    echo; echo "##### etapa $etapa  $(date -Is) #####"
    SALIDA=$BASE/$etapa/$ETIQ
    case $etapa in
        cotejo) CASOS=("${VAL[@]}");  EXTRA=(--sin-nifti) ;;
        delta)  CASOS=("${VAL[@]}");  EXTRA=(--incluir-banda) ;;
        final)  CASOS=("${TEST[@]}"); EXTRA=(--incluir-banda --particiones test --corrida-final) ;;
        *) echo "ERROR: etapa desconocida $etapa"; exit 1 ;;
    esac
    for caso in "${CASOS[@]}"; do
        echo; echo "=== $etapa $caso  $(date -Is) ==="
        python -u "$A15" --caso "$caso" "${COMUN[@]}" "${EXTRA[@]}" --out-dir "$SALIDA" \
            || { echo "ERROR en $etapa $caso"; rc=1; }
    done
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
