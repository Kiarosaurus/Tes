# Diseno A — renderizador por difusion en espacio de imagen (Objetivo 3)

> **ACTUALIZACION 2026-09-20 (3): las cuatro `[DECIDIR]` estan RESUELTAS** por decision de la autora, escrita en
> `01-decisiones.md` (entrada 2026-09-20 (2)). D1 = umbral 2500 con semimaximo de sensibilidad; **D2 = la unidad de
> entrenamiento es el COMPONENTE, no el corte** (#102); D3 = cilindro uniforme de ~4.9 mm con cabeza como
> sensibilidad (E11, #101); D4 = forma del contraste fijada, margen `Delta` tras el piloto sobre validacion.
> **Lo unico que falta para preinscribir es el margen `Delta`**, que por construccion se mide despues.
>
> **Estado: CONGELADO el 2026-10-09 (ver seccion 0). Lo que sigue en este bloque es historico: BORRADOR para revision de la autora. NO preinscrito.** Decision que lo origina: `01-decisiones.md`,
> 2026-09-19 (tras el No-Go de P1, #91). Se preinscribe (se congela y se registra) **antes de entrenar**. Todo lo marcado
> `[DECIDIR]` necesita respuesta de la autora; lo marcado `[SUPUESTO]` es propuesta del asistente como asesor y queda
> declarado. Nada de este documento esta medido salvo donde se cita un experimento.

> ## CONGELADO el 2026-10-09 (`01-decisiones.md` 2026-10-09 (6)), ANTES de tocar ningun paciente de test
>
> La seccion 0 manda sobre todo lo que sigue. Las secciones 1-9 quedan como **registro historico** de como se llego
> aqui: sus `[DECIDIR]` y `[SUPUESTO]` estan resueltos por la seccion 0. **Se declara:** el modelo se entreno antes de
> congelar (2026-09/10). Lo que se congela antes de tocar test es la **evaluacion**, y el checkpoint se eligio sobre
> validacion.

## 0. Diseno congelado para la corrida final

**Sintetizador** (`a15_cadena_completa.py`):
- Checkpoint `mejor_37k` (`$DATA/a7/run02/mejor.pt`), elegido por cotejo de 1 mm (2026-10-09).
- Representacion `pub+asinh`; lectura `regla_suave` con `delta = 0.05`; 2.5D de 3 cortes; parche de 256.
- DDIM de 50 pasos, **5 semillas (0-4)** por paciente.
- Tornillo: cilindro de 4.91 mm con cabeza, como en `a11`/`a15` (D3), en la pose del eje del corredor de E9-TS
  (`default6mm`, sin perturbar).
- **Todos los cortes axiales que toca `G` (`--incluir-banda`, #160).**
- Contexto intacto fuera de `G`. Todo en GPU, un mismo tipo de GPU en toda la corrida (#151).

**Brazo fisico** (`a19_peters_completo.py`):
- Protocolo de la sonda (fantoma `(HU+1000)/1000` con realce del repositorio AAPM; `M` binaria identica a la del
  difusor).
- Cortes alternos (`k = 2`) entre los que toca `G`.
- **Material primario: `Ti`** (cotejo frente a lo real, 2026-10-09 (5)). **`Fe`, sensibilidad.**
- Replicas A y B.

**E-A2, endpoint primario** (`a20_evaluador_ea2.py`):
- `streak amplitude` con la definicion de 2026-10-05 (3) y (4): anillos completos en planos perpendiculares a `u`,
  de una guarda de un voxel en plano a 12 mm, recorte de 8 mm por extremo, rebanadas del espesor de la guarda,
  minimo 20 voxeles por ROI, mediana sobre ROIs.
- Cada brazo se mide en sus cortes producidos: el difusor en todos los que toca `G`; Peters en los alternos. Es el
  mismo dominio con que se midio `Delta`.
- **Valor por paciente:**
  - difusor: mediana de las 5 semillas;
  - fisico: mediana (= media) de las replicas A y B.
- Se reporta siempre la fraccion de la ROI en el suelo de -1000 HU.

**Contrastes sobre los 14 pacientes de test sin metal:**

| | Contraste | Prueba | Criterio |
|---|---|---|---|
| **Primario** | difusor frente a Peters **Ti** | **TOST pareado**: IC90 de la diferencia media pareada con *t* de Student, n = 14 | equivalencia solo si el IC90 cae entero en **[-188.7, +188.7] HU** (`Delta`, 2026-10-09 (4)) |
| Sensibilidad | difusor frente a Peters Fe | el mismo TOST | descriptivo |
| Cordura | difusor frente a copia y pegado (HU constante) | Wilcoxon de rangos con signo, una cola, alfa 0.05 | piso, **no** evidencia de calidad |

- **Declaracion de potencia (preaceptada, 2026-10-05 (6)):** con n = 14 el resultado honesto puede ser "no se pudo
  concluir equivalencia", y asi se reporta.
- **Esperable a la vista de validacion (#161):** el difusor quedo unos 1240 HU bajo Ti en `0101` y unos 50 HU en
  `0102`.

**Realismo (opcion 3, descriptivo, sin prueba de hipotesis):**
- Estadisticos sin referencia (perfil radial de 1 mm e histograma dentro de `M`) de lo sintetizado en E-A2, frente a
  los **tornillos aislados reales de los pacientes de test** (#155 (2), decidido por la autora el 2026-10-09).
- **Quien entra se define por una REGLA, no por una lista** (aclaracion del 2026-10-09, `01-decisiones.md`
  2026-10-09 (7)). La regla se escribio antes de que la autora terminara su revision de test y antes de cualquier
  resultado de sintesis en test:
  - **Entra** cada paciente de test con al menos un tornillo intraoseo aislado (IS, TS u otro), segun la **columna
    `autora`** de `experiments/exploration-3d/tornillos_conteo.csv`: `2_n_IS`, `3_n_TS` o `4_n_otros_aislados`
    con un entero >= 1.
  - **Queda fuera, y se declara**, el paciente con `incierto` en esas preguntas y ningun entero >= 1. No se adivina.
  - **Componentes de referencia:** los tornillos aislados de esos pacientes. Placas y fijadores quedan excluidos de
    las cascaras, como el otro tornillo de `0039` en `a17`.
  - Se reporta ademas el desglose por tipo (IS/TS frente a otros), solo descriptivo.
  - La lista anterior (`0009`, `0024`, `0048`, `0049`, `0066`) era la propuesta del agente; queda sustituida.
- Resumen: fraccion de cascaras dentro de la envolvente real, por paciente. No depende del material del brazo
  fisico.

**Limitaciones declaradas, no corregidas:**
- p95 del difusor bajo lo real (#157).
- El brazo fisico exagera el artefacto respecto de lo real, aun con Ti (#159, `a21`).
- Fantoma de Peters tomado del repositorio y no del articulo (#158).
- `Delta` fijado por la variabilidad del difusor; 2 pacientes de validacion (2026-10-09 (4)).
- Material real de CLINIC desconocido.

**Lo que NO entra en la corrida final:** variantes de rosca, arandela o canulacion (D3, sensibilidad no programada);
poses perturbadas del muestreador; mejora de la subexposicion (pendiente del equipo; si se hace, sera una version
posterior declarada).

**Orden de la corrida final** (exige `--corrida-final` en los scripts; ninguno toca test sin esa bandera):
1. `a15` sobre los 14 de test.
2. `a19` sobre los 14.
3. Copia y pegado.
4. `a20` y los contrastes.

## 1. Que resuelve y que no

- **Resuelve:** el error de ida y vuelta del autoencoder (P1: 61.72 HU en hueso, 69.89 HU en `B_delta`). Sin latente,
  lo que no se genera queda identico al CT de origen, voxel a voxel.
- **No resuelve, y se declara:** que la apariencia del artefacto pueda generarse en el dominio de la imagen sin
  proyecciones (supuesto de `main.tex:56`); el streaking lejano mas alla de `B_delta` (truncado por diseno, #57); la
  reconstruccion desconocida de CLINIC-metal (#73).
- **Cambia respecto a `main.tex`:** desaparecen "Latent", "Stable Diffusion 1.5 backbone" y ControlNet (no hay base
  preentrenada en pixeles de CT que congelar; #74 se cierra por reemplazo). Se mantienen multi-ventana, `B_delta`,
  mascara de implante rigido, protocolo de Peters, muestreador y SAP.

## 2. Formulacion

**Inpainting condicionado en la region de generacion `G = M ∪ B_delta`**, donde `M` es la mascara del implante y
`B_delta` la banda de ~12 mm a su alrededor (distancia euclidea 3D con el spacing del header, como en P1).

- **Entrada del modelo:** el parche con `G` borrado (contexto intacto fuera de `G`), la mascara `M` y la mascara `G`.
- **Salida:** los HU dentro de `G`. Fuera de `G` se copia el original (composicion exacta).
- **Entrenamiento:** pares reales. En pacientes de entrenamiento con metal, `M` sale del metal real y el objetivo es el
  CT real dentro de `G`. El modelo aprende "dado este contexto y esta mascara, que aspecto tienen implante y artefacto".
- **Uso (sintesis):** paciente sin metal + mascara de tornillo parametrico en una pose -> el modelo rellena `G`.

## 3. Datos y particion

- **Particion:** la de P1 (`experiments/objetivo1/p1_particion.csv`, semilla 20260917), para cumplir la *Strict
  Isolation Rule* (`main.tex:111`) y reutilizar un test ya fijado. Con metal: **74 pacientes de entrenamiento**
  (52 dataset7 + 22 dataset6), 5 de validacion (**3 tras R2**: `metal_0011`, `_0039`, `_0056`; 2026-09-21 (2) y 2026-10-05 (6)), **20 de test**. Sin metal en test: 14 (dataset6).
- **Unidad de entrenamiento (DECIDIDA 2026-09-20, D2/#102):** parches 2.5D por **COMPONENTE** de implante, no por
  corte. Cada componente conexo de `M` lleva su propia `B_delta` y su propio parche; los canales `M` y `G`
  contienen **solo el componente objetivo**, y el metal de otros componentes que caiga en el parche se queda en
  los HU de contexto y se cuenta (`n_metal_otros`). Motivo: en sintesis se coloca **un** tornillo, asi la `G` de
  entrenamiento tiene la misma estructura que la de uso. Script: `a1b_parches_componente.py`.
- **`[DECIDIR]` Mascara `M` en entrenamiento.** Opciones (ligadas a #95):
  - (a) umbral 2500 HU (el de cribado, #22). E8: cerca del semimaximo, recorta periferia, fragmenta 10 de 62.
  - (b) semimaximo local por objeto (propuesta abierta de #22/#46). Mas fiel al borde; mas codigo.
  - **Recomendado: (a) para el piloto y (b) como sensibilidad**, porque (a) ya esta validado en E1/E8.
  - Detalle y consecuencias: seccion **8 bis, D1**. Se puede fijar **ya**.
- **`[SUPUESTO]` Que implantes entran:** todo el metal de los pacientes de entrenamiento (placas, protesis, tornillos),
  no solo tornillos. Mas datos de apariencia; el tipo de implante no esta anotado (`main.tex:111`). Riesgo: el modelo
  aprende sobre todo protesis grandes. Se reporta la mezcla por tamano de componente (E8 ya mide componentes de metal).

## 4. Representacion

- **`[SUPUESTO]` Codificacion `pub+asinh`** (3 canales: LW asinh [-1000, 20000], MW, SW). Identidad exacta en hueso y
  metal (E6c: 0.00 HU a float; P1: 0.00 en identidad), y es la primera del orden a priori de #76.
- **Lectura de HU del resultado: DECIDIDA el 2026-10-07** (`01-decisiones.md`): `regla_suave` (v2) con
  `delta = 0.05` (`common.ventanas.DELTA_OBJ3`). Antes se leia con la `regla` de P1 (canal mas estrecho no
  saturado), que borraba metal casi saturado y recortaba la cola clara de las rayas (#152). La `regla` v1
  sigue siendo la del Objetivo 1 y es caso particular de la v2.
- **2.5D:** 3 cortes axiales contiguos -> 9 canales de imagen + 2 de mascara (`M`, `G`) en la entrada; se genera el
  corte central. `[SUPUESTO]`.
- **`[DECIDIR]` Tamano del parche.** Un tornillo iliosacro cruza el corte axial casi de lado a lado: su largo es el
  del corredor (Kaiser, `main.tex:113`) mas 2 x 12 mm de banda. **Recomendado 256 x 256** (~200 mm a ~0.78 mm) para que
  el tornillo entero y su banda quepan; 128 x 128 no los contiene. Es la eleccion que mas pesa en el computo.
  Detalle y control que puede cambiarla: seccion **8 bis, D2**. Se puede fijar **ya**, sujeto al control de A1.

## 5. Modelo y entrenamiento `[SUPUESTO]`

- U-Net de difusion condicionada por concatenacion (tipo DDPM/ADM), en pixeles, float32. Sin base preentrenada.
- Objetivo de prediccion de ruido (o `v`) con perdida **solo dentro de `G`** (fuera se copia).
- Muestreo DDIM, 50 pasos, semillas fijas; varias muestras por caso para medir variabilidad.
- **Pasos de entrenamiento: 30 000.** DECIDIDO por la autora el 2026-10-05 (B2), registrado en
  `docs/01-decisiones.md`. **Es una eleccion de hiperparametro hecha sobre VALIDACION, no fijada de
  antemano, y asi debe declararse en la tesis.** Sale del minimo de validacion de dos corridas que
  trazan la misma curva dentro de 1.5e-3 en todos los bloques compartidos: el minimo **no es un punto
  sino una meseta de ~20 000 a ~40 000 pasos** (`run01` lo pone en el bloque 20-30 k con 0.05809,
  `run02` en el 30-40 k con 0.05891), y 30 000 cae en su centro. Pasado el bloque 40-50 k la validacion
  sube de forma monotona en las dos corridas. Ninguna de las dos se midio sobre test. Evidencia en
  `docs/04-implicancias.md` #134 y en `experiments/objetivo3/outputs/a7/run01|run02/curva.csv`.
- **Coste medido:** 0.377 s/paso en la particion MIG `a100_3g.20gb` (12.3 GB de 20), de donde 30 000
  pasos son **~3 h 10** de pared. `run02` hizo 60 000 en 6 h 20.
- **`[DECIDIR]` El papel de la validacion cambio y esta linea lo contradice.** Este documento decia
  *"registra curva, no elige checkpoint (igual que P1)"*. **Hoy la validacion hace las dos cosas que
  esa frase niega:** `guarda()` escribe `mejor.pt` en cada minimo de validacion (correccion de #134,
  2026-10-04), de modo que **elige el checkpoint**, y la cifra de 30 000 pasos sale de ese mismo
  minimo. El cambio es deliberado y resolvio una perdida real —en `run01` las pesas del optimo se
  perdieron—, pero **aparta al Objetivo 3 del precedente de P1 y no esta declarado en ninguna parte**.
  Hace falta decidir como se declara: seleccion de modelo por validacion, con test intacto, es
  practica estandar y defendible; lo que no se puede es sostener la frase anterior. Anotado por el
  asistente al aplicar B2; la decision es de la autora (regla 14).
- **Presupuesto:** medido. Prueba corta de 200 pasos en Khipu (s/paso, memoria), como en P1, y dos
  corridas completas: `run01` (144 500 pasos, A100 entera) y `run02` (60 000 pasos, MIG).

## 6. Tornillo sintetico (uso)

- **ACTUALIZACION 2026-10-08: lo que sigue en esta vineta esta SUPERADO.** La geometria de sintesis es el
  cilindro de **~4.91 mm** (D3, 2026-09-20 (2)); 6.5-8.0 mm queda solo para la viabilidad del corredor y 7.0 mm
  para medir la brecha en SAP (D-O2.4). El implante es un **tornillo transiliaco-transsacro** (#130). Texto
  original: **Geometria (ya decidida, `main.tex:113`, #41 via c):** cilindro liso rigido; diametro 6.5-8.0 mm
  (`gardner2010safezones`) y 6.3-8 mm (`kaiser2014dysmorphism`); largo acotado por el corredor medido en cada volumen.
  Rosca, canulacion, cabeza y arandela: sin fuente textual -> simplificacion declarada.
- **Rasterizacion:** cilindro a la resolucion del CT; `M` = voxeles cuyo centro cae dentro. `[SUPUESTO]`
- **Pose inicial (antes del muestreador P3):** eje del corredor S1 ya medido en E9-TS (`e9ts_corredor.csv`: centro
  `c_x/c_y/c_z`, direccion `u_x/u_y/u_z`, largo `L_TS_mejor_mm`, viabilidad por diametro y holgura). Cuando P3 exista,
  sus poses.
- **Geometria de la mascara (propuesta del asistente tras las lecturas del 2026-09-19/20, #97).** El catalogo describe
  el tornillo fisico; el modelo aprendio **mascaras por umbral de implantes reales**. La mascara debe parecerse a lo
  segundo. Fuste de catalogo 4.8 mm (`synthes2006cannulated`, `zhu2022optimalposition`) y 4.9 mm (`gardner2015screw`)
  frente a los **5.00 mm medidos en E8**: coinciden dentro de un cuarto de voxel.
  - **Piloto, dos piezas:** cuerpo cilindrico de **5.0 mm** en todo el corredor + **cabeza de 8.0 mm de diametro y
    4.5 mm de altura** (`sayres2014comparison`), apoyada en la cortical iliaca y **sin avellanar** (*"No countersink was
    used"*, p. 33). Sin rosca explicita, sin arandela y sin canulacion.
  - **`[DECIDIR]` D3 — el diametro no se fija hasta leer E11** (seccion 8 bis, D3). Lo de abajo es la verificacion
    que lo decide, **lanzada sobre la cohorte completa el 2026-09-20**; hasta que haya CSV, el "5.0 mm" del piloto
    es propuesta, no decision.
  - **Verificacion barata antes de fijarlo (~1 h, CPU local):** perfil de diametro **a lo largo del eje** en los
    tornillos reales de CLINIC-metal. E8 da un solo diametro por componente (`d_ext_2500_mm`), no su variacion axial.
    Si el extremo distal se ensancha hacia 7.3 mm, hay que anadir el tramo de rosca; si el volumen parcial lo promedia
    a ~5 mm, el cilindro uniforme queda justificado **con medicion propia**.
  - **Variantes declaradas, como sensibilidad:** envolvente de rosca 7.3 mm en los 16/32 mm distales y variante
    totalmente roscada (209.620-209.780); arandela 13.0 x **1.5 mm** (`doublemedical2021trauma`, otro fabricante,
    salvedad declarada; conviene medir antes cuantos pacientes reales la llevan); canulacion hueca frente a maciza
    (**parametro libre**, decision de la autora del 2026-09-20).
  - **Actualizacion 2026-09-20 (#99), con la guia del fabricante (`synthes2003guide`):** el cuerpo del tornillo queda
    cerrado en **4.8 mm** (*"4.8 mm diameter shaft"*) y el documento aclara que *"The core and shaft diameters are the
    same."*, asi que los 4.7 mm de `gardner2015screw` son el nucleo **bajo la rosca**, otra magnitud. La guia **no
    publica** espesor de arandela ni canulacion, y su 2.9 mm es canulacion de **instrumental**: el parametro libre se
    mantiene y ahora con evidencia de que la pista del distribuidor venia de una broca. Material del mismo sistema:
    **316L o Ti-6Al-7Nb**, lo que refuerza que la mascara binaria no codifica aleacion (#98).
  - **No se mezcla con #31:** la viabilidad del corredor sigue usando la envolvente de 6.5-8.0 mm. Son dos geometrias
    para dos preguntas, como hace `zhu2022optimalposition` sin declararlo (p. 1547 frente a p. 1548).

## 7. Evaluacion (a preinscribir; sin umbrales numericos no verificados, como pide `main.tex:115`)

| Bloque | Pacientes | Que se mide | Contra que |
|---|---|---|---|
| E-A1 Reconstruccion de implante real | 20 de test con metal | Bone integrity y metal integrity (Peters, nombres publicados) dentro de `G`; **DISCREPANCIA** frente al CT real, con el MAE en HU dentro de `G`. **`streak amplitude` NO se mide aqui**: su definicion exige desviacion respecto a una verdad de terreno sin metal, que en un paciente con implante real no existe (DECISION 2026-10-05 (3), `01-decisiones.md`) | El CT real (referencia de apariencia, no ground truth fisico, #73) |
| E-A2 Tornillo sintetico | 14 de test sin metal | Las mismas metricas de Peters, **y aqui si `streak amplitude`**, porque la verdad de terreno es el CT limpio del mismo paciente: `Delta(x) = I_sintetica - I_original`, **anillos completos (360 grados)** derivados de la pose, de **un voxel en plano de guarda** alrededor de `M` hasta los **12 mm** de `B_delta`, en **todos los cortes con `M` menos 8 mm por extremo** (parametros fijados sobre validacion, `01-decisiones.md` 2026-10-05 (4)), mediana por paciente, **mas la fraccion de voxeles de la ROI en el suelo de -1000 HU** como indicador de censura (#141). **costura en el borde de `B_delta`** (salto de HU a traves del borde; medido por `a10_costura.py`). Todo fijado en `01-decisiones.md` 2026-10-05 (3) | (i) copia-pega ingenua, declarada **control de cordura y no evidencia**: su amplitud vale ~0 por construccion; (ii) brazo fisico de Peters, **contraste PRIMARIO por TOST**; (iii) **realismo**: distancia entre la distribucion de amplitudes sinteticas y la medida en CLINIC-metal real |
| E-A3 Preservacion fuera de `B_delta` | todos | RMSE y SSIM fuera de `G` | **Cero por construccion**; se reporta como tal, no como resultado |
| E-A4 QC visual | muestra fija | Laminas con el mismo formato de las de E9-TS | Revision de la autora |

- **Criterio de exito `[DECIDIR]`:** `main.tex:98` dice *"Lower profile discrepancy than naive copy-paste insertion,
  with streak amplitudes statistically comparable to, or better than, the adopted physics-based protocol"*. Falta fijar
  **que prueba estadistica** y **que es "comparable"** antes de ver resultados (patron #76).
  Propuesta completa en la seccion **8 bis, D4**: endpoint primario unico, Wilcoxon de una cola para "mejor que
  copia-pega", **TOST** para "comparable al brazo fisico", y el margen `Delta` medido **solo en validacion**. La forma
  se fija **ya**; el margen, **despues del piloto**.

## 8. Riesgos conocidos

1. **Contexto con y sin artefacto (nuevo, #96).** En entrenamiento el contexto fuera de `G` ya trae el streaking lejano
   del implante real; en uso, el paciente sin metal tiene contexto limpio. El modelo puede depender de rayas que en uso
   no existen. Se ve en E-A2 como costura o como artefacto debil. Mitigacion posible: entrenar con contexto recortado
   o suavizado fuera de `G`; se decide tras la prueba corta.
2. **Brecha de mascara** (#95).
3. **Mezcla de implantes** dominada por protesis grandes (seccion 3).
4. **Computo sin medir** (#89): la prueba corta de la semana 1 es obligatoria antes de lanzar nada largo.

## 8 bis. Recomendaciones del asesor sobre las cuatro `[DECIDIR]` (2026-09-20)

> Propuesta del asistente en rol de asesor, pedida por la autora el 2026-09-20. **No es una decision**: la decision
> la escribe la autora en `01-decisiones.md` (regla 3). Lo importante de esta seccion es la **columna "cuando"**:
> dos de las cuatro se pueden fijar hoy, y dos **no deben fijarse todavia** porque dependen de una medicion que
> aun no existe. Fijar por adelantado lo que depende de un dato, o fijar despues de ver el dato lo que deberia ser
> a priori, son los dos errores que este proyecto ya tiene catalogados (#25, #37, #45, #47, #50, #76).

| # | Decision | Recomendacion | Cuando se puede fijar |
|---|---|---|---|
| D1 | Mascara `M` de entrenamiento | (a) umbral 2500 HU en el piloto, (b) semimaximo como sensibilidad | **Ya.** No depende de ninguna medicion pendiente |
| D2 | Tamano de parche | 256 x 256 | **Ya como valor por defecto**, confirmado con el control de contencion de A1 |
| D3 | Diametro del cilindro de sintesis | **no fijar todavia** | **Despues de E11** (perfil axial de los tornillos reales) |
| D4 | Criterio de exito | forma del contraste, ya; margen de equivalencia, no | **Mixto**: la forma ya, el margen **despues del piloto sobre validacion** |

### D1 — mascara de entrenamiento: fijar ya, (a) piloto + (b) sensibilidad

Sin cambios respecto a la seccion 3. El argumento es que (a) es el unico umbral con validacion propia en esta
cohorte (E1: 0 falsos negativos en 113 candidatos; E8: mediana 5.00 mm de diametro externo), y que (b) existe
justamente para medir cuanto cambia el resultado si el borde se define mejor. Nada de esto depende de E11 ni de A1.

**Consecuencia que hay que aceptar al elegir (a):** E8 encontro que a 2500 HU los tornillos salen **fragmentados en
9 de 57** casos. Una `M` fragmentada en entrenamiento ensena al modelo que el metal puede tener huecos; la `M`
parametrica de sintesis sera siempre solida. Eso es #95 y **no lo resuelve la eleccion de umbral**: se declara.

### D2 — RESUELTA (2026-09-20): parche 256 y **unidad = COMPONENTE**

> El control de A1 sobre la cohorte **refuto** la lectura de abajo, que se conserva como registro de lo que se
> creia antes de medir. Decision de la autora del 2026-09-20; implicancia **#102**.

- **El parche se queda en 256 px.** No era pequeno: mide 211.7 mm de mediana, y agrandarlo no habria alcanzado
  para los 380 mm de un caso bilateral.
- **Lo que cambia es la unidad:** cada **componente conexo** de `M` con su propia `B_delta`, en vez de la union
  de todo el metal del corte. Script nuevo `a1b_parches_componente.py`; `a1_parches.py` queda **congelado** como
  evidencia de #102.
- **Verificado en los dos casos de prueba, uno de ellos el peor de #102** (`CLINIC_metal_0044`, que tenia
  215 de 298 cortes sin contener): **0 de 1217 parches** con `G` fuera del encuadre, frente al 20.1% por corte.
  Control de composicion 1217 de 1217.
- **Efecto secundario que hay que declarar:** **548 de 1217** parches contienen metal de **otro** componente. No
  se enmascara — es anatomia real del paciente — pero se **cuenta** (`n_metal_otros`), asi la mezcla se mide en
  vez de suponerse. Esto es material para #96, no una solucion de #96.
- **Coste:** el numero de parches sube (un corte con varios implantes produce un parche por implante), asi que el
  cache crece y la subida a Khipu pesa mas. Se mide al terminar A1b.

### D2 (lectura original, ANTES de medir) — parche 256 sujeto a un control

256 x 256 a ~0.78 mm cubre ~200 mm, que contiene el corredor completo mas 2 x 12 mm de banda; 128 no. La prueba en
2 casos dio **216 de 216 cortes contenidos**, pero 2 casos no son la cohorte.

**Control que puede cambiar esto:** A1 sobre la particion completa reporta la fraccion de `G` que no cabe en el
parche, por caso. Si esa fraccion es 0 en todos, 256 queda fijado. Si aparece cola, la respuesta **no** es agrandar
el parche sin mas (el computo crece con el cuadrado del lado): es mirar si los casos que se salen son protesis
grandes, que son precisamente los que la seccion 3 ya senala como riesgo de sesgo de la mezcla.

### D3 — RESUELTA CON MEDICION PROPIA (E11 corrido el 2026-09-20)

> **E11 ya corrio sobre los 178 volumenes.** La autora acepta la lectura el 2026-09-20; falta que la escriba en
> `01-decisiones.md` (regla 3). Registro completo: `experiments/objetivo2/e11_perfil_axial.md` e implicancia #101.

- **Cuerpo: cilindro uniforme de ~4.9 mm.** `d_centro` mediana **4.91 mm**, frente a 4.8 mm de catalogo
  (`synthes2003guide`) y 5.00 mm de E8: tres vias independientes dentro de un cuarto de voxel.
- **Cabeza y rosca: como sensibilidad, no en el piloto.** El ensanchamiento de extremo tiene mediana **0.96 mm**,
  del orden de un voxel, asi que en el caso tipico el volumen parcial las promedia. Pero **12 de 59** superan
  2 mm, asi que no se declaran inexistentes: entran como variante.
- **El filtro que produjo estas cifras es GEOMETRICO, no clinico** (HU > 2500, largo >= 30 mm, anchos <= 12 mm).
  Selecciona 79 componentes en 43 casos y **no afirma que sean tornillos iliosacros**: afirma que son componentes
  metalicos alargados y finos. Sus seis limitaciones estan listadas en `e11_perfil_axial.md`, seccion "EL FILTRO
  GEOMETRICO", y **cualquier cifra de E11 que vaya al documento tiene que ir con ellas**.
- **No citar `d_max` (8.10 mm) como diametro de cabeza medido:** es un maximo sobre tramos, sesgado al alza.

### D3 (justificacion original) — por que no se fijaba antes de E11

Esta es la unica de las cuatro que **no debe responderse hoy**. La pregunta es si la mascara de sintesis lleva un
tramo de rosca de 7.3 mm o un cilindro uniforme de ~5 mm, y esa pregunta tiene una medicion propia disenada para
contestarla: E11 mide el diametro exterior **a lo largo del eje** de los tornillos reales de la cohorte.

- Si el perfil se ensancha hacia el extremo distal -> la rosca **se ve** en el CT y la mascara la necesita.
- Si el volumen parcial lo promedia a ~5 mm -> el cilindro uniforme queda justificado **con medicion propia**, no
  por comodidad, y el catalogo (4.8 mm de fuste, `synthes2003guide`) pasa a ser corroboracion y no fuente unica.

En los dos casos la respuesta es **citable y verificable**, que es lo que el resto de este documento no tiene todavia.
Responder D3 antes de leer E11 desperdicia el unico experimento que la geometria del tornillo acaba de habilitar.

### D4 — criterio de exito: la forma se fija ya, el margen espera al piloto

`main.tex:98` promete *"Lower profile discrepancy than naive copy-paste insertion, with streak amplitudes
statistically comparable to, or better than, the adopted physics-based protocol"*. Son **dos contrastes distintos**
y hoy ninguno tiene prueba definida. Propuesta, en cuatro piezas:

**(i) Endpoint primario unico, declarado antes de mirar el test.** Una sola metrica de Peters, sobre los 14
pacientes de test sin metal, con las demas **descriptivas**. Sin esto se repite #76: seis combinaciones y basta con
que pase una. Recomendado como primario: **streak amplitude**, porque es la magnitud que el Objetivo 3 dice generar
y la unica que la copia-pega no puede producir por construccion.

**(ii) "Mejor que copia-pega" = superioridad, pareada y de una cola.** Mismos pacientes en los dos brazos, asi que
el contraste es pareado. Con n = 14 y sin supuesto de normalidad: **Wilcoxon de rangos con signo, una cola**,
alfa 0.05. Se reporta ademas el tamano de efecto y su IC, no solo el p.

**(iii) "Comparable al brazo fisico" = equivalencia, y NO un contraste de diferencia.** Este es el punto con mas
riesgo de error del documento. "Comparable" **no** se demuestra con un contraste de diferencia que sale no
significativo: un p > 0.05 con n = 14 es mucho mas probable que indique falta de potencia que igualdad, y un jurado
lo senala. Lo correcto es un **contraste de equivalencia (TOST)** con un margen `Delta` declarado de antemano, que
concluye equivalencia solo si el IC90 de la diferencia pareada cae entero dentro de `[-Delta, +Delta]`.

**(iv) De donde sale `Delta`, y por que todavia no se puede escribir.** No existe umbral publicado de "streak
amplitude comparable" (mismo hueco que el proyecto ya declaro para los 25 HU en `main.tex`, decision 2026-09-15 (2)).
Calibrar `Delta` sobre los resultados de test seria exactamente el patron prohibido. La salida limpia:

> `Delta` se fija como la **variabilidad propia del metodo bajo condiciones que no deberian cambiar el resultado**
> — dispersion entre semillas DDIM del mismo caso, y test-retest del brazo fisico — medida **solo en los 5
> pacientes de validacion**, nunca en los 20/14 de test, y escrita en `01-decisiones.md` **antes** de correr la
> evaluacion. El argumento es: si el metodo no se distingue del brazo fisico por mas de lo que se distingue de si
> mismo, "comparable" esta justificado; y ese numero es medible sin tocar el test.

Por eso D4 se marca **mixto**: (i), (ii) y (iii) se pueden escribir hoy; (iv) necesita el piloto sobre validacion.

**Declaracion de potencia, se escriba lo que se escriba.** n = 14 sin metal y n = 20 con metal son muestras
chicas para un TOST. Es muy posible que el resultado honesto sea *"no se pudo concluir equivalencia con esta n"*,
y **eso tambien es un resultado publicable** — el Objetivo 1 de esta misma tesis ya lo demuestra. Lo que no es
aceptable es convertir un no-concluyente en un "comparable" por la via del p > 0.05.

### Fuera de las cuatro: dos que el plan no lista como decisiones y lo son

- **Mitigacion de #96 (contexto con y sin artefacto).** La seccion 8.1 la deja "se decide tras la prueba corta".
  Eso convierte una decision de diseno en una reaccion a un resultado. Recomendado: declarar **ahora** que el
  piloto corre con contexto intacto, y que el contexto recortado/suavizado entra **solo** como brazo de
  sensibilidad preinscrito, no como arreglo posterior si la costura sale fea.
- **#98**, que es de `main.tex` y no de este documento, pero bloquea la misma frase que justifica `B_delta`.

## 9. Semana 1 (orden)

1. Autora responde los `[DECIDIR]` (mascara de entrenamiento, parche, diametro, criterio de exito).
2. Script de extraccion de parches y conteo (CPU, local), con control: fuera de `G` el parche compuesto es identico
   al original bit a bit.
3. Prueba corta en Khipu (200 pasos): s/paso y memoria.
4. Preinscripcion: este documento pasa a `PREINSCRITO` con fecha, y se registra en `01-decisiones.md`.
5. En paralelo: paso 0 de MAISI (normalizacion de HU en el codigo) y edicion de `main.tex` (titulo, Obj 1, Obj 3).
