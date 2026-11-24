#!/bin/bash
# SCRIPT MAESTRO DESATENDIDO (docs/01-decisiones.md 2026-11-21 (18) y (18-a)). EXPLORATORIO, POST-HOC.
# Un solo job en la T4 que corre, en orden y sin intervencion: metricas de referencia -> humos de T, P y A -> corrida en prueba de 100:0.3 (+ a20 en
# segundo plano) -> T -> P -> A (solo si queda tiempo). Cada etapa es idempotente y deja una fila en estado.tsv. Una etapa fallida marca SALTADAS las que
# dependen de ella; las independientes siguen. Una etapa no arranca si no cabe antes del corte (DEADLINE, por omision dom 2026-11-22 11:00).
# Al final escribe $OUT/REPORTE.md aunque algo haya fallado.
#
# USO (desde ~/metalsynth, rama exp/textura-percep-adv, tras git pull):
#   un solo job (T4):  sbatch experiments/objetivo3/pipeline_textura.sbatch
#   DOS jobs en paralelo (decision (20)): GRUPO=test en la T4 (GEN_TEST + a20) y GRUPO=entrena en A100/A6000 (humos, control C, T, P, A):
#     sbatch --export=ALL,GRUPO=test experiments/objetivo3/pipeline_textura.sbatch
#     sbatch -p all --gres=gpu:a100:1 --export=ALL,GRUPO=entrena,FACTOR=25 experiments/objetivo3/pipeline_textura.sbatch
# Para relanzar tras un corte: el mismo comando (las etapas OK se saltan). SALTAR=GEN_TEST,TRAIN_A omite etapas por nombre. Otro corte: DEADLINE=<epoch> sbatch --export=ALL,DEADLINE=...
# Salida: $HOME/metalsynth/data/pipeline_textura/{estado.tsv, REPORTE.md, res/, smoke_*.log, lambda_*.txt}
#SBATCH --job-name=pipetex
#SBATCH --partition=all
#SBATCH --account=tesis
#SBATCH --qos=a-tesis
#SBATCH --gres=gpu:tesla:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=14:00:00
#SBATCH --output=%x_%j.log

set -u
DATA=$HOME/metalsynth/data
REPO=$HOME/metalsynth
OBJ3=$REPO/experiments/objetivo3
OUT=${OUT:-$DATA/pipeline_textura}
RES=$OUT/res
mkdir -p "$RES"
GRUPO=${GRUPO:-todo}   # todo | test (T4: GEN_TEST + a20) | entrena (A100/A6000: humos, control C, T, P, A)
FACTOR=${FACTOR:-100}  # % del tiempo estimado (T4 = 100; A100 ~ 25) para la guarda de reloj
ESTADO=$OUT/estado_$GRUPO.tsv
touch "$ESTADO"
DEADLINE=${DEADLINE:-$(date -d "2026-11-22 11:00" +%s)}
INIT=$DATA/a7/run04/mejor.pt
MAN=$OBJ3/a5_manifiesto_train_run04.csv
B=$DATA/obj3_pose/b_min

module load miniconda/3.0
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate totalseg || { echo "ERROR: no se activo el entorno"; exit 1; }
python -c "import torch; assert torch.cuda.is_available(); print('torch', torch.__version__)" || { echo "ERROR: sin cuda"; exit 1; }
for f in "$INIT" "$MAN" "$REPO/src/renderizador/texturas.py" "$OBJ3/a15_final_eta.sbatch" "$OBJ3/a20_eta_test.sbatch" "$OBJ3/a15_val_ckpt.sbatch"; do
    [ -f "$f" ] || { echo "ERROR: falta $f (git pull; rama exp/textura-percep-adv)"; exit 1; }
done
echo "inicio $(date -Is)  nodo $(hostname)  commit $(git -C "$REPO" rev-parse --short HEAD)  corte $(date -d @$DEADLINE -Is)"

