#!/bin/bash
# Version 2, EXPLORATORIO (#182; declarado en v2_plan.md): evaluacion E-A2 de run05a y run05b en Khipu, en CPU, con el
# mismo procedimiento que run04 (resultados_validacion_pose.md §3 y resultados_prueba_v1.md), para no bajar los NIfTI.
#   1. validacion: a20 peters (peters_val) + a20 difusor (etapa delta, 0101/0102, 5 semillas) -> Delta = max(s, r)
#   2. prueba: a20 peters (peters_final) + copia y pegado (5371 HU, a22 run04) + a20 difusor (final, 13 x 5 semillas)
#   3. a24 para cada run05 con su propio Delta (TOST frente a Peters Ti, sensibilidades, Wilcoxon frente a copia y pegado)
# Peters y la copia y pegado se recalculan aqui (deterministas: mismos valores que con run04).
#
# USO (cuando terminen a15_cadena_v2 ETAPAS=final de los dos):
#   sbatch --dependency=afterok:<FA>:<FB> experiments/objetivo3/a20_v2.sbatch
# Salida: $DATA/v2_prueba/{a20_val.csv, a20_delta_<run>_mejor.json, a20_test.csv, a24/<run>_mejor/}
#SBATCH --job-name=a20v2
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=48G
#SBATCH --time=08:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
OUT=$DATA/v2_prueba
A20="$REPO/experiments/objetivo3/a20_evaluador_ea2.py"
A24="$REPO/experiments/objetivo3/a24_contrastes.py"
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"
RUNS=(run05a_mejor run05b_mejor)
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
grep -q "Analisis exploratorio en prueba (DECLARADO" "$REPO/experiments/objetivo3/v2_plan.md" \
    || { echo "ERROR: v2_plan.md sin la declaracion del analisis exploratorio (git pull)"; exit 1; }
for et in "${RUNS[@]}"; do
    for caso in "${TEST[@]}"; do
        ls "$DATA/obj3_pose/final/$et/a15_${caso}_${et}_s4_sintetica.nii.gz" >/dev/null 2>&1 \
            || { echo "ERROR: falta la corrida final de $et ($caso)"; exit 1; }
    done
done
mkdir -p "$OUT"
rm -f "$OUT/a20_val.csv" "$OUT/a20_test.csv"
echo "inicio $(date -Is)  commit $(git -C "$REPO" rev-parse --short HEAD)"
echo "AVISO: evaluacion EXPLORATORIA y POSTERIOR de la version 2 (v2_plan.md, #182): no reemplaza a run04"

echo "##### 1. validacion y Delta #####"
python -u "$A20" peters --npz "$DATA"/obj3_pose/peters_val/a19_*.npz --out "$OUT/a20_val.csv" || exit 1
for et in "${RUNS[@]}"; do
    for caso in "${VAL[@]}"; do
        python -u "$A20" difusor --caso "$caso" --dir "$DATA/obj3_pose/delta/$et" --etiqueta "$et" \
            --out "$OUT/a20_val.csv" || exit 1
    done
    python -u "$A20" delta --csv "$OUT/a20_val.csv" --etiqueta "$et" || exit 1
    mv "$OUT/a20_delta.json" "$OUT/a20_delta_$et.json"
done

echo "##### 2. prueba #####"
python -u "$A20" peters --npz "$DATA"/obj3_pose/peters_final/a19_*.npz --corrida-final --out "$OUT/a20_test.csv" || exit 1
python -u "$A20" copiapega --casos "${TEST[@]}" --hu 5371 --corrida-final --out "$OUT/a20_test.csv" || exit 1
for et in "${RUNS[@]}"; do
    for caso in "${TEST[@]}"; do
        python -u "$A20" difusor --caso "$caso" --dir "$DATA/obj3_pose/final/$et" --etiqueta "$et" --corrida-final \
            --out "$OUT/a20_test.csv" || exit 1
    done
done

echo "##### 3. a24 #####"
rc=0
for et in "${RUNS[@]}"; do
    python -u "$A24" --csv "$OUT/a20_test.csv" --etiqueta "$et" --delta-json "$OUT/a20_delta_$et.json" \
        --out-dir "$OUT/a24/$et" || rc=1
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
