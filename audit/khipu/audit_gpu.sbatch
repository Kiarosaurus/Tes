#!/bin/bash
# AUDITORIA: diagnosticos de SOLO INFERENCIA de run04_mejor (ningun entrenamiento, no toca checkpoints ni scripts del repo).
# Origen: informes C (Opus) y F (Codex) de audit/reports/. Cada MODO responde una recomendacion de C:
#   MODO=r4   R-4  efecto de la tarjeta: val 0101/0102, 5 semillas, como la referencia 15-oct. Lanzar con la GPU del ajuste fino (T4).
#   MODO=r1   R-1  piso de ruido (G sin M) de los 13 de prueba. Si ya existe $DATA/obj3_pose/nulo/run04_mejor_nulo, no regenera.
#   MODO=r2   R-2  piso de ruido de variantes de eta: val 0101/0102, --sin-metal, (50:0), (50:0.3), (100:0.3), 5 semillas.
#   MODO=r9   R-9  atajo del contexto: val 0101/0102, contexto original (control) vs contexto suavizado (mediana 5 px fuera de G).
#   MODO=r9s  R-9 con --sin-metal: el mismo par ctxorig/ctxsuave SIN metal (separa artefacto de anatomia). val 0101/0102, 5 semillas.
#   MODO=r9v  R-9 VISUAL: val 0101, semillas 0 y 1, CON NIfTI (ctxorig y ctxsuave) para abrirlos en ITK-SNAP y comparar a ojo.
#   MODO=r3   R-3  "validacion 2": casos de $CASOS (por omision audit/khipu/casos_val2.txt), run04_mejor x {50:0, 50:0.3, 100:0.3}.
#   MODO=r12  R-12 sintesis sobre poses perturbadas del muestreador en esos mismos casos (--perturbar).
# USO (desde ~, sin tocar ~/metalsynth ni su rama):
#   sbatch --test-only -p all --gres=gpu:tesla:1 --export=ALL,MODO=r4 ~/audit_khipu/audit_gpu.sbatch
#   sbatch -p all --gres=gpu:tesla:1 --export=ALL,MODO=r4 ~/audit_khipu/audit_gpu.sbatch
# Reanudable: se salta lo que ya tiene `_s4_perfil.csv`. Salidas en $DATA/obj3_pose/audit/<modo>/
#SBATCH --job-name=audit
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:tesla:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
AUD=${AUD:-$HOME/audit_khipu}
PT="$DATA/a7/run04/mejor.pt"
A15="$REPO/experiments/objetivo3/a15_cadena_completa.py"
A15DIR="$REPO/experiments/objetivo3"
OUT0=$DATA/obj3_pose/audit
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch, scipy; assert torch.cuda.is_available(); print('torch', torch.__version__)" || { echo "ERROR: sin cuda o scipy"; exit 1; }
[ -f "$PT" ] || { echo "ERROR: falta $PT"; exit 1; }
for f in "--sin-metal" "--eta" "--perturbar" "--guardar-u-g"; do
    grep -q -- "'$f'" "$A15" || { echo "ERROR: a15 de la rama actual no tiene $f"; exit 1; }
done
echo "inicio $(date -Is)  nodo $(hostname)  modo ${MODO:-}  commit $(git -C "$REPO" rev-parse --short HEAD) rama $(git -C "$REPO" branch --show-current)"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
COMUN=(--cortes 0 --dispositivo cuda --semillas 0 1 2 3 4 --data "$DATA/extracted" --ckpt "$PT" --delta 0.03 --sin-nifti --pasos-cotejo-mm 1.0)
GENCOM=("${COMUN[@]}"); LASTSEED=4
rc=0

