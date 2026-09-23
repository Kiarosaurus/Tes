#!/bin/bash
# E13: muestreo de poses + SAP + Wasserstein-1 contra zwingmann2009navigated. Solo CPU: no gasta GPU.
# Corre las DOS cohortes en un solo job: la primaria (72 casos, grupos 2 y 3) y la sensibilidad
# (49 casos, grupo 3). La semilla es por caso, asi que los 49 reciben exactamente las mismas poses que
# en la corrida de 72 y la diferencia entre ambas cifras aisla el efecto de cohorte.
#
# Requiere TODO en ~/metalsynth/qc/ (mismo directorio, sin subcarpetas):
#   sap.py, muestreo.py, e13_muestreo_sap.py, e12_sap_control.py, e9ts_corredor.py, e9_corredor.py,
#   r1_landmarks.py, ts_piloto_qc.py, r1_landmarks.csv, e9ts_corredor.csv.
#   `sap.py` y `muestreo.py` van aqui y no en src/: los scripts anaden su propio directorio al
#   sys.path, asi que con estar al lado basta.
# Salida: ~/metalsynth/qc/{e13_poses.csv, e13_sap.md, e13_poses_g3.csv, e13_sap_g3.md}
#
# Coste medido en local: 15.7 s por caso, sin paralelismo. 72 + 49 casos ~ 32 min de reloj.
# `python -u`: sin el, la salida va a bloque porque el log es un archivo y no una terminal, y el
# progreso por caso no aparece hasta el final. Se noto en la corrida 52175.
# La hora de pared pedida es holgada a proposito; el job no usa GPU y no compite por ella.
#SBATCH --job-name=e13sap
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=04:00:00
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

echo "== cohorte primaria: 72 casos (grupos 2 y 3) =="
python -u e13_muestreo_sap.py --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" --refs-dir .
rc1=$?
echo "rc primaria = $rc1"

echo "== sensibilidad: 49 casos (grupo 3) =="
python -u e13_muestreo_sap.py --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" --refs-dir . \
    --grupos "grupo 3" --out-sufijo _g3
rc2=$?
echo "rc sensibilidad = $rc2"

rc=$(( rc1 > rc2 ? rc1 : rc2 ))
echo "fin $(date -Is)  rc=$rc"
exit $rc
