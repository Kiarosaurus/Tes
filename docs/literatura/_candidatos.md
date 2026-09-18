# Candidatos de snowballing

> Papers citados DENTRO de los que ya lei, que podrian importar.
> Claude los agrega al leer. La autora decide LEER o DESCARTAR.
> Al decidir LEER, la entrada pasa a `_index.md` y se descarga el PDF.

Estados: PENDIENTE | LEER | DESCARTADO

Todos los de abajo salieron de la ronda de 10 lecturas del 2026-09-06. Ninguno se
busco fuera del PDF donde aparece: se transcriben tal como los cita la fuente.
Las filas anadidas el 2026-09-08 salieron de la lectura de `hinsche2002fluoroscopy`,
de la relectura completa de `wang2025adaptiveweighting` (ahora con PDF), de la
lectura de `mclaren2021corridor`, de la lectura de `kaiser2014dysmorphism`, de la
lectura de `ziran2007fluoroscopic` y de la lectura de `moed2006s2screw`.

## PRIORIDAD VIGENTE — leer esto primero (auditoria 2026-09-18, actualizada tras la ronda de 13 lecturas)

> **Actualizacion 2026-09-18 (2):** se leyeron 13 fuentes mas (Ziran 2003, Gardner 2011, Reilly, Miller, Wu, Xu, Ebraheim
> 2000, Griffin, Mostafavi, DuDoNet++, ACDNet, Yazdi y b-MAR, esta ultima solo desde el abstract). **Ninguna entra en la
> tabla de prioridad:** todas quedaron LEIDAS. Reilly paso a `main.tex:117`. **La tabla de abajo no cambia:** los
> candidatos 1 (MWLNet) y 2 (Choi, LDM condicional para MAR) siguen siendo los unicos que tocan el renderizador, y faltan
> su PDF y su raw. Las filas nuevas de snowballing de esta ronda son todas N3-N4 "no perseguir". `song2024bmar` solo
> sube de prioridad si se planea una lectura humana ordinal del realismo, y para eso hace falta el PDF.

> Auditoria completa del archivo contra `refs/clean/` y `docs/literatura/`: 9 filas decian PENDIENTE pero ya estaban
> leidas (Gertzbein, Herman, Tejwani, Fan 2022, Zhang & Yu 2018, Yu 2021, De Man 1999, DuDoNet, Zwingmann 2013); ya
> estan marcadas LEIDO. Las filas historicas de abajo se conservan. **Esta tabla ordena solo lo que de verdad falta**,
> por cuanto puede mover la tesis con el alcance del 2026-09-17 (renderizador conservado, compuerta del Objetivo 1,
> ablaciones fuera). La prioridad la propone el asistente; decide la autora.

