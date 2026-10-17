# Asesor — capitulo2 r09

Archivo: `overleaf/secciones/capitulo2.tex` (estado de r08) y su Tabla A.1 en `overleaf/secciones/anexos.tex`:30.
Encargo: `redaccion/ENCARGO_2026-10-16.md`. Lint: `capitulo2-r09-lint.md` (GAP lit=1 dato=2 dec=0; PASA).
Decisiones que mandan: `docs/01-decisiones.md` 2026-10-16 (#193 (a), ptos 1-3); 2026-10-15 (3) ptos 1 y 9;
2026-09-17 (tabla de implicancias, filas #71 y #57, l. 988 y l. 990).

Recuento verificado en el `.tex`: 1 `\GAPLIT` (l. 88, Niu, Li y Wang: se queda), 2 `\GAPDATO` (l. 98, l. 112),
0 `\GAPDEC`; **7** `\REVVISUAL` en `capitulo2.tex` (l. 100, 102, 104, 112, 114, 124, 126) y **2 mas en
`anexos.tex`:30** (fila "Este trabajo" de la Tabla A.1, que es del cap. 2: el lint de la seccion no la cuenta).

| # | GAP (linea) | tipo | clase A/B/C/D | propuesta (1-2 lineas) | fuente |
|---|---|---|---|---|---|
| 1 | l. 98, cifras de la ablacion de Li et al. por verificar | GAPDATO | **A** | La decision ya fijo "sin cifras de `li2024`": la marca anuncia una verificacion que nadie va a usar. Retirarla y apoyar la oracion en la frase textual de Sec. I (no en la Tabla I) | `01-decisiones.md`:988 (2026-09-17, fila #71: "**Sin cifras de `li2024`** (tabla poco nitida)"); ficha `li2024.md`:17 y :81 (Sec. I, p. 1866) y :137 (Sec. IV-B, p. 1871) |
| 2 | l. 112, contraste de realismo sin script (H5) | GAPDATO | **D** | No se ejecuta: trabajo futuro declarado, con la razon; retirar `\REVVISUAL` y `\GAPDATO` | `01-decisiones.md` 2026-10-16 ptos 2-3; `00-tesis.md`:195, :208-212; misma formula que `introduccion.tex`:41 y :98 (r09, ya cerrada) |

No hay calculo barato que hacer: el GAP #1 es de lectura de un PDF (no de calculo) y la decision de 2026-09-17 lo
vuelve innecesario; el #2 lo excluye la decision de 2026-10-16. **No se escribio script ni registro.**

Afirmaciones sin marca que deberian llevar `\GAPDEC`: ninguna. Las convenciones de la seccion (ancho de $B_{\delta}$
como convencion, l. 104; brecha acotada, l. 116) estan respaldadas (DEC 2026-09-17 fila #57; DEC 2026-10-15 (3)
pto 9). Lo que si queda desfasado es texto dentro de `\REVVISUAL` que afirma en presente un contraste no ejecutado
(l. 112, l. 114, `anexos.tex`:30): se corrige abajo.

## Textos para el redactor (clase A y D)

**GAP #1 (A), l. 98.** Sustituir la oracion de Li et al. (con su `\GAPDATO`) y la siguiente por:
> "Li et al.~\cite{li2024}, cuya rama de solo imagen parte de la reconstrucción con artefacto, sostienen que
> trabajar en un solo dominio no recupera con eficacia el tejido a partir de los datos corrompidos, y comparan esa
> rama con su red de cuatro dominios en una ablación. Las dos fuentes tratan de reducción, que Lin et al. describen
> como un problema mal planteado porque paciente y metal contribuyen a la misma traza del sinograma."

Respaldo: *"Working in a single domain cannot effectively recover the true tissues from corrupted data."* (Sec. I,
p. 1866; ficha :17, :81) y *"The second group works only in the image domain with metal-corrupted images as input"*
(Sec. IV-B, p. 1871; ficha :137). No se dan cifras ni el orden de la Tabla I (DEC 2026-09-17, #71). Nota: "Los dos
resultados" pasa a "Las dos fuentes", porque Li et al. queda como afirmacion de los autores y no como cifra. Si la
autora quisiera las cifras, haria falta una relectura de la Tabla I por `lector-papers` con el PDF ampliado y una
nueva decision que revoque la de #71; no lo recomiendo: Lin et al. ya da la cifra del comparativo y el argumento no
gana nada.

**GAP #2 (D), l. 112.** Sustituir la oracion `\REVVISUAL` (con el `\GAPDATO`) por:
> "El contraste de realismo frente a las observaciones reales de artefacto no se ejecutó y queda como trabajo futuro
> (Sección~\ref{sec:ap-realismo})."

Respaldo: DEC 2026-10-16 pto 2 ("La comparacion visual a ciegas (D3) y el contraste de realismo sin script (H5) no se
ejecutan: se declaran como trabajo futuro, con la razon"). La razon ya la da la introduccion (§Alcance, l. 98); aqui
basta la remision, para no repetir (PAT-86).

### Reescritura de cada `\REVVISUAL` (retirar la macro; formulacion respaldada)

| # | Linea | Que hacer | Texto propuesto | Respaldo |
|---|---|---|---|---|
| R1 | 100 | Conservar la 1.a oracion (supuesto, "se asume": PAT-85) sin macro; reescribir la 2.a, que dice que el Obj 3 "contrasta ese supuesto" sin acotar | "Se asume que la apariencia del artefacto puede generarse en el dominio de imagen, porque sintetizar no exige separar las contribuciones del paciente y del metal. La comparación del Objetivo~3 con el protocolo físico contrasta ese supuesto solo en la amplitud del artefacto dentro de la banda, y no lo sostiene: no permite afirmar la equivalencia (Sección~\ref{sec:ea-brecha}). El realismo visual del artefacto sintético no se reclama (Sección~\ref{sec:amenazas})." | DEC 2026-10-15 (3) pto 1 ("La hipotesis de equivalencia con el protocolo fisico no se sostiene"); DEC 2026-10-16 pto 1 (reclamo acotado a la sintesis local en la banda); `introduccion.tex`:98 |
| R2 | 102 | Solo retirar la macro: el contenido esta decidido | "La banda $B_{\delta}$ trunca por diseño los efectos que estas fuentes describen lejos del metal, y esa limitación se discute en la Sección~\ref{sec:amenazas}." (sin cambios) | DEC 2026-09-17, fila #57 (`01-decisiones.md`:990: "trunca por diseno el streaking lejano"); `introduccion.tex`:102 |
| R3 | 104 | Solo retirar la macro; la cifra ya esta en el cap. 3 | Sin cambios de texto. Opcional, para alinear con la intro: "...no se separa del de un control sin metal más allá de 10~mm (Sección~\ref{sec:v2})." | `capitulo3.tex`:268 (18 pacientes, 500-4000 mm$^3$, anillo de 8 a 10 mm, IC90 por remuestreo); `introduccion.tex`:102 |
| R4 | 112 | Ver GAP #2 | (texto de arriba) | DEC 2026-10-16 pto 2 |
| R5 | 114 | Reescribir: afirma como existente una comparacion con lo real que no se ejecuto. La unica comparacion con lo real que si se corrio es E-A1, descriptiva | "En este trabajo, el contraste de realismo frente a observaciones reales no se ejecutó (Sección~\ref{sec:ap-realismo}), y la única comparación con el artefacto observado en pacientes es la reconstrucción descriptiva de implantes reales, que no incluye al protocolo físico (Sección~\ref{sec:ap-reconstruccion})." | DEC 2026-10-16 pto 2; `capitulo3.tex`:357 (E-A1: compara con la TC real, sin Peters); `objetivo3/EXPERIMENTOS.md`:84 (E-A1 CORRIDO 2026-10-12) |
| R6 | 124 | Reescribir el inciso: "para los efectos de adquisicion" sugiere que la banda los logra. Usar el proposito de diseno ("pensada para", que BITACORA 2026-10-15 deja fuera de `\REVVISUAL`) o la formula neutra de l. 122 | "...la codificación multiventana, la banda $B_{\delta}$ que extiende la generación fuera de la máscara del implante y la copia exacta fuera de $G$." | DEC 2026-10-08 pto 30 (combinacion de cuatro piezas); `capitulo2.tex`:122; BITACORA §2, 2026-10-15 (l. 456) |
| R7 | 126 | Conservar las dos oraciones sin macro y anadir una oracion de limitacion (sin numeros: el cap. 2 remite) | "La brecha descansa en un supuesto y en una convención que las fuentes revisadas no resuelven, y se evalúa de otro modo que la síntesis de lesiones. El supuesto es que la apariencia del artefacto puede generarse en el dominio de imagen, y la convención, el ancho de $B_{\delta}$ (Sección~\ref{sec:ea-representacion}). Este trabajo no reclama el realismo visual del artefacto sintético, que queda como limitación del Objetivo~3 (Sección~\ref{sec:amenazas})." | DEC 2026-10-16 ptos 1 y 3; `00-tesis.md`:208-212 |
| R8 | `anexos.tex`:30, celda de enfoque | Solo retirar la macro (el supuesto se enuncia igual en cuerpo, cierre y tabla: BITACORA l. 458) | "Supuesto: el artefacto puede generarse en el dominio de imagen." (sin cambios) | DEC 2026-09-30 (enunciado identico en los tres sitios, citado en BITACORA l. 458) |
| R9 | `anexos.tex`:30, ultima celda | Reescribir "contraste de realismo pendiente" | "...Copia y pegado solo como control de cordura; contraste de realismo no ejecutado (trabajo futuro)" | DEC 2026-10-16 pto 2 |

Notas para el redactor:
- **Dependencia con cap. 3 (r27).** R1, R5 y R7 remiten a `sec:ap-realismo` y `sec:amenazas`. La introduccion r09 ya
  remite a `sec:ap-realismo`; si capitulo3-r27 retira o renombra esa subseccion, hay que ajustar las tres remisiones.
  `sec:amenazas` debe recoger la limitacion de realismo (lo hara r27 por DEC 2026-10-16 pto 3); si no lo hiciera,
  cambiar la remision a "véanse las limitaciones en la introducción".
- No anadir en el cap. 2 las cifras de la limitacion (razon 1.92 frente a 4.08 de #187, piso 893 frente a 184 HU de
  #188, p95 de #191): son resultados propios y su lugar es el cap. 3/4. El cap. 2 solo declara y remite.
- No mencionar la prueba de Turing (no era compromiso: DEC 2026-10-16 pto 2).
- R1 usa "no permite afirmar la equivalencia", no "no equivalencia" (DEC 2026-10-15 (3) pto 1; #194).

## Decisiones para la autora (clase B), con texto listo para 01-decisiones.md

Ninguna. Los dos `\GAPDATO` y los nueve `\REVVISUAL` se cierran con decisiones ya fechadas (2026-09-17 fila #71;
2026-10-15 (3) pto 1; 2026-10-16 ptos 1-3).

## Calculos hechos (clase C -> A) y calculos no baratos que quedan

Ninguno. No hay GAP de clase C en esta seccion.

TOTAL A=1 B=0 C=0 D=1 | GAP que quedarian si se aplica todo: lit=1 dato=0 dec=0
