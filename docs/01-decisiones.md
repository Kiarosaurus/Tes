# 01 — Log de decisiones

> Solo lo escribe la autora. Formato: una entrada por decision, con fecha.
> Tres lineas bastan. Este archivo es la evidencia de que el trabajo avanzo.

## 2026-09-07 — Reglas de lectura de la revisión 3D de los 178 volúmenes

**Decisión:** la clasificación de material de los 178 CT locales se lee así. En `dataset6`,
columna vacía o `nada` significa que no se encontró implante ni material metálico; con
texto, ese texto es el objeto metálico. En `dataset7`, columna vacía significa que **sí**
hay material ortopédico; con texto, hay material ortopédico **y además** lo anotado.
Dictada por la autora tras revisar en 3D los 178 volúmenes y registrada por el asistente
con instrucción explícita el 2026-09-07.

**Alternativas descartadas:** anotar cada fila de `dataset7` repitiendo «material
ortopédico»; y tratar la columna vacía como «sin revisar», que era la lectura del
inventario automático.

**Por qué:** la revisión es exhaustiva y el material ortopédico es la condición por
defecto de CLINIC-metal, así que anotar solo las excepciones es más rápido y menos
propenso a error que repetir lo constante. Aplicada, da 72 de 75 volúmenes de `dataset7`
con material ortopédico y 70 de `dataset6` sin objeto.

---

## 2026-09-07 — Duplicados: prevalece dataset7 y no tiene material ortopédico

**Decisión:** cuando un grupo de duplicados exactos tiene un volumen en `dataset7` y otro
en `dataset6`, prevalece siempre el de `dataset7` como representante, y ese volumen queda
marcado **sin** material ortopédico, porque ningún volumen de `dataset6` lo tiene. Afecta
a tres grupos: `metal_0061` = `CLINIC_0037`, `metal_0036` = `CLINIC_0048`,
`metal_0064` = `CLINIC_0070`.

**Alternativas descartadas:** conservar el volumen de `dataset6`; conservar los dos y
repartirlos entre entrenamiento y prueba, que es fuga directa.

**Por qué:** son el mismo contenido de vóxeles, así que mantener ambos lados pondría el
mismo volumen en entrenamiento y en prueba. Consecuencia: el conjunto de prueba con metal
no son 75 volúmenes sino 72, y 69 de contenido único. **Queda pendiente** elegir
representante en los tres grupos duplicados internos de `dataset7`
(`0012`/`0021`, `0013`/`0043`, `0046`/`0074`), que esta decisión no cubre.

---

## 2026-09-07 — Prioridad de la revisión 3D sobre la propuesta del agente

**Decisión:** si la autora anotó «sin objeto» y el agente `clasificador-metal` quedó en
`incierto`, manda «sin objeto». Caso resuelto por esta regla: `dataset6_CLINIC_0074_data`,
donde hay una estructura en lazo evidente que **no es metal ni material ortopédico** y por
eso no se anota como objeto. Los desacuerdos por borde del campo de visión
(`CLINIC_0039`, `0058`, `0066`, `0077`) se cierran igual. Confirmado también que
`metal_0059` y `metal_0071` **no son el mismo paciente**, pese a compartir spacing y
HU mínimo.

**Alternativas descartadas:** escalar cada `incierto` del agente a una segunda revisión;
dejar esas filas bloqueadas fuera de toda cohorte.

**Por qué:** el agente no certifica, propone; su `incierto` es ausencia de evidencia en
16 cortes, no evidencia de presencia. La revisión 3D de la autora es la fuente válida.
Los textos preliminares del asistente anterior en `metal_0002` y `metal_0003` se borraron
por la misma razón.

---

## 2026-09-07 — Adopción del protocolo híbrido de Peters

**Decisión:** adoptar `peters2025hybrid` como protocolo del brazo físico de comparación. Decisión comunicada el 2026-09-06 y registrada por el asistente con autorización explícita de la autora el 2026-09-07.

