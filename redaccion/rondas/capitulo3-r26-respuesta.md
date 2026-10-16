# Respuesta del redactor — capitulo3 — r26 (ronda unica, encargo 2026-10-15c)

Fuentes de las cifras nuevas (overleaf/CLAUDE.md regla 5; ver T14):
- Ajuste del decodificador (L1, AdamW, lr $10^{-4}$, 500 pasos de calentamiento, lote 4, recorte 1.0, 30 000 pasos, 1-2 epocas, validacion cada 1 000 pasos): `experiments/registro/registro_metodos_2026-10-15.md` §2.
- Eje del corredor (rejilla de 3 mm, 3-75 mm, 45 mm detras / 10 mm delante, 81 direcciones, ±20° en pasos de 5°, huecos de 2 mm, 40 mm, picos a 12 mm): registro §3.
- Referencias anatomicas (150 HU, 60 mm, p99.9, 130 mm, 100 mm sostenido 10 mm, 5 mm, p0.1, 25-100 mm, 40 mm; esfera de 12 mm, -200 HU, 2500 HU, 5 mm): registro §4.
- IC90 por anillo (2 000 remuestreos, percentiles 5 y 95, medianas corte-componente-paciente): registro §5.
- Razon de solo banda 0.638 (5 526 frente a 8 656; 0.620 antes de los retiros): registro §7 (`experiments/registro/r_razon_banda_run04.py`).
- Sensibilidad sin `CLINIC_0022`/`0024` (70 casos) e IC95 de W1 (2 000 remuestreos; series de la referencia como fijas): `experiments/objetivo2/e15_w1_sensibilidad.md` l. 8-12; registro §8.
- IC95 de v1 excluye el cero: registro §9 / `experiments/objetivo3/resultados_dec_2026-10-15.md`; DEC 2026-10-15 (4) pto 1. Sin cifras en el cap. 3.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 / T03 | guia, trazabilidad | APLICADO | :85-87: GAPDATO retirado; el ajuste se describe en un parrafo propio (parte ajustada, datos, perdida, optimizador, lote, recorte, parada por 30 000 pasos fijos, validacion que no elige estado). El total de cortes no consta en el registro: se da "entre una y dos epocas", sin GAP reducido (opcion que T03 admite) |
| guia-2 / T04 | guia, trazabilidad | APLICADO | :107: algoritmo de busqueda en un parrafo nuevo (pasos 2-5 del registro §3); la separacion S1 / segundo corredor bajo S1 por picos de 12 mm se nombra como heuristica declarada; lo ya dicho (envolvente, $D$, 8 mm) no se repite |
| guia-3 / T05 | guia, trazabilidad | APLICADO | :117-119: heuristica (crestas, platillo, espinas) y legibilidad (esfera de 12 mm, umbrales) descritas; "cota superior de la localizabilidad, revisada sobre laminas" como en el registro. Se conserva la salvedad "no se ha revisado clinicamente": laminas no es revision clinica, no se contradicen |
| guia-4 / T08 | guia, trazabilidad | APLICADO | sec:v2: el procedimiento del IC90 por anillo se enuncia en la oracion que define el intervalo |
| guia-5 / T06 / T07 | guia, trazabilidad | APLICADO | :222: 0.62 queda como dato previo a los retiros y 0.638 (5 526 frente a 8 656) como razon del modelo evaluado; :232: "0.638 frente a 1.40", sin la salvedad vieja (PAT-168) |
| guia-6 / T09 | guia, trazabilidad | APLICADO | :113: sensibilidad con 70 pacientes, resultado al cap. 4, sin cifras (BITACORA 2026-10-11) |
| guia-7 / T10 | guia, trazabilidad | APLICADO | :535: IC del 95 % por remuestreo de pacientes, 2 000 remuestreos, no preinscrito, resultado al cap. 4, con el limite de e15 (series de la referencia tratadas como fijas). Tabla de diseno: "IC 95 %" (baja, de paso) |
| guia-8 / T11 | guia, trazabilidad | APLICADO | #195 opcion (a): en sec:ap-analisis, $\Delta$ como convencion inspirada en Haber y Barnhart (idea general, ficha "Donde entra"); en Amenazas, que el maximo no es su regla (promedio sin referencia; solo la referencia con referencia), que sus coeficientes crecen con la variabilidad intrametodo (p. 168) y que $s$ y $r$ son estimadores distintos. No se atribuye `max`, el rango ni el TOST a la fuente (PAT-194). Lo ya dicho (2 pacientes, medianas de 5 semillas, margen mas ancho con mas variabilidad) no se repite |
| guia-9 / T01 | guia, trazabilidad | APLICADO | GAPDATO de #194 retirado. Por indicacion del orquestador (capitulo1-r10 ya escribe el mapeo), :425 deja solo la remision a sec:mt-estadistica y la lectura: para la v1 el IC95 excluye el cero y la diferencia a la baja corresponde al caso diferente y no equivalente de Lakens. Las cifras del IC95 (que T01 proponia) van al cap. 4, por BITACORA §2 2026-10-14 (cifras del resultado de v1 en el cap. 4) |
| guia-10 / T02 | guia, trazabilidad | APLICADO | :295: GAPDATO de #184 retirado; la lectura de E-A1 de v2 se dice fijada (lado a lado, exploratoria, con los dos limites de lectura), sin cifras ni nombres de corrida. Se suma a "las ultimas" decisiones del 15 de octubre en Amenazas |
| T12 | trazabilidad (alta) | APLICADO | :214: las dos oraciones del ancho y del truncamiento acotado, en `\REVVISUAL`. :268: la suficiencia ("alcanza ... el deficit esta dentro de la banda") en `\REVVISUAL`; fuera queda solo el hecho de diseno "La version 2 conserva el ancho de 12 mm" (BITACORA §2 capitulo2-r08 e introduccion-r08). `\REVVISUAL` existentes sin tocar |
| T13 | trazabilidad (alta) | APLICADO (sin cambio de texto) | La fuente ya se corrigio: `objetivo3/EXPERIMENTOS.md`:109 y :111 dan el control real de D7 como corrido en `a28`, y RD lo da como trivial. :256 ("el control sobre parches reales resulto trivial ... ida y vuelta exacta") es coherente con ambas |
| T14 | trazabilidad | ESCALADO | Las cifras nuevas salen de `experiments/registro/` y de `e15_w1_sensibilidad.md`, que el encargo fija como fuente, pero no tienen fila en un `EXPERIMENTOS.md` (regla 5). Rutas exactas arriba. La autora agrega filas para `e15` (objetivo2) y `r_razon_banda_run04` (objetivo3). Sin marca en el texto: no hay discrepancia de cifras |
| S1 | estilo | APLICADO | "a la escala de esa variabilidad" |
| S2 | estilo | APLICADO | "En una nota posterior, Bland y Altman~\cite{bland1996...}"; en Amenazas, "Bland y Altman~\cite{bland1986...} juzgan ... y en el mismo articulo advierten" (ficha `bland1986statisticalmeasurement` l. 15-16) |
| S3 | estilo | APLICADO | Las dos oraciones sobre el momento de "las primeras" se funden en una |
| S4 | estilo | APLICADO | "Como el estado final queda mas cerca de lo real dentro de $M$, la sintesis ... se repite con el" |

