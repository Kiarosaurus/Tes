#!/bin/bash
# QC de TotalSegmentator sobre la cohorte (ts_qc.py) en Khipu. Solo CPU: no gasta GPU.
# Lanzarlo DESPUES de ts_cohorte.sbatch:  sbatch --dependency=afterany:<ID_TS> ts_qc_cohorte.sbatch
# Requiere en ~/metalsynth/qc/ (ver KHIPU.md, paso 1): ts_qc.py, ts_piloto_qc.py, r1_landmarks.py,
#   e9b_densidad_s1.py, r1_landmarks.csv, e9b_densidad_s1.csv, e8_componentes.csv.
# Reanudable: relanzar continua donde quedo; los casos que TS aun no termino se saltan sin marcarse.
# Salida: ~/metalsynth/data/ts_total_qc/{ts_qc.csv, ts_qc_esferas.csv, ts_qc_tornillos.csv,
#         ts_qc_errores.csv, laminas/*.png}
#
# --- SLURM ---  big-mem = n006 (la cuenta ya funciono ahi)
#SBATCH --job-name=ts_qc
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=24:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno totalseg"; exit 1; }
python -c "import nibabel, numpy, pandas, scipy, matplotlib; print('dependencias ok')" \
    || { echo "ERROR: faltan dependencias; instalar en el nodo de acceso (ver KHIPU.md)"; exit 1; }
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)"
python ts_qc.py --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" --refs-dir . --out-dir "$DATA/ts_total_qc"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
