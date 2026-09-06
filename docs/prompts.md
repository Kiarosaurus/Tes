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
