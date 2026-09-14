#!/bin/bash
# Lanza la noche completa en Khipu con una sola orden:  bash ~/metalsynth/noche_e9ts.sh
#   1. E10  ts_componentes.sbatch  (4 CPU)   ┐ en paralelo
#   2. E9-TS e9ts_corredor.sbatch  (16 CPU)  ┘
#   3. resumen (e9ts_resumen.py), cuando terminen los dos (afterany: corre aunque uno falle,
#      y el resumen dice que falta).
# No elige nada: la fraccion de limpieza y #52 se deciden despues leyendo data/e9ts/e9ts_resumen.md.
set -o pipefail
cd "$HOME/metalsynth" || exit 1
sed -i 's/\r$//' ./*.sbatch ./*.sh
for f in qc/ts_componentes.py qc/e9ts_corredor.py qc/e9_corredor.py qc/e9ts_resumen.py qc/r1_landmarks.py \
         qc/ts_piloto_qc.py qc/e9b_densidad_s1.py qc/r1_landmarks.csv qc/r1_estados.csv qc/ts_nivel_s1.csv; do
    [ -f "$f" ] || { echo "ERROR: falta $f (ver KHIPU.md, E9-TS paso 1)"; exit 1; }
done
n_ok=$(find data/ts_total -name .ok | wc -l)
[ "$n_ok" -eq 358 ] || { echo "ERROR: data/ts_total tiene $n_ok .ok (esperado 358)"; exit 1; }

E=$(sbatch --parsable ts_componentes.sbatch) || exit 1
N=$(sbatch --parsable e9ts_corredor.sbatch) || exit 1
R=$(sbatch --parsable --dependency=afterany:$E:$N --job-name=e9ts_resumen --partition=big-mem \
    --nodelist=n006 --account=tesis --qos=a-tesis --cpus-per-task=1 --mem=4G --time=01:00:00 \
    --output=e9ts_resumen_%j.log --wrap "module load miniconda/3.0; \
source \"\$(conda info --base)/etc/profile.d/conda.sh\"; conda activate totalseg; cd \$HOME/metalsynth/qc; \
python e9ts_resumen.py --e9-dir \$HOME/metalsynth/data/e9ts --e10-dir \$HOME/metalsynth/data/ts_componentes") || exit 1
echo "E10=$E  E9TS=$N  RESUMEN=$R" | tee -a noche_e9ts_jobs.txt
squeue -u "$USER" -o "%.8i %.14j %.9P %.2t %.10M %.8N %R"
