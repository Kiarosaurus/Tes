# Respuesta del redactor — capitulo3 — r24 (ronda unica, encargo 2026-10-15b)

Archivo: `overleaf/secciones/capitulo3.tex`. Fuentes nuevas: DEC 2026-10-15 (3) ptos 1-6; DEC 2026-10-15 ptos 7 y 10;
`experiments/objetivo3/resultados_dec_2026-10-15.md` (D-extra 2 :71-81; D7 :118-126; #189 :128-162; a29 y pareado
:164-230); `EXPERIMENTOS.md` §6c; fichas `bland1986statistical`, `pitman1939note`, `morgan1939test`; #193 (ABIERTA).
Lint final: PASA (alta 0, media 0, baja 24 E-P1 preexistentes; GAP lit 2, dato 18, dec 0).

Fuente de las cifras nuevas del capitulo: 1 de 7 cascaras (D7, `resultados_dec`:123); 893 y 184 HU
(`resultados_dec`:78-79); -455.0 HU, IC90 -647.6 a -262.5 (`resultados_dec`:221 y DEC (3) pto 3); razon < 2 para
"plano" y regla (i) de la mitad (`resultados_dec`:183-186). Ninguna cifra del perfil (1.92, 2.42, 4.08), del
parametrico (1495.7) ni del TOST (-301.0) entra al cap. 3: van al cap. 4.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | `\GAPDEC` cerrado con DEC (3) pto 1 en un parrafo propio: dos niveles (objetivo de diseno y evaluacion cumplido; hipotesis de equivalencia, que un intervalo entero fuera del margen habria rechazado); no concluyente = los datos no permiten afirmar equivalencia, ni equivalencia ni no equivalencia demostrada; lectura declarada posterior a la prueba de las dos versiones. `\GAPLIT` nuevo para la fuente metodologica (E3). La introduccion (:50) dice "la no equivalencia haria fallar el objetivo": choca con el pto 1 si no se separan niveles; es de introduccion-r08, no de esta seccion |
| guia-2 | guia | APLICADO | :519 reescrito: pisos 893 frente a 184 HU, sentido (favorece al sintetizador, igual que las tres elecciones), pareado -455.0 HU con IC90, descriptivo y con su limite. La cifra entra pese a BITACORA §2 2026-10-11 porque el encargo E2 de la autora la da expresamente para el cap. 3; no se da -301.0. La frase "de ese efecto solo se conoce el sentido" (:487) se mantiene: trata del efecto conjunto de las tres elecciones, no del piso, y sigue siendo cierta |
| guia-3 | guia | APLICADO | :429 partido en dos parrafos: escalas del pto 2 (TOST en HU; Bland y Altman en razon por log, declarado como eleccion propia porque las diferencias no son proporcionales; Pitman y Morgan en HU = varianzas, en log = CV aproximado con `\GAPLIT`). Se quito "compara varianzas y no CV" (PAT-176). Los cinco limites de #189 van en un parrafo nuevo de Validez de la conclusion |
| guia-4 | guia | APLICADO | Marcas de #191 (:250), #187 (:367), #187-189 (:427) retiradas; en :289 la marca queda solo para #184 (ABIERTA), sin #190 (PAT-133) |
| guia-5 | guia | APLICADO | :481-483: dos tandas (primeras, previas a la prueba de v2; ultimas, posteriores a las dos versiones) y la lista de lo que fijaron las ultimas |
| guia-6 | guia | APLICADO | Dos parrafos nuevos en `sec:ap-analisis`: perfil por anillos 0-12 mm (razon 0-2/6-8, "plano" si < 2) y contraste pareado (misma semilla, mismo corte, regla de la mitad en 8-12 mm, banda completa frente a 196.3 HU descriptiva, limite, v2 sin sintesis sin metal). Papel del parametrico en positivo: oraculo de nivel, nivel por construccion y no textura |
| guia-7 | guia | APLICADO (parcial) | `\REVVISUAL` en :31 (figura), :38, :40, :248, :250 (atribucion), :256 (defecto desde 4 mm, que la autora puede desmarcar: es medicion), :287, :289 (comparacion a ciegas), :357-361, :399, :431-435, tabla `tab:diseno` fila 3, :471, :483, :497, :499 y :503 (por coherencia con capitulo2-r08, que marco el truncamiento de $B_\delta$ y el supuesto del dominio de imagen), :505, :507, :511. No se marcan :36 ni el titulo de :323: describen que se evalua (coherencia fisica y quirurgica), no afirman realismo, y capitulo2:126 deja la misma frase sin marcar |
| guia-8 | guia | APLICADO | $\beta$ -> $\eta$ en el artefacto parametrico, como ya fijaba BITACORA §2 2026-10-15 (capitulo3-r23); $\eta$ no se usa en otro capitulo |
| T01 | trazabilidad | APLICADO | Ver guia-1 |
| T02 | trazabilidad | APLICADO | Ver guia-3; condicion de Bland y Altman (diferencias proporcionales) citada con la ficha y declarada no cumplida |
| T03 | trazabilidad | APLICADO | Ver guia-2; mediana 1308 -> 1112 no se da (amplitud de prueba, cap. 4) |
| T04 | trazabilidad | APLICADO | :250 abre con el diagnostico, cierra con la atribucion al modelo (1 de 7) y el control trivial |
| T05 | trazabilidad | APLICADO | Ver guia-6; "no su textura ni la estructura de sus rayas" |
| T06 | trazabilidad | APLICADO | Marca retirada |
| T07 | trazabilidad | APLICADO | Ver guia-4; resultados de v2 remitidos al cap. 4 junto a v1 |
| T08 | trazabilidad | APLICADO | Ver guia-6 |
| T09 | trazabilidad | APLICADO | Ver guia-5; en :417 la salvedad "antes de cualquier prueba de equivalencia de la version 2" queda solo para los tres desenlaces |
| T10 | trazabilidad | APLICADO | Ver guia-7 |
| S1 | estilo | APLICADO | Salvedad completa solo en :417 y en Amenazas; :38, :216, :256, :423 con "el 15 de octubre"; :439 reescrito (S2) |
| S2 | estilo | APLICADO | :439 de nueve a siete oraciones; la oracion del entrenamiento antes de la enmienda se retira (ya esta en `sec:vision`) |
| S3 | estilo | APLICADO | "Receptor/a" solo para las dos pelvis de validacion; :66, :317, :319, :509 con "cohorte primaria" o "anatomia del paciente" |
| S4 | estilo | APLICADO | Limite de convexidad y su `\GAPDATO` movidos al parrafo de los limites de la prueba de admision |
| S5 | estilo | APLICADO | :258 sin "despues de diagnosticar el defecto" |