# genera ETIQ sobre los casos dados; $1 etiqueta, $2 dir salida, $3 pasos, $4 eta, resto = casos; EXTRA = banderas adicionales (array)
gen() {
    local etiq=$1 sal=$2 pasos=$3 eta=$4; shift 4
    for caso in "$@"; do
        if [ -f "$sal/a15_${caso}_${etiq}_s${LASTSEED}_perfil.csv" ]; then echo "=== $caso $etiq ya generado, se salta ==="; continue; fi
        echo; echo "=== $etiq $caso  $(date -Is) ==="
        python -u "$A15" --caso "$caso" "${GENCOM[@]}" --etiquetas "$etiq" --pasos "$pasos" --eta "$eta" \
            "${EXTRA[@]}" --out-dir "$sal" || { echo "ERROR $etiq $caso"; rc=1; }
    done
}
EXTRA=()
case "${MODO:-}" in
    r4)  GPU=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1 | tr ' ' '_')
         EXTRA=(--particiones val); gen run04_mejor "$OUT0/r4_$GPU" 50 0 "${VAL[@]}" ;;
    r1)  if [ -d "$DATA/obj3_pose/nulo/run04_mejor_nulo" ] && [ "$(ls "$DATA"/obj3_pose/nulo/run04_mejor_nulo/*_s4_perfil.csv 2>/dev/null | wc -l)" -ge 13 ]; then
             echo "R-1: ya existe $DATA/obj3_pose/nulo/run04_mejor_nulo con los 13 casos; no se regenera. Bajar esa carpeta (solo *_perfil.csv)."
         else
             EXTRA=(--sin-metal --incluir-banda --particiones test --corrida-final)
             gen run04_mejor_nulo "$OUT0/r1_nulo" 50 0 "${TEST[@]}"
         fi ;;
    r2)  EXTRA=(--sin-metal --incluir-banda --particiones val)
         for v in "50 0" "50 0.3" "100 0.3"; do set -- $v
             gen "run04_mejor_nulo_p$1_e$2" "$OUT0/r2_piso_eta" "$1" "$2" "${VAL[@]}"
         done ;;
    r9)  EXTRA=(--particiones val)
         export A15_DIR="$A15DIR"
         A15="$AUD/audit_r9_contexto.py"
         export R9_SUAVE=0; gen run04_mejor_ctxorig  "$OUT0/r9_contexto" 50 0 "${VAL[@]}"
         export R9_SUAVE=1; gen run04_mejor_ctxsuave "$OUT0/r9_contexto" 50 0 "${VAL[@]}" ;;
    r9s) EXTRA=(--particiones val --sin-metal)
         export A15_DIR="$A15DIR"
         A15="$AUD/audit_r9_contexto.py"
         export R9_SUAVE=0; gen run04_mejor_nulo_ctxorig  "$OUT0/r9s_contexto_sinmetal" 50 0 "${VAL[@]}"
         export R9_SUAVE=1; gen run04_mejor_nulo_ctxsuave "$OUT0/r9s_contexto_sinmetal" 50 0 "${VAL[@]}" ;;
    r9v) EXTRA=(--particiones val)
         GENCOM=(--cortes 0 --dispositivo cuda --semillas 0 1 --data "$DATA/extracted" --ckpt "$PT" --delta 0.03 --pasos-cotejo-mm 1.0); LASTSEED=1
         export A15_DIR="$A15DIR"
         A15="$AUD/audit_r9_contexto.py"
         export R9_SUAVE=0; gen run04_mejor_ctxorig  "$OUT0/r9v_visual" 50 0 "${VAL[0]}"
         export R9_SUAVE=1; gen run04_mejor_ctxsuave "$OUT0/r9v_visual" 50 0 "${VAL[0]}" ;;
    r3|r12)
         CASOS=${CASOS:-$AUD/casos_val2.txt}
         [ -f "$CASOS" ] || { echo "ERROR: falta $CASOS"; exit 1; }
         mapfile -t V2 < "$CASOS"; echo "casos validacion 2: ${#V2[@]}"
         if [ "$MODO" = r3 ]; then
             EXTRA=(--incluir-banda --particiones train)
             for v in "50 0" "50 0.3" "100 0.3"; do set -- $v
                 gen "run04_mejor_p$1_e$2" "$OUT0/r3_val2" "$1" "$2" "${V2[@]}"
             done
         else
             EXTRA=(--incluir-banda --particiones train --perturbar --semilla-pose 0)
             gen run04_mejor_pert "$OUT0/r12_poses" 50 0 "${V2[@]}"
         fi ;;
    *) echo "ERROR: falta MODO=r4|r1|r2|r9|r9s|r9v|r3|r12"; exit 1 ;;
esac
echo "fin $(date -Is)  rc=$rc"
exit $rc
