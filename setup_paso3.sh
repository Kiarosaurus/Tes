#!/usr/bin/env bash
# =====================================================================
# setup_paso3.sh
# Agrega las bitacoras que faltaban:
#   - implicancias sobre la tesis (de cualquier origen)
#   - sesiones semanales con el asesor
#   - snowballing (candidatos surgidos de las lecturas)
#   - registro de accesibilidad de fuentes
# Correr dentro del repo, despues de setup_paso2.sh.
# =====================================================================
set -euo pipefail

if [ ! -f CLAUDE.md ]; then
  echo "ERROR: no estas en la carpeta del repo (no encuentro CLAUDE.md)."
  exit 1
fi

w () { if [ -f "$1" ]; then echo "  (existe) $1"; cat >/dev/null; else cat > "$1"; echo "  creado  $1"; fi; }

w docs/04-implicancias.md <<'EOF'
# 04 — Implicancias sobre la tesis

> Cola de hallazgos que PODRIAN cambiar algo del documento.
> La alimenta cualquier actividad: lecturas, tareas del asesor, experimentos.
> Claude escribe aqui. La autora decide: al resolver una entrada, la decision
> definitiva se copia a `01-decisiones.md` y aqui queda como APLICADA.

Estados: ABIERTA | APLICADA | DESCARTADA

| # | Fecha | Origen | Hallazgo | Que seccion toca | Tipo | Estado |
|---|---|---|---|---|---|---|

Tipos: REDACCION (ajustar como lo digo) | ALCANCE (agranda o achica el trabajo)
| GAP (posible nueva contribucion) | RIESGO (amenaza un supuesto mio)
| BASELINE (afecta con que me comparo)

---

## Detalle de entradas abiertas

<!-- Una seccion por entrada ABIERTA, con el contexto completo.
     Formato:

### [#] Titulo corto — ABIERTA
- **Origen:** <paper / tarea del asesor / experimento>
- **Hallazgo:** <que se encontro, con evidencia textual si viene de un paper>
- **Por que importa:** <que supuesto o afirmacion mia queda tocada>
- **Seccion afectada:** <Problem Statement / Hipotesis / Objetivo N / Datasets>
- **Opciones:** <que podria hacer al respecto>
- **Pendiente de:** <decision mia / consultar al asesor / mas lectura>
-->
EOF

w docs/05-asesor.md <<'EOF'
# 05 — Bitacora de sesiones con el asesor

> Una entrada por reunion. La autora anota la tarea encargada;
> Claude completa "que se hizo" e "implicancias" al cerrar la tarea.

---

## AAAA-MM-DD

**Tarea encargada:**

**Que se hizo:**

**Resultado / hallazgo principal:**

**Implicancias detectadas:** (numeros de entrada en 04-implicancias.md, o "ninguna")

**Para la proxima reunion:**
- Preguntas que le llevo:
- Lo que quedo pendiente:

---
EOF

w docs/literatura/_candidatos.md <<'EOF'
# Candidatos de snowballing

> Papers citados DENTRO de los que ya lei, que podrian importar.
> Claude los agrega al leer. La autora decide LEER o DESCARTAR.
> Al decidir LEER, la entrada pasa a `_index.md` y se descarga el PDF.

Estados: PENDIENTE | LEER | DESCARTADO

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|

## Reglas para proponer un candidato

Solo se propone si cumple al menos una:
- Es la fuente original de una cifra, escala o umbral que yo pienso citar.
- Es un metodo que compite directamente con el muestreador o el renderizador.
- Reporta la tasa clinica de malposicion o de brecha cortical.
- Define una metrica que podria reemplazar o validar SAP, BFC o ISC.

No se proponen papers "de contexto general" ni surveys adicionales.
EOF

w docs/literatura/_acceso.md <<'EOF'
# Registro de accesibilidad de fuentes

> Que tan a fondo pude leer cada fuente. Importa porque una afirmacion
> sostenida solo por un abstract es mas fragil y hay que saberlo.