Bajos aplicados: guia-9/T11 (v2 "se ejecuto salvo la comparacion visual a ciegas", con `\GAPDATO` nuevo dentro de
`\REVVISUAL`), guia-10 ($\mathcal{N}$), T12 ("los tres desenlaces que este trabajo fija"), S6, S7, S8, S9, S10, S11,
S12, S13, S14, S15 (segunda mitad retirada: el registro no da valor), S16, S17. T13 (cerrar #184) es de la autora.

## `\GAPLIT` nuevos (candidatos PENDIENTES en `docs/literatura/_candidatos.md`)
1. Fuente metodologica sobre la lectura de un intervalo de equivalencia que cruza un limite del margen (no concluyente).
2. Fuente de que la varianza del logaritmo aproxima el cuadrado del coeficiente de variacion (Pitman y Morgan sobre ln).

## Para la autora
- #184 sigue ABIERTA aunque #190 la subsume (T13): si la cierra, cae la ultima marca de :289.
- `introduccion` (:50) conserva "la no equivalencia haria fallar el objetivo"; con el pto 1, la formula coherente es
  "la no equivalencia rechazaria la hipotesis de equivalencia; el objetivo de diseno y evaluacion se cumple".
- La cifra del pareado (-455.0 HU) entra al cap. 3 por el encargo; si prefiere la regla de BITACORA (veredictos sin
  cifra en el cap. 3), basta con dejar el sentido y remitir.

## Decisiones de redaccion
- Lectura posterior que da un objetivo por cumplido: se separan dos niveles (objetivo de diseno y evaluacion /
  hipotesis), y se nombra el resultado que habria rechazado la hipotesis.
- Decisiones del mismo dia con momentos distintos frente a los datos: "las primeras" (previas a la prueba de v2) y
  "las ultimas" (posteriores a las dos versiones), dicho una vez en Amenazas.
- Nombres nuevos: **perfil por anillos** (0-12 mm, razon 0-2/6-8, "plano" si < 2) y **contraste pareado** (sintesis
  con $M$ menos sintesis de $G$ sin $M$, misma semilla); papel del artefacto parametrico = "oraculo de nivel".
- Eleccion propia sobre una tecnica citada cuya condicion no se cumple: se cita la condicion de la fuente, se dice que
  aqui no se cumple y que la eleccion es de este trabajo (Bland y Altman en log).
- `\REVVISUAL`: envuelve oraciones o parrafos enteros (nunca titulos), con los GAP dentro; en tablas, celda por
  celda; las frases de alcance ("coherencia fisica y quirurgica") no se marcan.
