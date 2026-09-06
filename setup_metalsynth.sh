#!/usr/bin/env bash
# =====================================================================
# setup_metalsynth.sh
# Crea el andamiaje del repositorio de tesis MetalSynth-Pelvis.
# Uso:
#   bash setup_metalsynth.sh
# Se ejecuta DENTRO de la carpeta donde quieres el repo.
# Es seguro correrlo dos veces: no sobrescribe archivos existentes.
# =====================================================================
set -euo pipefail

write_if_absent () {
  # $1 = ruta, stdin = contenido
  if [ -f "$1" ]; then
    echo "  (existe, no se toca) $1"
    cat > /dev/null
  else
    cat > "$1"
    echo "  creado  $1"
  fi
}

echo "== 1. Estructura de carpetas =="
mkdir -p papers
mkdir -p data
mkdir -p docs/literatura
mkdir -p tesis
mkdir -p src/muestreador src/renderizador src/common
mkdir -p notebooks
mkdir -p experiments
mkdir -p scripts
echo "  listo"

echo "== 2. Archivos base =="

write_if_absent .gitignore <<'EOF'
# ---- NUNCA subir ----
papers/          # PDFs con copyright del editor
data/            # volumenes CT: pesados y potencialmente identificables
*.nii
*.nii.gz
*.dcm
*.mhd
*.raw

# ---- Artefactos ----
__pycache__/
*.py[cod]
.ipynb_checkpoints/
.venv/
venv/
env/
*.egg-info/

# ---- LaTeX ----
*.aux
*.log
*.out
*.toc
*.bbl
*.blg
*.synctex.gz
*.fls
*.fdb_latexmk

# ---- Salidas de experimentos ----
experiments/**/checkpoints/
experiments/**/outputs/
*.ckpt
*.pth

# ---- Sistema ----
.DS_Store
Thumbs.db
EOF

write_if_absent papers/.gitkeep <<'EOF'
EOF

write_if_absent data/.gitkeep <<'EOF'
EOF

write_if_absent README.md <<'EOF'
# MetalSynth-Pelvis

Tesis de pregrado, UTEC. Autora: Kiara Balcazar Santa Cruz. Asesor: Victor Flores Benites.

Sintesis condicionada de implantes de osteosintesis y artefactos metalicos locales
en volumenes de CT pelvica mediante difusion latente multi-ventana.

## Que hay aqui

- `docs/` es la fuente de verdad del proyecto. Empezar por `docs/00-tesis.md`.
- `papers/` y `data/` NO estan versionados (ver .gitignore). Viven solo en local.
- `tesis/` contiene el documento LaTeX.
- `src/` codigo, separado en muestreador (geometria/pose) y renderizador (apariencia).
- `experiments/` un directorio por experimento, con su README de hipotesis y resultado.

## Estado

Fase: definicion de alcance y revision de literatura.
EOF

write_if_absent CLAUDE.md <<'EOF'
# CLAUDE.md — MetalSynth-Pelvis

Instrucciones permanentes para cualquier sesion de Claude Code en este repositorio.

## Que es este proyecto

Tesis de pregrado en imagen medica. Objetivo: sintetizar implantes de osteosintesis
(tornillos, placas) y sus artefactos metalicos locales en volumenes de CT pelvica,
para usarlos como aumentacion de datos y mejorar la robustez de redes de segmentacion
osea en la zona peri-implante.

El pipeline tiene DOS componentes que se disenan y evaluan por separado:

1. **Muestreador**: decide donde y con que pose 3D va el implante, respetando la
   anatomia. Restringido por mapas de densidad osea, contencion cortical y zonas
   seguras. No optimiza una trayectoria "perfecta": muestrea de la distribucion
   clinica real de malposiciones (31-60% segun Zwingmann et al. 2009).
2. **Renderizador**: genera la apariencia. Modelo de difusion latente 2.5D guiado por
   ControlNet, con codificacion multi-ventana en HU y una banda de generacion
   extendida (B_delta, ~12mm) mas alla de la mascara del implante, para que el
   streaking y el beam hardening puedan manifestarse fuera del metal.

Insumo propio: un banco de 61 geometrias de implantes.
Dataset primario: CTPelvic1K (Liu et al. 2021), subconjunto CLINIC-metal.
Baseline fisico de comparacion: XCIST/CatSim.

## Estructura y donde escribir

- `docs/00-tesis.md`     pregunta, hipotesis, alcance minimo vs completo
- `docs/01-decisiones.md` log fechado de decisiones (SOLO lo escribe la autora)
- `docs/02-datos.md`     data card de los datos disponibles
- `docs/03-glosario.md`  terminos (HU, MAR, ventana osea, brecha cortical, ...)
- `docs/literatura/`     una nota .md por paper, mas `_index.md`
- `papers/`              PDFs locales, nombre = clave BibTeX
- `refs.bib`             bibliografia
- `tesis/main.tex`       documento

