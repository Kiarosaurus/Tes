#!/bin/bash
# Contraste PAREADO del difusor (#188, #187 c; regla fijada antes en `resultados_dec_2026-10-15.md`, seccion "Perfil
# por anillos y contraste pareado"). POSTERIOR y descriptivo: no cambia el desenlace confirmatorio.
#
# Referencia del difusor = su sintetica SIN metal (`a15 --sin-metal`, job 56867), misma semilla y mismo corte,
# en vez de la TC original: el analogo de Peters, que se mide contra su propia simulacion sin metal. Solo v1
# (run04_mejor): v2 no tiene nulo (`--sin-metal` no esta definido para entrada 12).
#
# Variantes: base (banda congelada) y los anillos 0-12 mm de 2 mm. En CPU; los NIfTI solo estan en Khipu.
# USO (desde ~/metalsynth, tras git pull):  sbatch experiments/objetivo3/a20_pareado.sbatch
# Salida: $DATA/obj3_pose/pareado/a20_pareado_<VARIANTE>.csv (un CSV por variante; candado contra doble envio)
#SBATCH --job-name=a20par
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
OUT=$DATA/obj3_pose/pareado
A20="$REPO/experiments/objetivo3/a20_evaluador_ea2.py"
FIN=$DATA/obj3_pose/final/run04_mejor
NUL=$DATA/obj3_pose/nulo/run04_mejor_nulo
mapfile -t TEST < <(tr -d '\r' < "$REPO/experiments/objetivo3/casos_ea2_test.txt")
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
grep -q -- "--ref-dir" "$A20" || { echo "ERROR: a20 sin --ref-dir (git pull)"; exit 1; }
for caso in "${TEST[@]}"; do
    for s in 0 1 2 3 4; do
        for f in "$FIN/a15_${caso}_run04_mejor_s${s}_sintetica.nii.gz" "$NUL/a15_${caso}_run04_mejor_nulo_s${s}_sintetica.nii.gz"; do
            [ -f "$f" ] || { echo "ERROR: falta $f"; exit 1; }
        done
    done
done
mkdir -p "$OUT"
mkdir "$OUT/.candado" 2>/dev/null || { echo "ERROR: ya hay (o hubo) un job: borra $OUT/.candado si fallo"; exit 1; }
echo "inicio $(date -Is)  commit $(git -C "$REPO" rev-parse --short HEAD)"
rc=0
for v in base r00_02 r02_04 r04_06 r06_08 r08_10 r10_12; do
    case $v in
        base) OPC=() ;;
        r00_02) OPC=(--r-min-mm 0 --r-max-mm 2) ;; r02_04) OPC=(--r-min-mm 2 --r-max-mm 4) ;;
        r04_06) OPC=(--r-min-mm 4 --r-max-mm 6) ;; r06_08) OPC=(--r-min-mm 6 --r-max-mm 8) ;;
        r08_10) OPC=(--r-min-mm 8 --r-max-mm 10) ;; r10_12) OPC=(--r-min-mm 10 --r-max-mm 12) ;;
    esac
    CSV=$OUT/a20_pareado_$v.csv
    rm -f "$CSV"
    echo; echo "=== $v $(date -Is)"
    for caso in "${TEST[@]}"; do
        python -u -W ignore "$A20" difusor --caso "$caso" --dir "$FIN" --etiqueta run04_mejor --ref-dir "$NUL" \
            --ref-etiqueta run04_mejor_nulo --corrida-final "${OPC[@]}" --out "$CSV" || { echo "ERROR $v $caso"; rc=1; }
    done
done
echo "fin $(date -Is)  rc=$rc"
exit $rc
