# CLAUDE.md — Documento de tesis UTEC (overleaf/)

Instrucciones para cualquier sesion que lea o escriba dentro de `overleaf/`. **Se suman** a las del
`CLAUDE.md` raiz; no lo reemplazan. Sus reglas duras 1, 2, 3, 6, 9, 13, 14 y 15 siguen valiendo.

## Que es esta carpeta

`overleaf/` es el **documento que se entrega a la universidad**: plantilla UTEC (`tesisutec.cls`),
en **espanol**, con citas **IEEE numericas** (`IEEEtran.bst`, `\cite`). `tesis/main.tex` es otra
cosa: el boceto en ingles con que se presento la idea. Hoy es **la fuente de contenido mas
actualizada**, pero no el formato de entrega.

`overleaf/` **no es una traduccion** de `tesis/main.tex`. Se reorganiza en los cuatro bloques de
la guia del departamento (`Guia general y recomendaciones para la redaccion de CS.pdf`) y se explica
para un lector de computacion que no conoce el subtema (criterio G-B1). Lo que **no** se hace es
agregar contenido tecnico que no este respaldado en el repositorio.

## Archivos de apoyo (fuera de esta carpeta, para no subirlos a Overleaf)

| Archivo | Para que |
|---|---|
| `redaccion/RUBRICA.md` | Criterios con ID (`G-*` de la guia, `P-*` de la plantilla). Todo hallazgo de estructura cita uno |
| `redaccion/ESTILO.md` | Registro, voz, listas negras. Todo hallazgo de estilo cita un `E-*` |
| `redaccion/muestras_autora.md` | Parrafos de la autora. **Manda sobre ESTILO.md** en tono. Solo lo edita ella |
| `redaccion/MAPA.md` | Que archivo cubre que bloque, de que fuentes se redacta, su estado, y la tabla de GAP conocidos |
| `redaccion/rondas/` | Un reporte por ronda y revisor: `<seccion>-rNN-<revisor>.md`, mas la respuesta del redactor |
| `redaccion/BITACORA.md` | Patrones de error recurrentes, decisiones de redaccion y registro de cada etapa con su compilacion |
| `scripts/lint_redaccion.py` | Lint determinista. `--compilar` compila en `redaccion/.build/` |

## Reglas duras de redaccion

1. **Ninguna afirmacion sin respaldo en el repositorio.** Cada afirmacion tecnica, cifra o cita sale
   de `tesis/main.tex`, de una ficha en `docs/literatura/`, de `docs/` o de `experiments/`. Si no hay
   respaldo, **no se completa con conocimiento propio**: se marca.
2. **Marcas de GAP**, definidas en el preambulo de `overleaf/main.tex`, visibles en el PDF:
   - `\GAPLIT{que falta}`: hace falta una fuente que el repositorio no tiene. Ademas, se agrega el
     candidato a `docs/literatura/_candidatos.md` como PENDIENTE (regla 15 raiz). No se busca ni
     se descarga dentro del ciclo de redaccion.
   - `\GAPDATO{que falta}`: hace falta un resultado propio (experimento o revision no hechos).
   - `\GAPDEC{que falta}`: hace falta una decision de la autora o del asesor.

   El texto dentro de la marca dice **que** falta en una frase, no lo que se "espera" encontrar.
   Cada GAP nuevo se anota en la tabla de `redaccion/MAPA.md`.
3. **Implicancia ABIERTA = GAP, no hecho.** Solo entran como hechos las entradas APLICADAS o
   CERRADAS de `docs/04-implicancias.md` y lo decidido en `docs/01-decisiones.md`.
4. **Cita con ficha.** Solo claves que existan en `refs.bib`. Si la ficha del paper dice
   "Profundidad: solo abstract", no se cita ninguna cifra de su cuerpo. La cita no puede afirmar
   mas que la ficha (E-R6).
5. **Cifras propias**: se copian de `tesis/main.tex` o de `experiments/*/EXPERIMENTOS.md` y en el
   reporte de ronda se deja la fuente de cada una. Una cifra que difiera entre ambas fuentes se
   marca `\GAPDEC` y se reporta a la autora.
6. **Que se puede editar:**
   - `secciones/*.tex`: si, dentro de `/ciclo-redaccion` o por pedido explicito de la autora.
   - `main.tex`: solo el preambulo y el orden de `\input`, y solo por pedido explicito.
   - `referencias.bib`: **nunca**. Lo genera `python scripts/build_refs.py` a partir de `refs.bib`.
   - `tesisutec.cls`, `IEEEtran.bst`, `encabezados/`, `images/`: **nunca**. La dedicatoria y los
     agradecimientos son de la autora.
7. **El resumen y el abstract se escriben al final**, cuando los capitulos que resumen esten
   cerrados. Sin citas, siglas, figuras ni tablas (P-R2).
8. **Compilar al cerrar cada etapa.** Una etapa es una serie de correcciones cerrada: la redaccion
   inicial de una seccion o una ronda `rNN` ya respondida por el redactor. Al cerrarla, se compila
   el documento entero (`python scripts/lint_redaccion.py --compilar`), se guarda el PDF en
   `redaccion/.build/etapas/<seccion>-rNN.pdf` y se registra la etapa y sus patrones en
   `redaccion/BITACORA.md`. Una etapa que no compila no esta cerrada. Esto vale tambien para
   ediciones fuera de `/ciclo-redaccion` (por ejemplo, una correccion pedida en el chat).
9. **Al terminar una sesion de redaccion:** actualizar `redaccion/MAPA.md`, aplicar la regla 13 raiz
   (implicancias) y actualizar `docs/ESTADO.md`.

## Estructura (decision de la autora, 2026-09-29: orden de la guia)

Introduccion (a) -> Cap. I Marco teorico (b) -> Cap. II Estado del arte y brecha (b) ->
Cap. III Propuesta y metodologia (c) -> Cap. IV Resultados y discusion (c) -> Conclusiones y
Trabajos futuros (d). Los titulos de seccion dentro de cada capitulo son una **propuesta** y se
pueden cambiar.

## Terminos fijos (E-T1)

Alineados con `docs/03-glosario.md`. Si la autora cambia uno, se cambia en todo el documento.

| Concepto (tesis/main.tex) | En el documento |
|---|---|
| CT | tomografia computarizada (TC) |
| HU | unidades Hounsfield (HU) |
| metal artifact | artefacto metalico |
| streaking | rayas (*streaking*) |
| beam hardening | endurecimiento del haz |
| photon starvation | inanicion de fotones |
| MAR | reduccion de artefactos metalicos (MAR, *metal artifact reduction*) |
| generation band $B_{\delta}$ | banda de generacion extendida $B_{\delta}$ |
| implant mask $M$, generation region $G = M \cup B_{\delta}$ | mascara del implante $M$, region de generacion $G$ |
| placement sampler | muestreador de colocacion |
| cortical breach grade | grado de brecha cortical |
| osseous corridor | corredor oseo |
| SAP | admisibilidad quirurgica de la colocacion (SAP, *Surgical Admissibility of Placement*) |
| bone integrity, metal integrity, streak amplitude | se conservan en ingles y en cursiva: son nombres publicados del protocolo de `peters2025hybrid`, y la tesis decidio no renombrarlos |
| multi-window encoding | codificacion multiventana |
| round-trip | ida y vuelta (HU -> representacion -> HU) |
| pre-registration | preinscripcion |
| copy-paste insertion | insercion por copia y pegado |
| inpainting | *inpainting* (en cursiva; sin traduccion establecida) |
