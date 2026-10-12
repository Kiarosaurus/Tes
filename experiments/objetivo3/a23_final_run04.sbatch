#!/bin/bash
# CORRIDA FINAL E-A1 con run04: reconstruccion del implante real en los pacientes de test con metal
# (diseno_A.md seccion 0 + ENMIENDA 2026-10-11 (run04); `metal_0072` incluido, ya sin fuga, #166).
# Derivado de `a23_final.sbatch` (el de `mejor_37k`, archivado). Componentes >= 500 mm3, hasta 24 cortes por
# componente, `run04_mejor`, 5 semillas. E-A1 va solo con el checkpoint principal (la sensibilidad de #169 (b) es
# de E-A2).
# GPU FIJA: gpu:rtxa6000:1 en `all`, la de toda la repeticion con la pose corregida (diseno_A.md, #173, #151).
# La corrida de `mejor_37k` en RTX A6000 tardo 2 h 31 min.
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only experiments/objetivo3/a23_final_run04.sbatch
#   J=$(sbatch --parsable experiments/objetivo3/a23_final_run04.sbatch); echo $J
# Salida: $DATA/a23_final_run04/ (a23_parches.csv, a23_pacientes.csv y el cache de parches de test)
# DELTA (#172, opcion (A), 2026-10-11): `run04_mejor` se lee con 0.03 (valor por omision) -> salida con sufijo _d003.
# Principal confirmado por la autora el 2026-10-12 (#174 (a)).
#SBATCH --job-name=a23fin04
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=05:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
DELTA=${DELTA:-0.03}           # #172 (A): run04_mejor 0.03
SUF=""; [ "$DELTA" != "0.05" ] && SUF="_d${DELTA/./}"
REPO=$HOME/metalsynth
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available()" || { echo "ERROR: sin cuda"; exit 1; }
[ -f "$DATA/a7/run04/mejor.pt" ] || { echo "ERROR: falta run04/mejor.pt"; exit 1; }
grep -q "ENMIENDA 2026-10-11 (run04)" "$REPO/experiments/objetivo3/diseno_A.md" || { echo "ERROR: diseno_A.md sin la enmienda de run04 (git pull)"; exit 1; }
for viejo in metal_0053 metal_0003; do
    grep -q "dataset7_CLINIC_${viejo}_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
        && { echo "ERROR: p1_particion.csv vieja (aun tiene $viejo; #156/#166)"; exit 1; }
done

echo "inicio $(date -Is)  nodo $(hostname)  delta $DELTA"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
python -u "$REPO/experiments/objetivo3/a23_ea1.py" --particiones test --corrida-final --dispositivo cuda \
    --data "$DATA/extracted" --ckpt "$DATA/a7/run04/mejor.pt" --delta "$DELTA" --out-dir "$DATA/a23_final_run04$SUF"
rc=$?
echo "fin $(date -Is)  rc=$rc"
exit $rc