## Reglas duras

1. **Nunca inventes referencias, DOIs, numeros de pagina ni cifras.** Si un dato no
   aparece explicito en el PDF que estas leyendo, escribe literalmente
   `NO ENCONTRADO EN EL PDF` y sigue. No estimes, no infieras, no completes.
2. **Toda cifra que vaya a la tesis necesita evidencia textual.** Cuando extraigas un
   numero de un paper, copia la frase original que lo contiene (menos de 15 palabras)
   y la seccion o pagina donde aparece.
3. **No edites `docs/01-decisiones.md`.** Ese archivo lo escribe solo la autora. Si
   crees que hace falta una decision, propon el texto en el chat y deja que ella lo pegue.
4. **No modifiques `tesis/main.tex` sin que se te pida explicitamente en ese turno.**
5. **Las notas de literatura siguen `docs/literatura/_plantilla.md`.** Sin excepciones
   de formato. El campo `Leido a fondo por la autora` se deja siempre en `no`.
6. **Nada de `papers/` ni de `data/` se copia dentro de archivos versionados.** Puedes
   leerlos, no reproducirlos. Extractos cortos citados estan bien; volcar paginas no.
7. Antes de proponer arquitectura o metodo, lee `docs/00-tesis.md` y
   `docs/01-decisiones.md`. No repropongas cosas ya descartadas ahi.
8. Si una tarea te obliga a asumir algo no documentado, **para y pregunta**. Es
   preferible una pregunta a un avance sobre un supuesto silencioso.

## Estilo

- Espanol para documentacion interna (`docs/`), ingles para `tesis/`.
- Python + PyTorch. Codigo con type hints y docstrings cortos.
- Nada de notebooks para logica reutilizable: eso va a `src/`.
EOF

write_if_absent docs/literatura/_plantilla.md <<'EOF'
# <clave-bibtex> — <titulo corto>

- **DOI / URL:**
- **Nivel de lectura:** 1 (profunda) | 2 (metodo) | 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/<archivo>.pdf

## Que hace (3 lineas maximo)

## Restriccion o supuesto clave
<Para papers de sintesis generativa: que supuesto explicito o implicito le impide
manejar implantes metalicos rigidos? Citar la frase donde se ve.>

## Que toco de aqui
- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
|  |  |  |

## Donde entra en mi tesis
<seccion / objetivo / metrica>

## Dudas para el asesor
EOF

write_if_absent docs/literatura/_index.md <<'EOF'
# Indice de literatura

Nivel 1 = leer a fondo yo misma. Nivel 2 = metodo y figuras. Nivel 3 = contexto.

| Clave | Nivel | PDF | Nota | Leido por mi | Para que lo uso |
|---|---|---|---|---|---|
| liu2021ctpelvic1k | 1 | si | | no | dataset primario |
| wu2022xcist | 1 | | | no | baseline fisico |
| peters2025benchmark | 1 | | | no | protocolo validacion |
| zwingmann2009malposition | 1 | | | no | tasa 31-60%, metrica SAP |
| smith2006iliosacral | 1 | | | no | escala de brecha cortical |
| wang2025adaptive | 1 | | | no | multi-ventana (C3) |
EOF

write_if_absent docs/00-tesis.md <<'EOF'
# 00 — Definicion de la tesis

> Este archivo lo escribe la autora. Es la fuente de verdad del alcance.

## Titulo actual

MetalSynth-Pelvis: Conditioned synthesis of osteosynthesis implants and local metal
artifacts in pelvic CT scan volumes using Multi-Window Latent Diffusion.

## Pregunta de investigacion

<pegar del main.tex>

## Hipotesis

<pegar del main.tex>

## Alcance MINIMO VIABLE (lo que garantizo defender)

- Objetivo 1: validacion de la representacion multi-ventana (Go/No-Go, MAE < 25 HU en hueso)
- Objetivo 2: muestreador de colocacion quirurgicamente restringido
- Metrica SAP + comparacion de distribuciones contra la tasa clinica real

Defendible por si solo como: "un muestreador de colocacion de implantes
quirurgicamente admisible, validado contra la distribucion clinica real de malposiciones".

## Alcance COMPLETO (si el tiempo alcanza)

- Objetivo 3: renderizador (LDM 2.5D + ControlNet + banda B_delta)
- Objetivo 4: metricas BFC e ISC
- Objetivo 5: evaluacion downstream (Dice, HD95) + ablaciones
- Reimplementacion validada de XCIST como brazo de comparacion

## Fuera de alcance (explicito)

<que decides NO hacer, para poder decirlo en la sustentacion>

## Fechas

| Hito | Fecha objetivo |
|---|---|
|  |  |
EOF

write_if_absent docs/01-decisiones.md <<'EOF'
# 01 — Log de decisiones

