# Indice de literatura

Fuente unica de verdad sobre la bibliografia. Una fila por entrada de refs.bib.

**Criterio de nivel (autora, 2026-09-06):** riesgo de afectar el argumento central
o el benchmark principal.
- **Nivel 1** — critico. Si me equivoco aqui, se cae una tesis o el benchmark.
- **Nivel 2** — afecta la redaccion. Related Work, encuadre, justificacion.
- **Nivel 3** — apoyo. No amenaza nada; se cita, no se discute.
- **Nivel 4** — descartado del uso actual. No queda un rol útil en la tesis;
  documentar si falta el aporte necesario o si está fuera de alcance. No es una
  evaluación de calidad del paper y no elimina su entrada de refs.bib.

**Descarte (autorización de la autora, 2026-09-06):** se registra como estado
separado del nivel de riesgo, para no confundir relevancia con suficiencia.
- **DESCARTADO PARA UN ROL:** relacionado, pero no aporta lo necesario para el uso
  propuesto; indicar rol y carencia verificable. Puede conservar otro rol y su nivel.
- **FUERA DE ALCANCE:** no aporta a los componentes, evaluación ni contexto de esta
  tesis; indicar motivo verificable. No equivale a un paper de mala calidad.
La falta de PDF es un estado de acceso, nunca motivo de descarte por contenido.
Un descarte para un rol conserva N1–N3 si el paper tiene otro uso vigente. N4 se
reserva al descarte del uso completo. No se eliminan entradas de refs.bib.
Actualización 2026-09-07: ningún paper pasa a N4; adoptar Peters no vuelve
irrelevantes las fuentes del simulador.

**Acceso:** COMPLETO (PDF entero) | PARCIAL | ABSTRACT | SIN ACCESO
**PDF:** si = archivo presente en `papers/` | FALTA = no esta

**35 entradas en `refs.bib`**, tras incorporar `vandenbosch2002` desde su raw
(2026-09-08). Van den Bosch: N1, texto completo; Moed: N2 confirmado tras auditar
la comparativa original. Las secciones posteriores conservan el historial de lecturas.

> Estado vigente de Gardner: LEIDO, N1. La busqueda del origen del 10 mm esta
> cerrada por decision; los pasajes posteriores sobre candidatas vivas son historicos.
> #27 excluye fenotipos; Gardner conserva su aporte anatomico S1/S2.

## Nivel 1 — critico