**Alternativa descartada:** una reimplementación independiente de XCIST cuya validación de artefactos metálicos se atribuya a `wu2022xcist`.

**Por qué:** Peters aporta el protocolo específico de simulación y evaluación de artefactos; Wu describe el toolkit y sus limitaciones. La adopción no valida automáticamente la adaptación de MAR 2D a síntesis pélvica 3D: siguen pendientes configuración, controles y métricas (#16–17).

## 2026-09-07 — Prioridad bibliográfica tras adoptar Peters

**Decisión:** `peters2025hybrid` permanece en N1 como protocolo adoptado; `wu2022xcist` pasa de N1 a N2 como fundamento técnico y fuente de limitaciones del simulador. Se incorpora N4 para descartes sin uso vigente, con motivo explícito.

**Alternativas descartadas:** bajar Peters por haber elegido su protocolo; descartar Wu por no validar metal; equiparar descarte de un rol con descarte de todo el paper.

**Por qué:** el nivel mide riesgo sobre el argumento y el benchmark. Peters concentra ahora esa dependencia. Wu todavía exige discusión metodológica, por lo que no es una cita de apoyo N3 ni un descarte N4. Esta recategorización responde al encargo de la autora en este turno.

---

## AAAA-MM-DD — Separacion en muestreador y renderizador

**Decision:** el pipeline se divide en dos componentes evaluados por separado.

**Alternativas descartadas:** un solo modelo end-to-end que coloque y renderice.

**Por que:** permite atribuir el error a geometria o a apariencia, y hace que el
muestreador sea defendible como contribucion independiente.

---

## 2026-09-07 — Precedencia de `refs/raw` y `refs.bib` como archivo generado

**Decisión:** ante cualquier discrepancia bibliográfica manda `refs/raw/`, el archivo tal
como lo entregó el editor; en su defecto, `refs/clean/`. Un campo que venía en la versión
anterior de `refs.bib` y que el raw no confirma no se conserva por costumbre: se marca
`% VERIFICAR` y se cierra bajando la fuente real. Si la fuente real tampoco lo trae, se
elimina. `refs.bib` pasa a ser un archivo **generado** por `scripts/build_refs.py`; las
correcciones se hacen en `refs/clean/`, nunca sobre `refs.bib`. Dictada por la autora y
registrada por el asistente con orden explícita el 2026-09-07.

**Alternativas descartadas:** mantener `refs.bib` como archivo de edición manual, que era
la regla 9 original de `CLAUDE.md`; y conservar los campos heredados sin respaldo por ser
plausibles.

**Por qué:** los 27 DOIs no tenían procedencia verificable. Con `refs/raw/` cada campo es
auditable contra el editor y ningún dato depende de memoria ni de conocimiento del
asistente. La regla ya se aplicó y tuvo dos consecuencias opuestas el mismo día: cerró
`wu2022xcist` (el .bib de IOP confirmó `pages = {194002}`, que el registro de PubMed no
traía) y obligó a **retirar** los tres volúmenes LNCS de `jacob2026lgesynthnet` (16459),
`ramzan2026claim` (16038) y `wang2019cochlear` (11769), porque el exportador BibTeX de
Springer omite serie y volumen en los capítulos de actas. Los valores retirados quedan
registrados en `refs/MAPEO.md` por si se recuperan de otra fuente.

**Nota sobre `CLAUDE.md`:** esta decisión modifica de hecho la regla 9 («refs.bib es
autoridad… la definió la autora a mano»). La regla de fondo se mantiene —nadie añade,
elimina ni corrige una entrada con conocimiento propio— pero el archivo donde se edita
pasa a ser `refs/clean/`. Actualizar el texto de `CLAUDE.md` queda pendiente de la autora.

---

## 2026-09-08 — Objetivo 5 fuera de alcance: sin evaluación downstream

**Decisión:** la evaluación downstream de segmentación (Dice, HD95) sale del alcance de
esta tesis y se declara trabajo futuro. Aplicada a `tesis/main.tex` (Research Question,
Hipótesis, Objetivo general, lista de objetivos y tabla de Expected Results) y a
`docs/00-tesis.md`.

**Alternativas descartadas:** mantenerla como alcance completo opcional, que era el
estado anterior; y recortar en su lugar el Objetivo 4, que ya era opcional y por tanto no
acortaba el camino crítico.

**Por qué:** no es falta de tiempo, son dos condiciones auditables. Solo una minoría de
los volúmenes con metal tiene anotación ósea verificada (implicancia #13) y solo una parte
de la colección publicada está en disco (implicancia #18). Un Dice o un HD95 se apoyaría
en una cohorte demasiado pequeña y parcialmente anotada para sostener una afirmación de
robustez. Declararlo con esas dos razones es más defendible que entregarlo débil. Degrada
#13 y #18 de bloqueo a limitación declarada.

---

## 2026-09-08 — Se retiran BFC e ISC; SAP queda como única métrica propia

**Decisión:** las métricas Boundary Feature Coherence (BFC) e Inter-slice Consistency
(ISC) se retiran como contribución. La apariencia se evalúa con las métricas del
protocolo adoptado bajo **sus nombres publicados**: bone integrity, metal integrity y
streak amplitude (`peters2025hybrid`). La escala 0–4 del benchmark no se traslada.
Surgical Admissibility of Placement (SAP) queda como la única métrica introducida por
esta tesis. Registrado también en `docs/03-glosario.md` con aviso de no reintroducirlas.

**Alternativas descartadas:** rellenar BFC e ISC con las medidas de Peters conservando
las siglas propias; y definir BFC e ISC de verdad, con estimadores propios en z y en la
interfaz cortical, que era más caro y no cabía en el tiempo restante.

**Por qué:** el Objetivo 4 decía «Formalization of physical-coherence metrics». Rellenar
siglas propias con medidas heredadas dejaba ese verbo sin contenido: la sigla se quedaba
y el significado se deslizaba. Es exactamente el conflicto de las implicancias #14 y #16,
que quedan **cerradas** con esta decisión. Heredar de un benchmark publicado es más sólido
que inventar, siempre que se llame por su nombre.

---

## 2026-09-08 — El rango único de malposición se sustituye por dos distribuciones ordinales

**Decisión:** desaparece de la tesis el rango 31–60%. SAP se compara contra las **dos
distribuciones completas de cuatro grados** de `zwingmann2009navigated` (navegado
69/15/8/8; convencional 40/37/11.5/11.5), condicionadas por técnica quirúrgica. Se añade
un segundo eje de condicionamiento por **nivel sacro** (S1 vs S2). El rango 2–15% tampoco
se usa.

**Alternativas descartadas:** mantener 31% y 60% como cotas escritas explícitamente como
cálculo propio; y buscar una fuente clínica con una tasa agregada real, que exigía PDFs
nuevos sin garantía de existir con esa granularidad.

**Por qué:** el 31–60% **no aparece** en `zwingmann2009navigated`: sale de 100−69 y 100−40
sobre dos poblaciones separadas por técnica, con diferencia significativa (p = 0.02), así
que colapsarlas en un rango borra la variable que las explica. Y el 2–15% resultó ser cita
de tercera mano: `hinsche2002fluoroscopy` no lo mide, lo cita de cuatro trabajos, y además
es banco sobre pelvis de plástico. Comparar contra las distribuciones ordinales es más
fuerte, no más débil, y usa la misma escala de grados que ya está en la tesis. El eje S1/S2
viene de que Hinsche localizó el 82% de los tornillos mal colocados en S2. Implicancia #12.

---

## 2026-09-08 — El umbral de 10 mm se usa como convención de holgura geométrica

**Decisión:** el criterio de corredor ≥10 mm se escribe como **convención de holgura
geométrica**, no como umbral de seguridad clínica validado, citando a
`kaiser2014dysmorphism` como quien lo adopta y su justificación dimensional: holgura de
1–2 mm alrededor de un tornillo de 6.3–8 mm.

**Alternativas descartadas:** presentarlo como umbral establecido, que es como lo cita
`mclaren2021corridor`; y detener el uso del criterio hasta tener la fuente primaria.

**Por qué:** la cadena tiene tres saltos. McLaren dice que lo toma de Kaiser; Kaiser dice
*«was chosen as a conservative size»* y *«has been previously established… by experienced
surgeons»*, citando a Moed 2006, Gardner 2010 y Ziran 2007. Pero Kaiser sí da su razón
interna, y es dimensional, no empírica. Eso basta para usarlo con honestidad sin depender
de la fuente primaria. Implicancias #7 y #25.

**Estado:** la autora subió Moed, Gardner y Ziran en una primera ronda para comprobar si
aportan algo más. Si no aportan, esta decisión queda firme tal como está.

---

## 2026-09-08 — Se adopta el marco de referencia de Kaiser para el muestreador

**Decisión:** el muestreador expresa sus restricciones en el marco de referencia de
`kaiser2014dysmorphism`: reformateo a lo largo del eje sacro, perpendicular al platillo
superior de S1; angulación coronal del corredor contra la línea que une las crestas
ilíacas; angulación axial contra la línea que une las espinas ilíacas posteriores; y regla
de longitud útil con al menos **5 mm** de holgura a la cortical a cada lado. Los fenotipos
de morfología sacra se usan como **estratificador descriptivo** de la variabilidad
anatómica (grupo dismórfico = 41% de su cohorte). La **distribución de poses** dentro de
ese marco sigue siendo construcción propia.

**Alternativas descartadas:** quedarse solo con `mclaren2021corridor`, que da el
procedimiento de corredor y las tolerancias angulares pero **no** coordenadas ni ángulos
de referencia; y construir un marco propio desde cero.

**Por qué:** es lo primero de toda la bibliografía leída que se puede implementar
directamente sobre un volumen: los tres landmarks (platillo superior de S1, crestas
ilíacas, espinas ilíacas posteriores) son óseos y segmentables. Cubre el hueco exacto que
dejaba abierta la implicancia #7, que baja de RIESGO a cubierta operacionalmente. El
`score > 70` se usa como **descriptivo**, nunca como corte validado: el propio paper lo
reporta como observación sobre 104 pelvis y declara que falta validación externa.

---

## 2026-09-08 — C3 se reescribe: la novedad no es el multi-ventana

**Decisión:** la contribución C3 deja de reclamar la codificación multi-ventana como
novedad. Se declara que el marco multi-ventana proviene de trabajo previo de MAR y que
`wang2025adaptiveweighting` lo atribuye a su vez a trabajo anterior. Lo que se reclama es
**su uso para síntesis**, junto con la banda extendida B_delta.

**Alternativas descartadas:** conseguir la fuente primaria del marco multi-ventana y
citarla, migrando el nivel 1 a ese trabajo; y mantener el reclamo tal como estaba.

**Por qué:** la lectura completa de `wang2025adaptiveweighting` mostró dos cosas. Que el
marco no es suyo (*«Motivated by the existing work [24], we construct the general
multiple-window MAR framework»*), y que además el mecanismo publicado es una **cascada**
de ventana ancha a estrecha con capa de transferencia, no la codificación multicanal de
entrada que plantea la tesis. Escribir «multi-ventana (Wang et al., 2025)» sin esa
salvedad atribuye un diseño que la fuente no tiene. En cambio B_delta **sí** queda sin
precedente: ninguna fuente leída define una banda peri-implante con valor numérico.
Implicancia #24.

---

## 2026-09-08 — Riesgo asumido: el marco de referencia se validó en pelvis sin implante

**Decisión:** se adopta el marco de referencia de Kaiser **asumiendo un riesgo declarado
y explícito**, escrito en `tesis/main.tex`. El riesgo se resuelve midiendo en la cohorte
local, no leyendo más.

**El riesgo:** `kaiser2014dysmorphism` caracterizó su marco sobre **pelvis no lesionadas**
y excluyó explícitamente los CT con *«implants obscuring the lumbosacral junction»*. Los
tres landmarks están en la unión lumbosacra, que es justo donde pega el streaking. No está
establecido por la fuente que sigan siendo localizables en volúmenes con metal, que es
donde la tesis los necesita.

**Cómo se cierra:** cuantificar sobre los volúmenes locales con metal en cuántos se pueden
ubicar los tres landmarks. Es un experimento sobre datos ya en disco, no una lectura, y da
una cifra propia y citable. **Plan de contingencia ya escrito en la tesis:** si no
sobreviven, el marco se calcula solo sobre anatomía sin metal y se declara la limitación
para el conjunto de evaluación. Implicancia #26.

---

## 2026-09-08 — Riesgo PENDIENTE: hasta dónde comprometerse con lo que Kaiser declara

**Decisión:** se adopta lo que Kaiser aporta **operacionalmente** (marco de referencia,
definiciones angulares, margen de 5 mm, fenotipos como estratificador descriptivo), y
queda **PENDIENTE en estado de RIESGO** decidir si se continúa por esa línea hacia usos
más comprometidos: el score de dismorfismo como predictor, el corte `>70`, o los cortes de
longitud de los tres fenotipos como reglas duras del muestreador.

**Por qué se deja pendiente y no se cierra:** tres razones verificadas en el PDF. El `>70`
es **descriptivo**, no un umbral propuesto ni validado. Los propios autores escriben que
falta validación externa: *«Future clinical research is recommended to validate and test
the ability to use reformatted CT»*. Y el Appendix, que contiene la tabla de scores por
quintil y la figura de los clusters, **está fuera del PDF disponible**. A eso se suman
cuatro discrepancias internas documentadas en la ficha.

**Qué decide la continuación:** el resultado del riesgo anterior (visibilidad de landmarks
bajo artefacto) y lo que aporten Moed 2006, Gardner 2010 y Ziran 2007, en lectura. Si el
marco no sobrevive al metal, comprometerse más con Kaiser no tiene sentido.

---

## 2026-09-08 (2) — La cadena del 10 mm se declara agotada: es una convención, no una medición

**Decisión:** se deja de subir por la cadena de citas del umbral de 10 mm. Se usa como
convención de holgura geométrica derivada del calibre del tornillo, y la tesis lo afirma
con las frases de las fuentes auditadas.

**Alternativas descartadas:** conseguir Ziran 2003, el único eslabón que queda sin auditar,
para cerrar el rastreo del umbral.

**Por qué:** cuatro eslabones auditados y ninguno lo mide. `ziran2007fluoroscopic` no
contiene el umbral ni mide ninguna distancia. `moed2006s2screw` tiene un «1 cm» terminal
pero es separación interforaminal en cortes axiales, otra magnitud. `kaiser2014dysmorphism`
lo elige (*«was chosen as a conservative size»*) y lo justifica como holgura de 1–2 mm sobre
un tornillo de 6.3–8 mm. `gardner2010safezones` lo declara como el punto *«below which
placement of a large (6.5-mm to 8.0-mm) cannulated iliosacral screw would be considered
difficult by most orthopaedic surgeons»*. Que no haya origen empírico **no es un fallo de la
búsqueda: es el hallazgo**. No hay origen porque nunca fue una medición.

**Aviso de desambiguación registrado:** el Ziran del umbral es el de **2003, JBJS Br
85:411-418**, no `ziran2007fluoroscopic`, ya leído. Hay discrepancia de año sin resolver
entre las dos fuentes que lo citan (Moed imprime 2002, Gardner 2003, mismo volumen y
páginas).

---

## 2026-09-08 (2) — No se estratifica por fenotipo sacro

**Decisión:** los fenotipos de morfología sacra **no** se usan como variable estratificadora
del muestreador. El muestreador mide la geometría del corredor directamente sobre cada
volumen. El score de dismorfismo y el corte `>70` tampoco se usan.

**Alternativas descartadas:** adoptar los tres fenotipos de `kaiser2014dysmorphism` como
estratificador descriptivo, que era la redacción escrita horas antes; y condicionar por
`nivel × fenotipo` tras ver la inversión S1/S2 de `gardner2010safezones`.

**Por qué:** el efecto del fenotipo sobre el tamaño de la zona segura **no es consistente
entre estudios**. Gardner recoge que Carlson 2000 *«found no difference in the safe zone
size between normal and dysmorphic sacra»*. A eso se suma que Kaiser clasifica dismorfismo
por score y Gardner por radiografía simple: dos criterios que habría que conciliar. Medir
sobre cada volumen evita las tres cosas. **Efecto colateral:** la objeción de Carlson deja
de aplicar a esta tesis, y la inconsistencia entre estudios pasa a ser el argumento de la
decisión en vez de una amenaza. Cierra la implicancia #27.

---

## 2026-09-08 (2) — La geometría medida solo en pelvis intactas se declara limitación del campo

**Decisión:** el párrafo de `tesis/main.tex` sobre la visibilidad de los landmarks deja de
redactarse como riesgo asumido por la tesis y pasa a **limitación del campo**, nombrando las
tres fuentes y su exclusión respectiva.

**Alternativas descartadas:** mantenerlo como riesgo declarado propio, que era la redacción
anterior.

**Por qué:** no es una debilidad de esta cohorte, es el estado de la literatura.
`kaiser2014dysmorphism` excluye los CT con implantes en la unión lumbosacra;
`mclaren2021corridor` usa CTs no lesionados; `ziran2007fluoroscopic` es cadavérico y avisa
que fractura, desplazamiento y lesión de partes blandas alterarían lo visible. **Ninguna
fuente ha caracterizado el corredor en la población de interés.** Medirlo en la cohorte
local pasa de remiendo a aportación. La implicancia #26 sigue abierta hasta que exista esa
cifra.

---

## 2026-09-08 (2) — La premisa del muestreador se respalda también por vía anatómica

**Decisión:** el Problem Statement incorpora los coeficientes de variación de
`ziran2007fluoroscopic` como respaldo anatómico de que no existe una pose canónica: 7–25%
en la mayoría de superficies, 43%, 47–52%, y 97–140% para la orientación del ala superior
de S1 en el plano frontal sacro, sobre 17 pelvis cadavéricas.

**Alternativas descartadas:** dejar el argumento apoyado únicamente en las tasas de
malposición quirúrgica.

**Por qué:** hasta ahora la premisa de C2 se sostenía solo en que los cirujanos fallan. Con
Ziran se sostiene además en que **la anatomía varía tanto que una trayectoria fija no puede
servir a todos**. Es un argumento independiente del error humano, y más difícil de discutir
en una sustentación. Salió de una lectura que se hizo por otro motivo (auditar la cadena
del umbral).

---

## 2026-09-08 (2) — Cribado por umbrales múltiples: se adopta la tabla de sensibilidad

**Decisión:** el cribado de cohorte no se compromete con un único umbral. Se recuenta a
**1500, 2500 y 3500 HU** y se reporta cuántos volúmenes cambian de clase.

**Alternativas descartadas:** fijar solo 2500 HU citando a `wang2025adaptiveweighting`; y
usar la regla adaptativa por ROI de `peters2025hybrid` para el cribado.

**Por qué:** el 2500 es arbitrario, y Peters no lo respalda: su umbral es **relativo al ROI**
y ese ROI se define alrededor del metal ground truth, así que para cribar habría que conocer
ya la respuesta. Reportar la sensibilidad convierte una elección arbitraria en una
caracterizada: si el recuento es estable entre 1500 y 3500 la arbitrariedad queda
neutralizada con una cifra propia; si es inestable, eso es un hallazgo y además señala qué
volúmenes necesitan revisión. Los tres valores ya existen como superficies en la exploración
local, así que no hay que recalcular nada. Implicancia #22.

**Pendiente:** correr el recuento, y decidir aparte si se adopta el reparto en dos reglas
(fijo para cribado, adaptativo por ROI para medir metal integrity sobre geometría CAD
propia).

---

## 2026-09-08 (2) — Niveles: Ziran 2007 en N2, Moed 2006 en N2 provisional

**Decisión:** `ziran2007fluoroscopic` queda en **N2**, definitivo. `moed2006s2screw` baja a
**N2 provisional**, con revisión pendiente.

**Alternativas descartadas:** N4 para Ziran, que el lector ya había descartado; y N1 para
Moed, que era el nivel propuesto por su lector.

**Por qué:** Ziran conserva dos roles vigentes —eslabón auditado de la cadena y evidencia de
variabilidad angular— pero no entra al muestreador como restricción ejecutable, porque no da
longitudes y trabaja en el marco del haz de fluoroscopia, que un CT no tiene. Moed entró
como candidato N1 por ser nodo terminal, pero su «1 cm» mide otra magnitud y no aporta prior
clínico: hoy no sostiene ninguna restricción. **Se revisa cuando se lea van den Bosch:** si
esa lectura confirma la comparativa S1 vs S2 que Moed cita de segunda mano, Moed puede
volver a N1 como vía de acceso a esa cifra.

---

## 2026-09-08 (2) — van den Bosch es la próxima lectura, y queda preparada sin ejecutar

**Decisión:** van den Bosch pasa a ser la fuente pendiente de máxima prioridad, por delante
de Ziran 2003 y de `templeman1996proximity`. **No se lanza la lectura todavía**: falta el
PDF. El encargo para el subagente queda redactado y listo en `docs/04-implicancias.md`,
entrada #28.

**Alternativas descartadas:** perseguir Ziran 2003 primero, que era el eslabón vivo de la
cadena del umbral; y seguir con Templeman, que era la prioridad anterior.

**Por qué:** decide dos cosas a la vez. Primero, el **eje S1/S2** del muestreador, que hoy
se justifica solo con `hinsche2002fluoroscopy`, banco sobre plástico; van den Bosch lo
pasaría a respaldo clínico. Segundo, la **implicancia #12**, que sigue sin ningún prior
clínico de malposición. `moed2006s2screw` lo cita con **6/31 frente a 1/49 por nivel**, la
única comparativa S1 vs S2 medida en pacientes vista en todo el proyecto, pero es cita de
segunda mano y por la regla 2 no puede usarse sin el original.

**Qué sería decepcionante, anotado por adelantado:** que la cifra sea un conteo sin
porcentaje ni criterio operacional; que use criterio binario en vez de la escala ordinal de
cuatro grados, en cuyo caso no se puede mezclar con el benchmark de SAP; o que la cohorte
esté auto-seleccionada por un criterio anatómico de inclusión. Los tres precedentes
aparecieron en esta misma ronda.

---

## 2026-09-08 (2) — Nota de proceso: máximo dos lectores en paralelo

**Decisión:** no se lanzan más de dos subagentes `lector-papers` a la vez mientras compartan
`docs/literatura/_index.md` y `_candidatos.md`.

**Por qué:** en la ronda de tres lecturas simultáneas, el agente de Gardner perdió cuatro
intentos de escritura por conflicto y el merge lo tuvo que hacer la sesión principal, que
además encontró una fila duplicada de Ziran 2003 creada por otro agente. `_candidatos.md`
ya supera el tamaño de una lectura, así que una reescritura completa desde un subagente ha
dejado de ser segura.

---