estado_de() { awk -F'\t' -v n="$1" '$1==n{s=$2} END{print s}' "$ESTADO"; }
registra() { printf '%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "${3:-}" "$(date -Is)" "${4:-}" >> "$ESTADO"; }

# etapa NOMBRE DEPENDENCIAS(coma) EST_MIN comando...
etapa() {
    local n=$1 deps=$2 est=$3
    shift 3
    est=$(( est * FACTOR / 100 ))
    if [ "$(estado_de "$n")" = OK ]; then echo "[$n] ya OK, se salta"; return 0; fi
    case ",${SALTAR:-}," in
        *",$n,"*) registra "$n" SALTADA "" "omitida por la autora (SALTAR)"; echo "[$n] omitida (SALTAR)"; return 0;;
    esac
    local d
    for d in $(echo "$deps" | tr ',' ' '); do
        [ -z "$d" ] && continue
        if [ "$(estado_de "$d")" != OK ]; then
            registra "$n" SALTADA "" "depende de $d (estado: $(estado_de "$d"))"
            echo "[$n] SALTADA: depende de $d"
            return 0
        fi
    done
    if [ $(( $(date +%s) + est * 60 )) -gt "$DEADLINE" ]; then
        registra "$n" SALTADA "" "reloj: no cabe antes del corte (estimado $est min)"
        echo "[$n] SALTADA por reloj"
        return 0
    fi
    echo; echo "##### [$n] $(date -Is)"
    local t0
    t0=$(date -Is)
    "$@"
    local rc=$?
    if [ $rc -eq 0 ]; then registra "$n" OK "$t0" ""; else registra "$n" FALLO "$t0" "rc=$rc"; fi
    return 0
}

args_comunes() {  # imprime los argumentos comunes de entrenar.py (ajuste fino de run04_mejor, como B)
    echo --cache "$DATA/a1b_cache" --particion "$REPO/experiments/objetivo1/p1_particion.csv" --manifiesto "$MAN" \
         --manifiesto-val "$OBJ3/a5_manifiesto_val.csv" --lr 5e-5 --base 64 --lado 256 --lotes-val 16 --cada-ckpt 250 \
         --trabajadores "${SLURM_CPUS_PER_TASK:-4}" --preinscrito --init-modelo "$INIT"
}

lista_dirs() {  # directorios a15 de validacion que existen, para metricas y cascaras
    local d
    for d in "$DATA/obj3_pose/delta/run04_mejor" "$B/b_min_l0" "$B/b_min_l0.8_t1000" "$B/b_min_l3_t300" "$B/run04_mejor_p100_e0.3" "$B/aux_C" "$B/aux_T" "$B/aux_P" "$B/aux_A"; do
        [ -d "$d" ] && echo "$d"
    done
}

ref_metricas() {
    local rc=0 d k
    for d in "$DATA/obj3_pose/delta/run04_mejor" "$B/b_min_l0" "$B/b_min_l0.8_t1000" "$B/b_min_l3_t300" "$B/run04_mejor_p100_e0.3"; do
        [ -d "$d" ] || { echo "AVISO: falta $d"; continue; }
        k=$(basename "$d")
        python "$OBJ3/textura_metricas.py" --dir "$d" --etiqueta "$k" --out "$RES/$k.json" || rc=1
    done
    python "$OBJ3/d2_perfil_sintetico.py" --base "$B" --puntos b_min_l0 b_min_l0.8_t1000 b_min_l3_t300 run04_mejor_p100_e0.3 \
        --out-dir "$RES/d2_ref" && cp "$RES/d2_ref/d2_perfil.csv" "$RES/d2_perfil.csv" || echo "AVISO: D2 no disponible en Khipu (se hace en local)"
    return $rc
}

smoke() {  # T | P | A
    local V=$1
    local S=$DATA/a7/aux_smoke_$V LOG=$OUT/smoke_$V.log lote rc=1 ARGS
    case $V in T) ARGS="--aux-tex 1.0";; P) ARGS="--aux-per 1.0";; A) ARGS="--aux-adv 0.01";; esac
    for lote in 16 8; do
        rm -rf "$S"
        python -u "$REPO/src/renderizador/entrenar.py" $(args_comunes) --out "$S" --pasos 100 --cada 100 --lote $lote $ARGS > "$LOG" 2>&1
        rc=$?
        if grep -qi "out of memory" "$LOG"; then echo "[smoke $V] OOM con lote $lote"; rc=1; continue; fi
        break
    done
    [ $rc -eq 0 ] || return 1
    echo $lote > "$OUT/lote_$V.txt"
    case $V in
        T) python "$OBJ3/pipeline_lambda.py" "$LOG" tex > "$OUT/lambda_T.txt" || return 1;;
        P) python "$OBJ3/pipeline_lambda.py" "$LOG" per > "$OUT/lambda_P.txt" || return 1;;
        A) python - "$LOG" <<'EOF' || return 1
import math, re, sys
lad = ld = None
for l in open(sys.argv[1], encoding='utf-8', errors='replace'):
    m = re.search(r'^paso \d+/\d+ .*L_adv ([0-9.eE+-]+) L_D ([0-9.eE+-]+)', l)
    if m:
        lad, ld = float(m.group(1)), float(m.group(2))
