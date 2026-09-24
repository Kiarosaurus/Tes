#!/bin/bash
# E9-TS, segunda pasada: guarda el EJE DEL CORREDOR A CADA ALTURA en e9ts_perfiles.csv (#121).
# Solo CPU: no gasta GPU.
#
# QUE CAMBIA respecto de la corrida original (job 51505): `buscar()` conservaba solo el diametro por
# altura y descartaba el `c`/`u` de cada z; ahora los guarda, y `CAMPOS_PERFIL` pasa de 6 a 12 columnas
# (+ c_x_mm, c_y_mm, c_z_mm, u_x, u_y, u_z). El resto del calculo es el mismo.
#
# POR QUE SE CORRE LA COHORTE ENTERA Y NO SOLO LOS 72: el coste es bajo (la corrida original sumo
# 1.34 h de CPU sobre 152 casos y todas las variantes) y correrlo todo permite el control de abajo
# sobre los 152, no sobre un subconjunto.
#
# CONTROL QUE PUEDE FALLAR: el cambio solo ANADE columnas al archivo de perfiles. El `e9ts_corredor.csv`
# nuevo tiene que salir identico por valor al existente. Si difiere en algo que no sea dtype, el cambio
# toco lo que no debia y no se usa nada de esta corrida. Verificado ya en local sobre un caso piloto:
# 46 columnas, ninguna difiere.
#
# NO SOBRESCRIBE NADA: escribe en un --out-dir propio. El `e9ts_corredor.csv` del repositorio respalda
# cifras que ya estan en `tesis/main.tex`.
#
# Requiere en ~/metalsynth/qc/: e9ts_corredor.py (la version nueva), e9_corredor.py, r1_landmarks.py,
#   ts_piloto_qc.py, e9b_densidad_s1.py, r1_landmarks.csv, r1_estados.csv, ts_nivel_s1.csv.
# Salida: ~/metalsynth/data/e9ts_ejes/{e9ts_corredor.csv, e9ts_perfiles.csv}
# Reanudable: relanzar salta los casos que ya tienen filas.
#SBATCH --job-name=e9tsejes
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

# Sin --laminas: no hacen falta y cuestan tiempo.
python -u e9ts_corredor.py --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" --refs-dir . \
    --out-dir "$DATA/e9ts_ejes" --workers "$SLURM_CPUS_PER_TASK"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
