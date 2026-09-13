#!/bin/bash
# TotalSegmentator sobre TODA la cohorte en Khipu (#48, #49, #50). Sigue al piloto (ts_piloto.sbatch).
#
# Cada volumen de ts_input (179 = 178 originales + union 0059u0071) con los dos recortes de #49,
# porque la autora aun no elige: robust3mm (--robust_crop) y default6mm.
# Mismo --task y --roi_subset que el piloto A PROPOSITO: el recorte depende de las clases pedidas y
# el piloto mostro que el recorte cambia la mascara (#49). Cambiar las clases rompe la comparacion.
#
# Reanudable: una corrida con .ok se salta; una sin .ok se borra y se repite. Si se acaba el tiempo,
# relanzar el mismo script. Un volumen que falle NO detiene el job: queda en _procedencia/ts_tiempos.csv.
# Al final compara las mascaras de los 2 casos del piloto con las de esta corrida (repetibilidad, #49).
#
# Salida: ~/metalsynth/data/ts_total/<caso>/<modo>/{sacrum,vertebrae_S1,hip_left,hip_right}.nii.gz + .ok
#         ~/metalsynth/data/ts_total/_procedencia/ (entorno, pip freeze, pesos, sha256, tiempos, repetibilidad)
# Estimado con el piloto: 59-76 s por corrida en MIG 3g.20gb -> 358 corridas ~ 6-8 h (sin medir en cohorte).
#
# --- SLURM ---  Antes de lanzar: sbatch --test-only ts_cohorte.sbatch. Si no hay MIG libre, ver KHIPU.md.
#SBATCH --job-name=ts_cohorte
#SBATCH --partition=gpu
#SBATCH --gres=shard:a100_3g.20gb:1
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=24:00:00
#SBATCH --output=%x_%j.log

set -o pipefail   # sin -e: un volumen que falle no debe tumbar el job

ROI=(sacrum vertebrae_S1 hip_left hip_right)
MODOS=(robust3mm default6mm)
DATA=$HOME/metalsynth/data
IN_DIR=$DATA/ts_input
OUT_DIR=$DATA/ts_total
PROC=$OUT_DIR/_procedencia
export TOTALSEG_HOME_DIR=$HOME/metalsynth/totalseg_home

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno totalseg"; exit 1; }

mkdir -p "$PROC"
{
    echo "job $SLURM_JOB_ID  nodo $(hostname)  inicio $(date -Is)"
    pip show TotalSegmentator | grep -E "^(Name|Version):"   # no usar head: con pipefail, SIGPIPE mata el job
    python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())"
    nvidia-smi --query-gpu=name,memory.total --format=csv
    echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"
} | tee "$PROC/entorno_${SLURM_JOB_ID}.txt"
python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)" \
    || { echo "ERROR: sin CUDA en el nodo; aborto para no caer a CPU en silencio"; exit 1; }
pip freeze > "$PROC/pip_freeze_${SLURM_JOB_ID}.txt"
find "$TOTALSEG_HOME_DIR" -maxdepth 3 -type d > "$PROC/pesos_${SLURM_JOB_ID}.txt"
cp -f "$DATA/sha256_check.txt" "$PROC/" 2>/dev/null || echo "AVISO: no se encontro $DATA/sha256_check.txt"

TIEMPOS=$PROC/ts_tiempos.csv
[ -f "$TIEMPOS" ] || echo "job,caso,modo,estado,segundos,n_mascaras,fin" > "$TIEMPOS"

ARCHIVOS=("$IN_DIR"/*.nii.gz)
echo "volumenes en $IN_DIR: ${#ARCHIVOS[@]} (esperado 179)"

hechas=0; fallos=0; saltadas=0
for f in "${ARCHIVOS[@]}"; do
    caso=$(basename "$f" .nii.gz)
    for modo in "${MODOS[@]}"; do
        out="$OUT_DIR/$caso/$modo"
        if [ -f "$out/.ok" ]; then saltadas=$((saltadas + 1)); continue; fi
        rm -rf "$out"; mkdir -p "$out"
        extra=()
        [ "$modo" = robust3mm ] && extra=(--robust_crop)
        echo "== $(date -Is) $caso / $modo =="
        t0=$(date +%s)
        TotalSegmentator -i "$f" -o "$out" --task total --roi_subset "${ROI[@]}" "${extra[@]}" \
            --device gpu --nr_thr_resamp "$SLURM_CPUS_PER_TASK" --nr_thr_saving 2
        rc=$?
        seg=$(( $(date +%s) - t0 ))
        n=$(find "$out" -maxdepth 1 -name "*.nii.gz" | wc -l)
        if [ "$rc" -eq 0 ] && [ "$n" -eq "${#ROI[@]}" ]; then
            touch "$out/.ok"; estado=ok; hechas=$((hechas + 1))
        else
            estado="fallo_rc${rc}"; fallos=$((fallos + 1))
        fi
        echo "$SLURM_JOB_ID,$caso,$modo,$estado,$seg,$n,$(date -Is)" >> "$TIEMPOS"
        echo "   -> $estado  ${seg} s  mascaras=$n"
    done
done
echo "== resumen: nuevas ok=$hechas  fallos=$fallos  ya hechas=$saltadas  fin $(date -Is)"

# Repetibilidad (#49): mismo modelo, recorte, clases y tipo de GPU que el piloto -> ¿mascaras identicas?
python - "$DATA/ts_piloto" "$OUT_DIR" <<'EOF' | tee "$PROC/repetibilidad_piloto_${SLURM_JOB_ID}.txt"
import sys
from pathlib import Path

import nibabel as nib
import numpy as np

piloto, total = Path(sys.argv[1]), Path(sys.argv[2])
if not piloto.is_dir():
    print('sin carpeta de piloto: no se compara')
    sys.exit(0)
print('caso modo estructura voxeles_distintos dice')
for d in sorted(p for p in piloto.iterdir() if p.is_dir()):
    for modo in ('robust3mm', 'default6mm'):
        for est in ('sacrum', 'vertebrae_S1', 'hip_left', 'hip_right'):
            a, b = piloto / d.name / modo / f'{est}.nii.gz', total / d.name / modo / f'{est}.nii.gz'
            if not (a.exists() and b.exists()):
                print(d.name, modo, est, 'falta')
                continue
            x = np.asanyarray(nib.load(a).dataobj) > 0
            y = np.asanyarray(nib.load(b).dataobj) > 0
            s = int(x.sum() + y.sum())
            print(d.name, modo, est, int((x ^ y).sum()), round(2 * int((x & y).sum()) / s, 5) if s else 'nan')
EOF

[ "$fallos" -eq 0 ] || exit 1
