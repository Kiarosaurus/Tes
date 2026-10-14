#!/bin/bash
# VERSION 2 (`v2_plan.md`): la misma cadena que `a15_cadena_pose.sbatch` (pose corregida, #173) con el `mejor.pt` de
# run05a o run05b, en tres etapas:
#   1. cotejo  - 0101/0102 (validacion), cascaras de 1 mm, sin NIfTI                       (a17, reportado)
#   2. delta   - 0101/0102 (validacion), `--incluir-banda`, 5 semillas, NIfTI              (perfil D2 -> regla; `s` de Delta)
#   3. final   - 13 de prueba de E-A2: SOLO para el punto que elija `v2_eleccion.py`, nunca antes de la eleccion
# El `delta` de `regla_suave` sale de `a16_v2.sbatch` ($DATA/a16_v2/$RUN/a16_elegido.csv), salvo que se pase DELTA=.
# `a15` lee del checkpoint si el modelo lleva el canal T (run05b, 12 entradas) y su escala.
#
# USO (desde ~/metalsynth, tras `git pull`), encadenado detras de a16_v2:
#   JA=$(sbatch --parsable --export=ALL,RUN=run05a experiments/objetivo3/a16_v2.sbatch)
#   sbatch --dependency=afterok:$JA --export=ALL,RUN=run05a experiments/objetivo3/a15_cadena_v2.sbatch
#   Solo la final, tras la eleccion:  --export=ALL,RUN=<elegido>,ETAPAS=final
# Salida: $DATA/obj3_pose/{cotejo,delta,final}/<RUN>_mejor/ (junto a run04, para compararlos con las mismas rutas)
#SBATCH --job-name=a15v2
# Generar usa pocos GB (lote 1): shards, como a15_cadena_pose; los dos RUN pueden compartir la MIG a la vez.
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=shard:a100_3g.20gb:5
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=03:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
case "${RUN:-}" in
    run05a|run05b) ;;
    *) echo "ERROR: falta RUN=run05a o RUN=run05b (sbatch --export=ALL,RUN=...)"; exit 1 ;;
esac
PT=$DATA/a7/$RUN/mejor.pt
ETIQ=${RUN}_mejor
if [ -z "${DELTA:-}" ]; then
    F16=$DATA/a16_v2/$RUN/a16_elegido.csv
    [ -f "$F16" ] || { echo "ERROR: falta $F16 (correr a16_v2.sbatch con RUN=$RUN, o pasar DELTA=)"; exit 1; }
    DELTA=$(awk -F, -v e="$ETIQ" '$1==e {print $2}' "$F16")
    [ -n "$DELTA" ] || { echo "ERROR: $F16 no trae el delta de $ETIQ"; exit 1; }
fi
ETAPAS=${ETAPAS:-"cotejo delta"}
case " $ETAPAS " in
    *" final "*) [ -f "$DATA/v2_eleccion/v2_eleccion.md" ] && grep -q "elegido \`$ETIQ\`" "$DATA/v2_eleccion/v2_eleccion.md" \
        || { echo "ERROR: la etapa final solo corre para el punto elegido por v2_eleccion.py"; exit 1; } ;;
esac
BASE=${BASE:-$DATA/obj3_pose}
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" \
    || { echo "ERROR: sin torch o sin cuda"; exit 1; }
for f in "$PT" "$REPO/experiments/objetivo2/outputs/e9ts_ejes_corredor.csv" "$REPO/src/common/cotejo.py"; do
    [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
done
grep -q "def pose_a_marco_crudo" "$REPO/experiments/objetivo3/a11_rasterizar_tornillo.py" \
    || { echo "ERROR: a11 sin la correccion de pose de #173 (git pull)"; exit 1; }
grep -q "Regla de eleccion (APROBADA" "$REPO/experiments/objetivo3/v2_plan.md" \
    || { echo "ERROR: v2_plan.md sin la regla de eleccion aprobada (git pull)"; exit 1; }
for viejo in metal_0053 metal_0003; do
    grep -q "dataset7_CLINIC_${viejo}_data" "$REPO/experiments/objetivo1/p1_particion.csv" \
        && { echo "ERROR: p1_particion.csv vieja (aun tiene $viejo; #156/#166)"; exit 1; }
done

echo "inicio $(date -Is)  nodo $(hostname)  gpu $CUDA_VISIBLE_DEVICES  ckpt $ETIQ  delta $DELTA  etapas: $ETAPAS"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
A15="$REPO/experiments/objetivo3/a15_cadena_completa.py"
COMUN=(--cortes 0 --dispositivo cuda --semillas 0 1 2 3 4 --pasos-cotejo-mm 1.0 --data "$DATA/extracted"
       --ckpt "$PT" --etiquetas "$ETIQ" --delta "$DELTA")
rc=0
for etapa in $ETAPAS; do
    echo; echo "##### etapa $etapa  $(date -Is) #####"
    SALIDA=$BASE/$etapa/$ETIQ
    case $etapa in
        cotejo) CASOS=("${VAL[@]}");  EXTRA=(--sin-nifti) ;;
        delta)  CASOS=("${VAL[@]}");  EXTRA=(--incluir-banda) ;;
        final)  CASOS=("${TEST[@]}"); EXTRA=(--incluir-banda --particiones test --corrida-final) ;;
        *) echo "ERROR: etapa desconocida $etapa"; exit 1 ;;
    esac
    for caso in "${CASOS[@]}"; do
        echo; echo "=== $etapa $caso  $(date -Is) ==="
        python -u "$A15" --caso "$caso" "${COMUN[@]}" "${EXTRA[@]}" --out-dir "$SALIDA" \
            || { echo "ERROR en $etapa $caso"; rc=1; }
    done
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
