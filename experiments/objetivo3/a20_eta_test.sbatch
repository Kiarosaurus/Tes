#!/bin/bash
# a20 (evaluador comun de E-A2, definicion congelada = variante `base`) sobre la corrida en prueba de la variante eta.
# EXPLORATORIO y POSTERIOR (docs/01-decisiones.md 2026-11-21 (13)); no reemplaza a E-A2. Produce SOLO el CSV de a20;
# `a24_contrastes.py` se corre en local sobre ese CSV. Espejo de la etapa `test` de a20_v2.sbatch con RUNS = la variante eta.
#
# USO (desde ~/metalsynth, tras git pull y cuando a15_final_eta.sbatch haya terminado con 13/13):
#   sbatch --export=ALL experiments/objetivo3/a20_eta_test.sbatch
# Salida: $DATA/eta_prueba/a20_test_base.csv  (aborta si ya existe, salvo OVERWRITE=1), a20_val.csv y a20_delta_<etiqueta>.json
#SBATCH --job-name=a20eta
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
OUT=$DATA/eta_prueba
CSV=$OUT/a20_test_base.csv
A20="$REPO/experiments/objetivo3/a20_evaluador_ea2.py"
ETIQ=${ETIQ:-run04_mejor_p100_e0.3}
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
[ "${#TEST[@]}" -eq 13 ] || { echo "ERROR: casos_ea2_test.txt no tiene 13 casos"; exit 1; }
for caso in "${TEST[@]}"; do
    ls "$DATA/obj3_pose/final/$ETIQ/a15_${caso}_${ETIQ}_s4_sintetica.nii.gz" >/dev/null 2>&1 \
        || { echo "ERROR: falta la corrida final de $ETIQ ($caso)"; exit 1; }
done
mkdir -p "$OUT"
if [ -f "$CSV" ] && [ -z "${OVERWRITE:-}" ]; then echo "ERROR: $CSV ya existe (OVERWRITE=1 para rehacerlo)"; exit 1; fi
rm -f "$CSV"
echo "inicio $(date -Is)  etiqueta $ETIQ  commit $(git -C "$REPO" rev-parse --short HEAD)"
echo "AVISO: evaluacion EXPLORATORIA y POSTERIOR de una variante de muestreo: no reemplaza a E-A2"
rc=0
python -u "$A20" peters --npz "$DATA"/obj3_pose/peters_final/a19_*.npz --corrida-final --out "$CSV" || exit 1
python -u "$A20" copiapega --casos "${TEST[@]}" --hu 5371 --corrida-final --out "$CSV" || exit 1
python -u "$A20" parametrico --casos "${TEST[@]}" --hu 5371 --corrida-final --out "$CSV" || exit 1
for caso in "${TEST[@]}"; do
    python -u "$A20" difusor --caso "$caso" --dir "$DATA/obj3_pose/final/$ETIQ" --etiqueta "$ETIQ" \
        --corrida-final --out "$CSV" || { echo "ERROR $ETIQ $caso"; rc=1; }
done
# Delta de validacion de la variante (0101/0102, 5 semillas, cortes con M; salidas de a15_val_ckpt.sbatch en b_min/)
CSV_VAL=$OUT/a20_val.csv
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
rm -f "$CSV_VAL" "$OUT/a20_delta.json"
python -u "$A20" peters --npz "$DATA"/obj3_pose/peters_val/a19_*.npz --out "$CSV_VAL" || { echo "ERROR peters val"; rc=1; }
for caso in "${VAL[@]}"; do
    python -u "$A20" difusor --caso "$caso" --dir "$DATA/obj3_pose/b_min/$ETIQ" --etiqueta "$ETIQ" --out "$CSV_VAL" \
        || { echo "ERROR val $ETIQ $caso"; rc=1; }
done
python -u "$A20" delta --csv "$CSV_VAL" --etiqueta "$ETIQ" || { echo "ERROR delta"; rc=1; }
mv "$OUT/a20_delta.json" "$OUT/a20_delta_$ETIQ.json" 2>/dev/null
echo "fin $(date -Is)  rc=$rc"
exit $rc
