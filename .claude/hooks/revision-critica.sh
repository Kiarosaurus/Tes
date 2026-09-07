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
