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
