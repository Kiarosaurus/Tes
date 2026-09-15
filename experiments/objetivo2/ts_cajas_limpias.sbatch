#!/bin/bash
# E10b: cajas de las mascaras de TS antes y despues de la limpieza por fraccion (ts_cajas_limpias.py).
# Comprueba que F = 0.001 (decision 2026-09-14 (3)) elimina los 10 desplazamientos de caja de #49.
# Solo CPU: no gasta GPU. Control incluido: con F = 0 debe reproducir ts_qc.csv.
# Requiere: ~/metalsynth/qc/ts_cajas_limpias.py, la cohorte en ~/metalsynth/data/ts_total (358 .ok)
#           y ~/metalsynth/data/ts_total_qc/ts_qc.csv.
# Reanudable: relanzar continua donde quedo.
# Salida: ~/metalsynth/data/ts_cajas_limpias/{ts_cajas_limpias.csv, ts_cajas_limpias_control.csv,
#         ts_cajas_limpias_errores.csv}
#
# --- SLURM ---  big-mem = n006 (misma cola que E10)
#SBATCH --job-name=ts_cajas_limpias
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=06:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno totalseg"; exit 1; }
python -c "import nibabel, numpy, scipy, pandas; print('dependencias ok')" \
    || { echo "ERROR: faltan dependencias; instalar en el nodo de acceso (ver KHIPU.md)"; exit 1; }
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)"
python ts_cajas_limpias.py --ts-dir "$DATA/ts_total" --out-dir "$DATA/ts_cajas_limpias" \
    --ts-qc "$DATA/ts_total_qc/ts_qc.csv"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
