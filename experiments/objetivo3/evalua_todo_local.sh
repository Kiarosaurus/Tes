#!/bin/bash
# EVALUACION LOCAL de todo lo que dejo el script maestro (docs/01-decisiones.md 2026-11-21 (18)). Un comando, en WSL, con el venv activo:
#   source ~/venv-tesis/bin/activate && bash experiments/objetivo3/evalua_todo_local.sh
# Pide la contrasena de Khipu UNA vez por conexion (3 conexiones). Solo lee en Khipu; escribe en local.
set -u
R=${R:-/mnt/d/UTEC/CICLOX/Salvar-El-Ciclo/PFCII/metalsynth-pelvis}
T=${T:-/mnt/d/UTEC/CICLOX/Salvar-El-Ciclo/_plan_urgente_2026-11/tesis}
D=$R/experiments/objetivo3/outputs/obj3_pose/b_min
E=$R/experiments/objetivo3/outputs/eta_prueba
mkdir -p "$D" "$E"
echo "== 1/4 REPORTE de Khipu"
ssh khipu.utec.edu.pe 'cat ~/metalsynth/data/pipeline_textura/REPORTE.md' | tee "$T/REPORTE_pipeline.md"
echo "== 2/4 NIfTI de los brazos nuevos (sin marcas.npz)"
ssh khipu.utec.edu.pe 'cd ~/metalsynth/data/obj3_pose/b_min && tar cf - --exclude="*_marcas.npz" $(ls -d aux_T aux_P aux_A 2>/dev/null)' | tar xf - -C "$D"
echo "== 3/4 resultados de la corrida en prueba (a20)"
ssh khipu.utec.edu.pe 'cd ~/metalsynth/data/eta_prueba && tar cf - a20_test_base.csv a20_val.csv a20_delta_*.json 2>/dev/null' | tar xf - -C "$E"
ARMS=""; for a in aux_T aux_P aux_A; do [ -d "$D/$a" ] && ARMS="$ARMS $a"; done
echo "brazos nuevos disponibles:${ARMS:- ninguno}"
echo "== 4/4 evaluacion local"
if [ -n "$ARMS" ]; then
    cd "$R" && python3 experiments/objetivo3/d2_perfil_sintetico.py --base "$D" --puntos b_min_l0 $ARMS --out-dir experiments/objetivo3/outputs/d2_aux && head -9 experiments/objetivo3/outputs/d2_aux/d2_perfil.csv
    cd "$T" && METALSYNTH_REPO=$R python -I c4_eta.py --b-min "$D" --variantes b_min_l0 $ARMS --out c4/c4_aux_resumen.md && sed -n '/K = 48/,/^$/p' c4/c4_aux_resumen.md | head -14
    ARGS=(); for a in b_min_l0 $ARMS; do ARGS+=(--arm "$a=$D/$a"); done
    METALSYNTH_REPO=$R python -I c2b_ciego.py --sufijo _aux --arm run04_mejor=$R/experiments/objetivo3/outputs/obj3_pose/delta/run04_mejor --arm run04_mejor_p100_e0.3=$D/run04_mejor_p100_e0.3 "${ARGS[@]}"
    echo "Sesion a ciegas nueva: $T/c2/ciego_b_aux.html (no abras la clave)"
fi
if [ -f "$E/a20_test_base.csv" ]; then
    cd "$R" && python3 experiments/objetivo3/a24_contrastes.py --csv "$E/a20_test_base.csv" --etiqueta run04_mejor_p100_e0.3 --delta-json "$E/a20_delta_run04_mejor_p100_e0.3.json" --out-dir experiments/objetivo3/outputs/a24_eta | tail -30
fi
echo "listo. Pegale a Claude: REPORTE, D2, C4 (K=48) y la salida de a24."
