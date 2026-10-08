# 00 — Definicion de la tesis

> Este archivo lo escribe la autora. Es la fuente de verdad del alcance.

## Titulo actual

MetalSynth-Pelvis: Conditioned synthesis of osteosynthesis implants and local metal
artifacts in pelvic CT scan volumes using Multi-Window Image-Domain Diffusion.

> Actualizado el 2026-09-21: *Latent* -> *Image-Domain*, aplicando el punto 4 de la decision
> del 2026-09-19. `tesis/main.tex:36` ya lo tenia; este archivo iba retrasado.

## Pregunta de investigacion

> Copiada literal de `tesis/main.tex` (seccion *Research Question*) el 2026-10-08. El documento de
> entrega (`overleaf/introduccion.tex`) todavia no la alinea con los cuatro objetivos (`\GAPDEC`, #126).

What improvement does a surgical admissibility-constrained (osseous corridor and cortical containment) 3D
placement sampler, a multi-window image-domain diffusion model conditioned on the rigid implant geometries
and an extended generation band ($B_{\delta}$), have in terms of distributional physical-coherence of the
synthesized pelvic osteosynthesis implants and their local artifacts, when compared with both naive
copy-paste insertion and the adopted physics-based simulation protocol of \citet{peters2025hybrid}?
Downstream segmentation impact is deliberately excluded from this study and is stated as out of scope below.

## Hipotesis

> Copiada literal de `tesis/main.tex` (seccion *Hypothesis*) el 2026-10-08.

The synthetic generation of medical anomalies and metallic implants using a rigid geometry and extended
spatial boundaries, HU-conditioned diffusion model and whose placement is surgically enforced via a
corridor-constrained placement sampler is more physically-coherent than unconstrained generative baseline methods
and on the same footing as the adopted explicit physics-based simulation protocol \citep{peters2025hybrid}.
Placement coherence is quantified by Surgical Admissibility of Placement (SAP), the single metric introduced
by this work, which emulates the measured ordinal distribution of real-world implant placement. Appearance
coherence is quantified with the metrics of the adopted protocol under their published names, not with newly
coined ones.

> **Nota de alcance (2026-10-08):** la hipotesis decia *"density-based placement sampler"*, pero el
> muestreador preinscrito perturba el eje del corredor y **no** condiciona por densidad. **DECIDIDO el
> 2026-10-08** (`01-decisiones.md`, entrada delegada, punto 14): la fraccion por zona de densidad **sale de
> SAP** (su fuente, E9b, quedo retirada por #50) y el muestreador se describe como restringido por el
> **corredor oseo medido**. `main.tex` se alineo el mismo dia por orden explicita de la autora (#153), y la
> copia de arriba con el.

## Alcance MINIMO VIABLE (lo que garantizo defender)

- Objetivo 1: validacion de la representacion multi-ventana (Go/No-Go, MAE < 25 HU en hueso).
  **EJECUTADO el 2026-09-19. Resultado: NO-GO**, y se reporta como resultado (#91, decision
  2026-09-19 pto 1). Mejor de las seis combinaciones preinscritas: **61.72 HU** (IC95 bootstrap
  [55.12, 68.99]), **34/34 pacientes** por encima del umbral. MAISI se descarto sin correr: recorta
  a [-1000, 1000] HU y ese recorte solo ya da 42.24 HU (#93). El criterio no se movio.
- Objetivo 2: muestreador de colocacion quirurgicamente restringido, expresado en el
  marco de referencia de `kaiser2014dysmorphism` (reformateo por el eje sacro perpendicular
  al platillo superior de S1; angulo coronal contra la linea de crestas iliacas; angulo
  axial contra la linea de espinas iliacas posteriores; holgura cortical de 5 mm), con
  viabilidad de corredor segun `mclaren2021corridor` expresada como
  `Dmax >= d_implante + 2c` (#31, decision del 2026-09-11): `d_implante` del tornillo
  parametrico (6.5-8.0 mm) y holgura radial `c` de 1-2 mm por lado, derivada de Kaiser
- Metrica SAP + comparacion contra las DOS distribuciones ordinales de cuatro grados de
  `zwingmann2009navigated`, condicionadas por tecnica quirurgica **solo en S1**.
  S1/S2 se conserva como variable geometrica del muestreador; S2 se evalua
  descriptivamente (geometria y grados de brecha), sin prior ordinal clinico disponible.
  **EJECUTADO (E13) y CERRADO.** Distribucion de poses y SAP preinscritas el 2026-09-22 (D-O2.1 a
  D-O2.7) antes del primer Wasserstein-1; ningun parametro se tomo de Zwingmann. Resultado
  (`tesis/main.tex`, *Expected Results* y *Placement result*): **72 volumenes, 3 600 poses**, grados
  0-3 = 51.5 / 31.4 / 11.1 / 6.0 %, **W1 = 0.206** frente a la serie navegada y 0.230 frente a la
  convencional; sensibilidad, 49 volumenes: 0.186 y 0.299. Post hoc declarado: en los 57 volumenes cuyo
  corredor admite 7.0 mm, grado 0 = 64.2 % y W1 = 0.183; en los 15 estrechos, 3.3 % y 1.122.
- **Implante: tornillo transiliaco-transsacro (transiliosacro)**, por decision de la autora del
  2026-10-04 (#130): el corredor medido va de la cortical externa de un ilion a la del otro y cruza
  ambas articulaciones sacroiliacas. "Iliosacro" queda para describir trabajos ajenos.
- **SAP tiene dos componentes** (decision delegada 2026-10-08, puntos 14-17): grado de brecha cortical,
  solo dimension de perforacion, comparado por W1 sin regla de fallo y con la distancia entre los dos brazos
  de Zwingmann (0.395, calculo propio post hoc) como escala de lectura; y viabilidad del corredor a 7.0 mm con
  holgura de 1 mm, descriptiva. La fraccion por zona de densidad queda fuera.
- **Envolvente osea vigente:** cierre de 2 mm **sin** relleno de cavidades (correccion de D-O2.3 del
  2026-10-04; con mascaras de TotalSegmentator el relleno no cambia ningun caso de la cohorte).

> **Tres geometrias para tres preguntas distintas** (decision 2026-09-20 pto 5; D3 del 2026-09-20 (2);
> D-O2.4 del 2026-09-22). No se mezclan, y cada una se nombra por su proposito:
>
> | Geometria | Para que sirve | Origen |
> |---|---|---|
> | Envolvente **6.5-8.0 mm** | **viabilidad** de corredor, `Dmax >= d + 2c` | #31, 2026-09-11 |
> | Cilindro **~4.91 mm** | lo que se **sintetiza** (Objetivo 3) | D3, 2026-09-20 (2) |
> | Cilindro **7.0 mm** | lo que **mide** la brecha cortical en SAP | D-O2.4, 2026-09-22; #118 |
>
> La de sintesis es el `d_centro` mediana de E11 (4.91 mm, frente a 4.8 mm de catalogo y 5.00 mm de E8),
> con cabeza y rosca de 7.3 mm como sensibilidad. La de SAP es **7.0 mm porque es el calibre del
> benchmark**: `zwingmann2009navigated` midio sus cuatro grados sobre tornillos canulados de 7.0 mm
> (*"the screws using a 7.0-mm cannulated screw"*, Materials and Methods, p. 1835). Como la profundidad
> de perforacion escala con el radio, medir SAP con otro calibre meteria un sesgo sistematico dentro del
> Wasserstein-1 y lo volveria ininterpretable. `zhu2022optimalposition` usa dos diametros sin declararlo;
> aqui las tres se declaran.

Defendible por si solo como: "un muestreador de colocacion de implantes
quirurgicamente admisible, validado contra la distribucion clinica real de malposiciones".

## Alcance COMPLETO (si el tiempo alcanza)

- Objetivo 3: renderizador **por difusion en el espacio de imagen, sin autoencoder** ("opcion A",
  decision 2026-09-19 pto 2). Sustituye a la formulacion latente y, con ella, al backbone
  ControlNet + Stable Diffusion 1.5. Se formula como **inpainting de la region de generacion**
  `G = M union B_delta`: el modelo recibe el parche con `G` borrada, la mascara del implante y la de
  banda, y genera HU **solo dentro de `G`**; fuera de `G` se copia del volumen fuente, asi que la
  preservacion fuera de la banda vale **por construccion, no por medicion**. Se conserva la
  codificacion multi-ventana y la banda `B_delta` (~12 mm).
  - **Es una decision POSTERIOR al resultado del Objetivo 1 y asi se declara.** La compuerta se fijo
    antes y no se modifico.
  - El diseno (`experiments/objetivo3/diseno_A.md`) **se preinscribe antes de entrenar**; hoy sigue en
    BORRADOR. Para congelarlo faltan (orden de la decision 2026-10-05 (6), punto 5): **elegir el
    checkpoint**, la **sonda de viabilidad** del brazo fisico y medir el margen `Delta` (D4).
  - La unidad de entrenamiento es el **componente conexo**, no el corte (D2, #102). Conjunto congelado
    el 2026-09-21: **17 149 parches, 241 componentes, 47 casos** (`train`) y **896 parches, 3 casos**
    (`val`, #105); `Delta` se medira sobre **n = 3 pacientes**, y se declara.
  - **Tres desplazamientos de dominio declarados**, no supuestos ausentes: mascara de entrenamiento por
    umbral frente a cilindro parametrico liso; contexto con streaking real frente a paciente limpio;
    y parches de solo banda menos frecuentes de lo que predice la geometria del corredor.
  - **Decisiones de octubre (todas en `01-decisiones.md`; anadido el 2026-10-08):**
    - **Entrenamiento: 30 000 pasos** (2026-10-05 (2)), eleccion de hiperparametro **sobre validacion**,
      no fijada de antemano. Su argumento quedo debilitado y su revision **aplazada** hasta medir el
      criterio de seleccion (2026-10-05 (6), punto 3).
    - **El checkpoint NO se elige por la perdida de validacion** (2026-10-05 (6)), sino por un cotejo de
      apariencia **sobre la tarea de sintesis**: tornillo parametrico en pelvis limpias de validacion,
      perfil radial de HU (mediana y p95 como elevacion sobre el anillo de 12-15 mm) e histograma
      dentro de `M` sobre voxeles > 2500 HU, contra los **2 tornillos aislados de `metal_0039`**, unico
      paciente de validacion con tornillo aislado (`0011` fijador externo, `0056` placas; 2026-10-08 (2),
      #154); regla por envolvente real; con 1 paciente descarta, no prueba (2026-10-07 (2)).
    - **Validacion = 3 pacientes de CLINIC-metal** (`metal_0011`, `_0039`, `_0056`); `0011` aporta el
      60 % de los parches (2026-10-05 (6), punto 2).
    - **Lectura de HU del Objetivo 3: `regla_suave` (v2), `delta = 0.05`** (2026-10-07). La `regla` v1
      sigue siendo la del Objetivo 1, cuyas cifras no cambian; la v1 es caso particular de la v2.
    - **Endpoint primario `streak amplitude` preinscrito por completo** (2026-10-05 (3) y (4)): verdad de
      terreno = TC limpia del mismo paciente, asi que solo se mide en los **14 de test sin metal**
      (E-A2); en los 20 con metal se mide **discrepancia**. ROIs = anillos completos de un voxel de
      guarda a 12 mm, cortes con `M` menos 8 mm por extremo; mediana por paciente; se reporta la
      fraccion de voxeles en el suelo de -1000 HU. Jerarquia: **TOST contra el brazo fisico
      (primario)**, realismo frente a CLINIC-metal, y copia y pegado como **control de cordura**.
    - **Suelo de -1000 HU** (2026-10-05): regla preinscrita; si la perdida atribuible a la
      representacion (percentil 5 del paciente, eleccion post hoc declarada) es menor que `Delta`, se
      declara como limitacion de alcance; si es mayor, se cambia la representacion.
    - **Brazo fisico: se reproduce, NO se valida** (2026-10-05 (5)). Verificado en su codigo: paciente
      y metal se proyectan **juntos**; geometria 2D de una fila de detector; su metal son formas
      fractales, no implantes.
    - **Orden de trabajo** (2026-10-05 (6), punto 5): cadena completa -> sonda de viabilidad de Peters
      -> Peters completo -> `Delta` -> congelar `diseno_A.md` -> corrida final.
    - **Diseno fijado por delegacion (2026-10-08, puntos 1-13):** `pub+asinh` en float32; 3 cortes 2.5D;
      arquitectura tal como corrio (U-Net `base = 64`, `v`, coseno, DDIM 50); 5 semillas por caso; copia y
      pegado = HU constante (mediana del metal real de entrenamiento); `bone/metal integrity` descriptivas, leidas
      contra el brazo fisico; realismo = perfil radial e histograma frente a E-A1; brazo fisico sobre los 14
      de E-A2, test-retest con otra semilla de ruido. Para congelar `diseno_A.md` solo faltan datos: checkpoint,
      sonda de Peters y `Delta`.
- Objetivo 4: SAP como unica metrica propia, mas las metricas del protocolo adoptado
  (`peters2025hybrid`) con SUS nombres publicados
- ~~Ablaciones por restriccion~~ **FUERA** (2026-09-17): trabajo futuro. Ver punto 10 de `Fuera de alcance`

## Fuera de alcance (explicito)

> Actualizado el 2026-09-08 por decision de la autora, aplicado tambien a `tesis/main.tex`.

1. **Evaluacion downstream de segmentacion (Dice, HD95). FUERA.** No por falta de tiempo:
   por dos condiciones auditables. Solo una minoria de los volumenes con metal tiene
   anotacion osea verificada (implicancia #13), y solo una parte de la coleccion publicada
   esta en disco (implicancia #18). Un resultado downstream se apoyaria en una cohorte
   demasiado pequena y demasiado parcialmente anotada. Se declara trabajo futuro.
2. **Metricas BFC e ISC como contribucion propia. RETIRADAS.** La apariencia se evalua
   con las metricas del protocolo adoptado bajo sus nombres publicados (bone integrity,
   metal integrity, streak amplitude). Renombrar medidas heredadas vaciaba el Objetivo 4.
   Cierra las implicancias #14 y #16. **SAP queda como unica metrica introducida por
   esta tesis.**
3. **Reimplementacion validada de XCIST como brazo de comparacion. FUERA.** Sustituida
   por la adopcion del protocolo de `peters2025hybrid` (implicancia #8, ya aplicada).
4. **Reclamo de novedad sobre la codificacion multi-ventana en si. RETIRADO.** El marco
   multi-ventana es de trabajo previo de MAR y `wang2025adaptiveweighting` lo atribuye a
   su vez a trabajo anterior (implicancia #24). La novedad reclamada es su uso **para
   sintesis** junto con B_delta.
5. **Rango unico de malposicion (31-60% o 2-15%). RETIRADO.** Ninguno resiste: el primero
   es derivacion propia sobre dos poblaciones distintas y el segundo es cita de tercera
   mano (implicancias #12 y #25). Se usan las distribuciones ordinales medidas.
6. **Zona segura sacroiliaca como geometria heredada. NO SE RECLAMA.** El marco de
   referencia se hereda de `kaiser2014dysmorphism` y el procedimiento de corredor de
   `mclaren2021corridor`. Lo que se reclama como propio es **la distribucion de poses**
   dentro de ese marco (implicancia #7).
7. **El umbral de 10 mm como estandar clinico validado. NO SE PRESENTA ASI.** Se usa como
   convencion de holgura geometrica, con la justificacion dimensional de Kaiser (1-2 mm
   alrededor de un tornillo de 6.3-8 mm). La cadena de citas tiene tres saltos
   (implicancia #25).
8. **Estratificacion por fenotipo sacro. FUERA POR COMPLETO** (2026-09-08). Ni los tres
   fenotipos, ni el score de dismorfismo, ni el corte `>70`. El efecto del fenotipo sobre
   el tamano de la zona segura **no es consistente entre estudios** (Carlson 2000, recogido
   en `gardner2010safezones`, no halla diferencia), y Kaiser y Gardner clasifican
   dismorfismo con criterios distintos. El muestreador **mide la geometria del corredor
   directamente sobre cada volumen**. Cierra la implicancia #27.
9. **Subir mas por la cadena de citas del umbral de 10 mm. FUERA.** Cuatro eslabones
   auditados, ninguno lo mide: es una convencion profesional derivada del calibre del
   tornillo, y las fuentes que la enuncian lo dicen en su texto (implicancia #25).

10. **Ablaciones por restriccion. FUERA** (2026-09-17, decision delegada al asistente). Se declaran trabajo futuro
    para liberar tiempo del camino critico (VAE y muestreador). El brazo fisico de Peters se conserva sobre un
    subconjunto reducido de pacientes.

## Criterio de cohorte del Objetivo 2: lo que significa y lo que NO (2026-10-04)

> Anadido tras el cribado ciego de fractura (#132). Lo escribe el asistente **por orden explicita de la
> autora**; la decision de fondo sigue siendo suya.

La cohorte del Objetivo 2 se construyo con el criterio de la decision **#52 (a)**: medir el corredor en
pelvis **sin osteosintesis**. **Eso no es lo mismo que pelvis sin fractura, y nunca se verifico.**

Un cribado ciego de 30 volumenes de esa cohorte —15 con corredor estrecho y 15 de comparacion, leidos
por un medico licenciado **sin especialidad**, con la asignacion a estrato oculta— hallo **fractura en
20 de los 30**. En **7 de los 15** corredores estrechos la fractura es **sacra y desplazada**, frente a
**2 de 15** en el grupo de comparacion (`p = 0.109`).

Por tanto:

- **La cohorte NO es anatomia sana.** Es la particion sin metal de CTPelvic1K, y la mayoria de los
  volumenes examinados tiene fractura. Donde el documento hable de la anatomia receptora debe decir
  **"sin osteosintesis"**, nunca "intacta" ni "sin fractura".
- **El corredor se mide sobre cada volumen tal como esta**, asi que ninguna cifra del Objetivo 2 depende
  de esto. Lo que cambia es **como se interpreta** el estrechamiento, no como se calcula.
- **Una fraccion no cuantificable del estrechamiento puede ser patologia** y no variacion anatomica
  normal. La muestra no permite decir cuanta: el efecto es grande pero no alcanza significacion, y 5 de
  las 14 fracturas sacras estan en S2, donde `reilly2003effect` no transfiere.
- **El cribado es eso, un cribado.** Lector sin especialidad, y evidencia heterogenea: 18 casos juzgados
  sobre laminas y 12 sobre el volumen completo en un visor.

## Riesgos asumidos (2026-09-08)

> Se declaran aqui porque condicionan el Objetivo 2. Los dos estan en
> `04-implicancias.md` y en `01-decisiones.md`.

- **R1 — Los landmarks del marco de referencia pueden no sobrevivir al artefacto.**
  `kaiser2014dysmorphism` caracterizo su marco sobre pelvis **no lesionadas** y excluyo los
  CT con implantes que oscurecen la union lumbosacra, que es justo donde estan los tres
  landmarks y donde pega el streaking. **Se cierra midiendo en casa**, no leyendo:
  cuantificar en cuantos volumenes locales con metal se pueden ubicar los tres landmarks.
  **MEDIDO el 2026-09-11 y escrito en `main.tex`:** de 65 pacientes con material
  ortopedico, marco computable con S1 confirmado por revisor clinico en 49 y sin
  contaminacion en 30. La perdida la explican mas el FOV (7) y la localizacion que el
  artefacto. **El pendiente de los 7 con FOV cortado queda CERRADO el 2026-09-22** (D-O2.2, #119):
  no por resolverlo, sino **por irrelevancia para la cohorte del Objetivo 2**. Verificado sobre
  `e9ts_corredor.csv` (152 casos unicos), `fov7 = True` se da en **4 casos y los cuatro son de grupo 1**;
  la cohorte primaria son los grupos 2 y 3, asi que ninguno entra. El "7" original cuenta sobre los 65
  pacientes de R1, que es un universo distinto: las dos cifras no deben citarse juntas. Implicancia #26.
- **R2 — RESUELTO el 2026-09-08 por la via corta: no se avanza.** Se adopta de Kaiser solo
  lo operacional (marco de referencia, definiciones angulares, margen de 5 mm). El score,
  el `>70` y los fenotipos quedan fuera, asi que ya no hay nada que decidir. Las tres
  lecturas que iban a informar esta decision se hicieron: ninguna aporta un umbral medido
  y `gardner2010safezones` trajo ademas la objecion de Carlson 2000 a estratificar por
  fenotipo. Ver el punto 8 de `Fuera de alcance`.

## Pendiente de ejecucion (decidido, falta correrlo)

- ~~Tabla de sensibilidad del cribado (#22)~~ **HECHA** el 2026-09-09 (E1).
- ~~Cifra de R1 (#26)~~ **HECHA** el 2026-09-11 y escrita en `main.tex` (49 de 65 con
  marco computable y S1 confirmado por revisor clinico; 30 sin contaminacion).
- ~~**Medicion del corredor por volumen (E9, #31).** Bloqueada por segmentacion~~ **DESBLOQUEADA y
  HECHA** (E9-TS, 2026-09-14/15): el bloqueo era que un umbral HU no representa el esponjoso del sacro
  (#48), y se resolvio segmentando con TotalSegmentator en vez de por umbral. `e9ts_corredor.csv` trae
  **2 352 filas validas sobre 152 casos, 0 errores**, con eje del corredor por caso (centro `c_*`,
  direccion `u_*`, angulos coronal y axial) y banderas de viabilidad por combinacion `(d, c)`.
  Cohorte del Objetivo 2, 72 casos: `D` mediana **9.5 mm**, **40.3%** pasa el criterio de 10 mm,
  **65.3%** con `d=6.5, c=1`.

## Pendiente de decision de la autora

- ~~Reparto del umbral en dos reglas (#22)~~ **DECIDIDO el 2026-09-11**: 2500 HU solo para
  cribado; metal integrity con la regla adaptativa por ROI de `peters2025hybrid`. ~~Queda
  **propuesta** (no decidida) una tercera regla para extraer mascaras de implantes reales:
  umbral de semimaximo local (E8, #46).~~ **DECIDIDO el 2026-09-20** (D1): la mascara `M` de
  entrenamiento se extrae con **umbral de 2500 HU en el piloto**, y el **semimaximo local queda como
  variante de sensibilidad**, no como regla principal.
- ~~`templeman1996proximity` sigue en `refs.bib` sin PDF.~~ **RESUELTO 2026-09-17**: PDF y ficha
  completos; no publica ningun % de malposicion (#77).

## Eje S1/S2 y limite del benchmark (2026-09-08; implicancias #12 y #28)

`gardner2010safezones` aporta el respaldo **anatomico** del eje S1/S2: areas medias
minimas iliosacras de 346/109.3 mm2 en normales y 222/220.1 mm2 en dismorficos
(S1/S2; Results, p. 624 y Tabla 1, p. 627; evidencia textual en su ficha).
Las ultimas son aproximadamente iguales, no una inversion de las medias ni prueba
de igual seguridad clinica. Se evalua cada nivel midiendo su corredor en cada volumen,
sin imponer una jerarquia universal de amplitud ni reintroducir fenotipos o score.
Gardner mide el lado no lesionado y trayectorias centrales ideales: no aporta
frecuencias clinicas de grados de brecha ni calibra SAP en S2.

`vandenbosch2002` ya fue leido con `lector-papers`. Los 6/31 frente a 1/49
son **pacientes con quejas neurologicas por configuracion de tornillos**, no tornillos
malposicionados por nivel. Aporta respaldo clinico asociativo para distinguir S1/S2,
con sesgo temporal y de aprendizaje declarado. Su evaluacion de posicion es binaria
y no permite construir los cuatro grados de SAP en S2.

Se conserva el benchmark ordinal por tecnica de Zwingmann **en S1**; no se extrapola
a S2 ni se convierte lesion neurologica en brecha cortical. S2 conserva evaluacion
geometrica y descriptiva. #28 queda resuelta; #12 se cierra por delimitar el benchmark
al soporte disponible, no porque van den Bosch aporte el prior ordinal faltante.

## Fechas

| Hito | Fecha objetivo |
|---|---|
|  |  |
