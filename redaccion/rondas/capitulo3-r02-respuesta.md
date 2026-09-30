# capitulo3 — r02 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo3.tex`. Reportes leidos: `capitulo3-r02-lint.md`,
`-guia.md`, `-estilo.md`, `-traza.md`. Fuentes releidas para cada cifra o regla tocada: `docs/01-decisiones.md`
(2026-09-10; 2026-09-11 (2) #31; 2026-09-14 #50; 2026-09-14 (3); 2026-09-15 (2); 2026-09-17 B.2, D.1 y (3);
2026-09-19; 2026-09-20 (2) D3-D4; 2026-09-21 R1-R4; 2026-09-21 (2); D-O2.1 a D-O2.7),
`experiments/objetivo2/e9ts_resumen.md` (:14-20), `e13_sap.md`, `e12_sap_control.md`, `r1_landmarks.md`,
`preinscripcion_muestreador.md` §2-§4, `experiments/objetivo3/diseno_A.md` §4, `experiments/objetivo1/p1_compuerta.md`,
`docs/02-datos.md` (:117-137), `tesis/main.tex` :77, :79, :121, y la ficha `guo2025maisi`.

Criterio de autoridad aplicado (indicacion del orquestador y orden de `MAPA.md`): lo que consta en
`docs/01-decisiones.md` entra como hecho aunque no este en `tesis/main.tex`. Solo queda `\GAPDEC` cuando dos
decisiones se contradicen, cuando decision e implementacion difieren, o cuando ninguna decision da el dato.

