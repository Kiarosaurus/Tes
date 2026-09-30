# introduccion — r05 (corregir, alcance acotado, ultima ronda) — respuesta del redactor

Alcance: solo `Objetivos de investigación`, `Justificación` y `Alcance y limitaciones / restricciones`.
No se tocaron el encabezado ni la Formulación del problema. Los títulos no cambian.

Fuentes abreviadas: TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex`; IMP = `docs/04-implicancias.md`.

Criterio de la ronda, según indicó el orquestador: cada salvedad de alcance se dice una vez y las demás
apariciones se eliminan o remiten; ningún párrafo supera 7 oraciones; solo se agrega el texto mínimo que
exige un hallazgo. Tras la ronda, el párrafo más largo de las tres subsecciones tiene 7 oraciones (Obj. 4
sin contar su título en negrita, párrafo de falsabilidad y justificación computacional).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| lint l. 7, 13, 21 (E-O1) | lint | ESCALADO (fuera de alcance) | Encabezado y Formulación, excluidos por la autora y DESFASADOS (#126). Dentro del alcance, el lint no marca nada |
| guia-1 | guia | APLICADO | El hallazgo se enuncia en lo que el Obj. 1 mide: "ninguna de las seis combinaciones bajó de 25~HU, y que en el autoencoder entrenado con TC la sola saturación a su rango de salida ya superaba ese criterio (Sección~\ref{sec:obj1})". Fuente: TM l. 77 ("with all 34 patients above the threshold in every combination"; "Clipping the held-out volumes to that range, with no model involved, already yields ... above the 25 HU criterion"). Sale el mecanismo (rangos que excluyen hueso denso y metal), que es interpretación y no medida. Sin cifras nuevas: C3 l. 75 deja los valores para resultados |
| S01 | estilo | APLICADO | La utilidad excluida queda dicha en la exclusión 1 del alcance. Obj. general: "El único implante que se sintetiza es un tornillo iliosacro (véase el alcance)". Justificación: sale "no por una mejora de segmentación que aquí se mida" de la primera oración, y la cuarta queda como remisión: "pero esa utilidad no se mide aquí (véase el alcance)". Se conserva esa remisión porque, sin ella, la motivación de fondo se leería como promesa (G-A5) |
| S02 | estilo | APLICADO | Sale "El Objetivo~3 responde a ese hallazgo sintetizando en el dominio de imagen." (l. 62) y el inciso "por el veredicto del Objetivo~1" (alcance). La relación veredicto → dominio de imagen queda solo en l. 46 |
| S03 | estilo | RECHAZADO | La formulación propuesta ("la prueba solo fallaría si el sintetizador no generara rayas") afirma qué resultado haría fallar la prueba. C3 l. 217 deja eso abierto con `\GAPDEC` ("qué resultado ... contaría como fallo ... o si la prueba decisiva ... es la de equivalencia"), y la introducción lleva el mismo `\GAPDEC`. Escribirla resolvería por inferencia una decisión pendiente (regla dura 1 y 3 de `overleaf/CLAUDE.md`). La consecuencia que sí da la fuente (C3 l. 217: "por sí sola, no dice si las rayas generadas se parecen a las reales") ya está en el texto |
| S04 | estilo | APLICADO (con otra forma) | Sale "clínica": "produce a la vez una distribución de poses del implante y la apariencia de su artefacto". No se agrega "comparable con la referencia clínica": el Obj. 2 ya dice que se compara, y sin regla de decisión "comparable" sería otro juicio |
| S05 | estilo | APLICADO | "En los que acotan el \emph{inpainting} a la máscara no hay un mecanismo para los cambios de intensidad que el objeto generado induce fuera de ella, y en ninguno hay una señal de entrenamiento para esos cambios." Ficha `zhang2025diffboost` (Alg. 1, p. 3676) |
| S06 | estilo | APLICADO | "Esos autores reportan en S1 un área transversal mínima de la zona segura de 222~mm$^2$ en sacros dismórficos frente a 346~mm$^2$ en normales, pero recogen un estudio previo que no halló diferencia." Ficha `gardner2010safezones`, fila "222 mm2 [standard deviation {SD}, 67] versus 346 mm2 [SD, 71]" (Resultados, p. 624). Se parte la oración anterior en dos para no pasar de 40 palabras |
| S07 | estilo | APLICADO | Obj. 2: "de un tornillo iliosacro, que une el ilion con el sacro y se modela como un cilindro paramétrico y rígido". Limitaciones: "la de síntesis es el cilindro paramétrico liso" (se conserva "liso", que en C3 l. 182 es el contraste con la máscara umbralizada) |
| S08 | estilo | APLICADO (con otra forma) | "La síntesis opera sobre parches alrededor del implante, y dentro de cada parche solo genera la región $G$; fuera de ella copia el volumen de origen (Sección~\ref{sec:sintetizador})." Fuente: C3 l. 172. Sale "en el dominio de imagen", ya dicho en el Obj. 3 y en l. 46 (PAT-46) |
| S09 | estilo | APLICADO | Limitaciones de apariencia en dos párrafos: comparación (observaciones reales, protocolo físico y truncamiento de $B_{\delta}$; 4 oraciones) y desplazamientos de dominio más estado del Obj. 3 (5 oraciones) |
| S10 | estilo | APLICADO | Se corta tras el `\GAPDEC` del implante (4 oraciones). El segundo párrafo abre con "En el nivel sacro, la comparación con la referencia clínica se limita a S1." y cierra con la síntesis (4 oraciones) |
| S11 | estilo | APLICADO | "La desviación estándar de las perturbaciones del eje se fija en la mitad del margen cortical de longitud útil de 5~mm que exigen Kaiser et al. \GAPDEC{justificación de la convención $h = 2\sigma$}". Término fijo de BITACORA §2 (2026-09-29). Sin ordinal (ver S17) |

## Hallazgos bajos

| Hallazgo | Decision | Detalle |
|---|---|---|
| guia-2 | NO APLICADO | Pide texto nuevo en el Obj. 2 y la regla de la ronda es no agregar salvo lo mínimo. El alcance ya dice que el segundo corredor queda fuera de la comparación y que su muestreo no se ha ejecutado (`\GAPDATO`). Queda para la autora si el Obj. 2 lo nombra como reporte descriptivo |
| guia-3 | APLICADO | En el Obj. 1, en lugar de "El criterio se aplica a 34 pacientes de prueba": "La regla de la compuerta examina seis combinaciones, de dos variantes del autoencoder y tres codificaciones, sobre 34 pacientes de prueba, y aprueba si alguna cumple el criterio (Sección~\ref{sec:obj1})". Fuente: TM l. 77, C3 l. 71. Va en l. 37 y no en l. 48 porque "la regla de la compuerta" ya aparece en l. 46. En l. 48, "Su regla operativa" pasa a "Su regla" |
| guia-4 | APLICADO | "Entre los candidatos a la cohorte del Objetivo~2, la discordancia de nivel excluyó a 11 de 34 ..." (C3 l. 52: los 34 y los 57 suman los 91 con S1 localizado). Se aplica junto con T01 |
| S12 | ESCALADO | El argumento nuevo es válido: la decisión de BITACORA §2 (2026-09-30) reserva "componentes" para la cadena y los objetos metálicos, y las partes de SAP son un tercer sentido (PAT-14). Pero C3 l. 189 dice "SAP tiene tres componentes", y cambiarlo solo aquí rompería E-T1 entre capítulos; no puedo tocar C3. La decisión es del documento entero |
| S13 | APLICADO | "los objetos metálicos alargados extraídos con un umbral fijo aparecen fragmentados" (BITACORA §2, 2026-09-29; IMP #95) |
| S14 | APLICADO | "sobre conjuntos de pacientes que el artículo llama clínicamente representativos, el metal se inserta en ubicaciones que llama pertinentes" |
| S15 | APLICADO | Sale "El muestreador no se ajustó a ellas."; lo dice l. 62 |
| S16 | APLICADO | "No todos los objetivos fijan de antemano qué resultado los haría fallar; el Objetivo~1 sí lo fija." |
| S17 | APLICADO (solo l. 78) | Las convenciones abren por su objeto ("Ninguna fuente revisada calibra el ancho ...", "Los límites de grado ...", "Los cuatro grados ...", "La desviación estándar ..."). En l. 76 se dejan los ordinales de los supuestos, porque sin ellos el lector pierde el recuento que la oración inicial anuncia |
| S18 | APLICADO | "El aporte de este trabajo se limita a emplear esas ventanas como codificación de la entrada para generar." |
| S19 | APLICADO (con otra forma) | "En CTPelvic1K son 14 (véase la justificación), y no está verificado que sus anotaciones estén disponibles localmente." Oración aparte para no pasar de 40 palabras |
| S20 | APLICADO | "Con la misma regla y sobre los mismos pacientes de prueba se examinó después un autoencoder entrenado con TC (Sección~\ref{sec:obj1})." (junto con T03) |
| S21 | APLICADO (con otra forma) | La propuesta ("no genera cambios de intensidad fuera de la máscara") es falsa para Zhang et al., que genera el corte entero (S05, E-R6). Queda: "no liga al objeto generado los cambios de intensidad fuera de su máscara, y el artefacto metálico no queda dentro del implante" |
| T01 | APLICADO | "la discordancia de nivel excluyó a 11 de 34 ... y a 7 de 57 sin objeto" (C3 l. 52). Aviso al orquestador: C3 l. 253 lleva la formulación imprecisa ("el control de nivel") |
| T02 | APLICADO | "Si esa revisión mostrara un fallo de la variante, se reabriría su elección como variante principal, y con ella cambiarían los diámetros de corredor, las poses y los grados de brecha de la cohorte." Fuente: IMP #123 (ABIERTA; se enuncia como condición, no como hecho) |
| T03 | APLICADO | Remisión a `sec:obj1` (C3 l. 75) |

Cambios mínimos no señalados, derivados de la regla de la ronda (PAT-46):
- l. 76: sale "si se mantiene dentro del plazo"; la contingencia de plazo ya está en la justificación y en el `\GAPDEC` de las limitaciones de apariencia. Queda la remisión "(véanse las limitaciones)".
- l. 78: sale "que, por diseño, trunca las rayas lejanas", que se repetía en las limitaciones de apariencia; allí queda como "Como $B_{\delta}$ trunca por diseño las rayas lejanas ...".

## GAP

- Abiertos: ninguno. Cerrados: ninguno. `\GAPLIT` nuevos: ninguno, sin candidatos.
- Totales de la sección según el lint: lit 0, dato 5, dec 16 (sin cambio). MAPA sin cambios.
- Lint: en el alcance, 0 altas, 0 medias y 0 bajas. En el archivo, 0/3/1, todas en l. 7, 13 y 21 (fuera del alcance). Compila en 67 páginas.

## Para la autora (escalados)

1. **Encabezado y Formulación (lint l. 7, 13 y 21):** siguen DESFASADOS (#126, #128.7).
2. **(bajo) "Componentes" de SAP (S12, re-apertura de guia-4 r04):** ¿las tres partes de SAP pasan a llamarse "medidas" en todo el documento, incluido C3 l. 189, para respetar la reserva de "componentes" (BITACORA §2, 2026-09-30), o se mantiene "componentes" y se amplía esa reserva?
3. **(bajo) Segundo corredor bajo S1 (guia-2):** ¿el Obj. 2 declara que sus resultados en ese corredor son descriptivos, o quedan fuera del objetivo?

Implicancias: sin implicancias nuevas sobre la tesis.

## Decisiones de redaccion

- Un resultado propio se enuncia en lo que el diseño del objetivo mide (umbral superado o no, cota), no en el mecanismo que lo explica; el mecanismo, si se conserva, va marcado como interpretación.
- Una salvedad de alcance vive en Alcance; en objetivos y justificación queda, como mucho, una remisión "(véase el alcance)" y solo donde su ausencia haría leer una promesa.
- Una negación que cubre varias fuentes se parte por subgrupo cuando no vale igual para todas ("en los que acotan ... no hay mecanismo; en ninguno hay señal").
- Una convención propia se redacta como fijación ("se fija en"), nunca como igualdad hallada ("equivale a").
- En listas de convenciones, cada oración abre por el objeto que fija, no por un ordinal.
