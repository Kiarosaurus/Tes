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


## 2026-09-08 (3) ? Van den Bosch: nivel sacro clinicamente motivado, benchmark ordinal solo en S1

**Decision:** se conserva S1/S2 como variable geometrica del muestreador con respaldo
clinico asociativo de `vandenbosch2002`. El benchmark ordinal de SAP queda limitado a
S1, con las dos distribuciones por tecnica de `zwingmann2009navigated`. S2 se evalua
con geometria y grados descriptivos, sin afirmar calibracion clinica ordinal.
Resolucion registrada por el asistente en cumplimiento del encargo actual de la autora
de leer van den Bosch y resolver sus implicancias.

**Alternativas descartadas:** usar 6/31 y 1/49 como tasas de malposicion por tornillo;
convertir posicion binaria en cuatro grados; extrapolar a S2 las distribuciones de S1.

**Por que:** los pares son pacientes con quejas neurologicas por configuracion de
fijacion, con sesgo temporal y de aprendizaje declarado. El paper publica malposicion
binaria dependiente de modalidad, sin prior ordinal S2. #28 queda resuelta y #12 se
cierra por delimitar el benchmark, no por haber encontrado ese prior. Si se exige
calibracion clinica ordinal S2, #12 debe reabrirse. Moed queda N2 confirmado: la cita
primaria sustituye su papel de intermediario. Aplicado en `main.tex`, `00-tesis.md`,
`03-glosario.md` y los registros de literatura.


## 2026-09-08 (4) - Gardner como respaldo anatomico explicito del eje S1/S2

**Decision:** incorporar `gardner2010safezones` al alcance y a `main.tex`
(Problem Statement y Objetivo 2) como respaldo anatomico para evaluar S1 y S2
midiendo el corredor de cada nivel sobre cada volumen. Registrado y aplicado por
el asistente por encargo explicito de la autora en este turno.

**Por que:** las areas medias minimas S1/S2 son 346/109.3 mm2 en normales y
222/220.1 mm2 en dismorficos (Results, p. 624 y Tabla 1, p. 627). No sostienen una
jerarquia universal de amplitud. Gardner aporta geometria en el lado no lesionado
y trayectorias ideales; van den Bosch aporta una asociacion de sintomas clinicos
por configuracion. Son respaldos distintos para considerar el nivel sacro.

**Alternativas descartadas:** describir las areas dismorficas como inversion o igual
seguridad, importar medias como reglas universales, reintroducir fenotipos o score,
y usar geometria ideal como prior ordinal de malposicion. Se mantiene #27 cerrada y
el benchmark SAP de Zwingmann solo en S1 por tecnica; S2 conserva reporte descriptivo.

---

## 2026-09-10 — La unidad de independencia es el paciente; tratamiento de duplicados parciales

**Decisión:** mismo paciente = mismo `Grupo paciente` = mismo lado del split, y una sola
unidad en las estadísticas de cohorte. Por tipo de relación:

- **Subconjunto exacto:** se conserva el contenedor. Se retiran `metal_0034` (subconjunto
  de `metal_0011`) y `CLINIC_0038` (subconjunto de `CLINIC_0090`); los cortes de diferencia
  no aportan información significativa.
- **FOV solapados del mismo escaneo:** se unen sin interpolar en un volumen derivado.
  `metal_0071` (cortes 0-349) + `metal_0059` (cortes 216-287) =
  `data/derivados/dataset7_CLINIC_metal_0059u0071_union.nii.gz`, 422 cortes. `0059` aporta
  los cortes superiores y `0071` los inferiores; ambos muestran el implante.
- **Adquisiciones distintas del mismo paciente:** se conservan con el mismo
  `Grupo paciente`. Una es primaria por una regla fijada a priori (menor spacing en plano;
  empate, más cortes) y la otra es par de reproducibilidad, fuera de las cohortes.
  `metal_0065`/`metal_0066`: primario `metal_0066` (0.770 frente a 0.835 mm). La regla la
  propuso el asistente y se aplica por orden de la autora; **nunca se elige por cómo se ve
  el metal**.
- **`metal_0068` no tiene material ortopédico.** Excepción observada a la regla «fila vacía
  en dataset7 = material ortopédico»; su metal es una cremallera extracorpórea.
- **Ningún `.nii.gz` se borra ni se mueve.** Los volúmenes fuera de uso se declaran con
  motivo, evidencia y decisión en `experiments/exploration-3d/exclusiones.csv`, y las
  cohortes se construyen leyendo ese archivo.

**Corrige la entrada del 2026-09-07:** `metal_0059` y `metal_0071` **sí** son el mismo
paciente. La revisión de ese día los separó por aspecto; la medición muestra 216 cortes
idénticos bit a bit con desfase coherente con el affine.

**Alternativas descartadas:** criterio de duplicado solo por hash SHA256 del volumen (no
ve subconjuntos ni FOV solapados); conservar como independientes dos volúmenes del mismo
escaneo; fusionar por registro dos adquisiciones distintas (interpola y destruye la
diferencia que las hace útiles como control); borrar los archivos redundantes.

