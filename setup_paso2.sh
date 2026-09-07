#!/usr/bin/env bash
# =====================================================================
# setup_paso2.sh
# Instala el subagente de lectura y reescribe docs/prompts.md con el
# orden definitivo. Correr DESPUES de setup_metalsynth.sh, dentro del repo.
# =====================================================================
set -euo pipefail

if [ ! -f CLAUDE.md ]; then
  echo "ERROR: no estas en la carpeta del repo (no encuentro CLAUDE.md)."
  exit 1
fi

mkdir -p .claude/agents scripts

cat > .claude/agents/lector-papers.md <<'EOF'
---
name: lector-papers
description: Lee un PDF de papers/ y escribe su ficha en docs/literatura/. Usar para cualquier lectura de literatura de este proyecto.
tools: [Read, Write, Glob, Grep]
---

Eres un extractor de literatura cientifica. Tu unica salida es un archivo .md.

Procedimiento:
1. Lee docs/literatura/_plantilla.md y respetala exactamente.
2. Lee el PDF que se te indica en papers/.
3. Escribe docs/literatura/<clave-bibtex>.md siguiendo la plantilla.
4. Agrega al final una seccion "## Evidencia textual": tabla con TODA cifra,
   umbral, definicion de escala o criterio de evaluacion del paper, cada uno con
   la frase original (maximo 15 palabras) y la seccion o pagina exacta.
5. Deja siempre "Leido a fondo por la autora: no".

Prohibido:
- Inventar cifras, DOIs, paginas o resultados. Si no esta en el PDF, escribe
  literalmente NO ENCONTRADO EN EL PDF.
- Completar con conocimiento general del area.
- Reproducir parrafos completos del paper.

Devuelve al final solo dos lineas: la ruta del archivo escrito, y cuantas
entradas quedaron como NO ENCONTRADO EN EL PDF.
EOF
echo "  creado  .claude/agents/lector-papers.md"

# Agregar la regla 9 a CLAUDE.md si aun no esta
if ! grep -q "refs.bib es autoridad" CLAUDE.md; then
  cat >> CLAUDE.md <<'EOF'

9. **refs.bib es autoridad.** La lista de referencias la definio la autora a mano.
   Nunca agregues, elimines ni sustituyas entradas. Nunca "corrijas" un campo con
   conocimiento propio. Si detectas un problema, marcalo con
   `% VERIFICAR: <clave> — <que problema>` y sigue.

10. **Lecturas de literatura siempre via el subagente `lector-papers`.** No leas
    PDFs en la sesion principal.
EOF
  echo "  actualizado  CLAUDE.md (reglas 9 y 10)"
fi

cat > docs/prompts.md <<'EOF'
# Prompts — ORDEN DEFINITIVO

Copiar y pegar en Claude Code, abierto en la carpeta del repo.
Uno por sesion. No saltarse el orden: P2 depende de P1, P3 depende de P2.

---

## P1 — Generar refs.bib

Lee la seccion References de tesis/main.tex y conviertela a refs.bib en la raiz del
repo. Claves con formato apellidoANIOpalabraclave (ej. liu2021ctpelvic1k).

No busques en internet, no agregues ni quites referencias, no completes campos con
conocimiento propio. Si a una entrada le falta DOI, volumen o paginas, escribe
"% VERIFICAR: <clave> — falta <campo>" en la linea anterior a esa entrada.

Al terminar dime cuantas entradas quedaron marcadas.

---

## P2 — Renombrar los PDFs (genera script, no ejecuta)

Lee los nombres de archivo en papers/ (vienen como "Autor - Titulo") y emparejalos
con las entradas de refs.bib.

Genera scripts/renombrar_papers.sh con una linea `mv` por archivo y, al lado, un
comentario con el nombre original. Los que no puedas emparejar con confianza, ponlos
al final comentados bajo "# SIN EMPAREJAR".

No ejecutes nada. Yo reviso el script y lo corro.

>>> Despues de revisarlo, en tu terminal:  bash scripts/renombrar_papers.sh

---

## P3 — Armar el indice de literatura

Actualiza docs/literatura/_index.md: una fila por cada entrada de refs.bib, indicando
si el PDF esta presente en papers/ o falta.

Asigna nivel de lectura segun estas reglas:
- Nivel 1: liu2021ctpelvic1k, wu2022xcist, peters2025benchmark,
  zwingmann2009malposition, smith2006iliosacral, wang2025adaptive
- Nivel 2: papers de sintesis generativa e insercion de metal
  (difftumor, diffboost, claim, lgesynthnet, ren2022, wang2019, xie2024,
  arand2019, ramadanov2025)
- Nivel 3: todo lo demas (surveys, reviews, contexto)

Dime al final que PDFs me faltan descargar.

---

## P4 — Fichas nivel 3 y 2 (en paralelo, con subagentes)

Usa el subagente lector-papers para procesar los PDFs de nivel 3 segun
docs/literatura/_index.md. Lanza maximo 4 en paralelo.

Cuando terminen, dame una tabla: archivo generado y numero de
NO ENCONTRADO EN EL PDF de cada uno.

>>> Repetir el mismo prompt cambiando "nivel 3" por "nivel 2".

---

## P5 — Fichas nivel 1 (una por una)

Usa el subagente lector-papers para leer papers/<clave>.pdf y generar su ficha.

Cuando termine, muestrame en el chat la seccion "Evidencia textual" completa para
que yo la revise antes de pasar al siguiente.

>>> Repetir seis veces, un paper por vez. NO en paralelo.

---

## P6 — Verificacion de cobertura

Verifica cobertura: para cada entrada de refs.bib, comprueba que exista (a) fila en
docs/literatura/_index.md, (b) PDF en papers/, (c) nota .md en docs/literatura/.

Dame la lista de las que fallen en alguno de los tres. No arregles nada, solo reporta.

---

## P7 — Auditoria del LaTeX

Revisa tesis/main.tex y reportame en el chat, SIN editar el archivo:
1. Comandos usados pero no definidos.
2. Cifras afirmadas en el texto sin respaldo en las fichas de docs/literatura/.
3. Frases ambiguas o atacables por un jurado.

Lista numerada, con la linea aproximada de cada hallazgo.

---

## P8 — Inventario de datos (cuando tengas la data en data/)

Lee los volumenes en data/ en modo SOLO LECTURA y escribe docs/02-datos.md con:
numero de volumenes, spacing, dimensiones, rango de HU, presencia y extension de
metal, y que casos estan incompletos o inusables.

Genera tambien scripts/inventario_datos.py que reproduzca ese reporte.
No modifiques ni muevas nada dentro de data/.
EOF
echo "  reescrito  docs/prompts.md"

echo ""
echo "Listo. Abre docs/prompts.md y sigue P1 -> P8 en orden."
