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
#   bash scripts/khipu_elegir_gpu.sh experiments/objetivo3/a15_cotejo_run04.sbatch 25 4
#   bash scripts/khipu_elegir_gpu.sh experiments/objetivo3/a15_cotejo_run04.sbatch 25 4 -- dataset6_CLINIC_0102_data
#   PARTICIONES="gpu lenovo" bash scripts/khipu_elegir_gpu.sh ...   # solo esas particiones
#
# <minutos_en_A100>: cuanto tardaria el job en una A100 entera (estimalo de una corrida anterior).
# [GB_minimos]: memoria de GPU que necesita el job; descarta las opciones con menos (por omision 4).
# La cuenta y la QoS salen del .sbatch (#SBATCH --account / --qos); este script no las cambia.
#
# AVISO: las velocidades relativas son APROXIMADAS (fraccion de A100 para las MIG; RTX A6000 ~0.6; la
# tesla (T4, 15 GB) no esta medida y se toma 0.3; un tipo desconocido tambien 0.3). Los shards comparten la GPU con
# otros jobs: su velocidad real depende de quien mas este corriendo, y se penalizan (x0.5). Un shard
# no reserva memoria de GPU: la columna GB es la de la GPU entera, no la garantizada. La hora de inicio
# de `--test-only` es una estimacion de Slurm basada en los limites de tiempo de los demas: puede
# adelantarse o atrasarse. QoS a-tesis: maximo 40 shards por usuario.
#
# TRUCO QUE MAS AYUDA: pedir un --time realista. Slurm mete jobs cortos en los huecos (backfill). Este
# script ya pide para cada opcion --time = 2 x la duracion estimada (minimo 30 min).
#
# TOPES DE TIEMPO (2026-10-11): `sbatch --test-only` NO aplica el MaxWall de la QoS (run03 quedo en espera
# por QOSMaxWallDurationPerJobLimit con una opcion que el script daba por buena). El tope se lee de
# `sacctmgr show qos <qos del .sbatch>` y del MaxTime de cada particion (`sinfo %l`); manda el menor.
# Si no se puede leer, se fija a mano: TOPE_MIN=1440 bash scripts/khipu_elegir_gpu.sh ...
# Nada se descarta; la columna NOTA dice que pasa:
#   TOPE    el doble de la duracion no cabe, pero la duracion si: --time se recorta al tope.
#   EXCEDE  la duracion estimada ya pasa el tope: no se recomienda (solo con --reanudar y varios jobs).
#   GB?     memoria de GPU desconocida para ese tipo: no se recomienda (verificar con nvidia-smi).

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
        tesla)         echo "15 0.30" ;;   # Tesla T4, 15360 MiB (nvidia-smi en g001, 2026-10-11); velocidad NO medida
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