Conteo (alta + media): **25 APLICADOS, 0 RECHAZADOS, 4 ESCALADOS** (29 hallazgos).

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| lint E-T3 "AI" (media) | lint | APLICADO | Por indicacion del orquestador ya no se despliega el nombre en ingles. En §Compuerta dice "el del generador de volumenes de TC de Guo et al.~\cite{guo2025maisi}", apoyado en la ficha ("Genera volumenes CT 3D"). En validez interna y en validez de la conclusion dice "el latente de Guo et al.". La sigla MAISI desaparece del capitulo; sin ese cambio el lint la marcaba como sigla sin definir |
| guia-1 (media) | guia | ESCALADO | `\GAPDEC{que resultado de la prueba de superioridad frente a la copia y pegado contaria como fallo, dado que esa linea base no genera rayas por construccion, o si la prueba decisiva del Objetivo 3 es la de equivalencia frente al protocolo fisico}` en §Apariencia. D4 fija la prueba de superioridad y no dice cuando falla; presentarla como "comprobacion de cordura" seria redefinir el diseno de la autora |
| guia-2 (media) | guia | ESCALADO | La codificacion del sintetizador es `[SUPUESTO]` en `diseno_A.md` §4 (borrador), y ninguna decision la fija. El parrafo de l.184 se unio al de la formulacion (S11), y su `\GAPDEC` se amplio para cubrir la codificacion ("el borrador supone la de arcoseno hiperbolico") y su error de ida y vuelta sin autoencoder. El error de identidad existe en `p1_compuerta.md`, pero no en TM ni en un `EXPERIMENTOS.md`, asi que no se copio |
| guia-3 (media) | guia | APLICADO | Validez interna: "la regla operativa y sus seis combinaciones se fijaron despues de una exploracion del autoencoder preentrenado que incluia a los pacientes de prueba y que ya habia fallado el criterio de 25 HU. Ese umbral era anterior a la exploracion y no se movio, y anadir combinaciones solo podia favorecer un veredicto aprobatorio". Fuentes: DEC 2026-09-15 (2), con E6b en 178 de 178 y el umbral mantenido, y DEC 2026-09-17 (3) |
| guia-4 (media) | guia | APLICADO | "se congelo antes de calcular cualquier distancia contra la referencia clinica" (formula de l.127; PRE, encabezado) |
| guia-5 (media) | guia | APLICADO | En §SAP: solo la distribucion de grados se compara con la referencia clinica; la densidad y la viabilidad se reportan como descriptivas, la viabilidad por caso (D-O2.6: "componente que se reporta"). Fila 2 de `tab:diseno`: "fraccion por zona de densidad y viabilidad del corredor por caso, descriptivas" |
| guia-6 (media) | guia | APLICADO | Junto con S12: "Antes de la corrida se fijaron tres comprobaciones que la implementacion debia cumplir. Son controles de consistencia de la implementacion y no condiciones de fallo del muestreador como modelo". Las dos primeras son C2 y C3 de `e12_sap_control.md`; la tercera es la integridad de `e13_sap.md` ("Poses sin grado: 0") |
| guia-7 (media) | guia | APLICADO | Un nombre para cada cantidad: "margen cortical de longitud util" ($h$, 5 mm) y "holgura radial" ($\epsilon$, 1-2 mm). En l.83 se dice por que $h$ es transversal: es "el radio del corredor de 10 mm", no una holgura anadida al tornillo (DEC 2026-09-11 (2), alternativa descartada). La fila de `tab:preinscripcion` y l.158 se alinean. El `\GAPDEC` de $h = 2\sigma$ no cambia |
| guia-8 (media) | guia | APLICADO | Se nombra "el autoencoder variacional de Stable Diffusion 1.5" (DEC 2026-09-17 (3)). La adaptacion queda asi: "un decodificador adaptado por cada codificacion", ajustado "con cortes codificados de los pacientes de entrenamiento, separados de los de prueba" (DEC 2026-09-17 D.1). Lo que ninguna fuente da va a `\GAPDATO{parametros del ajuste del decodificador (numero de cortes, funcion de perdida, optimizador y criterio de parada)...}` |
| guia-9 (media) | guia | APLICADO | Filtro de DEC D3: "voxeles sobre 2500 HU, longitud de al menos 30 mm y anchos de 12 mm o menos". "43 casos" pasa a "43 volumenes" (E11 corrio sobre los 178 volumenes; guia-11) |
| S01 (media) | estilo | APLICADO | Tres negativos acotados a "las fuentes revisadas" (l.95, l.164, l.174) |
| S02 (media) | estilo | APLICADO | "Cualquier cambio posterior se registra como desviacion, con fecha y motivo." |
| S03 (media) | estilo | APLICADO | "El Objetivo 2 no tiene regla de decision: ningun valor de la distancia se fijo de antemano..." |
| S04 (media) | estilo | APLICADO | "metricas de Peters et al." en la figura y en l.46; "protocolo fisico" solo para el brazo |
| S05 (media) | estilo | APLICADO | l.212 "Zwingmann et al. no reportan haber excluido..."; l.260 "en la referencia clinica"; l.262 "Las dos series de la referencia clinica son pequenas" |
| S06 (media) | estilo | APLICADO | "que las pelvis receptoras, sin fractura conocida, no reproducen"; l.254 "en la cohorte del Objetivo 2" |
| S07 (media) | estilo | APLICADO | Junto con guia-3: "sobre los 178 volumenes locales, incluidos los de los pacientes que despues formaron la particion de prueba, ya habia quedado por encima del criterio en todos ellos. La regla se fijo, por tanto, conociendo un resultado exploratorio desfavorable" (DEC 2026-09-15 (2): 178 de 178) |
| S08 (media) | estilo | APLICADO | Se ubica en el embudo: "En el primer paso, 7 pacientes quedaron fuera porque el campo de vision truncaba las crestas iliacas". Una cresta truncada impide tener las cinco referencias en el campo de vision, que es el primer paso (TM:121). No se calculo el resto por diferencia |
| S09 (media) | estilo | APLICADO | Igual que guia-4 |
| S10 (media) | estilo | APLICADO | Parrafo reescrito segun la propuesta; se eliminaron la repeticion y "construccion declarada" |
| S11 (media) | estilo | APLICADO | El parrafo de una oracion se unio al final de la formulacion (l.170), junto con guia-2 |
| S12 (media) | estilo | APLICADO | Igual que guia-6 |
| S13 (media) | estilo | APLICADO | "es la referencia de mecanismo, porque es el unico de los tres brazos que simula..." |
| S14 (media) | estilo | APLICADO | "de modo que puede no alcanzar a concluir equivalencia ni diferencia" |
| T01 (alta) | traza | ESCALADO | `\GAPDEC{calibre con que SAP evalua la viabilidad del corredor: la decision que define SAP fija la envolvente nominal de 6.5 a 8.0 mm, y la corrida del Objetivo 2 uso los calibres de 4.91, 7.0 y 7.3 mm con una holgura de 1 mm}` en §SAP. Contradiccion concreta: D-O2.4 (tabla de geometrias) contra `e13_sap.md`, seccion "Viabilidad de corredor (componente 3 de SAP)". El texto sigue la decision, y los recuentos conformes a ella son los de §Corredor (T02). Se escala por analogia con la regla 5 de `overleaf/CLAUDE.md`: la fuente de mas autoridad y la corrida difieren |
| T02 (media) | traza | APLICADO | Se cierra el `\GAPDATO`. Con el recorte por defecto, el criterio se cumplio en el 65.3 % de los 72 pacientes con d = 6.5 y $\epsilon$ = 1, y en el 23.6 % con d = 8.0 y $\epsilon$ = 2. Con el recorte alternativo, en el 62.5 y el 20.8 %. Fuente: `e9ts_resumen.md` :16 y :20, indexado como VIGENTE en `experiments/objetivo2/EXPERIMENTOS.md`. DEC 2026-09-11 (2) pide "Se reportan ambos extremos". "Corredores viables" pasa a "pacientes que cumplen cada criterio" |
| T03 (media) | traza | ESCALADO | `\GAPDEC` reescrito con la contradiccion concreta entre dos decisiones. D-O2.6 (2026-09-22) calcula la densidad "sobre `e9b_densidad_s1.csv`", mientras que DEC 2026-09-14 (#50) dice "E9b se retira como evidencia de densidad" y D-O2.6 no la deroga. El `\GAPDEC` agrega que la definicion implementada solo consta en el codigo |
| T04 (media) | traza | APLICADO | Se cierra el `\GAPDEC` escalado en r01 (guia-8) con el criterio 1 del orquestador. l.180 dice "parches que solo contienen banda en razon de 0.62 respecto de los parches con metal, que son todos los disponibles". l.182 dice "0.62 frente a 1.40 parches de solo banda por parche con metal" (DEC 2026-09-21, R3) |
| T05 (media) | traza | APLICADO | Se cierra el `\GAPDEC` escalado en r01. DEC 2026-09-21 (2) corrige el dato de D4 ("`val` tiene 8 casos, no 5") y fija "el margen `Delta` de D4 se medira sobre 3 pacientes". El texto dice "3 pacientes de validacion con implante real, con varias semillas por caso". No son decisiones contradictorias: la posterior sustituye a la anterior |

## Revision de los GAPDEC escalados en r01 con el criterio del orquestador

| GAP de r01 | Resultado | Motivo |
|---|---|---|
| Proporcion de parches de solo banda | CERRADO | DEC 2026-09-21 R3 da 0.62 (y 1.40) (T04) |
| Pacientes de validacion para $\Delta$ | CERRADO | DEC 2026-09-21 (2) fija 3 (T05) |
| Pacientes del brazo fisico | SE MANTIENE | DEC 2026-09-17 B.2 dice "subconjunto reducido" sin cifra. D4 menciona n = 14 y n = 20 de prueba "para un TOST", pero no dice que sea el subconjunto del brazo fisico, y TM:119 sigue hablando de subconjunto: la decision no da el dato |
| $h = 2\sigma$ | SE MANTIENE | Ni DEC ni PRE §3.1 la justifican ("propia, declarada") |
| Agregacion por paciente | SE MANTIENE | D4 solo dice "pareada (mismos pacientes en los dos brazos)" |
| Escala o regla de W1 | SE MANTIENE | D-O2.1 acepta de antemano "que el W1 puede salir alto" sin fijar escala ni fallo |
| Evidencia del Obj 4 | SE MANTIENE | Ninguna decision la fija |
| Alineacion con la introduccion | SE MANTIENE | #126 ABIERTA; es otra seccion |
| Avisos de r01 (T14 sobre TM:78/:117; T03/T04 sobre TM:77) | SIN MARCA | El texto ya sigue DEC. Solo queda pedir a la autora que alinee `tesis/main.tex` |

## Bajas

Aplicadas:
- guia-10: holgura radial $\epsilon$ e indice de paciente $i$ en la Ec. `eq:mae`.
- guia-11: "69 pacientes sin objeto metalico de la carpeta `dataset6`" (DAT:124-127, DEC 2026-09-10) y "43 volumenes".
- guia-12: "fijan de antemano la magnitud que se mide".
- guia-14: SHA256 y huella por corte (DEC 2026-09-10); remision a §Marco con metal para la localizacion de referencias.
- S15, S16, S17 (l.79, l.203, l.210, l.212), S18, S19, S20, S21 (l.85, l.89, l.91, l.101; l.176 reescrita), S22, S23, S24, S25 (l.38 y l.58), S26.
- T06, T07, T08, T09, T10, T11: este ultimo por remision al subconjunto del brazo fisico. No se copiaron n = 14 y 20: ver la tabla anterior.

No aplicadas:
- guia-13: PRE §3.1 no da la razon de las 50 poses. Abrir otro `\GAPDEC` por un parametro menor no compensa. Queda para la autora.
- guia-14, parte del semimaximo: ninguna fuente de contenido lo define mas alla del nombre.

Cambio minimo fuera de lo senalado: se actualizo el comentario de cabecera del archivo para remitir tambien a esta respuesta.

## GAP (tras r02)

- `\GAPDATO` (9): se cerro el recuento con `d + 2c` (T02) y se abrio el de los parametros de ajuste del
  decodificador (guia-8). El de la heuristica cambio de texto (T07).
- `\GAPDEC` (16): se cerraron la proporcion de solo banda (T04) y la n de validacion (T05). Se abrieron el calibre
  de viabilidad de SAP (T01) y la condicion de fallo de la prueba de superioridad (guia-1). Cambiaron de texto la
  densidad (T03) y el diseno no congelado del sintetizador, que ahora incluye la codificacion (guia-2).
- `\GAPLIT` (0). `docs/literatura/_candidatos.md` no se toco.

## Lint

`python scripts/lint_redaccion.py capitulo3 --compilar`: compila (55 paginas el documento entero).
**Alta 0, media 0, baja 5, `LINT: PASA`.** Las cinco bajas son E-P1 en lineas con parametros de diseno trazados a
DEC, sin cita posible:

| Linea | Parametros | Fuente |
|---|---|---|
| l.176 | 12 mm | TM:79 |
| l.180 y l.182 | 0.62 y 1.40 | DEC R3 |
| l.196 | 8 mm | D-O2.3 |
| l.251 | 25 HU | DEC 2026-09-15 (2) |

## Decisiones de redaccion

- **Cantidades de Kaiser:**
  - "margen cortical de longitud util" ($h$ = 5 mm) es la distancia radial al eje de la regla de longitud util.
  - "holgura radial" ($\epsilon$ = 1-2 mm) es la del criterio de viabilidad $D \geq d + 2\epsilon$.
  - Nunca se dice "holgura" a secas para $h$.
  - El simbolo $c$ queda libre para el centro $\mathbf{c}$.
- **Indice de paciente:** $i$ (por ejemplo, $\mathrm{MAE}_i$). $p$ queda solo para el valor p.
- **MAISI:** no se despliega el nombre en ingles, porque contiene la sigla "AI". Se dice "el generador de volumenes
  de TC de Guo et al." en la primera mencion y "el latente de Guo et al." despues.
- **Protocolo de Peters et al.:**
  - "metricas de Peters et al." designa las tres metricas.
  - "protocolo fisico (de Peters et al.)" designa solo el brazo de simulacion.
- **Negativos sobre la literatura:** se acotan siempre a "las fuentes revisadas".
- **Controles de implementacion frente a falsacion:** a las comprobaciones de consistencia no se les llama "falsables".
  "Controles de consistencia de la implementacion" se distingue de la regla de fallo de un objetivo.
- **Cifras de diseno en DEC:** una cifra que la autora congelo en `docs/01-decisiones.md` entra como hecho. Por ejemplo,
  0.62 de parches de solo banda y 3 pacientes de validacion. `\GAPDEC` solo si dos decisiones se contradicen, si
  decision y corrida difieren, o si ninguna da el dato.
- **Recuentos de viabilidad:** se reportan los dos extremos del criterio. Son $d = 6.5$, $\epsilon = 1$ y
  $d = 8.0$, $\epsilon = 2$, con ambos recortes. Se nombran como "pacientes que cumplen el criterio", no "corredores viables" sueltos.