Niveles de acceso:
- **COMPLETO** — PDF completo disponible en papers/
- **ABSTRACT** — solo abstract; no hay acceso al texto completo
- **PARCIAL** — preprint, version de conferencia, o partes faltantes
- **SIN ACCESO** — ni siquiera abstract confiable

| Clave | Acceso | Ruta intentada | Riesgo si solo abstract |
|---|---|---|---|

## Regla dura

Ninguna cifra especifica (porcentaje, umbral, tamano de muestra, resultado
cuantitativo) puede citarse en la tesis desde una fuente marcada ABSTRACT o
SIN ACCESO. Si la cifra es imprescindible, hay que conseguir el texto completo
o cambiar la afirmacion por una cualitativa.
EOF

# ---- Reglas nuevas en CLAUDE.md ----
if ! grep -q "04-implicancias" CLAUDE.md; then
cat >> CLAUDE.md <<'EOF'

13. **Evaluacion de impacto, siempre.** Al terminar CUALQUIER tarea (lectura,
    encargo del asesor, experimento, analisis de datos), pregunta explicitamente:
    este hallazgo obliga a ajustar la redaccion, el alcance, un supuesto, un
    baseline, o abre un gap nuevo? Si la respuesta es si en algun punto, agrega una
    entrada a `docs/04-implicancias.md` con estado ABIERTA. Si es no, dilo
    explicitamente en el chat: "sin implicancias sobre la tesis". Nunca lo omitas
    en silencio.

14. **No apliques implicancias por tu cuenta.** No edites `tesis/main.tex` ni
    `docs/00-tesis.md` a raiz de una implicancia. Registrala y espera decision de
    la autora.

15. **Snowballing.** Al leer un paper, si aparece una referencia que cumple las
    reglas de `docs/literatura/_candidatos.md`, agregala ahi como PENDIENTE. No
    la busques, no la descargues, no la agregues a refs.bib.

16. **Accesibilidad.** Toda fuente procesada se registra en
    `docs/literatura/_acceso.md` con su nivel de acceso. Si una ficha se genero
    solo desde el abstract, escribe "Profundidad: solo abstract" al inicio de la
    nota y no llenes la tabla de Evidencia textual con cifras del cuerpo.
EOF
echo "  actualizado  CLAUDE.md (reglas 13-16)"
fi

# ---- Prompts nuevos ----
if ! grep -q "P9 —" docs/prompts.md; then
cat >> docs/prompts.md <<'EOF'

---

## P9 — Tarea semanal del asesor

Victor me encargo esta tarea: <describir la tarea>.

Antes de empezar lee docs/00-tesis.md, docs/01-decisiones.md, docs/ESTADO.md y
docs/04-implicancias.md.

Al terminar:
1. Escribe el resultado donde corresponda (docs/, src/, experiments/).
2. Agrega la entrada de la reunion en docs/05-asesor.md.
3. Evalua explicitamente el impacto sobre la tesis segun la regla 13 de CLAUDE.md
   y registra lo que corresponda en docs/04-implicancias.md.
4. Actualiza docs/ESTADO.md.

Si concluyes que no hay implicancias, dimelo explicitamente y explica por que.

---

## P10 — Revision de implicancias (antes de cada reunion)

Lee docs/04-implicancias.md y dame un resumen de las entradas ABIERTAS ordenadas
por gravedad: primero las de tipo RIESGO y ALCANCE, luego GAP, luego BASELINE y
REDACCION.

Para cada una, en dos lineas: que decision me falta tomar y que necesito para
tomarla. No edites nada.

Usalo para preparar lo que le llevo a Victor.

---

## P11 — Revision de snowballing (mensual)

Lee docs/literatura/_candidatos.md y dame las entradas PENDIENTE agrupadas por la
regla que cumplen. Para cada una: en una linea, que afirmacion mia reforzaria o
amenazaria. Recomiendame cuales pasar a LEER, maximo cinco. No edites nada.
EOF
echo "  actualizado  docs/prompts.md (P9-P11)"
fi

echo ""
echo "Listo. Nuevas bitacoras en docs/. Prompts P9-P11 agregados."
