#!/bin/bash
# E14: cuanto cambia la envolvente osea si se anade el relleno de cavidades cerradas (#127, pto 13).
# Solo CPU: no gasta GPU. NO rehace la busqueda de corredor y NO toca ninguna salida existente.
#
# Que contesta: si el relleno que D-O2.3 ordena, y que el codigo no aplica, mueve `D_TS` sobre el eje
# ya guardado. Si no lo mueve, se corrige el texto de la decision; si lo mueve en algun caso, ese caso
# justifica la corrida de sensibilidad completa.
#
# Coste esperado: mucho menor que E9-TS, que con 16 CPU tardo 6 min 39 s de reloj (job 51505) e incluia
# la busqueda de corredor sobre 81 direcciones por altura. Aqui solo se arman dos mascaras por caso y se
# evalua un eje. La hora de pared pedida es holgada a proposito.
#
# Requiere en ~/metalsynth/qc/: e14_relleno_envolvente.py, sap.py, e9ts_corredor.py, e9_corredor.py,
#   r1_landmarks.py, ts_piloto_qc.py, r1_landmarks.csv, e9ts_corredor.csv.
# Salida: ~/metalsynth/qc/e14_relleno.csv
#SBATCH --job-name=e14relleno
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=16
#SBATCH --mem=60G
#SBATCH --time=02:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno totalseg"; exit 1; }
python -c "import nibabel, numpy, pandas, scipy; print('dependencias ok')" \
    || { echo "ERROR: faltan dependencias; instalar en el nodo de acceso (ver KHIPU.md)"; exit 1; }
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)  cpus $SLURM_CPUS_PER_TASK"

python -u e14_relleno_envolvente.py --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" \
    --refs-dir . --out e14_relleno.csv --workers "$SLURM_CPUS_PER_TASK"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
