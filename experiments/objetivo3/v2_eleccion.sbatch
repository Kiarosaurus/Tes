#!/bin/bash
# Version 2: aplica la regla de eleccion (v2_plan.md) a run04, run05a y run05b, en CPU, cuando terminan las etapas
# `cotejo` y `delta` de a15_cadena_v2.sbatch de las dos corridas (y con las de run04, ya hechas en obj3_pose).
#   1. d2_perfil_sintetico.py sobre $DATA/obj3_pose/delta/{run04_mejor,run05a_mejor,run05b_mejor}
#   2. a17_cotejo.py sobre los cotejos de los tres (reportado, no decide)
#   3. v2_eleccion.py -> $DATA/v2_eleccion/v2_eleccion.md
# USO:  sbatch --dependency=afterok:$CA:$CB experiments/objetivo3/v2_eleccion.sbatch
#SBATCH --job-name=v2elige
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
OUT=$DATA/v2_eleccion
PUNTOS=(run04_mejor run05a_mejor run05b_mejor)
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
for p in "${PUNTOS[@]}"; do
    for c in dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data; do
        ls "$DATA/obj3_pose/delta/$p/a15_${c}_${p}_s4_sintetica.nii.gz" >/dev/null 2>&1 \
            || { echo "ERROR: falta la etapa delta de $p ($c)"; exit 1; }
    done
done
mkdir -p "$OUT/cotejo"
for p in "${PUNTOS[@]}"; do
    # a17 busca `a15_*_cotejo.csv` en una sola carpeta y agrupa por la columna `etiqueta`
    for f in "$DATA/obj3_pose/cotejo/$p"/a15_*_cotejo.csv; do ln -sf "$f" "$OUT/cotejo/a15_${p}__$(basename "${f#*/a15_}")"; done
done
echo "inicio $(date -Is)  commit $(git -C "$REPO" rev-parse --short HEAD)"
cd "$REPO/experiments/objetivo3" || exit 1
python -u d2_perfil_sintetico.py --base "$DATA/obj3_pose/delta" --puntos "${PUNTOS[@]}" --out-dir "$OUT/d2" \
    || { echo "ERROR en d2"; exit 1; }
python -u a17_cotejo.py --dir-sintetico "$OUT/cotejo" --data "$DATA/extracted" --out-dir "$OUT/a17" --paso-mm 1 \
    || echo "AVISO: a17 fallo (no decide; se sigue)"
A17=$OUT/a17/a17_cotejo.md; [ -f "$A17" ] || A17=
python -u v2_eleccion.py --d2 "$OUT/d2/d2_perfil.csv" ${A17:+--a17 "$A17"} --out "$OUT/v2_eleccion.md"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
