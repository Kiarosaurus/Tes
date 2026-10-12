# Respuesta del redactor — capitulo3 — r16

Entrada: `capitulo3-r16-{lint,guia,estilo,trazabilidad}.md` y las notas del orquestador (1-8). Fuentes que releí:
`experiments/objetivo1/p1_sin_0072.md`, IMP #156, #162 (3), #163, #166 (con la adenda en #172), #172,
`docs/02-datos.md` (actualizacion 2026-10-11), DEC 2026-10-11 y 2026-10-09 (4), `docs/ESTADO.md`:14 y BITACORA §2.
Los cruces con `introduccion.tex` (guia, cobertura G-C4) quedan fuera de alcance, como indica la nota 8.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Nuevo parrafo en §Datos, tras el del paciente compartido. El paciente compartido tambien afecta a la compuerta: la variante adaptada se ajusto con volumenes de entrenamiento, entre ellos el retirado, y se evaluo en el de prueba. La fuga solo favorece un aprobado. Con n = 32 (sin `0053` ni `0072`), la mejor combinacion da 61.08 HU, IC 95 % de 54.23 a 68.57 HU, y el veredicto no cambia (`p1_sin_0072.md`, copiado). En §Obj 1 (l. 77), "separados de los de prueba" pasa a "dos de ellos resultaron ser despues otras adquisiciones de pacientes de prueba". En la validez interna del Obj 1 se dice que la fuga solo favorece un aprobado y que sin esos dos pacientes el veredicto no cambia. Ya no hace falta `\GAPDATO`: la sensibilidad existe |
| guia-2 | guia | APLICADO | En §Sintetizador (lectura de HU): "El cotejo del punto de control y el margen $\Delta$ se calcularon con 0.05, la corrida final lo usa, y los tres dependen de ese limite" (ESTADO:14; #172). En §Amenazas, la recalibracion entra en la lista de decisiones posteriores a la evaluacion previa, entre las que aplican un criterio registrado antes (el de 0.05, l. 198). Pasan a ser cuatro con criterio previo y dos sin el. No hay valor nuevo |
| guia-3 | guia | APLICADO (con T02) | "El unico paciente adquirido dos veces" pasa a "un paciente cuyas dos adquisiciones conservan el mismo implante". Se anade que las demas adquisiciones repetidas son secundarias o salieron de las cohortes, con remision a §Datos |
| S1 | estilo | APLICADO | `\emph{streak amplitude}` (nota 6) |
| S2 | estilo | APLICADO | La condicion va al abrir el recuento ("En la primera auditoria, ... agruparon"). Se quita el cierre que anunciaba el parrafo siguiente |
| S3 | estilo | APLICADO | Nombre unico: **auditorias de identidad de paciente**, en negrita en §Datos. La l. 208 ya no las nombra: remite (S4) |
| S4 | estilo | APLICADO | §Sintetizador abre ahora con la remision: "El paciente compartido entre entrenamiento y prueba (Seccion datos) obligo a reentrenar el sintetizador". El caso solo se cuenta en §Datos |
| S5 | estilo | APLICADO | "La regla que elige los tornillos reales de prueba del contraste de realismo" |
| S6 | estilo | APLICADO | "autoencoder del generador de volumenes de TC de Guo et al., entrenado con TC" (l. 83); "autoencoder de Guo et al." en validez interna y en la de la conclusion |
| S7 | estilo | APLICADO | Al cierre de la regla de la compuerta: "Tras el veredicto negativo, el Objetivo 3 se rediseno en el dominio de imagen (...), sin modificar la regla de la compuerta" |
| S8 | estilo | APLICADO | "que en el recuento de la primera auditoria reune 66 pacientes" |
| S9 | estilo | APLICADO | Igual que T04 (nota 7) |
| S10 | estilo | APLICADO | "y no es la tarea que decide el Objetivo 3" |
| S11 | estilo | APLICADO | Se quita la 2.a oracion. El parrafo cierra con "La sensibilidad con el estado final es, por eso, la lectura conservadora: enfrenta al protocolo fisico una amplitud mas alejada de la suya" (749/1076 frente a 977/1238; Ti 2051/1279 HU, sin cambio) |
| S12 | estilo | APLICADO | Se fusionaron las oraciones 4.a y 5.a. Despues el lint marco 42 palabras (E-O1), asi que se partio de nuevo en "Se mide la discrepancia ... Se miden con ella las dos metricas ...". El parrafo baja de 8 a 7 oraciones |
| S13 | estilo | APLICADO | Fusion propuesta: "la imagen generada por el sintetizador y por el protocolo fisico se compara..." |
| S14 | estilo | APLICADO | "El protocolo fisico sobre esos 13 pacientes ya se corrio, porque no depende del sintetizador. Su amplitud se evalua...": se partio en dos por E-O1 |
| S15 | estilo | APLICADO | El dato de 1.6 mm pasa a §Sintetizador, tras "no alcanzan ese criterio". Se copio sin cambiar su contenido (DEC 2026-10-09 (4): "`0019` no cabe: corredor de 1.6 mm") |
| S16 | estilo | APLICADO | Dos oraciones. La del ancho de cascara dice "antes de entrenar el modelo evaluado". La del material dice "despues de ver en validacion las amplitudes de los dos materiales, con una regla que no usa el sintetizador" (l. 319). Se rompe la apertura "En el ..." repetida |
| S17 | estilo | APLICADO | Se elimina la oracion repetida "El sesgo que introducen ... va, por tanto, hacia concluir equivalencia". El sentido sigue dicho como hecho en la 3.a oracion |
| S18 | estilo | APLICADO | El parrafo se parte. El nuevo abre con "Se asume, ademas, que la apariencia de un artefacto metalico puede generarse en el dominio de imagen..." |
| T01 | traza | APLICADO | Sin orden (nota 2): "tenia un volumen en entrenamiento y otro en prueba, adquiridos antes y despues de la cirugia". La l. 208 tampoco da orden. Para la autora: `docs/02-datos.md`:146 enumera el par en un orden que puede leerse al reves; ese archivo no lo puedo editar |
| T02 | traza | ESCALADO | Las fuentes no coinciden: #156 dice que `0053` lleva el implante femoral y #163, que `0054` lleva el clavo femoral. Lo que es cierto en ambas versiones queda en prosa: el paciente tiene tres adquisiciones y una lleva ademas un implante femoral. Si queda dentro o fuera de las cohortes va a `\GAPDEC`, que cita las dos implicancias. No elijo version (nota 3). Ya no se afirma "esa adquisicion queda fuera" |
| T03 | traza | ESCALADO | El sentido de las tres elecciones sigue como hecho. Al final del parrafo se repone `\GAPDEC{si, ademas de declarar el sentido conjunto ..., se reporta la prueba de equivalencia con un margen no fijado por el sintetizador como sensibilidad descriptiva anadida despues del congelamiento (implicancia 162)}`. Asi lo pide BITACORA §2 2026-10-10 (nota 4) |
| T04 | traza | APLICADO | "Ninguna cifra que este documento presenta proviene de un modelo afectado" (formulacion de #171, nota 7) |

Bajos aplicados: guia-4 (= T04), guia-5 (se da el 64 "que quedaban tras retirar la adquisicion repetida con el mismo
implante pelvico, antes del recuento del 11 de octubre"), T05 (§Datos dice "el recuento del 11 de octubre, que las
aplica", no fecha las auditorias), T06 ("De los 103 pacientes sin osteosintesis de la primera auditoria"), S19
(oracion del rediseno quitada de l. 66; queda en S7), S21 ("mas cerca ... con titanio que con hierro"), S22 (se
nombran la sensibilidad con el estado final y el retiro de los componentes), S23 (apertura sin recuento), S24
(cierre quitado), S25, S26 (se cierra con "Ninguna de las cifras se transfiere, por tanto, a otra coleccion o
reconstruccion sin comprobarse", partida en oracion propia por E-O1). Bajo no aplicado: S20 ("porcion" de la
tarjeta grafica). "Particion" choca con la particion de datos, y el nombre tecnico de la division por hardware no
consta en una fuente que pueda citar sin anadir contenido.

Correccion lateral: la lista post hoc de §Amenazas paso de 41 a 44 palabras al sumar la recalibracion (E-O1). Se
partio en "se fijaron seis decisiones: ... Se fijaron tambien ...".

Lint final: PASA (alta 0, media 0, baja 12 E-P1); compila, 135 paginas. GAP capitulo3: 2 `\GAPLIT`, 14 `\GAPDATO`,
17 `\GAPDEC` (+2 `\GAPDEC`: implante femoral, T02; sensibilidad con margen no fijado por el sintetizador, T03).

## Para la autora

1. **Implante femoral (T02):** que adquisicion lo lleva, `0053` (#156, fuera de cohortes) o `0054` (#163, primaria
   de entrenamiento).
2. **#162 (3), opcion (b):** si se reporta la prueba de equivalencia con un margen no fijado por el sintetizador,
   como sensibilidad descriptiva posterior al congelamiento.
3. `docs/02-datos.md`:146 puede reescribirse sin orden implicito para el par `0003`/`0072` (T01).

## Decisiones de redaccion

- **Nombre unico del procedimiento:** "auditorias de identidad de paciente" para las revisiones que unen
  adquisiciones del mismo paciente. Va en negrita en §Datos. Otras secciones lo retoman o remiten; no se usa
  "de mismo paciente" ni "de pacientes duplicados".
- **Fuga entre particiones:** se declara en cada objetivo que uso la particion afectada (aqui, Obj 1 y Obj 3). En cada
  uno se dice que puede favorecer y que hace su sensibilidad, con la cifra copiada del experimento.
- **Dos implicancias que se contradicen en un detalle de datos:** la prosa conserva lo que es cierto en las dos
  versiones. La discrepancia va a `\GAPDEC` y cita ambas implicancias, sin elegir.
- **Parametro en recalibracion:** se dice que cifras dependen de el, y la recalibracion entra en la lista de
  decisiones posteriores a la evaluacion previa.
