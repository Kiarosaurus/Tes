#!/bin/bash
# A15 DELTA run04 en Khipu: componente `s` de `Delta = max(s, r)` (D4) con el modelo sin fuga (#166).
# 01-decisiones 2026-10-11 (2) punto 2: `s` se recalcula con el checkpoint elegido, en validacion, antes de test.
# Se generan LOS DOS candidatos (#169, opcion (b) de la autora, 2026-10-11): `run04_mejor` (el elegido por la
# regla) y `run04_60k` (sensibilidad de E-A2). Cada uno lleva su propio `s`; `r` (Peters) no cambia.
#
# Derivado de `a15_delta.sbatch` (el de `mejor_37k`, archivado). Igual: 5 semillas, `--incluir-banda` (#160),
# NIfTI, cascaras de 1 mm, receptores `0101`/`0102`.
# GPU: `a100_3g.20gb:1` en `all`, la misma del cotejo de run04 (job 55820). `a15_final` DEBE usar la misma
# (#151: con la misma semilla, otra GPU da otro ruido y `s` dejaria de describir la corrida final).
#
# USO (desde ~/metalsynth, tras `git pull`):
#   sbatch --test-only experiments/objetivo3/a15_delta_run04.sbatch
#   J=$(sbatch --parsable experiments/objetivo3/a15_delta_run04.sbatch); echo $J
# Salida: $DATA/a15_delta_run04/ (un .nii.gz por semilla, checkpoint y paciente, mas original, M y G)
#SBATCH --job-name=a15del04
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:a100_3g.20gb:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=02:30:00
#SBATCH --output=%x_%j.log

set -o pipefail

DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
SALIDA=${SALIDA:-$DATA/a15_delta_run04}
CASOS=("$@")
[ ${#CASOS[@]} -eq 0 ] && CASOS=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$DATA/a7/run04/mejor.pt" "$DATA/a7/run04/ckpt.pt" \
         "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" \
         "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q -- "--incluir-banda" "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
    || { echo "ERROR: a15 sin --incluir-banda (git pull)"; exit 1; }
for viejo in metal_0053 metal_0003; do
    grep -q "dataset7_CLINIC_${viejo}_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
        && { echo "ERROR: p1_particion.csv vieja (aun tiene $viejo; #156/#166)"; exit 1; }
done

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

rc=0
for caso in "${CASOS[@]}"; do
    echo; echo "=== $caso  $(date -Is) ==="
    python -u "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
        --caso "$caso" --cortes 0 --incluir-banda --dispositivo cuda --semillas 0 1 2 3 4 \
        --pasos-cotejo-mm 1.0 \
        --data "$DATA/extracted" \
        --ckpt "$DATA/a7/run04/mejor.pt" "$DATA/a7/run04/ckpt.pt" --etiquetas run04_mejor run04_60k \
        --out-dir "$SALIDA" \
        || { echo "ERROR en $caso"; rc=1; }
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
