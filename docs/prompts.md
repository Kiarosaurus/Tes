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