ok = lad is not None and math.isfinite(lad) and math.isfinite(ld) and 0.1 <= ld <= 3.0
print('humo A: L_adv', lad, 'L_D', ld, '->', 'OK' if ok else 'FALLA (NaN o L_D fuera de [0.1, 3])')
sys.exit(0 if ok else 1)
EOF
        ;;
    esac
    echo "[smoke $V] ok, lote $lote"
}

gen_test() { bash "$OBJ3/a15_final_eta.sbatch"; }

train() {  # T | P | A
    local V=$1
    local S=$DATA/a7/aux_$V lote ARGS
    if [ "$V" = C ]; then lote=$(cat "$OUT/lote_T.txt" 2>/dev/null || echo 16); else lote=$(cat "$OUT/lote_$V.txt"); fi
    case $V in T) ARGS="--aux-tex $(cat "$OUT/lambda_T.txt")";; P) ARGS="--aux-per $(cat "$OUT/lambda_P.txt")";; A) ARGS="--aux-adv 0.01";; C) ARGS="";; esac
    # reanudable: si la ventana del job se corto, la siguiente continua desde ckpt.pt (la carpeta NO se borra)
    python -u "$REPO/src/renderizador/entrenar.py" $(args_comunes) --out "$S" --pasos 3000 --cada 250 --lote "$lote" --reanudar $ARGS >> "$OUT/train_$V.log" 2>&1
    local rc=$?
    grep -q "^LISTO" "$OUT/train_$V.log" && [ -f "$S/ckpt.pt" ] || return 1
    return $rc
}

evalua() {  # T | P | A
    local V=$1
    ETIQ=aux_$V PT=$DATA/a7/aux_$V/ckpt.pt CORTES=0 bash "$OBJ3/a15_val_ckpt.sbatch" > "$OUT/eval_$V.log" 2>&1
}

metricas() {  # T | P | A
    local V=$1 rc=0
    python "$OBJ3/textura_metricas.py" --dir "$B/aux_$V" --etiqueta "aux_$V" --out "$RES/aux_$V.json" || rc=1
    python "$OBJ3/d2_perfil_sintetico.py" --base "$B" --puntos "aux_$V" --out-dir "$RES/d2_aux_$V" || echo "AVISO: D2 no disponible (se hace en local)"
    return $rc
}

# ---- orden fijado en (18) punto 6 y (20) ----
if [ "$GRUPO" != test ]; then
    etapa REF "" 20 ref_metricas
    etapa SMOKE_T "" 15 smoke T
    etapa SMOKE_P "" 15 smoke P
    etapa SMOKE_A "" 15 smoke A
fi
A20PID=""
if [ "$GRUPO" != entrena ]; then
    etapa GEN_TEST "" 340 gen_test
    if [ "$(estado_de GEN_TEST)" = OK ] && [ "$(estado_de A20_TEST)" != OK ]; then
        ( bash "$OBJ3/a20_eta_test.sbatch" > "$OUT/a20_eta.log" 2>&1; echo $? > "$OUT/a20_eta.rc" ) &
        A20PID=$!
        echo "a20 de la corrida en prueba lanzado en segundo plano (pid $A20PID)"
    fi
fi
if [ "$GRUPO" != test ]; then
    if [ "$GRUPO" = entrena ]; then   # control del MISMO hardware (decision (20))
        etapa TRAIN_C "" 145 train C
        etapa EVAL_C TRAIN_C 25 evalua C
        etapa MET_C EVAL_C 10 metricas C
    fi
    etapa TRAIN_T SMOKE_T 145 train T
    etapa EVAL_T TRAIN_T 25 evalua T
    etapa MET_T EVAL_T 10 metricas T
    etapa TRAIN_P SMOKE_P 145 train P
    etapa EVAL_P TRAIN_P 25 evalua P
    etapa MET_P EVAL_P 10 metricas P
    etapa TRAIN_A SMOKE_A 215 train A
    etapa EVAL_A TRAIN_A 25 evalua A
    etapa MET_A EVAL_A 10 metricas A
fi
if [ -n "$A20PID" ]; then
    wait "$A20PID"
    if [ "$(cat "$OUT/a20_eta.rc" 2>/dev/null)" = 0 ]; then registra A20_TEST OK "" "a20 de 100:0.3 en prueba"; else registra A20_TEST FALLO "" "ver a20_eta.log"; fi
fi
# resumen final (siempre)
python "$OBJ3/veredicto_cascaras.py" --repo "$REPO" --data "$DATA/extracted" --dirs $(lista_dirs) --out "$RES/veredicto_cascaras.md" > /dev/null 2>&1 || echo "AVISO: cascaras no disponibles"
python "$OBJ3/pipeline_reporte.py" "$OUT" || true
echo "fin $(date -Is)"
exit 0
