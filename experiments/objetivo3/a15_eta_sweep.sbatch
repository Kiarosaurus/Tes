#!/bin/bash
# V3 ETAPA 0 (POST-HOC, EXPLORATORIA; borrador en _plan_urgente_2026-11/tesis/v3_plan.md): barrido del MUESTREO
# (pasos DDIM x eta) con el run04_mejor YA ENTRENADO, sobre validacion 0101/0102. No reentrena nada.
# Control: la variante 50:0 reproduce el cotejo de run04_mejor (mismo delta 0.03, mismas semillas): si sus cifras no
# coinciden con `$DATA/obj3_pose/cotejo/run04_mejor`, el barrido no es interpretable.
# Salida: $DATA/obj3_pose/eta_sweep/run04_mejor_p<PASOS>_e<ETA>/  (_cotejo.csv, sin NIfTI)
# Leer despues con a17_cotejo.py --dir-sintetico <carpeta> --paso-mm 1 (regla de a17: fijada antes).
#
# VARIANTES="pasos:eta ..." (por omision, ver abajo; las fija la autora antes de correr). CORTES=0 -> todos los cortes
# con M; CORTES=2 para una prueba de humo.
# USO (desde ~/metalsynth, tras `git fetch origin && git switch exp/v3-eta-muestreo`):
#   sbatch --test-only --export=ALL,CORTES=2,VARIANTES="50:0 50:0.3" experiments/objetivo3/a15_eta_sweep.sbatch
#   sbatch --export=ALL,CORTES=2,VARIANTES="50:0 50:0.3" experiments/objetivo3/a15_eta_sweep.sbatch    # humo
#   sbatch -p all --gres=gpu:a100:1 --time=06:00:00 experiments/objetivo3/a15_eta_sweep.sbatch           # completo
# Lo que se pase con -p/--gres/--time al enviar manda sobre los #SBATCH de abajo (--time <= MaxWall 24 h).
#SBATCH --job-name=a15eta
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=shard:a100_3g.20gb:5
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=06:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
PT="$DATA/a7/run04/mejor.pt"
DELTA=${DELTA:-0.03}
CORTES=${CORTES:-0}
VARIANTES=${VARIANTES:-"50:0 50:0.3 50:0.6 100:0.3 200:0"}
BASE=${BASE:-$DATA/obj3_pose/eta_sweep}
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$PT" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q "'--eta'" "$REPO/experiments/objetivo3/a15_cadena_completa.py" \
    || { echo "ERROR: a15 sin --eta (cambiar a la rama exp/v3-eta-muestreo)"; exit 1; }

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  delta $DELTA  cortes $CORTES  variantes: $VARIANTES"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
A15="$REPO/experiments/objetivo3/a15_cadena_completa.py"
rc=0
for v in $VARIANTES; do
    P=${v%%:*}; E=${v##*:}
    ETIQ=run04_mejor_p${P}_e${E}
    SALIDA=$BASE/$ETIQ
    echo; echo "##### variante $ETIQ  $(date -Is) #####"
    for caso in "${VAL[@]}"; do
        echo "=== $ETIQ $caso  $(date -Is) ==="
        python -u "$A15" --caso "$caso" --cortes "$CORTES" --dispositivo cuda --semillas 0 1 2 3 4 \
            --pasos-cotejo-mm 1.0 --data "$DATA/extracted" --ckpt "$PT" --etiquetas "$ETIQ" --delta "$DELTA" \
            --pasos "$P" --eta "$E" --sin-nifti --out-dir "$SALIDA" \
            || { echo "ERROR en $ETIQ $caso"; rc=1; }
    done
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
