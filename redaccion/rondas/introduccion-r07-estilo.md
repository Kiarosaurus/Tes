# Revision de estilo — introduccion — r07

Fuentes leidas: `redaccion/ESTILO.md`, `overleaf/CLAUDE.md` (tabla de terminos), `redaccion/BITACORA.md`
(§1 y §2), lint `introduccion-r07-lint.md` (no se repiten la oracion de 41 palabras de l.7 ni
"robustos" como palabra), `redaccion/ENCARGO_2026-10-15.md`. `muestras_autora.md` esta vacio. No hay
respuesta r06. Fichas cotejadas: `liu2021ctpelvic1k`, `kazerouni2023diffusionsurvey`,
`chen2024tumorsynthesis`, `selles2024marreview`, `xie2024implantsegmentation`.

Nota: el GAPDATO de l.90 ("no existe aun resultado del Objetivo 3") ya lo cubre el encargo
(punto 13 y 15 de DEC 2026-10-15) y es trazabilidad, no estilo; no se reporta aqui.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S01 | alta | E-R2, E-P3 | l.7, ultima oracion | "Esta distribucion produce una representacion reducida ... y limita el desarrollo de modelos" | La ficha dice que CLINIC-metal se retira del entrenamiento supervisado ("taken off in our supervised training phase"): la representacion es nula, no "reducida", y el efecto sobre los modelos es justo lo que esta tesis no mide. Propuesta: "En el entrenamiento supervisado de Liu et al. no entra ningun volumen con metal \cite{liu2021ctpelvic1k}." Eliminar "y limita el desarrollo de modelos ..." |
| S02 | alta | E-M4 | l.9, ultima oracion | "Los modelos de difusion latente reducen el costo ... mientras que ControlNet permite" | El parrafo presenta la difusion latente y ControlNet como las herramientas del trabajo, y l.13 dice "sin espacio latente". El lector tiene que adivinar por que se introducen. Anadir la consecuencia: "La compuerta del Objetivo~1 examina si esa ruta latente conserva los HU; su veredicto negativo llevo el sintetizador al dominio de imagen (vease el Objetivo~1)." |
| S03 | media | E-R2, E-P4 | l.3, primera oracion | "constituye una tarea relevante para el analisis de lesiones" | "La segmentacion automatica de los huesos en tomografias computarizadas (TC) pelvicas se usa en el analisis de lesiones, la reconstruccion tridimensional y la planificacion quirurgica." |
| S04 | media | E-M3, E-M8 | l.3, ultima oracion | "siendo esta ultima una de las condiciones mas dificiles para la segmentacion" | Cortar el gerundio y dar a la cita su verbo: "Liu et al.~\cite{liu2021ctpelvic1k} senalan los artefactos metalicos como la mas dificil de esas variaciones." (la ficha dice "the most difficult to handle") |
| S05 | media | E-T1 | l.5, tercera oracion | "el endurecimiento del haz, la escasez de fotones y las inconsistencias" | "inanicion de fotones" (tabla de terminos). Patron PAT-14 reincide |
| S06 | media | E-T1 | l.5, primera oracion | "suelen manifestarse como bandas oscuras, regiones brillantes y trazos" | "zonas oscuras" (decision de bitacora 2026-09-29: "banda" reservada a $B_\delta$). Patron PAT-14 reincide |
| S07 | media | E-T2 | l.5, primera oracion; l.41 | "trazos en forma de rayas" | Primera aparicion con el termino fijo: "zonas oscuras, zonas brillantes y rayas (\emph{streaking})". En l.41, "las rayas" sin repetir el ingles |
| S08 | media | E-R5, E-T1 | l.5 ("Estos artefactos inducidos por metal"); l.17 | "Estos artefactos inducidos por metal pueden ocultar los limites" | "Estos artefactos metalicos pueden ocultar los limites ..."; en l.17, "los artefactos metalicos". El documento usa "artefacto metalico" (tabla de terminos). Patron PAT-14 reincide |
| S09 | media | E-M4, E-P3 | l.5, ultima oracion | "reproducir de manera exacta ... requiere normalmente informacion del dominio de proyeccion" | Quitar "normalmente" (certeza sin fuente) y decir la consecuencia para este trabajo: "Por esta razon, reproducir la formacion del artefacto requiere informacion del dominio de proyeccion, como los sinogramas y los parametros de adquisicion, que este trabajo no usa." |
| S10 | media | E-R4 | l.7 y l.52; l.74 | "publican anotaciones oseas para 14 de los 75 volumenes" | Las cifras 14/75/61 se dan en l.7 y otra vez en l.52. Dejarlas en l.7; en l.52: "Como se expuso al inicio del capitulo, CTPelvic1K tiene pocos volumenes con metal anotados." y en l.74 "(vease el inicio del capitulo)". Patron PAT-102 reincide |
| S11 | media | E-O3 | l.9, tercera oracion | "En este contexto, los modelos de difusion ofrecen" | Eliminar el conector: "Los modelos de difusion se han usado para sintetizar imagenes medicas \cite{kazerouni2023diffusionsurvey}." |
| S12 | media | E-R2 | l.9, tercera oracion | "ofrecen un mecanismo para aprender distribuciones complejas" | Ver S11: decir para que se han usado, no que "aprenden distribuciones complejas" |
| S13 | media | E-R3, E-R4 | l.11 (todo el parrafo); l.15, primera oracion | "Esa evaluacion presupone, sin embargo, que lo sintetizado sea plausible" | El parrafo defiende la evaluacion por tarea posterior y la retira en la ultima oracion; la misma salvedad vuelve en l.15, l.52 y l.74. Reescribir l.11 con la tesis al inicio: "La sintesis condicionada se ha evaluado tambien por su utilidad en una tarea posterior (\textit{downstream task}) \cite{chen2024tumorsynthesis}, una evaluacion que presupone que lo sintetizado sea plausible." Eliminar "Esta forma de evaluacion resulta pertinente ..." y en l.15 quitar "y no su utilidad para entrenar una red de segmentacion". Patron PAT-46 reincide (ERRADICADO) |
| S14 | media | E-M4, E-V1 | l.13, primera oracion | "A partir de esta necesidad, la presente investigacion propone" | La "necesidad" no se nombra en el parrafo anterior. "Este trabajo propone una cadena de sintesis de dos componentes que ..." Patron PAT-34 reincide |
| S15 | media | E-R2 | l.48, sexta oracion | "es un control de cordura que supera cualquier brazo que genere algo" | "La superioridad frente a la insercion por copia y pegado, que no produce rayas, es un control de cordura: cualquier brazo que genere rayas la alcanza, y ningun resultado suyo cuenta a favor del sintetizador." |
| S16 | media | E-T1 | l.56, ultima oracion | "Si alcanza la equivalencia con la simulacion fisica es justamente lo que" | "Si alcanza la equivalencia con el protocolo fisico es lo que pone a prueba el Objetivo~3; esa equivalencia es una pregunta de este trabajo y no una premisa." (decision 2026-10-05: "protocolo fisico" para el brazo; "justamente" es enfasis de relleno) |
| S17 | media | E-R1 | l.64, l.68, l.72 (aperturas) | "tiene dos partes:" / "acotado en cuatro puntos:" / "cuatro tareas, cada una" | Tres aperturas seguidas por recuento. l.64: "El muestreador no se construye con los datos contra los que se compara, y el veredicto negativo del Objetivo~1 aporta un hallazgo propio." l.68: "El alcance se acota por la cohorte, el implante, el nivel sacro y la forma de la sintesis." Patron PAT-114 reincide |
| S18 | media | E-M1 | l.86 (todo el parrafo) | "Las cifras principales del Objetivo~2 dependen de una variante de la segmentacion" | Parrafo cajon: variante, etiqueta de S1, discordancia de nivel y envolvente sin oracion tematica comun. Abrir con: "La medicion del corredor depende de la segmentacion anatomica, de su etiqueta de S1 y de la envolvente osea, y ninguna esta verificada en todos los casos." Patron PAT-33 reincide |
| S19 | baja | E-O3 | l.17 | "Posteriormente, se describe ... Finalmente, se presentan y discuten" | "El Capitulo I presenta ...; el Capitulo II, ...; el Capitulo III describe ...; el Capitulo IV presenta y discute ...", sin conectores de secuencia |
| S20 | baja | E-P3 | l.77, segunda oracion | "no es consistente entre estudios" | "Los estudios revisados no coinciden en el efecto del dismorfismo sobre el tamano de la zona segura." (forma decidida el 2026-09-30) |
| S21 | baja | E-IA | l.62, quinta oracion | "Del sintetizador se reclama la combinacion del objeto metalico rigido" | Calco de *claim*: "El aporte del sintetizador es la combinacion del objeto metalico rigido, ..., y no cada pieza por separado." |

