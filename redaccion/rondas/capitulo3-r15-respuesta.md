# capitulo3 — r15: respuesta del redactor (modo corregir)

Archivos editados: `overleaf/secciones/capitulo3.tex`, `redaccion/MAPA.md`. No se tocaron `tesis/main.tex` ni otros
capitulos. No se escribio ninguna cifra de #164 (modelo afectado) ni de la corrida final con run04 (en curso).
Fuentes nuevas leidas: `docs/00-tesis.md` bloque Obj 3 (incluida la diferencia sin commit: "la corrida final de test
sigue en curso"; "entrenado despues del congelamiento y antes de la enmienda"), #171 (correccion 2026-10-11), #172,
DEC 2026-10-11 (1)-(4), `docs/02-datos.md` actualizacion 2026-10-11, `docs/ESTADO.md`:14 (`a16` recalibrando,
decision de la autora), `EXPERIMENTOS.md`:68, :76-78.

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 (alta) | guia | APLICADO | §Amenazas, validez interna, ultimo parrafo: el sentido de las tres elecciones esta registrado y es el mismo (punto de control: amplitud mas cercana a Ti y margen mas ancho, 163.8 frente a 100.3 HU; material; margen). Se declara el sesgo hacia concluir equivalencia y que las sensibilidades examinan cada eleccion por separado, ninguna el efecto conjunto. `\GAPDEC` retirado (la orden del orquestador y #171 corregida lo cubren) |
| T04 | trazabilidad | APLICADO | Mismo cambio que guia-1 |
| guia-2 | guia | APLICADO | Parrafo propio sobre la evaluacion previa de la prueba: las cinco decisiones posteriores (reentrenamiento, punto de control, sensibilidad, margen, retiro de 3 componentes) se fijaron con el resultado de prueba visto y pudieron orientarse por el; tres aplican reglas previas, dos no; la sensibilidad es la lectura conservadora y los componentes estaban identificados desde #109. Sin cifras de #164 |
| S2 | estilo | APLICADO | "esos resultados" sustituido por "ese resultado de prueba", con la consecuencia explicita |
| T07 | trazabilidad | APLICADO | La lista incluye la sensibilidad con el estado final y el retiro de los tres componentes como decisiones sin regla previa |
| guia-3 | guia | APLICADO | La sensibilidad con el estado final entra en la enumeracion de decisiones posteriores a validacion, con su motivo (distancia dentro de `M`) |
| S1 | estilo | APLICADO | El parrafo de 15 oraciones se parte en cuatro: decisiones posteriores a validacion del flujo de evaluacion; las del cotejo y el comparador; la regla de realismo; la evaluacion previa con el modelo afectado. Apertura sin recuento ("varias decisiones") |
| guia-4 | guia | APLICADO | §Brazos: la medicion que motivo el cambio de material se hizo "con un modelo afectado"; con el modelo evaluado "esa cercania se mantiene", y siguen las cifras de run04. Sin cifras del modelo archivado |
| T06 | trazabilidad | APLICADO | Mismo cambio que guia-4 |
| guia-5 | guia | APLICADO | "el unico parametro heredado" retirado. Se enumera lo fijado con los modelos afectados: ancho de cascara, eleccion por cotejo y no por la perdida, limite de la lectura de HU (en recalibracion), y la observacion que motivo la regla del material. El salto de borde ya dice en su parrafo que se midio con otro punto de control |
| T05 | trazabilidad | APLICADO | Mismo cambio que guia-5 |
| S5 | estilo | APLICADO | Un solo nombre: "modelos afectados" se define en §Sintetizador como todos los modelos anteriores al reentrenamiento, entrenados con el volumen compartido; con uno de ellos se evaluo la prueba. §Sintetizador (lectura de HU), §cascaras, §Brazos y §Amenazas usan ese nombre |
| guia-6 | guia | APLICADO | `\GAPDEC` de §Sintetizador retirado. Se escribe la frase decidida (#171 corregida; `00-tesis.md`): la sensibilidad con el estado final es la lectura conservadora; medianas entre semillas 749/1076 frente a 977/1238 HU; Ti 2051/1279 HU; el elegido, fijado sin usar el protocolo fisico, es el mas cercano |
| T03 | trazabilidad | APLICADO | Mismo cambio que guia-6 |
| guia-7 | guia | APLICADO (parcial, como T10) | La prosa dice que la simulacion sobre los 13 ya se corrio y no depende del sintetizador; el `\GAPDATO` se reduce a la evaluacion de su amplitud, que se hace con la corrida final. Se mantiene marca porque `docs/ESTADO.md` da pendiente el `a20` de test sobre `a19_final` (manda trazabilidad) |
| guia-8 | guia | APLICADO | Recuentos de DEC 2026-10-11 (4) y `02-datos.md`: §Datos (166 volumenes = 159 pacientes; 118/125, 8, 33; test 20 + 13 y 9/10/14; grupos.csv 59/41/66 por volumen); §Sintesis 19 = 9 + 10; §Reconstruccion cohorte de diseno 19, n efectivo 13 = 9 + 4 por el umbral de 500 mm3; Tabla "13 de los 19". `\GAPDEC` de §Datos retirado |
| T02 (alta) | trazabilidad | APLICADO | Mismo cambio que guia-8. Ademas: "Los 64 pacientes con material ortopedico" (§Datos, cuatro funciones) pasa a "Los pacientes con material ortopedico"; §Marco-metal conserva los 64 del analisis y dice que son del recuento anterior a las auditorias; `\GAPDATO` de la referencia de realismo sin el "11"; §Amenazas: "3 de los 11 pacientes de prueba que entonces se contaban con material" (DEC 2026-10-09 (7), hecho historico) |
| guia-9 | guia | APLICADO | §Marco-metal: "componente que, solo por su forma, es candidato a tornillo transiliaco-transsacro", y el conteo de la autora no halla ninguno en CLINIC-metal (remision a §Amenazas) |
| S16 | estilo | APLICADO | §Amenazas, validez externa: remision a §Geometria ("lo son solo por su forma"); quitado "que conto" |
| T01 (alta) | trazabilidad | APLICADO | "se regeneraron con el los resultados" sustituido: con el modelo reentrenado se repitieron eleccion del punto de control, margen y valor de copia y pegado; la corrida final, todavia en curso, se hace solo con el (`EXPERIMENTOS.md`:76-78; `00-tesis.md` corregido) |
| T08 | trazabilidad | APLICADO | El 0.62 lleva la condicion: medido en el conjunto anterior a los retiros |
| S3 | estilo | APLICADO | Las dos oraciones del rediseno del Obj 3 y la regla de la compuerta pasan al parrafo de la compuerta (§Obj 1), fundidas en una |
| S4 | estilo | APLICADO | "Su evaluacion sigue el diseno congelado el 9 de octubre y enmendado el 11; el modelo evaluado se entreno antes de esa enmienda, que no fija su entrenamiento" (coincide con `00-tesis.md`, T09) |
| S6 | estilo | APLICADO | Se mantienen "dos tipos de unidades" (secundarios y componentes) y el paciente compartido abre parrafo propio. La mencion del 0.05 en ese parrafo se conserva, abreviada ("el limite de la lectura de HU, hoy en recalibracion"), porque guia-5/T05 piden enumerar lo heredado (manda rubrica sobre estilo) |
| S7 | estilo | APLICADO | Igual que T08 |
| S8 | estilo | APLICADO | "mide el error de la prediccion $v$" |
| S9 | estilo | APLICADO | "el cotejo no identifica un numero optimo de pasos"; el parrafo de dos oraciones sobre los 39 casos se funde al final del de entrenamiento, sin "no se afirma" |
| S10 | estilo | APLICADO | "principal" para el punto de control o el margen retirado del §Sintetizador y §Analisis: "el de 163.8 HU", "obtenido con el elegido". El GAPDEC que lo usaba ya no existe |
| S11 | estilo | APLICADO | "compartida con otros procesos de computo" (no "otros usuarios": la fuente no dice de quien son) |
| S12 | estilo | APLICADO | Semillas y tarjeta grafica en parrafo propio tras el de arquitectura |
| S13 | estilo | APLICADO | La justificacion del ancho de 1 mm pasa al parrafo donde se define la cascara; el parrafo del cotejo abre con el resultado; quitado "Ese es el punto de control que pasa a la evaluacion" |
| S14 | estilo | APLICADO | "En validacion, el sintetizador subestima..." y "queda bajo lo real en validacion" |
| S15 | estilo | APLICADO | Eliminada "Es una debilidad reconocida del diseno y no una victoria del metodo" |

## Hallazgos de severidad baja

| Hallazgo | Decision | Detalle |
|---|---|---|
| guia-10 | APLICADO | Igual que T08 |
| S17 | APLICADO | "Su distancia a la mediana real de esos dos percentiles"; quitada la repeticion de que la regla no la usa |
| S18 | APLICADO | "que el estado final" |
| S19 | APLICADO | Sin apertura por recuento; cada hallazgo abre con su contenido |
| S20 | APLICADO | "valores de HU mas bajos que los reales"; "una *streak amplitude* menor"; en §Amenazas "una *streak amplitude* mas cercana" |
| S21 | APLICADO | "ella los ubica en general fuera del cuerpo, sin un recuento por objeto" (#167 no da recuento) |
| S22 | APLICADO | "Se asume tambien" |
| S23 | APLICADO | Eliminada |
| T09 | sin cambio | El texto ya era correcto; la fuente (`00-tesis.md`) ya se corrigio (punto 4 del orquestador) |
| T11 | sin cambio | Por indicacion del orquestador: la columna de la autora dice 0; "0 de 56" se mantiene |

## Fuente de cada cifra nueva o movida

| Cifra | Ubicacion | Fuente |
|---|---|---|
| 166 volumenes, 159 pacientes; 118 (125), 8, 33; 20 + 13; 9/10/14 | §Datos | DEC 2026-10-11 (4) pto 2; `02-datos.md` tabla 2026-10-11 |
| 59/41/66 (grupos.csv, por volumen); 7 secundarios | §Datos | `02-datos.md` 2026-10-11; DEC 2026-10-11 (4) pto 1 |
| Primario `0072` (test), sale `0003` | §Datos | DEC 2026-10-11 (regla de espaciado) |
| 19 = 9 + 10; n efectivo 13 = 9 + 4; 6 de dataset6 sin componentes >= 500 mm3 | §Sintesis, §Reconstruccion, Tabla | DEC 2026-10-11 (4) pto 3; `00-tesis.md` Obj 3 |
| 749/1076 y 977/1238 HU (medianas entre semillas); 2051/1279 HU | §Sintetizador | #171 correccion; `00-tesis.md` "Sensibilidad de checkpoint" |
| 163.8 frente a 100.3 HU | §Amenazas | DEC 2026-10-11 (3) pto 3 (ya en §Analisis) |
| 11 pacientes "que entonces se contaban con material" | §Amenazas | DEC 2026-10-09 (7) "Motivo" |

## Ajustes colaterales minimos

- Lint E-O1 (oraciones > 40 palabras) aparecio en 13 oraciones nuevas o fusionadas; se partieron todas. Para no pasar
  de 7 oraciones por parrafo (PAT-58) se fundieron dos oraciones en §Brazos (cortes simulados en la primera) y en
  §Sintetizador (lectura de HU, con punto y coma).
- §Marco-metal: los 64 pacientes se conservan como cohorte de ese analisis, con la condicion de recuento, para que
  no choquen con los 59 de §Datos.

## GAP

- Cerrados: `\GAPDEC` recuentos de §Datos; `\GAPDEC` sentido de la eleccion del punto de control frente al
  protocolo fisico; `\GAPDEC` efecto conjunto de las tres elecciones (sesgo declarado); `\GAPDEC` del limite de
  0.05, que pasa a `\GAPDATO` (recalibracion en curso, #172).
- Abiertos: `\GAPDATO` del limite de la lectura de HU calibrado con el modelo evaluado (sustituye al `\GAPDEC`).
- Reformulados: `\GAPDATO` del protocolo fisico sobre los 13 (evaluacion de su amplitud); `\GAPDATO` de la
  referencia de realismo (sin el "11").
- Totales del lint: 2 `\GAPLIT`, 14 `\GAPDATO`, 15 `\GAPDEC` (antes 2/13/19). Ningun `\GAPLIT` nuevo:
  `_candidatos.md` no cambia.

## Lint

`python scripts/lint_redaccion.py capitulo3 --compilar`: **PASA**, alta 0, media 0, baja 14 (E-P1, cifras sin cita
en la linea; preexistentes o con fuente en esta tabla). Compila: `redaccion/.build/main.pdf`, 134 paginas.

## Para la autora (sin editar nada fuera del capitulo)

1. `docs/02-datos.md` y DEC 2026-10-11 (4) no dan los pacientes por grupo, solo los volumenes de `grupos.csv`
   (59/41/66, con los 7 secundarios). El capitulo da los volumenes y lo dice; no se calculo el recuento por paciente.
2. §Datos (cuatro funciones del grupo 1) sigue diciendo "el unico paciente adquirido dos veces sin cambios en el
   implante"; con #156 (`0053` = `0054`, mismo implante) y `reproducibilidad` = 3 en `grupos.csv`, esa frase puede
   haber envejecido. Nadie la senalo y no se toco.
3. Si `a16` con run04 no da 0.05, cambian el cotejo, el margen y la corrida final (`docs/ESTADO.md`:14), y con ellos
   las cifras del §Sintetizador, §Analisis y la Tabla de diseno.

## Decisiones de redaccion

- **"Modelos afectados"** (plural, en negrita al definirse en §Sintetizador) = todos los modelos anteriores al
  reentrenamiento, entrenados con el volumen compartido entre particiones. "Un modelo afectado" cuando se habla de
  uno (la evaluacion previa de la prueba, la medicion que motivo el material). Sustituye a "modelo anterior al
  reentrenamiento" y "modelo anterior" como nombres paralelos.
- **Parametros heredados se enumeran, no se resumen con "el unico"**: si un elemento del metodo se fijo con un modelo
  retirado, se nombra cada uno y se dice si se recalibra.
- **Cronologia de una decision motivada por un modelo retirado**: la observacion se atribuye a ese modelo sin sus
  cifras, y las cifras del modelo vigente entran como "se mantiene" (comprobacion posterior), no como motivo.
- **Recuentos por grupo de `grupos.csv` se dan como volumenes**, con la razon (conserva los secundarios), mientras no
  haya recuento de pacientes por grupo registrado.
- **Cohorte de diseno frente a n efectivo**: se dan las dos, con la causa de la diferencia (umbral previo de 500 mm3).
