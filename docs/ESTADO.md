# Estado actual

> Lo actualiza Claude al cerrar cada sesion. Fuente de verdad de "por donde voy".

## PUNTO DE RETOMA — leer esto primero (2026-09-11)

> Escrito para que una sesion nueva, sin historial, retome sin releer nada mas. Todo lo de
> abajo esta verificado contra archivos en disco. Las decisiones son de la autora: Claude no
> las aplica sin orden explicita (reglas 3, 4 y 14 de `CLAUDE.md`).

### Donde esta el proyecto

- **Literatura cerrada por saturacion; el proyecto esta en fase experimental.** `src/` sigue
  **vacio**: todo lo ejecutable esta en `experiments/`. Segun #23, la entrega queda a unas 12
  semanas.
- **Cohorte por paciente (decision del 2026-09-10):**
  - 178 volumenes = 168 pacientes (`Grupo paciente` en `revision.csv`).
  - Volumenes fuera de uso: `experiments/exploration-3d/exclusiones.csv` (11; ningun archivo
    borrado).
  - Particion por objetivo: `grupos.csv` (grupo 1 con material ortopedico = 65, grupo 2 = 37,
    grupo 3 limpio = 66).
  - `metal_0059` y `metal_0071` estan unidos sin perdida en `data/derivados/`.
- **`tesis/main.tex` compila** (4 paginas, 40 referencias, 0 citas indefinidas). Cambios
  recientes:
  - C1 reescrita;
  - parrafo `Implant geometry source` (geometria parametrica);
  - regla de aislamiento;
  - cifra de R1 en `Field limitation`.

### Lo que se midio (reproducible, en disco)

