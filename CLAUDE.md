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

9. **refs.bib es autoridad.** La lista de referencias la definio la autora a mano.
   Nunca agregues, elimines ni sustituyas entradas. Nunca "corrijas" un campo con
   conocimiento propio. Si detectas un problema, marcalo con
   `% VERIFICAR: <clave> — <que problema>` y sigue.

10. **Lecturas de literatura siempre via el subagente `lector-papers`.** No leas
    PDFs en la sesion principal.

11. **Al inicio de cada sesion, lee `docs/ESTADO.md`** para saber en que punto va el
    proyecto. No asumas continuidad con sesiones anteriores.

12. **Al final de cada sesion, actualiza `docs/ESTADO.md`**: ultimo paso completado,
    siguiente paso, y pendientes que surgieron. Se breve, tres o cuatro lineas.
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

17. **`docs/04-implicancias.md` es el archivo critico irreemplazable.** Registra
    hallazgos que tocan el argumento de la tesis y que no se pueden reconstruir
    despues. Si dudas entre registrar o no, registra.

18. **`docs/literatura/_index.md` absorbio el registro de accesibilidad.** No crees
    `_acceso.md`. El nivel de acceso va como columna en `_index.md`.
