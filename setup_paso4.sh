#!/usr/bin/env bash
# =====================================================================
# setup_paso4.sh — Endurecimiento del sistema
#   1. Fusiona _acceso.md dentro de _index.md (elimina desincronizacion)
#   2. Hook de git: no deja commitear si ESTADO.md no cambio
#   3. Hook Stop de Claude Code: avisa al cerrar cada respuesta si se
#      tocaron archivos criticos, y obliga a Claude a reportarlo
#   4. Quinta regla de snowballing (evidencia en contra)
#   5. scripts/auditar_bitacoras.sh para la revision a las 3 semanas
# Correr dentro del repo, despues de setup_paso3.sh.
# =====================================================================
set -euo pipefail

[ -f CLAUDE.md ] || { echo "ERROR: no estas en la carpeta del repo."; exit 1; }
[ -d .git ]      || { echo "ERROR: no hay repositorio git aqui."; exit 1; }

mkdir -p .claude/hooks scripts

# ---------------------------------------------------------------------
echo "== 1. Fusionar _acceso.md dentro de _index.md =="
# ---------------------------------------------------------------------
if [ -f docs/literatura/_acceso.md ]; then
  # Si el archivo ya tiene filas de datos, no lo borramos: lo respaldamos.
  if grep -qE '^\| [a-z]' docs/literatura/_acceso.md 2>/dev/null; then
    mv docs/literatura/_acceso.md docs/literatura/_acceso.RESPALDO.md
    echo "  tenia datos -> respaldado como _acceso.RESPALDO.md (migralos a mano)"
  else
    rm docs/literatura/_acceso.md
    echo "  estaba vacio -> eliminado"
  fi
fi

cat > docs/literatura/_index.md <<'EOF'
# Indice de literatura

Fuente unica de verdad sobre la bibliografia. Una fila por entrada de refs.bib.

**Nivel:** 1 = leer a fondo yo misma | 2 = metodo y figuras | 3 = contexto
**Acceso:** COMPLETO (PDF entero) | PARCIAL (preprint o secciones faltantes)
| ABSTRACT (solo resumen) | SIN ACCESO

| Clave | Nivel | Acceso | Nota generada | Leido por mi | Para que lo uso |
|---|---|---|---|---|---|
| liu2021ctpelvic1k | 1 | | | no | dataset primario |
| wu2022xcist | 1 | | | no | baseline fisico |
| peters2025benchmark | 1 | | | no | protocolo de validacion |
| zwingmann2009malposition | 1 | | | no | tasa 31-60%, base de SAP |
| smith2006iliosacral | 1 | | | no | escala de brecha cortical |
| wang2025adaptive | 1 | | | no | multi-ventana (C3) |

## Regla dura de accesibilidad

Ninguna cifra especifica (porcentaje, umbral, tamano de muestra, resultado
cuantitativo) puede citarse en la tesis desde una fuente marcada ABSTRACT o
SIN ACCESO. Si la cifra es imprescindible: conseguir el texto completo, o
cambiar la afirmacion por una cualitativa.

## Fuentes con acceso limitado — detalle

| Clave | Acceso | Que intente para conseguirla | Que afirmacion mia queda en riesgo |
|---|---|---|---|
EOF
echo "  reescrito  docs/literatura/_index.md (con columnas de acceso)"

# ---------------------------------------------------------------------
echo "== 2. Quinta regla de snowballing =="
# ---------------------------------------------------------------------
if ! grep -q "MENOR de lo que afirmo" docs/literatura/_candidatos.md 2>/dev/null; then
cat >> docs/literatura/_candidatos.md <<'EOF'

- **Cualquier trabajo que pudiera hacer que mi gap sea MENOR de lo que afirmo**,
  que ya haya intentado algo parecido, o que contradiga alguno de mis supuestos.
  Estos son los candidatos MAS importantes, no los menos. Proponlos siempre,
  aunque debiliten mi propuesta.
EOF
echo "  agregada regla de evidencia en contra"
fi

# ---------------------------------------------------------------------
echo "== 3. Hook de git: ESTADO.md obligatorio =="
# ---------------------------------------------------------------------
cat > .git/hooks/pre-commit <<'EOF'
#!/usr/bin/env bash
# Bloquea el commit si docs/ESTADO.md no fue actualizado.
# Saltar puntualmente:  SKIP_ESTADO=1 git commit -m "..."
set -e

[ "${SKIP_ESTADO:-0}" = "1" ] && exit 0
[ -f docs/ESTADO.md ] || exit 0

CAMBIOS=$(git diff --cached --name-only)
# Si el commit solo toca ESTADO.md o archivos de configuracion, pasa.
SUSTANTIVOS=$(echo "$CAMBIOS" | grep -vE '^(docs/ESTADO\.md|\.gitignore|README\.md)$' || true)
[ -z "$SUSTANTIVOS" ] && exit 0

if ! echo "$CAMBIOS" | grep -q '^docs/ESTADO\.md$'; then
  echo ""
  echo "  COMMIT BLOQUEADO: docs/ESTADO.md no fue actualizado."
  echo ""
  echo "  Estas commiteando cambios sustantivos sin dejar constancia de"
  echo "  por donde vas. Actualiza ESTADO.md (ultimo paso, siguiente paso,"
  echo "  pendientes) y vuelve a intentar."
  echo ""
  echo "  Para saltarlo esta vez:  SKIP_ESTADO=1 git commit -m \"...\""
  echo ""
  exit 1
