#!/bin/bash
# Elige la GPU de Khipu con la que un job TERMINA antes (no la que empieza antes).
#
# Para cada opcion de --gres corre `sbatch --test-only` (no envia nada), lee la hora de inicio que estima
# Slurm y le suma la duracion esperada en esa GPU. Imprime una tabla ordenada por hora de fin y el
# comando listo para enviar con la mejor opcion.
#
# USO (en Khipu, desde ~/metalsynth):
#   bash khipu_elegir_gpu.sh <archivo.sbatch> <minutos_en_A100> [GB_minimos] [-- args del sbatch]
#   bash khipu_elegir_gpu.sh experiments/objetivo3/a15_cotejo.sbatch 25 4
#   bash khipu_elegir_gpu.sh experiments/objetivo3/a15_cotejo.sbatch 25 4 -- dataset6_CLINIC_0102_data
#
# <minutos_en_A100>: cuanto tardaria el job en una A100 entera (estimalo de una corrida anterior).
# [GB_minimos]: memoria de GPU que necesita el job; descarta las opciones con menos (por omision 4).
#
# AVISO: las velocidades relativas son APROXIMADAS (fraccion de A100 para las MIG; RTX A6000 ~0.6; la
# tesla no esta medida y se toma 0.3). Los shards comparten la GPU con otros jobs: su velocidad real
# depende de quien mas este corriendo, y se penalizan (x0.5). La hora de inicio de `--test-only` es una
# estimacion de Slurm basada en los limites de tiempo de los demas: puede adelantarse o atrasarse.
#
# TRUCO QUE MAS AYUDA: pedir un --time realista. Slurm mete jobs cortos en los huecos (backfill). Este
# script ya pide para cada opcion --time = 2 x la duracion estimada (minimo 30 min).

set -u
SB=${1:?falta el .sbatch}
MIN_A100=${2:?faltan los minutos estimados en A100}
GB_MIN=${3:-4}
shift $(( $# >= 3 ? 3 : $# ))
[ "${1:-}" = "--" ] && shift
EXTRA=("$@")

# opcion | memoria GB | velocidad relativa a A100 entera
OPCIONES="gpu:a100:1|40|1.00
gpu:rtxa6000:1|48|0.60
gpu:a100_3g.20gb:1|20|0.43
gpu:a100_2g.10gb:1|10|0.28
gpu:a100_1g.5gb:1|5|0.14
gpu:tesla:1|0|0.30
shard:rtxa6000:4|48|0.30
shard:a100_1g.5gb:8|5|0.07"

ahora=$(date +%s)
printf '%-22s %6s %8s %-17s %-17s %s\n' OPCION GB DUR_MIN INICIO FIN TIME_PEDIDO
filas=""
while IFS='|' read -r gres gb vel; do
    if [ "$gb" != 0 ] && [ "$gb" -lt "$GB_MIN" ]; then continue; fi
    dur=$(awk -v m="$MIN_A100" -v v="$vel" 'BEGIN{printf "%d", m/v + 0.999}')
    pedir=$(( dur * 2 < 30 ? 30 : dur * 2 ))
    t=$(printf '%02d:%02d:00' $((pedir / 60)) $((pedir % 60)))
    salida=$(sbatch --test-only --time="$t" --gres="$gres" "$SB" "${EXTRA[@]}" 2>&1)
    inicio=$(echo "$salida" | grep -o 'start at [0-9T:-]*' | awk '{print $3}')
    if [ -z "$inicio" ]; then
        printf '%-22s %6s %8s %s\n' "$gres" "$gb" "$dur" "RECHAZADO: $(echo "$salida" | tail -1)"
        continue
    fi
    ini_s=$(date -d "$inicio" +%s)
    [ "$ini_s" -lt "$ahora" ] && ini_s=$ahora
    fin_s=$(( ini_s + dur * 60 ))
    filas+="$fin_s|$gres|$gb|$dur|$(date -d @"$ini_s" '+%m-%d %H:%M')|$(date -d @"$fin_s" '+%m-%d %H:%M')|$t"$'\n'
done <<< "$OPCIONES"

echo "$filas" | grep -v '^$' | sort -t'|' -k1,1n | while IFS='|' read -r _ g gb d i f t; do
    printf '%-22s %6s %8s %-17s %-17s %s\n' "$g" "$gb" "$d" "$i" "$f" "$t"
done
mejor=$(echo "$filas" | grep -v '^$' | sort -t'|' -k1,1n | head -n 1)
[ -z "$mejor" ] && { echo "Ninguna opcion valida."; exit 1; }
IFS='|' read -r _ g _ _ _ f t <<< "$mejor"
echo
echo "Recomendada: $g (termina ~$f). Para enviarla:"
echo "  J=\$(sbatch --parsable --time=$t --gres=$g $SB ${EXTRA[*]}); echo \$J"
