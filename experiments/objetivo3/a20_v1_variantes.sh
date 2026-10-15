#!/bin/bash
# Variantes POSTERIORES de DEC 2026-10-15 sobre la corrida final de la version 1 (run04_mejor), en LOCAL: los NIfTI
# de run04 estan en outputs/obj3_pose/final/. Mismas variantes que a20_v2.sbatch. Salida:
# outputs/obj3_pose/a20_variantes/a20_test_<VARIANTE>.csv. Uso: bash a20_v1_variantes.sh [variantes...]
cd "$(dirname "$0")"
OUT=outputs/obj3_pose/a20_variantes
mkdir -p "$OUT"
mapfile -t TEST < <(tr -d '\r' < casos_ea2_test.txt)   # el checkout de Windows trae CRLF
VARS=("$@"); [ ${#VARS[@]} -eq 0 ] && VARS=(base inter suelo sincabeza r08_10 r10_12 r12_14 r14_16)
for v in "${VARS[@]}"; do
    case $v in
        base|inter) OPC=() ;; suelo) OPC=(--suelo-simetrico) ;; sincabeza) OPC=(--excluir-cabeza-mm 20) ;;
        r08_10) OPC=(--r-min-mm 8 --r-max-mm 10) ;; r10_12) OPC=(--r-min-mm 10 --r-max-mm 12) ;;
        r12_14) OPC=(--r-min-mm 12 --r-max-mm 14) ;; r14_16) OPC=(--r-min-mm 14 --r-max-mm 16) ;;
        *) echo "variante desconocida $v"; exit 1 ;;
    esac
    CSV=$OUT/a20_test_$v.csv
    rm -f "$CSV"
    echo "=== $v $(date -Is)"
    python -W ignore a20_evaluador_ea2.py peters --npz outputs/obj3_pose/peters_final/a19_*.npz --corrida-final "${OPC[@]}" --out "$CSV" > /dev/null || exit 1
    python -W ignore a20_evaluador_ea2.py parametrico --casos "${TEST[@]}" --hu 5371 --corrida-final "${OPC[@]}" --out "$CSV" > /dev/null || exit 1
    python -W ignore a20_evaluador_ea2.py copiapega --casos "${TEST[@]}" --hu 5371 --corrida-final "${OPC[@]}" --out "$CSV" > /dev/null || exit 1
    for caso in "${TEST[@]}"; do
        INT=(); [ "$v" = inter ] && INT=(--interseccion "outputs/obj3_pose/peters_final/a19_${caso}.npz")
        python -W ignore a20_evaluador_ea2.py difusor --caso "$caso" --dir outputs/obj3_pose/final/run04_mejor \
            --etiqueta run04_mejor --corrida-final "${OPC[@]}" "${INT[@]}" --out "$CSV" > /dev/null || exit 1
    done
done
echo "fin $(date -Is)"