fi
exit 0
EOF
chmod +x .git/hooks/pre-commit
echo "  instalado  .git/hooks/pre-commit"

# ---------------------------------------------------------------------
echo "== 4. Hook Stop de Claude Code: revision critica =="
# ---------------------------------------------------------------------
cat > .claude/hooks/revision-critica.sh <<'EOF'
#!/usr/bin/env bash
# Hook Stop. Se dispara cuando Claude va a cerrar su respuesta.
# Si se tocaron archivos criticos, sale con codigo 2: Claude lee stderr
# y debe reportar los cambios antes de terminar.
cd "$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0

ENTRADA=$(cat)

# Guarda anti-bucle: si ya estamos dentro de un stop hook, no reactivar.
echo "$ENTRADA" | grep -qE '"stop_hook_active"[[:space:]]*:[[:space:]]*true' && exit 0

CRITICOS='^(tesis/|docs/00-tesis\.md|docs/01-decisiones\.md|docs/04-implicancias\.md|refs\.bib|CLAUDE\.md)'
TOCADOS=$(git status --porcelain 2>/dev/null | awk '{print $2}' | grep -E "$CRITICOS" || true)

[ -z "$TOCADOS" ] && exit 0

{
  echo "REVISION CRITICA OBLIGATORIA antes de cerrar."
  echo ""
  echo "Se modificaron estos archivos criticos en el arbol de trabajo:"
  echo "$TOCADOS" | sed 's/^/  - /'
  echo ""
  echo "Antes de terminar, responde de forma breve y explicita:"
  echo "1. Que cambio exactamente en cada uno de esos archivos y por que."
  echo "2. Hay algo aqui que afecte la redaccion, el alcance, un supuesto,"
  echo "   un baseline o abra un gap nuevo? Si si, registralo en"
  echo "   docs/04-implicancias.md. Si no, dilo explicitamente."
  echo "3. Que tiene que revisar la autora personalmente y por que."
  echo ""
  echo "No repitas trabajo ya hecho. Solo el reporte."
} >&2
exit 2
EOF
chmod +x .claude/hooks/revision-critica.sh

# settings.json del proyecto (no pisa uno existente)
if [ -f .claude/settings.json ]; then
  echo "  OJO: ya existe .claude/settings.json — agrega el hook a mano."
  echo "       Ver .claude/settings.EJEMPLO.json"
  DEST=.claude/settings.EJEMPLO.json
else
  DEST=.claude/settings.json
fi
cat > "$DEST" <<'EOF'
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$(git rev-parse --show-toplevel)\" && bash .claude/hooks/revision-critica.sh"
          }
        ]
      }
    ]
  }
}
EOF
echo "  instalado  $DEST"

# ---------------------------------------------------------------------
echo "== 5. Auditoria de bitacoras =="
# ---------------------------------------------------------------------
cat > scripts/auditar_bitacoras.sh <<'EOF'
#!/usr/bin/env bash
# Ultima modificacion real (segun git) de cada bitacora.
# Correr cada 3 semanas. Regla: si un archivo no se toco y SI hubo
# actividad relevante, el archivo no funciona -> borrarlo o fusionarlo.
cd "$(git rev-parse --show-toplevel)"
printf "%-40s %-12s %s\n" "ARCHIVO" "ULT. CAMBIO" "COMMIT"
printf "%-40s %-12s %s\n" "---" "---" "---"
for f in docs/00-tesis.md docs/01-decisiones.md docs/02-datos.md \
         docs/04-implicancias.md docs/05-asesor.md docs/ESTADO.md \
         docs/literatura/_index.md docs/literatura/_candidatos.md; do
  [ -f "$f" ] || continue
  INFO=$(git log -1 --format="%ad %h" --date=short -- "$f" 2>/dev/null)
  [ -z "$INFO" ] && INFO="(nunca commiteado)"
  printf "%-40s %s\n" "$f" "$INFO"
done
echo ""
echo "Critico e irreemplazable: docs/04-implicancias.md"
echo "Si ese esta frio y hubo actividad, el sistema fallo donde mas duele."
EOF
chmod +x scripts/auditar_bitacoras.sh
echo "  creado  scripts/auditar_bitacoras.sh"

# ---------------------------------------------------------------------
if ! grep -q "archivo critico irreemplazable" CLAUDE.md; then
cat >> CLAUDE.md <<'EOF'

17. **`docs/04-implicancias.md` es el archivo critico irreemplazable.** Registra
    hallazgos que tocan el argumento de la tesis y que no se pueden reconstruir
    despues. Si dudas entre registrar o no, registra.

18. **`docs/literatura/_index.md` absorbio el registro de accesibilidad.** No crees
    `_acceso.md`. El nivel de acceso va como columna en `_index.md`.
EOF
echo "  actualizado  CLAUDE.md (reglas 17-18)"
fi

echo ""
echo "======================================================"
echo "Listo. Prueba el bloqueo de commit:"
echo "  git add -A && git commit -m 'endurecimiento'"
echo "(debe fallar hasta que edites docs/ESTADO.md)"
echo "======================================================"