| Clave | PDF | Acceso | Nota generada | Leido por mi | Que amenaza si me equivoco |
|---|---|---|---|---|---|
| vandenbosch2002 (leido 2026-09-08, N1) | si | COMPLETO | vandenbosch2002.md | no | Respaldo clinico asociativo S1/S2: 6/31 frente a 1/49 son pacientes con quejas neurologicas por configuracion, no tornillos malposicionados por nivel. Criterio de posicion binario; CT sobre 220 tornillos; sesgo de aprendizaje declarado. No aporta prior ordinal S2. #28 resuelta; #12 cerrada delimitando benchmark a S1. |
| zwingmann2009navigated (CONFIRMADO, ROL CORREGIDO) | si | COMPLETO | zwingmann2009navigated.md | no | **El rango 31-60% NO aparece en el PDF.** Son dos complementos derivados (69% y 40% de Grado 0) de dos brazos distintos. Aporta escala 0/<2/2-4/>4 mm y dos tasas por tecnica. Ver implicancia #12 |
| smith2006iliosacral (CONFIRMADO) | si | COMPLETO | smith2006iliosacral.md | no | Escala graduada 0-3 con umbrales 2 mm y 4 mm. Confirmado N1. Pero es fuente SECUNDARIA: la escala viene de la literatura de tornillos pediculares |
| liu2021ctpelvic1k (CONFIRMADO, con reservas) | si | COMPLETO | liu2021ctpelvic1k.md | no | Dataset primario. **Solo 14 de 75 volumenes de CLINIC-metal estan anotados**; no dice que tipo de metal; no da cifra de degradacion. Ver implicancia #13 |
| wang2025adaptiveweighting (VERIFICADO 2026-09-08, ROL CORREGIDO) | **si** | **COMPLETO** | wang2025adaptiveweighting.md | no | **N1 se sostiene, pero es fuente SECUNDARIA del multi-ventana**: el marco viene de su ref. [24] (Niu & Wang, SPIE 2021). Aporta las tres ventanas exactas (LW/MW/SW), el umbral de 2500 HU y el uso de CLINIC-metal. Confirma la implicancia #2 (es remocion, no sintesis) y NO trae ninguna banda extendida tipo B_delta |
| peters2025hybrid (N1, PROTOCOLO ADOPTADO 2026-09-07) | si | COMPLETO | peters2025hybrid.md | no | Fuente principal del protocolo híbrido y benchmark elegidos: un error afecta el brazo físico. Aporta métricas de integridad ósea/metálica y la limitación de colocación aleatoria. Adaptación a síntesis pendiente; no equiparar automáticamente esas métricas con BFC/ISC (#16–17) |
| zhang2026pediclescrew (sube) | **FALTA** | ABSTRACT | zhang2026pediclescrew.md | no | Implicancias #3 y #4: colision con mi reclamo de novedad y segunda escala de brecha cortical |
| ren2022metalinsertion (CONFIRMADO tras leer) | si | COMPLETO | ren2022metalinsertion.md | no | Unica fuente con la advertencia explicita del metodo analitico sobre implantes ortopedicos. Fija umbrales de artefacto -75/75/500 HU |
| mclaren2021corridor (NUEVA FILA, leido 2026-09-08) | si | COMPLETO | mclaren2021corridor.md | no | **Unica fuente con definicion operacional de zona segura sacroiliaca: umbral Dmax >= 10 mm (igual para S1 y S2) y procedimiento 3D reproducible sobre 433 CTs.** Es lo que `ramadanov2025safezone` no pudo dar (#7). Riesgos de citarla mal: 1.53/1.02 grados NO son margen anatomico (incluyen 7 mm de tornillo y 150 mm estimados de piel a sacro); el 31.1% es solo S1, el "sin ningun corredor" es 5.1%; el umbral de 10 mm es heredado de Kaiser, no medido aqui — **y la lectura de Kaiser del mismo dia confirma que Kaiser tampoco lo mide**. NO publica coordenadas, angulos, margenes ni Dmax medio |
| kaiser2014dysmorphism (NUEVA FILA, leido 2026-09-08) | si | COMPLETO | kaiser2014dysmorphism.md | no | **El umbral de 10 mm NO se establece aqui: se elige y se hereda.** *"was chosen as a conservative size"* (Metodos, p. e120(2), refs. 29 y 37) y *"has been previously established ... by experienced surgeons"* (Discusion, p. e120(7), refs. 4, 29 y 37). La cadena sigue hacia Gardner 2010, Ziran 2007 y Moed 2006 — **Ziran ya se leyo el 2026-09-08 y NO contiene el umbral**; **Moed tambien se leyo el 2026-09-08 y SI contiene "1 cm", pero como separacion interforaminal en 2D, no como diametro de corredor**. Lo que SI aporta y nadie mas tiene: procedimiento de reformateo del CT segun el eje del sacro, definiciones operacionales de los angulos coronal y axial con landmarks oseos, y el sacral dysmorphism score = (coronal S1) + 2(axial S1). Riesgos de citarlo mal: atribuirle el 10 mm; tomar el >70 como umbral validado cuando es descriptivo; confundir sus cifras iliosacras (Tabla II) con las transsacras (score, 41%); ignorar que la cohorte EXCLUYE CT con implantes |
| gardner2010safezones (NUEVA FILA, leido 2026-09-08) | si | COMPLETO | gardner2010safezones.md | no | **El umbral de 10 mm SI aparece, pero tampoco nace aqui: se declara como criterio y se atribuye a las refs. 17 y 20 de Gardner** --- *"A safe zone dimension of 10 mm was considered the critical threshold"* (M&M, p. 624), con llamada a **Ziran 2003 (JBJS Br 85:411-418)** y **Moed 2006 (JOT 20:378-383)**. **Aviso critico: el Ziran del umbral es el de 2003, NO `ziran2007fluoroscopic`** (ese es su ref. 21 y nunca se usa para el umbral). Lo que SI aporta y nadie mas tiene: geometria de **S1 y S2 por separado y por fenotipo**, y la **aproximacion de areas S1/S2 en dismorficos** (222 y 220.1 mm2; no inversion del orden ni prior clinico de malposicion). Riesgos de citarlo mal: atribuirle el umbral; confundir cifras **iliosacras** (area, longitud, angulos) con **transsacras** (anchos y "transverse screw possible"); citar el abstract, que imprime *"15% versus 4%"* donde el cuerpo dice grados y mezcla inlet con outlet en S2; ignorar que clasifica dismorfismo **por radiografia simple, sin score**, y que mide el lado **no lesionado**. 25 entradas NO ENCONTRADO EN EL PDF |

## Nivel 2 — afecta la redaccion

| Clave | PDF | Acceso | Nota generada | Leido por mi | Para que lo uso |
|---|---|---|---|---|---|
| moed2006s2screw (leido 2026-09-08, **N2 CONFIRMADO**) | si | COMPLETO | moed2006s2screw.md | no | **Es la ref. 4 de Kaiser y el primer nodo TERMINAL de la cadena del 10 mm: el numero "1 cm" esta aqui y NO se cita a nadie.** Pero designa OTRA magnitud: *"a minimum of 1 cm between the S1 and S2 neural foramina on 3 sequential preoperative CT 3-mm sections"* (Metodos, p. 379) es separacion interforaminal en cortes axiales 2D, no el *"10-mm-diameter corridor"* perpendicular al eje que le atribuye Kaiser. **NO resuelve la implicancia #12:** no publica ninguna tasa de malposicion; publica 0 de 53 con criterio BINARIO (*"satisfactory screw position"*, Resultados, p. 380), sin definicion operacional y sin observador independiente declarado. Su unica escala en mm es de REDUCCION de la fractura (4 / 5-10 / 11-20 / >20 mm, p. 380), NO de posicion del tornillo: no mezclar con la escala 0-3 de `smith2006iliosacral`. Cifras propias citables: 49 pacientes, 53 tornillos S2, tornillo canulado de 7.0 mm, 6.5 mm como minimo declarado seguro en S2, 2 de 49 revisiones, P=0.008 y RR 15.67 (IC 5.24-46.83). Toda comparacion S1 vs S2 es cita de terceros. 31 entradas NO ENCONTRADO EN EL PDF **Revision tras van den Bosch (2026-09-08): N2 confirmado.** La comparativa es de quejas neurologicas por paciente y se cita desde la fuente primaria; ser intermediario no lo vuelve N1. |
| wu2022xcist (N1 → N2, 2026-09-07) | si | COMPLETO | wu2022xcist.md | no | Fundamento técnico de XCIST y discusión de límites de validación y reconstrucción. Descartado como respaldo autónomo de validación de metal; conserva uso metodológico. El protocolo adoptado se sustenta en Peters (#8, #17) |
| chen2024tumorsynthesis (VERIFICADO) | si | COMPLETO | chen2024tumorsynthesis.md | no | DiffTumor confirmado. No modela nada fuera de la mascara y trunca HU a [-175,250]: respaldo de B_delta y de C3. Candidato a N1 |
| hinsche2002fluoroscopy (NUEVA FILA, leido 2026-09-08) | si | COMPLETO | hinsche2002fluoroscopy.md | no | **No da ninguna tasa clinica de malposicion: el 2%-15% es cita heredada de sus refs. 5, 11, 20, 24 (Introduccion, p. 135).** Estudio de banco sobre 35 modelos de PLASTICO, no pacientes. Sirve para documentar que la cadena del 2%-15% no termina aqui (#12), para una definicion binaria de colocacion insegura, y para la asimetria S1/S2 (82% de los mal colocados en S2) |
| ziran2007fluoroscopic (NUEVA FILA, leido 2026-09-08) | si | COMPLETO | ziran2007fluoroscopic.md | no | **Entro como candidato a fuente del umbral de 10 mm (ref. 37 de Kaiser) y el PDF lo descarta del modo mas fuerte: no contiene NINGUNA medida de longitud.** Todas sus mediciones son angulares (goniometro de 1 grado) sobre 17 pelvis cadavericas. Aporta: angulos reales de las superficies criticas (27/50/53 inlet; 37/59/80 outlet), la critica al estandar de 40 grados, el volumen seguro definido por CUATRO superficies oseas, la reidentificacion de landmarks fluoroscopicos mal atribuidos (alar slope = cortical periarticular SI), y coeficientes de variacion de 7%-25% hasta 97%-140%. Riesgos de citarlo mal: atribuirle el 10 mm; usar sus angulos como si fueran orientaciones en el marco del CT (son angulos de haz de fluoroscopia); tomarlo como transsacro (es iliosacro simple a S1, con S2 y S3 excluidos a proposito) |
| zhang2025diffboost | si | COMPLETO | | no | Difusion guiada por texto para aumentacion en segmentacion |
| ramzan2026claim | si | COMPLETO | | no | Analogo metodologico: sintesis de lesion condicionada (LGE-MRI) |
| jacob2026lgesynthnet | si | COMPLETO | | no | Analogo metodologico: sintesis de cicatriz controlada (LGE-MRI) |
| xie2024implantsegmentation | si | COMPLETO | | no | Segmentacion de implantes; posible insumo de ISC |
| arand2019pelvicring | si | COMPLETO | | no | Variacion anatomica del anillo pelvico; justifica que el corredor no sea fijo |
| ramadanov2025safezone (BAJA tras leer) | si | COMPLETO | ramadanov2025safezone.md | no | Motivacion cualitativa de la restriccion del muestreador. NO da geometria 3D ni umbral: no es implementable |
| wang2019cochlear (VUELVE a 2 tras leer) | si | COMPLETO | wang2019cochlear.md | no | Precedente directo de insercion sintetica de metal: 1090 pares fabricados con fisica analitica. Mi degradacion a N3 fue error |
| liu2025pipeline (BAJA tras leer) | si | COMPLETO | liu2025pipeline.md | no | Plan optimo determinista, sin distribucion de poses. Pero define CSV y QID sobre CTPelvic1K, cerca de SAP/BFC |
| yun2026simulationdriven (BAJA tras leer) | si | COMPLETO | yun2026simulationdriven.md | no | MAR, no segmentacion. Pero usa CLINIC-metal y trae la frase del gap y una critica a XCIST |
| karageorgos2024ddpm (VERIFICADO, con disenso) | si | COMPLETO | karageorgos2024ddpm.md | no | Inserta metal con CatSim para fabricar sus pares. El agente propuso N1; se mantiene N2, ver disenso abajo |
| haneda2025aapm (CONFIRMADO tras leer) | si | COMPLETO | haneda2025aapm.md | no | Es la aplicacion competitiva del protocolo de `peters2025hybrid`, que lo cita como companero. Umbrales citables: 150 HU, +250 HU, escala 0-4 |

> **Mapeo difftumor RESUELTO (2026-09-06).** El PDF nombra su propio metodo:
> *"we introduce a novel framework, termed DiffTumor"* (Sec. 1, p. 2). La equivalencia
> difftumor = `chen2024tumorsynthesis` queda confirmada contra el texto.

## Nivel 3 — apoyo

| Clave | PDF | Acceso | Nota generada | Leido por mi | Para que lo uso |
|---|---|---|---|---|---|
| rombach2022latentdiffusion | si | COMPLETO | | no | Arquitectura LDM. Nadie la discute: se implementa, no se defiende |
| zhang2023controlnet | si | COMPLETO | | no | Arquitectura ControlNet. Idem |
| kazerouni2023diffusionsurvey | si | COMPLETO | | no | Survey de difusion en imagen medica |
| selles2024marreview | si | COMPLETO | | no | Review de MAR |
| deman2007catsim (BAJA tras leer) | si | COMPLETO | deman2007catsim.md | no | Paper de presentacion de software. No modela metal ni trae fisica reimplementable |
| vanbosse2011pelvicpositioning (BAJA tras leer) | si | COMPLETO | vanbosse2011pelvicpositioning.md | no | Error angular y RELATIVO sobre variables acetabulares. No afecta pose rigida en el marco del CT |
| singhrao2024fiducial | si | COMPLETO | | no | Fiduciales en radiocirugia; tangencial |

> **N3 no significa "no leer".** `rombach2022latentdiffusion` y `zhang2023controlnet`
> hay que leerlos igual, como manual de implementacion. Estan en N3 porque no
> amenazan el argumento, no porque sobren.

## Nivel 4 — descartes

Sin entradas actualmente. Al mover un paper aquí, conservar una única fila vigente
con clave, acceso, ficha y motivo: **aporte insuficiente para el uso previsto** o
**fuera de alcance**. La falta de acceso nunca demuestra insuficiencia de contenido.

## Nivel propuesto para moed2006s2screw — 2026-09-08

**Propuesta: N1, acceso COMPLETO.** Justificacion en una linea: es el primer eslabon de la
cadena del 10 mm que **no reenvia a nadie**, y a la vez el que demuestra que el numero
heredado designa una magnitud geometrica distinta de la que usan Kaiser y McLaren, asi que
un error al citarlo se traduce directamente en una restriccion mal definida en el Objetivo 2.
Entro a `_candidatos.md` con nivel sugerido 1 como "tercera fuente del 10 mm"; la lectura
**confirma el nivel y corrige el rol dos veces**: si contiene el numero (a diferencia de
Kaiser y de Ziran), pero como criterio de seleccion de pacientes —separacion interforaminal
en cortes axiales de 3 mm— y no como diametro de corredor. Decision final de la autora.

**Alternativa defendible: N2**, si la autora concluye que, por tratarse de otra magnitud,
Moed **no pertenece** a la cadena del corredor de 10 mm y queda solo como serie clinica de
contexto sobre S2. En ese caso el N1 de la cadena deberia migrar entero a Gardner 2010,
ultima fila viva de `_candidatos.md` en esa seccion.

**Lo que este paper NO puede hacer, escrito para que no se le vuelva a pedir:** servir de
prior clinico de malposicion. Cero eventos sobre 53 tornillos, criterio binario sin
definicion operacional, cohorte auto-seleccionada por un umbral anatomico estricto y lectura
no cegada. La implicancia #12 sigue abierta. Tampoco aporta geometria de corredor en
milimetros ni angulos de trayectoria.

## Nivel propuesto para ziran2007fluoroscopic — 2026-09-08

**Propuesta: N2, acceso COMPLETO.** Justificacion en una linea: entro a `_candidatos.md`
con nivel sugerido 1 como posible fuente original del umbral de 10 mm, y el PDF refuta ese
rol de la forma mas concluyente posible —**no contiene ninguna medida de longitud, solo
angulos**—, con lo que cae la unica razon que lo hacia N1 y queda como material de
redaccion: prueba documental del corte de la cadena y respaldo de la variabilidad
anatomica. Decision final de la autora.

**No se propone N4.** Conserva dos roles vigentes (eslabon auditado de la cadena del
umbral; evidencia de variabilidad angular inter-especimen), asi que no es un descarte de
uso completo. El rol que **no** cubre, escrito para que no se le vuelva a pedir: no aporta
geometria de corredor en milimetros, ni escala de colocacion segura/insegura, ni tasa
clinica de malposicion, ni nada reimplementable sobre un volumen CT.

**Alternativa defendible: N1**, solo si la autora decide que la auditoria de la cadena del
10 mm es en si misma critica para el Objetivo 2; en ese caso este paper es una de las tres
piezas de prueba y describirlo mal (atribuirle el umbral, como hace Kaiser) tocaria la
restriccion dura.

## Nivel propuesto para kaiser2014dysmorphism — 2026-09-08

**Propuesta: N1, acceso COMPLETO.** Justificacion en una linea: es el eslabon donde la
tesis creia cerrar la cadena del umbral de 10 mm y donde en realidad se abre, y al mismo
tiempo es hoy la unica fuente que da un procedimiento de medida angular calculable sobre
un volumen CT, asi que un error al citarlo (atribuirle el umbral, o confundir sus cifras
iliosacras con las transsacras) toca directamente la restriccion del Objetivo 2.
Entro a `_candidatos.md` con nivel sugerido 1 como "fuente original del umbral de 10 mm";
la lectura refuta ese rol pero **confirma el nivel por una razon distinta**: pasa de ser
el origen del umbral a ser la prueba documental de que el umbral no tiene origen conocido
en esta cadena, y ademas aporta el metodo que McLaren no publica. Decision final de la autora.

**Alternativa defendible: N2**, si la autora decide que el umbral de 10 mm no se adopta
como restriccion dura y que el sacral dysmorphism score se usa solo como encuadre. En ese
caso el N1 deberia migrar a Gardner 2010 / Ziran 2007 / Moed 2006, ya registrados en
`_candidatos.md` con nivel sugerido 1.

> Actualizacion 2026-09-08: de esos tres destinos, **Ziran 2007 queda descartado como
> destino del N1 por contenido** (no mide longitudes). Quedan Gardner 2010 y Moed 2006.
>
> Segunda actualizacion, misma fecha: **leido Moed 2006**. Si contiene el numero y no lo
> atribuye a nadie, pero lo define como **separacion entre los forametros S1 y S2 en
> cortes axiales**, no como diametro de corredor. La atribucion de Kaiser no es solo
> indirecta: **cambia de magnitud por el camino**. Queda **Gardner 2010** como unico
> destino posible del N1 de la cadena.

## Nivel propuesto para mclaren2021corridor — 2026-09-08

**Propuesta: N1, acceso COMPLETO.** Justificacion en una linea: es hoy la unica fuente
que da umbral numerico, procedimiento geometrico 3D y n grande para la restriccion del
Objetivo 2, asi que un error al citarla (confundir tolerancia quirurgica con margen
anatomico, o el 31.1% de S1 con "sin ningun corredor") se lleva por delante la
justificacion del muestreador en la sustentacion. Entro a `_candidatos.md` con nivel
sugerido 1 y la lectura lo confirma, con una salvedad: cubre el umbral, no la geometria.
Decision final de la autora.

## Nivel propuesto para hinsche2002fluoroscopy — 2026-09-08

**Propuesta: N2, acceso COMPLETO.** Justificacion en una linea: no puede amenazar el
benchmark porque no aporta ninguna cifra clinica citable (es banco sobre plastico y el
2%-15% lo cita de terceros), pero obliga a reescribir como se justifica la tasa de
malposicion, que es material de redaccion. Entro a `_candidatos.md` con nivel sugerido 1
bajo el supuesto de ser la fuente original del 2%-15%; la lectura refuto ese supuesto,
y con el cae la razon para N1. Decision final de la autora.

## Recategorización vigente — 2026-09-07

Peters permanece en N1: elegir su protocolo aumenta la dependencia del benchmark
respecto a su lectura correcta. Wu baja de N1 a N2 porque ya no sostiene por sí solo
el protocolo de comparación, pero sus límites y funcionamiento aún deben discutirse.
Solo correspondería N3 si quedara como cita del software sin argumento metodológico;
N4 exigiría que dejara de tener todo uso vigente. Véase `../01-decisiones.md`.

Las secciones siguientes conservan el historial: sus niveles no sustituyen las
tablas vigentes N1–N4 de arriba.

## Recriterio de niveles — 2026-09-06 (histórico)

El reparto anterior seguia una regla de tema (dataset / sintesis generativa / resto).
La autora lo redefinio por **riesgo sobre el argumento central o el benchmark
principal**. Diez filas se movieron.

### Subieron a N1

| Clave | Antes | Por que sube |
|---|---|---|
| liu2025pipeline | 3 | *End-to-End Geometry-Based Pipeline for Automatic Preoperative Surgical Planning of Pelvic Fracture Reduction and Fixation*, IEEE TMI 2025. El Obj 2 (muestreador de colocacion pelvica restringido) es lo unico del alcance MINIMO VIABLE que es contribucion propia. Esto es planificacion geometrica automatica de fijacion pelvica publicada en la misma revista. Es la colision de novedad mas directa que tiene el muestreador, y estaba en "no tan relevante". |
| zhang2026pediclescrew | 3 (conflicto) | El criterio de riesgo resuelve el conflicto que quedo abierto: es origen de DOS implicancias ABIERTAS (#3 colision de encuadre, #4 segunda escala de brecha cortical con umbral de 2 mm). Por definicion de la autora, eso es N1. La regla anterior lo mandaba a 3 solo por no estar en una lista. |
| ren2022metalinsertion | 2 | Insercion de metal en el dominio de proyeccion, ya publicado y funcionando. Es la respuesta directa a "por que necesitas un LDM si esto ya existe". Amenaza de novedad y candidato a baseline, no material de redaccion. |
| yun2026simulationdriven | 3 | *Simulation-Driven CT Metal Artifact Reduction Toward Improving Network Generalizability*, Medical Physics 2026. Simular artefactos metalicos para que una red generalice mejor: es mi receta con otro objetivo (ellos MAR, yo segmentacion osea). Es lo mas reciente y lo mas parecido en encuadre. |

### Subieron a N2

| Clave | Antes | Por que sube |
|---|---|---|
| karageorgos2024ddpm | 3 | Difusion aplicada a artefactos metalicos, pero para removerlos. Es evidencia citable de la implicancia #2 (el gap: lo publicado remueve, yo genero). Eso es material de Related Work, no de relleno. |
| haneda2025aapm | 3 | `refs.bib` lo pone en Medical Physics vol. 52, num. 10, e70050; `peters2025hybrid` (que es N1) esta en vol. 52, num. 10, e70020. Mismo numero. Si `peters2025hybrid` es el protocolo de validacion, esto es el reto al que sirve, y define como el campo evalua artefactos metalicos simulados. |
| deman2007catsim | 3 | El alcance COMPLETO promete "reimplementacion validada de XCIST como brazo de comparacion". CatSim es el antecedente de XCIST. Reimplementar un simulador exige su fisica, no solo su paper mas nuevo. |
| vanbosse2011pelvicpositioning | 3 | El posicionamiento pelvico introduce error en mediciones CT del acetabulo. Yo reporto pose 3D de implantes medida en el marco del CT. Es un caveat metodologico que hay que escribir, no ignorar. |

### Bajo a N3

| Clave | Antes | Por que baja |
|---|---|---|
| wang2019cochlear | 2 | MICCAI 2019, MAR con deep learning en implante coclear. Otra anatomia (hueso temporal), otra escala, y tarea inversa a la mia. Estaba en N2 por la regla de tema ("insercion de metal"), pero no inserta: remueve. No amenaza nada. |

### Se quedaron donde estaban, a proposito

- `wu2022xcist` en N1 aunque el brazo de comparacion sea alcance COMPLETO: si ese
  brazo se cae, el renderizador queda sin con que compararse.
- `arand2019pelvicring` en N2 y no N1: el muestreador trabaja sobre geometria del
  paciente (CTPelvic1K), no sobre un modelo estadistico poblacional. Justifica la
  variabilidad, no define la restriccion.
- `rombach2022latentdiffusion` y `zhang2023controlnet` en N3: nadie va a discutir
  en la sustentacion si LDM o ControlNet funcionan. Ver nota arriba.
- `chen2024tumorsynthesis` en N2: es precedente de paradigma (sintetizar lesiones
  mejora segmentacion), y ese precedente me favorece. Un precedente que apoya no es
  un riesgo.

### Costo de este reparto

N1 paso de 6 a 11 fuentes, y **dos de las 11 no tienen PDF**
(`wang2025adaptiveweighting`, `zhang2026pediclescrew`). Orden sugerido de lectura,
de mayor a menor riesgo no cubierto:

1. `liu2025pipeline` — colision con el Obj 2, sin registrar hasta hoy
2. `zwingmann2009navigated` y `smith2006iliosacral` — el benchmark y la escala
4. `yun2026simulationdriven` y `ren2022metalinsertion` — novedad del renderizador
5. `liu2021ctpelvic1k`, `peters2025hybrid`, `wu2022xcist` — infraestructura
6. `wang2025adaptiveweighting`, `zhang2026pediclescrew` — bloqueados por el PDF

> Actualizacion 2026-09-08: `wang2025adaptiveweighting` ya no esta bloqueado. Queda
> `zhang2026pediclescrew` como unica fuente N1 sin PDF.


## Verificado contra el PDF

Lecturas hechas con el subagente `lector-papers` para comprobar los niveles que se
habian asignado por titulo. Aqui solo lo ya confirmado o corregido.

### moed2006s2screw — leido 2026-09-08, N1 PROPUESTO (entra por snowballing)

Entro desde `_candidatos.md` como "tercera fuente del 10 mm, citada solo en la Discusion de
Kaiser". **El PDF confirma que el numero esta aqui, y a la vez rompe la equivalencia:**

- **El numero aparece dos veces y no se cita a nadie.** Abstract: *"a minimum of 1 cm
  between foramina on 3 sequential preoperative CT slices"* (Patients, p. 378). Metodos:
  *"a minimum of 1 cm between the S1 and S2 neural foramina on 3 sequential preoperative
  CT 3-mm sections"* (p. 379). Ninguna de las dos apariciones lleva llamada de referencia.
  **Es, hasta donde alcanza esta lectura, un nodo terminal de la cadena.**
- **Pero NO es un diametro de corredor.** Es una separacion entre los forametros S1 y S2
  medida en cortes axiales de 3 mm y exigida en tres cortes consecutivos. Kaiser le
  atribuye un *"10-mm-diameter corridor perpendicular to the axis of the safe zone"*.
  Son magnitudes distintas. **Fuente o justificacion anatomica del valor 1 cm:
  NO ENCONTRADO EN EL PDF.**
- **Va con una segunda condicion, nunca solo:** *"in conjunction with inadequate available
  space in S1"* (Abstract, p. 378). Es un criterio de indicacion del nivel S2, no de
  viabilidad geometrica general.
- **No aporta prior de malposicion (implicancia #12).** *"satisfactory screw position in
  the body of S2 was documented on the postoperative plain radiographs and CT scan in all
  cases"* (Resultados, p. 380): 0 de 53, en conteo, **sin porcentaje**. Criterio binario,
  **sin definicion operacional de "satisfactory"**, sin observador independiente ni cegado
  declarado, sin kappa. Modalidad: radiografia AP/inlet/outlet **mas TC 2D de 3 mm**.
- **El unico compromiso foraminal no fue error de insercion:** *"acute loss of reduction
  after injudicious full–weight bearing on the third postoperative day"* precedio al
  *"compromise of the S1 neural foramina by the S2 iliosacral screw"* (Resultados, p. 380).
  El tornillo migro con el hueso.
- **Trampa de familia de criterios:** la unica escala en milimetros del paper es de
  REDUCCION de la fractura, tomada de su ref. 2 (Matta y Tornetta 1996): *"excellent (4 mm
  of displacement), good (5 to 10 mm of displacement)"*, *"fair (11 to 20 mm)"*, *"poor
  (>20 mm)"* (Metodos, p. 380), medida como desplazamiento maximo en las tres proyecciones.
  **No es la escala 0-3 de brecha cortical de `smith2006iliosacral` y no debe mezclarse.**
- **Complicaciones con cifra:** cero lesiones nerviosas iatrogenicas intraoperatorias;
  2 de 49 revisiones por perdida de fijacion, ambas con osteopenia sospechada, una con
  lesion de raiz S1 recuperada por completo dentro del ano; 2 de 5 osteopenicos frente a
  0 de 44, *"P = 0.008, Fisher exact test"*, RR 15.67 (IC 95% 5.24-46.83).
  **Complicaciones vasculares: NO ENCONTRADO EN EL PDF.**
- **Geometria citable, minima:** tornillo canulado de 7.0 mm con broca de 3.2 mm
  (Metodos, p. 379) y *"the S2 body can safely accept a 6.5-mm or larger cancellous screw"*
  (Discusion, p. 382). **Diametro, area, longitud, angulos, punto de entrada y margenes del
  corredor: NO ENCONTRADO EN EL PDF.**
- **Ninguna comparacion S1 vs S2 es propia.** Todas son citas en Discusion (p. 382):
  van den Bosch 6/31 frente a 1/49; Hinsche con los mal colocados concentrados en S2;
  Carlson con *"much less margin for error when inserting an S2"* y con el espacio S2 que
  *"increased in patients with sacral dysmorphism"*; Ziran (2002, JBJS Br) con 31 tornillos
  S2 sin evento adverso; Griffin con 4 fallos de 62. **El paper ni siquiera reporta cuantos
  tornillos S1 coloco en su propia serie.**
- **No hay seccion de limitaciones: NO ENCONTRADO EN EL PDF.** Solo el diseno declarado
  retrospectivo y dos frases sueltas (*"based on limited data and merits further study"*,
  *"some factors other than placing a screw in the S2 body may have contributed"*, p. 382).
- **La tabla de Evidencia textual de la ficha cierra 31 entradas como NO ENCONTRADO EN EL
  PDF**, entre ellas el DOI impreso, la fuente del 1 cm, la tasa como porcentaje, la
  definicion de "satisfactory", la escala de posicion del tornillo, quien leyo la TC, el
  numero de tornillos S1, toda la geometria del corredor, kVp/mAs/kernel y la seccion de
  limitaciones.
- **Discrepancias de metadatos:** `_candidatos.md` lo fecha en *"2006 Aug"* y el PDF y
  `refs/raw/` dicen **July 2006**. Moed cita a Hinsche como *"Clin Orthop. 2001;395:135-144"*
  (su ref. 10) mientras `refs.bib` lo fecha en 2002, con mismo volumen y paginas. Y su
  ref. 22 es **Ziran 2002 (JBJS Br)**, no el `ziran2007fluoroscopic` leido el mismo dia.

**Se propone N1, una linea:** el rol se corrige dos veces (si tiene el numero, pero no es la
misma magnitud) y el nivel se sostiene porque es la fuente que decide si la tesis puede
declarar un origen para el umbral de su restriccion dura. Consecuencia para la implicancia
#7: **el umbral de corredor sigue sin fuente primaria auditada**, y ahora ademas la
atribucion de Kaiser queda bajo sospecha de cambiar de magnitud. Consecuencia para la
implicancia #12: **no se cierra**; una serie con cero eventos no es un prior. Consecuencia
para la implicancia #25: **cuarto eslabon consecutivo auditado en la misma cadena**.

### ziran2007fluoroscopic — leido 2026-09-08, N2 PROPUESTO (entra por snowballing)

Entro desde `_candidatos.md` como "segunda fuente citada por Kaiser en las dos ocasiones
del 10 mm". **El PDF cierra ese rol de forma definitiva:**

- **El umbral de 10 mm NO aparece. Ni el umbral ni ninguna otra longitud.** Revisado
  texto completo, abstract, Tabla 1, pies de las figuras 1-10, Apendice y conclusiones:
  **todas las mediciones del paper son angulares**, hechas con *"a metal goniometer with
  1-degree increments"* (Fluoroscopic Evaluation, p. 349). No hay diametro, area, seccion
  ni volumen de corredor en ninguna unidad. Los unicos milimetros del texto son el tornillo
  (*"screws (6.5–7.3 mm diameter)"*, Introduccion, p. 347) y el alambre de los marcadores
  (*"2-mm lead wire"*, p. 348). **Ziran 2007 no puede ser la fuente del umbral.**
  Consecuencia: de las tres filas de `_candidatos.md` para el origen del 10 mm quedan
  **dos vivas** (Gardner 2010 y Moed 2006).
- **Lo que si define es el volumen seguro por SUPERFICIES, no por un numero:** *"bounded
  by four surfaces: the posterior S1 body, the superior S1 ala, the anterior S1 ala, and
  the roof of the S1 foramen"* (Discusion, p. 353), con las estructuras neurales en riesgo
  por cada lado. El cuello de botella se declara sin cuantificar: *"the narrowest area of
  bone occurs in the sacral foraminal region"* (Abstract, p. 347).
- **Escala de colocacion segura o insegura: NO ENCONTRADO EN EL PDF.** Ni binaria ni
  graduada. No colocan tornillos, no miden brechas y no reportan tasa propia de
  malposicion. A diferencia de `hinsche2002fluoroscopy`, aqui no hay ni siquiera criterio
  binario.
- **Angulos reales frente al estandar de 40 grados** (Angular Measurements, p. 351):
  cuerpo anterior de S1 27 ± 11, cortical anterior del ala 50 ± 8, S1 posterior 53 ± 6
  (inlet); platillo S1 37 ± 6, eje foraminal S1 59 ± 8, cortical superior del ala 80 ± 7
  (outlet). Critica explicita: *"(27 and 53 degrees, respectively) both differ from the 40
  degrees described in the literature"* (Discusion, p. 353). Inlet util recomendado:
  *"averaged 49 degrees in our specimens"*; outlet util para el foramen S1: *"around 50
  degrees outlet"* (p. 354).
- **Respaldo cuantitativo de la variabilidad anatomica:** varianzas inter-especimen
  *"between 7% and 25%"* en general, y coeficientes de variacion de 43% (superficie
  anterior del cuerpo S1), 47%-52% (articulacion SI en axial sacro) y **97%-140%** (ala
  superior S1 en frontal sacro), Resultados, pp. 351-352. Util para argumentar que el
  muestreador no puede asumir pose canonica.
- **Reidentifica landmarks fluoroscopicos mal atribuidos:** la linea caudal a la creciente
  de S1 en AP *"is in actuality the inferior border of the posterior S2 foraminal outlet"*
  (p. 352) y el alar slope / iliac cortical density *"was in actuality the tangential
  projection of cortical bone around the sacroiliac joint"* (p. 352), no la cortical alar.
  Traslado a CT: cualitativo, sin coordenadas.
- **Es iliosacro simple a S1, NO transsacro.** *"S2 and S3 bodies were not characterized"*
  (p. 348) y la cohorte **excluye** dismorfismo alar. Ninguna cifra suya es comparable con
  el Dmax transiliosacro de McLaren ni con las cifras transsacras de Kaiser.
- **Poblacion:** *"17 whole cadaveric adult pelves (5 female, 12 male)"* (p. 348), de
  coleccion esqueletica, sin trauma. **No se adquirio ninguna CT en el estudio**; la CT
  solo aparece como trabajo ajeno citado y como alternativa clinica sugerida.
- **Dos discrepancias internas registradas en la ficha:** la fila "Superior ala (left
  coronal, outlet)" de la Tabla 1 da Male 10 y Female 6 con Total 5 (inferior a ambos), y
  el texto reporta 9 ± 10 grados donde la Tabla 1 da 5 (12) y 11 (10).
- **Limitacion que toca directamente a CLINIC-metal:** *"the presence of fracture and
  displacement would significantly affect fluoroscopic visualization"* (Discusion, p. 354).
  Suma al patron ya visto en Kaiser (cohorte sin implantes) y McLaren (pelvis intactas):
  **toda la cadena del corredor mide pelvis sanas**.
- **La tabla de Evidencia textual cierra 28 entradas como NO ENCONTRADO EN EL PDF**, entre
  ellas el umbral de 10 mm, cualquier diametro o area de corredor, longitud de trayectoria,
  margen al foramen y a la cortical, tolerancia angular, escala de seguridad, tasa propia
  de malposicion, protocolo de CT, kVp/mAs, umbral en HU, kappa entre los tres observadores,
  y edad/talla/peso/etnia de los especimenes.

**Se propone N2, una linea:** el rol por el que entro (fuente del umbral) queda refutado y
con el la razon para N1; conserva valor de redaccion como prueba del corte de la cadena y
como respaldo de la variabilidad angular. Consecuencia para la implicancia #7: **el umbral
de 10 mm sigue sin fuente primaria auditada, y ahora con un candidato menos**. Consecuencia
para la implicancia #25: **caso reforzado**, tercer eslabon consecutivo que hereda sin medir.

### kaiser2014dysmorphism — leido 2026-09-08, N1 PROPUESTO (entra por snowballing)

Entro desde `_candidatos.md` como "fuente original del umbral de 10 mm, que McLaren
adopta sin medirlo". **El PDF refuta ese rol y abre la cadena un eslabon mas:**

- **El 10 mm NO se mide aqui, se elige.** Metodos: *"A 10-mm-diameter corridor
  perpendicular to the axis of the safe zone was chosen as a conservative size for
  passage of an iliosacral screw"* (Quantification of the Osseous Safe Corridor,
  p. e120(2)), con llamada a las refs. **29 y 37**. Discusion: *"has been previously
  established as a reasonably 'safe'-diameter corridor by experienced surgeons"*
  (p. e120(7)), con llamada a las refs. **4, 29 y 37**. Los autores lo llaman
  *"our conservative 10-mm threshold"*. La unica justificacion interna es dimensional:
  *"chosen to allow 1 to 2 mm of circumference around a 6.3 to 8-mm-diameter screw"*.
  Las tres fuentes reales (Gardner 2010, Ziran 2007, Moed 2006) quedaron en
  `_candidatos.md`, seccion "el origen REAL del umbral de 10 mm", con nivel sugerido 1.
  **Actualizacion 2026-09-08: leida la ref. 37 (Ziran 2007), no contiene el umbral ni
  ninguna longitud. Leida tambien la ref. 4 (Moed 2006): contiene "1 cm", sin citar a
  nadie, pero como separacion interforaminal en cortes axiales, no como diametro de
  corredor.** Queda **Gardner 2010** como unica candidata viva.
- **Si aporta lo que McLaren no publica: los angulos de referencia.** Coronal:
  *"angle subtended by a line drawn perpendicular to the axis of the osseous corridor"*
  y *"a line connecting the top of the iliac crests"*. Axial: la misma perpendicular
  frente a *"a line connecting the posterior iliac spines"* (ambas en Metodos,
  p. e120(2)). Plano de reformateo: *"the axis was perpendicular to the superior end
  plate of the first sacral segment"* (Fig. 1, panel 2, p. e120(3)).
- **Sacral dysmorphism score, formula exacta:** *"sacral dysmorphism score = (first
  sacral coronal angle) + 2(first sacral axial angle)"* (Resultados, p. e120(4)),
  simplificada de una regresion logistica con coeficientes −0.122 y −0.268 y AUROC 0.93.
- **El >70 es DESCRIPTIVO, no un umbral validado.** *"There were no safe transsacral
  corridors in any subject with a dysmorphic score >70"* (Resultados, p. e120(4)).
  Sensibilidad, especificidad y valor p en ese punto: NO ENCONTRADO EN EL PDF. Media,
  DE y rango del score en la cohorte tampoco: estan solo en el Appendix online.
- **Cifras citables:** area minima S1 417.4 ± 81.1 mm2 y S2 213.3 ± 87.9 mm2; angulacion
  coronal 22.6 ± 11.1 y 5.2 ± 4.9 grados; axial 11 ± 10.5 y 3.4 ± 4.6 grados; longitud
  maxima de tornillo **iliosacro** 119.2 ± 35.7 mm y 128.1 ± 20.4 mm (Tabla II,
  p. e120(5)); 41% de fenotipo dismorfico y 12% de minoritario; cinco caracteristicas
  cualitativas con prevalencia 28-53%, acuerdo 70-81% y kappa 0.26-0.59 (Tabla I).
- **Cuatro discrepancias internas documentadas en la ficha:** tres rangos distintos de
  acuerdo entre revisores (abstract 70-81%, Resultados 75-81%, Discusion 70-80%), dos de
  kappa (abstract 0.26-0.59, Discusion 0.29-0.59), la fila de longitud de tornillo cuya
  direccion contradice al texto, y las referencias 17 y 22 duplicadas (Templeman 1996).
- **La cohorte EXCLUYE los CT con implantes:** *"radiographic contrast medium or implants
  obscuring the lumbosacral junction"* (Materials and Methods, p. e120(2)), y son pelvis
  no lesionadas. Caveat directo para trasladar la restriccion a CLINIC-metal.
- **Sobre planificacion automatica hay una frase A FAVOR**, no en contra: *"may represent
  an ideal application of computer navigation technology"* (Discusion, p. e120(7)).
  Una frase que diga que el metodo NO sirve para planificacion automatica:
  **NO ENCONTRADO EN EL PDF**.
- **La tabla de Evidencia textual cierra 41 entradas como NO ENCONTRADO EN EL PDF**, entre
  ellas coordenadas 3D, punto de entrada, margen al foramen, Dmax en mm, r o r2, grosor de
  corte, resolucion, kVp/mAs, kernel, umbral HU de la cortical, y n absoluto por cluster.

**Se propone N1, una linea:** el rol cambia (de origen del umbral a prueba de que el umbral
no tiene origen conocido en esta cadena) pero el nivel se sostiene, porque es la fuente que
decide si la tesis puede usar 10 mm como restriccion dura y ademas la unica que aporta las
definiciones angulares calculables. Consecuencia para la implicancia #7: **el umbral sigue
sin fuente primaria auditada**; los angulos de referencia quedan **parcialmente cubiertos**.
Consecuencia para la implicancia #25: **caso confirmado**, y con dos eslabones, no uno.

### mclaren2021corridor — leido 2026-09-08, N1 PROPUESTO (entra por snowballing)

Entro desde `_candidatos.md` como "posible solucion a la implicancia #7". **El PDF lo
sostiene a medias, y la mitad que falta importa:**

- **Si aporta umbral:** *"Dmax of≥10 mm was defned as the target amount of available
  space"* (Material and methods, PDF p. 2). Mismo umbral para S1 y S2.
- **Si aporta procedimiento 3D reproducible:** malla de contornos corticales, recta de
  tabla externa iliaca a tabla externa contralateral, y expansion *"until it contacted
  and breached the thickness of the cortex ... in at least three locations"* (misma
  seccion). Es lo que hace transiliosacro al corredor, no iliosacro simple.
- **Pero el umbral no es suyo:** *"Kaiser et al. recommended 10 mm or greater"* y *"the
  minimal corridor ... has not yet been established"* (Introduccion, PDF p. 2), con un
  rango previo de 8 a 12 mm. **Actualizacion 2026-09-08: leido Kaiser, tampoco es de
  Kaiser.** Ver la entrada de `kaiser2014dysmorphism` arriba.
- **La tolerancia angular no es margen anatomico:** se calcula restando 7 mm de tornillo
  a Dmax y usando *"The distance from the skin to the sacral body (estimated to be
  150 mm)"* (Material and methods, PDF p. 3), metodo tomado de Templeman. Los autores
  admiten que con origen en la cortical iliaca contralateral *"would have increased the
  angular tolerance"* (Discusion, PDF p. 5).
