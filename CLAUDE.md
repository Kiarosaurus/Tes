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
