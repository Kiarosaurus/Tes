# Asesor — capitulo3 r27

Archivo: `overleaf/secciones/capitulo3.tex` (estado de r27). Lint: `capitulo3-r27-lint.md` (PASA; GAP lit=0 dato=10
dec=0). Encargo: `redaccion/ENCARGO_2026-10-16.md` (una ronda; parada anticipada si una clase B toca otros capitulos).
Decisiones que mandan: `docs/01-decisiones.md` 2026-10-16 (#193 (a); ptos 1-4), 2026-10-16 (2) (#196 (a)),
2026-10-15 (3) y (4), 2026-10-15 ptos 9-10 (D9, QC y D3), 2026-10-08 (lo no delegado: "constancia de la revision
multiplanar ... son datos, no decisiones").

Recuento: **10** `\GAPDATO` (l. 38, 48, 194, 287, 297, 349, 457, 513 x2, 519), 0 `\GAPDEC`, 0 `\GAPLIT`. Coincide con
el lint. **`\REVVISUAL`: 30 apariciones en 25 lineas** (l. 31, 38 x2, 40, 220, 254, 258, 264, 270, 295, 297, 365, 367,
369 x2, 407, 455, 457, 474 x3, 493, 505 x2, 519, 521, 525, 527, 529, 533). Todas en `capitulo3.tex`; ningun otro
`.tex` de `overleaf/secciones/` conserva la macro.

| # | GAP (linea) | tipo | clase A/B/C/D | propuesta (1-2 lineas) | fuente |
|---|---|---|---|---|---|
| 1 | l. 38, contraste de realismo sin script (H5) | GAPDATO | **D** | Trabajo futuro declarado, con la razon; retirar las dos `\REVVISUAL` de la linea | DEC 2026-10-16 ptos 2-3 |
| 2 | l. 48, constancia de la revision multiplanar | GAPDATO | **B** (B-3; dato que solo tiene la autora) | Declarar lo que acredita el registro (3D de los 178; cortes en los 56 de CLINIC-metal) como limitacion, salvo que la autora acredite la revision en cortes | `exploration-3d/revision.csv` (178 = "3D completa"), `README.md`:58, `tornillos_conteo.csv`; DEC 2026-10-08 (lo no delegado) |
| 3 | l. 194, muestreo en el segundo corredor bajo S1 | GAPDATO | **B** (B-2, pendiente desde introduccion-r09) | No preinscribir ni correr; trabajo futuro | `introduccion-r09-asesor.md` B-2; DEC 2026-09-08 (3)-(4); ENCARGO 2026-10-16 item 6 |
| 4 | l. 287, canal en cortes de seccion estrictamente convexa (#178) | GAPDATO | **C -> A** (hecho) | Estratificacion descriptiva de la prueba de admision; el efecto sobre la salida del modelo queda como limitacion | `experiments/registro/registro_2026-10-16.md` §3; `r_seccion_convexa.py` |
| 5 | l. 297, comparacion visual a ciegas (D3) | GAPDATO | **D** | Protocolo fijado, no ejecutado; trabajo futuro | DEC 2026-10-16 pto 2 |
| 6 | l. 349, resultado del exploratorio con poses del muestreador (D9) | GAPDATO | **B** (B-1, pendiente desde introduccion-r09; calculo no barato: GPU, Khipu, particion de prueba) | Declararlo fijado y no ejecutado; trabajo futuro | DEC 2026-10-15 pto 9; `objetivo3/EXPERIMENTOS.md`:111-112 |
| 7 | l. 457, lista de la referencia de realismo | GAPDATO | **D** | Sin contraste de realismo la lista no tiene uso; la regla se conserva como parte del diseno no ejecutado | DEC 2026-10-16 pto 3 (nombra la lista) |
| 8 | l. 513, envolvente y canal sacro | GAPDATO | **A** | Limitacion con las cifras de la cohorte (14 de 71; hasta 6.4 mm en z; 0044 fuera) | DEC 2026-10-16 (2); `registro_2026-10-16.md` §2 |
| 9 | l. 513, techo de la etiqueta de S1 frente al platillo | GAPDATO | **C -> A** (hecho; en parte) | Mediana 6.5 mm (3.7 a 15.4) en la columna media de los 72 casos; el voxel mas craneal de toda la etiqueta sigue sin medirse | `registro_2026-10-16.md` §4; `r_techo_platillo.py`; `objetivo2/ts_nivel_s1.csv` |
| 10 | l. 519, estructura direccional del artefacto sintetico | GAPDATO | **D** | Limitacion declarada: no se midio; no citar #176 (ABIERTA, inspeccion, no medicion) | DEC 2026-10-16 pto 3 (nombra "estructura direccional") |

### Afirmaciones sin marca que deberian cambiar (decision no tomada o hecho no registrado, escrito como hecho)

- **l. 365 y 367 (`\REVVISUAL`), control visual (E-A4).** "La autora revisa además láminas de una muestra fija" afirma en
  presente un control que el registro no acredita. `objetivo3/visto.md`:9 solo registra la inspeccion en HTML del
  2026-10-12 (#176, ABIERTA: inspeccion, no medicion). Ningun archivo de `experiments/objetivo3/` registra la muestra de
  13 x 3 laminas con la lista cerrada de cuatro defectos (DEC 2026-10-15 pto 10), y DEC 2026-10-16 no la menciona.
  Ver B-4.
- **l. 533, "Las poses perturbadas que entrega el muestreador solo se examinan en un análisis exploratorio con el
  sintetizador".** Escrito en presente como si se hubiera hecho, y D9 no se ejecuto (`objetivo3/EXPERIMENTOS.md`:111-112).
  Depende de B-1. Mientras tanto la frase debe decir "se fijó" y no "se examinan".
- **l. 64, control de nivel.** "Esa comparación enfrenta el techo de la máscara de S1 [...] con el punto del platillo".
  En el codigo (`ts_piloto_qc.techo_dz`) el techo es el de una columna de la linea media alrededor de ese punto, no el
  de toda la etiqueta. No es un GAP: hay que precisarlo junto con el GAP #9 (texto abajo).

## Textos para el redactor (clase A y D)

**Criterio general para los `\REVVISUAL` (DEC 2026-10-16 pto 3).** Se retira la macro en las 30 apariciones. Hay dos
casos:
- **Se conserva el contenido y solo se quita la macro** (lo afirmado esta medido o es un supuesto declarado): l. 220,
  254, 258, 264, 270, 295, 407, 521, 525, 529. Respaldo: #191 y DEC 2026-10-15 (3) pto 6 (l. 254, 258);
  `d1_d2_resultado.md` (l. 264, 270, 521); DEC 2026-10-16 (l. 295). En l. 407, la rama "el realismo pasaba a primario"
  es historia de la sonda; se conserva sin macro.
- **Se reescribe como diseno no ejecutado o limitacion:** l. 31, 38, 40, 297, 365-369, 455-457, 474, 493, 505, 519,
  527 y 533 (textos abajo). La etiqueta `sec:ap-realismo` se conserva: la citan el cap. 2 y la introduccion.

**GAP #1 (D), l. 38.** Sustituir desde "\REVVISUAL{Queda pendiente [...]" hasta el final del parrafo por:
> "El contraste de realismo (Sección~\ref{sec:ap-realismo}) no se ejecutó. Después se entrenó una versión~2 del
> sintetizador, posterior y exploratoria, cuya evaluación en prueba se ejecutó salvo la comparación visual a ciegas de
> los modelos (Sección~\ref{sec:v2}). Esa comparación y el contraste de realismo quedan como trabajo futuro: el
> resultado visual del modelo evaluado se juzgó insuficiente y se decidió no rediseñar el sintetizador."

Respaldo: DEC 2026-10-16 pto 2 ("La comparacion visual a ciegas (D3) y el contraste de realismo sin script (H5) no se
ejecutan: se declaran como trabajo futuro, con la razon").

**l. 31 (figura).** Quitar "\REVVISUAL{, y realismo frente a tornillos reales}". La figura describe lo evaluado.

**l. 40.** Quitar la oracion `\REVVISUAL` sobre la regla de los tornillos reales de prueba. El hecho se conserva en
§Amenazas (l. 493, abajo), de modo que no se oculta.

**GAP #5 (D), l. 297.** Sustituir el bloque `\REVVISUAL{Se fija, por último, [...]}` por:
> "Se fijó, por último, el protocolo de una comparación visual a ciegas de los tres modelos: los mismos cortes,
> etiquetas ocultas, un orden aleatorio generado con semilla guardada y una pregunta fija, ordenar los modelos por el
> realismo del artefacto frente a una referencia real. Esa comparación, descriptiva y sin papel en ninguna decisión,
> no se ejecutó y queda como trabajo futuro."

Respaldo: DEC 2026-10-15 pto 10 (protocolo); DEC 2026-10-16 pto 2 (no ejecutado).

**l. 369.** Sustituir las dos `\REVVISUAL` por:
> "La evaluación del Objetivo~3 ordenó tres contrastes: dos sobre la \emph{streak amplitude} y uno, el de realismo,
> sobre los estadísticos que no exigen una imagen sin metal, que quedó diseñado y no se ejecutó
> (Sección~\ref{sec:ap-realismo})."

La oracion "La comparación de los estadísticos [...] Repite para la apariencia la lógica del Objetivo~2 [...]" se
traslada a §Contraste de realismo (l. 455) como descripcion del diseno, en pasado.

**GAP #7 (D), l. 455-457 (§Contraste de realismo).** Conservar el diseno en pasado, sin macro, abrir con su estado y
cerrar sin el `\GAPDATO`:
> "El contraste de realismo se diseñó y no se ejecutó en prueba; queda como trabajo futuro, por la decisión de no
> rediseñar el sintetizador tras juzgar insuficiente su resultado visual. Su diseño era el siguiente. [l. 455 en
> pasado: 'se juzgaba', 'se medía', 'se comparaban', 'se resumía'.] [...] Solo los tornillos aislados de esos
> pacientes la formaban, y el metal de placas o fijadores del mismo paciente se excluía de las cáscaras. Como el
> contraste no se ejecutó, la regla no llegó a aplicarse para formar la lista de pacientes."

Respaldo: DEC 2026-10-16 ptos 2-3. No escribir la lista ni un recuento de pacientes de la referencia: la regla nunca
se aplico como parte de un analisis.

**Tabla l. 474.** Celda por celda: "perfil radial e histograma en $M$ (realismo)" -> "perfil radial e histograma en
$M$ (realismo; diseñado, no ejecutado)"; "tornillos aislados reales de prueba" -> "tornillos aislados reales de
prueba (no aplicada)"; "fracción de cáscaras dentro del intervalo real, descriptiva" -> "fracción de cáscaras dentro
del intervalo real (no ejecutada)". Sin macro.

**l. 493 (§Amenazas).** Sustituir por una version corta, en pasado y sin macro:
> "La regla de la referencia de realismo, a diferencia de esas decisiones, se escribió cuando la autora ya había
> revisado en cortes 3 de los 11 pacientes de prueba que entonces se contaban con material ortopédico, y en uno de
> ellos había hallado un tornillo aislado que una lista previa de candidatos no incluía. Usaba, por tanto, información
> de inclusión de la partición de prueba, aunque ningún resultado de síntesis sobre ella. Como el contraste de
> realismo no se ejecutó, esa información no entró en ningún resultado."

(Las cifras 3 de 11, el paso a 9 y el tornillo no listado ya estaban en el texto; si se conserva "el recuento del 11
de octubre deja 9", mantener la remision a §Datos.)

**l. 505.** Quitar las dos macros y anadir el estado: "[...] el artefacto paramétrico y la muestra del control visual
[ver B-4]" y "[...] el protocolo de la comparación visual a ciegas, que no se ejecutó (Sección~\ref{sec:v2})."

**GAP #10 (D), l. 519.** Sustituir la oracion `\REVVISUAL` por:
> "La estructura direccional del artefacto sintético dentro de $G$ no se midió, y queda como limitación del
> Objetivo~3: el criterio primario no permite afirmar que el sintetizador genere rayas."

Respaldo: DEC 2026-10-16 pto 3. No citar la inspeccion visual de #176: es una implicancia ABIERTA y no es una medicion.

**l. 527.** Sustituir el bloque `\REVVISUAL` por una oracion que no compare con un contraste no ejecutado:
> "La fracción de la región de medición del protocolo físico bajo $-1000$~HU, medida en la partición de prueba
> (Sección~\ref{sec:ap-analisis}), dice cuánto baja ese brazo del suelo."

El resto del parrafo ("En el contraste primario, el suelo afecta solo al sintetizador [...]") se conserva.

**l. 529.** Conservar sin macro; la ultima oracion queda bien. Opcional: anadir al final "El contraste de realismo,
que habría enfrentado el sintetizador con lo real, no se ejecutó (Sección~\ref{sec:ap-realismo})."

**l. 533.** Sustituir la ultima oracion `\REVVISUAL` por:
> "El sintetizador genera además un tipo de tornillo que no aparece en su conjunto de entrenamiento."

(Se elimina "ni en la referencia de realismo": esa referencia nunca se formo.) La oracion anterior sobre las poses
perturbadas depende de B-1 (texto condicionado abajo).

**GAP #8 (A), l. 513, envolvente y canal sacro.** Sustituir "El cierre morfológico [...] daría brecha nula
\GAPDATO{...}" por:
> "El cierre morfológico de la envolvente (Sección~\ref{sec:corredor}) podría ocupar el canal sacro o los forámenes,
> y en ese caso una perforación hacia ellos daría brecha nula. Una medición posterior y descriptiva sobre la línea
> media de S1 lo acota en parte. En 71 de los 72 pacientes de la cohorte primaria, la envolvente deja fuera un hueco
> medial con HU de partes blandas o grasa, y el cierre lo ocupa solo en 14, en tramos de hasta 6.4~mm en $z$ y donde
> la unión de máscaras ya lo dejaba estrecho, de hasta 6.3~mm en sentido anteroposterior. La medición no establece que
> ese hueco sea el canal, no mide los forámenes ni el efecto sobre la brecha de ninguna pose, y deja fuera un
> paciente cuyo control de reproducción no coincidió."

Cifras: `registro_2026-10-16.md` §2 (14 de 71; 40 de 2727 cortes; max 6.4 mm en z; max 6.3 mm AP; HU medianas -77 a
51; `CLINIC_0044` 134.0 frente a 135.0 mm). DEC 2026-10-16 (2) pto 3 fija esa formulacion y sus limites. Si se quiere
el desglose: 6 de 23 en el grupo 2 y 8 de 48 en el grupo 3.

**GAP #9 (C -> A), l. 513, techo de la etiqueta y platillo.** Sustituir desde "El marco de referencia se define
[...]" hasta el `\GAPDATO` por:
> "El marco de referencia se define perpendicular al platillo superior de S1 que da la localización de referencias,
> mientras que el control de nivel usa el techo de la etiqueta de S1 en una columna de la línea media alrededor de ese
> punto (Sección~\ref{sec:marco-metal}). En los 72 pacientes de la cohorte primaria, ese techo queda por encima del
> platillo, con una mediana de 6.5~mm (de 3.7 a 15.4~mm); la cohorte ya está seleccionada por ese control, así que la
> distribución está truncada. La etiqueta es de vértebra completa, y su vóxel más craneal puede estar en la cresta
> sacra media, fuera de esa columna; la distancia entre ese vóxel y el platillo no está medida, ni cuál de las dos
> superficies coincide con el platillo anatómico."

Cifras: `registro_2026-10-16.md` §4 (`r_techo_platillo.py`, desde `objetivo2/ts_nivel_s1.csv`, `default6mm`: n 72,
mediana 6.5, RIC [5.7, 7.2], 3.7 a 15.4; ningun caso < 0; 2 casos >= 10 mm). Descriptivo y posterior. La "columna"
es x +-5 mm, y +-10 mm alrededor del punto (`ts_piloto_qc.techo_dz`). En l. 64 conviene la misma precision: "Esa
comparación enfrenta el techo de la máscara de S1 en la línea media, sobre una columna alrededor del punto del
platillo, con ese punto". Quitar "y las medidas sobre máscaras": ninguna fuente revisada identifica otra medida que
use el techo de la etiqueta (la rejilla del corredor, l. 109, usa el platillo de la localizacion).

**GAP #4 (C -> A), l. 287, canal y seccion estrictamente convexa.** Sustituir "Tampoco separa los cortes [...] no
produciría rayas \GAPDATO{...}." por:
> "Al promediar sobre cortes, tampoco separa los de un tornillo aislado cuya sección es estrictamente convexa, en los
> que, según Park, Choi y Seo, el endurecimiento no produciría rayas. Una estratificación posterior y descriptiva de
> la misma prueba los aproxima por la forma de la sección. En las secciones compactas, de un solo componente y con
> una razón de ejes de hasta 1.5, la ganancia mediana es de 0.111 en 14 pacientes y la ganancia neta, de 0.012 en 8.
> En las secciones alargadas o con más de un componente son de 0.148 en 18 y de 0.148 en 13. Ese es el sentido que
> predice el teorema, pero una máscara de vóxeles nunca es estrictamente convexa, el estrato compacto tiene solo
> 11 cortes con control anatómico y no se hizo prueba. El efecto del canal sobre la salida del modelo con canal en
> esos cortes no se midió."

Cifras: `registro_2026-10-16.md` §3 (control: reproduce los 228 cortes y `n_pix`). Por corte: 0.079 frente a 0.201;
Spearman(elongacion, ganancia) 0.172 en 228 cortes; con los cortes 1.3 y 2.0 la ganancia neta del estrato compacto es
0.076 (4 pac.) y 0.012 (10 pac.). Calculo descriptivo y posterior: el corte de 1.5 se fijo despues de ver el piloto.
Mantener "ganancia" y "ganancia neta" (terminos del texto, l. 285).

## Decisiones para la autora (clase B), con texto listo para 01-decisiones.md

**Alcance de la parada anticipada.** B-1 y B-2 **tocan otros capitulos**: introduccion (l. 68 y 78, sus dos
`\GAPDATO` siguen abiertos), cap. 3 (l. 194, 349, 533), cap. 4 (resultados del Objetivo 3 y del Objetivo 2) y
`trabajosFuturos`. **No son nuevas:** son las B-1 y B-2 de `introduccion-r09-asesor.md`, pendientes desde entonces, y la
ronda siguio sin pararse en cap. 1 y cap. 2. El ENCARGO 2026-10-16 (item 6) ya lista "D9" y "segundo corredor S1" como
trabajo futuro, lo que anticipa la opcion (a), pero no es una decision fechada. B-3 y B-4 son locales del cap. 3 (y,
como mucho, de un paragrafo del cap. 4).

**Argumento nuevo para B-1 (afecta a introduccion, cap. 1 y conclusiones).** DEC 2026-10-16 pto 1 acota el reclamo del
Objetivo 3 a "la sintesis local, en la banda, **condicionada por la pose del muestreador**". Si D9 no se ejecuta,
ninguna evaluacion del Objetivo 3 usa poses del muestreador: E-A2 usa el eje sin perturbar (l. 349). El
condicionamiento por la pose seria entonces una propiedad del diseno (el sintetizador acepta cualquier pose), no un
resultado evaluado. Propuesta: que la decision de B-1 lo diga, para que introduccion, cap. 4 y conclusiones no
escriban "evaluada con las poses del muestreador". No es una re-apertura de DEC 2026-10-16: es su lectura.

**B-1. D9 (poses del muestreador en el Objetivo 3).** Recomendacion: **(a) declararlo fijado y no ejecutado; trabajo
futuro.** Argumento: exige generar con GPU en Khipu sobre la particion de prueba (13 x 5 poses x 5 semillas), despues
de DEC 2026-10-16 ("el proyecto y sus resultados quedan como estan"). Era exploratorio, sin umbral y solo con el
sintetizador, y no podia mover el contraste primario.
- (b) Correrlo: cierra el GAP con un resultado, pero abre la particion de prueba para un analisis posterior a #193 y
  pide GPU.
- (c) Borrarlo del diseno: no es admisible, porque se fijo el 2026-10-15 y ocultaria una desviacion.

**B-2. Segundo corredor bajo S1.** Recomendacion: **(a) no preinscribir ni correr el muestreo; trabajo futuro.**
Argumento: sin distribucion ordinal clinica bajo S1, el resultado seria solo descriptivo (DEC 2026-09-08 (3)-(4)); el
nivel del corredor varia (S2 a S4 en la submuestra de 18, l. 194). El eje medido (69 de 72) se conserva como dato de
geometria.
- (b) Preinscribir y correr en Khipu con los ejes ya medidos: CPU, pero exige una preinscripcion nueva y da una
  distribucion sin referencia.

Texto listo para `01-decisiones.md` (si se adoptan B-1 (a) y B-2 (a); es el mismo de introduccion-r09, con el punto
del reclamo anadido):

```
## 2026-10-16 (3) — D9 y segundo corredor bajo S1: no se ejecutan; trabajo futuro (introduccion-r09, capitulo3-r27)

Decidido por la autora a propuesta del asesor de tesis.

1. **D9 (2026-10-15 pto 9) no se ejecuta.** El analisis exploratorio con 5 poses del muestreador por paciente de
   E-A2, solo con el sintetizador, queda como analisis fijado en el diseno y no ejecutado, y se declara como trabajo
   futuro. Razon: exige generar con GPU sobre la particion de prueba del Objetivo 3 despues de la decision del
   2026-10-16 (#193), y su resultado, exploratorio y sin umbral, no podia cambiar el desenlace del contraste primario.
   Los capitulos lo escriben como no ejecutado, no como pendiente. Consecuencia para el reclamo de 2026-10-16 pto 1:
   que la sintesis este "condicionada por la pose del muestreador" es una propiedad del diseno; ninguna evaluacion del
   Objetivo 3 usa poses del muestreador (E-A2 usa el eje sin perturbar).
2. **Segundo corredor bajo S1: no se preinscribe ni se corre el muestreo de poses.** Trabajo futuro. Razon: sin
   distribucion ordinal clinica bajo S1 (2026-09-08 (3)-(4)), el resultado seria solo descriptivo; el nivel del
   corredor varia entre volumenes. El eje medido (69 de 72) se conserva y se reporta como dato de la geometria del
   corredor, no como resultado del muestreador.
```

Textos condicionados para el redactor (solo si se adoptan):
- l. 349: "[...] El 15 de octubre se fijó un análisis exploratorio con 5 poses del muestreador por paciente de esta
  evaluación, solo con el sintetizador, el modelo evaluado y cinco semillas, con la \emph{streak amplitude} y la
  \emph{metal integrity} resumidas por grado de brecha cortical y la expectativa, sin umbral numérico, de que la
  amplitud variara poco entre grados. Ese análisis no se ejecutó y queda como trabajo futuro."
- l. 194: "[...] y la preinscripción cubre solo S1. Su eje está medido en 69 de los 72 pacientes de la cohorte
  primaria, pero el muestreo de poses en él no se preinscribió ni se ejecutó, y queda como trabajo futuro."
- l. 533: "El sintetizador se evalúa sobre el eje del corredor sin perturbar (Sección~\ref{sec:ap-sintesis}); el
  análisis exploratorio con las poses perturbadas del muestreador se fijó y no se ejecutó."
- l. 505: "Añadieron el análisis exploratorio con poses del muestreador, que no se ejecutó, [...]".

**B-3. Constancia de la revision multiplanar (GAP #2, l. 48).** Es un dato que solo la autora puede dar (DEC
2026-10-08 lo excluyo de la delegacion: "son datos, no decisiones"). Lo que acredita el registro:
- `experiments/exploration-3d/revision.csv`: los 178 volumenes con "Revisión 3D y cortes" = "3D completa". El
  protocolo (`README.md`:58) manda escribir "completa" solo al terminar los dos modos, asi que el registro acredita
  solo la 3D.
- `experiments/exploration-3d/tornillos_conteo.csv`, columna `autora` (revision en cortes, `explorar.py cortes`): 54 de
  los 56 pacientes de CLINIC-metal que cuentan con las cinco preguntas respondidas y 2 con parte; ninguna fila de
  volumenes sin metal. Revisiones en cortes puntuales: `tornillos_revision_autora.csv` (6 casos), #156, #163, #166.
- Para los volumenes sin metal (grupo 3, los que la regla de elegibilidad de entrenamiento exige revisar en cortes)
  no hay registro de revision en cortes.

Recomendacion: **(a) si la autora hizo la revision en cortes de todos los volumenes, que lo registre** (columna
"Revisión 3D y cortes" = "completa", con fecha, en `revision.csv`) y el GAP se cierra como A con esa fuente. **(b) Si
no, declararlo como limitacion**, con el texto de abajo. No hay opcion intermedia: la frase actual afirma una regla de
elegibilidad cuyo cumplimiento no consta.

Texto para el redactor si (b), l. 48 desde "La autora revisó [...]":
> "La autora revisó en vistas tridimensionales los 178 volúmenes y anotó tipo y cantidad de material. La regla de
> elegibilidad pedía además una revisión de cortes en los tres planos. El registro la acredita para los pacientes de
> CLINIC-metal, revisados en cortes para el conteo de tornillos, y no para los volúmenes sin metal, cuya ausencia de
> metal descansa en la revisión tridimensional y en el cribado por HU."

Texto listo para `01-decisiones.md` si (b):

```
## 2026-10-16 (4) — Revision multiplanar: se declara lo que acredita el registro (capitulo3-r27)

Decidido por la autora. El registro (`experiments/exploration-3d/revision.csv`) acredita la revision 3D de los 178
volumenes; la revision en cortes consta para los 56 pacientes de CLINIC-metal (`tornillos_conteo.csv`, columna
`autora`) y no para los volumenes sin metal. El cap. 3 lo declara como limitacion de la auditoria de la cohorte, sin
afirmar que la revision multiplanar este completa.
```

**B-4. Control visual de calidad (E-A4; l. 365-367, afirmacion sin marca).** DEC 2026-10-15 pto 10 lo fijo como control,
no como evaluacion; DEC 2026-10-16 no lo nombra. El registro no lo acredita como ejecutado con la regla (13 x 3 laminas,
lista cerrada de cuatro defectos); solo consta la inspeccion del 2026-10-12 (#176, ABIERTA). Recomendacion: **(a)
declararlo no ejecutado, junto con D3 y H5**, por la misma razon de DEC 2026-10-16 pto 2. Si la autora lo hizo, (b)
registrar el resultado (que laminas, que defectos) en `experiments/objetivo3/` y describirlo como control.

Texto para el redactor si (a), l. 365 (ultima oracion) y l. 367:
> "La evaluación preinscrita del Objetivo~3 es solo métrica, porque no hay un lector clínico disponible para juzgar la
> apariencia, a diferencia de la del Objetivo~2, que incorpora lecturas humanas del nivel vertebral y del corredor
> (Secciones~\ref{sec:corredor} y~\ref{sec:marco-metal}). Se fijó también un control de calidad visual, que no es una
> evaluación: 13 pacientes, semilla~0 y tres cortes por paciente, juzgados contra una lista cerrada de cuatro
> defectos (costura visible, metal fragmentado, artefacto fuera de lugar y anatomía alterada), y no ciego para el
> modelo evaluado. Ese control no se ejecutó con esa regla."

Texto listo para `01-decisiones.md` si (a) (puede ir como pto 3 de la entrada de B-1/B-2):

```
3. **Control visual E-A4 (2026-10-15 pto 10): no se ejecuta con la regla fijada.** Como D3 y H5 (2026-10-16 pto 2),
   se declara fijado y no ejecutado. La unica inspeccion visual registrada es la del 2026-10-12 (#176), que no es una
   medicion ni sigue la lista cerrada de defectos.
```

**#138 (cierre propuesto, no es un GAP aparte).** Con el GAP #9 resuelto como arriba, #138 queda contestada en lo que
toca al control de nivel (mediana 6.5 mm en la columna media) y declarada en lo demas (voxel mas craneal sin medir).
Si la autora esta de acuerdo, puede pasarla a DECIDIDA con esa formulacion: "la diferencia en la columna media se
reporta (registro 2026-10-16 §4); la del voxel mas craneal se declara como supuesto no medido".

Ninguna decision previa delega B-1 a B-4 en el asistente.

## Calculos hechos (clase C -> A) y calculos no baratos que quedan

**1. `experiments/registro/r_seccion_convexa.py`** (GAP #4; local, CPU, ~8 min; `registro_2026-10-16.md` §3; fila en
`experiments/objetivo3/EXPERIMENTOS.md` §6c).
- Reconstruye los cortes de la prueba de admision (`b_piloto_plantilla.cortes_reales`, entrenamiento de run04 y
  validacion; **no toca la particion de prueba**) y los cruza con `b_piloto/b_por_corte.csv`.
- **Control de regresion:** 228 de 228 cortes con par en (caso, comp, corte, ref) y el mismo `n_pix`. **Reproduce.**
- Resultado (estratos fijados despues de ver el piloto): compacta (1 componente, elongacion <= 1.5): 40 cortes, 14
  pacientes, ganancia 0.079 por corte y 0.111 por paciente, ganancia neta 0.012 (8 pacientes, 11 cortes); alargada o
  multiple: 188 cortes, 18 pacientes, 0.201 y 0.148, neta 0.148 (13). Spearman(elongacion, ganancia) = 0.172
  (p = 0.0094, 228 cortes). Sensibilidad 1.3 / 2.0 en el registro.
- Descriptivo y posterior. No mide el efecto del canal sobre la salida del modelo.

**2. `experiments/registro/r_techo_platillo.py`** (GAP #9; local, segundos; `registro_2026-10-16.md` §4; fila en
`experiments/objetivo2/EXPERIMENTOS.md` §5).
- La cifra por caso ya existia en `objetivo2/ts_nivel_s1.csv` (`dz_S1_*`, la del control de nivel); el script la
  resume en la cohorte primaria.
- **Control de regresion:** reproduce `objetivo2/ts_analisis.md` §1 (25/125/16/2 de 168; clinico ok concordante n 51,
  mediana 6.3, 3.7 a 15.7 mm). **Reproduce.**
- Resultado: 72 de 72, mediana 6.5 mm, RIC [5.7, 7.2], 3.7 a 15.4 (`default6mm`); 0 casos < 0; 2 >= 10 mm.
- Descriptivo y posterior; la distribucion esta truncada por el propio control de nivel.

**No baratos que quedan (para la autora):**
1. **D9** (GAP #6): GPU en Khipu sobre la particion de prueba del Objetivo 3. Ver B-1.
2. **Segundo corredor** (GAP #3): CPU en Khipu, pero exige antes una preinscripcion. Ver B-2.
3. **Voxel mas craneal de `vertebrae_S1` frente al platillo** (resto de #138): necesita las mascaras de la cohorte,
   que estan en Khipu (localmente solo hay dos pilotos fuera de la cohorte). CPU de minutos con un script parecido a
   `r_envolvente_canal.py`; no se propone, porque la formulacion de arriba ya declara el limite.
4. **Efecto del canal en la salida de run05b en cortes compactos** (resto de GAP #4): generar con GPU. No se propone
   (DEC 2026-10-16: sin trabajo nuevo sobre el sintetizador).

Evaluacion de impacto: los dos calculos son descriptivos y no cambian ninguna cifra confirmatoria ni preinscrita. El
de #178 da el sentido que el teorema predecia y no abre un supuesto nuevo. El de #138 precisa una amenaza ya declarada.
La lectura de DEC 2026-10-16 pto 1 frente a D9 (B-1) **si** toca la redaccion del reclamo del Objetivo 3 en otros
capitulos: queda propuesta dentro de B-1, sin implicancia nueva hasta que la autora decida.

TOTAL A=1 B=3 C=2 D=4 | GAP que quedarian si se aplica todo: lit=0 dato=0 dec=0 (con B-1, B-2 y B-3 adoptadas como se proponen; sin ellas, dato=3: l. 48, 194, 349; los dos C ya pasaron a A)
