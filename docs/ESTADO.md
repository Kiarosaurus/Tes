# Estado actual

> Lo actualiza Claude al cerrar cada sesion. Fuente de verdad de "por donde voy".

## Ultimo paso completado
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
- `refs.bib`: los comentarios `% VERIFICAR` quedaron obsoletos. Las 28 lineas siguen
  diciendo «falta DOI» cuando el DOI ya esta puesto. Solo la autora puede tocar ese
  archivo: hay que borrar esas lineas o reescribirlas con lo que de verdad falta.
- `refs.bib`, campos que siguen ausentes: volumen en `deman2007catsim` (SPIE, puede no
  tenerlo), numero en `liu2021ctpelvic1k` y `xie2024implantsegmentation`. Verificar si
  esas revistas usan numero antes de darlos por faltantes.
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
- Dos verificaciones de #13 no son bibliograficas y nadie las bloquea: ver si CLINIC-metal
  amplio su anotacion desde 2021, y mirar los volumenes para saber que metal contienen.
- `wang2025adaptiveweighting`: unico N1 SIN VERIFICAR, tercera ronda bloqueado por el PDF.
- Faltan por verificar tambien:
  `arand2019pelvicring` y `xie2024implantsegmentation`.
- `SAP`, `BFC` e `ISC` siguen sin definir en `docs/03-glosario.md`. El nivel de
  `xie2024implantsegmentation` y el de `liu2025pipeline` dependen de esas definiciones.
- `tesis/main.tex` sigue con la bibliografia en texto plano dentro de `multicols`;
  migrar a `\bibliography{refs}` es decision de la autora (no se toco).

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
- **`refs.bib`: los 27 DOIs, PUESTOS.** Las 27 entradas tienen `doi` y se completaron
  los campos que faltaban: paginas en `jacob2026lgesynthnet` (34--44), `ramzan2026claim`
  (279--292) y `wang2019cochlear` (121--129); numero en `singhrao2024fiducial`,
  `smith2006iliosacral`, `vanbosse2011pelvicpositioning` y `yun2026simulationdriven`.
  El archivo lo escribe la autora; el asistente no lo toco. Queda solo limpiar los
  comentarios `% VERIFICAR`, ya obsoletos.


## Deudas asumidas
- Leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion:
  la metrica SAP depende de la definicion de grados de brecha cortical.
