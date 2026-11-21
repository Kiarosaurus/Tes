#!/bin/bash
# EVALUACION EN PRUEBA DE LA VARIANTE eta (POST-HOC, EXPLORATORIA): run04_mejor con --pasos 100 --eta 0.3 sobre los 13 de E-A2.
# Reglas: docs/01-decisiones.md 2026-11-21 (13). Misma etapa `final` de a15_cadena_pose.sbatch (13 de prueba, 5 semillas,
# --incluir-banda, NIfTI, --corrida-final); solo cambian el muestreo y la etiqueta. NO sustituye a E-A2.
# La variante (100:0.3) esta fijada de antemano; no se elige otra despues de ver resultados.
#
# USO (desde ~/metalsynth, rama exp/b-minima-angular, tras git pull):
#   sbatch --test-only -p all --gres=gpu:tesla:1 experiments/objetivo3/a15_final_eta.sbatch
#   sbatch -p all --gres=gpu:tesla:1 experiments/objetivo3/a15_final_eta.sbatch
# Si el job se corta, se relanza igual: los casos con `_s4_sintetica.nii.gz` ya existente se saltan.
# Salida: $DATA/obj3_pose/final/run04_mejor_p100_e0.3/   (misma convencion que final/run04_mejor)
#SBATCH --job-name=a15feta
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:tesla:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
PT="$DATA/a7/run04/mejor.pt"
DELTA=${DELTA:-0.03}
PASOS=${PASOS:-100}
ETA=${ETA:-0.3}
ETIQ=${ETIQ:-run04_mejor_p${PASOS}_e${ETA}}
SALIDA=${SALIDA:-$DATA/obj3_pose/final/$ETIQ}
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" || { echo "ERROR: sin cuda"; exit 1; }
for f in "$PT" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q "'--eta'" "$REPO/experiments/objetivo3/a15_cadena_completa.py" || { echo "ERROR: a15 sin --eta (git pull)"; exit 1; }
[ "${#TEST[@]}" -eq 13 ] || { echo "ERROR: casos_ea2_test.txt no tiene 13 casos"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  etiqueta $ETIQ  pasos $PASOS  eta $ETA  delta $DELTA  commit $(git -C "$REPO" rev-parse --short HEAD)"
A15="$REPO/experiments/objetivo3/a15_cadena_completa.py"
rc=0
for caso in "${TEST[@]}"; do
    if [ -f "$SALIDA/a15_${caso}_${ETIQ}_s4_sintetica.nii.gz" ]; then
        echo "=== $caso ya generado, se salta ==="; continue
    fi
    echo; echo "=== final $ETIQ $caso  $(date -Is) ==="
    python -u "$A15" --caso "$caso" --cortes 0 --dispositivo cuda --semillas 0 1 2 3 4 --pasos-cotejo-mm 1.0 \
        --data "$DATA/extracted" --ckpt "$PT" --etiquetas "$ETIQ" --delta "$DELTA" \
        --pasos "$PASOS" --eta "$ETA" --incluir-banda --particiones test --corrida-final \
        --out-dir "$SALIDA" || { echo "ERROR en $ETIQ $caso"; rc=1; }
done
n=$(ls "$SALIDA"/a15_*_"$ETIQ"_s4_sintetica.nii.gz 2>/dev/null | wc -l)
echo "fin $(date -Is)  rc=$rc  casos completos: $n/13"
[ "$n" -eq 13 ] || rc=1
exit $rc