> Solo lo escribe la autora. Formato: una entrada por decision, con fecha.
> Tres lineas bastan. Este archivo es la evidencia de que el trabajo avanzo.

---

## AAAA-MM-DD — Separacion en muestreador y renderizador

**Decision:** el pipeline se divide en dos componentes evaluados por separado.

**Alternativas descartadas:** un solo modelo end-to-end que coloque y renderice.

**Por que:** permite atribuir el error a geometria o a apariencia, y hace que el
muestreador sea defendible como contribucion independiente.

---
EOF

write_if_absent docs/02-datos.md <<'EOF'
# 02 — Data card

> Lo genera Claude Code a partir de los datos reales en `data/`.
> La autora revisa y corrige. Sin inventar: lo que no se puede medir, se marca.

## Estado

PENDIENTE — ejecutar el inventario.
EOF

write_if_absent docs/03-glosario.md <<'EOF'
# 03 — Glosario

- **HU (Hounsfield Unit):**
- **MAR (Metal Artifact Reduction):**
- **Beam hardening:**
- **Photon starvation:**
- **Streaking:**
- **Ventana osea / multi-ventana:**
- **Brecha cortical (cortical breach):**
- **Zona peri-implante:**
- **B_delta (banda de generacion extendida):**
- **SAP / BFC / ISC:**
EOF

write_if_absent docs/prompts.md <<'EOF'
# Prompts guardados

Copiar y pegar en Claude Code dentro de la carpeta del repo.

---

## P1 — Generar refs.bib desde el LaTeX

Lee la seccion References de tesis/main.tex y conviertela a un archivo refs.bib
en la raiz del repo. Usa claves con formato apellidoANIOpalabraclave (ej.
liu2021ctpelvic1k). No busques en internet ni completes campos faltantes: si a una
entrada le falta DOI, volumen o paginas, escribe una linea de comentario
"% VERIFICAR: <clave> — falta <campo>" justo antes de esa entrada.
Al terminar, dime cuantas entradas quedaron marcadas para verificar.

---

## P2 — Emparejar PDFs con referencias

Lista los archivos en papers/ y emparejalos con las entradas de refs.bib.
Actualiza docs/literatura/_index.md con la tabla completa: una fila por entrada de
refs.bib, marcando si el PDF esta presente o no. No renombres nada todavia:
proponme los renombramientos en el chat y espera mi confirmacion.

---

## P3 — Fichas de extraccion (nivel 1)

Lee papers/<archivo>.pdf y genera docs/literatura/<clave>.md siguiendo exactamente
docs/literatura/_plantilla.md.

Ademas de la plantilla, agrega al final una seccion "## Evidencia textual" con una
tabla de todas las cifras, umbrales, definiciones de escala y criterios de evaluacion
que aparezcan en el paper, cada uno con la frase original que lo contiene (maximo 15
palabras) y la seccion o pagina exacta.

Si algo que yo esperaria encontrar no esta en el PDF, escribe NO ENCONTRADO EN EL PDF.
No completes con conocimiento general. Deja "Leido a fondo por la autora: no".

---

## P4 — Fichas de contexto (nivel 3, en lote)

Para cada PDF que te indique, genera su nota en docs/literatura/ siguiendo la
plantilla, pero solo a partir de abstract, introduccion y conclusiones. Marca en la
nota "Profundidad: abstract + conclusiones". No inventes detalles de metodo que no
hayas leido.

---

## P5 — Auditoria del LaTeX

Revisa tesis/main.tex y reportame en el chat, sin editar el archivo:
1. Comandos usados pero no definidos.
2. Cifras afirmadas en el texto que no tengan respaldo en docs/literatura/.
3. Frases ambiguas o que un jurado podria atacar.
Dame una lista numerada con la linea aproximada de cada hallazgo.

---

## P6 — Inventario de datos

Lee los volumenes en data/ en modo solo lectura y escribe docs/02-datos.md con:
numero de volumenes, spacing, dimensiones, rango de HU, presencia y extension de
metal, y que casos estan incompletos o son inusables. Genera tambien un script
reproducible en scripts/inventario_datos.py que produzca ese reporte.
No modifiques ni muevas nada dentro de data/.
EOF

write_if_absent experiments/.gitkeep <<'EOF'
EOF

echo "== 3. Git =="
if [ -d .git ]; then
  echo "  ya hay un repo git aqui, no se reinicializa"
else
  git init -q
  echo "  git init listo"
fi

echo ""
echo "======================================================"
echo "Listo. Siguientes pasos manuales:"
echo "  1. Copia tu main.tex a  tesis/main.tex"
echo "  2. Copia tus PDFs a     papers/"
echo "  3. git add -A && git commit -m 'scaffold inicial'"
echo "  4. Abre Claude Code en esta carpeta y usa docs/prompts.md"
echo "======================================================"
