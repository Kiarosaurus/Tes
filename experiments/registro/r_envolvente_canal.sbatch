#!/bin/bash
# #196 (opcion b): la envolvente osea `B` de SAP y el canal sacro, en los 72 casos de la cohorte primaria del
# Objetivo 2 (grupos 2 y 3). Solo CPU: no gasta GPU. NO toca ninguna salida existente.
#
# Que contesta: en cuantos casos el cierre de 2 mm de `B` ocupa el hueco medial de S1 (el que en los pilotos tiene
# HU de partes blandas, compatible con el canal), y en cuantos mm. Descriptivo y posterior; no mide foramenes ni el
# efecto sobre la brecha de ninguna pose (ver `experiments/registro/registro_2026-10-16.md` §1).
#
# Control de regresion por caso: la longitud anclada sobre `B` debe reproducir `L_TS_mejor_mm` de E9-TS, como en
# E12. Si no reproduce, ese caso queda como NO REPRODUCE y sin cifras. En local reproduce los dos pilotos
# (113.0 y 154.0 mm) y las cifras del registro del 2026-10-16.
#
# Requiere TODO en ~/metalsynth/qc/ (mismo directorio). Ya estan ahi desde E13: sap.py, muestreo.py,
#   e13_muestreo_sap.py, e12_sap_control.py, e9ts_corredor.py, e9_corredor.py, r1_landmarks.py, ts_piloto_qc.py,
#   e9b_densidad_s1.py, r1_landmarks.csv, e9ts_corredor.csv. Nuevo: r_envolvente_canal.py.
# Salida: ~/metalsynth/qc/{r_envolvente_canal.md, r_envolvente_canal.csv} (el CSV se reescribe tras cada caso).
#
# Coste medido en local: ~10 s por caso, en serie. 72 casos ~ 12 min. La hora de pared pedida es holgada.
#SBATCH --job-name=renvcanal
#SBATCH --partition=big-mem
#SBATCH --nodelist=n006
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
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
for f in r_envolvente_canal.py sap.py muestreo.py e13_muestreo_sap.py e12_sap_control.py e9ts_corredor.py \
         e9_corredor.py r1_landmarks.py ts_piloto_qc.py e9b_densidad_s1.py r1_landmarks.csv e9ts_corredor.csv; do
    [ -f "$f" ] || { echo "ERROR: falta qc/$f"; exit 1; }
done
echo "inicio $(date -Is)  nodo $(hostname)  cpus $SLURM_CPUS_PER_TASK"

python -u r_envolvente_canal.py --cohorte --ts-dir "$DATA/ts_total" --ct-dir "$DATA/ts_input" \
    --refs-dir . --out r_envolvente_canal.md --csv r_envolvente_canal.csv
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