- **Discrepancias internas sin resolver:** 1.02 grados en las dos secciones de Resultados
  frente a 1.03 en las dos de Discusion; 48.3% (n=209) frente a *"352 (81.3%) pelves had
  both S1 and S2 corridors Dmax≥10 mm"* en el mismo parrafo; 31.1% en el abstract sin
  segmento frente a *"31% ... did not have a safe 10-mm S1 corridor"* en el cuerpo.
- **La tabla de Evidencia textual de la ficha cierra 22 entradas como NO ENCONTRADO EN
  EL PDF**, entre ellas coordenadas, angulos de referencia, margen al foramen o a la
  cortical, longitud del corredor, Dmax medio en mm, resolucion y protocolo de la CT,
  nombre de la institucion, y la ecuacion de la tolerancia en notacion matematica.
  Declara determinar *"the position, alignment and maximum diameter"* y publica solo el
  diametro.
- **Ninguna frase dice que el metodo no sirva para planificacion automatica:
  NO ENCONTRADO EN EL PDF.** Tampoco dice lo contrario.

**Se propone N1, una linea:** cierra el umbral que faltaba para el Objetivo 2, y por eso
mismo cualquier error al citarlo se propaga a la unica contribucion propia del minimo
viable. Consecuencia para la implicancia #7: queda **parcialmente cubierta** (umbral y
procedimiento si, geometria parametrizada no); las fuentes que cerrarian el resto estan
en `_candidatos.md`, seccion "la geometria que McLaren NO publica".