Bajas: S5 y S11 quedan sin objeto (el parrafo del mapeo y la oracion "a la baja ... solo si" se retiraron por guia-9 y la indicacion del orquestador); S6, S7, S8, S9, S10, S12, S13 y S14 aplicados tal como se proponen (S12: el parrafo de las decisiones queda en cuatro oraciones con verbos distintos, partido para no pasar de 40 palabras).

Arreglo vecino: al anadir la lectura de #184, la correspondencia de #194 y la convencion de #195, la lista de "las ultimas" decisiones del 15 de octubre (Amenazas) se completa con ellas, para que no quede una decision posterior sin fechar (PAT-193).

## Decisiones de redaccion

- Cuando una implicancia decidida pide citar una fuente de respaldo conceptual cuya ficha dice que no contiene la regla concreta (Haber y Barnhart para $\Delta$): en el metodo, "convencion de este trabajo, inspirada en la idea de X de ..."; en Amenazas, que la regla no es la de la fuente, que hace la fuente en su lugar y el efecto que la propia fuente reconoce. Nunca se atribuye la formula a la fuente.
- El mapeo de "no concluyente" con Walker y Nowacki y Lakens vive solo en `sec:mt-estadistica` (cap. 1); el cap. 3 remite y da la lectura aplicada a la v1 ("el IC del 95 % excluye el cero"), sin las cifras, que van al cap. 4.
- Procedimiento de un GAPDATO cerrado por un registro de metodos: se describe en prosa con sus parametros; si un dato del GAP original no consta en el registro (total de cortes), se da la magnitud que si consta (pasos, lote, epocas) y no se abre un GAP reducido salvo que el dato sea necesario para reproducir.
- Truncamiento y suficiencia de $B_\delta$: en `\REVVISUAL` en todas sus apariciones; el hecho de diseno que no afirma suficiencia ("la version 2 conserva el ancho de 12 mm") queda fuera.
- "Espina iliaca posterior" (como en `sec:corredor` y cap. 1) para la EIPS del registro; no "posterior superior".
