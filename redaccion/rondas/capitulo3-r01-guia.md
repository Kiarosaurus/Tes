# Revision guia CS — capitulo3 — r01

Leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (sin patrones VIGENTES en §1; decisiones de §2 respetadas), `redaccion/MAPA.md`, `capitulo3-r00-respuesta.md`, `capitulo3-r01-lint.md`. Cruces: `introduccion.tex` (redactada, marcada DESFASADA en MAPA, #126), `capitulo1.tex`, `capitulo2.tex` y `capitulo4.tex` (esqueletos). Contraste puntual con `experiments/objetivo2/preinscripcion_muestreador.md` §3.1 y §6.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | G-C4 | capitulo3.tex:12 | Los cuatro objetivos del cap. 3 (compuerta, muestreador+SAP, sintetizador, formalizacion SAP/protocolo) no coinciden con los cuatro de la introduccion (modelo 2D, conjunto sintetico, SSIM/MAE, Dice/HD95), ni el diseno experimental responde a la pregunta de `introduccion.tex:21`. El objetivo experimental no queda ligado a las preguntas del bloque (a). | El contenido del cap. 3 sigue `01-decisiones.md`; la correccion es realinear la introduccion (#126). En el cap. 3, una vez alineada, citar los objetivos y la pregunta con `\ref` en lugar de re-enunciarlos, y hasta entonces marcar `\GAPDEC` de la dependencia. |
| guia-2 | alta | G-C6 | capitulo3.tex:209, 231; tab:diseno fila 2 | El Objetivo 2 no tiene regla de decision ni escala de referencia para la distancia de Wasserstein-1 ("se reporta tal como se mide"; preinscripcion §6), asi que ningun valor lo haria fallar (G-A8). Ademas, l. 231 afirma que en las tres filas "el criterio y la regla de decision se fijaron antes de ver el resultado", lo que es falso para la fila 2. | Corregir l. 231 para que no atribuya regla de decision al Obj 2, y declarar con `\GAPDEC` si se fija una escala de lectura de W1 (p. ej. una linea base o la distancia entre los dos brazos clinicos) como analisis no preinscrito, o que resultado contaria como fallo del muestreador. |
| guia-3 | media | G-A7 | capitulo3.tex:12, 187, 231; tab:diseno | La l. 12 dice que cada objetivo "produce una pieza verificable", pero el Objetivo 4 (formalizar SAP y adoptar el protocolo) no tiene fila en tab:diseno ("tres objetivos evaluados") ni evidencia designada. Los seis controles sobre geometria conocida (l. 200) parecen serlo, pero no se atribuyen al Obj 4. | Decir explicitamente que evidencia verifica el Obj 4 (controles de l. 200 y que haria fallar la formalizacion) o declarar que el Obj 4 no se evalua experimentalmente y por que. |
| guia-4 | media | G-C1 | capitulo3.tex:147, 157 | La convencion $h = 2\sigma$ fija toda la escala del muestreador y por tanto la distancia W1, pero no tiene justificacion: solo se dice "propia y declarada". G-C1 pide justificar cada supuesto (por que 2 y no 1 o 3 desviaciones). | Anadir la razon de la convencion si consta en el repositorio; si no consta, `\GAPDEC` sobre la justificacion de $h = 2\sigma$ y mencionarla en validez de constructo. |
| guia-5 | media | G-C8 | capitulo3.tex:225 | Wilcoxon pareado y TOST sobre "la diferencia pareada" sin decir cual es la unidad de emparejamiento (paciente, pose, region de rayas). La l. 47 fija el paciente como unidad de independencia; si se parea por pose o region hay pseudorreplicacion. | Declarar la unidad de analisis de las pruebas del Obj 3 y como se agregan poses/regiones por paciente. |
| guia-6 | media | G-C7 | capitulo3.tex:74, 253, 261 | La extension de la compuerta a MAISI se decidio despues del veredicto negativo y con los mismos 34 pacientes de prueba; eso anade un septimo candidato post hoc que solo puede favorecer un aprobado. Validez interna (l. 253) y de conclusion (l. 261, "una de seis combinaciones") no lo recogen. | Anadir la extension a MAISI a las decisiones posteriores a los datos (l. 253) y a la multiplicidad de l. 261. |
| guia-7 | media | P-MM3 | capitulo3.tex:51, 84, 94 | "Control de calidad del nivel", "cada caso pasa un control de calidad" y "las referencias se localizaron con una heuristica" no se describen ni llevan GAP; un tercero no puede reproducir la cohorte de 72 ni el conteo 57/48/29. | Describir los criterios del control y la heuristica, o marcar `\GAPDATO` como con el algoritmo del eje (l. 86). |
| guia-8 | media | P-MM3 | capitulo3.tex:179, 223, 261 | Cantidades de diseno enunciadas sin valor ni GAP: "una proporcion declarada de parches que solo contienen banda", "subconjunto reducido de pacientes", "pocos pacientes de validacion". "Declarada" sin declarar el valor. | Marcar `\GAPDEC` (discrepancias 4 y 5 de la respuesta r00: cifras en `01-decisiones.md` pero no en `main.tex`) hasta que la autora las pase a una fuente admitida. |
| guia-9 | media | G-T2 | capitulo3.tex:78, 128, 161 | "Brecha" y "grados de brecha" se usan desde la l. 78 y en los controles de falsabilidad (l. 161), pero se definen recien en la l. 191 (Ec. brecha). El lector evalua la falsabilidad sin saber que es brecha. | Adelantar una definicion de una linea en la seccion del muestreador con `\ref{eq:brecha}`, o mover la definicion de SAP antes de §Poses. |
| guia-10 | baja | G-T2 | capitulo3.tex:169, 86 | "2.5D" y "umbral de semimaximo local por objeto" se usan sin definir. Puede resolverlo el cap. 1 (esqueleto). | Definirlos en su primer uso o remitir al cap. 1 cuando exista. |
| guia-11 | baja | G-T3 | capitulo3.tex:202, 255 | $P$ designa una distribucion en la Ec. (w1) y un valor p en "$P = 0.3$"; en l. 225 el valor p es $p$ minuscula. | Usar $p$ en l. 255. |
| guia-12 | baja | G-C5 | tab:diseno; l. 90, 113, 118, 122, 177, 227 | Las variables de sensibilidad (recorte alternativo, calibres 4.91/7.3 mm, cabeza y rosca, macizo/hueco, semimaximo) y la preservacion fuera de $B_{\delta}$ (RMSE, SSIM) no aparecen en la tabla que resume el diseno. | Anadir una columna o nota de sensibilidades por objetivo. |
| guia-13 | baja | P-MM2 | capitulo3.tex:29-30 | La caja de la compuerta aparece al final del diagrama, desconectada, aunque la l. 8 dice que va "antes de ambos". | Moverla arriba o indicar con una flecha lateral que fija el dominio del sintetizador. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP (arquitectura del sintetizador, algoritmo del eje) |
| G-T2 | no cumple (guia-9, guia-10) |
| G-T3 | no cumple (guia-11, baja) |
| G-T4 | cumple (verificacion de cifras: auditor-trazabilidad) |
| G-T5 | cumple (l. 8 justifica el orden; compuerta antes de los componentes) |
| G-T6 | cumple (las 30 claves citadas estan en `overleaf/referencias.bib`) |
| G-A7 (cruce) | no cumple (guia-3) |
| G-B3 (cruce) | no evaluable (capitulo1 en esqueleto) |
| G-C1 | no cumple a medias (guia-4); sintetizador cumple con GAP |
| G-C2 | cumple con GAP (GAPDATO algoritmo del eje; GAPDEC diseno del sintetizador) |
| G-C3 | cumple |
| G-C4 | no cumple (guia-1) |
| G-C5 | cumple con GAP (inversion de metricas de Peters); guia-12 baja |
| G-C6 | no cumple (guia-2); Obj 1 y Obj 3 cumplen con GAP (copia y pegado) |
| G-C7 | cumple a medias (guia-6); cuatro tipos presentes y no pro forma |
| G-C8 | no cumple a medias (guia-5); W1 sin inferencia cumple con GAP |
| G-C9 | cumple con GAP (brazo fisico de Peters como competidor mas fuerte, no ejecutado) |
| P-MM1 | cumple en orden y ligazon a objetivos; relacion con marco teorico no evaluable (capitulo1 en esqueleto) |
| P-MM2 | cumple (guia-13 baja) |
| P-MM3 | no cumple (guia-7, guia-8) |

## Propuestas de criterio
- La rubrica no tiene un criterio explicito en el bloque (c) para "cada objetivo tiene una regla de exito/fallo fijada a priori"; hoy se reparte entre G-A8 (bloque a) y G-C6. Sugiero un G-C propio, porque la regla vive en la metodologia.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Frase de sintesis que atribuye a todos los objetivos una propiedad que solo tienen algunos | G-C6 | "Las tres filas comparten ... la regla de decision se fijaron antes" | nuevo |
| Cantidad de diseno calificada como "declarada", "reducida" o "pocos" sin valor ni GAP | P-MM3 | "junto con una proporcion declarada de parches que solo contienen banda" | nuevo |
| Termino tecnico usado varias secciones antes de su definicion formal | G-T2 | "la distribucion de grados de brecha que resulta se compara" (l. 78) | nuevo |
| Procedimiento nombrado ("heuristica", "control de calidad") sin descripcion ni GAP | P-MM3 | "Las referencias se localizaron con una heuristica" | nuevo |