### wang2025adaptiveweighting — leido 2026-09-08, N1 CONFIRMADO con ROL CORREGIDO

Era la unica fuente N1 que seguia SIN VERIFICAR por falta de PDF (implicancia #1).
Con el texto completo (IEEE TMI 44(6):2408-2423, DOI 10.1109/TMI.2025.3534316):

- **Si es multi-ventana en HU, con tres ventanas explicitas:** LW [-1000HU, 2000HU],
  MW [-320HU, 480HU], SW [-160HU, 240HU] (*"we set the number of windows B to three"*,
  Sec. V-A-1, p. 2412). Se dan como rango [L, H], no como centro/ancho.
- **Pero el "adaptive weighting" del titulo NO es la parte multi-ventana.** El marco
  multi-ventana es de su ref. [24] (Niu & Wang, SPIE 2021): *"Motivated by the existing
  work [24], we construct the general multiple-window MAR framework"* (Sec. III,
  p. 2410). AdaW aporta el peso de la perdida por ventana, no la codificacion. **Para
  C3 es fuente SECUNDARIA**, el mismo defecto que ya tiene `smith2006iliosacral`.
- **La combinacion no es multicanal simultanea: es una cascada** de ventana ancha a
  estrecha con capa de transferencia y concatenacion por canal entre etapas (Eq. 1 y
  Fig. 1, p. 2410). No es identica a la codificacion multi-ventana de entrada de C3.
