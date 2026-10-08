# gaps-r03 — respuesta del redactor

Ronda **acotada**. No hubo reportes de revisores: las filas son los puntos 1-32 de la entrada
`docs/01-decisiones.md` **"2026-10-08 — Decisiones pendientes delegadas al asistente en rol de asesor"**,
que es decision registrada y entra como hecho (regla 3 de `overleaf/CLAUDE.md`). Secciones tocadas:
`introduccion`, `capitulo1`, `capitulo2`, `capitulo3`. No se tocaron: #90 (contingencia de plazo), el tipo de
implante de los 3 pacientes de referencia, la revision multiplanar, el desenlace del suelo, el valor de Delta ni
los `\GAPLIT` previos. Ninguna cifra de implicancias ABIERTAS entra al texto (en particular, ni los ~70 s por
corte de #146 ni nada de #141, #149-#152). Lineas = numeracion final de cada archivo.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| 1. Codificacion y precision | DEC 2026-10-08 (encargo) | APLICADO | `\GAPDEC` cerrado en los cuatro sitios: `introduccion`:46 ("una de esas dos", porque ahi "la tercera" es la de 21.80 HU), `capitulo1`:46 ("la tercera", numeracion del cap. 1), `capitulo2`:86, `capitulo3`:182 (primera del orden a priori y la de todas las corridas). Compresion arcoseno hiperbolico (`pub+asinh`) en coma flotante de 32 bits. Sin nueva cifra de ida y vuelta en el cap. 3 |
| 2. Entrada 2.5D | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo1`:118 cerrado: tres cortes contiguos, "porque un modelo tridimensional completo no cabe en los datos ni en el computo disponibles". Repetido en el parrafo nuevo de `capitulo3`:188 |
| 3. Arquitectura | DEC 2026-10-08 | APLICADO | Parrafo nuevo `capitulo3`:188 (U-Net base 64, multiplicadores 1-2-4-8, atencion en la resolucion mas baja, prediccion `v`, coseno 1000 pasos, AdamW 1e-4, lote 4, parche 256; "sin busqueda de arquitectura"). Prosa alineada en `capitulo1`:108 ("se fijo tal como se entreno"). **`\GAPLIT` nuevo** de la prediccion `v`: ninguna ficha la define; candidato PENDIENTE en `_candidatos.md` |
| 4. Muestreo y semillas | DEC 2026-10-08 | APLICADO | Determinista, 50 pasos (`capitulo1`:110, `capitulo3`:188); 5 semillas por caso como convencion (`capitulo3`:188 y :264, que decia "no esta fijado"). La parte Delta del antiguo `\GAPDEC` de preinscripcion pasa a **`\GAPDATO`** (`capitulo3`:188) |
| 5. Muestreo frente a RePaint y LeFusion | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `capitulo1`:116 y `capitulo2`:28; descripcion completa en `capitulo3`:188 (concatenacion del contexto y de `M`, `G`; perdida solo en `G`, como LeFusion; copia exacta fuera de `G`; sin remuestreo). La frase "no lo recompone en cada paso con el fondo real ruidoso" se apoya en la ficha de LeFusion y en el "no es ninguno de los dos" del punto |
| 6. Desplazamiento mascara/cilindro | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo3`:198 cerrado con lo ya medido: 9 de 57 objetos fragmentados a 2500 HU (`experiments/objetivo2/e8_componentes.md`:33; DEC 2026-09-20 D1) y cuerpo 4.91 mm (Tabla de geometrias). `introduccion`:90 alineada |
| 7. Continuidad en el borde de `B_delta` | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo3`:198 cerrado: salto de HU al cruzar el borde de `G`, en la evaluacion del sintetizador, descriptivo y sin umbral; se conserva el hecho de la medicion previa (#139, sin cifras). "Para los dos brazos" se redacto "los dos brazos que generan artefacto": **interpretacion**, ver pendientes |
| 8. Copia y pegado | DEC 2026-10-08 | APLICADO, a `\GAPDATO` | `capitulo3`:254: HU constante en `M` = mediana de voxeles > 2500 HU en implantes reales de entrenamiento, nunca de prueba; TC intacta fuera de `M`. **`\GAPDATO`** del valor |
| 9. Obj 3 solo con metricas | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo3`:250 cerrado: no hay lector clinico disponible; QC visual de la autora sobre laminas de una muestra fija, como control y no como evaluacion (E-A4, `diseno_A.md`:143) |
| 10. *bone* y *metal integrity* | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `introduccion`:43, `capitulo2`:76, `capitulo3`:240; prosa alineada en `capitulo1`:68. "Conservan su formula e invierten su lectura", mismos pacientes, TC sin metal y regiones que la *streak amplitude*, referencia = valor del protocolo fisico, descriptivas. "Los dos brazos" = sintetizador y protocolo fisico (**interpretacion**, ver pendientes) |
| 11. Contraste de realismo | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo3`:248 y de `introduccion`:41 cerrados; `capitulo3`:252 y Tabla de diseno (:283) alineadas (ya no "distancia entre distribuciones de amplitudes"). Estadisticos sin referencia de DEC 2026-10-07 (2), sinteticos sobre los pacientes de prueba sin metal frente a implantes reales de los 20 de prueba con implante (E-A1, `diseno_A.md`:140), fraccion de cascaras dentro de la envolvente real, descriptivo |
| 12. Regla del suelo | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo3`:304 cerrado: la regla se evalua contra el contraste primario porque Delta es el margen de la equivalencia; en el realismo el sesgo solo se describe por su sentido. "Los dos contrastes que miden la amplitud" se corrigio, porque el realismo ya no mide amplitud. El `\GAPDATO` del desenlace (`capitulo1`:48, `capitulo3`:184) no se toco |
| 13. Subconjunto y prueba y reprueba del brazo fisico | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo3`:260 (numero de pacientes) y :264 (que cambia entre corridas) cerrados: los 14 pacientes de prueba sin metal; dos corridas identicas salvo la semilla del ruido del simulador. Prosa "subconjunto de pacientes" alineada en `introduccion`:56, `capitulo2`:106 y `capitulo3`:308. "Segun el plazo" se conserva (#90) |
| 14. SAP con dos componentes | DEC 2026-10-08 | APLICADO | Fraccion por zona de densidad retirada en todo el documento: `introduccion`:43 (Obj 4), `capitulo1`:92, `capitulo2`:76, `capitulo3`:176 (§Poses: "La unica restriccion anatomica del muestreador es el corredor oseo medido"), :212 (§SAP) y Tabla de diseno (:282). Arand et al. quedan como motivacion y trabajo futuro. Grep de "densidad" en las cuatro secciones: ninguna frase dice que el muestreador se restrinja por densidad |
| 15. Dimension angular de Smith | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `capitulo1`:88, `capitulo2`:74, `capitulo3`:214. Zwingmann et al. gradua solo perforacion (ficha, Materials and Methods p. 1835); el texto de Smith et al. pasa del grado angular 0 al 2 sin grado 1 (ficha `smith2006iliosacral.md`:53, 84-87) |
| 16. Calibre de viabilidad | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `capitulo3`:212 e `introduccion`:43: 7.0 mm y holgura 1 mm (D >= 9 mm), mismo calibre de la brecha, dentro del nominal; 4.91 y 7.3 mm, sensibilidad. Efecto colateral: Tabla de geometrias (:120, :122) y `capitulo3`:109 decian que el calibre nominal es el de la viabilidad de SAP; ahora "viabilidad del corredor en la cohorte" y "brecha y viabilidad en SAP" |
| 17. Escala de lectura de W1 | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `capitulo3`:228-232 e `introduccion`:48. Calculo propio, post hoc ("elegida despues de conocer la distancia del muestreador"), con la aritmetica visible. Verificado: acumuladas 0.69/0.84/0.92 frente a 0.40/0.77/0.885, diferencias 0.29 + 0.07 + 0.035 = **0.395**. **No se escribio el 0.206 del muestreador** (BITACORA §2: los veredictos de Wasserstein-1 van al cap. 4) |
| 18. Remuestreo de W1 | DEC 2026-10-08 | APLICADO, a `\GAPDATO` | `capitulo3`:308: analisis no preinscrito y descriptivo; **`\GAPDATO`** del intervalo. Tabla de diseno (:282) lo nombra |
| 19. h = 2 sigma | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `capitulo3`:168 e `introduccion`:82, como consecuencia de la convencion y no como fuente. Verificado: P(\|Z\| < 2) = 0.954 (0.957 con el truncamiento en 3 sigma), escrito "cerca del 95 %". Termino fijo "margen cortical", no "holgura" (BITACORA §2) |
| 20. Exclusion de 8 mm | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo3`:221 cerrado: convencion sin fuente heredada del codigo del corredor y reutilizada en SAP y en las regiones de medicion |
| 21. Umbral de 10 mm y holgura de Kaiser en el corredor transiliaco-transsacro | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo1`:76 cerrado, como convencion, con `\cite{mclaren2021corridor}` (ficha: "had a safe zone (corridor diameter≥10 mm) for transiliosacral placement", Abstract) y la justificacion dimensional de Kaiser. Para no pasar de 7 oraciones se fundieron dos oraciones previas del parrafo |
| 22. `CLINIC_0022` y `CLINIC_0024` | DEC 2026-10-08 | APLICADO, a `\GAPDATO` | `capitulo3`:97: siguen en la cohorte preinscrita (excluirlos tras verlos seria seleccion posterior) y **`\GAPDATO`** de la sensibilidad sin ellos |
| 23. Objetivo 4 | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `introduccion`:48 (y :43, adopcion de Peters no evaluada) y `capitulo3`:208 |
| 24. Pregunta de investigacion | DEC 2026-10-08 | APLICADO | `introduccion`:21 reescrita desde la *Research Question* de `tesis/main.tex`:62 (frente a copia y pegado y al protocolo fisico; sin Dice/HD95, 2D ni aumento convencional), 35 palabras. Cerrados el `\GAPDEC` de `introduccion`:28 y el de `capitulo3`:13. Encabezado corregido **solo en lo contradictorio**: :11 (ultima oracion, que exigia evaluar la tarea posterior), :13 (metodo 2D con mascara osea), :15 (SSIM, MAE, Dice y HD95) y :17 (hoja de ruta con "segmentacion osea"). Se mantiene el orden de la introduccion |
| 25. Por que un sintetizador aprendido | DEC 2026-10-08 | APLICADO | `\GAPDEC` cerrado en `introduccion`:56 (parrafo propio, para no pasar de 7 oraciones) y `capitulo2`:106; cifras y rasgos del protocolo fisico de la ficha de Peters (ya en `capitulo3`:256 y `capitulo2`:42) |
| 26. Coherencia antes que utilidad | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `introduccion`:52 cerrado; la segunda razon (cohorte anotada insuficiente) ya estaba en la misma oracion previa con remision al alcance |
| 27. Restriccion al tornillo | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `introduccion`:68 cerrado; acotado a "en las fuentes revisadas" (PAT-64) y con la salvedad de #130.3 (la distribucion es de tornillos iliosacros y entra como referencia externa) |
| 28. Ablaciones | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `introduccion`:75 cerrado; **titulo del item cambiado** a "Ablaciones del muestreador"; `capitulo3`:36 alineado |
| 29. Revision narrativa | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo2`:12 cerrado: narrativa y dirigida, no declara bases, cadenas ni criterios |
| 30. Novedad | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo2`:112 cerrado ("se formula, por eso, como una combinacion"); `introduccion`:62 anade la misma combinacion para el sintetizador, sin tocar los tres elementos del aporte de la cadena |
| 31. Zwingmann et al. 2010 | DEC 2026-10-08 | APLICADO | `\GAPDEC` de `capitulo2`:64 cerrado: fuera de la referencia clinica, citada solo de forma descriptiva |
| 32. Cifras de Jacob et al. | DEC 2026-10-08 | APLICADO (parcial) | `capitulo2`:22 sin numeros (Dice, 300, SSIM 0.587 y "<1 %" retirados). Efecto colateral: el SSIM se definia en el encabezado de la introduccion, que se reescribio; ahora se define aqui. **No aplicado en `anexos.tex`:21** (Tabla de comparacion, fuera de las cuatro secciones del encargo): sigue con SSIM 0.587 y Dice 0.72 -> 0.77 |

## GAP por tipo (lint)

| Seccion | Antes (lit/dato/dec) | Despues (lit/dato/dec) |
|---|---|---|
| `introduccion` | 0 / 3 / 15 | 0 / 3 / 1 |
| `capitulo1` | 4 / 2 / 7 | 4 / 2 / 1 |
| `capitulo2` | 1 / 2 / 10 | 1 / 2 / 0 |
| `capitulo3` | 1 / 11 / 22 | 2 / 15 / 2 |
| **Documento** | **6 / 18 / 54** | **7 / 22 / 4** |

Los 4 `\GAPDEC` que quedan son los excluidos por el encargo: #90 (tres sitios) y el tipo de implante de los 3
pacientes de referencia. Abiertos: 1 `\GAPLIT` (prediccion `v`) y 4 `\GAPDATO` (sensibilidad sin los dos casos,
valor de HU de copia y pegado, intervalo de W1, Delta).

Lint por seccion (`gaps-r03-lint-<seccion>.md`): `capitulo1`, `capitulo2`, `capitulo3` **PASA** (`capitulo3` con
los 5 E-P1 bajos de siempre). `introduccion` **FALLA** solo por una E-O1 de 41 palabras en la l. 7 (encabezado,
anterior y no contradictorio, no tocado); las E-O1 de las l. 13 y 21 desaparecieron con la reescritura. Las
oraciones largas que introduje se partieron antes de cerrar. Compilacion del documento entero: compila, 116
paginas, sin citas ni referencias indefinidas y sin Overfull (el de 4.07 pt de `capitulo3` ya no
aparece). Los 8 G-T1 altos del lint global son plantillas sin redactar (resumen, abstract, anexos,
conclusiones, trabajos futuros).

## Puntos que al aplicarlos parecen mal sostenidos (para la autora)

1. **"Para los dos brazos" (ptos 7 y 10).** La decision no dice cuales. Se redacto sintetizador y protocolo
   fisico (los que generan artefacto); si incluye la copia y pegado, cambian `capitulo3`:198 y :240.
2. **Punto 17, cifra 0.206.** La decision la da, pero el cap. 3 no publica veredictos (BITACORA §2); queda para el
   cap. 4. La escala de lectura se eligio conociendo esa distancia, y asi se escribio.
3. **Punto 27.** "Unico implante con distribucion clinica publicada de grados" es exacto solo si se acepta que la
   distribucion es de tornillos iliosacros (#130.3); el texto lo dice para no sugerir lo contrario.
4. **Punto 5.** "No recompone en cada paso con el fondo real ruidoso" sale de la lectura de codigo de #117 (ABIERTA)
   mas el "no es ninguno de los dos" de la decision; si la autora quiere atenerse solo a la decision, basta quitar
   esa clausula en `capitulo1`:116 y `capitulo2`:28.
5. **Punto 3, prediccion `v`.** Sin fuente en el repositorio; abierto `\GAPLIT` y candidato PENDIENTE. El marco
   teorico (cap. 1) solo explica la prediccion del ruido.
6. **Punto 11, termino "envolvente real".** BITACORA §2 reserva "envolvente" para la envolvente osea, pero la
   decision y `capitulo3`:202 (r08) ya dicen "envolvente real"; se mantuvo para no dar dos nombres a lo mismo.
7. **`anexos.tex`:21** conserva las cifras de Jacob et al. (pto 32) y queda fuera de los archivos de este encargo.
8. **Encabezado de la introduccion.** Fuera de lo contradictorio sigue DESFASADO (#126): "escasez de fotones"
   (:5) no es el termino fijo "inanicion de fotones", y "robustos" (:7) esta en la lista negra. No se tocaron.

## Decisiones de redaccion

| Decision | Por que | Donde debe aplicarse igual |
|---|---|---|
| Una convencion sin fuente que la decision justifica "por su consecuencia" se escribe "no tiene fuente y se justifica por su consecuencia: ...", con la consecuencia numerica redondeada ("cerca del 95 %") y sin presentarla como hallazgo | PAT-62, DEC 2026-10-08 pto 19 | `capitulo4`, `conclusiones` |
| Precision numerica float32 = "coma flotante de 32 bits" | E-T1 | todo el documento |
| `bone`/`metal integrity` en sintesis: "conservan su formula e invierten su lectura, con el valor del protocolo fisico como referencia"; nunca "pendiente de invertir" | DEC 2026-10-08 pto 10 | `capitulo4`, `conclusiones` |
| SAP = "dos componentes" (grado de brecha y viabilidad); la densidad, "motivacion y trabajo futuro" | DEC 2026-10-08 pto 14 | `capitulo4`, `conclusiones`, `trabajosFuturos`, resumen y abstract |
| El contraste de realismo se nombra "comparacion de los estadisticos sin referencia" y se resume como "fraccion de cascaras dentro de la envolvente real"; ya no "distancia entre distribuciones de amplitud" | DEC 2026-10-08 pto 11 | `capitulo4` |
| Calculo propio sobre cifras publicadas: "Este trabajo la calcula ... a partir de las distribuciones publicadas por X", con la aritmetica visible y la cita de la fuente de las cifras | PAT-6, E-R6 | todo el documento |
