#!/bin/bash
# Elige la GPU de Khipu con la que un job TERMINA antes (no la que empieza antes).
#
# Lee de `sinfo` todas las particiones y tipos de GPU/shard del cluster, y para cada par
# (particion, --gres) corre `sbatch --test-only` (no envia nada). Lee la hora de inicio que estima
# Slurm y le suma la duracion esperada en esa GPU. Imprime una tabla ordenada por hora de fin y el
# comando listo para enviar con la mejor opcion. Las particiones a las que tu cuenta no puede entrar,
# o cuyo MaxTime es menor que lo pedido, salen como RECHAZADO.
#
# USO (en Khipu, desde ~/metalsynth):
#   bash scripts/khipu_elegir_gpu.sh <archivo.sbatch> <minutos_en_A100> [GB_minimos] [-- args del sbatch]
#   bash scripts/khipu_elegir_gpu.sh experiments/objetivo3/a15_cotejo.sbatch 25 4
#   bash scripts/khipu_elegir_gpu.sh experiments/objetivo3/a15_cotejo.sbatch 25 4 -- dataset6_CLINIC_0102_data
#   PARTICIONES="gpu lenovo" bash scripts/khipu_elegir_gpu.sh ...   # solo esas particiones
#
# <minutos_en_A100>: cuanto tardaria el job en una A100 entera (estimalo de una corrida anterior).
# [GB_minimos]: memoria de GPU que necesita el job; descarta las opciones con menos (por omision 4).
# La cuenta y la QoS salen del .sbatch (#SBATCH --account / --qos); este script no las cambia.
#
# AVISO: las velocidades relativas son APROXIMADAS (fraccion de A100 para las MIG; RTX A6000 ~0.6; la
# tesla no esta medida y se toma 0.3; un tipo desconocido tambien 0.3). Los shards comparten la GPU con
# otros jobs: su velocidad real depende de quien mas este corriendo, y se penalizan (x0.5). Un shard
# no reserva memoria de GPU: la columna GB es la de la GPU entera, no la garantizada. La hora de inicio
# de `--test-only` es una estimacion de Slurm basada en los limites de tiempo de los demas: puede
# adelantarse o atrasarse. QoS a-tesis: maximo 40 shards por usuario.
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

# tipo -> "memoria_GB velocidad_relativa_a_A100"
datos_tipo() {
    case "$1" in
        a100)          echo "40 1.00" ;;
        rtxa6000)      echo "48 0.60" ;;
        a100_3g.20gb)  echo "20 0.43" ;;
        a100_2g.10gb)  echo "10 0.28" ;;
        a100_1g.5gb)   echo "5 0.14" ;;
        tesla)         echo "0 0.30" ;;
        *)             echo "0 0.30" ;;
    esac
}

# Opciones (particion|gres|GB|velocidad) desde sinfo, sin repetir.
opciones=$(sinfo -h -o "%P|%G" | sort -u | while IFS='|' read -r part gres; do
    part=${part%\*}
    if [ -n "${PARTICIONES:-}" ] && ! [[ " $PARTICIONES " == *" $part "* ]]; then continue; fi
    [ "$gres" = "(null)" ] && continue
    IFS=',' read -ra toks <<< "$gres"
    for tok in "${toks[@]}"; do
        clase=${tok%%:*}; resto=${tok#*:}; tipo=${resto%%:*}
        read -r gb vel <<< "$(datos_tipo "$tipo")"
        if [ "$clase" = gpu ]; then
            echo "$part|gpu:$tipo:1|$gb|$vel"
        elif [ "$clase" = shard ]; then
            n=8; [ "$tipo" = rtxa6000 ] && n=4
            echo "$part|shard:$tipo:$n|$gb|$(awk -v v="$vel" 'BEGIN{printf "%.3f", v*0.5}')"
        fi
    done
done | sort -u)

[ -z "$opciones" ] && { echo "sinfo no devolvio GPUs."; exit 1; }

ahora=$(date +%s)
printf '%-12s %-22s %4s %7s %-12s %-12s %s\n' PARTICION OPCION GB DUR_MIN INICIO FIN TIME_PEDIDO
filas=""
rechazos=""
while IFS='|' read -r part gres gb vel; do
    if [ "$gb" != 0 ] && [ "$gb" -lt "$GB_MIN" ]; then continue; fi
    dur=$(awk -v m="$MIN_A100" -v v="$vel" 'BEGIN{printf "%d", m/v + 0.999}')
    pedir=$(( dur * 2 < 30 ? 30 : dur * 2 ))
    t=$(printf '%02d:%02d:00' $((pedir / 60)) $((pedir % 60)))
    salida=$(sbatch --test-only -p "$part" --time="$t" --gres="$gres" "$SB" "${EXTRA[@]}" 2>&1)
    inicio=$(echo "$salida" | grep -o 'start at [0-9T:-]*' | awk '{print $3}')
    if [ -z "$inicio" ]; then
        rechazos+="$(printf '%-12s %-22s %s' "$part" "$gres" "RECHAZADO: $(echo "$salida" | tail -1 | cut -c1-90)")"$'\n'
        continue
    fi
    ini_s=$(date -d "$inicio" +%s)
    [ "$ini_s" -lt "$ahora" ] && ini_s=$ahora
    fin_s=$(( ini_s + dur * 60 ))
    filas+="$fin_s|$part|$gres|$gb|$dur|$(date -d @"$ini_s" '+%m-%d %H:%M')|$(date -d @"$fin_s" '+%m-%d %H:%M')|$t"$'\n'
done <<< "$opciones"

echo "$filas" | grep -v '^$' | sort -t'|' -k1,1n | while IFS='|' read -r _ p g gb d i f t; do
    printf '%-12s %-22s %4s %7s %-12s %-12s %s\n' "$p" "$g" "$gb" "$d" "$i" "$f" "$t"
done
[ -n "$rechazos" ] && { echo; printf '%s' "$rechazos"; }

mejor=$(echo "$filas" | grep -v '^$' | sort -t'|' -k1,1n | head -n 1)
[ -z "$mejor" ] && { echo "Ninguna opcion valida."; exit 1; }
IFS='|' read -r _ p g _ _ _ f t <<< "$mejor"
echo
echo "Recomendada: -p $p $g (termina ~$f). Para enviarla:"
echo "  J=\$(sbatch --parsable -p $p --time=$t --gres=$g $SB ${EXTRA[*]}); echo \$J"
