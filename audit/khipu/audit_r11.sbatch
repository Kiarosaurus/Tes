#!/bin/bash
# AUDITORIA R-11 (C): W1 con sigma x0.5 / x1 (control, debe reproducir e13_sap.md) / x2. SOLO CPU, ~20 min por factor.
# Escribe en ~/audit_khipu/r11/ (symlinks a las entradas de ~/metalsynth/qc); NO toca ~/metalsynth.
# USO: sbatch --test-only ~/audit_khipu/audit_r11.sbatch   y luego   sbatch ~/audit_khipu/audit_r11.sbatch
#SBATCH --job-name=auditr11
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=%x_%j.log
set -o pipefail
DATA=$HOME/metalsynth/data; QC=$HOME/metalsynth/qc; AUD=${AUD:-$HOME/audit_khipu}; W=$AUD/r11
mkdir -p "$W"
for f in e9ts_corredor.csv r1_landmarks.csv; do [ -f "$QC/$f" ] || { echo "ERROR: falta $QC/$f"; exit 1; }; ln -sf "$QC/$f" "$W/$f"; done
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
echo "inicio $(date -Is) nodo $(hostname) commit $(git -C $HOME/metalsynth rev-parse --short HEAD)"
rc=0
for fac in 4.0 2.0 1.0; do
    echo "=== FACTOR_SIGMA=$fac $(date -Is) ==="
    FACTOR_SIGMA=$fac python -u "$AUD/audit_r11_sigma.py" --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" \
        --refs-dir "$W" --out-sufijo "_fs$fac" || { echo "ERROR fs$fac"; rc=1; }
done
echo "fin $(date -Is) rc=$rc"; exit $rc