**Por qué:** el hash por corte (implicancia #45) mostró tres pares del mismo estudio que el
SHA256 no detectaba. Contar volúmenes en vez de pacientes mete fuga entre entrenamiento y
prueba y duplica vóxeles en las estadísticas. El par `0065`/`0066` muestra, con el mismo
implante, que la geometría sobre 2500 HU cambia con la adquisición (#46). Resultado: 178
volúmenes = 168 pacientes; dataset7 con material ortopédico 71 volúmenes = **65
pacientes**; dataset6 sin objeto 70 volúmenes = **69 pacientes**. Registrada por el
asistente con orden explícita de la autora el 2026-09-10.

**Queda pendiente:** el representante en las tres copias exactas internas de dataset7
(#20). Se usa el índice menor por regla determinista; como el contenido es idéntico, la
elección no cambia ningún vóxel. *(Resuelto en la entrada siguiente, 2026-09-10 (2).)*

---

## 2026-09-10 (2) — #20: copias exactas internas de dataset7, se conserva el índice menor

**Decisión:** en los tres pares de copias exactas internas de dataset7 se conservan
`metal_0012`, `metal_0013` y `metal_0046`; se retiran `metal_0021`, `metal_0043` y
`metal_0074` (declarados en `exclusiones.csv`, sin borrar archivos).

**Alternativas descartadas:** elegir el representante por inspección visual de cada par.

**Por qué:** el contenido es idéntico vóxel a vóxel, así que la elección no altera ninguna
cifra, y una regla determinista es reproducible. Cierra la implicancia #20. Registrada por
el asistente con orden explícita de la autora (2026-09-11).

---

## 2026-09-11 — #41: geometrías de implante paramétricas; extracción real solo como contingencia

**Decisión:** el insumo de geometrías de implante del muestreador y de ambos brazos de
síntesis es **paramétrico**: tornillos rígidos modelados con dimensiones que tengan evidencia
textual. El calibre se toma de los rangos ya citados en la tesis (6.5–8.0 mm,
`gardner2010safezones`; 6.3–8 mm, `kaiser2014dysmorphism`). La longitud no sale de un rango
publicado fijo: la acota en cada volumen el corredor medido, con la regla de longitud útil de
Kaiser (≥ 5 mm de holgura cortical). Los detalles finos sin fuente (rosca, canulación,
cabeza, arandela) se simplifican a un cilindro liso declarado. Los implantes reales de
CLINIC-metal **no forman el banco**: se usan como contraste descriptivo de poses, como
referencia de apariencia para el sintetizador y como control test-retest
(`metal_0065`/`metal_0066`). Aplicada a `tesis/main.tex` (Objetivo 2 y Datasets).

**Contingencia, abierta:** si a futuro faltara **por completo** bibliografía con calibres y
longitudes utilizables, se reconsidera extraer geometrías de los implantes de CLINIC-metal
(vía a). En ese caso la regla de aislamiento pasa a ser vinculante a nivel de paciente y hay
que declarar las limitaciones medidas en E8 (#46). La falta de detalles finos **no** dispara
la contingencia.

**Alternativas descartadas por ahora:** extraer geometrías por umbral de CLINIC-metal (E8:
fragmentación, fuste por debajo del calibre publicado y dependencia de la adquisición, #46);
CAD de fabricante o de repositorio público (existencia y licencia no verificadas).

**Por qué:** es ejecutable hoy, da dimensiones conocidas para SAP y para el ROI de metal
integrity, hace utilizable `Dmax >= d_implante + holgura` (#31), cumple la regla de
aislamiento por construcción y encaja con C1 tal como está escrita. La justificación de C1
cita a `xie2024implantsegmentation`, en lectura (#47); su redacción puede ajustarse al leerla.
Registrada por el asistente con orden explícita de la autora (2026-09-11).

---

## 2026-09-11 (2) — #31: viabilidad de corredor como calibre más holgura

**Decisión:** el muestreador acepta un corredor cuando `Dmax >= d_implante + 2c`.
`d_implante` es el calibre del tornillo paramétrico (6.5–8.0 mm, `gardner2010safezones`;
7.3 mm, `grass2016`). `c` es la **holgura de Kaiser**: 1 a 2 mm radiales por lado. Se
reportan ambos extremos. El escalar fijo de 10 mm deja de ser la restricción y queda como
convención heredada de comparación.

**Aviso de interpretación:** Kaiser escribe *"1 to 2 mm of circumference around a 6.3 to
8-mm-diameter screw"* y no publica la cuenta. Leerlo como holgura radial por lado es una
**operacionalización propia**, declarada, y no se cita como resultado de Kaiser. Es
coherente con su propio par (8 mm + 2 × 1 mm = 10 mm). Con los calibres usados, el umbral
va de 8.5 a 12 mm, dentro de los valores previos de 8 a 12 mm que recoge
`mclaren2021corridor`.

**Alternativas descartadas:** mantener el escalar de 10 mm (convención sin medición, #25);
usar como holgura los 5 mm de la regla de longitud útil de Kaiser (son el radio del propio
corredor de 10 mm, no una holgura añadida al tornillo).

**Por qué:** las siete fuentes auditadas derivan el umbral del calibre del implante (#31).
Con geometría paramétrica (#41) el calibre es un parámetro conocido, así que la
restricción deja de ser heredada y la sensibilidad a `c` se vuelve una ablación natural.
Registrada por el asistente con orden explícita de la autora (2026-09-11).

---

## 2026-09-11 (3) — #22: el umbral de 2500 HU queda solo para cribado

**Decisión:** 2500 HU se usa **únicamente** para cribar la cohorte (E1: cero falsos
negativos contra la revisión 3D). La **metal integrity** se mide con la regla adaptativa por
ROI de `peters2025hybrid` sobre la geometría paramétrica conocida. Ningún umbral fijo define
la forma de un implante.

**Propuesta abierta, no decidida:** para extraer la máscara de un implante **real** (usos
descriptivos y de apariencia, #41), usar un umbral de semimáximo local por objeto en lugar
de 2500 HU. Motivo, E8 (#46): a 2500 HU los tornillos salen fragmentados y más finos, y el
semimáximo local varía entre objetos (p10 1991, p90 6587 HU).

**Alternativas descartadas:** un único umbral fijo para cribado, medida y forma.

**Por qué:** cada uso necesita algo distinto. El cribado necesita sensibilidad y 2500 HU la
tiene. La medida necesita adaptarse al ROI, que es lo que hace Peters. La forma necesita
seguir a cada objeto. Registrada por el asistente con orden explícita de la autora
(2026-09-11).

---

## 2026-09-14 — #48, #49, #50: TotalSegmentator como máscara anatómica del Objetivo 2

**Decisión** (texto propuesto por el asistente el 2026-09-13 y adoptado sin cambios por la autora):

```
2026-09-13 — Segmentacion para el Objetivo 2 (#48, #49, #50)
- Se adopta TotalSegmentator 2.18.0, tarea `total`, como mascara anatomica (no referencia).
  QC por caso con exclusion: nivel TS/R1 discordante, S1 cortada por FOV o vacia.
- Recorte principal: default 6 mm; robust 3 mm como analisis de sensibilidad de Dmax.
- Limpieza: eliminar componentes menores que una fraccion (a fijar) del volumen de su estructura;
  no "componente mayor" (fracturas).
- total_v3 no se evalua: trabajo futuro. Repetibilidad: se declara la cota observada.
- E9b se retira como evidencia de densidad; la densidad se mide dentro de las mascaras en E9.
  No se afirma contraste con/sin metal.
- Pendiente: tratamiento de los voxeles de implante existentes al medir Dmax.
```

**Fundamento** (asesoría del asistente del 2026-09-13, copiada literal por orden de la autora; solo
cambia el nivel de los encabezados):

Principio que ordena todo: **el Objetivo 2 necesita un `Dmax` que se pueda defender, no una
segmentación perfecta.** Cada decisión se juzga por si lo protege frente a un tribunal y cabe en el
tiempo.

### #48 — Adoptar TS: **sí, con condiciones**

**Por qué:**
- Es la única vía con una máscara de hueso rellena que ya corrió sobre toda la cohorte.
- Las alternativas (segmentación cortical propia o semimanual) no caben en 12 semanas y serían otra tesis.
- La cohorte no mostró un fallo que lo descarte: el nivel coincide con el clínico en 56 de 57, el metal queda dentro de las máscaras y ningún corte del FOV lo trunca, fuera de los ya conocidos.

**Condiciones, que en la tesis se escriben como parte del método:**
1. **TS es herramienta, no referencia.** Nada de "ground truth"; decir: "anatomical masks from TotalSegmentator 2.18.0, quality-controlled per case".
2. **Control de calidad por caso con criterio de exclusión explícito.** Se excluye o se revisa:
   - el caso donde TS y R1 no coinciden en el nivel;
   - la S1 cortada por el FOV (`z+`);
   - la S1 vacía.
3. **El metal existente.** TS etiqueta el tornillo como hueso: en un volumen con tornillo, `Dmax` mediría a través del implante. Hay que decidir si el corredor se mide solo en pelvis sin osteosíntesis o si los vóxeles > 2500 HU cuentan como ocupados. **Es una decisión nueva, anótala.**

### #49 — Recorte, limpieza y versión

**Recorte: el de 6 mm como principal y el de 3 mm como análisis de sensibilidad.**
- El nivel no cambia en ningún caso, así que el recorte no afecta la selección de pacientes.
- En tornillos, 6 mm va algo mejor: mediana del eje fuera 5.2% frente a 5.7%, y en `metal_0008` 5.8% frente a 17.5%.
- El de 3 mm protege contra truncamientos que no aparecieron.
- 6 mm es lo que corre TS por defecto: lo que otro grupo reproduciría sin configurar nada.
- Las dos máscaras ya existen, así que medir `Dmax` con ambas cuesta cómputo, no trabajo. La diferencia se reporta como incertidumbre del método. Eso convierte un punto débil (#49) en rigor.

**Limpieza de fragmentos: quitar componentes pequeños, no quedarse solo con el más grande.**
- En CLINIC-metal hay fracturas pélvicas. Un sacro fracturado puede ser dos componentes grandes y legítimos, y "el más grande" borraría uno.
- Regla propuesta: por estructura, conectividad 26, eliminar componentes por debajo de una fracción del volumen de esa estructura. El umbral hay que fijarlo y declararlo; no tengo cifra con respaldo.
- Reportar cuántos vóxeles se quitaron y comprobar que desaparecen los 10 desplazamientos de caja.

**Versión: quedarse con `total`.**
- `total` ya está corrido (358 corridas), controlado y analizado.
- `total_v3` no está evaluado: ni siquiera se verificó si trae las cuatro clases. Cambiar ahora obliga a repetir cómputo, control y análisis sin ninguna evidencia de mejora.
- Se declara como trabajo futuro. Solo se reabre si `total` falla algo imprescindible.

**Repetibilidad: opción (a).** Declarar la cota observada (≤ 16 vóxeles por máscara en 2 casos) y no invertir más tiempo: es cuatro órdenes de magnitud menor que el efecto del recorte.

### #50 — La cifra de #48 y el brazo sin metal

**Cifra: opción (b).** Retirar E9b como evidencia de densidad y no citar ni 38/43% ni 8/15% en la tesis.
- El 38/43% ya está refutado por dos mecanismos: el error de nivel y la geometría de la sonda.
- El 8/15% sale de la misma sonda con un filtro que yo fijé mirando los datos, sobre muestras pequeñas: sería repetir el error con otro número.
- La medida correcta sale gratis del E9 rehecho: HU dentro de `sacrum` + `vertebrae_S1` a lo largo de las trayectorias candidatas. Es la región que importa para el corredor y para bone integrity.
- Mientras tanto, lo defendible es cualitativo, con dos apoyos:
  1. el tornillo real de `metal_0008` atraviesa ala a 0–100 HU;
  2. un umbral de 150 HU dejaría fuera una fracción grande de la máscara del sacro en los tres grupos.

**Brazo sin metal: no usarlo como contraste.**
- Servía para afirmar "es el hueso, no el artefacto". Para eso haría falta comparar grupos emparejados por edad y sexo, con nivel auditado, y no los tienes.
- La conclusión que el Objetivo 2 necesita ("hace falta segmentación rellena, no umbral") **no depende** de ese contraste. Retira la afirmación causal y quédate con la operativa.
- No hace falta auditar la calibración a mano: el control de nivel de TS ya excluye los 7 casos con error si alguna vez se usan.

**Consecuencia para bone integrity (Peters):** declarar que la regla de 150 HU no representa el esponjoso sacro hipodenso, o calcularla dentro de la máscara de TS. Decídelo al trasladar el protocolo (#17).

**Nota del 2026-09-14 (el asistente, al registrar):** el "56 de 57" del fundamento se calculó antes de
que la autora corrigiera la transcripción de `metal_0012` (`ok` -> `+1`), que era el caso discordante.
La cifra vigente está en `experiments/objetivo2/ts_analisis.md`. La decisión no depende de ella.

**Sigue abierto:** la fracción de la regla de limpieza (se mide con E10, `ts_componentes.py`) y el
tratamiento del implante existente al medir `Dmax` (#52). Registrada por el asistente con orden
explícita de la autora (2026-09-14).

---

## 2026-09-14 (2) — #52: corredor en pelvis sin osteosíntesis, con diferencia por implante; #35 cerrada

**Decisión:** (a) el corredor del Objetivo 2 se mide en pelvis sin osteosíntesis (grupos 2 y 3).
(c) En los volúmenes con implante se mide con el implante como hueso y como espacio ocupado, y se
reporta la diferencia. La ocupación se calcula con 2500 HU (cota superior del corredor ocupado) y con
semimáximo local por objeto (propuesta abierta de #22); cuál es la principal queda pendiente.
#35 se cierra: se adopta el reparto por objetivo de `grupos.csv` (Obj 1 = grupos 1-3; Obj 2 =
grupos 2 y 3; Obj 3 = grupo 3). No cierra la evidencia de artefacto de Obj 3 (#34) ni #43.

**Por qué:** el Objetivo 2 necesita geometría ósea intacta y corredor libre (#35); la literatura
mide en pelvis intactas, así que (a) hace comparables las cifras; (c) cuantifica cuánto cambia el
corredor medido cuando TS etiqueta el implante como hueso (`metal_0008`: 11.3 frente a 10.0 mm).

Registrada por el asistente con orden explícita de la autora (2026-09-14).

---

## 2026-09-14 (3) — Fracción de limpieza, política de ocupación principal y exclusión por nivel (#49, #52, #54)

**Decisión** (recomendación del asistente del 2026-09-14, aceptada por la autora):
- Limpieza de máscaras TS: F = 0.001 por estructura, conectividad 26. Elegida tras E10 y E9-TS; se
  declara como post hoc y se reporta que `D_TS` y la viabilidad son idénticas para F en
  {0, 0.001, 0.01, 0.05} en la cohorte del Objetivo 2.
- Implante existente como espacio ocupado: política principal `ocupado_semimax`; `ocupado_2500` se
  reporta como cota. Difieren en 6 de 118 filas y en ninguna cambia la viabilidad a 10 mm.
- QC de nivel (#54, opción a): se mantiene la exclusión (72 de 91) y se declara el embudo
  103 -> 91 -> 72: discordancia de nivel TS/R1 en 18 (grupo 2: 11 de 34; grupo 3: 7 de 57) y S1 en
  el borde del FOV en 1.

**Por qué:** F no cambia el resultado y 0.001 es la menor probada que quita las islas de los 10
desplazamientos de caja (inferido desde componentes; se verifica con el recálculo de cajas en Khipu);
semimáximo es coherente con #22 (2500 HU solo para cribado); recentrar con el nivel de TS exige cambiar
la entrada de S1 y queda como sensibilidad.

Registrada por el asistente con orden explícita de la autora (2026-09-14).

---

## 2026-09-14 (4) — #49: recorte principal de 6 mm; se retira la preferencia por 3 mm

**Decisión** (recomendación del asistente del 2026-09-14, aceptada por la autora):
- Se mantiene el recorte por defecto de TotalSegmentator (6 mm) como principal. Se fijó el 2026-09-14, antes
  de correr E9-TS y de ver `D_TS`. El recorte robusto (3 mm, `--robust_crop`) queda como análisis de
  sensibilidad.
- Se retira la preferencia por 3 mm, que se apoyaba solo en el README de TotalSegmentator (no citable).
- Se reabre solo si la revisión de láminas muestra un fallo del recorte de 6 mm.

**Por qué:** cambiar el principal después de ver las cifras sería una decisión post hoc, y los datos no lo
piden. En la cohorte del Objetivo 2 (72 pacientes), la mediana de `D(6) − D(3)` es 0.0 mm y los viables a
10 mm son 29 con 6 mm frente a 27 con 3 mm. E10b (job 51527) no muestra un fallo sistemático de ninguno de
los dos recortes. De las 11 estructuras con la caja desplazada más de 10 mm, 5 se deben a islas del recorte
de 3 mm, 4 a islas del de 6 mm y 2 a los dos.

Registrada por el asistente con orden explícita de la autora (2026-09-14).

---

## 2026-09-14 (5) — Corrección de la justificación de F (decisión 2026-09-14 (3))

**Decisión** (recomendación del asistente del 2026-09-14, opción (a) de #49, aceptada por la autora):
- Se mantiene F = 0.001.
- Queda refutada la frase de la decisión 2026-09-14 (3) "0.001 es la menor probada que quita las islas de los
  10 desplazamientos de caja". Lo mostró E10b (job 51527): con F = 0.001 quedan 4 estructuras con la caja
  desplazada más de 10 mm entre recortes, 1 original y 3 creadas por la limpieza, y ninguna F probada las
  elimina todas.
- Justificación vigente: la limpieza es higiene de máscara, y `D_TS` y la viabilidad son idénticas para F en
  {0, 0.001, 0.01, 0.05}. Los desplazamientos de caja entre recortes se declaran.

**Por qué:** pasar a F = 0.01, que deja 1 residual, sería la segunda elección post hoc del mismo parámetro y no
cambia ningún resultado del corredor. La frase de `main.tex` sobre la limpieza sigue siendo cierta.

Registrada por el asistente con orden explícita de la autora (2026-09-14).

---

## 2026-09-15 — #53: segundo juicio del nivel de S1 en ITK-SNAP

**Decisión** (de la autora, 2026-09-15):
- El revisor clínico revisa los **61 casos** con punto de S1, no solo los 15 dudosos, sobre el volumen completo
  en ITK-SNAP. Usa la planilla ciega `experiments/objetivo2/r1_revision_itksnap_revisor.csv` y sus instrucciones
  `r1_revision_itksnap_revisor.md`.
- Las categorías son las mismas del juicio sobre el mosaico (`ok`, `+1`, `otro`, `?`), más un campo de vértebra
  de transición lumbosacra.
- El juicio nuevo se guarda aparte y no sobrescribe `r1_auditoria_s1_clinico.csv`.

**Por qué:** el mosaico sagital de ±60 mm no permite contar niveles ni ver una vértebra de transición (#53,
Hallazgo 1). Revisar los 61 evita tener que mezclar controles para no revelarle al revisor cuáles son los dudosos.

Registrada por el asistente con orden explícita de la autora (2026-09-15).

---

## 2026-09-15 (2) — El umbral de 25 HU del Go/No-Go se ancla en la literatura y se declara su limitacion de metrica

**Decision** (de la autora, 2026-09-15):
- El umbral del Objetivo 1 **se mantiene en 25 HU**. No se baja ni se sube.
- Deja de presentarse como cifra propia sin respaldo. En `main.tex` se declara que **no existe un umbral
  publicado de pasa/no-pasa** en exactitud de numero CT, y se ancla el valor en el nivel de error que
  alcanzan hoy los metodos de artefacto metalico:
  - NMAR, el algoritmo con que se calibra la escala 0-4 del reto AAPM: **RMSE 20.2 HU**
    (`karageorgos2024ddpm`, Tabla I, p. 28);
  - difusion en imagen: **RMSE 12.3 HU** (misma tabla);
  - difusion latente (MLD-MAR): **RMSE 12.74 HU** (`yun2026simulationdriven`, Tabla 1, p. 10).
- El ROI de hueso se declara delimitado por el **mismo umbral de 150 HU** que usa el protocolo adoptado
  (`peters2025hybrid`, 2.5, p. 5; `haneda2025aapm`, Sec. 2.3, p. 7).
- **Se declara en el texto** que las cifras citadas son RMSE y el criterio de la tesis es MAE, y que RMSE
  nunca queda por debajo de MAE para los mismos residuos. La comparacion fija el **orden de magnitud**, no
  una equivalencia. Se declara, no se resuelve.

**Alternativas descartadas:**
- **Bajar el umbral** para que alguna configuracion de E6b pase. Descartada: seria mover el criterio despues
  de ver el resultado, que es el patron que este proyecto vigila (#25, #37, #45, #47, #50).
- **Dejar el 25 HU sin cita**, como estaba. Descartada: es una repregunta segura en la sustentacion y el
  respaldo existe.
- **Cambiar la metrica de MAE a RMSE** para igualarla a la literatura. No descartada, **aplazada**: exige
  rehacer la corrida de E6b (~8.7 h) porque el CSV solo guarda MAE. Queda como pendiente tecnico.
- **Usar el criterio relativo de Peters** (*"the mean CT number deviation ... was less than 2%"*, Abstract,
  p. 1) en vez de un umbral absoluto. Queda abierta como opcion de formulacion, no adoptada.

**Por que:** E6b midio que el VAE de SD 1.5 sin reentrenar falla el umbral en 178 de 178 volumenes con las
tres configuraciones, y tambien con el decodificador oraculo, que es cota inferior (#36/#39, ronda (7)).
Eso obligaba a responder si el umbral era el correcto antes de cambiar de VAE. La revision de las fichas ya
escritas mostro que **la familia de metrica si tiene precedente** y que **25 HU cae justo por encima de
donde aterriza NMAR**, el ancla del campo. El umbral no necesitaba bajarse: necesitaba citarse.

**Aplicado a `main.tex`** el 2026-09-15 (Objetivo 1 y la fila `Representation Viability` de la tabla de
metricas). Compila: 4 paginas, 42 referencias, 0 citas indefinidas. `refs.bib` sin cambios: las cuatro
claves ya estaban.

Registrada por el asistente con orden explicita de la autora (2026-09-15).

---

## 2026-09-15 (3) — `chen2026foundationvae` se cita como preprint de arXiv, con dos excepciones declaradas

**Decision** (de la autora, 2026-09-15):
- La entrada **cita el preprint de arXiv** (`arXiv:2605.30893`, 29 may 2026), que es la unica version que hay
  en `refs/raw/`. Es la primera entrada `@misc` del repositorio: las otras 42 son 35 `@article` y
  7 `@inproceedings`.
- **Excepcion 1, de normalizacion:** se conservan `eprint`, `archivePrefix` y `primaryClass`, que la regla 7
  de `refs/MAPEO.md` descarta. En las demas entradas sobraban porque habia DOI o revista; aqui son el unico
  localizador que trae el raw. Sin ellos la entrada no se puede encontrar.
- **Excepcion 2, de version:** el paper fue aceptado en **ICML 2026**, asi que se esta citando como preprint
  un trabajo revisado por pares. Se acepta **por ahora**, porque no hay raw de las actas.
- El campo `url` del raw venia roto (`httpsarxiv.orgabs2605.30893`). **No se corrigio ni se toco el raw**
  (regla 9): la regla 7 ya descartaba `url` para todas las entradas, asi que el defecto no llega a `refs.bib`.

**Alternativas descartadas o aplazadas:**
- **Conseguir el raw de PMLR y citar las actas.** No descartada, **aplazada**: es lo correcto y se hara si el
  paper llega a citarse en `main.tex` como apoyo de un argumento. Hoy no se cita.
- **Aplicar la regla 7 al pie de la letra** y quitar `eprint`. Descartada: dejaria una entrada sin ningun
  identificador.
- **Dejar el PDF fuera de la bibliografia** hasta tener las actas. Descartada: la autora quiere la fuente
  registrada ya, y `MAPEO.md` deja constancia de que es un preprint.

**Por que:** el paper es la lectura de prioridad 1 del Objetivo 1 (#36/#39, ronda (8)): hace la misma pregunta
que E6b y da la respuesta contraria. Tenerlo dado de alta permite trabajarlo sin bloquear nada, y la
diferencia entre preprint y actas no cambia su contenido tecnico.

**Lo que NO se escribe en ninguna parte:** el numero de volumen **`PMLR 306`**. Sale unicamente del pie de la
primera pagina del PDF y la pagina del editor no se encontro al buscar (2026-09-15). La aceptacion en ICML 2026
si tiene dos respaldos independientes; el volumen no. No se cita esa cifra hasta confirmarla.

**Condicion de reapertura:** si el paper pasa a citarse en `main.tex`, se consigue el raw de las actas antes de
escribir la frase que lo cite.

**Efecto colateral declarado:** `main.tex:139` tiene `
ocite{*}`, asi que la entrada **aparece en la
bibliografia del PDF aunque ningun texto la cite**. El documento paso de 42 a 43 referencias por esto.
`main.tex` **no se edito**: no hacia falta.

Registrada por el asistente con orden explicita de la autora (2026-09-15).

---

## 2026-09-16 — Se adoptan las recomendaciones de #64, #66, #67 y #68; #65 espera el raw de las actas

**Decision** (de la autora, 2026-09-16: *"Adopta tus recomendaciones, redacta main.tex y 01-decisiones.md"*):

1. **#64, opcion (a) — densidad osea del muestreador.** El Objetivo 2 deja de decir que el muestreador se restringe con
   *"bone density maps \citep{arand2019pelvicring}"*. Ahora la densidad se **lee del HU de cada volumen**, y
   `arand2019pelvicring` queda como motivacion: su modelo estadistico **medio poblacional** muestra heterogeneidad
   sistematica de masa osea (valores bajos en el ala sacra, el *"so-called alar void"*; la frase de `main.tex` es
   parafrasis, no cita). `main.tex:52` (*"pelvic density
   representations"*) no cambia.
2. **#66, opcion (a) — error del autoencoder dentro de `B_delta`.** En volumenes con metal, el error de ida y vuelta
   (HU -> multi-ventana -> VAE -> HU) se reporta **tambien dentro de la banda `B_delta` alrededor del metal**,
   **descriptivo y fuera del Go/No-Go**. El criterio de 25 HU en hueso no cambia. Escrito en el Objetivo 1 y en la
   fila `Representation Viability`.
3. **#67 — limitacion del benchmark por resolucion de referencia.** La re-verificacion de `zwingmann2009navigated`
   (2026-09-16) dio grosor de corte, intervalo, kernel y acuerdo interobservador **NO ENCONTRADO EN EL PDF**, y un solo
   radiologo evaluador. La opcion de re-muestrear a su grosor es **imposible**; se aplica la de declarar. `main.tex`
   dice ahora que el emparejamiento se lee como **acuerdo entre distribuciones de grados medidas a una resolucion de
   referencia desconocida**, no como equivalencia a nivel de voxel, citando la tendencia de `tejwani2014` con su
   *P* = .3.
4. **#68, opcion (a) + regla de borde — escala del benchmark.**
   - `main.tex:52`: *"four lettered grades"* -> *"four numbered grades"* (Zwingmann y Mirza numeran 0-3).
   - Frase nueva: la forma de cuatro grados (0, <2, 2-4, >4 mm) **aparece literal en `mirza2003`**, que declara los
     cortes tomados de estudios previos, mide en columna toracica cadaverica y advierte que esos umbrales *"do not apply
     to the thoracic spine"* y son *"likely different for different directions"*.
   - **Regla de borde de SAP, declarada como convencion:** grado 0 = sin perforacion; 1 = (0, 2) mm; 2 = [2, 4] mm;
     3 = (4, inf) mm. Zwingmann no define a que grado van 2.0 y 4.0 mm (NO ENCONTRADO EN EL PDF); la regla sigue la
     lectura literal de *"less than 2 mm"* y *"greater than 4 mm"* y cierra el grado 2 por ambos lados.
5. **#65 — NO se cita `chen2026foundationvae` todavia.** La decision 2026-09-15 (3) exige el raw de las **actas**
   (ICML 2026 / PMLR) antes de citarlo; el raw actual es el preprint de arXiv. La autora elige esperar. Frase preparada,
   **no insertada**, para el Objetivo 1 o Related Work:
   > *A concurrent study reports that frozen video autoencoders transfer to CT without medical fine-tuning
   > \citep{chen2026foundationvae}; it reports PSNR, SSIM and MSE without declared units and no HU error, evaluates no
   > bone or metal region, uses no pelvic or metal-bearing volumes, and declares intensity clipping to [-1000, 1000]~HU
   > for its generation experiments, so it does not address the dense-bone and metal range this criterion targets.*

**Alternativas descartadas:**
- #64 (b)/(c): mover Arand a la frase de *no canonical pose* o sustituirlo por Wagner 2014. Aplazadas: (a) basta para
  que la cita sea fiel.
- #66 (b): declarar la limitacion sin medir. Descartada: la medida es barata porque la mascara de metal ya se calcula.
- #68 (b): leer Vaccaro 1995 Part II antes de escribir. Aplazada: solo mejora la atribucion; la escala ya es convencion.
- #65 (b): anadir un VAE de video congelado a E6b. No adoptada en esta ronda.

**Por que:** las cuatro correcciones salen de lecturas del 2026-09-16 que mostraron citas mas fuertes que su fuente
(#64), un control que no puede ver la senal del Objetivo 3 (#66), un benchmark cuyo protocolo de medida no esta
publicado (#67) y un eslabon de la cadena de la escala que el texto omitia (#68).

**Pendiente de ejecucion (decidido, falta correrlo):** anadir el ROI `B_delta` a
`experiments/objetivo1/e6b_vae_sd15.py` sin romper el control de identidad, y correrlo en Khipu con el VAE que se elija
por #36/#39.

**Aplicado a `main.tex`** el 2026-09-16. Ver compilacion en `ESTADO.md`. `refs.bib` sin cambios: `arand2019pelvicring`,
`mirza2003` y `tejwani2014` ya estaban.

**Fuera de esta decision (registradas ABIERTAS, sin aplicar):** #69 (nivel S1 del brazo navegado y un tornillo por
paciente), #70 (validacion de Peters y proyeccion conjunta), #71 (Quad-Net y `main.tex:56`), #72 (frase de "dos
familias"), #73 (reconstruccion de CLINIC-metal), #74 (ControlNet y cambio de VAE), #75 (Rombach como cita de #66).

Registrada por el asistente con orden explicita de la autora (2026-09-16).

---

## 2026-09-17 — Decisiones delegadas al asistente en rol de asesor: se mantiene el renderizador, con compuerta dura y alcance recortado

**Delegacion** (de la autora, 2026-09-17): *"necesito que te pongas en la postura de un asesor de tesis profesional y
empieces a decidir, porque necesito sacar la tesis lo antes posible y solo tengo para hacer pruebas ya ... o acortar mi
alcance"*. El asistente propuso recortar al alcance minimo (Obj 1 + Obj 2, renderizador a trabajo futuro); **la autora lo
rechazo y eligio mantener el renderizador**. Todo lo que sigue se decide dentro de esa restriccion.

### A. Cita de Chen (reabre la decision 2026-09-15 (3))
- `chen2026foundationvae` **se cita como preprint de arXiv** en el Objetivo 1, porque aun no tiene version publicada con
  raw disponible. Se levanta la condicion de reapertura de 2026-09-15 (3). Frase: la preparada el 2026-09-16 (#65),
  presentada como *"A concurrent preprint"*.

### B. Alcance
1. **Ablaciones por restriccion: FUERA, a trabajo futuro.** Salen de la hipotesis y de la tabla de resultados.
2. **Brazo fisico de Peters: se conserva, sobre un subconjunto reducido de pacientes.** El ground truth sin metal que
   exigen sus metricas existe en sintesis (es el CT limpio de origen), asi que el brazo sigue siendo viable; lo caro es
   simular, y se acota el numero de casos.
3. **Renderizador condicionado a la compuerta del Objetivo 1 (regla escrita en `main.tex`).** La compuerta se evalua en
   pacientes separados para (i) el autoencoder preentrenado y (ii) una variante con **decodificador adaptado y encoder
   congelado**. **Si ninguna pasa, el Objetivo 3 no se ejecuta y el No-Go se reporta como resultado.** Esta regla se fija
   ANTES de correr la prueba.

### C. Implicancias decididas
| # | Decision | Aplicado |
|---|---|---|
| 36/39/74 | Via: **adaptar solo el decodificador** del VAE de SD 1.5 con el encoder congelado. Mantiene el espacio latente, asi que el U-Net preentrenado y ControlNet siguen siendo validos (resuelve #74). Es la prueba que decide el Objetivo 1 (ver D). Otro VAE (MAISI) queda como contingencia solo si el decodificador adaptado no pasa y queda tiempo | `main.tex` Obj 1 y Obj 3 |
| 66/75 | Se mantiene el ROI `B_delta` (descriptivo) y se cita `rombach2022latentdiffusion` como respaldo (*"removes high-frequency details"*) | `main.tex` Obj 1 |
| 69 | (a)+(c): S1 explicito solo en el brazo convencional; en el navegado **se declara supuesto**; grados por tornillo con pacientes con mas de uno | `main.tex:52` |
| 70 | (a)+(b): se acota lo que cubre la validacion de Peters y se compromete verificar en el codigo del simulador si paciente y metal se proyectan juntos antes de reproducir | `main.tex:50` |
| 71 | (a)+(c): `li2024` refuerza la penalizacion solo-imagen sin el sesgo de interpolacion; queda una sola salvedad (remocion vs sintesis). El multi-ventana previo se precisa como de reconstruccion por ventana o de perdida, no de codificacion de entrada. **Sin cifras de `li2024`** (tabla poco nitida) | `main.tex:54`, `:56` |
| 72 | (a): *"diffusion-based lesion synthesis models"* | `main.tex:48` |
| 57 | Se retira *"propagate globally far beyond"*; el caracter global se atribuye a `li2024`; `B_delta` se declara **parametro de diseno que trunca por diseno el streaking lejano** | `main.tex:48`, `:54`, Obj 3 |
| 73 | (b): reconstruccion de CLINIC-metal no reportada; los artefactos reales son referencia de apariencia de reconstruccion desconocida, no ground truth fisico. No se buscan metadatos (no hay DICOM) | `main.tex` Datasets |
| 62 | Sin cambio: `main.tex` ya dice *"by the same first author"* y *"enters that pool with zero events"*. **CERRADA** | — |
| 61/63 | Cerradas en redaccion por #71: generabilidad en imagen queda como supuesto evaluado | — |

### D. Pruebas que se corren ya (para fundamentar, en orden)
1. **P1 — Compuerta del Objetivo 1 con decodificador adaptado (bloqueante).** Afinar solo el decodificador del VAE de SD
   1.5 con cortes multi-ventana de pacientes de entrenamiento; evaluar con el pipeline de E6b (MAE y RMSE en hueso, metal y
   `B_delta`) en pacientes separados. Criterio: el ya escrito (MAE en hueso < 25 HU). Presupuesto: 1 semana. Resultado
   decide si hay Objetivo 3.
2. **P2 — Proyeccion conjunta en XCIST (#70).** Lectura del codigo o ejemplos del simulador; 1 dia. Si no es conjunta,
   se declara como limitacion del brazo fisico.
3. **P3 — Muestreador + SAP (Objetivo 2).** Implementar en `src/muestreador/` y comparar con Wasserstein-1 contra
   Zwingmann en S1 con la regla de borde de 2026-09-16. Corre en paralelo a P1 (CPU).

### E. Pendientes previos de `ESTADO.md`, decididos
- **#53 (segundo juicio en ITK-SNAP):** se mantiene con **plazo de 2 semanas**. Si el revisor no devuelve, se reporta la
  cifra vigente (48/29) con el acuerdo agente-clinico (kappa 0.81) y se declara el segundo juicio como no realizado.
- **Laminas de la autora (`e9ts_revision_laminas_autora.csv`, 0/16):** obligatorio, ~1 h. Sin eso la decision
  2026-09-14 (4) queda sin verificar.
- **#55:** cerrada como declarada (`main.tex` ya dice que no se asume la precision del paper). No se leen LiTS/KiTS19.
- **#22, tercera regla de umbral:** no se formaliza aparte; el semimaximo ya es la politica principal de E9-TS (#52).
- **Revision clinica de crestas y EIPS:** no se hace; queda declarada como heuristica.
- **#34, #35, #37 (revision de artefactos por la autora):** no se hace; el Objetivo 3 usa el cribado automatico.
- **Vaccaro 1995, Szalkowski 2021, Selles 2023 y MAISI:** no se leen salvo que P1 falle (MAISI) o sobre tiempo.

**Por que:** con ~11 semanas, el camino critico es el VAE. Adaptar solo el decodificador es la prueba mas barata que
decide si el renderizador existe sin romper ControlNet, y fijar la regla antes de correrla evita mover el criterio
despues (#25, #37, #45, #47, #50). Todo lo demas se resolvio en redaccion, sin corridas.

Registrada por el asistente en rol de asesor con delegacion explicita de la autora (2026-09-17). La autora puede revertir
cualquier punto.

---

## 2026-09-17 (2) — No se relanza la cohorte de E6b con RMSE; MAE y RMSE se reportan dentro de P1

**Decision** (delegada al asistente en rol de asesor, 2026-09-17):
- La cohorte de E6b con columnas RMSE **no se corrio** (verificado por la autora en Khipu: solo los jobs 51539, 51540 y
  51591; `~/metalsynth/data/e6b/` vacio). **No se relanza por separado.**
- El script de P1 reporta **MAE y RMSE** en hueso, metal y `B_delta` para el VAE preentrenado y para el de decodificador
  adaptado, en pacientes separados.

**Por que:** RMSE nunca es menor que MAE para los mismos residuos, y la cohorte MAE ya dio 152-212 HU en hueso frente al
umbral de 25 HU. Rehacerla (~8.8 h) no puede cambiar el No-Go del VAE preentrenado; solo aporta la cifra comparable con la
literatura, que P1 produce igual.

**Alternativa descartada:** relanzar la cohorte RMSE antes de P1. Cuesta una corrida y una sesion sin poder cambiar
ninguna decision.

Registrada por el asistente en rol de asesor con delegacion explicita de la autora (2026-09-17).

---

## 2026-09-17 (3) — Regla operativa de la compuerta del Objetivo 1 en P1 (#76)

**Decision** (preguntas 1-4 respondidas por la autora; desempate y marginal decididos por el asistente como asesor por orden
explicita de la autora; todo fijado ANTES de correr P1):
- **Combinaciones:** modelo {VAE de SD 1.5 preentrenado, decodificador afinado con encoder congelado} x codificacion
  {`pub`, `LW20000`, `pub+asinh`}; un decodificador afinado por codificacion. **Hay Go si alguna de las seis pasa.**
- **Lectura de HU:** `vae regla` (canal mas estrecho no saturado, sin usar el HU verdadero). `vae oraculo` es cota.
- **Estadistico:** MAE en hueso (> 150 HU) por paciente; **media sobre los 34 pacientes de test < 25 HU**
  (`experiments/objetivo1/p1_particion.csv`, semilla 20260917, estratos Dataset x Metal). Si falta algun paciente de test,
  la combinacion queda sin veredicto.
- **Multiplicidad:** declarada, sin corregir. IC95 bootstrap por paciente junto a cada veredicto; un pase con limite
  superior >= 25 HU se reporta como **MARGINAL** y no cambia el veredicto.
- **Desempate si pasan varias:** orden a priori, no por error: `pub+asinh`, `LW20000`, `pub`; dentro de cada codificacion,
  preentrenado antes que afinado.
- **No deciden:** RMSE, metal, `B_delta`, mediana, pacientes que fallan, subgrupos.

**Aplicado:** `tesis/main.tex:77` y fila *Representation Viability* de la tabla (compila: 0 errores, 6 paginas, 64
referencias); `p1_decodificador_sd15.py` (`ORDEN_OBJ3`, etiqueta MARGINAL); #76 DECIDIDA Y APLICADA.

**Por que:** las cuatro elecciones cambian el veredicto y no estaban en el documento; una regla preinscrita que solo vive
en un script no se puede auditar. Elegir entre combinaciones por menor error seria seleccionar sobre el test. El orden
pone primero las codificaciones que representan el rango del metal (el techo de 2000 HU de `pub` lo recorta, #39) y el
modelo que menos cambia.

**Alternativas descartadas:** una sola codificacion preinscrita (propuesta del asistente; la autora eligio las tres);
decidir por limite superior del IC95 < 25 HU (mas estricto; la autora eligio la media); desempate por menor MAE.

Registrada por el asistente por orden explicita de la autora (2026-09-17).



---

## 2026-09-17 (4) — Literatura nueva (#77-#82), sin cambio de alcance

**Decision** (delegada al asistente en rol de asesor, 2026-09-17):
- Se leen 8 fuentes nuevas de `refs/raw/`. **Ninguna cambia alcance, hipotesis, objetivos, baseline, la compuerta del
  Objetivo 1 ni el renderizador.**
- **Origen del 2-15% resuelto (#77):** Routt 1997 (2.05%, binario) + cita de Routt a una presentacion de congreso de
  Keating (15%; el articulo publicado da 13%). Templeman no publica ningun porcentaje. El rango sigue retirado.
- **Escala de 4 grados (#78):** no esta en Vaccaro 1995 (Partes I y II). Cadena de #68 cerrada; `main.tex:52` ya es correcto.
- **Ambas cadenas se cierran sin tocar `main.tex`.**
- **Lectura del benchmark bajo artefacto (#79):** Templeman no pudo graduar 5 de 57 tornillos por scatter. Se declara
  como limitacion del Objetivo 2 al escribir sus resultados.
- **Raw duplicados (#82):** `gertzbein1990pedicularscrew` y `templeman1996iliosacralscrews` no generan claves nuevas; sus
  PDF se asocian a `gertzbein1990` y `templeman1996proximity`.
- **Pendiente:** quitar `
ocite{*}` antes de la entrega (#82, recomendado; requiere orden sobre `main.tex`).

**Por que:** las lecturas solo auditan cadenas de citas del Objetivo 2 y confirman decisiones ya tomadas; ninguna justifica
gastar tiempo del camino critico (P1).

**Alternativas descartadas:** ver #77-#82 en `04-implicancias.md`.

Registrada por el asistente por orden explicita de la autora (2026-09-18).


---

## 2026-09-18 — Literatura nueva (#83-#88), duplicados borrados y correccion de `main.tex:117` (#85)

**Decision** (delegada al asistente en rol de asesor; borrado de duplicados y edicion de `main.tex` por orden explicita de
la autora, 2026-09-18):
- **Se leen 13 fuentes nuevas** (12 con PDF completo, `song2024bmar` solo desde el abstract). Ya no queda ningun PDF de
  `papers/` sin ficha ni ningun raw sin su entrada en `clean`. `refs.bib` = 83 entradas.
- **Duplicados borrados:** `miller2012sacralmorphology` (raw y PDF identicos byte a byte a `miller2012variations`),
  `gertzbein1990pedicularscrew` (raw y PDF) y el raw `templeman1996iliosacralscrews`. El PDF de Templeman se renombra a
  `papers/templeman1996proximity.pdf`. Detalle en `refs/MAPEO.md`.
- **#85 APLICADA en `main.tex:117`:** *"With one exception"*. Reilly 2003 midio el corredor con fractura (area para
  tornillos de S1 reducida un 36-90% con 5-20 mm de desplazamiento), lo que respalda medir el corredor en cada volumen. Se
  declara que el benchmark viene de pelvis fracturadas (Tile B y C) y los corredores se miden en pelvis sin osteosintesis.
- **Se cierran sin cambios:**
  - #83: Ziran 2003 no propone el 10 mm y no da prior ordinal en S2.
  - #84: tres atribuciones de Kaiser (a Gardner 2011, Miller y Wu) no aparecen en sus fuentes; `main.tex` no las usa.
  - #86: el punto de entrada y los margenes neurales no tienen fuente en mm, y el diseno no los necesita.
  - #87: los umbrales de metal (2500 y 3000 HU) no tienen origen en la literatura MAR.
  - #88: aviso de versiones (reimpresion de Griffin, preprints de Lyu y ACDNet).
- **Regla de redaccion:** no citar via Kaiser la definicion de dismorfismo, el requisito transsacro ni argumentos etnicos.
- **Pendiente:** quitar `
ocite{*}` antes de la entrega (#82/#88; recomendado); PDF y raw de MWLNet y Choi (prioridades
  1-2 de `_candidatos.md`).

**Por que:** la unica lectura que contradecia el documento era Reilly. Corregirla convierte una afirmacion falsa en
respaldo del diseno, sin nuevas corridas. Las demas lecturas cierran cadenas de citas y no tocan el camino critico (P1).

**Alternativas descartadas:** para #85, (b) acotar la frase a *"clinical CT cohorts"* y (c) borrarla. Tambien crear
claves nuevas para los duplicados y reabrir el punto 8 de `Fuera de alcance`. Detalle en #83-#88 de `04-implicancias.md`.

Registrada por el asistente por orden explicita de la autora (2026-09-18).

---

## 2026-09-19 — Tras el No-Go de P1 (#91): opcion A (difusion en espacio de imagen) y MAISI como extension del Objetivo 1

**Decision** (de la autora, 2026-09-19: *"Acepto tus propuestas"*; sin tope rigido para MAISI a peticion suya;
escrita por el asistente por orden explicita: *"escribelo en 01-decisiones"*):
1. **El No-Go del Objetivo 1 se reporta tal cual** (P1: mejor combinacion afinado `pub+asinh`, 61.72 HU, IC95
   [55.12, 68.99], 34/34 pacientes >= 25 HU; controles 165/165, 330/330, 3/3, 3/3). El criterio no se mueve.
2. **El Objetivo 3 se redisena como difusion en el espacio de imagen, por parches alrededor del implante, sin
   autoencoder.** Es una decision **posterior al resultado**, y asi se declara en la tesis. El diseno
   (`experiments/objetivo3/diseno_A.md`) **se preinscribe antes de entrenar**.
3. **MAISI se evalua como extension del Objetivo 1**, con sus pesos preentrenados, sobre los mismos 34 pacientes de
   test (`p1_particion.csv`) y con la misma regla (media por paciente del MAE en hueso < 25 HU). **Subordinado a A**
   (prioridad de GPU y de tiempo) y **sin tope rigido**; revision conjunta al terminar la semana 3. Paso 0: si su
   normalizacion (codigo o suplementario) recorta el rango del hueso denso, se descarta por diseno sin correr.
   **Su resultado no cambia el diseno del Objetivo 3.**
4. **Pendiente de aplicar tras revisar el diseno:** titulo (*"Multi-Window Latent Diffusion"*), Objetivo 3, #74 y
   `main.tex`; `00-tesis.md` (alcance completo).

**Por que:** la compuerta mostro que los latentes preentrenados no transportan HU de hueso (61.72 HU en el mejor caso,
curvas en plateau, 69.89 HU dentro de `B_delta`). Quitar el latente elimina el error de reconstruccion por
construccion y mantiene multi-ventana, `B_delta`, el protocolo de Peters y el muestreador. MAISI (#93) y MedVAE (#94)
no documentan su rango de HU ni error en HU; MAISI es 3D con difusor propio, por eso solo se mide como argumento del
Objetivo 1.

**Alternativas descartadas:** (a) de #91 sola, sin Objetivo 3 (la autora quiere resultados de generacion); MedVAE
como compuerta nueva (excluye metal en su entrenamiento, #94); seguir con el decodificador afinado de SD como
exploratorio (mostraria imagenes que la propia compuerta rechazo); subir el umbral o cambiar la lectura tras ver el test.

Registrada por el asistente por orden explicita de la autora (2026-09-19).

---

## 2026-09-20 — Geometria del implante para el Objetivo 3 (#97)

**Decision** (de la autora, 2026-09-20: *"Acepto citar Double Medical y canulacion como parametro libre"* y, sobre el
modelado, aceptada la recomendacion del asistente; escrita por el asistente por orden explicita):

1. **Espesor de arandela: 1.5 mm**, citando `doublemedical2021trauma` (*"Thickness: 1.5mm"*, impresa 5/7) y
   **declarando que es otro fabricante**. Synthes y Acumed publican el ancho (13.0 mm) pero no el espesor.
2. **Canulacion: parametro libre del modelo.** No hay fuente citable: el unico valor (2.9 mm) esta solo en listados de
   distribuidor y el documento del fabricante no lo publica. Se evalua macizo frente a hueco como sensibilidad.
3. **Mascara del piloto, dos piezas:** cuerpo cilindrico de **5.0 mm** (medido en E8; el catalogo da 4.8-4.9 mm) y
   **cabeza de 8.0 mm de diametro y 4.5 mm de altura** (`sayres2014comparison`), apoyada en la cortical iliaca y sin
   avellanar. Sin rosca explicita, sin arandela y sin canulacion.
4. **Antes de fijarla se mide** el perfil de diametro **a lo largo del eje** en los tornillos reales de CLINIC-metal
   (E11, `experiments/objetivo2/e11_perfil_axial.py`, CPU local). Si el extremo distal se ensancha hacia 7.3 mm, se
   anade el tramo de rosca; si no, el cilindro uniforme queda justificado con medicion propia.
5. **La envolvente de 6.5-8.0 mm se reserva a la viabilidad del corredor (#31).** Son dos geometrias para dos
   preguntas distintas; `zhu2022optimalposition` usa las dos sin declararlo (p. 1547 frente a p. 1548).
6. **Variantes declaradas como sensibilidad:** envolvente de rosca de 7.3 mm en los 16/32 mm distales y variante
   totalmente roscada; arandela de 13.0 x 1.5 mm; canulacion hueca frente a maciza.

**Por que:** el catalogo describe el tornillo fisico, pero el renderizador aprendio **mascaras por umbral de implantes
reales**, y la mascara de sintesis tiene que parecerse a esas. El fuste de catalogo (4.8-4.9 mm) y el medido en E8
(5.00 mm) coinciden dentro de un cuarto de voxel, asi que el cuerpo se puede modelar con confianza; lo que falta por
decidir (rosca si o no) se resuelve midiendo, no eligiendo.

**Alternativas descartadas:** mantener el cilindro liso de 6.5-8.0 mm en todo el trayecto (sobreestima el area
transversal del metal en mas del doble, #97); perseguir mas fuentes para la canulacion (solo quedaria la guia tecnica
del sistema 7.3 mm de Synthes, y su ausencia no bloquea el piloto).

Registrada por el asistente por orden explicita de la autora (2026-09-20).


## 2026-09-20 (2) — Las cuatro decisiones abiertas del Diseno A (D1-D4), con dos de ellas resueltas por medicion propia

**Decision** (de la autora, 2026-09-20: *"Me gusta la decision D3 que sugieres"*, *"ahora trataremos D2 como
COMPONENTE"* y *"Aplica las recomendaciones que puedes aplicar ahora"*; escrita por el asistente por orden
explicita). Las cuatro corresponden a los `[DECIDIR]` de `experiments/objetivo3/diseno_A.md`.

### D1 — Mascara `M` de entrenamiento: umbral de 2500 HU en el piloto, semimaximo como sensibilidad

Se mantiene el umbral de cribado (#22), que es el unico con validacion propia en esta cohorte (E1: 0 falsos
negativos sobre 113 candidatos). El semimaximo local por objeto entra como analisis de sensibilidad.

**Consecuencia aceptada y declarada:** a 2500 HU los tornillos salen fragmentados en 9 de 57 (E8, #46), asi que
el modelo ve mascaras con huecos mientras que la mascara parametrica de sintesis sera siempre solida. Eso es la
brecha #95 y **no la arregla la eleccion de umbral**: se declara como limitacion.

### D2 — La unidad de entrenamiento es el COMPONENTE, no el corte (#102)

El parche se mantiene en **256 x 256**. Lo que cambia es la unidad: cada **componente conexo** de `M` con su
propia banda `B_delta`, en lugar de la union de todo el metal del corte.

**Por que, con la medicion que lo forzo:** A1 sobre la cohorte dio **2714 de 13496 cortes (20.1%)** con `G` fuera
del encuadre, cuando el piloto de 2 casos habia dado 0%. Se descartaron con datos dos explicaciones — la mezcla de
implantes (20.0% con componente esbelto frente a 20.2% sin) y el spacing (sin tendencia) — y se verifico la real:
en los tres casos peores el metal tiene **9, 12 y 7 componentes** repartidos en **380, 358 y 321 mm**, es decir
toda la anchura pelvica. El parche no era pequeno (211.7 mm de mediana); `G` estaba mal definida.

El argumento de fondo no es de encuadre: en **sintesis** se coloca **un** tornillo. Entrenar con `G` multi-implante
y usar con `G` de un implante es una brecha de dominio distinta de #95, y la extraccion por componente la cierra.

**Verificacion antes de adoptarla:** sobre `CLINIC_metal_0044` —el peor caso de #102, con 215 de 298 cortes sin
contener— la extraccion por componente da **0 de 1217 parches** fuera del encuadre, con control de composicion
1217 de 1217.

**Declarado:** **548 de 1217** parches contienen metal de **otro** componente. No se enmascara, porque es anatomia
real del paciente, pero se cuenta (`n_metal_otros`). Es insumo para #96, no su solucion.

**Alternativas descartadas:** agrandar el parche (el computo crece con el cuadrado del lado y aun asi no cubre
380 mm); dejar 256 por corte y declarar el 20% (ensena al modelo a completar mascaras cortadas por el borde, cosa
que en sintesis no ocurre nunca).

`a1_parches.py` queda **congelado** como evidencia de #102; el script nuevo es `a1b_parches_componente.py`.

### D3 — Geometria de sintesis: cilindro uniforme de ~4.9 mm, cabeza y rosca como sensibilidad (E11, #101)

E11 corrio sobre los **178 volumenes** (79 componentes esbeltos en 43 casos):

- `d_centro` mediana **4.91 mm**, frente a **4.8 mm** de catalogo (`synthes2003guide`) y **5.00 mm** de E8: tres
  vias independientes dentro de **un cuarto de voxel**. El cuerpo del tornillo queda cerrado con medicion propia.
- Ensanchamiento de extremo: mediana **0.96 mm**, del orden de **un voxel**. En el caso tipico el volumen parcial
  promedia cabeza y rosca, asi que el cilindro uniforme **queda justificado midiendo, no eligiendo**.
- Pero **12 de 59** componentes superan 2 mm de ensanchamiento: la cabeza no se declara inexistente y entra como
  variante de sensibilidad, junto con la rosca de 7.3 mm.

**Limites que acompanan a toda cifra de E11:** el filtro es **geometrico** (HU > 2500, largo >= 30 mm, anchos
<= 12 mm), **no clinico**: selecciona componentes metalicos alargados y finos, y **no afirma que sean tornillos
iliosacros**. Sus seis limitaciones estan en `experiments/objetivo2/e11_perfil_axial.md`. **`d_max` (8.10 mm) es
un maximo sobre tramos, sesgado al alza, y no debe citarse como diametro de cabeza medido.**

Esto sustituye al punto 3 de la decision del 2026-09-20 (que fijaba 5.0 mm sobre E8) y **cumple su punto 4**, que
condicionaba la geometria a medir el perfil axial.

### D4 — Criterio de exito: la forma se fija ahora, el margen de equivalencia despues del piloto

`main.tex:98` promete *"Lower profile discrepancy than naive copy-paste insertion, with streak amplitudes
statistically comparable to, or better than, the adopted physics-based protocol"*. Son dos contrastes distintos:

1. **Endpoint primario unico, declarado antes de mirar el test: streak amplitude.** Las demas metricas de Peters
   quedan **descriptivas**. Sin esto se repite el patron de #76 (varias combinaciones, basta con que pase una).
2. **"Mejor que copia-pega" = superioridad**, pareada (mismos pacientes en los dos brazos) y de **una cola**:
   **Wilcoxon de rangos con signo**, alfa 0.05, reportando tamano de efecto e IC ademas del p.
3. **"Comparable al brazo fisico" = equivalencia, con TOST**, no un contraste de diferencia. Un p > 0.05 con
   n = 14 indica falta de potencia mucho mas probablemente que igualdad. Se concluye equivalencia solo si el
   **IC90** de la diferencia pareada cae entero dentro de `[-Delta, +Delta]`.
4. **El margen `Delta` NO se fija hoy, y no por descuido.** No existe umbral publicado de "streak amplitude
   comparable" (mismo hueco que el proyecto ya declaro para los 25 HU, decision 2026-09-15 (2)), y calibrarlo
   sobre los resultados de test seria exactamente el patron prohibido. `Delta` se define como la **variabilidad
   propia del metodo bajo condiciones que no deberian cambiar el resultado** — dispersion entre semillas DDIM del
   mismo caso y test-retest del brazo fisico — medida **solo en los 5 pacientes de validacion**, nunca en los
   20/14 de test, y escrita aqui **antes** de correr la evaluacion.

**Declaracion de potencia, aceptada de antemano:** n = 14 sin metal y n = 20 con metal son muestras chicas para un
TOST. Es posible que el resultado honesto sea *"no se pudo concluir equivalencia con esta n"*, y **eso se
reportara como tal**: el Objetivo 1 de esta tesis ya demuestra que un resultado negativo es publicable. No se
convertira un no-concluyente en un "comparable" por la via del p > 0.05.

### Fuera de las cuatro, decidido en el mismo turno

- **Mitigacion de #96:** el piloto corre con **contexto intacto**. El contexto recortado o suavizado entra **solo**
  como brazo de sensibilidad preinscrito, no como arreglo posterior si la costura sale fea.
- **Preinscripcion:** `diseno_A.md` se congela y se registra **cuando se mida `Delta`**. Es lo unico que falta.
- **#89:** el presupuesto de computo del Objetivo 3 se cierra con la cifra **medida** en el piloto de 200 pasos en
  Khipu (`a2_entrenar.sbatch`), no con la extrapolacion desde P1, que era otro modelo.

Registrada por el asistente por orden explicita de la autora (2026-09-20).

## 2026-09-21 — Criterio de inclusion del conjunto de entrenamiento del Objetivo 3 (R1-R3), PREINSCRITO

**Decision** (de la autora, 2026-09-21: *"apruebo las 4 reglas actuales"*, *"Acepto estos nuevos parametros"* y
*"congela esos parametros"*; escrita por el asistente por orden explicita). Congela la composicion del conjunto
con el que se entrenara el renderizador. Implicancias que la originan: **#104, #105, #109, #110, #111, #112**.

### Lo que se descarto, y por que consta aqui

La primera propuesta del asistente filtraba por **forma** (PCA tipo tornillo) y por **volumen** (>= 200 mm3).
**Las dos quedan descartadas**, con medicion:

- El renderizador aprende la relacion **mascara -> artefacto**, que es fisica y **no depende** de si el objeto
  es tornillo, placa o fragmento. Filtrar por forma tira datos que ensenan justo lo que se quiere aprender: en
  la muestra revisada solo **5 de 40** componentes son tornillos.
- El umbral de 200 mm3 quita solo el **4%** de los parches pero elimina el **29%** de los componentes: descarta
  variedad de formas sin ganar tamano de conjunto.

La pregunta que decide cada regla no es *"¿esto es un tornillo?"* sino **"¿este ejemplo ensena algo que en
sintesis sera falso?"**.

### Reglas congeladas

1. **R1 — el componente esta dentro del cuerpo.** Cuerpo = tejido por encima de **-400 HU**, componente conexo
   mayor, huecos rellenos (`a4_html_componentes.mascara_cuerpo`). Motivo: un electrodo o una cremallera tienen
   contexto de aire y piel; en sintesis el tornillo va en hueso.
   - **El umbral de fraccion minima (`--dentro-min`) es INVARIANTE y no se elige.** Medido sobre los 40
     componentes revisados, `frac_dentro` es **0.000 o 1.000, nunca intermedio**; el barrido de **0.05 a 0.95**
     da exactitud 92% con TP/FP/TN/FN identicos. Se fija en **0.5** por convencion, y **se declara que
     cualquier valor del rango da el mismo resultado**. Es el mismo argumento con que se justifico `F = 0.001`
     (decision 2026-09-14 (5)).
2. **R2 — el caso tiene material ortopedico declarado** en `Tipo de estructura observada` de `revision.csv`.
   Se usa **solo en la direccion que concluye**: si el caso **no** tiene material ortopedico, ningun componente
   suyo puede ser implante. La direccion contraria **no dice nada** del componente (#110, verificada con cero
   contradicciones sobre los 40 veredictos).
3. **R3 — el parche contiene metal del componente objetivo**, mas una proporcion declarada de parches de solo
   banda. **No se eliminan del todo**: la banda mas alla de la punta del implante es real.
   - **`ratio-banda` = 0.62**, que es **todos los parches de solo banda disponibles** tras R2.
   - **Brecha declarada:** el ratio que producira la **sintesis** es **1.40** (calculado sobre 908 corredores
     viables de `e9ts_corredor.csv`, robusto al diametro supuesto: 1.40 con 4.9 mm, 1.23 con 7.3, 1.19 con 8.0).
     **1.40 NO es alcanzable**: harian falta 14 820 parches de banda y solo hay 6 584. Se entrena con 0.62 y
     **la diferencia se declara como limitacion**, junto a #95 (forma de la mascara) y #96 (contexto).
4. **R4 — tamano y forma NO filtran: se reportan.** Se publica la mezcla del conjunto por volumen y elongacion,
   y se declara que **el tipo de implante no esta anotado** (`main.tex:111`).

### Conjunto resultante (particion `train` de `p1_particion.csv`, semilla 20260917)

| | Parches | Componentes | Casos |
|---|---|---|---|
| A1b completo | 21 754 | 339 | 72 |
| Tras R2 | 17 170 | 241 | 47 |
| Con metal (R3) | 10 586 | 241 | 47 |
| **Congelado (R2 + R3 con ratio 0.62)** | **17 170** | **241** | **47** |

### Validacion del criterio, sobre la muestra ya revisada

Medido con `a5_criterio_inclusion.py` **sobre las mismas 40 laminas** de #104 (la regla fijada de antemano
prohibe generar una muestra nueva para esto); 1 `dudoso` excluido del calculo, no forzado a ningun lado:

**36 de 39 = 92% de acuerdo binario incluir/excluir**, precision 88%, **recall 100%**. El criterio anterior,
basado en forma y volumen, acertaba **16 de 40 = 40%** de tipo. De los 14 aciertos de exclusion, **7 los caza
R1** y **7 los caza R2**: ninguna regla es redundante.

**Limitacion declarada:** los 3 falsos positivos —dos piezas de `metal_0045` que estan dentro del cuerpo pese a
ser marcadas `externo`, y el DIU de `metal_0062`— **no los separa ninguna regla geometrica**. Requieren criterio
humano y se aceptan como error conocido del criterio.

### Lo que queda fuera de esta decision

- **La particion de validacion** sigue con **2 de 5 casos sin ningun implante** (#105). Se decide aparte; toca
  la *Strict Isolation Rule* de `main.tex:111` y condiciona la medicion del margen `Delta` de D4.
- **La opcion de extraer mas parches de banda** bajando `MIN_VOX_G` queda **descartada por ahora** (#112): la
  perdida normaliza por imagen, asi que parches con `G` diminuta pesarian igual que un tornillo entero y
  dominarian el gradiente. Se reconsidera **solo** si el piloto muestra problema de costura, y entonces
  **junto** con cambiar la normalizacion a peso proporcional a `|G|`.

Registrada por el asistente por orden explicita de la autora (2026-09-21).

## 2026-09-21 (2) — Validacion: se aplica R2 tambien a `val`, sin rehacer la particion (#105)

**Decision** (de la autora, 2026-09-21: pide reevaluar si la recomendacion sobre #105 era la adecuada y
aplicarla si procede; escrita por el asistente por orden explicita). **Reemplaza la recomendacion anterior del
asistente**, que proponia rehacer la particion de validacion.

**Lo que se hace:** el criterio de inclusion preinscrito hoy (R1-R3) se aplica **igual a `train` y a `val`**.
No se rehace la particion, no se cambia la semilla 20260917 y **no se toca `test`**.

**Por que la recomendacion anterior se descarta:** rehacer la particion tocaba la *Strict Isolation Rule*
(`main.tex:111`) y la semilla sobre la que descansa el resultado **No-Go del Objetivo 1** (#91), que es un
resultado de la tesis. El problema no lo justificaba.

**Dato que corrige el planteamiento:** `val` tiene **8 casos**, no 5. Tres llevan material ortopedico
(`metal_0011`, `metal_0039`, `metal_0056`), tres **no llevan metal** (`CLINIC_0046`, `CLINIC_0066`,
`CLINIC_0101`) y dos llevan metal **no ortopedico** (`CLINIC_0019`, accesorio; `CLINIC_0102`, cremallera).
Los tres sin metal **no son un problema**: son el caso de uso de sintesis (analogo del bloque E-A2). El
problema se reduce a **dos casos**, y R2 los excluye por la regla ya escrita.

**Ventaja decisiva:** **cero seleccion post hoc.** No se elige que casos entran; se aplica un criterio fijado
antes. Mover casos de `train` a `val` para volver a cinco habria obligado a **elegir cuales**, despues de ver
los datos.

**Resultado:** `val` queda en **896 parches** (553 con metal, 343 de banda) sobre **3 casos con implante real**.
Manifiesto versionado en `experiments/objetivo3/a5_manifiesto_val.csv`, generado por el mismo codigo que el de
entrenamiento.

**Limitacion aceptada y declarada:** el margen `Delta` de D4 se medira sobre **3 pacientes**. Es poco. Mitiga
en parte que `Delta` mide variabilidad **intra-metodo** (semillas DDIM sobre el mismo caso, mas test-retest del
brazo fisico), de modo que el n efectivo es 3 casos por k semillas y no 3 observaciones. **El informe debe
declarar esta n**, y no presentar el `Delta` resultante como robusto.

Registrada por el asistente por orden explicita de la autora (2026-09-21).

---

## 2026-09-22 — Objetivo 2: las siete decisiones de la agenda (D-O2.1 a D-O2.7), PREINSCRITAS

> Registrada por el asistente **por orden explicita de la autora** (2026-09-22, en chat: *"Estoy de acuerdo
> con todas tus recomendaciones, aplicalas (y redacta mi decision en donde corresponda)"*). Mismo
> procedimiento que la entrada del 2026-09-21 (2). La regla 3 sigue vigente para todo lo demas.

Estas siete decisiones se toman **antes** de calcular un solo Wasserstein-1 contra `zwingmann2009navigated`.
Esa anterioridad es lo que hace del resultado una validacion y no un ajuste, y por eso consta la fecha.

### D-O2.1 — El muestreador NO se calibra contra Zwingmann. Se muestrea, se mide y se compara

Se adopta la **opcion (a)**: muestrear poses desde una distribucion geometrica **declarada y preinscrita**,
**medir** la distribucion de grados de brecha que resulta, y **compararla** con las dos distribuciones
ordinales de `zwingmann2009navigated` por distancia de Wasserstein-1.

Se **rechaza** la opcion (b) —calibrar el muestreador para reproducir las proporciones de Zwingmann— porque
compara contra lo que se uso para ajustar. Con (b) la metrica dejaria de ser validacion y pasaria a ser
verificacion de ajuste, y SAP, que `00-tesis.md` declara **unica metrica introducida por esta tesis**, se
quedaria sin contenido evaluativo.

**Condicion que hace exigible la decision, y no solo declarativa:** los parametros de la perturbacion
**no pueden derivarse de Zwingmann ni ajustarse mirando el W1 resultante**. Salen de fuente independiente
(holgura cortical de 5 mm de `kaiser2014dysmorphism`; tolerancia angular de 4 grados que Zwingmann cita de
terceros en su Introduction, p. 1834) o se declaran convencion. Se fijan **una vez**, por escrito, antes de
medir.

**Se acepta de antemano que el W1 puede salir alto.** Ese resultado es reportable y sigue siendo el
resultado propio de la tesis. Lo que no seria reportable es un W1 bajo obtenido moviendo parametros.

### D-O2.2 — Cohorte: 72 casos primaria, 49 sensibilidad. El pendiente de FOV queda cerrado

Cohorte primaria del Objetivo 2: **72 casos** (grupos 2 y 3 con QC de nivel). Sensibilidad: **49 casos**
(grupo 3). Las dos tablas ya existen en `e9ts_resumen.md` y no hay que recalcular nada.

El pendiente que `00-tesis.md` arrastraba desde el 2026-09-11 —*"El tratamiento de los 7 con FOV cortado
sigue sin decidir"*— **se cierra por irrelevancia para esta cohorte**: verificado sobre
`e9ts_corredor.csv` (152 casos unicos), `fov7 = True` se da en **4 casos y los cuatro son de grupo 1**.
Ninguno entra en grupos 2 o 3. Ver **#119**.

### D-O2.3 — Definicion operativa de la brecha cortical

La brecha se mide como **profundidad de protrusion del cilindro fuera de la envolvente osea**:

1. Envolvente osea `B`: la **misma** del corredor (union de `sacrum`, `vertebrae_S1`, `hip_left`,
   `hip_right` de TotalSegmentator, cierre morfologico de 2 mm, relleno de cavidades cerradas en 3D). Se
   reutiliza, no se redefine: si SAP usara otra envolvente, el grado y la viabilidad dejarian de ser
   comparables entre si.
2. Campo de distancia euclidea **fuera** de `B`, con el spacing del header.
3. Se muestrea la **superficie lateral** del cilindro a lo largo del eje y en angulo. Para cada punto
   fuera de `B`, su profundidad es el valor del campo. **Brecha = maximo** sobre todos los puntos.
4. Se excluyen **8 mm por extremo** del tramo oseo, con el mismo `RECORTE_EXTREMO_MM` de `e9_corredor.py`.
   **Razon clinica, no numerica:** un tornillo iliosacro entra y sale por la cortical del ilion **por
   diseno**. Sin este recorte, toda trayectoria valida puntuaria como grado 3 por sus propios puntos de
   entrada y salida.

#### CORRECCION DE D-O2.3 (2026-10-04)

> Registrada por el asistente **por orden explicita de la autora** (chat del 2026-10-04). La regla 3
> sigue vigente para todo lo demas.
>
> **Los cuatro puntos de arriba se conservan tal como se escribieron el 2026-09-22.** No se corrigen en
> su sitio a proposito: este archivo es una **bitacora de decisiones**, no una especificacion. Su valor
> esta en poder reconstruir que se decidio y cuando; reescribir el pasado para que coincida con el
> codigo lo convertiria en documentacion y destruiria la auditoria. Lo que sigue **sustituye** a los
> puntos 1, 3 y 4 como definicion operativa vigente.

**Que paso.** Tres de los cuatro puntos describen una implementacion que nunca existio en E9-TS. Los
tres desajustes tienen el mismo origen: D-O2.3 dice *"la misma del corredor"* y copio la descripcion de
`e9_corredor.recortar`, que es la via **por umbral de HU** que #48 reemplazo. Cuando E9-TS cambio la
fuente de la mascara a TotalSegmentator, esas tres frases dejaron de describir lo que se ejecuta.

| Punto | Lo que decia | Lo que hace el codigo |
|---|---|---|
| 1 | cierre de 2 mm **+ relleno de cavidades cerradas en 3D** | **solo** el cierre de 2 mm |
| 3 | muestrear la **superficie lateral** del cilindro | medir sobre el **eje**: `max(0, radio + sd)` |
| 4 | recorte de 8 mm sobre el **tramo oseo** | recorte de 8 mm sobre el **propio implante**, de longitud fija |

**Por que no se corrige el codigo y se vuelve a correr, que era la otra opcion.**

- **Punto 1, medido (E14, `outputs/e14_relleno.csv`, 152 casos, 0 errores):** anadir el relleno cambia
  `D_TS` en **0 de los 72 casos de la cohorte**, con diferencia maxima de **0.000 mm**. Los 4 casos que
  se mueven en toda la coleccion estan fuera de la cohorte. Volver a correr produciria **las mismas
  cifras** a cambio de rehacer E9-TS, E12 y E13.
- **Y hay una razon de construccion, no una casualidad:** el relleno existia para tapar el hueco
  trabecular de una mascara por umbral de HU, que queda como un cascaron cortical (`e9_corredor.py`:95-98
  lo dice explicitamente). Las etiquetas de TotalSegmentator son volumenes solidos: **no hay hueco que
  tapar**. El relleno es un no-op por diseno de la fuente, no por suerte.
- **Puntos 3 y 4** ya se habian corregido en el codigo **con motivo y por control**, no por descuido:
  los fijo la **#120** despues de que los controles C5 y C6 de E12 tumbaran dos definiciones anteriores.
  Medir sobre la superficie daba 1.000 mm donde la identidad exige 0; hacer depender el tramo del hueso
  premiaba a las poses que se salen. La definicion vigente es **mejor** que la escrita, no una
  desviacion a reparar.

**Definicion operativa vigente, que es la que esta implementada en `src/muestreador/sap.py`:**

1. **Envolvente osea `B`:** union de `sacrum`, `vertebrae_S1`, `hip_left` y `hip_right` de
   TotalSegmentator, con **cierre morfologico de 2 mm**. **Sin relleno de cavidades**, porque con
   mascaras de TS no anade nada (E14). Sigue siendo **la misma del corredor**, que es lo que el punto 1
   queria garantizar.
2. **Campo de distancia signada** `sd`: positiva fuera de `B`, negativa dentro, cero en el borde. Se usa
   signada y no solo exterior para que la identidad *"cilindro de diametro `D_TS_max` sobre el eje del
   corredor => brecha 0"* se cumpla por construccion (#120).
3. **Brecha** `= max sobre t de max(0, radio + sd(c + t u))`, evaluada **sobre el eje**, no sobre la
   superficie lateral.
4. **Tramo evaluado:** el **propio implante**, de longitud fija igual a la del corredor de ese caso,
   centrado en la pose anclada al punto medio del corredor, y recortado **8 mm por extremo**. La razon
   clinica del punto 4 original no cambia; lo que cambia es que la extension es la del implante y **no
   depende de donde este el hueso**.
5. **Resolucion declarada: 0.083 mm** (control C1 de E12). Por debajo, la metrica no distingue.

**Que cierra esta correccion:** el punto 13 de **#127**. **Ninguna cifra publicada cambia.**

**Limite que se declara en el mismo sitio donde se reporte la cifra:** la mascara de TotalSegmentator es
una mascara de **hueso**, no una segmentacion de cortical. Su borde **aproxima** la superficie cortical
externa. SAP mide protrusion fuera de la envolvente osea segmentada, y asi debe enunciarse; no se
reclama medicion de cortical.

**Control que puede fallar, obligatorio en cada corrida:** un cilindro de diametro `<= D_TS_max` centrado
en el eje del corredor de ese mismo caso **tiene que dar brecha 0**, porque `D_TS_max` es por construccion
dos veces la distancia libre minima a lo largo del eje recortado. Si da mas que 0, la implementacion esta
mal y la cifra no se usa. Se anade la monotonia en diametro: la brecha no puede decrecer al ensanchar el
cilindro.

### D-O2.4 — El diametro de SAP es 7.0 mm. Es una TERCERA geometria, y se declara como tal

`zwingmann2009navigated` midio sus grados sobre tornillos canulados de **7.0 mm**: *"the screws using a
7.0-mm cannulated screw"* (Materials and Methods, p. 1835). La profundidad de perforacion escala con el
radio, asi que medir SAP con otro diametro mete un sesgo sistematico dentro del propio Wasserstein-1 y lo
vuelve ininterpretable: no se sabria cuanto de la distancia es diferencia de poses y cuanto es diferencia
de calibre.

**SAP se mide con un cilindro de 7.0 mm.** `4.91 mm` y `7.3 mm` entran como **sensibilidad declarada**.

Con esto el proyecto pasa a declarar **tres** geometrias con tres propositos distintos, y no se mezclan:

| Geometria | Para que | Origen |
|---|---|---|
| Envolvente **6.5-8.0 mm** | viabilidad de corredor, `Dmax >= d + 2c` | #31, decision 2026-09-11 |
| Cilindro **~4.91 mm** | lo que se **sintetiza** en el Objetivo 3 | D3, decision 2026-09-20 (2) |
| Cilindro **7.0 mm** | lo que **mide** la brecha en SAP | esta decision; #118 |

**No se reabre D3.** Cambiar la geometria de sintesis a 7.0 mm obligaria a rehacer E11 y la cache de
17 149 parches, y D3 respondia a una pregunta distinta ("que se sintetiza"), no a esta ("con que se mide
la brecha"). `zhu2022optimalposition` ya usa dos diametros sin declararlo; aqui se declara.
7.0 cae dentro del rango 6.3-8 mm de Kaiser que `main.tex` ya cita, asi que no contradice lo escrito.

### D-O2.5 — S1 y S2: se muestrea en los dos, el prior ordinal es solo S1

El muestreador propone pose en **S1 y en S2**. El benchmark ordinal de Zwingmann y el Wasserstein-1 se
aplican **solo en S1**. S2 se reporta **descriptivamente** (geometria y grados de brecha), sin prior
clinico. Es lo que ya cerraron #12 y #28 y no se reabre.

### D-O2.6 — La fraccion por zona de densidad es componente REPORTADO de SAP, no condicionante del muestreo

Entra como **componente que se reporta**, calculado sobre `e9b_densidad_s1.csv`. **No** condiciona la
distribucion de muestreo. Si condicionara el muestreo se convertiria en un parametro ajustable mas, y la
circularidad que D-O2.1 acaba de cerrar volveria a entrar por la puerta de atras.

### D-O2.7 — Preinscripcion

SAP y la distribucion de poses se congelan por escrito **antes** de calcular el primer Wasserstein-1,
igual que se hizo con `diseno_A.md` y con el criterio de inclusion R1-R3. Esta entrada es esa
preinscripcion para las siete decisiones; la distribucion de poses concreta se preinscribe en su propio
documento cuando se fije.

### Orden de implementacion decidido en el mismo turno

**SAP primero, muestreador despues.** SAP se puede validar sobre los tornillos **reales** ya censados
(E8/E11), donde la posicion es dato y no salida del muestreador. Implementar el muestreador antes
obligaria a depurar metrica y muestreador a la vez, con dos fuentes de error simultaneas y ninguna
referencia externa.

---

## 2026-10-05 — Suelo de -1000 HU de la representación multiventana: `run02` corre sin cambios y la cantidad que decidirá se preinscribe hoy (#141)

**Decisión:** la codificación `pub+asinh` del Objetivo 1 **no se toca para `run02`**, y la cantidad
que decidirá si se declara o se cambia **se preinscribe en esta entrada, antes de conocer `Delta`**.
Dictada por la autora tras la recomendación del asistente y registrada por él con instrucción
explícita el 2026-10-05.

1. **`run02` corre con la representación actual.** Cambiar el suelo exigiría recachear los 23 058
   parches y reentrenar, cuesta el turno de cola ya asignado (arranque predicho 2026-10-06T04:02 en
   un clúster saturado) y reabriría una decisión preinscrita del Objetivo 1 **después** de haber
   visto un resultado.

2. **Cantidad preinscrita.** La fracción del vano entre los extremos del 5 % que **sobrevive a la ida
   y vuelta por la representación**, medida **sin modelo** sobre la banda `G \ M` de los **77
   pacientes con metal de entrenamiento y validación**, nunca de test
   (`experiments/objetivo3/a9_suelo_representacion.py`, 23 058 parches, 2026-10-05):

   | Estadístico, entre pacientes | Valor |
   |---|---|
   | mediana de la mediana del paciente | **0.999** |
   | mediana del percentil 5 del paciente | **0.914** |
   | peor paciente (mediana) | **0.498** |
   | pacientes con > 10 % de la banda recortada | **19 de 77** |

   La pérdida atribuible a la representación es `1 -` esos valores.

3. **Regla de decisión, evaluable cuando `Delta` exista** (tras el piloto de `run02` sobre los 5
   pacientes de validación, D4): si la pérdida de vano atribuible a la representación es **menor**
   que `Delta`, el suelo de -1000 HU se **declara como limitación de alcance** y la representación no
   se cambia. Si es **mayor** que `Delta`, la representación es la **restricción activa** del
   Objetivo 3 y se cambia, con la recacheada y el reentrenamiento que eso implica.

4. **La regla se evalúa en el percentil 5 del paciente, no en la mediana.** El efecto es de cola: en
   el paciente típico el recorte toca el 1.0 % de la banda y el vano sobrevive al 99.9 %, pero 19 de
   77 pacientes pasan del 10 % de banda recortada y en el peor el parche mediano pierde la mitad del
   vano. Evaluar en la mediana haría pasar la regla trivialmente y dejaría fuera justo a los
   pacientes donde el problema existe. *Este punto lo propuso el asistente después de ver la
   distribución, y la autora lo adopta; queda declarado como elección post hoc del estadístico de
   decisión, no como criterio fijado a ciegas.*

5. **Se declara en tres sitios, decida lo que decida la regla:** en el alcance, en las amenazas a la
   validez de constructo con la dirección del sesgo, y en el criterio de la compuerta del Objetivo 1,
   cuyo alcance cubre HU de hueso y **no** el rango negativo del artefacto.

6. **Toda cifra del vano que llegue al documento va con su salvedad en la misma oración.** Lo medido
   **no es `streak amplitude`**: es la forma del estadístico de Peters calculada sobre HU en la banda,
   porque la desviación respecto a verdad de terreno no existe para un paciente real con metal y la
   inversión de las métricas de Peters sigue sin definirse (#16, #17). Y el proxy **subestima**: la
   banda está dominada por el contraste hueso-aire y no por el streak, mientras las ROIs de Peters se
   trazan perpendiculares a los streaks fuertes. El 0.999 es un **límite superior optimista**.

**Alternativas descartadas:** (a) **cambiar el suelo ahora** —un cuarto canal, o un `asinh` con signo
sobre un rango simétrico— y relanzar: pierde el turno de cola, deja la tesis sin primer entrenamiento
válido y convierte una decisión preinscrita en una reacción a un resultado; (b) **declararlo sin
medirlo**: la cifra que originó el hallazgo (23.4 % de la banda) venía de un solo componente de un
solo paciente y resultó ser de la cola alta, no el caso típico; (c) **inferir la pérdida del mínimo de
HU de cada volumen**: la correlación entre ese mínimo y lo recortado es **-0.12**, prácticamente nula,
así que saber hasta dónde baja un volumen no predice cuánto pierde.

**Por qué:** la métrica afectada es `streak amplitude`, que `peters2025hybrid` define (§2.5, p. 5)
como la diferencia entre el promedio del 5 % superior y el del 5 % inferior de la desviación, es decir
el vano entre el lóbulo claro y el oscuro. El suelo recorta uno de los dos extremos, el sesgo es de
dirección conocida y siempre a la baja, y **afecta al brazo del sintetizador y no al brazo físico**,
que reconstruye y no pasa por esta codificación. Por eso esto toca **D4** y no solo la redacción: un
TOST de equivalencia con un lado sesgado por construcción no mide lo que dice medir. Y por eso la
cantidad se preinscribe hoy: `Delta` se mide después del piloto por diseño, así que fijar ahora el
número contra el que se comparará es la única forma de que el desenlace —cualquiera de los dos— no
quede elegido después de verlo.

---

## 2026-10-05 (2) — El entrenamiento del renderizador se fija en 30 000 pasos (B2, #134)

**Decisión:** el número de pasos del entrenamiento del Diseño A es **30 000**. Dictada por la autora
tras ver las curvas de `run01` y `run02`, y registrada por el asistente con instrucción explícita el
2026-10-05.

**De dónde sale la cifra, y qué clase de elección es.** Las dos corridas trazan la misma curva de
validación dentro de **1.5e-3** en todos los bloques compartidos, con instrumentos de medición
distintos, y las dos muestran que el mínimo **no es un punto sino una meseta** que va de ~20 000 a
~40 000 pasos:

| Bloque | `run01` | `run02` |
|---|---|---|
| 20 000 | **0.05809** | 0.05927 |
| 30 000 | 0.06008 | **0.05891** |
| 40 000 | 0.06058 | 0.06132 |
| 50 000 | 0.06310 | 0.06364 |

30 000 cae en el **centro** de esa meseta. Pasado el bloque 40-50 k la validación sube de forma
monótona en las dos corridas.

**Esto es una elección de hiperparámetro hecha sobre VALIDACIÓN, y se declara como tal.** No fue
fijada de antemano: sale del mínimo observado en `run01` y `run02`, las dos medidas sobre los 5
pacientes de validación y **ninguna sobre test**. Validación existe precisamente para esto y no
compromete el aislamiento por paciente (`main.tex`:111), pero presentarla en el documento como un
valor elegido a priori sería falso. En `diseno_A.md` y en la tesis va con esa salvedad.

**Alternativas descartadas:** (a) **40 000**, el extremo alto de la meseta: defendible con la misma
evidencia, pero cuesta un 33 % más de cómputo para un valor de validación que no mejora;
(b) **60 000**, lo que corrió `run02`: los últimos 22 500 pasos **empeoraron** el modelo, el 37.5 % de
la corrida se gastó después del óptimo; (c) **mantener 200 000** como en el borrador original: la
curva de `run01` sube durante doce bloques consecutivos hasta 0.10807, casi el doble del mínimo.

**Por qué:** con el margen de cómputo que da la meseta, el criterio que queda es el coste. 30 000
pasos son ~3 h 10 en la partición MIG `a100_3g.20gb` al ritmo medido de 0.377 s/paso, frente a ~4 h 15
con 40 000 y ~6 h 20 con 60 000. En un clúster saturado, donde el turno es el recurso escaso y la
corrida preinscrita todavía está por delante, un 25 % menos de tiempo de pared por corrida es la
diferencia entre caber en un turno y esperar otro. Y `mejor.pt` sigue escribiéndose en cada mínimo de
validación (#134), así que una corrida que se corte antes de los 30 000 tampoco pierde el modelo.

---

## 2026-10-05 (3) — Definición operativa de `streak amplitude` para síntesis, y jerarquía de contrastes del Objetivo 3 (D4, #16, #17, #141)

**Decisión:** se adopta la definición de `peters2025hybrid` §2.5 con una sola sustitución declarada, y
se fija la jerarquía de contrastes. Dictada por la autora el 2026-10-05 sobre la recomendación del
asistente, y registrada por él con instrucción explícita. **Esta entrada es preinscripción: se escribe
antes de tocar los pacientes de test.**

### 1. La verdad de terreno es el CT limpio del mismo paciente, y eso ancla el endpoint en E-A2

Peters la define como *"the average over the highest and lowest 5% CT number deviation to ground truth
in each ROI"*, y *"the remaining streak amplitude is then defined as the difference between the two"*.
En MAR la verdad de terreno existe; en síntesis hay que decir cuál es. Se fija:

> verdad de terreno = el CT original **sin metal** del mismo paciente
> campo de desviación: Δ(x) = I_sintética(x) − I_original(x), en HU

Eso solo existe en los **14 pacientes de test sin metal**, que es exactamente donde D4 ya pone el
endpoint primario. La definición no se inventó para encajar: encaja porque el endpoint ya estaba ahí.

**Consecuencia que corrige un defecto de la tabla de evaluación.** `diseno_A.md` §7 lista
`streak amplitude` como medible en **E-A1** (20 pacientes con metal). **Ahí no hay verdad de terreno y
no se puede medir.** Lo que E-A1 puede medir es **discrepancia** entre lo sintetizado y el CT real, que
es otra magnitud y debe llamarse así. La fila de E-A1 se corrige: `bone integrity` y `metal integrity`
se mantienen, `streak amplitude` sale de E-A1 y pasa a nombrarse discrepancia, con el MAE en HU dentro
de `G` que ya estaba como descriptivo.

### 2. Las ROIs se derivan de la pose, no se trazan a mano

Peters las coloca manualmente *"perpendicular to strong streak artifacts in the uncorrected images"*, y
su propio texto declara esa colocación como limitación. Aquí la pose es analítica (`c`, `u`), así que:

> en planos perpendiculares a `u`, **arcos anulares** a radios declarados dentro de `B_δ`, excluyendo
> `M` y una guarda de un vóxel

Los streaks radian desde la sección de metal, así que un arco tangencial los cruza, que es lo que
"perpendicular al streak" significa. Tres razones: es reproducible sin lector; es **idéntica para los
dos brazos**, como `diseno_A.md` ya exige ("misma anatomía y mismas poses"); y se declara como
**desviación del protocolo publicado**, coherente con que `main.tex` ya diga que extenderlo a síntesis
exige adaptación explícita y **no hereda su validación**.

### 3. La censura por el suelo de −1000 HU se reporta como cifra, no como salvedad en prosa

El 5 % inferior de la desviación es exactamente lo que el suelo de la representación multiventana
censura (#141). Junto al endpoint se reporta siempre:

> fracción de vóxeles de la ROI de la imagen sintética que quedan **exactamente en el suelo**
> (−1000 HU)

Si esa fracción es apreciable, la cola inferior está **censurada** y `streak amplitude` es una **cota
inferior**, dicho con un número. Esto hace #141 auditable en el momento de la evaluación y permite
afirmar que el método midió y reportó su propio techo. **El brazo físico reconstruye y sí puede bajar
de −1000 HU**, así que esta cifra separa lo que es límite de la representación de lo que es límite del
modelo.

### 4. La unidad de agregación es el paciente

Mediana sobre ROIs y cortes → **un valor por paciente** → pruebas pareadas sobre n = 14. Es obligado
porque D4 usa Wilcoxon pareado y TOST con n = 14. **Cierra el `\GAPDEC` abierto** sobre cómo se agregan
poses y regiones de medición antes de Wilcoxon y TOST.

### 5. Jerarquía de contrastes, y por qué el de copia y pegado no es evidencia

| | Contraste | Qué prueba |
|---|---|---|
| **Primario** | TOST contra el brazo físico, E-A2, con margen `Delta` | equivalencia |
| **Realismo** | distancia entre la distribución de amplitudes sintéticas y la medida en CLINIC-metal real | que lo generado se parece a lo que existe |
| **Cordura** | Wilcoxon de una cola contra copia y pegado | piso, **no** evidencia de calidad |

**El contraste contra copia y pegado es casi vacuo y se declara como tal.** El propio diseño dice que
la copia y pegado *"no puede producir"* streaking por construcción, así que su amplitud vale ~0 y
cualquier cosa que genere algo gana. Es un control de cordura.

El de **realismo** entra porque hace que los dos componentes de la tesis se evalúen con la misma
lógica: el Objetivo 2 compara **distribuciones** de grados contra una referencia clínica externa
(Zwingmann) y no instancias; el Objetivo 3 hará lo mismo con las amplitudes contra CLINIC-metal real.
La coherencia metodológica entre los dos objetivos es un argumento del documento, no un adorno.

**Alternativas descartadas:** (a) medir `streak amplitude` en E-A1 usando una referencia
reconstruida o suavizada como sustituto de la verdad de terreno: introduce un paso sin validación en
el centro del endpoint primario; (b) colocar las ROIs a mano siguiendo a Peters al pie de la letra:
hereda una limitación que ellos mismos declaran y hace irreproducible la comparación entre brazos;
(c) usar el contraste contra copia y pegado como prueba principal: pasaría por construcción y dejaría
la métrica sin nada que validar, que es el patrón que #76 ya obligó a cerrar en este proyecto.

**Por qué:** `streak amplitude` es la única de las métricas adoptadas que mide lo que el Objetivo 3
dice generar, y es la que la copia y pegado no puede producir. Si su definición operativa queda
abierta hasta ver los resultados, el criterio de éxito se vuelve elegible a posteriori, que es
exactamente el riesgo que D4 existe para cerrar.

### Lo que esta entrada NO fija todavía, y dónde se fija

Para que esto sea preinscripción completa faltan cuatro parámetros, y **se fijan sobre validación,
nunca sobre test**, en `diseno_A.md` al congelarlo: los **radios** de los arcos anulares dentro de
`B_δ`; el **número y separación de los planos** perpendiculares a `u`; la **apertura angular** del
arco; y el **margen de guarda** alrededor de `M`. Hasta que estén escritos, esta decisión fija el
**qué** y el **contra qué**, no el **con qué parámetros**.

**Dependencia:** el contraste primario y el segundo componente de `Delta` (test-retest) necesitan el
**brazo físico de Peters implementado**, que la autora decidió implementar el 2026-10-05. Implementar
su protocolo **no es validar XCIST**: la reimplementación validada sigue fuera de alcance y lo que se
hace es reproducir un protocolo publicado, documentando revisión de código, configuración y ajustes de
reconstrucción, como `main.tex` ya promete.

---

## 2026-10-05 (4) — Parámetros de las ROIs de `streak amplitude`, fijados sobre validación (completa la entrada 2026-10-05 (3))

**Decisión:** los cuatro parámetros que la entrada `2026-10-05 (3)` dejó abiertos quedan fijados así.
Medido con `experiments/objetivo3/a12_roi_parametros.py` sobre los **631 parches con metal de los 5
pacientes de validación** que los tienen; **ningún paciente de test y ninguna salida del
sintetizador**. Dictada por la autora y registrada por el asistente con instrucción explícita el
2026-10-05.

| # | Parámetro | Valor | Cómo se fijó |
|---|---|---|---|
| 1 | Apertura del arco | **360°, anillo completo** | argumento |
| 2 | Planos | **todos los cortes con `M`, menos 8 mm por extremo** | reutilización |
| 3 | Guarda alrededor de `M` | **un vóxel en plano del propio caso** (mediana en validación: 0.83 mm) | argumento, al mínimo |
| 4 | Radios de los anillos | **de la guarda a 12.0 mm** | se sigue de `B_δ` |

**1. Anillo completo, y así se elimina un parámetro en vez de fijarlo.** Peters et al. colocan las
ROIs *"perpendicular to strong streak artifacts"* y a mano, y su propio texto declara esa colocación
como limitación. Con un estadístico **de colas**, la direccionalidad del streak deja de importar: el
5 % superior y el 5 % inferior encuentran las rayas claras y oscuras dondequiera que estén en el
anillo. Es una desviación del protocolo publicado y se declara como tal.

**2. Los 8 mm por extremo se reutilizan, no se inventan.** Es `RECORTE_EXTREMO_MM = 8.0` de
`e9_corredor.py`, la exclusión de extremos ya decidida para SAP (D-O2.3). Un segundo valor para la
misma idea geométrica crearía una discrepancia gratuita entre el Objetivo 2 y el 3.

**4. El radio exterior no es un grado de libertad.** El sintetizador escribe solo dentro de `G`, así
que el campo de desviación es **cero fuera de `G` por construcción** (E-A3, comprobado en cada
síntesis). El exterior es el ancho de `B_δ`, ya declarado. Buscarlo con una medición habría sido
fabricar un parámetro que el diseño ya fijó.

**3. LA GUARDA NO SE PUDO FIJAR POR MEDICIÓN, y esto hay que leerlo entero.** Se probaron dos
criterios y **los dos fallan, por razones opuestas**:

- **Fracción de vóxeles sobre 2500 HU:** da **cero en todas las cáscaras por construcción**. La
  distancia se mide desde `~metal`, así que las cáscaras excluyen el metal por definición. El
  criterio no podía detectar nada.
- **Elevación de la mediana de HU respecto a fuera de `B_δ`:** solo baja de 25 HU **a los 11 mm**, de
  modo que la guarda se habría comido la banda entera y habría dejado una ROI de 1 mm. Falla porque
  **la elevación no es contaminación: es el artefacto**, que es la señal que la métrica existe para
  medir. El criterio excluía justo lo que hay que medir.

En una imagen real, a esta escala, **el volumen parcial del metal y el artefacto de campo cercano son
la misma señal**, y separarlos exigiría una referencia sin metal del mismo paciente, que es el
problema que la métrica ya tiene. Por eso la guarda se fija **por argumento y al mínimo**: un vóxel en
plano, porque el volumen parcial no puede extenderse menos que eso.

**El argumento decisivo es la dirección del sesgo.** Cualquier guarda mayor descarta señal de
artefacto y sesga `streak amplitude` **a la baja** — la **misma dirección** que la censura por el
suelo de −1000 HU (#141). Ante dos sesgos del mismo signo, el parámetro se elige para no sumar un
tercero.

**Evidencia del perfil radial, que se reporta:** la elevación de la mediana de HU cae de **+2330 HU**
en la cáscara de 0.5–1.0 mm a **+926 HU** en la de 3.0–3.5 mm, y de ahí a los 12 mm decae despacio
hasta **+2 HU**. La caída abrupta se agota hacia los 3–4 mm; ese tramo lento posterior es artefacto y
**no se excluye**.

**Alternativas descartadas:** (a) guarda de 3.5 mm, donde se agota la caída abrupta: descartaría el
campo cercano, que es donde el artefacto es más intenso, y sumaría sesgo a la baja; (b) guarda medida
por umbral de elevación: produce 11 mm y una ROI de 1 mm, absurda; (c) arcos de apertura fija
siguiendo a Peters literalmente: hereda una limitación que ellos declaran y hace irreproducible la
comparación entre brazos.

**Por qué esta entrada existe aparte:** la entrada `2026-10-05 (3)` dijo explícitamente que fijaba el
**qué** y el **contra qué**, no el **con qué parámetros**, y que estos se fijarían sobre validación.
Con esta entrada la preinscripción del endpoint primario del Objetivo 3 queda **completa**, y ya no
hay ningún parámetro del endpoint pendiente de decidir cuando lleguen los resultados.

---

## 2026-10-05 (5) — El brazo físico se reproduce, NO se valida; y lo verificado en su código entra al documento (#8, #146)

**Decisión:** dos partes, las dos dictadas por la autora el 2026-10-05 y registradas por el asistente
con instrucción explícita.

### 1. No se valida XCIST. Se reafirma el límite de #8

**Validar un simulador es compararlo contra mediciones físicas en un fantoma real escaneado en un
tomógrafo real.** La tesis no tiene fantoma con material metálico conocido, ni acceso declarado a un
escáner, ni mediciones de referencia, y conseguirlos no cabe en el alcance. A lo que se suma el
argumento que #8 ya registró: **el propio artículo de XCIST no contiene ningún estudio de artefacto
metálico** y declara su validación como *"first-order"* e *"in progress"*. Reclamar una validación que
el autor del simulador no ha hecho expone la tesis a una pregunta que no puede contestar.

**Lo que sí se hizo, y se nombra distinto: verificación de reproducción.** Se corrió su protocolo en
local, se obtuvo su salida, y se verificó en su código un supuesto que su artículo no declara. Eso es
lo que `main.tex` ya promete —*"document the code revision, configuration, reconstruction settings and
access conditions"*— y es defendible sin mover el alcance.

**Alternativa descartada:** ampliar el alcance a una validación propia. Obligaría a conseguir fantoma
y escáner, y dejaría la tesis dependiente de un recurso que no está asegurado.

### 2. Lo verificado en el código del brazo físico entra al documento como hecho

Son observaciones directas de fuentes primarias —el código, los archivos de licencia y la
documentación del repositorio— y quedan autorizadas a escribirse en `overleaf/` con esta entrada,
con la trazabilidad de #146:

| Hecho verificado | Dónde |
|---|---|
| **Paciente y metal se proyectan JUNTOS**, en una pasada, como un volumen de tres materiales: agua con el paciente (+1), agua con la máscara de metal (**−1**, desplaza el agua) y la aleación con la misma máscara (+1). Es desplazamiento de material **antes** de proyectar, no pegado en el dominio de imagen | `simulation_scripts/run.py` |
| Licencia **BSD 3-Clause**, GE Precision HealthCare 2024 | `LICENSE` de los dos repos |
| Revisión de código: commits **`4cf3544`** (xcist-main) y **`4993e87`** (xcist-example) | `git log` |
| El metal de sus datos de entrenamiento son **formas fractales aleatorias** colocadas en posiciones aleatorias de tejido blando o hueso, no implantes | `data_generation.md` |
| Su geometría es **2D de una sola fila de detector** (900 columnas, 1000 vistas), con dispersión equivalente a 64 filas y reconstrucción FDK con corrección de agua | `data_generation.md` |
| El **filtro de realce de frecuencias** aplicado a las imágenes de paciente antes de simular está confirmado | `data_generation.md` |
| Su script publicado **no corre tal como viene**: aborta al serializar `sim.json` porque un valor es `np.float32`. Reproducirlo exige un parche de una línea, que vive en `experiments/objetivo3/peters/` y **no** en el clon de `repos/` | ejecución del 2026-10-05 |

**Cómo se escribe el primer punto, que es el que más pesa.** `main.tex` dice hoy que *"the paper does
not state whether patient and metal are projected jointly, which this work verifies in the simulator
code before reproduction"*. Esa frase pasa de promesa a hecho: **se verificó, y la respuesta es que sí,
por desplazamiento de agua**. Y refuerza el encuadre del protocolo como híbrido, porque la inserción
ocurre a nivel de material y no de imagen.

**Lo que NO autoriza esta entrada:** afirmar nada sobre el rendimiento del brazo físico, ni sobre la
profundidad de su *undershoot* más allá de la medición de una sola imagen con un objeto de titanio
(ampliación a #141 y #146). Esa cifra sigue siendo de una configuración y no una cota.

**Por qué:** los dos refuerzos del gap —que su metal no es un implante y que su geometría es de una
fila— convierten en concreto y citable lo que el documento afirmaba de forma general. Y la
verificación de la proyección conjunta cierra un pendiente que estaba escrito en el propio
`main.tex`, de modo que dejarlo fuera del documento de entrega sería perder trabajo ya hecho.

---

## 2026-10-05 (6) — Criterio de selección del modelo, conjunto de validación, aplazamiento de B1 y B2, y orden de trabajo (#145, #147, #142, #143)

**Decisión:** seis puntos, adoptados por la autora el 2026-10-05 sobre la recomendación del asistente
y con una corrección que ella aceptó (punto 1). Registrada por él con instrucción explícita.

### 1. El modelo final NO se elige por la pérdida de validación

**Lo que queda establecido por medición y ya no se discute:** la pérdida de validación **no ordena los
modelos por fidelidad en HU**. Comparación pareada sobre los 5 pacientes de validación, mismos cortes
y misma semilla: el checkpoint del mínimo de la pérdida pierde **5 de 5** en error de HU dentro del
metal y **5 de 5** en la banda, y reproduce el 55-67 % del metal real frente al 92-95 % del otro
(#145 y su confirmación). Prueba de signos de una cola, p = 0.031, declarada antes de ver el resultado.

**El criterio pasa a ser una métrica de APARIENCIA medida sobre validación.** Eso es legítimo —para
eso existe validación— y **no toca los pacientes de prueba**.

**CORRECCIÓN IMPORTANTE, aceptada por la autora.** La primera versión de esta recomendación proponía
elegir con la fracción de metal reproducida y el error en HU sobre la tarea de **reconstruir implantes
reales**. Se descartó: esa tarea **premia memorizar**, porque los implantes de validación se parecen a
los de entrenamiento, y elegir así seleccionaría el checkpoint más sobreentrenado por una razón que
**no se traslada** al uso real de la tesis, que es colocar un tornillo donde no había nada.

**El criterio adoptado se mide sobre la tarea de SÍNTESIS:**

> Se coloca el tornillo paramétrico en una pelvis **limpia** de validación, se genera con cada
> checkpoint candidato, y se comparan dos estadísticos del resultado contra los mismos estadísticos
> medidos en los **implantes reales** de los pacientes de validación:
>
> 1. el **perfil radial de HU** alrededor del metal, por cáscaras de distancia; y
> 2. el **histograma de HU dentro de la máscara del implante**.
>
> Gana el checkpoint cuyo artefacto sintético se parezca más al real.

**Por qué estos dos y no la amplitud de rayas.** La amplitud de rayas exige una verdad de terreno sin
metal, y **en un paciente con implante real esa verdad no existe**. El perfil radial y el histograma
**sí se miden sobre la imagen real sin ninguna referencia**, y de hecho ya se midieron
(`a12_roi_parametros.py`). Esto además **cierra un hueco de la decisión `2026-10-05 (3)`**, cuyo
contraste de realismo estaba especificado contra una magnitud que no es calculable en los pacientes
reales.

**Coherencia metodológica:** es la misma lógica del Objetivo 2, que compara **distribuciones** contra
una referencia clínica externa en vez de instancias.

**Cuándo se mide:** después de la prueba de la cadena completa (punto 5). **No espera a Peters.**

### 2. El conjunto de validación son los **3 pacientes de CLINIC-metal**

`dataset7_CLINIC_metal_0011`, `_0039` y `_0056`. Son los que el manifiesto de entrenamiento usa de
verdad (896 parches), y los únicos con implante real. Los dos de `dataset6` que aparecieron en
`a9`, `a12` y `a13` tienen **objeto metálico incidental** y entraron por un descuido del asistente,
que cargó el caché en vez del manifiesto (#147).

**Se declara con ellos el desbalance:** de los 896 parches, **`0011` aporta 538 (60 %)** y el **65 %
del metal**. La validación está dominada por un paciente, y toda cifra medida sobre ese conjunto lo
lleva escrito al lado.

**Consecuencia:** `Delta` se calibra sobre **3** pacientes, no 5. La regla de #141 decía "los 5
pacientes de validación" y queda corregida aquí.

### 3. B1 y B2 quedan APLAZADOS, y se declara por qué

- **B1** (si la saturación con 47 pacientes entra como limitación): su evidencia es la curva de la
  pérdida de validación, que acaba de mostrarse que no ordena los modelos por lo que la tesis mide.
  **Declararlo hoy sería declararlo con el instrumento equivocado.**
- **B2** (los 30 000 pasos): se eligió por el mínimo de esa misma curva. La cifra **sigue en pie** —cae
  en una meseta reproducida— pero **el argumento que la sostiene es más débil**, y la entrada
  `2026-10-05 (2)` queda remitida a esta.

Los dos se reabren en cuanto el criterio del punto 1 esté medido.

### 4. #142 y #143 se DECLARAN, no se rehacen

- **#142** (el eje del corredor se busca en una rejilla de 5°, mientras la tolerancia angular citada es
  de 1.53°): **declarar**. Refinarlo reabriría el Objetivo 2 completo, que está cerrado con una corrida
  preinscrita. El sesgo es además **conservador**: el muestreador aparece peor de lo que sería con un
  eje mejor orientado.
- **#143** (la máscara binaria tiene un sesgo de volumen que depende de la orientación): **declarar**,
  y **medirlo antes sobre las poses perturbadas del muestreador**, que son oblicuas casi siempre. El
  7.27 % del caso malo corresponde a un eje alineado con la rejilla y **puede ser raro en la práctica**.
  Ninguna cifra entra al documento antes de esa medición.

### 5. Orden de trabajo: la cadena completa ANTES que Peters

1. **Ejecutar la cadena completa sobre una pelvis limpia de validación.** Nunca se ha hecho. Es el
   único experimento que puede invalidar el Objetivo 3 entero, y es barato. Se corre con **los dos
   checkpoints candidatos**, pareado, para que sirva también al punto 1.
2. **Sonda de viabilidad de Peters, no la implementación completa.** Su protocolo es **bidimensional y
   de una sola fila de detector**, y el tornillo de esta tesis mide 138 mm en el eje axial. Si esa
   extensión resulta inviable, **el contraste primario se queda sin brazo** y D4 hay que replantearlo.
   Eso se descubre con un corte, no con tres semanas de ingeniería.
3. Recién después: Peters completo, `Delta`, congelar `diseno_A.md`, corrida final.

**Por qué no empezar por Peters:** es lo más caro en tiempo, es ingeniería y no investigación, y **su
valor depende por completo de que el sintetizador produzca algo usable**. Si la cadena falla sobre una
pelvis limpia, el brazo de comparación no tiene con qué compararse.

### 6. Lo que esta entrada NO decide

El criterio del punto 1 fija **qué se mide y contra qué**. Los detalles de la comparación —ancho de
las cáscaras del perfil radial, número de cortes, cómo se resume la distancia entre distribuciones—
se fijan **sobre validación** antes de medir, igual que se hizo con los parámetros de las ROIs en la
entrada `2026-10-05 (4)`. Hasta entonces, **ningún checkpoint está elegido**.

## 2026-10-07 — Lectura de HU del Objetivo 3: `regla_suave` (v2) con `delta = 0.05` (#152)

> Escrita por el asistente con autorizacion explicita de la autora en el chat del 2026-10-07, que
> acepto el texto propuesto. Excepcion puntual a la regla 3 de `CLAUDE.md`.

El Objetivo 3 lee los HU con la `regla_suave` (v2): mezcla suave con LW como ancla, `delta = 0.05`,
fijado en `a16` sobre validación (5 pacientes, 2 checkpoints) con un criterio registrado antes del
resultado (#152, adendas 4 y 5). La `regla` v1 sigue siendo la del Objetivo 1, cuyas cifras y texto
no cambian. Con `delta = EPS`, la v2 es idéntica a la v1.

## 2026-10-07 (2) — Definición común de los estadísticos del criterio de selección de checkpoint (#150)

> Escrita por el asistente con autorización explícita de la autora en el chat del 2026-10-07, que
> aprobó la propuesta. Excepción puntual a la regla 3 de `CLAUDE.md`.

Detalla la decisión `2026-10-05 (6)`, punto 6 ("lo que esta entrada NO decide").

- **Perfil radial:** distancia 2D en el plano del corte, cáscaras de 0.5 mm de 0 a 12 mm, anillo
  completo. En cada cáscara, la **mediana y el p95** de HU, expresados como **elevación** respecto a la
  mediana del anillo de 12–15 mm del mismo paciente. Agregación por corte -> por paciente -> entre
  pacientes.
- **Histograma dentro de `M`:** p50, p75 y p95 de HU sobre los vóxeles > 2500 HU, por paciente. La
  fracción sintética > 2500 se reporta como **control**, no se compara con lo real (cuya máscara se
  define con ese umbral, `a1b_parches_componente.py:100`).
- **Referencia real:** los 3 pacientes de validación con implante; se excluyen los 2 con objeto
  incidental (#147).
- **Lectura sintética:** `regla_suave` con `delta = 0.05` (entrada 2026-10-07).
- **Regla de decisión:** gana el checkpoint con más cáscaras dentro de la envolvente real (mínimo a
  máximo de los 3 pacientes) en las dos curvas; desempata la distancia a la mediana real en p50 y p95
  dentro de `M`; un empate persistente lo decide la autora.
- **Alcance:** con n = 3 el cotejo **descarta**, no prueba.
- **Condición previa, PENDIENTE:** verificar el tipo de implante de los 3 pacientes de referencia con
  el agente `clasificador-metal` (propuesta preliminar) antes de cotejar. Si no son tornillos, el
  cotejo se revisa.

---

## 2026-10-08 — Decisiones pendientes delegadas al asistente en rol de asesor (cierre de las marcas GAPDEC de diseno y redaccion)

**Delegacion** (de la autora, chat del 2026-10-08): *"Sobre las decisiones mias pendientes, evalua en la
posicion de un experto en tesis IA con aplicaciones medicas la mejor opcion y mas respaldable en la tesis
actual, y toma las decisiones mas recomendables."* Mismo procedimiento que la entrada 2026-09-17. Escrita por el
asistente; **la autora puede revertir cualquier punto**. Criterio aplicado en todas: preferir lo que ya esta
medido o preinscrito, no elegir nada mirando resultados de test, y declarar como convencion lo que no tiene
fuente en vez de buscarle una.

**Lo que NO se decide aqui, y por que:** (i) **#90**, si el brazo TOST pasa a trabajo futuro por plazo: depende
del plazo real, que solo conoce la autora; (ii) el **tipo de implante** de `metal_0011/0039/0056`, la
**constancia de la revision multiplanar**, el **desenlace de la regla del suelo** y el **margen `Delta`**: son
datos, no decisiones; (iii) el texto de `tesis/main.tex` (regla 4): estas decisiones se aplican a `overleaf/` y a
`docs/`, y `main.tex` queda pendiente de una orden explicita.

### A. Sintetizador (Objetivo 3)

1. **Codificacion y precision: `pub+asinh` en float32.** Es la de todas las corridas (`run01`, `run02`), la
   primera del orden a priori de #76, y su ida y vuelta sin modelo es 0.00 HU en hueso (`p1_compuerta.md`,
   columna identidad). Cambiarla exigiria recachear y reentrenar sin evidencia de mejora. Alternativa
   descartada: `LW20000` (identica en hueso; no aporta nada y rompe la continuidad con lo entrenado).
2. **Entrada 2.5D: 3 cortes axiales contiguos.** Es lo entrenado; un modelo 3D no cabe en datos ni en computo.
3. **Arquitectura congelada tal como corrio:** U-Net `base = 64`, multiplicadores (1, 2, 4, 8), atencion en la
   resolucion mas baja, prediccion `v`, planificador coseno de 1000 pasos, AdamW lr 1e-4, lote 4, parche 256
   (`src/renderizador/`). Se declara que **no** se hizo busqueda de arquitectura.
4. **Muestreo: DDIM determinista (eta = 0), 50 pasos; 5 semillas por caso** para medir la variabilidad que
   entra en `Delta`. 5 es una convencion declarada (coste bajo: la generacion por paciente es de minutos).
5. **Procedimiento de muestreo frente a RePaint y LeFusion:** se describe lo implementado y se dice que **no es
   ninguno de los dos**: condicionamiento por concatenacion del contexto conocido y de `M`, `G`; perdida solo en
   `G`; composicion exacta fuera de `G`; sin remuestreo de la region conocida (#117).
6. **Desplazamiento de dominio de la mascara (umbral frente a cilindro): se cuantifica con lo ya medido**, sin
   metrica nueva: fragmentacion de tornillos a 2500 HU (E8, 9 de 57) y diametro de cuerpo (E11, mediana 4.91 mm).
7. **Continuidad en el borde de `B_delta`: se mide con `a10_costura.py`** (salto de HU al cruzar el borde de
   `G`), en E-A2, para los dos brazos, **descriptiva y sin umbral**.
8. **Insercion por copia y pegado:** `M` recibe un valor **constante** de HU igual a la mediana de los voxeles
   > 2500 HU dentro de las mascaras de los implantes reales de **entrenamiento** (nunca test); fuera de `M`, el
   CT intacto. El valor se mide una vez y se reporta (dato pendiente).
9. **Evaluacion del Objetivo 3 solo con metricas**, mas el QC visual de la autora (E-A4) declarado como control
   y no como evaluacion. No hay lector clinico disponible; inventarlo seria peor que declararlo.
10. **`bone integrity` y `metal integrity` en sintesis: no se invierte la formula, se invierte la lectura.** Se
    calculan como en Peters et al., en E-A2, contra la TC limpia del mismo paciente y en las mismas regiones que
    la `streak amplitude`, para los dos brazos. Un valor alejado del ideal **no** es "peor": la referencia de
    lectura es el valor del brazo fisico. Siguen siendo **descriptivas** (D4).
11. **Contraste de realismo (resuelve el hueco que dejo 2026-10-05 (3)):** la `streak amplitude` no es
    calculable en implantes reales, asi que el realismo se mide con los **estadisticos sin referencia de la
    decision 2026-10-07 (2)** —perfil radial (mediana y p95 como elevacion) e histograma dentro de `M`—, de lo
    sintetizado en E-A2 frente a los implantes reales de E-A1, resumido como **fraccion de cascaras dentro de la
    envolvente real**. Descriptivo, sin prueba de hipotesis.
12. **Regla del suelo de -1000 HU:** se evalua contra el **contraste primario** (su umbral es `Delta`, el margen
    del TOST). El sesgo en el contraste de realismo se declara de forma cualitativa.
13. **Subconjunto del brazo fisico: los 14 pacientes de E-A2.** El TOST es pareado y necesita los 14; a ~70 s por
    corte (#146) cabe en CPU local. **Test-retest del brazo fisico:** dos corridas identicas salvo la semilla del
    ruido del simulador.

### B. Muestreador y SAP (Objetivos 2 y 4)

14. **Fraccion por zona de densidad: SE RETIRA de SAP.** Su unica fuente (E9b) quedo retirada como evidencia de
    densidad por #50, y D-O2.6 ya la dejaba fuera del muestreo. SAP queda con **dos** componentes: grado de
    brecha (comparado) y viabilidad del corredor (descriptiva). Donde el texto diga *"density-based placement
    sampler"* debe decir que el muestreador se restringe por el **corredor oseo medido**; la densidad pasa a
    motivacion y a trabajo futuro.
15. **Dimension angular de Smith et al.: no entra.** La referencia clinica (Zwingmann et al.) gradua solo
    perforacion, y la escala angular de Smith tiene un grado 1 no definido en el texto (#11). SAP declara que usa
    solo la dimension de perforacion.
16. **Calibre de viabilidad: 7.0 mm con holgura c = 1 mm** (`D_TS_max >= 9 mm`), el mismo calibre de la brecha
    (D-O2.4) y dentro del nominal 6.5-8.0 mm; 4.91 y 7.3 mm, sensibilidad. Es lo que reporta E13.
17. **Wasserstein-1 sin regla de fallo**, porque fijarla ahora seria post hoc. Se da una **escala de lectura**,
    declarada post hoc: la distancia entre los dos brazos clinicos de Zwingmann et al., calculada de sus cifras
    publicadas (69/15/8/8 frente a 40/37/11.5/11.5 %), es **0.395 grados**; el muestreador queda a 0.206 del
    brazo navegado.
18. **Intervalo por remuestreo de pacientes para W1: SI**, como analisis no preinscrito y descriptivo (dato
    pendiente; CPU).
19. **Convencion h = 2 sigma:** se justifica por su consecuencia, no por una fuente: con perturbacion
    semi-normal, ~95 % de las magnitudes quedan dentro de la holgura de 5 mm de Kaiser et al. Sigue siendo
    convencion y asi se declara.
20. **Exclusion de 8 mm por extremo:** convencion heredada del codigo del corredor y reutilizada en SAP y en las
    ROIs para no tener dos valores de la misma idea. Sin fuente; se declara.
21. **Umbral de 10 mm y holgura de Kaiser para el corredor transiliaco-transsacro: SI aplican, como
    convencion.** McLaren et al. aplican ese mismo criterio a corredores transiliosacros, y su justificacion es
    dimensional (holgura alrededor del diametro), no dependiente del tipo de trayectoria.
22. **Los dos casos con error de segmentacion (`CLINIC_0022`, `CLINIC_0024`): se mantienen** en la cohorte
    preinscrita (excluirlos despues de verlos seria seleccion post hoc) y se anade una sensibilidad sin ellos
    (dato pendiente).
23. **Objetivo 4:** se declara **objetivo de definicion**, verificado por los controles de implementacion
    (identidad, monotonia, resolucion) y ejercido en el Objetivo 2; no se evalua experimentalmente por separado,
    y la adopcion de las metricas de Peters et al. no se presenta como contribucion evaluada.

### C. Encuadre del documento

24. **Pregunta de investigacion:** se alinea con la de `tesis/main.tex` (sin segmentacion; comparacion contra
    copia y pegado y contra Peters) y con los cuatro objetivos. Se mantiene el orden actual de la introduccion.
25. **Por que un sintetizador aprendido si hay simulacion fisica:** el protocolo fisico necesita simular
    proyecciones por pose, es 2D de una sola fila de detector y su metal son formas fractales; el sintetizador
    opera sobre cualquier TC sin proyecciones. **Si alcanza la equivalencia con la fisica es exactamente lo que
    pone a prueba el Objetivo 3**: se presenta como pregunta de la tesis, no como premisa.
26. **Coherencia antes que utilidad:** medir la utilidad para segmentacion de ejemplos cuya plausibilidad fisica
    no se conoce confundiria las dos cosas; y la cohorte anotada no alcanza (punto 1 de Fuera de alcance).
27. **Restriccion al tornillo transiliaco-transsacro:** es el unico implante con corredor oseo medible por
    volumen y con distribucion clinica publicada de grados de brecha; placas y otros tornillos no tienen ninguna
    de las dos.
28. **Ablaciones fuera de alcance:** se enuncian como las de los componentes del muestreador vigente (anclaje al
    eje del corredor, escala de la perturbacion), no como restricciones de densidad.
29. **Revision de literatura:** se declara **narrativa y dirigida**, con busquedas fechadas y snowballing, no
    sistematica. No se inventa un protocolo que no se siguio.
30. **Novedad:** se estrecha a la combinacion objeto metalico rigido + codificacion multiventana + banda
    `B_delta` + copia exacta fuera de `G` (#56).
31. **Zwingmann et al. 2010: fuera de la referencia clinica** (grado 4 sin definir, posible solapamiento con
    2009, #113), citada solo de forma descriptiva.
32. **Cifras de Jacob et al.: no se citan** (la ficha registra cifras discrepantes); se describe el trabajo sin
    numeros.

## 2026-10-08 (2) — Referencia del cotejo de checkpoint: solo los tornillos aislados de `metal_0039` (#154, opcion 1)

Escrito por el asistente por orden explicita de la autora ("Aplica la opcion 1 usando solo 0039"), despues
de revisar los 65 pacientes con material ortopedico (`experiments/exploration-3d/tornillos_candidatos.md`).

- **Referencia real del cotejo** (2026-10-07 (2)): solo los **2 tornillos intraoseos aislados de `metal_0039`**
  (comp `e8` 1, IS, L 76.9 mm, d 4.93 mm; comp `e8` 2, pubis -> acetabulo, L 97.1 mm, d 5.76 mm). Salen
  `metal_0011` (fijador externo) y `metal_0056` (placas con tornillos).
- **No se usan tornillos de train ni de test** como referencia: se mantiene la separacion de particiones.
- **Envolvente real:** minimo a maximo de esos 2 componentes en cada cascara; el resto de la regla (desempate
  por p50/p95 dentro de `M`, empate persistente lo decide la autora) no cambia.
- **Alcance:** 1 paciente y 2 tornillos. El cotejo sigue descartando, no probando; con n = 1 paciente la
  envolvente es mas estrecha y puede descartar checkpoints que solo difieren de ese paciente.
- **Condicion previa:** la autora valida en cortes que los 2 elementos de `0039` son tornillos aislados.

## 2026-10-08 (3) — Cotejo de checkpoint: 5 semillas por checkpoint y paciente

Escrito por el asistente por orden explicita de la autora ("usa 5 semillas").

- **5 semillas DDIM** (0-4) por checkpoint (`run01_140k`, `mejor_37k`) y por pelvis limpia de validacion
  (`0101`, `0102`), todo en GPU (#151), lectura v2. Igual que el punto 4 de la entrada 2026-10-08.
- **Detalle de implementacion propuesto por el asistente, a confirmar por la autora:** agregacion corte ->
  semilla -> paciente -> checkpoint por medianas; la regla suma las cascaras dentro de la envolvente en las
  dos curvas (p50 y p95); solo cuentan las cascaras con valor en lo real y en lo sintetico (con cascaras de
  0.5 mm y pixel de 0.7-1 mm algunas quedan vacias). Codigo: `src/common/cotejo.py`, `a15 --semillas`,
  `a17_cotejo.py`.

## 2026-10-09 — Checkpoint del Objetivo 3: `mejor_37k`, con cascaras de 1 mm en el cotejo (#157, opcion a)

Escrito por el asistente por orden explicita de la autora ("Elige (a) y redacta en 01-decisiones lo elegido").

1. **Agregacion del cotejo confirmada por la autora** (pendiente en 2026-10-08 (3)): corte -> semilla ->
   paciente -> checkpoint por medianas; se suman las cascaras dentro de la envolvente en las dos curvas
   (p50 y p95); solo cuentan las cascaras con valor en lo real y en lo sintetico.
2. **Ancho de cascara del perfil radial: 1 mm** (antes 0.5 mm). Razon: una cascara mas fina que el pixel
   (0.896 mm en los receptores, 0.976 mm en `metal_0039`) produce una alternancia par/impar en el perfil
   sintetico. Esa alternancia se observo a 0.5 mm y desaparece a 1 mm. **Es un cambio POSTERIOR a ver el
   resultado y asi se declara:** con 0.5 mm la regla daba `run01_140k` (8 frente a 7 de 46 cascaras); con
   1 mm da `mejor_37k` (11 frente a 5 de 24). Se reportan los dos.
3. **Checkpoint elegido: `mejor_37k`** (`$DATA/a7/run02/mejor.pt`). Con 1 mm, su mediana sigue la envolvente
   real en 9 de 12 cascaras. En contra, y se declara: varia mas entre semillas (324 HU frente a 162).
4. **Se declara como hallazgo, no se corrige:** con cualquier ancho de cascara y en los dos checkpoints, el
   p95 sintetico queda bajo la envolvente real en 10-11 de 12 cascaras (unos 150-200 HU mas alla de 3 mm),
   y el p95 dentro de `M` queda unos 900 HU bajo lo real. Lo sintetico subestima la cola alta del artefacto
   y el pico del metal.
5. **Alcance sin cambios:** 1 paciente de referencia y 2 tornillos; 2 receptores limpios (`0101`, `0102`).
   El cotejo descarta, no prueba.
6. **Reproducibilidad verificada:** misma GPU (MIG `a100_3g.20gb`) y mismas semillas dan resultados
   identicos (jobs 55130 y 55171).
7. **Evidencia:** `experiments/objetivo3/a17_cotejo_resultado.md`; codigo `src/common/cotejo.py`,
   `a15 --pasos-cotejo-mm`, `a17 --paso-mm`.
8. **Reabre B1 y B2** (2026-10-05 (6), punto 3: "se reabren en cuanto el criterio del punto 1 este medido").
   No se deciden aqui.

## 2026-10-09 (2) — Delegadas: sonda de Peters preinscrita, B2 cerrada, B1 declarada

Escrito por el asistente por orden explicita de la autora ("Evalua la mejor decision a realizar para estos
pendientes, y realiza las redacciones pertinentes"). Son decisiones tomadas por delegacion: la autora las
revisa.

1. **Sonda de viabilidad de Peters: protocolo y criterios fijados antes de correr**
   (`experiments/objetivo3/sonda_peters.md`).
   - Un corte de `0101` con el tornillo de `a15`.
   - Material principal: acero inoxidable, por la Tabla 2 de Peters (implantes espinales de 2.5-10 mm).
     Titanio solo como sensibilidad.
   - Criterios:
     - V1: corre sin truncamiento y el brazo completo cuesta 72 h o menos.
     - V2: sin metal, sesgo de +/-20 HU o menos frente al original.
     - V3: el artefacto es al menos 3 veces el ruido test-retest.
   - **Salida fijada ahora:** si fallan V2, V3 o el truncamiento, el TOST contra Peters baja a secundario
     descriptivo y el realismo frente a CLINIC-metal pasa a primario. Si solo falla el coste, se submuestrean
     los cortes y se declara.
   - La sonda no compara amplitudes con el difusor: eso seria mirar el contraste primario.
2. **B2 (30 000 pasos) se CIERRA sin reentrenar.**
   - El modelo de la tesis es `mejor_37k` (2026-10-09). La cifra de 30 000 pasos deja de describir el modelo
     usado y se reemplaza por: "checkpoint elegido por cotejo de apariencia entre dos candidatos (paso ~37 000,
     minimo de la perdida de validacion de `run02`, y paso 140 000 de `run01`)".
   - Se declara que solo se evaluaron dos candidatos. No se afirma que ~37 000 sea optimo.
   - Que el cotejo prefiera el candidato cercano al minimo de validacion es coherente con la meseta de B2,
     no lo prueba.
3. **B1 (saturacion con 47 pacientes) se DECLARA como limitacion, sin afirmar saturacion.**
   - No se midio el efecto de anadir pacientes.
   - Lo unico medido es que **4 veces mas pasos** (140 000 frente a ~37 000) no mejoraron el cotejo a 1 mm
     (5 frente a 11 de 24 cascaras).
   - Eso habla de la duracion del entrenamiento, no del tamano de la cohorte, y se escribe asi.
4. **El sesgo del p95 (#157) se declara y NO bloquea** la sonda ni Peters.
   - Hipotesis de mecanismo, sin verificar: que el modelo aprenda mal la cola alta cerca de los techos de los
     canales estrechos (#152).
   - Si la autora quiere verificarlo, es un diagnostico aparte y no cambia el orden de trabajo.

## 2026-10-09 (3) — Brazo fisico: Fe preinscrito + Ti como sensibilidad (#159, opcion 2)

Escrito por el asistente por orden explicita de la autora ("Pega tu la decision en 01-decisiones"). La opcion la
eligio la autora ("Me quedo con tu recomendacion 2").

1. **El brazo completo de Peters corre con `Fe` y con `Ti`.**
   - `Fe` es el material preinscrito: sustituye al acero, que no esta en el catalogo de XCIST.
   - `Ti` es la sensibilidad.
   - Los dos llevan test-retest A/B, y la geometria y la `M` son identicas a las del difusor.
2. **Cortes:** uno de cada `k = 2` entre los cortes axiales que toca `G`. Es la salida preinscrita de la sonda
   (`sonda_peters.md`) para el fallo solo por coste.
3. **Particiones:** el brazo corre primero solo en validacion (`0101`, `0102`) para medir `Delta`. Test entra
   solo en la corrida final, despues de congelar `diseno_A.md` (`--corrida-final`).
4. **Se declara como limitacion del brazo fisico:**
   - El metal simulado es mucho mas brillante que el real de CLINIC-metal (mediana en `M`: Fe ~9900 HU,
     Ti ~5400 HU, frente a 3100-3800 HU en `metal_0039`). No se sabe si viene del material, de la
     reconstruccion o del escaner.
   - El TOST compara el difusor con una referencia que puede estar desplazada respecto de lo real, y en sentido
     contrario al sesgo del difusor (#157).
5. **Pendiente del equipo:** mejorar la subexposicion del difusor (p95 bajo lo real, #157). No esta programado y no
   bloquea `Delta`.
6. **Codigo:** `experiments/objetivo3/a19_peters_completo.py` y `a19_peters.sbatch` (CPU, sin GPU).

## 2026-10-09 (4) — E-A2 con cortes de solo banda (#160) y formula de `Delta` (D4)

Escrito por el asistente por orden explicita de la autora ("Escribe sobre 01-decisiones.md"). Las dos decisiones
son de la autora ("Usa --incluir-banda y Delta = max(s, r)").

1. **El difusor genera todos los cortes axiales que toca `G`** (`a15 --incluir-banda`).
   - Antes solo generaba los cortes con `M`, y la mitad de las ROIs de E-A2 caia en cortes no generados, con
     desviacion cero por construccion: en `0101`, 51 cortes con ROI frente a 25 generados.
   - Es lo que describe el diseno: el modelo genera dentro de `G` y entreno con parches de solo banda.
   - Por omision `a15` sigue sin la opcion, para reproducir lo ya corrido. El cotejo (`a17`) no cambia, porque
     solo mide cortes con `M`.
2. **`Delta = max(s, r)`**, fijada antes de ver ningun numero:
   - `s` = rango (maximo menos minimo) de la `streak amplitude` del difusor (`mejor_37k`) entre sus 5 semillas
     DDIM;
   - `r` = |`streak amplitude` Fe_A - Fe_B| del brazo fisico (test-retest);
   - cada uno por paciente y promediado sobre los receptores de validacion (`0101`, `0102`).
   - Se mide con el evaluador comun `a20_evaluador_ea2.py` (`peters`, `difusor`, `delta`).
3. **Se declara:** si `s > r`, el margen lo fija la variabilidad del propio difusor. Un `Delta` mayor facilita
   concluir equivalencia en el TOST.
4. **Alcance:** 2 pacientes de validacion. El diseno hablaba de "los 5 pacientes de validacion", pero solo `0101`
   y `0102` tienen receptor limpio con corredor viable (`0019` no cabe: corredor de 1.6 mm).

## 2026-10-09 (5) — Regla para elegir el material del brazo fisico: el que mas se parezca a los tornillos REALES (#161)

Escrito por el asistente por orden explicita de la autora ("Si, escribe la regla y corre el cotejo de Peters").
**Se escribe y se sube ANTES de correr el cotejo.**

**Contexto que se declara.** El material primario (Fe, 2026-10-09 (3)) se habia elegido por una analogia de
tamano (Peters, Tabla 2). Despues se vio en validacion que el difusor queda mucho mas cerca del brazo con Ti
que del brazo con Fe (#161). Cambiar el material **porque favorece al difusor** convertiria el TOST en una
eleccion de referencia. Por eso el criterio que sigue **no usa el difusor en ningun paso**: compara el brazo
fisico con los tornillos reales. El cambio es posterior a ver la comparacion en validacion, y asi se declarara
en la tesis.

1. **Pregunta:** que material, Fe o Ti, hace que el brazo fisico de Peters reproduzca mejor los tornillos reales
   de CLINIC-metal.
2. **Datos:**
   - simulaciones `a19` de `0101` y `0102`, las dos replicas A y B, en los cortes simulados que contienen `M`;
   - referencia real: los 2 tornillos aislados de `metal_0039` (2026-10-08 (2)).
3. **Estadisticos:** los del cotejo de checkpoint (`src/common/cotejo.py`, 2026-10-07 (2)), con cascaras de **1 mm**
   (2026-10-09):
   - perfil radial 2D por corte: elevacion de la mediana y del p95 sobre el anillo de 12-15 mm, de 0 a 12 mm;
   - histograma dentro de `M`: p50, p75 y p95 de los voxeles > 2500 HU.
4. **Agregacion:** corte -> replica -> paciente -> material, por medianas. Es la misma estructura que el cotejo de
   checkpoint, con las replicas A y B en el lugar de las semillas.
5. **Regla:** igual a la del checkpoint.
   - Gana el material con mas cascaras dentro de la envolvente real (minimo a maximo de los 2 tornillos), sumando
     las curvas p50 y p95.
   - Desempate: menor |p50 - mediana real| + |p95 - mediana real| dentro de `M`.
   - Empate persistente: lo decide la autora.
6. **Consecuencia fijada ahora:** el material ganador pasa a ser el **primario** del TOST; el otro queda como
   sensibilidad. Se reportan los dos.
7. **Se declara:** con 1 paciente de referencia el cotejo descarta, no prueba. El material real de los tornillos
   de CLINIC es desconocido (el dataset no lo registra). La literatura ficheada muestra los dos materiales en uso
   clinico: Ti en Acumed y DoubleMedical; acero en Berk 2023; los dos en Synthes.
- **Resultado (`a21_cotejo_material.py`, despues del commit f9d27cc):**
  - **gana `Ti`**: 7 de 24 cascaras dentro de la envolvente real, frente a 0 de 24 con `Fe` (Fe queda sobre lo
    real en las 24);
  - distancia de histograma: 3986 HU con Ti, 14 005 HU con Fe;
  - **por la regla, `Ti` pasa a ser el material primario del TOST y `Fe` la sensibilidad.**
  - Reemplaza el punto 1 de 2026-10-09 (3) en lo que toca al material primario.
  - Los dos materiales exageran el artefacto respecto de los tornillos reales. Se declara como limitacion del brazo
    fisico.

## 2026-10-09 (6) — `diseno_A.md` CONGELADO (#161, opciones 1 + 3; #155 (2))

Escrito por el asistente por orden explicita de la autora ("Congela el diseno con la opcion 1 + 3"). La referencia
de realismo la eligio la autora en el chat ("Solo tornillos aislados").

1. **`experiments/objetivo3/diseno_A.md` queda CONGELADO**, seccion 0, antes de tocar ningun paciente de test.
   - Se declara que el modelo se entreno antes de congelar.
   - Lo que se congela es la corrida final y su evaluacion.
2. **#161, opcion 1:** sin trabajar antes la subexposicion del difusor.
   - Primario: TOST pareado difusor frente a Peters **Ti**, IC90 con *t*, n = 14, margen **+/-188.7 HU**.
   - Sensibilidad: el mismo TOST frente a Fe.
   - Cordura: Wilcoxon de una cola frente a copia y pegado.
   - Valor por paciente: mediana de las 5 semillas (difusor) y de las replicas A y B (fisico).
3. **#161, opcion 3, y #155 (2):** contraste de realismo descriptivo frente a los **tornillos aislados reales de
   test** (`0009`, `0024`, `0048`, `0049`, `0066`), con los estadisticos sin referencia de 1 mm. No depende del
   material del brazo fisico.
4. **Mejorar la subexposicion** (#157) queda como trabajo del equipo **posterior y declarado**. No entra en la
   corrida final congelada.
5. Ningun script toca test sin `--corrida-final`.

## 2026-10-09 (7) — Aclaracion del congelamiento: la referencia de realismo se define por REGLA, no por lista (#155 (2))

Escrito por el asistente por orden explicita de la autora ("Si, escribe la regla"). Se escribe **antes** de que la
autora termine su revision en cortes de los pacientes de test, y **antes** de cualquier resultado de sintesis en
test. Sustituye a la lista del punto 3 de 2026-10-09 (6).

**Motivo.** La lista congelada (`0009`, `0024`, `0048`, `0049`, `0066`) venia de la propuesta sin validar del
agente (`tornillos_candidatos.md`).
- La autora solo habia revisado 3 de los 11 pacientes de test con material, y en uno de ellos (`0006`) encontro un
  tornillo aislado que el agente no vio.
- La lista dejaba fuera los tornillos aislados que no son IS, aunque el cotejo de checkpoint uso los dos tornillos
  de `metal_0039`, uno de pubis a acetabulo.

**Regla:**
1. **Entra** en la referencia de realismo cada paciente de test con al menos un tornillo intraoseo aislado (IS, TS u
   otro), segun la **columna `autora`** de `experiments/exploration-3d/tornillos_conteo.csv`: preguntas `2_n_IS`,
   `3_n_TS` o `4_n_otros_aislados` con un entero >= 1.
2. **Queda fuera, y se declara**, el paciente con `incierto` en esas preguntas y ningun entero >= 1.
3. **Referencia:** solo los componentes tornillo aislado de esos pacientes; el metal de placas o fijadores del mismo
   paciente se excluye de las cascaras.
4. **Reporte:** fraccion de cascaras dentro de la envolvente real, mas el desglose descriptivo por tipo (IS/TS
   frente a otros).
5. **Condicion previa:** la autora completa su columna para los 11 pacientes de test con material antes de calcular
   el realismo. Hoy faltan 8: `0023`, `0024`, `0031`, `0032`, `0048`, `0049`, `0066` y `0072`.
6. La corrida final de E-A2 (`a15` y `a19` sobre los 14 sin metal) no depende de esta lista y puede avanzar en
   paralelo.

## 2026-10-09 (8) — Enmiendas del congelamiento antes de correr: E-A1, n = 13 y corredores angostos

Escrito por el asistente por orden explicita de la autora ("Si, agrega E-A1 y prepara la corrida final"). Las dos
decisiones sobre pacientes las tomo la autora en el chat ("Excluir y declarar", "Entran, declarado"). **Todo se
fija antes de correr nada en test.**

1. **E-A1 entra en la seccion 0 de `diseno_A.md`.**
   - Faltaba por omision del asistente al congelar.
   - Abarca los 19 de test con metal, reportados como 11 ortopedicos y 8 con objetos.
   - Unidad: el componente. Medidas: discrepancia MAE en `G`, `M` y `B_delta`, mas `bone integrity` y `metal
     integrity` adaptadas, mas la costura. Sin `streak amplitude`.
2. **Metricas de Peters adaptadas:** se reportan SDC y cambio de volumen (hueso > 150 HU fuera de `M`; metal
   > 2500 HU), no la escala 0-4, que se calibra con NMAR. Es la adaptacion que pedia #16.
3. **E-A2 con n = 13:** se excluye `dataset6_CLINIC_0034_data` porque no tiene eje del corredor (pixel de 1.62 mm).
4. **Corredores mas angostos que el tornillo** (`0016`, `0047`, `0022`): entran, declarados. La sensibilidad sin
   ellos tiene n = 10.
5. **HU de la copia y pegado: 5373 HU** (`a22_hu_copiapega.py`).
   - Es la mediana de 1 978 270 voxeles de metal en los 17 149 parches de entrenamiento (47 casos, criterio R2),
     en el corte central y en la mascara del componente.
   - Ningun paciente de validacion ni de test interviene.
6. **Errata y tope de E-A1, corregidos antes de correr:**
   - El punto 1 decia "componentes >= 500 mm3, igual que en el entrenamiento", pero el entrenamiento (`a1b`)
     admitia >= 10 mm3.
   - Se mantiene **500 mm3**, el umbral de la referencia del cotejo (`a17`): deja fuera fragmentos que son sobre
     todo islas de artefacto.
   - Se fija un tope de **24 cortes por componente**, repartidos uniformemente; sin el, el coste supera 15 h de GPU.
7. **Scripts de la corrida final:**
   - `a23_ea1.py` (E-A1) y `a23_final.sbatch`;
   - `a24_contrastes.py`: TOST con *t*, sensibilidades Fe y n = 10, Wilcoxon de cordura;
   - `a20` con `bone integrity` y `metal integrity` adaptadas, y la via de copia y pegado.