## Impresion general
Leida seguida, la seccion tiene dos voces: los parrafos de contexto (l.3-17) suenan a resumen generico ("constituye una tarea relevante", "En este contexto", "A partir de esta necesidad", gerundio "siendo") y no usan los terminos fijos del documento; desde los objetivos, el texto es sobrio pero denso.
El patron dominante es el contexto nuevo que no conversa con el resto: nombra herramientas descartadas (difusion latente, ControlNet) y repite cifras y salvedades que la justificacion y el alcance ya dan.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Parrafo de contexto escrito fuera del ciclo que no usa los terminos fijos del documento | E-T1, E-R5 | "la escasez de fotones", "bandas oscuras", "artefactos inducidos por metal" | PAT-14 |
| El contexto presenta como herramienta del trabajo un metodo que la propuesta descarto, sin decirlo | E-M4 | "ControlNet permite incorporar condiciones espaciales" (y despues "sin espacio latente") | nuevo |
| Cierre de parrafo que afirma un efecto sobre modelos de segmentacion que la tesis declara no medir | E-R2, E-P3 | "limita el desarrollo de modelos robustos ante este tipo de alteracion" | nuevo |
| Conector de transicion que apunta a una "necesidad" o un "contexto" no nombrados | E-O3, E-M4 | "A partir de esta necesidad, la presente investigacion propone" | PAT-34 |
| Cifras de una fuente repetidas en contexto y justificacion | E-R4 | "14 de los 75 volumenes" en l.7 y l.52 | PAT-102 |
| Aperturas de parrafo por recuento en serie | E-R1 | "tiene dos partes:" / "cuatro puntos:" / "cuatro tareas" | PAT-114 |
| La salvedad de no medir la segmentacion repetida en cada subseccion | E-R4 | "y este trabajo examina esa plausibilidad antes que la utilidad" | PAT-46 |
| Parrafo de limitaciones que agrega controles sin oracion tematica comun | E-M1 | variante + S1 + discordancia + envolvente en l.86 | PAT-33 |
