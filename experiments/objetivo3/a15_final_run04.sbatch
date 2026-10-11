#!/bin/bash
# CORRIDA FINAL E-A2 con run04, difusor: los 13 pacientes de test sin metal (casos_ea2_test.txt).
# Diseno: diseno_A.md seccion 0 + ENMIENDA 2026-10-11 (run04). Un checkpoint por job, elegido con CKPT:
#   CKPT=mejor -> run04/mejor.pt (principal)      CKPT=60k -> run04/ckpt.pt (sensibilidad, #169 (b))
# 5 semillas, --incluir-banda, NIfTI. Cada checkpoint escribe en su propia carpeta (los dos jobs pueden correr a la
# vez sin pisarse los original/M/G).
# GPU FIJA: gpu:a100_3g.20gb:1 en `all`, la misma en que se midio `s` de Delta (job 55825). NO pasar por
# khipu_elegir_gpu.sh ni cambiar --gres (#151; KHIPU.md nota 12).
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only --export=ALL,CKPT=mejor experiments/objetivo3/a15_final_run04.sbatch
#   J1=$(sbatch --parsable --export=ALL,CKPT=mejor experiments/objetivo3/a15_final_run04.sbatch); echo $J1
#   J2=$(sbatch --parsable --export=ALL,CKPT=60k   experiments/objetivo3/a15_final_run04.sbatch); echo $J2
#   Relanzar solo algunos:  sbatch --export=ALL,CKPT=mejor ... a15_final_run04.sbatch dataset6_CLINIC_0012_data ...
# Salida: $DATA/a15_final_run04/run04_<CKPT>/
#SBATCH --job-name=a15fin04
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:a100_3g.20gb:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
case "${CKPT:-}" in
    mejor) PT="$DATA/a7/run04/mejor.pt" ;;
    60k)   PT="$DATA/a7/run04/ckpt.pt" ;;
    *) echo "ERROR: falta CKPT=mejor o CKPT=60k (sbatch --export=ALL,CKPT=...)"; exit 1 ;;
esac
ETIQ=run04_$CKPT
SALIDA=${SALIDA:-$DATA/a15_final_run04/$ETIQ}
CASOS=("$@")
[ ${#CASOS[@]} -eq 0 ] && mapfile -t CASOS < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$PT" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q "ENMIENDA 2026-10-11 (run04)" "$REPO/experiments/objetivo3/diseno_A.md" \
    || { echo "ERROR: diseno_A.md sin la enmienda de run04 (git pull)"; exit 1; }
for viejo in metal_0053 metal_0003; do
    grep -q "dataset7_CLINIC_${viejo}_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
        && { echo "ERROR: p1_particion.csv vieja (aun tiene $viejo; #156/#166)"; exit 1; }
done

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  casos ${#CASOS[@]}  ckpt $ETIQ"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
rc=0
for caso in "${CASOS[@]}"; do
    echo; echo "=== $caso  $(date -Is) ==="
    python -u "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
        --caso "$caso" --particiones test --corrida-final \
        --cortes 0 --incluir-banda --dispositivo cuda --semillas 0 1 2 3 4 --pasos-cotejo-mm 1.0 \
        --data "$DATA/extracted" --ckpt "$PT" --etiquetas "$ETIQ" \
        --out-dir "$SALIDA" \
        || { echo "ERROR en $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