| # | Candidato | Fila | Que puede cambiar | Cuando leerlo |
|---|---|---|---|---|
| 1 | Niu C, Wang G. *Multiple window learning for metal artifact reduction* (MWLNet), Proc. SPIE 11840, 2021 | abajo, "origen del marco multi-ventana" | **C3 y el reclamo de novedad del renderizador.** Es la fuente original del MAR multi-ventana: hoy C3 se apoya en fuentes secundarias (`wang2025adaptiveweighting`, `li2024`) | **Ya.** Es el unico candidato que toca un reclamo vigente de `main.tex` |
| 2 | Choi D, Yun S, Hyun S, Cho S. *Metal artifact reduction algorithm with conditional latent diffusion model* | de `yun2026simulationdriven` | **Precedente directo del renderizador** (LDM condicional con metal, #9). Si ya genera artefacto condicionado, hay que acotar la novedad | **Ya**, junto con el 1 |
| 3 | Zwingmann J et al., J Trauma 2010;69:1501-1506 | de `zwingmann2013` (ref. 11) | **Benchmark del Objetivo 2.** Cohorte mayor (14/131 convencional, 1/63 navegado); si publica grados, seria la segunda distribucion ordinal | Antes de fijar el benchmark de SAP |
| 4 | Selles et al. 2023, ref. [140] de `selles2024marreview` (CT pelvica y fusion sacroiliaca) | de `selles2024marreview` | **`B_delta` y #57.** Seria la primera medicion de la extension espacial del artefacto cerca de un implante sacroiliaco | Antes de escribir la justificacion de `B_delta`. Primero hay que transcribir la cita completa |
| 5 | Park HS, Chung YE, Seo JK. *CT beam-hardening artefacts: mathematical characterization*, Phil Trans A 2015 | de `zhu2023sinogram` | #57 (estructura espacial del beam hardening), solo teorico | Si sobra tiempo |
| 6 | MAISI (Guo et al., WACV 2025), MedVAE (Varma et al.), CVQ-VAE (Zheng & Vedaldi, ICCV 2023) | de `chen2026foundationvae` / `yun2026simulationdriven` | **VAE alternativo para el Objetivo 3** | **Solo si P1 da No-Go** en las seis combinaciones (decision 2026-09-17) |
| — | Herramientas de GitHub del CT-MAR (scoring y FBP/reproyeccion) | de `haneda2025aapm` | Implementacion del brazo de Peters y P2 (#70) | Al implementar P2; es codigo, no lectura |

**No leer (cerrados por decision o sin impacto):** Ziran 2003 (cadena del 10 mm cerrada; ademas falta el raw), Roy-Camille
(ref. 4 de Gertzbein; ancla de 2 mm: la escala ya es convencion, #68 y #78), Carlson 2000 (bloqueada sin PDF ni raw; la medicion directa de
`D_TS` ya sustituye su "vestibulo"), y toda fila marcada "no perseguir". Las demas filas PENDIENTE de nivel 2-3 son
Related Work opcional y no cambian ningun objetivo.


## Cadena del umbral de 10 mm - estado vigente tras las lecturas

Gardner, Kaiser, Moed y Ziran 2007 estan LEIDOS. Gardner declara el umbral y lo
atribuye a Ziran 2003 y Moed; no lo valida empiricamente. La autora dio por agotada
la busqueda del origen y adopto 10 mm como convencion geometrica. Ziran 2003 sigue
sin leer, pero no es una tarea activa para perseguir ese umbral.

Gardner aporta geometria S1/S2; no distribuciones clinicas de brecha cortical.
Las decisiones vigentes conservan medicion individual sin fenotipos (#27) y el
benchmark ordinal solo en S1 (#12). Las filas siguientes reflejan ese estado.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Gardner MJ, Morshed S, Nork SE, Ricci WM, Chip Routt ML Jr. Quantification of the upper and second sacral segment safe zones in normal and dysmorphic sacra. J Orthop Trauma. 2010 Oct;24(10):622-9 | kaiser2014dysmorphism (ref. 29), mclaren2021corridor (ref. 9) | Geometria por nivel y morfologia. Areas medias iliosacras S1/S2 aproximadamente iguales en dismorficos (222/220.1 mm2), sin inversion de esas medias. No aporta prior ordinal SAP. Umbral de 10 mm declarado y heredado, no validado. Medicion individual sin fenotipos sigue vigente (#27). | 1 | LEIDO 2026-09-08; gardner2010safezones.md |
| Ziran BH, Smith WR, Towers J, et al. Iliosacral screw fixation of the posterior pelvic ring using local anaesthesia and computerised tomography. J Bone Joint Surg Br. **2002 o 2003**;85:411-418 | **gardner2010safezones (ref. 17)** y **moed2006s2screw (ref. 22)** | **ESLABON NUEVO del umbral, y a la vez pista para #12. Dos entradas independientes convergen en el mismo trabajo.** (a) Gardner le atribuye el 10 mm junto con Moed: fue candidata a origen del umbral antes del cierre de la busqueda, porque el "1 cm" de Moed resulto ser separacion interforaminal. (b) Moed la cita como *"Ziran et al inserted 31 screws into S2 without an adverse event using a CT-guided technique"* (Discusion, p. 382): serie clinica con **n por nivel sacro** y colocacion **guiada por CT**, el escenario mas cercano al que la tesis simula, como pista historica; #12 hoy se cierra delimitando el benchmark a S1. **AVISO 1: NO es `ziran2007fluoroscopic`**, ya leido; otro trabajo del mismo primer autor, otra revista, otro ano, otro diseno. **AVISO 2: discrepancia de ano entre las dos fuentes que la citan** --- Moed imprime `2002` y Gardner imprime `2003`, con el mismo volumen y las mismas paginas (85:411-418). Verificar contra el registro del editor antes de dar de alta la entrada | 1 | **LEIDO 2026-09-18** -> `ziran2003.md`: NO propone umbral de 10 mm (solo *"very narrow (10 to 14 mm) corridors"* en dismorficos, p. 417); 113 tornillos (80 S1, 31 S2, 2 S3), 0 malposicion con criterio binario; ano 2003 confirmado (#83) |
| Ziran BH, Wasan AD, Marks DM, Olson SA, Chapman MW. Fluoroscopic imaging guides of the posterior pelvis pertaining to iliosacral screw placement. J Trauma. 2007 Feb;62(2):347-56; discussion 356 | kaiser2014dysmorphism (ref. 37, dos veces) | Entro como **segunda fuente citada por Kaiser en las dos ocasiones del 10 mm**. **La lectura lo refuta de la forma mas concluyente: el paper no mide ninguna longitud, solo angulos.** No hay diametro, area ni seccion de corredor en todo el PDF. Lo que SI aporta, y por eso conserva valor: los angulos reales de las superficies criticas frente al estandar de 40 grados, el volumen seguro definido por CUATRO superficies oseas, la reidentificacion de landmarks fluoroscopicos mal atribuidos, y coeficientes de variacion inter-especimen de hasta 97%-140% | 1 → 2 | **LEIDO 2026-09-08.** Ficha en `ziran2007fluoroscopic.md`, fila anadida a `_index.md` en N2. **Descartado como origen del umbral de 10 mm por contenido** |
| Moed BR, Geer BL. S2 iliosacral screw fixation for disruptions of the posterior pelvic ring: a report of 49 cases. J Orthop Trauma. 2006 Aug;20(6):378-83 | kaiser2014dysmorphism (ref. 4) | Entro como **tercera fuente del 10 mm**, citada solo en la Discusion de Kaiser, y con aviso de descarte previo en la ronda de McLaren. **La lectura confirma a medias y refuta a medias:** el numero "1 cm" **si esta** y **no se cita de nadie** (nodo terminal), pero designa la **separacion entre los forametros S1 y S2 en cortes axiales de 3 mm**, no un diametro de corredor perpendicular al eje. Ademas **no aporta tasa de malposicion** (0 de 53, criterio binario, sin porcentaje ni definicion operacional): no resuelve la implicancia #12. Lo que SI aporta: criterio clinico de indicacion del nivel S2, calibres de tornillo (7.0 mm colocado, 6.5 mm minimo declarado seguro en S2) y la escala de REDUCCION de Matta 4/5-10/11-20/>20 mm. **Aviso de metadatos: el PDF y `refs/raw/` dicen July 2006, no August** | 2 | **LEIDO 2026-09-08.** Ficha en `moed2006s2screw.md`, N2 confirmado en `_index.md`. **Contiene el numero pero de otra magnitud**: Gardner tambien fue leido y no valida el umbral; cadena cerrada por decision |

## Prioridad maxima — el origen del marco multi-ventana (C3)

`wang2025adaptiveweighting` NO inventa la reconstruccion multi-ventana: la toma de su
ref. [24] y lo dice dos veces (*"Motivated by the existing work [24], we construct the
general multiple-window MAR framework"*, Sec. III, p. 2410; *"Following [24], we set
the number of windows B to three"*, Sec. V-A-1, p. 2412). Si C3 se apoya en
multi-ventana, el ancestro es este, no AdaW.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| C. Niu and G. Wang, "Multiple window learning for metal artifact reduction," Proc. SPIE, vol. 11840, p. 116, Sep. 2021 | wang2025adaptiveweighting (ref. 24); `li2024` (ref. 11, como *"Multi-window learning for metal artifact reduction"*, C. Niu, M. Li y G. Wang, Proc. SPIE 11840, may 2021, Art. no. 1184015: titulo, autores y mes discrepan de wang2025) | **Fuente ORIGINAL del marco MAR multi-ventana (MWLNet) y de las tres ventanas LW/MW/SW que sostienen C3.** Sin ella, C3 se cita desde una fuente secundaria, el mismo problema que ya arrastra `smith2006iliosacral`. Es ademas el competidor mas cercano al reclamo de novedad de la codificacion multi-ventana | 1 | PENDIENTE |

## Prioridad maxima — la cadena de la escala de brecha cortical

Las tres fuentes N1 de la tesis (`smith2006iliosacral`, `zwingmann2009navigated` y,
probablemente, `zhang2026pediclescrew`) usan la MISMA escala 0/<2/2-4/>4 mm, y ninguna es
su origen. Sin el ancestro, BFC se cita desde una fuente secundaria.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Gertzbein SD, Robbins SE. Accuracy of pedicular screw placement in vivo. Spine 1990;15:11-4 | smith2006iliosacral (ref. 7) | **Candidata a FUENTE ORIGINAL de la escala 0-3 con umbrales de 2 y 4 mm.** Es el ancestro probable de BFC y, si se confirma, cierra la implicancia #4: las dos escalas que parecian competir descenderian de aqui | 1 | **LEIDO** -> `gertzbein1990.md` (2026-09-15; verificado contra segunda copia del PDF 2026-09-17). Seis tramos de 2 mm, no cuatro grados |
| Vaccaro AR, Rizzolo SJ, Balderston RA, et al. Placement of pedicle screws in the thoracic spine. Part II. JBJS Am 1995;77:1200-6 | smith2006iliosacral (ref. 6) | Segunda de las tres fuentes que Smith cita como origen del metodo de graduacion . **Sube (2026-09-16, #68):** `mirza2003` le atribuye los cortes junto a Gertzbein, y Gertzbein no tiene cuatro grados: es el unico nodo sin leer entre los seis tramos de 1990 y los cuatro grados de 2003 | 1 | **LEIDO 2026-09-17** (`vaccaro1995part2.md`): **NO contiene escala graduada**; clasifica cada tornillo solo como perforacion medial, lateral o correcta (Tabla I, p. 1201). No es origen de los 4 grados; cadena de #68 cerrada (#78) |
| Mirza SK, Wiggins GC, Kuntz Ct, et al. Accuracy of thoracic vertebral body screw placement. A cadaver study. Spine 2003;28:402-13 | smith2006iliosacral (ref. 8) | Tercera fuente de la escala; ademas diseno cadaverico comparativo | 3 | LEIDA 2026-09-16 -> `mirza2003.md` (#68) |
| Matta JM, Tornetta P III. Internal fixation of unstable pelvic ring injuries. Clin Orthop. 1996;329:129-140 | moed2006s2screw (ref. 2) | **Fuente original de una SEGUNDA escala graduada en milimetros que la tesis podria confundir con BFC.** Moed la usa para calificar la REDUCCION de la fractura, no la posicion del tornillo: *"excellent (4 mm of displacement), good (5 to 10 mm of displacement)"*, fair 11-20 mm, poor >20 mm (Metodos, p. 380), medida como desplazamiento maximo en las tres proyecciones radiograficas. Si la tesis cita umbrales en mm de esta familia creyendo que son de brecha cortical, mezcla dos criterios incompatibles. Auditar para deslindar | 2 | **LEIDO 2026-09-17** (`matta1996internal.md`): escala de REDUCCION confirmada, no de posicion; limites inconsistentes entre abstract y Metodos (4/5 y 10 mm en dos categorias). No evalua malposicion de tornillos (#80) |

## Prioridad maxima — el origen real del 2%-15%

`zwingmann2009navigated` NO mide ese rango: lo cita. Si la tesis lo usa, debe citarlo
desde aqui. Ver implicancia #12.

**Actualizacion 2026-09-08, tras leer el PDF de Hinsche.** Hinsche 2002 **tampoco mide
ese rango**: lo cita en su Introduccion (p. 135) y lo atribuye a sus referencias 5, 11,
20 y 24. La cadena tiene un eslabon mas de lo que se creia. Las cuatro fuentes reales
del 2%-15% son las cuatro filas marcadas abajo con "(una de las 4 fuentes del 2%-15%)".

> **Actualizacion 2026-09-08, tras leer Moed.** La implicancia #12 **sigue sin cubrirse**.
> Moed es la primera serie clinica leida y **no publica ninguna tasa**: reporta 0 tornillos
> mal colocados de 53, con criterio binario y sin definicion operacional, sobre una cohorte
> auto-seleccionada por un umbral anatomico estricto y con lectura no cegada. Como prior de
> una distribucion de malposiciones es inservible. Las candidatas que si podrian aportar una
> tasa medida siguen siendo Routt 1997, van den Bosch 2002 y Keating 1999, mas las dos
> series nuevas de la seccion "de la lectura de Moed" (Ziran 2002 y Griffin 2003).

> **Actualizacion tras leer Keating (2026-09-08):** Keating SI publica una tasa propia:
> 5 de 38 pacientes (13%) con malposicion. Es un punto interior, no la banda completa
> ni sus extremos; la unidad es paciente y el criterio es binario radiografico. La ruta
> hacia Zwingmann es indirecta: Zwingmann -> Hinsche -> Keating. No sirve para SAP ordinal.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Hinsche AF, Giannoudis PV, Smith RM. Fluoroscopy-based multiplanar image guidance for insertion of sacroiliac screws. Clin Orthop Relat Res. 2002;395:135-144 | zwingmann2009navigated (ref. 13), smith2006iliosacral (ref. 2), **moed2006s2screw (ref. 10, fechada 2001)** | **NO es la fuente original del 2%-15%: lo cita de sus refs. 5, 11, 20 y 24.** Ademas es un estudio de banco sobre 35 modelos de PLASTICO, no clinico. Ficha: `hinsche2002fluoroscopy.md`. **Aviso 2026-09-08: Moed la referencia como "Clin Orthop. 2001;395:135-144"**, mismo volumen y paginas pero otro ano; discrepancia sin resolver | 2 | LEIDO 2026-09-08 |
| Routt MLC, Simonian PT, Mills WJ: Iliosacral screw fixation: Early complications of the percutaneous technique. J Orthop Trauma 11:584-589, 1997 | hinsche2002fluoroscopy (ref. 20), mclaren2021corridor (ref. 14), **kaiser2014dysmorphism (ref. 19)**, **ziran2007fluoroscopic (ref. 5)** | **(una de las 4 fuentes del 2%-15%).** Es ademas la unica serie clinica que Hinsche usa como contraste ("177 patients with 244 screws") y la fuente del tiempo de radiacion de 2.1 minutos por tornillo. Candidata mas fuerte a prior clinico de complicaciones. Confirmada ahora por CUARTA lectura independiente: Ziran la cita como una de las fuentes del riesgo de lesion cuando la fijacion sale del volumen oseo. **2026-09-08: sube de urgencia tras leer Moed**, que tampoco aporta tasa; esta sigue siendo la mejor candidata a prior clinico. **Aviso: no confundir con Routt, Simonian e Inaba 1997 en Oper Tech Orthop**, fila nueva mas abajo | 1 | **LEIDO 2026-09-17** (`routt1997early.md`): 5 de 244 tornillos mal colocados, *"2.05 percent"* (p. 587), criterio binario, 240 en S1. El *"15 percent"* del mismo parrafo es cita a Keating (ref. 5). Origen del 2%-15% resuelto (#77). No sirve como prior ordinal |
| Templeman D, Schmidt A, Freese J, Weisman I. Proximity of iliosacral screws to neurovascular structures after internal fixation. Clin Orthop Relat Res. 1996;329:194-198 | zwingmann2009navigated (ref. 28), smith2006iliosacral (ref. 3), hinsche2002fluoroscopy (ref. 24), mclaren2021corridor (ref. 10), **kaiser2014dysmorphism (refs. 17 y 22, duplicada en su lista)**, **ziran2007fluoroscopic (ref. 15)**, **moed2006s2screw (ref. 7)** | **(una de las 4 fuentes del 2%-15%).** Confirmada ahora por SEPTIMA lectura independiente. Fuente del umbral angular de 4 grados que `zwingmann2009navigated` cita como limite de dano neurovascular, y **Kaiser le atribuye exactamente la misma cifra**: *"A change in trajectory of only 4° can result in cortical perforation"* (Introduccion, p. e120(2), llamada a su ref. 22). Toca SAP directamente. Es ademas el origen del METODO trigonometrico que McLaren reutiliza (brazo estimado de 150 mm piel-sacro, 4.2 grados de tolerancia iliosacra, n=31 CTs postoperatorias). **Ziran la cita ademas como la unica fuente que aboga por las corticales anterior y posterior del cuerpo sacro como landmarks del inlet** (Discusion, p. 353). **Moed la cita para la proximidad del trayecto a las raices L5 y sacras y al canal espinal** (Introduccion, p. 378). Sin este PDF ni el 4° ni la tolerancia angular de McLaren se pueden auditar | 1 | **LEIDO 2026-09-17** (PDF `papers/templeman1996proximity.pdf`, clave `templeman1996proximity`): sin ningun % de malposicion; +-4 grados de trigonometria 2D idealizada (p. 197); 57 tornillos en S1 (#77, #79) |
| Ebraheim NA, Coombs RJ, Hoeflinger MJ, et al: A pitfall of radiologic evaluation of sacroiliac joint screw positioning. Orthopedics 16:616-618, 1993 | hinsche2002fluoroscopy (ref. 5) | **(una de las 4 fuentes del 2%-15%).** El titulo anuncia un sesgo en la evaluacion radiologica de la posicion del tornillo: si ese sesgo es real, afecta como se mide BFC sobre imagen. **LEIDO 2026-09-14:** reporte de un caso, **sin tasa de malposicion**; no es fuente del 2%-15%. El sesgo es de proyeccion en la AP (foramen S1 posterior superpuesto al ala), no de la CT: no cambia BFC ni SAP. Ficha: `ebraheim1993.md`. Snowballing: su ref. 6 (Ebraheim 1987, estabilizacion percutanea guiada por CT) no cumple las reglas y no se propone | 3 | LEIDO 2026-09-14 |
| Keating JF, Werier J, Blachut P, et al: Early fixation of the vertically unstable pelvis: The role of iliosacral fixation of the posterior lesion. J Orthop Trauma 13:107-113, 1999 | hinsche2002fluoroscopy (ref. 11), mclaren2021corridor (ref. 23), **kaiser2014dysmorphism (ref. 10)** | **LEIDO: SI contribuye evidencia a la afirmacion heredada.** Publica 5/38 pacientes (13%) con malposicion, pero no escribe 2%-15%, no fija los extremos y no informa una tasa por tornillo pese a usar 85. Criterio binario radiografico; sin datos S1/S2 ni escala ordinal. Ficha: `keating1999iliosacral.md`. | 2 | LEIDO 2026-09-08 |
| van den Bosch EW, van Zwienen CM, van Vugt AB. Fluoroscopic positioning of sacroiliac screws in 88 patients. J Trauma. 2002;53:44-48 | zwingmann2009navigated (ref. 32), smith2006iliosacral (ref. 4), mclaren2021corridor (ref. 12), moed2006s2screw (ref. 12) | **LEIDO 2026-09-08**, ficha `vandenbosch2002.md`. Confirma 6/31 vs 1/49 como pacientes con quejas neurologicas por configuracion, no malposicion por tornillo/nivel. Posicion binaria, sin prior ordinal S2; sesgo de aprendizaje. #28 resuelta; #12 delimitada a benchmark ordinal S1. | 1 | LEIDO |

## Prioridad alta — tocan una implicancia ABIERTA

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| McLaren, D.A.; Busel, G.A.; Parikh, H.R.; et al. Corridor-diameter-dependent angular tolerance for safe transiliosacral screw placement: An anatomic study of 433 pelves. Eur. J. Orthop. Surg. Traumatol. 2021, 31, 1485-1492 | ramadanov2025safezone | **Es la posible solucion a la implicancia #7.** Fuente original de las tolerancias 1.53 grados (S1) y 1.02 grados (S2) y del ~31% sin corredor viable, sobre 433 pelvis. Es la candidata mas fuerte a definicion OPERACIONAL de zona segura, que es justo lo que `ramadanov2025safezone` no da | 1 | **LEIDO 2026-09-08.** Ficha en `mclaren2021corridor.md`, fila anadida a `_index.md`. Aporta umbral (Dmax >= 10 mm) y procedimiento geometrico 3D reproducible; NO publica coordenadas, angulos, margenes ni Dmax medio en mm |
| Noojin FK, Malkani AL, Haikal L, et al: Cross-sectional geometry of the sacral ala for safe insertion of iliosacral lag screws: A computed tomography model. J Orthop Trauma 14:31-35, 2000 | hinsche2002fluoroscopy (ref. 15), **ziran2007fluoroscopic (ref. 21)** | **Toca la implicancia #7.** Es la fuente, medida por CT en pacientes, de las dimensiones del pediculo sacro que Hinsche usa para validar su modelo de plastico (27.76 mm de alto, 28.05 mm de ancho). Geometria del corredor derivada de CT, que es exactamente el insumo del muestreador. **Segunda lectura independiente: Ziran la agrupa entre los estudios que "caracterizan por CT este volumen de hueso", el tipo de fuente que a el le falta y a la tesis tambien** | 1 | **LEIDO 2026-09-17** (`noojin2000cross.md`): corte sagital oblicuo unilateral, 13 pacientes; alto/ancho del contorno, no diametro inscrito perpendicular al eje. **No comparable con D_TS; no cierra #7** (#80) |
| Herman, A.; Keener, E.; Dubose, C.; Lowe, J.A. Simple mathematical model of sacroiliac screws safe-zone-Easy to implement by pelvic inlet and outlet views. J. Orthop. Res. 2017, 35, 1478-1484 | ramadanov2025safezone | Modelo geometrico de zona segura: compite directamente con el muestreador. Fuente original del 32% de brechas corticales en 156 tornillos, cifra vecina del 31-60% de `zwingmann2009navigated` | 1 | **LEIDO** -> `herman2016.md` |
| Tejwani, N.C.; Raskolnikov, D.; McLaurin, T.; Takemoto, R. The role of computed tomography for postoperative evaluation of percutaneous sacroiliac screw fixation and description of a "safe zone". Am. J. Orthop. 2014, 43, 513-516 | ramadanov2025safezone | Fuente original del umbral **>2.7 mm** de penetracion foraminal asociado a deficit neurologico, y de la tasa 23/51. Umbral candidato para BFC e ISC; engancha con la implicancia #4 (umbral de 2 mm de `zhang2026pediclescrew`) | 1 | **LEIDO** -> `tejwani2014.md` |
| AAPM CT Metal Artifact Reduction (CT-MAR) grand challenge benchmark tool. GitHub, xcist/example/tree/main/AAPM_datachallenge | haneda2025aapm | **Toca la implicancia #8.** Herramienta de scoring y rutina FBP/reproyeccion en Python. Podria validar la reimplementacion de XCIST, o reemplazarla como brazo de comparacion ya parametrizado | 2 | PENDIENTE |
| AAPM CT Metal Artifact Reduction (CT-MAR) Grand Challenge Scoring Metrics. GitHub, AAPM_datachallenge/scoring_metric.md | haneda2025aapm | Definiciones matematicas y umbrales operativos de las ocho metricas del reto, incluidas *bone integrity* (150 HU) y *metal integrity* (+250 HU). Reutilizable para BFC e ISC | 2 | PENDIENTE |
| Fan, Y.; Pack, J.; De Man, B. A virtual imaging trial framework to study cardiac CT blooming artifacts. SPIE 2022 | haneda2025aapm, karageorgos2024ddpm | **Toca las implicancias #8 y #9.** Es la validacion citada de que CatSim produce artefactos realistas. Aparece en dos lecturas independientes como la fuente de esa afirmacion. Si el respaldo del realismo de CatSim es debil, cambia el peso del brazo de comparacion | 2 | **LEIDO** -> `fan2022.md` |
| Zhang, Y.; Yu, H. Convolutional neural network based metal artifact reduction in X-ray computed tomography. IEEE TMI 2018, 37(6), 1370-1381 | ren2022metalinsertion, yun2026simulationdriven, karageorgos2024ddpm, wang2025adaptiveweighting (ref. 8), xie2024implantsegmentation (ref. 50) | **Toca la implicancia #9.** Aparece en CUATRO lecturas independientes como el origen del banco de mascaras/formas metalicas usado para insertar metal sinteticamente; `wang2025adaptiveweighting` toma de aqui sus 90 metales de entrenamiento. Es la fuente de facto de la geometria de implantes en toda esta literatura, y el punto de comparacion natural del banco propio de 61 geometrias | 1 | **LEIDO** -> `zhang2018.md` |
| Y. Song, "B-MAR: Bidirectional artifact representations learning framework for metal artifact reduction in dental CBCT," Phys. Med. Biol., vol. 69, no. 14, Jul. 2024, Art. no. 145010 | wang2025adaptiveweighting (ref. 55) | **Fuente original de la escala de calificacion humana de 5 niveles** que `wang2025adaptiveweighting` usa para evaluar sobre CLINIC-metal, justamente porque ese dataset no tiene imagen limpia de referencia. Es el unico protocolo de lectura humana visto hasta ahora aplicado al dataset pelvico primario, y es candidato a validar el realismo del renderizador cuando no hay ground truth. Toca la implicancia #13 | 2 | **FICHA DESDE ABSTRACT 2026-09-18** -> `song2024bmar.md` (sin PDF): el abstract no menciona escala de 5 niveles; verificar requiere el PDF |
| Zhu Y, Zhao H, Wang T, Deng L, Yang Y, Jiang Y, Li N, Chan Y, Dai J, Zhang C. Sinogram domain metal artifact correction of CT via deep learning[J]. Comput Biol Med. 2023;155:106710 | xie2024implantsegmentation (ref. 36) | **Toca la implicancia #47.** Es la unica referencia a la que Xie atribuye que el umbral simple *"may result in inaccurate metal segmentation or hinder clinical applications"* (Discussion, p. 8): eslabon siguiente de la afirmacion que C1 usa como justificacion | 2 | **LEIDO 2026-09-17** (`zhu2023sinogram.md`): dice que el umbral simple *"can make the metal projection data inaccurate"* (Sec. 2.2.1, p. 4); Xie desplaza el objeto (proyeccion -> segmentacion). **No toca `main.tex`**: C1 cita a Xie por su propia sobrecobertura (#81) |
| Yu L, Zhang Z, Li X, Xing L. Deep sinogram completion with image prior for metal artifact reduction in CT images[J]. IEEE Trans Med Imaging. 2020;40(1):228-38 | xie2024implantsegmentation (ref. 49); tambien listada en la ficha de yun2026simulationdriven (ref. 21) | **Toca la implicancia #47 y compite con el renderizador.** Es el protocolo de simulacion (beam hardening, Poisson, volumen parcial) con el que Xie fabrica el ground truth sobre el que mide la sobrecobertura del umbral. Si la sobrecobertura depende de ese simulador, la cifra no se traslada a CT clinica. Segunda lectura independiente que la cita | 2 | **LEIDO** -> `yu2021.md` |
| Yazdi M, Lari MA, Bernier G, Beaulieu L. An opposite view data replacement approach for reducing artifacts due to metallic dental objects[J]. Med Phys. 2011;38(4):2275-81 | xie2024implantsegmentation (ref. 15) | Umbral RELATIVO (*"90% of the maximum gray value"*, Xie p. 2) en lugar de HU fijo. Es un precedente publicado de umbral relativo al maximo, cercano al semimaximo local de E8 (#47). Dental | 2 | **LEIDO 2026-09-18** -> `yazdi2011opposite.md`: umbral global 0.9*Imax por corte, sin validar; precedente de umbral relativo, NO del semimaximo local (#87) |
| Lyu Y, Lin W-A, Lu J, Zhou SK. Dudonet++: encoding mask projection to reduce ct metal artifacts[J]. arXiv preprint arXiv:200100340, 2020 | xie2024implantsegmentation (ref. 7) | Unica fuente que Xie da para el umbral de 3000 HU (p. 2). Probablemente convencion, no origen medido | 3 | **LEIDO 2026-09-18** -> `lyu2020dudonet.md` (ver #87) |
| Li Z, Gao Q, Wu Y, Niu C, Zhang J, Wang M, Wang G, Shan H. Quad-Net: quad-domain network for CT metal artifact reduction[J]. IEEE Transactions on Medical Imaging; 2024 | xie2024implantsegmentation (ref. 9) | Una de las tres fuentes que Xie da para el umbral de 2500 HU (p. 2), el que usa E8. Probablemente convencion, no origen | 3 | LEIDA 2026-09-16 -> `li2024.md` (#71) |
| Wang H, Li Y, Meng D, Zheng Y. Adaptive convolutional dictionary network for CT metal artifact reduction[J]. arXiv preprint arXiv:2205.07471, 2022 | xie2024implantsegmentation (ref. 14) | Otra de las tres fuentes del 2500 HU en Xie (p. 2). Mismo grupo que `wang2025adaptiveweighting`, que atribuye el 2500 HU a DICDNet y DuDoNet | 3 | **LEIDO 2026-09-18** -> `wang2022adaptativeconv.md` (PDF = arXiv v2): 2500 HU *"Following [Yu et al., 2020]"*, pero `yu2021` usa 2000 HU (#87) |

## Prioridad alta — la geometria que McLaren NO publica (2026-09-08)

`mclaren2021corridor` cierra el umbral (Dmax >= 10 mm) y el procedimiento, pero declara haber
determinado "position, alignment and maximum diameter" y **solo reporta el diametro**. No hay
coordenadas, ni angulos de referencia, ni margen al foramen, ni Dmax medio en mm. Estas filas
son las que faltarian para que el muestreador tenga la restriccion completa. Ver implicancia #7.

> Actualizacion 2026-09-08, tras leer Kaiser: **Kaiser cubre parcialmente el hueco de los
> angulos de referencia** (define angulo coronal y axial con landmarks oseos y da el plano
> de reformateo), pero **no** aporta coordenadas, punto de entrada, margen al foramen ni
> Dmax en mm. Las filas de abajo siguen abiertas.

> Actualizacion 2026-09-08, tras leer Ziran: **no cubre nada de este hueco.** Sus angulos
> son de haz de fluoroscopia, no orientaciones en el marco del CT, y no da ninguna longitud.
> Aporta solo el listado cualitativo de las cuatro superficies que acotan el volumen.

> Actualizacion 2026-09-08, tras leer Moed: **tampoco cubre nada.** Su unica longitud
> geometrica es el criterio de 1 cm interforaminal medido en 2D; no da diametro, area,
> longitud de corredor, angulos, punto de entrada ni margen. Las filas siguen abiertas.

> **CIERRE 2026-09-08: seccion agotada.** Las 8 filas estan LEIDAS. Resultado: la
> geometria SI existe, pero repartida en marcos de referencia que no componen entre si
> (implicancia #30), y ninguna terna posicion-orientacion-diametro es coherente. Las dos
> atribuciones de McLaren para el 10 mm (Kaiser y Lee) colapsan en el mismo nodo ya
> auditado. **No queda ninguna fila PENDIENTE aqui y no se propone reabrirla.**

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Gottschling H. SM, Reimers N., Fischer F., Homeier A., Burgkart R. (2009) A System for Performing Automated Measurements on Large Bone Databases. In: Dossel O., Schlegel W.C. (eds) World Congress on Medical Physics and Biomedical Engineering | mclaren2021corridor (ref. 31) | **Es el algoritmo que McLaren usa y no describe** ("utilizing the 3D methodology for automatic bone contour extraction previously described by Gottschling"). Sin el, el procedimiento de Dmax no es reimplementable y el muestreador no hereda de McLaren nada ejecutable | 1 | **LEIDO 2026-09-08.** Ficha en `gottschling2009.md`. **Trata solo femur y tibia** (1265 femures, 805 tibias): no aparece pelvis, sacro, corredor ni tornillo. No documenta la medicion sacra de McLaren y no da parametros de implementacion. Origen de la implicancia #32 |
| Kaiser SP, Gardner MJ, Liu J, Routt ML Jr, Morshed S (2014) Anatomic determinants of sacral dysmorphism and implications for safe iliosacral screw placement. J Bone Joint Surg Am 96(14):e120 | mclaren2021corridor (ref. 19) | Entro como **supuesta fuente original del umbral de 10 mm**. **La lectura lo refuta:** Kaiser tampoco lo mide, lo elige como criterio conservador y lo atribuye a sus refs. 4, 29 y 37. Lo que SI aporta y no tenia ninguna otra fuente: el procedimiento de reformateo del CT segun el eje del sacro y las definiciones operacionales de los angulos coronal y axial con landmarks oseos, mas el sacral dysmorphism score | 1 | **LEIDO 2026-09-08.** Ficha en `kaiser2014dysmorphism.md`, fila anadida a `_index.md`. Cadena auditada, incluido Gardner: busqueda cerrada por decision; 10 mm como convencion |
| Lee JJ, Rosenbaum SL, Martusiewicz A, Holcombe SA, Wang SC, Goulet JA (2015) Transsacral screw safe zone size by sacral segmentation variations. J Orthop Res 33(2):277-282 | mclaren2021corridor (ref. 18) | Segunda de las dos fuentes que McLaren cita para "previously been defned as 10 mm". Junto con Kaiser cierra de donde sale el umbral que sostendria la restriccion del muestreador. **Sube de urgencia**: como Kaiser resulto ser eslabon y no origen, esta es ahora la otra mitad de la atribucion de McLaren y hay que auditarla igual | 1 | **LEIDO 2026-09-08.** Ficha en `lee2014.md` (clave por el raw; fasciculo impreso 2015). **CITA el 10 mm de Gardner, no lo mide ni lo elige**: *"an arbitrary safety threshold of 10 mm"*. Con esto las DOS atribuciones de McLaren colapsan en el mismo nodo ya auditado. Aporta ademas geometria n=526 y el efecto LSTV (S2 viable 26% vs 73%) |
| Gras F, Gottschling H, Schroder M, Marintschev I, Hofmann GO, Burgkart R (2016) Transsacral osseous corridor anatomy is more amenable to screw insertion in males: a biomorphometric analysis of 280 pelves. Clin Orthop Relat Res 474(10):2304-2311 | mclaren2021corridor (refs. 28, 31) | Segunda cohorte grande (280 pelvis) medida con el MISMO software automatizado. Es la fuente que McLaren cita para la diferencia por sexo y para el "upward of 90% at least one safe corridor". Candidata a aportar las dimensiones en mm que McLaren no publica | 1 | **LEIDO 2026-09-08.** Ficha en `grass2016.md`. **SI publica la geometria en mm**: S1 12.8 mm, S2 11.6 mm, y por sexo. Umbral propio de 9 mm derivado de un tornillo de 7.3 mm. **Aviso: el PDF no menciona a McLaren ni afirma usar el mismo software** (eso era supuesto del candidato). Excluye pelvis con hardware o fractura |
| Wagner D, Kamer L, Sawaguchi T, Geof Richards R, Noser H, Uesugi M, Ossendorf C, Rommens PM (2017) Critical dimensions of trans-sacral corridors assessed by 3D CT models: relevance for implant positioning in fractures of the sacrum. J Orthop Res 35(11):2577-2584 | mclaren2021corridor (ref. 29) | Modelo estadistico 3D de las dimensiones criticas del corredor transsacro. Compite con la parametrizacion del muestreador y es candidato a aportar la geometria que McLaren dice haber determinado y no reporta | 2 | **LEIDO 2026-09-08.** Ficha en `wagner2017.md`. Da S1cc 11.6 mm y S2cc 14.0 mm, umbrales 12/8 mm y modelo PCA de forma. **Invierte el orden S1/S2 respecto a Gras por definicion de diametro distinta** (#30b). No da punto de entrada, angulos ni margen al foramen. Excluye fracturas y patologias |
| Mendel T, Noser H, Wohlrab D, Stock K, Radetzki F (2011) The lateral sacral triangle—A decision support for secure transverse sacroiliac screw insertion. Injury 42(10):1164-1170 | mclaren2021corridor (ref. 36) | Construccion geometrica explicita (triangulo sacro lateral) como soporte de decision para la trayectoria transversa segura. Alternativa parametrizable frente a un unico escalar Dmax | 2 | **LEIDO 2026-09-08.** Ficha en `mendel2011.md`. Triangulo sacro lateral con boundary ratio 1.5 (VPP 97%, sensibilidad 94%), calibrado contra tornillo de 7.3 mm. **Parcialmente reimplementable**: la alineacion a vista lateral estricta es codigo propio de Amira y la formula de ratioT queda ambigua. Cero angulos |
| Zhao Y, Li J, Wang D, Lian W (2012) Parameters of lengthened sacroiliac screw fixation: a radiological anatomy study. Eur Spine J 21(9):1807-1814 | mclaren2021corridor (ref. 37) | El titulo promete **parametros** de la trayectoria iliosacra alargada (angulos, longitudes), que es exactamente el hueco de McLaren. Candidato directo a completar la pose del muestreador | 2 | **LEIDO 2026-09-08.** Ficha en `zhao2012.md`. **Cubre media pose**: punto de entrada como distancias a EIPS y escotadura ciatica mayor (S1 42.21-63.69 y 32.77-53.75 mm; S2 22.68-54.28 y 14.06-33.70 mm) y longitudes por nivel. **Ningun angulo en ninguna unidad**; direccion solo cualitativa. n=66 pelvis sanas |
| Hasenboehler EA, Stahel PF, Williams A, et al. (2011) Prevalence of sacral dysmorphia in a prospective trauma population: implications for a "safe" surgical corridor for sacro-iliac screw placement. Patient Saf Surg 5(1):8 | mclaren2021corridor (ref. 39) | Fuente de la prevalencia de dismorfismo (hasta 50%) que McLaren usa para explicar su 31% sin corredor S1 seguro. Determina que fraccion de la poblacion cae fuera del corredor estandar | 3 | **LEIDO 2026-09-08.** Ficha en `hasenboehler2011.md`. Prevalencia **14.2%-14.5%** (49/344), no 50%: origen de la implicancia #33. Aporta angulos axiales medios (S1 19.27, S2 13.10 grados) y corredores axiales (1.73 cm S1, 1.15 cm S2). Adopta la clasificacion tipo 1/2/3 de Carlson, no fija umbral propio |

## Prioridad alta — de la lectura de Kaiser (2026-09-08)

Filas nuevas que no salen del umbral de 10 mm pero cumplen las reglas de proposicion.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Miller AN, Routt ML Jr. Variations in sacral morphology and implications for iliosacral screw fixation. J Am Acad Orthop Surg. 2012 Jan;20(1):8-16 | kaiser2014dysmorphism (ref. 27) | **Fuente de la DEFINICION de displasia del segmento sacro superior que Kaiser adopta**: *"a sacral phenotype in which the size and orientation of the upper sacral segment does not allow safe passage of a transiliac, transsacral screw"* (Introduccion, p. e120(2)). Si el muestreador estratifica por dismorfismo, la definicion se cita desde aqui, no desde Kaiser | 2 | **LEIDO 2026-09-18** -> `miller2012variations.md`: review cualitativo, 7 signos de dismorfismo sin umbrales; la definicion que Kaiser le atribuye NO esta en el PDF (#84) |
| Day CS, Prayson MJ, Shuler TE, Towers J, Gruen GS. Transsacral versus modified pelvic landmarks for percutaneous iliosacral screw placement—a computed tomographic analysis and cadaveric study. Am J Orthop (Belle Mead NJ). 2000 Sep;29(9 Suppl):16-21 | kaiser2014dysmorphism (ref. 23), **ziran2007fluoroscopic (ref. 19)** | **Analisis por CT de landmarks pelvicos para colocacion iliosacra percutanea**, con validacion cadaverica. Es el tipo exacto de fuente que podria dar los landmarks y la geometria de referencia que McLaren no publica y que Kaiser solo cubre a medias. **Segunda lectura independiente. Es ademas la unica referencia de Ziran cuyo titulo distingue transsacro de landmarks modificados, distincion que la tesis debe mantener** | 2 | PENDIENTE |
| Gardner MJ, Routt ML Jr. Transiliac-transsacral screws for posterior pelvic stabilization. J Orthop Trauma. 2011 Jun;25(6):378-84 | kaiser2014dysmorphism (ref. 21) | Fuente citada por Kaiser para el requisito geometrico del tornillo transsacro: *"must be of sufficient size and complementary orientation to allow screw placement without a cortical breach"*. Es la definicion operacional de **transiliaco-transsacro** frente a iliosacro, distincion que la tesis debe mantener explicita | 2 | **LEIDO 2026-09-18** -> `gardner2011transiliac-transsacral.md`: criterio de viabilidad cualitativo, sin umbral en mm; la frase que Kaiser le atribuye NO esta en el PDF (#84) |
| Reilly MC, Bono CM, Litkouhi B, Sirkin M, Behrens FF. The effect of sacral fracture malreduction on the safe placement of iliosacral screws. J Orthop Trauma. 2003 Feb;17(2):88-94 | kaiser2014dysmorphism (ref. 18) | **Unica fuente vista hasta ahora que cuantifica como la FRACTURA degrada la zona segura.** Toda la cadena de corredores (Kaiser, McLaren, Gras) mide pelvis intactas; la tesis trabaja sobre CT con fractura e implante. Si el muestreador aplica una restriccion medida en pelvis sanas a pelvis fracturadas, esta es la fuente que dice cuanto se paga por ello. **2026-09-08: refuerzo desde Ziran**, que declara *"the presence of fracture and displacement would significantly affect fluoroscopic visualization"* (Discusion, p. 354). Tercera cohorte consecutiva medida sobre pelvis sanas. **Segundo refuerzo desde Moed**, cuyo unico compromiso foraminal se produjo por perdida de reduccion POSTOPERATORIA y no por error de insercion (Resultados, p. 380): la seguridad geometrica depende de que la reduccion se mantenga | 2 | **LEIDO 2026-09-18** -> `reilly2003effect.md`: SI mide corredor en pelvis fracturadas (cadaver, S1, desplazamiento craneal 5-20 mm): el area limite cae 36-90%. **Citado en `main.tex:117`** (#85 APLICADA 2026-09-18) |
| Lu LP, Li YK, Li YM, Zhang YQ, Zhong SZ. Sacral morphology of the sacrum in a Chinese population. Clin Anat. 2009 Jul;22(5):619-26 | kaiser2014dysmorphism (ref. 36) | **Toca directamente la transferibilidad del score a CTPelvic1K.** Kaiser cita este trabajo al explicar por que su prevalencia de 41% esta en el extremo alto y atribuye la diferencia a la composicion etnica (*"a 73% prevalence of minority ethnicities"*, Discusion, p. e120(6)). CTPelvic1K es mayoritariamente poblacion china: si el corredor y los angulos difieren por poblacion, la restriccion del muestreador no se traslada sin ajuste | 2 | **LEIDO 2026-09-18** -> `wu2009variable.md` (autores reales Wu LP et al., Kaiser imprime "Lu"): 203 sacros secos, sin CT ni corredor ni dismorfismo; no sostiene la diferencia etnica que Kaiser le atribuye (#84) |

## Prioridad alta — de la lectura de Ziran (2026-09-08)

Filas nuevas que salen del PDF de `ziran2007fluoroscopic`. Ziran declara explicitamente el
hueco que estas fuentes podrian llenar: *"we have not found a study that correlated the
anatomic landmarks of the posterior pelvis to their corresponding fluoroscopic images"*
(Introduccion, p. 347), con llamada a sus refs. 16 y 17. Ese es exactamente el tipo de
correspondencia que la tesis necesita, pero medida sobre volumen y no sobre proyeccion.

> Las citas se transcriben **tal como las imprime Ziran en sus pp. 355-356**, incluidas sus
> abreviaturas y sus paginaciones incompletas. No se completaron ni se corrigieron.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Ebraheim NA, Rongming X, Biyani A, Nadaua MC. Morphologic consideration of the first sacral pedicle for iliosacral screw placement. Spine. 1997;22:841-846 | ziran2007fluoroscopic (ref. 17) | **Morfologia del pediculo de S1 especificamente para colocacion iliosacra: es geometria en milimetros del mismo volumen que la tesis quiere restringir.** Ziran la cita como una de las dos unicas fuentes previas de correlacion landmark-anatomia. Candidata a aportar las dimensiones que ni McLaren ni Kaiser publican, y por tanto a la implicancia #7 | 1 | **LEIDO 2026-09-08.** Ficha en `ebraheim1997.md`. Da geometria fina del pediculo de S1 (altura anterior 30.2 mm, profundidad 27.8 mm, ala 45.8 mm), punto de entrada a 3-3.5 cm del borde posterior del ilion, longitud segura hasta 80 mm y **margen de 4-6 mm entre dos tornillos**, cifra unica en toda la linea. **No da angulos, ni sexo, ni S2**, y su marco de referencia no compone con el de `zhao2012` (#30 ampliada). Aviso de metadatos: PubMed imprime **Xu R**, no 'Rongming X'; fasciculo 22(8):841-6 |
| Carlson DA, Scheid DK, Maar DC, et al. Safe placement of s1 and s2 iliosacral screw: The "vestibule" concept. J Orthop Trauma. 2000;14:4 | ziran2007fluoroscopic (ref. 18), **moed2006s2screw (ref. 13, que la imprime como "J Orthop Trauma. 2000;14:264-269")** | **Define un concepto geometrico propio de colocacion segura (el "vestibulo") para S1 y S2.** Es una definicion operacional alternativa a Dmax y al volumen de cuatro superficies de Ziran, y por tanto compite con la restriccion del muestreador. **Aviso: "Carlson 2000" figura en la lista de descartados de la lectura de McLaren** como comparacion biomecanica o serie sin geometria; **reaparece con rol nuevo** (fuente de una definicion de zona segura), que si cumple la regla. Segundo aviso: **la paginacion que imprime Ziran es "14:4", incompleta; Moed imprime 14:264-269**, que probablemente la resuelve, pero la discrepancia se deja anotada sin decidir. **SEGUNDA lectura independiente, y refuerzo fuerte desde Moed:** la describe como estudio por CT en **30 voluntarios sanos** que define *"the space available for iliosacral screws in the S1 and S2 vertebral bodies"*, y le atribuye dos afirmaciones que la tesis necesita: *"much less margin for error when inserting an S2, as opposed to an S1, iliosacral screw"* y que ese espacio *"increased in patients with sacral dysmorphism"* (Discusion, p. 382). Gardner ya aporta geometria comparada S1/S2 y recoge un desacuerdo con Carlson sobre fenotipo; Carlson sigue pendiente como fuente primaria de ese desacuerdo, no por ausencia de geometria leida | 1 | **LEER (decision de la autora, 2026-09-08).** Ultima lectura de la linea junto con Ebraheim 1997. **BLOQUEADA: no hay PDF en `papers/` ni entrada en `refs/raw/`.** Nota previa: **Cuarto, quinto y sexto refuerzo 2026-09-08:** `hasenboehler2011` adopta su clasificacion tipo 1/2/3 (>1.2 cm / 0.75-1.2 cm / <0.75 cm) como unico umbral y no fija uno propio; `wagner2017` le toma el umbral de 12 mm; `mendel2011` y `lee2014` tambien la citan. **Es el nodo de convergencia que queda vivo** tras cerrar la cadena del 10 mm, pero su rol ya no es el umbral (cerrado por decision) sino una clasificacion por fenotipo que la tesis dejo FUERA por #27. Leerla no cambiaria ninguna decision vigente |
| Xu R, Ebraheim NB, Douglas K, Yeasting RA. The projection of the lateral sacral mass on the outer table of the posterior ilium. Spine. 1996;21:790-795 | ziran2007fluoroscopic (ref. 11) | **Es literalmente la proyeccion de una estructura sacra sobre la tabla externa del ilion**, es decir la correspondencia entre punto de entrada y volumen diana. El punto de entrada es el parametro que McLaren declara haber determinado y no publica, y que el muestreador necesita para posar el implante | 2 | **LEIDO 2026-09-18** -> `xu1996projection.md`: triangulo de la masa lateral en la tabla externa (EIPS 30 mm, EIPI 27.4 mm al eje), sin S1/S2, sin angulos ni CT. No da punto de entrada puntual (#86) |
| Ebraheim NA, Haman SP, Xu R, et al. The lumbosacral nerves in relation to dorsal s1 screw placement and their locations on plain radiographs. Orthop. 2000;23:245-247 | ziran2007fluoroscopic (ref. 13) | Ubica los nervios lumbosacros **respecto al tornillo de S1 y sobre la imagen**. Las cuatro superficies del volumen seguro de Ziran se justifican por las estructuras neurales adyacentes, pero Ziran no da ninguna distancia; esta fuente podria dar el margen en milimetros que falta para definir BFC o ISC con criterio anatomico | 2 | **LEIDO 2026-09-18** -> `ebraheim2000lumbosacral.md`: tornillo dorsal S1 (NO iliosacro); sin margenes neurales en mm (#86) |
| Mostafavi H, Tornetta P. Radiographic evaluation of the pelvis. Clin Orthop. 1996;329:6-14 | ziran2007fluoroscopic (ref. 25) | **Fuente de un metodo de landmarks que Ziran refuta explicitamente**: *"we could not identify an anatomic basis for their proposal"* y *"we do not think that S2 and S3 structures accurately delineate the boundaries"* (Discusion, p. 353). Es un desacuerdo publicado sobre cual es el landmark valido: si la tesis adopta landmarks de referencia, tiene que saber que hay dos escuelas y cual sigue | 2 | **LEIDO 2026-09-18** -> `mostafavi1996radiologic.md`: origen de la regla S2/S3 como limite anterior (sin justificacion; refutada por Ziran 2007). `main.tex` no la usa |
| Amongero ME, Wilber JH. Upper sacral morphology and its relation to sacroiliac screw fixation. Orthopaedic Trans. 1995;19:435 | ziran2007fluoroscopic (ref. 16) | La otra de las dos unicas fuentes previas que Ziran reconoce sobre morfologia sacra superior en relacion con la fijacion sacroiliaca. **Aviso de acceso: es un resumen de congreso (Orthopaedic Transactions), probablemente sin texto completo**, igual que Leighton 1998 | 3 | PENDIENTE |

## Prioridad alta — de la lectura de Moed (2026-09-08)

Filas nuevas que salen del PDF de `moed2006s2screw`. Moed declara un hueco que la tesis
tambien tiene: *"Although a few reports can be found describing the use of an S2 screw, no
body of clinical data exists"* (Introduccion, p. 378). Las dos primeras filas son las unicas
series clinicas con conteos por nivel sacro vistas hasta ahora, y la tesis acaba de decidir
condicionar el muestreador por nivel (S1 vs S2). Ver implicancias #7 y #12.

> Las citas se transcriben **tal como las imprime Moed en sus pp. 382-383**.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| ~~Ziran BH, Smith WR, Towers J, et al. (JBJS Br 85:411-418)~~ | moed2006s2screw (ref. 22) | **FILA FUSIONADA el 2026-09-08.** Se consolido con la entrada equivalente de la seccion "el origen REAL del umbral de 10 mm", donde sube a nivel 1 al converger con la atribucion de Gardner. Ver alli, incluida la discrepancia de ano | --- | **MOVIDA arriba** |
| Griffin DR, Starr AJ, Reinert CM, et al. Vertically unstable pelvic fractures fixed with percutaneous iliosacral screws: does posterior injury pattern predict fixation failure? J Orthop Trauma. 2003;17:399-405 | moed2006s2screw (ref. 23) | **Serie clinica de 62 pacientes con distribucion detallada por nivel** (*"56 with 1 screw in S1 and another in S2"*) y **tasa de fallo de fijacion de 4 de 62**, que Moed usa como su contraste principal (Discusion, p. 382). Es una tasa clinica medida y asociada a patron de lesion, por tanto candidata a la implicancia #12. Aviso que pone el propio Moed: *"No mention was made of neurological complications"*, asi que aporta fallo mecanico, no malposicion | 2 | **LEIDO 2026-09-18** -> `griffin2003vertically.md` (PDF = reimpresion JOT 2006 Suppl): 62 pacientes, posicion solo radiografica, sin malposicion ni grados. No es prior S2 |
| Gautier E, Bachler R, Heini PF, et al. Accuracy of computer-guided screw fixation of the sacroiliac joint. Clin Orthop. 2001;393:310-317 | moed2006s2screw (ref. 11) | **Fuente de una restriccion de DIAMETRO dependiente del nivel sacro:** *"They described an increased risk for S2 because of limited bone stock and recommended screws no larger than 4.5 mm"* (Discusion, p. 382). Si se confirma, el banco de 61 geometrias no puede usarse igual en S1 y en S2. **Aviso: ya existe una fila de "Gautier E, Baechler R 1999" (resumen de congreso de CAOS, desde Hinsche) con la MISMA recomendacion de 4.5 mm.** Podrian ser el mismo trabajo publicado despues en revista; esta version esta en revista y deberia auditarse primero | 2 | PENDIENTE |
| Routt MLC, Simonian PT, Inaba J. Iliosacral screw complications. Oper Tech Orthop. 1997;7:206-220 | moed2006s2screw (ref. 8, la mas citada de su PDF) | **Es la referencia mas usada de todo el PDF de Moed** y la fuente a la que atribuye las tres afirmaciones que sostienen el encuadre S1 vs S2: que el dismorfismo limita el espacio en S1, que la zona segura de S2 *"is smaller and more difficult to understand fluoroscopically"* (Discusion, p. 382), y la tecnica de las vistas inlet/outlet/lateral. **Aviso: NO es Routt, Simonian y Mills 1997 en J Orthop Trauma 11:584-589**, ya registrado arriba entre las 4 fuentes del 2%-15%; es otro trabajo del mismo ano y grupo, en Operative Techniques in Orthopaedics. Si la tesis afirma que la zona segura de S2 es menor, esta es la fuente que Moed cita para ello | 2 | LEIDA 2026-09-16 -> `routt1997.md` |

## Prioridad media — compiten con un componente

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Goerres, J.; Uneri, A.; Jacobson, M.; et al. Planning, guidance, and quality assurance of pelvic screw placement using deformable image registration. Phys. Med. Biol. | liu2025pipeline | Planificacion y control de calidad de colocacion de tornillos pelvicos. Compite con el muestreador por una via distinta a la de `liu2025pipeline` (registro deformable, no optimizacion geometrica) | 2 | PENDIENTE |
| Yang, W.; Feng, S.; Song, J.; et al. Computer-aided automatic planning and biomechanical analysis of a novel arc screw for pelvic fracture internal fixation. Comput. Methods Programs Biomed. 2022, 220, 106810 | liu2025pipeline | Planificacion automatica de tornillo en fractura pelvica; competidor directo del Objetivo 2 | 2 | PENDIENTE |
| Aregger, F.C.; Gewiess, J.; Albers, C.E.; et al. Evaluation of the true lateral fluoroscopic projection for the relation of the S1 recess/foramen to safe corridors in transiliac-transsacral screw placement in human cadaveric pelves. Eur. J. Orthop. Surg. Traumatol. 2024, 35, 31 | ramadanov2025safezone | Define zona segura por la diagonal del cuerpo de S1 y reporta 10/14 pelvis con corredor viable. Definicion geometrica alternativa; segunda opcion si McLaren no sirve. **2026-09-08: gana peso tras leer Ziran**, que declara que la vista lateral es clave pero *"difficult to obtain and interpret"* y que el landmark que se le atribuye esta mal identificado. **Segundo refuerzo desde Moed**, que hace de la vista lateral sacra la clave de su tecnica (*"used to target the center of the S2 body"*, Metodos, p. 379) y atribuye a su ausencia los malos resultados de van den Bosch en S2 | 2 | **LEIDO 2026-09-18** -> `gardner2011transiliac-transsacral.md`: criterio de viabilidad cualitativo, sin umbral en mm; la frase que Kaiser le atribuye NO esta en el PDF (#84) |
| Routt MLC, Simonian PT, Agnew SG, et al: Radiographic recognition of the sacral alar slope for optimal placement of iliosacral screws: A cadaveric and clinical study. J Orthop Trauma 10:171-177, 1996 | hinsche2002fluoroscopy (ref. 19), **kaiser2014dysmorphism (ref. 31)**, **ziran2007fluoroscopic (ref. 7)**, **moed2006s2screw (ref. 9)** | Define el alar slope, el rasgo geometrico que Hinsche senala como la desviacion principal entre su modelo de plastico y la anatomia real, y que Kaiser usa como una de las cinco caracteristicas cualitativas ("acute alar slope", kappa 0.59, de los dos mas altos). Posible restriccion geometrica del muestreador, con validacion cadaverica y clinica. **TERCERA lectura independiente, y la mas critica: Ziran sostiene que ese landmark esta mal atribuido** (*"was in actuality the tangential projection of cortical bone around the sacroiliac joint"*, p. 352). Si la tesis usa el alar slope, tiene que resolver este desacuerdo. **Sube de urgencia.** **CUARTA lectura independiente: Moed la cita como fuente de los 5 pacientes con dismorfismo en quienes el tornillo se coloco con seguridad en S2, y rotula el alar slope como landmark operativo en su Figura 2** | 2 | PENDIENTE |
| Xu R, Ebraheim NA, Robke J, et al: Radiologic evaluation of iliosacral screw placement. Spine 21:582-588, 1996 | hinsche2002fluoroscopy (ref. 31), **kaiser2014dysmorphism (ref. 26)**, **ziran2007fluoroscopic (ref. 12)** | Metodo de evaluacion radiologica de la colocacion iliosacra; competidor o complemento de la definicion de BFC medida sobre imagen, y contraparte del "pitfall" que denuncia Ebraheim 1993. **TERCERA lectura independiente** | 2 | PENDIENTE |
| Gautier E, Baechler R: Transcutaneous screw placement for Sacroiliac Joint Fixation: A Feasibility Study. Proceedings of the Fourth International Symposium on Computer Assisted Orthopaedic Surgery. Davos, Switzerland 12, 1999 | hinsche2002fluoroscopy (ref. 6) | Fuente citada de la recomendacion de usar solo tornillos de 4.5 mm en S2. Es una restriccion de DIAMETRO dependiente del nivel vertebral: si se confirma, el muestreador no puede tratar S1 y S2 con el mismo banco de geometrias. **Aviso 2026-09-08: la version en revista (Gautier 2001, Clin Orthop 393:310-317) esta registrada en la seccion "de la lectura de Moed" con la misma recomendacion.** Auditar esa primero | 2 | PENDIENTE |
| Leighton RK, Lammens P: Percutaneous ilio-sacral screws, radiographic evaluation and cadaveric dissection: Are they safe? Proceedings of the Orthopaedic Trauma Association 14th Annual Meeting, USA 321, 1998 | hinsche2002fluoroscopy (ref. 12) | Una de las dos fuentes citadas para "el area admite dos tornillos de 7.3 mm": cota superior de ocupacion del corredor. Solo es resumen de congreso, acceso probablemente dificil | 3 | PENDIENTE |
| Ferrero, A.; et al. Technical note: insertion of digital lesions in the projection domain for dual-source, dual-energy CT. Med. Phys. 2017, 44(5), 1655-1660 | ren2022metalinsertion | Fuente original del marco de insercion en dominio de proyeccion que `ren2022` extiende. Antecedente aun mas antiguo de la insercion sintetica (implicancia #9) | 2 | PENDIENTE |
| Chen, B.; et al. Lesion insertion in the projection domain: methods and initial results. Med. Phys. 2015, 42(12), 7034-7042 | ren2022metalinsertion | Segunda fuente base del pipeline de insercion; define el estandar de validacion "insertar y comparar contra el real", que es un protocolo directamente reutilizable | 2 | PENDIENTE |
| De Man, B.; et al. Metal streak artifacts in X-ray computed tomography: a simulation study. IEEE Trans. Nucl. Sci. 1999, 46(3), 691-696 | ren2022metalinsertion, karageorgos2024ddpm | Fuente clasica de los mecanismos fisicos (photon starvation, beam hardening, bandas oscuras) y de la contribucion Compton. Cuestiona el supuesto de dispersion despreciable de `ren2022`, que es donde cuelga la frase que sostiene el gap | 2 | **LEIDO** -> `deman1999.md` |
| Choi, D.; Yun, S.; Hyun, S.; Cho, S. Metal artifact reduction algorithm with conditional latent diffusion model for dental cone-beam CT. J. Appl. Clin. Med. Phys. 2025, 26, e70317 | yun2026simulationdriven | LDM **condicional** aplicado a artefactos metalicos, del mismo grupo. Precedente metodologico directo del renderizador; toca el reclamo de novedad (implicancia #9) | 2 | PENDIENTE |
| Fan, F.; Ritschl, L.; Beister, M.; et al. Simulation-driven training of vision transformers enables metal artifact reduction of highly truncated CBCT scans. Med. Phys. 2021, 51(5), 3360-3375 | haneda2025aapm | Otro caso de entrenamiento guiado por simulacion de artefacto metalico. Suma a la implicancia #9 | 3 | PENDIENTE |
| Hu, Q.; Chen, Y.; Xiao, J.; et al. Label-free liver tumor segmentation. CVPR 2023 | chen2024tumorsynthesis | Sintesis basada en modelo, no aprendida: es la alternativa analitica dentro del paradigma de sintesis de lesiones, y el unico baseline generativo de DiffTumor. Util para encuadrar "generativo vs analitico" | 2 | LEIDA 2026-09-16 -> `hu2023.md` (#72) |
| R. Machacek, L. Mozaffari, Z. Sepasdar, S. Parasa, P. Halvorsen, M. A. Riegler, and V. Thambawita, "Mask-conditioned latent diffusion for generating gastrointestinal polyp images," arXiv preprint arXiv:2304.05233, 2023 | zhang2025diffboost (ref. [24]) | LDM condicionado por mascara para datos de segmentacion. Sirve para comprobar si la familia "inpainting acotado" de `main.tex:48` esta bien delimitada (#56): hay que ver si genera solo dentro de la mascara o la imagen completa | 3 | LEIDA 2026-09-16 -> `macháček2023.md` |
| Z. Dorjsembe, H.-K. Pao, and F. Xiao, "Polyp-DDPM: Diffusion-based semantic polyp synthesis for enhanced segmentation," arXiv preprint arXiv:2402.04031, 2024 | zhang2025diffboost (ref. [41]) | Sintesis semantica condicionada para aumentar datos de segmentacion; misma comprobacion de la frase de `main.tex:48` (#56) | 3 | LEIDA 2026-09-16 -> `dorjsembe2024.md` |
| Z. Dorjsembe, H.-K. Pao, S. Odonchimed, and F. Xiao, "Conditional diffusion models..." (ref. [35] de `zhang2025diffboost`, Refs., p. 3682; titulo completo por copiar del PDF) | zhang2025diffboost (ref. [35], version IEEE TMI) | Med-DDPM: sintesis semantica **3D** condicionada por mascara. DiffBoost le atribuye *"improving segmentation accuracy from 65.31% to 66.75% in terms of Dice score"* (§II-B, p. 3672); esa es una cifra ajena, no citable desde aqui. Es el unico de la familia que trabaja en 3D, como el renderizador (2.5D). Sirve para la misma comprobacion de #56: ver si genera solo dentro de la mascara o el volumen entero. La primera lectura de DiffBoost lo habia descartado en bloque ([20]-[40]); se rehabilita por la regla "ya intento algo parecido" | 3 | PENDIENTE (2026-09-15) |
| Lin, W.-A.; et al. DuDoNet: dual domain network for CT metal artifact reduction. CVPR 2019 | ren2022metalinsertion, wang2025adaptiveweighting (ref. 1) | Consumidor tipico de datos sinteticos de metal; util para definir el protocolo de datos de la tarea aguas abajo. `wang2025adaptiveweighting` lo cita ademas como una de las dos fuentes del umbral de 2500 HU con que segmenta la mascara metalica | 3 | **LEIDO** -> `lin2019.md` |

| Lee PY, Lai JY, Hu YS, et al. Virtual 3D planning of pelvic fracture reduction and implant placement. Biomed Eng Appl Basis Commun 2012;24(03):245-262 | liu2021ctpelvic1k | Planificacion virtual 3D de colocacion de implante en fractura pelvica: tercer competidor directo del muestreador, junto a `liu2025pipeline` y Goerres | 2 | PENDIENTE |
| Day AC, Stott PM, Boden BP. The accuracy of computer-assisted percutaneous iliosacral screw placement. Clin Orthop Relat Res. 2007;463:179-186 | zwingmann2009navigated (ref. 8) | Tasa de perforacion cortical en cadaver (2 de 10 tornillos); baseline experimental de exactitud iliosacra | 2 | PENDIENTE |
| Goldberg BA, Lindsey RW, Foglar C, et al. Imaging assessment of sacroiliac screw placement relative to the neuroforamen. Spine 1998;23:585-589 | zwingmann2009navigated (ref. 12) | Metrica de posicion relativa al neuroforamen: posible componente de SAP que hoy no existe | 2 | PENDIENTE |
| Tile M, Pennal GF. Pelvic disruption: principles of management. Clin Orthop Relat Res. 1980;151:56-64 | zwingmann2009navigated (ref. 29), hinsche2002fluoroscopy (ref. 26) | Clasificacion Tile/Pennal B y C usada como criterio de inclusion; define la poblacion anatomica sobre la que el muestreador deberia operar | 3 | PENDIENTE |
| CT Metal Artifact Reduction (CT-MAR): An AAPM Grand Challenge. aapm.org/GrandChallenge/CT-MAR/ | peters2025hybrid (ref. 35) | Fuente institucional de la definicion oficial de las metricas. **Contiene el mapeo a la escala 0-4 que NO esta en el PDF de `peters2025hybrid`**; imprescindible si se cita la escala | 2 | **CUBIERTA** por `haneda2025aapm` (articulo del reto, leido). Las filas de GitHub (scoring y FBP) siguen aparte |
| FitzGerald P, et al. Semiempirical, parameterized spectrum estimation for x-ray computed tomography. Med Phys 2021;48(5):2199-2213 | wu2022xcist | Fuente original del modelo de espectro de XCIST y del unico rango validado (80-140 kV). Necesaria si se reimplementa el brazo fisico (implicancia #8) | 2 | PENDIENTE |
| Abadi E, et al. DukeSim: A Realistic, Rapid, and Scanner-Specific Simulation Framework in Computed Tomography. IEEE TMI 2019;38(6):1457-65 | wu2022xcist | Simulador competidor scanner-specific. Si XCIST no sirve como brazo de comparacion (#8 agravada), este es el reemplazo mas obvio | 2 | LEIDA 2026-09-16 -> `abadi2019.md` (validado sin metal: no reemplaza a Peters) |
| Isensee F, Jager PF, Kohl SA, et al. Automated design of deep learning methods for biomedical image segmentation (nnU-Net). arXiv:1904.08128 | liu2021ctpelvic1k | Es la arquitectura exacta del baseline downstream de CTPelvic1K. Imprescindible para el Objetivo 5: sin ella no hay contra que comparar Dice | 2 | LEIDO (2026-09-14) en su version publicada, Nature Methods 2021 (`isensee2021`, ficha `isensee2021.md`); una primera lectura se hizo sobre este preprint. El Objetivo 5 esta fuera de alcance: hoy se cita porque TotalSegmentator se basa en nnU-Net |
| Bilic et al., LiTS (ref. 18 de `isensee2021`; cita completa por copiar del PDF) | isensee2021 | El articulo de nnU-Net lo cita junto al postprocesado por componentes conexas: posible precedente publicado de limpiar componentes, que hoy falta para la regla F (#55). Encaje dudoso: puede ser solo el reto, no la regla | 3 | PENDIENTE |
| Heller et al., KiTS19 (ref. 25 de `isensee2021`; cita completa por copiar del PDF) | isensee2021 | Idem: citado junto al postprocesado por componentes conexas; posible precedente de la regla F | 3 | PENDIENTE |

## Prioridad media — marco anatomico y pose

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Tsumura et al. 2005 (simulacion de colocacion optima con tolerancia de 5 grados) | vanbosse2011pelvicpositioning | Simula colocacion optima con una tolerancia angular explicita; compite conceptualmente con el muestreador y da un umbral de tolerancia citable | 2 | PENDIENTE |
| Lembeck et al. 2005 (el tilt pelvico degrada la navegacion de implantes) | vanbosse2011pelvicpositioning | El caso mas cercano a malposicion causada por error de referencia; conecta el marco de coordenadas con la tasa de malposicion, que es el benchmark del minimo viable. **2026-09-08: refuerzo desde Ziran**, que declara *"there are in vivo variations in the actual pelvic tilt"* como limitacion de sus propios angulos (Discusion, p. 354) | 2 | PENDIENTE |
| McKibbin 1970 (definicion de posicion anatomica pelvica) | vanbosse2011pelvicpositioning | Define el marco anatomico operacionalizado con landmarks oseos visibles en CT (sinfisis y ambas EIAS). Solo importa si se decide reportar la pose en marco anatomico y no en el marco del CT. **2026-09-08: Ziran usa el MISMO marco** (*"the two anterior-superior iliac spines and the pubic symphysis"*, p. 348), asi que hay al menos dos fuentes independientes para esa definicion | 3 | PENDIENTE |

## Snowballing de la ronda de McLaren-geometria (2026-09-08) — NINGUNO SE PERSIGUE

Salen de las 7 lecturas de esta ronda. Se registran por la regla 15 de `CLAUDE.md`.
**Recomendacion del asesor: ninguno se lee.** La ronda mostro saturacion: las fuentes
nuevas ya no cambian decisiones, solo anaden una definicion mas de diametro. Quedan
aqui para que nadie los reproponga como si fueran hallazgos frescos.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Wagner D, Kamer L, Rommens PM, Sawaguchi T, Richards RG, Noser H. 3D statistical modeling techniques to investigate the anatomy of the sacrum, its bone mass distribution, and the trans-sacral corridors. J Orthop Res 2014;32:1543-1548 | wagner2017 (ref. 16), grass2016 (ref. 39) | Es el metodo al que `wagner2017` remite para su PCA (*"as previously described"*): sin el, ese modelo de forma no es reimplementable. Ademas modela distribucion de masa osea, vecina del mapa de densidad del muestreador | 2 | PENDIENTE — no perseguir |
| Mendel T, Radetzki F, Wohlrab D, Stock K, Hofmann GO, Noser H. CT-based 3-D visualisation of secure bone corridors and optimal trajectories for sacroiliac screws. Injury 2013;44:957-963 | grass2016 (ref. 23) | **Compite directamente con el muestreador**: corredores 3D y trayectorias optimas sobre CT. Es la version 3D del triangulo de `mendel2011`. El unico candidato de la ronda que cumple la regla de "metodo que compite" | 2 | PENDIENTE — no perseguir |
| Mendel T, Appelt K, Kuhn P, Suhm N. Bony sacroiliac corridor. A virtual volume model for the accurate insertion of transarticular screws. Unfallchirurg 2008;111:19-26 | mendel2011, wagner2017 (ref. 20) | Modelo de VOLUMEN del corredor, no un escalar: definicion alternativa a Dmax. En aleman; acceso probablemente parcial | 3 | PENDIENTE — no perseguir |
| Gras F, Hillmann S, Rausch S, Klos K, Hofmann GO, Marintschev I. Biomorphometric analysis of ilio-sacro-iliacal corridors for an intra-osseous implant to fix posterior pelvic ring fractures. J Orthop Res 2015;33:254-260 | grass2016 (ref. 11) | Misma escuela y mismo metodo que `grass2016`, un ano antes, sobre corredores ilio-sacro-iliacos. Candidato a duplicar geometria ya obtenida | 3 | PENDIENTE — no perseguir |
| Noojin FK, Malkani AL, Haikal L, et al. Cross-sectional geometry of the sacral ala for safe insertion of iliosacral lag screws: a computed tomography model. J Orthop Trauma 2000;14:31-35 | lee2014 (ref. 9), mendel2011, hasenboehler2011 (ref. 31) | Geometria de seccion del ala sacra por CT. **Tres lecturas independientes lo citan**, lo que lo hace el segundo nodo de convergencia de la ronda despues de Carlson | 3 | LEIDO 2026-09-17 (ver fila de Noojin arriba) |
| Conflitti JM, Graves ML, Chip Routt ML Jr. Radiographic quantification and analysis of dysmorphic upper sacral osseous anatomy and associated iliosacral screw insertions. J Orthop Trauma 2010;24:630-636 | lee2014 (ref. 6), zhao2012 | Cuantificacion radiografica de anatomia sacra dismorfica. **Su eje es el fenotipo, que la tesis dejo fuera por #27**: se registra por trazabilidad, no por utilidad | 3 | PENDIENTE — no perseguir |
| Routt ML Jr, Simonian PT, Agnew SG, Mann FA. Radiographic recognition of the sacral alar slope for optimal placement of iliosacral screws. J Orthop Trauma 1996;10:171-177 | lee2014 (ref. 3), mendel2011, hasenboehler2011 (ref. 9) | Reconocimiento del alar slope como landmark. Tres citas independientes, pero es reconocimiento radiografico 2D, no geometria en el marco del CT: mismo limite que ya tuvo Ziran | 3 | PENDIENTE — no perseguir |
| Gardner MJ, Chip Routt ML. Transiliac-transsacral screws for posterior pelvic stabilization. J Orthop Trauma 2011;25:378-384 | zhao2012 | Describe la tecnica transiliaco-transsacra que la tesis modela geometricamente. Aportaria criterios clinicos de colocacion, no geometria | 3 | **LEIDO 2026-09-18** -> `gardner2011transiliac-transsacral.md`: criterio de viabilidad cualitativo, sin umbral en mm; la frase que Kaiser le atribuye NO esta en el PDF (#84) |

**Descartados en el filtrado de esta ronda** (para que no se vuelvan a proponer):
Huang 2006 (free form deformations), Sud 2006 (distance fields) y Baerentzen 2002
(signed distance fields), las tres piezas tecnicas que faltan para reimplementar
`gottschling2009`: **no se persiguen porque Gottschling resulto ser de femur y tibia**,
asi que reimplementarlo no da la medicion sacra (#32). Murdoch 2002, Hudson 2006 y
Yoshioka 1987: metodos manuales de medicion osea, contexto general. Konin y Walz 2010
(clasificacion LSTV): revision radiologica, y la variacion anatomica que describe el
muestreador la mide directamente. Van Zwienen 2004 y Vanderschot 2001: ya estaban
descartadas como comparaciones biomecanicas. Reilly 2006 (J Orthop Trauma 20(1
Suppl):S37-43) que cita `hasenboehler2011` **puede no ser la misma referencia** que la
Reilly 2003 17(2):88-94 ya registrada desde Kaiser; discrepancia anotada, sin decidir.


**Snowballing de `ebraheim1997` (2026-09-08).** Siete referencias citadas; **una sola
cumple las reglas y merece nombrarse**:

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Morse BJ, Ebraheim NA, Jackson WT, et al. Preoperative CT determination of angles for sacral screw placement. Spine 1994;19:604-7 | ebraheim1997 (ref. 14) | **Es, por titulo, exactamente el hueco que queda abierto tras siete lecturas: angulos para colocacion de tornillo sacro determinados sobre TC preoperatoria.** Ninguna fuente de la linea ha dado un angulo en el marco del CT. Si alguna cosa justificaria reabrir la busqueda despues de los experimentos, es esta | 2 | PENDIENTE — candidata unica de reapertura |

Las otras seis (Asher 1986, Ebraheim 1994, Esses 1991, Mickovic 1991, Miller 1993,
Steinmann 1990) son antropometria sacra general, tecnica percutanea guiada por TC o
valoracion radiografica de colocacion: **no se proponen**, por la misma razon por la que
se cerro la linea. Quedan listadas aqui para que nadie las reproponga como hallazgo nuevo.

## Reglas para proponer un candidato

Solo se propone si cumple al menos una:
- Es la fuente original de una cifra, escala o umbral que yo pienso citar.
- Es un metodo que compite directamente con el muestreador o el renderizador.
- Reporta la tasa clinica de malposicion o de brecha cortical.
- Define una metrica que podria reemplazar o validar SAP, BFC o ISC.
- Cualquier trabajo que pudiera hacer que mi gap sea MENOR de lo que afirmo,
  que ya haya intentado algo parecido, o que contradiga alguno de mis supuestos.
  Estos son los candidatos MAS importantes, no los menos.

No se proponen papers "de contexto general" ni surveys adicionales.

## Descartados en el filtrado (para que no se vuelvan a proponer)

Las 10 lecturas arrojaron mas de 60 referencias. Se descartaron por la regla de
"contexto general o survey": revisiones de estado del arte (Moolenaar 2022,
Gjesteby 2016, Stradiotti 2009), fuentes metodologicas genericas (SSIM de Wang 2004,
DDIM de Song 2021, VQGAN de Esser 2021, RePaint, Palette, escala Likert), baselines
de MAR ya cubiertos por `selles2024marreview` (NMAR de Meyer 2010, DICDNet,
InDuDoNet+, O-MAR, Huang 2015), y datasets alternativos que no reemplazan a
CTPelvic1K (DeepLesion, AbdomenAtlas-8K, LDCT-and-Projection-data).

Excepcion: **NMAR (Meyer et al. 2010)** aparecio en tres lecturas y es el ancla de
calibracion de la escala 0-4 del reto AAPM (NMAR = 2). Si se adopta ese protocolo de
evaluacion (implicancia #8, opcion 3), deja de ser contexto y pasa a ser
imprescindible. Queda anotado aqui, no en la tabla, hasta que esa decision se tome.

Segunda excepcion anotada, sin promover (2026-09-08): **DICDNet (H. Wang et al.,
IEEE TMI 41(4):869-880, 2022)** esta descartado como baseline de MAR, pero
`wang2025adaptiveweighting` lo cita como una de las dos fuentes del umbral de
**2500 HU** para segmentar la mascara metalica (*"consistent with [1] and [2], the
metal mask is empirically segmented based on the thresholding of 2500HU"*, Sec. V-E,
p. 2422). Si la tesis adopta ese umbral para definir la mascara del implante, DICDNet
deja de ser baseline descartado y pasa a ser fuente de un umbral. Decision de la
autora; no se agrega a la tabla por respetar el descarte previo.

Tercera excepcion, esta si promovida (2026-09-08): **Moed BR, Geer BL 2006** figuraba
en el bloque "series de resultados de fijacion (... Moed 2006/2007/2010)" descartado
tras leer McLaren. La lectura de Kaiser le da un rol nuevo: es una de las tres
referencias a las que Kaiser atribuye el umbral de 10 mm. Se agrego a la tabla de
"el origen REAL del umbral de 10 mm" con nivel sugerido 1 y aviso explicito del
descarte previo. Decision final de la autora.
**Cierre 2026-09-08: la rehabilitacion estaba justificada.** Se leyo el PDF
(ficha `moed2006s2screw.md`) y el paper si contiene el numero, aunque de otra magnitud.
El descarte de McLaren ("serie clinica sin geometria reutilizable") era correcto en
cuanto a geometria e incorrecto en cuanto a umbral. **Leccion registrada: un descarte
por tipo de estudio no cubre el rol de "fuente de una cifra".**

Cuarta excepcion, tambien promovida (2026-09-08, tras leer Ziran): **Carlson DA,
Scheid DK, Maar DC, et al. 2000, el "vestibule" concept**, figuraba en el bloque de
descartados de McLaren ("Carlson 2000"). Ziran lo cita como fuente de una definicion
geometrica propia de colocacion segura para S1 y S2, rol que si cumple la regla de
proposicion. Se agrego a la seccion "de la lectura de Ziran" con nivel sugerido 1 y
aviso del descarte previo. Mismo tratamiento que Moed 2006. Decision de la autora.
**Refuerzo 2026-09-08, tras leer Moed:** segunda cita independiente, y Moed le atribuye
explicitamente el menor margen de error en S2 y el aumento del espacio S2 en sacros
dismorficos, medidos por CT en 30 voluntarios sanos. La rehabilitacion se confirma.

De la lectura de `wang2025adaptiveweighting` (2026-09-08) se descartaron ademas, por
la regla de "contexto general o baseline de MAR ya cubierto": las lineas base
clasicas LI (Kalender 1987), FSMAR (Meyer 2012) y NLSMAR (Anhaus 2022), el backbone
MAIL (Zhang 2024), el dataset DeepLesion (Yan 2018), y todo el bloque de
meta-learning y optimizacion (MAML, L2RW, Meta-Weight-Net, DARTS, Frank-Wolfe,
minimax, hypergradient descent), que son fuentes metodologicas genericas.

De la lectura de `hinsche2002fluoroscopy` (2026-09-08) se descartaron por la misma
regla las referencias de congreso sobre navegacion asistida por computador que no
aportan cifra, escala ni competencia directa (Amstutz y Nolte 1999, Berlemann 2000,
Gruetzner 2000, Kahler 2000, Stoeckle 2000, Suhm 2000, Tonetti 1998, Cogley 1998),
los trabajos de monitoreo neurofisiologico intraoperatorio (Venables 1995,
Vrahas 1992) y las fuentes anatomicas o clinicas generales de fijacion pelvica
(Jackson 1993, Matta 1989, Miller 1993, Reilly 2000, Routt 1995, Routt 1996 closed
reduction, Duwelius 1992, Waldrop 1993, Tile 1988, Stafford 1999).

De la lectura de `mclaren2021corridor` (2026-09-08) se descartaron por la misma regla
las referencias clinicas o biomecanicas sin geometria reutilizable: series de
resultados de fijacion (Tornetta 1996, Routt 1995 y 2000, Griffin 2006, Rysavy 2010,
Moed 2006/2007/2010, Shuler 1995, Gautier 2001, Altman 1999, McLaren 1991,
Carlson 2000, Nork 2001), comparaciones biomecanicas (van Zwienen 2004, Tabaie 2013,
Min 2014, Schildhauer 1998 y 2003, Sagi 2009, Toogood 2013), clasificaciones y
capitulos generales (Kellam 1987 y 1995, Smith 2010) y descriptores de dismorfismo
sin geometria de corredor (Karachalios 2010, Mahato 2010, Konin 2010, Conflitti 2010,
Vanderschot 1999). La ref. 21 de McLaren (Smith HE et al. 2006) ya esta en `refs.bib`
como `smith2006iliosacral`: no es candidato nuevo.
**Aviso 2026-09-08: "Carlson 2000" de esta lista queda promovido, ver la cuarta
excepcion. "Moed 2006" queda promovido y ya LEIDO, ver la tercera. Y "Gautier 2001"
de esta misma lista queda promovido tras leer Moed**, por ser la fuente de la
recomendacion de no pasar de 4.5 mm en S2 (restriccion de diametro por nivel sacro).

De la lectura de `kaiser2014dysmorphism` (2026-09-08) se descartaron por la misma
regla: las series clinicas y de complicaciones sin geometria ni umbral reutilizable
(Enninghorst 2010, Gardner 2009, Cole 1996, Moed 2006 S2 —promovido aparte, ver la
tercera excepcion—, Routt 1995, Schweitzer 2008, Shuler 1995, Pohlemann 1994,
Tile 1996, Griffin 2006, Sagi 2005, Altman 1999, Ko 2001, Peeters 2010, Weil 2007,
Reilly 2000, Griffin 2003, Routt 1995 supine), la fuente metodologica generica del
kappa (Landis y Koch 1977) y del analisis de componentes principales (Abdi y
Williams 2010, Jackson 1993), la de malrotacion del arco en C (Wolinsky y Lee 2007)
y los descriptores de dismorfismo ya descartados en la ronda de McLaren
(Karachalios 2010, Conflitti 2010). Las refs. 28 y 30 de Kaiser caen en ese ultimo
bloque. Las refs. 4, 29 y 37 estan promovidas a nivel 1 arriba; las refs. 18, 21, 23,
26, 27, 31 y 36 tienen fila propia.
**Aviso 2026-09-08: "Griffin 2003" de esta lista queda promovido tras leer Moed**, que
la usa como su contraste clinico principal (4 fallos de fijacion de 62 pacientes, con
distribucion por nivel sacro). Mismo patron que Moed y Carlson: un descarte por tipo de
estudio no cubre el rol de "serie con conteos por nivel".

De la lectura de `ziran2007fluoroscopic` (2026-09-08) se descartaron por las mismas
reglas, sobre sus 25 referencias: las series clinicas y capitulos generales de
fijacion pelvica (Matta y Saucedo 1989, Routt 1995, Routt 1996 closed reduction,
Routt 1996 U-shaped, Baque 2005, Resnik 1992, Tile 1995 libro), la fijacion guiada
por CT en quirofano sin geometria reutilizable (Nelson y Duwelius 1991), el bloque de
monitoreo neurofisiologico intraoperatorio ya descartado en la ronda de Hinsche
(Moed 1998, Webb 2000), el libro de acetabulo de LeTournel y Judet 1981 (usado solo
como analogia metodologica de colocacion de marcadores) y McCollum y Gray 1990, que es
luxacion tras artroplastia total de cadera y no toca el anillo pelvico posterior. La
ref. 20 (Tonetti 1998) ya estaba descartada en la ronda de Hinsche. Las refs. 5, 7,
12, 15, 19 y 21 ya tenian fila y solo se les anadio la referencia cruzada; las refs.
11, 13, 16, 17, 18 y 25 tienen fila nueva.

De la lectura de `moed2006s2screw` (2026-09-08) se descartaron por las mismas reglas,
sobre sus 23 referencias: las series y capitulos generales de fijacion del anillo
pelvico ya descartados en rondas anteriores (Cole 1996, Matta y Saucedo 1989,
Routt y Simonian 1996 closed reduction, Kellam 1995, y el capitulo de libro de
Moed 2003), la clasificacion institucional (OTA Fracture and Dislocation Compendium
1996, equivalente a la fila ya existente de Tile/Pennal), el bloque completo de
monitoreo neurofisiologico intraoperatorio ya descartado en la ronda de Hinsche
(Moed 1998 modelo animal, Moed 1998 JBJS estudio clinico, Moed 1999 modelo animal,
Ricci 2003 sobre la posicion del anodo, y la carta al editor de Moed 2003) y las
comparaciones biomecanicas ya descartadas en la ronda de McLaren (van Zwienen 2004,
Yinger 2003). Sus refs. 2, 8, 11, 13, 22 y 23 tienen fila propia o promocion; las
refs. 7, 9, 10 y 12 ya tenian fila y solo se les anadio la referencia cruzada.

### Descartes de la lectura de xie2024implantsegmentation (2026-09-11)

De la lectura de `xie2024implantsegmentation` (2026-09-11), sobre sus 62 referencias:
**InDuDoNet+ (Wang H et al., Med Image Anal 2023;85:102729, ref. 8)** es una de las tres
fuentes del 2500 HU en Xie, pero ya estaba descartada como baseline de MAR. Se anota sin
promover, igual que DICDNet (segunda excepcion). **Zhang Y, Yu H 2018 (ref. 50)** ya tiene fila
(l. 102). Es ademas la fuente de las 100 mascaras de Xie; conviene anadir la referencia cruzada
`xie2024implantsegmentation (ref. 50)` a esa fila. **NMAR (Meyer 2010, ref. 3)** entra en la
excepcion ya anotada. **CTPelvic1K (ref. 48)** ya es `liu2021ctpelvic1k`. Por la regla de
"contexto general" se descartan: segmentacion de metal por procesado de imagen sin cifra ni
metrica reutilizable (Pauwels 2014, Chen 2012, Karimi 2012, Bal 2006), segmentacion de metal
en proyeccion dental (Hegazy 2019), MAR generico (Chang 2018, Mehranian 2013, Zhang 2011,
Jeong 2009, Prell 2010, Wang 2010, Zhang 2007, Arabi 2021, Agrawal 2023, Wang 2019 coclear,
DAN-Net 2021), arquitecturas y muestreadores genericos (DDPM, LDM, MedSegDiff, U-Net,
Attention U-Net, R2U-Net, DeepLab, DPM-Solver, SegDiff/ensembles/Guo 2023, TriDo-Former) y el
bloque de refs. 19-34 y 57-62 (aplicaciones de DL ajenas a CT de metal).

### Descartes de la lectura de zhang2025diffboost (2026-09-15, version IEEE TMI)

De sus 56 referencias se proponen solo Machacek [24], Med-DDPM [35] y Polyp-DDPM [41] (tabla
"compiten con un componente"). **DiffuseExpand (S. Shao, X. Yuan et al., ref. [36])** se descarta
por la regla de "contexto general": es expansion generica de datasets 2D para segmentacion, sin
mascara acotada ni condicionamiento que ponga a prueba la frase de #56, y sin CT de metal. ControlNet
(`zhang2023controlnet`) y LDM (`rombach2022latentdiffusion`) ya estan en `refs.bib`. El resto del bloque
[20]-[40] y las fuentes metodologicas genericas quedan descartadas como se indica en la ficha.

### Candidatos de AUTOENCODER, abiertos por el resultado de E6b (2026-09-15, ronda (7))

E6b midio que el VAE de SD 1.5 sin reentrenar falla el Go/No-Go de hueso en 178/178 (#36/#39).
El autoencoder deja de ser "contexto general" y pasa a ser la decision que bloquea el Objetivo 1.
Estas dos filas salen de PDFs ya leidos; no se busco nada fuera.

| Referencia | De donde sale | Por que puede importar | Prio | Estado |
|---|---|---|---|---|
| Zheng C, Vedaldi A. Online clustered codebook. IEEE Int. Conf. Comput. Vis. pp. 22741-22750, 2023 | `yun2026simulationdriven` (ref. 23) | **Es el CVQ-VAE que usa MLD-MAR**, el unico modelo latente del corpus con cifra de HU medida: RMSE 12.74 (σ=5.36) en sintetico (Tabla 1, p.10) y 21.01 en ROI clinico libre de artefacto (Tabla 3, p.11). Su latente es *"× 4 down-sampled"* (Sec. 2.3.1, p.4), frente al factor 8 de SD 1.5: razon mecanica concreta para esperar menos perdida. **Candidato principal de la opcion 3 de #36/#39** | 1 | PENDIENTE (2026-09-15) |
| Esser P, Rombach R, Ommer B. Taming transformers for high-resolution image synthesis. CVPR 2021 | `chen2024tumorsynthesis` (ref. 22) | VQGAN que DiffTumor adapta a 3D y entrena en 9.262 CT (§3.1, p.4), con latente a 1/4 en alto, ancho y profundidad (Apendice E.2, p.21). **Estaba DESCARTADO** como "fuente metodologica generica" en el filtrado de las 10 lecturas; E6b lo rehabilita, igual que la excepcion de NMAR. Aviso: la ficha de DiffTumor ya advierte que ese autoencoder **nunca vio el rango del metal** y que no publica cifra de fidelidad en HU | 2 | PENDIENTE (2026-09-15) |

Ya estaba en la tabla y sube de prioridad por el mismo motivo: **Choi et al. 2025** (LDM condicional
para CBCT dental, del grupo de `yun2026simulationdriven`).

**Lo que NINGUNA fuente del corpus reporta:** el error de ida y vuelta de un autoencoder solo,
en HU, sobre CT oseo. Todas las cifras de arriba son de tuberia completa contra ground truth.
Es exactamente lo que mide E6b, y por eso no hay con que compararlo de frente.

### Busqueda WEB de benchmarks de autoencoders en CT (2026-09-15, orden explicita de la autora)

**Excepcion declarada al flujo normal.** Estas filas NO salen de un PDF ya leido: salen de una busqueda web
autorizada por la autora para resolver la opcion 3 de #36/#39. **Ninguna entro a `refs.bib`** (regla 9: la
lista la define la autora y empieza por pegar el archivo en `refs/raw/`). Los datos de abajo vienen del
abstract o de la version HTML, no de una lectura con `lector-papers`: **estan SIN VERIFICAR** y ninguna cifra
de aqui puede ir a la tesis todavia.

| Referencia | De donde sale | Por que puede importar | Prio | Estado |
|---|---|---|---|---|
| Chen Q, Ding S, Gu Y, Liu N, Bian J, Yuille A, Zhou Z, Fu J. "Foundation VAEs for 3D CT Reconstruction, Augmentation, and Generation". ICML 2026. arXiv:2605.30893 | Busqueda web 2026-09-15 | **El paper mas cercano a E6b que existe.** Prueba **siete VAE de video genericos congelados** (WAN2.1, WAN2.2, VideoVAE+, IVVAE, CVVAE, WFVAE, LeanVAE) como interfaz de CT *"without medical fine-tuning"*. Es la pregunta de E6b con respuesta contraria. **Diferencia critica que hay que auditar:** recortan la intensidad a **[-1000, 1000] HU**, rango que **excluye el hueso denso y todo el metal**; el Objetivo 1 vive justo fuera de ese recorte. Reportan PSNR 30.93 (pulmon) y 39.18 (pancreas) y MSE 77.97 / 8.58, con la unidad sin confirmar. Compresion 8x8x4 o 16x16x4 | 1 | LEIDA 2026-09-16 -> `chen2026foundationvae.md` (#65, #66) |
| Shi J, Pelt DM, Batenburg KJ. "DM4CT: Benchmarking Diffusion Models for Computed Tomography Reconstruction". arXiv:2602.18589, 2026 | Busqueda web 2026-09-15 | Benchmark de modelos de difusion para CT. **Valor principal: confirma el hueco de #36/#39 por la negativa.** No separa la calidad del autoencoder de primera etapa de la tuberia completa, y declara *"we do not use Hounsfield Unit for display, as the benchmark is not intended for clinical analysis"*. Es decir, el benchmark de referencia del campo **no mide lo que mide E6b** | 2 | PENDIENTE (2026-09-15) |
| Literatura de sCT en radioterapia MR-only (MAE en HU por tejido; varios articulos, sin clave asignada) | Busqueda web 2026-09-15 | Es el **unico subcampo que publica MAE en HU con ROI de hueso separado**, que es exactamente la metrica de E6b. Las magnitudes que aparecen en los resumenes de busqueda son de **cientos de HU en hueso**, pero la tarea es sintesis MR -> CT, mucho mas dificil que una ida y vuelta: **no sirven como ancla del umbral** y por eso NO se usaron en `main.tex`. Valor real: de ahi puede salir la convencion de *como se reporta* MAE en HU por tejido. **Sin verificar, sin articulo concreto elegido** | 3 | PENDIENTE (2026-09-15) |

**Conclusion de la busqueda:** no aparecio ningun trabajo que publique el **error de ida y vuelta de un
autoencoder solo, en HU, sobre CT oseo con rango de metal**. El hueco de #36/#39 se confirma tras buscar
fuera del corpus, no solo dentro.

## Ronda 2026-09-15 — salidas de `gertzbein1990`, `ramzan2026claim`, `herman2016` y `deman1999`

Transcritas tal como las cita cada fuente. Ninguna se busco fuera del PDF donde aparece, ninguna
se descargo y ninguna se agrego a `refs.bib` (reglas 9 y 15). La autora decide LEER o DESCARTAR.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Roy-Camille R, Saillant G, Mazel C. Internal fixation of the lumbar spine with pedicle screw plating. Clin Orthop 203:7-17, 1988 | `gertzbein1990` (ref. 4) | **Unico eslabon vivo de la cadena de la escala del benchmark.** Es la fuente a la que Gertzbein atribuye el **ancla de 2 mm** (*"anatomical dissections have shown that there is 2 mm of epidural space"*). Gertzbein es terminal para los tramos de 4/6/8 mm, pero no para este. Si el 2 mm tampoco esta medido aqui, la escala entera queda como convencion, igual que paso con el umbral de 10 mm. **Aviso: es espacio epidural lumbar, no corredor iliosacro**; aunque la cadena se cierre, la magnitud sigue sin ser la que mide la tesis | 1 | PENDIENTE |
| Zhang et al. LeFusion: Controllable pathology synthesis via lesion-focused diffusion models. arXiv:2403.14066, 2024 | `ramzan2026claim` (ref. 16) | **Base declarada de CLAIM y fuente original de la composicion enmascarada** `m*generado + (1-m)*original`. CLAIM la hereda, asi que el nodo real del argumento de #56 —el que hace el streaking peri-implante imposible por construccion— esta aqui, no en CLAIM. Mismo patron de fuente secundaria que `smith2006iliosacral` y `wang2025adaptiveweighting` | 2 | PENDIENTE |
| Lugmayr et al. RePaint: Inpainting using denoising diffusion probabilistic models. CVPR 2022 | `ramzan2026claim` (ref. 19) | Origen del esquema de inpainting por difusion del que descienden CLAIM y LeFusion. Solo interesa si la autora quiere citar el ancestro del mecanismo en vez del uso medico | 3 | PENDIENTE |
| Jin et al. Free-form tumor synthesis in computed tomography images. Knowl Based Syst 218:106753, 2021 | `ramzan2026claim` (ref. 13) | **Sintesis en CT**, no en MRI: mas cercano a la modalidad de la tesis que los cuatro analogos ya leidos. Podria decir si alguien ya midio algo fuera de la mascara en CT | 2 | PENDIENTE |
| Wu et al. FreeTumor. arXiv:2502.18519, 2025 | `ramzan2026claim` (ref. 15) | Sintesis en CT, reciente. Mismo motivo que la fila anterior, con riesgo adicional de colision de encuadre | 3 | PENDIENTE |
| Zwingmann J, et al. Arch Orthop Trauma Surg 133:1257-1265, 2013 (metaanalisis de malposicion por modalidad) | `herman2016` | **Es la candidata mas fuerte de la ronda para #12.** Metaanalisis de tasas de malposicion **por modalidad de guia**, del mismo primer autor que `zwingmann2009navigated`, que es la fuente N1 del prior ordinal. Si publica distribuciones agregadas por tecnica, toca directamente el benchmark SAP y la cadena del 2%-15%. **Aviso: #12 esta CERRADA POR DELIMITACION (S1 ordinal, S2 descriptivo); esta fila no la reabre por si sola** | 1 | **LEIDO** -> `zwingmann2013.md` |
| Miller AN, Routt ML Jr. Variations in sacral morphology and implications for iliosacral screw fixation. JAAOS 20:8-16, 2012 | `herman2016` | Morfologia sacra y sus implicancias para el tornillo iliosacro. Podria aportar prevalencias o tipologia que hoy salen de `hasenboehler2011` (14.2%-14.5%) y `kaiser2014dysmorphism`. Herman ademas reporta que el dismorfismo **no** se asocio a brecha, lo que hace util contrastar | 2 | **LEIDO 2026-09-18** -> `miller2012variations.md`: review cualitativo, 7 signos de dismorfismo sin umbrales; la definicion que Kaiser le atribuye NO esta en el PDF (#84) |
| Farrell ED, et al. J Orthop Trauma 23:333-339, 2009 (tunel de raiz sacra superior, 91% de cadaveres) | `herman2016` | Estructura anatomica que limita el corredor y que ninguna fuente leida modela. Solo interesa si el muestreador llega a restringir por raiz nerviosa y no solo por cortical | 3 | PENDIENTE |
| Glover GH, Pelc NJ. Nonlinear partial volume artifacts in x-ray computed tomography. Med Phys 7(3):238-248, 1980 | `deman1999` (ref. 16) | **Cubre exactamente la causa que De Man excluye de su alcance**, y es la que mas pesa en el borde metal/hueso que esta tesis sintetiza. Candidata a ser la fuente que si cuantifique algo espacial, que es lo que `deman1999` no da (#60) | 2 | PENDIENTE |
| Joseph PM, Spital RD. The exponential edge-gradient effect in x-ray computed tomography. Phys Med Biol 26:473-481, 1981 | `deman1999` (ref. 12) | Unica fuente del EEGE, uno de los cuatro mecanismos que De Man declara mas importantes. Solo interesa si el brazo fisico necesita citar el mecanismo por separado | 3 | PENDIENTE |
| Joseph PM, Spital RD. The effects of scatter in x-ray computed tomography. Med Phys 9:464-472, 1982 | `deman1999` (ref. 10) | Idem, para scatter. De Man elige su relacion scatter-primario de forma **arbitraria** (0.0001) y aun asi produce estrias; el valor defendible estaria aqui | 3 | PENDIENTE |
| Duerinckx AJ, Macovski A. Nonlinear polychromatic and noise artifacts in x-ray computed tomography images. JCAT 3:519-526, 1979 | `deman1999` (ref. 4) | Contexto historico del beam hardening no lineal. Baja prioridad | 3 | PENDIENTE |

**Ya leidas, no son candidatas.** `herman2016` atribuye el umbral de 10 mm a *Gardner MJ et al. 2010, J Orthop
Trauma 24(10):622-629* y a *Lee JJ et al. 2015, J Orthop Res 33(2):277-82*. Las dos estan **LEIDAS**:
`gardner2010safezones.md` y `lee2014.md` (esta ultima con clave 2014 por el raw; el fasciculo impreso es 2015).
Ziran y Moed **no aparecen** en la bibliografia de Herman. La cadena del 10 mm no se reabre: sigue cerrada por
decision de la autora y adoptada como convencion geometrica.

## Ronda 2026-09-15 (2) — salidas de `zwingmann2013` y `lin2019`

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Zhang Y, Yu H. Convolutional neural network based metal artifact reduction in X-ray computed tomography. IEEE Trans Med Imaging 2018 | `lin2019` (ref. 33) | **LEIDA 2026-09-16 -> `zhang2018.md`.** **La mas rentable de esta ronda, y ya esta en el repositorio.** Es la fuente original del protocolo de simulacion de metal que DuDoNet reutiliza, con los **materiales, coeficientes de atenuacion y geometrias** que `lin2019` omite (todos NO ENCONTRADO en su PDF). Clave `zhang2018`: **PDF en `papers/`, raw en `refs/raw/` y entrada ya en `refs.bib` desde el 2026-09-15**. No hay que buscar ni descargar nada: solo mandarlo a `lector-papers` | 1 | LEIDA 2026-09-16 |
| Zwingmann J, et al. J Trauma 2010;69:1501-1506 | `zwingmann2013` (ref. 11) | Tercera cohorte del mismo autor, entra al metaanalisis como estudio numero 9 con **14/131 convencional y 1/63 navegado**, tamanos mayores que los de 2009. Si publica grados y no solo binario, seria una **segunda distribucion ordinal** y la unica via de ampliar el prior del benchmark. **Aviso: no seria independiente de las otras dos fuentes Zwingmann** (#62) | 1 | PENDIENTE |
| Templeman D, Schmidt A, Freese J, Weisman I. Proximity of iliosacral screws to neurovascular structures after internal fixation. Clin Orthop 1996;(329):194-198 | `zwingmann2013` (ref. 25) | **Segundo extremo de la banda 2%-15%, y el ultimo nodo de esa cadena sin leer.** Zwingmann 2013 la cita para *"2 to 15 %"* en la Introduccion y para *"0 to 15 %"* en la Discusion: solo el PDF dice cual es el numero real. **Ya tiene entrada en `refs.bib` desde el raw, pero NO tiene PDF en `papers/`** (estado de acceso, no descarte). Tambien se le atribuye un umbral de 4 grados | 2 | **LEIDO 2026-09-17** (ver fila de Templeman arriba): no publica 2%, 15% ni 0-15%; la cita de Zwingmann 2013 no se sostiene en la fuente (#77) |
| Konrad G, et al. Unfallchirurg 2010;113:29-35 | `zwingmann2013` (ref. 34) | Variabilidad de la posicion del tornillo tras navegacion 3D **segun la experiencia del cirujano**. Seria una covariable del muestreador que ninguna fuente leida cuantifica. En aleman | 3 | PENDIENTE |

## Ronda 2026-09-16 — salidas de `chen2026foundationvae`, `zhang2018`, `arand2019pelvicring` y `tejwani2014`

Solo pasan el filtro las que podrian contradecir un supuesto o reemplazar una cita. Datos bibliograficos tal como
los transcribio `lector-papers` desde la lista de referencias de cada PDF; no verificados contra el editor.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Guo et al. MAISI: Medical AI for synthetic imaging. WACV 2025 | `chen2026foundationvae` | **VAE entrenado en CT**, contrapunto directo a E6b y a la opcion 3 de #36/#39 (otro VAE con MAE de hueso < 25 HU). Si publica error en HU o su rango de recorte cubre hueso denso, es el candidato natural a VAE del renderizador; si recorta como Chen, refuerza #65 | 1 | PENDIENTE |
| Varma et al. MedVAE: Efficient automated interpretation of medical images with large-scale generalizable autoencoders. arXiv:2502.14753, 2025 | `chen2026foundationvae` | Autoencoder medico de 1 canal; mismo papel que MAISI para la opcion 3 de #36/#39. Chen reporta cifras contradictorias de MedVAE entre texto y tabla | 2 | PENDIENTE |
| Tonetti J, Carrat L, Blendea S, et al. Clinical results of percutaneous pelvic surgery. Computer assisted surgery using ultrasound compared to standard fluoroscopy. Comput Aided Surg 2001 | `tejwani2014` | Reporta una tasa clinica de malposicion (fuente del "24%" de Tejwani). Es la cohorte de 2001, **no** Tonetti 1998 ya descartado. Baja prioridad: el prior ordinal ya esta delimitado a Zwingmann en S1 | 3 | PENDIENTE |
| Wagner D, Kamer L, Rommens PM, et al. 3D statistical modeling techniques to investigate the anatomy of the sacrum, its bone mass distribution, and the trans-sacral corridors. J Orthop Res 2014 | `arand2019pelvicring` (tercera fuente que la cita; ya registrada arriba como "NINGUNO SE PERSIGUE") | **Cambia de estatus por #64:** es la unica candidata conocida que podria respaldar "bone mass distribution" con corredores, si la autora decide mantener una cita de densidad en `main.tex`. No se persigue sin esa decision | 2 | PENDIENTE (condicionada a #64) |

**Descartadas en el filtrado (no reproponer):** de `zhang2018`, Tang 2008 (J X-Ray Sci Technol), Kyriakou 2010
(EBHC), Elbakri & Fessler 2002, Verburg & Seco 2012, Stille 2013 y Mouton 2013: fuentes metodologicas de simulacion
o MAR, ninguna mide extension espacial del artefacto ni sintetiza; Park 2017 (arXiv 1708.00607 y 1708.00244):
remocion, ya cubierta por `lin2019`. De `arand2019pelvicring`, Noser 2011 (otro procedimiento de corredor; la ronda de
McLaren ya mostro saturacion), Kamer 2016 y Gehweiler 2017 (metodo de densidad en otros huesos), Peretz 1998 y
Ebraheim 2000 (arquitectura interna del sacro, contexto). De `tejwani2014`: Templeman 1996, Hinsche 2002 y Routt
1996 ya estan registradas o leidas.

## Ronda 2026-09-16 (2) — salidas de `fan2022`, `mirza2003`, `routt1997` y `macháček2023`

Sin filas nuevas. Vaccaro 1995 Part II ya estaba registrada (fila de `smith2006iliosacral`) y **sube a nivel 1** por
#68. Descartadas (no reproponer): de `fan2022`, sus refs. de artefactos de calcio [3], [11] (no miden extension en mm
segun el PDF) y CatSim [15] (ya leido como `deman2007catsim`); de `routt1997`, Routt 1996 J Orthop Trauma 10 (ya
registrada como "sacral alar slope"); de `macháček2023`, PolypConnect [10] y Qadir [28] (polipos, sin efectos fuera
de mascara).

## Ronda 2026-09-16 (3) — salidas de las 11 fichas faltantes y de las re-verificaciones

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Szalkowski G, Nie D, Zhu T, Yap PT, Lian J. Synthetic digital reconstructed radiographs for MR-only robotic stereotactic radiation therapy: a proof of concept. Comput Biol Med. 2021;138:104917 | `singhrao2024fiducial` (ref. 20) | Segun el lector, un GAN genera **marcadores metalicos pequenos** en imagen sintetica y se evalua con medidas de imagen y observadores: seria un intento previo de sintesis generativa de metal (regla "ya intento algo parecido"). **Sin verificar** si es CT o DRR (el titulo dice DRR) ni si modela artefacto | 2 | PENDIENTE |
| Selles et al. 2023, ref. [140] de `selles2024marreview` (cita completa: ver lista de referencias de ese PDF; no transcrita por el lector) | `selles2024marreview` | Segun el lector, **cuantifica artefactos en musculo y hueso con CT de pelvis antes y despues de fusion sacroiliaca**: anatomia e implante muy cercanos a la tesis. Si usa ROI a distancias del implante, seria la primera fuente con extension espacial (#57) | 2 | PENDIENTE (transcribir cita completa antes de todo) |

**Descartadas (no reproponer):** Geman 2015 (Visual Turing Test, metodo generico, de `hu2023`); Liao 2020 ADN (remocion no
supervisada, de `yu2021`); De Man 1998 IEEE NSS (probable version de congreso de `deman1999`, de `yu2021`); Med-DDPM (ya
registrada, de `dorjsembe2024`); Hakvoort 2020 (visibilidad cerca del metal en fantoma, de `selles2024marreview`).

## Ronda 2026-09-17 (2) — de las lecturas de `routt1997early`, `templeman1996proximity`, `noojin2000cross`, `vaccaro1995part1`, `zhu2023sinogram`

Transcritas tal como aparecen en cada PDF. Ninguna se busco fuera. Keating (ref. 5 de Routt) ya esta leida
(`keating1999iliosacral`); Shuler 1995, Routt 1996 (alar slope) y Jackson & McManus 1993 ya estaban registradas.

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Routt M, Meier M, Kregor P. Percutaneous iliosacral screws with the patient supine technique. Oper Tech Orthop 1993;3:35-45 | `routt1997early` (ref. 16) | Descripcion de la tecnica y del corredor S1 a la que remite Routt 1997 | 3 | PENDIENTE — no perseguir |
| "Mirkovic et al" = Mirkovic S, Abitbol JJ, Steinman J, et al. Anatomic consideration for sacral screw placement. Spine 1991;16:S289-S294 (cita completa desde `ebraheim2000lumbosacral`, ref. 5) | `templeman1996proximity` (ref. 9), `ebraheim2000lumbosacral` (ref. 5) | Distancias de vena iliaca interna y raices L4-L5 a la cortical anterior del ala | 3 | PENDIENTE — no perseguir |
| Krag MH, Weaver DL, Beynnon BD, Haugh LD. Morphometry of the thoracic and lumbar spine related to transpedicular screw placement for surgical spinal fixation. Spine 13:27-32, 1988 | `vaccaro1995part1` (ref. 11) | Validacion CT frente a medicion directa (segun Vaccaro, solo longitudes) | 3 | PENDIENTE — no perseguir |
| Misenhimer GR et al. Anatomic analysis of pedicle cortical and cancellous diameter as related to screw size. Spine 14:367-372, 1989 | `vaccaro1995part1` (ref. 16) | Diametro cortical vs esponjoso frente al calibre del tornillo (holgura) | 3 | PENDIENTE — no perseguir |
| H.S. Park, Y.E. Chung, J.K. Seo, Computed tomographic beam-hardening artefacts: mathematical characterization and analysis, Philos Trans A 373 (2015) | `zhu2023sinogram` (ref. 42) | Caracterizacion matematica del beam hardening; podria describir la estructura espacial del artefacto (#57: alcance espacial sin medir) | 2 | PENDIENTE |
| B. Meng, J. Wang, L. Xing, Sinogram preprocessing and binary reconstruction for determination of the shape and location of metal objects in CT, Med. Phys. 37 (2010) 5867-5875 | `zhu2023sinogram` (ref. 5) | Localizacion de metal en sinograma; limites del umbral | 3 | PENDIENTE — no perseguir |

La ref. 41 de Zhu (Zhang & Yu 2018, CNN-MAR, IEEE TMI 37:1370-1381) coincide por titulo con `refs/raw/zhang2018.nbib`: no es candidata nueva.

## Ronda 2026-09-18 — de las 13 lecturas nuevas

Transcritas tal como aparecen en cada PDF. No se repiten las que ya estaban (Carlson, Day, Goldberg, Noojin, Keating,
Amongero, Routt 1996, Mendel 2008, Tonetti 2000, Templeman-Goulet 1996, Kellam 1992, Waldrop 1993, Jackson & McManus,
Conflitti, Karachalios, Matta & Saucedo 1989, DICDNet).

| Cita (como aparece) | Salio de | Por que podria importar | Nivel sugerido | Estado |
|---|---|---|---|---|
| Ziran BH, Wason AG, Olsen S, Chapman MW. Radiographic anatomy of the iliosacral corridor. Procs Orthopaedic Trauma Association, 1996:192 | `ziran2003` (ref. 22) | Resumen de congreso; posible origen del 10 mm | 4 | PENDIENTE — no perseguir (cadena del 10 mm cerrada por decision) |
| Tornetta P, Matta J. Outcome of operatively treated unstable posterior pelvic ring disruptions. Clin Orthop 1996;329:186-193 | `reilly2003effect` (ref. 16) | Escala de desplazamiento residual (<4, <10, >10 mm); de REDUCCION, no de brecha | 3 | PENDIENTE — no perseguir |
| Ebraheim N, Coombs R, Jackson W, et al. Percutaneous computed tomography-guided stabilization of posterior pelvic fractures. Clin Orthop 1994;307:222-228 | `reilly2003effect` (ref. 3) | Desplazamiento aceptable (1 cm craneal, 5 mm posterior) para colocar el tornillo | 3 | PENDIENTE — no perseguir |
| Miller MD, Cain JE, Lauerman WC, et al. Posterior sacroiliac fixation using a sacral pedicle targeting device: an anatomic study. J Orthop Trauma 1993;7:514-20 | `xu1996projection` (ref. 15) | Tornillos que violan vena iliaca o canal (malposicion en cadaver) | 3 | PENDIENTE — no perseguir |
| Licht NJ, Rowe DE, Ross LM. Pitfalls of pedicle screw fixation in the sacrum: a cadaver model. Spine 1992;17:892-896 | `ebraheim2000lumbosacral` (ref. 4) | Estructuras anteriores al sacro; posibles distancias neurales en mm (no verificado) | 3 | PENDIENTE — no perseguir |
| Tornetta III P, Matta JM. Internal fixation of unstable pelvic ring injuries. Orthop Trans 18:727, 1994 | `mostafavi1996radiologic` (ref. 15) | Abstract de congreso; criterio de 3 corticales | 4 | PENDIENTE — no perseguir |
| Edeiken-Monroe BS, Browner BD, Jackson H. The role of standard roentgenograms in the evaluation of instability of pelvic ring disruption. Clin Orthop 240:63-76, 1989 | `mostafavi1996radiologic` (ref. 4) | Desplazamiento radiografico frente a estabilidad | 4 | PENDIENTE — no perseguir |
| M. Yazdi, L. Gingras, L. Beaulieu. An adaptive approach of metal artifact reduction in helical CT for radiation therapy treatment planning: experimental and clinical studies. Int J Radiat Oncol Biol Phys 62, 1224-1231 (2005) | `yazdi2011opposite` (ref. 14) | MAR con protesis de cadera; enfoque "adaptive" de segmentacion de metal (#87) | 3 | PENDIENTE — no perseguir |