# Duracion de Slurm (infinite, M, H:M:S, D-H:M:S, D-H) -> minutos; vacio si no hay tope.
a_min() {
    local v=${1:-}
    case "$v" in ''|infinite|UNLIMITED|INVALID|Partition_Limit) echo ""; return ;; esac
    local d=0 h=0 m=0 conDia=0
    if [[ "$v" == *-* ]]; then d=${v%%-*}; v=${v#*-}; conDia=1; fi
    IFS=':' read -ra p <<< "$v"
    case ${#p[@]} in
        1) if [ "$conDia" = 1 ]; then h=${p[0]}; else m=${p[0]}; fi ;;
        2) if [ "$conDia" = 1 ]; then h=${p[0]}; m=${p[1]}; else m=${p[0]}; fi ;;
        *) h=${p[0]}; m=${p[1]} ;;
    esac
    echo $(( 10#$d * 1440 + 10#$h * 60 + 10#$m ))
}

QOS=$(grep -m1 -oP '^#SBATCH\s+--qos[= ]\K\S+' "$SB")
if [ -n "${TOPE_MIN:-}" ]; then
    TOPE_QOS=$TOPE_MIN; origen="TOPE_MIN"
elif [ -n "$QOS" ]; then
    TOPE_QOS=$(a_min "$(sacctmgr -n -P show qos "$QOS" format=MaxWall 2>/dev/null | head -1)"); origen="QoS $QOS"
else
    TOPE_QOS=""; origen=""
fi
if [ -n "$TOPE_QOS" ]; then
    echo "Tope de tiempo: $TOPE_QOS min ($origen), y el MaxTime de cada particion."
else
    echo "AVISO: no se pudo leer el tope de la QoS. Fijalo con TOPE_MIN=<minutos> si lo conoces."
fi

ahora=$(date +%s)
printf '%-12s %-22s %4s %7s %-12s %-12s %-11s %s\n' PARTICION OPCION GB DUR_MIN INICIO FIN TIME_PEDIDO NOTA
filas=""
rechazos=""
while IFS='|' read -r part gres gb vel; do
    if [ "$gb" != 0 ] && [ "$gb" -lt "$GB_MIN" ]; then continue; fi
    dur=$(awk -v m="$MIN_A100" -v v="$vel" 'BEGIN{printf "%d", m/v + 0.999}')
    pedir=$(( dur * 2 < 30 ? 30 : dur * 2 ))
    tope=$TOPE_QOS
    tp=$(a_min "$(sinfo -h -p "$part" -o %l | head -1)")
    if [ -n "$tp" ] && { [ -z "$tope" ] || [ "$tp" -lt "$tope" ]; }; then tope=$tp; fi
    nota=""
    if [ -n "$tope" ] && [ "$pedir" -gt "$tope" ]; then
        if [ "$dur" -le "$tope" ]; then pedir=$tope; nota="TOPE"; else nota="EXCEDE"; fi
    fi
    [ "$gb" = 0 ] && nota="${nota:+$nota,}GB?"
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
    filas+="$fin_s|$part|$gres|$gb|$dur|$(date -d @"$ini_s" '+%m-%d %H:%M')|$(date -d @"$fin_s" '+%m-%d %H:%M')|$t|${nota:--}"$'\n'
done <<< "$opciones"

echo "$filas" | grep -v '^$' | sort -t'|' -k1,1n | while IFS='|' read -r _ p g gb d i f t n; do
    printf '%-12s %-22s %4s %7s %-12s %-12s %-11s %s\n' "$p" "$g" "$gb" "$d" "$i" "$f" "$t" "$n"
done
[ -n "$rechazos" ] && { echo; printf '%s' "$rechazos"; }

# Tipos de GPU sin memoria conocida en datos_tipo(): comando para medirla y pasarselo a Claude.
CUENTA=$(grep -m1 -oP '^#SBATCH\s+(--account|-A)[= ]\K\S+' "$SB")
desconocidos=$(echo "$opciones" | awk -F'|' '$3 == 0 {split($2, g, ":"); if (!(g[2] in v)) {v[g[2]] = 1; print $1 "|" g[1] "|" g[2]}}')
if [ -n "$desconocidos" ]; then
    echo
    echo "AVISO: tipos de GPU sin memoria conocida (salen con GB?). Corre esto y pasale la salida a Claude"
    echo "para agregarlos a datos_tipo() en scripts/khipu_elegir_gpu.sh:"
    while IFS='|' read -r pt cl tp; do
        if [ "$cl" = shard ]; then gr="shard:$tp:1"; else gr="gpu:$tp:1"; fi
        echo "  srun -p $pt ${CUENTA:+-A $CUENTA }--gres=$gr -t 5 nvidia-smi --query-gpu=name,memory.total --format=csv"
    done <<< "$desconocidos"
fi

# Se recomienda la que termina antes entre las que caben en el tope y tienen memoria conocida.
mejor=$(echo "$filas" | grep -v '^$' | awk -F'|' '$9 == "-" || $9 == "TOPE"' | sort -t'|' -k1,1n | head -n 1)
[ -z "$mejor" ] && { echo "Ninguna opcion recomendable (todas EXCEDE o GB?)."; exit 1; }
IFS='|' read -r _ p g _ _ _ f t _ <<< "$mejor"
echo
echo "Recomendada: -p $p $g (termina ~$f). Para enviarla:"
echo "  J=\$(sbatch --parsable -p $p --time=$t --gres=$g $SB ${EXTRA[*]}); echo \$J"