- **Confirma la implicancia #2: es REMOCION.** *"The image-domain-based technique aims
  to directly recover artifact-removed images from the corresponding corrupted ones"*
  (Sec. II-A, p. 2409). No propone generar artefacto en ningun punto.
- **Dominio imagen, sin datos crudos de fabricante en inferencia.** Reproducible sobre
  imagenes reconstruidas como CTPelvic1K.
- **No es difusion ni latente.** La difusion solo aparece citada como trabajo ajeno.
- **Nada tipo B_delta: banda extendida, margen o region peri-implante con valor
  numerico: NO ENCONTRADO EN EL PDF.** Solo menciones cualitativas al area cercana al
  metal. B_delta sigue sin precedente publicado.
- **Usa CLINIC-metal, y su ref. [54] es `liu2021ctpelvic1k`**: *"This popular clinical
  pelvic CT dataset is from [54] and it contains 14 metal-corrupted volumes"*
  (Sec. V-A-2, p. 2413). Coincide con las 14 series anotadas de la implicancia #13.

**Se sostiene N1, una linea:** sigue siendo la fuente que decide si C3 tiene respaldo
publicado, y ahora ademas aporta tres cifras citables (las ventanas, el umbral de
2500 HU y el uso de CLINIC-metal); el riesgo de citarla mal no bajo, cambio de sitio.
**Alternativa defendible: N2**, si la autora considera que el respaldo real de C3 es
Niu & Wang [24] y que AdaW pasa a ser solo confirmacion del encuadre; en ese caso el
N1 deberia migrar a Niu & Wang, ya registrado en `_candidatos.md` con nivel sugerido 1.

