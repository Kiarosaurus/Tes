# Respuesta del redactor — capitulo3 — r25 (ronda unica)

Encargo: cerrar los dos `\GAPLIT` (lectura de un IC que cruza un limite; var(ln) ~ CV^2) con
`walker2011understanding`, `lakens2017equivalence` y `bland1996statistics`, sin renombrar los desenlaces (#194 ABIERTA,
mapeo pendiente de visto bueno). `\REVVISUAL` sin tocar (en :250 la oracion envuelta queda igual y pasa a abrir el
parrafo nuevo). Lint final: PASA (0 media; 25 bajas E-P1 preexistentes, una por el corrimiento de lineas); GAP lit 0,
dato 19, dec 0.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Parrafo nuevo tras :417 con el mapeo: Walker y Nowacki ("equivalence not established"; la no equivalencia no puede descartarse), Lakens (B "statistically different from zero but not statistically equivalent" si el IC95 excluye 0; "undetermined" si lo incluye). "No concluyente" = nombre de este trabajo, cubre B y D; "no equivalencia" = categoria propia que ninguna fuente nombra aparte (fichas: Walker :46, Lakens :125). Sin renombrar. `\GAPLIT` retirado de :419 |
| guia-2 | guia | APLICADO | Parrafo nuevo: la direccion se lee con el IC90 (regla de DEC 2026-10-15 pto 15, sin cambio) y Lakens decide la diferencia con el IC95; "a la baja" corresponde al escenario B solo si el IC95 excluye 0. IC95 de v1 sin cifra, con `\GAPDATO{calculado; consta en una implicancia abierta (implicancia 194)}` (BITACORA §2 2026-10-15, capitulo3-r23). Aviso a capitulo1 (:130) e introduccion (:52) queda para sus rondas (#194: "cap. 1 queda para su proxima ronda") |
| guia-3 | guia | APLICADO | :437 partido en tres parrafos. `bland1996statistics` solo para log indicado si la DE es proporcional a la media y antilog(DE) - 1 ~ CV con DE no grande; se dice que usa log10 y duplicados. Cambio de base y $e^s - 1 \approx s$, y su uso en Pitman y Morgan sobre ln, declarados como no contenidos en las fuentes. `\GAPLIT` retirado |
| guia-4 | guia | APLICADO | :437 da la condicion (sin umbral en la fuente; 0.496 "too large"; con 0.241 la validez no esta establecida). :525 alineado sin cifra nueva |
| guia-5 | guia | APLICADO | Dos oraciones en Validez de la conclusion (:523): el margen no es la mayor diferencia clinicamente aceptable de Walker y Nowacki (ficha :85), sino la variabilidad del metodo; una equivalencia no diria que la diferencia es irrelevante. Para el orquestador (regla 13 raiz): #194 no lo recoge; posible implicancia nueva sobre el significado del margen |
| T01 | trazabilidad | APLICADO | Igual que guia-1 y guia-2. "Ni como no equivalencia demostrada" y "la habria rechazado" quedan sin cita, como decision propia (DEC (3) pto 1). IC95 no aparece como cifra en el cap. 3 |
| T02 | trazabilidad | APLICADO | Igual que guia-3. `bland1996statistics` no se cita en la oracion de Pitman y Morgan (PAT-194) |
| T03 | trazabilidad | APLICADO | :525: "Leer la prueba de Pitman y Morgan sobre el logaritmo como comparacion de coeficientes de variacion es una aproximacion propia, y con el coeficiente del protocolo fisico su validez no esta establecida" |
| T04 | trazabilidad | APLICADO | :417: "como advierten Walker y Nowacki~\cite{walker2011understanding}, un resultado no significativo solo implica que no puede descartarse la equivalencia" (ficha :117) |
| S1 | estilo | APLICADO | :250 partido; "en ningun caso cambian..." pasa a la oracion 4; segundo parrafo abre con el `\REVVISUAL` intacto y cierra con la consecuencia (segunda condicion cumplida por construccion) |
| S2 | estilo | APLICADO | :256 sin la cronologia de v1; resultado con la formula de BITACORA §2 (streak amplitude por debajo); :258 "La version~2 es, por eso, posterior y exploratoria". La segunda oracion de :256 abre con "Esta version" para no abrir tres oraciones seguidas con "La version~2" (E-R1) |
| S3 | estilo | APLICADO | Oracion de direccion retirada de :419 |
| S4 | estilo | APLICADO | "Se separan dos niveles." |
| S5 | estilo | APLICADO | Salvedad completa solo en :419. :431 y :437 la retoman como "junto con la lectura de dos niveles" (no "con esas mismas decisiones": entre :419 y :431 hay cinco parrafos y el antecedente quedaba lejos); :531 "fijado con las ultimas decisiones del 15 de octubre" |
| S6 | estilo | APLICADO | :427 "su amplitud de solo ruido, o **piso de ruido**"; despues solo "piso de ruido" (:433, :529, :533). :331 conserva "amplitud de solo ruido", anterior a la definicion |
| S7 | estilo | APLICADO | "se saturan en el mismo suelo", "La saturacion en el suelo", "saturado en el mismo suelo"; :273 "extraer el parche" |
| S8 | estilo | APLICADO | Con T03 |

Bajas aplicadas: S9, S10, S11, S12 (incluido "desde las primeras"), S13, S14 (con "un perfil se llama plano si su
razon es menor que 2", para conservar el termino "plano" de BITACORA §2), S15, S16 (:525 y :435), S17 (:331, :367,
:429), guia-6 (= T04). No aplicada: T05 (opcional; la cita de Walker sobre fijar el margen antes de registrar los datos
exigiria precisar que el margen se midio en validacion, y no se quiso arriesgar E-R6).

## Decisiones de redaccion

- Desenlaces del TOST frente a la literatura: se conservan los nombres propios y se mapean una vez, en
  `sec:ap-analisis`, con el rotulo de cada fuente en ingles, entre comillas y en cursiva: "no concluyente" = "equivalence
  not established" (Walker y Nowacki) y escenarios B y D de Lakens; "no equivalencia" se declara categoria propia. En
  otras secciones (cap. 1 `sec:mt-estadistica`, introduccion) no se repite el mapeo: se remite a `sec:ap-analisis`.
- Direccion de la diferencia: se dice que se lee con el IC90 y que la correspondencia con "diferente" de Lakens exige
  el IC95; el IC95 de v1 va como `\GAPDATO{calculado; consta en una implicancia abierta (implicancia 194)}`, sin cifra,
  mientras #194 este ABIERTA.
- Derivacion propia junto a una cita: la fuente se cita solo para su eslabon (con su base, su contexto y su condicion), y
  la oracion que da el paso propio no lleva cita y dice que no esta en las fuentes.
- Anclaje temporal de las decisiones posteriores del 15 de octubre dentro de `sec:ap-analisis`: "junto con la lectura
  de dos niveles"; en Amenazas, "las ultimas decisiones del 15 de octubre".
- $\alpha$ no se usa para el nivel de significacion en el cap. 3 (reservado para el muestreador): se escribe "IC del
  90 % para un nivel de significacion de 0.05".
