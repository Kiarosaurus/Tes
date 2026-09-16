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
