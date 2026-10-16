#!/bin/bash
# Lanza UN revisor de /ciclo-redaccion con Codex (OpenAI) en vez de con un subagente de Claude (autora, 2026-10-16:
# ahorrar uso de Claude; la cuota de OpenAI se puede usar).
#
# USO:  bash scripts/codex_revisor.sh <guia|estilo|trazabilidad> <seccion> <rNN> [contexto extra]
#   ENCARGO=redaccion/ENCARGO_2026-10-16.md bash scripts/codex_revisor.sh guia capitulo3 r27
#
# - Codex corre con `-C redaccion/rondas -s workspace-write`: lee todo el repositorio pero SOLO puede escribir en
#   `redaccion/rondas/` (probado 2026-10-16: escribir en `redaccion/` queda bloqueado).
# - El rol sale de `.claude/agents/<agente>.md`; las reglas, de `AGENTS.md`, `CLAUDE.md` y `overleaf/CLAUDE.md`.
# - Respuesta previa: la `<seccion>-r*-respuesta.md` de numero mas alto menor que rNN, si existe.
# - Log completo en `redaccion/.build/codex/` (ignorado por git).
# - Sale con 0 e imprime "<ruta> alta=N media=N baja=N" si el reporte existe; con 1 si no (el orquestador lanza
#   entonces el subagente de Claude equivalente).
set -o pipefail
cd "$(dirname "$0")/.." || exit 1
TIPO=$1; SEC=$2; R=$3; EXTRA=${4:-}
case "$TIPO" in
    guia) AGENTE=revisor-guia-cs ;;
    estilo) AGENTE=revisor-estilo ;;
    trazabilidad) AGENTE=auditor-trazabilidad ;;
    *) echo "uso: $0 <guia|estilo|trazabilidad> <seccion> <rNN> [contexto]"; exit 2 ;;
esac
[ -n "$SEC" ] && [[ "$R" =~ ^r[0-9]+$ ]] || { echo "uso: $0 <tipo> <seccion> <rNN>"; exit 2; }
command -v codex >/dev/null || { echo "ERROR: codex no esta en el PATH"; exit 1; }
LINT=redaccion/rondas/$SEC-$R-lint.md
[ -f "$LINT" ] || { echo "ERROR: falta $LINT (corre el lint antes)"; exit 1; }
REPORTE=redaccion/rondas/$SEC-$R-$TIPO.md
[ -f "$REPORTE" ] && { echo "ERROR: $REPORTE ya existe; no se sobrescribe"; exit 1; }
N=${R#r}; N=$((10#$N))
PREV=$(ls redaccion/rondas/$SEC-r*-respuesta.md 2>/dev/null | sed -E "s/.*-r([0-9]+)-respuesta.md/\1 &/" \
       | awk -v n="$N" '$1+0 < n' | sort -n | tail -1 | cut -d' ' -f2)
LOGD=redaccion/.build/codex; mkdir -p "$LOGD"
LOG=$LOGD/$SEC-$R-$TIPO.log; ULT=$LOGD/$SEC-$R-$TIPO.ultimo.txt
RAIZ=$(pwd -W 2>/dev/null || pwd)

PROMPT=$(cat <<EOF
Eres un revisor de /ciclo-redaccion. Directorio de trabajo: redaccion/rondas/ del repositorio $RAIZ.
Primero lee, desde la raiz del repositorio: AGENTS.md, CLAUDE.md y overleaf/CLAUDE.md.
Despues lee ENTERO el archivo .claude/agents/$AGENTE.md: define tu rol, tus criterios y el formato de tu reporte.
Ignora su bloque YAML inicial; sus herramientas (Read, Grep, Glob, Write) son las de Claude Code: usa tus equivalentes.

Seccion: $SEC
Ronda: $R
Lint de esta ronda: $LINT
Respuesta del redactor a la ronda previa: ${PREV:-ninguna}
Encargo de la autora para esta ronda: ${ENCARGO:-ninguno}
${EXTRA:+Contexto del orquestador: $EXTRA}

Escribe tu reporte SOLO en el archivo $SEC-$R-$TIPO.md de tu directorio de trabajo (= $REPORTE).
No crees ni edites ningun otro archivo. No leas PDFs.
Tu respuesta final: una linea con la ruta del reporte y "alta=N media=N baja=N".
EOF
)
echo "inicio $(date -Is) $AGENTE $SEC $R (codex)" | tee "$LOG"
timeout 2400 codex exec -C redaccion/rondas -s workspace-write --ephemeral --color never -o "$ULT" - \
    <<<"$PROMPT" >>"$LOG" 2>&1
rc=$?
echo "fin $(date -Is) rc=$rc" >>"$LOG"
# Archivos nuevos en rondas que no son el reporte (el sandbox impide escribir fuera de rondas)
EXTRAS=$(git status --porcelain --untracked-files=all redaccion/rondas | awk '{print $2}' \
         | grep -E "^redaccion/rondas/$SEC-$R-" | grep -v -x "$REPORTE" | grep -v -E -- "-(guia|estilo|trazabilidad|asesor|lint)\.md$")
[ -n "$EXTRAS" ] && echo "AVISO: archivos extra de codex: $EXTRAS"
if [ ! -s "$REPORTE" ]; then
    echo "ERROR: codex no escribio $REPORTE (rc=$rc; log $LOG). Lanzar el subagente $AGENTE de Claude."
    exit 1
fi
TOT=$(grep -m1 -oE "alta=[0-9]+ media=[0-9]+ baja=[0-9]+" "$REPORTE")
[ -z "$TOT" ] && TOT=$(grep -oE "alta=[0-9]+ media=[0-9]+ baja=[0-9]+" "$ULT" 2>/dev/null | head -1)
echo "$REPORTE ${TOT:-TOTAL NO ENCONTRADO (revisar el reporte)}"
