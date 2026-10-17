# Respuesta del redactor — introduccion — r09

Encargo que manda: `redaccion/ENCARGO_2026-10-16.md` (DEC 2026-10-16, #193 opcion a). Reportes: lint, guia, estilo,
trazabilidad (anteriores a la DEC 2026-10-16) y asesor. Encabezado (l. 3-17) y Formulacion (l. 21) siguen bajo #126:
solo se les retiro la macro `\REVVISUAL`, sin cambiar el texto.

## Encargo y asesor

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| Retirar todo `\REVVISUAL` (l. 15, 21, 41, 54 x2, 88, 98, 100) | encargo | APLICADO | 0 macros en la seccion. l. 15, 21 y 88: macro retirada, texto igual (respaldado; l. 21 bajo #126). l. 41, 54, 98, 100: reescritos como limitacion, ver filas siguientes |
| GAP #1 (H5) y #2 (D3), l. 54 | asesor (D) | APLICADO | Sin marca. Obj 3 (l. 41): el contraste de realismo "quedo disenado y no se ejecuto". Parrafo del Obj 3: la comparacion a ciegas "no se hizo". §Alcance, parrafo nuevo de limitacion: razon (juicio visual de la autora, decision de no redisenar con su asesor) y trabajo futuro (DEC 2026-10-16 ptos 1-3) |
| l. 41, afirmacion "Se compara tambien con observaciones reales" | asesor / encargo | APLICADO | Texto del asesor, con remision a `sec:ap-realismo` y a las limitaciones |
| GAP #7 (estructura direccional), l. 100 | asesor (D) | APLICADO | "la estructura direccional del artefacto sintetico no se midio", seguida de la consecuencia de C3 :519 (una amplitud equivalente no probaria rayas). No se cita la inspeccion de #176 (ABIERTA). Sin "queda como limitacion" (PAT-5) |
| Limitacion de realismo del Obj 3 | encargo (pto 3) | APLICADO | Parrafo nuevo al abrir las limitaciones de apariencia: el reclamo se acota a la sintesis local en `G`, con la geometria y la pose del implante, frente al protocolo fisico y con el diseno congelado (DEC 2026-10-16 pto 1). Lo medido, sin cifras: atenuacion desde unos 4 mm en validacion (C3 :264, :270) y v2 tampoco alcanzo la equivalencia (#190). "Condicionada por la pose del muestreador" de la DEC se escribe "por la geometria y la pose del implante" porque la evaluacion usa el eje sin perturbar (PAT-175) |
| GAP #5 (sensibilidad del Obj 2), l. 94 | asesor (A) | APLICADO | Formula de C3 :115, con "posterior y descriptivo" (E15 :3) y 70 pacientes (E15 :8); sin cifras |
| GAP #3 (D9, l. 66), #4 (segundo corredor, l. 78), #6 (envolvente/canal, l. 96; #196 ABIERTA) | asesor (B) | ESCALADO | Decisiones B-1, B-2 y B-3 de la autora. Marcas sin cambio de sentido; l. 66 solo pierde "Por eso" (S16) |

## Guia

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Igual que GAP #5. Sin las cifras 0.203 / 0.237 que proponia: el encargo y el asesor mandan la formula de C3 :115, y T01 la da por valida (forma a). La trazabilidad manda sobre el estilo |
| guia-2 | guia | APLICADO | "en el conjunto de entrenamiento del modelo evaluado, los parches que solo contienen banda son menos frecuentes de lo que la geometria del corredor predice"; alineado con C3 :224 y :234; sin "antes de los ultimos retiros" |
| guia-3 | guia | APLICADO | l. 52: el margen es "una convencion de este trabajo" que mide la variabilidad propia de los metodos y "no una diferencia fijada como aceptable para algun uso" (#195 (a)); sin cita a Haber y Barnhart ni `max(s, r)`, que van en el cap. 3 |
| guia-4 (baja) | guia | no aplicado | El parrafo del Obj 2 crece y el intervalo por remuestreo se reporta en el cap. 3 y 4 (PAT-58) |

## Estilo

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| S01 | estilo | APLICADO | Sin cifras, con la condicion "posterior y descriptivo" (PAT-31); ver guia-1 |
| S02 | estilo | APLICADO | Salvedad temporal retirada de la primera oracion de l. 52; queda solo en el parrafo del resultado |
| S03 | estilo | APLICADO | Oracion tematica: "Ni el control de cordura ni la version 2 del sintetizador deciden el desenlace del Objetivo 3." |
| S04 | estilo | APLICADO | Parrafo de l. 72 suprimido: la independencia del muestreador va al segundo elemento de la contribucion; el hallazgo del Obj 1 va al parrafo de la compuerta, que se parte en dos (veredicto y hallazgo / codificacion sin autoencoder) |
| S05 | estilo | APLICADO | Cada desplazamiento se nombra y se mide junto; seis oraciones de cuerpo en lugar de ocho |
| S06 | estilo | APLICADO | "de saturacion en el suelo de $-1000$~HU de la representacion"; "piso de ruido" solo para el ruido |
| S07 | estilo | APLICADO | "el percentil~95 del perfil radial de HU del sintetizador" (C3 :252-254) |
| S08 | estilo | APLICADO | "sobre la TC reconstruida" |
| S09 | estilo | APLICADO | Texto propuesto |
| S10 | estilo | APLICADO | Texto propuesto |
| S11 | estilo | APLICADO | "La brecha que queda es la sintesis ..." sin "asi", formula del pto 9 literal. Queda al cierre del parrafo de la MAR no pareada porque una oracion sola no hace parrafo (E-O2) |
| S12-S21 (bajas) | estilo | APLICADO | S12, S13, S14, S15, S16, S17, S18, S19, S20, S21 con el texto propuesto o equivalente |

## Trazabilidad

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 | trazabilidad | APLICADO | Forma (a), con la formula de C3 :115 |
| T02 | trazabilidad | ESCALADO (sin marca) | El texto no usa las cifras de E15, asi que no hace falta marca. Al orquestador: E15 esta en `objetivo2/EXPERIMENTOS.md`:122 pero en §7 ("Superados y archivados"), no en §5; `00-tesis.md` no tiene 0.203 / 0.237 (lo dice el asesor) |
| T03 (baja) | trazabilidad | APLICADO | Junto con guia-3: la regla general y despues "en el modelo evaluado lo fija la variabilidad entre semillas del sintetizador" |

## Lint

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| E-O1, l. 7 (41 palabras) y "robustos" | lint | ESCALADO (se mantiene) | Encabezado bajo #126 (ENCARGO 2026-10-16 pto 1). Cuatro oraciones nuevas de mas de 40 palabras se partieron en esta ronda |

## Decisiones de redaccion

- Ensayo de realismo no ejecutado por la DEC 2026-10-16: en los objetivos, "quedo disenado y no se ejecuto"; en el resultado, "no se hizo"; la razon y "trabajo futuro" se dan **una sola vez**, en el parrafo de limitacion de apariencia. Nunca `\GAPDATO` ni "pendiente".
- La limitacion de realismo se escribe con el agente: "La autora juzgo insuficiente ese realismo al inspeccionar las salidas, y con su asesor decidio no redisenar ni reentrenar el sintetizador". Es un juicio y no una medicion, asi que se dice quien lo hizo (E-V2).
- Reclamo acotado del Obj 3: "la sintesis local del artefacto en la region $G$, condicionada por la geometria y la pose del implante y evaluada frente al protocolo fisico con el diseno congelado". No se escribe "pose del muestreador", porque la evaluacion usa el eje sin perturbar (PAT-175).
- Lo que no se midio y debilita el contraste se escribe como hecho ("no se midio") seguido de su consecuencia, no como "queda como limitacion" (PAT-5).
- El margen $\Delta$ fuera del cap. 3: "convencion de este trabajo que mide la variabilidad propia de los metodos ... y no una diferencia fijada como aceptable para algun uso", y despues la rama que gano en el modelo evaluado. Sin cita ni formula.
