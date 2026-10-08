# gaps-r01 — respuesta del redactor

Ronda **acotada**, por pedido explicito de la autora ("resuelve gaps que solo faltan redactar puesto
que las fuentes ya existen"). No hubo reportes de revisores: las filas son los puntos E1-E12 del
encargo del orquestador. Secciones tocadas: `introduccion`, `capitulo1`, `capitulo2`, `capitulo3`.
Ninguna cifra de #141, #145, #149-#152 (ABIERTAS) entra al texto.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| E1. `\GAPDEC` de agregacion por paciente (`capitulo1.tex`:122) | orquestador (encargo) | APLICADO, CERRADO | Mismo contenido que `capitulo3.tex`:258: la unidad de analisis del Obj 3 es el paciente, la mediana de la *streak amplitude* sobre regiones de medicion y cortes deja un valor unico, y las pruebas pareadas van sobre los 14 valores de los pacientes de prueba sin metal, con `\ref{sec:apariencia}`. Fuente: DEC 2026-10-05 (3) pto 4. Cifra 14: misma fuente y `capitulo3.tex`:238 |
| E2. `\GAPDEC` de que haria fallar el Obj 3 (`introduccion.tex`:48) | orquestador (encargo) | APLICADO, CERRADO | Dos oraciones sustituyen a las dos anteriores (el parrafo sigue en 7): decide la equivalencia frente al protocolo fisico, que solo se concluye si el IC del 90 % de la diferencia pareada cae entero en $[-\Delta, +\Delta]$, "aun sin medir"; la superioridad frente a copia y pegado es control de cordura y ningun resultado suyo cuenta a favor del sintetizador. Fuentes: DEC 2026-10-05 (3) pto 5; DEC 2026-09-20 (2) D4 pto 3. Delta sin marca nueva: la cubre el `\GAPDEC` de preinscripcion de `capitulo3.tex`:182 ("margen de equivalencia"), como pidio el encargo. Se cierra el GAP entero y no solo la mitad: con la jerarquia fijada, "que haria fallar" queda respondido por la regla del IC 90 % (D4 pto 3) |
| E3. `\GAPDATO` del cribado de fractura (`introduccion.tex`:82) | orquestador (encargo) | APLICADO, CERRADO | La oracion "Al menos un paciente..." se sustituye por dos: 30 casos, 15 de corredor estrecho y 15 de control, fractura confirmada en 20 de 30, 10 en cada grupo; lector sin especialidad, cribado y no lectura de especialista; la cohorte receptora no es una coleccion de pelvis sanas. Cifras copiadas de `capitulo3.tex`:54 (capitulo3-r06), coinciden con `docs/00-tesis.md`:136-139. **No se nombra el soporte (laminas)**: el cap. 3 dice "laminas fijas" y `docs/00-tesis.md`:151-152 dice "18 casos sobre laminas y 12 sobre el volumen completo en un visor". Para no propagar la discrepancia se omitio; ver pendientes |
| E4. `\GAPDATO` de la revision de los 16 casos (`introduccion.tex`:84) | orquestador (encargo) | APLICADO, CERRADO | Tres oraciones sustituyen a la marca y a la condicional: revision de los 16 sobre laminas por la autora con apoyo de un medico sin especialidad, 14 conformes, 2 fallan con las dos variantes, ninguno solo con la principal (unico veredicto que reabria la eleccion), la variante se mantiene. Cifras de `capitulo3.tex`:97; verificadas contra `experiments/objetivo2/e9ts_revision_laminas_autora.csv` (16 filas: 14 `ok`, 2 `fallo_ambos`) y #131 §1 (CERRADA). El `\GAPDEC` de los dos casos con error de segmentacion no se duplica: queda en el cap. 3 |
| E5. `\GAPDEC` del error de ida y vuelta sin autoencoder (`introduccion.tex`:46) | orquestador (encargo) | APLICADO, CERRADO y reemplazado | "No lo verifica ningun objetivo" pasa a: se midio en los experimentos del Obj 1, aunque no entra en su criterio de fallo; media del MAE en hueso 0.00 HU en dos de las tres codificaciones y 21.80 HU en la tercera, 34 pacientes de prueba. Fuente: `experiments/objetivo1/p1_compuerta.md`:31-38, tabla "MAE en ROI hueso (test)", columna "identidad regla" (`LW20000` y `pub+asinh` 0.00, `pub` 21.80, n = 34; iguales para `sd15` y `afinado`, porque no pasan por el autoencoder). Nuevo `\GAPDEC` con el texto de `capitulo2.tex`:86: que codificacion y que precision numerica adopta el sintetizador. Nota: las cifras no estan en `tesis/main.tex` ni en un `EXPERIMENTOS.md` (no existe para el Obj 1); se copiaron porque el encargo autorizo esa fuente (regla 5 de `overleaf/CLAUDE.md`) |
| E6. `\GAPDEC` de preinscripcion del sintetizador (`capitulo3.tex`:182) | orquestador (encargo) | APLICADO, ESTRECHADO | Se quito "y su error de ida y vuelta sin autoencoder". El resto, igual |
| E7. `\GAPDEC` de la envolvente (`capitulo3.tex`:91) | orquestador (encargo) | APLICADO, CERRADO | La envolvente se define "con un cierre morfologico de 2 mm y sin relleno de cavidades cerradas"; nueva oracion: la decision que la definia con relleno se corrigio porque las mascaras de TotalSegmentator son volumenes solidos y no dejan hueco que tapar; se conserva la de 0 de 72. Fuente: DEC 2026-09-22, "CORRECCION DE D-O2.3 (2026-10-04)" pto 1 y su razon de construccion; cifra 72 de E14 en la misma correccion y #131 §2 (CERRADA). El parrafo queda en 7 oraciones |
| E8. `\GAPDEC` del suelo de $-1000$ HU (`capitulo1.tex`:48, `capitulo3.tex`:182) | orquestador (encargo) | APLICADO, REFORMULADO a `\GAPDATO` | Cap. 1: una oracion con la regla preinscrita (limitacion si la perdida atribuible a la representacion es menor que el margen de equivalencia; cambio si es mayor) y `\GAPDATO{desenlace de la regla preinscrita ..., que depende del margen de equivalencia, aun no medido}`. Cap. 3: la regla va en un **parrafo propio** (el original habria pasado a 9 oraciones, PAT-58): que mide (sin modelo, en $B_{\delta}$ de pacientes con metal de entrenamiento y validacion, la parte de la diferencia entre las colas del 5 % que pierde la ida y vuelta), el percentil 5 del paciente "y no la mediana, una eleccion hecha despues de ver su distribucion", y la regla con la misma marca. Para eso la oracion de la codificacion no congelada se movio una posicion arriba, dentro del primer parrafo. Sin 0.999/0.914/0.498 ni 77 pacientes. Fuente: DEC 2026-10-05 (primera entrada) ptos 2-4. El `\GAPDEC` de `capitulo3.tex`:300 (contra cual contraste) no se toco |
| E9. `\GAPDEC` de la contingencia de plazo del brazo de equivalencia (`capitulo1.tex`:128, `capitulo3.tex`:260, `introduccion.tex`:88) | orquestador (encargo) | **NO APLICADO** | La ACTUALIZACION de #90 (2026-09-21, `docs/04-implicancias.md`:8120-8146) registra el recorte como "contingencia declarada, a aplicar solo si el plazo lo obliga"; #90 sigue ABIERTA (:6464) y ninguna entrada posterior de DEC ni de implicancias la retira (`docs/ESTADO.md`:856 la repite). DEC 2026-10-05 (3) "Dependencia" (la autora decide implementar el brazo) no corta la contingencia, que ya presuponia la meta, y DEC 2026-10-05 (6) pto 5.2 anade una condicion tecnica (sonda de viabilidad) que convive con la de plazo. Segun el encargo, si la contingencia sigue vigente no se aplica. Ver pendientes |
| E10. `\GAPDEC` de la inversion de las metricas de Peters (`introduccion.tex`:43, `capitulo2.tex`:76) | orquestador (encargo) | APLICADO, ESTRECHADO | Introduccion: una clausula ("lo que ya esta definido para la *streak amplitude*", con `\ref{sec:apariencia}`) y la marca con el texto de `capitulo3.tex`:236. Cap. 2: una oracion nueva (la previa ya tenia 36 palabras) con la misma marca; el parrafo pasa a 7 oraciones. Fuente: DEC 2026-10-05 (3) y (4) |
| E11. `\GAPDEC` de la comparacion con observaciones reales (`introduccion.tex`:41) | orquestador (encargo) | APLICADO, ESTRECHADO | Texto de la marca igual al de `capitulo3.tex`:244: "que distancia entre distribuciones de amplitud se usa frente a las observaciones reales de artefacto, y con que analisis". Fuente: DEC 2026-10-05 (3) pto 5 |
| E12. Nombre del implante (`introduccion.tex`:66) | orquestador (encargo) | APLICADO | "tornillo transilíaco-transsacro" para el implante de este trabajo y en el texto del `\GAPDEC` (que sigue abierto). "Iliosacros" se mantiene en la oracion de la referencia clinica y del marco de Kaiser et al. (regla de #130). Fuente: #130, decision de la autora 2026-10-04, aplicada en `tesis/main.tex` y `capitulo3.tex`:9, 109 |

Efectos colaterales corregidos al minimo, y se declaran:

1. **E12, misma seccion.** `introduccion.tex`:32 (objetivo general, "un tornillo iliosacro") y :39
   (Obj 2, "un tornillo iliosacro, que une el ilion con el sacro") contradecian la correccion de :66.
   Ahora dicen "tornillo transilíaco-transsacro, o transiliosacro" (:32, primera aparicion en el
   documento) y "tornillo transilíaco-transsacro, que cruza las dos articulaciones sacroilíacas de un
   ilion al otro" (:39), con la descripcion de `capitulo1.tex`:76.
2. **E8, cap. 1.** `capitulo1.tex`:58 decia "La decision sobre ese limite esta pendiente"; ahora dice
   que el tratamiento depende de una regla preinscrita cuyo desenlace aun no se conoce.
3. **E10, cap. 1.** `capitulo1.tex`:68 decia en prosa que la inversion "esta pendiente para cada
   metrica"; ahora, definida para la *streak amplitude* y pendiente para las otras dos.

## GAP cerrados, estrechados y reformulados

| Marca | Seccion | Estado |
|---|---|---|
| `\GAPDEC` agregacion por paciente (E1) | `capitulo1` | **CERRADO** |
| `\GAPDEC` que haria fallar el Obj 3 / comparacion decisiva (E2) | `introduccion` | **CERRADO** |
| `\GAPDATO` cribado de fractura (E3) | `introduccion` | **CERRADO** |
| `\GAPDATO` revision de los 16 casos (E4) | `introduccion` | **CERRADO** |
| `\GAPDEC` ida y vuelta sin autoencoder (E5) | `introduccion` | **CERRADO**; abierto en su lugar el `\GAPDEC` de codificacion y precision que adopta el sintetizador (mismo texto que el cap. 2) |
| `\GAPDEC` preinscripcion del sintetizador (E6) | `capitulo3` | **ESTRECHADO** |
| `\GAPDEC` envolvente (E7) | `capitulo3` | **CERRADO** |
| `\GAPDEC` suelo de $-1000$ HU (E8) | `capitulo1`, `capitulo3` | **REFORMULADO** a `\GAPDATO` (desenlace de la regla) |
| `\GAPDEC` contingencia de plazo (E9) | `introduccion`, `capitulo1`, `capitulo3` | sin cambio (NO APLICADO) |
| `\GAPDEC` inversion de Peters (E10) | `introduccion`, `capitulo2` | **ESTRECHADO** a *bone* y *metal integrity* |
| `\GAPDEC` observaciones reales (E11) | `introduccion` | **ESTRECHADO** |
| `\GAPDEC` razon del tipo de implante (E12) | `introduccion` | sigue abierto, con el nombre corregido |

Conteo de GAP por tipo (lint por seccion):

| Seccion | Antes (lit/dato/dec) | Despues (lit/dato/dec) |
|---|---|---|
| `introduccion` | 0 / 5 / 16 | 0 / 3 / 15 |
| `capitulo1` | 4 / 1 / 9 | 4 / 2 / 7 |
| `capitulo2` | 1 / 2 / 10 | 1 / 2 / 10 |
| `capitulo3` | 1 / 10 / 24 | 1 / 11 / 22 |
| **Documento** | **6 / 18 / 59** | **6 / 18 / 54** |

Lint: `capitulo1`, `capitulo2` y `capitulo3` **PASA** (`capitulo3` con los 5 E-P1 bajos anteriores;
una E-O1 de 50 palabras que introduje en la l. 184 se partio antes de cerrar). `introduccion`
**FALLA** por las tres E-O1 de las lineas 7, 13 y 21 (encabezado y formulacion, DESFASADO por #126),
anteriores a esta ronda y no tocadas; ninguna linea editada genera hallazgo. Compilacion del
documento entero: compila, 117 paginas (antes 116), 0 citas indefinidas; un Overfull de 4.07 pt en
`capitulo3.tex`:202, que es el mismo de r08 (antes l. 200, desplazado por el parrafo nuevo del
suelo), no causado por estos cambios. Los G-T1 altos del lint global son plantillas sin redactar
(resumen, abstract, anexos, conclusiones, trabajos futuros). Lint de seccion guardado en
`redaccion/rondas/gaps-r01-lint-<seccion>.md`. El PDF de etapa y el registro en `BITACORA.md` quedan
para el orquestador (fuera de los archivos que este agente puede editar).

## Pendientes para la autora (no se resolvieron aqui)

1. **Contingencia de plazo del brazo de equivalencia (E9).** Para reformular la marca como condicion
   tecnica (sonda de viabilidad, DEC 2026-10-05 (6) pto 5.2) hace falta que la autora retire o
   confirme la contingencia de #90 en el registro. Mientras tanto la marca de plazo se mantiene.
2. **Soporte del cribado de fractura.** `capitulo3.tex`:54 dice "sobre laminas fijas";
   `docs/00-tesis.md`:151-152 dice 18 casos sobre laminas y 12 sobre el volumen completo en un visor.
   La introduccion no nombra el soporte; el cap. 3 deberia corregirse en una ronda suya.
3. **Cifras del Obj 1 en la introduccion.** 0.00 y 21.80 HU salen de `p1_compuerta.md`, no de
   `tesis/main.tex` ni de un `EXPERIMENTOS.md`. Si la autora prefiere el criterio del cap. 2 (sin
   cifras, remision al capitulo de resultados), basta con quitar la segunda oracion de
   `introduccion.tex`:46.

## Decisiones de redaccion

| Decision | Por que | Donde debe aplicarse igual |
|---|---|---|
| Un `\GAPDEC` cuya decision ya esta preinscrita y solo espera un dato pasa a `\GAPDATO` con la forma "desenlace de la regla preinscrita ..., que depende de X, aun no medido", y la regla se escribe en prosa sin las cifras de la implicancia ABIERTA | regla 2 y 3 de `overleaf/CLAUDE.md`; E8 | cualquier otra regla preinscrita a la espera de Delta (`capitulo4`, `conclusiones`) |
| Una eleccion de estadistico hecha despues de ver la distribucion se escribe como hecho ("una eleccion hecha despues de ver su distribucion"), no como metadeclaracion ("se declara post hoc") | PAT-5 | todo el documento |
| El implante de este trabajo se nombra "tornillo transilíaco-transsacro"; en la primera aparicion del documento (`introduccion` objetivo general) va con el alias "o transiliosacro"; "iliosacro" queda para trabajos ajenos (Smith, Kaiser, Zwingmann, Reilly, Liu) y para la categoria quirurgica (fijacion iliosacra) | #130 | `capitulo4`, `conclusiones`, resumen y abstract |
