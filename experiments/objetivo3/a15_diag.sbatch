#!/bin/bash
# Diagnosticos en GPU de DEC 2026-10-15 con `run04_mejor` (delta 0.03, el de su corrida final). POSTERIORES.
#
#   MODO=nulo  amplitud nula del difusor (pto 18): los 13 de E-A2, `G` intacta y canal `M` a cero (`--sin-metal`),
#              --incluir-banda, 5 semillas; despues `a20 difusor` sobre esas salidas (CPU, mismo job).
#              Salida: $DATA/obj3_pose/nulo/run04_mejor_nulo/ y $DATA/obj3_pose/nulo/a20_nulo.csv
#   MODO=p95   mecanismo del p95 (pto 7): validacion 0101/0102 como la etapa `cotejo` (cortes con `M`, 5 semillas,
#              cascaras de 1 mm), guardando `u` crudo de todo `G` (`--guardar-u-g`). La decodificacion alternativa
#              (solo LW) y el control sobre imagenes reales se hacen en local.
#              Salida: $DATA/obj3_pose/diag_p95/run04_mejor/ (*_cotejo.csv, *_marcasG.npz)
#
# USO:  sbatch --export=ALL,MODO=nulo experiments/objetivo3/a15_diag.sbatch
#       sbatch --export=ALL,MODO=p95  experiments/objetivo3/a15_diag.sbatch
#SBATCH --job-name=a15diag
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
PT=$DATA/a7/run04/mejor.pt
A15="$REPO/experiments/objetivo3/a15_cadena_completa.py"
A20="$REPO/experiments/objetivo3/a20_evaluador_ea2.py"
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available()" || { echo "ERROR: sin cuda"; exit 1; }
[ -f "$PT" ] || { echo "ERROR: falta $PT"; exit 1; }
grep -q "guardar-u-g" "$A15" || { echo "ERROR: a15 sin las banderas de 2026-10-15 (git pull)"; exit 1; }
grep -q "def pose_a_marco_crudo" "$REPO/experiments/objetivo3/a11_rasterizar_tornillo.py" \
    || { echo "ERROR: a11 sin la correccion de pose de #173 (git pull)"; exit 1; }
COMUN=(--cortes 0 --dispositivo cuda --semillas 0 1 2 3 4 --data "$DATA/extracted" --ckpt "$PT" --delta 0.03)
echo "inicio $(date -Is)  nodo $(hostname)  modo ${MODO:-}  commit $(git -C "$REPO" rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
rc=0
case "${MODO:-}" in
    nulo)
        SAL=$DATA/obj3_pose/nulo/run04_mejor_nulo
        for caso in "${TEST[@]}"; do
            echo; echo "=== nulo $caso  $(date -Is) ==="
            python -u "$A15" --caso "$caso" "${COMUN[@]}" --etiquetas run04_mejor_nulo --sin-metal \
                --incluir-banda --particiones test --corrida-final --pasos-cotejo-mm 1.0 --out-dir "$SAL" \
                || { echo "ERROR a15 $caso"; rc=1; }
        done
        CSV=$DATA/obj3_pose/nulo/a20_nulo.csv
        rm -f "$CSV"
        for caso in "${TEST[@]}"; do
            python -u "$A20" difusor --caso "$caso" --dir "$SAL" --etiqueta run04_mejor_nulo --corrida-final \
                --out "$CSV" || { echo "ERROR a20 $caso"; rc=1; }
        done ;;
    p95)
        SAL=$DATA/obj3_pose/diag_p95/run04_mejor
        for caso in "${VAL[@]}"; do
            echo; echo "=== p95 $caso  $(date -Is) ==="
            python -u "$A15" --caso "$caso" "${COMUN[@]}" --etiquetas run04_mejor --sin-nifti --guardar-u-g \
                --pasos-cotejo-mm 1.0 --out-dir "$SAL" || { echo "ERROR a15 $caso"; rc=1; }
        done ;;
    *) echo "ERROR: falta MODO=nulo o MODO=p95"; exit 1 ;;
esac
echo "fin $(date -Is)  rc=$rc"
exit $rc
