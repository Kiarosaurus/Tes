#!/bin/bash
# E9-TS: corredor oseo sobre las mascaras de TS (e9ts_corredor.py) en Khipu. Solo CPU: no gasta GPU.
# Calcula todas las variantes (recorte x fraccion de limpieza) para no tener que volver a correr cuando
# se decidan la fraccion (E10) y #52. Puede correr en paralelo con ts_componentes.sbatch.
# Requiere en ~/metalsynth/qc/: e9ts_corredor.py, e9_corredor.py, r1_landmarks.py, ts_piloto_qc.py,
#   e9b_densidad_s1.py, r1_landmarks.csv, r1_estados.csv, ts_nivel_s1.csv (ver KHIPU.md, E9-TS).
# Reanudable: relanzar salta los casos ya escritos.
# Salida: ~/metalsynth/data/e9ts/{e9ts_corredor.csv, e9ts_perfiles.csv, laminas/*.png}
#
# Recursos: a-tesis limita a 32 CPU y 98G sumando jobs. Con ts_componentes (4 CPU, 32G) en marcha,
# 16 CPU + 60G deja margen.
#SBATCH --job-name=e9ts
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=16
#SBATCH --mem=60G
#SBATCH --time=24:00:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno totalseg"; exit 1; }
python -c "import nibabel, numpy, pandas, scipy, matplotlib; print('dependencias ok')" \
    || { echo "ERROR: faltan dependencias; instalar en el nodo de acceso (ver KHIPU.md)"; exit 1; }
# Un hilo por proceso: el paralelismo lo pone el pool de casos.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1

cd "$HOME/metalsynth/qc" || { echo "ERROR: falta ~/metalsynth/qc"; exit 1; }
echo "inicio $(date -Is)  nodo $(hostname)  cpus $SLURM_CPUS_PER_TASK"
python e9ts_corredor.py --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" --refs-dir . \
    --out-dir "$DATA/e9ts" --workers "$SLURM_CPUS_PER_TASK" --laminas
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
