# Revision guia CS — capitulo3 — r02

Leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (PAT-1 a PAT-13 VIGENTES; decisiones de §2 respetadas), `capitulo3-r01-guia.md`, `capitulo3-r01-respuesta.md`, `capitulo3-r02-lint.md`. Cruces: `introduccion.tex` (redactada, desfasada, #126), `capitulo1.tex` y `capitulo4.tex` (esqueletos).

Respuesta r01: guia-1 a guia-8 quedan resueltos o cubiertos por GAP declarado (no se reportan). guia-10 ("2.5D") y guia-12 (sensibilidades en la tabla) no aplicados con motivo; no se reabren. El lint "AI" de MAISI (rechazado) no es de este dominio.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C9 | capitulo3.tex:220, 222, 226 | El criterio primario (*streak amplitude*) se elige porque la copia y pegado "no puede producir [rayas] por construccion". Asi, la unica prueba con regla fijada (Wilcoxon de superioridad) compara contra una linea base que por diseno obtiene cero en esa magnitud y dificilmente puede fallar (G-A8). La comparacion que si puede fallar es la TOST contra el protocolo fisico, y su permanencia esta en `\GAPDEC` (l. 226). | Decir que resultado de la prueba de Wilcoxon contaria como fallo, una vez definida la inversion de la metrica. Si no hay ninguno, presentarla como comprobacion de cordura y declarar que la prueba decisiva del Obj 3 es la TOST, con su dependencia del GAP de l. 226. |
| guia-2 | media | G-C2 | capitulo3.tex:170 (y 60, 69, 71) | El sintetizador usa "la codificacion multiventana", pero no se dice cual de las tres probadas en la compuerta (ventanas publicadas, techo de 20 000 HU o arcoseno hiperbolico). La l. 71 dice que la de ventanas publicadas recorta el metal a 2000 HU. Tampoco se dice si la ida y vuelta de la codificacion sola, sin autoencoder, conserva los HU. La l. 9 promete que la compuerta "decide en que representacion puede operar el sintetizador", y el capitulo no lo cierra. | Nombrar la codificacion que usa el sintetizador y su error de ida y vuelta sin autoencoder, o marcar `\GAPDEC`. |
| guia-3 | media | G-C7 | capitulo3.tex:58, 254 | La l. 58 dice que la regla de la compuerta se escribio despues de una exploracion "sobre la cohorte completa" (lo que incluye a los 34 pacientes de prueba) que ya habia quedado por encima del criterio. La validez interna (l. 254) enumera las decisiones tomadas despues de ver datos y omite esta: el umbral y las seis combinaciones se fijaron conociendo el resultado preliminar sobre la particion de prueba. | Anadir a la validez interna que la regla se fijo tras una exploracion que incluia la particion de prueba, y en que sentido podia sesgar el veredicto. |
| guia-4 | media | G-C7 | capitulo3.tex:254 | Patron PAT-13 reincide. "La distribucion se congelo antes de medir" dice mas que el registro de l. 127 ("antes de calcular cualquier distancia contra las distribuciones clinicas"). Los corredores ya estaban medidos al congelar: $\sigma_a$ usa la mediana $L = 138$ mm de la cohorte (Tabla `tab:preinscripcion`), y la fraccion de limpieza se fijo despues de inspeccionar resultados (l. 91). | Usar la formula de l. 127: "antes de calcular cualquier distancia contra la referencia clinica". |
| guia-5 | media | G-C5 | capitulo3.tex:192; tab:diseno fila 2 | SAP se presenta como la metrica del trabajo, con tres componentes (grado de brecha, fraccion por zona de densidad y viabilidad del corredor), pero la fila 2 de la tabla solo lista la distribucion de grados como variable dependiente. No se dice como se reportan los otros dos componentes (por pose, por caso, agregados) ni si SAP produce un valor unico o un vector. | Anadir a la fila 2 la viabilidad y la fraccion por zona de densidad, con su unidad y su nivel de reporte, o decir que son descriptivas. La definicion de la fraccion ya tiene `\GAPDEC` (l. 166). |
| guia-6 | media | G-A8 | capitulo3.tex:162 vs 210 | "El diseno se declaro falsable en tres puntos": los tres puntos son comprobaciones de la implementacion (brecha nula en el eje, monotonia, ninguna pose sin calificar), no condiciones en que el muestreador fallaria como modelo. Mas abajo, la l. 210 reconoce que el Obj 2 no tiene regla de fallo. Llamar "falsable" al diseno oculta esa ausencia. | Llamarlos "controles de consistencia de la implementacion" (o equivalente) y dejar la cuestion de falsabilidad del Obj 2 solo en el `\GAPDEC` de l. 210. |
| guia-7 | media | G-T2 | capitulo3.tex:83, 89, 147, 158 | "Holgura" de Kaiser et al. designa dos cantidades distintas. Una es la holgura de 5 mm hasta la cortical de la regla de longitud util (l. 83, $h$, que fija toda la escala de las perturbaciones). La otra es la holgura radial de 1 a 2 mm del criterio de viabilidad (l. 89, $c$). El lector no sabe cual de las dos es "la holgura de 5 mm que ya adopta el marco" (l. 158). Tampoco sabe por que una holgura definida para la longitud util sirve como escala de la perturbacion transversal. | Dar un nombre distinto a cada una (p. ej. "margen cortical de longitud util" frente a "holgura radial") y decir en §Poses por que $h$ se aplica en el plano perpendicular al eje, o marcarlo en el `\GAPDEC` de $h = 2\sigma$. |
| guia-8 | media | P-MM3 | capitulo3.tex:60, 69 | Patron PAT-4 reincide. La compuerta evalua "un autoencoder variacional" preentrenado y "una version con el decodificador adaptado", pero no nombra el modelo (solo se infiere en l. 172 que es el de Stable Diffusion 1.5). Tampoco describe como se adapto el decodificador (datos, particion, entrenamiento). Un tercero no puede reproducir las seis combinaciones. | Nombrar el autoencoder en §Compuerta y describir la adaptacion del decodificador, o marcar `\GAPDATO`. |
| guia-9 | media | P-MM3 | capitulo3.tex:119 | Patron PAT-4 reincide. Los 79 componentes de los que sale el cuerpo de 4.91 mm, que es la mascara que se sintetiza, se "seleccionaron por un filtro geometrico" que no se describe (que medidas, que umbrales). | Describir los criterios del filtro o marcar `\GAPDATO`. |
| guia-10 | baja | G-T3 | capitulo3.tex:60, 89, 131, 226, 256 | Hay simbolos con dos significados en el mismo capitulo. $c$ es la holgura radial (l. 89) y $\mathbf{c}$ el centro anclado (l. 131). $p$ es el indice de paciente en la Ec. `eq:mae` (l. 60) y el valor $p$ en las l. 226 y 256. La decision de la bitacora sobre $p$ minuscula choca con el indice. | Renombrar la holgura radial (p. ej. $\epsilon$) y el indice de paciente (p. ej. $i$), manteniendo $p$ para el valor p. |
| guia-11 | baja | G-T4 | capitulo3.tex:95, 119 | Posible reincidencia del patron PAT-10. En la l. 95, "69 pacientes sin metal" no concuerda con los 66 pacientes del grupo 3 (l. 48). En la l. 119, "43 casos" no dice si son pacientes o volumenes. | Precisar la unidad (paciente o unidad de volumen) en ambos recuentos; el auditor verifica la cifra. |
| guia-12 | baja | G-C6 | capitulo3.tex:232 | Patron PAT-1 reincide, atenuado. "Los tres fijan de antemano que se mide", pero para el Obj 3 siguen sin fijar la inversion de las metricas (l. 218), la definicion de la copia y pegado (l. 222) y la agregacion por paciente (l. 226). | "Los tres fijan de antemano la magnitud que se mide" o anadir que en el Obj 3 su definicion operativa sigue pendiente. |
| guia-13 | baja | G-C1 | capitulo3.tex:152 | "Poses por caso: 50" figura con procedencia "Declarado" y sin razon (precision de la distribucion por caso, costo, estabilidad de $W_1$). | Dar la razon si consta en la preinscripcion o marcarla en el mismo `\GAPDEC` de la escala. |
| guia-14 | baja | P-MM3 | capitulo3.tex:48, 52, 87 | Patron PAT-4 reincide en tres procedimientos nombrados sin describir. En la l. 48, "huella del volumen completo / de cada corte" (que huella y que coincidencia cuenta como duplicado parcial). En la l. 52, "localizacion automatica de referencias anatomicas" del control de nivel, sin remitir al `\GAPDATO` de l. 95 si es la misma heuristica. En la l. 87, "umbral de semimaximo local por objeto". | Una oracion por procedimiento o una remision al GAP existente. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP (arquitectura del sintetizador, algoritmo del eje, heuristica de referencias) |
| G-T2 | no cumple (guia-7) |
| G-T3 | no cumple (guia-10, baja) |
| G-T4 | cumple, salvo guia-11 (baja); verificacion de cifras: auditor-trazabilidad |
| G-T5 | cumple (l. 9 justifica el orden; la compuerta encabeza la figura) |
| G-T6 | cumple (sin claves nuevas respecto de r01; el lint no reporta citas faltantes) |
| G-A7 (cruce) | cumple con GAP (evidencia del Obj 4, `\GAPDEC` l. 188) |
| G-A8 (cruce) | cumple con GAP para el Obj 2 (`\GAPDEC` l. 210); no cumple en la redaccion de l. 162 (guia-6) ni en la prueba de superioridad del Obj 3 (guia-1) |
| G-B3 (cruce) | no evaluable (capitulo1 en esqueleto) |
| G-C1 | cumple con GAP ($h = 2\sigma$, ancho de $B_{\delta}$ justificado en su sentido); guia-13 baja |
| G-C2 | no cumple a medias (guia-2); el resto cumple con GAP |
| G-C3 | cumple |
| G-C4 | cumple con GAP (desalineacion con la introduccion, `\GAPDEC` l. 13; #126) |
| G-C5 | no cumple a medias (guia-5); inversion de metricas cumple con GAP |
| G-C6 | cumple con GAP (regla del Obj 2, copia y pegado, agregacion); guia-12 baja |
| G-C7 | no cumple a medias (guia-3, guia-4); cuatro tipos presentes y no pro forma |
| G-C8 | cumple con GAP (agregacion por paciente, intervalo de $W_1$, $\Delta$) |
| G-C9 | no cumple a medias (guia-1); la permanencia del brazo fisico cumple con GAP |
| P-MM1 | cumple en orden y ligazon a objetivos; la relacion con el marco teorico no es evaluable (capitulo1 en esqueleto) |
| P-MM2 | cumple |
| P-MM3 | no cumple (guia-8, guia-9, guia-14) |

## Propuestas de criterio
- Se mantiene la de r01: un criterio del bloque (c) que exija, para cada objetivo, una regla de exito o fallo fijada a priori, y que distinga los controles de implementacion de la falsacion del objetivo (caso guia-6).

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Procedimiento nombrado sin descripcion ni GAP | P-MM3 | "seleccionados por un filtro geometrico y no clinico" | PAT-4 |
| Integridad de la preinscripcion afirmada mas fuerte que el registro | G-C7, G-T4 | "la distribucion se congelo antes de medir" | PAT-13 |
| Frase de sintesis que atribuye a todos los objetivos una propiedad parcial | G-C6 | "Los tres fijan de antemano que se mide" | PAT-1 |
| Unidad de recuento ambigua entre paciente y volumen | G-T4 | "el maximo observado en 69 pacientes sin metal" | PAT-10 |
| Un mismo termino designa dos cantidades distintas de la misma fuente | G-T2 | "holgura de 5 mm" y "holgura radial de 1 a 2 mm" | nuevo |
| Un simbolo se reutiliza para dos cantidades en el mismo capitulo | G-T3 | "$c$ vale entre 1 y 2 mm" / "Sea $\mathbf{c}$ el centro" | nuevo |
| Comprobaciones de implementacion presentadas como falsabilidad del objetivo | G-A8 | "El diseno se declaro falsable en tres puntos" | nuevo |
| Metrica primaria elegida porque la linea base no puede producirla | G-C9 | "la unica que la insercion por copia y pegado no puede producir" | nuevo |
