#!/bin/bash
# Version 2, EXPLORATORIO (#182; v2_plan.md) + mediciones de DEC 2026-10-15: evaluacion E-A2 de run05a y run05b en
# Khipu, en CPU (los NIfTI de la final de v2 solo estan aqui). Produce SOLO los CSV de `a20`; `a24` (contrastes,
# desenlaces de DEC 2026-10-15 pto 15, margenes, permutacion) se corre en local sobre esos CSV.
#
# Etapas (variable ETAPA):
#   val  - a20 peters (peters_val) + a20 difusor (etapa delta, 0101/0102, 5 semillas) -> Delta = max(s, r) por modelo
#   test - a20 peters (peters_final) + copia y pegado (5371 HU) + a20 difusor (final, 13 x 5) en la VARIANTE pedida
#
# Variantes de prueba (VARIANTE; todas POSTERIORES salvo `base`, DEC 2026-10-15):
#   base       definicion congelada (+ suelo_frac de Peters y exceso_costura de los dos brazos, ptos 1 y 5)
#   inter      difusor solo en los cortes simulados por Peters (`--interseccion`, pto 17)
#   suelo      los dos brazos recortados a -1000 HU (pto 1)
#   sincabeza  sin ROIs a menos de 20 mm del extremo con cabeza (pto 2)
#   r08_10 r10_12 r12_14 r14_16   perfil de amplitud en anillos de 2 mm (pto 5)
#
# USO (desde ~/metalsynth, tras git pull):
#   sbatch --export=ALL,ETAPA=val experiments/objetivo3/a20_v2.sbatch
#   for v in base inter suelo sincabeza r08_10 r10_12 r12_14 r14_16; do
#       sbatch --export=ALL,ETAPA=test,VARIANTE=$v experiments/objetivo3/a20_v2.sbatch; done
# Salida: $DATA/v2_prueba/{a20_val.csv, a20_delta_<run>_mejor.json, a20_test_<VARIANTE>.csv}
# Cada (ETAPA, VARIANTE) escribe SOLO su propio CSV y toma un candado: un segundo envio igual aborta sin tocar nada
# (el 2026-10-14 un doble envio borro el CSV de validacion, #184).
#SBATCH --job-name=a20v2
#SBATCH --partition=big-mem
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --cpus-per-task=4
#SBATCH --mem=48G
#SBATCH --time=08:00:00
#SBATCH --output=%x_%j.log

set -o pipefail
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
OUT=$DATA/v2_prueba
A20="$REPO/experiments/objetivo3/a20_evaluador_ea2.py"
VAL=(dataset6_CLINIC_0101_data dataset6_CLINIC_0102_data)
mapfile -t TEST < "$REPO/experiments/objetivo3/casos_ea2_test.txt"
RUNS=(run05a_mejor run05b_mejor)
ETAPA=${ETAPA:-}
VARIANTE=${VARIANTE:-base}
case "$ETAPA" in
    val) CSV=$OUT/a20_val.csv; CAND=$OUT/.candado_val ;;
    test) CSV=$OUT/a20_test_$VARIANTE.csv; CAND=$OUT/.candado_test_$VARIANTE ;;
    *) echo "ERROR: falta ETAPA=val o ETAPA=test"; exit 1 ;;
esac
case "$VARIANTE" in
    base) OPC=() ;;
    inter) OPC=() ;;
    suelo) OPC=(--suelo-simetrico) ;;
    sincabeza) OPC=(--excluir-cabeza-mm 20) ;;
    r08_10) OPC=(--r-min-mm 8 --r-max-mm 10) ;;
    r10_12) OPC=(--r-min-mm 10 --r-max-mm 12) ;;
    r12_14) OPC=(--r-min-mm 12 --r-max-mm 14) ;;
    r14_16) OPC=(--r-min-mm 14 --r-max-mm 16) ;;
    *) echo "ERROR: VARIANTE desconocida $VARIANTE"; exit 1 ;;
esac
module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
grep -q "Analisis exploratorio en prueba (DECLARADO" "$REPO/experiments/objetivo3/v2_plan.md" \
    || { echo "ERROR: v2_plan.md sin la declaracion del analisis exploratorio (git pull)"; exit 1; }
grep -q "2026-10-15 — Cierre de las" "$REPO/docs/01-decisiones.md" \
    || { echo "ERROR: 01-decisiones.md sin la entrada 2026-10-15 (git pull)"; exit 1; }
grep -q "suelo-simetrico" "$A20" || { echo "ERROR: a20 sin las variantes de 2026-10-15 (git pull)"; exit 1; }
for et in "${RUNS[@]}"; do
    for caso in "${TEST[@]}"; do
        ls "$DATA/obj3_pose/final/$et/a15_${caso}_${et}_s4_sintetica.nii.gz" >/dev/null 2>&1 \
            || { echo "ERROR: falta la corrida final de $et ($caso)"; exit 1; }
    done
done
mkdir -p "$OUT"
mkdir "$CAND" 2>/dev/null || { echo "ERROR: ya hay (o hubo) un job de $ETAPA/$VARIANTE: borra $CAND si fallo"; exit 1; }
rm -f "$CSV"
echo "inicio $(date -Is)  etapa $ETAPA  variante $VARIANTE  commit $(git -C "$REPO" rev-parse --short HEAD)"
echo "AVISO: evaluacion EXPLORATORIA y POSTERIOR de la version 2 (v2_plan.md, #182): no reemplaza a run04"
rc=0
if [ "$ETAPA" = val ]; then
    python -u "$A20" peters --npz "$DATA"/obj3_pose/peters_val/a19_*.npz --out "$CSV" || exit 1
    for et in "${RUNS[@]}"; do
        for caso in "${VAL[@]}"; do
            python -u "$A20" difusor --caso "$caso" --dir "$DATA/obj3_pose/delta/$et" --etiqueta "$et" \
                --out "$CSV" || exit 1
        done
        python -u "$A20" delta --csv "$CSV" --etiqueta "$et" || exit 1
        mv "$OUT/a20_delta.json" "$OUT/a20_delta_$et.json"
    done
else
    python -u "$A20" peters --npz "$DATA"/obj3_pose/peters_final/a19_*.npz --corrida-final "${OPC[@]}" \
        --out "$CSV" || exit 1
    python -u "$A20" copiapega --casos "${TEST[@]}" --hu 5371 --corrida-final "${OPC[@]}" --out "$CSV" || exit 1
    python -u "$A20" parametrico --casos "${TEST[@]}" --hu 5371 --corrida-final "${OPC[@]}" --out "$CSV" || exit 1
    for et in "${RUNS[@]}"; do
        for caso in "${TEST[@]}"; do
            INT=()
            [ "$VARIANTE" = inter ] && INT=(--interseccion "$DATA/obj3_pose/peters_final/a19_${caso}.npz")
            python -u "$A20" difusor --caso "$caso" --dir "$DATA/obj3_pose/final/$et" --etiqueta "$et" \
                --corrida-final "${OPC[@]}" "${INT[@]}" --out "$CSV" || { echo "ERROR $et $caso"; rc=1; }
        done
    done
fi
echo "fin $(date -Is)  rc=$rc"
exit $rc