### hinsche2002fluoroscopy — leido 2026-09-08

Entro por snowballing como "fuente original del rango 2%-15%". **El PDF lo desmiente
dos veces:**

- El rango es una cita, no una medicion: *"has been reported to range between 2% and
  15%, even by experienced surgeons"* (Introduccion, p. 135), con llamadas a sus
  referencias 5, 11, 20 y 24 (Ebraheim 1993, Keating 1999, Routt 1997, Templeman 1996).
- El estudio no es clinico: *"28 plastic pelvic models (Synthes, Oberdorf,
  Switzerland) were used"* (Materials, p. 136), y *"No attempt to create a fracture or
  displacement was made"* (Experimental Setup, p. 136).

Lo que si aporta: criterio binario de colocacion insegura (*"unsafe when the screw path
perforated one of the cortices while jeopardizing neurovascular structures"*,
Measurements, p. 138), tasas de exito de banco por nivel (93% en S1; 71% y 64% en S2) y
la concentracion de fallos en S2 (*"18 of the 22 (82%) misplaced screws were at the S2
level"*, p. 142). Nueve entradas quedaron como NO ENCONTRADO EN EL PDF, entre ellas
margen al foramen, tolerancia angular y escala graduada en milimetros.

> Actualizacion 2026-09-08: `moed2006s2screw` **cita este mismo hallazgo** en su Discusion
> (p. 382), *"most of the misplaced screws, no matter which method was used, occurred at
> the S2 level"*, y lo referencia como *"Clin Orthop. 2001;395:135-144"*, no 2002. Mismo
> volumen y paginas; la discrepancia de ano queda anotada, sin resolver.

### ramadanov2025safezone — 1 CORREGIDO A 2 (2026-09-06)

Se habia promovido a N1 con el argumento de que era la unica fuente que define una
zona segura sacroiliaca desde CT. **El PDF no lo sostiene.** Lo que define es un
procedimiento cualitativo, no una geometria:

- Estudio piloto sobre **una sola CT**: *"This study is based on a single CT scan of
  a 75-year-old male patient"* (Sec. 4.1, p. 10).
- La zona sale de una proyeccion **2D**, no de un corredor 3D: *"a 2D lateral view of
  the sacrum was generated by summing the Y-axis slices"* (Metodos, paso 4, p. 4).
- El umbral no tiene valor: *"choosing a threshold high enough to only outline the
  high density of S1"* (Figura 5, p. 8).
- Umbral numerico propio, coordenadas, angulos, diametros, margen al cortical o al
  foramen, y tasa de malposicion propia: **NO ENCONTRADO EN EL PDF** (5 entradas).
- Los autores admiten que la formula esta pendiente: *"A formula or algorithm that
  allows for the application of the Ramadanov-Zabler Safe Zone [...] could
  significantly enhance clinical applicability"* (Sec. 4.2, p. 11).

Queda en **N2**: sirve para motivar la restriccion del muestreador, no para
implementarla ni para citar un umbral. Consecuencia registrada en la implicancia #7.

> Actualizacion 2026-09-08: la cita que este paper hacia de McLaren (1.53 / 1.02 grados,
> ~31.1% sin corredor viable) queda **verificada contra el PDF original**. Los valores
> coinciden con la seccion de Resultados de McLaren; el 31.1% aparece solo en su
> abstract y en el cuerpo se declara especifico de S1.


### Disenso registrado: karageorgos2024ddpm

El subagente propuso subirlo a N1 porque **inserta metal sintetico con CatSim** para
fabricar sus pares: *"Training data are generated by performing highly realistic CT
simulations of real patient images with and without metal objects"* (Sec. II-A, p. 3).
El dato es correcto y esta registrado.

Se mantiene en **N2** por consistencia: `wang2019cochlear`, `haneda2025aapm` y
`ren2022metalinsertion` tambien insertan metal sintetico, y si cada instancia sube a N1,
N1 pierde sentido como categoria. El hallazgo no es de este paper, es del patron, y esta
registrado como implicancia #9. `ren2022metalinsertion` se queda en N1 no por insertar
metal sino por su frase sobre implantes ortopedicos, que ningun otro trae.
Ademas no aporta a C3: normalizacion por ventana HU, **NO ENCONTRADO EN EL PDF**.

Decision de la autora si prefiere N1.

> Nota 2026-09-08: `wang2025adaptiveweighting` tambien inserta metal sintetico para
> fabricar su set de entrenamiento (*"then insert them into the collected clinical
> slices by carefully adjusting the size, angle, and position"*, Sec. V-A-2, p. 2414).
> Suma al patron de la implicancia #9, no cambia su nivel.

### Verificacion de los 6 N1 originales — 2026-09-06

Asignados por la autora, verificados con `lector-papers`. **Los 5 con PDF conservan
nivel 1.** Ninguno bajo. Pero dos tenian el ROL mal descrito:

| Clave | Nivel | Rol |
|---|---|---|
| `smith2006iliosacral` | 1 confirmado | Sostiene. Salvedad: es fuente SECUNDARIA de la escala |
| `peters2025hybrid` | 1 confirmado | Sostiene, y da mas de lo que se le pedia |
| `liu2021ctpelvic1k` | 1 confirmado | Sostiene con reservas graves (implicancia #13) |
| `zwingmann2009navigated` | 1 confirmado | **Rol falso**: el 31-60% no existe en el PDF (#12) |
| `wu2022xcist` | 1 confirmado | **Rol falso**: no valida artefacto metalico (#8) |
| `wang2025adaptiveweighting` | 1 confirmado (2026-09-08) | **Rol corregido**: es fuente SECUNDARIA del multi-ventana (viene de Niu & Wang [24]) y la combinacion es en cascada, no multicanal |

Contraste con la ronda anterior: de los movimientos que Claude hizo por titulo, 6 de 9
estaban mal. De las asignaciones de la autora, 5 de 5 correctas en nivel. El criterio de
la autora funciona; lo que fallo fue la descripcion del rol, que es un error mas dificil
de detectar porque no se nota hasta que alguien pide la cita.
Con la lectura del 2026-09-08 el marcador es **6 de 6 correctas en nivel** y **tres
roles corregidos** de seis.

> Actualizacion 2026-09-08 (tras Kaiser): el marcador de **roles corregidos por lectura**
> sube a cinco si se cuentan las dos fuentes que entraron por snowballing con un rol
> supuesto y salieron con otro: `hinsche2002fluoroscopy` (no es origen del 2%-15%) y
> `kaiser2014dysmorphism` (no es origen del 10 mm). Ambos conservan valor, con otro rol.

> Actualizacion 2026-09-08 (tras Ziran): sube a **seis**. `ziran2007fluoroscopic` entro
> con nivel sugerido 1 como fuente del 10 mm y sale en N2 con otro rol. Es el tercer
> caso consecutivo de una fuente que la cadena de citas presenta como origen de una cifra
> y que, leida, no la contiene. El patron ya no es anecdotico: **antes de citar cualquier
> cifra heredada, abrir el PDF del eslabon**.

> Actualizacion 2026-09-08 (tras Moed): sube a **siete**, y con una variante nueva del
> patron. `moed2006s2screw` **si contiene el numero heredado**, pero designando otra
> magnitud. No es "la cifra no esta": es "la cifra esta y mide otra cosa", que es mas
> dificil de detectar y mas peligroso de citar. **Verificar no solo que el numero
> aparezca, sino que la magnitud coincida.**

### Candidato a subir: chen2024tumorsynthesis

Entro como "precedente que me favorece, por tanto no es riesgo". La lectura lo
convierte en respaldo de dos decisiones de diseno (B_delta y C3), no solo de redaccion.
Si sostener una decision de diseno cuenta como N1 bajo el criterio de riesgo, sube.
Sin decidir. Ver implicancia #10.

## Notas de mapeo de claves

Seis nombres del encargo original no existen literalmente en `refs.bib`. `refs.bib`
es autoridad (regla 9), asi que se uso la clave real. `refs.bib` no se toco.

| Nombre usado en el encargo | Clave real en `refs.bib` |
|---|---|
| peters2025benchmark | peters2025hybrid |
| zwingmann2009malposition | zwingmann2009navigated |
| wang2025adaptive | wang2025adaptiveweighting |
| difftumor | chen2024tumorsynthesis (CONFIRMADO contra el PDF) |
| claim | ramzan2026claim |
| lgesynthnet | jacob2026lgesynthnet |

## Estado del inventario de PDFs

25 de 27 PDFs presentes en `papers/`, verificado por listado de archivos el
2026-09-06. Faltan `wang2025adaptiveweighting` y `zhang2026pediclescrew`, que son
las dos fuentes marcadas ABSTRACT y ahora ambas N1.
Actualizacion 2026-09-08: `papers/hinsche2002fluoroscopy.pdf` esta presente y se
leyo entero (pp. 135-144). **`papers/wang2025adaptiveweighting.pdf` tambien esta
presente y se leyo entero (16 paginas, pp. 2408-2423).** **`papers/mclaren2021corridor.pdf`
esta presente y se leyo entero (8 paginas de PDF; el archivo NO imprime numeros de
pagina de revista, el rango 1485-1492 viene de `refs/raw/`).**
**`papers/kaiser2014dysmorphism.pdf` esta presente y se leyo entero (8 paginas,
numeradas e120(1) a e120(8); el Appendix NO esta en el PDF, remite a jbjs.org).**
**`papers/ziran2007fluoroscopic.pdf` esta presente y se leyo entero (10 paginas,
numeradas 347-356; incluye Apendice, lista de 25 referencias y un "Editorial Comment"
firmado por John Gorczyca, University of Rochester).**
**`papers/moed2006s2screw.pdf` esta presente y se leyo entero (6 paginas, numeradas
378 a 383; incluye las tres figuras y la lista completa de 23 referencias).** Queda
`zhang2026pediclescrew` como unico N1 sin PDF.

> COMPLETO aqui significa "hay un PDF en `papers/`". No se abrio ningun PDF para
> confirmar que este entero ni que corresponda a la entrada de `refs.bib`.

> Los niveles reasignados salen de titulo, revista y metadatos de `refs.bib`, mas
> las dos fichas ya generadas desde abstract. **Ningun PDF se leyo para decidirlos.**
> Al leer, un nivel puede moverse otra vez.

## Regla dura de accesibilidad

Ninguna cifra especifica (porcentaje, umbral, tamano de muestra, resultado
cuantitativo) puede citarse en la tesis desde una fuente marcada ABSTRACT o
SIN ACCESO. Si la cifra es imprescindible: conseguir el texto completo, o
cambiar la afirmacion por una cualitativa.

## Fuentes con acceso limitado — detalle

| Clave | Acceso | Que intente para conseguirla | Que afirmacion mia queda en riesgo |
|---|---|---|---|
| zhang2026pediclescrew | ABSTRACT | La autora aporto el abstract el 2026-09-06 y dice que esta consiguiendo el articulo. | Su encuadre colisiona con mi reclamo de novedad (implicancia #3) y su escala de brecha cortical toca la definicion de BFC (implicancia #4). Ninguna de sus cifras es citable en este estado. |

**Resuelto el 2026-09-08:** `wang2025adaptiveweighting` sale de esta tabla. La autora
consiguio el PDF (IEEE Xplore, descarga del 2026-09-08 desde UTEC), se leyo entero y
paso a acceso COMPLETO. La regla dura de accesibilidad ya no le aplica: sus cifras son
citables. Cierra la implicancia #1.