| Exp | Donde | Resultado vigente |
|---|---|---|
| E1 | `exploration-3d/sensibilidad_hu.py` | 2500 HU criba con 0 falsos negativos (113 candidatos) |
| Dup. | `exploration-3d/duplicados_parciales.py` | 6 grupos por SHA256 + 3 por cortes compartidos; todos resueltos por paciente |
| E6a / E6c | `objetivo1/` | Techo de 2000 HU de LW: 48 de 75 con metal fallan el Go/No-Go. `pub+MTW` (4a ventana) domina (#39) |
| R1 | `objetivo2/r1_*.py` | 65 pacientes: marco computable con S1 confirmado por revisor clinico **49**, sin contaminacion **30**. Revisor: medico ORL, ciego; acuerdo con el agente kappa 0.80 |
| E8 | `objetivo2/e8_*.py` | >= 17 de 65 con tornillo iliosacro; a 2500 HU los tornillos salen fragmentados (9/57) y con fuste de 5.1 mm (#46). Test-retest `0065`/`0066` |
| E9b | `objetivo2/e9b_*.py` | Alguna esfera de S1 con mediana < 150 HU en **38% con metal y 43% sin metal** (#48) |
| E9 | `objetivo2/e9_corredor.py` | **NO VALIDO**, no correr: el umbral HU no captura el esponjoso sacro (#48) |

### Decisiones tomadas en esta ronda (todas en `01-decisiones.md`)

1. **Unidad = paciente:** duplicados parciales, union, `metal_0068` sin material ortopedico,
   ningun `.nii.gz` se borra.
2. **#20:** indice menor en las copias exactas.
3. **#41 via (c):** geometria parametrica, calibre de 6.5-8.0 mm, cilindro liso. **Contingencia
   abierta:** via (a), extraer de CLINIC-metal, **solo** si a futuro falta por completo
   bibliografia de calibres y longitudes. La falta de rosca o cabeza no la dispara.
4. **#31:** `Dmax >= d_implante + 2c`, `c` = 1-2 mm radiales (operacionalizacion declarada de
   Kaiser).
5. **#22:** 2500 HU solo para cribado; metal integrity con la regla adaptativa de Peters.

### PENDIENTES PARA LA PROXIMA SESION, por urgencia

1. **#48: segmentacion osea para medir el corredor. Bloquea el Objetivo 2**, el unico aporte
   propio del minimo.
   - La autora elige via: TotalSegmentator (#29; necesita **Khipu**: la PC no tiene GPU y
     tiene ~2 GB de RAM libres), segmentacion cortical propia o semi-manual en un subconjunto.
   - Despues, rehacer E9 reutilizando la logica de `e9_corredor.py` (trayectorias, EDT,
     salida por el ilion, restriccion #31) sobre la mascara nueva, **con y sin los 7 de FOV
     cortado** (pedido de la autora, aun sin decidir).
2. **#36 + #39: VAE y ventanas, juntas. Bloquean el Objetivo 1**, que es obligatorio.
   - `main.tex` sugiere SD 1.5, cuyo VAE es de 3 canales; la mejor salida de E6c usa 4.
   - Opciones en #36/#39. E6b se corre en Khipu.
3. **Textos propuestos y no aplicados a `main.tex`:**
   - restriccion #31 en el Objetivo 2 (texto en #31, ronda 2026-09-11 tarde);
   - declaracion de que bone integrity (HU > 150) no captura el esponjoso sacro (#48, #17).
4. **Decisiones pequenas de la autora:**
   - los 7 de FOV cortado (cuando E9 sea valido);
   - tercera regla de umbral (semimaximo local para implantes reales, #22).
5. **Opcional, para blindar R1:** segundo revisor (radiologo o traumatologo) solo en los 17
   casos senalados en #26; revision clinica de crestas y EIPS.
6. **No urgente:**
   - revision de artefactos por la autora (#34, #35, #37; solo Objetivo 3);
   - candidatos PENDIENTE de `_candidatos.md`;
   - deuda: leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion.

### Avisos para quien retome

- **Memoria.** La PC tiene 11.8 GB y suele quedar con ~1.5-2 GB libres. Los scripts pesados
  corren por lotes reanudables (`--max`), en primer plano o con procesos nuevos por lote: dos
  corridas de fondo murieron por RAM. Lo que necesite GPU o modelos grandes va a **Khipu**
  (comandos de transferencia en el chat del 2026-09-10; host y usuario sin documentar).
- **Procedencia.**
  - `objetivo2/r1_auditoria_s1_clinico.csv`: medico ORL, **no la autora**.
  - `r1_auditoria_s1_agente.csv`: agente.
  - `revision.csv` solo se toca con scripts que verifican y respaldan (`procedencia.py`,
    `grupo_paciente.py`, `correcciones_autora.py`).
- **Historicos que no se usan:** `r1_landmarks.v1-parcial.csv`, `r1_landmarks.v2a.*`,
  `revision.pre-*.csv`.
- **Bibliografia:** `refs/raw` -> `refs/clean` -> `python scripts/build_refs.py` (regla 9). No
  editar `refs.bib` a mano.
- **Patron a vigilar (visto 5 veces):** un enunciado se vuelve verdad por citarse a si mismo, o
  un control que no puede fallar se toma por verificacion (#25, #37, #40, #45, #47). Verificar
  contra el archivo o el dato antes de construir encima.
- `04-implicancias.md` es el archivo critico irreemplazable (regla 17). Llega hasta la #48.

## Ultimo paso completado
2026-09-11 (cierre): #31 y #22 decididas y registradas; cifra de R1 escrita en `main.tex`; E9
(corredor) pilotado y **declarado no valido** por segmentacion (#48); E9b mide esponjoso de S1 bajo
150 HU en ~40% de los pacientes, con o sin metal; con y sin los 7 de FOV da lo mismo en densidad.
Siguiente: decidir la via de segmentacion (#48/#29, Khipu) y #36+#39. Detalle en PUNTO DE RETOMA.

## Paso anterior (2026-09-10 / 11, detalle)
2026-09-10: **R1 y E8 ejecutados enteros, y barrido de duplicados parciales.** #26 con cifra
provisional (52/69 marco computable con S1 correcto, 33 sin contaminacion; FOV y heuristica
pesan mas que el metal). #45 nueva: `metal_0059`/`0071` son el mismo estudio (contradice la
decision del 2026-09-07), mas `0011`/`0034` y `CLINIC_0038`/`0090`. #46 nueva: la via (a) de
#41 no produce geometria por umbral. #21: `metal_0068` sin osteosintesis densa.
Cierre del 2026-09-10: la autora **confirma** mismo paciente en los tres pares de #45, que
`0065`/`0066` son la misma persona y que `metal_0068` no tiene material ortopedico. Queda en
#45 una propuesta por par: contenedor, union sin perdida o par de reproducibilidad. Con
ella, dataset7 con osteosintesis pasa a 71 volumenes y 65 pacientes. Tambien hay texto
propuesto para `01-decisiones.md`, sin aplicar.
**Aplicado por orden de la autora:** union sin perdida de `0059`/`0071` en `data/derivados/`
y `Grupo paciente` lleno: 178 volumenes, 168 pacientes; dataset7 con osteosintesis 71/65,
dataset6 sin objeto 70/69.
**Cierre final del 2026-09-10 (orden de la autora):** decision por paciente escrita en
`01-decisiones.md`; `exclusiones.csv` creado (11 volumenes, ningun archivo borrado);
`metal_0068` corregido; `grupos.csv` regenerado (65/37/66); R1 y E8 recontados por paciente:
marco computable con S1 correcto 51/65, sin contaminacion 32/65; >= 17 con tornillo
iliosacro; fuste 5.08 mm.
#20 CERRADA por la autora (indice menor). Mosaicos regenerados sobre 65 pacientes y
plantilla ciega `experiments/objetivo2/r1_auditoria_s1_clinico.csv`.
2026-09-11: la plantilla de S1 la lleno un **medico cirujano ORL** (revisor clinico externo,
no la autora). Con el como referencia: **49/65** marco computable con S1 correcto, **30/65**
ademas sin contaminacion; acuerdo con el agente kappa 0.80. #20 escrita en `01-decisiones.md`.
2026-09-11 (2): **#41 via (c) APLICADA** en `01-decisiones.md` y `main.tex` (Objetivo 2,
regla de aislamiento, parrafo `Implant geometry source`; compila). **Contingencia (a)
ABIERTA:** extraer geometrias de CLINIC-metal si a futuro falta por completo bibliografia
con calibres y longitudes (no la disparan rosca, canulacion ni cabeza). Plantilla renombrada
por la autora a `r1_auditoria_s1_clinico.csv`. Lectura de `xie2024` (#47) lanzada.
Xie leido (#47): cita de C1 PARCIALMENTE respaldada (sobrecobertura solo en cortes simulados;
direccion dependiente del umbral); redaccion alternativa de C1 propuesta, sin aplicar.
Por orden de la autora: `grass2016`, `lee2014`, `wagner2017` y `zhao2012` anadidas a `refs.bib`
(36 -> 40, MAPEO actualizado; tesis compila: 4 paginas, 0 citas indefinidas, 2 avisos ya
conocidos) y `00-tesis.md:114` pasa de 'CAD propia' a geometria parametrica.
C1 reescrita en `main.tex:54` por orden de la autora; **#47 CERRADA**.
Siguiente: FOV del Obj 2 (7 pacientes sin crestas); cifra de R1 (49/65, revisor clinico) en
`main.tex:115`.

## Paso anterior
2026-09-09 (cierre real): **#40 RESUELTA y #41 abierta, y es lo mas grave de la sesion.**
La autora identifico el origen del "banco de 61": es la cita de `liu2021ctpelvic1k`,
Data annotation p. 3, *"The remaining 61 metal-affected CTs ... left unannotated"*.
Confirmado contra la ficha ya verificada y contra la Tabla 1 (`0(61)/0/14`), y contra el
disco: **61 + 14 = 75 = dataset7**. `CLAUDE.md:23` encadena dos errores de categoria:
CT de pacientes leidos como geometrias de implante, y dataset publico de terceros leido
como "insumo propio". **#41: C1 se queda sin insumo.** No existe ninguna fuente de
geometrias de implante en el repositorio, y con eso el Objetivo 2 (unico aporte propio del
minimo viable) no tiene que colocar, **#31 colapsa** (`d_implante` no existe), `main.tex:111`
regula un banco inexistente y `00-tesis.md:114` habla de un CAD propio que no hay.
Opciones ejecutables con lo que hay en disco: (a) extraer geometrias de los implantes de
los 75 CLINIC-metal, con la tension de aislamiento que eso implica, o (c) geometrias
parametricas con los rangos publicados de #30 y #31. Propuesta de correccion de
`CLAUDE.md:23` redactada en #40, sin aplicar.
Precision: 1184 y 75 son cifras del propio paper de 2021 (Introduction p. 2 y Tabla 1
p. 3), no una actualizacion posterior. **#40 CERRADA el 2026-09-09**: la autora retira su
observacion sobre el dataset y confirma que el estado de ANOTACION de los 61 no ha
cambiado y que la lectura de la evidencia textual era correcta. Sin efecto sobre #13
(siguen 14 de 75 anotados) ni sobre #41, que sigue ABIERTA.
Siguiente: la autora decide #41 (de donde salen las geometrias) — es ahora el bloqueo
numero uno del alcance minimo, por delante de #37, #39 y #36.

## Paso anterior
2026-09-09 (cierre): **E6a ejecutado** y **bloqueo declarado por pedido de la autora**.
E6a mide el tramo `HU -> ventana -> HU` del Objetivo 1 (sin VAE, cota inferior de
cualquier decodificador). Dos hallazgos: **#38**, las tres ventanas publicadas son
**redundantes en reconstruccion** (`max |LW - oraculo|` en hueso a float = **0.0 exacto**;
la unica ganancia es 1.679 HU a 8 bits, o sea cuantizacion, no rango) — no refuta C3, pero
si refuta que la multi-ventana **preserve mejor los HU**; y **#39**, el Go/No-Go
**no puede fallar** en pelvis limpia (mediana **0.00 HU**) y **falla en 48 de 75** con
metal (mediana 46.36, max 274.49), antes del VAE, solo por el techo de 2000 HU de LW.
En ROI de metal el MAE es **3588.80 HU** de mediana, con HU maximo mediano de 18 822 y
pico 24 970 contra un techo de 2000: **la representacion no puede codificar lo que la
tesis debe generar.** `main.tex` no declara sobre que cohorte se evalua el Objetivo 1.
**Bloqueo declarado:** #15, #22, #34 y #35 detenidas hasta que la autora marque artefactos.
Afecta solo la cohorte del Objetivo 3; Obj 1 y Obj 2 siguen libres.
Antes tambien: **#34 corregida por procedencia** (la columna `Artefactos` la llenaron los
agentes desde laminas, no la autora; sus 20 `no` son afirmaciones de ausencia fragiles),
**#35** (una cohorte para tres consumidores), **#36** (el VAE del Obj 1 no esta
especificado en ningun documento) y **#37** (`revision.csv` no declara procedencia por
campo).
Siguiente: la autora decide **#37 primero** (procedencia por campo) y luego hace la
revision visual de estriacion sobre los 33 volumenes de dataset6 con objeto. En paralelo,
decidir #38/#39 (que hacer con el techo de 2000 HU) y #36 (que VAE). Sigue sin ubicarse el
banco de 61 geometrias.

## Paso anterior
2026-09-09: **primer experimento del giro a benchmarks (E1)**. Corrido
`experiments/exploration-3d/sensibilidad_hu.py` sobre los 178 volumenes locales (solo
lectura; `revision.csv` intacto). **#22 EJECUTADA**: 1500 HU deja 177 de 178 como
candidatos y **queda descartado** (entra hueso cortical); 2500 HU da 113 candidatos, 65
limpios y **cero falsos negativos** contra la revision 3D de la autora; 3500 HU da 104
candidatos y 74 limpios pero **pierde 5 metales reales**. Cambios de clase: 64 de 1500 a
2500, 9 de 2500 a 3500. Las 178 clasificaciones a 2500 reproducen exactamente
`revision.csv`. **#34 nueva**: los 5 que pierde el 3500 son los cinco `accesorio`
extracorporeos de dataset6, asi que el umbral y la definicion de `Objeto extraño` son la
misma decision (2500 -> 65 limpios; 3500 -> 74 limpios). Ademas, analisis de prioridad de
las 34 implicancias y cola de experimentos E1-E6 propuesta.
Siguiente: **E6, el Go/No-Go del Objetivo 1** (MAE < 25 HU en hueso del round-trip
multi-ventana), que no tiene ningun bloqueo. Antes de E2 y E3 hacen falta tres decisiones
de la autora: adoptar o no TotalSegmentator (#29), donde esta el banco de 61 geometrias
(NO esta en `data/`, que solo tiene dataset6 y dataset7), y si se adopta la formulacion
parametrica `Dmax >= d_implante + holgura` (#31).
Aviso de estado del repo: `docs/04-implicancias.md`, `refs.bib` y `tesis/main.pdf` siguen
modificados sin commitear desde el 2026-09-08, mas 15 `refs/raw/*` sin trackear.

## Paso anterior
2026-09-08: cerrada la seccion "la geometria que McLaren NO publica" con 7 lecturas
(`grass2016`, `wagner2017`, `lee2014`, `hasenboehler2011`, `zhao2012`, `mendel2011`,
`gottschling2009`). La geometria SI existe pero en marcos que no componen (#30); Gras y
Wagner se invierten el orden S1/S2 por definicion distinta de diametro (#30b, corrobora
#12 y #27); el umbral es siempre calibre de tornillo mas holgura en 7 fuentes, lo que
habilita expresarlo como `Dmax >= d_implante + holgura` sobre el banco de 61 (#31);
Gottschling es de femur y tibia (#32); el "hasta 50%" de dismorfismo no lo sostiene
ninguna de las tres fuentes citadas (#33). Busqueda de corredor: **cerrada por saturacion**.
Decision de la autora: cerrar **tras** dos lecturas finales (`carlson2000`, `ebraheim1997`),
y cierre **reversible** si los experimentos revelan que falta geometria. **Ebraheim leido**
(pediculo S1 en mm, entrada a 3-3.5 cm del borde posterior del ilion, margen 4-6 mm entre
dos tornillos; sin angulos, sin S2; septimo marco incompatible, #30 ampliada).
**Carlson BLOQUEADO: falta el PDF y el raw.** Unica candidata de reapertura anotada:
Morse 1994, angulos para tornillo sacro sobre TC preoperatoria.
Siguiente (decidido por la autora): cerrar los tres pendientes de datos — cifra de R1 (#26),
tabla de sensibilidad HU 1500/2500/3500 (#22) y representante de los 3 grupos duplicados
(#20, que bloquea el split). Todo sobre datos ya en disco.

## Paso anterior
2026-09-08: evaluado TotalSegmentator para el Objetivo 2 (#29 ABIERTA). Es util como
ROI/mascara anatomica inicial (`sacrum`, S1, caderas), no entrega S2, cortical, landmarks
ni corredor y no esta validado aqui bajo metal. Recomendado piloto 1.5 mm + QC local;
pendiente decision de adopcion. No cambia SAP ni downstream.

## Paso anterior
2026-09-08: Keating 1999 leido con `lector-papers` desde DOCX completo sin paginacion.
SI publica malposicion en 5/38 pacientes (13%): fuente indirecta via Hinsche y punto
interior, no origen del rango 2%-15% ni de sus extremos. Binario, radiografico, sin
S1/S2 ni escala SAP; #12 no se reabre. `refs.bib` = 36; tesis recompilada sin citas
indefinidas. Siguiente: sensibilidad HU y #26.

## Paso anterior
2026-09-08: Gardner incorporado como respaldo anatomico S1/S2 en `00-tesis.md`,
`01-decisiones.md` y `main.tex` (Problem Statement y Objetivo 2), por encargo de la autora.
Se mantiene geometria individual sin fenotipos y benchmark ordinal SAP solo en S1.
PDF recompilado: 4 paginas, sin citas indefinidas. Siguiente: sensibilidad HU y landmarks (#26).

## Paso anterior
2026-09-08: auditada consistencia de Gardner contra su ficha ya leida. Corregidos
candidatos, indice, ficha e implicancias: LEIDO; areas S1/S2 similares en dismorficos,
no inversion ni prior ordinal. Sin cambio de alcance: geometria individual sin fenotipos;
SAP clinico solo S1. Siguiente: sensibilidad HU y landmarks (#26).

## Paso anterior
2026-09-08: van den Bosch leido con `lector-papers`; 6/31 vs 1/49 son pacientes con
quejas neurologicas, no malposicion por nivel. #28 resuelta; #12 cerrada delimitando
SAP ordinal a S1 por tecnica, S2 descriptivo. Aplicado en tesis y alcance; 35 referencias.
Siguiente: sensibilidad HU y landmarks (#26). Prior ordinal clinico S2 sigue no disponible.
Validacion: PDF recompilado, 35 entradas y ninguna cita indefinida; dos avisos BibTeX
ya documentados por revistas sin volumen (Hinsche y Templeman).

## Paso anterior
2026-09-08 (cierre): auditada entera la cadena de citas del umbral de 10 mm con tres
lecturas mas (`ziran2007fluoroscopic`, `moed2006s2screw`, `gardner2010safezones`).
**Cuatro eslabones, ninguno lo mide**: Ziran no contiene el umbral, el "1 cm" de Moed es
separacion interforaminal (otra magnitud), Kaiser lo elige y Gardner lo declara como
consenso por calibre de tornillo. Conclusion: **nunca fue una medicion, es una convencion
profesional**, y la tesis lo afirma con frases literales. Cadena declarada agotada.
Decisiones de la autora aplicadas: **no estratificar por fenotipo** (#27 CERRADA, y con eso
la objecion de Carlson 2000 deja de aplicar); la geometria en pelvis intactas se reescribe
como **limitacion del campo** en `main.tex`; se anade el respaldo **anatomico** de C2 con
los coeficientes de variacion de Ziran (hasta 97-140%); se adopta la **tabla de
sensibilidad** de cribado a 1500/2500/3500 HU; Ziran queda N2 y Moed baja a **N2
provisional**. `refs.bib` = 34. 16 decisiones fechadas en `01-decisiones.md`.
**#28 nueva**: van den Bosch preparado con el encargo completo redactado y SIN ejecutar.
Siguiente: conseguir el PDF de van den Bosch (decide el eje S1/S2 y puede cerrar #12),
correr la tabla de sensibilidad y la cifra de R1 (#26). Ambas sobre datos ya en disco.

## Paso anterior
2026-09-08 (tarde/noche): la autora adopto las opciones recomendadas y autorizo
aplicarlas. **APLICADO** en `tesis/main.tex` (RQ e hipotesis sin downstream, Obj 5
eliminado con parrafo `Explicitly out of scope`, Obj 4 con SAP como unica metrica propia
y metricas de Peters con sus nombres, C3 reescrita, el rango 31-60% sustituido por las dos
distribuciones ordinales de Zwingmann condicionadas por tecnica y nivel sacro, zona segura
via McLaren con el umbral declarado heredado), en `docs/00-tesis.md` (`Fuera de alcance`
escrito con seis puntos) y en `docs/03-glosario.md` (escrito entero). Compila limpio, 31
entradas. **#14 y #16 CERRADAS**; #13 y #18 degradadas a limitacion declarada.
Alta y lectura de `kaiser2014dysmorphism`: **no** establece el 10 mm (tercer salto de
cita, hacia Gardner 2010 / Ziran 2007 / Moed 2006), pero aporta el marco de referencia
calculable (reformateo perpendicular al platillo de S1, angulo coronal vs crestas iliacas,
angulo axial vs espinas iliacas posteriores, margen cortical de 5 mm, tres fenotipos).
**#26 nueva**: Kaiser midio en pelvis SIN implante y excluye los CT con metal.
Siguiente: la autora decide sobre las cinco propuestas de Kaiser (a-e), y falta que
recoja en `01-decisiones.md` las seis decisiones ya aplicadas.

## Paso anterior
2026-09-08: alta de 3 fuentes (`mclaren2021corridor`, `hinsche2002fluoroscopy`,
`templeman1996proximity`) y llegada del PDF de `wang2025adaptiveweighting`. `refs.bib`
regenerado a 30 entradas. Tres lecturas con `lector-papers`. Resultado: **#1 CERRADA**;
**#2 confirmada** contra el cuerpo; **#7 pasa a PARCIALMENTE CUBIERTA** (McLaren da
umbral y procedimiento, no geometria parametrizada); **#12 agravada** (el 2-15% es cita
de tercera mano y Hinsche es banco sobre plastico); **#13** con tres datos cruzados;
**#24 nueva** (el respaldo de C3 es fuente secundaria y el mecanismo es cascada, no
codificacion de entrada); **#25 nueva** (patron sistemico: tres anclas cuantitativas son
citas heredadas). Decision de la autora tomada: adoptar metricas de Peters, Obj 5 fuera
de alcance, Obj 4 modificado; falta registrarla en `01-decisiones.md` y aplicarla.
Siguiente: que la autora elija opciones en #7, #12, #24 y #25, y decida el nivel de
McLaren (ficha dice N2, `_index.md` dice N1).

## Paso anterior
2026-09-07: cerrados tres pendientes abiertos por orden de la autora.
(1) **LNCS: se ignoran.** La tabla con los volumenes retirados salio de `refs/MAPEO.md`;
en su lugar queda la decision de no perseguirlos, sin los valores, para que nadie los
reintroduzca sin respaldo en `refs/raw/`. (2) **`.gitignore` limpio**: se quitaron el
`@'` inicial y la linea `'@ | Set-Content ...` final; las reglas se verificaron con
`git check-ignore` (`papers/`, `data/`, `*.nii.gz`, `*.bbl`). (3) **`main.tex` migrado a
BibTeX**: `natbib` con `abbrvnat`, `\bibliography{../refs}` y las 19 citas del cuerpo
convertidas a `\citep`/`\citet`/`\citealp`. La lista en texto plano (27 entradas a mano)
desaparecio; ahora sale de `refs.bib`. Compila limpio, 0 citas indefinidas, 27 entradas
en el `.bbl`, y las citas del cuerpo se imprimen igual que antes.
Siguiente: cerrar el representante de los 3 grupos internos de dataset7.

## Paso anterior
2026-09-07: montado el pipeline bibliografico `refs/raw` -> `refs/clean` -> `refs.bib`
por encargo de la autora. 27 fuentes del editor (16 nbib de PubMed, 10 bib, 1 txt),
27 entradas normalizadas en `refs/clean/`, procedencia y reglas en `refs/MAPEO.md`,
regeneracion con `scripts/build_refs.py`. Los 27 DOIs y las 27 claves quedaron
identicos; se corrigio `issue`->`number` en tres entradas (fasciculo que BibTeX
descartaba), se desambiguo `CORR`, se completaron autores y el volumen de SPIE.
`main.tex`: 15 correcciones en la lista de referencias, sin migrar a BibTeX.
Cerrado con los 5 .bib oficiales que pego la autora: `wu2022xcist` confirmado por IOP,
`ramadanov2025safezone` por MDPI, y los tres volumenes LNCS retirados porque el
exportador de Springer no los trae. `refs.bib` sin ningun `% VERIFICAR`. Decision de
precedencia registrada en `01-decisiones.md` con orden explicita.
Regla 9 de `CLAUDE.md` reescrita y marcas eliminadas de `refs.bib`.
Siguiente: cerrar el representante de los 3 grupos internos de dataset7.

## Paso anterior
2026-09-07: la autora reviso en 3D los 178 volumenes; fusionadas sus tres reglas de
clasificacion con la investigacion de los agentes en `revision.csv` (178 filas,
`3D completa`). Cifras: dataset7 con material ortopedico 72 de 75 (69 de contenido
unico); dataset6 con objeto 33, de ellos 27 solo extracorporeo; 70 candidatos a
entrenamiento limpio. #20 y #21 resueltas en criterio, #22 cuantificada (27 volumenes
en juego). #19 estrechada: `CLINIC_0074` resuelto (hay lazo, no es metal) y regla nueva
"autora sin objeto + agente incierto = sin objeto". `metal_0059`/`metal_0071` descartado
como par. Textos "preliminar" borrados de metal_0002 y metal_0003.
Siguiente: que la autora copie sus reglas a `01-decisiones.md` y elija representante en
los 3 grupos duplicados internos de dataset7.

## Paso anterior
2026-09-07: corridos 12 agentes `clasificador-metal` sobre los 113 candidatos HU.
113 filas en `propuesta_clasificacion.csv`, todas `propuesta sin validar`; `revision.csv`
intacto (sigue con 3 filas parciales). Metal: 65 `si (propuesto)`, 42 `incierto`, 1 `no`,
5 mixtos. Cuatro implicancias nuevas #19-22: el umbral HU no detecta (objeto bajo 1500 HU
en CLINIC_0074), duplicados CRUZADOS entre sub-datasets (fuga train/test), CLINIC-metal
con material extracorpóreo, y `Objeto extraño` sin definicion operativa.
Siguiente: decidir #19 (revisar los 178) y #22 (definicion), resolver duplicados.

## Paso anterior
2026-09-07: auditado `experiments/exploration-3d` contra el encargo de Victor.
Descripcion de datos cubierta para lo local; metal y split instrumentados pero SIN
ejecutar (0 de 178 confirmadas, 166 pendiente + 12 duplicado). Nuevo: solo 178 de los
1184 volumenes de CTPelvic1K estan en disco -> implicancia #18. Construido (no corrido)
el subagente `clasificador-metal` con `laminas.py` y `propuesta_clasificacion.csv`.
Siguiente: correr el agente sobre los 113 candidatos y los 65 no candidatos de dataset6.

## Paso anterior
2026-09-07: adopción de Peters registrada en `01-decisiones.md` con autorización.
Índice y fichas armonizados: Peters N1, Wu/XCIST N2; N4 de descartes creado y vacío.
Siguiente: concretar adaptación/validación del protocolo (#16–17) y armonizar `00-tesis.md`.
Continúan pendientes revisión 3D completa, pacientes/duplicados y máscaras.

## Paso anterior — exploración 3D
2026-09-07 (cierre del encargo del 06): flujo 3D con un script y un CSV listo;
178 CT, 113 candidatos HU, 6 grupos duplicados, 3 revisiones parciales. Peters en main.tex.
Siguiente: completar revisión 3D+cortes, resolver duplicados/pacientes y máscaras.
Nuevas implicancias #15–17; #8 aplicada a redacción, validación técnica pendiente.

## Paso anterior — verificación bibliográfica
P4: verificacion de niveles con 10 subagentes `lector-papers`, uno por PDF. **6 de mis
7 movimientos verificados estaban mal.** Reparto corregido a 8/12/7, con 10 fichas
nuevas. Salieron 4 implicancias (#7 a #10) y se actualizaron #5 y #6 con evidencia
textual. `_candidatos.md` poblado con 21 candidatos de snowballing.

## Paso anterior
P3: niveles de `_index.md` reasignados por el criterio nuevo de la autora (riesgo
sobre el argumento central o el benchmark).

## Paso anterior
P2: `docs/literatura/_index.md` completado. Las 27 entradas de `refs.bib` tienen fila,
con estado del PDF y acceso. Inventario: 25 de 27 PDFs presentes; faltan
`wang2025adaptiveweighting` y `zhang2026pediclescrew`.

## Paso anterior
P1: `refs.bib` generado desde la seccion References de `tesis/main.tex`. 27 entradas,
claves `apellidoANIOpalabraclave`. Las 27 quedaron marcadas `% VERIFICAR`.

Ademas: `scripts/renombrar_papers.sh` generado (NO ejecutado). Los 25 PDFs
emparejados, ninguno pendiente. Conflicto de claves resuelto: manda `refs.bib`,
se corrigio `_index.md`. Ficha de `wang2025adaptiveweighting` creada desde abstract.

## Pendientes bibliográficos anteriores
Decidir sobre la implicancia #9 (reenunciar el gap) y la #7 (el muestreador sin fuente
operacional de zona segura). Las dos tocan el alcance minimo viable y ninguna se puede
resolver leyendo mas: son decision de la autora. En paralelo, conseguir McLaren 2021,
que es la posible solucion de #7.

## Pendientes abiertos
- La bibliografia crecio de 2 a 3 paginas al migrar a BibTeX. No es un error: la lista
  a mano llevaba `et al.` y omitia DOI, editores e ISBN; la generada los imprime todos.
  Se probo `plainnat`, `abbrvnat` y `biblatex` con `maxbibnames=1`: las tres dan
  3 paginas. Si hay limite de dos, la decision es de la autora y las palancas son
  quitar los DOI del impreso o bajar el cuerpo de letra de la lista.
- 11 de las 27 entradas no se citan en el cuerpo (`karageorgos2024ddpm`,
  `kazerouni2023diffusionsurvey`, `ren2022metalinsertion`, `rombach2022latentdiffusion`,
  `selles2024marreview`, `singhrao2024fiducial`, `vanbosse2011pelvicpositioning`,
  `wang2019cochlear`, `yun2026simulationdriven`, `zhang2023controlnet`,
  `zhang2026pediclescrew`). Las sostiene `\nocite{*}`, puesto para que la lista siga
  siendo exactamente la que definio la autora. Citarlas en el cuerpo o retirarlas es
  decision suya; sin `\nocite{*}` la lista bajaria a 16 entradas.
- Implicancia #1 ABIERTA: `wang2025adaptiveweighting` es nivel 1 y solo hay abstract.
  Al llegar el PDF, releer con `lector-papers` y regenerar la ficha completa.
- Implicancia #2 ABIERTA (GAP): el multi-ventana publicado es todo de remocion, no
  de sintesis. Verificar el reclamo de novedad antes de escribirlo.
- Implicancias #3 y #4 ABIERTAS, ambas de `zhang2026pediclescrew`: colision de
  encuadre con mi novedad, y una segunda escala de brecha cortical con umbral de
  2 mm que toca la definicion de BFC.
- Implicancia #5 ABIERTA, ACTUALIZADA: `liu2025pipeline` no compite en metodo (plan
  optimo determinista), pero define CSV y QID sobre CTPelvic1K, vecinas de SAP y BFC.
- Implicancia #6 ABIERTA (GAP), ACTUALIZADA: `ren2022` aporta la frase que fundamenta
  el gap pero no sirve de brazo de comparacion (exige raw data de fabricante).
- Implicancia #7 ABIERTA (RIESGO): el muestreador se queda SIN fuente operacional de
  zona segura. Toca el alcance minimo viable. La mas urgente.
- Implicancia #9 ABIERTA (GAP): insertar metal sintetico ya es practica establecida en
  4 trabajos, y la difusion latente ya compitio en MAR. Hay que reenunciar la novedad.
- Implicancia #10 ABIERTA (REDACCION): `chen2024tumorsynthesis` no modela nada fuera de
  la mascara y trunca HU a [-175,250]: respaldo citable de B_delta y de C3.
- `karageorgos2024ddpm`: el subagente propuso N1, se mantuvo en N2 por consistencia.
  Disenso registrado en `_index.md`; decision de la autora.
- `chen2024tumorsynthesis`: candidato a subir a N1, sin decidir.
- Implicancia #11 ABIERTA: SAP ignora la segunda escala (angular) de `smith2006iliosacral`,
  y las tasas de ese paper son cadavericas n=4: no sirven de prior clinico.
- Implicancia #12 ABIERTA (RIESGO, la mas grave): el rango 31-60% NO aparece en
  `zwingmann2009navigated`. Son dos complementos derivados de dos brazos distintos.
- Implicancia #13 ABIERTA (RIESGO): CLINIC-metal tiene solo 14 de 75 volumenes anotados,
  el paper no dice que metal contiene, y no da cifra de degradacion.
- Implicancias #19-22 ABIERTAS, todas de la clasificacion asistida, pero
  estrechadas por la revision 3D del 2026-09-07:
  - #19 estrechada: `CLINIC_0074` resuelto (no es metal). Siguen vivas dos patas,
    el artefacto que fabrica componentes y la mesa del escaner como componente.
    Opcion 1 (correr laminas sobre los 65 no candidatos, ~25 min) sigue abierta.
  - #20: criterio cruzado ya dictado por la autora; falta elegir representante en
    los 3 grupos internos de dataset7 (`0012`/`0021`, `0013`/`0043`, `0046`/`0074`).
    Hasta eso, sigue bloqueando el split.
  - #21 CONFIRMADA con cifra: 3 de 75 de CLINIC-metal no tienen osteosintesis.
    El test es 72, de contenido unico 69. Falta fijar esa cifra.
  - #22 sin decidir, y es la mas barata: define 70 vs 97 volumenes de entrenamiento.
- Implicancia #18 ABIERTA (DATOS): en disco hay 178 de los 1184 volumenes de
  CTPelvic1K; faltan ABDOMEN, COLONOG, MSD_T10, KITS19 y CERVIX. Decidir si se
  descargan o si el alcance de datos se declara como CLINIC + CLINIC-metal.
- Encargo de Victor a medias: `experiments/exploration-3d/cumplimiento-encargo.md`
  detalla que sub-tarea esta cubierta. `clasificador-metal` ya corrio y la revision
  3D esta completa; falta representante en los 3 grupos internos de dataset7 y
  `Grupo paciente`, vacio en las 178 filas, antes de cualquier split.
- Implicancia #14 ABIERTA (GAP): `peters2025hybrid` da la base operacional de BFC e ISC y
  sostiene por escrito la novedad del muestreador. La lectura mas productiva de todas.
- Falta armonizar el alcance completo de `00-tesis.md` con la adopcion de Peters
  (su frase sobre reimplementacion independiente de XCIST).
- Verificacion de #13 pendiente y no bibliografica: mirar los volumenes para saber que
  metal contienen. (La otra —si CLINIC-metal amplio su anotacion desde 2021— quedo
  CERRADA el 2026-09-09 con el cierre de #40: no se amplio.)
- `wang2025adaptiveweighting`: unico N1 SIN VERIFICAR, tercera ronda bloqueado por el PDF.
- Faltan por verificar tambien:
  `arand2019pelvicring` y `xie2024implantsegmentation`.
- `SAP`, `BFC` e `ISC` siguen sin definir en `docs/03-glosario.md`. El nivel de
  `xie2024implantsegmentation` y el de `liu2025pipeline` dependen de esas definiciones.

## Pendientes cerrados
> Lo que ya no requiere accion. Se conserva para no reabrirlo por olvido.

- **Implicancia #8 — APLICADA (redaccion).** La autora adopto el protocolo de
  `peters2025hybrid` como brazo de comparacion en lugar de la reimplementacion de
  XCIST; `wu2022xcist` no valida metal. Decision registrada en `01-decisiones.md`
  con autorizacion el 2026-09-07 y escrita en `main.tex`. Lo que sigue vivo es #17
  (ejecucion, configuracion y validacion) y armonizar `00-tesis.md`.
- **`zhang2026pediclescrew`: nivel resuelto.** Queda en nivel 1 por el criterio de
  riesgo, al ser origen de las implicancias #3 y #4.
- **Mapeo difftumor = `chen2024tumorsynthesis`: RESUELTO** contra el PDF.
- **Par `metal_0059` / `metal_0071`: DESCARTADO.** La autora confirmo el 2026-09-07,
  tras revision 3D, que no son el mismo paciente: comparten spacing y HU minimo, nada
  mas. Sin `Grupo paciente` comun. Registrado en `01-decisiones.md`.
- **#20, criterio cruzado: DICTADO.** En un grupo duplicado que cruza sub-datasets
  prevalece el volumen de dataset7 como representante, y ese volumen queda marcado
  sin material ortopedico. Afecta a `metal_0061`=`CLINIC_0037`,
  `metal_0036`=`CLINIC_0048`, `metal_0064`=`CLINIC_0070`.
- **#19, conflictos autora/agente: RESUELTOS.** `CLINIC_0074` tiene una estructura en
  lazo pero no es metal, asi que sigue siendo candidato limpio. Regla general dictada:
  autora «sin objeto» + agente `incierto` = sin objeto. Cierra los cinco desacuerdos
  menores.
- **Revision 3D de los 178 volumenes: COMPLETA** (`3D completa`, no recorrido de
  cortes). Fusionada con la investigacion de los agentes en `revision.csv`.
- **Textos «preliminar»** borrados de `metal_0002` y `metal_0003`.
- **`refs.bib`: los 27 DOIs, PUESTOS y VERIFICADOS contra el raw del editor.**
  Ninguno cambio al reconstruir el archivo, ni se anadio ni se quito ninguna entrada.
- **Pipeline bibliografico `raw` -> `clean` -> `refs.bib`: MONTADO** el 2026-09-07 por
  encargo de la autora. `refs/raw/` (27 fuentes del editor, intactas), `refs/clean/`
  (27 entradas normalizadas a mano), `refs/MAPEO.md` (procedencia y reglas) y
  `scripts/build_refs.py`, que regenera `refs.bib`. Los `% VERIFICAR` obsoletos
  desaparecieron; quedan 4 nuevos, reales.
- **Bug de compilacion corregido: `issue` -> `number`** en `liu2021ctpelvic1k` (16(5)),
  `xie2024implantsegmentation` (24(1)) y `zhang2026pediclescrew` (34(4)). BibTeX
  clasico descarta `issue` sin avisar: esos tres fasciculos no se habrian impreso.
- **`CORR` desambiguado** a *Clinical Orthopaedics and Related Research* en
  `vanbosse2011pelvicpositioning` y `zwingmann2009navigated`. Se confundia con el
  repositorio de preprints *CoRR* de arXiv. Igual `IEEE TMI` e `Int J CARS`.
- **`deman2007catsim` volume 6510**, que faltaba, confirmado por el raw de SPIE.
- **Autores completos en las 27.** Antes 25 decian `and others`.
- **Precedencia dictada por la autora (2026-09-07): manda `refs/raw/`,** y en su
  defecto `refs/clean/`. Un campo que el raw no confirme no se conserva por costumbre.
  Pendiente que la autora lo copie a `01-decisiones.md`.
- **`ramadanov2025safezone`: raw RESUELTO** el 2026-09-07. La autora sustituyo el .txt
  degradado por el .bib real de MDPI y borro el .txt. Confirma 14(10):3567, el DOI que
  ya estaba, y que el titulo si lleva los dos puntos. Es la fuente de la implicancia #7.
- **Los 4 campos sin respaldo: CERRADOS** el 2026-09-07 con los .bib oficiales.
  `wu2022xcist` CONFIRMADO por IOP (`pages = {194002}`, 67(19)). Los tres volumenes
  LNCS RETIRADOS de `refs.bib` y de `main.tex`: el exportador de Springer no los da.
  `refs.bib` ya no tiene ningun `% VERIFICAR`.
- **Decision de precedencia REGISTRADA** en `01-decisiones.md` el 2026-09-07 con orden
  explicita de la autora.
- **Regla 9 de `CLAUDE.md` REESCRITA** el 2026-09-07 con orden explicita: describe el
  flujo `raw` -> `clean` -> `refs.bib` generado, prohibe cualquier campo sin respaldo
  en el raw y mantiene que la lista de entradas la define la autora.
- **Marcas eliminadas de `refs.bib`.** Ni `% VERIFICAR` ni `% NOTA`: lo que esta en el
  archivo tiene respaldo en el raw. Lo retirado queda solo en `refs/MAPEO.md`.
- **`main.tex`, MIGRADO A BIBTEX** el 2026-09-07 con orden explicita de la autora.
  `\usepackage[round,authoryear]{natbib}`, `\bibliographystyle{abbrvnat}` y
  `\bibliography{../refs}` dentro del `multicols`, con `\renewcommand{\bibsection}{}`
  para no duplicar el encabezado `\section{References}`. Las 17 citas del cuerpo pasaron
  de texto a `\citep` (parentesis), `\citet` (autor + anio en linea) y `\citealp`
  (dentro del parentesis de C1). La lista a mano se borro entera. Compila con
  `pdflatex; bibtex; pdflatex; pdflatex` desde `tesis/`: 0 citas indefinidas, 27
  `\bibitem` en el `.bbl` y las citas del cuerpo impresas igual que antes. Lo que
  cambia de aspecto es la lista: 3 paginas en vez de 2, y 11 entradas la sostiene
  `\nocite{*}`. Las dos cosas estan en Pendientes abiertos.
- **`.gitignore`: LIMPIADO** el 2026-09-07. Se quitaron el `@'` de la primera linea y
  el `'@ | Set-Content -Encoding utf8 .gitignore` de la ultima, restos de un here-string
  de PowerShell que se escribio en vez de ejecutarse. Reglas verificadas con
  `git check-ignore -v`: `papers/`, `data/`, `*.nii.gz` y `*.bbl` se ignoran;
  `refs/raw/*.bib` no.
- **LNCS: IGNORADOS por decision de la autora** el 2026-09-07. Los tres volumenes
  (`jacob2026lgesynthnet`, `ramzan2026claim`, `wang2019cochlear`) no se persiguen en
  otra fuente. Sus valores salieron de `refs/MAPEO.md` para que nadie los reintroduzca
  sin respaldo en `refs/raw/`; ahi queda solo la decision y el motivo (el exportador de
  Springer no trae `series` ni `volume`).
- **`main.tex`, lista de referencias actualizada** el 2026-09-07 con autorizacion
  explicita: 15 correcciones (revistas completas, fasciculos, paginas de las tres
  actas, volumen de SPIE). Sigue en texto plano; no se migro a BibTeX.


## Deudas asumidas
- Leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion:
  la metrica SAP depende de la definicion de grados de brecha cortical.
