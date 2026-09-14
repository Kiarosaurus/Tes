#!/bin/bash
# E10: componentes conexas de las mascaras de TS (ts_componentes.py) en Khipu. Solo CPU: no gasta GPU.
# Insumo para fijar la fraccion de la regla de limpieza (decision 2026-09-14, #49 opcion e).
# Requiere: ~/metalsynth/qc/ts_componentes.py y la cohorte en ~/metalsynth/data/ts_total (358 .ok).
# Reanudable: relanzar continua donde quedo.
# Salida: ~/metalsynth/data/ts_componentes/{ts_componentes_resumen.csv, ts_componentes.csv,
#         ts_componentes_errores.csv}
#
# --- SLURM ---  big-mem = n006 (la cuenta ya funciono ahi con ts_qc_cohorte.sbatch)
#SBATCH --job-name=ts_componentes
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
python -c "import nibabel, numpy, scipy; print('dependencias ok')" \
    || { echo "ERROR: faltan dependencias; instalar en el nodo de acceso (ver KHIPU.md)"; exit 1; }
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)"
python ts_componentes.py --ts-dir "$DATA/ts_total" --out-dir "$DATA/ts_componentes"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
