# Indice de literatura

Fuente unica de verdad sobre la bibliografia. Una fila por entrada de refs.bib.

**Criterio de nivel (autora, 2026-09-06):** riesgo de afectar el argumento central
o el benchmark principal.
- **Nivel 1** — critico. Si me equivoco aqui, se cae una tesis o el benchmark.
- **Nivel 2** — afecta la redaccion. Related Work, encuadre, justificacion.
- **Nivel 3** — apoyo. No amenaza nada; se cita, no se discute.

**Acceso:** COMPLETO (PDF entero) | PARCIAL | ABSTRACT | SIN ACCESO
**PDF:** si = archivo presente en `papers/` | FALTA = no esta

27 entradas en `refs.bib`, 27 filas aqui. Reparto: 8 en N1, 12 en N2, 7 en N3.
Las 10 filas que dependian de inferencia ya se verificaron leyendo el PDF, ver "Verificado contra el PDF".

## Nivel 1 — critico

| Clave | PDF | Acceso | Nota generada | Leido por mi | Que amenaza si me equivoco |
|---|---|---|---|---|---|
| zwingmann2009navigated (CONFIRMADO, ROL CORREGIDO) | si | COMPLETO | zwingmann2009navigated.md | no | **El rango 31-60% NO aparece en el PDF.** Son dos complementos derivados (69% y 40% de Grado 0) de dos brazos distintos. Aporta escala 0/<2/2-4/>4 mm y dos tasas por tecnica. Ver implicancia #12 |
| smith2006iliosacral (CONFIRMADO) | si | COMPLETO | smith2006iliosacral.md | no | Escala graduada 0-3 con umbrales 2 mm y 4 mm. Confirmado N1. Pero es fuente SECUNDARIA: la escala viene de la literatura de tornillos pediculares |
| liu2021ctpelvic1k (CONFIRMADO, con reservas) | si | COMPLETO | liu2021ctpelvic1k.md | no | Dataset primario. **Solo 14 de 75 volumenes de CLINIC-metal estan anotados**; no dice que tipo de metal; no da cifra de degradacion. Ver implicancia #13 |
| wang2025adaptiveweighting | **FALTA** | ABSTRACT | wang2025adaptiveweighting.md | no | Multi-ventana en HU (C3). Obj 1 es Go/No-Go: si cae, cae el minimo viable |
| peters2025hybrid (CONFIRMADO, el mas valioso) | si | COMPLETO | peters2025hybrid.md | no | Fuente unica de bone integrity (150 HU + SDC) y metal integrity, base operacional de BFC e ISC. Y declara por escrito que la colocacion realista de metal es impracticable: sostiene la novedad del muestreador |
| wu2022xcist (N1 CONFIRMADO, ROL CORREGIDO) | si | COMPLETO | wu2022xcist.md | no | Da geometria, espectro y ecuaciones, pero **no contiene ningun estudio ni validacion de artefacto metalico**. Es referencia fisica parcial, no baseline validado. Ver implicancia #8 |
| zhang2026pediclescrew (sube) | **FALTA** | ABSTRACT | zhang2026pediclescrew.md | no | Implicancias #3 y #4: colision con mi reclamo de novedad y segunda escala de brecha cortical |
| ren2022metalinsertion (CONFIRMADO tras leer) | si | COMPLETO | ren2022metalinsertion.md | no | Unica fuente con la advertencia explicita del metodo analitico sobre implantes ortopedicos. Fija umbrales de artefacto -75/75/500 HU |

## Nivel 2 — afecta la redaccion

| Clave | PDF | Acceso | Nota generada | Leido por mi | Para que lo uso |
|---|---|---|---|---|---|
| chen2024tumorsynthesis (VERIFICADO) | si | COMPLETO | chen2024tumorsynthesis.md | no | DiffTumor confirmado. No modela nada fuera de la mascara y trunca HU a [-175,250]: respaldo de B_delta y de C3. Candidato a N1 |
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

## Recriterio de niveles — 2026-09-06

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


## Verificado contra el PDF

Lecturas hechas con el subagente `lector-papers` para comprobar los niveles que se
habian asignado por titulo. Aqui solo lo ya confirmado o corregido.

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
| `wang2025adaptiveweighting` | 1 | **SIN VERIFICAR**: no hay PDF, tercera ronda bloqueado |

Contraste con la ronda anterior: de los movimientos que Claude hizo por titulo, 6 de 9
estaban mal. De las asignaciones de la autora, 5 de 5 correctas en nivel. El criterio de
la autora funciona; lo que fallo fue la descripcion del rol, que es un error mas dificil
de detectar porque no se nota hasta que alguien pide la cita.

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
| wang2025adaptiveweighting | ABSTRACT | La autora aporto el abstract el 2026-09-06. Dice que consigue el PDF pronto, pero aun no. | Es nivel 1 y sostiene la codificacion multi-ventana en HU (C3). Con solo el abstract, el respaldo de C3 es cualitativo: no se puede citar ninguna cifra suya. |
| zhang2026pediclescrew | ABSTRACT | La autora aporto el abstract el 2026-09-06 y dice que esta consiguiendo el articulo. | La mas cara de las dos. Su encuadre colisiona con mi reclamo de novedad (implicancia #3) y su escala de brecha cortical toca la definicion de BFC (implicancia #4). Ninguna de sus cifras es citable en este estado. |
