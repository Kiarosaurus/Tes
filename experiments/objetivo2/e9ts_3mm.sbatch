#!/bin/bash
# E9-TS con laminas del recorte de 3 mm (preferencia de la autora, 2026-09-14; cambio de principal PENDIENTE).
# Las cifras con robust3mm ya estan en data/e9ts (corrida 51505): esta corrida NO cambia ninguna cifra.
# Hace tres cosas:
#   1. repite E9-TS en data/e9ts_3mm con --modo-laminas robust3mm (laminas de QC con 3 mm);
#   2. control de repetibilidad: su CSV debe ser IDENTICO al de data/e9ts (e9ts_repetibilidad.py);
#   3. resumen con --modo-principal robust3mm (seccion 5, densidad) en data/e9ts_3mm.
# Requiere en ~/metalsynth/qc/: e9ts_corredor.py (con --modo-laminas), e9ts_resumen.py (con --modo-principal),
#   e9ts_repetibilidad.py, e9_corredor.py, r1_landmarks.py, ts_piloto_qc.py, e9b_densidad_s1.py,
#   r1_landmarks.csv, r1_estados.csv, ts_nivel_s1.csv. Reanudable: relanzar salta los casos ya escritos.
#SBATCH --job-name=e9ts_3mm
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=16
#SBATCH --mem=60G
#SBATCH --time=06:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno totalseg"; exit 1; }
python -c "import nibabel, numpy, pandas, scipy, matplotlib; print('dependencias ok')" \
    || { echo "ERROR: faltan dependencias; instalar en el nodo de acceso (ver KHIPU.md)"; exit 1; }
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)  cpus $SLURM_CPUS_PER_TASK"
python e9ts_corredor.py --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" --refs-dir . \
    --out-dir "$DATA/e9ts_3mm" --workers "$SLURM_CPUS_PER_TASK" --laminas --modo-laminas robust3mm
rc=$?
echo "corredor rc=$rc  $(date -Is)"
[ $rc -eq 0 ] || exit $rc

echo "== REPETIBILIDAD frente a data/e9ts =="
python e9ts_repetibilidad.py --a "$DATA/e9ts/e9ts_corredor.csv" --b "$DATA/e9ts_3mm/e9ts_corredor.csv"
rep=$?

echo "== RESUMEN (principal robust3mm) =="
python e9ts_resumen.py --e9-dir "$DATA/e9ts_3mm" --e10-dir "$DATA/ts_componentes" --modo-principal robust3mm >/dev/null
res=$?
echo "fin $(date -Is)  corredor=$rc  repetibilidad=$rep  resumen=$res"
exit $(( rep != 0 || res != 0 ))
