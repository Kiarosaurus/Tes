# introduccion — r00 (redaccion inicial, alcance acotado) — respuesta del redactor

Modo: redactar. Archivo: `overleaf/secciones/introduccion.tex`. Por pedido de la autora, solo se
reescribieron `\introsection{Objetivos de investigación}`, `\introsection{Justificación}` e
`\introsection{Alcance y limitaciones / restricciones}` (antes l. 23-49). No se tocaron el encabezado
del capitulo (l. 1-17) ni `\introsection{Formulación del problema}` (l. 19-21). No se cambiaron titulos.
El texto anterior (DESFASADO, #126) no se uso como fuente. No hay reportes de revision en esta etapa.

## 1. Lo redactado

| Subseccion | Criterios de rubrica | Contenido |
|---|---|---|
| Objetivos: parrafo de apertura | G-A6, G-T5 | Los objetivos son los cuatro del cap. 3; se evalua coherencia fisica y quirurgica, no segmentacion. `\GAPDEC` sobre la pregunta |
| Objetivo general | G-A6, G-A10 | Cadena de sintesis por difusion en dominio de imagen; colocacion restringida por criterios quirurgicos; codificacion multiventana; utilidad para segmentacion = trabajo futuro |
| Objetivos especificos (lista, titulo en negrita) | G-A6, G-A7 | 1 compuerta Go/No-Go (ida y vuelta, 25 HU, 34 pacientes, regla fijada antes de la prueba que decide); 2 muestreador (Kaiser, McLaren, grado de brecha cortical, referencia clinica en S1, sin ajuste); 3 sintetizador (inpainting 2.5D en dominio de imagen, `G`, `M`, `B_delta` ~12 mm, comparacion con copia y pegado y protocolo fisico); 4 SAP + metricas de Peters con nombres publicados |
| Objetivos: parrafo de falsabilidad | G-A7, G-A8 | Que objetivo fija de antemano su fallo (solo el 1) y cuales no (2, 3, 4), cada uno con su `\GAPDEC` |
| Objetivos: parrafo de orden | G-A10 | La compuerta se formulo para difusion latente con ControlNet; veredicto negativo; Obj 3 reformulado despues; regla no modificada |
| Justificacion (5 parrafos) | G-A9, G-A3, G-A10 | (1) necesidad: datos anotados escasos con metal (14/75/61), motivacion de fondo y por que no se mide; (2) colocacion: Peters (colocacion aleatoria en entrenamiento, experta en evaluacion), Liu et al. (trayectoria unica), Zwingmann (distribuciones por tecnica); (3) apariencia: De Man (origen de las rayas), modelos de difusion de lesiones sin mecanismo fuera de la mascara; (4) contribucion C1-C3, multiventana no reclamada como propia, `B_delta` sin precedente; (5) justificacion metodologica: preinscripcion del muestreador y hallazgo del No-Go |
| Alcance (4 parrafos + lista) | G-A10 | Que entra (cohorte local, tornillo iliosacro parametrico, S1 y segundo corredor descriptivo, parches en dominio de imagen); cuatro exclusiones con su razon; cuatro supuestos; limitaciones con sus GAP |

## 2. Fuente de cada cifra

TM = `tesis/main.tex`; C3 = `overleaf/secciones/capitulo3.tex` (ya auditado en r00-r05); DEC = `docs/01-decisiones.md`.

| Cifra | Donde | Fuente |
|---|---|---|
| 25 HU (criterio de la compuerta) | Obj. 1; parrafo de falsabilidad | TM Objectives, item 1 ("below a 25~HU threshold") |
| 34 pacientes de prueba | Obj. 1 | TM Objectives, item 1 ("evaluated on 34 held-out patients") |
| cuatro niveles del grado de brecha | Obj. 2 | TM Problem Statement ("four-level cortical-breach scale") |
| ~12 mm de `B_delta` | Obj. 3; supuestos | TM Objectives, item 3 ("$B_{\delta}$ ($\sim$12mm)") |
| 14 de 75 anotados, 61 sin anotar | Justificacion; Alcance | `\cite{liu2021ctpelvic1k}`; ficha: "and 14 metal-affected CTs", "The remaining 61 metal-affected CTs are left unannotated", "including 75 CTs with metal artifacts" |
| 1 184 volumenes | Alcance | `\cite{liu2021ctpelvic1k}`; ficha: "including 1, 184 CT volumes" |
| 178 volumenes locales | Alcance | C3 §Datos (desde `docs/02-datos.md`) |
| cortes de 2 mm de la escala | Supuestos | TM Problem Statement ("The 2~mm bin width is therefore adopted here as a geometric convention") |
| 30 casos del cribado de fractura | GAPDATO | C3 §Datos; #125 |
| 16 casos de la revision | GAPDATO | #123; MAPA |
| al menos un paciente con fractura confirmada | Limitaciones | C3 §Amenazas; #125 (`CLINIC_0060`) |

Afirmaciones con cita, contrastadas con su ficha: Peters et al. colocacion aleatoria e impracticable
la manual ("manual metal placement was impractical", Discussion p. 9) y colocacion experta en el
benchmark de scoring; Liu et al. (`liu2025pipeline`) plan optimo unico; De Man et al. cuatro causas de
las rayas (TM Problem Statement); `ramzan2026claim`, `chen2024tumorsynthesis`, `jacob2026lgesynthnet`
como inpainting, `zhang2025diffboost` como generacion del corte entero desde ruido (ficha: "Genera la
imagen entera desde ruido"); `gardner2010safezones` contrasta con un estudio previo sin diferencia
(ficha: "that study found no difference in the safe zone size"); multiventana en MAR
(`wang2025adaptiveweighting`, `li2024`), TM Recognized Gap.

## 3. GAP abiertos en esta seccion

Ninguno es nuevo en el fondo, salvo el primero: todos repiten, en la introduccion, GAP ya
registrados en `redaccion/MAPA.md` (se anoto la nueva ubicacion en cada fila).

`\GAPDEC` (5):
1. "reformular la pregunta de la formulación del problema, que todavía promete síntesis 2D, Dice, HD95 y comparación con aumento de datos convencional, para que coincida con estos objetivos" — **nuevo** (#126).
2. "qué distancia de Wasserstein-1 contaría como fallo del muestreador" — #127.6; C3 §SAP.
3. "qué resultado haría fallar el Objetivo~3, o si su prueba decisiva es la de equivalencia frente al protocolo físico" — #127.3; C3 §Apariencia.
4. "qué evidencia verifica el Objetivo~4 más allá de esos controles, o si se declara que no se evalúa experimentalmente" — #127.6; C3 §Protocolo.
5. "si la comparación de equivalencia frente al protocolo físico se mantiene o pasa a trabajo futuro, contingencia de plazo registrada por la autora" — #90.

`\GAPDATO` (3):
1. "cribado ciego de fractura en 30 casos de la cohorte del Objetivo~2, preparado y no realizado" — #125.
2. "revisión de la autora de los 16 casos marcados por diferencia de diámetro entre variantes de segmentación o por desplazamiento de la caja de una estructura" — #123.
3. "el sintetizador no ha generado ninguna muestra sintética, así que no existe resultado del Objetivo~3" — #116.

`\GAPLIT`: ninguno. Sin candidatos nuevos para `docs/literatura/_candidatos.md`.

**GAP de alineacion en `capitulo3` §Vision general: NO se cierra.** Los cuatro objetivos de la
introduccion ya coinciden con los del cap. 3, pero ese GAP tambien pide alinear la pregunta de
investigacion, y la pregunta (Formulacion del problema, fuera del encargo) sigue prometiendo 2D,
Dice/HD95 y aumento de datos. Se puede cerrar cuando se reescriba la Formulacion. Queda anotado en MAPA.

## 4. Discrepancias entre fuentes

1. **Densidad osea en el Obj. 2.** TM Objectives item 2 dice "constrained by bone density"; D-O2.6
   (DEC 2026-09-22) la hace componente reportado de SAP y no condicionante (tambien C3 l. 166). Manda
   DEC: el objetivo no dice que la densidad restrinja las poses. (Ya en #127.5.)
2. **Consecuencia del No-Go.** TM item 1 dice "the latent route is abandoned"; C3 dice que la regla
   registrada establece que el Obj. 3 no se ejecuta. El Obj. 1 se redacto neutro ("su veredicto se
   reporta como resultado, sea positivo o negativo"). (Ya en #127.5.)
3. **Insumo de implantes.** El `CLAUDE.md` raiz dice "PENDIENTE DE DEFINIR"; TM Implant geometry
   source y C3 usan tornillo parametrico. Manda TM; se redacto "tornillo iliosacro parametrico y rigido".
   El `CLAUDE.md` raiz parece desfasado en ese punto.
4. **Titulo del Obj. 3.** TM lo llama "Design of a conditioned synthesizer" sin evaluacion; la Tabla
   `tab:diseno` de C3 pone la evaluacion de apariencia en la fila del Obj. 3. Se siguio C3 (el objetivo
   incluye la comparacion con copia y pegado y con el protocolo fisico).
5. **Obj. 1 como "Ensure".** TM formula el Obj. 1 como asegurar un error bajo 25 HU; se redacto como
   "Determinar si", porque un objetivo que promete aprobar no es falsable (G-A8) y el resultado fue No-Go.

## 5. Fuera del encargo, para la autora y el orquestador

- El encabezado del capitulo (l. 3-17) sigue DESFASADO: promete DSC/HD95, 2D, difusion latente y
  ControlNet, y el lint marca oraciones largas en l. 7 y 13 (media, E-O1). La Formulacion (l. 21) tiene
  una oracion de 91 palabras (media, E-O1). No se tocaron por el alcance del encargo.
- **La hipotesis no aparece en la introduccion** (G-A1 pide preguntas o hipotesis). TM la tiene en
  *Hypothesis*; su lugar natural es la Formulacion del problema, cuando se reescriba.
- El encabezado define hoy TC, HU, SSIM, MAE, DSC y HD95. Las tres subsecciones nuevas usan TC y HU
  sin redefinirlas; si el encabezado se reescribe, debe seguir definiendolas antes de l. 23.
- SAP y MAR se definen ahora por primera vez en la introduccion; `capitulo3` los vuelve a definir
  (l. 13 y 44). No es error del lint; la autora decide si el cap. 3 conserva la definicion completa.

Implicancias: sin implicancias nuevas sobre la tesis; lo encontrado ya esta en #126 y #127.

## Decisiones de redaccion

- Objetivo especifico = titulo en negrita con verbo en infinitivo, seguido de 2-3 oraciones (no una
  sola oracion larga), para cumplir E-O1 y G-A6.
- Los objetivos de la introduccion llevan un parrafo de falsabilidad que dice, objetivo por objetivo,
  si su fallo esta fijado de antemano; los que no, con su `\GAPDEC`. Evita PAT-1 y PAT-15.
- "HU" es masculino en todo el documento ("los HU"), como en el cap. 3.
- En la introduccion, la TOST se nombra "comparacion de equivalencia frente al protocolo fisico"; la
  sigla TOST se define recien en el cap. 3.
- En la introduccion, el recorte de TotalSegmentator se describe como "variante de la segmentacion
  anatomica" para no adelantar la herramienta; en el cap. 3 se mantiene "recorte por defecto /
  alternativo". Pendiente de visto bueno de la autora (riesgo E-R5).
- "Grado de brecha cortical", "referencia clinica", "region de generacion", "mascara del implante",
  "banda de generacion extendida" e "insercion por copia y pegado" quedan definidos por primera vez en
  la introduccion (Obj. especificos), en negrita; "ida y vuelta (HU -> representacion -> HU)" tambien,
  sin negrita.
